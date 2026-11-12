---
title: "IPv4 到 IPv6 的过渡机制：完整指南"
date: 2023-02-18
lastmod: 2026-11-12
toc: true
draft: false
description: "本指南介绍从 IPv4 迁移到 IPv6 时使用的不同机制。"
tags: ["IPv4", "IPv6", "网络", "过渡机制", "双栈", "NAT64", "DNS64", "IPv6 隧道", "ISATAP", "6to4", "DS-Lite", "MAP-T", "IPv6 迁移", "网络协议", "互联网协议", "网络架构", "路由", "子网划分", "寻址"]
cover: "/img/cover/A_cartoon_image_of_a_person_standing_at_a_crossroads.webp"
coverAlt: "卡通插图中，一人站在路口，路标分别指向 IPv4 和 IPv6，象征在两种协议之间作出选择并进行迁移。"
coverCaption: ""
---
**IPv4 到 IPv6 的过渡机制**

随着联网设备数量和互联网流量持续增长，全球可用的 IPv4 地址逐渐不足。IPv6 为解决这一问题而推出，许多网络已经采用它，但迁移工作仍在进行。本文介绍从 IPv4 迁移到 IPv6 时可使用的不同机制。

## 简介

**IPv4** 是最初的 IP 地址格式，从互联网早期开始使用。它使用 32 位地址，最多支持 43 亿个唯一地址。联网设备不断增加后，这一数量已显不足。相比之下，**IPv6** 使用 128 位地址，可支持近乎无限数量的唯一地址。要让互联网继续发展，就需要迁移到 IPv6。

## 过渡机制

### 双栈

最直接的过渡方式是在同一网络上同时运行 IPv4 和 IPv6，这称为**双栈（Dual Stack）**。双栈网络会在网络设备上启用两种协议，设备可使用其中任一种进行通信。这种方式支持逐步迁移到 IPv6，同时维持 IPv4 连接。

### 隧道

**隧道**是将 IPv6 数据包封装在 IPv4 数据包中，以便通过 IPv4 网络传输的方法。它用于连接被 IPv4 网络隔开的 IPv6 网络区域。IPv6 数据包封装在 IPv4 数据包中后，由 IPv4 网络转发到隧道另一端。在那里，IPv6 数据包会被解封装并送达目的地。

### 转换

**转换**机制用于协助 IPv4 和 IPv6 网络之间通信。两种转换方式是 Network Address Translation-Protocol Translation (NAT-PT) 和 Address Family Transition Router (AFTR)。**NAT-PT** 可将 IPv6 数据包转换为 IPv4 数据包，反向转换也可以。**AFTR** 则为仅使用 IPv4 的主机提供 IPv6 连接。

### 6rd

**IPv6 Rapid Deployment (6rd)** 可在 IPv4 网络中快速部署 IPv6。使用 6rd 时，IPv6 前缀会封装在 IPv4 数据包中，并通过 IPv4 网络传输。数据包到达另一端后，IPv6 数据包会被解封装并送达目的地。希望快速、高效部署 IPv6 的服务提供商可采用这种机制。

### DS-Lite

**Dual-Stack Lite (DS-Lite)** 用于向仅使用 IPv4 的网络提供 IPv6 连接。DS-Lite 会把 IPv6 数据包封装在 IPv4 数据包中，再通过 IPv4 网络发送。到达另一端后，IPv6 数据包会被解封装并送达目的地。这样可逐步迁移到 IPv6，同时不中断 IPv4 连接。

### NAT64

**NAT64** 用于向仅使用 IPv4 的主机提供 IPv6 连接。它会把 IPv6 数据包转换成 IPv4 数据包，再通过 IPv4 网络传输。到达另一端后，IPv4 数据包会再次转换为 IPv6 数据包并送达目的地。对于无法升级以支持 IPv6 的主机，这种机制有助于提供连接。

______

迁移到 IPv6 对互联网持续发展至关重要。迁移仍在进行，目前有多种过渡机制可用
