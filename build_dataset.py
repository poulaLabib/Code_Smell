"""
Dataset Builder — FIXED VERSION
=================================
Merges CK metrics + Sonar detections into one unified dataset.
Works correctly on both synthetic AND real projects.

Key logic:
  - CK metrics provide the FEATURES (numeric) + raw_code (text)
  - Sonar detections provide the LABELS (predicted smell per class)
  - Matching is done by file_path (both tools write the same absolute path)
  - For real projects: label comes from Sonar detection
  - For synthetic projects: we ALSO have ground_truth_meta.json for validation
  - Gold set: a subset flagged for manual human review

The "Label Quality Report" only compares Sonar vs ground_truth for the
synthetic -sim projects (where we know the true answer). For real projects,
Sonar IS the label — you manually verify a sample to build the gold set.
"""

import json, csv, os, random
from collections import defaultdict, Counter

# ── Dynamic path ──
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = SCRIPT_DIR

random.seed(42)

# ── Load CK metrics (features + raw code) ──
ck_path = os.path.join(BASE, "ck_metrics", "all_ck_metrics.json")
print("Loading CK metrics from: {}".format(ck_path))
with open(ck_path) as f:
    ck_data = json.load(f)
print("  Loaded {} classes from CK".format(len(ck_data)))

# ── Load Sonar detections (labels) ──
sonar_path = os.path.join(BASE, "sonar_issues", "all_sonar_issues.json")
print("Loading Sonar issues from: {}".format(sonar_path))
with open(sonar_path) as f:
    sonar_data = json.load(f)["issues"]
print("  Loaded {} Sonar issues".format(len(sonar_data)))

# ── Load ground truth (only exists for synthetic -sim projects) ──
truth_path = os.path.join(BASE, "gold_set", "ground_truth_meta.json")
truth_by_path = {}
if os.path.exists(truth_path):
    with open(truth_path) as f:
        truth_data = json.load(f)
    # Index by file_path
    for t in truth_data:
        truth_by_path[t["file_path"]] = t["true_smell"]
    print("  Loaded {} ground-truth entries (synthetic projects only)".format(len(truth_by_path)))
else:
    print("  No ground_truth_meta.json — will use Sonar labels only")

# ── Index Sonar detections by file_path ──
sonar_by_path = defaultdict(list)
for issue in sonar_data:
    sonar_by_path[issue["file_path"]].append(issue["smell_label"])

# ── Smell types ──
SMELL_TYPES = ["GodClass", "FeatureEnvy", "LongMethod", "DataClass", "DeadCode"]

# ── Build unified dataset ──
dataset = []
unmatched_sonar = 0  # count CK files that have no Sonar match

for ck in ck_data:
    fpath = ck["file_path"]

    # --- Get Sonar labels for this file ---
    sonar_smells = sonar_by_path.get(fpath, [])

    # --- Determine predicted smell (from Sonar) ---
    # If multiple smells detected, pick the most "severe" one in priority order
    priority = ["GodClass", "LongMethod", "FeatureEnvy", "DataClass", "DeadCode"]
    predicted_smell = "Clean"
    for p in priority:
        if p in sonar_smells:
            predicted_smell = p
            break

    # --- Determine true smell ---
    # For synthetic projects: use ground truth
    # For real projects: use Sonar prediction (this IS our label)
    is_synthetic = ck["project"].endswith("-sim")
    if is_synthetic and fpath in truth_by_path:
        true_smell = truth_by_path[fpath]
    else:
        # Real project: Sonar label IS the truth for training
        true_smell = predicted_smell

    row = {
        # Identifiers
        "project":      ck["project"],
        "file_path":    fpath,
        "class_name":   ck["class_name"],
        "package":      ck["package"],
        "is_synthetic": is_synthetic,

        # Numeric features
        "LOC":              ck["LOC"],
        "WMC":              ck["WMC"],
        "METHODS":          ck["METHODS"],
        "FIELDS":           ck["FIELDS"],
        "PRIVATE_METHODS":  ck["PRIVATE_METHODS"],
        "CBO":              ck["CBO"],
        "DIT":              ck["DIT"],
        "LCOM":             ck["LCOM"],
        "TCC":              ck["TCC"],
        "ATFD":             ck["ATFD"],
        "MAX_METHOD_LOC":   ck["MAX_METHOD_LOC"],
        "NOC":              ck["NOC"],

        # Code text (for CodeBERT)
        "raw_code":         ck["raw_code"],

        # Labels
        "predicted_smell":  predicted_smell,
        "true_smell":       true_smell,
        "label_OR":         1 if len(sonar_smells) > 0 else 0,
    }

    # Per-smell binary flags from Sonar
    for smell in SMELL_TYPES:
        row["sonar_" + smell] = 1 if smell in sonar_smells else 0

    # Per-smell binary ground truth
    for smell in SMELL_TYPES:
        row["true_" + smell] = 1 if true_smell == smell else 0
    row["true_Clean"] = 1 if true_smell == "Clean" else 0

    dataset.append(row)

print("\nDataset built: {} total examples".format(len(dataset)))

# ── Stats ──
real_count = sum(1 for r in dataset if not r["is_synthetic"])
sim_count  = sum(1 for r in dataset if r["is_synthetic"])
print("  Real projects: {} classes | Synthetic projects: {} classes".format(real_count, sim_count))

smell_dist = Counter(r["true_smell"] for r in dataset)
print("\n  Label distribution (all projects):")
for smell in SMELL_TYPES + ["Clean"]:
    count = smell_dist.get(smell, 0)
    pct = count / len(dataset) * 100 if len(dataset) > 0 else 0
    bar = "X" * int(pct / 2)
    print("    {:15s}: {:5d} ({:5.1f}%)  {}".format(smell, count, pct, bar))

