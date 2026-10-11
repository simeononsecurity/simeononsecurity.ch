---
title: "Meta-র Context Language Models: এজেন্টের উন্নত স্মৃতি, হ্যালুসিনেশনের অবসান নয়"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Context Language Models কীভাবে এজেন্টের স্মৃতি সম্পাদনা করে, বেঞ্চমার্ক কী প্রমাণ করে, এবং ক্যাশের খরচ, মডেলের সক্ষমতা ও অবিশ্বস্ত নোট কীভাবে নির্ভরযোগ্যতাকে প্রভাবিত করে।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "AI এজেন্ট", "স্থানীয় AI", "AI নিরাপত্তা"]
tags: ["Context Language Models", "CLM", "Meta AI", "AI হ্যালুসিনেশন", "এজেন্ট স্মৃতি", "কনটেক্সট ব্যবস্থাপনা", "কনটেক্সট কমপ্যাকশন", "কনটেক্সট উইন্ডো", "Suffix Cache Reuse", "KV ক্যাশ", "SGLang", "llama.cpp", "প্রম্পট ক্যাশিং", "প্রম্পট ইনজেকশন", "BrowseComp-Plus", "ContextBench", "EdgeBench", "Qwen3.6", "দীর্ঘসময় চলা এজেন্ট", "AI নির্ভরযোগ্যতা", "এজেন্ট যাচাই"]
cover: "/img/cover/context-language-models-editable-memory.webp"
coverAlt: "অন্ধকার পৃষ্ঠের ওপর পুনর্বিন্যস্ত স্বচ্ছ নথি কার্ড এবং আলাদা আর্কাইভ স্তূপের পাশে একটি উজ্জ্বল প্রসেসর"
coverCaption: "সম্পাদনাযোগ্য এজেন্ট স্মৃতির ধারণামূলক চিত্র।"
---

**Context Language Models (CLM)** একটি AI এজেন্টকে তার পরবর্তী মডেল কলের জন্য পাঠানো তথ্যের ওপর সরাসরি নিয়ন্ত্রণ দেয়। প্রকাশিত কয়েকটি মূল্যায়নে এই পদ্ধতি কনটেক্সট ব্যবস্থাপনা উন্নত করেছে, কিন্তু হ্যালুসিনেশনের অবসান প্রমাণ করেনি। এজেন্টের দাবির জন্য এখনও প্রমাণ এবং কাজের স্বাধীন যাচাই প্রয়োজন।

প্রকৌশলগত প্রশ্ন হলো, নির্বাচিত সম্পাদনা গ্রহণযোগ্য খরচে সঠিক তথ্য ধরে রাখে কি না। ছোট কথোপকথন তখনই উপকারী, যখন এজেন্ট নিজের প্রয়োজনীয়তা ধরে রাখে, পর্যবেক্ষণ ও অনুমান আলাদা করে, এবং প্রয়োজন হলে সহায়ক প্রমাণ উদ্ধার করে।

<!--more-->

## মূল বিষয়গুলো

- **সম্পাদনাযোগ্য কনটেক্সট:** CLM বিদ্যমান মডেলের জন্য একটি এক্সিকিউশন পদ্ধতি। এর ব্যবহার উন্নত করতে ঐচ্ছিক প্রশিক্ষণ যোগ করা যায়।
- **শর্তসাপেক্ষ লাভ:** মডেলের আকার, কনটেক্সট বাজেট, কাজ এবং সার্ভিং ব্যাকএন্ড ফলাফলে প্রভাব ফেলে।
- **কম্পিউট হিসাব:** prefix-reuse FLOPs সম্পাদনার পরের পুনর্গণনা ধরে, কিন্তু সরাসরি অতিবাহিত সময় বা বিলিং মাপে না।
- **স্মৃতির অখণ্ডতা:** এজেন্টের নিজের নোট ভুলপ্রবণ এবং সম্ভাব্য অনিরাপদ ইনপুট হিসেবে থাকে।
- **ব্যবহারিক মূল্যায়ন:** গৃহীত ফলাফল, হারানো তথ্য, অসমর্থিত দাবি এবং পুনরুদ্ধারের খরচ একসঙ্গে মাপুন।

## স্মৃতি ও প্রমাণ আলাদা রাখুন

