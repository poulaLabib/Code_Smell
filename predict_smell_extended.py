"""
🔍 EXTENDED CODE SMELL PREDICTOR
=================================
Analyzes Java code for a comprehensive set of code smells using:
  - ML Models (trained on your dataset)
  - CK Metrics (pure Python)
  - PMD Static Analysis (optional, requires Java)
  - Checkstyle (optional, requires Java)

This is an enhanced version of predict_smell.py that detects MORE code smells!

Detected Code Smells:
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PRIMARY (ML + Metrics based):
    ✓ GodClass - Class doing too much
    ✓ DataClass - Mostly data, little behavior  
    ✓ LongMethod - Method too long/complex
    ✓ FeatureEnvy - Uses other class's data too much
    ✓ Clean - No smell detected
  
  EXTENDED (via PMD/Checkstyle integration):
    ✓ LongParameterList - Too many parameters
    ✓ DeepNesting - Too many nested control structures
    ✓ HighCoupling - Too many dependencies
    ✓ ComplexConditional - Boolean expressions too complex
    ✓ MessageChain - Train wreck code (a.b().c().d())
    ✓ DuplicatedCode - Copy-paste code
    ✓ LazyClass - Class doesn't do enough
    ✓ RefusedBequest - Subclass ignores parent methods
    ✓ MiddleMan - Just delegates to another class
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Usage:
    python predict_smell_extended.py  [interactive mode]
    python predict_smell_extended.py <file.java>
    python predict_smell_extended.py <directory>
    python predict_smell_extended.py --use-pmd --use-checkstyle

Requirements:
    - Python 3.8+
    - scikit-learn, joblib, numpy (pip install scikit-learn joblib numpy)
    - Java 11+ (optional, for PMD/Checkstyle)
"""

import os
import sys
import json
import re
import csv
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

# Add paths
SCRIPT_DIR = Path(__file__).parent.absolute()
BASE = SCRIPT_DIR.parent if SCRIPT_DIR.name == "tools" else SCRIPT_DIR
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(BASE / "tools"))

# Try to import ML models
try:
    import joblib
    HAS_JOBLIB = True
except ImportError:
    HAS_JOBLIB = False
    print("⚠️ joblib not installed. ML models unavailable. Run: pip install joblib")

# Try to import unified detector
try:
    from unified_detector import UnifiedSmellDetector, SMELL_DEFINITIONS
    HAS_UNIFIED = True
except ImportError:
    HAS_UNIFIED = False

# ═══════════════════════════════════════════════════════════════════════════════
# Colors for Terminal
# ═══════════════════════════════════════════════════════════════════════════════

class Colors:
    if os.name == 'nt':
        os.system('')
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
    return ''.join(styles) + str(text) + Colors.END


# ═══════════════════════════════════════════════════════════════════════════════
# Smell Definitions
# ═══════════════════════════════════════════════════════════════════════════════

# Model's training labels (MUST match ultimate_model.py exactly)
# DeadCode removed from ML - now purely static/rule-based detection
MODEL_SMELLS = ["Clean", "DataClass", "FeatureEnvy", "GodClass", "LongMethod"]

# Primary smells from ML model
PRIMARY_SMELLS = ["Clean", "DataClass", "FeatureEnvy", "GodClass", "LongMethod"]

# Extended smells detected via static analysis (including DeadCode)
EXTENDED_SMELLS = [
    "DeadCode", "LongParameterList", "DeepNesting", "HighCoupling", "ComplexConditional",
    "MessageChain", "DuplicatedCode", "LazyClass", "RefusedBequest", "MiddleMan"
]

ALL_SMELLS = PRIMARY_SMELLS + EXTENDED_SMELLS

SMELL_INFO = {
    "Clean": {
        "icon": "✨", "color": Colors.GREEN,
        "description": "No significant code smell detected",
        "recommendation": "Great job! The code follows good design principles."
    },
    "LowMaintainability": {
        "icon": "⚠️", "color": Colors.YELLOW,
        "description": "Code has multiple maintainability issues that should be addressed",
        "recommendation": "Address the issues listed below to improve code quality."
    },
    "GodClass": {
        "icon": "👑", "color": Colors.RED,
        "description": "Class is doing too much - violates Single Responsibility Principle",
        "recommendation": "Split into smaller, focused classes. Each class should have one reason to change."
    },
    "DataClass": {
        "icon": "📦", "color": Colors.YELLOW,
        "description": "Class mostly contains data with little behavior (getters/setters only)",
        "recommendation": "Add behavior that operates on this data, or use Java Records (14+)."
    },
    "LongMethod": {
        "icon": "📏", "color": Colors.YELLOW,
        "description": "Method is too long or too complex",
        "recommendation": "Break down into smaller methods with clear, descriptive names."
    },
    "FeatureEnvy": {
        "icon": "👀", "color": Colors.YELLOW,
        "description": "Method uses another class's data more than its own",
        "recommendation": "Move this method to the class whose data it primarily uses."
    },
    "LongParameterList": {
        "icon": "📋", "color": Colors.YELLOW,
        "description": "Method has too many parameters (usually > 5-7)",
        "recommendation": "Introduce Parameter Object or use Builder pattern."
    },
    "DeepNesting": {
        "icon": "🪆", "color": Colors.YELLOW,
        "description": "Too many levels of nested control structures",
        "recommendation": "Use early returns (guard clauses), extract methods, or use polymorphism."
    },
    "HighCoupling": {
        "icon": "🔗", "color": Colors.YELLOW,
        "description": "Class has too many dependencies on other classes",
        "recommendation": "Apply Dependency Injection, use interfaces, consider Facade pattern."
    },
    "ComplexConditional": {
        "icon": "❓", "color": Colors.CYAN,
        "description": "Boolean expressions are too complex",
        "recommendation": "Extract conditions into well-named methods or use Strategy pattern."
    },
    "MessageChain": {
        "icon": "⛓️", "color": Colors.CYAN,
        "description": "Long chain of method calls (a.b().c().d())",
        "recommendation": "Hide delegate behind wrapper method, apply Tell Don't Ask."
    },
    "DuplicatedCode": {
        "icon": "📑", "color": Colors.YELLOW,
        "description": "Same code appears in multiple places",
        "recommendation": "Extract common code to shared method or use Template Method pattern."
    },
    "LazyClass": {
        "icon": "😴", "color": Colors.CYAN,
        "description": "Class doesn't do enough to justify its existence",
        "recommendation": "Merge with related class or add more meaningful behavior."
    },
    "RefusedBequest": {
        "icon": "🙅", "color": Colors.CYAN,
        "description": "Subclass doesn't use inherited methods/data properly",
        "recommendation": "Use composition instead of inheritance, or extract interface."
    },
    "MiddleMan": {
        "icon": "🤷", "color": Colors.CYAN,
        "description": "Class just delegates to another class",
        "recommendation": "Remove the middle man or add real behavior."
    },
    "BadNaming": {
        "icon": "🏷️", "color": Colors.YELLOW,
        "description": "Uncommunicative/mysterious names make code hard to understand",
        "recommendation": "Use descriptive names: 'userName' not 'u', 'processOrder()' not 'doIt()'."
    },
    "MagicNumbers": {
        "icon": "🔢", "color": Colors.YELLOW,
        "description": "Hard-coded numeric literals without named constants",
        "recommendation": "Replace magic numbers with named constants (e.g., MAX_RETRIES = 3)."
    },
    "GlobalMutableState": {
        "icon": "🌍", "color": Colors.RED,
        "description": "Public static mutable fields cause unpredictable behavior",
        "recommendation": "Use encapsulation, dependency injection, or immutable state."
    },
    "RawCollections": {
        "icon": "📥", "color": Colors.YELLOW,
        "description": "Collections without generic type parameters cause type safety issues",
        "recommendation": "Add generics: List<String> instead of raw List."
    },
    "SwallowedException": {
        "icon": "🔥", "color": Colors.RED,
        "description": "Exceptions being caught and ignored silently",
        "recommendation": "Log the exception, rethrow, or handle meaningfully - never ignore."
    },
    "DeadCode": {
        "icon": "💀", "color": Colors.RED,
        "description": "Code that can never execute (e.g., if(false), code after return)",
        "recommendation": "Remove dead code to improve maintainability and reduce confusion."
    },
    "DuplicateCode": {
        "icon": "📑", "color": Colors.YELLOW,
        "description": "Same logic repeated in multiple places",
        "recommendation": "Extract common code to a reusable method."
    },
    "PointlessLoop": {
        "icon": "🔄", "color": Colors.YELLOW,
        "description": "Loop has no net effect on state",
        "recommendation": "Remove pointless loops or fix the logic."
    },
    "UnnecessaryBoxing": {
        "icon": "📦", "color": Colors.CYAN,
        "description": "Deprecated wrapper constructors (new Integer() etc.)",
        "recommendation": "Use Integer.valueOf() or primitive types instead."
    },
    "StringConcatInLoop": {
        "icon": "🧵", "color": Colors.YELLOW,
        "description": "String concatenation in loop is inefficient",
        "recommendation": "Use StringBuilder for better performance."
    },
    "GodMethod": {
        "icon": "🐙", "color": Colors.RED,
        "description": "Method doing too many different things",
        "recommendation": "Split into smaller methods - each doing one thing well."
    }
}


# ═══════════════════════════════════════════════════════════════════════════════
# CK Metrics Loading (from pre-computed CSV files)
# ═══════════════════════════════════════════════════════════════════════════════

CK_COLS = ['LOC', 'WMC', 'METHODS', 'FIELDS', 'PRIVATE_METHODS', 
           'CBO', 'DIT', 'LCOM', 'TCC', 'ATFD', 'MAX_METHOD_LOC', 'NOC']

# Global cache for CK metrics
_CK_METRICS_CACHE = {}

