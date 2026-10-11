---
title: "Secure CI/CD Quiz Answer Key"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Check and explain the ten Secure CI/CD course questions before the release gate capstone."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["secure CI/CD answer key", "software supply chain quiz", "release verification questions"]
cover: "/img/cover/secure-cicd-course.webp"
coverAlt: "A source repository, build runner, artifact, and verification gate connected in a release workflow"
coverCaption: ""
---

[Return to the quiz](/articles/secure-cicd-quiz/)

**Compare your choices with these explanations.** Mark each miss and explain the correction without copying the key. Eight correct answers plus corrected misses prepare you for the capstone.

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

**Next:** [Complete the release gate capstone](/articles/secure-cicd-capstone/).
