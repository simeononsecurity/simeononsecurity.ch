---
title: "ChromiumADMX: Chromium ব্রাউজারের জন্য সঠিক ADMX টেমপ্লেট"
date: 2020-07-25
---


Chromium ব্রাউজারের জন্য সঠিক ADMX টেমপ্লেট

ক্রোমিয়াম, একটি কোম্পানি হিসাবে, ক্রোমিয়াম ব্রাউজারের জন্য ADMX টেমপ্লেট প্রকাশ করতে ব্যর্থ হয়েছে যা Google Chrome টেমপ্লেটগুলির মতো একই সময়ে ইনস্টল করা যেতে পারে৷
এটি মাথায় রেখে, আমরা ক্রোমিয়াম ব্রাউজারের রেজিস্ট্রি পাথকে প্রতিফলিত করার জন্য Google Chrome ADMX টেমপ্লেটগুলিকে সংশোধন করেছি এবং GPO-তে Google ADMX ফোল্ডারে ট্যান্ডামে স্থাপন করেছি৷

**এই নীতির সংজ্ঞাগুলি একটি প্রাক-আলফা অবস্থায় রয়েছে। এগুলি শুধুমাত্র পরীক্ষার উদ্দেশ্যে ব্যবহার করা উচিত**

## প্রয়োজনীয় ফাইল ডাউনলোড করুন

** থেকে প্রয়োজনীয় ফাইল ডাউনলোড করুন[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## মন্তব্য

সংশোধিত Google Chrome নীতির সংজ্ঞা অনুযায়ী:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**দ্রষ্টব্য:** "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" এর পরিবর্তে "HKEY_LOCAL_MACHINE\Software\Policies\Chromium"

**দ্রষ্টব্য:** একই সময়ে SOS'es Chromium এবং Brave Browser ADMX টেমপ্লেট ইনস্টল করবেন না।

## কিভাবে ইনস্টল করতে হবে

1.) readme.md ছাড়া সব ফাইল কপি করুন "C:\Windows\PolicyDefinitions" এবং/অথবা "\\\domain.tld\domain\Policy\PolicyDefinitions" এ

2.) লাভ?




