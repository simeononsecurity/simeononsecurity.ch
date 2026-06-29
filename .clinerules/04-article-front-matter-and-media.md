# Article Front Matter, Images, Ads, and Shortcodes

This rule documents the conventions for standard articles (`content/articles/<slug>/index.en.md`)
and guides (`content/guides/<slug>/index.en.md`). Articles and guides share an identical schema.
Use existing articles like `tailscale-vs-headscale-comparison-guide` and `docker-vs-vms` as the
canonical reference. The prose style in `03-content-writing-style.md` still applies to article
bodies.

## Front Matter

Front matter is always **YAML**, delimited by `---` ... `---`. Never use TOML (`+++`). Keys:

- `title` — quoted string. Comparison and guide titles usually carry the current year and a colon
  subtitle, for example `"Tailscale vs Headscale: Complete 2026 Comparison Guide for Self-Hosted VPN"`.
- `date` — original publish date, format `YYYY-MM-DD` only (no time, no timezone).
- `lastmod` — last-updated date, same `YYYY-MM-DD` format. Add or bump this whenever you revise an
  existing article.
- `toc` — boolean, almost always `true`.
- `draft` — boolean, effectively always `false`.
- `description` — one or two skimmable sentences naming the topic and what the page covers.
- `genre` — array of broad topic categories. Optional (some older articles omit it). Include it on
  new content.
- `tags` — array of many specific keyword phrases, often 20 to 40 entries seeded with the title's
  key terms and search variants.
- `cover` — path to the cover image, usually `/img/cover/<slug>.webp` (PNG and other names also
  exist on older posts).
- `coverAlt` — descriptive alt text for the cover image.
- `coverCaption` — short caption, frequently left empty (`""`).

Do **not** add `author` or `authors` keys. Authorship is handled by the single author profile at
`content/authors/simeononsecurity/`, so article front matter carries no author field.

Representative block:

```yaml
---
title: "Topic vs Alternative: Complete 2026 Comparison Guide"
date: 2026-05-24
lastmod: 2026-05-24
toc: true
draft: false
description: "Comprehensive 2026 comparison of X and Y covering features, performance, security, and use cases."
genre: ["Network Security", "Self-Hosted", "Open Source"]
tags: ["x vs y", "x alternative", "y setup", "comparison", "self-hosted"]
cover: "/img/cover/<slug>.webp"
coverAlt: "An illustration showing ... on a dark background."
coverCaption: ""
---
```

## Embedding Images in the Body

Do not use raw markdown `![alt](url)` or `<img>` tags for body images. Use the site's custom
**`{{< figure >}}`** shortcode, which adds lazy loading, `ImageObject` schema, and automatic
affiliate/external `rel` handling.

```text
{{< figure src="wifi-security.webp" alt="A screenshot of the recommended WiFi security configuration" >}}
{{< figure src="T568A.jpg" alt="T568A Wiring Standard" caption="T568A Wiring Standard - showmecables.com" link="https://www.showmecables.com/blog/post/rj45-pinout" >}}
{{< figure src="t740.jpg" alt="HP t740 Thin Client" link="https://amzn.to/3Td6xJE" >}}
```

`figure` parameters:

- `src` — **required**. A bare filename (such as `wifi-security.webp`) resolves to a file sitting
  next to the page's `index.en.md`. A full `http(s)://` URL is used as-is.
- `alt` — **required**. Always provide descriptive alt text.
- `caption` — optional visible caption rendered under the image (supports markdown).
- `link` — optional wrap-the-image link. The shortcode auto-detects the `rel`: known affiliate
  domains (Amazon, `amzn.to`, and the others in the shortcode list) get
  `rel="nofollow noopener external sponsored"`, generic external links get `noopener external`,
  and internal `simeononsecurity.com` links are followed.
- Other optional params: `title`, `class`, `width`, `height`, `target`, `attr`, `attrlink`.

Prefer locally stored `.webp` images placed in the page's own folder, referenced by bare filename.

## Embedding YouTube Videos

Use the **`{{< youtube >}}`** shortcode with the named `id=` parameter form exclusively. Never use
the bare positional form (`{{< youtube VIDEO_ID >}}`).

```text
{{< youtube id="USjZcfj8yxE" >}}
```

- `id` — **required**, the YouTube video ID.
- `playlistid` — optional, to play within a playlist:
  `{{< youtube id="6XqYB1J1vQY" playlistid="PLBQ_gEkQNRZLSWCk7Z0PnwGVBhiKRBugw" >}}`
- Optional `autoplay="true"`, `class`, `title`, `description`.

The shortcode uses the privacy-friendly `lite-youtube` web component and emits `VideoObject` /
`LearningResource` schema, so a single video tag handles SEO and performance for you.

## Advertisements

**Do not hand-place ad code in article bodies.** Site-wide ads (display banners and the rotating OrangeWebsite house ads) are injected automatically by layout partials, not by content authors.

The only in-body ad shortcode is `{{< inarticle-dark >}}`, and its partial is currently commented
out, so it renders nothing. Do not add it to new articles. Leave ad placement to the layouts.

## Other Available Shortcodes

These shortcodes exist in `layouts/shortcodes/` and may be used when relevant:

- `{{< button >}}` and `{{< centerbutton >}}` — call-to-action buttons.
- `{{< gist >}}` — embed a GitHub gist.
- `{{< highlight >}}` — syntax-highlighted code blocks (fenced code blocks are also fine).
- `{{< ref >}}` and `{{< relref >}}` — resolve internal links to other pages.
- `{{< twitter >}}` / `{{< twitter_simple >}}`, `{{< instagram >}}` / `{{< instagram_simple >}}`,
  `{{< vimeo >}}` / `{{< vimeo_simple >}}` — social and video embeds.
- `{{< readfile >}}`, `{{< param >}}`, `{{< jobsdate >}}`, and the `amp-*` family for AMP pages.

Stick to the established shortcodes above instead of writing raw HTML in content.
