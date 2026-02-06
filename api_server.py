"""
EduCode Code Smell Detection API Server
========================================
REST API for Unity integration - Converts Java code analysis into
building metrics for 3D city visualization.

Run with: python api_server.py
API runs on: http://localhost:5000

Endpoints:
- POST /analyze/code       - Analyze single Java code snippet
- POST /analyze/file       - Analyze a single .java file
- POST /analyze/repo       - Analyze all Java files in a directory
- POST /analyze/github     - Clone and analyze a GitHub repository
- GET  /health             - Health check endpoint
"""

import os
import sys
import json
import tempfile
import shutil
import subprocess
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any
from flask import Flask, request, jsonify
from flask_cors import CORS

# Import our smell detection module
import predict_smell_extended as detector

app = Flask(__name__)
CORS(app)  # Enable CORS for Unity WebGL builds

# Load models once at startup
print("Loading ML models...")
MODELS = detector.load_models()
print("✓ Models loaded!")

# ═══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES FOR UNITY
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class BuildingMetrics:
    """Metrics for a single building (class) in the city"""
    class_name: str
    file_path: str
    
    # Code quality color (single int: 0xRRGGBB)
    color: int             # Combined RGB as integer (e.g., 0x33CC4D for green)
    quality_score: float   # 0.0 (bad) to 1.0 (clean)
    
    # Primary smell
    primary_smell: str
    smell_confidence: float
    
    # All detected smells
    all_smells: List[Dict[str, Any]]
    
    # Raw metrics
    loc: int
    wmc: int
    cbo: int
    dit: int
    rfc: int
    lcom: float
    
    # Recommendations
    recommendations: List[str]


@dataclass 
class CityLayout:
    """Complete city data for Unity"""
    buildings: List[BuildingMetrics]
    
    # Relationships for connections
    inheritance: List[Dict[str, str]]    # Bridges
    associations: List[Dict[str, str]]   # Roads
    compositions: List[Dict[str, str]]   # Annexes
    dependencies: List[Dict[str, str]]   # Utility lines
    aggregations: List[Dict[str, str]]   # Courtyards
    
    # Summary stats
    total_classes: int
    clean_count: int
    smell_count: int
    average_quality: float


# ═══════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def get_quality_color(smell: str, confidence: float) -> tuple:
    """
    Returns RGB color (0-1) based on code quality.
    Green = clean, Yellow = minor issues, Red = major smells
    """
    if smell == "Clean":
        return (0.2, 0.8, 0.3)  # Green
    
    # Color based on smell severity
    severity_colors = {
        "LongMethod": (1.0, 0.6, 0.0),      # Orange
        "GodClass": (0.9, 0.1, 0.1),        # Red
        "DataClass": (0.7, 0.5, 0.0),       # Brown/Orange
        "FeatureEnvy": (0.8, 0.4, 0.0),     # Dark Orange
        "DeadCode": (0.5, 0.5, 0.5),        # Gray
        "MagicNumbers": (0.9, 0.7, 0.0),    # Yellow
        "SwallowedException": (0.8, 0.2, 0.2), # Dark Red
        "GlobalMutableState": (0.7, 0.2, 0.5), # Purple
        "BadNaming": (0.6, 0.6, 0.0),       # Olive
        "GodMethod": (0.9, 0.2, 0.0),       # Red-Orange
    }
    
    return severity_colors.get(smell, (1.0, 0.5, 0.0))  # Default orange


def calculate_quality_score(result) -> float:
    """Calculate overall quality score 0.0 (worst) to 1.0 (best)"""
    if result.primary_smell == "Clean":
        return 1.0
    
    # Reduce score based on number and severity of smells
    score = 1.0
    severe_smells = {"GodClass", "GodMethod", "SwallowedException"}
    medium_smells = {"LongMethod", "FeatureEnvy", "GlobalMutableState"}
    
    for smell, conf in result.all_smells:
        if smell == "Clean":
            continue
        if smell in severe_smells:
            score -= 0.3 * conf
        elif smell in medium_smells:
            score -= 0.2 * conf
        else:
            score -= 0.1 * conf
    
    return max(0.0, min(1.0, score))


def extract_class_name(code: str, file_path: str = "") -> str:
    """Extract class name from Java code or filename"""
    import re
    
    # Try to find class declaration
    match = re.search(r'(?:public\s+)?class\s+(\w+)', code)
    if match:
        return match.group(1)
    
    # Fall back to filename
    if file_path:
        return Path(file_path).stem
    
    return "UnknownClass"


