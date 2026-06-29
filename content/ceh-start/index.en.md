---
title: "EC-Council CEH Course: Complete Study Guide for the Certified Ethical Hacker v13 Exam"
date: 2025-01-01
toc: true
draft: false
description: "A comprehensive EC-Council Certified Ethical Hacker (CEH v13) study course covering all 20 modules: ethical hacking methodology, footprinting, scanning, enumeration, system hacking, malware, web attacks, wireless attacks, cloud security, and cryptography."
genre: ["CEH Course", "Certified Ethical Hacker", "Ethical Hacking", "Penetration Testing", "EC-Council Certification", "Network Security", "Web Application Security", "Malware Analysis", "Social Engineering", "Cryptography"]
tags: ["CEH", "CEH v13", "Certified Ethical Hacker", "ethical hacking", "footprinting", "reconnaissance", "scanning", "enumeration", "system hacking", "malware", "social engineering", "denial of service", "session hijacking", "web server hacking", "SQL injection", "wireless hacking", "cloud security", "cryptography", "IoT security", "EC-Council"]
cover: "/img/cover/ec-council-ceh-course-study-guide-illustration.webp"
coverAlt: "A digital illustration of a hacker silhouette analyzing network data against a dark background, with vibrant accents representing cybersecurity tools, networks, and vulnerabilities."
coverCaption: "Master the CEH and Think Like an Attacker"
---

The **EC-Council Certified Ethical Hacker (CEH v13)** teaches you to think and act like an attacker to defend systems more effectively. This course is designed for security professionals, penetration testers, and IT administrators who want a structured path through all 20 CEH exam domains. *Every technique covered in this course must only be applied to systems and networks for which you have explicit written authorization.*

## Resources

- [EC-Council CEH Practice Test](/ceh-practice-test/)
- [Official EC-Council CEH Page](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/)
- [CompTIA Security+ Course](/security-plus-start/) - Recommended foundation
- [CompTIA PenTest+ Course](/pentest-plus-start/) - Related certification
- [Cybersecurity Career Playbook](/cyber-security-career-playbook-start/)
- [Additional Learning Resources](/recommendations/learning_resources/)

-----

## Phase 1: Foundations

### [Module 01: Introduction to Ethical Hacking](/ceh/introduction-to-ethical-hacking/)

- Understand the scope and legal framework of **ethical hacking** and penetration testing
- Learn the **five phases of hacking**: reconnaissance, scanning, gaining access, maintaining access, and covering tracks
- Distinguish between **black-box, white-box, and grey-box** testing engagements
- Review key information security laws, compliance frameworks, and the importance of written authorization
- Explore the **CEH exam objectives** and the mindset required to think like an attacker

### [Module 02: Footprinting and Reconnaissance](/ceh/footprinting-and-reconnaissance/)

- Perform **passive reconnaissance** using open-source intelligence (OSINT) sources and public records
- Use tools such as **Maltego**, **theHarvester**, and **Shodan** to map an organization's external footprint
- Extract DNS records, WHOIS data, and BGP routing information to build a target profile
- Identify email addresses, employee names, and social media presence as attack surface indicators
- Understand **Google dorking** and advanced search operators for targeted information gathering

-----

## Phase 2: Reconnaissance and Scanning

### [Module 03: Scanning Networks](/ceh/scanning-networks/)

- Use **Nmap** to perform host discovery, port scanning, and service version detection
- Understand TCP/IP scanning techniques including **SYN scans, FIN scans, XMAS scans**, and NULL scans
- Perform **OS fingerprinting** and banner grabbing to identify remote systems
- Enumerate open ports and map network topology using tools like **Hping3** and **Zenmap**
- Use scanning results to prioritize targets and plan the next phase of an engagement

### [Module 04: Enumeration](/ceh/enumeration/)

- Extract detailed information from target systems using **NetBIOS**, **SNMP**, and **LDAP** enumeration
- Enumerate **SMB shares**, user accounts, and group memberships on Windows systems
- Use tools such as **enum4linux**, **SNMPwalk**, and **NBTscan** for systematic enumeration
- Perform **DNS zone transfers** and brute-force subdomain enumeration
- Identify service banners, application versions, and default credentials exposed on the network

