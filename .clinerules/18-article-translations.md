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

## Preserve Source Meaning and Structure

- Translate the full body and reader-facing metadata, including image alt text
  and captions. Keep technical names accurate and use Gurmukhi for Punjabi.
- Preserve publication dates, URLs, resource paths, code blocks, inline commands,
  shortcode names, and nontext shortcode parameters. Set `lastmod` when writing
  a new or refreshed translation.
- Protect code and markup before automated translation. Validate the exact
  placeholder counts before restoring the protected source text.
- Require all translation segments to return. Reject truncation, missing keys,
  missing headings, and altered table structure. Never substitute English text
  for a failed translation.
- Preserve existing unrelated edits. Before replacing an older translation,
  compare its current hash with the hash recorded during inspection.

## Validate the Result

- Parse every changed file's YAML and compare nontranslated metadata with its
  source. Compare code, link targets, shortcode parameters, and heading levels.
- Check every configured language for every selected bundle after generation.
- Treat language detection as a screening check. English product names and link
  labels distort results on short technical pages. Inspect script usage and
  surrounding prose before replacing a translation flagged by a detector.
- Scan the full translated prose for style violations. A filter requiring Latin
  letters skips paragraphs written entirely in another script.
- Check Punjabi, Bengali, and Hindi for stray letters from other Indic scripts.
  Exclude shared punctuation such as danda from wrong-script findings.
- Render a copied subset with the real Hugo templates for large multilingual
  batches. Verify expected output files exist, then inspect language metadata,
  article text, image paths, and structured data.
- Distinguish automated structural checks from native-speaker review. Translation
  work does not establish a new technical fact-check of the English source.
