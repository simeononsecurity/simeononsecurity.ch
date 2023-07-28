---
title: "Защита приложений для совместного доступа в Интернет: Эффективные меры для усиления защиты"
draft: false
toc: true
date: 2023-06-01
description: "Узнайте, как защитить приложения для совместного доступа к Интернету в Linux с помощью передовых мер по блокированию вредоносного ПО, трекеров, трафика Tor и торрентов."
tags: ["Безопасность Linux", "приложения для совместного использования интернета", "защита от вредоносного ПО", "блокировка трекера", "Блокировка трафика Tor", "предотвращение торрентов", "безопасность сети", "Snort", "Securita", "Защита DNS", "расширенные правила межсетевого экрана", "Обновления Ubuntu", "автоматические обновления", "мониторинг сети", "кибербезопасность", "Интернет-безопасность Linux", "Безопасность приложений в Linux", "блокировка вредоносных программ", "Предотвращение трафика Tor", "защита торрентов", "сетевой брандмауэр", "Сетевая безопасность Linux", "безопасное совместное использование Интернета", "Защита DNS в Linux", "расширенная сетевая безопасность", "Обновление системы Linux", "средства мониторинга сети", "Меры кибербезопасности в Linux", "Методы обеспечения безопасности в Linux"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "Мультипликационная иллюстрация, изображающая щит, защищающий сеть взаимосвязанных устройств от вредоносных угроз."
coverCaption: ""
---

**Как защитить приложения для совместного доступа к Интернету в Linux**.

Безопасность приложений для совместного доступа к Интернету в Linux имеет первостепенное значение для защиты сети и конфиденциальных данных. В этой статье мы рассмотрим эффективные стратегии повышения безопасности этих приложений и защиты от вредоносного ПО, трекеров, трафика Tor и торрентов.

### Повышение безопасности путем блокирования вредоносного ПО и трекеров

Одним из важнейших шагов в обеспечении безопасности приложений для совместного доступа в Интернет является **принудительная отправка всех DNS-запросов на DNS Cloudflare для защиты от вредоносного ПО и трекеров**. Это позволит блокировать любые попытки доступа к вредоносным или отслеживающим веб-сайтам, обеспечивая дополнительный уровень безопасности.

Для дальнейшего усиления безопасности сети рекомендуется **блокировать DNS/HTTPS-запросы**. Ограничение этих запросов позволяет предотвратить потенциальные уязвимости в системе безопасности и попытки несанкционированного доступа, заставляя использовать незашифрованные DNS и тем самым контролируя часть исходящего целевого трафика.

*Если в вашей сети имеется доступ к более совершенному маршрутизатору или межсетевому экрану, вы можете использовать такие мощные инструменты, как [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) для создания дополнительных правил. Эти инструменты позволяют блокировать известные IP-адреса, ограничивать доступ к Tor, ограничивать P2P-трафик и применять расширенный мониторинг сетевой безопасности. Применение этих дополнительных правил может значительно повысить уровень безопасности сети.*

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

#### Расширенное блокирование ToR
Для более сложного блокирования ToR можно сделать следующее:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Дополнительные конфигурации:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Заключение

Применив эти меры безопасности, вы сможете повысить защищенность приложений для совместного использования Интернета в Linux, эффективно блокируя вредоносное ПО, трекеры, трафик Tor и торренты.

Помните, что необходимо поддерживать систему и приложения в актуальном состоянии и применять дополнительные расширенные правила, если они доступны, для дальнейшей защиты сети.

## Ссылки

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
