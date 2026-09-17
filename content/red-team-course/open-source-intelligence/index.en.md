---
title: "Module 8: Open-Source Intelligence"
date: 2026-09-12
toc: true
draft: false
description: "Collect intelligence from public sources: Google dorks, Whois ownership, Shodan banners, SpiderFoot automation, DNS and certificate enumeration, people and code harvesting, plus the collection methodology and the OPSEC around it."
genre: ["Red Team", "Offensive Security", "OSINT"]
tags: ["red team", "OSINT", "Google dorks", "Whois", "Shodan", "SpiderFoot", "theHarvester", "Maltego", "subdomain enumeration", "certificate transparency", "crt.sh", "GEOINT", "ADS-B", "AIS", "open source intelligence", "red team course"]
cover: "/img/cover/open-source-intelligence-osint-collection-techniques.webp"
coverAlt: "A modern workspace with multiple screens showing open-source intelligence data, including social media feeds and analytics, against a dark background. Abstract data flows connect the screens."
coverCaption: "Module 8: read what the internet already knows before you touch the target."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Open-source intelligence (OSINT) is collection from public sources, done so it never triggers an alert or a deconfliction.** You read what the internet already knows. Done right, it lets you walk into active reconnaissance already knowing the network.

*This module takes about 25 minutes. The goal is to enter active recon knowing the layout, not discovering it.*

> **Why it matters:** Reading what is already public costs you no alerts. Every query you skip by using others' scan data is one less chance to burn the operation.

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Google dork** | a search operator narrowing results |
| **Whois** | the registry lookup naming an IP's owner |
| **Banner** | what a service answers when you connect |
| **ASN** | the number naming a routing block |
| **Subdomain** | a name beneath a domain, like `vpn.corp.local` |
| **Certificate transparency** | a public log of every TLS certificate issued |
| **Zone transfer** | a misconfigured DNS copy of every host in a domain |
| **OSINF** | raw open-source data, before analysis |
| **Sock puppet** | a managed research account |
| **Managed attribution** | hiding your real identity while you collect |
| **ADS-B and AIS** | aviation and maritime position broadcasts |
| **GEOINT** | intelligence from geospatial and imagery data |

______

## What OSINT Buys You

OSINT is the first active-feeling phase, yet done right it touches nothing a defender flags. The material includes the customer's own website, externally facing devices, employee posts on social media and forums, leaked documents, and scan data other people already collected.

Several services have already scanned the entire internet and stored the results. You query their data instead of scanning yourself, which keeps you quiet during the one phase where generating a deconfliction is exactly what you want to avoid.

There is a split worth holding onto. Raw open-source information (OSINF) is the unanalyzed data. OSINT is what you get after the data goes through verification and analysis. Collection is only the first step. The intelligence product, cross-checked and turned into a finding, is what feeds an attack plan.

The mindset matters as much as the tooling. Assume something useful is exposed, and go find it. Good OSINT separates a failed operation from walking straight in.

______

## Passive, Semi-Passive, and Active

OSINT spans a spectrum of how much you touch, and staying quiet depends on staying at the left end of it.

| Method | What you touch | Example |
|--------|----------------|---------|
| **Passive** | nothing, read what others already collected | search engines, Whois, certificate logs |
| **Semi-passive** | auxiliary services, not the target itself | DNS servers, third-party databases |
| **Active** | the target directly | port scans, direct banner grabs |

Stay passive as long as possible. Each step toward active collection raises your visibility and edges you into the next phase. The line between semi-passive and active is where a deconfliction starts to become possible.

______

## OPSEC for the Collector

OSINT sounds safe, but your own query tips the target. Protect the investigation with the same care you put into the operation:

- Use an isolated virtual machine with a privacy browser.
- Use a managed research account, a sock puppet, for social collection.
- Obfuscate your browser fingerprint and block DNS leaks.
- Never query from infrastructure tied to you or your employer.

Counterintelligence cuts both ways. Burn a research account or leak your IP, and the target learns someone is watching before a single packet reaches their network.

______

## Google Hacking

Google is a search engine, but for an operator it is a targeted collection tool. A handful of operators narrow results from millions to the few pages you want:

| Operator | What it does | Example use |
|----------|--------------|-------------|
| `site:` | limits results to one domain | everything indexed under the target |
| `inurl:` | matches text in the URL | find login, admin, or upload paths |
| `filetype:` | matches a file extension | surface documents, not pages |
| `intext:` | matches text in the page body | find pages mentioning a keyword |
| `intitle:` | matches text in the page title | find portal and index titles |

