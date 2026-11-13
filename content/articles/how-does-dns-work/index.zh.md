---
title: "DNS 如何工作：根 DNS 的作用与故障排查"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "了解 DNS 与根 DNS 的层级结构、名称解析流程、缓存机制和故障排查方法。"
genre: ["DNS 基础", "根 DNS", "域名系统", "DNS 解析", "DNS 层级", "DNS 缓存", "DNS 故障排查", "DNS 记录", "DNS 管理", "DNS 命令"]
tags: ["DNS", "根 DNS", "域名系统", "DNS 解析", "DNS 层级", "DNS 缓存", "DNS 记录", "DNS 管理", "DNS 故障排查", "网络", "互联网基础设施", "IP 地址", "访问网站", "递归查询", "权威名称服务器", "TTL", "缓存机制", "清除 DNS 缓存", "根 DNS 服务器", "任播路由", "ICANN", "DNS 协作", "A 记录", "AAAA 记录", "CNAME 记录", "MX 记录", "TXT 记录", "SRV 记录", "NS 记录", "PTR 记录", "SOA 记录", "DNS 诊断命令", "Windows", "macOS", "Linux", "命令提示符", "终端"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "互联的计算机网络图，其中显示域名和 IP 地址，体现 DNS 与根 DNS 的工作方式。"
coverCaption: "了解 DNS，掌握域名系统"
---

## DNS 与根 DNS 的工作方式

### 引言

域名系统（DNS）是互联网基础设施的重要组成部分。它让用户使用域名而非 IP 地址访问网站。DNS 类似电话簿，会把人类可读的域名转换成计算机能够理解的 IP 地址。根 DNS 是参与域名解析的分层分布式系统的核心。本文介绍 DNS、根 DNS 的工作方式，以及域名可能包含的记录。

{{< youtube id="mpQZVYPuDGU" >}}

## 域名系统（DNS）

**域名系统（DNS）** 是一种去中心化命名系统，用于将域名与 IP 地址关联起来。用户只需在浏览器中输入域名，就能访问网站和其他互联网资源。DNS 免去了记忆复杂 IP 地址的需要。

### DNS 层级

DNS 采用多层级结构。最顶层是根区，其下依次是顶级域（TLD）、二级域和子域。每一级共同组成完整域名。在 `www.example.com` 中，“www”是子域，“example”是二级域，“com”是 TLD。

### DNS 解析流程

用户在浏览器中输入域名后，DNS 解析随即开始。浏览器向 DNS 解析器发送查询，解析器通常由互联网服务提供商（ISP）提供。解析器按照一系列步骤解析域名并获取对应的 IP 地址。

1. **本地 DNS 缓存**：解析器先检查本地缓存中是否有请求的域名和 IP 地址。如果找到信息，就直接返回结果。

2. **递归查询**：如果缓存中没有信息，解析器会发起递归查询。它首先联系负责“.”（点）区域的根 DNS 服务器。根服务器会返回请求域名所属 TLD 服务器的 IP 地址。

3. **TLD 查询**：解析器联系上一步找到的 TLD 服务器，并请求负责该域名的权威名称服务器的 IP 地址。

4. **查询权威名称服务器**：解析器向 TLD 服务器提供的权威名称服务器发送查询。这些服务器保存域名的权威记录，并返回与该域名关联的 IP 地址。

5. **向客户端响应**：解析器从权威名称服务器收到 IP 地址后，将其返回给浏览器。浏览器随后使用该地址连接 Web 服务器。

### DNS 缓存

DNS 解析器通过缓存提高性能并减少 DNS 服务器的负载。收到 DNS 查询响应后，解析器会在本地保存域名与 IP 地址之间的映射。同一域名的后续查询可以直接从缓存获取结果，无需再次查询 DNS 层级。

缓存会出现在多个层级，包括本地解析器、ISP 解析器，以及路由器和操作系统等设备。DNS 响应中的 Time-to-Live（TTL）值决定记录在缓存中的保存时间。TTL 到期后，解析器会丢弃记录并重新查询。

#### 清除本地 DNS 缓存

清除 DNS 缓存有助于解决某些 DNS 问题，并让系统获取最新记录。以下是不同操作系统的操作步骤：

##### Windows

在 Windows 中清除 DNS 缓存：

1. 按 `Win + R`，输入 `cmd`，再按 Enter 打开命令提示符。

2. 输入以下命令并按 Enter：

```bash
ipconfig /flushdns
```

此命令会清除 Windows 系统上的 DNS 解析器缓存。

##### macOS

在 macOS 中清除 DNS 缓存：

1. 从“应用程序”>“实用工具”打开终端，或使用 Spotlight 搜索终端。

2. 在终端中输入以下命令并按 Enter：

```bash
sudo killall -HUP mDNSResponder
```

此命令会重启 mDNSResponder 进程，该进程负责 macOS 上的 DNS 解析。

##### Linux

Linux 中清除 DNS 缓存的步骤因发行版和解析器而异。以下是两种常见方法：

1. **基于 systemd 的系统（例如 Ubuntu、Fedora）**：

打开终端，并以管理员权限运行以下命令：

```bash
sudo systemd-resolve --flush-caches

```

此命令会清除使用 systemd-resolved 作为解析器的系统上的 DNS 缓存。

2. **不使用 systemd 的系统**：

打开终端，并以管理员权限运行以下命令：

```bash
sudo /etc/init.d/nscd restart

```

此命令会重启 Name Service Cache Daemon（nscd），它负责在不使用 systemd 的 Linux 发行版中缓存 DNS。

以上是通用步骤。命令和方法可能因操作系统版本略有不同。清除 DNS 缓存有助于解决部分 DNS 问题，但无法解决所有网络连接问题。

## 根 DNS 系统的工作方式

根 DNS 系统是 DNS 基础设施的重要组成部分。以下是它的工作方式：

### 1. 根区和根服务器

根 DNS 系统从 **根区** 开始，它是 DNS 层级的最高层。根区包含所有顶级域（TLD）的权威名称服务器信息，例如 .com、.org、.net，以及 .us、.uk 等国家/地区代码 TLD。

根 DNS 系统由 13 个根 DNS 服务器组成，以 A 到 M 的字母标识。它们分布在世界各地，以提供冗余和可靠性。

### 2. 任播路由

为了处理大量 DNS 流量，根服务器使用 **任播路由**。多个服务器可以共享同一个 IP 地址，但分布在不同地理位置。网络会根据当前状况将查询路由到合适的服务器，从而有效分配负载。

用户发起 DNS 查询时，任播会将请求路由到附近可用的根服务器。网络基础设施会根据网络状况选择最短路径。任播有助于分配负载并避免瓶颈。

### 3. 递归 DNS 解析器

DNS 解析器收到域名查询后，会开始递归解析流程，并联系其中一个根 DNS 服务器。

根服务器会返回负责请求 TLD 的 TLD 名称服务器 IP 地址的指引。这些 TLD 服务器保存该 TLD 内各域名权威名称服务器的信息。

### 4. 指引和权威名称服务器

收到根服务器的指引后，解析器会联系对应的 TLD 名称服务器。

TLD 名称服务器会返回另一条指引，其中包含请求域名的权威名称服务器 IP 地址。

随后，解析器会向权威名称服务器请求与该域名关联的 IP 地址。

### 5. 缓存和 TTL

DNS 解析过程中的缓存可以提高性能并减少 DNS 服务器负载。DNS 解析器会保存域名与 IP 地址之间的映射。

DNS 记录会按照 Time-to-Live（TTL）值指定的时长进行缓存。TTL 表示记录的有效时间。TTL 到期后，解析器会丢弃缓存记录并重新查询以获取更新后的 IP 地址。

### 6. 协作与管理

根 DNS 系统由 Internet Corporation for Assigned Names and Numbers（ICANN）和 根服务器运营方 协作管理。

ICANN 负责 DNS 的整体管理与协调，并与根服务器运营方合作。他们共同维护根区文件，其中包含 13 个根 DNS 服务器及其 IP 地址的信息。

根服务器运营方 确保根 DNS 服务器正常运行并保持可用，从而支持整个 DNS 基础设施的稳定性和弹性。

根 DNS 系统是 DNS 解析的起点。它帮助将域名映射到 IP 地址，使用户能够高效访问网站和其他互联网资源。

#### 13 个根 DNS 服务器

13 个根 DNS 服务器以 A 到 M 的字母标识。每个服务器在多个物理位置托管，以提供冗余和容错能力。它们负责处理根区查询，包括 .com、.org、.net 等 TLD，以及 .us、.uk 等国家/地区代码 TLD。

#### ICANN 与根 DNS 管理

Internet Corporation for Assigned Names and Numbers（**ICANN**）负责管理和协调 DNS，并分配 IP 地址。ICANN 与 根服务器运营方 合作，确保根 DNS 的稳定性和安全性。双方共同维护根区文件，其中包含 13 个根服务器及其 IP 地址的信息。

______

## DNS 记录类型及用途

{{< youtube id="HnUDtycXSNE" >}}

DNS 记录是域名系统（DNS）的重要组成部分，用于提供与域名相关的各类信息。以下是一些常见记录类型及其用途：

| 记录类型 | 说明 | 示例 |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | 将域名映射到 IPv4 地址。 | `example.com     IN A 192.0.2.1` |
| AAAA | 将域名映射到 IPv6 地址。 | `example.com     IN AAAA 2001:db8::1` |
| CNAME | 将别名（规范名称）映射到实际域名。 | `www.example.com IN CNAME example.com` |
| MX | 指定负责接收该域名邮件的邮件服务器。 | `example.com     IN MX 10 mail.example.com` |
| TXT | 存储任意文本，常用于 SPF、DKIM 或域名验证。 | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | 指定域名的权威名称服务器。 | `example.com     IN NS ns1.example.com` |
| SOA | 指定区域的全局属性（起始授权记录）。 | `example.com     IN SOA ns1.example.com` |
| SRV | 定义域名所提供特定服务的位置。 | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | 将 IP 地址映射到域名（反向 DNS 查询）。 | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. A 记录（地址记录）

**A 记录**将域名映射到 IPv4 地址。它是最基本且最常用的 DNS 记录类型。用户在浏览器输入域名时，A 记录帮助浏览器找到托管网站的 Web 服务器 IP 地址。

### 2. AAAA 记录（IPv6 地址记录）

**AAAA 记录**与 A 记录用途相同，但用于将域名映射到 IPv6 地址。随着向 IPv6 过渡，AAAA 记录对于 IPv6 网络连接越来越重要。

### 3. CNAME 记录（规范名称记录）

**CNAME 记录**为域名创建别名或规范名称。当你希望某个域名或子域指向另一个域名或子域时，可以使用它。例如，可以创建 CNAME 记录，让 "www" 指向 "mywebsite.com"。

### 4. MX 记录（邮件交换记录）

**MX 记录**指定负责接收域名邮件的邮件服务器。可以配置多个 MX 记录并设置优先级，以便主服务器不可用时按顺序尝试其他服务器。

### 5. TXT 记录（文本记录）

**TXT 记录**用于存储与域名关联的文本信息。常见用途包括域名验证、用于电子邮件身份验证的 Sender Policy Framework（SPF）记录，以及一般信息或备注。

### 6. SRV 记录（服务记录）

**SRV 记录**定义域名中某项服务或资源的位置。它常用于 VoIP、即时消息等需要查找特定服务器或服务的应用。

### 7. NS 记录（名称服务器记录）

**NS 记录**指定域名的权威名称服务器。这些服务器保存域名的 DNS 记录。DNS 解析器会查询 NS 记录以找到域名对应的权威名称服务器。

### 8. PTR 记录（指针记录）

**PTR 记录**用于反向 DNS 查询，将 IP 地址映射到域名。它常用于验证邮件服务器身份并帮助防范垃圾邮件。反向 DNS 查询有助于验证邮件服务器的真实性。

### 9. SOA 记录（授权起始记录）

**SOA 记录**包含域名的管理信息，包括主权威名称服务器、域名管理员的联系邮箱，以及 DNS 记录的多个时间参数。

以上只是众多 DNS 记录类型中的几个示例。每种记录都有特定用途，帮助 DNS 高效、准确地将域名解析到相关资源。

______

## 不同操作系统的 DNS 故障排查命令

遇到 DNS 问题时，诊断命令有助于查明原因。以下是不同操作系统中常用的 DNS 排查命令：

### Windows

#### 1. `ipconfig /flushdns`

此命令会清除 Windows 中的 DNS 缓存，有助于解决过期或错误 DNS 记录导致的问题。打开命令提示符并运行该命令。

#### 2. `ipconfig /all`

运行 `ipconfig /all` 会显示 Windows 网络接口的详细信息，包括已配置的 DNS 服务器。可用它确认系统是否使用了正确的 DNS 服务器。

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

此命令会重启 macOS 上负责 DNS 解析的 mDNSResponder 进程。它有助于刷新 DNS 设置并解决相关问题。打开终端并使用管理员权限运行命令。

#### 2. `nslookup`

`nslookup` 可用于查询 DNS 记录、测试 DNS 解析，以及检查与 DNS 服务器的连接。打开终端，运行 `nslookup`，后接要检查的域名或 IP 地址。

### Linux

#### 1. `systemd-resolve --flush-caches`

在使用 systemd 作为 DNS 解析器的 Linux 系统上，`systemd-resolve --flush-caches` 会清除 DNS 缓存。它有助于解决过期缓存条目导致的问题。打开终端并使用管理员权限运行该命令。

#### 2. `dig`

`dig` 是 Linux 上功能丰富的 DNS 诊断工具，可显示 DNS 查询、响应和服务器配置的详细信息。你可以使用 `dig` 查询特定记录、测试 DNS 解析并排查相关问题。打开终端，运行 `dig`，后接要调查的域名或 IP 地址。

这些命令有助于在不同操作系统上诊断和解决 DNS 问题。它们能帮助检查 DNS 配置、服务器设置和连接问题。

命令及其选项可能因操作系统版本和发行版而异。请查阅对应版本的文档，了解详细用法。
______


## 总结

域名系统（DNS）和根 DNS 在互联网运行中发挥着重要作用。DNS 让用户通过易读的域名访问网站，根 DNS 则构成整个 DNS 层级的基础。了解它们的工作方式有助于使用网络，并理解支撑在线服务的基础设施。

______

## 参考资料

- [维基百科：DNS](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Cloudflare：DNS 的工作方式](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [ICANN 官方网站](https://www.icann.org/)
- [根服务器运营方](https://www.root-servers.org/)
