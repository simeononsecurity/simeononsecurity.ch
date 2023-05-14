---
title: "Hoje aprendi sobre o CVE-2020-17049 e a ativação baseada em token do Windows"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**O que SimeonOnSecurity aprendeu e achou interessante hoje**

SimeonOnSecurity aprendeu recentemente sobre dois tópicos no campo da segurança do computador: CVE-2020-17049, também conhecido como Kerberos Bronze Bit Attack e Windows Token-Based Activation.

O Kerberos Bronze Bit Attack, conforme explicado em uma série de postagens de blog da Netspi e em uma postagem da Trimarcsecurity, é uma vulnerabilidade no protocolo de autenticação Kerberos. Essa vulnerabilidade pode permitir que um invasor comprometa um Active Directory, que é um repositório central de informações sobre usuários, computadores e outros recursos de uma organização. A implantação das alterações do Kerberos S4U para lidar com essa vulnerabilidade é discutida em um artigo de suporte da Microsoft.

A ativação baseada em token do Windows é um método de ativação de produtos Windows, conforme descrito em um artigo de documentação da Microsoft. O processo de ativação é realizado por meio do script SLMGR.vbs, conforme explicado em um artigo abrangente no ss64.com. Uma postagem no fórum no Microsoft Technet fornece mais informações sobre a ativação baseada em token do Windows 10 Enterprise.

## CVE-2020-17049 - Kerberos Bronze Bit Attack:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Ativação baseada em token do Windows:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Vídeos de interesse:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
