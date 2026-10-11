---
title: "Module 6: Home Network Security"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Back up and harden a home router, then test WiFi, guest, IoT, IPv6, DNS, VPN, and inbound access with a safe rollback plan through repeatable checks."
genre: ["Personal Security", "Network Security", "Router Hardening", "Privacy", "WiFi"]
tags: ["network security", "router hardening", "wifi security", "wpa3", "vpn", "dns over https", "dns privacy", "upnp", "wps", "ssid", "guest network", "wireguard", "openvpn", "wigle", "dns leak", "port forwarding", "personal security course"]
cover: "/img/cover/home-network-security-router-devices-illustration.webp"
coverAlt: "An illustration of a modern home network with a glowing router at the center, surrounded by smart devices and abstract representations of the internet, all on a dark background with vibrant colors."
coverCaption: "Module 6: review the router trust boundary"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**The router enforces a boundary between your devices and the internet.** Router and firewall policy shape inbound, outbound, and local traffic. Device firewalls, direct cellular links, virtual private networks, and application controls form additional boundaries.

This module covers a hardening sequence in priority order, what a VPN genuinely changes, the two separate problems hiding under "secure DNS", and how your WiFi network gets catalogued by strangers.

*Budget about 40 minutes. The router work is done once and then mostly forgotten.*

## What You Will Learn

- **Sequence** router hardening by risk rather than by checkbox
- **Explain** which exposures WPS, UPnP, and remote administration each create
- **Distinguish** DNS privacy from DNS integrity
- **Evaluate** a VPN claim against what a VPN protects
- **Describe** how passive WiFi scanning builds public maps of network names and locations
- **Produce** a network record listing router settings, DNS configuration, and open ports

| Term | Meaning |
|---|---|
| **NAT** | Address translation between internal and external networks. Firewall policy provides the security decision |
| **UPnP** | A protocol letting applications request inbound port mappings automatically |
| **WPS** | A push-button pairing method with a long history of weaknesses |
| **DNS leak** | DNS queries leaving through a different path than your tunnel |
| **WiGLE** | A crowdsourced database of observed WiFi networks and locations |
| **MAC address** | A hardware identifier, and a partial tracking signal on WiFi |

## The Router Is the Boundary

**Default configurations vary by vendor.** Review exposed services, update policy, credentials, and remote management instead of treating NAT or the router's WAN address as proof of a reachable admin service.

Start the review with three common problem categories:

| Category | Examples | Consequence |
|---|---|---|
| **Credential weakness** | Default admin password, weak WiFi passphrase | Direct access to the network |
| **Convenience services** | UPnP, WPS, remote administration, cloud management | Additional access paths when exposed, misconfigured, or compromised |
| **Stale software** | Unpatched router firmware | Exploitation of known vulnerabilities |

*A router processes traffic between the home network and the internet. WAN exposure, management access, automatic updates, and support life differ by model and provider.*

## A Hardening Sequence

**Work in this order.** The early steps remove access paths, and the later steps reduce what an attacker learns.

### 1. Credentials

- **Change the admin password** before anything else. Default router credentials are published and indexed
- **Use WPA3 where supported**, or WPA2 with AES or CCMP. Review WPA2/WPA3 transition mode because legacy compatibility changes downgrade exposure
- **Use a long passphrase** rather than a short complex string, following Module 1's reasoning

### 2. Remove the Convenience Back Doors

| Feature | Risk | Action |
|---|---|---|
| **WPS** | PIN mode has known brute-force risk. Push-button mode permits enrollment during its active window | Disable when unused |
| **UPnP** | Applications open inbound ports without your knowledge | Disable unless a specific device requires it |
| **Remote administration** | Router admin panel reachable from the internet | Disable |
| **Cloud management** | Vendor-held control plane over your router | Disable if you do not use it |
| **Telnet and unused services** | Telnet sends session data without transport encryption. Unused services add attack surface | Disable |

### 3. Firmware

**Enable automatic updates if the vendor offers them.** If not, check quarterly. A router which stopped receiving updates is a decision point: replace it, or place a maintained device in front of it.

