---
title: "Eye Spy: Passive Surveillance Detector for the M5Stack Atom Lite (ESP32)"
date: 2026-06-07
toc: true
draft: false
description: "A complete technical reference for Eye Spy v1.1 — an open-source passive BLE and WiFi surveillance detector running on the M5Stack Atom Lite (ESP32-PICO-D4) that scans for body cameras, ALPR systems, AirTags, drones, and hidden cameras using a confidence-score threat model and a single RGB LED."
genre: ["Privacy Tools", "Counter-Surveillance", "IoT Security", "Embedded Systems", "Security Research", "WiFi Security", "Bluetooth Security", "ESP32 Projects", "Hardware Security", "Open Source Security"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Surveillance Detection", "Counter-Surveillance", "BLE Detection", "WiFi Scanning", "AirTag Detection", "ALPR Detection", "Flock Safety", "Body Camera Detection", "Drone Detection", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Open Source", "Privacy", "Passive BLE", "Promiscuous Mode", "OUI Detection", "Tracker Detection", "Axon Body Camera", "Ray-Ban Meta", "Samsung SmartTag", "Tile Tracker", "Hidden Camera", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
---

**A Thumb-Sized Passive Sensor That Tells You When Something Is Watching**

## Introduction: The Surveillance Landscape You Can't See

The physical world is increasingly instrumented with devices that watch, record, and track — license-plate readers on street corners, body cameras on law enforcement, rental property cameras, commercial AirTag-style trackers hidden in bags or cars, and commercial surveillance cameras at every retail entrance. Most of these devices communicate wirelessly over Bluetooth LE or WiFi, and most of those communications are broadcast into the open air for anyone with the right receiver to detect.

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) is a passive surveillance detection tool that exploits exactly this fact. Running on the M5Stack Atom Lite — an ESP32-PICO-D4 development board roughly the size of a sugar cube — Eye Spy continuously monitors the BLE and WiFi spectrums for the electronic signatures of recording devices, surveillance cameras, ALPR (automatic license plate reader) systems, drones, and personal trackers. When it finds something, its RGB LED changes color.

It does not connect to anything. It does not transmit. It watches, scores, and lights up.

This article is a complete technical reference: what Eye Spy detects, how the confidence-score system works, the engineering behind each detection engine, how to build and flash it, and what its practical limitations are.

---

## LED Indicators: The Entire User Interface

Like the [ESP32 WiFi Canary](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), Eye Spy's entire output is a single SK6812 RGB NeoPixel on GPIO 27 of the M5Stack Atom Lite. The LED communicates a four-state threat level at all times:

| Color | Meaning | Score Range |
|-------|---------|-------------|
| 🔵 Blue pulse | Startup / first scan | — |
| 🟢 Green solid | Clear — nothing detected | 0–2 |
| 🟡 Yellow solid | Caution — possible recording device nearby | 3–5 |
| 🔴 Red flashing | Alert — definite surveillance / tracking device detected | 6+ |

A single high-confidence detection (Axon body camera, Flock Safety camera, ALPR OUI match, AirTag) scores enough points to immediately push the LED to red in a single detection cycle. Multiple medium-confidence detections accumulate to yellow and can combine toward red.

---

## Hardware

### Primary Target: M5Stack Atom Lite

| Component | Detail |
|-----------|--------|
| Board | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | SK6812 NeoPixel on GPIO 27 |
| Button | GPIO 39 (input only) |
| Flash | 4 MB |

The Atom Lite is a complete self-contained platform. No soldering, no breadboard, no external components. Plug it into USB and it runs.

### Generic ESP32 DevKit

A second PlatformIO build environment (`esp32dev`) targets any standard ESP32 DevKit with an onboard LED on GPIO 2. All detection logic runs identically. The DevKit build is useful for development, testing detection logic, and deployment when the Atom Lite form factor is not required.

---

## The Scoring System

Eye Spy uses a **confidence-score model** that aggregates signals from all detection engines into a single integer. The score drives LED state (green / yellow / red) and is subject to two automatic management mechanisms:

### Score Decay

The score drops **−1 point every 60 seconds** without new detections. If you move away from a detected device, the LED returns to green within a few minutes without any user intervention.

