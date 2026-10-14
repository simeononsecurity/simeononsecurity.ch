---
title: "Secure CI/CD Knowledge Check"
date: 2026-10-10
lastmod: 2026-10-14
toc: true
draft: false
description: "Test dependency, SBOM, pipeline, Scorecard, provenance, attestation, and tampered-release decisions before viewing the separate answer key."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["secure CI/CD quiz", "SBOM quiz", "SLSA quiz", "software supply chain assessment"]
cover: "/img/cover/secure-cicd-quiz.webp"
coverAlt: "A learner reviews a CI/CD security checklist beside pipeline and artifact symbols."
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**Answer all ten questions before opening the separate answer key.** Write one sentence explaining each choice. Score at least eight on a closed-book attempt and correct every miss before the capstone. Retake the full quiz after review if your first score is lower. This is a skills check, not certification prep.

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

## Review and Continue

**After answering, open the [answer key](/secure-cicd-course/07-quiz-answer-key/).** For every missed question, link the relevant lesson section in your packet and rewrite the rule in your own words. Reanswer without looking at the key. Use the [SLSA build track](https://slsa.dev/spec/v1.2/tracks) and [GitHub's secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) for questions 5 and 9.

**Next:** [Complete the release gate capstone](/secure-cicd-course/06-capstone/).
