---
title: "Module 5: Command and Control Operations"
date: 2026-09-12
lastmod: 2026-09-17
toc: true
draft: false
description: "Follow C2 task delivery, polling latency, uncertain outcomes, and operator handovers through worked examples and a task-ledger exercise."
genre: ["Red Team", "Offensive Security", "Command and Control"]
tags: ["red team", "command and control", "Cobalt Strike", "C2", "team server", "beacon", "listener", "asynchronous C2", "red team course"]
cover: "/img/cover/command-and-control-operations-cybersecurity.webp"
coverAlt: "An illustration showing three components of command and control operations: a secure fortress as the team server, a high-tech console as the client, and a glowing implant representing the beacon, all against a dark background."
coverCaption: "Module 5: trace a task from request to supported outcome."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Command and control (C2)** connects an operator's decisions to an agent running in a test environment. A useful operator distinguishes a submitted task from a delivered task, a completed action, and a returned result. Those states explain delays, prevent duplicate changes, and support an accurate activity record.

*Allow about 18 minutes, plus time to complete the timing exercise. The exercise uses invented timestamps and requires no deployed agent.*

## What You Will Learn

- **Identify** the client, team server, agent, listener, and redirector roles.
- **Explain** how polling affects task latency without treating it as a stealth guarantee.
- **Calculate** delivery delay from a short event timeline.
- **Compare** evidence from the console, network, and endpoint.
- **Produce** a task ledger with ownership, deadlines, and recovery decisions.

| Term | Meaning |
|---|---|
| **Client** | Operator interface connected to the shared backend |
| **Team server** | Backend coordinating sessions, tasks, and operation records |
| **Beacon** | Cobalt Strike's agent on an assessment endpoint |
| **Listener** | Named configuration for an agent's communication channel |
| **Redirector** | Intermediary forwarding selected assessment traffic |
| **Task ledger** | Your record of requests, results, and unresolved state |

## Separate the Components

The **client, team server, and Beacon** serve different roles. The client is the operator's interface, while the team server coordinates the operation and the agent performs work on an endpoint. Extension scripts loaded into one operator's client do not automatically appear in every other client. Mandiant's component analysis documents these boundaries. [Read the component analysis](https://cloud.google.com/blog/topics/threat-intelligence/defining-cobalt-strike-components/).

A **redirector** adds another communication dependency. A request reaching the intermediary proves less than a valid task exchange reaching the agent. A listener's display name is an organizational label, so record the actual destination, transport, owning server, and configuration revision alongside it.

The **management connection** and the **agent channel** also have separate failure modes. An operator might retain access to the console while an endpoint loses its permitted outbound route. Avoid describing both conditions as “the server is up” in a handover.

| Observation | What it establishes | What remains unknown |
|---|---|---|
| **Client connects** | Management access works | Agent delivery path |
| **Redirector responds** | A web endpoint answered | Correct forwarding and task decoding |
| **Agent checks in** | Recent communication occurred | Success of a particular task |
| **Task result arrives** | Output returned through the channel | Independent target-side confirmation |

## Follow a Task's Lifecycle

Use **queued, delivered, completed, and reported** as analytical states in your notes. These are course labels, not a promise about a product's UI terminology. The visible console often exposes only part of the lifecycle, so label unavailable timestamps as unknown.

**Asynchronous tasking** separates submitting work from receiving its result. Cobalt Strike's callback documentation describes responses arriving later, influenced by the agent's sleep interval. A callback in scripting also means a function handling a later result, so distinguish the programming term from a network check-in. [Read the callback documentation](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics_aggressor-scripts/as_callbacks.htm).

**Completion evidence** answers a different question from delivery evidence. A transport acknowledgment is insufficient to prove a registry read succeeded or an application accepted an operation. Preserve the task identifier and returned status so the record stays tied to the requested action.

{{< figure src="task-delivery-and-result-states.webp" alt="Four connected boxes trace a task from operator submission through delivery and execution to a recorded result" caption="Record unknown states explicitly instead of filling gaps with assumptions" >}}

## Understand Polling Latency

A **polling interval** creates a waiting period before queued work reaches an agent. For a simplified fixed schedule, a task arriving immediately after a poll waits nearly one full interval. Network delay, task duration, missed polls, and output transfer add further delay.

**Asynchronous** does not necessarily mean “open a new connection for every task.” Transport reuse, peer-to-peer communication, and implementation choices affect the underlying connections. Cobalt Strike supports multiple communication mechanisms, so describe the tested channel instead of assigning every agent one network pattern. [Read the vendor overview](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/welcome_main.htm).

**Detection** depends on the observed behavior and available sensors. Persistent connections occur in ordinary software, while repeated brief requests also create recognizable patterns. Changing the interval changes a measurement variable, not the truth value of “visible” or “invisible.”

| Simplified model | Result | Assumption |
|---|---|---|
| **Poll every 60 seconds** | Wait ranges from nearly 0 to nearly 60 seconds | No missed polls |
| **Uniform task arrival** | Mean polling wait is 30 seconds | Arrival independent of the schedule |
| **Five-second task** | Add five seconds to completion time | No contention or execution failure |

**The 30-second mean** is a mathematical expectation for this model, not a measured Cobalt Strike benchmark. Once the interval varies or tasks arrive in bursts, use the observed distribution. Report the sample count and collection window with any average.

## Work Through a Timeline

**Illustrative scenario:** an agent polls at 10:00:00, 10:01:00, and 10:02:00. An operator submits a read-only hostname request at 10:00:10. The task reaches the endpoint at 10:01:00, completes at 10:01:02, and its result appears in the console at 10:01:05.

