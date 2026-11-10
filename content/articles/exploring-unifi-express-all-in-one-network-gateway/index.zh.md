---
title: "Ubiquiti UniFi Express：紧凑型网关与 WiFi 6 接入点评测"
date: 2024-01-03
lastmod: 2026-11-08
toc: true
draft: false
description: "评测 UniFi Express 这款集成 WiFi 6 接入点、管理方式简便的紧凑型网关。"
genre: ["科技评测", "网络解决方案", "家庭网络设置", "WiFi 6 设备", "UniFi Express 解析", "紧凑型网关", "无线接入点", "Ubiquiti 产品", "网络安全", "小型企业网络"]
tags: ["UniFi Express", "WiFi 6", "网络网关", "Ubiquiti", "无线接入点", "科技评测", "网络安全", "家庭网络", "紧凑型网关", "小型企业", "一体化设备", "Mesh 网络", "设备设置", "互联网连接", "Ubiquiti 解决方案", "双核 CPU", "WiFi 覆盖", "IDS/IPS", "VPN 选项", "应用感知防火墙", "UniFi OS", "无线 Mesh", "网络扩展", "VLAN 支持", "技术信息", "设备限制", "Ubiquiti Networks", "路由性能", "简化网络管理"]
cover: "/img/cover/UniFi_Express_Connectivity.webp"
coverAlt: "UniFi Express 的象征性插图，展示其紧凑设计和流畅连接，并突出效率与创新"
coverCaption: "简化。连接。创新。UniFi Express，让网络管理更轻松。"
ref: ["/articles/the-ideal-ubiquiti-unifi-networking-setup-both-simple-and-advanced", "/articles/ubiquiti-unifi-good-for-home-use", "/articles/ubiquiti-unifi-vs-tp-link-omada"]
---
**Ubiquiti UniFi Express：适用于家庭和小型企业网络的紧凑型高性能网关**

在快速发展的网络解决方案领域，Ubiquiti 的 UniFi Express 凭借紧凑、高性能的网关和 WiFi 6 接入点脱颖而出。本评测介绍其规格、功能及与其他设备的区别，并分析它是否适合家庭和小型企业网络。

## UniFi Express 简介

UniFi Express 将新一代防火墙、应用感知功能和内置 WiFi 6 接入点集成在简洁紧凑的机身中，简化了网络管理。本评测将分析它的功能和限制，并与其他 UniFi 网关进行比较。

{{< youtube id="VbIamWqXjAk" >}}

______

## 技术性能：UniFi Express 规格

{{< figure src="sos-unifi-express.webp" alt="Ubiquiti UniFi Express" caption="Ubiquiti UniFi Express" link="https://amzn.to/418yMvj" >}}

UniFi Express 配备 1 GHz 双核 ARM Cortex-A53 CPU 和 1 GB DDR3L 内存。0.9 英寸显示屏可显示实时信息。其最高吞吐量为 1 Gbps，但也有一些限制：缺少 Suspicious Activity 功能，且最多仅支持 5 台 UniFi 设备。

- **CPU：** 1 GHz 双核 ARM Cortex-A53
- **内存：** 1 GB DDR3L
- **板载闪存：** 10 GB
- **显示屏：** 0.9 英寸
- **最大 SQM 吞吐量：** 1 Gbps
- **WAN 端口：** 1x Gigabit RJ45
- **LAN 端口：** 1x Gigabit RJ45
- **供电方式：** USB-C (5 V / 3 A)
- **最大功耗：** 10 W
- **尺寸：** 98 x 98 x 30 mm

这些技术参数为评估 UniFi Express 在不同网络环境中的性能提供了依据。

______

## WiFi 6 功能：内置接入点

UniFi Express 的一项突出功能是内置 WiFi 6 接入点。它不支持 6 GHz 频段（WiFi 6E），但在 2.4 GHz 和 5 GHz 频段都能提供较高吞吐量。其覆盖范围约为 140 m²（1,500 ft²），可在此范围内提供可靠连接。

- **2.4 GHz 发射功率：** 22 dBm
- **5 GHz 发射功率：** 25 dBm
- **MIMO：** 2 x 2 (DL/UL MU-MIMO)
- **2.4 GHz 吞吐量：** 573.5 Mbps
- **5 GHz 吞吐量：** 2.4 Gbps
- **同时连接的客户端：** 60 台以上

UniFi Express 还可用作 Mesh 接入点，方便扩展网络。

______

## UniFi Express 与其他网关对比

{{< figure src="sos-unifi-express-vs-unifi-gateway-lite.webp" alt="Ubiquiti UniFi Express 与 Ubiquiti UniFi Gateway Lite 对比" caption="Ubiquiti UniFi Express 与 Ubiquiti UniFi Gateway Lite 对比" link="https://amzn.to/3uPFKta" >}}

比较 Ubiquiti 的 UniFi Express、UniFi Gateway Lite、UniFi Dream Router (UDR) 和 UniFi Dream Machine Pro (UDM Pro/SE)，有助于根据不同网络需求选择合适的网关。

### UniFi Express

