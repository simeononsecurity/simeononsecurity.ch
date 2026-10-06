---
title: "One Source, Many Tools: Building an AI Collaboration Framework for Mixed Teams"
date: 2026-10-01
lastmod: 2026-10-01
toc: true
draft: false
description: "Build a shared AI collaboration framework for coders and non-coders. Assign sources of truth, track context versions, review durable changes, and choose project maps, RAG, or both."
genre: ["Artificial Intelligence", "Knowledge Management", "Software Engineering", "Team Collaboration"]
tags: ["AI collaboration framework", "mixed teams", "source of truth", "AI agents", "AGENTS.md", "CLAUDE.md", "Cline rules", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "retrieval augmented generation", "RAG", "Model Context Protocol", "project map", "context manifest", "knowledge management", "documentation drift", "human approval", "decision register", "agent handoff", "policy versioning", "Git worktrees", "pull request gates"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "An illustration of a group of professionals collaborating on cybersecurity work"
coverCaption: ""
---

**Two people ask two AI tools the same question:** how long should the service retain an export? In this illustrative example, the developer's IDE agent answers seven days from a README. The operations lead's chat assistant answers thirty days from a wiki page. Both responses sound confident. Each tool read a different copy of the truth.

**The failure is ownership**, not prompt quality. The wiki requirement changed last week, but nobody updated the README. The developer asks the agent to fix the retention job. It follows the older document and produces a tidy patch which restores the wrong behavior. Reviewers inspect the code without seeing the requirement version behind the answer.

**Give every fact one home.** Make every tool read from the home, and route every durable change back through a person. A repository, wiki, and tracker still serve different purposes. They need explicit authority, named owners, and a shared procedure for moving information between them.

**This guide gives you a model to apply this week**, with or without retrieval-augmented generation. Start with a project map, versioned instructions, evidence records, and reviewed proposals. Add search infrastructure only when the retrieval problem warrants it.

## Key Takeaways

- **Assign authority by information type**, rather than forcing everything into one application.
- **Treat memory and retrieval indexes as caches**, never as independent policy sources.
- **Attach source versions to proposals**, so reviewers know which facts informed a change.
- **Enforce approval outside prompts**, through access controls and required review gates.
- **Share the procedure across tools**, while adapting its delivery to each interface.

## Before You Begin

**Prerequisites:** choose one pilot project with a repository, a wiki or document system, a tracker, and owners willing to review changes. A team without a wiki substitutes a versioned document store. Keep the ownership model unchanged.

**Estimated time:** reserve two to four hours for the initial map and templates, followed by a one-week pilot. **Difficulty:** moderate. The hard part is agreeing on authority, not installing another AI tool.

**Scope:** this is a proposed team operating model. Its approval rules and naming conventions are recommendations, not default behavior guaranteed by Claude Code, Codex, Cline, Cowork, Copilot, or ChatGPT. The automatic table of contents above links to each implementation step.

## Mixed Tools, Split Context

**Coders and non-coders share a project**, but they approach it through different interfaces. A developer uses an IDE or terminal agent. A product owner uses a chat project. An operations lead works from a wiki and tracker. Choose those interfaces around the task, not around access to the authoritative facts.

**Context is the material available for the current answer.** Inspect each session for repository files, uploaded documents, chat history, saved memory, connector results, and retrieved excerpts. Two sessions with different evidence need not agree, even when their questions match.

| Failure | What you see |
|---|---|
| **Documentation drift** | A README repeats an obsolete requirement |
| **Summary promotion** | A session recap becomes evidence without its original source |
| **Overlapping writes** | Two agents replace the same page from different base versions |
| **Lost decisions** | A meeting agreement never reaches the decision register |
| **Missing provenance** | A plausible answer names no page version or commit |

**The retention example exposes the distinction.** The wiki describes the approved target behavior. The code describes implemented behavior. Neither should silently rewrite the other. Record the disagreement and ask the named owner whether implementation or requirement needs revision.

> **Key Takeaway:** agreeing on authority comes before agreeing on an AI tool. Start by defining the vocabulary below.

### Sidebar: Five Shared Terms

| Term | Meaning in this framework |
|---|---|
| **Source** | The designated authoritative record for an information type |
| **Cache** | A derived copy used for speed or convenience |
| **Proposal** | A suggested change awaiting owner approval |
| **Project map** | An index of source locations, identifiers, and owners |
| **Manifest** | A record of the exact evidence used for an answer or proposal |

## Give Facts One Home

**One source means one authority per fact**, not one database for the entire organization. Establish the following allocation during the pilot. Replace the example roles with your team's actual owners.

| Information type | Home system | Owner | Who writes | How agents read |
|---|---|---|---|---|
| **Code, tests, config, schemas** | Repository | Engineering maintainer | Contributors through reviewed PRs | Files at a recorded commit |
| **Shipped docs and ADRs** | Repository | Technical owner | Contributors through the same PR | Versioned files |
| **Requirements** | Wiki | Product owner | Owner or approved publisher | Page ID and revision |
| **Runbooks** | Wiki | Operations owner | Approved publisher | Page ID and revision |
| **Policy** | Wiki | Policy owner | Approved publisher after review | Canonical page plus local adapter |
| **Cross-team decisions** | Wiki decision register | Named decision owner | Owner after approval | Decision ID and status |
| **Tasks and findings** | Tracker | Task owner | People or authorized proposal intake | Issue key and revision |
| **Chats, summaries, embeddings** | Cache only | Session or index steward | Tools and participants | Reference only, followed by source checks |

**An architecture decision record (ADR)** belongs beside code when it governs repository design. A cross-team decision belongs in the shared register. Link the two records when a decision spans both scopes. Do not maintain two independent copies of its approval status.

**Local policy copies remain subordinate** to the canonical policy page. By contrast, a repository's tests and schemas are sources within their own scope. Location alone does not determine authority. The map does.

**A cache never overrides a source.** If a summary says seven days and the approved requirement says thirty, use the requirement for the target behavior. Preserve the conflicting summary as evidence of drift, not as a competing rule. With authority assigned, define the write path.

## Cache Down, Propose Up

**Agents pull evidence into session context**, then draft proposals. They do not approve durable facts on their own. Editing a task branch or submitting a draft is distinct from publishing policy, merging code, or marking a decision accepted.

```text
Source -> permission-checked read -> session context
Session context -> proposal + base version -> owner review
Owner approval -> controlled publication -> change log
Changed base version -> reconcile proposal -> review again
```

**Attach the base version** before requesting review. A reviewer needs the previous value, proposed value, reason, evidence, and affected systems. Approval must refer to a specific proposal revision, not an evolving chat thread.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Retain exports for thirty days instead of seven."
evidence:
  - "decision:DEC-12 accepted"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**The identifiers above are illustrative.** Store one change-log row per approved logical change with its proposal ID, target records, previous and resulting versions, approver, timestamp, and merge or publication reference. Link individual system audit events to the row instead of replacing their native histories.

**People own the decision.** An authorized publisher or constrained automation applies the approved revision. Limit write credentials accordingly. Instructions alone do not enforce separation between drafting and publication. The same distinction governs retrieval.

## Shared Context Without RAG

**A project map is the first retrieval index.** Maintain one page per project with source IDs, repository locations, tracker keys, authority scopes, and owners. Read the map first, then fetch the relevant record by ID. Use search when the ID is unknown.

### Sidebar: Sample Project Map

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Direct connectors reduce manual copying.** Model Context Protocol (MCP) is an integration protocol for exposing tools and context to AI applications. Use approved wiki, tracker, and repository connectors where supported. A targeted fetch limits irrelevant results, but it does not replace authorization or freshness checks. Follow the MCP security guidance linked under References when selecting connector permissions.

**Exact retrieval has a small setup burden.** It provides citable evidence without a vector database. Its limits are also clear: someone maintains the map, broad questions need additional search, and large pages consume session space. Fetch the relevant section with its surrounding constraints rather than pasting an entire handbook.

**Offline work uses explicit snapshots.** Record the exported revision and label answers as snapshot-based. Do not publish changes until an authorized person or connector checks the current source. Next, make the same policy visible in each interface.

## One Policy, Different Adapters

**Keep one shared policy**, then distribute short tool-specific adapters. Put the approved policy version on line one of every adapter or copied instruction set. Include its source ID and a reviewed local snapshot for sessions without connector access.

**Loading behavior differs by tool.** Codex documents layered **`AGENTS.md`** discovery. Claude Code documents **`CLAUDE.md`**, imports, and project memory. Cline documents **`.clinerules/`** and rule controls. Use their official instruction documentation linked under References. Verify the loaded instructions in your installed version instead of assuming filenames behave identically.

### Sidebar: Sample AGENTS.md Header

```markdown
Policy-Version: v3 | Source: wiki:POL-01 | Status: approved

# Project instructions

Read the project map MAP-01 before starting a task.
Load docs/policy-snapshot.md and record its source revision.
Treat chat memory and search excerpts as caches.
Attach source revisions to every factual proposal.
Use one task branch and one worktree per coding task.
Do not publish policy, approve decisions, or merge your own PR.
Stop on unresolved source conflicts or overlapping writes.
Required checks: tests, documentation review, policy freshness.
Owners: engineering maintainer, product owner, policy owner.
```

**Chat project instructions receive the same header and procedure.** A non-coder receives the policy snapshot and project map through approved uploads or connectors. If their interface lacks live access, a person supplies the versioned export and records the limitation.

**A version label is a claim, not proof of identical content.** Generate adapters from the approved snapshot or compare their policy portions against a stored digest. Review adapter-specific exceptions separately. Check for disabled rules, nested overrides, and personal instructions during the pilot. Then capture the evidence used by each task.

## Record a Context Manifest

**A context manifest explains the answer's evidence.** Record page IDs and revisions, issue keys and their revision or update time, and full repository commit IDs. Include retrieval time and relevant sections. Mark unavailable records rather than substituting a remembered summary.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook not retrieved. No runbook change proposed."
```

**The commit value is synthetic.** Replace it with the inspected commit in a real manifest. Add the retrieval timestamp during the actual read. A record created before inspection is a checklist, not evidence.

**Citations support checking**, not automatic trust. Point each material claim to its supporting record and section. If two sources disagree, keep both in the manifest and report the unresolved gap. Do not choose the newest timestamp without checking scope and approval status. This evidence discipline also applies to semantic retrieval.

## Shared Context With RAG

**Retrieval-augmented generation (RAG)** supplies retrieved material to a model while it produces an answer. A semantic index helps find relevant passages even when the question uses different wording. Microsoft's RAG overview describes grounding, retrieval constraints, and access-control requirements. See References for the official source.

**Use RAG for discovery across larger collections**, including legacy documentation, meeting notes, and transcripts. Label document classes and approval states. A transcript indexed from its original recording is a source for what participants said, not authority for approved requirements. Do not promote conversation into policy through indexing.

| Index rule | Required behavior |
|---|---|
| **Ingest sources, not caches** | Exclude generated summaries and untracked local copies |
| **Preserve provenance** | Store source ID, revision, section, and document status per chunk |
| **Refresh on change** | Re-index edits and invalidate obsolete chunks |
| **Honor access changes** | Update permissions and remove deleted or revoked content |
| **Return citations** | Expose record references alongside retrieved text |
| **Check the live record** | Fetch current evidence before proposing consequential action |

**A retrieved chunk acts as a pointer in this framework.** Its text helps locate evidence. The live source confirms current wording, approval, surrounding exceptions, and access. If live retrieval fails, label the snapshot and stop the consequential action. This is a governance rule, not a claim about every RAG implementation.

**Stale embeddings and missing context create separate risks.** An old chunk misses a revision. A current chunk still misleads if an exception sits in the next section. Preserve headings and retrieve adjacent constraints before evaluating a requirement.

**Permission leakage deserves its own test.** Enforce authorization before returning chunks to the model, not after generating the answer. Screen sensitive content before indexing or external embedding calls. Account for copied text in logs, model requests, and retrieval traces. Choosing a local model does not make a remote connector local. These checks determine whether RAG belongs in the pilot.

## Choose Map, RAG, or Both

**Match retrieval to the question.** A known requirement ID favors direct access. An open question about scattered historical material favors search. Start with the map unless discovery is already a measured problem.

### Sidebar: RAG or Not?

```text
Do tasks usually name a project, page, issue, or file?
  Yes -> Is direct retrieval sufficient for the pilot?
           Yes -> MAP ONLY
           No  -> HYBRID: map for known IDs, RAG for discovery
  No  -> Is evidence scattered across a large collection?
           No  -> MAP ONLY, plus native search
           Yes -> Is work exploratory and read-only?
                    Yes -> RAG-LED ONLY for discovery
                    No  -> HYBRID with live-source checks

Every option retains owners, authorization, and provenance.
RAG-led discovery still checks sources before durable action.
```

**RAG-only describes the retrieval interface**, not a permission to skip governance. Use it for a bounded exploratory collection where direct source checking remains available. It is a poor choice for known-ID changes which need precise version checks.

**The hybrid model separates discovery from verification.** The map handles known lookups. RAG locates unfamiliar records. RAG answers “where.” The source answers “what.” For the retention example, fetch **`REQ-17`** directly. For “which older export decisions explain this limit?”, search the register and fetch each relevant decision. Now put the repository side into practice.

## Information Inside the Repository

**Repository knowledge changes with implementation.** Keep a compact structure so an agent and a reviewer know where to look.

| File or directory | Responsibility |
|---|---|
| **`CONTEXT.md`** | Project terms and links to authoritative records |
| **`docs/adr/`** | Accepted repository architecture decisions |
| **`docs/design/`** | Approved descriptions of system behavior |
| **`docs/plans/`** | Proposed implementation plans with explicit status |
| **`AGENTS.md`** | Review gates, boundaries, and owner roles |
| **`README.md`** | Setup and entry points, not duplicate requirements |

**Apply the same-PR rule:** change code and affected repository docs together. If no knowledge-base update is needed, require a written exception in the PR description or agreed commit-trailer location.

```text
KB-Update: none (reason: internal refactor preserves documented behavior)
```

**The pipeline enforces the declaration.** A required check rejects behavior changes without documentation updates or an exception. A human documentation owner reviews the exception. A path-based check identifies candidate changes, but it does not prove semantic completeness. Require the check and review through branch protection or the equivalent merge control.

**A gate absent from the pipeline is not a gate.** Naming “documentation review” in an instruction file supplies guidance only. Test enforcement by submitting a deliberately incomplete PR in the pilot and confirming merge remains blocked.

**Use one task, one branch, one worktree.** Git's official worktree documentation describes separate working trees with their own checked-out state. Separate worktrees reduce local editing collisions. They do not prevent two branches from changing the same file or two agents from updating one wiki page.

**Never commit directly to the default branch**, whether it is named **`main`**, **`master`**, or something else. Report requirement-versus-code gaps in the tracker. Attach the conflicting records and let their owners resolve intended behavior before aligning either side. Apply equivalent controls outside Git.

## Information Outside the Repository

**The wiki needs a documentation standard.** Each authoritative page carries purpose, status, owner, revision, review date, and related source IDs. Put proposals in a drafts area with a clear non-authoritative label. Do not mix proposed wording into an approved requirement page.

**Safe updates follow a fixed sequence:**

1. **Reread** the current page and surrounding constraints.
2. **Compare** its version with the proposal's base version.
3. **Reconcile** intervening edits and obtain renewed approval for changed wording.
4. **Write** the approved revision with an expected-version condition.
5. **Verify** the saved page and add the change-log reference.

**Rereading alone does not eliminate races.** Use the system's conditional-update mechanism where available. Without one, serialize publication through a single owner and verify the result. Stop if another writer changes the base during review.

**The no-delete rule applies to agent workflows.** Agents propose archival or removal. Authorized humans apply retention and deletion procedures. Do not interpret this rule as permission to retain sensitive information indefinitely.

**Tracker findings carry evidence**, not only conclusions. Record what you observed, the exact command or inspection method, the inspected commit, expected behavior, actual behavior, and acceptance criteria. Remove secrets and sensitive output before attaching evidence. Mark suggested commands as unrun until someone executes them.

```text
Finding: retention implementation disagrees with approved requirement
Evidence: REQ-17 v8 and inspected config/retention.yaml
Inspection command: git show HEAD:config/retention.yaml
Commit: full inspected commit ID recorded in the manifest
Acceptance: approved duration matches code, tests, and runbook
Status: awaiting product and engineering owner review
```

**The example is a finding template**, not a measured result. Fill it from actual inspection. Keep the wiki update and tracker evidence linked through the proposal ID.

**The decision register separates rules from reasoning.** Store the question, options, recommendation, trade-offs, owner, approval status, and resulting rule reference. Agents propose. People decide. Approved rules go into policy and procedural skills. Their rationale remains in the register.

**Harvest durable facts from meetings and chats.** Submit a proposal with its source evidence, then obtain approval. Until publication, label the agreement tentative. Next, connect approved behavior across the repository and wiki.

## Bridge the Two Systems

**Post-merge sync carries implementation changes outward.** Create a wiki-update task linked to the merged commit, approved requirement, and affected runbook. An agent drafts the update. The wiki owner checks the current page and approves publication. Keep the sync task open until the saved revision is verified.

**Policy freshness is a separate audit.** Compare each repository adapter and chat instruction copy against the canonical approved version. Policy **`v3`** lives at **`POL-01`**. Each **`AGENTS.md`** names **`v3`** on line one. The audit flags **`v2`**, missing labels, and content mismatches despite matching labels.

| Check | Evidence of completion |
|---|---|
| **Policy freshness** | Canonical version and adapter digest comparison |
| **Requirement reconciliation** | Requirement revision compared with code and tests |
| **Post-merge sync** | Merged commit linked to published wiki revision |
| **Conflict resolution** | Owner-approved decision linked to both affected records |

**Reconcile on a schedule or at PR time.** A weekly audit fits a pilot. A behavior-changing PR needs a requirement check before merge. Choose cadence around the cost of drift and record the last successful check.

**The thirty-day change has several checkpoints:** product approves the requirement, engineering updates configuration and tests, reviewers merge the PR, and operations publishes the runbook update. One change-log row links the resulting records. A failed wiki sync remains visible rather than disappearing behind a successful merge. Shared handoffs keep this sequence intact across tools.

## One Procedure, Every Tool

**Package repeated steps as skills or prompts**, with a versioned procedure ID. Share the contract, not a presumed universal file format. Each tool adapter supplies the supported loading or invocation mechanism.

| Procedure | Required output |
|---|---|
| **Start task** | Owner, scope, policy version, source manifest, write reservation |
| **Doc lint** | Missing metadata, duplicated authority, broken source references |
| **Knowledge check** | Requirement-versus-code gaps with supporting revisions |
| **Handoff** | Current evidence, proposals, completed checks, unresolved questions |

**Non-coders work without Git.** They retrieve permitted sources in chat projects, complete the same proposal template, and submit it to the owner through a draft page or tracker task. They do not need a repository checkout to request a requirement correction.

**Coders use repository files and PR gates.** They link the approved proposal in the PR, record inspected commits, and run the required checks. Both groups hand off the same evidence structure.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "Attached source IDs, revisions, and inspected commit"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["RUN-04 publication assigned to operations-owner"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**A handoff is still a cache.** The next person rereads sources before acting and records new revisions. Do not inherit “completed” as proof without checking the linked approval or test evidence. Apply the guardrails below before any write.

## Guardrails Before Every Write

**Screen data before it leaves its home system.** Check classification, connector permissions, approved destinations, model-provider handling, and logging. Send the minimum relevant content. Keep restricted records out of unauthorized chat projects and embedding services.

**Retrieved text is evidence, not an instruction channel.** A wiki page or tool response telling an agent to ignore policy does not change its authority. Review content-origin instructions separately from the approved operating policy. Limit connectors to read access during retrieval and separate publication credentials from session access.

**Assign one active owner per page or file.** Record the reservation in the task tracker with scope and expiry. Reread before writing and use version checks. Separate worktrees help local isolation, while reservations and conditional writes address shared records.

| Stop-and-ask trigger | Required response |
|---|---|
| **Sources disagree without an owner** | Pause and request authority assignment |
| **Another task reserves the target** | Negotiate ownership before editing |
| **Base version changed** | Reconcile and request renewed approval |
| **A material claim lacks evidence** | Mark it unverified and request a source |
| **Data handling is unclear** | Keep content in its home system |
| **Live source access fails** | Record snapshot limits and pause durable action |

**Prompts are not security controls.** Test permission denial, protected branches, stale-base rejection, and write ownership outside the model. A compliant demonstration is insufficient if the account still has unrestricted publication rights. Use those tests to decide whether the pilot is ready.

## Pilot Before Promotion

**Start the framework as a draft.** Pilot one project with a coder, a non-coder, and named source owners. Run the same known-ID question through two tools, then run a deliberate source-conflict exercise. Review the manifests and proposals rather than grading prose fluency.

**Expected reasoning:** both participants identify the current approved requirement and separately describe inspected implementation. If they disagree, compare their manifest entries first. This is a proposed exercise, not an observed benchmark.

| Metric | Definition |
|---|---|
| **Citation rate** | Source-supported material claims divided by material factual claims in sampled outputs |
| **Weekly drift findings** | Confirmed authority or version mismatches, grouped by source type |
| **Proposal turnaround** | Median time from review-ready proposal to recorded decision |
| **Stale-context rework** | Reopened tasks attributable to obsolete or unverified evidence |

**Measure a baseline before setting targets.** More drift findings during the first week might reflect better detection rather than worse documentation. Track recurrence and resolution time alongside the raw count. Review sensitive evidence without copying it into analytics exports.

**Ship an example repository during rollout.** Include a synthetic map, policy adapters, manifests, proposal templates, documentation exceptions, and executable review checks. Use mock wiki and tracker records, with no production credentials. Demonstrate denied publication, changed-base rejection, policy-version drift, and a successful handoff.

**A template repository is a rollout deliverable**, not an asset supplied with this article. Promote the operating model after leadership and source owners review the pilot results. Keep exceptions and unresolved failure cases in the decision register. Before promotion, repair the predictable failures below.

## Troubleshooting Shared Context

| Symptom | First repair |
|---|---|
| **Two tools answer differently** | Compare source IDs, revisions, scope, and approval status |
| **Instructions seem current but behavior differs** | Inspect loaded adapters, rule toggles, and local overrides |
| **RAG returns old requirements** | Inspect index refresh and fetch the live page |
| **A wiki edit erases another change** | Require conditional writes or serialized publication |
| **Docs checks pass with stale wording** | Add owner review and a requirement reconciliation check |
| **Decisions remain in chat** | Assign proposal intake and register ownership |

**Fix the evidence path before rewriting the prompt.** Then rerun the failed pilot case and record the result. Use the checklist below to turn the repaired process into a repeatable weekly practice.

## Ten Steps This Week

1. **Choose one pilot project** and its participating people and tools.
2. **Assign a home and owner** to each information type.
3. **Publish a project map** with source IDs and authority scopes.
4. **Draft one shared policy** and obtain owner review.
5. **Version each instruction adapter** on line one and verify it loads.
6. **Require a context manifest** for material factual answers and proposals.
7. **Create a proposal intake path** with base versions and named approvers.
8. **Enforce write controls** and the same-PR documentation rule.
9. **Test drift, conflict, and handoff** using synthetic records.
10. **Review pilot metrics** and approve the next rollout stage.

**Give every fact one home, make every tool read from the home, and route every durable change through a person.**

## References and Next Steps

**Official documentation supports the technical components**, not the framework's organizational rules. Check installed tool behavior and connector permissions during your pilot.

- **Codex instructions:** [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md), covering instruction discovery and verification.
- **Claude Code instructions:** [How Claude remembers your project](https://code.claude.com/docs/en/memory), covering project instructions and memory.
- **Cline instructions:** [Rules](https://docs.cline.bot/customization/cline-rules), covering workspace rules and activation controls.
- **Retrieval design:** [Retrieval-augmented generation in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), covering grounding, retrieval constraints, and security.
- **Connector security:** [MCP Security Best Practices](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), covering authorization and connector risks.
- **Working-tree isolation:** [Git worktree documentation](https://git-scm.com/docs/git-worktree), covering separate working trees and their shared repository state.

**For local inference planning**, read the [Local AI GPU Context Guide](/articles/local-ai-model-gpu-context-guide/). Hardware capacity and shared-source governance solve different problems. A larger context window does not repair conflicting authority.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Read the Local AI Context Guide
{{< /centerbutton >}}