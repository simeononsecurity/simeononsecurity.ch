---
title: "Secure Release Gate Reference Packet"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Compare a completed local release decision packet with the Secure CI/CD capstone evidence and decision rules."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["secure release answer key", "release gate reference", "supply chain capstone"]
cover: "/img/cover/secure-cicd-course.webp"
coverAlt: "A source repository, build runner, artifact, and verification gate connected in a release workflow"
coverCaption: ""
---

[Return to the capstone](/articles/secure-cicd-capstone/)

**Use this reference only after writing your own packet.** The names and findings below come from the synthetic local archive. They do not describe an actual GitHub repository or Scorecard run.

## Release Identity

**Artifact:** `release-good.txt`, version `1.0.0`. **Expected source:** `https://github.com/example/workshop-calculator`. **Ref:** `refs/tags/v1.0.0`. **Workflow:** `.github/workflows/release.yml`. **Builder:** `https://build.example.invalid/runner`. These are exercise values from `release-policy.json`.

## Input Decision

**Dependency review:** `workshop-core` changes from `1.0.0` to `1.1.0`, and `workshop-parser 2.0.0` appears as a transitive addition. The advisory state is “not assessed.” Assign a fictional maintainer to confirm why the parser was added and review any real advisory before approving.

**SBOM:** `sample-sbom.cdx.json` is a supplied CycloneDX 1.6 fixture with two library components. `workshop-parser 2.0.0` appears. No Syft version or real scan target exists for this fixture. A real release needs an SBOM generated from the selected artifact or build target.

## Authority and Findings

**Test job:** `contents: read`, no release secret. **Release job:** `contents: read`, `id-token: write`, and `attestations: write` for the attestation exercise. A protected release ref and reviewed action pins remain required for a real release.

**Scorecard:** The sample Pinned-Dependencies score is 3 with a mutable-tag reason. This is illustrative. Review the action's upstream commit, pin the reviewed revision, and rerun a real Scorecard analysis. No live score was observed in the local path.

## Provenance and Tampering

**Policy check:** `inspect_packet.py` reports five matching fields for `sample-provenance.json`. The statement is unsigned, so signature verification is **not run**. The wrong-source fixture reports `source: MISMATCH`, `HOLD`, and exit code 1.

**Integrity check:** `verify_release.py release-good.txt` reports `PASS` and exit code 0. `verify_release.py release-tampered.txt` reports `FAIL: digest mismatch` and exit code 1. The tampered file adds a telemetry URL line. The integrity gate rejects that file.

## Final Decision

**Hold the fictional release.** The local path proves a byte mismatch is rejected and illustrates policy field matching. It does not prove publisher identity or a live repository's controls. To change the decision, obtain real dependency and SBOM evidence, confirm pipeline permissions, generate and verify a signed attestation, and match source and workflow against policy.

**Return to the [course outline](/secure-cicd-course-start/)** when your packet matches these decisions.
