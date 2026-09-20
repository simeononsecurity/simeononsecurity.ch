# Hugo Shortcodes and Partials Reference

This rule documents every shortcode in `layouts/shortcodes/` and the notable partials in
`layouts/partials/` that content authors need to know about. Always use these instead of raw
HTML in content files. Rule `04-article-front-matter-and-media.md` covers `figure` and `youtube`
in detail; this file covers the full inventory.

---

## Hugo Architecture Quick Reference

Hugo is a static site generator. Key rules that affect content authoring:

- Every URL must correspond to a file or directory in the `content/` tree.
- A file named `index.md` in a directory marks it as a **leaf bundle** (single page). Hugo
  will not process other Markdown files in that directory.
- A file named `_index.md` in a directory adds user content to Hugo's auto-generated **list
  page** for that directory.
- Templates are selected by content type and location. A file at `content/blog/post.md` uses
  `layouts/blog/single.html` before falling back to `layouts/_default/single.html`.
- The project `layouts/` directory overrides the theme. To customize any theme partial, copy
  it to `layouts/partials/` and edit the copy. The theme files are never modified directly.
- `draft: true` in front matter causes Hugo to silently skip the file. Remove this line in
  production content.
- Embedded HTML in Markdown is only passed through if `markup.goldmark.renderer.unsafe = true`
  is set in the site config. Use shortcodes instead of raw HTML to avoid this requirement.

---

## Shortcodes Available to Content Authors

Shortcodes live in `layouts/shortcodes/`. Use them in Markdown with
`{{< shortcode-name param="value" >}}` or the inner-content form
`{{< shortcode-name >}}inner content{{< /shortcode-name >}}`.

The `{{< >}}` delimiter passes inner content as raw HTML. The `{{% %}}` delimiter parses
inner content as Markdown before passing it to the template. Use `{{< >}}` for most cases.

---

### `figure` — Images with schema and smart link handling

**Required:** `src`, `alt`

```
{{< figure src="filename.webp" alt="Descriptive alt text" >}}
{{< figure src="filename.webp" alt="Alt text" caption="Caption text" >}}
{{< figure src="filename.webp" alt="Alt text" link="https://amzn.to/XXXXX" >}}
```

Parameters:
- `src` — bare filename resolves relative to the page bundle. Full `https://` URL used as-is.
- `alt` — **required**. Always write descriptive alt text for accessibility and SEO.
- `caption` — visible caption under the image. Supports Markdown.
- `link` — wraps the image in an anchor. The shortcode auto-selects `rel`:
  - Known affiliate domains (Amazon, `amzn.to`, etc.) → `rel="nofollow noopener external sponsored"`
  - Generic external links → `rel="noopener external"`
  - Internal simeononsecurity.com links → `rel="follow me"`
- `title` — rendered as an `<h4>` in the figcaption.
- `attr` / `attrlink` — attribution text and link in the caption.
- `credit` — source credit for third-party image metadata. Pair with `attr` and
  `attrlink` for visible attribution. Credited figures omit the default site
  creator, copyright, and licensing claims. Image `contentUrl` uses the resolved
  `src`, independently of an optional click-through `link`.
- `width`, `height` — pass through to the `<img>` tag.
- `class` — CSS class on the `<figure>` element.

The shortcode also emits `ImageObject` JSON-LD schema and sets `loading="lazy"` and
`fetchpriority="low"` automatically. Never use raw `<img>` tags in content files.

**Image sizing guidelines:**
- Diagrams: 900–1200 px wide
- Screenshots: 1400–1800 px wide
- Hero/cover images: 1600–2000 px wide
- Prefer `.webp` format. Name images descriptively: `cluster-overview.webp`, not `image1.png`.

---

### `youtube` — Embedded YouTube video with schema

**Required:** `id`

```
{{< youtube id="USjZcfj8yxE" >}}
{{< youtube id="6XqYB1J1vQY" playlistid="PLBQ_gEkQNRZLSWCk7Z0PnwGVBhiKRBugw" >}}
```

