"""First-pass literal review for ADR-B-0526–0540; report-only; after the second pass the bank has the expected SHA."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0526-0540.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0526-0540.json"
FIRST_PASS_BANK_SHA = "e0c671756644994d18480feae5c08bc70ee0ffbd"
EXPECTED_BANK_SHA = "6147aeb45bf0efd1631ae17ce5e1d82357bffb0b"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(526, 541)]
EXPECTED_PAGES = {
    "ADR-B-0526": [693],
    "ADR-B-0527": [693],
    "ADR-B-0528": [693],
    "ADR-B-0529": [54],
    "ADR-B-0530": [962],
    "ADR-B-0531": [964],
    "ADR-B-0532": [964],
    "ADR-B-0533": [971],
    "ADR-B-0534": [688],
    "ADR-B-0535": [688],
    "ADR-B-0536": [962],
    "ADR-B-0537": [962],
    "ADR-B-0538": [972],
    "ADR-B-0539": [1338, 1339],
    "ADR-B-0540": [688, 689, 1338],
}
EXPECTED_COUNTS = {"OK": 3, "POPRAW": 12, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


class Partia36LiteralReview(unittest.TestCase):
    def test_report_scope_counts_and_printed_page_headers(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0526–0540")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 255)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 240)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual({row["id"]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES)
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] and row["gazette_pages"] for row in manifest["records"]))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)

    def test_bank_after_second_pass_keeps_780_records_unverified(self):
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

    def test_duplicate_search_scope_and_counts(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 1)
        self.assertEqual(len(manifest["duplicate_search"]["threshold_0_25_candidates"]), 1)

    def test_second_pass_artifacts_and_bank_sha(self):
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0526-0540.jsonl"
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0526-0540.md"
        self.assertTrue(second_pass.is_file())
        self.assertTrue(corrections.is_file())
        records = [json.loads(line) for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual([row["id"] for row in records], EXPECTED_IDS)
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)


if __name__ == "__main__":
    unittest.main()
