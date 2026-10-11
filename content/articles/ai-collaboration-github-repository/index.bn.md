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

**প্রতিটি map entry-তে current retention value রাখবেন না।** “seven days” রাখা map PROP-042-এর পরে sync করার আরেকটি value হয়ে যাবে। স্থায়ী identifier এবং location map-এ রাখুন, value authoritative record থেকে পড়ুন।

**Map change-কে routing change হিসেবে protect করুন।** REQ-17-কে draft file-এ redirect করলে approved requirement অপরিবর্তিত থাকলেও source selection বদলে যায়। Map বদলালে destination, owner এবং authority scope review করুন।

## Baseline এবং candidate আলাদা করুন

**Repository root-এ active lab record থাকে।** Download করা **`baseline/`** directory একটি teaching fixture। প্রতিটি পরের PR-এর protected baseline এটি স্বয়ংক্রিয়ভাবে নয়। Reviewed work **`main`**-এ পৌঁছানোর পরে protected root record পরের proposal-এর base নির্ধারণ করে।

| অবস্থান | উদ্দেশ্য | PROP-042-এ edit করবেন? |
|---|---|---|
| **Root requirement/config/runbook** | Branch-এর proposed active record | হ্যাঁ, reviewed change-এর মাধ্যমে |
| **`baseline/`** | Original offline exercise fixture | না |
| **Detached trusted worktree** | Root থেকে captured protected record | না |
| **`context.json`** | Captured base byte-এর evidence | Reconciliation-এর পরে regenerate |

**Control change এবং retention change আলাদা রাখুন।** প্রথমে checker এবং review rule bootstrap করুন। পরে seven-to-thirty-day change propose করুন। Policy rewrite, workflow rewrite এবং value change একসঙ্গে করলে repaired control আর bypassed control আলাদা করা কঠিন হয়।

## সম্পূর্ণ পরিবর্তন review করুন

**PR description গ্রহণের আগে changed file খুলুন।** Description author-এর intention বলে। Diff submitted change দেখায়। PROP-042-এ requirement revision, scope exclusion, configuration, runbook, proposal base এবং manifest evidence পরীক্ষা করুন।

1. **Product review:** thirty-day intent এবং অপরিবর্তিত exclusion নিশ্চিত করুন।
2. **Operations review:** runbook proposed configuration-এর সঙ্গে মেলে এবং runtime limitation রাখে নিশ্চিত করুন।
3. **Maintainer review:** JSON, source capture, check result এবং unrelated change পরীক্ষা করুন।
4. **Control review:** map, policy, CODEOWNERS বা workflow-এর যেকোনো change আলাদা করে পরীক্ষা করুন।

**Green check unrelated deletion ব্যাখ্যা করে না।** Branch policy document সরিয়ে retention বদলালে separate proposal বা specific owner review চান। Scope সীমিত রাখলে review object বোঝা সহজ থাকে।

## Denial test নির্ণয় করুন

**প্রতিটি evidence row-তে একটি attempted action রাখুন।** “Contributor failed” অস্পষ্ট। User-এর সাধারণ write access নাও থাকতে পারে, browser limitation হতে পারে বা intended branch rule প্রয়োগ হতে পারে। এসব observation ভিন্ন boundary প্রতিষ্ঠা করে।

| Observation | Interpretation | Follow-up |
|---|---|---|
| **কোনো branch তৈরি করতে পারে না** | Contribution access নেই | Approved Issue/fork route ব্যবহার করুন |
| **Branch তৈরি করে, main-এ publish করতে পারে না** | Tested publication route restricted | Unchanged main revision capture করুন |
| **একটি review-এ merge blocked** | Tested PR-এ review count প্রযোজ্য | Role-specific evidence যোগ করুন |
| **Rule সত্ত্বেও administrator publish করে** | Tested identity boundary bypass করে | Bypass setting এবং grant পরীক্ষা করুন |

**Shared course evidence-এ account detail না দেখিয়ে role এবং action record করুন।** Reviewer-এর জন্য native actor record private-এ রাখুন। Rule configuration, attempted operation, denial এবং resulting protected revision একসঙ্গে capture করুন।

## Repository completion check

**এমন repository দিন যা অন্য contributor স্বাধীনভাবে ব্যবহার করতে পারে।** README map-এ নির্দেশ করে, map authoritative record resolve করে, owner coverage sensitive path অন্তর্ভুক্ত করে এবং protection **`main`**-এ প্রযোজ্য। একটি permitted proposal এবং একটি denied publication attempt রাখুন।

**শুধু setting দেখে enforcement দাবি করবেন না।** Setting intended configuration দেখায়। Sandbox attempt নির্দিষ্ট role এবং route-এর observed behavior দেখায়। Agent এবং Actions lesson-এ দুই ধরনের evidence রাখুন।

## Troubleshooting এবং rollback

**Owner request missing:** write access এবং base-branch path coverage নিশ্চিত করুন। **Protection absent:** plan এবং visibility যাচাই করুন। **Merge enabled:** rule target, bypass configuration এবং review count পরীক্ষা করুন।

**Rollback:** unmerged proposal বন্ধ করুন এবং lab automation deactivate করুন। আরেকটি reviewed PR দিয়ে merged lab content revert করুন। Disposable repository মুছার আগে evidence রাখুন। ব্যর্থ test শেষ করতে protection দুর্বল করবেন না।

## Exercise এবং self-check

**Contributor হিসেবে `docs/policy.md` edit propose করুন।** Maintainer approval একাই policy-owner approval প্রতিষ্ঠা করে কিনা সিদ্ধান্ত নিন।

**প্রত্যাশিত reasoning:** review count একা authority প্রতিষ্ঠা করে না। Path-এ policy-owner coverage এবং current role review দরকার। Enforced নয় এমন role-specific requirement procedural control হিসেবে তালিকাভুক্ত করুন।

## প্রধান রেফারেন্স

- **Plan এবং review control:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)।
- **Owner eligibility:** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)।
- **Browser contribution:** [Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)।

## পরবর্তী ধাপ

**[Agent Adapters and Actions](/articles/ai-collaboration-github-agents-actions/)-এ এগিয়ে যান** এবং source evidence-কে executable check-এর সঙ্গে যুক্ত করুন।
