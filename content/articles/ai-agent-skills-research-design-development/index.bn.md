---
title: "গবেষণা, ডিজাইন ও ডেভেলপমেন্টের জন্য ৯টি AI Agent Skill প্রকল্প"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "ওয়ার্কফ্লো, হোস্ট সাপোর্ট, নির্ভরতা ও খরচ অনুযায়ী নয়টি agent skill প্রকল্প তুলনা করুন। আপনার প্রয়োজনীয় skill ইনস্টল, পরিদর্শন ও পরীক্ষা করতে শিখুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "ডেভেলপার টুল", "সফটওয়্যার ডেভেলপমেন্ট"]
tags: ["AI agent skills", "Codex skills", "Claude Code skills", "last30days", "Impeccable", "gstack", "Superpowers", "Claude Video", "Humanizer", "NVIDIA SkillSpector", "HyperFrames", "Remotion", "SKILL.md", "agent workflows", "skill installation", "skill security", "AI research", "frontend design", "video generation", "development workflows", "agent customization"]
cover: "/img/cover/agent-skill-workflow-library.webp"
coverAlt: "গাঢ় ডেস্কের উপর ম্যাগনিফাইং লেন্স, রঙের নমুনা ও ছোট ফিল্ম রিলের পাশে ট্রেতে রাখা হাতির দাঁতের রঙের নির্দেশনা কার্ড"
coverCaption: "কাজভিত্তিক agent skill library-এর ধারণামূলক চিত্র।"
---

**পুনরাবৃত্ত কাজ উন্নত করতে একটি agent skill ইনস্টল করুন।** বর্তমান আলোচনা গবেষণা, interface design পর্যালোচনা এবং video render-এর জন্য আলাদা প্রক্রিয়া ও নির্ভরতা লাগে। একটি কার্যকর skill এই কাজগুলোর একটির জন্য প্রয়োজনীয় নির্দেশনা, reference material বা script দেয়।

**নয়টি প্রকল্প বিবেচনার যোগ্য:** last30days, Humanizer, Impeccable, Superpowers, gstack, Claude Video, Remotion, HyperFrames এবং NVIDIA SkillSpector। কিছু instruction bundle, কিছু executable tool-সহ, আর কিছু companion skill-সহ framework। এই guide তাদের নথিভুক্ত ভূমিকা তুলনা করে এবং প্রয়োজনীয় skill বাছাই, ইনস্টল ও মূল্যায়নের ব্যবহারিক পদ্ধতি দেয়।

**Documentation snapshot: 10 October 2026.** সুপারিশ প্রকল্পের documentation ও source inspection-এর উপর ভিত্তি করে, output quality-এর comparative benchmark নয়। Free installation inference, rendering, data access বা commercial use free প্রমাণ করে না।

<!--more-->

## মূল শিক্ষা

- **পুনরাবৃত্ত কাজ দিয়ে শুরু করুন:** পরিষ্কার output ও acceptance check-সহ skill বাছুন।
- **Skill ও runtime আলাদা রাখুন:** instruction ইনস্টল করলে প্রয়োজনীয় সব executable ইনস্টল হয় না।
- **Host পরীক্ষা করুন:** কার্যকর Claude Code integration থেকে Codex বা Cowork-এর একই আচরণ প্রমাণ হয় না।
- **Permission ও dependency পরীক্ষা করুন:** package command, hook, external service ও credential আলাদা করে দেখুন।
- **পরীক্ষার পর customize করুন:** project policy-কে authoritative রাখুন এবং upstream version লিখে রাখুন।

## Deliverable অনুযায়ী বাছাই

| প্রয়োজনীয় output | মূল্যায়নের প্রকল্প | প্রথম পরীক্ষা |
|---|---|---|
| **সাম্প্রতিক আলোচনার brief** | last30days | কোন source ব্যবহারযোগ্য evidence দিয়েছে? |
| **সম্পাদিত prose** | Humanizer | অর্থ ও attribution কি টিকে আছে? |
| **উন্নত interface** | Impeccable | সংশোধিত interaction কি কাজ করে? |
| **পরিকল্পিত ও পরীক্ষিত change** | Superpowers | process কি task complexity-এর সঙ্গে মেলে? |
| **Review ও QA workflow** | gstack | আপনার agent host-এ কোন feature কাজ করে? |
| **Video observation** | Claude Video / Watch | frame বা audio কি claim সমর্থন করে? |
| **React video composition** | Remotion skills | exported video কি preview-এর সঙ্গে মেলে? |
| **HTML video composition** | HyperFrames skills | seek করার সময় animation কি deterministic? |
| **Skill inspection report** | SkillSpector | analysis কি সম্পূর্ণ, এবং কী flag হয়েছে? |

