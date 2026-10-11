---
title: "GitHub AI सहयोग: रिपॉजिटरी और समीक्षा की सीमाएँ"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "GitHub-केंद्रित स्रोत मानचित्र बनाएँ, फ़ाइल स्वामित्व तय करें और समीक्षित AI योगदान के लिए सुरक्षित प्रकाशन सीमा स्थापित करें।"
genre: ["कृत्रिम बुद्धिमत्ता", "टीम सहयोग", "सॉफ्टवेयर इंजीनियरिंग"]
tags: ["AI सहयोग पाठ्यक्रम", "GitHub रिपॉजिटरी", "ब्रांच सुरक्षा", "CODEOWNERS", "स्रोत मानचित्र", "पुल रिक्वेस्ट समीक्षा", "प्रकाशन नियंत्रण"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "साइबर सुरक्षा कार्यक्षेत्र में साझा प्रोजेक्ट कार्य की समीक्षा करते पेशेवरों का चित्रण"
coverCaption: ""
---

[AI सहयोग पाठ्यक्रम पर लौटें](/ai-collaboration-course-start/)

**चार्टर की स्वीकृति के बाद मेंटेनर GitHub-केंद्रित प्रकाशन सीमा बनाता है।** आवश्यकताएँ, कॉन्फ़िगरेशन, नीति और रनबुक एक अस्थायी रिपॉजिटरी में रहते हैं। योगदानकर्ता Issues और पुल रिक्वेस्ट के माध्यम से प्रस्ताव देते हैं। आप तय करते हैं कि स्वीकृत तथ्य कहाँ रहते हैं और एजेंट जोड़ने से पहले असमीक्षित बदलाव रोकते हैं।

## मुख्य बातें

- **सुरक्षित `main`** प्रकाशन सीमा है।
- **Issues** प्रस्तावित काम इकट्ठा करते हैं, नीति को स्वीकृति नहीं देते।
- **CODEOWNERS** योग्य फ़ाइल समीक्षकों को नियुक्त करता है।
- **अलग उपयोगकर्ता** समीक्षा और अस्वीकृति नियंत्रण दिखाते हैं।

## शुरू करने से पहले

**पूर्वापेक्षाएँ:** [पायलट आधार](/articles/ai-collaboration-pilot-foundation/), निकाली गई लैब, रिपॉजिटरी एडमिनिस्ट्रेटर और अलग उत्पाद तथा संचालन समीक्षक। **अनुमानित समय:** 60 मिनट। **कठिनाई:** मध्यम।

**प्लान सीमा:** GitHub Free पर सार्वजनिक रिपॉजिटरी और Pro, Team या Enterprise पर निजी रिपॉजिटरी के लिए संरक्षित ब्रांच दस्तावेज़ित करता है। सार्वजनिक रिपॉजिटरी केवल सिंथेटिक सामग्री के लिए इस्तेमाल करें। प्रवर्तन पर निर्भर करने से पहले संरक्षित ब्रांच संदर्भ में दृश्यता और प्लान जाँचें।

**पूरा होने का परिणाम:** आपके पास सुरक्षित प्रकाशन ब्रांच, फ़ाइल स्वामी, स्रोत मानचित्र और साक्ष्य के रूप में दर्ज अस्वीकृति परीक्षण होगा।

## रिपॉजिटरी बनाएँ

1. README और डिफ़ॉल्ट ब्रांच **`main`** के साथ **`export-service-lab` बनाएँ**।
2. **निकाली गई लैब कॉपी करें** और **`check.py`**, **`test_check.py`** तथा **`baseline/`** सुरक्षित रखें। बेसलाइन रिकॉर्ड फ़ाइलों को प्रारंभिक रिकॉर्ड के रूप में रूट में कॉपी करें।
3. फाउंडेशन रजिस्टर का उपयोग करके **`docs/project-map.md` बनाएँ**। स्वीकृत POL-01 के साथ **`docs/policy.md`** जोड़ें।
4. चार्टर स्वीकृति, भूमिकाओं, बेसलाइन निर्णय और स्थिति के साथ **`docs/decisions/DEC-12.md` बनाएँ**।
5. एडमिनिस्ट्रेटर के रूप में **बूटस्ट्रैप कमिट करें**। इस शुरुआती अपवाद को दर्ज करें। अगले योगदान से पहले सुरक्षा सक्षम करें।

**Git Bash, macOS Terminal या Linux शेल के लिए स्थानीय बूटस्ट्रैप मार्ग:** ब्राउज़र में GitHub में साइन इन करें, नई रिपॉजिटरी खोलें, **Code** चुनें और उसका HTTPS clone URL कॉपी करें। अस्थायी कार्य निर्देशिका में नीचे दिए कमांड चलाएँ। दो प्लेसहोल्डर पथों को URL और डाउनलोड की गई लैब ZIP के पथ से बदलें। URL में टोकन न डालें।

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

Clone कमांड को रिपॉजिटरी निर्देशिका का नाम देना चाहिए। यदि `unzip` उपलब्ध नहीं है, तो फ़ाइल मैनेजर से ZIP निकालें और उसकी सामग्री इस checkout में कॉपी करें, रिपॉजिटरी README को सुरक्षित रखें। फाउंडेशन पैकेट से `docs/project-map.md`, `docs/policy.md` और `docs/decisions/DEC-12.md` टेक्स्ट एडिटर में सहेजें। फिर चलाएँ:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git को नई commit ID और फिर `main` पर सफल push दिखाना चाहिए। अंतिम short status खाली होना चाहिए। नई ब्राउज़र view में GitHub रिपॉजिटरी खोलें और पुष्टि करें कि फ़ाइलें तथा commit ID `main` पर दिखते हैं। commit URL को बूटस्ट्रैप साक्ष्य के रूप में सहेजें। यदि Git लेखक पहचान माँगे, तो course hub का setup bridge अपनाएँ। प्रमाणीकरण विफल होने पर GitHub का समर्थित credential flow इस्तेमाल करें और वही push फिर चलाएँ। यदि branch या remote गलत है, तो अगली write से पहले `git branch --show-current` और `git remote -v` जाँचें। यदि सुरक्षा पहले से सक्रिय होने के कारण push अस्वीकार हो, तो नियम को दरकिनार करने के बजाय proposal branch और PR खोलें। नीचे दिया browser-only मार्ग maintainer के लिए उपलब्ध है।

| रिकॉर्ड | स्थान | स्वामी |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | नीति स्वामी |
| **REQ-17** | `requirement.json` | उत्पाद स्वामी |
| **RUN-04** | `runbook.md` | संचालन स्वामी |
| **व्यवहार** | `config.json` | मेंटेनर |
| **निर्णय** | `docs/decisions/` | प्रोजेक्ट लीड |

**मानचित्र मानों की कॉपी करने के बजाय स्थानों को जोड़ता है।** README को सेटअप और मानचित्र पर केंद्रित रखें। संरक्षण आवश्यकताओं की पुनरावृत्ति एक ही रिपॉजिटरी में भी drift पैदा करती है।

## फ़ाइल स्वामी नियुक्त करें

**`.github/CODEOWNERS` बनाएँ** और वास्तविक sandbox handles का उपयोग करें। शुरुआती **`@`** के बिना handles दर्ज करें। खाते की पहचान निजी लैब में रखें, सार्वजनिक exercise साक्ष्य में नहीं।

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

GitHub द्वारा पहचान के लिए स्वामियों को write access चाहिए। ब्राउज़र में CODEOWNERS फ़ाइल की त्रुटियाँ जाँचें। स्वामित्व फ़ाइलों और workflow definitions को सामान्य सामग्री के साथ सुरक्षित करें।

**एक पंक्ति में कई नामों के लिए सभी सूचीबद्ध स्वामियों की स्वीकृति आवश्यक नहीं है।** GitHub संबंधित path के लिए एक योग्य स्वामी की स्वीकृति स्वीकार करता है। requirement और runbook paths के लिए अलग designated owners रखें। पायलट में अंतिम proposal से जुड़े product-owner और operations-owner attestations भी आवश्यक हैं।

## प्रकाशन सुरक्षित करें

1. **Settings, Branches खोलें** और **`main`** के लिए branch protection rule जोड़ें। इस exercise में rulesets के साथ मिलाने के बजाय branch-protection मार्ग लगातार इस्तेमाल करें।
2. **Pull request**, दो approving reviews और code-owner review आवश्यक करें।
3. नए commits के बाद **stale approvals हटाएँ** और conversation resolution आवश्यक करें।
4. **Do not allow bypassing the above settings सक्षम करें।** force pushes और deletion बंद रखें।
5. अगले module में पहले run के बाद **consistency check जोड़ें**। merge से पहले branches को up to date आवश्यक करें।

**दो approvals संख्या लागू करते हैं, business-role membership नहीं।** CODEOWNERS path-based owner coverage जोड़ता है। Maintainer दो role attestations भी जाँचता है। इस procedural control को स्पष्ट रूप से दर्ज करें, इसे automated two-role enforcement न कहें।

**Administrators configuration प्रबंधित करते रहते हैं।** परीक्षण से पहले और बाद में rule capture करें। contributor denial दिखाने के लिए agent को administrator access या privileged token न दें।

## सीमा सत्यापित करें

| प्रयास | अपेक्षित परिणाम |
|---|---|
| **Contributor branch submit करता है** | Proposal permitted |
| **Contributor सीधे publish करता है** | Protected publication denied |
| **एक reviewer approve करता है** | Review threshold से merge blocked |
| **Review के बाद नया commit आता है** | Fresh approval required |
| **Sensitive file में owner coverage नहीं है** | Publication से पहले repair |

**मार्ग की जाँच के लिए contributor का browser session इस्तेमाल करें।** GitHub web editor protected **`main`** branch को edit नहीं करता। Branch बनाने का prompt supported browser route दिखाता है। यह साबित नहीं करता कि server ने direct push reject किया। Platform-denial evidence के लिए approved local Git access वाले contributor से protected **`main`** पर harmless direct push करवाएँ और server response रखें। Local access न होने पर इस denial test को Blocked चिह्नित करें।

**Denial के बाद `main` पढ़ें** और पुष्टि करें कि revision बदली नहीं। actor role, attempted action, result और source revision दर्ज करें। Assistant का publish न करने का वादा behavioral evidence है, platform-permission test नहीं।

**Direct-push test के लिए contributor का अपना authenticated local clone इस्तेमाल करें।** Maintainer token गलत identity का परीक्षण करेगा। यह illustrative response रखने योग्य server evidence का प्रकार दिखाता है। Exact wording repository rules के अनुसार बदलती है।

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**यदि local Git authentication उपलब्ध नहीं है, तो server-side denial को Blocked चिह्नित करें।** Browser branch prompt को route evidence रखें और maintainer से अलग contributor test की व्यवस्था करने को कहें। Route prompt को rejected direct push न मानें।

## उपयोगी स्रोत मानचित्र बनाएँ

**Source map routing document है**, दूसरा requirements document नहीं। Chat से आने वाले व्यक्ति को competing summaries में चुनाव किए बिना current intent, implemented behavior और operational instructions मिलनी चाहिए।

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Current retention value हर map entry में न रखें।** “Seven days” वाली map PROP-042 के बाद synchronize करने के लिए एक और value बन जाती है। Map में stable identifiers और locations रखें और value authoritative record से पढ़ें।

**Map changes को routing changes की तरह सुरक्षित करें।** REQ-17 को draft file पर redirect करना source selection बदलता है, चाहे approved requirement unchanged रहे। Map बदलने पर destination, owner और authority scope review करें।

## Baseline और candidate अलग करें

**Repository root में active lab records रहते हैं।** Download किया गया **`baseline/`** directory teaching fixture है। हर बाद की PR के लिए यह अपने आप protected baseline नहीं है। Reviewed work **`main`** तक पहुँचने पर protected root records अगली proposal का base तय करते हैं।

| स्थान | उद्देश्य | PROP-042 के दौरान edit करें? |
|---|---|---|
| **Root requirement/config/runbook** | Branch पर proposed active records | हाँ, reviewed changes के माध्यम से |
| **`baseline/`** | Original offline exercise fixture | नहीं |
| **Detached trusted worktree** | Captured protected root records | नहीं |
| **`context.json`** | Captured base bytes का evidence | Reconciliation के बाद regenerate |

**Control changes और retention changes अलग रखें।** पहले checker और review rules bootstrap करें। फिर seven-to-thirty-day change propose करें। Policy, workflow और value rewrite को मिलाने से repaired controls और bypassed controls में अंतर करना कठिन होता है।

## पूरा बदलाव review करें

**PR description स्वीकार करने से पहले Files changed खोलें।** Description author intent बताती है। Diff submitted change दिखाता है। PROP-042 के लिए requirement revision, scope exclusions, configuration, runbook, proposal base और manifest evidence देखें।

1. **Product review:** thirty-day intent और unchanged exclusions की पुष्टि करें।
2. **Operations review:** runbook proposed configuration से मेल खाता है और runtime limitation रखता है, इसकी पुष्टि करें।
3. **Maintainer review:** JSON, source capture, check results और unrelated edits देखें।
4. **Control review:** map, policy, CODEOWNERS या workflow change अलग से देखें।

**Green check unrelated deletion नहीं समझाता।** Branch retention बदलते समय policy document हटाती है, तो separate proposal या specific owner review माँगें। Scope सीमित रखने से review object समझने योग्य रहता है।

## Denial test diagnose करें

**हर evidence row में एक attempted action रखें।** “Contributor failed” अस्पष्ट है। User के पास ordinary repository write access न हो, browser limitation मिले या intended branch rule hit हो। ये observations अलग boundaries स्थापित करते हैं।

| Observation | Interpretation | Follow-up |
|---|---|---|
| **कोई branch create नहीं कर सकता** | Contribution access अनुपस्थित है | Approved Issue/fork route इस्तेमाल करें |
| **Branch बनाता है, main पर publish नहीं कर सकता** | Tested publication route restricted है | Unchanged main revision capture करें |
| **One review पर merge blocked है** | Review count tested PR पर लागू है | Role-specific evidence जोड़ें |
| **Admin rule के बावजूद publish करता है** | Tested identity boundary bypass करती है | Bypass settings और grants देखें |

**Shared course evidence में account details उजागर किए बिना role और action दर्ज करें।** Native actor records reviewer के लिए privately उपलब्ध रखें। Rule configuration, attempted operation, denial और resulting protected revision साथ capture करें।

## Repository completion check

**ऐसी repository दें जिसे दूसरा contributor independently navigate कर सके।** README map की ओर point करता है, map authoritative records तक पहुँचता है, owner coverage sensitive paths शामिल करती है और protection **`main`** पर लागू होती है। एक permitted proposal और एक denied publication attempt रखें।

**केवल settings से enforcement claim न करें।** Settings intended configuration स्थापित करती हैं। Sandbox attempt किसी particular role और route के observed behavior को स्थापित करता है। दोनों को agent और Actions lesson में ले जाएँ।

## Troubleshooting और rollback

**Owner request missing:** write access और base-branch path coverage confirm करें। **Protection absent:** plan और visibility verify करें। **Merge enabled:** rule target, bypass configuration और review count देखें।

**Rollback:** unmerged proposals बंद करें और lab automation deactivate करें। Merged lab content को दूसरी reviewed PR से revert करें। Disposable repository delete करने से पहले evidence रखें। Failing test पूरा करने के लिए protection कमजोर न करें।

## Exercise और self-check

Contributor के रूप में **`docs/policy.md` में edit propose करें**। तय करें कि maintainer approval alone policy-owner approval स्थापित करती है या नहीं।

**Expected reasoning:** review count अकेले authority स्थापित नहीं करता। Path को policy-owner coverage और current role review चाहिए। Unenforced role-specific requirements को procedural controls के रूप में सूचीबद्ध करें।

## Primary references

- **Plan और review controls:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)।
- **Owner eligibility:** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)।
- **Browser contribution:** [Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)।

## अगला कदम

Executable checks से source evidence जोड़ने के लिए **[Agent Adapters and Actions](/articles/ai-collaboration-github-agents-actions/)** के साथ आगे बढ़ें।
