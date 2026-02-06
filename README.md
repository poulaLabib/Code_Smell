# 🔍 Extended Code Smell Detection System

This project now supports **16 types of code smells** through multiple detection methods!

## ✅ Supported Code Smells

| # | Smell | Description | Detection Method |
|---|-------|-------------|------------------|
| 1 | **GodClass** | Class doing too much (violates SRP) | ML Model + CK + PMD + Checkstyle |
| 2 | **DataClass** | Mostly data, little behavior | ML Model + CK + PMD |
| 3 | **LongMethod** | Method too long or complex | ML Model + CK + PMD + Checkstyle |
| 4 | **FeatureEnvy** | Uses other class's data too much | ML Model + CK + PMD |
| 5 | **Clean** | No smell detected | ML Model |
| 6 | **LongParameterList** | Too many parameters (>5-7) | PMD + Checkstyle + Pattern |
| 7 | **DeepNesting** | Too many nested control structures | Checkstyle + Pattern |
| 8 | **HighCoupling** | Too many class dependencies | CK + PMD + Checkstyle |
| 9 | **ComplexConditional** | Boolean expressions too complex | PMD + Pattern |
| 10 | **MessageChain** | Train wreck code (a.b().c().d()) | PMD + Pattern |
| 11 | **DuplicatedCode** | Copy-paste code | PMD |
| 12 | **LazyClass** | Class doesn't do enough | Pattern Analysis |
| 13 | **RefusedBequest** | Subclass ignores parent methods | Pattern Analysis |
| 14 | **MiddleMan** | Just delegates to another class | Pattern Analysis |
| 15 | **DeadCode** | Unused code | PMD |
| 16 | **ShotgunSurgery** | Changes require many small edits | Pattern Analysis |

---

## 🚀 Quick Start

### Basic Usage (ML + Pattern Detection)
```bash
# Interactive mode
python predict_smell_extended.py

# Analyze a single file
python predict_smell_extended.py path/to/MyClass.java

# Analyze a directory
python predict_smell_extended.py path/to/project/src
```

### Full Analysis (with PMD + Checkstyle)
```bash
# Requires Java 11+
python tools/unified_detector.py path/to/project

# With specific tools
python predict_smell_extended.py --use-pmd --use-checkstyle path/to/file.java
```

---

## 📁 File Structure

```
code_smell_project/
├── predict_smell_extended.py  # 🆕 Extended predictor (14 smells)
├── predict_smell.py           # Original predictor (5 smells)
├── tools/
│   ├── pmd_analyzer.py        # 🆕 PMD integration
│   ├── checkstyle_analyzer.py # 🆕 Checkstyle integration
│   └── unified_detector.py    # 🆕 Master detector combining all tools
├── models/
│   ├── ultimate_rf.joblib     # Random Forest model
│   ├── ultimate_gb.joblib     # Gradient Boosting model
│   ├── ultimate_xgb.joblib    # XGBoost model
│   └── ultimate_scaler.joblib # Feature scaler
└── ck_metrics/                # CK metrics data
```

---

## 🛠️ Detection Methods

### 1. ML Models (Primary)
- **Models**: Random Forest + Gradient Boosting + XGBoost ensemble
- **Features**: 39 features derived from CK metrics
- **Detects**: GodClass, DataClass, LongMethod, FeatureEnvy, Clean
- **Accuracy**: ~85%

### 2. PMD Static Analysis
- **Version**: PMD 7.0.0 (auto-downloaded)
- **Requires**: Java 11+
- **Detects**: GodClass, DataClass, LongMethod, DeadCode, DuplicatedCode, LongParameterList, ComplexConditional

### 3. Checkstyle Analysis
- **Version**: Checkstyle 10.12.5 (auto-downloaded)
- **Requires**: Java 11+
- **Detects**: LongMethod, DeepNesting, HighCoupling, LongParameterList

### 4. Pattern-Based Detection
- **Requires**: Just Python
- **Detects**: MessageChain, ComplexConditional, DeepNesting, LazyClass, MiddleMan

---

## ⚙️ Requirements

### Minimum (Basic Detection)
```
Python 3.8+
numpy
scikit-learn
joblib
```

### Full Detection (with PMD/Checkstyle)
```
Java 11+ (for PMD and Checkstyle)
Internet connection (first run to download tools)
```

### Install Python Dependencies
```bash
pip install numpy scikit-learn joblib
# Optional for XGBoost
pip install xgboost
```

---

## 📊 Detection Thresholds

