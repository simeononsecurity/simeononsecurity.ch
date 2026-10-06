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

## Verify and finish

Inspect every generated image visually. Reject invented commands, model versions, claims, unreadable text, or misleading pseudo-benchmarks. Match alt text to the actual image. Run the checker again and verify rendered image paths when rendering is required by rule 08. Commit assets with their referencing pages when a commit is requested; exclude build caches and temporary generation files.

For a deployed replacement, account for rule 13's immutable edge cache. A local file check does not verify live bytes. Purge only when the user's deployment scope authorizes it; otherwise report the affected URL and remaining deployment step. Do not initiate a site-wide purge for a local authoring request.
