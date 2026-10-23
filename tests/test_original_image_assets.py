import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class OriginalImageAssetsTests(unittest.TestCase):
    def test_all_question_image_references_exist_and_are_internal_svg(self):
        questions = [
            json.loads(line) for line in (ROOT/"podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        assigned = [q for q in questions if q.get("image")]
        self.assertGreaterEqual(len(assigned), 7)
        for question in assigned:
            path = Path(question["image"])
            self.assertEqual(path.parts[0], "assets")
            self.assertNotIn("..", path.parts)
            self.assertEqual(path.suffix, ".svg")
            self.assertTrue((ROOT/path).is_file(), question["id"])
            doc = ET.parse(ROOT/path).getroot()
            self.assertTrue(doc.tag.endswith("svg"))
            self.assertEqual(doc.attrib.get("viewBox"), "0 0 640 480")
            self.assertNotIn("<script", (ROOT/path).read_text(encoding="utf-8").lower())
            self.assertNotIn("http://", (ROOT/path).read_text(encoding="utf-8"))
            self.assertNotIn("xlink:href", (ROOT/path).read_text(encoding="utf-8"))
    
    def test_specifications_cover_all_bound_questions(self):
        specs=json.loads((ROOT/"assets/adr-original/specifications.json").read_text(encoding="utf-8"))
        records=[json.loads(s) for s in (ROOT/"podstawowy/questions.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
        matching={r["id"]:r["image"] for r in records if r.get("image")}
        self.assertEqual(len(specs["assets"]),7)
        for item in specs["assets"]:
            self.assertEqual(item["image"],matching[item["id"]])
            self.assertFalse(item["publication_ready"])
            self.assertTrue(item["needs_specialist_validation"])
            self.assertGreater(len(item["alt"]),20)


if __name__ == "__main__":
    unittest.main()
