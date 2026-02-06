# analyze.py - Enhanced Code Smell Detection Analysis
import numpy as np
import json
import os
from datetime import datetime
from sklearn.metrics import classification_report, confusion_matrix, f1_score, precision_recall_fscore_support
from collections import Counter

# ═══════════════════════════════════════════════════════════════════════════════
# ANSI Color Codes for Terminal Output
# ═══════════════════════════════════════════════════════════════════════════════
class Colors:
    # Enable colors on Windows
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
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    # Background colors
    BG_GREEN = '\033[42m'
    BG_RED = '\033[41m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'

def color(text, *styles):
    """Apply multiple color/style codes to text."""
    return ''.join(styles) + str(text) + Colors.END

def progress_bar(value, max_val=1.0, width=20, fill_char='█', empty_char='░'):
    """Create a visual progress bar."""
    filled = int(width * value / max_val)
    bar = fill_char * filled + empty_char * (width - filled)
    return bar

def get_grade(f1_score):
    """Get letter grade and color for F1 score."""
    if f1_score >= 0.80:
        return 'A', Colors.GREEN
    elif f1_score >= 0.70:
        return 'B', Colors.GREEN
    elif f1_score >= 0.55:
        return 'C', Colors.YELLOW
    elif f1_score >= 0.40:
        return 'D', Colors.YELLOW
    else:
        return 'F', Colors.RED

def print_header(title, width=90):
    """Print a fancy header box."""
    print()
    print(color('╔' + '═' * (width-2) + '╗', Colors.CYAN, Colors.BOLD))
    print(color('║', Colors.CYAN, Colors.BOLD) + color(f' {title}'.center(width-2), Colors.WHITE, Colors.BOLD) + color('║', Colors.CYAN, Colors.BOLD))
    print(color('╚' + '═' * (width-2) + '╝', Colors.CYAN, Colors.BOLD))
    print()

def print_section(title, width=90):
    """Print a section divider."""
    print()
    print(color('┌─', Colors.BLUE) + color(f' {title} ', Colors.WHITE, Colors.BOLD) + color('─' * (width - len(title) - 5) + '┐', Colors.BLUE))

def print_metric_row(label, value, bar_color=Colors.CYAN, show_bar=True, width=20):
    """Print a metric with optional visual bar."""
    bar = progress_bar(value, 1.0, width) if show_bar else ''
    pct = f'{value*100:5.1f}%'
    return f"  {label:15s} {color(bar, bar_color)} {color(pct, Colors.WHITE, Colors.BOLD)}"

# ═══════════════════════════════════════════════════════════════════════════════
# Load Data
# ═══════════════════════════════════════════════════════════════════════════════
# Try ensemble predictions first, fall back to original
import os
if os.path.exists("predictions_ensemble.npy"):
    predictions = np.load("predictions_ensemble.npy")
    MODEL_NAME = "ENSEMBLE (CodeBERT + CK Metrics)"
elif os.path.exists("predictions_enhanced.npy"):
    predictions = np.load("predictions_enhanced.npy")
    MODEL_NAME = "CODEBERT (ENHANCED)"
else:
    predictions = np.load("predictions.npy")
    MODEL_NAME = "CODEBERT (ORIGINAL)"

with open("dataset/dataset.json") as f:
    dataset = json.load(f)
with open("dataset/split_info.json") as f:
    splits = json.load(f)
test_data = [d for d in dataset if d["project"] in splits["test"]]

SMELLS_ALPHA = ["Clean", "DataClass", "DeadCode", "FeatureEnvy", "GodClass", "LongMethod"]
smell_to_idx = {s: i for i, s in enumerate(SMELLS_ALPHA)}

y_true_names = [d["true_smell"] for d in test_data]
y_true = np.array([smell_to_idx[s] for s in y_true_names])

y_pred_logits = predictions
y_pred = np.argmax(y_pred_logits, axis=1)

# Calculate metrics
p, r, f1, support = precision_recall_fscore_support(y_true, y_pred, labels=range(6), zero_division=0)
macro_f1 = f1_score(y_true, y_pred, average="macro")
micro_f1 = f1_score(y_true, y_pred, average="micro")
acc = (y_pred == y_true).mean()
cm = confusion_matrix(y_true, y_pred, labels=range(6))

