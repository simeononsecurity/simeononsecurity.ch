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

PARALLELISM & RATE LIMITS
--------------------------
--workers controls how many articles are processed concurrently.
Each worker makes 2 API calls (GPT prompt + image generation).
Default is 3 workers which stays safely within standard tier limits.

Automatic retry with exponential backoff + jitter handles 429 / 5xx
responses. The Retry-After header is respected when present.

CONTENT DIRS
------------
--content-dir accepts any comma-separated list of subdirectory names
under content/, OR the special values:

  all           → every subdirectory in content/ that contains index.en.md files
  both          → articles,guides  (backward-compat alias)

Examples:
  --content-dir articles
  --content-dir guides
  --content-dir blog
  --content-dir articles,guides,blog,writeups
  --content-dir all
"""

import argparse
import glob
import os
import random
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
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
CONTENT_DIR    = REPO_ROOT / "content"

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

# Retry config
RETRY_MAX       = 6          # max attempts per API call
RETRY_BASE_SECS = 1.0        # initial backoff
RETRY_MAX_SECS  = 60.0       # cap backoff at 60 s
RETRY_CODES     = {429, 500, 502, 503, 504}   # status codes worth retrying

# ---------------------------------------------------------------------------
# Thread-safe helpers
# ---------------------------------------------------------------------------
_print_lock  = threading.Lock()
_write_lock  = threading.Lock()   # serialises frontmatter file writes
_counter_lock = threading.Lock()

def tprint(*args, **kwargs) -> None:
    """Thread-safe print."""
    with _print_lock:
        print(*args, **kwargs)


# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------

def get_field(text: str, field: str) -> str:
    pattern = re.compile(
        r'^' + re.escape(field) + r'\s*:\s*"?(.*?)"?\s*$',
        re.MULTILINE
    )
    m = pattern.search(text)
    return m.group(1).strip().strip('"') if m else ""


def set_field(text: str, field: str, value: str) -> str:
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
    stripped = re.sub(r'^---\n.*?\n---\n', '', md_text, count=1, flags=re.DOTALL)
    stripped = re.sub(r'\{\{[<>][^}]+[<>]\}\}', '', stripped)
    stripped = re.sub(r'\n{3,}', '\n\n', stripped)
    return stripped.strip()[:ARTICLE_BODY_LIMIT]


# ---------------------------------------------------------------------------
# Slug → cover filename
# ---------------------------------------------------------------------------

def slug_from_path(md_path: str) -> str:
    """
    Return the slug for content/<subdir>/<slug>/index.en.md.
    Works with articles, guides, blog, writeups, or any other content subdir.
    """
    parts = Path(md_path).parts
    for i, part in enumerate(parts):
        if part == "content" and i + 2 < len(parts):
            return parts[i + 2]
    return Path(md_path).parent.name


# ---------------------------------------------------------------------------
# Detection: which articles need a cover?
# ---------------------------------------------------------------------------

def needs_cover(md_path: str, force: bool = False) -> bool:
    """
    Returns True only when the article has no cover set (field absent or empty).

    If force=True, also returns True when the cover field is set but the
    referenced file does not exist on disk — allowing broken covers to be
    regenerated.  Use --force on the CLI to enable this.

    We deliberately do NOT regenerate when a non-empty cover value is already
    present and force is False, even if the file happens to be missing from
    this checkout. That protects hand-crafted or externally-hosted cover art.
    """
    text      = Path(md_path).read_text(encoding="utf-8")
    cover_val = get_field(text, "cover").strip()

    if not cover_val:
        return True   # no cover at all — always generate

    if force:
        # In force mode, also flag covers whose file is absent on disk
        relative = cover_val.lstrip("/")
        return not (REPO_ROOT / "static" / relative).exists()

    return False      # cover field is set — leave it alone


def resolve_content_dirs(spec: str) -> list[str]:
    """
    Turn a --content-dir value into a list of glob patterns.

      all   → every immediate subdir of content/
      both  → articles,guides  (backward compat)
      else  → comma-separated subdir names
    """
    spec = spec.strip()
    if spec == "all":
        subdirs = [
            d.name for d in sorted(CONTENT_DIR.iterdir())
            if d.is_dir() and not d.name.startswith("_")
        ]
    elif spec == "both":
        subdirs = ["articles", "guides"]
    else:
        subdirs = [s.strip() for s in spec.split(",") if s.strip()]

    globs = []
    for subdir in subdirs:
        path = CONTENT_DIR / subdir
        if not path.is_dir():
            tprint(f"  [WARN] content/{subdir}/ does not exist — skipping.")
            continue
        globs.append(str(path / "**" / "index.en.md"))
    return globs


def find_articles_without_covers(content_globs: list[str], force: bool = False) -> list[str]:
    missing = []
    for pattern in content_globs:
        for md_path in sorted(glob.glob(pattern, recursive=True)):
            if needs_cover(md_path, force=force):
                missing.append(md_path)
    return missing


# ---------------------------------------------------------------------------
# Retry wrapper with exponential backoff + jitter
# ---------------------------------------------------------------------------

class RetryableError(Exception):
    """Raised for transient API errors that are safe to retry."""
    def __init__(self, msg: str, retry_after: float = 0.0):
        super().__init__(msg)
        self.retry_after = retry_after   # seconds from Retry-After header


class FatalError(Exception):
    """Raised for non-retryable API errors (bad key, bad request, etc.)."""


def _backoff_secs(attempt: int, retry_after: float = 0.0) -> float:
    """Exponential backoff with full jitter, respecting Retry-After."""
    if retry_after > 0:
        return retry_after + random.uniform(0, 1)
    cap  = min(RETRY_BASE_SECS * (2 ** attempt), RETRY_MAX_SECS)
    return cap * random.random() + 0.5   # jitter: [0.5, cap]


def call_with_retry(fn, label: str):
    """
    Call fn() up to RETRY_MAX times, backing off on RetryableError.
    Raises FatalError or the last RetryableError if all retries are exhausted.
    """
    last_exc = None
    for attempt in range(RETRY_MAX):
        try:
            return fn()
        except RetryableError as exc:
            last_exc = exc
            wait = _backoff_secs(attempt, exc.retry_after)
            tprint(f"    [retry {attempt+1}/{RETRY_MAX}] {label} — "
                   f"{exc} — waiting {wait:.1f}s")
            time.sleep(wait)
        except FatalError:
            raise
    raise last_exc  # exhausted


def _check_response(resp, context: str) -> None:
    """Raise the appropriate error type for non-200 HTTP responses."""
    import requests as req_mod
    status = resp.status_code
    if status == 200:
        return
    if status in RETRY_CODES:
        retry_after = 0.0
        ra_header = resp.headers.get("Retry-After", "")
        if ra_header:
            try:
                retry_after = float(ra_header)
            except ValueError:
                pass
        raise RetryableError(
            f"{context} returned {status}: {resp.text[:200]}",
            retry_after=retry_after,
        )
    raise FatalError(f"{context} returned {status}: {resp.text[:300]}")


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
    Call GPT-4o-mini to write a tailored image prompt + coverAlt.
    Returns (image_prompt, cover_alt).  Uses call_with_retry internally.
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

    def _call():
        resp = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )
        _check_response(resp, "GPT prompt-gen")
        return resp

    resp = call_with_retry(_call, "GPT prompt-gen")
    raw  = resp.json()["choices"][0]["message"]["content"].strip()
    data = json.loads(raw)
    image_prompt = data.get("prompt", "").strip()
    cover_alt    = data.get("alt",    "").strip()
    if not image_prompt:
        raise FatalError("GPT returned empty image prompt.")
    return image_prompt, cover_alt


# ---------------------------------------------------------------------------
# Step 2: gpt-image-2 generates the image
# ---------------------------------------------------------------------------

def generate_image(prompt: str, api_key: str) -> bytes:
    """Call gpt-image-2 with the AI-generated prompt. Returns WebP bytes."""
    import base64
    import requests

    payload = {
        "model":         IMAGE_MODEL,
        "prompt":        prompt,
        "n":             1,
        "size":          IMAGE_SIZE,
        "quality":       IMAGE_QUALITY,
        "output_format": "webp",
    }

    def _call():
        resp = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=120,
        )
        _check_response(resp, "Image gen")
        return resp

    resp = call_with_retry(_call, "Image gen")
    b64  = resp.json()["data"][0]["b64_json"]
    return base64.b64decode(b64)


def save_image(image_bytes: bytes, dest_path: Path) -> None:
    """
    Save generated image as WebP at OUTPUT_W × OUTPUT_H.
    gpt-image-2 native 2048×1152 needs no resize — PIL recompresses only.
    Falls back to scale+crop if dimensions differ.
    """
    from PIL import Image
    import io

    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    src_w, src_h = img.size

    if src_w == OUTPUT_W and src_h == OUTPUT_H:
        img.save(dest_path, "WEBP", quality=85, method=6)
        return

    scale = max(OUTPUT_W / src_w, OUTPUT_H / src_h)
    new_w = round(src_w * scale)
    new_h = round(src_h * scale)
    img   = img.resize((new_w, new_h), Image.LANCZOS)
    left  = (new_w - OUTPUT_W) // 2
    top   = (new_h - OUTPUT_H) // 2
    img   = img.crop((left, top, left + OUTPUT_W, top + OUTPUT_H))
    img.save(dest_path, "WEBP", quality=85, method=6)


# ---------------------------------------------------------------------------
# Frontmatter update (thread-safe)
# ---------------------------------------------------------------------------

def build_alt_text(title: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9 ,:-]", "", title)
    return f"Cover image for: {clean}"


def update_frontmatter(md_path: str, cover_url: str, cover_alt: str) -> None:
    with _write_lock:
        text = Path(md_path).read_text(encoding="utf-8")
        text = set_field(text, "cover",        cover_url)
        text = set_field(text, "coverAlt",     cover_alt)
        if not get_field(text, "coverCaption"):
            text = set_field(text, "coverCaption", "")
        Path(md_path).write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Per-article worker
# ---------------------------------------------------------------------------

def process_one(
    md_path:   str,
    idx:       int,
    total:     int,
    api_key:   str,
    post_delay: float,
) -> tuple[str, bool, str]:
    """
    Process a single article. Returns (slug, success, error_msg).
    Designed to be called from a thread pool.
    """
    md_text    = Path(md_path).read_text(encoding="utf-8")
    title      = get_field(md_text, "title")
    slug       = slug_from_path(md_path)
    cover_dest = COVER_DIR / f"{slug}.webp"
    cover_url  = f"{COVER_URL_BASE}/{slug}.webp"

    tprint(f"[{idx}/{total}] {slug}")
    tprint(f"  Title : {title[:80]}")

    if cover_dest.exists():
        tprint("  Image already on disk — updating frontmatter only.")
        update_frontmatter(md_path, cover_url, build_alt_text(title))
        tprint("  Frontmatter updated.\n")
        return slug, True, ""

    article_body = get_article_body(md_text)

    try:
        tprint("  Step 1: GPT writing image prompt + alt text...")
        image_prompt, cover_alt = generate_image_prompt(title, article_body, api_key)
        tprint(f"  Prompt : {image_prompt[:120]}...")
        tprint(f"  Alt    : {cover_alt[:80]}...")

        tprint("  Step 2: Generating image...")
        image_bytes = generate_image(image_prompt, api_key)

        with _write_lock:
            save_image(image_bytes, cover_dest)

        if not cover_alt:
            cover_alt = build_alt_text(title)
        update_frontmatter(md_path, cover_url, cover_alt)

        kb = cover_dest.stat().st_size // 1024
        tprint(f"  Saved  : {cover_dest}  ({kb} KB)\n")

        if post_delay > 0:
            time.sleep(post_delay)

        return slug, True, ""

    except (RetryableError, FatalError, Exception) as exc:
        tprint(f"  [FAILED] {exc}\n")
        return slug, False, str(exc)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Two-step AI cover: GPT writes the prompt, gpt-image-2 draws it."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="List articles missing covers, no API calls.")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max images to generate per run (0 = all).")
    parser.add_argument("--delay", type=float, default=0.5,
                        help="Per-worker sleep after each successful image (default: 0.5s). "
                             "Reduces burst pressure on the API.")
    parser.add_argument("--workers", type=int, default=3,
                        help="Parallel workers (default: 3). Stay within your API tier limits. "
                             "Each worker makes 2 API calls per article.")
    parser.add_argument("--content-dir", default="both",
                        metavar="DIRS",
                        help=(
                            "Comma-separated list of content subdirs to scan "
                            "(e.g. articles,guides,blog,writeups). "
                            "Special values: 'all' scans every subdir under content/, "
                            "'both' is an alias for 'articles,guides'. "
                            "Default: both"
                        ))
    parser.add_argument("--slug", type=str, default="",
                        help="Process only the article/guide with this slug.")
    parser.add_argument("--force", action="store_true",
                        help="Also (re-)generate covers whose cover field is set but "
                             "the referenced file is missing on disk. "
                             "Never overwrites articles that already have a cover "
                             "field pointing to an existing file.")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key and not args.dry_run:
        print(
            "\n[ERROR] OPENAI_API_KEY not set.\n"
            "  export OPENAI_API_KEY='sk-...'\n"
            "  or add it to a .env file in the repo root.\n"
        )
        sys.exit(1)

    globs = resolve_content_dirs(args.content_dir)
    if not globs:
        print("[ERROR] No valid content directories found. Check --content-dir value.")
        sys.exit(1)

    print("Scanning for articles without cover images...")
    missing = find_articles_without_covers(globs, force=args.force)
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
    total   = len(targets)
    workers = min(args.workers, total)

    print(f"Generating {total} cover image(s) with {workers} parallel worker(s) "
          f"(2 API calls each: GPT + image)...\n")

    # Early-import to surface missing deps before entering thread pool
    import requests   # noqa
    from PIL import Image  # noqa

    success_count = 0
    failed_count  = 0
    failed_slugs: list[str] = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                process_one, md_path, idx, total, api_key, args.delay
            ): md_path
            for idx, md_path in enumerate(targets, 1)
        }
        for future in as_completed(futures):
            slug, ok, err = future.result()
            if ok:
                success_count += 1
            else:
                failed_count += 1
                failed_slugs.append(slug)

    print("-" * 60)
    print(f"Done. {success_count} succeeded, {failed_count} failed.")
    if failed_slugs:
        print("Failed slugs (re-run to retry):")
        for s in failed_slugs:
            print(f"  {s}")


if __name__ == "__main__":
    main()
