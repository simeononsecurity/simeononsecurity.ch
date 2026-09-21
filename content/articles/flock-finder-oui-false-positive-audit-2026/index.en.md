---
title: "We Mapped 146,526 ‘Flock Cameras.’ 50,278 Were ClickShare Systems"
date: 2026-09-21
lastmod: 2026-09-21
toc: true
draft: false
description: "Our audit of Flock Finder found 50,278 Barco ClickShare devices and thousands of other false positives inside a 146,526-record camera map. Here is what failed, how we proved it, and what we changed."
genre: ["Security Research", "Privacy Technology", "Open Source Projects", "Data Journalism", "Counter Surveillance"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "OUI Fingerprinting", "WiGLE", "False Positives", "Data Quality", "Barco ClickShare", "MAC Address", "IEEE OUI", "Information Element Fingerprinting", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Open Source Accountability", "Surveillance Mapping", "WiFi", "Probe Request", "MAC Randomization"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "A dark city map crowded with red location pins that resolve into office WiFi devices while a few green pins remain as stronger detections"
coverCaption: "An audit of 146,526 Flock Finder records exposed how a useful field observation became an overconfident map claim."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**We put 146,526 points on a surveillance-camera map. At least 50,278 of them were Barco ClickShare presentation systems. Conference-room hardware accounted for more than one-third of what our headline called “Cameras Mapped.”**

This was our project, our data pipeline, and our mistake. Flock Finder queried WiGLE every day for MAC-address prefixes observed on Flock Safety cameras, published the results at full coordinate precision, and rendered them as equivalent pins. The records carried the word `suspected` in their metadata and the documentation mentioned false positives. The map and headline still communicated certainty.

When we finally ran a frequency histogram over the SSID column, the dataset explained the failure in minutes. ClickShare was only the largest category. Another 6,099 records named themselves `SMARTGATE_*`; 3,801 began with the generic WiFi Direct prefix `DIRECT-`; 314 were the exact name `AndroidAP`; 138 said `Audi HUD`; 133 said `MAX-PRINTER`; and 30 contained another detector's verdict string. In total, **60,793 rows, or 41.5%, matched the original audit's known-other naming rules.**

We have now changed Flock Finder to publish evidence classes per record, exclude known-other hardware from the default map and headline, expose filters, flag records outside the primary market, and separate high-confidence prefixes from contract-manufacturer prefixes. This article documents the error, the evidence, and the limits that remain.

______

## How Community ALPR Detection Works

Community-built Flock detectors generally combine three kinds of wireless evidence:

1. **WiFi MAC/OUI prefixes.** The first bytes of a globally administered MAC address can identify the organization that received the address block.
2. **WiFi behavior.** An SSID, wildcard probe request, receiver address, channel pattern, or sequence of 802.11 information elements can narrow the device class.
3. **Bluetooth evidence.** Manufacturer IDs and service UUIDs can identify radios exposed by a particular product or firmware generation.

OUI matching became common because it is cheap and passive. An inexpensive ESP32 can inspect nearby 802.11 frames without connecting to a network. A historical database such as [WiGLE](https://wigle.net/) also lets a project search past observations without deploying its own scanners.

The method moved through a community lineage: [DeFlock](https://deflock.org/) mapping and local organizing; [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you); forks and companion projects such as our own [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32); and finally [Flock Finder](https://github.com/simeononsecurity/flock-finder), which applied the prefix list to WiGLE data at global scale.

The original fieldwork deserves clear credit. [@NitekryDPaul](https://github.com/NitekryDPaul) observed 30 prefixes on real Flock equipment through promiscuous-mode research. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) contributed another during field testing. Those observations were legitimate. Our downstream error was treating **“observed on a Flock camera” as if it meant “exclusive to Flock cameras.”**

______

## The Structural Flaw: An OUI Is a Supply-Chain Fact

The IEEE describes an OUI as a 24-bit identifier assigned to a vendor, manufacturer, or other organization. Combined with another 24 bits chosen by the assignee, it forms a MAC address. The [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/) publishes the registry.

That tells us who received an address block. It does not necessarily tell us which brand is printed on a finished product. Contract manufacturers build radio modules for many customers, and a single chip vendor can appear in cameras, projectors, printers, vehicles, and hobby boards.

The registry assignments behind our list made the risk visible:

| Registrant | Prefixes in the audited list |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC`, and others |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

The Espressif entries should have stopped us. Two prefixes in a supposed camera list belonged to the maker of one of the world's most common embedded WiFi platforms, including the silicon used by many community detectors.

`B4:1E:52` is different because it is registered directly to Flock Safety. It had been added to the 38-prefix list at the audited commit, but **had not yet been queried**: `scan_stats.json` reported 31 queried prefixes. The same was true of six newly added battery-pack prefixes. The snapshot therefore provides no evidence about how common or rare Flock's own prefix is, and we will not turn “not queried” into “zero results.”

The current repository contains 39 prefixes after adding `E0:0A:F6` for parity with the detector firmware. Its retained scan summary still reports data for 31 prefixes, so the newer entries remain pending a completed recalculation rather than proven zero-result prefixes.

______

## The Dataset Audited Itself

Every historical audit number below was regenerated from `data/flock_cameras.csv` at Flock Finder commit [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829) with Python's standard-library `csv` and `collections.Counter`. No new drive test was required. The names, geography, and prefix composition already contradicted the headline. Figures describing the corrected implementation come from the current repository's retained `scan_stats.json` summary.

### Geography Was an Early Warning

Of 146,526 rows, 75,818 were in the United States, 70,674 were outside it, and 34 had no country value. Germany alone contributed 13,491 records, followed by Canada with 6,251, France with 5,839, Great Britain with 4,836, the Netherlands with 4,636, and Switzerland with 4,515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Stacked bar showing 75,818 United States records, 70,674 records outside the United States, and 34 records with no country value" caption="The country histogram sums to 146,492 because 34 rows have a null country." >}}

Geography is a screening signal, not proof. Flock describes its network as operating “nationwide” and says it connects customers across [49 U.S. states](https://www.flocksafety.com/flock-ecosystem). International expansion can also change the market boundary. We therefore flag out-of-market rows for review instead of deleting them or declaring every non-US record false.

The conservative conclusion is enough: almost half the records occurred outside the project's primary US market, so a worldwide OUI hit could not be treated as equally plausible without another signal.

### More Than 60,000 Devices Named Themselves

| SSID family in the original audit | Records | Share | What the name indicates |
|---|---:|---:|---|
| Contains `ClickShare` | 50,278 | 34.3% | Barco wireless presentation hardware |
| `SMARTGATE_*` | 6,099 | 4.2% | Gateway or OBD-style device family |
| `DIRECT-*` | 3,801 | 2.6% | WiFi Direct devices such as printers, TVs, and adapters |
| Exact name `AndroidAP` | 314 | 0.2% | Android hotspots |
| Exact name `Audi HUD` | 138 | 0.1% | Audi infotainment or head-up-display WiFi |
| Exact name `MAX-PRINTER` | 133 | 0.1% | Office printers |
| `Flock ALPR [...]` | 30 | <0.1% | Another detector's verdict stored as an SSID |
| **Combined original audit** | **60,793** | **41.5%** | Identifiable as other hardware or detector output |

Barco's own support documentation says a ClickShare Base Unit's default network name is [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). That gives us first-party confirmation of the product family without guessing from geography or vendor registration.

The production classifier has since replaced those exact-name checks with case-insensitive regular expressions and includes ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER, and detector-output labels. On the same 146,526 rows, it catches 629 AndroidAP variants, 139 Audi HUD variants, and 134 MAX-PRINTER variants. The current repository therefore reports **61,110 `identified_other` records**, slightly more than the 60,793 found in the original audit.

### The Confirming Signal Was Only 2.4%

Only **3,502 rows** carried a genuine Flock-pattern SSID. Another 24,964 had no SSID at all. The remaining records either named other hardware or rested on an OUI plus an unclassified name.

The 3,502 confirmed rows contained 161 genuine SSID variants: 3,342 instances of the bare name `Flock`, 157 one-off `Flock-XXXXXX` or `FLOCK-XXXXXX` provisioning names, and three other names containing `flock`. A previous README count of 166 variants included five distinct `Flock ALPR [...]` detector annotation strings. Those five are evidence of the detector, not the camera.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="A 100 percent stacked bar dividing 146,526 records into 3,502 SSID-confirmed, 57,267 named unclassified, 24,964 hidden OUI-only, 60,763 identified other, and 30 detector feedback records" caption="The old headline collapsed five materially different evidence classes into one count." >}}

### Prefix Quality Varied Dramatically

The false-positive rate was not uniform. Some prefixes retained a useful Flock signal; others were dominated by named office or consumer devices.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Horizontal stacked bars for 31 OUI prefixes showing Flock SSIDs in green, known-other SSIDs in red, hidden SSIDs in light gray, and unclassified records in dark gray" caption="The largest prefixes often contained the most known-other devices. Counts come from the 146,526-row audit snapshot." >}}

Consider two prefixes that the old map labeled identically:

- `70:C9:4E` had 495 rows: 133 Flock-pattern names and 29 known-other names.
- `74:4C:A1` had 11,872 rows: 211 Flock-pattern names and 8,385 known-other names.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Comparison of prefix 70 C9 4E with 26.9 percent Flock SSIDs and 5.9 percent known other against prefix 74 4C A1 with 1.8 percent Flock SSIDs and 70.6 percent known other" caption="One flat label concealed opposite signal-to-noise ratios." >}}

The same pattern appears in the biggest rows: `F4:6A:DD` had 8,422 known-other names against 327 Flock names; `D0:39:57` had 8,270 against 473; and `E0:4F:43` included 6,238 known-other names against 66 Flock names. Prefix volume was not evidence quality.

______

## The Feedback Loop Hidden in 30 Rows

Thirty records in Texas had SSIDs that were plainly another detector's output:

| Detector label stored as SSID | Confidence written by that tool | Records |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | low | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | medium | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | low | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | low | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | low | 1 |

Twenty-six of the 30 were labeled low confidence by the tool that created them. A WiGLE upload then stored the tool's verdict in the SSID field. Our pipeline found the word `Flock` and could have treated that label as independent confirmation.

Thirty rows are statistically small. The mechanism is consequential: tools that share a crowdsourced database can ingest one another's output and launder a low-confidence guess into apparent corroboration. The correction deny-lists the entire `Flock ALPR [` pattern before checking for a confirming `flock` substring.

______

## Where We Got It Wrong

The README headline reported **“Cameras Mapped | 146,526.”** The map published full-precision coordinates and drew every result as the same kind of pin. It updated on a GitHub Actions schedule, giving a weak heuristic the appearance of a maintained inventory.

We did include caveats. Every feature carried `match_confidence: "suspected"`. The README discussed ClickShare as a possible co-occupant, and the project maintained a separate candidate track for SSID discoveries. Those caveats did not govern the number, marker, or default view that readers actually saw.

We hedged in prose and quantified in the headline. The map made the claim.

The most avoidable part is that our [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) firmware already separated high-confidence identifiers from contract-manufacturer identifiers and scored weak evidence below the alert threshold. The concept existed in the same organization, but the mapping pipeline did not inherit it.

We found the scale of the error by running a histogram on our own SSID column. It took minutes. We had been committing 146,526 rows of evidence against our presentation every day.

______

## What We Changed

The correction is implemented in Flock Finder's data model and interface:

- **Per-record evidence:** `ssid_confirmed`, `oui_high`, `oui_mfr`, or `identified_other`.
- **OUI tiers:** prefixes are separated into field-observed high confidence and shared contract-manufacturer tiers.
- **Known-other exclusion:** ClickShare, SmartGate, WiFi Direct, Android hotspot, Audi HUD, MAX-PRINTER, and detector-output SSIDs are excluded from the map and headline by default.
- **Visible uncertainty:** marker colors, popups, counts, and filters expose the evidence class.
- **Market flagging:** records outside the primary US market carry `out_of_market: true` and remain available for review.
- **A decomposed headline:** 3,502 SSID-confirmed, 73,691 high-tier OUI suspected, 8,223 contract-manufacturer OUI suspected, and 61,110 identified as other.

The corrected actionable headline is **85,416**, and that number still includes 81,914 unconfirmed OUI matches. It is a defensible accounting of what passed the current rules, not a verified camera inventory.

`identified_other` is also an operational classifier, not an oracle. ClickShare has strong first-party documentation behind its default SSID, while a broad pattern such as `DIRECT-` describes a WiFi Direct naming convention used by many product classes. Publishing the matching rule and `blocked_reason` field lets researchers audit those exclusions and revise them when evidence improves.

### The Long-Term Answer Is Firmware Fingerprinting

OUI tiering limits damage but cannot make a shared manufacturer prefix product-specific. The stronger path is the ordered structure of 802.11 probe-request information elements. Upstream work documents this TLV signature:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

That sequence describes behavior of a particular firmware stack rather than ownership of a MAC block. Probe-request fingerprinting is an established device-identification technique; [published research on 802.11 MAC-layer fingerprinting](https://doi.org/10.1155/2017/6235484) shows that probe-request information elements can remain identifying when MAC addresses rotate. It also addresses the specific failure mode reported in [flock-you issue #43](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` appearing on sequential locally administered MAC addresses across 2.4 and 5 GHz.

The signature still needs independent field validation across hardware and firmware versions, and malformed captures require defensive parsing. It is nevertheless the right direction. MAC randomization makes OUI-only matching a dead end on a timer.

______

## Why This Matters Beyond One Repository

People use surveillance maps to decide where they drive, park, report, research, and organize. A false pin redirects attention. Tens of thousands of false pins can discredit accurate observations beside them.

There is also a credibility asymmetry. A vendor or critic needs one demonstrably false ClickShare pin to challenge the whole dataset. We supplied 50,278. Journalists and advocacy groups can repeat a clean headline faster than a later correction can follow it.

Open-source transparency work earns trust through inspectable methods and visible uncertainty. Publishing the raw data helped expose our error, but raw access did not excuse the interface that overstated it. The correction belongs wherever a reader encounters the claim: field, filter, marker, legend, and headline.

### A Request to Every Flock and ALPR Map

Other Flock and ALPR mapping projects should audit their datasets too. This is an invitation to compare methods, not an allegation that every map inherited our mistake.

[WiGLE](https://www.wigle.net/stats/) is the broadest publicly accessible, globally searchable WiFi observation dataset we know of. That reach is exactly what made Flock Finder attractive: one API could turn a field-researched signature list into a worldwide map. It also made the error large enough to measure. A global database will return every unrelated product sharing a radio supplier's address space, not only the product that motivated the query.

Other maps use different evidence. Some rely on photographs and volunteer field observations; others import OpenStreetMap surveillance tags, public records, vendor disclosures, or data from another community project. Their totals are not directly comparable to our WiGLE results, and our 2.4% SSID-confirmed rate should not be projected onto a field-verified dataset. The common risk is that one project's classification can flow into another project's source data, then appear to be independent corroboration.

Every public map should be able to answer a short audit:

1. **What does one marker mean?** A photographed device, a government record, an OUI match, a user report, or an import from another map?
2. **How many records have direct product evidence?** Publish counts by evidence class instead of one aggregate camera total.
3. **Which sources are independent?** Track provenance through imports so the same observation is not counted as multiple confirmations.
4. **What contradicts the classification?** Run frequency tables over SSIDs, vendors, countries, contributor labels, and every other categorical field.
5. **How are uncertainty and disputes rendered?** Put confidence and correction status in the marker, filters, exports, and headline.
6. **Can another researcher reproduce the count?** Publish the query, source snapshot, classification rules, and date.

This audit does not make the Flock problem smaller. A network of ALPR cameras can still record travel, support searches across jurisdictions, and affect people who never consented to the collection. Accurate counts make that criticism harder to dismiss. If we are going to challenge surveillance systems, our maps need to distinguish what we observed, what we inferred, and what we confirmed.

We made a well-informed mistake. The prefixes came from legitimate field research, the pipeline was reproducible, and the caveats were real. The inference still exceeded the evidence. Good intentions and good inputs do not remove the obligation to test what a system produces at scale.

______

## Reproduce the Audit

Check out commit `5551829`, then run the following from the repository root. It uses only Python's standard library and prints the total, geography, common SSIDs, and selected named-device families.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("rows", len(rows))
print("US", countries["US"])
print("non-US", sum(countries.values()) - countries["US"] - countries[""])
print("missing country", countries[""])
print("top SSIDs", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

For the exact historical input, use the CSV from that commit rather than a current generated dataset. The project stopped committing the large CSV, GeoJSON, and per-OUI files after the audit because each scan rewrote hundreds of megabytes and had grown the repository substantially. Current generated data is restored from and published to the rolling [`data-latest` release](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest); the small `scan_stats.json` summary remains in Git. A missing generated file on the current branch therefore does not mean the historical evidence was deleted or that its count became zero.

______

## The Lesson

**A heuristic labeled “suspected” in metadata but rendered as a confident pin on a map is a claim.** The label has to live in the data model and the visualization, not only in documentation.

The cheap check that would have caught this was a frequency histogram over every output field before publication. We had 146,526 rows of evidence against ourselves sitting in a CSV. We should have asked the dataset what it contained before telling readers what it meant.
