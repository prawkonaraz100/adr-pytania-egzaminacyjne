"""First-pass literal review report for ADR-B-0421–0435; bank must remain unchanged."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0421-0435.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0421-0435.json"
FIRST_PASS_BANK_SHA = "025066373056366cfff08ee01a6a5394c7c90218"
EXPECTED_BANK_SHA = "025066373056366cfff08ee01a6a5394c7c90218"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(421, 436)]


class Partia29LiteralReview(unittest.TestCase):
    def test_report_scope_and_verdicts(self):
        self.assertTrue(REPORT.is_file())
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["bank_count"], 780)
        self.assertEqual(data["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(data["bank_changed"])
        self.assertEqual(data["previous_uncompared"], 360)
        self.assertEqual(data["remaining_without_comparison"], 345)
        self.assertEqual(data["counts"], {"OK": 1, "POPRAW": 14, "BLOKUJ": 0})
        self.assertEqual(len(data["records"]), 15)
        self.assertEqual([row["id"] for row in data["records"]], EXPECTED_IDS)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in data["records"]))
        for row in data["records"]:
            if row["proposed_replacement"] is not None:
                self.assertEqual(row["proposed_replacement"]["correct_option"], row["original_correct_option"])

    def test_bank_remains_unchanged_after_first_pass(self):
        """The first-pass report must not alter the question bank."""
        raw = BANK.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        self.assertEqual(blob, EXPECTED_BANK_SHA)
        rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 780)
        for q in rows:
            if 421 <= int(q["id"][-4:]) <= 435:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
        self.assertEqual(sum(q["verification_status"] == "verified" for q in rows), 0)


if __name__ == "__main__":
    unittest.main()
