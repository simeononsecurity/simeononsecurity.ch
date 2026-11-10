---
title: "স্থানীয় মডেলে Claude Cowork ও Claude Code: ২০২৬ সালের সেটআপ গাইড"
date: 2026-09-22
lastmod: 2026-11-09
toc: true
draft: false
description: "Anthropic-সামঞ্জস্যপূর্ণ API ব্যবহার করে Claude Desktop ও Claude Code-এর সঙ্গে Ollama কনফিগার করুন। ২০২৬ সালের মডেল ও ক্লাউড-নির্ভর ফিচারগুলো দেখুন।"
genre: ["স্থানীয় এআই", "এআই প্রোগ্রামিং টুল", "স্ব-হোস্ট করা এআই", "ডেভেলপার টুল", "গোপনীয়তা", "ওপেন সোর্স মডেল", "স্বয়ংক্রিয়করণ", "এআই হার্ডওয়্যার"]
tags: ["claude cowork", "claude code", "claude desktop স্থানীয় মডেল", "ollama claude code", "anthropic base url", "anthropic_auth_token", "claude code স্থানীয় মডেল", "claude অফলাইনে চালানো", "স্থানীয় এআই কোডিং এজেন্ট", "ollama launch claude", "claude desktop ollama", "স্থানীয় llm কোডিং", "ব্যক্তিগত এআই কোডিং", "অফলাইন এআই কোডিং", "স্থানীয় এআই এজেন্ট", "qwen3.8", "glm ক্লাউড মডেল", "টুল কলিং মডেল", "claude code সেটআপ", "বিনামূল্যে claude code", "API key ছাড়া claude", "স্থানীয় মডেলের কনটেক্সট উইন্ডো", "llama.cpp", "ollama cloud", "এআই কোডিং গোপনীয়তা", "নেটওয়ার্ক-বিচ্ছিন্ন এআই", "devops এআই টুল"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "আধুনিক কর্মস্থলে কম্পিউটারে কোডিং ইন্টারফেস দেখা যাচ্ছে, পাশে ট্যাবলেট ও স্মার্ট স্পিকার, পেছনে রঙিন আলোর ছোঁয়াসহ গাঢ় নীল পটভূমি।"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Claude-এর এজেন্ট টুলগুলো এখন আপনার নিজের হার্ডওয়্যারে থাকা মডেলের সঙ্গে চলে। API key, সাবস্ক্রিপশন বা ডিভাইসের বাইরে ডেটা পাঠানোর দরকার নেই।** Ollama Anthropic-সামঞ্জস্যপূর্ণ API দেয়, আর কয়েকটি কমান্ডে Claude Code ও Claude Desktop তাতে যুক্ত হয়।

*অনেক গাইডে একটি গুরুত্বপূর্ণ বিষয় বাদ পড়ে। সেখানে Claude Cowork-এর কথা বলে পরে এমন ধাপ দেওয়া হয়, যা কমান্ড-লাইন টুল কনফিগার করে। এগুলো আলাদা দুটি ইন্টিগ্রেশন, আর একটিতেই Cowork পাওয়া যায়।*

এই গাইডে দুটি পথ আলাদাভাবে ব্যাখ্যা করা হয়েছে, জনপ্রিয় টিউটোরিয়ালগুলো যে পরিবেশ ভেরিয়েবলটি বাদ দেয় সেটিও দেখানো হয়েছে, সেপ্টেম্বর ২০২৬ অনুযায়ী কোন পথে কোন মডেল উপযুক্ত তা বলা হয়েছে, এবং কনফিগারেশন যাই হোক ক্লাউডেই থেকে যায় এমন ফিচারগুলো চিহ্নিত করা হয়েছে।

**এই গাইড শেষে:** আপনার দরকারি ইন্টিগ্রেশনটি শনাক্ত করে Ollama-র নথিভুক্ত পদ্ধতিতে যুক্ত করবেন এবং একটি টুল-কলিং পরীক্ষায় endpoint যাচাই করবেন। স্থানীয় ইনফারেন্সে মডেলের অনুরোধ ডিভাইসের ভেতরে থাকে তখনই, যখন স্থানীয় মডেল বেছে নিয়ে ক্লাউড-নির্ভর ফিচার এড়িয়ে চলেন।

## সংক্ষিপ্ত উত্তর

**Ollama-র সঙ্গে Claude যুক্ত করার দুটি আলাদা উপায় আছে। ভুলটি বেছে নেওয়াই সেই সাধারণ কারণ, যার ফলে নির্দেশিকা অনুসরণের পর টার্মিনাল চলে কিন্তু Cowork পাওয়া যায় না।**

| ইন্টিগ্রেশন | কী পাবেন | সেটআপ পদ্ধতি | প্ল্যাটফর্ম |
|---|---|---|---|
| **Claude Desktop** | Cowork, সাবএজেন্ট, ওয়েব সার্চ, অটো মোড | Ollama অ্যাপ, এরপর **Apps** ও **Connect Claude** | **শুধু macOS** |
| **Claude Code** | টুল কলিং ও ফাইল সম্পাদনাসহ CLI কোডিং এজেন্ট | `ollama launch claude` অথবা পরিবেশ ভেরিয়েবল | macOS, Linux, Windows |

**Cowork চাইলে Claude Desktop ইন্টিগ্রেশন ব্যবহার করুন।** Ollama অ্যাপে গ্রাফিক্যাল পদ্ধতিতে এটি সেট করা হয়, এবং এটি শুধু macOS-এ পাওয়া যায়। Windows সমর্থন এখনো আসন্ন বলে দেখানো হয়েছে।

**টার্মিনালে এজেন্ট চাইলে Claude Code ব্যবহার করুন।** একটি কমান্ডই যথেষ্ট।

*দুটিই বিনামূল্যে। খরচ শুধু হার্ডওয়্যার ও বিদ্যুতে।*

## একটি নয়, দুটি ইন্টিগ্রেশন

নাম থেকেই বিভ্রান্তি শুরু হয়। **Claude Cowork হলো Claude Desktop-এর ভেতরের একটি ফিচার**, আলাদা অ্যাপ্লিকেশন নয়, Claude Code-এর আরেক নামও নয়।

Ollama-র নথিতে দুটি পণ্য আলাদা পৃষ্ঠা ও আলাদা শিরোনামে আছে। Claude Desktop আছে **Assistants** অংশে, OpenClaw ও Hermes-এর পাশে। Claude Code আছে **Coding** অংশে, OpenCode, Cline ও Codex CLI-এর পাশে।

পার্থক্যটি গুরুত্বপূর্ণ, কারণ সেটআপ একেবারেই আলাদা:

- **Claude Desktop** Ollama অ্যাপের ইন্টারফেসে কনফিগার করা হয়। শেল প্রোফাইল বদলাতে হয় না।
- **Claude Code** পরিবেশ ভেরিয়েবল বা একটি চালু করার কমান্ড দিয়ে কনফিগার করা হয়।

যে গাইডে `ANTHROPIC_BASE_URL` এক্সপোর্ট করে `claude` চালাতে বলে, সেটি কমান্ড-লাইন টুল সেট করে। এই ধাপের পর Cowork ডেস্কটপ অভিজ্ঞতা আশা করলে, **সেটআপে কিছু ভাঙেনি। আপনি আলাদা পণ্য কনফিগার করেছেন।**

## Claude Desktop ও Cowork সেটআপ

এই পথ টার্মিনালের বদলে Ollama অ্যাপে চলে।

### প্রয়োজনীয় বিষয়

- macOS-এ **Ollama ইনস্টল করা**। Windows সমর্থন আসন্ন বলে নথিভুক্ত।
- স্থানীয়ভাবে চালালে আগে **একটি মডেল ডাউনলোড করা**। ক্লাউড মডেলের জন্য Ollama-তে সাইন ইন করে ক্লাউড মডেল চালু করুন। কিছু মডেলের জন্য অর্থপ্রদত্ত প্ল্যান লাগে।
- **Claude ইনস্টল করা।** না থাকলে সেটআপের সময় Ollama এটি ডাউনলোড করার প্রস্তাব দেয়।

### ধাপগুলো

1. Ollama খুলে **Apps** বেছে নিন।
2. **Connect Claude** বেছে নিন।
3. সেটআপের নির্দেশনা অনুসরণ করুন। অনুরোধ করলে Claude ইনস্টল করুন, এরপর বলা হলে এটি আবার চালু করুন।

এটাই পুরো পদ্ধতি। পরে মডেল বদলাতে **Ollama Settings** খুলে **Apps**-এ যান, মডেল বেছে নিয়ে **Restart Claude** নির্বাচন করুন।

### যেসব ফিচার পাওয়া যায়

Ollama-র নথিতে এই ইন্টিগ্রেশনে চারটি ফিচার সমর্থিত বলে উল্লেখ আছে:

- কঠিন কাজ শেষ করার জন্য **Cowork**
- বড় কাজ এজেন্টদের মধ্যে ভাগ করার জন্য **Subagents**
- ডিফল্টভাবে Ollama-র দেওয়া **Web search**
- **Auto mode**, যেখানে পরিবর্তনের আগে কখন অনুমতি চাইবে তা এজেন্ট ঠিক করে

*এই তালিকায় Cowork আছে। এই ইন্টিগ্রেশনে এটি পাওয়া যায়, কমান্ড-লাইন ইন্টিগ্রেশনে নয়।*

### সংযোগ বিচ্ছিন্ন করা

সংযোগ বিচ্ছিন্ন করলে Claude-এর আগের কনফিগারেশন ফিরে আসে, তাই পরিবর্তনটি ধ্বংসাত্মক নয়।

- ইন্টারফেসে **Apps** খুলে Claude disconnect করুন, তারপর অনুরোধ এলে Claude আবার চালু করুন।
- টার্মিনালে `ollama launch claude-desktop --restore` চালান।
- **Claude যুক্ত থাকা অবস্থায় Ollama বন্ধ করলেও Claude-এর স্বাভাবিক কনফিগারেশন ফিরে আসে।** স্থানীয় সেটআপ রাখতে Ollama চালু রাখুন।

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Ollama অ্যাপের Apps প্যানেল থেকে Claude Desktop-এ সংযোগ, Ollama সেটিংসে মডেল নির্বাচন এবং আগের কনফিগারেশনে ফেরার পথ দেখানো চিত্র" >}}

## CLI থেকে Claude Code সেটআপ

প্রায় সব গাইডে এই পথটি আছে, এবং টার্মিনালের কাজের জন্য এটিই সঠিক পথ।

### এক কমান্ডের পদ্ধতি

```bash
ollama launch claude
```

এই কমান্ড প্রয়োজনীয় পরিবেশ ভেরিয়েবল সেট করে, Claude Code-কে স্থানীয় Ollama instance-এ নির্দেশ করে এবং চালু করে। তালিকা থেকে মডেল বেছে Enter চাপুন। আগে থেকেই মডেল নির্দিষ্ট করতে flag যোগ করুন:

```bash
ollama launch claude --model qwen3.5
```

*Wrapper পরিবেশ তৈরি করে দেয়। পরের অংশটিও পড়ুন, কারণ কোন মান সেট হচ্ছে তা জানলে পরে সমস্যা খুঁজে সমাধান করা সহজ হয়।*

### পরিবেশ ভেরিয়েবল হাতে সেট করা

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**দ্বিতীয় লাইনটি জনপ্রিয় গাইডে বাদ পড়ে।** `ANTHROPIC_API_KEY` ফাঁকা string রাখলে পরিবেশে আগে থেকে থাকা আসল key স্থানীয় সংযোগে বাধা দিতে পারে না। প্রকাশিত গাইডে এই লাইন না থাকলে আগে থেকে key export করা পাঠকেরা বিভ্রান্তিকর ত্রুটি পান।

শেল প্রোফাইল বদলানো এড়াতে কমান্ডেই সব মান দিন:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

সরকারি নথির দুটি বিষয় মনে রাখুন:

- **`ANTHROPIC_AUTH_TOKEN` bearer authentication বহন করে**, তাই স্থানীয় মোডে এর আক্ষরিক মান `ollama`।
- **Claude-এর নিজস্ব settings ফাইল শেল ভেরিয়েবলের ওপর প্রাধান্য পায়।** নতুন মান export করার পর সংযোগ অস্বাভাবিক হলে settings দেখুন এবং ব্যবহৃত endpoint দেখতে Claude Code-এ `/status` চালান।

### সরাসরি Ollama Cloud-এ সংযোগ

এই পথে Ollama ইনস্টল দরকার নেই। API key সেট করে Claude Code-কে Ollama-র hosted endpoint দিন:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**এই পথে একটি সীমাবদ্ধতা আছে।** Ollama-র নথি অনুযায়ী hosted web search ও উন্নত tool control পুরোপুরি সমর্থিত নয়। সামঞ্জস্যপূর্ণ মডেলে সাধারণ chat, ফাইল সম্পাদনা ও tool calling চলে।

## সেপ্টেম্বর ২০২৬-এর মডেল নির্বাচন

২০২৬ সালে মডেলের তালিকা অনেক বদলেছে। বসন্তে লেখা পরামর্শ আবার যাচাই করা উচিত।

| মডেল | ধরন | কনটেক্সট | কেন বেছে নেবেন |
|---|---|---|---|
| **Qwen3.8 27B** | স্থানীয়, 18 GB | 256K | দৃষ্টি, tool calling ও চিন্তা নিয়ন্ত্রণসহ বর্তমান সেরা স্থানীয় বহুমুখী মডেল |
| **Qwen3 Coder Next** | স্থানীয়, মোট MoE 80B / সক্রিয় 3B | 256K | সবসময় চালু কোডিং এজেন্টের জন্য তৈরি, দ্রুত কাজের জন্য non-thinking mode আছে |
| **Qwen3.6 35B A3B** | স্থানীয়, MoE 35B / সক্রিয় 3B | 262K | Apache 2.0 এবং সীমিত মেমরিতে কার্যকর |
| **kimi-k2.7-code:cloud** | ক্লাউড | বড় | স্থানীয় হার্ডওয়্যার ছাড়া কোডিং-কেন্দ্রিক ক্লাউড মডেল |
| **glm-5.3-flash** | ক্লাউড | বড় | Ollama-র নিজস্ব নথিতে প্রথমে প্রস্তাবিত মডেল |

**মেমরি যথেষ্ট হলে Qwen3.8 27B দিয়ে শুরু করুন।** এটি স্থানীয়ভাবে 256K context window, native vision, tool calling এবং প্রতি অনুরোধে চালু বা বন্ধ করা যায় এমন thinking সহ চলে। 24 GB বা তার বেশি মেমরির কার্ডে এটি প্রতিদিনের কাজে সুবিধাজনক।

**সেই মেমরি না থাকলে ক্লাউড মডেল দিয়ে শুরু করুন।** Claude Code-কে hosted মডেলে যুক্ত করে বিনা খরচে পরীক্ষা করা যায় এবং হার্ডওয়্যারের চিন্তা থাকে না, তবে আপনার কোড ডিভাইস ছাড়ে।

### Ternary মডেল সম্পর্কে সতর্কতা

আমাদের **[স্থানীয় এআই গাইডে](/articles/local-ai-2026-build-your-rig-now/)** দেখানো হয়েছে, ternary Bonsai 2 27B **5.53 GiB**-এ একটি সম্পূর্ণ 27B মডেল চালায়। এখানেও এটি আকর্ষণীয় মনে হতে পারে।

**এই কর্মপদ্ধতিতে এটি চলবে না।** Ternary kernel Prism ML-এর llama.cpp fork-এ আছে, আর stock Ollama ওই ফাইল লোড করতে পারে না। `ollama launch claude --model Ternary-Bonsai-2-27B` ধরনের কমান্ড ইনফারেন্স শুরু হওয়ার আগেই ব্যর্থ হয়। Claude Code-এ standard Qwen3.8 27B package ব্যবহার করুন, আর ternary package সেই উপযোগী runtime-এর জন্য রাখুন।

*এখানে সুবিধা ও সর্বোচ্চ দক্ষতার জন্য আলাদা পছন্দ দরকার। সমন্বিত টুলগুলো standard GGUF আশা করে।*

## মডেলকে দোষ দেওয়ার আগে 64K কনটেক্সট সেট করুন

রিপোজিটরিতে কাজের জন্য Ollama-র নথিতে সরাসরি নির্দেশনা আছে: একটি মডেল বেছে নিয়ে **64K বা তার বেশি context window সেট করুন**, বড় রিপোজিটরির জন্য মান আরও বাড়ান।

Claude Code ফাইলের বিষয়বস্তু, diff এবং কমান্ডের output context window-তে রাখে। ডিফল্ট মান ছোট হলে কাজ শেষ হওয়ার আগেই জায়গা ফুরিয়ে যায়। সমস্যাটি reasoning-এর বলে মনে হয়, কিন্তু কারণ থাকে সেটিংসে।

| কনটেক্সট | যেসব কাজ সামলায় |
|---|---|
| 32K-এর নিচে | একটি ফাইল সম্পাদনা এবং দ্রুত প্রশ্ন |
| **64K** | মাঝারি রিপোজিটরিতে একাধিক ফাইল নিয়ে কাজ |
| 128K | বড় রিপোজিটরি ও দীর্ঘ কমান্ড output |
| 256K | Qwen3.8 27B-এর সম্পূর্ণ window |

*Claude Code কাজের মাঝপথে ধারাবাহিকতা হারালে মডেল বদলানোর আগে context setting দেখুন।*

## একটি কমান্ডে tool calling যাচাই

Tool calling-ই এজেন্ট ও text generator-এর পার্থক্য। অনুমান না করে এটি পরীক্ষা করুন।

Claude Code চালু হলে বলুন:

```text
Read the current directory and list all files
```

**বাস্তব ফাইলের তালিকা দিলে tool calling কাজ করছে।** যদি বলে যে এটি ডিরেক্টরি পড়ত এবং সেখানে কী থাকতে পারে তা বর্ণনা করে, তাহলে ফিচারটি যুক্ত নেই। আপনি coding prompt-সহ একটি chat model ব্যবহার করছেন, এজেন্ট নয়। আরও prompt দিলে এটি ঠিক হবে না।

সমস্যার কারণগুলো এই ক্রমে দেখুন:

1. **tool support নিশ্চিত এমন মডেলে যান।** সব মডেল এটি সমর্থন করে না, এবং parameter count দেখে পার্থক্য বোঝা যায় না।
2. **পরিবেশ Ollama-র দিকে নির্দেশ করছে কি না দেখুন।** `ollama --version` চালিয়ে `ANTHROPIC_BASE_URL` স্থানীয় endpoint-এ সেট আছে কি না নিশ্চিত করুন।
3. **Claude Code-এ `/status` চালান।** Claude-এর নিজস্ব settings ফাইলে থাকা base URL বা credential সদ্য export করা shell variable-এর ওপর প্রাধান্য পায়।

## যেসব ফিচার শুধু ক্লাউডে থাকে

স্থানীয় ইনফারেন্সকে ঘিরে কর্মপদ্ধতি সাজানোর আগে সীমাটি বুঝুন।

| ফিচার | স্থানীয় মডেলে | ক্লাউডে |
|---|---|---|
| Chat ও ফাইল সম্পাদনা | হ্যাঁ | হ্যাঁ |
| Tool calling | মডেলনির্ভর | হ্যাঁ |
| Subagents | হ্যাঁ | হ্যাঁ |
| Web search | Ollama-র মাধ্যমে | হ্যাঁ |
| **Cowork** | Claude Desktop ইন্টিগ্রেশনের মাধ্যমে | হ্যাঁ |
| Auto mode | Claude Desktop ইন্টিগ্রেশনের মাধ্যমে | হ্যাঁ |
| নির্ধারিত prompt | Claude Code-এ `/loop` দিয়ে | হ্যাঁ |

স্থানীয় ব্যবহারে তিনটি সীমা মনে রাখুন:

- **গতি কমার আগে একাধিক ফাইল নিয়ে reasoning দুর্বল হয়।** একটি ফাইল ভালোভাবে, তিনটি মোটামুটি এবং পুরো রিপোজিটরি দুর্বলভাবে সামলায়। কাজের পরিসর সে অনুযায়ী রাখুন।
- **কিছু ক্লাউড মডেলের জন্য Ollama-র অর্থপ্রদত্ত প্ল্যান লাগে।** সাইন ইন করে মডেলগুলো চালুও করতে হবে।
- **সরাসরি ক্লাউড পথে কিছু ফিচারের সীমা আছে।** স্থানীয় ইনস্টল বাদ দিলে hosted web search ও উন্নত tool control পুরোপুরি সমর্থিত নয়।

*স্থানীয় ইনফারেন্স সীমাবদ্ধ ও যাচাইযোগ্য কাজে ভালো, বিস্তৃত ও অস্পষ্ট কাজে কম উপযোগী। এই সীমা মাথায় রেখে কাজ ভাগ করুন।*

## স্বয়ংক্রিয়করণ

দুটি ফিচার এই সেটআপকে শুধু ইন্টারেক্টিভ ব্যবহারের মধ্যে সীমাবদ্ধ রাখে না।

### Script ও CI-তে headless চালানো

`--yes` flag ইন্টারেক্টিভ selector এড়িয়ে যায় এবং দরকার হলে মডেল ডাউনলোড করে। এর জন্য `--model` দরকার, আর `--`-এর পরের সবকিছু সরাসরি Claude Code-এ যায়:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**অনুমতির ব্যবস্থা খেয়াল করুন।** Claude Code বেশিরভাগ কাজের আগে অনুমতি চায়, তাই headless চালাতে সেট করা permission rule অথবা বিচ্ছিন্ন পরিবেশ দরকার। গুরুত্বপূর্ণ রিপোজিটরিতে তত্ত্বাবধানহীন এজেন্ট চালাবেন না।

### `/loop` দিয়ে নির্ধারিত prompt

Claude Code session-এর ভেতরে `/loop` নির্দিষ্ট বিরতিতে prompt বা slash command চালায়:

```text
/loop 30m Check my open PRs and summarize their status
/loop 1h Research the latest AI news and summarize key developments
/loop 15m Check for new GitHub issues and triage by priority
```

*Session খোলা থাকা পর্যন্ত এটি চলে। এটি background daemon নয়, তাই session শেষ হলে এটিও থামে।*

## সমস্যা সমাধান

| লক্ষণ | সম্ভাব্য কারণ | সমাধান |
|---|---|---|
| **সংযোগ প্রত্যাখ্যাত** | Ollama চালু নেই | `ollama serve` চালান এবং `curl http://localhost:11434/api/tags` দিয়ে নিশ্চিত করুন |
| **কাজ করার বদলে কাজের বিবরণ দেয়** | নির্বাচিত মডেল tool calling সমর্থন করে না | tool support নিশ্চিত এমন মডেল বেছে নিন |
| **স্থানীয় endpoint-এর বদলে বাস্তব API key ব্যবহার হচ্ছে** | `ANTHROPIC_API_KEY` এখনো export করা আছে | উপরের মতো একে ফাঁকা string করুন |
| **সেটআপের পরে Cowork নেই** | Claude Desktop-এর বদলে Claude Code CLI সেট হয়েছে | Cowork-এর জন্য Ollama-র **Apps** পদ্ধতি ব্যবহার করুন |
| **তৈরি হতে সময় লাগে** | context অতিরিক্ত বড় অথবা sparse মডেল যথেষ্ট হলেও dense মডেল বেছে নেওয়া হয়েছে | context কমিয়ে mixture-of-experts মডেল চেষ্টা করুন |
| **Export করা ভেরিয়েবল কাজে লাগে না** | Claude-এর settings ফাইল shell variable-এর ওপর প্রাধান্য পায় | settings ফাইল দেখুন, তারপর `/status` চালান |
| **Background request ব্যর্থ হয়** | Claude Code অভ্যন্তরীণ কাজে ছোট মডেল বেছে নেয় | ছোট মডেলের override একই স্থানীয় মডেলে দিন |

*এই সাতটির মধ্যে দুটি সমস্যার কারণ একই। বেশিরভাগ সেটআপ সমস্যা ভুল endpoint অথবা tool calling-সমর্থনহীন মডেল থেকে আসে।*

## মূল বিষয়গুলো

- **Claude Desktop ও Claude Code আলাদা ইন্টিগ্রেশন।** Cowork Claude Desktop-এ আছে, macOS-এ Ollama-র **Apps** প্যানেলে সেট হয়। CLI পথ Cowork দেয় না।
- **এক কমান্ডে CLI পথ চালু হয়:** `ollama launch claude`। হাতে সেট করতে তিনটি ভেরিয়েবল লাগে, আর **অনেক গাইড `ANTHROPIC_API_KEY=""` বাদ দেয়**।
- **স্থানীয় ইনস্টল বাধ্যতামূলক নয়।** API key-সহ Claude Code-কে `https://ollama.com`-এ নির্দেশ করুন।
- **মডেল বিচার করার আগে অন্তত 64K context সেট করুন।** ছোট window-কে reasoning failure মনে হতে পারে।
- **একটি request-এ tool calling যাচাই করুন।** মডেল কাজ করার বদলে কী করত তা বললে, সেটি এজেন্ট নয়, text generator।
- **Ternary Bonsai package এখানে চলে না।** এর জন্য Prism ML-এর llama.cpp fork লাগে, stock Ollama এগুলো লোড করতে পারে না।
- **সংযোগ বিচ্ছিন্ন করা নিরাপদ।** Ollama বন্ধ করলে Claude-এর আগের সেটিং ফিরে আসে, আর টার্মিনাল থেকে `ollama launch claude-desktop --restore` চালানো যায়।

## পরবর্তী ধাপ

1. Claude কনফিগার করার আগে **tool support নিশ্চিত এমন মডেলসহ Ollama ইনস্টল করুন**: **[Ollama মডেল লাইব্রেরি](https://ollama.com/library)**
2. বর্তমান flag ও মডেলের জন্য **Ollama-র Claude Code পৃষ্ঠা পড়ুন**: **[Claude Code ইন্টিগ্রেশন](https://docs.ollama.com/integrations/claude-code)**
3. Cowork চাইলে **Claude Desktop পৃষ্ঠা ব্যবহার করুন**: **[Claude Desktop ইন্টিগ্রেশন](https://docs.ollama.com/integrations/claude-desktop)**
4. হার্ডওয়্যার কেনার আগে **স্থানীয় ইনফারেন্স গাইডের মেমরি স্তর দেখে মাপ ঠিক করুন**: **[২০২৬ সালের স্থানীয় এআই: 27B মডেল Sonnet 4.6-কে ছাড়ায়](/articles/local-ai-2026-build-your-rig-now/)**
5. কম বিদ্যুতের যন্ত্রে সবসময় চালু এজেন্ট চাইলে **ছোট হার্ডওয়্যার কী সামলায় দেখুন**: **[Raspberry Pi 4 বা 5-এ কোন এআই মডেল চলে?](/articles/ai-models-raspberry-pi-4-5/)**

## সম্পর্কিত নিবন্ধ

| নিবন্ধ | বিষয়বস্তু |
|---|---|
| **[২০২৬ সালের স্থানীয় এআই: 27B মডেল Sonnet 4.6-কে ছাড়ায়](/articles/local-ai-2026-build-your-rig-now/)** | স্থানীয় ইনফারেন্সের বেঞ্চমার্ক, ternary quantization এবং হার্ডওয়্যার নির্বাচন |
| **[Raspberry Pi 4 বা 5-এ কোন এআই মডেল চলে?](/articles/ai-models-raspberry-pi-4-5/)** | সবসময় চালু ছোট সহকারীর জন্য স্থানীয় ইনফারেন্স |
| **[গোপনীয়তা-রক্ষাকারী Meshtastic এআই সহকারী তৈরি](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | অফ-গ্রিড রেডিও চালায় এমন স্থানীয় মডেল, যেখানে গোপনীয়তাই মুখ্য |
| **[এআই ডেভেলপমেন্টের সেরা VS Code এক্সটেনশন](/articles/best-visual-studio-code-extensions-for-ai/)** | স্থানীয় কোডিং এজেন্টের সঙ্গে ব্যবহারের জন্য এডিটর টুল |

## সূত্র

1. [Claude Code ইন্টিগ্রেশন - Ollama ডকুমেন্টেশন](https://docs.ollama.com/integrations/claude-code)
2. [Claude Desktop ইন্টিগ্রেশন - Ollama ডকুমেন্টেশন](https://docs.ollama.com/integrations/claude-desktop)
3. [Ollama মডেল লাইব্রেরি](https://ollama.com/library)
4. [Qwen3.8 - Ollama মডেল লাইব্রেরি](https://ollama.com/library/qwen3.8)
5. [স্থানীয় মডেলে Claude Cowork - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Prism ML llama.cpp fork - ternary kernel](https://github.com/PrismML-Eng/llama.cpp)
