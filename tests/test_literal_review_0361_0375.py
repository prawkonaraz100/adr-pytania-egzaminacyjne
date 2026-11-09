"""First literal review of ADR-B-0361–0375; questions.jsonl must remain unchanged."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0361-0375.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0361-0375.json"
EXPECTED_BANK_SHA = "129d09039ee7fbee90198049cb3d733368070c77"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(361, 376)]

class Partia25LiteralReview(unittest.TestCase):
    def test_report_scope_and_verdicts(self):
        self.assertTrue(REPORT.is_file())
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["bank_count"], 780)
        self.assertEqual(data["bank_blob_sha"], EXPECTED_BANK_SHA)
        self.assertFalse(data["bank_changed"])
        self.assertEqual(data["previous_uncompared"], 420)
        self.assertEqual(data["remaining_without_comparison"], 405)
        self.assertEqual(data["counts"], {"OK": 4, "POPRAW": 11, "BLOKUJ": 0})
        self.assertEqual(len(data["records"]), 15)
        self.assertEqual([row["id"] for row in data["records"]], EXPECTED_IDS)

    def test_bank_blob_and_question_records_unchanged(self):
        raw = BANK.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\\0" + raw).hexdigest()
        self.assertEqual(blob, EXPECTED_BANK_SHA)
        rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 780)
        for q in rows:
            if 361 <= int(q["id"][-4:]) <= 375:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
        self.assertEqual(sum(q["verification_status"] == "verified" for q in rows), 0)

if __name__ == "__main__":
    unittest.main()
