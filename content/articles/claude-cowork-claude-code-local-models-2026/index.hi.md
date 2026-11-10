---
title: "स्थानीय मॉडल के साथ Claude Cowork और Claude Code: 2026 सेटअप गाइड"
date: 2026-09-22
lastmod: 2026-11-09
toc: true
draft: false
description: "Anthropic-संगत API के ज़रिए Claude Desktop और Claude Code के साथ Ollama कॉन्फ़िगर करें। 2026 के मॉडल और क्लाउड-आधारित सुविधाएँ देखें।"
genre: ["स्थानीय AI", "AI प्रोग्रामिंग टूल", "स्व-होस्टेड AI", "डेवलपर टूल", "गोपनीयता", "ओपन-सोर्स मॉडल", "ऑटोमेशन", "AI हार्डवेयर"]
tags: ["claude cowork", "claude code", "claude desktop स्थानीय मॉडल", "ollama claude code", "anthropic base url", "anthropic_auth_token", "claude code स्थानीय मॉडल", "claude ऑफलाइन चलाएँ", "स्थानीय AI कोडिंग एजेंट", "ollama launch claude", "claude desktop ollama", "स्थानीय llm कोडिंग", "निजी AI कोडिंग", "ऑफलाइन AI कोडिंग", "स्थानीय AI एजेंट", "qwen3.8", "glm क्लाउड मॉडल", "टूल कॉलिंग मॉडल", "claude code सेटअप", "मुफ्त claude code", "API key के बिना claude", "स्थानीय मॉडल की context window", "llama.cpp", "ollama cloud", "AI कोडिंग गोपनीयता", "नेटवर्क से अलग AI", "devops AI टूल"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "आधुनिक कार्यस्थल में कंप्यूटर पर कोडिंग इंटरफ़ेस दिखता है। पास में टैबलेट और स्मार्ट स्पीकर हैं, पीछे रंगीन रोशनी के साथ गहरी नीली पृष्ठभूमि है।"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Claude के एजेंट टूल अब आपके अपने हार्डवेयर पर मौजूद मॉडल के साथ चलते हैं। API key, सब्सक्रिप्शन या डिवाइस से बाहर डेटा भेजने की ज़रूरत नहीं है।** Ollama Anthropic-संगत API देता है, और Claude Code व Claude Desktop कुछ कमांड से उससे जुड़ते हैं।

*कई गाइड एक अहम बात छोड़ देते हैं। वे Claude Cowork बताते हैं, फिर ऐसे चरण देते हैं जो कमांड-लाइन टूल को कॉन्फ़िगर करते हैं। ये दो अलग इंटीग्रेशन हैं, और Cowork सिर्फ एक में मिलता है।*

यह गाइड दोनों रास्ते अलग-अलग बताती है, लोकप्रिय ट्यूटोरियल में छूटने वाला environment variable समझाती है, सितंबर 2026 में हर रास्ते के लिए उपयुक्त मॉडल बताती है, और उन सुविधाओं की सीमा बताती है जो किसी भी कॉन्फ़िगरेशन के बावजूद क्लाउड पर निर्भर हैं।

**गाइड के बाद:** आप ज़रूरी इंटीग्रेशन पहचानेंगे, Ollama के दस्तावेज़ वाले तरीके से उसे जोड़ेंगे, और एक tool-calling परीक्षण से endpoint की पुष्टि करेंगे। स्थानीय inference मॉडल अनुरोधों को डिवाइस पर तभी रखता है जब आप स्थानीय मॉडल चुनें और क्लाउड-आधारित सुविधाओं से बचें।

## संक्षिप्त उत्तर

**Claude से जुड़ने के लिए Ollama के दो अलग तरीके हैं। गलत तरीका चुनने से गाइड के बाद टर्मिनल तो काम करता है, पर Cowork नहीं मिलता।**

| इंटीग्रेशन | क्या मिलता है | सेटअप का तरीका | प्लेटफ़ॉर्म |
|---|---|---|---|
| **Claude Desktop** | Cowork, subagents, web search, auto mode | Ollama ऐप, फिर **Apps** और **Connect Claude** | **केवल macOS** |
| **Claude Code** | tool calling और फ़ाइल संपादन वाला CLI कोडिंग एजेंट | `ollama launch claude` या environment variables | macOS, Linux, Windows |

**Cowork चाहिए तो Claude Desktop इंटीग्रेशन इस्तेमाल करें।** यह Ollama ऐप में ग्राफ़िकल प्रक्रिया है और केवल macOS पर उपलब्ध है। Windows समर्थन अभी आने वाला बताया गया है।

**टर्मिनल में एजेंट चाहिए तो Claude Code इस्तेमाल करें।** एक कमांड काफ़ी है।

*दोनों मुफ़्त हैं। खर्च केवल हार्डवेयर और बिजली का है।*

## एक नहीं, दो इंटीग्रेशन

नामों से भ्रम शुरू होता है। **Claude Cowork, Claude Desktop की एक सुविधा है**, अलग ऐप नहीं और Claude Code का दूसरा नाम भी नहीं।

Ollama के दस्तावेज़ दोनों को अलग पेज और अलग शीर्षकों में रखते हैं। Claude Desktop, **Assistants** के अंतर्गत OpenClaw और Hermes के साथ है। Claude Code, **Coding** के अंतर्गत OpenCode, Cline और Codex CLI के साथ है।

यह अंतर मायने रखता है क्योंकि सेटअप पूरी तरह अलग है:

- **Claude Desktop** को Ollama ऐप के इंटरफ़ेस से सेट करें। Shell profile छूने की ज़रूरत नहीं है।
- **Claude Code** को environment variables या एक launch command से सेट करें।

जो गाइड `ANTHROPIC_BASE_URL` export कराकर `claude` चलाती है, वह command-line टूल सेट कर रही है। अगर इन चरणों से Cowork का desktop अनुभव मिलने की उम्मीद थी, **तो सेटअप में कुछ टूटा नहीं है। आपने दूसरा उत्पाद कॉन्फ़िगर किया।**

## Claude Desktop और Cowork सेटअप

यह तरीका टर्मिनल के बजाय Ollama ऐप में पूरा होता है।

### ज़रूरी चीज़ें

- macOS पर **Ollama इंस्टॉल होना चाहिए**। Windows समर्थन आने वाला बताया गया है।
- स्थानीय उपयोग के लिए पहले **एक मॉडल डाउनलोड करें**। क्लाउड मॉडल के लिए Ollama में साइन इन करके cloud models चालू करें। कुछ के लिए सशुल्क प्लान चाहिए।
- **Claude इंस्टॉल होना चाहिए।** अगर यह मौजूद नहीं है, तो सेटअप के समय Ollama इसे डाउनलोड करने की पेशकश करता है।

### चरण

1. Ollama खोलें और **Apps** चुनें।
2. **Connect Claude** चुनें।
3. सेटअप निर्देशों का पालन करें। संकेत मिलने पर Claude इंस्टॉल करें और कहे जाने पर इसे फिर शुरू करें।

बस इतना ही। बाद में मॉडल बदलने के लिए **Ollama Settings** खोलें, **Apps** पर जाएँ, मॉडल चुनें और **Restart Claude** दबाएँ।

### उपलब्ध सुविधाएँ

Ollama के दस्तावेज़ इस इंटीग्रेशन में चार सुविधाएँ समर्थित बताते हैं:

- कठिन काम पूरे करने के लिए **Cowork**
- बड़े काम एजेंटों में बाँटने के लिए **Subagents**
- Ollama की ओर से डिफ़ॉल्ट रूप से उपलब्ध **Web search**
- **Auto mode**, जिसमें एजेंट बदलाव से पहले अनुमति माँगने का समय तय करता है

*Cowork इस सूची में है। यह सुविधा इस इंटीग्रेशन में मिलती है, command-line इंटीग्रेशन में नहीं।*

### डिस्कनेक्ट करना

डिस्कनेक्ट करने पर Claude का पिछला कॉन्फ़िगरेशन वापस आता है। इसलिए बदलाव विनाशकारी नहीं है।

- इंटरफ़ेस में **Apps** खोलें, Claude को डिस्कनेक्ट करें और कहे जाने पर उसे फिर शुरू करें।
- टर्मिनल से `ollama launch claude-desktop --restore` चलाएँ।
- **Claude जुड़ा होने पर Ollama बंद करने से भी Claude का सामान्य कॉन्फ़िगरेशन वापस आ जाता है।** स्थानीय सेटअप बनाए रखने के लिए Ollama चालू रखें।

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Ollama ऐप के Apps पैनल से Claude Desktop का कनेक्शन, Ollama सेटिंग में मॉडल चयन और मूल कॉन्फ़िगरेशन बहाल करने का रास्ता दिखाता आरेख" >}}

## CLI से Claude Code सेटअप

लगभग हर गाइड यही तरीका बताती है, और टर्मिनल के काम के लिए यही सही है।

### एक कमांड का तरीका

```bash
ollama launch claude
```

यह कमांड ज़रूरी environment variables सेट करती है, Claude Code को आपके स्थानीय Ollama instance पर भेजती है और उसे शुरू करती है। सूची से मॉडल चुनकर Enter दबाएँ। पहले से मॉडल बताने के लिए flag जोड़ें:

```bash
ollama launch claude --model qwen3.5
```

*Wrapper आपके लिए environment सेट करता है। अगला भाग भी पढ़ें, क्योंकि सेट की गई चीज़ें जानने से बाद में समस्या हल करने में मदद मिलेगी।*

### Environment variables हाथ से सेट करना

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**दूसरी पंक्ति लोकप्रिय गाइड में छूट जाती है।** `ANTHROPIC_API_KEY` को खाली string रखने से environment में पहले से मौजूद असली key स्थानीय कनेक्शन में दखल नहीं देती। प्रकाशित गाइड यह पंक्ति छोड़ दे तो पहले से key export करने वाले पाठकों को भ्रमित करने वाली त्रुटि मिलती है।

Shell profile में बदलाव से बचने के लिए सब कुछ उसी कमांड में दें:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

आधिकारिक दस्तावेज़ की दो बातें:

- **`ANTHROPIC_AUTH_TOKEN` bearer authentication रखता है**, इसलिए स्थानीय मोड में इसका शाब्दिक मान `ollama` होता है।
- **Claude की अपनी settings फ़ाइलें shell variables पर प्राथमिकता रखती हैं।** नए मान export करने के बाद कनेक्शन अजीब लगे तो उन settings को देखें और इस्तेमाल हो रहा endpoint जानने के लिए Claude Code में `/status` चलाएँ।

### सीधे Ollama Cloud से जुड़ना

इस तरीके के लिए Ollama इंस्टॉल करना ज़रूरी नहीं है। API key सेट करें और Claude Code को Ollama के hosted endpoint पर भेजें:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**इस रास्ते की एक सीमा है।** Ollama दस्तावेज़ के अनुसार hosted web search और उन्नत tool controls पूरी तरह समर्थित नहीं हैं। संगत मॉडल के साथ सामान्य chat, फ़ाइल संपादन और tool calling चलते हैं।

## सितंबर 2026 के मॉडल विकल्प

2026 में मॉडल सूची में बड़े बदलाव हुए हैं, इसलिए वसंत में लिखी सलाह फिर जाँचें।

| मॉडल | प्रकार | Context | क्यों चुनें |
|---|---|---|---|
| **Qwen3.8 27B** | स्थानीय, 18 GB | 256K | vision, tool calling और thinking control वाला मौजूदा बेहतर स्थानीय all-rounder |
| **Qwen3 Coder Next** | स्थानीय, कुल MoE 80B / सक्रिय 3B | 256K | हमेशा चालू coding agents के लिए बनाया गया, तेज़ी के लिए non-thinking mode |
| **Qwen3.6 35B A3B** | स्थानीय, MoE 35B / सक्रिय 3B | 262K | Apache 2.0 और कम मेमरी में कुशल |
| **kimi-k2.7-code:cloud** | क्लाउड | बड़ा | स्थानीय हार्डवेयर की ज़रूरत के बिना coding-केंद्रित क्लाउड मॉडल |
| **glm-5.3-flash** | क्लाउड | बड़ा | Ollama के अपने दस्तावेज़ में सबसे पहले सुझाया गया मॉडल |

**मेमरी पर्याप्त हो तो Qwen3.8 27B से शुरू करें।** यह 256K context window, native vision, tool calling और हर request पर चालू-बंद होने वाली thinking के साथ स्थानीय रूप से चलता है। कम-से-कम 24 GB वाली कार्ड पर यह रोज़ के उपयोग के लिए सुविधाजनक है।

**इतनी मेमरी न हो तो क्लाउड मॉडल से शुरू करें।** Claude Code को hosted मॉडल से जोड़कर मुफ़्त में आज़मा सकते हैं और हार्डवेयर का प्रश्न हट जाता है, लेकिन कोड डिवाइस से बाहर जाता है।

### Ternary मॉडल के बारे में चेतावनी

हमारे **[स्थानीय AI गाइड](/articles/local-ai-2026-build-your-rig-now/)** में बताया गया है कि ternary Bonsai 2 27B **5.53 GiB** में पूरा 27B मॉडल चलाता है। इसे यहाँ इस्तेमाल करना आकर्षक लग सकता है।

**यह इस workflow में नहीं चलेगा।** Ternary kernels, Prism ML के llama.cpp fork में हैं, और stock Ollama ये फ़ाइलें लोड नहीं कर सकता। `ollama launch claude --model Ternary-Bonsai-2-27B` जैसा कमांड inference शुरू होने से पहले विफल होगा। Claude Code के लिए standard Qwen3.8 27B पैकेज लें और ternary पैकेज ऐसे runtime के लिए रखें जो उन्हें संभालता हो।

*सुविधा और अधिकतम दक्षता के लिए यहाँ अलग विकल्प हैं। एकीकृत टूल standard GGUF चाहते हैं।*

## मॉडल को दोष देने से पहले context 64K पर सेट करें

Repository के काम के लिए Ollama दस्तावेज़ एक सीधा निर्देश देता है: मॉडल चुनें और **context window को 64K या उससे अधिक रखें**। बड़ी repository के लिए इसे और बढ़ाएँ।

Claude Code फ़ाइलों का पाठ, diff और command output context window में डालता है। छोटा default हो तो काम के बीच जगह खत्म हो जाती है। यह reasoning की समस्या लगती है, पर कारण setting होती है।

| Context | क्या संभालता है |
|---|---|
| 32K से कम | एक फ़ाइल में बदलाव और छोटे सवाल |
| **64K** | छोटी repository में कई फ़ाइलों का काम |
| 128K | बड़ी repository और लंबा command output |
| 256K | Qwen3.8 27B की पूरी window |

*अगर Claude Code काम के बीच धागा खो दे, तो मॉडल बदलने से पहले context setting देखें।*

## एक कमांड में tool calling की जाँच करें

Tool calling, agent और text generator के बीच का अंतर है। इसे मान लेने के बजाय जाँचें।

Claude Code शुरू होने पर उससे कहें:

```text
Read the current directory and list all files
```

**अगर वह असली फ़ाइलों की सूची दे, तो tool calling काम कर रही है।** अगर वह कहता है कि वह directory पढ़ेगा और बताता है कि वहाँ क्या होने की उम्मीद है, तो सुविधा जुड़ी नहीं है। आप coding prompt लगे chat model से बात कर रहे हैं, agent से नहीं। और prompt देना इसे ठीक नहीं करेगा।

समस्याएँ इस क्रम में जाँचें:

1. **Tool support की पुष्टि वाले मॉडल पर जाएँ।** हर मॉडल इसे लागू नहीं करता, और parameter count से यह अंतर नहीं दिखता।
2. **देखें कि environment Ollama की ओर निर्देशित है।** `ollama --version` चलाएँ और पुष्टि करें कि `ANTHROPIC_BASE_URL` स्थानीय endpoint पर है।
3. **Claude Code में `/status` चलाएँ।** Claude की settings फ़ाइल में base URL या credential, अभी export किए shell variables पर प्राथमिकता रखता है।

## कौन-सी सुविधाएँ केवल क्लाउड में रहती हैं

स्थानीय inference पर workflow दोबारा बनाने से पहले यह सीमा जानें।

| सुविधा | स्थानीय मॉडल के साथ | क्लाउड |
|---|---|---|
| Chat और फ़ाइल संपादन | हाँ | हाँ |
| Tool calling | मॉडल पर निर्भर | हाँ |
| Subagents | हाँ | हाँ |
| Web search | Ollama के ज़रिए | हाँ |
| **Cowork** | Claude Desktop इंटीग्रेशन के ज़रिए | हाँ |
| Auto mode | Claude Desktop इंटीग्रेशन के ज़रिए | हाँ |
| Scheduled prompts | Claude Code में `/loop` के ज़रिए | हाँ |

स्थानीय उपयोग की तीन सीमाएँ हैं:

- **गति से पहले multi-file reasoning बिगड़ती है।** स्थानीय मॉडल एक फ़ाइल को अच्छी तरह, तीन को ठीक-ठाक और पूरी repository को खराब संभालता है। काम का आकार उसी हिसाब से रखें।
- **कुछ क्लाउड मॉडल के लिए Ollama का सशुल्क प्लान चाहिए।** साइन इन करके उन्हें चालू भी करना होगा।
- **सीधे क्लाउड जाने पर कुछ सुविधाएँ सीमित रहती हैं।** स्थानीय इंस्टॉल छोड़ने पर hosted web search और उन्नत tool controls पूरी तरह समर्थित नहीं हैं।

*स्थानीय inference सीमित और जाँचे जा सकने वाले काम में अच्छा है, विस्तृत और अस्पष्ट काम में कमजोर। इसी सीमा के अनुसार योजना बनाएँ।*

## ऑटोमेशन

दो सुविधाएँ इसे केवल interactive इस्तेमाल से आगे ले जाती हैं।

### Scripts और CI के लिए headless runs

`--yes` flag interactive selectors छोड़ देता है और ज़रूरत पड़ने पर मॉडल डाउनलोड करता है। इसे `--model` चाहिए, और `--` के बाद का सब कुछ सीधे Claude Code को जाता है:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Permission model पर ध्यान दें।** Claude Code ज़्यादातर काम से पहले अनुमति माँगता है, इसलिए headless run के लिए configured permission rules या isolated environment चाहिए। किसी महत्वपूर्ण repository पर बिना निगरानी वाला agent न चलाएँ।

### `/loop` के साथ scheduled prompts

Claude Code session में `/loop` तय अंतराल पर prompt या slash command चलाता है:

```text
/loop 30m Check my open PRs and summarize their status
/loop 1h Research the latest AI news and summarize key developments
/loop 15m Check for new GitHub issues and triage by priority
```

*यह session खुला रहने तक चलता है। यह background daemon नहीं है, इसलिए session बंद होने पर रुक जाता है।*

## समस्या निवारण

| लक्षण | संभावित कारण | समाधान |
|---|---|---|
| **कनेक्शन अस्वीकार** | Ollama नहीं चल रहा | `ollama serve` चलाएँ और `curl http://localhost:11434/api/tags` से पुष्टि करें |
| **काम करने के बजाय उसका वर्णन करता है** | चुना गया मॉडल tool calling नहीं करता | Tool support की पुष्टि वाले मॉडल पर जाएँ |
| **स्थानीय endpoint की जगह असली API key उपयोग होती है** | `ANTHROPIC_API_KEY` अब भी export है | ऊपर की तरह इसे खाली string करें |
| **सेटअप के बाद Cowork नहीं मिलता** | Claude Desktop के बजाय Claude Code CLI सेट हुआ | Cowork के लिए Ollama का **Apps** तरीका अपनाएँ |
| **Generation धीमी है** | Context बहुत बड़ा है या sparse मॉडल के बजाय dense मॉडल चुना | Context कम करें और फिर mixture-of-experts मॉडल आज़माएँ |
| **Export किए variables का असर नहीं** | Claude settings फ़ाइलें shell variables पर प्राथमिकता रखती हैं | Settings फ़ाइलें देखें और `/status` चलाएँ |
| **Background request विफल होती है** | Claude Code आंतरिक काम में छोटा मॉडल चुनता है | छोटे मॉडल का override उसी स्थानीय मॉडल पर रखें |

*इन सात में से दो समस्याएँ एक ही कारण से होती हैं। अधिकांश सेटअप समस्याएँ गलत endpoint या tool calling न करने वाले मॉडल से आती हैं।*

## मुख्य बातें

- **Claude Desktop और Claude Code अलग इंटीग्रेशन हैं।** Cowork Claude Desktop में है और macOS पर Ollama के **Apps** पैनल से सेट होता है। CLI वाला रास्ता Cowork नहीं देता।
- **एक कमांड CLI रास्ता शुरू करती है:** `ollama launch claude`। हाथ से सेट करने के लिए तीन variables चाहिए और **कई गाइड `ANTHROPIC_API_KEY=""` छोड़ देती हैं**।
- **स्थानीय इंस्टॉल ज़रूरी नहीं है।** API key के साथ Claude Code को `https://ollama.com` पर भेजें।
- **मॉडल का मूल्यांकन करने से पहले कम-से-कम 64K context रखें।** छोटी window reasoning failure जैसी लग सकती है।
- **एक request से tool calling जाँचें।** मॉडल जो करता, उसका वर्णन करे तो आपके पास agent नहीं, text generator है।
- **Ternary Bonsai पैकेज यहाँ नहीं चलते।** उन्हें Prism ML का llama.cpp fork चाहिए, stock Ollama उन्हें लोड नहीं कर सकता।
- **डिस्कनेक्ट करना सुरक्षित है।** Ollama बंद करने से Claude की पुरानी configuration वापस आती है, और टर्मिनल से `ollama launch claude-desktop --restore` चला सकते हैं।

## अगले कदम

1. Claude छूने से पहले **Ollama इंस्टॉल करें और tool support वाला मॉडल डाउनलोड करें**: **[Ollama मॉडल लाइब्रेरी](https://ollama.com/library)**
2. वर्तमान flags और मॉडलों के लिए **Ollama का Claude Code पेज पढ़ें**: **[Claude Code इंटीग्रेशन](https://docs.ollama.com/integrations/claude-code)**
3. Cowork चाहिए तो **Claude Desktop पेज देखें**: **[Claude Desktop इंटीग्रेशन](https://docs.ollama.com/integrations/claude-desktop)**
4. खरीदने से पहले **स्थानीय inference गाइड की memory tiers से हार्डवेयर तय करें**: **[2026 में स्थानीय AI: 27B मॉडल Sonnet 4.6 से बेहतर](/articles/local-ai-2026-build-your-rig-now/)**
5. कम बिजली वाले बॉक्स पर हमेशा चालू agent चाहिए तो **छोटे हार्डवेयर की क्षमता देखें**: **[Raspberry Pi 4 या 5 पर कौन-से AI मॉडल चलते हैं?](/articles/ai-models-raspberry-pi-4-5/)**

## संबंधित लेख

| लेख | इसमें क्या है |
|---|---|
| **[2026 में स्थानीय AI: 27B मॉडल Sonnet 4.6 से बेहतर](/articles/local-ai-2026-build-your-rig-now/)** | स्थानीय inference का benchmark, ternary quantization और हार्डवेयर चयन |
| **[Raspberry Pi 4 या 5 पर कौन-से AI मॉडल चलते हैं?](/articles/ai-models-raspberry-pi-4-5/)** | छोटे हमेशा चालू assistant के लिए स्थानीय inference |
| **[Meshtastic के लिए गोपनीयता-सुरक्षित AI assistant बनाएँ](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | ऑफ-ग्रिड radio चलाने वाला स्थानीय मॉडल, जिसमें गोपनीयता मुख्य उद्देश्य है |
| **[AI विकास के लिए सर्वश्रेष्ठ VS Code extensions](/articles/best-visual-studio-code-extensions-for-ai/)** | स्थानीय coding agent के साथ उपयोग करने वाले editor टूल |

## संदर्भ

1. [Claude Code इंटीग्रेशन - Ollama दस्तावेज़](https://docs.ollama.com/integrations/claude-code)
2. [Claude Desktop इंटीग्रेशन - Ollama दस्तावेज़](https://docs.ollama.com/integrations/claude-desktop)
3. [Ollama मॉडल लाइब्रेरी](https://ollama.com/library)
4. [Qwen3.8 - Ollama मॉडल लाइब्रेरी](https://ollama.com/library/qwen3.8)
5. [स्थानीय मॉडलों के साथ Claude Cowork - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Prism ML llama.cpp fork - ternary kernels](https://github.com/PrismML-Eng/llama.cpp)