Parameters:
- `id` — **required**. Always use the named `id=` parameter form. Never use positional syntax.
- `playlistid` — optional, to play within a playlist.
- `autoplay` — optional, set to `"true"` to autoplay.
- `title`, `description`, `class` — optional metadata and styling.

The shortcode uses the privacy-friendly `lite-youtube` web component and emits `VideoObject`
and `LearningResource` JSON-LD schema.

---

### `button` — Call-to-action link button

```
{{< button href="https://example.com" description="Optional description" >}}
  Button text
{{< /button >}}

{{< button relref="/articles/my-post/" >}}
  Internal link button
{{< /button >}}
```

Parameters:
- `href` — external URL. Opens in a new tab. Auto-detects affiliate links and applies
  `rel="nofollow noopener external sponsored"` for known affiliate domains.
- `relref` — internal page path. Resolved via Hugo's `relref` function.
- `description` — optional short description rendered below the button.
- `class` — optional additional CSS class.

The button emits `WebPage` schema with `name` and `url`. Link handling mirrors `figure`:
internal links get `rel="follow"`, affiliate links get sponsored rel, other external links
get `rel="noopener external"`.

---

### `centerbutton` — Horizontally centered call-to-action button

Identical to `button` but wraps the output in `<center>`. Use this for standalone CTAs that
should sit centered on the page rather than inline with text.

```
{{< centerbutton href="https://amzn.to/XXXXX" >}}
  Buy on Amazon
{{< /centerbutton >}}
```

---

### `gist` — Embed a GitHub Gist

```
{{< gist username gist-id >}}
{{< gist username gist-id "specific-file.py" >}}
```

Positional parameters: `username`, `gist-id`, optional filename.

---

### `highlight` — Syntax-highlighted code with options

```
{{< highlight python "linenos=table,hl_lines=2 3,linenostart=1" >}}
def hello():
    print("Hello")
{{< /highlight >}}
```

