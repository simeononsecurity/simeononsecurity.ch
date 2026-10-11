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

**Audience:** Developers, release engineers, and security staff who maintain GitHub repositories or review packages. You need basic Git, a terminal, and Python 3.10 or later. A GitHub account is optional for the local path. The hosted path needs a disposable repository where you control Actions settings.

**Time:** Four to six hours for the lessons, one hour for the lab, and two hours for the capstone. The local tampering exercise has no cloud cost. Do not use production credentials or releases.

## Learning Outcomes

After the course, you will:

- **Review a dependency change** and document its direct and transitive effects.
- **Generate an SBOM** and state what its component list does and does not prove.
- **Limit pipeline permissions** and separate untrusted pull request work from release work.
- **Interpret Scorecard results** as evidence for a review decision.
- **Read SLSA provenance** and verify an artifact against an expected source and builder.
- **Reject a changed release** in a controlled local investigation.

## Lesson Order

| Stage | Page | Practical skill |
|---|---|---|
| **1** | [Review Dependencies and Build an SBOM](/articles/secure-cicd-dependencies-sbom/) | Create a dependency decision record and component inventory |
| **2** | [Limit Pipeline Authority and Use Scorecard](/articles/secure-cicd-pipeline-scorecard/) | Review token scope and record a prioritized Scorecard finding |
| **3** | [Verify Provenance and Attestations](/articles/secure-cicd-provenance-attestations/) | Match artifact digest, source, and workflow to a release policy |
| **4** | [Tampered Release Lab](/articles/secure-cicd-tampered-release-lab/) | Run a local rejection test and explain its trust boundary |
| **5** | [Knowledge Check](/articles/secure-cicd-quiz/) | Answer scenario questions and correct mistakes |
| **6** | [Release Gate Capstone](/articles/secure-cicd-capstone/) | Produce a release approval packet and test a failure path |

**Complete the pages in order.** Lessons 1 through 3 build the review method. The lab then shows a concrete failure. The capstone asks you to apply the method to a fresh release decision.

## What You Will Produce

**Keep one release packet** with a dependency review, SBOM path, permissions table, Scorecard finding, expected provenance identity, artifact digest, lab result, and release decision. Each page names the next field to add. A passing checksum alone is an integrity check. Publisher identity needs a separate trusted provenance check.

## Safe Practice Paths

**Local path:** Use the [downloadable lab directory](/downloads/secure-cicd-lab.zip) and Python. Read the hosted examples without claiming a GitHub run occurred. Record “not run” for hosted controls.

**Hosted path:** Use a disposable GitHub repository. Enable Actions, run only the example workflows after reviewing every action reference, then delete the repository and any test artifact when done. GitHub's [secure use guidance](https://docs.github.com/en/actions/reference/security/secure-use) explains why workflow code and tokens need careful review.

**Start with [dependency review and SBOMs](/articles/secure-cicd-dependencies-sbom/)**. Return to [Courses and Playbooks](/courses-and-playbooks/) for other paths.
