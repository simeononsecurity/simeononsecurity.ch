---
title: "今日はCVE-2020-17049とWindowsのトークンベースのアクティベーションについて学びました。"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

**SimeonOnSecurityが今日知ったこと、興味を持ったこと**。

SimeonOnSecurityは最近、コンピュータセキュリティの分野で2つのトピックについて学びました：CVE-2020-17049（KerberosのBronze Bit攻撃としても知られている）と、Windowsのトークンベースのアクティベーションです。

Kerberos Bronze Bit Attackは、Netspiの一連のブログ記事やTrimarcsecurityの投稿で説明されているように、Kerberos認証プロトコルにおける脆弱性です。この脆弱性により、攻撃者は、組織のユーザー、コンピュータ、およびその他のリソースに関する情報の中央リポジトリであるActive Directoryを侵害できる可能性があります。この脆弱性に対処するためのKerberos S4U変更の展開については、Microsoftのサポート記事で説明されています。

Windows Token-Based Activationは、Microsoftのドキュメント記事で説明されているように、Windows製品をアクティブ化する方法です。このアクティベーションプロセスは、ss64.comの包括的な記事で説明されているように、SLMGR.vbsスクリプトを通じて実行されます。Microsoft Technetのフォーラム投稿では、Windows 10 Enterprise Token Based Activationに関する詳細な情報が提供されています。

## CVE-2020-17049 - Kerberos Bronze Bit 攻撃：
- [CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
- [CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
- [Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
- [Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Windows トークンベースのアクティベーションです：
- [Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
- [SLMGR.vbs](https://ss64.com/nt/slmgr.html)
- [Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## 興味のある動画を紹介します：
- [Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
- [Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
- [Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
- [Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
- [Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
- [Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