# ── Save dataset CSV (no raw_code) ──
csv_keys = [k for k in dataset[0].keys() if k != "raw_code"]
with open(os.path.join(BASE, "dataset", "dataset.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=csv_keys)
    w.writeheader()
    for row in dataset:
        w.writerow({k: row[k] for k in csv_keys})

# ── Save dataset JSON (with raw_code) ──
with open(os.path.join(BASE, "dataset", "dataset.json"), "w") as f:
    json.dump(dataset, f, indent=2)

print("\n  Saved dataset.csv and dataset.json")

# ── Label Quality Report (synthetic projects only — where we have ground truth) ──
print("\n--- Label Quality Report (Synthetic Projects Only) ---")
print("    (Compares Sonar prediction vs known ground truth)")
syn_dataset = [r for r in dataset if r["is_synthetic"]]
if syn_dataset:
    for smell in SMELL_TYPES + ["Clean"]:
        tp = sum(1 for r in syn_dataset if r["true_smell"] == smell and r["predicted_smell"] == smell)
        fp = sum(1 for r in syn_dataset if r["true_smell"] != smell and r["predicted_smell"] == smell)
        fn = sum(1 for r in syn_dataset if r["true_smell"] == smell and r["predicted_smell"] != smell)
        tn = sum(1 for r in syn_dataset if r["true_smell"] != smell and r["predicted_smell"] != smell)
        p  = tp / (tp + fp) if (tp + fp) > 0 else 0
        r  = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2*p*r / (p+r) if (p+r) > 0 else 0
        print("  {:15s} | P={:.2f} R={:.2f} F1={:.2f} | TP={:3d} FP={:3d} FN={:3d} TN={:3d}".format(
            smell, p, r, f1, tp, fp, fn, tn))
else:
    print("  (no synthetic projects in dataset)")

# ── Project-level split ──
# Separate real and synthetic into their own splits
# Real projects: 70/15/15 split
# Synthetic projects: all go to a secondary eval set
all_projects = sorted(set(r["project"] for r in dataset))
real_projects = sorted(set(r["project"] for r in dataset if not r["is_synthetic"]))
sim_projects  = sorted(set(r["project"] for r in dataset if r["is_synthetic"]))

print("\n--- Project-Level Split ---")
print("  All projects: {}".format(all_projects))

if len(real_projects) >= 3:
    n = len(real_projects)
    train_end = int(n * 0.70)
    val_end   = train_end + max(1, int(n * 0.15))

    train_projs = real_projects[:train_end]
    val_projs   = real_projects[train_end:val_end]
    test_projs  = real_projects[val_end:]

    # Add some synthetic to train for augmentation
    if len(sim_projects) >= 3:
        train_projs += sim_projects[:int(len(sim_projects)*0.7)]
        val_projs   += sim_projects[int(len(sim_projects)*0.7):int(len(sim_projects)*0.85)]
        test_projs  += sim_projects[int(len(sim_projects)*0.85):]
else:
    # Not enough real projects — use everything together
    n = len(all_projects)
    train_end = int(n * 0.70)
    val_end   = train_end + max(1, int(n * 0.15))
    train_projs = all_projects[:train_end]
    val_projs   = all_projects[train_end:val_end]
    test_projs  = all_projects[val_end:]

print("  TRAIN: {} projects".format(len(train_projs)))
print("  VAL:   {} projects".format(len(val_projs)))
print("  TEST:  {} projects".format(len(test_projs)))

split_info = {"train": train_projs, "val": val_projs, "test": test_projs}
with open(os.path.join(BASE, "dataset", "split_info.json"), "w") as f:
    json.dump(split_info, f, indent=2)

# Add split to each row
for row in dataset:
    if row["project"] in train_projs:   row["split"] = "train"
    elif row["project"] in val_projs:   row["split"] = "val"
    else:                               row["split"] = "test"

train_n = sum(1 for r in dataset if r["split"] == "train")
val_n   = sum(1 for r in dataset if r["split"] == "val")
test_n  = sum(1 for r in dataset if r["split"] == "test")
print("  TRAIN: {} examples | VAL: {} examples | TEST: {} examples".format(train_n, val_n, test_n))

# Re-save with split
with open(os.path.join(BASE, "dataset", "dataset.json"), "w") as f:
    json.dump(dataset, f, indent=2)

# ── Gold Validation Set ──
# Sample stratified examples across smells from TEST set
# These are the ones a human should manually review and correct labels on
print("\n--- Gold Validation Set ---")
test_dataset = [r for r in dataset if r["split"] == "test"]
gold = []
by_smell = defaultdict(list)
for r in test_dataset:
    by_smell[r["true_smell"]].append(r)

gold_targets = {"GodClass": 30, "FeatureEnvy": 25, "LongMethod": 30,
                "DataClass": 30, "DeadCode": 20, "Clean": 50}

for smell, target in gold_targets.items():
    pool = by_smell.get(smell, [])
    n = min(target, len(pool))
    if n > 0:
        selected = random.sample(pool, n)
        gold.extend(selected)
        print("  {:15s}: {} sampled (pool={})".format(smell, n, len(pool)))

# Save gold set
with open(os.path.join(BASE, "gold_set", "gold_validation.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=csv_keys)
    w.writeheader()
    for row in gold:
        w.writerow({k: row[k] for k in csv_keys})

print("\n  Gold set total: {} examples saved to gold_set/gold_validation.csv".format(len(gold)))
print("  --> NEXT STEP: Open gold_validation.csv and manually verify/correct the 'true_smell' column")
print("      Then re-run build_dataset.py with your corrections.")
print("\n--- DONE ---")
print("Next commands to run:")
print("  python baseline_a_rf.py")
print("  python baseline_b_text.py")