Use fenced code blocks (` ```python`) in most cases. Reserve `highlight` for when you need
line numbers (`linenos=table`) or line highlighting (`hl_lines=`).

---

### `readfile` — Include a file's raw content

```
{{< readfile "/static/scripts/example.sh" >}}
```

Single positional parameter: path relative to the project root. The file content is output
as raw HTML. Use for embedding shared scripts or config snippets from `static/`.

---

### `ref` / `relref` — Resolve internal page URLs

```
[Link text]({{< ref "/articles/my-post/" >}})
[Link text]({{< relref "/guides/setup/" >}})
```

`ref` returns the absolute URL. `relref` returns the URL relative to the current page.
Use these only when you need to verify at build time that the target page exists. For most
internal links, a plain root-relative Markdown link (`[text](/path/to/page/)`) is simpler.

---

### `twitter` / `twitter_simple` — Embed a tweet

```
{{< twitter user="simeononsec" id="1234567890" >}}
{{< twitter_simple user="simeononsec" id="1234567890" >}}
```

`twitter_simple` omits the extra JS and renders a lighter embed.

---

### `instagram` / `instagram_simple` — Embed an Instagram post

```
{{< instagram shortcode >}}
{{< instagram_simple shortcode >}}
```

---

### `vimeo` / `vimeo_simple` — Embed a Vimeo video

```
{{< vimeo 146022717 >}}
{{< vimeo_simple 146022717 >}}
```

---

### `param` — Output a site or page parameter

```
{{< param "author" >}}
```

Outputs the value of a named front matter or site parameter.

---

### `jobsdate` — Output a dynamic date for job/career pages

```
{{< jobsdate >}}
```

Outputs a formatted date string used in career playbook pages to indicate when data was
last reviewed.

---

### `inarticle-dark` — In-article ad slot (currently disabled)

```
{{< inarticle-dark >}}
```

The corresponding partial is commented out. This renders nothing. Do not add it to new
articles. Ad placement is handled automatically by layouts.

---

### AMP shortcodes — AMP-compatible embeds

These shortcodes exist for AMP page variants and are rarely needed in standard content:

- `{{< amp-adsense >}}` — AdSense in AMP context
- `{{< amp-gif src="..." >}}` — GIF in AMP context
- `{{< amp-iframe src="..." >}}` — iframe in AMP context
- `{{< amp-image src="..." >}}` — image in AMP context
- `{{< amp-video src="..." >}}` — video in AMP context

Do not use these in standard (non-AMP) content pages.

---

### `__h_simple_assets` — Internal theme helper (do not use)

This shortcode is an internal theme utility. Do not call it from content files.

---

## Notable Partials (for layout authors, not content authors)

Partials live in `layouts/partials/`. They are called from templates, not from content
Markdown. Content authors do not call partials directly. This section is reference for
when modifying templates.

### Ad partials (`layouts/partials/ads/`)

- `random-lazy.html` — randomly selects a lazy-loading ad from the registered ad pool.
  This is the primary ad injection point in article layouts.
- `random-eager.html` — eager-loading variant for above-the-fold ad slots.
- `random-eager-floating.html` — fixed-position floating ad, hidden below 900 px viewport.
- `ads/stscollective/` — product-line ad partials: `stscollective`, `rayhunter`,
  `flockyou`, `eyespy`. Each has `-lazy`, `-eager`, and `-eager-floating` variants.
- `ads/signalandsteel/` — Signal & Steel brand ad partials including banner variants.

To add a new ad partial to the rotation, add its path to the `$ads` slice in
`layouts/partials/ads/random-lazy.html`. Follow the conventions in rule `07-ad-cta-guidelines.md`.

### Schema partials (`layouts/partials/schema/`)

- `articlecarosel.html` — emits `ItemList` / carousel JSON-LD for article listing pages.

### Other partials

| Partial | What it does |
|---------|-------------|
| `site_schema.html` | Emits site-wide `Organization` and `WebSite` JSON-LD schema |
| `quiz_jsonld.html` | Emits `Quiz` and `LearningResource` JSON-LD for practice-test pages |
| `breadcrumbs.html` | Renders breadcrumb nav and emits `BreadcrumbList` JSON-LD |
| `share-buttons.html` | Social share buttons (Twitter/X, LinkedIn, etc.) |
| `authorblock.html` | Author bio block rendered at the bottom of articles |
| `relatedcontent.html` | "Related articles" section based on Hugo's related-content engine |
| `referredarticles.html` | Curated "you may also like" links |
| `disclosurefooter.html` | FTC affiliate disclosure footer |
| `donatebutton.html` | Donate / support button |
| `editbuttons.html` | "Edit on GitHub" and "Report an issue" buttons |
| `comments.html` | Comment section integration |
| `extended_head.html` | Additional `<head>` tags injected per-page |
| `prepend_head.html` | Tags inserted at the very top of `<head>` |
| `google_tag_manager.html` | GTM snippet |
| `googleadsload.html` | Google AdSense script loader |
| `amazonadsload.html` | Amazon Associates script loader |
| `instantpage.html` | instant.page prefetch library |
| `load_service_worker.html` | Service worker registration |
| `yieldToMain.html` | `scheduler.postTask` / `setTimeout` yield helper for INP |
| `console-log.html` | Injects a console.log Easter egg |
| `mailerlite.html` | Mailing list signup form |
| `cybersentinelsclub.html` | Cyber Sentinels Club promo block |
| `blocks/image.html` | Reusable image block used inside other partials |

---

## Homepage (`layouts/_default/index.html`) Search Was Missing Its Runtime (Fixed 2026-09)

The homepage (Hugo `kind = home`, template `themes/soshellofriend/layouts/_default/index.html`)
had the search `<form>`/`<input id="search-query">` markup (with the schema.org `SearchAction`
metadata) but was missing every piece `static/js/search.js` actually needs to run: no
`#search-results`/`#search-pagination`/`.search-loading` containers, no `#search-result-template`,
and no `<script>` tags for Fuse.js, Mark.js, or `search.js` itself. Submitting the form only did a
full-page GET redirect to `/search?q=...`; it never searched in place on the homepage the way the
dedicated `layouts/section/search.html` page does.

**Fix:** copy the exact same results container / template / library `<script>` block from
`layouts/section/search.html` into the homepage template, right after the existing `.search-form`
div. The `<form>`'s plain GET submit is left untouched as the no-JS fallback; `search.js` calls
`event.preventDefault()` on submit and intercepts input events for progressive enhancement, so both
paths keep working. This is homepage-only (Hugo's `kind = home` uses `_default/index.html`
specifically, never `list.html` or `single.html`), so this had zero effect on `/search` or any
section/list page.

**Verification technique:** build locally, then use `jsdom` (`npm install jsdom fuse.js@6.6.2` in a
scratch `/tmp` dir) to load the real built homepage HTML, inject the real pinned Fuse.js version,
mock `fetch("/index.json")` with the real built `/index.json`, `eval()` the real `static/js/search.js`
unmodified, dispatch a real `input` event on `#search-query`, and assert `#search-results` renders
actual result markup (not the empty-state) for a query known to match real content, the empty-state
for a nonsense query, and pagination links for a broad query. This is the same jsdom pattern used to
validate `search.js` itself; it also works for any other page template that embeds the search widget.

## robots.txt Disallow Directives Do Not Inherit Across `User-agent:` Groups

`static/robots.txt` and `layouts/_default/robots.txt` repeat the same `Disallow:` lines (e.g.
`/quiz-dicts/`, `/presskit.zip`) inside every distinct `User-agent:` group in the file (the
wildcard `*` group, the SEO-crawler group, each image-crawler group, the AI-crawler group, the
general-crawler group). This is intentional and required: per the robots.txt spec, a crawler only
applies the rules in the single most-specific group that names it (or the wildcard group if no
named group matches), so a path added only to the `User-agent: *` block has zero effect on
`Googlebot-Image`, `SemrushBot`, `GPTBot`, etc. **When adding a new `Disallow:` path that should
apply site-wide, add it to every group's repeated disallow block, not just the wildcard group.**
Confirmed by adding `Disallow: /carousel/` (see below) to all 9 occurrences of the repeated
`Disallow: /quiz-dicts/` block using a script that inserts the new line immediately before each
occurrence, then verifying the count of both lines matches (9 == 9) and no line is malformed.

## `/carousel/` Noindexed and Hardened (Fixed 2026-09)

`content/carousel/_index.en.md` (rendered by `layouts/section/carousel.html`) aggregates every
cover image on the site into one page with no unique text content, a classic thin/duplicate-content
page that also has no reason to be crawled by search engines and is a magnet for image-scraping
bots. It already had `sitemap_ignore: true` but was missing `robotsdisallow: true`, so
`layouts/partials/opengraph.html` was still emitting `<meta name="robots" content="index, follow...">`
for it. Added `robotsdisallow: true` (front matter key already wired up in `opengraph.html`, see the
`content/admin` honeypot page for the original pattern) and added `Disallow: /carousel/` to every
`User-agent:` group in both `static/robots.txt` and `layouts/_default/robots.txt` (see rule above).

Separately, the carousel's own `<img>` tags (both the server-rendered initial batch and the ones
inserted by the `IntersectionObserver` lazy-batch-loader in `carousel.html`) had no `onerror`
handling, so a single broken/blocked image request (bot noise, a stale Cloudflare cache entry, a
dead file) left a permanently-broken tile in the grid instead of being dropped. Added
`onerror="this.closest('.carousel-item').remove()"` to the initial-batch `<img>` and an equivalent
`img.onerror = function () { wrapper.remove(); }` in the JS batch-loader so a bad image just
disappears instead of showing a broken-image icon forever.

