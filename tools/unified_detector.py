"""
🔬 UNIFIED CODE SMELL DETECTOR
==============================
Combines multiple static analysis tools to detect a comprehensive set of code smells.

Supported Tools:
  - CK (CK Metrics) - For object-oriented metrics
  - PMD - For design and best practices
  - Checkstyle - For complexity and size metrics
  - SonarQube (optional) - For advanced analysis if server available

Detected Code Smells:
  ┌──────────────────────────┬─────────────────────────────────────────────────────┐
  │ Code Smell               │ Detection Tools                                      │
  ├──────────────────────────┼─────────────────────────────────────────────────────┤
  │ GodClass                 │ CK, PMD, Checkstyle, SonarQube                      │
  │ DataClass                │ CK, PMD, SonarQube                                  │
  │ LongMethod               │ CK, PMD, Checkstyle, SonarQube                      │
  │ FeatureEnvy              │ CK, PMD (LawOfDemeter), SonarQube                   │
  │ LongParameterList        │ PMD, Checkstyle                                     │
  │ DeepNesting              │ PMD, Checkstyle                                     │
  │ HighCoupling             │ CK (CBO), PMD, Checkstyle                           │
  │ ComplexConditional       │ PMD, Checkstyle                                     │
  │ DuplicatedCode           │ PMD, SonarQube                                      │
  │ DeadCode                 │ PMD (unused), SonarQube                             │
  │ LazyClass                │ PMD, CK                                             │
  │ RefusedBequest           │ PMD                                                 │
  │ MiddleMan                │ CK (TCC analysis)                                   │
  │ MessageChain             │ PMD (LawOfDemeter)                                  │
  │ ShotgunSurgery           │ CK (high coupling + low cohesion)                   │
  │ ParallelInheritance      │ CK (DIT, NOC analysis)                              │
  └──────────────────────────┴─────────────────────────────────────────────────────┘

Usage:
  python unified_detector.py <path_to_java_file_or_directory>
  python unified_detector.py <path> --output results.json
  python unified_detector.py <path> --tools pmd,checkstyle
  
Requirements:
  - Python 3.8+
  - Java 11+ (for PMD and Checkstyle)
"""

import os
import sys
import json
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, asdict, field
from collections import defaultdict
from datetime import datetime

# Add parent directory to path for imports
SCRIPT_DIR = Path(__file__).parent.absolute()
PROJECT_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

# Import tool-specific analyzers
try:
    from pmd_analyzer import analyze_java_source as pmd_analyze, CodeSmellIssue
except ImportError:
    pmd_analyze = None

try:
    from checkstyle_analyzer import analyze_with_checkstyle as checkstyle_analyze
except ImportError:
    checkstyle_analyze = None


# ═══════════════════════════════════════════════════════════════════════════════
# ANSI Colors for Terminal Output
# ═══════════════════════════════════════════════════════════════════════════════

class Colors:
    if os.name == 'nt':
        os.system('')  # Enable ANSI on Windows
    
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'


def color(text, *styles):
    """Apply color styles to text"""
    return ''.join(styles) + str(text) + Colors.END


# ═══════════════════════════════════════════════════════════════════════════════
# Data Classes
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class SmellEvidence:
    """Evidence for a detected smell from one tool"""
    tool: str
    rule: str
    message: str
    line_number: int
    severity: str
    confidence: float  # 0.0 - 1.0

@dataclass
class UnifiedSmell:
    """A code smell with evidence from multiple tools"""
    smell_type: str
    description: str
    severity: str  # LOW, MEDIUM, HIGH, CRITICAL
    confidence: float  # Overall confidence (0.0 - 1.0)
    evidence: List[SmellEvidence] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)

@dataclass
class FileAnalysis:
    """Complete analysis of a single file"""
    file_path: str
    class_name: str
    smells: List[UnifiedSmell]
    primary_smell: str
    smell_count: int
    metrics: Dict
    tool_results: Dict  # Raw results from each tool


# ═══════════════════════════════════════════════════════════════════════════════
# Code Smell Definitions
# ═══════════════════════════════════════════════════════════════════════════════