def load_ck_metrics_cache():
    """Load all CK metrics from CSV files into memory."""
    global _CK_METRICS_CACHE
    if _CK_METRICS_CACHE:
        return _CK_METRICS_CACHE
    
    ck_dir = BASE / "ck_metrics"
    if not ck_dir.exists():
        return {}
    
    for csv_file in ck_dir.glob("*_ck.csv"):
        try:
            with open(csv_file, 'r', encoding='utf-8', errors='ignore') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Normalize file path for matching
                    file_path = row.get('file_path', '')
                    class_name = row.get('class_name', '')
                    
                    # Create keys for lookup
                    if file_path:
                        # Key by filename
                        fname = Path(file_path).name
                        key = fname.lower()
                        _CK_METRICS_CACHE[key] = row
                        
                        # Also key by class name
                        if class_name:
                            _CK_METRICS_CACHE[class_name.lower() + '.java'] = row
        except Exception as e:
            print(f"⚠️ Error loading {csv_file}: {e}")
    
    return _CK_METRICS_CACHE

def get_ck_metrics_for_file(file_path: str) -> Optional[Dict]:
    """Look up pre-computed CK metrics for a file."""
    cache = load_ck_metrics_cache()
    if not cache:
        return None
    
    # Try different matching strategies
    fname = Path(file_path).name.lower()
    
    # Direct filename match
    if fname in cache:
        row = cache[fname]
        return {col: float(row.get(col, 0) or 0) for col in CK_COLS}
    
    return None


def extract_metrics(code: str, file_path: str = None) -> Dict:
    """
    Extract CK metrics from Java code.
    
    First tries to use pre-computed CK metrics (accurate).
    Falls back to regex-based extraction (approximate).
    """
    # Try to use real CK metrics first
    if file_path:
        real_metrics = get_ck_metrics_for_file(file_path)
        if real_metrics:
            return real_metrics
    
    # Fallback: regex-based extraction (APPROXIMATE)
    # Mark as approximate so we can use rule-based detection instead of ML
    metrics = {'_approximate': True}
    
    # ====================================================================
    # DETECT CLASS TYPE EARLY (for accurate metrics)
    # ====================================================================
    class_type = "class"
    if re.search(r'\benum\s+\w+', code):
        class_type = "enum"
    elif re.search(r'\binterface\s+\w+', code):
        class_type = "interface"
    elif re.search(r'\babstract\s+class\s+\w+', code):
        class_type = "abstract_class"
    metrics['class_type'] = class_type
    
    lines = code.split('\n')
    non_empty = [l for l in lines if l.strip() and not l.strip().startswith('//')]
    metrics['LOC'] = len(non_empty)
    
    # ====================================================================
    # SPECIAL HANDLING FOR ENUMS
    # ====================================================================
    if class_type == "enum":
        # Enums don't have traditional methods/fields like classes
        enum_values = len(re.findall(r'^\s*\w+\s*[,;(]', code, re.MULTILINE))
        enum_methods = re.findall(r'(public|private|protected)?\s*\w+\s+\w+\s*\([^)]*\)\s*\{', code)
        metrics['METHODS'] = len(enum_methods)
        metrics['FIELDS'] = 0  # Enum constants aren't really "fields"
        metrics['ENUM_VALUES'] = enum_values
        metrics['WMC'] = len(enum_methods)  # WMC = number of methods for enums
        metrics['CBO'] = 0  # Enums typically have no coupling
        metrics['DIT'] = 0
        metrics['RFC'] = len(enum_methods)  # RFC = own methods for enums
        metrics['LCOM'] = 0
        metrics['TCC'] = 1.0  # Perfect cohesion for enums
        metrics['ATFD'] = 0
        metrics['MAX_METHOD_LOC'] = 0
        metrics['NOC'] = 0
        metrics['PRIVATE_METHODS'] = 0
        return metrics
    
    # ====================================================================
    # SPECIAL HANDLING FOR INTERFACES
    # ====================================================================
    if class_type == "interface":
        # Interfaces have method signatures, not implementations
        interface_methods = re.findall(r'(public\s+)?\w+\s+\w+\s*\([^)]*\)\s*;', code)
        default_methods = re.findall(r'default\s+\w+\s+\w+\s*\([^)]*\)\s*\{', code)
        metrics['METHODS'] = len(interface_methods) + len(default_methods)
        metrics['FIELDS'] = 0  # Interface constants aren't counted as fields
        metrics['WMC'] = len(default_methods)  # Only default methods have complexity
        metrics['CBO'] = 0  # Interfaces define contracts, not coupling
        metrics['DIT'] = 0
        metrics['RFC'] = len(interface_methods) + len(default_methods)  # RFC = all method signatures
        metrics['LCOM'] = 0
        metrics['TCC'] = 1.0  # Perfect cohesion for interfaces
        metrics['ATFD'] = 0
        metrics['MAX_METHOD_LOC'] = 0
        metrics['NOC'] = 0
        metrics['PRIVATE_METHODS'] = 0
        return metrics
    
    # ====================================================================
    # REGULAR CLASS METRICS
    # ====================================================================
    # Methods - improved pattern to catch constructors too
    method_pattern = r'(public|private|protected)?\s*(static\s+)?(final\s+)?(\w+)\s+(\w+)\s*\([^)]*\)\s*(throws\s+[\w,\s]+)?\s*\{'
    methods = re.findall(method_pattern, code)
    # Also find constructors (ClassName followed by params)
    class_match = re.search(r'class\s+(\w+)', code)
    class_name = class_match.group(1) if class_match else None
    if class_name:
        constructor_pattern = rf'(public|private|protected)?\s*{class_name}\s*\([^)]*\)\s*\{{'
        constructors = re.findall(constructor_pattern, code)
        metrics['METHODS'] = max(len(methods) + len(constructors), 1)
    else:
        metrics['METHODS'] = max(len(methods), 1)
    
    # Private methods
    private_methods = re.findall(r'private\s+\w+\s+\w+\s*\([^)]*\)\s*\{', code)
    metrics['PRIVATE_METHODS'] = len(private_methods)
    
    # Fields - count public/private/protected field declarations
    field_pattern = r'(private|public|protected)\s+(static\s+)?(final\s+)?([\w<>,\[\]\s]+)\s+(\w+)\s*(=|;)'
    fields = re.findall(field_pattern, code)
    metrics['FIELDS'] = len(fields)
    
    # WMC - Weighted Method Complexity (count decision points)
    wmc = metrics['METHODS']
    wmc += len(re.findall(r'\bif\s*\(', code))
    wmc += len(re.findall(r'\belse\s+if\s*\(', code))
    wmc += len(re.findall(r'\bwhile\s*\(', code))
    wmc += len(re.findall(r'\bfor\s*\(', code))
    wmc += len(re.findall(r'\bcase\s+', code))
    wmc += len(re.findall(r'\bcatch\s*\(', code))
    wmc += len(re.findall(r'&&', code))
    wmc += len(re.findall(r'\|\|', code))
    wmc += len(re.findall(r'\?[^?:]', code))  # Ternary
    metrics['WMC'] = wmc
    
    # CBO - count external type references
    imports = re.findall(r'import\s+([\w.]+);', code)
    types = set(re.findall(r'[<(,\s]([A-Z][a-zA-Z0-9]*)[>\s,)\[]', code))
    common = {'String', 'Integer', 'Long', 'Double', 'Float', 'Boolean', 
             'List', 'Map', 'Set', 'ArrayList', 'HashMap', 'Object', 'Exception',
             'System', 'Override'}
    types -= common
    if class_name:
        types.discard(class_name)
    metrics['CBO'] = len(imports) + len(types)
    
    # DIT
    extends = re.findall(r'\bextends\s+(\w+)', code)
    implements = re.findall(r'\bimplements\s+([\w,\s]+)', code)
    metrics['DIT'] = len(extends) + (1 if implements else 0)
    
    # LCOM - Lack of Cohesion (estimate based on field usage)
    # Using LCOM1-like: count methods that don't access any instance field
    # High LCOM = low cohesion (methods don't share fields)
    field_matches = re.findall(r'(private|public|protected)\s+(?!static)\w+\s+(\w+)\s*[;=]', code)
    field_names = {f[1] for f in field_matches}
    
    # More robust method body extraction - handle nested braces
    methods_using_fields = 0
    # Find each method and check if it uses any field
    method_pattern = r'(public|private|protected)\s+(?:static\s+)?(?:final\s+)?(?:\w+)\s+(\w+)\s*\([^)]*\)\s*\{'
    for match in re.finditer(method_pattern, code):
        method_start = match.end() - 1  # Start at the opening brace
        brace_count = 1
        method_end = method_start + 1
        
        # Find matching closing brace
        while method_end < len(code) and brace_count > 0:
            if code[method_end] == '{':
                brace_count += 1
            elif code[method_end] == '}':
                brace_count -= 1
            method_end += 1
        
        method_body = code[method_start:method_end]
        
        # Check if method uses any field (including via this.field, return field, etc.)
        for field in field_names:
            # Match: field alone, this.field, return field, field., field[, field =, field)
            if re.search(rf'(?:this\.)?\b{field}\b', method_body):
                methods_using_fields += 1
                break
    
    if metrics['METHODS'] > 1:
        # LCOM = methods that don't use any field
        metrics['LCOM'] = max(0, metrics['METHODS'] - methods_using_fields)
    else:
        metrics['LCOM'] = 0
    
    # TCC - Tight Class Cohesion (what % of method pairs share fields)
    if metrics['METHODS'] > 1 and field_names:
        # Simplified: ratio of methods that use at least one field
        metrics['TCC'] = methods_using_fields / metrics['METHODS']
    else:
        metrics['TCC'] = 0.5
    
    # ATFD - Access To Foreign Data
    getter_calls = len(re.findall(r'(\w+)\.(get|is|has)\w*\(', code))
    setter_calls = len(re.findall(r'(\w+)\.(set|add|put)\w*\(', code))
    metrics['ATFD'] = getter_calls + setter_calls
    
    # RFC - Response For a Class = methods in class + methods called by class
    # Count distinct method calls (methodName() pattern)
    method_calls = set(re.findall(r'\b(\w+)\s*\(', code))
    # Remove common keywords/constructors
    keywords = {'if', 'for', 'while', 'switch', 'catch', 'synchronized', 'return',
                'new', 'throw', 'assert', class_name or ''}
    method_calls -= keywords
    # RFC = own methods + external method calls
    metrics['RFC'] = metrics['METHODS'] + len(method_calls)
    
    # MAX_METHOD_LOC - find longest method
    max_loc = 10
    # Find method/constructor bodies
    brace_pattern = r'(public|private|protected)[^{]*\{'
    for match in re.finditer(brace_pattern, code):
        start = match.end()
        depth = 1
        pos = start
        while depth > 0 and pos < len(code):
            if code[pos] == '{': depth += 1
            elif code[pos] == '}': depth -= 1
            pos += 1
        method_text = code[start:pos]
        loc = len([l for l in method_text.split('\n') if l.strip()])
        max_loc = max(max_loc, loc)
    metrics['MAX_METHOD_LOC'] = max_loc
    
    # NOC
    metrics['NOC'] = 0
    
    return metrics


