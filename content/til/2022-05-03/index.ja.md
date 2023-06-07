---
title: "今日はPowershellとAnsibleのモジュールをさらに勉強しました。"
date: 2022-05-03
toc: true
draft: false
description: ""
genre: ["オートメーション", "コンプライアンス", "アンシブル", "Ansible Playbooks（アンシブル プレイブック", "Ansibleコレクション", "Windowsのセキュリティ", "ウィンドウズ・アドミニストレーション", "パワーシェル", "ITオートメーション", "コンフィギュレーションマネジメント"]
tags: ["オートメーション", "コンプライアンス", "アンシブル", "Ansible Playbooks（アンシブル プレイブック", "Ansibleコレクション", "ギットハブ", "ランアズ", "インボークコマンド", "スタート-プロセス", "win_powershell（ウィンパワーシェル", "win_shell（ウィンシェル", "プセック", "ウィンペセック", "Windowsのセキュリティ", "ウィンドウズ・アドミニストレーション", "STIGの条件", "PowerShellモジュール", "Ansibleモジュール", "ウィンドウズ・オートメーション", "リモーティング", "シェルコマンド", "PowerShellコマンド", "Windows STIG Ansible", "Windows管理ツール", "コンフィギュレーションマネジメント", "ITオートメーションソリューション"]
---
SimeonOnSecurityが今日知って、面白いと思ったこと**。

SimeonOnSecurityは、Windows STIG Ansibleについて学び、関連レポを更新しました。また、powershell、リモーティング、invoke-command、start-process、win_powershell、win_shell、psexec、win_psexecなどのモジュールを使ったWindows上でのシェル/powershellコマンドの実行に関するMicrosoftとAnsibleの各種リソースを勉強しました。

## 新規/更新されたレポ

- [simeononsecurity/Windows_STIG_Ansible](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [simeononsecurity/windows_stigs](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## ラーニング・リソース
- [microsoft - invoke-command](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.2)
- [microsoft - start-process](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process?view=powershell-7.2)
- [microsoft - running remote commands](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.2)
- [ansible.windows.win_powershell](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_powershell_module.html)
- [ansible.windows.win_shell module](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_shell_module.html)
- [community.windows.psexec](https://docs.ansible.com/ansible/latest/collections/community/windows/psexec_module.html)
- [win_psexec](https://docs.ansible.com/ansible/2.5/modules/win_psexec_module.html)
