"""
PMD Code Smell Analyzer
========================
Integrates PMD static analysis tool to detect additional code smells.

PMD can detect the following code smells:
  - GodClass (via design rules)
  - DataClass (via design rules)  
  - LongMethod / CyclomaticComplexity
  - CognitiveComplexity
  - TooManyMethods
  - TooManyFields
  - ExcessiveImports (high coupling)
  - DeepNestedIf
  - LawOfDemeter
  - ExcessiveParameterList
  - NPathComplexity
  - CouplingBetweenObjects

Requirements:
  - Java 11+ installed
  - PMD 7.x (will be downloaded automatically)

Usage:
  python pmd_analyzer.py <path_to_java_file_or_directory>
"""

import os
import sys
import json
import subprocess
import tempfile
import urllib.request
import zipfile
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict

# ═══════════════════════════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════════════════════════

SCRIPT_DIR = Path(__file__).parent.absolute()
PMD_VERSION = "7.0.0"
PMD_URL = f"https://github.com/pmd/pmd/releases/download/pmd_releases%2F{PMD_VERSION}/pmd-dist-{PMD_VERSION}-bin.zip"
PMD_DIR = SCRIPT_DIR / "pmd"
PMD_BIN = PMD_DIR / f"pmd-bin-{PMD_VERSION}" / "bin" / ("pmd.bat" if os.name == 'nt' else "pmd")

# PMD Rule Categories for Code Smells
PMD_RULESET = """<?xml version="1.0" encoding="UTF-8"?>
<ruleset name="CodeSmellDetection"
    xmlns="http://pmd.sourceforge.net/ruleset/2.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://pmd.sourceforge.net/ruleset/2.0.0 https://pmd.sourceforge.io/ruleset_2_0_0.xsd">
    
    <description>Custom ruleset for detecting code smells</description>
    
    <!-- GodClass Detection -->
    <rule ref="category/java/design.xml/GodClass"/>
    
    <!-- DataClass Detection -->
    <rule ref="category/java/design.xml/DataClass"/>
    
    <!-- Complexity Metrics -->
    <rule ref="category/java/design.xml/CyclomaticComplexity">
        <properties>
            <property name="methodReportLevel" value="10"/>
            <property name="classReportLevel" value="80"/>
        </properties>
    </rule>
    
    <rule ref="category/java/design.xml/CognitiveComplexity">
        <properties>
            <property name="reportLevel" value="15"/>
        </properties>
    </rule>
    
    <rule ref="category/java/design.xml/NPathComplexity">
        <properties>
            <property name="reportLevel" value="200"/>
        </properties>
    </rule>
    
    <!-- Size Metrics -->
    <rule ref="category/java/design.xml/TooManyMethods">
        <properties>
            <property name="maxmethods" value="15"/>
        </properties>
    </rule>
    
    <rule ref="category/java/design.xml/TooManyFields">
        <properties>
            <property name="maxfields" value="15"/>
        </properties>
    </rule>
    
    <rule ref="category/java/design.xml/ExcessiveParameterList">
        <properties>
            <property name="minimum" value="7"/>
        </properties>
    </rule>
    
    <rule ref="category/java/design.xml/ExcessiveImports">
        <properties>
            <property name="minimum" value="30"/>
        </properties>
    </rule>
    
    <rule ref="category/java/design.xml/ExcessivePublicCount">
        <properties>
            <property name="minimum" value="25"/>
        </properties>
    </rule>
    
    <!-- Coupling -->
    <rule ref="category/java/design.xml/CouplingBetweenObjects">
        <properties>
            <property name="threshold" value="20"/>
        </properties>
    </rule>
    
    <rule ref="category/java/design.xml/LawOfDemeter"/>
    
    <!-- Nesting -->
    <rule ref="category/java/design.xml/AvoidDeeplyNestedIfStmts">
        <properties>
            <property name="problemDepth" value="3"/>
        </properties>
    </rule>
    
    <!-- Best Practices that indicate smells -->
    <rule ref="category/java/bestpractices.xml/UnusedPrivateMethod"/>
    <rule ref="category/java/bestpractices.xml/UnusedPrivateField"/>
    <rule ref="category/java/bestpractices.xml/UnusedLocalVariable"/>
    <rule ref="category/java/bestpractices.xml/UnusedFormalParameter"/>
    
    <!-- Code Style issues that may indicate smells -->
    <rule ref="category/java/design.xml/CollapsibleIfStatements"/>
    <rule ref="category/java/design.xml/SimplifyBooleanReturns"/>
    <rule ref="category/java/design.xml/SingularField"/>
    <rule ref="category/java/design.xml/UselessOverridingMethod"/>
    
</ruleset>
"""