Stack them until the noise drops away. Point `site:` at the target and add `filetype:` to pull only documents, or add `inurl:` to find a specific kind of page. Most other search engines accept the same syntax, so the skill carries across services.

______

## What to Hunt For

Know what leaks detail, then search for it directly:

- `.vsd` Visio files hand you the network diagram and its layout.
- `.ppt` files reveal planned or newly deployed systems.
- `.txt` and `.xls` files hold potential passwords and configuration data.
- `.doc` and `.docx` files carry embedded metadata, authors, and software versions.

Beyond documents, find the human trail:

- Forums where employees posted machine names, versions, or error messages.
- Internet-exposed printers, cameras, and SCADA devices the owner forgot.
- Job postings which name the technologies and systems in use.

Any one of these names a host or reveals a credential before you send a single packet at the customer.

______

## Whois Lookups

Before you target an IP, confirm who owns it. A Whois lookup tells you which organization a block belongs to, and the check protects the operation. Firing at an address owned by a third party is a scope mistake which burns a red team.

- `whois.icann.org`
- `whois.arin.net`
- `godaddy.com/whois`

ARIN is the regional registry for North American address space, and it is where you confirm ownership of a US customer's netblocks. Cross-check against the scope documents from mission preparation. If ownership does not clearly resolve to the customer, treat the address as out of scope until it does.

______

## Shodan

**Shodan** crawls the open internet and indexes the services running on reachable devices. Where Google indexes page content, Shodan indexes what a machine says when you connect: the service banner. It captures banners across `80`, `8080`, `443`, and `8443`, plus FTP, SSH, Telnet, and RTSP.

The value is what organizations forgot to remove. Outdated devices sitting on the open internet show up in Shodan even when the owner stops thinking about them, including traffic-light controls and SCADA systems. Those poorly-defended, high-impact targets are what you want to find early. Shodan also offers an API, so it plugs into other red team tools rather than living only in a browser.

> **Operator takeaway:** Shodan shows a target's front door without you knocking. Read the banners for outdated services and forgotten devices before planning active recon.

______

## SpiderFoot

**SpiderFoot** automates OSINT, querying many services in one run to build a picture of a target:

| Tool | What it is | Good for |
|------|-----------|----------|
| **Shodan** | internet-wide banner index | exposed and forgotten services |
| **SpiderFoot** | automation across many sources | correlating IPs, domains, emails, and people |

Three things make SpiderFoot flexible:

- **Modules.** You switch modules on or off, so you control what gets queried and how loud the collection is.
- **API keys.** Add your own keys to reach paid sources through the same interface.
- **Seed types.** It starts from an IP, domain, hostname, ASN, email address, phone number, or human name.

It pulls from sources like Shodan, Whois, and Have I Been Pwned. Feed it a domain and it fans out. Feed it an email and it correlates back to accounts and breaches.

The two tools work together. SpiderFoot casts wide, then you read the raw Shodan banners for the targets worth a closer look.

______

## More Tools and the Framework

Beyond the core set, a few tools cover the gaps:

| Tool | Purpose |
|------|---------|
| **Maltego** | graph relationships between people, domains, and entities |
| **Metagoofil** | extract metadata from documents |
| **BuiltWith** | profile a website's technology stack |
| **Recon-ng** | a modular reconnaissance framework |
| **Mitaka** | browser lookups for IPs, domains, and hashes |
| **Epieos** | de-anonymize an email across services |
| **PimEyes** | reverse image search for a face |
| **`theHarvester`** | harvest emails and subdomains |

For structure, `osintframework.com` lists methods and tools by category. Use it as a map when you do not know which tool fits the question you are asking.

______

## DNS and Subdomain Enumeration

DNS is free, public data, and it expands the attack surface fast:

- Query the record types, A, MX, NS, and TXT, for the domain.
- Enumerate subdomains with tools like `amass` or `sublist3r`, which pull from search engines, DNS, and certificate logs.
- A misconfigured DNS server still holds a full zone, and an `AXFR` zone transfer copies every host at once.

Every subdomain you find names another host, another login portal, another forgotten box. A domain with five registered hosts often has one hundred real attack surfaces.

______

## Certificate Transparency

Every TLS certificate issued for a domain is logged in the public certificate-transparency logs. `crt.sh` searches those logs, so you pull a list of subdomains straight from the certificates with no scanning at all. It fills in the hosts DNS enumeration missed, and it never touches the customer.

______

