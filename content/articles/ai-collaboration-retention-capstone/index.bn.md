---
title: "AI সহযোগিতার ক্যাপস্টোন: GitHub, Confluence এবং Jira"
date: 2026-10-01
lastmod: 2026-11-13
toc: true
draft: false
description: "ব্যর্থতার প্রমাণ এবং স্বাধীন পর্যালোচনাসহ GitHub-প্রথম এবং Confluence/Jira কর্মপ্রবাহে কৃত্রিম তথ্য-সংরক্ষণ পরিবর্তন সম্পন্ন করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "দলগত সহযোগিতা", "সফটওয়্যার ইঞ্জিনিয়ারিং"]
tags: ["AI সহযোগিতা কোর্স", "সংরক্ষণ প্রস্তাব", "GitHub পর্যালোচনা", "Confluence Jira কর্মপ্রবাহ", "ব্যর্থতার ম্যাট্রিক্স", "স্বাধীন গ্রহণ"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "সাইবার নিরাপত্তা কর্মক্ষেত্রে যৌথ প্রকল্পের কাজ পর্যালোচনা করা পেশাজীবীদের চিত্র"
coverCaption: ""
---

[AI সহযোগিতা কোর্সে ফিরে যান](/ai-collaboration-course-start/)

**PROP-042 দুইবার সরবরাহ করুন**, একবার GitHub-প্রথম পদ্ধতিতে এবং একবার GitHub-এর সঙ্গে Confluence/Jira ব্যবহার করে। আপনি অবদান রাখবেন, আলাদা মালিকেরা পর্যালোচনা করবেন, এবং অনুমোদিত প্রকাশকেরা পরিবর্তনটি প্রয়োগ করবেন। আগের পাঠের পর বিচ্ছিন্ন synthetic sandbox ব্যবহার করুন। এই ক্যাপস্টোন প্রত্যাখ্যান, পুনরুদ্ধার এবং স্বাধীন হস্তান্তরসহ সম্পূর্ণ প্রক্রিয়া পরীক্ষা করে। এটি শুধু সহকারীর লেখার মান পরীক্ষা করে না।

## মূল শিক্ষা

- **একটি অভিন্ন পরিবর্তন** দুইটি authority model তুলনা করে।
- **নেতিবাচক পরীক্ষা** সফল delivery-এর মতোই গুরুত্বপূর্ণ।
- **প্রমাণের প্যাকেজ** স্বাধীন পর্যালোচনাকে সহায়তা করে।
- **ল্যাব সম্পন্ন হওয়া** production rollout-এর অনুমতি দেয় না।

## শুরু করার আগে

**পূর্বশর্ত:** আগের [কোর্স মডিউল](/ai-collaboration-course-start/), অনুমোদিত sandbox access, এবং আলাদা reviewer। **পরিকল্পিত সময়:** একাধিক session-এ আট থেকে বারো ঘণ্টা, সঙ্গে স্বাধীন পর্যালোচনা। প্রকৃত সময় account setup এবং repair-এর ওপর নির্ভর করে। **কঠিনতা:** advanced।

**প্রয়োজনীয় উপকরণ:** সনদ, মানচিত্র, নীতি, সংযোগকারী, ভিত্তি, তালিকা, নির্দিষ্ট প্রস্তাব, দায়িত্বপ্রাপ্তের পর্যালোচনা, নথিপঞ্জি, পুনরুদ্ধার-নথি এবং হস্তান্তর। পরিকল্পনা-নির্ভর অনুমতি না থাকলে কাজ থামবে। অনুমান করে সেগুলোকে উত্তীর্ণ ধরা যাবে না।

**পরীক্ষার আগে প্রতিটি track-এর জন্য একটি evidence directory তৈরি করুন।** Reviewer যেন chat summary ছাড়াই actor, source revision, attempted action, observed result, এবং final state শনাক্ত করতে পারেন।

## দুটি প্রাথমিক মান স্থাপন করুন

1. **বিচ্ছিন্ন run তৈরি করুন** এবং নাম দিন GitHub-first ও Mixed। Revision এবং review আলাদা রাখুন।
2. **সাত দিনের baseline পুনরুদ্ধার করুন** প্রতিটি track-এর অনুমোদিত পদ্ধতিতে, এবং তৈরি হওয়া revision সংরক্ষণ করুন।
3. **Denial control যাচাই করুন** contributor এবং excluded-user account দিয়ে।
4. **বর্তমান context ধরুন** এবং adapter/policy-এর সামঞ্জস্য নিশ্চিত করুন।
5. **Scope ঘোষণা করুন:** ত্রিশ দিনের synthetic export retention। বাস্তব data, backup, এবং legal hold বাদ থাকবে।

**PROP-042 একটি correlation label, পুনঃব্যবহারযোগ্য approval নয়।** প্রতিটি run-এর frozen revision এবং source evidence আলাদা হবে। Report-এ run ID দিন।

## GitHub-first পদ্ধতি সম্পন্ন করুন

**GitHub lesson ব্যবহার করে Issue এবং candidate PR খুলুন।** Requirement, configuration, proposal, এবং runbook একসঙ্গে পরিবর্তন করুন। Protected base ধরুন, trusted check চালান, এবং final commit-এ product ও operations review নিন।

```text
রান: GitHub-first
পরিবর্তন: কৃত্রিম ডেটা সংরক্ষণ 7 -> 30 দিন
প্রয়োজনীয়তা: REQ-17 সংস্করণ ২
কনফিগারেশন: retention_days 30
রানবুক: সংরক্ষণের মেয়াদ: ৩০ দিন
প্রস্তাব: বেস সংস্করণ 1, থেকে 7, পর্যন্ত 30
ম্যানিফেস্ট: পরিবর্তনের আগের সুরক্ষিত সোর্স হ্যাশ
পর্যালোচনা: প্রোডাক্ট ও অপারেশনসের চূড়ান্ত প্রস্তাব সংস্করণে পর্যালোচনা
প্রকাশনা: মার্জ করা কমিট ও পুনরায় পড়ে যাচাই
সীমা: চলমান ডিলিশন সার্ভিস পরীক্ষা করা হয়নি
```

**Sandbox থেকে প্রকৃত reference পূরণ করুন।** এই outline প্রত্যাশিত mapping, সম্পূর্ণ evidence নয়। Reviewer শেষ না করা পর্যন্ত maintainer merge করবেন না। তারপর স্বাধীনভাবে **`main`** পড়ুন। Final record link করার পর Issue বন্ধ করুন।

## Mixed track সম্পন্ন করুন

**Confluence version পড়ুন এবং Jira proposal freeze করুন।** দুই owner-এর review নিন। Delivery pending অবস্থায় requirement publish করুন, configuration merge করুন, runbook publish করুন, এবং Done করার আগে সব system আবার পড়ুন।

**প্রতিটি publication record করুন** page version, commit, অথবা transition evidence-সহ। Repository requirement copy snapshot হিসেবে থাকবে। Local checker বর্তমান Confluence authority প্রমাণ করে না।

| তুলনা | GitHub-first | মিশ্র কর্মক্ষেত্র |
|---|---|---|
| **প্রয়োজনীয়তা** | সুরক্ষিত repository-তে পর্যালোচনা | Confluence-এর মালিক-পর্যালোচিত প্রকাশনা |
| **সমন্বয়** | Issue/PR | Jira-তে নির্দিষ্ট প্রস্তাব |
| **প্রকাশনার একক** | repository merge | আলাদা পৃষ্ঠা লেখা ও merge |
| **সতেজতা** | সুরক্ষিত commit | পৃষ্ঠা সংস্করণ ও commit |
| **পুনরুদ্ধার** | পর্যালোচিত revert বা ক্ষতিপূরণ | ledger-নির্দেশিত ক্ষতিপূরণ |

**Ownership need অনুযায়ী workflow বাছুন।** GitHub-first cross-system coordination কমায়। Mixed track workplace home ধরে রাখে এবং publication/access check যোগ করে।

## ব্যর্থতা পরীক্ষামালা চালান

| ঘটনা | প্রবর্তন | যে পর্যবেক্ষিত প্রমাণ চাই |
|---|---|---|
| **অনুমোদিত পরিবর্তন** | পর্যালোচিত ত্রিশ দিনের প্রস্তাব জমা দিন | সামঞ্জস্যপূর্ণ পুনরায় পাঠ ও পর্যালোচনা |
| **পুরোনো প্রসঙ্গ** | ধারণের পর উৎস বদলান | প্রত্যাখ্যান, সমন্বয়, পুনরায় অনুমোদন |
| **অননুমোদিত লেখা** | অবদানকারী প্রকাশনার চেষ্টা করে | প্রত্যাখ্যান এবং অপরিবর্তিত সংস্করণ |
| **দ্বন্দ্ব** | Jira-তে ষাট দিন, Confluence-এ সাত | আটকে দিন এবং মালিকের সমন্বয় নিন |
| **আংশিক প্রকাশনা** | একটি লেখার পর থামুন | অপেক্ষমাণ ledger এবং পুনরুদ্ধার |
| **প্রবেশাধিকার প্রত্যাখ্যান** | কাজের পাঠাধিকার সরান | সুরক্ষিত লেখা বা প্রকাশনা কোনোটিই নয় |
| **পুনরুদ্ধার** | অনুমোদিত সম্পন্নকরণ বা প্রত্যাবর্তন | নতুন পর্যালোচিত সংস্করণ |
| **হস্তান্তর** | নতুন সেশন শুধু মানচিত্র ও ledger পায় | নতুন করে পড়া এবং সঠিক পরের পদক্ষেপ |

**Cross-system conflict Mixed-এর বিষয়।** GitHub-first-এ Issue description এবং approved file-এর conflict পরীক্ষা করুন। অন্য প্রযোজ্য case দুই track-এই চালান। Local validator failure live permission evidence-এর বিকল্প নয়।

| ঘটনা ও প্রমাণের ফাইল | GitHub-first রান | Mixed রান |
|---|---|---|
| **অনুমোদিত পরিবর্তন** `01-approved-change.md` | পর্যালোচিত PR এবং পুনরায় পাঠ | পর্যালোচিত পৃষ্ঠা, merge এবং ledger |
| **পুরোনো প্রসঙ্গ** `02-stale-context.md` | ধারণের পর সুরক্ষিত ভিত্তি বদলান | ধারণের পর কর্তৃত্বপূর্ণ পৃষ্ঠা বদলান |
| **অননুমোদিত লেখা** `03-unauthorized-write.md` | সরাসরি push প্রত্যাখ্যান | পৃষ্ঠা সম্পাদনা ও অবস্থা পরিবর্তন প্রত্যাখ্যান |
| **দ্বন্দ্ব** `04-conflict.md` | Issue অনুমোদিত ফাইলের সঙ্গে মেলে না | Jira-র লেখা Confluence-এর সঙ্গে মেলে না |
| **আংশিক প্রকাশনা** `05-partial-publication.md` | merge বা পুনরায় পড়ার আগে থামুন | একটি পৃষ্ঠা লেখার পর থামুন |
| **প্রবেশাধিকার প্রত্যাখ্যান** `06-access-denial.md` | সুরক্ষিত repository উৎসে প্রবেশ বন্ধ রাখুন | সীমাবদ্ধ পৃষ্ঠা থেকে ব্যবহারকারী বাদ দিন |
| **পুনরুদ্ধার** `07-recovery.md` | পর্যালোচিত revert বা সম্পন্নকরণ | ledger-নির্দেশিত ক্ষতিপূরণ |
| **হস্তান্তর** `08-handoff.md` | নতুন সেশন সুরক্ষিত ফাইল পড়ে | নতুন সেশন নির্ধারিত পৃষ্ঠা ও ledger পড়ে |

**প্রতিটি test-এর আগে তার file তৈরি করুন।** Expected result, observed result, actor role, initial ও final revision, native evidence reference, এবং reviewer decision লিখুন। দুই track-এর directory আলাদা রাখুন।

**Expected এবং observed outcome আলাদা রাখুন।** প্রতিটি case-এ run ID, actor role, initial revision, attempted action, expectation, observation, resulting revision, এবং reviewer decision record করুন। Shared report থেকে credential এবং account identifier সরিয়ে দিন।

## সম্পন্ন হওয়ার মূল্যায়ন করুন

**প্রযোজ্য প্রতিটি row-এর observed evidence** এবং independent acceptance না থাকলে pass নয়। Reviewer permission, source freshness, role review, partial publication, এবং handoff reconstruction পরীক্ষা করবেন।

**Unauthorized publication, model-এ denied text পৌঁছানো, অথবা পরিবর্তিত base নীরবে overwrite হলে সঙ্গে সঙ্গে fail করুন।** Control সংশোধন করে repeat test pass না করা পর্যন্ত কাজ Blocked রাখুন। Failure-কে favorable score-এ মেশাবেন না।

**Completed/blocked case, rejected stale proposal, denied write, recovery, এবং reviewer time মাপুন।** Observed না হওয়া পর্যন্ত proposed outcome expected থাকবে।

## দুটি পরীক্ষা পরিকল্পনা করুন

**দুই track-এ approval পুনঃব্যবহার করবেন না।** Value একই হলেও source home, captured revision, permission, এবং publication sequence আলাদা। প্রতিটি run-এর নিজস্ব evidence directory এবং review packet দিন।

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    একই প্রমাণের বিভাগ, আলাদাভাবে সংগ্রহ করা
```

**এই নামগুলো organization example।** এগুলো supplied archive file নয়। Approved sandbox-এ প্রকৃত evidence ব্যক্তিগতভাবে রাখুন। Shared submission-এ role label ও redacted reference ব্যবহার করুন।

**Failure চালানোর আগে test observer নিযুক্ত করুন।** Contributor attempted action করবে। Observer initial state, outcome, এবং resulting state লিখবে। Reviewer পরে evidence claim সমর্থন করে কি না নির্ধারণ করবেন। Role overlap থাকলে প্রকাশ করুন।

## ব্যর্থতাগুলো আলাদাভাবে চালান

**Case-এর মাঝখানে verified reviewed state-এ reset করুন।** Source drift, access revocation, এবং runbook mismatch একসঙ্গে inject করলে কোন control proposal reject করেছে বোঝা যায় না। প্রতি run-এ একটি failure reviewer-এর জন্য traceable কারণ দেয়।

1. **Initial state ধরুন:** source revision, configuration, delivery state, এবং actor role।
2. **একটি synthetic injection দিন:** authorized test route দিয়ে একটি condition বদলান।
3. **Bounded action চেষ্টা করুন:** validation, read, publication, অথবা handoff।
4. **Observation record করুন:** actual output এবং resulting source state।
5. **Review-এর মাধ্যমে repair করুন:** control restore করার আগে failure evidence রাখুন।
6. **Positive case পুনরায় চালান:** corrected workflow permitted work deliver করে কি না দেখুন।

**প্রতি ঘটনার ইনজেকশন ও পুনরুদ্ধার কার্ড:** পরের ঘটনার আগে নতুন কৃত্রিম প্রস্তাব নিন অথবা পর্যালোচিত ভিত্তি ফিরিয়ে আনুন। পর্যবেক্ষক পূর্বশর্ত নথিভুক্ত করে এবং পুনরুদ্ধার নিশ্চিত করে। ব্যর্থ প্রচেষ্টা ledger থেকে মুছবেন না।

| ঘটনা | GitHub-first: প্রবেশ ও যাচাই | Mixed: প্রবেশ ও যাচাই | পরের ঘটনার আগে পুনরুদ্ধার |
|---|---|---|---|
| অনুমোদিত পরিবর্তন | নির্দিষ্ট PR জমা দিন, দুইটি পর্যালোচনা নিন, merge করুন, তারপর `main` আবার খুলুন | REQ-17 প্রকাশ করুন, পর্যালোচিত diff merge করুন, RUN-04 প্রকাশ করুন, তারপর সব রেকর্ড আবার পড়ুন | চূড়ান্ত রিভিশনগুলো নতুন ভিত্তি হিসেবে নথিভুক্ত করুন |
| পুরোনো প্রসঙ্গ | manifest নিন, তারপর পুরোনো প্রস্তাব যাচাইয়ের আগে আলাদা পর্যালোচিত PR দিয়ে পরীক্ষার ভিত্তি বদলান | পৃষ্ঠার সংস্করণ নিন, তারপর লেখার আগের পাঠের আগে অনুমোদিত সম্পাদককে পরীক্ষার পৃষ্ঠা বদলাতে বলুন | থামুন, সংস্করণ তুলনা করুন, নতুন উৎস নিন, নতুন প্যাকেজ পর্যালোচনা করুন |
| অননুমোদিত লেখা | Contributor সুরক্ষিত `main`-এ নিরীহ সরাসরি push করার চেষ্টা করে এবং সার্ভারের প্রত্যাখ্যান নথিভুক্ত করে | Contributor REQ-17 সম্পাদনা ও Approved রূপান্তরের চেষ্টা করে | commit, পৃষ্ঠার সংস্করণ ও Jira অবস্থা আবার পড়ে অপরিবর্তিত থাকা নিশ্চিত করুন |
| দ্বন্দ্ব | খসড়া Issue-তে ৬০ দিন, অনুমোদিত ফাইলে ৭ দিন | খসড়া Jira-তে ৬০ দিন, REQ-17-এ ৭ দিন | পণ্যের মালিক খসড়া মিলিয়ে সিদ্ধান্ত নথিভুক্ত করেন |
| আংশিক প্রকাশ | অনুমোদনের পর কিন্তু merge বা পুনরায় পড়ার আগে থামুন, Issue খোলা রাখুন | REQ-17 আবার পড়ার পর থামুন, যখন কনফিগারেশন ও RUN-04-এ এখনও ৭ দিন | ডেলিভারি মুলতবি রাখুন এবং পর্যালোচিত সম্পন্নকরণ বা ক্ষতিপূরণের সিদ্ধান্ত নিন |
| প্রবেশাধিকার প্রত্যাখ্যান | বাদ পড়া পরীক্ষামূলক পরিচয় দিয়ে ব্যক্তিগত পরীক্ষাগারের কৃত্রিম উৎস পড়ার চেষ্টা | বাদ পড়া পরিচয় দিয়ে সীমাবদ্ধ কৃত্রিম পৃষ্ঠা খোলার চেষ্টা | শুধু অনুমোদিত পরীক্ষামূলক প্রবেশাধিকার ফিরিয়ে দিন এবং স্বাভাবিক পাঠককে যাচাই করুন |
| পুনরুদ্ধার | অনুমোদিত পরীক্ষার পরিবর্তন থামিয়ে পর্যালোচিত সম্পন্নকরণ বা প্রত্যাবর্তন প্রস্তাব করুন | আংশিক প্রকাশের ledger দিয়ে পর্যালোচিত সম্পন্নকরণ বা ক্ষতিপূরণ প্রস্তাব করুন | প্রতিটি উৎস আবার পড়ুন এবং ledger মেলান |
| হস্তান্তর | পুরোনো চ্যাট ছাড়া নতুন পর্যালোচককে MAP-01 ও ledger দিন | পুরোনো চ্যাট ছাড়া নতুন পর্যালোচককে নির্ধারিত পৃষ্ঠা ID ও ledger দিন | পর্যালোচক বর্তমান উৎস খুলে পরের অনুমোদিত পদক্ষেপ নথিভুক্ত করেন |

প্রতিটি প্রত্যাখ্যাত ঘটনার জন্য প্ল্যাটফর্মের প্রতিক্রিয়া ও সুরক্ষিত রেকর্ডের দ্বিতীয় পাঠ নথিভুক্ত করুন। বাদ পড়া ব্যবহারকারীর ক্ষেত্রে provider-এর টুল ট্রেস, retrieval log বা audit record দেখে সুরক্ষিত লেখা কাজে পৌঁছেছিল কি না যাচাই করুন। এসব প্রমাণ না থাকলে প্রবেশ-নিরাপত্তা যাচাইকে Blocked চিহ্নিত করুন, কারণ দৃশ্যমান প্রত্যাখ্যান cached excerpt ফেরত আসেনি তা প্রমাণ করে না। পরিকল্পনায় নিয়ন্ত্রণ বা অনুমোদিত পরীক্ষার পরিচয় না থাকলেও পাসের অভিনয় না করে Blocked লিখুন।



**Planned failure-ও failure observation।** Probe করার উদ্দেশ্য ছিল বলে unauthorized publication-কে successful test বলবেন না। Test defect প্রকাশ করেছে, কিন্তু publication boundary fail করেছে এবং repair দরকার।

## মিশ্র ফলাফল ব্যাখ্যা করুন

**Illustrative evidence package:** local consistency pass, product ও operations fixed package review করেছে, requirement publication সফল, এবং runbook edit access denied। Configuration এখনও merge হয়নি। Jira Blocked।

| দাবি | সিদ্ধান্ত | কারণ |
|---|---|---|
| **প্রস্তাবিত রেকর্ডগুলো মেলে** | স্থানীয় যাচাইয়ে সমর্থিত | দেওয়া রেকর্ড তুলনা পাস করেছে |
| **দায়িত্বপ্রাপ্তেরা উদ্দেশ্য ও কার্যক্রম মেনেছেন** | নির্দিষ্ট native পর্যালোচনা চাই | শুধু ভূমিকার লেবেল যথেষ্ট নয় |
| **ত্রিশ দিনের সরবরাহ সম্পন্ন** | সমর্থিত নয় | আবশ্যক প্রকাশনার ধাপ বাকি |
| **প্রতিটি ভূমিকার জন্য অনুমতির সীমা কাজ করে** | সমর্থিত নয় | একটি প্রত্যাখ্যাত কাজ সীমিত ক্ষেত্র দেখায় |
| **পুনরুদ্ধারের দায়িত্বপ্রাপ্তের পদক্ষেপ নেওয়া উচিত** | পরের পদক্ষেপ হিসেবে সমর্থিত | আংশিক সরবরাহে পর্যালোচিত সিদ্ধান্ত দরকার |

**Expected reasoning:** run incomplete রাখুন, current source যাচাই করুন, এবং appropriate owner decision চান। Permission দুর্বল করে বা snapshot check-কে live publication evidence বলে কাজ শেষ করবেন না।

**ভরা মিশ্র-ট্র্যাক শিক্ষণ প্যাকেট, কৃত্রিম এবং প্রকৃত tenant-এর প্রমাণ নয়:**

```text
রান: MIXED-042-example
ধরা বেসলাইন: REQ-17 v4 = 7 দিন; RUN-04 v2 = 7 দিন।
GitHub main base-001 config.json = {"retention_days": 7}; Jira PROP-042 r1 = In Review.
স্থির প্রস্তাব: REQ-17 v5-এ কৃত্রিম এক্সপোর্ট 30 দিন রাখার কথা। উৎপাদন ডেটা, ব্যাকআপ ও আইনি সংরক্ষণ বাদ।
GitHub config.json-এ retention_days 7 থেকে 30। RUN-04 v3-এ 30 দিন; ল্যাবে কোনো ডিলিশন সার্ভিস চলে না। অসম্পূর্ণ প্রকাশনা অপেক্ষমাণ।
পর্যালোচনা: পণ্য-মালিক PROP-042 r1-এ REQ-17-এর হুবহু ভাষা অনুমোদন করেন। অপারেশনস r1-এ কনফিগারেশন diff ও রানবুক অনুমোদন করে।
প্রকাশনা: প্রকাশক REQ-17 v5 ও RUN-04 v3 পড়ে 30 দিন নিশ্চিত করেন; রক্ষণাবেক্ষক merge-002-এ main পড়ে retention_days 30 নিশ্চিত করেন।
প্রত্যাখ্যাত কাজ: অবদানকারী REQ-17 v5 সম্পাদনা করতে পারেননি। প্রকাশক অপরিবর্তিত অবস্থা নিশ্চিত করেন; পর্যবেক্ষক প্ল্যাটফর্মের প্রমাণ সংরক্ষণ করেন।
পুনরুদ্ধার: RUN-04 চেষ্টা ব্যর্থ, Jira Blocked থাকে। অপারেশনস পুনঃচেষ্টা অনুমোদন করে; v3 আবার পড়ার পর Jira Done হয়।
হস্তান্তর: নতুন পর্যালোচক MAP-01 ও লগ পান, তিনটি উৎস এবং Jira পড়ে 30 দিন ও বাকি রানটাইম ঘাটতি জানান।
সীমা: শুধু উৎস প্রকাশের প্রমাণ আছে। ডিলিশনের সময়: চালানো হয়নি।
```

## স্বতন্ত্র পাঠকের সঙ্গে পর্যালোচনা করুন

**Reviewer-কে event reconstruct করতে বলুন**, আপনার conclusion পড়তে নয়। তিনি approved baseline, fixed proposal, owner decision, resulting revision, failed attempt, repair, এবং remaining gap আপনার narration ছাড়া খুঁজে পাবেন।

```text
স্বাধীন পর্যালোচনার প্রশ্ন:
এই প্রবাহে সংরক্ষণের উদ্দেশ্য কোন উৎস নির্ধারণ করে?
প্রতিটি মালিক ঠিক কোন প্যাকেজ পর্যালোচনা করেছেন?
পর্যালোচনার পর কোনো উৎস বদলেছে কি?
কী প্রকাশিত হয়েছে, আর কী অপেক্ষমাণ?
কোন প্রত্যাখ্যাত কাজ কোন ভূমিকার অধীনে দেখা গেছে?
সুরক্ষিত লেখা কি বাদ পড়া ব্যবহারকারীর প্রসঙ্গে পৌঁছেছে?
কোন সংশোধন পর্যালোচনা করে পুনরায় পড়া হয়েছে?
নতুন হস্তান্তর কি স্বাধীনভাবে বর্তমান অবস্থা পুনর্গঠন করে?
```

**প্রতিটি requirement আলাদা score করুন।** Supported, Failed, Blocked, অথবা Not run এবং evidence reference ব্যবহার করুন। Consistency, approval, permission, recovery, ও handoff পৃথক requirement। Green local test-এর সমষ্টি failed live publication boundary পূরণ করে না।

```text
রান আইডি ও প্রবাহ:
পর্যালোচকের ভূমিকা ও তারিখ:
কেস 01 অনুমোদিত পরিবর্তন: অবস্থা ___ প্রমাণ ___ ঘাটতি ___
কেস 02 পুরোনো প্রসঙ্গ: অবস্থা ___ প্রমাণ ___ ঘাটতি ___
কেস 03 অননুমোদিত লেখা: অবস্থা ___ প্রমাণ ___ ঘাটতি ___
কেস 04 দ্বন্দ্ব: অবস্থা ___ প্রমাণ ___ ঘাটতি ___
কেস 05 আংশিক প্রকাশনা: অবস্থা ___ প্রমাণ ___ ঘাটতি ___
কেস 06 প্রবেশ প্রত্যাখ্যান: অবস্থা ___ প্রমাণ ___ ঘাটতি ___
কেস 07 পুনরুদ্ধার: অবস্থা ___ প্রমাণ ___ ঘাটতি ___
কেস 08 হস্তান্তর: অবস্থা ___ প্রমাণ ___ ঘাটতি ___
সামগ্রিক সিদ্ধান্ত: সমর্থিত / ব্যর্থ / অবরুদ্ধ / চালানো হয়নি
পরবর্তী দায়িত্বপ্রাপ্ত ভূমিকা ও কাজ:
```

**Supported মানে reviewer প্রতিটি প্রযোজ্য case-এর observed evidence পেয়েছেন।** Observed control failure হলে Failed, access বা control না থাকলে Blocked, এবং চেষ্টা না হলে Not run লিখুন। প্রতিটি case-এর native reference তার named evidence file-এ রাখুন।

**Course pass gate:** GitHub-first এবং Mixed দুই track শেষ করুন। প্রতিটি track-এর আটটি প্রযোজ্য case Supported হতে হবে। Failed boundary অথবা missing native read-back track block করে। একটি track শেষ হলে documented partial result হবে, course completion নয়।

**Redacted model package, illustrative only:**

```text
প্রবাহ: github-first | রান: G-01 | পর্যালোচক: পৃথক পাইলট ভূমিকা
বেস: সুরক্ষিত কমিট base-001 | স্থির প্রস্তাব: PROP-042 r1
অনুমোদন: পণ্য পর্যালোচনা P-01, অপারেশনস পর্যালোচনা O-01
সামঞ্জস্য: স্থানীয় পরীক্ষা পাস, আউটপুট C-01 সংরক্ষিত
অনুমতি: অবদানকারীর সরাসরি push প্রত্যাখ্যাত, নেটিভ ইভেন্ট D-01
প্রকাশনা: কমিট merge-002; নতুন ক্লোনে 30 দিন নিশ্চিত
ব্যতিক্রম: ব্যাকআপ ও আইনি সংরক্ষণ বাদ
পুনরুদ্ধার: বিঘ্ন R-01 পুনরায় পড়ে পর্যালোচনার মাধ্যমে সমাধান
হস্তান্তর: দ্বিতীয় পাঠক বর্তমান বেস, ব্যতিক্রম ও পরের কাজ খুঁজে পান
রানটাইম সীমা: উৎপাদন ডিলিশন বা ডেপ্লয়মেন্টের দাবি নেই
সিদ্ধান্ত: কেবল কৃত্রিম GitHub-first প্রবাহের জন্য সমর্থিত
```

Illustrative reference-গুলোর বদলে sandbox-এর observed artifact বসান। Mixed track-এর জন্য আলাদা source version ও review-সহ পুরো package পুনরাবৃত্তি করুন। Reviewer-এর mixed package-এ copied GitHub approval প্রত্যাখ্যান করা উচিত।

## সীমাবদ্ধ সিদ্ধান্ত লিখুন

**ভালো closing decision পরের pilot নির্ধারণ করে**, unrestricted rollout নয়। একই role এবং direct lookup route রেখে আরেকটি synthetic export setting বাছুন। Real data এবং automated publication scope-এর বাইরে রাখুন।

| সিদ্ধান্তের অংশ | যে বিবরণ দরকার |
|---|---|
| **পরিসর** | পরবর্তী একটি পরিবর্তন এবং স্পষ্টভাবে বাদ থাকা বিষয় |
| **প্রমাণ** | সমর্থিত ঘটনা এবং অমীমাংসিত ব্যর্থতা |
| **নিয়ন্ত্রণ** | প্ল্যাটফর্ম-প্রয়োগ করা নিয়ম ও পদ্ধতিগত শর্ত আলাদা করে |
| **দায়িত্বপ্রাপ্ত** | প্রতিটি বাকি ঘাটতির জন্য জবাবদিহি ভূমিকা |
| **রানটাইম ঘাটতি** | পরীক্ষা না করা মুছে ফেলা বা deployment আচরণ |
| **থামার শর্ত** | প্রবেশাধিকার নেই, কর্তৃত্ব বদলেছে, অননুমোদিত প্রকাশনা |

**Completion check:** দুই run package independent reconstruction পার করবে, প্রযোজ্য failure case observed evidence পাবে, এবং unresolved control দৃশ্যমান থাকবে। শুধু GitHub track শেষ হলে partial course completion report করুন। Mixed track একই আচরণ করবে ধরে নেবেন না।

## সমস্যা সমাধান ও পূর্বাবস্থায় ফেরানো

**শুধু happy-path evidence:** denial এবং interruption test আবার চালান। **Overlapping role:** প্রকাশ করে আলাদা user দিয়ে repeat করুন। **Missing plan control:** থামুন এবং approved sandbox নিন।

**Backout:** reviewed PR ও Confluence edit দিয়ে baseline restore করুন, temporary integration revoke করুন, Jira evidence archive করুন, এবং evidence retention-এর পর owner-approved synthetic cleanup করুন। Recovery history রাখুন।

## পর্যায়ক্রমে চালুর সিদ্ধান্ত নিন

```text
সিদ্ধান্ত: আরেকটি কৃত্রিম পাইলট, অবরুদ্ধ, বা প্রত্যাখ্যাত
প্রমাণ: দুই রান প্যাকেজ ও ব্যর্থতার ম্যাট্রিক্স
প্রয়োগহীন শর্ত: পদ্ধতিগত নিয়ন্ত্রণ স্পষ্টভাবে লিখুন
প্রোভাইডার পর্যালোচনা: ইনপুট পরিসর ও সংরক্ষণ
দায়িত্বের আওতা: পণ্য, অপারেশনস, নীতি, রিপোজিটরি, ডেলিভারি
উৎপাদন ঘাটতি: রানটাইম পরীক্ষা, গোপন তথ্য, ডেপ্লয়মেন্ট, প্রবেশ পর্যালোচনা
পরবর্তী কাজ: দায়িত্বপ্রাপ্ত ভূমিকার সঙ্গে সীমিত অনুসরণ
পর্যালোচনার তারিখ: পাইলট মালিকেরা নির্ধারণ করবেন
```

**Expected reasoning:** Synthetic success আরেকটি bounded pilot সমর্থন করে। Production-এর জন্য real data, deployment, provider handling, এবং runtime behavior নিয়ে আলাদা approval দরকার। Successful assistant answer deployment authorization নয়।

## প্রধান তথ্যসূত্র

- **রিপোজিটরির নিয়ন্ত্রণ:** [সুরক্ষিত শাখা](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)।
- **কর্মক্ষেত্রে প্রবেশাধিকার:** [Confluence-এর অনুমতি](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/)।
- **সরবরাহের নিয়ন্ত্রণ:** [Jira-এর অনুমতি-স্কিম](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/)。

## পরবর্তী ধাপ

**অনুপস্থিত নিয়ন্ত্রণ পর্যালোচনা করতে [কোর্স হাব](/ai-collaboration-course-start/)-এ ফিরুন।** আরেকটি পাইলট বাছার আগে [ফ্রেমওয়ার্ক নিবন্ধ](/articles/one-source-many-tools-ai-collaboration-framework/)-এর সঙ্গে আপনার বাস্তবায়ন তুলনা করুন।
