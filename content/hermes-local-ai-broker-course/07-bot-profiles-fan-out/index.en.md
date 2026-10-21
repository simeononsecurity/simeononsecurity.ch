---
title: "Lesson 7: Hermes Bot Profiles: Fan Work Out to Specialized Agents With a Kanban Dispatcher"
date: 2026-10-21
lastmod: 2026-10-21
toc: true
draft: false
description: "Run one gateway with role-specific Hermes profiles, pin each to a model tier, split a job into dependent kanban cards, and verify every handoff before you trust it."
genre: ["Artificial Intelligence", "Software Engineering", "AI Security"]
tags: ["hermes agent", "bot profiles", "kanban dispatcher", "multi-agent orchestration", "agent fan-out", "model tiers", "local AI agents", "dependent tasks", "parent child cards", "agent handoff verification", "researcher writer reviewer", "security gate agent", "private edge", "ai broker", "per-key budget", "orchestrator agent", "specialized agents", "profile model override", "self-hosted AI", "agent workflow"]
cover: "/img/cover/hermes-bot-profiles-fanout-2026.webp"
coverAlt: "Diagram of one gateway dispatching work to researcher, writer, and reviewer profiles across linked kanban cards on a dark background"
coverCaption: ""
---
[Return to the Hermes Agent and Local AI Course](/hermes-local-ai-broker-course-start/)

**One agent in one chat hits a ceiling fast.** A long job mixes research, drafting, review, and a final safety check into a single context window, and quality drops as the window fills. Hermes answers this with **profiles**: each role runs as its own agent with its own memory, skills, and model, and a shared board routes work between them.

This guide shows the pattern from end to end. You will define role-specific profiles, match each profile to a **model tier**, split a large job into **dependent cards** on a kanban board, and verify each result before the work counts as done.

*Read the [Hermes Agent overview](/hermes-local-ai-broker-course/01-hermes-agent-overview/) first if profiles and the gateway are new to you.*

**Learning outcome:** by the end you move from applying this pattern to designing your own fan-out and its verification gate.

<!--more-->

## Key Takeaways

- A **profile** is a separate Hermes home with its own config, memory, skills, credentials, and model.
- The **dispatcher** is a loop inside the gateway, routing each card to the assigned profile.
- **Dependent cards** let parents hold children, so research lands before writing starts.
- A **model tier** comes from each profile's config, and a card overrides it only when it sets its own model and provider.
- A **verification gate** exists because a worker's completion summary is a claim, not proof. An orchestrator or reviewer re-checks it.

## Before You Begin

**Prerequisites:** a working Hermes install with the gateway and kanban enabled, and at least three profiles you create during this guide. Set aside 45 minutes. Difficulty is intermediate.

You also need a model endpoint each profile reaches. Use a local model behind a [private edge and broker](/hermes-local-ai-broker-course-start/) or a cloud provider key.

## Why Fan Work Out

One profile per role beats one agent per job for three reasons.

- **Context stays clean.** Each agent loads only the skills and memory its role needs, so the review step never wades through the drafting chatter.
- **Models match the task.** A cheap local model drafts and summarizes. A long-context or cloud model handles the hard review.
- **Work runs in parallel.** Independent research cards run at the same time instead of queuing in one chat.

The cost is coordination. You now own naming, dependencies, and a verification step. The rest of this guide covers each.

## One Gateway, Many Profiles

A **profile** is a separate Hermes home directory with its own `config.yaml`, `.env`, memory, sessions, skills, cron jobs, and state database. Hermes treats a directory as a profile when it carries an identity file. Creating a profile also registers a command alias, so a profile named `researcher` answers to `researcher chat` and `researcher gateway start`.

Keep the related names distinct, because they solve different problems.

- A **Bot** is the same profile primitive with a roster presentation in the desktop Bot Mode.
- A **messaging bot** is a platform account wired to the gateway, identified by its bot token.
- A **subagent** is a `delegate_task` child with a fresh conversation, not a profile.

Create one profile per role and confirm every name before you assign work to it.

```bash
hermes profile create researcher   # also registers the `researcher` command alias
hermes profile create writer
hermes profile create reviewer
hermes profile list                # confirm each name before you assign work
```

