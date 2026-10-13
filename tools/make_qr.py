"""Regenerate the QR codes that point at the live site.

Usage:
    pip install segno
    python tools/make_qr.py [url]

Writes assets/qr.svg (for the page) and assets/qr.png (for slides and posters).
"""
import sys
from pathlib import Path

import segno

URL = sys.argv[1] if len(sys.argv) > 1 else "https://himanshubeniwal.github.io/BabelDojo/"
INK = "#0E1726"
OUT = Path(__file__).resolve().parent.parent / "assets"

qr = segno.make(URL, error="q")
qr.save(str(OUT / "qr.svg"), omitsize=True, border=3, dark=INK, light="#ffffff", xmldecl=False, svgns=True, nl=False)
qr.save(str(OUT / "qr.png"), scale=24, border=4, dark=INK, light="#ffffff")
print(f"QR v{qr.version} ({qr.error}) -> {URL}")
