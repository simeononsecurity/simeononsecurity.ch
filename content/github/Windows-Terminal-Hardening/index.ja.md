---
title: "WindowsコマンドプロンプトとPowerShellのハードニング"
date: 2020-11-18
toc: true
draft: false
description: "WindowsコマンドプロンプトとPowerShellのセキュリティを確保するために、包括的なハードニングスクリプトとドキュメントを提供し、システムのセキュリティとコンプライアンスを強化します。"
tags: ["パワーシェル", "焼入れ", "Windowsコマンドプロンプト", "セキュリティ", "コンプライアンス", "オートメーション", "制約条件付き言語モード", "PowerShellのロギング", "PowerShellスクリプト", "WSMAN", "PSRemoting（リモーティング", "エンタープライズ・セキュリティ", "ブルーチーム", "サイバーセキュリティ", "ベストプラクティス", "コマンドプロンプトを無効にする", "PowerShell v2を無効にする", "GitHub リポジトリ", "Windows Defender", "マイクロソフト"]
---
およびWindowsコマンドプロンプトとPowerShellのハードニングのためのドキュメンテーション

## このスクリプトは何をするのか？
- コマンドプロンプトを使用不可にする
- PowerShell v2を無効にする
- WSMANとPSRemotingを無効にする
- PowerShell Constrained Language Modeを有効にする
- PowerShellのロギングを有効にする

## 推薦図書
-[PowerShell Best Practices](https://www.digitalshadows.com/blog-and-research/powershell-security-best-practices/)
-[PowerShell Constrained Language Mode](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)
-[Securing PowerShell in the Enterprise](https://www.cyber.gov.au/acsc/view-all-content/publications/securing-powershell-enterprise)
-[Windows Defender Hardening](https://github.com/simeononsecurity/Windows-Defender-Hardening)

## 必要なファイルをダウンロードする：

必要なファイルのダウンロード：必要なファイルを下記よりダウンロードしてください。[GitHub Repository](https://github.com/simeononsecurity/Windows-Terminal-Hardening)

## スクリプトの実行方法

**スクリプトの実行方法： **スクリプトは、GitHubでダウンロードしたスクリプトから、以下のように起動します。
```
.\sos-windowsterminalhardening.ps1
```