### 4. Segmentation

- **Use a guest network for visitors** after verifying client isolation and blocked access to trusted LAN devices
- **Put IoT devices on their own network** where the router supports it, covered further in Module 9
- **Place devices according to required access.** A managed or important device might still use a guest segment when internet-only access fits its role

### 5. Reduce Exposure

- **Close forwarded ports** you do not recognize. Every forwarded port is a deliberately opened inbound path
- **Review the port forwarding list** rather than assuming it is empty
- **Change the router's local address** if you want to defeat scripts which target common defaults, though the benefit is modest
- **Reduce transmit power** if your network reaches further than you need

## What a VPN Changes

**A VPN moves trust, it does not remove it.** This single sentence resolves most confusion about the technology.

| A VPN Does | A VPN Does Not |
|---|---|
| Hide destination names and traffic details from the local operator when tunnel and application encryption provide such protection | Hide traffic from the sites you visit |
| Change your apparent source address | Make you anonymous to a logged-in service |
| Protect traffic entering the tunnel on untrusted WiFi | Protect traffic outside the tunnel or malware on your device |
| Carry DNS through the tunnel when configured to do so | Guarantee which resolver handles each lookup |

**A VPN fits selected threat models.** The tunnel shifts observable connection data from the local network or internet provider to the VPN provider. HTTPS still protects application content from the VPN when correctly implemented.

Two configuration points matter:

- **Prefer a maintained modern protocol such as WireGuard, OpenVPN, or a supported TLS-based option.** PPTP is obsolete. SSTP still uses TLS on supported Windows systems, though ecosystem and audit trade-offs differ
- **Confirm the intended resolver handles DNS.** A lookup outside the tunnel might use plaintext or another encrypted resolver and exposes the name to a different path

**The honest limit:** the VPN provider sees connection metadata and traffic not protected by application encryption. You are choosing another trust point.

*Tor Browser routes traffic through multiple relays and standardizes browser behavior. Account sign-in, entry and exit observation, traffic correlation, endpoint compromise, and user behavior still affect anonymity.*

## DNS: Two Separate Problems

**People treat "secure DNS" as one thing. It is two, and they are solved differently.**

| Problem | What Is At Risk | Solution |
|---|---|---|
| **Privacy** | The resolver path might expose queried names to network parties | DNS over HTTPS or DNS over TLS protects the client-to-resolver path |
| **Integrity** | An attacker returns a forged answer | DNSSEC validation for signed data. Encryption separately protects the client-to-resolver path |

**DNS-over-HTTPS addresses privacy. DNSSEC addresses integrity.** Encrypting your DNS does not validate the answers, and validating them does not hide the questions.

Two honest caveats about encrypted DNS:

- **It moves trust rather than eliminating it.** Your resolver sees your queries instead of your internet provider, so the resolver's policy is the thing to evaluate
- **An outside encrypted resolver might bypass local DNS filtering.** Use the resolver and policy approved by the network owner for parental, school, employer, or managed networks

*Encrypted DNS protects the path to the chosen resolver. Encrypted transport does not make a malicious resolver trustworthy, validate unsigned answers, or protect a compromised endpoint.*

Inspect the addressing of a network with local tools: the **[CIDR Subnet Calculator](/cidr-calculator/)** for IPv4 ranges, and the **[IPv6 Address Expander](/ipv6-expander/)** when the network carries IPv6.

## WiFi Exposure Beyond Your Network

**Your network name is public.** Every device broadcasting an SSID is announcing it to anything in range, and crowdsourced wardriving projects have been cataloguing those observations for years.

The practical implications:

| Practice | Reason |
|---|---|
| **Do not put personal details in the SSID** | Names, flat numbers, and device models identify both you and your hardware |
| **Know SSIDs and locations get published** | Crowdsourced databases map networks to places, which correlates to a physical address |
| **Enable MAC randomization on devices** | Reduces the ability to track one device across multiple networks |
| **Understand hiding the SSID is weak** | Observed client traffic might reveal the network name, and hiding breaks some devices |