The **gateway** is the long-lived host process. It runs the dispatcher, delivers platform messages, and fires cron jobs. One gateway owns the dispatcher by default. Other per-profile gateways set the dispatch flag to false, so two hosts never race to spawn the same card.

## Match Profiles to Model Tiers

Each profile resolves its model from its own `config.yaml`. Point a role at a cheap tier for bulk work and reserve an expensive tier for the review step.

```yaml
model:
  default: "<MODEL_ID>"          # a model id the endpoint lists
  provider: "custom"             # ollama, vllm, and llamacpp also map to custom
  base_url: "https://<PRIVATE_EDGE_HOST>/v1"
  api_mode: chat_completions     # pin this for an OpenAI-compatible endpoint

model_overrides:
  custom:
    "<MODEL_ID>":
      context_window: 131072     # set the real window when the endpoint under-reports it
```

Set `api_mode: chat_completions` when the endpoint speaks the OpenAI-compatible API instead of a messages API. Pin `model_overrides.<provider>.<model>.context_window` when the endpoint advertises no window or a wrong one, so the agent never falls back silently.

Assign a tier by role. The table below is a generic shape, not one machine's model list.

| Role | Typical tier | Why |
|---|---|---|
| **researcher** | local small or mid model | high volume, short reasoning, cheap to run |
| **writer** | local long-context model | long drafts need a wide window on the private edge |
| **reviewer** | escalated cloud or large model | the judgment step warrants the strongest model |
| **security gate** | escalated cloud or large model | the final safety check is the one place to pay for depth |
| **orchestrator** | mid tier | routing and judging summaries, not heavy generation |

*Spend the expensive tier on the gate, not the draft. A strong model reviewing cheap output beats a cheap model reviewing expensive output.*

