---
title: "Module 1: Red Team Methodology"
date: 2026-09-12
lastmod: 2026-09-17
toc: true
draft: false
description: "The seven-phase red team methodology: preparation, intelligence, reconnaissance, access, post exploitation, cleanup and backout, and reporting, with the judgment behind each."
genre: ["Red Team", "Offensive Security", "Methodology"]
tags: ["red team", "red team methodology", "mission preparation", "OSINT", "active reconnaissance", "target exploitation", "post exploitation", "cleanup", "backout", "mission objective", "adversary emulation", "red team course"]
cover: "/img/cover/red-team-methodology-six-phases-visualization.webp"
coverAlt: "An illustration of a circular flowchart representing the six phases of Red Team methodology, featuring vibrant colors against a dark background. Abstract elements suggest data streams and network connections."
coverCaption: "Module 1: the seven phases every technique slots into."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Red team methodology** connects an agreed business question to a controlled test and evidence the customer is able to use. This course uses six phases to organize the work, with feedback between phases as observations change the plan. Your outcome is an evidence-backed conclusion, an explained limit, and a verified restoration record.

*Allow 25 minutes for reading and 30 minutes for the tabletop exercise. No attack tooling is required for this module.*

## Learning Outcomes

- **Recall the phases:** place a technique within a larger operation.
- **Explain the objective:** distinguish access, business impact, and assessment evidence.
- **Apply a planning method:** connect an approved action to a specific observation.
- **Evaluate a result:** distinguish prevention, missing telemetry, and insufficient evidence.
- **Create a test plan:** define entry conditions, stopping points, cleanup, and acceptance criteria.

## The Six Phases

**The seven-phase model** is this course's organizing convention. It is not the MITRE ATT&CK matrix, an official maturity score, or a guarantee of one correct sequence. An operation often returns to reconnaissance after a new observation, and some tests finish without persistence or a domain-controller objective.

| Phase | Main question | Deliverable |
|---|---|---|
| **Mission preparation** | What is authorized and ready? | Scope, test conditions, contacts, and infrastructure inventory |
| **Open-source intelligence** | What does public information support? | Attributed observations with confidence and collection dates |
| **Active reconnaissance** | What does interaction with the approved environment reveal? | A bounded target and dependency map |
| **Target exploitation** | Does the selected route produce the intended test condition? | Reproducible evidence of success, prevention, or a limit |
| **Post exploitation** | Which approved objective follows from the obtained context? | An access path and its observed effects |
| **Cleanup and backout** | What must be removed or restored? | Artifact ledger, backout actions, and baseline verification |
| **Mission objective and reporting** | What did the assessment prove? | Findings, restoration evidence, and remediation priorities |

**Cleanup, backout, and reporting begin during preparation.** They are not tasks postponed until the final day. An operation lacking an artifact register, original-state record, or timestamps is difficult to explain even when the technical action succeeds.

## Objectives Before Techniques

A **mission objective** states the question the assessment is intended to answer. “Obtain administrator access” is incomplete unless it explains which business or control outcome the access tests. A customer might instead need evidence about segregation between application roles or the ability to recognize one defined behavior.

**Illustrative objective:** Determine whether a synthetic finance user is permitted to read a restricted sample report outside their role. The sample report contains no real financial data. Success means the test establishes an access-control result and collects enough evidence to reproduce the conclusion.

| Weak objective | More useful formulation |
|---|---|
| **Get a shell** | Determine whether the approved entry route reaches the designated lab execution context |
| **Become domain admin** | Evaluate the named privilege boundary supporting the agreed business scenario |
| **Avoid detection** | Measure which approved behaviors produce telemetry, alerts, and analyst action |
| **Exfiltrate data** | Demonstrate the approved data path using a designated synthetic marker and transfer limit |

**An objective also defines when to stop.** If a sample-file read answers the question, copying an entire share adds data exposure without improving the finding. The test plan should identify the minimum proof before an operator reaches the resource.

## Use ATT&CK Precisely

