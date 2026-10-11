---
title: "নন-কোডারদের জন্য GitHub AI ওয়ার্কফ্লো: Issues এবং Pull Requests"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "স্থানীয় ডেভেলপমেন্ট পরিবেশ ছাড়াই ব্রাউজার সম্পাদনা, Issues, চ্যাট কনটেক্সট প্যাকেট এবং পর্যালোচিত pull requests ব্যবহার করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "দলগত সহযোগিতা", "সফটওয়্যার ইঞ্জিনিয়ারিং"]
tags: ["AI সহযোগিতা কোর্স", "GitHub ব্রাউজার সম্পাদনা", "GitHub Issues", "pull request", "নন-কোডিং অবদানকারী", "কনটেক্সট প্যাকেট", "রিভিউ হ্যান্ডঅফ"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "সাইবার নিরাপত্তা কর্মক্ষেত্রে যৌথ প্রকল্প পর্যালোচনা করা পেশাজীবীদের চিত্র"
coverCaption: ""
---

[AI সহযোগিতা কোর্সে ফিরে যান](/ai-collaboration-course-start/)

**নন-কোডিং অবদানকারীরা ব্রাউজারেও একই কর্তৃত্বের নিয়ম ব্যবহার করেন।** আপনি GitHub-এর উৎস পড়েন, অনুমোদিত চ্যাট টুল দিয়ে খসড়া তৈরি করেন এবং একটি Issue বা branch edit জমা দেন। Maintainer পরীক্ষা চালিয়ে review-এর পর প্রকাশ করেন। Repository protection সক্রিয় হওয়ার পর এই workflow ব্যবহার করুন, যাতে ব্রাউজার access coding-agent নিয়ন্ত্রণ এড়িয়ে না যায়।

## মূল বিষয়

- **ব্রাউজার কাজের** জন্য স্থানীয় terminal লাগে না।
- **Context packet** scope এবং revision evidence ধরে রাখে।
- **Issues এবং branches** প্রস্তাব হিসেবেই থাকে।
- **Handoff** বাকি কাজ এবং পরের ভূমিকা চিহ্নিত করে।

## শুরু করার আগে

**প্রয়োজনীয়তা:** [repository boundary lesson](/articles/ai-collaboration-github-repository/), lab read access এবং প্রয়োজনে অনুমোদিত chat tool। **সময়:** 45 থেকে 60 মিনিট। **কঠিনতা:** প্রাথমিক। শুধু Issue ব্যবহারকারী contributors স্থানীয় Git এবং Actions বাদ দেন। PR জমা দেওয়া contributors [agent and Actions lesson](/articles/ai-collaboration-github-agents-actions/) শেষ করা maintainer-এর সঙ্গে সমন্বয় করেন।

**Connector-বিহীন ভিত্তি:** নিজে GitHub খুলুন এবং শুধু synthetic excerpt দিন। কোনো chat subscription feature ধরে নেওয়া হয় না। কোনো provider অনুমোদিত না হলে একই record ব্যবহার করে হাতে খসড়া লিখুন।

**সমাপ্তির ফল:** fixed source revision, proposed wording, affected files, exclusions এবং unresolved questions-সহ একটি Issue বা PR hand off করবেন।

## Source packet পড়ুন

1. **`main`-এ MAP-01 খুলুন**, তারপর POL-01, REQ-17 এবং RUN-04 খুঁজুন।
2. **প্রতিটি source পড়ুন** এবং browser-এর commit view থেকে commit revision লিখে রাখুন।
3. **প্রাসঙ্গিক synthetic section কপি করুন** filename, revision, scope এবং exception-সহ।
4. **Packet-কে snapshot-based হিসেবে চিহ্নিত করুন**, যতক্ষণ না publication-এর আগে maintainer current source-এর সঙ্গে তুলনা করেন।

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

**আসল sandbox revision ব্যক্তিগতভাবে যুক্ত করুন।** Template-এ সম্পূর্ণ evidence নেই। Publication সুপারিশের আগে assistant-কে missing record চিহ্নিত করতে বলুন।

**Live source পড়ার আগে পূর্ণ synthetic packet:**

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

**এটি একটি সম্পূর্ণ draft request।** Missing-evidence line ইচ্ছাকৃত। Publication চাওয়ার আগে supplied lab baseline-এর বদলে live sandbox revision দিন।

## একটি Issue খুলুন

**Issues, New issue নির্বাচন করুন** এবং **`PROP-042: propose thirty-day synthetic retention`** title ব্যবহার করুন। এই description paste করে source packet যুক্ত করুন।

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

**Chat-কে packet-এর সঙ্গে proposal তুলনা করতে বলুন**, assumption তালিকাভুক্ত করতে এবং owner question-এর draft লিখতে বলুন। Draft-টি Issue-এ সংরক্ষণ করুন। Approval বা publication চাইবেন না এবং chat thread-কে decision register ভাববেন না।

## Browser edit জমা দিন

1. **Repository-এর Code tab খুলুন।** File list-এর ওপর branch menu বেছে **`main`** নিশ্চিত করুন, **`proposal-042`** লিখুন এবং **Create branch: proposal-042 from main** নির্বাচন করুন। Branch তৈরি না হলে approved fork বা নিচের Issue route ব্যবহার করুন।
2. **Branch menu-তে `proposal-042` নিশ্চিত করুন** এবং তারপর file খুলুন। File ও pencil icon বেছে edit করুন। GitHub web editor protected branch edit করে না।
3. **Requirement edit করে** thirty days এবং revision 2 দিন। প্রতিটি পরের edit-এর আগে branch menu আবার খুলুন। একই branch-এ configuration এবং runbook edit করুন।
4. **`proposal.json` edit করে** to_days 30, from_days 7 এবং base_revision 1 দিন।
5. **Markdown preview করুন** এবং JSON punctuation দেখুন। প্রতিটি browser edit **`proposal-042`**-এ commit করুন।
6. **Pull requests, তারপর New pull request খুলুন।** **`proposal-042`**-এর সঙ্গে **`main`** compare করুন, চারটি file change দেখুন এবং Issue উল্লেখ করে PR তৈরি করুন। Maintainer-কে protected base-এর fresh manifest যুক্ত করে consistency check চালাতে বলুন।
7. **Final proposal revision-এ owner review চাইুন।** Review এবং read-back সফল না হওয়া পর্যন্ত delivery open রাখুন।

**Navigation record:** repository name, Issue number, proposal branch, changed-file path, PR number, check-run name, review revision এবং final `main` commit লিখুন। Issues, Code, Pull requests, Actions এবং PR Checks/Reviews view ব্যবহার করে record আবার খুঁজুন। GitHub control সরালে screenshot দেখে অনুমান করবেন না, number বা commit ID দিয়ে একই record খুঁজুন। Record URL এবং observed status-সহ private evidence note export করুন। Authorized team-এর বাইরে share করার আগে account name, email, token, tenant identifier এবং unrelated repository data সরান। Unredacted evidence approved private location-এ রাখুন।

**GitHub branch এবং fork contribution route নথিভুক্ত করে।** Write access না থাকা contributor approved fork বা Issue route ব্যবহার করেন। Fork মূল repository-তে publication access দেয় না।

## Worked diff দেখুন

| File | Baseline | Candidate |
|---|---|---|
| **Requirement** | Revision 1, seven days | Revision 2, thirty days |
| **Configuration** | Seven days | Thirty days |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Proposal** | From 7, to 7 | From 7, to 30, base 1 |
| **Manifest** | Not captured | Hashes of protected pre-change sources |

**Manifest base বর্ণনা করে**, proposed thirty-day wording নয়। Candidate requirement hash করে baseline evidence বললে trusted-base mismatch তৈরি হয়।

## Verify এবং handoff

**Positive test:** owner review এবং successful check-এর পর maintainer merge করেন। **`main`**-এর resulting file খুলে agreement নিশ্চিত করুন। Resulting commit এবং read-back Issue-এ যুক্ত করুন। এটি committed configuration প্রমাণ করে, runtime deletion behavior নয়।

**Negative test:** Chat-কে proposal approve বা publish করতে বলুন। Expected policy behavior হলো draft-only response। Contributor হিসেবে আলাদা করে direct publication চেষ্টা করুন এবং unchanged source revision-সহ platform denial record করুন। Behavioral test এবং access-control test আলাদা রাখুন।

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

**শুধু map এবং handoff নিয়ে নতুন session শুরু করুন।** Fresh source read বা browser evidence-এর explicit request চাইুন। Previous assistant summary পুনরাবৃত্তি না করে source record থেকে value reconstruct করতে হবে।

## Context না হারিয়ে draft করুন

**Browser contributor-এর একটি সম্পূর্ণ question দরকার।** “Please change retention to thirty days” বর্তমান authority, scope, review state এবং affected record বাদ দেয়। Chat-কে source packet ও drafting instruction দিন। Record না থাকলে remembered text বসাবেন না, maintainer-এর কাছে authorized evidence চাইুন।

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Copy করার আগে answer inspect করুন।** Scope বদলেছে, commit বানানো হয়েছে বা approval complete বলা হয়েছে কি না দেখুন। Unsupported claim সরান এবং unresolved question Issue-এ রাখুন। Chat proposal লিখতে সাহায্য করে, সে না-পড়া system থেকে evidence দেয় না।

## Contribution route বেছে নিন

| Situation | Route | Deliverable |
|---|---|---|
| **Read access only** | Fixed proposed wording-সহ Issue | Maintainer-ready change request |
| **Approved branch access** | One proposal branch-এ browser edit | Related file change-সহ PR |
| **Approved fork route** | Fork এবং upstream PR | Upstream review-এর অপেক্ষায় candidate |
| **No source access** | Stop করে authorized evidence চাইুন | Explicitly blocked task |

**Issue route সম্পূর্ণ contribution**, ব্যর্থ coding exercise নয়। আপনি intended change, evidence, scope এবং review question দেন। Maintainer patch এবং manifest দেন। তারপর আপনার request-এর সঙ্গে patch মেলে কি না দেখুন।

| Route | Contributor completion check | Maintainer handoff |
|---|---|---|
| **Issue only** | Issue-এ verified source packet, fixed proposed wording, exclusions এবং open question আছে | Maintainer branch তৈরি, check চালান এবং PR link করেন |
| **PR** | One branch-এ সব affected file, PR diff proposal-এর সঙ্গে মেলে এবং reviewer final revision পান | Maintainer check চালান, owner review নেন, merge করেন এবং read-back record করেন |

**Browser edit করলে proposal branch-এ থাকুন।** প্রথম edit branch তৈরি করার পর একই branch selector থেকে বাকি file খুলুন। শেষে PR diff দেখুন। চারটি unrelated branch চারটি অসম্পূর্ণ change তৈরি করে, একটি reviewable package নয়।

## Proposed wording inspect করুন

**দুর্বল wording-এর উদাহরণ:** “Exports now remain available for thirty days.” এটি delivery complete বলে এবং synthetic scope বাদ দেয়। Review চলার সময় proposal statement ব্যবহার করুন।

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**প্রতিটি affected file-এর সঙ্গে wording তুলনা করুন।** Candidate-এ requirement revision এগিয়েছে। Configuration thirty-এ পৌঁছেছে। Runbook-এর প্রথম line thirty-এ পৌঁছেছে এবং lab limitation রেখেছে। Proposal এখনও seven-কে previous value এবং revision one-কে base বলে।

**Mismatch হলে অপরিচিত control repair না করে প্রশ্ন করুন।** Maintainer patch protection দুর্বল বা policy delete করলে explanation এবং separate review চাইুন। Workflow-এর প্রতিটি line না বুঝেও requested scope-এর বাইরের change চিহ্নিত করা যায়।

## Review feedback-এর উত্তর দিন

**উদাহরণ review:** Operations এমন একটি sentence চায় যা বলে configuration rollback deleted file ফিরিয়ে আনে না। একই branch-এ draft update করুন এবং reviewer-কে amended scope জানান। Final review modified proposal-এর উপর হতে হবে, পুরনো chat copy-এর উপর নয়।

| Review comment | Contributor action |
|---|---|
| **Missing exclusion** | Wording ফিরিয়ে এনে intent review চাইুন |
| **Stale source revision** | New authorized packet নিয়ে reconcile করুন |
| **Missing manifest** | Maintainer-কে protected base capture করতে বলুন |
| **Unrelated control change** | Review-এর আগে আলাদা বা remove করুন |
| **Untested runtime claim** | Exact lab limitation দিয়ে বদলান |

**উত্তর না পাওয়া পর্যন্ত question visible রাখুন।** মূল সমস্যা ঠিক না করে comment resolve করলে useful signal মুছে যায়। Reply-তে amendment বা evidence link দিন, যাতে অন্য reviewer পুরো conversation না পড়েও decision অনুসরণ করতে পারেন।

## Browser completion check

**এমন Issue বা PR hand off করুন যা অন্য maintainer অনুমান ছাড়া চালাতে পারেন।** এতে source packet, proposed wording, affected record, exclusions, owner role এবং unresolved question থাকবে। Publication-এর পর read-back নিন এবং original proposal থেকে আলাদা রাখুন।

**Self-check:** আপনার chat না-জানা কাউকে package দিন। Requested, approved এবং published value আলাদা করতে বলুন। Merge-এর আগে thirty delivered বললে package label ঠিক করুন। Workplace track-এও একই discipline রাখুন।

| Review gate | Pass condition |
|---|---|
| **Source revisions** | Claimed প্রতিটি commit বা page version sandbox-এ খোলে। Unknown revision Missing থাকে। |
| **Exclusions** | Production data, backup এবং legal hold proposal-এর বাইরে থাকে। |
| **Questions** | Unresolved owner বা source question Issue বা PR-এ দৃশ্যমান থাকে। |
| **Approval freshness** | Review final proposal revision-এর নাম দেয়। Earlier approval later edit cover করে না। |

**যে কোনো failed gate publication pending রাখে।** Issue-only contributor maintainer-কে result দেন। PR contributor repair-এর পর আবার review চান।

## Troubleshooting এবং rollback

**Edit permission নেই:** Issue বা approved fork ব্যবহার করুন। **Invented commit reference:** verified evidence দিয়ে বদলে আবার review করুন। **Edit-এর আগের approval:** fresh approval চাইুন।

**Rollback:** Unmerged PR close করে evidence রাখুন। Merged content-এর জন্য maintainer-এর কাছে protected revert proposal চাইুন। Recovery সফল দেখাতে baseline বদলাবেন না।

## Exercise এবং self-check

**নতুন assistant-এর কাছ থেকে requirement record গোপন করুন** এবং publication recommendation চাইুন।

**Expected reasoning:** authoritative evidence চাইবে অথবা response snapshot-based বলে চিহ্নিত করবে। Fresh read সফল না হওয়া পর্যন্ত publication blocked থাকবে।

## Primary references

- **Browser steps:** [Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)।
- **Review boundary:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)।

## পরের ধাপ

**[Confluence এবং Jira Setup](/articles/ai-collaboration-confluence-jira-setup/)-এ এগিয়ে যান** এবং workplace system-গুলোতে একই operating model পুনরাবৃত্তি করুন।
