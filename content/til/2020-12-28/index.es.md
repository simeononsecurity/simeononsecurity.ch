---
title: "Hoy he aprendido sobre CVE-2020-17049 y la activación basada en token de Windows"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**Lo que SimeonOnSecurity ha descubierto y encontrado interesante hoy**

SimeonOnSecurity ha aprendido recientemente sobre dos temas en el campo de la seguridad informática: CVE-2020-17049, también conocido como el Ataque Kerberos Bronze Bit, y la Activación Basada en Token de Windows.

El Ataque Kerberos Bronze Bit, como se explica en una serie de entradas de blog de Netspi y en un post de Trimarcsecurity, es una vulnerabilidad en el protocolo de autenticación Kerberos. Esta vulnerabilidad podría permitir a un atacante comprometer un Directorio Activo, que es un repositorio central de información sobre los usuarios, ordenadores y otros recursos de una organización. El despliegue de cambios Kerberos S4U para hacer frente a esta vulnerabilidad se discute en un artículo de soporte de Microsoft.

La activación basada en token de Windows es un método de activación de productos Windows, como se describe en un artículo de documentación de Microsoft. El proceso de activación se realiza a través del script SLMGR.vbs, como se explica en un artículo completo en ss64.com. Una publicación del foro en Microsoft Technet proporciona más información sobre la activación basada en token de Windows 10 Enterprise.

## CVE-2020-17049 - Ataque Kerberos Bronze Bit:
- [CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
- [Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
- [Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Activación basada en token de Windows:
- [Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
- [SLMGR.vbs](https://ss64.com/nt/slmgr.html)
- [Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Videos de interés:
- [Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
- [Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
- [Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
- [Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
- [Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
- [Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
