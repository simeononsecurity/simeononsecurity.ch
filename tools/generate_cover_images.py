#!/usr/bin/env python3
"""
generate_cover_images.py
------------------------
Two-step AI image pipeline for cover images AND missing in-article images:

  Step 1 – GPT-4o-mini reads the article and writes a tailored,
            detailed image-generation prompt, accessibility alt text,
            and an SEO-optimized, self-describing filename.

  Step 2 – gpt-image-2 generates a native 2048×1152 image (exact 16:9, 2K+).

For each article cover it then:
  • Saves the image to assets/img/cover/<seo-filename>.webp
  • Patches the frontmatter cover / coverAlt / coverCaption fields.

With --include-inline-images it additionally:
  • Scans the article body for image references (markdown, HTML <img>,
    and Hugo {{< figure >}} shortcodes).
  • Detects references whose target file does NOT exist on disk.
  • Generates the missing image and saves it to the referenced path
    (under static/ so plain /img/... references resolve directly).

Already-generated covers (cover field already set to an existing file)
are skipped automatically, so the script is safe to re-run.

SEO FILENAMES
-------------
Earlier versions named covers after the content directory, which produced
useless names like "index.en.md.webp" for top-level pages such as
content/courses-and-playbooks/index.en.md and risked duplicate filenames.
The prompt model now returns a descriptive, hyphenated, keyword-rich
filename (for example "comptia-a-plus-certification-study-guide.webp").
Collisions are resolved automatically with a numeric suffix.

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
    .venv/bin/python tools/generate_cover_images.py --dry-run --include-inline-images

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
COVER_DIR      = REPO_ROOT / "assets" / "img" / "cover"
COVER_URL_BASE = "/img/cover"
CONTENT_DIR    = REPO_ROOT / "content"
STATIC_DIR     = REPO_ROOT / "static"
ASSETS_DIR     = REPO_ROOT / "assets"

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

# How many chars of surrounding context to send for an inline image
INLINE_CONTEXT_CHARS = 700

# Retry config
RETRY_MAX       = 6          # max attempts per API call
RETRY_BASE_SECS = 1.0        # initial backoff
RETRY_MAX_SECS  = 60.0       # cap backoff at 60 s
RETRY_CODES     = {429, 500, 502, 503, 504}   # status codes worth retrying

# Image file extensions we know how to (re)generate as WebP
IMAGE_EXTS = {".webp", ".png", ".jpg", ".jpeg", ".gif"}

# ---------------------------------------------------------------------------
# Thread-safe helpers
# ---------------------------------------------------------------------------
_print_lock  = threading.Lock()
_write_lock  = threading.Lock()   # serialises frontmatter file writes
_counter_lock = threading.Lock()
_name_lock   = threading.Lock()   # serialises filename reservation

# Filenames reserved within this run (so parallel workers never collide even
# before the file is written to disk).
_reserved_names: set[str] = set()


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


def strip_frontmatter(md_text: str) -> str:
    return re.sub(r'^---\n.*?\n---\n', '', md_text, count=1, flags=re.DOTALL)


def get_article_body(md_text: str) -> str:
    stripped = strip_frontmatter(md_text)
    stripped = re.sub(r'\{\{[<>][^}]+[<>]\}\}', '', stripped)
    stripped = re.sub(r'\n{3,}', '\n\n', stripped)
    return stripped.strip()[:ARTICLE_BODY_LIMIT]


# ---------------------------------------------------------------------------
# Slug → cover filename
# ---------------------------------------------------------------------------

def slug_from_path(md_path: str) -> str:
    """
    Return the slug for any content/.../<slug>/index.en.md file.

    The slug is the name of the directory that directly contains the
    markdown file. This works for both:

      content/articles/<slug>/index.en.md   → <slug>
      content/<slug>/index.en.md            → <slug>

    The previous implementation returned the third path component which,
    for single-level pages, incorrectly yielded "index.en.md".
    """
    parent = Path(md_path).parent.name
    if parent and parent != "content":
        return parent
    # Fallback: filename without the .en.md suffix
    return Path(md_path).stem.replace(".en", "")


# ---------------------------------------------------------------------------
# SEO filename helpers
# ---------------------------------------------------------------------------

def sanitize_seo_filename(name: str, fallback: str = "cover") -> str:
    """
    Turn an arbitrary string into a safe, hyphenated, lowercase slug
    suitable for a filename (without extension).
    """
    name = (name or "").lower().strip()
    # Drop any extension the model may have appended
    name = re.sub(r'\.(webp|png|jpe?g|gif)$', '', name)
    name = re.sub(r'[^a-z0-9]+', '-', name)
    name = re.sub(r'-{2,}', '-', name).strip('-')
    name = name[:80].strip('-')
    return name or sanitize_seo_filename(fallback, "cover") or "cover"


def reserve_unique_cover_name(base: str) -> tuple[str, Path]:
    """
    Reserve a unique '<base>.webp' (or '<base>-N.webp') under COVER_DIR,
    accounting for both files already on disk and names reserved earlier
    in this same run. Returns (filename_without_ext_used, dest_path).
    """
    with _name_lock:
        candidate = base
        i = 2
        while (
            (COVER_DIR / f"{candidate}.webp").exists()
            or f"{candidate}.webp" in _reserved_names
        ):
            candidate = f"{base}-{i}"
            i += 1
        _reserved_names.add(f"{candidate}.webp")
        return candidate, COVER_DIR / f"{candidate}.webp"


# ---------------------------------------------------------------------------
# Detection: which articles need a cover?
# ---------------------------------------------------------------------------

def cover_file_exists(cover_val: str) -> bool:
    """
    True if the cover URL points to a file that exists under assets/ or static/.
    """
    if not cover_val:
        return False
    relative = cover_val.lstrip("/")
    return (
        (ASSETS_DIR / relative).exists()
        or (STATIC_DIR / relative).exists()
        # cover URLs are /img/cover/x.webp → assets/img/cover/x.webp
        or (ASSETS_DIR / "img" / relative).exists()
    )


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
        return not cover_file_exists(cover_val)

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


def all_markdown_files(content_globs: list[str]) -> list[str]:
    out: list[str] = []
    for pattern in content_globs:
        out.extend(sorted(glob.glob(pattern, recursive=True)))
    return out


# ---------------------------------------------------------------------------
# Inline-image detection
# ---------------------------------------------------------------------------

# Markdown images:        ![alt](url "title")
_MD_IMG_RE = re.compile(r'!\[(?P<alt>[^\]]*)\]\(\s*(?P<url>[^)\s]+)(?:\s+"[^"]*")?\s*\)')
# HTML <img ... src="url" ... alt="alt">
_HTML_IMG_RE = re.compile(r'<img\b[^>]*?>', re.IGNORECASE)
_HTML_SRC_RE = re.compile(r'src\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
_HTML_ALT_RE = re.compile(r'alt\s*=\s*["\']([^"\']*)["\']', re.IGNORECASE)
# Hugo figure shortcode:  {{< figure src="url" alt="alt" ... >}}
_FIGURE_RE = re.compile(r'\{\{<\s*figure\b(?P<args>[^>]*?)>\}\}', re.IGNORECASE)
_ARG_SRC_RE = re.compile(r'src\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
_ARG_ALT_RE = re.compile(r'alt\s*=\s*["\']([^"\']*)["\']', re.IGNORECASE)


def _is_local_image_ref(url: str) -> bool:
    """Only consider local image paths we could generate and host ourselves."""
    if not url:
        return False
    low = url.strip().lower()
    if low.startswith(("http://", "https://", "data:", "//", "mailto:")):
        return False
    ext = os.path.splitext(low.split("?")[0].split("#")[0])[1]
    return ext in IMAGE_EXTS


def _resolve_local_image(url: str, md_path: str) -> Path | None:
    """
    Map a referenced local image URL to the filesystem path it WOULD live at
    if it existed. Returns the most likely path (under static/ for root-anchored
    /img/... refs, alongside the article for relative refs).
    """
    clean = url.strip().split("?")[0].split("#")[0]
    if clean.startswith("/"):
        rel = clean.lstrip("/")
        return STATIC_DIR / rel
    # relative reference → alongside the markdown file
    return Path(md_path).parent / clean


def _image_ref_exists(url: str, md_path: str) -> bool:
    clean = url.strip().split("?")[0].split("#")[0]
    if clean.startswith("/"):
        rel = clean.lstrip("/")
        return (
            (STATIC_DIR / rel).exists()
            or (ASSETS_DIR / rel).exists()
            or (ASSETS_DIR / "img" / rel).exists()
        )
    candidate = Path(md_path).parent / clean
    return candidate.exists()


def find_missing_inline_images(md_path: str) -> list[dict]:
    """
    Return a list of dicts describing referenced-but-missing local images:
      {url, alt, dest, context}
    Deduplicated by url within the file.
    """
    raw = strip_frontmatter(Path(md_path).read_text(encoding="utf-8"))
    found: dict[str, dict] = {}

    def _consider(url: str, alt: str, pos: int):
        if not _is_local_image_ref(url):
            return
        if _image_ref_exists(url, md_path):
            return
        if url in found:
            return
        dest = _resolve_local_image(url, md_path)
        if dest is None:
            return
        start = max(0, pos - INLINE_CONTEXT_CHARS)
        end   = min(len(raw), pos + INLINE_CONTEXT_CHARS)
        context = re.sub(r'\s+', ' ', raw[start:end]).strip()
        found[url] = {
            "url": url,
            "alt": (alt or "").strip(),
            "dest": dest,
            "context": context,
        }

    for m in _MD_IMG_RE.finditer(raw):
        _consider(m.group("url"), m.group("alt"), m.start())

    for m in _HTML_IMG_RE.finditer(raw):
        tag = m.group(0)
        src_m = _HTML_SRC_RE.search(tag)
        if not src_m:
            continue
        alt_m = _HTML_ALT_RE.search(tag)
        _consider(src_m.group(1), alt_m.group(1) if alt_m else "", m.start())

    for m in _FIGURE_RE.finditer(raw):
        args = m.group("args")
        src_m = _ARG_SRC_RE.search(args)
        if not src_m:
            continue
        alt_m = _ARG_ALT_RE.search(args)
        _consider(src_m.group(1), alt_m.group(1) if alt_m else "", m.start())

    return list(found.values())


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
You are an expert at writing image generation prompts, accessibility alt text,
and SEO filenames for tech blog cover illustrations.

Given an article, produce a JSON object with exactly three keys:

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

  "filename" — A short, SEO-optimized, self-describing filename slug for the
    image. Rules:
    • Lowercase, words separated by single hyphens, NO file extension
    • 3 to 8 keyword-rich words drawn from the article's specific topic
    • Descriptive enough to stand alone (never generic like "index", "cover",
      "image", or "post")
    • Example: "comptia-a-plus-certification-study-guide"

Output ONLY valid JSON. No markdown fences, no explanation, no extra keys."""


