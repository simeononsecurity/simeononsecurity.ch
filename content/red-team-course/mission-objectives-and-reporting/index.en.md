---
title: "Module 20: Mission Objectives and Reporting"
date: 2026-09-12
lastmod: 2026-09-17
toc: true
draft: false
description: "Turn red-team objectives into bounded tests and evidence-backed findings with explicit limits, remediation owners, and retest conditions."
genre: ["Red Team", "Offensive Security", "Reporting", "Assessment"]
tags: ["red team", "objectives", "reporting", "evidence", "remediation", "retest", "red team course"]
cover: "/img/cover/mission-objectives-reporting.webp"
coverAlt: "A red team report board connects an objective to evidence, impact, remediation ownership, and a retest decision."
coverCaption: "Module 20: make the final report useful to the next decision maker"
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**A red-team report is a decision record.** It links an approved objective to observed evidence, impact, limits, remediation ownership, and a retest condition. A dramatic technique name without those links does not help the customer choose a fix.

This module creates a **mission finding package**. You will write a bounded objective, separate expected from observed behavior, and design a retest another assessor will reproduce.

*Allow 35–50 minutes. Difficulty: intermediate. The report example is synthetic.*

## Learning Outcomes

- **Define** objective, observation, impact, limitation, and retest.
- **Explain** why protocol support does not prove a configured access path.
- **Apply** an evidence chain to a host or identity finding.
- **Evaluate** competing explanations and remediation choices.
- **Create** a concise finding package with an owner and retest.

## Start With the Objective

An **objective** names the decision the assessment must inform. “Compromise the network” is too broad. “Determine whether the approved service account reads the reporting share from the staging host during the maintenance window” is testable.

| Objective field | Example |
|---|---|
| **Question** | Does the account read the named share? |
| **Source** | Staging host and recorded principal |
| **Target** | Reporting share on the approved server |
| **Window** | 2026-09-17 20:00–20:30 UTC |
| **Success evidence** | Server-side access record and controlled file result |
| **Stop condition** | No further access after first validated result |

## Separate Expected and Observed

**Expected behavior** comes from documentation, a lab fixture, or a hypothesis. **Observed behavior** comes from a timestamped command, event, trace, or owner confirmation. A report should label the difference so a reader does not confuse a planned step with a completed action.

| Statement | Classification |
|---|---|
| **SSH supports keys and certificates** | Protocol capability |
| **This server allows this key** | Configuration observation |
| **A Linux host joined the AD domain** | Environment observation |
| **Plaintext credentials were collected** | Evidence claim requiring a specific source |
| **Event 4624 occurred** | Logon event, not physical user presence |

**SSH supports several authentication methods** when configured. A Linux host joins an Active Directory domain, yet neither fact proves a stolen password, an interactive user, or administrative access. State the configured method and evidence source.

## Build the Evidence Chain

{{< figure src="objective-evidence-remediation-retest.webp" alt="A reporting flow connects a bounded objective to observed evidence, impact limits, remediation ownership, and a repeatable retest" caption="A useful finding preserves the path from question to retest" >}}

An **evidence chain** has five links: objective, action, observation, interpretation, and decision. If a link is missing, reduce the claim. A failed collection step belongs in the limitation field rather than being silently treated as a negative result.

**Impact** should be concrete. Name the account, resource, data class, or control affected. Avoid universal claims such as “full domain compromise” unless the evidence in practice establishes the required authority and path.

## Watch a Reporting Context

{{< youtube id="cULyBdtE-SM" enable="true" title="Compass Security Beer-Talk: Responding to Cyber Attacks" >}}

**Compass Security's incident-response discussion** complements the reporting lesson by showing why evidence, timeline, and ownership matter after an event. Use it to consider which facts a defender needs first. [Watch the discussion on YouTube](https://www.youtube.com/watch?v=cULyBdtE-SM).

**The video is context, not evidence for your finding. Your report still needs its own commands, events, timestamps, and scope.

## Write a Finding

Use a **finding structure** which makes review quick. Put the decision first, then the evidence and limits which support it.

```text
Title:
Objective and scope:
Observed condition:
Evidence references and timestamps:
Impact and affected owner:
Limitations and alternate explanations:
Remediation recommendation:
Remediation owner and target date:
Retest procedure and success condition:
```

**Title** should describe the condition and consequence, not a tool name. **Remediation** should address the weak boundary identified in the evidence. **Retest** should repeat the disputed operation after the fix and state what result closes the finding.

## Analyze a Synthetic Finding

**Assume a staging Linux host uses an approved SSH certificate. The server log records a successful certificate authentication for the named assessment account. The account reads one application directory but cannot write it. No evidence shows access to production hosts or plaintext passwords.

The **supported conclusion** is scoped read access to the staging directory through the configured certificate method. The report should not claim stolen passwords, production access, or domain compromise. A remediation owner narrows the account's directory ACL or remove the certificate after the window.

| Evidence | Supported claim |
|---|---|
| **SSH server log** | Certificate authentication occurred |
| **Directory read result** | Named read operation succeeded |
| **Write denial** | Named write operation was not authorized |
| **No production test** | Production access remains untested |
| **No secret artifact** | Plaintext collection is unsubstantiated |

## Choose Remediation and Retest

A **remediation** should change the condition enabling the finding. Rotating an unrelated password does not repair a directory ACL. Removing a certificate without checking alternate keys or service accounts might leave the same access path open.

| Finding condition | Retest |
|---|---|
| **Unneeded certificate** | Revoke it and repeat the named authentication attempt |
| **Excess directory read** | Adjust ACL and repeat the read test |
| **Broad service account** | Reduce scope and test each required service |
| **Missing logging** | Enable collection and repeat the bounded action |

The retest must preserve the **same objective, source, target, and operation** unless the change intentionally alters one of them. Record the new result and any residual limitation.

## Preserve the Timeline

**Timestamps** connect operator actions, endpoint events, server logs, and owner decisions. Use a consistent timezone and identify clock uncertainty. An event ID without host, channel, or collection status is difficult to validate.

**Evidence retention** follows the engagement agreement. Keep raw records and a readable analyst extract when possible. Do not delete customer logs to make the report shorter. If data was unavailable, say which collector, host, or time range was missing.

## Create the Mission Package

Write a **one-page mission finding** for the synthetic SSH case. Include one alternate explanation and a retest which was able to disprove your conclusion. Identify a remediation owner and the artifact which proves closure.

**Completion standard:** A reviewer identifies the question, observed result, impact boundary, limitation, owner, and repeatable retest without reading the entire course.

## Self-Check and Answers

| Question | Expected reasoning |
|---|---|
| **Does SSH support prove a key is configured?** | No, server configuration and logs are needed |
| **Does event 4624 prove a physical user?** | No, it records a logon event with context |
| **What belongs in limitations?** | Missing collection, untested scope, and alternate explanations |
| **What makes remediation relevant?** | It changes the documented enabling condition |
| **What makes a retest useful?** | It repeats the same disputed operation after the fix |
| **What closes a finding?** | Owner action plus evidence meeting the success condition |

## Next Steps

You have completed the **Red Team Course** sequence. Return to the [course hub](/red-team-course-start/) to review each module, then apply the mission package format to a new approved exercise.
