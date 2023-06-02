---
title: "Windows Hardening CTF: Capture the Flagイベントに向けてWindowsデバイスのセキュリティを強化します。"
date: 2020-10-19
toc: true
draft: false
description: "Windowsのセキュリティを強化する強力なスクリプトで、さまざまなハードニング対策を実施し、侵害を抑止します。"
tags: ["ウィンドウズ・ハード化", "Windowsのセキュリティ", "スクリプト", "Windowsデバイス", "コマンドプロンプト", "LLMNR", "パワーシェル", "エスエムビー", "TCPタイムスタンプ", "AppLocker", "ウィンドウズ・ロギング", "デップ", "EMETのコンフィギュレーション", "PowerShellの制約付き言語モード", "SMBの暗号化", "SpectreとMeltdownのミティゲーション", "Windows Defender", "Windowsファイアウォール", "PSWindowsUpdate", "Windowsのアップデート", "ハードニングスクリプト", "NSA推奨ポリシー", "Windowsのロギングとセキュリティコントロール", "Windows Defenderアプリケーションコントロール", "Windows Defenderの攻撃面減少対策について", "Windows Defender クラウドベースプロテクション", "Windows Defenderのエクスプロイト対策", "PSWindowsUpdateのインストール", "Windowsデバイスのセキュリティ強化", "Windowsのハード化対策", "Windowsセキュリティの強化"]
---

**ウィンドウズ・ハーデニング-CTF**｜株式会社日立ソリューションズ
Windowsデバイスを危険にさらすことを難しくし、より厄介にするWindows Hardeningスクリプトです。

## このスクリプトは何をするのか？
- コマンドプロンプトを無効にする
- LLMNRを無効にする
- PowerShell v2 を無効にする
- SMB Compressionを無効にする
- SMB v1 を無効にする
- SMB v2を無効にする
- TCPタイムスタンプの無効化
- WSMANおよびPSRemotingの無効化
- NSAが推奨するポリシーでAppLockerを使用可能にする
- ベストプラクティスのWindowsログとセキュリティコントロールの有効化
- DEPを使用可能にする
- EMET 構成を有効にする（EMET がインストールされているシステムにのみ適用されます。）
- PowerShell Constrined Language Modeの有効化
- PowerShellのロギングを有効にする
- SMB暗号化の有効化
- SpectreとMeltdownの緩和を有効にする
- Windows Defenderのアプリケーションコントロールの有効化
- Windows Defenderのアタックサーフェスリダクションの有効化
- Windows Defenderクラウドベースプロテクションの有効化
- Windows Defenderのエクスプロイトプロテクションを有効にする
- Windowsファイアウォールとログの有効化
- PSWindowsUpdateをインストールし、利用可能なすべてのWindowsアップデートをインストールします。

## 必要なファイルをダウンロードします：

必要なファイルのダウンロード：必要なファイルを下記からダウンロードします。 [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## スクリプトの実行方法

**スクリプトの実行方法： **スクリプトは、GitHubでダウンロードしたスクリプトから、以下のように起動します。
```
.\sos-windows-hardening-ctf.ps1
```