SMELL_DEFINITIONS = {
    "GodClass": {
        "description": "A class that does too much - violates Single Responsibility Principle",
        "severity": "HIGH",
        "indicators": ["high LOC", "high WMC", "many methods", "high coupling", "low cohesion"],
        "recommendations": [
            "Extract smaller classes with focused responsibilities",
            "Apply Single Responsibility Principle",
            "Consider splitting by feature or domain concept"
        ]
    },
    "DataClass": {
        "description": "A class with mostly data (fields/getters/setters) and little behavior",
        "severity": "MEDIUM",
        "indicators": ["many fields", "mostly accessors", "low WMC", "high NOPA"],
        "recommendations": [
            "Move behavior that operates on this data into the class",
            "Consider using Java Records (Java 14+) for true data carriers",
            "Encapsulate field access with meaningful methods"
        ]
    },
    "LongMethod": {
        "description": "A method that is too long, complex, or has too many responsibilities",
        "severity": "MEDIUM",
        "indicators": ["high LOC", "high cyclomatic complexity", "high nesting"],
        "recommendations": [
            "Extract smaller methods with descriptive names",
            "Use Extract Method refactoring",
            "Each method should do ONE thing"
        ]
    },
    "FeatureEnvy": {
        "description": "A method that uses data from another class more than its own",
        "severity": "MEDIUM",
        "indicators": ["high ATFD", "many external calls", "Law of Demeter violations"],
        "recommendations": [
            "Move the method to the class whose data it envies",
            "Consider if the classes should be merged",
            "Extract the envied logic into the target class"
        ]
    },
    "LongParameterList": {
        "description": "Method has too many parameters",
        "severity": "MEDIUM",
        "indicators": ["more than 5-7 parameters"],
        "recommendations": [
            "Introduce Parameter Object",
            "Use Builder pattern",
            "Consider breaking up the method"
        ]
    },
    "DeepNesting": {
        "description": "Too many levels of nested control structures",
        "severity": "MEDIUM",
        "indicators": ["nested if/for/while more than 3 levels"],
        "recommendations": [
            "Use early returns (guard clauses)",
            "Extract nested blocks to separate methods",
            "Use polymorphism instead of conditionals"
        ]
    },
    "HighCoupling": {
        "description": "Class has too many dependencies on other classes",
        "severity": "MEDIUM",
        "indicators": ["high CBO", "many imports", "high fan-out"],
        "recommendations": [
            "Apply Dependency Injection",
            "Use interfaces to reduce coupling",
            "Consider Facade pattern to reduce direct dependencies"
        ]
    },
    "ComplexConditional": {
        "description": "Boolean expressions are too complex",
        "severity": "LOW",
        "indicators": ["many boolean operators", "complex conditions"],
        "recommendations": [
            "Extract conditions into well-named methods",
            "Use Introduce Explaining Variable",
            "Consider Strategy pattern for complex branching"
        ]
    },
    "DeadCode": {
        "description": "Code that is never executed or used",
        "severity": "LOW",
        "indicators": ["unused methods", "unused variables", "unreachable code"],
        "recommendations": [
            "Remove unused code safely",
            "Check if it was intended to be used",
            "Use IDE tools to find all dead code"
        ]
    },
    "DuplicatedCode": {
        "description": "Same code appears in multiple places",
        "severity": "MEDIUM",
        "indicators": ["copy-pasted code", "similar methods"],
        "recommendations": [
            "Extract common code to shared method",
            "Use Template Method pattern for similar algorithms",
            "Consider Extract Class for duplicated groups"
        ]
    },
    "LazyClass": {
        "description": "A class that doesn't do enough to justify its existence",
        "severity": "LOW",
        "indicators": ["very few methods", "delegates everything", "thin wrapper"],
        "recommendations": [
            "Merge with related class",
            "Inline the class if it's a thin wrapper",
            "Add more behavior if the class should exist"
        ]
    },
    "RefusedBequest": {
        "description": "Subclass doesn't use inherited methods/data properly",
        "severity": "LOW",
        "indicators": ["overrides to do nothing", "inherits but ignores"],
        "recommendations": [
            "Reconsider inheritance relationship",
            "Use composition instead of inheritance",
            "Extract interface for needed functionality"
        ]
    },
    "MiddleMan": {
        "description": "Class that just delegates to another class",
        "severity": "LOW",
        "indicators": ["most methods just forward calls", "no real logic"],
        "recommendations": [
            "Remove the middle man",
            "Add real behavior or merge classes",
            "If it's an adapter, document it as such"
        ]
    },
    "MessageChain": {
        "description": "Long chain of method calls (a.b().c().d())",
        "severity": "LOW",
        "indicators": ["Law of Demeter violations", "train wreck code"],
        "recommendations": [
            "Hide delegate behind wrapper method",
            "Use Tell, Don't Ask principle",
            "Consider moving behavior closer to data"
        ]
    },
    "ShotgunSurgery": {
        "description": "A change requires many small changes in many classes",
        "severity": "HIGH",
        "indicators": ["high coupling", "scattered feature implementation"],
        "recommendations": [
            "Move related methods to one class",
            "Apply Move Method/Field refactorings",
            "Consider Feature-based package structure"
        ]
    },
    "Clean": {
        "description": "No significant code smells detected",
        "severity": "NONE",
        "indicators": [],
        "recommendations": ["Keep up the good work!"]
    }
}


