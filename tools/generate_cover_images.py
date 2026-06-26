#!/usr/bin/env python3
"""
generate_cover_images.py
------------------------
Two-step AI cover image pipeline:

  Step 1 – GPT-4o-mini reads the full article and writes a tailored,
            detailed image-generation prompt specific to the content.

  Step 2 – gpt-image-2 generates a native 2048×1152 image (exact 16:9, 2K+).

For each article it then:
  • Saves the image to static/img/cover/<slug>.webp
  • Patches the frontmatter cover / coverAlt / coverCaption fields.

Already-generated images (file exists on disk) are skipped automatically,
so the script is safe to re-run.

API KEY SECURITY
----------------
Never put your key in this file. Set OPENAI_API_KEY in the environment:

    export OPENAI_API_KEY="sk-..."
    .venv/bin/python tools/generate_cover_images.py

Or create a repo-root .env file (already in .gitignore):

    echo 'OPENAI_API_KEY=sk-...' > .env

SETUP
-----
    python3 -m venv .venv
    .venv/bin/pip install pillow requests python-dotenv

DRY RUN
-------
    .venv/bin/python tools/generate_cover_images.py --dry-run
"""

import argparse
import glob
import os
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Optional: load .env file if python-dotenv is available
# ---------------------------------------------------------------------------
try:
    from dotenv import load_dotenv
    _env_path = Path(__file__).resolve().parent.parent / ".env"
    if _env_path.exists():
        load_dotenv(dotenv_path=_env_path)
except ImportError:
    pass

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT      = Path(__file__).resolve().parent.parent
COVER_DIR      = REPO_ROOT / "static" / "img" / "cover"
COVER_URL_BASE = "/img/cover"

ARTICLE_GLOB = str(REPO_ROOT / "content" / "articles" / "**" / "index.en.md")
GUIDE_GLOB   = str(REPO_ROOT / "content" / "guides"   / "**" / "index.en.md")

# Model config
PROMPT_MODEL  = "gpt-4o-mini"  # cheap, fast; writes the image prompt
IMAGE_MODEL   = "gpt-image-2"  # generates the image (supports custom sizes)
IMAGE_SIZE    = "2048x1152"    # exact 16:9 at 2K+ (both dims /16). Native output.
IMAGE_QUALITY = "high"         # low | medium | high

# Native output dimensions (what gpt-image-2 produces — no resize needed)
OUTPUT_W = 2048
OUTPUT_H = 1152

# How many chars of article body to send to the prompt model (keeps costs low)
ARTICLE_BODY_LIMIT = 6000


# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------

def get_field(text: str, field: str) -> str:
    """Return a specific YAML front-matter field value."""
    pattern = re.compile(
        r'^' + re.escape(field) + r'\s*:\s*"?(.*?)"?\s*$',
        re.MULTILINE
    )
    m = pattern.search(text)
    return m.group(1).strip().strip('"') if m else ""


def set_field(text: str, field: str, value: str) -> str:
    """Set or insert a frontmatter field (quoted value)."""
    escaped = value.replace('"', '\\"')
    pattern = re.compile(
        r'^(' + re.escape(field) + r'\s*:).*$',
        re.MULTILINE
    )
    new_line = f'{field}: "{escaped}"'
    if pattern.search(text):
        return pattern.sub(new_line, text, count=1)
    close = text.find('\n---\n')
    if close == -1:
        return text
    return text[:close] + f'\n{new_line}' + text[close:]


def get_article_body(md_text: str) -> str:
    """Strip YAML frontmatter and return only the article body."""
    # Remove the opening --- block
    stripped = re.sub(r'^---\n.*?\n---\n', '', md_text, count=1, flags=re.DOTALL)
    # Remove markdown shortcodes like {{< youtube ... >}}
    stripped = re.sub(r'\{\{[<>][^}]+[<>]\}\}', '', stripped)
    # Collapse excess blank lines
    stripped = re.sub(r'\n{3,}', '\n\n', stripped)
    return stripped.strip()[:ARTICLE_BODY_LIMIT]


# ---------------------------------------------------------------------------
# Slug → cover filename
# ---------------------------------------------------------------------------

def slug_from_path(md_path: str) -> str:
    parts = Path(md_path).parts
    for i, part in enumerate(parts):
        if part in ("articles", "guides") and i + 1 < len(parts):
            return parts[i + 1]
    return Path(md_path).parent.name


# ---------------------------------------------------------------------------
# Detection: which articles need a cover?
# ---------------------------------------------------------------------------

