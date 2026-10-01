---
title: "Module 2: Web Browsing and Tracking"
date: 2026-09-30
lastmod: 2026-09-30
toc: true
draft: false
description: "How stateful and stateless tracking differ, which browser changes reduce collection, why fingerprint tweaks are lower yield than they appear, and what incognito does not protect against."
genre: ["Personal Security", "Web Browsing", "Privacy", "Tracking", "Browser Security"]
tags: ["browser privacy", "tracking", "cookies", "browser fingerprint", "third-party cookies", "tracker blocking", "ad blocking", "privacy browser", "search engine privacy", "dns over https", "incognito", "browser extensions", "https", "tor", "personal security course"]
cover: "/img/cover/web-browsing-tracking-privacy-illustration.webp"
coverAlt: "An illustration of a browser window with tracking identifiers flowing toward collection points while a shield filters them, on a dark background with teal accents."
coverCaption: "Module 2: reduce what the browser reports about you"
---

#### [← Return to the Personal Security Course](/personal-security-course-start/)

**The browser is where most of your personal data exposure happens.** It holds your authenticated sessions, reports a detailed description of your device to every site you visit, and executes code written by parties you never chose to trust.

This module covers the two distinct tracking mechanisms, the changes which reduce collection, and an honest accounting of which popular advice is lower yield than it appears.

*Budget about 30 minutes. Two settings and one extension produce most of the benefit.*

## What You Will Learn

- **Distinguish** stateful tracking, which depends on stored identifiers, from stateless tracking, which does not
- **Explain** why the HTTPS padlock proves confidentiality rather than trustworthiness
- **Configure** a privacy-respecting browser with tracker and cookie controls
- **Evaluate** a browser extension's access before installing it
- **Identify** which fingerprint countermeasures are worth the effort and which are not
- **Produce** a browser record listing your browser, search engine, and installed extensions

| Term | Meaning |
|---|---|
| **Stateful tracking** | Identifying you through something stored, such as a cookie or a local storage entry |
| **Stateless tracking** | Identifying you from characteristics of the request itself, with nothing stored |
| **First-party cookie** | Set by the site you are visiting, and generally needed for it to function |
| **Third-party cookie** | Set by another domain embedded in the page, and the main cross-site tracking mechanism |
| **Fingerprint** | The combination of attributes which distinguishes your browser from others |
| **Container** | An isolated browser profile with its own cookies and storage |

## Two Kinds of Tracking, Two Kinds of Countermeasure

**Confusing these two mechanisms is why browser privacy advice often contradicts itself.**

| | Stateful | Stateless |
|---|---|---|
| **Mechanism** | Cookies, local storage, cached identifiers | Screen size, fonts, timezone, GPU strings, canvas rendering |
| **Persistence** | Survives until cleared or expired | Recomputed on every request |
| **Countermeasure** | Block, isolate, or clear the store | Make yourself less distinctive |
| **Difficulty** | Straightforward | Hard, and it breaks sites |
| **Yield** | **High** | Moderate at best |

**The practical consequence.** Blocking third-party cookies and trackers is high-yield and low-cost, so it belongs at the top of the list. Fingerprint randomization is a partial measure against a moving target, so it belongs near the bottom.

*Anyone who spoofs their canvas signature before installing a content blocker has the ordering inverted.*

## Step 1: Choose the Browser

Your browser sees everything you do, which makes this the highest-leverage single choice in the module.

| Browser | Strength | Cost |
|---|---|---|
| **Firefox** | Configurable, independent engine, strong container support | Needs tuning to reach its potential |
| **Brave** | Blocks trackers by default, no setup required | Chromium-based, and its own features deserve review |
| **LibreWolf** | Hardened Firefox defaults | Fewer conveniences, and some sites break |
| **Tor Browser** | Anonymity against network observers, not only sites | Slower, and many sites block it |
| **Chrome, Edge, Safari** | Convenience and integration | Collect telemetry and offer weaker isolation by default |

**If you change nothing else, move off Chrome.** Its business model depends on data about your browsing, and the alternative browsers cost nothing.

