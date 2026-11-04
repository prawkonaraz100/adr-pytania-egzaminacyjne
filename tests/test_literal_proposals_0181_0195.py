"""Validate approved second-pass batch 13 corrections against the live bank."""
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BANK=ROOT/"podstawowy/questions.jsonl"
PATCHES=ROOT/"review/literal-pl/POPRAWKI-KONTROLA2-0181-0195.jsonl"
REPORT=ROOT/"review/literal-pl/PARTIA-0181-0195.json"
EXPECTED={f"ADR-B-{n:04d}" for n in range(181,196)}

def read_jsonl(path):
 return [json.loads(s) for s in path.read_text(encoding="utf-8").splitlines() if s.strip()]

class SecondBatch13Tests(unittest.TestCase):
 def test_all_15_records_applied_exactly(self):
  bank={r["id"]:r for r in read_jsonl(BANK)}
  records=read_jsonl(PATCHES)
  self.assertEqual(len(bank),780)
  self.assertEqual({r["id"] for r in records},EXPECTED)
  for r in records:
   self.assertEqual(r,bank[r["id"]])
   self.assertEqual(r["verification_status"],"needs_review")
   self.assertIsNone(r["checked_at"])
   self.assertIsNone(r["reviewer"])
  self.assertTrue(all(q["verification_status"]=="needs_review" for q in bank.values()))
  self.assertTrue(all(q["checked_at"] is None and q["reviewer"] is None for q in bank.values()))
 def test_report(self):
  o=json.loads(REPORT.read_text(encoding="utf-8"))
  self.assertEqual(o["counts"],{"OK":2,"POPRAW":13,"BLOKUJ":0})
  self.assertEqual(o["remaining_without_comparison"],558)
  self.assertEqual(len(o["records"]),15)
  self.assertEqual({r["id"] for r in o["records"]},EXPECTED)
  self.assertEqual({r["id"] for r in o["records"] if r["verdict"]=="OK"},{"ADR-B-0187","ADR-B-0195"})
  self.assertEqual(next(r["page"] for r in o["records"] if r["id"]=="ADR-B-0194"),959)

if __name__=="__main__":
 unittest.main()
