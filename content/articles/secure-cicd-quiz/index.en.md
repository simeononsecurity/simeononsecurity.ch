---
title: "Secure CI/CD Knowledge Check and Answer Key"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Test dependency, SBOM, pipeline, Scorecard, provenance, attestation, and tampered-release decisions with explained answers."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["secure CI/CD quiz", "SBOM quiz", "SLSA quiz", "software supply chain assessment"]
cover: "/img/cover/secure-cicd-course.webp"
coverAlt: "A source repository, build runner, artifact, and verification gate connected in a release workflow"
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**Answer all ten questions before opening the key.** Write one sentence explaining each choice. Eight correct answers and a corrected explanation for every miss prepare you for the capstone. This is a skills check, not certification prep.

## Questions

1. **Dependency change:** A manifest changes one direct package, while the lockfile adds six packages. What else should you review? A. Only the direct package. B. The six transitive additions. C. Only the application source. D. No further input.
2. **Empty review view:** GitHub shows no dependency diff. What is the best next step? A. Approve. B. Disable the dependency graph. C. Check feature availability and inspect the manifest and lockfile. D. Delete the lockfile.
3. **SBOM scope:** Syft scans a source directory. What does the resulting SBOM establish? A. Every runtime component. B. Components the scanner found in that source target. C. Publisher identity. D. No vulnerabilities.
4. **Pull request token:** A test job only needs checkout and tests. Which permission fits? A. `contents: read`. B. `contents: write`. C. `administration: write`. D. All permissions.
5. **Workflow boundary:** Why keep untrusted pull request code out of a privileged release job? A. It improves formatting. B. The code may act with release authority. C. It reduces log size. D. It speeds the build.
6. **Scorecard:** A check returns `?`. What should you record? A. Zero risk. B. A pass. C. Unavailable evidence and a manual review need. D. A release approval.
7. **Digest:** A received file matches a digest copied from the same compromised server. What remains unproven? A. Byte equality with that digest. B. File size. C. Independent publisher trust. D. Hash algorithm name.
8. **Attestation:** A valid attestation names a different repository than policy allows. What is the decision? A. Approve. B. Reject or hold. C. Ignore the repository. D. Rewrite the attestation.
9. **SLSA:** Does an attestation alone prove a build meets a SLSA level? A. Yes. B. Only for private repositories. C. Only if the SBOM exists. D. No, review all level requirements.
10. **Lab:** The tampered file produces a digest mismatch. What should the gate do? A. Publish with a note. B. Recompute the trusted digest from the tampered file. C. Reject and retain evidence. D. Ignore the exit code.

## Answer Key

1. **B.** A direct change may pull new transitive code into the build.
2. **C.** An empty interface does not prove the dependency set is safe.
3. **B.** Record the scan target and scanner version. An SBOM is an inventory, not a safety certificate.
4. **A.** Read access supports checkout without granting publication authority.
5. **B.** Untrusted code in a privileged job may use its token or secrets.
6. **C.** Missing evidence needs a separate decision.
7. **C.** The attacker may replace both artifact and checksum.
8. **B.** Signature validity does not override the expected source policy.
9. **D.** SLSA levels include build platform and provenance requirements.
10. **C.** A failed integrity gate should block release and preserve the observed digest.

## Review and Continue

**For every missed question**, link the relevant lesson section in your packet and rewrite the rule in your own words. Reanswer without looking at the key. Use the [SLSA build track](https://slsa.dev/spec/v1.2/tracks) and [GitHub's secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) for questions 5 and 9.

**Next:** [Complete the release gate capstone](/articles/secure-cicd-capstone/).
