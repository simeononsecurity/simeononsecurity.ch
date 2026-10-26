---
title: "Hermes Local Model Benchmarks: The GPU and Model Combinations I Would Use"
date: 2026-10-24
lastmod: 2026-10-26
toc: true
draft: false
description: "My Hermes model recommendations from long-context, tool, streaming, and vision tests on RTX 5060 Ti, RTX 2000E Ada, RTX 3060 Ti, and RTX 3070 systems."
genre: ["Artificial Intelligence", "Local AI", "Hardware"]
tags: ["Hermes Agent", "local language models", "LLM benchmarks", "GPU inference", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "model qualification", "tool calling", "long context", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Illustrated dual-fan and low-profile graphics cards beside the title Hermes Model Benchmarks on a dark blue background"
coverCaption: ""
---

For long-context Hermes work, I would start with Qwen3.5 35B on two 16GB RTX 5060 Ti cards. The tested route retained 239,153 input tokens through LiteLLM and passed separate tool, streaming, vision, queued-request, and cancellation checks. Qwen3.6 is my one-card alternative. On the RTX 3060 Ti and RTX 3070 systems, I would start with Qwen3.5 2B or 4B.

Those choices come from running models through the inference paths used by the agent. I tested long-input retention, tool round trips, streamed responses, image questions, and model release. I also tested the modes and memory settings behind the routes, because a model loading successfully says little about its usefulness during a long agent request.

Hermes requires at least 64,000 tokens of context for agent use with tools. I used 65,536 actual input tokens as the long-context qualification threshold. The input count matters more than the context size advertised by the server. ([Hermes Agent provider documentation](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## Which GPUs were in each system

The system letters identify the hardware combinations throughout the results.

| System | GPUs used for this benchmark | My starting model choice |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, 16GB each | Qwen3.5 35B across both cards, or Qwen3.6 on one card |
| B | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B when several minutes of long-input processing fits the task |
| C | 1 × RTX 2000E Ada, 16GB | Gemma 3 4B for the tested long-input path, Qwen3.5 0.8B in nonthinking mode for narrow recall work |
| D | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B, Gemma 4 12B-IT, or GPT-OSS 20B for the tested larger-model workloads |
| E | 9 × GeForce RTX 3060 Ti, 8GB each | Qwen3.5 2B or 4B |
| F | 8 × GeForce RTX 3060 Ti, 8GB each | Qwen3.5 2B or 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B or 4B |

Installed card count does not mean every request used every GPU. The Qwen3.5 35B and Flash Next trials used both cards in System A. Qwen3.6 used one card. The successful System E Qwen3.5 4B vision rerun used one selected card from an eight-card pool while a ninth card stayed excluded from AI work.

Treat the durations below as results for the tested model, runtime, and system together. These runs compare usable configurations. They do not isolate GPU architecture as the cause of a speed difference.

## Two RTX 5060 Ti cards make Qwen3.5 35B my long-context choice

Qwen3.5 35B produced the largest retained-input result in these tests. The direct Ollama progression retained 248,279 input tokens inside a 262,144-token runtime context. A separate streamed gateway request retained 239,153 input tokens, returned the opening marker, and ended naturally after 31 output tokens in 148.12 seconds.

The gateway result matters for Hermes because the request passed through the broker and LiteLLM. Separate requests completed a tool round trip, recognized a red image, and returned two correct answers when submitted together. The broker queued those two requests. Closing a streamed request released the broker and unloaded the model within 60.31 seconds.

| Qwen3.5 35B request | Input tokens | Output tokens | Duration | Outcome |
|---|---:|---:|---:|---|
| Direct Ollama, first progressive stage | 69,429 | 31 | 38.783 s | Exact opening marker |
| Direct Ollama, shared-prefix continuation | 124,179 | 31 | 28.472 s | Exact opening marker |
| Direct Ollama, shared-prefix continuation | 182,579 | 31 | 38.974 s | Exact opening marker |
| Direct Ollama, shared-prefix continuation | 248,279 | 31 | 54.215 s | Exact opening marker |
| Broker streaming request | 69,427 | 29 | 38.872 s | Exact opening marker |
| LiteLLM streaming request | 239,153 | 31 | 148.12 s | Exact opening marker, clean unload |

The progressive direct requests reused an expanding prefix. Their durations describe warm continuation behavior. The 54.215-second result is not an independent cold processing measurement for a fresh 248K prompt.

At the largest direct stage, the model reported about 27.3 billion bytes resident across the two GPUs. Per-card memory peaks reached 14,964 and 12,386 MiB.

Peak temperatures reached 62 and 63 C, and the run recorded no OOM or Xid fault. The input left 13,865 tokens inside the configured context for continuation. The short marker answer used 31 of those tokens.

I would use this route when retaining a large working set matters more than the shortest initial response. The tool and vision checks establish useful agent behaviors, while the long-input test establishes retention. They are separate workloads.

## Qwen3.6 is the one-card option

Qwen3.6-35B-A3B UD-Q4_K_XL retained 131,000 input tokens on one RTX 5060 Ti. The other card stayed idle during the test. This gives the system a useful alternative when dedicating both cards to one model is undesirable.

| Qwen3.6 gateway request | Input tokens | Output tokens | Duration | Outcome |
|---|---:|---:|---:|---|
| Initial long request | 66,007 |  | 167.82 s | Opening marker retained |
| Longer request | 90,000 | 11 | 159.92 s | Opening marker retained, zero cached input |
| Longer request | 119,999 | 11 | 250.61 s | Opening marker retained, zero cached input |
| Near runtime limit | 131,000 | 11 | 287.09 s | Opening marker retained, zero cached input |

The 131,000-token request approached the 131,072-token runtime limit. For an agent, I would leave more space for the answer and subsequent tool messages. A near-limit retention result is useful evidence of input handling, rather than a sensible default input budget.

Tool use passed with thinking disabled. Default thinking consumed the 512-token trial allowance before issuing the tool call. The successful pilot also passed quick, streamed, and vision requests. Its initial 65,845-token context check took 139.57 seconds.

## Qwen3.8 27B wins the matched 66K response comparison

For the same 66,007-token marker workload on System A, Qwen3.8 27B returned the answer fastest. I would keep this route available for requests around the tested input size, alongside Qwen3.5 35B for the larger working set.

| System A route | Input tokens | Duration | Outcome |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Opening marker retained |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Opening marker retained |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Opening marker retained |
| Flash Next IQ4 compatibility alias | 66,007 | 213.25 s | Marker retained |

Qwen3.8 27B took about one third of the matched Qwen3.6 and Flash Next request durations. These are complete-request observations with the tested runtimes, rather than a hardware-only comparison.

Quick responses, streaming, and tool use also passed. Thinking-disabled mode completed the full color sequence and tool round trip, while the thinking trial returned only part of the color sequence within its 512-token allowance.

Flash Next remains a less attractive default on this system because of memory pressure. Its 65,847-token pilot passed in 201.41 seconds at 98,304 runtime context. Two earlier 131,072-context profiles reached their memory limits before readiness.

The later route reached its 54 GiB cgroup cap. I would choose a route with more memory headroom for unattended work.

The route labelled `flash-iq2` served the Flash Next IQ4 compatibility backend. Its name does not identify an IQ2 result.

## The RTX 2000E Ada handles long input, but model choice changes the wait

Gemma 3 4B is my preferred tested long-input route on System C. Two paths retained more than 84K input tokens in about 88 seconds. The larger model routes passed useful retention checks too, but their requests took several minutes.

| System | Model and path | Input tokens | Duration | Outcome |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, gateway | 72,265 | 263 s | Both sentinels retained, later mining-recovery check passed |
| C | Gemma 3 4B, gateway | 84,044 | 88.05 s | Opening marker retained |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Opening marker retained |
| C | Gemma 4 12B-IT, gateway | 67,254 | 263.07 s | Opening marker retained |
| C | Gemma 4 12B-IT, Aperture non-stream | 67,255 | 274.24 s | Opening marker retained |
| C | Gemma 4 12B-IT, Aperture stream | 67,255 | 282.16 s | Opening marker retained |
| C | Qwen3.5 9B, gateway | 75,648 | 319.36 s | Opening marker retained, model unloaded |
| C | GPT-OSS 20B, gateway | 84,099 | 315.83 s | Opening marker retained, model unloaded |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Retention passed on the installed artifact |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Retention passed on the installed artifact |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Retention passed on the installed artifact |

Streaming did not remove Gemma 4's long-prefill wait on System C. The first streamed content arrived after 277.49 seconds, later than the complete 274.24-second non-stream response. An earlier non-stream attempt timed out before the successful retry. I would reserve this route for work where several minutes of initial processing fits the task.

Gemma 3 4B also shows why I would keep qualification specific to each tested system. System D missed the opening marker in two 65K recall attempts, including a temperature-zero repeat with 67,252 input tokens. The deterministic request ended naturally in 62.07 seconds with full GPU residency.

Fast completion and a normal API response did not make the answer correct. I would use the successful System C route and leave the failing System D route out of Hermes selection.

## Thinking mode decides whether Qwen3.5 0.8B is useful

Qwen3.5 0.8B became a useful narrow-recall candidate on System C after thinking was disabled. The small Q8_0 model retained 75,649 input tokens through the gateway in 65.92 seconds. This result belongs to the tested Q8_0 artifact and nonthinking route, rather than the older 16K-context configurations elsewhere in the table.

| Qwen3.5 0.8B request on System C | Input tokens | Output tokens | Duration | Outcome |
|---|---:|---:|---:|---|
| Default thinking, short diagnostic | 9,050 | 3,391 | 66.56 s | Exact opening marker |
| Thinking disabled, matched diagnostic | 9,055 | 21 | 7.65 s | Exact opening marker, no reasoning text |
| Default thinking, long attempt |  |  | 600 s timeout | No completed answer |
| Thinking disabled, native Ollama | 75,656 | 22 | 69.80 s | Exact opening marker |
| Nonthinking OpenAI-compatible endpoint | 75,646 | 12 | 69.09 s | Exact opening marker |
| Broker with nonthinking mode enforced | 75,647 | 13 | 66.83 s | Exact opening marker |
| LiteLLM through System A to System C | 75,649 | 15 | 65.92 s | Exact opening marker |

The matched diagnostic fell from 66.56 to 7.65 seconds, about 8.7 times faster, while generated output fell from 3,391 to 21 tokens. This is why I would set the reasoning mode explicitly for simple extraction and routing tasks. Default reasoning spent most of the work on output the task did not need.

A short OpenAI-compatible probe missed its marker before the temperature-zero retry passed. The successful route checks used nonthinking mode and natural completion without an output cap. Three other gateways passed short marker requests in 4.22, 4.37, and 3.85 seconds. Those checks establish routing, while the 75,649-token request establishes long-input retention through the gateway.

I would trial this route for bounded recall and extraction. I would choose a larger model for open-ended agent reasoning. Retrieving one synthetic marker is a narrower task than planning, coding, or coordinating several tools.

## The RTX 3060 Ti and RTX 3070 systems favor Qwen3.5 2B and 4B

Qwen3.5 2B and 4B are my practical starting choices for the 8GB cards. Their text context requests on Systems E, F, and G passed with 65,579 input tokens and durations from 30.343 to 93.753 seconds. The tested 4B routes also passed tool, streaming, and image checks.

System E's 4B vision-context rerun retained both markers and the ordered image colors at 65,637 input tokens in 44.88 seconds. Forward and reversed color-order requests passed too. The rerun used one healthy card after another card suffered an Xid 79 link fault and the system rebooted.

| System | Qwen3.5 2B text context | Qwen3.5 4B text context | Qwen3.5 4B vision context |
|---|---|---|---|
| E, RTX 3060 Ti pool | 65,579 tokens, 30.343 s | 65,579 tokens, 53.787 s | 65,637 tokens, 44.88 s |
| F, RTX 3060 Ti pool | 65,579 tokens, 61.282 s | 65,579 tokens, 93.753 s | 65,635 tokens, 84.749 s |
| G, RTX 3070 pool | 65,579 tokens, 76.731 s | 65,579 tokens, 90.807 s | 65,635 tokens, 87.496 s |

Each of these systems recorded 29 passing checks. The timing spread across the two RTX 3060 Ti systems also shows why I would select a tested system profile rather than rank cards from these request durations.

All seven systems returned to mining after the inference window. System B's separate post-stop recovery check passed with fresh accepted shares. The faulting card in System E later returned to mining after a reboot and PCIe link hardening, while its AI-pool exclusion stayed in place. Restoring mining at the end of the window is a separate result from automatic hand-back after an individual inference request.

## Loading a model does not qualify the model

I would exclude DeepSeek Coder V2 16B from the tested 65K Hermes choices. Its f16-cache run retained 50,477 input tokens, but the 65K-target run reached the VRAM guard. Q4 and Q8 cache alternatives loaded the weights on the GPUs, then hit host-memory limits or poor long-prompt throughput.

| DeepSeek Coder V2 cache profile | Runtime context | Observed result | My assessment |
|---|---:|---|---|
| f16 | 81,920 | 50,477-token recall passed, oversized request rejected | Useful shorter-context result |
| f16 | 73,728 | 65K-target prefill stopped at 15,802 MiB GPU use | Does not qualify for 65K |
| Q4_0 | 98,304 | Long prefill fell to 96.72 tokens/s before the controlled stop | Poor fit for this workload |
| Q8_0 | 77,824 | Long prefill fell to 120.12 tokens/s before the controlled stop | Poor fit for this workload |
| Q4_0 / Q8_0, larger profiles | 163,840 / 98,304 | Host-memory guards stopped the trials | Memory fit needs the whole system |

The practical lesson is to benchmark the request you intend to send. GPU residency, a short answer, and a large configured context do not establish retained long input at a useful latency.

Granite 4.2 8B and GPT-OSS 20B improved after route-specific follow-up work on System A. Granite's Q6_K route retained 66,082 input tokens in 88.636 seconds with zero cached input. GPT-OSS completed its tool round trip after the broker fix, with 9.854 seconds for the call and 9.849 seconds for the follow-up. I would keep these successful route checks distinct from earlier incomplete attempts.

## Full benchmark results

The table contains 295 checks across 59 model and system combinations. The matrix records 273 passes, one failed recall check, and seven incomplete, inconsistent, or incompatible outcomes. Fourteen checks sit outside the 65K qualification scope. Every row keeps its measured outcome visible.

My recommendations apply to the passing routes and workloads. A failed or incomplete row does not qualify the corresponding behavior.

Short-context and embedding passes apply to their own workloads. A 16K or 32K context pass does not qualify a route for the 65,536-input-token Hermes workload. Model names here are route labels. The `flash-iq2` label served the IQ4 compatibility backend.

The System A Qwen3.5 35B context row is the final shared-prefix stage from the progression above. Tool durations written with a plus sign show the call and follow-up separately.

The concurrency row gives the two queued request durations. The cancellation row gives release time after the client closed the stream. Supplemental context progressions and Qwen3.5 0.8B route comparisons appear in their own tables above.

### System A

| Model route label | Check | Outcome | Input tokens | Request duration |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Pass | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Pass | 57 | 6.429 s |
| bonsai-2-27b | stream | Pass |  | 9.371 s |
| bonsai-2-27b | tools | Pass |  | 10.478 s |
| deepseek-coder-v2:16b | context | Incompatible | 50,477 |  |
| deepseek-coder-v2:16b | quick | Pass | 77 | 43.239 s |
| flash-iq2 | context | Pass | 66,007 | 213.25 s |
| flash-iq2 | quick | Pass |  | 56.03 s |
| flash-iq2 | stream | Pass |  | 1.35 s |
| flash-iq2 | tools | Pass |  | 16.55 s |
| gemma-4-12b-it | context | Pass | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Pass | 21 | 5.166 s |
| gemma-4-12b-it | stream | Pass |  | 4.653 s |
| gemma-4-12b-it | tools | Pass |  | 18.72 s |
| gemma-4-12b-it | vision | Pass | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Pass | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Pass | 115 | 7.467 s |
| gemma-4-e4b-it | context | Pass | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Pass | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Pass |  | 4.25 s |
| gemma-4-e4b-it | tools | Pass |  | 8.734 s |
| gpt-oss-20b | context | Pass | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Pass | 73 | 10.548 s |
| gpt-oss-20b | stream | Pass |  | 20.594 s |
| gpt-oss-20b | tools | Pass |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Pass | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Pass | 20 | 4.009 s |
| granite-4.2-3b | stream | Pass |  | 5.365 s |
| granite-4.2-3b | tools | Pass |  | 6.086 s |
| granite-4.2-8b | context | Pass | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Pass | 20 | 5.857 s |
| granite-4.2-8b | stream | Pass |  | 11.826 s |
| granite-4.2-8b | tools | Pass |  | 11.852 s |
| qwen27b | context | Pass | 66,007 | 54.64 s |
| qwen27b | quick | Pass | 57 | 31.5 s |
| qwen27b | stream | Pass |  | 0.92 s |
| qwen27b | tools | Pass |  | 4.25 s |
| qwen3-embedding-0.6b | context | Pass | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Pass | 14 | 2.125 s |
| qwen3.5-0.8b | context | Pass | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Pass | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Pass |  | 2.125 s |
| qwen3.5-0.8b | tools | Pass |  | 4.416 s |
| qwen3.5-2b | context | Pass | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Pass | 17 | 4.519 s |
| qwen3.5-2b | stream | Pass |  | 3.736 s |
| qwen3.5-2b | tools | Pass |  | 5.046 s |
| qwen3.5-4b | context | Pass | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Pass | 15 | 19.935 s |
| qwen3.5-4b | stream | Pass |  | 17.496 s |
| qwen3.5-4b | tools | Pass |  | 7.308 s |
| qwen3.5-4b | vision | Pass | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Pass | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Pass | 70 | 4.386 s |
| qwen3.5-9b | context | Pass | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Pass | 17 | 3.88 s |
| qwen3.5-9b | stream | Pass |  | 3.378 s |
| qwen3.5-9b | tools | Pass |  | 10.204 s |
| qwen3.5-9b | vision | Pass | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Pass | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Pass | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Pass |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Pass |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Pass | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Pass | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Pass | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Pass | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Pass |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Pass |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Pass | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Pass | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Pass |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Pass | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Pass | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Pass | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Pass | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Pass |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Pass |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Pass |  | 3.86 s |

### System B

| Model route label | Check | Outcome | Input tokens | Request duration |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Pass | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Pass | 21 | 15.261 s |
| gemma-4-12b-it | stream | Pass |  | 148.792 s |
| gemma-4-12b-it | tools | Pass |  | 34.124 s |
| gemma-4-12b-it | vision | Pass | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Pass | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Pass | 120 | 32.511 s |
| gemma3-4b | context | Pass | 65,584 | 67.382 s |
| gemma3-4b | quick | Pass | 15 | 6.329 s |
| gemma3-4b | stream | Pass |  | 24.138 s |
| gemma3-4b | vision | Pass | 306 | 7.018 s |
| gemma3-4b | vision_context | Pass | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Pass | 306 | 5.762 s |
| gpt-oss-20b | context | Pass | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Pass | 72 | 16.583 s |
| gpt-oss-20b | stream | Pass |  | 32.075 s |
| gpt-oss-20b | tools | Pass |  | 28.102 s |
| nomic-embed-text | context | Incomplete | 2,048 |  |
| nomic-embed-text | quick | Pass |  | 7.117 s |
| qwen3-14b | context | Incomplete |  | 1800.09 s |
| qwen3-14b | quick | Pass | 15 | 37.199 s |
| qwen3-14b | stream | Pass |  | 35.471 s |
| qwen3-14b | tools | Pass |  | 87.554 s |
| qwen3-8b | context | Excluded below 65K, excluded |  |  |
| qwen3-8b | quick | Excluded below 65K, pass | 15 | 21.059 s |
| qwen3-8b | stream | Excluded below 65K, excluded |  |  |
| qwen3-8b | tools | Excluded below 65K, excluded |  |  |
| qwen3.5-9b | context | Pass | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Pass | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Pass |  |  |
| qwen3.5-9b | quick | Pass | 15 | 25.881 s |
| qwen3.5-9b | stream | Pass |  | 143.44 s |
| qwen3.5-9b | tools | Pass |  | 31.812 s |
| qwen3.5-9b | vision | Pass | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Pass | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Pass | 75 | 28.626 s |

### System C

| Model route label | Check | Outcome | Input tokens | Request duration |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Pass | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Pass | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Pass | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Pass | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Pass | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Pass | 27 | 20.98 s |
| gemma-4-12b-it | quick | Pass | 21 | 16.447 s |
| gemma-4-12b-it | stream | Pass |  | 15.175 s |
| gemma-4-12b-it | tools | Pass |  | 37.821 s |
| gemma-4-12b-it | vision | Pass | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Pass | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Pass | 120 | 31.25 s |
| gemma3-4b | aperture_context | Pass | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Pass | 24 | 5.42 s |
| gemma3-4b | aperture_short | Pass | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Pass |  | 3.72 s |
| gemma3-4b | context | Pass | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Pass | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Pass |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Pass |  |  |
| gemma3-4b | gateway_short_via_system_f | Pass |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Pass |  | 6.06 s |
| gemma3-4b | quick | Pass | 15 | 5.163 s |
| gemma3-4b | stream | Pass |  | 24.691 s |
| gemma3-4b | vision | Pass | 306 | 7.318 s |
| gemma3-4b | vision_context | Pass | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Pass | 306 | 5.831 s |
| gpt-oss-20b | context | Pass | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Pass | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Inconsistent |  |  |
| gpt-oss-20b | quick | Pass | 72 | 21.603 s |
| gpt-oss-20b | stream | Pass |  | 31.957 s |
| gpt-oss-20b | tools | Pass |  | 26.096 s |
| nomic-embed-text | context | Excluded below 65K, incomplete | 2,048 |  |
| nomic-embed-text | quick | Excluded below 65K, pass |  | 4.178 s |
| qwen3-14b | context | Excluded below 65K, incomplete |  | 1800.06 s |
| qwen3-14b | quick | Excluded below 65K, pass | 15 | 35.809 s |
| qwen3-14b | stream | Excluded below 65K, pass |  | 35.43 s |
| qwen3-14b | tools | Excluded below 65K, pass |  | 87.723 s |
| qwen3-8b | context | Excluded below 65K, excluded |  |  |
| qwen3-8b | quick | Excluded below 65K, pass | 15 | 21.293 s |
| qwen3-8b | stream | Excluded below 65K, incomplete |  | 900.01 s |
| qwen3-8b | tools | Excluded below 65K, excluded |  |  |
| qwen3.5-9b | context | Pass | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Pass | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Pass | 21 | 72.14 s |
| qwen3.5-9b | quick | Pass | 15 | 24.635 s |
| qwen3.5-9b | stream | Pass |  | 143.157 s |
| qwen3.5-9b | tools | Pass |  | 30.395 s |
| qwen3.5-9b | vision | Pass | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Pass | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Pass | 75 | 28.645 s |

### System D

| Model route label | Check | Outcome | Input tokens | Request duration |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Pass | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Pass | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Pass | 34 | 30.74 s |
| gemma-4-12b-it | quick | Pass | 21 | 15.05 s |
| gemma-4-12b-it | stream | Pass |  | 14.722 s |
| gemma-4-12b-it | tools | Pass |  | 33.869 s |
| gemma-4-12b-it | vision | Pass | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Pass | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Pass | 120 | 29.978 s |
| gemma3-4b | context | Pass | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Failed | 67,252 | 62.07 s |
| gemma3-4b | quick | Pass | 15 | 5.151 s |
| gemma3-4b | stream | Pass |  | 22.552 s |
| gemma3-4b | vision | Pass | 306 | 8.276 s |
| gemma3-4b | vision_context | Pass | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Pass | 306 | 5.651 s |
| gpt-oss-20b | context | Pass | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Pass | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Pass | 84 | 15.96 s |
| gpt-oss-20b | quick | Pass | 72 | 15.431 s |
| gpt-oss-20b | stream | Pass |  | 31.052 s |
| gpt-oss-20b | tools | Pass |  | 23.65 s |
| nomic-embed-text | context | Incomplete | 2,048 |  |
| nomic-embed-text | quick | Pass |  | 2.798 s |
| qwen3-14b | context | Incomplete | 40,939 | 872.209 s |
| qwen3-14b | quick | Pass | 15 | 36.021 s |
| qwen3-14b | stream | Pass |  | 33.491 s |
| qwen3-14b | tools | Pass |  | 82.471 s |
| qwen3-8b | context | Incomplete |  | 1800.07 s |
| qwen3-8b | quick | Pass | 15 | 19.283 s |
| qwen3-8b | stream | Pass |  | 19.401 s |
| qwen3-8b | tools | Pass |  | 65.054 s |
| qwen3.5-9b | context | Pass | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Pass | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Pass | 29 | 94.48 s |
| qwen3.5-9b | quick | Pass | 15 | 27.16 s |
| qwen3.5-9b | stream | Pass |  | 28.62 s |
| qwen3.5-9b | tools | Pass |  | 28.129 s |
| qwen3.5-9b | vision | Pass | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Pass | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Pass | 75 | 27.602 s |

### System E

| Model route label | Check | Outcome | Input tokens | Request duration |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Pass | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Pass | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Pass |  | 28.136 s |
| gemma-4-e4b-it | tools | Pass |  | 56.756 s |
| granite-4.0-h-tiny | context | Pass | 65,566 |  |
| granite-4.0-h-tiny | quick | Pass | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Pass |  | 27.798 s |
| granite-4.0-h-tiny | tools | Pass |  | 43.304 s |
| granite-4.2-3b | context | Pass | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Pass | 20 | 14.569 s |
| granite-4.2-3b | stream | Pass |  | 6.948 s |
| granite-4.2-3b | tools | Pass |  | 56.376 s |
| qwen3-embedding-0.6b | context | Pass | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Pass | 14 | 9.592 s |
| qwen3.5-0.8b | context | Pass | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Pass | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Pass |  | 11.163 s |
| qwen3.5-0.8b | tools | Pass |  | 39.214 s |
| qwen3.5-2b | context | Pass | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Pass | 15 | 12.509 s |
| qwen3.5-2b | stream | Pass |  | 26.165 s |
| qwen3.5-2b | tools | Pass |  | 42.056 s |
| qwen3.5-4b | context | Pass | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Pass | 15 | 26.736 s |
| qwen3.5-4b | stream | Pass |  | 26.02 s |
| qwen3.5-4b | tools | Pass |  | 57.293 s |
| qwen3.5-4b | vision | Pass | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Pass | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Pass | 72 | 9.96 s |

### System F

| Model route label | Check | Outcome | Input tokens | Request duration |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Pass | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Pass | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Pass |  | 28.042 s |
| gemma-4-e4b-it | tools | Pass |  | 73.891 s |
| granite-4.0-h-tiny | context | Pass | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Pass | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Pass |  | 27.296 s |
| granite-4.0-h-tiny | tools | Pass |  | 75.377 s |
| granite-4.2-3b | context | Pass | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Pass | 20 | 15.703 s |
| granite-4.2-3b | stream | Pass |  | 35.482 s |
| granite-4.2-3b | tools | Pass |  | 52.539 s |
| qwen3-embedding-0.6b | context | Pass | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Pass | 14 | 8.122 s |
| qwen3.5-0.8b | context | Pass | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Pass | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Pass |  | 13.266 s |
| qwen3.5-0.8b | tools | Pass |  | 40.825 s |
| qwen3.5-2b | context | Pass | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Pass | 15 | 16.738 s |
| qwen3.5-2b | stream | Pass |  | 25.29 s |
| qwen3.5-2b | tools | Pass |  | 47.444 s |
| qwen3.5-4b | context | Pass | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Pass | 15 | 33.039 s |
| qwen3.5-4b | stream | Pass |  | 25.658 s |
| qwen3.5-4b | tools | Pass |  | 71.731 s |
| qwen3.5-4b | vision | Pass | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Pass | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Pass | 70 | 27.518 s |

### System G

| Model route label | Check | Outcome | Input tokens | Request duration |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Pass | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Pass | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Pass |  | 43.549 s |
| gemma-4-e4b-it | tools | Pass |  | 66.616 s |
| granite-4.0-h-tiny | context | Pass | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Pass | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Pass |  | 31.751 s |
| granite-4.0-h-tiny | tools | Pass |  | 63.338 s |
| granite-4.2-3b | context | Pass | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Pass | 20 | 23.355 s |
| granite-4.2-3b | stream | Pass |  | 28.75 s |
| granite-4.2-3b | tools | Pass |  | 44.226 s |
| qwen3-embedding-0.6b | context | Pass | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Pass | 14 | 8.924 s |
| qwen3.5-0.8b | context | Pass | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Pass | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Pass |  | 15.095 s |
| qwen3.5-0.8b | tools | Pass |  | 36.672 s |
| qwen3.5-2b | context | Pass | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Pass | 15 | 20.949 s |
| qwen3.5-2b | stream | Pass |  | 25.194 s |
| qwen3.5-2b | tools | Pass |  | 37.552 s |
| qwen3.5-4b | context | Pass | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Pass | 15 | 41.84 s |
| qwen3.5-4b | stream | Pass |  | 40.812 s |
| qwen3.5-4b | tools | Pass |  | 54.999 s |
| qwen3.5-4b | vision | Pass | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Pass | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Pass | 70 | 26.283 s |

## How I tested Hermes viability

I used a synthetic marker near the beginning of a long prompt and asked for the marker after the filler. The response had to return the expected value. Server-reported input tokens determined the request size. A model answering normally after a large prompt still failed when the opening marker was wrong.

The Qwen3.5 35B progression used numbered filler records, temperature 0, and increasing lengths of 3,800, 6,800, 10,000, and 13,600 records. Those stages returned 69,429, 124,179, 182,579, and 248,279 prompt tokens. The model stayed loaded between stages, which allowed prefix reuse. The separate Qwen3.6 near-limit checks reported zero cached tokens.

The 0.8B long prompt repeated `river stone lantern orchard circuit velvet compass marble` 8,400 times between an opening answer key and a final recall question. The native run sent `think:false`, `num_ctx:131072`, `stream:false`, and `keep_alive:0`. The OpenAI-compatible route used `reasoning_effort:"none"`. The broker enforced nonthinking mode for its route, so gateway callers did not need a client override.

### Tool, vision, and release checks

Tool tests checked the request and the answer after a tool result returned. One simple test used `add_numbers(7, 11)` and expected 18. The Qwen3.5 35B test used `lookup_square` and expected 49. GPT-OSS used an inventory lookup and had to incorporate the returned inventory result.

Vision checks used red and blue image questions, reversed image order, and long prompts containing image colors plus opening and ending markers. The Qwen3.5 35B test used a 256 × 256 red PNG. The broker needed an image-content conversion fix before this request passed. The System E 4B long vision test required both markers and the ordered colors to survive the input.

I checked GPU memory, model residency, temperatures, host-memory pressure, OOM events, and GPU faults around the long runs. The Qwen3.5 35B guard also checked release after a controlled interruption. Later client-cancellation and queued-request checks exercised the broker path. Two queued requests prove request handling under the tested load, rather than two independent simultaneous GPU backends.

### Reading the performance results

Request durations include long-input prefill and the returned answer. They are not generation tokens per second. First-content delay matters for streaming, and cached-prefix progressions need their own interpretation.

The successful larger System A and System C follow-up runs used dedicated inference windows with mining inactive. Models unloaded after those requests. Mining restoration across all seven systems happened at the end of the test window. These results describe model service during an inference window, rather than simultaneous mining and inference.

## Backend profiles used in the tests

Choose the profile attached to the workload you want to reproduce. Quantization, runtime context, cache type, reasoning mode, and GPU placement all affect the result.

| System and model | Tested backend profile |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, f16 KV cache, both 16GB RTX 5060 Ti cards, 64 GiB host RAM, 262,144 runtime context for the large progression. Native requests used `think:false`, temperature 0, streaming, and five-minute keep-alive between stages. Gateway requests used the broker and LiteLLM. No request output cap. |
| A, Qwen3.8 27B | On-demand llama.cpp through the broker and LiteLLM, 262,144 runtime context, one inference slot, Q4 K/V cache, both RTX 5060 Ti cards. The 66,007-token request used no output cap. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, 131,072 context, INT8 KV cache, one selected GPU, 55 GiB process-group memory limit, 30-minute runtime limit, lazy load, 60-second idle unload. Pilot long answer: 217 output tokens. Near-limit gateway answer: 11 output tokens, no request output cap. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, 98,304 context, Q4 KV cache, 8 GiB resident expert cache, both RTX 5060 Ti cards. Pilot memory limit 52 GiB, later route 54 GiB. Pilot long answer: 10 output tokens. Earlier larger context/cache combinations stopped at memory limits. |
| A, Granite 4.2 8B | Q6_K GGUF weights, llama.cpp pooled worker, 131,072 context, Q4_0 K/V cache, `--n-predict -1`. Long request used temperature 0, streaming usage, and no output cap. |
| A, DeepSeek Coder V2 16B | Q4_0 GGUF weights, Ollama 0.34.2, two RTX 5060 Ti cards, 64 GiB host RAM. Separate f16, Q4_0, and Q8_0 cache trials used the runtime contexts shown in the comparison table. No request output cap. |
| B, C, D, audited Ollama service | Ollama 0.34.2, 131,072 context, parallelism 1, one loaded model, queue size 128, keep-alive 0, Flash Attention, Q4_0 KV cache. |
| B, Qwen3.5 9B gateway pilot | LiteLLM route timeout 1,800 seconds, zero retries, no context or output-token cap. Both sentinels retained at 72,265 input tokens. The separate mining-recovery check passed. |
| C, Qwen3.5 0.8B | Q8_0 weights on one RTX 2000E Ada at a 30 W power profile. Runtime context 131,072. Native `think:false`, OpenAI-compatible `reasoning_effort:"none"`, no output cap. The broker alias pinned the runtime context and enforced nonthinking mode. |
| C, Gemma 4 12B-IT | Single-GPU Ollama profile, 131,072 runtime context, streamed and non-streamed Aperture requests without an output cap. The direct Aperture run peaked at 75 C and 30.64 W under the configured 30 W profile, then unloaded. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Exact installed artifacts tested through Aperture, 131,072 runtime context, full residency on one GPU, natural completion without a request output cap. |
| E, F, G, llama.cpp chat workers | Build 11669, 99 GPU layers, parallelism 1, Flash Attention, Q4_0 K/V cache, `--n-predict -1`. Runtime context varied by model family. |

The recorded service profiles describe their own runtime configurations. The separately tested System A f16-cache Qwen3.5 35B profile does not inherit the Q4_0 cache settings of the smaller Ollama systems.

### Model fingerprints for the new retained-input runs

These model identifiers distinguish the tested artifacts from other downloads or aliases with similar names.

| Artifact | Quantization | Recorded digest or file SHA-256 |
|---|---|---|
| Qwen3.5 35B-A3B Ollama tag | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Qwen3.5 0.8B base Ollama tag | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Granite 4.2 8B GGUF file | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Ollama manifest digests and weight-file SHA-256 values identify different objects. Match the identifier to the artifact type in the table.

## What I would run with Hermes

I would make Qwen3.5 35B the main high-context route on the two-card RTX 5060 Ti system. Its 239,153-token gateway retention result, separate tool and vision passes, and verified request release make the choice stronger than a model advertised with a large context window. I would keep Qwen3.8 27B available for the faster matched 66K response and Qwen3.6 available when using one card matters.

On the RTX 2000E Ada systems, I would choose the verified System C Gemma 3 4B route for the tested long-input response workload. I would trial the nonthinking Qwen3.5 0.8B route for narrow recall and extraction. Larger Gemma, Qwen, and GPT-OSS routes suit work where their tested four-to-five-minute initial response is acceptable. I would exclude the failed System D Gemma 3 route from the selection.

For the 8GB RTX 3060 Ti and RTX 3070 cards, I would start with Qwen3.5 2B or 4B. Their 65K text results and the 4B image checks support a useful starting configuration without dedicating the two 16GB cards to every request. Flash Next's memory pressure and DeepSeek Coder V2's incomplete 65K behavior make them weaker defaults on the tested profiles.

The tests support these model and system choices for specific workflows. Retained input, a correct tool round trip, image recognition, and clean release each answer a different part of Hermes viability. A dependable setup needs the behaviors used by your agent, with enough context left for the answer and tool traffic.

## Sources and related reading

- [Hermes Agent provider setup and context requirements](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [NVIDIA GeForce RTX 3060 Ti specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [NVIDIA GeForce RTX 5060 Ti specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Hermes Agent overview](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Choosing a local model backend](/hermes-local-ai-broker-course/02-choose-a-backend/)
