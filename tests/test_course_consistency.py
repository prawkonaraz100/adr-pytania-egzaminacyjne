import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from course_consistency import audit, validate_image_assets


class CourseConsistencyTests(unittest.TestCase):
    def test_current_repository_structure(self):
        root=Path(__file__).resolve().parents[1]
        failures,warnings=audit(root)
        self.assertEqual(failures, [])
        self.assertTrue(any("not professionally approved" in x for x in warnings))

    def test_empty_folder_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            failures,_=audit(Path(temp))
            self.assertTrue(any("Missing question bank" in x for x in failures))

    def test_missing_or_malformed_svg_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            q = [{"id": "ADR-B-1000", "image": "assets/adr-original/missing.svg"}]
            issues = validate_image_assets(root, q)
            self.assertTrue(any("missing SVG" in item for item in issues))
            file = root / q[0]["image"]
            file.parent.mkdir(parents=True)
            file.write_text("<svg><title>Test</title></svg>", encoding="utf-8")
            self.assertTrue(any("missing accessible" in item for item in validate_image_assets(root, q)))
            file.write_text("<svg><title>Test</title><desc>Sample</desc><script>bad()</script></svg>", encoding="utf-8")
            self.assertTrue(any("forbidden" in item for item in validate_image_assets(root, q)))
            file.write_text("<svg><title>Test</title><desc>Sample</desc><path d=\"M0 0\" /></svg>", encoding="utf-8")
            self.assertEqual(validate_image_assets(root, q), [])


if __name__=="__main__":
    unittest.main()
