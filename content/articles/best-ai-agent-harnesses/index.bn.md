---
title: "২০২৬ সালের সেরা AI এজেন্ট হারনেস: কাজের ধরন অনুযায়ী বেছে নিন"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "টুল এক্সিকিউশন, মেমরি, পুনরুদ্ধার এবং ইন্টিগ্রেশন প্রচেষ্টার ভিত্তিতে Deep Agents, Claude Agent SDK, OpenAI Agents SDK, Pydantic AI, Pi এবং LangGraph তুলনা করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "সফটওয়্যার ডেভেলপমেন্ট", "AI নিরাপত্তা"]
tags: ["AI এজেন্ট হারনেস", "সেরা এজেন্ট ফ্রেমওয়ার্ক", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "Pi কোডিং এজেন্ট", "LangGraph", "এজেন্ট রানটাইম", "টুল কলিং", "এজেন্ট মেমরি", "কনটেক্সট ম্যানেজমেন্ট", "ডিউরেবল এক্সিকিউশন", "এজেন্ট পারমিশন", "AI এজেন্ট নিরাপত্তা", "লোকাল AI এজেন্ট", "এজেন্ট মূল্যায়ন", "হিউম্যান ইন দ্য লুপ", "এজেন্ট SDK তুলনা", "প্রোডাকশন এজেন্ট"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "অন্ধকার কাজের পৃষ্ঠে টিল ও কমলা পথ দিয়ে একটি উজ্জ্বল কেন্দ্রীয় প্রসেসরের সঙ্গে যুক্ত মডিউলার ধাতব উপাদান"
coverCaption: "একটি AI মডেলকে ঘিরে থাকা উপাদানগুলোর ধারণাগত চিত্র।"
---

**কনফিগারযোগ্য মডেল ও বিল্ট-ইন কনটেক্সট ম্যানেজমেন্টসহ সাধারণ কাজের এজেন্টের জন্য Deep Agents আমার প্রথম পছন্দ।** Claude Code-এর এক্সিকিউশন আচরণ অ্যাপ্লিকেশনে বসাতে Claude Agent SDK উপযুক্ত। অ্যাপ্লিকেশন-নির্দিষ্ট এজেন্টের জন্য OpenAI Agents SDK এবং Pydantic AI পরীক্ষা করা উচিত। Pi একটি ছোট এক্সটেনসিবল কোরকে অগ্রাধিকার দেয়, আর LangGraph স্পষ্ট ওয়ার্কফ্লো নিয়ন্ত্রণকে অগ্রাধিকার দেয়।

**সেরা পছন্দ নির্ভর করে আপনি কোন কাজ গ্রহণ করবেন তার ওপর।** গবেষণা সহকারী, রিপোজিটরি এডিটর এবং গ্রাহকের অনুরোধ প্রক্রিয়াকরণকারী সার্ভিসের জন্য আলাদা টুল ও পুনরুদ্ধার নিয়ম লাগে। এগুলো ১০ অক্টোবর ২০২৬ তারিখে পরীক্ষা করা অফিসিয়াল ডকুমেন্টেশনভিত্তিক সম্পাদকীয় মতামত, হাতে-কলমে পারফরম্যান্স বেঞ্চমার্কের ফল নয়।

<!--more-->

## মূল বিষয়

- **আগে abstraction বেছে নিন:** assembled agent, application SDK, অথবা workflow runtime।
- **এক্সিকিউশন সীমা পরীক্ষা করুন:** টুল অনুমোদন, ফাইলসিস্টেম আইসোলেশন এবং নেটওয়ার্ক নীতি আলাদা সমস্যা সমাধান করে।
- **পুনরুদ্ধার পরীক্ষা করুন:** শুধু কথোপকথনের ইতিহাস বাহ্যিক কাজের পুনরাবৃত্তি ঠেকায় না।
- **গৃহীত কাজ মাপুন:** খরচ তুলনায় ব্যর্থতা, পর্যালোচনার সময় এবং অবকাঠামো রাখুন।
- **মডেল স্পষ্ট রাখুন:** মডেল ও এজেন্ট সফটওয়্যার দুটো বদলালে সফটওয়্যার নয়, পুরো সিস্টেম পরীক্ষা হয়।

## একটি হারনেস কী দেয়

একটি **এজেন্ট হারনেস হলো মডেল কলকে ঘিরে থাকা সফটওয়্যার।** এটি কনটেক্সট প্রস্তুত করে, টুল প্রকাশ করে, অনুমোদিত কাজ চালায়, ফলাফল ফেরত দেয় এবং কখন চলবে বা থামবে তা ঠিক করে। বাস্তবায়ন অনুযায়ী এটি মেমরি, delegation, permission এবং recovery-ও পরিচালনা করে।

একটি **মডেল** পরবর্তী কাজ প্রস্তাব করে। একটি **টুল** কাজটি সম্পন্ন করে। একটি **রানটাইম** ওয়ার্কফ্লো চালায় এবং সংরক্ষণ করে। প্যাকেজ করা পণ্যে এই দায়িত্বগুলো মিশে থাকে, কিন্তু আলাদা করলে কোন ক্ষমতা অনুপস্থিত তা বোঝা সহজ হয়।

| উপাদান | যে প্রশ্নটি করবেন |
|---|---|
| **কনটেক্সট ম্যানেজমেন্ট** | দীর্ঘ রানেও কোন প্রয়োজনীয়তা টিকে থাকে? |
| **টুল এক্সিকিউশন** | আর্গুমেন্ট যাচাই ও ক্ষমতার সীমা কে নির্ধারণ করে? |
| **স্টেট স্টোরেজ** | প্রসেস পুনরায় চালু হলে কোন তথ্য থাকে? |
| **ভেরিফিকেশন** | কাজ শেষ হওয়ার প্রমাণ কী? |

একটি **উদাহরণভিত্তিক সাপোর্ট এজেন্ট** একটি অর্ডার পরীক্ষা করে প্রতিস্থাপন অনুরোধ তৈরি করবে। অর্ডার পড়া, প্রতিস্থাপনের প্রস্তাব এবং তা জমা দেওয়ার আলাদা ক্ষমতা থাকা উচিত। বিশ্বাসযোগ্য ব্যাখ্যা জমা দেওয়ার অনুমতি প্রমাণ করে না, আর সংরক্ষিত ট্রান্সক্রিপ্টও জমা দেওয়া হয়েছে কি না প্রমাণ করে না।

**পরিধি:** এই গাইড embed করা যায় এমন সফটওয়্যার ও রানটাইম পছন্দ তুলনা করে। প্রতিদিনের ডেভেলপার ইন্টারফেসের জন্য আলাদা [CLI coding-agent comparison](/articles/cli-coding-agents-comparison/) অথবা [GUI coding-agent comparison](/articles/gui-coding-agents-comparison/) ব্যবহার করুন। SDK তুলনা যেন নীরবে টার্মিনাল টুল ও এডিটর এক্সটেনশনের র‍্যাঙ্কিংয়ে পরিণত না হয়।

## ব্যবহারিক সংক্ষিপ্ত তালিকা

| প্রাথমিক প্রয়োজন | প্রথমে যে বিকল্পটি পরীক্ষা করবেন | যে মূল দায়িত্ব আপনার থাকবে |
|---|---|---|
| **সাধারণ কাজের এজেন্ট** | Deep Agents | backend, permission এবং model কনফিগার করা |
| **অ্যাপের মধ্যে Claude Code** | Claude Agent SDK | execution process চালানো ও isolate করা |
| **অ্যাপ্লিকেশন টুল ওয়ার্কফ্লো** | OpenAI Agents SDK | tool, approval এবং acceptance সংজ্ঞায়িত করা |
| **Typed Python application** | Pydantic AI এবং তার Harness package | capability ও workspace বাছাই করা |
| **ন্যূনতম embeddable coding core** | Pi SDK | extension ও execution policy একত্র করা |
| **স্পষ্ট durable workflow** | LangGraph | graph state ও recovery behavior ডিজাইন করা |

**এগুলো আলাদা শুরুর বিন্দু।** Deep Agents ইতিমধ্যে LangGraph ব্যবহার করে, তাই সেটি বেছে নেওয়া সবসময় either-or সিদ্ধান্ত নয়। Pydantic AI-ও তার মূল agent framework এবং assembled harness capability আলাদা রাখে। প্রতিটি সারিকে বিনিময়যোগ্য library ভাবার বদলে কতটা application code আপনার মালিকানায় থাকবে তা তুলনা করুন।

**Acceptance test পূরণ করা সবচেয়ে ছোট layer দিয়ে শুরু করুন।** সীমিত tool call-এর জন্য typed application framework, উন্মুক্ত file বা research কাজের জন্য assembled agent এবং recovery ও transition-এর named state দরকার হলে explicit graph ব্যবহার করুন। সহজ layer কেন ব্যর্থ হয় তা test দেখানোর পর memory, shell access বা subagent যোগ করুন।

## Deep Agents: assembled capability

**ফাইল, টুল এবং দীর্ঘ কথোপকথনে কাজ করা এজেন্টের জন্য আগে Deep Agents বেছে নিন।** এর [official overview](https://docs.langchain.com/oss/python/deepagents/overview) filesystem backend, context offloading, summarization, subagent এবং human approval নথিবদ্ধ করে। এটি LangChain এবং LangGraph runtime-এর ওপর তৈরি, আর একাধিক model provider-এর integration দেয়।

**Configuration এখনও আচরণ নির্ধারণ করে।** বর্তমান documentation অনুযায়ী version 0.7 থেকে task planning opt-in। পুরনো release-এর tutorial বর্তমান default বর্ণনা করে ধরে নেবেন না। Evaluation-এ package version ও enabled middleware লিখে রাখুন।

**Permission scope সতর্কভাবে পরীক্ষা করুন।** Documented filesystem rule built-in file tool কভার করে, sandbox backend-এর মাধ্যমে arbitrary shell command নয়। অন্য execution path একই file-এ পৌঁছালে file-tool denial যথেষ্ট নয়। Backend ও shell boundary একসঙ্গে test করুন।

**আমার সুপারিশ:** provider choice ও assembled capability দরকার হলে document-analysis বা repository-work service-এর shortlist-এ রাখুন। কাজ যদি দুটি নির্দিষ্ট API call ও validated response-এ সীমিত থাকে, ছোট starting point নিন। অতিরিক্ত tool মূল্যায়নের জন্য অতিরিক্ত behavior আনে।

## Claude: embedded execution

**আপনার application-এর ভেতরে Claude Code-এর agent চাইলে Claude Agent SDK বেছে নিন।** Anthropic-এর বর্ণনা অনুযায়ী Python ও TypeScript library-টি Claude Code-এর একই execution loop, tool এবং context management ব্যবহার করে। SDK আপনার পরিচালিত একটি process-এ Claude Code binary চালায়। এটি Anthropic-এর basic API client এবং hosted Managed Agents থেকে আলাদা। [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)।

**মূল আকর্ষণ হলো বিদ্যমান execution system পুনরায় ব্যবহার।** File operation, command, hook, permission, session ও subagent documented capability হিসেবে আসে। আপনার integration application boundary এবং task-specific acceptance check দেয়।

**Hosting একটি engineering decision।** Anthropic-এর [deployment guidance](https://code.claude.com/docs/en/agent-sdk/secure-deployment) filesystem control, network restriction এবং isolation নিয়ে আলোচনা করে। Permission prompt-কে operating-system boundary না ভেবে process-এর চারপাশে এগুলো configure করুন।

**আমার সুপারিশ:** Claude-কেন্দ্রিক document বা coding automation-এ file ও command কাজ বেশি হলে এটি মূল্যায়ন করুন। Local model এবং একাধিক hosted provider তুলনা product requirement হলে provider-flexible alternative বেছে নিন।

| Assembled option | Integration emphasis |
|---|---|
| **Deep Agents** | model selection, middleware ও backend configuration |
| **Claude Agent SDK** | application process-এর মধ্যে Claude Code execution |

## OpenAI: application tool workflow

**Function, delegated task ও explicit output-কেন্দ্রিক application-এর জন্য OpenAI Agents SDK বেছে নিন।** এর [overview](https://openai.github.io/openai-agents-python/) agent loop, handoff, guardrail, tracing ও sandbox-agent capability নথিবদ্ধ করে। SDK builder interface, Codex developer application নয়।

**Approval configurable behavior।** [Human-in-the-loop guide](https://openai.github.io/openai-agents-python/human_in_the_loop/) decision-এর পর interrupted run এবং resume করার serialized state বর্ণনা করে। Local shell ও patch tool-এর approval opt-in। শুধু approval callback যোগ করলে approval requirement সক্রিয় হয় না।

**Model support OpenAI-এর বাইরেও যায়।** [Provider documentation](https://openai.github.io/openai-agents-python/models/) external-provider integration point ও adapter বর্ণনা করে। Selected endpoint-এর structured output, tool calling ও transport support যাচাই করুন। Feature parity ধরে নেবেন না।

**আমার সুপারিশ:** কার্যকর action-গুলো well-defined application function হিসেবে আগে থেকেই থাকলে service-এর shortlist-এ রাখুন। যেমন order আনুন, ordinary code-এ eligibility হিসাব করুন এবং structured request প্রস্তুত করুন। Model পরের tool বেছে নিলেও authorization ও eligibility check application-এ রাখুন।

## Pydantic AI: typed application

**Python type এবং validated output application-এর কেন্দ্রে থাকলে Pydantic AI বেছে নিন।** এর [core documentation](https://pydantic.dev/docs/ai/overview/) typed tool, dependency injection, structured output ও durable-execution integration কভার করে। Validation output-এর required structure নিশ্চিত করে। প্রতিটি field সত্য কি না তা নিশ্চিত করে না।

**আলাদা Harness package assembled capability যোগ করে।** এর [documentation](https://pydantic.dev/docs/ai/harness/) Coder ও Researcher stack, filesystem ও shell access, memory এবং workspace integration অন্তর্ভুক্ত করে। Local workspace এবং isolated sandbox আলাদা execution choice। Relevant harness capability workspace চায়, নীরবে একটি workspace নির্বাচন করে না।

**আমার সুপারিশ:** typed record ফেরত দেওয়া Python service-এর জন্য core framework shortlist করুন। Task-এর workspace exploration বা open-ended research দরকার হলে harness capability যোগ করুন। এতে bounded extraction service নির্দিষ্ট প্রয়োজন ছাড়া shell access পাবে না।

একটি **উদাহরণ invoice-review agent**-এর জন্য schema validation দেখে total numeric কি না এবং currency অনুমোদিত set-এ আছে কি না। আলাদা application logic total-কে line item-এর সঙ্গে তুলনা করে এবং source evidence যাচাই করে। Trial-এ দুটো check-ই রাখুন।

| Application concern | Acceptance check |
|---|---|
| **Structured output** | field validate করুন এবং meaning স্বাধীনভাবে যাচাই করুন |
| **Approval pause** | exact pending action ও decision persist করুন |
| **Provider change** | tool-call ও output compatibility test পুনরায় চালান |

## Pi: ছোট extensible core

**Compact coding-agent implementation-এ সরাসরি নিয়ন্ত্রণ চাইলে Pi SDK বেছে নিন।** [Project documentation](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) interactive interface-এর পাশাপাশি SDK ও RPC integration বর্ণনা করে। Default tool set reading, writing, editing এবং shell execution নিয়ে গঠিত। Extension অতিরিক্ত behavior দেয়।

**Minimalism integrator-এর কাজ বাড়ায়।** Pi ইচ্ছাকৃতভাবে built-in permission popup ও subagent orchestration বাদ দেয়। Confirmation flow-এর জন্য documentation container বা custom extension ব্যবহারের নির্দেশ দেয়। এখানে embedded SDK মূল্যায়ন করুন, অন্য vendor-এর graphical editor-এর সঙ্গে terminal interface তুলনা করবেন না।

**আমার সুপারিশ:** bespoke coding service-এ execution restriction, extension review ও recovery policy নিজের দায়িত্বে নিতে প্রস্তুত থাকলে Pi shortlist করুন। ছোট core behavior বোঝা ও বদলানোর জন্য সুবিধাজনক। Built-in approval ও orchestration system প্রধান প্রয়োজন হলে এটি কম উপযুক্ত starting point।

## LangGraph: explicit workflow control

**Workflow-এর explicit state ও transition দরকার হলে LangGraph বেছে নিন।** [Persistence documentation](https://docs.langchain.com/oss/python/langgraph/persistence) thread-scoped checkpoint ও cross-thread store আলাদা করে। Persistent checkpointer process restart-এর পর recovery সমর্থন করে। In-memory checkpointer করে না।

**LangGraph একটি runtime foundation।** আপনি workflow সংজ্ঞায়িত করেন এবং model-driven behavior কোথায় থাকবে ঠিক করেন। Deep Agents এই foundation ব্যবহার করে, তাই execution path-এ সরাসরি নিয়ন্ত্রণ বেশি দরকার হলে LangGraph-এ নামা যুক্তিসঙ্গত।

**আমার সুপারিশ:** named stage, review pause এবং পৃথক recovery rule থাকা process-এর জন্য shortlist করুন। একটি document-intake workflow field extract, validate, review request এবং approved record publish করতে পারে। Model content বেছে নেবে কিন্তু business process বানাবে না, এমন অবস্থায় fixed transition উপযোগী।

| Workflow stage | Completion evidence |
|---|---|
| **Extract** | source-linked candidate record |
| **Validate** | deterministic check ও exception |
| **Review** | নির্দিষ্ট candidate-এর সঙ্গে যুক্ত decision |
| **Publish** | operation-এর বিপরীতে record করা external receipt |

**External effect-এর নিজস্ব recovery design দরকার।** Graph state save করলেই remote service transaction checkpoint-এর সঙ্গে atomic হয় না। Operation identifier ব্যবহার করুন এবং submission আবার করার আগে external result reconcile করুন।

## অনুপস্থিত অংশ পরীক্ষা করুন

**Feature list কেবল শুরু।** আপনার workload-এর মতো failure-এর মধ্য দিয়ে প্রতিটি candidate চালান। Disposable workspace ব্যবহার করুন এবং synthetic record দিয়ে service পরীক্ষা করুন।

| Test | যে evidence রাখবেন |
|---|---|
| **Interrupted submission** | recovery-এর পর একটি external effect |
| **Long conversation** | original requirement এখনও পূরণ |
| **Rejected action** | alternate tool দিয়ে কোনও effect নয় |
| **Untrusted document instruction** | document text authority পায় না |
| **Malformed tool arguments** | application mutation-এর আগে rejection |
| **Budget exhaustion** | inspectable partial work-সহ bounded stop |

**Repetition স্পষ্টভাবে নির্ধারণ করুন।** Replacement-request service-এ test service request accept করার পর, local completion save হওয়ার আগে worker থামান। Restart-এর পর workflow operation identifier খুঁজবে, অন্ধভাবে আবার submit করবে না। এটি proposed test, তালিকাভুক্ত product-এর observed result নয়।

**Compaction-এর পর evidence পরীক্ষা করুন।** Task-এর শুরুতে গুরুত্বপূর্ণ requirement রাখুন, তারপর configured context strategy সক্রিয় করার মতো বাস্তব উপাদান দিন। Agent-কে final artifact ও supporting source reference দিতে বলুন। [CLM and agent-memory analysis](/articles/context-language-models-agent-memory-hallucinations/) ব্যাখ্যা করে কেন note রাখা আর accurate evidence রাখা আলাদা বিষয়।

**Telemetry destination review করুন।** Tool trace ও memory store-এ task data থাকতে পারে। কোন system তা পায় এবং কতদিন রাখে লিখে রাখুন। Local model inference মানেই local-only logging, retrieval বা execution নয়।

## প্রতি গৃহীত task-এর খরচ তুলনা করুন

**দুটি evaluation track ব্যবহার করুন।** Controlled comparison-এ যেখানে সমর্থিত সেখানে model, tool, task set ও budget স্থির রাখুন। Deployment comparison প্রতিটি candidate-এর intended configuration ব্যবহার করে। প্রথমটি কিছু software effect আলাদা করে। দ্বিতীয়টি আপনার কাজের জন্য কোন complete setup ভালো তা বলে।

**Controlled track-এ unsupported configuration জোর করে দেবেন না।** দুই candidate-এর common model বা tool interface না থাকলে comparison-কে system evaluation হিসেবে report করুন। Setup effort ও human steering record-এ রাখুন।

```yaml
# Illustrative trial record, not a framework configuration file
candidate: "package and pinned version"
model: "provider and exact model identifier"
workspace: "isolated test environment"
task_set: "frozen fixtures and acceptance checks"
limits:
  elapsed_minutes: 15
  model_calls: 30
  tool_calls: 60
record:
  - accepted_result
  - unsupported_claims
  - duplicate_external_actions
  - inference_cost
  - infrastructure_cost
  - human_review_minutes
  - recovery_outcome
```

**প্রতিটি task-এ একাধিক trial চালান।** Unsuccessful attempt denominator-এ রাখুন এবং percentage-এর সঙ্গে raw count report করুন। ছোট trial failure pattern দেখায়, স্থিতিশীল industry ranking নয়।

**Illustrative cost calculation:** ধরুন setup A দশটি attempt-এ 12 ডলার খরচ করে এবং আটটি accepted result দেয়। প্রতি accepted task-এ inference cost 1.50 ডলার। Setup B 8 ডলার খরচ করে চারটি accepted result দেয়, তাই সংশ্লিষ্ট cost 2.00 ডলার। Human review বা infrastructure কোনও সংখ্যায় নেই। এগুলো আলাদা recorded total-এ থাকবে।

**Testing-এর আগে disqualifying failure ঠিক করুন।** Unauthorized submission বা cross-user data leak average quality score-এর মধ্যে হারিয়ে যাওয়া উচিত নয়। Requirement enforce করার পর correctness, recovery, review effort ও cost তুলনা করুন।

## সীমিত সিদ্ধান্ত নিন

**দুটি candidate এবং একটি বাস্তব workflow দিয়ে শুরু করুন।** Assembled provider-flexible agent-এর জন্য Deep Agents-কে application-উপযোগী narrower alternative-এর সঙ্গে তুলনা করুন। Service-এর মধ্যে Claude Code behavior চাইলে Claude Agent SDK trial করুন। Typed application কাজের জন্য Pydantic AI এবং OpenAI Agents SDK তুলনা করুন। Custom behavior-এর অতিরিক্ত integration work সার্থক হলে Pi বেছে নিন, explicit workflow control priority হলে LangGraph বেছে নিন।

**Trial-এর prerequisites:** approved model access, synthetic fixture, প্রয়োজনে isolated workspace এবং লিখিত acceptance criteria। প্রথম বিকেল setup ও basic failure test-এ দিন। Production decision-এর আগে repeated run সংগ্রহ করুন। External action ও recovery requirement অনুযায়ী difficulty intermediate থেকে advanced।

**আপনার requirements পূরণ করা সবচেয়ে ছোট system নির্বাচন করুন।** Trial fixture, package version ও failure record রাখুন। Model, context strategy, tool বা execution backend বদলালে আবার চালান। এই পরিবর্তনগুলো evaluated system বদলে দেয়।

## References

- [LangChain: Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic: Claude Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [Anthropic: Secure deployment](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [OpenAI: Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI: Human-in-the-loop execution](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [OpenAI: Model and provider integration](https://openai.github.io/openai-agents-python/models/)
- [Pydantic: AI framework overview](https://pydantic.dev/docs/ai/overview/)
- [Pydantic: AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Earendil: Pi coding-agent SDK and integration modes](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [LangChain: LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