INLINE_SYSTEM_PROMPT = """\
You are an expert at writing image generation prompts and accessibility alt text
for illustrations embedded inside technical blog articles.

You are given the article topic, the existing alt text for a specific in-article
image (which may be empty), and the surrounding paragraph context. Produce a JSON
object with exactly two keys:

  "prompt" — A detailed image generation prompt (under 900 chars) for an
    illustration that fits THIS specific spot in the article. Describe:
    • The concept the surrounding text is explaining
    • Art style: clean digital illustration, dark background (#0a0f1e or similar
      deep navy/charcoal), vibrant accent colors (blues, greens, purples, cyans)
    • Mood: technical, professional, modern, wide 16:9 landscape
    • IMPORTANT: absolutely NO text, letters, words, labels, or symbols
    • Be specific to the context, avoid generic shield/padlock clichés

  "alt" — A 1–2 sentence plain-English description of the image as accessibility
    alt text, under 200 characters. If useful existing alt text was provided,
    refine it; otherwise write fresh descriptive alt text.

Output ONLY valid JSON. No markdown fences, no explanation, no extra keys."""


def _chat_json(payload: dict, api_key: str, label: str) -> dict:
    import json
    import requests

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
        _check_response(resp, label)
        return resp

    resp = call_with_retry(_call, label)
    raw  = resp.json()["choices"][0]["message"]["content"].strip()
    return json.loads(raw)


