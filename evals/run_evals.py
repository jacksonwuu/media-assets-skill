#!/usr/bin/env python3
"""Run media-assets-skill eval cases and score results.

Usage:
  python3 evals/run_evals.py                # interactive mode
  python3 evals/run_evals.py --type quality # filter by case type
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def load_cases(cases_dir: Path, case_type: str | None) -> list[dict]:
    if yaml is None:
        sys.exit("PyYAML is required: pip install pyyaml")
    cases = []
    for path in sorted(cases_dir.rglob("*.yaml")):
        case = yaml.safe_load(path.read_text())
        case["_path"] = path
        if case_type and case.get("type") != case_type:
            continue
        cases.append(case)
    return cases


def run_trigger_case(case: dict) -> dict:
    print(f"\n=== {case['name']} ({case['type']}) ===")
    print(f"Prompt: {case['prompt']}")
    answer = input("Was the skill triggered? [y/n/skip]: ").strip().lower()
    triggered = {"y": True, "n": False, "skip": None}.get(answer)
    expected = case["expectations"]["skill_triggered"]
    passed = triggered is not None and triggered == expected
    return {
        "name": case["name"],
        "type": case["type"],
        "passed": passed,
        "skill_triggered": triggered,
        "expected": expected,
    }


def run_quality_case(case: dict) -> dict:
    print(f"\n=== {case['name']} ({case['type']}) ===")
    print(f"Prompt: {case['prompt']}")
    scores = {}
    for criterion in case["expectations"]["criteria"]:
        cid = criterion["id"]
        required = "required" if criterion.get("required") else "optional"
        raw = input(f"  {cid} [{required}] score 0–1 (skip to omit): ").strip()
        if raw.lower() == "skip" or not raw:
            scores[cid] = None
        else:
            try:
                scores[cid] = float(raw)
            except ValueError:
                scores[cid] = None
    required_ids = [c["id"] for c in case["expectations"]["criteria"] if c.get("required")]
    passed = all((scores.get(cid) or 0) >= 0.5 for cid in required_ids)
    return {
        "name": case["name"],
        "type": case["type"],
        "passed": passed,
        "scores": scores,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--type", choices=["trigger-positive", "trigger-negative", "quality"], help="Filter by case type")
    parser.add_argument("--dry-run", action="store_true", help="List cases without running")
    args = parser.parse_args()

    cases_dir = Path(__file__).parent / "cases"
    results_dir = Path(__file__).parent / "results"
    cases = load_cases(cases_dir, args.type)

    if not cases:
        print("No cases found.")
        return

    print(f"Found {len(cases)} case(s):")
    for case in cases:
        print(f"  - {case['name']} ({case['type']})")

    if args.dry_run:
        return

    results = []
    for case in cases:
        if case["type"] in ("trigger-positive", "trigger-negative"):
            results.append(run_trigger_case(case))
        else:
            results.append(run_quality_case(case))

    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = results_dir / f"{timestamp}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps({"timestamp": timestamp, "passed": passed, "total": total, "results": results}, indent=2))

    print(f"\n=== Summary: {passed}/{total} passed ===")
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  [{status}] {r['name']}")
    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
