# Inline Image Strategy — Breaking Up Walls of Text

This rule documents when, where, and how to add inline images to existing articles
and new content on this site. The goal is to prevent walls of text and give readers
a visual anchor every 400 words or fewer.

---

## The Core Rule: No 400-Word Desert

Per `.clinerules/03-content-writing-style.md`: any stretch of 400 words or more
without a `{{< figure >}}`, `{{< youtube >}}`, table, or code block is a wall.
Break it up.

**Quick scan method**: after drafting or auditing an article, search for `##`
headings that have no visual element before the next `##`. If the prose between
two headings is more than 400 words with no visual element, add a `{{< figure >}}`.

---

## When to Add an Inline Image

Add a `{{< figure >}}` at a section break when any of these are true:

- **Concept is structural** — a system has components, layers, or a flow that a
  diagram communicates faster than text. Example: a surveillance camera capturing
  three simultaneous signal types (plate, Bluetooth, TPMS).
- **Comparison exists** — two versions, two modes, or two states that benefit from
  a side-by-side visual. Example: Proxmox VE 8 vs VE 9 component versions.
- **Process has steps** — an upgrade path, installation flow, or decision tree.
- **Abstract concept needs grounding** — a policy argument, legal framework, or
  threat model that benefits from a summary diagram.
- **400-word rule triggered** — any section that exceeds the word limit with no
  other visual break.

Do not add a figure just to fill space. The image must illustrate the section it
follows. A caption-less stock photo that vaguely relates to the topic is worse than
no image.

---

## Where to Place the Figure

**After the section prose, before the next `##` heading.** Never in the middle of
an explanation — the code-first principle applies to images too. Write the text,
then place the figure as a visual summary or anchor.

Preferred placement patterns:

```markdown
## Section Title

Prose explaining the concept...

{{< figure src="concept-diagram.webp" alt="Descriptive alt text" >}}

______

## Next Section
```

For very long sections (700+ words), place the figure at roughly the midpoint
rather than the end, so the reader gets a visual break before reaching the bottom.

---

## How to Name Image Files

Image files live in the page bundle directory alongside `index.en.md`.

**Naming rules:**
- Lowercase, hyphenated slug. No spaces, no underscores, no uppercase.
- Descriptive enough that the filename alone tells you what the image shows.
  `flock-tpms-bluetooth-surveillance.webp` is good. `image1.webp` is not.
- Use `.webp` extension for all AI-generated images (the generator outputs WebP).
- Keep names under 60 characters.
- Do not reuse the article slug as the image name — that collides with the cover
  image naming in `assets/img/cover/`.

**Examples of good names:**
- `rayhunter-heuristics-overview.webp`
- `proxmox-ve-8-to-9-component-changes.webp`
- `flock-tpms-bluetooth-surveillance.webp`
- `alpr-data-sharing-network-diagram.webp`
- `imsi-catcher-threat-actor-tiers.webp`

---

## The `{{< figure >}}` Shortcode

Always use the site shortcode. Never use raw `![alt](src)` or `<img>` tags.

**Minimum required form:**
```text
{{< figure src="descriptive-name.webp" alt="Plain-English description of what is shown" >}}
```

**With caption:**
```text
{{< figure src="descriptive-name.webp" alt="Plain-English description" caption="One-line caption that adds context the surrounding prose does not already provide" >}}
```

`alt` text rules:
- Describe what is visually present, not what the image is called.
- Start with a noun phrase: "Diagram showing...", "Screenshot of...", "Chart comparing..."
- 10–25 words is the target range.
- Do not repeat the surrounding heading or caption word-for-word.

`caption` rules:
- Use a caption only when it adds information the alt text and prose do not cover.
- One sentence. No period at the end.
- Skip the caption if the surrounding prose already explains the image fully.

---

## Generating Missing Images

When you add a `{{< figure src="new-image.webp" ... >}}` and the file does not
exist on disk, the AI pipeline in `tools/generate_cover_images.py` will generate
it automatically.

### Run the generator

```bash
# Dry run first — see what is missing without API calls
.venv/bin/python tools/generate_cover_images.py \
  --content-dir all --include-inline-images --dry-run

# Generate missing inline images only (skip covers already present)
nohup .venv/bin/python tools/generate_cover_images.py \
  --content-dir all --include-inline-images --inline-only \
  > /tmp/inline_gen.log 2>&1 &

# Monitor
tail -f /tmp/inline_gen.log
```

The script reads 700 chars of surrounding text around each missing image reference
to generate a contextually accurate prompt. The closer the `{{< figure >}}` is to
the content it illustrates, the better the generated image will be.

### How the generator finds images to create

The generator scans every `{{< figure >}}` and `![](...)` reference. If the target
file does not exist in the page bundle, `static/`, or `assets/`, it generates one.

It respects stem-matching: if `foo.png` exists, a reference to `foo.webp` or
`foo.jpg` will NOT trigger a new generation (the same-stem file satisfies it).
See `.clinerules/10-cover-image-generation.md` for the full stem-matching details.

### After generation

Images are saved to the page bundle directory alongside `index.en.md`. Verify them
visually before committing. The AI occasionally generates off-topic images when the
surrounding context is ambiguous — regenerate with `--force` and `--slug <slug>` if
the output does not match the alt text.

```bash
# Regenerate one article's inline images
.venv/bin/python tools/generate_cover_images.py \
  --content-dir articles --slug my-article-slug \
  --include-inline-images --inline-only --force
```

---

## Auditing an Existing Article for Walls of Text

Use this checklist when auditing any article:

1. Open the article.
2. Scan each `##` section. Count the words between the heading and the next heading
   (or end of file).
3. Note every section with 400+ words and no `{{< figure >}}`, `{{< youtube >}}`,
   table, or fenced code block.
4. For each identified wall:
   - Decide what concept in that section would benefit from a visual.
   - Write a descriptive filename slug.
   - Insert `{{< figure src="slug.webp" alt="..." >}}` at the end of the wall or
     at the natural midpoint.
5. Run the generator to create the missing files.
6. Commit article changes and generated images together in one commit.

---

## Git Workflow

Commit article changes and generated images together. Do not commit a `{{< figure >}}`
reference without the corresponding image file in the same commit — that creates a
broken reference in the build.

```bash
git add content/articles/<slug>/index.en.md
git add content/articles/<slug>/*.webp
git commit -m "content(<slug>): add inline images to break wall-of-text sections"
```

If multiple articles are updated in one session, group the commit by article or by
batch if all images were generated in a single pipeline run.

---

## When NOT to Add an Image

- The section already has a table that serves as a visual anchor.
- The section is a code-heavy tutorial with multiple fenced blocks — code blocks
  count as visual breaks.
- The section is fewer than 300 words.
- The concept is purely textual (a policy argument, a list of references) with no
  structural component a diagram would illuminate.
- The article already has a `{{< youtube >}}` embed covering the same concept.

One well-placed image per section is the target. Do not add multiple figures to a
single `##` section unless each image illustrates a genuinely different sub-concept.

---

## Summary Checklist

Before publishing any article audit pass:

- [ ] Every `##` section checked for 400-word deserts
- [ ] Each new `{{< figure >}}` has descriptive `alt` text (10–25 words)
- [ ] Image filenames are lowercase-hyphenated slugs, under 60 characters
- [ ] Generator run, output verified visually
- [ ] No stem-conflict with existing images (`.png` exists for a `.webp` reference)
- [ ] Article changes and image files committed together
