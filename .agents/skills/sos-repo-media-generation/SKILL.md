---
name: sos-repo-media-generation
description: "Use the repository's bundled scripts to generate, convert, and validate article media. Apply when a page needs a cover or inline image generated or when generated media needs verification."
---

# Sos Repo Media Generation

Use this skill for repository-owned article media. Keep the workflow scoped to the requested page and preserve unrelated working-tree changes.

## Before changing files

1. Read the applicable `.clinerules/` files, especially the cover and inline-media rules.
2. Inspect the target article and run the read-only media check:

   `.venv/bin/python tools/check_content_media.py --require-cover content/articles/SLUG/index.en.md`

3. Inspect the selected generator before using it. Do not invent a new image pipeline when an included script already covers the task.

## Cover generation

Use `tools/generate_cover_images.py` for article covers. Start with a scoped dry run:

`.venv/bin/python tools/generate_cover_images.py --content-dir articles --slug SLUG --force --dry-run`

If the dry run selects the intended page, run the same command without `--dry-run`. The script asks a prompt model to produce a page-specific image prompt and then generates a native 2048x1152 WebP cover under `assets/img/cover/`. It also patches `cover`, `coverAlt`, and `coverCaption` in the article front matter.

Use `--include-inline-images` only when the request includes missing inline figures. Do not regenerate an existing cover unless the user asks for replacement or the current cover is broken and `--force` is appropriate.

## Other bundled media tools

- `tools/convert_images_to_webp.py` converts source images to WebP. Inspect its help and scope input paths before running it.
- `tools/optimize-images.py` optimizes existing image assets. Use only for an explicit optimization request.
- `tools/check_content_media.py` audits exact local references, front matter, figure attributes, and generated cover dimensions.

Do not use generated output as a substitute for source inspection. Do not expose API keys or `.env` contents.

## Verification

After generation:

1. Inspect the generated file with an image viewer.
2. Run the checker with the generated-image contract:

   `.venv/bin/python tools/check_content_media.py --require-cover --generated content/articles/SLUG/index.en.md`

3. Confirm the front matter points to the exact generated asset and inspect `git status --short` for scope.
4. Run the relevant Hugo validation when the article or asset pipeline requires rendered verification.

Report the exact generated path, checker result, and any remaining manual checks. Do not claim a successful generation when the script stopped before writing the file.
