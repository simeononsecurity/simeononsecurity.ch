---
title: "Claude Code-এর ১০টি প্লাগইন, স্কিল ও MCP টুল: ব্যবহারিক নির্দেশিকা"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "পরিকল্পনা, কোড পর্যালোচনা, জ্ঞান ব্যবস্থাপনা, ডিজাইন ও অটোমেশনের জন্য Claude Code এক্সটেনশন বেছে নিন। দশটি টুল, নির্ভরতা ও ব্যবহারিক পরীক্ষা তুলনা করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "ডেভেলপার টুল", "সফটওয়্যার উন্নয়ন"]
tags: ["Claude Code প্লাগইন", "Claude Code স্কিল", "MCP টুল", "Graphify", "grill-me", "grill-with-docs", "grill-me-codex", "Claudex Loop", "Codex প্লাগইন", "কোড পর্যালোচনা", "claude-obsidian", "Obsidian", "CLAUDE.md", "Karpathy নির্দেশিকা", "Impeccable", "Higgsfield", "NotebookLM", "notebooklm-py", "n8n MCP", "AI উন্নয়ন কর্মপ্রবাহ", "এজেন্ট নির্দেশনা", "জ্ঞান গ্রাফ"]
cover: "/img/cover/claude-code-plugins-workflow-management-tools.webp"
coverAlt: "অন্ধকার পটভূমিতে কেন্দ্রীয় জ্যামিতিক হাবের সঙ্গে যুক্ত নীল ও বেগুনি টুল আইকন, ফোল্ডার এবং বিমূর্ত চার্ট প্যানেল"
coverCaption: "কর্মপ্রবাহের ধারণাগত চিত্র। চার্টের আকার কোনো পরিমাপ করা ফল দেখায় না।"
---

**আপনার কর্মপ্রবাহের নির্দিষ্ট সমস্যাকে ঘিরে Claude Code এক্সটেনশন বেছে নিন।** অস্পষ্ট প্রয়োজনের জন্য পরিকল্পনা আলোচনা দরকার। বাদ পড়া ত্রুটির জন্য পর্যালোচনা ও পরীক্ষা দরকার। বারবার গবেষণার জন্য অনুসরণযোগ্য উৎস দরকার। দায়িত্ব পরিষ্কার থাকলেই বেশি টুল উপকার করে।

এই নির্দেশিকায় এসব কাজের জন্য **দশটি প্রকল্প** তুলনা করা হয়েছে। এতে সেটআপের উদাহরণ এবং একটি সম্পূর্ণ মূল্যায়ন অনুশীলন আছে। বিশ্লেষণটি বর্তমান প্রকল্পের ডকুমেন্টেশন এবং দেওয়া Chase AI ভিডিও থেকে নেওয়া। সুপারিশ সম্পাদনাগত মতামত। এগুলো হাতে-কলমে কর্মক্ষমতার মাপ বা দশগুণ উৎপাদনশীলতার প্রমাণ নয়।

<!--more-->

## মূল বিষয়

- **আউটপুট দেখে বাছুন:** পর্যালোচিত পরিকল্পনা, কোড ম্যাপ এবং তৈরি ছবি আলাদা টুল চায়।
- **ইনস্টলেশনের স্তর আলাদা রাখুন:** নির্দেশনা, এক্সিকিউটেবল প্রোগ্রাম, প্লাগইন এবং সার্ভিস সংযোগের নির্ভরতা আলাদা।
- **বর্তমান নাম পরীক্ষা করুন:** Graphify এবং grill-me-codex এখন ভিন্ন ক্যানোনিক্যাল রিপোজিটরিতে আছে।
- **সম্মতির বাইরে যাচাই করুন:** দুটি মডেল পরিকল্পনা গ্রহণ করলেই বাস্তবায়ন সঠিক প্রমাণ হয় না।
- **গৃহীত কাজ মাপুন:** সেটআপ, সার্ভিস ব্যবহার, ব্যর্থ চেষ্টা এবং মানুষের সংশোধন লিখে রাখুন।

## শুরু করার আগে

