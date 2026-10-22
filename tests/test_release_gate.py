import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from release_gate import content_sha256, eligible, load_jsonl, main


def fixture_record(i):
    return {
        "id": f"ADR-B-{i:04d}",
        "module_id": f"ADR-B-{((i - 1) % 13) + 1:02d}",
        "stem": f"Przykładowe pytanie testowe dla rekordu {i} na potrzeby testu bramki?",
        "options": {"A": "Wariant o poprawnym opisie działania", "B": "Wariant alternatywny, ale błędny", "C": "Trzecia niepoprawna czynność"},
        "correct_option": "A",
        "explanation": "To wyłącznie sztuczny rekord używany do testowania mechaniki eksportu.",
        "sources": [{"code": "TEST", "reference": "1.1.1 (synthetic)", "url": "https://example.org/mock"}],
        "legal_basis_version": "TEST-ONLY",
        "verification_status": "verified",
        "checked_at": "2026-10-22",
        "reviewer": "Fikcyjny recenzent TESTÓW",
        "image": None,
    }


def fixtures(root, n=39):
    records = [fixture_record(i) for i in range(1, n + 1)]
    approvals = []
    reports = root / "review" / "reports"
    reports.mkdir(parents=True)
    for row in records:
        location = f"review/reports/{row['id']}.md"
        (root / location).write_text(
            f"# SYNTETYCZNY TEST — {row['id']}\n"
            "Wyłącznie sztuczna akceptacja do testów mechaniki w katalogu tymczasowym.\n"
            "Zweryfikowano technicznie pola A/B/C, ale NIE przeprowadzono prawdziwej recenzji ADR.\n",
            encoding="utf-8",
        )
        approvals.append({
            "id": row["id"], "content_sha256": content_sha256(row),
            "reviewer": row["reviewer"], "checked_at": row["checked_at"], "evidence_path": location,
        })
    return records, approvals


class ReleaseGateTests(unittest.TestCase):
    def test_valid_synthetic_evidence_can_export_all_modules(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root)
            output, errors = eligible(rows, approvals, root)
            self.assertEqual(errors, [])
            self.assertEqual(len(output), 39)
            self.assertEqual(len({q["module_id"] for q in output}), 13)

    def test_modified_correct_answer_invalidates_approval(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root)
            rows[0]["correct_option"] = "B"
            output, errors = eligible(rows, approvals, root)
            self.assertEqual(len(output), 39)
            self.assertTrue(any("reviewed content hash mismatch" in x for x in errors))

    def test_modified_explanation_invalidates_approval(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root)
            rows[0]["explanation"] = "Zmodyfikowano objaśnienie po akceptacji, co blokuje wydanie."
            _, errors = eligible(rows, approvals, root)
            self.assertTrue(any("hash mismatch" in x for x in errors))

    def test_lost_evidence_file_blocks_release(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root)
            (root / approvals[0]["evidence_path"]).unlink()
            _, errors = eligible(rows, approvals, root)
            self.assertTrue(any("review evidence missing" in x for x in errors))

    def test_unapproved_verified_question_is_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root)
            _, errors = eligible(rows, approvals[:-1], root)
            self.assertTrue(any("without independent approval" in x for x in errors))

    def test_pending_items_excluded_and_stale_approval_denied(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root)
            rows[0]["verification_status"] = "needs_review"
            rows[0]["checked_at"] = None
            rows[0]["reviewer"] = None
            output, errors = eligible(rows, approvals, root)
            self.assertEqual(len(output), 38)
            self.assertTrue(any("not verified" in x for x in errors))

    def test_minimum_and_module_coverage_are_both_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root, n=13)
            output, errors = eligible(rows, approvals, root)
            self.assertEqual(len(output), 13)
            self.assertTrue(any("at least 30" in x for x in errors))
            # 30 records confined to 1 module cannot satisfy basic syllabus
            rows, approvals = fixtures(root, n=30)
            for row, approval in zip(rows, approvals):
                row["module_id"] = "ADR-B-01"
                approval["content_sha256"] = content_sha256(row)
            _, errors = eligible(rows, approvals, root)
            self.assertTrue(any("missing ADR basic modules" in x for x in errors))

    def test_no_output_when_release_not_eligible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root, n=3)
            q = root / "questions.jsonl"
            ap = root / "approvals.jsonl"
            out = root / "output.jsonl"
            q.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in rows), encoding="utf-8")
            ap.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in approvals), encoding="utf-8")
            result = main(["--questions", str(q), "--approvals", str(ap), "--root", str(root), "--output", str(out)])
            self.assertEqual(result, 1)
            self.assertFalse(out.exists())

    def test_successful_export_writes_only_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows, approvals = fixtures(root, n=39)
            rows.append({**fixture_record(100), "verification_status": "needs_review", "reviewer": None, "checked_at": None})
            q = root / "questions.jsonl"
            ap = root / "approvals.jsonl"
            out = root / "export.jsonl"
            q.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in rows), encoding="utf-8")
            ap.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in approvals), encoding="utf-8")
            result = main(["--questions", str(q), "--approvals", str(ap), "--root", str(root), "--output", str(out)])
            self.assertEqual(result, 0)
            exported = load_jsonl(out)
            self.assertEqual(len(exported), 39)
            self.assertTrue(all(x["verification_status"] == "verified" for x in exported))


if __name__ == "__main__":
    unittest.main()
