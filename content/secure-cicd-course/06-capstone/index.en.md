---
title: "Secure Release Gate Capstone"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Build and defend a release decision with dependency evidence, SBOM scope, pipeline permissions, provenance policy, and a tampering test."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["secure release capstone", "CI/CD release gate", "SBOM", "artifact verification", "supply chain security"]
cover: "/img/cover/secure-cicd-capstone.webp"
coverAlt: "Dependency, build, test, and attestation evidence converge at a release gate for review."
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**Decide whether the fictional workshop calculator is ready to release.** Build a packet that another maintainer can check without asking you what you meant. Extract a fresh copy of the [local lab](/downloads/secure-cicd-lab.zip) and enter its folder. Every local evidence source is included. Compare your packet with the separate [reference packet](/secure-cicd-course/08-capstone-answer-key/) after finishing. Plan two hours.

## Required Packet

**Create a Markdown or text file** outside the site repository. Use these headings in order:

1. **Release identity:** artifact name, version, expected source repository, protected ref, and workflow.
2. **Dependency review:** use `sample-dependency-change.json` to name the direct update, transitive addition, unassessed advisory, owner, and hold decision.
3. **SBOM record:** use `sample-sbom.cdx.json` to name the supplied inventory, one component, and its limits. Add a Syft scan only if you ran one.
4. **Pipeline authority:** test and release job permissions, untrusted input boundary, and secrets access.
5. **Scorecard review:** use the illustrative `sample-scorecard.json` check, score, reason, correction, and verification plan. Label a live run separately.
6. **Provenance policy:** use `release-policy.json` and `sample-provenance.json` to compare digest, source, builder, ref, and workflow. Include a hosted signed attestation result or “not run.”
7. **Tampering test:** commands, outputs, exit codes, changed line, and decision.
8. **Final decision:** approve, hold, or reject with the evidence needed to change the decision.

**Keep expected and observed results separate.** If you lack GitHub access, complete the local lab and label hosted steps “not run.” Do not invent a successful attestation or Scorecard score.

**Run the local evidence check** from the extracted folder. Save both outputs and exit codes:

```bash
python3 inspect_packet.py
python3 inspect_packet.py sample-provenance-wrong-source.json
```

**Expected result:** The first run matches five policy fields but says the signature was not verified. The second run holds for a wrong source. On Windows, use `py -3` and `$LASTEXITCODE`. If your files differ from the fixture, extract a fresh archive.

## Run the Failure Path

**First verify the good release, then the tampered release.** Use the two commands in the [lab lesson](/secure-cicd-course/04-tampered-release-lab/). The expected decisions are approve for the good bytes only after all other policy checks pass, and reject for the tampered bytes. The lab's checksum alone cannot approve publisher identity.

**Add a wrong-source case.** Assume a cryptographically valid attestation names another repository. Record “hold” or “reject” and name the mismatched field. This checks policy, not cryptography.

## Assess Your Packet

| Criterion | Pass condition |
|---|---|
| **Inputs** | The supplied dependency change and SBOM scope are specific |
| **Authority** | Test job has read access, release writes are isolated |
| **Provenance** | Supplied statement fields match policy, wrong-source case is rejected, and signature status says not verified |
| **Failure test** | Tampered bytes fail and block release |
| **Evidence** | Observed, expected, and not-run results are labeled |
| **Decision** | A second reviewer can reproduce the conclusion |

**Pass all six criteria** for the local fixture path before treating the packet as complete. A correct local decision is **hold** for release because the source and Scorecard evidence are illustrative and no signature was verified. Ask a peer to reproduce the local checks from a fresh copy. If a check differs, save the command, environment, output, and corrected decision. Keep optional Syft, Scorecard CLI, GitHub Actions, and signed attestation controls “not run” unless you exercised them.

## Reference Decision

**The supplied tampered release fails.** Its added telemetry line changes the digest, so the local integrity gate rejects it. The known-good file passes only the lab digest check. The sample provenance is unsigned. A real release still needs actual dependency, permission, provenance, and policy evidence. Review the [GitHub attestation guide](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) before claiming an authenticated release.

**Return to the [course outline](/secure-cicd-course-start/)** and keep the packet as a template for your next release review.
