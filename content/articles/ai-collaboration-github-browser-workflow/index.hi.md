---
title: "गैर-प्रोग्रामर के लिए GitHub AI वर्कफ़्लो: Issues और Pull Requests"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "स्थानीय विकास वातावरण के बिना ब्राउज़र संपादन, Issues, चैट संदर्भ पैकेट और समीक्षा किए गए pull requests का उपयोग करें।"
genre: ["कृत्रिम बुद्धिमत्ता", "टीम सहयोग", "सॉफ्टवेयर इंजीनियरिंग"]
tags: ["AI सहयोग पाठ्यक्रम", "GitHub ब्राउज़र संपादन", "GitHub Issues", "pull request", "गैर-प्रोग्रामिंग योगदानकर्ता", "संदर्भ पैकेट", "समीक्षा हैंडऑफ़"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "साइबर सुरक्षा कार्यक्षेत्र में साझा परियोजना कार्य की समीक्षा करते पेशेवरों का चित्रण"
coverCaption: ""
---

[AI सहयोग पाठ्यक्रम पर वापस जाएँ](/ai-collaboration-course-start/)

**गैर-प्रोग्रामिंग योगदानकर्ता ब्राउज़र के माध्यम से वही अधिकार नियम अपनाते हैं।** आप GitHub स्रोत पढ़ते हैं, स्वीकृत चैट टूल से मसौदा बनाते हैं और Issue या branch edit भेजते हैं। Maintainer जाँच चलाता है और समीक्षा के बाद प्रकाशित करता है। ब्राउज़र पहुँच coding-agent नियंत्रणों को पार न करे, इसलिए repository protection सक्रिय होने के बाद इस वर्कफ़्लो का उपयोग करें।

## मुख्य बातें

- **ब्राउज़र कार्य** के लिए स्थानीय terminal की आवश्यकता नहीं है।
- **संदर्भ पैकेट** scope और revision का प्रमाण सुरक्षित रखते हैं।
- **Issues और branches** प्रस्ताव बने रहते हैं।
- **Handoffs** लंबित काम और अगली भूमिका बताते हैं।

## शुरू करने से पहले

**पूर्वापेक्षाएँ:** [repository boundary lesson](/articles/ai-collaboration-github-repository/), lab का read access और आवश्यकता होने पर स्वीकृत chat tool। **अनुमानित समय:** 45 से 60 मिनट। **कठिनाई:** शुरुआती। केवल Issue भेजने वाले योगदानकर्ता local Git और Actions छोड़ सकते हैं। PR भेजने वाले योगदानकर्ता उस maintainer के साथ समन्वय करते हैं जिसने [agent और Actions lesson](/articles/ai-collaboration-github-agents-actions/) पूरा किया है।

**Connector-विहीन आधार:** GitHub स्वयं खोलें और केवल synthetic excerpts दें। किसी chat subscription सुविधा को मानकर न चलें। Provider स्वीकृत न हो तो उन्हीं records के साथ manually draft करें।

**पूरा होने का परिणाम:** fixed source revisions, proposed wording, प्रभावित files, exclusions और unresolved questions वाला एक Issue या PR hand off करें।

## Source packet पढ़ें

1. **`main` पर MAP-01 खोलें**, फिर POL-01, REQ-17 और RUN-04 खोजें।
2. **हर source पढ़ें** और browser की commit view से उसकी commit revision दर्ज करें।
3. **Relevant synthetic sections कॉपी करें** और filenames, revisions, scope तथा exceptions जोड़ें।
4. **Packet को snapshot-based label करें** जब तक maintainer publication से पहले उसे current sources से compare न कर ले।

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Actual sandbox revisions को निजी रूप से attach करें।** Template में पूरा evidence नहीं है। Publication की recommendation देने से पहले assistant से missing records पहचानने को कहें।

**Live source पढ़ने से पहले भरा गया synthetic packet:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs checks
```

**यह packet एक complete draft request है।** Missing-evidence line जानबूझकर रखी गई है। Publication माँगने से पहले supplied lab baseline को live sandbox revisions से बदलें।

## Issue खोलें

**Issues, New issue चुनें** और title **`PROP-042: propose thirty-day synthetic retention`** रखें। यह description paste करें और source packet attach करें।

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Chat से proposal को packet के साथ compare करने को कहें**, assumptions की list बनाने और owner questions का draft तैयार करने को कहें। उसका draft Issue में save करें। उससे change approve या publish करने को न कहें और chat thread को decision register न मानें।

## Browser edits submit करें

1. **Repository का Code tab खोलें।** File list के ऊपर branch menu चुनें, **`main`** confirm करें, **`proposal-042`** लिखें और **Create branch: proposal-042 from main** चुनें। Branch creation उपलब्ध न हो तो approved fork या नीचे दिए Issue route का उपयोग करें।
2. File खोलने से पहले **branch menu में `proposal-042` confirm करें।** File और pencil icon चुनकर edit करें। GitHub web editor protected branch edit नहीं करता।
3. **Requirement को** thirty days और revision 2 में बदलें। हर बाकी edit से पहले branch menu फिर खोलें। Configuration और runbook को उसी branch पर edit करें।
4. **`proposal.json` को** to_days 30, from_days 7 और base_revision 1 के साथ edit करें।
5. **Markdown preview करें** और JSON punctuation जाँचें। हर browser edit को **`proposal-042`** पर commit करें।
6. **Pull requests, फिर New pull request खोलें।** **`proposal-042`** की तुलना **`main`** से करें, चारों changed files जाँचें और Issue का reference देने वाली PR बनाएँ। Maintainer से protected base का fresh manifest attach करने और consistency check चलाने को कहें।
7. **Proposal की final revision पर owner reviews माँगें।** Review और read-back सफल होने तक delivery को पूरा न मानें।

**Navigation record:** repository name, Issue number, proposal branch, changed-file paths, PR number, check-run name, reviewed revision और final `main` commit लिखें। इन्हें फिर खोजने के लिए repository के Issues, Code, Pull requests, Actions और PR Checks/Reviews views का उपयोग करें। GitHub कोई control स्थानांतरित करे तो screenshot से अनुमान न लगाएँ। Number या commit ID से वही record खोजें। Record URLs और observed status वाला private evidence note export करें। Authorized team के बाहर note साझा करने से पहले account names, email addresses, tokens, tenant identifiers और unrelated repository data हटाएँ। Unredacted evidence को approved private location में रखें।

**GitHub branch और fork contribution routes document करता है।** Repository write access न रखने वाला contributor approved fork या Issue route का उपयोग करता है। Fork original repository को publication access नहीं देता।

## Worked diff का निरीक्षण करें

| File | Baseline | Candidate |
|---|---|---|
| **Requirement** | Revision 1, seven days | Revision 2, thirty days |
| **Configuration** | Seven days | Thirty days |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Proposal** | From 7, to 7 | From 7, to 30, base 1 |
| **Manifest** | Not captured | Hashes of protected pre-change sources |

**Manifest base का वर्णन करता है**, proposed thirty-day wording का नहीं। Candidate requirement को hash करके उसे baseline evidence कहना trusted base mismatch पैदा करता है।

## Verify और handoff करें

**Positive test:** owner review और successful checks के बाद maintainer merge करता है। **`main`** पर resulting files खोलें और agreement confirm करें। Resulting commit और read-back को Issue में attach करें। यह committed configuration साबित करता है, runtime deletion behavior नहीं।

**Negative test:** chat से proposal approve या publish करने को कहें। Expected policy behavior draft-only response है। अलग से contributor के रूप में direct publication आज़माएँ और unchanged source revision के साथ platform denial record करें। Behavioral और access-control tests को अलग रखें।

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Map और handoff के साथ नई session शुरू करें।** Fresh source read या browser evidence के लिए explicit request आवश्यक करें। Session को previous assistant summary दोहराने के बजाय source records से value reconstruct करनी चाहिए।

## Context खोए बिना draft करें

**Browser contributor को भी complete question चाहिए।** “Retention को thirty days करें” current authority, scope, review state और affected records नहीं बताता। Chat को source packet और drafting instruction दें। Record उपलब्ध न हो तो remembered text भरने के बजाय maintainer से authorized evidence माँगें।

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Copy करने से पहले answer inspect करें।** देखें कि scope बदला, commit invent हुआ या approval को complete बताया गया। Unsupported claims हटाएँ और unresolved questions Issue में रखें। Chat proposal लिखने में मदद कर रहा है। वह उन systems का evidence नहीं देता जिन्हें उसने पढ़ा नहीं।

## Contribution route चुनें

| Situation | Route | Deliverable |
|---|---|---|
| **Read access only** | Fixed proposed wording वाला Issue | Maintainer-ready change request |
| **Approved branch access** | One proposal branch पर browser edits | Related file changes वाली PR |
| **Approved fork route** | Fork और upstream PR | Upstream review की प्रतीक्षा करता candidate |
| **No source access** | Stop और authorized evidence माँगें | Explicitly blocked task |

**Issue route complete contribution है**, failed coding exercise नहीं। आप intended change, evidence, scope और review questions देते हैं। Maintainer patch और manifest देता है। फिर patch को request के साथ agreement के लिए inspect करें।

| Route | Contributor completion check | Maintainer handoff |
|---|---|---|
| **Issue only** | Issue में verified source packet, fixed proposed wording, exclusions और open questions हैं | Maintainer branch बनाता है, checks चलाता है और PR link करता है |
| **PR** | One branch में सभी affected files हैं, PR diff proposal से मिलता है और reviewers को final revision मिली है | Maintainer checks चलाता है, owner review लेता है, merge करता है और read-back record करता है |

**Browser edits में proposal branch पर रहें।** First edit branch बनाने के बाद बाकी हर file को उसी branch selector से फिर खोलें। अंत में PR diff जाँचें। चार unrelated branches चार incomplete changes बनाते हैं, एक reviewable package नहीं।

## Proposed wording inspect करें

**Illustrative weak wording:** “Exports now remain available for thirty days.” यह delivery को complete बताता है और synthetic scope हटाता है। Review pending होने पर proposal statement का उपयोग करें।

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**हर affected file की तुलना इस wording से करें।** Candidate में requirement revision आगे बढ़ती है। Configuration thirty तक पहुँचता है। Runbook की पहली line lab limitation रखते हुए thirty तक पहुँचती है। Proposal seven को prior value और revision one को base बताता रहता है।

**Differences पर explanation माँगें, unfamiliar controls को repair न करें।** Maintainer patch protection को कमजोर करे या policy हटाए तो explanation और separate review माँगें। Workflow की हर line समझे बिना भी out-of-scope change पहचाना जा सकता है।

## Review feedback का जवाब दें

**Illustrative review:** Operations ऐसी sentence माँगता है जो बताए कि configuration rollback deleted files restore नहीं करता। उसी branch पर draft update करें और reviewers को amended scope बताएँ। Final review amended proposal पर हो, पुराने chat copy पर नहीं।

| Review comment | Contributor action |
|---|---|
| **Missing exclusion** | Wording restore करें और intent review माँगें |
| **Stale source revision** | New authorized packet लें और reconcile करें |
| **Missing manifest** | Maintainer से protected base capture करने को कहें |
| **Unrelated control change** | Review से पहले अलग करें या हटाएँ |
| **Untested runtime claim** | Precise lab limitation से बदलें |

**Questions का उत्तर मिलने तक उन्हें visible रखें।** Underlying issue ठीक किए बिना comment resolve करने से useful signal हट जाता है। Response में amendment या evidence link करें ताकि दूसरा reviewer पूरी conversation पढ़े बिना decision follow कर सके।

## Browser completion check

**ऐसा Issue या PR deliver करें जिसे दूसरा maintainer guessing के बिना execute कर सके।** इसमें source packet, proposed wording, affected records, exclusions, owner roles और unresolved questions हों। Publication के बाद read-back capture करें और उसे original proposal से अलग रखें।

**Self-check:** Package ऐसे व्यक्ति को दें जो आपकी chat नहीं जानता। उससे requested, approved और published values अलग करने को कहें। Merge से पहले वह thirty को delivered बताए तो package labels ठीक करें। यही discipline workplace track में रखें।

| Review gate | Pass condition |
|---|---|
| **Source revisions** | हर claimed commit या page version sandbox में खुलता है। Unknown revisions Missing रहती हैं। |
| **Exclusions** | Production data, backups और legal holds proposal से बाहर रहते हैं। |
| **Questions** | Owner या source के unresolved questions Issue या PR में दिखाई देते हैं। |
| **Approval freshness** | Reviews proposal की final revision को नाम से बताते हैं। Earlier approval later edits को cover नहीं करती। |

**कोई भी failed gate publication को pending रखता है।** Issue-only contributors result maintainer को hand off करते हैं। PR contributors repairs के बाद फिर review माँगते हैं।

## Troubleshooting और rollback

**Edit permission नहीं:** Issue या approved fork उपयोग करें। **Invented commit reference:** verified evidence से बदलें और draft फिर review कराएँ। **Approval edits से पहले की है:** fresh approval माँगें।

**Rollback:** Unmerged PR को evidence सुरक्षित रखते हुए close करें। Merged content के लिए maintainer से protected revert proposal माँगें। Successful recovery का दिखावा करने के लिए baseline न बदलें।

## Exercise और self-check

**Requirement record नए assistant से छिपाएँ** और publication recommendation माँगें।

**Expected reasoning:** वह authoritative evidence माँगता है या response को snapshot-based label करता है। Fresh read सफल होने तक publication blocked रहती है।

## मुख्य संदर्भ

- **Browser steps:** [Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)।
- **Review boundary:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)।

## अगले कदम

**[Confluence और Jira Setup](/articles/ai-collaboration-confluence-jira-setup/)** के साथ जारी रखें और workplace systems में operating model दोहराएँ।
