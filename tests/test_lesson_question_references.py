"""Every question ID referenced by a lesson must exist in the current bank."""
import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ID_RE=re.compile(r"ADR-B-\d{4}")
class LessonQuestionReferenceTests(unittest.TestCase):
 def test_all_13_lessons_have_maps_and_existing_question_ids(self):
  bank=[json.loads(x) for x in (ROOT/"podstawowy"/"questions.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
  valid={q["id"] for q in bank}
  for n in range(1,14):
   path=ROOT/"podstawowy"/"lekcje"/f"ADR-B-{n:02d}.md"
   self.assertTrue(path.is_file(),f"missing lesson {path.name}")
   content=path.read_text(encoding="utf-8")
   self.assertIn("Mapa pytań i przykład praktyczny",content,f"{path.name}: missing question map")
   refs=set(ID_RE.findall(content))
   self.assertTrue(refs,f"{path.name}: no question IDs")
   self.assertFalse(refs-valid,f"{path.name}: unknown IDs {sorted(refs-valid)}")
if __name__=="__main__":unittest.main()
