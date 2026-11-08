---
title: "Self-Hosted Hindsight: Local Agent Memory and Private Model Routing"
date: 2026-11-08
lastmod: 2026-11-08
toc: true
draft: false
description: "A case study of self-hosted Hindsight, observed local Qwen routes, and request-scoped GPU work without a hosted model subscription on the inspected paths."
genre: ["Local AI", "Self-Hosted AI", "AI Agents", "AI Infrastructure", "Privacy"]
tags: ["Hindsight", "self-hosted Hindsight", "agent memory", "local AI", "local LLM", "Qwen3.5", "LiteLLM", "private VPN", "model gateway", "embeddings", "reranking", "GPU scheduling", "private inference", "Docker", "memory banks", "knowledge pages", "local model routing"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "An abstract private memory service routes work to local CPU and GPU model servers"
coverCaption: "Memory storage, retrieval, and the inspected model routes run on owned compute"
---

**Our Hindsight memory service runs on hardware we control.** The memory engine, database, embedding model, and reranker run in one self-hosted deployment. Hindsight sends generation requests to a private gateway. The inspected shared Qwen backend and tested page-refresh route use local model servers without a hosted inference subscription.

This is a description of one working deployment. **Self-hosted does not mean offline.** The VPN uses an external coordination service, and software images and model weights require downloads. The claim here concerns memory processing and model inference, not every network connection made by our devices or other agent tools.

<!--more-->

## Key Takeaways

- **Hindsight owns the memory workflow.** A Docker container serves the API, workers, and control plane, with bank data on a persistent volume.
- **Small retrieval models stay local.** Embeddings and reranking run inside the Hindsight process on CPU.
- **Qwen handles text generation.** Retain, Reflect, and consolidation request the private Qwen3.5-4B alias with reasoning disabled and bounded output. The inspected backend serves locally.
- **Long page refreshes get a GPU.** A separate model alias leases one card for a background request, then releases the card after the request.
- **The gateway hides physical placement.** Hindsight selects a model alias. Private routing services select a serving endpoint.

## Set the Boundary Before Choosing Models

**Hindsight is the memory engine, not the model server.** Its full Docker image includes local embedding and reranking models, but language-model generation needs an endpoint. The [Hindsight installation guide](https://hindsight.vectorize.io/developer/installation) documents this split and shows local llama.cpp, Ollama, and vLLM servers as alternatives to hosted providers.

Our API accepts agent requests over a private network. The web control plane stays on a local interface. A persistent volume holds the embedded database, so a container recreation does not discard banks. Authentication protects the memory API, and separate banks organize project context.

For generation, Hindsight sends OpenAI-compatible requests through a private gateway over a VPN. The gateway exposes stable model names and forwards requests to local serving endpoints. The inspected Qwen route reaches a LiteLLM deployment mapped to a local CPU server. [LiteLLM's router documentation](https://docs.litellm.ai/docs/routing) describes this model-alias pattern. An equivalent OpenAI-compatible router serves the same role.

{{< figure src="hindsight-private-request-path.webp" alt="Diagram showing agents, a private Hindsight service, local retrieval models, a private gateway, and local Qwen servers" caption="The diagram omits hostnames, addresses, access keys, and physical host labels" >}}

[Open the full-size request path diagram](hindsight-private-request-path.webp).

**An internal API still exists.** Hindsight calls a private gateway using the OpenAI-compatible format. The inspected model routes serve inference locally. We did not audit every gateway fallback rule, so gateway policy needs review before anyone treats local processing as a guarantee for every request.

## Assign Each Memory Job to the Right Compute

Hindsight's operations do different work. **Retain** extracts facts from new material. **Recall** finds relevant memories. **Reflect** searches and writes a synthesized answer. **Consolidation** merges related facts. Background **knowledge-page refresh** rebuilds a living summary from the bank.

| Operation | Model placement | Reason |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B through the private gateway | Local structured extraction with a bounded output budget |
| **Recall** | Local CPU embedding and reranking | Search does not need a generation API call |
| **Reflect** | Qwen3.5-4B through the private gateway | Synthesis needs generation after memory retrieval |
| **Consolidation** | Qwen3.5-4B through the private gateway | Small batches limit long structured responses |
| **Knowledge-page refresh** | Dedicated local GPU Qwen route | Large background synthesis exceeded the CPU route's wall limit |

The Hindsight container loads **BAAI/bge-small-en-v1.5** for embeddings and **hindsight-ai/hs-rerank-1** for reranking. Startup logs confirm both run locally on CPU. The [Hindsight model reference](https://hindsight.vectorize.io/developer/models) documents local model options and the optional decision-model path.

We kept the existing embedding model because changing an embedding space requires rebuilding stored vectors. The reranker already runs locally, so a hosted reranking service would add a new data boundary without solving the observed generation timeout. A local **hs-decide-1-flash** pilot produced one correct Reflect answer, but the result finished close to its test wall limit. The synthetic consolidation data did not exercise the decision path. The decision model is therefore absent from production routing.

## Give Slow Background Work a GPU

**The normal model name and the refresh model name differ.** Retain, Reflect, and consolidation use the shared Qwen alias. Background page refresh uses a node-specific GPU alias with one concurrent language-model call. This limits a long maintenance job to one GPU at a time.

The GPU pool starts a model worker when a request arrives. Its controller reserves one card, serves the request, stops the worker, and releases the reservation. The diagram omits the physical host inventory.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagram showing one GPU reserved for a background page refresh and released when the request completes" caption="A request-scoped lease reserves one GPU for a page refresh" >}}

[Open the full-size GPU lease diagram](hindsight-gpu-lease-cycle.webp).

This split came from a failure we measured. **One CPU-first page refresh reached a one-hour wall limit.** After routing background refreshes to the local GPU pool, five previously failed pages completed in roughly two to six minutes in one recovery run. These figures describe those pages and settings. They are not a general Qwen throughput benchmark.

## Fix Defaults and Timeouts

**Hindsight's former output limits did not fit our local router.** The router accepts at most 8,192 output tokens and applies a 256-token limit when a request omits one. A former 64,000-token Retain limit drew HTTP 400. Eight-fact consolidation batches reached an output-length stop, and Reflect needed an explicit cap to avoid the router's 256-token fallback.

We set **Retain to 8,192 output tokens**, **Reflect and consolidation to 4,096**, and **consolidation to four facts per call**. We disabled Qwen reasoning for these memory jobs. These changes address the observed limit failures without changing the embedding space or switching the production decision model.

**Multiple memory operations share local serving capacity.** Long page rebuilds compete with Retain and interactive Reflect for model slots. Hindsight now permits four concurrent LLM calls across ordinary work and one concurrent call for background page refresh. The refresh cap bounds this contention.

**The former 300-second call timeout cut off valid Qwen work.** The global LLM timeout is now 1,800 seconds, with 900-second limits for Reflect, consolidation, and page-refresh calls. Reflect has a 3,600-second operation wall and consolidation has a 14,400-second wall. Hindsight allows one model retry. Each limit bounds a different stage, so a longer operation wall does not remove the per-call limit.

In the recovery run, several Retain jobs completed with **1,042 to 2,076 output tokens**. Two consolidation runs completed **41 of 41** and **30 of 30** items. A later page-refresh wall expiry led to the separate GPU route described above. These recovery results do not establish long-term reliability.

## What the Design Trades Away

**No hosted model bill does not mean zero cost.** The deployment uses owned hardware, electricity, storage, maintenance time, and GPU time used during page refreshes. A CPU route preserves GPU availability but takes longer on large prompts. A node-specific GPU route finishes the tested page refreshes faster, yet depends on the GPU pool's health.

The embedded database keeps the stack compact. The [Hindsight installation guide](https://hindsight.vectorize.io/developer/installation) recommends a separate PostgreSQL service for larger production deployments. Our single-container layout accepts a narrower failure domain and needs backup and recovery testing as bank size grows.

**Private inference is a path property.** Check the selected Hindsight provider, gateway model mapping, fallback rules, local model process, log retention, and network egress. Hindsight's trace IDs help correlate requests, and Docker rotates the container logs. Neither measure proves a downstream request stayed local. A gateway audit supplies the missing end-to-end evidence.

If you plan a similar system, start with the [local AI privacy boundary guide](/articles/local-ai-privacy-boundary/). Draw your data path first. Then test Retain, Recall, Reflect, consolidation, and page refresh as separate workloads before assigning CPU or GPU capacity.
