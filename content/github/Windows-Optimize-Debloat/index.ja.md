---
title: "Windows-Optimize-Debloat で Windows PC を最適化する"
date: 2020-12-29
toc: true
draft: false
description: "Windows-Optimize-Debloat を使用すると、Windows オペレーティング システムのパフォーマンスとプライバシーが向上します。これは、ブロートウェアを削除し、システム設定を最適化するのに役立つ包括的なスクリプトです。"
tags: ["Windows-最適化-デブロート", "Windowsの最適化", "Windows の膨張", "Windowsを高速化する", "Windowsのパフォーマンスを最適化する", "Windows パフォーマンスの向上", "Windows システムの最適化", "マイクロソフト", "プライバシー", "ブロートウェアの削除", "ウィンドウズ10", "Windows 11", "Windows ディフェンダー", "Windowsアップデート", "コルトーナ", "グループポリシーオブジェクト", "テレメトリー", "Windows ストア", "Windows 10 プロフェッショナル", "Windows 10 ホーム"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Windows 10 および 11 のインストールを最小限に抑えたい人向け。*

**注意:** このスクリプトは、すべてではないにしても、ほとんどのシステムで問題なく動作するはずです。その間[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) このスクリプトの動作が理解できない場合は、実行しないでください。

＃＃ 序章：
Windows 10 および 11 は、そのままでは侵襲的で安全ではないオペレーティング システムです。
のような組織[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) などの人々は、Windows 10 オペレーティング システムを最適化し、肥大化を解消するために構成の変更を推奨しています。これらの変更には、テレメトリのブロック、ログの削除、ブロートウェアの削除などが含まれます。このスクリプトは、これらの組織が推奨する構成を自動化することを目的としています。

＃＃ ノート：
- このスクリプトは、主に **個人使用** 環境での動作を目的として設計されています。
- このスクリプトは、他のスクリプトとは異なり、最適化によって Windows のコア機能が損なわれないように設計されています。
 - Windows Update、Windows Defender、Windows ストア、Cortona などの機能は制限されていますが、他のほとんどの Windows 10 プライバシー スクリプトのように機能不全な状態にはありません。
- 商用環境のみを対象とした最小化されたスクリプトをお探しの場合は、これを参照してください。[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

＃＃ 要件：
- [X] Windows 10/11 Enterprise、Windows 10 Professional、または Windows 10 Home
  - Windows Home では GPO 構成ができません。
    - スクリプトは引き続き機能しますが、すべての設定が適用されるわけではありません。
  - Windows "N" エディションはテストされていません。
  - を実行します[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) 最新のメジャー リリースを更新して確認します。

## Microsoft アカウントまたは Xbox サービスの修正:
これは、Microsoft アカウントへのサインインがブロックされているためです。 Microsoft のテレメトリと ID の関連付けは眉をひそめています。
ただし、これらのサービスを引き続き使用したい場合は、次の問題チケットを参照して解決策を確認してください。
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## このコレクションが使用するスクリプトとツールのリスト:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## 追加の構成は以下から検討されました。
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## スクリプトの実行方法:
### 自動インストール:
スクリプトは、次のように、抽出された GitHub ダウンロードから起動できます。
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