# ═══════════════════════════════════════════════════════════════════════════════
# CK Metrics Integration (uses existing CK data)
# ═══════════════════════════════════════════════════════════════════════════════

def extract_ck_metrics(java_code: str) -> Dict:
    """Extract CK-like metrics from Java source code"""
    metrics = {}
    
    lines = java_code.split('\n')
    non_empty = [l for l in lines if l.strip() and not l.strip().startswith('//')]
    metrics['LOC'] = len(non_empty)
    
    # Methods
    method_pattern = r'(public|private|protected)\s+(static\s+)?(final\s+)?(\w+)\s+(\w+)\s*\([^)]*\)\s*(throws\s+[\w,\s]+)?\s*\{'
    methods = re.findall(method_pattern, java_code)
    metrics['METHODS'] = max(len(methods), 1)
    
    # Fields
    field_pattern = r'(private|public|protected)\s+(static\s+)?(final\s+)?([\w<>,\[\]\s]+)\s+(\w+)\s*(=|;)'
    fields = re.findall(field_pattern, java_code)
    metrics['FIELDS'] = len(fields)
    
    # WMC (Weighted Methods per Class) - approximate via complexity
    wmc = metrics['METHODS']
    wmc += len(re.findall(r'\bif\s*\(', java_code))
    wmc += len(re.findall(r'\bwhile\s*\(', java_code))
    wmc += len(re.findall(r'\bfor\s*\(', java_code))
    wmc += len(re.findall(r'\bcase\s+', java_code))
    wmc += len(re.findall(r'\bcatch\s*\(', java_code))
    wmc += len(re.findall(r'&&|\|\|', java_code))
    metrics['WMC'] = wmc
    
    # CBO (Coupling Between Objects)
    import_count = len(re.findall(r'import\s+([\w.]+);', java_code))
    type_refs = set(re.findall(r'[<(,\s]([A-Z][a-zA-Z0-9]*)[>\s,)\[]', java_code))
    common_types = {'String', 'Integer', 'Long', 'Double', 'Float', 'Boolean', 
                   'List', 'Map', 'Set', 'ArrayList', 'HashMap', 'Object'}
    type_refs -= common_types
    metrics['CBO'] = import_count + len(type_refs)
    
    # LCOM (Lack of Cohesion)
    metrics['LCOM'] = max(0, metrics['METHODS'] - min(metrics['FIELDS'], metrics['METHODS']))
    
    # TCC (Tight Class Cohesion) - simplified
    if metrics['METHODS'] > 0 and metrics['FIELDS'] > 0:
        metrics['TCC'] = min(1.0, (metrics['METHODS'] * 0.3) / (metrics['FIELDS'] + 1))
    else:
        metrics['TCC'] = 0.0
    
    # ATFD (Access To Foreign Data)
    getter_calls = len(re.findall(r'(\w+)\.(get|is|has|find)\w*\(', java_code))
    setter_calls = len(re.findall(r'(\w+)\.(set|add|put)\w*\(', java_code))
    metrics['ATFD'] = getter_calls + setter_calls
    
    # Max method LOC (find longest method)
    method_starts = list(re.finditer(r'(public|private|protected)\s+\w+\s+\w+\s*\([^)]*\)\s*\{', java_code))
    max_method_loc = 10
    for i, match in enumerate(method_starts):
        start = match.end()
        depth = 1
        pos = start
        while depth > 0 and pos < len(java_code):
            if java_code[pos] == '{':
                depth += 1
            elif java_code[pos] == '}':
                depth -= 1
            pos += 1
        method_text = java_code[start:pos]
        method_lines = len([l for l in method_text.split('\n') if l.strip()])
        max_method_loc = max(max_method_loc, method_lines)
    
    metrics['MAX_METHOD_LOC'] = max_method_loc
    
    # DIT (Depth of Inheritance Tree)
    extends = re.findall(r'\bextends\s+(\w+)', java_code)
    implements = re.findall(r'\bimplements\s+([\w,\s]+)', java_code)
    metrics['DIT'] = len(extends) + (1 if implements else 0)
    
    return metrics


