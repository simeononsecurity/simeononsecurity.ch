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
- Discover bundles recursively with `content/articles/**/index.en.md`; nested
  article bundles exist. Parse front matter and exclude `draft: true` sources
  from published-coverage totals. A one-level glob or an unfiltered source count
  can miss bundles or count drafts as published.
- Check existing files for valid YAML, published status, nonempty translated
  bodies, and missing sections. File existence alone does not establish coverage.
- Before recording bundle claims, run the strict English-fallback and structure
  checker on each selected bundle. Record absent locale files separately from
  present but incomplete files, and assign repairs for both sets. A present
  `index.<locale>.md` with source-structure or reader-facing English findings
  remains incomplete until repaired and rechecked; do not dispatch only the
  absent locales when existing files in the bundle also fail.
- Before dispatching a bundle, compute its English source hash from the current
  checkout and compare it with the recorded claim. Give the same verified hash
  to the writer. If a writer reports a mismatch, stop before copying or editing
  candidate files, then reconcile the claim and current source hash.
- Immediately before each batch dispatch, refresh the live agent list, Git status,
  and progress ledger. Exclude every active claim and modified bundle, even when
  another coordinator appended it during selection. Choose the next unused batch
  identifier from the latest ledger. Record all bundle paths and full 64-character
  source hashes together before spawning any writer, then verify those exact hashes
  and paths one final time. A unique batch number does not replace unique bundle
  ownership.
- Before forwarding or applying peer-review findings, verify the report names
  the assigned bundle and its English source hash. Compare each cited phrase
  with that exact source; quarantine findings about another article instead of
  applying them to the current candidate.
- Treat a frozen candidate directory as immutable once its manifest is written.
  For any correction, copy the snapshot to a new versioned candidate directory,
  preserve the earlier files and manifest, then create a new manifest. Reviewers
  must verify the manifest before and after review; stop and report a hash
  mismatch instead of reading a candidate that the author is still changing.
- Before assigning remaining locales in an unfinished candidate, enumerate its
  actual `index.<code>.md` files and verify their hashes against the candidate
  records. Derive the missing-code set from Hugo's configured locales minus the
  verified files. Do not infer missing locales from a stale ledger or summary.
- Compare section structure against English. A translation with far fewer
  headings needs inspection for an older or incomplete source revision.
- Treat a heading-count or heading-level mismatch as a blocking completeness
  defect. The strict leakage gate blocks `markdown_heading_levels_mismatch`;
  do not approve a locale until every source section has a translated
  counterpart, even when the existing prose is fluent and the locale file
  exists.
- Use script-aware checks for completeness. Whitespace word counts undercount
  Chinese and Japanese; compare sections, lists, links, and reader-facing
  content against the source before marking a file incomplete or complete.
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
  proper-name exception. Preserve the source tag and genre counts. The strict
  gate blocks `taxonomy_count_mismatch`; inspect the report's source/target
  counts, then compare value order manually because translations change values.
  A clean strict fallback scan still does not approve taxonomy: compare every
  tag and genre against the source, translate generic English values, preserve
  canonical product names and acronyms, and verify order and count before review.
- Do not translate a brand name into a common noun in titles, prose, or taxonomy.
  Keep names such as Brave, Epic, Puffin, and Waterfox intact, and translate only
  the generic descriptor around the name.
- In fenced formulas and text blocks, translate explanatory labels such as
  `layers`, `KV heads`, `dimensions`, and `bytes`. Preserve the numeric values,
  operators, and fixed identifiers such as `K` and `V`; a code or text fence does
  not make reader-facing labels exempt from localization.
- In glossary entries, retain the acronym as the fixed key and translate its
  reader-facing expansion. Do not leave the source English expansion as the
  only explanation. Keep the English wording alongside the localized expansion
  only when readers need the canonical phrase to identify the acronym.
  Localize ordinary glossary term keys, such as “firewall,” when the target
  language has a conventional term. Preserve fixed acronym keys such as `ACL`,
  `CI/CD`, and `QR Code`.
- Apply the same rule to acronym expansions in ordinary article prose. Keep the
  acronym, but translate reader-facing expansions such as “software as a
  service” unless the English wording is a formal product name or exact UI label.
  Do not leave a standard expansion in English only because the acronym is
  familiar to the target audience.
- Check false friends that change evidence-handling meaning. For example,
  “unredacted evidence” means sensitive details remain present, not that evidence
  is unedited or unremediated. Keep such evidence only in the approved private
  location.
