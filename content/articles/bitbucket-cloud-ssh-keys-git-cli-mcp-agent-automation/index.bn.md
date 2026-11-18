---
title: "Bitbucket Cloud SSH কী: AI এজেন্টের জন্য শুধু-পঠন Git প্রবেশাধিকার"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "শুধু-পঠন AI এজেন্ট কর্মপ্রবাহের জন্য Bitbucket Cloud SSH কী, Git CLI প্রবেশাধিকার, REST API টোকেন, 1Password এবং MCP টুল সেট আপ করুন।"
genre: ["ক্লাউড নিরাপত্তা", "ডেভেলপার টুল", "সিস্টেম প্রশাসন"]
tags: ["Bitbucket Cloud", "Bitbucket SSH কী", "রিপোজিটরি প্রবেশ কী", "প্রজেক্ট প্রবেশ কী", "ওয়ার্কস্পেস প্রবেশ কী", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "API টোকেন স্কোপ", "এজেন্ট অনুমতি", "শুধু-পঠন স্বয়ংক্রিয়করণ", "SSH হোস্ট কী"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "টার্মিনাল কর্মপ্রবাহে Bitbucket Cloud Git প্রবেশ, সীমিত-স্কোপ SSH কী, 1Password, REST API পাঠ এবং MCP টুল সংযুক্ত রয়েছে"
coverCaption: ""
---

**সীমাবদ্ধ এজেন্ট কর্মপ্রবাহ রিপোজিটরি পাঠ, API পাঠ, গোপন তথ্য ব্যবস্থাপনা এবং দূরবর্তী লেখার কাজ আলাদা রাখে।** সোর্সে প্রবেশের জন্য Secure Shell (SSH) দিয়ে Git ব্যবহার করুন, স্বয়ংক্রিয় checkout-এর জন্য শুধু-পঠন Bitbucket প্রবেশ কী, মেটাডেটার জন্য REST API এবং অনুমোদিত টুলের জন্য Model Context Protocol (MCP) সার্ভার ব্যবহার করুন। ব্যক্তিগত কী ও API টোকেন 1Password-এ রাখুন। লেখার কাজের আগে মানুষের অনুমোদন নিন।

<!--more-->

## মূল বিষয়

- **ডিফল্টে শুধু-পঠন:** এজেন্ট checkout-এর জন্য রিপোজিটরি বা প্রজেক্ট প্রবেশ কী ব্যবহার করুন। কোনোটিই push অনুমতি দেয় না।
- **ব্যক্তিগত পরিচয়:** ব্যবহারকারীর অ্যাকাউন্টের সঙ্গে যুক্ত ইন্টারেক্টিভ কাজের জন্য ব্যক্তিগত SSH কী ব্যবহার করুন।
- **গোপন তথ্যের হেফাজত:** 1Password SSH Agent ব্যবহার করুন, যাতে ব্যক্তিগত কী না পড়েই Git অনুমোদিত স্বাক্ষর কার্যক্রম করতে পারে।
- **CLI-এর অর্থ:** `git`, `curl` এবং ছোট নিরীক্ষিত API wrapper-কে ব্যবহারিক Bitbucket কমান্ড লাইন হিসেবে ধরুন।
- **MCP সীমা:** সীমিত পাঠ টুল প্রকাশ করুন। লেখার টুল বন্ধ রাখুন অথবা আলাদা অনুমোদনপথের পেছনে রাখুন।
- **লেখার অনুমোদন:** এজেন্টকে পরীক্ষা, তুলনা ও পরিবর্তন প্রস্তুত করতে দিন। push, pull request, merge বা সেটিংস পরিবর্তনের আগে মানুষের অনুমোদন নিন।

## শুরু করার আগে

**প্রয়োজনীয়তা:** Bitbucket Cloud প্রবেশাধিকার, Git, OpenSSH ক্লায়েন্ট, 1Password 8, 1Password CLI, সাইন-ইন করা CLI বা অনুমোদিত পরিষেবা অ্যাকাউন্ট এবং সার্ভার অনুমোদন নিয়ন্ত্রণসহ MCP হোস্ট। ৪৫ মিনিট রাখুন। দক্ষতার স্তর: মধ্যম।

প্রথমবার পরীক্ষার জন্য একটি টেস্ট রিপোজিটরি ব্যবহার করুন। উদাহরণের সব placeholder বদলান। নিচের কমান্ডগুলো পরীক্ষাহীন উদাহরণ। এগুলো কোনো সক্রিয় Bitbucket অ্যাকাউন্ট বা রিপোজিটরি নির্দেশ করে না।

**সংস্করণ:** এই নিবন্ধটি নকশার নির্দেশনা, নির্দিষ্ট সংস্করণভিত্তিক রানবুক নয়। পরীক্ষার আগে ইনস্টল করা Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, MCP হোস্ট ও MCP সার্ভারের সংস্করণ যাচাই করুন। `ssh-add -l` ব্যবহারের আগে বর্তমান অপারেটিং সিস্টেমের জন্য 1Password SSH Agent কনফিগার করুন।

**শেল, লগ, URL, Git রিমোট বা সোর্স ফাইলে পরিচয়পত্র রাখবেন না।** `<workspace>`, `<repository>`, `<api-token>` এবং `<socket-path>`-এর মতো placeholder ব্যবহার করুন। টার্মিনাল প্রতিলিপিতে আসল ব্যক্তিগত কী পেস্ট করবেন না।

## প্রবেশের সীমানা বেছে নিন

Bitbucket Cloud রিপোজিটরি, প্রজেক্ট ও ওয়ার্কস্পেস স্তরে প্রবেশ কী সমর্থন করে। কী কপি হলে প্রভাব কী হবে তা স্কোপ নির্ধারণ করে। [প্রবেশ কী নিয়ে আনুষ্ঠানিক তুলনা](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) অনুমতির পার্থক্য সরাসরি জানায়।

| প্রবেশপথ | স্কোপ | লেখার ক্ষমতা | উপযুক্ত ব্যবহার |
|---|---|---:|---|
| **রিপোজিটরি প্রবেশ কী** | একটি রিপোজিটরি | না | এজেন্টের ডিফল্ট checkout |
| **প্রজেক্ট প্রবেশ কী** | একটি প্রজেক্টের রিপোজিটরিগুলো | না | ছোট রিপোজিটরি-গোষ্ঠীতে শুধু-পঠন কাজ |
| **ওয়ার্কস্পেস প্রবেশ কী** | একটি ওয়ার্কস্পেসের রিপোজিটরিগুলো | হ্যাঁ | আলাদা লেখার পরিকল্পনাসহ নিয়ন্ত্রিত পরিষেবা স্বয়ংক্রিয়করণ |
| **ব্যক্তিগত SSH কী** | একজন ব্যবহারকারীর অনুমোদিত রিপোজিটরি | ব্যবহারকারী অ্যাকাউন্ট অনুসরণ করে | ইন্টারেক্টিভ প্রশাসন |
| **API টোকেন** | ব্যবহারকারীভিত্তিক API স্কোপ ও অ্যাকাউন্টের প্রবেশাধিকার | স্কোপের ওপর নির্ভর করে | REST API পাঠ বা অস্থায়ী লেখার কাজ |

**সবচেয়ে ছোট কার্যকর সীমানা দিয়ে শুরু করুন।** একটি রিপোজিটরি যথেষ্ট হলে রিপোজিটরি কী নিন। কয়েকটি রিপোজিটরি একই প্রজেক্টে থাকলে এবং শুধু-পঠন যথেষ্ট হলে প্রজেক্ট কী নিন। ওয়ার্কস্পেস কীকে লেখার পরিচয় হিসেবে ধরুন, সুবিধাজনক ডিফল্ট হিসেবে নয়।

Bitbucket সেটিংসের উপযুক্ত পথ দিয়ে সবচেয়ে সীমিত কী তৈরি ও নিবন্ধন করুন:

1. একটি রিপোজিটরির জন্য Repository settings, Access keys, তারপর Add key খুলুন। পাবলিক কী পেস্ট করুন এবং কীটি শুধু-পঠন রাখুন।
2. কয়েকটি রিপোজিটরির একটি প্রজেক্ট-সীমাবদ্ধ পাঠ পরিচয় দরকার হলে Project settings, Access keys, তারপর Add key খুলুন।
3. অনুমোদিত লেখার নকশাসহ যৌথ ওয়ার্কস্পেসে কেবল ওয়ার্কস্পেস কী ব্যবহার করুন। ব্যক্তিগত ওয়ার্কস্পেসে একই ওয়ার্কস্পেস-স্তরের পথ নেই।
4. কী-র লেবেল, স্কোপ, পাবলিক কী-র fingerprint, মালিক ও ঘোরানোর তারিখ নথিভুক্ত করুন। ব্যক্তিগত কী 1Password-এ রাখুন।

নিবন্ধনের পরে একবার সুনির্দিষ্ট শুধু-পঠন সংযোগ পরীক্ষা চালান:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**প্রত্যাশিত ফল:** `HEAD`-এর জন্য একটি commit reference। পরীক্ষাহীন উদাহরণ। সফল ফল প্রমাণ করে অনুমোদিত একটি SSH পরিচয় নির্দিষ্ট রিপোজিটরিতে পৌঁছেছে। এটি প্রমাণ করে না যে নিবন্ধিত কীটি নির্বাচিত হয়েছে বা লেখার অনুমতি আছে। প্রতি রিপোজিটরিতে একটি কী কনফিগার করার পর পরীক্ষা আবার চালান।

ব্যক্তিগত কী সংরক্ষণ ও 1Password SSH Agent সম্মতি সম্পর্কে [1Password CLI এবং SSH Agent: AI এজেন্টের জন্য SSH কী সুরক্ষা](/articles/1password-cli-ssh-keys-mcp-agent-administration/) পড়ুন।

## “Bitbucket CLI” সঠিকভাবে সংজ্ঞায়িত করুন

**Bitbucket CLI** কথাটি প্রায়ই তিনটি আলাদা ইন্টারফেসকে এক করে ফেলে। এগুলো আলাদা রাখুন।

- **Git CLI:** `git clone` এবং `git fetch` SSH বা HTTPS দিয়ে রিপোজিটরি ডেটা স্থানান্তর করে। `git diff` স্থানীয় ফাইল বা revision তুলনা করে।
- **REST ক্লায়েন্ট:** `curl` বা পর্যালোচিত wrapper Bitbucket Cloud Representational State Transfer (REST) API কল করে। API হলো ডেটা বা কাজের অনুরোধ করার প্রোগ্রামগত ইন্টারফেস। [Bitbucket Cloud REST API reference](https://developer.atlassian.com/cloud/bitbucket/rest/) রিপোজিটরি, সোর্স, branch, pull request, pipeline ও status resource তালিকাভুক্ত করে।
- **Atlassian CLI:** `acli` হলো Atlassian-এর আনুষ্ঠানিক কমান্ড লাইন। এর [ভূমিকা](https://developer.atlassian.com/cloud/acli/guides/introduction/) পণ্যটি বর্ণনা করে, আর [কমান্ড রেফারেন্স](https://developer.atlassian.com/cloud/acli/reference/commands/) `admin`, `jira`, `feedback` ও `rovodev` পৃষ্ঠ তালিকাভুক্ত করে। রেফারেন্সে Bitbucket Cloud কমান্ড নেই।

**Atlassian-এর আনুষ্ঠানিক `acli` কমান্ড রেফারেন্সে Bitbucket Cloud কমান্ড নেই।** `acli bitbucket clone`-এর মতো কমান্ড বানিয়ে বলবেন না। Git কাজের জন্য Git এবং Bitbucket Cloud ডেটার জন্য REST API ব্যবহার করুন।

### ঐচ্ছিক Teamwork Graph CLI

**Atlassian Teamwork Graph CLI, বা `twg`, প্রকাশ করে।** এর [পরিচিতি](https://developer.atlassian.com/cloud/twg-cli/) এবং [কমান্ড ক্যাটালগ](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) Bitbucket কমান্ডের পরিবার নথিভুক্ত করে। সেটআপ কমান্ড:

```bash
twg setup
```

সেটআপ কমান্ড স্থানীয় প্রমাণীকরণ অবস্থা বদলায়। ঐচ্ছিক Bitbucket টোকেন কনফিগারেশনের জন্য ইনস্টল করা সংস্করণের prompt অনুসরণ করুন। CLI-এর Bitbucket টোকেন পথ Atlassian OAuth থেকে আলাদা। সুনির্দিষ্ট কমান্ডের syntax ইনস্টল করা সংস্করণ ও বর্তমান ক্যাটালগের সঙ্গে মিলিয়ে নিন। পরিবর্তনকারী কমান্ডের জন্য আলাদা profile, সীমিত টোকেন, পর্যালোচিত ইনস্টল করা skill এবং মানুষের অনুমোদন ব্যবহার করুন।

**প্রত্যাশিত ফল, পরীক্ষাহীন:** বিচ্ছিন্ন profile Bitbucket প্রমাণীকরণ সেটিংস পায়। সেটআপের আগে profile-এর আগের অবস্থা লিখে রাখুন। rollback-এর সময় ইনস্টল করা সংস্করণে নথিভুক্ত logout বা configuration removal পদ্ধতিতে সংরক্ষিত credential সরান।

তৃতীয় পক্ষের কোনো প্রকল্প নিজেকে Bitbucket CLI বললে এর সোর্স, release প্রক্রিয়া, checksum, update পথ, প্রমাণীকরণ প্রবাহ, চাওয়া scope, নেটওয়ার্ক গন্তব্য, লগ ব্যবস্থাপনা ও লেখার কমান্ড নিরীক্ষা করুন। পরিচিত binary নাম vendor support বা নিরাপদ অনুমতির প্রমাণ নয়।

## 1Password-এর নিয়ন্ত্রণে SSH কী রাখুন

[1Password SSH Agent](https://www.1password.dev/ssh/agent) 1Password-এ রাখা SSH কী Git ও SSH ক্লায়েন্টকে দেয়। ক্লায়েন্ট অনুমোদিত signing অনুরোধ করে। ব্যক্তিগত কী 1Password অ্যাপের ভেতরে থাকে, এবং অনুমোদিত ক্লায়েন্ট কী ব্যবহার করার আগে 1Password সম্মতি চায়।

[1Password CLI reference](https://www.1password.dev/cli/reference)-এর কাজ আলাদা। item, API token, service account ও স্বয়ংক্রিয়করণ সেটআপে নিয়ন্ত্রিত প্রবেশের জন্য `op` ব্যবহার করুন। SSH signing-এর জন্য SSH Agent ব্যবহার করুন। এজেন্টের কাজ সহজ করতে ব্যক্তিগত কী অস্থায়ী ফাইলে export করবেন না।

শুধু-পঠন কমান্ড দিয়ে স্থানীয় CLI ও agent অবস্থা পরীক্ষা করুন:

```bash
op --version
ssh-add -l
```

**প্রত্যাশিত ফল:** 1Password CLI-এর একটি সংস্করণ এবং সক্রিয় agent-এর এক বা একাধিক পাবলিক-কী fingerprint। পরীক্ষাহীন উদাহরণ। `ssh-add -l` খালি ফল দিলে নির্বাচিত agent socket দিয়ে কোনো কী পাওয়া যাচ্ছে না।

নতুন কী হলে 1Password-এ Ed25519 SSH Key item তৈরি করুন অথবা বিশ্বস্ত স্থানীয় প্রক্রিয়ায় তৈরি কী import করুন। উদ্দেশ্য, স্কোপ ও ঘোরানোর তারিখ অনুযায়ী label দিন। Bitbucket Cloud-এ শুধু পাবলিক কী যোগ করুন। [Linux-এ repository access key নির্দেশিকা](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) রিপোজিটরি সেটিংসের পথ ও শুধু-পঠন সীমা বর্ণনা করে।

## প্রথমে Bitbucket host key যাচাই করুন

SSH ব্যবহারকারী প্রমাণীকরণ সার্ভারের পরিচয় প্রমাণ করে না। প্রমাণীকরণ অনুরোধ পাঠানোর আগে ক্লায়েন্টকে Bitbucket Cloud-এর host key যাচাই করতে হবে। Atlassian-এর [SSH ও two-step verification নির্দেশিকা](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) পাবলিক host key তালিকাভুক্ত করে এবং known-host entry আনার আনুষ্ঠানিক endpoint দেখায়।

তুলনার জন্য পাবলিক host-key ডেটা আনুন:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**প্রত্যাশিত ফল:** `bitbucket.org`-এর OpenSSH `known_hosts` লাইন। পরীক্ষাহীন উদাহরণ। `~/.ssh/known_hosts`-এ লাইন যোগ করার আগে ফেরত আসা key বা fingerprint একটি স্বাধীন বিশ্বস্ত কপির সঙ্গে তুলনা করুন।

অনুমোদিত entry যোগ হলে কঠোর host checking ব্যবহার করুন:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**এজেন্ট চলার সময় বদলে যাওয়া host key গ্রহণ করবেন না।** চলা থামান, Bitbucket Cloud-এর বর্তমান host-key record যাচাই করুন এবং স্থানীয় `known_hosts` entry দেখুন। স্বয়ংক্রিয় গ্রহণ একটি key-ভিত্তিক নিরাপত্তা সীমানা সরিয়ে দেয়।

## প্রতি রিপোজিটরির জন্য একটি কী বাছুন

একটি ডিভাইসে প্রায়ই একাধিক Bitbucket key থাকে। বিস্তৃত SSH agent একটি সংযোগে অনেক পরিচয় দেয়। অল্প authentication attempt-সীমা থাকা সার্ভার বা নীতি আগের key ব্যর্থ হলে সঠিক key-টিও প্রত্যাখ্যান করতে পারে।

Atlassian-এর [এক ডিভাইসে একাধিক repository access key নির্দেশিকা](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) repository Git configuration ফাইলে `core.sshCommand` এবং global Git configuration-এ `includeIf` ব্যবহার করে। প্রতি রিপোজিটরিতে একটি কী ব্যবহারের জন্য একই ধরন অনুসরণ করুন।

ফাইলভিত্তিক বহনযোগ্য উদাহরণ:

```ini
# একটি স্থানীয় রিপোজিটরির ভেতরের .gitconfig
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

উপরের block হলো নির্দিষ্ট automation পরিচয়ের জন্য ফাইলভিত্তিক ব্যক্তিগত-কী ব্যতিক্রম। এটি 1Password SSH Agent কনফিগার করে না। 1Password SSH Agent-এর জন্য [1Password setup guide](https://www.1password.dev/ssh/get-started) থেকে প্ল্যাটফর্মভিত্তিক `IdentityAgent` বা `SSH_AUTH_SOCK` মান কনফিগার করুন। কিছু OpenSSH configuration agent identity selector হিসেবে `.pub` ফাইল ব্যবহার করে। ব্যবহারের আগে প্ল্যাটফর্ম সমর্থন নিশ্চিত করুন। ফাইলভিত্তিক সেটআপে মিলে যাওয়া ব্যক্তিগত-কীর path লাগে। ব্যক্তিগত-key উপাদান চাওয়া কমান্ডে `.pub` ফাইল দেবেন না এবং ব্যক্তিগত ব্যক্তিগত কী export করবেন না।

স্থানীয় clone-এর একটি নির্দিষ্ট কী দরকার হলে স্পষ্ট repository configuration ব্যবহার করুন। একই প্রবেশসীমার একাধিক clone একটি directory-তে থাকলে `includeIf` ব্যবহার করুন। [একাধিক key নির্দেশিকা](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) Bitbucket workflow-এর দুই সেটিংস দেখায়।

SSH দিয়ে Git clone করুন:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**প্রত্যাশিত ফল:** Git `<local-directory>` তৈরি করে এবং `bitbucket.org` দিয়ে রিপোজিটরি আনে। পরীক্ষাহীন উদাহরণ। repository access key শুধু clone ও pull অনুমতি দেয়।

## সীমিত REST পাঠের জন্য API token ব্যবহার করুন

Git পরিবহনের জন্য SSH ব্যবহার করুন। Git পরিবহনের বাইরের metadata বা কাজের জন্য REST API ব্যবহার করুন। [API token permission নির্দেশিকা](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) Read, Write, Admin ও Delete-এর মতো repository scope তালিকাভুক্ত করে। Repository Read-এর মান `read:repository:bitbucket`; এতে pull request প্রবেশ অন্তর্ভুক্ত নয়।

পাঠ স্বয়ংক্রিয়করণের জন্য লক্ষ্য endpoint সমর্থন করলে Bitbucket repository বা project access token অগ্রাধিকার দিন। ব্যবহারকারীভিত্তিক API token ব্যবহারকারীর অ্যাকাউন্টের বিস্তৃত প্রবেশ ধরে রাখে। কাজের record-এ বিস্তৃত সীমা উল্লেখ থাকলেই workspace access token ব্যবহার করুন। token-এর ধরন বাছার আগে [Bitbucket access-token নির্দেশিকা](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) দেখুন।

এজেন্টের পাঠপথে `read:repository:bitbucket` দিয়ে শুরু করুন। এজেন্টের pull request ডেটা দরকার হলেই `read:pullrequest:bitbucket` যোগ করুন। কাজের record endpoint ও ফল উল্লেখ করলেই workspace বা pipeline scope যোগ করুন। Write ও admin scope-এর জন্য আলাদা অনুমোদনপথ লাগবে।

প্রতিটি API token এক উদ্দেশ্যে তৈরি করুন, মেয়াদ শেষের তারিখ দিন, rotation record-এ তারিখ রাখুন এবং মেয়াদ শেষ হওয়ার আগে token বদলান। Atlassian-এর [API token তৈরির নির্দেশিকা](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) নাম, মেয়াদ, app নির্বাচন ও scope চায়। তৈরির পর token একবার দেখা যায়।

মানটি 1Password বা পরিচালিত runtime secret-এ রাখুন। remote URL-এ দেবেন না। শুধু একটি পাঠের জন্য প্রয়োজনীয় process-এ environment variable দিয়ে bearer token পাঠান:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

`/path/to/agent.env` রিপোজিটরির বাইরে রাখুন। ফাইলে `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`-এর মতো reference রাখুন। `op run` reference সমাধান করে subprocess চলাকালে curl child process-কে মান দেয়। এতে child process environment variable-এর মান পড়তে বা লগে লিখতে বাধা পায় না। placeholder-কে সরাসরি token দিয়ে বদলাবেন না।

**প্রত্যাশিত ফল:** নির্বাচিত রিপোজিটরির JSON metadata। পরীক্ষাহীন উদাহরণ। placeholder যেন commit করা ফাইল বা লগে কখনো সত্যিকারের token না হয়।

দীর্ঘ automation-এর জন্য সমর্থিত CLI বা service-account প্রবাহে 1Password-কে process environment-এ secret দিতে দিন। token-এর মেয়াদ কাজের সঙ্গে সামঞ্জস্য রাখুন। কাজ আগে শেষ হলে বা host-এর মালিকানা বদলালে token বাতিল করুন।

## MCP-কে ছোট পাঠ-সারফেস দিন

নতুন সার্ভার পর্যালোচনায় [বর্তমান MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) এবং এর [authorization নিয়ম](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) ব্যবহার করুন। HTTP server-এ token audience পরীক্ষা এবং 401 ও 403 response-এর স্পষ্ট ব্যবস্থাপনা লাগবে।

MCP host ব্যবহারকারীর সম্মতি নেয়। client একটি server-এর সঙ্গে সংযোগ রাখে। server tool, resource বা prompt প্রকাশ করে। উৎস, পরিবহন, account ও permission পর্যালোচনা না হওয়া পর্যন্ত server-কে অবিশ্বস্ত কোড হিসেবে ধরুন।

পরের অনুচ্ছেদের 2025-06-18 specification URL ঐতিহাসিক সংস্করণ। নতুন পর্যালোচনায় বর্তমান 2026-07-28 specification ব্যবহার করুন।

[MCP specification](https://modelcontextprotocol.io/specification/2025-06-18) MCP host, client ও server-এর যোগাযোগ নির্ধারণ করে। server protocol দিয়ে tool, resource বা prompt প্রকাশ করে। MCP সংযোগের ধরন নির্দিষ্ট করে। তবে host, server বাস্তবায়ন, account, token scope ও অনুমোদন নীতিই নির্ধারণ করে কোন জায়গায় call পৌঁছায়।

Git ও Bitbucket Cloud REST API-এর ওপর সীমিত adapter হিসেবে MCP server ব্যবহার করুন।

token forwarding, server-side request forgery (SSRF) এবং confused-deputy আচরণ থেকে adapter-কে সুরক্ষিত করুন। SSRF-এ server অনিচ্ছিত গন্তব্যে request পাঠায়। confused-deputy আচরণে server caller-এর হয়ে বিস্তৃত অধিকার ব্যবহার করে। ক্ষতিকর স্থানীয় server, অনিরাপদ OAuth redirect এবং অতিরিক্ত বড় source-data response থেকেও সুরক্ষা দিন। অনুমোদিত Bitbucket origin ও repository identifier স্থির করুন। আলাদা operating-system user-এর অধীনে sandbox-এ স্থানীয় server চালান। tool result ও log-এ secret গোপন করুন।

এই অংশে নকশা বর্ণনা করা হয়েছে, পরীক্ষিত MCP configuration নয়। এখানে client, server, transport, version বা fixture নির্দিষ্ট নেই। production repository-তে agent যুক্ত করার আগে আলাদা test profile-এ একটি শুধু-পঠন server যাচাই করুন।

পাঠ টুলের উদাহরণ:

| টুল | সীমাবদ্ধ ফল |
|---|---|
| **`get_repository_metadata`** | একটি রিপোজিটরির metadata ফেরত দেয় |
| **`read_source_file`** | নির্দিষ্ট revision-এ একটি path পড়ে |
| **`list_branches`** | একটি রিপোজিটরির branch তালিকাভুক্ত করে |
| **`get_pull_request`** | token-এ pull request read scope থাকলে একটি pull request ফেরত দেয় |
| **`get_build_status`** | একটি commit-এর status data ফেরত দেয় |

এই নামগুলো নকশা বোঝায়। এগুলো Atlassian command নয়। arbitrary URL, shell command, raw token, ব্যক্তিগত-key export request বা সীমাহীন repository identifier গ্রহণ থেকে server-কে আটকান।

চার স্তরে permission সেট করুন:

1. **Bitbucket Cloud:** Git-এর জন্য repository বা project read key এবং REST পাঠের জন্য সবচেয়ে ছোট API token scope।
2. **1Password:** কাজের জন্য একটি vault বা service account, ব্যক্তিগত-key export পথ ছাড়া।
3. **MCP server:** read tool allowlist, নির্দিষ্ট Bitbucket Cloud endpoint, input validation, timeout limit এবং গোপন তথ্য মুছে ফেলা log।
4. **MCP host:** server এবং লেখার ক্ষমতাসম্পন্ন প্রতিটি কাজের জন্য ব্যবহারকারী অনুমোদন নিন; default profile-এ write tool বন্ধ রাখুন।

*MCP tool তালিকা আবিষ্কার প্রমাণ করে। এটি authorization, সঠিক scope, নিরাপদ input handling বা সঠিক ফল প্রমাণ করে না।*

## এজেন্ট কর্মপ্রবাহ সাজান

কর্মপ্রবাহ স্পষ্ট রাখুন। প্রতিটি ধাপ পরের ধাপের জন্য প্রমাণ তৈরি করে।

| ধাপ | এজেন্টের কাজ | অনুমতি | মানুষের অনুমোদন |
|---|---|---|---|
| **প্রস্তুতি** | configuration, host-key record, key label, token scope ও মেয়াদ পড়া | স্থানীয় পাঠ | সেটআপ record অনুমোদন |
| **পরিদর্শন** | SSH দিয়ে Git clone বা fetch এবং REST metadata query | repository ও API পাঠ | সেটআপের পর কিছু নয় |
| **বিশ্লেষণ** | অনুমোদিত tool দিয়ে file, branch, pull request ও build status পড়া | শুধু-পঠন MCP tool | সীমিত পাঠের জন্য কিছু নয় |
| **পরিবর্তন প্রস্তুত** | স্থানীয় workspace-এ patch, branch plan বা pull request draft তৈরি | শুধু স্থানীয় লেখা | diff ও লক্ষ্য পর্যালোচনা |
| **লেখা অনুমোদন** | নির্দিষ্ট remote action, scope ও rollback পথ দেখানো | এখনও remote write নয় | মানুষের অনুমোদন |
| **লেখা সম্পাদন** | branch push, pull request তৈরি বা write endpoint call | স্বল্পমেয়াদি write identity | প্রতিটি কাজ নিশ্চিত করুন |
| **যাচাই** | তৈরি হওয়া commit, pull request বা status পড়া | আবার শুধু-পঠন | প্রত্যাশিত ফল নিশ্চিত করুন |

ডিফল্ট agent profile **বিশ্লেষণ** বা **পরিবর্তন প্রস্তুত** ধাপে থামা উচিত। আলাদা write profile-এ আলাদা token বা key, স্বল্প মেয়াদ, নির্দিষ্ট লক্ষ্য এবং approval prompt থাকা উচিত। repository access key write ধাপ করতে পারে না, যা কার্যকর প্রযুক্তিগত সীমানা তৈরি করে।

## Rollback ও অপসারণ

প্রথমে প্রবেশাধিকার সরিয়ে তারপর স্থানীয় configuration পরিষ্কার করুন:

1. মিল থাকা Bitbucket settings page থেকে repository, project বা workspace access key সরান।
2. মিল থাকা Bitbucket security page থেকে repository, project, workspace বা user API token বাতিল করুন।
3. ইনস্টল করা CLI version-এর নথিভুক্ত [প্রমাণীকরণ পদ্ধতি](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) দিয়ে সংরক্ষিত Teamwork Graph credential সরান। আগের credential শুধু অনুমোদিত secret manager-এ রাখুন। যাচাই করুন বিচ্ছিন্ন profile-এ test credential আর নেই।
4. পরীক্ষা শেষে repository `.gitconfig` file ও তার `includeIf` entry সরান। সম্পর্কহীন Git configuration অক্ষত রাখুন।
5. পরীক্ষার জন্য যোগ করা শুধু যাচাইকৃত Bitbucket host-key line সরান। অন্য অনুমোদিত host key রাখুন।
6. বাইরের `agent.env` file ও অস্থায়ী output সরান। host configuration থেকে MCP server entry সরিয়ে host restart করুন।

প্রতিটি অপসারণ, অপারেটর ও সময় লিখে রাখুন। অপ্রত্যাশিত log, process record বা transcript-এ মান দেখা গেলে key বা token ঘোরান।

## স্থানীয় reference হালনাগাদসহ দূরবর্তী পাঠের চক্র

নিয়মিত repository পরীক্ষা করতে ছোট একটি চক্র ব্যবহার করুন:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` হলো repository-র বর্তমানে checkout করা reference। সফল ফল প্রমাণ করে অনুমোদিত SSH identity নির্দিষ্ট repository-তে পৌঁছেছে। কোন key নির্বাচিত হয়েছে বা push access আছে কি না তা প্রমাণ করে না।

**প্রত্যাশিত ফল:** fetch result, branch status ও একটি commit line। পরীক্ষাহীন উদাহরণ। `fetch` remote-এ কিছু লেখে না, তবে local reference ও `FETCH_HEAD` হালনাগাদ করে। চক্রটি push করে না বা branch বদলায় না।

MCP server-এর নামযুক্ত operation দিয়ে একই read boundary প্রকাশ করা উচিত। স্থানীয় shell wrapper বা MCP tool request পাঠানোর আগে write verb প্রত্যাখ্যান করবে। tool name, repository placeholder, revision, result class ও সময় লগ করুন। কাজের জন্য একটি file স্পষ্টভাবে দরকার না হলে token, cookie, ব্যক্তিগত path ও file content গোপন করুন।

## সমস্যা সমাধান

### `Permission denied (publickey)`

সক্রিয় agent socket, নির্বাচিত public key, repository access-key entry এবং `IdentitiesOnly` পরীক্ষা করুন। লক্ষ্য repository বা project-এ repository key থাকতে হবে। ব্যক্তিগত key-এর জন্য account permission দরকার। workspace access key-এর write boundary আলাদা।

### ভুল repository key দেওয়া হচ্ছে

প্রতি repository-তে `core.sshCommand` দিয়ে একটি key ব্যবহার করুন, অথবা `includeIf` নিয়ন্ত্রিত directory-তে clone গোষ্ঠীবদ্ধ করুন। `ssh-add -l` দিয়ে agent key তালিকাভুক্ত করুন। অনেক 1Password key থাকলে স্পষ্ট identity selector বা 1Password SSH bookmark ব্যবহার করুন। [1Password Agent guide](https://www.1password.dev/ssh/agent)-এ key সংখ্যা ও bookmark বিবেচনা আছে।

### SSH বদলে যাওয়া host key জানায়

agent থামান। প্রথম পদক্ষেপ হিসেবে `known_hosts` মুছবেন না। স্বাধীন channel দিয়ে বর্তমান Bitbucket Cloud host-key record ও স্থানীয় entry তুলনা করুন। তুলনা মেলার পরেই entry সরান বা প্রতিস্থাপন করুন।

### API `401` বা `403` দেয়

token-এর মেয়াদ, ধরন, endpoint scope এবং account বা workspace boundary পরীক্ষা করুন। repository read scope-এ pull request নেই। write endpoint-এর জন্য write scope ও অনুমোদিত write profile লাগবে। ব্যর্থ endpoint চিহ্নিত না করে scope বাড়াবেন না।

### API repository data দেয় কিন্তু pull request দেয় না

নতুন বা ঘোরানো token-এ সর্বনিম্ন pull request read scope যোগ করুন। শুধু-পঠন MCP server-এর জন্য বিস্তৃত user token পুনর্ব্যবহার করবেন না।

### MCP server tool দেখায় কিন্তু call ব্যর্থ হয়

server registration, connection, tool discovery, execution ও result verification আলাদা করে দেখুন। token না দেখিয়ে server log পরীক্ষা করুন। endpoint ও input shape যাচাই করুন। সংযোগ পরীক্ষা করে একবার retry করুন। দ্বিতীয় call ব্যর্থ হলে কাজ অসম্পূর্ণ চিহ্নিত করুন।

### তৃতীয় পক্ষের Bitbucket CLI বিস্তৃত প্রবেশ চায়

ইনস্টল থামান। চাওয়া প্রবেশ কাজের record-এর সঙ্গে তুলনা করুন। source, release signature বা checksum, নেটওয়ার্ক গন্তব্য, secret storage ও লেখার আচরণ পর্যালোচনা করুন। Atlassian CLI-এর আনুষ্ঠানিক command reference তৃতীয় পক্ষের Bitbucket binary সমর্থন প্রমাণ করে না।

## পরবর্তী ধাপ

repository বা project scope, key label, host-key যাচাইয়ের তারিখ, API scope, token মেয়াদ, 1Password মালিক, MCP tool allowlist, log policy ও write approver নিয়ে সংক্ষিপ্ত access record তৈরি করুন।

transcript-এ placeholder রেখে একটি শুধু-পঠন clone, একটি REST metadata পাঠ এবং একটি MCP tool পাঠ চালান। ফল তুলনা করুন। record ও log পর্যালোচনা না হওয়া পর্যন্ত agent profile শুধু-পঠন রাখুন।

লেখার কাজ এলে আগে স্থানীয় diff প্রস্তুত করুন। লক্ষ্য branch, বদলানো path, অনুরোধ করা API method, token scope ও rollback ধাপ দেখান। সঠিক কাজটিতে মানুষের অনুমোদনের পরেই আলাদা স্বল্পমেয়াদি write identity ব্যবহার করুন।
