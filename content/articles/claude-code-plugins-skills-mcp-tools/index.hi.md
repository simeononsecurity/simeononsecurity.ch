---
title: "Claude Code के 10 प्लगइन, स्किल और MCP टूल: व्यावहारिक गाइड"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "प्लानिंग, कोड समीक्षा, ज्ञान प्रबंधन, डिजाइन और ऑटोमेशन के लिए Claude Code एक्सटेंशन चुनें। दस टूल, निर्भरताओं और व्यावहारिक जांचों की तुलना करें।"
genre: ["कृत्रिम बुद्धिमत्ता", "डेवलपर टूल", "सॉफ्टवेयर विकास"]
tags: ["Claude Code प्लगइन", "Claude Code स्किल", "MCP टूल", "Graphify", "grill-me", "grill-with-docs", "grill-me-codex", "Claudex Loop", "Codex प्लगइन", "कोड समीक्षा", "claude-obsidian", "Obsidian", "CLAUDE.md", "Karpathy दिशानिर्देश", "Impeccable", "Higgsfield", "NotebookLM", "notebooklm-py", "n8n MCP", "AI विकास वर्कफ़्लो", "एजेंट निर्देश", "ज्ञान ग्राफ"]
cover: "/img/cover/claude-code-plugins-workflow-management-tools.webp"
coverAlt: "गहरे बैकग्राउंड पर नीले और बैंगनी टूल आइकन, फ़ोल्डर और अमूर्त चार्ट पैनल एक केंद्रीय ज्यामितीय केंद्र से जुड़े हुए"
coverCaption: "वर्कफ़्लो का वैचारिक चित्र। चार्ट आकार किसी मापे गए परिणाम को नहीं दिखाते।"
---

**अपने वर्कफ़्लो की एक खास समस्या के आधार पर Claude Code एक्सटेंशन चुनें।** अस्पष्ट आवश्यकताओं के लिए प्लानिंग बातचीत चाहिए। छूटे हुए दोषों के लिए समीक्षा और टेस्ट चाहिए। बार-बार होने वाले शोध के लिए ट्रेस करने योग्य स्रोत चाहिए। अधिक टूल इंस्टॉल करना तभी उपयोगी है जब उनकी जिम्मेदारियां स्पष्ट हों।

यह गाइड इन कामों के लिए **दस प्रोजेक्ट** की तुलना करती है। इसमें सेटअप उदाहरण और मूल्यांकन अभ्यास भी है। विश्लेषण वर्तमान प्रोजेक्ट दस्तावेज़ और दी गई Chase AI वीडियो पर आधारित है। सुझाव संपादकीय निर्णय हैं। वे व्यावहारिक प्रदर्शन माप या उत्पादकता दस गुना बढ़ने का प्रमाण नहीं हैं।

<!--more-->

## मुख्य बातें

- **आउटपुट के आधार पर चुनें:** समीक्षा किया हुआ प्लान, कोड मैप और बनाई गई इमेज के लिए अलग टूल चाहिए।
- **इंस्टॉलेशन लेयर अलग रखें:** निर्देश, एक्जीक्यूटेबल प्रोग्राम, प्लगइन और सर्विस कनेक्शन की निर्भरताएं अलग होती हैं।
- **वर्तमान नाम जांचें:** Graphify और grill-me-codex के कैनोनिकल रिपॉजिटरी स्थान अब अलग हैं।
- **सहमति से आगे जांचें:** दो मॉडल किसी प्लान को स्वीकार करें, फिर भी इम्प्लीमेंटेशन सही सिद्ध नहीं होता।
- **स्वीकृत काम मापें:** सेटअप, सर्विस उपयोग, असफल प्रयास और मानव सुधार शामिल करें।

## शुरू करने से पहले

**आवश्यकताएं:** काम करता हुआ Claude Code इंस्टॉलेशन, डिस्पोजेबल प्रोजेक्ट या ब्रांच, और चुनी हुई बाहरी सेवाओं के उपयोग की अनुमति। CLI उदाहरण टर्मिनल और नामित पैकेज मैनेजर मानते हैं। क्लाउड इंटीग्रेशन के लिए अपने अकाउंट और प्रमाणीकरण चाहिए।

**अनुमानित समय:** पढ़ने में 15 मिनट, फिर एक सीमित ट्रायल के लिए 30 से 60 मिनट। **कठिनाई:** CLI सेटअप और सर्विस इंटीग्रेशन के लिए मध्यम। निर्देश स्किल पढ़ने में कम सेटअप चाहिए।

