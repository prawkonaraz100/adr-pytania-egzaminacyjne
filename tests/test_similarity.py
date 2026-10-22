import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from similarity import tokens, jaccard, find_candidates


class SimilarityTests(unittest.TestCase):
    def test_polish_diacritics_are_normalized(self):
        self.assertIn("bezpieczenstwo", tokens("Bezpieczeństwo towarów"))
        self.assertEqual(tokens("żrące"), tokens("zrące"))

    def test_identical_phrasing_in_same_module_is_candidate(self):
        a = {"id": "ADR-B-0001", "module_id": "ADR-B-01", "stem": "Gdzie umieszczono wymagany numer na pomarańczowej tablicy?"}
        b = {"id": "ADR-B-0002", "module_id": "ADR-B-01", "stem": "Gdzie umieszczono wymagany numer na pomarańczowej tablicy?"}
        matches = find_candidates([a, b])
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0][0], 1.0)

    def test_different_modules_are_not_compared(self):
        a = {"id": "ADR-B-0001", "module_id": "ADR-B-01", "stem": "Gdzie umieszczono numer na tablicy?"}
        b = {"id": "ADR-B-0002", "module_id": "ADR-B-02", "stem": "Gdzie umieszczono numer na tablicy?"}
        self.assertEqual(find_candidates([a, b]), [])

    def test_score_is_symmetric(self):
        self.assertEqual(jaccard({"a", "b"}, {"b", "c"}), 1/3)
        self.assertEqual(jaccard({"b", "c"}, {"a", "b"}), 1/3)


if __name__ == "__main__":
    unittest.main()
