---
title: "インターネット共有アプリケーションを安全に保護強化のための効果的な対策"
draft: false
toc: true
date: 2023-06-01
description: "マルウェア、トラッカー、Tor トラフィック、トレントをブロックする高度な対策で、Linux のインターネット共有アプリを保護する方法をご紹介します。"
tags: ["Linuxのセキュリティ", "インターネット共有アプリ", "マルウェアプロテクション", "トラッカーブロッキング", "Torトラフィックブロッキング", "迸り防止", "ネットワークセキュリティ", "スノート", "セキュリタ", "DNSの保護", "アドバンスドファイアウォールルール", "Ubuntuのアップデート", "自動更新", "ネットワークモニタリング", "サイバーセキュリティ", "Linuxのインターネットセキュリティ", "Linuxアプリのセキュリティ", "マルウェアブロッキング", "Torトラフィック防止", "トレントプロテクション", "ネットワークファイアウォール", "Linuxのネットワークセキュリティ", "セキュアなインターネット共有", "LinuxのDNS対策", "高度なネットワークセキュリティ", "Linuxシステムのアップデート", "ネットワークモニタリングツール", "Linuxのサイバーセキュリティ対策", "Linuxのセキュリティ対策"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "相互に接続された機器のネットワークを悪意のある脅威から守るシールドを示す漫画のイラストです。"
coverCaption: ""
---

**Linuxでインターネット共有アプリのセキュリティを確保する方法**」。

Linux上のインターネット共有アプリのセキュリティは、ネットワークと機密データを保護するために最も重要です。この記事では、これらのアプリのセキュリティを強化し、マルウェア、トラッカー、Torトラフィック、およびトレントから保護するための効果的な戦略を探ります。

### マルウェアとトラッカーをブロックしてセキュリティを強化する

インターネット共有アプリのセキュリティを確保するための重要なステップの1つは、**すべてのDNSリクエストをCloudflareのマルウェアおよびトラッキング保護DNS**に強制することです。そうすることで、悪意のあるウェブサイトやトラッキングウェブサイトにアクセスしようとする試みを確実にブロックし、セキュリティの追加レイヤーを提供することができます。

ネットワークのセキュリティをさらに強化するために、**DNS/HTTPSリクエスト**をブロックすることをお勧めします。これらのリクエストを制限することで、暗号化されていないDNSを強制的に使用し、送信先トラフィックの一部を制御することができるため、潜在的なセキュリティ脆弱性や不正なアクセスの試みを防ぐことができます。

*ネットワーク上でより高度なルーターやファイアウォールを利用できる場合は、以下のような強力なツールを活用することができます。 [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/)を使用して、追加のルールを作成することができます。これらのツールにより、既知の悪質なIPのブロック、Torアクセスの制限、P2Pトラフィックの制限、高度なネットワークセキュリティ監視を適用することができます。これらの高度なルールを導入することで、ネットワークのセキュリティ態勢を大幅に強化することができます*。

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

#### 高度なToRブロッキング
より高度なToRブロッキングを行うには、以下のようにします：
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### オプションの設定
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## 結論

これらのセキュリティ対策を実施することで、Linux上のインターネット共有アプリのセキュリティを強化し、マルウェア、トラッカー、Torトラフィック、Torrentを効果的にブロックすることができます。

システムおよびアプリケーションを常に最新の状態に保ち、ネットワークをさらに保護するために追加の高度なルールを適用することが重要であることを忘れないでください。

## 参考文献

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