The [broker's router](/hermes-local-ai-broker-course/04-auto-routing-local-and-cloud/) sends cheap tiers to local models and escalates expensive tiers to a cloud provider. Enforce the limit with [per-key budgets at the broker](/hermes-local-ai-broker-course/08-broker-governance/), so a runaway card never overspends.

A card inherits its assignee profile's tier unless the card sets its own `model` and `provider`. Create most cards without them and let the profile decide. Override per card only for a one-off escalation.

## Split Work Into Dependent Cards

The board holds the work. A **card** (also called a **task**) is a durable item with an assignee, a status, parents, children, comments, and a handoff. The **dispatcher** is a loop inside the gateway, on a default 60 second tick, which promotes ready cards, claims one atomically, and spawns the assigned profile to run it.

Model the job as a graph. Research cards are **parents**. Writing cards are **children** gated on the research. One final **gate** card depends on every writing card.

{{< figure src="hermes-kanban-fanout-parent-child-cards.webp" alt="Diagram showing two parent research cards feeding two child drafting cards, both feeding one final review gate card" >}}

Create the parents first. Each parent is independent, so the dispatcher runs them in parallel.

```bash
# Parents: independent research. Assignee must be a real profile name.
hermes kanban create "Research: source list for topic A" --assignee researcher
hermes kanban create "Research: source list for topic B" --assignee researcher
```

Capture the id each command returns. Create each writing child gated on its research parent.

```bash
# Child drafting card, held until its research parent reaches done
hermes kanban create "Draft: topic A guide" \
  --assignee writer \
  --parents <RESEARCH_A_ID>
```

Create one gate card gated on every draft. This is where the security review runs.

```bash
# Final gate, held until every draft card is done
hermes kanban create "Review and security gate: full set" \
  --assignee reviewer \
  --parents <DRAFT_A_ID>,<DRAFT_B_ID>
```

Inside an orchestrator agent you build the same graph with tool calls, not the CLI. Call `kanban_create(title=..., assignee="researcher")`, capture the returned id, then `kanban_create(title=..., assignee="writer", parents=[<id>])`. Link two existing cards after the fact with `kanban_link(parent_id=..., child_id=...)`.

A child card stays held in `todo` until every parent reaches `done`. It then auto-promotes to `ready` and the dispatcher picks it up. The original decomposed card stays alive as the parent, so the orchestrator wakes to judge the result once the children finish.

Start the host and watch the board.

```bash
hermes kanban init
hermes gateway start   # hosts the dispatcher by default
hermes kanban watch    # live board view for a human
```

With the graph built and the gateway running, the one piece left is proof.

## Verify the Handoff

A worker ends its run with a completion summary. **Treat the summary as a claim, not as proof.** The worker is reporting what it believes it did. For anything with a side effect, a file written, an upload, a committed change, re-check the real artifact before the card counts as done.

{{< figure src="hermes-handoff-verification-gate.webp" alt="Flow diagram showing a worker completion summary checked by an orchestrator, a reviewer lane, or a review skill before a card is marked done" >}}

Hermes gives you three re-check paths. Pick one per card. Do not skip all three.

- **The held parent.** The orchestrator profile wakes when its children finish and judges their combined output.
- **A reviewer lane.** A worker calls `kanban_request_review`, and a reviewer profile approves with `kanban_complete` or returns work with `kanban_request_changes`.
- **The review skill.** A dedicated review profile loads the `sdlc-review` skill to review kanban handoffs and route verified outcomes.

Run this checklist before you mark any card done.

- [ ] The summary names a concrete artifact, a path, a URL, or an id, not a general claim of success.
- [ ] You opened the artifact and confirmed it exists and meets the card's acceptance criteria.
- [ ] Tests, a build, or a validator ran, and you read the output, not only the exit status.
- [ ] No secret, credential, or host identifier leaked into the summary, the comments, or the committed files.
- [ ] Every child card the work depended on reached `done`, not `blocked` or `review`.

> **Key Takeaway:** a green status line is not verification. The dispatcher reports a worker idle a short time after its run closes, so read the card's terminal event, not the status line, to confirm a run ended.

## Common Mistakes

| Mistake | What happens | Fix |
|---|---|---|
| **Unknown assignee** | silent drop, the card sits in ready forever | ground every assignee in `hermes profile list` |
| **Trusting the status line** | a stale idle state hides an open run | read the card's terminal event |
| **Trusting the self-report** | unverified work ships as done | re-check the artifact independently |
| **Worker writes a protected file** | an approval prompt stalls a headless worker | keep workers off `.env` and config files |
| **Two agents share one home** | compounded memory no one authored | run one profile per agent |
| **Endpoint under-reports context** | silent fallback or a 404 | pin `context_window` and `api_mode` |
| **Missing provider plugin or key** | "Unknown provider" and a silent fall-through | install the provider plugin and a placeholder key |
| **Memory write over the limit** | an error, not a silent drop | consolidate entries in the same turn and retry |

## Next Steps

- Start with the [Hermes Agent overview](/hermes-local-ai-broker-course/01-hermes-agent-overview/) if profiles and the gateway are new.
- Route tiers automatically with the [local and cloud auto-router](/hermes-local-ai-broker-course/04-auto-routing-local-and-cloud/).
- Enforce spend with [broker key governance](/hermes-local-ai-broker-course/08-broker-governance/).
- See the whole stack in the [brokerized workflow master guide](/hermes-local-ai-broker-course-start/).
- Sharpen each role with [agent delegation](/articles/effective-ai-agent-delegation/), [task packets](/articles/effective-ai-task-packets/), [bounded agent loops](/articles/effective-ai-bounded-agent-loops/), and [output verification](/articles/effective-ai-output-verification/).

## Your Turn: Design a Fan-Out

Design a three-role fan-out for a job you run for real. Produce three artifacts.

1. **A role to tier table.** List each role, the model tier you assign it, and one sentence of justification. Spend the expensive tier on the gate.
2. **A card graph.** Write the `hermes kanban create` commands for two parent research cards, two child drafting cards gated on them, and one gate card gated on both drafts. Use real profile names from your `hermes profile list`.
3. **A verification checklist.** Adapt the checklist above to your job. Name the concrete artifact each card must produce and the exact command you run to confirm it.

Expected reasoning: your gate card lists every child as a parent, your drafting cards each name one research parent, and no card trusts a worker's summary without a named artifact and a check command. If a card would mark itself done on a self-report alone, add the missing verification before you run it.

Continue with [Lesson 8: Secure the Broker with Keys and Budgets](/hermes-local-ai-broker-course/08-broker-governance/).