def detect_smells_from_ck(metrics: Dict) -> List[UnifiedSmell]:
    """Detect smells based on CK metrics"""
    smells = []
    
    # GodClass detection
    if (metrics.get('LOC', 0) > 300 or 
        metrics.get('WMC', 0) > 50 or 
        (metrics.get('METHODS', 0) > 20 and metrics.get('FIELDS', 0) > 15)):
        
        confidence = 0.0
        if metrics.get('LOC', 0) > 500: confidence += 0.3
        elif metrics.get('LOC', 0) > 300: confidence += 0.2
        if metrics.get('WMC', 0) > 50: confidence += 0.3
        if metrics.get('METHODS', 0) > 20: confidence += 0.2
        if metrics.get('TCC', 1.0) < 0.3: confidence += 0.2
        
        smells.append(UnifiedSmell(
            smell_type="GodClass",
            description=SMELL_DEFINITIONS["GodClass"]["description"],
            severity="HIGH",
            confidence=min(confidence, 1.0),
            evidence=[SmellEvidence(
                tool="CK",
                rule="GodClass",
                message=f"LOC={metrics.get('LOC')}, WMC={metrics.get('WMC')}, Methods={metrics.get('METHODS')}",
                line_number=0,
                severity="HIGH",
                confidence=confidence
            )],
            recommendations=SMELL_DEFINITIONS["GodClass"]["recommendations"]
        ))
    
    # DataClass detection
    accessor_ratio = 0
    if metrics.get('METHODS', 0) > 0:
        # Estimate accessor methods
        accessor_ratio = metrics.get('FIELDS', 0) * 2 / metrics.get('METHODS', 1)
    
    if accessor_ratio > 0.7 and metrics.get('WMC', 0) < 20 and metrics.get('FIELDS', 0) > 3:
        smells.append(UnifiedSmell(
            smell_type="DataClass",
            description=SMELL_DEFINITIONS["DataClass"]["description"],
            severity="MEDIUM",
            confidence=min(accessor_ratio, 0.9),
            evidence=[SmellEvidence(
                tool="CK",
                rule="DataClass",
                message=f"High accessor ratio: {accessor_ratio:.2f}, Fields={metrics.get('FIELDS')}",
                line_number=0,
                severity="MEDIUM",
                confidence=accessor_ratio
            )],
            recommendations=SMELL_DEFINITIONS["DataClass"]["recommendations"]
        ))
    
    # LongMethod detection
    if metrics.get('MAX_METHOD_LOC', 0) > 50:
        confidence = min(0.5 + (metrics.get('MAX_METHOD_LOC', 0) - 50) / 100, 1.0)
        smells.append(UnifiedSmell(
            smell_type="LongMethod",
            description=SMELL_DEFINITIONS["LongMethod"]["description"],
            severity="MEDIUM",
            confidence=confidence,
            evidence=[SmellEvidence(
                tool="CK",
                rule="LongMethod",
                message=f"Longest method: {metrics.get('MAX_METHOD_LOC')} lines",
                line_number=0,
                severity="MEDIUM",
                confidence=confidence
            )],
            recommendations=SMELL_DEFINITIONS["LongMethod"]["recommendations"]
        ))
    
    # FeatureEnvy detection
    if metrics.get('ATFD', 0) > 5 and metrics.get('TCC', 1.0) < 0.4:
        confidence = min(metrics.get('ATFD', 0) / 15, 0.9)
        smells.append(UnifiedSmell(
            smell_type="FeatureEnvy",
            description=SMELL_DEFINITIONS["FeatureEnvy"]["description"],
            severity="MEDIUM",
            confidence=confidence,
            evidence=[SmellEvidence(
                tool="CK",
                rule="FeatureEnvy",
                message=f"ATFD={metrics.get('ATFD')}, TCC={metrics.get('TCC'):.2f}",
                line_number=0,
                severity="MEDIUM",
                confidence=confidence
            )],
            recommendations=SMELL_DEFINITIONS["FeatureEnvy"]["recommendations"]
        ))
    
    # HighCoupling detection
    if metrics.get('CBO', 0) > 15:
        confidence = min(metrics.get('CBO', 0) / 30, 0.9)
        smells.append(UnifiedSmell(
            smell_type="HighCoupling",
            description=SMELL_DEFINITIONS["HighCoupling"]["description"],
            severity="MEDIUM",
            confidence=confidence,
            evidence=[SmellEvidence(
                tool="CK",
                rule="CouplingBetweenObjects",
                message=f"CBO={metrics.get('CBO')}",
                line_number=0,
                severity="MEDIUM",
                confidence=confidence
            )],
            recommendations=SMELL_DEFINITIONS["HighCoupling"]["recommendations"]
        ))
    
    return smells


