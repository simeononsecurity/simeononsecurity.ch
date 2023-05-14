---
title: "Astăzi am aflat despre CVE-2020-17049 și activarea bazată pe token Windows"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**Ceea ce SimeonOnSecurity a învățat și a găsit interesant astăzi**

SimeonOnSecurity a aflat recent despre două subiecte din domeniul securității computerelor: CVE-2020-17049, cunoscut și sub numele de Kerberos Bronze Bit Attack, și Windows Token-Based Activation.

Atacul Kerberos Bronze Bit, așa cum este explicat într-o serie de postări pe blog de Netspi și într-o postare de Trimarcsecurity, este o vulnerabilitate în protocolul de autentificare Kerberos. Această vulnerabilitate ar putea permite unui atacator să compromită un Active Directory, care este un depozit central pentru informații despre utilizatorii unei organizații, computerele și alte resurse. Desfășurarea modificărilor Kerberos S4U pentru a aborda această vulnerabilitate este discutată într-un articol de asistență Microsoft.

Activarea pe bază de jetoane Windows este o metodă de activare a produselor Windows, așa cum este descris într-un articol de documentație Microsoft. Procesul de activare se realizează prin scriptul SLMGR.vbs, așa cum este explicat într-un articol cuprinzător de pe ss64.com. O postare pe forum pe Microsoft Technet oferă mai multe informații despre activarea pe bază de jetoane Windows 10 Enterprise.

## CVE-2020-17049 - Kerberos Bronze Bit Attack:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Activare pe bază de jetoane Windows:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Videoclipuri de interes:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
