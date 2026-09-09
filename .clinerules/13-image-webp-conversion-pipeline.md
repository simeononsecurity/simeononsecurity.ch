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

## Purge Cloudflare Cache After Deleting/Renaming Images (Critical)

`netlify.toml` sends `Cache-Control: public, immutable, s-maxage=31536000,
max-age=31536000` on `/img/*` and every `.png`/`.jpg`/`.jpeg`/`.webp` response.
**"Immutable" tells Cloudflare's edge (and browsers) it never needs to
revalidate that URL, so it will keep serving the old bytes for up to a full
year even after the origin file is deleted, unless the cache is explicitly
purged.**

This was confirmed as a real, live bandwidth-waste bug 2026-09: after
`741bfbe84e4` converted ~928 PNG/JPG/JPEG files to WebP and deleted the
originals, Cloudflare kept serving stale copies of at least one deleted file
(`installedantenna.png`, originally 13.3MB) at close to its pre-conversion
size on repeat requests, weeks after the source file was gone from the repo
and Netlify origin. The dead URL was not falling through to a small 404 page,
it was still resolving to the old cached asset.

**After every image conversion, rename, or deletion pass (WebP conversion,
cover regeneration, ad-image regeneration), purge the affected paths from
Cloudflare:** Cloudflare dashboard → Caching → Configuration → Purge Cache →
Custom Purge (list the specific old URLs), or Purge Everything for a
site-wide conversion pass like this one. Do not assume deleting the file from
the repo and redeploying is sufficient; the edge cache is a separate
long-lived store from the origin.

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

## 2275 Cover References Left Pointing at Deleted Raster Files (Found and Fixed 2026-09)

A live symptom report ("this article's cover image is missing:
`/articles/the-ideal-ubiquiti-unifi-networking-setup-both-simple-and-advanced/`") traced
back to the original `741bfbe84e4` WebP conversion commit itself, not a later regression.
`convert_images_to_webp.py` correctly deleted the `.png`/`.jpg`/`.jpeg` and created the
`.webp`, but `rewrite_webp_references.py`'s global "cover" category replacement (a plain
`dict[old_string] = new_string` built from the TSV map, applied via string substitution
across every text file) silently failed to rewrite 2275 `cover:` front-matter lines across
17 languages (222 unique English articles/sections, mirrored across a subset of
translations each). Since `postcover.html`'s `resources.Get` returns `nil` for a path that
no longer exists on disk, every affected page fell through to an empty
`<figure class="post-cover"></figure>` with **no image at all**, plus a dead `og:image` URL,
and the build produced zero warnings or errors, exactly the "invisible until a human
reports it" failure pattern described in
`.clinerules/15-hugo-internal-template-overrides-and-relative-urls.md`.

**Root cause of the miss was never fully isolated** (the original TSV map and script run
logs no longer exist to diff against), but the fix does not require knowing why the
original rewrite pass skipped these 2275 lines: every single one of them already had a
same-stem `.webp` file sitting on disk (the real converted image was never lost, only the
front-matter *pointer* to it), so the fix is a pure text substitution, not an image
regeneration. Confirmed this holds for **all** 2275 broken references, in every language,
with zero exceptions, before writing a single byte.

**Detection query** (run this after any bulk image rename/conversion, not just this one):

```python
import os, re, glob
broken = []
for md in glob.glob('content/**/index.*.md', recursive=True) + glob.glob('content/**/_index.*.md', recursive=True):
    with open(md, errors='ignore') as f:
        text = f.read()
    m = re.search(r'^cover:\s*"?(/img/cover/[^"\n]+)"?', text, re.M)
    if not m:
        continue
    cover_path = m.group(1).strip().strip('"')
    if not os.path.exists('assets' + cover_path):
        broken.append((md, cover_path))
print(len(broken))
```

**Fix approach**: for each broken reference, check whether a same-stem `.webp` exists
(`os.path.splitext(basename)[0] + ".webp"` in `assets/img/cover/`). If yes, and the exact
old path string appears **exactly once** in the file (verified per-file before writing, to
guarantee the substitution cannot touch an unrelated occurrence), rewrite the extension in
place. If no same-stem `.webp` exists, that page needs real image regeneration via
`tools/generate_cover_images.py --force`, not a text fix — none of the 2275 hit that case
this time, but do not assume that will always be true.

**A second, unrelated bug with the identical symptom was found in the same audit**: all 16
non-English translations of one 2026 article
(`content/articles/flock-cameras-public-safety-or-surveillance-2026/`) had a `cover:` value
derived from the article's URL slug (a filename that was never actually generated) instead
of the real English cover image, a translation-tool (glotta) slug/cover mismatch with no
connection to the WebP conversion. **Lesson: "missing cover image" has more than one
possible root cause on this site.** Always run the detection query above fresh rather than
assuming every broken cover reference traces back to the same historical commit; compare
the broken translation's `cover:` value against its English sibling's `cover:` value to
tell the two failure modes apart (WebP-conversion miss: broken ref matches a real file with
a different extension; glotta slug mismatch: broken ref matches neither the English cover
nor any real file, but a slug-derived filename that was never generated).

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
it to the image directory tree only. Updated 2026-09 to also add `pinterest.com`
and `pinterest.com/` as explicit `User-agent` tokens in both `static/robots.txt`
and `layouts/_default/robots.txt`, since some Pinterest-affiliated fetchers
(e.g. link-preview/unfurl requests triggered when a user pastes a URL into
Pinterest) have been observed identifying with the bare domain rather than
the `Pinterestbot` product token.
