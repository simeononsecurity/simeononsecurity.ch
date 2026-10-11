---
title: "Local AI Secure Server Capstone Answer Key"
date: 2026-10-11
lastmod: 2026-10-11
toc: true
draft: false
description: "Compare a completed Local AI Secure Server capstone package with the beginner and advanced reference decisions."
genre: ["Artificial Intelligence", "Self-Hosted", "Capstone"]
tags: ["local AI capstone answer key", "secure Ollama server", "local LLM deployment decision", "AI server evidence review"]
cover: "/img/cover/local-ai-capstone-answer-key.webp"
coverAlt: "A reviewer compares beginner and advanced local AI server deployment packages with access and recovery evidence"
coverCaption: "Compare the deployment package with the reference evidence."
---

[Return to the capstone](/local-ai-secure-server-course/07-capstone/)

**Use this reference after completing your package and deployment decision.** Compare its scope, evidence, conditions, and open risks with your own record.

## Beginner Reference

A strong beginner decision reads:

> Approve for one local user with synthetic and low-sensitivity data. The runtime listens on loopback. The selected model fits with measured memory headroom. Three warm trials meet the stated response target. Remote access is absent. The prior configuration and model record support rollback.

## Advanced Reference

A strong advanced decision reads:

> Approve for approved private-network users after observed timeout and concurrency overload tests pass. The native runtime stays on loopback. An authenticated TLS gateway enforces per-user model access, request size, output, rate, and concurrency limits. Access tests show unauthorized and oversized requests denied before inference. Protected logs retain metadata under the stated schedule. Production data waits for privacy, legal, and incident reviews.

## Reconcile Your Decision

For each difference, record your original claim, the evidence in your package, the corrected claim, and any change to the decision. Keep synthetic gateway results separate from tests against your own server.

- **Beginner gate:** Confirm all nine files, model identity and license evidence, three warm trials, loopback binding, firewall policy, rollback results, and owners for remaining conditions.
- **Beginner rollback reference:** Preserve a pre-change configuration file and hash, apply one controlled lab-only change, record health, listener, and denial results, restore the saved file, repeat those checks, and record cleanup. A narrative without before and after evidence does not pass the rollback gate.
- **Advanced gate:** Confirm all nine files, artifact digest and retention, evaluation and capacity records, private gateway design, identity and logging controls, unauthorized and oversized denial tests, observed timeout and concurrency overload results, rollback results, and owners for remaining conditions. A missing timeout or overload result blocks approval.

Return to the [course hub](/local-ai-secure-server-course-start/) after your package meets the selected track gate.
