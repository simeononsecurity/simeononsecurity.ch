---
title: "Today I Learned about Ansible and Block/Rescue Modules"
date: 2022-05-02
toc: true
draft: false
description: ""
genre: ["自动化", "合规性", "Ansible", "Ansible 操作手册", "Ansible 套件", "视窗安全", "视窗管理", "安全合规", "IT 自动化", "配置管理"]
tags: ["自动化", "合规性", "Ansible", "Ansible 操作手册", "Ansible 套件", "GitHub", "街区", "救援", "始终如一", "视窗安全", "视窗管理", "STIG 要求", "安全自动化", "配置管理", "信息技术安全", "Ansible 模块", "视窗自动化", "Ansible Galaxy", "视窗 STIG", "Windows 管理工具", "安全技术实施指南", "Ansible 内容", "Windows 安全最佳实践", "IT 自动化解决方案", "安全审计", "视窗系统配置"]
---
SimeonOnSecurity 今天了解到并觉得有趣**

SimeonOnSecurity 今天学习并发现了几件与 Windows 安全和使用 Ansible 进行自动化有关的有趣事情。

首先，我们发现了两个新的更新版本库。Windows_STIG_Ansible 资源库为使用 Ansible 自动化平台配置 Windows 系统以满足《安全技术实施指南》（STIG）要求提供了完整的解决方案。windows_stigs 资源库是用于配置 Windows 系统以满足 STIG 要求的 Ansible 角色的集合，可在 Ansible Galaxy（一个用于共享 Ansible 内容的中央资源库）上使用。

SimeonOnSecurity 还找到了几个与使用 Ansible 进行 Windows 自动化相关的学习资源。ansible.windows.win_copy 模块文档提供了如何使用 Ansible 在 Windows 系统上复制文件的信息。ansible blocks 文档提供了有关如何使用块的信息，这是 Ansible 的一项强大功能，允许您将多个任务组合在一起并应用条件执行。ansible galaxy 用户指南提供了如何使用 Ansible Galaxy 的信息，ansible installing content 文档提供了如何从 Ansible Galaxy 安装内容的信息。

### 新的/更新的 Repos：

- [simeononsecurity/Windows_STIG_Ansible](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [simeononsecurity/windows_stigs](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## 学习资源：
- [ansible.windows.win_copy module](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_copy_module.html)
- [ansible blocks](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html)
- [ansible galaxy user guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html)
- [ansible installing content](https://galaxy.ansible.com/docs/using/installing.html)