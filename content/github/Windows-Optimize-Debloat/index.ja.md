---
title: "Windows-Optimize-DebloatでWindows PCを最適化する。"
date: 2020-12-29
toc: true
draft: false
description: "ブロートウェアの削除とシステム設定の最適化を支援する包括的なスクリプトであるWindows-Optimize-Debloatを使用して、Windowsオペレーティングシステムのパフォーマンスとプライバシーを改善します。"
tags: ["Windows-Optimize-Debloat（ウィンドウズ・オプティマイズ・デブロート", "Windowsの最適化", "デブロートウィンドウ", "Windowsを高速化する", "Windowsのパフォーマンスを最適化する", "Windowsのパフォーマンス向上", "Windows システムの最適化", "マイクロソフト", "プライバシー", "ブロートウェアの削除", "ウィンドウズ10", "ウィンドウズ11", "Windows Defender", "Windows Update", "コルトーナ", "グループポリシーオブジェクト", "テレメトリー", "ウィンドウズストア", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Windows 10、11のインストールを最小限に抑えようとする方におすすめです。

**注：**このスクリプトは、すべてではないにしても、ほとんどのシステムで問題なく動作するはずです。一方 [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)このスクリプトが何をするものか理解できない場合は、実行しないでください。

## はじめに
Windows 10 と 11 は、箱から出したままでは侵略的で安全でないオペレーティングシステムです。
以下のような組織では [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io)などが、Windows 10オペレーティングシステムを最適化し、デブロートするための構成変更を推奨しています。これらの変更には、テレメトリーのブロック、ログの削除、ブロートウェアの削除など、いくつかの例を挙げることができます。このスクリプトは、これらの組織が推奨する設定を自動化することを目的としています。

## 注意事項
- このスクリプトは、主に**Personal Use**環境での運用を想定して設計されています。
- このスクリプトは、他のスクリプトとは異なり、最適化によってWindowsのコア機能が破壊されないように設計されています。
 - Windows Update、Windows Defender、Windowsストア、Cortonaなどの機能は制限されていますが、他のWindows 10プライバシースクリプトのように機能不全の状態にはなっていません。
- 商用環境のみを対象とした最小化スクリプトをお探しの場合は、こちらをご覧ください。 [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## 必要条件
- X] Windows 10/11 Enterprise、Windows 10 Professional、Windows 10 Homeのいずれか。
  - Windows Homeでは、GPOの設定ができません。
    - スクリプトは動作しますが、すべての設定が適用されるわけではありません。
  - Windows "N" Editionsはテストされていません。
  - スクリプトを実行する [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant)で、最新のメジャーリリースをアップデートして確認します。

## MicrosoftアカウントまたはXboxサービスを修正する：
これは、マイクロソフトアカウントへのサインインをブロックしているためです。マイクロソフトのテレメトリとIDの関連付けは嫌われます。
しかし、これらのサービスを使用したい場合は、以下のチケットで解決できます：
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## このコレクションが利用するスクリプトとツールのリストです：
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## からの追加設定を検討した：
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## スクリプトの実行方法
### 自動インストール：
自動インストール：GitHubからダウンロードしたスクリプトを、以下のように起動します：
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### 手動でインストールします：
手動でダウンロードした場合、スクリプトは、管理用パワーシェルから、以下のすべてのファイルが含まれるディレクトリで起動する必要があります。 [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

スクリプト「sos-optimize-windows.ps1」には、最適化プロセスのカスタマイズを可能にするいくつかのパラメータが含まれています。各パラメーターはブール値で、指定しない場合はデフォルトでtrueになります。

- **$cleargpos**：グループポリシーオブジェクトの設定をクリアします。
- **$installupdates**：システムにアップデートをインストールします：システムにアップデートをインストールします。
- **$removebloatware**：システムに更新プログラムをインストールします：システムから不要なプログラムおよび機能を削除します。
- **$disabletelemetry**：データ収集と遠隔測定を無効にします：データ収集とテレメトリーを無効にします。
- **$privacy**：プライバシーを向上させるための変更を行います。
- **$imagecleanup**：システムから不要なファイルをクリーンアップします。
- **$diskcompression**：システムディスクを圧縮します：システムディスクを圧縮します。
- アップデート管理**：システム上でアップデートを管理し、改善する方法を変更します。
- **$sosbrowsers**：システムのウェブブラウザを最適化します：システムの Web ブラウザを最適化します。

特定のパラメータを指定してスクリプトを起動する例は、次のとおりです：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