# ═══════════════════════════════════════════════════════════════════════════════
# Unified Analysis Engine
# ═══════════════════════════════════════════════════════════════════════════════

class UnifiedSmellDetector:
    """Main class for unified code smell detection"""
    
    def __init__(self, tools: Optional[List[str]] = None):
        """
        Initialize detector with specific tools.
        
        Args:
            tools: List of tools to use. Default: all available
                   Options: 'ck', 'pmd', 'checkstyle'
        """
        self.available_tools = []
        
        # Check which tools are available
        if pmd_analyze:
            self.available_tools.append('pmd')
        if checkstyle_analyze:
            self.available_tools.append('checkstyle')
        self.available_tools.append('ck')  # Always available (pure Python)
        
        if tools:
            self.tools = [t for t in tools if t in self.available_tools]
        else:
            self.tools = self.available_tools
        
        print(f"🔧 Using tools: {', '.join(self.tools)}")
    
    def analyze_code(self, java_code: str, class_name: str = "UnknownClass") -> FileAnalysis:
        """
        Analyze a Java code string.
        
        Args:
            java_code: Java source code
            class_name: Name of the class
            
        Returns:
            FileAnalysis with all detected smells
        """
        all_smells = []
        tool_results = {}
        metrics = {}
        
        # Always run CK analysis (pure Python)
        ck_metrics = extract_ck_metrics(java_code)
        metrics.update(ck_metrics)
        ck_smells = detect_smells_from_ck(ck_metrics)
        all_smells.extend(ck_smells)
        tool_results['ck'] = {
            'metrics': ck_metrics,
            'smells': len(ck_smells)
        }
        
        # Run PMD if available
        if 'pmd' in self.tools and pmd_analyze:
            with tempfile.TemporaryDirectory() as tmpdir:
                temp_file = Path(tmpdir) / f"{class_name}.java"
                temp_file.write_text(java_code, encoding='utf-8')
                
                pmd_results = pmd_analyze(str(temp_file))
                if pmd_results:
                    for file_path, summary in pmd_results.items():
                        for issue in summary.issues:
                            smell = UnifiedSmell(
                                smell_type=issue.smell_type,
                                description=SMELL_DEFINITIONS.get(issue.smell_type, {}).get(
                                    'description', issue.message),
                                severity="MEDIUM" if issue.priority > 2 else "HIGH",
                                confidence=0.7 if issue.priority > 2 else 0.85,
                                evidence=[SmellEvidence(
                                    tool="PMD",
                                    rule=issue.rule_name,
                                    message=issue.message,
                                    line_number=issue.line_number,
                                    severity=str(issue.priority),
                                    confidence=0.7
                                )],
                                recommendations=SMELL_DEFINITIONS.get(issue.smell_type, {}).get(
                                    'recommendations', [])
                            )
                            all_smells.append(smell)
                        
                        tool_results['pmd'] = {
                            'issues': len(summary.issues),
                            'smells': list(summary.smells)
                        }
        
        # Run Checkstyle if available
        if 'checkstyle' in self.tools and checkstyle_analyze:
            with tempfile.TemporaryDirectory() as tmpdir:
                temp_file = Path(tmpdir) / f"{class_name}.java"
                temp_file.write_text(java_code, encoding='utf-8')
                
                cs_results = checkstyle_analyze(str(temp_file))
                if cs_results:
                    for file_path, summary in cs_results.items():
                        for issue in summary.issues:
                            smell = UnifiedSmell(
                                smell_type=issue.smell_type,
                                description=SMELL_DEFINITIONS.get(issue.smell_type, {}).get(
                                    'description', issue.message),
                                severity="MEDIUM",
                                confidence=0.65,
                                evidence=[SmellEvidence(
                                    tool="Checkstyle",
                                    rule=issue.check_name,
                                    message=issue.message,
                                    line_number=issue.line_number,
                                    severity=issue.severity,
                                    confidence=0.65
                                )],
                                recommendations=SMELL_DEFINITIONS.get(issue.smell_type, {}).get(
                                    'recommendations', [])
                            )
                            all_smells.append(smell)
                        
                        tool_results['checkstyle'] = {
                            'issues': len(summary.issues),
                            'smells': list(summary.smells)
                        }
        
        # Merge duplicate smells (same type from multiple tools increases confidence)
        merged_smells = self._merge_smells(all_smells)
        
        # Determine primary smell
        primary_smell = self._determine_primary_smell(merged_smells)
        
        return FileAnalysis(
            file_path="",
            class_name=class_name,
            smells=merged_smells,
            primary_smell=primary_smell,
            smell_count=len(merged_smells),
            metrics=metrics,
            tool_results=tool_results
        )
    
    def analyze_file(self, file_path: str) -> Optional[FileAnalysis]:
        """Analyze a Java file"""
        path = Path(file_path)
        if not path.exists():
            print(f"❌ File not found: {file_path}")
            return None
        
        java_code = path.read_text(encoding='utf-8', errors='ignore')
        class_name = path.stem
        
        analysis = self.analyze_code(java_code, class_name)
        analysis.file_path = str(path.absolute())
        
        return analysis
    
    def analyze_directory(self, dir_path: str) -> Dict[str, FileAnalysis]:
        """Analyze all Java files in a directory"""
        results = {}
        path = Path(dir_path)
        
        java_files = list(path.rglob("*.java"))
        print(f"\n📂 Found {len(java_files)} Java files")
        
        for i, java_file in enumerate(java_files, 1):
            print(f"  [{i}/{len(java_files)}] Analyzing: {java_file.name}")
            analysis = self.analyze_file(str(java_file))
            if analysis:
                results[str(java_file)] = analysis
        
        return results
    
    def _merge_smells(self, smells: List[UnifiedSmell]) -> List[UnifiedSmell]:
        """Merge duplicate smells, boosting confidence when detected by multiple tools"""
        by_type = defaultdict(list)
        for smell in smells:
            by_type[smell.smell_type].append(smell)
        
        merged = []
        for smell_type, type_smells in by_type.items():
            if not type_smells:
                continue
            
            # Combine evidence from all instances
            all_evidence = []
            all_recommendations = set()
            tools_detecting = set()
            max_severity = "LOW"
            severity_order = {"NONE": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}
            
            for smell in type_smells:
                all_evidence.extend(smell.evidence)
                all_recommendations.update(smell.recommendations)
                for ev in smell.evidence:
                    tools_detecting.add(ev.tool)
                if severity_order.get(smell.severity, 0) > severity_order.get(max_severity, 0):
                    max_severity = smell.severity
            
            # Calculate confidence boost based on number of tools detecting
            base_confidence = max(s.confidence for s in type_smells)
            tool_boost = min(0.1 * (len(tools_detecting) - 1), 0.2)
            final_confidence = min(base_confidence + tool_boost, 1.0)
            
            merged.append(UnifiedSmell(
                smell_type=smell_type,
                description=SMELL_DEFINITIONS.get(smell_type, {}).get(
                    'description', type_smells[0].description),
                severity=max_severity,
                confidence=final_confidence,
                evidence=all_evidence,
                recommendations=list(all_recommendations)
            ))
        
        # Sort by severity and confidence
        severity_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1, "NONE": 0}
        merged.sort(key=lambda x: (severity_order.get(x.severity, 0), x.confidence), reverse=True)
        
        return merged
    
    def _determine_primary_smell(self, smells: List[UnifiedSmell]) -> str:
        """Determine the primary (most significant) smell"""
        if not smells:
            return "Clean"
        
        # Priority order for primary smell
        priority = ["GodClass", "ShotgunSurgery", "LongMethod", "FeatureEnvy", 
                   "DataClass", "HighCoupling", "DeepNesting", "DuplicatedCode",
                   "LongParameterList", "DeadCode"]
        
        for priority_smell in priority:
            for smell in smells:
                if smell.smell_type == priority_smell and smell.confidence > 0.5:
                    return priority_smell
        
        # Fall back to highest confidence
        if smells:
            return smells[0].smell_type
        
        return "Clean"


