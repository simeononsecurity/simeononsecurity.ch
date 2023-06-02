---
title: "Windowsとサーバーシステムを強化する：カスタムブランディングセットアップガイド"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Windowsブランディング", "サーバーのブランディング", "カスタムブランディング", "システムカスタマイゼーション", "ブランディングセットアップ", "ウィンドウズ10", "サーバー2016", "サーバー2019", "サーバー2022", "ユーザーエクスペリエンス", "システムカスタマイズガイド", "パーソナル化", "システムブランディング", "Windowsのカスタマイズ", "サーバーのカスタマイズ", "OEMロゴ", "ユーザーイメージ", "ゲストイメージ", "ブランディングスクリプト", "マイクロソフトセキュリティコンプライアンスツールキット", "Windowsのブランディング設定", "サーバーブランディングの設定", "カスタムブランディングガイド", "パーソナライズドブランディング", "システムカスタマイズチュートリアル", "Windowsシステムのカスタマイズ", "サーバーシステムカスタマイズ", "ブランディングイメージ", "ブランディングベストプラクティス", "Windows カスタマイズのヒント", "サーバーのカスタマイズ技術"]
---

**Windows 10およびServer 2016/2019/2022のシステムでセットアップブランディングを行う**。

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## ブランディングファイルの設定方法
- X] すべての画像をあなたのブランディング画像に置き換える。
  - [X] OEMロゴは95x95または120x20で".bmp "形式でなければなりません。
  - 32x32, 40x40, 48x48, 192x192 のユーザー画像を作成する。
  - X] ゲストイメージのためにユーザーイメージを生成またはコピーする。
  
## このスクリプトは、以下のツールを使用します：
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## スクリプトの実行方法
### 手動インストール：
手動でダウンロードした場合、スクリプトは、管理用パワーシェルから [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### 自動インストール：
スクリプトは、GitHubからダウンロードしたものを次のように起動することができます：
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/sosbranding.ps1'|iex
```

