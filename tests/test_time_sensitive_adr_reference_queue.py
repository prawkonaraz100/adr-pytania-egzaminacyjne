"""Regression guard for time-limited ADR multilateral agreements mentioned in course materials."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "podstawowy" / "questions.jsonl"
QUEUE = ROOT / "review" / "specialist" / "KOLEJKA-TERMINY-2026-2027.json"
LESSONS = ROOT / "podstawowy" / "lekcje"


class TimeSensitiveAgreementTests(unittest.TestCase):
    def test_m364_mentions_are_queued_and_expiry_is_explicit(self):
        bank = [json.loads(line) for line in BANK.read_text(encoding="utf-8").splitlines() if line.strip()]
        queue = json.loads(QUEUE.read_text(encoding="utf-8"))
        queue_ids = {row["id"] for row in queue["records"]}
        mentioned_ids = {
            q["id"] for q in bank
            if re.search(r"\bM364\b", " ".join([
                q.get("stem", ""),
                q.get("explanation", ""),
                " ".join(q.get("options", {}).values()),
                " ".join(s.get("reference", "") for s in q.get("sources", [])),
            ]))
        }
        self.assertEqual(mentioned_ids, queue_ids)
        self.assertEqual(queue["agreement"], "M364")
        self.assertEqual(queue["expiry_date"], "2026-12-31")
        self.assertTrue(any("gov.pl/attachment/" in s["url"] for s in queue["official_sources"]))
        self.assertTrue(any("unece.org/transport/road-transport/adr-multilateral-agreements" in s["url"] for s in queue["official_sources"]))
        self.assertFalse(queue["answer_changes_made"])
        self.assertFalse(queue["formal_approval"])
        self.assertTrue(all(row["verification_status"] == "needs_review" for row in queue["records"]))
        lesson_refs = {
            p.name for p in LESSONS.glob("ADR-B-*.md")
            if re.search(r"\bM364\b", p.read_text(encoding="utf-8"))
        }
        self.assertEqual(lesson_refs, {"ADR-B-08.md", "ADR-B-13.md"})
        self.assertEqual(set(queue["lesson_refs"]), {
            "podstawowy/lekcje/ADR-B-08.md", "podstawowy/lekcje/ADR-B-13.md"
        })


if __name__ == "__main__":
    unittest.main()