### Re-Score Cooldown

Each detection *type* has a **120-second cooldown** before it can add points again from the same source. This prevents a single persistent device from infinitely stacking the score — a Flock Safety camera that remains in range adds +5 once, then waits 120 seconds before it can contribute again.

These two mechanisms together mean:

- **Transient detections** (a car with an AirTag driving past) resolve automatically
- **Persistent surveillance** (a fixed body-cam deployment) keeps the LED at alert as long as you remain in range
- **No runaway scoring** from one device seen repeatedly

---

## Detection Engines

Eye Spy operates three distinct scanning phases in a continuous rotation:

**BLE passive (9 s) → WiFi scan (~3 s) → Promiscuous sniff (5 s) → repeat**

BLE is explicitly stopped before any WiFi operations to respect the shared ESP32 radio. It restarts cleanly at the beginning of each new cycle.

---

### Engine 1: BLE — Passive Scanning

BLE scanning is implemented using **NimBLE with no scan requests transmitted**. The device listens for BLE advertising packets without sending any response. This makes Eye Spy electronically invisible to the equipment it is scanning for — a passive scanner cannot be detected by the target.

Devices weaker than **−90 dBm** are ignored to reduce false positives in dense environments.

#### BLE Detection Table

| # | Target | Detection Method | Score |
|---|--------|-----------------|-------|
| 1 | **Axon body camera** | BLE MAC OUI `00:25:df` (Axon — body cams, tasers, LE equipment) | +5 🔴 |
| 2 | **Ray-Ban Meta smart glasses** | BLE service UUID `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE** | BLE device name containing `Flock`, `Penguin`, `Pigvision`, or `FS Ext Battery` | +5 🔴 |
| 4 | **Card skimmer (HC-03/05/06)** | BLE device name exact match — Bluetooth modules commonly found in payment-terminal skimmers | +5 🔴 |
| 5 | **Apple AirTag** | Manufacturer data `0x004C` subtype `0x12`/`0x1E`, or raw payload `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Drone (OpenDroneID BLE)** | BLE service UUID `0xFFFA`, or raw AD service-data payload with app code `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | BLE service UUID `0xFD5A` | +3 🟡 |
| 8 | **Tile tracker** | BLE service UUID `0xFEED` or `0xFEEC` | +3 🟡 |
| 9 | **MeshCore node** | BLE device name prefix `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (retail/venue tracking)** | Manufacturer data `0x004C 0x02 0x15` — deployed in stores, airports, and stadiums to track movement | +2 🟡 |
| 11 | **Unknown persistent device** | Any unclassified BLE MAC seen ≥3× over ≥5 minutes (device scout / follower detection) | +2 🟡 |

#### Notable BLE Detections in Depth

**Axon Body Camera (+5)**: Axon (formerly TASER International) manufactures the most widely deployed body camera systems for law enforcement in the United States. The OUI `00:25:df` is registered to Axon and appears in their wearable hardware. A single detection immediately reaches the Alert threshold.

**Ray-Ban Meta Smart Glasses (+5)**: The Ray-Ban Meta collaboration produces consumer smart glasses capable of video and photo recording. The BLE service UUID `0xFD5F` is the characteristic advertisement used by these devices. Notably, these are a consumer product and may appear in crowded public spaces — any detection at this score level is worth awareness regardless of the wearer's intent.

**Card Skimmer Bluetooth Modules (+5)**: HC-03, HC-05, and HC-06 are cheap commodity Bluetooth serial modules frequently discovered in payment terminal overlays and ATM skimmer hardware. Detection uses exact device name matching against known module firmware default names. This is one of the more unusual detections in the suite.

**Apple AirTag (+4)**: AirTags advertise using Apple's proprietary Nearby Interaction protocol. The detection targets the manufacturer-specific data header (`0x004C` = Apple) with the AirTag-specific subtypes (`0x12` for the standard advertisement, `0x1E` for the lost-item advertisement). Raw payload patterns provide redundant detection coverage.

