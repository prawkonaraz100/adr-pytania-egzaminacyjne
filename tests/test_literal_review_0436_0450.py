"""First-pass literal review checks for ADR-B-0436–0450; after the second pass the bank has the expected SHA."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0436-0450.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0436-0450.json"
FIRST_PASS_BANK_SHA = "fa4e38350731bd52c1a64a8cab934bdf18988438"
EXPECTED_BANK_SHA = "094473164719bc6a651a6e303dc117cfa6503ffb"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(436, 451)]


class Partia30LiteralReview(unittest.TestCase):
    def test_report_scope_and_verdicts(self):
        self.assertTrue(REPORT.is_file())
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["bank_count"], 780)
        self.assertEqual(data["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(data["bank_changed"])
        self.assertEqual(data["previous_uncompared"], 345)
        self.assertEqual(data["remaining_without_comparison"], 330)
        self.assertEqual(data["counts"], {"OK": 0, "POPRAW": 15, "BLOKUJ": 0})
        self.assertEqual(len(data["records"]), 15)
        self.assertEqual([row["id"] for row in data["records"]], EXPECTED_IDS)
        self.assertEqual(data["verified"], 0)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in data["records"]))

    def test_bank_has_expected_sha_after_second_pass(self):
        """After the second pass the bank has the expected SHA."""
        raw = BANK.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        self.assertEqual(blob, EXPECTED_BANK_SHA)
        rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 780)
        self.assertEqual([q["id"] for q in rows if 436 <= int(q["id"][-4:]) <= 450], EXPECTED_IDS)
        for q in rows:
            if 436 <= int(q["id"][-4:]) <= 450:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
        self.assertEqual(sum(q["verification_status"] == "verified" for q in rows), 0)


if __name__ == "__main__":
    unittest.main()