**दस्तावेज़ 10 अक्टूबर 2026 को जांचे गए।** कमांड और एक्सेस नियम लिंक किए गए स्रोतों पर आधारित हैं। पुराने ट्यूटोरियल से पहले अपने इंस्टॉल किए गए संस्करण को फिर जांचें। यह लेख Claude Code से इस्तेमाल होने वाले एक्सटेंशन पर केंद्रित है और जरूरी जगह पर होस्ट के अंतर बताता है।

**इंस्टॉलेशन के बाद लेयर के अनुसार जांचें।** फाइल, होस्ट डिस्कवरी, एक्जीक्यूटेबल निर्भरता, क्रेडेंशियल और एक प्रतिनिधि कार्य अलग-अलग जांचें। सफल इंस्टॉलर यह सिद्ध नहीं करता कि ब्राउज़र, MCP सर्वर, मीडिया टूल या बाहरी अकाउंट काम करता है। पहला टेस्ट सिंथेटिक डेटा पर करें और upstream revision लिखें।

## एक्सटेंशन का प्रकार समझें

| प्रकार | भूमिका | उदाहरण |
|---|---|---|
| **निर्देश फाइल** | प्रोजेक्ट की स्थायी अपेक्षाएं तय करती है | CLAUDE.md |
| **स्किल** | चुने हुए काम के लिए प्रक्रिया देती है | grill-me |
| **प्लगइन** | रजिस्टर्ड कमांड और इंटीग्रेशन पैक करता है | Codex plugin |
| **CLI** | टर्मिनल से कमांड चलाता है | Graphify |
| **MCP सर्वर** | एजेंट क्लाइंट के लिए कॉल किए जा सकने वाले टूल देता है | n8n instance integration |

**Model Context Protocol (MCP)** एजेंट एप्लिकेशन को सर्वर द्वारा दिए गए टूल और डेटा से जोड़ता है। कमांड-लाइन इंटरफेस, या **CLI**, एक्जीक्यूटेबल कमांड चलाता है। स्किल एजेंट को इनमें से किसी इंटरफेस का उपयोग सिखा सकती है, लेकिन इसकी मौजूदगी काम करता हुआ कनेक्शन सिद्ध नहीं करती।

**लापता क्षमता से शुरू करें।** यदि एजेंट के पास रिपॉजिटरी सर्च पहले से है, तो नई सर्च प्रक्रिया का दिखाई देने वाला लाभ होना चाहिए। यदि एजेंट के पास ऑटोमेशन प्लेटफॉर्म की पहुंच नहीं है, तो केवल निर्देश फाइल प्रमाणित पहुंच नहीं देगी। [एजेंट रनटाइम गाइड](/articles/best-ai-agent-harnesses/) मॉडल कॉल और टूल निष्पादन के आसपास के सॉफ्टवेयर को समझाती है।

## पहला टूल चुनें

| समस्या | टूल | पहली स्वीकृति जांच |
|---|---|---|
| **अस्पष्ट आवश्यकताएं** | grill-me / grill-with-docs | स्पष्ट निर्णय और स्वीकृति मानदंड |
| **बार-बार स्कोप बदलना** | Karpathy-प्रेरित CLAUDE.md | हर बदलाव मांगे गए परिवर्तन की सेवा करे |
| **जोखिम वाला इम्प्लीमेंटेशन प्लान** | Claudex Loop | समीक्षा निष्कर्ष प्रमाण के साथ हल हों |
| **बिना समीक्षा के कोड बदलाव** | OpenAI Codex plugin | निष्कर्ष कोड और विफलता मामलों से जुड़े हों |
| **अनजान रिपॉजिटरी** | Graphify | संबंध स्रोत फाइलों से मेल खाएं |
| **बिखरा हुआ प्रोजेक्ट ज्ञान** | claude-obsidian | दावों में मूल प्रमाण के लिंक रहें |
| **बार-बार स्रोत संश्लेषण** | notebooklm-py | उत्तर इच्छित स्रोतों को उद्धृत करें |
| **भ्रमित इंटरफेस** | Impeccable | उपयोगकर्ता इच्छित इंटरैक्शन पूरा करे |
| **लापता दृश्य सामग्री** | Higgsfield | आउटपुट स्वीकृत ब्रीफ के अनुसार हो |
| **दोहराने योग्य सर्विस वर्कफ़्लो** | n8n MCP | टेस्ट निष्पादन अपेक्षित परिणाम दे |

