import sys
import json
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from course_consistency import audit, validate_image_assets, validate_reviewer_manifest, validate_practical_scenario_map, validate_learning_material_links
from answer_length_bias import measure as measure_answer_length_bias


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

    def test_stale_legal_reference_and_manifest_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            specialist = root / "review" / "specialist"
            legal = root / "review" / "legal-polish"
            specialist.mkdir(parents=True)
            legal.mkdir(parents=True)
            row = {"id":"ADR-B-0001", "module_id":"ADR-B-01", "verification_status":"needs_review",
                "image":None, "sources":[{"reference":"ADR 2025, 1.3.2"}]}
            manifest = {"question_count":1, "last_id":"ADR-B-0001",
                "status_counts":{"needs_review":1,"verified":0}, "images":[],
                "unresolved_literal_comparisons":1, "source_ledger":"review/legal-polish/ledger.json"}
            ledger = {"entries":[{"id":"ADR-B-0001","module_id":"ADR-B-01",
                "source_references":["ADR 2025, 1.3.2"],
                "verification_status":"needs_review",
                "official_polish_pdf_exact_section_access":"not_retrieved_not_literally_compared"}]}
            mf=specialist/"PAKIET-0001-MANIFEST.json"
            lf=legal/"ledger.json"
            mf.write_text(json.dumps(manifest),encoding="utf-8")
            lf.write_text(json.dumps(ledger),encoding="utf-8")
            self.assertEqual(validate_reviewer_manifest(root, [row]), [])
            ledger["entries"][0]["source_references"]=["ADR 2025, 9.9.9"]
            lf.write_text(json.dumps(ledger),encoding="utf-8")
            self.assertTrue(any("Stale legal ledger clause" in err
                for err in validate_reviewer_manifest(root, [row])))
            ledger["entries"][0]["source_references"]=["ADR 2025, 1.3.2"]
            lf.write_text(json.dumps(ledger),encoding="utf-8")
            manifest["unresolved_literal_comparisons"]=0
            mf.write_text(json.dumps(manifest),encoding="utf-8")
            self.assertTrue(any("unresolved legal count" in err
                for err in validate_reviewer_manifest(root, [row])))


    def test_course_readme_matches_live_bank_and_links_all_lessons(self):
        root = Path(__file__).resolve().parents[1]
        bank = [json.loads(line) for line in
                (root / "podstawowy" / "questions.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()]
        readme = (root / "podstawowy" / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"{len(bank)} `needs_review`, 0 `verified`", readme)
        self.assertNotIn("216 rekordów", readme)
        stats = measure_answer_length_bias(bank)
        strict = sum(group["strict"] for group in stats.values())
        metric = f"{strict}/{len(bank)} = {100 * strict / len(bank):.2f}%".replace(".", ",")
        self.assertIn(metric, readme)
        for number in range(1, 14):
            module = f"ADR-B-{number:02d}"
            lesson = root / "podstawowy" / "lekcje" / f"{module}.md"
            self.assertTrue(lesson.is_file(), f"missing lesson file: {module}")
            self.assertIn(f"lekcje/{module}.md", readme)
        self.assertIn("egzamin-probny/wariant-001.json", readme)
        self.assertIn("raporty/etap-4q-przeglad-kursanta-2026-10-24.md", readme)

    def test_practical_scenario_map_has_three_scenarios_per_module_and_existing_question_ids(self):
        root = Path(__file__).resolve().parents[1]
        bank = [json.loads(line) for line in
                (root / "podstawowy" / "questions.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()]
        scenarios = json.loads((root / "podstawowy" / "praktyka" / "scenariusze-13-dzialow.json").read_text(encoding="utf-8"))["scenarios"]
        counts = {f"ADR-B-{n:02d}": 0 for n in range(1, 14)}
        for scenario in scenarios:
            counts[scenario["module_id"]] += 1
        self.assertTrue(all(count >= 3 for count in counts.values()), counts)
        self.assertEqual(validate_practical_scenario_map(root, bank), [])


    def test_lessons_and_instructor_guides_link_all_module_scenarios_and_questions(self):
        root = Path(__file__).resolve().parents[1]
        bank = [json.loads(line) for line in
                (root / "podstawowy" / "questions.jsonl").read_text(encoding="utf-8").splitlines()
                if line.strip()]
        self.assertEqual(validate_learning_material_links(root, bank), [])

    def test_practical_scenario_map_rejects_missing_question_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "podstawowy" / "praktyka"
            folder.mkdir(parents=True)
            scenarios = [
                {"id": f"SC-ADR-B-{i:02d}-{j:02d}", "module_id": f"ADR-B-{i:02d}",
                 "steps": ["1", "2", "3"], "question_ids": ["ADR-B-9999"],
                 "safety_boundary": "simulation only"}
                for i in range(1, 14) for j in range(1, 4)
            ]
            (folder / "scenariusze-13-dzialow.json").write_text(
                json.dumps({"scenarios": scenarios}), encoding="utf-8")
            bank = [{"id": f"ADR-B-{i:04d}", "module_id": f"ADR-B-{i:02d}"}
                    for i in range(1, 14)]
            errors = validate_practical_scenario_map(root, bank)
            self.assertTrue(any("missing question" in err for err in errors))

if __name__=="__main__":
    unittest.main()