[**UniFi Express**](https://amzn.to/418yMvj) 是一款紧凑、高性能的一体化网关，并内置 WiFi 6 接入点。它运行 UniFi Network 应用，路由性能为 1 Gbps，售价 149 美元。它不提供 IDS 和 IPS 威胁检测功能。

### UniFi Gateway Lite

[**UniFi Gateway Lite**](https://amzn.to/3uPFKta) 是 UniFi Security Gateway 的后续产品，管理时需要额外的控制台。它售价 129 美元，路由性能与 UniFi Express 一样为 1 Gbps，但没有内置接入点。它提供 IDS 和 IPS 威胁检测，支持更高级的防护。

### UniFi Dream Router (UDR)

[**UniFi Dream Router (UDR)**](https://amzn.to/41rpBq9) 面向家庭用户，将多项功能集成在一台设备中。它配备 1 GHz 双核 ARM Cortex-A53 处理器、2 GB 内存，路由性能为 1 Gbps。UDR 运行 UniFi Network 和 UniFi Protect，并支持 IDS 和 IPS 威胁检测。售价 199 美元，还包含内置接入点，适合构建功能完善的家庭网络。

### UniFi Dream Machine Pro (UDM Pro/SE)

[**UniFi Dream Machine Pro (UDM Pro/SE)**](https://amzn.to/3uP1tS1) 是面向企业的解决方案。该网关配备 1.7 GHz 双核 Arm Cortex-A57 处理器、4 GB RAM，路由性能为 10 Gbps。它支持 UniFi Network、UniFi Protect、IDS 和 IPS 威胁检测，以及多个 PoE 端口，适合规模较大的网络。售价为 379 至 499 美元，可满足复杂部署的多种需求。

### 选择合适的网关

选择这些网关时，请先考虑网络的具体需求。如果简单管理、紧凑设计和基础威胁防护已经足够，UniFi Express 是不错的选择。若优先考虑高级威胁检测，UniFi Gateway Lite 更合适。UniFi Dream Router 面向家庭用户，UniFi Dream Machine Pro/SE 面向企业用户，两者都为更大规模的网络提供相应功能。

______

## 设置 UniFi Express：轻松上手

设置过程体现了 UniFi Express 即插即用的特点。通过 WAN 端口将设备连接到互联网，然后在手机上打开 UniFi Network 应用即可开始简化设置。需要使用 Ubiquiti 账户将设备关联到易用的软件界面。

### 初始设置

1. 将 UniFi Express 连接到互联网。
2. 在手机上打开 UniFi Network 应用。
3. 按照屏幕提示为 UniFi Express 命名，并配置无线网络。
4. 收到提示后，连接到新的无线网络。

设置过程简单，适合希望操作方便且不想牺牲功能的用户。

#### 配置 UniFi Network

最好通过浏览器版 UniFi Network 应用调整网络配置。使用网关的 IP 地址登录，或访问 [https://unifi.ui.com](https://unifi.ui.com) 打开设置。下方视频展示了 Ubiquiti UniFi 设备的完整设置过程。

{{< youtube id="bWJNZvXXgf8" >}}

______

## 将 UniFi Express 用作 Mesh 接入点：扩展用途

除了作为独立网关，UniFi Express 还可作为现有网络中的 Mesh 接入点。它支持有线或无线回程连接，能够轻松集成到网络中，提供灵活的部署方式。

- **支持的设备数量：** 另外 4 台 UniFi Network 设备
- **两个端口均可用作 LAN：** 是，Mesh 模式下
- **Mesh 兼容性：** 所有第二代或更新的 UniFi 接入点
- **VLAN 支持：** LAN/WAN 端口不支持
- **作为 CloudKey 网关：** 否，需要 UniFi Gateway Lite

这种灵活性让 UniFi Express 能够作为接入点工作，并在需求变化时扩展网络。

______

## 常见问题

{{< youtube id="0A7a9_6ZgCU" >}}

1. **UniFi Express (UX) 支持多少台设备？**
   - UniFi Express 可管理另外 4 台 UniFi Network 设备。

2. **在 Mesh 模式下，两个端口都能用作 LAN 端口吗？**
   - 可以。UniFi Express 连接到 Mesh 网络后，两个端口都可用作 LAN 端口。

3. **UX 能与普通 UniFi 接入点组建 Mesh 网络吗？**
   - 可以。UX 能与所有第二代或更新的 UniFi 接入点组建 Mesh 网络。

4. **LAN/WAN 端口支持 VLAN 吗？**
   - 不能为 LAN 或 WAN 端口分配 VLAN。

5. **UniFi Express 能作为 CloudKey 的网关吗？**
   - 不能。如果网络中有 CloudKey，UX 只能用作接入点，此时需要 UniFi Gateway Lite。

______

## 总结

UniFi Express 是一款有吸引力的入门级 Cloud Gateway，尤其适合简单的家庭网络和小型办公室。它支持的设备数量有限，也缺少 IDS/IPS，但紧凑设计和内置接入点使其成为许多用户实用的一体化方案。网络需求变化后，仍可继续将 UniFi Express 用作接入点。

______

## 参考资料

1. [Ubiquiti UniFi Express 产品页面](https://store.ui.com/us/en/pro/category/all-unifi-cloud-gateways/products/ux)
2. [Ubiquiti UniFi Gateway Lite 产品页面](https://store.ui.com/us/en/products/uxg-lite)
3. [Ubiquiti 文档](https://help.ui.com/hc/en-us)
4. [UniFi Network 应用](https://apps.apple.com/us/app/unifi/id1057750338) (iOS)
5. [UniFi Network 应用](https://play.google.com/store/apps/details?id=com.ubnt.easyunifi&hl=en_US&gl=US) (Android)
6. [UniFi OS 更新](https://community.ui.com/releases)
7. [LazyAdmin 的 UniFi Express 评测](https://lazyadmin.nl/home-network/unifi-express-review/#:~:text=The%20UniFi%20Express%20is%20really,takes%20a%20couple%20of%20minutes.)