---
title: "プライバシーとセキュリティを向上させる Windows 10 システム全体の広告ブロッカー スクリプト"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "カスタムの hosts エントリを保持する PowerShell スクリプトで、Windows 上で StevenBlack のリストにあるドメインをブロックします。"
tags: ["ウィンドウズ10", "広告ブロッカー", "テレメトリのブロック", "PowerShell スクリプト", "システム全体の広告ブロック", "プライバシー", "安全"]
---

カスタムの hosts エントリを保持する PowerShell スクリプトで、Windows 上で StevenBlack のリストにあるドメインをブロックします。

## 準備とプレビュー

リポジトリ全体をダウンロードして展開します。実行前に [GitHub の README](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) とスクリプトを確認してください。展開したフォルダーで Windows PowerShell 5.1 または PowerShell 7 を管理者として開きます。まず使い捨ての Windows テスト環境で DNS と必要なアプリを確認してください。

最初のコマンドで変更内容を確認します。適用する準備ができたら、2 番目のコマンドを別途実行してください。

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## 元の hosts ファイルを復元

最初のコマンドで復元内容を確認します。復元する準備ができたら、2 番目のコマンドを別途実行してください。

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

復元が成功するまでバックアップを変更せずに保管してください。適用後に別のユーザーやアプリが hosts ファイルを編集した場合、復元は中止されます。変更内容を保存し、差分を調整してから再試行してください。

## ブロックリスト

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [問題を報告](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
