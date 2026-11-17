---
title: "স্থানীয় AI গোপনীয়তা: আপনার কম্পিউটারে কী থাকে এবং কী থাকে না"
date: 2026-10-10
lastmod: 2026-11-13
toc: true
draft: false
description: "স্থানীয় inference বা hosted AI service বেছে নেওয়ার আগে prompt, model file, tool, log, network exposure এবং বিদ্যুৎ খরচ অনুসরণ করুন।"
genre: ["স্থানীয় AI", "গোপনীয়তা", "নিজে হোস্ট করা AI", "সাইবার নিরাপত্তা", "AI অর্থনীতি"]
tags: ["স্থানীয় AI গোপনীয়তা", "স্থানীয় ইনফারেন্স", "ক্লাউডে AI", "AI ডেটার গোপনীয়তা", "নিজে হোস্ট করা AI", "LLM গোপনীয়তা", "GPU মালিকানার খরচ", "AI বিদ্যুতের খরচ", "RTX 5070", "Claude Haiku 5.5", "Ollama গোপনীয়তা", "llama.cpp", "AI নিরাপত্তা", "অফলাইন AI", "স্থানীয় ভাষার মডেল", "প্রম্পটের গোপনীয়তা", "AI হুমকি-মডেল", "GPU খরচ-সমতার বিন্দু", "AI ডেটার সীমা", "ব্যক্তিগত AI"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "দৃশ্যমান data path দিয়ে cloud service-এ যুক্ত একটি local AI workstation"
coverCaption: "স্থানীয় ও hosted AI data path-এর চিত্র"
---

**স্থানীয় AI আপনার data boundary ছোট করে।** Model, tool, log এবং network path local থাকলে local runtime-এ process করা prompt আপনার device-এই থাকে। Local GPU একটি computer-কে sealed system বানায় না।

Model runtime, tool plugin, browser extension, remote access, exposed API এবং model download আপনার risk নির্ধারণ করে। Cost-ও গুরুত্বপূর্ণ। Electricity hosted token price-এর নিচে থাকতে পারে, কিন্তু hardware ownership পূর্ণ break-even অনেক দূরে ঠেলে দেয়।

এই guide আগে privacy boundary map করে। এরপর current vendor price, একটি স্পষ্ট power assumption এবং supplied video-র reported figure দিয়ে cost পরীক্ষা করে।

<!--more-->

নিচের formula বোঝার জন্য এই local-versus-hosted cost comparison ব্যবহার করুন। একই model file এবং runtime আপনার hardware-এ test না করে throughput figure কপি করবেন না।

{{< youtube id="DmkuFpoMYmc" enable="true" title="Is local AI worth it? We did the math vs Claude Haiku 5.5" description="A local-versus-hosted AI cost comparison." >}}

ভিডিওটি 2 মিনিট 31 সেকেন্ড runtime report করে। Watch page দিয়ে title ও runtime যাচাই করেছি। Hardware test পুনরাবৃত্তি করিনি, তাই reported speed source-reported measurement হিসেবেই থাকছে।

## সংক্ষিপ্ত উত্তর

- **নিয়ন্ত্রিত data path-এর জন্য local inference বেছে নিন।** Model server device-এ রাখুন, loopback-এ bind করুন এবং tool access সীমিত করুন।
- **মাঝে মাঝে কাজের জন্য hosted inference বেছে নিন।** Workload ছোট হলে বা পছন্দের model system-এ না চললে hardware খরচ এড়ান।
- **Local cost-কে দুইটি সংখ্যা হিসেবে দেখুন।** Active hour-এর electricity এবং hardware ownership আলাদা করুন।
- **Privacy-কে system property হিসেবে দেখুন।** Plugin file upload করলে বা local API সব network interface-এ শুনলে private model-এর সুবিধা হারায়।

Sensitive text workstation বা isolated network-এর ভিতরে রাখার দরকার হলে local inference সহায়ক। Offline operation, fixed model version বা provider quota ছাড়া predictable access দরকার হলেও এটি সহায়ক।

এই সুবিধাগুলি better answer প্রমাণ করে না। Hosted model কোনো task-এ বেশি উপযুক্ত, দ্রুততর বা কম maintenance-এর হতে পারে। Hardware কেনার আগে workload মাপুন।

## ডেটার প্রবাহ অনুসরণ করুন

Request-এর প্রতিটি component map করুন। শুধু model name data কোথায় যায় তা দেখায় না।

| উপাদান | গোপনীয়তার প্রশ্ন | যে প্রমাণ সংগ্রহ করবেন |
|---|---|---|
| **স্থানীয় মডেল সার্ভার** | প্রম্পট কি হোস্টেই থাকে? | প্রক্রিয়ার কনফিগারেশন, সার্ভারের সংযোগ গ্রহণের ঠিকানা এবং বহির্গামী নেটওয়ার্ক ট্র্যাফিক |
| **ক্লাউড মডেল** | কোন লেখা, ফাইল এবং টুলের ফলাফল হোস্ট ছেড়ে যায়? | API এন্ডপয়েন্ট, সেবা প্রদানকারীর শর্তাবলি, অনুরোধের লগ এবং অ্যাকাউন্টের সেটিংস |
| **স্থানীয় অ্যাপের ক্লাউড মোড** | নির্বাচিত মডেলটি কি ডিভাইসে চলে? | মডেলের শনাক্তকারী, সেবা প্রদানকারীর নাম এবং নেটওয়ার্ক সংযোগ |
| **টুল প্লাগইন** | মডেলটি কি ফাইল, শেল আউটপুট বা ব্রাউজারের বিষয়বস্তু পায়? | টুলের তালিকা, অনুমতি এবং ধারণ করা অনুরোধের তথ্য |
| **মডেল ডাউনলোড** | কোন কোড ও ওজন হোস্টে যোগ হয়? | উৎস রিপোজিটরি, লাইসেন্স, রিলিজের চেকসাম এবং ডাউনলোডের পথ |
| **স্থানীয় লগ** | প্রম্পট ও টুলের ফলাফল কোথায় সংরক্ষিত থাকে? | রানটাইম লগ, শেল ইতিহাস, ক্র্যাশ রিপোর্ট এবং ব্যাকআপের পরিধি |

**Local model prompt path থেকে একটি provider সরায়।** বাকি path review করার প্রয়োজন সরায় না।

## স্থানীয় হলেই প্রাথমিক সেটিংয়ে গোপনীয়তা থাকে না

[Ollama-এর গোপনীয়তা নীতি](https://ollama.com/privacy) বলে, model locally চললে Ollama prompt বা data দেখে না। Policy local operation এবং cloud-hosted model আলাদা করে। একই application দুই mode চালালেও cloud model একটি service boundary তৈরি করে।

[llama.cpp সার্ভারের ডকুমেন্টেশন](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) অনুযায়ী local server default-এ `127.0.0.1:8080` শোনে। Docker example-এ `--host 0.0.0.0`-ও আছে, যা সব interface-এ service প্রকাশ করে। Wider bind address access boundary বদলায়।

Sensitive text পাঠানোর আগে listening address দেখুন:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

সাধারণ ক্ষেত্রে `127.0.0.1` বা `localhost` access একই host-এ সীমিত করে। LAN address বা `0.0.0.0`-এর জন্য firewall rule এবং authentication plan দরকার। দুটো test না করে model endpoint network-এ প্রকাশ করবেন না।

Selected model name-ও দেখুন। Ollama cloud documentation cloud model-কে আলাদা service path বলে। Local interface local execution প্রমাণ করে না।

Ollama [FAQ](https://docs.ollama.com/faq) local-only mode document করে। Service restart-এর আগে `disable_ollama_cloud` variable-টি `~/.ollama/server.json` file-এ set করুন, অথবা `OLLAMA_NO_CLOUD=1` set করুন। এটি selected runtime থেকে Ollama cloud model এবং web search সরায়। Host-এর অন্য application, browser tool, plugin বা network access সীমিত করে না।

```json
{
  "disable_ollama_cloud": true
}
```

Restart-এর পর setting verify করুন। Local-only runtime একটি path সংকুচিত করে। এটি private host তৈরি করে না।


## Ollama-র স্পিচ ও নেটওয়ার্ক সীমা

*[Ollama v0.40.11 রিলিজ](https://github.com/ollama/ollama/releases/tag/v0.40.11) macOS-এ speech generation ঘোষণা করে। এর [API রেফারেন্স](https://docs.ollama.com/api/openai-compatibility) `/v1/audio/speech` এন্ডপয়েন্টের সময় v0.40.8-এ নির্ধারণ করে, তাই v0.40.11 এন্ডপয়েন্টের নথিভুক্ত প্রথম সংস্করণ নয়।* এটি **text-to-speech**, speech-to-text নয়: অনুরোধে speech model-এ, যেমন Phonon-এ, text পাঠানো হয় এবং streamed audio ফেরত আসে। [স্পিচ গাইড](https://docs.ollama.com/capabilities/speech)-এ `ollama run phonon` দিয়ে স্থানীয়ভাবে audio চালানো বা output redirect করলে WAV file লেখার উদাহরণও আছে।

**স্থানীয় স্পিচ পথের** জন্য ডাউনলোড করা স্থানীয় model ও স্থানীয় server লাগে। Ollama-র [FAQ](https://docs.ollama.com/faq) বলেছে, server ডিফল্টভাবে `127.0.0.1:11434`-এ bind করে এবং **`OLLAMA_HOST`** bind address বদলায়। ডিফল্ট এখনও কার্যকর ধরে না নিয়ে, আগের `lsof` command দিয়ে সক্রিয় listener পরীক্ষা করুন। Ollama-র [API পরিচিতি](https://docs.ollama.com/api/introduction) বলেছে, স্থানীয় request-এ API key লাগে না। ব্যক্তিগত text পাঠানোর আগে wider bind-কে firewall ও access control দিয়ে সীমাবদ্ধ করুন।

**Loopback bind-ই পুরো সীমা নয়।** Ollama তার HTTP server reverse proxy বা tunnel দিয়ে forward করার নির্দেশনা দেয়। Ollama নিজে loopback-এ listen করলেও প্রতিটি proxy-র listener, authentication ও request logging পরীক্ষা করুন। আপনার পাঠানো text এবং ফেরত audio proxy connection পেরিয়ে যায়। Ollama-র [সমস্যা সমাধানের গাইড](https://docs.ollama.com/troubleshooting) server log চিহ্নিত করে, কিন্তু speech documentation audio retention-এর প্রতিশ্রুতি দেয় না। client কোথায় WAV output save করে এবং proxy বা app log কোথায় থাকে তা দেখুন। Ollama-র FAQ বলে, local run-এ Ollama prompt বা data দেখে না। model download-এ network লাগে, আর cloud model আলাদা পথ ব্যবহার করে। শুধু Ollama-র স্থানীয় model setup হলে, আগের বর্ণিত `OLLAMA_NO_CLOUD=1` setting Ollama-র cloud feature বন্ধ করে। এটি অন্য application নিয়ন্ত্রণ করে না।

## হোস্টেড সেবার খরচ গণনা করুন

Token price input এবং output আলাদা করে। [Anthropic Claude Haiku 5.5-এর জন্য 100,000 token পর্যন্ত prompt-এ প্রতি million input token $0.10 এবং প্রতি million output token $0.50 তালিকাভুক্ত করে](https://www.anthropic.com/claude/haiku)। 100,000-এর বেশি prompt-এ উচ্চতর rate প্রযোজ্য।

[OpenAI-এর টোকেন নির্দেশিকা](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) ব্যাখ্যা করে কেন শব্দের সংখ্যা টোকেনের সংখ্যার সমান নয়। এটি ইনপুট, আউটপুট, ক্যাশ করা ইনপুট এবং যুক্তি-সংক্রান্ত টোকেনও আলাদা করে। শব্দ গোনার ভিত্তিতে অনুমান না করে সরবরাহকারীর ব্যবহার-তথ্য ব্যবহার করুন।

সহজ comparison-এ এক million generated token এবং এক million input token আলাদা workload হিসেবে নিন। Coding agent repeated context পাঠায় এবং ছোট answer দেয়, তাই এক combined token figure cost mix লুকায়।

## স্থানীয় বিদ্যুতের খরচ হিসাব করুন

[NVIDIA RTX 5070 উন্মোচন ঘোষণায়](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) প্রারম্ভিক দাম $549 বলা হয়েছে। [NVIDIA RTX 5070 পরিবারের পৃষ্ঠা](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) Founders Edition-এর রেফারেন্স নকশায় 12 GB মেমোরি এবং 250 W মোট গ্রাফিক্স ক্ষমতা উল্লেখ করে। NVIDIA-এর পণ্য পৃষ্ঠায় এখনও $549 দাম দেখানো হয়েছে, এবং এই পর্যালোচনার সময় কার্ডটি স্টকে ছিল না।

GPU power figure whole-system power নয়। PC-র জন্য wall meter ব্যবহার করুন। নিচের example-এ **400 W whole-system draw** ধরা হয়েছে, যেখানে GPU, processor, memory, storage, fan এবং power-supply loss আছে। এটি arithmetic assumption, measured result নয়।

[যুক্তরাষ্ট্রের জ্বালানি তথ্য প্রশাসনের পূর্বাভাস](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) 2026 সালের গড় আবাসিক বিদ্যুতের দাম প্রতি কিলোওয়াট-ঘণ্টায় 18.2 সেন্ট ধরে। আপনার বিদ্যুতের হার ফলাফল বদলে দেয়।

Generated output-এর জন্য formula:

```text
প্রতি 1M আউটপুট টোকেনের স্থানীয় খরচ =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

400 W এবং প্রতি kilowatt-hour $0.182 হলে system-এর active hour প্রতি খরচ $0.0728।

| আউটপুট টোকেনের গতি | ১০ লক্ষ টোকেনের সময় | ১০ লক্ষ টোকেনের বিদ্যুতের খরচ |
|---:|---:|---:|
| **20 টোকেন প্রতি সেকেন্ড** | 13 ঘণ্টা 53 মিনিট | **$1.01** |
| **50 টোকেন প্রতি সেকেন্ড** | 5 ঘণ্টা 33 মিনিট | **$0.40** |
| **94 টোকেন প্রতি সেকেন্ড** | 2 ঘণ্টা 57 মিনিট | **$0.22** |

50 output token per second-এ local power Haiku 5.5-এর $0.50 output price-এর কম। 20 output token per second-এ local power বেশি। এই assumption-এ output-speed threshold প্রায় 40 token per second।

Input calculation একই formula ব্যবহার করে। 2,650 input token per second-এ 1M input token প্রায় 6 মিনিট 17 সেকেন্ড এবং power cost প্রায় $0.008। 1,000 input token per second-এ একই কাজের খরচ প্রায় $0.020।

Supplied transcript RTX 5070 example-এর জন্য 94 output token per second এবং 2,650 input token per second report করে। 400 W assumption-এ উপরের arithmetic ওই figure-এর সঙ্গে মেলে। Transcript-এ independent lab record, model file hash, runtime build, prompt বা wall-meter reading নেই। Speed-কে reference result ধরুন, purchase guarantee নয়।

## হার্ডওয়্যার বদলালে খরচ-সমতার বিন্দু

শুধু power saving hardware শোধ করে না। Full purchase-এর সঙ্গে hosted output cost এবং local variable cost-এর difference তুলনা করুন।

50 output token per second-এ:

```text
$0.50 হোস্ট করা আউটপুটের দাম - $0.40 স্থানীয় বিদ্যুৎ খরচ = প্রতি 1M আউটপুট টোকেনে $0.10 সাশ্রয়
$549 GPU-এর দাম / $0.10 = প্রায় 5.5 বিলিয়ন আউটপুট টোকেন
```

94 output token per second-এ rounded saving প্রতি million token প্রায় $0.28। $549 GPU recover করতে প্রায় 2 billion output token দরকার। দুটো figure-ই system memory, storage, motherboard, power supply, cooling, maintenance এবং resale value বাদ দেয়।

Launch price universal purchase quote নয়। NVIDIA current page official price দেখিয়েছে, stock নয়। Break-even model-এ $819 seller listing বসানোর আগে আলাদা verification দরকার। নিজের invoice এবং measured wall power ব্যবহার করুন।

**Existing hardware decision বদলায়।** Workstation-এ যথেষ্ট memory এবং suitable GPU থাকলে পরের task-এর জন্য hardware cost sunk। Power, time, quality, privacy এবং maintenance তুলনা করুন। Complete system কিনতে হলে full system-এর সঙ্গে hosted use তুলনা করুন।

মডেল উপযোগিতার বিস্তারিত জানতে [স্থানীয় AI মডেল ও GPU প্রসঙ্গ নির্দেশিকা](/articles/local-ai-model-gpu-context-guide/) এবং [16GB VRAM পরিমাপ নির্দেশিকা](/articles/is-16gb-vram-enough-local-llm/) পড়ুন। স্থানীয় কোডিং-এজেন্টের বর্ণিত সেটআপ জানতে [Strata ও OpenCode নির্দেশিকা](/articles/strata-opencode-local-coding-agent-16gb/) পড়ুন।

## স্থানীয় গোপনীয়তা কী দেয়

- **ছোট data path:** inference local থাকলে prompt model provider-এ পৌঁছাতে হয় না।
- **Offline operation:** downloaded model এবং local runtime text generation-এর জন্য live provider connection চায় না।
- **Version control:** automatic provider change-এর বদলে model file এবং runtime version আপনি বেছে নেন।
- **Usage control:** hardware ownership এবং power হিসাবের পর local inference প্রতি request cloud meter এড়ায়।
- **Network policy control:** firewall এবং host control model endpoint-এ কার access থাকবে নির্ধারণ করে।

Source code, client record, unreleased design, private note এবং disconnected environment-এর কাজে লাভ বেশি। Local inference-এর জন্য disk encryption, host update, account separation এবং restricted tool-ও দরকার।

## স্থানীয় গোপনীয়তা কী দেয় না

- **Quality guarantee নয়:** ছোট বা quantized model-কে real acceptance criteria-র বিরুদ্ধে test করতে হয়।
- **Supply-chain guarantee নয়:** model file, runtime, plugin এবং container image-এর trusted source ও integrity check দরকার।
- **Clean host নয়:** malware, browser extension, backup, crash reporter এবং remote administration এখনও host data দেখে।
- **Safe network endpoint নয়:** every-interface server নতুন defend করার service তৈরি করে।
- **Free system নয়:** electricity, storage, cooling, hardware wear এবং maintenance-এর cost আছে।

[Strata-এর স্থানীয় কোডিং-এজেন্ট নির্দেশিকা](/articles/strata-opencode-local-coding-agent-16gb/) দেখায় কেন সিস্টেম মেমোরি, প্রসঙ্গ, টুল অ্যাক্সেস এবং রানটাইম সেটিংস মূল্যায়নের অংশ। GPU memory একা privacy বা performance boundary নির্ধারণ করে না।

## সঠিক সীমা বেছে নিন

| পরিস্থিতি | প্রথমে যে বিকল্পটি বেছে নেবেন | কারণ |
|---|---|---|
| **সংবেদনশীল নথি এবং আগে থেকে থাকা উপযুক্ত PC** | স্থানীয় ইনফারেন্স | নিয়ন্ত্রিত হোস্টে প্রম্পট রাখুন এবং নতুন হার্ডওয়্যারের খরচ এড়ান |
| **মাঝেমধ্যে সাধারণ লেখা তৈরি** | হোস্ট করা API বা চ্যাট পরিষেবা | অল্প কাজের জন্য অর্থ দিন এবং রক্ষণাবেক্ষণের খরচ এড়ান |
| **সর্বাধুনিক মডেল বা বিশেষায়িত ক্লাউড টুল** | হোস্ট করা পরিষেবা | প্রয়োজনীয় মডেল বা টুল স্থানীয় হোস্টে নেই |
| **যাচাইকৃত স্থানীয় মডেল নিয়ে নিয়মিত বড় পরিমাণের কাজ** | স্থানীয় বা মিশ্র ব্যবস্থা | বিদ্যুৎ, গুণমান, সহায়তার সময় এবং সেবা প্রদানকারীর মূল্য তুলনা করুন |
| **মিশ্র কাজের চাপ** | মিশ্র পদ্ধতিতে রাউটিং | সংবেদনশীল কাজ স্থানীয় রাখুন এবং অনুমোদিত সাধারণ কাজ হোস্ট করা মডেলে পাঠান |

**Hybrid routing-এর explicit classification rule দরকার।** Data-কে local-only, hosted processing-এর জন্য approved, অথবা review না হওয়া পর্যন্ত forbidden হিসেবে mark করুন। Rule enforce করতে model name বা application icon-এর ওপর নির্ভর করবেন না।

## বিশ্বাস করার আগে যাচাই করুন

1. **Model path লিখুন।** Model identifier, runtime, version এবং download source record করুন।
2. **Bind address দেখুন।** Wider path-এর documented need না থাকলে server loopback-এ শোনে নিশ্চিত করুন।
3. **সব tool তালিকাভুক্ত করুন।** File, shell, browser, network এবং plugin access review করুন।
4. **Persistence inspect করুন।** Prompt log, tool output, crash report, backup এবং shared model directory খুঁজুন।
5. **Network behavior test করুন।** Representative prompt দিয়ে sensitive test-এর সময় connection observe করুন।
6. **System measure করুন।** Wall power, output speed, input speed, context length এবং retry record করুন।
7. **Accepted work test করুন।** শুধু token per second নয়, completed task এবং review effort তুলনা করুন।

[স্থানীয় AI ও ChatGPT তুলনা নির্দেশিকা](/articles/local-ai-vs-chatgpt-how-close-are-we/) মডেলের সক্ষমতার পার্থক্য ব্যাখ্যা করে। Quality test-এর পাশে এই privacy checklist ব্যবহার করুন।

## তথ্যসূত্র

- [Video, Is local AI worth it? We did the math vs Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [NVIDIA Blackwell GeForce RTX 50 Series launch announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [NVIDIA GeForce RTX 5070 family specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [NVIDIA GeForce RTX 5070 product page](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, October 2026 Short-Term Energy Outlook](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Anthropic Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, Understanding and counting tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Ollama-এর গোপনীয়তা নীতি](https://ollama.com/privacy)
- [Ollama v0.40.11 রিলিজ নোট](https://github.com/ollama/ollama/releases/tag/v0.40.11)
- [Ollama স্পিচ গাইড](https://docs.ollama.com/capabilities/speech)
- [Ollama OpenAI-সামঞ্জস্য API রেফারেন্স](https://docs.ollama.com/api/openai-compatibility)
- [Ollama API পরিচিতি](https://docs.ollama.com/api/introduction)
- [Ollama FAQ: server configuration, cloud settings ও reverse proxy](https://docs.ollama.com/faq)
- [Ollama সমস্যা সমাধান ও server log](https://docs.ollama.com/troubleshooting)
- [llama.cpp সার্ভারের ডকুমেন্টেশন](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