# ═══════════════════════════════════════════════════════════════════════════════
# Display Results
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" * 2)
print_header(f"🔬 {MODEL_NAME} - CODE SMELL DETECTION ANALYSIS")

# Quick summary box
overall_grade, grade_color = get_grade(macro_f1)
print(color('  ╭─────────────────────────────────────────────────────────────────────────────────╮', Colors.DIM))
print(color('  │', Colors.DIM) + f"  📊 {color('Quick Summary', Colors.WHITE, Colors.BOLD)}                                                              " + color('│', Colors.DIM))
print(color('  │', Colors.DIM) + f"     Test Samples: {color(f'{len(test_data):,}', Colors.CYAN, Colors.BOLD):>38s}    Grade: {color(overall_grade, grade_color, Colors.BOLD)}                 " + color('│', Colors.DIM))
print(color('  │', Colors.DIM) + f"     Accuracy:     {color(f'{acc*100:.1f}%', Colors.GREEN if acc > 0.7 else Colors.YELLOW, Colors.BOLD):>38s}    Macro F1: {color(f'{macro_f1:.3f}', grade_color, Colors.BOLD)}            " + color('│', Colors.DIM))
print(color('  ╰─────────────────────────────────────────────────────────────────────────────────╯', Colors.DIM))

# Dataset Distribution
print_section("📁 DATASET DISTRIBUTION")
print()
print(f"  {'Class':<14} {'True':>8}  {'Pred':>8}  {'Diff':>8}  {'Distribution':<30}")
print(color(f"  {'─'*14} {'─'*8}  {'─'*8}  {'─'*8}  {'─'*30}", Colors.DIM))

total_true = len(y_true)
for i, smell in enumerate(SMELLS_ALPHA):
    true_count = (y_true == i).sum()
    pred_count = (y_pred == i).sum()
    diff = pred_count - true_count
    diff_color = Colors.GREEN if abs(diff) < true_count * 0.1 else (Colors.YELLOW if abs(diff) < true_count * 0.3 else Colors.RED)
    diff_str = f"+{diff}" if diff > 0 else str(diff)
    
    pct = true_count / total_true
    bar_width = int(30 * pct / 0.8)  # Scale to max ~80%
    bar = '█' * bar_width + '░' * (30 - bar_width)
    
    smell_icon = {'Clean': '✨', 'DataClass': '📦', 'DeadCode': '💀', 'FeatureEnvy': '👀', 'GodClass': '👑', 'LongMethod': '📏'}
    icon = smell_icon.get(smell, '•')
    
    print(f"  {icon} {smell:<12} {color(f'{true_count:>6,}', Colors.WHITE)}  {color(f'{pred_count:>6,}', Colors.CYAN)}  {color(f'{diff_str:>6}', diff_color)}  {color(bar, Colors.BLUE)} {pct*100:>5.1f}%")

print()

# Per-Smell Metrics Table
print_section("📈 PER-CLASS PERFORMANCE METRICS")
print()
print(f"  {'Class':<14} {'Precision':>10} {'Recall':>10} {'F1-Score':>10} {'Support':>10}  {'Performance':<25}")
print(color(f"  {'─'*14} {'─'*10} {'─'*10} {'─'*10} {'─'*10}  {'─'*25}", Colors.DIM))

for i, smell in enumerate(SMELLS_ALPHA):
    grade, grade_color = get_grade(f1[i])
    
    # Color code metrics
    p_color = Colors.GREEN if p[i] >= 0.7 else (Colors.YELLOW if p[i] >= 0.4 else Colors.RED)
    r_color = Colors.GREEN if r[i] >= 0.7 else (Colors.YELLOW if r[i] >= 0.4 else Colors.RED)
    f1_color = grade_color
    
    # Performance bar
    perf_bar = progress_bar(f1[i], 1.0, 15)
    
    smell_icon = {'Clean': '✨', 'DataClass': '📦', 'DeadCode': '💀', 'FeatureEnvy': '👀', 'GodClass': '👑', 'LongMethod': '📏'}
    icon = smell_icon.get(smell, '•')
    
    print(f"  {icon} {smell:<12} {color(f'{p[i]:.3f}', p_color):>18} {color(f'{r[i]:.3f}', r_color):>18} {color(f'{f1[i]:.3f}', f1_color):>18} {support[i]:>10,}  {color(perf_bar, grade_color)} {color(grade, grade_color, Colors.BOLD)}")