**পূর্বশর্ত:** কার্যকর Claude Code ইনস্টলেশন, ফেলে দেওয়া যায় এমন একটি প্রকল্প বা শাখা, এবং নির্বাচিত বাহ্যিক সার্ভিস ব্যবহারের অনুমতি। CLI উদাহরণে টার্মিনাল ও উল্লিখিত প্যাকেজ ম্যানেজার ধরা হয়েছে। ক্লাউড ইন্টিগ্রেশনের জন্য নিজস্ব অ্যাকাউন্ট ও প্রমাণীকরণ লাগে।

**আনুমানিক সময়:** পড়তে ১৫ মিনিট। একটি সীমিত পরীক্ষার জন্য আরও ৩০ থেকে ৬০ মিনিট রাখুন। **কঠিনতা:** CLI সেটআপ ও সার্ভিস ইন্টিগ্রেশনে মধ্যম। নির্দেশনা-ভিত্তিক স্কিল পড়তে কম সেটআপ লাগে।

**১০ অক্টোবর ২০২৬-এ ডকুমেন্টেশন পরীক্ষা করা হয়েছে।** কমান্ড ও অ্যাক্সেস নিয়ম লিঙ্ক করা উৎসের সঙ্গে মেলে। পুরনো টিউটোরিয়াল অনুসরণের আগে ইনস্টল করা সংস্করণ আবার পরীক্ষা করুন। এই নিবন্ধে Claude Code থেকে ব্যবহৃত এক্সটেনশন দেখানো হয়েছে, প্রয়োজনে হোস্টের পার্থক্য উল্লেখ করা হয়েছে।

**ইনস্টলের পরে স্তরে স্তরে যাচাই করুন।** ফাইল, হোস্ট শনাক্তকরণ, এক্সিকিউটেবল নির্ভরতা, ক্রেডেনশিয়াল এবং একটি প্রতিনিধিত্বশীল কাজ আলাদা করে পরীক্ষা করুন। ইনস্টলার সফল হলেই ব্রাউজার, MCP সার্ভার, মিডিয়া টুল বা বাহ্যিক অ্যাকাউন্ট কাজ করে না। প্রথম পরীক্ষা সিন্থেটিক ডেটায় করুন এবং আপস্ট্রিম রিভিশন লিখে রাখুন।

## এক্সটেনশনের ধরন জানুন

| ধরন | ভূমিকা | উদাহরণ |
|---|---|---|
| **নির্দেশনা ফাইল** | স্থায়ী প্রকল্প প্রত্যাশা নির্ধারণ করে | CLAUDE.md |
| **স্কিল** | নির্বাচিত কাজের পদ্ধতি দেয় | grill-me |
| **প্লাগইন** | নিবন্ধিত কমান্ড ও ইন্টিগ্রেশন প্যাক করে | Codex প্লাগইন |
| **CLI** | টার্মিনাল থেকে কমান্ড চালায় | Graphify |
| **MCP সার্ভার** | এজেন্ট ক্লায়েন্টকে কলযোগ্য টুল দেয় | n8n ইন্টিগ্রেশন |

**Model Context Protocol (MCP)** এজেন্ট অ্যাপ্লিকেশনকে সার্ভারের প্রকাশ করা টুল ও ডেটার সঙ্গে যুক্ত করে। **Command-line interface (CLI)** এক্সিকিউটেবল কমান্ড চালায়। স্কিল এজেন্টকে যেকোনো ইন্টারফেস ব্যবহারের পদ্ধতি শেখায়, কিন্তু স্কিল থাকা কার্যকর সংযোগের প্রমাণ নয়।

**অনুপস্থিত সক্ষমতা দিয়ে শুরু করুন।** এজেন্টের রিপোজিটরি সার্চ থাকলে নতুন সার্চ পদ্ধতির দৃশ্যমান সুবিধা থাকা দরকার। এজেন্টের অটোমেশন প্ল্যাটফর্মে অ্যাক্সেস না থাকলে শুধু গদ্য নির্দেশনা প্রমাণীকৃত অ্যাক্সেস দেবে না। বিস্তৃত [এজেন্ট রানটাইম নির্দেশিকা](/articles/best-ai-agent-harnesses/) মডেল কল ও টুল এক্সিকিউশনের চারপাশের সফটওয়্যার ব্যাখ্যা করে।

## প্রথম টুল বেছে নিন

