---
title: "Windows Audit Policy ScriptでWindowsの監査を最大化する。"
date: 2021-05-10
toc: true
draft: false
description: "セキュリティと監視を強化するために、Windows監査ポリシースクリプトを実装することで、Windows監査を最大限に活用する方法をご紹介します。"
tags: ["Windowsの監査ポリシー", "Windowsの監査", "セキュリティ", "モニタリング", "監査警察", "ウィンドウズコマンド", "Windowsのセキュリティ", "監査構成", "安全保護方針", "イベントログ", "システムモニタリング", "ウィンドウズサーバー", "セキュリティベストプラクティス", "サイバーセキュリティ", "ログ解析", "セキュリティコンプライアンス", "インシデントレスポンス", "セキュリティモニタリングツール", "特権的アクセス", "ウィンドウズ・アドミニストレーション", "スクリプト", "システム管理", "情報セキュリティ", "コンプライアンス監査", "ウィンドウズ・ハード化", "セキュリティ制御", "セキュリティオートメーション", "ログ管理", "Windowsのセキュリティ設定"]
---

## Windows-Audit-Policy（ウィンドウズ・オーディット・ポリシー

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Windows Auditingの最大化

## おすすめ読み物
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## スクリプトの実行方法
### 手動インストール：
手動でダウンロードした場合、スクリプトを起動するためには、他のすべてのファイルを含むディレクトリから [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