def add_derived_features(metrics: Dict) -> np.ndarray:
    """Convert metrics to feature array with derived features.
    
    MUST match the 32 features from ultimate_model.py exactly:
    - 12 base CK columns
    - 20 derived features
    """
    base = [float(metrics.get(col, 0) or 0) for col in CK_COLS]
    
    # Base metrics with safety (matching ultimate_model.py)
    loc = max(metrics.get('LOC', 1), 1)
    wmc = max(metrics.get('WMC', 1), 1)
    methods = max(metrics.get('METHODS', 1), 1)
    fields = max(metrics.get('FIELDS', 0), 0)
    cbo = max(metrics.get('CBO', 0), 0)
    lcom = max(metrics.get('LCOM', 0), 0)
    max_method_loc = max(metrics.get('MAX_METHOD_LOC', 1), 1)
    atfd = max(metrics.get('ATFD', 0), 0)
    tcc = max(metrics.get('TCC', 0.001), 0.001)
    dit = max(metrics.get('DIT', 0), 0)
    noc = max(metrics.get('NOC', 0), 0)
    private_methods = max(metrics.get('PRIVATE_METHODS', 0), 0)
    
    # 20 derived features - MUST match ultimate_model.py exactly
    derived = [
        # Complexity ratios
        wmc / methods,                      # Avg complexity per method
        loc / methods,                      # Avg LOC per method
        max_method_loc / loc,               # Longest method ratio
        
        # Data class indicators
        fields / (fields + methods + 1),    # Data-heaviness ratio
        fields / methods if methods > 0 else 0,  # Field to method ratio
        
        # God class indicators
        wmc * loc / 1000,                   # Size-complexity product
        cbo * wmc / 100,                    # Coupling * Complexity
        methods * cbo / 100,                # Methods * Coupling
        
        # Feature envy indicators
        atfd / (methods + 1),               # External access per method
        cbo / (methods + 1),                # Coupling per method
        
        # Long method indicators
        max_method_loc,                     # Absolute longest method
        max_method_loc / methods,           # Longest vs avg
        
        # Cohesion indicators
        lcom / (methods + 1),               # Lack of cohesion per method
        1 / (tcc + 0.001),                  # Inverse TCC
        
        # Encapsulation
        private_methods / (methods + 1),    # Encapsulation ratio
        
        # Hierarchy
        dit + noc,                          # Inheritance depth + children
        
        # Interactions (non-linear features)
        np.log1p(loc),                      # Log LOC
        np.log1p(wmc),                      # Log WMC
        np.sqrt(cbo * wmc),                 # Sqrt of coupling-complexity
        loc ** 0.5 * wmc ** 0.5,            # Geometric mean size-complexity
    ]
    
    return np.array(base + derived, dtype=np.float32)


# ═══════════════════════════════════════════════════════════════════════════════
# Extended Smell Detection (Pattern-based)
# ═══════════════════════════════════════════════════════════════════════════════