## Email and People Harvesting

People are the weakest link, so names and addresses feed the phishing phase:

- `theHarvester` pulls emails and subdomains from search engines and public services.
- LinkedIn and similar profiles map the org chart and job titles.
- Breach data, via Have I Been Pwned, shows which accounts already leaked, a direct prompt for password reuse.
- Reverse image search finds where a person's photo appears, connecting profiles across platforms.

An employee email list plus one known leaked password is frequently the beginning of an initial-access campaign.

______

## Code and Forums

Source and support material leak credentials and internal names:

- GitHub and GitLab code search find repositories and commits mentioning the target.
- Paste sites and support forums carry error messages, machine names, and software versions employees posted.

Search these for the target's name, domain, and product names. What an employee pasted into a forum in a hurry is often the exact detail which names a host or a secret.

______

## Geospatial Intelligence

Physical movement is public data too, and it matters when the objective involves a person or a site:

- **ADS-B** transponders broadcast aircraft positions, so flight paths expose logistics and travel.
- **AIS** transponders broadcast ship positions, revealing supply chains and ship-to-ship transfers.
- Satellite imagery and public maps corroborate ground activity and infrastructure.

GEOINT turns these feeds into answers about where things are and where they move, a different lens from the network-level picture the rest of the module builds.

______

## Limits and Risks

OSINT has sharp limits, and a false finding is worse than no finding:

- **Privacy.** Collection edges toward sensitive personal data.
- **Misinformation.** A source is wrong, outdated, or planted.
- **Legal.** Scraping and illicit data sit outside the lines.
- **Bias.** You only read the sources you found, not the whole picture.

Verify across independent sources, note what the evidence supports, and treat anything unverified as a lead, not a fact.

______

## Build Your Target List

For a target domain, decide which tool answers each need:

1. What does the company own, IP-wise?
2. Which forgotten devices still face the internet?
3. Which subdomains exist beyond the obvious few?
4. Which emails and leaked accounts feed the phishing list?

Answer from memory first. The explanations are in the Answer Key at the end.

______

## Why Collection Discipline Matters

Public data reduces contact with the target, but collection still leaves search, API, and account records. Older OSINT practice treated screenshots as proof, while modern work records source, time, query, confidence, and corroboration. Passive collection and a fictional domain provide the same verification exercise without targeting a real person. **Stop at the boundary set by law and the engagement scope.**

______

## Common Mistakes

- Skipping the Whois ownership check and scanning a third-party block.
- Using search operators one at a time instead of stacking them.
- Treating Shodan banners as optional before planning recon.
- Ignoring subdomains and certificate logs, and missing most of the surface.
- Querying from your real machine or a personal account, and tipping the target.
- Firing at an address which ownership did not clearly resolve to the customer.

______

## Self-Check

1. Name three Google operators and each use.
2. Why check ownership through Whois before scanning?
3. What does Shodan index which Google does not?
4. How do SpiderFoot and Shodan complement each other?
5. What does a certificate-transparency log reveal?
6. Why does subdomain enumeration expand the attack surface?
7. What separates passive from active collection, and why stay passive?
8. What turns raw OSINF into actionable OSINT?

______

## Answer Key

**Self-Check**

1. **`site:` limits to a domain, `inurl:` matches URLs, `filetype:` matches extensions.** Each narrows results toward the pages you want.
2. **Ownership protects scope.** A Whois check stops you firing at a third-party block.
3. **Service banners.** Shodan indexes what a machine says when you connect, not page content.
4. **SpiderFoot correlates across sources, then you read the right Shodan banners.** One casts wide, the other confirms detail.
5. **Every subdomain which ever held a certificate.** The public logs list each TLS certificate, so the hosts surface with no scanning.
6. **Each subdomain names another host.** Five registered hosts often become one hundred real attack surfaces.
7. **Passive reads what others already collected, active touches the target.** Staying passive keeps you unseen.
8. **Verification and analysis.** OSINF becomes OSINT when the raw data is cross-checked and turned into a finding.

**Exercise**

1. **Whois and ARIN** name the owner of the address space.
2. **Shodan** lists the exposed, forgotten devices.
3. **DNS enumeration and `crt.sh`** surface the subdomains.
4. **`theHarvester` and breach data** build the phishing list.

______

## Next Steps

OSINT fills your target list quietly. Next, the moment you start touching infrastructure: active reconnaissance and scanning.

**[→ Module 9: Active Reconnaissance and Scanning](/red-team-course/active-reconnaissance-and-scanning/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
