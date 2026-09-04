# Image WebP Conversion Pipeline

This rule documents the one-time (and repeatable) conversion of every PNG/JPG/JPEG
raster image in the repo to WebP, done to cut bandwidth. Use this rule whenever new
raster images enter the repo (e.g. from a contributor PR, a manual upload, or a
script that has not yet been updated to output WebP) and need conversion.

## Why This Matters

`assets/img/cover/` alone was ~380MB of raw PNG cover images served with zero
compression by the theme's cover partial and by the `/carousel/` gallery page
(`layouts/section/carousel.html`), which loops every page's raw cover image and
eager-loads the first 24 in the initial DOM. Across the whole repo, PNG + JPEG
totaled ~572MB versus ~112MB of pre-existing WebP. Converting to WebP at quality 85
cuts each file by 75-90% with no visible quality loss, since WebP is already the
format the site's own Hugo image pipeline (`.Resize "... webp q80"`) re-encodes
everything to for responsive srcsets.

## The Three Scripts (`tools/`)

Run in this order. All three are idempotent and safe to re-run.

1. **`convert_images_to_webp.py`** — converts PNG/JPG/JPEG to WebP (quality 85),
   deletes the raster original, writes `tools/_webp_conversion_map.tsv` (a
   temporary file, delete it after the pipeline finishes). Excludes all `.gif`
   files and a fixed PWA/OS icon set (`static/img/windows11|ios|android/`,
   `favicon.png`, `apple-touch-icon-*.png`, `maskable_icon.png`, `512x512.png`,
   `96x96.png`) where WebP support is inconsistent on older iOS Safari/Windows.
   ```bash
   .venv/bin/python3 tools/convert_images_to_webp.py --dry-run   # preview
   .venv/bin/python3 tools/convert_images_to_webp.py --dir assets/img/cover
   ```
   **Collision handling**: if a `.webp` with the same stem already exists, the
   script validates it (`PIL.Image.open().load()`) before trusting it. A 0-byte
   or corrupted pre-existing `.webp` is regenerated from the raster source rather
   than blindly kept. This guards against a real bug found during the 2026-09
   conversion: a stale 0-byte cover `.webp` from a failed prior AI-generation run
   silently broke a Hugo build (`resize: source size must be greater than 0`)
   until the script started validating collisions.

2. **`rewrite_webp_references.py`** — rewrites every text reference to a
   converted file (markdown front matter, markdown bodies, TOML config, Hugo
   templates, XML feeds). Reads `tools/_webp_conversion_map.tsv`.
   ```bash
   .venv/bin/python3 tools/rewrite_webp_references.py --dry-run
   .venv/bin/python3 tools/rewrite_webp_references.py
   ```
   Uses three different rewrite strategies depending on where the image lives:
   - `assets/img/cover/*` — safe to replace by bare basename repo-wide (one
     cover per article, flat directory, no collisions).
   - `assets/img/ads/**/*` — replace by the directory-qualified
     `img/ads/.../file.ext` path (with and without leading `/`), since this is
     how `resources.Get "..."` calls and `content/advertise/index.en.md`
     reference them.
   - `content/**/*` (page-bundle inline images) — rewritten **only** within
     text files in the SAME directory as the image, never repo-wide, because
     basenames collide across different article directories (for example
     `installedantenna.png` exists in three separate GPS-mining guides, each
     with its own distinct image). A repo-wide basename swap here would corrupt
     unrelated articles.
   - Any basename match inside an `http(s)://` URL is protected from rewriting.
     A page bundle can contain a local image (`copyasadmin.png`) whose basename
     coincidentally matches a remote-hosted asset referenced via full URL
     (`https://github.com/.../demo/copyasadmin.png?raw=true`); only the local
     file gets its reference updated, the remote URL is left untouched.

3. **`fix_ad_permalink_idiom.py`** — fixes a paired-idiom bug that step 2 alone
   cannot fix. Every ad partial under `layouts/partials/ads/**` and the theme's
   `themes/soshellofriend/layouts/partials/preload-images.html` derives a resized
   filename with:
   ```gotemplate
   {{ $Xsrc := resources.Get "path/file.EXT" }}
   {{ $Xsrcpermalink := replace $Xsrc.RelPermalink ".EXT" "" }}
   ```
   Once `resources.Get` is repointed at the new `.webp` file (by step 2), the
   `replace ... ".EXT" ""` strip still targets the OLD extension and silently
   fails to match, leaving `$Xsrcpermalink` ending in `.webp`. The later
   `printf "%s_%dx%d.%s" ... "webp"` call then produces a double-extension
   filename like `file.webp_255x255.webp`, a real filename that Hugo happily
   writes but that breaks the `<link rel=prefetch>` and `<img>` tags pointing at
   the correctly-named resized derivative. This script finds every
   `resources.Get "....webp"` line whose immediately-following
   `replace $VAR.RelPermalink "...."` line uses a non-webp extension and
   rewrites that extension to `.webp`. It correctly leaves `.gif`-target Resize
   blocks alone (the `orangewebsite` ad and the Presearch floating-ad variant
   both intentionally resize to `.gif`, not `.webp`).
   ```bash
   .venv/bin/python3 tools/fix_ad_permalink_idiom.py --dry-run
   .venv/bin/python3 tools/fix_ad_permalink_idiom.py
   ```

