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

**The memory API stays on the private network.** The web control plane stays on a local interface. A persistent volume holds the embedded database, so a container recreation does not discard banks. Authentication protects the API, and separate banks organize project context.

**The generation gateway supplies stable model names.** Hindsight sends OpenAI-compatible requests through the private gateway over a VPN. The gateway forwards requests to local serving endpoints. The inspected Qwen route reaches a LiteLLM deployment mapped to a local CPU server. [LiteLLM's router documentation](https://docs.litellm.ai/docs/routing) describes this model-alias pattern. An equivalent OpenAI-compatible router serves the same role.

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

*Keep small retrieval jobs on CPU and reserve GPU inference for measured long-running work.*

The Hindsight container loads **BAAI/bge-small-en-v1.5** for embeddings and **hindsight-ai/hs-rerank-1** for reranking. Startup logs confirm both run locally on CPU. The [Hindsight model reference](https://hindsight.vectorize.io/developer/models) documents local model options and the optional decision-model path.

We kept the existing embedding model because changing an embedding space requires rebuilding stored vectors. The reranker already runs locally, so a hosted reranking service would add a new data boundary without solving the observed generation timeout. A local **hs-decide-1-flash** pilot produced one correct Reflect answer, but the result finished close to its test wall limit. The synthetic consolidation data did not exercise the decision path. The decision model is therefore absent from production routing.

## Give Slow Background Work a GPU

**The normal model name and the refresh model name differ.** Retain, Reflect, and consolidation use the shared Qwen alias. Background page refresh uses a node-specific GPU alias with one concurrent language-model call. This limits a long maintenance job to one GPU at a time.

**A request-scoped reservation limits GPU use.** The GPU pool starts a model worker when a request arrives. Its controller reserves one card, serves the request, stops the worker, and releases the reservation. The diagram omits the physical host inventory.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagram showing one GPU reserved for a background page refresh and released when the request completes" caption="A request-scoped lease reserves one GPU for a page refresh" >}}

[Open the full-size GPU lease diagram](hindsight-gpu-lease-cycle.webp).

This split came from a failure we measured. **One CPU-first page refresh reached a one-hour wall limit.** After routing background refreshes to the local GPU pool, five previously failed pages completed in roughly two to six minutes in one recovery run. These figures describe those pages and settings. They are not a general Qwen throughput benchmark.

## Fix Defaults and Timeouts

**Hindsight's former output limits did not fit our local router.** The router accepts at most 8,192 output tokens and applies a 256-token limit when a request omits one. A former 64,000-token Retain limit drew HTTP 400. Eight-fact consolidation batches reached an output-length stop, and Reflect needed an explicit cap to avoid the router's 256-token fallback.

**We made the limits explicit for each job.** Qwen reasoning is off for these memory operations. Hindsight now permits four concurrent LLM calls overall, including at most one background page-refresh call. The global LLM timeout is 1,800 seconds with one model retry.

| Workload | Output or batch cap | Call and operation limits |
| --- | --- | --- |
| **Retain** | 8,192 output tokens | Global 1,800-second call timeout |
| **Reflect** | 4,096 output tokens | 900 seconds per call, 3,600-second operation wall |
| **Consolidation** | 4,096 output tokens, four facts per call | 900 seconds per call, 14,400-second operation wall |
| **Page refresh** | One concurrent model call | 900 seconds per call, dedicated GPU route |

*These values describe our November 2026 deployment and its local router.*

**A call timeout and an operation wall bound different stages.** Some valid Qwen calls exceeded the former 300-second call timeout. The longer operation walls permit multi-call work, while the 900-second per-call limits still bound each attempt.

In the recovery run, several Retain jobs completed with **1,042 to 2,076 output tokens**. Two consolidation runs completed **41 of 41** and **30 of 30** items. A later page-refresh wall expiry led to the separate GPU route described above. These recovery results do not establish long-term reliability.

## What the Design Trades Away

**No hosted model bill does not mean zero cost.** The deployment uses owned hardware, electricity, storage, maintenance time, and GPU time during page refreshes. Each placement choice trades capacity for latency or operational simplicity.

| Choice | Benefit | Trade-off |
| --- | --- | --- |
| **CPU-first generation** | Preserves GPU availability | A tested page refresh reached its one-hour wall |
| **GPU page refresh** | Five pages finished in roughly two to six minutes in one run | Uses GPU capacity and depends on the dedicated route |
| **Embedded database** | Keeps the deployment compact | Narrows the failure domain and requires backup testing |

*Use a GPU refresh route after measured CPU latency exceeds your maintenance window.*

The [Hindsight installation guide](https://hindsight.vectorize.io/developer/installation) recommends separate PostgreSQL for larger production deployments. **Our embedded database needs a tested backup and recovery path** as the bank grows.

**Private inference is a path property.** Check the selected Hindsight provider, gateway model mapping, fallback rules, local model process, log retention, and network egress. Hindsight's trace IDs help correlate requests, and Docker rotates the container logs. Neither measure proves a downstream request stayed local. A gateway audit supplies the missing end-to-end evidence.

## Recommendation

**Start with local retrieval models and explicit generation limits.** Place Hindsight and its embedding and reranking models on owned compute. Route generation through a private OpenAI-compatible gateway over a VPN. Measure each operation before assigning CPU or GPU capacity, and reserve the GPU route for background jobs whose CPU latency exceeds your maintenance window.

*Review every gateway fallback and test bank recovery before treating the deployment as private and resilient.* The [local AI privacy boundary guide](/articles/local-ai-privacy-boundary/) provides a starting checklist.

## Conclusion

**This deployment keeps Hindsight memory and the inspected inference paths on owned compute without a hosted model subscription.** CPU retrieval, bounded Qwen calls, and a single-call GPU refresh route address different workloads. The recovery runs completed Retain, consolidation, and page-refresh work under these settings. A full gateway fallback audit, backup test, and longer reliability observation remain the next checks.
