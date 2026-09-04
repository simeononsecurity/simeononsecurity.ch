#!/usr/bin/env python3
"""
rewrite_webp_references.py - After convert_images_to_webp.py has converted
raster images and written tools/_webp_conversion_map.tsv, rewrite every text
reference to the old filename so the site keeps working.

Four reference categories, each handled differently to avoid unsafe collisions:

  A. assets/img/cover/<name>.<ext>  - flat directory, one cover per article,
     basename is unique -> safe to replace by basename repo-wide (front
     matter `cover: "/img/cover/<name>.<ext>"` in every language file).

  B. assets/img/ads/**/<name>.<ext> - referenced by directory-qualified path
     in resources.Get calls and in content/advertise/index.en.md markdown
     image refs -> replace by the "img/ads/.../name.ext" relative path
     (with and without a leading slash), repo-wide. Also fixes the paired
     `replace $X.RelPermalink ".ext" ""` idiom used to derive resized
     filenames in the ad partials.

  C. static/img/<name>.<ext> (top-level loose files, e.g. banner.png,
     avatar.png) - few, uniquely named -> replace by basename in "/img/..",
     "img/..", and absolute "https://simeononsecurity.com/img/.." forms.

  D. content/**/<name>.<ext> (page-bundle inline images referenced by bare
     filename in {{< figure src="..."> }} / markdown / <img>) - basename
     collides across different bundles (e.g. installedantenna.png exists in
     three different article directories), so this category is rewritten
     ONLY within files that live in the same directory as the image.

Usage:
    .venv/bin/python3 tools/rewrite_webp_references.py --dry-run
    .venv/bin/python3 tools/rewrite_webp_references.py
"""

import argparse
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP_PATH = os.path.join(BASE, "tools", "_webp_conversion_map.tsv")

PRUNE_DIRS = {
    "node_modules", "public", ".git", ".venv", "resources",
    "__pycache__", ".pio-mcp-workspace",
}
TEXT_EXTS = (".md", ".toml", ".html", ".xml", ".json", ".js")


def load_mapping():
    entries = []
    with open(MAP_PATH, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            old_rel, new_rel = line.split("\t")
            entries.append((old_rel, new_rel))
    return entries


def all_text_files():
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in PRUNE_DIRS]
        for f in files:
            if f.lower().endswith(TEXT_EXTS):
                yield os.path.join(root, f)


def categorize(old_rel):
    parts = old_rel.split(os.sep)
    if old_rel.startswith("assets" + os.sep + "img" + os.sep + "cover" + os.sep):
        return "cover"
    if old_rel.startswith("assets" + os.sep + "img" + os.sep + "ads" + os.sep):
        return "ads"
    if old_rel.startswith("static" + os.sep + "img" + os.sep) and len(parts) == 3:
        return "static_loose"
    if old_rel.startswith("assets" + os.sep + "img" + os.sep) and len(parts) == 3:
        return "static_loose"
    if old_rel.startswith("content" + os.sep):
        return "content_bundle"
    return "other"


def build_global_replacements(entries):
    """
    For 'cover', 'ads', and 'static_loose' categories, build a global
    find -> replace map applied to every text file in the repo.
    Returns dict old_string -> new_string, longest keys first when applied.
    """
    repl = {}
    for old_rel, new_rel in entries:
        cat = categorize(old_rel)
        old_base = os.path.basename(old_rel)
        new_base = os.path.basename(new_rel)

        if cat == "cover":
            repl[f"/img/cover/{old_base}"] = f"/img/cover/{new_base}"
            repl[f"img/cover/{old_base}"] = f"img/cover/{new_base}"
        elif cat == "ads":
            old_sub = old_rel.split("assets" + os.sep, 1)[1]  # img/ads/.../file.ext
            new_sub = new_rel.split("assets" + os.sep, 1)[1]
            old_sub = old_sub.replace(os.sep, "/")
            new_sub = new_sub.replace(os.sep, "/")
            repl[old_sub] = new_sub
            repl["/" + old_sub] = "/" + new_sub
            # The paired `replace $x.RelPermalink ".ext" ""` idiom in ad
            # partials keys off extension only, no rewrite needed there
            # since resources.Get path itself is what we just replaced.
        elif cat == "static_loose":
            repl[f"/img/{old_base}"] = f"/img/{new_base}"
            repl[f"img/{old_base}"] = f"img/{new_base}"
            repl[f"https://simeononsecurity.com/img/{old_base}"] = (
                f"https://simeononsecurity.com/img/{new_base}"
            )
    return repl


