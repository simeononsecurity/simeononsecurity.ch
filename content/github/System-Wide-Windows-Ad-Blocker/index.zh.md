---
title: "Windows 10 系统范围的广告拦截器脚本，可提供更好的隐私和安全性"
date: 2021-04-02
toc: true
draft: false
description: "使用此强大的 PowerShell 脚本在 Windows 10 上阻止广告、跟踪器和遥测，该脚本利用主机文件和 Windows 防火墙进行系统范围的广告拦截。"
tags: ["视窗 10", "广告拦截器", "遥测阻塞", "PowerShell脚本", "全系统广告拦截", "隐私", "安全", "简易列表", "轻松隐私", "NoCoin 过滤器列表", "AdGuard DNS 过滤器", "溜溜球列表", "Peter Lowe 的广告跟踪恶意软件服务器", "Windows 防火墙", "域列表", "阻止 Windows 跟踪器", "块跟踪器", "屏蔽广告", "块跟踪"]
---

＃＃ 描述：
此脚本通过主机文件阻止遥测相关域，并通过 Windows 防火墙阻止相关 IP。

**笔记：**
- 添加这些域可能会破坏某些软件，如 iTunes 或 Skype
- 据报道，与 Akamai 相关的条目会导致 Widevine DRM 出现问题

### 使用的列表：
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

＃＃＃ 例子：

自动运行最新版本的脚本：
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
