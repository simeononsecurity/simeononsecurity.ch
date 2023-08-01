---
title: "Today I Learned about Ansible and Block/Rescue Modules"
date: 2022-05-02
toc: true
draft: false
description: ""
genre: ["オートメーション", "コンプライアンス", "アンシブル", "Ansible Playbooks", "Ansibleコレクション", "Windowsセキュリティ", "ウィンドウズ管理", "セキュリティ・コンプライアンス", "ITオートメーション", "コンフィギュレーション管理"]
tags: ["オートメーション", "コンプライアンス", "アンシブル", "Ansible Playbooks", "Ansibleコレクション", "ギットハブ", "ブロック", "レスキュー", "常に", "Windowsセキュリティ", "ウィンドウズ管理", "STIGの要件", "セキュリティ・オートメーション", "コンフィギュレーション管理", "ITセキュリティ", "Ansibleモジュール", "ウィンドウズ・オートメーション", "アンシブル・ギャラクシー", "ウィンドウズSTIG", "Windows管理ツール", "セキュリティ技術導入ガイド", "アンシブル・コンテンツ", "Windowsセキュリティのベストプラクティス", "ITオートメーション・ソリューション", "セキュリティ監査", "Windowsシステム構成"]
---
SimeonOnSecurityが今日知り、面白いと思ったこと**。

SimeonOnSecurityは今日、WindowsのセキュリティとAnsibleを使った自動化に関するいくつかの興味深いことを学び、発見した。

まず、2つの新しく更新されたリポジトリが確認された。Windows_STIG_Ansible リポジトリは、Ansible 自動化プラットフォームを使用して、Windows システムをセキュリティ技術実装ガイド (STIG) 要件を満たすように構成するための完全なソリューションを提供します。windows_stigsリポジトリは、STIG要件を満たすためにWindowsシステムを構成するためのAnsibleロールのコレクションであり、Ansibleコンテンツを共有するための中央リポジトリであるAnsible Galaxyで利用できます。

SimeonOnSecurityは、AnsibleによるWindows自動化に関連する学習リソースもいくつか見つけました。ansible.windows.win_copyモジュールのドキュメントには、Ansibleを使用してWindowsシステム上でファイルをコピーする方法に関する情報が記載されています。ansible blocksドキュメントは、複数のタスクをグループ化し、条件付き実行を適用できるAnsibleの強力な機能であるブロックの使用方法に関する情報を提供します。ansible galaxy ユーザー・ガイド』には、Ansible Galaxy の使用方法に関する情報が記載されており、『ansible installing content』には、Ansible Galaxy からコンテンツをインストールする方法に関する情報が記載されています。

## 新規/更新レポ

- [simeononsecurity/Windows_STIG_Ansible](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [simeononsecurity/windows_stigs](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

#学習リソース
- [ansible.windows.win_copy module](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_copy_module.html)
- [ansible blocks](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html)
- [ansible galaxy user guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html)
- [ansible installing content](https://galaxy.ansible.com/docs/using/installing.html)