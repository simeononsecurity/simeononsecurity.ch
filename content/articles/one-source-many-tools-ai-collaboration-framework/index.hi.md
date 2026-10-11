---
title: "एक स्रोत, अनेक उपकरण: मिश्रित टीमों के लिए AI सहयोग ढांचा"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "डेवलपर और गैर-डेवलपर के लिए साझा AI सहयोग ढांचा बनाएं। सत्य के स्रोत तय करें, संदर्भ संस्करणों को ट्रैक करें, स्थायी बदलावों की समीक्षा करें और प्रोजेक्ट मैप, RAG या दोनों चुनें।"
genre: ["कृत्रिम बुद्धिमत्ता", "ज्ञान प्रबंधन", "सॉफ्टवेयर इंजीनियरिंग", "टीम सहयोग"]
tags: ["AI सहयोग ढांचा", "मिश्रित टीमें", "सत्य का स्रोत", "AI एजेंट", "AGENTS.md", "CLAUDE.md", "Cline नियम", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "retrieval augmented generation", "RAG", "Model Context Protocol", "प्रोजेक्ट मैप", "संदर्भ मैनिफेस्ट", "ज्ञान प्रबंधन", "दस्तावेज़ विचलन", "मानवीय स्वीकृति", "निर्णय रजिस्टर", "एजेंट हैंडऑफ", "नीति संस्करण", "Git worktrees", "pull request gates"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "साइबर सुरक्षा कार्य पर सहयोग करते पेशेवरों के समूह का चित्र"
coverCaption: ""
---

**दो लोग दो AI उपकरणों से एक ही सवाल पूछते हैं:** सेवा को export कितने समय तक रखना चाहिए? इस उदाहरण में डेवलपर का IDE एजेंट README से सात दिन पढ़ता है। ऑपरेशंस सहायक wiki पेज से तीस दिन पढ़ता है। दोनों उत्तर भरोसेमंद लगते हैं। दोनों ने सत्य की अलग प्रति पढ़ी।

**विफलता prompt की गुणवत्ता में नहीं, स्वामित्व में है।** Wiki की आवश्यकता बदली, लेकिन README नहीं बदला। एजेंट पुराने दस्तावेज़ का पालन करता है और सही दिखने वाला गलत patch बनाता है। समीक्षक उस आवश्यकता का संस्करण नहीं देखते जिसने उत्तर को दिशा दी।

**हर तथ्य का एक घर तय करें।** हर उपकरण को उसी घर से पढ़ाएं और हर स्थायी बदलाव को व्यक्ति की समीक्षा से गुजारें। Repository, wiki और tracker के अलग उद्देश्य रखें। स्पष्ट अधिकार, नामित मालिक और सूचना स्थानांतरित करने की साझा प्रक्रिया तय करें।

**यह मार्गदर्शिका इस सप्ताह लागू करने योग्य मॉडल देती है**, RAG हो या न हो। पहले project map, versioned instructions, evidence records और reviewed proposals बनाएं। Search infrastructure तभी जोड़ें जब retrieval समस्या वास्तविक हो।

**पहला deliverable source register है**, connector नहीं। हर तथ्य प्रकार, authoritative home, owner, current revision और approval owner लिखें।

## मुख्य बातें

- **अधिकार सूचना प्रकार के अनुसार तय करें**, हर चीज को एक application में न भरें।
- **Memory और retrieval indexes को cache मानें**, स्वतंत्र policy source नहीं।
- **Proposal में source version जोड़ें**, ताकि reviewer जान सके कि बदलाव किन तथ्यों पर आधारित है।
- **Prompt के बाहर approval लागू करें**, access controls और review gates से।
- **प्रक्रिया सभी tools में समान रखें**, interface के अनुसार उसका रूप बदलें।

## शुरू करने से पहले

**आवश्यकताएं:** एक pilot project चुनें जिसमें repository, wiki या document system, tracker और review करने वाले owners हों। Wiki न हो तो versioned document store लें। Ownership model वही रखें।

**समय:** प्रारंभिक map और templates के लिए दो से चार घंटे, फिर एक सप्ताह का pilot रखें। **कठिनाई:** मध्यम। कठिन भाग authority पर सहमति है, नया AI tool लगाना नहीं।

**सीमा:** यह प्रस्तावित team operating model है। Approval rules और naming conventions Claude Code, Codex, Cline, Cowork, Copilot या ChatGPT का default behavior नहीं हैं।

## मिश्रित उपकरण, अलग संदर्भ

**Coder और non-coder एक project साझा करते हैं**, लेकिन interfaces अलग इस्तेमाल करते हैं। Developer IDE या terminal agent में काम करता है। Product owner chat project में काम करता है। Operations lead wiki और tracker से काम करता है। Interface task के अनुसार चुनें, authoritative facts के access के अनुसार नहीं।

**Context वर्तमान उत्तर के लिए उपलब्ध सामग्री है।** Repository files, uploaded documents, chat history, saved memory, connector results और retrieved excerpts देखें। अलग evidence वाली दो sessions अलग उत्तर दे सकती हैं।

| विफलता | दिखाई देने वाला परिणाम |
|---|---|
| **Documentation drift** | README पुरानी आवश्यकता दोहराता है |
| **Summary promotion** | मूल source के बिना session summary evidence बन जाती है |
| **Overlapping writes** | दो agents अलग base versions से एक page बदलते हैं |
| **Lost decisions** | Meeting agreement decision register में नहीं आता |
| **Missing provenance** | उत्तर page version या commit नहीं बताता |

**Retention उदाहरण अंतर स्पष्ट करता है।** Wiki approved behavior बताता है। Code implemented behavior बताता है। कोई भी चुपचाप दूसरे को rewrite न करे। अंतर दर्ज करें और named owner से निर्णय मांगें।

> **मुख्य बात:** AI tool चुनने से पहले authority पर सहमति बनाएं।

### साइडबार: पांच साझा शब्द

| शब्द | इस ढांचे में अर्थ |
|---|---|
| **Source** | किसी सूचना प्रकार का authoritative record |
| **Cache** | speed या convenience के लिए derived copy |
| **Proposal** | owner approval की प्रतीक्षा करता suggested change |
| **Project map** | source locations, identifiers और owners का index |
| **Manifest** | उत्तर या proposal में उपयोग हुए exact evidence का record |

## हर तथ्य का एक घर

**One source का अर्थ हर fact के लिए एक authority है**, पूरे संगठन के लिए एक database नहीं। Pilot में यह allocation तय करें।

| सूचना प्रकार | Home system | Owner | कौन लिखता है | Agents कैसे पढ़ते हैं |
|---|---|---|---|---|
| **Code, tests, config, schemas** | Repository | Engineering maintainer | Reviewed PR के contributors | Recorded commit की files |
| **Shipped docs और ADRs** | Repository | Technical owner | उसी PR के contributors | Versioned files |
| **Requirements** | Wiki | Product owner | Owner या approved publisher | Page ID और revision |
| **Runbooks** | Wiki | Operations owner | Approved publisher | Page ID और revision |
| **Policy** | Wiki | Policy owner | Review के बाद approved publisher | Canonical page और local adapter |
| **Cross-team decisions** | Wiki decision register | Named decision owner | Approval के बाद owner | Decision ID और status |
| **Tasks और findings** | Tracker | Task owner | People या authorized intake | Issue key और revision |
| **Chats, summaries, embeddings** | Cache only | Session/index steward | Tools और participants | Source check के बाद reference |

ADR code के पास रखें जब वह repository design नियंत्रित करता हो। Cross-team decision shared register में रखें। Local policy copy canonical page के नीचे रहे। Cache source को override नहीं करता।

## Cache नीचे, proposal ऊपर

**Agents evidence को session context में लाते हैं**, फिर proposal बनाते हैं। वे अकेले durable facts approve नहीं करते। Draft बनाना policy publish या code merge करना नहीं है।

```text
Source -> permission-checked read -> session context
Session context -> proposal + base version -> owner review
Owner approval -> controlled publication -> change log
Changed base version -> reconcile proposal -> review again
```

**Review से पहले base version जोड़ें।** Reviewer को previous value, proposed value, reason, evidence और affected systems चाहिए। Approval किसी specific proposal revision से जुड़ा हो।

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Retain exports for thirty days instead of seven."
evidence:
  - "decision:DEC-12 accepted"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**ऊपर के identifiers illustrative हैं।** हर approved logical change के लिए proposal ID, previous और resulting versions, approver, timestamp और publication reference वाली change-log row रखें।

## RAG के बिना साझा context

**Project map पहला retrieval index है।** हर project के लिए source IDs, repository locations, tracker keys, authority scopes और owners वाला page रखें। पहले map पढ़ें, फिर ID से record लें।

### साइडबार: नमूना project map

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Direct connectors manual copying घटाते हैं।** MCP AI applications को tools और context देने वाला integration protocol है। Approved connectors का उपयोग करें, लेकिन authorization और freshness checks बनाए रखें। Offline काम में exported revision को snapshot के रूप में दर्ज करें।

## एक policy, अलग adapters

**एक shared policy रखें**, फिर छोटे tool-specific adapters बांटें। हर adapter की पहली line में approved policy version, source ID और reviewed local snapshot दें। Codex `AGENTS.md`, Claude Code `CLAUDE.md` और Cline `.clinerules/` के अलग loading नियमों का व्यवहार installed version में जांचें।

### साइडबार: नमूना AGENTS.md header

```markdown
Policy-Version: v3 | Source: wiki:POL-01 | Status: approved

# Project instructions

Read the project map MAP-01 before starting a task.
Load docs/policy-snapshot.md and record its source revision.
Treat chat memory and search excerpts as caches.
Attach source revisions to every factual proposal.
Use one task and one worktree per coding task.
Do not publish policy, approve decisions, or merge your own code.
Stop on unresolved source conflicts or overlapping writes.
Required checks: tests, documentation review, policy freshness.
Owners: engineering maintainer, product owner, policy owner.
```

Version label समान सामग्री का प्रमाण नहीं है। Approved snapshot से adapters बनाएं या policy हिस्से का digest compare करें। Local overrides और disabled rules जांचें।

## Context manifest दर्ज करें

**Context manifest उत्तर के evidence को समझाता है।** Page IDs, revisions, issue keys, update times और full repository commit दर्ज करें। Retrieval time और sections भी लिखें। उपलब्ध न होने वाले records को mark करें।

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook not retrieved. No runbook change proposed."
```

Synthetic commit को वास्तविक inspected commit से बदलें। हर material claim को source और section से जोड़ें। Conflicting sources को साथ रखें और scope तथा approval जांचे बिना newest timestamp न चुनें।

## RAG के साथ साझा context

**Retrieval-augmented generation (RAG)** model को response बनाते समय retrieved material देता है। Semantic index अलग शब्दों में लिखे passages खोजता है। बड़े collections में RAG discovery के लिए उपयोगी है, authority के लिए नहीं। Transcript में कही बातें approved requirement नहीं बनतीं।

| Index rule | Required behavior |
|---|---|
| **Ingest sources, not caches** | Generated summaries और untracked copies हटाएं |
| **Preserve provenance** | हर chunk में source ID, revision, section और status रखें |
| **Refresh on change** | Edit पर re-index करें और पुराने chunks invalidate करें |
| **Honor access changes** | Permissions update करें और revoked content हटाएं |
| **Return citations** | Retrieved text के साथ references दें |
| **Check the live record** | Consequential proposal से पहले current evidence लें |

Retrieved chunk pointer है। Live source wording, exceptions और access की पुष्टि करता है। Live retrieval विफल हो तो snapshot label करें और durable action रोकें। Stale embeddings और missing context अलग जोखिम हैं। Permission leakage के लिए authorization को model को chunk देने से पहले लागू करें।

## Map, RAG या दोनों चुनें

**Question के अनुसार retrieval चुनें।** Known requirement ID direct access को favor करता है। Scattered history open search को। Known lookup में map से शुरू करें।

### साइडबार: RAG या नहीं?

```text
Do tasks usually name a project, page, issue, or file?
  Yes -> Is direct retrieval sufficient for the pilot?
           Yes -> MAP ONLY
           No  -> HYBRID: map for known IDs, RAG for discovery
  No  -> Is evidence scattered across a large collection?
           No  -> MAP ONLY, plus native search
           Yes -> Is work exploratory and read-only?
                    Yes -> RAG-LED ONLY for discovery
                    No  -> HYBRID with live-source checks

Every option retains owners, authorization, and provenance.
RAG-led discovery still checks sources before durable action.
```

RAG-only retrieval interface है, governance छोड़ने की permission नहीं। Hybrid model discovery और verification अलग करता है। Map बताता है “कहां”, source बताता है “क्या”।

## Repository के अंदर की जानकारी

**Repository knowledge implementation के साथ बदलता है।** Agent और reviewer के लिए compact structure रखें।

| File या directory | Responsibility |
|---|---|
| **`CONTEXT.md`** | Project terms और authoritative records के links |
| **`docs/adr/`** | Accepted architecture decisions |
| **`docs/design/`** | Approved behavior descriptions |
| **`docs/plans/`** | Status वाली proposed implementation plans |
| **`AGENTS.md`** | Review gates, boundaries और owner roles |
| **`README.md`** | Setup और entry points, duplicate requirements नहीं |

**Same-PR rule लागू करें:** code और affected docs साथ बदलें। Update न हो तो PR में exception लिखें। एक task, branch और worktree रखें। Default branch पर सीधे commit न करें।

```text
KB-Update: none (reason: internal refactor preserves documented behavior)
```

## Repository के बाहर की जानकारी

**Wiki में documentation standard रखें।** हर authoritative page में purpose, status, owner, revision, review date और related source IDs हों। Proposals को non-authoritative drafts में रखें।

**Safe update क्रम:**

1. **Relire** वर्तमान page और surrounding constraints.
2. **Compare** base version से।
3. **Reconcile** बीच के edits और approval।
4. **Write** expected-version condition के साथ।
5. **Verify** saved page और change-log reference।

Conditional update उपलब्ध हो तो उपयोग करें। Tracker findings में observation, exact command, commit, expected behavior, actual behavior और acceptance criteria रखें।

```text
Finding: retention implementation disagrees with approved requirement
Evidence: REQ-17 v8 and inspected config/retention.yaml
Inspection command: git show HEAD:config/retention.yaml
Commit: full inspected commit ID recorded in the manifest
Acceptance: approved duration matches code, tests, and runbook
Status: awaiting product and engineering owner review
```

Decision register में question, options, trade-offs, owner और approval रखें। Agents propose करते हैं। लोग decide करते हैं।

## दोनों systems को जोड़ें

**Post-merge sync implementation changes बाहर भेजता है।** Merged commit, approved requirement और runbook से linked wiki task बनाएं। Owner saved page verify करे। Policy freshness को अलग audit रखें।

| Check | Completion evidence |
|---|---|
| **Policy freshness** | Canonical version और adapter digest comparison |
| **Requirement reconciliation** | Requirement revision की code और tests से तुलना |
| **Post-merge sync** | Merged commit से published wiki revision link |
| **Conflict resolution** | दोनों records से linked owner-approved decision |

Pilot में weekly audit रखें। Behavior-changing PR को merge से पहले requirement check चाहिए। तीस दिन वाला बदलाव product approval, code और tests, PR review और runbook publication से गुजरता है।

## हर tool के लिए एक procedure

**Repeated steps को versioned procedure ID वाले skills या prompts में रखें।** Contract साझा करें, universal file format न मानें।

| Procedure | Required output |
|---|---|
| **Start task** | Owner, scope, policy version, source manifest, write reservation |
| **Doc lint** | Missing metadata, duplicate authority, broken source references |
| **Knowledge check** | Supporting revisions वाले requirement-code gaps |
| **Handoff** | Current evidence, proposals, completed checks, unresolved questions |

Non-coders chat projects में वही proposal template भरते हैं। Coders PR में approved proposal, inspected commits और checks जोड़ते हैं। दोनों groups एक ही evidence structure hand off करते हैं।

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "Attached source IDs, revisions, and inspected commit"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["RUN-04 publication assigned to operations-owner"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

Handoff भी cache है। अगला व्यक्ति source reread करे और नई revisions दर्ज करे।

## हर write से पहले guardrails

**Data को home से बाहर भेजने से पहले screen करें।** Classification, connector permissions, approved destinations, provider handling और logging जांचें। Minimum relevant content भेजें।

**Retrieved text evidence है, instruction channel नहीं।** Wiki का text policy को override नहीं करता। हर page या file के लिए एक active owner रखें, reservation और expiry दर्ज करें, write से पहले reread करें।

| Stop-and-ask trigger | Required response |
|---|---|
| **Owner के बिना sources disagree** | Pause और authority मांगें |
| **दूसरी task target reserve करती है** | Edit से पहले ownership negotiate करें |
| **Base version बदल गया** | Reconcile और renewed approval लें |
| **Material claim बिना evidence** | Unverified mark करें और source मांगें |
| **Data handling unclear** | Content home system में रखें |
| **Live source access fail** | Snapshot limit दर्ज करें और durable action रोकें |

Prompts security controls नहीं हैं। Permission denial, protected branches, stale-base rejection और write ownership को model के बाहर test करें।

## Promotion से पहले pilot

**Framework को draft से शुरू करें।** Coder, non-coder और source owners वाला एक project चुनें। दो tools में same known-ID question चलाएं और source conflict exercise करें। Manifest और proposals देखें।

| Metric | Definition |
|---|---|
| **Citation rate** | Source-supported material claims / sampled material factual claims |
| **Weekly drift findings** | Source type के अनुसार confirmed authority/version mismatches |
| **Proposal turnaround** | Review-ready proposal से recorded decision तक median time |
| **Stale-context rework** | Obsolete या unverified evidence से reopened tasks |

Targets से पहले baseline मापें। अधिक findings बेहतर detection दिखा सकते हैं। Synthetic repository में map, adapters, manifests, proposal templates और executable checks रखें।

## Shared context troubleshooting

| Symptom | First repair |
|---|---|
| **दो tools अलग उत्तर देते हैं** | IDs, revisions, scope और approval status compare करें |
| **Instructions current, behavior अलग** | Loaded adapters, toggles और overrides inspect करें |
| **RAG old requirements देता है** | Index refresh और live page जांचें |
| **Wiki edit दूसरी change मिटाती है** | Conditional writes या serialized publication चाहिए |
| **Docs checks stale wording स्वीकारते हैं** | Owner review और requirement reconciliation जोड़ें |
| **Decisions chat में रहती हैं** | Proposal intake और register owner तय करें |

**Prompt बदलने से पहले evidence path ठीक करें।** Failed pilot case फिर चलाएं और परिणाम दर्ज करें।

## इस सप्ताह के दस कदम

1. **एक pilot project चुनें** और लोग तथा tools तय करें।
2. **हर information type का home और owner तय करें।**
3. **Source IDs और authority scopes वाली project map publish करें।**
4. **Shared policy draft करें** और owner review लें।
5. **हर instruction adapter को version करें** और loading verify करें।
6. **Material factual answers और proposals के लिए context manifest मांगें।**
7. **Base versions और named approvers वाला proposal path बनाएं।**
8. **Write controls और same-PR documentation rule लागू करें।**
9. **Synthetic records से drift, conflict और handoff test करें।**
10. **Pilot metrics review करें** और अगला rollout stage approve करें।

**हर तथ्य का एक घर रखें, हर tool को वहीं से पढ़ाएं और हर durable change को व्यक्ति से गुजारें।**

## References और अगले कदम

**Official documentation technical components को support करती है**, organizational rules को नहीं। Pilot में installed behavior और connector permissions जांचें।

- **Codex instructions:** [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- **Claude Code instructions:** [How Claude remembers your project](https://code.claude.com/docs/en/memory)
- **Cline instructions:** [Rules](https://docs.cline.bot/customization/cline-rules)
- **Retrieval design:** [Retrieval-augmented generation in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- **Connector security:** [MCP Security Best Practices](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices)
- **Working-tree isolation:** [Git worktree documentation](https://git-scm.com/docs/git-worktree)

**Local inference planning के लिए** [Local AI GPU Context Guide](/articles/local-ai-model-gpu-context-guide/) पढ़ें। Hardware capacity और shared-source governance अलग समस्याएं हैं। बड़ा context window conflicting authority नहीं सुधारता।

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Local AI GPU Context Guide पढ़ें
{{< /centerbutton >}}
