---
title: "Vast.ai पर Llama 3.1 8B और Qwen3.8 27B GPU बेंचमार्क"
date: 2026-10-02
lastmod: 2026-10-10
toc: true
draft: false
description: "प्रमुख Vast.ai GPU पर Llama 3.1 8B और Qwen3.8 27B के मापे गए Ollama बेंचमार्क। डिकोड गति, लंबे संदर्भ, किराया लागत, self-hosting, API क्रेडिट और सदस्यताओं की तुलना।"
genre: ["स्थानीय AI", "GPU बेंचमार्किंग", "Self-hosted AI", "क्लाउड कंप्यूटिंग", "कृत्रिम बुद्धिमत्ता", "AI अर्थशास्त्र"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "GPU बेंचमार्क", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "स्थानीय LLM", "लंबा संदर्भ", "GPU किराया", "self-hosted AI", "abliterated मॉडल", "uncensored मॉडल", "API क्रेडिट", "AI सदस्यता", "Q4_K_M", "प्रति सेकंड टोकन"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "ग्राफिक्स कार्ड और स्थानीय AI बेंचमार्क परिणाम दिखाती स्क्रीन वाला हाई-टेक कार्यस्थल"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**दोनों Ollama परीक्षणों में H100 SXM सबसे तेज कार्ड था, लेकिन सबसे अच्छा मूल्य नहीं था।** RTX PRO 5000 और RTX 6000 Ada ने गति और किराया लागत का बेहतर संतुलन दिया। पूरे हुए Qwen3.8 27B परीक्षणों में CMP 170HX का प्रति घंटे मूल्य सबसे कम था।

*ये परिणाम एक मॉडल, एक Ollama wrapper, एक डिफ़ॉल्ट quantization और एक serving pattern को मापते हैं। इन्हें इस workload के sizing data की तरह देखें, सार्वभौमिक GPU ranking की तरह नहीं।*

यह लेख **Llama 3.1:8b**, 8.03B parameters वाली Ollama Q4_K_M build, और **Qwen3.8:27b**, लगभग 27.3B parameters वाली Ollama Q4_K_M build की तुलना करता है। दोनों का परीक्षण Vast.ai से किराये पर ली गई GPU instances पर हुआ। परीक्षणों ने समर्थित context limit तक वास्तविक prompt लंबाई पर decode throughput मापा।

## संक्षिप्त उत्तर

**नियमित single-user काम के लिए RTX PRO 5000 या RTX 6000 Ada किराये पर लें।** छोटे और मध्यम context में RTX PRO 5000 का मूल्य सबसे अच्छा था। RTX 6000 Ada सस्ता था और A100 cards से आगे रहा। जब response speed hourly cost से अधिक महत्वपूर्ण हो, या prompts लंबे हों, H100 SXM लें।

| लक्ष्य | सुझाव | कारण |
|---|---|---|
| **सबसे कम परीक्षण लागत** | CMP 170HX | $0.420 प्रति घंटा और tested Q4_K_M models के लिए पर्याप्त VRAM |
| **$1.25/hr से कम में सर्वोत्तम मूल्य** | RTX PRO 5000 या RTX 6000 Ada | H100 किराये के बिना अच्छा decode speed |
| **सबसे तेज उत्तर** | H100 SXM | दोनों model tests में सबसे अधिक decode speed |
| **लंबे context वाला Qwen काम** | H100 SXM या RTX PRO 6000 Max-Q | दोनों ने लगभग 131k-token Qwen run पर्याप्त VRAM headroom के साथ पूरा किया |
| **लोकप्रिय 8B baseline** | Llama 3.1:8b | 128K context limit वाली व्यावहारिक 8B तुलना |
| **छोटा recurring workload** | API credits या chat subscription | idle GPU, maintenance और deployment का खर्च नहीं |
| **निजी और लगातार workload** | अपनी GPU workstation | sustained utilization में hardware cost उचित ठहरती है |
| **Abliterated या uncensored प्रयोग** | पहले किराये पर लें, लगातार उपयोग के बाद ही खरीदें | behavior, license और operational risk की अलग जाँच आवश्यक है |

## क्या परीक्षण किया गया

**Benchmark ने default Q4_K_M model build के साथ Ollama का उपयोग किया।** Special quantization, speculative decoding, custom sampler या अलग serving stack नहीं जोड़ा गया। उद्देश्य GPU instances की सरल, reproducible तुलना था।

Vast.ai अपनी सेवा को compute providers और users को जोड़ने वाला GPU cloud marketplace बताता है। Documentation में on-demand, reserved, interruptible और serverless विकल्प तथा GPU model, memory, price और availability filters हैं। नीचे के hourly rates इसी session में चुनी गई instances से आए हैं, स्थायी price list से नहीं।

मापा गया output **decode throughput** था, यानी प्रति सेकंड generated tokens। Prefill throughput अलग दिया गया है क्योंकि वह prompt processing मापता है, उत्तर दिखने की गति नहीं। लंबा prompt decode speed ऊँची रहने पर भी काफी processing time लेता है।

हर context पर दो valid trials लिए गए और median decode result दर्ज किया गया। पूरे हुए स्तर वास्तविक `prompt_eval_count` पर आधारित थे:

- **लगभग 16.4k prompt tokens**
- **लगभग 32.8k prompt tokens**
- **लगभग 65.5k prompt tokens**
- **लगभग 131k prompt tokens**

मांगा गया 256k-token run पूरा नहीं हुआ। 40 GB A100 cards और कई छोटे cards target context पर processing में थे या पूरा नहीं कर सके।

> **Benchmark सीमा:** ये आँकड़े एक serving pattern में दो Ollama Q4_K_M workloads बताते हैं। ये training speed, multi-user throughput, image generation, vLLM performance या किसी दूसरे model के परिणाम का अनुमान नहीं हैं।

## Llama 3.1 8B rerun

**Llama 3.1:8b उसी GPU pool के लिए व्यावहारिक baseline है।** Ollama लगभग 120 million downloads बताता है। [Official Ollama model page](https://ollama.com/library/llama3.1:8b) 4.9 GB Q4_K_M build, 8.03B parameters और 128K context window बताती है।

Rerun ने model-specific benchmark runner और Ollama tokenizer के अनुसार calibrated prompt generator इस्तेमाल किया। Labels requested settings के बजाय वास्तविक counts हैं:

- **32k target के लिए लगभग 32,676 actual prompt tokens**
- **64k target के लिए लगभग 65,342 actual prompt tokens**
- **128k target के लिए लगभग 130,671 actual prompt tokens**

Llama 3.1 8B की listed context limit 128K है, इसलिए 256k unsupported है। Runner ने retries और status rows रखीं, इसलिए timeout गायब नहीं होता।

### Llama 3.1 8B परिणाम

| GPU | ~32k decode tok/s | ~64k decode tok/s | ~128k decode tok/s |
|---|---:|---:|---:|
| **H100 SXM** | **163.5** | **124.0** | **82.4** |
| **H100 SXM** | **158.6** | **121.2** | **80.6** |
| **RTX PRO 5000** | 110.1 | 79.8 | 49.9 |
| **CMP 170HX 64GB** | 91.9 | 71.0 | 50.1 |
| **RTX 6000 Ada** | 88.3 | 53.9 | 29.3 |
| **RTX PRO 6000 Max-Q** | 66.7 | 53.0 | 40.3 |
| **RTX PRO 6000 S** | 60.3 | 42.5 | 33.9 |
| **A100 SXM4 40GB** | 2.0 | 40.6 | 38.5 |
| **A100 PCIe 40GB** | 1.2 | 20.3 | 20.3 |
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Timeout |

दो H100 rows एक ही GPU class की अलग valid instances से थीं। दोनों अन्य cards से स्पष्ट रूप से आगे थीं। 32k पर वे RTX PRO 5000 से 44% से 48% तेज थीं। 128k पर बढ़त लगभग 61% से 65% थी। A100 और RTX 5060 Ti के 32k results comparable GPU execution नहीं दिखाते। RTX 5060 Ti host दूसरे 128k trial में timeout हुआ। इसे valid GPU comparison के लिए अनुपयुक्त मानें।

| Context target | स्थिति |
|---|---|
| **32k** | सभी 10 hosts पर पूरा |
| **64k** | सभी 10 hosts पर पूरा |
| **128k** | 9 hosts पर पूरा। 2x RTX 5060 Ti host दूसरे trial में timeout हुआ |
| **256k** | सभी hosts के लिए unsupported, क्योंकि Llama 3.1 8B अधिकतम 128K context support करता है |

## दोनों models की तुलना

**छोटा Llama model हर comparable GPU पर तेज था, लेकिन model size और quality एक-दूसरे के बदले नहीं हैं।** Llama 3.1 8B कम memory वाला लोकप्रिय baseline है। Qwen3.8 27B अधिक memory लेता है और अलग capability profile देता है। इन numbers का उपयोग hardware selection के लिए करें, universal winner घोषित करने के लिए नहीं।

| Use case | बेहतर benchmark reference | कारण |
|---|---|---|
| **तेज 8B assistant** | Llama 3.1:8b | अधिक decode speed और कम model memory |
| **27B local sizing** | Qwen3.8:27b | बड़े single-GPU workload के लिए अधिक प्रतिनिधि |
| **128K context ceiling** | Llama 3.1:8b | explicit 128K limit के कारण 256k valid target नहीं |
| **VRAM headroom test** | Qwen3.8:27b | बड़ा model memory और long-context limits जल्दी दिखाता है |
| **Cross-provider baseline** | Llama 3.1:8b | popularity और size से result दोहराना आसान |

पहले Qwen rerun ने supported levels पर actual counts लगभग **32,770**, **65,538** और **131,074** tokens सुधारे। Qwen तुलना में ये corrected labels requested `num_ctx` values की जगह इस्तेमाल होते हैं।

## लगभग 16k tokens

**H100 SXM ने short-context run में 134.4 decode tokens प्रति सेकंड प्राप्त किए।** RTX PRO 5000 113.9 tokens प्रति सेकंड पर थी और उसका hourly rate आधे से कम था।

| Rank | GPU | VRAM | Decode tok/s | Prefill tok/s | Rental rate |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

## लगभग 32.8k tokens

**Medium context में ranking स्थिर रही।** H100 SXM 120.0 tokens प्रति सेकंड, RTX PRO 5000 105.0 और RTX 6000 Ada 75.7 पर पहुँची।

| Rank | GPU | VRAM | Decode tok/s | Prefill tok/s | Rental rate |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

## लगभग 65.5k tokens

**लंबे prompts ने memory capacity और headroom के बीच बड़ा अंतर दिखाया।** H100 112.0 tokens प्रति सेकंड पर पहले रहा। RTX PRO 6000 Max-Q decode speed में RTX 6000 Ada से आगे आया।

| Rank | GPU | VRAM | Decode tok/s | Prefill tok/s | Rental rate |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

## लगभग 131k tokens

**इस context length पर H100 ही 100 decode tokens प्रति सेकंड से ऊपर था।** RTX PRO 6000 Max-Q 73.4 पर और RTX 6000 Ada 61.7 पर पूरा हुआ।

| Rank | GPU | VRAM | Decode tok/s | Prefill tok/s | Rental rate |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | N/A | N/A | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | N/A | N/A | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | N/A | N/A | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

## Overall decode comparison

| GPU | ~16k | ~32.8k | ~65.5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | N/A |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | N/A |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | N/A |
| **A100 PCIe** | 38.4 | 36.1 | N/A | N/A |

**H100 ने हर completed context length में lead किया।** इसका advantage RTX PRO 5000 पर लगभग 16k में 20.5 tokens प्रति सेकंड से 32.8k में 12.0 तक घटा। Fast first response और लंबे session की कम लागत के बीच चुनाव करें।

## प्रति million decode tokens लागत

**Hourly price अकेले उपयोगी तुलना छिपाता है।** Supplied hourly rate को decode throughput से divide करने पर one million generated tokens की rough rental cost मिलती है। इसमें prompt processing, idle time, storage, transfer, tax, discount और failed runs शामिल नहीं हैं।

| GPU | Short-context rate | लगभग लागत प्रति 1M decode tokens |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**CMP 170HX इस सीमित arithmetic comparison में जीता।** RTX PRO 5000 और RTX 6000 Ada पास थे तथा दोनों अधिक throughput देते थे। Interactive use में extra waiting time अक्सर lowest token cost से अधिक महत्वपूर्ण है।

## किराया, credits, subscription या hardware?

**सही विकल्प utilization और control requirements पर निर्भर है।** GPU rental variable compute bill है। API credits variable model bill हैं। Chat subscription fixed access fee और usage limits देता है। Owned hardware capital purchase के बाद electricity, cooling, maintenance और depreciation लाता है।

| Monthly budget और workload | Recommended path | कारण | मुख्य compromise |
|---|---|---|---|
| **$10 से कम** | API credits खरीदें या free local model लें | idle GPU cost के बिना workflow साबित होता है | hosting और rate limits पर कम control |
| **$10 से $30** | occasional काम के लिए API credits, daily chat के लिए subscription | credits scripts के लिए, subscription human chat के लिए | default private 27B endpoint नहीं |
| **$30 से $100** | active sessions में RTX 6000 Ada या RTX PRO 5000 किराये पर लें | short bursts cover होते हैं और ownership overhead बचता है | setup, storage, monitoring और shutdown आवश्यक |
| **$100 से $250** | scheduled work के लिए तेज card किराये पर लें या owned plan test करें | sustained use दिखाई देने लगता है | rates और availability बदलती है |
| **$250 से $600** | एक महीने का PRO 5000 rental local GPU से तुलना करें | frequent private inference का निर्णय बिंदु | power, heat, support और resale risk |
| **$600 से अधिक** | high utilization पर ही खरीदें या burst के लिए H100 reserve करें | mixed strategy peak hardware ownership से बचाती है | capital एक configuration में बंधता है |

H100 $2.693/hr पर लगातार 24 घंटे में लगभग $64.63 और 30 दिनों में $1,941.00 पड़ता है। RTX PRO 5000 $1.005/hr पर लगभग $24.12 प्रतिदिन और $723.60 प्रति 30 दिन पड़ती है। केवल active sessions वाला total अलग होगा।

### API credits कब बेहतर हैं

**जब usage irregular हो, automation महत्वपूर्ण हो और किसी खास local model की आवश्यकता न हो, API credits बेहतर हैं।** वे provisioning, downloads, drivers और idle time से बचाते हैं। OpenRouter catalog model context, providers और token pricing की तुलना करता है। Live calculator से bill जाँचें।

### Subscription कब बेहतर है

**हर दिन hosted assistant इस्तेमाल करने वाले व्यक्ति के लिए subscription उपयुक्त है।** Claude के individual plans Free, Pro और Max access को अलग limits और features के साथ रखते हैं। Subscription API access नहीं है। Interactive writing, research, coding और file review में इसका उपयोग करें। Script या agent को metered endpoint चाहिए तो API credits चुनें।

### Vast.ai कब बेहतर है

**Open model, private runtime control या थोड़े समय के high throughput के लिए Vast.ai बेहतर है।** GPU चुनें, instance launch करें, Ollama चलाएँ, model test करें और काम के बाद instance बंद करें। GPU usage, VRAM, exposed service और shutdown की जाँच आपकी जिम्मेदारी है।

### GPU खरीदना कब बेहतर है

**Sustained utilization, stable model requirements और local control के बाद hardware खरीदना उचित है।** Purchase availability risk हटाता है और private data को hosted provider के बिना चलाने देता है। Host, power supply, storage, cooling, electricity, replacement और setup time भी लागत में जोड़ें। RTX 4090 reference specs 24 GB memory, 450 W graphics power और 850 W minimum system power बताती हैं। यह tested 27B Q4_K_M configuration के लिए 24 GB से कम है, इसलिए वास्तविक model memory जाँचें।

## Abliterated और uncensored models

**Abliterated और uncensored variants खरीद निर्णय बदलते हैं।** कम refusals आकर्षक हो सकते हैं, पर safety behavior कमजोर, provenance अनिश्चित, prompt format inconsistent और license limits संभव हैं। पहले किराये पर लें। दिए rate पर RTX PRO 5000 का एक दिन लगभग $24.12 पड़ता है।

**Uncensored model को सीधे public Internet पर expose न करें।** Authentication, rate limits, logging controls और network isolation लगाएँ। बिना समीक्षा वाले source को personal, confidential या regulated data न दें।

## Benchmark caveats

**Missing results भी result का हिस्सा हैं।** `N/A` valid measurement न बनने का अर्थ है, दूसरे card के score जितनी धीमी GPU होने का नहीं। दूसरा H100 model download देर से पूरा होने के कारण valid set नहीं बना सका। 2x RTX 5060 Ti CPU execution के कारण exclude हुआ। Qwen 256k पूरा नहीं हुआ और उसका highest valid level लगभग 131k actual tokens था। Requested `num_ctx` ranking label नहीं था और final tables actual `prompt_eval_count` values इस्तेमाल करती हैं। दो valid trials का median लिया गया। Tuned vLLM या llama.cpp अलग ranking देंगे।

## अंतिम सिफारिश

**RTX 6000 Ada या RTX PRO 5000 rental से शुरू करें।** $0.813/hr उपलब्ध हो तो RTX 6000 Ada budget choice है। H100 SXM long prompts और latency के लिए लें। 8B model के लिए CMP 170HX को कम hourly rate के कारण test करें। एक सफल test के बाद GPU न खरीदें। वास्तविक workloads का एक महीना चलाएँ, active hours, prompt lengths, concurrency और model changes लिखें और ownership bill से तुलना करें।

Occasional work के लिए API credits या chat subscription सरल हैं। Private local inference, open models या abliterated testing के लिए Vast.ai workstation खरीदने से कम commitment देता है। Llama 3.1 8B low-memory baseline और Qwen3.8 27B actual deployment target के लिए रखें।

## अगले कदम

अपने prompt lengths और active-hour estimate के साथ comparison दोहराएँ। GPU use verify करें, model revision और runtime version लिखें, हर run के बाद instance बंद करें और खरीद से पहले monthly rental को full ownership cost से तुलना करें।

## संदर्भ

1. [Vast.ai GPU cloud marketplace](https://vast.ai/)
2. [Vast.ai documentation: marketplace, instances, pricing और rental types](https://docs.vast.ai/)
3. [Ollama Qwen3 model library](https://ollama.com/library/qwen3)
4. [Ollama Llama 3.1 8B model page](https://ollama.com/library/llama3.1:8b)
5. [OpenRouter model catalog और pricing comparison](https://openrouter.ai/models)
6. [Claude pricing और individual subscription plans](https://www.anthropic.com/pricing)
7. [NVIDIA GeForce RTX 4090 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [2026 में local AI: Qwen3.8 27B और self-hosted model hardware](/articles/local-ai-2026-build-your-rig-now/)
9. [Raspberry Pi hardware पर Ollama model testing](/articles/ai-models-raspberry-pi-4-5/)
