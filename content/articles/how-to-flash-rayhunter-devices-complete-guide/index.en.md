---
title: "How to Flash Rayhunter Devices: Complete Installation and Configuration Guide for IMSI Catcher Detection"
draft: false
toc: true
date: 2026-03-09
description: "Comprehensive guide on how to flash and configure Rayhunter devices for IMSI catcher detection. Learn installation procedures, supported devices, and where to find Rayhunter for sale."
tags: ["Rayhunter", "IMSI catcher", "cell site simulator", "mobile security", "surveillance detection", "privacy protection", "Orbic RC400L", "TP-Link M7350", "mobile hotspot", "device flashing", "cybersecurity", "wireless security", "surveillance countermeasures", "EFF", "privacy tools", "Rayhunter for sale", "installation guide", "configuration", "supported devices", "network security"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "A Rayhunter device detecting wireless signals and IMSI catchers with security shields around it"
coverCaption: "Rayhunter IMSI Catcher Detection System - Protecting Mobile Communications from Surveillance"
---

**Complete Guide to Flashing and Configuring Rayhunter - The Ultimate IMSI Catcher Detection System**

## TL;DR

**Rayhunter** is an open-source IMSI catcher detection system that runs on modified mobile hotspots to alert users when surveillance equipment attempts to intercept cellular communications. This guide covers complete installation for Orbic RC400L and TP-Link M7350 devices, configuration options, threat actor analysis, and effectiveness in 5G networks. Key points: requires compatible Qualcomm-based device, detects 2G/3G/4G surveillance through multiple heuristics, remains effective despite 5G adoption due to continued downgrade attacks, and provides essential protection for journalists, activists, and privacy-conscious individuals against government, criminal, and corporate surveillance.

**Rayhunter** is a revolutionary open-source tool designed to detect IMSI catchers (cell site simulators) that can intercept mobile communications. If you're looking for **Rayhunter for sale** or want to learn how to properly flash and configure these devices, this comprehensive guide covers everything you need to know about installation, configuration, and usage of **Rayhunter** systems.

**Sponsorship Disclosure**: This article is sponsored by [STS Collective](https://stscollective.com), the main provider of Rayhunter-compatible devices. Despite this sponsorship, all technical information, analysis, and recommendations in this guide remain completely unbiased and based solely on the official Rayhunter documentation, community feedback, and objective technical assessment.

## Introduction to Rayhunter

**Rayhunter** is an advanced IMSI catcher detection system developed by the **Electronic Frontier Foundation (EFF)**, a leading nonprofit organization dedicated to defending civil liberties in the digital world. The EFF has been at the forefront of privacy rights advocacy since 1990, fighting for digital privacy, free expression, and innovation through impact litigation, policy analysis, grassroots activism, and technology development.

This powerful tool runs on compatible mobile hotspot devices and continuously monitors cellular networks for suspicious activity that might indicate the presence of cell site simulators or "Stingrays" used for surveillance. **Rayhunter** represents the EFF's commitment to providing practical privacy protection tools to individuals and organizations who need protection from surveillance.

The **Rayhunter** system provides real-time alerts when potentially malicious cellular behavior is detected, making it an essential privacy protection tool for journalists, activists, security professionals, and privacy-conscious individuals. When you're ready to purchase compatible devices, you can find **[Rayhunter for sale](https://stscollective.com/collections/rayhunter)** through STS Collective, which serves as the main provider of these specialized devices.

### Supporting the Rayhunter Project

**Rayhunter** is an open-source project that benefits from community support. You can contribute to the project's continued development in several ways:

- **Purchase through STS Collective**: STS Collective donates a portion of profits from every Rayhunter device sale back to the EFF to support continued **Rayhunter** development and privacy research
- **Direct donations**: Support the EFF's broader privacy advocacy and **Rayhunter** development directly at **[https://supporters.eff.org/donate/donate](https://supporters.eff.org/donate/donate)**
- **Community participation**: Contribute to discussions, documentation, and testing through the official GitHub repository

Your support helps ensure **Rayhunter** remains free, open-source, and continuously improved to address evolving surveillance threats.

## Support, Feedback, and Community

**Rayhunter** is supported by an active community of security researchers, privacy advocates, and concerned citizens. You can find support and contribute to the project through various channels:

- **Official Documentation**: [Rayhunter Documentation](https://efforg.github.io/rayhunter/introduction.html) - Complete installation, configuration, and usage guides
- **GitHub Repository**: [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Community Discussions**: Open discussions on GitHub for device compatibility and troubleshooting
- **Security Research**: Collaborate with researchers to improve **Rayhunter** detection capabilities

If you're looking for compatible devices, **[Rayhunter for sale](https://stscollective.com/collections/rayhunter)** options are available through STS Collective.

## Frequently Asked Questions

### Do I need an active SIM card to use Rayhunter?

**Rayhunter** requires a SIM card to be inserted into the device, but it doesn't need to have an active service plan. The SIM card is necessary for the device to connect to cellular networks and monitor for suspicious activity. If you want to use the device as a hotspot while running **Rayhunter**, then an active plan would be required.

### How can I test that my Rayhunter device is working?

You can enable the Test Heuristic in the **Rayhunter** configuration settings. This will trigger alerts every time your device detects a cell tower, helping you verify that the system is functioning properly. This test mode is very noisy, so remember to disable it after testing.

### Should I get a locked or unlocked device?

For **Rayhunter** compatibility, unlocked devices are generally preferred, especially if you plan to use non-Verizon SIM cards. Most Verizon-branded Orbic devices are actually unlocked, but verify compatibility before purchase. You can find verified compatible devices **[Rayhunter for sale](https://stscollective.com/collections/rayhunter)** from STS Collective.

## Installation Guide

### Installing from the Latest Release

**Rayhunter** installation has been tested on macOS and Ubuntu 24.04. If you encounter issues with pre-built releases, you may need to install from source.

#### Prerequisites

Before installing **Rayhunter**, ensure you have a compatible device. For TP-Link devices, insert a FAT-formatted SD card for storing recordings.

#### Download and Setup

1. **Download the latest release**: Get the appropriate `rayhunter-vX.X.X-PLATFORM.zip` from the official releases page:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Extract and navigate to the folder**:
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Connect to your device**: Turn on your device and connect via WiFi or USB tethering. You should be able to access:
   - Orbic devices: `http://192.168.1.1`
   - TP-Link devices: `http://192.168.0.1`

#### Device-Specific Installation

**For Orbic RC400L devices** (available **[Rayhunter for sale](https://stscollective.com)**):

**Rayhunter** supports two installation methods for Orbic RC400L devices. The WiFi method is recommended for most users, while the USB method provides additional debugging capabilities.

**WiFi Installation Method (Recommended)**:
```bash
# macOS users need to run this first:
xattr -d com.apple.quarantine installer

# For Verizon RC400L (admin password is same as WiFi password):
./installer orbic --admin-password 'YourWiFiPassword'

# For Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# For Moxee devices (password format: 12$ + last 3 digits of WiFi password):
./installer orbic --admin-password='12$XXX'
```

**USB Installation Method (Advanced Users)**:
The USB method enables ADB (Android Debug Bridge) access for advanced debugging but is not recommended for typical installations:

```bash
# WARNING: USB installer is not recommended for most use cases
./installer orbic-usb
```

This method forces the device into debug mode to enable ADB access, installs the rootshell and **Rayhunter**, then reboots the device. Use this method only if you need ADB access for other purposes.

**For TP-Link M7350 devices** (available **[Rayhunter for sale](https://stscollective.com)**):
```bash
./installer tplink
```

The installer will complete the **Rayhunter** flashing process and reboot the device. You'll see a green line on the device display indicating **Rayhunter** is running successfully.

### Installing from Source

For developers or users who need to build **Rayhunter** from source, the project includes:

- **Frontend**: JavaScript SvelteKit application (`./daemon/web/`)
- **Backend**: Rust binary `rayhunter-daemon` (`./daemon/`)
- **Installer**: Rust binary that bundles everything (`./installer`)

#### Build Dependencies

Install the following dependencies:
- Rust programming language
- Node.js/npm
- C compiler tools (`build-essential` on Linux, `xcode-select --install` on macOS)

#### Build Process

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Replace 'orbic' with your device type
```

For frontend development with hot-reloading:
```bash
cd daemon/web
npm run dev
# Or with custom target:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Updating Rayhunter

Updating **Rayhunter** is identical to the installation process. Simply repeat the installation steps with the latest release to update your device to the newest **Rayhunter** version.

## Configuration

**Rayhunter** can be configured through the web interface or by editing `/data/rayhunter/config.toml` directly on the device.

### Web Interface Configuration

Access the **Rayhunter** web interface by connecting to your device's network and visiting:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Rayhunter Web Interface Dashboard" caption="The Rayhunter web interface provides comprehensive monitoring and configuration options" >}}

#### Key Configuration Options

**Device UI Level**: Controls what **Rayhunter** displays on the device screen:
- **Invisible mode**: No display output
- **Subtle mode**: Colored line indicator (green=safe, red=alert, white=paused)
- **Demo mode**: Shows orca graphics with status line
- **EFF logo**: Displays EFF logo with status line
- **High visibility**: Full-screen color display

**Device Input Mode**: Configure power button behavior:
- **Disable button control**: Power button disabled for **Rayhunter**
- **Double-tap to restart recording**: Reset alerts and restart monitoring

**Notification Settings**: Configure ntfy URL for remote alerts and enable/disable notification types for warnings and low battery alerts.

**Analyzer Heuristics**: Enable or disable specific **Rayhunter** detection algorithms based on your environment and threat model.

## Uninstalling Rayhunter

### Orbic Devices

To remove **Rayhunter** from Orbic devices:

```bash
./installer util orbic-shell --admin-password mypassword
```

Inside the shell:
```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### TP-Link Devices

For TP-Link device uninstallation:

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Remove any leftover port triggers in the TP-Link admin interface under Settings > NAT Settings > Port Triggers.

## Using Rayhunter

Once installed, **Rayhunter** runs automatically and continuously monitors cellular networks for suspicious activity. The device display shows a green line during normal operation, which changes to yellow dots, orange dashes, or red solid when potential IMSI catchers are detected.

### Rayhunter's Detection Heuristics

**Rayhunter** employs multiple sophisticated detection algorithms to identify potential IMSI catcher activity:

#### IMSI Requested Detection
This heuristic identifies suspicious sequences where cellular towers request device identity (IMSI - International Mobile Subscriber Identity) without following proper authentication protocols. **Rayhunter** monitors the timing and context of these requests, flagging abnormal patterns that indicate potential surveillance equipment.

Legitimate cellular networks follow standardized authentication procedures before requesting sensitive identifiers. IMSI catchers often bypass these protocols to quickly harvest device identities, creating detectable anomalies in the authentication sequence. This detection method is particularly effective against basic "passive" IMSI catchers that simply collect device information.

#### Connection Release/2G Downgrade Detection
**Rayhunter** continuously monitors for suspicious attempts to force mobile devices to disconnect from secure 4G/5G networks and reconnect to less secure 2G networks. This downgrade attack is a common tactic used by IMSI catchers because 2G networks have weaker encryption and are easier to intercept.

The system analyzes patterns in connection releases, looking for abnormal frequency, timing, or contextual indicators that suggest malicious intent rather than normal network optimization. Legitimate networks may occasionally suggest downgrades for coverage or capacity reasons, but **Rayhunter** can distinguish between normal network behavior and potential surveillance activities.

#### LTE SIB6/7 Downgrade Detection
System Information Blocks (SIB) are broadcast messages that cellular networks use to provide configuration information to mobile devices. **Rayhunter** specifically monitors SIB6 and SIB7 messages, which contain information about neighboring cells and frequency redirection.

Malicious actors can broadcast fake SIB6/7 messages to force devices to abandon secure 4G connections and connect to attacker-controlled 2G networks. **Rayhunter** analyzes these broadcasts for inconsistencies, abnormal redirection patterns, and other indicators that suggest the presence of rogue base stations attempting to downgrade device connections for interception purposes.

#### Null Cipher Detection
This critical detection method identifies when cellular networks suggest using no encryption (null cipher) for communications. Legitimate commercial cellular networks should never propose unencrypted connections, as this would violate security standards and regulatory requirements.

**Rayhunter** flags any network that suggests null cipher usage as highly suspicious, as this is a clear indicator of surveillance equipment attempting to intercept communications in plaintext. This heuristic is particularly effective against IMSI catchers that prioritize data collection over maintaining the appearance of legitimate network operations.

#### Incomplete SIB Detection
Legitimate cellular base stations broadcast complete System Information Blocks containing essential network configuration data. **Rayhunter** monitors for base stations that provide incomplete or missing system information, which often indicates hastily deployed or improperly configured surveillance equipment.

IMSI catchers frequently fail to implement complete cellular network functionality, focusing only on the minimum features required for device connection and data interception. By detecting these incomplete implementations, **Rayhunter** can identify potentially malicious base stations that lack the full feature set expected from legitimate cellular infrastructure.

## Threat Actors and Potential Targets

Understanding who deploys IMSI catchersresellt and who they target is crucial for assessing your personal threat model and determining appropriate **Rayhunter** configurations. Different threat actors use varying levels of sophistication, and their targeting strategies directly inform the types of surveillance activities **Rayhunter** is designed to detect.

### Government and Law Enforcement Agencies

**Threat Sophistication**: Advanced to Professional Grade
**Primary Targets**:
- Criminal suspects under investigation
- Persons of interest in national security cases
- Protesters and activists during demonstrations
- General population surveillance in high-security areas
- Foreign nationals and diplomatic personnel

**Detection Patterns**: Government-operated IMSI catchers often use sophisticated equipment that may avoid triggering basic detection heuristics. However, they frequently employ **2G downgrade attacks** and **connection release patterns** to force devices onto less secure networks for easier interception. **Rayhunter's** LTE SIB6/7 downgrade detection and connection release monitoring are particularly effective against law enforcement surveillance techniques.

**Typical Scenarios**:
- Event-based surveillance at protests, rallies, or public gatherings
- Location-based monitoring near government facilities or sensitive infrastructure
- Targeted surveillance of specific individuals under investigation
- Border and airport surveillance operations

### Intelligence Agencies (Domestic and Foreign)

**Threat Sophistication**: Professional to Military Grade
**Primary Targets**:
- Foreign intelligence operatives and assets
- Government officials and diplomatic personnel
- Defense contractors and researchers
- Corporate executives in strategic industries
- Journalists covering national security topics
- Activists working on sensitive political issues

**Detection Patterns**: Intelligence-grade equipment is designed to be stealthy, but **Rayhunter's** null cipher detection and incomplete SIB monitoring can identify even sophisticated surveillance operations. Intelligence agencies often use equipment that requests **IMSI information** during targeted operations, triggering **Rayhunter's** IMSI requested detection algorithms.

**Typical Scenarios**:
- Long-term surveillance of high-value intelligence targets
- Industrial espionage operations near corporate headquarters
- Diplomatic and embassy monitoring
- Counter-intelligence operations
- Foreign intelligence services targeting domestic assets

### Criminal Organizations

**Threat Sophistication**: Basic to Intermediate
**Primary Targets**:
- Wealthy individuals for kidnapping or extortion
- Business competitors for corporate intelligence
- Law enforcement personnel investigating organized crime
- Witnesses and informants in criminal cases
- Victims of stalking, harassment, or domestic abuse

**Detection Patterns**: Criminal organizations typically use lower-cost, commercially available IMSI catchers that trigger multiple **Rayhunter** heuristics simultaneously. These devices often exhibit **incomplete SIB implementations**, use **null ciphers** to maximize data collection, and employ aggressive **2G downgrade attacks** due to limited technical sophistication.

**Typical Scenarios**:
- Tracking potential kidnapping or robbery targets
- Monitoring law enforcement communications during criminal operations
- Corporate espionage and competitive intelligence gathering
- Stalking and harassment campaigns
- Witness intimidation and location tracking

### Corporate Espionage and Private Intelligence

**Threat Sophistication**: Intermediate to Advanced
**Primary Targets**:
- Executive leadership of competing companies
- Research and development teams
- Merger and acquisition negotiators
- Intellectual property holders
- Trade secret custodians
- Corporate whistleblowers and insider threat sources

**Detection Patterns**: Corporate surveillance operations often use mid-tier equipment that balances cost with capability. These deployments frequently trigger **connection release detection** and **IMSI requested alerts** when targeting specific individuals during business negotiations or product development cycles.

**Typical Scenarios**:
- Surveillance during merger and acquisition negotiations
- Competitive intelligence gathering at trade shows and conferences
- Intellectual property theft operations
- Employee monitoring and insider threat detection
- Customer data harvesting for competitive advantage

### Private Investigators and Surveillance Firms

**Threat Sophistication**: Basic to Intermediate
**Primary Targets**:
- Individuals under investigation for insurance fraud
- Spouses in divorce proceedings
- Employees suspected of misconduct
- Individuals involved in legal disputes
- Celebrity and high-profile targets

**Detection Patterns**: Private surveillance operations typically use commercially available equipment with limited customization. These systems often trigger **Rayhunter's** basic detection heuristics, particularly **null cipher detection** and **incomplete SIB monitoring**, due to cost constraints and technical limitations.

**Typical Scenarios**:
- Divorce and custody investigations
- Insurance fraud surveillance
- Employee misconduct investigations
- Celebrity stalking and paparazzi operations
- Legal case investigation and evidence gathering

### Malicious Individuals and Hacktivists

**Threat Sophistication**: Basic to Intermediate
**Primary Targets**:
- Personal enemies or romantic interests
- Public figures and celebrities
- Random victims in public spaces
- Participants at specific events or locations
- Members of targeted communities or groups

**Detection Patterns**: Individual actors typically use basic, often improvised IMSI catcher setups that trigger multiple **Rayhunter** detection algorithms simultaneously. These deployments commonly exhibit **null cipher usage**, **incomplete SIB broadcasts**, and crude **2G downgrade attempts**.

**Typical Scenarios**:
- Stalking and harassment campaigns
- Identity theft and financial fraud operations
- Political activism and protest disruption
- General cybercriminal activities
- Opportunistic surveillance at public events

### Threat Assessment and Rayhunter Configuration

**High-Risk Individuals** (journalists, activists, government officials, executives) should enable all **Rayhunter** heuristics and use **high visibility** display modes for maximum detection capability.

**Moderate-Risk Individuals** (general privacy-conscious users) can use **subtle mode** displays with core detection heuristics enabled for daily protection without attracting attention.

**Event-Based Protection** (protests, sensitive meetings, travel) warrants temporary activation of all detection methods and notification systems for comprehensive surveillance awareness.

Understanding your threat model helps optimize **Rayhunter** configurations for your specific risk profile while ensuring appropriate detection coverage for the threat actors most likely to target you or your activities.

## Rayhunter Effectiveness in the 5G Era

As cellular networks transition to 5G technology, questions arise about **Rayhunter's** continued effectiveness given its support for 2G, 3G, and 4G/LTE detection but not native 5G surveillance methods. Understanding the current limitations and ongoing relevance of **Rayhunter** in a 5G world is crucial for planning long-term surveillance detection strategies.

### Why Rayhunter Remains Effective in 5G Networks

#### Downgrade Attack Persistence
The fundamental attack vector that **Rayhunter** detects—forcing devices to connect to less secure networks—remains highly relevant in 5G deployments. **IMSI catchers continue to rely on 2G and 3G downgrade attacks** because:

- **Lower implementation costs**: Building surveillance equipment for older protocols requires significantly less investment than developing 5G-capable systems
- **Broader device compatibility**: Targeting 2G/3G ensures surveillance works against older devices that may not support 5G
- **Established attack methodologies**: Surveillance techniques for 2G/3G networks are well-documented and tested
- **Regulatory advantages**: Some older surveillance technologies may face fewer legal restrictions than cutting-edge 5G interception methods

#### Network Backward Compatibility
5G networks maintain **backward compatibility with 4G/LTE**, and most mobile devices support multiple generations simultaneously. This compatibility creates ongoing opportunities for the downgrade attacks that **Rayhunter** specializes in detecting:

- **Automatic fallback mechanisms**: Devices naturally fall back to 4G when 5G coverage is poor, creating opportunities for surveillance equipment to intercept these transitions
- **Protocol negotiation vulnerabilities**: The handshake process between different network generations can be manipulated by sophisticated IMSI catchers
- **Coverage gap exploitation**: Surveillance equipment strategically deployed in areas with incomplete 5G coverage can force devices onto monitored 4G/LTE networks

#### Gradual 5G Deployment Timeline
The **slow rollout of comprehensive 5G coverage** ensures **Rayhunter** remains relevant for years to come:

- **Urban vs. rural disparities**: Many regions still rely primarily on 4G/LTE networks, making **Rayhunter** detection capabilities directly applicable
- **Indoor coverage limitations**: 5G signals often struggle with building penetration, causing devices to fall back to 4G networks that **Rayhunter** can monitor effectively
- **International travel considerations**: Global 5G deployment varies significantly by country, ensuring 4G/LTE surveillance remains a concern for travelers

#### Threat Actor Technology Lag
**Surveillance equipment acquisition and deployment cycles** often lag behind commercial network technology:

- **Government procurement timelines**: Law enforcement and intelligence agencies may continue using existing 4G-capable surveillance equipment for several years after 5G deployment
- **Cost-benefit analysis**: Many surveillance operations achieve their objectives with less expensive 4G/LTE interception, reducing incentives to upgrade to 5G-capable systems
- **Training and expertise requirements**: Operating 5G surveillance equipment requires specialized knowledge that may take time to develop within surveillance organizations

### Limitations of Rayhunter in True 5G Environments

#### Native 5G Surveillance Blind Spots
**Rayhunter** cannot detect **native 5G IMSI catcher operations** that don't rely on downgrade attacks:

- **5G standalone (SA) networks**: When devices connect to pure 5G networks without falling back to 4G, **Rayhunter** cannot monitor these communications
- **Advanced 5G surveillance equipment**: Sophisticated threat actors with access to cutting-edge technology could potentially intercept 5G communications without triggering **Rayhunter's** detection heuristics
- **Network slicing exploitation**: 5G network slicing capabilities could potentially be abused for surveillance purposes in ways that **Rayhunter** cannot detect

#### Enhanced 5G Security Features
5G networks incorporate **improved security measures** that could reduce the effectiveness of traditional surveillance techniques:

- **Stronger encryption protocols**: 5G implements more robust encryption standards that are harder to break than previous generations
- **Enhanced authentication procedures**: Improved device authentication in 5G networks could make IMSI harvesting more difficult
- **Network security monitoring**: 5G infrastructure includes better intrusion detection capabilities that might identify and counteract surveillance attempts

#### Device Behavior Changes
As 5G becomes more prevalent, **mobile device behavior may evolve** in ways that affect **Rayhunter's** detection capabilities:

- **Reduced willingness to downgrade**: Future device software updates might become more resistant to downgrade attacks as 5G coverage improves
- **5G-first connectivity preferences**: Devices may increasingly prioritize 5G connections and become more suspicious of requests to use older network protocols
- **Enhanced security awareness**: Mobile operating systems may implement better detection of suspicious network behavior

### Strategic Considerations for Rayhunter Deployment

#### Current Deployment Recommendations
For immediate and near-term deployment, **Rayhunter** provides **comprehensive surveillance detection capabilities**:

- **Urban deployments**: Even in major cities with extensive 5G coverage, **Rayhunter** detects surveillance attempts targeting 4G/LTE networks
- **Critical event protection**: For protests, sensitive meetings, or high-risk activities, **Rayhunter** provides essential detection capabilities regardless of 5G availability
- **Travel security**: **Rayhunter** remains highly effective for detecting surveillance during domestic and international travel

#### Future-Proofing Strategies
Organizations and individuals planning long-term surveillance detection should consider:

- **Hybrid detection approaches**: Combining **Rayhunter** with other security tools and monitoring techniques provides comprehensive coverage across multiple threat vectors
- **Regular threat assessment updates**: Monitoring the evolution of surveillance technology helps inform decisions about when to supplement or replace **Rayhunter** capabilities
- **Community development support**: Supporting **Rayhunter's** open-source development increases the likelihood of 5G detection capabilities being added in future releases

#### Technology Evolution Monitoring
The **Rayhunter** community and EFF continue researching **5G surveillance detection capabilities**:

- **Protocol analysis research**: Ongoing research into 5G protocols may identify new detection opportunities for future **Rayhunter** versions
- **Hardware compatibility studies**: Evaluating whether current **Rayhunter**-compatible devices can be enhanced to detect 5G surveillance attempts
- **Threat landscape monitoring**: Tracking the development and deployment of 5G-capable surveillance equipment informs future **Rayhunter** development priorities

**Rayhunter** remains a **critical surveillance detection tool** in the current telecommunications landscape, with continued relevance expected for several years as 5G deployment progresses gradually and threat actors continue relying on proven downgrade attack methodologies.

### Re-analyzing Recordings

**Rayhunter** continuously improves its detection capabilities. You can re-analyze old recordings to benefit from updated heuristics by clicking "N warnings" in the web interface and selecting "re-analyze."

### Desktop Analysis

For advanced users, **Rayhunter** includes `rayhunter-check`, a CLI tool for analyzing PCAP and QMDL files on desktop systems:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Debug mode
```

## Supported Devices

**Rayhunter** supports various mobile hotspot devices with Qualcomm modems that expose the `/dev/diag` interface.

{{< figure src="rayhunter-device-regions.svg" alt="Rayhunter Device Compatibility by Region" caption="Device compatibility and regional recommendations for Rayhunter installations" >}}

### Recommended Devices

These devices have been extensively tested and are widely used in the **Rayhunter** community:

#### Orbic RC400L (Sometimes branded Kajeet RC400L)
- **Recommended region**: Americas
- **Supported bands**: 
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Global & Roaming: n257/n78
- **Availability**: **[New Rayhunter Orbic RC400L](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** and **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)** - Compatible devices available
- **Price range**: Professional models available through STS Collective

#### TP-Link M7350
- **Recommended region**: Africa, Europe, Middle East (also works in Americas but typically more expensive)
- **Special requirements**: Requires FAT-formatted SD card for recordings
- **Availability**: **[TP-Link M7350 Rayhunter](https://stscollective.com/collections/rayhunter)** - Verified compatible models available

### Functional Devices

**Rayhunter** is confirmed to work on these additional devices:

- **Wingtech CT2MHS01** (Americas) - **[Rayhunter for sale](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Americas) - **[Rayhunter for sale](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (Africa, Europe, Middle East) - **[Rayhunter for sale](https://stscollective.com)**
- **PinePhone and PinePhone Pro** (Global) - **[Rayhunter for sale](https://stscollective.com)**
- **FY UZ801** (Asia, Europe) - **[Rayhunter for sale](https://stscollective.com)**
- **Moxee hotspot** (Americas) - **[Moxee K779HSDL Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Device-Specific Installation Notes

#### Orbic/Kajeet RC400L
The Orbic RC400L is the original device for which **Rayhunter** was developed. Available **[Rayhunter for sale](https://stscollective.com)** through STS Collective.

**Installation methods**:
- **Network-based**: `./installer orbic` (recommended, works over WiFi)
- **USB-based**: `./installer orbic-usb` (provides ADB access and root shell)

**Default passwords**:
- **Verizon RC400L**: Admin password is always the same as the WiFi password (found in device menu)
- **Kajeet/Smartspot RC400L**: `$m@rt$p0tc0nf!g`
- **Moxee devices**: Password format is `12$XXX` where XXX represents the last 3 digits of the WiFi password (check under battery for WiFi password)

**Shell access**: Use `./installer util orbic-shell` after installation.

#### TP-Link M7350/M7310
These devices work reliably with **Rayhunter** and are available **[Rayhunter for sale](https://stscollective.com)**.

**Installation**: `./installer tplink` (no admin password required)
**Storage**: Insert FAT-formatted SD card before installation
**Shell access**: `./installer util tplink-shell`

#### Specialized Devices

**PinePhone and PinePhone Pro**: Global compatibility, available **[Rayhunter for sale](https://stscollective.com)**
**UZ801**: Popular in Asia-Europe regions, available **[Rayhunter for sale](https://stscollective.com)**
**Wingtech CT2MHS01**: Americas-focused device, available **[Rayhunter for sale](https://stscollective.com)**

### Adding New Devices

**Rayhunter** can potentially support any device with a Qualcomm modem that exposes `/dev/diag`. If you have a device you'd like **Rayhunter** to support, open a discussion on the official GitHub repository.

## REST API Documentation

**Rayhunter** provides a comprehensive REST API for programmatic access to device status, recordings, and configuration. The API enables integration with other security tools and automated monitoring systems.

### Official API Documentation

For complete API reference documentation, including detailed endpoint specifications, request/response examples, and authentication methods, visit the **[Official Rayhunter REST API Documentation](https://efforg.github.io/rayhunter/api-docs/)**.

### API Endpoints

The **Rayhunter** API is accessible at `http://[device-ip]:8080/api/` and provides endpoints for:

- **System status**: Monitor device health and **Rayhunter** operation
- **Recording management**: Start, stop, and download recordings
- **Alert retrieval**: Access detection alerts and analysis results
- **Configuration**: Programmatically update **Rayhunter** settings
- **Heuristic control**: Enable/disable specific detection algorithms
- **Device information**: Retrieve device specifications and capabilities
- **Network monitoring**: Access real-time cellular network data
- **Event logging**: Query historical detection events and alerts

### Authentication

API access uses the same authentication as the web interface. Ensure your **Rayhunter** device is properly secured and accessible only to authorized users.

### Integration Examples

The **Rayhunter** REST API can be integrated with various security monitoring platforms, SIEM systems, and custom automation tools. Refer to the **[official API documentation](https://efforg.github.io/rayhunter/api-docs/)** for complete implementation examples and best practices.

## Troubleshooting

### Common Installation Issues

**USB Connection Problems**: Try different USB cables or ports. Faulty USB connections frequently cause installation failures.

**macOS Security Issues**: If you see "No Orbic device found," temporarily change "Allow accessories to connect" to "Always" in security settings.

**Device Detection**: Enable the test heuristic after installation to verify **Rayhunter** is working properly.

### Getting Help

For installation support and troubleshooting:
- Check the official **Rayhunter** documentation
- Use `./installer --help` and `./installer util --help` for command options
- Join the GitHub discussions for community support
- Contact **[STS Collective](https://stscollective.com)** for device compatibility questions

## Frequently Asked Questions (FAQ)

### General Questions

#### What exactly is an IMSI catcher and how does it work?
An IMSI catcher (also called StingRay, cell site simulator, or fake cell tower) is surveillance equipment that mimics legitimate cellular towers to intercept mobile device communications. It forces nearby devices to connect to the malicious equipment instead of legitimate towers, allowing operators to harvest device identifiers (IMSI numbers), location data, call metadata, and potentially intercept communications. **Rayhunter** detects these devices by identifying abnormal cellular network behavior patterns.

#### Can Rayhunter detect all types of surveillance equipment?
**Rayhunter** specifically detects IMSI catchers and cell site simulators operating on 2G, 3G, and 4G/LTE networks. It cannot detect other types of surveillance such as WiFi monitoring, GPS tracking devices, physical surveillance, or native 5G surveillance that doesn't use downgrade attacks. **Rayhunter** is one component of a comprehensive privacy protection strategy.

#### Is it legal to use Rayhunter?
**Rayhunter** is completely legal to use in most jurisdictions as it is a passive monitoring tool that doesn't interfere with cellular networks or other devices. It simply analyzes cellular signals that your device receives naturally. However, local laws vary, so users should verify compatibility with their local regulations. The EFF developed **Rayhunter** as a legitimate privacy protection tool.

### Technical Questions

#### Why does Rayhunter require a SIM card if it doesn't need active service?
The SIM card provides the International Mobile Subscriber Identity (IMSI) needed for your device to authenticate with cellular networks and participate in the cellular protocol exchanges that **Rayhunter** monitors. Without a SIM card, the device cannot connect to cellular networks and **Rayhunter** would have no network activity to analyze for suspicious patterns.

#### How much data does Rayhunter consume during normal operation?
**Rayhunter** uses minimal data for basic monitoring since it primarily analyzes cellular protocol information rather than internet traffic. However, if you enable remote notifications via ntfy or use the device as a hotspot simultaneously, data usage will increase accordingly. The monitoring itself consumes negligible bandwidth.

#### Can I use Rayhunter while using the device as a mobile hotspot?
Yes, **Rayhunter** can operate simultaneously while the device functions as a mobile hotspot. This requires an active cellular service plan. **Rayhunter** monitoring operates independently of hotspot functionality, though using both features simultaneously will consume more battery power.

#### What's the difference between WiFi and USB installation methods?
The **WiFi method** (recommended for most users) installs **Rayhunter** over the device's wireless interface and provides standard functionality. The **USB method** enables Android Debug Bridge (ADB) access for advanced users who need debugging capabilities but is more complex and not necessary for typical installations.

### Device and Compatibility Questions

#### Why are only certain devices supported by Rayhunter?
**Rayhunter** requires devices with Qualcomm modems that expose the `/dev/diag` interface, which provides access to cellular protocol information. Most consumer devices don't expose this interface for security reasons. The supported devices have been specifically tested and confirmed to work with **Rayhunter's** requirements.

#### Can I install Rayhunter on my regular smartphone?
No, **Rayhunter** cannot be installed on regular smartphones. It requires specialized mobile hotspot devices with specific Qualcomm modems that expose diagnostic interfaces. Supported devices include the Orbic RC400L, TP-Link M7350, and several other mobile hotspot models.

#### What happens if I try to install Rayhunter on an incompatible device?
The **Rayhunter** installer includes device detection and will typically refuse to install on incompatible hardware. Attempting to force installation on unsupported devices could potentially damage the device or render it inoperable. Always verify device compatibility before attempting installation.

#### Do I need different devices for different regions?
Yes, cellular frequency bands vary by geographic region. The Orbic RC400L is optimized for Americas networks, while the TP-Link M7350 works well in Europe, Africa, and the Middle East. **Rayhunter** device compatibility information includes regional recommendations to ensure optimal performance in your location.

### Usage and Configuration Questions

#### How do I know if my Rayhunter device is working properly?
Enable the Test Heuristic in **Rayhunter's** configuration settings. This will trigger alerts every time your device detects any cell tower, confirming the system is functioning. The device display should show a green line during normal operation. Remember to disable the test heuristic after verification as it produces many alerts.

#### What should I do if Rayhunter triggers an alert?
When **Rayhunter** detects suspicious activity, first note your location and circumstances. False positives can occur due to network optimization or equipment issues. If alerts persist in the same location or during sensitive activities, consider changing locations and reviewing the alert details in the web interface to understand what was detected.

#### How often should I update Rayhunter?
Check for **Rayhunter** updates regularly (monthly recommended) as new detection heuristics and device compatibility improvements are added frequently. The EFF continuously improves **Rayhunter's** capabilities based on evolving surveillance techniques. Updating is identical to the initial installation process.

#### Can Rayhunter protect multiple people simultaneously?
**Rayhunter** detects IMSI catchers in the surrounding area, so it can potentially protect multiple people within range (typically a few hundred meters depending on signal strength). However, each individual serious about surveillance detection should consider having their own **Rayhunter** device for maximum protection and configuration control.

### Security and Privacy Questions

#### Does using Rayhunter make me more conspicuous to surveillance?
**Rayhunter** operates passively and doesn't broadcast signals that would identify it to surveillance equipment. However, using any security tool indicates privacy consciousness. The benefits of detection typically outweigh risks, especially for high-risk individuals like journalists and activists.

#### Can surveillance equipment detect that I'm using Rayhunter?
**Rayhunter** is a passive monitoring system that doesn't transmit identifying signals. Surveillance operators cannot detect **Rayhunter** usage from the cellular protocol level. Physical observation of the device or network traffic analysis might reveal **Rayhunter** usage if remote notifications are enabled.

#### What information does Rayhunter collect about me?
**Rayhunter** analyzes cellular protocol information and stores detection alerts locally on the device. It doesn't collect personal information, communications content, or location data beyond what's necessary for detection algorithms. All data remains on your device unless you choose to enable remote notifications.

### Advanced Questions

#### Can I analyze Rayhunter data on my computer?
Yes, **Rayhunter** includes the `rayhunter-check` command-line tool for analyzing recorded PCAP and QMDL files on desktop systems. This enables advanced users to perform detailed analysis of detection events and investigate suspicious activity using full computer resources.

#### How does Rayhunter perform in dense urban environments?
Dense urban areas with many legitimate cell towers can increase false positive rates as network optimization and tower handoffs occur more frequently. **Rayhunter's** algorithms are designed to distinguish between normal network behavior and surveillance activity, but users in dense areas may need to adjust sensitivity settings.

#### Will Rayhunter work during international travel?
**Rayhunter** effectiveness during travel depends on device compatibility with local cellular bands and roaming agreements. The detection algorithms work globally, but ensure your device supports the frequency bands used in your destination country. International roaming may be required for full functionality.

______

**Rayhunter** represents a crucial advancement in personal privacy protection and surveillance detection. By properly flashing and configuring **Rayhunter** on compatible devices, you gain powerful capabilities to detect IMSI catchers and protect your mobile communications from unauthorized surveillance.

Whether you're a journalist, activist, security professional, or privacy-conscious individual, **Rayhunter** provides the tools necessary to maintain mobile security in an increasingly surveilled world. For verified compatible devices, check out **[Rayhunter for sale](https://stscollective.com)** options from trusted security equipment suppliers.

## References

- [Rayhunter Official GitHub Repository](https://github.com/EFForg/rayhunter)
- [Latest Rayhunter Release](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective - Rayhunter Equipment Supplier](https://stscollective.com)
