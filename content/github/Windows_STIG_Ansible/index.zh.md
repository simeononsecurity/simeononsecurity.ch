---
title: "使用 Ansible STIG Playbook 自动执行 Windows 合规性"
date: 2022-04-26
toc: true
draft: false
description: "使用适用于 Windows 系统的 Ansible STIG Playbook 简化您的安全合规性。"
tags: ["自动化", "Windows 合规性", "Ansible STIG 剧本", "Windows强化", "STIG 脚本", "STIG 合规性", "银河系", "电源外壳", "PowerShell 脚本", "视窗伺服器", "Windows Defender的", "。网", "火狐", "甲骨文 JRE 8", "Adobe Reader DC", "互联网连接", "离线兼容性", "安全加固", "Windows 安全"]
---


SimeonOnSecurity 的 STIG 脚本的 Ansible 剧本

## 注意事项：

- 目前需要互联网连接。 （离线兼容性 WIP）

＃＃ 用法：

＃＃ 安装：

-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

```bash
ansible-galaxy collection install simeononsecurity.windows_stigs
```

＃＃ 基于：

-[simeononsecurity/STIG-Compliant-Domain-Prep](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)
-[simeononsecurity/Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[simeononsecurity/Standalone-Windows-Server-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-Server-STIG-Script)
-[simeononsecurity/Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[simeononsecurity/.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[simeononsecurity/FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[simeononsecurity/Oracle-JRE-8-STIG-Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script)
-[simeononsecurity/Adobe-Reader-DC-STIG-Script](https://github.com/simeononsecurity/Adobe-Reader-DC-STIG-Script)
