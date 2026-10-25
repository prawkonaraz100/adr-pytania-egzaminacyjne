import json,subprocess,sys,tempfile,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"scripts"))
from draft_mock_exam import draw_exam,load_bank
from check_mock_exam_variants import remap_explanation
class DraftExamTests(unittest.TestCase):
 def test_sample_ids_exist_and_key_matches(self):
  bank=load_bank(ROOT/"podstawowy"/"questions.jsonl");ids={q["id"] for q in bank}
  e=json.loads((ROOT/"podstawowy"/"egzamin-probny"/"wariant-001.json").read_text(encoding="utf-8"));k=json.loads((ROOT/"podstawowy"/"egzamin-probny"/"klucz-001.json").read_text(encoding="utf-8"))
  qids=[q["id"] for q in e["questions"]]
  self.assertEqual(len(qids),30);self.assertEqual(len(set(qids)),30);self.assertTrue(set(qids)<=ids)
  self.assertEqual(qids,[a["id"] for a in k["answers"]]);self.assertEqual(e["module_distribution"],dict(sorted(Counter(q["module_id"] for q in e["questions"]).items())))
  self.assertEqual(e["pass_mark_correct"],20);self.assertFalse(e["publication_authorized"]);self.assertFalse(k["publication_authorized"])
  by_id={q["id"]:q for q in bank}
  for paper in e["questions"]:
   current=by_id[paper["id"]]
   self.assertEqual(paper["stem"],current["stem"])
   self.assertEqual(Counter(paper["options"].values()),Counter(current["options"].values()))
   mapping={old:next(new for new in "ABC" if paper["options"][new]==current["options"][old]) for old in "ABC"}
   self.assertEqual(paper["image"],current["image"])
  for answer in k["answers"]:
   current=by_id[answer["id"]];paper=next(q for q in e["questions"] if q["id"]==answer["id"])
   mapping={old:next(new for new in "ABC" if paper["options"][new]==current["options"][old]) for old in "ABC"}
   self.assertEqual(paper["options"][answer["correct_option"]],current["options"][current["correct_option"]])
   self.assertEqual(answer["explanation"],remap_explanation(current["explanation"],mapping))
 def test_checked_in_variant_matches_its_seed(self):
  rows=load_bank(ROOT/"podstawowy"/"questions.jsonl")
  exam,_=draw_exam(rows,20261024)
  checked=json.loads((ROOT/"podstawowy"/"egzamin-probny"/"wariant-001.json").read_text(encoding="utf-8"))
  self.assertEqual([q["id"] for q in exam["questions"]],[q["id"] for q in checked["questions"]])
 def test_seed_reproducible_and_all_modules_present(self):
  rows=load_bank(ROOT/"podstawowy"/"questions.jsonl");a,ak=draw_exam(rows,1234);b,bk=draw_exam(rows,1234)
  self.assertEqual(a,b);self.assertEqual(ak,bk);self.assertEqual(len(a["questions"]),30);self.assertEqual(len(a["module_distribution"]),13)
 def test_variant_002_excludes_variant_001_when_pool_allows(self):
  rows=load_bank(ROOT/"podstawowy"/"questions.jsonl")
  first=json.loads((ROOT/"podstawowy"/"egzamin-probny"/"wariant-001.json").read_text(encoding="utf-8"))
  second=json.loads((ROOT/"podstawowy"/"egzamin-probny"/"wariant-002.json").read_text(encoding="utf-8"))
  key=json.loads((ROOT/"podstawowy"/"egzamin-probny"/"klucz-002.json").read_text(encoding="utf-8"))
  first_ids={q["id"] for q in first["questions"]};second_ids=[q["id"] for q in second["questions"]]
  self.assertEqual(len(second_ids),30);self.assertEqual(len(set(second_ids)),30)
  self.assertFalse(first_ids & set(second_ids))
  self.assertEqual(second["seed"],20261025);self.assertEqual(second["variant"],2)
  self.assertEqual(second["excluded_question_ids"],sorted(first_ids))
  self.assertEqual(second_ids,[a["id"] for a in key["answers"]])
  self.assertEqual([q["id"] for q in draw_exam(rows,20261025,first_ids,2,"dac5ecc0ac3191c4db8afa5873e208a5f48bbeeb")[0]["questions"]],second_ids)
  by_id={q["id"]:q for q in rows}
  self.assertTrue(set(second_ids)<=set(by_id))
  for ans in key["answers"]:
   current=by_id[ans["id"]];paper=next(q for q in second["questions"] if q["id"]==ans["id"])
   mapping={old:next(new for new in "ABC" if paper["options"][new]==current["options"][old]) for old in "ABC"}
   self.assertEqual(paper["options"][ans["correct_option"]],current["options"][current["correct_option"]])
   self.assertEqual(ans["explanation"],remap_explanation(current["explanation"],mapping))
 def test_cli_writes_separate_exam_and_key(self):
  with tempfile.TemporaryDirectory() as td:
   e,k=Path(td)/"e.json",Path(td)/"k.json";p=subprocess.run([sys.executable,str(ROOT/"scripts"/"draft_mock_exam.py"),"--seed","99","--output",str(e),"--key-output",str(k)],capture_output=True,text=True)
   self.assertEqual(p.returncode,0,p.stdout+p.stderr);self.assertEqual(len(json.loads(e.read_text())["questions"]),30);self.assertEqual(len(json.loads(k.read_text())["answers"]),30)
if __name__=="__main__":unittest.main()
