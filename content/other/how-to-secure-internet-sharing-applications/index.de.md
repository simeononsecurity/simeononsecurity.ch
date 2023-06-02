---
title: "Sichern Sie Ihre Internet-Sharing-Anwendungen: Effektive Maßnahmen für verbesserten Schutz"
draft: false
toc: true
date: 2023-06-01
description: "Erfahren Sie, wie Sie Ihre Linux-Internet-Sharing-Anwendungen mit fortschrittlichen Maßnahmen zum Blockieren von Malware, Trackern, Tor-Traffic und Torrents absichern können."
tags: ["Linux-Sicherheit", "Internet-Sharing-Anwendungen", "Malwareschutz", "Tracker-Blockierung", "Blockierung des Tor-Verkehrs", "Torrent-Prävention", "Netzwerksicherheit", "Snort", "Securita", "DNS-Schutz", "erweiterte Firewall-Regeln", "Ubuntu-Aktualisierungen", "automatische Aktualisierungen", "Netzüberwachung", "Cybersicherheit", "Linux Internetsicherheit", "Sicherheit von Linux-Anwendungen", "Malware-Blockierung", "Verhinderung von Tor-Verkehr", "Torrentschutz", "Netzwerk-Firewall", "Linux-Netzwerksicherheit", "sicheres Internet-Sharing", "Linux DNS-Schutz", "erweiterte Netzwerksicherheit", "Linux-System-Updates", "Netzwerk-Überwachungstools", "Linux-Cybersicherheitsmaßnahmen", "Linux-Sicherheitspraktiken"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "Eine Cartoon-Illustration, die ein Schild zeigt, das ein Netz miteinander verbundener Geräte vor bösartigen Bedrohungen schützt."
coverCaption: ""
---

**Wie man Internetfreigabeanwendungen unter Linux sichert**

Die Sicherheit von Internet-Sharing-Anwendungen unter Linux ist von größter Bedeutung, um Ihr Netzwerk und Ihre sensiblen Daten zu schützen. In diesem Artikel werden wir effektive Strategien zur Verbesserung der Sicherheit dieser Apps und zum Schutz vor Malware, Trackern, Tor-Traffic und Torrents untersuchen.

### Erhöhen Sie die Sicherheit durch Blockieren von Malware und Trackern

Ein entscheidender Schritt zur Absicherung Ihrer Internet-Sharing-Apps besteht darin, **alle DNS-Anfragen an den Malware- und Tracking-Schutz-DNS von Cloudflare zu leiten**. Auf diese Weise können Sie sicherstellen, dass alle Versuche, auf bösartige oder Tracking-Websites zuzugreifen, blockiert werden, was eine zusätzliche Sicherheitsebene darstellt.

Um die Sicherheit Ihres Netzwerks weiter zu erhöhen, wird die **Blockierung von DNS/HTTPS-Anfragen** empfohlen. Durch die Einschränkung dieser Anfragen können Sie potenzielle Sicherheitslücken und unbefugte Zugriffsversuche verhindern, indem Sie unverschlüsseltes DNS erzwingen und so einen Teil des ausgehenden Zielverkehrs kontrollieren können.

*Wenn Sie Zugang zu einem fortschrittlicheren Router oder einer Firewall in Ihrem Netzwerk haben, können Sie leistungsfähige Tools einsetzen, wie z. B. [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) um zusätzliche Regeln zu erstellen. Mit diesen Tools können Sie bekannte bösartige IPs blockieren, den Tor-Zugang einschränken, den P2P-Verkehr begrenzen und eine erweiterte Überwachung der Netzwerksicherheit durchführen. Die Implementierung dieser erweiterten Regeln kann die Sicherheitslage Ihres Netzwerks erheblich verbessern.*

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

#### Erweiterte ToR-Blockierung
Für eine erweiterte ToR-Blockierung können Sie Folgendes tun:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Optionale Konfigurationen:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Schlussfolgerung

Durch die Implementierung dieser Sicherheitsmaßnahmen können Sie die Sicherheit Ihrer Internet-Sharing-Anwendungen unter Linux verbessern und Malware, Tracker, Tor-Traffic und Torrents effektiv blockieren.

Denken Sie daran, dass es wichtig ist, Ihr System und Ihre Anwendungen auf dem neuesten Stand zu halten und zusätzliche erweiterte Regeln anzuwenden, falls verfügbar, um Ihr Netzwerk weiter zu schützen.

## Referenzen

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