def detect_extended_smells(code: str, metrics: Dict, class_type: str = "class") -> List[Tuple[str, float, str]]:
    """
    Detect extended smells via pattern analysis.
    
    Args:
        code: Java source code
        metrics: Extracted metrics dict
        class_type: One of 'class', 'interface', 'enum', 'abstract_class'
    """
    detected = []
    
    # ══════════════════════════════════════════════════════════════════════════
    # MAGIC NUMBERS
    # ══════════════════════════════════════════════════════════════════════════
    # Find numeric literals that aren't 0, 1, -1, 2 (common acceptable values)
    magic_pattern = r'[=<>!+\-*/\[\(,]\s*(\d+(?:\.\d+)?)'
    magic_numbers = []
    for match in re.finditer(magic_pattern, code):
        num_str = match.group(1)
        try:
            num = float(num_str) if '.' in num_str else int(num_str)
            # Skip common acceptable values
            if num not in (0, 1, 2, -1, 10, 100, 0.0, 1.0, 2.0):
                magic_numbers.append(num_str)
        except:
            pass
    if len(magic_numbers) >= 2:
        examples = list(set(magic_numbers))[:5]
        detected.append(("MagicNumbers", min(0.5 + len(magic_numbers) * 0.1, 0.9),
                        f"Found magic numbers: {', '.join(examples)}"))
    
    # ══════════════════════════════════════════════════════════════════════════
    # GLOBAL MUTABLE STATE
    # ══════════════════════════════════════════════════════════════════════════
    global_state_pattern = r'public\s+static\s+(?!final)(\w+)\s+(\w+)\s*[=;]'
    global_vars = re.findall(global_state_pattern, code)
    if global_vars:
        names = [name for _, name in global_vars]
        detected.append(("GlobalMutableState", min(0.6 + len(global_vars) * 0.1, 0.95),
                        f"Public static mutable fields: {', '.join(names)}"))
    
    # ══════════════════════════════════════════════════════════════════════════
    # RAW COLLECTIONS (missing generics)
    # ══════════════════════════════════════════════════════════════════════════
    raw_types = r'List|Map|Set|Collection|ArrayList|HashMap|HashSet|LinkedList|Queue|TreeMap|TreeSet|Stack|Vector|LinkedHashMap|LinkedHashSet|Hashtable'
    raw_collection_pattern = rf'\b({raw_types})\s+\w+\s*='
    raw_collections = re.findall(raw_collection_pattern, code)
    generic_pattern = rf'\b({raw_types})\s*<'
    generics = re.findall(generic_pattern, code)
    if raw_collections and len(raw_collections) > len(generics):
        detected.append(("RawCollections", 0.85,
                        f"Found {len(raw_collections)} raw type collections (missing generics)"))
    
    # ══════════════════════════════════════════════════════════════════════════
    # SWALLOWED EXCEPTIONS (empty catch blocks)
    # ══════════════════════════════════════════════════════════════════════════
    # Pattern: catch block with only comments or whitespace
    swallowed_pattern = r'catch\s*\([^)]+\)\s*\{\s*(?://[^\n]*\s*)*\}'
    swallowed = re.findall(swallowed_pattern, code)
    if swallowed:
        detected.append(("SwallowedException", 0.95,
                        f"Found {len(swallowed)} empty catch block(s) - exceptions being ignored"))
    
    # ══════════════════════════════════════════════════════════════════════════
    # DEAD CODE - Only truly unreachable/never-executed code
    # NOTE: Empty catch blocks are SwallowedException, NOT dead code (they execute!)
    # NOTE: We can't reliably detect "code after return" with regex - needs AST parsing
    #       because "return" inside an if-block is followed by valid code in the outer scope
    # ══════════════════════════════════════════════════════════════════════════
    dead_code_patterns = [
        (r'if\s*\(\s*false\s*\)', "if (false) block - never executes"),
        (r'while\s*\(\s*false\s*\)', "while (false) - never executes"),
        # Only match return followed by statement AT SAME INDENTATION (method-level return)
        # This catches: "return x;\n    doSomething();" but NOT conditional returns
        (r'^\s{0,4}return\s+[^;]+;\s*\n\s{0,4}[a-zA-Z_]\w+\s*[=(;]', "code after method-level return"),
    ]
    dead_code_found = []
    for pattern, desc in dead_code_patterns:
        if re.search(pattern, code, re.MULTILINE):
            dead_code_found.append(desc)
    
    # Check for unused private methods (declared but never called)
    private_methods = re.findall(r'private\s+\w+\s+(\w+)\s*\([^)]*\)\s*\{', code)
    unused_private = 0
    for method in private_methods:
        # Count how many times method is called (excluding its declaration)
        calls = len(re.findall(rf'\b{method}\s*\(', code))
        if calls <= 1:  # Only the declaration
            unused_private += 1
    if unused_private >= 2:
        dead_code_found.append(f"{unused_private} unused private methods")
    
    # Check for commented-out code (Java code patterns in comments) - significant amount
    commented_code = len(re.findall(r'//\s*(if|for|while|return|int|String|public|private)\s+\w+', code))
    block_commented_code = len(re.findall(r'/\*[\s\S]*?(if|for|while|return|private|public)[\s\S]*?\*/', code))
    if commented_code >= 5 or block_commented_code >= 2:
        dead_code_found.append("significant commented-out code blocks")
    
    # NOTE: Empty catch blocks are NOT dead code - they execute when exception is thrown
    # They are already detected as SwallowedException
    
    # Check for unused private fields (stricter - must be private and truly unused)
    private_field_names = re.findall(r'private\s+\w+\s+(\w+)\s*[;=]', code)
    unused_fields = 0
    for field in private_field_names:
        refs = len(re.findall(rf'\b{field}\b', code))
        if refs <= 1:  # Only declaration
            unused_fields += 1
    if unused_fields >= 3:  # Stricter threshold
        dead_code_found.append(f"{unused_fields} unused private fields")
    
    # Check for methods with only comments (placeholder/stub methods) - must be multiple
    stub_methods = len(re.findall(r'\)\s*\{\s*(/\*[^}]*\*/|//[^\n]*\n\s*)+\}', code))
    if stub_methods >= 3:  # Stricter threshold
        dead_code_found.append(f"{stub_methods} stub/placeholder methods")
    
    # Only report DeadCode if we have strong evidence
    if dead_code_found:
        # Confidence based on severity of findings
        confidence = 0.75 if len(dead_code_found) == 1 else 0.90
        detected.append(("DeadCode", confidence,
                        f"Found: {', '.join(dead_code_found)}"))
    
    # ══════════════════════════════════════════════════════════════════════════
    # DUPLICATE/REDUNDANT CODE
    # ══════════════════════════════════════════════════════════════════════════
    # Find duplicate consecutive method calls (SAME call twice in a row = likely bug)
    dup_call_pattern = r'(\w+\.\w+\([^)]*\)\s*;)\s*\1'
    dup_calls = re.findall(dup_call_pattern, code)
    
    # Find duplicate statements (min 10 chars to avoid trivial matches)
    # Exclude common patterns that are expected to repeat
    lines = [l.strip() for l in code.split('\n') if l.strip() and not l.strip().startswith('//')]
    line_counts = {}
    for line in lines:
        # Only consider substantial lines (10+ chars)
        if len(line) >= 10 and not line.startswith('}') and not line.startswith('{'):
            # Exclude common repeating patterns that are OK:
            # - System.out.println (output statements are OK to repeat)
            # - @Override, @Deprecated, etc. (annotations)
            # - return this; (builder pattern)
            # - break; continue; return; (control flow)
            # - super(...) calls
            # - this.field = field; (constructor assignments)
            skip_patterns = [
                r'^System\.out\.print',
                r'^@\w+',
                r'^return\s+(this|null|true|false|\d+);?$',
                r'^(break|continue);?$',
                r'^super\s*\(',
                r'^this\.\w+\s*=\s*\w+;$',
                r'^import\s+',
                r'^package\s+',
            ]
            should_skip = any(re.match(pattern, line) for pattern in skip_patterns)
            if not should_skip:
                line_counts[line] = line_counts.get(line, 0) + 1
    
    # Need 4+ identical lines to be considered duplicate (raised from 3)
    duplicates = [l for l, c in line_counts.items() if c >= 4]
    
    # Only flag if we have real consecutive duplicates OR many duplicate lines
    if dup_calls:
        detected.append(("DuplicateCode", 0.7,
                        f"Found {len(dup_calls)} consecutive duplicate call(s)"))
    elif len(duplicates) >= 2:  # Need 2+ different duplicate patterns
        detected.append(("DuplicateCode", min(0.5 + len(duplicates) * 0.1, 0.85),
                        f"Found {len(duplicates)} duplicate statements"))
    
    # ══════════════════════════════════════════════════════════════════════════
    # POINTLESS LOOPS (no net effect)
    # ══════════════════════════════════════════════════════════════════════════
    # Pattern: x = x + something; x = x - something; in same loop
    # Also check for += and -= patterns
    pointless_patterns = [
        r'(for|while)\s*\([^)]+\)\s*\{[^}]*(\w+)\s*=\s*\2\s*\+[^;]+;[^}]*\2\s*=\s*\2\s*-',  # x = x + ...; x = x - ...
        r'(for|while)\s*\([^)]+\)\s*\{[^}]*(\w+)\s*\+=\s*[^;]+;[^}]*\2\s*\-=',  # x += ...; x -= ...
        r'(for|while)\s*\([^)]+\)\s*\{[^}]*(\w+)\s*\*=\s*[^;]+;[^}]*\2\s*/=',    # x *= ...; x /= ...
    ]
    for pattern in pointless_patterns:
        if re.search(pattern, code, re.DOTALL):
            detected.append(("PointlessLoop", 0.9,
                            "Loop has no net effect (increment/decrement cancel out)"))
            break
    
    # ══════════════════════════════════════════════════════════════════════════
    # UNNECESSARY OBJECT CREATION
    # ══════════════════════════════════════════════════════════════════════════
    # new Integer(), new Boolean(), etc. - use primitives or valueOf instead
    deprecated_boxing = r'new\s+(Integer|Boolean|Long|Double|Float|Short|Byte|Character)\s*\('
    boxing_matches = re.findall(deprecated_boxing, code)
    if boxing_matches:
        detected.append(("UnnecessaryBoxing", 0.85,
                        f"Use {', '.join(set(boxing_matches))}.valueOf() instead of new"))
    
    # String concatenation in loops
    string_concat_loop = r'for\s*\([^)]+\)\s*\{[^}]*\+\s*[^+]*String|String[^}]*\+='
    if re.search(r'(for|while)\s*\([^)]+\)\s*\{[^}]*\w+\s*=\s*\w+\s*\+\s*\w+', code):
        # Check if it involves strings
        if 'String' in code and ('+=' in code or '= s' in code.lower()):
            detected.append(("StringConcatInLoop", 0.8,
                            "String concatenation in loop - use StringBuilder"))
    
    # ══════════════════════════════════════════════════════════════════════════
    # GOD METHOD (does too much - many different concerns)
    # ══════════════════════════════════════════════════════════════════════════
    # Check the whole file for signs of a god method (simpler, more robust)
    concerns = []
    if 'System.out' in code or 'System.err' in code: concerns.append("I/O")
    if re.search(r'\bnew\s+File\b|\bScanner\b|\bReader\b|\bWriter\b', code): concerns.append("File I/O")
    if re.search(r'try\s*\{', code): concerns.append("exception handling")
    if re.search(r'for\s*\(|while\s*\(', code): concerns.append("loops")
    if code.count('if (') + code.count('if(') > 3: concerns.append("complex conditionals")
    if re.search(r'\bprepareStatement\b|\bexecute\b', code): concerns.append("database")
    if len(re.findall(r'=\s*new\s+\w+', code)) > 2: concerns.append("object creation")
    if re.search(r'\bconnect\b|\bConnection\b|\bSocket\b', code): concerns.append("networking")
    if re.search(r'continue\b|break\b', code): concerns.append("control flow")
    if len(concerns) >= 4:
        detected.append(("GodMethod", 0.9,
                        f"Method does too many things: {', '.join(concerns)}"))
    
    # LongParameterList
    param_pattern = r'\([^)]*\)'
    for match in re.finditer(r'\w+\s*\(([^)]+)\)', code):
        params = match.group(1).split(',')
        if len(params) >= 6:
            confidence = min(0.6 + (len(params) - 6) * 0.1, 0.95)
            detected.append(("LongParameterList", confidence, 
                           f"Method with {len(params)} parameters"))
            break
    
    # DeepNesting - count max nesting depth
    max_depth = 0
    depth = 0
    for char in code:
        if char == '{': 
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == '}': 
            depth -= 1
    
    if max_depth > 5:
        confidence = min(0.5 + (max_depth - 5) * 0.1, 0.9)
        detected.append(("DeepNesting", confidence, 
                        f"Nesting depth of {max_depth}"))
    
    # MessageChain - a.b().c().d()
    chain_pattern = r'(\w+\.){3,}\w+\('
    chains = re.findall(chain_pattern, code)
    if len(chains) > 3:
        confidence = min(0.5 + len(chains) * 0.05, 0.85)
        detected.append(("MessageChain", confidence,
                        f"Found {len(chains)} method chains"))
    
    # ComplexConditional
    complex_conditions = re.findall(r'\bif\s*\([^)]*(\&\&|\|\|)[^)]*(\&\&|\|\|)[^)]*\)', code)
    if complex_conditions:
        confidence = min(0.5 + len(complex_conditions) * 0.1, 0.85)
        detected.append(("ComplexConditional", confidence,
                        f"Found {len(complex_conditions)} complex conditions"))
    
    # LazyClass - few methods, low LOC
    # IMPORTANT: Do NOT apply LazyClass to enums or interfaces!
    # - Enums are supposed to be small
    # - Interfaces often have few or no methods by design (marker interfaces, etc.)
    if class_type == "class" or class_type == "abstract_class":
        if metrics.get('METHODS', 0) <= 3 and metrics.get('LOC', 0) < 50:
            # But only if it's not a typical small class
            if metrics.get('FIELDS', 0) < 3:
                detected.append(("LazyClass", 0.5, 
                               f"Class with only {metrics.get('METHODS')} methods"))
    
    # MiddleMan - mostly delegation
    delegation_pattern = r'return\s+\w+\.\w+\('
    delegations = len(re.findall(delegation_pattern, code))
    if metrics.get('METHODS', 1) > 0:
        delegation_ratio = delegations / metrics.get('METHODS', 1)
        if delegation_ratio > 0.7 and metrics.get('METHODS', 0) >= 3:
            detected.append(("MiddleMan", min(0.5 + delegation_ratio * 0.3, 0.85),
                           f"High delegation ratio: {delegation_ratio:.0%}"))
    
    # HighCoupling (from metrics)
    if metrics.get('CBO', 0) > 20:
        confidence = min(0.5 + (metrics.get('CBO', 0) - 20) * 0.02, 0.9)
        detected.append(("HighCoupling", confidence,
                        f"CBO = {metrics.get('CBO')}"))
    
    # ══════════════════════════════════════════════════════════════════════════
    # BAD NAMING DETECTION (Uncommunicative Names / Mysterious Names)
    # ══════════════════════════════════════════════════════════════════════════
    bad_names = []
    
    # 1. Single-letter field names (except common loop vars)
    field_pattern = r'(public|private|protected)\s+\w+\s+(\w+)\s*[;=]'
    field_names = re.findall(field_pattern, code)
    single_letter_fields = [name for _, name in field_names 
                           if len(name) == 1 and name not in ('i', 'j', 'k', 'n', 'm')]
    if single_letter_fields:
        bad_names.extend(single_letter_fields)
    
    # 2. Single-letter or two-letter parameter names
    method_params = re.findall(r'\(([^)]+)\)', code)
    for params in method_params:
        if ',' in params or any(c.isupper() for c in params):  # Likely method signature
            param_names = re.findall(r'\b(\w+)\s*[,)]', params)
            for pname in param_names:
                if len(pname) <= 2 and pname.lower() not in ('id', 'io', 'db'):
                    bad_names.append(pname)
    
    # 3. Meaningless names
    meaningless = {'thing', 'stuff', 'data', 'info', 'temp', 'tmp', 'obj', 
                  'val', 'var', 'foo', 'bar', 'baz', 'test', 'xxx', 'zzz',
                  'doit', 'run', 'go', 'process', 'handle', 'execute', 'dowork',
                  'doeverything', 'dostuff', 'helper', 'manager', 'processor',
                  'result', 'res', 'ret', 'value', 'item', 'element', 'x',
                  'cnt', 'num', 'str', 'buf', 'arr', 'ptr', 'idx', 'len',
                  'mgr', 'svc', 'proc', 'impl', 'util', 'utils'}
    
    # 4. Generic "My" prefix pattern (MyClass, MyMethod, myVar)
    my_pattern = r'\b[mM]y[A-Z]\w*'
    my_names = re.findall(my_pattern, code)
    if my_names:
        bad_names.extend(my_names[:3])  # Add first 3 "My*" names
    
    # Check class name
    class_match = re.search(r'class\s+(\w+)', code)
    if class_match:
        class_name = class_match.group(1)
        if class_name.lower() in meaningless or len(class_name) <= 2:
            bad_names.append(f"class:{class_name}")
    
    # Check method names
    method_names = re.findall(r'(public|private|protected)\s+\w+\s+(\w+)\s*\(', code)
    for _, mname in method_names:
        if mname.lower() in meaningless or len(mname) <= 2:
            bad_names.append(f"method:{mname}")
    
    # Check field names against meaningless
    for _, fname in field_names:
        if fname.lower() in meaningless:
            bad_names.append(fname)
    
    # Single letter local variables
    local_vars = re.findall(r'\b(\w+)\s+(\w)\s*=', code)
    for type_name, var_name in local_vars:
        if len(var_name) == 1 and var_name not in ('i', 'j', 'k', 'n', 'm'):
            bad_names.append(var_name)
    
    # Calculate bad naming score
    if bad_names:
        # More bad names = higher confidence
        num_bad = len(bad_names)
        total_identifiers = len(field_names) + len(method_names) + 1  # +1 for class
        bad_ratio = num_bad / max(total_identifiers, 1)
        
        if num_bad >= 2 or bad_ratio > 0.2:
            confidence = min(0.5 + num_bad * 0.08 + bad_ratio * 0.3, 0.95)
            examples = list(set(bad_names))[:5]  # Show first 5 unique
            detected.append(("BadNaming", confidence,
                           f"Poor names: {', '.join(examples)}"))
    
    return detected


