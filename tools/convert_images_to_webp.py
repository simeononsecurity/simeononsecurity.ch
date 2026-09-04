#!/usr/bin/env python3
"""
convert_images_to_webp.py - Convert PNG/JPEG/JPG raster images to WebP, delete
the old raster file, and write a TSV conversion map for the reference-rewrite
script. Excludes PWA/OS icon assets (favicons, apple-touch icons, Windows
tile icons) and all GIFs, per project convention.

Usage:
    .venv/bin/python3 tools/convert_images_to_webp.py --dry-run
    .venv/bin/python3 tools/convert_images_to_webp.py
    .venv/bin/python3 tools/convert_images_to_webp.py --dir assets/img/cover
"""

import argparse
import os

from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRUNE_DIRS = {
    "node_modules", "public", ".git", ".venv", "resources", "themes",
    "__pycache__", ".pio-mcp-workspace",
}

EXCLUDED_DIRS = {
    os.path.join("static", "img", "windows11"),
    os.path.join("static", "img", "ios"),
    os.path.join("static", "img", "android"),
}
EXCLUDED_FILES = {
    os.path.join("static", "img", "favicon.png"),
    os.path.join("static", "img", "apple-touch-icon-192.png"),
    os.path.join("static", "img", "apple-touch-icon-144-precomposed.png"),
    os.path.join("static", "img", "maskable_icon.png"),
    os.path.join("static", "img", "512x512.png"),
    os.path.join("static", "img", "96x96.png"),
}

RASTER_EXTS = (".png", ".jpg", ".jpeg")
QUALITY = 85


def is_excluded(rel_path):
    for d in EXCLUDED_DIRS:
        if rel_path == d or rel_path.startswith(d + os.sep):
            return True
    if rel_path in EXCLUDED_FILES:
        return True
    return False


def find_targets(root_dir):
    """Yield relative paths (from BASE) of every convertible raster image."""
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in PRUNE_DIRS]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext not in RASTER_EXTS:
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, BASE)
            if is_excluded(rel):
                continue
            yield rel


def convert_one(rel_path, dry_run=False):
    """
    Convert rel_path (png/jpg/jpeg) to a sibling .webp file.
    Returns (webp_rel_path, old_bytes, new_bytes, deleted_stale_dup) or None.
    """
    full = os.path.join(BASE, rel_path)
    stem, _ext = os.path.splitext(full)
    webp_full = stem + ".webp"
    webp_rel = os.path.relpath(webp_full, BASE)

    old_bytes = os.path.getsize(full)

    # Collision: a .webp with the same stem already exists (leftover from a
    # prior manual conversion). Validate it before trusting it: a 0-byte or
    # otherwise corrupted pre-existing .webp (seen in the wild from failed
    # AI-generation runs) must be regenerated from the raster source instead
    # of blindly kept, or the site ships a broken image.
    if os.path.exists(webp_full):
        existing_valid = False
        if os.path.getsize(webp_full) > 0:
            try:
                probe = Image.open(webp_full)
                probe.load()
                existing_valid = True
            except Exception:
                existing_valid = False
        if existing_valid:
            if not dry_run:
                os.remove(full)
            return (webp_rel, old_bytes, os.path.getsize(webp_full), True)
        print(f"  WARN existing {webp_rel} is 0-byte/corrupted, regenerating from {rel_path}")
        # Fall through to normal conversion, overwriting the corrupted file.

    try:
        im = Image.open(full)
        im.load()
    except Exception as exc:
        print(f"  ERROR opening {rel_path}: {exc}")
        return None

    if im.mode in ("P", "LA"):
        im = im.convert("RGBA")
    elif im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")

    if dry_run:
        return (webp_rel, old_bytes, None, False)

    try:
        im.save(webp_full, "WEBP", quality=QUALITY, method=6)
    except Exception as exc:
        print(f"  ERROR saving {webp_rel}: {exc}")
        return None

    new_bytes = os.path.getsize(webp_full)
    os.remove(full)
    return (webp_rel, old_bytes, new_bytes, False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dir", default=".", help="Restrict conversion to this subdirectory (relative to repo root)")
    parser.add_argument("--dry-run", action="store_true", help="List what would be converted without writing anything")
    args = parser.parse_args()

    scan_root = os.path.join(BASE, args.dir)
    targets = sorted(find_targets(scan_root))

    print(f"Found {len(targets)} PNG/JPG/JPEG files to convert under {args.dir!r}")
    if args.dry_run:
        total = sum(os.path.getsize(os.path.join(BASE, rel)) for rel in targets)
        print(f"Total raster bytes: {total / 1024 / 1024:.1f} MB")
        for rel in targets[:50]:
            print("  ", rel)
        if len(targets) > 50:
            print(f"  ... and {len(targets) - 50} more")
        return

    total_old = 0
    total_new = 0
    converted = 0
    collisions = 0
    failed = 0
    mapping = []

    for rel in targets:
        result = convert_one(rel, dry_run=False)
        if result is None:
            failed += 1
            continue
        webp_rel, old_bytes, new_bytes, was_collision = result
        total_old += old_bytes
        if new_bytes:
            total_new += new_bytes
        if was_collision:
            collisions += 1
        else:
            converted += 1
        mapping.append((rel, webp_rel))
        tag = "DEDUP" if was_collision else "OK"
        print(f"  {tag}  {rel} -> {webp_rel}  ({old_bytes/1024:.0f}KB -> {(new_bytes or 0)/1024:.0f}KB)")

    print()
    print(f"--- Done: {converted} converted, {collisions} deduped, {failed} failed ---")
    print(f"Old total: {total_old/1024/1024:.1f} MB, New total: {total_new/1024/1024:.1f} MB")
    if total_old:
        print(f"Reduction: {(1 - total_new/total_old)*100:.1f}%")

    map_path = os.path.join(BASE, "tools", "_webp_conversion_map.tsv")
    mode = "a" if os.path.exists(map_path) else "w"
    with open(map_path, mode, encoding="utf-8") as fh:
        for old_rel, new_rel in mapping:
            fh.write(f"{old_rel}\t{new_rel}\n")
    print(f"Wrote conversion map: {map_path} (+{len(mapping)} entries)")


if __name__ == "__main__":
    main()
