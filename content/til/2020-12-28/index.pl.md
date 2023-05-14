---
title: "Dziś dowiedziałem się o CVE-2020-17049 i Windows Token-Based Activation"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**Co SimeonOnSecurity dowiedział się i uznał za interesujące dzisiaj**

SimeonOnSecurity dowiedział się ostatnio o dwóch tematach z dziedziny bezpieczeństwa komputerowego: CVE-2020-17049, znanym również jako Kerberos Bronze Bit Attack, oraz Windows Token-Based Activation.

Kerberos Bronze Bit Attack, jak wyjaśniono w serii wpisów na blogu Netspi oraz w poście Trimarcsecurity, jest luką w protokole uwierzytelniania Kerberos. Luka ta może potencjalnie pozwolić atakującemu na zaatakowanie Active Directory, który jest centralnym repozytorium informacji o użytkownikach, komputerach i innych zasobach organizacji. Wdrożenie zmian Kerberos S4U w celu usunięcia tej luki zostało omówione w artykule pomocy technicznej firmy Microsoft.

Windows Token-Based Activation to metoda aktywacji produktów Windows, opisana w artykule w dokumentacji firmy Microsoft. Proces aktywacji odbywa się za pomocą skryptu SLMGR.vbs, jak wyjaśniono w obszernym artykule na ss64.com. Post na forum Microsoft Technet zawiera więcej informacji na temat Windows 10 Enterprise Token Based Activation.

## CVE-2020-17049 - Kerberos Bronze Bit Attack:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Windows Token-Based Activation:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Videos of Interest:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
