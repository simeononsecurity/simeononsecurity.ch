---
title: "Module 2: Web Browsing and Tracking"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Audit browser tracking, storage, permissions, extensions, private mode, and profile separation. Verify improvements without claiming anonymity."
genre: ["Personal Security", "Web Browsing", "Privacy", "Tracking", "Browser Security"]
tags: ["browser privacy", "tracking", "cookies", "browser fingerprint", "third-party cookies", "tracker blocking", "ad blocking", "privacy browser", "search engine privacy", "dns over https", "incognito", "browser extensions", "https", "tor", "personal security course"]
cover: "/img/cover/web-browsing-tracking-privacy-settings.webp"
coverAlt: "An illustration of a web browser interface on a dark background, featuring tabs for privacy settings and abstract icons representing tracking mechanisms like cookies and fingerprinting, highlighted in vibrant colors."
coverCaption: "Module 2: reduce what the browser reports about you"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**The browser holds authenticated sessions and exposes device and request details to sites.** The browser also executes site code, stores local state, and mediates camera, microphone, location, and notification permissions.

This module covers the two distinct tracking mechanisms, the changes which reduce collection, and an honest accounting of which popular advice is lower yield than it appears.

*Budget about 30 minutes. Start with storage, tracking, permission, and extension review.*

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
| **Stateless tracking** | Linking activity through browser, device, network, or behavior signals without a stored browser identifier |
| **First-party cookie** | Set in the context of the site you are visiting for functions such as sessions, preferences, or measurement |
| **Third-party cookie** | Set in a third-party context and used for purposes which might include cross-site tracking |
| **Fingerprint** | The combination of attributes which distinguishes your browser from others |
| **Container** | An isolated browser profile with its own cookies and storage |

## Two Kinds of Tracking, Two Kinds of Countermeasure

**Confusing these two mechanisms is why browser privacy advice often contradicts itself.**

| | Stateful | Stateless |
|---|---|---|
| **Mechanism** | Cookies, local storage, cached identifiers | Browser APIs, protocol fields, screen size, fonts, timezone, GPU strings, canvas rendering |
| **Persistence** | Survives until cleared or expired | Recomputed or reused across requests, depending on the technique |
| **Countermeasure** | Block, isolate, or clear the store | Make yourself less distinctive |
| **Difficulty** | Direct browser controls exist | Some changes affect compatibility or uniqueness |
| **Practical starting point** | Browser controls directly address stored identifiers | Test carefully because unusual changes might increase uniqueness |

**The practical consequence.** Start with third-party storage and tracking controls because browsers expose direct settings for them. Fingerprint changes need testing because a rare configuration might become easier to distinguish.

*Anyone who spoofs their canvas signature before installing a content blocker has the ordering inverted.*

## Step 1: Choose the Browser

Your browser handles site content, local storage, sessions, permissions, and updates. Choose one with current support on your device.

| Browser | Strength | Cost |
|---|---|---|
| **Firefox** | Configurable, independent engine, strong container support | Needs tuning to reach its potential |
| **Brave** | Blocks trackers by default, no setup required | Chromium-based, and its own features deserve review |
| **LibreWolf** | Hardened Firefox defaults | Fewer conveniences, and some sites break |
| **Tor Browser** | Routes traffic through the Tor network and standardizes many browser attributes | Entry and exit observation, account sign-in, behavior, and endpoint compromise still matter |
| **Chrome, Edge, Safari** | Platform integration and built-in safety controls | Privacy behavior depends on settings, platform, and account use |

**Choose from your device support, accessibility needs, update policy, extension needs, and privacy controls.** Safari includes tracking protections on Apple platforms. Firefox, Brave, and Tor Browser serve different goals. Recheck vendor documentation after major releases.

