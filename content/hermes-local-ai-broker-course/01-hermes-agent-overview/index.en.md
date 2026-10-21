---
title: "Lesson 1: Hermes Agent for Security and Automation: Profiles, Skills, and Bots Explained"
date: 2026-10-21
lastmod: 2026-10-21
toc: true
draft: false
description: "Understand Hermes Agent and its parts — profiles, skills, memory, bots, the gateway, and the kanban board — and learn when the persistent model beats a per-project CLI coding agent."
genre: ["Artificial Intelligence", "Automation", "Self-Hosted", "AI Security"]
tags: ["hermes agent", "hermes profiles", "hermes bots", "bot mode", "ai agent orchestration", "multi-agent", "kanban dispatcher", "agent skills", "progressive disclosure", "persistent memory", "local ai agents", "openai compatible endpoint", "ollama", "vllm", "llama.cpp", "tailscale", "private edge", "ai broker", "cli coding agent", "security automation", "agent profiles", "agent gateway", "scheduled agents", "cron agents", "delegate task", "subagents", "self-hosted ai", "agentskills.io", "model context protocol", "home lab ai"]
cover: "/img/cover/hermes-agent-overview-security-automation.webp"
coverAlt: "Illustration of several labeled agent profiles linked to a shared coordination board and a local model endpoint on a dark background"
coverCaption: ""
---
[Return to the Hermes Agent and Local AI Course](/hermes-local-ai-broker-course-start/)

**Hermes Agent is a persistent agent platform, not a single chat window.** It gives each assistant its own home directory with separate configuration, memory, skills, credentials, and scheduled work. One install runs several named agents at once and coordinates them over a shared board.

**A per-project CLI coding agent lives inside one repository for one session.** Hermes keeps state across sessions and across projects, delivers messages on chat platforms, and runs scheduled jobs on its own. This page defines the parts, maps the terms, and shows when the persistent model earns its extra setup. The claims here come from the Hermes documentation reviewed on **October 21, 2026**.

<!--more-->

## Key Takeaways

- **A profile is a separate agent home**, with its own config, keys, memory, skills, cron jobs, and database.
- **Skills load on demand**, so procedural knowledge enters the prompt only when the work needs it.
- **Memory stays small and always present**, while session search handles unlimited recall.
- **The gateway hosts one dispatcher**, which routes board cards to the profile named on each card.
- **Reach for Hermes over a per-project CLI agent** when work spans sessions, projects, schedules, or several coordinated agents.

## Before You Begin

**Prerequisites:** a working Hermes install and comfort at the command line. You need one model provider, local or hosted, reachable over an OpenAI-compatible endpoint. No kanban or multi-agent experience is required.

**Estimated time:** about 15 minutes to read, and roughly an hour to stand up a second profile and a first board card. **Difficulty:** beginner to intermediate.

**Scope:** this is the first page in the series **Hermes Agent and Local AI: a brokerized workflow**. It covers the agents layer. Later pages cover the private edge, the broker, and the backends.

## What Is Hermes Agent?

**Hermes Agent** is the product. **The agent** is the running assistant answering you. **A profile** is the persistent home the agent reads and writes. Keeping these three terms apart removes most of the confusion around multi-agent setups.

A profile is a separate Hermes home directory under **`~/.hermes/profiles/<name>/`**. Each one holds its own **`config.yaml`**, **`.env`**, **`SOUL.md`**, memories, sessions, skills, cron jobs, and state database. Hermes treats a directory as a profile only when it carries an identity file such as `config.yaml`, `.env`, `SOUL.md`, `profile.yaml`, `auth.json`, or `state.db`. A bare folder left behind by logging is ignored.

The words around profiles have precise meanings. Use the table below as the glossary for the rest of this page.

| Term | Meaning |
|---|---|
| **profile** | A persistent Hermes home with its own config, keys, memory, sessions, skills, cron, and state |
| **agent** | The live assistant using a profile. The product name is Hermes Agent |
| **Bot** | A profile surfaced in the Bot Mode roster with an avatar and a pinned chat |
| **messaging bot** | A Telegram, Discord, or Slack account wired to the gateway by its bot token |
| **subagent** | A `delegate_task` child with a fresh conversation, spawned for a reasoning subtask |