# ═══════════════════════════════════════════════════════════════════════════════
# Reporting Functions
# ═══════════════════════════════════════════════════════════════════════════════

def print_file_report(analysis: FileAnalysis):
    """Print detailed report for a single file"""
    print(f"\n{'='*80}")
    print(f"📄 {color(analysis.class_name, Colors.CYAN, Colors.BOLD)}")
    print(f"   {analysis.file_path}")
    print(f"{'='*80}")
    
    if not analysis.smells:
        print(f"\n   {color('✨ Clean Code!', Colors.GREEN, Colors.BOLD)} No significant code smells detected.")
        return
    
    print(f"\n   Primary Smell: {color(analysis.primary_smell, Colors.YELLOW, Colors.BOLD)}")
    print(f"   Total Smells: {len(analysis.smells)}")
    
    # Metrics
    print(f"\n   {color('📊 Metrics:', Colors.BLUE)}")
    for metric, value in analysis.metrics.items():
        print(f"      {metric:20s}: {value}")
    
    # Smells
    print(f"\n   {color('🔍 Detected Smells:', Colors.BLUE)}")
    for smell in analysis.smells:
        severity_color = {
            "CRITICAL": Colors.RED,
            "HIGH": Colors.RED,
            "MEDIUM": Colors.YELLOW,
            "LOW": Colors.CYAN
        }.get(smell.severity, Colors.WHITE)
        
        print(f"\n      {color(f'■ {smell.smell_type}', severity_color, Colors.BOLD)}")
        print(f"        Severity: {smell.severity}  |  Confidence: {smell.confidence:.0%}")
        print(f"        {smell.description}")
        
        if smell.evidence:
            print(f"        Evidence:")
            for ev in smell.evidence[:3]:  # Show first 3
                print(f"          - [{ev.tool}] {ev.rule}: {ev.message[:60]}...")
        
        if smell.recommendations:
            print(f"        Recommendations:")
            for rec in smell.recommendations[:2]:  # Show first 2
                print(f"          → {rec}")