**OpenDroneID BLE (+4)**: The ASTM F3411 Remote ID standard (also adopted by FAA for commercial drones in the US) defines a broadcast protocol for drones to announce their identity and position. Eye Spy looks for the GATT service UUID `0xFFFA` (the designated Remote ID service) and the application code `0x0D` in AD service-data payloads. Any compliant commercial drone operating nearby will trigger this detection.

**Unknown Persistent Device (+2)**: This is the **follower detection** engine. Any BLE MAC not classified by the specific detections above is tracked. If the same unclassified MAC appears three or more times over five or more minutes, it scores. The device persistence tracker watches up to 50 unknown MACs simultaneously, with entries purged after 30 minutes of absence. This catches custom or modified trackers that don't match any known service UUID or manufacturer pattern.

**iBeacon (+2)**: Apple's iBeacon format (`0x4C 0x00 0x02 0x15`) is used by retailers, airports, and stadiums to track device movement through physical spaces. The detection fires on the standard advertisement format regardless of UUID — targeting the deployment type, not any specific UUID. A hit here means you're likely in a location that is actively tracking Bluetooth device presence.

---

### Engine 2: WiFi Scan — Active Channel Scan

The WiFi scan engine uses the ESP32's standard AP scanning interface to enumerate nearby access points and compare their BSSIDs and SSIDs against known surveillance device fingerprints.

#### WiFi Scan Detection Table

| # | Target | Detection Method | Score |
|---|--------|-----------------|-------|
| 12 | **Flock Safety camera (OUI)** | BSSID matches 22-entry Flock Safety OUI table (`d4:bb:e6`, `3c:61:05`, FS-Ext-Battery prefixes) | +5 🔴 |
| 13 | **ALPR / LPR camera (OUI)** | BSSID matches Motorola Solutions / Vigilant Solutions OUI `00:0e:58` | +5 🔴 |
| 14 | **Flock keyword SSID** | SSID contains: `flock`, `flocksafety`, `fs ext`, `penguin`, `pigvision` | +5 🔴 |
| 15 | **ALPR keyword SSID** | SSID contains: `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola`, `automate` | +4 🔴 |
| 16 | **Surveillance camera vendor (OUI)** | BSSID matches 31-entry camera OUI table — Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix, Ubiquiti UniFi | +3 🟡 |
| 17 | **Camera keyword SSID** | SSID contains: `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect`, `genetec`, and more | +2 🟡 |

#### The Flock Safety OUI Table

The 22-entry `FLOCK_OUIS` table is the most detailed lookup in the project. It covers:

- `d4:bb:e6` — IEEE-registered Flock Safety OUI
- `3c:61:05` — IEEE-registered Flock Safety OUI
- 20 additional MAC prefixes observed on Flock FS-Ext-Battery and Flock Wi-Fi camera hardware in the field

These 22 entries represent hardware MAC ranges that have been observed on deployed Flock Safety ALPR camera systems. Detection via OUI is independent of SSID — a Flock camera with a non-keyword SSID still scores +5 if its BSSID OUI matches.

Flock Safety and Vigilant Solutions OUIs are in separate tables specifically so both can score independently in the same scan cycle. A location with both vendor types could accumulate +10 in a single WiFi scan pass.

#### Surveillance Camera Vendor OUI Table

The 31-entry surveillance camera table covers the major IP camera manufacturers whose hardware is likely to appear in retail, commercial, and residential surveillance deployments:

- **Enterprise/commercial**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix, Genetec
- **Consumer/SOHO**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex, Amcrest
- **Infrastructure**: Ubiquiti UniFi (access points and cameras share OUI space), FLIR

A match here scores +3 (Caution-range) without any keyword confirmation. Combined with a keyword SSID match, the same camera network could score +5 on the OUI alone, then +2 more from the SSID, reaching Alert in a single scan cycle.

---

### Engine 3: WiFi Promiscuous — Passive Frame Sniffing

The promiscuous engine drops the ESP32 radio into monitor mode and captures raw 802.11 management frames. This enables detection of devices that don't advertise an SSID — specifically, drones using the Remote ID protocol over WiFi Neighbor Awareness Networking (NaN).

During the promiscuous phase, the radio **channel-hops** across `{1, 6, 11, 3, 8, 13}` every 400 ms to maximize coverage of the drone NaN frame broadcast channels.

#### Promiscuous Detection Table