def generate_image_prompt(title: str, article_body: str, api_key: str) -> tuple[str, str, str]:
    """
    Call GPT-4o-mini to write a tailored image prompt, coverAlt, and an
    SEO-optimized filename slug.
    Returns (image_prompt, cover_alt, seo_filename). Uses call_with_retry.
    """
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
        "max_tokens": 450,
        "temperature": 0.7,
        "response_format": {"type": "json_object"},
    }

    data = _chat_json(payload, api_key, "GPT prompt-gen")
    image_prompt = data.get("prompt", "").strip()
    cover_alt    = data.get("alt",    "").strip()
    seo_filename = sanitize_seo_filename(data.get("filename", ""), fallback=title)
    if not image_prompt:
        raise FatalError("GPT returned empty image prompt.")
    return image_prompt, cover_alt, seo_filename


def generate_inline_prompt(
    title: str, alt: str, context: str, api_key: str
) -> tuple[str, str]:
    """
    Call GPT-4o-mini to write an image prompt + alt text for a missing
    in-article image. Returns (image_prompt, alt_text).
    """
    user_content = (
        f"Article topic: {title}\n\n"
        f"Existing alt text (may be empty): {alt}\n\n"
        f"Surrounding context:\n{context}"
    )
    payload = {
        "model": PROMPT_MODEL,
        "messages": [
            {"role": "system", "content": INLINE_SYSTEM_PROMPT},
            {"role": "user",   "content": user_content},
        ],
        "max_tokens": 400,
        "temperature": 0.7,
        "response_format": {"type": "json_object"},
    }

    data = _chat_json(payload, api_key, "GPT inline prompt-gen")
    image_prompt = data.get("prompt", "").strip()
    alt_text     = data.get("alt",    "").strip()
    if not image_prompt:
        raise FatalError("GPT returned empty inline image prompt.")
    return image_prompt, alt_text


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

    dest_path.parent.mkdir(parents=True, exist_ok=True)

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
# Per-article cover worker
# ---------------------------------------------------------------------------

