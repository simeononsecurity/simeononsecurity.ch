---
title: "Inside Our Hybrid Agentic AI Fleet: Hermes, LiteLLM, and Tailscale"
date: 2026-10-21
lastmod: 2026-10-21
toc: true
draft: false
description: "See a verified lazy local AI fleet and its staged T0 to T4 control plane with Hermes, LiteLLM, Tailscale Aperture, and Pearl mining."
genre: ["Local AI", "Self-Hosted AI", "AI Agents", "AI Infrastructure", "GPU Mining"]
tags: ["agentic AI fleet", "Hermes Agent", "LiteLLM", "Tailscale Aperture", "Tailscale", "llama.cpp", "Ollama", "Strata", "local LLM", "GPU inference", "GPU mining", "Pearl mining", "lazy loading", "model routing", "T0 T4 models", "Qwen3.5", "Granite 4.2", "Gemma 4", "embeddings", "vision model", "OpenAI compatible API", "self hosted AI"]
cover: "/img/cover/hybrid-agentic-ai-fleet-tailscale-litellm-hermes.webp"
coverAlt: "An anonymized private AI network linking cloud models, a secure gateway, and local GPU servers"
coverCaption: "A tiered agent fleet sends each task to an appropriate model while idle GPUs return to mining"
---

**We deployed a request-scoped local GPU fleet and designed its hybrid control plane.** The verified path starts at LiteLLM, selects a model pool, and loads a local model on one GPU at a time. Hermes tier policy is proposed, and a Tailscale Aperture configuration artifact is ready for the next integration test. Neither is verified as part of one end-to-end route.

Idle cards mine Pearl. An AI request pauses mining only on the leased card, serves the request, unloads the model, and returns the card to the miner.

<!--more-->

## Key Takeaways

- **T0 through T2 handle expensive or demanding work.** These routes favor hosted frontier models and ordered fallback chains.
- **T3 handles substantial local work.** The fleet assigns planning, coding, review, and vision to 4B through 12B models.
- **T4 handles high-volume local work.** Small models route, classify, extract, embed, and complete bounded code tasks.
- **Each GPU is an independent resource.** One card serves AI while the other cards keep mining.
- **Local models stay unloaded while idle.** No model holds GPU memory between request windows.
- **Every gateway exposes the same logical catalog.** Shared aliases spread work across eligible systems. Node-prefixed aliases preserve exact placement when needed.
- **The experimental broker did not enter production.** Its canary served a request, then failed a clean shutdown test. LiteLLM stayed on the verified request-scoped path.
- **Hermes and Aperture remain staged.** Their target design exists, while end-to-end acceptance testing remains open.

**Prerequisites:** Several Linux GPU hosts, stable NVIDIA drivers, a Tailscale tailnet, systemd, a working miner, model storage, and acceptance tests for each model route.

**Time and difficulty:** Advanced. Plan several days for inventory, model downloads, service definitions, routing tests, failure drills, and per-card mining recovery checks.

**Terms used below:** A **tailnet** is the private network formed by Tailscale identities and devices. A **model alias** is a stable model name presented to clients. A **model group** places several deployments behind one alias. A **pool proxy** is the small local service which leases a GPU, starts the model worker, and returns the card to mining.

## The Design Goal

Agentic work arrives in many shapes. A repository repair needs a different model from a title, screenshot, embedding, or intent label. Sending every turn to the largest model wastes money and local capacity. Sending every turn to the smallest model creates retries and weak results.

We wanted one catalog with five workload bands. The policy needed to serve hosted and local models through familiar API formats. Local GPUs needed to stay productive between AI requests.

The fleet also needed concurrency. A multi-card host should serve several independent jobs at once. A request on one card should not stop mining on every card in the chassis.

{{< figure src="hybrid-agentic-ai-fleet-architecture.webp" alt="Anonymized architecture diagram separating proposed Hermes and staged Aperture routing from verified LiteLLM gateways and local GPU workers" caption="The proposed and staged control path sits above the verified LiteLLM and per-GPU execution path" >}}

The diagram uses generic node names. It omits private addresses, user identities, access keys, wallet data, and physical host labels.

## What T0 Through T4 Mean

The tier names are our routing policy. They are not an industry standard and they do not describe model size alone.

