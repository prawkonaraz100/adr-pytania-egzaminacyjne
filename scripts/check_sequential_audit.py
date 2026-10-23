#!/usr/bin/env python3
"""Technical integrity of consecutive ADR editorial first-pass audit.

Checks *presence and freshness*, not ADR legal correctness or expert approval.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_FIELDS = ("stem", "options", "correct_option", "explanation", "sources", "legal_basis_version", "image")


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate(root=ROOT):
    errors = []
    bank = read_jsonl(root / "podstawowy" / "questions.jsonl")
    audit_dir = root / "review" / "sequential"
    paths = sorted(audit_dir.glob("*.json")) if audit_dir.is_dir() else []
    rows = []
    if not paths:
        errors.append("no sequential audit files")
    for path in paths:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            if payload.get("not_a_release_approval") is not True:
                errors.append(f"{path.name}: audit mistaken for approval")
            if payload.get("status") != "pending_full_official_polish_clause_and_independent_expert_review":
                errors.append(f"{path.name}: unsupported substantive verification status")
            current = payload.get("records")
            if not isinstance(current, list):
                errors.append(f"{path.name}: missing records")
                continue
            if not current:
                errors.append(f"{path.name}: empty audit batch")
                continue
            start = len(rows) + 1
            stop = start + len(current) - 1
            expected_name = f"{start:03d}-{stop:03d}.json"
            if path.name != expected_name:
                errors.append(f"{path.name}: expected contiguous batch name {expected_name}")
            rows.extend(current)
        except (ValueError, KeyError) as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
    if len(rows) != len(bank):
        errors.append(f"audit covers {len(rows)} vs bank {len(bank)} questions")
    for i, bank_row in enumerate(bank):
        if i >= len(rows):
            break
        a = rows[i]
        if a.get("id") != bank_row.get("id") or a.get("sequence") != i + 1:
            errors.append(f"row {i+1}: ID or sequence mismatch")
            continue
        expected = {key: bank_row.get(key) for key in SNAPSHOT_FIELDS}
        if a.get("exact_record_snapshot") != expected:
            errors.append(f"{a['id']}: stale audit snapshot after question edit")
        read = a.get("editorial_read_through", {})
        if any(read.get(key) is not True for key in
               ("stem", "option_A", "option_B", "option_C", "correct_option", "explanation", "reference_pointer")):
            errors.append(f"{a['id']}: editorial field not examined")
        if a.get("question_status") != bank_row.get("verification_status"):
            errors.append(f"{a['id']}: question status mismatch")
        if a.get("polish_official_text_fully_compared") is not False or a.get("independent_ADR_expert_approved") is not False:
            errors.append(f"{a['id']}: audit cannot claim unperformed official/expert approval")
        if a.get("review_outcome") != "editorial_first_pass_only_not_legally_approved":
            errors.append(f"{a['id']}: unsupported outcome")
        if a.get("source_crosscheck_scope") != "reference_listed_without_individual_full_clause_comparison" and not a.get("supplementary_source_url", "").startswith("https://"):
            errors.append(f"{a['id']}: source cross-check requires URL")
    return errors, {"questions": len(bank), "audit_records": len(rows), "batches": len(paths),
                    "manual_attention": sum(a.get("expert_review_priority")=="manual_attention" for a in rows),
                    "additional_source_crosschecks": sum(bool(a.get("supplementary_source_url")) for a in rows)}


def main():
    errors, stats = validate()
    print("ADR sequential editorial audit:", stats)
    if errors:
        for error in errors[:40]:
            print("ERROR:", error)
        if len(errors) > 40:
            print(f"... and {len(errors)-40} more")
        return 1
    print("PASS: 216 IDs covered in order with current snapshots. Expert/legal gate remains OPEN.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
