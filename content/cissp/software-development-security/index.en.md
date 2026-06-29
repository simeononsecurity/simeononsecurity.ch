---
title: "ISC2 CISSP: Software Development Security"
date: 2025-01-01
toc: true
draft: false
description: "Master Software Development Security for the ISC2 CISSP exam. Learn the secure SDLC, maturity models, security controls in development, assessing software security, and secure coding standards."
genre: ["ISC2 CISSP Course", "Software Development Security", "Secure SDLC", "DevSecOps", "Application Security", "ISC2 Certification", "Information Security", "Secure Coding", "CI/CD", "Cybersecurity"]
tags: ["ISC2 CISSP", "CISSP", "software development security", "SDLC", "DevSecOps", "CMM", "SAMM", "secure coding", "API security", "SAST", "DAST", "SCA", "IAST", "CI/CD", "code repositories"]
cover: "/img/cover/isc2-cissp-software-development-security-sdlc.webp"
coverAlt: "An illustration showing the software development lifecycle with stages like planning, coding, testing, and deployment, featuring vibrant colors and security elements against a dark background."
coverCaption: "Master Software Development Security for the CISSP Exam"
---

#### [Click Here to Return To the ISC2 CISSP Course Page](/cissp-start/)

**Software Development Security** is **10%** of the **ISC2 CISSP** exam. This module covers building security into software and judging the safety of code you buy or borrow. *Security is cheapest when designed into the development process from the start, so the exam rewards "shift left" thinking.*

Most breaches trace back to a software flaw someone could have caught earlier. A bug found in design costs little to fix. The same bug found in production costs a hundred times more and may already be exploited. This domain teaches you to find flaws early and keep them out.

## The Secure Software Development Life Cycle

The **SDLC** is the process you follow from idea to retirement. You add security to every phase rather than testing at the end.

| Phase | Security activity |
|-------|-------------------|
| **Requirements** | Define security and privacy requirements |
| **Design** | Threat model the architecture |
| **Development** | Apply secure coding standards |
| **Testing** | Run SAST, DAST, and security tests |
| **Deployment** | Harden the configuration |
| **Maintenance** | Patch and monitor |

You apply this within a development methodology:

- **Waterfall** moves through phases in sequence. It is predictable but slow to change.
- **Agile** delivers small increments in short sprints with constant feedback.
- **DevOps** unites development and operations to ship faster with automation.
- **DevSecOps** builds security into DevOps so every commit is tested for flaws. *Security becomes everyone's job, not a final gate.*
- **Scaled Agile Framework (SAFe)** coordinates Agile across large organizations.

## Maturity Models

You measure how mature your development process is so you can improve it deliberately.

| Model | Focus |
|-------|-------|
| **CMM** (Capability Maturity Model) | Overall process maturity, from initial to optimizing |
| **SAMM** (Software Assurance Maturity Model) | Security practices across the SDLC |

The **CMM** levels run from **Initial** (ad hoc and chaotic) through **Repeatable**, **Defined**, and **Managed**, to **Optimizing** (continuous improvement). You raise maturity one level at a time.

## Security Controls in Development Ecosystems

You secure the tools and environment, not just the code.

- **Programming languages** carry different risks. Memory-unsafe languages like C allow buffer overflows, while managed languages reduce that class of bug.
- **Libraries and dependencies** can introduce vulnerabilities you did not write. You track and update them.
- **CI/CD pipelines** automate build, test, and deploy. You secure the pipeline because it has access to everything.
- **Code repositories** hold your source. You protect them with access control, branch protection, and secret scanning, as compared in [best code repositories](/articles/best-code-repositories-comparison/).
- **Configuration management** keeps environments consistent and auditable.

```bash
# Scan project dependencies for known vulnerabilities
npm audit

# Prevent secrets from entering a repository with a pre-commit scan
git secrets --scan
```

## Assessing Software Security Effectiveness

You test software with several methods because each finds different flaws.

| Method | What it does | When it runs |
|--------|--------------|--------------|
| **SAST** | Static analysis of source code | Before running, in the pipeline |
| **DAST** | Dynamic testing of a running app | At runtime, black-box |
| **SCA** | Software composition analysis of dependencies | Continuously |
| **IAST** | Interactive analysis from inside a running app | During testing |

**SAST** finds flaws early but produces false positives. **DAST** finds runtime issues but only in code paths it exercises. **SCA** catches vulnerable third-party components, the source of many real-world breaches. You combine them for full coverage.

## Assessing Acquired Software

Most organizations buy more software than they build, so you assess what you acquire.

| Source | Risk to assess |
|--------|----------------|
| **COTS** (Commercial off-the-shelf) | Vendor patching, hidden flaws, support lifecycle |
| **Open source** | Maintenance health, license terms, known CVEs |
| **Third-party** | Contractual security obligations and audits |
| **Managed/cloud services** | Shared responsibility and provider controls |

You demand a **software bill of materials (SBOM)** so you know every component in what you run, tying back to supply chain risk in [Security and Risk Management](/cissp/security-and-risk-management/).

## Secure Coding Guidelines

You apply standards so developers avoid common mistakes.

- **Input validation** rejects malformed input that drives injection attacks.
- **Output encoding** prevents cross-site scripting.
- **Parameterized queries** stop SQL injection.
- **Error handling** fails securely without leaking internal detail.
- **API security** authenticates every call, enforces rate limits, and validates all input, since APIs expose business logic directly.

The **OWASP Top 10** lists the most critical web application risks and is the baseline every developer should know. Pair secure coding with the testing from [Security Assessment and Testing](/cissp/security-assessment-and-testing/) to confirm the controls hold.

## Next Steps

You have now covered all eight CISSP domains. Test your readiness with the [ISC2 CISSP Practice Test](/cissp-practice-test/), review weak areas across [Security and Risk Management](/cissp/security-and-risk-management/) through [Security Operations](/cissp/security-operations/), and return to the [ISC2 CISSP Course](/cissp-start/). For more certification paths, visit [Courses and Playbooks](/courses-and-playbooks/) and read [tips for passing certification exams](/articles/tips-and-tricks-for-passing-comptia-exams/).
