"""Temporary official Dz.U. page-header source probe; remove before merge."""
import io, re, sys, subprocess, unittest, urllib.request, hashlib
URLS={n:f"https://eli.gov.pl/api/acts/DU/2025/642/text/O/D20250642-{n:02d}.pdf" for n in (3,38,53,54)}
CLAUSES=("1.4.2.3.2","8.4.1","5.2.1.1","5.2.2.1.1","5.3.2.2.1","5.3.2.2.2","5.3.2.3.1","5.4.3.4")
class Probe(unittest.TestCase):
 def test_official_pdf_clauses(self):
  try: from pypdf import PdfReader
  except ImportError:
   r=subprocess.run([sys.executable,"-m","pip","install","-q","pypdf"],capture_output=True,text=True,timeout=80)
   if r.returncode:print("PAGEPROBE_PIP_FAIL",r.stderr[-200:]);return
   from pypdf import PdfReader
  for n,url in URLS.items():
   try:
    with urllib.request.urlopen(url, timeout=25) as r:
     raw=r.read()
     print("PAGEPROBE_DOWNLOAD",n,"bytes",len(raw),"sha",hashlib.sha256(raw).hexdigest()[:16],"contentlength",r.headers.get("content-length"))
    if not raw.startswith(b"%PDF"):print("PAGEPROBE_NOTPDF",n);continue
    reader=PdfReader(io.BytesIO(raw));print("PAGEPROBE_PDF",n,"pages",len(reader.pages),"FIRST"," ".join((reader.pages[0].extract_text() or "")[:250].split()),"LAST"," ".join((reader.pages[-1].extract_text() or "")[:250].split()))
    for idx,p in enumerate(reader.pages):
     txt=p.extract_text() or ""
     found=[c for c in CLAUSES if re.search(r"(?m)^"+re.escape(c)+r"\s",txt)]
     if found:
      head=" ".join(txt[:240].split())
      for c in found:
       at=re.search(r"(?m)^"+re.escape(c)+r"\s",txt)
       print("PAGEPROBE_CLAUSE",n,idx,c,"HEAD",head,"SNIP"," ".join(txt[at.start():at.start()+1000].split())[:820])
   except Exception as exc:print("PAGEPROBE_ERROR",n,type(exc).__name__,str(exc)[:220])
