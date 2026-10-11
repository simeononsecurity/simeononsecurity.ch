---
title: "Secure CI/CD and Software Supply Chains Course"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Build a safer release path with dependency review, SBOMs, limited pipeline permissions, Scorecard, SLSA provenance, attestations, and release verification."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["secure CI/CD course", "software supply chain", "SBOM", "SLSA provenance", "artifact attestation", "OpenSSF Scorecard"]
cover: "/img/cover/secure-cicd-course.webp"
coverAlt: "A source repository, build runner, artifact, and verification gate connected in a release workflow"
coverCaption: ""
---

**Build a release process you can inspect and verify.** This course follows one fictional calculator release from a dependency change to a consumer decision. You will record what changed, narrow the build's authority, generate a component inventory, inspect provenance, and reject a tampered release.

## Audience and Prerequisites

**Audience:** Developers, release engineers, and security staff who maintain repositories or review packages. The guided local path needs Python 3.10 or later and a terminal. Git and a GitHub account are optional. The hosted path needs a disposable repository where you control Actions settings.

**Time:** Four to six hours for the lessons, one hour for the lab, and two hours for the capstone. The local tampering exercise has no cloud cost. Do not use production credentials or releases.

## Learning Outcomes

After the course, you will:

- **Review a dependency change** and document its direct and transitive effects.
- **Inspect a sample SBOM**, then generate one from your own project with Syft if you take the optional tool path.
- **Limit pipeline permissions** and separate untrusted pull request work from release work.
- **Interpret a Scorecard finding** and make a review decision.
- **Read SLSA provenance fields** and compare an artifact with an expected source and builder. The hosted path adds signed attestation verification.
- **Reject a changed release** in a controlled local investigation.

## Lesson Order

| Stage | Page | Practical skill |
|---|---|---|
| **1** | [Review Dependencies and Build an SBOM](/articles/secure-cicd-dependencies-sbom/) | Create a dependency decision record and component inventory |
| **2** | [Limit Pipeline Authority and Use Scorecard](/articles/secure-cicd-pipeline-scorecard/) | Review token scope and record a prioritized Scorecard finding |
| **3** | [Verify Provenance and Attestations](/articles/secure-cicd-provenance-attestations/) | Match artifact digest, source, and workflow to a release policy |
| **4** | [Tampered Release Lab](/articles/secure-cicd-tampered-release-lab/) | Run a local rejection test and explain its trust boundary |
| **5** | [Knowledge Check](/articles/secure-cicd-quiz/) and [answer key](/articles/secure-cicd-quiz-answer-key/) | Answer scenario questions and correct mistakes |
| **6** | [Release Gate Capstone](/articles/secure-cicd-capstone/) and [reference packet](/articles/secure-cicd-capstone-answer-key/) | Produce a release decision packet and test a failure path |

**Complete the pages in order.** Lessons 1 through 3 build the review method. The lab then shows a concrete failure. The capstone asks you to apply the method to a fresh release decision.

## What You Will Produce

**Keep one release packet** with a dependency review, SBOM component, permissions table, Scorecard finding, expected provenance identity, artifact digest, lab result, and release decision. The lessons and [lab archive](/downloads/secure-cicd-lab.zip) supply the local examples and evidence. Its Scorecard and provenance files are clearly labeled teaching fixtures, not live tool results. A passing checksum alone is an integrity check. Publisher identity needs a separate signed attestation check.

## Safe Practice Paths

**Local path:** Download the [lab archive](/downloads/secure-cicd-lab.zip), extract it, and use Python to inspect the fictional dependency change, SBOM, Scorecard result, provenance statement, policy, and release files. All local pass criteria use these fixtures. Record “not run” for Syft, GitHub Actions, and signed attestation checks you did not execute.

**Hosted path:** Use a disposable GitHub repository. Enable Actions, run only the example workflows after reviewing every action reference, then delete the repository and any test artifact when done. GitHub's [secure use guidance](https://docs.github.com/en/actions/reference/security/secure-use) explains why workflow code and tokens need careful review.

**Start with [dependency review and SBOMs](/articles/secure-cicd-dependencies-sbom/)**. Return to [Courses and Playbooks](/courses-and-playbooks/) for other paths.
