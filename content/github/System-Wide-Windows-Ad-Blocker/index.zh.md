---
title: "Windows 10 系统范围的广告拦截器脚本，可提供更好的隐私和安全性"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "使用 PowerShell 脚本在 Windows 中屏蔽 StevenBlack 列表中的域名，同时保留 hosts 文件中的自定义条目。"
tags: ["视窗 10", "广告拦截器", "遥测阻塞", "PowerShell脚本", "全系统广告拦截", "隐私", "安全"]
---

使用 PowerShell 脚本在 Windows 中屏蔽 StevenBlack 列表中的域名，同时保留 hosts 文件中的自定义条目。

## 准备和预览

下载并解压完整的仓库。运行前查看 [GitHub 上的 README](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) 和脚本。在解压后的目录中以管理员身份打开 Windows PowerShell 5.1 或 PowerShell 7。先在可丢弃的 Windows 测试环境中验证 DNS 和所需应用。

先预览更改。确认要应用后，再单独运行第二条命令。

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## 恢复原始 hosts 文件

先预览恢复操作。确认要恢复后，再单独运行第二条命令。

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

恢复成功前，请保持备份完整。如果应用更改后有用户或应用程序修改了 hosts 文件，恢复操作会停止。请先保存并协调这些修改，再重试。

## 屏蔽列表

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [报告问题](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
