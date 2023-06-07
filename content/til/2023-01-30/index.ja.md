---
title: "今日は「Windowsのカスタムイメージ作成」について学びました。"
date: 2023-01-30
toc: true
draft: false
description: "今日は、Windowsのカスタムイメージ作成、Sysprep、一般化について学びました。"
genre: ["Windowsのイメージ管理", "カスタマイズ", "Windowsの展開", "シスプリ", "一般化", "ウィンドウズ10", "ウィンドウズ11", "イメージキャプチャー", "画像展開", "エヌティーライト", "Windowsの最適化"]
tags: ["シスプリ", "エヌティーライト", "一般化", "カスタムイメージ", "カスタムウィンドウのイメージ", "ウィンドウズ11", "デブロート", "カスタマイズ", "イメージキャプチャ", "イメージ展開", "Windowsのイメージ管理", "Windowsのデプロイメントツール", "Windowsイメージのカスタマイズ", "Windowsイメージの最適化", "Microsoft Learn", "WinCustomリポジトリ"]
---

**SimeonOnSecurityが今日知ったこと、興味を持ったこと**。

本日、SimeonOnSecurityは、Windowsイメージを管理するために使用されるコマンドラインツールであるDISMを使用して、Windows 10イメージをキャプチャし適用するプロセスについて学びました。イメージを取り込むには、Sysprepツールを使用してインストールを一般化し、ハードウェア固有の情報を削除して、複数のデバイスに展開するためのイメージを準備することができます。

SimeonOnSecurityは、Windowsイメージのキャプチャと適用に関する情報を提供する、MicrosoftのLearnサイトやGitHubのWinCustomリポジトリなど、さまざまなリソースを紹介されました。Microsoftのリソースでは、単一の.WIMファイルを使用したWindowsイメージのキャプチャと適用の基本、ブータブルWindows PEメディアの作成、SysprepによるWindowsインストールの一般化について説明されています。

さらに、SimeonOnSecurityは、Windowsイメージのカスタマイズと最適化を可能にするソフトウェアであるNTLiteについて学びました。NTLiteを使用することで、Windowsイメージから不要なコンポーネントを削除し、ディスクスペースを節約してパフォーマンスを向上させることができます。

全体として、SimeonOnSecurityの今日の研究は、Windowsイメージのキャプチャと適用のプロセスについて包括的に理解することができました。

## 作成/更新されたレポ
- なし / 該当なし

## 学習リソース
- [Learn How to Sysprep Capture Windows 10 Image using DISM](https://www.anoopcnair.com/sysprep-capture-windows-10-image-using-dism/)
- [Microsoft - Capture and apply a Windows image using a single .WIM file](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11)
- [Microsoft - Create bootable Windows PE media](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive?view=windows-11)
- [Microsoft - Sysprep (Generalize) a Windows installation](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11)
- [WinTenDev/WinCustom](https://github.com/WinTenDev/WinCustom)

## 議論された、または利用されたソフトウェア：
- [NTLite](https://www.ntlite.com/)