Also deleted `layouts/section/image-carousel.html`, a stale, unreferenced duplicate of the same
page (no `content/` file anywhere sets `layout: "image-carousel"`) that predated `carousel.html`'s
lazy-batching/click-to-expand rewrite and had none of its fixes. Confirmed dead via
`grep -rn "image-carousel\|image_carousel" content/ layouts/ static/_redirects` before deleting.

## Donate/Sponsor Button CSS Had a Stale Duplicate in `style-base.css` (Fixed 2026-09)

`layouts/partials/donatebutton.html` (the fixed floating "Support SimeonOnSecurity" CTA,
rendered via `extended_footer.html` on every page) had two real problems: it used the
identical `position: fixed; bottom: 20px; left: 20px; z-index: 9999` coordinates as every
floating ad partial (`stscollective`, `eyespy`, `rayhunter`, `flockyou`, `signalandsteel`,
`audible`, `bitdefender`, `presearch`, etc.), so on any viewport >= 901px (where those ads
are visible) the donate button and the floating ad rendered stacked in the exact same
corner; and its hover state swapped the brand pink background for a flat gray
(`var(--background-secondary)`), losing the CTA's visual identity on interaction.

**The fix looked simple (rewrite the inline `<style>` block in the partial) but a second,
independent bug made the first build of the fix appear to silently fail**:
`themes/soshellofriend/assets/style-base.css` (loaded render-blocking on every page via
`prepended_head.html`) had its own stale, legacy copy of `.sponsor-button` /
`.sponsor-button a` rules using the old flat-gray-hover, non-offset styling. Because that
selector (`.sponsor-button a`, specificity 0,1,1) is more specific than the partial's new
`.sponsor-button-link` class selector (0,1,0), it kept winning regardless of the two
stylesheets' load order, so the built HTML still showed the old CSS text after the partial
was edited. **Lesson: when a component's styling doesn't seem to update after editing its
partial's own `<style>` block, grep every theme-level CSS file
(`themes/soshellofriend/assets/*.css`) for the same class name before assuming the edit
didn't take effect** — a leftover duplicate rule elsewhere in the cascade can win purely on
specificity, independent of document order. Fixed by deleting the stale block from
`style-base.css` and leaving a comment pointing back at the partial as the single source of
truth.

