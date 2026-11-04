"""Temporary official Dz.U. header crosscheck for batch 13; remove before merge."""
import io,re,subprocess,sys,unittest,urllib.request
PAGES={2:[(6,57,"1.4.2.3.2")],19:[(34,935,"5.2.1.1"),(38,939,"5.2.2.1.1")],20:[(4,955,"5.3.2.2.1"),(5,956,"5.3.2.3.1"),(6,957,"5.3.2.3.2"),(24,975,"INSTRUKCJE PISEMNE")],27:[(32,1333,"8.4.1")]}
class OfficialHeaderCheck(unittest.TestCase):
 def test_original_publication_headers(self):
  try:from pypdf import PdfReader
  except ImportError:
   p=subprocess.run([sys.executable,"-m","pip","install","-q","pypdf"],capture_output=True,text=True,timeout=90)
   if p.returncode:self.fail("pypdf install failed: "+p.stderr[-400:])
   from pypdf import PdfReader
  for part,items in PAGES.items():
   url=f"https://www.dziennikustaw.gov.pl/DU/2025/642/D20250000642{part:02d}.pdf"
   with urllib.request.urlopen(url,timeout=30) as response:raw=response.read()
   reader=PdfReader(io.BytesIO(raw))
   print("HEADER_SOURCE",part,"pages",len(reader.pages),"bytes",len(raw))
   for index,official_page,needle in items:
    txt=reader.pages[index].extract_text() or ""
    header=" ".join(txt[:150].split())
    print("HEADER_CHECK",part,index,official_page,"ACTUAL",header,"MATCH",needle in txt)
    self.assertIn("Dziennik Ustaw",txt[:200])
    self.assertRegex(txt[:200],r"(?<!\d)"+str(official_page)+r"(?!\d)")
    self.assertIn(needle,txt)
    p=txt.find(needle)
    print("HEADER_QUOTE",official_page,needle," ".join(txt[p:p+420].split())[:400])
