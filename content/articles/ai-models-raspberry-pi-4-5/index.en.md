---
title: "Which AI Models Can Run on a Raspberry Pi 4 or 5?"
date: 2026-09-20
lastmod: 2026-09-20
toc: true
draft: false
description: "Use measured Raspberry Pi 4 and 5 results to choose local language models by memory, speed, and workload, from tiny LFM2.5 models to 3B and larger options."
genre: ["Raspberry Pi", "Artificial Intelligence", "Self Hosting"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "local AI", "small language models", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "model quantization", "edge AI"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Two Raspberry Pi computers on a dark desk with blue and amber neural network illustrations above them"
coverCaption: "Illustration of local AI models running on Raspberry Pi hardware."
---

A Raspberry Pi can run a useful language model locally, but the model must fit the board's memory and the response time your application can tolerate. A 2 GB Raspberry Pi 4 is best suited to models below about one billion parameters. An 8 GB Raspberry Pi 5 can run compact 1B–3B models comfortably and load some larger quantized models with substantial compromises.

We benchmarked these models ourselves through Ollama on a **2 GB Pi 4B** and an **8 GB Pi 5**, both using microSD storage. The runs behind the tables used the same five short assistant prompts, system prompt, fixed seed, and 140-token output cap. We unloaded other models before each run and measured cold-load time, time to first visible token, total reply time, output speed, and peak resident memory. These were single-pass tests of a short-reply workload, so the results are sizing examples rather than universal speed or answer-quality rankings. The Pi 5's [Cortex-A76 CPU and available memory configurations](https://www.raspberrypi.com/products/raspberry-pi-5/) also differ materially from the Pi 4's [Cortex-A72 platform](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## The model types that make sense

| Kind of model | Examples from the measurements | Practical use |
|---|---|---|
| Tiny text models, about 230M–600M parameters | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Short local commands, summaries, and constrained question answering; the best starting point for a 2 GB Pi 4 |
| Compact text models, about 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | More room for nuanced instructions on a Pi 5 or a higher-memory Pi 4, with slower replies than the tiniest models |
| Quantized 3B–4B text models | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | More capable candidates for an 8 GB Pi 5 when a wait of several seconds per reply is acceptable |
| Larger sparse or hybrid models | LFM2.5 8B | Technically runnable on the tested 8 GB Pi 5, but with a large memory footprint and long cold load |

These are **text-generation** results. They do not establish performance for image generation, speech recognition, vision, or training. “Runs” also means more than fitting the model file on a card: the runtime, context cache, operating system, and other services need RAM. Quantization reduces the weight file size, but it can reduce answer quality, especially at extreme settings such as 1-bit weights.

### What our numbers measure

The benchmark sent short factual, procedural safety, retrieved-context, weather, and help prompts to Ollama's chat API. Each model saw the same prompt set and seed. Before timing a model, we unloaded it so the next request would include a cold load; the reported **wall time** is the complete request, while **tokens per second** describes only output generation. We also recorded the first *visible* token, which matters when a model spends time reasoning before it answers.

For memory, we sampled the Pi's available RAM and swap alongside the resident memory of Ollama and its inference process during each request. The **RSS** figures below are process-resident memory, not the entire host's memory demand. File-backed pages, the operating system, a browser, or another local service can still make a nominally fitting model swap. The tables use the original five-prompt, single-pass runs. We later extended the harness with a news prompt and reply-rule checks; those checks clarify what to look for, but they do not turn the earlier timings into six-prompt compliance results.

Neither tokens per second nor parameter count is a quality score. A model can emit text quickly yet omit a requested source, exceed a word budget, or produce an unfinished sentence. We would compare models on the prompts we actually plan to send, then inspect their answers before choosing one for an application.

## Raspberry Pi 4: favor the smallest models

The tested 2 GB Pi 4 had limited headroom. The smallest LFM2.5 models completed all five prompts, as did `qwen2.5:0.5b`. They are sensible choices for brief offline replies or a small local assistant.

| Model | Model file | Measured output speed | Average reply time | Observed memory or outcome |
|---|---:|---:|---:|---|
| LFM2.5-230M, imported GGUF | 0.25 GB | 12.8 tokens/s | 7.2 s | 383 MB peak resident memory; 5/5 prompts |
| LFM2.5-350M, imported GGUF | 0.38 GB | 8.6 tokens/s | 8.6 s | 516 MB peak resident memory; 5/5 prompts |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 prompts; available directly in Ollama |
| MiniCPM5-1B, imported GGUF, reasoning off | 0.69 GB | 5.9 tokens/s | 12.2 s | 883 MB peak resident memory; 5/5 prompts |
| MiniCPM5-1B, imported GGUF, default reasoning | 0.69 GB | 5.7 tokens/s | 33.3 s | Only 1/5 prompts returned a useful visible reply |
| `qwen3:0.6b`, default reasoning | 0.52 GB | 6.4 tokens/s | 40.4 s | One empty reply; board rebooted |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, no swap or reboot; slow but stable |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | Heavy swapping; board rebooted during testing |
| `qwen3.5:0.8b` | 1.04 GB | — | — | Did not complete; board rebooted |

The Pi 4 results are especially sensitive to the rest of the system. We observed board resets during larger-model tests, including a `qwen3.5:0.8b` run that never completed. That is evidence about our 2 GB setup, rather than a claim that every Pi 4 or every 1B model will reboot. A 4 GB or 8 GB Pi 4 has more memory, but its CPU will still make inference slower than on the tested Pi 5. We did not directly benchmark those Pi 4 memory variants.

One early Pi 4 pass also appeared much worse than the final measurements: roughly 625 MB of staged GGUF files sat in a RAM-backed `/tmp`, leaving only about 500–600 MB free and pushing hundreds of megabytes into swap. After moving those files to persistent storage, the small-model results above gave a more useful picture of inference memory. On a 2 GB board, even the *location of a download* can distort a benchmark.

**Recommendation:** The imported LFM2.5-350M is our default for this 2 GB board. It remained stable at **516 MB RSS**, left about **1 GB of RAM available**, and passed **5/6** reply-rule checks in the Pi 4 compliance pass. It did miss source names in repeated Pi 5 testing, so applications that require attribution should check for it. Choose LFM2.5-230M when latency and memory headroom matter most: it was faster and lighter, but in one medical-context answer it garbled “nausea or vomiting” into “nausea/ventilator use.” That content error makes it a weaker default for safety or health replies despite its higher repeated mechanical compliance score. Choose `qwen2.5:0.5b` if you need a model from the [Ollama registry](https://ollama.com/library/qwen2.5/tags), while accounting for its weaker instruction compliance. `granite4:350m` stayed stable but took longer and used more memory; MiniCPM5-1B is viable only when the client disables reasoning. Avoid Gemma 3 1B and Qwen3.5 0.8B on this specific 2 GB setup because our runs triggered resets.

## Raspberry Pi 5: more choice, with a speed tradeoff

The 8 GB Pi 5 handled all **25 models** in our speed-and-memory benchmark. The table includes every run, including models we do not recommend for this short-reply workload. A dagger marks an imported GGUF. “Think off” records the setting used for the speed run; the separate compliance pass did not necessarily use that setting.

| Model | File GB | Output tok/s | Reply s | Peak RSS MB | Short-reply assessment |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Lowest latency; 78% repeated compliance |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Skip: 1-bit weights and 3/6 single-pass compliance |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Fast, but missed source citation in 5/18 repeats |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Easy registry option; 61% repeated compliance |
| `qwen3:0.6b`, think off | 0.52 | 23.0 | 4.3 | 1,069 | Conditional: 4/6 compliance pass, reasoning setting matters |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Experimental 1-bit model; 6/6 single pass is unconfirmed |
| `minicpm5-1b` †, think off | 0.69 | 18.4 | 5.1 | 869 | Conditional: default reasoning gave empty replies |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Fits, but slower and larger than small LFM2.5 |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Best overall for our workload; 89% repeated compliance |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Registry alternative; 5/6 compliance pass |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Best registry-only repeated compliance: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6 compliance pass; Gemma 3 1B followed rules better |
| `qwen3.5:0.8b`, think off | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 with default reasoning; avoid without thinking control |
| `spark-x2.5-1.7b` †, think off | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 with default reasoning; avoid without thinking control |
| `qwen3:1.7b`, think off | 1.36 | 8.1 | 12.4 | 1,867 | Conditional; more memory and delay than smaller choices |
| `minicpm5-2b` †, think off | 1.56 | 7.7 | 10.9 | 1,787 | Conditional; 5/6 single pass, extra bullets |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Trial 3B option; 5/6 single pass |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Skip for interactive use: slow decode |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Alternative 3B trial; no compliance run reported |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Fits, but slower replies than smaller alternatives |
| `qwen3.5:2b`, think off | 2.74 | 5.0 | 16.1 | 3,627 | High memory and delay; no compliance run reported |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Skip for responsive replies; 14.3 s to first token |
| `ling-3.0-tiny` †, think off | 4.82 | 9.9 | 19.4 | 5,071 | Large footprint; 5/6 single pass with grounding failure |
| `lfm2.5:8b`, think off | 5.16 | 8.7 | 54.6 | 5,317 | Fits tightly; 34.4 s cold load and overlong answers |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Skip: swap pressure alongside other Pi services |

† Imported GGUF. Reply times and memory figures are from the five-prompt Pi 5 speed run; compliance figures come from separate six-prompt tests. A model without a compliance score was not shown to obey the reply rules.

The small LFM2.5 models were the fastest *for this short-reply workload*. The 1.2B version offers a practical middle ground on the tested Pi 5. Gemma 3 1B is a registry-only alternative with better repeated reply-rule compliance than Qwen2.5 1.5B in our later tests. A 3B model may be worth the slower output for prompts that need more capacity, but these timings alone do not prove which model gives the best answers.

Cold-load and first-token delays change the experience. LFM2.5-230M loaded in about **0.21 seconds** and produced a visible token in **0.37 seconds** on the Pi 5. Qwen2.5 1.5B took **2.59 seconds** to load and **3.66 seconds** to its first visible token; Qwen2.5 3B took **5.60** and **7.97 seconds**, respectively. For an occasional question, those delays may matter more than the output rate once generation begins. For a continuously loaded model, they matter less, but keeping a model resident consumes memory between requests.

Other measured candidates illustrate why we do not rank by parameter count alone. With reasoning disabled, `qwen3:0.6b` reached **23.0 tokens/s** on the Pi 5 at **1,069 MB RSS**, while imported MiniCPM5-1B reached **18.4 tokens/s** at **869 MB RSS**. `granite4:350m` needed a **0.71 GB** download and generated **12.1 tokens/s**, despite its 350M label. Model packaging and architecture change the relationship between name, file size, memory, and speed.

If your client can reliably send `think: false`, Qwen3 0.6B and MiniCPM5-1B are reasonable experiments when you want alternatives to LFM2.5. MiniCPM5-2B, Qwen3 1.7B, and Spark-X2.5 1.7B also ran on the Pi 5, but none offered a clear speed-and-memory advantage over our primary choices. The compliance test used default reasoning for MiniCPM5-1B and Spark-X2.5; its empty replies should not be presented as the outcome of their think-off speed runs. Conversely, a fast think-off timing does not establish that a bridge which omits that flag will receive a usable answer.

If installation simplicity matters more than raw speed, Gemma 3 1B and Llama 3.2 1B are plausible registry choices on the 8 GB Pi 5. Gemma 3 1B followed the tested reply rules in **15/18** repeated replies. Llama 3.2 1B passed **5/6** in one pass, so its compliance estimate is less certain. Qwen2.5 1.5B loaded and answered faster than Gemma 3 1B in our timing run, but passed only **4/6** reply-rule checks in its single compliance pass. Choose between them using the requirement that matters to your own prompts.

For occasional longer or harder text prompts, the quantized Qwen2.5 3B and Llama 3.2 3B are the 3B candidates with manageable memory use on our 8 GB Pi 5. We measured their speed and memory, and Qwen2.5 3B passed **5/6** in one compliance pass; we did not publish a comparable compliance run for Llama 3.2 3B. Their larger parameter counts are a reason to *test* them on tasks where smaller models fall short, not proof that they answered those tasks better. Granite 4 Micro and Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny, and Gemma 3n E2B all fit or loaded in our Pi 5 trials, but offered less attractive latency, memory headroom, or reply reliability for this short-response application.

The two Bonsai models demonstrate the cost of extreme quantization. Their Q1_0 files were strikingly small for 1.7B and 4B parameter names, yet the 1.7B model passed only **3/6** reply-rule checks. The 4B model passed a single six-prompt compliance pass, but took **18.1 seconds** per reply and has no repeated compliance confirmation. We would treat both as experiments rather than default recommendations, especially where answer quality matters.

The 8B LFM2.5 result needs context: its hybrid design uses fewer active parameters per token, so its decode rate exceeded the measured 3B dense models. It still took **34.4 seconds to load cold** from microSD and used over **5.3 GB resident memory**. It is a demonstration of what fits, not a comfortable default for a Pi that also runs other services. The measured `gemma3n:e2b` similarly used about 5.3 GB resident memory and caused swapping alongside the other services on the test host.

The LFM2.5 8B run also reached the full **140-token cap** instead of keeping its response brief. The 4B Gemma 3 run took **14.3 seconds** to its first token and **30.3 seconds** for the complete reply. Both can be loaded on this Pi 5, but neither behaved like a responsive small assistant in our tests. A tiny model with an appropriately short answer may serve a radio or command interface better than a larger model with a faster decode rate on paper.

## Memory, reasoning, and model format

A useful first estimate from our measurements is **model download size × 1.4** for resident inference memory. It is only a rule of thumb: context length, runtime settings, model architecture, and other processes can change the requirement. Check available memory while generating, keep only one model loaded on a small host, and leave room for the OS. A 4 GB board can reasonably start with the tiny or compact models, but our 4 GB recommendations are extrapolations rather than direct 4 GB tests.

For example, a 0.73 GB LFM2.5-1.2B file corresponded to about **967 MB RSS** on the Pi 5, while the 0.99 GB Qwen2.5 1.5B file reached **1,361 MB RSS**. The rule works reasonably for those models, but it is not a hard limit. Plan for more than the measured model process if the Pi also runs an interface, search index, local library, or other background service. Watch swap use during a real request; a model that technically loads while constantly swapping is not a practical fit.

Some models generate an internal reasoning block before their visible answer. In our tests, `qwen3:0.6b` on the 2 GB Pi 4 took much longer to produce visible text, and MiniCPM5-1B answered only one of five prompts with its default reasoning setting versus five of five with reasoning disabled. For a short response budget, set `think: false` in a compatible Ollama API request, or select a model that does not default to reasoning. This setting applies to supported models and clients; it is not a universal speed switch.

The distinction matters because a token cap can include tokens spent on reasoning even when the user sees no answer. On the Pi 4, default-thinking `qwen3:0.6b` averaged **40.4 seconds per request**, and one prompt produced an empty visible reply. MiniCPM5-1B averaged **33.3 seconds** with its default setting versus **12.2 seconds** with reasoning disabled. We also disabled reasoning for the Pi 5 runs of Qwen3, Qwen3.5, MiniCPM5, Ling-3.0, and Spark-X2.5 where indicated in our records. Compare a model under the exact reasoning setting your client will use.

### Check whether the reply is usable

For our short mesh-assistant workload, the response contract is as important as speed: at most **90 words**, no more than **three bullets**, plain text, a finished sentence, and use of supplied retrieval context with its source named. The bridge divides text into **180-character chunks**. A long answer occupies more radio airtime, even if the model generated it quickly.

The later version of our benchmark checks for empty replies, a prompt-specific word limit, too many bullets, Markdown tables or code fences, an unfinished ending, missing terms from supplied context, and a missing source name. When we scored replies against the deployed assistant prompt, small models breached these rules regularly. The most consequential failures were **empty replies** when reasoning consumed the token budget, followed by answers that ignored retrieved context or omitted its source. Going over the word limit or using too many bullets still delivered visible text, but wasted airtime. These are mechanical checks, not a substitute for reading the answer: they cannot establish factual accuracy or whether safety advice is sound.

#### Repeated Pi 5 compliance results

We first ran six prompts once per model with a **220-token cap** and the deployed system prompt. Models that looked plausible were then tested twice more with a different seed, giving **18 replies per model**. A perfect single pass did not guarantee a perfect repeat. The repeated results below provide a firmer comparison for the short mesh replies we tested:

| Model | Replies that followed all checked rules | Main observed failures |
|---|---:|---|
| Imported LFM2.5-1.2B | 16/18 (89%) | Two unfinished replies |
| `gemma3:1b` | 15/18 (83%) | Three unfinished replies |
| Imported LFM2.5-230M | 14/18 (78%) | Unfinished replies and missing source names |
| Imported LFM2.5-350M | 13/18 (72%) | Missing source names |
| `qwen2.5:0.5b` | 11/18 (61%) | Too many bullets, excess words, missing source names |

On the **2 GB Pi 4**, the separate six-prompt compliance pass found **5/6** for LFM2.5-350M, **4/6** for LFM2.5-230M, and **2/6** for Qwen2.5-0.5B. MiniCPM5-1B improved from **1/6** with default reasoning to **5/6** with reasoning disabled. These Pi 4 scores are single-pass results, so we give more weight to the repeated Pi 5 results when discussing general instruction-following behavior, while using the Pi 4 runs to judge stability and speed on that board.

The failures have different consequences. An **empty** reply gives the user nothing; an answer that ignores supplied material can be misleading. A missing source name prevents readers from checking attribution. Extra bullets or words mainly consume additional 180-character packets. An unfinished sentence may indicate truncation. The LFM2.5-230M medical-term error is a reminder that a reply can pass these mechanical checks and still be wrong. None of the five repeated candidates followed every rule in all 18 replies, so an application that requires a strict length or format should enforce it after generation as well and review high-stakes content separately.

We also checked the actual bridge endpoint, Ollama's OpenAI-compatible `/v1/chat/completions`, with retrieved WikiMed context. On the Pi 5, LFM2.5-1.2B returned a 28-word answer using six supplied terms; Qwen2.5-0.5B returned 38 words using seven. Both fit within two 180-character packets. That endpoint check confirms the imported LFM2.5 model works through the bridge's request path, but one successful answer is not a reliability guarantee.

Ollama publishes many ready-to-pull models, including [Qwen2.5's 0.5B, 1.5B, and 3B variants](https://ollama.com/library/qwen2.5/tags). We imported the small LFM2.5 models from [Liquid AI's GGUF releases](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main) into Ollama. Check the exact tag or GGUF filename before downloading: model registries and repositories can change. Keep GGUF downloads on persistent storage; in our tests, staging files in a RAM-backed `/tmp` consumed scarce Pi 4 memory.

### Registry tags and GGUF imports

An Ollama tag is the shortest path to a first test: pull the exact tag and run it. The small LFM2.5 models in our tables were **GGUF imports**, not tags named `lfm2.5-230m`, `lfm2.5-350m`, or `lfm2.5-1.2b` in Ollama's public library. GGUF is a model-file format; names such as `Q8_0` and `Q4_K_M` identify quantization choices. The 230M and 350M LFM2.5 files we used were Q8_0, while the 1.2B file was Q4_K_M. Consequently, the same parameter count downloaded in another quantization may not have the same file size, memory use, or quality.

To import the tested 350M variant, download its GGUF to a directory on persistent storage, create a Modelfile pointing to it, and let Ollama copy it into its model store:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

The import temporarily needs space for both the downloaded file and Ollama's stored copy. We used resumable downloads because long GGUF transfers sometimes broke mid-file. Before importing a downloaded GGUF, compare its SHA-256 with the file hash published by its source; a partial transfer can otherwise look like a model problem. On our Pi setup, `/tmp` was RAM-backed, so staging a GGUF there reduced the memory available for inference.

## A practical starting point

| Hardware and goal | First model to try | Why |
|---|---|---|
| 2 GB Pi 4, default | Imported LFM2.5-350M | Stable at 516 MB RSS with about 1 GB available; selected after a medical-term error from 230M |
| 2 GB Pi 4, lowest latency | Imported LFM2.5-230M | 383 MB RSS and 7.2-second average reply; verify content carefully, especially for health or safety questions |
| 2 GB Pi 4, registry-only | `qwen2.5:0.5b` | Direct Ollama pull and stable in our five-prompt Pi 4 run; 61% repeated compliance on the Pi 5 |
| 4 GB Pi 4 or Pi 5 | Imported LFM2.5-1.2B, then test locally | 967 MB RSS and 89% repeated compliance on our 8 GB Pi 5; we did not benchmark 4 GB variants directly |
| 8 GB Pi 5, responsive assistant | Imported LFM2.5-1.2B | 15.5 tokens/s, 4.7-second total reply, and the highest repeated compliance we measured |
| 8 GB Pi 5, registry-only setup | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS, and 83% repeated compliance |
| 8 GB Pi 5, try a larger text model | Quantized Qwen2.5 3B or Llama 3.2 3B | Both ran at about 5 tokens/s and used 2.4–2.8 GB RSS; Qwen2.5 3B passed 5/6 in a single compliance pass |

These choices prioritize short, useful replies on a Pi that may also run other services. They are starting points rather than claims that one model is best at every task. In our single-pass Pi 5 compliance check, default-thinking `qwen3.5:0.8b` and Spark-X2.5 returned no compliant replies, while MiniCPM5-1B managed 1/6; a client that cannot disable their reasoning should avoid them for this short-reply workload. We would test the final model with the actual prompt, context length, concurrency, and response limit planned for deployment.

For the registry model, after [installing Ollama for Linux](https://ollama.com/download/linux), run:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Test with your own prompts, desired answer length, and other services running. Record both total reply time and memory use. That will tell you more about whether a model belongs on your Pi than its parameter count alone.

On a memory-constrained node, keep an eye on swap while testing. If a larger model makes the board unresponsive, use a smaller model and set an Ollama service memory limit appropriate to that model so an oversized load fails instead of exhausting the host. A service cap is a safeguard, not a way to make an oversized model fit. The Pi 4 resets in our tests show why responsiveness and memory headroom belong in the selection criteria alongside tokens per second.
