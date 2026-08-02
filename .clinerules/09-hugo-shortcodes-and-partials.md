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