**Skill ও agent harness এক জিনিস নয়।** Skill task-specific guidance এবং কখনও script দেয়। Harness ঠিক করে agent কীভাবে instruction load করবে, tool call করবে ও permission enforce করবে। আমাদের [agent-harness comparison](/articles/best-ai-agent-harnesses/) এই surrounding system নিয়ে আলোচনা করে।

**Skill folder plugin installation-ও নয়।** Plugin hook বা অতিরিক্ত tool register করতে পারে, যা manual folder copy-তে থাকে না। সমতুল্য আচরণ ধরে নেওয়ার আগে আপনার host ও installation mode-এর instruction পড়ুন।

## Research ও writing

### last30days

**সাম্প্রতিক discussion research-এর জন্য last30days ব্যবহার করুন।** [Project](https://github.com/mvanhorn/last30days-skill) Reddit, Hacker News, YouTube, X ও web-এর মতো source একত্র করে। Available coverage নির্বাচিত source, installed tool, authentication ও provider access-এর উপর নির্ভর করে। Preflight mode পরিকল্পিত access বর্ণনা করে এবং research শুরু না করেই লেখে।

**Evidence trail চাইুন।** কার্যকর result-এ date, link, recurring complaint ও disagreement থাকে। unavailable source coverage gap হিসেবে দেখা উচিত। Engagement count সংগৃহীত post-এর activity বোঝায়, সব user-এর representative survey নয়।

**উদাহরণ task:** সম্প্রতি প্রকাশিত library-র recurring installation failure অনুসন্ধান করুন। Version ও operating system অনুযায়ী report group করুন, তারপর library issue tracker বা documentation দিয়ে proposed fix যাচাই করুন। জনপ্রিয় workaround-কে upstream-supported solution ধরে নেবেন না।

### Humanizer

**Editing pass হিসেবে Humanizer ব্যবহার করুন।** [Skill](https://github.com/blader/humanizer) repetitive contrast, staged introduction, inflated claim এবং অন্যান্য writing habit লক্ষ্য করে। এটি voice sample নেয় এবং underlying meaning বজায় রাখতে চায়।

**Draft-এর সঙ্গে constraint দিন।** Audience, থাকা আবশ্যক fact এবং কাছাকাছি থাকা আবশ্যক citation চিহ্নিত করুন। Edit-এর পর original-এর সঙ্গে factual claim তুলনা করুন। Better rhythm unsupported statistic validate করে না।

| Writing check | Passing result |
|---|---|
| **Meaning** | একই claim, qualification ও scope |
| **Sources** | উদ্ধৃত findings-এর কাছে attribution থাকে |
| **Voice** | intended reader ও supplied example-এর সঙ্গে মেলে |
| **Originality** | copied prose ঢাকার বদলে independent reasoning যোগ করে |

**ভিন্ন stage-এ এই project ব্যবহার করুন।** last30days investigation material সংগ্রহ করে। Humanizer expression edit করে। কোনোটিই source verification বা independent authorship-এর বিকল্প নয়।

## Interface ও development work

### Impeccable

**Focused design work-এর জন্য Impeccable ব্যবহার করুন।** এর [website](https://impeccable.style/) ও [repository](https://github.com/pbakaus/impeccable) critique, typography, layout, clarity, motion ও polish-সহ design workflow document করে। অস্পষ্টভাবে impressive page চাইবার বদলে নির্দিষ্ট user problem দিয়ে শুরু করুন।

**উদাহরণ brief:** cancellation না লুকিয়ে বা keyboard navigation না বদলে subscription settings page সহজে scan করার মতো করুন। আগে critique চান, তারপর নির্বাচিত change implement করুন। পরে mobile layout, focus order, contrast ও original task completion পরীক্ষা করুন।

**Installation mode গুরুত্বপূর্ণ।** বর্তমান Codex instruction skill ও project-local design hook আলাদা করে। Hook trust-এর জন্য Codex-এ আলাদা approval লাগে। Copied skill folder active hook প্রমাণ করে না।

### Superpowers

**Structured development process-এর জন্য Superpowers ব্যবহার করুন।** এর [repository](https://github.com/obra/superpowers) brainstorming, planning, testing, debugging ও review workflow package করে। Codex-সহ host-specific plugin installation-ও document করে।

**Assignment অনুযায়ী process মিলিয়ে নিন।** data storage, UI ও test-জুড়ে feature হলে explicit plan উপকারী। Spelling correction-এর জন্য অনেক কম ceremony লাগে। Authorized scope নির্ধারণ করুন, যাতে general development workflow ছোট request-কে adjacent work-এ না বাড়ায়।

**Project instruction প্রযোজ্য থাকে।** Skill-এর preferred testing method, worktree approach বা delegation pattern repository ও user request-এর সঙ্গে মানানসই হতে হবে। Methodology install করলে তার সব action-এর অনুমতি মেলে না।

### gstack

**Executable tooling-সহ বিস্তৃত engineering workflow-এর জন্য gstack ব্যবহার করুন।** [Documentation](https://github.com/garrytan/gstack)-এ planning, review, browser QA, investigation ও release-oriented skill আছে। Installation শুধু prose copy না করে supporting tool তৈরি করে।

**Codex support এখন experimental।** Project Claude Code-এর hook-enforced safety feature এবং Codex-এর advisory behavior আলাদা করে। একই নামের command host জুড়ে একই enforcement দেয় ধরে নেবেন না।

**আমার selection rule:** missing piece যদি repeatable development process হয়, Superpowers trial করুন। নির্দিষ্ট review বা browser tool বর্তমান need মেটালে gstack trial করুন। দুটোই ইনস্টল থাকলে প্রতি task-এ একটিকে primary workflow করুন এবং অন্যটিকে named contribution-এর জন্য ব্যবহার করুন।

| Development problem | Useful evaluation task |
|---|---|
| **অস্পষ্ট scope** | acceptance criteria-সহ bounded plan তৈরি করুন |
| **ভঙ্গুর implementation** | seeded regression ঠিক করে existing behavior রাখুন |
| **ভাঙা interaction** | browser failure reproduce করে evidence রাখুন |
| **বিরোধী workflow** | কেবল selected process task নির্দেশ করছে নিশ্চিত করুন |

## Video evidence ও production

### Claude Video / Watch

**Video থেকে evidence সংগ্রহে Claude Video ব্যবহার করুন।** Repository name সত্ত্বেও [Watch skill](https://github.com/bradautomates/claude-video) Codex-এর মতো local agent support করে। Local route download, sampled frame ও caption বা transcription ব্যবহার করে। Configured থাকলে আলাদা Gemini route analysis-এর জন্য video পাঠায়।

**বর্তমান host support পরীক্ষা করুন।** README Claude Chat ও Cowork-কে unsupported বলে। Local execution-এ FFmpeg ও yt-dlp-এর মতো media tool লাগে, এবং প্রতিটি website access limit দিতে পারে।

**Visual ও audio claim আলাদা রাখুন।** Transcript spoken word support করে। Frame sampled time-এর visible detail support করে। কোনোটিই sample-এর মাঝের unseen event প্রমাণ করে না। পুরো recording বুঝেছি এমন unqualified claim-এর বদলে timestamp ও unresolved observation চাইুন।

### Remotion

**React-এ লেখা video composition-এর জন্য Remotion ব্যবহার করুন।** [Framework repository](https://github.com/remotion-dev/remotion) আলাদা [agent-skills collection](https://www.remotion.dev/docs/ai/skills)-এ নির্দেশ করে। Collection project creation, markup, map, caption, Studio ও rendering cover করে। Collection install করলে video project তৈরি বা সব project dependency install হয় না।

**Skill download থেকে আলাদাভাবে license পরীক্ষা করুন।** [Remotion pricing page](https://www.remotion.dev/docs/license/pricing) তিনজন পর্যন্ত individual ও company-এর জন্য free license এবং বড় company ও নির্দিষ্ট collaboration-এর জন্য company license তালিকাভুক্ত করে। আপনার use case-এর current term পরীক্ষা করুন।

### HyperFrames

**HTML-based video composition-এর জন্য HyperFrames ব্যবহার করুন।** [Repository](https://github.com/heygen-com/hyperframes) HTML, CSS, media ও seekable animation MP4-তে render করা বর্ণনা করে। Published skill composition, preview, validation ও rendering guide করে।

**Documented core set দিয়ে শুরু করুন।** Current installation guidance core skill, larger published collection ও repository-internal skill আলাদা করে। প্রতিটি folder indiscriminately install করলে unrelated instruction বাড়ে এবং maintenance কঠিন হয়।

| Video workflow | গুরুত্বপূর্ণ acceptance check |
|---|---|
| **Watch** | timestamped observation inspected media-এর সঙ্গে মেলে |
| **Remotion** | final export timing, font, audio ও layout রাখে |
| **HyperFrames** | frame seek করলে intended visual state পাওয়া যায় |

**Controlled sample দিয়ে বাছুন।** Remotion ও HyperFrames-কে একই brief, asset, duration ও output dimension দিন। উদাহরণ হিসেবে caption ও একটি diagram-সহ তিন ধাপের maintenance procedure animate করুন। Exported file, editing effort ও render failure তুলনা করুন। একটি আকর্ষণীয় demo সাধারণ winner প্রমাণ করে না।

## SkillSpector দিয়ে পরিদর্শন

```bash
skillspector scan ./downloaded-skill --no-llm --format json --output report.json
```

**NVIDIA SkillSpector scanner, video বা writing skill নয়।** [Project](https://github.com/NVIDIA/SkillSpector) agent skill package-এর static check ও optional model-assisted analysis document করে। উপরকার command ধরে নেয় CLI আগে ইনস্টল করা আছে এবং target skill execute না করে local folder scan করে।

**Finding ও coverage একসঙ্গে পড়ুন।** Flagged file ও surrounding code inspect করুন, তারপর কোন check complete হয়েছে লিখুন। Incomplete scan clean verdict হওয়া উচিত নয়। Keyword hit-এরও context লাগে, provider-এর documented public map token এবং unrelated credential সংগ্রহ করা code এক নয়।

**Static-only মানে fully offline নয়।** Project অনুযায়ী `--no-llm`-সহ vulnerability lookup-এর জন্য dependency name ও version OSV-তে যায়। Model analysis চালু করলে eligible file content configured provider-এ যায়। Review material অনুযায়ী mode বাছুন।

**Decision-এর evidence হিসেবে report ব্যবহার করুন।** প্রতিটি finding stated task-এর জন্য প্রয়োজনীয় কি না, কোন data machine ছাড়ে এবং runtime কোন authority দেয় ব্যাখ্যা করুন। Low score safety প্রমাণ করে না, reputation unexplained finding মুছে দেয় না।

## সঠিক package ইনস্টল করুন

**প্রথমে canonical skill distribution চিহ্নিত করুন।** Remotion framework ও skill আলাদা repository-তে থাকে। Claude Video Watch নামে skill দেয়। SkillSpector CLI হিসেবে install হয়, agent integration আলাদা। তাই project clone করলেই সবসময় যথেষ্ট হয় না।

**নিচের example command project-এর current installation documentation থেকে এসেছে।** Selected project-এর command-ই চালান। Package runner installer code download ও execute করে, তাই চালানোর আগে upstream project inspect এবং installation scope নির্বাচন করুন।

```bash
# Humanizer: user-wide Codex installation
npx skills add blader/humanizer --global --agent codex

# last30days: user-wide Codex installation
npx skills add mvanhorn/last30days-skill -g -a codex

# Remotion: official skill collection, not the framework repository
npx skills add remotion-dev/skills
```

**তৃতীয় command installer workflow খোলে।** উপরকার explicitly scoped command-এর default একই ধরে না নিয়ে intended agent ও scope নির্বাচন করুন। Plugin installer ও standalone folder install-এর update mechanism-ও আলাদা।

**Existing installation রাখুন।** Skill replace করার আগে version, local change ও manager পরীক্ষা করুন। Host কীভাবে resolve করে document না করলে user, project ও plugin location-এ competing copy রাখবেন না।

| Installation state | যা প্রমাণ করে |
|---|---|
| **File present** | instruction ও referenced asset আছে |
| **Host discovers skill** | agent name ও description চিনতে পারে |
| **Dependency ready** | required executable ও package available |
| **Task verified** | representative result independent check পাস করে |

**প্রতিটি stage ক্রমে verify করুন।** Successful folder copy installation check, working browser, download, transcription বা render-এর evidence নয়। Optional provider setup basic installation থেকে আলাদা রাখুন এবং skill file-এ credential রাখবেন না।

**প্রতিটি trial-এর host ও revision লিখুন।** Skill Claude Code, Codex, Cowork বা অন্য host দিয়ে চলে কি না লিখুন। Acceptance result-এর সঙ্গে upstream commit বা package version রাখুন। একই রকম skill name identical discovery, hook, permission বা tool access প্রমাণ করে না।

## Customize করার আগে test করুন

**একটি saved task baseline হিসেবে ব্যবহার করুন।** New skill ছাড়া task চালান, তারপর skill-সহ চালান। সম্ভব হলে model, input, tool ও acceptance criteria একই রাখুন। Failure ও human correction final result-এর সঙ্গে record করুন।

```yaml
# Illustrative evaluation record, not a skill configuration schema
job: "review a settings page"
input: "same source revision and test data"
variants:
  - "agent without the selected skill"
  - "same agent with the selected skill"
acceptance:
  - "required actions remain visible"
  - "keyboard navigation works"
  - "mobile layout remains usable"
record:
  - "skill source and revision"
  - "model and enabled tools"
  - "completed checks and retained evidence"
  - "elapsed time and manual corrections"
  - "external service usage"
```

**পুরো package নয়, recurring failure customize করুন।** Research summary conflicting evidence হারালে dissenting source রাখার requirement যোগ করুন। Design pass established color বদলালে design token দেখান। Video caption overflow হলে export-resolution check যোগ করুন।

**Local addition traceable রাখুন।** Upstream revision, আপনার change ও যে task এটি ঘটিয়েছে লিখুন। নতুন trigger, script বা dependency আগের evaluated workflow বদলায়, তাই update-এর পর আবার trial করুন।

**Overlapping instruction লক্ষ্য করুন।** Development suite, design skill ও prose editor সবাই preference দেয়। Repository rule ও user request conflict মেটাবে। Style skill accessibility label, citation বা technical term সরাবে না শুধু wording বদলানোর জন্য।

## কার্যকর library তৈরি করুন

**যে কাজ সবচেয়ে বেশি repeat হয় তা দিয়ে শুরু করুন।** Writer last30days ও Humanizer trial করতে পারে। Frontend developer Impeccable ও একটি development workflow দিয়ে শুরু করতে পারে। Video producer-এর source-video analysis প্রয়োজন হলে production framework বেছে Watch যোগ করা উচিত।

**Installation থেকে operation cost আলাদা হিসাব করুন।** Model call, optional search provider, transcription, media generation, rendering infrastructure ও applicable license ধরুন। Free repository cost-এর এক অংশের উত্তর দেয়।

**প্রথম trial-এর আগে:** approved model access, disposable project বা sample input এবং written acceptance criteria প্রস্তুত করুন। Basic instruction skill beginner-এর জন্য সহজ। Browser tooling, media dependency ও cloud rendering বেশি setup চায়। প্রথমে একটি bounded trial-এর জন্য এক ঘণ্টা দিন, তারপর workflow routine করার আগে representative input দিয়ে repeat করুন।

**প্রমাণিত value-র skill রাখুন।** Missed step বা review effort কমায় এমন skill রাখুন, conflicting behavior যোগ করা duplicate সরান। Agent environment বদলালে host compatibility ও dependency আবার দেখুন।

{{< youtube id="3fdb_giOrLo" enable="true" title="9 Free AI Agent Skills You NEED to Install Now" >}}

## Reference

- [last30days: research skill and installation](https://github.com/mvanhorn/last30days-skill)
- [Humanizer: writing skill](https://github.com/blader/humanizer)
- [Impeccable: design workflow](https://impeccable.style/)
- [Impeccable: repository and host-specific setup](https://github.com/pbakaus/impeccable)
- [Superpowers: development skills](https://github.com/obra/superpowers)
- [gstack: engineering tools and host support](https://github.com/garrytan/gstack)
- [Claude Video: Watch skill and runtime requirements](https://github.com/bradautomates/claude-video)
- [Remotion: React video framework](https://github.com/remotion-dev/remotion)
- [Remotion: agent skills](https://www.remotion.dev/docs/ai/skills)
- [Remotion: licensing and pricing](https://www.remotion.dev/docs/license/pricing)
- [HyperFrames: framework and skill distribution](https://github.com/heygen-com/hyperframes)
- [NVIDIA SkillSpector: scanner behavior and data handling](https://github.com/NVIDIA/SkillSpector)
- [Futurepedia: 9 Free AI Agent Skills You NEED to Install Now](https://www.youtube.com/watch?v=3fdb_giOrLo)
