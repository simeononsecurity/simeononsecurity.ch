---
title: "CompTIA CySA+ Course"
date: 2025-01-01
toc: true
draft: false
description: "A CompTIA CySA+ CS0-004 topic guide for security operations, vulnerability management, incident response, and reporting. Use the official objectives to check exam coverage."
genre: ["CompTIA CySA+ Course", "Cybersecurity Analyst", "Security Operations", "Vulnerability Management", "Incident Response", "CompTIA Certification", "SIEM", "Threat Intelligence", "Threat Hunting", "Security Analysis"]
tags: ["CompTIA CySA+", "CS0-004", "cybersecurity analyst", "security operations", "vulnerability management", "incident response", "threat intelligence", "threat hunting", "SIEM", "log analysis", "digital forensics", "reporting", "compliance", "CompTIA certification"]
cover: "/img/cover/comptia-cysa-plus-security-operations-center-illustration.webp"
coverAlt: "An illustration of a modern Security Operations Center with cybersecurity analysts working at a central workstation surrounded by multiple screens showing data analytics and threat intelligence."
coverCaption: "Master CompTIA CySA+ and Excel as a Cybersecurity Analyst"
---

The **CompTIA CySA+** (CS0-004) certification validates the skills of intermediate-level cybersecurity analysts working in **security operations**, **threat intelligence**, and **incident response**. *CompTIA Security+ is a recommended prerequisite before starting this course.*

**Use the current CS0-004 objectives as your checklist.** The four lessons introduce the domains and selected tasks. The exam objectives include more detailed tools, formats, AI use, scanning methods, incident artifacts, and reporting duties. Record each objective as practiced, needs review, or not covered before scheduling the exam.

## Resources

