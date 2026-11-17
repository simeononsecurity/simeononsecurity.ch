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
  translation would change the reference. Screen every identical source tag and
  genre value, including single-word values, in inline and block-style YAML lists
  for manual review. Translate reader-facing taxonomy terms and record any
  proper-name exception. Preserve the source tag and genre counts. The leakage
  checker flags `taxonomy_count_mismatch`; inspect the report's source/target
  counts, then compare value order manually because translations change values.
- Check false friends that change evidence-handling meaning. For example,
  “unredacted evidence” means sensitive details remain present, not that evidence
  is unedited or unremediated. Keep such evidence only in the approved private
  location.
- Translate security terms by their established meaning, not by a literal
  cognate. In Catalan, do not render phishing as `pesca` alone; retain
  `phishing` or use a recognized descriptive phrase, and confirm the wording
  still refers to credential theft or impersonation attacks.
- Use the established target-language acronym for laws and regulatory regimes.
  In French, use `RGPD` for `GDPR`; introduce `GDPR` once in parentheses only
  when the English acronym helps identify sources, then use `RGPD` consistently
  in reader-facing metadata and prose.
- Preserve publication dates, URLs, resource paths, code blocks, inline commands,
  shortcode names, and nontext shortcode parameters. Set `lastmod` when writing
  a new or refreshed translation. For a batch refresh, update and verify
  `lastmod` in every changed locale file. Existing translations can carry
  different older dates, so verify the complete changed-file set instead of
  replacing only one known date value.
- Before broad phrase replacements, protect or recheck fixed asset paths such as
  `cover`. Replacing a translated term can also mutate a lowercase filename.
  Compare every fixed path with the English source after edits.
- Protect code and markup before automated translation. Validate the exact
  placeholder counts before restoring the protected source text. Restore symbolic
  placeholders by exact token match. When names share prefixes, replace longer tokens
  first or use a token-aware mapping. For example, restore `@academy_home` before
  `@academy`, then compare restored ordered URL targets with the source.
- Use exact phrase or word-boundary substitutions for terminology. Do not
  replace substrings inside other words. For example, matching `laybooks` inside
  `playbooks` changes the correct technical term.
- Protect Markdown link destinations before running any phrase-replacement
  script. A terminology match inside a URL path, query, or anchor is part of the
  destination, not reader-facing prose. After restoring translated labels,
  compare every ordered URL target and its source-aligned sentence with English.
- Require all translation segments to return. Reject truncation, missing keys,
  missing headings, and altered table structure. Never substitute English text
  for a failed translation.
- Never copy or rename `index.en.md` into a locale filename as a placeholder,
  and never keep a partially translated file when a translation call fails.
  Write generated translations to a temporary path first. Before moving one into
  the content bundle, verify that its title, opening, and every reader-facing
  section contain target-language prose. If any segment is missing or still
  source English, leave that locale marked incomplete in the work report and
  do not create or approve its locale file.
  Treat a locale filename as a claim that the file contains a complete
  translation, not as an in-progress marker. Keep drafts and failed or
  incomplete candidates outside `content/articles/`. Before adding or replacing
  a locale file, screen the temporary candidate against the English source for
  copied paragraphs, sentences, spans, metadata, and English-dominant prose.
  Manually inspect every finding. If the candidate still contains untranslated
  reader-facing English, do not move it into the bundle; report the locale as
  missing until the complete translation passes this gate.
  Compare normalized article bodies for an exact English copy even when front
  matter differs. Inspect short paragraphs individually, since English-only
  sections can evade long-paragraph thresholds. A locale extension marks final
  translated content, never a placeholder or progress state.
  Treat `tools/check_translation_english_leakage.py --fail-on-english-fallback`
  as a blocking gate on the temporary candidate bundle before moving it into
  `content/articles/`, and run it again against the in-tree bundle before peer
  review or commit. A nonzero result means the locale file stays outside the
  article bundle until each high-confidence English fallback is translated and
  the gate passes. Review all other checker findings manually, since copied
  headings, labels, code examples, and citation titles can be valid exceptions
  or reader-facing English that still needs translation. Record unresolved
  findings in the external batch report; do not treat a translated body as
  approval for untranslated reader-facing sections.
  For each locale, include a source-aligned review record for the title,
  description, opening, every section, and every reader-facing example or
  caption. The peer reviewer must verify each record against the frozen file
  hashes. Keep the locale incomplete until all reader-facing prose is in the
  target language or a specific retained English term is documented as a
  proper name, official source title, fixed identifier, command, or literal
  value. A filename, `lastmod`, script ratio, or clean strict-checker result
  alone never establishes translated coverage.
