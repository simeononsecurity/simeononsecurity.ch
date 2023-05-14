---
title: "Avui he après sobre CVE-2020-17049 i l'activació basada en testimonis de Windows"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**El que SimeonOnSecurity ha après i ha trobat interessant avui**

SimeonOnSecurity va conèixer recentment dos temes en l'àmbit de la seguretat informàtica: CVE-2020-17049, també conegut com l'atac Kerberos Bronze Bit, i l'activació basada en fitxes de Windows.

El Kerberos Bronze Bit Attack, tal com s'explica en una sèrie de publicacions de blog de Netspi i en una publicació de Trimarcsecurity, és una vulnerabilitat del protocol d'autenticació Kerberos. Aquesta vulnerabilitat podria permetre que un atacant comprometi un Active Directory, que és un dipòsit central d'informació sobre els usuaris, ordinadors i altres recursos d'una organització. El desplegament dels canvis de Kerberos S4U per abordar aquesta vulnerabilitat es tracta en un article de suport de Microsoft.

L'activació basada en testimonis de Windows és un mètode per activar els productes de Windows, tal com es descriu en un article de documentació de Microsoft. El procés d'activació es realitza mitjançant l'script SLMGR.vbs, tal com s'explica en un article complet a ss64.com. Una publicació del fòrum a Microsoft Technet proporciona més informació sobre l'activació basada en testimonis empresarials de Windows 10.

## CVE-2020-17049 - Atac de Kerberos Bronze Bit:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Activació basada en fitxes de Windows:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Vídeos d'interès:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
