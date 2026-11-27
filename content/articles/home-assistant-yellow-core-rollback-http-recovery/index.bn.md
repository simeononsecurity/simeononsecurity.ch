---
title: 'Home Assistant Core 2026.11 থেকে 2026.10.4-এ ফিরে যাওয়া: HTTP স্টোরেজ সংস্করণ 3 মেরামত'
date: 2026-11-15
lastmod: 2026-11-27
toc: true
draft: false
description: Yellow-এ Home Assistant Core 2026.11 থেকে 2026.10.4-এ ফিরে যাওয়ার পর HTTP স্টোরেজ সংস্করণ 3 ত্রুটি ঠিক করুন।
  এতে সুরক্ষিত কমান্ড ও যাচাইকৃত ফলাফল রয়েছে।
genre:
- হোম অটোমেশন
- সমস্যা সমাধান
tags:
- Home Assistant Yellow
- Home Assistant OS
- Core 2026.11 থেকে ফিরে যাওয়া
- Core 2026.10.4
- HTTP স্টোরেজ সংস্করণ 3
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: হলুদ কম্পিউটার বোর্ড, বিচ্ছিন্ন কনফিগারেশন সংযোগ এবং পুনরুদ্ধার করা ওয়েব ড্যাশবোর্ডের চিত্র
coverCaption: ''
---

Home Assistant Core 2026.11 আপডেট ব্যর্থ হওয়ার পর আমার Yellow CM4-এ 2026.10.4 সংস্করণ ফিরিয়ে আনে। Yellow নেটওয়ার্কে পৌঁছানো যাচ্ছিল, কিন্তু ড্যাশবোর্ড দেখানো বন্ধ করে দেয়। ফিরে যাওয়ার সময় HTTP সেটিংস ফাইলটি স্টোরেজ সংস্করণ 3.1-এ ছিল, অথচ Core 2026.10.4 সংস্করণ 2.2 সমর্থন করে। আমি ফাইলটি সংরক্ষণ করেছি, কঠোর যাচাইয়ের মধ্যে একটি কপি রূপান্তর করেছি, HTTP অ্যাক্সেস ফিরিয়েছি, তারপর Core-কে 2026.11.1-এ আপডেট করেছি।

<!--more-->

## মূল বিষয়গুলো

- **অমিল নিশ্চিত করুন।** Core লগের ত্রুটির সঙ্গে ইনস্টল করা রিলিজ ও HTTP স্টোরেজ সংস্করণ মিলিয়ে দেখুন।
- **ফাইলটি সংরক্ষণ করুন।** পুনরুদ্ধারের আগে অপরিবর্তিত কপি এবং ডিভাইসের বাইরে একটি ব্যাকআপ রাখুন।
- **ফল যাচাই করুন।** Core-এর অবস্থা, সংরক্ষিত লিসেনার, ড্যাশবোর্ড এবং ইনস্টল করা সংস্করণ পরীক্ষা করুন।

