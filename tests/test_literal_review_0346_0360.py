"""Regression gate for first literal-review pass, ADR-B-0346–0360."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0346-0360.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0346-0360.json"
EXPECTED_BANK_SHA = "d44c95488d28507ffc3fa901d14b7d20cdd9fb38"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(346, 361)]


class LiteralReview0346To0360Tests(unittest.TestCase):
    def test_report_and_manifest_exist(self):
        self.assertTrue(REPORT.is_file())
        self.assertTrue(MANIFEST.is_file())

    def test_bank_was_not_changed_and_has_expected_sha(self):
        raw = BANK.read_bytes()
        digest = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        self.assertEqual(digest, EXPECTED_BANK_SHA)

    def test_manifest_covers_exact_batch_and_preserves_review_state(self):
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual([row["id"] for row in data["records"]], EXPECTED_IDS)
        self.assertEqual(data["counts"], {"OK": 1, "POPRAW": 14, "BLOKUJ": 0})
        self.assertEqual(data["remaining_without_comparison"], 420)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in (
            json.loads(line) for line in BANK.read_text(encoding="utf-8").splitlines() if line.strip()
        )))


if __name__ == "__main__":
    unittest.main()
