---
title: "স্থানীয় AI গোপনীয়তা: আপনার কম্পিউটারে কী থাকে এবং কী থাকে না"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "স্থানীয় inference বা hosted AI service বেছে নেওয়ার আগে prompt, model file, tool, log, network exposure এবং বিদ্যুৎ খরচ অনুসরণ করুন।"
genre: ["স্থানীয় AI", "গোপনীয়তা", "self-hosted AI", "সাইবার নিরাপত্তা", "AI অর্থনীতি"]
tags: ["local AI privacy", "local inference", "cloud AI", "AI data privacy", "self-hosted AI", "LLM privacy", "GPU ownership cost", "AI electricity cost", "RTX 5070", "Claude Haiku 5.5", "Ollama privacy", "llama.cpp", "AI security", "offline AI", "local language models", "prompt privacy", "AI threat model", "GPU break-even", "AI data boundary", "private AI"]
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

## Data path অনুসরণ করুন

Request-এর প্রতিটি component map করুন। শুধু model name data কোথায় যায় তা দেখায় না।

| Component | Privacy question | Evidence to collect |
|---|---|---|
| **Local model server** | Prompt কি host-এ থাকে? | Process configuration, listening address এবং outbound traffic |
| **Cloud model** | কোন text, file এবং tool result host ছাড়ে? | API endpoint, provider terms, request log এবং account setting |
| **Local app-এর cloud mode** | Selected model কি device-এ চলে? | Model identifier, provider label এবং network connection |
| **Tool plugin** | Model কি file, shell output বা browser content পায়? | Tool list, permission এবং captured request data |
| **Model download** | কোন code এবং weight host-এ ঢোকে? | Source repository, license, release checksum এবং download path |
| **Local log** | Prompt এবং tool result কোথায় থাকে? | Runtime log, shell history, crash report এবং backup scope |

**Local model prompt path থেকে একটি provider সরায়।** বাকি path review করার প্রয়োজন সরায় না।

## Local মানেই default privacy নয়

