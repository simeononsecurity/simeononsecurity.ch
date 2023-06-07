---
title: "Today I Learned about Ansible and Block/Rescue Modules"
date: 2022-05-02
toc: true
draft: false
description: ""
genre: ["オートメーション", "コンプライアンス", "アンシブル", "Ansible Playbooks（アンシブル プレイブック", "Ansibleコレクション", "Windowsのセキュリティ", "ウィンドウズ・アドミニストレーション", "セキュリティ・コンプライアンス", "ITオートメーション", "コンフィギュレーションマネジメント"]
tags: ["オートメーション", "コンプライアンス", "アンシブル", "Ansible Playbooks（アンシブル プレイブック", "Ansibleコレクション", "ギットハブ", "ブロック", "レスキュー", "常に", "Windowsのセキュリティ", "ウィンドウズ・アドミニストレーション", "STIGの条件", "セキュリティオートメーション", "コンフィギュレーションマネジメント", "ITセキュリティ", "Ansibleモジュール", "ウィンドウズ・オートメーション", "Ansible Galaxy（アンシブル・ギャラクシー", "ウィンドウズSTIG", "Windows管理ツール", "セキュリティ技術実装ガイド", "Ansibleコンテンツ", "Windowsセキュリティのベストプラクティス", "ITオートメーションソリューション", "セキュリティ監査", "Windowsのシステム構成"]
---
SimeonOnSecurityが今日知って、面白いと思ったこと**。

SimeonOnSecurityは今日、WindowsのセキュリティとAnsibleを使った自動化に関連して、いくつかの興味深いことを学び、発見しました。

まず、2つの新しいリポジトリと更新されたリポジトリが確認されました。Windows_STIG_Ansibleリポジトリは、Ansible自動化プラットフォームを使用して、セキュリティ技術実装ガイド（STIG）要件を満たすようにWindowsシステムを構成するための完全なソリューションを提供します。windows_stigsリポジトリは、STIG要件を満たすためにWindowsシステムを構成するためのAnsibleロールのコレクションであり、Ansibleコンテンツを共有するための中央リポジトリであるAnsible Galaxyで利用可能である。

SimeonOnSecurityは、AnsibleによるWindows自動化に関連する学習リソースもいくつか見つけました。ansible.windows.win_copyモジュールのドキュメントには、Ansibleを使用してWindowsシステム上でファイルをコピーする方法に関する情報が記載されています。ansible blocksドキュメントは、複数のタスクをグループ化し、条件付き実行を適用できるAnsibleの強力な機能であるブロックの使用方法に関する情報を提供します。ansible galaxyユーザーガイドには、Ansible Galaxyの使用方法に関する情報が、ansible installing contentドキュメントには、Ansible Galaxyからコンテンツをインストールする方法に関する情報が記載されています。

## 新規/更新されたレポです：

- [simeononsecurity/Windows_STIG_Ansible](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [simeononsecurity/windows_stigs](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## ラーニング・リソース
- [ansible.windows.win_copy module](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_copy_module.html)
- [ansible blocks](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html)
- [ansible galaxy user guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html)
- [ansible installing content](https://galaxy.ansible.com/docs/using/installing.html)