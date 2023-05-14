---
title: "Windows システム向けの自動ブランディング - デスクトップ、ロック画面などを簡単に制御"
date: 2020-08-14
---


多くの組織は、Windows システムのブランドを制御する必要がある、または制御したいと考えています。
これには、デスクトップの壁紙、ユーザーのアバター、Windows ロック画面、および場合によっては OEM ロゴが含まれます。
Windows 10、Windows Server 2016、および Windows Server 2019 では、これは特に簡単ではありません。
ただし、リンクされたスクリプトを使用すると、部分的に自動化し、プロセスをはるかに簡単にすることができます。

## 必要なファイルをダウンロードします

**必要なファイルを次の場所からダウンロードします。[GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## ブランド化ファイルの設定方法

- [X] すべての画像をブランド画像に置き換えます
  - [X] OEM ロゴは 95x95 または 120x20 で、「.bmp」形式である必要があります。
  - [X] 32x32、40x40、48x48、192x192 のバリアントとともにユーザー イメージを生成します。
  - [X] ゲスト イメージのユーザー イメージを生成またはコピーします。

## スクリプトの実行方法
```
.\sos-copybranding.ps1
```

## このスクリプトは次のツールを利用します。

-[Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
