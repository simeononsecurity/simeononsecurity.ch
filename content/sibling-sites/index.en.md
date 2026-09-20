---
title: "Sibling Sites - SimeonOnSecurity's Standalone Cybersecurity Tools"
date: 2026-09-20
lastmod: 2026-09-20
toc: true
draft: false
description: "Every SimeonOnSecurity sibling site in one place. Seven standalone tools on their own subdomains, covering WiFi data maps, ALPR surveillance mapping, ESP32 counter-surveillance firmware, and resume optimization."
genre: ["Cybersecurity", "Privacy", "Open Source", "Network Tools", "Surveillance", "Self-Hosted"]
tags: ["sibling sites", "simeononsecurity tools", "subdomains", "helium map", "openroaming map", "flock finder", "eye spy", "ats resume match", "offload search", "carrier offload", "wigle", "alpr", "surveillance mapping", "counter-surveillance", "passpoint", "hotspot 2.0", "resume optimizer", "self-hosted tools", "open source tools"]
cover: "/img/cover/sibling-sites-simeononsecurity-cybersecurity-tools.webp"
coverAlt: "An illustration showing interconnected nodes representing cybersecurity and privacy tools in vibrant colors against a dark background."
coverCaption: ""
---

**SimeonOnSecurity builds tools large enough to deserve their own web address.** Seven standalone projects run on dedicated subdomains today. Each one does a single job, pulls its own data, and ships on its own schedule.

This page collects all seven in one place so you know what exists, what each tool does, and where to find it. One more project, **track-carrier-openroaming-support**, publishes its results through a repository instead.

*Sibling sites are written in English only. They are not translated into the other site languages.*

{{< figure src="simeononsecurity-sibling-sites-subdomain-family.webp" alt="Illustration of the main SimeonOnSecurity site with its tool subdomains branching from it" caption="Standalone tools, each on its own subdomain" >}}

## Key Takeaways

- **Seven sibling sites** run on dedicated **simeononsecurity.com** subdomains.
- **Three are passive data maps** built from the WiGLE crowdsourced WiFi database.
- **Two are ESP32 firmware projects** for detecting Flock Safety cameras in the field.
- **Offload Search** rates one address at a time for carrier offload suitability.
- **ATS Resume Match** scores and rewrites resumes for applicant tracking systems.
- **OpenRoaming carrier support** is tracked in a repository, without a subdomain of its own.
- Every sibling site is **open source** and **self-hostable** unless noted.

## Sibling Sites at a Glance

