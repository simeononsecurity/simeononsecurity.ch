---
title: "Capstone: Review a Secure Agent and MCP Design"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Produce and evaluate a review-ready security package for an AI agent with MCP tools."
genre: ["Artificial Intelligence", "Cybersecurity", "Capstone"]
tags: ["AI agent security capstone", "MCP design review", "agent threat model", "security evidence"]
cover: "/img/cover/secure-agent-mcp-capstone.webp"
coverAlt: "Review board with an agent authority map, MCP contract, test trace, and approval record"
coverCaption: ""
---

[Return to the Secure AI Agents and MCP Course](/secure-ai-agents-mcp-course-start/)

**Your capstone is a security decision package for Patch Clerk.** Another reviewer should reach the same deployment decision from your artifacts and evidence.

## Scenario Change

Patch Clerk now reads synthetic issues, reads repository files, proposes a patch, and applies a reviewed patch in a test repository. A product owner requests a new `post_comment` tool. The tool would publish text to a fictional issue system.

Your job is to decide whether `post_comment` enters the first release. Treat publication as an external side effect.

## Required Package

Create **`capstone/`** with these files:

```text
capstone/
  system-map.md
  authority-matrix.md
  mcp-security-contract.md
  event-example.json
  detection-plan.md
  attack-test.md
  deployment-decision.md
```

Each file has one purpose:

- **`system-map.md`** names components, trust boundaries, data origins, and owners.
- **`authority-matrix.md`** lists operations, identities, approval, and evidence.
- **`mcp-security-contract.md`** defines inputs, outputs, limits, errors, and side effects.
- **`event-example.json`** shows the decision event format without storing unnecessary raw content.
- **`detection-plan.md`** maps signals to stop and recovery actions.
- **`attack-test.md`** records the hostile fixture, expected result, observed result, and retest.
- **`deployment-decision.md`** states approve, approve with conditions, or reject.

## Build the Review

1. Copy your lesson artifacts into **`capstone/`**.
2. Add `post_comment` to the authority matrix as proposed.
3. Define a 2,000-character limit and one approved issue target.
4. Require a preview and trusted host-held, single-use approval bound to the comment digest and target-state precondition. A caller-supplied digest is not approval.
5. Give the tool a dedicated identity restricted to comment creation on the approved test project.
6. Add rate limits and a stop rule for repeated publication requests.
7. Run the [local comment policy simulator](/downloads/secure-ai-agents-mcp-course/comment_policy_lab.py) with `python3 comment_policy_lab.py`. Record all nine expected and observed decisions in **`attack-test.md`**. Include the hostile denial, valid `would_post` decision, replay denial, forged self-approval denial, target and length denials, identity denial, changed-state denial, and rate-limit denial.
8. Record your decision and residual risks.

Do not connect a live issue service. Treat the capstone as a design and local policy test.

## Decision Rubric

| Area | 0 points | 1 point | 2 points |
|---|---|---|---|
| **Authority** | Broad shared identity | Narrow identity with gaps | Dedicated least-privilege identity |
| **Input** | Free-form unchecked payload | Length or target check | Typed input, target allowlist, and length limit |
| **Approval** | None | Approval before final payload | Preview and digest-bound single-use approval |
| **Evidence** | Model transcript only | Host event | Host, server, and downstream correlation |
| **Attack test** | No hostile fixture | Expected result only | Observed local denial plus positive test |
| **Recovery** | Restart only | Revoke or restore | Stop, revoke, preserve, restore, repair, retest |

A score below **10 out of 12** fails the release review. Any zero in authority, approval, or attack test also fails.

## Expected Result

Your package scores at least 10. It contains no real secrets or external connections. The decision states who owns remaining risk and which evidence is still missing for production.

## Troubleshooting

- **The package repeats chat transcripts:** Replace narrative with maps, contracts, events, diffs, and test results.
- **The comment identity reaches every project:** Restrict the downstream account before relying on server input checks.
- **Approval lacks a payload digest:** Bind approval to the final issue target and comment text.
- **The attack test blocks valid comments:** Add a positive test and repair the narrow policy path.
- **Residual risk has no owner:** Assign a named role with a review date and acceptance decision.

## Verify Completion

```bash
find capstone -maxdepth 1 -type f -print | sort
python3 -m json.tool capstone/event-example.json
grep -Ein "decision|owner|residual|approval|digest" capstone/deployment-decision.md
```

Pass when all seven files exist, JSON parses, the rubric score reaches ten, no core area scores zero, and the decision separates observed local evidence from future production tests. Finish and score your package before opening the [Capstone Answer Key](/secure-ai-agents-mcp-course/08-capstone-answer-key/).

Review the [Capstone Answer Key](/secure-ai-agents-mcp-course/08-capstone-answer-key/) after you record your score and decision. Return to the [course hub](/secure-ai-agents-mcp-course-start/) or review the [MCP 2026-07-28 release notes](https://blog.modelcontextprotocol.io/posts/2026-07-28/) before adapting the package to a real implementation.