- Translate security terms by their established meaning, not by a literal
  cognate. In Catalan, do not render phishing as `pesca` alone; retain
  `phishing` or use a recognized descriptive phrase, and confirm the wording
  still refers to credential theft or impersonation attacks.
- Preserve the established programming-security meaning of common terms:
  `hard-coded credentials` means credentials embedded directly in source code,
  not credentials that are difficult to encode; `input sanitization` means
  validating and cleaning input or output, not physical disinfection or
  removal; and `data leakage` means unauthorized exposure, not data loss.
  Translate `code injection` with the target language's established term and
  preserve its meaning. When review finds one of these semantic errors, search
  the entire locale file for related prose and taxonomy, correct each occurrence,
  and recheck the full bundle.
- Translate common English technical terms when the target language has a clear
  reader-facing equivalent. In Italian prose and table labels, use
  `velocità di trasferimento` for `throughput` and `integrato`,
  `tutto-in-uno`, or `con funzioni integrate` for `all-in-one`. Keep the English
  only for an exact UI label or formal product name.
- In Italian, `password` is a standard security loanword. Phrases such as
  `gestore di password` are localized when surrounding grammar is Italian;
  retain the strict fallback finding only for an otherwise copied English label.
- In Hindi, translate password-manager `vault` consistently as
  `पासवर्ड मैनेजर का सुरक्षित भंडार`. Search the whole locale file for every
  occurrence instead of repairing only the flagged paragraph.
- Use the established target-language acronym for laws and regulatory regimes.
  In French, use `RGPD` for `GDPR`; introduce `GDPR` once in parentheses only
  when the English acronym helps identify sources, then use `RGPD` consistently
  in reader-facing metadata and prose.
- Preserve publication dates, URLs, resource paths, code blocks, inline commands,
  shortcode names, and nontext shortcode parameters. Set `lastmod` when writing
  a new or refreshed translation. For a batch refresh, update and verify
  `lastmod` in every changed locale file. Existing translations can carry
  different older dates, so verify the complete changed-file set instead of
  replacing only one known date value. The leakage checker's `read_page()` helper
  omits `lastmod`; inspect raw front matter or parse the YAML directly when
  verifying translation dates.
