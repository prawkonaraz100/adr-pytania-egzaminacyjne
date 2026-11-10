"""First-pass literal review tests for ADR-B-0676–0690."""
import hashlib, json, re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BANK=ROOT/"podstawowy"/"questions.jsonl"
REPORT=ROOT/"review"/"literal-pl"/"PARTIA-0676-0690.md"
MANIFEST=ROOT/"review"/"literal-pl"/"PARTIA-0676-0690.json"
FIRST_PASS_BANK_SHA="ff06e555f833fa3f679c7c145c1223395ae923db"
EXPECTED_BANK_SHA="ff06e555f833fa3f679c7c145c1223395ae923db"
EXPECTED_IDS=[f"ADR-B-{i:04d}" for i in range(676,691)]
EXPECTED_PAGES={
    "ADR-B-0676": [
        187
    ],
    "ADR-B-0677": [
        1310
    ],
    "ADR-B-0678": [
        1332
    ],
    "ADR-B-0679": [
        56
    ],
    "ADR-B-0680": [
        963
    ],
    "ADR-B-0681": [
        1325
    ],
    "ADR-B-0682": [
        939
    ],
    "ADR-B-0683": [
        1309
    ],
    "ADR-B-0684": [
        1307
    ],
    "ADR-B-0685": [
        955
    ],
    "ADR-B-0686": [
        1325
    ],
    "ADR-B-0687": [
        975
    ],
    "ADR-B-0688": [
        940
    ],
    "ADR-B-0689": [
        928
    ],
    "ADR-B-0690": [
        1332
    ]
}
ABSOLUTE=re.compile(r"\b(tylko|zawsze|każdy|każda|każde|każdej|wszystkie|wyłącznie|żaden|żadnych|nigdy|całkowicie|automatycznie|niezależnie)\b",re.I)
def git_blob_sha(data): return hashlib.sha1(b"blob "+str(len(data)).encode("ascii")+b"\0"+data).hexdigest()
class Partia46LiteralReview(unittest.TestCase):
 def test_manifest_and_replacements(self):
  self.assertTrue(REPORT.is_file()); m=json.loads(MANIFEST.read_text(encoding="utf-8"))
  self.assertEqual(m["scope"],"first_pass_literal_review"); self.assertEqual(m["batch"],"ADR-B-0676–0690")
  self.assertEqual(m["bank_count"],780); self.assertEqual(m["bank_blob_sha"],FIRST_PASS_BANK_SHA); self.assertFalse(m["bank_changed"])
  self.assertEqual(m["previous_uncompared"],105); self.assertEqual(m["compared"],15); self.assertEqual(m["remaining_without_comparison"],90)
  self.assertEqual(m["counts"],{"OK":0,"POPRAW":15,"BLOKUJ":0}); self.assertEqual([x["id"] for x in m["records"]],EXPECTED_IDS)
  self.assertEqual({x["id"]:x["gazette_pages"] for x in m["records"]},EXPECTED_PAGES); self.assertTrue(all(x["exact_quote"] and x["legal_basis"] for x in m["records"]))
  self.assertTrue(all(x["verification_status"]=="needs_review" for x in m["records"])); self.assertEqual(m["verified"],0)
  for row in m["records"]:
   r=row["proposed_replacement"]; self.assertEqual(r["module_id"],row["module_id"]); self.assertEqual(r["competency_id"],row["competency_id"]); self.assertEqual(r["correct_option"],row["original_correct_option"])
   lens={k:len(v) for k,v in r["options"].items()}; self.assertEqual(set(lens),{"A","B","C"}); self.assertLessEqual(max(lens.values()),80)
   c=lens[r["correct_option"]]; self.assertFalse(c==min(lens.values()) and list(lens.values()).count(c)==1); self.assertFalse(c==max(lens.values()) and list(lens.values()).count(c)==1)
   for v in r["options"].values(): self.assertIsNone(ABSOLUTE.search(v)); self.assertNotIn(";",v); self.assertFalse(v.endswith("."))
   e=r["explanation"]; self.assertGreaterEqual(len(e),300); ss=re.split(r"(?<=[.!?])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ])",e.strip()); self.assertGreaterEqual(len(ss),2); self.assertLessEqual(len(ss),5)
   for s in ss: self.assertLessEqual(len(re.findall(r"\b[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+\b",s)),35)
   self.assertTrue(r["sources"]); self.assertTrue(r["replacement_quote"]); self.assertTrue(r["replacement_pages"])
 def test_bank_unchanged(self):
  raw=BANK.read_bytes(); self.assertEqual(git_blob_sha(raw),EXPECTED_BANK_SHA)
  qs=[json.loads(x) for x in raw.decode("utf-8").splitlines() if x.strip()]; self.assertEqual(len(qs),780)
  by={q["id"]:q for q in qs}; self.assertEqual(len(by),780)
  for qid in EXPECTED_IDS: self.assertEqual(by[qid]["verification_status"],"needs_review"); self.assertIsNone(by[qid]["checked_at"]); self.assertIsNone(by[qid]["reviewer"])
if __name__ == "__main__": unittest.main()