print()
print(color(f"  {'─'*90}", Colors.DIM))
print(f"  {color('OVERALL', Colors.WHITE, Colors.BOLD):<22} {color(f'{np.mean(p):.3f}', Colors.CYAN):>18} {color(f'{np.mean(r):.3f}', Colors.CYAN):>18} {color(f'{macro_f1:.3f}', grade_color):>18} {sum(support):>10,}  {color(progress_bar(macro_f1, 1.0, 15), grade_color)} {color(overall_grade, grade_color, Colors.BOLD)}")
print()

# Confusion Matrix
print_section("🎯 CONFUSION MATRIX (True → Predicted)")
print()

# Header row
header = "  " + " " * 14
for smell in SMELLS_ALPHA:
    short = smell[:8]
    header += f"{short:>10}"
header += f"  {'Total':>8}"
print(color(header, Colors.WHITE, Colors.BOLD))
print(color("  " + "─" * 14 + ("─" * 10) * 6 + "──" + "─" * 8, Colors.DIM))

for i, smell in enumerate(SMELLS_ALPHA):
    row = f"  {smell:<14}"
    for j in range(6):
        val = cm[i][j]
        if i == j:
            # Diagonal (correct predictions) - green
            row += color(f"{val:>10,}", Colors.GREEN, Colors.BOLD)
        elif val > 100:
            # Major confusion - red
            row += color(f"{val:>10,}", Colors.RED)
        elif val > 50:
            # Moderate confusion - yellow
            row += color(f"{val:>10,}", Colors.YELLOW)
        elif val > 0:
            # Minor confusion - dim
            row += color(f"{val:>10,}", Colors.DIM)
        else:
            row += color(f"{val:>10}", Colors.DIM)
    row += color(f"  {support[i]:>8,}", Colors.CYAN)
    print(row)

print()

# Top Confusions
print_section("⚠️  TOP MISCLASSIFICATIONS")
print()

confusions = []
for i in range(6):
    for j in range(6):
        if i != j and cm[i][j] > 0:
            confusions.append((SMELLS_ALPHA[i], SMELLS_ALPHA[j], cm[i][j]))

confusions.sort(key=lambda x: -x[2])
top_n = min(8, len([c for c in confusions if c[2] > 10]))

for true_label, pred_label, count in confusions[:top_n]:
    pct_of_true = count / support[SMELLS_ALPHA.index(true_label)] * 100
    severity = Colors.RED if count > 200 else (Colors.YELLOW if count > 50 else Colors.DIM)
    bar_width = min(30, int(count / 20))
    bar = '█' * bar_width
    
    print(f"  {true_label:<14} {color('→', Colors.DIM)} {pred_label:<14} {color(f'{count:>5,}', severity)} errors ({pct_of_true:>5.1f}% of {true_label}) {color(bar, severity)}")

print()

# Diagnosis & Recommendations
print_section("🔍 DIAGNOSIS & INSIGHTS")
print()

issues = []
recommendations = []

# Check for class imbalance issues
min_support = min(support)
max_support = max(support)
imbalance_ratio = max_support / min_support if min_support > 0 else float('inf')

if imbalance_ratio > 100:
    issues.append(("🚨", Colors.RED, "SEVERE CLASS IMBALANCE", f"Ratio {imbalance_ratio:.0f}:1 between largest and smallest class"))
    recommendations.append(("Class Balancing", "Use SMOTE, class weights, or focal loss to handle imbalance"))

# Check individual class performance
for i, smell in enumerate(SMELLS_ALPHA):
    if f1[i] < 0.30:
        issues.append(("❌", Colors.RED, f"{smell} CRITICAL", f"F1={f1[i]:.3f} - Model essentially failing on this class"))
        if support[i] < 50:
            recommendations.append((f"Augment {smell}", f"Only {support[i]} samples - need 5-10x more through augmentation"))
    elif f1[i] < 0.50 and smell != "FeatureEnvy":
        issues.append(("⚠️", Colors.YELLOW, f"{smell} UNDERPERFORMING", f"F1={f1[i]:.3f} - Below acceptable threshold"))

