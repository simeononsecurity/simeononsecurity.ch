---
title: "Protejați-vă aplicațiile de partajare pe internet: Măsuri eficiente pentru o protecție sporită"
draft: false
toc: true
date: 2023-06-01
description: "Aflați cum să vă protejați aplicațiile de partajare pe internet Linux cu măsuri avansate pentru a bloca programele malware, urmăritorii, traficul Tor și torrentele."
tags: ["Securitate Linux", "aplicații de partajare pe internet", "protecție împotriva malware-ului", "blocarea urmăritorilor", "Blocarea traficului Tor", "prevenirea torrentului", "securitatea rețelei", "Snort", "Securita", "Protecția DNS", "reguli avansate de firewall", "Actualizări Ubuntu", "actualizări automate", "monitorizarea rețelei", "securitate cibernetică", "Linux securitate pe internet", "Securitatea aplicațiilor Linux", "blocarea malware", "Prevenirea traficului Tor", "protecție torrent", "firewall de rețea", "Securitatea rețelei Linux", "partajarea securizată a internetului", "Protecție DNS Linux", "securitate avansată a rețelei", "Actualizări ale sistemului Linux", "instrumente de monitorizare a rețelei", "Măsuri de securitate cibernetică Linux", "Practici de securitate Linux"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "O ilustrație de desen animat care prezintă un scut care protejează o rețea de dispozitive interconectate împotriva amenințărilor rău intenționate."
coverCaption: ""
---

**Cum să securizați aplicațiile de partajare a internetului pe Linux**

Securitatea aplicațiilor de partajare a internetului pe Linux este de o importanță capitală pentru a vă proteja rețeaua și datele sensibile. În acest articol, vom explora strategii eficiente pentru a spori securitatea acestor aplicații și pentru a le proteja împotriva malware-ului, trackerilor, traficului Tor și torrentelor.

### Creșterea securității prin blocarea programelor malware și a urmăritorilor

Un pas crucial în securizarea aplicațiilor de partajare pe internet este să **forțați toate cererile DNS către DNS-ul de protecție împotriva malware-ului și a urmăririi de la Cloudflare**. Procedând astfel, vă puteți asigura că orice încercare de accesare a site-urilor web malițioase sau de urmărire este blocată, oferind un nivel suplimentar de securitate.

Pentru a consolida și mai mult securitatea rețelei dumneavoastră, se recomandă **blocarea cererilor DNS/HTTPS**. Prin restricționarea acestor solicitări, puteți preveni potențiale vulnerabilități de securitate și încercări de acces neautorizat prin forțarea DNS necriptate și, astfel, puteți controla o parte din traficul de destinație de ieșire.

*Dacă aveți acces la un router mai avansat sau la un firewall în rețeaua dumneavoastră, puteți utiliza instrumente puternice, cum ar fi [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) pentru a crea reguli suplimentare. Aceste instrumente vă permit să blocați IP-urile cunoscute ca fiind rău-platnice, să restricționați accesul la Tor, să limitați traficul P2P și să aplicați o monitorizare avansată a securității rețelei. Punerea în aplicare a acestor reguli avansate poate îmbunătăți în mod semnificativ poziția de securitate a rețelei dumneavoastră.*

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

#### Blocaj ToR avansat
Pentru o blocare ToR mai avansată, puteți face următoarele:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Configurații opționale:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Concluzie

Prin implementarea acestor măsuri de securitate, puteți spori securitatea aplicațiilor de partajare pe internet pe Linux, blocând în mod eficient programele malware, urmăritorii, traficul Tor și torrentele.

Nu uitați, este esențial să vă mențineți sistemul și aplicațiile actualizate și să aplicați reguli avansate suplimentare, dacă sunt disponibile, pentru a vă proteja și mai mult rețeaua.

## Referințe

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
