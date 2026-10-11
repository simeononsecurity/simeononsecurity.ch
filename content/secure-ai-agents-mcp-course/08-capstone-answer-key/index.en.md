---
title: "Secure AI Agents and MCP Capstone Answer Key"
date: 2026-10-11
lastmod: 2026-10-11
toc: true
draft: false
description: "Compare a completed Secure AI Agents and MCP capstone with the reference deployment decision and required security conditions."
genre: ["Artificial Intelligence", "Cybersecurity", "Capstone"]
tags: ["AI agent security capstone answer key", "MCP design review answer", "agent threat model review", "security evidence assessment"]
cover: "/img/cover/secure-agent-capstone-answer-key.webp"
coverAlt: "A reviewer comparing an AI agent deployment decision with MCP approval, evidence, and attack-test requirements"
coverCaption: "Compare the completed package with the reference decision."
---

[Return to the Secure AI Agents and MCP Capstone](/secure-ai-agents-mcp-course/06-capstone/)

**Open this reference after you finish and score your capstone package.** Record each difference as a correction or residual risk.

## Reference Decision

The reference decision is **approve with conditions for a test environment**.

Required conditions:

1. `post_comment` uses a dedicated test-project identity.
2. The host shows the issue identifier and final comment text.
3. A trusted host records approval with a random, single-use token bound to the action digest and expiry. Untrusted content cannot mint approval.
4. The server rejects any other project, issue, or payload over 2,000 characters. Approval binds the preview and current target-state digest.
5. The event stream records preview, approval, call, and downstream result under one run ID.
6. A hostile issue instruction fails before the downstream request.
7. A valid approved comment returns `would_post` in the synthetic positive test. The local simulator prints `9/9 passed` and makes no downstream request.

Production release stays out of scope until a real authorization test, downstream audit review, and incident exercise produce evidence.

## Review Gate

Use the rubric on the [capstone prompt](/secure-ai-agents-mcp-course/06-capstone/). Pass when the package scores **10 out of 12 or higher** and authority, approval, and attack test each score at least one point.

## Verify Your Review

- [ ] The decision names the test-only release boundary
- [ ] All seven required conditions appear in the package or correction record
- [ ] The score reaches 10 out of 12
- [ ] Authority, approval, and attack test have no zero scores
- [ ] Production evidence gaps have owners and follow-up checks

Return to the [Secure AI Agents and MCP Course](/secure-ai-agents-mcp-course-start/) after you record corrections and the final score.
