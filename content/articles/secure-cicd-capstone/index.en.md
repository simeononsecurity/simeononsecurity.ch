---
title: "Secure Release Gate Capstone"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Build and defend a release decision with dependency evidence, SBOM scope, pipeline permissions, provenance policy, and a tampering test."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["secure release capstone", "CI/CD release gate", "SBOM", "artifact verification", "supply chain security"]
cover: "/img/cover/secure-cicd-course.webp"
coverAlt: "A source repository, build runner, artifact, and verification gate connected in a release workflow"
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**Decide whether the fictional workshop calculator is ready to release.** Build a packet that another maintainer can check without asking you what you meant. Use a fresh copy of the [local lab](/downloads/secure-cicd-lab.zip) and the workflow examples from the previous lessons. Plan two hours.

## Required Packet

**Create a Markdown or text file** outside the site repository. Use these headings in order:

1. **Release identity:** artifact name, version, expected source repository, protected ref, and workflow.
2. **Dependency review:** one proposed direct change, its transitive effects, advisory check, owner, and decision. Use a real disposable pull request or label the scenario “illustrative.”
3. **SBOM record:** scan target, scanner and version, output path, one component found, and the inventory's limits.
4. **Pipeline authority:** test and release job permissions, untrusted input boundary, and secrets access.
5. **Scorecard review:** one check, score or “not run,” reason, remediation, and verification plan.
6. **Provenance policy:** expected digest, source, builder, and workflow. Include a hosted attestation result or “not run.”
7. **Tampering test:** commands, outputs, exit codes, changed line, and decision.
8. **Final decision:** approve, hold, or reject with the evidence needed to change the decision.

**Keep expected and observed results separate.** If you lack GitHub access, complete the local lab and label hosted steps “not run.” Do not invent a successful attestation or Scorecard score.

## Run the Failure Path

**First verify the good release, then the tampered release.** Use the two commands in the [lab lesson](/articles/secure-cicd-tampered-release-lab/). The expected decisions are approve for the good bytes only after all other policy checks pass, and reject for the tampered bytes. The lab's checksum alone cannot approve publisher identity.

**Add a wrong-source case.** Assume a cryptographically valid attestation names another repository. Record “hold” or “reject” and name the mismatched field. This checks policy, not cryptography.

## Assess Your Packet

| Criterion | Pass condition |
|---|---|
| **Inputs** | Dependency record and SBOM scope are specific |
| **Authority** | Test job has read access, release writes are isolated |
| **Provenance** | Policy names digest, repository, ref, and builder |
| **Failure test** | Tampered bytes fail and block release |
| **Evidence** | Observed, expected, and not-run results are labeled |
| **Decision** | A second reviewer can reproduce the conclusion |

**Pass all six criteria** before treating the packet as complete. Ask a peer to reproduce the local checks from a fresh copy. If a check differs, save the command, environment, output, and corrected decision. If Syft or GitHub CLI is unavailable, keep those controls “not run” and list the remaining work.

## Reference Decision

**The supplied tampered release fails.** Its added telemetry line changes the digest, so the local integrity gate rejects it. The known-good file passes only the lab digest check. A real release still needs the dependency, permission, provenance, and policy evidence described in the packet. Review the [GitHub attestation guide](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) before claiming an authenticated release.

**Return to the [course outline](/secure-cicd-course-start/)** and keep the packet as a template for your next release review.
