---
title: "Raspberry Pi 4 বা 5-এ কোন AI মডেল চলে?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Raspberry Pi 4 ও 5-এর পরিমাপ করা ফল থেকে মেমরি, গতি ও কাজের ধরন অনুযায়ী স্থানীয় ভাষার মডেল বাছুন, ছোট LFM2.5 থেকে 3B ও বড় বিকল্প পর্যন্ত।"
genre: ["Raspberry Pi", "কৃত্রিম বুদ্ধিমত্তা", "স্ব-হোস্টিং"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "স্থানীয় AI", "ছোট ভাষার মডেল", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "মডেল কোয়ান্টাইজেশন", "এজ AI"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "গাঢ় ডেস্কের ওপর দুটি Raspberry Pi কম্পিউটার, ওপরে নীল ও অ্যাম্বার রঙের নিউরাল নেটওয়ার্কের চিত্র"
coverCaption: "Raspberry Pi হার্ডওয়্যারে চলা স্থানীয় AI মডেলের চিত্র।"
---

Raspberry Pi স্থানীয়ভাবে কার্যকর ভাষার মডেল চালাতে পারে, তবে মডেলটি বোর্ডের মেমরিতে ধরতে হবে এবং অ্যাপের সহনীয় সময়ে উত্তর দিতে হবে। 2 GB Raspberry Pi 4 প্রায় এক বিলিয়নের কম প্যারামিটারের মডেলের জন্য বেশি উপযোগী। 8 GB Raspberry Pi 5 স্বাচ্ছন্দ্যে কমপ্যাক্ট 1B–3B মডেল চালায় এবং বড় কোয়ান্টাইজড মডেলও লোড করতে পারে, তবে বড় আপসের সঙ্গে।

আমরা নিজেরাই Ollama দিয়ে **2 GB Pi 4B** ও **8 GB Pi 5**-এ এসব মডেল পরীক্ষা করেছি; দুটিতেই microSD স্টোরেজ ছিল। টেবিলের পরীক্ষায় একই পাঁচটি ছোট সহকারী-প্রম্পট, একই সিস্টেম প্রম্পট, নির্দিষ্ট seed এবং 140-token আউটপুট সীমা ব্যবহৃত হয়েছে। প্রতিটি পরীক্ষার আগে অন্য মডেল আনলোড করেছি এবং ঠান্ডা অবস্থায় লোডের সময়, প্রথম দৃশ্যমান token আসার সময়, পুরো উত্তরের সময়, আউটপুট গতি ও সর্বোচ্চ resident memory মেপেছি। এগুলো ছোট উত্তরের কাজের এক-পাস পরীক্ষা। ফলাফল রিসোর্স নির্ধারণের উদাহরণ, সর্বজনীন গতি বা উত্তর-মানের র‌্যাঙ্কিং নয়। Pi 5-এর [Cortex-A76 CPU ও উপলভ্য মেমরি বিন্যাস](https://www.raspberrypi.com/products/raspberry-pi-5/) Pi 4-এর [Cortex-A72 প্ল্যাটফর্ম](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf) থেকেও উল্লেখযোগ্যভাবে আলাদা।

## কোন ধরনের মডেল উপযোগী

| মডেলের ধরন | পরিমাপে দেখা উদাহরণ | ব্যবহারিক কাজ |
|---|---|---|
| প্রায় 230M–600M প্যারামিটারের ছোট টেক্সট মডেল | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | ছোট স্থানীয় কমান্ড, সারাংশ ও সীমাবদ্ধ প্রশ্নোত্তর; 2 GB Pi 4-এর সেরা শুরু |
| প্রায় 1B–2B কমপ্যাক্ট টেক্সট মডেল | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Pi 5 বা বেশি মেমরির Pi 4-এ সূক্ষ্ম নির্দেশ মানার সুযোগ বেশি, তবে ক্ষুদ্র মডেলের চেয়ে উত্তর ধীর |
| কোয়ান্টাইজড 3B–4B টেক্সট মডেল | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | প্রতি উত্তরে কয়েক সেকেন্ড অপেক্ষা গ্রহণযোগ্য হলে 8 GB Pi 5-এর বেশি সক্ষম বিকল্প |
| বড় sparse বা hybrid মডেল | LFM2.5 8B | পরীক্ষিত 8 GB Pi 5-এ চলে, তবে মেমরি বেশি লাগে ও cold load দীর্ঘ |

এগুলো **টেক্সট তৈরির** ফল। ছবি তৈরি, কথা শনাক্তকরণ, দৃষ্টিশক্তি বা প্রশিক্ষণের পারফরম্যান্স প্রমাণ করে না। “চলে” বলতে শুধু মডেল ফাইল কার্ডে ধরে বোঝায় না: runtime, context cache, অপারেটিং সিস্টেম ও অন্য সার্ভিসেরও RAM লাগে। Quantization ওজনের ফাইল ছোট করে, তবে উত্তরমান কমাতে পারে, বিশেষত 1-bit ওজনের মতো চরম সেটিংয়ে।

### সংখ্যাগুলো কী মাপে

Benchmark-এ Ollama chat API-তে তথ্য, নিরাপত্তা পদ্ধতি, পুনরুদ্ধার করা context, আবহাওয়া ও সহায়তা নিয়ে ছোট prompt পাঠানো হয়। প্রতিটি মডেল একই prompt সেট ও seed পেয়েছে। সময় মাপার আগে মডেল আনলোড করেছি, যাতে পরের অনুরোধে cold load থাকে। **মোট সময়** পুরো request-এর সময়, আর **tokens per second** শুধু আউটপুট তৈরির গতি। প্রথম *দৃশ্যমান* token-ও রেকর্ড করেছি, কারণ মডেল উত্তর দেওয়ার আগে reasoning-এ সময় দিতে পারে।

মেমরি মাপতে প্রতিটি request চলাকালে Pi-র উপলভ্য RAM ও swap-এর পাশাপাশি Ollama এবং inference process-এর resident memory নিয়েছি। **RSS**-এর মান process-এর resident memory, পুরো host-এর চাহিদা নয়। ফাইল-সমর্থিত পেজ, OS, browser বা অন্য স্থানীয় সার্ভিসের কারণে কাগজে-কলমে ধরে এমন মডেলেও swap হতে পারে। টেবিলে প্রথম পাঁচ-prompt, এক-পাস পরীক্ষা আছে। পরে news prompt ও reply-rule check যোগ করেছি। এসব check কী দেখতে হবে বোঝায়, কিন্তু আগের timing-কে ছয়-prompt compliance ফল করে না।

Tokens per second বা parameter count কোনোটিই মানের স্কোর নয়। দ্রুত লেখা তৈরি করেও মডেল উৎস বাদ দিতে, শব্দসীমা ছাড়াতে বা অসম্পূর্ণ বাক্য দিতে পারে। যেসব prompt পাঠাবেন সেগুলো দিয়ে মডেল তুলনা করুন এবং অ্যাপের জন্য বাছার আগে উত্তর পড়ুন।

## Raspberry Pi 4: সবচেয়ে ছোট মডেল বেছে নিন

পরীক্ষিত 2 GB Pi 4-এ মেমরির বাড়তি জায়গা কম ছিল। ছোট LFM2.5 মডেল এবং `qwen2.5:0.5b` পাঁচটি prompt-ই শেষ করেছে। ছোট offline উত্তর বা ক্ষুদ্র স্থানীয় সহকারীর জন্য এগুলো যুক্তিসঙ্গত।

| মডেল | মডেল ফাইল | মাপা আউটপুট গতি | গড় উত্তর সময় | মেমরি বা ফল |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF আমদানি | 0.25 GB | 12.8 tokens/s | 7.2 s | সর্বোচ্চ resident memory 383 MB; 5/5 prompt |
| LFM2.5-350M, GGUF আমদানি | 0.38 GB | 8.6 tokens/s | 8.6 s | সর্বোচ্চ resident memory 516 MB; 5/5 prompt |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 prompt; Ollama থেকে সরাসরি পাওয়া যায় |
| MiniCPM5-1B, GGUF আমদানি, reasoning বন্ধ | 0.69 GB | 5.9 tokens/s | 12.2 s | সর্বোচ্চ resident memory 883 MB; 5/5 prompt |
| MiniCPM5-1B, GGUF আমদানি, default reasoning | 0.69 GB | 5.7 tokens/s | 33.3 s | পাঁচটির মধ্যে মাত্র একটিতে কার্যকর দৃশ্যমান উত্তর |
| `qwen3:0.6b`, default reasoning | 0.52 GB | 6.4 tokens/s | 40.4 s | একটি ফাঁকা উত্তর; বোর্ড reboot করেছে |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, swap বা reboot নেই; ধীর হলেও স্থিতিশীল |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | ভারী swap; পরীক্ষা চলাকালে বোর্ড reboot করেছে |
| `qwen3.5:0.8b` | 1.04 GB | — | — | শেষ হয়নি; বোর্ড reboot করেছে |

Pi 4-এর ফল সিস্টেমের অন্য কাজের ওপর বিশেষভাবে নির্ভরশীল। বড় মডেলের পরীক্ষায় বোর্ড reset হয়েছে, যার মধ্যে `qwen3.5:0.8b` চালানোও অসমাপ্ত ছিল। এটি আমাদের 2 GB সেটআপের প্রমাণ, সব Pi 4 বা সব 1B মডেল reboot করবে এমন দাবি নয়। 4 GB বা 8 GB Pi 4-এ মেমরি বেশি, তবে CPU পরীক্ষিত Pi 5-এর চেয়ে ধীর inference দেবে। ওই Pi 4 memory variant সরাসরি মাপিনি।

Pi 4-এর প্রথম দিকের একটি পরীক্ষা চূড়ান্ত ফলের চেয়ে অনেক খারাপ ছিল: RAM-ভিত্তিক `/tmp`-এ প্রায় 625 MB অস্থায়ী GGUF ছিল, ফলে মাত্র 500–600 MB ফাঁকা থাকে এবং শত শত MB swap-এ যায়। ফাইল স্থায়ী স্টোরেজে সরানোর পর ছোট মডেলের ফল inference memory ভালোভাবে দেখায়। 2 GB বোর্ডে *download কোথায় রাখছেন* তাও benchmark বদলে দিতে পারে।

**পরামর্শ:** এই 2 GB বোর্ডে default হিসেবে আমদানি করা LFM2.5-350M বেছে নিই। এটি **516 MB RSS**-এ স্থির ছিল, প্রায় **1 GB RAM খালি** রেখেছিল এবং Pi 4 reply-rule পরীক্ষায় **5/6** পেয়েছিল। Pi 5-এর repeated test-এ কখনও উৎসের নাম বাদ গেছে, তাই attribution দরকার এমন অ্যাপে তা পরীক্ষা করুন। Latency ও memory headroom সবচেয়ে গুরুত্বপূর্ণ হলে LFM2.5-230M নিন: এটি দ্রুত ও হালকা, কিন্তু এক medical-context উত্তরে “nausea or vomiting”-কে “nausea/ventilator use” করেছে। এই বিষয়গত ভুলের কারণে স্বাস্থ্য বা নিরাপত্তার উত্তরে এটি দুর্বল default, যদিও পুনরাবৃত্ত mechanical compliance score বেশি। [Ollama registry](https://ollama.com/library/qwen2.5/tags) থেকে মডেল দরকার হলে `qwen2.5:0.5b` নিন, তবে instruction compliance দুর্বল। `granite4:350m` স্থিতিশীল ছিল, কিন্তু ধীর ও বেশি memory ব্যবহার করেছে। Client reasoning বন্ধ করলেই MiniCPM5-1B চলার মতো। এই নির্দিষ্ট 2 GB setup-এ আমাদের পরীক্ষায় reboot হওয়ায় Gemma 3 1B ও Qwen3.5 0.8B এড়িয়ে চলুন।

## Raspberry Pi 5: বেশি বিকল্প, গতির বিনিময়ে

8 GB Pi 5 speed ও memory benchmark-এর **25টি মডেলই** চালিয়েছে। ছোট-উত্তরের কাজের জন্য অনুপযুক্ত মডেলসহ সব run টেবিলে আছে। † চিহ্নে আমদানি করা GGUF বোঝায়। “Think off” speed run-এর সেটিং; আলাদা compliance পরীক্ষায় সেটিই ব্যবহৃত হয়েছে এমন নয়।

| মডেল | ফাইল GB | আউটপুট tok/s | উত্তর s | সর্বোচ্চ RSS MB | ছোট উত্তরের মূল্যায়ন |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | সর্বনিম্ন latency; repeated compliance 78% |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | এড়ান: 1-bit weight এবং এক-পাস compliance 3/6 |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | দ্রুত, তবে 18টির মধ্যে 5টি উত্তরে উৎস বাদ |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | সহজ registry বিকল্প; repeated compliance 61% |
| `qwen3:0.6b`, reasoning বন্ধ | 0.52 | 23.0 | 4.3 | 1,069 | শর্তসাপেক্ষ: 4/6, reasoning setting গুরুত্বপূর্ণ |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | পরীক্ষামূলক 1-bit model; এক-পাস 6/6 নিশ্চিত নয় |
| `minicpm5-1b` †, reasoning বন্ধ | 0.69 | 18.4 | 5.1 | 869 | শর্তসাপেক্ষ: default reasoning-এ ফাঁকা উত্তর |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | ধরে, তবে ছোট LFM2.5-এর চেয়ে বড় ও ধীর |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | আমাদের কাজে সেরা; repeated compliance 89% |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | registry বিকল্প; compliance 5/6 |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | registry-only মডেলের মধ্যে সেরা repeated compliance: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6; Gemma 3 1B নিয়ম ভালো মেনেছে |
| `qwen3.5:0.8b`, reasoning বন্ধ | 1.04 | 8.8 | 12.2 | 1,592 | default reasoning-এ 0/6; reasoning নিয়ন্ত্রণ না থাকলে এড়ান |
| `spark-x2.5-1.7b` †, reasoning বন্ধ | 1.11 | 9.7 | 9.4 | 1,542 | default reasoning-এ 0/6; reasoning নিয়ন্ত্রণ না থাকলে এড়ান |
| `qwen3:1.7b`, reasoning বন্ধ | 1.36 | 8.1 | 12.4 | 1,867 | শর্তসাপেক্ষ; ছোট বিকল্পের চেয়ে বেশি memory ও delay |
| `minicpm5-2b` †, reasoning বন্ধ | 1.56 | 7.7 | 10.9 | 1,787 | শর্তসাপেক্ষ; এক-পাসে 5/6, অতিরিক্ত bullet |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | পরীক্ষার জন্য 3B বিকল্প; এক-পাসে 5/6 |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | interactive ব্যবহারে এড়ান: decode ধীর |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | বিকল্প 3B পরীক্ষা; compliance run রিপোর্ট নেই |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | ধরে, তবে ছোট বিকল্পের চেয়ে উত্তর ধীর |
| `qwen3.5:2b`, reasoning বন্ধ | 2.74 | 5.0 | 16.1 | 3,627 | বেশি memory ও delay; compliance run রিপোর্ট নেই |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | দ্রুত উত্তরের জন্য এড়ান; প্রথম token-এ 14.3 s |
| `ling-3.0-tiny` †, reasoning বন্ধ | 4.82 | 9.9 | 19.4 | 5,071 | বড় footprint; এক-পাসে 5/6, grounding failure-সহ |
| `lfm2.5:8b`, reasoning বন্ধ | 5.16 | 8.7 | 54.6 | 5,317 | কষ্টে ধরে; cold load 34.4 s, উত্তর দীর্ঘ |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | এড়ান: অন্য Pi service চলাকালে swap চাপ |

† আমদানি করা GGUF। উত্তর সময় ও memory-র মান Pi 5-এর পাঁচ-prompt speed run থেকে; compliance মান আলাদা ছয়-prompt পরীক্ষা থেকে এসেছে। compliance score না থাকলে reply-rule অনুসরণের প্রমাণ মেলেনি।

ছোট LFM2.5 মডেলগুলো এই ছোট উত্তরের কাজে দ্রুততম ছিল। পরীক্ষিত Pi 5-এ 1.2B সংস্করণটি ব্যবহারিক মধ্যপথ। Gemma 3 1B registry-only বিকল্প, যা পরবর্তী পরীক্ষায় Qwen2.5 1.5B-এর চেয়ে বেশি বার উত্তর নিয়ম মেনেছে। বেশি সক্ষমতা দরকার এমন prompt-এ 3B মডেলের ধীর output গ্রহণযোগ্য হতে পারে, কিন্তু এই timing একা কোনটি ভালো উত্তর দেয় তা প্রমাণ করে না।

Cold-load ও first-token delay ব্যবহারের অভিজ্ঞতা বদলায়। Pi 5-এ LFM2.5-230M প্রায় **0.21 seconds**-এ load হয়েছে এবং **0.37 seconds**-এ দৃশ্যমান token দিয়েছে। Qwen2.5 1.5B load-এ **2.59 seconds**, প্রথম দৃশ্যমান token-এ **3.66 seconds** নিয়েছে; Qwen2.5 3B নিয়েছে **5.60** ও **7.97 seconds**। মাঝে মাঝে প্রশ্নে generation শুরুর পরের output rate-এর চেয়ে এই delay গুরুত্বপূর্ণ হতে পারে। মডেল সবসময় load থাকলে এ বিলম্ব কম, তবে request-এর মাঝেও memory দখল করে।

অন্য measured candidate-ও দেখায় কেন শুধু parameter count দিয়ে সাজানো যায় না। reasoning বন্ধ রেখে `qwen3:0.6b` Pi 5-এ **1,069 MB RSS**-এ **23.0 tokens/s** করেছে, আর আমদানি করা MiniCPM5-1B **869 MB RSS**-এ **18.4 tokens/s** করেছে। `granite4:350m`-এর নাম 350M হলেও **0.71 GB** download দরকার হয়েছে এবং গতি ছিল **12.1 tokens/s**। Model packaging ও architecture নাম, file size, memory ও speed-এর সম্পর্ক বদলায়।

Client নির্ভরযোগ্যভাবে `think: false` পাঠাতে পারলে LFM2.5-এর বিকল্প হিসেবে Qwen3 0.6B ও MiniCPM5-1B পরীক্ষা করা যুক্তিসঙ্গত। MiniCPM5-2B, Qwen3 1.7B ও Spark-X2.5 1.7B-ও Pi 5-এ চলেছে, কিন্তু মূল পছন্দের তুলনায় speed ও memory-তে স্পষ্ট লাভ দেয়নি। MiniCPM5-1B ও Spark-X2.5-এর compliance test-এ default reasoning ছিল; তাদের ফাঁকা উত্তরকে think-off speed run-এর ফল বলা যাবে না। উল্টোভাবে, think-off-এ দ্রুত চলা প্রমাণ করে না যে ওই flag বাদ দেওয়া bridge ব্যবহারযোগ্য উত্তর পাবে।

কাঁচা গতির চেয়ে সহজ ইনস্টল গুরুত্বপূর্ণ হলে 8 GB Pi 5-এ Gemma 3 1B ও Llama 3.2 1B registry বিকল্প হিসেবে যুক্তিসঙ্গত। Gemma 3 1B repeated reply-তে **15/18** বার নিয়ম মেনেছে। Llama 3.2 1B একবারে **5/6** পেয়েছে, তাই অনুমান কম নিশ্চিত। সময় পরীক্ষায় Qwen2.5 1.5B Gemma 3 1B-এর চেয়ে দ্রুত load ও reply দিয়েছে, কিন্তু এক compliance pass-এ **4/6** পেয়েছে। নিজের prompt-এর প্রয়োজন দেখে বেছে নিন।

মাঝে মাঝে দীর্ঘ বা কঠিন text prompt-এর জন্য quantized Qwen2.5 3B ও Llama 3.2 3B আমাদের 8 GB Pi 5-এ মাঝারি memory ব্যবহারকারী 3B বিকল্প। Speed ও memory মেপেছি; Qwen2.5 3B এক compliance pass-এ **5/6** পেয়েছে। Llama 3.2 3B-এর তুলনীয় compliance run রিপোর্ট করা হয়নি। বেশি parameter ছোট মডেল যেখানে ব্যর্থ হয় সেখানে *পরীক্ষা করার* কারণ, ভালো উত্তর দেওয়ার প্রমাণ নয়। Granite 4 Micro ও Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny এবং Gemma 3n E2B Pi 5 পরীক্ষায় ধরে বা load হয়েছে, কিন্তু ছোট উত্তরের কাজে latency, memory headroom বা reliability কম আকর্ষণীয় ছিল।

দুটি Bonsai মডেল extreme quantization-এর দাম দেখায়। 1.7B ও 4B নামের তুলনায় তাদের Q1_0 ফাইল অস্বাভাবিক ছোট, কিন্তু 1.7B মডেল reply-rule check-এ মাত্র **3/6** পেয়েছে। 4B মডেল এক ছয়-prompt pass পেরেছে, কিন্তু প্রতি উত্তর **18.1 seconds** নিয়েছে এবং repeated compliance নিশ্চিত নয়। উত্তরমান গুরুত্বপূর্ণ হলে দুটিকে default recommendation নয়, experiment হিসেবে ধরুন।

LFM2.5-8B ফলের প্রেক্ষাপট দরকার: hybrid architecture প্রতি token-এ কম active parameter ব্যবহার করে, তাই এর decode rate মাপা dense 3B মডেলগুলোর চেয়ে বেশি ছিল। তবু microSD থেকে cold load হতে **34.4 seconds** এবং resident memory **5.3 GB-এর বেশি** লেগেছে। এটি কী চালানো যায় তা দেখায়, তবে অন্য service-সহ Pi-এর আরামদায়ক default নয়। মাপা `gemma3n:e2b`-ও প্রায় 5.3 GB resident memory ব্যবহার করেছে এবং test host-এর অন্য service-সহ swap ঘটিয়েছে।

LFM2.5 8B run উত্তর ছোট না রেখে পুরো **140-token cap**-এ পৌঁছেছিল। Gemma 3 4B প্রথম token-এ **14.3 seconds** এবং পূর্ণ উত্তরে **30.3 seconds** নিয়েছে। এই Pi 5-এ দুটোই load করা যায়, কিন্তু পরীক্ষায় responsive small assistant-এর মতো ছিল না। মানানসই ছোট উত্তর দেওয়া ক্ষুদ্র মডেল radio বা command interface-এ কাগজে দ্রুত decode করা বড় মডেলের চেয়ে ভালো হতে পারে।

## মেমরি, reasoning ও model format

আমাদের মাপ থেকে resident inference memory-র একটি প্রাথমিক হিসাব হলো **model download size × 1.4**। এটি কেবল আনুমানিক নিয়ম: context length, runtime setting, model architecture ও অন্য process প্রয়োজন বদলায়। Generation-এর সময় available memory দেখুন, ছোট host-এ একবারে একটি model load রাখুন এবং OS-এর জন্য জায়গা রাখুন। 4 GB বোর্ডে ছোট বা compact model দিয়ে শুরু করা যায়, তবে 4 GB recommendation অনুমান; সরাসরি 4 GB variant পরীক্ষা নয়।

যেমন Pi 5-এ 0.73 GB LFM2.5-1.2B ফাইল প্রায় **967 MB RSS**-এর সমান ছিল, আর 0.99 GB Qwen2.5 1.5B ফাইল **1,361 MB RSS**-এ উঠেছিল। এই মডেলে হিসাব মোটামুটি কাজে লাগে, তবে নির্দিষ্ট সীমা নয়। Pi-তে interface, search index, local library বা অন্য background service চললে model process-এর মাপা memory-র চেয়ে বেশি রাখুন। বাস্তব request-এ swap দেখুন; load হলেও সবসময় swap করা model ব্যবহারিকভাবে উপযুক্ত নয়।

কিছু model দৃশ্যমান উত্তরের আগে ভেতরের reasoning block তৈরি করে। পরীক্ষায় 2 GB Pi 4-এর `qwen3:0.6b` দৃশ্যমান text দিতে অনেক বেশি সময় নিয়েছে। MiniCPM5-1B default reasoning-এ পাঁচটির মধ্যে একটিতে কার্যকর উত্তর দিয়েছে; reasoning বন্ধে পাঁচটির সবকটিতে। ছোট reply budget হলে compatible Ollama API request-এ `think: false` দিন অথবা default-এ reasoning করে না এমন model নিন। সেটি সমর্থিত model ও client-এ কাজ করে; universal speed switch নয়।

পার্থক্যটি জরুরি, কারণ token cap-এ reasoning-এর token-ও থাকতে পারে, যদিও ব্যবহারকারী উত্তর দেখেন না। Pi 4-এ default reasoning-সহ `qwen3:0.6b` request-পিছু গড়ে **40.4 seconds** নিয়েছে; একটি prompt-এ দৃশ্যমান উত্তর ফাঁকা ছিল। MiniCPM5-1B default setting-এ গড় **33.3 seconds**, reasoning বন্ধে **12.2 seconds** নিয়েছে। Pi 5 run-এ নথিতে যেসব Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 ও Spark-X2.5-এর কথা আছে, সেগুলোর reasoning-ও বন্ধ করেছি। Client যে setting ব্যবহার করবে, সেই setting-এ model তুলুন।

### উত্তর ব্যবহারযোগ্য কি না দেখুন

আমাদের ছোট mesh-assistant কাজে reply contract গতি যতটা গুরুত্বপূর্ণ: সর্বোচ্চ **90 শব্দ**, সর্বোচ্চ **তিনটি bullet**, plain text, সম্পূর্ণ বাক্য, দেওয়া retrieval context ব্যবহার এবং উৎসের নাম উল্লেখ। Bridge text-কে **180-character chunk**-এ ভাগ করে। দ্রুত তৈরি হলেও দীর্ঘ উত্তর বেশি radio airtime নেয়।

Benchmark-এর পরের সংস্করণে ফাঁকা উত্তর, prompt-নির্দিষ্ট শব্দসীমা, অতিরিক্ত bullet, Markdown table বা code fence, অসমাপ্ত সমাপ্তি, দেওয়া context-এর term না থাকা এবং source name বাদ পড়া দেখা হয়। ব্যবহৃত assistant-এর deployed system prompt অনুযায়ী score করলে ছোট model নিয়মগুলো প্রায়ই ভেঙেছে। সবচেয়ে গুরুত্বপূর্ণ ব্যর্থতা ছিল reasoning token budget খরচ করলে **ফাঁকা উত্তর**, এরপর retrieved context উপেক্ষা বা source বাদ। শব্দ বা bullet limit ছাড়ালে text দৃশ্যমান ছিল, তবে airtime নষ্ট হয়েছে। এগুলো যান্ত্রিক পরীক্ষা, উত্তর পড়ার বিকল্প নয়: factual accuracy বা safety advice যথার্থ কি না প্রমাণ করে না।

#### Pi 5-এর repeated compliance ফল

প্রথমে deployed system prompt ও **220-token cap** দিয়ে প্রতি model-এ ছয় prompt একবার চালিয়েছি। আশাব্যঞ্জক model-কে ভিন্ন seed দিয়ে আরও দুবার পরীক্ষা করেছি, অর্থাৎ **প্রতি model-এ 18টি reply**। একবারের নিখুঁত ফল repeated ফল নিশ্চিত করেনি। নিচের repeated ফল পরীক্ষিত ছোট mesh reply-এর শক্ত তুলনা দেয়:

| মডেল | সব পরীক্ষিত নিয়ম মেনেছে এমন উত্তর | প্রধান দেখা ভুল |
|---|---:|---|
| আমদানি করা LFM2.5-1.2B | 16/18 (89%) | দুটি অসমাপ্ত উত্তর |
| `gemma3:1b` | 15/18 (83%) | তিনটি অসমাপ্ত উত্তর |
| আমদানি করা LFM2.5-230M | 14/18 (78%) | অসমাপ্ত উত্তর ও source name অনুপস্থিত |
| আমদানি করা LFM2.5-350M | 13/18 (72%) | source name অনুপস্থিত |
| `qwen2.5:0.5b` | 11/18 (61%) | বেশি bullet ও শব্দ, source name অনুপস্থিত |

**2 GB Pi 4**-এ আলাদা ছয়-prompt compliance pass-এ LFM2.5-350M **5/6**, LFM2.5-230M **4/6**, Qwen2.5-0.5B **2/6** পেয়েছে। MiniCPM5-1B default reasoning-এ **1/6** থেকে reasoning বন্ধে **5/6** হয়েছে। Pi 4-এর মান এক-pass ফল। তাই সাধারণ instruction-following নিয়ে বলার সময় repeated Pi 5 ফলকে বেশি গুরুত্ব দিই; Pi 4 run দিয়ে ওই বোর্ডে স্থিতি ও গতি দেখি।

ব্যর্থতার পরিণতি আলাদা। **ফাঁকা** উত্তর ব্যবহারকারীকে কিছু দেয় না; দেওয়া তথ্য উপেক্ষা করলে বিভ্রান্তি হতে পারে। source name না থাকলে পাঠক attribution যাচাই করতে পারে না। বাড়তি bullet বা শব্দে মূলত অতিরিক্ত 180-character packet লাগে। অসমাপ্ত বাক্য truncation-এর ইঙ্গিত হতে পারে। LFM2.5-230M-এর medical-term ভুল মনে করায়, যান্ত্রিক check পাস করেও উত্তর ভুল হতে পারে। repeated test-এর পাঁচ model-এর কোনোটিই 18টি উত্তরের সবকটিতে সব নিয়ম মানেনি। কঠোর length বা format দরকার এমন app-এ generation-এর পর তা প্রয়োগ করুন এবং উচ্চ-ঝুঁকির বিষয় আলাদাভাবে যাচাই করুন।

পুনরুদ্ধার করা WikiMed context নিয়ে বাস্তব bridge endpoint, Ollama-র OpenAI-compatible `/v1/chat/completions`,-ও পরীক্ষা করেছি। Pi 5-এ LFM2.5-1.2B দেওয়া ছয় term ব্যবহার করে 28-শব্দের উত্তর দিয়েছে; Qwen2.5-0.5B সাতটি term ব্যবহার করে 38-শব্দের উত্তর দিয়েছে। দুটোই 180-character-এর দুই packet-এ ধরেছে। Endpoint check দেখায় import করা LFM2.5 bridge request path-এ কাজ করে, কিন্তু একটি সফল উত্তর reliability-র নিশ্চয়তা নয়।

Ollama অনেক ready-to-pull model প্রকাশ করে, এর মধ্যে [Qwen2.5-এর 0.5B, 1.5B ও 3B variant](https://ollama.com/library/qwen2.5/tags) আছে। আমরা ছোট LFM2.5 model Ollama-তে এনেছি [Liquid AI-এর GGUF release](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main) থেকে। download-এর আগে নির্দিষ্ট tag বা GGUF filename দেখুন; registry ও repository বদলাতে পারে। GGUF download persistent storage-এ রাখুন; পরীক্ষায় RAM-backed `/tmp` Pi 4-এর সীমিত memory নিয়েছে।

### Registry tag ও GGUF import

প্রথম পরীক্ষার সবচেয়ে ছোট পথ Ollama tag: নির্দিষ্ট tag pull করে চালান। টেবিলের ছোট LFM2.5-গুলো **GGUF import**, Ollama-র public library-তে `lfm2.5-230m`, `lfm2.5-350m` বা `lfm2.5-1.2b` নামে tag নয়। GGUF model file format; `Q8_0` ও `Q4_K_M`-এর মতো নাম quantization বোঝায়। ব্যবহৃত 230M ও 350M LFM2.5 file ছিল Q8_0, আর 1.2B file ছিল Q4_K_M। অন্য quantization-এ একই parameter count মানেই একই file size, memory use বা quality নয়।

পরীক্ষিত 350M variant import করতে GGUF persistent storage-এর directory-তে download করুন, path-সহ Modelfile বানান এবং Ollama-কে model store-এ copy করতে দিন:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

Import-এর সময় download করা file ও Ollama-র copy, দুটির জন্য সাময়িক জায়গা লাগে। বড় GGUF transfer মাঝেমধ্যে ভেঙে যাওয়ায় resumable download ব্যবহার করেছি। import-এর আগে download-এর SHA-256 source প্রকাশিত hash-এর সঙ্গে মিলিয়ে নিন; অসম্পূর্ণ transfer model-এর সমস্যা বলে মনে হতে পারে। আমাদের Pi-তে `/tmp` RAM-backed ছিল, তাই সেখানে GGUF রাখলে inference-এর memory কমত।

## ব্যবহারিক শুরু

| হার্ডওয়্যার ও লক্ষ্য | প্রথমে যে মডেল চেষ্টা করবেন | কারণ |
|---|---|---|
| 2 GB Pi 4, default | আমদানি করা LFM2.5-350M | 516 MB RSS-এ স্থিতিশীল, প্রায় 1 GB available; 230M-এর medical-term ভুলের পরে নির্বাচন |
| 2 GB Pi 4, কম latency | আমদানি করা LFM2.5-230M | 383 MB RSS ও গড় উত্তর 7.2 s; স্বাস্থ্য বা নিরাপত্তা প্রশ্নে বিষয়বস্তু ভালোভাবে যাচাই করুন |
| 2 GB Pi 4, registry-only | `qwen2.5:0.5b` | Ollama থেকে সরাসরি pull, Pi 4-র পাঁচ-prompt run-এ স্থিতিশীল; Pi 5-এ repeated compliance 61% |
| 4 GB Pi 4 বা Pi 5 | আমদানি করা LFM2.5-1.2B, তারপর স্থানীয় পরীক্ষা | 8 GB Pi 5-এ 967 MB RSS ও 89% repeated compliance; 4 GB variant সরাসরি মাপিনি |
| 8 GB Pi 5, responsive assistant | আমদানি করা LFM2.5-1.2B | 15.5 tokens/s, পূর্ণ উত্তর 4.7 s, এবং মাপা মডেলগুলোর সর্বোচ্চ repeated compliance |
| 8 GB Pi 5, registry-only setup | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS, 83% repeated compliance |
| 8 GB Pi 5, বড় text model পরীক্ষা | quantized Qwen2.5 3B বা Llama 3.2 3B | দুটো প্রায় 5 tokens/s-এ চলে ও 2.4–2.8 GB RSS নেয়; Qwen2.5 3B এক compliance pass-এ 5/6 পেয়েছে |

এই বিকল্পগুলো এমন Pi-তে ছোট, দরকারি উত্তরকে অগ্রাধিকার দেয় যেখানে অন্য service-ও চলতে পারে। এগুলো শুরু করার পথ, সব কাজের জন্য কোনো মডেল শ্রেষ্ঠ এমন দাবি নয়। Pi 5-এর এক-pass compliance check-এ default reasoning-সহ `qwen3.5:0.8b` ও Spark-X2.5 কোনো compliant reply দেয়নি; MiniCPM5-1B পেয়েছে 1/6। Client reasoning বন্ধ করতে না পারলে ছোট-উত্তরের কাজে এগুলো এড়ান। Deploy করার পরিকল্পিত prompt, context, concurrency ও response limit দিয়ে চূড়ান্ত মডেল পরীক্ষা করুন।

Registry model-এর জন্য [Linux-এ Ollama ইনস্টল](https://ollama.com/download/linux) করে চালান:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

নিজের prompt, কাঙ্ক্ষিত উত্তর-দৈর্ঘ্য ও অন্য service চালু রেখে পরীক্ষা করুন। মোট উত্তর সময় ও memory use দুটোই লিখে রাখুন। Parameter count একা যতটা বলে তার চেয়ে এতে Pi-তে মডেলটি মানাবে কি না ভালো বোঝা যায়।

সীমিত memory-র node-এ পরীক্ষার সময় swap দেখুন। বড় model board ধীর করে দিলে ছোট model নিন এবং Ollama service-এর memory cap এমনভাবে দিন যাতে অতিরিক্ত বড় load host memory শেষ করার আগে ব্যর্থ হয়। Service cap সুরক্ষা, বড় model-কে ছোট করে না। Pi 4-এর reboot দেখায়, tokens per second-এর পাশাপাশি responsiveness ও memory headroom-ও নির্বাচন মানদণ্ড হওয়া উচিত।

## Benchmark-কে deployment সিদ্ধান্তে রূপ দিন

দৈনন্দিন ব্যবহারের আগে চারটি সীমা লিখে রাখুন: **সর্বোচ্চ উত্তর সময়, সর্বোচ্চ resident memory, response format ও failure behavior**। একই বোর্ডের অন্য service-সহ এসব সীমা পরীক্ষা করুন। একা পাস করলেও radio bridge বা dashboard-এর পাশে swap করানো model deployment requirement পূরণ করে না।

একটি ছোট fallback model ইনস্টল রাখুন। প্রধান model memory limit ছাড়ালে, ফাঁকা উত্তর দিলে বা response contract ভাঙলে সেটিতে যান। প্রতিটি তুলনায় model tag, quantization, Ollama version, prompt, context length ও seed লিখুন, যাতে পরের model update-কে hardware improvement মনে না হয়।
