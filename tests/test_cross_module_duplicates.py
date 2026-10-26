import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_cross_module_duplicates import find_candidates, normalize


def row(qid, module, stem, options=None):
    return {"id": qid, "module_id": module, "stem": stem,
            "options": options or {"A": "Wariant A", "B": "Wariant B", "C": "Wariant C"}}


class CrossModuleDuplicateTests(unittest.TestCase):
    def test_identical_stem_across_modules_is_blocked(self):
        rows = [
            row("ADR-B-0001", "ADR-B-01", "Gdzie znajduje się numer UN na tablicy?"),
            row("ADR-B-0002", "ADR-B-02", "Gdzie znajduje się numer UN na tablicy?"),
        ]
        self.assertEqual(len(find_candidates(rows)), 1)
        self.assertTrue(find_candidates(rows)[0]["same_stem"])

    def test_same_answer_set_across_modules_is_blocked(self):
        options = {"A": "Pierwsza opcja", "B": "Druga opcja", "C": "Trzecia opcja"}
        rows = [
            row("ADR-B-0001", "ADR-B-01", "Pytanie o nadanie przesyłki", options),
            row("ADR-B-0002", "ADR-B-02", "Pytanie o tunnelowanie", options),
        ]
        self.assertTrue(find_candidates(rows)[0]["same_options"])

    def test_near_duplicate_stems_across_modules_are_blocked(self):
        rows = [
            row("ADR-B-0001", "ADR-B-01", "Kiedy kierowca powinien sprawdzić dokument przewozowy przed wyjazdem?"),
            row("ADR-B-0002", "ADR-B-02", "Kiedy kierowca powinien sprawdzić dokument przewozowy przed rozpoczęciem jazdy?"),
        ]
        self.assertTrue(find_candidates(rows, threshold=0.75))

    def test_same_module_pairs_are_not_cross_module_duplicates(self):
        rows = [
            row("ADR-B-0001", "ADR-B-01", "Gdzie znajduje się numer UN?"),
            row("ADR-B-0002", "ADR-B-01", "Gdzie znajduje się numer UN?"),
        ]
        self.assertEqual(find_candidates(rows), [])

    def test_normalization_ignores_accents_and_case(self):
        self.assertEqual(normalize("Żółć ADR"), normalize("zolc adr"))


if __name__ == "__main__":
    unittest.main()