def analyze_code_for_building(code: str, file_path: str = "") -> BuildingMetrics:
    """Analyze Java code and return building metrics for Unity"""
    
    # Run smell detection
    result = detector.predict_smell(code, MODELS, use_extended=True)
    
    # Calculate building dimensions from metrics
    metrics = result.details.get("metrics", {})
    loc = metrics.get("LOC", len(code.split('\n')))
    wmc = metrics.get("WMC", 5)
    methods = metrics.get("METHODS", 1)
    fields = metrics.get("FIELDS", 0)
    cbo = metrics.get("CBO", 0)
    dit = metrics.get("DIT", 0)
    rfc = metrics.get("RFC", methods)  # Default to methods count if not calculated
    lcom = metrics.get("LCOM", 0.0)
    
    # Get quality color and convert to single int
    color_rgb = get_quality_color(result.primary_smell, result.primary_confidence)
    color_int = (int(color_rgb[0] * 255) << 16) | (int(color_rgb[1] * 255) << 8) | int(color_rgb[2] * 255)
    quality = calculate_quality_score(result)
    
    # Format all smells for Unity
    all_smells = []
    for smell, conf in result.all_smells:
        all_smells.append({
            "name": smell,
            "confidence": round(conf, 3),
            "is_primary": smell == result.primary_smell
        })
    
    # Add extended smells with descriptions
    for smell, conf, desc in result.details.get("extended_smells", []):
        # Check if already in list
        existing = [s for s in all_smells if s["name"] == smell]
        if existing:
            existing[0]["description"] = desc
        else:
            all_smells.append({
                "name": smell,
                "confidence": round(conf, 3),
                "is_primary": False,
                "description": desc
            })
    
    # Get recommendations
    recommendations = []
    smell_recommendations = {
        'GodClass': 'Split into smaller, focused classes (Single Responsibility)',
        'LongMethod': 'Break down into smaller methods with clear names',
        'DataClass': 'Move behavior to this class or use a record/struct',
        'FeatureEnvy': 'Move this method to the class it uses most',
        'DeadCode': 'Remove unused code to improve maintainability',
        'MagicNumbers': 'Replace magic numbers with named constants',
        'SwallowedException': 'Log or handle exceptions properly',
        'GlobalMutableState': 'Use encapsulation and dependency injection',
        'BadNaming': 'Use descriptive, meaningful names',
        'GodMethod': 'Split method into smaller focused methods',
        'DuplicateCode': 'Extract duplicate logic into reusable methods',
        'RawCollections': 'Add generic type parameters to collections',
    }
    
    seen_smells = set()
    for smell, _ in result.all_smells:
        if smell != "Clean" and smell not in seen_smells:
            if smell in smell_recommendations:
                recommendations.append(smell_recommendations[smell])
            seen_smells.add(smell)
    
    return BuildingMetrics(
        class_name=extract_class_name(code, file_path),
        file_path=file_path,
        color=color_int,
        quality_score=round(quality, 3),
        primary_smell=result.primary_smell,
        smell_confidence=round(result.primary_confidence, 3),
        all_smells=all_smells,
        loc=loc,
        wmc=wmc,
        cbo=cbo,
        dit=dit,
        rfc=rfc,
        lcom=round(lcom, 3) if isinstance(lcom, float) else lcom,
        recommendations=recommendations
    )