### [Module 05: Vulnerability Analysis](/ceh/vulnerability-analysis/)

- Use **Nessus**, **OpenVAS**, and **Qualys** to scan for known vulnerabilities in target systems
- Understand the **CVSS scoring system** and how to prioritize vulnerabilities by risk
- Distinguish between **authenticated and unauthenticated** vulnerability scans
- Map discovered vulnerabilities to **CVE entries** and public exploit databases
- Interpret scan reports and translate findings into actionable remediation recommendations

-----

## Phase 3: System Attack Techniques

### [Module 06: System Hacking](/ceh/system-hacking/)

- Follow the **system hacking methodology**: gaining access, escalating privileges, maintaining access, and clearing logs
- Crack passwords using **John the Ripper**, **Hashcat**, and rainbow table attacks
- Use **Metasploit Framework** to exploit known vulnerabilities and gain shell access
- Perform **privilege escalation** on both Windows and Linux systems
- Cover tracks by clearing event logs, modifying timestamps, and using rootkits

### [Module 07: Malware Threats](/ceh/malware-threats/)

- Analyze the behavior of **viruses, worms, Trojans, ransomware**, and spyware
- Understand how **Remote Access Trojans (RATs)** establish persistent backdoors
- Use **static and dynamic analysis** techniques to examine malware samples safely
- Study **keyloggers**, fileless malware, and living-off-the-land attack strategies
- Implement malware countermeasures including endpoint detection, application whitelisting, and sandboxing

### [Module 08: Sniffing](/ceh/sniffing/)

- Capture and analyze network traffic using **Wireshark** and **tcpdump**
- Understand **passive versus active sniffing** and when each applies
- Perform **ARP poisoning** and **MAC flooding** to intercept traffic on switched networks
- Identify credentials and sensitive data transmitted over unencrypted protocols
- Deploy countermeasures such as **dynamic ARP inspection** and encrypted communications

### [Module 09: Social Engineering](/ceh/social-engineering/)

- Recognize common **social engineering attack vectors**: phishing, vishing, smishing, and pretexting
- Conduct **phishing simulations** using frameworks like **GoPhish** to test user awareness
- Understand **impersonation, baiting, tailgating**, and other physical social engineering techniques
- Build security awareness training programs to reduce human-factor risk
- *All social engineering testing requires explicit written scope approval and rules of engagement*

-----

## Phase 4: Network Attack Techniques

### [Module 10: Denial-of-Service](/ceh/denial-of-service/)

- Understand the difference between **DoS and DDoS** attacks and their traffic patterns
- Study volumetric attacks, **protocol attacks**, and application-layer attacks
- Analyze **amplification and reflection** techniques used in large-scale DDoS campaigns
- Use tools such as **LOIC**, **HOIC**, and **hping3** in controlled lab environments
- Implement defenses including **rate limiting, scrubbing centers, and anycast filtering**

### [Module 11: Session Hijacking](/ceh/session-hijacking/)

- Understand **TCP session hijacking** and how attackers exploit sequence number prediction
- Perform **cookie theft** and **session fixation** attacks against web applications
- Use **cross-site scripting (XSS)** to steal session tokens from authenticated users
- Analyze tools such as **Hamster** and **Ferret** for session capture and replay
- Apply countermeasures including **secure cookie flags**, HTTPS enforcement, and token rotation

### [Module 12: Evading IDS, Firewalls, and Honeypots](/ceh/evading-ids-firewalls-honeypots/)

- Understand how **intrusion detection systems (IDS)** and **intrusion prevention systems (IPS)** detect attacks
- Use **packet fragmentation, TTL manipulation**, and protocol obfuscation to evade signature-based detection
- Bypass **firewall rules** using port knocking, tunneling, and allowed-protocol abuse
- Identify **honeypots** and honeynet deployments to avoid triggering deception environments
- Study **Snort rules** and learn how attackers craft traffic to avoid triggering alerts

-----

## Phase 5: Application and Platform Attacks

### [Module 13: Hacking Web Servers](/ceh/hacking-web-servers/)