- In fenced examples, preserve executable syntax, commands, identifiers, and
  literal output. Translate natural-language comments and reader instructions
  inside the fence, including lines such as `# Build and flash for Atom Lite`.
  Translate reader-facing strings returned by examples, including short
  greetings such as `Hello,`. Check `return` values as well as `print` and log
  calls. The strict leakage gate blocks unchanged source-matched short greetings
  in code output.
  Localize unchanged natural-language sample inputs in code, such as a YAML
  `user_input: "Hello! This is a string with non-alphanumeric characters."`
  value. Keep the key and example logic unchanged, and translate only the
  sample data when it serves as reader-facing prose. The strict gate screens
  source-matched English sentences in quoted YAML scalar values.
  Treat comment markers as code syntax, not as proof that the words after them
  are fixed technical text. Compare each reader-facing comment with its source
  counterpart and inspect code-prose fallback findings before freezing a
  candidate.
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
  The English-dominant title screen blocks descriptive English titles that
  differ from the source title. An unchanged source title stays a manual-review
  finding because official product or publication names can remain in English.
  Review title, description, tags, alt text, and captions against the source. For
  acronym expansions, strict mode blocks unchanged lowercase expansions in
  reader prose, including lists and blockquotes, when the target adds no
  localized explanation. The broader checker queues bilingual expansions and
  title-case expansions for manual review. Script detection does not establish
  meaning: phonetic transliteration of English words does not count as a
  localized expansion. Keep the canonical acronym key and require a target-
  language gloss. For every queued expansion, the peer reviewer must compare
  the localized words with the source meaning and record a disposition. This
  review catches untranslated expansions even when the strict checker cannot
  distinguish transliteration from translation.
  For non-Latin locales, the leakage checker reports exact English phrases
  copied from the English source inside localized prose. Review every reported
  phrase for product names, identifiers, or legitimate loanwords. Strict mode
  blocks a locale when 20 or more distinct source-matched phrases remain; this
  catches heavily code-mixed files that paragraph-level language detection
  misses. Translate reader-facing phrases, then rerun the strict checker and
  inspect the remaining phrase report manually.
  For German, Dutch, and Portuguese bilingual expansions, the checker uses
  locale markers, including recognized compound stems, to decide whether added
  wording enters manual review. An unrecognized suffix does not clear a strict
  finding. Add a marker only after confirming the term against a native-language
  source and adding a regression test. Review every queued expansion for meaning.
  For each locale, include a source-aligned review record for the title,
  description, opening, every section, and every reader-facing example or
  caption. Within each section, map every source prose paragraph to a translated
  paragraph or an explicitly justified structural equivalent. Heading, list,
  table, and link counts do not prove ordinary narrative paragraphs are complete.
  Source-alignment CSV cells can contain quoted newlines. Count logical records
  with a CSV parser, not physical lines or `wc -l`.
  The peer reviewer must verify each mapping against the frozen file hashes.
  Keep the locale incomplete until all reader-facing prose is in the
  target language or a specific retained English term is documented as a
  proper name, official source title, fixed identifier, command, or literal
  value. A filename, `lastmod`, script ratio, or clean strict-checker result
  alone never establishes translated coverage.
  During that review, compare every title, subtitle, description, table header,
  table label, and link anchor, including external links and bibliography
  references, with its English source and target-language meaning. Generic labels
  such as `Link`, `Model A`, `Total certifications`, `with
  fallback`, and `Plug-and-play` are reader-facing text, not model names or
  technical identifiers.
  In Snyk references, keep the product name `Snyk` and translate generic
  descriptors such as `Open Source Security Platform`; do not carry over the
  full English link label just because it starts with a brand name.
  Translate descriptive link anchors such as `TLS RFC`; preserve the RFC URL
  and the TLS acronym.
  Translate them even when surrounding table rows are localized. Treat an exact
  English label in a locale file as a blocker unless the reviewer documents why
  the literal English is required. Record the source and target wording in the
  review ledger, then rerun the strict fallback screen after corrections.
  For reference links, preserve an English label as an official title only
  after checking that the destination uses that exact title. Localize
  author-written descriptions while retaining the organization or product name.
  Apply the same check to genre and tag values. The strict checker blocks exact
  carryovers for reviewed generic labels such as `ad-blocking`, `cross-platform`,
  `data privacy`, `internet privacy`, `open-source`, `python interpreter`, and
  `python security documentation`.
  Preserve exact taxonomy text only for verified product names, acronyms, or
  accepted target-language loanwords, and record the locale-specific reason.
  Translate reader-facing `description`, `caption`, and `alt` values in shortcode
  arguments. Preserve official video titles, IDs, and other fixed parameters.
  The leakage checker treats an unchanged multiword shortcode description,
  caption, or alt value as a blocking English fallback; inspect other translated
  values against their source because exact-copy checks do not detect every
  incomplete translation.
  Review `high_confidence_english_title` and `english_dominant_title_review`
  separately. The strict gate blocks clear English title fallbacks. The `VS Code`
  product name is not a comparison. Comparator matches remain in the manual-review queue because
  `vs` appears in local-language titles; compare the source and target convention,
  then translate reader-facing comparison wording when needed. The title-review
  queue also includes ambiguous one-word matches; compare those with the source
  and local-language title before changing them. Do not treat product names,
  acronyms, locale stopwords, or localized cognates as English evidence by
  themselves.
- Preserve existing unrelated edits. Before replacing an older translation,
  compare its current hash with the hash recorded during inspection.

## Keep the English-Fallback Gate Runnable

- Run the focused regression suite from the repository root with
  `python3 tools/test_translation_english_leakage.py`. Do not invoke it as
  `python3 -m unittest tools.test_translation_english_leakage`: the test imports
  the checker as a top-level module, so that package-style invocation fails
  before tests run.
- The full `tools/check_translation_english_leakage.py --all` scan takes longer
  than 10 minutes on the current article corpus. Set
  `.github/workflows/translation-english-fallback.yml` to a timeout of at least
  30 minutes so the checker finishes. Confirm the CSV is complete and inspect
  high-confidence prose findings before treating a run as a pass. The mixed-
  phrase scan must tokenize each line once and validate word gaps from token
  offsets. Do not compile a new regular expression for every phrase window.
  Pass raw Markdown to the checker; do not pre-clean it and then let the checker
  clean it again. The `--all` summary counts only sources accepted by the same
  `read_page` and `published` filter used for auditing; keep a draft fixture in
  the regression suite when changing that count.
- The table-cell checker exempts only the exact product-name cells `Azure` and
  `Server 2019`. Keep these fixed names when the source identifies those
  products; translate surrounding headings and prose. Do not widen the
  exemption to generic cells such as `server`, `capacity`, or `description`.
  In the OpenRouter routing example, keep endpoint IDs `A` and `B` in the table
  and formulas. The checker exempts those IDs only in a table with the
  `Illustrative endpoint` source header. A standalone `A` elsewhere remains a
  table-cell finding.
