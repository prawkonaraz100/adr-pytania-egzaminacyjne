#!/usr/bin/env python3
"""Fail-closed exporter: ONLY individually verified and attested ADR questions.

Automated attestation checks do NOT prove the reviewer is a qualified ADR expert
or that the legal reasoning is correct. Both require real human verification.
"""

import argparse
import hashlib
import json
import os
import tempfile
from collections import Counter
from datetime import date
from pathlib import Path

from validate import MODULES, validate_record

ROOT = Path(__file__).resolve().parents[1]
REVIEW_FIELDS = {"id", "content_sha256", "reviewer", "checked_at", "evidence_path"}
CONTENT_FIELDS = (
    "id", "module_id", "stem", "options", "correct_option", "explanation",
    "sources", "legal_basis_version", "image",
)


def content_sha256(record):
    """Digest binds review to question and every answer, excluding review metadata."""
    payload = {key: record[key] for key in CONTENT_FIELDS}
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def load_jsonl(path):
    if not path.is_file():
        raise ValueError(f"Missing input file: {path}")
    records = []
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{index}: Invalid JSON: {exc.msg}") from exc
        if not isinstance(obj, dict):
            raise ValueError(f"{path}:{index}: Record must be an object")
        records.append(obj)
    return records


def check_attestation(record, approval, root):
    """Validate documentary evidence; does not attest professional qualifications."""
    qid = record["id"]
    errors = []
    if set(approval) != REVIEW_FIELDS:
        return [f"{qid}: approval fields must be {', '.join(sorted(REVIEW_FIELDS))}"]
    if approval["id"] != qid:
        errors.append(f"{qid}: mismatched approval ID")
    if record.get("checked_at") != approval["checked_at"] or record.get("reviewer") != approval["reviewer"]:
        errors.append(f"{qid}: reviewer or review date differs from approval")
    if not isinstance(approval["reviewer"], str) or len(approval["reviewer"].strip()) < 3:
        errors.append(f"{qid}: approval reviewer missing")
    try:
        reviewed = date.fromisoformat(approval["checked_at"])
        if reviewed.isoformat() != approval["checked_at"] or reviewed > date.today():
            errors.append(f"{qid}: invalid or future approval date")
    except (TypeError, ValueError):
        errors.append(f"{qid}: approval checked_at must be ISO date")
    if not isinstance(approval["content_sha256"], str) or approval["content_sha256"] != content_sha256(record):
        errors.append(f"{qid}: reviewed content hash mismatch")
    loc = approval["evidence_path"]
    if not isinstance(loc, str):
        errors.append(f"{qid}: evidence_path must be a repository-relative path")
    else:
        p = Path(loc)
        if p.is_absolute() or ".." in p.parts or len(p.parts) < 3 or p.parts[:2] != ("review", "reports") or p.suffix != ".md":
            errors.append(f"{qid}: evidence must be a Markdown file under review/reports/")
        else:
            report = root / p
            if not report.is_file():
                errors.append(f"{qid}: review evidence missing: {loc}")
            else:
                body = report.read_text(encoding="utf-8")
                if qid not in body or len(body.strip()) < 100:
                    errors.append(f"{qid}: evidence file must contain ID and substantive review")
    return errors


def eligible(records, approvals, root, minimum=30):
    """Return (verified exportable records, blockers)."""
    errors = []
    if not isinstance(minimum, int) or minimum < 1:
        return [], ["minimum must be a positive integer"]
    approved = {}
    for a in approvals:
        ident = a.get("id")
        if not isinstance(ident, str):
            errors.append("approval entry missing string ID")
        elif ident in approved:
            errors.append(f"{ident}: duplicate approval entry")
        else:
            approved[ident] = a
    questions = {q.get("id"): q for q in records if isinstance(q.get("id"), str)}
    for ident in sorted(set(approved) - set(questions)):
        errors.append(f"{ident}: approval for absent question")
    results = []
    for q in records:
        if q.get("verification_status") != "verified":
            continue
        errors.extend(f"{q.get('id')}: {m}" for m in validate_record(q))
        a = approved.get(q.get("id"))
        if a is None:
            errors.append(f"{q.get('id')}: verified without independent approval record")
            continue
        errors.extend(check_attestation(q, a, root))
        results.append(q)
    if len(results) < minimum:
        errors.append(f"release requires at least {minimum} verified records; found {len(results)}")
    covered = {q["module_id"] for q in results if q.get("module_id") in MODULES}
    if covered != MODULES:
        errors.append("release missing ADR basic modules: " + ", ".join(sorted(MODULES - covered)))
    # A question left in pending status is never included even if there is an approval.
    errors.extend(f"{id}: approval exists but question is not verified" for id in sorted(set(approved) - {q['id'] for q in results}))
    return sorted(results, key=lambda q: q["id"]), errors


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, default=ROOT / "podstawowy/questions.jsonl")
    parser.add_argument("--approvals", type=Path, default=ROOT / "review/approvals.jsonl")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, help="Explicit output path; no output on rejected build")
    parser.add_argument("--minimum", type=int, default=30)
    parser.add_argument("--report", action="store_true", help="Show release blockers; always exit zero, no export")
    args = parser.parse_args(argv)
    if not args.report and args.output is None:
        parser.error("Provide --output or use --report")
    try:
        questions = load_jsonl(args.questions)
        approvals = load_jsonl(args.approvals)
        export, blockers = eligible(questions, approvals, args.root, args.minimum)
    except (ValueError, KeyError, TypeError) as exc:
        if args.report:
            print(f"BLOCKED: {exc}")
            return 0
        print(f"BLOCKED: {exc}")
        return 1

    statuses = Counter(q.get("verification_status") for q in questions)
    print(f"ADR release gate: verified={statuses['verified']}, needs_review={statuses['needs_review']}, approvals={len(approvals)}")
    if blockers:
        print(f"BLOCKED: {len(blockers)} condition(s)")
        for msg in blockers[:35]:
            print(" - " + msg)
        if len(blockers) > 35:
            print(f" ... and {len(blockers)-35} more")
        return 0 if args.report else 1
    if args.report:
        print(f"ELIGIBLE (not exported): {len(export)} verified records")
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Atomic write prevents a half-built output on system failure.
    data = "".join(json.dumps(q, ensure_ascii=False, sort_keys=True) + "\n" for q in export)
    name = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=args.output.parent, delete=False) as handle:
            name = handle.name
            handle.write(data)
        os.replace(name, args.output)
    finally:
        if name is not None and os.path.exists(name):
            os.unlink(name)
    print(f"EXPORTED: {len(export)} verified questions -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