**একটি কনটেক্সট উইন্ডো** কল চলাকালে মডেলের জন্য উপলব্ধ ইনপুট ধারণ করে। নির্দেশনা, টুলের উত্তর, কাজের নোট এবং আগের বার্তা জায়গার জন্য প্রতিযোগিতা করে। কমপ্যাকশন এই উপাদানের কিছু অংশকে ছোট উপস্থাপনায় বদলে দেয়।

একটি **উদাহরণধর্মী dependency-upgrade কাজ** বিবেচনা করুন। একটি টেস্ট রানার দুটি ব্যর্থতার কথা জানায়। এজেন্ট তার ইতিহাসকে এমন একটি নোটে সংকুচিত করে যেখানে বলা হয় আপগ্রেড সফল। আসল টেস্ট আউটপুট ডিস্কে থাকলেও পরের কাজ ভুল ধারণা থেকে শুরু হয়।

কমপ্যাকশন পদ্ধতি বদলালে ভুল নোটটি কীভাবে কাজের স্মৃতিতে ঢোকে তা বদলায়। কিন্তু এটি **প্রমাণ হিসেবে টেস্ট রানারের জায়গা নেয় না**। আপগ্রেড গ্রহণের আগে কাজের প্রবাহে এখনও নতুন টেস্ট ফলাফল বা সংশ্লিষ্ট রানটির পরিদর্শনযোগ্য রেকর্ড প্রয়োজন।

| ব্যর্থতা | উপযুক্ত পরীক্ষা |
|---|---|
| **হারানো প্রয়োজনীয়তা** | বর্তমান অবস্থার সঙ্গে আসল গ্রহণযোগ্যতার মানদণ্ড তুলনা করুন |
| **বানানো পর্যবেক্ষণ** | দাবিটিকে কোনো টুল ফলাফল বা উৎস রেকর্ডের সঙ্গে মিলিয়ে দেখুন |
| **ভুল যুক্তি** | কাজটির প্রত্যাশিত আচরণের বিরুদ্ধে সিদ্ধান্ত পরীক্ষা করুন |
| **অননুমোদিত নির্দেশনা** | মডেল-লিখিত নোটের বাইরে অনুমতি প্রয়োগ করুন |

যে কোনো স্মৃতি কৌশল মূল্যায়নে এই পার্থক্য গুরুত্বপূর্ণ। **সংরক্ষণ ও সঠিকতা আলাদা বৈশিষ্ট্য।** কোনো সিস্টেম ভুল দাবিকে নিখুঁতভাবে ধরে রাখলেও সেটি ভুলই থাকে।

## CLM কী বদলায়

