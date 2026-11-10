---
title: "GitHub AI সহযোগিতা: রিপোজিটরি ও রিভিউ সীমা"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "GitHub-ভিত্তিক সোর্স ম্যাপ তৈরি করুন, ফাইলের মালিক নির্ধারণ করুন এবং পর্যালোচিত AI অবদানের জন্য সুরক্ষিত প্রকাশনা সীমা তৈরি করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "দলগত সহযোগিতা", "সফটওয়্যার প্রকৌশল"]
tags: ["AI সহযোগিতা কোর্স", "GitHub রিপোজিটরি", "ব্রাঞ্চ সুরক্ষা", "CODEOWNERS", "সোর্স ম্যাপ", "pull request রিভিউ", "প্রকাশনা নিয়ন্ত্রণ"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "সাইবার নিরাপত্তা কর্মক্ষেত্রে যৌথ প্রকল্পের কাজ পর্যালোচনা করা পেশাজীবীদের চিত্র"
coverCaption: ""
---

[AI সহযোগিতা কোর্সে ফিরে যান](/ai-collaboration-course-start/)

**চার্টার অনুমোদনের পরে রক্ষণাবেক্ষণকারী GitHub-ভিত্তিক প্রকাশনা সীমা তৈরি করেন।** প্রয়োজনীয়তা, কনফিগারেশন, নীতি এবং রানবুক একটি অস্থায়ী রিপোজিটরিতে থাকে। অবদানকারীরা Issues এবং pull request-এর মাধ্যমে প্রস্তাব দেয়। অনুমোদিত তথ্য কোথায় থাকবে তা নির্ধারণ করুন এবং এজেন্ট যুক্ত করার আগে অপর্যালোচিত পরিবর্তন আটকে দিন।

## মূল বিষয়

- **সুরক্ষিত `main`** প্রকাশনার সীমা।
- **Issues** প্রস্তাবিত কাজ সংগ্রহ করে, নীতি অনুমোদন করে না।
- **CODEOWNERS** যোগ্য ফাইল রিভিউয়ার নির্ধারণ করে।
- **আলাদা ব্যবহারকারী** রিভিউ এবং প্রত্যাখ্যান নিয়ন্ত্রণ দেখায়।

## শুরু করার আগে

**পূর্বশর্ত:** [পাইলট ভিত্তি](/articles/ai-collaboration-pilot-foundation/), নিষ্কাশিত ল্যাব, রিপোজিটরি প্রশাসক এবং আলাদা পণ্য ও অপারেশন রিভিউয়ার। **আনুমানিক সময়:** ৬০ মিনিট। **কঠিনতা:** মাঝারি।

**প্ল্যান সীমা:** GitHub Free-এ public এবং Pro, Team বা Enterprise-এ private রিপোজিটরির জন্য protected branch নথিভুক্ত করে। public রিপোজিটরি শুধু synthetic বিষয়বস্তুর জন্য ব্যবহার করুন। enforcement-এর উপর নির্ভর করার আগে protected branch রেফারেন্স অনুযায়ী visibility এবং plan যাচাই করুন।

**সমাপ্তির ফল:** protected publication branch, file owner, source map এবং প্রমাণ হিসেবে নথিভুক্ত denial test নিয়ে কাজ শেষ হবে।

## রিপোজিটরি তৈরি করুন

1. README এবং default branch **`main`** সহ **`export-service-lab`** তৈরি করুন।
2. **নিষ্কাশিত ল্যাব কপি করুন** রিপোজিটরির root-এ এবং **`check.py`**, **`test_check.py`** ও **`baseline/`** রাখুন। baseline record file-গুলো initial record হিসেবে root-এ কপি করুন।
3. foundation register ব্যবহার করে **`docs/project-map.md`** তৈরি করুন। অনুমোদিত POL-01 সহ **`docs/policy.md`** যোগ করুন।
4. charter approval, role, baseline decision এবং status সহ **`docs/decisions/DEC-12.md`** তৈরি করুন।
5. administrator হিসেবে **bootstrap commit** করুন। এই initial exception নথিভুক্ত করুন। পরবর্তী contribution-এর আগে protection চালু করুন।

**Git Bash, macOS Terminal বা Linux shell-এর স্থানীয় bootstrap পথ:** browser-এ GitHub-এ sign in করুন, নতুন repository খুলুন, **Code** নির্বাচন করুন এবং HTTPS clone URL কপি করুন। একটি disposable working directory-তে নিচের command চালান। দুটি placeholder path-এর বদলে URL এবং downloaded lab ZIP path দিন। URL-এ token দেবেন না।

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

clone command-এ repository directory-এর নাম থাকতে হবে। `unzip` না থাকলে file manager দিয়ে ZIP extract করে এই checkout-এ copy করুন এবং repository README অপরিবর্তিত রাখুন। `git status --short`-এ copied record, checker, test এবং `baseline/` নতুন file হিসেবে দেখা উচিত। text editor দিয়ে foundation packet-এর `docs/project-map.md`, `docs/policy.md` এবং `docs/decisions/DEC-12.md` সংরক্ষণ করুন। তারপর চালান:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git নতুন commit ID এবং পরে `main`-এ সফল push দেখাবে। শেষের short status ফাঁকা থাকবে। নতুন browser view-তে GitHub repository খুলে `main`-এ file এবং commit ID দেখা যাচ্ছে কিনা নিশ্চিত করুন। commit URL bootstrap evidence হিসেবে সংরক্ষণ করুন। Git author identity চাইলে course hub-এর setup bridge অনুসরণ করুন। Authentication ব্যর্থ হলে GitHub-এর supported credential flow ব্যবহার করে একই push আবার চালান। branch বা remote ভুল হলে থামুন এবং লেখার আগে `git branch --show-current` ও `git remote -v` দেখুন। protection আগে চালু থাকায় push প্রত্যাখ্যাত হলে rule এড়িয়ে না গিয়ে proposal branch এবং PR খুলুন। browser-only route maintainer-এর মাধ্যমে থাকবে।

| রেকর্ড | অবস্থান | মালিক |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | নীতি মালিক |
| **REQ-17** | `requirement.json` | পণ্য মালিক |
| **RUN-04** | `runbook.md` | অপারেশন মালিক |
| **আচরণ** | `config.json` | রক্ষণাবেক্ষণকারী |
| **সিদ্ধান্ত** | `docs/decisions/` | প্রকল্প নেতা |

**ম্যাপ value copy না করে location link করে।** README-কে setup এবং map-এ সীমাবদ্ধ রাখুন। retention requirement বারবার লিখলে এক repository-র মধ্যেও drift তৈরি হয়।

## ফাইলের মালিক নির্ধারণ করুন

**বাস্তব sandbox handle দিয়ে `.github/CODEOWNERS`** local-এ তৈরি করুন। শুরুর **`@`** ছাড়া handle লিখুন। account identity private lab-এ রাখুন, public exercise evidence-এ নয়।

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

**GitHub-এ চিনতে file owner-এর write access দরকার।** browser-এ CODEOWNERS file পরীক্ষা করুন। ownership file এবং workflow definition-ও সাধারণ content-এর সঙ্গে protect করুন।

**এক লাইনে একাধিক নাম থাকলেও সবার approval দরকার হয় না।** GitHub matching path-এর একজন eligible owner-এর approval গ্রহণ করে। requirement এবং runbook path-এর জন্য আলাদা designated owner ব্যবহার করুন। pilot-এর final proposal-এ product-owner এবং operations-owner attestation-ও দরকার।

## প্রকাশনা সুরক্ষিত করুন

1. **Settings, Branches** খুলে **`main`**-এর জন্য branch protection rule যোগ করুন। এই exercise-এ ruleset-এর সঙ্গে না মিশিয়ে branch-protection route ব্যবহার করুন।
2. **pull request**, দুইটি approving review এবং code owner review বাধ্যতামূলক করুন।
3. নতুন commit-এর পরে **পুরোনো approval বাতিল** করুন এবং conversation resolution বাধ্যতামূলক করুন।
4. **Do not allow bypassing the above settings** চালু করুন। force push এবং deletion বন্ধ রাখুন।
5. পরের module-এ প্রথম run-এর পরে **consistency check** যোগ করুন। merge-এর আগে branch up to date থাকা বাধ্যতামূলক করুন।

**দুইটি approval সংখ্যা নিশ্চিত করে, business role নয়।** CODEOWNERS path-based owner coverage যোগ করে। Maintainer দুই role attestation-ও পরীক্ষা করে। এটিকে automated two-role enforcement না বলে procedural control হিসেবে নথিভুক্ত করুন।

**Administrator-রাই configuration পরিচালনা করেন।** test-এর আগে এবং পরে rule capture করুন। contributor denial দেখানোর জন্য agent-কে administrator access বা privileged token দেবেন না।

## সীমা যাচাই করুন

| চেষ্টা | প্রত্যাশিত ফল |
|---|---|
| **Contributor branch জমা দেয়** | Proposal অনুমোদিত |
| **Contributor সরাসরি publish করে** | Protected publication প্রত্যাখ্যাত |
| **একজন reviewer approval দেয়** | Review threshold-এ merge আটকে যায় |
| **Review-এর পরে নতুন commit আসে** | নতুন approval দরকার |
| **Sensitive file-এর owner coverage নেই** | Publication-এর আগে মেরামত |

**Route পরীক্ষা করতে contributor-এর browser session ব্যবহার করুন।** GitHub web editor protected **`main`** edit করে না। Branch তৈরির prompt supported browser route দেখায়। এটি server direct push প্রত্যাখ্যান করেছে এমন প্রমাণ নয়। Platform-denial evidence-এর জন্য approved local Git access থাকা contributor-কে protected **`main`**-এ harmless direct push চেষ্টা করান এবং server response রাখুন। local access না থাকলে denial test-কে Blocked হিসেবে চিহ্নিত করুন।

**Denial-এর পরে `main` পড়ে** revision বদলায়নি নিশ্চিত করুন। actor role, attempted action, result এবং source revision লিখুন। assistant publish না করার প্রতিশ্রুতি behavioral evidence, platform-permission test নয়।

**Direct-push test-এ contributor-এর নিজের authenticated local clone ব্যবহার করুন।** Maintainer token ভুল identity পরীক্ষা করবে। নিচের illustrative response-এ রাখার মতো server evidence-এর ধরন দেখানো হয়েছে। Exact wording repository rule অনুযায়ী বদলায়।

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Local Git authentication না থাকলে server-side denial-কে Blocked করুন।** Browser branch prompt route evidence হিসেবে রাখুন এবং maintainer-কে আলাদা contributor test আয়োজন করতে বলুন। route prompt-কে rejected direct push হিসেবে score করবেন না।

## কার্যকর source map তৈরি করুন

**Source map হলো routing document**, দ্বিতীয় requirements document নয়। chat থেকে আসা ব্যক্তি যেন competing summary বেছে না নিয়ে current intent, implemented behavior এবং operational instruction খুঁজে পায়।

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

**প্রতিটি মানচিত্র-এন্ট্রিতে বর্তমান সংরক্ষণ-মেয়াদ রাখবেন না।** “সাত দিন” রাখলে PROP-042-এর পরে মানচিত্রে আরেকটি মান সমন্বয় করতে হবে। মানচিত্রে স্থায়ী শনাক্তকারী ও অবস্থান রাখুন, আর মানটি কর্তৃত্বপূর্ণ রেকর্ড থেকে পড়ুন।

**মানচিত্রের পরিবর্তনকে রাউটিং পরিবর্তন হিসেবে সুরক্ষিত করুন।** REQ-17-কে খসড়া ফাইলে পাঠালে অনুমোদিত requirement অপরিবর্তিত থাকলেও উৎস নির্বাচন বদলে যায়। মানচিত্র বদলালে গন্তব্য, দায়িত্বপ্রাপ্ত ব্যক্তি এবং কর্তৃত্বের পরিধি পর্যালোচনা করুন।

## বেসলাইন ও প্রস্তাবিত পরিবর্তন আলাদা করুন

**রিপোজিটরির রুটে সক্রিয় ল্যাব রেকর্ড থাকে।** ডাউনলোড করা **`baseline/`** ডিরেক্টরিটি শিক্ষামূলক নমুনা। পরবর্তী প্রতিটি PR-এর সুরক্ষিত বেসলাইন এটি স্বয়ংক্রিয়ভাবে নয়। পর্যালোচিত কাজ **`main`**-এ পৌঁছালে সুরক্ষিত রুট রেকর্ড পরবর্তী প্রস্তাবের ভিত্তি নির্ধারণ করে।

| অবস্থান | উদ্দেশ্য | PROP-042 চলাকালে সম্পাদনা করবেন? |
|---|---|---|
| **রুটের প্রয়োজনীয়তা/কনফিগারেশন/কাজের নির্দেশিকা** | শাখায় প্রস্তাবিত সক্রিয় রেকর্ড | হ্যাঁ, পর্যালোচিত পরিবর্তনের মাধ্যমে |
| **`baseline/`** | মূল অফলাইন অনুশীলনের নমুনা | না |
| **বিচ্ছিন্ন বিশ্বস্ত worktree** | রুট থেকে নেওয়া সুরক্ষিত রেকর্ডের কপি | না |
| **`context.json`** | ধারণ করা বেস বাইটের প্রমাণ | সমন্বয়ের পরে নতুন করে তৈরি করুন |

**নিয়ন্ত্রণের পরিবর্তন ও সংরক্ষণ-মেয়াদের পরিবর্তন আলাদা রাখুন।** প্রথমে checker ও পর্যালোচনার নিয়ম চালু করুন। এরপর সাত থেকে ত্রিশ দিনের পরিবর্তন প্রস্তাব করুন। নীতি, কর্মপ্রবাহ ও মান একসঙ্গে বদলালে সংশোধিত নিয়ন্ত্রণ আর এড়িয়ে যাওয়া নিয়ন্ত্রণ আলাদা করা কঠিন হয়।

## সম্পূর্ণ পরিবর্তন পর্যালোচনা করুন

**PR-এর বিবরণ গ্রহণের আগে পরিবর্তিত ফাইল খুলুন।** বিবরণে লেখকের উদ্দেশ্য থাকে। Diff জমা দেওয়া পরিবর্তন দেখায়। PROP-042-এর জন্য requirement সংস্করণ, পরিধির বর্জন, কনফিগারেশন, runbook, প্রস্তাবের ভিত্তি ও manifest-এর প্রমাণ পরীক্ষা করুন।

1. **পণ্য পর্যালোচনা:** ত্রিশ দিনের উদ্দেশ্য এবং অপরিবর্তিত বর্জন নিশ্চিত করুন।
2. **পরিচালনা পর্যালোচনা:** runbook প্রস্তাবিত কনফিগারেশনের সঙ্গে মেলে এবং runtime সীমাবদ্ধতা উল্লেখ করে কি না নিশ্চিত করুন।
3. **রক্ষণাবেক্ষণকারীর পর্যালোচনা:** JSON, উৎস ধারণ, যাচাইয়ের ফল এবং সম্পর্কহীন পরিবর্তন পরীক্ষা করুন।
4. **নিয়ন্ত্রণ পর্যালোচনা:** মানচিত্র, নীতি, CODEOWNERS বা workflow-এর পরিবর্তন আলাদাভাবে পরীক্ষা করুন।

**সবুজ check সম্পর্কহীন মোছার ব্যাখ্যা দেয় না।** শাখা থেকে নীতির নথি সরিয়ে সংরক্ষণ-মেয়াদ বদলালে আলাদা প্রস্তাব বা নির্দিষ্ট দায়িত্বপ্রাপ্ত ব্যক্তির পর্যালোচনা চান। পরিধি সীমিত রাখলে পর্যালোচনার বিষয় বোঝা সহজ হয়।

## প্রত্যাখ্যান পরীক্ষা বিশ্লেষণ করুন

**প্রতিটি প্রমাণের সারিতে একটি করে চেষ্টা করা কাজ রাখুন।** “অবদানকারী ব্যর্থ হয়েছে” কথাটি অস্পষ্ট। ব্যবহারকারীর সাধারণ রিপোজিটরি লেখার অনুমতি নাও থাকতে পারে, ব্রাউজারে সীমাবদ্ধতা দেখা দিতে পারে, অথবা নির্ধারিত branch rule প্রয়োগ হতে পারে। এসব পর্যবেক্ষণ ভিন্ন সুরক্ষা-সীমা দেখায়।

| পর্যবেক্ষণ | ব্যাখ্যা | পরবর্তী পদক্ষেপ |
|---|---|---|
| **কোনো branch তৈরি করতে পারে না** | অবদানের অনুমতি নেই | অনুমোদিত Issue/fork পথ ব্যবহার করুন |
| **branch তৈরি করে, main-এ প্রকাশ করতে পারে না** | পরীক্ষিত প্রকাশ-পথ সীমাবদ্ধ | অপরিবর্তিত main সংস্করণ ধারণ করুন |
| **একটি review থাকায় merge আটকে যায়** | পরীক্ষিত PR-এ review সংখ্যা প্রযোজ্য | ভূমিকা-নির্দিষ্ট প্রমাণ যোগ করুন |
| **নিয়ম থাকা সত্ত্বেও administrator প্রকাশ করে** | পরীক্ষিত পরিচয় সুরক্ষা-সীমা এড়ায় | bypass সেটিং ও অনুমতি পরীক্ষা করুন |

**সবার সঙ্গে ভাগ করা কোর্স-প্রমাণে অ্যাকাউন্টের বিবরণ প্রকাশ না করে ভূমিকা ও কাজ লিখুন।** পর্যালোচকের জন্য মূল actor record ব্যক্তিগতভাবে রাখুন। নিয়মের কনফিগারেশন, চেষ্টা করা কাজ, প্রত্যাখ্যান এবং পরিণতিতে সুরক্ষিত সংস্করণ একসঙ্গে ধারণ করুন।

## রিপোজিটরি সম্পূর্ণতার যাচাই

**এমন রিপোজিটরি দিন যা অন্য অবদানকারী স্বাধীনভাবে বুঝে ব্যবহার করতে পারে।** README মানচিত্রের দিকে নির্দেশ করে, মানচিত্র কর্তৃত্বপূর্ণ রেকর্ড খুঁজে দেয়, মালিকানার আওতায় সংবেদনশীল path থাকে এবং সুরক্ষা **`main`**-এ প্রযোজ্য। একটি অনুমোদিত প্রস্তাব এবং একটি প্রত্যাখ্যাত প্রকাশ-চেষ্টা রাখুন।

**শুধু সেটিং দেখে নিয়ম কার্যকর হওয়ার দাবি করবেন না।** সেটিং উদ্দেশ্যকৃত কনফিগারেশন দেখায়। Sandbox পরীক্ষা নির্দিষ্ট ভূমিকা ও পথের পর্যবেক্ষিত আচরণ দেখায়। Agent এবং Actions পাঠে দুই ধরনের প্রমাণই রাখুন।

## সমস্যা সমাধান ও রোলব্যাক

**মালিকের অনুরোধ অনুপস্থিত:** লেখার অনুমতি এবং ভিত্তি শাখার path coverage নিশ্চিত করুন। **সুরক্ষা অনুপস্থিত:** পরিকল্পনা ও দৃশ্যমানতা যাচাই করুন। **Merge চালু:** rule target, bypass কনফিগারেশন এবং পর্যালোচনার সংখ্যা পরীক্ষা করুন।

**রোলব্যাক:** merge না হওয়া প্রস্তাব বন্ধ করুন এবং ল্যাবের automation নিষ্ক্রিয় করুন। আরেকটি পর্যালোচিত PR দিয়ে merge হওয়া ল্যাবের বিষয়বস্তু ফিরিয়ে নিন। ফেলে দেওয়া যায় এমন রিপোজিটরি মুছার আগে প্রমাণ রাখুন। ব্যর্থ পরীক্ষা শেষ করতে সুরক্ষা দুর্বল করবেন না।

## অনুশীলন ও স্ব-মূল্যায়ন

**অবদানকারী হিসেবে `docs/policy.md` সম্পাদনার প্রস্তাব দিন।** শুধু রক্ষণাবেক্ষণকারীর অনুমোদন নীতি-মালিকের অনুমোদন প্রতিষ্ঠা করে কি না সিদ্ধান্ত নিন।

**প্রত্যাশিত যুক্তি:** পর্যালোচনার সংখ্যা একা কর্তৃত্ব প্রতিষ্ঠা করে না। Path-এর জন্য নীতি-মালিকের অন্তর্ভুক্তি এবং বর্তমান ভূমিকা-পর্যালোচনা দরকার। কার্যকরভাবে বলবৎ নয় এমন ভূমিকা-নির্দিষ্ট শর্তগুলো প্রক্রিয়াগত নিয়ন্ত্রণ হিসেবে তালিকাভুক্ত করুন।

## প্রধান রেফারেন্স

- **পরিকল্পনা ও পর্যালোচনা নিয়ন্ত্রণ:** [সুরক্ষিত শাখা](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)।
- **মালিক নির্ধারণ:** [কোডের মালিক](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)।
- **ব্রাউজার থেকে অবদান:** [ফাইল সম্পাদনা](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)।

## পরবর্তী ধাপ

**[এজেন্ট অ্যাডাপ্টার ও অ্যাকশন](/articles/ai-collaboration-github-agents-actions/)-এ এগিয়ে যান** এবং উৎসের প্রমাণকে চালানো যায় এমন যাচাইয়ের সঙ্গে যুক্ত করুন।
