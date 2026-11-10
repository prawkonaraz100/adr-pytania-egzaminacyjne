"""First-pass report and second-pass deployment checks for ADR-B-0586–0600."""

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0586-0600.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0586-0600.json"
FIRST_PASS_BANK_SHA = "bcac6f69bcec5dd257832774e54922c7c2c47d97"
EXPECTED_BANK_SHA = "6dc2b850f70d300ef3c214708b3283933934301c"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(586, 601)]
EXPECTED_PAGES = {
    "ADR-B-0586": [974], "ADR-B-0587": [974], "ADR-B-0588": [1324],
    "ADR-B-0589": [974], "ADR-B-0590": [974, 1324],
    "ADR-B-0591": [1338, 1339], "ADR-B-0592": [975],
    "ADR-B-0593": [975], "ADR-B-0594": [975], "ADR-B-0595": [23],
    "ADR-B-0596": [1325], "ADR-B-0597": [1325], "ADR-B-0598": [961],
    "ADR-B-0599": [962], "ADR-B-0600": [962],
}
EXPECTED_COUNTS = {"OK": 5, "POPRAW": 10, "BLOKUJ": 0}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


class Partia40LiteralReview(unittest.TestCase):
    def test_report_scope_counts_pages_and_quotes(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0586–0600")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 195)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 180)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        verdict_counts = {key: sum(row["verdict"] == key for row in manifest["records"]) for key in ("OK", "POPRAW", "BLOKUJ")}
        self.assertEqual(verdict_counts, EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual({row["id"]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES)
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] and row["gazette_pages"] for row in manifest["records"]))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 3)
        self.assertTrue(manifest["duplicate_search"]["manual_duplicate_pairs"])

    def test_bank_after_second_pass_and_records_remain_unverified(self):
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
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0586-0600.md"
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0586-0600.jsonl"
        self.assertTrue(second_pass.is_file())
        lines = [line for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(lines), 15)
        records = [json.loads(line) for line in lines]
        self.assertEqual([row["id"] for row in records], EXPECTED_IDS)
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)


if __name__ == "__main__":
    unittest.main()