**Rulin Shao ও সহলেখকেরা**, Meta Superintelligence Labs এবং University of Washington-এর গবেষকদের সঙ্গে, 29 সেপ্টেম্বর 2026-এর একটি preprint-এ CLM উপস্থাপন করেন। তাঁদের বাস্তবায়ন সক্রিয় কনটেক্সটকে সম্পাদনাযোগ্য ফাইল হিসেবে প্রকাশ করে। এজেন্ট shell কমান্ড বা কোড দিয়ে ফাইল বদলায়, আর runtime পরের কলে সংশোধিত বিষয়বস্তু সরবরাহ করে। দেখুন [Context Language Models](https://arxiv.org/abs/2609.37725)।

```text
Ordinary continuation:
existing context + new response + new tool output

Editable-context continuation:
agent revises context file -> runtime loads revised context -> next model call
```

**Zero-shot পদ্ধতিতে মডেল আর্কিটেকচার বদলাতে হয় না।** Runtime বিদ্যমান মডেলের চারপাশে একটি সক্ষমতা যোগ করে। পেপারটি নির্দেশনা, শেখা কনটেক্সট-ব্যবস্থাপনা কৌশল এবং reinforcement learning-ও আলাদাভাবে পরীক্ষা করে।

একটি **নোট ফাইল** আলাদা বিষয়। সংরক্ষিত নোট পড়লে তার বিষয়বস্তু কথোপকথনে যোগ হয়। পরে ফাইল সম্পাদনা করলেও সক্রিয় কনটেক্সট থেকে পুরোনো লেখা স্বয়ংক্রিয়ভাবে সরে না। পরের অনুরোধের সঙ্গে সম্পাদনা সমন্বয় করতে CLM-এর runtime সমর্থন প্রয়োজন। [অফিশিয়াল বাস্তবায়ন](https://github.com/facebookresearch/context-language-models)-এ এজেন্ট কোড এবং আলাদা সার্ভিং এক্সটেনশন রয়েছে।

**বাহ্যিক স্টোরেজ এখনও উপকারী।** বিস্তারিত লগ ও উৎস নথি উদ্ধারের জন্য রাখুন, আর কাজের স্মৃতিতে সংক্ষিপ্ত রেফারেন্স রাখুন। পরের প্রম্পটে প্রতিটি লাইন রাখার চেয়ে নথির অবস্থান এবং সেটি যে দাবিকে সমর্থন করে তা অনেক সময় বেশি গুরুত্বপূর্ণ।

## ফলাফল সতর্কভাবে পড়ুন

**বেঞ্চমার্কের উন্নতি নির্দিষ্ট তুলনা।** পরের ফলাফলগুলো লেখকদের মূল্যায়ন থেকে এসেছে, এই নিবন্ধের জন্য করা পরীক্ষা থেকে নয়। গবেষণাটি এখনও preprint, আর নির্বাচিত বেঞ্চমার্কের ফল যেকোনো কাজের প্রবাহে নির্ভরযোগ্যতা প্রমাণ করে না।

| মূল্যায়ন | জানানো ফলাফল | ব্যাখ্যা |
|---|---|---|
| **BrowseComp-Plus, zero-shot** | শক্তিশালী baseline-এর তুলনায় আপেক্ষিক নির্ভুলতা 11.4% বেশি এবং prefix-reuse FLOPs 21.5% কম | এই সেটআপে নির্ভুলতা ও কম্পিউট দুটোই উন্নত |
| **TerminalBench 2.1** | 29.5% কম FLOPs-এ শক্তিশালী baseline-এর সমান নির্ভুলতা | তুলনীয় নির্ভুলতায় লাভটি দক্ষতা |
| **EdgeBench, 12 ঘণ্টার রান** | 59% কম FLOPs-এ স্কোর 5% বেশি | সফটওয়্যার অপ্টিমাইজেশনের স্কোর, হ্যালুসিনেশনের হার নয় |
| **প্রশিক্ষিত Qwen3.5-9B** | প্রশিক্ষিত summary-এর 42.1%-এর বিপরীতে CLM 42.5% | বেশি কম্পিউট পার্থক্যের সঙ্গে ছোট নির্ভুলতা পার্থক্য |

প্রশিক্ষিত 9B তুলনায় **প্রতি প্রশ্নে 1.34 বনাম 2.19 PFLOPs** ব্যবহার হয়। CLM-এর জন্য কম্পিউট প্রায় 38.8% কম। প্রশিক্ষণের আগে 28.8% থেকে পরে 42.5%-এ উন্নতি, প্রশিক্ষিত summarization-এর বিপরীতে 0.4-পয়েন্ট ব্যবধানের থেকে আলাদা তুলনা। baseline স্পষ্ট রাখুন। দেখুন [পেপারের ফলাফল ও প্রশিক্ষণ সারণি](https://arxiv.org/html/2609.37725v1)।

**আপেক্ষিক শতাংশের** একটি denominator-ও দরকার। প্রায় 53.3% থেকে 59.4%-এ বৃদ্ধি প্রায় 6.1 percentage points, অথবা আপেক্ষিকভাবে 11.4%। কোনো প্রকাশই বোঝায় না যে সিস্টেম প্রতিটি প্রশ্নের সঠিক উত্তর দেয়।

### কনটেক্সট বাজেট ফলাফল বদলায়

**32K কনটেক্সট বাজেট** প্রধান মূল্যায়নগুলোতে দেখা যায়। এটি ধরে রাখা ও সম্পাদনার ওপর গুরুত্বপূর্ণ সীমা তৈরি করে। এই বাজেটের ফলাফল প্রতিটি বড়-window deployment-এ প্রয়োগ করা উচিত নয়।

**EdgeBench-10-এ 128K** অবস্থায় Appendix F দশটি কাজ ও তিনটি seed-এর ফল জানায়:

| পদ্ধতি | চূড়ান্ত স্কোর | প্রতি ট্রায়ালে গড় prefix-reuse PFLOPs |
|---|---|---|
| **Summarization** | 47.8 | 222 |
| **CLM** | 47.3 | 142 |
| **Subagents-সহ CLM** | 50.2 | 219 |

**একক-এজেন্ট নির্ভুলতা কাছাকাছি**, আর এই তুলনায় CLM প্রায় 36% কম কম্পিউট ব্যবহার করে। Subagent configuration আবার ফল বদলায়। পদ্ধতির নামের পাশাপাশি কনটেক্সট ক্ষমতা, এজেন্ট configuration এবং কম্পিউট বাজেটও তুলনায় রাখুন।

### মডেলের সক্ষমতা এখনও গুরুত্বপূর্ণ

**ছোট মডেল স্বয়ংক্রিয়ভাবে স্মৃতি ভালোভাবে পরিচালনা করে না।** প্রশিক্ষণ তুলনায় প্রশিক্ষণহীন 9B CLM summary baseline-এর নিচে শুরু করে। আলাদা supplementary evaluation BrowseComp-Plus-এ 39.9% বনাম 37.7% জানায়। এগুলো আলাদা experimental setup, বিনিময়যোগ্য মাপ নয়।

Supplementary TerminalBench analysis-এ **9B-এর অর্ধেক কাজেই কোনো context edit হয়নি**। মডেলকে editing interface দিলেই সেটি কার্যকরভাবে ব্যবহার করবে এমন নিশ্চয়তা নেই। CLM-কে universal upgrade না ধরে নির্বাচিত মডেল ও সেটিংস মূল্যায়ন করুন।

## পুনঃপ্রক্রিয়াকরণ হিসাব করুন

**KV cache** attention-এর মধ্যবর্তী গণনা ধরে রাখে। সাধারণ prefix caching-এ পরের অনুরোধের শুরুতে অপরিবর্তিত লেখা আগের গণনা পুনর্ব্যবহার করে। শুরুর কাছে সম্পাদনা করলে পুনর্ব্যবহারযোগ্য prefix ছোট হয় এবং পরের লেখা আবার process করতে হয়।

```text
Previous request: A + B + C
Revised request:  A + replacement for B + C

Standard prefix reuse:
reuse A, recompute replacement for B and C
```

পেপারের **prefix-reuse FLOPs** মেট্রিক প্রথম অমিলের পর generation এবং prompt processing গণনা করে। একটি PFLOP হলো 10¹⁵ floating-point operation। এটি আনুমানিক কম্পিউট মোট, quality score, throughput measurement বা invoice নয়।

Appendix C-এর **7.7× উদাহরণে** 20,000-token prompt এবং 500-token response ব্যবহার করা হয়েছে। শুরুতে সম্পাদনা করলে 18,000-token পুনর্ব্যবহারযোগ্য prefix-সহ modeled append-only turn-এর 7.7 গুণ খরচ হয়। নির্দিষ্ট দৈর্ঘ্যের পুনর্গণনা penalty এটি, হ্যালুসিনেশন 7.7 গুণ কমার মাপ নয়।

**স্থানীয় latency prompt throughput-এর ওপর নির্ভর করে।** গাণিতিক উদাহরণ হিসেবে, প্রতি সেকেন্ডে অনুমিত 800 token গতিতে 24,000 token আবার পড়তে অন্য overhead-এর আগে 30 সেকেন্ড লাগে। এটি কোনো নির্দিষ্ট Mac বা GPU-এর benchmark নয়। যে backend, quantization এবং বাস্তব prompt size ব্যবহার করবেন সেগুলো মাপুন।

[Hybrid-model reprocessing নিয়ে llama.cpp আলোচনা](https://github.com/ggml-org/llama.cpp/issues/20225) দেখায় কেন **prefix change এবং recurrent-state checkpoint** গুরুত্বপূর্ণ। llama.cpp ব্যবহার করা প্রতিটি release বা application-এ একই আচরণ প্রমাণ করে না। Runtime version লিখে রাখুন এবং cache log দেখুন।

## Cache savings-এর সীমা আছে

**Suffix Cache Reuse (SCR)** সম্পাদনার পর টিকে থাকা লেখার জন্য cached state ধরে রাখে। প্রকাশিত extension SGLang লক্ষ্য করে, আর তার README version 0.5.16 উল্লেখ করে। এটি আলাদা serving optimization, মৌলিক editable-context পদ্ধতির শর্ত নয়।

**Reuse আনুমানিক।** টিকে থাকা token আগের context-এর অধীনে গণনা করা state ধরে রাখে। তাই benchmark performance মিলে গেলেও নতুন prompt পুরোপুরি পুনর্গণনার সঙ্গে numerical equivalence প্রমাণ হয় না।

BrowseComp-Plus তুলনায় লেখকেরা **server-side compute 35% কম** জানান। অতিরিক্ত পুনর্ব্যবহৃত prompt token-এর 7.8 percentage point-এর মধ্যে 5.3 এসেছে বাদ দেওয়া reasoning block থেকে, 2.5 এসেছে অন্য edit থেকে। তাই এই লাভের বড় অংশ explicit CLM editing-এর বাইরেও প্রযোজ্য। দেখুন [SCR implementation notes](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md)।

**API billing-এর ক্ষেত্রে** সাধারণ input, cache write এবং cache read আলাদা করুন। Anthropic Sonnet 4.6-এর জন্য প্রতি মিলিয়ন token-এ সাধারণ input, পাঁচ মিনিটের cache write এবং cache hit-এর দাম যথাক্রমে $3, $3.75 এবং $0.30 জানায়। 20,000 token cache write হিসেবে আবার লিখতে $0.075 লাগে, hit-এর জন্য $0.006। $0.069 পার্থক্যে output ও অন্য billing modifier ধরা নেই। [Prompt-caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), 10 অক্টোবর 2026-এ পরীক্ষা করা হয়েছে।

**মোট কাজের খরচই tradeoff ঠিক করে।** মাঝেমধ্যে ব্যয়বহুল edit পরের input অনেক কমালে সাশ্রয় দেয়। অল্প কয়েকটি বাকি turn-এর আগে ঘন ঘন edit করলে খরচ ফেরত পাওয়ার সুযোগ কমে।

**যে serving path deploy করবেন সেখানে cache behavior যাচাই করুন।** পেপারের reuse measurement প্রমাণ করে না যে API, SGLang release বা local runtime একই cache control প্রকাশ করে। Pilot চলাকালে cache hit, prompt token, recomputation এবং reset behavior লিখে রাখুন। Telemetry না থাকাকে evaluation limitation ধরুন।

## নির্দেশনার নিচে নোট রাখুন

**মডেল-লিখিত স্মৃতি অবিশ্বস্ত task data।** এতে observation, interpretation এবং কখনও ভুল থাকে। প্রতিটি নোটকে instruction ধরলে সেই ভুলগুলো ভবিষ্যৎ action-এর ওপর কর্তৃত্ব পায়।

OpenAI একটি unreleased Astra-family model-এর আলাদা training run-এ **27টি jailbreak-সদৃশ compaction summary** নথিভুক্ত করেছে। কিছু injected instruction উপেক্ষা করা হয়েছিল, আর task-specific restriction একটি জানানো continuation-কে প্রভাবিত করেছিল। রিপোর্টটি বিরল আচরণ বর্ণনা করে এবং বলে যে final Astra model বা traffic-এ ব্যবহৃত checkpoint-এ regeneration এটি পুনরাবৃত্তি করেনি। এটি failure mode-এর প্রমাণ, deployed CLM-এ এর prevalence-এর প্রমাণ নয়। দেখুন [OpenAI-র compaction-summary report](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/)।

একটি **defensive implementation**-এ এই দায়িত্বগুলো আলাদা থাকা উচিত:

| উপাদান | ব্যবস্থা |
|---|---|
| **ব্যবহারকারীর প্রয়োজনীয়তা ও অনুমতি** | সম্পাদনাযোগ্য notes layer-এর বাইরে সংরক্ষণ করুন |
| **কাজের নোট** | revision অনুমতি দিন, provenance রাখুন এবং uncertainty চিহ্নিত করুন |
| **আসল প্রমাণ** | summary থেকে স্বাধীনভাবে উদ্ধারযোগ্য record রাখুন |
| **Action ও edit** | পরিবর্তন log করুন এবং code-এ access control প্রয়োগ করুন |

**মুছে ফেলা মানেই সবসময় erase নয়।** SCR আগের context দ্বারা প্রভাবিত state ধরে রাখে। Engineering inference হিসেবে, editable file থেকে লেখা সরানো cached state-এর সব প্রভাব সরেছে এমন প্রমাণ নয়। Workflow-এ clean restart দরকার হলে explicit reset behavior পরীক্ষা করুন।

## সীমিত Pilot পরীক্ষা করুন

**Advertised context length দিয়ে নয়, retention requirement দিয়ে শুরু করুন।** পরিচিত উত্তর, অপরিবর্তনীয় input record এবং পরিষ্কার completion check-সহ একটি পুনরাবৃত্ত কাজ বেছে নিন। প্রথম তুলনার জন্য synthetic data-সহ sandbox ব্যবহার করুন।

1. **সঠিক তথ্য তৈরি করুন:** identifier, পরিবর্তিত requirement, ব্যর্থ চেষ্টা এবং একটি সংশোধিত value দিন।
2. **তুলনাযোগ্য configuration চালান:** fixed summarization, editable context এবং fresh-session notes workflow।
3. **Input স্থির রাখুন:** একই model, task set, tool, generation limit এবং context budget ব্যবহার করুন।
4. **Memory change-এর পর পরীক্ষা করুন:** exact recall, source retrieval এবং superseded fact obsolete হিসেবে চিহ্নিত আছে কি না দেখুন।
5. **পুরো run মাপুন:** success rate, unsupported claim, elapsed time, edit, overflow recovery এবং manual correction record করুন।

**Token accounting runtime-এ থাকা উচিত।** Appendix G tested model-এ context-length awareness সীমিত পায়, আর environmental hint estimate উন্নত করে। Experimental setup-এ overflow recovery-ও আছে। মাপা token count দিন এবং response space রাখুন, model-এর capacity estimate-এর ওপর নির্ভর করবেন না।

Live-context editing না থাকলে **notes-based fallback** উপকারী। Handoff সংক্ষিপ্ত এবং evidence-linked রাখুন। নিচের রেকর্ডটি উদাহরণ, CLM API format নয়:

```yaml
objective: Upgrade the dependency without changing export behavior
verified:
  - claim: Date export test still fails
    evidence: artifacts/export-test-result.txt
superseded:
  - claim: All tests passed
    reason: Contradicted by the retained test result
unknown:
  - Whether the parser change affects empty input
next_step: Test empty input before changing the formatter
```

**নতুন session-ও এই নোট পড়ার খরচ দেয়**, আর খারাপ নোট খারাপ তথ্যই স্থানান্তর করে। গুরুত্বপূর্ণ দাবির জন্য evidence আবার খুলুন এবং আসল task specification হাতের কাছে রাখুন। এটি compatibility option, CLM-সমতুল্য লাভের প্রমাণ নয়।

## গৃহীত ফলাফল দিয়ে সিদ্ধান্ত নিন

দীর্ঘসময় চলা কাজ বারবার দরকারি state হারালে বা পুরোনো context-এ অনেক compute খরচ করলে **CLM পরীক্ষা করুন**। অল্প history-সহ ছোট interaction-এ এই নির্দিষ্ট optimization-এর সুযোগ কম।

Official repository **CC BY-NC 4.0** শর্তে প্রকাশিত। Commercial project-এ implementation নেওয়ার আগে [license](https://github.com/facebookresearch/context-language-models/blob/main/LICENSE) দেখুন। Public source থাকলেই unrestricted commercial reuse-এর অনুমতি মেলে না।

**Reliable completion-ই লক্ষ্য।** Evidence check দুর্বল না করে accepted outcome উন্নত বা cost কমালে তবেই method রাখুন। Related deployment choice-এর জন্য [local AI ও hosted-model comparison](/articles/local-ai-vs-chatgpt-how-close-are-we/) এবং [GPU ও context planning guide](/articles/local-ai-model-gpu-context-guide/) পড়ুন।

{{< youtube id="9-iiHFQyzuM" enable="true" title="The End of AI Hallucinations? Meta's New Fix (CLM's)" description="Context Language Models, agent memory, serving costs, and reliability considerations." >}}

## রেফারেন্স

- **Rulin Shao et al.:** [Context Language Models](https://arxiv.org/abs/2609.37725), 29 সেপ্টেম্বর 2026, সঙ্গে [পূর্ণ ফলাফল ও appendix](https://arxiv.org/html/2609.37725v1)।
- **Meta research implementation:** [Context Language Models repository](https://github.com/facebookresearch/context-language-models)।
- **Serving implementation:** [Suffix Cache Reuse documentation](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md)।
- **Anthropic:** [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)।
- **OpenAI:** [Self-generated prompt injections in compaction summaries](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/)।
- **llama.cpp:** [Hybrid-model prompt reprocessing discussion](https://github.com/ggml-org/llama.cpp/issues/20225)।
- **Kai:** [The End of AI Hallucinations? Meta's New Fix (CLM's)](https://www.youtube.com/watch?v=9-iiHFQyzuM)।
