import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_explanation_heuristics import has_explanatory_signal


class ExplanationHeuristicTests(unittest.TestCase):
    def test_accepts_expanded_causal_signals(self):
        for text in (
            "To oznacza to, że przewóz wymaga dokumentu.",
            "Towar jest niedopuszczony, więc kierowca nie może ruszyć.",
            "To inna kategoria, czyli stosuje się inną regułę.",
            "Nie wolno tego zrobić, z tego powodu trzeba przerwać czynność.",
            "Wymóg dotyczy kierowcy, natomiast nie zastępuje szkolenia.",
        ):
            with self.subTest(text=text):
                self.assertTrue(has_explanatory_signal(text))

    def test_signal_check_is_case_insensitive(self):
        self.assertTrue(has_explanatory_signal("DlAtEgO należy sprawdzić dokument."))

    def test_no_signal_is_only_a_candidate_not_a_finding(self):
        self.assertFalse(has_explanatory_signal("Dokument musi znajdować się w kabinie."))


if __name__ == "__main__":
    unittest.main()
