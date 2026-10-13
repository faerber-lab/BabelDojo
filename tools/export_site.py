"""Export the site as a folder that can be dropped into another website.

Written for the lab website (faerber-lab/faerber-lab.github.io), a Jekyll site
whose build runs every .css and .js file through a minifier. Files that end in
.min.css or .min.js are copied through untouched, and so are static .html
files, so the export:

  * renames the stylesheet and script to *.min.css / *.min.js (content unchanged),
  * points the canonical URL, the share link and the QR code at the new address.

Usage:
    pip install segno
    python tools/export_site.py OUT_DIR --url https://faerber-lab.github.io/projects/babeldojo/

Then copy OUT_DIR into the target repository, e.g. as projects/babeldojo/.
"""
import argparse
import re
import shutil
from pathlib import Path

from make_qr import write_qr

ROOT = Path(__file__).resolve().parent.parent
SOURCE_REPO = "https://github.com/faerber-lab/BabelDojo"
NOTE = (
    "Exported from {repo} by tools/export_site.py. Edit the source there, not this copy.\n"
    "   Not minified: the .min suffix only keeps the host site's build tools from rewriting the file."
)


def bare(url):
    """https://host/path/ -> host/path (the form shown next to the QR code)."""
    return re.sub(r"^https?://", "", url).rstrip("/")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--url", required=True, help="address the exported copy will be served from")
    args = parser.parse_args()

    new_url = args.url.rstrip("/") + "/"
    html = (ROOT / "index.html").read_text()
    css = (ROOT / "assets" / "styles.css").read_text()
    js = (ROOT / "assets" / "app.js").read_text()

    match = re.search(r'<link rel="canonical" href="([^"]+)">', html)
    if not match:
        raise SystemExit("index.html has no canonical link to read the current address from")
    old_url = match.group(1)

    def repoint(text):
        return text.replace(old_url, new_url).replace(bare(old_url), bare(new_url))

    html = repoint(html)
    js = repoint(js)
    for old, new in (("assets/styles.css", "assets/styles.min.css"), ("assets/app.js", "assets/app.min.js")):
        if old not in html:
            raise SystemExit(f"index.html does not reference {old}")
        html = html.replace(old, new)

    assets = args.out_dir / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    note = NOTE.format(repo=SOURCE_REPO)
    (args.out_dir / "index.html").write_text(html)
    (assets / "styles.min.css").write_text(f"/* {note} */\n\n{css}")
    (assets / "app.min.js").write_text(f"/* {note} */\n\n{js}")
    shutil.copy(ROOT / "assets" / "favicon.svg", assets / "favicon.svg")
    write_qr(new_url, assets)

    print(f"exported to {args.out_dir} for {new_url} (was {old_url})")


if __name__ == "__main__":
    main()