**सुझाया गया आरंभ:** एक पंक्ति चुनें और इंस्टॉलेशन से पहले बेसलाइन कार्य बचाएं। दूसरा टूल तभी जोड़ें जब वह अलग और मापने योग्य योगदान दे।

## काम स्पष्ट करें

### grill-me और grill-with-docs

**Matt Pocock की स्किल** अधूरे विचार को निर्णयों में बदलती हैं। [grill-me प्रवेश बिंदु](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) साझा grilling skill चलाता है। [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) grilling और domain modeling चलाता है। [कलेक्शन दस्तावेज़](https://github.com/mattpocock/skills) साझा शब्दावली और आर्किटेक्चर निर्णय रिकॉर्ड समझाता है।

**जब व्यावसायिक शब्द इम्प्लीमेंटेशन को प्रभावित करें तब documentation variant लें।** एक उदाहरण CSV importer में तय करें कि existing customer का अर्थ वही ईमेल, वही external identifier, या दोनों है। डुप्लिकेट पहचान लिखने से पहले यह परिभाषा दर्ज करें।

**इंटरव्यू को अनुपात में रखें।** उपयोगी session महत्वपूर्ण अनिश्चितता हल करता है। रिपॉजिटरी में उपलब्ध उत्तर दोहराने की जरूरत नहीं। अंत में plan, अनसुलझे प्रश्न और दिखाई देने वाली completion checks रखें।

### Karpathy-प्रेरित CLAUDE.md

**Multica द्वारा रखे गए दिशानिर्देश** Karpathy के अवलोकनों को चार विषयों में बदलते हैं: स्पष्ट assumptions, सरल समाधान, केंद्रित बदलाव और सत्यापित लक्ष्य। [रिपॉजिटरी](https://github.com/multica-ai/andrej-karpathy-skills) उनके अवलोकनों से प्रेरित community implementation है। इसे Karpathy का व्यक्तिगत रूप से maintained plugin कहना गलत होगा।

**उपयोगी मार्गदर्शन को मौजूदा project policy में मिलाएं।** build commands, content conventions और deployment restrictions बचाएं। ऐसा replacement instruction file जो इन्हें हटाए, नई गलतियां पैदा करता है।

**प्रोजेक्ट नियम का उदाहरण:** importer बदलाव से मौजूदा duplicate handling बचाने और हर जानबूझकर किए बदलाव को fixture से समझाने को कहें। Instructions expectations बताती हैं। Tests और runtime controls अलग प्रमाण देते हैं।

| प्लानिंग आर्टिफैक्ट | उद्देश्य |
|---|---|
| **Requirement** | उपयोगकर्ता को दिखने वाला परिणाम बताता है |
| **Glossary entry** | अस्पष्ट शब्द को एक अर्थ देता है |
| **Decision record** | महत्वपूर्ण चयन का कारण बचाता है |
| **Acceptance check** | completion आकलन करने का तरीका तय करता है |

## प्लान और कोड की समीक्षा करें

### grill-me-codex, अब Claudex Loop

**Claudex Loop** मूल grill-me-codex रिपॉजिटरी का वर्तमान गंतव्य है। इसकी [documentation](https://github.com/chaseai-yt/claudex-loop) repository reconnaissance, requirements, दूसरे provider की review, implementation और independent inspection समझाती है। पूरा loop दोनों CLI और Python 3.10 या बाद का संस्करण मांगता है।

**महत्वपूर्ण योजनाओं के लिए Claudex Loop लें** जिनकी assumptions को इम्प्लीमेंटेशन से पहले चुनौती चाहिए। वर्तमान workflow Claude Code या Codex से शुरू हो सकता है। यह findings और dispositions रिकॉर्ड करता है और review की अनुमति को build की अनुमति से अलग रखता है। वीडियो का पुराना five-round विवरण installed workflow के वर्तमान round budget की जगह नहीं लेता।

**हर objection के साथ evidence मांगें।** CSV importer review को concrete duplicate या retry case और expected behavior बताना चाहिए। Model agreement review outcome है, proof नहीं। Review budget खत्म होने पर unresolved findings रखें।

### OpenAI Codex Plugin

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**Claude Code के लिए OpenAI का Codex plugin** Claude Code के भीतर code review और task delegation जोड़ता है। ये Claude Code commands हैं, shell commands नहीं। [Official repository](https://github.com/openai/codex-plugin-cc) Node.js 18.18 या बाद और ChatGPT अथवा OpenAI API key से authenticated Codex access बताती है।

```text
/codex:review --background
/codex:status
/codex:result
```

**Current changes या branch comparison के लिए ordinary review लें।** Focused challenge के लिए **`/codex:adversarial-review`** लें। **`/codex:rescue`** जैसे delegation commands read-only review से अलग काम करते हैं। Intended authority स्पष्ट करें।

**Codex usage का budget अलग रखें।** Project supported accounts में ChatGPT Free बताता है, लेकिन usage limits लागू रहती हैं। Plugin इंस्टॉल करने से unlimited access नहीं मिलता।

**चयन नियम:** existing patch के लिए bounded plugin review लें। Requirements और plan revision के लिए अपना recorded process चाहिए तो बड़ा loop चुनें।

## उपयोगी संदर्भ बचाएं

### Graphify

```bash
uv tool install graphifyy
graphify install --project
graphify extract . --code-only
graphify query "show the authentication flow"
```

**Graphify** repository संबंधों को queryable knowledge graph में मैप करता है। इसका [canonical repository](https://github.com/Graphify-Labs/graphify) अब Graphify-Labs के अंतर्गत है। Package name **`graphifyy`** है, अंत में दो y हैं। Executable **`graphify`** ही है।

**Code-only extraction** स्थानीय abstract syntax tree parsing इस्तेमाल करता है। Document और media interpretation अलग model-backed path इस्तेमाल करते हैं। Local privacy या cost का दावा हर mode पर लागू न करें।

**Optional hooks** commit और branch switch के बाद code graph बनाते हैं। Pull या merge के बाद documented workflow **`graphify update .`** चलाता है। Documentation changes को अलग refresh चाहिए। Obsidian export graph का दूसरा view देता है।

**Relationship questions के लिए Graphify लें**, फिर संबंधित source देखें। Graph file selection में मदद करता है। Graph structure runtime behavior सिद्ध नहीं करती और tests की जगह नहीं लेती। Graph construction और maintenance समेत अपने प्रश्नों पर token savings मापें।

### claude-obsidian

**claude-obsidian** source material को linked और cited Obsidian pages में व्यवस्थित करता है। इसका [repository](https://github.com/AgriciDaniel/claude-obsidian) ingestion, retrieval, knowledge maintenance, source retention और support या contradiction records बताता है। Vault सामान्य local files रहती है।

**स्थायी project knowledge के लिए claude-obsidian लें:** design decisions, source documents और research notes जो अलग-अलग conversations से आगे रहें। उपयोगी output provenance वाला maintainable record है, यानी हर महत्वपूर्ण claim का traceable origin।

**Ingestion के बाद vault review करें।** कुछ claims चुनकर citations को original material तक follow करें। Conflicting evidence बचाएं। Local storage local inference सिद्ध नहीं करती। Sensitive documents देने से पहले host और model configuration जांचें।

| Context system | पहला उपयोगी प्रश्न |
|---|---|
| **Graphify** | कौन से source components जुड़े हैं? |
| **claude-obsidian** | कौन सा retained evidence इस decision को support करता है? |
| **notebooklm-py** | चुने हुए research sources क्या कहते हैं? |

### notebooklm-py

```bash
uv tool install "notebooklm-py[browser]"
notebooklm login
notebooklm auth check --test --json
notebooklm skill install
```

**notebooklm-py** Google की notebook research service के लिए Python library, CLI और agent skill देता है। [Project](https://github.com/teng-lin/notebooklm-py) source imports, grounded questions, generated artifacts और batch downloads बताता है। Browser extra interactive login flow संभालता है।

**यह unofficial integration है।** Library undocumented Google interfaces पर निर्भर है और breakage तथा rate limits के अधीन है। इसे Google-supported public API न बताएं।

**सीमित research corpus के लिए notebooklm-py लें**, जैसे एक dependency की release notes और migration guides। Plan में findings डालने से पहले citations source text से जांचें। Saved authentication state को account access material की तरह सुरक्षित रखें।

**Research offload करने से work location बदलती है।** इससे orchestration tokens, service quotas, review effort या data-handling obligations खत्म नहीं होते। Token savings को मापी जाने वाली चीज समझें, installation की automatic property नहीं।

## Assets डिजाइन और जनरेट करें

### Impeccable

```text
/impeccable critique settings
/impeccable audit settings
/impeccable polish settings
```

**Impeccable** focused interface work के लिए design vocabulary देता है। इसकी [documentation](https://github.com/pbakaus/impeccable) critique, layout, typography, accessibility checks, motion और browser visual iteration बताती है। उदाहरण installed skill और settings surface वाले project मानते हैं।

**Interaction problem से शुरू करें।** Importer में पूछें कि users validation errors क्यों चूकते हैं या duplicate choice को गलत समझते हैं। Visual polish लगाने से पहले proposed changes review करें। अच्छा spacing ambiguous action ठीक नहीं करता।

**Live iteration** browser में alternatives की तुलना करने देती है। Keyboard navigation, mobile layout, error messages और contrast जांचें। Commands की संख्या releases में बदलती है। Installed version की सूची इस्तेमाल करें, video की संख्या याद न रखें।

### Higgsfield

**Higgsfield का MCP integration** agents को image और video generation service से जोड़ता है। इसकी [official integration page](https://higgsfield.ai/mcp) Claude Code और CLI connection options बताती है। अपने account और interface के लिए वर्तमान setup flow लें।

**जब missing deliverable media हो तब Higgsfield चुनें।** Illustrative product page के लिए variants बनाने से पहले aspect ratio, composition, brand constraints और placement लिखें। Visual brief को page implementation से अलग रखें।

**Service access और consumption पहले जांचें।** Integration listing हर model तक access, unlimited generation या commercial usage right सिद्ध नहीं करती। Production workflow से पहले account terms और selected model देखें।

**Final file को intended display size पर review करें।** Visible text, unwanted symbols, crop और product consistency जांचें। Generated terminal screens और diagrams सफल test का प्रमाण नहीं हैं।

| Design deliverable | Completion evidence |
|---|---|
| **Interface revision** | Required actions target viewports पर काम करें |
| **Image asset** | Dimensions, crop और content brief से मेल खाएं |
| **Video asset** | Timing, motion और final export brief से मेल खाएं |

## दोहराने योग्य workflow जोड़ें

### n8n MCP

**n8n का built-in MCP server** connected clients के लिए workflow operations खोलता है। वर्तमान [connection documentation](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) Cloud और self-hosted instances कवर करती है। Workflow building और editing n8n 2.13.0 से documented है। यह लेख n8n के अपने server पर है, समान नाम वाले community package पर नहीं।

**यहां instance-level access लें।** MCP Server Trigger node का scope अलग है: एक workflow से exposed tools। [Tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) को deployed version से मिलाएं।

**Access सोच-समझकर enable करें।** Existing workflows को full access के लिए MCP exposure चाहिए। Search previews user permissions के भीतर अधिक visibility रखते हैं। Workflow exposure client-specific अलग allowlist नहीं है, हालांकि client permissions operations को नियंत्रित करती हैं।

**Execution mode जांचें।** Documented **`execute_workflow`** default published production version चलाता है। Manual mode current unpublished version चलाता है। Execution से पहले inputs और downstream actions जांचें।

**पहला उपयोगी trial:** synthetic support requests classify करें और results test destination में लिखें। Missing fields और retries की जांच करें। Self-hosting के लिए compute, maintenance और paid downstream services भी चाहिए।

## नियंत्रित ट्रायल चलाएं

**Illustrative exercise:** छोटी application में CSV importer जोड़ें। Importer rows preview करता है, invalid email fields बताता है और duplicate creation रोकता है। Customer records या live external destinations की जरूरत नहीं।

```yaml
# Evaluation worksheet, not a tool configuration file
task: "add CSV import preview"
inputs:
  - "valid rows"
  - "invalid email field"
  - "repeated customer identifier"
  - "same import submitted twice"
acceptance:
  - "preview creates no records"
  - "invalid rows receive useful messages"
  - "duplicate policy matches the written requirement"
  - "repeat submission creates no extra records"
record:
  - "source revision and selected skill version"
  - "model and service configuration"
  - "elapsed time and billed usage"
  - "failed checks and human corrections"
```

**पहले baseline बनाएं।** Starting revision बचाएं और agent को existing workflow से task पूरा करने दें। Independent acceptance checks चलाएं और result रखें। उसी revision से एक selected extension और समान requirements के साथ दोहराएं।

**Experiment को suspected problem से मिलाएं।** Duplicate handling गलत समझी जाती है तो requirements skill trial करें। Existing validator छूटता है तो repository mapping trial करें। Users errors नहीं देखते तो interface critique trial करें। सभी दस टूल एक साथ load करने से attribution संभव नहीं रहती।

**Expected reasoning:** सफल दूसरा प्रयास उपयोगी evidence है, लेकिन एक run सामान्य productivity multiplier सिद्ध नहीं करता। Repeated runs tool value और model variability अलग करने में मदद करते हैं। Accepted results, review effort और failed attempts की तुलना करें।

| Observation | Interpretation |
|---|---|
| **Faster answer, failed tests** | Task completion के बिना कम response time |
| **Longer run, fewer corrections** | Total delivery effort में संभावित लाभ |
| **Two agreeing reviewers** | Independent verification मांगने वाली agreement |
| **Lower agent usage, new service charges** | Providers के बीच cost transfer |

**Retained decision record बनाएं।** Problem, selected tool, observed benefit, unresolved issue और next trial की conditions लिखें। जिस tool का योगदान इस जांच में टिके उसे रखें। बड़ी installed collection के लिए बड़ा active workflow जरूरी नहीं।

## समस्या समाधान

| लक्षण | अगली जांच |
|---|---|
| **Skill मौजूद है पर command fail है** | Executable installation, PATH और required sidecar files |
| **Old tutorial names में commands नहीं** | Installed version और canonical upstream instructions |
| **Graph recent changes छोड़ता है** | Graph freshness और separate document refresh |
| **Reviewer resolved objections दोहराता है** | Exact plan revision, evidence और review budget |
| **Notebook authentication fail है** | Auth diagnostic, session validity और upstream issues |
| **n8n connection में expected operations नहीं** | Deployed version, exposure settings और granted permissions |
| **Design बेहतर दिखता है पर खराब चलता है** | Original acceptance criteria और interaction checks |

**Installation layers इसी क्रम में जांचें:** files present, host discovery, dependencies ready, authentication working और representative task verified। Successful installer केवल chain का एक हिस्सा सिद्ध करता है।

**दूसरी copy जोड़ने से पहले overlapping skills देखें।** Requirements interviews, planning suites, design tools और review packages में competing defaults हो सकते हैं। Job के लिए एक primary procedure चुनें। Named contributions के लिए supporting tools जोड़ें। Repository policy और requested scope बचाएं।

## वीडियो वॉकथ्रू

{{< youtube id="IShdbDP4Jgg" enable="true" title="The Top 10 Claude Code Plugins to 10x Your Next Project (June '26)" >}}

**Chase AI का walkthrough** यहां चर्चा किए गए दस projects का परिचय देता है। Demonstrations के लिए [original video देखें](https://www.youtube.com/watch?v=IShdbDP4Jgg)। Current installation और behavior के लिए linked project documentation लें। Video title promotional claim है, इस guide से स्थापित measured result नहीं।

## अगले कदम

**एक recurring failure और एक acceptance test चुनें।** Matching extension को disposable project पर trial करें। फिर वह सबसे छोटा combination रखें जो result सुधारता है। Knowledge management, media generation या automation तभी जोड़ें जब work को ये outputs चाहिए।

**संबंधित मार्गदर्शन के लिए** agent चुनते समय [CLI coding-agent comparison](/articles/cli-coding-agents-comparison/) पढ़ें। Requirements, evidence और review responsibilities के practical work के लिए [AI collaboration course](/ai-collaboration-course-start/) लें।

{{< centerbutton href="/ai-collaboration-course-start/" >}}
AI Collaboration Course पढ़ें
{{< /centerbutton >}}

## संदर्भ

- [Graphify: code graphs और installation](https://github.com/Graphify-Labs/graphify)
- [Matt Pocock: skill collection](https://github.com/mattpocock/skills)
- [Claudex Loop: current grill-me-codex project](https://github.com/chaseai-yt/claudex-loop)
- [OpenAI: Codex plugin for Claude Code](https://github.com/openai/codex-plugin-cc)
- [claude-obsidian: source-linked knowledge management](https://github.com/AgriciDaniel/claude-obsidian)
- [Multica: Karpathy-inspired coding guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
- [Impeccable: design commands and installation](https://github.com/pbakaus/impeccable)
- [Higgsfield: agent integration](https://higgsfield.ai/mcp)
- [notebooklm-py: unofficial library, CLI, and skill](https://github.com/teng-lin/notebooklm-py)
- [n8n: official MCP connection guide](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
