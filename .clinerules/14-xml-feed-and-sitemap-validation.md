# XML Feed and Sitemap Validation

This rule documents the real bugs found (and fixed) in this repo's Hugo-generated XML
outputs, and how to validate them correctly. There are 8 XML output formats:
`index.xml` (default RSS, `themes/soshellofriend/layouts/_default/rss.xml`),
`rssall.xml`, `fulltext.xml`, `smartnews.xml`, `news.xml`, `imagessitemap.xml`
(all in `layouts/_default/`), `sitemap.xml` (`layouts/sitemap.xml`), and
`sitemap-index.xml` (`static/sitemap-index.xml`, hand-maintained, not templated).

## How to Validate Locally (the live site blocks external validators)

Cloudflare bot protection returns HTTP 403 to `curl`, the W3C Feed Validator, and the
`fetch_web_content` tool when they hit `simeononsecurity.com` directly. There is no way
to validate the live production output externally. Instead:

1. Build locally with the **exact** `--config` flag a real workflow uses, e.g.
   `hugo -D --minify --config config/language/en/config.toml --destination /tmp/x`.
   **Always pass `--minify`** when checking XML well-formedness: unminified Hugo output
   has leading blank lines before `<?xml ... ?>` from template whitespace, which makes
   `xmllint` report a false "XML declaration allowed only at the start of the document"
   error. This is cosmetic and never reaches production (every real build uses `--minify`).
2. Validate well-formedness: `xmllint --noout /tmp/x/<file>.xml`.
3. To check what is **actually live**, inspect the committed output branches instead of
   the site itself: `git show origin/website-en-alt:<file>.xml`. Netlify serves
   `website-en-alt`'s pre-built files as-is (`netlify.toml` has
   `build.processing.skip_processing = true`), so that branch is ground truth for
   `simeononsecurity.com`.

## Do Not Assume `relativeURLs = true` Breaks Feed URLs

`config/_default/config.toml` and every `config/language/<lang>/config.toml` set
`relativeURLs = true` and `canonifyURLs = true`. This looks alarming but is **harmless
for `.Permalink`, `absURL`, and all XML templates**: verified empirically (isolated
Hugo test projects on v0.163.3) that `.Permalink` always returns a fully absolute
URL (scheme + host) regardless of `relativeURLs`, and `absURL`/`absLangURL` are
likewise unaffected. `relativeURLs` only rewrites the HTML-output-format post-processing
pass, not RSS/sitemap/XML output formats (`isHTML: false` in the output-format table).

**The only way to get relative URLs in a real build here** is running `hugo` with no
`--config` flag at all (or pointed at a file lacking `baseurl`). `config/language/` is
NOT one of Hugo's auto-loaded config-directory names (`config/_default/`,
`config/<environment>/`), so a bare `hugo` command silently builds with **no
`baseurl` configured**, producing root-relative paths everywhere. This exact mistake
produced a stale, uncommitted local `public/` directory that looked like a "critical
relative-URL bug" in the real site, but every actual production workflow explicitly
passes `--config config/language/<lang>/config.toml` and is unaffected. Confirm the
theory before "fixing" a Hugo URL bug: rebuild with the exact CI `--config` flag and
diff against `git show origin/website-en-alt:<file>`.

## Real Bugs Found and Fixed (2026-09)

- **`layouts/_default/index.news.xml`**: used `{{ $.Title }}` (site title) instead of
  `.Title` for `<news:title>` inside the per-article range loop. Every entry in the
  live `news.xml` showed the identical wrong title "simeononsecurity". Fixed by using
  `.Title` (the page in scope inside `range`).
- **Same file, filter bug**: filtered on `.Lastmod` for both the 48-hour recency window
  and `news:publication_date`, with no section scoping. Combined with the shallow-clone
  issue below, this made ~893 of ~956 total site URLs (including `/hof/`,
  `/ctfranks/`, `/recommendations/organizations/`) incorrectly appear in the news
  sitemap. Fixed by: (1) scoping to `{{ $newsSections := slice "articles" "writeups"
  "blog" "til" "guides" }}` and checking `in $newsSections .Section`, and (2) switching
  both the recency filter and `news:publication_date` to `.Date` (the original front
  matter publish date), which Google's docs require anyway ("Specify the original date
  and time when the article was first published... Don't specify the time when you
  added the article to your sitemap") and which is immune to the Git-derived Lastmod
  inaccuracy below.
- **Shallow-clone `Lastmod` corruption (root cause, all 19 `branch_build_hugo_*.yml`
  workflows)**: every workflow uses `actions/checkout@v7` (default `fetch-depth: 1`,
  i.e. shallow) together with `hugo --enableGitInfo`. Per Hugo's own docs
  ("Hosting considerations" on the GitInfo page), a shallow clone makes Git-derived
  `Lastmod` inaccurate, typically collapsing to the most recent repo commit for every
  file instead of that file's actual last-modifying commit. This explained why the live
  `sitemap.xml` had only 2 distinct `<lastmod>` values across 956 URLs. Fixed by adding
  `fetch-depth: 0` to the checkout step in every `branch_build_hugo_*.yml` workflow that
  was missing it (`branch_build_hugo_en_github.yml` already had it). This is the single
  highest-leverage fix in this pass: it affects `sitemap.xml` `<lastmod>` accuracy for
  every language and both news-sitemap correctness and any theme/partial that reads
  `.Lastmod`.
