---
title: "Best AI Agent Harnesses in 2026: Choose by Workflow"
date: 2026-10-06
lastmod: 2026-10-06
toc: true
draft: false
description: "Compare Deep Agents, Claude Agent SDK, OpenAI Agents SDK, Pydantic AI, Pi, and LangGraph by tool execution, memory, recovery, and integration effort."
genre: ["Artificial Intelligence", "Software Development", "AI Security"]
tags: ["AI agent harnesses", "best agent frameworks", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "Pi coding agent", "LangGraph", "agent runtime", "tool calling", "agent memory", "context management", "durable execution", "agent permissions", "AI agent security", "local AI agents", "agent evaluation", "human in the loop", "agent SDK comparison", "production agents"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "Modular metallic components connected to a glowing central processor by teal and orange paths on a dark work surface"
coverCaption: "Conceptual illustration of the components surrounding an AI model."
---

**Deep Agents is my first shortlist entry for a general-purpose agent with configurable models and built-in context management.** Claude Agent SDK is a strong fit for embedding Claude Code's execution behavior. OpenAI Agents SDK and Pydantic AI deserve a trial for application-specific agents, while Pi favors a small extensible core and LangGraph favors explicit workflow control.

**The best choice depends on the work you intend to accept.** A research assistant, a repository editor, and a service processing customer requests need different tools and recovery rules. These recommendations are editorial judgments from official documentation checked on **October 6, 2026**, not results from a hands-on performance benchmark.

<!--more-->

## Key Takeaways

- **Choose the abstraction first:** assembled agent, application SDK, or workflow runtime.
- **Check execution boundaries:** tool approval, filesystem isolation, and network policy solve different problems.
- **Test recovery:** conversation history alone does not prevent duplicate external actions.
- **Measure accepted work:** include failures, review time, and infrastructure in your cost comparison.
- **Keep the model explicit:** changing both model and agent software tests the complete system, not the software alone.

## What a Harness Provides

An **agent harness** is the software surrounding a model call. It prepares context, exposes tools, executes approved actions, feeds results back, and decides when to continue or stop. Depending on the implementation, it also manages memory, delegation, permissions, and recovery.

A **model** proposes the next action. A **tool** performs an operation. A **runtime** runs and preserves the workflow. These responsibilities overlap in packaged products, but separating them helps you identify missing capabilities.

| Component | Question to ask |
|---|---|
| **Context management** | Which requirements survive a long run? |
| **Tool execution** | Who validates arguments and limits authority? |
| **State storage** | What survives a process restart? |
| **Verification** | What evidence establishes completion? |

Consider an **illustrative support agent** asked to inspect an order and prepare a replacement request. Reading the order, proposing a replacement, and submitting it should have separate authority. A persuasive explanation does not establish permission to submit, and a saved transcript does not establish whether submission already happened.

**Scope:** this guide compares embeddable software and runtime choices. For daily developer interfaces, use the separate [CLI coding-agent comparison](/articles/cli-coding-agents-comparison/) or [GUI coding-agent comparison](/articles/gui-coding-agents-comparison/). An SDK comparison should not silently become a ranking of terminal tools against editor extensions.

## The Practical Shortlist

| Starting requirement | First option to evaluate | Main responsibility you retain |
|---|---|---|
| **General-purpose agent** | Deep Agents | Configure backend, permissions, and model |
| **Claude Code in an app** | Claude Agent SDK | Operate and isolate the execution process |
| **Application tool workflow** | OpenAI Agents SDK | Define tools, approvals, and acceptance |
| **Typed Python application** | Pydantic AI and its Harness package | Select capabilities and workspace |
| **Minimal embeddable coding core** | Pi SDK | Assemble extensions and execution policy |
| **Explicit durable workflow** | LangGraph | Design graph state and recovery behavior |

**These are different starting points.** Deep Agents already uses LangGraph, so choosing them is not necessarily an either-or decision. Pydantic AI also separates its core agent framework from assembled harness capabilities. Compare the amount of application code you need to own, rather than treating every row as an interchangeable library.

## Deep Agents: Assembled Capabilities

**Choose Deep Agents first for an agent working across files, tools, and long conversations.** Its [official overview](https://docs.langchain.com/oss/python/deepagents/overview) documents filesystem backends, context offloading, summarization, subagents, and human approval. It builds on LangChain and the LangGraph runtime, with integrations for multiple model providers.

**Configuration still determines behavior.** The current documentation makes task planning opt-in starting with version 0.7. Do not assume a tutorial for an older release describes the current defaults. Record the package version and enabled middleware in your evaluation.

**Inspect permission scope carefully.** The documented filesystem rules cover built-in file tools, not arbitrary shell commands through sandbox backends. A file-tool denial is insufficient if another execution path reaches the same file. Test the backend and the shell boundary together.

**My recommendation:** shortlist it for a document-analysis or repository-work service when you want assembled capabilities and provider choice. Prefer a smaller starting point when the job consists of two narrowly defined API calls and a validated response. Extra tools introduce extra behavior to evaluate.

## Claude: Embedded Execution

**Choose Claude Agent SDK when you want Claude Code's agent inside your application.** Anthropic describes a Python and TypeScript library using the same execution loop, tools, and context management as Claude Code. The SDK runs the Claude Code binary in a process you operate. It is distinct from Anthropic's basic API client and hosted Managed Agents. [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview).

**The attraction is reuse of an existing execution system.** File operations, commands, hooks, permissions, sessions, and subagents arrive as documented capabilities. Your integration supplies the application boundary and task-specific acceptance checks.

**Hosting remains an engineering decision.** Anthropic's [deployment guidance](https://code.claude.com/docs/en/agent-sdk/secure-deployment) discusses filesystem controls, network restrictions, and isolation. Configure those around the process rather than treating a permission prompt as an operating-system boundary.

**My recommendation:** evaluate it for Claude-centered document or coding automation with substantial file and command work. Choose a provider-flexible alternative if comparing local models and several hosted providers is a core product requirement.

| Assembled option | Integration emphasis |
|---|---|
| **Deep Agents** | Model selection, middleware, and backend configuration |
| **Claude Agent SDK** | Claude Code execution inside an application process |

## OpenAI: Application Tool Workflows

**Choose OpenAI Agents SDK for an application organized around functions, delegated tasks, and explicit outputs.** Its [overview](https://openai.github.io/openai-agents-python/) documents the agent loop, handoffs, guardrails, tracing, and sandbox-agent capabilities. The SDK is a builder's interface, distinct from the Codex developer application.

**Approval is configurable behavior.** The [human-in-the-loop guide](https://openai.github.io/openai-agents-python/human_in_the_loop/) describes interrupted runs and serialized state for resuming after a decision. For local shell and patch tools, approval is opt-in. Adding an approval callback alone does not enable the approval requirement.

**Model support extends beyond OpenAI.** The [provider documentation](https://openai.github.io/openai-agents-python/models/) describes external-provider integration points and adapters. Validate structured outputs, tool calling, and transport support for your selected endpoint instead of assuming feature parity.

**My recommendation:** shortlist it for a service whose useful actions already exist as well-defined application functions. For example, retrieve an order, calculate eligibility in ordinary code, and prepare a structured request. Keep authorization and eligibility checks in the application even when the model selects the next tool.

## Pydantic AI: Typed Applications

**Choose Pydantic AI when Python types and validated outputs are central to your application.** Its [core documentation](https://pydantic.dev/docs/ai/overview/) covers typed tools, dependency injection, structured outputs, and durable-execution integrations. Validation establishes the output's required structure. It does not establish the truth of every field.

**The separate Harness package adds assembled capabilities.** Its [documentation](https://pydantic.dev/docs/ai/harness/) includes Coder and Researcher stacks, filesystem and shell access, memory, and workspace integrations. A local workspace and an isolated sandbox are different execution choices. Relevant harness capabilities require a workspace rather than silently selecting one.

**My recommendation:** shortlist the core framework for a Python service returning typed records. Add harness capabilities when the task also requires workspace exploration or open-ended research. This keeps a bounded extraction service from inheriting shell access without a concrete need.

For an **illustrative invoice-review agent**, schema validation checks whether a total is numeric and a currency belongs to an allowed set. Separate application logic compares the total against line items and verifies source evidence. Both checks belong in the trial.

| Application concern | Acceptance check |
|---|---|
| **Structured output** | Validate fields and independently verify their meaning |
| **Approval pause** | Persist the exact pending action and decision |
| **Provider change** | Repeat tool-call and output compatibility tests |

## Pi: Small Extensible Core

**Choose Pi's SDK when you want direct control over a compact coding-agent implementation.** The [project documentation](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) describes SDK and RPC integration alongside its interactive interface. Its default tool set consists of reading, writing, editing, and shell execution, with extensions for additional behavior.

**Minimalism shifts work to the integrator.** Pi deliberately omits built-in permission popups and subagent orchestration. Its documentation directs users toward containers or custom extensions for confirmation flows. Evaluate the embedded SDK here, not its terminal interface against another vendor's graphical editor.

**My recommendation:** shortlist Pi for a bespoke coding service when you are prepared to own execution restrictions, extension review, and recovery policy. Its small core is attractive for understanding and changing behavior. It is a less suitable starting point when your main requirement is an already assembled approval and orchestration system.

## LangGraph: Explicit Workflow Control

**Choose LangGraph when the workflow itself needs explicit state and transitions.** Its [persistence documentation](https://docs.langchain.com/oss/python/langgraph/persistence) distinguishes thread-scoped checkpoints from cross-thread stores. A persistent checkpointer supports recovery across process restarts. An in-memory checkpointer does not.

**LangGraph is a runtime foundation.** You define the workflow and decide where model-driven behavior belongs. Deep Agents already uses this foundation, so dropping to LangGraph makes sense when you need more direct control over execution paths.

**My recommendation:** shortlist it for a process with named stages, review pauses, and distinct recovery rules. A document-intake workflow might extract fields, validate them, request review, and publish an approved record. Fixed transitions are useful when a model should choose content but should not invent the business process.

| Workflow stage | Completion evidence |
|---|---|
| **Extract** | Source-linked candidate record |
| **Validate** | Deterministic checks and exceptions |
| **Review** | Decision attached to the specific candidate |
| **Publish** | External receipt recorded against the operation |

**External effects need their own recovery design.** Saving graph state does not make a remote service transaction atomic with the checkpoint. Use an operation identifier and reconcile the external result before retrying a submission.

## Test the Missing Pieces

**A feature list is only a starting point.** Run each candidate through failures which resemble your workload. Use a disposable workspace and test services with synthetic records.

| Test | Evidence to retain |
|---|---|
| **Interrupted submission** | One external effect after recovery |
| **Long conversation** | Original requirements still satisfied |
| **Rejected action** | No effect through an alternate tool |
| **Untrusted document instruction** | Document text does not acquire authority |
| **Malformed tool arguments** | Rejection before application mutation |
| **Budget exhaustion** | Bounded stop with inspectable partial work |

**Define repetition explicitly.** For a replacement-request service, stop the worker after the test service accepts a request but before local completion is saved. On restart, the workflow should look up the operation identifier instead of blindly submitting again. This is a proposed test, not an observed result for the listed products.

**Check evidence after compaction.** Put an important requirement early in the task, then supply enough realistic material to trigger the configured context strategy. Ask the agent to produce its final artifact and supporting source references. Our [CLM and agent-memory analysis](/articles/context-language-models-agent-memory-hallucinations/) explains why retaining notes and retaining accurate evidence are separate concerns.

**Review telemetry destinations.** Tool traces and memory stores often contain task data. Record which systems receive them and how long they remain available. Local model inference does not imply local-only logging, retrieval, or execution.

## Compare Cost Per Accepted Task

**Use two evaluation tracks.** A controlled comparison holds the model, tools, task set, and budgets steady where supported. A deployment comparison uses each candidate's intended configuration. The first isolates some software effects. The second answers which complete setup serves your work better.

**Do not force unsupported configurations into the controlled track.** If two candidates lack a common model or tool interface, report the comparison as a system evaluation. Keep setup effort and human steering in the record.

```yaml
# Illustrative trial record, not a framework configuration file
candidate: "package and pinned version"
model: "provider and exact model identifier"
workspace: "isolated test environment"
task_set: "frozen fixtures and acceptance checks"
limits:
  elapsed_minutes: 15
  model_calls: 30
  tool_calls: 60
record:
  - accepted_result
  - unsupported_claims
  - duplicate_external_actions
  - inference_cost
  - infrastructure_cost
  - human_review_minutes
  - recovery_outcome
```

**Run several trials per task.** Keep unsuccessful attempts in the denominator and report raw counts alongside percentages. A small trial reveals failure patterns, not a stable industry ranking.

**Illustrative cost calculation:** suppose setup A spends $12 across ten attempts and produces eight accepted results. Its inference cost per accepted task is $1.50. Setup B spends $8 but produces four accepted results, so its corresponding cost is $2.00. Neither number includes human review or infrastructure, which belong in a separate recorded total.

**Set disqualifying failures before testing.** An unauthorized submission or cross-user data leak should not disappear inside an average quality score. After enforcing those requirements, compare correctness, recovery, review effort, and cost.

## Make a Bounded Choice

**Start with two candidates and one real workflow.** For an assembled provider-flexible agent, compare Deep Agents with a narrower alternative suited to your application. For Claude Code behavior inside a service, trial Claude Agent SDK. For typed application work, compare Pydantic AI with OpenAI Agents SDK. Choose Pi when custom behavior is worth additional integration work, and LangGraph when explicit workflow control is the priority.

**Prerequisites for the trial:** approved model access, synthetic fixtures, an isolated workspace where needed, and written acceptance criteria. Allow an initial afternoon for setup and basic failure tests, then collect repeated runs before making a production decision. Difficulty is intermediate to advanced, depending on external actions and recovery requirements.

**Select the smallest system which passes your requirements.** Preserve the trial fixtures, package versions, and failure records. Rerun them when changing the model, context strategy, tools, or execution backend. Those changes alter the system you evaluated.

## References

- [LangChain: Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic: Claude Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [Anthropic: Secure deployment](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [OpenAI: Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI: Human-in-the-loop execution](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [OpenAI: Model and provider integration](https://openai.github.io/openai-agents-python/models/)
- [Pydantic: AI framework overview](https://pydantic.dev/docs/ai/overview/)
- [Pydantic: AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Earendil: Pi coding-agent SDK and integration modes](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [LangChain: LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