[Ollama privacy policy](https://ollama.com/privacy) বলে, model locally চললে Ollama prompt বা data দেখে না। Policy local operation এবং cloud-hosted model আলাদা করে। একই application দুই mode চালালেও cloud model একটি service boundary তৈরি করে।

[llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) অনুযায়ী local server default-এ `127.0.0.1:8080` শোনে। Docker example-এ `--host 0.0.0.0`-ও আছে, যা সব interface-এ service প্রকাশ করে। Wider bind address access boundary বদলায়।

Sensitive text পাঠানোর আগে listening address দেখুন:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

সাধারণ ক্ষেত্রে `127.0.0.1` বা `localhost` access একই host-এ সীমিত করে। LAN address বা `0.0.0.0`-এর জন্য firewall rule এবং authentication plan দরকার। দুটো test না করে model endpoint network-এ প্রকাশ করবেন না।

Selected model name-ও দেখুন। Ollama cloud documentation cloud model-কে আলাদা service path বলে। Local interface local execution প্রমাণ করে না।

Ollama [FAQ](https://docs.ollama.com/faq) local-only mode document করে। Service restart-এর আগে `~/.ollama/server.json`-এ `disable_ollama_cloud` set করুন, অথবা `OLLAMA_NO_CLOUD=1` set করুন। এটি selected runtime থেকে Ollama cloud model এবং web search সরায়। Host-এর অন্য application, browser tool, plugin বা network access সীমিত করে না।

```json
{
  "disable_ollama_cloud": true
}
```

Restart-এর পর setting verify করুন। Local-only runtime একটি path সংকুচিত করে। এটি private host তৈরি করে না।

## Hosted cost গণনা করুন

Token price input এবং output আলাদা করে। [Anthropic Claude Haiku 5.5-এর জন্য 100,000 token পর্যন্ত prompt-এ প্রতি million input token $0.10 এবং প্রতি million output token $0.50 তালিকাভুক্ত করে](https://www.anthropic.com/claude/haiku)। 100,000-এর বেশি prompt-এ উচ্চতর rate প্রযোজ্য।

[OpenAI token guide](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) ব্যাখ্যা করে কেন word count token count নয়। এটি input, output, cached input এবং reasoning token আলাদা করে। Word-count estimate-এর বদলে provider usage field ব্যবহার করুন।

সহজ comparison-এ এক million generated token এবং এক million input token আলাদা workload হিসেবে নিন। Coding agent repeated context পাঠায় এবং ছোট answer দেয়, তাই এক combined token figure cost mix লুকায়।

## Local power হিসাব করুন

[NVIDIA RTX 5070 launch announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) $549 starting price তালিকাভুক্ত করেছিল। [RTX 5070 family page](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) Founders Edition reference design-এর জন্য 12 GB memory এবং 250 W total graphics power তালিকাভুক্ত করে। Review-এর সময় product page-এ $549 এবং out-of-stock দেখা গেছে।

GPU power figure whole-system power নয়। PC-র জন্য wall meter ব্যবহার করুন। নিচের example-এ **400 W whole-system draw** ধরা হয়েছে, যেখানে GPU, processor, memory, storage, fan এবং power-supply loss আছে। এটি arithmetic assumption, measured result নয়।

[U.S. Energy Information Administration forecast](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) 2026-এর average residential electricity price হিসেবে প্রতি kilowatt-hour 18.2 cents ব্যবহার করেছে। আপনার utility rate ফল বদলায়।

Generated output-এর জন্য formula:

```text
local cost per 1M output tokens =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

400 W এবং প্রতি kilowatt-hour $0.182 হলে system-এর active hour প্রতি খরচ $0.0728।

| Output speed | 1M token-এর সময় | 1M token-এর power cost |
|---:|---:|---:|
| **20 token per second** | 13 ঘণ্টা 53 মিনিট | **$1.01** |
| **50 token per second** | 5 ঘণ্টা 33 মিনিট | **$0.40** |
| **94 token per second** | 2 ঘণ্টা 57 মিনিট | **$0.22** |

50 output token per second-এ local power Haiku 5.5-এর $0.50 output price-এর কম। 20 output token per second-এ local power বেশি। এই assumption-এ output-speed threshold প্রায় 40 token per second।

Input calculation একই formula ব্যবহার করে। 2,650 input token per second-এ 1M input token প্রায় 6 মিনিট 17 সেকেন্ড এবং power cost প্রায় $0.008। 1,000 input token per second-এ একই কাজের খরচ প্রায় $0.020।

Supplied transcript RTX 5070 example-এর জন্য 94 output token per second এবং 2,650 input token per second report করে। 400 W assumption-এ উপরের arithmetic ওই figure-এর সঙ্গে মেলে। Transcript-এ independent lab record, model file hash, runtime build, prompt বা wall-meter reading নেই। Speed-কে reference result ধরুন, purchase guarantee নয়।

## Hardware change-এর break-even

শুধু power saving hardware শোধ করে না। Full purchase-এর সঙ্গে hosted output cost এবং local variable cost-এর difference তুলনা করুন।

50 output token per second-এ:

```text
$0.50 hosted output price - $0.40 local power = $0.10 saved per 1M tokens
$549 GPU price / $0.10 = about 5.5 billion output tokens
```

94 output token per second-এ rounded saving প্রতি million token প্রায় $0.28। $549 GPU recover করতে প্রায় 2 billion output token দরকার। দুটো figure-ই system memory, storage, motherboard, power supply, cooling, maintenance এবং resale value বাদ দেয়।

Launch price universal purchase quote নয়। NVIDIA current page official price দেখিয়েছে, stock নয়। Break-even model-এ $819 seller listing বসানোর আগে আলাদা verification দরকার। নিজের invoice এবং measured wall power ব্যবহার করুন।

**Existing hardware decision বদলায়।** Workstation-এ যথেষ্ট memory এবং suitable GPU থাকলে পরের task-এর জন্য hardware cost sunk। Power, time, quality, privacy এবং maintenance তুলনা করুন। Complete system কিনতে হলে full system-এর সঙ্গে hosted use তুলনা করুন।

Model-fit detail-এর জন্য [local AI model and GPU context guide](/articles/local-ai-model-gpu-context-guide/) এবং [16GB VRAM sizing guide](/articles/is-16gb-vram-enough-local-llm/) পড়ুন। Reported local coding-agent setup-এর জন্য [Strata and OpenCode guide](/articles/strata-opencode-local-coding-agent-16gb/) পড়ুন।

## Local privacy কী দেয়

- **ছোট data path:** inference local থাকলে prompt model provider-এ পৌঁছাতে হয় না।
- **Offline operation:** downloaded model এবং local runtime text generation-এর জন্য live provider connection চায় না।
- **Version control:** automatic provider change-এর বদলে model file এবং runtime version আপনি বেছে নেন।
- **Usage control:** hardware ownership এবং power হিসাবের পর local inference প্রতি request cloud meter এড়ায়।
- **Network policy control:** firewall এবং host control model endpoint-এ কার access থাকবে নির্ধারণ করে।

Source code, client record, unreleased design, private note এবং disconnected environment-এর কাজে লাভ বেশি। Local inference-এর জন্য disk encryption, host update, account separation এবং restricted tool-ও দরকার।

## Local privacy কী দেয় না

- **Quality guarantee নয়:** ছোট বা quantized model-কে real acceptance criteria-র বিরুদ্ধে test করতে হয়।
- **Supply-chain guarantee নয়:** model file, runtime, plugin এবং container image-এর trusted source ও integrity check দরকার।
- **Clean host নয়:** malware, browser extension, backup, crash reporter এবং remote administration এখনও host data দেখে।
- **Safe network endpoint নয়:** every-interface server নতুন defend করার service তৈরি করে।
- **Free system নয়:** electricity, storage, cooling, hardware wear এবং maintenance-এর cost আছে।

[Strata local coding-agent guide](/articles/strata-opencode-local-coding-agent-16gb/) দেখায় কেন system memory, context, tool access এবং runtime setting evaluation-এ থাকে। GPU memory একা privacy বা performance boundary নির্ধারণ করে না।

## সঠিক boundary বাছুন

| Situation | Better first choice | Reason |
|---|---|---|
| **Sensitive document এবং compatible PC আছে** | Local inference | Controlled host-এর ভিতরে prompt রাখা এবং নতুন hardware খরচ এড়ানো |
| **মাঝে মাঝে generic drafting** | Hosted API বা chat service | ছোট workload-এর জন্য pay করা এবং maintenance এড়ানো |
| **Frontier model বা specialized cloud tool** | Hosted service | প্রয়োজনীয় model বা tool local host-এ নেই |
| **Verified local model সহ বড় recurring volume** | Local বা hybrid | Power, quality, support time এবং provider price তুলনা করা |
| **Mixed workload** | Hybrid routing | Sensitive task local রেখে approved generic task hosted model-এ পাঠানো |

**Hybrid routing-এর explicit classification rule দরকার।** Data-কে local-only, hosted processing-এর জন্য approved, অথবা review না হওয়া পর্যন্ত forbidden হিসেবে mark করুন। Rule enforce করতে model name বা application icon-এর ওপর নির্ভর করবেন না।

## Trust করার আগে verify করুন

1. **Model path লিখুন।** Model identifier, runtime, version এবং download source record করুন।
2. **Bind address দেখুন।** Wider path-এর documented need না থাকলে server loopback-এ শোনে নিশ্চিত করুন।
3. **সব tool তালিকাভুক্ত করুন।** File, shell, browser, network এবং plugin access review করুন।
4. **Persistence inspect করুন।** Prompt log, tool output, crash report, backup এবং shared model directory খুঁজুন।
5. **Network behavior test করুন।** Representative prompt দিয়ে sensitive test-এর সময় connection observe করুন।
6. **System measure করুন।** Wall power, output speed, input speed, context length এবং retry record করুন।
7. **Accepted work test করুন।** শুধু token per second নয়, completed task এবং review effort তুলনা করুন।

[Local AI versus ChatGPT guide](/articles/local-ai-vs-chatgpt-how-close-are-we/) model capability trade-off ব্যাখ্যা করে। Quality test-এর পাশে এই privacy checklist ব্যবহার করুন।

## References

- [Video, Is local AI worth it? We did the math vs Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [NVIDIA Blackwell GeForce RTX 50 Series launch announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [NVIDIA GeForce RTX 5070 family specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [NVIDIA GeForce RTX 5070 product page](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, October 2026 Short-Term Energy Outlook](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Anthropic Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, Understanding and counting tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Ollama privacy policy](https://ollama.com/privacy)
- [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