*Every Bot is a profile. Not every profile is a Bot.* The [official Profiles documentation](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) states each of these definitions directly.

## Profiles: One Home Per Agent

**Create a profile and it becomes its own command alias.** A profile named `coder` gives you `coder chat`, `coder setup`, and `coder gateway start` right away. The alias keeps separate agents out of each other's state.

The following commands stand up a second profile. They are untested, illustrative examples drawn from the documented quick start.

```bash
hermes profile create researcher
researcher setup
researcher chat
```

**Keep one agent per home.** Pointing two agent processes at the same profile makes both write memory automatically, and each loads the other's writes into its system prompt at session start. Two writers on one home compound each other's entries into state no one authored. The fix is one profile per agent, with an external memory provider when agents need to share.

**Why a security or automation reader cares:** separate profiles give separate credentials and separate audit trails. A research agent with read-only keys and a deploy agent with write keys never share a `.env`, so a mistake in one does not reach the other.

## Skills: Knowledge on Demand

**Skills are on-demand knowledge documents loaded with progressive disclosure.** The agent lists skills first, opens one when a task matches, and reads a linked file only when it needs the detail. Full content enters the prompt only at the last step, which keeps token use low.

The loading pattern has three levels:

- **`skills_list()`** returns the catalog of names and one-line triggers, around 3,000 tokens.
- **`skill_view(name)`** loads one skill's full `SKILL.md` body when the work calls for it.
- **`skill_view(name, path)`** opens a linked reference, template, or script inside the skill.

Skills live in **`~/.hermes/skills/`**, the source of truth. Bundled skills are seeded on install and on each `hermes update`. Hub-installed and agent-created skills land in the same place, and a profile opts out with a `.no-bundled-skills` marker. The format follows the [agentskills.io open standard](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills), so a skill written for one host reads on another.

> **Key Takeaway:** skills scale knowledge without bloating every prompt. The agent pays the token cost of a procedure only when it runs the procedure.

## Memory Versus Skills

**Memory is a small, always-present fact store. Skills are on-demand procedures.** Mixing the two is a common mistake, so the split below matters. Memory rides in the system prompt on every turn, so it stays tiny. Skills load only when relevant, so they hold the long material.

| Store | What it holds | Size and loading |
|---|---|---|
| **`MEMORY.md`** | Environment facts, conventions, lessons | 2,200 chars (~800 tokens), always in prompt |
| **`USER.md`** | User identity and preferences | 1,375 chars (~500 tokens), always in prompt |
| **skills** | Procedural knowledge | Loaded on demand, no prompt cost until opened |
| **session search** | "Did we discuss X" recall | Unlimited, full-text search over past sessions |

Both memory files sit in **`~/.hermes/memories/`** and are injected as a frozen snapshot at session start. **Memory does not auto-compact.** A write over the character limit returns an error instead of dropping entries silently, so the agent consolidates or removes entries in the same turn and retries. Session search, backed by full-text search over the state database, is the separate tool for unbounded recall. The [Persistent Memory documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) describes both behaviors.

## Bots and Messaging Bots

**A Bot is a profile, with no new primitive to learn.** Bot Mode is a desktop interface over the profile, so a Bot has its own role, model, memory, skills, and avatar, all stored under `~/.hermes/profiles/<name>/`. The CLI reaches the same agent with `hermes -p <bot> chat`, and a Bot's routines appear in `hermes cron list`.

The word "bot" carries two meanings, so keep them apart:

- A **Bot** is a profile shown in the Bot Mode roster. You build a specialist once and it stays available.
- A **messaging bot** is a platform account, such as a Telegram or Discord account, connected through the gateway and identified by its bot token.

A **subagent** is neither of these. It is a `delegate_task` child with a fresh conversation, spawned for a reasoning subtask and gone when the subtask ends. The [Bot Mode documentation](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode) confirms the equivalence between a Bot and the profile behind it.

## The Gateway and the Dispatcher

**The gateway is the long-lived host process.** It delivers platform messages, runs cron and routines, and hosts the kanban **dispatcher** by default. Only one gateway owns the dispatcher, so gateways never race to spawn the same work. Other per-profile gateways set the dispatcher off and keep message delivery profile-owned.