- Enumerate web server software versions and misconfigurations using **Nikto** and **dirb**
- Exploit **default credentials**, directory traversal, and verbose error messages
- Study **web server attack types**: defacement, DoS, DNS hijacking, and cache poisoning
- Use **Metasploit modules** targeting Apache, IIS, and Nginx vulnerabilities
- Harden web servers through patch management, disabling unnecessary modules, and WAF deployment

### [Module 14: Hacking Web Applications](/ceh/hacking-web-applications/)

- Map web application attack surfaces using **Burp Suite** for intercepting and modifying requests
- Exploit **authentication flaws**, broken access control, and insecure direct object references
- Perform **command injection**, file inclusion (LFI/RFI), and XML external entity (XXE) attacks
- Understand the **OWASP Top 10** and how each category translates to real attack scenarios
- Apply secure development practices and input validation to remediate application vulnerabilities

### [Module 15: SQL Injection](/ceh/sql-injection/)

- Perform **in-band, blind, and out-of-band SQL injection** attacks against vulnerable web applications
- Use **SQLMap** to automate detection and exploitation of SQL injection vulnerabilities
- Extract database schemas, tables, and credentials through **UNION-based and error-based** injection
- Bypass authentication forms using **SQL injection payloads** and comment sequences
- Prevent SQL injection through **parameterized queries**, stored procedures, and input sanitization

### [Module 16: Hacking Wireless Networks](/ceh/hacking-wireless-networks/)

- Perform **wireless reconnaissance** using **Aircrack-ng** and **Kismet** to identify access points
- Execute **WPA2 handshake capture** and offline dictionary attacks against Wi-Fi passwords
- Understand **evil twin attacks**, rogue access points, and **KARMA attacks** against clients
- Analyze **Bluetooth vulnerabilities** including bluejacking, bluesnarfing, and BlueBorne
- Secure wireless networks with **WPA3**, certificate-based authentication, and rogue AP detection

### [Module 17: Hacking Mobile Platforms](/ceh/hacking-mobile-platforms/)

- Understand the **Android and iOS attack surfaces** including app sandboxing and permission models
- Analyze **malicious apps**, sideloading risks, and insecure data storage on mobile devices
- Use **ADB (Android Debug Bridge)** and tools like **MobSF** for mobile application analysis
- Study **mobile device management (MDM)** bypass techniques and jailbreaking/rooting risks
- Implement mobile security controls including app vetting policies and containerization

### [Module 18: IoT and OT Hacking](/ceh/iot-ot-hacking/)

- Enumerate IoT devices using **Shodan** and identify exposed management interfaces
- Understand **OT and SCADA system architectures** and the consequences of attacks on critical infrastructure
- Exploit **default credentials, insecure firmware**, and unencrypted communications on IoT devices
- Study **Modbus, DNP3**, and other industrial protocols and their security weaknesses
- Apply **network segmentation, firmware hardening**, and OT-specific monitoring as defenses

-----

## Phase 6: Advanced Topics

### [Module 19: Cloud Computing](/ceh/cloud-computing-threats/)

- Understand **IaaS, PaaS, and SaaS** security responsibilities under the shared responsibility model
- Identify common cloud misconfigurations including **open S3 buckets**, exposed APIs, and weak IAM policies
- Use tools such as **ScoutSuite**, **Pacu**, and **CloudSploit** to audit cloud environments
- Study **container security** risks with Docker and Kubernetes including escape vulnerabilities
- Implement **cloud security posture management (CSPM)** and least-privilege access controls

### [Module 20: Cryptography](/ceh/cryptography-and-pki/)

- Understand **symmetric and asymmetric cryptography** and the use cases for each
- Study **PKI components**: certificate authorities, digital certificates, and certificate revocation
- Analyze common **cryptographic attacks** including brute force, birthday attacks, and padding oracle attacks
- Understand **TLS/SSL handshake processes** and how weak cipher suites expose encrypted traffic
- Apply cryptographic best practices including **key management, forward secrecy**, and algorithm selection

-----

This course covers all 20 CEH v13 modules to prepare you for the exam and real-world engagements. When you are ready to test your knowledge, take the [EC-Council CEH Practice Test](/ceh-practice-test/). To explore other certifications and career paths, visit [Courses and Playbooks](/courses-and-playbooks/).