- [Tips for Passing CompTIA Exams](/articles/tips-and-tricks-for-passing-comptia-exams/)
- [CompTIA CySA+ Practice Test](/cysa-plus-practice-test/) - Test your readiness
- [Official CS0-004 Exam Objectives](https://lecbyo.files.cmp.optimizely.com/download/68b1eae88e5011f08868a275d699e612)
- [Cybersecurity Career Playbook](/cyber-security-career-playbook-start/)
- [CompTIA Security+ Course](/security-plus-start/) - Recommended prerequisite
- [Additional Learning Resources](/recommendations/learning_resources/)

-----

## Domain 1: Security Operations (34%)

### [Security Operations and Threat Intelligence](/cysa-plus/security-operations/)

- Understand the role of a **Security Operations Center (SOC)** and analyst responsibilities
- Apply **threat intelligence** concepts including indicators of compromise (IoCs) and threat feeds
- Differentiate between **tactical**, **operational**, and **strategic** threat intelligence
- Use **threat modeling** frameworks such as **MITRE ATT&CK** and **Diamond Model**
- Identify threat actor types, motives, and **TTPs** (tactics, techniques, and procedures)
- Apply the **cyber kill chain** model to map adversary behavior
- Perform **log analysis** from endpoints, network devices, and cloud platforms
- Correlate events across multiple log sources to identify malicious activity
- Use **SIEM** tools to aggregate, normalize, and query security event data
- Write and tune **SIEM alerts** to reduce false positives and improve detection fidelity
- Perform **threat hunting** by forming hypotheses and searching telemetry proactively
- Identify **anomalous behaviors** using behavioral analytics and baseline deviations
- Apply **network traffic analysis** using tools like **Wireshark** and **Zeek**
- Interpret **NetFlow** and packet captures to identify suspicious communications
- Analyze **endpoint detection and response (EDR)** data for signs of compromise
- Review **firewall**, **IDS/IPS**, **DNS**, and **proxy logs** for security-relevant events
- Apply knowledge of **scripting and automation** to support repetitive SOC tasks
- Understand **cloud security monitoring** concepts including cloud-native logging services
- Assess AI-assisted log analysis for false claims, prompt injection, and sensitive-data exposure before using results in an incident decision
- Implement threat intelligence sharing using **STIX** and **TAXII** protocols

-----

## Domain 2: Vulnerability Management (26%)

### [Vulnerability Management and Scanning](/cysa-plus/vulnerability-management/)

- Implement a **vulnerability management program** lifecycle from discovery to remediation
- Configure and execute **vulnerability scans** using tools such as **Nessus** and **Qualys**
- Differentiate between **authenticated** and **unauthenticated** scans and their outputs
- Understand the impact of **scan scope**, **scheduling**, and **credentialed access**
- Analyze **vulnerability scan results** and identify true positives versus false positives
- Interpret **Common Vulnerabilities and Exposures (CVE)** identifiers and advisories
- Apply **Common Vulnerability Scoring System (CVSS)** scores to assess severity
- Use the **Common Weakness Enumeration (CWE)** and **OWASP Top 10** as reference frameworks
- Perform **remediation prioritization** based on CVSS, asset criticality, and exploitability
- Distinguish between **patching**, **configuration changes**, **compensating controls**, and **acceptance**
- Track remediation status and verify fixes through **validation scanning**
- Apply vulnerability management concepts to **cloud**, **mobile**, and **OT/ICS** environments
- Understand **attack surface management** and the importance of continuous asset inventory
- Use **threat intelligence** to contextualize vulnerabilities with known active exploits
- Recognize **zero-day** vulnerabilities and appropriate organizational responses
- Assess vulnerabilities in **web applications** including **SQL injection**, **XSS**, and **CSRF**
- Perform **software composition analysis (SCA)** to identify vulnerable dependencies
- Apply **secure configuration baselines** using **CIS Benchmarks** and **DISA STIGs**

-----

## Domain 3: Incident Response and Management (24%)

### [Incident Response and Digital Forensics](/cysa-plus/incident-response-management/)

- Apply the **incident response lifecycle**: preparation, detection, containment, eradication, recovery, and lessons learned
- Follow **incident response plans (IRPs)** and **playbooks** for common attack scenarios
- Classify incidents by **severity**, **category**, and **impact** to guide prioritization
- Perform **triage** to determine scope and whether an event qualifies as an incident
- Execute **containment strategies** including network isolation and account disablement
- Follow **chain of custody** procedures when collecting and handling digital evidence
- Perform **digital forensics** tasks including disk imaging, memory acquisition, and file analysis
- Use forensic tools such as **Autopsy**, **FTK**, **Volatility**, and **dd**
- Analyze **memory artifacts** to identify injected code, running processes, and network connections
- Perform **log correlation** during an active incident to establish a timeline of events
- Conduct **root cause analysis (RCA)** to identify the initial attack vector
- Apply **malware analysis** techniques including static and dynamic analysis
- Identify **persistence mechanisms** such as registry run keys, scheduled tasks, and cron jobs
- Perform **eradication** steps including malware removal and rebuilding compromised systems
- Execute **recovery procedures** including restoration from known-good backups
- Coordinate with **legal**, **HR**, and **executive stakeholders** during incident response
- Apply knowledge of **threat hunting** to identify lateral movement post-compromise
- Understand **regulatory and legal obligations** for breach notification and evidence preservation
- Conduct **post-incident reviews** and document lessons learned to improve future response

-----

## Domain 4: Reporting and Communication (16%)

### [Reporting, Communication, and Compliance](/cysa-plus/reporting-and-communication/)

- Create **vulnerability assessment reports** tailored for technical and executive audiences
- Document **findings**, **risk ratings**, and **remediation recommendations** clearly
- Track **vulnerability metrics** over time including mean time to remediate (MTTR) and patch compliance rates
- Build and maintain **dashboards** to communicate security posture to stakeholders
- Communicate **incident findings** through structured reports and executive briefings
- Apply **risk scoring** frameworks to prioritize findings in written reports
- Recommend **security controls** aligned to frameworks such as **NIST CSF**, **ISO 27001**, and **CIS Controls**
- Understand **compliance requirements** including **PCI DSS**, **HIPAA**, **SOC 2**, and **GDPR**
- Map security findings to **control frameworks** to support audit and compliance activities
- Produce **after-action reports (AARs)** and incorporate findings into security program improvements
- Differentiate between **quantitative** and **qualitative** risk analysis in reporting contexts
- Apply **inhibitors to remediation** analysis including resource constraints and business risk acceptance
- Communicate **remediation timelines** and escalate unresolved critical vulnerabilities appropriately
- Support **third-party risk assessments** by producing documentation of organizational controls
- Understand the role of **KPIs** and **KRIs** in measuring the effectiveness of security operations

-----

Work through all four lessons, complete a lab for each domain, and compare your evidence against the [official CS0-004 objectives](https://lecbyo.files.cmp.optimizely.com/download/68b1eae88e5011f08868a275d699e612). Use the [CySA+ practice test](/cysa-plus-practice-test/) as one review tool, not as proof of work readiness. For other learning paths, see [Courses and Playbooks](/courses-and-playbooks/).