The dispatcher is a loop, default every 60 seconds, with a steady set of duties:

- **Promotes** ready tasks and reclaims stale or crashed claims.
- **Claims** a task atomically so two workers never grab the same card.
- **Spawns** the profile named on the card as its own operating-system process.

**Unknown assignee equals silent drop.** A card whose assignee is not a real profile name is never dispatched and sits waiting with no error. Ground every card in a profile from `hermes profile list` before you create it. This single failure mode causes more stuck boards than any other.

## The Kanban Board: Coordinated Work

**The board turns several profiles into a work pipeline.** Each unit of work is a **card**, with an assignee, a status, parents, children, comments, and a handoff. The dispatcher matches a card's assignee to a profile and runs the matched profile in the card's pinned workspace, with the task identity set in its environment and a guidance block added to its system prompt.

Dependencies gate the flow. A child card waits in the backlog until every parent reaches **done**, then promotes to **ready**. The original decomposed task stays alive as the parent so its orchestrator wakes to judge the result once the children finish.

The documented lifecycle moves a claim through a fixed set of states:

| Stage | Meaning |
|---|---|
| **ready** | Promoted and waiting for a free worker |
| **running** | Claimed, a worker process is active |
| **review** | Handed off for a second check before done |
| **blocked** | Waiting on human input or an external dependency |
| **done / archived** | Terminal, result recorded |

Workers drive the board through a dedicated **`kanban_*` toolset**, not by shelling out to `hermes kanban`. A worker's completion summary is a self-report, not a verified fact. For anything with side effects, such as files written or uploads, the orchestrator or a reviewer lane re-checks the output independently before the work is final. The [Kanban reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban) documents the board, the lifecycle, and the toolset.

## When Hermes Beats a Per-Project CLI Agent

**A per-project CLI coding agent is scoped to one repository for one session.** It is the right tool for focused edits inside a checkout. Hermes adds persistence, scheduling, messaging, and multi-agent coordination, at the cost of more setup. Choose by the shape of the work, not by brand.

| Workload | Better fit | Why |
|---|---|---|
| **One-off edits in a single repo** | Per-project CLI agent | Session-scoped, no standing infrastructure |
| **Work resumed across sessions** | Hermes profile | Memory and skills persist in the profile home |
| **Several agents on a shared task** | Hermes kanban board | Durable cards, parents, and single-owner dispatch |
| **Scheduled or recurring jobs** | Hermes cron and routines | Jobs run under the gateway without a human present |
| **Chat-platform delivery** | Hermes messaging bot | The gateway routes Telegram, Discord, or Slack |
| **Separate credentials per role** | Hermes profiles | Each home has its own `.env` and audit trail |

