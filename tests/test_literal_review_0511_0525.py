"""First-pass literal review for ADR-B-0511–0525; report-only, with separate first-pass and expected bank digests."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0511-0525.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0511-0525.json"
FIRST_PASS_BANK_SHA = "f732aa354f959e2ba17bf870d901d2fe51aa0426"
EXPECTED_BANK_SHA = "6147aeb45bf0efd1631ae17ce5e1d82357bffb0b"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(511, 526)]
EXPECTED_COUNTS = {"OK": 4, "POPRAW": 11, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


class Partia35LiteralReview(unittest.TestCase):
    def test_report_scope_counts_and_first_pass_bank_snapshot(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0511–0525")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 270)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 255)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)

    def test_bank_has_expected_sha_and_batch_remains_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        for question_id in EXPECTED_IDS:
            row = by_id[question_id]
            self.assertEqual(row["verification_status"], "needs_review")
            self.assertIsNone(row["checked_at"])
            self.assertIsNone(row["reviewer"])
        self.assertEqual(sum(row["verification_status"] == "verified" for row in questions), 0)

    def test_literal_quotes_pages_competencies_and_duplicates(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] and row["gazette_pages"] for row in manifest["records"]))
        self.assertTrue(all(row["competency_id"] for row in manifest["records"]))
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 0)
        duplicates = {row["id"]: row["duplicate_candidates"] for row in manifest["records"] if row["duplicate_candidates"]}
        self.assertIn("ADR-B-0119", duplicates["ADR-B-0511"])
        self.assertIn("ADR-B-0540", duplicates["ADR-B-0512"])
        self.assertIn("ADR-B-0092", duplicates["ADR-B-0513"])
        self.assertIn("ADR-B-0672", duplicates["ADR-B-0519"])

    def test_second_pass_corrections_are_registered_and_match_bank(self):
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0511-0525.jsonl"
        records = [json.loads(line) for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual([row["id"] for row in records], EXPECTED_IDS[:14])
        bank = [json.loads(line) for line in BANK.read_text(encoding="utf-8").splitlines() if line.strip()]
        by_id = {row["id"]: row for row in bank}
        for record in records:
            self.assertEqual(record, by_id[record["id"]])
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)
        self.assertEqual(len(bank), 780)
        self.assertEqual(sum(row["verification_status"] == "verified" for row in bank), 0)


if __name__ == "__main__":
    unittest.main()
