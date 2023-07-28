---
title: "确保互联网共享应用程序的安全：加强保护的有效措施"
draft: false
toc: true
date: 2023-06-01
description: "了解如何使用先进的措施来阻止恶意软件、跟踪器、Tor 流量和 Torrent，从而确保 Linux 互联网共享应用程序的安全。"
tags: ["Linux 安全", "互联网共享应用程序", "恶意软件保护", "跟踪器屏蔽", "阻止 Tor 流量", "防止激流", "网络安全", "嗤之以鼻", "Securita", "DNS 保护", "高级防火墙规则", "乌班图更新", "自动更新", "网络监控", "网络安全", "Linux 互联网安全", "Linux 应用程序安全", "恶意软件拦截", "防止 Tor 流量", "洪流保护", "网络防火墙", "Linux 网络安全", "安全网络共享", "Linux DNS 保护", "高级网络安全", "Linux 系统更新", "网络监控工具", "Linux 网络安全措施", "Linux 安全实践"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "一幅卡通插图，展示了保护互联设备网络免受恶意威胁的防护罩。"
coverCaption: ""
---

**如何确保 Linux 上互联网共享应用程序的安全**

Linux 互联网共享应用程序的安全对于保护网络和敏感数据至关重要。在本文中，我们将探讨有效的策略，以增强这些应用程序的安全性，防止恶意软件、跟踪器、Tor 流量和洪流。

###通过阻止恶意软件和跟踪器提高安全性

确保互联网共享应用程序安全的一个关键步骤是**强制所有 DNS 请求到 Cloudflare 的恶意软件和跟踪保护 DNS**。这样做可以确保阻止任何访问恶意或跟踪网站的尝试，从而提供额外的安全保护。

为进一步加强网络安全，建议**屏蔽 DNS/HTTPS 请求**。通过限制这些请求，您可以强制使用未加密的 DNS，从而控制部分出站目标流量，防止潜在的安全漏洞和未经授权的访问尝试。

*如果你的网络上有更先进的路由器或防火墙，你可以利用功能强大的工具，如 [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/)来创建附加规则。通过这些工具，您可以阻止已知的不良 IP、限制 Tor 访问、限制 P2P 流量并应用高级网络安全监控。实施这些高级规则可以大大增强网络的安全态势。

```bash
# Allow SSH
sudo ufw allow 22

# Allow DNS out
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp

# Redirect all DNS back to 1.1.1.2 or 1.0.0.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.0.0.2 -j DNAT --to-destination 1.1.1.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.1.1.2 -j DNAT --to-destination 1.0.0.2

# Block DNS over HTTPS
sudo ufw deny out 853/tcp
sudo ufw deny out 853/udp 

# Block malware and trackers
iptables -A FORWARD -m string --string "get_peers" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "announce_peer" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "find_node" --algo bm -j LOGDROP

# Block default Tor ports
sudo ufw deny out 9050/tcp
sudo ufw deny out 9050/udp
sudo ufw deny out 9051/tcp
sudo ufw deny out 9051/udp

# Block torrents
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

# Save the changes and enable the firewall
sudo iptables-save
sudo ufw enable
```

#### 高级 ToR 屏蔽
对于更高级的 ToR 屏蔽，您可以执行以下操作：
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### 可选配置：
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## 结论

通过实施这些安全措施，你可以增强 Linux 上互联网共享应用程序的安全性，有效阻止恶意软件、跟踪器、Tor 流量和洪流。

请记住，保持系统和应用程序的最新状态，并在可用的情况下应用额外的高级规则来进一步保护你的网络是非常重要的。

## 参考资料

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
