---
title: "今天我学习了更多 Powershell 和 Ansible 模块"
date: 2022-05-03
toc: true
draft: false
description: ""
genre: ["自动化", "合规性", "Ansible", "Ansible 操作手册", "Ansible 套件", "视窗安全", "视窗管理", "PowerShell", "IT 自动化", "配置管理"]
tags: ["自动化", "合规性", "Ansible", "Ansible 操作手册", "Ansible 套件", "GitHub", "运行", "调用命令", "启动-流程", "win_powershell", "win_shell", "psexec", "win_psexec", "视窗安全", "视窗管理", "STIG 要求", "PowerShell 模块", "Ansible 模块", "视窗自动化", "远程", "shell 命令", "PowerShell 命令", "Windows STIG Ansible", "Windows 管理工具", "配置管理", "IT 自动化解决方案"]
---
SimeonOnSecurity 今天了解到并觉得有趣**

SimeonOnSecurity 学习了 Windows STIG Ansible 并更新了相关 repos。此外，还学习了与 powerhell、远程控制以及使用 invoke-command、start-process、win_powershell、win_shell、psexec 和 win_psexec 等模块在 Windows 上执行 shell/powershell 命令有关的各种 Microsoft 和 Ansible 资源。

### 新增/更新 Repos：

- [simeononsecurity/Windows_STIG_Ansible](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [simeononsecurity/windows_stigs](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## 学习资源：
- [microsoft - invoke-command](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.2)
- [microsoft - start-process](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process?view=powershell-7.2)
- [microsoft - running remote commands](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.2)
- [ansible.windows.win_powershell](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_powershell_module.html)
- [ansible.windows.win_shell module](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_shell_module.html)
- [community.windows.psexec](https://docs.ansible.com/ansible/latest/collections/community/windows/psexec_module.html)
- [win_psexec](https://docs.ansible.com/ansible/2.5/modules/win_psexec_module.html)
