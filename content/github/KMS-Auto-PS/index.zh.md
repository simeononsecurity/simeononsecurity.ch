---
title: "使用 GLVK 脚本自动执行 Windows KMS 激活"
date: 2020-12-18
toc: true
draft: false
description: "使用 SimeonOnSecurity 的 GLVK 自动安装脚本简化 Windows 10 KMS 激活过程，并从 Microsoft 的推荐阅读中了解有关 KMS 和 GLVK 客户端密钥的更多信息。"
tags: ["Windows 激活", "KMS 客户端密钥", "GLVK", "Windows 更新", "遵守", "Powershell 脚本", "密钥管理服务", "批量许可", "企业激活", "密钥管理服务器", "自动化", "微软产品", "操作系统", "软件", "企业环境", "行政Powershell", "GitHub 资料库", "脚本", "网络安全", "西蒙论安全"]
---

用于 KMS 激活的 GLVK 自动安装脚本

## 推荐阅读：
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## 如何运行脚本：
### 手动安装：
如果手动下载，脚本必须从包含所有文件的目录中的管理 powershell 启动[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
