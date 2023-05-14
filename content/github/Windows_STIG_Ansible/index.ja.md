---
title: "Ansible STIG Playbook を使用して Windows コンプライアンスを自動化する"
date: 2022-04-26
toc: true
draft: false
description: "Windows システム用の Ansible STIG Playbook を使用してセキュリティ コンプライアンスを合理化します。"
tags: ["オートメーション", "Windows コンプライアンス", "Ansible STIG プレイブック", "Windows の強化", "STIG スクリプト", "STIG コンプライアンス", "アンシブルギャラクシー", "パワーシェル", "PowerShell スクリプト", "Windowsサーバー", "Windows ディフェンダー", "。ネット", "ファイアフォックス", "オラクル JRE 8", "Adobe Reader DC", "インターネット接続", "オフライン互換性", "セキュリティの強化", "Windows セキュリティ"]
---


SimeonOnSecurity の STIG スクリプト用の Ansible プレイブック

＃＃ ノート：

- 現在、インターネット接続が必要です。 (オフライン互換性 WIP)

＃＃ 使用法：

## インストール:

-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

```bash
ansible-galaxy collection install simeononsecurity.windows_stigs
```

＃＃ に基づく：

-[simeononsecurity/STIG-Compliant-Domain-Prep](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)
-[simeononsecurity/Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[simeononsecurity/Standalone-Windows-Server-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-Server-STIG-Script)
-[simeononsecurity/Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[simeononsecurity/.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[simeononsecurity/FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[simeononsecurity/Oracle-JRE-8-STIG-Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script)
-[simeononsecurity/Adobe-Reader-DC-STIG-Script](https://github.com/simeononsecurity/Adobe-Reader-DC-STIG-Script)
