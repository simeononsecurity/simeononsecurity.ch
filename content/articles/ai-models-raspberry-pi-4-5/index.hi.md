---
title: "Raspberry Pi 4 या 5 पर कौन से AI मॉडल चल सकते हैं?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Raspberry Pi 4 और 5 के मापे गए परिणामों से मेमोरी, गति और काम के अनुसार स्थानीय भाषा मॉडल चुनें, छोटे LFM2.5 से 3B और बड़े विकल्पों तक।"
genre: ["Raspberry Pi", "कृत्रिम बुद्धिमत्ता", "स्व-होस्टिंग"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "स्थानीय AI", "छोटे भाषा मॉडल", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "मॉडल क्वांटाइज़ेशन", "एज AI"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "गहरे रंग की मेज पर दो Raspberry Pi कंप्यूटर, ऊपर नीले और एम्बर रंग के न्यूरल नेटवर्क चित्र"
coverCaption: "Raspberry Pi हार्डवेयर पर चलने वाले स्थानीय AI मॉडल का चित्र।"
---

Raspberry Pi स्थानीय रूप से उपयोगी भाषा मॉडल चला सकता है, लेकिन मॉडल बोर्ड की मेमोरी में फिट होना चाहिए और आपके ऐप के लिए स्वीकार्य समय में जवाब देना चाहिए। 2 GB वाला Raspberry Pi 4 लगभग एक अरब से कम पैरामीटर वाले मॉडल के लिए उपयुक्त है। 8 GB वाला Raspberry Pi 5 छोटे 1B–3B मॉडल आसानी से चलाता है और कुछ बड़े क्वांटाइज़्ड मॉडल भी लोड कर सकता है, लेकिन बड़े समझौतों के साथ।

हमने Ollama से **2 GB Pi 4B** और **8 GB Pi 5** पर इन मॉडलों का परीक्षण किया। दोनों में microSD स्टोरेज था। तालिका के परीक्षणों में वही पाँच छोटे सहायक prompts, वही system prompt, निश्चित seed और 140-token आउटपुट सीमा रही। हर परीक्षण से पहले दूसरे मॉडल unload किए और cold-load समय, पहले दिखाई देने वाले token तक का समय, पूरा उत्तर समय, आउटपुट गति और अधिकतम resident memory मापी। ये छोटे उत्तरों वाले काम के एक-पास परीक्षण थे। परिणाम संसाधन का अनुमान हैं, सार्वभौमिक गति या उत्तर-गुणवत्ता रैंकिंग नहीं। Pi 5 का [Cortex-A76 CPU और उपलब्ध मेमोरी विन्यास](https://www.raspberrypi.com/products/raspberry-pi-5/) Pi 4 के [Cortex-A72 प्लेटफॉर्म](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf) से भी काफी अलग है।

## कौन से मॉडल प्रकार उपयुक्त हैं

| मॉडल प्रकार | माप में शामिल उदाहरण | व्यावहारिक उपयोग |
|---|---|---|
| लगभग 230M–600M पैरामीटर वाले छोटे टेक्स्ट मॉडल | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | छोटे स्थानीय आदेश, सारांश और सीमित प्रश्नोत्तर; 2 GB Pi 4 के लिए सबसे अच्छा आरंभ |
| लगभग 1B–2B कॉम्पैक्ट टेक्स्ट मॉडल | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Pi 5 या अधिक मेमोरी वाले Pi 4 पर सूक्ष्म निर्देशों की बेहतर क्षमता, छोटे मॉडल से धीमे उत्तर |
| क्वांटाइज़्ड 3B–4B टेक्स्ट मॉडल | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | 8 GB Pi 5 के अधिक सक्षम विकल्प, यदि हर उत्तर के लिए कुछ सेकंड इंतजार स्वीकार्य हो |
| बड़े sparse या hybrid मॉडल | LFM2.5 8B | परीक्षण किए गए 8 GB Pi 5 पर तकनीकी रूप से चलता है, लेकिन मेमोरी ज्यादा लेता और cold-load में देर करता है |

ये **टेक्स्ट जनरेशन** के परिणाम हैं। ये इमेज जनरेशन, वाक् पहचान, vision या training का प्रदर्शन नहीं बताते। “चलता है” का अर्थ सिर्फ मॉडल फाइल का कार्ड में फिट होना नहीं है। Runtime, context cache, ऑपरेटिंग सिस्टम और दूसरी सेवाओं को भी RAM चाहिए। Quantization वजन की फाइल छोटी करती है, लेकिन उत्तर की गुणवत्ता घटा सकती है, खासकर 1-bit वजन जैसे चरम विकल्पों पर।

### आंकड़े क्या मापते हैं

Benchmark ने Ollama chat API को तथ्य, सुरक्षा प्रक्रिया, retrieved context, मौसम और सहायता पर छोटे prompts भेजे। हर मॉडल को वही prompt-set और seed मिला। समय मापने से पहले मॉडल unload किया ताकि अगली request में cold-load शामिल हो। **कुल समय** पूरी request का है, जबकि **tokens per second** केवल आउटपुट जनरेशन बताता है। हमने पहला *दिखाई देने वाला* token भी दर्ज किया, क्योंकि मॉडल जवाब से पहले reasoning में समय लगा सकता है।

मेमोरी के लिए हर request के दौरान Pi की उपलब्ध RAM और swap के साथ Ollama तथा inference process की resident memory देखी। **RSS** process की resident memory है, पूरे host की जरूरत नहीं। File-backed pages, OS, browser या दूसरी स्थानीय सेवा से ऐसा मॉडल भी swap कर सकता है जो नाममात्र फिट बैठता हो। तालिकाएं पांच prompts वाले शुरुआती single-pass runs दिखाती हैं। बाद में हमने news prompt और reply-rule checks जोड़े। वे जांच में मदद करते हैं, पर पुराने timing को छह-prompt compliance परिणाम नहीं बनाते।

न tokens per second, न पैरामीटर संख्या गुणवत्ता का स्कोर है। मॉडल तेजी से पाठ दे सकता है, फिर भी स्रोत छोड़ सकता है, शब्द सीमा लांघ सकता है या वाक्य अधूरा छोड़ सकता है। जिन prompts का इस्तेमाल करेंगे उन्हीं पर मॉडल की तुलना करें और ऐप के लिए चुनने से पहले उत्तर पढ़ें।

## Raspberry Pi 4: सबसे छोटे मॉडल चुनें

जांचे गए 2 GB Pi 4 में बहुत कम headroom था। सबसे छोटे LFM2.5 मॉडल ने पांचों prompts पूरे किए, जैसा `qwen2.5:0.5b` ने भी किया। छोटे offline जवाब या स्थानीय सहायक के लिए ये उचित विकल्प हैं।

| मॉडल | मॉडल फाइल | मापी गई आउटपुट गति | औसत जवाब समय | मापी गई मेमोरी या परिणाम |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF import | 0.25 GB | 12.8 tokens/s | 7.2 s | अधिकतम resident memory 383 MB; 5/5 prompts |
| LFM2.5-350M, GGUF import | 0.38 GB | 8.6 tokens/s | 8.6 s | अधिकतम resident memory 516 MB; 5/5 prompts |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 prompts; Ollama से सीधे उपलब्ध |
| MiniCPM5-1B, GGUF import, reasoning off | 0.69 GB | 5.9 tokens/s | 12.2 s | अधिकतम resident memory 883 MB; 5/5 prompts |
| MiniCPM5-1B, GGUF import, default reasoning | 0.69 GB | 5.7 tokens/s | 33.3 s | पांच में केवल एक उपयोगी दिखाई देने वाला जवाब |
| `qwen3:0.6b`, default reasoning | 0.52 GB | 6.4 tokens/s | 40.4 s | एक खाली जवाब; बोर्ड reboot हुआ |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, swap या reboot नहीं; धीमा लेकिन स्थिर |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | भारी swapping; परीक्षण के दौरान बोर्ड reboot हुआ |
| `qwen3.5:0.8b` | 1.04 GB | — | — | पूरा नहीं हुआ; बोर्ड reboot हुआ |

Pi 4 के परिणाम सिस्टम के बाकी हिस्से पर खास तौर से निर्भर हैं। बड़े मॉडल परीक्षणों में बोर्ड reset हुआ, जिसमें `qwen3.5:0.8b` का अधूरा run भी शामिल है। यह हमारे 2 GB setup का परिणाम है, यह दावा नहीं कि हर Pi 4 या हर 1B मॉडल reboot करेगा। 4 GB या 8 GB Pi 4 में मेमोरी ज्यादा है, पर CPU परीक्षण किए Pi 5 से धीमा inference देगा। इन Pi 4 मेमोरी-वेरिएंट को सीधे benchmark नहीं किया।

Pi 4 का एक शुरुआती run अंतिम माप से बहुत खराब दिखा: RAM-backed `/tmp` में करीब 625 MB अस्थायी GGUF फाइलें थीं, केवल 500–600 MB खाली बचे और सैकड़ों MB swap में गए। फाइलों को स्थायी storage पर ले जाने के बाद छोटे मॉडल के परिणाम inference memory का बेहतर चित्र दिखाते हैं। 2 GB बोर्ड में *डाउनलोड की जगह* भी benchmark बिगाड़ सकती है।

**सिफारिश:** इस 2 GB बोर्ड के लिए default के रूप में import किया LFM2.5-350M चुनते हैं। यह **516 MB RSS** पर स्थिर रहा, करीब **1 GB RAM उपलब्ध** छोड़ी और Pi 4 reply-rule test में **5/6** पाया। Pi 5 के repeated test में कभी-कभी source name छूटा, इसलिए जिन ऐप में attribution जरूरी है वे इसे जांचें। Latency और memory headroom सबसे अहम हों तो LFM2.5-230M चुनें: यह तेज और हल्का था, लेकिन एक medical-context उत्तर में “nausea or vomiting” को “nausea/ventilator use” बना दिया। यह content error इसे स्वास्थ्य या सुरक्षा जवाबों के लिए कमजोर default बनाती है, भले repeated mechanical compliance score अधिक हो। [Ollama registry](https://ollama.com/library/qwen2.5/tags) से मॉडल चाहिए तो `qwen2.5:0.5b` चुनें, लेकिन इसकी कमजोर instruction compliance ध्यान में रखें। `granite4:350m` स्थिर रहा पर धीमा और ज्यादा memory वाला था; MiniCPM5-1B तभी ठीक है जब client reasoning बंद करे। इस विशेष 2 GB setup पर हमारे runs में reboot हुए, इसलिए Gemma 3 1B और Qwen3.5 0.8B से बचें।

## Raspberry Pi 5: ज्यादा विकल्प, गति का समझौता

8 GB Pi 5 ने speed-and-memory benchmark के **सभी 25 मॉडल** संभाले। छोटे-जवाब वाले काम में जिनकी सिफारिश नहीं करते वे भी तालिका में हैं। † import किए GGUF को दिखाता है। “Think off” speed run की setting बताता है; अलग compliance परीक्षण में जरूरी नहीं वही setting रही हो।

| मॉडल | फाइल GB | आउटपुट tok/s | जवाब s | अधिकतम RSS MB | छोटे जवाब का आकलन |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | सबसे कम latency; repeated compliance 78% |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | न लें: 1-bit weights और single-pass compliance 3/6 |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | तेज, पर 18 में 5 बार स्रोत citation छूटा |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | आसान registry विकल्प; repeated compliance 61% |
| `qwen3:0.6b`, think off | 0.52 | 23.0 | 4.3 | 1,069 | शर्तों पर: 4/6; reasoning setting मायने रखती है |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | प्रयोगात्मक 1-bit मॉडल; एकल 6/6 पुष्टि नहीं हुई |
| `minicpm5-1b` †, think off | 0.69 | 18.4 | 5.1 | 869 | शर्तों पर: default reasoning में खाली जवाब |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | फिट होता है, पर छोटे LFM2.5 से बड़ा और धीमा |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | हमारे काम के लिए सर्वश्रेष्ठ; repeated compliance 89% |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | registry विकल्प; compliance 5/6 |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | registry मॉडल में सर्वश्रेष्ठ repeated compliance: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6; Gemma 3 1B ने नियम बेहतर माने |
| `qwen3.5:0.8b`, think off | 1.04 | 8.8 | 12.2 | 1,592 | default reasoning में 0/6; reasoning control न हो तो बचें |
| `spark-x2.5-1.7b` †, think off | 1.11 | 9.7 | 9.4 | 1,542 | default reasoning में 0/6; reasoning control न हो तो बचें |
| `qwen3:1.7b`, think off | 1.36 | 8.1 | 12.4 | 1,867 | शर्तों पर; छोटे विकल्पों से ज्यादा memory और delay |
| `minicpm5-2b` †, think off | 1.56 | 7.7 | 10.9 | 1,787 | शर्तों पर; एकल test में 5/6, अतिरिक्त bullets |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | आजमाने योग्य 3B विकल्प; single-pass 5/6 |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | interactive काम के लिए न लें: धीमा decode |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | दूसरा 3B विकल्प; compliance run रिपोर्ट नहीं |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | फिट होता है, पर छोटे विकल्पों से धीमा |
| `qwen3.5:2b`, think off | 2.74 | 5.0 | 16.1 | 3,627 | ज्यादा memory और delay; compliance run रिपोर्ट नहीं |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | तेज जवाबों के लिए न लें; पहले token में 14.3 s |
| `ling-3.0-tiny` †, think off | 4.82 | 9.9 | 19.4 | 5,071 | बड़ा footprint; single-pass 5/6, grounding failure सहित |
| `lfm2.5:8b`, think off | 5.16 | 8.7 | 54.6 | 5,317 | मुश्किल से फिट; cold-load 34.4 s और लंबे जवाब |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | न लें: दूसरी Pi सेवाओं के साथ swap दबाव |

† आयात किया GGUF। जवाब समय और memory आंकड़े Pi 5 पर पांच-prompt speed run के हैं; compliance आंकड़े अलग छह-prompt tests से हैं। जिस मॉडल का compliance score नहीं, उसने reply rules मानने का प्रमाण नहीं दिया।

छोटे LFM2.5 मॉडल इस छोटे-जवाब काम में सबसे तेज थे। परीक्षण किए Pi 5 पर 1.2B संस्करण व्यावहारिक मध्य विकल्प है। Gemma 3 1B registry-only विकल्प है और बाद के tests में Qwen2.5 1.5B से बेहतर repeated reply-rule compliance दिखाता है। ज्यादा क्षमता मांगने वाले prompt के लिए 3B मॉडल की धीमी output स्वीकार्य हो सकती है, लेकिन timing अकेले बेहतर उत्तर देने वाला मॉडल नहीं बताती।

Cold-load और first-token delay अनुभव बदलते हैं। Pi 5 पर LFM2.5-230M करीब **0.21 seconds** में load हुआ और **0.37 seconds** में दृश्य token दिया। Qwen2.5 1.5B को load में **2.59 seconds** और पहले दृश्य token में **3.66 seconds** लगे; Qwen2.5 3B को **5.60** और **7.97 seconds**। कभी-कभार प्रश्न में generation शुरू होने के बाद की output rate से ये delay ज्यादा महत्वपूर्ण हो सकते हैं। लगातार loaded मॉडल में delay कम मायने रखता है, लेकिन request के बीच भी memory घेरे रहता है।

अन्य मापे candidate दिखाते हैं कि parameter count से अकेले रैंक क्यों नहीं करना चाहिए। Reasoning बंद करके `qwen3:0.6b` Pi 5 पर **1,069 MB RSS** और **23.0 tokens/s** तक पहुंचा; import किया MiniCPM5-1B **869 MB RSS** और **18.4 tokens/s** पर था। `granite4:350m` को **0.71 GB** download चाहिए था और इसकी गति **12.1 tokens/s** थी, नाम 350M होने पर भी। Model packaging और architecture नाम, file size, memory और speed का संबंध बदलते हैं।

यदि client भरोसेमंद तरीके से `think: false` भेज सकता है, तो Qwen3 0.6B और MiniCPM5-1B को LFM2.5 के विकल्प के रूप में जांचना ठीक है। MiniCPM5-2B, Qwen3 1.7B और Spark-X2.5 1.7B भी Pi 5 पर चले, लेकिन मुख्य विकल्पों के मुकाबले speed और memory में साफ लाभ नहीं था। MiniCPM5-1B और Spark-X2.5 के compliance test में default reasoning था; उनके खाली जवाबों को think-off speed run का परिणाम न बताएं। इसके उलट, तेज think-off timing यह साबित नहीं करती कि वह flag हटाने वाला bridge उपयोगी उत्तर पाएगा।

यदि raw speed से अधिक आसान installation चाहिए, तो 8 GB Pi 5 पर Gemma 3 1B और Llama 3.2 1B registry विकल्प हैं। Gemma 3 1B ने repeated replies में **15/18** बार नियम माने। Llama 3.2 1B एक pass में **5/6** थी, इसलिए उसका अनुपालन अनुमान कम पक्का है। Timing run में Qwen2.5 1.5B ने Gemma 3 1B से तेजी से load और जवाब दिया, लेकिन एक compliance pass में **4/6** ही पाए। अपने prompts की जरूरत से चुनें।

कभी-कभी लंबे या कठिन text prompts के लिए quantized Qwen2.5 3B और Llama 3.2 3B हमारे 8 GB Pi 5 में मध्यम memory उपयोग वाले 3B विकल्प हैं। Speed और memory मापे; Qwen2.5 3B एक compliance pass में **5/6** था। Llama 3.2 3B का तुलनीय compliance run रिपोर्ट नहीं हुआ। ज्यादा parameters उन्हें उन कामों पर *जांचने* का कारण हैं जहां छोटे मॉडल कम पड़ते हैं, यह प्रमाण नहीं कि वे बेहतर उत्तर देते हैं। Granite 4 Micro और Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny और Gemma 3n E2B Pi 5 परीक्षण में फिट या load हुए, लेकिन इस छोटे-उत्तर ऐप में latency, memory headroom या विश्वसनीयता कम आकर्षक थी।

दो Bonsai मॉडल extreme quantization की कीमत दिखाते हैं। 1.7B और 4B पैरामीटर नामों के लिए उनके Q1_0 file चौंकाने वाले छोटे थे, फिर भी 1.7B ने reply-rule check में केवल **3/6** पाए। 4B ने एक छह-prompt pass पास किया, लेकिन हर उत्तर में **18.1 seconds** लगे और repeated compliance की पुष्टि नहीं है। खासकर उत्तर-गुणवत्ता महत्वपूर्ण हो तो इन्हें default सिफारिश नहीं, प्रयोग मानें।

LFM2.5-8B के परिणाम का संदर्भ जरूरी है: hybrid architecture प्रति token कम active parameters इस्तेमाल करती है, इसलिए इसकी decode rate मापे गए dense 3B मॉडल से अधिक थी। फिर भी microSD से cold load **34.4 seconds** लगा और **5.3 GB से अधिक resident memory** इस्तेमाल हुई। यह दिखाता है कि क्या फिट हो सकता है, लेकिन अन्य सेवाओं वाले Pi के लिए सुविधाजनक default नहीं। मापा `gemma3n:e2b` भी लगभग 5.3 GB resident memory लेता था और test host की दूसरी सेवाओं के साथ swap करता था।

LFM2.5 8B run ने उत्तर छोटा रखने के बजाय पूरी **140-token सीमा** छू ली। Gemma 3 4B run में पहले token तक **14.3 seconds** और पूरे जवाब तक **30.3 seconds** लगे। दोनों इस Pi 5 में load हो सकते हैं, पर हमारे tests में responsive छोटे assistant जैसे नहीं थे। सही छोटा उत्तर देने वाला बहुत छोटा मॉडल radio या command interface के लिए कागज पर तेज decode वाले बड़े मॉडल से बेहतर हो सकता है।

## मेमोरी, reasoning और मॉडल प्रारूप

हमारे माप से resident inference memory का आरंभिक अनुमान **मॉडल download size × 1.4** है। यह केवल thumb rule है: context length, runtime settings, model architecture और दूसरे process जरूरत बदलते हैं। Generation के समय उपलब्ध memory देखें, छोटे host पर एक ही model load रखें और OS के लिए जगह छोड़ें। 4 GB बोर्ड छोटे या compact मॉडल से शुरू कर सकता है, लेकिन 4 GB के हमारे सुझाव अनुमान हैं, प्रत्यक्ष 4 GB परीक्षण नहीं।

उदाहरण के लिए Pi 5 पर 0.73 GB LFM2.5-1.2B फाइल करीब **967 MB RSS** से मेल खाती थी, जबकि 0.99 GB Qwen2.5 1.5B फाइल **1,361 MB RSS** तक पहुंची। इन मॉडलों के लिए thumb rule ठीक काम करता है, लेकिन यह कठोर सीमा नहीं। यदि Pi पर interface, search index, local library या background service भी है, तो मापे model process से अधिक memory रखें। असली request में swap देखें; केवल load होने वाला लेकिन लगातार swapping model व्यावहारिक रूप से फिट नहीं है।

कुछ मॉडल दृश्य उत्तर से पहले अंदरूनी reasoning block बनाते हैं। परीक्षण में 2 GB Pi 4 पर `qwen3:0.6b` को दृश्य पाठ देने में काफी अधिक समय लगा। MiniCPM5-1B ने default reasoning के साथ पांच में केवल एक उपयोगी उत्तर दिया, reasoning बंद होने पर पांच में पांच। छोटे reply budget के लिए compatible Ollama API request में `think: false` रखें या default में reasoning न करने वाला मॉडल चुनें। यह setting समर्थित मॉडल और client पर लागू है, सार्वभौमिक speed switch नहीं।

यह फर्क इसलिए अहम है कि token cap में reasoning token भी शामिल हो सकते हैं, भले उपयोगकर्ता को उत्तर न दिखे। Pi 4 पर default reasoning वाले `qwen3:0.6b` ने प्रति request औसतन **40.4 seconds** लिए; एक prompt में दृश्य उत्तर खाली था। MiniCPM5-1B ने default setting पर औसतन **33.3 seconds**, reasoning बंद होने पर **12.2 seconds** लिए। Pi 5 के runs में हमारे रिकॉर्ड के अनुसार Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 और Spark-X2.5 के लिए reasoning बंद किया। Client जिस setting का उपयोग करेगा, उसी पर मॉडल तुलना करें।

### देखें कि जवाब उपयोगी है या नहीं

हमारे छोटे mesh-assistant काम में reply contract गति जितना ही जरूरी है: अधिकतम **90 शब्द**, **तीन bullets** तक, plain text, पूरा वाक्य, और दिए गए retrieval context का स्रोत नाम सहित उपयोग। Bridge पाठ को **180-character chunks** में बांटता है। लंबा जवाब अधिक radio airtime लेता है, भले मॉडल उसे तेजी से बनाए।

Benchmark का बाद का संस्करण खाली reply, prompt-विशिष्ट शब्दसीमा, बहुत अधिक bullets, Markdown table या code fence, अधूरा अंत, दिए context के term का अभाव और source name न होना जांचता है। deployed assistant के system prompt के आधार पर score करने पर छोटे मॉडल ने ये नियम अक्सर तोड़े। सबसे गंभीर विफलताएं थीं reasoning से token budget खत्म होने पर **खाली जवाब**, फिर retrieved context को अनदेखा करने या स्रोत छोड़ने वाले उत्तर। शब्द या bullets सीमा पार करने पर पाठ दिखा, लेकिन airtime बर्बाद हुआ। ये mechanical checks हैं, उत्तर पढ़ने का विकल्प नहीं: ये तथ्य की सटीकता या सुरक्षा सलाह की उपयुक्तता साबित नहीं करते।

#### Pi 5 के repeated compliance परिणाम

पहले हमने deployed system prompt और **220-token cap** के साथ हर मॉडल पर छह prompts एक बार चलाए। संभावित अच्छे मॉडल को अलग seed से दो बार और जांचा, यानी **हर मॉडल के 18 replies**। एक परफेक्ट single pass से repeated सफलता निश्चित नहीं हुई। नीचे के repeated परिणाम छोटे mesh replies की मजबूत तुलना देते हैं:

| मॉडल | सभी जांचे नियम मानने वाले जवाब | मुख्य देखी गई विफलताएं |
|---|---:|---|
| आयात किया LFM2.5-1.2B | 16/18 (89%) | दो अधूरे जवाब |
| `gemma3:1b` | 15/18 (83%) | तीन अधूरे जवाब |
| आयात किया LFM2.5-230M | 14/18 (78%) | अधूरे जवाब और source name गायब |
| आयात किया LFM2.5-350M | 13/18 (72%) | source name गायब |
| `qwen2.5:0.5b` | 11/18 (61%) | ज्यादा bullets, अतिरिक्त शब्द, source name गायब |

**2 GB Pi 4** पर अलग छह-prompt compliance pass ने LFM2.5-350M के लिए **5/6**, LFM2.5-230M के लिए **4/6** और Qwen2.5-0.5B के लिए **2/6** पाया। MiniCPM5-1B default reasoning से **1/6** से बढ़कर reasoning बंद करने पर **5/6** हुआ। Pi 4 स्कोर single-pass हैं। इसलिए सामान्य instruction-following पर हम repeated Pi 5 परिणाम को अधिक महत्व देते हैं और Pi 4 run से इस बोर्ड की स्थिरता व गति देखते हैं।

विफलताओं के असर अलग हैं। **खाली** जवाब उपयोगकर्ता को कुछ नहीं देता; दी गई जानकारी की अनदेखी भ्रमित कर सकती है। source name न हो तो पाठक attribution जांच नहीं सकता। अतिरिक्त bullets या शब्द मुख्यतः और 180-character packet लेते हैं। अधूरा वाक्य truncation का संकेत हो सकता है। LFM2.5-230M का medical-term error याद दिलाता है कि mechanical check पास कर उत्तर फिर भी गलत हो सकता है। पांच repeated candidate में किसी ने भी सभी 18 उत्तरों में हर नियम नहीं माना। सख्त length या format वाला ऐप generation के बाद भी उसे लागू करे और high-stakes content अलग जांचे।

हमने retrieved WikiMed context के साथ असली bridge endpoint, Ollama का OpenAI-compatible `/v1/chat/completions`, भी जांचा। Pi 5 पर LFM2.5-1.2B ने दिए छह term उपयोग करते हुए 28-शब्द उत्तर दिया; Qwen2.5-0.5B ने सात term के साथ 38 शब्द दिए। दोनों दो 180-character packet में समाए। Endpoint check पुष्टि करता है कि import किया LFM2.5 bridge request path से काम करता है, लेकिन एक सफल उत्तर reliability की गारंटी नहीं।

Ollama कई ready-to-pull मॉडल देता है, जिनमें [Qwen2.5 के 0.5B, 1.5B और 3B विकल्प](https://ollama.com/library/qwen2.5/tags) शामिल हैं। हमने छोटे LFM2.5 मॉडल [Liquid AI के GGUF releases](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main) से Ollama में import किए। Download से पहले सही tag या GGUF filename जांचें, क्योंकि registry और repository बदलते रहते हैं। GGUF download स्थायी storage में रखें; हमारे परीक्षण में RAM-backed `/tmp` ने Pi 4 की कम memory खर्च की।

### Registry tag और GGUF import

पहले test का छोटा रास्ता Ollama tag है: सही tag pull करके चलाएं। तालिकाओं के छोटे LFM2.5 मॉडल **GGUF imports** थे, Ollama public library के `lfm2.5-230m`, `lfm2.5-350m` या `lfm2.5-1.2b` tags नहीं। GGUF model-file format है; `Q8_0` और `Q4_K_M` जैसे नाम quantization विकल्प बताते हैं। उपयोग किए 230M और 350M LFM2.5 file Q8_0 थे, जबकि 1.2B file Q4_K_M थी। इसलिए दूसरी quantization में वही parameter count समान file size, memory use या quality की गारंटी नहीं देता।

जांचे गए 350M variant को import करने के लिए GGUF स्थायी storage के directory में download करें, file path वाला Modelfile बनाएं और Ollama को अपने model store में copy करने दें:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

Import के समय download की गई फाइल और Ollama में रखी copy, दोनों के लिए अस्थायी जगह चाहिए। लंबे GGUF transfer कभी-कभी टूटने के कारण resumable download उपयोग किया। Import से पहले downloaded GGUF का SHA-256 source द्वारा प्रकाशित hash से मिलाएं; अधूरा transfer model समस्या जैसा लग सकता है। हमारे Pi में `/tmp` RAM-backed था, इसलिए वहां GGUF रखने से inference memory कम हुई।

## उपयोगी शुरुआत

| हार्डवेयर और लक्ष्य | पहले आजमाने वाला मॉडल | कारण |
|---|---|---|
| 2 GB Pi 4, default | आयात किया LFM2.5-350M | 516 MB RSS पर स्थिर और करीब 1 GB उपलब्ध; 230M की medical-term गलती के बाद चुना |
| 2 GB Pi 4, सबसे कम latency | आयात किया LFM2.5-230M | 383 MB RSS और औसत 7.2 s reply; स्वास्थ्य या सुरक्षा प्रश्न में सामग्री ध्यान से जांचें |
| 2 GB Pi 4, registry-only | `qwen2.5:0.5b` | सीधा Ollama pull और Pi 4 के पांच-prompt run में स्थिर; Pi 5 पर repeated compliance 61% |
| 4 GB Pi 4 या Pi 5 | आयात किया LFM2.5-1.2B, फिर स्थानीय जांच | 8 GB Pi 5 पर 967 MB RSS और 89% repeated compliance; 4 GB variant सीधे नहीं मापा |
| 8 GB Pi 5, responsive assistant | आयात किया LFM2.5-1.2B | 15.5 tokens/s, कुल reply 4.7 s और मापा गया सबसे अधिक repeated compliance |
| 8 GB Pi 5, registry-only setup | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS और 83% repeated compliance |
| 8 GB Pi 5, बड़ा text model आजमाएं | quantized Qwen2.5 3B या Llama 3.2 3B | दोनों करीब 5 tokens/s पर चले और 2.4–2.8 GB RSS लिया; Qwen2.5 3B ने एक pass में 5/6 पाए |

ये विकल्प ऐसे Pi पर छोटे उपयोगी जवाब प्राथमिकता देते हैं जो अन्य service भी चला सकता है। ये शुरुआती विकल्प हैं, हर काम के लिए किसी एक को सर्वोत्तम बताने का दावा नहीं। Pi 5 के single-pass compliance check में default reasoning वाले `qwen3.5:0.8b` और Spark-X2.5 ने compliant जवाब नहीं दिए; MiniCPM5-1B ने 1/6 पाया। Client reasoning बंद न कर सके तो छोटे-जवाब के काम में इन्हें न लें। Final model को नियोजित prompt, context length, concurrency और response limit के साथ जांचें।

Registry model के लिए [Linux पर Ollama इंस्टॉल](https://ollama.com/download/linux) करने के बाद चलाएं:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

अपने prompt, चाही गई जवाब लंबाई और दूसरे चलते service के साथ टेस्ट करें। कुल reply time और memory use दोनों दर्ज करें। इससे अकेले parameter count की तुलना में Pi के लिए suitability ज्यादा स्पष्ट होगी।

कम memory वाले node पर testing के समय swap देखें। बड़ा model बोर्ड को धीमा करे तो छोटा मॉडल लें और Ollama service पर उचित memory cap रखें ताकि बड़ा load host की memory खत्म होने से पहले fail हो जाए। Service cap सुरक्षा है, बहुत बड़े model को फिट करने की तरकीब नहीं। हमारे Pi 4 reboot बताते हैं कि tokens per second के साथ responsiveness और memory headroom भी selection criteria हैं।

## Benchmark को deployment निर्णय में बदलें

रोजाना उपयोग से पहले चार सीमाएं तय करें: **अधिकतम reply time, अधिकतम resident memory, response format और failure behavior**। उसी बोर्ड को साझा करने वाली सेवाओं के साथ इन्हें जांचें। अकेले चलने पर पास, पर radio bridge या dashboard के साथ swap कराने वाला मॉडल deployment requirement पूरा नहीं करता।

एक छोटा fallback model इंस्टॉल रखें। मुख्य मॉडल memory limit पार करे, खाली reply दे या response contract तोड़े तो उस पर जाएं। हर तुलना के साथ model tag, quantization, Ollama version, prompt, context length और seed लिखें, ताकि बाद का model update hardware सुधार जैसा न लगे।
