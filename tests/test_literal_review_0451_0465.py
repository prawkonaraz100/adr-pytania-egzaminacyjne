"""First-pass literal review checks for ADR-B-0451–0465; the bank remains unchanged."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0451-0465.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0451-0465.json"
FIRST_PASS_BANK_SHA = "094473164719bc6a651a6e303dc117cfa6503ffb"
EXPECTED_BANK_SHA = "094473164719bc6a651a6e303dc117cfa6503ffb"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(451, 466)]


class Partia31LiteralReview(unittest.TestCase):
    def test_report_scope_and_verdicts(self):
        self.assertTrue(REPORT.is_file())
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["bank_count"], 780)
        self.assertEqual(data["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(data["bank_changed"])
        self.assertEqual(data["previous_uncompared"], 330)
        self.assertEqual(data["remaining_without_comparison"], 315)
        self.assertEqual(data["counts"], {"OK": 3, "POPRAW": 12, "BLOKUJ": 0})
        self.assertEqual(len(data["records"]), 15)
        self.assertEqual([row["id"] for row in data["records"]], EXPECTED_IDS)
        self.assertEqual(data["verified"], 0)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in data["records"]))

    def test_bank_unchanged_after_first_pass(self):
        raw = BANK.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\\0" + raw).hexdigest()
        self.assertEqual(blob, EXPECTED_BANK_SHA)
        rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 780)
        self.assertEqual([q["id"] for q in rows if 451 <= int(q["id"][-4:]) <= 465], EXPECTED_IDS)
        for q in rows:
            if 451 <= int(q["id"][-4:]) <= 465:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
        self.assertEqual(sum(q["verification_status"] == "verified" for q in rows), 0)

    def test_duplicate_replacement_is_non_tank_and_same_competency(self):
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        row = next(item for item in data["records"] if item["id"] == "ADR-B-0464")
        proposal = row["proposed_replacement"]
        self.assertIsNotNone(proposal)
        self.assertEqual(row["original_correct_option"], "C")
        self.assertEqual(proposal["correct_option"], "C")
        self.assertEqual(proposal["sources"][0]["reference"], "ADR 2025, 5.2.1.8.3")
        self.assertTrue(all(len(option) <= 80 for option in proposal["options"].values()))
        lengths = [len(option) for option in proposal["options"].values()]
        self.assertFalse(lengths.count(max(lengths)) == 1 and lengths[2] == max(lengths))
        self.assertFalse(lengths.count(min(lengths)) == 1 and lengths[2] == min(lengths))
        self.assertGreaterEqual(len(proposal["explanation"]), 300)


if __name__ == "__main__":
    unittest.main()
