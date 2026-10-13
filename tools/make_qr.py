"""Regenerate the QR codes that point at the live site.

Usage:
    pip install segno
    python tools/make_qr.py [url]

Writes assets/qr.svg (for the page) and assets/qr.png (for slides and posters).
"""
import sys
from pathlib import Path

import segno

DEFAULT_URL = "https://faerber-lab.github.io/projects/babeldojo/"
INK = "#0E1726"
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def write_qr(url, out_dir):
    """Write qr.svg and qr.png for `url` into `out_dir`; return the QR object."""
    out_dir = Path(out_dir)
    qr = segno.make(url, error="q")
    qr.save(str(out_dir / "qr.svg"), omitsize=True, border=3, dark=INK, light="#ffffff", xmldecl=False, svgns=True, nl=False)
    qr.save(str(out_dir / "qr.png"), scale=24, border=4, dark=INK, light="#ffffff")
    return qr


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    qr = write_qr(url, ASSETS)
    print(f"QR v{qr.version} ({qr.error}) -> {url}")
