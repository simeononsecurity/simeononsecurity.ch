---
title: "Module 9: Smart Home and IoT"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Inventory smart-home devices, map data flows, test network access, verify support and recovery, and plan safe service loss or removal for each product."
genre: ["Personal Security", "Smart Home", "IoT Security", "Privacy", "Network Segmentation"]
tags: ["smart home security", "iot security", "voice assistant privacy", "alexa privacy", "smart speaker", "iot network segmentation", "device data collection", "wearables privacy", "smart lock", "camera privacy", "firmware updates", "vlan iot", "personal security course"]
cover: "/img/cover/smart-home-iot-devices-network-segmentation.webp"
coverAlt: "An illustration of a modern smart home featuring various IoT devices like a smart speaker, thermostat, camera, and smart lock, interconnected with a network diagram on a dark background."
coverCaption: "Module 9: review each device and network connection"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**A smart device combines computing, network access, and product-specific inputs or controls.** Cameras and speakers include obvious sensors. Locks, lights, plugs, and appliances expose different event, state, account, and telemetry data. Review each product from its real hardware and service design.

This module covers the purchase decision, network segmentation for devices you did not build, voice assistant specifics, and wearables.

*Budget about 30 minutes. Start with inventory, support status, data flows, and network policy.*

## What You Will Learn

- **Evaluate** a smart device against its data practices rather than its feature list
- **Segment** IoT devices onto a separate network from your computers
- **Explain** what voice assistants retain and what changes when you disable recording
- **Assess** which wearable sensors sample data, how often they run, and where records go
- **Decide** which home functions should never connect to the internet
- **Produce** a smart home record listing devices, network segment, and firmware status

| Term | Meaning |
|---|---|
| **IoT** | Internet of Things, meaning network-connected devices beyond computers and phones |
| **Segmentation** | Applying network boundaries and policy to restrict traffic between device groups |
| **Default credential** | A factory or shared credential which needs review and replacement where supported |
| **Voice assistant** | A device or service which handles voice input under product-specific local and remote processing rules |
| **Telemetry** | Usage data a device reports back to its vendor |

## The Trade, Stated Plainly

**Smart-home benefits and data costs vary by product.** Compare required data, optional telemetry, local processing, cloud processing, retention, sharing, and service dependence against the household benefit.

| Category | Typical Collection | Honest Assessment |
|---|---|---|
| **Smart speaker** | Wake events, queries, audio, account activity, or device state under the selected settings | Review activation, indicators, retention, and linked accounts |
| **Indoor camera** | Video, motion events, audio, thumbnails, or account events under the selected settings | Review recording triggers, storage, sharing, and breach impact |
| **Smart lock** | Entry events, codes, users, battery state, or remote commands | Review access logs, recovery, overrides, and account security |
| **Thermostat** | Temperature, schedules, device state, or occupancy signals | Review remote access, sharing, and local operation |
| **Smart lighting** | Device state, schedules, scenes, and account events | Review whether cloud access adds enough household value |
| **Fitness wearable** | Sensor samples chosen by the model and enabled features | Review sampling, sync, export, retention, and deletion |

**Give cameras and microphones close scrutiny.** Their placement, account access, storage, retention, indicators, mute design, and sharing settings directly affect household privacy.

*Ask the inverse question when considering a purchase: what is the worst outcome if this vendor is breached, and would I accept the outcome for what the device does?*

## What Earns a Place on Your Network

Run this before buying, not after.

1. **Does the device require an internet connection to function?** Local operation reduces service dependence, while firmware, companion apps, supply chain, and optional cloud features might preserve vendor risk
2. **Does the vendor publish a privacy policy with specifics**, or only generalities
3. **Does it support local control** through a standard protocol rather than a vendor cloud
4. **Is there a firmware update history**, and how recent is the last one
5. **Does it require a cloud account**, and does your identity need to be real

**Prefer a documented local control path when the design fits household needs.** Local operation reduces cloud dependency. Vendor updates, account recovery, remote access, and controller security still need review.

## Test Network Segmentation

**Put suitable IoT devices on a restricted network segment.** The firewall policy decides what a compromised device reaches.

| Setup | Effect |
|---|---|
| **Guest network for IoT** | Present on many routers. Isolation behavior needs a direct test |
| **Dedicated VLAN** | A separate broadcast domain. Firewall policy and router behavior determine isolation |
| **Per-device blocking** | Firewall rules denying outbound access for devices which do not need it |

Three rules for the IoT segment:

- **Deny IoT access to computers and storage unless a documented function needs a narrow path.** Test guest isolation and firewall behavior directly
- **Deny internet access where the device does not need it**, which applies to many bulbs and sensors
- **Rename every device** to something generic, so a device list does not describe your hardware to anyone who sees it

*Our **[Network Security Checklist](/checklists/network-security-checklist/)** covers the segment design in more depth, and Module 6 covers the router configuration.*

## Voice Assistants

**A voice assistant is a microphone with a network connection and a retention policy.**

| Setting | What It Changes |
|---|---|
| **Delete voice recordings** | Removes stored audio, and review whether it also removes transcripts |
| **Disable voice purchases** | Removes the product's supported voice-purchase path when the setting works as documented |
| **Turn off personalization** | Changes the uses described by the product. Verify retained history and other account data separately |
| **Use the documented mute control** | Reduces capture according to the product design. Verify whether the control is electrical or software based |
| **Review linked accounts and skills** | Third-party access follows current scopes, tokens, account links, and revocation behavior |

