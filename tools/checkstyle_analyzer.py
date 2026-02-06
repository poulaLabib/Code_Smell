"""
Checkstyle Code Smell Analyzer
==============================
Integrates Checkstyle static analysis tool to detect code smells.

Checkstyle can detect:
  - MethodLength (LongMethod)
  - CyclomaticComplexity
  - NPathComplexity
  - ClassFanOutComplexity (Coupling)
  - ClassDataAbstractionCoupling
  - NestedIfDepth / NestedForDepth / NestedTryDepth
  - ParameterNumber
  - BooleanExpressionComplexity
  - JavaNCSS (Non-Commenting Source Statements)
  - ExecutableStatementCount
  - AnonInnerLength
  - FileLength

Requirements:
  - Java 11+ installed
  - Checkstyle JAR (will be downloaded automatically)

Usage:
  python checkstyle_analyzer.py <path_to_java_file_or_directory>
"""

import os
import sys
import json
import subprocess
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict

# ═══════════════════════════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════════════════════════

SCRIPT_DIR = Path(__file__).parent.absolute()
CHECKSTYLE_VERSION = "10.12.5"
CHECKSTYLE_URL = f"https://github.com/checkstyle/checkstyle/releases/download/checkstyle-{CHECKSTYLE_VERSION}/checkstyle-{CHECKSTYLE_VERSION}-all.jar"
CHECKSTYLE_DIR = SCRIPT_DIR / "checkstyle"
CHECKSTYLE_JAR = CHECKSTYLE_DIR / f"checkstyle-{CHECKSTYLE_VERSION}-all.jar"

# Checkstyle Configuration for Code Smell Detection
CHECKSTYLE_CONFIG = """<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <property name="charset" value="UTF-8"/>
    <property name="severity" value="warning"/>

    <module name="TreeWalker">
        
        <!-- Method Length - LongMethod Detection -->
        <module name="MethodLength">
            <property name="max" value="50"/>
            <property name="countEmpty" value="false"/>
        </module>
        
        <!-- Cyclomatic Complexity -->
        <module name="CyclomaticComplexity">
            <property name="max" value="10"/>
            <property name="switchBlockAsSingleDecisionPoint" value="true"/>
        </module>
        
        <!-- NPath Complexity -->
        <module name="NPathComplexity">
            <property name="max" value="200"/>
        </module>
        
        <!-- Class Fan-Out Complexity (Coupling) -->
        <module name="ClassFanOutComplexity">
            <property name="max" value="20"/>
        </module>
        
        <!-- Class Data Abstraction Coupling -->
        <module name="ClassDataAbstractionCoupling">
            <property name="max" value="10"/>
        </module>
        
        <!-- Nested If Depth -->
        <module name="NestedIfDepth">
            <property name="max" value="3"/>
        </module>
        
        <!-- Nested For Depth -->
        <module name="NestedForDepth">
            <property name="max" value="3"/>
        </module>
        
        <!-- Nested Try Depth -->
        <module name="NestedTryDepth">
            <property name="max" value="2"/>
        </module>
        
        <!-- Parameter Number -->
        <module name="ParameterNumber">
            <property name="max" value="7"/>
            <property name="ignoreOverriddenMethods" value="true"/>
        </module>
        
        <!-- Boolean Expression Complexity -->
        <module name="BooleanExpressionComplexity">
            <property name="max" value="5"/>
        </module>
        
        <!-- Java NCSS (Non-Commenting Source Statements) -->
        <module name="JavaNCSS">
            <property name="methodMaximum" value="50"/>
            <property name="classMaximum" value="500"/>
            <property name="fileMaximum" value="1000"/>
        </module>
        
        <!-- Executable Statement Count -->
        <module name="ExecutableStatementCount">
            <property name="max" value="30"/>
        </module>
        
        <!-- Anonymous Inner Class Length -->
        <module name="AnonInnerLength">
            <property name="max" value="40"/>
        </module>
        
        <!-- Method Count (Too Many Methods) -->
        <module name="MethodCount">
            <property name="maxTotal" value="30"/>
            <property name="maxPrivate" value="15"/>
            <property name="maxPublic" value="20"/>
        </module>
        
        <!-- Return Count (multiple returns) -->
        <module name="ReturnCount">
            <property name="max" value="5"/>
            <property name="maxForVoid" value="3"/>
        </module>
        
        <!-- Throws Count -->
        <module name="ThrowsCount">
            <property name="max" value="4"/>
        </module>
        
    </module>
    
    <!-- File Length -->
    <module name="FileLength">
        <property name="max" value="500"/>
    </module>
    
</module>
"""

