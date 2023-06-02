---
title: "Asegure sus aplicaciones para compartir en Internet: Medidas eficaces para una mayor protección"
draft: false
toc: true
date: 2023-06-01
description: "Aprende a proteger tus aplicaciones Linux para compartir Internet con medidas avanzadas para bloquear malware, rastreadores, tráfico Tor y torrents."
tags: ["Seguridad en Linux", "aplicaciones para compartir internet", "protección antimalware", "bloqueo de rastreadores", "Bloqueo del tráfico Tor", "prevención de torrents", "seguridad de la red", "Snort", "Securita", "Protección DNS", "reglas avanzadas de cortafuegos", "Actualizaciones de Ubuntu", "actualizaciones automáticas", "supervisión de redes", "ciberseguridad", "Seguridad en Internet con Linux", "Seguridad de las aplicaciones Linux", "bloqueo de malware", "Prevención del tráfico Tor", "protección de torrents", "cortafuegos de red", "Seguridad de la red Linux", "compartir internet de forma segura", "Protección de DNS en Linux", "seguridad avanzada de redes", "Actualizaciones del sistema Linux", "herramientas de supervisión de redes", "Medidas de ciberseguridad en Linux", "Prácticas de seguridad en Linux"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "Ilustración de dibujos animados que muestra un escudo que protege una red de dispositivos interconectados de amenazas maliciosas."
coverCaption: ""
---

**Cómo proteger las aplicaciones para compartir Internet en Linux**

La seguridad de las aplicaciones para compartir Internet en Linux es de suma importancia para salvaguardar su red y sus datos sensibles. En este artículo, exploraremos estrategias efectivas para mejorar la seguridad de estas aplicaciones y protegerlas contra malware, rastreadores, tráfico Tor y torrents.

### Aumentar la Seguridad Bloqueando el Malware y los Rastreadores

Un paso crucial para asegurar tus aplicaciones para compartir en Internet es **forzar todas las peticiones DNS al DNS de protección contra malware y rastreadores de Cloudflare**. Al hacerlo, puede asegurarse de que se bloquee cualquier intento de acceder a sitios web maliciosos o de seguimiento, lo que proporciona una capa adicional de seguridad.

Para reforzar aún más la seguridad de su red, se recomienda **bloquear las solicitudes DNS/HTTPS**. Restringiendo estas peticiones, puedes prevenir potenciales vulnerabilidades de seguridad e intentos de acceso no autorizados forzando dns no encriptados y pudiendo así controlar parte del tráfico de destino saliente.

*Si tienes acceso a un router o firewall más avanzado en tu red, puedes aprovechar potentes herramientas como [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) para crear reglas adicionales. Estas herramientas le permiten bloquear IP maliciosas conocidas, restringir el acceso a Tor, limitar el tráfico P2P y aplicar una supervisión avanzada de la seguridad de la red. La aplicación de estas reglas avanzadas puede mejorar significativamente la seguridad de su red.

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

#### Bloqueo ToR avanzado
Para un bloqueo ToR más avanzado, puede hacer lo siguiente:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Configuraciones opcionales:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Conclusión

Implementando estas medidas de seguridad, puedes mejorar la seguridad de tus aplicaciones para compartir internet en Linux, bloqueando eficazmente malware, rastreadores, tráfico Tor y torrents.

Recuerda, es esencial mantener tu sistema y aplicaciones actualizados y aplicar reglas avanzadas adicionales si están disponibles para proteger aún más tu red.

## Referencias

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
