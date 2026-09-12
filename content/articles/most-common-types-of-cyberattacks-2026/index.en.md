---
title: "The Most Common Types of Cyberattacks and How Defenders Catch Them"
date: 2026-09-11
lastmod: 2026-09-11
toc: true
draft: false
description: "A practical tour of the most common cyberattack types, the evidence each one leaves behind in logs and telemetry, and how to practice detecting them in a home security lab."
genre: ["Cybersecurity", "Threat Detection", "Blue Team", "Security Operations", "Career Development"]
tags: ["cyberattack types", "malware", "ransomware", "phishing", "spear phishing", "social engineering", "spoofing", "identity-based attacks", "credential stuffing", "password spraying", "SQL injection", "cross-site scripting", "supply chain attack", "insider threat", "DNS tunneling", "IoT attacks", "AI-powered attacks", "denial of service", "detection engineering", "SOC analyst", "blue team", "home lab", "log analysis", "incident response", "MITRE ATT&CK", "cybersecurity career", "threat hunting", "security operations center", "telemetry", "alert triage"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "A digital illustration featuring colorful abstract icons symbolizing various cyberattack types like ransomware, phishing, and denial of service against a dark background."
coverCaption: ""
---

An **attack type** is a category of technique, not a single tool. Ransomware, phishing, and credential stuffing each name a method an adversary repeats against many targets with minor variations. Learning the categories gives you a mental index for the alerts you will meet on a security team.

*Individual malware families appear and disappear within months. The attack categories below have stayed stable for years, and each one leaves a recognizable trail in endpoint, identity, network, or email telemetry.*

<!--more-->

## Key Takeaways

- **Learn the pattern, not the payload.** Attack categories change far slower than individual tools.
- **Every category leaves evidence.** The detection work starts with knowing which telemetry records the activity.
- **Reproduce an attack to understand it.** A home lab turns an abstract category into a recorded observation.
- **Write up what you found.** A short investigation note proves the work and teaches you the evidence.

## The Attack Types at a Glance

The table below lists the categories security teams meet most often. Each later section describes the category, its common variants, and the data a defender reviews to find it.

| Attack type | What it does |
|---|---|
| **Malware** | Runs malicious software such as ransomware, spyware, and trojans |
| **Denial of service** | Floods a service with traffic until legitimate users lose access |
| **Phishing** | Tricks a person into revealing credentials or running a malicious file |
| **Spoofing** | Disguises an attacker as a trusted system, sender, or address |
| **Identity-based attacks** | Abuses stolen or forged credentials to act as a valid user |
| **Code injection** | Inserts malicious code into an application to change its behavior |
| **Supply chain attacks** | Compromises a trusted vendor, library, or update channel |
| **Social engineering** | Manipulates a person into taking an unsafe action |
| **Insider threats** | Misuses access held by a current or former employee |
| **DNS tunneling** | Encodes data inside DNS queries to move it past controls |
| **IoT attacks** | Targets connected devices to pivot, spy, or join a botnet |
| **AI-powered attacks** | Uses machine learning to generate content, impersonate people, or evade filters |

**A note on scope:** these categories overlap. A phishing email often delivers malware, and a successful credential theft often precedes an identity-based attack. Treat the list as a set of lenses rather than rigid boxes.

______

## Malware

**Malware** covers any program built to harm, control, or profit from a system. The term spans ransomware, fileless malware, spyware, adware, trojans, worms, rootkits, keyloggers, and botnets.

| Subtype | Behavior |
|---|---|
| **Ransomware** | Encrypts files and demands payment for the decryption key |
| **Fileless malware** | Runs through built-in system tools and writes little to disk |
| **Spyware** | Collects activity data without the user's knowledge |
| **Trojan** | Poses as legitimate software to gain execution |
| **Worm** | Copies itself across hosts without user action |
| **Rootkit** | Hides inside the operating system to keep persistent control |

**Where the evidence lives:** endpoint detection and response tools, or **EDR**, record process trees, command lines, file writes, and registry changes. Even a fileless attack produces process and script-block telemetry, because the operating system still launches the tools it abuses.

______

## Denial of Service

**A denial-of-service (DoS) attack** floods a target with requests until legitimate users lose access. **A distributed denial-of-service (DDoS) attack** repeats the same idea from many systems at once, which makes the traffic far harder to filter by source address.

| Trait | DoS | DDoS |
|---|---|---|
| **Origin** | One system | Many systems |
| **Blocking difficulty** | Moderate | High, since the sources span many networks |
| **Typical impact** | Lost availability | Lost availability at larger scale |

**Where the evidence lives:** traffic volume against a baseline, connection counts per source, request-rate spikes, and error-rate changes. Availability monitoring often alerts before the security team sees the event.

______

## Phishing

**Phishing** uses email, text messages, phone calls, or social media to push a person toward revealing credentials or running a malicious attachment. The category splits by target and channel.

| Variant | Target and channel |
|---|---|
| **Spear phishing** | A specific person or team, usually by email |
| **Whaling** | Senior or executive staff, often to move money or data |
| **Smishing** | Fraudulent text messages |
| **Vishing** | Fraudulent phone calls or voice messages |

**Where the evidence lives:** mail-gateway logs, URL detonation results, attachment analysis, and user reports. A report from a cautious employee is one of the highest-value signals on this list.

______

## Spoofing

**Spoofing** hides an attacker behind a trusted identity so a target accepts the connection, message, or address. The disguise buys time and defeats checks built around trust.

| Type | What gets faked |
|---|---|
| **Domain spoofing** | A lookalike website or email domain impersonating a real brand |
| **Email spoofing** | The sender address on a message |
| **ARP spoofing** | A local network address, to intercept traffic between two hosts |

**Where the evidence lives:** SPF, DKIM, and DMARC results in mail headers, domain registration age, certificate mismatches, and duplicate address warnings on a local network.

______

## Identity-Based Attacks

**Identity-based attacks** use a valid account rather than a defect in software. The attacker holds a working credential, so the activity sits close to normal use and blends into the background. This category drives a large share of the alerts a **security operations center (SOC)** handles each day.

*If you practice one category in a home lab, choose this one. The signals are rich, the exercises repeat, and the setup stays small.*

| Technique | What happens |
|---|---|
| **Kerberoasting** | Requests a service ticket, then cracks the encrypted password offline |
| **Man-in-the-middle (MITM)** | Sits between two parties to read or alter a session |
| **Pass-the-hash** | Reuses a stolen password hash to open a new session |
| **Golden ticket** | Forges a Kerberos ticket-granting ticket for broad domain access |
| **Silver ticket** | Forges a service ticket for one specific service |
| **Credential harvesting** | Collects usernames and passwords in bulk |
| **Credential stuffing** | Replays one set of credentials across many unrelated sites |
| **Password spraying** | Tries one common password across many accounts |
| **Brute force** | Guesses many passwords against one account |
| **Downgrade** | Forces a connection into a weaker protocol version |

**Where the evidence lives:** sign-in records, failed-authentication counts, token anomalies, impossible-travel flags, and identity risk detections. **Adversary-in-the-middle (AiTM) phishing** belongs here too, because the attacker steals a live session token rather than a password, and the replay from unfamiliar infrastructure trips the identity risk engine.

______

## Code Injection

**Code injection** places attacker-controlled code inside a vulnerable application so the application runs it as part of normal work. The application, not the attacker, carries out the harmful action.

| Type | Target |
|---|---|
| **SQL injection** | A database query built from unvalidated input |
| **Cross-site scripting (XSS)** | A web page which renders attacker script in a visitor's browser |
| **Malvertising** | A legitimate ad slot filled with malicious code |
| **Data poisoning** | A training set for an AI or machine learning model |

**Where the evidence lives:** web application logs, database query records, content security policy reports, and request patterns which differ from normal application use.

______

## Supply Chain Attacks

**A supply chain attack** targets a trusted third party whose product or service reaches many customers. A **software supply chain attack** injects malicious code into an application, library, or update so every user of the product receives it. A **hardware supply chain attack** compromises a physical component before it ships.

*Modern software leans on third-party libraries, so one compromised dependency reaches far past the original vendor.*

**Where the evidence lives:** software composition analysis, build-pipeline records, unexpected outbound connections from a trusted update, and integrity checks on shipped artifacts.

______

## Social Engineering

**Social engineering** uses psychological pressure to move a person toward an unsafe action. The attacker appeals to authority, urgency, fear, money, or trust.

| Technique | Approach |
|---|---|
| **Pretexting** | Invents a believable scenario to gain trust |
| **Business email compromise (BEC)** | Impersonates a trusted colleague to redirect a payment or share data |
| **Disinformation** | Spreads false narratives through social media and bots |
| **Quid pro quo** | Offers a reward in exchange for information or access |
| **Honeytrap** | Builds a false relationship to extract money, data, or access |
| **Tailgating** | Follows an employee through a secured door |

**Where the evidence lives:** email authentication results, unusual payment-change requests, helpdesk records, and physical access logs.

______

## Insider Threats

**An insider threat** is misuse of access by a current or former employee, contractor, or partner. Some insiders act with intent, driven by money or grievance. Others act through negligence, such as leaving credentials in a shared document.

*Negligent insiders appear more often than malicious ones in incident reports, and both call for the same detective control: compare access against a baseline for the role.*

**Where the evidence lives:** data-transfer volume, activity outside normal hours, privilege changes, and bulk downloads from sensitive repositories.

______

## DNS Tunneling

**DNS tunneling** encodes data inside DNS queries and responses. Almost every network permits DNS, so the technique moves data past controls built to inspect web traffic.

*Detection leans on volume and shape. A single host sending thousands of queries to one domain stands apart from a normal baseline, and unusually long subdomains hint at an encoded payload.*

**Where the evidence lives:** DNS query records, query length and volume per host, uncommon record types such as TXT, and lookups to domains registered days earlier.

______

## IoT-Based Attacks

**An IoT-based attack** targets a connected device such as a camera, printer, thermostat, or sensor. Weak default credentials and rare firmware updates make these devices a common foothold. Once compromised, a device joins a botnet, leaks data, or becomes a route into the wider network.

*The 5G rollout adds connected devices at scale, and each new device is another target with a long patch cycle.*

**Where the evidence lives:** device inventory, outbound connection patterns, abnormal data transfer from a device with a fixed role, and firmware version drift across a fleet.

______

## AI-Powered Attacks

**AI-powered attacks** apply machine learning to the attacker's side of the work.

| Technique | Use |
|---|---|
| **Adversarial AI/ML** | Manipulates training data or inputs to mislead a model |
| **Dark AI** | Applies AI and machine learning specifically to exploit vulnerabilities |
| **Deepfake** | Generates realistic fake audio, video, or images |
| **AI-generated social engineering** | Runs convincing chat or voice conversations at scale |

*A deepfake voice call or a fluent phishing chat raises the credibility of an old trick. The underlying technique stays familiar, which is why detection skills built on behavior outlast detection skills tied to one tool.*

**Where the evidence lives:** content provenance signals, out-of-band verification for money or access requests, and behavioral anomalies around identity and payment changes.

______

## Mapping Attacks to Telemetry

Each category feeds a different data source. The table below pairs them, which gives you a starting point for detection work.

| Attack type | Primary telemetry |
|---|---|
| **Malware** | EDR process, file, and registry records |
| **Denial of service** | Network flow and availability monitors |
| **Phishing** | Mail gateway and URL detonation records |
| **Spoofing** | Mail authentication and network address records |
| **Identity-based** | Sign-in and identity protection records |
| **Code injection** | Web application and database query logs |
| **Supply chain** | Build pipeline and dependency inventory |
| **Social engineering** | Mail, helpdesk, and physical access records |
| **Insider threat** | Data access and transfer records |
| **DNS tunneling** | DNS query records |
| **IoT** | Device inventory and outbound flow records |
| **AI-powered** | Identity, payment, and content provenance records |

*Begin detection work with the telemetry column. A useful rule grows from a known data source and a known behavior, not from a tool name.*

______

## Practice Detecting Them in a Lab

A category stays abstract until you watch it happen. A home lab lets you generate the activity, capture the telemetry, and compare the alert against the raw record. The [career video on building a security operations center](https://www.youtube.com/watch?v=s3g8o7Np1_g) shows the full build for gaining job experience before being hired.

{{< youtube id="s3g8o7Np1_g" >}}

Start with the identity category. Create a test user, enable sign-in logging, and run a sequence of failed and successful sign-ins. Then read the sign-in record and write down the fields which separate normal use from the exercise.

**A repeatable exercise:**

1. **Pick one category** from the telemetry table above.
2. **Reproduce a benign version** of the activity against your own test system or account.
3. **Collect the telemetry** the category produces.
4. **Write the detection idea** as a rule, a saved search, or a query.
5. **Test the rule** against the exercise and confirm it fires on the intended behavior.
6. **Record the limits** of the rule, including the activity it misses.

The [Microsoft SOC Home Lab guide](/articles/microsoft-soc-home-lab-2026/) covers the environment build in detail: licensing, network segmentation, log collection, and identity control testing. The [Mad Hat Cyber Range guide](https://madhat.io/pages/cyber-range-guide) expands the same idea into a workshop-grade build with an attack, detect, and defend exercise.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Read the Microsoft SOC Home Lab Guide
{{< /centerbutton >}}

______

## Next Steps

Start with one category and one exercise. Add a second category after you complete and document the first. The goal is depth on a single investigation, not a checklist of tools.

- **[Microsoft SOC Home Lab guide](/articles/microsoft-soc-home-lab-2026/)** builds the environment for these exercises.
- **[Building an IT home lab](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** covers the infrastructure layer underneath a security lab.
- **[IT resume writing tips](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** shows how to present a documented lab as practical experience.
- **[The top five cyber attack vectors and mitigations](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** narrows the list to the vectors seen most often.

**Source material:** the attack categories and their subtypes follow [CrowdStrike's overview of common cyberattacks](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/) by Kurt Baker. Product and reference links point to Microsoft documentation.