| Event | Timestamp | Elapsed since submission |
|---|---|---|
| **Queued** | 10:00:10 | 0 seconds |
| **Delivered** | 10:01:00 | 50 seconds |
| **Completed** | 10:01:02 | 52 seconds |
| **Reported** | 10:01:05 | 55 seconds |

**Calculate first:** identify queue delay, execution duration, and the remaining reporting delay. Then explain why submitting the same task again at 10:00:40 would complicate the record. Assume all clocks share the same time reference for this exercise.

**Expected reasoning:** queue delay is 50 seconds, execution takes two seconds, and reporting adds three seconds after completion. The second submission creates another pending request before the first reaches its scheduled delivery opportunity. An absent early result does not establish a failed task.

**Change one assumption:** suppose the endpoint clock is 20 seconds ahead. Which durations remain trustworthy from these timestamps alone? Cross-host differences now need clock-offset information, while durations measured within a single reliable clock remain interpretable.

## Handle Uncertain Results

**Unknown outcome** is an operational state worth retaining. A connection loss after delivery leaves open whether the task ran, failed, or completed without returning output. Retrying a state-changing task without reconciliation risks applying the action twice.

**Read-only and state-changing tasks** need different retry decisions. A repeated inventory query mainly affects workload and evidence volume. A repeated configuration change requires checking current state and the expected effects of repetition before resubmission.

| Failure point | First check | Record before retrying |
|---|---|---|
| **No recent check-in** | Channel health and endpoint availability | Last confirmed communication |
| **Delivered, no result** | Endpoint outcome and task status | Delivery evidence and uncertainty |
| **Result is an error** | Exact error and requested resource | Arguments, context, and timestamp |
| **Conflicting operators** | Session owner and pending work | Agreed next action |

**A deadline** belongs in the task record before execution. It sets the point for review or escalation, rather than an automatic instruction to resend. For long-running work, verify the documented cancellation behavior before treating a console action as proof the endpoint stopped.

## Observe Both Ends

**Endpoint evidence** provides a separate view of the action. For example, configured Sysmon network events associate a connection with a process, while process events help reconstruct execution. Event availability depends on installation, configuration, filtering, and retention. [Read Microsoft's Sysmon documentation](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

**A missing event** has several explanations. The action might not have happened, the relevant event type might be disabled, or collection might have failed. Before treating absence as a security finding, verify the observation path with a known benign control action.

**Cross-source correlation** needs host identity, timestamps, task identifiers, and the test window. IP addresses and process IDs alone are weak long-term join keys because their assignments change. Keep the raw evidence location with your interpretation so another reviewer has a path back to the source.

| Evidence source | Useful question |
|---|---|
| **Operator ledger** | Who requested the task and why? |
| **Team-server record** | What was queued and returned? |
| **Network record** | Which observed endpoints exchanged traffic? |
| **Endpoint record** | What process or resource activity occurred? |

## Watch the Operations Lecture

The **Cobalt Strike Archive** lecture covers the operations model, team servers, logging, and reporting. Watch for the separation between managing an operation and proving a task's outcome. Then map one demonstrated action onto the four analytical states used above.

*This is a historical 2019 lecture. Use current vendor documentation for supported releases, authentication requirements, and UI details.*

{{< youtube id="q7VQeK533zI" enable="true" title="Red Team Ops with Cobalt Strike (1 of 9): Operations" >}}

**Watch on YouTube:** [Red Team Ops with Cobalt Strike (1 of 9): Operations](https://www.youtube.com/watch?v=q7VQeK533zI).

## Build Your Task Ledger

**Create a handover record** for three hypothetical tasks: a successful inventory query, a delivered task with no returned result, and a queued task canceled before confirmed delivery. Give each task a different identifier. Include only synthetic hosts and identities.

```text
Task ID:
Objective and approved endpoint:
Operator and session owner:
Requested action and expected output:
Queued timestamp:
Delivery evidence:
Completion evidence:
Returned status and evidence location:
Deadline and review decision:
Retry or cancellation rationale:
Remaining uncertainty:
```

**Review your design** with a second reader. They should identify which tasks are safe to close, which require reconciliation, and who owns the next decision without opening the original console. A ledger filled with “done” and “failed” is insufficient if it hides the evidence behind those labels.

**Success criterion:** every closed task has a supported outcome, and every unresolved task has an owner and next check. Keep timing calculations separate from claims about security-tool performance. This artifact extends the infrastructure register from [Module 2](/red-team-course/mission-preparation-and-infrastructure/) into day-to-day operation.

## Check Your Understanding

1. **Components:** why does a working client connection fail to prove agent reachability?
2. **Timing:** what assumptions support the half-interval mean waiting time?
3. **Retries:** why is missing output insufficient justification for repeating a configuration change?
4. **Evidence:** what should you verify before interpreting an absent network event?

| Question | Expected reasoning |
|---|---|
| **Components** | Management and agent traffic use distinct paths and dependencies |
| **Timing** | A fixed successful polling schedule and independent uniform task arrival |
| **Retries** | The action might already have completed without returning output |
| **Evidence** | Sensor health, event configuration, filters, retention, and a control observation |

## Next Steps

**Execution location** adds another dimension to task reliability. Continue to [Module 6: Beacon Execution and Beacon Object Files](/red-team-course/beacon-execution-and-beacon-object-files/) to compare process boundaries, dependencies, and failure consequences. Return to the [Red Team Course hub](/red-team-course-start/) for the full sequence.
