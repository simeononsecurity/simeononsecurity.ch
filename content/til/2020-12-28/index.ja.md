---
title: 「今日、CVE-2020-17049 と Windows トークンベースのライセンス認証について学びました」
date: 2020-12-27
toc: true
draft: false
---

**SimeonOnSecurity が今日学び、興味深かったこと**

SimeonOnSecurity は最近、コンピューター セキュリティの分野における 2 つのトピック、つまり Kerberos ブロンズ ビット攻撃としても知られる CVE-2020-17049 と Windows トークンベースのライセンス認証について知りました。

Netspi による一連のブログ投稿および Trimarcsecurity による投稿で説明されているように、Kerberos ブロンズ ビット攻撃は、Kerberos 認証プロトコルの脆弱性です。この脆弱性により、攻撃者は、組織のユーザー、コンピュータ、およびその他のリソースに関する情報の中央リポジトリである Active Directory を侵害する可能性があります。この脆弱性に対処するための Kerberos S4U 変更の導入については、Microsoft サポート記事で説明されています。

Windows トークンベースのライセンス認証は、Microsoft のドキュメント記事で説明されているように、Windows 製品をライセンス認証する方法です。 ss64.com の包括的な記事で説明されているように、アクティベーション プロセスは SLMGR.vbs スクリプトを通じて実行されます。 Microsoft Technet のフォーラム投稿には、Windows 10 Enterprise トークン ベースのライセンス認証に関する詳細情報が記載されています。

## CVE-2020-17049 - Kerberos ブロンズ ビット攻撃:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## Windows トークンベースのライセンス認証:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## 興味のあるビデオ:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
