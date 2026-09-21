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

## Current `bump.md` Policy (User Directive, 2026-09-19)

Do not change `bump.md` for every content or interface commit. Use `bump.md` only
when **at least two** of the following conditions are true:

1. The change is a critical functionality fix which affects every site variant.
2. The content update affects every language.
3. Updating every language version of the site is necessary for the change.

For a minor UI or front-end change, commit the source change without touching
`bump.md`. Let the existing GitHub Actions workflows handle the normal language
builds and deployment timing. Do not create a bump solely to force unrelated
language builds after an ordinary content, rule, or interface change.

Before touching `bump.md`, record which two conditions apply in the commit or
review notes. If fewer than two apply, leave `bump.md` unchanged.

## Pushing a Content Fix to `master` Does Not Guarantee It Deploys (Confirmed 2026-09)

Every `branch_build_hugo_*.yml` workflow (one per language, plus `EN` and `EN_alt`) is
`on: push: branches: [master]` with an explicit `paths:` filter, e.g.
`branch_build_hugo_es.yml` only fires on `contents/**/*.es.md`, `index.es.md`,
`**/index.es.md`, or `bump.md`. **Every single one of these workflows also lists
`bump.md` as one of its trigger paths, and this is the load-bearing fallback, not a
decoration.** When a push's changed-file set does not happen to match a given
language's narrow filter, that language's build silently does not run, and the commit
just sits in `master` unbuilt and undeployed until something else triggers it.

**Symptom observed directly**: after committing a real content fix (2291 files under
`content/**/index.*.md`, touching `**/index.en.md` among others) and pushing it, a
second reported page confirmed the live production HTML at `origin/website-en-alt`
(the branch Netlify actually serves, see `.clinerules/14`) still matched the pre-fix
version. Comparing commit timestamps showed the `website-en-alt` branch's last update
commit predated the fix's push, i.e. the fix had not been built/deployed yet. Fetching
`https://github.com/<owner>/<repo>/actions` and reading the in-progress/queued run list
is the fastest way to confirm whether a given push actually fired the language build
workflows.

**Historical workaround:** appending a trivial change to `bump.md` at the repo root
was the former way to force every `branch_build_hugo_*` workflow. Because `bump.md`
is in every workflow's path filter, that small commit reliably fired all language
builds. This remains useful only when the current two-condition policy above is met.
For ordinary changes, leave `bump.md` untouched and allow the normal GitHub Actions
path filters to decide which builds run.

**Do not assume** that because a workflow's path filter includes a broad pattern like
`**/index.en.md`, every push touching any file under `content/` will fire it — path
filters match the exact file list, and a previous unrelated push (e.g. a docs-only
`.clinerules` commit) can coincidentally satisfy one language's filter (observed
`Branch Build Hugo - es` and `- zh` firing on a clinerules-only commit, unrelated to
their own path filters, likely because those two runs were still catching up from an
earlier queued push) while genuinely missing another's. Verify via the Actions run list
after any push whose deployment matters, rather than assuming the path filter logic
worked as expected.

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

## Invalid JSON-LD in `extended_footer.html` (Fixed 2026-09) and the Raw-HTML-in-Markdown Minifier Flake

Two separate findings from the same investigation. Neither is a content bug in the page that
reported the error.

### Finding 1: trailing comma made `OnlineBusiness` schema invalid on every page

`themes/soshellofriend/layouts/partials/extended_footer.html` ended with an
`OnlineBusiness` JSON-LD block carrying a **trailing comma** after its final property:

```json
"url": "https://simeononsecurity.com",
  }
```

Trailing commas are valid in JavaScript and invalid in JSON, so the block never passed a
strict JSON parser. The consequence is silent: every page shipped invalid
`application/ld+json`, so strict consumers (Google Rich Results, schema validators)
discarded the `OnlineBusiness` schema entirely. Nothing in the build reported it.

**Fix:** remove the trailing comma. Never "fix" this by disabling `--minify` or the JSON
minifier.

### Finding 2: raw HTML in markdown is the minifier flake trigger

After the comma fix, `npx hugo --minify -D --config config/language/en/config.toml`
still failed intermittently, always naming the same page:

```
failed to process "/sibling-sites/index.html": "...:8281:36": expected comma character
or an array or object ending on line 8281 and column 36
```

What the investigation established:

1. **The failure is nondeterministic.** The identical command produced a clean build on
   retry. Measured on the content that existed at the time: 2 failures in 9 minified
   builds (about 22 percent). `Total in ... ms` prints before the error, so the site
   renders fully and then dies in the post-processing pass.
2. **The unminified render of the same page is complete and valid.** Every JSON-LD block
   parses cleanly. The corruption is introduced by the minifier stage only.
3. **Hugo's own debug dump is misleading.** On failure Hugo writes the input to
   `$TMPDIR/hugo-transform-error<N>` and prints a context line whose line number does not
   correspond to the reported position (the error said line 8281, the printed context was
   labelled `16:`). In the dump the closing tag appeared truncated to `</s`. Do not treat
   that dump as ground truth when diagnosing.
