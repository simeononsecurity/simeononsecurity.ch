---
title: "GitHub Copilot CLI বনাম VS Code: ২০২৬ কর্মপ্রবাহের তুলনা"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Copilot-এর টার্মিনাল এজেন্টের সঙ্গে VS Code অভিজ্ঞতা তুলনা করুন। এতে এডিটর প্রসঙ্গ, ভিজ্যুয়াল ডিফ, Agent মোড, CLI সংযোগ এবং অ্যাকাউন্ট নীতি রয়েছে।"
genre: ["ডেভেলপার টুল", "কৃত্রিম বুদ্ধিমত্তা", "সফটওয়্যার ডেভেলপমেন্ট"]
tags: ["GitHub Copilot CLI বনাম VS Code", "Copilot CLI", "GitHub Copilot", "VS Code", "Agent মোড", "CLI বনাম GUI", "এডিটর প্রসঙ্গ", "ইনলাইন সাজেশন", "ভিজ্যুয়াল ডিফ", "Copilot সেশন", "টার্মিনাল এজেন্ট", "GitHub কর্মপ্রবাহ", "কোড রিভিউ", "IDE ইন্টিগ্রেশন", "MCP টুল", "এজেন্ট অনুমতি", "AI Credits", "ডেভেলপার টুল", "কোডিং সহকারী", "অটোমেশন"]
cover: "/img/cover/github-copilot-cli-vs-vscode.webp"
coverAlt: "নীল ও সবুজ কোডিং কর্মক্ষেত্রে এডিটর নির্বাচনের সঙ্গে যুক্ত টার্মিনাল প্রম্পট এবং ভিজ্যুয়াল ডিফ"
coverCaption: ""
---

**GitHub Copilot CLI এবং VS Code-এর Copilot কোডিং কাজের জন্য আলাদা প্রবেশপথ দেয়।** CLI শুরু হয় shell ও কাজের প্রম্পট দিয়ে। VS Code এডিটর প্রসঙ্গ, সাজেশন, চ্যাট ও এজেন্ট কর্মপ্রবাহ একত্র করে। একই অ্যাকাউন্ট ও রিপোজিটরি নীতির অধীনে দুটিই মূল্যায়ন করুন।

**পছন্দটি একচেটিয়া নয়।** GitHub Copilot CLI এবং VS Code-এর সংযোগ নথিভুক্ত করেছে। স্পষ্টভাবে সংযোগ করলে টার্মিনাল কাজ এডিটর নির্বাচন ও ভিজ্যুয়াল রিভিউ থেকে সুবিধা পায়।

## মূল বিষয়

- **টার্মিনাল-ভিত্তিক কাজের জন্য Copilot CLI ব্যবহার করুন** এবং সমর্থিত প্রোগ্রামেটিক কল চালান।
- **এডিটর-কেন্দ্রিক কাজের জন্য VS Code-এ Copilot ব্যবহার করুন**, ইনলাইন সহায়তা ও Agent মোডসহ।
- **CLI-কে VS Code-এর সঙ্গে সংযোগ করুন** যখন টার্মিনাল প্রম্পটে এডিটর প্রসঙ্গ ও ডিফ দরকার।
- **অ্যাকাউন্ট, মডেল ও নীতি যাচাই করুন**, একই পণ্য পরিবারের মধ্যেও।

**পরিধি ও তারিখ:** ১০ অক্টোবর ২০২৬-এ অফিসিয়াল নথি পরীক্ষা করা হয়েছে। এই তুলনায় স্বতন্ত্র `copilot` CLI এবং VS Code-এর Copilot আছে। পুরনো `gh copilot` এক্সটেনশন বা GitHub issue-তে দেওয়া cloud agent নেই। পরীক্ষাযোগ্য রিপোজিটরি ও অনুমোদিত Copilot অ্যাক্সেস দরকার। পরীক্ষার জন্য এক ঘণ্টা রাখুন।

## কাজের তিন পদ্ধতি

| কর্মপ্রবাহ | প্রধান ইন্টার‌্যাকশন | উপযুক্ত পরীক্ষার কাজ |
|---|---|---|
| **স্বতন্ত্র CLI** | টার্মিনাল প্রম্পট ও কমান্ড আউটপুট | পুনরুৎপাদিত টেস্ট ব্যর্থতা ব্যাখ্যা ও ঠিক করা |
| **VS Code সংযোগ** | এডিটর নির্বাচন, চ্যাট, সাজেশন ও ডিফ | নির্বাচিত ফাংশন ও তার টেস্ট বদলানো |
| **VS Code-এ যুক্ত CLI** | এডিটর প্রসঙ্গ ও রিভিউসহ টার্মিনাল কাজ | shell থেকে তদন্ত করে প্যাচ দেখা |

