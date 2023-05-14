---
title: "GLVK スクリプトを使用して Windows KMS ライセンス認証を自動化する"
date: 2020-12-18
toc: true
draft: false
description: "SimeonOnSecurity の GLVK 自動インストール スクリプトを使用して Windows 10 KMS ライセンス認証プロセスを簡素化し、Microsoft の推奨資料から KMS および GLVK クライアント キーについて詳しく学習してください。"
tags: ["Windowsのアクティベーション", "KMS クライアントキー", "GLVK", "Windows アップデート", "コンプライアンス", "パワーシェルスクリプト", "鍵管理サービス", "ボリュームライセンス", "エンタープライズアクティベーション", "鍵管理サーバー", "オートメーション", "マイクロソフト製品", "オペレーティング·システム", "ソフトウェア", "エンタープライズ環境", "管理用 Powershell", "GitHub リポジトリ", "スクリプト作成", "サイバーセキュリティ", "SimeonOnセキュリティ"]
---

KMS アクティベーション用の GLVK 自動インストール スクリプト

## 推奨読書:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## スクリプトの実行方法:
### 手動インストール:
手動でダウンロードした場合、スクリプトは、[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
