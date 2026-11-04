"""First literal comparison, part 17; proposals are not merged into the bank."""
import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path):return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
class Partia17(unittest.TestCase):
 def test_proposal_schema_and_keys(self):
  bank={x["id"]:x for x in load(ROOT/"podstawowy/questions.jsonl")}
  proposed=load(ROOT/"review/literal-pl/POPRAWKI-0241-0255.jsonl")
  self.assertEqual(len(proposed),15)
  self.assertEqual({x["id"] for x in proposed},{f"ADR-B-{i:04d}" for i in range(241,256)})
  for q in proposed:
   base=bank[q["id"]]
   self.assertEqual(list(q),list(base));self.assertEqual(q["module_id"],base["module_id"])
   self.assertEqual(q["correct_option"],base["correct_option"])
   self.assertEqual(q["verification_status"],"needs_review")
   self.assertIsNone(q["checked_at"]);self.assertIsNone(q["reviewer"])
   opts=list(q["options"].values());self.assertEqual(len(set(opts)),3)
   L=[len(x) for x in opts];self.assertLessEqual(max(L),80,q["id"])
   k=len(q["options"][q["correct_option"]]);self.assertFalse(L.count(k)==1 and k in (min(L),max(L)),q["id"])
   e=q["explanation"];self.assertGreaterEqual(len(e),300,q["id"])
   sentences=re.split(r"(?<=[.!?])\s+",e)
   self.assertTrue(2<=len(sentences)<=5,(q["id"],len(sentences)))
   self.assertRegex(e,r"Podstawa: ADR .+\.$")
 def test_report(self):
  d=json.loads((ROOT/"review/literal-pl/PARTIA-0241-0255.json").read_text(encoding="utf-8"))
  self.assertEqual(d["counts"],{"OK":0,"POPRAW":15,"BLOKUJ":0})
  self.assertEqual((d["previous_uncompared"],d["remaining_without_comparison"]),(513,498))
  self.assertEqual(len(d["records"]),15)
if __name__=="__main__":unittest.main()
