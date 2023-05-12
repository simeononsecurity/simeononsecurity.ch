---
title: „Heute habe ich etwas über CVE-2020-17049 und die tokenbasierte Windows-Aktivierung erfahren“
date: 2020-12-27
toc: true
draft: false
---

**Was SimeonOnSecurity heute erfahren und interessant fand**

SimeonOnSecurity hat kürzlich von zwei Themen im Bereich der Computersicherheit erfahren: CVE-2020-17049, auch bekannt als Kerberos Bronze Bit Attack, und Windows Token-Based Activation.

Der Kerberos-Bronze-Bit-Angriff ist, wie in einer Reihe von Blogbeiträgen von Netspi und in einem Beitrag von Trimarcsecurity erläutert, eine Schwachstelle im Kerberos-Authentifizierungsprotokoll. Diese Sicherheitslücke könnte es einem Angreifer möglicherweise ermöglichen, ein Active Directory zu gefährden, das ein zentrales Repository für Informationen über die Benutzer, Computer und andere Ressourcen einer Organisation darstellt. Die Bereitstellung von Kerberos S4U-Änderungen zur Behebung dieser Sicherheitslücke wird in einem Microsoft-Supportartikel erläutert.

Die tokenbasierte Windows-Aktivierung ist eine Methode zur Aktivierung von Windows-Produkten, wie in einem Microsoft-Dokumentationsartikel beschrieben. Der Aktivierungsprozess wird über das SLMGR.vbs-Skript durchgeführt, wie in einem ausführlichen Artikel auf ss64.com erläutert. Ein Forumbeitrag auf Microsoft Technet bietet weitere Informationen zur tokenbasierten Aktivierung von Windows 10 Enterprise.

## CVE-2020-17049 – Kerberos-Bronze-Bit-Angriff:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Windows-Token-basierte Aktivierung:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Interessante Videos:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
