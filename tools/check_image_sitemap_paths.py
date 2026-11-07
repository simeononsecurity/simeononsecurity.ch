"""Verify local image-sitemap URLs resolve after one normal HTTP path decode.

Usage: python3 tools/check_image_sitemap_paths.py /path/to/hugo/output
The XML is generated locally by Hugo, not fetched from an untrusted URL.
"""

import argparse
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
IMAGE_NS = "http://www.google.com/schemas/sitemap-image/1.1"


def audit(output_dir: Path) -> tuple[list[str], int, int]:
    """Return (missing/unsafe local URLs, checked local count, skipped remote count)."""
    output_dir = output_dir.resolve()
    # A production Hugo build is the sole XML input; no user-supplied XML is parsed.
    root = ET.parse(output_dir / "imagessitemap.xml").getroot()
    page = root.find(f"{{{SITEMAP_NS}}}url/{{{SITEMAP_NS}}}loc")
    if page is None or not page.text:
        return ["image sitemap has no page URL to identify its site host"], 0, 0
    site_host = urlsplit(page.text).netloc
    if not site_host:
        return ["image sitemap page URL has no site host"], 0, 0
    errors: list[str] = []
    checked = skipped_remote = 0
    for image in root.iter(f"{{{IMAGE_NS}}}loc"):
        url = (image.text or "").strip()
        parsed = urlsplit(url)
        if parsed.netloc != site_host:
            skipped_remote += 1
            continue
        checked += 1
        if parsed.scheme != "https" or not parsed.path.startswith("/"):
            errors.append(f"invalid local image URL: {url}")
            continue
        # Browsers and ordinary static servers decode percent escapes before opening a
        # file. Testing the literal '%20' filename would miss broken public URLs.
        target = (output_dir / unquote(parsed.path).lstrip("/")).resolve()
        if not target.is_relative_to(output_dir) or not target.is_file():
            errors.append(f"missing decoded image target: {url}")
    return errors, checked, skipped_remote


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path, help="Hugo destination directory")
    args = parser.parse_args()
    try:
        errors, checked, skipped = audit(args.output_dir)
    except (OSError, ET.ParseError) as exc:
        print(f"could not read local Hugo image sitemap: {exc}", file=sys.stderr)
        return 1
    print(f"local images checked: {checked}; remote URLs skipped: {skipped}; failures: {len(errors)}")
    for error in errors:
        print(error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
