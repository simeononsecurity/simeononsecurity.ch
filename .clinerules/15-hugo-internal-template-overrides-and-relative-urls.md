# Hugo Internal Template Overrides and relativeURLs Pitfalls

This rule documents two real, previously-undetected Hugo configuration bugs found and
fixed in this repo (2026-09), plus the diagnostic technique used to find them. Both bugs
were "invisible" in the sense that the site built cleanly with zero warnings/errors;
the only symptom was wrong runtime behavior.

## Bug 1: `{{ template "_internal/X.html" . }}` Does Not Override Hugo's Built-In X.html

This project had custom overrides at `layouts/_internal/opengraph.html`,
`layouts/_internal/twitter_cards.html`, and `layouts/_internal/google_news.html`,
invoked from `themes/soshellofriend/layouts/partials/head.html` via
`{{ template "_internal/opengraph.html" . }}` etc. **This silently does nothing.**
Hugo (confirmed on v0.163.3) always renders its own built-in embedded partial for these
three names and completely ignores the project's `layouts/_internal/` file when called
via `template "_internal/...."`. No warning, no error, no build-time signal at all.

**Symptom:** the rendered `<head>` only ever contained Hugo's minimal built-in Open
Graph set (`og:url`, `og:title`, `og:description`, `og:locale`, `og:type`, `og:image`).
None of this project's ~250 lines of custom meta tags in `opengraph.html` (robots,
googlebot, HandheldFriendly, keywords, canonical-adjacent tags, schema.org itemprops,
pagination link rels, wot-verification, etc.) ever reached production. This is how a
site can silently go a long time with `<meta name="robots">` never appearing on any page.

**The correct override mechanism** (per current Hugo docs, and confirmed empirically
with an isolated reproduction): move the file to `layouts/partials/<name>.html` (or
`layouts/_partials/<name>.html`) and call it with `{{ partial "<name>.html" . }}`
instead of `{{ template "_internal/<name>.html" . }}`. Verified with a minimal
isolated Hugo project:

```
# layouts/_internal/opengraph.html + {{ template "_internal/opengraph.html" . }}
-> renders Hugo's own built-in Open Graph tags, project file is ignored entirely.

# layouts/partials/opengraph.html + {{ partial "opengraph.html" . }}
-> renders the project's custom content correctly.
```

This bug is **specific to names that collide with a real Hugo-provided embedded
partial** (`opengraph.html`, `twitter_cards.html`, `google_news.html`, `disqus.html`,
`google_analytics.html`, etc — check https://gohugo.io/templates/embedded/ for the
current authoritative list). A custom name that does NOT collide with a real Hugo
internal (`microsoft_clarity.html`, `utterances.html`, `schema.html`, `pagination.html`
in this repo) works fine when called via `{{ template "_internal/customname.html" . }}`
- confirmed with an isolated test. Do not assume every `_internal/` file in this repo
has this bug; check each name against Hugo's actual embedded-template list first.

**Diagnostic technique used to find this:** build with `--panicOnWarning` (clean, no
signal) then directly grep the rendered HTML for a tag that should be present
(`<meta name=robots`, remembering minified HTML omits attribute quotes) and confirm
it is missing on both a minified and unminified build. Once missing, bisect by
checking whether OTHER tags emitted later by unrelated logic (`extended_head.html`'s
`theme-color`/`canonical`, which run in a separate partial call) DO appear -- if those
appear but the target tag from the suspect partial does not, and the suspect partial
is invoked via `template "_internal/..."`, suspect this exact bug.

## Bug 2: `relativeURLs = true` Rewrites Absolute href/src Into Depth-Relative Paths

`config/_default/config.toml` (and until this fix, `config/language/en/config.toml`
too) set `relativeURLs = true`. This setting is **not the same** as leaving URLs
absolute-but-root-relative (`/js/x.js`). It rewrites every literal absolute
`href`/`src` HTML attribute into a path relative to the CURRENT page's directory
depth: `./js/x.js` at the site root, `../js/x.js` one level deep, `../../js/x.js`
two levels deep, and so on. Confirmed empirically with an isolated Hugo project:

