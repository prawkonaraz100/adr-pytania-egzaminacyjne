"""First literal review of ADR-B-0301–0315; questions.jsonl must remain unchanged."""
import hashlib
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
class Partia21LiteralReview(unittest.TestCase):
    def test_report_scope_and_verdicts(self):
        d = json.loads((ROOT / "review/literal-pl/PARTIA-0301-0315.json").read_text(encoding="utf-8"))
        self.assertEqual(d["bank_count"], 780)
        self.assertEqual(d["counts"], {"OK": 0, "POPRAW": 15, "BLOKUJ": 0})
        self.assertEqual((d["previous_uncompared"], d["remaining_without_comparison"]), (453, 438))
        self.assertEqual(len(d["records"]), 15)
    def test_bank_blob_and_question_records_unchanged(self):
        raw = BANK.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        self.assertIn(blob, {"ba829d36bc7e1c04aeab108d826bfae33938422f", "f732aa354f959e2ba17bf870d901d2fe51aa0426", "e0c671756644994d18480feae5c08bc70ee0ffbd", "ff06e555f833fa3f679c7c145c1223395ae923db"})
        rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 780)
        for q in rows:
            if 301 <= int(q["id"][-4:]) <= 315:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
if __name__ == "__main__":
    unittest.main()
