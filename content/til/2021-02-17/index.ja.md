---
title: "今日はPowerShellとBashでJSONを操作してパースする方法を学びました。"
date: 2021-02-18
toc: true
draft: false
genre: ["オートメーション", "コンプライアンス", "Windowsのセキュリティ", "Ansible Playbooks（アンシブル プレイブック", "Ansibleコレクション", "ITセキュリティ", "コンフィギュレーションマネジメント", "デブオプス", "ウィンドウズ・アドミニストレーション", "システム構成"]
tags: ["オートメーション", "コンプライアンス", "アンシブル", "Windowsのセキュリティ", "Ansible Playbooks（アンシブル プレイブック", "Ansibleコレクション", "ウィンドウズSTIG", "コンフィギュレーションマネジメント", "デブオプス", "ITセキュリティ", "ウィンドウズ・アドミニストレーション", "システム構成", "ウィンドウズ・オートメーション", "STIGコンプライアンス", "Windows_STIG_Ansible", "ウィンドウズ_STIGs", "ギットハブ", "ブロック", "レスキュー", "常に", "Windowsオートメーションガイド", "Windowsセキュリティの自動化", "セキュリティ・コンプライアンス", "Ansibleオートメーション", "STIGの条件", "Ansibleモジュール", "Windowsの構成", "Windows管理ツール", "オートメーションフレームワーク", "ITインフラの自動化", "コンフィギュレーション・コンプライアンス", "Windowsセキュリティのベストプラクティス"]
---

**SimeonOnSecurityが今日知ったこと、興味を持ったこと**。

SimeonOnSecurityは、彼のウェブサイトのページを更新し、彼が興味深いと思ういくつかのリソースについて学びました。更新されたページは、HackTheBoxのInvite Challengeの書き出しです。このページでは、WindowsとLinuxの両方のシステムで課題を解決するプロセスの詳細な分析が行われています。

SimeonOnSecurityは、更新されたページに加えて、いくつかの有用な学習リソースも発見しました。そのリソースの1つが、Cameron Nokes氏によるブログ記事で、jqツールを使ってbashでJSONを扱うことに焦点を当てています。jqツールは、JSONデータの解析、フィルタリング、操作を簡単に行うことができるコマンドラインユーティリティです。

もう2つのリソースは、PowerShellでのJSONデータの変換に関連するものです。Microsoftのドキュメントには、ConvertFrom-JsonおよびConvertTo-Jsonコマンドレットに関する情報が記載されています。これらのコマンドレットを使用すると、JSONデータをPowerShellオブジェクトに変換したり、PowerShellオブジェクトから変換したりすることができ、データの操作や分析が容易になります。

## Updated Pages：
- [HackTheBox - Invite Challenge (Windows/Linux)](https://simeononsecurity.ch/writeups/hackthebox-invite-challenge/)

## ラーニング・リソース
- [Cameron Nokes - Working with JSON in bash using jq](https://cameronnokes.com/blog/working-with-json-in-bash-using-jq/)
- [Microsoft - ConvertFrom-Json](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json?view=powershell-7.1)
- [Microsoft - ConvertTo-Json](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-json?view=powershell-7.1)