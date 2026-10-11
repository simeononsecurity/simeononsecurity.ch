---
title: "SLSA Provenance and GitHub Artifact Attestations"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Read SLSA build provenance, create a GitHub artifact attestation, and verify digest, source, and workflow identity."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["SLSA provenance", "GitHub artifact attestation", "release verification", "gh attestation", "build integrity"]
cover: "/img/cover/secure-cicd-course.webp"
coverAlt: "A source repository, build runner, artifact, and verification gate connected in a release workflow"
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**Provenance connects an artifact to a build claim.** The [SLSA v1.2 specification](https://slsa.dev/spec/v1.2/) describes a build track with increasing requirements for the trustworthiness of provenance. A consumer still needs a release policy. Verification should check the artifact digest and the expected source repository, ref, and builder identity.

## Key Takeaways

- **Digest:** The exact bytes of a release are part of the claim.
- **Provenance:** A statement names the build process and source materials.
- **Attestation:** A signed statement needs verification against a trusted identity and policy.

## Read the Claim

**Start with a release policy**, not an attestation file. Write the expected repository, protected ref or tag, workflow path, artifact name, and digest algorithm. Then compare the statement with your policy. The [SLSA build provenance specification](https://slsa.dev/spec/v1.2/build-provenance) defines the fields and their meaning.

| Field | Reader question |
|---|---|
| **Subject digest** | Do the bytes match the file I received? |
| **Source** | Is the repository and revision the one I approved? |
| **Builder** | Did the allowed build service produce the claim? |
| **Workflow** | Did the approved release path run? |

**Expected result:** Your policy is precise enough to reject a valid attestation from the wrong repository. A valid signature with the wrong source is a policy failure.

## Create a Hosted Attestation

**Use a disposable GitHub repository** with a protected release workflow. Read GitHub's current [artifact attestation guide](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) for feature availability and syntax. The release job needs `contents: read`, `id-token: write`, and `attestations: write`. Build the file first. Then pass its path to `actions/attest`:

```yaml
permissions:
  contents: read
  id-token: write
  attestations: write
steps:
  - uses: actions/checkout@v6
    with:
      persist-credentials: false
  - run: cp release-good.txt release.txt
  - uses: actions/attest@v4
    with:
      subject-path: release.txt
```

**Expected result:** The release job reports an attestation for `release.txt`. The snippet belongs inside a release job. It is not a complete workflow. Add a protected trigger, project tests, and a reviewed action pin before using the pattern for a real release. If the attestation step reports a permission error, inspect the job permissions and repository feature availability. Do not add broad write access as a shortcut.

## Verify as a Consumer

**Download the release file independently**, then run the official GitHub CLI verification against the expected repository:

```bash
gh attestation verify release.txt -R OWNER/REPOSITORY
```

**Expected result:** The CLI reports a verified attestation and its source identity. Compare the reported source and workflow with your recorded policy. Use the [GitHub verification guide](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) for current flags when your policy also requires a source ref or signer workflow. If verification fails, keep the artifact out of release and save the error and digest in the packet. If no attestation exists, record the control as absent, not passed.

**Do not equate one attestation with a SLSA level.** The [SLSA build track](https://slsa.dev/spec/v1.2/tracks) includes build platform requirements beyond the presence of a statement. Record which requirements your build meets and which need independent evidence.

## Verify Your Work

**Pass this lesson** when your packet includes a release policy with source and workflow identity, a digest, a verification result or “not run,” and a decision for the wrong-source case. Keep expected examples separate from observed hosted results.

**Next:** [Run the tampered release lab](/articles/secure-cicd-tampered-release-lab/).