4. **The page is the only page on the site that authors raw HTML in markdown.**
   `content/sibling-sites/index.en.md` was the sole file under `content/` containing a
   literal `<script type="application/ld+json">` block or a `<u>` tag. Every other page
   gets its markup from templates and shortcodes.
5. **Both failure positions land at or immediately after that raw `<script>` block.** One
   error resolved at the block's own closing tag, the other inside the mailerlite
   `<style type="text/css">` block which follows it directly in document order.
6. **The ad partials were ruled out.** All 43 files under `layouts/partials/ads/` have
   balanced `div`, `span`, `a`, and `style` tags, and none contains a `<script>`.

**Rule: do not author raw HTML inside markdown content.** This is the convention rule 09
already states ("Use shortcodes instead of raw HTML to avoid this requirement"). Put page
schema in a template or shortcode, and use a `> **Warning:**` blockquote callout instead of
`<u>`. The sibling-sites page had both constructs removed and now matches every other page
in markup provenance.

### Diagnosing a minifier failure on a page you just added

1. **Do not assume your new content is at fault just because the error names your page.**
   The path in the error is the page whose output was being minified, not the origin of the
   malformed token. Retry the build once; if the second run passes, the trigger is
   intermittent.
2. **Compare the minified build against an unminified one.** If
   `hugo -D --config config/language/<lang>/config.toml` (no `--minify`) renders the page
   correctly, the content and templates are fine and the problem is in the minify stage.
3. **Check whether the page authors raw HTML.** Run
   `grep -rn '<[a-z]' content/<section>/<slug>/index.en.md`. If it returns a tag, that is
   the suspect. Remove it.
4. **Validate every JSON-LD block on the built page mechanically** rather than reading
   them. This handles Hugo's minified, unquoted-attribute output:

   ```bash
   python3 - <<'PY'
   import re, json
   html = open('/tmp/build/<page>/index.html', encoding='utf-8').read()
   blocks = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html, re.S)
   print('blocks:', len(blocks))
   for i, b in enumerate(blocks):
       try:
           json.loads(b)
           print(i, 'VALID', len(b))
       except Exception as e:
           print(i, 'INVALID', e)
           print(b[:400])
   PY
   ```

   A `type="application/ld+json"` selector must match on the **unquoted** form too. A
   regex looking for `<script type="application/ld+json">` returns 0 blocks on minified
   output and looks like "there is no JSON-LD here", which is wrong.
3. **Check whether the failing element is inside an ad partial.** `layouts/partials/ads/`
   is the only nondeterministic content in a build (`random-lazy.html` /
   `random-eager.html` / `random-eager-floating.html` pick a random partial per page and
   per build). Confirm with `grep -rn '<script' layouts/partials/ads/`. As of 2026-09 the
   ad partials contain inline `<style>` only and **no** `<script>`, so they cannot be the
   source of a JS or JSON minifier error.
4. The count of JSON-LD blocks on a standard article page is **7**: `Article`,
   `BreadcrumbList`, one `ImageObject` per `{{< figure >}}`, any page-authored `ItemList`,
   and the footer's `OnlineBusiness`. If the count drops, a schema partial silently
   stopped emitting.


## Emitting JSON-LD From a Template Requires `jsonify` Plus `safeJS`

Page-specific structured data belongs in a template, not in the markdown body (see the
raw-HTML finding above). The author profile `Person` entity is the worked example:
`layouts/partials/schema/author_person.html`, called from
`layouts/partials/extended_head.html` behind
`{{ if and .IsPage (eq .Section "authors") }}`.

Build the object with `dict` and `slice` rather than hand-written JSON. That removes the
whole class of trailing-comma and quote-escaping bugs, and it keeps every string escaped by
Go's JSON encoder instead of by hand.

**The trap:** `{{ $person | jsonify }}` alone is not enough. Hugo renders templates with
`html/template`, which treats the inside of a `<script>` element as a JavaScript context.
The `jsonify` output arrives there as a plain string, so the escaper encodes it as a JS
*string literal* and the page ends up with double-encoded JSON:

```
<script type="application/ld+json">"{\"@context\":\"https://schema.org\", ...}"</script>
```

That block fails every strict parser, and the failure is invisible in a browser. The fix is
one more pipe:

```gotemplate
<script type="application/ld+json">{{ $person | jsonify | safeJS }}</script>
```

Note that `site_schema.html` avoids the problem a different way, by hand-writing the JSON and
applying `safeJS` to each interpolated value. Either pattern is fine. Do not mix them.

**Verification:** parse every block rather than eyeballing it. Wrap the parse in a type check,
because a double-encoded block parses successfully as a Python `str` and a naive script
reports it as valid:

```python
import re, json
html = open('/tmp/build/<page>/index.html', encoding='utf-8').read()
for i, b in enumerate(re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html, re.S)):
    obj = json.loads(b)
    if isinstance(obj, str):
        print(i, 'DOUBLE-ENCODED STRING - missing safeJS')
    else:
        print(i, 'VALID', obj.get('@type'))
```

Also confirm the `@id` you emit matches the reference other pages use. `site_schema.html`
points `Organization.founder` at `$baseURL + authors/simeononsecurity/#person`, so the profile
page has to publish a `Person` with that exact `@id` for the two nodes to resolve to one
entity.

