---
title: "为什么 DNS 过滤会被绕过：检查解析器路径"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "查明设备或浏览器绕过 DNS 过滤的原因。比较直接查询和默认查询，检查日志，再核对加密 DNS、VPN、IPv6 和路由器设置。"
genre: ["家庭网络", "DNS", "隐私"]
tags: ["绕过 DNS 过滤", "绕过 Pi-hole", "DNS 查询日志", "浏览器安全 DNS", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "VPN DNS", "IPv6 DNS", "路由器 DHCP DNS", "Resolve-DnsName", "DNS 故障排查", "DNS 过滤器测试", "NextDNS 故障排查", "AdGuard DNS 故障排查"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "笔记本的蓝色 DNS 路径经过过滤器后停在阻止图标处，而浏览器的橙色路径则到达另一个解析器。"
coverCaption: "修改过滤规则前先追踪查询路径。"
---

你配置了过滤解析器，但某台设备仍能访问策略中应被阻止的域名。原因可能是规则、设备的 Domain Name System (DNS) 分配、浏览器的加密解析器或 VPN。**先测试路径，再更改设置。**直接查询过滤器与设备的普通查询回答的是不同问题。

<!--more-->

## 要点

- **先检查规则：**确认过滤器收到并阻止了安全的测试域名。
- **追踪每一层：**路由器、操作系统、浏览器、VPN 和移动设备设置都会影响 DNS 路由。
- **使用新查询：**将新的主机名和时间与过滤器查询日志对应起来。
- **说明证据边界：**一次观察到的查询只证明一条路径，不能证明所有应用或设备的行为。

## 开始前

预留约 20 分钟。你需要访问过滤解析器的查询日志，准备一台出现问题的设备，并记录路由器的 DNS 设置。示例使用 Windows 笔记本和 **Pi-hole**，但任何提供逐客户端查询日志的解析器都适用。先确定过滤器的准确地址。不要在公开报告中粘贴私有客户端地址、查询日志或策略规则。

选择一个策略已经阻止的**无害测试域名**。也可以在测试配置中临时添加一条精确拒绝规则，目标是你控制的域名。记录规则，并在测试后删除。不要使用仍在活动的恶意软件域名进行探测。被阻止的页面是有用的症状，但解析器日志能提供更有力的路径证据。

| 层级 | 问题 |
|---|---|
| **过滤器** | 直接查询是否到达预期解析器并匹配规则？ |
| **设备** | 网络分配了哪些 DNS 服务器？ |
| **浏览器或应用** | 客户端使用设备解析器还是单独的路径？ |
| **VPN 或中继** | 活动隧道是否改变了查询目的地？ |

## 验证过滤器是否工作

打开解析器的查询日志。将选定的被阻止域名直接发送给过滤器查询。在 Windows 上使用 PowerShell，并在提示时输入过滤器地址和测试域名：

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

Microsoft 的 [**`Resolve-DnsName`**参考文档](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname)将 **`-Server`**定义为向指定解析器发送查询。到过滤器日志中查找该查询，并检查响应和匹配规则。Pi-hole 的[查询和日志文档](https://docs.pi-hole.net/main/pihole-command/)介绍了本地查询工具。如果直接查询被允许，先修正规则或客户端组分配，再调查绕过。如果查询没有到达过滤器，则检查地址、服务和网络路径。

**这项直接测试不能证明笔记本平时使用该过滤器。**选项 **`-Server`**只在此查询中覆盖默认解析器。区分两者可以避免常见的假阳性。

## 追踪设备路径

使用新的主机名，避免命中旧的 DNS 缓存记录。下面的示例将一个查询直接发送给过滤器，另一个通过笔记本的常规解析器选择发送。两个名称不同，因此你可以判断日志条目对应哪条路径。**NXDOMAIN**响应表示 DNS 服务器报告该主机名不存在。如果随机名称没有被使用，这属于正常情况。此处要看的是查询是否出现在过滤器日志中。

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

在过滤器日志中搜索两个完整名称，并记录时间和报告的客户端。如果 **`direct-`**出现而 **`default-`**没有出现，请检查分配给笔记本的 DNS 服务器。Windows 的 **`Get-DnsClientServerAddress`**会按接口显示 DNS 服务器地址。检查当前使用的 Wi-Fi 或以太网适配器，不要检查已断开的适配器。Microsoft 的 [DNS 客户端参考文档](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress)说明了这个只读命令。

第一次测试时保留错误输出。错误或超时需要单独诊断，与查询日志中没有条目并不相同。

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

比较 IPv4 和 IPv6 行。**DHCP**分配 DNS 服务器等网络设置。**IPv6**是较新的 Internet Protocol 地址族，使用 128 位地址。IPv4 租约可能指定了过滤器，但 IPv6 路由器通告仍提供另一个 DNS 服务器。检查路由器的 **DHCP**和**IPv6 DNS**通告，修正后续订设备的网络租约。Pi-hole 的[安装后指南](https://docs.pi-hole.net/main/post-install/)说明 DHCP 如何将客户端指向 Pi-hole。[路由器示例](https://docs.pi-hole.net/routers/fritzbox/)介绍了 IPv6 DNS 通告。

如果日志将**路由器**显示为客户端，路由器可能代表设备转发查询。此时过滤器日志只能证明路由器到达了过滤器，不能证明哪个设备发起了查询。先确认路由器的转发设计，再判断客户端身份是否确实缺失。

## 检查浏览器 DNS

命令行查询测试的是设备解析器路径。浏览器可能改用 **DNS over HTTPS (DoH)**。在浏览器中打开同一个被阻止的测试域名，并在过滤器日志中查找对应查询。如果缓存结果影响比较，请清除浏览器 DNS 缓存，或使用测试规则覆盖的新主机名。

在电脑上的 **Chrome** 中打开 **设置 > 隐私和安全 > 安全 > 使用安全 DNS**。根据 [Google Chrome 帮助](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en)，自动模式使用当前提供商，失败时会回退到未加密查询。选择自定义提供商后不会以同样方式回退。更改前记录当前模式和提供商。

在 **Firefox** 中打开 **设置 > 隐私与安全 > DNS over HTTPS**。[Mozilla 保护级别指南](https://support.mozilla.org/en-US/kb/dns-over-https)区分默认、增强、最大、自定义和关闭模式。[DoH 概述](https://support.mozilla.org/en-US/kb/firefox-dns-over-https)说明浏览器解析器何时会绕过本地 DNS 过滤器。一次只更改一项设置并重新测试，然后恢复所需的隐私设置。

**不要把每个浏览器查询缺失都称为绕过。**浏览器可能复用了缓存数据、访问了已知地址，或使用了代理。得出查询去向的结论前，请对比新名称、对应时间窗口和浏览器解析器设置。

## 检查移动设备和 VPN 路径

在 **Android** 上检查 **设置 > 网络和互联网 > 私人 DNS**。提供商主机名会选择一项不同于路由器通告 DNS 的私人 DNS 服务。Google 的 [Android 网络设置说明](https://support.google.com/android/answer/9654714?hl=en)介绍了关闭、自动和提供商主机名选项。若要获得受控的本地结果，请在 Wi-Fi 下关闭移动数据进行测试，然后恢复常用设置。

在 **Apple 设备**上，检查网络是否启用了 **iCloud Private Relay**，以及 Safari 是否使用预期路径。Apple 表示，[Private Relay 会保护 Safari 浏览和 DNS 信息](https://support.apple.com/en-gb/102602)。[网络控制项](https://support.apple.com/en-ie/102022)说明过滤与 Private Relay 冲突时按网络进行的处理。不要将 Safari 的结果推广到设备上的所有应用。

**VPN**可能提供自己的 DNS 解析器，也可能通过隧道发送查询。记录 VPN 是否已连接、DNS 设置和分流隧道策略。只有在安全策略允许时，才比较 VPN 开启和关闭时的同一测试。结果变化说明路径不同，但单凭此结果不能证明存在泄漏或过滤器故障。

## 解读结果

| 证据 | 下一步可能的检查 |
|---|---|
| **过滤器日志中没有直接查询** | 过滤器地址、DNS 服务、日志记录或网络可达性 |
| **直接查询被允许** | 精确拒绝规则、组策略或规则优先级 |
| **直接查询有记录，默认查询没有记录** | DHCP、设备静态 DNS、IPv6 DNS 或 VPN 解析器 |
| **默认查询有记录，浏览器查询没有记录** | 浏览器 DoH、浏览器缓存、代理或中继 |
| **两项都记录并被阻止，但网站仍能加载** | 其他主机名、缓存内容、直接地址或应用路径 |

如果日志功能关闭、路由器代表客户端转发，或测试复用了缓存数据，**日志缺失就有多种解释**。修改防火墙规则前，请使用新主机名重试并检查查询时间。阻止发往外部解析器的普通 DNS，并不能强制加密浏览器或 VPN 使用你的过滤器。Pi-hole 的 [OPNsense 指南](https://docs.pi-hole.net/routers/opnsense/)将阻止外部 DNS 作为可选网络控制措施。设备策略和浏览器配置仍是独立控制项。

## 修复并重新测试

一次只更改一个层级。修正 DHCP 或 IPv6 DNS 通告，删除意外配置的静态解析器，在浏览器中选择预期的 DNS 提供商，或调整 VPN 的 DNS 策略。不要为了修复一次失败的测试，就在所有设备上悄然削弱加密 DNS 或中继保护。记录来源设备、接口、过滤器地址、查询名称、时间、响应、日志中的客户端、浏览器模式、VPN 状态和所做更改。

每次更改后都重新执行**直接查询**、**默认查询**和**浏览器测试**。每次运行使用新的主机名。如果设备有多个网络配置文件，请分别测试。[DNS 解析器对比](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/)有助于选择服务。[浏览器泄漏测试](/articles/privacy-browser-leak-test-dns-webrtc/)回答的是另一个问题：哪些网络信息离开浏览器和 VPN 配置。**可靠的过滤结果需要经过验证的规则和经过验证的客户端路径。**

## 下一步

每次受控更改后，重复直接、默认和浏览器测试。选择过滤服务时，请查看 [DNS 解析器对比](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/)。