# ═══════════════════════════════════════════════════════════════════════════════
# ML Model Loading
# ═══════════════════════════════════════════════════════════════════════════════

def load_models() -> Optional[Dict]:
    """Load trained ML models"""
    if not HAS_JOBLIB:
        return None
    
    model_dir = BASE / "models"
    models = {}
    
    try:
        # Try to load ultimate models
        if (model_dir / "ultimate_rf.joblib").exists():
            models['rf'] = joblib.load(model_dir / "ultimate_rf.joblib")
            models['gb'] = joblib.load(model_dir / "ultimate_gb.joblib")
            models['scaler'] = joblib.load(model_dir / "ultimate_scaler.joblib")
            if (model_dir / "ultimate_xgb.joblib").exists():
                models['xgb'] = joblib.load(model_dir / "ultimate_xgb.joblib")
            print("✓ Loaded trained ML models")
            return models
    except Exception as e:
        print(f"⚠️ Could not load ML models: {e}")
    
    return None


# ═══════════════════════════════════════════════════════════════════════════════
# Main Prediction Function
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class PredictionResult:
    """Complete prediction result"""
    primary_smell: str
    primary_confidence: float
    all_smells: List[Tuple[str, float]]  # (smell, confidence)
    metrics: Dict
    recommendations: List[str]
    details: Dict


