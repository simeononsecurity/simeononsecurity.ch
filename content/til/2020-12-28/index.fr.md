---
title: "Aujourd'hui, j'ai découvert CVE-2020-17049 et l'activation basée sur des jetons Windows"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**Ce que SimeonOnSecurity a appris et trouvé intéressant aujourd'hui**

SimeonOnSecurity a récemment pris connaissance de deux sujets dans le domaine de la sécurité informatique : CVE-2020-17049, également connu sous le nom d'attaque Kerberos Bronze Bit, et l'activation basée sur des jetons Windows.

L'attaque Kerberos Bronze Bit, comme expliqué dans une série d'articles de blog de Netspi et dans un article de Trimarcsecurity, est une vulnérabilité du protocole d'authentification Kerberos. Cette vulnérabilité pourrait potentiellement permettre à un attaquant de compromettre un Active Directory, qui est un référentiel central d'informations sur les utilisateurs, les ordinateurs et d'autres ressources d'une organisation. Le déploiement des modifications de Kerberos S4U pour résoudre cette vulnérabilité est abordé dans un article de support Microsoft.

L'activation basée sur les jetons Windows est une méthode d'activation des produits Windows, comme décrit dans un article de la documentation Microsoft. Le processus d'activation est effectué via le script SLMGR.vbs, comme expliqué dans un article complet sur ss64.com. Un message de forum sur Microsoft Technet fournit plus d'informations sur l'activation basée sur les jetons Windows 10 Enterprise.

## CVE-2020-17049 - Attaque Kerberos Bronze Bit :
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Activation basée sur un jeton Windows :
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Vidéos intéressantes :
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