- Preserve existing unrelated edits. Before replacing an older translation,
  compare its current hash with the hash recorded during inspection.
- When a script splits a Markdown file on `---`, validate the split parts before
  writing. With Python `text.split('---', 2)`, part 0 is the prefix before the
  opening delimiter, part 1 is front matter, and part 2 is the body. Assert the
  front matter contains expected keys and validate the complete output in memory
  before writing any file.
- Keep Markdown body line indexes relative to the body returned by the split.
  Do not apply a body line number to the whole file, since front matter shifts
  the target. Before a batch edit, assert each intended phrase occurs once and
  inspect the rewritten lines before writing.
- When inserting a missing source section into an existing translation, do not
  search for the English heading text as an insertion anchor. Locate the
  corresponding localized heading or a verified structural boundary in each
  locale, then compare the complete ordered heading sequence with English to
  confirm the section was inserted exactly once.
- Before restoring a suspected missing sentence, align the source and translated
  segments and check whether the meaning already appears in translated wording.
  Do not use absence of one proposed translated sentence as proof that the source
  meaning is missing. Insert only the omitted idea or qualifier, then review the
  complete translated paragraph for repeated claims.
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
  Do not count underscore-only horizontal-rule lines as emphasis.
- Treat source-level marker counts as insufficient. After rendering each changed
  locale, inspect the generated article prose outside `pre` and `code` elements
  for literal Markdown emphasis delimiters: `*`, `**`, and `__`. Valid emphasis
  renders as `<em>` or `<strong>` and leaves no delimiters in prose. Treat
  unescaped delimiters as a failed render check until reviewed and fixed. Review
  intentional escaped literal asterisks separately. Compare the rendered
  `<strong>` and `<em>` spans with the source meaning, then record this check per
  locale in the review report.
- Inspect emphasis boundaries in the target script. Do not split a word, compound,
  or grammatical particle with Markdown markers, and keep bold spans focused on
  a scannable term or phrase rather than a long sentence. Review Japanese and
  Chinese boundaries manually; the automated split-word check skips those
  scripts because they do not use spaces between words.
- Translate source-attribution notes from the current article only. Before
  retaining a citation summary, compare its claim and URL with the English
  source; a note copied from another article can introduce an unrelated claim.
- Check every configured language for every selected bundle after generation.
- Treat language detection as a screening check. English product names and link
  labels distort results on short technical pages. Inspect script usage and
  surrounding prose before replacing a translation flagged by a detector.
  Translate each descriptive link label in the sentence where it appears, and
  adjust nearby articles, prepositions, case, gender, number, and word order to
  fit the translated label. Read the complete sentence after each label change;
  a translated label can still leave the sentence ungrammatical. Keep the link
  inside the source-aligned sentence or list item; preserving its target and
  order does not catch a link moved after the sentence it completes.
