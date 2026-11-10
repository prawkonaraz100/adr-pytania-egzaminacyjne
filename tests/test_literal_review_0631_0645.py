"""Literal review tests for ADR-B-0631–0645; first-pass report plus second-pass deployment checks."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0631-0645.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0631-0645.json"
FIRST_PASS_BANK_SHA = "8596a7a61cdc27c4f558af7197cdca9072090c4e"
EXPECTED_BANK_SHA = "6dc2b850f70d300ef3c214708b3283933934301c"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(631, 646)]
EXPECTED_PAGES = {
    "ADR-B-0631": [
        975
    ],
    "ADR-B-0632": [
        975
    ],
    "ADR-B-0633": [
        975,
        1325
    ],
    "ADR-B-0634": [
        955
    ],
    "ADR-B-0635": [
        956
    ],
    "ADR-B-0636": [
        955
    ],
    "ADR-B-0637": [
        956
    ],
    "ADR-B-0638": [
        1307
    ],
    "ADR-B-0639": [
        22
    ],
    "ADR-B-0640": [
        975
    ],
    "ADR-B-0641": [
        975
    ],
    "ADR-B-0642": [
        975
    ],
    "ADR-B-0643": [
        975
    ],
    "ADR-B-0644": [
        975
    ],
    "ADR-B-0645": [
        975
    ]
}
EXPECTED_COUNTS = {"OK": 2, "POPRAW": 13, "BLOKUJ": 0}

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

class Partia43LiteralReview(unittest.TestCase):
    def test_report_scope_counts_pages_and_quotes(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0631–0645")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 150)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 135)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual({row["id"]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES)
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] for row in manifest["records"]))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)
        for row in manifest["records"]:
            if row["verdict"] == "POPRAW":
                replacement = row.get("proposed_replacement")
                self.assertIsInstance(replacement, dict)
                self.assertEqual(replacement["competency_id"], row["competency_id"])
                self.assertEqual(replacement["correct_option"], row["original_correct_option"])
                self.assertTrue(replacement["stem"].strip())
                self.assertEqual(set(replacement["options"]), {"A", "B", "C"})
                self.assertTrue(all(replacement["options"][key].strip() for key in "ABC"))
                self.assertGreaterEqual(len(replacement["explanation"]), 300)
                self.assertTrue(replacement["sources"])

    def test_bank_after_second_pass_and_ids_stay_needs_review(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        self.assertEqual(len(by_id), 780)
        for question_id in EXPECTED_IDS:
            self.assertEqual(by_id[question_id]["verification_status"], "needs_review")


    def test_second_pass_artifacts_and_bank_sha(self):
        second_pass_report = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0631-0645.md"
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0631-0645.jsonl"
        self.assertTrue(second_pass_report.is_file())
        self.assertTrue(corrections.is_file())
        correction_rows = [json.loads(line) for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(correction_rows), 15)
        self.assertEqual([row["id"] for row in correction_rows], EXPECTED_IDS)
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)

if __name__ == "__main__":
    unittest.main()
