---
title: "今日は、WDACのポリシー作成と実施について詳しく学びました。"
date: 2022-05-18
toc: true
draft: false
description: "今日はAnsibleの条件分岐と変数管理について詳しく学びました"
genre: ["オートメーション", "Windowsのセキュリティ", "アプリケーションコントロール", "Windows Defender", "ダブリューダブリューエーシー", "パワーシェル", "スレットプロテクション", "Windows Server 2019", "エンタープライズ・セキュリティ", "ポリシーマネジメント", "セキュリティのベストプラクティス"]
tags: ["オートメーション", "ダブリューダブリューエーシー", "アプリケーションコントロール", "Windows Defenderアプリケーションコントロール", "Windows Defender", "パワーシェル", "マイクロソフトのドキュメント", "WDACのポリシー作成", "ポリシー展開", "スクリプトベースの展開", "マルチプルWDACポリシー", "固定荷重装置", "トラステッドアプリケーション", "方針を否定する", "セキュリティ対策", "政策運営", "エンタープライズセキュリティ", "脅威防御", "Windows Server", "Windowsのセキュリティ", "アプリケーションホワイトリスト"]
---

**SimeonOnSecurityが今日知ったこと、興味を持ったこと**。

本日、SimeonOnSecurityはリポジトリ「Windows-Defender-Application-Control-Hardening」を更新し、Windows 10 EnterpriseとWindows Server 2019の機能で、デバイス上で実行されるものを制御してセキュリティを提供する「Windows Defender Application Control（WDAC）」について学びました。

SimeonOnSecurityは、WDACに関するMicrosoftのドキュメントを掘り下げ、ポリシーの作成と展開のためのいくつかの重要なリソースを発見しました。彼は、リファレンスコンピュータを使用して固定作業負荷デバイス用のWDACポリシーを作成する方法、スクリプトを使用してWDACポリシーを展開する方法、および異なるシナリオに複数のポリシーを使用する方法について学びました。

さらに、SimeonOnSecurityは、WDAC拒否ポリシーの作成に関するガイダンスを理解し、デバイス上で信頼できるアプリケーションの実行のみを許可し、その他のアプリケーションを拒否するというコンセプトをよりよく理解することができました。

全体として、SimeonOnSecurityは、Windows Defenderアプリケーションコントロールの探求により、現代のセキュリティ実践におけるアプリケーションコントロールの重要性に対する理解をさらに強固なものにしました。

## Repos Updated：
- [simeononsecurity/Windows-Defender-Application-Control-Hardening](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening)

## WDACの読み方：
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)
