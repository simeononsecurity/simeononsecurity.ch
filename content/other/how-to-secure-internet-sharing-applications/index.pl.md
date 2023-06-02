---
title: "Zabezpiecz swoje aplikacje do udostępniania Internetu: Skuteczne środki zwiększające ochronę"
draft: false
toc: true
date: 2023-06-01
description: "Dowiedz się, jak zabezpieczyć aplikacje do udostępniania Internetu w systemie Linux za pomocą zaawansowanych środków blokowania złośliwego oprogramowania, modułów śledzących, ruchu Tor i torrentów."
tags: ["Bezpieczeństwo systemu Linux", "aplikacje do udostępniania w internecie", "ochrona przed złośliwym oprogramowaniem", "blokowanie trackera", "Blokowanie ruchu Tor", "zapobieganie torrentom", "bezpieczeństwo sieci", "Snort", "Securita", "Ochrona DNS", "zaawansowane reguły zapory", "Aktualizacje Ubuntu", "automatyczne aktualizacje", "monitorowanie sieci", "cyberbezpieczeństwo", "Bezpieczeństwo internetowe w systemie Linux", "Bezpieczeństwo aplikacji Linux", "Blokowanie złośliwego oprogramowania", "Zapobieganie ruchowi Tor", "ochrona torrentów", "zapora sieciowa", "Bezpieczeństwo sieci Linux", "Bezpieczne udostępnianie Internetu", "Ochrona DNS w systemie Linux", "zaawansowane bezpieczeństwo sieci", "Aktualizacje systemu Linux", "narzędzia do monitorowania sieci", "Środki cyberbezpieczeństwa systemu Linux", "Praktyki bezpieczeństwa systemu Linux"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "Rysunkowa ilustracja przedstawiająca tarczę chroniącą sieć połączonych urządzeń przed złośliwymi zagrożeniami."
coverCaption: ""
---

**Jak zabezpieczyć aplikacje do udostępniania Internetu w systemie Linux**

Bezpieczeństwo aplikacji do udostępniania Internetu w systemie Linux ma ogromne znaczenie dla ochrony sieci i wrażliwych danych. W tym artykule zbadamy skuteczne strategie zwiększania bezpieczeństwa tych aplikacji i ochrony przed złośliwym oprogramowaniem, trackerami, ruchem Tor i torrentami.

### Zwiększenie bezpieczeństwa poprzez blokowanie złośliwego oprogramowania i trackerów

Jednym z kluczowych kroków w zabezpieczaniu aplikacji do udostępniania Internetu jest **wymuszenie wszystkich żądań DNS do złośliwego oprogramowania Cloudflare i ochrony przed śledzeniem DNS**. W ten sposób można upewnić się, że wszelkie próby uzyskania dostępu do złośliwych lub śledzących stron internetowych są blokowane, zapewniając dodatkową warstwę bezpieczeństwa.

Aby jeszcze bardziej wzmocnić bezpieczeństwo sieci, zaleca się **blokowanie żądań DNS/HTTPS**. Ograniczając te żądania, można zapobiec potencjalnym lukom w zabezpieczeniach i nieautoryzowanym próbom dostępu, wymuszając niezaszyfrowane DNS, a tym samym będąc w stanie kontrolować część wychodzącego ruchu docelowego.

*Jeśli masz dostęp do bardziej zaawansowanego routera lub firewalla w swojej sieci, możesz wykorzystać potężne narzędzia, takie jak [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) aby utworzyć dodatkowe reguły. Narzędzia te umożliwiają blokowanie znanych adresów IP o złym działaniu, ograniczanie dostępu do sieci Tor, ograniczanie ruchu P2P i stosowanie zaawansowanego monitorowania bezpieczeństwa sieci. Wdrożenie tych zaawansowanych reguł może znacznie poprawić stan bezpieczeństwa sieci*.

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

#### Zaawansowane blokowanie ToR
W celu bardziej zaawansowanego blokowania ToR można wykonać następujące czynności:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Konfiguracje opcjonalne:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Wnioski

Wdrażając te środki bezpieczeństwa, można zwiększyć bezpieczeństwo aplikacji do udostępniania Internetu w systemie Linux, skutecznie blokując złośliwe oprogramowanie, moduły śledzące, ruch Tor i torrenty.

Pamiętaj, że ważne jest, aby aktualizować system i aplikacje oraz stosować dodatkowe zaawansowane reguły, jeśli są dostępne, aby jeszcze bardziej chronić swoją sieć.

## Referencje

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