def process_one(
    md_path:   str,
    idx:       int,
    total:     int,
    api_key:   str,
    post_delay: float,
    force:     bool = False,
) -> tuple[str, bool, str]:
    """
    Process a single article cover. Returns (slug, success, error_msg).
    Designed to be called from a thread pool.
    """
    md_text    = Path(md_path).read_text(encoding="utf-8")
    title      = get_field(md_text, "title")
    slug       = slug_from_path(md_path)
    cover_val  = get_field(md_text, "cover").strip()

    tprint(f"[{idx}/{total}] {slug}")
    tprint(f"  Title : {title[:80]}")

    # Guard: a valid cover already exists — only refresh alt text.
    if cover_val and cover_file_exists(cover_val) and not force:
        tprint("  Cover already present — updating frontmatter only.")
        alt = get_field(md_text, "coverAlt") or build_alt_text(title)
        update_frontmatter(md_path, cover_val, alt)
        tprint("  Frontmatter updated.\n")
        return slug, True, ""

    article_body = get_article_body(md_text)

    try:
        tprint("  Step 1: GPT writing prompt + alt text + SEO filename...")
        image_prompt, cover_alt, seo_name = generate_image_prompt(
            title, article_body, api_key
        )
        # Prefer the AI SEO name; fall back to the slug if it degenerates.
        base_name = seo_name or sanitize_seo_filename(slug, "cover")
        if base_name in ("cover", "index", "image", "post"):
            base_name = sanitize_seo_filename(f"{slug}-{base_name}", "cover")

        used_name, cover_dest = reserve_unique_cover_name(base_name)
        cover_url = f"{COVER_URL_BASE}/{used_name}.webp"

        tprint(f"  Prompt : {image_prompt[:120]}...")
        tprint(f"  Alt    : {cover_alt[:80]}...")
        tprint(f"  File   : {used_name}.webp")

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
# Per-inline-image worker
# ---------------------------------------------------------------------------

