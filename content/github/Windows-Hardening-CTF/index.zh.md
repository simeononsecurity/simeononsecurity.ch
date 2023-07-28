---
title: "Windows 加固 CTF：加强 Windows 设备在夺旗战活动中的安全性"
date: 2020-10-19
toc: true
draft: false
description: "探索一个功能强大的脚本，该脚本可通过实施各种加固措施来增强 Windows 的安全性，从而阻止入侵。"
tags: ["窗口加固", "视窗安全", "脚本", "Windows 设备", "命令提示符", "LLMNR", "PowerShell", "中小型企业", "TCP 时间戳", "应用程序锁", "视窗登录", "环境保护部", "EMET 配置", "PowerShell 限制语言模式", "SMB 加密", "Spectre 和 Meltdown 缓解措施", "Windows Defender", "Windows 防火墙", "PSWindowsUpdate", "视窗更新", "加固脚本", "美国国家安全局建议的政策", "Windows 日志和安全控制", "Windows Defender 应用程序控制", "Windows Defender 攻击面减少程序", "Windows Defender 基于云的保护", "Windows Defender 漏洞保护", "安装 PSWindowsUpdate", "Windows 设备安全增强", "视窗加固措施", "加强视窗安全"]
---

**窗口加固-CTF***
一款 Windows 加固脚本，可使入侵 Windows 设备变得更加困难和恼人。

## 这个脚本有什么作用？
- 禁用命令提示符
- 禁用 LLMNR
- 禁用 PowerShell v2
- 禁用 SMB 压缩
- 禁用 SMB v1
- 禁用 SMB v2
- 禁用 TCP 时间戳
- 禁用 WSMAN 和 PSRemoting
- 启用带有 NSA 建议策略的 AppLocker
- 启用最佳实践 Windows 日志和安全控制
- 启用 DEP
- 启用 EMET 配置（仅适用于已安装 EMET 的系统）
- 启用 PowerShell 串联语言模式
- 启用 PowerShell 日志
- 启用 SMB 加密
- 启用 Spectre 和 Meltdown 缓解功能
- 启用 Windows Defender 应用程序控制
- 启用 Windows Defender 攻击面缩小程序
- 启用 Windows Defender 基于云的保护
- 启用 Windows Defender 漏洞利用保护
- 启用 Windows 防火墙和日志记录
- 安装 PSWindowsUpdate 并安装所有可用的 Windows 更新

## 下载所需文件：

从 [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## 如何运行脚本：

**从 GitHub 下载提取的脚本可以这样运行：**
```
.\sos-windows-hardening-ctf.ps1
```
