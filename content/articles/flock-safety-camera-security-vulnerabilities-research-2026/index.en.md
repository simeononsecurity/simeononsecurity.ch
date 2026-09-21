---
title: "Flock Safety Camera Vulnerabilities: 50+ Flaws Found"
date: 2026-05-24
lastmod: 2026-09-20
toc: true
draft: false
description: "Comprehensive analysis of 50+ critical security vulnerabilities discovered in Flock Safety ALPR cameras including hardcoded passwords, lack of encryption, unauthorized data collection, and physical access exploits based on independent security research."
genre: ["Security Research", "Vulnerability Analysis", "Surveillance Technology", "Cybersecurity", "Privacy Security", "IoT Security", "Physical Security", "Network Security", "Critical Infrastructure", "Government Technology"]
tags: ["Flock Safety Vulnerabilities", "ALPR Security", "Camera Hacking", "IoT Security Flaws", "Hardcoded Passwords", "Android Things Vulnerabilities", "Physical Access Exploit", "Network Security", "Encryption Failures", "Data Privacy Violations", "CVE Disclosures", "Security Research", "GainSec Research", "Ben Jordan Investigation", "Surveillance Camera Security", "Government Technology Flaws", "Critical Vulnerabilities", "Responsible Disclosure", "Cybersecurity Analysis", "Law Enforcement Technology", "Public Safety Security", "Wireless Access Point", "Authentication Bypass", "Clear Text Credentials", "RF Leakage", "Tempest Attack", "Information Disclosure", "Root Shell Access", "Remote Code Execution", "Security Audit", "Vulnerability Assessment", "National Security Risk", "Senate Investigation", "Bug Bounty", "Zero Day", "Exploit Development", "Penetration Testing", "Security White Paper", "404 Media Coverage", "Independent Research", "Hardware Security", "Firmware Analysis", "System Exploitation"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "A high-tech surveillance camera is depicted with bright blue and green highlights against a dark background. Abstract shapes and lines surround it, representing digital security vulnerabilities."
coverCaption: "Critical security flaws expose 80,000+ surveillance cameras to unauthorized access"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**50+ Critical Security Vulnerabilities Expose Nation's Largest Private Surveillance Network**

## Introduction: A National Security Crisis

In late 2024 and throughout 2025, independent security researchers uncovered what may be **the most significant security failure in law enforcement surveillance technology** in American history. Over **50 critical vulnerabilities** have been discovered in Flock Safety's camera systems - the same cameras that photograph and track over **150 million vehicles daily** across more than **80,000 deployments** nationwide.

This article provides a comprehensive technical analysis of these vulnerabilities based on:
- **GainSec's formal white paper** "Examining the Security Posture of an Anti-Crime Ecosystem" (51 findings, 22 assigned CVEs, 8 pending)
- **Ben Jordan's investigative journalism** and hands-on security testing
- **404 Media's reporting** on publicly exposed camera feeds
- **Official responses** from Flock Safety and U.S. Senators
- **National Vulnerability Database** (NVD) published disclosures
- **The September 2026 filesystem dump** published by Distributed Denial of Secrets, with a line-by-line technical teardown by Micah Lee and a joint WIRED and 404 Media investigation

For context on **why these cameras exist** and **privacy implications**, see our article: **[Flock Safety Camera Surveillance: Prevalence, Privacy Concerns, and Protection Strategies](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

For information on **detecting these cameras**, see: **[Flock-You Detection Project: Counter-Surveillance Hardware Guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## The Scope of the Problem

### Scale of Vulnerable Infrastructure

As of May 2026:
- **80,000+ Flock Safety cameras** deployed across the United States
- **5,000+ cities and towns** using Flock services
- **3,500+ law enforcement agencies** with system access
- **22,000+ law enforcement users** accessing databases
- **Billions of data points** stored in searchable databases

### Vulnerability Timeline

- **Late 2024**: Initial vulnerabilities discovered by security researcher Jon "GainSec" Gaines
- **February 2025**: Responsible disclosure to Flock Safety begins
- **April 2025**: First CVE assignments published
- **November 2025**: Formal white paper published with 51 findings
- **December 2025**: Ben Jordan demonstrates vulnerabilities on video
- **January 2026**: 404 Media discovers 60+ publicly accessible camera feeds
- **February 2026**: U.S. Senators request FTC investigation
- **May 2026**: Ongoing disclosure process continues

### Vulnerability Categories

The 50+ vulnerabilities span multiple categories:
1. **Authentication & Authorization** (hardcoded passwords, lack of MFA)
2. **Cryptography & Encryption** (unencrypted data at rest and in transit)
3. **Network Security** (exposed WiFi access points, clear-text credentials)
4. **Physical Security** (button press exploits, exposed USB ports)
5. **Data Privacy** (unauthorized data collection, extended retention)
6. **System Design** (outdated software, inadequate access controls)
7. **Information Disclosure** (exposed API keys, public camera feeds)

______

## The September 2026 Filesystem Dump

**In September 2026, the transparency nonprofit Distributed Denial of Secrets published complete filesystem images taken from an in-service Flock camera.** A collective calling itself **stegan0gram** unscrewed the hardware from its pole, copied the internal storage, and released the images. **404 Media** and **WIRED** ran a joint investigation, and security researcher **Micah Lee** published a technical teardown of the contents.

Every earlier finding in this article came from a researcher's lab device or a purchased unit. This dataset comes from a camera in active municipal service, which makes it the strongest evidence published to date.

*The camera was not breached over the network. It was physically removed.*

### What the Dump Contains

The release includes three partition images, and each one carries a different part of the story.

| Partition | Size | Why It Matters |
|-----------|------|----------------|
| **system** | 1.5 GB | Android system image holding **19 Flock-built apps**, among them `flock-sambuca`, `flock-collins`, and `flock-phone-home` |
| **persist** | 32 MB | Device credentials at `flock/auth0/auth0_cred`, on an **unencrypted partition built to survive a factory reset** |
| **media** | 18 GB | Logs and imagery inside a container whose **decryption key is stored on the same partition** |

### The Credentials Problem, Confirmed

The dump settles whether hardcoded credentials are theoretical or deployed. They are deployed.

**An API key granting access to Flock's backend appears hardcoded into the application binaries.** The value lives in a class called `CameraSettings` inside `com.flocksafety.android.common.lib`. Flock bundles the shared library into all 19 apps, so the key ships inside every one of them. The `flock-sambuca` app uses it during provisioning.

**The authentication flow works like this:**

1. Each camera requests credentials from a Flock server, identifying itself by **MAC address**
2. Flock's **Okta Auth0** sign-in service returns a short-lived `FlockAuth0Token`
3. The camera stores the returned credentials **in plain text**

The Auth0 client ID and client secret sit on the **unencrypted `/persist` partition**, in a file built to survive a factory reset. An attacker recovers the persist partition first, because nothing protects it.

[Critical Vulnerability #4](#critical-vulnerability-4-hardcoded-credentials-throughout-system) covers the wider pattern of hardcoded secrets across the platform.

### The Encryption Key Shipped With the Lock

Flock describes its cameras as protected by **on-device encryption**. The dump shows what the implementation looks like in practice.

The 18 GB media partition does sit inside an encrypted container. The decryption key sits on the same partition, in a filename ending `.key`. The stegan0gram collective recovered the key, unlocked the container, and read the contents. **The imagery is encrypted in the same sense a locked box is locked when the key is taped to the lid.**

Recovered logs also revealed the camera's own position. GPS coordinates appear **155 times** in the logs, clustered within roughly 100 meters, which is ordinary drift for a receiver bolted to a pole. The coordinates resolve to **Wauwatosa, Wisconsin**, a suburb of Milwaukee, where the camera was mounted on N Mayfair Road. Micah Lee matched the logs against Google Street View and identified the specific unit by serial number and MAC address.

*Encryption at rest means nothing when the key is stored beside the ciphertext.*

### What Flock Said

Flock's response repeated its position from the earlier GainSec findings. A spokesperson stated:

> "Flock takes security seriously and maintains a public Vulnerability Disclosure Policy for security researchers to report potential vulnerabilities directly to us. We received no report through that process, and based on the limited information provided, we do not have enough detail to assess the claims being made."

This response is difficult to reconcile with the timeline. The vulnerabilities in the camera's operating system were patched publicly in **2018 and 2021**, and the standards for credential storage and key management are unchanged since well before the camera shipped. **Reviewing a decade of public vulnerability history does not require an external report.**

Flock also characterized the removal and analysis of the camera as illegal, which it is under current law, while the security findings stand on their own regardless of how the hardware was obtained.

### Why This Matters More Than the Earlier Research

The GainSec white paper documented 51 findings against devices obtained legally. Flock disputed severity and argued access required physical proximity.

This dump removes those caveats. The default state of a production camera, with no modifications by its operators, contains plain-text infrastructure credentials, keys stored alongside the data they protect, and an operating system missing eight years of security patches. **None of it required an exploit. It required a wrench.**

______

## The Device Fleet

Flock sells a product line rather than a single camera, and the security properties differ by device. The specifications below come from GainSec teardowns and the firmware analysis compiled by the detection community at **[WiFi Mothership](https://wifimothership.com/flock)**.

| Device | Role | Platform | OS |
|--------|------|----------|-----|
| **Falcon** | Solar-powered ALPR camera | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Wired-power ALPR camera | Same as Falcon | Android 8.1 |
| **Raven** | Gunshot and distress audio detection | ESP32-WROOM-32D with Syntiant NDP120-B0 DSP | FreeRTOS / ESP-IDF |
| **Bravo** | Edge AI compute box | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, kernel 5.4.180** |
| **Picard** | Legacy compute box | Phased out in favor of Bravo | |
| **Condor** | PTZ camera | Not fully documented | |
| **Alpha** | Autonomous drone | Flock-designed, NDAA-compliant | Proprietary autopilot |
| **Aerodome M350** | Legacy drone | DJI Matrice M350 / M300 RTK | DJI firmware |
| **LPR Trailer (ATS-5)** | Mobile ALPR platform | All Traffic Solutions chassis with a Flock camera | Same as Falcon |
| **Wing** | Software bridge for third-party cameras | None, it wraps existing IP cameras | |

*The generational gap is the first thing worth noticing. The compute box runs Android 13 while the cameras it serves run Android 8.1, an operating system released in 2017.*

**Falcon is the device to watch.** It carries the ALPR workload, it has not moved off Android 8.1, and it stores to **32 GB of unencrypted eMMC**. The same eMMC is where the media and logs recovered by the stegan0gram collective lived. Sparrow is the same platform with wired power.

**Bravo is the opposite case.** A modern compute box running Android 13 with AI inference for camera feeds shows the company is willing to ship current software when it chooses to.

## Verified CVE Identifiers

Fifteen CVEs are assigned across the Falcon, Sparrow, Raven, and Bravo families. Every identifier below was verified against its **CVE.org record** in September 2026 rather than quoted from a secondary source.

### Gunshot Detection and Audio Devices

| CVE | Finding | CVSS |
|-----|---------|------|
| **CVE-2025-47818** | Hard-coded password for a connection | 2.2 |
| **CVE-2025-47819** | On-chip debug interface with improper access control | 6.4 |
| **CVE-2025-47820** | Cleartext storage of code | 2.0 |
| **CVE-2025-47821** | Hard-coded password for a system | 2.2 |

All four affect Gunshot Detection devices **before version 1.3**.

### License Plate Readers

| CVE | Finding | CVSS |
|-----|---------|------|
| **CVE-2025-47822** | On-chip debug interface with improper access control | 6.4 |
| **CVE-2025-47823** | Hard-coded password for a system | 2.2 |
| **CVE-2025-47824** | Cleartext storage of code | 2.0 |

These three affect License Plate Reader firmware **through version 2.2**.

### Fleet-Wide Application Flaws

| CVE | Finding | CVSS |
|-----|---------|------|
| **CVE-2025-59403** | The Collins app exposes administrative endpoints on **port 8080 with no authentication**: `/reboot`, `/logs`, `/crashpack`, and `/adb/enable`. The last one starts ADB over TCP without debugging confirmation, which hands an attacker on the same network a shell | **9.8 CRITICAL** |
| **CVE-2025-59407** | The DetectionProcessing app bundles a Java keystore together with its **hard-coded password**, and the keystore holds a private key | **9.8 CRITICAL** |
| **CVE-2025-59405** | The Peripheral app contains a cleartext DataDog API key | 7.5 |
| **CVE-2025-59409** | Production Falcon and Sparrow firmware ships **development WiFi credentials in cleartext** | 7.5 |
| **CVE-2025-59406** | The Pisco app embeds a cleartext **Auth0 client secret** | 6.2 |

### Bravo Compute Box

| CVE | Finding | CVSS |
|-----|---------|------|
| **CVE-2025-59402** | Accepts the default Thundercomm TurboX 6490 Firehose loader, allowing firmware flashing and partition dumps | 5.4 |
| **CVE-2025-59404** | Ships with the bootloader unlocked, bypassing Android Verified Boot | 7.5 |
| **CVE-2025-59408** | Ships with Secure Boot disabled | 7.3 |

**Four of these carry a network attack vector at 7.5 or higher, which means none of them require physical access.** CVE-2025-59403 is the assigned identifier for the unauthenticated API path, and it includes the `/adb/enable` call which [Critical Vulnerability #1](#critical-vulnerability-1-button-press-wireless-access-point) depends on to reach a root shell.

*The CVE records matter for a second reason. They confirm the plaintext-secret problem from independent registries rather than only from researcher writeups, and Flock's own security alert page is listed as a reference on the Raven and LPR entries.*

______

## Critical Vulnerability #1: Button Press Wireless Access Point

### CVE-2025-59403

**Severity**: CRITICAL (CVSS 9.8)

### The Exploit

The most alarming vulnerability discovered allows **anyone with physical access** to a Flock Safety camera to gain complete control in under 60 seconds:

**Step 1**: Press the button on the back of Falcon/Sparrow camera **three times**
**Step 2**: Device creates open WiFi access point
**Step 3**: Connect to WiFi network (hardcoded password: documented in GainSec white paper)
**Step 4**: Send ADB (Android Debug Bridge) enable command
**Step 5**: Connect via ADB and obtain root shell access

### Technical Details

```
Device: Flock Safety Falcon/Sparrow ALPR Camera
Hardware: Android Things 8.0/8.1 (EOL 2021)
Attack Vector: Physical button press sequence
Authentication: Hardcoded WiFi password (universal across devices)
Impact: Complete device compromise, data exfiltration, malware installation
```

### What This Enables

Once shell access is obtained, an attacker can:
- **Extract all stored imagery** (including people, not just vehicles)
- **Modify or delete evidence** stored on device
- **Install persistent malware** (survives reboots)
- **Clone device identity** for spoofing
- **Intercept and modify** video streams
- **Use device as botnet client** for DDoS attacks
- **Capture WiFi credentials** from nearby devices (honeypot attacks)
- **Disable camera** or cause denial of service

### Demonstration

Security researcher Ben Jordan demonstrated this exploit on YouTube, showing:
- Connection to WiFi access point in **under 30 seconds**
- Root shell access obtained in **under 60 seconds total**
- Complete access to file system, stored images, and system memory
- Ability to install arbitrary Android applications

**Quote from demonstration**:
> "The password for that access point is [REDACTED] in all lowercase. For every single camera that we've tried, it all has that hard-coded password. Then you just send it a command to enable ADB...it's probably under 30 seconds, you can completely shell the device and have full access to it."

### Vendor Response

Flock Safety initially claimed the vulnerability only affected **devices not connected to the cloud**, comparing them to **"an iPhone stolen off a truck before being connected"**.

*This claim was disproven.* Researchers reproduced the vulnerability **on cloud-connected devices**, across multiple camera models showing **identical vulnerability**, and on devices acquired from **different sources**. All exhibited the flaw.

______

## Critical Vulnerability #2: Outdated Android Operating System

### CVE-2025-47822 through CVE-2025-47824

**Severity**: MEDIUM to LOW (CVSS 6.4, 2.2, and 2.0)

### The Problem

Flock Safety cameras run **Android Things 8.0 or 8.1**, which:
- Was **discontinued by Google in 2021**
- Has **NO security updates since 2021**
- Has **900+ published vulnerabilities** as of 2026
- Is **5+ years out of support**

### Technical Analysis

**Operating System**: Android Things 8.0/8.1
**End of Life**: January 2021
**Known Vulnerabilities**: 900+
**Security Patches**: None since EOL
**Affected Devices**: Falcon, Sparrow, Condor, Bravo compute boxes

### What the September 2026 Dump Shows

The filesystem images published in September 2026 give exact versions for a camera in active service, rather than a lab unit.

| Component | Version On the Camera | Status |
|-----------|----------------------|--------|
| **Android** | 8.1, build dated June 5, 2025 | Security patch level **2018-06-05** |
| **Linux kernel** | 3.18.71 | Released 2017, and the 3.18 series ended at 3.18.140 in May 2019 |
| **Current Android release** | Android 17, June 2026 | Nine major versions ahead |

The camera build itself is recent. The **operating system underneath it is not**, and the patch level shows the device has received no Android security updates for **eight years**. The kernel sits **69 patch releases behind** even the end of its own maintenance branch, which is over nine years of missing fixes.

### Two Vulnerabilities Present in This Build

Micah Lee identified two publicly known flaws affecting components the camera ships with. The patch dates prove the camera predates every fix.

| CVE | Component | Effect | Patched |
|-----|-----------|--------|---------|
| **CVE-2021-1905** | Qualcomm Adreno GPU driver | A use-after-free allowing **any code on the device, including unprivileged apps, to corrupt kernel memory and take full control** | May 2021 |
| **CVE-2018-9568** "WrongZone" | Linux kernel socket handling | Type confusion over IPv6 allowing a program to **escalate to root**. Public exploit code exists | December 2018 |

Both were patched years before this camera's firmware was built. **Neither depends on physical access, because both are reachable by software already running on the device.** The proximity caveat Flock used to downplay the GainSec findings does not apply to either one.

### Comparison to Consumer Devices

For perspective:
- Your **smartphone** refuses to update after ~5 years and manufacturers **stop selling them**
- Your **home security camera** running 5-year-old software would be considered **critically insecure**
- Government agencies require **up-to-date, supported software** for sensitive systems

*Yet Flock Safety continues deploying and selling cameras running software that has no vendor support, receives no security patches, contains hundreds of known exploits, and processes sensitive law enforcement data.*

### Why This Matters

Running **EOL software** on surveillance devices means:
- **Any published Android 8.x vulnerability** works on these cameras
- **Exploit code is publicly available** for many vulnerabilities
- **No patches will ever fix** newly discovered issues
- **Regulatory compliance** (FISMA, NIST, CMMC) is impossible to achieve

______

## Critical Vulnerability #3: Lack of Encryption at Runtime

### CVE-2025-47824 and CVE-2025-59407

**Severity**: HIGH to CRITICAL (CVSS 2.0 to 9.8)

### Flock Safety's Claims vs. Reality

**Flock Safety's Website States**:
> "Data and footage is encrypted throughout the entire life cycle"

**Independent Research Findings** (GainSec & Ben Jordan):
> "In all of our research, we've not unencrypted or cracked a thing. All of it was unencrypted at runtime."

*The gap between the marketing claim and the technical reality is total.*

### What Is Unencrypted

When researchers examined devices, they found **unencrypted**:
1. **Stored video footage and imagery**
2. **License plate data and metadata**
3. **Wi-Fi credentials and API keys**
4. **Database files with detection records**
5. **Network traffic** (see Vulnerability #6)
6. **System logs with sensitive information**

### Data Retention Contradiction

**Flock Safety Claims**: Data automatically removed after 7 days
**Research Findings**: Images found dating back to **device manufacturing** (months or years old)

GainSec white paper excerpt:
> "We found images older than 7 days. In fact, stored images were captured when the camera was triggered inside the factory where the device was made."

*This means stated privacy policies are not enforced at the device level.*

### Privacy Implications

This encryption failure means:
- **Physical device theft** = immediate data breach
- **Network interception** exposes clear-text data
- **Insider threats** can easily exfiltrate data
- **Warrant protections** may not apply to unencrypted data
- **Compliance violations** for numerous regulations (HIPAA, CCPA, etc.)

______

## Critical Vulnerability #4: Hardcoded Credentials Throughout System

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407, and CVE-2025-59409

**Severity**: CRITICAL (CVSS 9.8 at the top of the range)

### Categories of Hardcoded Secrets

Security researchers discovered **extensive hardcoded credentials**:

#### 1. WiFi Access Point Passwords
- **Universal password** across all Falcon/Sparrow cameras
- **Cannot be changed** by users or administrators
- **Known to researchers** and published in white paper (redacted sections)
- **Confirmed by CVE-2025-59409**: production Falcon and Sparrow firmware (build `OPM1.171019.026`) ships **development WiFi credentials in cleartext**

#### 2. API Keys and Tokens
- **Hard-coded in firmware** and application code
- **Grants backend access** to various services
- **Found via reverse engineering** of Android APKs
- **Confirmed by the September 2026 dump**: a backend API key hardcoded in `CameraSettings` inside `com.flocksafety.android.common.lib`, a shared library bundled into **all 19 Flock apps** on the device
- **Auth0 client ID and secret stored on the unencrypted `/persist` partition** at `flock/auth0/auth0_cred`, a location built to survive a factory reset
- **Returned credentials stored in plain text** after the camera authenticates to Flock's Okta Auth0 service using its own MAC address

#### 3. Database Credentials
- **SQLite databases** with no password protection
- **MySQL/PostgreSQL** credentials in configuration files
- **Direct database access** from local shell

#### 4. Cryptographic Keystores
- **Confirmed by CVE-2025-59407**: the DetectionProcessing app bundles a Java keystore alongside its hard-coded password, and the keystore holds a **private key**
- **Severity**: CRITICAL (CVSS 9.8), because the key material travels with the binary meant to protect it

#### 5. Wi-Fi Network Names
- **List of preferred** networks hard-coded in firmware
- Enables **rogue access point** attacks (see Vulnerability #6)

#### 6. Cloud Service Credentials
- **AWS/Azure tokens** embedded in code
- **Third-party API keys** (ArcGIS, mapping services)
- **OAuth tokens** never rotated

### Attack Scenario: Rogue Network

Using hardcoded WiFi network names, researchers demonstrated:

1. Attacker sets up **fake WiFi network** matching hardcoded SSID
2. Camera **automatically connects** (prioritizes hardcoded networks)
3. Attacker captures **all network traffic** via man-in-the-middle
4. Clear-text credentials extracted from traffic
5. Attacker gains **backend system access**

**No physical access to camera required.** Proximity within WiFi range is enough.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Diagram showing five hardcoded credential attack vectors in Flock Safety cameras including WiFi passwords, API keys, database credentials, and cloud service tokens" >}}

______

## Critical Vulnerability #5: Lack of Multi-Factor Authentication

### Organizational Policy Failure

**Severity**: HIGH (Organizational)

### The Revelation

**Flock Safety doesn't require 2FA/MFA** for some law enforcement agencies, *the same agencies accessing tracking data on 150 million vehicles daily.*

Security researcher quote:
> "When I first found this out, I simply couldn't believe it. The security process you go through when you log into Disney Plus is just too much to ask some police departments to do when accessing confidential information and the location of, in some cases, virtually everyone."

### Why This Matters

Without MFA/2FA:
- **Single compromised password** = full system access
- **Phishing attacks** are highly effective
- **Credential stuffing** from other breaches works
- **Insider threats** are easier to execute
- **Stolen devices** grant immediate access

### Comparison

Security requirements for **less sensitive** systems:
- **Disney+**: 2FA available
- **Gmail**: 2FA default for new accounts
- **Banking**: 2FA required by law
- **Social media**: 2FA standard

Security requirements for **tracking 150M+ vehicles daily**:
- **Flock Safety**: 2FA optional (some agencies don't use it)

### U.S. Senator Response

This finding was specifically highlighted in **Senator Wyden's letter** requesting an FTC investigation, citing it as evidence Flock Safety has:
> "unnecessarily exposed Americans sensitive personal data to theft by hackers and foreign spies"

### Simple Solution

**USB/NFC security keys** cost **$10-25** and provide:
- **Phishing-resistant** authentication
- **No additional apps** or codes needed
- **FIDO2/WebAuthn** standard compliance
- **Simple user experience** (plug in or tap device)

*If this is "too much hassle" for law enforcement personnel, they **shouldn't have access** to national surveillance systems.*

______

## Critical Vulnerability #6: Clear-Text Network Traffic

### Awaiting Identifier Assignment

**Severity**: HIGH (CVSS 7.8 estimated by researchers)

**No CVE identifier has been assigned to this category.** The closest assigned record, CVE-2025-59406, carries the CWE-319 cleartext transmission classification, but it covers an embedded Auth0 secret rather than in-transit interception. The findings in this section still rest on the researcher writeups cited above.

### The Vulnerability

When cameras connect to networks (LTE or WiFi), they transmit data **without adequate encryption**:

**Affected Traffic**:
- License plate images and text
- Detection metadata
- System logs
- Configuration data
- Credentials (in some cases)

### Attack Vector #1: Rogue WiFi Network

Researchers demonstrated:
1. Remove SIM card from camera **OR** set up fake network with hardcoded SSID
2. Camera connects to rogue WiFi
3. Capture traffic with **Wireshark** or similar packet analyzer
4. Analyze with tools like **NetworkMiner** or **Unblo**
5. Extract **clear-text credentials** and sensitive data

Quote from GainSec research:
> "I captured the pcap data being transmitted from one of these cameras for a little while and analyzed it with Wireshark and Unblo...and sure enough there were clear text credentials in the data."

### Attack Vector #2: IMSI Catcher / Stingray

More sophisticated attack doesn't require physical proximity:
1. Use **IMSI catcher** (DIY Stingray device) or professional-grade SDR
2. **Hijack LTE connection** by impersonating cell tower
3. Camera connects to **rogue base station**
4. **Man-in-the-middle** all traffic
5. Extract credentials, imagery, and metadata

**No physical access required.** This works from **hundreds of feet away.**

### Modern Tempest Attack Potential

The clear-text transmission also enables **Tempest-style attacks** where:
- RF emissions from camera can be captured
- Video stream can be **reconstructed remotely**
- Similar to **Cold War-era CIA** techniques
- Modern SDR equipment makes this **accessible to hobbyists**

______

## Critical Vulnerability #7: Exposed Public Camera Feeds

### January 2026 Discovery

**Severity**: CRITICAL (CVSS 10.0 - Complete System Exposure)

### The Discovery

In January 2026, Ben Jordan and **404 Media** discovered that using **simple Google searches**, they could find:
- **60+ completely exposed** Flock Safety camera administrative interfaces
- **No username or password required**
- **Live video streams** and 30 days of archived footage
- **Complete camera control** panel access

### What Was Accessible

From these exposed interfaces, anyone could:
- **Watch live video feeds** in real-time
- **Review 30 days** of archived footage
- **Download video files** directly
- **Control PTZ cameras** (Pan/Tilt/Zoom) on Condor units
- **See file paths and hashes** of evidence
- **Delete evidence** with single button click
- **Modify camera settings**
- **View device serial numbers and locations**

### Privacy Violations Observed

Ben Jordan documented witnessing:
- **Family loading infant** into car at Lowe's parking lot
- **Man leaving his home** in New York in the morning
- **Woman jogging alone** on forest trail in Georgia
- **Couple arguing** at street market in Atlanta (AI auto-zoomed on faces)
- **Officer and ambulance** assisting mental health crisis in Iowa
- **Children playing** at playground in California Bay Area
- **Man on swing set** in empty park having private moment

Quote from Ben Jordan:
> "Just saying this stuff out loud nauseates me. But I'm trying to show you just a fraction of the information that anyone in the world with access to a commercial search engine has had regarding anyone who attended this market or walked on this trail in the last 31 days."

### Targeting Capabilities

The exposed Condor PTZ cameras feature **AI-powered tracking**:
- **Automatically zoom in** on people
- **Follow individuals** as they move
- **Detect and focus** on smartphones (to read screens)
- **Track multiple targets** simultaneously
- **Record continuously** with no oversight

### Doxing Potential

Ben Jordan demonstrated how easily exposed footage leads to identity:
> "Within two minutes of open source intelligence using a commercial facial recognition engine, I found out that one of them just finished medical school and the other is dealing with chronic irritable bowel syndrome. The couple also just had a baby last year...I also know that they drove over 45 minutes from their address in the suburbs."

Cross-referencing with:
- **Facial recognition** services
- **Social media** profiles
- **Public records** databases
- **Data breach** information (Park Mobile, etc.)
- **Emergency call logs** (many cities publish these)

Result: **Complete deanonymization** in minutes

______

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Overview diagram showing how exposed Flock Safety PTZ cameras with AI auto-tracking allowed public access to live video feeds of individuals at parks, trails, and parking lots" >}}

______

## Critical Vulnerability #8: Unauthorized Data Collection

### Contradiction to Public Statements

**Severity**: HIGH (Privacy/Legal Implications)

### Flock Safety's Claims

**Official Website Statement**:
> "Flock Safety doesn't capture or record data of people, only vehicles"

### Independent Research Findings

**What cameras actually do**:
1. **Motion detection** triggers camera **for anything**, not just vehicles
2. **AI looks for license plate** in image
3. **If no plate found**, image is **still stored** (not deleted)
4. **Separate folder** stores images without plates
5. **People, pedestrians, cyclists** captured and retained

*The "vehicles only" claim is false. The camera stores images of anyone who walks in front of it.*

### Verified Observations

Researchers documented cameras capturing:
- **Person walking** in front of camera (stored image)
- **Hand waving** at lens (stored image)
- **Desk or object** moved near camera (stored image)
- **Factory workers** at manufacturing facility (stored for months)

GainSec quote:
> "When I moved in front of the camera, the radar module triggered the camera module to take a picture of me. Then the onboard AI looked for a license plate and didn't find one, but it stored the image anyway to a separate folder."

### Legal Implications

This unauthorized data collection could:
- **Violate stated privacy policies** (deceptive practices)
- **Breach procurement contracts** (if cities specified "vehicles only")
- **Trigger GDPR/CCPA** violations (EU citizens, California residents)
- **Invalidate consent** agreements
- **Expose company to litigation** for false advertising

### Surveillance Scope Expansion

The **Condor PTZ cameras** (deployed 2025-2026) are **explicitly designed** to track people:
- **AI-powered person detection**
- **Automatic zoom** on faces
- **Follow tracking** as people move
- **No opt-out** mechanism
- **Often deployed** at parks, trails, transit stations

*This represents a massive scope expansion from "license plate readers" to general population surveillance, with no policy change, no new contracts, and no public notice.*

______

## Critical Vulnerability #9: Exposed USB Ports for Rubber Ducky Attacks

### Physical Access Exploitation

**Severity**: HIGH (With Physical Access)

### The Vulnerability

**Bravo Compute Boxes** and some camera models have:
- **Exposed USB-C ports** on exterior
- **No physical security** (enclosure seals)
- **Auto-execution** of USB devices
- **No authentication** required

### Rubber Ducky / BadUSB Attack

A **BadUSB device** (costs $5-15):
- Appears as **USB keyboard** to system
- **Executes pre-programmed scripts** (payloads)
- **Runs automatically** when plugged in
- **No user interaction** needed

### Attack Scenario

GainSec demonstrated:
1. Approach deployed Flock device
2. Plug in **BadUSB device** to exposed port
3. Device executes payload (script)
4. Payload installs **persistent malware**
5. Attacker **walks away**
6. Malware **phones home** over LTE/WiFi

**Total time**: Under 30 seconds

### What Payloads Can Do

Automated scripts can:
- **Enable wireless access point** (bypass button presses)
- **Install backdoor** for remote access
- **Exfiltrate data** to remote server
- **Modify footage** or evidence
- **Disable camera** or create DoS
- **Join botnet** for DDoS attacks
- **Capture credentials** from other systems

### Why This Matters

With **80,000+ cameras** often in **semi-rural locations** with **limited visibility**:
- **Physical access** is relatively easy
- **No guards** or constant monitoring
- Attached with **simple hose clamps**
- Often mounted **7 feet off ground** (reachable with stepstool)

Quote from Ben Jordan:
> "These cameras aren't exactly little impenetrable fortresses. They're plastic Android cameras and compute boxes mounted 7 feet off the ground with hose clamps."

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Attack chain diagram showing how a BadUSB device plugged into an exposed Flock Safety camera USB port can install persistent malware in under 30 seconds" >}}

______

## Critical Vulnerability #10: Publicly Exposed API Keys

### Discovery by OSINT Researcher

**Severity**: CRITICAL (CVSS 9.5)

### The Discovery

In 2025, **OSINT researcher Joshua Michael** discovered:
- **Exposed Flock Safety demo website** via Google dorking
- **5,000 lines of source code** visible
- **Live API key** embedded in code
- **Access to 50+ private layers** of geospatial data

### What The API Key Granted Access To

The exposed **ArcGIS API key** provided access to:

**1. Registration Data**
- Customer names
- Email addresses
- Number of cameras per location
- File attachment capabilities

**2. Live Patrol Car Locations** (Multiple Departments)
- Real-time GPS tracking of police vehicles
- Aurora, Colorado deployment
- Carrollton Police Department
- **National security risk**

**3. Officer Personal Information**
- Names and phone numbers
- Email addresses
- Expected patrol areas
- Home jurisdictions

**4. Hot List Alerts Database** (Dallas, Texas)
- **6,000 records** of flagged vehicles
- License plates and reasons for flags
- Detection locations and timestamps
- Camera IDs that captured vehicles
- **5 months of movement tracking**

Joshua Michael quote:
> "Anyone could Google, find this map, and trace these people's movement patterns for 5 months. Also going to note the reason category has someone in there for just 'suspect' and a bunch of others literally have no reason or are blank."

### Attack Surface

Exposed API keys enable:
- **Stalking** of specific vehicles
- **Officer safety** compromised (home addresses, patrol patterns)
- **Operational security** breached (where police are/aren't)
- **Witness intimidation** (track people who reported crimes)
- **Criminal intelligence** gathering by organized crime

### Breach Context: Flax Typhoon

Just weeks before this discovery, **Chinese state-sponsored** hacking group **Flax Typhoon** compromised ArcGIS, according to security researchers Alexa Feminina and James Zhang.

InfoSecurity Magazine quote:
> "The hackers allegedly targeted a legitimate public-facing ArcGIS application...used for disaster recovery, emergency management, and other critical functions."

**This means hostile nation-states had potential access to** police vehicle locations, officer identities, surveillance camera placements, and emergency response patterns.

______

## Additional Vulnerabilities (Summary of 50+)

### Vulnerabilities 11-51

The GainSec white paper documents **41 additional findings**, including:

**System Design Flaws**:
- Debug mode enabled in production firmware
- Insecure boot process allows bootloader compromise
- No secure element or TPM for key storage
- Predictable firmware update mechanism

**Authentication Issues**:
- Session tokens never expire
- No IP-based access restrictions
- Shared credentials across device fleets
- No certificate pinning

**Network Security**:
- Open ports with debug services
- Telnet enabled on some units
- FTP servers with weak credentials
- DNS rebinding vulnerabilities

**Privacy/Data Retention**:
- Images stored beyond stated retention
- Metadata never purged
- Facial recognition data collected
- Location tracking beyond vehicles

**Physical Security**:
- Easy disassembly of enclosures
- Exposed serial interfaces
- JTAG debugging ports accessible
- No tamper-evident seals

**Cryptographic Failures**:
- Weak random number generation
- Hardcoded encryption keys
- MD5 still used in hash chain
- Certificate validation disabled

**Information Disclosure**:
- Verbose error messages reveal internals
- Directory listing enabled on web servers
- Source code comments contain credentials
- Configuration backups world-readable

### CVE Status

As of May 2026:
- **22 CVEs assigned** and published
- **8 CVEs pending** MITRE assignment
- **21 findings** not submitted for CVE (researcher discretion)
- **All findings** documented in GainSec white paper

Full technical details: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## Flock Safety's Response

### Official Statements

**November 2025 Blog Post**:
> "Flock is committed to continuously improving security...None of the vulnerabilities detailed in the report have an impact on our customers' ability to carry out their public safety objectives."

**Claim**: Vulnerabilities require physical access and "intimate knowledge"

**Counter-Evidence**:
- Exposed camera feeds required **only Google search**
- Wireless exploits require **only proximity**
- API key exposure was **completely remote**
- Hardcoded passwords are **universally known** after disclosure

### Dismissal of Research Devices

Flock initially claimed research devices were:
> "Not connected to the cloud...like an iPhone stolen off a truck before it was ever connected"

*This was proven false.* Researchers tested **cloud-connected devices** and got identical results. Public-facing cameras exhibited the **same vulnerabilities**, and 404 Media found **60+ exposed production cameras**.

### Response to Researcher

GainSec reported attempts at responsible disclosure met with:
- **Bug bounty with NDA** (silencing disclosure)
- **No confirmation** of fixes
- **PR statement** released before 90-day window
- **No acknowledgment** of researcher in PR
- **Job loss** for researcher within 48 hours of video release

Ben Jordan reported:
- **Police visits** to his property
- **Suspected private investigators** photographing home
- **Neighbor harassment**
- **Cease and desist** threats from Flock Safety

Quote from Ben:
> "I don't view these things as consequences or punishment for researching security vulnerabilities. I view these as consequences and punishment for doing it ethically and transparently."

### Continued Deployment

*Despite all of this*, Flock Safety:
- **Continues selling** vulnerable devices
- **No firmware updates** addressing root causes
- **Still running** Android Things 8.x (EOL 2021)
- **No mandatory MFA** for law enforcement

______

## Legislative and Policy Response

### U.S. Senate Investigation Request

**February 2026**: Senators **Ron Wyden** (Oregon) and **Raja Krishnamoorthi** (Illinois) sent formal letter to FTC requesting investigation.

**Letter excerpt**:
> "Flock has unnecessarily exposed Americans sensitive personal data to theft by hackers and foreign spies."

**Grounds cited**:
- National security risks
- Deceptive privacy claims
- Inadequate security practices
- Lack of MFA requirements

### City Council Actions

**Denver, Colorado**:
- City Council **voted against** Flock contract renewal (December 2025)
- Cited Flock's "**disregard for honesty and accountability**"
- Mayor **override** via "backroom deal" (January 2026)
- Public backlash ongoing

**Evanston, Illinois**:
- Discovered **ICE using cameras** without consent
- Voted to **remove cameras**
- *Flock reinstalled cameras without authorization*
- City spending taxpayer money to **cover cameras** with sheeting and pursue legal action

**Oakland, California**:
- Delayed **$2.25 million expansion** vote
- Commissioned independent security audit
- Found Flock's efficacy claims **misleading**

### Public Records Requests

Multiple cities conducting investigations based on:
- Publicly available security research
- FOIA requests for Flock contracts
- Independent audit requirements
- Community advocacy pressure

______

## Technical Analysis: Real-World Attack Scenarios

### Scenario 1: Nation-State Surveillance

**Threat Actor**: Foreign intelligence service

**Objective**: Track government officials

**Method**:
1. Use IMSI catcher to intercept camera LTE traffic
2. Extract clear-text credentials from stream
3. Access backend via compromised API keys (or previously exposed ArcGIS layer)
4. Query database for vehicles registered to government facilities
5. Track movements of officials, military personnel

**Time to Execute**: Days (once infrastructure in place)
**Detection Likelihood**: Low (encrypted C2, mimics legitimate traffic)

### Scenario 2: Organized Crime Counter-Surveillance

**Threat Actor**: Drug trafficking organization

**Objective**: Identify police patrol patterns

**Method**:
1. Purchase BadUSB device ($15)
2. Drive to cameras in operating territory
3. Plug BadUSB into exposed USB port (30 seconds)
4. Payload disables camera or modifies footage
5. Alternative: Payload exfiltrates police vehicle tracking to remote server

**Time to Execute**: 30 seconds per camera
**Detection Likelihood**: Low (appears as legitimate device activity)

### Scenario 3: Stalker / Domestic Violence

**Threat Actor**: Abusive ex-partner

**Objective**: Track victim's movements

**Method**:
1. Obtain victim's license plate (public information)
2. Search Google for exposed Flock camera interface (January 2026 vulnerability)
3. Query 30 days of footage for vehicle appearances
4. Cross-reference with public databases (work address, home, etc.)
5. Establish pattern of life and timing

**Time to Execute**: Minutes to hours
**Detection Likelihood**: Zero (no authentication logs exist)

### Scenario 4: Evidence Tampering

**Threat Actor**: Defendant in criminal case

**Objective**: Destroy evidence before trial

**Method**:
1. Learn camera location via warrant discovery
2. Physical access to camera (button press sequence)
3. Root shell obtained
4. Navigate to evidence folder
5. Delete specific images/videos or modify timestamps

**Time to Execute**: Under 5 minutes
**Detection Likelihood**: Low (unless camera forensically examined before defense access)

### Scenario 5: Privacy Activist / Journalist

**Threat Actor**: Transparency advocate

**Objective**: Document surveillance overreach

**Method**:
1. Use detection devices (see our [Flock-You Hardware Guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Map camera locations in community
3. File FOIA requests for footage policies
4. Demonstrate vulnerabilities to city council
5. Advocate for removal or oversight

**Time to Execute**: Ongoing
**Detection Likelihood**: High (public activity)

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matrix comparing five real-world attack scenarios against Flock Safety cameras including nation-state surveillance, organized crime counter-surveillance, stalking, evidence tampering, and privacy advocacy" >}}

______

## Defending Against These Vulnerabilities

### For Law Enforcement Agencies

**Immediate Actions**:
1. **Require MFA/2FA** for all users (USB security keys)
2. **Audit access logs** monthly for unauthorized queries
3. **Restrict sharing** to minimum necessary jurisdictions
4. **Network isolation** - cameras on dedicated VLANs
5. **Physical security** - tamper-evident seals, surveillance of cameras
6. **Incident response plan** for compromise

**Contractual Requirements**:
1. **Regular security audits** by independent firms
2. **Mandatory firmware updates** within 30 days of patch release
3. **CVE notification** within 24 hours
4. **Encrypted evidence storage** with customer-managed keys
5. **SLA penalties** for security breaches
6. **Right to audit** vendor facilities and code

**Long-Term Strategy**:
1. **Transition plan** away from EOL operating systems
2. **Self-hosted infrastructure** (reduce cloud dependence)
3. **Open-source alternatives** evaluation
4. **Community transparency** about camera locations and policies

### For Flock Safety (Recommendations)

**Critical Priority** (Immediate):
1. **Disable button-press** wireless access point creation
2. **Force MFA** for all user accounts (no exceptions)
3. **Rotate all** hardcoded credentials system-wide
4. **Emergency patch** for exposed public interfaces
5. **Encryption at rest** with proper key management

**High Priority** (30 days):
1. **Migrate to supported OS** (Android 12+ or Linux-based)
2. **Bug bounty program** without NDAs
3. **Third-party security audit** - publish results
4. **Network traffic encryption** end-to-end
5. **Physical security improvements** (remove exposed USB, hardened enclosures)

**Medium Priority** (90 days):
1. **Complete redesign** of authentication system
2. **Secure boot** with verified firmware
3. **Hardware security module** integration
4. **Compliance certifications** (FedRAMP, SOC 2, ISO 27001)
5. **Customer security dashboard** with breach notifications

**Long-Term** (1 year):
1. **Open-source security components** (build trust)
2. **Adversarial testing** program (red team)
3. **Security engineering** role requirements
4. **SDLC integration** of security practices (DevSecOps)
5. **Industry standards** participation (OWASP, CIS)

### For Individuals

**Protection Strategies**:
1. **Use detection devices** (see our [Hardware Guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Map camera locations** in your area
3. **Vary routes and timing** to reduce pattern analysis
4. **Advocate at city council** for oversight and transparency
5. **FOIA requests** for your data (where legally allowed)
6. **Support privacy legislation** at state and federal levels

**OpSec Measures**:
1. **Avoid unique vehicles** (common make/model/color)
2. **Different vehicles** for sensitive activities (where legal)
3. **Alternative transportation** (bike, public transit, walking)
4. **Privacy-focused plate covers** (only if legal in jurisdiction)
5. **Faraday bags** for phones when correlation is concern

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Prioritized remediation roadmap showing immediate, 30-day, 90-day, and long-term security fixes Flock Safety should implement to address critical vulnerabilities" >}}

______

## The Research Team

### GainSec (Jon "GainSec" Gaines)

**Background**: Offensive security professional, 10+ years experience

**Contribution**:
- Discovered **47 of 51** vulnerabilities
- Published **formal white paper** with technical details
- Coordinated **responsible disclosure** with Flock Safety
- Registered **30 CVEs** (22 published, 8 pending)
- Created **Defender's Checklist** for security practitioners

**Contact**: whitepaper@gainsecmail.com
**Research**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Background**: Journalist, musician, technology investigator

**Contribution**:
- **Video documentation** of vulnerabilities
- **Public demonstrations** for journalists (The Guardian, 404 Media)
- Discovered **60+ exposed camera feeds** via Google
- **Advocacy and public education**
- **Legislative coordination** with Senator offices

**Contact**: Via YouTube channel
**Work**: YouTube - Benn Jordan

### Joshua Michael (Next AI)

**Background**: OSINT specialist, privacy researcher

**Contribution**:
- Discovered **exposed API keys** via Google dorking
- Documented **ArcGIS layer exposures**
- **OSINT methodology** for tracking research
- **Data correlation** with public breaches

**Organization**: Next AI - All-source intelligence firm

### Supporting Contributors

- **404 Media** - Investigative journalism and public disclosure
- **The Guardian** - International coverage
- **Lucy Parsons Labs** - Years of ALPR advocacy and research
- **Sassy South** - Community organizing and transparency
- **DeFlock / Will Freeman** - Camera location mapping project
- **Ed Vogel** - Legal and policy analysis

______

## Ethical Considerations

### Responsible Disclosure Timeline

The security community followed **responsible disclosure** best practices:

**Standard Protocol**:
1. Discover vulnerability
2. **90-day private notification** to vendor
3. Vendor develops and deploys patch
4. **Public disclosure** after patch or 90 days (whichever first)
5. Detailed write-up for defensive learning

**What Actually Happened**:
1. GainSec discovered vulnerabilities (Late 2024)
2. **Repeated contact** with Flock Safety (Feb 2025+)
3. Flock offered **bug bounty with NDA** (silencing)
4. Flock issued **PR statement early** (without acknowledging researcher)
5. **No confirmation** patches were deployed
6. GainSec proceeded with **public disclosure** after 90-day windows
7. Ben Jordan and 404 Media **independently verified** on production systems

### Researcher Retaliation

Both GainSec and Ben Jordan reported:
- **Job loss** or employment difficulties
- **Police visits** to personal residences
- **Suspected surveillance** of homes and property
- **Neighbor harassment**
- **Cease and desist** threats
- **Social media attacks** (called "terrorists" by Flock CEO)

This **chilling effect** on security research:
- Discourages vulnerability disclosure
- Delays critical security fixes
- Harms public safety
- Violates ethical norms of security community

*Flock Safety's response to researchers who followed disclosure protocols sets a dangerous precedent for the entire security research community.*

Quote from Ben Jordan:
> "I don't have the luxury to dedicate even more months to yet another Flock Safety vulnerability, but as you can see, this one is urgent, and frankly, I'm worried that it's already being exploited."

### The Public Interest

These researchers acted in **public interest** by:
- **Following responsible disclosure** protocols
- **Notifying vendor first** before public disclosure
- **Redacting sensitive details** that enable exploitation
- **Providing defensive guidance** for practitioners
- **Advocating for policy change** through proper channels
- **Accepting personal risk** to inform the public

Without their work:
- **80,000+ vulnerable cameras** would continue unaddressed
- **150M+ daily vehicle scans** would remain unprotected
- **Millions of Americans** would be unknowingly exposed
- **National security** would be compromised
- **No legislative action** would be underway

______

## Conclusion: The Path Forward

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Timeline diagram summarizing the 2024-2026 Flock Safety vulnerability disclosure process from initial discovery through responsible disclosure to ongoing unpatched exposure" >}}

### Current State (May 2026)

- **50+ critical vulnerabilities** documented and partially disclosed
- **80,000+ cameras** remain deployed with unpatched flaws
- **No comprehensive remediation** from vendor
- **Limited regulatory action** (FTC investigation requested but not opened)
- **Ongoing exploitation risk** to national security and individual privacy

### What Needs to Happen

**Industry-Wide**:
1. **Mandatory security audits** before government deployment
2. **Independent testing** by qualified third parties
3. **Public disclosure** of audit results
4. **Vendor liability** for security failures
5. **Standards compliance** (NIST, ISO, etc.)

**Flock Safety Specifically**:
1. **Immediate emergency patches** for critical vulnerabilities
2. **OS migration** to supported platform
3. **Public acknowledgment** of scope
4. **Compensation** for affected researchers
5. **Transparency reporting** on security posture

**Law Enforcement**:
1. **Security requirements** in procurement contracts
2. **Regular audits** of deployed systems
3. **MFA mandatory** for all users
4. **Incident response** plans
5. **Community transparency** about surveillance programs

**Legislative**:
1. **Federal standards** for surveillance technology
2. **Required disclosure** of vulnerabilities to affected parties
3. **Whistleblower protections** for security researchers
4. **Civil remedies** for privacy violations
5. **Oversight mechanisms** for surveillance systems

### The Bigger Picture

This case study represents **more than just Flock Safety.** It is emblematic of:
- **Surveillance industry** prioritizing growth over security
- **Government procurement** lacking technical expertise
- **Vendor claims** going unchallenged and unverified
- **Financial incentives** misaligned with public safety
- **Regulatory gaps** in emerging technology oversight

*Every city that signs a Flock contract without independent security verification accepts these risks on behalf of its residents.*

### Call to Action

**For Security Professionals**:
- **Support responsible disclosure** efforts
- **Contribute to open-source** security tools
- **Advocate for researcher protection**

**For Law Enforcement**:
- **Demand accountability** from vendors
- **Require security audits** before deployment
- **Implement MFA immediately**
- **Engage security community** for consultation

**For Policymakers**:
- **Pass legislation** mandating security standards
- **Fund independent audits** of surveillance technology
- **Protect whistleblowers** and researchers
- **Create oversight** bodies with technical expertise

**For the Public**:
- **Educate yourself** about surveillance in your community
- **Attend city council** meetings when contracts are discussed
- **Support organizations** fighting for transparency
- **Contact representatives** about concerns
- **Use detection tools** to map surveillance (see our [Hardware Guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### Related Reading

- **[Flock Safety Camera Surveillance: Prevalence, Privacy Concerns, and Protection Strategies](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** - Understand the surveillance landscape
- **[Flock-You Detection Project: Counter-Surveillance Hardware Guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - Build your own detection device

Waiting on the industry to fix these flaws is not a protection strategy. **[FlockYou detection devices](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** from STS Collective work today, and reader code **SIMEONONSECURITY** takes up to 20% off.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Shop FlockYou Detectors, Save 20%
{{< /centerbutton >}}

______

## References

1. [GainSec Anti-Crime Ecosystem Research - GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [GainSec White Paper - Zenodo DOI: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [GainSec Blog - Informal Technical Writeups](https://gainsec.com/)
4. [Flock Safety Official Response - November 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media - Exposed Flock Camera Feeds](https://www.404media.co/)
6. [Ben Jordan YouTube - Vulnerability Demonstrations](https://www.youtube.com/@BennJordan)
7. [National Vulnerability Database](https://nvd.nist.gov/)
8. [MITRE CVE Database](https://cve.mitre.org/)
9. [Electronic Frontier Foundation - ALPR Surveillance](https://www.eff.org/issues/automated-license-plate-readers)
10. [Senator Wyden Letter to FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs - ALPR Research](https://lucyparsonslabs.com/)
12. [DeFlock Project - Camera Mapping](https://deflockproject.org/)
13. [Distributed Denial of Secrets - Flock ALPR Camera Filesystem Images](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee - Flock cameras are riddled with security vulnerabilities and hard-coded credentials](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED and 404 Media - Hackers Got Inside a Flock Camera](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday - This Week In Security: Flock Cameras Are Old](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD - CVE-2021-1905 Qualcomm Adreno GPU Use-After-Free](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD - CVE-2018-9568 Linux Kernel Socket Type Confusion](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership - Flock Safety ALPR Detection and Device Reference](https://wifimothership.com/flock)
20. [CVE.org - CVE Program Record Search](https://www.cve.org/)
21. [Flock Safety Security Alert - Gunshot Detection and License Plate Reader](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec - Fly By Device 2: Falcon and Sparrow Wireless RCE](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec - Root from the Coop Device 3: Bravo Compute Box](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)
