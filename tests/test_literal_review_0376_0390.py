"""First-pass manifest is historical; after the second pass the bank has the expected SHA."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0376-0390.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0376-0390.json"
FIRST_PASS_BANK_SHA = "4e00ad8db1a63f644ab205910c434dae20669de8"
EXPECTED_BANK_SHA = "8596a7a61cdc27c4f558af7197cdca9072090c4e"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(376, 391)]

class Partia26LiteralReview(unittest.TestCase):
    def test_report_scope_and_verdicts(self):
        self.assertTrue(REPORT.is_file())
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0376-0390.md"
        patch_file = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0376-0390.jsonl"
        self.assertTrue(second_pass.is_file())
        self.assertTrue(patch_file.is_file())
        patch_rows = [json.loads(line) for line in patch_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(patch_rows), 15)
        self.assertEqual([row["id"] for row in patch_rows], EXPECTED_IDS)
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["bank_count"], 780)
        self.assertEqual(data["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(data["bank_changed"])
        self.assertEqual(data["previous_uncompared"], 405)
        self.assertEqual(data["remaining_without_comparison"], 390)
        self.assertEqual(data["counts"], {"OK": 2, "POPRAW": 13, "BLOKUJ": 0})
        self.assertEqual(len(data["records"]), 15)
        self.assertEqual([row["id"] for row in data["records"]], EXPECTED_IDS)

    def test_bank_has_expected_sha_after_second_pass(self):
        raw = BANK.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        self.assertEqual(blob, EXPECTED_BANK_SHA)
        rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 780)
        for q in rows:
            if 376 <= int(q["id"][-4:]) <= 390:
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])
        self.assertEqual(sum(q["verification_status"] == "verified" for q in rows), 0)

if __name__ == "__main__":
    unittest.main()