| সমস্যা | টুল | প্রথম গ্রহণযোগ্যতা পরীক্ষা |
|---|---|---|
| **অস্পষ্ট প্রয়োজন** | grill-me / grill-with-docs | স্পষ্ট সিদ্ধান্ত ও গ্রহণযোগ্যতার মানদণ্ড |
| **বারবার স্কোপ বদল** | Karpathy-অনুপ্রাণিত CLAUDE.md | প্রতিটি সম্পাদনা চাওয়া পরিবর্তনে কাজ করে |
| **ঝুঁকিপূর্ণ বাস্তবায়ন পরিকল্পনা** | Claudex Loop | প্রমাণসহ পর্যালোচনা ফল সমাধান |
| **অপর্যালোচিত কোড পরিবর্তন** | OpenAI Codex প্লাগইন | কোড ও ব্যর্থতার সঙ্গে যুক্ত ফল |
| **অপরিচিত রিপোজিটরি** | Graphify | উৎস ফাইলের সঙ্গে সম্পর্কের মিল |
| **ছড়ানো প্রকল্প জ্ঞান** | claude-obsidian | দাবির সঙ্গে মূল প্রমাণের লিঙ্ক |
| **বারবার উৎস সংশ্লেষণ** | notebooklm-py | নির্দিষ্ট উৎসে উত্তর উদ্ধৃত করা |
| **বিভ্রান্তিকর ইন্টারফেস** | Impeccable | ব্যবহারকারী কাঙ্ক্ষিত কাজ শেষ করে |
| **অনুপস্থিত ভিজ্যুয়াল সম্পদ** | Higgsfield | অনুমোদিত সম্পদ ব্রিফের সঙ্গে মিল |
| **পুনরাবৃত্তিযোগ্য সার্ভিস কর্মপ্রবাহ** | n8n MCP | পরীক্ষার এক্সিকিউশন প্রত্যাশিত ফল দেয় |

**প্রস্তাবিত শুরু:** একটি সারি বেছে নিয়ে ইনস্টলের আগে বেসলাইন টাস্ক সংরক্ষণ করুন। দ্বিতীয় টুল কেবল আলাদা, মাপযোগ্য অবদান দিলে যোগ করুন।

## কাজ পরিষ্কার করুন

### grill-me এবং grill-with-docs

