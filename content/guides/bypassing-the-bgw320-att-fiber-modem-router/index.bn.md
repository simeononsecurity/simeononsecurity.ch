---
title: "BGW-320 বাইপাস করা: একটি Azores COTS ONT ব্যবহার করা - একটি ধাপে ধাপে নির্দেশিকা"
draft: false
toc: true
date: 2023-04-30
description: "কীভাবে BGW-320 বাইপাস করবেন এবং আপনার ISP-এর নেটওয়ার্কের সাথে সংযোগ করতে Azores-এর তৈরি একটি COTS ONT ব্যবহার করবেন তা এই সহজ-অনুসরণযোগ্য গাইডের মাধ্যমে শিখুন।"
tags: ["COTS ONT", "BGW-320", "অ্যাজোরস", "ফাইবার", "অন্তর্জাল", "XGS-PON", "ইথারনেট", "আইপি পাসথ্রু", "কাস্টমাইজেশন", "আইএসপি", "অন আইডি", "MAC ঠিকানা", "সরঞ্জাম আইডি", "ইমেজ সংস্করণ", "হার্ডওয়্যার সংস্করণ", "টেলনেট", "CLI আবেদন", "ওয়েব GUI", "কারখানা কনফিগারেশন মোড", "উপযুক্ততা বিষয়"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "ব্যাকগ্রাউন্ডে একটি ফাইবার তারের সাথে একটি COTS ONT ধরে থাকা একজন কার্টুন প্রযুক্তিবিদ৷"
coverCaption: ""
---

## কীভাবে BGW-320 বাইপাস করবেন এবং একটি Azores WAG-D20 ব্যবহার করবেন

ফাইবারযুক্ত বেশিরভাগ লোকেরই ইন্টারনেটের সাথে সংযোগ করার দুটি উপায় রয়েছে - একটি ONT থেকে ফাইবার, একটি গেটওয়েতে ইথারনেট বা সরাসরি গেটওয়েতে ফাইবার৷ এই নিবন্ধে, আমরা কীভাবে BGW-320 বাইপাস করব এবং Azores দ্বারা তৈরি একটি COTS ONT ব্যবহার করব তার উপর ফোকাস করব।

### প্রযুক্তিগত দিক

দ্য[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### ডিভাইস অ্যাক্সেস

ডিভাইসের ডিফল্ট আইপি ঠিকানা হল 192.168.1.1 এবং এর গেটওয়ে ঠিকানায় একটি পাবলিক আইপি ঠিকানা ব্যবহার করে ফ্যাক্টরি টাইপো আছে অর্থাৎ এটি 192.168.1.1 এর পরিবর্তে 192.162.1.1 দেখায়।

এটি বুট হয়ে গেলে, আপনাকে TTL সিরিয়াল ইন্টারফেস (115200 8N1) এ একটি লগইন প্রম্পট পেতে এন্টার চাপতে হবে। এই ডিভাইসটিতে একটি A/B ইমেজ সিস্টেম রয়েছে যার একটি ওভারলে পার্টিশন রয়েছে যা আপনার কাস্টমাইজ করা যেকোনো ফাইল ধারণ করে।
 
### শংসাপত্র

- `admin`/`ADMIN123!@#` - ওয়েব GUI-এর জন্য প্রশাসক লগইন
- 'অতিথি'/'স্বাগত' - অতিথি লগইন
- `পরীক্ষা`/`ডিফল্ট` - ফ্যাক্টরি লগইন

### ইথারনেট ইন্টারফেস

আপনার ক্লায়েন্টকে 10G ইথারনেট পোর্টের সাথে সংযুক্ত করুন এবং এটিকে 192.168.1.x/24 নেটওয়ার্কে একটি ঠিকানা দিয়ে কনফিগার করুন যেমন - 192.168.1.2/255.255.255.0৷

1-65535 থেকে একটি পোর্ট স্ক্যান চালানোর পরে, আপনি কিছু খোলা পোর্ট লক্ষ্য করবেন:

- পোর্ট `23` & `8009` - টেলনেট, লগইন প্রয়োজন, CLI অ্যাপ্লিকেশন চালায়।
- পোর্ট `10002` - অজানা
- পোর্ট `80` - WebUI, মাত্র দুটি ফাংশন

### ONT কাস্টমাইজ করা

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

এখন গুরুত্বপূর্ণ অংশটি আসে, যেমন আপনার আইএসপির নেটওয়ার্কের সাথে সামঞ্জস্যপূর্ণ করতে ডিভাইসের কিছু তথ্য পরিবর্তন করা।

প্রথমে, আপনার ISP গেটওয়ে বা ONT থেকে নিম্নলিখিত তথ্য নিন:

1. **ONT ID**
2. **MAC ঠিকানা**
3. **সরঞ্জাম আইডি**
4. **চিত্র সংস্করণ**
5. **হার্ডওয়্যার সংস্করণ**

দ্রষ্টব্য: এইগুলি OMCI মান এবং ওয়েব UI থেকে নয়৷

আপনার ব্যক্তিগত ONT (টেলনেট 192.168.1.1) তে টেলনেট, **`ডিফল্ট`** পাসওয়ার্ড ব্যবহার করে **`টেস্ট`** হিসাবে লগইন করুন এবং ফ্যাক্টরি কনফিগারেশন মোডে ড্রপ করতে 'টেস্ট' কমান্ডটি চালান।

'শো' কমান্ডের সাথে বর্তমানে সেট করা মানগুলি প্রদর্শন করুন:

- `gpon mac দেখান`
- `sn' দেখান
- `সরঞ্জাম আইডি দেখান`

একবার হয়ে গেলে, x আপনার ডিভাইসের মানগুলির সাথে প্রতিস্থাপন করে নিম্নলিখিত কমান্ডগুলি দিয়ে সেটিংস কাস্টমাইজ করুন:

- `সেট gpon mac xx:xx:xx:xx:xx:xx`
- `সেট করুন sn <এখানে ONT ID সন্নিবেশ করুন>`

HUMAX এর জন্য:

- `সেট ইকুইপমেন্ট আইডি "iONT320500G"`
- `config ONU-G_Version "BGW320-500_2.1"`

নোকিয়ার জন্য:

- `সেট ইকুইপমেন্ট আইডি "iONT320505G"`
- `config ONU-G_Version "BGW320-505_2.2"`

দ্রষ্টব্য: শেষ দুটি কমান্ড **`পরীক্ষা`** ব্যবহারকারী হিসাবে লগ ইন করা টেলনেট থেকে প্রয়োগ করা উচিত।

### রিবুট করুন এবং সত্যিকারের আইপি পাসথ্রু উপভোগ করুন

কাস্টমাইজ করার পরে, ONT রিবুট করুন এবং সত্যিকারের আইপি পাসথ্রু উপভোগ করুন।

### সমস্যা সমাধান এবং অতিরিক্ত পদক্ষেপ
এই বিষয়ে আরো তথ্যের জন্য, অনুগ্রহ করে দেখুন[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### উপসংহার

এই পদক্ষেপগুলি অনুসরণ করে কেউ সফলভাবে BGW-320 বাইপাস করতে পারে এবং তাদের ISP-এর নেটওয়ার্কে সংযোগ করতে Azores দ্বারা তৈরি COTS ONT ব্যবহার করতে পারে। যাইহোক, কমান্ডগুলি প্রবেশ করার সময় সতর্কতা অবলম্বন করুন এবং আপনার ডিভাইসের মানগুলির সাথে সঠিকভাবে 'x' প্রতিস্থাপন করা নিশ্চিত করুন অন্যথায়, আপনি সামঞ্জস্যপূর্ণ সমস্যার সম্মুখীন হতে পারেন যার ফলে সংযোগ ব্যর্থ হতে পারে।