| # | Target | Detection Method | Score |
|---|--------|-----------------|-------|
| 18 | **Drone (OpenDroneID WiFi NaN)** | 802.11 Management frame to destination `51:6f:9a:01:00:00` — ASTM F3411 Remote ID broadcast | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: The ASTM F3411 standard defines a multicast destination address `51:6f:9a:01:00:00` for all Remote ID WiFi NaN frames. Any commercially regulated drone broadcasting its position and identity over WiFi will send frames to this destination. Eye Spy simply watches for management frames addressed to this multicast MAC — passive, reliable, and unpatchable by the drone operator short of disabling Remote ID entirely (which would itself be a regulatory violation).

This detection complements the BLE OpenDroneID engine (detection #6). A drone may advertise over BLE, WiFi, or both depending on its hardware and configuration. Eye Spy covers both.

---

## Phase Schedule and Radio Management

```
BLE passive (9 s) → WiFi scan (~3 s) → Promiscuous sniff (5 s) → repeat
```

The ESP32-PICO-D4 has a single shared 2.4 GHz radio that handles both BLE and WiFi. Eye Spy manages this carefully:

1. **BLE phase** (9 seconds): NimBLE stack active, passive scan running, no scan requests transmitted
2. **BLE shutdown**: BLE stack explicitly stopped before touching WiFi
3. **WiFi scan** (~3 seconds): Active AP scan across all channels, OUI and SSID matching
4. **Promiscuous sniff** (5 seconds): Passive 802.11 frame capture with channel hopping
5. **WiFi shutdown**: WiFi stopped, BLE restarted for the next cycle

This explicit phase management prevents radio conflicts and ensures both BLE and WiFi engines get clean access to the radio every cycle.

---

## Serial Output

All output is prefixed with `[eyespy]` for easy filtering. The serial monitor runs at **115200 baud**.

### Startup

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Normal Cycle

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Detection Events

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

The `tracked=N` field shows how many unique BLE MACs are currently in the persistence tracker — useful for understanding the density of the BLE environment.

### Score Fields

Each status line includes:
- **score** — current threat score
- **state** — `CLEAR` / `CAUTION` / `ALERT`
- **phase** — which engine is currently active (`BLE` / `WIFI` / `PROMISC`)
- **tracked** — number of unique BLE MACs in the persistence table

---

## Build and Flash

### Requirements

- **PlatformIO** (CLI or VS Code extension)
- **M5Stack Atom Lite** or any ESP32 DevKit
- USB-C cable

### Dependencies

PlatformIO installs these automatically:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** drives the SK6812 RGB LED. **NimBLE-Arduino** provides the passive BLE scanning stack — it is preferred over the default ESP32 BLE library because it supports passive scan mode cleanly, avoids sending scan request packets, and has lower memory overhead.

### Flash to M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Build and flash for Atom Lite
pio run -e atom-lite -t upload

# Serial monitor at 115200 baud
pio device monitor -b 115200
```

### Flash to Generic ESP32 DevKit

```bash
pio run -e esp32dev -t upload
```

### Project Structure

```
eye-spy/
├── src/
│   └── main.cpp          # All firmware logic
├── platformio.ini         # Build environments (atom-lite, esp32dev)
├── partitions_4mb.csv     # 4 MB flash partition table
└── README.md
```

### platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

The `atom-lite` environment uses the `m5stick-c` board definition — same ESP32-PICO-D4 silicon with a compatible pin mapping for GPIO 27 NeoPixel.

---

## Detection Notes and Practical Limitations

### What Eye Spy Cannot Do

**5 GHz WiFi**: The ESP32 is a 2.4 GHz-only device. Any surveillance camera, ALPR system, or access point operating exclusively on 5 GHz bands will not be visible to the WiFi scan or promiscuous engines. Many modern IP cameras are 2.4 GHz capable even if they also support 5 GHz, but dedicated 5 GHz-only deployments will be missed.

**Encrypted BLE**: Several high-end surveillance products encrypt or obfuscate their BLE advertisements. Eye Spy detects devices that broadcast identifiable signatures — OUIs, service UUIDs, manufacturer data — in plaintext. Devices that rotate MAC addresses (a privacy feature increasingly common in consumer trackers) will evade MAC-based detection and may only be caught by the persistence tracker if they rotate on a schedule slower than 5 minutes.

**Wired cameras**: IP cameras connected via Ethernet and not running a WiFi radio will produce no wireless emissions for Eye Spy to detect. Hidden cameras without network connectivity (purely local recording) similarly produce no RF signature.

**Range limitations**: The ESP32 antenna has practical indoor receive range of 20–40 meters for strong signals, less for weak or obscured signals. Devices at the edge of range or behind significant RF shielding may score zero or fail the −90 dBm RSSI threshold filter.

### False Positives to Expect

**Consumer cameras at neighbors' homes**: Ring, Nest, Wyze, Arlo, and Reolink cameras are ubiquitous in residential neighborhoods. Their OUIs appear in the 31-entry camera table. In residential environments, you should expect some yellow (Caution, +3) hits from neighbors' doorbell cameras. These are not false positives in the technical sense — the device *is* detecting a camera — but context matters.

**Retail iBeacon deployments**: Major retailers deploy iBeacon infrastructure in virtually every store. Any detection trip to a mall or grocery store will likely trigger the iBeacon detection (+2). Again, the device is doing its job — the retail tracking infrastructure really is there.

**Ubiquiti UniFi infrastructure**: UniFi access points appear in the surveillance camera OUI table because Ubiquiti manufactures both networking and security camera products under overlapping OUI ranges. A deployment that uses UniFi networking gear will score +3 on OUI matches from the WiFi scan engine.

**Samsung SmartTag vs. consumer devices**: The SmartTag UUID (`0xFD5A`) is a Samsung-registered service. Samsung SmartTags are consumer product trackers with legitimate personal use. Any Samsung SmartTag owner in vicinity will trigger this detection.

### What Each Score Level Actually Means in Practice

| Score | Likely Real-World Situation |
|-------|-----------------------------|
| 6–10 (🔴) | Credible high-confidence detection: Axon camera within ~30m, Flock Safety camera with matching OUI, confirmed AirTag following pattern, or drone broadcasting Remote ID |
| 3–5 (🟡) | Multiple consumer trackers, neighbor cameras accumulating, possible Flock camera, or a single OpenDroneID detection |
| 0–2 (🟢) | No significant surveillance signatures detected; normal consumer device chatter present but scored below threshold |

---

## Comparison to Related Projects

Eye Spy targets physical surveillance in the environment; the [ESP32 WiFi Canary](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) targets network-layer WiFi attacks against your own devices. They are complementary tools addressing different threat models.

| Capability | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| AirTag / tracker detection | ✅ | ❌ |
| ALPR / Flock camera detection | ✅ | ❌ |
| Body camera detection | ✅ | ❌ |
| Drone (Remote ID) detection | ✅ | ❌ |
| Evil-twin AP detection | ❌ | ✅ |
| Deauth attack detection | ❌ | ✅ |
| Security downgrade detection | ❌ | ✅ |
| Baseline learning | ❌ | ✅ |
| Passive BLE | ✅ | ❌ |
| Same hardware platform | ✅ | ✅ |

Both projects run on the same M5Stack Atom Lite hardware using the same LED indicators and PlatformIO build system. For a comprehensive physical + network surveillance awareness kit, both can be flashed to different Atom Lite units and carried simultaneously.

Eye Spy also complements the [Flock You detection project](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) for users specifically concerned about ALPR surveillance infrastructure.

---

## Use Cases

### Counter-Surveillance Awareness

The primary audience for Eye Spy is anyone who wants ambient awareness of surveillance infrastructure in their immediate vicinity. Walking through a neighborhood, driving past a traffic intersection, or attending a public event — Eye Spy provides a real-time signal that collapses complex RF analysis into a single LED state.

### AirTag Stalking Detection

AirTag-based stalking is a documented problem. Eye Spy's follower detection engine (unknown persistent BLE MAC seen ≥3× over ≥5 minutes) specifically addresses modified or custom trackers that don't match Apple's known advertisement format. Combined with the direct AirTag detection, it provides two independent paths to catching a tracker that's following you.

### Rental Property / Hotel Room Inspection

Entering a new hotel room or rental property with Eye Spy running gives a first-pass indication of unexpected BLE and WiFi-broadcasting devices. A camera keyword SSID match or surveillance OUI in the WiFi scan engine adds Caution-level points. This is not a substitute for a proper RF sweep, but it adds a passive ambient layer to any physical inspection.

### ALPR Deployments / Privacy Research

For researchers documenting surveillance infrastructure, journalists working in surveilled environments, or privacy advocates mapping ALPR deployments, Eye Spy provides field-portable detection hardware at minimal cost. The serial output provides a log of every detection with RSSI, making it suitable for use as a simple data collection device.

### Travel Security

Like the WiFi Canary, Eye Spy is designed for travel form factor. The Atom Lite fits in any pocket or attaches to a bag. During travel through airports, train stations, or public events with known surveillance density, it provides continuous passive monitoring without requiring any interaction.

---

## Architecture Notes

### Why Passive BLE Matters

The choice of passive BLE scanning (no scan request packets) has meaningful security consequences. In standard BLE scanning, a scanner transmits a SCAN_REQ packet requesting additional advertising data from each advertiser. This means active BLE scanning is mutually observable — the device being scanned sees the scanner's address in the scan request.

NimBLE passive mode listens only to undirected advertising packets (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) without ever transmitting a SCAN_REQ. The eye-spy device produces zero BLE transmission during the scan phase. An Axon body camera, Flock device, or AirTag being detected cannot observe or react to the scanner's presence.

### The Persistence Tracker Design

The unknown-device persistence tracker maintains a table of up to 50 BLE MAC addresses with first-seen and last-seen timestamps. Detection fires when a MAC has been seen three or more times across a window of five or more minutes.

The 50-entry limit and 30-minute purge window are engineering choices that balance detection sensitivity against RAM constraints on the ESP32. In a dense BLE environment (transit, conference, mall), the table may fill quickly with consumer devices. The −90 dBm RSSI threshold reduces this by filtering out distant devices, keeping the tracker focused on nearby persistent sources.

### Score Decay and Cooldown Interaction

The 120-second re-score cooldown prevents a device that permanently stays in range from continuously stacking points every 9-second BLE cycle. Without the cooldown, a single Flock camera would add +5 every 15 seconds, reaching hundreds of points in minutes.

The 60-second score decay means that once a device leaves range (and its cooldown expires without re-triggering), the score drops by 1 per minute. A single +5 detection that doesn't re-trigger will decay to zero in 5 minutes. This gives the device a natural "all clear" time that matches plausible transit scenarios.

---

## Contributing and Project Status

Eye Spy is available at [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy) under the Apache-2.0 license.

Potential areas for extension include:

- **Additional OUI entries**: The Flock Safety and camera OUI tables can be extended as new hardware MACs are documented in the field
- **Additional BLE service UUIDs**: New Smart Glasses, cameras, or trackers entering the market introduce new UUIDs
- **Persistence tracker tuning**: The 50-entry limit, 3-sighting threshold, and 5-minute window are adjustable constants
- **Serial data logging**: The serial output format is designed for programmatic parsing — an external logger could aggregate detection events from multiple Eye Spy units

The firmware is a single `main.cpp` in the `src/` directory, making it straightforward to read, audit, and modify.

---

## Conclusion

Eye Spy addresses a narrow but meaningful problem: the physical surveillance environment around you is increasingly instrumented, and most of that instrumentation broadcasts detectable RF signatures. A $15 M5Stack Atom Lite running the Eye Spy firmware becomes a continuous ambient scanner that turns the complexity of BLE packet analysis and WiFi OUI lookups into a single RGB LED.

The confidence-scoring model reflects realistic threat weighting: an Axon body camera at law enforcement density scores +5 and immediately illuminates red; a retail iBeacon scores +2 and contributes to a broader awareness picture without triggering a false alarm on its own. Score decay and re-score cooldowns keep the device from crying wolf on transient or persistent low-level signals.

For counter-surveillance work, travel security, AirTag detection, or simply wanting to know whether something nearby is watching — Eye Spy is a practical, open-source, passively-operating tool that earns its place in any security practitioner's kit.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)