- Before approval, screen every reader-facing segment in each locale file for
  English-copy leakage: front matter, headings, inline link labels, paragraphs,
  table cells, list items, captions, and alt text. Compare segments with the English source and
  flag unchanged multiword prose, identical headings including short headings,
  and English word fragments left in mixed-language headings,
  or prose a language detector identifies as English. Exclude code, URLs,
  shortcode syntax, product names, and technical identifiers from automatic
  findings. Treat short heading
  matches as a manual-review queue because brands, acronyms, and cognates often
  remain unchanged. Also compare Markdown link labels by
  their unchanged target and order. Flag identical descriptive labels of two
  or more words for manual review, even when surrounding paragraph prose differs.
  The checker also flags an unchanged multiword source label embedded inside a
  longer target label. It also flags generic unchanged one-word English labels
  such as `here`, `click`, `download`, and `documentation` for manual review.
  Translate generic link wording in the target language; retain a one-word label
  only when context confirms a product, organization, fixed identifier, or
  official name. Inspect these matches in context and translate copied
  descriptive wording, while retaining official titles, product names, and
  fixed identifiers when context supports them.
  Review each flag in context, then translate copied reader-facing prose before
  freezing the hash snapshot.
  Treat every unexplained `English_reader_heading_copy` finding as an approval
  blocker. An official English term does not make a descriptive heading
  translated: localize the heading wording and retain the acronym or fixed
  designation. Keep the full English expansion only where the initial
  definition needs it, paired with its localized explanation. Record the exact
  locale and disposition for every retained unchanged heading in the author
  report, and require the peer reviewer to check those dispositions. A zero
  `--fail-on-english-fallback` count does not clear heading findings because
  that strict gate does not block them.
  Compare unchanged descriptive table cells directly with the source. The
  leakage checker queues copied descriptive cells, including common
  single-word labels, for manual review. Translate
  headers, method names, and explanatory labels; preserve product/model names,
  identifiers, commands, and numeric results when they are fixed data.
  Review each unchanged table-cell flag in context and record the reason
  when you preserve it as a product name, status, identifier, or fixed value.
  Treat every `English_reader_table_cell_copy` result as an approval blocker until
  you inspect the source-aligned table row. Translate copied descriptive text,
  and document the precise reason for every retained product name, status,
  identifier, or fixed value. After editing, rerun
  `tools/check_translation_english_leakage.py` on the affected article bundles
  and recheck the `copied_english_table_cells` report column before approval.
  A locale filename, nonempty body, expected-script sample, or low file-wide
  English ratio does not establish translated coverage. Before approval, inspect
  the title, description, opening, every section, and reader-facing examples in
  each locale. If any segment is still English source prose or a section has no
  translated reader-facing content, return `CHANGES REQUIRED`; do not freeze,
  commit, or integrate that locale until it is translated and re-reviewed.
  Retain English only when the exact phrase is a product or organization name,
  fixed identifier, source title, command, citation title, or literal sample
  value, and record the reason in the review report. A mixed-language paragraph
  with copied English clauses is still a translation defect.
  Compare sentence-sized segments and unchanged source spans of eight or more
  words as well as full paragraphs. A translated paragraph can still contain
  English clauses between localized text, so a low English-word ratio does not
  clear the paragraph. The checker also queues unchanged five-to-seven-word
  spans with English stopwords, including short clauses next to preserved legal
  or product names. Translate copied prose and connectors while retaining an
  official name when appropriate.
  Screen each paragraph separately for English stopword dominance as well as
  scanning the full article. A mostly translated article can hide a fully
  English paragraph in its overall ratio. Treat each paragraph-level flag as a
  manual-review item, inspect it against the English source, and translate
  reader-facing English prose before approval. Preserve named entities, fixed
  identifiers, literal data, and runtime output when context confirms them.
  The leakage checker screens paragraphs with 10 or more Latin-word tokens.
  In Arabic, Bengali, Hindi, Japanese, Punjabi, Russian, and Chinese, paragraphs
  with at least 15 Latin-word tokens use a 0.25 English-stopword ratio threshold
  regardless of nearby target-language characters. Other paragraphs under 30
  tokens use a 0.35 threshold; paragraphs with 30 or more tokens use 0.28.
  These thresholds create a review queue, not an automatic language verdict.
  For Arabic, Bengali, Hindi, Japanese, Punjabi, Russian, and Chinese, assess
  English stopword density among Latin-word tokens without letting nearby
  target-language characters suppress the flag. A translated sentence can still contain
  a copied English clause. Review flags in context and retain Latin product names
  when they are names rather than prose.
  For sentences containing inline links, compare the surrounding sentence with
  each link replaced by a neutral placeholder. This catches copied English
  prose whose remaining word count falls below the normal span threshold after
  link labels are removed. Translate the sentence around product names while
  preserving the names and their targets.
  When a source repeats a destination, preserve each link occurrence in its
  original translated sentence, list item, step, or table cell. Matching the
  total URL count and order does not prove correct placement; compare each
  occurrence with its source context so a duplicate link does not migrate to a
  different claim.
  Record which locales were screened and how each finding was resolved. File
  presence, script checks, and a detector score do not establish translated
  prose coverage.
