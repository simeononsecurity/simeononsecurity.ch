---
title: "Lesson 4: Auto-Routing AI Requests: Mix Local and Cloud Models Behind One API"
date: 2026-10-21
lastmod: 2026-10-21
toc: true
draft: false
description: "Send one auto request and let the broker, not the agent, pick a local GPU model or a remote premium model using capability filtering, cost tiers, cascade, latency budgets, and placement pinning."
genre: ["Local AI", "AI Infrastructure", "Self-Hosted AI", "Developer Tools"]
tags: ["auto routing AI", "AI model router", "local and cloud AI", "model auto", "OpenAI-compatible broker", "LLM router", "self-hosted AI", "cost-based routing", "cascade routing", "latency budget", "data residency", "placement pinning", "capability filtering", "GBNF classifier", "heuristic router", "cost tier", "model registry", "Ollama", "vLLM", "llama.cpp", "local LLM", "AI broker", "hybrid AI routing", "LLM cost optimization", "AI gateway", "fail-closed routing"]
cover: "/img/cover/ai-auto-router-local-cloud-mix-2026.webp"
coverAlt: "A single API endpoint routing requests to a local GPU model and a remote cloud model on a dark background"
coverCaption: ""
---
[Return to the Hermes Agent and Local AI Course](/hermes-local-ai-broker-course-start/)

**One endpoint. One request field.** An agent sends `"model": "auto"` to a single OpenAI-compatible base URL, and the broker decides which backend answers. The agent never names a local model or a premium model. The broker reads registry data and the request shape, then routes the call to the cheapest backend able to do the work.

This article explains how the broker's `auto` router makes a local or premium choice, how to shape it with registry fields and headers, and how to write a routing policy for your own mix of backends. The evidence here comes from a reference broker at **v0.6.0**. Behavior marked **tested** was run against the broker's fake backend offline during preparation. Behavior marked **doc-cited** comes from the shipped documentation and source without a live run here.

*The thesis is simple: placement is a broker decision driven by registry data, not an agent decision driven by prompt logic.*

<!--more-->

## Key Takeaways

- **One field decides routing.** The agent sends `"model": "auto"`. Registry tags, cost tiers, and placement labels decide the backend.
- **Capability comes before price.** The router filters to backends able to serve the request, then prefers the cheapest survivor.
- **Cascade escalates once.** A cheap model answers first. One quality signal promotes the retry to a stronger model.
- **Placement pinning fails closed.** A request with no compliant backend returns `403`, never a silent spill to a non-compliant one.
- **"Cloud premium" means a remote self-hosted endpoint.** In v0.6.0 the broker fronts OpenAI-compatible backends, not hosted OpenAI or Anthropic APIs.

## Prerequisites

- A running OpenAI-compatible broker in front of your backends. Start with the companion guide, [One Endpoint for Many AI Backends](/hermes-local-ai-broker-course/03-openai-compatible-broker/).
- At least two registered backends with different cost and capability, for example a small local model on a GPU box and a larger model on a remote GPU host.
- Comfort editing a YAML registry and sending HTTP headers with your requests.

**Estimated time:** 25 minutes to read. **Difficulty:** intermediate. You should already know how an OpenAI-compatible chat request is shaped.

## What "model": "auto" Changes

Without a router, the agent picks the model name. The caller decides local or premium on every request, and the decision logic lives in application code spread across many agents.

With `auto`, the caller sends one virtual model name. The broker owns the decision. Moving the policy into the broker gives you one place to change cost rules, one audit trail, and one set of guardrails for every agent.

The router runs a fixed sequence for each `auto` request. This sequence is **doc-cited**, and the heuristic path was observed in a live run during preparation.

