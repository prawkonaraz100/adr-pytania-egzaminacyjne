import json,subprocess,sys,tempfile,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"scripts"))
from draft_mock_exam import draw_exam,load_bank
class DraftExamTests(unittest.TestCase):
 def test_sample_ids_exist_and_key_matches(self):
  bank=load_bank(ROOT/"podstawowy"/"questions.jsonl");ids={q["id"] for q in bank}
  e=json.loads((ROOT/"podstawowy"/"egzamin-probny"/"wariant-001.json").read_text(encoding="utf-8"));k=json.loads((ROOT/"podstawowy"/"egzamin-probny"/"klucz-001.json").read_text(encoding="utf-8"))
  qids=[q["id"] for q in e["questions"]]
  self.assertEqual(len(qids),30);self.assertEqual(len(set(qids)),30);self.assertTrue(set(qids)<=ids)
  self.assertEqual(qids,[a["id"] for a in k["answers"]]);self.assertEqual(e["module_distribution"],dict(sorted(Counter(q["module_id"] for q in e["questions"]).items())))
  self.assertEqual(e["pass_mark_correct"],20);self.assertFalse(e["publication_authorized"]);self.assertFalse(k["publication_authorized"])
 def test_seed_reproducible_and_all_modules_present(self):
  rows=load_bank(ROOT/"podstawowy"/"questions.jsonl");a,ak=draw_exam(rows,1234);b,bk=draw_exam(rows,1234)
  self.assertEqual(a,b);self.assertEqual(ak,bk);self.assertEqual(len(a["questions"]),30);self.assertEqual(len(a["module_distribution"]),13)
 def test_cli_writes_separate_exam_and_key(self):
  with tempfile.TemporaryDirectory() as td:
   e,k=Path(td)/"e.json",Path(td)/"k.json";p=subprocess.run([sys.executable,str(ROOT/"scripts"/"draft_mock_exam.py"),"--seed","99","--output",str(e),"--key-output",str(k)],capture_output=True,text=True)
   self.assertEqual(p.returncode,0,p.stdout+p.stderr);self.assertEqual(len(json.loads(e.read_text())["questions"]),30);self.assertEqual(len(json.loads(k.read_text())["answers"]),30)
if __name__=="__main__":unittest.main()
