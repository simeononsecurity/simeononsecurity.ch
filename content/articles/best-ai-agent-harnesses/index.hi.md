---
title: "2026 के सर्वश्रेष्ठ AI Agent Harnesses: कार्यप्रवाह के आधार पर चुनें"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Deep Agents, Claude Agent SDK, OpenAI Agents SDK, Pydantic AI, Pi और LangGraph की तुलना टूल निष्पादन, मेमोरी, रिकवरी और एकीकरण प्रयास के आधार पर करें।"
genre: ["कृत्रिम बुद्धिमत्ता", "सॉफ्टवेयर विकास", "AI सुरक्षा"]
tags: ["AI agent harnesses", "श्रेष्ठ agent frameworks", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "Pi coding agent", "LangGraph", "agent runtime", "tool calling", "agent memory", "context management", "durable execution", "agent permissions", "AI agent security", "local AI agents", "agent evaluation", "human in the loop", "agent SDK comparison", "production agents"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "अंधेरी कार्य सतह पर चमकीले केंद्रीय प्रोसेसर से जुड़े हुए मॉड्यूलर धातु घटक, जिनके बीच फ़िरोज़ी और नारंगी रास्ते हैं"
coverCaption: "AI मॉडल के आसपास मौजूद घटकों का वैचारिक चित्रण।"
---

**Deep Agents कॉन्फ़िगर किए जा सकने वाले मॉडल और अंतर्निहित संदर्भ प्रबंधन वाले सामान्य एजेंट के लिए मेरी पहली सूची में है।** Claude Agent SDK, Claude Code के निष्पादन व्यवहार को ऐप में जोड़ने के लिए उपयुक्त है। ऐप-विशिष्ट एजेंटों के लिए OpenAI Agents SDK और Pydantic AI का परीक्षण करें। Pi छोटा और विस्तार योग्य कोर रखता है, जबकि LangGraph स्पष्ट कार्यप्रवाह नियंत्रण पर केंद्रित है।

**सही चुनाव उस काम पर निर्भर है जिसे आप स्वीकार करना चाहते हैं।** शोध सहायक, रिपॉज़िटरी संपादक और ग्राहक अनुरोधों को संसाधित करने वाली सेवा के लिए अलग टूल और रिकवरी नियम चाहिए। ये सिफारिशें 10 अक्टूबर 2026 को जाँचे गए आधिकारिक दस्तावेज़ों पर आधारित संपादकीय निर्णय हैं। ये व्यावहारिक प्रदर्शन बेंचमार्क के परिणाम नहीं हैं।

<!--more-->

## मुख्य बातें

- **पहले abstraction चुनें:** assembled agent, application SDK या workflow runtime।
- **निष्पादन सीमाएँ जाँचें:** टूल approval, filesystem isolation और network policy अलग समस्याएँ हल करते हैं।
- **रिकवरी का परीक्षण करें:** केवल conversation history दोहरी बाहरी कार्रवाई नहीं रोकती।
- **स्वीकृत काम मापें:** लागत तुलना में failures, review time और infrastructure शामिल करें।
- **मॉडल स्पष्ट रखें:** मॉडल और agent software दोनों बदलने पर पूरा system test होता है, केवल software नहीं।

## Harness क्या देता है

एक **agent harness मॉडल कॉल के आसपास का software है।** यह context तैयार करता है, tools उपलब्ध कराता है, approved actions चलाता है, परिणाम वापस देता है और तय करता है कि कब आगे बढ़ना या रुकना है। Implementation के अनुसार यह memory, delegation, permissions और recovery भी संभालता है।

एक **model** अगली कार्रवाई सुझाता है। एक **tool** operation करता है। एक **runtime** workflow चलाता और सुरक्षित रखता है। Packaged products में ये जिम्मेदारियाँ मिल सकती हैं, फिर भी उन्हें अलग करने से missing capabilities दिखती हैं।

| Component | पूछने योग्य प्रश्न |
|---|---|
| **Context management** | लंबी run में कौन सी requirements बचती हैं? |
| **Tool execution** | Arguments कौन validate करता है और authority कौन सीमित करता है? |
| **State storage** | Process restart के बाद क्या बचता है? |
| **Verification** | Completion सिद्ध करने के लिए कौन सा evidence चाहिए? |

एक **illustrative support agent** को order देखने और replacement request तैयार करने को कहें। Order पढ़ना, replacement सुझाना और submission करना अलग permissions में होना चाहिए। अच्छा explanation submission की permission सिद्ध नहीं करता। Saved transcript यह सिद्ध नहीं करती कि submission पहले हो चुकी है।

**Scope:** यह guide embeddable software और runtime choices की तुलना करती है। दैनिक developer interfaces के लिए अलग [CLI coding-agent comparison](/articles/cli-coding-agents-comparison/) या [GUI coding-agent comparison](/articles/gui-coding-agents-comparison/) देखें। SDK comparison को चुपचाप terminal tools और editor extensions की ranking न बनाएं।

## व्यावहारिक shortlist

| शुरुआती आवश्यकता | पहले जाँचने का विकल्प | मुख्य जिम्मेदारी जो आपके पास रहती है |
|---|---|---|
| **General-purpose agent** | Deep Agents | Backend, permissions और model configure करना |
| **ऐप में Claude Code** | Claude Agent SDK | Execution process चलाना और isolate करना |
| **Application tool workflow** | OpenAI Agents SDK | Tools, approvals और acceptance define करना |
| **Typed Python application** | Pydantic AI और उसका Harness package | Capabilities और workspace चुनना |
| **Minimal embeddable coding core** | Pi SDK | Extensions और execution policy assemble करना |
| **Explicit durable workflow** | LangGraph | Graph state और recovery behavior design करना |

**ये अलग starting points हैं।** Deep Agents पहले से LangGraph का उपयोग करता है, इसलिए चुनाव अनिवार्य रूप से either-or नहीं है। Pydantic AI भी अपने core agent framework को assembled harness capabilities से अलग रखता है। हर row को interchangeable library मानने के बजाय वह application code मापें जिसे आपको own करना होगा।

**Acceptance test पास करने वाली सबसे छोटी layer से शुरू करें।** Bounded tool calls के लिए typed application framework, open-ended file या research work के लिए assembled agent और named states वाली recovery के लिए explicit graph चुनें। Memory, shell access या subagents तभी जोड़ें जब test सरल layer की कमी दिखाए।

## Deep Agents: assembled capabilities

**Files, tools और लंबी conversations पर काम करने वाले agent के लिए पहले Deep Agents देखें।** इसका [official overview](https://docs.langchain.com/oss/python/deepagents/overview) filesystem backends, context offloading, summarization, subagents और human approval document करता है। यह LangChain और LangGraph runtime पर बना है और कई model providers से जुड़ता है।

**Configuration अब भी behavior तय करती है।** Current documentation के अनुसार version 0.7 से task planning opt-in है। पुराने release का tutorial current defaults बताता है, ऐसा न मानें। Evaluation में package version और enabled middleware लिखें।

**Permission scope ध्यान से जाँचें।** Documented filesystem rules built-in file tools को cover करते हैं, sandbox backends से चलने वाले arbitrary shell commands को नहीं। अगर दूसरा execution path उसी file तक पहुँचता है तो file-tool denial पर्याप्त नहीं है। Backend और shell boundary को साथ test करें।

**मेरी recommendation:** Document-analysis या repository-work service के लिए इसे shortlist करें जब assembled capabilities और provider choice चाहिए। दो narrowly defined API calls और validated response वाली task के लिए छोटा starting point लें। Extra tools अतिरिक्त behavior लाते हैं, जिसे evaluate करना होगा।

## Claude: embedded execution

**जब Claude Code का agent application में चाहिए, Claude Agent SDK चुनें।** Anthropic के अनुसार Python और TypeScript library वही execution loop, tools और context management इस्तेमाल करती है जो Claude Code में हैं। SDK आपके चलाए process में Claude Code binary चलाता है। यह basic Anthropic API client और hosted Managed Agents से अलग है। [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)।

**फायदा मौजूदा execution system का reuse है।** File operations, commands, hooks, permissions, sessions और subagents documented capabilities के रूप में मिलते हैं। आपकी integration application boundary और task-specific acceptance checks देती है।

**Hosting engineering decision है।** Anthropic की [deployment guidance](https://code.claude.com/docs/en/agent-sdk/secure-deployment) filesystem controls, network restrictions और isolation पर चर्चा करती है। Permission prompt को operating-system boundary मानने के बजाय process के आसपास ये controls configure करें।

**मेरी recommendation:** बहुत से file और command work वाले Claude-centered document या coding automation के लिए इसे evaluate करें। अगर local models और कई hosted providers की तुलना product requirement है तो provider-flexible विकल्प चुनें।

| Assembled option | Integration emphasis |
|---|---|
| **Deep Agents** | Model selection, middleware और backend configuration |
| **Claude Agent SDK** | Application process के अंदर Claude Code execution |

## OpenAI: application tool workflows

**Functions, delegated tasks और explicit outputs वाली application के लिए OpenAI Agents SDK चुनें।** इसका [overview](https://openai.github.io/openai-agents-python/) agent loop, handoffs, guardrails, tracing और sandbox-agent capabilities document करता है। यह builder interface है और Codex developer application से अलग है।

**Approval configurable behavior है।** [Human-in-the-loop guide](https://openai.github.io/openai-agents-python/human_in_the_loop/) decision के बाद resume करने के लिए interrupted runs और serialized state बताती है। Local shell और patch tools में approval opt-in है। केवल approval callback जोड़ने से approval requirement सक्रिय नहीं होती।

**Model support OpenAI से आगे है।** [Provider documentation](https://openai.github.io/openai-agents-python/models/) external-provider integration points और adapters बताता है। Selected endpoint पर structured outputs, tool calling और transport validate करें। Feature parity मानकर न चलें।

**मेरी recommendation:** ऐसे service के लिए shortlist करें जिसकी useful actions पहले से well-defined application functions हैं। उदाहरण के लिए order लें, eligibility ordinary code में calculate करें और structured request तैयार करें। Model अगला tool चुनता हो तब भी authorization और eligibility checks application में रखें।

## Pydantic AI: typed applications

**जब Python types और validated outputs application के केंद्र में हों, Pydantic AI चुनें।** इसका [core documentation](https://pydantic.dev/docs/ai/overview/) typed tools, dependency injection, structured outputs और durable-execution integrations cover करता है। Validation output की required structure तय करती है। यह हर field की truth सिद्ध नहीं करती।

**अलग Harness package assembled capabilities जोड़ता है।** इसकी [documentation](https://pydantic.dev/docs/ai/harness/) Coder और Researcher stacks, filesystem और shell access, memory और workspace integrations दिखाती है। Local workspace और isolated sandbox अलग execution choices हैं। Relevant harness capabilities के लिए workspace चाहिए।

**मेरी recommendation:** typed records लौटाने वाली Python service के लिए core framework shortlist करें। Workspace exploration या open-ended research भी चाहिए तो harness capabilities जोड़ें। इससे bounded extraction service को बिना concrete need shell access नहीं मिलेगा।

एक **illustrative invoice-review agent** में schema validation जाँचती है कि total numeric है और currency allowed set में है। Separate application logic total को line items से compare करती है और source evidence verify करती है। Trial में दोनों checks रखें।

| Application concern | Acceptance check |
|---|---|
| **Structured output** | Fields validate करें और meaning independently verify करें |
| **Approval pause** | Exact pending action और decision persist करें |
| **Provider change** | Tool-call और output compatibility tests दोहराएँ |

## Pi: small extensible core

**Compact coding-agent implementation पर direct control चाहिए तो Pi SDK चुनें।** [Project documentation](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) interactive interface के साथ SDK और RPC integration बताता है। Default tools reading, writing, editing और shell execution हैं। Extensions अतिरिक्त behavior जोड़ती हैं।

**Minimalism integrator पर काम डालता है।** Pi built-in permission popups और subagent orchestration जानबूझकर नहीं देता। Confirmation flows के लिए documentation containers या custom extensions की ओर भेजती है। Embedded SDK evaluate करें, उसके terminal interface को दूसरे vendor के graphical editor से नहीं।

**मेरी recommendation:** bespoke coding service के लिए Pi shortlist करें, यदि execution restrictions, extension review और recovery policy आप संभालेंगे। छोटा core behavior समझने और बदलने में मदद करता है। पहले से assembled approval और orchestration system चाहिए तो यह कम उपयुक्त starting point है।

## LangGraph: explicit workflow control

**जब workflow को explicit state और transitions चाहिए, LangGraph चुनें।** इसकी [persistence documentation](https://docs.langchain.com/oss/python/langgraph/persistence) thread-scoped checkpoints और cross-thread stores अलग करती है। Persistent checkpointer process restart के बाद recovery support करता है। In-memory checkpointer नहीं करता।

**LangGraph runtime foundation है।** Workflow आप define करते हैं और model-driven behavior की जगह तय करते हैं। Deep Agents इसी foundation का उपयोग करता है। Execution paths पर अधिक direct control चाहिए तो LangGraph तक आना उचित है।

**मेरी recommendation:** named stages, review pauses और अलग recovery rules वाले process के लिए shortlist करें। Document-intake workflow fields extract, validate, review request और approved record publish कर सकता है। Fixed transitions तब उपयोगी हैं जब model content चुने लेकिन business process न बनाए।

| Workflow stage | Completion evidence |
|---|---|
| **Extract** | Source-linked candidate record |
| **Validate** | Deterministic checks और exceptions |
| **Review** | Specific candidate से जुड़ा decision |
| **Publish** | Operation से जुड़ी external receipt |

**External effects के लिए अलग recovery design चाहिए।** Graph state save करना remote service transaction को checkpoint के साथ atomic नहीं बनाता। Operation identifier रखें और submission retry से पहले external result reconcile करें।

## Missing pieces test करें

**Feature list केवल starting point है।** हर candidate को आपके workload जैसे failures से गुजारें। Disposable workspace और synthetic records वाले test services इस्तेमाल करें।

| Test | Retain करने वाला evidence |
|---|---|
| **Interrupted submission** | Recovery के बाद एक external effect |
| **Long conversation** | Original requirements अब भी पूरी हों |
| **Rejected action** | Alternate tool से कोई effect न हो |
| **Untrusted document instruction** | Document text authority न पाए |
| **Malformed tool arguments** | Application mutation से पहले rejection |
| **Budget exhaustion** | Inspectable partial work के साथ bounded stop |

**Repetition स्पष्ट रूप से define करें।** Replacement-request service में test service के request accept करने के बाद और local completion save होने से पहले worker रोकें। Restart पर workflow operation identifier lookup करे, blind resubmission नहीं। यह proposed test है, listed products का observed result नहीं।

**Compaction के बाद evidence जाँचें।** Task की शुरुआत में important requirement रखें। फिर इतना realistic material दें कि configured context strategy trigger हो। Agent से final artifact और supporting source references माँगें। हमारी [CLM और agent-memory analysis](/articles/context-language-models-agent-memory-hallucinations/) बताती है कि notes रखना और accurate evidence रखना अलग concerns हैं।

**Telemetry destinations review करें।** Tool traces और memory stores में task data हो सकता है। कौन से systems उन्हें receive करते हैं और कितने समय तक रखते हैं, लिखें। Local model inference local-only logging, retrieval या execution का प्रमाण नहीं है।

## Accepted task की लागत तुलना

**दो evaluation tracks रखें।** Controlled comparison में जहाँ संभव हो model, tools, task set और budgets समान रखें। Deployment comparison हर candidate की intended configuration इस्तेमाल करती है। पहली track कुछ software effects अलग करती है। दूसरी बताती है कि आपके काम के लिए कौन सा complete setup बेहतर है।

**Unsupported configurations को controlled track में force न करें।** Common model या tool interface न हो तो comparison को system evaluation कहें। Setup effort और human steering record में रखें।

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

**हर task पर कई trials चलाएँ।** Unsuccessful attempts denominator में रखें और raw counts के साथ percentages report करें। छोटा trial failure patterns दिखाता है, stable industry ranking नहीं।

**Illustrative cost calculation:** मानें setup A दस attempts पर $12 खर्च करता है और आठ accepted results देता है। Accepted task की inference cost $1.50 है। Setup B $8 खर्च करके चार accepted results देता है, इसलिए cost $2.00 है। दोनों numbers human review या infrastructure शामिल नहीं करते। उन्हें अलग recorded total में रखें।

**Testing से पहले disqualifying failures तय करें।** Unauthorized submission या cross-user data leak average quality score में छिपना नहीं चाहिए। Requirements enforce करने के बाद correctness, recovery, review effort और cost compare करें।

## Bounded choice बनाएं

**दो candidates और एक real workflow से शुरू करें।** Provider-flexible assembled agent के लिए Deep Agents को application के लिए suitable narrow alternative से compare करें। Service में Claude Code behavior चाहिए तो Claude Agent SDK trial करें। Typed application work में Pydantic AI और OpenAI Agents SDK compare करें। Custom behavior अतिरिक्त integration के योग्य हो तो Pi चुनें। Explicit workflow control priority हो तो LangGraph चुनें।

**Trial prerequisites:** approved model access, synthetic fixtures, जरूरत पर isolated workspace और written acceptance criteria। Setup और basic failure tests के लिए initial afternoon दें। Production decision से पहले repeated runs collect करें। External actions और recovery requirements के अनुसार difficulty intermediate से advanced हो सकती है।

**अपनी requirements पास करने वाला सबसे छोटा system चुनें।** Trial fixtures, package versions और failure records रखें। Model, context strategy, tools या execution backend बदलने पर फिर चलाएँ। ये बदलाव evaluated system बदलते हैं।

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
