---
title: "নন-কোডারদের জন্য GitHub AI ওয়ার্কফ্লো: Issues এবং Pull Requests"
date: 2026-10-01
lastmod: 2026-11-14
toc: true
draft: false
description: "স্থানীয় ডেভেলপমেন্ট পরিবেশ ছাড়াই ব্রাউজার সম্পাদনা, Issues, চ্যাট কনটেক্সট প্যাকেট এবং পর্যালোচিত pull requests ব্যবহার করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "দলগত সহযোগিতা", "সফটওয়্যার ইঞ্জিনিয়ারিং"]
tags: ["AI সহযোগিতা কোর্স", "GitHub ব্রাউজার সম্পাদনা", "GitHub Issues", "পুল রিকোয়েস্ট", "নন-কোডিং অবদানকারী", "কনটেক্সট প্যাকেট", "রিভিউ হ্যান্ডঅফ"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "সাইবার নিরাপত্তা কর্মক্ষেত্রে যৌথ প্রকল্প পর্যালোচনা করা পেশাজীবীদের চিত্র"
coverCaption: ""
---

[AI সহযোগিতা কোর্সে ফিরে যান](/ai-collaboration-course-start/)

**নন-কোডিং অবদানকারীরা ব্রাউজারেও একই কর্তৃত্বের নিয়ম ব্যবহার করেন।** আপনি GitHub-এর উৎস পড়েন, অনুমোদিত চ্যাট টুল দিয়ে খসড়া তৈরি করেন এবং একটি Issue বা branch edit জমা দেন। Maintainer পরীক্ষা চালিয়ে review-এর পর প্রকাশ করেন। Repository protection সক্রিয় হওয়ার পর এই workflow ব্যবহার করুন, যাতে ব্রাউজার access coding-agent নিয়ন্ত্রণ এড়িয়ে না যায়।

## মূল বিষয়

- **ব্রাউজার কাজের** জন্য স্থানীয় terminal লাগে না।
- **Context packet** scope এবং revision evidence ধরে রাখে।
- **Issues এবং branches** প্রস্তাব হিসেবেই থাকে।
- **Handoff** বাকি কাজ এবং পরের ভূমিকা চিহ্নিত করে।

## শুরু করার আগে

**প্রয়োজনীয়তা:** [রিপোজিটরি সীমার পাঠ](/articles/ai-collaboration-github-repository/), lab read access এবং প্রয়োজনে অনুমোদিত chat tool। **সময়:** 45 থেকে 60 মিনিট। **কঠিনতা:** প্রাথমিক। শুধু Issue ব্যবহারকারী contributors স্থানীয় Git এবং Actions বাদ দেন। PR জমা দেওয়া contributors [এজেন্ট ও Actions পাঠ](/articles/ai-collaboration-github-agents-actions/) শেষ করা maintainer-এর সঙ্গে সমন্বয় করেন।

**Connector-বিহীন ভিত্তি:** নিজে GitHub খুলুন এবং শুধু synthetic excerpt দিন। কোনো chat subscription feature ধরে নেওয়া হয় না। কোনো provider অনুমোদিত না হলে একই record ব্যবহার করে হাতে খসড়া লিখুন।

**সমাপ্তির ফল:** fixed source revision, proposed wording, affected files, exclusions এবং unresolved questions-সহ একটি Issue বা PR hand off করবেন।

## উৎস-প্যাকেট পড়ুন

1. **`main`-এ MAP-01 খুলুন**, তারপর POL-01, REQ-17 এবং RUN-04 খুঁজুন।
2. **প্রতিটি source পড়ুন** এবং browser-এর commit view থেকে commit revision লিখে রাখুন।
3. **প্রাসঙ্গিক synthetic section কপি করুন** filename, revision, scope এবং exception-সহ।
4. **Packet-কে snapshot-based হিসেবে চিহ্নিত করুন**, যতক্ষণ না publication-এর আগে maintainer current source-এর সঙ্গে তুলনা করেন।

```text
প্রকল্প: export-service-lab
কাজ: PROP-042-এর খসড়া, প্রকাশের অনুমতি নেই
অনুমোদিত কর্তৃত্ব: requirement.json, REQ-17 revision 1
ভিত্তিমূল্য: retention_days 7
নীতি: POL-01 সংস্করণ 1
প্রস্তাবিত অনুরোধ: retention_days 30
প্রমাণ: browser-এ যাচাইকৃত commit-এর রেফারেন্স সংযুক্ত করুন
অনুপস্থিত প্রমাণ: runtime-এ মুছে ফেলার পর্যবেক্ষণ নেই
আউটপুট: প্রস্তাবিত ভাষ্য, প্রভাবিত ফাইল, প্রশ্ন, পূর্বাবস্থায় ফেরানোর পরিকল্পনা
থামুন: উৎস অনুপলব্ধ, রিভিশন পরিবর্তিত, কর্তৃত্বে দ্বন্দ্ব
```

**আসল sandbox revision ব্যক্তিগতভাবে যুক্ত করুন।** Template-এ সম্পূর্ণ evidence নেই। Publication সুপারিশের আগে assistant-কে missing record চিহ্নিত করতে বলুন।

**Live source পড়ার আগে পূর্ণ synthetic packet:**

```text
প্রকল্প: export-service-lab
কাজ: Issue-এ PROP-042-এর খসড়া তৈরি করুন
অনুমোদিত ভিত্তিমূল্য: REQ-17 রিভিশন 1, retention_days 7
প্রস্তাব: retention_days 30, শুধু কৃত্রিম এক্সপোর্ট ফাইলের জন্য
প্রভাবিত রেকর্ড: requirement.json, config.json, proposal.json, runbook.md
বাদ: উৎপাদনের তথ্য, ব্যাকআপ ও আইনি সংরক্ষিত উপাদান
জানা প্রমাণ: সরবরাহ করা ল্যাবের ভিত্তিমূল ফাইল
অনুপস্থিত প্রমাণ: বর্তমান main commit, মালিকের সিদ্ধান্ত, runtime-এ মুছে ফেলার ফল
অবস্থা: খসড়া; বর্তমান রিভিশন ও পর্যালোচনা সম্পন্ন না হওয়া পর্যন্ত প্রকাশনা বন্ধ
পরবর্তী ভূমিকা: রক্ষণাবেক্ষণকারী যাচাইকৃত main commit দেবেন এবং যাচাই চালাবেন
```

**এটি একটি সম্পূর্ণ draft request।** Missing-evidence line ইচ্ছাকৃত। Publication চাওয়ার আগে supplied lab baseline-এর বদলে live sandbox revision দিন।

## একটি ইস্যু খুলুন

**Issues, New issue নির্বাচন করুন** এবং **`PROP-042: propose thirty-day synthetic retention`** title ব্যবহার করুন। এই description paste করে source packet যুক্ত করুন।

```text
প্রস্তাব: PROP-042
অবস্থা: খসড়া
বর্তমান অনুমোদিত মান: 7 দিন, REQ-17 রিভিশন 1
অনুরোধকৃত মান: 30 দিন
কারণ: কাল্পনিক পাইলট প্রকল্পের প্রয়োজন, নিয়ম-অনুবর্তিতা সংক্রান্ত পরামর্শ নয়
পরিধি: শুধু কৃত্রিম এক্সপোর্ট রেকর্ড
প্রভাবিত ফাইল: requirement.json, config.json, runbook.md
প্রমাণ: উৎসের রিভিশন ও নীতির সংস্করণ সংযুক্ত
পর্যালোচক: পণ্য-মালিক এবং কার্যক্রম-মালিক
বাস্তবায়ন পর্যালোচক: রিপোজিটরি রক্ষণাবেক্ষণকারী
গ্রহণযোগ্যতা: সামঞ্জস্যপূর্ণ রেকর্ড, প্রকাশনা প্রত্যাখ্যান, হালনাগাদ হস্তান্তর
পূর্বাবস্থায় ফেরানো: পর্যালোচনার পর অনুমোদিত ভিত্তিমূল পুনরুদ্ধার
```

**Chat-কে packet-এর সঙ্গে proposal তুলনা করতে বলুন**, assumption তালিকাভুক্ত করতে এবং owner question-এর draft লিখতে বলুন। Draft-টি Issue-এ সংরক্ষণ করুন। Approval বা publication চাইবেন না এবং chat thread-কে decision register ভাববেন না।

## ব্রাউজারে সম্পাদনা জমা দিন

1. **Repository-এর Code tab খুলুন।** File list-এর ওপর branch menu বেছে **`main`** নিশ্চিত করুন, **`proposal-042`** লিখুন এবং **Create branch: proposal-042 from main** নির্বাচন করুন। Branch তৈরি না হলে approved fork বা নিচের Issue route ব্যবহার করুন।
2. **Branch menu-তে `proposal-042` নিশ্চিত করুন** এবং তারপর file খুলুন। File ও pencil icon বেছে edit করুন। GitHub web editor protected branch edit করে না।
3. **Requirement edit করে** thirty days এবং revision 2 দিন। প্রতিটি পরের edit-এর আগে branch menu আবার খুলুন। একই branch-এ configuration এবং runbook edit করুন।
4. **`proposal.json` edit করে** to_days 30, from_days 7 এবং base_revision 1 দিন।
5. **Markdown preview করুন** এবং JSON punctuation দেখুন। প্রতিটি browser edit **`proposal-042`**-এ commit করুন।
6. **Pull requests, তারপর New pull request খুলুন।** **`proposal-042`**-এর সঙ্গে **`main`** compare করুন, চারটি file change দেখুন এবং Issue উল্লেখ করে PR তৈরি করুন। Maintainer-কে protected base-এর fresh manifest যুক্ত করে consistency check চালাতে বলুন।
7. **Final proposal revision-এ owner review চাইুন।** Review এবং read-back সফল না হওয়া পর্যন্ত delivery open রাখুন।

**Navigation record:** repository name, Issue number, proposal branch, changed-file path, PR number, check-run name, review revision এবং final `main` commit লিখুন। Issues, Code, Pull requests, Actions এবং PR Checks/Reviews view ব্যবহার করে record আবার খুঁজুন। GitHub control সরালে screenshot দেখে অনুমান করবেন না, number বা commit ID দিয়ে একই record খুঁজুন। Record URL এবং observed status-সহ private evidence note export করুন। Authorized team-এর বাইরে share করার আগে account name, email, token, tenant identifier এবং unrelated repository data সরান। Unredacted evidence approved private location-এ রাখুন।

**GitHub branch এবং fork contribution route নথিভুক্ত করে।** Write access না থাকা contributor approved fork বা Issue route ব্যবহার করেন। Fork মূল repository-তে publication access দেয় না।

## উদাহরণসহ পরিবর্তনের তুলনা দেখুন

| File | Baseline | Candidate |
|---|---|---|
| **প্রয়োজনীয়তা** | রিভিশন 1, সাত দিন | রিভিশন 2, ত্রিশ দিন |
| **Configuration** | Seven days | Thirty days |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **প্রস্তাব** | 7 থেকে 7 | 7 থেকে 30, ভিত্তি 1 |
| **ম্যানিফেস্ট** | সংগ্রহ করা হয়নি | সুরক্ষিত পরিবর্তন-পূর্ব উৎসের হ্যাশ |

**Manifest base বর্ণনা করে**, proposed thirty-day wording নয়। Candidate requirement hash করে baseline evidence বললে trusted-base mismatch তৈরি হয়।

## যাচাই ও হস্তান্তর

**Positive test:** owner review এবং successful check-এর পর maintainer merge করেন। **`main`**-এর resulting file খুলে agreement নিশ্চিত করুন। Resulting commit এবং read-back Issue-এ যুক্ত করুন। এটি committed configuration প্রমাণ করে, runtime deletion behavior নয়।

**Negative test:** Chat-কে proposal approve বা publish করতে বলুন। Expected policy behavior হলো draft-only response। Contributor হিসেবে আলাদা করে direct publication চেষ্টা করুন এবং unchanged source revision-সহ platform denial record করুন। Behavioral test এবং access-control test আলাদা রাখুন।

```text
হস্তান্তর: HANDOFF-042
প্রস্তাব: PROP-042
নীতি: POL-01 সংস্করণ 1
উৎস: বর্তমান প্রয়োজনীয়তা, রানবুক ও কনফিগারেশনের রিভিশন সংযুক্ত করুন
প্রকাশিত মান: main পড়ে নথিভুক্ত করুন
সম্পন্ন: মার্জ করা ফাইল ও যাচাইয়ের রেফারেন্স
বাকি: রানটাইমে মুছে ফেলার পরিষেবা পরীক্ষা করা হয়নি
পরবর্তী ভূমিকা: কার্যক্রম-মালিক
পরবর্তী পদক্ষেপ: স্বাধীনভাবে উৎস পড়া ও রানবুক যাচাই
থামুন: উৎস পরিবর্তিত, প্রবেশাধিকার নেই, কর্তৃত্বে দ্বন্দ্ব
```

**শুধু map এবং handoff নিয়ে নতুন session শুরু করুন।** Fresh source read বা browser evidence-এর explicit request চাইুন। Previous assistant summary পুনরাবৃত্তি না করে source record থেকে value reconstruct করতে হবে।

## প্রসঙ্গ বজায় রেখে খসড়া তৈরি করুন

**Browser contributor-এর একটি সম্পূর্ণ question দরকার।** “Please change retention to thirty days” বর্তমান authority, scope, review state এবং affected record বাদ দেয়। Chat-কে source packet ও drafting instruction দিন। Record না থাকলে remembered text বসাবেন না, maintainer-এর কাছে authorized evidence চাইুন।

```text
সংযুক্ত কৃত্রিম উৎস-প্যাকেট থেকে PROP-042-এর জন্য একটি Issue খসড়া করুন।
সাত দিনকে অনুমোদিত ভিত্তিমূল্য হিসেবে চিহ্নিত রাখুন।
ত্রিশ দিনকে প্রস্তাবিত উদ্দেশ্য হিসেবে চিহ্নিত রাখুন।
উৎপাদন ডেটা, ব্যাকআপ এবং আইনি সংরক্ষণের ব্যতিক্রম বজায় রাখুন।
প্রয়োজনীয়তা, কনফিগারেশন, প্রস্তাব এবং রানবুকের পরিবর্তনগুলো তালিকাভুক্ত করুন।
অনুমানভিত্তিক রিভিশন দিয়ে পূরণ না করে অনুপস্থিত প্রমাণের তালিকা দিন।
মালিকের অনুমোদন বা কাজ সম্পন্ন হয়েছে বলে দাবি করবেন না।
```

**Copy করার আগে answer inspect করুন।** Scope বদলেছে, commit বানানো হয়েছে বা approval complete বলা হয়েছে কি না দেখুন। Unsupported claim সরান এবং unresolved question Issue-এ রাখুন। Chat proposal লিখতে সাহায্য করে, সে না-পড়া system থেকে evidence দেয় না।

## অবদানের পথ বেছে নিন

| পরিস্থিতি | অবদানপথ | জমাদানের ফল |
|---|---|---|
| **শুধু পড়ার অনুমতি** | নির্ধারিত প্রস্তাবিত ভাষ্যসহ Issue | রক্ষণাবেক্ষণকারীর জন্য প্রস্তুত পরিবর্তনের অনুরোধ |
| **অনুমোদিত ব্রাঞ্চে প্রবেশাধিকার** | একটি প্রস্তাব ব্রাঞ্চে ব্রাউজারে সম্পাদনা | সংশ্লিষ্ট ফাইলের পরিবর্তনসহ PR |
| **অনুমোদিত ফর্ক পদ্ধতি** | ফর্ক ও মূল রিপোজিটরিতে PR | মূল রিপোজিটরির পর্যালোচনার অপেক্ষায় থাকা পরিবর্তনের প্রস্তাব |
| **উৎসে প্রবেশাধিকার নেই** | থামুন এবং অনুমোদিত প্রমাণ চান | স্পষ্টভাবে অবরুদ্ধ কাজ |

**Issue route সম্পূর্ণ contribution**, ব্যর্থ coding exercise নয়। আপনি intended change, evidence, scope এবং review question দেন। Maintainer patch এবং manifest দেন। তারপর আপনার request-এর সঙ্গে patch মেলে কি না দেখুন।

| অবদানপথ | অবদানকারীর কাজ সম্পন্নতার যাচাই | রক্ষণাবেক্ষণকারীর কাছে হস্তান্তর |
|---|---|---|
| **শুধু Issue** | Issue-এ যাচাইকৃত উৎস-প্যাকেট, নির্ধারিত প্রস্তাবিত ভাষ্য, ব্যতিক্রম ও খোলা প্রশ্ন আছে | রক্ষণাবেক্ষণকারী ব্রাঞ্চ তৈরি করেন, যাচাই চালান এবং PR-এর লিংক দেন |
| **PR** | একটি ব্রাঞ্চে সব প্রভাবিত ফাইল আছে, PR-এর পরিবর্তন প্রস্তাবের সঙ্গে মেলে এবং পর্যালোচকেরা চূড়ান্ত রিভিশন পান | রক্ষণাবেক্ষণকারী যাচাই চালান, মালিকের পর্যালোচনা নেন, merge করেন এবং পড়ে নিশ্চিত করা ফল নথিভুক্ত করেন |

**Browser edit করলে proposal branch-এ থাকুন।** প্রথম edit branch তৈরি করার পর একই branch selector থেকে বাকি file খুলুন। শেষে PR diff দেখুন। চারটি unrelated branch চারটি অসম্পূর্ণ change তৈরি করে, একটি reviewable package নয়।

## প্রস্তাবিত ভাষ্য পর্যালোচনা করুন

**দুর্বল wording-এর উদাহরণ:** “Exports now remain available for thirty days.” এটি delivery complete বলে এবং synthetic scope বাদ দেয়। Review চলার সময় proposal statement ব্যবহার করুন।

```text
প্রস্তাবিত অভিপ্রায়:
কৃত্রিম এক্সপোর্ট ফাইল ৩০ দিন রাখুন।
উৎপাদনের তথ্য, ব্যাকআপ ও আইনি সংরক্ষিত উপাদান বাদ দিন।

বর্তমান অনুমোদিত অভিপ্রায়:
REQ-17-এর রিভিশন 1 অনুযায়ী কৃত্রিম এক্সপোর্ট ফাইল 7 দিন রাখুন।

সরবরাহ:
প্রকাশিত নয়। রানটাইমে মুছে ফেলার কোনো পরিষেবা পরীক্ষা করা হয়নি।
```

**প্রতিটি affected file-এর সঙ্গে wording তুলনা করুন।** Candidate-এ requirement revision এগিয়েছে। Configuration thirty-এ পৌঁছেছে। Runbook-এর প্রথম line thirty-এ পৌঁছেছে এবং lab limitation রেখেছে। Proposal এখনও seven-কে previous value এবং revision one-কে base বলে।

**Mismatch হলে অপরিচিত control repair না করে প্রশ্ন করুন।** Maintainer patch protection দুর্বল বা policy delete করলে explanation এবং separate review চাইুন। Workflow-এর প্রতিটি line না বুঝেও requested scope-এর বাইরের change চিহ্নিত করা যায়।

## পর্যালোচনার মতামতের উত্তর দিন

**উদাহরণ review:** Operations এমন একটি sentence চায় যা বলে configuration rollback deleted file ফিরিয়ে আনে না। একই branch-এ draft update করুন এবং reviewer-কে amended scope জানান। Final review modified proposal-এর উপর হতে হবে, পুরনো chat copy-এর উপর নয়।

| পর্যালোচনার মন্তব্য | অবদানকারীর পদক্ষেপ |
|---|---|
| **ব্যতিক্রম অনুপস্থিত** | বাদ পড়া ভাষ্য ফিরিয়ে এনে উদ্দেশ্য পর্যালোচনার অনুরোধ করুন |
| **পুরোনো উৎস-রিভিশন** | নতুন অনুমোদিত প্যাকেটের সঙ্গে মিলিয়ে দেখুন |
| **ম্যানিফেস্ট অনুপস্থিত** | রক্ষণাবেক্ষণকারীকে সুরক্ষিত মূল সংস্করণের স্ন্যাপশট তৈরি করতে বলুন |
| **অপ্রাসঙ্গিক নিয়ন্ত্রণের পরিবর্তন** | পর্যালোচনার আগে পরিবর্তনটি আলাদা করুন বা সরিয়ে দিন |
| **পরীক্ষাহীন রানটাইম-সংক্রান্ত দাবি** | ল্যাবের নির্দিষ্ট সীমাবদ্ধতা দিয়ে প্রতিস্থাপন করুন |

**উত্তর না পাওয়া পর্যন্ত question visible রাখুন।** মূল সমস্যা ঠিক না করে comment resolve করলে useful signal মুছে যায়। Reply-তে amendment বা evidence link দিন, যাতে অন্য reviewer পুরো conversation না পড়েও decision অনুসরণ করতে পারেন।

## ব্রাউজারে কাজ সম্পন্ন হয়েছে কি না যাচাই

**এমন Issue বা PR hand off করুন যা অন্য maintainer অনুমান ছাড়া চালাতে পারেন।** এতে source packet, proposed wording, affected record, exclusions, owner role এবং unresolved question থাকবে। Publication-এর পর read-back নিন এবং original proposal থেকে আলাদা রাখুন।

**Self-check:** আপনার chat না-জানা কাউকে package দিন। Requested, approved এবং published value আলাদা করতে বলুন। Merge-এর আগে thirty delivered বললে package label ঠিক করুন। Workplace track-এও একই discipline রাখুন।

| Review gate | Pass condition |
|---|---|
| **Source revisions** | Claimed প্রতিটি commit বা page version sandbox-এ খোলে। Unknown revision Missing থাকে। |
| **Exclusions** | Production data, backup এবং legal hold proposal-এর বাইরে থাকে। |
| **Questions** | Unresolved owner বা source question Issue বা PR-এ দৃশ্যমান থাকে। |
| **Approval freshness** | Review final proposal revision-এর নাম দেয়। Earlier approval later edit cover করে না। |

**যে কোনো failed gate publication pending রাখে।** Issue-only contributor maintainer-কে result দেন। PR contributor repair-এর পর আবার review চান।

## সমস্যা নির্ণয় ও পূর্বাবস্থায় ফেরানো

**Edit permission নেই:** Issue বা approved fork ব্যবহার করুন। **Invented commit reference:** verified evidence দিয়ে বদলে আবার review করুন। **Edit-এর আগের approval:** fresh approval চাইুন।

**Rollback:** Unmerged PR close করে evidence রাখুন। Merged content-এর জন্য maintainer-এর কাছে protected revert proposal চাইুন। Recovery সফল দেখাতে baseline বদলাবেন না।

## অনুশীলন ও স্ব-মূল্যায়ন

**নতুন assistant-এর কাছ থেকে requirement record গোপন করুন** এবং publication recommendation চাইুন।

**Expected reasoning:** authoritative evidence চাইবে অথবা response snapshot-based বলে চিহ্নিত করবে। Fresh read সফল না হওয়া পর্যন্ত publication blocked থাকবে।

## প্রধান তথ্যসূত্র

- **Browser steps:** [ফাইল সম্পাদনা](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)।
- **Review boundary:** [সুরক্ষিত ব্রাঞ্চ](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)।

## পরের ধাপ

**[Confluence এবং Jira Setup](/articles/ai-collaboration-confluence-jira-setup/)-এ এগিয়ে যান** এবং workplace system-গুলোতে একই operating model পুনরাবৃত্তি করুন।
