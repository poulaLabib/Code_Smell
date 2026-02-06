"""
Test Extended Smell Detection with 100 Java Code Samples
Tests all new detection features: MagicNumbers, GlobalMutableState, RawCollections,
SwallowedException, DeadCode, DuplicateCode, PointlessLoop, UnnecessaryBoxing,
BadNaming, GodMethod
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from extended_test_samples import EXTENDED_TEST_SAMPLES

# Import the predictor
import predict_smell_extended as ps

def run_extended_tests():
    """Run all 100 extended smell detection tests"""
    
    print("="*70)
    print("EXTENDED SMELL DETECTION TEST SUITE")
    print("Testing 100 Java code samples for new detection features")
    print("="*70)
    print()
    
    # Load models
    models = ps.load_models()
    
    # Track results
    results = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "partial": 0,
        "by_smell": defaultdict(lambda: {"expected": 0, "detected": 0}),
        "failures": [],
        "partial_matches": []
    }
    
    # Category tracking
    categories = {
        "MagicNumbers": (1, 10),
        "GlobalMutableState": (11, 20),
        "RawCollections": (21, 30),
        "SwallowedException": (31, 40),
        "DeadCode": (41, 50),
        "DuplicateCode": (51, 60),
        "PointlessLoop": (61, 70),
        "UnnecessaryBoxing": (71, 80),
        "BadNaming": (81, 90),
        "GodMethod": (91, 95),
        "Combined": (96, 100)
    }
    
    for sample in EXTENDED_TEST_SAMPLES:
        results["total"] += 1
        sample_id = sample["id"]
        name = sample["name"]
        expected_smells = set(sample["expected_smells"])
        code = sample["code"]
        
        # Run prediction
        result = ps.predict_smell(code, models, use_extended=True)
        
        # Collect detected smells
        detected_smells = set()
        
        # Add primary smell
        if result.primary_smell:
            detected_smells.add(result.primary_smell)
        
        # Add all smells from all_smells
        for smell, conf in result.all_smells:
            detected_smells.add(smell)
        
        # Add extended smells
        for smell, conf, desc in result.details.get("extended_smells", []):
            detected_smells.add(smell)
        
        # Track by smell type
        for smell in expected_smells:
            results["by_smell"][smell]["expected"] += 1
            if smell in detected_smells:
                results["by_smell"][smell]["detected"] += 1
        
        # Check if all expected smells were detected
        matched = expected_smells.intersection(detected_smells)
        missing = expected_smells - detected_smells
        
        if len(missing) == 0:
            # All expected smells detected
            results["passed"] += 1
            status = "✅ PASS"
        elif len(matched) > 0:
            # Some expected smells detected
            results["partial"] += 1
            status = "⚠️ PARTIAL"
            results["partial_matches"].append({
                "id": sample_id,
                "name": name,
                "expected": list(expected_smells),
                "detected": list(matched),
                "missing": list(missing)
            })
        else:
            # No expected smells detected
            results["failed"] += 1
            status = "❌ FAIL"
            results["failures"].append({
                "id": sample_id,
                "name": name,
                "expected": list(expected_smells),
                "detected": list(detected_smells)
            })
        
        # Print progress for each sample
        exp_str = ", ".join(sorted(expected_smells))
        det_str = ", ".join(sorted(detected_smells)) if detected_smells else "(none)"
        print(f"[{sample_id:3d}] {status} {name}")
        print(f"      Expected: {exp_str}")
        print(f"      Detected: {det_str}")
        print()
    
    # Print summary
    print()
    print("="*70)
    print("SUMMARY")
    print("="*70)
    print()
    
    total = results["total"]
    passed = results["passed"]
    partial = results["partial"]
    failed = results["failed"]
    
    pass_rate = (passed / total) * 100 if total > 0 else 0
    overall_rate = ((passed + partial) / total) * 100 if total > 0 else 0
    
    print(f"Total Samples:    {total}")
    print(f"Passed (full):    {passed} ({pass_rate:.1f}%)")
    print(f"Partial Match:    {partial}")
    print(f"Failed:           {failed}")
    print(f"Overall Success:  {overall_rate:.1f}%")
    print()
    
    # By smell type
    print("Detection Rate by Smell Type:")
    print("-"*50)
    for smell in sorted(results["by_smell"].keys()):
        stats = results["by_smell"][smell]
        rate = (stats["detected"] / stats["expected"]) * 100 if stats["expected"] > 0 else 0
        bar = "█" * int(rate / 10) + "░" * (10 - int(rate / 10))
        print(f"  {smell:20s} [{bar}] {rate:5.1f}% ({stats['detected']}/{stats['expected']})")
    
    # By category
    print()
    print("Detection Rate by Category:")
    print("-"*50)
    for cat_name, (start, end) in categories.items():
        cat_samples = [s for s in EXTENDED_TEST_SAMPLES if start <= s["id"] <= end]
        cat_passed = 0
        for sample in cat_samples:
            sample_id = sample["id"]
            if not any(f["id"] == sample_id for f in results["failures"]) and \
               not any(p["id"] == sample_id for p in results["partial_matches"]):
                cat_passed += 1
        cat_rate = (cat_passed / len(cat_samples)) * 100 if cat_samples else 0
        bar = "█" * int(cat_rate / 10) + "░" * (10 - int(cat_rate / 10))
        print(f"  {cat_name:20s} [{bar}] {cat_rate:5.1f}% ({cat_passed}/{len(cat_samples)})")
    
    # Print failures
    if results["failures"]:
        print()
        print("="*70)
        print("FAILURES (No expected smells detected)")
        print("="*70)
        for f in results["failures"]:
            print(f"  [{f['id']}] {f['name']}")
            print(f"       Expected: {', '.join(f['expected'])}")
            print(f"       Detected: {', '.join(f['detected']) if f['detected'] else '(none)'}")
    
    # Print partial matches
    if results["partial_matches"]:
        print()
        print("="*70)
        print("PARTIAL MATCHES (Some expected smells missing)")
        print("="*70)
        for p in results["partial_matches"]:
            print(f"  [{p['id']}] {p['name']}")
            print(f"       Missing:  {', '.join(p['missing'])}")
    
    print()
    print("="*70)
    print("TEST COMPLETE")
    print("="*70)
    
    return pass_rate >= 80

if __name__ == "__main__":
    success = run_extended_tests()
    sys.exit(0 if success else 1)