def apply_global_replacements(repl, dry_run):
    """Apply the cover/ads/static_loose replacements across every text file."""
    if not repl:
        return 0
    keys_sorted = sorted(repl.keys(), key=len, reverse=True)
    changed_files = 0
    for path in all_text_files():
        try:
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
        except (UnicodeDecodeError, OSError):
            continue
        original = content
        for old in keys_sorted:
            if old in content:
                content = content.replace(old, repl[old])
        if content != original:
            changed_files += 1
            if not dry_run:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(content)
    return changed_files


URL_TOKEN_RE = re.compile(r"https?://\S+")


def safe_replace_basename(content, old_base, new_base):
    """
    Replace old_base with new_base everywhere EXCEPT inside http(s):// URLs,
    so a local page-bundle image sharing a basename with a remote-hosted
    asset (e.g. a GitHub raw URL) does not get its remote reference mangled.
    """
    pattern = re.escape(old_base)
    protected = {}

    def stash_url(m):
        key = f"\x00URLTOKEN{len(protected)}\x00"
        protected[key] = m.group(0)
        return key

    stashed = URL_TOKEN_RE.sub(stash_url, content)
    replaced = re.sub(pattern, new_base, stashed)
    for key, original in protected.items():
        replaced = replaced.replace(key, original)
    return replaced


def apply_content_bundle_replacements(entries, dry_run):
    """
    For content/** images, only rewrite references within text files that
    live in the SAME directory as the image (page bundle), since basenames
    collide across different article directories. URLs are left untouched
    (see safe_replace_basename) so remote-hosted assets sharing a basename
    with a local page-bundle image are not corrupted.
    """
    changed_files = 0
    for old_rel, new_rel in entries:
        if categorize(old_rel) != "content_bundle":
            continue
        bundle_dir = os.path.dirname(os.path.join(BASE, old_rel))
        old_base = os.path.basename(old_rel)
        new_base = os.path.basename(new_rel)
        if not os.path.isdir(bundle_dir):
            continue
        for fname in os.listdir(bundle_dir):
            if not fname.lower().endswith(TEXT_EXTS):
                continue
            fpath = os.path.join(bundle_dir, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as fh:
                    content = fh.read()
            except (UnicodeDecodeError, OSError):
                continue
            if old_base not in content:
                continue
            new_content = safe_replace_basename(content, old_base, new_base)
            if new_content != content:
                changed_files += 1
                if not dry_run:
                    with open(fpath, "w", encoding="utf-8") as fh:
                        fh.write(new_content)
    return changed_files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not os.path.exists(MAP_PATH):
        print(f"No conversion map found at {MAP_PATH}. Run convert_images_to_webp.py first.")
        return

    entries = load_mapping()
    print(f"Loaded {len(entries)} conversion entries")

    by_cat = {}
    for old_rel, _ in entries:
        by_cat.setdefault(categorize(old_rel), 0)
        by_cat[categorize(old_rel)] += 1
    print("By category:", by_cat)

    repl = build_global_replacements(entries)
    print(f"Built {len(repl)} global find/replace pairs (cover/ads/static_loose)")
    n1 = apply_global_replacements(repl, args.dry_run)
    print(f"Global pass: {n1} files {'would be' if args.dry_run else ''} changed")

    n2 = apply_content_bundle_replacements(entries, args.dry_run)
    print(f"Content-bundle pass: {n2} files {'would be' if args.dry_run else ''} changed")


if __name__ == "__main__":
    main()