**হাইব্রিড পদ্ধতিও CLI সেশন।** ইন্টিগ্রেটেড টার্মিনালে চালালেই এটি এডিটরের native Agent-mode কথোপকথন হয় না। সক্রিয় সেশন ও সংযোগ পরীক্ষা করুন।

## CLI কী দেয়

```bash
copilot
```

**বর্তমান স্বতন্ত্র কমান্ড টার্মিনাল এজেন্ট চালু করে।** GitHub-এর [Copilot CLI overview](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli) ইন্টার‌্যাক্টিভ ও প্রোগ্রামেটিক ব্যবহার, পরিকল্পনা এবং টুল অনুমতি বর্ণনা করে। টার্মিনাল আউটপুট প্রধান প্রমাণ হলে এখানে পরীক্ষা করুন।

**ভালো প্রথম কাজে নির্দিষ্ট ব্যর্থতা থাকে।** ব্যর্থ কমান্ড, প্রত্যাশিত আচরণ এবং সম্পর্কহীন refactoring নিষেধের সীমা দিন। ফাইল বদলানোর আগে সমস্যা পুনরুৎপাদন করতে বলুন এবং চূড়ান্ত ব্যাখ্যা টেস্ট আউটপুটের সঙ্গে মিলিয়ে দেখুন।

**অটোমেশনে স্পষ্ট সীমা দরকার।** বর্তমান invocation ও নিয়ন্ত্রণের জন্য [CLI ব্যবহার নির্দেশিকা](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli) ব্যবহার করুন। unattended কাজের আগে অনুমোদিত টুল, সময়সীমা ও আউটপুট ব্যবস্থা নির্ধারণ করুন। ইন্টার‌্যাক্টিভ অনুমতিকে pipeline-এর পূর্ণ অনুমতিতে বদলাবেন না।

**Sandbox পরীক্ষার সীমা বদলায়।** GitHub ফাইল সিস্টেম, নেটওয়ার্ক ও সিস্টেমের জন্য local sandbox এবং বিচ্ছিন্ন execution-এর জন্য cloud sandbox বর্ণনা করে। আসল রিপোজিটরি বদলানোর আগে harmless fixture দিয়ে sandbox, নেটওয়ার্ক ও write scope পরীক্ষা করুন।

## VS Code কী যোগ করে

**IDE-তে Copilot-এর অভিজ্ঞতায় সাজেশন, চ্যাট ও agent task রয়েছে।** [IDE overview](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides) ফাংশনগুলো আলাদা করে। আপনি প্রধান editor থাকলে inline সহায়তা উপযোগী। একাধিক ফাইলে সীমিত পরিবর্তনের ফলের জন্য Agent মোড উপযোগী।

**Agent মোড বারবার edit ও command চালায়।** [Agent-mode guide](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode) chat-এ Agent বাছাই, পরিবর্তন দেখা ও MCP দিয়ে টুল বাড়ানো বর্ণনা করে। উপলভ্যতা configuration ও administration-এর ওপরও নির্ভর করে।

**Context transfer পরিকল্পিতভাবে পরীক্ষা করুন।** একটি function বেছে error handling ব্যাখ্যা চাইুন। তারপর স্বাধীন test-সহ ছোট পরিবর্তন চাইুন। পাশের ফাইল দেওয়া দরকার হয়েছে কি না এবং agent-এর অনুমান ঠিক করতে হয়েছে কি না লিখুন।

{{< figure src="copilot-terminal-editor-bridge.webp" alt="একটি রিপোজিটরি workspace-এ এডিটর নির্বাচনের সঙ্গে যুক্ত টার্মিনাল প্রম্পট এবং পাশাপাশি কোড ডিফ" caption="যুক্ত CLI সেশন টার্মিনাল ইনপুট ও এডিটর রিভিউ একত্র করে" >}}

## দুটি ইন্টারফেস যুক্ত করুন

```text
/ide
```

**ইন্টার‌্যাক্টিভ Copilot CLI সেশনে `/ide` ব্যবহার করুন** VS Code সংযোগ পরীক্ষা বা বদলাতে। [সংযোগ নির্দেশিকা](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code) trusted workspace মিল, editor selection ভাগ করা এবং প্রস্তাবিত edit-কে diff হিসেবে দেখানো বর্ণনা করে।

