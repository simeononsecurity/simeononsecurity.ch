# Cover Image Generation Pipeline

This rule documents `tools/generate_cover_images.py` — the two-step AI pipeline
that generates cover images and missing in-article images for every content page
on this site.

---

## What the Script Does

**Step 1** — GPT-4o-mini reads the article title and body (up to 6,000 chars) and
returns a JSON object with three fields:

- `prompt` — a detailed image-generation prompt under 900 chars
- `alt` — plain-English accessibility alt text under 200 chars
- `filename` — an SEO-optimized hyphenated slug (no extension)

**Step 2** — gpt-image-2 generates a native 2048×1152 WebP (exact 16:9 at 2K+).
PIL recompresses to WebP quality 85. No resize is needed for the native size.

For covers, the script saves to `assets/img/cover/<seo-filename>.webp` and patches
`cover`, `coverAlt`, and `coverCaption` in the article's front matter.

For inline images (`--include-inline-images`), it scans for `![](url)`, `<img>`,
and `{{< figure >}}` references whose target file does not exist, generates the
missing image, and saves it to the exact path the markdown references.

---

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install pillow requests python-dotenv
echo 'OPENAI_API_KEY=sk-...' > .env   # already in .gitignore
```

---

## Common Commands

```bash
# Dry run — see what work is pending without making API calls
.venv/bin/python tools/generate_cover_images.py --content-dir all --force --include-inline-images --dry-run

# Full generation, background, 3 parallel workers
nohup .venv/bin/python tools/generate_cover_images.py \
  --content-dir all --force --include-inline-images --workers 3 \
  > /tmp/cover_gen.log 2>&1 &

# Monitor the log
tail -f /tmp/cover_gen.log

# Single article
.venv/bin/python tools/generate_cover_images.py \
  --content-dir articles --slug my-article-slug --force

# Inline images only
.venv/bin/python tools/generate_cover_images.py \
  --content-dir all --inline-only
```

**Key flags:**

| Flag | Purpose |
|------|---------|
| `--content-dir all` | Scan every subdirectory under `content/` |
| `--force` | Also regenerate covers whose file is referenced but missing on disk |
| `--include-inline-images` | Also generate missing body images |
| `--inline-only` | Skip covers, only generate missing inline images |
| `--workers N` | Parallel workers (default 3); each uses 2 API calls |
| `--limit N` | Max images per run |
| `--dry-run` | Print work list, no API calls |
| `--slug <slug>` | Restrict to one article by slug |

---

## Where Images Are Saved

| Reference type | Saved to |
|----------------|----------|
| Cover (`/img/cover/x.webp`) | `assets/img/cover/x.webp` |
| Root-anchored inline (`/img/foo/x.webp`) | `static/img/foo/x.webp` |
| Relative inline (`x.webp`) | `content/<path>/<slug>/x.webp` (page bundle) |

---

## Stem-Matching Bug Fixed 2026-08-02

`_image_ref_exists` now also checks all `IMAGE_EXTS` for the same stem in
every search directory (page bundle, `static/`, `assets/`). This prevents
the script from regenerating an image when `foo.png` already exists but
the article references `foo.jpg`.

**How it was triggered:** An article had two `{{< figure >}}` tags — one
referencing `aclu-get-flock-out-header.png` (the real photo) and a second
referencing `aclu-get-flock-out-header.jpg` (a stale/erroneous variant).
The `.png` existed; the `.jpg` did not. The old code saw only the exact
filename match and generated a new AI `.jpg`, overwriting intent.

**Fix:** After the exact-match checks fail, the function now loops over
`IMAGE_EXTS` and checks `stem + ext` in each search location. If any image
with the same stem and any supported extension exists, it returns `True`.

**Lesson:** When an article references `foo.jpg` but `foo.png` exists (same
stem), always treat it as already satisfied rather than generating a new image.
Do not commit an AI-generated `.jpg` when an original `.png` is present. The
`.png` is the real image; the `.jpg` reference in the article should be fixed
to match the actual file extension.

## Image Existence Checks — Critical Bug Fixed 2026-08-02
## Image Existence Checks — Critical Bug Fixed 2026-08-02

`cover_file_exists()` and `_image_ref_exists()` both check multiple locations.
Before the fix, they only checked `assets/` and `static/`, missing images stored
in the page bundle alongside `index.en.md`.

**After the fix:**

- `cover_file_exists(cover_val, md_path)` accepts the markdown file path and also
  checks `Path(md_path).parent / Path(relative).name`.
- `_image_ref_exists(url, md_path)` root-anchored branch now also checks
  `page_bundle_dir / Path(rel).name`.
- All callers of `cover_file_exists` pass `md_path` as the second argument.

**Symptom of the old bug:** `--dry-run --force --include-inline-images` reported
images as missing even though they existed in the page bundle. After the fix,
the dry run correctly reports "Nothing to do" for those files.

---

## SEO Filename Behavior

The prompt model returns a descriptive filename slug. The script sanitizes it
(lowercase, hyphens, max 80 chars, strips extension). Numeric suffixes (`-2`,
`-3`, ...) are appended automatically if the name is already taken on disk or
reserved within the current run (thread-safe).

Cover filenames intentionally do NOT use the content directory slug because many
`_index.en.md` pages share generic parent directory names like `index`.

---

## Retry and Rate Limits

The script uses exponential backoff with full jitter (base 1s, cap 60s) on HTTP
429 / 5xx responses. The `Retry-After` header is respected when present.

Default 3 workers × 2 API calls each = 6 concurrent calls. This stays safely
within standard-tier gpt-image-2 limits. Reduce `--workers` if you hit persistent
429 errors.

---

## Article Body Limit

Only the first 6,000 chars of the stripped article body are sent to GPT. This
keeps prompt costs low while providing enough context for a specific image prompt.

---

## Inline Image Context Window

For missing inline images, 700 chars of surrounding text (before and after the
image reference position) are extracted and sent as context. This lets the prompt
model understand what the image should illustrate.