- **`atom:link rel="self"` wrong href** in `index.fulltext.xml`, `index.smartnews.xml`,
  `index.rssall.xml`: all three hardcoded `.OutputFormats.Get "RSS"`, which resolves to
  the *default* RSS format (`/index.xml`) regardless of which output format template is
  actually rendering. Every one of these three feeds self-referenced `/index.xml`
  instead of its own file. Fixed by changing each to `.OutputFormats.Get "<own format
  name>"` (`"fulltext"`, `"smartnews"`, `"rssall"` respectively), matching the
  `[outputFormats.<name>]` key in `config/_default/config.toml`.
- **Double-slash in `<image><url>`** in `index.xml` (theme `rss.xml`), `rssall.xml`,
  `smartnews.xml`: `{{ printf "%s%s" .Permalink .Site.Params.RssImage }}` where
  `.Permalink` already ends in `/` and `RssImage` (`/img/banner.webp`) starts with `/`,
  producing `https://.../` + `/img/banner.webp` = a literal `//`. Fixed by replacing
  with `{{ .Site.Params.RssImage | absURL }}`, which handles the path join correctly.
- **Copy-paste bug duplicated 4x**: `resources.Copy` for the "large" (1920px) resized
  image variant was copying to `$mediumfilename` instead of `$largefilename` in
  `layouts/_default/index.imagessitemap.xml` and three call sites in
  `themes/soshellofriend/layouts/partials/preload-images.html`. This silently
  overwrote the real 731px medium image's cached file with the 1920px content (last
  write wins on the same resource path), so the image sitemap emitted a duplicate
  `_731x411.webp` entry instead of a genuine `_1920x1080.webp` one, and no real
  1920px derivative ever existed on disk. Fixed all 4 occurrences to
  `resources.Copy $largefilename`.
- **Same bug in `themes/soshellofriend/layouts/partials/postcover.html`, plus a second,
  more visible bug**: the visible `<picture><source srcset>` on every article's cover
  image used `{{ $optimizedmedium }} 1920w, {{ $optimizedmedium }} 731w, ...`, the
  1920w descriptor pointed at the medium image, never referencing `$optimizedlarge` at
  all, and `sizes` never asked for `1920px` at any breakpoint. Fixed the filename
  copy-paste in this file too, changed the `1920w` srcset entry to reference
  `$optimizedlarge`, and changed the `(min-width: 4096px)` sizes entry to `1920px`.
- **Deprecated Google Image Sitemap tags**: `<image:title>` and `<image:caption>` were
  emitted in `index.imagessitemap.xml`. Google's Image Sitemap docs (checked live,
  updated 2025-12-10) confirm these tags plus `<image:geo_location>` and
  `<image:license>` were removed from processing; `<image:loc>` is the only tag Google
  still reads. Removed all `<image:title>`/`<image:caption>` emission (5 occurrences).
- **`sitemap_exclude` vs `sitemap_ignore` naming mismatch**: `content/admin/index.html`
  (a canary-token honeypot page, `robotsdisallow: true`) sets `sitemap_ignore: true` to
  keep itself out of sitemaps, matching the key `layouts/sitemap.xml` checks. But
  `index.imagessitemap.xml` checked the different, unused key `sitemap_exclude`, so the
  honeypot page was included in the image sitemap despite clear author intent. Fixed
  `index.imagessitemap.xml` to check `sitemap_ignore` (same key as the main sitemap).

## Validation Checklist After Touching Any XML Template

1. Rebuild with `--minify` using the real per-language `--config` flag, not a bare
   `hugo` command.
2. `xmllint --noout <file>.xml` for well-formedness.
3. `grep -o '<loc>[^<]*</loc>'` / `<link>` / `<guid>` / `<image:loc>` and confirm every
   value starts with `https://`, never a bare `/`.
4. For self-referencing feeds, `grep -o 'atom:link href="[^"]*"'` and confirm the href
   matches that file's own name, not `/index.xml`.
5. For `news.xml`, confirm entry count is 0 unless something was actually published in
   the current front matter `date` within the last 48 hours, and confirm `<news:title>`
   values are distinct per article, not all identical.
6. For `index.imagessitemap.xml`, confirm the four cover-image variants
   (`_240x135`, `_480x270`, `_731x411`, `_1920x1080` for a typical 16:9 cover) are all
   distinct file sizes/dimensions on disk under `img/cover/`, not two identical files
   under different names.
