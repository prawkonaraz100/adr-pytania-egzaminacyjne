import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_sequential_audit import validate, SNAPSHOT_FIELDS


class SequentialAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "podstawowy").mkdir()
        (self.root / "review" / "sequential").mkdir(parents=True)
        self.questions = []
        self.rows = []
        for number in range(1, 3):
            obj = {"id": f"ADR-B-{number:04d}", "stem": f"Pytanie numer {number}?",
                   "module_id": "ADR-B-01", "options": {"A": "Poprawna", "B": "Fałsz", "C": "Nieprawda"},
                   "correct_option": "A", "explanation": "Przykładowe wyjaśnienie",
                   "sources": [{"reference": "1.3.1"}], "legal_basis_version": "ADR-2025-PL",
                   "image": None, "verification_status": "needs_review"}
            self.questions.append(obj)
            self.rows.append({"id": obj["id"], "sequence": number,
                "exact_record_snapshot": json.loads(json.dumps({key: obj.get(key) for key in SNAPSHOT_FIELDS})),
                "editorial_read_through": {key: True for key in
                    ("stem","option_A","option_B","option_C","correct_option","explanation","reference_pointer")},
                "question_status": "needs_review", "polish_official_text_fully_compared": False,
                "independent_ADR_expert_approved": False,
                "review_outcome": "editorial_first_pass_only_not_legally_approved",
                "expert_review_priority": "standard_expert_review",
                "source_crosscheck_scope": "reference_listed_without_individual_full_clause_comparison",
                "supplementary_source_url": None})
        self.write()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self):
        (self.root / "podstawowy" / "questions.jsonl").write_text(
            "".join(json.dumps(x, ensure_ascii=False)+"\n" for x in self.questions), encoding="utf-8")
        (self.root / "review" / "sequential" / "001-002.json").write_text(
            json.dumps({"not_a_release_approval": True,
                        "status": "pending_full_official_polish_clause_and_independent_expert_review",
                        "records": self.rows}, ensure_ascii=False), encoding="utf-8")

    def test_two_records_pass_structural_review(self):
        errors, stats = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(stats["audit_records"], 2)

    def test_a_question_edit_invalidates_earlier_audit(self):
        self.questions[0]["options"]["A"] = "Zmieniona odpowiedź"
        self.write()
        errors, _ = validate(self.root)
        self.assertTrue(any("stale audit snapshot" in x for x in errors))

    def test_review_cannot_fake_expert_approval(self):
        self.rows[1]["independent_ADR_expert_approved"] = True
        self.write()
        errors, _ = validate(self.root)
        self.assertTrue(any("unperformed" in x for x in errors))

    def test_missing_row_is_rejected(self):
        self.rows.pop()
        self.write()
        errors, _ = validate(self.root)
        self.assertTrue(any("audit covers 1 vs bank 2" in x for x in errors))


if __name__ == "__main__":
    unittest.main()
