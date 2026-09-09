# Welcome to the SimeonOnSecurity Website Source Code

[![Sponsor](https://img.shields.io/badge/Sponsor-Click%20Here-ff69b4)](https://github.com/sponsors/simeononsecurity)

<a href="https://simeononsecurity.com" target="_blank" rel="noopener noreferrer">
  <h2>Explore the World of Cybersecurity</h2>
</a>
<a href="https://simeononsecurity.com" target="_blank" rel="noopener noreferrer">
  <img src="https://simeononsecurity.com/img/banner.webp" alt="SimeonOnSecurity Logo" width="300" height="300">
</a>

## Introduction

Welcome to the SimeonOnSecurity website! Here, we provide the latest information, articles, and resources related to cybersecurity. Our goal is to offer valuable insights and promote best practices to help you stay safe and secure in the digital world.

## Badges

[![Netlify Status](https://api.netlify.com/api/v1/badges/920d9bff-3d07-4c34-849b-f4f9100adb87/deploy-status)](https://app.netlify.com/sites/simeononsecurity/deploys)
[![Test Hugo Latest Version](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/hugo.yml/badge.svg)](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/hugo.yml)
![Greetings](https://github.com/simeononsecurity/simeononsecurityweb/workflows/Greetings/badge.svg)
[![VirusTotal Scan](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/virustotal.yml)
[![ClamAV Scan](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/git_av_scan.yml/badge.svg)](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/git_av_scan.yml)
[![HTML Validation](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/html_verify_built.yml/badge.svg)](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/html_verify_built.yml)
[![Push Sitemap to Bing IndexNow and Google Indexing API](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/sitemap_submission.yml/badge.svg)](https://github.com/simeononsecurity/simeononsecurity.ch/actions/workflows/sitemap_submission.yml)

## Technologies Used

- [CloudFlare](https://www.cloudflare.com/): Utilized for Proxy, CDN, Caching, and Country Blocking.
- [Hugo Extended](https://gohugo.io/): Used for Static Site Generation.
- [Hugo - Hello Friend Theme](https://themes.gohugo.io/hugo-theme-hello-friend/): A modern and user-friendly theme.
- [Node.js](https://nodejs.org/en/): A dependency for Hello Friend, used for dynamic theme generation.
- [Netlify](https://www.netlify.com/): Used for Hosting, SSL Registration, Forms, and Automated Hugo Site Generation.
- [glotta](https://github.com/simeononsecurity/glotta): Used for article translations, supporting 16 languages. Developed by [1nf053c](https://github.com/1nf053c).
- [Progressive Web App / Service Workers](https://web.dev/progressive-web-apps/): Implemented to improve site usability and accessibility. 
  - We're looking for help with [this issue](https://github.com/simeononsecurity/simeononsecurity.ch/issues/487).

## Responsible Disclosure

SimeonOnSecurity.ch supports the [security.txt](https://securitytxt.org/) [RFC](https://tools.ietf.org/html/draft-foudil-securitytxt-10). If you discover any security concerns or vulnerabilities with our website or any of our repositories, please report them following the details outlined [here](https://simeononsecurity.com/.well-known/security.txt).

Verified reports will be acknowledged in the [SimeonOnSecurity Hall of Fame](https://simeononsecurity.com/hof).

## Guest Blogging
We are excited to announce that we now accept guest blog submissions on topics related to cybersecurity, information technology, automation, programming, coding, best practices, compliance, security regulations, and more. If you have valuable insights and expertise to share with our audience, we welcome your contributions. For guidelines and submission details, please refer to our [Guest Blogging Guidelines](https://simeononsecurity.com/guest-posts).

## About Our Advertising Opportunities
At SimeonOnSecurity, we offer a range of advertising options to help you promote your brand and reach a targeted audience of security enthusiasts and professionals. Our [Advertising page](https://simeononsecurity.com/advertise/) provides detailed information about the ad sizes and slots we support, ensuring optimal performance and quality for your advertisements. Partner with us to showcase your products and services to our engaged community. Explore the various opportunities available to grow your reach and connect with like-minded individuals in the cybersecurity industry.

## Notable Features & Optimizations

This is a statically generated site, but it's engineered well past what most static
sites ship with. A few things we're proud of:

### Performance & Caching
- **Tiered edge caching tuned per asset type.** `netlify.toml` sets distinct
  `Cache-Control` policies for HTML, JS/CSS, XML feeds, JSON quiz banks, and
  immutable images, splitting browser TTL from CDN (`s-maxage`) TTL so Cloudflare
  can serve stale-but-safe responses for far longer than a browser should cache
  them.
- **A real Service Worker with a minimal precache.** `static/service-worker.js`
  precaches only `/` and `/offline.html` (a ~1.7KB SVG-based fallback, down from a
  ~49KB inline-base64 version) instead of eagerly force-fetching every script on
  install, so first-install cost stays tiny while the app-shell/runtime caching
  strategy still makes repeat visits and offline navigation fast.
- **Live-search runs entirely client-side.** `/search` and the homepage both ship
  a Fuse.js + Mark.js powered fuzzy search against a prebuilt `index.json`, with
  debounced live-as-you-type results, in-place client-side pagination (no re-fetch
  per page), and graceful empty/error states. No server, no database, no
  third-party search SaaS.
- **Every image is served responsively and lazily.** The custom `figure`
  shortcode auto-generates multiple `.webp` resolutions with `srcset`/`sizes`,
  lazy-loads below-the-fold images, and emits `ImageObject` schema, all from a
  single shortcode call in Markdown.
- **Font and image preloading is hand-tuned, not guessed at.** `preload-fonts.html`
  and `preload-images.html` emit exact-match `<link rel="preload"/prefetch">` tags
  keyed to the same `.Resize` cache strings the actual partials use, so the
  browser starts fetching the *exact* bytes that will render, not a near-miss that
  gets fetched twice.

### Security
- **A real, enforced Content-Security-Policy**, plus `Strict-Transport-Security`
  (HSTS with `preload`), `X-Frame-Options`, `X-Content-Type-Options`, and a locked
  down `Permissions-Policy` disabling camera, microphone, USB, geolocation, and
  more by default, all set at the edge via `netlify.toml`.
- **`security.txt` (RFC 9116) support** at `/.well-known/security.txt`, with a
  public [Hall of Fame](https://simeononsecurity.com/hof) for researchers who
  report issues responsibly, and a dedicated
  [`SECURITY.md`](./SECURITY.md) disclosure policy.
- **Automated malware/virus scanning on every push.** GitHub Actions runs a
  [VirusTotal scan](.github/workflows/virustotal.yml) and a full
  [ClamAV git-history scan](.github/workflows/git_av_scan.yml) against the repo,
  not just a one-time check.
- **A live canary-token honeypot** (`content/admin/index.html`) that fires an
  alert if anyone actually goes digging where they shouldn't, kept out of search
  engines and sitemaps via `robotsdisallow`/`sitemap_ignore` front matter.
- **Locked-down CI.** Every `branch_build_hugo_*.yml` workflow does a full,
  non-shallow (`fetch-depth: 0`) Hugo build per language so `Lastmod`/GitInfo data
  stays accurate, and `html_verify_built.yml` validates the actual built HTML
  output on every push before it ships.

### SEO & Structured Data
- **A per-bot-family `robots.txt` built for the AI-crawler era**, over 350 lines
  distinguishing search bots, image bots, AI/LLM training and RAG bots
  (`GPTBot`, `ClaudeBot`, `PerplexityBot`, etc.), archive bots, and SEO scrapers,
  each with its own `Crawl-delay` and IETF
  [Content-Signal](https://contentsignals.org/) directives (`ai-train=no,
  search=yes, ai-input=yes`) stating exactly how the content may and may not be
  used, per bot family, not one blanket rule.
- **Eight distinct XML output formats** generated straight from Hugo: standard
  RSS, a full-text RSS variant, a Google News sitemap, a SmartNews feed, an image
  sitemap, and a combined sitemap index, across every language, all validated for
  well-formedness and self-referencing `atom:link` correctness in CI.
- **JSON-LD structured data everywhere it matters**: `Organization`/`WebSite`
  site-wide schema, `ImageObject` on every figure, `VideoObject`/
  `LearningResource` on every embedded YouTube video, `Quiz`/`LearningResource` on
  every practice test, and `ItemList` carousels on article listing pages.
- **Automatic search-engine push on publish.** A scheduled GitHub Action
  ([`sitemap_submission.yml`](.github/workflows/sitemap_submission.yml)) submits
  the sitemap to Bing IndexNow and the Google Indexing API daily, instead of
  waiting for a crawl.

### Accessibility & PWA
- **Installable as a real Progressive Web App**, with a full `manifest.json`
  covering iOS, Android, and Windows tile icon sets, an offline fallback page,
  and background-sync-friendly service worker caching.
- **Raw HTML is intentionally avoided in content.** Every image, video, button,
  and social embed goes through a purpose-built Hugo shortcode
  (`figure`, `youtube`, `button`, `gist`, `twitter`, `instagram`, `vimeo`, ...)
  so accessibility attributes, lazy-loading, and schema markup stay consistent
  across hundreds of content pages without any single article having to get it
  right by hand.

### Content Scale & Automation
- **16 fully translated languages** via the in-house
  [glotta](https://github.com/simeononsecurity/glotta) translation pipeline, each
  published to its own subdomain with its own sitemap and RSS feed (see the table
  below).
- **Certification practice tests with real question banks**, not a handful of
  sample questions: each exam ships a deterministically generated (seeded), 100+
  question-per-domain JSON bank, versioned and served straight from the CDN.
- **AI-assisted, pipeline-generated cover and inline imagery** for every article
  and guide, with automatic WebP compression, alt-text generation, and stem-aware
  duplicate detection so the same image is never regenerated twice.
- **89 top-level content sections and 500+ articles, guides, and writeups**, all
  built, translation-checked, and HTML-validated automatically on every push
  across 18 parallel per-language build workflows.

## Domains Built with This Source

This source code has been used to build the following domains:

| Domain | Local Name | Sitemap | RSS Feed |
|--------|------------|---------|---------|
| [https://simeononsecurity.ch](https://simeononsecurity.ch) | English | [Sitemap](https://simeononsecurity.ch/sitemap.xml) | [RSS](https://simeononsecurity.ch/index.xml) |
| [https://simeononsecurity.com](https://simeononsecurity.com) | English | [Sitemap](https://simeononsecurity.com/sitemap.xml) | [RSS](https://simeononsecurity.com/index.xml) |
| [https://ar.simeononsecurity.com](https://ar.simeononsecurity.com) | Arabic | [Sitemap](https://ar.simeononsecurity.com/sitemap.xml) | [RSS](https://ar.simeononsecurity.com/index.xml) |
| [https://bn.simeononsecurity.com](https://bn.simeononsecurity.com) | Bengali | [Sitemap](https://bn.simeononsecurity.com/sitemap.xml) | [RSS](https://bn.simeononsecurity.com/index.xml) |
| [https://ca.simeononsecurity.com](https://ca.simeononsecurity.com) | Catalan | [Sitemap](https://ca.simeononsecurity.com/sitemap.xml) | [RSS](https://ca.simeononsecurity.com/index.xml) |
| [https://de.simeononsecurity.com](https://de.simeononsecurity.com) | German | [Sitemap](https://de.simeononsecurity.com/sitemap.xml) | [RSS](https://de.simeononsecurity.com/index.xml) |
| [https://es.simeononsecurity.com](https://es.simeononsecurity.com) | Spanish | [Sitemap](https://es.simeononsecurity.com/sitemap.xml) | [RSS](https://es.simeononsecurity.com/index.xml) |
| [https://fr.simeononsecurity.com](https://fr.simeononsecurity.com) | French | [Sitemap](https://fr.simeononsecurity.com/sitemap.xml) | [RSS](https://fr.simeononsecurity.com/index.xml) |
| [https://hi.simeononsecurity.com](https://hi.simeononsecurity.com) | Hindi | [Sitemap](https://hi.simeononsecurity.com/sitemap.xml) | [RSS](https://hi.simeononsecurity.com/index.xml) |
| [https://it.simeononsecurity.com](https://it.simeononsecurity.com) | Italian | [Sitemap](https://it.simeononsecurity.com/sitemap.xml) | [RSS](https://it.simeononsecurity.com/index.xml) |
| [https://ja.simeononsecurity.com](https://ja.simeononsecurity.com) | Japanese | [Sitemap](https://ja.simeononsecurity.com/sitemap.xml) | [RSS](https://ja.simeononsecurity.com/index.xml) |
| [https://nl.simeononsecurity.com](https://nl.simeononsecurity.com) | Dutch | [Sitemap](https://nl.simeononsecurity.com/sitemap.xml) | [RSS](https://nl.simeononsecurity.com/index.xml) |
| [https://pa.simeononsecurity.com](https://pa.simeononsecurity.com) | Punjabi | [Sitemap](https://pa.simeononsecurity.com/sitemap.xml) | [RSS](https://pa.simeononsecurity.com/index.xml) |
| [https://pl.simeononsecurity.com](https://pl.simeononsecurity.com) | Polish | [Sitemap](https://pl.simeononsecurity.com/sitemap.xml) | [RSS](https://pl.simeononsecurity.com/index.xml) |
| [https://pt.simeononsecurity.com](https://pt.simeononsecurity.com) | Portuguese | [Sitemap](https://pt.simeononsecurity.com/sitemap.xml) | [RSS](https://pt.simeononsecurity.com/index.xml) |
| [https://ro.simeononsecurity.com](https://ro.simeononsecurity.com) | Romanian | [Sitemap](https://ro.simeononsecurity.com/sitemap.xml) | [RSS](https://ro.simeononsecurity.com/index.xml) |
| [https://ru.simeononsecurity.com](https://ru.simeononsecurity.com) | Russian | [Sitemap](https://ru.simeononsecurity.com/sitemap.xml) | [RSS](https://ru.simeononsecurity.com/index.xml) |
| [https://zh.simeononsecurity.com](https://zh.simeononsecurity.com) | Chinese | [Sitemap](https://zh.simeononsecurity.com/sitemap.xml) | [RSS](https://zh.simeononsecurity.com/index.xml) |
