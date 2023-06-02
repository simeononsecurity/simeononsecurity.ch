---
title: "Proteggere le applicazioni di condivisione su Internet: Misure efficaci per una maggiore protezione"
draft: false
toc: true
date: 2023-06-01
description: "Imparate a proteggere le vostre applicazioni di condivisione internet su Linux con misure avanzate per bloccare malware, tracker, traffico Tor e torrent."
tags: ["Sicurezza di Linux", "applicazioni per la condivisione di internet", "protezione da malware", "blocco del tracker", "Blocco del traffico Tor", "prevenzione dei torrent", "sicurezza della rete", "Sbuffare", "Securita", "Protezione DNS", "regole avanzate del firewall", "Aggiornamenti di Ubuntu", "aggiornamenti automatici", "monitoraggio della rete", "sicurezza informatica", "Sicurezza Internet di Linux", "Sicurezza delle applicazioni Linux", "blocco del malware", "Prevenzione del traffico Tor", "protezione torrent", "firewall di rete", "Sicurezza della rete Linux", "condivisione sicura di Internet", "Protezione DNS di Linux", "sicurezza di rete avanzata", "Aggiornamenti del sistema Linux", "strumenti di monitoraggio della rete", "Misure di cybersicurezza per Linux", "Pratiche di sicurezza Linux"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "Un'illustrazione a fumetti che mostra uno scudo che protegge una rete di dispositivi interconnessi da minacce dannose."
coverCaption: ""
---

**Come proteggere le applicazioni di condivisione di Internet su Linux**

La sicurezza delle applicazioni di condivisione Internet su Linux è di fondamentale importanza per salvaguardare la rete e i dati sensibili. In questo articolo esploreremo le strategie più efficaci per migliorare la sicurezza di queste app e per proteggerle da malware, tracker, traffico Tor e torrent.

### Aumentare la sicurezza bloccando malware e tracker

Un passo fondamentale per proteggere le vostre app di condivisione su Internet è quello di **forzare tutte le richieste DNS al DNS di protezione da malware e tracker di Cloudflare**. In questo modo, è possibile garantire il blocco di qualsiasi tentativo di accesso a siti web dannosi o di tracciamento, fornendo un ulteriore livello di sicurezza.

Per rafforzare ulteriormente la sicurezza della rete, si consiglia di **bloccare le richieste DNS/HTTPS**. Limitando queste richieste, si possono prevenire potenziali vulnerabilità di sicurezza e tentativi di accesso non autorizzati, forzando i dns non criptati e potendo così controllare parte del traffico di destinazione in uscita.

*Se si ha accesso a un router o a un firewall più avanzato sulla propria rete, è possibile sfruttare strumenti potenti come [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) per creare regole aggiuntive. Questi strumenti consentono di bloccare IP noti che agiscono in modo scorretto, limitare l'accesso a Tor, limitare il traffico P2P e applicare un monitoraggio avanzato della sicurezza di rete. L'implementazione di queste regole avanzate può migliorare in modo significativo la sicurezza della rete.

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

#### Blocco ToR avanzato
Per un blocco ToR più avanzato, è possibile procedere come segue:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Configurazioni opzionali:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Conclusione

Implementando queste misure di sicurezza, è possibile migliorare la sicurezza delle applicazioni di condivisione di Internet su Linux, bloccando efficacemente malware, tracker, traffico Tor e torrent.

Ricordate che è essenziale mantenere il sistema e le applicazioni aggiornate e applicare regole avanzate aggiuntive, se disponibili, per proteggere ulteriormente la rete.

## Riferimenti

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