- Inspect fenced examples separately. A `text`, `plaintext`, or `markdown`
  template, form, sample dialogue, or Markdown document remains reader-facing
  prose. The leakage checker includes these fence types and flags unchanged
  examples copied from English. It excludes
  executable and other fenced code. Translate labels and explanatory text in
  reader-facing fences while preserving placeholders and syntax. Keep structured
  evidence such as MAC/OUI records, hashes, and literal data values unchanged.
  These values are not English prose even inside a `text` fence. Exclude code,
  literal commands, and data-only examples from prose review.
  Preserve literal runtime diagnostics and expected validation output exactly.
  Translate explanatory labels or surrounding prose, but do not translate fixed
  output such as a permission error or a required `PASS:` result.
  Inspect executable fences for reader-facing comments and natural-language
  strings as well. Translate comments and example text such as a commit subject
  while preserving valid command syntax. The checker covers Azure CLI
  (`azurecli`/`azcli`) comments and common human-readable `Description`,
  `Message`, `Title`, and similar assignments in executable fences. Its strict
  gate blocks copied code prose with at least five words and English stopword
  density of 0.16 or higher. Keep literal runtime output, identifiers,
  paths, and command names unchanged. The checker screens comments and common
  output calls in shell and PowerShell (`powershell`/`pwsh` fences), Python,
  JavaScript/TypeScript, C/C++, Java, C#, Go, Rust,
  Swift, Kotlin, PHP, Lua, Scala, and Groovy. It also screens visible text and
  accessibility labels in fenced HTML, including single-word labels. Treat an
  unchanged Python module, class, or function docstring as reader-facing prose
  and translate it while preserving the code structure. The checker screens
  docstrings in parseable Python fences. Treat an
  unchanged comment or example string as a manual-review flag, not as executable
  syntax to ignore. Exempt fixed diagnostics and identifier-only values from
  translation. Review output-string findings in context, preserve fixed runtime output, and record
  the reason when retaining English text the checker flags. Do not exempt generic
  status words such as `start`, `stop`, `ready`, or `done` automatically. Review
  those strings in context because they can serve as visible instructions or labels.
  Manually inspect every human-readable value in an executable example, even
  when the value is shorter than the strict gate threshold or uses an
  unsupported file format. For example, translate a generic Packer
  `image_description` value such as `My custom image` and any prose that repeats
  it, while preserving valid JSON or HCL syntax. A passing strict scan does not
  clear short reader-facing values.
  When an example prompt names exact English words or sentences as its target,
  keep those literal strings identical in every locale and translate the
  surrounding instructions. Compare any quoted removal or matching rule with
  the corresponding text in the example; preserve order and duplicate entries.
  An unlabeled code fence can still contain reader-facing labels or explanatory
  placeholders alongside literal data. The checker reports unchanged prose lines
  from unlabeled fences as `copied_unlabeled_fence_line`; translate those labels
  and placeholders while keeping addresses, model identifiers, and literal values.
  Numeric content does not make a line data-only: cost explanations, percentages,
  quantities, and numbered timeline phases remain reader-facing prose. Review
  these lines even when they contain currency symbols or arithmetic. Exclude only
  data-only rows, fixed output, commands, and identifiers with a specific reason.
  Arrows can connect reader-facing decision labels or instructions. Translate the
  words around an arrow; retain a line unchanged only when it is an identifier/path
  mapping or literal data, and record that reason.
  Match each code fence language to the syntax shown. For example, `#` comments
  belong in a PowerShell fence, not a `cmd` fence. A wrong fence label can hide
  comments from the language-aware leakage checker and misrepresent how commands
  run.
  Inspect YAML block scalars under `name:` and `msg:` line by line, including
  continuation lines, and translate all reader-facing text. The checker scans
  these fields but cannot establish whether their wording is appropriate. It is not a language
  parser, so manually inspect user-facing strings and markup in every other
  executable fence, including template literals, UI labels, and generated sample text.
  Compare individual lines inside `text`, `plaintext`, and `markdown` fences as well as full
  examples. A localized sample can still contain copied English field labels or
  short instructions that a whole-block comparison misses. Translate those
  lines while preserving paths, commands, placeholders, and structured values.
  Treat every unchanged reader-facing label or instruction in these fences as
  an approval blocker. Do not mark a locale complete while the checker reports
  `copied_reader_fenced_line` until each line has been translated or documented
  as fixed output or literal data.
  Apply the same blocker to `copied_unlabeled_fence_line`; translate each
  reader-facing line or record a specific reason when it is fixed output or literal data.
  Compare the ordered fence inventory with the English source before approval.
  Every reader-facing `text`, `plaintext`, or `markdown` example must appear exactly once in
  each locale and retain its field and line coverage. File presence and a clean
  leakage scan do not prove that an example was translated; omitted examples
  and shortened sections are completeness failures. Also compare ordered
  heading levels, table shapes, and ordered/unordered list item counts with the
  source. Inspect count differences to distinguish an intentional language
  format change from omitted content, and repair confirmed omissions before
  peer review.
