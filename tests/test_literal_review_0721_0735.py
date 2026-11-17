"""Literal review tests for ADR-B-0721–0735; first-pass report plus second-pass deployment checks."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
COMPETENCIES = ROOT / "podstawowy/kompetencje.json"
REPORT = ROOT / "review/literal-pl/PARTIA-0721-0735.md"
MANIFEST = ROOT / "review/literal-pl/PARTIA-0721-0735.json"
FIRST_PASS_BANK_SHA = "884f19a050315bef28c614aa0f4aae9533ed14a9"
EXPECTED_BANK_SHA = "ff19af70af76de006d2f58b1fbfed7c091d52590"
EXPECTED_IDS = [f"ADR-B-{n:04d}" for n in range(721, 736)]
ABSOLUTE = re.compile(r"\b(tylko|zawsze|każdy|każda|każde|każdej|wszystkie|wyłącznie|żaden|żadnych|nigdy|całkowicie|automatycznie|niezależnie)\b", re.I)

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

class Partia49LiteralReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.raw = BANK.read_bytes()
        cls.bank = {q["id"]: q for q in (json.loads(line) for line in cls.raw.decode("utf-8").splitlines() if line.strip())}
        matrix = json.loads(COMPETENCIES.read_text(encoding="utf-8"))
        cls.competency_by_question = {
            question_id: competency
            for competency in matrix["competencies"]
            for question_id in competency["question_ids"]
        }

    def test_scope_counts_sources_and_similarity(self):
        m = self.m
        self.assertTrue(REPORT.is_file())
        self.assertEqual(m["scope"], "first_pass_literal_review")
        self.assertEqual(m["batch"], "ADR-B-0721–0735")
        self.assertEqual(m["base_commit"], "252640f4655e8947544b45d3174638265a9ba7a2")
        self.assertEqual(m["bank_count"], 780)
        self.assertEqual(m["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertFalse(m["bank_changed"])
        self.assertEqual(m["previous_uncompared"], 60)
        self.assertEqual(m["compared"], 15)
        self.assertEqual(m["remaining_without_comparison"], 45)
        self.assertEqual(m["verified"], 0)
        self.assertEqual(m["counts"], {"OK": 0, "POPRAW": 15, "BLOKUJ": 0})
        self.assertEqual(m["similarity"]["threshold_0_45"], {"pairs_in_bank": 7, "pairs_with_batch": 0})
        self.assertEqual(m["similarity"]["threshold_0_25"], {"pairs_in_bank": 156, "pairs_with_batch": 0})
        rows = m["records"]
        self.assertEqual([r["id"] for r in rows], EXPECTED_IDS)
        self.assertEqual(len(rows), 15)
        counts = dict(Counter(r["verdict"] for r in rows))
        self.assertEqual(m["counts"], {key: counts.get(key, 0) for key in ("OK", "POPRAW", "BLOKUJ")})
        for row in rows:
            with self.subTest(id=row["id"]):
                self.assertIn(row["verdict"], ("OK", "POPRAW", "BLOKUJ"))
                self.assertTrue(row["legal_basis"])
                self.assertTrue(row["exact_quote"])
                self.assertTrue(row["gazette_pages"])
                self.assertTrue(all(isinstance(p, int) and p > 0 for p in row["gazette_pages"]))
                self.assertEqual(row["verification_status"], "needs_review")
                self.assertEqual(row["original_correct_option"], self.bank[row["id"]]["correct_option"])
                self.assertEqual(row["module_id"], self.bank[row["id"]]["module_id"])
                self.assertEqual(self.competency_by_question[row["id"]]["id"], row["competency_id"])
                self.assertEqual(row["proposed_replacement"]["module_id"], row["module_id"])
                self.assertEqual(row["proposed_replacement"]["competency_id"], row["competency_id"])

    def test_proposed_replacements(self):
        for row in self.m["records"]:
            if row["verdict"] != "POPRAW":
                continue
            with self.subTest(id=row["id"]):
                p = row["proposed_replacement"]
                self.assertIsInstance(p, dict)
                self.assertTrue(p["stem"])
                self.assertEqual(set(p["options"]), {"A", "B", "C"})
                self.assertEqual(p["correct_option"], self.bank[row["id"]]["correct_option"])
                lengths = {key: len(value) for key, value in p["options"].items()}
                self.assertLessEqual(max(lengths.values()), 80)
                key_length = lengths[p["correct_option"]]
                self.assertFalse(key_length == max(lengths.values()) and list(lengths.values()).count(key_length) == 1)
                self.assertFalse(key_length == min(lengths.values()) and list(lengths.values()).count(key_length) == 1)
                for option in p["options"].values():
                    self.assertFalse(option.endswith("."))
                    self.assertNotIn(";", option)
                    self.assertIsNone(ABSOLUTE.search(option))
                explanation = p["explanation"]
                self.assertGreaterEqual(len(explanation), 300)
                self.assertLessEqual(len(explanation), 500)
                self.assertRegex(explanation, r"Podstawa: ADR 2025, .+\.$")
                sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ])", explanation.strip())
                self.assertGreaterEqual(len(sentences), 2)
                self.assertLessEqual(len(sentences), 5)
                for sentence in sentences:
                    self.assertLessEqual(len(re.findall(r"\b[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+\b", sentence)), 35)
                self.assertTrue(p["sources"])
                self.assertTrue(all(s["code"] == "ADR-2025-PL" and s["url"] for s in p["sources"]))
                self.assertTrue(p["replacement_quote"])
                self.assertTrue(p["replacement_pages"])
                self.assertTrue(all(isinstance(page, int) and page > 0 for page in p["replacement_pages"]))

    def test_bank_after_second_pass_and_all_questions_unverified(self):
        self.assertEqual(git_blob_sha(self.raw), EXPECTED_BANK_SHA)
        self.assertNotEqual(FIRST_PASS_BANK_SHA, EXPECTED_BANK_SHA)
        self.assertEqual(len(self.bank), 780)
        for question_id in EXPECTED_IDS:
            question = self.bank[question_id]
            self.assertEqual(question["verification_status"], "needs_review")
            self.assertIsNone(question["checked_at"])
            self.assertIsNone(question["reviewer"])

    def test_second_pass_artifacts_and_bank_sha(self):
        report = ROOT / "review/literal-pl/KONTROLA2-PARTIA-0721-0735.md"
        changes = ROOT / "review/literal-pl/POPRAWKI-KONTROLA2-0721-0735.jsonl"
        self.assertTrue(report.is_file())
        self.assertTrue(changes.is_file())
        records = [json.loads(line) for line in changes.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(records), 15)
        self.assertEqual([r["id"] for r in records], EXPECTED_IDS)
        self.assertTrue(all(r["verification_status"] == "needs_review" for r in records))
        self.assertEqual(git_blob_sha(BANK.read_bytes()), EXPECTED_BANK_SHA)

if __name__ == "__main__":
    unittest.main()