```
baseURL = "https://example.org/"
relativeURLs = true
# source template: <script src="/js/test.js">
# rendered at site root:        <script src="./js/test.js">
# rendered one level deep:      <script src="../js/test.js">
```

**This does NOT affect Go template helpers** (`.Permalink`, `.RelPermalink`,
`absURL`, `relURL`, `absLangURL`, `relLangURL`) -- those always resolve correctly and
consistently regardless of `relativeURLs`. It ONLY affects the automatic HTML
post-processing pass that rewrites literal `<a href>`, `<script src>`, `<link href>`
attribute values already present in rendered output.

**Real-world symptom observed in Cloudflare access logs:** thousands of 404s for
ever-deepening, garbage URLs like
`/tags/.net-framework-4.0/writeups/guides/practice-tests/recommendhome/checklists/js/sw-prefetch.js`.
Root cause: `extended_head.html`/`prepend_head.html` hardcode
`<script defer src="/js/sw-prefetch.js">`. With `relativeURLs=true`, Netlify's custom
`404.html` (served at whatever deep URL a bot/browser requests, per SPA-style 404
handling) still contains the SAME depth-relative reference computed for `404.html`'s
own nominal root-level depth (`./js/sw-prefetch.js`). A client that resolves this
relative reference against the actual (much deeper) request URL, rather than against
`/404.html`'s own URL, computes an ever-deepening wrong path on every retry, exactly
matching the multi-segment garbage seen in the logs.

**Fix:** set `relativeURLs = false` in `config/_default/config.toml` (and remove the
override in `config/language/en/config.toml`, which had explicitly re-set it to
`true`, overriding the `_default` value for the primary EN build). `canonifyURLs`
can safely stay `true` alongside `relativeURLs = false` -- confirmed with an isolated
test that the combination produces fully-qualified absolute URLs
(`https://example.org/js/x.js`) with no regressions to `.RelPermalink`/`relURL`
output (those remain correctly root-relative, e.g. `/sub/`, regardless of either
setting).

**Verification after the fix:** grep the built HTML for the known-bad reference (e.g.
`sw-prefetch`) on pages at multiple different URL depths (home, a section list page,
a deeply-nested article) and confirm every occurrence resolves to the identical,
fully-qualified absolute URL rather than a depth-varying relative one.

## General Lesson: Config-Level Settings That Silently Corrupt Output With No Build Signal

Both bugs above share a pattern worth remembering for future audits of this repo:
Hugo will build 100% cleanly (`--panicOnWarning`, zero errors) while silently
producing wrong runtime output. Neither bug is detectable by running the build; both
require diffing actual rendered HTML content against what the source templates
clearly intend. When investigating a reported runtime symptom (missing meta tag,
wrong URL, 404 pattern in logs), always:

1. Reproduce the exact symptom in a fresh local build using the real production
   `--config` flag.
2. Grep the rendered output (not just the template source) for the expected content.
3. If the source template clearly should produce X but the rendered output doesn't
   contain X, suspect a config-level setting or a template-call mechanism issue
   before assuming the template logic itself is wrong.
4. Reproduce the suspected mechanism in an isolated minimal Hugo project (a few
   files in `/tmp`) to confirm the exact behavior before touching the real repo.

## Ad Placement Bug Fixed Alongside This (2026-09)

`layouts/partials/ads/random-eager.html` and `random-eager-floating.html` guarded
their ad render with `{{ if and (not .IsHome) (.IsPage) }}`. `.IsPage` is `true` only
for `kind = page` (single content pages); it is `false` for `kind = section` list
pages. This repo has no dedicated `section.html`/`taxonomy.html`/`term.html`
template, so every section/tag/taxonomy list page renders through the shared
`_default/list.html`, which calls these same two ad partials. The `.IsPage` guard
therefore silently zeroed out the eager banner ad and the floating ad on every
list-type page on the site (`/articles/`, `/writeups/`, every `/tags/<x>/` page,
etc.), leaving only the footer's `random-lazy.html` (which has no such restriction)
showing on those pages. Fixed by changing the guard to `{{ if not .IsHome }}` in both
files, matching the pattern `random-lazy.html` already used correctly.