```text
 request: {"model":"auto", messages, headers}
        |
        v
 1. capability filter   drop backends missing a required capability
        |               (tools, vision, context length, placement labels)
        v
 2. hard overrides      a matched rule forces a specific model
        |               (when has_images -> vision model, etc.)
        v
 3. classifier          heuristic (pure Python) OR GBNF-constrained GGUF
        |               produces a request class and candidate ranking
        v
 4. validate + score    cheapest capable candidate wins under the weights
        |               (capability, cost, prefer_loaded, priority)
        v
 5. deterministic       no valid pick falls back to router.default
    fallback
        |
        v
 chosen backend  ->  x-broker-route header names the winner
```

## The Capability Filter Runs First

Stage one removes any backend unable to serve the request. A request with image parts drops every text-only model. A request asking for tool calls drops models without tool support. A long input drops models with a smaller context limit. A placement header drops backends without the required label.

The classifier never sees an incapable backend. This ordering matters: the router never has to "know" a weak model lacks vision, because the filter removed it before scoring. **Capability is a hard gate. Price is a tie-breaker among survivors.**

## Heuristic vs GBNF Classifier

The router ships two classifier backends. Both answer the same question: which registered model should serve this request?

| Backend | How it decides | Cost and honesty |
|---|---|---|
| **Heuristic** | Pure-Python keyword and structural rules. Default in CI and as a fallback. | No model file, near-zero latency. The documentation calls it a cheap default, not a strong classifier. |
| **GBNF-constrained GGUF** | A small llama.cpp model answers under a grammar restricting output to the exact candidate ids. | Needs the bundled-router image or a mounted GGUF. An invalid answer is impossible because the grammar only permits a candidate id. |

The grammar approach has one property worth stating plainly. The candidate list is injected at inference time, so adding or removing a model needs no retrain. The grammar forces the answer to be one of the current candidate ids, one to three tokens long.

> **Honesty note:** the project's own evaluation of the heuristic classifier reports strong results for chat and creative prompts and weak results for hard reasoning, with a blind-set reasoning score near 0.44 in the project's own evaluation suite. These numbers are measured by the project, not verified here. Treat the heuristic as a cost-saver for easy traffic and reach for the GBNF backend or cascade on hard code, math, and reasoning.

The heuristic backend was run here. The GBNF path is **doc-cited**, not tested on this machine.

## Cascade: Serve Cheap, Escalate Once

Capability filtering picks a single model per request. Cascade mode changes the shape. It serves the cheapest capable model first, inspects the answer, and escalates one step when a signal says the answer is weak.

Set `router.mode: cascade` in the registry. The escalation signals include:

- **Truncation** means the first answer stopped with `finish_reason == "length"`.
- **Too short or empty** means the answer is shorter than a configured `min_chars`.
- **Refusal** means the answer matches a refusal regex.

The response carries an `x-broker-route` header showing the path, for example `tiny->coder`. **One escalation is the cap.** Cascade never walks an unbounded chain of models.

A newer option adds a calibrated reliability scorer. It aggregates length and logprob features into one score in the zero-to-one range and escalates when the score falls below a threshold. The documentation is explicit: the scorer is a heuristic aggregator, not a trained model. Both cascade modes are **doc-cited** here.

## Latency Budget Routing

Some requests are interactive and need a fast first token more than a strong answer. A latency budget tells the router to prefer the fastest capable candidate.

Set the budget three ways, in order of precedence:

- Per request, send the `x-broker-latency-budget-ms` header.
- Per virtual model, set `router.latency_budget_ms` in the registry.
- Globally, set the `BROKER_ROUTER_LATENCY_BUDGET_MS` value.

The router estimates service time from recent usage-log percentiles plus a cold-start penalty. Streaming requests use time-to-first-token. Non-streaming requests use end-to-end time. **A budget never overrides capability or placement.** The router will miss a budget before it serves an incapable or non-compliant backend. This behavior is **doc-cited**.

*The project's routing latency figures come from a discrete-event simulation, not field measurement. Treat published millisecond numbers as simulated.*

## Placement and Data-Residency Pinning

Placement is the control for regulated and location-sensitive traffic. Each backend carries `placement` labels in the registry. A request carries required labels through the `x-broker-placement` header or the `BROKER_DEFAULT_PLACEMENT` setting.