**Matt Pocock-এর স্কিল** অস্পষ্ট ধারণাকে সিদ্ধান্তে রূপ দিতে সাহায্য করে। বর্তমান [grill-me প্রবেশপথ](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) শেয়ার্ড grilling স্কিল চালায়। [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) grilling ও domain modeling চালায়। [সংগ্রহের ডকুমেন্টেশন](https://github.com/mattpocock/skills) সাক্ষাৎকারের সঙ্গে ভাগ করা পরিভাষা ও আর্কিটেকচার সিদ্ধান্ত রেকর্ড বর্ণনা করে।

**ব্যবসায়িক শব্দ বাস্তবায়নে প্রভাব ফেললে ডকুমেন্টেশন সংস্করণ ব্যবহার করুন।** একটি উদাহরণ CSV ইম্পোর্টারে existing customer বলতে একই ইমেল, একই বাহ্যিক আইডি, নাকি দুটো বোঝায় তা ঠিক করুন। ডুপ্লিকেট শনাক্তকরণ লেখার আগে সংজ্ঞা লিখুন।

**সাক্ষাৎকারের আকার অনুপাতে রাখুন।** কার্যকর সেশন গুরুত্বপূর্ণ অনিশ্চয়তা দূর করে। রিপোজিটরিতে আগে থেকেই থাকা উত্তর আবার দিতে বলবেন না। পরিকল্পনা, অনিষ্পন্ন প্রশ্ন এবং দৃশ্যমান সমাপ্তি পরীক্ষায় শেষ করুন।

### Karpathy-অনুপ্রাণিত CLAUDE.md

**Multica-র নির্দেশিকা** Karpathy-র পর্যবেক্ষণকে চারটি বিষয়ে রূপ দেয়: স্পষ্ট অনুমান, সহজ সমাধান, সীমিত পরিবর্তন এবং যাচাইযোগ্য লক্ষ্য। [রিপোজিটরি](https://github.com/multica-ai/andrej-karpathy-skills) তাঁর পর্যবেক্ষণ থেকে অনুপ্রাণিত কমিউনিটি বাস্তবায়ন। প্রকল্পটিকে Karpathy-র ব্যক্তিগতভাবে রক্ষিত প্লাগইন বলা উৎস সম্পর্কে ভুল ধারণা দেয়।

**উপকারী নির্দেশনা বর্তমান প্রকল্প নীতিতে মেশান।** বিল্ড কমান্ড, কনটেন্ট নিয়ম এবং ডিপ্লয়মেন্ট সীমা রাখুন। সেগুলো বাদ দেওয়া নতুন নির্দেশনা ফাইল নতুন ভুলের উৎস তৈরি করে।

**প্রকল্প নিয়মের উদাহরণ:** ইম্পোর্টার পরিবর্তনে বর্তমান ডুপ্লিকেট হ্যান্ডলিং রাখতে হবে এবং fixture দিয়ে ইচ্ছাকৃত পরিবর্তন ব্যাখ্যা করতে হবে। সাধারণ সতর্কতার পছন্দকে এতে পর্যালোচকের বোঝার মতো পরীক্ষায় রূপ দেওয়া হয়। নির্দেশনা প্রত্যাশা প্রকাশ করে। পরীক্ষা ও রানটাইম নিয়ন্ত্রণ আলাদা প্রমাণ দেয়।

| পরিকল্পনার উপাদান | উদ্দেশ্য |
|---|---|
| **প্রয়োজন** | ব্যবহারকারীর দৃশ্যমান ফলের নাম দেয় |
| **শব্দকোষ এন্ট্রি** | বহুমুখী শব্দকে এক অর্থ দেয় |
| **সিদ্ধান্ত রেকর্ড** | গুরুত্বপূর্ণ সিদ্ধান্তের কারণ ধরে রাখে |
| **গ্রহণযোগ্যতা পরীক্ষা** | সমাপ্তি মূল্যায়নের পদ্ধতি নির্ধারণ করে |

## পরিকল্পনা ও কোড পর্যালোচনা করুন

### grill-me-codex, এখন Claudex Loop

**Claudex Loop** মূল grill-me-codex রিপোজিটরির বর্তমান গন্তব্য। [ডকুমেন্টেশন](https://github.com/chaseai-yt/claudex-loop) রিপোজিটরি অনুসন্ধান, প্রয়োজন, অন্য প্রদানকারীর পর্যালোচনা, বাস্তবায়ন এবং স্বাধীন পরিদর্শন বর্ণনা করে। পূর্ণ লুপের জন্য দুই CLI এবং Python 3.10 বা পরের সংস্করণ লাগে।

**গুরুত্বপূর্ণ পরিকল্পনায় Claudex Loop ব্যবহার করুন** যখন বাস্তবায়নের আগে অনুমানকে চ্যালেঞ্জ করা দরকার। বর্তমান কর্মপ্রবাহ Claude Code বা Codex থেকে শুরু করা যায়। এটি ফল ও সিদ্ধান্ত রেকর্ড করে এবং পর্যালোচনার অনুমতিকে বিল্ডের অনুমতি থেকে আলাদা রাখে। ভিডিওর পুরনো পাঁচ রাউন্ডের বিবরণ ইনস্টল করা কর্মপ্রবাহের বর্তমান সীমার বদলি নয়।

**প্রতিটি আপত্তির সঙ্গে প্রমাণ চান।** CSV ইম্পোর্টার পর্যালোচনায় নির্দিষ্ট ডুপ্লিকেট বা পুনরায় চেষ্টার ঘটনা এবং প্রত্যাশিত আচরণ দেখাতে হবে। মডেলের সম্মতি পর্যালোচনার ফল, প্রমাণ নয়। বাজেট শেষ হলে অনিষ্পন্ন ফল সংরক্ষণ করুন।

### OpenAI Codex প্লাগইন

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**Claude Code-এর জন্য OpenAI Codex প্লাগইন** Claude Code-এর মধ্যে কোড পর্যালোচনা ও টাস্ক ডেলিগেশন যোগ করে। এগুলো Claude Code কমান্ড, shell কমান্ড নয়। [অফিশিয়াল রিপোজিটরি](https://github.com/openai/codex-plugin-cc) Node.js 18.18 বা পরের সংস্করণ এবং ChatGPT বা OpenAI API key দিয়ে প্রমাণীকৃত Codex অ্যাক্সেস বর্ণনা করে।

```text
/codex:review --background
/codex:status
/codex:result
```

**বর্তমান পরিবর্তন বা শাখা তুলনায় সাধারণ পর্যালোচনা ব্যবহার করুন।** নির্দিষ্ট চ্যালেঞ্জের জন্য **`/codex:adversarial-review`** ব্যবহার করুন। **`/codex:rescue`**-এর মতো ডেলিগেশন কমান্ড read-only পর্যালোচনা থেকে আলাদা কাজ করে, তাই কাঙ্ক্ষিত কর্তৃত্ব লিখুন।

**Codex ব্যবহারের আলাদা বাজেট রাখুন।** প্রকল্পটি ChatGPT Free-কে সমর্থিত অ্যাকাউন্টে রাখে, কিন্তু ব্যবহারের সীমা থাকে। প্লাগইন ইনস্টল করলে সীমাহীন অ্যাক্সেস তৈরি হয় না।

**বাছাইয়ের নিয়ম:** বিদ্যমান patch-এর জন্য সীমিত প্লাগইন পর্যালোচনা নিন। প্রয়োজন ও পরিকল্পনা সংশোধনের নিজস্ব নথিবদ্ধ প্রক্রিয়া দরকার হলে বড় লুপ নিন।

## দরকারী প্রসঙ্গ ধরে রাখুন

### Graphify

```bash
uv tool install graphifyy
graphify install --project
graphify extract . --code-only
graphify query "show the authentication flow"
```

**Graphify** রিপোজিটরির সম্পর্ককে query করা যায় এমন knowledge graph-এ ম্যাপ করে। [ক্যানোনিক্যাল রিপোজিটরি](https://github.com/Graphify-Labs/graphify) এখন Graphify-Labs-এর অধীনে। প্যাকেজের নাম শেষে দুইটি y সহ **`graphifyy`**। এক্সিকিউটেবল **`graphify`**-ই থাকে।

**Code-only extraction** স্থানীয় abstract syntax tree parsing ব্যবহার করে এবং কোডের গঠন পড়ে। ডকুমেন্ট ও মিডিয়া ব্যাখ্যার আলাদা model-backed পথ আছে। সব মোডে স্থানীয় গোপনীয়তা বা খরচের দাবি প্রয়োগ করবেন না।

**ঐচ্ছিক hook** commit ও branch switch-এর পরে code graph পুনর্নির্মাণ করে। pull বা merge-এর পরে নথিবদ্ধ কর্মপ্রবাহ **`graphify update .`** চালায়। ডকুমেন্ট পরিবর্তনের আলাদা refresh দরকার। Obsidian export graph-এর আরেকটি দৃশ্য দেয়।

**সম্পর্কের প্রশ্নে Graphify ব্যবহার করুন,** তারপর প্রাসঙ্গিক source পরীক্ষা করুন। graph ফাইল বাছতে সাহায্য করে। graph structure রানটাইম আচরণ প্রমাণ করে না এবং test-এর বদলি নয়। graph তৈরি ও রক্ষণাবেক্ষণসহ নিজের প্রশ্নে token সাশ্রয় মাপুন।

### claude-obsidian

**claude-obsidian** source-linked, source-cited Obsidian পৃষ্ঠায় উৎস উপাদান সাজায়। [রিপোজিটরি](https://github.com/AgriciDaniel/claude-obsidian) ingestion, retrieval, knowledge maintenance, source retention এবং support বা contradiction-এর record বর্ণনা করে। vault সাধারণ স্থানীয় ফাইলই থাকে।

**স্থায়ী প্রকল্প জ্ঞানের জন্য claude-obsidian ব্যবহার করুন:** নকশা সিদ্ধান্ত, উৎস ডকুমেন্ট এবং গবেষণা নোট যা আলাদা কথোপকথনের পরেও দরকার। উপকারী ফল হলো provenance-সহ রক্ষণযোগ্য record, অর্থাৎ গুরুত্বপূর্ণ দাবির অনুসরণযোগ্য উৎস।

**ingestion-এর পরে vault পর্যালোচনা করুন।** কয়েকটি দাবি নিয়ে citation অনুসরণ করে মূল উপাদানে যান। বিরোধী প্রমাণকে আত্মবিশ্বাসী সারাংশে মেশাবেন না। স্থানীয় storage নিজে local inference প্রমাণ করে না। সংবেদনশীল ডকুমেন্ট দেওয়ার আগে host ও model configuration পরীক্ষা করুন।

| প্রসঙ্গ ব্যবস্থা | প্রথম প্রশ্ন |
|---|---|
| **Graphify** | কোন source component যুক্ত? |
| **claude-obsidian** | কোন সংরক্ষিত প্রমাণ সিদ্ধান্তটিকে সমর্থন করে? |
| **notebooklm-py** | নির্বাচিত গবেষণা উৎসগুলো কী বলে? |

### notebooklm-py

```bash
uv tool install "notebooklm-py[browser]"
notebooklm login
notebooklm auth check --test --json
notebooklm skill install
```

**notebooklm-py** Google-এর notebook research service-এর জন্য Python library, CLI এবং agent skill দেয়। [প্রকল্প](https://github.com/teng-lin/notebooklm-py) source import, grounded question, generated artifact এবং batch download নথিবদ্ধ করে। browser extra interactive login flow সমর্থন করে।

**এটি unofficial integration।** library undocumented Google interface-এর ওপর নির্ভর করে এবং ভাঙন ও rate limit-এর অধীন। এটিকে Google-সমর্থিত public API বলবেন না।

**সীমিত research corpus-এর জন্য notebooklm-py ব্যবহার করুন,** যেমন একটি dependency-র release note ও migration guide। plan-এ ফল যোগের আগে source text দিয়ে citation পরীক্ষা করুন। সংরক্ষিত authentication state-কে account access material হিসেবে সুরক্ষিত রাখুন।

**Research offloading কাজের স্থান বদলায়।** এতে orchestration token, service quota, review effort বা data-handling obligation দূর হয় না। token saving-কে installation-এর স্বয়ংক্রিয় বৈশিষ্ট্য নয়, মাপার বিষয় হিসেবে ধরুন।

## সম্পদ ডিজাইন ও তৈরি করুন

### Impeccable

```text
/impeccable critique settings
/impeccable audit settings
/impeccable polish settings
```

**Impeccable** focused interface work-এর জন্য design vocabulary দেয়। [Documentation](https://github.com/pbakaus/impeccable)-এ critique, layout, typography, accessibility check, motion এবং browser-based visual iteration আছে। উদাহরণে installed skill ও settings surface-সহ project ধরা হয়েছে।

**Interaction problem দিয়ে শুরু করুন।** ইম্পোর্টারে ব্যবহারকারীরা কেন validation error মিস করে বা duplicate handling পছন্দ ভুল বোঝে তা জিজ্ঞেস করুন। visual polish-এর আগে proposed change review করুন। সুন্দর spacing একা অস্পষ্ট action ঠিক করে না।

**Live iteration** browser-এ বিকল্প তুলনা করতে সাহায্য করে। keyboard navigation, mobile layout, error message এবং contrast যাচাই করুন। release অনুযায়ী command count বদলায়, তাই ভিডিওর সংখ্যা মনে না রেখে installed version-এর command list ব্যবহার করুন।

### Higgsfield

**Higgsfield-এর MCP integration** agent-কে image ও video generation service-এর সঙ্গে যুক্ত করে। [Official integration page](https://higgsfield.ai/mcp)-এ Claude Code ও CLI connection option এবং creative workflow আছে। account ও interface অনুযায়ী current setup flow ব্যবহার করুন।

**Missing deliverable media হলে Higgsfield বেছে নিন।** illustrative product page-এর জন্য variant তৈরির আগে aspect ratio, composition, brand constraint এবং placement লিখুন। visual brief-কে page implementation task থেকে আলাদা রাখুন।

**আগে service access ও consumption পরীক্ষা করুন।** integration listing সব model-এ access, unlimited generation বা নির্দিষ্ট commercial usage right প্রমাণ করে না। production workflow নেওয়ার আগে account terms ও selected model দেখুন।

**Final file** intended display size-এ review করুন। visible text, unintended symbol, crop এবং product consistency পরীক্ষা করুন। generated terminal screen বা diagram সফল test-এর evidence নয়।

| Design deliverable | Completion evidence |
|---|---|
| **Interface revision** | target viewport-এ প্রয়োজনীয় action কাজ করে |
| **Image asset** | dimension, crop এবং content brief-এর সঙ্গে মেলে |
| **Video asset** | timing, motion এবং final export brief-এর সঙ্গে মেলে |

## পুনরাবৃত্তিযোগ্য কর্মপ্রবাহ যুক্ত করুন

### n8n MCP

**n8n-এর built-in MCP server** connected client-কে workflow operation দেয়। [Current connection documentation](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)-এ Cloud ও self-hosted instance আছে। n8n 2.13.0 থেকে workflow build ও edit নথিবদ্ধ। এই নিবন্ধ n8n-এর নিজস্ব server নিয়ে, একই নামের unrelated community package নিয়ে নয়।

**এখানে instance-level access ব্যবহার করুন।** MCP Server Trigger node-এর scope আলাদা, এটি একটি workflow-এর tool প্রকাশ করে। [Tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) deployed version-এর সঙ্গে মিলিয়ে দেখুন।

**ইচ্ছাকৃতভাবে access enable করুন।** full access-এর জন্য existing workflow-এ MCP exposure দরকার। search preview ব্যবহারকারীর existing permission-এর মধ্যে বিস্তৃত visibility দেয়। workflow exposure client-পিছু আলাদা allowlist নয়, যদিও client permission operation নিয়ন্ত্রণ করে।

**Execution mode পরীক্ষা করুন।** documentation অনুযায়ী **`execute_workflow`** default-এ published production version চালায়। manual mode current unpublished version চালায়। execution-এর আগে input ও downstream action যাচাই করুন।

**ভালো প্রথম পরীক্ষা:** synthetic support request classify করে test destination-এ ফল লিখুন। missing field ও retry workflow সামলায় কি না দেখুন। self-hosting-এ compute, maintenance ও paid downstream service লাগে।

## নিয়ন্ত্রিত পরীক্ষা চালান

**Illustrative exercise:** ছোট application-এ CSV importer যোগ করুন। importer row preview, invalid email field report এবং duplicate creation প্রতিরোধ করবে। customer record বা live external destination লাগবে না।

```yaml
# Evaluation worksheet, not a tool configuration file
task: "add CSV import preview"
inputs:
  - "valid rows"
  - "invalid email field"
  - "repeated customer identifier"
  - "same import submitted twice"
acceptance:
  - "preview creates no records"
  - "invalid rows receive useful messages"
  - "duplicate policy matches the written requirement"
  - "repeat submission creates no extra records"
record:
  - "source revision and selected skill version"
  - "model and service configuration"
  - "elapsed time and billed usage"
  - "failed checks and human corrections"
```

**আগে baseline স্থাপন করুন।** starting revision সংরক্ষণ করে existing workflow দিয়ে agent-কে task শেষ করতে বলুন। independent acceptance check চালিয়ে result রাখুন। একই starting revision, requirement এবং একটি extension দিয়ে আবার চালান।

**পরীক্ষাকে অনুমান করা সমস্যার সঙ্গে মিলান।** duplicate handling বারবার ভুল হলে requirements skill পরীক্ষা করুন। existing validator বাদ পড়লে repository mapping পরীক্ষা করুন। user error মিস করলে interface critique পরীক্ষা করুন। দশটি tool একসঙ্গে load করলে improvement-এর কারণ বোঝা যায় না।

**প্রত্যাশিত reasoning:** দ্বিতীয় সফল চেষ্টা উপকারী evidence, কিন্তু এক run সাধারণ productivity multiplier প্রমাণ করে না। repeated run tool value ও model variability আলাদা করতে সাহায্য করে। accepted result, review effort এবং failed attempt একসঙ্গে তুলনা করুন।

| Observation | Interpretation |
|---|---|
| **Faster answer, failed tests** | task completion ছাড়া কম response time |
| **Longer run, fewer corrections** | total delivery effort-এ সম্ভাব্য লাভ |
| **Two agreeing reviewers** | independent verification দরকার |
| **Lower agent usage, new service charges** | provider-এর মধ্যে cost স্থানান্তর |

**Retained decision record তৈরি করুন।** problem, selected tool, observed benefit, unresolved issue এবং next trial condition লিখুন। এই পরীক্ষা টিকলে tool রাখুন। বড় installed collection বড় active workflow বাধ্য করে না।

## সমস্যা সমাধান

| লক্ষণ | পরের পরীক্ষা |
|---|---|
| **স্কিল আছে কিন্তু কমান্ড ব্যর্থ** | executable installation, PATH এবং sidecar file |
| **পুরনো tutorial-এ command নেই** | installed version ও canonical upstream instruction |
| **graph সাম্প্রতিক change বাদ দেয়** | graph freshness ও আলাদা document refresh |
| **reviewer resolved objection আবার বলে** | exact plan revision, evidence ও review budget |
| **Notebook authentication ব্যর্থ** | auth diagnostic, session validity ও upstream issue |
| **n8n connection-এ operation নেই** | deployed version, exposure setting ও granted permission |
| **design ভালো দেখায় কিন্তু খারাপ কাজ করে** | original acceptance criteria ও interaction check |

**Installation layer ক্রমে পরীক্ষা করুন:** file present, host discovery, dependency ready, authentication এবং representative task। সফল installer এই chain-এর কেবল একটি অংশ প্রমাণ করে।

**আরেকটি copy যোগের আগে overlapping skill পরীক্ষা করুন।** requirements interview, planning suite, design tool ও review package পরস্পরবিরোধী default দিতে পারে। কাজের জন্য একটি primary procedure নিন এবং named contribution-এর জন্য supporting tool যোগ করুন। repository policy ও user scope রাখুন।

## ভিডিও নির্দেশনা

{{< youtube id="IShdbDP4Jgg" enable="true" title="The Top 10 Claude Code Plugins to 10x Your Next Project (June '26)" >}}

**Chase AI-এর walkthrough** এখানে আলোচিত দশটি project পরিচয় করায়। demonstration-এর জন্য [মূল ভিডিও দেখুন](https://www.youtube.com/watch?v=IShdbDP4Jgg)। current installation ও behavior-এর জন্য linked project documentation ব্যবহার করুন। ভিডিওর title promotional claim, এই guide-এর প্রতিষ্ঠিত measured result নয়।

## পরবর্তী ধাপ

**একটি recurring failure ও একটি acceptance test বেছে নিন।** disposable project-এ matching extension পরীক্ষা করুন। তারপর ফল উন্নত করা সবচেয়ে ছোট combination রাখুন। কাজের output দরকার হলেই knowledge management, media generation বা automation যোগ করুন।

**সম্পর্কিত নির্দেশনার জন্য**, agent বাছার সময় [CLI coding-agent comparison](/articles/cli-coding-agents-comparison/) পড়ুন। requirements, evidence ও review responsibility-র ব্যবহারিক কাজের জন্য [AI collaboration course](/ai-collaboration-course-start/) ব্যবহার করুন।

{{< centerbutton href="/ai-collaboration-course-start/" >}}
AI Collaboration Course পড়ুন
{{< /centerbutton >}}

## রেফারেন্স

- [Graphify: code graphs and installation](https://github.com/Graphify-Labs/graphify)
- [Matt Pocock: skill collection](https://github.com/mattpocock/skills)
- [Claudex Loop: current grill-me-codex project](https://github.com/chaseai-yt/claudex-loop)
- [OpenAI: Codex plugin for Claude Code](https://github.com/openai/codex-plugin-cc)
- [claude-obsidian: source-linked knowledge management](https://github.com/AgriciDaniel/claude-obsidian)
- [Multica: Karpathy-inspired coding guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
- [Impeccable: design commands and installation](https://github.com/pbakaus/impeccable)
- [Higgsfield: agent integration](https://higgsfield.ai/mcp)
- [notebooklm-py: unofficial library, CLI, and skill](https://github.com/teng-lin/notebooklm-py)
- [n8n: official MCP connection guide](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