# ═══════════════════════════════════════════════════════════════════════════════
# Data Classes
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class CodeSmellIssue:
    """Represents a code smell detected by PMD"""
    file_path: str
    class_name: str
    method_name: Optional[str]
    line_number: int
    smell_type: str
    rule_name: str
    message: str
    priority: int
    category: str

@dataclass 
class SmellSummary:
    """Summary of smells for a file/class"""
    file_path: str
    class_name: str
    smells: List[str]
    primary_smell: str
    issues: List[CodeSmellIssue]
    metrics: Dict

# ═══════════════════════════════════════════════════════════════════════════════
# PMD Rule to Smell Mapping
# ═══════════════════════════════════════════════════════════════════════════════

# Map PMD rules to our smell categories
RULE_TO_SMELL = {
    # Direct mappings
    "GodClass": "GodClass",
    "DataClass": "DataClass",
    
    # Complexity -> LongMethod
    "CyclomaticComplexity": "LongMethod",
    "CognitiveComplexity": "LongMethod", 
    "NPathComplexity": "LongMethod",
    
    # Size issues
    "TooManyMethods": "GodClass",
    "TooManyFields": "GodClass",
    "ExcessivePublicCount": "GodClass",
    "ExcessiveImports": "HighCoupling",
    "ExcessiveParameterList": "LongParameterList",
    
    # Coupling
    "CouplingBetweenObjects": "HighCoupling",
    "LawOfDemeter": "FeatureEnvy",
    
    # Nesting
    "AvoidDeeplyNestedIfStmts": "DeepNesting",
    
    # Unused code -> DeadCode indicators
    "UnusedPrivateMethod": "DeadCode",
    "UnusedPrivateField": "DeadCode",
    "UnusedLocalVariable": "DeadCode",
    "UnusedFormalParameter": "DeadCode",
    
    # Other design issues
    "CollapsibleIfStatements": "ComplexConditional",
    "SimplifyBooleanReturns": "ComplexConditional",
    "SingularField": "LazyClass",
    "UselessOverridingMethod": "RefusedBequest",
}

# Extended smell categories with descriptions
SMELL_CATEGORIES = {
    "GodClass": "Class doing too much - violates Single Responsibility Principle",
    "DataClass": "Class with mostly data and little behavior",
    "LongMethod": "Method is too long or too complex",
    "FeatureEnvy": "Method uses other class's data more than its own",
    "HighCoupling": "Class has too many dependencies",
    "DeadCode": "Unused code that should be removed",
    "LongParameterList": "Method has too many parameters",
    "DeepNesting": "Too many levels of nested control structures",
    "ComplexConditional": "Overly complex conditional logic",
    "LazyClass": "Class doesn't do enough to justify its existence",
    "RefusedBequest": "Subclass doesn't use inherited methods properly",
    "DuplicatedCode": "Same code appears in multiple places",
    "Clean": "No significant code smells detected",
}

# ═══════════════════════════════════════════════════════════════════════════════
# PMD Setup & Execution
# ═══════════════════════════════════════════════════════════════════════════════

