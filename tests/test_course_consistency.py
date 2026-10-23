import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from course_consistency import audit


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


if __name__=="__main__":
    unittest.main()