def cover_file_exists(cover_value: str) -> bool:
    if not cover_value:
        return False
    relative = cover_value.lstrip("/")
    return (REPO_ROOT / "static" / relative).exists()


def needs_cover(md_path: str) -> bool:
    text = Path(md_path).read_text(encoding="utf-8")
    cover_val = get_field(text, "cover")
    if not cover_val:
        return True
    return not cover_file_exists(cover_val)


def find_articles_without_covers(content_globs: list[str]) -> list[str]:
    missing = []
    for pattern in content_globs:
        for md_path in sorted(glob.glob(pattern, recursive=True)):
            if needs_cover(md_path):
                missing.append(md_path)
    return missing


# ---------------------------------------------------------------------------
# Step 1: GPT generates a tailored image prompt from the article
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert at writing image generation prompts and accessibility alt text
for tech blog cover illustrations.

Given an article, produce a JSON object with exactly two keys:

  "prompt" — A detailed image generation prompt (under 900 chars) describing:
    • The central visual concept specific to the article's exact topic
    • Art style: clean digital illustration, dark background (#0a0f1e or similar
      deep navy/charcoal), vibrant accent colors (blues, greens, purples, cyans)
    • Mood: technical, professional, modern
    • Composition: wide 16:9 landscape format, suitable as a blog header
    • IMPORTANT: absolutely NO text, letters, words, labels, or symbols
    • No generic shield/padlock clichés — be specific and creative

  "alt" — A 1–2 sentence plain-English description of what the image looks like,
    written as accessibility alt text. Describe the visual elements concretely,
    as if describing it to someone who cannot see it. No opinions, no marketing.
    Keep it under 200 characters.

