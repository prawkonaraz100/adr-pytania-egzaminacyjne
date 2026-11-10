"""First-pass literal review for ADR-B-0541–0555; report-only; after the second pass the bank has the expected SHA."""
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BANK=ROOT/"podstawowy"/"questions.jsonl"
REPORT=ROOT/"review"/"literal-pl"/"PARTIA-0541-0555.md"
MANIFEST=ROOT/"review"/"literal-pl"/"PARTIA-0541-0555.json"
FIRST_PASS_BANK_SHA="73aa25f2ae5fed6f40b1948dfb917f082c08b58e"
EXPECTED_BANK_SHA="7f2be64ba60fef44ab136bdf59cbb4bdd949c172"
EXPECTED_IDS=[f"ADR-B-{i:04d}" for i in range(541,556)]
EXPECTED_PAGES={
    "ADR-B-0541": [154, 942, 945],
    "ADR-B-0542": [942, 945, 165],
    "ADR-B-0543": [
        956
    ],
    "ADR-B-0544": [
        956
    ],
    "ADR-B-0545": [
        956
    ],
    "ADR-B-0546": [
        950,
        951
    ],
    "ADR-B-0547": [
        950,
        951
    ],
    "ADR-B-0548": [
        951
    ],
    "ADR-B-0549": [952, 953],
    "ADR-B-0550": [
        950,
        951
    ],
    "ADR-B-0551": [
        1324,
        1344
    ],
    "ADR-B-0552": [
        1344
    ],
    "ADR-B-0553": [
        1344
    ],
    "ADR-B-0554": [
        1304
    ],
    "ADR-B-0555": [
        1304
    ]
}
EXPECTED_COUNTS={"OK":7,"POPRAW":8,"BLOKUJ":0}
def git_blob_sha(data): return hashlib.sha1(b"blob "+str(len(data)).encode("ascii")+b"\0"+data).hexdigest()
class Partia37LiteralReview(unittest.TestCase):
 def test_report_and_bank_after_second_pass(self):
  m=json.loads(MANIFEST.read_text(encoding="utf-8"))
  self.assertEqual(m["bank_blob_sha"],FIRST_PASS_BANK_SHA); self.assertFalse(m["bank_changed"])
  self.assertEqual(m["previous_uncompared"],240); self.assertEqual(m["remaining_without_comparison"],225)
  self.assertEqual(m["counts"],EXPECTED_COUNTS); self.assertEqual([r["id"] for r in m["records"]],EXPECTED_IDS)
  self.assertEqual({r["id"]:r["gazette_pages"] for r in m["records"]},EXPECTED_PAGES); self.assertTrue(REPORT.is_file())
  raw=BANK.read_bytes(); self.assertEqual(git_blob_sha(raw),EXPECTED_BANK_SHA)
  q=[json.loads(x) for x in raw.decode("utf-8").splitlines() if x.strip()]
  self.assertEqual(len(q),780); by={x["id"]:x for x in q}
  for id in EXPECTED_IDS: self.assertEqual(by[id]["verification_status"],"needs_review"); self.assertIsNone(by[id]["checked_at"]); self.assertIsNone(by[id]["reviewer"])
  self.assertEqual(sum(x["verification_status"]=="verified" for x in q),0)
 def test_second_pass_artifacts_and_bank_sha(self):
  corrections=ROOT/"review"/"literal-pl"/"POPRAWKI-KONTROLA2-0541-0555.jsonl"
  second_pass=ROOT/"review"/"literal-pl"/"KONTROLA2-PARTIA-0541-0555.md"
  self.assertTrue(second_pass.is_file())
  lines=[json.loads(x) for x in corrections.read_text(encoding="utf-8").splitlines() if x.strip()]
  self.assertEqual(len(lines),15); self.assertEqual([x["id"] for x in lines],EXPECTED_IDS)
  self.assertEqual(git_blob_sha(BANK.read_bytes()),EXPECTED_BANK_SHA)
if __name__=="__main__": unittest.main()
