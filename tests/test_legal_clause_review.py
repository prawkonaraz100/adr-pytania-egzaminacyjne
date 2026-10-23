import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from check_legal_clause_review import validate, SNAPSHOT_FIELDS


class LegalClauseReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        (self.root/"podstawowy").mkdir()
        (self.root/"review"/"legal-clauses").mkdir(parents=True)
        self.question={
            "id":"ADR-B-0001","module_id":"ADR-B-01","stem":"Przykładowe pytanie testowe?",
            "options":{"A":"Pierwszy wariant","B":"Drugi wariant","C":"Trzeci wariant"},
            "correct_option":"B","explanation":"Tylko mechaniczna treść testowa.",
            "sources":[{"reference":"1.3.2","url":"https://example.org"}],
            "legal_basis_version":"ADR-2025-PL","image":None,"verification_status":"needs_review"
        }
        self.entry={
            "id":"ADR-B-0001","order":1,"clause":"1.3.2",
            "source_2025_comparison_url":"https://example.org/adr",
            "answer_review":{
                "A":{"expected_correct":False,"rationale":"Wariant A nie jest poprawny w tej fikcyjnej sytuacji."},
                "B":{"expected_correct":True,"rationale":"Wariant B jest kluczem do fikcyjnego pytania."},
                "C":{"expected_correct":False,"rationale":"Wariant C jest fałszywy w fikcyjnym przykładzie."}
            },
            "observed_answer_key":"B",
            "notes_on_conditions":"Syntetyczny warunek zastosowania, bez prawnego potwierdzenia.",
            "official_polish_full_text_comparison":"pending",
            "independent_specialist_approval":"pending",
            "final_verification_status":"needs_review",
            "question_snapshot":{k:copy.deepcopy(self.question.get(k)) for k in SNAPSHOT_FIELDS}
        }
        self.save()

    def tearDown(self):
        self.tmp.cleanup()

    def save(self):
        (self.root/"podstawowy"/"questions.jsonl").write_text(
            json.dumps(self.question,ensure_ascii=False)+"\n",encoding="utf-8")
        (self.root/"review"/"legal-clauses"/"001-001.json").write_text(
            json.dumps({"release_approved":False,"records":[self.entry]},ensure_ascii=False),encoding="utf-8")

    def test_synthetic_complete_rationales(self):
        self.assertEqual(validate(self.root,expected=1)[0],[])

    def test_changed_key_requires_fresh_review(self):
        self.question["correct_option"]="A"
        self.save()
        errs,_=validate(self.root,expected=1)
        self.assertTrue(any("stale" in e or "key mismatch" in e for e in errs))

    def test_changed_wrong_answer_invalidates_snapshot(self):
        self.question["options"]["C"]="Nowy, niezatwierdzony wariant"
        self.save()
        errs,_=validate(self.root,expected=1)
        self.assertTrue(any("stale" in e for e in errs))

    def test_missing_option_review_is_rejected(self):
        del self.entry["answer_review"]["C"]
        self.save()
        errs,_=validate(self.root,expected=1)
        self.assertTrue(any("option C" in e for e in errs))

    def test_fake_expert_approval_is_rejected(self):
        self.entry["independent_specialist_approval"]="approved"
        self.save()
        errs,_=validate(self.root,expected=1)
        self.assertTrue(any("unsupported specialist approval" in e for e in errs))


if __name__=="__main__":
    unittest.main()
