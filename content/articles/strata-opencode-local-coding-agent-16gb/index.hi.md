---
title: "16GB GPU पर स्थानीय AI कोडिंग: Strata, OpenCode और Qwen3.8"
date: 2026-10-06
lastmod: 2026-11-13
toc: true
draft: false
description: "Strata और OpenCode के साथ स्थानीय कोडिंग एजेंट चलाएँ। रिपोर्ट किए गए RTX 4060 Ti परिणामों, RAM आवश्यकताओं, प्रॉम्प्ट पुनःउपयोग, रीजनिंग बजट और भुगतान वाली सदस्यता बदलने की सीमाओं को देखें।"
genre: ["स्थानीय AI", "डेवलपर टूल", "स्व-होस्टेड AI", "AI हार्डवेयर"]
tags: ["स्थानीय AI कोडिंग एजेंट", "Strata", "OpenCode", "Qwen3.8 Flash Next", "125B मॉडल", "RTX 4060 Ti", "16GB GPU", "64GB RAM", "IQ3_S", "mixture of experts", "expert cache", "prompt caching", "prefix reuse", "reasoning budget", "coding assistant", "local inference", "AI subscriptions", "GPU offload", "Docker", "automated tests", "OpenAI compatible API", "context window", "NVMe SSD", "self hosted AI"]
cover: "/img/cover/local-ai-coding-16gb-gpu-nvidia-rtx-4060-ti.webp"
coverAlt: "स्थानीय AI कोडिंग वातावरण का चित्र, जिसमें NVIDIA RTX 4060 Ti GPU गहरे बैकग्राउंड पर चमकती डेटा धाराओं और कोड अंशों से घिरा है।"
coverCaption: ""
---

**16GB GPU पर स्थानीय कोडिंग एजेंट सीमित विकास कार्यों के लिए व्यावहारिक विकल्प है।** Strata और OpenCode स्थानीय inference को फ़ाइल संपादन, shell commands और test execution से जोड़ते हैं। RTX 4060 Ti पर रिपोर्ट किए गए Qwen3.8-Flash-Next run ने paid inference calls के बिना एक application, बाद के बदलाव और racing-game prototype पूरा किया।

**Subscription बदलने के लिए व्यापक test चाहिए।** Published results एक मशीन पर चलने वाला setup दिखाते हैं। वे अलग भाषाओं, repositories या कठिन debugging tasks में paid coding services के बराबर प्रदर्शन सिद्ध नहीं करते। Hardware में 64GB system RAM भी है, जो model का बड़ा भाग संभालती है।

## मुख्य बातें

- **16GB GPU memory को बताता है**, reported configuration के लिए कुल memory को नहीं।
- **Prompt reuse महत्वपूर्ण है**, क्योंकि coding agents बार बार मिलते-जुलते conversation history भेजते हैं।
- **Reasoning को budget चाहिए**, ताकि planning code और tool calls के लिए जगह छोड़े।
- **Generated tests पास होना केवल आंशिक प्रमाण है**, Docker और gameplay के लिए अलग checks चाहिए।
- **Zero API spend ownership costs को नहीं गिनता**, जैसे electricity और maintenance time।

**आवश्यकताएँ:** Compatible computer, selected model के लिए पर्याप्त free storage, Git, npm सहित Node.js और terminal tools का अनुभव। Reported IQ3_S setup के साथ 64GB RAM रखें। अन्य configurations के लिए current Strata installer देखें।

**समय और कठिनाई:** Intermediate। Task completion speed का मूल्यांकन करने से पहले बड़े model downloads और installation के लिए समय रखें। Reported task timings में setup शामिल नहीं है।

## परीक्षित विन्यास

| घटक | Reported configuration |
|---|---|
| **GPU** | NVIDIA RTX 4060 Ti, 16GB VRAM |
| **CPU** | Intel Core i5-11600K |
| **सिस्टम मेमोरी** | 64GB RAM |
| **Storage** | NVMe SSD |
| **मॉडल** | Qwen3.8-Flash-Next, 125B MoE, IQ3_S |
| **Inference engine** | Strata |
| **Coding agent** | OpenCode |
| **Configured context** | 65,536 tokens |
| **कॉन्फ़िगर की गई आउटपुट सीमा** | 16,384 tokens |

