"""Temporary diagnostic to obtain literal Polish ADR 2025 quotations for batch 12.
The source is the 2025 Polish PDF mirror; not a legal authorization or test of approval.
This diagnostic MUST be removed before merge.
"""
import pathlib
import re
import subprocess
import tempfile
import sys
import unittest
import urllib.request

URL = "https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8"
CLAUSES = ["5.4.3.4", "8.1.4.5", "8.1.5.2", "8.1.5.3",
           "5.3.2.3.1", "7.5.1.5", "7.3.1.1", "8.6.3.1",
           "8.1.2.1", "8.1.4.4", "7.5.8.1", "5.4.1.1.3.1"]

class SourceProbe(unittest.TestCase):
    def test_print_source_clauses(self):
        try:
            with urllib.request.urlopen(URL, timeout=20) as r:
                pdf = r.read(12000000)
            print("SOURCE_PROBE_DOWNLOAD",len(pdf))
            if not pdf.startswith(b"%PDF"):
                return
            with tempfile.TemporaryDirectory() as directory:
                p=pathlib.Path(directory)/"adr.pdf"
                p.write_bytes(pdf)
                try:
                    from pypdf import PdfReader
                except ImportError:
                    install=subprocess.run([sys.executable,"-m","pip","install","--quiet","pypdf"],capture_output=True,text=True,timeout=90)
                    print("SOURCE_PROBE_PIP",install.returncode,install.stderr[-300:])
                    if install.returncode: return
                    from pypdf import PdfReader
                reader=PdfReader(str(p))
                pages=[""] * len(reader.pages)
                for ix in [262,263,268,280,281,282,283,597,598,611,615,616,630,631,644]:
                    pages[ix]=reader.pages[ix].extract_text(extraction_mode="layout") or ""
            print("SOURCE_PROBE_PAGE_COUNT",len(pages))
            for idx in [262,263,268,280,281,282,283,597,598,611,615,616,630,631,644]:
                content=" ".join(pages[idx].split())
                print(f"SOURCE_PROBE_PAGE_DETAIL PDF_PAGE {idx+1} TEXT {content[:3400]}")
            for term in CLAUSES:
                found=0
                for number,page in enumerate(pages):
                    # first true section, not reference in the table of contents
                    expr=r"(?m)^\s*"+re.escape(term)+r"\s"
                    match=re.search(expr,page)
                    if not match or number<10:
                        continue
                    piece=" ".join(page[match.start():match.start()+1100].split())
                    print(f"SOURCE_PROBE_CLAUSE {term} PDF_PAGE {number+1} TEXT {piece}")
                    found+=1
                    if found>=2:break
                if not found:print("SOURCE_PROBE_NOT_FOUND",term)
        except Exception as exc:
            print("SOURCE_PROBE_UNAVAILABLE",type(exc).__name__,str(exc)[:350])

if __name__ == "__main__":
    unittest.main()