- Add a confirmed generic English phrase to the strict fallback checker only
  with a narrow regression fixture. For example, `GPS wardriving` is a
  reader-facing capability description. Localize it while preserving fixed
  identifiers such as GPS, Wi-Fi, and product names.
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
  Treat `copied_english_acronym_expansion` as an approval blocker. Translate the
  glossary expansion while retaining its acronym key. A bilingual expansion is
  acceptable only when localized wording appears beside the canonical English
  phrase.
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
  paragraphs, sentences, descriptive lines in reader-facing fences, or copied English word spans, English stopword
  dominance, missing expected scripts, and exact English reader metadata. Treat
  `copied_english_body` as a blocking exact-body fallback finding, even when
  translated front matter differs. Repair English-dominant short paragraphs;
  translated text elsewhere in the file does not make those paragraphs complete.
  The strict gate also blocks one high-confidence English-dominant reader prose
  paragraph, a single exact English paragraph, or a long reader-facing list item
  copied from the source. The paragraph blocker excludes title-cased references,
  linked bibliography entries, code, headings, tables, and paragraphs with
  substantial expected-language script. Review broad mixed-script flags in
  context instead of treating product names or source titles as English prose.
  Keep localized bibliography headings in `REFERENCE_HEADINGS` so translated
  citations do not look like reader prose. The strict paragraph screen skips
  Markdown table rows because copied descriptive cells have their own check,
  and counts accented Latin words as whole tokens before comparing English and
  locale stopwords.
  Run it on the temporary
  candidate before integration and again on the frozen in-tree bundle. Do not
  count code fences, tables, headings, shortcodes, linked list entries that
  contain only names, or title-cased list entries as prose for this blocker;
  review those through their dedicated findings.
  Treat each result as a manual-review queue. Inspect
  all reader-facing metadata and prose, resolve confirmed English copy, and
  record any false positives before peer review. Do not approve a bundle solely because the
  checker returns no flags.
  Before repairing a saved leakage report, regenerate it from the current
  source and translation files and inspect the exact flagged text. Reports can
  be stale, and technical names, UI labels, bibliography titles, and mixed
  script prose can trigger screening flags without being English fallbacks.
  Never replace a locale file based on a report summary alone; record the live
  path, exact phrase, and disposition for every confirmed fallback or exception.
  In translated lists of linked products or organizations, translate connective
  prose as well as surrounding sentences. In particular, do not leave the
  English conjunctions `and` or `or` before the final Markdown link. The strict
  fallback checker flags this pattern and CI blocks it. Keep official linked
  names and destinations unchanged.
  Reader-verb flags can match valid words in another language, such as Spanish
  `uses` or French `supports`. Check the complete sentence against its English
  source before changing text; keep grammatical target-language wording and
  disposition a confirmed false positive in the batch report.
  Translate descriptive labels for first-party article links when a localized
  sibling page exists. Keep the URL unchanged. The strict checker blocks an
  unchanged English label when the linked article has a translated title.
  When reviewing a link-label finding, confirm the exact label and its paired
  destination in the report. An unrelated first-party link elsewhere on the
  same page does not make an external product label an internal article link.
  Acronym glossary entries also need a localized expansion beside the fixed
  acronym key. Keep the canonical English phrase only when it helps readers
  identify the acronym, and pair it with localized wording. The strict checker
  blocks an expansion copied unchanged from English, including expansions that
  contain no English stopwords, and flags substantial copied phrases inside a
  partially localized expansion. Check repeated acronym keys entry by entry;
  one localized expansion does not clear another occurrence of the same key.
  Repeating the fixed acronym key beside the English expansion does not count
  as localized wording; the checker excludes key tokens from its localization
  threshold.
  When the canonical English phrase remains beside a CJK translation, require at
  least six target-script letters before treating the expansion as localized.
  For German and Dutch, one localized compound must contain at least eight
  letters. Other Latin-script languages need at least two localized words.
  Accents alone do not clear copied English.
  Keep fixed technical keys such as `CI/CD`, `DDoS`, and `QR Code` intact. The
  checker includes mixed-case and slash-separated acronym keys, plus `QR Code`
  and `Qubit`, in its glossary screen. It screens unchanged parenthetical
  acronym expansions in ordinary prose, lists, and blockquotes, including
  acronym keys joined to locale-specific compounds such as German
  `NFC-Zahlung`. It queues bilingual expansions and non-Latin transliterations
  of acronym keys for peer review. Glossary definition lists use their
  dedicated acronym-key check. A fixed acronym in a product or tool list is
  not an expansion.
  Keep the acronym key itself unchanged. Treat `missing_acronym_key` as a
  blocking finding and restore the source key while localizing its expansion.
  Review unchanged one-word technical terms in context. Keep them only when the
  same form is accepted in the target language, such as `JavaScript`; otherwise
  localize them too.
  `Python-Interpreter`/`python-interpreter` is an accepted technical term in
  German and Dutch taxonomy. The checker exempts only that exact term in those
  locales. `cloud computing` is an accepted technical loanword in German,
  Italian, and Romanian taxonomy. The checker exempts only that exact term in
  those locales.
  Table-cell copy findings compare cells within the same table even when a
  translation changes row or column order. Inspect each flagged cell against
  its localized row and do not dismiss it because its coordinates changed.
  The checker exempts a short exact list of reviewed product, standards, and
  fixed-value labels in `TABLE_FIXED_NAMES`. The OpenRouter `A` and `B` endpoint
  IDs use a separate table-context check. Do not add a broad phrase or term
  exemption. Add an exact value only after comparing its source and target row,
  confirming it is a proper product/standard/literal, and adding a regression
  fixture. Translate generic headers such as `Total certifications`.
  A standalone `Cost` cell is valid in Catalan and Romanian; the checker exempts
  only that exact word, not longer English labels such as `Cost per user`.
  `Performance` is an established French label; keep the checker exemption exact
  to that standalone French word.
  Translate common English prose verbs when they appear inside localized
  paragraphs. The checker blocks source-matching verbs such as `offers`,
  `provides`, `includes`, and `supports`, even when the rest of the paragraph
  uses the target language. Spanish `uses` is also a valid form of `usar` in
  phrases such as `no lo uses`; the checker exempts only that exact word for
  Spanish. Still inspect the full sentence for English carryover.
  The `Translation English Fallback Check` workflow runs the high-confidence
  fallback screen on article changes. Run the same gate locally with
  `python3 tools/check_translation_english_leakage.py --all --fail-on-english-fallback`.
  Strict mode also blocks `translation_missing`; a zero exit requires every
  configured locale file to exist. Keep the recursive configured-locale
  inventory separate because the strict language gate does not validate
  translation completeness or source structure.
  A locale suffix does not prove that a file contains a translation. Before
  approving a locale file, compare its reader-facing body with `index.en.md`.
  The strict gate must block an unchanged English body even when the filename
  and front matter use the target locale; keep this case covered by a regression
  test.
  It blocks exact English-body copies, copied English prose verbs, copied English expansions in glossary
  entries or lowercase parenthetical prose without a localized explanation,
  copied labels for localized first-party article links, copied English
  calculation labels in reader-facing formulas, one
  high-confidence English-dominant
  reader paragraph, multiple copied English paragraphs, English-dominant prose,
  missing expected scripts, copied reader-facing
  openings, linked-list connectors, English-heavy code comments or sample
  values, copied reader-facing descriptions, image alt text, captions, and
  high-confidence English titles that differ from the source. The metadata
  parser covers quoted, plain, folded, and literal YAML scalars. Exact copied
  titles remain a review finding because product and proper names can be valid.
  The
  CSV also queues retained `vs` comparators for manual review; the abbreviation
  alone does not fail the strict gate. Preserve product names and localize the
  connector when the target-language title needs it. An English list of brands
  is not a localized title. The broader checker
  remains a manual-review gate for shorter copied passages, reader-facing
  examples, headings, exact copied titles, taxonomy values outside the reviewed
  generic-label set, and false positives. Review those
  full-checker findings before approval. Translate
  descriptive values. Keep exact source wording only for a verified official
  name or fixed value, and record the reason.
  Script-aware paragraph ratios miss short English phrases inside otherwise
  localized Bengali, Hindi, Arabic, Japanese, Punjabi, Russian, and Chinese
  prose. Review the CSV's exact two-to-six-word source phrase matches in those
  locales, even when the strict paragraph screen passes. Translate reader-facing
  phrases; preserve only verified names and fixed settings, and record the
  reason. The strict gate blocks reviewed generic descriptors such as
  `Multi-Gigabit` and `Hardware Controller` when copied verbatim. Add a narrow
  regression fixture before adding any new descriptor to the checker. It also
  blocks unchanged generic link anchors such as `Link`; translate bibliography
  labels while keeping their destinations unchanged. Accept standard localized
  compounds such as German `Python-Website` when the language uses the same
  technical loanword.
  For cloud-provider bibliography links, keep provider names such as Amazon Web
  Services (AWS), Microsoft Azure, and Google Cloud Platform, but translate
  descriptive suffixes such as `Security` and `Security and Compliance`. The
  strict checker blocks those three exact copied English labels.
  For Chocolatey links, preserve the brand and destination but translate
  author-written labels such as `Chocolatey documentation on Puppet
  integration`, `Chocolatey module documentation for Ansible`, `Chocolatey
  documentation on package creation`, `Chocolatey Official Website`, and
  `Chocolatey Documentation`. Localize generic labels such as `NuGet Package
  Manager` while preserving the product name. The strict checker blocks each
  exact English label.
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
  The strict `--fail-on-english-fallback` gate now blocks every
  `markdown_*_mismatch` as well as taxonomy-count mismatches. Do not waive a
  structural blocker from a clean prose scan; inspect the source-aligned item
  or section, restore it, and rerun the strict gate.
  Same-page heading fragments may change when the target heading is translated.
  Preserve the link path and query, then point the fragment at the Hugo-generated
  ID for the matching translated heading. Verify the target heading at the same
  source-aligned ordinal and inspect rendered HTML for each configured locale.
  The checker accepts changed fragments only when the link path is empty and
  the fragment resolves to the translated heading at that ordinal. Keep fragments
  on relative links to another page unchanged unless you resolve the destination
  page's headings. The checker blocks changed paths, cross-page fragments,
  external URLs, queries, unmatched fragments, and changed explicit heading IDs. Repeated generated
  heading IDs use Hugo's numeric suffix and remain aligned by heading order. Hugo's
  `markup.goldmark.parser.autoHeadingIDType = 'github'` preserves non-ASCII
  letters, drops combining marks, converts spaces to hyphens, and suffixes
  duplicate IDs. Verify anchor behavior with the repository's Hugo version.
