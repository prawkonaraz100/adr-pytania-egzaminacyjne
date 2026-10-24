"""Offline tests use synthetic approved records in temporary folders only."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from mock_exam import draw_exam, run
from release_gate import content_sha256


def make_record(n):
    module = (n - 1) % 13 + 1
    return {
        "id": f"ADR-B-{n:04d}", "module_id": f"ADR-B-{module:02d}",
        "stem": f"SYNTETYCZNE PYTANIE TESTOWE {n} — nie pochodzi z banku?",
        "options": {"A":"test A", "B":"test B", "C":"test C"},
        "correct_option":"A", "explanation":("This is synthetic test-only explanatory text, not legal guidance or ADR verification. " * 3).strip(),
        "sources":[{"code":"TEST","reference":"dummy 1.1.1", "url":"https://example.org/mock"}],
        "legal_basis_version":"TEST-ONLY",
        "verification_status":"verified", "checked_at":"2026-10-22",
        "reviewer":"WYŁĄCZNIE TEST TECHNICZNY", "image":None
    }


class MockExamTests(unittest.TestCase):
    def test_draw_is_reproducible_and_has_all_modules(self):
        approved = [make_record(n) for n in range(1, 40)]
        a = draw_exam(approved, seed=8)
        b = draw_exam(approved, seed=8)
        self.assertEqual(a, b)
        self.assertEqual(len(a["questions"]), 30)
        self.assertEqual(len(set(v["id"] for v in a["questions"])), 30)
        self.assertEqual(len(set(v["module_id"] for v in a["questions"])), 13)
        self.assertFalse(a["publication_authorized"])

    def test_empty_approval_blocks_and_creates_no_file(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            questions = root / "questions.jsonl"
            approvals = root / "approvals.jsonl"
            output = root / "exam.json"
            records = [{**make_record(n), "verification_status":"needs_review",
                        "checked_at":None, "reviewer":None} for n in range(1, 40)]
            questions.write_text("".join(json.dumps(x)+"\n" for x in records), encoding="utf-8")
            approvals.write_text("", encoding="utf-8")
            self.assertEqual(run(["--questions",str(questions),"--approvals",str(approvals),
                                  "--root",str(root),"--output",str(output)]), 1)
            self.assertFalse(output.exists())

    def test_synthetic_approved_records_can_generate_offline_only(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root/"review"/"reports").mkdir(parents=True)
            records = [make_record(n) for n in range(1, 40)]
            approvals = []
            for r in records:
                filename = f"review/reports/{r['id']}.md"
                (root/filename).write_text(f"# SYNTETYCZNY TEST {r['id']}\n"+("Test only. "*30), encoding="utf-8")
                approvals.append({"id":r["id"], "content_sha256":content_sha256(r),
                    "reviewer":r["reviewer"],"checked_at":r["checked_at"],
                    "evidence_path":filename})
            qf = root/"bank.jsonl"
            ap = root/"approvals.jsonl"
            out = root/"exam.json"
            qf.write_text("".join(json.dumps(r)+"\n" for r in records), encoding="utf-8")
            ap.write_text("".join(json.dumps(a)+"\n" for a in approvals), encoding="utf-8")
            self.assertEqual(run(["--questions",str(qf),"--approvals",str(ap),
                                  "--root",str(root),"--output",str(out)]), 0)
            data = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(len(data["questions"]), 30)
            self.assertEqual(len(data["answer_key_internal_only"]), 30)
            self.assertEqual(len(data["source_bank_sha256"]), 64)
            self.assertTrue(all("image" in item for item in data["questions"]))

    def test_missing_approved_svg_blocks_export(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "review" / "reports").mkdir(parents=True)
            rows = [make_record(n) for n in range(1, 40)]
            approvals = []
            for row in rows:
                row["image"] = "assets/adr-original/missing-draft.svg"
                path = f"review/reports/{row['id']}.md"
                (root / path).write_text(f"# SYNTHETIC {row['id']}\n" + "Test only. " * 30, encoding="utf-8")
                approvals.append({"id": row["id"], "content_sha256": content_sha256(row),
                    "reviewer": row["reviewer"], "checked_at": row["checked_at"], "evidence_path": path})
            qf, af, output = root / "questions.jsonl", root / "approvals.jsonl", root / "mock.json"
            qf.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
            af.write_text("".join(json.dumps(row) + "\n" for row in approvals), encoding="utf-8")
            self.assertEqual(run(["--questions", str(qf), "--approvals", str(af),
                "--root", str(root), "--output", str(output)]), 1)
            self.assertFalse(output.exists())


if __name__=="__main__":
    unittest.main()
