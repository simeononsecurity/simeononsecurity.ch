---
title: "Secure CI/CD Quiz Answer Key"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Check and explain the ten Secure CI/CD course questions before the release gate capstone."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["secure CI/CD answer key", "software supply chain quiz", "release verification questions"]
cover: "/img/cover/secure-cicd-quiz-answer-key.webp"
coverAlt: "A reviewer compares a completed answer sheet with security controls and flags one conditional result."
coverCaption: ""
---

[Return to the quiz](/secure-cicd-course/05-quiz/)

**Compare your choices with these explanations.** Mark each miss and explain the correction without copying the key. Score at least eight on a closed-book attempt and correct every miss before the capstone.

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

## Record and Repair Your Score

Write `score: X/10` and list every missed question in your course record. At least eight correct on a closed-book attempt plus a corrected explanation for every miss meet the quiz threshold. Retake the full quiz after review if your first score is lower. Use the lesson map to repair a weak area:

| Questions | Review |
|---|---|
| **1 to 3** | [Dependency review and SBOMs](/secure-cicd-course/01-dependencies-sbom/) |
| **4 to 6** | [Pipeline permissions and Scorecard](/secure-cicd-course/02-pipeline-scorecard/) |
| **7 to 9** | [Provenance and attestations](/secure-cicd-course/03-provenance-attestations/) |
| **10** | [Tampered release lab](/secure-cicd-course/04-tampered-release-lab/) |

For each miss, write the unsafe choice, the correct decision, and the evidence needed in a real release. Then answer the missed question again without viewing this key. Record the second answer and link the lesson section used. If the second answer is still wrong, repeat the related lab step or source check before starting the capstone.

## Troubleshooting

- **A score differs from your record:** Recount the ten original choices before using corrected answers.
- **Two options still seem plausible:** State what each option proves, then choose the one matching the question's required evidence.
- **A lab question lacks a result:** Run the local tampered-release fixture again and record the exit code.

## Verify Completion

- [ ] Latest closed-book score is at least eight, with missed question numbers recorded
- [ ] Every miss has a corrected rule and lesson link
- [ ] Missed questions are answered again without the key
- [ ] The latest closed-book attempt scores at least eight, and every miss has been repaired before the capstone

**Next:** [Complete the release gate capstone](/secure-cicd-course/06-capstone/).
