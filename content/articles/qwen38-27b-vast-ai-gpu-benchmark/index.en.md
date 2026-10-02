---
title: "Qwen3.8 27B GPU Benchmark on Vast.ai: H100, RTX PRO, A100, and More"
date: 2026-10-02
lastmod: 2026-10-02
toc: true
draft: false
description: "A measured Ollama benchmark of Qwen3.8 27B across leading Vast.ai GPUs. Compare decode speed, long-context behavior, rental cost, self-hosting tradeoffs, API credits, and subscriptions."
genre: ["Local AI", "GPU Benchmarking", "Self-Hosted AI", "Cloud Computing", "Artificial Intelligence", "AI Economics"]
tags: ["Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "GPU benchmark", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "local LLM", "long context", "GPU rental", "self-hosted AI", "abliterated models", "uncensored models", "API credits", "AI subscription", "Q4_K_M", "tokens per second"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "A high-tech workspace with a graphics card and screens displaying local AI benchmark results"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**The H100 SXM was the fastest card in this Qwen3.8 27B Ollama test, but it was not the best value.** The RTX PRO 5000 and RTX 6000 Ada delivered a stronger speed-to-rental-cost balance, while the CMP 170HX offered the lowest hourly rate among the completed runs.

*These results measure one model, one Ollama wrapper, one default quantization, and one serving pattern. Treat them as sizing data for this workload, not as a universal GPU ranking.*

This article compares **Qwen3.8:27b**, the Ollama Q4_K_M build at roughly 27.3B parameters, across GPU instances rented from Vast.ai. The test focused on decode throughput at four actual prompt lengths, including a long-context run near 131,000 prompt tokens.

## The Short Answer

**Rent an RTX PRO 5000 or RTX 6000 Ada for regular single-user work.** The RTX PRO 5000 led the value comparison at short and medium context lengths. The RTX 6000 Ada cost less and kept a useful lead over the A100 cards. Rent an H100 SXM when response speed matters more than hourly cost or when long prompts are part of the workload.

| Goal | Recommendation | Reason |
|---|---|---|
| **Lowest test cost** | CMP 170HX | $0.420 per hour and enough VRAM for this Q4_K_M model |
| **Best value under $1.25/hr** | RTX PRO 5000 or RTX 6000 Ada | Strong decode speed without H100 rental cost |
| **Fastest replies** | H100 SXM | Highest decode speed at every completed prompt length |
| **Long-context work** | H100 SXM or RTX PRO 6000 Max-Q | Both completed the approximately 131k-token run with substantial VRAM headroom |
| **Small recurring workload** | API credits or a chat subscription | No idle GPU charge, maintenance, or deployment work |
| **Private and frequent workload** | Owned GPU workstation | Hardware cost becomes easier to justify with sustained utilization |
| **Abliterated or uncensored experiments** | Rent first, then buy only after sustained use | Model behavior, licensing, and operational risk deserve a separate test before hardware spend |

## What Was Tested

**The benchmark used Ollama with the default Q4_K_M model build.** No special quantization, speculative decoding, custom sampler, or serving stack was added. The goal was a simple, locally reproducible comparison of the GPU instances.

Vast.ai describes its service as a GPU cloud marketplace connecting compute providers with users. Its documentation lists on-demand, reserved, interruptible, and serverless options, with search filters for GPU model, memory, price, and availability. The hourly rates below came from the selected instances during this benchmark session, not from a permanent Vast.ai price list.

The measured output was **decode throughput**, expressed as generated tokens per second. Prefill throughput is listed separately because it describes prompt processing, not the speed at which the answer appears. A long prompt often takes substantial time to process even when decode speed remains high.

The benchmark used two valid trials per context and recorded the median decode result. The completed prompt levels were based on actual `prompt_eval_count` values:

- **Approximately 16.4k prompt tokens**
- **Approximately 32.8k prompt tokens**
- **Approximately 65.5k prompt tokens**
- **Approximately 131k prompt tokens**

The requested 256k-token run was not completed. The 40 GB A100 cards and several smaller cards were still processing or failed to finish at the target context length.

> **Benchmark limit:** The figures describe one Qwen3.8 27B Q4_K_M workload. They do not predict training speed, multi-user throughput, image generation speed, vLLM performance, or another model's result.

## Approximately 16k Tokens

**The H100 SXM led the short-context run at 134.4 decode tokens per second.** The RTX PRO 5000 followed at 113.9 tokens per second while costing less than half as much per hour.

| Rank | GPU | VRAM | Decode tok/s | Prefill tok/s | Rental rate |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

At this prompt length, the RTX PRO 5000 produced about 84.7% of the H100's decode speed at 37.3% of the hourly rental rate. The RTX 6000 Ada produced about 66.3% of the H100's speed at 30.2% of the hourly rate.

## Approximately 32.8k Tokens

**The ranking stayed stable through the medium-context run.** The H100 SXM fell to 120.0 tokens per second, while the RTX PRO 5000 reached 105.0 and the RTX 6000 Ada reached 75.7.

| Rank | GPU | VRAM | Decode tok/s | Prefill tok/s | Rental rate |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

The RTX PRO 5000 remained the most attractive rental in this group. It was only 12.5% slower than the H100 while costing 62.7% less per hour.

## Approximately 65.5k Tokens

**Longer prompts exposed a wider gap between cards with large memory capacity and cards with less headroom.** The H100 stayed first at 112.0 tokens per second. The RTX PRO 6000 Max-Q moved ahead of the RTX 6000 Ada in decode speed.

| Rank | GPU | VRAM | Decode tok/s | Prefill tok/s | Rental rate |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

The RTX PRO 5000 was still the best balance in the completed table. The RTX 6000 Ada was slower than the RTX PRO 5000, but its lower rental rate made it attractive for budgets focused on availability over peak speed.

## Approximately 131k Tokens

**The H100 was the only card above 100 decode tokens per second at this context length.** The RTX PRO 6000 Max-Q completed the run at 73.4 tokens per second, followed by the RTX 6000 Ada at 61.7.

| Rank | GPU | VRAM | Decode tok/s | Prefill tok/s | Rental rate |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | N/A | N/A | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | N/A | N/A | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | N/A | N/A | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

The RTX PRO 6000 Max-Q became the practical alternative to the H100 for long prompts. It delivered 67.8% of the H100's decode speed at 56.0% of the hourly rate. The RTX 6000 Ada cost less, but its 48 GB of VRAM leaves less room for long prompts, larger batches, or another model configuration.

## Overall Decode Comparison

| GPU | ~16k | ~32.8k | ~65.5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | N/A |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | N/A |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | N/A |
| **A100 PCIe** | 38.4 | 36.1 | N/A | N/A |

**The H100 led every completed context length.** Its advantage narrowed from 20.5 tokens per second over the RTX PRO 5000 at roughly 16k tokens to 12.0 at roughly 32.8k tokens. The value ranking depends on whether you need the fastest first response or the lowest cost for a long-running session.

## Cost per Million Decode Tokens

**Hourly price alone hides the useful comparison.** Dividing the supplied hourly rate by decode throughput gives a rough rental cost for one million generated tokens. This ignores prompt processing, idle time, storage, data transfer, taxes, discounts, and failed or interrupted runs.

| GPU | Short-context rate | Approx. cost per 1M decode tokens |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**The CMP 170HX won this narrow arithmetic comparison.** The RTX PRO 5000 and RTX 6000 Ada were close behind, and both provided more throughput than the CMP 170HX. For interactive use, the extra waiting time often matters more than the lowest token cost.

## Rent, Buy Credits, Subscribe, or Buy Hardware?

**The right option depends on utilization and control requirements.** A GPU rental is a variable compute bill. API credits are a variable model bill. A chat subscription is a fixed access fee with usage limits. Owned hardware is a capital purchase followed by electricity, cooling, maintenance, and depreciation.

| Monthly budget and workload | Recommended path | Why | Main compromise |
|---|---|---|---|
| **Under $10** | Buy API credits or use a free local model | Proves the workflow without idle GPU cost | Less control over model hosting and rate limits |
| **$10 to $30** | API credits for occasional work, or a chat subscription for daily interactive use | A subscription suits human chat, while credits suit scripts and measured calls | Neither option gives a private 27B endpoint by default |
| **$30 to $100** | Rent an RTX 6000 Ada or RTX PRO 5000 only during active sessions | This budget covers short research bursts and avoids ownership overhead | The instance still needs setup, storage, monitoring, and shutdown discipline |
| **$100 to $250** | Rent a fast card for scheduled work, or test an owned workstation plan | Sustained monthly usage starts to make utilization visible | Rental availability and hourly rates change |
| **$250 to $600** | Compare a month of RTX PRO 5000 rental against a used or new local GPU | This is the decision point for frequent private inference | Hardware adds power, heat, support, and resale risk |
| **Above $600** | Buy hardware only with high utilization, or reserve H100-class rental for burst work | A mixed strategy avoids owning peak hardware for occasional demand | Capital remains tied up in a single configuration |

These bands are decision guides, not provider quotes. The benchmark rates show the key break-even issue: an H100 at $2.693 per hour costs about $64.63 for a continuous 24-hour day and about $1,941.00 for 30 days before storage or other charges. The RTX PRO 5000 at $1.005 per hour costs about $24.12 per day and $723.60 for 30 continuous days. A GPU rented only for active sessions has a different total from a GPU left running all month.

### When API Credits Win

**API credits win when usage is irregular, automation matters, and the task does not require a specific local model.** Credits avoid GPU provisioning, model downloads, driver problems, and idle time. They also let you compare several hosted models before committing to hardware.

API pricing differs by model and provider. OpenRouter's model catalog is designed for comparing model context sizes, providers, and token pricing. Use the provider's live calculator before comparing an API bill with this benchmark. A local GPU produces tokens without a per-token provider charge, but its rental hour continues while the instance waits.

### When a Subscription Wins

**A subscription suits a person who uses a hosted assistant every day.** Claude's current individual plans, for example, separate free, Pro, and Max access levels with different usage limits and features. A subscription is not the same as API access. It often gives a polished interface and bundled tools, while API credits give programmatic control.

Choose a subscription when the work is mostly interactive writing, research, coding, or file review. Choose API credits when a script, application, or agent needs a metered endpoint.

### When Vast.ai Wins

**Vast.ai wins when you need an open model, private runtime control, or a short burst of high throughput.** You select the GPU, launch an instance, run Ollama, test a model, and shut the instance down when finished. This is a strong path for Qwen3.8 27B, abliterated variants, and other model files unable to fit a consumer laptop.

The cost is operational work. You need to confirm the model is using the GPU, watch VRAM, protect the exposed service, preserve any required model files, and stop the instance after the run. A low hourly rate does not fix a forgotten instance.

### When Buying a GPU Wins

**Buying hardware wins after sustained utilization, stable model requirements, and a need for local control.** The purchase removes rental availability risk and gives you a persistent environment. It also gives you the option to run private data without sending prompts to a hosted provider.

The purchase price is only one part of the bill. Add the host system, power supply, storage, cooling, electricity, replacement risk, and the value of your setup time. A high-end card also sits idle during periods when API credits or a subscription would cost less.

NVIDIA's RTX 4090 reference specifications list 24 GB of memory, a 450 W total graphics power rating, and an 850 W minimum system power recommendation. This makes it a useful local-inference reference point, but its 24 GB capacity is below the 27B Q4_K_M configurations tested here. Check actual model memory use rather than assuming a card fits from the parameter count alone.

## Abliterated and Uncensored Models

**Abliterated and uncensored model variants change the buying decision.** Their appeal is often fewer refusal behaviors or fewer built-in restrictions. Their costs include weaker safety behavior, uncertain provenance, inconsistent prompt formatting, higher review needs, and possible license or acceptable-use limits.

For these models, rent before buying. A one-day RTX PRO 5000 test at the supplied rate costs about $24.12 before other charges. This is enough to confirm model fit, GPU use, response quality, and operational risk.

**Do not expose an uncensored model directly to the public internet.** Put authentication, rate limits, logging controls, and network isolation in front of it. Avoid sending personal, confidential, or regulated data to a model source you have not reviewed.

If the model becomes a daily tool, compare the monthly rental total with the full cost of an owned workstation. If usage is occasional, the rental remains easier to stop and replace.

## Benchmark Caveats

**The missing results are part of the result.** A dash means the run did not produce a valid measurement. It does not mean the GPU is slow by the amount implied by another card's score.

- **The second H100 instance produced no valid benchmark set** because the model download completed too late.
- **The 2x RTX 5060 Ti instance was excluded** because Ollama loaded the model on the CPU instead of using the GPUs.
- **The 256k-token prompt was not completed.** The highest valid level was approximately 131k actual prompt tokens.
- **The requested `num_ctx` was not used as the ranking label.** The final tables use actual `prompt_eval_count` values.
- **Two valid trials per context were summarized with the median decode result.** This reduces the effect of one slow run, but it does not replace a larger test set.
- **The wrapper was simple by design.** A tuned vLLM or llama.cpp deployment will produce a different ranking.

## Final Recommendation

**Start with an RTX 6000 Ada or RTX PRO 5000 rental.** The RTX 6000 Ada is the budget choice when its $0.813 hourly rate is available. The RTX PRO 5000 is the stronger speed choice below H100 pricing. Use the H100 SXM for long prompts, demanding interactive latency, or a short benchmark window where time matters more than rental cost.

**Do not buy a GPU after one successful test.** Rent for a month of real workloads, record active hours, prompt lengths, concurrency, and model changes, then compare the rental total with the complete ownership bill. Buy hardware when the workload is frequent enough to keep the card busy and stable enough to justify the loss of flexibility.

For occasional work, API credits or a chat subscription are simpler. For private local inference, open model experimentation, or abliterated model testing, Vast.ai provides a lower-commitment path than buying a workstation immediately.

## References

1. [Vast.ai GPU cloud marketplace](https://vast.ai/)
2. [Vast.ai documentation: marketplace, instances, pricing, and rental types](https://docs.vast.ai/)
3. [Ollama Qwen3 model library](https://ollama.com/library/qwen3)
4. [OpenRouter model catalog and pricing comparison](https://openrouter.ai/models)
5. [Claude pricing and individual subscription plans](https://www.anthropic.com/pricing)
6. [NVIDIA GeForce RTX 4090 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
7. [Local AI in 2026: Qwen3.8 27B and self-hosted model hardware](/articles/local-ai-2026-build-your-rig-now/)
8. [Ollama model testing on Raspberry Pi hardware](/articles/ai-models-raspberry-pi-4-5/)