See the full comparison in **[Best Privacy Browsers 2026: LibreWolf vs Brave vs Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**.

## Step 2: Block the Collection Layer

**Ads and trackers are the primary collection mechanism on the web**, and they are also a substantial attack surface. Two changes cover most of the ground.

### Content and Tracker Blocking

| Tool | What It Blocks | Note |
|---|---|---|
| **uBlock Origin** | Ads, trackers, and known malicious domains | The default recommendation for Firefox |
| **Tracker blockers** | Analytics and cross-site beacons | Use one, not several |
| **Brave Shields** | Built in, no extension needed | Suitable if you prefer zero configuration |

**Use exactly one.** Stacking blockers causes conflicts, slows the browser, and makes breakage harder to diagnose.

### Cookie and Storage Controls

- **Block third-party cookies.** This is the single highest-yield browser setting available.
- **Clear cookies regularly**, or scope them to a container so they never reach other sites.
- **Review site permissions** for location, camera, microphone, and notifications, which are granted per origin and persist silently.

### Compartmentalization

**Isolating contexts prevents one identity from being linked to another.** Firefox containers are the cleanest implementation, giving each profile its own cookie jar. The practical setup is one container per purpose: work, shopping, social, and personal. Sites in different containers never observe each other's storage.

*This is high value and often skipped, because it requires a small amount of ongoing discipline rather than a one-time toggle.*

## Step 3: Reduce the Fingerprint

**Fingerprinting identifies you by what your browser reports**, including screen dimensions, installed fonts, timezone, language settings, and the exact output of canvas rendering. It does not require storing anything.

A useful property: **a distinctive fingerprint is worse than a common one.** The goal is not uniqueness, it is blending in.

| Measure | Yield | Trade-off |
|---|---|---|
| **Use a popular browser default configuration** | Good | You lose some convenience settings |
| **Disable WebRTC where unused** | Moderate | Breaks video calling in the browser |
| **Spoof canvas output** | Moderate | Breaks some image-heavy sites |
| **Rotate user agent** | Low | Marginal benefit, and it makes you more distinctive |
| **Send Do Not Track** | **None** | Most sites ignore it, and it adds a distinguishing signal |

> **Common Mistake: treating fingerprint randomization as a primary control.** It is a partial measure against a technique which is designed to survive partial measures. Do the cookie and tracker work first.

## Where Incognito Helps and Where It Does Not

**Incognito prevents local storage, not remote observation.** It stops your browser from recording history and cookies on your own device. It does nothing about what the network operator, the site, or your employer observes.

| Incognito Protects | Incognito Does Not Protect |
|---|---|
| Local history and cookies | Your IP address |
| Saved form data in the session | Network-level observation |
| Session persistence on a shared machine | The site's own server logs |
| | Fingerprinting |

**Use it on other people's machines**, which is its genuine strength. Do not treat it as anonymity.

## Site Legitimacy and the Padlock Myth

**The padlock indicates encryption, not honesty.** Certificates are free and automated, so almost every phishing site has one. Confidentiality and trustworthiness are separate properties.

Signs worth checking:

- **Verify the domain letter by letter**, especially for login pages and anything involving payment
- **Prefer bookmarks over links** for sites you use often
- **Treat unexpected redirects as a warning**, and check where a short link resolves before following it
- **Trust browser warnings**, which reflect observed malicious behavior rather than configuration

Browser malware produces its own signals: a changed homepage or search engine, unfamiliar toolbars or extensions, a jump in ad volume, and pages loading far slower than before. Any of those justifies an extension audit.

## The Browser Record

```text
BROWSER RECORD
Browser:               ______________________
Search engine:         ______________________
Content blocker:       ______________________  (exactly one)
Third-party cookies:   blocked / allowed / partial
Container profiles:    ______________________
Extensions installed:
  - ______________________  why kept: __________
  - ______________________  why kept: __________
Permissions revoked:   camera / microphone / location / notifications
```

*Review the extension list quarterly. An extension you installed once and forgot still reads every page you visit.*

{{< figure src="browser-tracking-stateful-vs-stateless.webp" alt="Diagram contrasting stateful tracking through cookies and local storage with stateless tracking through browser fingerprint attributes, showing which countermeasure applies to each" >}}

## Next Steps

1. **Continue to Module 3** and secure the account which unlocks everything else: **[Email Security](/personal-security-course/email/)**
2. **Compare browsers properly** before switching: **[LibreWolf vs Brave vs Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**
3. **Inspect what a site exposes** with the local **[EXIF Viewer](/exif-viewer/)** before sharing media
4. **Check your deployment's security headers** if you also run a website: **[Security Headers Check](/securityheaders/)**
5. **Read the organizational counterpart** if you manage browsers for others: **[Web Application Security Checklist](/checklists/web-application-security-checklist/)**