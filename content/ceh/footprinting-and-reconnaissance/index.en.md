---
title: "CEH v13: Footprinting and Reconnaissance"
date: 2025-01-01
toc: true
draft: false
description: "Master footprinting and reconnaissance for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn passive and active recon, OSINT, Google dorking, WHOIS, DNS, and tools like Maltego, theHarvester, and Shodan."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "footprinting and reconnaissance", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-footprinting-reconnaissance-techniques.webp"
coverAlt: "A digital landscape illustration showing elements of cybersecurity footprinting and reconnaissance, including magnifying glasses and interconnecting nodes against a dark backdrop with vibrant colors."
coverCaption: "Master Footprinting and Reconnaissance for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Footprinting and Reconnaissance** is the first phase of an engagement in the **EC-Council CEH v13** course. This module covers how you gather information about a target before sending a single attack packet. *The more you learn here, the less noise you make later.*

Reconnaissance builds a profile of the target: domains, IP ranges, employees, technologies, and exposed services. Good recon often decides whether a test succeeds.

## Passive vs. Active Reconnaissance

You split recon by how much you touch the target.

| Type | Contact with target | Detection risk |
|------|---------------------|----------------|
| **Passive** | None, uses third-party sources | Very low |
| **Active** | Direct queries to target systems | Higher |

Passive recon uses **OSINT** (open-source intelligence) from search engines, social media, job posts, and public records. Active recon includes DNS queries and banner grabbing that reach the target.

## OSINT and Google Dorking

Search operators turn a search engine into a recon tool. This is **Google dorking**.

```text
site:example.com filetype:pdf
intitle:"index of" site:example.com
inurl:admin site:example.com
```

These find exposed documents, open directories, and login pages. Job listings reveal the technology stack, and employee names feed later social engineering.

## DNS, WHOIS, and Network Records

You map the target's external footprint with public records.

- **WHOIS** returns registrar, contact, and registration dates for a domain.
- **DNS records** (A, MX, NS, TXT) reveal mail servers, name servers, and services.
- **BGP** data exposes the IP ranges an organization owns.

```bash
# Pull DNS records and WHOIS data
dig example.com ANY +noall +answer
whois example.com
```

## Recon Tooling

| Tool | Use |
|------|-----|
| **Maltego** | Visual link analysis of people and infrastructure |
| **theHarvester** | Collects emails, subdomains, and hosts |
| **Shodan** | Indexes internet-exposed devices and banners |
| **Recon-ng** | Modular OSINT framework |

Try the on-site [Shodan IP lookup tool](/shodan_ip/) to see exposed service data for an address. *Use these tools only against assets in your authorized scope.*

## Next Steps

Move from passive recon to active discovery in [Scanning Networks](/ceh/scanning-networks/). Review the legal limits in [Introduction to Ethical Hacking](/ceh/introduction-to-ethical-hacking/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