Output ONLY valid JSON. No markdown fences, no explanation, no extra keys."""


def generate_image_prompt(title: str, article_body: str, api_key: str) -> tuple[str, str]:
    """
    Call GPT-4o-mini to write a tailored image prompt and coverAlt from the article.
    Returns (image_prompt, cover_alt).
    """
    import json
    import requests
    user_content = (
        f"Article title: {title}\n\n"
        f"Article content:\n{article_body}"
    )
    payload = {
        "model": PROMPT_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_content},
        ],
        "max_tokens": 400,
        "temperature": 0.7,
        "response_format": {"type": "json_object"},
    }
    resp = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )
    if resp.status_code != 200:
        raise RuntimeError(
            f"GPT prompt-gen error {resp.status_code}: {resp.text[:300]}"
        )
    raw = resp.json()["choices"][0]["message"]["content"].strip()
    data = json.loads(raw)
    image_prompt = data.get("prompt", "").strip()
    cover_alt    = data.get("alt", "").strip()
    if not image_prompt:
        raise RuntimeError("GPT returned empty image prompt.")
    if not cover_alt:
        cover_alt = build_alt_text(title)
    return image_prompt, cover_alt


# ---------------------------------------------------------------------------
# Step 2: gpt-image-1 generates the image
# ---------------------------------------------------------------------------

def generate_image(prompt: str, api_key: str) -> bytes:
    """Call gpt-image-1 with the AI-generated prompt and return WebP bytes."""
    import base64
    import requests
    payload = {
        "model": IMAGE_MODEL,
        "prompt": prompt,
        "n": 1,
        "size": IMAGE_SIZE,
        "quality": IMAGE_QUALITY,
        "output_format": "webp",
    }
    resp = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=120,
    )
    if resp.status_code != 200:
        raise RuntimeError(
            f"Image gen error {resp.status_code}: {resp.text[:400]}"
        )
    b64 = resp.json()["data"][0]["b64_json"]
    return base64.b64decode(b64)


def save_image(image_bytes: bytes, dest_path: Path) -> None:
    """
    Save the generated image as WebP at OUTPUT_W × OUTPUT_H.

    gpt-image-2 at 2048×1152 is already exact 16:9 at 2K+ resolution.
    We pass through PIL only for format conversion and WebP compression.
    If for any reason the returned size differs, PIL center-crops to target.
    """
    from PIL import Image
    import io
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    src_w, src_h = img.size

    if src_w == OUTPUT_W and src_h == OUTPUT_H:
        # Perfect match — just recompress as WebP
        img.save(dest_path, "WEBP", quality=85, method=6)
        return

    # Fallback: scale to cover then center-crop to target dimensions
    scale = max(OUTPUT_W / src_w, OUTPUT_H / src_h)
    new_w = round(src_w * scale)
    new_h = round(src_h * scale)
    img   = img.resize((new_w, new_h), Image.LANCZOS)
    left  = (new_w - OUTPUT_W) // 2
    top   = (new_h - OUTPUT_H) // 2
    img   = img.crop((left, top, left + OUTPUT_W, top + OUTPUT_H))
    img.save(dest_path, "WEBP", quality=85, method=6)


# ---------------------------------------------------------------------------
# Frontmatter update
# ---------------------------------------------------------------------------

def build_alt_text(title: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9 ,:-]", "", title)
    return f"Cover image for: {clean}"


def update_frontmatter(md_path: str, cover_url: str, cover_alt: str) -> None:
    text = Path(md_path).read_text(encoding="utf-8")
    text = set_field(text, "cover", cover_url)
    text = set_field(text, "coverAlt", cover_alt)
    if not get_field(text, "coverCaption"):
        text = set_field(text, "coverCaption", "")
    Path(md_path).write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Two-step AI cover: GPT writes the prompt, gpt-image-1 draws it."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="List articles missing covers, no API calls.")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max images to generate per run (0 = all).")
    parser.add_argument("--delay", type=float, default=2.0,
                        help="Seconds between API call pairs (default: 2).")
    parser.add_argument("--content-dir",
                        choices=["articles", "guides", "both"], default="both",
                        help="Which content directories to scan.")
    parser.add_argument("--slug", type=str, default="",
                        help="Process only the article/guide with this slug.")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key and not args.dry_run:
        print(
            "\n[ERROR] OPENAI_API_KEY not set.\n"
            "  export OPENAI_API_KEY='sk-...'\n"
            "  or add it to a .env file in the repo root.\n"
        )
        sys.exit(1)

    globs = []
    if args.content_dir in ("articles", "both"):
        globs.append(ARTICLE_GLOB)
    if args.content_dir in ("guides", "both"):
        globs.append(GUIDE_GLOB)

    print("Scanning for articles without cover images...")
    missing = find_articles_without_covers(globs)
    if args.slug:
        missing = [p for p in missing if slug_from_path(p) == args.slug]

    if not missing:
        print("All articles have cover images. Nothing to do.")
        return

    print(f"\nFound {len(missing)} article(s) missing a cover image.")
    if args.dry_run:
        for p in missing:
            print(f"  {slug_from_path(p)}")
        print(f"\n[DRY RUN] No images generated.")
        return

    COVER_DIR.mkdir(parents=True, exist_ok=True)
    targets = missing if not args.limit else missing[: args.limit]
    total = len(targets)
    print(f"Generating {total} cover image(s) (2 API calls each: GPT + image)...\n")

    import requests  # noqa – early import to catch missing dep
    from PIL import Image  # noqa

    success = 0
    failed = 0

    for idx, md_path in enumerate(targets, 1):
        md_text      = Path(md_path).read_text(encoding="utf-8")
        title        = get_field(md_text, "title")
        slug         = slug_from_path(md_path)
        cover_dest   = COVER_DIR / f"{slug}.webp"
        cover_url    = f"{COVER_URL_BASE}/{slug}.webp"

        print(f"[{idx}/{total}] {slug}")
        print(f"  Title : {title[:80]}")

        # Already generated – just fix frontmatter
        if cover_dest.exists():
            print("  Image already on disk. Updating frontmatter only.")
            update_frontmatter(md_path, cover_url, build_alt_text(title))
            print("  Frontmatter updated.\n")
            success += 1
            continue

        article_body = get_article_body(md_text)

        try:
            # --- Step 1: GPT writes the image prompt + alt text ---
            print("  Step 1: GPT writing image prompt + alt text...")
            image_prompt, cover_alt = generate_image_prompt(title, article_body, api_key)
            print(f"  Prompt : {image_prompt[:120]}...")
            print(f"  Alt    : {cover_alt[:80]}...")

            # --- Step 2: gpt-image-1 renders the image ---
            print("  Step 2: Generating image...")
            image_bytes = generate_image(image_prompt, api_key)
            save_image(image_bytes, cover_dest)

            update_frontmatter(md_path, cover_url, cover_alt)
            print(f"  Saved  : {cover_dest}")
            print(f"  Size   : {cover_dest.stat().st_size // 1024} KB\n")
            success += 1

        except Exception as exc:
            print(f"  [FAILED] {exc}\n")
            failed += 1

        if idx < total:
            time.sleep(args.delay)

    print("-" * 60)
    print(f"Done. {success} succeeded, {failed} failed.")
    if failed:
        print("Re-run to retry failed articles.")


if __name__ == "__main__":
    main()
