---
title: "Standalone-Windows-STIG-Script：打造符合要求的电脑"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "逐步介绍如何使用 Standalone-Windows-STIG-Script 配置符合要求的 Windows 系统，并说明参数和验证步骤。"
tags: ["STIG 脚本", "Windows 安全", "符合要求的 Windows 系统", "系统加固", "Windows STIG", "安全的 Windows", "Windows 合规", "手动安装", "Windows 更新", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Windows 防火墙", "风险缓解措施", "Nessus PID", "VMware Horizon", "可选加固"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "电脑屏幕上显示安全合规界面、动态进度条和数据流的插图，背景为深海军蓝并带有鲜明点缀色。"
coverCaption: ""
---

Windows 系统广泛用于企业、组织和家庭。随着网络攻击不断增加，你需要确保这些系统安全并符合行业标准。Standalone-Windows-STIG-Script 是一款有助于完成这项工作的工具。本文介绍该脚本的用途、工作方式，以及如何使用它创建安全且符合要求的 Windows 系统。

## 什么是 Standalone-Windows-STIG-Script？

**Standalone-Windows-STIG-Script** 是 Simeononsecurity 开发的脚本，用于自动按照 Security Technical Implementation Guide (STIG) 加固 Windows 系统。该脚本采用开源许可，可在 **GitHub** 上获取。

## 它如何工作？

Standalone-Windows-STIG-Script 会应用 STIG 中的指导来保护 Windows 系统。在 Windows 系统上运行后，它会进行符合 STIG 要求所需的更改。脚本涵盖多项安全措施，包括：

- 账户策略
- 审计策略
- 安全选项
- 防火墙设置
- 服务设置

## 使用 Standalone-Windows-STIG-Script 的好处：

- **自动化**：脚本自动执行 Windows 系统加固流程，节省时间并减少人为错误的可能性。

- **合规性**：脚本应用 STIG 指导，帮助 Windows 系统符合行业标准。

- **安心**：使用 Standalone-Windows-STIG-Script 后，你可以更放心地认为 Windows 系统已得到保护并符合行业标准。

_________________________________________________________________________________________________________________________

## 如何使用 Standalone-Windows-STIG-Script：

1. Standalone-Windows-STIG-Script 的使用相对简单。步骤如下：

2. **下载脚本**：脚本位于 GitHub（https://github.com/simeononsecurity/Standalone-Windows-STIG-Script）下载后保存到 Windows 系统中。

3. **打开提升权限的命令提示符**：右键单击 Windows“开始”按钮，然后选择 "Windows PowerShell (Admin)"。

4. **运行脚本**：转到保存脚本的位置，并输入以下命令运行：

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. 检查更改：脚本运行完毕后，查看系统所做的更改，确认配置符合预期。

## 结语：

Standalone-Windows-STIG-Script 有助于保护 Windows 系统并使其符合行业标准。它会自动执行加固流程并应用 STIG 指导。若要创建安全且符合要求的 Windows 系统，可以考虑使用 Standalone-Windows-STIG-Script。
