---
title: "使用低功耗硬件构建可盈利的被动收入箱：指南"
draft: false
toc: true
date: 2023-02-07
description: "了解如何使用 Raspberry Pi 或英特尔 NUC 设置低功率被动收入加密矿工，并通过本指南每月每箱赚取 10-20 美元"
tags: ["建立一个有利可图的被动收入箱", "低功耗硬件", "被动收入", "加密矿工", "树莓派", "英特尔 NUC", "指导", "硬件要求", "操作系统安装", "软件安装", "码头工人", "自动 Docker 容器更新", "Ubuntu 服务器", "Ubuntu桌面", "树莓派", "预算", "USFF", "微小的", "小型的", "微型电脑", "技术经验", "赚应用程序", "神秘岛", "Peer2Profit", "蜂蜜增益", "TraffMonitizer", "岗楼", "咬咬牙", "Linux 更新", "Ubuntu", "德比安", "中央操作系统", "RHEL", "离线更新", "本地存储库", "缓存", "服务器设置", "客户端设置", "镜像", "debmirror", "创建仓库", "apt-缓存-ng", "yumcron", "Linux 系统更新", "离线包更新", "离线软件更新", "本地包存储库", "本地包缓存", "离线 Linux 更新", "处理离线更新", "离线更新方法", "离线系统维护", "Linux 服务器更新", "Linux 客户端更新", "离线软件管理", "离线包管理", "更新策略", "Linux 安全更新"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "一块绿色的电路板，形状像一个盒子，上面有互联网连接符号，就像连接到它的电线一样。"
coverCaption: ""
---

**使用低功耗硬件构建可盈利的被动收入盒：指南**
如今，许多人都在从事加密货币挖矿和低功率矿机，例如氦气矿机。这些都很棒，但他们不再赚那么多了，他们专注于一种收入。今天，我们将构建一个低功率被动收入盒，每个盒和住宅 IP 每月可赚取 10 至 20 美元。

*如果您有能力在访客网络或更好的隔离 VLAN 上设置此设备，请执行此操作。虽然这是一个安全博客，但我们不能假设每个人的安全问题和风险承受能力。*

## 硬件要求：
以下之一是必需的。我们基本上只需要我们可以得到的任何高效低功耗的计算机。任何 Raspberry PI、Intel NUC 或类似产品都可以。他们不必那么强大。但是我建议您至少有 32g-64g 的存储空间、4g 的 ram 和至少 2 个 cpu 线程。为此，我们将硬件预算定在 100-200 美元左右，但如果满足您的需求，您可以随意提高预算。我们的功率目标是大约。平均25w。
### 树莓派：
这些天很难掌握，但它们的功率超低并且非常可定制。有关如何在 Raspberry PI 上安装 raspian 的信息
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### 英特尔 Nuc：
那里有各种各样的模型。随意选择一个较新的。
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### 任何 USFF/Tiny/Mini/Micro PC：
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### 任何配备 Intel N5100 或类似处理器的迷你电脑
对于超低功耗 Raspberry Pi 等效但在 x64 平台上。
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

##操作系统安装：
我们不会在这里讨论如何安装操作系统的技术细节。但是这里有一些很棒的资源可以帮助您入门
### 树莓派：
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu：
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## 软件安装：
这将是一个较长的部分。我们将设置 docker，然后通过 docker 设置自动 docker 容器更新并安装多个 docker 容器。我们还假设您使用的是 ubuntu 服务器，但是 ubuntu 服务器、ubuntu 桌面和 raspbian 的命令应该都是相同的。

*对于本节，我们假设您有一些基本的技术经验，并且您已经安装了操作系统并且知道如何进入终端。*

＃＃＃ 在安装更新：
我们首先要确保我们的系统完全是最新的：
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### 安装 Docker：
我们需要卸载操作系统预打包的任何现有版本，并从 Docker 的存储库中自行安装最新版本。
```bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 安装守望台：
此 docker 容器会定期自动将所有 docker 容器更新为最新图像，并清理旧（陈旧）图像。
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### 安装比特：
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping 为您提供了在 Solana 中获得报酬的能力，因为它为企业提供了一个节点，可以从您的网络运行轻量级网络测试。
这平均每个节点每天约 0.1 美分。我知道的不多，但它有潜力，而且回报很容易。

＃＃＃＃ 创建一个帐户：
创建一个帐户 [bitping.com](https://bitping.com)

#### 安装 docker 容器：
第 1 步。首先运行这些命令，因为它会引导您设置容器并要求您登录。
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

使用您的 bitping 帐户登录后，按键盘上的 CTRL+C 以退出容器。

步骤 2. 运行此命令以在后台持久化容器
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### 安装赚取应用程序：
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

Earn 应用程序可让您将互联网作为 VPN 服务共享，以获得数量惊人的奖励。每个住宅 IP 每个节点平均每月约 5 美元。通过贝宝和亚马逊礼品卡提供付款。

#### 创建一个赚取的应用程序帐户：
创建一个帐户 [earnapp.com](https://earnapp.com/i/c1dllee)
*警告，需要一个谷歌帐户*

#### 安装应用程序的非 docker 版本以获取你的 UUID：
确保在获得 UUID 后卸载，否则你最终会在同一台主机上运行它两次并且没有自动更新
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### 安装 docker 容器：
在粘贴到终端之前修改字符串。您需要指定您的 earn app UUID。
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### 视频教程：
{{< youtube id="tt499o0OjGU" >}}

### 安装蜂蜜增益：
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Honey Gain 让您可以将您的互联网作为 VPN 服务共享，以获得惊人的奖励。每个住宅 IP 每个节点平均每月约 5 美元。支出可能很复杂。在决定使用这个容器之前进一步阅读它

#### 创建蜂蜜增益帐户：
创建一个帐户 [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### 安装 Docker 容器：
在粘贴到终端之前用明显的电子邮件、密码和设备名称修改字符串
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Raspberry Pi 的替代说明
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### 视频教程：
{{< youtube id="Wd11M0nSy1k" >}}

### 安装 PawnsApp：
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
Pawns 应用程序，与此处列出的其他应用程序类似，提供向您支付共享互联网的费用。最低支出为 5 美元。每个节点每个 IP 的平均支出为每月 0.50 美元。

#### 创建一个 PawnsApp 帐户：
创建一个帐户 [https://pawns.app](https://pawns.app/?r=2092882)

#### 安装 Docker 容器：

在复制到您的终端之前，使用您的电子邮件、密码、设备名称和设备 ID 修改以下内容。
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### 安装 Peer 2 利润：
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://dashboard.peer2profit.app/register-with-referral/16538445386293aa3aaec4e?lang=en)

与 EarnApp 和 HoneyGain 类似，Peer2Profit 共享您的互联网用于 VPN 和抓取目的。每个 IP 每个节点每个月赚取大约 1 美元。
提供多种支付方式，包括汇票、BTC、LTC、LTC、MATIC 等。

#### 创建 Peer 2 利润账户：
创建一个帐户 [peer2profit.com](https://dashboard.peer2profit.app/register-with-referral/16538445386293aa3aaec4e?lang=en)

#### 安装 Docker 容器：
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
#### 视频教程：
{{< youtube id="J_rSV5N8aQk" >}}


### 安装 Repocket：
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

与此处的其他产品类似。最低 20 美元的支出。支出可能很复杂。自己研究看看是否要使用此服务。每个节点每个盒子每月的支出平均约为 1 美元。

#### 创建一个 Repocket 帐户：
创建一个帐户 [repocket.co](https://link.repocket.co/raqc) 并从您的仪表板中获取您的 api 密钥。
#### 安装 Docker 容器：
在粘贴到您的终端之前，使用您的电子邮件和 api 密钥修改以下行。
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### 视频教程：
{{< youtube id="171gWknfAbY" >}}

### 安装 Traff Monetizer：
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

与 EarnApp 和 HoneyGain 类似，TraffMonetizer 向您支付费用以共享您的互联网。每个节点每个 IP 平均每月约 2 美元。仅提供 BTC 支付。

#### 创建您的 Traff Monetizer 帐户：
创建您的帐户 [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
进入仪表板后，请记下您的应用程序令牌。

#### 安装 Docker 容器：
复制以下字符串并附加您在粘贴到终端之前从仪表板获得的令牌。

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### 安装神秘：
[Mysterium](https://www.mysterium.network/) 是建立在 Etherium 和 Polygon 区块链上的去中心化 VPN 和网络抓取服务。
平均每月支付 1-20 美元，具体取决于每个 IP 每个节点的多个因素。设置激活节点的费用为 1.XX 美元。以 MYST 代币支付。


#### 安装 Docker 容器：
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### 设置 Docker 容器：
通过将“nodeip”替换为您节点的 IP 地址，转到 http://"nodeip"/#/dashboard。您可以通过在终端中键入“ifconfig”来找到它。

单击“开始节点设置”。

将您要接收奖励的ERC20钱包地址填入，点击“下一步”。您可以使用标准的以太坊地址，例如您的 MetaMask 地址之一。

输入您以后将用于访问此节点仪表板的密码。请务必选中该复选框以声明您网络中的节点。

单击“在此处获取”链接并找到您的 API 密钥。复制它。回去贴一下。单击“保存并继续”。

＃＃＃＃ 转发端口：
我们无法描述如何为每个人的特定硬件进行端口转发。这里有一些学习如何移植的资源。
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### 在启动时自动重启 Docker 容器：
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### 可选配置：
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### 通过阻止恶意软件和跟踪器来提高安全性。
强制所有对 Cloudflares 恶意软件和跟踪保护 dns 的 DNS 请求。
此外，阻止 DNS/HTTPS 请求。
*如果你在网络上有更高级的路由器或防火墙，你甚至可以使用像 snort/securita 这样的包来创建更高级的规则来阻止已知的不良 IP、Tor 访问、种子、一般的 p2p 流量等。这是非常好的建议但不是必需的。*
```bash
# Allow ssh still
sudo ufw allow 22
# Allow dns out
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp
# Redirect all dns back to 1.1.1.2 or 1.0.0.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.0.0.2 -j DNAT --to-destination 1.1.1.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.1.1.2 -j DNAT --to-destination 1.0.0.2
# Block DNS over HTTPS
sudo ufw deny out 853/tcp
sudo ufw deny out 853/udp 
iptables -A FORWARD -m string --string "get_peers" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "announce_peer" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "find_node" --algo bm -j LOGDROP
# Block Default ToR Ports
sudo ufw deny out 9050/tcp
sudo ufw deny out 9050/udp
sudo ufw deny out 9051/tcp
sudo ufw deny out 9051/udp
# Block Torrents
sudo ufw deny out 6881/tcp
sudo ufw deny out 6881/udp
sudo ufw deny out 6882-6999/tcp
sudo ufw deny out 6882-6999/udp
iptables -A FORWARD -m string --algo bm --string "BitTorrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "BitTorrent protocol" -j DROP
iptables -A FORWARD -m string --algo bm --string "peer_id=" -j DROP
iptables -A FORWARD -m string --algo bm --string ".torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce.php?passkey=" -j DROP
iptables -A FORWARD -m string --algo bm --string "torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce" -j DROP
iptables -A FORWARD -m string --algo bm --string "info_hash" -j DROP
# Save the Changes and Enable the Firewall
sudo iptables-save
sudo ufw enable
```
对于更高级的 ToR 阻止，您可以执行以下操作：
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

＃＃ 利润？