# ═══════════════════════════════════════════════════════════════════════════════
# Data Classes
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class CheckstyleIssue:
    """Represents a code smell detected by Checkstyle"""
    file_path: str
    line_number: int
    column: int
    severity: str
    check_name: str
    message: str
    smell_type: str

@dataclass 
class CheckstyleSummary:
    """Summary of Checkstyle findings for a file"""
    file_path: str
    class_name: str
    smells: List[str]
    primary_smell: str
    issues: List[CheckstyleIssue]
    metrics: Dict

# ═══════════════════════════════════════════════════════════════════════════════
# Checkstyle Check to Smell Mapping
# ═══════════════════════════════════════════════════════════════════════════════

CHECK_TO_SMELL = {
    # Method/Class Size
    "MethodLength": "LongMethod",
    "FileLength": "GodClass",
    "JavaNCSS": "LongMethod",
    "ExecutableStatementCount": "LongMethod",
    "AnonInnerLength": "LongMethod",
    "MethodCount": "GodClass",
    
    # Complexity
    "CyclomaticComplexity": "LongMethod",
    "NPathComplexity": "LongMethod",
    "BooleanExpressionComplexity": "ComplexConditional",
    
    # Coupling
    "ClassFanOutComplexity": "HighCoupling",
    "ClassDataAbstractionCoupling": "HighCoupling",
    
    # Nesting
    "NestedIfDepth": "DeepNesting",
    "NestedForDepth": "DeepNesting",
    "NestedTryDepth": "DeepNesting",
    
    # Parameters
    "ParameterNumber": "LongParameterList",
    
    # Others
    "ReturnCount": "ComplexMethod",
    "ThrowsCount": "ComplexMethod",
}

SMELL_DESCRIPTIONS = {
    "LongMethod": "Method is too long or too complex",
    "GodClass": "Class is too large - violates Single Responsibility Principle",
    "HighCoupling": "Class has too many dependencies on other classes",
    "DeepNesting": "Too many levels of nested control structures",
    "LongParameterList": "Method has too many parameters",
    "ComplexConditional": "Boolean expressions are too complex",
    "ComplexMethod": "Method has too many exit points or exception types",
    "Clean": "No significant code smells detected",
}

# ═══════════════════════════════════════════════════════════════════════════════
# Checkstyle Setup & Execution
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

def download_checkstyle() -> bool:
    """Download Checkstyle JAR if not present"""
    if CHECKSTYLE_JAR.exists():
        print(f"✓ Checkstyle already installed at {CHECKSTYLE_DIR}")
        return True
    
    print(f"📥 Downloading Checkstyle {CHECKSTYLE_VERSION}...")
    CHECKSTYLE_DIR.mkdir(parents=True, exist_ok=True)
    
    try:
        urllib.request.urlretrieve(CHECKSTYLE_URL, CHECKSTYLE_JAR)
        print(f"✓ Checkstyle installed at {CHECKSTYLE_DIR}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to download Checkstyle: {e}")
        return False

def create_config_file() -> Path:
    """Create Checkstyle configuration file"""
    config_path = CHECKSTYLE_DIR / "codesmell_checks.xml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(CHECKSTYLE_CONFIG, encoding='utf-8')
    return config_path

