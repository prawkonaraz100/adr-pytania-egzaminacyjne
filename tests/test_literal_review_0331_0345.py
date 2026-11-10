"""Regression gate for the second literal-review pass, ADR-B-0331–0345."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
FIRST_REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0331-0345.md"
FIRST_MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0331-0345.json"
SECOND_REPORT = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0331-0345.md"
CORRECTIONS = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0331-0345.jsonl"
EXPECTED_BANK_SHA = "6dc2b850f70d300ef3c214708b3283933934301c"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(331, 346)]


class LiteralReview0331To0345Tests(unittest.TestCase):
    def test_all_review_artifacts_exist(self):
        for path in (FIRST_REPORT, FIRST_MANIFEST, SECOND_REPORT, CORRECTIONS):
            with self.subTest(path=path.name):
                self.assertTrue(path.is_file())

    def test_correction_manifest_has_exact_15_ids_and_preserves_review_state(self):
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
        self.assertEqual(sum(q["verification_status"] == "verified" for q in bank.values()), 0)
        for patch in corrections:
            with self.subTest(id=patch["id"]):
                self.assertEqual(bank[patch["id"]], patch)


if __name__ == "__main__":
    unittest.main()