def predict_smell(code: str, models: Optional[Dict] = None, 
                  use_extended: bool = True, file_path: str = None) -> PredictionResult:
    """
    Predict code smells for given Java code.
    
    Args:
        code: Java source code
        models: Loaded ML models (optional)
        use_extended: Whether to detect extended smells
        file_path: Path to the Java file (for CK metrics lookup)
        
    Returns:
        PredictionResult with all detected smells
    """
    # Extract metrics (uses real CK data if available)
    metrics = extract_metrics(code, file_path)
    is_approximate = metrics.get('_approximate', False)
    
    # ====================================================================
    # DETECT CLASS TYPE (class, interface, enum, abstract_class)
    # This affects which smells apply (e.g., LazyClass doesn't apply to enums)
    # ====================================================================
    class_type = "class"  # Default
    if re.search(r'\benum\s+\w+', code):
        class_type = "enum"
    elif re.search(r'\binterface\s+\w+', code):
        class_type = "interface"
    elif re.search(r'\babstract\s+class\s+\w+', code):
        class_type = "abstract_class"
    
    # Store class_type in metrics for use by callers (e.g., Unity)
    metrics['class_type'] = class_type
    
    all_smells = []
    details = {'metrics': metrics, 'approximate_metrics': is_approximate, 'class_type': class_type}
    
    # If we have real CK metrics, use ML model
    # If approximate (pasted code), use rule-based detection for better accuracy
    use_ml = models and 'scaler' in models and not is_approximate
    
    if use_ml:
        features = add_derived_features(metrics)
        features = np.nan_to_num(features, nan=0.0, posinf=0.0, neginf=0.0)
        
        X = features.reshape(1, -1)
        X_scaled = models['scaler'].transform(X)
        
        # Get probabilities from ensemble
        rf_proba = models['rf'].predict_proba(X_scaled)[0]
        gb_proba = models['gb'].predict_proba(X_scaled)[0]
        
        if 'xgb' in models:
            xgb_proba = models['xgb'].predict_proba(X_scaled)[0]
            ensemble_proba = (rf_proba + gb_proba + xgb_proba) / 3
        else:
            ensemble_proba = (rf_proba + gb_proba) / 2
        
        # Map to smell names (use MODEL_SMELLS which matches training)
        for i, smell in enumerate(MODEL_SMELLS):
            if ensemble_proba[i] > 0.1:  # Threshold
                all_smells.append((smell, float(ensemble_proba[i])))
        
        details['ml_predictions'] = {
            MODEL_SMELLS[i]: float(ensemble_proba[i]) 
            for i in range(len(MODEL_SMELLS))
        }
    else:
        # Rule-based detection for pasted code (more reliable than ML with bad features)
        details['detection_mode'] = 'rule-based'
        
        # ====================================================================
        # SPECIAL HANDLING FOR ENUMS AND INTERFACES
        # - Enums are supposed to be small and simple
        # - Interfaces define contracts, not implementations
        # - Both should generally be "Clean" unless they have real issues
        # ====================================================================
        if class_type == "enum":
            # Enums are almost always clean - they're meant to be simple
            # Only flag if they have unusual issues like god-enum with too many values
            enum_values = len(re.findall(r'^\s*\w+\s*[,;(]', code, re.MULTILINE))
            if enum_values > 50:
                all_smells.append(("GodClass", 0.6))  # Enum with too many values
            else:
                all_smells.append(("Clean", 0.90))
            # Skip all other smell detection for enums
            return PredictionResult(
                primary_smell=all_smells[0][0] if all_smells else "Clean",
                primary_confidence=all_smells[0][1] if all_smells else 0.90,
                all_smells=all_smells,
                metrics=metrics,
                recommendations=[],
                details=details
            )
        
        if class_type == "interface":
            # Interfaces are almost always clean - they define contracts
            # Only flag if they have too many methods (interface bloat)
            interface_methods = len(re.findall(r'(public\s+)?\w+\s+\w+\s*\([^)]*\)\s*;', code))
            if interface_methods > 15:
                all_smells.append(("GodClass", 0.6))  # Interface with too many methods
            else:
                all_smells.append(("Clean", 0.90))
            # Skip all other smell detection for interfaces
            return PredictionResult(
                primary_smell=all_smells[0][0] if all_smells else "Clean",
                primary_confidence=all_smells[0][1] if all_smells else 0.90,
                all_smells=all_smells,
                metrics=metrics,
                recommendations=[],
                details=details
            )
        
        loc = metrics.get('LOC', 0)
        wmc = metrics.get('WMC', 0)
        methods = metrics.get('METHODS', 1)
        fields = metrics.get('FIELDS', 0)
        max_method_loc = metrics.get('MAX_METHOD_LOC', 0)
        tcc = metrics.get('TCC', 0.5)
        atfd = metrics.get('ATFD', 0)
        lcom = metrics.get('LCOM', 0)
        cbo = metrics.get('CBO', 0)  # Coupling Between Objects
        
        # ====================================================================
        # DETECT DATACLASS FIRST - prevents misclassification as GodClass
        # ====================================================================
        getter_pattern = r'(public|protected)\s+\w+\s+get\w+\s*\([^)]*\)\s*\{'
        setter_pattern = r'(public|protected)\s+void\s+set\w+\s*\([^)]*\)\s*\{'
        getters = len(re.findall(getter_pattern, code))
        setters = len(re.findall(setter_pattern, code))
        accessor_methods = getters + setters
        
        # Count BEHAVIORAL methods: non-getter/setter methods with parameters that DO something
        # These indicate the class has real behavior, not just data storage
        all_method_signatures = re.findall(
            r'(public|private|protected)\s+(?:static\s+)?(?:\w+)\s+(\w+)\s*\(([^)]*)\)', code
        )
        behavioral_methods = 0
        for modifier, method_name, params in all_method_signatures:
            # Skip getters (getXxx with no params or returning field)
            if method_name.startswith('get') and not params.strip():
                continue
            # Skip setters (setXxx with one param, void return)
            if method_name.startswith('set'):
                continue
            # Skip constructors (method name matches class name)
            class_name_match = re.search(r'class\s+(\w+)', code)
            if class_name_match and method_name == class_name_match.group(1):
                continue
            # Skip isXxx/hasXxx boolean getters
            if (method_name.startswith('is') or method_name.startswith('has')) and not params.strip():
                continue
            # Method with parameters that's not a setter = behavioral method
            if params.strip():
                behavioral_methods += 1
        
        is_data_class = False
        data_class_conf = 0
        
        # Only flag as DataClass if there are NO or very few behavioral methods
        if accessor_methods > 0 and fields >= 2 and behavioral_methods <= 1:
            accessor_ratio = accessor_methods / max(methods, 1)
            # Strong DataClass indicators:
            # 1. Most methods are getters/setters (ratio >= 0.6)
            # 2. Has matching getters/setters for fields
            # 3. Few to no behavioral methods
            if accessor_ratio >= 0.6 or (getters >= fields * 0.8 and setters >= fields * 0.5):
                is_data_class = True
                data_class_conf = min(0.6 + accessor_ratio * 0.25, 0.85)
                all_smells.append(("DataClass", data_class_conf))
        
        # Alternative DataClass: field-heavy class with simple methods and no behavior
        if not is_data_class and fields >= 3 and methods > 0 and behavioral_methods <= 1:
            field_to_method = fields / methods
            complexity_per_method = wmc / max(methods, 1)
            if field_to_method >= 0.5 and complexity_per_method < 1.5 and accessor_methods >= 2:
                is_data_class = True
                data_class_conf = min(0.5 + field_to_method * 0.2, 0.75)
                all_smells.append(("DataClass", data_class_conf))
        
        # ====================================================================
        # DETECT CLEAN PATTERNS EARLY - well-designed code patterns
        # This must happen before LongMethod/FeatureEnvy to prevent false positives
        # BUT: If code is very long (high LOC), it's likely LongMethod, not Clean
        # NOTE: Check for method DEFINITIONS, not just calls to avoid false positives
        # ====================================================================
        is_clean_pattern = False
        
        # Get LOC for this check - high LOC suggests LongMethod, not Clean
        code_loc = metrics.get('loc', len(code.split('\n')))
        
        # Builder pattern: has build() method DEFINITION and method chaining returning 'this'
        has_builder = re.search(r'public\s+\w+\s+build\s*\(', code) is not None
        returns_this = len(re.findall(r'return\s+this\s*;', code)) >= 2
        
        # Repository pattern: DEFINES findBy*, save, delete methods (not just calls them)
        has_repo_methods = (re.search(r'public\s+\w+\s+(findBy|findAll|save|delete)\s*\(', code) is not None and
                           methods <= 10)
        
        # Factory pattern: DEFINES create methods returning objects
        has_factory = re.search(r'public\s+(static\s+)?\w+\s+create\w*\s*\(', code) is not None
        
        # Strategy/Observer pattern: implements interface methods
        has_override = len(re.findall(r'@Override', code)) >= 1
        
        # Value object: immutable with equals/hashCode OR private final fields with value methods
        has_value_obj = (re.search(r'private\s+final\s+\w+', code) is not None and
                        (re.search(r'public\s+\w+\s+(equals|hashCode|add|subtract|multiply)\s*\(', code) is not None or
                         methods <= 8))
        
        # Adapter pattern: wraps another object with simple delegation  
        has_delegate = re.search(r'private\s+(final\s+)?\w+\s+(delegate|client|service|adapter|stripeClient)', code, re.IGNORECASE) is not None
        
        # Pre-check for FeatureEnvy: count getters on parameters BEFORE Clean detection
        # This helps avoid marking FeatureEnvy cases as Clean just because they have "validate" in name
        # Include more getter-like patterns: get*, is*, has*, are*, contains*, requires*
        pre_param_getters = re.findall(r'([a-z][a-zA-Z0-9]*)\.(?:get|is|has|are|contains|requires)\w*\s*\(\s*\)', code)
        pre_getter_counts = {}
        pre_common_skip = {'this', 'super', 'System', 'Math', 'String', 'result', 'builder', 'sb', 'logger'}
        for pg in pre_param_getters:
            if pg.lower() not in pre_common_skip and len(pg) > 1:
                pre_getter_counts[pg] = pre_getter_counts.get(pg, 0) + 1
        pre_max_access = max(pre_getter_counts.values()) if pre_getter_counts else 0
        
        # Check if this looks like a Repository pattern (BEFORE likely_feature_envy check)
        # Repositories naturally access entity getters but that's not FeatureEnvy
        is_repo_pattern = (re.search(r'public\s+\w+\s+(findBy|findAll|save|delete)\s*\(', code) is not None and
                         methods <= 10)
        
        # FeatureEnvy is likely ONLY if:
        # - Many getters on one object (>=5)
        # - NOT a repository pattern (repos naturally access entity data)
        likely_feature_envy = pre_max_access >= 5 and not is_repo_pattern
        
        # Validation service: DEFINES validate* methods (method definition, not call)
        # BUT NOT if it looks like FeatureEnvy (accessing one object extensively)
        has_validation = (re.search(r'public\s+\w+\s+validate\w*\s*\(', code) is not None and 
                         re.search(r'ValidationResult|boolean|isValid', code, re.IGNORECASE) is not None and
                         code_loc < 80 and
                         not likely_feature_envy)  # Don't mark as Clean if FeatureEnvy is likely
        
        # Notification/Event service: DEFINES send*, notify*, publish* methods (not calls them)
        has_notification = (re.search(r'public\s+\w+\s+(send|notify|publish)\w*\s*\(', code) is not None and 
                           methods <= 8 and code_loc < 100)
        
        # Caching decorator: Wrap with cache operations
        has_cache = re.search(r'cache\.(get|put)', code, re.IGNORECASE) is not None
        
        # Only mark as Clean if LOC is reasonable and no FeatureEnvy signal
        if code_loc > 120:
            # Too long to be "Clean" - likely LongMethod
            is_clean_pattern = False
        elif likely_feature_envy:
            # Strong FeatureEnvy signal - skip Clean detection
            is_clean_pattern = False
        elif has_builder and returns_this:
            is_clean_pattern = True
        elif has_repo_methods and code_loc < 100:
            is_clean_pattern = True
        elif has_factory and methods <= 8 and code_loc < 80:
            is_clean_pattern = True
        elif has_value_obj and code_loc < 100:
            is_clean_pattern = True
        elif has_delegate and methods <= 10 and code_loc < 100:
            is_clean_pattern = True
        elif has_override and methods <= 8 and not is_data_class and code_loc < 100:
            is_clean_pattern = True
        elif has_validation and methods <= 6:
            is_clean_pattern = True
        elif has_notification:
            is_clean_pattern = True
        elif has_cache and methods <= 5 and code_loc < 80:
            is_clean_pattern = True
        
        # If clean pattern, add Clean smell and skip problematic detections
        if is_clean_pattern:
            all_smells.append(("Clean", 0.92))
        
        # ====================================================================
        # DETECT LONGMETHOD - SKIP if clean pattern
        # LongMethod is a METHOD-level smell - requires evidence of long methods
        # Cannot be inferred from class-level metrics alone without method LOC
        # ====================================================================
        is_long_method = False
        long_method_conf = 0
        
        # Calculate statements per method (needed for is_clearly_long check later)
        semicolons = code.count(';')
        method_count = max(methods, 1)
        statements_per_method = semicolons / method_count
        
        # CRITICAL CHECK: Average method LOC must be reasonable for LongMethod
        # If class has multiple methods and average LOC per method is small, skip LongMethod
        avg_method_loc = code_loc / method_count if method_count > 0 else code_loc
        has_small_avg_methods = (methods >= 3 and avg_method_loc <= 12)
        
        # Classes with behavioral methods (non-getter/setter methods with parameters) should be Clean
        # Example: Owner.adoptPet(pet), Owner.feedPet(pet, food) are behavioral
        behavioral_methods = re.findall(r'public\s+\w+\s+(?!(get|set|is|has)\w*\b)(\w+)\s*\([^)]+\)', code)
        has_behavioral_methods = len(behavioral_methods) >= 2
        
        if not is_clean_pattern and not is_data_class and not has_small_avg_methods:
            # Primary indicator: max method LOC (must be HIGH threshold)
            if max_method_loc > 35:  # Raised from 25 to require strong evidence
                is_long_method = True
                long_method_conf = min(0.55 + (max_method_loc - 35) / 50, 0.95)
                all_smells.append(("LongMethod", long_method_conf))
            
            # Secondary: many statements per method (compressed code)
            if statements_per_method > 15 and not is_long_method:  # Raised from 12
                is_long_method = True
                long_method_conf = min(0.5 + (statements_per_method - 15) * 0.035, 0.95)
                all_smells.append(("LongMethod", long_method_conf))
        
        # ====================================================================
        # DETECT FEATUREENVY - method heavily uses OTHER object's data
        # Key insight: A method that repeatedly calls getters on the SAME parameter
        # This approach counts obj.getX() calls per parameter - 5+ on one = FeatureEnvy
        # BUT: Long processing methods legitimately access data - that's NOT FeatureEnvy
        # FeatureEnvy = method should belong to ANOTHER class
        # LongMethod = method does too much work (but belongs here)
        # ====================================================================
        # Find all param.getX() calls and count per-parameter
        # Include more getter-like patterns: get*, is*, has*, are*, contains*, requires*
        param_getter_matches = re.findall(r'([a-z][a-zA-Z0-9]*)\.(?:get|is|has|are|contains|requires)\w*\s*\(\s*\)', code)
        
        # Count getters per parameter
        param_getter_counts = {}
        common_non_params = {'this', 'super', 'System', 'Math', 'String', 'Integer', 'Double', 
                            'result', 'builder', 'sb', 'out', 'logger', 'log', 'props', 'config',
                            'report', 'email', 'query', 'queryBuilder', 'parameters', 'items', 'item'}
        for param in param_getter_matches:
            if param.lower() not in common_non_params and len(param) > 1:
                param_getter_counts[param] = param_getter_counts.get(param, 0) + 1
        
        # Find the most-accessed parameter
        max_param_access = max(param_getter_counts.values()) if param_getter_counts else 0
        total_param_getters = sum(param_getter_counts.values())
        num_params_accessed = len(param_getter_counts)
        
        # Deep getter chains like a.getB().getC() - also strong indicator
        deep_chain_pattern = r'\w+\.get\w+\(\)\.get\w+\(\)'
        deep_chains = len(re.findall(deep_chain_pattern, code))
        
        is_feature_envy = False
        feature_envy_conf = 0
        
        # ====================================================================
        # DETECT FEATUREENVY - Always detect, but priority logic decides winner
        # FeatureEnvy: Method heavily uses ANOTHER object's data
        # LongMethod: Method does too much work (but may also access data)
        # Key distinction:
        # - SHORT code with many getters on external object = FeatureEnvy
        # - LONG code with many getters = LongMethod (data access is incidental)
        # ====================================================================
        
        # Determine if code is "genuinely long" (not just slightly over threshold)
        # Use higher thresholds to avoid suppressing FeatureEnvy in moderate-length code
        genuinely_long = (
            max_method_loc > 50 or  # Very long method
            statements_per_method > 25 or  # Many statements
            (code_loc > 120 and methods <= 2)  # Long code in few methods
        )
        
        # For genuinely long methods, require much stronger FeatureEnvy signal
        # For moderate-length methods, use normal thresholds
        feature_envy_threshold = 5 if not genuinely_long else 8
        concentration_threshold = 8 if not genuinely_long else 12
        
        # Check for "processing" indicators that suggest LongMethod over FeatureEnvy
        # These are signs that the method is doing significant work, not just accessing data
        setter_calls = len(re.findall(r'\w+\.set\w+\s*\(', code))
        service_calls = len(re.findall(r'\w+\.(save|send|delete|update|notify|publish|create|remove|add|insert|block|confirm)\s*\(', code))
        new_object_creations = len(re.findall(r'new\s+\w+\s*\(', code))
        has_heavy_processing = (setter_calls >= 3 or service_calls >= 2 or (setter_calls >= 2 and service_calls >= 1))
        has_very_heavy_processing = (setter_calls >= 5 or service_calls >= 3 or (setter_calls >= 3 and service_calls >= 2) or new_object_creations >= 3)
        
        # If code has heavy processing indicators, raise the FeatureEnvy thresholds
        # This prevents classifying complex processing code as FeatureEnvy just because it uses getters
        if has_very_heavy_processing:
            # Very heavy processing - this is almost certainly LongMethod
            feature_envy_threshold = max(feature_envy_threshold, 15)
            concentration_threshold = max(concentration_threshold, 20)
        elif has_heavy_processing:
            # Regular heavy processing - raise thresholds moderately
            feature_envy_threshold = max(feature_envy_threshold, 10)
            concentration_threshold = max(concentration_threshold, 15)
        
        if not is_clean_pattern:
            # FeatureEnvy: accessing single external object's data extensively
            # Key: many getters on the SAME parameter (>=5 on one object for SHORT methods)
            
            if max_param_access >= feature_envy_threshold:
                # Strong indicator: many getters on a single parameter
                feature_envy_conf = min(0.6 + max_param_access * 0.04, 0.85)
                is_feature_envy = True
                all_smells.append(("FeatureEnvy", feature_envy_conf))
            elif deep_chains >= 2:
                # Deep method chaining indicates FeatureEnvy
                feature_envy_conf = min(0.55 + deep_chains * 0.1, 0.80)
                is_feature_envy = True
                all_smells.append(("FeatureEnvy", feature_envy_conf))
            elif total_param_getters >= concentration_threshold and num_params_accessed <= 2:
                # Many getters concentrated on few objects
                concentration = total_param_getters / max(num_params_accessed, 1)
                feature_envy_conf = min(0.5 + concentration * 0.03, 0.80)
                is_feature_envy = True
                all_smells.append(("FeatureEnvy", feature_envy_conf))
        
        # ====================================================================
        # GodClass detection - SKIP if DataClass or Clean pattern
        # ====================================================================
        god_class_score = 0
        god_class_reasons = []
        
        # SKIP GodClass detection if it's a DataClass or Clean pattern
        if not is_data_class and not is_clean_pattern:
            # Too many methods is a strong indicator (but not for DataClass)
            if methods > 12:
                god_class_score += 0.4
                god_class_reasons.append(f"Too many methods ({methods})")
            elif methods > 9:
                god_class_score += 0.25
                god_class_reasons.append(f"Many methods ({methods})")
            
            # Many fields combined with methods (but need MANY methods, not just getters/setters)
            if fields >= 4 and methods > 8:
                god_class_score += 0.25
                god_class_reasons.append(f"Multiple fields ({fields}) with many methods")
            elif fields >= 6:
                god_class_score += 0.2
                god_class_reasons.append(f"Many fields ({fields})")
            
            # LOC based (for multi-line code) - higher threshold
            if loc > 150: 
                god_class_score += 0.15
                if loc > 250: god_class_score += 0.15
                
            if wmc > 20: 
                god_class_score += 0.15
                god_class_reasons.append(f"High complexity (WMC={wmc})")
                
            if tcc < 0.3 and methods > 4:
                god_class_score += 0.1
                god_class_reasons.append("Low cohesion")
            
            if god_class_score >= 0.5:
                all_smells.append(("GodClass", min(god_class_score, 0.95)))
        
        # Additional ATFD check for FeatureEnvy (if not already detected)
        if atfd > 5 and tcc < 0.3 and not is_feature_envy:
            conf = min(0.5 + atfd / 15, 0.80)
            all_smells.append(("FeatureEnvy", conf))
            is_feature_envy = True
        
        # Clean smell is already added earlier when is_clean_pattern is set
    
    # Extended smell detection
    if use_extended:
        extended = detect_extended_smells(code, metrics, class_type)
        # Convert 3-tuples to 2-tuples (drop description)
        for smell, conf, desc in extended:
            all_smells.append((smell, conf))
        details['extended_smells'] = [(s, c, d) for s, c, d in extended]
    
    # Sort by confidence
    all_smells.sort(key=lambda x: x[1], reverse=True)
    
    # Remove duplicates, keep highest confidence
    seen = set()
    unique_smells = []
    for smell, conf in all_smells:
        if smell not in seen:
            seen.add(smell)
            unique_smells.append((smell, conf))
    
    # Determine primary smell
    # PRIMARY PREDICTION can be ML model smells OR high-confidence static detections (DeadCode)
    # DeadCode is now detected purely statically (not from ML model)
    PRIMARY_SMELLS = {"GodClass", "DataClass", "LongMethod", "FeatureEnvy", "DeadCode", "Clean"}
    
    # Separate core smells from extended smells
    # DeadCode is treated as a core smell when detected with high confidence
    core_smells = [(s, c) for s, c in unique_smells if s in PRIMARY_SMELLS]
    extended_only = [(s, c) for s, c in unique_smells if s not in PRIMARY_SMELLS]
    
    # ========================================================================
    # BEHAVIORAL METHODS CHECK - Classes with real behavior should be Clean
    # This catches classes like Owner that have adoptPet(pet), feedPet(pet, food)
    # These are NOT DataClass, NOT LongMethod - they are well-designed classes
    # ========================================================================
    # Check if class has behavioral methods (non-getter/setter methods with parameters)
    behavioral_methods = re.findall(r'public\s+\w+\s+(?!(get|set|is|has)\w*\b)(\w+)\s*\([^)]+\)', code)
    has_behavioral_methods = len(behavioral_methods) >= 2
    
    # Check average method LOC - if small avg, LongMethod is unlikely
    method_count = max(metrics.get('METHODS', 1), 1)
    avg_method_loc = code_loc / method_count
    has_small_methods = (method_count >= 3 and avg_method_loc <= 12)
    
    # If class has behavioral methods AND small average method LOC, it should be Clean
    # Remove any LongMethod that was incorrectly detected
    if has_behavioral_methods and has_small_methods:
        # Remove LongMethod from core_smells if present
        core_smells = [(s, c) for s, c in core_smells if s != "LongMethod"]
        # Add Clean if not already present
        if not any(s == "Clean" for s, c in core_smells):
            core_smells.append(("Clean", 0.90))
    
    primary = None
    
    # Check for Clean confidence
    clean_conf = 0
    for smell, conf in core_smells:
        if smell == "Clean":
            clean_conf = conf
            break
    
    # Priority for core smells (what the test expects)
    if core_smells:
        # Smart priority: Consider the NATURE of the smell, not just order
        # FeatureEnvy with high confidence should beat LongMethod
        # DataClass should always win (structural smell)
        
        # Build a lookup of detected smells and their confidence
        smell_lookup = {s: c for s, c in core_smells if s != "Clean"}
        
        # Check if this is GENUINELY a LongMethod situation
        # Key distinction:
        # - Genuinely long code (50+ LOC or 25+ statements) = LongMethod
        # - Moderate code (30-50 LOC) with many getters = FeatureEnvy
        # - Short code with many getters = FeatureEnvy
        is_very_long = (
            (max_method_loc > 50) or  # Very long method
            (statements_per_method > 25) or  # Many statements per method
            (code_loc > 120 and methods <= 2) or  # Long code in few methods
            (wmc > 25 and methods <= 3)  # High complexity in few methods
        )
        
        # Moderate length that could be either
        is_moderate = (
            (max_method_loc > 30 and max_method_loc <= 50) or
            (statements_per_method > 15 and statements_per_method <= 25)
        )
        
        best_smell = None
        
        # 1. DataClass always takes priority (structural classification)
        if "DataClass" in smell_lookup and smell_lookup["DataClass"] >= 0.6:
            best_smell = ("DataClass", smell_lookup["DataClass"])
        
        # 2. GodClass with high confidence
        elif "GodClass" in smell_lookup and smell_lookup["GodClass"] >= 0.5:
            best_smell = ("GodClass", smell_lookup["GodClass"])
        
        # 3. DeadCode detected statically with high confidence
        elif "DeadCode" in smell_lookup and smell_lookup["DeadCode"] >= 0.85:
            best_smell = ("DeadCode", smell_lookup["DeadCode"])
        
        # 4. Very long code = LongMethod (even if FeatureEnvy detected)
        elif is_very_long and "LongMethod" in smell_lookup and smell_lookup["LongMethod"] >= 0.7:
            best_smell = ("LongMethod", smell_lookup["LongMethod"])
        
        # 4. FeatureEnvy with strong signal wins over moderate LongMethod
        elif "FeatureEnvy" in smell_lookup and smell_lookup["FeatureEnvy"] >= 0.6:
            if is_very_long and "LongMethod" in smell_lookup and smell_lookup["LongMethod"] >= 0.9:
                # Only defer to LongMethod if VERY long with high confidence
                best_smell = ("LongMethod", smell_lookup["LongMethod"])
            else:
                best_smell = ("FeatureEnvy", smell_lookup["FeatureEnvy"])
        
        # 5. LongMethod for moderate-length code when no FeatureEnvy
        elif "LongMethod" in smell_lookup and smell_lookup["LongMethod"] >= 0.5:
            best_smell = ("LongMethod", smell_lookup["LongMethod"])
        
        # 6. Lower confidence FeatureEnvy 
        elif "FeatureEnvy" in smell_lookup and smell_lookup["FeatureEnvy"] >= 0.5:
            best_smell = ("FeatureEnvy", smell_lookup["FeatureEnvy"])
        
        # 8. Fallback to any detected smell
        elif smell_lookup:
            for smell in ["LongMethod", "FeatureEnvy", "GodClass", "DataClass", "DeadCode"]:
                if smell in smell_lookup and smell_lookup[smell] >= 0.4:
                    best_smell = (smell, smell_lookup[smell])
                    break
        
        if best_smell:
            primary = best_smell
        elif clean_conf > 0.5:
            primary = ("Clean", clean_conf)
        else:
            # Fallback: just pick highest confidence
            for smell, conf in core_smells:
                if smell != "Clean" and conf > 0.3:
                    primary = (smell, conf)
                    break
    
    # If no core smell detected with confidence, default to Clean
    if not primary:
        primary = ("Clean", 0.9)
    
    # Get recommendations
    recommendations = []
    for smell, conf in unique_smells[:3]:  # Top 3 smells
        if smell in SMELL_INFO and conf > 0.3:
            recommendations.append(f"[{smell}] {SMELL_INFO[smell]['recommendation']}")
    
    if not recommendations:
        recommendations = ["No major issues. Keep following good coding practices!"]
    
    return PredictionResult(
        primary_smell=primary[0],
        primary_confidence=primary[1],
        all_smells=unique_smells,
        metrics=metrics,
        recommendations=recommendations,
        details=details
    )