def process_inline_image(
    md_path:    str,
    ref:        dict,
    idx:        int,
    total:      int,
    api_key:    str,
    post_delay: float,
) -> tuple[str, bool, str]:
    """
    Generate one missing in-article image referenced by `ref`.
    Saves to the exact path the markdown references so the link resolves.
    Returns (url, success, error_msg).
    """
    title = get_field(Path(md_path).read_text(encoding="utf-8"), "title")
    url   = ref["url"]
    dest  = ref["dest"]

    tprint(f"[inline {idx}/{total}] {url}")
    tprint(f"  In     : {slug_from_path(md_path)}")

    try:
        tprint("  Step 1: GPT writing inline prompt + alt text...")
        image_prompt, alt_text = generate_inline_prompt(
            title, ref.get("alt", ""), ref.get("context", ""), api_key
        )
        tprint(f"  Prompt : {image_prompt[:120]}...")

        tprint("  Step 2: Generating image...")
        image_bytes = generate_image(image_prompt, api_key)

        with _write_lock:
            save_image(image_bytes, dest)

        kb = dest.stat().st_size // 1024
        tprint(f"  Saved  : {dest}  ({kb} KB)\n")

        if post_delay > 0:
            time.sleep(post_delay)

        return url, True, ""

    except (RetryableError, FatalError, Exception) as exc:
        tprint(f"  [FAILED] {exc}\n")
        return url, False, str(exc)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Two-step AI cover + inline image generator: GPT writes the "
                    "prompt and an SEO filename, gpt-image-2 draws it."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="List work to be done, no API calls.")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max images to generate per run (0 = all).")
    parser.add_argument("--delay", type=float, default=0.5,
                        help="Per-worker sleep after each successful image (default: 0.5s). "
                             "Reduces burst pressure on the API.")
    parser.add_argument("--workers", type=int, default=3,
                        help="Parallel workers (default: 3). Stay within your API tier limits. "
                             "Each worker makes 2 API calls per image.")
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
    parser.add_argument("--include-inline-images", action="store_true",
                        help="Also scan article bodies for image references "
                             "(markdown, <img>, and {{< figure >}}) whose target "
                             "file does not exist, and generate the missing images.")
    parser.add_argument("--inline-only", action="store_true",
                        help="Skip cover generation and only generate missing "
                             "in-article images. Implies --include-inline-images.")
    args = parser.parse_args()

    if args.inline_only:
        args.include_inline_images = True

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

    # -------------------------------------------------------------------
    # Discover cover work
    # -------------------------------------------------------------------
    cover_targets: list[str] = []
    if not args.inline_only:
        print("Scanning for articles without cover images...")
        cover_targets = find_articles_without_covers(globs, force=args.force)
        if args.slug:
            cover_targets = [p for p in cover_targets if slug_from_path(p) == args.slug]

    # -------------------------------------------------------------------
    # Discover inline-image work
    # -------------------------------------------------------------------
    inline_jobs: list[tuple[str, dict]] = []
    if args.include_inline_images:
        print("Scanning article bodies for missing inline images...")
        for md_path in all_markdown_files(globs):
            if args.slug and slug_from_path(md_path) != args.slug:
                continue
            for ref in find_missing_inline_images(md_path):
                inline_jobs.append((md_path, ref))

    if not cover_targets and not inline_jobs:
        print("Nothing to do. All covers present and no missing inline images.")
        return

    print(f"\nFound {len(cover_targets)} article(s) missing a cover image.")
    if args.include_inline_images:
        print(f"Found {len(inline_jobs)} missing inline image reference(s).")

    if args.dry_run:
        if cover_targets:
            print("\nCovers to generate:")
            for p in cover_targets:
                print(f"  {slug_from_path(p)}")
        if inline_jobs:
            print("\nMissing inline images to generate:")
            for md_path, ref in inline_jobs:
                print(f"  {slug_from_path(md_path)} -> {ref['url']}")
        print("\n[DRY RUN] No images generated.")
        return

    COVER_DIR.mkdir(parents=True, exist_ok=True)

    # Apply a combined limit across both kinds of work.
    if args.limit:
        cover_targets = cover_targets[: args.limit]
        remaining = max(0, args.limit - len(cover_targets))
        inline_jobs = inline_jobs[: remaining]

    cover_total  = len(cover_targets)
    inline_total = len(inline_jobs)
    workers      = max(1, min(args.workers, cover_total + inline_total))

    print(f"Generating {cover_total} cover(s) and {inline_total} inline image(s) "
          f"with {workers} parallel worker(s) (2 API calls each)...\n")

    # Early-import to surface missing deps before entering thread pool
    import requests   # noqa
    from PIL import Image  # noqa

    success_count = 0
    failed_count  = 0
    failed_items: list[str] = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {}

        for idx, md_path in enumerate(cover_targets, 1):
            fut = executor.submit(
                process_one, md_path, idx, cover_total, api_key, args.delay, args.force
            )
            futures[fut] = ("cover", slug_from_path(md_path))

        for idx, (md_path, ref) in enumerate(inline_jobs, 1):
            fut = executor.submit(
                process_inline_image, md_path, ref, idx, inline_total,
                api_key, args.delay
            )
            futures[fut] = ("inline", ref["url"])

        for future in as_completed(futures):
            kind, label = futures[future]
            ident, ok, err = future.result()
            if ok:
                success_count += 1
            else:
                failed_count += 1
                failed_items.append(f"{kind}: {label}")

    print("-" * 60)
    print(f"Done. {success_count} succeeded, {failed_count} failed.")
    if failed_items:
        print("Failed items (re-run to retry):")
        for s in failed_items:
            print(f"  {s}")


if __name__ == "__main__":
    main()
