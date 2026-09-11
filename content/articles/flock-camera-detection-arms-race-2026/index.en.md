---
title: "Flock Camera Detection Arms Race: What Changed in 2026"
date: 2026-09-10
lastmod: 2026-09-10
toc: true
draft: false
description: "Flock-You users are reporting zero detections on drives that used to catch cameras every time. Here is what changed in Flock Safety's hardware, why BLE and the old management AP both stopped working, how the open-source detection community responded, and an emerging infrared-based detection approach that skips WiFi entirely."
genre: ["Privacy Technology", "Counter Surveillance", "Open Source Projects", "Digital Rights", "Network Security", "Security Research", "Hardware Hacking", "Privacy Tools"]
tags: ["Flock Safety", "ALPR", "Flock-You", "OUI Detection", "Wildcard Probe Request", "Promiscuous Mode WiFi", "802.11 Monitoring", "DeFlockJoplin", "NitekryDPaul", "BLE Detection", "5GHz WiFi", "Locally Administered MAC", "SSID Pattern Matching", "Counter Surveillance Hardware", "STS Collective", "colonelpanichacks", "Detection Evasion", "ESP32", "WiFi Detection", "Surveillance Awareness", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "GitHub Issue Tracking", "Firmware Update", "Anti-Fingerprinting", "MAC Randomization", "Information Element Fingerprinting", "Channel Hopping", "Privacy Advocacy", "Open Source Security", "Mass Surveillance", "Detection Firmware", "Wardriving", "Camera Uprooting", "Privacy Hardware", "Infrared Detection", "IR Illuminator", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Optical Detection", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "An urban scene with a Flock camera on a lamppost and a vehicle equipped with a high-tech detection device. Glowing signals illustrate wireless data communication in a dark background."
coverCaption: "How Flock Safety's shifting hardware keeps breaking open-source detection tools, and how the community keeps catching up"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**If your Flock-You detector has gone quiet on a route that used to catch cameras every time, you are not imagining it, and your hardware probably is not broken.** Flock Safety's camera hardware and firmware have changed at least twice in the last year in ways that broke the community's detection methods, and open-source researchers have had to reverse-engineer a new signature each time.

*This is a fast-moving story. The detection method and OUI list below reflect the `colonelpanichacks/flock-you` `main` branch as of September 2026. Check the [GitHub repository](https://github.com/colonelpanichacks/flock-you) before assuming your device is defective.*

{{< youtube id="cVf-id71BuQ" >}}

*The video above, from Valleytech Custom Solutions, documents exactly the symptom this article explains: a routine war drive that suddenly returns zero detections across multiple firmware builds, on a route where cameras were reliably detected before, in a county where several previously-flagged cameras had physically disappeared.*

______

## A War Drive That Suddenly Turned Up Nothing

The pattern shows up the same way for almost everyone who reports it. A driver runs a route they have driven dozens of times. Their detector, running current firmware, has caught the same cameras before. Then, on one drive, it catches nothing. Not a single beep, not a single log entry, across every custom firmware build they try.

The Valleytech video above describes exactly this: a daily route to the post office that always registered at least one Flock camera stopped registering any, and a second route past Micro Center that used to flag five cameras now shows only one still active, with the other four physically uprooted from their poles.

**Two things were happening on the same timeline, and it is easy to confuse them:**

- **Cameras are being physically removed or relocated** in some areas, which genuinely reduces the number of devices there are to detect.
- **The wireless signature the cameras broadcast has changed**, which means even a camera still sitting on its pole will not trigger detection hardware running outdated firmware.

Two separate GitHub issues on the `colonelpanichacks/flock-you` repository, filed months apart, document the second problem in detail. Reading them in order tells the story of how the community's detection method has had to evolve twice already.

______

## Issue #20: The Management AP Went Dark

**[Issue #20](https://github.com/colonelpanichacks/flock-you/issues/20)**, opened in January 2026, started with a familiar complaint: a user tested their device next to a known Flock camera, documented on DeFlock, and got nothing. Over the following weeks, more users piled on with the same result, from Florida to Indiana to Atlanta to the Midwest, using different hardware and different antennas.

One commenter asked the question that turns out to matter most: **had Flock changed something on their end, in a way that broke detection for everyone at roughly the same time?**

The project maintainer, colonelpanichacks, eventually confirmed exactly that. **Around December 2025, Flock deactivated the management access point their cameras used to broadcast.** That AP was the original basis for wireless detection. When it disappeared, the community pivoted to Bluetooth Low Energy (BLE) signals as a substitute. That substitute also stopped working reliably by spring 2026.

| Detection surface | Status |
|---|---|
| **Management WiFi AP** | Deactivated by Flock, approximately December 2025 |
| **BLE beaconing** | Stopped working reliably, spring 2026 |
| **Cellular LTE uplink** | Still in use for cloud upload, but not passively detectable |
| **Wildcard 802.11 probe requests** | Current basis for detection (see below) |

*Every custom firmware built around the old AP or BLE detection paths is now looking for a signal the cameras stopped sending. That is why a device that used to work goes completely silent without anything being wrong with the hardware.*

______

## The Replacement Method: Wildcard Probes and Frame Fingerprinting

The current `flock-you` firmware runs in dedicated 802.11 promiscuous mode. The radio never transmits and never joins a network. It only listens, hopping WiFi channels 11, 6, and 1 at a 250-millisecond dwell time to keep pace with how often the cameras themselves change channel.

**A detection now requires all of the following to line up before the firmware alerts:**

1. The frame is an 802.11 **Management Probe Request** (type 0, subtype 4).
2. The **SSID Information Element is present with length 0**, meaning it is a wildcard probe rather than one asking for a specific network.
3. The transmitter address (**addr2**) matches one of the known Flock OUI prefixes.
4. The rest of the frame's Information Elements match the fingerprint pattern the DeFlockJoplin community documented, based on Pintor and Atzori's 2022 research on **[WiFi probe request IE fingerprinting](https://ieeexplore.ieee.org/document/10001618)**.

This method is named `wifi_wildcard_probe_ie_sig` in the firmware. Field testing by the DeFlockJoplin community caught **11 of 12 known cameras with only 2 false positives** along their test route, the same field-verified baseline cited in the project's own **[hardware guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**. The 12th camera used an OUI that has since been added to the list below.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Timeline diagram showing the Flock camera detection method evolving from a management WiFi access point, through Bluetooth Low Energy beaconing, to the current wildcard probe request and information element fingerprint, with a fourth stage showing emerging SSID, 5GHz, and MAC address evasion" >}}

______

## The Current OUI List

The wildcard-probe fingerprint above only fires after the transmitter's MAC address matches one of the OUI prefixes the community has confirmed against real Flock hardware. The list is maintained primarily by researcher **@NitekryDPaul**, with the 31st entry contributed by the **DeFlockJoplin** community after it caught a camera the original 30-entry list missed.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**This list is not static.** The upstream research notes several prefixes that were tested and then demoted (one turned out to be a Sony media player, another an early placeholder that never matched anything). Two entries are flagged as low-confidence and one, `82:6b:f2`, is deliberately kept even though it is a locally-administered address, because filtering it out would have silently dropped a real, confirmed DeFlockJoplin detection.

*If you maintain your own firmware fork, pull the OUI list from the upstream `datasets/` folder rather than hardcoding a copy. The list changes as the research does, and a stale copy is a slow, silent way to start missing cameras again.*

______

## Issue #43: New SSID Pattern, 5GHz, and MAC Anti-Fingerprinting

Three months after Issue #20 closed, a second report arrived that describes what looks like a deliberate anti-detection countermeasure rather than an incidental firmware change. **[Issue #43](https://github.com/colonelpanichacks/flock-you/issues/43)**, filed in May 2026, is built on WiGLE wardriving data captured against a camera already confirmed on DeFlock, and it documents three findings none of the existing tooling accounted for.

### Finding 1: A Different SSID Format

The documented Flock hotspot SSID has always followed the pattern `Flock-XXXXXX`. The camera in this report broadcast **`Flock Camera net.`** instead, a completely different naming convention. Anyone searching WiGLE for the `Flock-*` wildcard, as several researchers had been doing, would get zero results for this camera even though it was actively broadcasting.

### Finding 2: A Confirmed 5GHz Hotspot

The same camera broadcast simultaneously on **2.4GHz channel 1** and **5GHz channel 157**, using sequential MAC addresses on each band (`...9f:a2:de` and `...9f:a2:df`), which points to a single dual-band WiFi module assigning adjacent addresses to each radio rather than two unrelated devices. A separate, independent report from researcher nsm_barii had already logged a Flock probe request on 5GHz channel 149, so this is now two data points confirming 5GHz operation is real and not a one-off misconfiguration.

**Every detection method described earlier in this article, including the current wildcard-probe firmware, only listens on 2.4GHz.** A camera broadcasting exclusively (or primarily) on 5GHz is invisible to that hardware regardless of OUI list accuracy.

### Finding 3: Locally Administered MAC Addresses on the Hotspot

Both captured MAC addresses have the **locally administered bit set**, meaning they were not assigned from Flock's real IEEE-registered OUI block. The standard `flock-you` detection logic deliberately skips locally administered addresses, because that is the standard way to filter out MAC-randomizing phones and laptops.

**That filter, which exists specifically to reduce false positives, means a Flock camera using a locally administered MAC on its hotspot interface gets filtered out by the exact same logic meant to clean up noise.** The sequential last bytes on the two captured addresses rule out random generation, which is what makes this look like intentional, structured address assignment rather than coincidence.

| Finding | What still works despite it |
|---|---|
| **New SSID format** (`Flock Camera net.`) | SSID pattern matching still works if the match pattern is broadened |
| **5GHz operation** | Nothing in current WiFi-only firmware, since detection only scans 2.4GHz |
| **Locally administered MAC** | SSID pattern matching, since it does not depend on MAC address at all |

*SSID-based matching is the one method in this table that keeps working regardless of which band the camera uses or how its MAC address is assigned. That is the practical argument for adding broader SSID pattern support rather than relying on OUI matching alone.*

______

## Is Flock Deliberately Evading Detection?

Neither GitHub issue proves intent, and it is worth being precise about that. Issue #43's own author raised it as an open question rather than a conclusion: is this consistent across Flock's deployments, or specific to one firmware version on one camera?

But look at the pattern across both issues together. A detection surface goes dark. The community finds a replacement. The replacement's blind spots (2.4GHz-only scanning, OUI-based matching, filtering out locally administered MACs) line up closely with exactly the properties a new SSID format, a 5GHz radio, and a locally administered MAC address would exploit. **That could be coincidence produced by an unrelated firmware upgrade cycle, or it could be a vendor tightening its own wireless footprint in ways that happen to break third-party detection as a side effect, intentional or not.**

*The most useful stance is not to argue which one it is. It is to build detection that does not depend on any single assumption holding forever, because on this project's own two-year track record, none of them have.*

### Visual Confirmation: Powered On, Broadcasting Nothing

**[A third Valleytech Custom Solutions short](https://www.youtube.com/shorts/sjI8FB0cLk0) closes the loop on the "maybe the camera was removed" explanation.**

{{< youtube id="sjI8FB0cLk0" >}}

The creator returned to the same camera from the first video, at night, and visually confirmed its **IR LEDs were still firing**, meaning the unit was powered on and actively illuminating for night capture. At the same time, **every custom firmware they tested logged zero legitimate hits** against that camera. One alert did fire, but it was a confirmed false positive rather than a real detection. Nothing from the camera was reaching the wireless side at all.

**This separates the two competing explanations cleanly.** A camera that has been uprooted or relocated cannot explain a unit that is visibly powered on and illuminating at night. A camera that is live, illuminating, and still silent on every WiFi detection method is evidence the wireless signature itself has gone dark, not that the hardware disappeared.

The creator also reported, after talking with other developers working on the same problem, that this was not an isolated result. **Multiple people observed the same pattern at roughly the same time**, which points toward a coordinated, nationwide change on Flock's side rather than a local fluke at one camera. *That claim is anecdotal, based on informal conversation rather than a published dataset, but it lines up with the same December 2025 and spring 2026 windows described in Issue #20, and it is the kind of report that belongs in a new GitHub issue rather than staying as a comment thread.*

______

## What This Means for Your Detection Hardware

If your device has gone quiet, work through this checklist before assuming it is broken:

1. **Update your firmware first.** If you are running anything older than the current `main` branch, you are likely still looking for the deactivated management AP or dead BLE beacons. Pull the latest firmware and reflash.
2. **Confirm the camera is still there.** Some of the "zero detections" reports turned out to be genuinely uprooted or relocated hardware, not a detection failure. Cross-reference against **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** or **[DeFlock](https://deflock.org/)** before troubleshooting your device.
3. **Slow down at intersections.** The 250ms channel-hop dwell means a fast pass carries you past a camera's detection window before your radio lands on the right channel. A 30-60 second stop catches far more cameras than a fast drive-by with a bigger antenna.
4. **Report what you see.** A confirmed zero-detection result next to a visually verified camera is exactly the kind of data point that turned into Issues #20 and #43. Open a new issue rather than assuming someone else already reported it.
5. **Know the current limits.** WiFi-only, 2.4GHz-only firmware will not see a camera that has moved to 5GHz or gone quiet on the bands it scans. That is a real gap right now, not a bug in your specific build.

**None of this makes the hardware pointless.** The OUI list and wildcard-probe fingerprint still catch the overwhelming majority of deployed cameras today. It means treating any detector, DIY or purchased, as a snapshot of the current arms race rather than a permanent solution.

{{< stscollective-ad "flockyou" >}}

______

## A Parallel Approach: Detecting the Infrared Flash Instead of the WiFi Signal

Wireless detection is not the only front in this arms race. **[A separate follow-up video](https://www.youtube.com/shorts/mzpr6bslsYA) from the same creator, Valleytech Custom Solutions, describes an entirely different approach**: instead of listening for a radio signature, watch for the camera's infrared illuminator.

{{< youtube id="mzpr6bslsYA" >}}

Most ALPR cameras, Flock's included, use **infrared illumination to capture readable plates at night**, the same reason ordinary security cameras work in the dark. That IR light is invisible to the human eye but visible to an image sensor that has not had its infrared-cut filter installed. *That single hardware detail, a missing IR-cut filter, is what turns an ordinary camera module into a Flock detector.*

### What the Prototype Looks Like

The approach documented in the video went through several iterations before landing on a workable combination:

- **First attempt**: dedicated IR photodiode receivers. Technically workable, but the parts were too expensive to be a practical DIY option.
- **Second attempt**: a **Jetson Nano paired with a Raspberry Pi camera module**. This proved the concept worked, but the hardware cost and power draw made it impractical for a handheld or vehicle-mounted build.
- **Current build**: an **ESP32-based camera module without an IR-cut lens**. The creator tested an **ESP32-CAM** and an **M5Stack S3 Cam** before settling on the **Seeed Studio XIAO ESP32S3 Sense**, paired with a **Seeed XIAO GNSS module built on the Quectel L76K chip** for GPS-tagging detections, the same GPS-wardriving pattern the WiFi-based `flock-you` dashboard already uses.

| Requirement | Why it matters |
|---|---|
| **No IR-cut filter on the camera module** | The filter that makes ordinary photos look color-correct also blocks the exact light this method needs to see |
| **A camera rather than a photodiode** | Photodiode receivers capable of isolating the signal were too expensive to be practical for a DIY build |
| **GPS logging** | Matches detections to a location the same way the WiFi firmware's Flask dashboard does |

### The Camera's Blink Pattern

The premise depends on the illuminator flashing in a detectable, repeating pattern rather than staying continuously lit. The creator reported a **self-measured timing of roughly 20 milliseconds on and 80 milliseconds off, a 100-millisecond period, which works out to a 20% duty cycle at 10Hz**, and was explicit that this figure is unverified and could be wrong. *Treat that specific number as a starting point for your own measurement, not a confirmed spec, since Flock has never published it and the creator did not claim certainty either.*

### Where the Project Stands

**This is an early, DIY-only prototype, not a finished product.** The creator described the software as "vibe coded" and still in progress, with a buzzer for audible alerts planned but not yet added, and no packaged board equivalent to the OUI-SPY hardware. The current version still requires a **human to visually confirm** that a flagged detection is an actual camera rather than another IR-emitting light source, so it works as a screening tool rather than a fully automated one.

*This is a genuinely different detection surface than everything else in this article. It does not depend on WiFi, 2.4GHz or 5GHz, OUI matching, or MAC address behavior at all, which means none of the evasion techniques described in Issue #43 apply to it. That also means it inherits its own limitations: line of sight, daylight interference, and a duty cycle assumption that has not been independently confirmed.*

______

## What the Community Is Doing About It

The response to both issues followed the same pattern that has kept this project useful for two years: someone reports a gap, someone else contributes the fix, and the fix ships as an update rather than sitting in a backlog.

- **Issue #20** ended with a confirmed root cause and a firmware rewrite around the wildcard-probe signature, credited to the DeFlockJoplin community's field research.
- **Issue #43** remains open as of this writing, with the SSID pattern-matching suggestion still pending implementation. *If you want to help close that gap, the fix (adding `Flock Camera` as an additional match pattern) is a small, well-scoped contribution for anyone comfortable with the firmware's match logic.*
- The underlying OUI dataset is versioned and dated in the repository, with demoted and low-confidence entries documented rather than silently dropped, so anyone forking the project sees exactly what changed and why.

*This is the practical case for open-source detection tooling over a closed-source alternative. A proprietary detector cannot be patched by the person who found the gap. This one already has been, twice.*

______

## Conclusion: Detection Is a Moving Target, Not a Fixed Answer

A silent detector on a route that used to catch cameras is not proof your hardware failed. It is evidence that the wireless signature it was built to recognize has changed, again, in a pattern that has now repeated twice inside a single year. The **management AP, BLE beaconing, and now potentially the 2.4GHz-only, OUI-only assumptions baked into the current firmware** have each had a limited shelf life.

**The fix has never been to give up on wireless detection.** It has been to keep the detection method's assumptions visible, documented, and open to correction the next time a report like Issue #20 or Issue #43 comes in. That is the argument for open-source firmware over any closed alternative: the fix ships as soon as the community finds the gap, not on the vendor's schedule.

### Key Takeaways

- **Two documented detection surfaces have already gone dark**: the management WiFi AP (deactivated around December 2025) and BLE beaconing (unreliable by spring 2026).
- **The current method, wildcard probe requests plus OUI and IE fingerprint matching, has a field-verified 11-of-12 detection rate**, but it is WiFi-only and 2.4GHz-only.
- **A pending report describes a new SSID format, a confirmed 5GHz hotspot, and locally-administered MAC addresses** that the current OUI-based, 2.4GHz-only method cannot see.
- **A separate, non-wireless approach is emerging**: an ESP32 camera module with its IR-cut filter removed spots a Flock camera's infrared illuminator, a detection surface that ignores WiFi entirely and is immune to every evasion technique above.
- **Visual confirmation backs the wireless silence up**: a camera visibly powered on and illuminating at night still logged zero legitimate WiFi hits, which rules out "the camera was removed" as the explanation for that specific unit.
- **A zero-detection result on a known camera does not automatically mean your hardware is broken.** Update your firmware first, then confirm the camera is physically still there.
- **This is an open-source project that keeps shipping fixes as the community finds gaps.** Read the GitHub issues, not only the README, to know the current state of detection.

### Next Steps

1. **Update your firmware** to the current `main` branch before troubleshooting anything else: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Read the full hardware guide** if you have not already: **[Flock-You Detection Project: Counter-Surveillance Hardware Guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Cross-reference suspected dead zones** against **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** before assuming your device missed something
4. **Understand what you are up against**: **[Flock Safety Camera Surveillance: Prevalence, Privacy Concerns, and Protection Strategies](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Pair WiFi detection with cellular detection** using **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)** for a fuller counter-surveillance picture, since none of this article's methods detect cell-site simulators

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Shop Ready-to-Go FlockYou Devices, Save 20%
{{< /centerbutton >}}

______

## Related Articles

| Article | What it covers |
|---------|---------------|
| **[Flock-You Detection Project: Counter-Surveillance Hardware Guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Full technical guide to the three hardware platforms, firmware setup, and the detection methodology this article builds on |
| **[Flock Finder: Map Every Suspected Flock Camera Near You](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Cross-reference a suspected dead zone against 40,000+ mapped camera locations before troubleshooting your device |
| **[Flock Cameras: Public Safety Tool or Warrantless Surveillance Machine?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Independent analysis of what Flock's database actually enables and why the warrant question matters more than the detection question |
| **[Flock Safety Camera Surveillance: Prevalence, Privacy Concerns, and Protection Strategies](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | The full picture on deployment scale, documented abuse cases, and community organizing resources |
| **[Flock Safety Camera Vulnerabilities: 50+ Flaws Found](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | The hardware and software security research side of Flock's cameras, separate from the wireless detection question this article covers |
| **[How to Flash Rayhunter Devices: Complete Guide](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detect IMSI catchers and stingrays, the cellular equivalent of the WiFi detection gap this article describes |

______

## References

1. [Flock-You GitHub Repository - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [GitHub Issue #20 - Flock cameras not detected, but other devices detected](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [GitHub Issue #43 - 5GHz signal? New OUI / MAC address filtering](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [NitekryDPaul OUI Research Dataset](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - Community ALPR Research](https://deflockjoplin.today)
7. [Pintor, L. & Atzori, L. (2022) - Analysis of Wi-Fi Probe Requests Towards Information Element Fingerprinting, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [The Hunt for the Hidden Probe - Hidden SSID Wildcard Probe Behavior](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
9. [DeFlock - Crowdsourced ALPR Camera Map](https://deflock.org/)
10. [Colonel Panic Tech - OUI-SPY and Detection Hardware](https://colonelpanic.tech)
11. [STS Collective - FlockYou Devices](https://stscollective.com/discount/SIMEONONSECURITY)
12. [Something Strange Is Happening With Flock Cameras - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
13. [Infrared Wardriving Flock Cameras - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
14. [Flock Cameras Still On But No Broadcast - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
15. [Automatic Number-Plate Recognition - Wikipedia (infrared illumination in ANPR/ALPR systems)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
16. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
17. [L76K GNSS Module for Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)