The rule is strict. Only a backend carrying every required label is eligible. If no backend qualifies, the broker returns `403 placement_denied`. It never spills to a non-compliant backend.

This was **tested** during preparation. A request with `x-broker-placement: cloud` routed to the cloud-tagged model. A request with `x-broker-placement: region:eu`, a label no backend carried, returned HTTP `403` and never fell through to a local or cloud model.

> **Why fail-closed matters:** a data-residency control which silently picks a non-compliant backend is worse than no control. The `403` is the correct answer when nothing compliant is available.

## The Registry Control Surface

Every routing decision is driven by registry data, not agent code. Five fields shape the `auto` pick:

- **`tags`** label capability and category, for example `chat`, `code`, `math`, `reasoning`, `vision`, `cheap`, and `fast`.
- **`cost_tier`** is an integer from 1 (cheapest) to 5 (most expensive).
- **`priority`** breaks ties when cost and capability match.
- **`placement`** holds the data-residency labels described above.
- **`router_eligible`** keeps a model out of `auto` selection when false.

A sixth setting shapes the scoring math. Since v0.6.0 the `cost_normalized` weight defaults to true. It normalizes cost into a zero-to-one factor so a single capability match outranks a cheaper price. Without it, a warm cheap model would win code, math, and reasoning work it should not take.

## The Cost-Routing Decision Table

This table is the core of the article. Each row maps a request class to a preferred tier and the registry or config mechanism which enforces it. Every mechanism is data, not agent logic.

| Request class | Preferred tier | Enforcing mechanism |
|---|---|---|
| **Trivial chat, greeting, short creative** | Cheapest local (`cost_tier: 1`) | `auto` picks the cheapest capable model. `cost_normalized` keeps cost a tie-breaker. |
| **Code, math, hard reasoning** | Capable mid or high tier | Capability-first scoring, or `router.mode: cascade` to escalate once, or the GBNF router for better routing. |
| **Tool or function calling** | A tool-capable model | Capability filter plus an override such as `when {has_tools: true} use <tool-model>`. |
| **Vision or image parts** | A vision-capable model | Capability filter removes text-only models, plus `when {has_images: true}`. |
| **Long context (32k or more)** | Long-context model | Override `when {min_ctx_tokens: 32000} use <long-ctx-model>`. |
| **Interactive, latency-sensitive** | Fastest capable within budget | `x-broker-latency-budget-ms` or `router.latency_budget_ms`. |
| **Regulated or data-residency** | Only compliant placement | `placement` labels plus `x-broker-placement`, fail-closed `403`. |
| **Key barred from paid tier** | Local only | Per-key `allowed_models`, applied to the `auto` pick and each cascade hop. |
| **Budget-capped key** | Whatever stays under budget | Per-key daily or monthly cost budget, returns `429` when exceeded. |
| **Repeated identical prompt** | No model at all | Response cache returns the stored answer with no inference. |

Read the table as a policy worksheet. For each class your agents send, pick the tier and the mechanism which enforces it. The mechanisms compose. A single request matches a placement rule, a latency budget, and a cost tier at once.

## A Worked Example: Cheap Local Plus Premium Cloud

This example shows the thesis directly. Two backends, one virtual `auto` model, and the broker alone deciding local or premium.

The registry registers a cheap local model and a premium "cloud" model. An override sends long inputs to the cloud model regardless of cost.

```yaml
router:
  default: local-small
  weights:
    { capability: 3.0, cost: 1.0, prefer_loaded: 1.0, priority: 1.0, cost_normalized: true }
  overrides:
    - when: { min_ctx_tokens: 32000 }
      use: cloud-frontier
models:
  - alias: local-small
    backend: ollama
    base_url: http://YOUR_GPU_HOST:11434
    runtime_model_id: tiny-chat-v1
    tags: [general, cheap, fast, chat, creative]
    cost_tier: 1
    priority: 1
    placement: [local]
  - alias: cloud-frontier
    backend: vllm
    base_url: https://YOUR_CLOUD_GPU_HOST/v1
    runtime_model_id: frontier-v1
    tags: [reasoning, math, general]
    context_limit: 200000
    cost_tier: 5
    placement: [cloud]
```

