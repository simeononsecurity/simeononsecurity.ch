#!/usr/bin/env python3
"""
fix_ad_permalink_idiom.py - After convert_images_to_webp.py + rewrite_webp_
references.py update `resources.Get "img/ads/.../file.EXT"` calls to point at
the new .webp file, the paired idiom

    {{ $Xsrc := resources.Get "path/file.webp" }}
    {{ $Xsrcpermalink := replace $Xsrc.RelPermalink ".OLDEXT" "" }}

still strips the OLD extension (.png/.jpg/.jpeg), which no longer matches
since RelPermalink now ends in .webp. Left alone, $Xsrcpermalink keeps the
".webp" suffix and the later printf "%s_%dx%d.%s" ... "webp" call produces a
double-extension filename like "file.webp_255x255.webp".

This script finds every `resources.Get "....webp"` line whose very next
`replace $VAR.RelPermalink "....EXT" ""` uses a non-webp EXT, and rewrites
that EXT to "webp" so the strip actually matches.

Usage:
    .venv/bin/python3 tools/fix_ad_permalink_idiom.py --dry-run
    .venv/bin/python3 tools/fix_ad_permalink_idiom.py
"""

import argparse
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRUNE_DIRS = {"node_modules", "public", ".git", ".venv", "resources", "__pycache__"}

GET_RE = re.compile(
    r'(\{\{\s*\$(\w+)\s*:=\s*resources\.Get\s*"([^"]+\.webp)"\s*\}\}\s*\n[ \t]*)'
    r'(\{\{\s*\$\2permalink\s*:=\s*replace\s*\$\2\.RelPermalink\s*")(\.\w+)("\s*""\s*\}\})'
)
# Groups: 1=first-line, 2=varname, 3=webp-path, 4=replace-opening,
#         5=old-extension, 6=replace-closing


def fix_file(path, dry_run):
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()

    def repl(m):
        old_ext = m.group(5)
        if old_ext == ".webp":
            return m.group(0)
        return m.group(1) + m.group(4) + ".webp" + m.group(6)

    new_content = GET_RE.sub(repl, content)
    if new_content != content:
        if not dry_run:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_content)
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    changed = 0
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in PRUNE_DIRS]
        for f in files:
            if not f.endswith(".html"):
                continue
            path = os.path.join(root, f)
            if fix_file(path, args.dry_run):
                changed += 1
                print(f"  {'WOULD FIX' if args.dry_run else 'FIXED'}  {os.path.relpath(path, BASE)}")
    print(f"\n--- {changed} files {'would be' if args.dry_run else ''} fixed ---")


if __name__ == "__main__":
    main()