# Check precision/recall balance
for i, smell in enumerate(SMELLS_ALPHA):
    if p[i] > 0 and r[i] > 0:
        pr_ratio = p[i] / r[i]
        if pr_ratio > 2:
            issues.append(("📉", Colors.YELLOW, f"{smell} LOW RECALL", f"P/R ratio {pr_ratio:.1f} - Missing too many actual cases"))
        elif pr_ratio < 0.5:
            issues.append(("📈", Colors.YELLOW, f"{smell} LOW PRECISION", f"P/R ratio {pr_ratio:.1f} - Too many false positives"))

# Overall assessment
if macro_f1 >= 0.65:
    overall_status = ("✅", Colors.GREEN, "GOOD PERFORMANCE", "Model is performing reasonably well")
elif macro_f1 >= 0.50:
    overall_status = ("🔶", Colors.YELLOW, "ACCEPTABLE PERFORMANCE", "Model works but has room for improvement")
else:
    overall_status = ("🔴", Colors.RED, "NEEDS IMPROVEMENT", "Model requires significant tuning")

print(f"  {overall_status[0]} {color(overall_status[2], overall_status[1], Colors.BOLD)}: {overall_status[3]}")
print()

if issues:
    print(f"  {color('Issues Detected:', Colors.WHITE, Colors.UNDERLINE)}")
    for icon, clr, title, desc in issues[:6]:  # Limit to top 6
        print(f"    {icon} {color(title, clr)}: {desc}")
    print()

# Recommendations
print_section("💡 RECOMMENDED ACTIONS")
print()

priority_actions = [
    ("HIGH", Colors.RED, "Address Class Imbalance", [
        "Add class_weight='balanced' to your loss function",
        "Oversample minority classes (DataClass, DeadCode) by 10-20x",
        "Consider Focal Loss: γ=2.0 focuses on hard examples"
    ]),
    ("MED", Colors.YELLOW, "Improve FeatureEnvy Detection", [
        "This is semantic - CodeBERT helps but needs more context",
        "Try combining CodeBERT embeddings + CK metrics (fusion model)",
        "Add data flow analysis features"
    ]),
    ("MED", Colors.YELLOW, "Reduce Clean↔FeatureEnvy Confusion", [
        "These share similar structure but different semantics",
        "Add method-external reference counting as feature",
        "Consider two-stage classifier: binary first, then multiclass"
    ]),
    ("LOW", Colors.CYAN, "Fine-tuning Improvements", [
        "Try learning rate warmup + cosine decay",
        "Experiment with larger context windows (512→1024 tokens)",
        "Add layer-wise learning rate decay for CodeBERT"
    ])
]

for priority, clr, title, actions in priority_actions:
    print(f"  [{color(priority, clr, Colors.BOLD)}] {color(title, Colors.WHITE, Colors.BOLD)}")
    for action in actions:
        print(f"       {color('→', Colors.DIM)} {action}")
    print()

# Final Summary Box
print()
print(color('╔' + '═' * 88 + '╗', Colors.CYAN))
print(color('║', Colors.CYAN) + color(' 📋 SUMMARY METRICS '.center(88), Colors.WHITE, Colors.BOLD) + color('║', Colors.CYAN))
print(color('╠' + '═' * 88 + '╣', Colors.CYAN))
metric_line = f"  Accuracy: {color(f'{acc*100:.1f}%', Colors.GREEN if acc > 0.7 else Colors.YELLOW)}   │   Macro F1: {color(f'{macro_f1:.3f}', grade_color)}   │   Micro F1: {color(f'{micro_f1:.3f}', Colors.CYAN)}   │   Grade: {color(overall_grade, grade_color, Colors.BOLD)}"
print(color('║', Colors.CYAN) + metric_line.ljust(117) + color('║', Colors.CYAN))
print(color('╚' + '═' * 88 + '╝', Colors.CYAN))
print()
print(color(f"  Analysis completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", Colors.DIM))
print()