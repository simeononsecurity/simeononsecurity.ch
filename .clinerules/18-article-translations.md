# Article Translation Coverage

## Select Pages From Traffic Evidence

- Record the Ahrefs report target, displayed date, location scope, sorting, and
  row limit before selecting articles. Organic traffic estimates differ from
  measured visitor counts and from dashboard summaries.
- Include language subdomains. Group ranking URLs by article bundle before
  counting translation work. Normalize trailing slashes and `www` variants.
- Resolve older URL spellings against source files, explicit slugs, and aliases.
  For example, the operating-systems comparison bundle contains commas which
  are absent from its ranking URL.
- Separate article content from calculators and section listings. Keep the
  ranking evidence and validation output outside committed content.

## Derive Coverage From Configuration

- Read language keys from `[languages.<code>]` in
  `config/_default/config.toml`. Do not use existing filenames as the supported
  language list.
- Store each translation as `index.<code>.md` beside `index.en.md` in the same
  leaf bundle. Preserve the bundle path and routing metadata.
- Check existing files for valid YAML, published status, nonempty translated
  bodies, and missing sections. File existence alone does not establish coverage.
- Compare section structure against English. A translation with far fewer
  headings needs inspection for an older or incomplete source revision.
- When work is split into language batches, derive the complete language list
  again before the final audit. Do not treat a completed batch as full bundle
  coverage. Include every configured code, including `pl` when present.

## Preserve Source Meaning and Structure

- Translate the full body and reader-facing metadata, including image alt text
  and captions. Keep technical names accurate and use Gurmukhi for Punjabi.
- Translate reader-facing `genre` and `tags` values while preserving array order
  and count. Retain product names, model identifiers, and other proper nouns where
  translation would change the reference.
- Check false friends that change evidence-handling meaning. For example,
  “unredacted evidence” means sensitive details remain present, not that evidence
  is unedited or unremediated. Keep such evidence only in the approved private
  location.
- Preserve publication dates, URLs, resource paths, code blocks, inline commands,
  shortcode names, and nontext shortcode parameters. Set `lastmod` when writing
  a new or refreshed translation. For a batch refresh, update and verify
  `lastmod` in every changed locale file. Existing translations can carry
  different older dates, so verify the complete changed-file set instead of
  replacing only one known date value.
- Protect code and markup before automated translation. Validate the exact
  placeholder counts before restoring the protected source text. Restore symbolic
  placeholders by exact token match. When names share prefixes, replace longer tokens
  first or use a token-aware mapping. For example, restore `@academy_home` before
  `@academy`, then compare restored ordered URL targets with the source.
- Use exact phrase or word-boundary substitutions for terminology. Do not
  replace substrings inside other words. For example, matching `laybooks` inside
  `playbooks` changes the correct technical term.
- Require all translation segments to return. Reject truncation, missing keys,
  missing headings, and altered table structure. Never substitute English text
  for a failed translation.
- Preserve existing unrelated edits. Before replacing an older translation,
  compare its current hash with the hash recorded during inspection.
- When a script splits a Markdown file on `---`, validate the split parts before
  writing. With Python `text.split('---', 2)`, part 0 is the prefix before the
  opening delimiter, part 1 is front matter, and part 2 is the body. Assert the
  front matter contains expected keys and validate the complete output in memory
  before writing any file.
- When inserting a missing source section into an existing translation, do not
  search for the English heading text as an insertion anchor. Locate the
  corresponding localized heading or a verified structural boundary in each
  locale, then compare the complete ordered heading sequence with English to
  confirm the section was inserted exactly once.
- When restoring omitted content, compare ordered source and translation links,
  tables, and shortcode sequences before and after insertion. Reuse existing
  references; remove duplicated related-link tables or reference entries, then
  verify every source target appears exactly once in the expected order.
- Validate translated tables by row/column shape and divider structure, not
  literal cell-text equality. Cell text is expected to differ after translation.

## Validate the Result

- Parse every changed file's YAML and compare nontranslated metadata with its
  source. Compare code, link targets, shortcode parameters, and heading levels.
- Check bold and italic markup against the English source. Compare emphasis
  placement and verify paired markers line by line. A matching total marker
  count can still hide an unpaired delimiter in a translated line.
- Inspect emphasis boundaries in the target script. Do not split a word, compound,
  or grammatical particle with Markdown markers, and keep bold spans focused on
  a scannable term or phrase rather than a long sentence.
- Translate source-attribution notes from the current article only. Before
  retaining a citation summary, compare its claim and URL with the English
  source; a note copied from another article can introduce an unrelated claim.
- Check every configured language for every selected bundle after generation.
- Treat language detection as a screening check. English product names and link
  labels distort results on short technical pages. Inspect script usage and
  surrounding prose before replacing a translation flagged by a detector.
- Before approval, screen every reader-facing segment in each locale file for
  English-copy leakage: front matter, headings, paragraphs, table cells, list
  items, captions, and alt text. Compare segments with the English source and
  flag unchanged multiword prose or prose a language detector identifies as
  English. Exclude code, URLs, shortcode syntax, product names, and technical
  identifiers from automatic findings. Review each flag in context, then
  translate any copied reader-facing prose before freezing the hash snapshot.
  Record which locales were screened and how each finding was resolved. File
  presence, script checks, and a detector score do not establish translated
  prose coverage.
- Run `python3 tools/check_translation_english_leakage.py content/articles/<slug>`
  for each finished bundle. For a repository audit, use
  `python3 tools/check_translation_english_leakage.py --all --csv <report.csv>`.
  The checker flags missing locale files, empty bodies, repeated English source
  paragraphs, English stopword dominance, missing expected scripts, and exact
  English reader metadata. Treat each result as a manual-review queue. Inspect
  all reader-facing metadata and prose, resolve confirmed English copy, and
  record any false positives before peer review. Do not approve a bundle solely because the
  checker returns no flags.
- Scan the full translated prose for style violations. A filter requiring Latin
  letters skips paragraphs written entirely in another script.
- Check Punjabi, Bengali, and Hindi for stray letters from other Indic scripts.
  Exclude shared punctuation such as danda from wrong-script findings.
- Render a copied subset with the real Hugo templates for large multilingual
  batches. Verify expected output files exist, then inspect language metadata,
  article text, image paths, and structured data.
- Distinguish automated structural checks from native-speaker review. Translation
  work does not establish a new technical fact-check of the English source.

## Commit and Integrate Reviewed Bundles

- After a bundle passes its assigned peer review and coordinator validation,
  create one local commit containing only that article's translation files.
- Merge each approved bundle into the existing local `master` or `main` checkout
  as soon as validation and worktree state allow. Preserve unrelated changes and
  avoid creating additional worktrees when an existing main checkout is usable.
- Do not push, publish, or deploy unless the user separately authorizes that
  action. A commit or local merge does not imply permission to publish.