def extract_relationships(java_files: Dict[str, str]) -> Dict[str, List[Dict]]:
    """
    Extract relationships between classes for city connections.
    Returns inheritance, associations, compositions, dependencies, aggregations.
    """
    import re
    
    relationships = {
        "inheritance": [],
        "associations": [],
        "compositions": [],
        "dependencies": [],
        "aggregations": []
    }
    
    # Build class name to file mapping
    class_names = set()
    for path, code in java_files.items():
        match = re.search(r'(?:public\s+)?class\s+(\w+)', code)
        if match:
            class_names.add(match.group(1))
    
    for path, code in java_files.items():
        # Get current class name
        class_match = re.search(r'(?:public\s+)?class\s+(\w+)', code)
        if not class_match:
            continue
        current_class = class_match.group(1)
        
        # INHERITANCE: extends keyword -> Bridges
        extends_match = re.search(r'extends\s+(\w+)', code)
        if extends_match:
            parent = extends_match.group(1)
            if parent in class_names:
                relationships["inheritance"].append({
                    "from": current_class,
                    "to": parent,
                    "type": "extends"
                })
        
        # IMPLEMENTS -> Also bridges
        implements_match = re.search(r'implements\s+([\w\s,]+)', code)
        if implements_match:
            interfaces = [i.strip() for i in implements_match.group(1).split(',')]
            for iface in interfaces:
                if iface in class_names:
                    relationships["inheritance"].append({
                        "from": current_class,
                        "to": iface,
                        "type": "implements"
                    })
        
        # COMPOSITION: Private final fields of other classes -> Annexes
        comp_pattern = r'private\s+final\s+(\w+)\s+\w+\s*[;=]'
        for match in re.finditer(comp_pattern, code):
            field_type = match.group(1)
            if field_type in class_names and field_type != current_class:
                relationships["compositions"].append({
                    "from": current_class,
                    "to": field_type
                })
        
        # AGGREGATION: Private non-final fields -> Shared Courtyards
        agg_pattern = r'private\s+(?!final)(\w+)\s+\w+\s*[;=]'
        for match in re.finditer(agg_pattern, code):
            field_type = match.group(1)
            if field_type in class_names and field_type != current_class:
                relationships["aggregations"].append({
                    "from": current_class,
                    "to": field_type
                })
        
        # ASSOCIATION: Public fields or method params -> Roads
        assoc_pattern = r'public\s+(\w+)\s+\w+\s*[;=\(]'
        for match in re.finditer(assoc_pattern, code):
            field_type = match.group(1)
            if field_type in class_names and field_type != current_class:
                relationships["associations"].append({
                    "from": current_class,
                    "to": field_type
                })
        
        # DEPENDENCY: new ClassName() or method calls -> Utility Lines
        new_pattern = r'new\s+(\w+)\s*\('
        for match in re.finditer(new_pattern, code):
            created_type = match.group(1)
            if created_type in class_names and created_type != current_class:
                # Avoid duplicates with composition
                existing_comp = [c for c in relationships["compositions"] 
                               if c["from"] == current_class and c["to"] == created_type]
                if not existing_comp:
                    relationships["dependencies"].append({
                        "from": current_class,
                        "to": created_type
                    })
    
    # Remove duplicates
    for rel_type in relationships:
        seen = set()
        unique = []
        for rel in relationships[rel_type]:
            key = (rel["from"], rel["to"])
            if key not in seen:
                seen.add(key)
                unique.append(rel)
        relationships[rel_type] = unique
    
    return relationships


def clone_github_repo(repo_url: str) -> str:
    """Clone a GitHub repository and return the temp directory path"""
    temp_dir = tempfile.mkdtemp(prefix="educode_")
    
    try:
        # Clone the repository
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, temp_dir],
            check=True,
            capture_output=True,
            text=True
        )
        return temp_dir
    except subprocess.CalledProcessError as e:
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise Exception(f"Failed to clone repository: {e.stderr}")


def find_java_files(directory: str) -> Dict[str, str]:
    """Find all .java files in a directory and return path -> code mapping"""
    java_files = {}
    
    for root, dirs, files in os.walk(directory):
        # Skip test directories and hidden folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'test' and d != 'tests']
        
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        java_files[file_path] = f.read()
                except Exception:
                    pass  # Skip unreadable files
    
    return java_files


# ═══════════════════════════════════════════════════════════════════════════════
# API ENDPOINTS
# ═══════════════════════════════════════════════════════════════════════════════

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "models_loaded": MODELS is not None,
        "version": "1.0.0"
    })


@app.route('/analyze/code', methods=['POST'])
def analyze_code():
    """
    Analyze a single Java code snippet.
    
    Request body:
    {
        "code": "public class Example { ... }",
        "filename": "Example.java"  (optional)
    }
    
    Returns: BuildingMetrics for the class
    """
    data = request.get_json()
    
    if not data or 'code' not in data:
        return jsonify({"error": "Missing 'code' in request body"}), 400
    
    code = data['code']
    filename = data.get('filename', '')
    
    try:
        building = analyze_code_for_building(code, filename)
        return jsonify(asdict(building))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/analyze/file', methods=['POST'])
def analyze_file():
    """
    Analyze a Java file by path.
    
    Request body:
    {
        "file_path": "/path/to/Example.java"
    }
    """
    data = request.get_json()
    
    if not data or 'file_path' not in data:
        return jsonify({"error": "Missing 'file_path' in request body"}), 400
    
    file_path = data['file_path']
    
    if not os.path.exists(file_path):
        return jsonify({"error": f"File not found: {file_path}"}), 404
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        building = analyze_code_for_building(code, file_path)
        return jsonify(asdict(building))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/analyze/repo', methods=['POST'])
