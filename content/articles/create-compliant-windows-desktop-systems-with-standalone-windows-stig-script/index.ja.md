---
title: "サイバーセキュリティの力：Standalone-Windows-STIG-Scriptでコンプライアンス＆セキュアなWindowsシステムを構築する方法"
date: 2023-02-02
toc: true
draft: false
description: "使いやすいStandalone-Windows-STIG-Scriptで、安全でコンプライアンスに優れたWindowsシステムを構築する方法をご紹介します。この記事では、ステップバイステップの手順と詳細なパラメータ解説を掲載しています。"
tags: ["STIGスクリプト", "Windowsのセキュリティ", "準拠のWindowsシステム", "システムハードニング", "ウィンドウズSTIG", "セキュアウィンドウズ", "Windows コンプライアンス", "マニュアルインストール", "Windowsのアップデート", "アドビリーダー", "ファイアフォックス", "クローム", "インターネットエクスプローラー11", ".NET Framework", "オフィス", "OneDrive（ワンドライブ", "Java", "Windows Defender", "Windowsファイアウォール", "ミティゲーション", "ネサスPID", "VMware Horizon", "オプションの焼入れ"]
cover: "/img/cover/A_screenshot_of_a_computer_screen_with_with_a_progress_bar.png"
coverAlt: "完成度を示すプログレスバーが表示されたパソコン画面のスクリーンショットです。"
coverCaption: ""
---

Windowsシステムは、企業、組織、そして家庭でも広く使用されています。サイバー攻撃が増加する中、これらのシステムが安全で業界標準に準拠していることを確認することが極めて重要です。Standalone-Windows-STIG-Scriptは、まさにそれを実現するための便利なツールです。この記事では、Standalone-Windows-STIG-Scriptとは何か、どのように機能するのか、そして安全で準拠したWindowsシステムを作成するためにどのように使用できるのかを探ります。

## Standalone-Windows-STIG-Scriptとは何ですか？

**Standalone-Windows-STIG-Script**は、Simeononsecurity社によって開発されたスクリプトで、Windowsシステムを安全かつセキュリティ技術実装ガイド（STIG）に準拠させるプロセスを自動化するために設計されています。このスクリプトはオープンソースで、**GitHub**で公開されています。

## How does it work?

Standalone-Windows-STIG-Script は、Windows システムのセキュリティを確保するために STIG で提供されるガイドラインを実装します。このスクリプトはWindowsシステム上で実行することができ、STIGに準拠するために必要な変更をシステムに加えます。このスクリプトは、以下を含むがこれらに限定されない幅広いセキュリティ対策をカバーしている：

- アカウントポリシー
- 監査ポリシー
- セキュリティ・オプション
- ファイアウォール設定
- サービス設定

## Standalone-Windows-STIG-Scriptを使用するメリット：

- **Automation**：このスクリプトは、Windowsシステムのセキュリティを確保するプロセスを自動化するため、時間を節約し、人的ミスの可能性を排除します。

- コンプライアンス**：スクリプトは、STIGで提供されるガイドラインを実装し、Windowsシステムが業界標準に準拠することを保証します。

- 安心感**：Standalone-Windows-STIG-Scriptを使用することで、Windowsシステムが安全で業界標準に準拠していることに安心感を持つことができます。

_________________________________________________________________________________________________________________________

## Standalone-Windows-STIG-Scriptの使用方法：

1.Standalone-Windows-STIG-Scriptの使い方は比較的簡単です。以下、スクリプトを使用する手順を説明します：

2.**スクリプトをダウンロードします：スクリプトはGitHub（https://github.com/simeononsecurity/Standalone-Windows-STIG-Script）で公開されています。スクリプトをダウンロードし、Windows システムに保存します。

3.**昇格コマンドプロンプトを開く**：Windowsのスタートボタンを右クリックし、「Windows PowerShell (Admin)」を選択します。

4.**スクリプトを実行する**：スクリプトの実行**：スクリプトを保存した場所に移動し、以下のコマンドを入力してスクリプトを実行します：

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5.変更点を確認するスクリプトの実行が終了したら、システムに加えられた変更を確認し、すべてが正しく構成されていることを確認します。

## 結論

結論：Standalone-Windows-STIG-Scriptは、Windowsシステムのセキュリティ確保と業界標準への準拠を支援する有用なツールである。このスクリプトを使用することで、Windows システムのセキュリティ保護プロセスを自動化し、STIG に準拠していることを確認し、システムが安全であることに安心感を与えることができます。従って、準拠した安全なWindowsシステムを作成したい場合は、Standalone-Windows-STIG-Scriptの使用を検討してください。