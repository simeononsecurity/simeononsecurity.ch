---
name: sos-content-media
description: "Generate, replace, convert, or audit cover and inline images for SimeonOnSecurity content. Use for missing article images and complete image batches; use the ad-creative skill for advertisements."
---

## Read first

From the repository root, read `.clinerules/08-clinerules-maintenance.md`, then rules 04, 10, and 11. Read rule 13 only for conversion, stale references, or deployed image failures. Follow these canonical rules rather than copying their policies into the skill.

## Scope and audit

Start with the requested pages, not a site-wide regeneration. Inspect `cover`, `coverAlt`, and every body image reference. Run:

```bash
.venv/bin/python tools/check_content_media.py --require-cover content/articles/ARTICLE/index.en.md
```

The checker is read-only. It verifies exact local targets and raster decoding, reports remote media for manual verification, and suggests same-stem alternatives without treating the broken reference as valid. It does not check visual quality, all Markdown syntax, or full Hugo resource resolution. SVG and remote assets require separate inspection. `--generated` additionally requires native 2048×1152 WebP for every selected local raster, so use it only on a wholly generated batch.

## Generate or repair

Inspect `tools/generate_cover_images.py` and use the existing environment and repository pipeline. Never print credentials. Preview the selected article first:

```bash
.venv/bin/python tools/generate_cover_images.py --content-dir articles --slug ARTICLE --force --include-inline-images --dry-run
```

Run the same scoped command without `--dry-run` when generation is needed. `--force` includes missing covers; it does not replace existing images. Correct an obsolete extension when the intended original exists. For a rejected newly generated image, use the exact-asset replacement procedure in rule 10. Do not replace real source photos with generated approximations.

For conversion, inspect the three existing scripts and follow rule 13 in order. Keep reference rewrites scoped to the correct bundle, protect remote URLs, and preserve excluded icons and animation. Never delete Hugo caches as a repair shortcut.

## Shrink an oversized raster ("compress")

"Compress" means the same filename and the same format at fewer bytes. Do not delete the file, convert it to WebP, or redirect its URL, even when a WebP twin exists. Downloads and external links depend on the exact URL. Retire or convert a file only when the user asks for that explicitly.

1. Measure first. For a photographic PNG, a lossless pass (Pillow `optimize=True, compress_level=9`) saves only about 4%, which is not worth committing. Real savings need palette quantization.
2. Work on a scratch copy and compare settings: `pngquant --force --skip-if-larger --speed 1 --quality=<q> --output <tmp> <src>`, then `oxipng -q -o 4 --strip safe <tmp>`. `--quality=90-100` is visually lossless (about 41 dB PSNR, about 60% smaller). `65-85` roughly halves it again (about 37 dB) and risks banding.
3. Compute PSNR against the original with numpy, and look at full-resolution crops of the original and each candidate side by side before choosing. Default to the highest setting with no visible difference.
4. Copy the chosen file over the original. Confirm `file` and Pillow `verify()` show the same dimensions, then commit with the method and PSNR in the body.
5. Tell the user two things. The URL is unchanged and served `immutable`, so the edge keeps the old bytes until that one URL is Custom-Purged (rule 13). Git history still holds the old blob, so the repo does not shrink without a history rewrite they must approve.

## Re-host externally hosted images

1. Build a manifest of every distinct remote URL and each file and line that uses it. In a translated bundle, the locale files share the same images.
2. Download each URL once. Confirm an image content type. Leave a dead URL in place and report it rather than substituting another image.
3. Convert per rule 13, store the result in the page's own bundle with a descriptive name, and rewrite the EN and locale references to a bare-filename `{{< figure >}}` that keeps the existing alt, caption and link.
4. Verify from the commit diff:
   - every removed line contained the remote host;
   - every added line is a figure;
   - every local `src` resolves;
   - every added file decodes;
   - no raster originals are left behind;
   - `rg` finds no remaining references to the host.
5. Report alt text that is only a placeholder, such as "Illustration related to <heading>", as a follow-up instead of silently rewriting it.

## Verify and finish

Inspect every generated image visually. Reject invented commands, model versions, claims, unreadable text, or misleading pseudo-benchmarks. Match alt text to the actual image. Run the checker again and verify rendered image paths when rendering is required by rule 08. Commit assets with their referencing pages when a commit is requested; exclude build caches and temporary generation files.

For a deployed replacement, account for rule 13's immutable edge cache. A local file check does not verify live bytes. Purge only when the user's deployment scope authorizes it; otherwise report the affected URL and remaining deployment step. Do not initiate a site-wide purge for a local authoring request.
