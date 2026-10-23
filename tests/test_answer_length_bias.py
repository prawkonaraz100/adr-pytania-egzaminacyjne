import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from answer_length_bias import check

def rec(module,answers,key):
    return {"module_id":module,"options":dict(zip("ABC",answers)),"correct_option":key}

class BiasMetricTests(unittest.TestCase):
    def test_strict_longest_excludes_ties(self):
        rows=[rec("ADR-B-01",["short","longest","mid"],"B"),
              rec("ADR-B-01",["same","same","tiny"],"A"),
              rec("ADR-B-01",["tiny","large","longer"],"A")]
        groups,n,den,over,mods=check(rows,.40)
        self.assertEqual((n,den),(1,3))
        self.assertEqual(groups["ADR-B-01"]["tied"],1)
        self.assertFalse(over)
        self.assertFalse(mods)
    def test_threshold_rejects_imbalanced_module(self):
        rows=[rec("ADR-B-01",["short","much longer","mid"],"B"),
              rec("ADR-B-01",["short","much longer","mid"],"B"),
              rec("ADR-B-02",["much longer","mid","tiny"],"C")]
        _,n,den,over,modules=check(rows,.40)
        self.assertEqual((n,den),(2,3))
        self.assertTrue(over)
        self.assertEqual(modules,["ADR-B-01"])
