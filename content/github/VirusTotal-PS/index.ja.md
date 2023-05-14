---
title: "VirusTotal PowerShell モジュールを使用した効率的なウイルス スキャン"
date: 2020-11-24
toc: true
draft: false
description: "VirusTotal API との対話を自動化し、セキュリティ ワークフローを合理化することで、VirusTotal PowerShell モジュールを使用して効率的なウイルス スキャンを実行します。"
tags: ["PowerShell モジュール", "パワーシェル", "オートメーション", "ウイルス合計", "ウイルススキャン", "ドメインスキャン", "APIキー", "VirusTotal API", "VirusTotal 開発者ページ", "システム管理", "セキュリティワークフロー", "効率的なウイルススキャン", "ダウンロードとインストール", "GitHub リポジトリ", "APIの使用例"]
---
 VirusTotal API と対話するための PowerShell モジュールのコレクション

**ノート：**
- VirusTotal API キーが必要になります。このキーは、[Shodan Account](https://www.virustotal.com/gui/)
- モジュールで使用される API の例は、[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

＃＃ ダウンロードとインストール
- からモジュールをダウンロードします。[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- すべてのモジュールをインストールします
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```