*This site maintains two mapping projects in this space, both useful for understanding what public WiFi observations reveal: **[OpenRoaming and Hotspot 2.0 Map](/sibling-sites/)** and **[Flock Finder](/sibling-sites/)**. They are demonstrations of how much is inferable from passive scanning rather than tools for your own network.*

**Assess your own exposure** by checking what your neighbourhood already reveals, then decide whether your SSID adds anything an observer did not already have.

{{< figure src="network-router-hardening-and-dns-paths.webp" alt="Diagram showing a home router with hardened settings, separate device segments, and two DNS paths illustrating plaintext lookups compared with encrypted lookups through a tunnel" >}}

## The Network Record

```text
NETWORK RECORD
Router model:            ______________________
Firmware version:        ______________________  auto-update: on / off
Admin password changed:  yes / no
WiFi security:           WPA3 / WPA2 / other
WiFi passphrase:         in vault? yes / no

Disabled:
  WPS:                   yes / no
  UPnP:                  yes / no
  Remote administration: yes / no
  Cloud management:      yes / no

DNS:
  Resolver:              ______________________
  Encryption:            DoH / DoT / none
  DNSSEC validation:     on / off / unknown
  Leak test passed:      yes / no

Segments:
  Guest network:         enabled / disabled
  IoT network:           enabled / disabled / unsupported
  Devices on guest:      ______________________

Forwarded ports (should be empty or intentional):
  - ______________________  purpose: __________
```

## Practice and Verify

Do this exercise beside the router. Save its current configuration before changing a setting. Keep a wired connection or reset instructions ready.

1. Export the router configuration and photograph cable positions.
2. Record model, firmware version, update status, WiFi mode, and remote-management state.
3. Create or review a guest or IoT network without moving safety-critical devices yet.
4. Connect two test devices to the new segment.
5. Test device-to-device access, trusted-LAN access, internet access, IPv4, IPv6, DNS, and needed casting or controller traffic.
6. Review forwarded ports from the router interface. Verify each intentional service from a separate external connection.

> **Expected Result:** test devices reach only approved destinations, unexpected inbound services stay closed, and required household functions still work.

If internet access disappears, restore the saved configuration and check DHCP, DNS, VLAN tagging, and WAN settings one change at a time. If trusted-LAN access still works, guest isolation or firewall policy is incomplete. If casting breaks, document the narrow discovery traffic needed instead of joining every device to the trusted segment.

```text
REDACTED EXAMPLE
Router/firmware:       model hidden, current vendor release
Backup:                exported before changes
Test segment:          IoT
Peer access:           blocked
Trusted LAN:           blocked
Internet/DNS/IPv6:     pass / pass / pass
Required casting:      failed, restored pending rule review
Rollback test:         configuration import located
```

**Pass checklist**

- [ ] Configuration backup and reset instructions exist
- [ ] Admin access, updates, WiFi security, WPS, UPnP, and remote management received review
- [ ] Segmentation passed peer, LAN, internet, IPv6, DNS, and required-service tests
- [ ] Every forwarded port has an owner and purpose
- [ ] The rollback route restores household connectivity

**Primary reference, checked 2026-10-10:** [NIST consumer-grade router security requirements](https://www.nist.gov/publications/recommended-cybersecurity-requirements-consumer-grade-router-products). Follow the current router manual for vendor-specific paths.

## Next Steps

1. **Continue to Module 7** and reduce what your phone reports: **[Mobile Device Security](/personal-security-course/mobile-devices/)**
2. **Change the router admin password and disable WPS and UPnP** now, which takes about five minutes
3. **Review the port forwarding list** and remove anything you do not recognize
4. **Check for DNS leaks** if you use a VPN, then confirm validation separately
5. **Explore addressing** with the **[CIDR Calculator](/cidr-calculator/)** and **[IPv6 Expander](/ipv6-expander/)**
6. **Read the organizational counterpart**: **[Network Security Checklist](/checklists/network-security-checklist/)**
