---
title: "SLSA Provenance and GitHub Artifact Attestations"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Read SLSA build provenance, create a GitHub artifact attestation, and verify digest, source, and workflow identity."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["SLSA provenance", "GitHub artifact attestation", "release verification", "gh attestation", "build integrity"]
cover: "/img/cover/secure-cicd-provenance-attestations.webp"
coverAlt: "A release artifact connects to source and build records through an attestation reviewed for identity."
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**Provenance connects an artifact to a build claim.** The [SLSA v1.2 specification](https://slsa.dev/spec/v1.2/) describes a build track with increasing requirements for the trustworthiness of provenance. A consumer still needs a release policy. Verification should check the artifact digest and the expected source repository, ref, and builder identity.

## Key Takeaways

- **Digest:** The exact bytes of a release are part of the claim.
- **Provenance:** A statement names the build process and source materials.
- **Attestation:** A signed statement needs verification against a trusted identity and policy.

## Read the Claim

**Start with `release-policy.json`** in the extracted [lab archive](/downloads/secure-cicd-lab.zip). It names the fictional `example/workshop-calculator` repository, `refs/tags/v1.0.0`, `.github/workflows/release.yml`, an illustrative builder, and SHA-256. Open `sample-provenance.json` and compare its subject, source, ref, workflow, and builder fields with that policy. The sample is unsigned. It teaches field matching, not cryptographic verification. The [SLSA build provenance specification](https://slsa.dev/spec/v1.2/build-provenance) defines the format.

| Field | Reader question |
|---|---|
| **Subject digest** | Do the bytes match the file I received? |
| **Source** | Is the repository and revision the one I approved? |
| **Builder** | Did the allowed build service produce the claim? |
| **Workflow** | Did the approved release path run? |

**Expected result:** Your policy is precise enough to reject a valid attestation from the wrong repository. A valid signature with the wrong source is a policy failure.

**Run the local field check** from the extracted folder:

```bash
python3 inspect_packet.py
python3 inspect_packet.py sample-provenance-wrong-source.json
```

**Expected result:** The first command prints five `MATCH` fields and says `Signature not verified`. The second prints `source: MISMATCH`, `HOLD`, and exits with code 1. On Windows use `py -3`. If a JSON file is missing, extract the archive again. Record the mismatched field and the decision in your packet.

## Create a Hosted Attestation

**For the optional hosted path, use a disposable GitHub repository.** Copy `release-good.txt` to the repository root and save this full workflow as `.github/workflows/release.yml`. Trigger it manually from Actions after checking repository settings. Read GitHub's current [artifact attestation guide](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) for feature availability and syntax:

```yaml
name: Release exercise
on: workflow_dispatch
permissions:
  contents: read
jobs:
  attest:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
      attestations: write
      artifact-metadata: write
    steps:
      - uses: actions/checkout@v7
        with:
          persist-credentials: false
      - run: cp release-good.txt release.txt
      - uses: actions/attest@v4
        with:
          subject-path: release.txt
      - uses: actions/upload-artifact@v7
        with:
          name: workshop-release
          path: release.txt
```

**Expected result:** The Actions run reports an attestation for `release.txt`. This is a training workflow. It does not publish the file or meet a SLSA level. Protect a real release trigger, add project tests, and pin reviewed action commits before production use. If the attestation step reports a permission error, inspect the job permissions and repository feature availability. Do not add broad write access as a shortcut.

## Verify as a Consumer

**For the hosted path, download `workshop-release` from the completed Actions run's Artifacts section.** Extract `release.txt`, then run the official GitHub CLI verification against the repository you used:

```bash
gh attestation verify release.txt -R OWNER/REPOSITORY
```

**Expected result:** The CLI reports a verified attestation and its source identity. Compare the reported source and workflow with your recorded policy. Use the [GitHub verification guide](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) for current flags when your policy also requires a source ref or signer workflow. If verification fails, keep the artifact out of release and save the error and digest in the packet. If no attestation exists, record the control as absent, not passed.

**Do not equate one attestation with a SLSA level.** The [SLSA build track](https://slsa.dev/spec/v1.2/tracks) includes build platform requirements beyond the presence of a statement. Record which requirements your build meets and which need independent evidence.

## Verify Your Work

**Pass this lesson** when your packet includes the supplied policy values, the sample digest, the local five-field comparison, the wrong-source rejection, and a hosted verification result or “not run.” Keep expected examples separate from observed hosted results.

**Next:** [Run the tampered release lab](/secure-cicd-course/04-tampered-release-lab/).
