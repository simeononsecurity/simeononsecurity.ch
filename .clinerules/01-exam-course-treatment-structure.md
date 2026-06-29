# Exam Course "Treatment" Structure

When asked to build (or extend) a certification course on this Hugo site, produce a complete
**four-piece treatment**. Use the existing CompTIA SecOT+ (`SOT-001`) and SecAI+ (`CY0-001`)
sets as the canonical reference for every convention below.

Pick a short, lowercase, hyphenated `<exam>` slug (for example `secot-plus`, `secai-plus`,
`cysa-plus`). Reuse it consistently across all four pieces.

## The Four Pieces

1. **Study course (one page per exam domain)**
   - Path: `content/<exam>/<domain-slug>/index.en.md`
   - One file per official exam domain. `<domain-slug>` is the domain title, lowercased and hyphenated.
   - Cover convention: `cover: "/img/cover/comptia-<exam>-<domain-slug>.webp"`.

2. **Start page (the course hub)**
   - Path: `content/<exam>-start/index.en.md`
   - Links out to every domain page and to the practice test.

3. **Practice test**
   - Page: `content/<exam>-practice-test/_index.en.md` — front matter only, with `layout: "<exam>_quiz"`.
   - Layout: `layouts/section/<exam>_quiz.html` — clone an existing quiz layout via `sed` (see below).
   - Question bank: `static/quiz-dicts/<examdict>.json` — served at
     `https://simeononsecurity.com/quiz-dicts/<examdict>.json`.

4. **Listing links**
   - Add the new course + practice test to **both**:
     - `content/practice-tests/index.en.md` (table row + `###` heading entry)
     - `content/courses-and-playbooks/index.en.md` (course list + practice-test list)
   - `replace_in_file` has silently failed on these two listing pages before. **Always edit them
     with `write_to_file` (full rewrite), then verify with `grep -c "<exam>"`.**

## Front Matter Conventions

All content pages use this front-matter shape (TOML-style keys in YAML front matter):

- `title`, `date` (use `2025-01-01` for course pages), `toc: true`, `draft: false`
- `description` — one to two skimmable sentences naming the exam code and what the page covers
- `genre: [...]` and `tags: [...]` — arrays seeded with the exam name, code, and key topic terms
- `cover`, `coverAlt`, `coverCaption`

The **practice-test** `_index.en.md` carries only front matter (no body) and adds:

```yaml
sitemap:
  priority: 0.3
layout: "<exam>_quiz"
```

## Course Domain Page Skeleton

Each `content/<exam>/<domain-slug>/index.en.md` body follows this order:

1. Return link header:
   `#### [Click Here to Return To the CompTIA <Exam> Course Page](/<exam>-start/)`
2. **Bold intro paragraph** that states the domain's exam weight percentage and why it matters.
   Add one *italic* study-priority callout sentence.
3. `##` topic headings, one per major objective grouping. Mix comparison tables and bullet lists.
4. `## Next Steps` closing section linking the next sibling domain page(s) and the start page.

## Start Page Skeleton

`content/<exam>-start/index.en.md` body follows this order:

1. **Bold intro paragraph** naming the exam code and audience, plus an *italic* experience-recommendation line.
2. A **domain weight table** (`Domain | Title | Exam Weight`).
3. An **`**Exam details:**`** line describing question types and a reminder to confirm specifics on CompTIA's site.
4. `## Resources` — bulleted list of related courses, the practice test, official objectives, and the career playbook.
5. One `## Domain N: Title (X%)` section per domain, each with a `### [Title](/<exam>/<slug>/)` link and bullet summary.
6. Closing paragraph linking the practice test and `/courses-and-playbooks/`.

## Quiz Layout Cloning

Never hand-write the quiz layout. Clone a working one and rename every reference:

```bash
sed -e 's/<srcdict>/<newdict>/g' \
    -e 's/<SrcLabel> Quiz/<NewLabel> Quiz/g' \
    layouts/section/<src>_quiz.html > layouts/section/<exam>_quiz.html
```

After cloning, verify with `grep`:
- The new dict filename appears (it is referenced twice: JSON-LD `resources.Get` + the `fetch` URL).
- The gtag `event_category` label (for example `'SecOT+ Quiz'`) is correct.
- Zero leftover references to the source exam.

## Build Notes

- Adding a new treatment adds content pages, so a full build is the real test:
  `npx hugo --gc --minify -D` (multilingual build takes roughly 8+ minutes).
- `execute_command` times out at 30s. Launch long builds in the background and poll a log file
  for `Total in`:
  `nohup npx hugo --gc --minify -D > /tmp/<exam>_build.log 2>&1 &`
- The quiz JavaScript only activates in the production CI environment. **Locally, practice-test
  pages render as plain section list pages. That is expected, not a bug.**
