---
title: "设置 Cloudflare 隧道：简化并保护您的网络流量"
draft: false
toc: true
date: 2023-05-26
description: "了解如何设置 Cloudflare 通道，以简化和保护网络流量，提高性能和安全性。"
tags: ["Cloudflare 隧道", "网络安全", "网站性能", "代理服务器", "网络流量", "网络配置", "Ubuntu 服务器", "Cloudflare 账户", "认证", "隧道创建", "交通路由", "DNS 记录", "安全连接", "网站托管", "代理服务", "网络保护", "性能优化", "Cloudflare 集成", "服务器配置", "流量加密", "网络流量管理", "安全虚拟主机", "网站安全", "Ubuntu 设置", "隧道技术", "Cloudflare 服务", "网络性能", "网络安全", "服务器安全", "交通管理", "Cloudflare 代理服务器"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "插图显示了一条连接本地服务器和 Cloudflare 徽标的网络隧道，象征着安全、精简的网络流量。"
coverCaption: ""
---

** Cloudflare 隧道设置指南**

## 简介
Cloudflare 隧道通过在本地网络和 Cloudflare 之间建立直接连接，提供了一种安全的网站托管方式。本指南将指导您完成 Cloudflare 隧道的设置过程，以提高网站的安全性和性能。

______

## 为什么选择 Cloudflare 隧道？
Cloudflare 隧道具有多种优势，包括减少攻击载体和简化网络配置。利用 Cloudflare 作为代理，您可以关闭外部端口，确保所有流量都通过 Cloudflare 的安全网络。这为您的网站提供了额外的保护。

______

## 前提条件
在设置 Cloudflare Tunnels 之前，请确保您具备以下条件：

1.活跃的 Cloudflare 账户。
2.运行 Ubuntu 的服务器。

______

## 第 1 步：安装
首先，您需要在 Ubuntu 服务器上安装 Cloudflare Tunnels 软件包。请按照以下步骤操作：

1.在 Ubuntu 服务器上打开终端。
2.运行以下命令下载最新版本的 Cloudflare Tunnels 软件包：

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## 第 2 步：验证
接下来，您需要使用 Cloudflare Tunnels 服务验证您的 Cloudflare 账户。请按照以下步骤操作：

1.在终端中运行以下命令：

```shell
cloudflared tunnel login
```

2.点击您想使用隧道的网站，完成验证过程。

## 第 3 步：创建隧道

现在是创建 Cloudflare 隧道的时候了。请按照以下步骤操作：

1.在终端中运行以下命令创建隧道：

```shell
cloudflared tunnel create name_of_tunnel
```

2.为隧道选择一个好记和描述性的名称。请注意，隧道名称以后不能更改。

3.创建隧道后，您将获得重要信息，包括隧道的 UUID。请记下这个 UUID，因为进一步配置时需要用到它。

4.要查看所有活动隧道的列表，请使用以下命令：

```shell
cloudflared tunnel list
```

这将显示隧道的名称和 UUID。

#### 第 4 步：配置隧道

要配置隧道并开始路由流量，请按照以下步骤操作：

1.导航至服务器上的 Cloudflare 隧道目录。默认位置是 `/etc/cloudflared`

2.在该目录下新建一个名为 `config.yml`使用您选择的文本编辑器。

3.用以下内容填充 config.yml 文件：

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

确保更换 `<your_tunnels_uuid>`并在必要时更新凭证文件的路径。

## 第 5 步：路由流量

要指定要通过隧道提供的内部服务，请按照以下步骤操作：

1. `Open the `再次存档。

2.在文件中添加入口参数，以定义要通过 Cloudflare 路由的服务。例如

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

更换 `<your_tunnels_uuid>`使用隧道的 UUID，并根据配置更新主机名和服务详细信息。

3.保存 config.yml 文件。


## 第 6 步：创建 DNS 记录

要为隧道主机名和服务创建 DNS 记录，请按照以下步骤操作：

1.打开终端。

2.使用以下命令创建 DNS 记录：

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
更换 `<UUID or NAME of tunnel>`隧道的 UUID 或名称，以及 `<hostname>`为您的服务输入所需的主机名。

3.例如，要为 example.com 创建 DNS 记录，请运行以下命令：

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

请注意，更改将反映在 Cloudflare 仪表板的 DNS 部分。

## 第 7 步：启动隧道

要测试并启动 Cloudflare 隧道，请按照以下步骤操作：

1.打开终端。

2.运行以下命令启动隧道：

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

更换 `<UUID or NAME of tunnel>`的 UUID 或隧道名称。

3.Cloudflared 现在将设置您的隧道并显示其状态信息。一旦隧道成功启动并运行，您就可以进入下一步。

4.为防止退出终端时关闭隧道，您需要将 Cloudflared 作为 systemd 服务运行。使用以下命令：

```shell
cloudflared --config /path/to/config.yml service install
```

更换 `/path/to/config.yml`的路径。 `config.yml`锉刀

## 结论

在本指南中，我们介绍了在 Ubuntu 上设置 Cloudflare 通道的步骤。按照这些说明，您可以利用 Cloudflare 的网络来提高网站的安全性和性能。请记住定期监控隧道并根据需要调整配置。

如果遇到任何问题或需要进一步帮助，请参阅 [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## 参考资料
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)