| Tier | Primary role | Typical destination | Failure posture |
| --- | --- | --- | --- |
| **T0** | Default coordinator and hardest decisions | Hosted frontier reasoning model | Ordered hosted fallback chain |
| **T1** | High-value worker agents | Hosted high-capability model pool | Retry within the assigned chain |
| **T2** | Broad worker pool | Fast hosted models, with escalation | Escalate difficult work to T1 or T0 |
| **T3** | Substantial private local work | 4B to 12B local chat, code, review, and vision models | Retry an eligible local node, then fail closed for restricted data |
| **T4** | Narrow and frequent local work | 0.6B to 3B routing, classification, code, and embedding models | Retry a local replica or move to T3 inside the same data boundary |

Tiers describe the job before they describe the model. A short security-sensitive classification fits T4. A long repository plan fits T3 or higher. A difficult architectural decision starts higher even when its prompt is short.

This split also changes agent economics. T4 workers absorb repeated low-risk transforms. T3 workers keep common code and analysis inside the tailnet. T0 through T2 remain available for difficult work and failure recovery.

**A data-class gate must precede every hosted fallback.** Public, internal, and restricted jobs receive separate chains. Restricted work stays local and fails closed. A boundary-crossing retry needs sanitized input plus explicit user or workflow approval. Redaction removes credentials, repository secrets, private tool output, and sensitive retrieval content before any hosted call.

## How Hermes Will Own Task Policy

Hermes is the proposed agent layer. The target policy assigns a model class, runs tools, delegates work, and walks explicit fallback chains. Hermes documents separate routes for the main model, auxiliary jobs, delegated agents, and task-specific fallbacks. It also supports custom OpenAI-compatible endpoints through a base URL. See the [Hermes configuration guide](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) and [fallback provider guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers/).

Our policy maps Hermes jobs to stable aliases instead of physical servers. Examples include:

```text
t3-smart
t3-code
t3-review
t3-vision
t4-code
t4-classify
t4-router
t4-embedding
```

The alias expresses intent. Hermes will not need to know which GPU is free, which node has a larger card, or which replica failed its health check. Lower layers own those decisions.

Some work still needs deterministic placement. A node-prefixed model ID sends an operator diagnostic or benchmark to one selected system. Separate Aperture grants should restrict these aliases to operators. Normal agent traffic uses shared tier aliases.

Model access does not secure agent tools. The Hermes rollout needs least-privilege tool allowlists, isolated workspaces, scoped credentials, network egress controls, and prompt-injection handling. Delegated workers should inherit no more access than their assigned job needs.

## Aperture Is the Staged Identity Boundary