See the full comparison in **[Best Privacy Browsers 2026: LibreWolf vs Brave vs Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**.

## Step 2: Block the Collection Layer

**Ads, analytics, embedded services, account activity, and browser signals create distinct collection paths.** Which data exists depends on the site, browser, settings, account state, and third parties. Content and tracking controls address part of this set.

### Content and Tracker Blocking

| Tool | What It Blocks | Note |
|---|---|---|
| **uBlock Origin** | Ads, trackers, and known malicious domains | The default recommendation for Firefox |
| **Tracker blockers** | Analytics and cross-site beacons | Use one, not several |
| **Brave Shields** | Built in, no extension needed | Suitable if you prefer zero configuration |

**Start with one blocker.** Multiple tools might overlap, increase breakage, or complicate diagnosis. Add another only for a documented gap.

### Cookie and Storage Controls

- **Block or partition third-party cookies.** This reduces a common cross-site identifier with low setup cost.
- **Clear cookies regularly**, or scope them to a container so selected site storage stays inside the chosen context.
- **Review site permissions** for location, camera, microphone, and notifications, which are granted per origin and persist silently.

### Compartmentalization

**Isolating contexts separates selected cookies and site storage.** Firefox containers support one context per purpose, such as work, shopping, social, and personal. They do not stop correlation through account sign-ins, IP addresses, fingerprinting, payment data, or shared identifiers.

*This separation needs ongoing discipline because sign-ins and exceptions might reconnect the contexts.*

## Step 3: Reduce the Fingerprint

**Fingerprinting uses browser and device signals to distinguish or link activity with varying confidence.** Signals include screen dimensions, installed fonts, timezone, language settings, and canvas rendering output. The technique does not require a stored cookie.

A useful property: **a distinctive fingerprint is worse than a common one.** The goal is not uniqueness, it is blending in.

| Measure | Intended Effect | Trade-off |
|---|---|---|
| **Use a supported browser configuration shared by many users** | Reduces selected uniqueness | You lose some convenience settings |
| **Limit WebRTC where unused** | Reduces an unused feature and selected address-exposure paths | Breaks browser calling |
| **Spoof canvas output** | Changes one fingerprint signal | Might break sites or make a rare setup easier to distinguish |
| **Rotate user agent** | Changes a reported identifier | Mismatch with other signals might increase uniqueness |
| **Send Do Not Track** | Expresses a preference | Compliance depends on site policy and applicable law |

> **Common Mistake: treating fingerprint randomization as a primary control.** It is a partial measure against a technique which is designed to survive partial measures. Do the cookie and tracker work first.

## Where Incognito Helps and Where It Does Not

**Private mode uses temporary local session state and limits saved browsing history.** Cookies and storage exist during the session, then the browser removes selected state when all private windows close. Downloads, bookmarks, device logs, malware, networks, and sites remain outside this protection.

| Incognito Protects | Incognito Does Not Protect |
|---|---|
| Local history and cookies | Your IP address |
| Saved form data in the session | Network-level observation |
| Session persistence on a shared machine | The site's own server logs |
| | Fingerprinting |

**Avoid signing in on an untrusted computer.** Private mode does not stop keyloggers, hostile extensions, screen capture, downloads, or an abandoned session. Use your own updated device. If access is unavoidable, use a low-value account, refuse password saving, sign out, and revoke the session later from a trusted device.

## Site Legitimacy and the Padlock Myth

**The padlock indicates transport encryption, not site honesty.** A phishing site also uses HTTPS. Read the domain and use a saved bookmark for high-value accounts.

Signs worth checking:

- **Verify the domain letter by letter**, especially for login pages and anything involving payment
- **Prefer bookmarks over links** for sites you use often
- **Treat unexpected redirects as a warning**, and check where a short link resolves before following it
- **Stop at browser warnings** and inspect the exact cause. Certificate errors, an incorrect clock, a captive portal, extensions, managed policy, and known malicious behavior require different responses

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

*Review the extension list quarterly. An extension sees data allowed by its declared and granted permissions. Remove access which no longer serves a clear purpose.*

{{< figure src="browser-tracking-stateful-vs-stateless.webp" alt="Diagram contrasting stateful tracking through cookies and local storage with stateless tracking through browser fingerprint attributes, showing which countermeasure applies to each" >}}

## Practice and Verify

Create a fresh browser profile. Keep your daily profile closed during this test.

1. Update the browser and record its exact version.
2. Set third-party cookie or tracking protection to the vendor's recommended strict option.
3. Review camera, microphone, location, notification, and pop-up permissions.
4. Install no extension at first. Visit two normal sites you use.
5. Add one reviewed blocker, repeat the visits, and record visible breakage.
6. Sign in to a test account inside one container or profile. Confirm another container or profile stays signed out.

> **Expected Result:** unwanted permissions are absent, the second context has no shared login cookie, and both test sites still complete their main task.

If a site breaks, disable the newest control for the affected site, repeat the task, then record the smallest exception. If contexts share a login, check whether the browser opened both tabs in the same profile or the site used a shared identity provider. Containers separate selected storage. They do not provide anonymity.

```text
REDACTED EXAMPLE
Browser/version:       Firefox [version removed]
Profile:               course-test
Tracking setting:      strict
Extensions:            one reviewed blocker
Permission changes:    notifications removed from 3 sites
Isolation test:        shopping signed in, personal signed out
Breakage and fix:      checkout blocked, site-only exception
```

**Pass checklist**

- [ ] Browser and extensions receive supported updates
- [ ] Every extension has a stated purpose and reviewed permissions
- [ ] Sensitive site permissions match current use
- [ ] A fresh profile or container test shows storage separation
- [ ] The record makes no anonymity claim

**Primary references, checked 2026-10-10:** [Mozilla Multi-Account Containers](https://support.mozilla.org/en-US/kb/containers) and [Firefox privacy and security features](https://support.mozilla.org/en-US/kb/firefox-privacy-and-security-features).

## Next Steps

1. **Continue to Module 3** and secure an account used for many recovery paths: **[Email Security](/personal-security-course/email/)**
2. **Compare browsers properly** before switching: **[LibreWolf vs Brave vs Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**
3. **Inspect metadata in an image file** with the local **[EXIF Viewer](/exif-viewer/)** before sharing media
4. **Check your deployment's security headers** if you also run a website: **[Security Headers Check](/securityheaders/)**
5. **Read the organizational counterpart** if you manage browsers for others: **[Web Application Security Checklist](/checklists/web-application-security-checklist/)**
