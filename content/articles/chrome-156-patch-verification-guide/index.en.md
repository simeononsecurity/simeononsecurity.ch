---
title: "Chrome 156 Security Update: Verify the October 2026 Patch"
date: 2026-10-28
lastmod: 2026-10-28
toc: true
draft: false
description: "Check the October 27 Chrome 156 security release on Windows, macOS, Linux, and Android. Compare the installed build, finish a pending relaunch, and check managed devices separately."
genre: ["Browsers", "Security", "Patch Management"]
tags: ["Chrome 156", "Chrome security update", "Chrome patch verification", "Chrome version check", "Chrome 156 Windows", "Chrome 156 macOS", "Chrome 156 Linux", "Chrome 156 Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "browser patching", "Chrome Enterprise Core", "managed browsers", "Chromium security", "browser updates", "Chrome relaunch", "chrome://version", "chrome://settings/help", "Android Chrome update", "Brave security updates", "Edge security updates"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Illustration of a padlock and shield representing a security update, not a Chrome version screen"
coverCaption: ""
---

**Chrome's October 27, 2026 security release** lists 52 security fixes. To check your installation, compare its full version with the release for your operating system, then restart Chrome to finish any pending update. An announced version does not prove your device has received the update. ([Chrome desktop release](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## What version should you see?

Google published these Stable-channel versions on October 27, 2026. The desktop release lists separate Windows/macOS and Linux builds. The [Android release](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) names its own build and says Android releases contain the same security fixes as corresponding desktop releases "unless otherwise noted."

| Platform | Build in Google's October 27 announcement |
|---|---|
| **Windows** | 156.0.8078.73 or 156.0.8078.74 |
| **macOS** | 156.0.8078.73 or 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Use this table for the October 27 release, not as a permanent target. Consult the current [Chrome Releases feed](https://chromereleases.googleblog.com/) for later security updates.* Google said the desktop rollout would take "the coming days/weeks" and the Android build would reach Google Play over the next few days. A device below the listed build still needs a check, even during a staged rollout. ([Desktop notice](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [Android notice](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

The [desktop security-fixes list](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) labels four reported flaws **Critical**: FileSystem memory corruption [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), FileAPI improper input validation CVE-2026-118331, Skia improper input validation CVE-2026-118348, and Layout use-after-free CVE-2026-118344. The same notice lists further **High** and **Medium** CVEs. The 52 figure describes security fixes in the release, not 52 independently verified exploit reports. NVD describes CVE-2026-118306 as affecting Chrome versions before 156.0.8078.73. ([NVD record](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**The release notice does not assert active exploitation** of these listed vulnerabilities. Its warning concerns disclosure timing: "Access to bug details and links may be kept restricted until a majority of users are updated with a fix." Do not treat restricted issue details as evidence of exploitation. ([Desktop notice](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Check and finish the desktop update

1. Open **`chrome://version`** in the Chrome installation you use. Record its full version and operating system, not merely the major version 156. A Chrome window on another channel or installed in another location needs its own check.
2. Open **`chrome://settings/help`**, or select **More > Help > About Google Chrome**. Google says Chrome checks for updates on this page. Wait for the check to finish. ([Google's desktop update instructions](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Select **Relaunch** if the page offers it. Save unfinished work first. Close any remaining Chrome windows, reopen the browser, and check **`chrome://version`** again. The recorded version after relaunch is the one to compare with the platform table.
4. If the version is still below the announced build, check again for an available update. If an organization manages the browser or the updater reports an error, contact its administrator rather than assuming a successful download means the running browser has changed.

> **Expected result:** After relaunch, the running Stable-channel Chrome build meets the applicable October 27 version or a later vendor-announced build. A pending Relaunch button is not completion evidence.

On **Android**, open Play Store > profile icon > Manage apps & device, then update Chrome under Updates available if offered. Open Chrome > More > Settings > About Chrome to read the installed version. Compare it with the Android row after the app update finishes. These menu paths follow [Google's Android instructions](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Verify managed fleets

For enrolled browsers, use the Google Admin console's **Chrome versions report** to find older builds by operating system. Open the Browser Versions view, select the relevant organizational unit, inspect the full minor version, and export the CSV if you need a device-by-device worklist. Google says the report includes browsers with reports in the previous 28 days. It notes potential reporting delay, especially for large fleets. ([View Chrome version details](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Separate reported inventory from live verification.** Review each device's last report time and channel, then confirm outliers directly in the browser or through your managed endpoint inventory. Google counts separate Chrome installations, such as Stable and Beta, separately. Browser reporting requires enrollment and [managed browser reporting](https://support.google.com/chrome/a/answer/9301421?hl=en). A machine missing from a report is not evidence of a patched installation.

## Check Chromium derivatives separately

**Chrome's version table applies to Google Chrome.** Microsoft Edge, Brave, and other Chromium-based browsers have their own packages, release numbers, and update schedules. The Chrome announcement does not establish their patch status. Check each browser's installed version and its own security advisory or release notes for the relevant Chromium fixes. Do not compare an Edge or Brave product version directly with Chrome's 156.0.8078.73 number and declare it patched.

For each derivative, record its product name, channel, installed build, vendor advisory URL, and the vendor's stated fixed build. If its vendor has not confirmed a fix, mark the status **unverified** and follow the named vendor's update guidance. Keep Chrome and derivative results in separate rows of your inventory.

## Sources and references

- [Chrome Releases: Stable Channel Update for Desktop, October 27, 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Desktop builds, 52 fixes, CVEs, and vendor disclosure wording.
- [Chrome Releases: Chrome for Android Update, October 27, 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Android build and corresponding desktop fixes caveat.
- [Chromium issue tracker: M156 security-fixes query](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Linked from the desktop release. Individual issue details depend on disclosure access.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) and [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Vulnerability descriptions and affected Chrome versions. Severity labels above follow Google's notice, not an NVD CVSS assessment.
- [Google Chrome Help: Update Google Chrome on computers](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) and [on Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Update checks and version menu paths.
- [Chrome Enterprise Help: View Chrome version details](https://support.google.com/chrome/a/answer/10025748?hl=en) and [turn on managed browser reporting](https://support.google.com/chrome/a/answer/9301421?hl=en). Fleet reporting prerequisites and limitations.
