---
title: "PowerShell スクリプトを使用して FireFox STIG コンプライアンスを自動化する"
date: 2020-08-15
---

FireFox STIG スクリプト

の[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip) STIG の中で最も簡単に適用できるものではありません。
このスクリプトは、必要な FireFox ポリシーのほとんどを実装します。将来的には、FireFox ADMX テンプレートと GPO がこのスクリプトに適用される予定です。

**作業中**

## 必要なファイルをダウンロードします

から必要なファイルをダウンロードします。[GitHub Repository](https://github.com/simeononsecurity/FireFox-STIG-Script)

## スクリプトの実行方法


**スクリプトは、次のように抽出された GitHub ダウンロードから起動できます:**
```
.\sos-firefoxstig.ps1
```