**Also fixed while investigating**: `.sponsor-button` now offsets to `bottom: 296px` at
`min-width: 901px` (the breakpoint where the floating ad partials switch from `display:none`
to visible) so the two CTAs stack vertically instead of overlapping, gained a `max-width`
so the long i18n label (`support_button_text`, up to ~48 chars in English) can't overflow a
narrow viewport, gained a `:focus-visible` outline and a `prefers-reduced-motion` guard
(this was the first use of that media query anywhere in the theme's CSS), and the dead
`@media (max-width: 767px) { .sponsor-button a::after { margin: auto; } }` rule (targeted a
`::after` pseudo-element that never existed in the markup) was removed entirely.

**Caution for anyone re-running a full local Hugo build while investigating a CSS/asset
issue**: do NOT `rm -rf resources/_gen` before rebuilding. Unlike `resources/_gen/assets`
(gitignored), `resources/_gen/images` is intentionally committed to git as a build-cache
artifact (see `.clinerules/13-image-webp-conversion-pipeline.md`). Deleting it and rebuilding
regenerates thousands of files that git then reports as locally modified/deleted; recover
with `git checkout -- resources/` immediately after the rebuild completes, before committing
anything else. A cold-cache rebuild (no `resources/_gen`) also takes roughly 2x as long
(~240s vs ~110s locally) since every image variant gets reprocessed from scratch instead of
reused from cache.

## Hugo Content File Conventions for This Site

- All content lives in `content/`. Articles use `content/articles/<slug>/index.en.md`.
  Guides use `content/guides/<slug>/index.en.md`.
- Place images in the same directory as the `index.en.md` file they belong to. Reference
  them by bare filename in `{{< figure >}}`. Hugo resolves them relative to the page bundle.
- Use `toc: true` in front matter for any page over 1,500 words. Hugo renders a table of
  contents from `##` and `###` headings automatically.
- The `<!--more-->` separator in the body controls what appears as the article summary on
  list pages. Place it after the first two to three sentences.
- `draft: true` silently prevents Hugo from building the page. Remove it before publishing.
- `lastmod:` in front matter should be bumped whenever the article is revised. The site
  displays "Last updated" from this field.
- The `layout:` front matter key selects a specific template. Quiz pages use
  `layout: "<exam>_quiz"` to load the quiz section template. Do not set `layout` on ordinary
  articles or guides.

## YouTube Privacy Defaults and Explicit Embeds

`config/_default/privacy.toml` sets `[privacy.youtube] disable = true`. Ordinary
YouTube shortcodes therefore render no player. For an explicitly requested embed,
use the per-shortcode opt-in rather than changing the global privacy setting:

```text
{{< youtube id="VIDEO_ID" enable="true" title="Actual video title" uploadDate="VERIFIED_ISO_DATE" >}}
```

The `enable="true"` parameter overrides the global disable flag for this instance
only. It does not override `privacyEnhanced`: the player still uses YouTube's
privacy-enhanced host when configured. Disabled instances emit neither the loader
nor the player. Keep a normal YouTube watch link in the article as a fallback.

Players load on click by default. `autoload="true"` opts into the component's
intersection-triggered iframe loading. `nocookie` and `autoload` are presence-based
boolean attributes in lite-youtube 1.5.0: emitting `nocookie="false"` or
`autoload="false"` still enables them, so omit false attributes entirely.

`title` is interpolated into `videotitle` rather than emitted as the literal
`$title`. `uploadDate` is optional and must come from verified video metadata.
When unknown, omit it instead of substituting the article's publication date.
The loader falls back to direct loading if the site's `yieldToMain` helper is
unavailable. The no-JavaScript fallback links to the normal YouTube watch URL.

After a build, verify `<lite-youtube videoid=...>` exists for the requested video.
A bare video ID or loader-script URL does not establish a working embed. Test
both the enabled instance and an ordinary shortcode under the disabled global
setting. Check the video title, privacy attribute, absence of automatic loading,
and accurate VideoObject upload date in rendered output.

## Sibling Sites: Subdomain Tools and the English-Only Footer "Tools" Group (Added 2026-09)

SimeonOnSecurity runs six standalone tools on dedicated `simeononsecurity.com`
subdomains. They are grouped on the site as **sibling sites**: a tool with a full
application behind it (its own dataset, build pipeline, and subdomain) rather than a
browser-only utility on the main domain.

| Subdomain | Project | What it does | Data source | Freshness |
|---|---|---|---|---|
| `heliummap.simeononsecurity.com` | `track-helium-mobile-wifi` | Maps Helium Mobile and Helium Free WiFi hotspots | WiGLE.net + Helium Blockchain Exporter API | Upstream repo archived 2025-04-29, so the map is a dated snapshot |
| `offloadsearch.simeononsecurity.com` | `location-search-tool` | Rates one address for carrier offload | FCC Broadband Map, Nominatim, Google Maps / Foursquare / Yelp | Static page, client-side |
| `openroamingmap.simeononsecurity.com` | `track-openroaming-passpoint` | Maps Hotspot 2.0, Passpoint, and OpenRoaming APs | WiGLE.net | Daily rebuild, yearly reset with archives |
| `flockfinder.simeononsecurity.com` | `flock-finder` | Maps suspected Flock Safety ALPR cameras by WiFi OUI fingerprint | WiGLE.net + public OUI research | Daily at 06:00 UTC, 730-day retention |
| `eyespy.simeononsecurity.com` | `eye-spy` | Web flasher and dashboard for ESP32 passive surveillance detection firmware | None (device telemetry only) | Firmware releases, M5Stack Atom Lite |
| `flockyouesp32.simeononsecurity.com` | `flock-you-esp32` | Web flasher and dashboard for WiFi promiscuous-mode Flock Safety camera detection | None (device telemetry only) | Fork of `colonelpanichacks/flock-you`, ESP32 DevKit and M5 boards |
| `atsresumeimprover.simeononsecurity.com` | `ats-resume-improver` | ATS resume scoring, keyword gap analysis, cover letter generation | None (browser-local, optional user-supplied AI key) | React + Vite + TypeScript + Docker |
| (no subdomain, repository only) | `track-carrier-openroaming-support` | Tracks OpenRoaming support per carrier PLMNID with NAPTR and SRV lookups | mcc-mnc.com PLMNID list | Weekly GitHub Actions run, results committed to the README |

Facts worth keeping straight when writing about these tools:

- **Flock Finder records are heuristics, not confirmations.** An OUI match means the
  MAC prefix matches a known Flock Safety prefix. Prefixes get shared, reassigned, or
  spoofed, and WiGLE data arrives sporadically because the cameras wake only to upload.
  Always pair a Flock Finder claim with a "suspected" qualifier and suggest on-site
  confirmation.
- **Helium Map is the only sibling site whose upstream repo is archived.** State the
  archive date rather than claiming a live daily cadence.
- **Eye Spy is firmware, not a website feature.** The subdomain hosts a web flasher and
  dashboard, and the flashing target is an M5Stack Atom Lite (ESP32-PICO-D4).
- **Two sibling sites are camera-detection firmware and they are not duplicates.**
  `eye-spy` (M5Stack Atom Lite, wider sensor list, one RGB score LED) and
  `flock-you-esp32` (a fork of `colonelpanichacks/flock-you`, any ESP32 with 4MB flash,
  five WiFi and BLE detection techniques, Flask GPS wardriving dashboard, $5 to $12
  builds). Keep the distinction in prose rather than describing them as the same tool.
- **`track-carrier-openroaming-support` has no subdomain.** Its output is a carrier table
  and a realm lookup table, so it publishes through the repository README and a weekly
  GitHub Actions run. It lives on the `/sibling-sites/` page under `## Related Research
  Projects` and must **not** be added to the footer Tools group, which lists subdomains
  only. The repo's About panel points at `simeononsecurity.com`, not a subdomain, which is
  the tell.

### The `/sibling-sites/` Hub Page

`content/sibling-sites/index.en.md` is the index for all six. It carries one `##`
section per tool, each ending in a `{{< centerbutton >}}` CTA, plus a `## Sibling Sites
at a Glance` two-column table, a `## What Counts as a Sibling Site` section that
contrasts sibling sites against the browser-only utilities on `/tools/`, a `## Why They
Live on Subdomains` section, an `## ItemList` JSON-LD block, and a `## Next Steps`
section. Cover and inline images were generated with
`tools/generate_cover_images.py --content-dir all --slug sibling-sites --force
--include-inline-images`.

Only an `index.en.md` file exists in the directory, which is what makes the page
English-only. Do not add translated `index.<lang>.md` files for it.

### The Footer "Tools" Group Is Language-Gated

`themes/soshellofriend/layouts/partials/footer.html` carries a fourth nav group, `Tools`,
between `<nav class="footer__nav">` and the `Company` group. It links `/sibling-sites/`
plus all six subdomains. The whole group sits inside:

```gotemplate
{{ if or (eq .Site.Language.Lang "en") (eq .Site.Language.Lang "EN") }}
```

Sibling sites are English-only, so the group must never render on the translated
subdomains. Adding a new sibling site means three edits: the new tool's content page (if
it gets one), the footer group, and the `/sibling-sites/` page. `partialCached` already
keys the footer by `.Site.Language.Lang`, so the per-language render is cached correctly.

Two details to watch:

- **`{{ ("sibling-sites/" | absURL) }}` resolves against the language baseURL.** The EN
  config (`config/language/en/config.toml`) sets `baseurl = "https://simeononsecurity.ch"`,
  so the footer link on the EN site points at the `.ch` domain while the tool subdomains
  stay on `.com`. This matches every other `absURL` link already in the footer.
- **`{{< button >}}` and `{{< centerbutton >}}` build their `title` attribute from
  `$.Page.Title`, not from the inner button text.** On a page with six CTAs, every tool
  button therefore carries the page title as its tooltip. This is existing shortcode
  behavior, not a bug introduced by the sibling-sites page. Fix the shortcode if a
  per-button title ever matters.

External subdomain links in the footer use `target="_blank" rel="noopener external"`,
matching the social icon row.