def analyze_repo():
    """
    Analyze all Java files in a local directory.
    Returns complete city layout with buildings and relationships.
    
    Request body:
    {
        "directory": "/path/to/project",
        "max_files": 100  (optional, default 100)
    }
    """
    data = request.get_json()
    
    if not data or 'directory' not in data:
        return jsonify({"error": "Missing 'directory' in request body"}), 400
    
    directory = data['directory']
    max_files = data.get('max_files', 100)
    
    if not os.path.isdir(directory):
        return jsonify({"error": f"Directory not found: {directory}"}), 404
    
    try:
        # Find all Java files
        java_files = find_java_files(directory)
        
        if not java_files:
            return jsonify({"error": "No Java files found in directory"}), 404
        
        # Limit number of files
        if len(java_files) > max_files:
            java_files = dict(list(java_files.items())[:max_files])
        
        # Analyze each file
        buildings = []
        clean_count = 0
        
        for file_path, code in java_files.items():
            relative_path = os.path.relpath(file_path, directory)
            building = analyze_code_for_building(code, relative_path)
            buildings.append(asdict(building))
            if building.primary_smell == "Clean":
                clean_count += 1
        
        # Extract relationships
        relationships = extract_relationships(java_files)
        
        # Calculate averages
        avg_quality = sum(b["quality_score"] for b in buildings) / len(buildings) if buildings else 0
        
        city = {
            "buildings": buildings,
            "inheritance": relationships["inheritance"],
            "associations": relationships["associations"],
            "compositions": relationships["compositions"],
            "dependencies": relationships["dependencies"],
            "aggregations": relationships["aggregations"],
            "total_classes": len(buildings),
            "clean_count": clean_count,
            "smell_count": len(buildings) - clean_count,
            "average_quality": round(avg_quality, 3)
        }
        
        return jsonify(city)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/analyze/github', methods=['POST'])
def analyze_github():
    """
    Clone and analyze a GitHub repository.
    
    Request body:
    {
        "repo_url": "https://github.com/username/repo",
        "max_files": 100  (optional)
    }
    
    Returns: Complete city layout
    """
    data = request.get_json()
    
    if not data or 'repo_url' not in data:
        return jsonify({"error": "Missing 'repo_url' in request body"}), 400
    
    repo_url = data['repo_url']
    max_files = data.get('max_files', 100)
    
    temp_dir = None
    try:
        # Clone the repository
        temp_dir = clone_github_repo(repo_url)
        
        # Find and analyze Java files
        java_files = find_java_files(temp_dir)
        
        if not java_files:
            return jsonify({"error": "No Java files found in repository"}), 404
        
        # Limit files
        if len(java_files) > max_files:
            java_files = dict(list(java_files.items())[:max_files])
        
        # Analyze each file
        buildings = []
        clean_count = 0
        
        for file_path, code in java_files.items():
            relative_path = os.path.relpath(file_path, temp_dir)
            building = analyze_code_for_building(code, relative_path)
            buildings.append(asdict(building))
            if building.primary_smell == "Clean":
                clean_count += 1
        
        # Extract relationships
        relationships = extract_relationships(java_files)
        
        # Calculate averages
        avg_quality = sum(b["quality_score"] for b in buildings) / len(buildings) if buildings else 0
        
        city = {
            "repo_url": repo_url,
            "buildings": buildings,
            "inheritance": relationships["inheritance"],
            "associations": relationships["associations"],
            "compositions": relationships["compositions"],
            "dependencies": relationships["dependencies"],
            "aggregations": relationships["aggregations"],
            "total_classes": len(buildings),
            "clean_count": clean_count,
            "smell_count": len(buildings) - clean_count,
            "average_quality": round(avg_quality, 3)
        }
        
        return jsonify(city)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        # Cleanup temp directory
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     EduCode - Code Smell Detection API                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Endpoints:                                                                   ║
║    POST /analyze/code     - Analyze Java code snippet                         ║
║    POST /analyze/file     - Analyze a local .java file                        ║
║    POST /analyze/repo     - Analyze local directory                           ║
║    POST /analyze/github   - Clone and analyze GitHub repo                     ║
║    GET  /health           - Health check                                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  Running on: http://localhost:5000                                            ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
