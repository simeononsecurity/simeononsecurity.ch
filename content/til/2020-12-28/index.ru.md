---
title: «Сегодня я узнал о CVE-2020-17049 и активации на основе токенов Windows»
date: 2020-12-27
toc: true
draft: false
---

**Что SimeonOnSecurity узнал и нашел интересным сегодня**

SimeonOnSecurity недавно узнал о двух темах в области компьютерной безопасности: CVE-2020-17049, также известной как атака Kerberos Bronze Bit, и активация на основе токенов Windows.

Атака Kerberos Bronze Bit Attack, как объясняется в серии сообщений блога Netspi и в сообщении Trimarcsecurity, представляет собой уязвимость в протоколе аутентификации Kerberos. Эта уязвимость потенциально может позволить злоумышленнику скомпрометировать Active Directory, которая является центральным хранилищем информации о пользователях, компьютерах и других ресурсах организации. Развертывание изменений Kerberos S4U для устранения этой уязвимости обсуждается в статье службы поддержки Microsoft.

Активация на основе токенов Windows — это метод активации продуктов Windows, описанный в статье документации Microsoft. Процесс активации выполняется с помощью сценария SLMGR.vbs, как описано в подробной статье на ss64.com. В сообщении на форуме Microsoft Technet содержится дополнительная информация об активации Windows 10 Enterprise на основе токена.

## CVE-2020-17049 — Битовая атака Kerberos Bronze:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Активация на основе токена Windows:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## Интересные видео:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
