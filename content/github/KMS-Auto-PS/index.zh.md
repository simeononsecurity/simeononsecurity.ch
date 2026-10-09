---
title: "使用 GLVK 脚本自动化 Windows KMS 激活"
date: 2020-12-18
toc: true
draft: false
description: 使用 SimeonOnSecurity 的 GLVK 自动安装脚本简化 Windows 10 和 Windows 11 的 KMS 激活过程，并通过微软推荐阅读了解更多关于 KMS 和 GLVK 客户端密钥的信息。
tags:
- Windows 激活
- KMS 客户端密钥
- GLVK
- Windows 更新
- 合规性
- Powershell 脚本
- 密钥管理服务
- 批量许可
- 企业激活
- 密钥管理服务器
- 自动化
- 微软产品
- 操作系统
- 软件
- 企业环境
- 管理员 Powershell
- GitHub 仓库
- 脚本编写
- 网络安全
- SimeonOnSecurity
- KMS 激活
- GLVK 自动安装脚本
- Windows 产品
- 企业
- 集中管理
- 节省时间
- IT 管理
- 简化激活
- 无忧无虑
- 生产力
- 减少错误
- 监控能力
- 效率
- 软件激活
- 批量许可密钥
- 脚本自动化
- IT 管理
- 激活流程
- 软件许可
- 许可管理
- 激活工具
- 软件部署
- IT 生产力
cover: /img/cover/KMS-Auto-PS.webp
coverAlt: 一个未来感十足的服务器，周围环绕着发光的客户端计算机，展示了在黑暗环境中以鲜艳色彩进行的 KMS 激活场景。画面强调数字连接和现代技术。
coverCaption: ''
lastmod: 2026-10-08
---

**GLVK 自动安装脚本用于 KMS 激活**

*推荐阅读：* [微软 - KMS 客户端密钥 (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## 介绍

KMS（密钥管理服务）激活是微软在企业环境中激活和授权其产品的一种方法。该过程涉及一个中央服务器，通过分配称为 GLVK（通用批量许可密钥）的批量许可密钥来激活客户端计算机。

本文将探讨 GLVK 自动安装脚本，它简化了使用 KMS 激活 Windows 产品的过程。我们将提供逐步操作指南，并强调该脚本对组织的益处。

## 推荐阅读

在深入了解 GLVK 自动安装脚本之前，建议先熟悉 KMS 的概念以及微软提供的可用 KMS 客户端密钥。您可以参考以下微软文档获取更多信息：

- [微软 - KMS 客户端密钥 (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## 如何运行脚本

### 手动安装

要手动安装并运行 GLVK 自动安装脚本，请按照以下步骤操作：

1. 从 [GitHub 仓库](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip) 下载脚本及相关文件。
2. 启动管理员权限的 PowerShell 会话。
3. 进入包含所有下载文件的目录。
4. 运行以下命令：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

这些命令将设置执行策略为 RemoteSigned 以允许运行脚本，解除任何下载的 PowerShell 脚本的阻止状态，并执行 GLVK 自动安装脚本。

## GLVK 自动安装脚本的优势

GLVK 自动安装脚本为希望使用 KMS 激活 Windows 产品的组织提供了多项优势：

1. **简化激活**：脚本自动化 KMS 激活过程，消除手动配置需求，减少人为错误。

2. **节省时间和精力**：利用该脚本，IT 管理员可以节省大量用于多台机器手动激活的时间和精力。

3. **集中管理**：GLVK 自动安装脚本支持 KMS 激活的集中管理，提供更好的控制和监控能力。

## 结论

GLVK 自动安装脚本是组织寻求高效且简化的 Windows 产品 KMS 激活方法的宝贵工具。通过自动化激活流程，它节省时间、减少错误并增强集中管理能力。借助提供的逐步指南，组织可以轻松实施该脚本，享受无忧的 KMS 激活体验。

## 参考文献

1. [微软 - KMS 客户端密钥 (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)
2. [GitHub 仓库 - GLVK 自动安装脚本](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
