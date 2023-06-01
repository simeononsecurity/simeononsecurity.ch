---
title: "Secure Your Internet Sharing Applications: Effective Measures for Enhanced Protection"
draft: false
toc: true
date: 2023-06-01
description: "Learn how to secure your Linux internet sharing apps with advanced measures to block malware, trackers, Tor traffic, and torrents."
tags: ["Linux security","internet sharing apps","malware protection","tracker blocking","Tor traffic blocking","torrent prevention","network security","Snort","Securita","DNS protection","advanced firewall rules","Ubuntu updates","automatic updates","network monitoring","cybersecurity","Linux internet security","Linux app security","malware blocking","Tor traffic prevention","torrent protection","network firewall","Linux network security","secure internet sharing","Linux DNS protection","advanced network security","Linux system updates","network monitoring tools","Linux cybersecurity measures","Linux security practices"]
cover: "/img/cover/A_cartoon_illustration_showing_a_shield_protecting_a_network.png"
coverAlt: "A cartoon illustration showing a shield protecting a network of interconnected devices from malicious threats."
coverCaption: ""
---

**How to Secure Internet Sharing Apps on Linux**

The security of internet sharing apps on Linux is of paramount importance to safeguard your network and sensitive data. In this article, we will explore effective strategies to enhance the security of these apps and protect against malware, trackers, Tor traffic, and torrents.

### Increase Security by Blocking Malware and Trackers

One crucial step in securing your internet sharing apps is to **force all DNS requests to Cloudflare's malware and tracking protection DNS**. By doing so, you can ensure that any attempts to access malicious or tracking websites are blocked, providing an additional layer of security.

To further strengthen the security of your network, **blocking DNS/HTTPS requests** is recommended. By restricting these requests, you can prevent potential security vulnerabilities and unauthorized access attempts by forcing unencrypted dns and thus being able to control some of the outbound destination traffic.

*If you have access to a more advanced router or firewall on your network, you can leverage powerful tools such as [**Snort**](https://www.snort.org/) or [**Securita**](https://www.securita.io/) to create additional rules. These tools enable you to block known bad-acting IPs, restrict Tor access, limit P2P traffic, and apply advanced network security monitoring. Implementing these advanced rules can significantly enhance your network's security posture.*

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

#### Advanced ToR Blocking
For more advanced ToR blocking, you can do the following:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

#### Optional Configurations:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)

## Conclusion

By implementing these security measures, you can enhance the security of your internet sharing apps on Linux, effectively blocking malware, trackers, Tor traffic, and torrents.

Remember, it's essential to keep your system and applications up to date and apply additional advanced rules if available to further protect your network.

## References

- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
- [Snort - Intrusion Detection and Prevention System](https://www.snort.org/)
- [Securita - Advanced Network Security Monitoring](https://www.securita.io/)