**The mute design matters.** A labeled physical control might still send a software command. Check the manual, teardown, or vendor design statement before treating the control as an electrical disconnect.

*Consider whether the assistant needs to exist in bedrooms or rooms where you discuss sensitive matters. A microphone in a bedroom is a different risk from one in a kitchen.*

## Wearables

**A wearable often samples data throughout the day**, according to enabled sensors, settings, and use.

| Data | What It Reveals |
|---|---|
| **Heart rate** | Supports estimates or inferences offered by the device, subject to sensor and model limits |
| **Movement and steps** | Supports activity and routine estimates when sampling and retention are enabled |
| **Sleep patterns** | Supports estimated sleep windows and disturbances under the product method |
| **Location** | Records or infers journeys and stops when location features are enabled |
| **Audio** | Collection depends on sensors, settings, trigger design, and product behavior |

Review which parties receive wearable data through the vendor, connected apps, research programs, insurance benefits, employer programs, advertising systems, or legal process. Availability and restrictions vary by product, agreement, and jurisdiction.

*Our dedicated analysis of the trade-offs: **[Privacy-First Smartwatch Options for Data-Savvy Users](/articles/smartwatches-for-privacy-and-security-enthusiasts/)**.*

## Safety-Critical Devices

**Safety and accessibility devices need a separate decision.**

- **Life-safety systems.** Require local alarms or operation, power-loss behavior, emergency contacts, and a tested offline path
- **Access control.** Document fail-secure or fail-safe behavior, mechanical override, battery replacement, and household accessibility needs
- **Water and heating controls.** Keep local operation and freeze or leak protection after internet or vendor-service loss

Connected products sometimes add monitored safety or accessibility. Decide from fail-safe behavior, local control, power, support lifetime, household needs, and recovery evidence. Include devices in outbuildings or other places with unreliable connectivity in the offline test.

**The test is the failure mode.** Ask what happens when the internet is down, when the vendor shuts down, or when the account is locked. If the answer is unacceptable, the device belongs on a local-only path or nowhere.

*Cloud service closure or account loss might remove remote features or core operation. Record the product's documented offline behavior, support policy, export path, and mechanical or local fallback.*

{{< figure src="smart-home-iot-segmentation-and-data-flow.webp" alt="Diagram showing a home network with IoT devices isolated on a separate segment, local-only devices avoiding the internet, and data flows from cameras and voice assistants leaving the property" >}}

## The Smart Home Record

```text
SMART HOME RECORD
Devices:
  - ______________________  segment: ______  internet: yes / no / blocked
  - ______________________  segment: ______  internet: yes / no / blocked
  - ______________________  segment: ______  internet: yes / no / blocked
  - ______________________  segment: ______  internet: yes / no / blocked

Network:
  IoT segment:            guest network / VLAN / none
  Devices blocked from internet: ______________________
  Device names anonymized: yes / no

Firmware:
  Auto-update enabled:    ______________________
  Last manual check:      ______________________

Voice assistants:
  Physical mute:          yes / no
  Voice recordings deleted: yes / no
  Personalization off:    yes / no
  Skills/accounts reviewed: yes / no

Local-only (no cloud dependency):
  - ______________________
```

## Practice and Verify

Inventory first. Change one low-impact device before moving a lock, alarm, medical device, heating control, or water control.

1. Record each device, model, owner account, network, data types, controller, firmware, and support date.
2. Draw arrows from the device to the phone, hub, vendor cloud, voice assistant, and third parties.
3. Move one bulb or plug to the IoT segment.
4. Test peer access, trusted-LAN access, internet access, IPv6, DNS, local control, remote control, and casting.
5. Turn off internet access briefly where safe. Record which functions remain.
6. Review account recovery and remove an old household member or linked service.

> **Expected Result:** the selected device reaches only required services, household control still works, firmware state is known, and loss of vendor service has a documented outcome.

If discovery fails, restore the original network and inspect the protocol before adding a narrow firewall exception. If the device has no supported update path or recovery owner, increase isolation, replace the device, or document a removal date. Restore safety controls immediately after any bounded test.

```text
REDACTED EXAMPLE
Device:                smart plug, model hidden
Data flow:             plug to local hub to vendor cloud
Firmware/support:      current, support date published
IoT-to-LAN:            blocked
Internet off test:     local switch worked, schedules failed
Recovery owner:        household admin
Removal trigger:       end of security updates
```

**Pass checklist**

- [ ] Every device has an owner, support status, data flow, and removal trigger
- [ ] Network tests cover peer, LAN, internet, IPv6, DNS, and required discovery
- [ ] Local, power-loss, and vendor-end-of-service behavior are recorded
- [ ] Safety and accessibility needs appear in the decision
- [ ] Account recovery and household access were reviewed

**Primary reference, checked 2026-10-10:** [NIST IR 8425 consumer IoT profile](https://csrc.nist.gov/pubs/ir/8425/final), including device identification, configuration, data protection, access control, updates, and state awareness.

## Next Steps

1. **Continue to Module 10** and protect your accounts and cards: **[Personal Finance Security](/personal-security-course/personal-finance/)**
2. **Move one low-impact IoT device to a tested restricted segment** before changing safety-critical devices
3. **Delete stored voice recordings** and disable voice purchasing
4. **Rename each device** so the list does not describe your hardware
5. **Review the smart home checklist** for the organizational version: **[Physical Security Checklist](/checklists/physical-security-checklist/)**
6. **Read the smartwatch comparison** before buying a wearable: **[Privacy-First Smartwatch Options](/articles/smartwatches-for-privacy-and-security-enthusiasts/)**