- After rendering, compare the ordered heading levels in Hugo output with the
  English page. Source checks that require whitespace after a Markdown heading
  marker can miss malformed headings such as `#はじめに`; inspect rendered
  headings so these lines do not hide a missing or misleveled section.
- Run `python3 tools/check_translation_english_leakage.py content/articles/<slug>`
  for each finished bundle. For a repository audit, use
  `python3 tools/check_translation_english_leakage.py --all --csv <report.csv>`.
  Run the checker after writing the files and again on the frozen review snapshot.
  A nonzero exit blocks approval until each finding is fixed or supported with a
  specific reason. Inspect the opening reader-facing line even when it is too
  short for paragraph-level language detection. The `copied_english_opening`
  finding blocks approval when it repeats descriptive English; retain a product-
  only comparison heading only after confirming it contains no untranslated
  reader-facing wording.
  The checker flags missing locale files, empty bodies, repeated English source
  paragraphs, sentences, or copied English word spans, English stopword
  dominance, missing expected scripts, and exact English reader metadata. Treat
  `copied_english_body` as a blocking exact-body fallback finding, even when
  translated front matter differs. Repair English-dominant short paragraphs;
  translated text elsewhere in the file does not make those paragraphs complete.
  The strict gate also blocks a single exact English prose paragraph or long
  reader-facing list item copied from the source. Run it on the temporary
  candidate before integration and again on the frozen in-tree bundle. Do not
  count code fences, tables, headings, shortcodes, linked list entries that
  contain only names, or title-cased list entries as prose for this blocker;
  review those through their dedicated findings.
  Treat each result as a manual-review queue. Inspect
  all reader-facing metadata and prose, resolve confirmed English copy, and
  record any false positives before peer review. Do not approve a bundle solely because the
  checker returns no flags.
  In translated lists of linked products or organizations, translate connective
  prose as well as surrounding sentences. In particular, do not leave the
  English conjunctions `and` or `or` before the final Markdown link. The strict
  fallback checker flags this pattern and CI blocks it. Keep official linked
  names and destinations unchanged.
  The `Translation English Fallback Check` workflow runs the high-confidence
  fallback screen on article changes. Run the same gate locally with
  `python3 tools/check_translation_english_leakage.py --all --fail-on-english-fallback`.
  It blocks exact English-body copies, multiple copied English paragraphs,
  English-dominant prose, missing expected scripts, copied reader-facing
  openings and linked-list connectors, and English-heavy code comments or
  sample values. In product comparisons, preserve product names but translate the
  comparison wording such as `vs`; an English list of brands is not a localized
  title. The broader checker
  remains a manual-review gate for shorter copied passages, reader-facing
  examples, headings, metadata, and false positives. The high-confidence gate
  does not block exact copied titles, descriptions, image alt text, captions,
  genres, or tags. Review those full-checker findings before approval. Translate
  descriptive values. Keep exact source wording only for a verified official
  name or fixed value, and record the reason.
  In CSV reports, review `copied_reader_fenced_lines`,
  `copied_unlabeled_fence_lines`, and `copied_reader_code_prose` separately from
  `exact_english_sentences`; fixed
  examples and executable-code comments are distinct findings and must not be
  mistaken for copied article sentences. Before approval, resolve every
  `copied_reader_code_prose` finding in context: translate reader-facing code
  comments, help text, and natural-language sample strings; retain fixed runtime
  output, identifiers, and literal data only with a recorded reason. A clean
  article-prose scan does not approve a locale while copied reader-facing code
  prose remains. In YAML examples, inspect top-level, mapping-level, and
  list-item `name:` labels, plus `msg:` values. These fields can be reader-facing
  even though they are structured values rather than comments. Preserve technical
  package names and identifiers when the field carries literal data.
  The checker also flags unchanged prose in executable-fence comments or
  natural-language command strings, and Markdown emphasis that splits a word.
  Preserve command syntax and classify fixed output separately.
  The checker also queues differences in ordered heading levels, Markdown table
  row/cell shapes, ordered and unordered list counts per section, link targets
  and order, shortcode sequences, and fenced-code language inventories. Compare
  each flagged structure with the source and restore omitted content before
  review. These shape signals require human inspection and do not establish
  translation completeness on their own.