# ═══════════════════════════════════════════════════════════════════════════════
# Backwards Compatible Wrapper (for test scripts)
# ═══════════════════════════════════════════════════════════════════════════════

def predict_smell_compat(code: str, models: Optional[Dict] = None) -> Dict:
    """
    Backwards compatible wrapper for test scripts.
    Returns dict with 'prediction' and 'confidence' keys.
    """
    result = predict_smell(code, models, use_extended=True, file_path=None)
    return {
        'prediction': result.primary_smell,
        'confidence': result.primary_confidence * 100,  # Convert to percentage
        'all_smells': result.all_smells,
        'metrics': result.metrics,
        'recommendations': result.recommendations
    }


# ═══════════════════════════════════════════════════════════════════════════════
# Display Functions
# ═══════════════════════════════════════════════════════════════════════════════

def display_result(result: PredictionResult, class_name: str = ""):
    """Display prediction result with nice formatting"""
    info = SMELL_INFO.get(result.primary_smell, SMELL_INFO["Clean"])
    
    print()
    print("=" * 70)
    if class_name:
        print(f"📄 Analysis for: {color(class_name, Colors.CYAN, Colors.BOLD)}")
    
    # Show detection mode
    if result.details.get('approximate_metrics'):
        print(f"   {color('(Using rule-based detection for pasted code)', Colors.DIM)}")
    print("=" * 70)
    
    # Primary smell - but show "Low Maintainability" if Clean has multiple issues
    extended = result.details.get('extended_smells', [])
    significant_issues = [s for s, c, _ in extended if c >= 0.7]  # High confidence issues
    
    display_smell = result.primary_smell
    display_conf = result.primary_confidence
    display_info = info
    
    # If "Clean" but has 3+ significant issues, show as "Low Maintainability" instead
    if result.primary_smell == "Clean" and len(significant_issues) >= 3:
        display_smell = "Low Maintainability"
        display_conf = 1.0 - (0.1 * len(significant_issues))  # Lower confidence with more issues
        display_conf = max(0.5, display_conf)
        display_info = SMELL_INFO.get("LowMaintainability", info)
    
    print(f"\n{display_info['icon']} Primary Smell: {color(display_smell, display_info['color'], Colors.BOLD)}")
    print(f"   Confidence: {display_conf:.0%}")
    print(f"   {display_info['description']}")
    
    # Extended smells with descriptions (show ALL issues found)
    # Note: extended was already computed above for primary smell logic
    if extended:
        print(f"\n🚨 {color('Issues Found:', Colors.RED, Colors.BOLD)}")
        for smell, conf, desc in extended:
            icon = SMELL_INFO.get(smell, {}).get('icon', '⚠️')
            smell_color = SMELL_INFO.get(smell, {}).get('color', Colors.YELLOW)
            print(f"   {icon} {color(smell, smell_color)} ({conf:.0%})")
            print(f"      └─ {desc}")
    
    # All detected smells (without duplicating extended)
    non_extended = [s for s in result.all_smells if s[0] not in [e[0] for e in extended] and s[1] > 0.3]
    if non_extended:
        print(f"\n🔍 Other Detected Smells:")
        for smell, conf in non_extended:
            if conf > 0.3:
                s_info = SMELL_INFO.get(smell, SMELL_INFO["Clean"])
                bar = "█" * int(conf * 10) + "░" * (10 - int(conf * 10))
                print(f"   {s_info['icon']} {smell:20s} [{bar}] {conf:.0%}")
    
    # Metrics
    print(f"\n📊 Key Metrics:")
    print(f"   LOC: {result.metrics.get('LOC', 0):>5}  |  Methods: {result.metrics.get('METHODS', 0):>3}  |  Fields: {result.metrics.get('FIELDS', 0):>3}")
    print(f"   WMC: {result.metrics.get('WMC', 0):>5}  |  CBO: {result.metrics.get('CBO', 0):>7}  |  ATFD: {result.metrics.get('ATFD', 0):>5}")
    print(f"   Max Method LOC: {result.metrics.get('MAX_METHOD_LOC', 0):>4}  |  TCC: {result.metrics.get('TCC', 0):.2f}")
    
    # Recommendations
    print(f"\n💡 Recommendations:")
    for rec in result.recommendations:
        print(f"   → {rec}")
    
    # Additional recommendations for extended smells
    extended_recs = {
        'MagicNumbers': 'Replace magic numbers with named constants',
        'GlobalMutableState': 'Avoid public static mutable fields - use encapsulation',
        'RawCollections': 'Add generic type parameters to collections (e.g., List<String>)',
        'SwallowedException': 'Log or handle exceptions properly - never ignore them',
        'DeadCode': 'Remove unreachable code to improve maintainability',
        'DuplicateCode': 'Extract duplicate logic into reusable methods',
        'PointlessLoop': 'Remove or fix loops with no net effect',
        'UnnecessaryBoxing': 'Use primitive types or .valueOf() instead of new wrapper',
        'StringConcatInLoop': 'Use StringBuilder for string concatenation in loops',
        'GodMethod': 'Split method into smaller, focused methods (Single Responsibility)',
        'DeepNesting': 'Reduce nesting with early returns or extract methods',
    }
    for smell, _, _ in extended:
        if smell in extended_recs:
            print(f"   → [{smell}] {extended_recs[smell]}")
    
    print()


