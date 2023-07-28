---
title: "安装 Mysterium：分散式 VPN 和网络抓取服务"
draft: false
toc: true
date: 2023-06-01
description: "Mysterium 是基于区块链技术构建的去中心化 VPN 和网络搜刮服务，提供安全浏览和创收机会。"
tags: ["神秘", "虚拟专用网", "网络搜刮", "分散", "隐私", "安全", "区块链", "以太坊", "多边形", "网络浏览", "创收机会", "Docker", "设置", "端口转发", "分散式虚拟专用网", "网络搜刮服务", "安全浏览", "收益", "区块链技术", "在线隐私", "Docker 容器", "节点设置", "IP 地址", "ERC20 钱包", "元掩码地址", "API 密钥", "端口转发说明", "PortForward.com", "神秘文件"]
cover: "/img/cover/An_illustration_depicting_a_shield_protecting_a_computer.png"
coverAlt: "这幅插图描绘了一个保护电脑屏幕的盾牌，象征着增强网络隐私和安全。"
coverCaption: ""
---

## 安装 Mysterium：分散式 VPN 和网络抓取服务

您在寻找分散式 VPN 和网络搜索服务吗？那就来 Mysterium 吧。Mysterium 基于以太坊（Ethereum）和多边形（Polygon）区块链构建，提供安全、私密的互联网浏览体验。每个节点每个 IP 每月平均支付 1 美元到 20 美元不等的费用，这提供了一个潜在的创收机会。值得注意的是，节点激活的设置成本为 1.XX美元，支付以 MYST 代币进行。现在就来了解 Mysterium 的好处，提高您的在线隐私保护！

{{< youtube id="KSW2k2tHTZY" >}}

### 安装 Docker 容器
要使用 Docker 容器安装 Mysterium，请按以下步骤操作：

#### 安装 Docker

学习 [how to install docker](https://simeononsecurity.ch/other/creating-profitable-low-powered-crypto-miners/#installing-docker)

#### 安装 Mysterium Docker 容器

```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```
#### 设置 Docker 容器

1.转到 `http://nodeip/#/dashboard`将 "nodeip "替换为节点的 IP 地址。在终端中输入 "ifconfig "即可找到。
2.点击 "start node setup"（开始节点设置）。
3.粘贴您要接收奖励的 ERC20 钱包地址，然后点击 "下一步"。您可以使用标准的以太坊地址，比如您的 MetaMask 地址。
4.4. 输入您将来用来访问节点仪表板的密码。选中复选框，在您的网络中申请节点。
5.点击 "在此获取 "链接并复制您的 API 密钥。将其粘贴回设置页面，然后单击 "保存并继续"。

### 端口转发

有关端口转发的说明，可参考以下资源：

- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)

## 结论

Mysterium 提供去中心化的 VPN 和网络搜刮服务，让你在维护隐私和安全的同时赚取收入。每个 IP 节点的潜在月收入从 1 美元到 20 美元不等，它为用户提供了创收机会。现在就开始使用 Mysterium 并利用其功能吧！

完成后，您应该 [Learn How to Secure Internet Sharing Applications](https://simeononsecurity.ch/other/how-to-secure-internet-sharing-applications/)

## 参考资料

- [Mysterium](https://www.mysterium.network/)
- [Mysterium Documentation - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)