| Site | What it does |
|------|--------------|
| **[Helium Map](https://heliummap.simeononsecurity.com/)** | Maps Helium Mobile and Helium Free WiFi hotspots recorded by WiGLE |
| **[Offload Search](https://offloadsearch.simeononsecurity.com/)** | Rates one address for carrier offload and nearby foot traffic |
| **[OpenRoaming Map](https://openroamingmap.simeononsecurity.com/)** | Maps Hotspot 2.0, Passpoint, and OpenRoaming access points |
| **[Flock Finder](https://flockfinder.simeononsecurity.com/)** | Maps suspected Flock Safety ALPR cameras by WiFi OUI fingerprint |
| **[Eye Spy](https://eyespy.simeononsecurity.com/)** | Flashes surveillance detection firmware onto an M5Stack Atom Lite |
| **[Flock-You ESP32](https://flockyouesp32.simeononsecurity.com/)** | Flashes Flock Safety camera detection firmware onto any ESP32 board |
| **[ATS Resume Match](https://atsresumeimprover.simeononsecurity.com/)** | Scores and rewrites a resume for applicant tracking systems |

## What Counts as a Sibling Site

A sibling site is a tool with a full application behind it. It has its own dataset, its own build pipeline, and its own subdomain.

The single-page utilities on [Tools](/tools/) (password checker, hash calculator, Base64 encoder, EXIF viewer, and the rest) stay on the main domain because they run entirely in the browser and need no backend.

Sibling sites fall into three groups:

**Passive data maps** rebuilt from WiGLE records
- **Helium Map**
- **OpenRoaming Map**
- **Flock Finder**

**Lookup and scoring tools** driven by public APIs
- **Offload Search**
- **ATS Resume Match**

**Device firmware** with a browser flasher
- **Eye Spy**
- **Flock-You ESP32**

The split matters for maintenance. Map projects depend on third-party data and break when an upstream API changes. Lookup tools depend on browser support. Firmware depends on hardware shipped to a reader.

## Helium Map

**Helium Map** plots Helium Mobile and Helium Free WiFi network locations pulled from two sources: the WiGLE.net crowdsourced WiFi dataset and the Helium Blockchain Exporter API. The final published scan maps **8,335 access points**, and the repository also carries Helium-provided device status and subscriber growth tables.

Markers carry the SSID, the RCOI, and the device category. Filter checkboxes hide categories you do not care about, and a search box matches SSIDs or RCOIs with an optional regular expression.

{{< centerbutton href="https://heliummap.simeononsecurity.com/" >}}
Open Helium Map
{{< /centerbutton >}}

*GitHub archived the upstream repository in April 2025, so treat this map as a dated snapshot rather than a live feed.*

## Offload Search

**Offload Search** answers one question: is this address a good spot for carrier offload?

Type an address and the tool geocodes it, then returns the FCC Broadband Map for the area plus Google Maps, Foursquare, and Yelp links for checking nearby foot traffic. Nominatim reverse geocoding classifies the location as **Business**, **Residential**, or **Other** and estimates the odds a carrier accepts service there.

An optional estimator turns a foot-traffic number into a rough offload figure using network averages. *Dwell time above the 5 to 30 minute average pushes the real number lower than the estimate.*

The tool runs in the browser, stores nothing, and needs no account. **Run it before committing a venue to a hotspot or offload deployment.**

{{< centerbutton href="https://offloadsearch.simeononsecurity.com/" >}}
Check an Address
{{< /centerbutton >}}

## OpenRoaming Map

**OpenRoaming Map** tracks **Hotspot 2.0**, **Passpoint**, and **OpenRoaming** access points recorded in the WiGLE dataset.

The published map groups markers by operator, so OpenRoaming settled and unsettled RCOIs, Google Orion devices, IronWiFi devices, **eduroam**, **cityroam**, **XNET**, **MetaBlox**, **Wayru**, Helium deployments, and plain Hotspot 2.0 access points appear side by side. A daily GitHub Actions job fetches new records, rebuilds the map, and refreshes the README statistics, which list every unique RCOI with a count. The dataset resets each year and the previous year is archived. A companion Dune dashboard tracks the same network family.

*A yearly reset keeps the marker count readable instead of growing without limit.*

{{< centerbutton href="https://openroamingmap.simeononsecurity.com/" >}}
Open the OpenRoaming Map
{{< /centerbutton >}}

## Flock Finder

**Flock Finder** maps suspected **Flock Safety ALPR cameras**. It queries WiGLE for networks matching the 31 known Flock Safety OUI (MAC address) prefixes gathered from public research, then plots each hit on a clustered Leaflet map. As of September 2026 the published map carries more than 146,000 suspected camera records across 138 countries.

Every record shows the BSSID, SSID, OUI, channel, first-seen and last-seen dates, and a confidence label. A daily workflow re-scans at 06:00 UTC and keeps two years of data. The project also documents the SSID naming patterns seen in the wild, covering the bare **Flock** name, the **Flock-XXXXXX** provisioning format, and the **Flock Camera net** variant which no OUI lookup spots.

> **Warning: an OUI match is a heuristic, not proof of a camera.** MAC prefixes get shared, reassigned, or spoofed, and WiGLE records arrive sporadically because Flock cameras wake only to upload. Treat the map as a lead, then confirm on site. The project maintains a full data policy, a data dictionary, and a corrections process.

Detection hardware pairs with the map. **[Flock-You ESP32](#flock-you-esp32)** below builds the same WiFi detection method onto a $5 board, and **[FlockYou detectors from STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** package it as a finished device with LED and audio alerts. Use code **FLOCKFINDER** for 20% off FlockYou hardware, or **SIMEONONSECURITY** for up to 20% off the full order.

{{< centerbutton href="https://flockfinder.simeononsecurity.com/" >}}
Open Flock Finder
{{< /centerbutton >}}

## Eye Spy

**Eye Spy** is passive surveillance detection firmware for the **M5Stack Atom Lite** (ESP32-PICO-D4). It listens on BLE and WiFi for body cameras, ALPR systems, AirTags, personal trackers, drones, and hidden cameras, then scores what it hears.

A single RGB LED reports the threat level: **blue** for startup, **green** for clear, **yellow** for caution, and **red flashing** for a likely recording or tracking device. The score drops one point every 60 seconds so stale hits fade.

Scanning stays passive. The device sends no probe requests, so the equipment it hunts gets no hint the device exists. The sibling site hosts a web flasher plus a live dashboard, firmware installs over USB, and native unit tests cover the OUI and keyword tables without hardware on the bench. The Atom Lite is the primary target, and experimental builds exist for the LILYGO T-Dongle C5.

{{< centerbutton href="https://eyespy.simeononsecurity.com/" >}}
Flash Eye Spy
{{< /centerbutton >}}

## Flock-You ESP32

**Flock-You ESP32** is a WiFi promiscuous-mode detector for Flock Safety surveillance cameras, ported to standard ESP32 hardware from **colonelpanichacks/flock-you**. A build starts at **$5** for an ESP32 DevKit and a USB cable, or $10 to $12 with a breadboard, a passive buzzer, and a 3D printed case.

Every hit is scored from 0 to 100 across five techniques: WiFi promiscuous sniffing with three OUI confidence tiers, the wildcard probe signature, SSID pattern matching which catches **Flock Camera net** units on locally administered MACs, BLE cross-correlation, and multi-address matching on addr1, addr2, and addr3. Scores below 30 log quietly, scores from 30 to 59 read **PROBABLE**, and scores of 60 or higher trigger an alert.

A buzzer plays the **Super Mario Bros. World 1-2** theme at startup, then two ascending beeps on each new detection. The bundled Flask dashboard tags hits with GPS and exports JSON, CSV, or KML for Google Earth. Boards include the ESP32 DevKit, M5Atom Lite, M5Atom Echo, M5Atom Voice, Atom VoiceS3R, and the LILYGO T-Dongle C5. 38 host-side Unity tests cover the detection tables without hardware on the bench.

**Eye Spy and Flock-You ESP32 overlap by design.** Eye Spy targets the M5Stack Atom Lite, watches a wider sensor list, and reports through one RGB score LED. Flock-You ESP32 runs on any ESP32 with 4MB of flash and carries the WiFi research behind the original Flock-You firmware.

{{< centerbutton href="https://flockyouesp32.simeononsecurity.com/" >}}
Flash Flock-You ESP32
{{< /centerbutton >}}

## ATS Resume Match

**ATS Resume Match** is a free, self-hostable resume optimizer. Parsing and scoring run in the browser, so the resume file stays on your machine unless you switch on an AI feature.

It detects the resume type from seven profiles, reorders sections for the profile, scores the document across five dimensions, and shows the plain text an applicant tracking system reads. Keyword gap analysis compares the resume against a job post, the optimizer rewrites weak sections, and the cover letter generator applies a house style guide which strips em dashes, banned buzzwords, and passive voice.

AI features work with OpenAI, Anthropic Claude, or a local Ollama model. Bring a key or run it offline. Export goes to PDF, DOCX, TXT, or Markdown, and the project ships a Dockerfile plus deploy targets for Vercel, Cloudflare Pages, and Netlify.

{{< centerbutton href="https://atsresumeimprover.simeononsecurity.com/" >}}
Optimize Your Resume
{{< /centerbutton >}}

{{< figure src="passive-wifi-data-pipeline-to-map.webp" alt="Diagram showing WiGLE WiFi records flowing through a daily build job into an interactive map" caption="Records in, a daily job, a Leaflet map out" >}}

## Related Research Projects

Not every project needs its own address. When the output is a data table rather than an interactive map, the repository README does the job.

### OpenRoaming Carrier Support

**track-carrier-openroaming-support** checks whether each mobile network operator supports OpenRoaming by running **NAPTR** and **SRV** lookups against every PLMNID (MCC and MNC pair) listed on mcc-mnc.com.

The published result is blunt. **0.20%** of listed carriers answer the lookup. The README names each carrier which does, alongside its identity provider host and port, and adds a lookup table mapping public domains to their hosts, built from public certificates, public documentation, and authentication attempts. A GitHub Actions job re-runs the check each week and commits any change.

The Wireless Broadband Alliance publishes a manual checker for these records at [wballiance.com/OR/Tools/realm-check.html](https://wballiance.com/OR/Tools/realm-check.html).

{{< centerbutton href="https://github.com/simeononsecurity/track-carrier-openroaming-support" >}}
Read the Carrier Report
{{< /centerbutton >}}


## Why They Live on Subdomains

Isolation is the main reason. A sibling site fails alone. When a map workflow breaks, the main Hugo site keeps building and deploying.

The other reasons hold up in practice:

- **Different stacks.** The main site runs Hugo. The sibling sites run Python, Folium, Leaflet, React, and PlatformIO.
- **Different cadence.** Maps rebuild every 24 hours. The main site deploys on content commits.
- **Different hosting rules.** A subdomain gets its own cache rules, its own Cloudflare settings, and its own CORS policy.
- **Different failure modes.** A 403 from an upstream API hits one tool, not the whole domain.

The cost is duplication. Each project carries its own CI workflow, its own secrets, and its own data retention policy. Each one also needs a reader who remembers it exists, which is the job this page does.

## Next Steps

- Browse the [on-site tools](/tools/) for browser-only utilities.
- Read the [articles](/articles/) for the research behind the maps.
- Practice with the [free certification practice tests](/practice-tests/).
- Follow the [guides](/guides/) for build-along instructions.

