"""Tests for new non-blocking leakage metrics."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from answer_leakage_metrics import measure, ABSOLUTE

class LeakMetricsTests(unittest.TestCase):
    def test_absolute_matches_words_not_substrings(self):
        self.assertTrue(ABSOLUTE.search("Bez względu na masę"))
        self.assertTrue(ABSOLUTE.search("Wyłącznie dokumenty"))
        self.assertFalse(ABSOLUTE.search("dotylko"))
    def test_strict_shortest_ignores_ties(self):
        rows=[{"module_id":"ADR-B-01","correct_option":"A","options":{"A":"a","B":"ab","C":"abc"}},{"module_id":"ADR-B-01","correct_option":"A","options":{"A":"a","B":"a","C":"abc"}}]
        g=measure(rows)["ADR-B-01"]
        self.assertEqual(g["shortest"],1)
        self.assertEqual(g["questions"],2)

if __name__=="__main__": unittest.main()