def read_file(path: str) -> Optional[str]:
    """Read Java file"""
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


def interactive_mode(models: Optional[Dict]):
    """Interactive analysis mode"""
    print()
    print("=" * 70)
    print(color("🔍 EXTENDED CODE SMELL DETECTOR - Interactive Mode", Colors.CYAN, Colors.BOLD))
    print("=" * 70)
    print()
    print("Enter Java code to analyze. Options:")
    print("  - Paste code directly (end with a line containing only 'END')")
    print("  - Enter a file path")
    print("  - Type 'quit' to exit")
    print()
    
    while True:
        print("-" * 40)
        user_input = input(color("Enter code or file path: ", Colors.YELLOW)).strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! 👋")
            break
        
        code = None
        class_name = "UserCode"
        
        if os.path.isfile(user_input):
            code = read_file(user_input)
            class_name = Path(user_input).stem
        elif user_input:
            # Multi-line input
            print("(Paste code, then type 'END' on a new line)")
            lines = [user_input]
            while True:
                line = input()
                if line.strip() == 'END':
                    break
                lines.append(line)
            code = '\n'.join(lines)
        
        if code:
            result = predict_smell(code, models, use_extended=True, 
                                   file_path=user_input if os.path.isfile(user_input) else None)
            display_result(result, class_name)


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Main entry point"""
    print(color("\n🔍 EXTENDED CODE SMELL PREDICTOR", Colors.CYAN, Colors.BOLD))
    print(color("   Detects 14 types of code smells using ML + Static Analysis\n", Colors.DIM))
    
    # Load models
    models = load_models()
    
    # Parse args
    use_pmd = "--use-pmd" in sys.argv
    use_checkstyle = "--use-checkstyle" in sys.argv
    
    # Filter out flags
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    
    if not args:
        # Interactive mode
        interactive_mode(models)
    elif os.path.isfile(args[0]):
        # Single file
        code = read_file(args[0])
        if code:
            result = predict_smell(code, models, use_extended=True, file_path=args[0])
            display_result(result, Path(args[0]).stem)
    elif os.path.isdir(args[0]):
        # Directory
        java_files = list(Path(args[0]).rglob("*.java"))
        print(f"📂 Found {len(java_files)} Java files\n")
        
        results = []
        for java_file in java_files[:20]:  # Limit to 20 for display
            code = read_file(str(java_file))
            if code:
                result = predict_smell(code, models, use_extended=True, file_path=str(java_file))
                results.append((java_file.stem, result))
        
        # Summary
        print("\n" + "=" * 70)
        print(color("📊 SUMMARY", Colors.CYAN, Colors.BOLD))
        print("=" * 70)
        
        smell_counts = {}
        for name, result in results:
            smell = result.primary_smell
            smell_counts[smell] = smell_counts.get(smell, 0) + 1
        
        for smell, count in sorted(smell_counts.items(), key=lambda x: -x[1]):
            info = SMELL_INFO.get(smell, SMELL_INFO["Clean"])
            print(f"  {info['icon']} {smell:20s}: {count} files")
        
        # Show top problematic files
        print(f"\n🔥 Most Problematic Files:")
        problem_files = [(n, r) for n, r in results if r.primary_smell != "Clean"]
        problem_files.sort(key=lambda x: x[1].primary_confidence, reverse=True)
        
        for name, result in problem_files[:5]:
            info = SMELL_INFO.get(result.primary_smell, {})
            print(f"  {info.get('icon', '❓')} {name}: {result.primary_smell} ({result.primary_confidence:.0%})")
    else:
        print(f"❌ Path not found: {args[0]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
