"""Regression gate: module-level answer-length leakage remains below 18%."""
import json
import unittest
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Stage4uModuleMetricsTests(unittest.TestCase):
 def test_each_module_below_18_percent(self):
  qs=[json.loads(line) for line in (ROOT/"podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
  by_module=defaultdict(list)
  for q in qs:
   self.assertEqual(q["verification_status"],"needs_review")
   self.assertGreaterEqual(len(q["explanation"]),300)
   by_module[q["module_id"]].append(q)
  self.assertEqual(len(by_module),13)
  for module,records in by_module.items():
   longest=sum(q["options"][q["correct_option"]].__len__()>max(len(v) for k,v in q["options"].items() if k!=q["correct_option"]) for q in records)
   self.assertLessEqual(100*longest/len(records),18.0,f"{module}: {longest}/{len(records)}")
if __name__=="__main__": unittest.main()