Tailscale connects the configured gateway and inference hosts without publishing each service to the public internet. Aperture is prepared as the user-facing boundary and model router. This route still needs an end-to-end acceptance test. Tailscale documents encrypted client access over the tailnet and provider forwarding over TLS in [How Aperture works](https://tailscale.com/docs/aperture/how-aperture-works/).

Aperture also separates reachability from permission. Its grants are deny-by-default. A user or tagged device needs a matching model grant after reaching the gateway. The [Aperture grants guide](https://tailscale.com/docs/aperture/how-grants-work/) explains the additive grant model and identity sources.

The staged Aperture configuration should follow four rules before deployment:

1. **One named identity holds the admin role.** General model access does not grant administration.
2. **Providers list literal model IDs.** Aperture does not infer models from an upstream service.
3. **Provider URLs point at tailnet addresses.** Private node names and addresses stay outside the article and public configuration examples.
4. **Secrets must stay in service-owned files.** Apply owner-only permissions, restricted service accounts, rotation, and log redaction before deployment. Diagnostic output must never print LiteLLM keys, tailnet addresses, subscription tokens, or wallet data.

Aperture appends the incoming request path to each provider base URL. Its [configuration reference](https://tailscale.com/docs/aperture/configuration/) warns against placing a duplicate `/v1` suffix in the provider root. This detail caused enough integration risk to earn an explicit validation check.

Vision is prepared to travel through the OpenAI Chat Completions format with image content. Embeddings use the private LiteLLM endpoint directly because the current Aperture self-hosted provider matrix documents chat formats, while our embedding path depends on LiteLLM and llama.cpp endpoints outside the chat picker. See the [supported providers and clients reference](https://tailscale.com/docs/aperture/reference/supported-providers-clients/).

The direct embedding route needs its own authorization boundary. LiteLLM authentication, restrictive Tailscale grants, service binding to the tailnet interface, and host firewall rules should limit access to approved identities or service tags. A private address alone is not an authorization policy.

## LiteLLM Presents One Catalog

Each inference host runs a LiteLLM gateway. Every gateway exposes the same logical model catalog, even when a model lives on another node. A client keeps one API shape and one set of aliases.

LiteLLM groups several deployments under one model name. Its router then selects an eligible deployment and applies retries, timeouts, cooldowns, or fallbacks. The current [LiteLLM routing documentation](https://docs.litellm.ai/docs/routing) covers shared model names, routing strategies, and retry behavior.

The catalog has two address styles:

| Address style | Example | Use |
| --- | --- | --- |
| **Shared alias** | `t4-classify` | Spread normal work across eligible nodes |
| **Node alias** | `node-b/qwen-small` | Run diagnostics or preserve placement |

Shared aliases produce horizontal scale without changing Hermes. Adding an eligible replica extends the model group. Removing an unhealthy replica narrows the group.

We keep GPU lifecycle logic below LiteLLM. The gateway stays warm because its memory footprint does not reserve GPU memory. A local pool proxy receives the selected model request, leases one card, starts the worker, and tears the worker down after the response.

## The Local Model Catalog

The fleet favors models at or below 12B parameters. This boundary matches the available card memory while leaving room for context and runtime buffers.

**Model notation:** `B` means billions of parameters. `K` means thousands of configured context tokens. **Quantization** stores model weights at reduced numeric precision to lower memory use. The **KV cache** holds attention state for the active context and grows with prompt length. **E4B** is Google's size label for the smaller Gemma 4 variant.

| Tier route | Model class | Configured context | Main job | Placement |
| --- | --- | ---: | --- | --- |
| **T3 smart** | Qwen3.5 9B, quantized | 64K | Hard local planning and general agent work | Higher-memory GPU nodes |
| **T3 code** | Granite 4.2 8B, quantized | 64K | Repository work, tools, terminal tasks, structured output | Higher-memory GPU nodes |
| **T3 review** | Gemma 4 12B, quantized | 32K | Independent review and alternate reasoning | Higher-memory GPU nodes |
| **T3 general and vision** | Qwen3.5 4B, quantized | 32K | Scaled general work and image understanding | Every compatible GPU |
| **T3 alternate review** | Gemma 4 E4B, quantized | 8K | Diverse review path | Every compatible GPU |
| **T4 code** | Granite 4.2 3B, quantized | 16K | Small edits, tool calls, structured output | Every compatible GPU |
| **T4 classify** | Qwen3.5 2B, quantized | 16K | Classification, extraction, and rewriting | Every compatible GPU |
| **T4 router** | Qwen3.5 0.8B, high precision quantization | 16K | Intent, labels, titles, and short transforms | Every compatible GPU |
| **T4 embedding** | Qwen3 Embedding 0.6B, quantized | 32K | Agent memory, RAG, code retrieval, and clustering | Every compatible GPU |

These context values are deployment settings, not advertised model limits. A larger advertised window still consumes KV cache and runtime memory. We selected lower values for stable single-card service.

Qwen describes Qwen3.5 as a multimodal family and publishes small through larger dense variants in the [Qwen3.5 collection](https://huggingface.co/collections/Qwen/qwen35). IBM publishes agentic coding and long-context results for [Granite 4.2 8B](https://huggingface.co/ibm-granite/granite-4.2-8b). Google lists multimodal input, function calling, and a larger advertised window for [Gemma 4](https://ai.google.dev/gemma/docs/core/model_card_4).

The embedding route uses a separate model instead of asking a chat model for vectors. The [Qwen3 Embedding 0.6B model card](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) lists a 32K sequence length, multilingual retrieval, code retrieval, and output dimensions up to 1,024.

{{< figure src="tiered-model-placement-map.webp" alt="Anonymized model placement diagram showing larger T3 models on high-memory nodes and replicated T3 and T4 models on multi-GPU nodes" caption="Larger specialists stay on higher-memory cards while smaller specialists replicate across the fleet" >}}

## Why llama.cpp Runs Production

llama.cpp matches the resource model. One static worker maps to one GPU, one model file, one configured context, and one lease. The process boundary makes startup, teardown, GPU visibility, and logs easy to audit.

Its server exposes OpenAI-compatible chat, responses, and embeddings. It also supports parallel decoding and continuous batching. The current server documentation labels multimodal support experimental. Those features appear in the [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).

Ollama stays available as a compatibility path on a larger node. Ollama supports concurrent model loads when memory fits and immediate unload through `keep_alive: 0`, as documented in the [Ollama FAQ](https://github.com/ollama/ollama/blob/main/docs/faq.mdx). We did not select Ollama for the per-card production path because static llama.cpp workers gave us tighter placement and teardown control.

We also reviewed Strata. Strata targets a large Qwen mixture-of-experts model spread across GPU memory, system RAM, and storage. Its published presets start at 32 GB of combined memory, while low-RAM mode trades speed for lower capacity. See the [Strata repository](https://github.com/kossum/strata). Strata fits a different goal: one larger hybrid model across one or more cards. Our fleet favors many independent sub-12B workers.

## Per-GPU Lazy Loading

Lazy loading applies to every model worker. The system keeps only gateways, pool proxies, watchdogs, and the miner active between requests.

{{< figure src="per-gpu-ai-mining-lifecycle.webp" alt="Anonymized flow diagram showing a GPU moving from Pearl mining to an AI lease, model service, unload, and mining recovery" caption="Only the leased card leaves the miner, then returns after the model process exits" >}}

The request lifecycle follows these steps:

1. **LiteLLM selects a deployment.** The request lands on a pool proxy for the selected model class.
2. **The pool acquires a lease.** A lock prevents two exclusive workers from taking the same card.
3. **The miner restarts without one GPU.** Every unleased card stays in the Pearl command.
4. **llama.cpp starts on the leased device.** Readiness checks finish before the proxy forwards the request.
5. **The worker serves the response.** Concurrent requests start workers on other free cards.
6. **The worker exits.** The pool removes the lease after process teardown.
7. **The miner restarts with the released GPU.** Health checks confirm the card rejoined mining.

This differs from an all-or-nothing host switch. A chassis with several cards serves several models while its remaining cards keep mining. An idle fleet returns every healthy GPU to Pearl.

The [Pearl whitepaper](https://pearlresearch.ai/Pearl_Whitepaper.pdf) describes its matrix-computation proof system. Our architecture does not rely on a profitability forecast or a claim about economic return. Mining serves as the configured idle workload.

## Failure Handling Matters More Than Startup

Model startup is only half of the lifecycle. Forced stops, vanished GPUs, interrupted requests, stale leases, and miner restarts need explicit handling.

Our watchdog compares the configured GPU set with the live NVIDIA device list. A confirmed missing GPU triggers one guarded full-system reboot. A safe production trigger should require repeated failed checks, a cooldown, active-job drain, a persistent reboot counter, and a remote alert. One failed recovery should stop automation and require manual intervention.

The same watchdog reconciles stale leases. If no worker owns a lease, reconciliation removes the stale record and restores the GPU to the miner. This recovery path mattered during the broker canary.

| Failure | Response |
| --- | --- |
| **Model fails readiness** | Stop the worker, release the lease, restore mining, return an error |
| **Request ends unexpectedly** | Bound cleanup time, terminate the worker tree, reconcile the lease |
| **GPU disappears** | Confirm repeated misses, drain active work, trigger one guarded reboot, alert, then verify the complete configured GPU set |
| **Miner omits an idle card** | Rebuild the device list from active leases and restart the miner |
| **LiteLLM deployment fails** | Retry another replica in the same model group, then follow the fallback policy |
| **Aperture grant blocks a route** | Fix the identity or model grant, never bypass the gateway policy |

## What Happened with the Experimental Broker

The [backend-agnostic broker](https://github.com/simeononsecurity/backend-agnostic-broker) aims to present one OpenAI-compatible surface across Ollama, vLLM, llama.cpp, and Strata. It includes per-model lifecycle management, idle unload, and GPU placement.

We tested broker version 0.6.0 at commit `c12b65` on October 21, 2026. Its local suite reported 1,101 passed tests and 2 skipped tests, with Ruff clean. The canary then loaded a model on demand and served a successful chat request. Other GPUs kept mining during the request.

Shutdown exposed a critical lifecycle problem. After a model had loaded, the broker remained in its stop path until systemd killed the process tree. The forced stop left a stale GPU lease until reconciliation restored the miner. We also found a gap between the documented required-GPU setting and production adapter enforcement.

**We disabled the broker in the production path.** LiteLLM now routes through the request-scoped pool proxy. The broker stays experimental until bounded child-process shutdown, process-group termination, required-GPU admission checks, and stale-lease cleanup pass integration tests.

This result is a useful engineering lesson. A broker proves little when it starts a model once. Production readiness depends on clean teardown, bounded recovery, exclusive device admission, and repeatable failure drills.

## Verification We Ran

The deployment test covered more than a model response:

- Each shared chat model completed the load, answer, exit, and Pearl recovery cycle on at least one eligible host.
- Vision accepted image input through the chat route.
- Embeddings returned the configured vector size through the private LiteLLM path.
- Multiple models ran at the same time on separate cards.
- Unleased cards stayed in the miner during concurrent AI requests.
- Shared aliases routed across eligible nodes.
- Node-prefixed aliases preserved deterministic placement.
- Every LiteLLM gateway listed the same logical catalog.
- A missing GPU recovered after one full host reboot. The watchdog now carries a persistent loop guard.
- A broker shutdown failure recovered through lease reconciliation.
- The final settled state showed no AI leases and every healthy GPU back in the miner set.

Health checks and model listings were not treated as model-load tests. A useful acceptance test sends a real request, checks the response, confirms the selected GPU, watches teardown, and verifies mining recovery.

## Troubleshooting the Fleet

| Symptom | First check |
| --- | --- |
| **Model appears but requests fail** | Upstream model ID, API format, auth header, and provider base URL |
| **Aperture returns 405** | Provider root has no duplicate `/v1` suffix |
| **Wrong node serves the request** | Shared alias versus node-prefixed alias |
| **Two workers target one card** | Lease lock, stale lease state, and GPU admission logic |
| **Mining stops on every card** | Miner restart code builds its device list from active leases |
| **GPU stays out of mining** | Worker process tree, lease reconciliation, and miner device list |
| **Cold load is slow** | Model size, storage speed, PCIe link width, and host CPU pressure |
| **Long prompts fail** | Configured context, KV cache headroom, and output reservation |
| **Embedding route is missing in Aperture** | Use the authenticated LiteLLM route restricted by Tailscale identity and host firewall policy |
| **Broker stop hangs** | Disable the broker route and return traffic to the verified pool proxy |

## Design Rules Worth Keeping

1. **Route by job purpose.** Model size alone does not define a tier.
2. **Keep policy above placement.** Hermes will select a capability alias. LiteLLM selects a deployment. The pool selects a GPU.
3. **Treat every GPU as a separate lease.** Host-wide switching wastes available cards.
4. **Unload every idle model.** Warm gateways do not require warm GPU workers.
5. **Preserve a restricted exact-placement path.** Operator-only node aliases make diagnostics reproducible.
6. **Test teardown first.** Miner recovery and lease cleanup belong in acceptance tests.
7. **Separate chat, vision, and embeddings.** One gateway does not imply one protocol path.
8. **Keep private details out of diagrams.** Publish roles and flows, not addresses, keys, identities, or wallet data.
9. **Make reboot logic guarded.** Require repeated misses, a cooldown, a persistent counter, an alert, and manual intervention after one failed recovery.
10. **Keep an experimental bypass.** A failed broker should not take the verified route with it.

## Next Steps

The next phase is workload evaluation. Each tier needs a fixed task set, acceptance criteria, latency records, GPU occupancy, mining interruption time, and escalation rates. Those measurements will show which T2 jobs belong on T3 and which T3 jobs fit T4.

We also plan to run the first Hermes through Aperture through LiteLLM acceptance test, then retest the broker after its shutdown and GPU-admission paths receive fixes. Image generation needs its own lazy OpenAI-compatible adapter before joining the same routing catalog.

For model sizing, read the [local AI model and GPU context guide](/articles/local-ai-model-gpu-context-guide/). For privacy boundaries, read [local AI privacy and security](/articles/local-ai-privacy-boundary/). For miner setup and risk, read the [Pearl mining guide](/articles/pearl-prl-mining-guide-2026/) rather than treating idle mining as guaranteed profit.