def run_checkstyle(source_path: str) -> Optional[str]:
    """Run Checkstyle analysis on source code"""
    if not CHECKSTYLE_JAR.exists():
        if not download_checkstyle():
            return None
    
    config_path = create_config_file()
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        output_path = f.name
    
    try:
        cmd = [
            "java",
            "-jar", str(CHECKSTYLE_JAR),
            "-c", str(config_path),
            "-f", "xml",
            "-o", output_path,
            source_path
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        # Checkstyle returns non-zero if violations found
        if os.path.exists(output_path):
            with open(output_path, 'r', encoding='utf-8') as f:
                return f.read()
        
        return None
        
    except subprocess.TimeoutExpired:
        print("❌ Checkstyle analysis timed out")
        return None
    except Exception as e:
        print(f"❌ Error running Checkstyle: {e}")
        return None
    finally:
        if os.path.exists(output_path):
            os.unlink(output_path)

# ═══════════════════════════════════════════════════════════════════════════════
# Checkstyle Output Parsing
# ═══════════════════════════════════════════════════════════════════════════════

def parse_checkstyle_xml(xml_content: str) -> List[CheckstyleIssue]:
    """Parse Checkstyle XML output into CheckstyleIssue objects"""
    issues = []
    
    try:
        root = ET.fromstring(xml_content)
        
        for file_elem in root.findall('.//file'):
            file_path = file_elem.get('name', '')
            
            for error in file_elem.findall('error'):
                source = error.get('source', '')
                # Extract check name from source (e.g., "...checks.sizes.MethodLengthCheck")
                check_name = source.split('.')[-1].replace('Check', '')
                smell_type = CHECK_TO_SMELL.get(check_name, 'Other')
                
                issue = CheckstyleIssue(
                    file_path=file_path,
                    line_number=int(error.get('line', 0)),
                    column=int(error.get('column', 0)),
                    severity=error.get('severity', 'warning'),
                    check_name=check_name,
                    message=error.get('message', ''),
                    smell_type=smell_type
                )
                issues.append(issue)
                
    except ET.ParseError as e:
        print(f"❌ Failed to parse Checkstyle output: {e}")
    
    return issues

def aggregate_checkstyle_smells(issues: List[CheckstyleIssue]) -> Dict[str, CheckstyleSummary]:
    """Aggregate issues by file"""
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
        
        # Determine primary smell
        smell_priority = ["GodClass", "LongMethod", "HighCoupling", "DeepNesting", 
                         "LongParameterList", "ComplexConditional", "ComplexMethod"]
        
        primary_smell = "Clean"
        for smell in smell_priority:
            if smell in smell_counts:
                primary_smell = smell
                break
        
        metrics = {
            "total_issues": len(file_issues),
            "smell_types": dict(smell_counts),
            "error_count": sum(1 for i in file_issues if i.severity == 'error'),
            "warning_count": sum(1 for i in file_issues if i.severity == 'warning'),
        }
        
        summaries[file_path] = CheckstyleSummary(
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

def analyze_with_checkstyle(source_path: str) -> Dict[str, CheckstyleSummary]:
    """
    Analyze Java source code for code smells using Checkstyle.
    
    Args:
        source_path: Path to Java file or directory
        
    Returns:
        Dictionary mapping file paths to CheckstyleSummary objects
    """
    print(f"\n🔍 Analyzing with Checkstyle: {source_path}")
    
    # Check prerequisites
    if not check_java_installed():
        print("❌ Java is not installed. Please install Java 11+ first.")
        return {}
    
    # Run Checkstyle
    xml_output = run_checkstyle(source_path)
    if not xml_output:
        print("⚠️ No Checkstyle output generated")
        return {}
    
    # Parse results
    issues = parse_checkstyle_xml(xml_output)
    print(f"📊 Found {len(issues)} potential issues")
    
    # Aggregate by file
    summaries = aggregate_checkstyle_smells(issues)
    
    return summaries

def analyze_code_string(java_code: str, temp_filename: str = "TempClass.java") -> Optional[CheckstyleSummary]:
    """
    Analyze a single Java code snippet.
    
    Args:
        java_code: Java source code as string
        temp_filename: Name for temporary file
        
    Returns:
        CheckstyleSummary for the code, or None if analysis failed
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file = Path(tmpdir) / temp_filename
        temp_file.write_text(java_code, encoding='utf-8')
        
        summaries = analyze_with_checkstyle(str(temp_file))
        
        if summaries:
            return list(summaries.values())[0]
    
    return None

def print_checkstyle_report(summaries: Dict[str, CheckstyleSummary]):
    """Print a formatted analysis report"""
    print("\n" + "=" * 80)
    print("📋 CHECKSTYLE CODE SMELL ANALYSIS REPORT")
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
        desc = SMELL_DESCRIPTIONS.get(smell, "")
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

def export_checkstyle_results(summaries: Dict[str, CheckstyleSummary], output_path: str):
    """Export analysis results to JSON"""
    export_data = {
        "tool": "Checkstyle",
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
        print("\nUsage: python checkstyle_analyzer.py <path_to_java_source>")
        print("       python checkstyle_analyzer.py <path> --output results.json")
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
    summaries = analyze_with_checkstyle(source_path)
    
    if summaries:
        print_checkstyle_report(summaries)
        
        if output_path:
            export_checkstyle_results(summaries, output_path)
    else:
        print("\n✨ No code smells detected!")

if __name__ == "__main__":
    main()