**এই নির্দিষ্ট সমস্যার সমাধান:** [HTTP ফাইলটি সংরক্ষণ করুন](#preserve-recovery-options), [সংস্করণ 2.2-এর একটি প্রার্থী তৈরি করে যাচাই করুন](#apply-the-tested-fix-for-version-31), [Core বন্ধ করার পর সেটি ইনস্টল করুন](#apply-the-tested-fix-for-version-31), এবং [আপডেটের ফল যাচাই করুন](#verify-the-update-outcome)। রূপান্তরটি মূল ফিল্ডগুলো পরীক্ষা করে, অমিল পেলে থেমে যায়। পরীক্ষা না করা HTTP ফাইলে এটি প্রয়োগ করবেন না।

## শুরু করার আগে

আপনার Yellow CM4-এ সরাসরি প্রবেশাধিকার, একটি USB-C ডেটা কেবল, সচল সিরিয়াল কনসোল এবং ব্যবহারযোগ্য ব্যাকআপ বা সংরক্ষিত কনফিগারেশন দরকার। হাতে-কলমে পদ্ধতিতে হোস্ট শেলের অ্যাক্সেস ও JSON সতর্কভাবে পরীক্ষা করতে হবে। সমস্যা নির্ণয় ও মেরামতের জন্য অন্তত 30 মিনিট রাখুন। বড় ইনস্টলেশনে Core চালু হওয়া ও ব্যাকআপ পুনরুদ্ধারে আরও সময় লাগে।

## সমস্যাটি শনাক্ত করুন

Core লগে নির্ণায়ক ত্রুটিটি দেখা গিয়েছিল:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

পুরোনো Core রিলিজ `http` লোড করতে পারেনি। HTTP-এর ওপর নির্ভরশীল ফ্রন্টএন্ড ও অন্যান্য কম্পোনেন্টও কাজ করেনি। রাউটারের লিজ পাওয়া বা Observer পৃষ্ঠা সচল থাকা ড্যাশবোর্ড অ্যাক্সেস প্রমাণ করে না। [Home Assistant Core-এর সমস্যা #190583](https://github.com/home-assistant/core/issues/190583)-এ Yellow-সহ একাধিক ইনস্টলেশনে একই রোলব্যাক ব্যর্থতার বিবরণ আছে। [ইস্যুতে আমার মন্তব্যে](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) এই Yellow-এ পরীক্ষিত পুনরুদ্ধার ও Core-এর চূড়ান্ত অবস্থা লেখা আছে।

**ওয়েব বন্ধ হওয়ার কারণ:** Core 2026.11 `.storage/http`-কে 3.1 ফরম্যাটে লিখেছিল। রোলব্যাকে Core 2026.10.4 ফিরলেও সামঞ্জস্যপূর্ণ HTTP ফাইল ফেরেনি। Core 2026.10.4 স্টোরেজ সংস্করণ 3 প্রত্যাখ্যান করে। এই Yellow-এ সংরক্ষিত `intermediate_v6` প্রোফাইলটিও পুরোনো স্কিমার সঙ্গে মেলে না। প্রথম আপডেট কেন ব্যর্থ হয়ে রোলব্যাক ঘটায়, তা জানা যায়নি। 2026-11-15 তারিখে সংশ্লিষ্ট ইস্যুটি খোলা ছিল এবং আলোচনায় রক্ষণাবেক্ষণকারীর নিশ্চিত করা কোনো সমাধান ছিল না।

ফাইল বদলানোর আগে ইনস্টল করা Core রিলিজ ও HTTP স্টোর পরীক্ষা করুন:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

নিচের ফলাফলগুলোতে টাইমস্ট্যাম্প ও ব্যক্তিগত বিবরণ বাদ দিয়ে এই ঘটনার অবস্থা দেখানো হয়েছে:

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

নিচের পুনরুদ্ধার কমান্ডগুলো Supervisor-এর সংরক্ষিত লিসেনার ও HTTP ফাইল তুলনা করে, কিন্তু কোনো মান প্রকাশ করে না। অমিল হলে ফাইল বদলানোর আগে Core-এর প্রকৃত লিসেনার যাচাই করুন।

| সংকেত | অর্থ |
| --- | --- |
| Core স্টোরেজ সংস্করণ 2 সমর্থন করে, ফাইলে সংস্করণ 3 আছে | পুরোনো রিলিজ সংরক্ষিত HTTP সেটিংস লোড করতে পারবে না |
| HTTP ফাইল ও Supervisor তালিকায় ভিন্ন লিসেনার আছে | সমস্যার কারণ ধরার আগে Core-এর প্রকৃত লিসেনার পরীক্ষা করুন |
| মূল পৃষ্ঠা সাড়া দেয়, Core-এর অবস্থা এখনও STARTING | শুধু ফ্রন্টএন্ডের সাড়া Core-এর স্টার্টআপ শেষ হওয়া প্রমাণ করে না |

## পুনরুদ্ধারের বিকল্পগুলো সংরক্ষণ করুন {#preserve-recovery-options}

আরেকটি আপডেটের আগে Yellow-এর বাইরে ব্যবহারযোগ্য ব্যাকআপ রাখুন। [Home Assistant-এর ব্যাকআপ নির্দেশিকা](https://www.home-assistant.io/common-tasks/general/backups/) ক্লাউড ও ডিভাইসের বাইরের অবস্থান ব্যাখ্যা করে। এনক্রিপ্ট করা ব্যাকআপের জন্য তার পুনরুদ্ধার কী দরকার। এই স্টোরেজ অমিল নির্ণয়ের সময় NVMe ডেটা ডিস্ক মুছবেন না।

সম্পাদনার আগে HTTP ফাইলটি কপি করুন:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

কমান্ড ব্যর্থ হলে থামুন। একই নামে আগের পুনরুদ্ধার কপিটি অপরিবর্তিত রাখুন। নতুন নাম বেছে নিয়ে এগোনোর আগে পরীক্ষা পুনরাবৃত্তি করুন।

ড্যাশবোর্ড অপ্রাপ্য হলে Yellow-এর সিরিয়াল কনসোল ব্যবহার করুন। [Linux ও macOS-এর জন্য Nabu Casa নির্দেশিকা](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS)-তে USB-C সংযোগ ও JP1 UART-এর অবস্থান দেখানো হয়েছে। আপনার হার্ডওয়্যারের CM4 নির্দেশনা অনুসরণ করুন।

## সংস্করণ 3.1-এর পরীক্ষিত সমাধান প্রয়োগ করুন {#apply-the-tested-fix-for-version-31}

পছন্দের পথ হলো আপডেটের আগের সামঞ্জস্যপূর্ণ HTTP ফাইল ব্যবহার করা। সম্পূর্ণ পুনরুদ্ধার উপযুক্ত হলে Home Assistant-এর নথিভুক্ত পদ্ধতিতে ব্যাকআপ ফিরিয়ে আনুন। একটি ফাইল আলাদা করলে সক্রিয় ফাইল প্রতিস্থাপনের আগে তার স্টোরেজ সংস্করণ ও সংরক্ষিত লিসেনার নিশ্চিত করুন। সামঞ্জস্যপূর্ণ HTTP ফাইল না থাকলে এই Yellow-এ নিচের কমান্ডগুলোই সরাসরি পরীক্ষিত সমাধান ছিল।

[ইস্যুর মূল অস্থায়ী সমাধান](https://github.com/home-assistant/core/issues/190583) `.storage/http` সরিয়ে রাখে এবং পুরোনো Core-কে নতুন ফাইল তৈরি করতে দেয়। পরের একটি [Yellow প্রতিবেদন](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119)-এ পুনরায় তৈরি ফাইলে ভিন্ন লিসেনার দেখা যায়। ওয়েব ইন্টারফেস ঠিক হয়েছে বলে ধরে নেওয়ার আগে নতুন ফাইল ও `ha core info` পরীক্ষা করুন।

আমার ইনস্টলেশনে `http:` YAML ব্লক বা কোনো অপেক্ষমাণ HTTP কনফিগারেশন ছিল না, আর স্থায়ী সেটিংসে TLS সার্টিফিকেট বা কীও ছিল না। সংরক্ষিত প্রোফাইলটি ছিল `intermediate_v6`। এই সীমিত অবস্থায় আমি আলাদা 2.2 সংস্করণের প্রার্থী বানিয়ে বর্তমান লিসেনার রেখেছিলাম:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

সক্রিয় ফাইল প্রতিস্থাপনের আগে ওপরের প্রতিটি কমান্ড সফল হতে হবে। `jq` ব্যর্থ হলে প্রার্থী ফাইল মুছে আবার চেষ্টা করার আগে সেটি পরীক্ষা করুন। [Core 2026.10.4-এর HTTP সোর্সে](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) স্টোরেজ সংস্করণ 2.2 নির্ধারিত এবং `intermediate` প্রোফাইল গ্রহণ করা হয়। [Core 2026.11.1-এর সোর্সে](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) সংস্করণ 3.1 ও সংস্করণযুক্ত প্রোফাইল নাম ব্যবহৃত হয়। ইনস্টল করা পুরোনো Core-এর `HTTP_STORAGE_SCHEMA` দিয়েও ইনস্টল করার আগে প্রার্থী যাচাই করেছি।

কনটেইনার চালু থাকা অবস্থায় ইনস্টল করা পুরোনো Core-এর স্কিমা পরীক্ষা চালান:

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("স্কিমা গৃহীত হয়েছে")
'
```

স্কিমা প্রার্থীকে প্রত্যাখ্যান করলে থামুন। এই ধাপে প্রতিটি ইন্টিগ্রেশন বা HTTP স্টোরের অপরীক্ষিত সব রূপ যাচাই হয় না।

এই প্রার্থীর জন্য স্কিমা পরীক্ষায় `স্কিমা গৃহীত হয়েছে` দেখা গিয়েছিল। অন্য যেকোনো ফল এ পুনরুদ্ধার পদ্ধতি থামায়।

এই হাতে করা রূপান্তরটি উল্লেখিত ফিল্ডগুলোর জন্য পরীক্ষা করা হয়েছিল। TLS সেটিংস, trusted proxies বা অপেক্ষমাণ কনফিগারেশন থাকলে আলাদা পর্যালোচনা দরকার। শুধু ওপরের সংস্করণ নম্বর বদলালে এমন প্রোফাইল থেকে যায় যা পুরোনো Core গ্রহণ করে না।

আমার ক্ষেত্রে Supervisor-এর একটি সক্রিয় Core কাজ ছিল এবং `ha core stop` প্রত্যাখ্যান করেছিল। হোস্ট কনসোল থেকে Core কনটেইনার থামিয়ে যাচাইকৃত প্রার্থী ইনস্টল করে আবার চালু করেছি:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

থামানোর পর কোনো কমান্ড ব্যর্থ হলে `docker start homeassistant` চালানোর আগে সক্রিয় HTTP ফাইল পরীক্ষা করুন। ফাইল বদলে গেলে তার সর্বশেষ বিষয়বস্তু থেকে নতুন প্রার্থী বানাতে হবে। এই ধাপের পর HTTP পৃষ্ঠা ফিরেছিল। শুধু HTTP সাড়া Core-এর স্টার্টআপ শেষ হওয়া প্রমাণ করেনি, তাই সিস্টেম উদ্ধার হয়েছে ধরে নেওয়ার আগে Supervisor-এর অবস্থা পরীক্ষা করেছি।

এই Yellow-এ `docker inspect -f '{{.State.Status}}' homeassistant` তখন `running` দেখিয়েছিল। আরেকটি আপডেটের অনুরোধের আগে `ha core info` ও ড্যাশবোর্ড পরীক্ষা করুন।

## আপডেটের ফল যাচাই করুন {#verify-the-update-outcome}

HTTP অ্যাক্সেস ফিরে আসার পর Core-কে 2026.11.1-এ আপডেট করেছি। ওই রিলিজের অনুরোধ করতে:

```bash
ha core update --version 2026.11.1
```

দীর্ঘ স্টার্টআপের পর কমান্ডটি ব্যর্থতার কথা জানায়। এরপর Supervisor Core-কে RUNNING হিসেবে লগ করে এবং `Successfully started Home Assistant 2026.11.1` বার্তা দেয়। অবস্থা পরীক্ষা করে দেখা যায় ইনস্টল করা রিলিজটি বর্তমান, HTTP ফাইল আবার সংস্করণ 3.1-এ স্থানান্তরিত হয়েছে, এবং পর্যবেক্ষণের সময় কনটেইনার একবারও রিস্টার্ট করেনি। লগইন করা ড্যাশবোর্ড লোড হয়েছে। **আপডেট কমান্ড ব্যর্থতার কথা বললেও চূড়ান্ত অবস্থা যাচাই করুন।**

আপনার সিস্টেমে দীর্ঘ আপডেটের পর রিলিজ, Supervisor-এর স্বাস্থ্য ও কনটেইনারের অবস্থা পরীক্ষা করুন:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

এই ঘটনায় প্রথম ও তৃতীয় কমান্ড থেকে নিচের পরিচয়মুক্ত ফলাফল পাওয়া গিয়েছিল:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

এরপর আপনার স্বাভাবিক স্থানীয় ঠিকানা দিয়ে ড্যাশবোর্ড খুলে সক্রিয় অবস্থা লোড হচ্ছে কি না দেখুন। পরের ব্যাকআপ সম্পন্ন হওয়া এবং স্বাভাবিক কাজ যাচাই না হওয়া পর্যন্ত সংরক্ষিত HTTP ফাইলটি রাখুন।

আমার Yellow-এর প্রমাণে প্রথম আপডেট ব্যর্থ হওয়ার কারণ প্রতিষ্ঠিত হয়নি। পরের কাজটির ব্যর্থতার বার্তাও কারণ জানায়নি। ইনস্টল করা রিলিজ ও সচল ড্যাশবোর্ড কমান্ড-লাইন বার্তার চেয়ে ফলাফলের ভালো প্রমাণ, কিন্তু কোন কারণে Supervisor কাজটিকে ব্যর্থ বলেছিল তা কোনোটিই ব্যাখ্যা করে না।

## পরবর্তী পদক্ষেপ

HTTP স্টোরেজ ত্রুটি থাকলে সংরক্ষিত ফাইল পরীক্ষা করুন, সামঞ্জস্যপূর্ণ ব্যাকআপ ফিরিয়ে আনুন অথবা এমন Core রিলিজ চালান যা ওই স্টোরেজ সংস্করণ পড়তে পারে। পুরোনো Core-এ সংস্করণ 3 ফাইল ফিরিয়ে আনলে একই সমস্যা হবে। Core RUNNING হলেও কিছু ডিভাইস অপ্রাপ্য থাকলে সেই ইন্টিগ্রেশনগুলো আলাদাভাবে পরীক্ষা করুন। পরের ব্যাকআপ সম্পন্ন হওয়া ও ড্যাশবোর্ড সচল থাকা পর্যন্ত পুনরুদ্ধার কপি এবং ক্লাউড ব্যাকআপ রাখুন।
