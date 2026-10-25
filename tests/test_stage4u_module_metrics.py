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
  strict_by_module={}
  for module,records in by_module.items():
   longest=sum(len(q["options"][q["correct_option"]])>max(len(v) for k,v in q["options"].items() if k!=q["correct_option"]) for q in records)
   strict_by_module[module]=(longest,len(records))
   self.assertLessEqual(100*longest/len(records),18.0,f"{module}: {longest}/{len(records)}")
  # Stage 4x20 regression target: B-01 and B-04 must stay at or below 14%.
  for module in ("ADR-B-01","ADR-B-04"):
   longest,total=strict_by_module[module]
   self.assertLessEqual(100*longest/total,14.0,f"{module}: {longest}/{total}; target <=14%")
if __name__=="__main__": unittest.main()
