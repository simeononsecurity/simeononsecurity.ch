---
title: "Standalone-Windows-STIG-Script：準拠したPCを構築する"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "パラメーターと確認手順を含む、準拠したWindowsシステムを構築するためのStandalone-Windows-STIG-Scriptの手順ガイドです。"
tags: ["STIGスクリプト", "Windowsセキュリティ", "準拠したWindowsシステム", "システムの強化", "Windows STIG", "安全なWindows", "Windowsコンプライアンス", "手動インストール", "Windows更新プログラム", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Windowsファイアウォール", "リスク軽減策", "Nessus PID", "VMware Horizon", "任意のシステム強化"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "濃紺の背景に、鮮やかなアクセントカラーの動的な進捗バーとデータの流れを備えたセキュリティ準拠インターフェースを表示するコンピューター画面のイラスト。"
coverCaption: ""
---

Windowsシステムは企業、組織、家庭で広く使われています。サイバー攻撃が増える中、システムを安全に保ち、業界標準に準拠させることが重要です。Standalone-Windows-STIG-Scriptは、そのために役立つツールです。この記事では、このスクリプトの概要、仕組み、安全で準拠したWindowsシステムを作成するための使い方を説明します。

## Standalone-Windows-STIG-Scriptとは？

**Standalone-Windows-STIG-Script**は、Security Technical Implementation Guide (STIG) に沿ってWindowsシステムを保護する作業を自動化するため、Simeononsecurityが開発したスクリプトです。オープンソースで、**GitHub**から入手できます。

## どのように動作しますか？

Standalone-Windows-STIG-Scriptは、Windowsシステムを保護するためにSTIGのガイドラインを適用します。Windows上で実行すると、STIGへの準拠に必要な変更をシステムに加えます。対象となるセキュリティ対策には、次のものがあります。

- アカウントポリシー
- 監査ポリシー
- セキュリティオプション
- ファイアウォール設定
- サービス設定

## Standalone-Windows-STIG-Scriptを使う利点：

- **自動化**：Windowsシステムの保護を自動化し、時間を節約するとともに、人為的ミスの可能性を減らします。

- **準拠**：STIGのガイドラインを適用し、Windowsシステムを業界標準に準拠させます。

- **安心感**：Standalone-Windows-STIG-Scriptを使うことで、Windowsシステムが保護され、業界標準に準拠していることを確認できます。

_________________________________________________________________________________________________________________________

## Standalone-Windows-STIG-Scriptの使い方：

1. Standalone-Windows-STIG-Scriptの使い方は比較的簡単です。次の手順に従ってください。

2. **スクリプトをダウンロードする**：スクリプトはGitHubの https://github.com/simeononsecurity/Standalone-Windows-STIG-Script から入手できます。ダウンロードしてWindowsシステムに保存します。

3. **管理者権限のコマンドプロンプトを開く**：Windowsのスタートボタンを右クリックし、「Windows PowerShell (Admin)」を選択します。

4. **スクリプトを実行する**：保存した場所に移動し、次のコマンドを入力して実行します。

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. 変更を確認する：スクリプトの実行後、システムに加えられた変更を確認し、すべてが正しく構成されていることを確認します。

## 結論：

Standalone-Windows-STIG-Scriptは、Windowsシステムを保護し、業界標準に準拠させるのに役立つツールです。保護のプロセスを自動化し、STIGのガイドラインを適用します。安全で準拠したWindowsシステムを作成する場合は、Standalone-Windows-STIG-Scriptの利用を検討してください。