- Scan the full translated prose for style violations. A filter requiring Latin
  letters skips paragraphs written entirely in another script.
- Check Punjabi, Bengali, and Hindi for stray letters from other Indic scripts.
  Exclude shared punctuation such as danda from wrong-script findings.
- Render a copied subset with the real Hugo templates for large multilingual
  batches. Verify expected output files exist, then inspect language metadata,
  article text, image paths, and structured data. Inspect user-facing text emitted
  by localized shortcodes and partials, including image alt/title text and CTA
  labels. A matching source shortcode does not prove its generated output is
  localized. Record English output from a shared component as a separate
  component follow-up instead of silently treating the article as fully localized.
  Hugo 0.169 does not accept `--resourceDir`. When a copied render needs an
  isolated resource directory, set `resourceDir` in a task-scoped TOML overlay
  and include that overlay after the locale config in `--config`.
- Distinguish automated structural checks from native-speaker review. Translation
  work does not establish a new technical fact-check of the English source.

## Commit and Integrate Reviewed Bundles

- Before committing a locale bundle, stage its exact reviewed paths and run
  `git diff --cached --check`. Fix extra blank lines at end of newly created
  translation files before commit. Any edit after peer approval requires a new
  frozen manifest and approval of that exact snapshot.
- After a bundle passes its assigned peer review and coordinator validation,
  create one local commit containing only that article's translation files.
- In a shared worktree, stage an explicit list of files for one bundle, then
  inspect `git diff --cached --name-only` before committing. Confirm every staged
  path belongs to that bundle and no checker, rule, test, or other article path
  is staged. If another writer is using the shared index, ask them to pause Git
  writes before staging. Do not amend a commit while another writer may have
  staged files. If a commit has mixed scope, record its hash and exact path list,
  then restore the prior commit while preserving all working files; create
  separate commits only after validating each frozen scope.
- Treat the staged-path check as time-sensitive: another writer can stage files
  after the check and before `git commit`. Keep stage, scope check, and commit in
  one serialized Git transaction. After any intervening Git activity or index
  lock, recheck `HEAD` and the full staged path list. If other writers cannot
  pause, defer the commit until they finish instead of risking a mixed bundle.
- If a scoped commit uses a separate `GIT_INDEX_FILE`, record the shared staged
  path list first. After commit, update only the committed bundle paths in the
  shared index from the worktree with `git add -- <exact paths>`. Verify those
  paths no longer appear in `git diff --cached --name-only` and confirm all
  unrelated staged paths remain unchanged. Do not reset the whole shared index.
- Merge each approved bundle into the existing local `master` or `main` checkout
  as soon as validation and worktree state allow. Preserve unrelated changes and
  avoid creating additional worktrees when an existing main checkout is usable.
- Do not push, publish, or deploy unless the user separately authorizes that
  action. A commit or local merge does not imply permission to publish.
