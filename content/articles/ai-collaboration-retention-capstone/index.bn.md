---
title: "AI সহযোগিতার ক্যাপস্টোন: GitHub, Confluence এবং Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "ব্যর্থতার প্রমাণ এবং স্বাধীন পর্যালোচনাসহ GitHub-প্রথম এবং Confluence/Jira কর্মপ্রবাহে একটি কৃত্রিম retention পরিবর্তন সম্পন্ন করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "দলগত সহযোগিতা", "সফটওয়্যার ইঞ্জিনিয়ারিং"]
tags: ["AI সহযোগিতা কোর্স", "retention প্রস্তাব", "GitHub পর্যালোচনা", "Confluence Jira কর্মপ্রবাহ", "ব্যর্থতার ম্যাট্রিক্স", "স্বাধীন গ্রহণ"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "সাইবার নিরাপত্তা কর্মক্ষেত্রে যৌথ প্রকল্পের কাজ পর্যালোচনা করা পেশাজীবীদের চিত্র"
coverCaption: ""
---

[AI সহযোগিতা কোর্সে ফিরে যান](/ai-collaboration-course-start/)

**PROP-042 দুইবার সরবরাহ করুন**, একবার GitHub-প্রথম পদ্ধতিতে এবং একবার GitHub-এর সঙ্গে Confluence/Jira ব্যবহার করে। আপনি অবদান রাখবেন, আলাদা মালিকেরা পর্যালোচনা করবেন, এবং অনুমোদিত প্রকাশকেরা পরিবর্তনটি প্রয়োগ করবেন। আগের পাঠের পর বিচ্ছিন্ন synthetic sandbox ব্যবহার করুন। এই ক্যাপস্টোন প্রত্যাখ্যান, পুনরুদ্ধার এবং স্বাধীন হস্তান্তরসহ সম্পূর্ণ প্রক্রিয়া পরীক্ষা করে। এটি শুধু সহকারীর লেখার মান পরীক্ষা করে না।

## মূল শিক্ষা

- **একটি অভিন্ন পরিবর্তন** দুইটি authority model তুলনা করে।
- **নেতিবাচক পরীক্ষা** সফল delivery-এর মতোই গুরুত্বপূর্ণ।
- **প্রমাণের প্যাকেজ** স্বাধীন পর্যালোচনাকে সহায়তা করে।
- **ল্যাব সম্পন্ন হওয়া** production rollout-এর অনুমতি দেয় না।

## শুরু করার আগে

**পূর্বশর্ত:** আগের [কোর্স মডিউল](/ai-collaboration-course-start/), অনুমোদিত sandbox access, এবং আলাদা reviewer। **পরিকল্পিত সময়:** একাধিক session-এ আট থেকে বারো ঘণ্টা, সঙ্গে স্বাধীন পর্যালোচনা। প্রকৃত সময় account setup এবং repair-এর ওপর নির্ভর করে। **কঠিনতা:** advanced।

**প্রয়োজনীয় artifact:** charter, map, policy, adapter, baseline, manifest, fixed proposal, owner review, ledger, recovery record, এবং handoff। পরিকল্পনা-নির্ভর অনুমতি না থাকলে completion বন্ধ হবে। সেগুলোকে অনুমান করে pass ধরা যাবে না।

**পরীক্ষার আগে প্রতিটি track-এর জন্য একটি evidence directory তৈরি করুন।** Reviewer যেন chat summary ছাড়াই actor, source revision, attempted action, observed result, এবং final state শনাক্ত করতে পারেন।

## দুইটি baseline তৈরি করুন

1. **বিচ্ছিন্ন run তৈরি করুন** এবং নাম দিন GitHub-first ও Mixed। Revision এবং review আলাদা রাখুন।
2. **সাত দিনের baseline পুনরুদ্ধার করুন** প্রতিটি track-এর অনুমোদিত পদ্ধতিতে, এবং তৈরি হওয়া revision সংরক্ষণ করুন।
3. **Denial control যাচাই করুন** contributor এবং excluded-user account দিয়ে।
4. **বর্তমান context ধরুন** এবং adapter/policy-এর সামঞ্জস্য নিশ্চিত করুন।
5. **Scope ঘোষণা করুন:** ত্রিশ দিনের synthetic export retention। বাস্তব data, backup, এবং legal hold বাদ থাকবে।

**PROP-042 একটি correlation label, পুনঃব্যবহারযোগ্য approval নয়।** প্রতিটি run-এর frozen revision এবং source evidence আলাদা হবে। Report-এ run ID দিন।

## GitHub-first delivery

**GitHub lesson ব্যবহার করে Issue এবং candidate PR খুলুন।** Requirement, configuration, proposal, এবং runbook একসঙ্গে পরিবর্তন করুন। Protected base ধরুন, trusted check চালান, এবং final commit-এ product ও operations review নিন।

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**Sandbox থেকে প্রকৃত reference পূরণ করুন।** এই outline প্রত্যাশিত mapping, সম্পূর্ণ evidence নয়। Reviewer শেষ না করা পর্যন্ত maintainer merge করবেন না। তারপর স্বাধীনভাবে **`main`** পড়ুন। Final record link করার পর Issue বন্ধ করুন।

## Mixed track delivery

**Confluence version পড়ুন এবং Jira proposal freeze করুন।** দুই owner-এর review নিন। Delivery pending অবস্থায় requirement publish করুন, configuration merge করুন, runbook publish করুন, এবং Done করার আগে সব system আবার পড়ুন।

**প্রতিটি publication record করুন** page version, commit, অথবা transition evidence-সহ। Repository requirement copy snapshot হিসেবে থাকবে। Local checker বর্তমান Confluence authority প্রমাণ করে না।

| তুলনা | GitHub-first | Mixed workplace |
|---|---|---|
| **Requirement** | Protected repository review | Confluence owner-reviewed publication |
| **Coordination** | Issue/PR | Fixed Jira proposal |
| **Publication unit** | Repository merge | Separate page writes and merge |
| **Freshness** | Protected commit | Page versions plus commit |
| **Recovery** | Reviewed revert/compensation | Ledger-guided compensation |

**Ownership need অনুযায়ী workflow বাছুন।** GitHub-first cross-system coordination কমায়। Mixed track workplace home ধরে রাখে এবং publication/access check যোগ করে।

## Failure matrix চালান

| Case | Injection | Required observed evidence |
|---|---|---|
| **Approved change** | Submit reviewed thirty-day proposal | Consistent read-back and review |
| **Stale context** | Change source after capture | Rejection, reconciliation, reapproval |
| **Unauthorized write** | Contributor publishes | Denial and unchanged revision |
| **Conflict** | Jira says sixty, Confluence seven | Block and owner reconciliation |
| **Partial publication** | Interrupt after one write | Pending ledger and recovery |
| **Access denial** | Remove task read access | No protected text or publication |
| **Recovery** | Approved completion/backout | New reviewed revisions |
| **Handoff** | New session gets map/ledger only | Fresh read and correct next action |

**Cross-system conflict Mixed-এর বিষয়।** GitHub-first-এ Issue description এবং approved file-এর conflict পরীক্ষা করুন। অন্য প্রযোজ্য case দুই track-এই চালান। Local validator failure live permission evidence-এর বিকল্প নয়।

| Case and evidence file | GitHub-first run | Mixed run |
|---|---|---|
| **Approved change** `01-approved-change.md` | Reviewed PR and read-back | Reviewed pages, merge, and ledger |
| **Stale context** `02-stale-context.md` | Change protected base after capture | Change an authority page after capture |
| **Unauthorized write** `03-unauthorized-write.md` | Contributor direct-push denial | Contributor page edit and transition denial |
| **Conflict** `04-conflict.md` | Issue disagrees with approved file | Jira text disagrees with Confluence |
| **Partial publication** `05-partial-publication.md` | Stop before merge or read-back | Stop after one page write |
| **Access denial** `06-access-denial.md` | Withhold a protected repository source | Exclude a user from a restricted page |
| **Recovery** `07-recovery.md` | Reviewed revert or completion | Ledger-guided compensation |
| **Handoff** `08-handoff.md` | New session reads protected files | New session reads mapped pages and ledger |

**প্রতিটি test-এর আগে তার file তৈরি করুন।** Expected result, observed result, actor role, initial ও final revision, native evidence reference, এবং reviewer decision লিখুন। দুই track-এর directory আলাদা রাখুন।

**Expected এবং observed outcome আলাদা রাখুন।** প্রতিটি case-এ run ID, actor role, initial revision, attempted action, expectation, observation, resulting revision, এবং reviewer decision record করুন। Shared report থেকে credential এবং account identifier সরিয়ে দিন।

## Completion মূল্যায়ন

**প্রযোজ্য প্রতিটি row-এর observed evidence** এবং independent acceptance না থাকলে pass নয়। Reviewer permission, source freshness, role review, partial publication, এবং handoff reconstruction পরীক্ষা করবেন।

**Unauthorized publication, model-এ denied text পৌঁছানো, অথবা পরিবর্তিত base নীরবে overwrite হলে সঙ্গে সঙ্গে fail করুন।** Control সংশোধন করে repeat test pass না করা পর্যন্ত কাজ Blocked রাখুন। Failure-কে favorable score-এ মেশাবেন না।

**Completed/blocked case, rejected stale proposal, denied write, recovery, এবং reviewer time মাপুন।** Observed না হওয়া পর্যন্ত proposed outcome expected থাকবে।

## দুইটি run পরিকল্পনা করুন

**দুই track-এ approval পুনঃব্যবহার করবেন না।** Value একই হলেও source home, captured revision, permission, এবং publication sequence আলাদা। প্রতিটি run-এর নিজস্ব evidence directory এবং review packet দিন।

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**এই নামগুলো organization example।** এগুলো supplied archive file নয়। Approved sandbox-এ প্রকৃত evidence ব্যক্তিগতভাবে রাখুন। Shared submission-এ role label ও redacted reference ব্যবহার করুন।

**Failure চালানোর আগে test observer নিযুক্ত করুন।** Contributor attempted action করবে। Observer initial state, outcome, এবং resulting state লিখবে। Reviewer পরে evidence claim সমর্থন করে কি না নির্ধারণ করবেন। Role overlap থাকলে প্রকাশ করুন।

## Failure isolation-এ চালান

**Case-এর মাঝখানে verified reviewed state-এ reset করুন।** Source drift, access revocation, এবং runbook mismatch একসঙ্গে inject করলে কোন control proposal reject করেছে বোঝা যায় না। প্রতি run-এ একটি failure reviewer-এর জন্য traceable কারণ দেয়।

1. **Initial state ধরুন:** source revision, configuration, delivery state, এবং actor role।
2. **একটি synthetic injection দিন:** authorized test route দিয়ে একটি condition বদলান।
3. **Bounded action চেষ্টা করুন:** validation, read, publication, অথবা handoff।
4. **Observation record করুন:** actual output এবং resulting source state।
5. **Review-এর মাধ্যমে repair করুন:** control restore করার আগে failure evidence রাখুন।
6. **Positive case পুনরায় চালান:** corrected workflow permitted work deliver করে কি না দেখুন।

**Planned failure-ও failure observation।** Probe করার উদ্দেশ্য ছিল বলে unauthorized publication-কে successful test বলবেন না। Test defect প্রকাশ করেছে, কিন্তু publication boundary fail করেছে এবং repair দরকার।

## Mixed result ব্যাখ্যা করুন

**Illustrative evidence package:** local consistency pass, product ও operations fixed package review করেছে, requirement publication সফল, এবং runbook edit access denied। Configuration এখনও merge হয়নি। Jira Blocked।

| Claim | Verdict | Reason |
|---|---|---|
| **Candidate records agree** | Supported by local check | Supplied records passed comparisons |
| **Owners accepted intent and operations** | Requires native fixed reviews | Role labels alone are insufficient |
| **Thirty-day delivery completed** | Unsupported | Required publication steps remain pending |
| **Permission boundary works for every role** | Unsupported | One denied action has limited scope |
| **Recovery owner should act** | Supported as next step | Partial delivery needs a reviewed decision |

**Expected reasoning:** run incomplete রাখুন, current source যাচাই করুন, এবং appropriate owner decision চান। Permission দুর্বল করে বা snapshot check-কে live publication evidence বলে কাজ শেষ করবেন না।

## Independent reader দিয়ে review

**Reviewer-কে event reconstruct করতে বলুন**, আপনার conclusion পড়তে নয়। তিনি approved baseline, fixed proposal, owner decision, resulting revision, failed attempt, repair, এবং remaining gap আপনার narration ছাড়া খুঁজে পাবেন।

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**প্রতিটি requirement আলাদা score করুন।** Supported, Failed, Blocked, অথবা Not run এবং evidence reference ব্যবহার করুন। Consistency, approval, permission, recovery, ও handoff পৃথক requirement। Green local test-এর সমষ্টি failed live publication boundary পূরণ করে না।

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported মানে reviewer প্রতিটি প্রযোজ্য case-এর observed evidence পেয়েছেন।** Observed control failure হলে Failed, access বা control না থাকলে Blocked, এবং চেষ্টা না হলে Not run লিখুন। প্রতিটি case-এর native reference তার named evidence file-এ রাখুন।

**Course pass gate:** GitHub-first এবং Mixed দুই track শেষ করুন। প্রতিটি track-এর আটটি প্রযোজ্য case Supported হতে হবে। Failed boundary অথবা missing native read-back track block করে। একটি track শেষ হলে documented partial result হবে, course completion নয়।

**Redacted model package, illustrative only:**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

Illustrative reference-গুলোর বদলে sandbox-এর observed artifact বসান। Mixed track-এর জন্য আলাদা source version ও review-সহ পুরো package পুনরাবৃত্তি করুন। Reviewer-এর mixed package-এ copied GitHub approval প্রত্যাখ্যান করা উচিত।

## সীমাবদ্ধ সিদ্ধান্ত লিখুন

**ভালো closing decision পরের pilot নির্ধারণ করে**, unrestricted rollout নয়। একই role এবং direct lookup route রেখে আরেকটি synthetic export setting বাছুন। Real data এবং automated publication scope-এর বাইরে রাখুন।

| Decision element | Required detail |
|---|---|
| **Scope** | One next change and its explicit exclusions |
| **Evidence** | Supported cases and unresolved failures |
| **Controls** | Platform-enforced and procedural requirements separately |
| **Owners** | Accountable role for each remaining gap |
| **Runtime gap** | Untested deletion/deployment behavior |
| **Stop conditions** | Missing access, changed authority, unauthorized publication |

**Completion check:** দুই run package independent reconstruction পার করবে, প্রযোজ্য failure case observed evidence পাবে, এবং unresolved control দৃশ্যমান থাকবে। শুধু GitHub track শেষ হলে partial course completion report করুন। Mixed track একই আচরণ করবে ধরে নেবেন না।

## Troubleshooting এবং backout

**শুধু happy-path evidence:** denial এবং interruption test আবার চালান। **Overlapping role:** প্রকাশ করে আলাদা user দিয়ে repeat করুন। **Missing plan control:** থামুন এবং approved sandbox নিন।

**Backout:** reviewed PR ও Confluence edit দিয়ে baseline restore করুন, temporary integration revoke করুন, Jira evidence archive করুন, এবং evidence retention-এর পর owner-approved synthetic cleanup করুন। Recovery history রাখুন।

## Rollout decision তৈরি করুন

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**Expected reasoning:** Synthetic success আরেকটি bounded pilot সমর্থন করে। Production-এর জন্য real data, deployment, provider handling, এবং runtime behavior নিয়ে আলাদা approval দরকার। Successful assistant answer deployment authorization নয়।

## প্রধান reference

- **Repository controls:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)।
- **Workplace access:** [Confluence permissions](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/)।
- **Delivery controls:** [Jira permission schemes](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/)。

## পরবর্তী ধাপ

**Missing control review করতে [course hub](/ai-collaboration-course-start/)-এ ফিরুন।** আরেকটি pilot বাছার আগে [framework article](/articles/one-source-many-tools-ai-collaboration-framework/)-এর সঙ্গে implementation তুলনা করুন।