**MITRE ATT&CK** provides a vocabulary for adversary behavior. A tactic describes an adversary goal, while a technique describes behavior supporting a goal. Map a specific observation to a technique when the evidence supports it, then retain the actual procedure and environment details alongside the mapping. [MITRE guidance on adversary emulation and red teaming](https://attack.mitre.org/resources/get-started/adversary-emulation-and-red-teaming/)

**A technique identifier is not a test result.** Listing an identifier does not establish whether an action executed, whether a sensor recorded it, or whether an analyst understood it. Different implementations of a related behavior also exercise different prerequisites and telemetry.

{{< figure src="objective-evidence-review-loop.webp" alt="Diagram linking an assessment objective to an approved test, collected evidence, and a review decision" caption="Every test needs a question, a bounded action, and evidence supporting its conclusion" >}}

## Preparation and Scope

**Mission preparation** establishes the assets, actions, identities, and time windows included in the exercise. It also records exclusions, data-handling rules, operational contacts, and the restoration process. NIST's assessment guidance provides a planning reference for these decisions. [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)

**Deconfliction** is the process for comparing suspicious activity with the team's authorized actions. A matching source address alone is weak evidence. Use timestamps, action identifiers, hosts, accounts, and operator records to distinguish the exercise from an unrelated incident.

| Planning item | Example decision |
|---|---|
| **Target boundary** | Only the named lab application and two test accounts |
| **Permitted action** | Attempt a read of the designated synthetic report |
| **Stop condition** | An unrelated production record appears |
| **Contact** | Named exercise controller and a tested backup channel |
| **Restoration** | Remove test grants and verify the baseline role assignments |

**Scope changes require a recorded decision.** A newly reachable system or interesting credential is an observation, not an extension of the approved target list. Bring the observation to the exercise controller before treating it as another test step.

## OSINT and Active Reconnaissance

**Open-source intelligence (OSINT)** uses publicly available information. Its collection method determines whether it touches customer-controlled infrastructure. Reading an archived page differs from browsing the customer's live site, and public content still produces access logs when requested directly.

**Active reconnaissance** deliberately interacts with a target to answer a specific question. The important distinction is the collection path and the resulting evidence, not an absolute claim about generating zero alerts. Document both third-party sources and direct interactions.

| Collection | Likely observation point | Limitation |
|---|---|---|
| **Third-party archive** | Archive provider | Historical content might be stale |
| **Public registration record** | Registry or lookup provider | Ownership does not establish test authorization |
| **Live customer webpage** | Customer web or proxy logs | Public access is still direct interaction |
| **Approved service probe** | Target network and service logs | A response establishes only the tested condition |

**Reconnaissance produces hypotheses.** A banner suggesting an older product version is a lead to validate, not proof of an exploitable vulnerability. A missing response likewise does not prove a host is absent.

## Exploitation and Post Exploitation

**Target exploitation** tests a selected route within the agreed conditions. Select the route because it answers the objective and fits the risk constraints. There is no requirement to demonstrate every possible weakness or to persist after every successful entry.

**Post exploitation** evaluates the context obtained after access. Identity, privilege, reachable resources, and dependencies determine which approved next step is meaningful. Extra persistence or lateral movement adds work and artifacts, so it needs a reason tied to the scenario.

| Result | Useful next decision |
|---|---|
| **Route prevented** | Preserve prevention evidence and determine whether another route is part of scope |
| **Low-privilege access obtained** | Record the context and test the permitted objective |
| **Objective already satisfied** | Stop expansion and validate evidence and restoration |
| **Unexpected sensitive access** | Pause and use the agreed deconfliction channel |

**A domain controller is one possible dependency**, not the destination of every operation. The assessment might finish at a file-server permission boundary or a cloud application's role check. Explain the business significance of the result instead of treating domain control as a universal score.

## Supplemental Video

{{< youtube id="tvQbh0bawEM" enable="true" title="Adversary Emulation: Generating MITRE ATT&CK Technique Sequences" >}}

**Watch:** [Adversary Emulation: Generating MITRE ATT&CK Technique Sequences](https://www.youtube.com/watch?v=tvQbh0bawEM), presented by Martin Eian and published by FIRST. The presentation examines dependencies between techniques when assembling an emulation sequence. Use it to assess why a list of behaviors needs an execution plan.

**Viewing task:** Pick two behaviors from a fictional scenario and write the prerequisite connecting them. Then identify one condition under which the second behavior would be irrelevant. Compare the dependency with the objective instead of assuming a longer sequence is a better test.

## Evidence Has Several Stages

**Execution, collection, alerting, and response** are different outcomes. A successful test action might produce an event without generating an alert. An alert might exist without reaching an analyst inside the evaluation window. Report each observed stage separately.

| Stage | Evidence needed |
|---|---|
| **Action executed** | Operator record and observed target-side result |
| **Telemetry collected** | Relevant event present at the expected sensor or collector |
| **Detection generated** | Alert tied to the test's entity and time |
| **Analyst response** | Case activity showing interpretation and an action |
| **Restoration verified** | Comparison against the agreed baseline |

**An empty search is not a detection verdict.** The event might be missing because logging was disabled, collection failed, timestamps differ, or the search selected the wrong host. Resolve these possibilities before classifying a control gap.

**Illustrative reasoning:** A file-access exercise succeeds at 10:05 UTC. The operator has a screenshot, but the analyst searches local time and finds no event. The first follow-up is time and collection correlation, not a claim of undetected access.

## Cleanup and Backout

**Cleanup** removes artifacts owned by the exercise. **Backout** returns modified systems to the agreed baseline. The two actions overlap, but they are not identical. A newly created test value might be removed, while a pre-existing permission change needs its recorded original value restored.

**Plan the backout before the first state change.** Record the owner, original value, affected process, trigger, evidence location, and verification step. Preserve customer logs and assessment evidence according to the engagement agreement. Backout does not mean erasing the record of what happened.

| Backout item | Required evidence |
|---|---|
| **Created artifact** | Ownership record, removal result, and absence check |
| **Modified setting** | Original value, narrow restoration, and comparison |
| **Running process** | Process owner, stop action, and later state |
| **Service or task** | Configuration baseline, state, and trigger retest |
| **Customer evidence** | Retention decision and report reference |

**Backout completion is a finding**, not an assumption. Mark each item verified, unresolved, or retained by agreement. If another administrator changed the same object, pause the reversal and use the named owner to resolve the conflict.

**Exercise:** Add a cleanup and backout section to the synthetic finance-report test card. List one created artifact, one modified setting, one running process, and the evidence proving each final state. State the condition preventing backout from proceeding safely.

**Expected reasoning:** The artifact register determines ownership. The original-state record determines restoration. A process check determines whether the removed trigger left an existing instance running. A conflict with a later administrator change requires owner review rather than an automatic overwrite.

## Design One Bounded Test

Use this **test-card template** before a tabletop or lab exercise:

```text
Business question:
Approved assets and identities:
Required starting context:
Behavior and ATT&CK mapping, if justified:
Permitted action and maximum scope:
Expected operator-side evidence:
Expected defender-side observation:
Stop conditions and controller contact:
Restoration steps and verification:
Observed result, limitations, and next decision:
```

**Micro emulation plans** provide examples of narrowly scoped tests organized around specific behaviors. Their value is repeatability and an explicit relationship between action and observation. Adapt the idea to the customer question rather than treating a public plan as approval to run it. [MITRE Center for Threat-Informed Defense project](https://ctid.mitre.org/projects/micro-emulation-plans/)

**Exercise:** Create a card for the synthetic finance-report scenario. Include an authorized reader and a restricted reader, the exact sample resource, a collection window, and the restoration check. Record what would establish a permission problem and what would leave the result inconclusive.

## Evaluate Your Test Card

**Expected reasoning:** The authorized reader establishes a baseline for the resource's availability. The restricted reader tests the intended access boundary. A successful unauthorized read supports the access-control finding, while a timeout requires investigation before it supports any permission conclusion.

**Improve the plan** by adding one controlled variation. For example, repeat the same read after correcting the sample folder permission. Keep the identities, resource, and collection method stable so the comparison answers a clear question.

| Review question | A useful answer contains |
|---|---|
| **What is being tested?** | A named business or control boundary |
| **What changes?** | One explicit action or configuration difference |
| **What proves the result?** | Evidence from the relevant layer |
| **What ends the test?** | A success condition, limit, or stop rule |
| **What remains afterward?** | An artifact inventory and verified baseline |

## Self-Check

1. **Seven phases:** Which phases repeat after new evidence appears?
2. **OSINT:** Why does publicly available information not imply zero interaction?
3. **ATT&CK:** What does a technique identifier leave unspecified?
4. **Post exploitation:** When is additional persistence unnecessary?
5. **Negative result:** What must you examine before calling an action undetected?

**Answer key:** Reconnaissance and planning repeat as the situation changes. Public resources still have collection paths and access logs. ATT&CK identifiers leave procedure, prerequisites, and actual test results to document.

**Operation decisions:** Persistence is unnecessary when the objective does not require it. An undetected-action claim needs verified execution, appropriate collection, a valid search, and a defined observation window. Cleanup and backout need their own final-state evidence.

## Next Steps

**Keep your test card** and refine its infrastructure and deconfliction requirements in **[Module 2: Mission Preparation and Infrastructure](/red-team-course/mission-preparation-and-infrastructure/)**. Return to the **[course hub](/red-team-course-start/)** for the module sequence.
