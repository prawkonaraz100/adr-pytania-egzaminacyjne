"""Literal review tests for ADR-B-0661–0675; first-pass report plus second-pass deployment checks."""

import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
REPORT = ROOT / "review" / "literal-pl" / "PARTIA-0661-0675.md"
MANIFEST = ROOT / "review" / "literal-pl" / "PARTIA-0661-0675.json"
FIRST_PASS_BANK_SHA = "835ba93341ece797cd831d85defa4d147da0942e"
EXPECTED_BANK_SHA = "ff06e555f833fa3f679c7c145c1223395ae923db"
EXPECTED_IDS = [f"ADR-B-{i:04d}" for i in range(661, 676)]
EXPECTED_PAGES = {
    "ADR-B-0661": [
        176,
        1285,
        1286
    ],
    "ADR-B-0662": [
        1344,
        1345
    ],
    "ADR-B-0663": [
        1332
    ],
    "ADR-B-0664": [
        1332,
        1353
    ],
    "ADR-B-0665": [
        182,
        183
    ],
    "ADR-B-0666": [
        191
    ],
    "ADR-B-0667": [
        1285,
        1286
    ],
    "ADR-B-0668": [
        229,
        641,
        820
    ],
    "ADR-B-0669": [
        931,
        932
    ],
    "ADR-B-0670": [
        214,
        975
    ],
    "ADR-B-0671": [
        854,
        855
    ],
    "ADR-B-0672": [
        110
    ],
    "ADR-B-0673": [
        274,
        611
    ],
    "ADR-B-0674": [
        188
    ],
    "ADR-B-0675": [
        188
    ]
}
ABSOLUTE = re.compile(r"\b(tylko|zawsze|każdy|każda|każde|każdej|wszystkie|wyłącznie|żaden|żadnych|nigdy|całkowicie|automatycznie|niezależnie)\b", re.IGNORECASE)


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


class Partia45LiteralReview(unittest.TestCase):
    def test_report_scope_counts_pages_and_quotes(self):
        self.assertTrue(REPORT.is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["scope"], "first_pass_literal_review")
        self.assertEqual(manifest["batch"], "ADR-B-0661–0675")
        self.assertEqual(manifest["bank_count"], 780)
        self.assertEqual(manifest["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(manifest["bank_changed"])
        self.assertEqual(manifest["previous_uncompared"], 120)
        self.assertEqual(manifest["compared"], 15)
        self.assertEqual(manifest["remaining_without_comparison"], 105)
        counts = Counter(row["verdict"] for row in manifest["records"])
        computed = {key: counts.get(key, 0) for key in ("OK", "POPRAW", "BLOKUJ")}
        self.assertEqual(computed, manifest["counts"])
        self.assertEqual([row["id"] for row in manifest["records"]], EXPECTED_IDS)
        self.assertEqual({row["id"]: row["gazette_pages"] for row in manifest["records"]}, EXPECTED_PAGES)
        self.assertTrue(all(row["exact_quote"] and row["legal_basis"] for row in manifest["records"]))
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in manifest["records"]))
        self.assertEqual(manifest["verified"], 0)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_45_pairs"], 7)
        self.assertEqual(manifest["duplicate_search"]["threshold_0_25_pairs"], 159)

    def test_every_popraw_has_same_competency_valid_replacement(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        bank = [json.loads(line) for line in BANK.read_text(encoding="utf-8").splitlines() if line.strip()]
        by_id = {q["id"]: q for q in bank}
        for row in manifest["records"]:
            if row["verdict"] != "POPRAW":
                continue
            replacement = row.get("proposed_replacement")
            self.assertIsInstance(replacement, dict)
            original = by_id[row["id"]]
            self.assertEqual(replacement["module_id"], original["module_id"])
            self.assertEqual(replacement["competency_id"], row["competency_id"])
            self.assertEqual(replacement["correct_option"], original["correct_option"])
            self.assertEqual(row["original_correct_option"], original["correct_option"])
            self.assertTrue(replacement["stem"].strip())
            self.assertEqual(set(replacement["options"]), {"A", "B", "C"})
            lengths = {key: len(value) for key, value in replacement["options"].items()}
            for option in replacement["options"].values():
                self.assertLessEqual(len(option), 80)
                self.assertNotIn(";", option)
                self.assertFalse(option.endswith("."))
                self.assertIsNone(ABSOLUTE.search(option))
            correct_length = lengths[original["correct_option"]]
            self.assertFalse(correct_length == max(lengths.values()) and list(lengths.values()).count(correct_length) == 1)
            self.assertFalse(correct_length == min(lengths.values()) and list(lengths.values()).count(correct_length) == 1)
            explanation = replacement["explanation"]
            self.assertGreaterEqual(len(explanation), 300)
            self.assertTrue(explanation.endswith("."))
            self.assertIn("Podstawa: ADR ", explanation)
            sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ])", explanation.strip())
            self.assertGreaterEqual(len(sentences), 2)
            self.assertLessEqual(len(sentences), 5)
            for sentence in sentences:
                words = re.findall(r"\b[\wĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9]+\b", sentence)
                self.assertLessEqual(len(words), 35)
            self.assertTrue(replacement["sources"])
            self.assertTrue(replacement["replacement_quote"])
            self.assertTrue(replacement["replacement_pages"])

    def test_bank_after_second_pass_and_batch_stays_unverified(self):
        raw = BANK.read_bytes()
        self.assertEqual(git_blob_sha(raw), EXPECTED_BANK_SHA)
        questions = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(questions), 780)
        by_id = {row["id"]: row for row in questions}
        self.assertEqual(len(by_id), 780)
        for question_id in EXPECTED_IDS:
            self.assertEqual(by_id[question_id]["verification_status"], "needs_review")
            self.assertIsNone(by_id[question_id]["checked_at"])
            self.assertIsNone(by_id[question_id]["reviewer"])


    def test_second_pass_artifacts_and_bank_sha(self):
        corrections = ROOT / "review" / "literal-pl" / "POPRAWKI-KONTROLA2-0661-0675.jsonl"
        second_pass = ROOT / "review" / "literal-pl" / "KONTROLA2-PARTIA-0661-0675.md"
        self.assertTrue(second_pass.is_file())
        self.assertTrue(corrections.is_file())
        rows = [json.loads(line) for line in corrections.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(rows), 15)
        self.assertEqual([row["id"] for row in rows], EXPECTED_IDS)
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)

if __name__ == "__main__":
    unittest.main()