- Scan the full translated prose for style violations. A filter requiring Latin
  letters skips paragraphs written entirely in another script.
- Check Punjabi, Bengali, and Hindi for stray letters from other Indic scripts.
  Scan every changed file after the final edits, not only reviewer-cited words.
  A file containing the expected script can still contain stray characters or
  words from another Indic script. Exclude shared punctuation such as danda
  from wrong-script findings.
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
- Mixed-language sentences need a phrase-level check even when the paragraph is
  mostly translated. The strict checker blocks unchanged generic phrases such
  as `incident response`, `best practices`, and `supply chain`; translate them
  unless a specific product, publication, or organization name requires the
  English wording. It also blocks reviewed phonetic spellings of `incident
  response` in Bengali, Hindi, Punjabi, and Japanese, plus `supply chain` in
  Japanese. Keep any named-entity exception in the review record.
- Treat the locale extension as routing metadata, not evidence of translation.
  Run the blocking leakage check on every candidate before adding it to
  `content/articles/`, then inspect any English-dominant heading, sentence,
  table cell, metadata value, or link label manually. Keep official publication
  titles and product or organization names in their source language when
  needed, but translate descriptive reference labels such as `Best Practice
  Framework`. Record the reason when an English title or name remains.
- When an exact English browser or application UI label must remain so readers
  find the control, add a concise target-language gloss beside it in every
  instruction where the label appears. Translate the surrounding sentence and
  record the literal label and gloss as the reason for retaining English.
- Distinguish automated structural checks from native-speaker review. Translation
  work does not establish a new technical fact-check of the English source.

## Commit and Integrate Reviewed Bundles

- Before copying or staging a completed bundle, derive the non-English locale set
  from `config/_default/config.toml` in the validation script. Compare the exact
  source, candidate, and destination locale-code sets; stop on any missing or
  extra path. Do not hand-type a locale list in a copy or `git add` command. A
  strict leakage scan can report a missing translation without making the
  omission obvious in a long manual file list.
- Before committing a locale bundle, stage its exact reviewed paths and run
  `git diff --cached --check`. Fix extra blank lines at end of newly created
  translation files before commit. Any edit after peer approval requires a new
  frozen manifest and approval of that exact snapshot.
- Check whitespace-only blank lines before freezing a translation candidate, not
  after peer review. If `git diff --cached --check` finds whitespace after
  approval, preserve the approved snapshot, make a new versioned candidate, and
  obtain approval for the new hashes before commit.
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
