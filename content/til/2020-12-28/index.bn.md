---
title: "আজ আমি CVE-2020-17049 এবং উইন্ডোজ টোকেন-ভিত্তিক অ্যাক্টিভেশন সম্পর্কে জানলাম"
date: 2020-12-27
toc: true
draft: false
---

**SimeonOnSecurity যা শিখেছে এবং আজকে আকর্ষণীয় মনে হয়েছে**

SimeonOnSecurity সম্প্রতি কম্পিউটার নিরাপত্তার ক্ষেত্রে দুটি বিষয় সম্পর্কে শিখেছে: CVE-2020-17049, যা Kerberos Bronze Bit Attack নামেও পরিচিত, এবং Windows টোকেন-ভিত্তিক অ্যাক্টিভেশন।

কারবারোস ব্রোঞ্জ বিট অ্যাটাক, যেমনটি নেটস্পির ব্লগ পোস্টের একটি সিরিজে এবং ট্রাইমার্কসিকিউরিটির একটি পোস্টে ব্যাখ্যা করা হয়েছে, কার্বেরোস প্রমাণীকরণ প্রোটোকলের একটি দুর্বলতা। এই দুর্বলতা সম্ভাব্যভাবে একজন আক্রমণকারীকে একটি সক্রিয় ডিরেক্টরির সাথে আপস করার অনুমতি দিতে পারে, যা একটি প্রতিষ্ঠানের ব্যবহারকারী, কম্পিউটার এবং অন্যান্য সংস্থান সম্পর্কে তথ্যের জন্য একটি কেন্দ্রীয় সংগ্রহস্থল। এই দুর্বলতা মোকাবেলায় Kerberos S4U পরিবর্তনগুলি একটি Microsoft সমর্থন নিবন্ধে আলোচনা করা হয়েছে।

উইন্ডোজ টোকেন-ভিত্তিক অ্যাক্টিভেশন হল উইন্ডোজ পণ্যগুলি সক্রিয় করার একটি পদ্ধতি, যেমনটি Microsoft ডকুমেন্টেশন নিবন্ধে বর্ণিত হয়েছে। সক্রিয়করণ প্রক্রিয়াটি SLMGR.vbs স্ক্রিপ্টের মাধ্যমে সম্পাদিত হয়, যেমনটি ss64.com-এর একটি বিস্তৃত নিবন্ধে ব্যাখ্যা করা হয়েছে। মাইক্রোসফ্ট টেকনেটের একটি ফোরাম পোস্ট Windows 10 এন্টারপ্রাইজ টোকেন ভিত্তিক অ্যাক্টিভেশন সম্পর্কে আরও তথ্য সরবরাহ করে।

## CVE-2020-17049 - Kerberos Bronze Bit Attack:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## উইন্ডোজ টোকেন-ভিত্তিক অ্যাক্টিভেশন:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## আগ্রহের ভিডিও:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
