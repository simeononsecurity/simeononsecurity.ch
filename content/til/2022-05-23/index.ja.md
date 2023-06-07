---
title: "今日は「ショコラパッケージの作り方」を学びました"
date: 2022-05-23
toc: true
draft: false
description: "今日はAnsibleの条件分岐と変数管理について詳しく学びました"
genre: ["オートメーション", "Windowsのパッケージ管理", "パッケージ作成", "パッケージ管理", "IaC（Infrastructure as Code）とは", "Windowsソフトウエアのデプロイメント", "ソフトウェアパッケージ", "ウィンドウズ・オートメーション", "パッケージリポジトリ", "Windowsツール"]
tags: ["オートメーション", "パワーシェル", "ショコラティエパッケージマネージャー", "ショコラトリー", "チョコ", "パッケージ作成", "パッケージオートメーション", "ヌーペック", "ネソール", "Windowsパッケージマネージャ", "アイエーシー", "コードとしてのインフラ", "Windows ソフトウェアの展開", "ソフトウェアパッケージング", "リポジトリ管理", "パッケージシェアリング", "ショコラトリー・ドキュメント", "チュートリアル", "パッケージ出版"]
---

**SimeonOnSecurityが今日知ったこと、興味を持ったこと**。

今日、SimeonOnSecurityはChocolateyパッケージマネージャのパッケージを作成するプロセスについて学びました。ChocolateyはWindows用のパッケージマネージャで、アプリケーションやツールのインストール、アップグレード、管理を簡単に行うことができます。パッケージを作成することで、SimeonOnSecurityはソフトウェアのインストールを自動化したり、コミュニティで他の人とパッケージを共有することができます。

SimeonOnSecurityは、Chocolateyパッケージの作成に関連する2つのリポジトリをGitHub上に作成し、更新しました。最初のリポジトリ、simeononsecurity/Chocolatey-Nethorは、Nethorのためのパッケージです。2つ目のリポジトリ、simeononsecurity/chocolateypackagesは、SimeonOnSecurityが作成した様々なアプリケーションやツール用のパッケージの集合体である。

パッケージを作成するために、SimeonOnSecurityは、パッケージとその内容に関するメタデータを提供するNuspecファイル形式を使用しました。また、パッケージの作成プロセスでは、Install-ChocolateyInstallPackageやInstall-ChocolateyPackageなどの関数を使用して、インストールするソフトウェアや必要な依存関係を指定しました。

また、SimeonOnSecurityは、Chocolateyパッケージの作成と公開のプロセスについてより深く理解するために、Chocolatey公式ドキュメントやTop Bug Netによるチュートリアルなど、いくつかの学習リソースを確認しました。

全体として、SimeonOnSecurityは今日の学習で、Chocolateyパッケージマネージャのパッケージ作成プロセスを包括的に理解し、ソフトウェアのインストールを自動化したり、コミュニティの他の人とパッケージを共有したりすることが容易になりました。

## 作成・更新されたレポ
- [simeononsecurity/Chocolatey-Nethor](https://github.com/simeononsecurity/Chocolatey-Nethor)
- [simeononsecurity/chocolateypackages](https://github.com/simeononsecurity/chocolateypackages)

## Learning resources：
- [Chocolatey - Create Packages](https://docs.chocolatey.org/en-us/create/create-packages#nuspec)
- [Chocolatey - Install-ChocolateyInstallPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateyinstallpackage)
- [Chocolatey - Install-ChocolateyPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateypackage)
- [Top Bug Net - Create and Publish Chocolatey Packages](https://www.topbug.net/blog/2012/07/02/a-simple-tutorial-create-and-publish-chocolatey-packages/)