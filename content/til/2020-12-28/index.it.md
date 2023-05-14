---
title: "Oggi ho appreso di CVE-2020-17049 e dell'attivazione basata su token di Windows"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**Ciò che SimeonOnSecurity ha imparato e trovato interessante oggi**

SimeonOnSecurity ha recentemente appreso di due argomenti nel campo della sicurezza informatica: CVE-2020-17049, noto anche come Kerberos Bronze Bit Attack, e Windows Token-Based Activation.

Il Kerberos Bronze Bit Attack, come spiegato in una serie di post sul blog di Netspi e in un post di Trimarcsecurity, è una vulnerabilità nel protocollo di autenticazione Kerberos. Questa vulnerabilità potrebbe potenzialmente consentire a un utente malintenzionato di compromettere un Active Directory, che è un archivio centrale per le informazioni su utenti, computer e altre risorse di un'organizzazione. La distribuzione delle modifiche Kerberos S4U per risolvere questa vulnerabilità è discussa in un articolo di supporto Microsoft.

L'attivazione basata su token di Windows è un metodo di attivazione dei prodotti Windows, come descritto in un articolo della documentazione Microsoft. Il processo di attivazione viene eseguito tramite lo script SLMGR.vbs, come spiegato in un articolo completo su ss64.com. Un post del forum su Microsoft Technet fornisce ulteriori informazioni sull'attivazione basata su token di Windows 10 Enterprise.

## CVE-2020-17049 - Attacco Kerberos Bronze Bit:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Attivazione basata su token di Windows:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Video di interesse:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
