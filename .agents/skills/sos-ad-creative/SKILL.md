---
name: sos-ad-creative
description: "Create or revise sponsored ad artwork and Hugo ad partials for SimeonOnSecurity, including brand palettes, variant registration, and matching image preloads. Excludes article covers."
---

## Read first

Read `.clinerules/08-clinerules-maintenance.md`, rule 07, and relevant template guidance in rules 09 and 15. Read rule 13 only for conversion or deployed asset replacement. Inspect the requested brand's current generator configuration, partials, rotation entries, and preloads.

## Workflow

Use verified offer details and the brand's exact palette. Do not invent urgency, discounts, or social proof. Apply rule 07's one-offer CTA and code-visibility requirements to the requested creative.

Check that `tools/generate_ad_images.py` exists before invoking it; it is ignored by Git and is not guaranteed in a fresh clone. If absent, report the missing generator rather than substituting the article pipeline or inventing a replacement. Continue independent copy/layout work within scope.

Generate only the requested brand and variants with the existing credentials. Inspect each resulting image for actual text, palette, dimensions, cropping, and unsupported claims. The ad generator's `--force` behavior is distinct from the cover generator; do not interchange their flags or procedures.

For a new brand, follow rule 07's registration steps across lazy/eager/floating partials, rotation pools, and preloads. Keep sponsor link attributes and loading behavior intact. Match each `resources.Get` and resize argument byte-for-byte between the ad partial and its preload, including quality and format.

Use `sos-hugo-validation` for the shared render checks. Confirm the requested and prefetched derivative filenames agree on the built page. A source-only check misses resource-cache key mismatches.

## Finish

Report the generated variants, visual checks, and rendered alignment. Keep temporary generation output and credentials out of Git. Commit source artwork with its partials only when requested. Treat publication and cache purge as separate actions requiring authorization within the task.
