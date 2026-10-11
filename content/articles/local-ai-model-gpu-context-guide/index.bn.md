---
title: "কোন স্থানীয় AI মডেল চালাবেন? অক্টোবর ২০২৬-এর GPU কনটেক্সট ও কোডিং গাইড"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "কোডিং এজেন্টের জন্য স্থানীয় AI মডেল বাছাইয়ের অক্টোবর ২০২৬-এর ব্যবহারিক গাইড। GPU মেমরি, KV-cache বৃদ্ধি, কনটেক্সট আকার, quantization quality, prompt processing, reasoning settings এবং cloud rental cost তুলনা করুন।"
genre: ["স্থানীয় AI", "AI হার্ডওয়্যার", "Self-Hosted AI", "GPU Benchmarking", "Developer Tools", "AI Economics"]
tags: ["স্থানীয় AI মডেল", "কোডিং এজেন্ট", "GPU গাইড", "VRAM", "KV cache", "কনটেক্সট উইন্ডো", "Qwen 27B", "mixture of experts", "quantization", "llama.cpp", "Ollama", "speculative decoding", "multi-token prediction", "স্থানীয় LLM", "GPU rental", "AI workstation", "agent coding", "prompt processing", "inference speed"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "স্থানীয় AI মডেল, GPU মেমরি ব্যবহার এবং কোডিং এজেন্টের কনটেক্সট উইন্ডো দেখানো একটি ওয়ার্কস্টেশন"
coverCaption: ""
ref: ["/articles/32gb-vram-qwen-27b-hardware-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/local-ai-2026-build-your-rig-now"]
---

**সেরা স্থানীয় কোডিং মডেল হলো সেই মডেল, যা আপনার প্রকল্পের যথেষ্ট অংশ মেমরিতে রাখে এবং ব্যবহারযোগ্য থাকার মতো দ্রুত পড়ে।** মডেলের আকার গুরুত্বপূর্ণ, কিন্তু system RAM-এ spill করার পর চলা বড় মডেলটি স্থিতিশীল context window-সহ ছোট মডেলের চেয়ে খারাপ অনুভূত হতে পারে।

*মডেল এবং মেমরি বাজেট একসঙ্গে বেছে নিন। Tier list থেকে মডেল বেছে অনুপযুক্ত হার্ডওয়্যারে জোর করে চালাবেন না।*

এই গাইড coding agent নিয়ে, ছোট autocomplete prompt নিয়ে নয়। Agent ফাইল, tool output, compiler error এবং test result পড়ে তারপর fix লেখে। এই input-গুলো context ব্যবহার করে, আর context হার্ডওয়্যার সিদ্ধান্ত বদলে দেয়।

## ভিডিওটি একটি রেফারেন্স

নিচের ভিডিওটি কয়েকটি GPU memory tier-এ স্থানীয় মডেল তুলনা করে। ব্যবহারিক model-selection observation এবং রিপোর্ট করা hardware result-এর জন্য এটি সহায়ক। এই নিবন্ধে memory behavior, agent context, prompt processing এবং total ownership cost ঘিরে সিদ্ধান্ত সাজানো হয়েছে।

{{< youtube id="C9M6iUFtVB4" enable="true" title="I Tested Every Local AI Model So You Don't Have To" description="GPU memory tier জুড়ে স্থানীয় AI মডেলের ব্যবহারিক তুলনা, coding workload এবং hardware limit-এর ওপর নজরসহ।" >}}

## Tier list কেন ব্যর্থ হয়

Model tier list সাধারণত parameter count-কে GPU memory number-এর সঙ্গে মেলায়। প্রথম অনুমানের জন্য shortcut-টি উপকারী। Coding agent বাস্তব repository পড়া শুরু করলে এর উপযোগিতা শেষ হয়।

Model weight প্রথম allocation। **KV cache** হলো বাড়তে থাকা allocation। এটি active context-এর attention key এবং value রাখে, যাতে প্রতিটি generated token-এর পরে runtime-কে পুরো prompt আবার গণনা করতে না হয়।

| Memory consumer | কী রাখে | কেন গুরুত্বপূর্ণ |
|---|---|---|
| **Model weights** | Quantized parameter | একবারের loading requirement |
| **KV cache** | Active context-এর note | Prompt এবং conversation বাড়লে বাড়ে |
| **Runtime buffers** | Temporary computation space | Backend এবং batch size অনুযায়ী বদলে যায় |
| **Agent instructions** | System prompt এবং tool definition | Project file আসার আগেই context ব্যবহার করে |

**Card-এ model file fit করলেই usable agent প্রমাণ হয় না।** Runtime-এর cache, temporary buffer, tool definition এবং next response-এর জন্য জায়গা দরকার।

## আসল budget হলো context

Coding agent শুধু source file-এ context খরচ করে না। System instruction, tool schema, directory listing, shell output, compiler message, test result এবং আগের conversation turn-ও budget-এর অংশ।

Verbose tool definition-সহ তিনটি MCP connection agent project file খোলার আগেই কয়েক হাজার token খরচ করতে পারে। ছোট default context code-এর জন্য সামান্য জায়গা রাখে। Agent উত্তর দেয়, কিন্তু multi-step repair-এর working set হারায়।

Ollama-র [runtime FAQ](https://docs.ollama.com/faq) 4,096 token-এর default context উল্লেখ করে। `OLLAMA_CONTEXT_LENGTH` default বদলায়, আর `OLLAMA_NUM_PARALLEL` concurrent request-এর সংখ্যা অনুযায়ী প্রয়োজনীয় memory বাড়ায়। Local benchmark-এর সঙ্গে single-request result তুলনা করার আগে দুটির মান লিখে রাখুন।

```bash
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_NUM_PARALLEL=1 ollama serve
```

এই উদাহরণ একটি active request-এর জন্য 32K default সেট করে। এটি project file-এর জন্য 32K token reserve করে না। Instruction, tool definition, input এবং output একই window ভাগ করে।

### একটি সহজ context record

GPU তুলনার আগে এই মানগুলি লিখে রাখুন:

- **Project size:** সাধারণ task-এর file এবং আনুমানিক source line।
- **Tool overhead:** system prompt, MCP schema, shell tool এবং editor instruction।
- **Error payload:** স্বাভাবিক compiler এবং test output-এর দৈর্ঘ্য।
- **Target context:** truncation ছাড়া রাখতে চাওয়া বড় prompt।
- **Response allowance:** পরিকল্পিত patch এবং explanation-এর জন্য রাখা জায়গা।

ফলটিকে workload specification হিসেবে ব্যবহার করুন। একবারে একটি file edit করা developer-এর memory requirement এবং monorepo-তে API trace করতে বলা developer-এর requirement এক নয়।

## KV Cache ranking বদলে দেয়

Parameter count কাছাকাছি হলেও দুই model-এর context cost ভিন্ন হতে পারে। প্রতিটি layer growing cache-এ অংশ নেওয়া dense model-এর বেশি memory লাগে, hybrid attention design ব্যবহার করা model-এর তুলনায়।

Reference material-এ আলোচিত একটি 27B coding model সীমিত কিছু full-attention layer ব্যবহার করে, অন্য layer fixed-size summary ব্যবহার করে। Report করা 128K context cost cache-এর জন্য 9GB-এর নিচে থাকে। একই context length-এ প্রতিটি layer-এ full growing attention-সহ একই আকারের model-এর 21GB-এর বেশি দরকার বলে report করা হয়েছে।

এই সংখ্যা নির্দিষ্ট model architecture এবং runtime setting বর্ণনা করে। এগুলিকে architecture পরীক্ষা করার কারণ হিসেবে নিন, universal memory formula হিসেবে নয়।

| Model behavior | Context effect | Hardware implication |
|---|---|---|
| **প্রতিটি layer-এ full attention** | বড় cache growth | Long prompt-এর জন্য বেশি memory লাগে |
| **Hybrid বা sliding attention** | কিছু layer-এ কম cache growth | একই model size-এ বেশি context headroom |
| **Mixture of experts** | প্রতি token-এ কম active parameter | প্রতি token-এ কম compute, কিন্তু total weight storage দরকার |
| **Long-context extension** | বড় working window | বেশি cache memory এবং বেশি prompt-processing work |

**Memory কেনার আগে model architecture পড়ুন।** শুধু parameter count দীর্ঘ coding session-এর cost লুকিয়ে রাখে।

## GPU memory tier অনুযায়ী বাছুন

### চার থেকে আট GB

ছোট dense model ব্যবহারিক পছন্দ থাকে। এটি card-এ fit করে, দ্রুত সাড়া দেয় এবং autocomplete, short explanation ও narrow file edit-এর জন্য ভালো কাজ করে।

CPU offload-সহ বড় model text তৈরি করতে পারে, কিন্তু response time সীমা হয়ে দাঁড়ায়। Coding agent-এর repeated file read এবং tool call দরকার। প্রতি সেকেন্ডে চার token-এর setup model technically চললেও প্রতিটি repair দীর্ঘ অপেক্ষায় পরিণত করে।

Mixture-of-experts model আরেকটি পথ দেয়। ছোট active অংশ compute pressure কমায়, আর full weight set system memory-তে আংশিক থাকে। এই পদ্ধতির জন্য যথেষ্ট RAM এবং দ্রুত transfer path দরকার।

| Workload | প্রস্তাবিত দিক |
|---|---|
| **Autocomplete** | Short prompt-সহ ছোট dense model |
| **Single-file edit** | Tool support-সহ ছোট instruct model |
| **Repository-wide agent** | আগে বড় GPU rent করুন বা system memory বাড়ান |
| **NDA-র অধীনে private code** | Local model ব্যবহার করুন, ছোট scope বা ধীর run মেনে নিন |

**এই tier-এ বড় model খোঁজার আগে system RAM কিনুন।** Bus জুড়ে data সরাতে থাকা বড় model-এর চেয়ে স্থিতিশীল ছোট model ভালো।

### বারো থেকে ষোলো GB

এই tier 27B coding model-এর সুযোগ দেয়, কিন্তু quantization choice কেন্দ্রীয় হয়ে ওঠে। প্রায় 17GB-এর standard 4-bit build runtime overhead যোগ হলে 16GB card-এ fit করে না।

প্রায় 13GB-এর 3-bit build context-এর জন্য বেশি জায়গা রাখে। 12GB card 2-bit build বা ছোট mixture-of-experts model-এর দিকে ঠেলে দেয়। নির্দিষ্ট quantizer এবং calibration process-এর ওপর quality নির্ভর করে, তাই একই bit depth-এর দুই upload-এ coding result ভিন্ন হয়।

Quantized model download-এর আগে দেখুন:

- **Quantizer author এবং release note**
- **Calibration data এবং evaluation result**
- **Tokenizer compatibility**
- **Tool-calling test**
- **বাছাই করা quantization-এ context length**
- **Ollama, llama.cpp বা নির্বাচিত front end-এ runtime support**

**“2-bit” বা “3-bit”-কে quality-এর সম্পূর্ণ বর্ণনা ভাববেন না।** Packing method এবং calibration record গুরুত্বপূর্ণ।

### চব্বিশ থেকে বত্রিশ GB

27B coding model-এর জন্য এই range সবচেয়ে flexible। 24GB card-এ useful context-সহ 4-bit build প্রায়ই fit করে, কিন্তু full 128K window অবশিষ্ট memory ছাড়িয়ে যেতে পারে। 32GB card cache এবং temporary allocation-এর জন্য runtime-কে বেশি জায়গা দেয়।

এই range ownership-কে সহজে যুক্তিসঙ্গত করে। দুই-card split-এর জটিলতা ছাড়া একটি GPU workload সামলায়। Multi-GPU build-এর চেয়ে system কম power ব্যবহার করে, আর software support পরীক্ষা সহজ হয়।

| Capacity | Practical position |
|---|---|
| **24GB** | Context limit মাপার মতো শক্তিশালী 4-bit model |
| **32GB** | বেশি context headroom-সহ 4-bit বা 6-bit 27B model |
| **48GB** | Core model বদলানো ছাড়াই বেশি precision বা বড় cache |

**নিয়মিত private coding work-এর জন্য 24GB থেকে 32GB range ownership-এর যুক্তিসঙ্গত অঞ্চল।** Data-center hardware desktop case-এ না ঢুকিয়েও দুর্বল offload behavior এড়ানো যায়।

### আটচল্লিশ GB এবং তার বেশি

বেশি memory মানেই নতুন model নয়। একই 27B model 48GB card-এ 8-bit precision-এ চলতে পারে, বড় cache এবং কম compromise-সহ। উন্নতি reasoning-এর নতুন স্তর নয়, consistency, context room এবং output quality।

128GB-এ decision বদলে যায়। অনেক বড় mixture-of-experts model সম্ভব হয়, কিন্তু prompt processing গুরুতর বিষয় হয়ে ওঠে। Model প্রায়ই দ্রুত generate করে, অথচ বড় repository বা নতুন tool result ingest করতে দীর্ঘ সময় নেয়।

**বড় model-এর জন্য prefill speed এবং decode speed আলাদা করে মাপুন।** ধীর prompt read-এর পরে দ্রুত answer এলেও agent workflow-এ তা ধীর লাগে।

## Decode speed test-এর অর্ধেক মাত্র

**Decode speed** generated token per second মাপে। প্রশ্নের উত্তর, “Model কত দ্রুত লেখে?” **Prefill speed** prompt processing মাপে। প্রশ্নের উত্তর, “Model কত দ্রুত পড়ে?”

Agent-এর অনেক সময় পড়তে যায়। প্রতিটি tool call নতুন text যোগ করে। পরের response শুরুর আগে দীর্ঘ source file, stack trace বা test log prompt-এ ঢোকে।

| Metric | User experience |
|---|---|
| **Decode token per second** | Processing-এর পরে answer কত দ্রুত দেখা যায় |
| **Prompt token per second** | Answer শুরুর আগে agent কতক্ষণ অপেক্ষা করে |
| **Time to first token** | Prompt processing এবং setup-এর মিলিত delay |
| **Context retention** | Task চলাকালে কত project state available থাকে |

**নিজের prompt size benchmark করুন।** ছোট synthetic prompt repository work-এর সবচেয়ে গুরুত্বপূর্ণ cost লুকিয়ে রাখে।

## আগে বিনামূল্যের runtime setting

Hardware upgrade performance-এর প্রথম ধাপ নয়। Shopping page খোলার আগে runtime setting পরীক্ষা করুন।

### Multi-Token Prediction

কিছু model ও backend combination কয়েকটি future token অনুমান করে এক pass-এ verify করতে পারে। Feature-টি প্রায়ই runtime flag বা compatible draft setup-এর মাধ্যমে পাওয়া যায়।

Reference material-এর report করা test কিছু high-end card-এ বড় gain দেখায়। Model file, backend, driver এবং card অনুযায়ী result বদলে যায়। Conversion-এর সময় Apple Metal path প্রয়োজনীয় feature ধরে নাও রাখতে পারে।

### Reasoning level

Maximum reasoning enabled থাকা model result ফেরানোর আগে internal work-এ বেশি সময় দেয়। Code repair-এর জন্য medium reasoning প্রায়ই ভালো balance দেয়, বিশেষত task-এ clear error message এবং narrow file target থাকলে।

সহজ test matrix ব্যবহার করুন:

1. Low, medium এবং high reasoning-এ একই bug-fix task চালান।
2. Time to first token, total time, patch success এবং test result লিখুন।
3. Short prompt এবং repository-sized prompt দিয়ে পুনরাবৃত্তি করুন।
4. Highest token rate নয়, completed task-এর সেরা result দেওয়া setting রাখুন।

**Compatible multi-token path-সহ medium reasoning ভালো starting point।** Default করার আগে নিজের code-এ quality যাচাই করুন।

## Local hardware নাকি rental GPU?

Occasional work-এর জন্য rental compute জেতে। সারা বছর card কেনা, cooling, updating এবং powering-এর বদলে active session-এর জন্য টাকা দেন।

Workload frequent, private বা offline হলে owned hardware জেতে। Queue time বাদ যায় এবং repeatable test-এর জন্য stable environment পাওয়া যায়।

| Situation | Better first move |
|---|---|
| **মাসে কয়েকটি session** | GPU rent করুন বা API ব্যবহার করুন |
| **Daily private coding** | Supported 24GB থেকে 32GB system কিনুন |
| **Frequent reload-সহ বড় repository** | আগে rent করে prefill speed মাপুন |
| **Code building ছেড়ে যায় না** | Context target পূরণ করা সবচেয়ে ছোট system own করুন |
| **নতুন model পরীক্ষা** | Hardware কেনার আগে rent করুন |

Break-even active hour দিয়ে হিসাব করুন, calendar hour দিয়ে নয়। Electricity, storage, cooling, maintenance এবং runtime সচল রাখার সময় ধরুন।

**Occasional experiment-এর জন্য high-end GPU কেনা hobby expense।** Daily private work-এ ব্যবহৃত 24GB থেকে 32GB system-এর economic case শক্তিশালী।

## ভালো buying checklist

Model এবং GPU তুলনা করার সময় এই ক্রম ব্যবহার করুন:

1. **Task নির্ধারণ করুন।** Autocomplete, single-file repair, repository agent বা long-context analysis।
2. **Prompt মাপুন।** Normal system instruction, tool schema, file এবং test output গুনুন।
3. **Cache behavior দেখুন।** Architecture note এবং context-memory measurement খুঁজুন।
4. **Quantization বাছুন।** শুধু bit count নয়, নির্দিষ্ট upload-এর quality result দেখুন।
5. **Prefill এবং decode test করুন।** নিজের repository-এর prompt ব্যবহার করুন।
6. **Reasoning tune করুন।** কয়েকটি reasoning level-এ completed task time তুলনা করুন।
7. **Privacy এবং maintenance test করুন।** Source code কোথায় যায় এবং backend কে maintain করে নিশ্চিত করুন।
8. **Rental cost তুলনা করুন।** Expected active hour ব্যবহার করুন এবং owned-system estimate-এ power যোগ করুন।

## শেষ সুপারিশ

**12GB-এর নিচে, যথেষ্ট system RAM-সহ ছোট model বা mixture-of-experts model চালান।** বেশিরভাগ সময় offload করা 27B dense model জোর করে চালাবেন না।

**12GB থেকে 16GB-এ quantization quality এবং controlled context target-এ মন দিন।** Tool support-সহ ভালোভাবে test করা 2-bit বা 3-bit build এমন 4-bit file-এর চেয়ে বেশি উপকারী, যা cleanly fit করে না।

**24GB থেকে 32GB-এ 27B coding model private daily work-এর practical default হয়।** Full advertised window available ধরে নেওয়ার আগে context usage এবং prompt speed মাপুন।

**48GB বা তার বেশি হলে বড় model-এ যাওয়ার আগে অতিরিক্ত memory precision, cache room এবং stable session-এ দিন।** Model 128GB territory পার হলে raw capacity-এর চেয়ে prompt-reading speed এবং rental economics বেশি মনোযোগ দাবি করে।

Model name কেবল শুরু। দরকারি প্রশ্ন হলো model, runtime, tool এবং cache ভাগ নেওয়ার পরে কত project context বাকি থাকে।

## Related reading

- [Qwen 27B-এর জন্য 32GB VRAM: Local AI hardware guide](/articles/32gb-vram-qwen-27b-hardware-guide/), 27B workload-এর hardware path নিয়ে।
- [Vast.ai-এ Llama 3.1 8B এবং Qwen3.8 27B GPU benchmark](/articles/qwen38-27b-vast-ai-gpu-benchmark/), measured rental-GPU result এবং long-context limit।
- [২০২৬-এ Local AI: একটি 27B model Sonnet 4.6-কে হারায়](/articles/local-ai-2026-build-your-rig-now/), model quality, quantization এবং local hardware economics।
