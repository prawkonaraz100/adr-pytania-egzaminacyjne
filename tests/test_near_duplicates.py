import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_near_duplicates import find_candidates, REVIEWED_PAIR_ALLOWLIST

def row(qid, module, stem, options=None):
    return {"id": qid, "module_id": module, "stem": stem,
            "options": options or {"A": "A", "B": "B", "C": "C"}}

class NearDuplicateGateTests(unittest.TestCase):
    def test_identical_stem_in_same_module_is_blocked(self):
        rows = [
            row("ADR-B-0001", "ADR-B-01", "Gdzie znajduje się numer UN na tablicy?"),
            row("ADR-B-0002", "ADR-B-01", "Gdzie znajduje się numer UN na tablicy?"),
        ]
        self.assertEqual(len(find_candidates(rows)), 1)

    def test_same_options_in_same_module_are_blocked(self):
        options = {"A": "pierwsza odpowiedź", "B": "druga odpowiedź", "C": "trzecia odpowiedź"}
        rows = [row("ADR-B-0001", "ADR-B-01", "Pytanie o załadunek", options),
                row("ADR-B-0002", "ADR-B-01", "Pytanie zupełnie inne", options)]
        self.assertEqual(len(find_candidates(rows)), 1)

    def test_different_modules_are_not_compared(self):
        rows = [row("ADR-B-0001", "ADR-B-01", "Gdzie znajduje się numer UN na tablicy?"),
                row("ADR-B-0002", "ADR-B-02", "Gdzie znajduje się numer UN na tablicy?")]
        self.assertEqual(find_candidates(rows), [])

    def test_reviewed_threshold_pair_has_documented_allowlist(self):
        self.assertIn(("ADR-B-0071", "ADR-B-0072"), REVIEWED_PAIR_ALLOWLIST)

if __name__ == "__main__":
    unittest.main()