**Cover partials never need this fix.** `postcover.html`, `opengraph.html`,
`twitter_cards.html`, `relatedcontent.html`, and `articlecarosel.html` all derive
the strip extension dynamically via `$cover.MediaType.SubType` (the actual
resolved file's MIME subtype at build time), so they work correctly regardless of
whether the cover is PNG, JPEG, or WebP. Only the ad partials hardcode the
extension literal, which is why only they needed the idiom fix.

## Verification After Conversion

1. **Integrity scan every `.webp` in the repo** before trusting the batch:
   ```bash
   .venv/bin/python3 -c "
   from PIL import Image
   import os
   prune = {'node_modules','public','.git','.venv','resources','themes','__pycache__'}
   bad = []
   for root, dirs, files in os.walk('.'):
       dirs[:] = [d for d in dirs if d not in prune]
       for f in files:
           if f.lower().endswith('.webp'):
               p = os.path.join(root, f)
               if os.path.getsize(p) == 0:
                   bad.append((p, 'zero-byte')); continue
               try:
                   im = Image.open(p); im.load()
               except Exception as e:
                   bad.append((p, str(e)))
   print('bad:', len(bad))
   for p, r in bad: print(' ', p, r)
   "
   ```
2. **Full local Hugo build**, cold cache, to catch any Resize-time errors the
   integrity scan alone would miss (a valid WebP can still trip a transient
   resize timeout under heavy concurrent load right after a full cache wipe;
   retry once before treating it as a real bug):
   ```bash
   rm -rf resources/_gen public
   nohup sh -c 'npx hugo --gc --minify -D --panicOnWarning' > /tmp/build.log 2>&1 &
   # poll with: tail -f /tmp/build.log ; grep -ci 'error\|panic' /tmp/build.log
   ```
   A cold-cache full-language build with `-D` typically takes 9-10 minutes.
3. **Delete `tools/_webp_conversion_map.tsv`** once the reference rewrite is
   confirmed correct. It is a temporary intermediate file, not a repo artifact.

## `resources/_gen/images` Is Committed to Git

Unlike `resources/_gen/assets` (gitignored), `resources/_gen/images` is
deliberately tracked in this repo as a build-cache/CDN artifact store restored
and saved by `actions/cache` in the CI workflows. After converting source images
to WebP, the old cache entries under the previous filenames become orphaned
(their source no longer exists) and new entries appear under new content
hashes. Commit both the deletions and the additions together with the source
image conversion, following the existing repo convention (see commit history:
"chore(resources): commit missing Hugo image-cache artifacts" /
"chore(resources): prune orphaned Hugo image-cache artifacts").

## Excluded From Conversion (Keep as PNG)

- `static/img/windows11/*`, `static/img/ios/*`, `static/img/android/*` — Windows
  tile icons and iOS touch icons referenced from `static/manifest.json`.
- `static/img/favicon.png`, `apple-touch-icon-192.png`,
  `apple-touch-icon-144-precomposed.png`, `maskable_icon.png`, `512x512.png`,
  `96x96.png` — referenced directly in `layouts/partials/extended_head.html` and
  `static/manifest.json`.
- All `.gif` files (animated content: tutorial screen-recordings, the
  OrangeWebsite ad animation). GIF-to-WebP animated conversion is out of scope
  for this pipeline; only static PNG/JPG/JPEG are converted.

## Upstream Fix: Image-Generation Scripts Already Output WebP

`tools/generate_ad_images.py` and `tools/generate_cover_images.py` (the two
OpenAI/gpt-image-2 pipelines, see `.clinerules/10-cover-image-generation.md` and
`.clinerules/07-ad-cta-guidelines.md`) both already request
`"output_format": "webp"` from the API and save via
`img.save(dest_path, "WEBP", quality=85, method=6)`. No changes were needed
there; this conversion pipeline exists only to clean up the large backlog of
pre-existing raster images that predate those scripts, plus any manually-added
image that bypasses them.

## Restricting Pinterestbot in `robots.txt`

Applied alongside this conversion since Pinterest is a pure image scraper and
was a meaningful share of image bandwidth. `static/robots.txt` is the file
actually served (verified identical to the built `public/robots.txt`);
`layouts/_default/robots.txt` is a Hugo template that is currently unused
(the static file takes priority) but is kept in sync as a safety net in case
`enableRobotsTXT` config ever changes. Pinterest's documented crawler docs
(`pinterest.com/bot.html`) give the real user-agent token as `Pinterestbot`;
`Pinterest` is kept as a second `User-agent:` line since some third-party bot
lists still use that shorter alias. Per Pinterest's own docs, `Crawl-delay`
values above 1 second are silently truncated to 1, so `Crawl-delay: 1` is
already the strictest rate limit robots.txt can express for this bot. Since
Pinterestbot only ever fetches images and cannot render article/page HTML,
its whole `User-agent` block is `Disallow: /` plus `Allow: /img/`, restricting
it to the image directory tree only.
