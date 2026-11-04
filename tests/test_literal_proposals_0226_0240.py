"""First literal audit batch 16 proposals, on a copy of the ADR basic bank."""
import copy, json, re, unittest
from pathlib import Path
from scripts.check_near_duplicates import find_candidates
ROOT=Path(__file__).resolve().parents[1]
BANK=ROOT/"podstawowy/questions.jsonl"
PROPOSALS=ROOT/"review/literal-pl/POPRAWKI-0226-0240.jsonl"
REPORT=ROOT/"review/literal-pl/PARTIA-0226-0240.json"
EXPECTED={f"ADR-B-{n:04d}" for n in range(226,241)}
def load(p):return [json.loads(s) for s in p.read_text(encoding="utf-8").splitlines() if s.strip()]
class TestBatch16FirstReview(unittest.TestCase):
 def test_proposals_on_bank_copy(self):
  bank=load(BANK); proposed=load(PROPOSALS); self.assertEqual(len(bank),780)
  self.assertEqual(len(proposed),15); self.assertEqual({x["id"] for x in proposed},EXPECTED)
  old={x["id"]:x for x in bank}; simulated=copy.deepcopy(old)
  for q in proposed:
   original=old[q["id"]]; self.assertEqual(list(q),list(original))
   self.assertEqual(q["module_id"],original["module_id"])
   self.assertEqual(q["correct_option"],original["correct_option"])
   self.assertEqual(q["verification_status"],"needs_review")
   self.assertIsNone(q["checked_at"]);self.assertIsNone(q["reviewer"])
   self.assertEqual(set(q["options"]),{"A","B","C"})
   opts=list(q["options"].values());self.assertEqual(len(set(opts)),3)
   lengths=[len(x) for x in opts];self.assertLessEqual(max(lengths),80,q["id"])
   current=len(q["options"][q["correct_option"]]);unique=lengths.count(current)==1
   self.assertFalse(unique and (current==min(lengths) or current==max(lengths)),q["id"])
   explanation=q["explanation"].strip();self.assertGreaterEqual(len(explanation),300,q["id"])
   sentences=re.split(r"(?<=[.!?])\s+",explanation)
   self.assertTrue(2<=len(sentences)<=5,(q["id"],len(sentences)))
   self.assertTrue(all(len(s.split())<=35 for s in sentences),q["id"])
   self.assertRegex(explanation,r"Podstawa: ADR .+\.$")
   self.assertEqual(q["sources"][0]["reference"].replace("ADR 2025, ",""),explanation.split("Podstawa: ADR ",1)[1][:-1])
   simulated[q["id"]]=q
  self.assertEqual(len(simulated),780)
  self.assertTrue(all(x["verification_status"]=="needs_review" for x in simulated.values()))
  collisions=[]
  for score,a,b,*_ in find_candidates(list(simulated.values()),threshold=0.60):
   if a in EXPECTED or b in EXPECTED:collisions.append((a,b,round(score,3)))
  self.assertEqual(collisions,[],collisions[:10])
 def test_report(self):
  d=json.loads(REPORT.read_text(encoding="utf-8"))
  self.assertEqual(d["counts"],{"OK":0,"POPRAW":15,"BLOKUJ":0})
  self.assertEqual((d["previous_uncompared"],d["remaining_without_comparison"]),(528,513))
  self.assertEqual(len(d["records"]),15)
  self.assertEqual({x["id"] for x in d["records"]},EXPECTED)
  self.assertTrue(all(x["quote"] and x["clause"] and x["page"] for x in d["records"]))
if __name__=="__main__":unittest.main()
