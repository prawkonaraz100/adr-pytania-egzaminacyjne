"""Kontrola pierwsza ADR-B-0736–0750 (raport) oraz kontrola druga – wdrożenie poprawek."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy/questions.jsonl"
REPORT = ROOT / "review/literal-pl/PARTIA-0736-0750.md"
MANIFEST = ROOT / "review/literal-pl/PARTIA-0736-0750.json"
COMPETENCIES = ROOT / "podstawowy/kompetencje.json"
FIRST_PASS_BANK_SHA = "5448ab43d2bed3ac17abd384b6bdc1eb596ef93f"
EXPECTED_BANK_SHA = "e2fba7594e5334356a1e5f3192987e538d58ee2c"
EXPECTED_IDS = [f"ADR-B-{n:04d}" for n in range(736, 751)]
ABSOLUTE = re.compile(r"\b(tylko|zawsze|każdy|każda|każde|każdej|wszystkie|wyłącznie|żaden|żadnych|nigdy|całkowicie|automatycznie|niezależnie)\b", re.I)

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

class Partia50LiteralReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.raw = BANK.read_bytes()
        cls.questions = [json.loads(s) for s in cls.raw.decode("utf-8").splitlines() if s.strip()]
        cls.bank = {r["id"]: r for r in cls.questions}
        matrix = json.loads(COMPETENCIES.read_text(encoding="utf-8"))
        cls.competencies = {qid:c for c in matrix["competencies"] for qid in c["question_ids"]}

    def test_first_pass_scope_and_bank_sha(self):
        self.assertTrue(REPORT.is_file())
        self.assertEqual(git_blob_sha(self.raw), EXPECTED_BANK_SHA)
        self.assertNotEqual(FIRST_PASS_BANK_SHA, EXPECTED_BANK_SHA)
        self.assertEqual(len(self.questions), 780)
        self.assertEqual(self.m["bank_blob_sha"], FIRST_PASS_BANK_SHA)
        self.assertEqual(self.m["base_commit"], "64bb28f5f1105f8825327f9696e4f570bf2c4b28")
        self.assertEqual(self.m["scope"], "first_pass_literal_review")
        self.assertEqual(self.m["batch"], "ADR-B-0736–0750")
        self.assertFalse(self.m["bank_changed"])
        self.assertEqual(self.m["bank_count"], 780)
        self.assertEqual(self.m["previous_uncompared"], 45)
        self.assertEqual(self.m["compared"], 15)
        self.assertEqual(self.m["remaining_without_comparison"], 30)
        self.assertEqual(self.m["verified"], 0)

    def test_verdicts_and_literal_citations(self):
        rows = self.m["records"]
        self.assertEqual([x["id"] for x in rows], EXPECTED_IDS)
        self.assertEqual(len(rows), 15)
        counts = Counter(x["verdict"] for x in rows)
        self.assertEqual(self.m["counts"], {key:counts.get(key,0) for key in ("OK","POPRAW","BLOKUJ")})
        self.assertEqual(self.m["counts"], {"OK":0,"POPRAW":15,"BLOKUJ":0})
        for row in rows:
            with self.subTest(id=row["id"]):
                q = self.bank[row["id"]]
                self.assertEqual(row["module_id"], q["module_id"])
                self.assertEqual(row["original_correct_option"], q["correct_option"])
                self.assertEqual(row["competency_id"], self.competencies[row["id"]]["id"])
                self.assertTrue(row["legal_basis"])
                self.assertTrue(row["exact_quote"])
                self.assertTrue(row["gazette_pages"])
                self.assertTrue(all(isinstance(x,int) and x>0 for x in row["gazette_pages"]))
                self.assertEqual(row["verification_status"], "needs_review")
                self.assertEqual(q["verification_status"], "needs_review")
                self.assertIsNone(q["checked_at"])
                self.assertIsNone(q["reviewer"])

    def test_proposed_replacements(self):
        for row in self.m["records"]:
            with self.subTest(id=row["id"]):
                p = row["proposed_replacement"]
                self.assertEqual(p["module_id"], row["module_id"])
                self.assertEqual(p["competency_id"], row["competency_id"])
                self.assertEqual(p["correct_option"], row["original_correct_option"])
                self.assertTrue(p["stem"])
                self.assertEqual(set(p["options"]), {"A","B","C"})
                lengths = {k:len(v) for k,v in p["options"].items()}
                self.assertLessEqual(max(lengths.values()), 80)
                key_length = lengths[p["correct_option"]]
                self.assertFalse(key_length == max(lengths.values()) and list(lengths.values()).count(key_length)==1)
                self.assertFalse(key_length == min(lengths.values()) and list(lengths.values()).count(key_length)==1)
                for option in p["options"].values():
                    self.assertFalse(option.endswith("."))
                    self.assertNotIn(";",option)
                    self.assertIsNone(ABSOLUTE.search(option))
                explanation=p["explanation"]
                self.assertGreaterEqual(len(explanation),300)
                self.assertLessEqual(len(explanation),500)
                self.assertRegex(explanation,r"Podstawa: ADR 2025, .+\.$")
                self.assertTrue(p["replacement_quote"])
                self.assertTrue(p["replacement_pages"])
                self.assertTrue(all(isinstance(n,int) and n>0 for n in p["replacement_pages"]))
                self.assertEqual(len(p["sources"]),1)
                self.assertEqual(p["sources"][0]["code"],"ADR-2025-PL")

if __name__ == "__main__":
    unittest.main()

    def test_second_pass_artifacts_and_bank_sha(self):
        report = ROOT / 'review/literal-pl/KONTROLA2-PARTIA-0736-0750.md'
        changes = ROOT / 'review/literal-pl/POPRAWKI-KONTROLA2-0736-0750.jsonl'
        self.assertTrue(report.is_file())
        self.assertTrue(changes.is_file())
        rows = [json.loads(line) for line in changes.read_text(encoding='utf-8').splitlines() if line.strip()]
        self.assertEqual(len(rows), 15)
        self.assertEqual([r['id'] for r in rows], EXPECTED_IDS)
        for row in rows:
            self.assertEqual(row['verification_status'], 'needs_review')
            self.assertEqual(row['correct_option'], self.bank[row['id']]['correct_option'])
            self.assertEqual(row, self.bank[row['id']])
        self.assertEqual(git_blob_sha(self.raw), EXPECTED_BANK_SHA)
