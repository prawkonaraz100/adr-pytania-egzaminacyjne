"""First literal review of ADR-B-0391–0405; questions.jsonl must remain unchanged."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0391-0405.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0391-0405.json"
EXPECTED_BANK_SHA = "9475e2d4f7107dc676486710ce03d626dc7473d8"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(391, 406)]

class Partia27LiteralReview(unittest.TestCase):
    def test_report_scope_and_verdicts(self):
        self.assertTrue(REPORT.is_file())
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["bank_count"], 780)
        self.assertEqual(data["bank_blob_sha"], EXPECTED_BANK_SHA)
        self.assertFalse(data["bank_changed"])
        self.assertEqual(data["previous_uncompared"], 390)
        self.assertEqual(data["remaining_without_comparison"], 375)
        self.assertEqual(data["counts"], {"OK": 0, "POPRAW": 15, "BLOKUJ": 0})
        self.assertEqual(len(data["records"]), 15)
        self.assertEqual([row["id"] for row in data["records"]], EXPECTED_IDS)

    def test_bank_blob_and_question_records_unchanged(self):
        raw = BANK.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\\0" + raw).hexdigest()
        self.assertEqual(blob, EXPECTED_BANK_SHA)
        rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 780)
        for q in rows:
            if 391 <= int(q["id"][-4:]) <= 405:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
        self.assertEqual(sum(q["verification_status"] == "verified" for q in rows), 0)

if __name__ == "__main__":
    unittest.main()
