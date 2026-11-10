"""Literal review tests for ADR-B-0646–0660; first-pass report plus second-pass deployment checks."""

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0646-0660.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0646-0660.json"
FIRST_PASS_BANK_SHA = "6dc2b850f70d300ef3c214708b3283933934301c"
EXPECTED_BANK_SHA = "ff06e555f833fa3f679c7c145c1223395ae923db"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(646, 661)]
EXPECTED_PAGES = {
    "0646": [
        1328
    ],
    "0647": [
        1325
    ],
    "0648": [
        975,
        1328
    ],
    "0649": [
        975,
        1325,
        1328
    ],
    "0650": [
        87
    ],
    "0651": [
        977
    ],
    "0652": [
        264
    ],
    "0653": [
        956,
        959
    ],
    "0654": [
        959
    ],
    "0655": [
        119,
        308
    ],
    "0656": [
        23
    ],
    "0657": [
        155
    ],
    "0658": [
        165
    ],
    "0659": [
        22,
        23
    ],
    "0660": [
        1327,
        49
    ]
}
EXPECTED_COUNTS = {"OK": 0, "POPRAW": 15, "BLOKUJ": 0}
ABSOLUTE_WORDS = re.compile(r"\b(zawsze|nigdy|wyłącznie|tylko|jedynie|każdy|żaden|żadnych|całkowicie|niezależnie|automatycznie|wszystkie)\b", re.I)

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

class Partia44LiteralReview(unittest.TestCase):
    def test_report_scope_counts_pages_quotes_and_replacements(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0646–0660")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 135)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 120)
        self.assertEqual(manifest["counts"], EXPECTED_COUNTS)
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual({row["id"].split("-")[-1]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES)
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] for row in manifest["records"]))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)
        for row in manifest["records"]:
            replacement = row.get("proposed_replacement")
            self.assertIsInstance(replacement, dict, row["id"])
            self.assertEqual(replacement["module_id"], row["module_id"])
            self.assertEqual(replacement["competency_id"], row["competency_id"])
            self.assertEqual(replacement["correct_option"], row["original_correct_option"])
            self.assertEqual(set(replacement["options"]), {"A", "B", "C"})
            lengths = {key: len(value) for key, value in replacement["options"].items()}
            self.assertLessEqual(max(lengths.values()), 80, row["id"])
            correct_len = lengths[replacement["correct_option"]]
            other_lengths = [value for key, value in lengths.items() if key != replacement["correct_option"]]
            self.assertFalse(correct_len < min(other_lengths), row["id"])
            self.assertFalse(correct_len > max(other_lengths), row["id"])
            for option in replacement["options"].values():
                self.assertIsNone(ABSOLUTE_WORDS.search(option))
            explanation = replacement["explanation"]
            self.assertGreaterEqual(len(explanation), 300, row["id"])
            sentences = re.split(r"(?<=[.!?])\s+", explanation.strip())
            self.assertGreaterEqual(len(sentences), 2)
            self.assertLessEqual(len(sentences), 5)
            for sentence in sentences:
                words = re.findall(r"\b[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+\b", sentence)
                self.assertLessEqual(len(words), 35, row["id"])
            self.assertTrue(replacement["sources"])

    def test_bank_after_second_pass_and_batch_stays_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        self.assertEqual(len(by_id), 780)
        for question_id in EXPECTED_IDS:
            self.assertEqual(by_id[question_id]["verification_status"], "needs_review")

    def test_second_pass_artifacts_and_bank_sha(self):
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0646-0660.md"
        patches = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0646-0660.jsonl"
        self.assertTrue(second_pass.is_file())
        self.assertTrue(patches.is_file())
        rows = [json.loads(line) for line in patches.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 15)
        self.assertEqual([row["id"] for row in rows], EXPECTED_IDS)
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)

if __name__ == "__main__":
    unittest.main()