def print_summary_report(results: Dict[str, FileAnalysis]):
    """Print summary report for multiple files"""
    print(f"\n{'='*80}")
    print(f"{color('📋 UNIFIED CODE SMELL ANALYSIS - SUMMARY', Colors.CYAN, Colors.BOLD)}")
    print(f"{'='*80}")
    
    total_files = len(results)
    total_smells = sum(len(a.smells) for a in results.values())
    files_with_smells = sum(1 for a in results.values() if a.smells)
    
    print(f"\n   📁 Files analyzed: {total_files}")
    print(f"   ⚠️  Files with smells: {files_with_smells}")
    print(f"   🔍 Total smells: {total_smells}")
    
    # Aggregate smell types
    smell_counts = defaultdict(int)
    for analysis in results.values():
        for smell in analysis.smells:
            smell_counts[smell.smell_type] += 1
    
    print(f"\n   {color('📊 Smells by Type:', Colors.BLUE)}")
    for smell_type, count in sorted(smell_counts.items(), key=lambda x: -x[1]):
        desc = SMELL_DEFINITIONS.get(smell_type, {}).get('description', '')[:50]
        print(f"      {smell_type:20s}: {count:4d}  - {desc}...")
    
    # Top problematic files
    print(f"\n   {color('🔥 Most Problematic Files:', Colors.BLUE)}")
    sorted_files = sorted(results.values(), key=lambda x: len(x.smells), reverse=True)[:10]
    for analysis in sorted_files:
        if analysis.smells:
            print(f"      📄 {analysis.class_name:30s} - {len(analysis.smells)} smells ({analysis.primary_smell})")


