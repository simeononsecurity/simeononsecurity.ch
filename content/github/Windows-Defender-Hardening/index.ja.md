---
title: "Defender Hardening スクリプトを使用して Windows 10 のセキュリティを強化する"
date: 2020-11-15
toc: true
draft: false
description: "Windows Defender ウイルス対策 STIG V2R1 のすべての要件を実装し、Windows Defender ウイルス対策の強化を図る PowerShell スクリプトを使用して Windows 10 のセキュリティを強化する方法について説明します。"
tags: ["Windows ディフェンダー", "ウィンドウズ10", "Windows 10のセキュリティ", "PowerShell スクリプト", "硬化", "ディフェンダーの強化", "セキュリティの自動化", "コンプライアンス", "フォルダーアクセスの制御", "侵入防御システム", "アプリケーション制御", "攻撃対象領域の削減", "エクスプロイト保護", "クラウドによる保護", "ネットワーク保護", "Windows Defender STIG スクリプト", "Windows Defender STIG", "Windows Defender ウイルス対策 STIG V2R1", "WDAC", "ASR"]
---


## このスクリプトは何をするのでしょうか?
- クラウド提供の保護を有効にします
- 制御されたフォルダーアクセスを有効にします
- ネットワーク保護を有効にします
- 侵入防御システムを有効にする
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- にリストされているすべての要件を実装します。[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

＃＃ 要件：
- [x] Windows 10 Enterprise (**推奨**) または Windows 10 Professional
  - Windows 10 Home では GPO 構成が許可されていない、または[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
ただし、これらの構成のほとんどは引き続き適用されます。
  - Windows 10「N」エディションはテストされていません。

## 必要なファイルをダウンロードします。

から必要なファイルをダウンロードします。[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## スクリプトの実行方法:

**スクリプトは、次のように抽出された GitHub ダウンロードから起動できます:**
```
.\sos-windowsdefenderhardening.ps1
```
