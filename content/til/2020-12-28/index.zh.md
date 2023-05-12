---
title: “今天我了解了 CVE-2020-17049 和基于 Windows 令牌的激活”
date: 2020-12-27
toc: true
draft: false
---

**SimeonOnSecurity 今天学到的东西和有趣的东西**

SimeonOnSecurity 最近了解了计算机安全领域的两个话题：CVE-2020-17049，也称为 Kerberos Bronze Bit 攻击，以及 Windows Token-Based Activation。

正如 Netspi 的一系列博客文章和 Trimarcsecurity 的一篇文章中所解释的，Kerberos 青铜位攻击是 Kerberos 身份验证协议中的一个漏洞。此漏洞可能允许攻击者破坏 Active Directory，它是有关组织的用户、计算机和其他资源的信息的中央存储库。 Microsoft 支持文章中讨论了部署 Kerberos S4U 更改以解决此漏洞。

Windows 基于令牌的激活是一种激活 Windows 产品的方法，如 Microsoft 文档文章中所述。激活过程是通过 SLMGR.vbs 脚本执行的，如 ss64.com 上的综合文章中所述。 Microsoft Technet 上的论坛帖子提供了有关 Windows 10 Enterprise Token Based Activation 的更多信息。

## CVE-2020-17049 - Kerberos 青铜位攻击：
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Windows 基于令牌的激活：
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## 感兴趣的视频：
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
