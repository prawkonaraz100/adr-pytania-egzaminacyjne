"""First-pass literal review for ADR-B-0496–0510; report-only; after the second pass the bank has the expected SHA."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0496-0510.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0496-0510.json"
FIRST_PASS_BANK_SHA = "f2cea3f46167e3f99d4c5c7b91658744eba1d8c7"
EXPECTED_BANK_SHA = "6dc2b850f70d300ef3c214708b3283933934301c"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(496, 511)]
EXPECTED_PAGES = {
    "ADR-B-0496": "129",
    "ADR-B-0497": "129",
    "ADR-B-0498": "129",
    "ADR-B-0499": "275",
    "ADR-B-0500": "275",
    "ADR-B-0501": "275",
    "ADR-B-0502": "275",
    "ADR-B-0503": "957",
    "ADR-B-0504": "957",
    "ADR-B-0505": "957",
    "ADR-B-0506": "957",
    "ADR-B-0507": "956",
    "ADR-B-0508": "962",
    "ADR-B-0509": "1325",
    "ADR-B-0510": "187",
}
EXPECTED_PAGES_ALL = {
    "ADR-B-0496": [129],
    "ADR-B-0497": [129],
    "ADR-B-0498": [129],
    "ADR-B-0499": [275],
    "ADR-B-0500": [275],
    "ADR-B-0501": [275],
    "ADR-B-0502": [275],
    "ADR-B-0503": [957],
    "ADR-B-0504": [957],
    "ADR-B-0505": [957],
    "ADR-B-0506": [957],
    "ADR-B-0507": [956],
    "ADR-B-0508": [962],
    "ADR-B-0509": [1325],
    "ADR-B-0510": [187],
}
EXPECTED_COUNTS = {"OK": 4, "POPRAW": 11, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


class Partia34LiteralReview(unittest.TestCase):
    def test_report_scope_counts_and_printed_page_headers(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0496–0510")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 285)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 270)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual({row["id"]: str(row["gazette_page"]) for row in manifest["records"]}, EXPECTED_PAGES)
        self.assertEqual({row["id"]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES_ALL)
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)

    def test_bank_has_expected_sha_after_second_pass_and_batch_remains_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        self.assertTrue(set(EXPECTED_IDS).issubset(by_id))
        for question_id in EXPECTED_IDS:
            row = by_id[question_id]
            self.assertEqual(row["verification_status"], "needs_review")
            self.assertIsNone(row["checked_at"])
            self.assertIsNone(row["reviewer"])
        self.assertEqual(sum(row["verification_status"] == "verified" for row in questions), 0)


    def test_second_pass_artifacts_and_bank_sha(self):
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0496-0510.md"
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0496-0510.jsonl"
        self.assertTrue(second_pass.is_file())
        self.assertTrue(corrections.is_file())
        records = [json.loads(line) for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual([row["id"] for row in records], EXPECTED_IDS)
        self.assertEqual(len(records), 15)
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)

    def test_literal_quotes_and_similarity_review_are_present(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] and row["gazette_pages"] for row in manifest["records"]))
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 2)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 17)
        self.assertEqual(len(manifest["duplicate_search"]["threshold_0_25_candidates"]), 17)
        self.assertTrue(all(row["proposed_replacement"] is None for row in manifest["records"]))

    def test_no_question_bank_or_exam_files_are_changed_by_report(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertEqual(len(manifest["records"]), 15)


if __name__ == "__main__":
    unittest.main()
