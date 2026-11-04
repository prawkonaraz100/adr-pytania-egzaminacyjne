"""Temporary official Dz.U. clause-to-header verification; delete before merge."""
import io,re,sys,subprocess,unittest,urllib.request
TARGETS={
 2:{"1.4.2.3.2":range(3,10)},
 19:{"5.2.1.1":range(30,39),"5.2.2.1.1":range(35,43)},
 20:{"5.3.2.2.1":range(1,9),"5.3.2.3.1":range(3,10),"5.4.3.4":range(20,28)},
 27:{"8.4.1":range(28,37)}
}
class OfficialHeaderCheck(unittest.TestCase):
 def test_extract_exact_headers(self):
  try:from pypdf import PdfReader
  except ImportError:
   p=subprocess.run([sys.executable,"-m","pip","install","-q","pypdf"],capture_output=True,text=True,timeout=90)
   if p.returncode:self.fail("install pypdf error")
   from pypdf import PdfReader
  for part,clauses in TARGETS.items():
   url=f"https://www.dziennikustaw.gov.pl/DU/2025/642/D20250000642{part:02d}.pdf"
   with urllib.request.urlopen(url,timeout=30) as response:raw=response.read()
   rdr=PdfReader(io.BytesIO(raw))
   print("HEADER_SOURCE",part,len(rdr.pages))
   for clause,indices in clauses.items():
    matches=[]
    for ix in indices:
     if ix>=len(rdr.pages):continue
     s=rdr.pages[ix].extract_text() or ""
     header=" ".join(s[:85].split())
     found=clause in s
     print("HEADER_PAGE",part,ix,clause,found,header)
     if found:
      pos=s.find(clause)
      matches.append((ix,header," ".join(s[pos:pos+350].split())))
    for ix,header,snip in matches:print("HEADER_MATCH",clause,ix,header,"QUOTE",snip[:320])
    self.assertTrue(matches,f"Not found {clause} part {part}")
