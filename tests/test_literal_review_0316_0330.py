"""Regression gate for the second literal-review pass, ADR-B-0316–0330."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0316-0330.md"
CORRECTIONS = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0316-0330.jsonl"
EXPECTED_BANK_SHA = "e0c671756644994d18480feae5c08bc70ee0ffbd"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in list(range(316, 319)) + list(range(320, 331))]

class LiteralReview0316To0330Tests(unittest.TestCase):
    def test_report_and_correction_manifest_exist(self):
        self.assertTrue(REPORT.is_file())
        self.assertTrue(CORRECTIONS.is_file())

    def test_correction_manifest_has_exact_14_ids_and_preserves_review_state(self):
        rows = [json.loads(line) for line in CORRECTIONS.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual([row["id"] for row in rows], EXPECTED_IDS)
        for row in rows:
            self.assertEqual(row["verification_status"], "needs_review")
            self.assertIsNone(row["checked_at"])
            self.assertIsNone(row["reviewer"])

    def test_bank_blob_matches_expected_sha(self):
        raw = BANK.read_bytes()
        digest = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
        self.assertEqual(digest, EXPECTED_BANK_SHA)

    def test_corrected_records_match_manifest_without_changing_keys_or_status(self):
        bank = {row["id"]: row for row in (json.loads(line) for line in BANK.read_text(encoding="utf-8").splitlines() if line.strip())}
        corrections = [json.loads(line) for line in CORRECTIONS.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(bank), 780)
        self.assertTrue(all(q["verification_status"] == "needs_review" for q in bank.values()))
        for patch in corrections:
            with self.subTest(id=patch["id"]):
                self.assertEqual(bank[patch["id"]], patch)

if __name__ == "__main__":
    unittest.main()
