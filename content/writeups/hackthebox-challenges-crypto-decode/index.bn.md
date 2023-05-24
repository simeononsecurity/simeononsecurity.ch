---
title: "HackTheBox - চ্যালেঞ্জ - ক্রিপ্টো - ডিকোড"
date: 2020-10-07
draft: false
description: "হ্যাক দ্যাবক্স ক্রিপ্টো চ্যালেঞ্জের সমাধান করতে এবং লুকানো পতাকা উন্মোচন করতে ফার্নেট এবং মালবোজ সাইফারকে কীভাবে ডিকোড করতে হয় তা শিখুন।"
tags: ["HackTheBox", "চ্যালেঞ্জ", "ক্রিপ্টো", "ডিকোড", "লেখা", "ফার্নেট সাইফার", "ম্যালবোজ সাইফার", "সিমেট্রিক এনক্রিপশন", "সাইবার নিরাপত্তা", "ক্রিপ্টোগ্রাফি", "অনুপ্রবেশ পরীক্ষা", "পাইথন", "নিরাপত্তা", "চ্যালেঞ্জ", "সিটিএফ", "পতাকা", "জোড়া লাগানো", "ডিক্রিপশন", "বেস64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "একটি কার্টুন হ্যাকার একটি বড় তালার পাশে দাঁড়িয়ে আছে যার এক হাতে একটি ফার্নেট লোগো চাবি রয়েছে এবং অন্য হাতে একটি মালবোজ লোগো চাবি রয়েছে যখন তালার ভিতরে একটি পতাকা দেখা যাচ্ছে"
coverCaption: ""
---

HackTheBox Crypto Decode চ্যালেঞ্জের একটি বিস্তারিত ওয়াক-থ্রু পান। তথ্যের দুটি স্ট্রিং দেওয়া, এই নিবন্ধটি আপনাকে একটি ফার্নেট সাইফার এবং একটি মালবোজ সাইফার ডিকোড করার প্রক্রিয়ার মাধ্যমে পতাকাটি প্রকাশ করার জন্য গাইড করে। সমাধানটি অর্জন করতে asecuritysite.com এবং base64decode.org দ্বারা প্রদত্ত সরঞ্জামগুলি ব্যবহার করুন৷

______

## প্রদত্ত ফাইল:

এই চ্যালেঞ্জে আপনাকে তথ্যের দুটি স্ট্রিং প্রদান করা হয়।

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
এবং
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## ওয়াক থ্রু:

প্রথম নজরে মনে হচ্ছে এটি এক ধরণের কী এবং কিছু সাইফার টেক্সট।
চারপাশে অনুসন্ধান করার পরে, আপনি দেখতে পাবেন যে এটি একটি ফার্নেট সাইফার।
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) আপনার জন্য এটি ডিকোড করার জন্য একটি দুর্দান্ত সরঞ্জাম রয়েছে।

উপরের তথ্য থেকে সরল পাঠ্য আপনাকে একটি base64 এনকোডেড স্ট্রিং দেয়

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

এটিকে ডিকোড করতে, আমরা প্রদত্ত টুল ব্যবহার করব [base64decode.org](https://www.base64decode.org/)

ডিকোডিং আবার আপনাকে নিম্নলিখিত দেয়:
```
ডি'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB{x_xxx_xxxx}
```