The agent sends the same request shape every time. Only the content changes.

```bash
curl http://YOUR_BROKER_HOST/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"auto","messages":[{"role":"user","content":"hey there, how are you today?"}]}'
```

What the broker chose in the preparation runs, **tested** against the fake backend offline:

```text
trivial chat                   -> x-broker-route: local-small     (cheap tier wins)
math / reasoning prompt         -> x-broker-route: cloud-frontier  (capability beats price)
x-broker-placement: cloud       -> x-broker-route: cloud-frontier  (only cloud eligible)
x-broker-placement: region:eu   -> HTTP 403 placement_denied       (no model carries it)
```

Both backends were the broker's `fake` backend for the offline test, with the real `backend` and `base_url` values swapped in as placeholders above. The fake backend exercises the full auth, routing, and placement path without a GPU or network. Replace the placeholders with your real hosts in production.

## What This Broker Does Not Do

Three limits keep the article honest.

**No hosted-frontier adapter in v0.6.0.** The broker has no OpenAI or Anthropic API adapter. A "cloud premium" model here is a remote self-hosted OpenAI-compatible endpoint, for example vLLM or Ollama on a cloud GPU, reached by `base_url`. Do not read "local and cloud mix" as fronting a third-party paid API. Fronting hosted APIs is out of scope for this release.

**Router accuracy is project-measured.** The classifier accuracy numbers come from the project's own evaluation suite with a synthetic model catalogue. The honest headline is the blind set: strong on chat and creative, weak on reasoning. These were not re-measured here.

**Routing latency is simulated.** The published millisecond comparisons come from a queueing simulation, not field measurement. Use them for relative intuition, not capacity planning.

## Your Turn: Design a Routing Policy

This is the create-level exercise. Design a routing policy for the scenario below, then compare your reasoning with the expected reasoning. The expected answers are reasoning, not measurements.

**Scenario.** Your team runs a small chat model on a local GPU box and a larger reasoning model on a remote cloud GPU. Three rules apply:

1. Support tickets which contain customer records must stay in your home region.
2. An interactive help widget needs a fast first token.
3. A nightly batch job summarizes long documents with no latency limit.

Write the registry fields and request headers for each rule.

**Expected reasoning (not measured):**

- **Customer records.** Tag the local backend `placement: [region-home]` and send `x-broker-placement: region-home` on ticket requests. A request with no compliant backend returns `403`, which is the correct fail-closed outcome.
- **Help widget.** Send a tight `x-broker-latency-budget-ms` so the router prefers the fastest capable model. Capability and placement still win over the budget.
- **Nightly batch.** Rely on the long-context override (`when {min_ctx_tokens: ...} use <long-ctx-model>`) and skip the latency budget. The cost tier is acceptable because throughput, not latency, is the goal.

Check your policy against the decision table above. Each rule should map to one preferred tier and one enforcing mechanism.

## Next Steps

- Start with the prerequisite: [One Endpoint for Many AI Backends](/hermes-local-ai-broker-course/03-openai-compatible-broker/).
- Add guardrails and per-key budgets in [Governing a Self-Hosted AI Broker](/hermes-local-ai-broker-course/08-broker-governance/).
- Fan one request out to many agent profiles in [Hermes Bot Profiles and Fan-Out](/hermes-local-ai-broker-course/07-bot-profiles-fan-out/).
- See the whole series in [Hermes Agent and Local AI: A Brokerized Workflow](/hermes-local-ai-broker-course-start/).
- Compare local and hosted model capability in [Local AI vs ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/).
- Weigh the GPU economics in [GPU ROI for Qwen 27B](/articles/gpu-roi-qwen27b-mining-vs-api-roi-2026/).

Continue with [Lesson 5: Tailscale Aperture, the Private Edge](/hermes-local-ai-broker-course/05-tailscale-aperture-private-edge/).
