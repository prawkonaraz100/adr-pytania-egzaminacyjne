"""Temporary text probe on Polish ADR 2025 volume II; remove before merge."""
import io, re, subprocess, sys, unittest, urllib.request
URL="https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8"
CLAUSES=("5.2.1.1","5.2.2.1.1","5.3.2.2.1","5.3.2.2.2","5.3.2.3.1","5.3.2.3.2","8.4.1")
class Probe(unittest.TestCase):
 def test_extract_clauses(self):
  try:from pypdf import PdfReader
  except ImportError:
   r=subprocess.run([sys.executable,"-m","pip","install","-q","pypdf"],capture_output=True,text=True,timeout=90)
   if r.returncode:print("SOURCE13_PIPFAIL",r.stderr[-300:]);return
   from pypdf import PdfReader
  with urllib.request.urlopen(URL,timeout=30) as resp: pdf=resp.read()
  reader=PdfReader(io.BytesIO(pdf))
  print("SOURCE13_VOLUMEII",len(reader.pages))
  for idx in [241,242,243,244,245,246,247,248,249,259,260,261,262,263,639,640,641,642,643]:
   if idx>=len(reader.pages):continue
   s=reader.pages[idx].extract_text(extraction_mode="layout") or ""
   head=" ".join(s[:130].split());tail=" ".join(s[-95:].split())
   print("SOURCE13_PAGE",idx,"HEAD",head,"TAIL",tail)
   for clause in CLAUSES:
    match=re.search(r"(?m)^\s*"+re.escape(clause)+r"\s",s)
    if match:print("SOURCE13_CLAUSE",idx,clause,"QUOTE"," ".join(s[match.start():match.start()+1150].split())[:950])
