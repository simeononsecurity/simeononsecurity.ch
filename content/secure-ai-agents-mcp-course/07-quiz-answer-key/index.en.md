---
title: "Secure AI Agents and MCP Quiz Answer Key"
date: 2026-10-11
lastmod: 2026-10-11
toc: true
draft: false
description: "Score the Secure AI Agents and MCP knowledge check, review each reason, and repair missed security artifacts before the capstone."
genre: ["Artificial Intelligence", "Cybersecurity", "Assessment"]
tags: ["AI agent security quiz answer key", "MCP security quiz answers", "prompt injection assessment", "agent security review"]
cover: "/img/cover/secure-agent-quiz-answer-key.webp"
coverAlt: "A reviewer comparing secure agent quiz answers with an MCP authority map and approval record"
coverCaption: "Score the quiz and repair each missed control."
---

[Return to the Secure AI Agents and MCP Quiz](/secure-ai-agents-mcp-course/05-knowledge-check/)

**Use this key after you answer all ten questions.** Compare your reason with the security boundary or evidence named below.

## Answer Key

| # | Answer | Reason |
|---|---|---|
| **1** | C | Enforcement belongs outside untrusted content and model output. |
| **2** | C | The server validates a trusted host-held, single-use approval token and bound target state before the narrow write. A caller-supplied digest does not prove approval. |
| **3** | B | Schema validates shape. Server logic and identity controls enforce authority. |
| **4** | B | Approval needs the final action, target, payload, and effect. |
| **5** | C | An independent enforcement event proves the decision with useful context. |
| **6** | B | Environment inheritance often carries credentials and host configuration. |
| **7** | A | Tokens need audience and boundary checks. A token for one service should not flow to another. |
| **8** | B | The host should stop after the defined repeated failure threshold. |
| **9** | C | A controlled retest proves the enforcement change addresses the observed path. |
| **10** | B | Security review follows behavior and authority, not the feature label. |

## Passing Gate

You pass when your score reaches **8 out of 10** and questions **1, 2, 4, and 5** are correct.

- **Pass both gates:** Record your score and start the capstone.
- **Miss a core question:** Revisit the related lesson, repair the artifact, and answer the question again.
- **Score below eight:** Review every missed topic, update the related artifacts, and retake the quiz from a clean copy.

## Verify Your Review

- [ ] The recorded score reaches 8 out of 10
- [ ] Questions 1, 2, 4, and 5 are correct
- [ ] Every missed answer has a corrected reason
- [ ] Every related course artifact reflects the correction

Continue with the [Security Capstone](/secure-ai-agents-mcp-course/06-capstone/) after you pass both gates.
