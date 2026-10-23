#!/usr/bin/env python3
"""Integrity for the clause-by-clause ADR legal editorial review.

Mechanically checks completeness and freshness. DOES NOT establish legal truth,
an authoritative Polish-text comparison, or an independent DGSA approval.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_FIELDS = ("id","module_id","stem","options","correct_option","explanation","sources","legal_basis_version","image")


def validate(root=ROOT, expected=None):
    errors, processed = [], []
    question_file = root/"podstawowy"/"questions.jsonl"
    questions = [json.loads(s) for s in question_file.read_text(encoding="utf-8").splitlines() if s.strip()]
    paths = sorted((root/"review"/"legal-clauses").glob("*.json"))
    if not paths:
        return ["No clause review files"], {"reviewed":0,"questions":len(questions)}
    for file in paths:
        try:
            document = json.loads(file.read_text(encoding="utf-8"))
        except ValueError as e:
            errors.append(f"{file.name}: invalid JSON {e}")
            continue
        if document.get("release_approved") is not False:
            errors.append(f"{file.name}: false claim of release approval")
        for item in document.get("records", []):
            i=len(processed)
            processed.append(item)
            if i>=len(questions):
                errors.append(f"{file.name}: extra review item")
                continue
            q=questions[i]
            id=q["id"]
            if item.get("id")!=id or item.get("order")!=i+1:
                errors.append(f"Unexpected review order: {id}")
            snap={k:q.get(k) for k in SNAPSHOT_FIELDS}
            if item.get("question_snapshot")!=snap:
                errors.append(f"{id}: stale legal-review snapshot")
            if item.get("observed_answer_key")!=q["correct_option"]:
                errors.append(f"{id}: answer key mismatch")
            assessment=item.get("answer_review",{})
            for letter in "ABC":
                data=assessment.get(letter,{})
                if data.get("expected_correct") is not (letter==q["correct_option"]):
                    errors.append(f"{id}: incorrect truth-value for option {letter}")
                if not isinstance(data.get("rationale"),str) or len(data["rationale"].strip())<20:
                    errors.append(f"{id}: missing reasoning for option {letter}")
            if item.get("official_polish_full_text_comparison")!="pending":
                errors.append(f"{id}: unsupported official Polish text attestation")
            if item.get("independent_specialist_approval")!="pending":
                errors.append(f"{id}: unsupported specialist approval")
            if item.get("final_verification_status")!="needs_review":
                errors.append(f"{id}: unsupported verified claim")
            if not isinstance(item.get("notes_on_conditions"),str) or len(item["notes_on_conditions"])<25:
                errors.append(f"{id}: missing legal-condition note")
            if not str(item.get("source_2025_comparison_url","")).startswith("https://"):
                errors.append(f"{id}: missing additional source")
    if expected is None:
        expected = len(questions)
    if len(processed)!=expected:
        errors.append(f"Expected {expected} clause-by-clause reviews; got {len(processed)}")
    if any(q["verification_status"]=="verified" for q in questions[:len(processed)]):
        errors.append("Unexpected verified status before specialist approval")
    return errors,{"reviewed":len(processed),"questions":len(questions),"files":len(paths)}


def main():
    errors, stats=validate()
    print("ADR legal review QA:", stats)
    if errors:
        for e in errors[:25]:
            print("ERROR:",e)
        return 1
    print("PASS: A/B/C detailed editorial rationale for all bank IDs; Polish official text and independent expert signoff still pending.")
    return 0


if __name__=="__main__":
    sys.exit(main())