*For a model-first view of the software around a model call, see the companion guide on agent harnesses in [Next Steps](#next-steps).* The short rule: reach for Hermes when state, schedule, isolation, or coordination outlasts a single session. Keep a per-project CLI agent for bounded, in-repo tasks.

## Where Local Models Fit

**A profile resolves its model from `config.yaml`, so the endpoint is configuration, not code.** Hermes talks to any OpenAI-compatible endpoint through `provider: "custom"`, and the aliases `ollama`, `vllm`, and `llamacpp` map to the same custom path with a `base_url`. One base URL serves every model the endpoint lists.

The series stacks four layers. The agent sits at the top, and each layer below hides a concern from the one above:

- **Agents** are the Hermes profiles and Bots described on this page.
- **Private edge** is **Tailscale Aperture**, a tailnet-identity gateway with no public ports, so only devices on your tailnet reach it.
- **Broker** is one backend-agnostic, OpenAI-compatible endpoint in front of several model servers.
- **Backends** are the serving processes, such as Ollama, vLLM, llama.cpp, or Strata, one endpoint each.

A public edge such as LiteLLM is out of scope for this series, which uses the private, tailnet-only path instead. The following profile snippet points an agent at a private edge. It is an untested, illustrative example, and every value in angle brackets is a placeholder.

```yaml
model:
  default: "<MODEL_ID>"
  provider: "custom"
  base_url: "https://<APERTURE_HOST>/v1"
  api_mode: chat_completions

model_overrides:
  custom:
    "<MODEL_ID>":
      context_window: 131072
```

**Pin the real values when the endpoint under-reports them.** An OpenAI-compatible edge sometimes advertises a wrong context window or expects `/v1/chat/completions` while a profile defaults to a messages API. Set `model_overrides.<provider>.<model>.context_window` and `model.api_mode: chat_completions` to remove the guesswork. A kanban card passing `model=` or `provider=` overrides the profile for the one card.

## Worked Example: Fan Out Work to Two Profiles

**The pattern is one parent card and one gated child.** A research profile gathers sources, then a writer profile drafts from the finished research. The child stays in the backlog until the parent reaches done.

These commands are untested, illustrative examples. Replace every placeholder, and never paste a real host, key, or user path into a card.

```bash
hermes kanban create "Research: retrieval corpus sources" \
  --assignee researcher

hermes kanban create "Draft: corpus ingestion guide" \
  --assignee writer \
  --parents <PARENT_TASK_ID>
```

Inside an orchestrator agent, the same flow runs as tool calls rather than CLI verbs. The agent calls `kanban_create` for the parent, captures the returned id, then calls `kanban_create` for the child with the captured id in `parents`. The writer reads the research through its own `kanban_show`, which returns the parent handoff to treat as ground truth.

Start the host running the board with the following commands. They are untested, illustrative examples.

```bash
hermes kanban init
hermes gateway start
hermes kanban watch
```

> **Expected Result:** the writer card stays in the backlog, then promotes to ready the moment the researcher card reaches done, and the dispatcher spawns the writer profile in the card's workspace.

## Troubleshooting

Common failure modes, each phrased so you recognize it before it costs an hour.

- **Unknown assignee, stuck card.** A card whose assignee is not a real profile never dispatches and surfaces no error. Check the name against `hermes profile list` before creating the card.
- **Status line lags reality.** A gateway reports idle while a worker finishes its final turn, and the dispatcher reaps a finished worker only after a short delay. Read the task's terminal event, not the status line, to confirm a run ended.
- **Self-reported completion is not verification.** A `kanban_complete` summary is a claim. For external side effects, require a path, URL, or id and inspect it before calling the work done.
- **Approval prompts on protected files.** Writing to `.env` or provider config triggers a command-approval prompt, and a headless worker stalls on it. Keep workers off protected files unless the task requires them, and never let a worker type a secret.
- **Two agents, one home.** Sharing a profile between processes compounds auto-written memory into state no one authored. Give every agent its own profile.
- **Endpoint under-reports context or wrong API mode.** An OpenAI-compatible edge advertises a wrong window or expects a different route, producing silent fallback or 404s. Pin `context_window` and `api_mode` explicitly.
- **Memory write rejected.** A memory write over the limit returns an error rather than dropping entries. Consolidate or remove entries in the same turn, then retry.

## Next Steps

You now know the parts of Hermes Agent and the point where the persistent model earns its setup. Continue with the rest of the series and the related guides below.

- Build a roster and fan out work in [Hermes Bots and profiles: a fan-out workflow](/hermes-local-ai-broker-course/07-bot-profiles-fan-out/).
- Put one endpoint in front of several model servers in [The OpenAI-compatible AI broker](/hermes-local-ai-broker-course/03-openai-compatible-broker/).
- Add the tailnet-only private edge in [Tailscale Aperture as a local AI gateway](/hermes-local-ai-broker-course/05-tailscale-aperture-private-edge/).
- Read the full architecture in [Hermes Agent and local AI: a brokerized workflow](/hermes-local-ai-broker-course-start/).
- Compare the software around a model call in [Best AI agent harnesses](/articles/best-ai-agent-harnesses/).
- Write the repository rules your agents read in [Write AGENTS.md and CLAUDE.md for coding agents](/articles/effective-ai-agents-md-context/).
- Start from the basics in the [Practical AI workflow course](/effective-ai-course-start/).

Continue with [Lesson 2: Choose a Backend](/hermes-local-ai-broker-course/02-choose-a-backend/).
