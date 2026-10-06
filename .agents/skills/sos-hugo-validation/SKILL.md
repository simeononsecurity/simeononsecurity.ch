---
name: sos-hugo-validation
description: "Validate or troubleshoot SimeonOnSecurity Hugo rendering, shortcodes, metadata, feeds, sitemaps, and asset URLs. Select targeted or production-config builds according to the changed surface."
---

## Read first

Read `.clinerules/08-clinerules-maintenance.md` for build scope, rule 09 for templates and shortcodes, and rule 15 for rendering failures and release boundaries. Read rule 14 for XML outputs or dates, rule 13 for image conversion, and rule 07 for ad assets only when relevant.

## Choose the check

- Ordinary Markdown or documentation: source checks and a targeted render when useful. Do not launch a full multilingual build by default.
- Shared templates, CSS/JS, configuration, output formats, or resource processing: follow the canonical build requirements and inspect representative rendered pages.
- XML: use the real CI language config with `--minify`, then parse the actual XML and verify its semantics.

Inspect the applicable workflow before choosing flags. Put test output and logs outside the source tree. Do not clear caches or restore broad directories without first preserving unrelated changes. A minimal isolated reproduction diagnoses one mechanism; it does not establish a full production build passed.

## Inspect outcomes

Check exit status and logs, then the expected markup. A successful build alone does not establish correct behavior. Verify the rendered image targets, requested YouTube player, TOC anchors, canonical and social metadata, and relevant page/section differences.

Parse JSON-LD with a strict JSON parser. Reject a double-encoded string as well as invalid JSON. Derive expected schema types from the page and active templates rather than assuming every article emits the same count. HTML parsers must handle unquoted and valueless attributes in minified output.

For feeds, verify absolute URLs, each feed's own self-link, news dates/titles, sitemap exclusions, and distinct image derivatives. Confirm rendered modification dates when GitInfo is enabled. Compare pages at several URL depths when investigating path rewriting.

For a source/output mismatch, reproduce the suspected Hugo mechanism in a small temporary project before changing shared settings. Read the specific diagnostic sections of rules 14 and 15 rather than applying a historical fix blindly.

## Finish

Report exactly which output and build configuration passed, and any remaining limitation. Do not change `bump.md` unless rule 15's two-condition policy applies. A commit does not prove deployment; push, deployment, and cache purge remain within the user's authorized scope.
