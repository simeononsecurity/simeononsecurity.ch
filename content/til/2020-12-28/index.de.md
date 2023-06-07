---
title: "Heute habe ich über CVE-2020-17049 und die Token-basierte Windows-Aktivierung gelernt"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**Was SimeonOnSecurity heute erfahren und interessant gefunden hat**

SimeonOnSecurity hat sich kürzlich über zwei Themen aus dem Bereich der Computersicherheit informiert: CVE-2020-17049, auch bekannt als Kerberos Bronze Bit Attack, und Windows Token-Based Activation.

Der Kerberos-Bronze-Bit-Angriff ist eine Schwachstelle im Kerberos-Authentifizierungsprotokoll, die in einer Reihe von Blogbeiträgen von Netspi und in einem Beitrag von Trimarcsecurity erläutert wird. Diese Schwachstelle könnte es einem Angreifer ermöglichen, ein Active Directory zu kompromittieren, das ein zentrales Repository für Informationen über die Benutzer, Computer und anderen Ressourcen einer Organisation ist. Der Einsatz von Kerberos-S4U-Änderungen zur Behebung dieser Schwachstelle wird in einem Microsoft-Support-Artikel beschrieben.

Windows Token-Based Activation ist eine Methode zur Aktivierung von Windows-Produkten, die in einem Microsoft-Dokumentationsartikel beschrieben wird. Der Aktivierungsprozess wird über das Skript SLMGR.vbs durchgeführt, wie in einem umfassenden Artikel auf ss64.com erläutert wird. Ein Forumsbeitrag auf Microsoft Technet bietet weitere Informationen über die Token-basierte Aktivierung von Windows 10 Enterprise.

## CVE-2020-17049 - Kerberos Bronze Bit Attack:
- [CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
- [Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
- [Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Windows Token-basierte Aktivierung:
- [Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
- [SLMGR.vbs](https://ss64.com/nt/slmgr.html)
- [Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Videos von Interesse:
- [Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
- [Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
- [Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
- [Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
- [Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
- [Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