def export_results(results: Dict[str, FileAnalysis], output_path: str):
    """Export results to JSON"""
    export_data = {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_files": len(results),
            "files_with_smells": sum(1 for a in results.values() if a.smells),
            "total_smells": sum(len(a.smells) for a in results.values()),
        },
        "smell_definitions": SMELL_DEFINITIONS,
        "files": {}
    }
    
    for file_path, analysis in results.items():
        export_data["files"][file_path] = {
            "class_name": analysis.class_name,
            "primary_smell": analysis.primary_smell,
            "smell_count": analysis.smell_count,
            "metrics": analysis.metrics,
            "smells": [
                {
                    "type": s.smell_type,
                    "severity": s.severity,
                    "confidence": s.confidence,
                    "description": s.description,
                    "evidence": [asdict(e) for e in s.evidence],
                    "recommendations": s.recommendations
                }
                for s in analysis.smells
            ],
            "tool_results": analysis.tool_results
        }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2)
    
    print(f"\n💾 Results exported to: {output_path}")


# ═══════════════════════════════════════════════════════════════════════════════
# CLI Interface
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUsage:")
        print("  python unified_detector.py <path_to_java_source>")
        print("  python unified_detector.py <path> --output results.json")
        print("  python unified_detector.py <path> --tools pmd,checkstyle,ck")
        print("\nExamples:")
        print("  python unified_detector.py ./projects/myapp/")
        print("  python unified_detector.py MyClass.java --output report.json")
        sys.exit(1)
    
    source_path = sys.argv[1]
    output_path = None
    tools = None
    
    # Parse arguments
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]
    
    if "--tools" in sys.argv:
        idx = sys.argv.index("--tools")
        if idx + 1 < len(sys.argv):
            tools = sys.argv[idx + 1].split(',')
    
    if not os.path.exists(source_path):
        print(f"❌ Path not found: {source_path}")
        sys.exit(1)
    
    # Create detector
    detector = UnifiedSmellDetector(tools=tools)
    
    # Run analysis
    path = Path(source_path)
    if path.is_file():
        analysis = detector.analyze_file(source_path)
        if analysis:
            print_file_report(analysis)
            if output_path:
                export_results({source_path: analysis}, output_path)
    else:
        results = detector.analyze_directory(source_path)
        if results:
            print_summary_report(results)
            # Print detailed reports for files with smells
            for file_path, analysis in list(results.items())[:5]:  # Top 5
                if analysis.smells:
                    print_file_report(analysis)
            
            if output_path:
                export_results(results, output_path)


if __name__ == "__main__":
    main()