**Automatic connection workspace মিলের ওপর নির্ভর করে।** শুধু repository name এক হলেই local CLI remote Codespace-এ যুক্ত হয় না। একই environment-এ CLI চালান। বিস্তৃত edit authorization প্রস্তাবিত diff approval এড়িয়ে যায়। প্রত্যাশিত prompt না এলে permission দেখুন।

**CLI transcript VS Code-এর Sessions view-তে দেখা যায়**, Resume in Terminal দিয়ে চালিয়ে যাওয়া যায়। এতে terminal workflow থাকে, কিন্তু কথোপকথন native editor-agent session হয়ে যায় না।

| সংযোগের আগে | যাচাই |
|---|---|
| **Workspace** | নির্দিষ্ট folder খোলা ও trusted |
| **Execution location** | CLI ও editor integration একই environment নির্দেশ করে |
| **Selection** | হাইলাইট করা code বর্তমান অনুরোধের সঙ্গে মেলে |
| **Permissions** | প্রয়োজন হলে proposed-edit review চালু থাকে |
| **Session** | নির্দিষ্ট conversation চলতে থাকে |

## Model, billing ও policy

**সম্ভব হলে দুই interface trial-এ একই model ব্যবহার করুন।** পার্থক্য থাকলে লিখে রাখুন। Model, context বা tool set বদলালে পরীক্ষা graphics-versus-terminal তুলনার বাইরে যায়।

**অ্যাকাউন্টের বর্তমান usage accounting যাচাই করুন।** GitHub-এর Agent-mode documentation AI Credits উল্লেখ করে। billing arrangement না দেখে পুরনো premium-request estimate ব্যবহার করবেন না। CLI prompt ও editor task স্বয়ংক্রিয়ভাবে একই work unit নয়।

**Organization access দরকার।** Feature না থাকলে extension reinstall-এর আগে policy দেখুন। দুই surface-এর অনুমোদিত tools ও integrations লিখুন। Provider login সব repository বদলানো বা সব external service-এ যোগাযোগের অনুমতি দেয় না।

## জোড়া পরীক্ষা চালান

**একই starting revision-এর দুই কপি তৈরি করুন।** একই instructions ও acceptance tests ব্যবহার করুন। প্রথমটি standalone CLI-তে, দ্বিতীয়টি VS Code Agent mode-এ চালান। আপনার কাজে মানানসই হলে connected CLI দিয়ে তৃতীয়টি চালান।

| মাপ | কেন লিখবেন |
|---|---|
| **দেওয়া context** | লুকানো manual setup effort দেখায় |
| **সঠিকতা** | plausible code ও verified fix আলাদা করে |
| **Approval steps** | একই policy-তে supervision burden দেখায় |
| **Review time** | পুরো patch বোঝার সময় মাপে |
| **Manual repairs** | agent শেষ করার পরের কাজ ধরে |
| **Usage** | cost ও accepted outcome যুক্ত করে |

**Recovery পরীক্ষার অংশ রাখুন।** একটি প্রস্তাবিত পদ্ধতি প্রত্যাখ্যান করে কারণ বলুন। পরের চেষ্টা useful কাজ রাখে এবং correction মানে কি না দেখুন। এটি একটিমাত্র uninterrupted demo-এর চেয়ে দৈনিক ব্যবহার ভালো দেখায়।

## সমস্যা সমাধান ও পরবর্তী ধাপ

**CLI ভুল editor window-এ যুক্ত হলে**, `/ide` পরীক্ষা করে সঠিক workspace বাছুন। visual approval বন্ধ হলে broad edit permission দেখুন। Agent mode না থাকলে extension state ও organization policy দেখুন।

**Standalone CLI বাছুন** যখন shell context ও repeatable invocation প্রধান। **VS Code বাছুন** যখন selection context, inline কাজ ও graphical review প্রধান। **Connected CLI ব্যবহার করুন** যখন terminal entry ও editor inspection একসঙ্গে ভালো কাজ করে।

**Vendor তুলনার জন্য** [CLI master comparison](/articles/cli-coding-agents-comparison/) বা [GUI master comparison](/articles/gui-coding-agents-comparison/) পড়ুন। একই product family-এর এই interface trial থেকে সেগুলো আলাদা রাখুন।
