---
title: "Module 7: Mobile Device Security"
date: 2026-09-30
lastmod: 2026-09-30
toc: true
draft: false
description: "A phone is a sensor platform which travels with you. This module covers carrier-level protections including SIM swap defense, permission and app inventory, stalkerware detection, and why the keyboard matters."
genre: ["Personal Security", "Mobile Security", "Privacy", "Android", "iOS"]
tags: ["mobile security", "phone privacy", "sim swap", "carrier pin", "app permissions", "stalkerware", "juice jacking", "mobile firewall", "custom keyboard privacy", "android privacy", "ios privacy", "custom rom", "location tracking", "personal security course"]
cover: "/img/cover/mobile-device-security-sensors-privacy-illustration.webp"
coverAlt: "An illustration of a smartphone surrounded by sensor icons for location, camera, microphone, and Bluetooth, with permission dialogs layered over a dark background."
coverCaption: "Module 7: the phone travels with you"
---

#### [← Return to the Personal Security Course](/personal-security-course-start/)

**A phone is a sensor platform which travels with you.** It knows your location continuously, holds a camera and two microphones, carries your authenticated sessions, and receives your second-factor codes. Losing control of it compromises almost everything in Module 1.

This module covers the carrier layer, which most guides skip, then permissions, app inventory, stalkerware, and the input methods people never think about.

*Budget about 30 minutes. The SIM PIN and the permission audit are the two highest-yield actions.*

## What You Will Learn

- **Explain** why the phone number is a security asset rather than a mere identifier
- **Configure** carrier-level protections against SIM swap
- **Audit** app permissions and background activity
- **Recognize** the indicators of stalkerware and the correct response
- **Evaluate** third-party keyboards, launchers, and input methods
- **Produce** a mobile record listing encryption status, carrier PIN, and audited permissions

| Term | Meaning |
|---|---|
| **SIM swap** | Moving your number to another SIM, which redirects calls and messages |
| **Carrier PIN** | A passcode required before a provider changes your SIM or plan |
| **Juice jacking** | Data theft through a charging cable which also carries data |
| **Stalkerware** | Monitoring software installed by someone with physical device access |
| **Sandboxing** | Isolating an app so it cannot read other apps' data |

## Why the Phone Deserves Its Own Module

**Three properties make a phone a different risk category from a laptop.**

| Property | Consequence |
|---|---|
| **Continuous location** | Movement patterns are recorded, and location is inferable without GPS |
| **Always-present sensors** | Camera, microphone, accelerometer, and Bluetooth radios |
| **It receives your second factors** | SMS and push codes arrive here, so compromise escalates to every account |

**The third property is the one to internalize.** A phone is not only a device holding your data. It is the delivery mechanism for the factor protecting your other accounts, which is why the carrier layer matters so much.

*This is also why Module 1 recommends passkeys and hardware keys over SMS. Moving the factor off the phone removes an entire attack path.*

## The Carrier Layer

**Your phone number is an asset which many services trust as proof of identity.** The trust is the vulnerability.

### Set a Carrier PIN

**This is the single most valuable phone action and it takes about ten minutes.**

A carrier PIN is a passcode your provider requires before changing your SIM, porting your number, or altering your plan. Without it, an attacker who knows your personal details convinces a support agent to move your number to their device. With it, the conversation fails.

| Attack | Effect Without a PIN | Effect With a PIN |
|---|---|---|
| **SIM swap** | Attacker receives your calls and SMS | Blocked at the provider |
| **Number porting** | Your number moves to another carrier | Requires the passcode |
| **Account recovery** | SMS-based recovery routes to the attacker | Recovery codes stay with you |

Two supporting steps:

- **Port-freeze your number** where the provider offers it, which blocks unauthorized transfers
- **Reduce your number's exposure**, since it is both a tracking identifier and a link between datasets

**A secondary number or virtual number for account recovery is worth considering** if you register with many services. Keeping the recovery number separate from the number you publish limits what a single compromise reaches.

*This connects directly to Module 1. SMS as a second factor is only as strong as the carrier protections behind it.*

## Permissions and App Inventory

**Every installed app is code with a set of granted permissions**, and most people have never reviewed the list.

### Start With the Inventory

- **Uninstall what you do not use.** An unused app still holds its permissions and still runs in the background
- **Prefer official app stores**, where applications are reviewed and cryptographically signed, though review is not a guarantee
- **Prefer the browser over a dedicated app** for services you use occasionally, since a website receives no standing permissions