def check_java_installed() -> bool:
    """Check if Java is installed and accessible"""
    try:
        result = subprocess.run(
            ["java", "-version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False

def download_pmd() -> bool:
    """Download and extract PMD if not present"""
    if PMD_BIN.exists():
        print(f"✓ PMD already installed at {PMD_DIR}")
        return True
    
    print(f"📥 Downloading PMD {PMD_VERSION}...")
    PMD_DIR.mkdir(parents=True, exist_ok=True)
    
    zip_path = PMD_DIR / "pmd.zip"
    
    try:
        # Download PMD
        urllib.request.urlretrieve(PMD_URL, zip_path)
        print("📦 Extracting PMD...")
        
        # Extract
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(PMD_DIR)
        
        # Cleanup
        zip_path.unlink()
        
        # Make executable on Unix
        if os.name != 'nt':
            os.chmod(PMD_BIN, 0o755)
        
        print(f"✓ PMD installed at {PMD_DIR}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to download PMD: {e}")
        return False

def create_ruleset_file() -> Path:
    """Create temporary ruleset file"""
    ruleset_path = PMD_DIR / "codesmell_ruleset.xml"
    ruleset_path.parent.mkdir(parents=True, exist_ok=True)
    ruleset_path.write_text(PMD_RULESET, encoding='utf-8')
    return ruleset_path

def run_pmd(source_path: str, output_format: str = "xml") -> Optional[str]:
    """Run PMD analysis on source code"""
    if not PMD_BIN.exists():
        if not download_pmd():
            return None
    
    ruleset_path = create_ruleset_file()
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        output_path = f.name
    
    try:
        cmd = [
            str(PMD_BIN),
            "check",
            "-d", source_path,
            "-R", str(ruleset_path),
            "-f", output_format,
            "-r", output_path,
            "--no-cache"
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        # PMD returns non-zero if violations found, that's OK
        if os.path.exists(output_path):
            with open(output_path, 'r', encoding='utf-8') as f:
                return f.read()
        
        return None
        
    except subprocess.TimeoutExpired:
        print("❌ PMD analysis timed out")
        return None
    except Exception as e:
        print(f"❌ Error running PMD: {e}")
        return None
    finally:
        if os.path.exists(output_path):
            os.unlink(output_path)

# ═══════════════════════════════════════════════════════════════════════════════
# PMD Output Parsing
# ═══════════════════════════════════════════════════════════════════════════════

def parse_pmd_xml(xml_content: str) -> List[CodeSmellIssue]:
    """Parse PMD XML output into CodeSmellIssue objects"""
    issues = []
    
    try:
        root = ET.fromstring(xml_content)
        
        for file_elem in root.findall('.//file'):
            file_path = file_elem.get('name', '')
            
            # Extract class name from file path
            class_name = Path(file_path).stem
            
            for violation in file_elem.findall('violation'):
                rule_name = violation.get('rule', '')
                smell_type = RULE_TO_SMELL.get(rule_name, 'Other')
                
                issue = CodeSmellIssue(
                    file_path=file_path,
                    class_name=class_name,
                    method_name=violation.get('method'),
                    line_number=int(violation.get('beginline', 0)),
                    smell_type=smell_type,
                    rule_name=rule_name,
                    message=violation.text.strip() if violation.text else '',
                    priority=int(violation.get('priority', 3)),
                    category=violation.get('ruleset', 'Design')
                )
                issues.append(issue)
                
    except ET.ParseError as e:
        print(f"❌ Failed to parse PMD output: {e}")
    
    return issues

def aggregate_smells(issues: List[CodeSmellIssue]) -> Dict[str, SmellSummary]:
    """Aggregate issues by file/class"""
    by_file = defaultdict(list)
    
    for issue in issues:
        by_file[issue.file_path].append(issue)
    
    summaries = {}
    
    for file_path, file_issues in by_file.items():
        class_name = Path(file_path).stem
        
        # Count smell types
        smell_counts = defaultdict(int)
        for issue in file_issues:
            smell_counts[issue.smell_type] += 1
        
        # Determine primary smell (most severe)
        smell_priority = ["GodClass", "LongMethod", "FeatureEnvy", "DataClass", 
                         "HighCoupling", "DeadCode", "DeepNesting", "LongParameterList"]
        
        primary_smell = "Clean"
        for smell in smell_priority:
            if smell in smell_counts:
                primary_smell = smell
                break
        
        # Calculate metrics from issues
        metrics = {
            "total_issues": len(file_issues),
            "smell_types": dict(smell_counts),
            "high_priority_issues": sum(1 for i in file_issues if i.priority <= 2),
        }
        
        summaries[file_path] = SmellSummary(
            file_path=file_path,
            class_name=class_name,
            smells=list(smell_counts.keys()),
            primary_smell=primary_smell,
            issues=file_issues,
            metrics=metrics
        )
    
    return summaries

# ═══════════════════════════════════════════════════════════════════════════════
# Main Analysis Functions
# ═══════════════════════════════════════════════════════════════════════════════

def analyze_java_source(source_path: str) -> Dict[str, SmellSummary]:
    """
    Analyze Java source code for code smells using PMD.
    
    Args:
        source_path: Path to Java file or directory
        
    Returns:
        Dictionary mapping file paths to SmellSummary objects
    """
    print(f"\n🔍 Analyzing: {source_path}")
    
    # Check prerequisites
    if not check_java_installed():
        print("❌ Java is not installed. Please install Java 11+ first.")
        return {}
    
    # Run PMD
    xml_output = run_pmd(source_path)
    if not xml_output:
        print("⚠️ No PMD output generated")
        return {}
    
    # Parse results
    issues = parse_pmd_xml(xml_output)
    print(f"📊 Found {len(issues)} potential issues")
    
    # Aggregate by file
    summaries = aggregate_smells(issues)
    
    return summaries

def analyze_single_file(java_code: str, temp_filename: str = "TempClass.java") -> Optional[SmellSummary]:
    """
    Analyze a single Java code snippet.
    
    Args:
        java_code: Java source code as string
        temp_filename: Name for temporary file
        
    Returns:
        SmellSummary for the code, or None if analysis failed
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file = Path(tmpdir) / temp_filename
        temp_file.write_text(java_code, encoding='utf-8')
        
        summaries = analyze_java_source(str(temp_file))
        
        if summaries:
            return list(summaries.values())[0]
    
    return None

def print_analysis_report(summaries: Dict[str, SmellSummary]):
    """Print a formatted analysis report"""
    print("\n" + "=" * 80)
    print("📋 CODE SMELL ANALYSIS REPORT")
    print("=" * 80)
    
    # Summary statistics
    total_files = len(summaries)
    total_issues = sum(s.metrics['total_issues'] for s in summaries.values())
    
    smell_totals = defaultdict(int)
    for summary in summaries.values():
        for smell, count in summary.metrics['smell_types'].items():
            smell_totals[smell] += count
    
    print(f"\n📁 Files analyzed: {total_files}")
    print(f"⚠️  Total issues: {total_issues}")
    
    print("\n📊 Issues by Smell Type:")
    for smell, count in sorted(smell_totals.items(), key=lambda x: -x[1]):
        desc = SMELL_CATEGORIES.get(smell, "")
        print(f"   {smell:20s}: {count:4d}  - {desc}")
    
    # Top offending files
    print("\n🔥 Top Files with Most Issues:")
    sorted_files = sorted(summaries.values(), 
                         key=lambda x: x.metrics['total_issues'], 
                         reverse=True)[:10]
    
    for summary in sorted_files:
        print(f"\n   📄 {summary.class_name}")
        print(f"      Primary Smell: {summary.primary_smell}")
        print(f"      Total Issues: {summary.metrics['total_issues']}")
        print(f"      Smells: {', '.join(summary.smells)}")

def export_results(summaries: Dict[str, SmellSummary], output_path: str):
    """Export analysis results to JSON"""
    export_data = {
        "total_files": len(summaries),
        "total_issues": sum(s.metrics['total_issues'] for s in summaries.values()),
        "files": {}
    }
    
    for file_path, summary in summaries.items():
        export_data["files"][file_path] = {
            "class_name": summary.class_name,
            "primary_smell": summary.primary_smell,
            "all_smells": summary.smells,
            "metrics": summary.metrics,
            "issues": [asdict(i) for i in summary.issues]
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
        print("\nUsage: python pmd_analyzer.py <path_to_java_source>")
        print("       python pmd_analyzer.py <path> --output results.json")
        sys.exit(1)
    
    source_path = sys.argv[1]
    output_path = None
    
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]
    
    if not os.path.exists(source_path):
        print(f"❌ Path not found: {source_path}")
        sys.exit(1)
    
    # Run analysis
    summaries = analyze_java_source(source_path)
    
    if summaries:
        print_analysis_report(summaries)
        
        if output_path:
            export_results(summaries, output_path)
    else:
        print("\n✨ No code smells detected!")

if __name__ == "__main__":
    main()
