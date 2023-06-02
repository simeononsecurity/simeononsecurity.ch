---
title: "Sécurisez vos applications de partage d'Internet : Des mesures efficaces pour une protection renforcée"
draft: false
toc: true
date: 2023-06-01
description: "Apprenez à sécuriser vos applications Linux de partage d'Internet avec des mesures avancées pour bloquer les logiciels malveillants, les traqueurs, le trafic Tor et les torrents."
tags: ["Linux security", "applications de partage de l'internet", "protection contre les logiciels malveillants", "blocage du traceur", "Blocage du trafic Tor", "prévention des torrents", "sécurité des réseaux", "Snort", "Securita", "Protection DNS", "règles avancées de pare-feu", "Mises à jour d'Ubuntu", "mises à jour automatiques", "surveillance du réseau", "cybersécurité", "Linux internet security", "Sécurité des applications Linux", "blocage des logiciels malveillants", "Prévention du trafic Tor", "torrent protection", "pare-feu réseau", "Sécurité du réseau Linux", "partage sécurisé de l'internet", "Linux DNS protection", "sécurité avancée des réseaux", "Mises à jour du système Linux", "outils de surveillance du réseau", "Mesures de cybersécurité pour Linux", "Pratiques de sécurité Linux"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "Dessin humoristique montrant un bouclier protégeant un réseau d'appareils interconnectés contre les menaces malveillantes."
coverCaption: ""
---

**Comment sécuriser les applications de partage d'Internet sous Linux**

La sécurité des applications de partage Internet sous Linux est d'une importance capitale pour protéger votre réseau et vos données sensibles. Dans cet article, nous allons explorer des stratégies efficaces pour améliorer la sécurité de ces applications et les protéger contre les logiciels malveillants, les traqueurs, le trafic Tor et les torrents.

### Augmenter la sécurité en bloquant les logiciels malveillants et les traqueurs

Une étape cruciale dans la sécurisation de vos applications de partage d'Internet consiste à **forcer toutes les requêtes DNS vers le DNS de protection contre les logiciels malveillants et les traqueurs de Cloudflare**. Ce faisant, vous pouvez vous assurer que toute tentative d'accès à des sites Web malveillants ou de traçage est bloquée, ce qui constitue une couche de sécurité supplémentaire.

Pour renforcer encore la sécurité de votre réseau, il est recommandé de **bloquer les requêtes DNS/HTTPS**. En limitant ces requêtes, vous pouvez prévenir les failles de sécurité potentielles et les tentatives d'accès non autorisé en forçant les DNS non cryptés et en étant ainsi en mesure de contrôler une partie du trafic de destination sortant.

*Si vous avez accès à un routeur ou à un pare-feu plus avancé sur votre réseau, vous pouvez utiliser des outils puissants tels que [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) pour créer des règles supplémentaires. Ces outils vous permettent de bloquer les IP connues pour leur mauvaise action, de restreindre l'accès à Tor, de limiter le trafic P2P et d'appliquer une surveillance avancée de la sécurité du réseau. La mise en œuvre de ces règles avancées peut améliorer considérablement la sécurité de votre réseau.*

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

#### Blocage avancé des ToR
Pour un blocage ToR plus avancé, vous pouvez procéder comme suit :
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Configurations optionnelles :
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Conclusion

En mettant en œuvre ces mesures de sécurité, vous pouvez améliorer la sécurité de vos applications de partage Internet sous Linux, en bloquant efficacement les logiciels malveillants, les traqueurs, le trafic Tor et les torrents.

N'oubliez pas qu'il est essentiel de maintenir votre système et vos applications à jour et d'appliquer des règles avancées supplémentaires, le cas échéant, pour mieux protéger votre réseau.

## Références

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
