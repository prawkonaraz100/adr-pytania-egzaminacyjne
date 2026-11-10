"""First-pass and second-pass literal review for ADR-B-0556–0570; report-only; after the second pass the bank has the expected SHA."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0556-0570.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0556-0570.json"
FIRST_PASS_BANK_SHA = "7f2be64ba60fef44ab136bdf59cbb4bdd949c172"
EXPECTED_BANK_SHA = "6147aeb45bf0efd1631ae17ce5e1d82357bffb0b"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(556, 571)]
EXPECTED_PAGES = {
    "ADR-B-0556": [1291, 1292],
    "ADR-B-0557": [312, 1291],
    "ADR-B-0558": [1291],
    "ADR-B-0559": [1291, 312],
    "ADR-B-0560": [1304],
    "ADR-B-0561": [951],
    "ADR-B-0562": [950, 952],
    "ADR-B-0563": [951, 952],
    "ADR-B-0564": [951],
    "ADR-B-0565": [954],
    "ADR-B-0566": [1344, 1324],
    "ADR-B-0567": [1327],
    "ADR-B-0568": [1327],
    "ADR-B-0569": [1327],
    "ADR-B-0570": [28],
}
EXPECTED_COUNTS = {"OK": 0, "POPRAW": 15, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


class Partia38LiteralReview(unittest.TestCase):
    def test_report_scope_counts_and_printed_page_headers(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0556–0570")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 225)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 210)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual({row["id"]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES)
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] and row["gazette_pages"] for row in manifest["records"]))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 1)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 4)

    def test_bank_after_second_pass_and_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        for question_id in EXPECTED_IDS:
            self.assertEqual(by_id[question_id]["verification_status"], "needs_review")
            self.assertIsNone(by_id[question_id]["checked_at"])
            self.assertIsNone(by_id[question_id]["reviewer"])

    def test_second_pass_artifacts_and_bank_sha(self):
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0556-0570.md"
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0556-0570.jsonl"
        self.assertTrue(second_pass.is_file())
        self.assertTrue(corrections.is_file())
        rows = [json.loads(line) for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 15)
        self.assertEqual([row["id"] for row in rows], EXPECTED_IDS)
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)


if __name__ == "__main__":
    unittest.main()
