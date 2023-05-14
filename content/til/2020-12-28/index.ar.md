---
title: "تعرفت اليوم على CVE-2020-17049 والتنشيط المستند إلى Windows Token"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

** ما علمه SimeonOnSecurity ووجده مثيرًا للاهتمام اليوم **

علمت SimeonOnSecurity مؤخرًا عن موضوعين في مجال أمان الكمبيوتر: CVE-2020-17049 ، المعروف أيضًا باسم Kerberos Bronze Bit Attack ، والتنشيط المستند إلى Windows Token.

إن هجوم Kerberos Bronze Bit ، كما هو موضح في سلسلة من مشاركات المدونة بواسطة Netspi وفي منشور بواسطة Trimarcsecurity ، هو ثغرة أمنية في بروتوكول مصادقة Kerberos. قد تسمح هذه الثغرة الأمنية للمهاجمين بخرق Active Directory ، وهو مستودع مركزي للمعلومات حول مستخدمي المؤسسة وأجهزة الكمبيوتر والموارد الأخرى. تمت مناقشة نشر تغييرات Kerberos S4U لمعالجة مشكلة عدم الحصانة هذه في مقالة دعم Microsoft.

التنشيط المستند إلى Windows Token هو طريقة لتنشيط منتجات Windows ، كما هو موضح في مقالة وثائق Microsoft. يتم تنفيذ عملية التنشيط من خلال البرنامج النصي SLMGR.vbs ، كما هو موضح في مقال شامل على ss64.com. توفر إحدى مشاركات المنتدى على Microsoft Technet مزيدًا من المعلومات حول التنشيط المستند إلى Windows 10 Enterprise Token.

## CVE-2020-17049 - هجوم Kerberos Bronze Bit:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## التنشيط المستند إلى رمز Windows:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## مقاطع الفيديو المهمة:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
