---
title: "Beveilig uw toepassingen voor internetdeling: Effectieve maatregelen voor een betere bescherming"
draft: false
toc: true
date: 2023-06-01
description: "Leer hoe u uw Linux-apps voor internetdeling kunt beveiligen met geavanceerde maatregelen om malware, trackers, Tor-verkeer en torrents te blokkeren."
tags: ["Linux beveiliging", "apps voor het delen van internet", "bescherming tegen malware", "tracker blokkeren", "Tor verkeer blokkeren", "preventie van torrents", "netwerkbeveiliging", "Snort", "Securita", "DNS-bescherming", "geavanceerde firewall-regels", "Ubuntu updates", "automatische updates", "netwerkbewaking", "cyberbeveiliging", "Linux internetbeveiliging", "Linux app beveiliging", "malware blokkering", "Tor-verkeer voorkomen", "torrent bescherming", "netwerk firewall", "Linux netwerkbeveiliging", "veilig delen via internet", "Linux DNS bescherming", "geavanceerde netwerkbeveiliging", "Linux systeem updates", "tools voor netwerkbewaking", "Linux-cyberbeveiligingsmaatregelen", "Linux beveiligingspraktijken"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "Een cartoonillustratie met een schild dat een netwerk van onderling verbonden apparaten beschermt tegen kwaadaardige bedreigingen."
coverCaption: ""
---

**Hoe beveilig je applicaties voor internetdeling op Linux**

De beveiliging van apps voor internetdeling op Linux is van het grootste belang om uw netwerk en gevoelige gegevens veilig te stellen. In dit artikel verkennen we effectieve strategieën om de beveiliging van deze apps te verbeteren en te beschermen tegen malware, trackers, Tor-verkeer en torrents.

### De beveiliging verhogen door malware en trackers te blokkeren

Een cruciale stap in de beveiliging van uw apps voor internetdeling is **het afdwingen van alle DNS-verzoeken naar Cloudflare's DNS voor malware- en trackingbescherming**. Door dit te doen, kunt u ervoor zorgen dat alle pogingen om toegang te krijgen tot kwaadaardige of tracking websites worden geblokkeerd, wat een extra beveiligingslaag biedt.

Om de beveiliging van uw netwerk verder te versterken wordt **het blokkeren van DNS/HTTPS-verzoeken** aanbevolen. Door deze verzoeken te beperken, kunt u potentiële beveiligingsproblemen en ongeoorloofde toegangspogingen voorkomen door ongecodeerde dns te forceren en zo een deel van het uitgaande bestemmingsverkeer te controleren.

*Als u toegang heeft tot een meer geavanceerde router of firewall op uw netwerk, kunt u gebruik maken van krachtige hulpmiddelen zoals [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) om extra regels op te stellen. Met deze tools kunt u bekende slecht handelende IP's blokkeren, Tor-toegang beperken, P2P-verkeer beperken en geavanceerde netwerkbeveiligingsbewaking toepassen. De toepassing van deze geavanceerde regels kan de beveiliging van uw netwerk aanzienlijk verbeteren.*

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

#### Geavanceerde ToR-blokkering
Voor meer geavanceerde ToR-blokkering kunt u het volgende doen:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Optionele configuraties:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Conclusie

Door deze beveiligingsmaatregelen te implementeren, kunt u de beveiliging van uw apps voor het delen van internet op Linux verbeteren, waarbij malware, trackers, Tor-verkeer en torrents effectief worden geblokkeerd.

Vergeet niet dat het essentieel is om je systeem en applicaties up-to-date te houden en aanvullende geavanceerde regels toe te passen indien beschikbaar om je netwerk verder te beschermen.

## Referenties

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
