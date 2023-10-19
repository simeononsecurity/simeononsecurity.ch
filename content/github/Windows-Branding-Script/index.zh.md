---
title: "增强 Windows 和服务器系统：自定义品牌设置指南"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["视窗品牌", "服务器品牌", "定制品牌", "系统定制", "品牌设置", "Windows 10", "服务器 2016", "服务器 2019", "2022 服务器", "用户体验", "系统定制指南", "个性化", "系统品牌", "视窗定制", "服务器定制", "OEM 徽标", "用户图像", "客座形象", "品牌脚本", "微软安全合规工具包", "Windows 品牌设置", "服务器品牌设置", "定制品牌指南", "个性化品牌", "系统定制教程", "Windows 系统定制", "服务器系统定制", "品牌形象", "品牌推广最佳实践", "Windows 个性化提示", "服务器定制技术"]
---

在 Windows 10 和 Server 2016/2019/2022 系统上**设置品牌**

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## 如何设置品牌文件
- X] 将所有图像替换为品牌图像
  - [X] OEM 徽标必须是 95x95 或 120x20，格式为".bmp"。
  - X] 生成用户图像以及 32x32、40x40、48x48、192x192 变体。
  - [X] 生成或复制用户图像用于客人图像。
  
### 本脚本使用以下工具：
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

### 如何运行脚本
#### 手动安装：
如果是手动下载，则必须从管理 Powershell 中启动脚本，该目录中包含来自 [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
#### 自动安装：
可以像这样从 GitHub 下载的提取文件中启动脚本：
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/sosbranding.ps1'|iex
```