### Then Audit Permissions

| Permission | Grant Only When | Warning Sign |
|---|---|---|
| **Location** | Navigation or a genuine local need | A shopping or social app requesting precise location at all times |
| **Microphone** | Voice features you use | Any app without a voice function |
| **Camera** | Photography or scanning | An app requesting camera without a stated use |
| **Contacts** | Messaging or calling apps | A game or utility reading your address book |
| **Files and photos** | Editing apps | An app requesting your entire library for one image |

**Set location to approximate rather than precise** where the platform offers the choice. A weather app does not need your street address.

Two further steps reduce background collection:

- **Restrict background activity** per app, which limits both battery drain and data collection
- **Disable connectivity you are not using.** Bluetooth, WiFi, and NFC left enabled are all continuously broadcast

*Restarting the device weekly clears in-memory state and is a low-cost habit worth keeping.*

## Stalkerware

**Stalkerware is monitoring software installed by someone with access to your device**, frequently a partner or former partner. It differs from other malware because the attacker is known to you.

Indicators worth noticing:

- **Battery draining faster than usual** or the device running warm while idle
- **Unfamiliar apps**, especially ones with generic or system-sounding names
- **Settings you did not change**, particularly accessibility services and device administrators
- **Someone showing knowledge of your activity** which they should not have

**Check accessibility services and device administrators directly.** Stalkerware frequently uses accessibility permissions, which are broad and easy to overlook.

> **Warning: do not remove stalkerware on a device you believe is monitored without a safety plan. Removal is often detectable, and the person who installed it often escalates. Consider using a different device to seek advice before acting.**

*The correct response to suspected stalkerware on a device you control is often a factory reset rather than an uninstall, since a reset is more thorough. Follow it with a new passcode the other person has never seen.*

## Input Methods and Physical Ports

**The keyboard sees everything you type**, including passwords before they reach the vault.

| Input Method | Consideration |
|---|---|
| **Stock keyboard** | Maintained by the platform vendor and covered by system updates |
| **Third-party keyboard** | Receives every keystroke, including passwords. Some also serve ads |
| **Cloud-based prediction** | Sends context to a server to improve suggestions |

**Use the stock keyboard, or a third-party keyboard with a genuine reputation and cloud features disabled.** The convenience gain rarely justifies the exposure.

Two physical considerations:

- **Avoid public charging ports where possible.** A USB port carries data as well as power, so prefer your own adapter or a power-only cable
- **Enable erase-after-failed-attempts** if the platform supports it, which limits the value of a stolen locked device

*Combined with Module 1's guidance on avoiding four-digit PINs, these two settings make a stolen phone substantially less useful to whoever holds it.*

{{< figure src="mobile-device-carrier-permission-risk-layers.webp" alt="Diagram showing mobile security layers from the carrier SIM protections at the bottom through operating system encryption, app permissions, and input methods such as keyboards" >}}

## The Mobile Record

```text
MOBILE RECORD
Device:                  ______________________
OS version:              ______________________  auto-update: on / off
Device encryption:       on / off / unknown
Lock method:             PIN (length: __) / passphrase / biometric
Erase after N attempts:  enabled / disabled

Carrier:
  Provider:              ______________________
  Carrier PIN set:       yes / no
  Port freeze:           yes / no / unavailable
  Recovery number:       separate / same as primary

Permissions audited:
  Location set to approximate: yes / no
  Apps with microphone:   ______  revoked: ______
  Apps with camera:       ______  revoked: ______
  Apps with contacts:     ______  revoked: ______

Uninstalled this session: ______________________
Accessibility services reviewed: yes / no
Keyboard:                stock / third-party: __________
```

## Next Steps

1. **Continue to Module 8** and secure the machine your accounts and files live on: **[Personal Computer Security](/personal-security-course/personal-computers/)**
2. **Set a carrier PIN and port freeze today.** This is the highest-value ten minutes in the module
3. **Audit accessibility services and device administrators** for anything you did not enable
4. **Switch location permissions to approximate** for apps which do not need precision
5. **Review your keyboard** and disable cloud prediction if you keep a third-party one
6. **Read the organizational counterpart**: **[Mobile Device Security Checklist](/checklists/mobile-device-security-checklist/)**