**NetworkCoder की published configuration और results** ये figures देती हैं। [परीक्षण रिपॉज़िटरी](https://github.com/network-tocoder/Free-Local-AI-Coding-Agent-125B-on-16GB-GPU) 46.84GiB expert weights को 28 seconds में load करने की report देता है। 4,431 experts GPU memory में 8.45GiB लेते हैं। ये measurements tested run का वर्णन करते हैं, किसी दूसरे engine version में allocation की guarantee नहीं।

**मौजूदा अनुकूलता इस परीक्षण से व्यापक है।** 6 अक्टूबर 2026 को जाँचे गए [Strata प्रोजेक्ट](https://github.com/Niko1221/Strata) में कम से कम 12GB VRAM वाले चुनिंदा NVIDIA और AMD कार्डों तथा 32GB RAM सिस्टम के लिए छोटे मॉडल दर्ज हैं। ये विकल्प 16GB GPU, 64GB RAM और IQ3_S वाले परीक्षण को दोहराते नहीं हैं। हार्डवेयर खरीदने से पहले सही GPU, model variant और runtime support जाँचें।

## Model कहाँ रहता है

**Mixture of experts**, या MoE, हर token के लिए model के expert networks का एक subset activate करता है। हर step पर सभी parameters चलाने की तुलना में active computation घटता है। बाकी weights को फिर भी storage और computation तक रास्ता चाहिए।

**Strata का hybrid execution** अक्सर उपयोग होने वाले experts को GPU पर रखता है और expert collection को system RAM में रखता है। CPU uncached experts को वहीं compute करता है और GPU cached experts संभालता है। Storage में model files और lookup data भी रहते हैं। System पूरे 125B model को 16GB VRAM में नहीं रखता।

**GPU memory कई कामों के बीच बँटती है।** Runtime allocation, attention state और expert cache एक सीमित संसाधन साझा करते हैं। Context के लिए अधिक memory देने पर expert cache की बची क्षमता घटती है। Strata के मौजूदा versions KV-cache streaming का भी समर्थन करते हैं, इसलिए data placement पुराने configuration से अलग है। अपने engine version के [तकनीकी दस्तावेज़](https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md) देखें।

{{< figure src="local-agent-gpu-ram-expert-cache.webp" alt="Illustration of a local workstation distributing model execution across a graphics card, system memory, and solid-state storage" caption="The GPU is one part of the inference system, alongside CPU execution, system RAM, and storage" >}}

## प्रॉम्प्ट का पुनः उपयोग गति को बदलता है

**Coding agent loop में चलता है:** task पढ़ता है, tool action माँगता है, result पाता है और अगला action चुनता है। File contents, errors और test output conversation में जमा होते हैं। Agents context को compact या select भी करते हैं, इसलिए हर implementation हमेशा पूरी unchanged history नहीं भेजती।

**Prefill** generation से पहले input tokens process करता है। **Decode** response बनाता है। Fast decode लेकिन slow repeated prefill वाला system tool calls के बीच आपको प्रतीक्षा करवाता है।

**Reported 44K-token timing में prefix reuse था।** Strata ने पहले process किए गए conversation content को reuse किया और बढ़ता prompt लगभग एक से तीन seconds में तैयार हुआ। Continuing agent session के लिए यह उपयोगी evidence है। यह सिद्ध नहीं करता कि 44,000 बिल्कुल नए tokens को एक second में scratch से process किया गया।

| Measurement | क्या record करें |
|---|---|
| **Cold prompt** | Reusable prefix state के बिना new content का समय |
| **Warm continuation** | Existing context में tool result जोड़ने के बाद का समय |
| **Generation speed** | Response के दौरान tokens per second |
| **कार्य अवधि** | Planning, generation, tools, tests और retries साथ में |

**दो caches के अलग उद्देश्य हैं।** Expert cache अक्सर उपयोग होने वाले weights को GPU computation के पास रखता है। Prefix reuse पहले के input पर दोहराया काम बचाता है। High expert-cache hit rate prompt-cache hit सिद्ध नहीं करता।

## Tasks ने क्या दिखाया

| Task | रिपोर्ट किया गया समय | Reported outcome |
|---|---|---|
| **Build task manager** | 3m 38s | Express API, interface, 5/5 tests |
| **संपादन सुधारें और तारीखें जोड़ें** | 4m 58s | Changes complete, 6/6 tests |
| **निर्यात, आयात और पैकेजिंग जोड़ें** | 3m 48s | 7/7 tests, Docker build unverified |
| **Racing game, first attempt** | 6m 35s | Reasoning में output खत्म, कोई code नहीं |
| **Racing game, budgeted retry** | 4m 51s | Game generated, JavaScript syntax checked |

**[प्रकाशित परिणाम फ़ाइल](https://raw.githubusercontent.com/network-tocoder/Free-Local-AI-Coding-Agent-125B-on-16GB-GPU/main/results.csv)** पहले task में 48–52, दूसरे में 40–43 और तीसरे में 37–44 tokens per second की गति दर्ज करती है। “Up to 52” इन मापों में सबसे अधिक गति है, हर task की लगातार बनी रहने वाली दर नहीं।

**पहले तीन tasks एक application को बढ़ाते हैं।** 5/5, 6/6 और 7/7 successive test suites हैं। इन्हें जोड़ना 18 independent capabilities सिद्ध नहीं करता। उसी agent द्वारा लिखे tests की coverage और assertions की समीक्षा भी चाहिए।

**Environmental recovery work का हिस्सा थी।** Agent ने inappropriate shell command से recover किया और testing के दौरान stale application server पहचाना। ये उपयोगी behaviors हैं, फिर भी shared development environment में existing process terminate करने के लिए deliberate permission चाहिए।

**Docker unverified रहा।** Agent ने Dockerfile लिखा, पर build के लिए running Docker engine नहीं था। Container के बाहर passing application tests working image सिद्ध नहीं करते। Game retry ने syntax check किया और browser खोला, पर agent के पास gameplay की direct visual confirmation नहीं थी।

## Output के लिए जगह रखें

```json
{
  "reasoning_budget_tokens": 8000
}
```

**यह setting existing `strata-iq3_s.json` configuration में merge करें**, दूसरे fields बचाएँ और selected Strata model restart करें। यह Strata setting है, OpenCode configuration file का replacement नहीं। Startup output में active budget verify करें।

**Strata hard reasoning budget document करता है** जो thinking phase समाप्त करके answer की ओर बढ़ता है। Request-level value configured default को override करती है। यह setting low या high जैसी general reasoning-effort instruction से अलग है।

**First game attempt ने planning के दौरान अपना 16,384-token allowance समाप्त कर दिया।** Retry ने 8,000-token thinking budget लगाया और code दिया। यह workload के लिए bounded reasoning phase का समर्थन करता है। यह 8,000 को हर task के लिए best setting सिद्ध नहीं करता।

**Remaining output allowance maximum है, reservation guarantee नहीं।** 16,384 total limit के भीतर 8,000-token cap पूरा खर्च हो तो अन्य overhead से पहले लगभग 8,384 tokens बचेंगे। Results log retry पर 11,054 written tokens report करता है, पर reasoning और code का complete split नहीं देता। इसे उसी limit के भीतर 8,000 reasoning plus 11,054 code न समझें।

**Narrow edits के लिए छोटा budget रखें**, फिर अधिक analysis वाले tasks पर बड़े budgets test करें। Complete file output, finish status और test results देखें। अधिक planning time तभी उपयोगी है जब delivered change सुधरे।

## Strata और OpenCode connect करें

```bash
git clone https://github.com/Niko1221/Strata.git
cd Strata
./setup.sh
```

**यह Linux setup entry point है।** Current installation instructions देखें और documented Windows path के लिए **`START-HERE.bat`** इस्तेमाल करें। Reported configuration के करीब जाने के लिए original Qwen3.8-Flash-Next IQ3_S variant और 65,536-token context चुनें। Benchmark notes में engine version और model files save करें।

```bash
npm install -g opencode-ai
```

**OpenCode इंस्टॉल करें** और इसके [आधिकारिक निर्देश](https://opencode.ai/docs/) अपनाएँ। दूसरे terminal में **`STRATA_BASE_URL`** को Strata से मिले local API address पर सेट करें और अंत में **`/v1`** जोड़ें। इस व्यवस्था में inference को local machine तक सीमित रखें।

```json
{
  "provider": {
    "strata": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Strata local",
      "options": {
        "baseURL": "{env:STRATA_BASE_URL}",
        "apiKey": "local"
      },
      "models": {
        "qwen3.8-flash-next-iq3_s": {
          "name": "Qwen3.8-Flash-Next IQ3_S",
          "limit": { "context": 65536, "output": 16384 }
        }
      }
    }
  },
  "model": "strata/qwen3.8-flash-next-iq3_s"
}
```

**मौजूदा settings बचाते हुए provider block को `~/.config/opencode/opencode.json` में जोड़ें।** [प्रकाशित उदाहरण कॉन्फ़िगरेशन](https://raw.githubusercontent.com/network-tocoder/Free-Local-AI-Coding-Agent-125B-on-16GB-GPU/main/config/opencode.json) environment variable से local endpoint का address लेता है। OpenCode [कस्टम प्रदाता](https://opencode.ai/docs/providers/) और [परिवेश चर प्रतिस्थापन](https://opencode.ai/docs/config/) का समर्थन करता है।

**`local` placeholder credential है**, example के unauthenticated local setup से मेल खाता है। यह server को secure नहीं करता। Strata instance authentication enable करता हो तो appropriate local secret mechanism से configured credential दें।

**Disposable project copy में `opencode` शुरू करें** और configured model चुनें। Code भेजने से पहले selected provider verify करें। Client-side context declaration server का configured context नहीं बढ़ाती, और 65,536-token window input के लिए पूरी 65,536 जगह नहीं छोड़ती जब output के लिए भी स्थान चाहिए।

## Local inference और permissions

```json
{
  "permission": {
    "edit": "ask",
    "bash": "ask"
  }
}
```

**Agent का मूल्यांकन करने से पहले OpenCode configuration में शुरुआती permissions जोड़ें।** [अनुमति संबंधी दस्तावेज़](https://opencode.ai/docs/permissions/) उपलब्ध controls समझाते हैं। Inference जहाँ भी चले, file में बदलाव और shell commands आपकी machine को प्रभावित करते हैं।

**Local inference हर tool को local नहीं बनाता।** Package downloads, web tools, external integrations और optional sharing अब भी network services लेते हैं। Private repositories संभालने से पहले enabled tools देखें। “Model locally runs” का अर्थ “कुछ भी computer से बाहर नहीं जाता” नहीं है।

## पहली बार की समस्याओं का समाधान

| Symptom | पहले क्या जाँचें |
|---|---|
| **Provider unavailable** | Strata चल रहा है और environment variable OpenCode process तक पहुँचता है |
| **Model selection में नहीं** | Provider ID और model ID saved configuration से मेल खाते हैं |
| **Context-limit error** | Prompt length और requested output server की active window में फिट हैं |
| **Planning without code** | Reasoning budget, total output limit और finish status |
| **Slow continuation** | Prefix reuse, memory pressure, expert-cache behavior और competing processes |
| **Docker command fails** | Working engine उपलब्ध है, केवल command-line client नहीं |

**एक समय में एक setting बदलें** और saved starting state से वही task दोहराएँ। इससे configuration improvement को अलग prompt या आसान test से अलग रखा जाता है।

## क्या यह subscription बदलता है?

| Local setup test करने योग्य है | दूसरी option उपलब्ध रखें |
|---|---|
| **Compatible hardware पहले से है** | Untested workload के लिए ही hardware खरीदना |
| **Bounded application changes** | Large unfamiliar repositories और difficult migrations |
| **Repeatable acceptance tests** | Correctness जाँचने का reliable तरीका न होना |
| **Runtime maintenance का समय** | Minimal setup और support overhead वाला काम |

**Zero API spend महत्वपूर्ण है**, खासकर जब hardware पहले से हो। इसमें electricity, hardware depreciation, storage और environment maintenance time शामिल नहीं हैं। Displayed zero-cost field भी इन खर्चों को meter नहीं करता।

**Subscription comparison के लिए matched tasks चाहिए।** दोनों systems में same starting repository, instructions और acceptance checks चलाएँ। Retries और human corrections को elapsed time के साथ record करें। Full workflow में first failed game attempt भी रखें, केवल successful retry report न करें।

**Useful local agent को universal superiority नहीं चाहिए।** यदि वह routine edits reliably संभालता है और कठिन tasks का छोटा set किसी अन्य tool को देता है, तो वह पहले से बदलता है कि आपको कौन सी paid services चाहिए। अपने projects पर accepted work से निर्णय लें।

## प्रदर्शन और अगले कदम

{{< youtube id="QBPbvMaHkJc" enable="true" title="Local coding agent test with Strata, OpenCode, and a 16GB GPU" >}}

**आगे देखें:** [125B local coding agent का प्रदर्शन](https://www.youtube.com/watch?v=QBPbvMaHkJc)। ऊपर के माप प्रकाशित परीक्षण के हैं। ये इस लेख के लिए किया गया स्वतंत्र benchmark नहीं हैं।

1. **एक छोटा task दोहराएँ** fixed acceptance criteria और saved starting revision के साथ।
2. **Cold और warm turns मापें**, prefix reuse को cold prefill speed न मानें।
3. **Packaging अलग verify करें** successful image build, startup और container-level checks से।
4. **Generated tests inspect करें** और वे cases जोड़ें जिनका implementation ने अनुमान नहीं लगाया।
5. **Completed work compare करें** subscription बदलने से पहले current coding tool के साथ।

**हार्डवेयर योजना के लिए**, [स्थानीय AI model और GPU संदर्भ मार्गदर्शिका](/articles/local-ai-model-gpu-context-guide/) पढ़ें। Hosted model के व्यवहार और लागत के लिए [OpenRouter प्रदाता routing मार्गदर्शिका](/articles/openrouter-provider-routing-quality-cost/) देखें।
