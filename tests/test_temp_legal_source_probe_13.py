"""Temporary official Dz.U. page header mapping; remove before merge."""
import io,subprocess,sys,unittest,urllib.request,re
PARTS=[2,19,20,37,38,49,50,51]
class Probe(unittest.TestCase):
 def test_map_official_pages(self):
  try:from pypdf import PdfReader
  except ImportError:
   x=subprocess.run([sys.executable,"-m","pip","install","-q","pypdf"],capture_output=True,text=True,timeout=90)
   if x.returncode:print("MAP_PIP_FAIL",x.stderr[-200:]);return
   from pypdf import PdfReader
  for n in PARTS:
   url=f"https://www.dziennikustaw.gov.pl/DU/2025/642/D20250000642{n:02d}.pdf"
   try:
    with urllib.request.urlopen(url,timeout=25) as f: raw=f.read()
    if not raw.startswith(b"%PDF"):print("MAP_NOTPDF",n,len(raw));continue
    rdr=PdfReader(io.BytesIO(raw))
    first=" ".join((rdr.pages[0].extract_text() or "")[:220].split())
    last=" ".join((rdr.pages[-1].extract_text() or "")[:220].split())
    print("MAP_PART",n,"pages",len(rdr.pages),"bytes",len(raw),"FIRST",first,"LAST",last)
    for ix,p in enumerate(rdr.pages):
     s=p.extract_text() or ""
     for clause in ["1.4.2.3.2","5.2.1.1","5.2.2.1.1","5.3.2.2.1","5.3.2.3.1","8.4.1"]:
      if re.search(r"(?m)^\s*"+re.escape(clause)+r"\s",s):
       print("MAP_MATCH",n,ix,clause,"HEADER"," ".join(s[:160].split()))
   except Exception as e:print("MAP_ERROR",n,type(e).__name__,str(e)[:180])
