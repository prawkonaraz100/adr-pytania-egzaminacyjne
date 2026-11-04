import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TestLiteralPartia18(unittest.TestCase):
 def test_report(self):
  d=json.loads((ROOT/'review/literal-pl/PARTIA-0256-0270.json').read_text(encoding='utf-8'))
  self.assertEqual(d['counts'],{'OK':4,'POPRAW':11,'BLOKUJ':0})
  self.assertEqual((d['previous_uncompared'],d['remaining_without_comparison']),(498,483))
  self.assertEqual(len(d['records']),15)
 def test_bank_untouched(self):
  qs=[json.loads(x) for x in (ROOT/'podstawowy/questions.jsonl').read_text(encoding='utf-8').splitlines() if x]
  self.assertEqual(len(qs),780)
  for q in qs:
   if 256<=int(q['id'][-4:])<=270:self.assertEqual(q['verification_status'],'needs_review')
if __name__=='__main__':unittest.main()