| Metric | Low | Medium | High |
|--------|-----|--------|------|
| LOC (Lines of Code) | <100 | 100-300 | >300 |
| WMC (Weighted Method Count) | <20 | 20-50 | >50 |
| CBO (Coupling) | <10 | 10-20 | >20 |
| Methods per Class | <10 | 10-20 | >20 |
| Max Method LOC | <30 | 30-50 | >50 |
| Parameters per Method | <5 | 5-7 | >7 |
| Nesting Depth | <3 | 3-5 | >5 |

---

## 🎯 Usage Examples

### Example 1: Analyze a Class
```python
from predict_smell_extended import predict_smell, load_models

code = """
public class UserService {
    private UserRepository repo;
    private EmailService email;
    
    public void createUser(String name, String email, String phone, 
                          String address, String city, String country,
                          String postalCode, int age) {
        // Long parameter list smell!
        User user = new User();
        user.setName(name);
        // ... 100 more lines
    }
}
"""

models = load_models()
result = predict_smell(code, models, use_extended=True)

print(f"Primary Smell: {result.primary_smell}")
print(f"Confidence: {result.primary_confidence:.0%}")
print(f"All Smells: {result.all_smells}")
```

### Example 2: Use Unified Detector
```python
from tools.unified_detector import UnifiedSmellDetector

detector = UnifiedSmellDetector(
    project_path="path/to/java/project",
    use_pmd=True,
    use_checkstyle=True
)

# Analyze project
results = detector.analyze_project()

# Get summary
summary = detector.get_summary()
print(f"Total files: {summary['total_files']}")
print(f"Smelly files: {summary['smelly_files']}")
```

### Example 3: Batch Analysis
```bash
# Analyze multiple projects
for project in projects/*/; do
    echo "Analyzing $project"
    python tools/unified_detector.py "$project" --output results/
done
```

---

## 📈 Output Format

### JSON Output
```json
{
  "file": "MyClass.java",
  "smells": [
    {
      "type": "GodClass",
      "confidence": 0.85,
      "sources": ["ML", "PMD", "CK"],
      "metrics": {
        "LOC": 450,
        "WMC": 65,
        "METHODS": 25
      }
    },
    {
      "type": "LongMethod",
      "confidence": 0.72,
      "sources": ["PMD", "Checkstyle"]
    }
  ],
  "recommendations": [
    "Split into smaller, focused classes",
    "Break down long methods into smaller units"
  ]
}
```

---

## 🔧 Customization

### Adjust Thresholds
Edit `tools/unified_detector.py`:
```python
THRESHOLDS = {
    'god_class_loc': 300,      # Reduce for stricter detection
    'god_class_methods': 20,
    'long_method_loc': 50,
    'high_coupling_cbo': 20,
    'long_param_count': 5,
}
```

### Add Custom Rules
For PMD: Edit `tools/pmd_analyzer.py` → `create_custom_ruleset()`
For Checkstyle: Edit `tools/checkstyle_analyzer.py` → `create_checkstyle_config()`

---

## 🚨 Troubleshooting

### "Java not found" Error
```bash
# Check Java version
java -version

# Should be Java 11 or higher
# Download from: https://adoptium.net/
```

### PMD/Checkstyle Download Failed
```bash
# Manual download
cd tools/cache
# Download PMD from: https://github.com/pmd/pmd/releases
# Download Checkstyle from: https://github.com/checkstyle/checkstyle/releases
```

### Model Loading Error
```bash
# Retrain models
python ultimate_model.py
```

---

## 📚 References

- **CK Metrics**: Chidamber & Kemerer (1994) - A Metrics Suite for Object-Oriented Design
- **PMD**: https://pmd.github.io/
- **Checkstyle**: https://checkstyle.org/
- **Code Smell Catalog**: https://refactoring.guru/refactoring/smells

---

## 🎉 What's New

### Version 2.0 (Extended Detection)
- ✅ Added PMD integration for static analysis
- ✅ Added Checkstyle integration for complexity metrics
- ✅ Unified detector combining all tools
- ✅ Extended from 5 to 16 detectable code smells
- ✅ Confidence boosting when multiple tools agree
- ✅ Interactive analysis mode
- ✅ Batch processing support
- ✅ JSON output format

### Original Version
- ML-based detection (5 smells)
- CK metrics analysis
- SonarQube integration

---

## 🤝 Contributing

To add more smells or improve detection:
1. Update `SMELL_DEFINITIONS` in `unified_detector.py`
2. Add detection rules in appropriate analyzer
3. Update thresholds in configuration
4. Test on known smelly code samples

---

**Happy Smell Hunting! 🔍**
