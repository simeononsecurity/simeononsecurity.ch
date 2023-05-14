---
title: "Vandaag leerde ik over CVE-2020-17049 en Windows Token-Based Activation"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**Wat SimeonOnSecurity vandaag heeft geleerd en interessant vond**

SimeonOnSecurity heeft onlangs geleerd over twee onderwerpen op het gebied van computerbeveiliging: CVE-2020-17049, ook bekend als de Kerberos Bronze Bit Attack, en Windows Token-Based Activation.

De Kerberos Bronze Bit Attack, zoals uitgelegd in een serie blog posts van Netspi en in een post van Trimarcsecurity, is een kwetsbaarheid in het Kerberos authenticatieprotocol. Deze kwetsbaarheid zou een aanvaller in staat kunnen stellen een Active Directory, een centrale opslagplaats voor informatie over de gebruikers, computers en andere bronnen van een organisatie, te compromitteren. De inzet van Kerberos S4U wijzigingen om deze kwetsbaarheid te verhelpen wordt besproken in een Microsoft support artikel.

Windows Token-Based Activation is een methode om Windows-producten te activeren, zoals beschreven in een Microsoft-documentatieartikel. Het activeringsproces wordt uitgevoerd via het SLMGR.vbs-script, zoals uitgelegd in een uitgebreid artikel op ss64.com. Een forumbericht op Microsoft Technet biedt meer informatie over Windows 10 Enterprise Token Based Activation.

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

## Interessante video's:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
