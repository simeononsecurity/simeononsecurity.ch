---
title: "Windows DefenderでWindowsを強化する完全ガイド..."
date: 2020-12-16
toc: true
draft: false
description: Windows Defender Application Control（WDAC）を使用して、スクリプトやツールでWindowsオペレーティングシステムを強化する方法を学びます。
tags:
- Windows Defender Application Control（WDAC）強化
- PowerShell
- PowerShellスクリプト
- 自動化
- コンプライアンス
- ブルーチーム
- Windows Defender STIGスクリプト
- Windows Defender強化
- Windows Defender STIG
- Defender STIG
- Windows Defender Exploit Protection（WDEP）
- Windows Defender Attack Surface Reduction（ASR）
- Windows Server 2016 2019
- Windows Server Core
- Microsoft WDAC-Toolkit
- CIポリシーの更新
- Microsoft推奨のブロックルール
- Microsoft推奨のドライバーブロックルール
- XMLポリシー
- BINポリシー
- グループポリシー
- Microsoft Intune
cover: /img/cover/Windows-Defender-Application-Control-Hardening.webp
coverAlt: Windows Defender Application Controlに関連するXMLおよびBINファイル構造を表示する発光スクリーンがある未来的なサーバールームのイラスト。暗い背景が鮮やかな色を際立たせています。
coverCaption: ''
lastmod: 2026-10-08
---

**Windows Defender Application Control（WDAC）でWindowsを強化する**

## 注意事項:
- Windows Server 2016/2019またはバージョン1903以前は、同時に1つのレガシーポリシーのみをサポートします。
- Windows Server Coreエディションは[WDAC](https://simeononsecurity.com/til/2022-05-18/)をサポートしますが、AppLockerに依存する一部のコンポーネントは動作しません。
- 実装やテストの前に必ず[推奨読書](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading)をお読みください。

## このコレクションで使用されるスクリプトとツールの一覧:

- [MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
- [Microsoft - CIポリシーの更新](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## 追加で検討された設定:

- [Microsoft - 推奨ブロックルール](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - 推奨ドライバーブロックルール](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## 説明:

### XMLとBINの違い:

- 簡単に言うと、**「XML」**ポリシーはローカルマシンに適用するためのもので、**「BIN」**ファイルは[グループポリシー](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)や[Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)で適用するためのものです。ローカル展開ではXML、BIN、CIPポリシーのいずれも使用可能ですが、一般的には監査やトラブルシューティング時に特にXMLを使用することを推奨します。

### ポリシーの説明:

- **デフォルトポリシー:**
  - 「デフォルト」ポリシーはWDAC-Toolkitのデフォルト機能のみを使用します。
- **推奨ポリシー:**
  - 「推奨」ポリシーはデフォルト機能に加え、Microsoftの推奨する[ブロック](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)および[ドライバーブロック](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)ルールを使用します。
- **監査ポリシー:**
  - 「監査」ポリシーはルールの例外をログに記録するだけです。これは環境でのテスト用で、環境のニーズに合わせてポリシーを自由に変更できます。
- **強制ポリシー:**
  - 「強制」ポリシーはルールの例外を許可しません。準拠しないアプリケーション、ドライバー、dllなどはブロックされます。

### 利用可能なポリシー:

- **XML:**
  - **監査のみ:**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **強制:**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN:**
  - **監査のみ:**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **強制:**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP:**
  - **監査のみ:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **強制:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

スクリプト内の次の行を更新して、ローカルで使用したいポリシーを指定してください:

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

または、[グループポリシー](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)や[Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)を使用してWDACポリシーを適用することもできます。

## 監査:

WDACのイベントログはイベントビューアーの以下の場所で確認できます:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## 推奨読書:

- [Argonsys - Windows 10アプリケーションコントロールポリシーの展開](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Windows Defender Application Controlポリシーの監査](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - 参照コンピューターを使用した固定ワークロードデバイス向けWDACポリシーの作成](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - グループポリシーを使用したWindows Defender Application Controlポリシーの展開](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Microsoft Intuneを使用したWindows Defender Application Controlポリシーの展開](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - スクリプトを使用したWDACポリシーの展開](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Windows Defender Application Controlポリシーの強制](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - WDAC拒否ポリシー作成のガイダンス](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - 複数のWindows Defender Application Controlポリシーの使用](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## スクリプトの実行方法:

### 手動インストール:

手動でダウンロードした場合、スクリプトは[GitHubリポジトリ](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)からすべてのファイルがあるディレクトリ内の管理者権限のPowerShellから起動する必要があります。

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
