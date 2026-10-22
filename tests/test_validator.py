import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate import validate_file, validate_record


def question():
    return {
        "id": "ADR-B-0001",
        "module_id": "ADR-B-01",
        "stem": "Która odpowiedź jest prawidłowa?",
        "options": {"A": "Wariant pierwszy", "B": "Wariant drugi", "C": "Wariant trzeci"},
        "correct_option": "A",
        "explanation": "To testowy opis wyjaśnienia, a nie rzeczywista odpowiedź ADR.",
        "sources": [{
            "code": "PL-EGZAMINY",
            "reference": "§ 9 ust. 1",
            "url": "https://eli.gov.pl/api/acts/DU/2024/964/text.html"
        }],
        "legal_basis_version": "PL-2024",
        "verification_status": "draft",
        "checked_at": None,
        "reviewer": None,
        "image": None
    }


class ValidatorTests(unittest.TestCase):
    def test_valid_draft_passes(self):
        self.assertEqual(validate_record(question()), [])

    def test_wrong_number_of_choices_fails(self):
        q = question()
        del q["options"]["C"]
        self.assertTrue(any("A, B, C" in x for x in validate_record(q)))

    def test_duplicate_choices_fail(self):
        q = question()
        q["options"]["B"] = q["options"]["A"]
        self.assertTrue(any("powtarzać" in x for x in validate_record(q)))

    def test_verified_requires_review(self):
        q = question()
        q["verification_status"] = "verified"
        self.assertTrue(any("reviewer" in x for x in validate_record(q)))

    def test_verified_with_review_passes_structurally(self):
        q = question()
        q["verification_status"] = "verified"
        q["checked_at"] = "2025-12-01"
        q["reviewer"] = "ekspert-testowy"
        self.assertEqual(validate_record(q), [])

    def test_duplicate_ids_in_file_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "questions.jsonl"
            payload = json.dumps(question(), ensure_ascii=False)
            p.write_text(payload + "\n" + payload + "\n", encoding="utf-8")
            errors, _ = validate_file(p)
            self.assertTrue(any("zduplikowane id" in x for x in errors))

    def test_empty_working_dataset_passes_but_release_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "questions.jsonl"
            p.write_text("", encoding="utf-8")
            self.assertEqual(validate_file(p)[0], [])
            self.assertNotEqual(validate_file(p, release=True)[0], [])


if __name__ == "__main__":
    unittest.main()
