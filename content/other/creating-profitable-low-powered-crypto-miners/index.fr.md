---
title: "Construire une boîte de revenu passif rentable avec du matériel à faible puissance : un guide"
draft: false
toc: true
date: 2023-02-07
description: "Apprenez à configurer un crypto-mineur à faible revenu passif à l'aide d'un Raspberry Pi ou d'Intel NUC, et gagnez 10 à 20 $ par mois et par boîte avec ce guide"
tags: ["Construire une boîte de revenu passif rentable", "Matériel de faible puissance", "Revenu passif", "Mineur de crypto", "Tarte aux framboises", "Intel® NUC", "Guide", "Exigences matérielles", "Installation du système d'exploitation", "Installation du logiciel", "Docker", "Mises à jour automatiques du conteneur Docker", "Serveur Ubuntu", "Bureau Ubuntu", "raspbian", "Budget", "USFF", "Minuscule", "mini", "Micro-ordinateur", "Expérience technique", "EarnApp", "MYST", "Peer2Profit", "MielGain", "Moniteur de trafic", "Tour de guet", "Mordre", "Mises à jour Linux", "Ubuntu", "DebianName", "CentOS", "RHEL", "mises à jour hors ligne", "référentiel local", "cache", "configuration du serveur", "configuration du client", "apt-miroir", "debmirror", "créer un dépôt", "apt-cacher-ng", "miam-cron", "Mises à jour du système Linux", "mises à jour hors ligne des packages", "mises à jour logicielles hors ligne", "référentiel de packages local", "cache de paquets local", "mises à jour Linux hors ligne", "gestion des mises à jour hors ligne", "méthodes de mise à jour hors ligne", "maintenance du système hors ligne", "Mises à jour du serveur Linux", "Mises à jour des clients Linux", "gestion des logiciels hors ligne", "gestion hors ligne des packages", "mettre à jour les stratégies", "Mises à jour de sécurité Linux"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "un circuit imprimé vert en forme de boîte avec des symboles de connectivité Internet sous forme de fils connectés."
coverCaption: ""
---

**Construire une boîte de revenu passif rentable avec du matériel à faible puissance : un guide**
Beaucoup de gens ces jours-ci sont dans l'extraction de crypto et les mineurs de faible puissance tels que les mineurs d'hélium. Ce sont super et tout, mais ils ne gagnent plus beaucoup et ils se concentrent sur un seul type de revenu. Aujourd'hui, nous allons construire une boîte à revenus passifs à faible puissance qui rapporte entre 10 et 20 $ par mois par boîte et IP résidentielle.

* Si vous avez la possibilité de configurer ce boîtier sur un réseau invité ou, mieux encore, sur un VLAN séparé, faites-le. Bien qu'il s'agisse d'un blog sur la sécurité, nous ne pouvons pas assumer les problèmes de sécurité et la tolérance au risque de chacun.*

## Exigences matérielles:
L'un des éléments suivants est requis. Nous avons simplement besoin d'un ordinateur efficace et peu puissant sur lequel nous pouvons mettre la main. N'importe quel Raspberry PI, Intel NUC ou similaire fera l'affaire. Ils n'ont pas besoin d'être si puissants. Cependant, je vous recommanderai d'avoir au moins 32g-64g de stockage, 4g de RAM et au moins 2 threads cpu. Pour cela, nous visons un budget d'environ 100 à 200 dollars pour le matériel, mais n'hésitez pas à augmenter si cela répond à vos besoins. Notre objectif de puissance est d'env. 25w en moyenne.
### Tarte aux framboises:
Difficile à obtenir ces jours-ci, mais ils sont très peu puissants et sont assez personnalisables. Pour savoir comment installer raspian sur votre Raspberry PI
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Nuc Intel :
Grande variété de modèles disponibles. N'hésitez pas à en choisir un plus récent.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### N'importe quel USFF/Tiny/Mini/Micro PC :
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Tout mini PC avec Intel N5100 ou similaire
Pour l'équivalent Raspberry Pi super basse consommation mais sur plate-forme x64.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Installation du système d'exploitation :
Nous n'entrerons pas ici dans les détails techniques de l'installation d'un système d'exploitation. Cependant, voici quelques excellentes ressources pour vous aider à démarrer
### Raspbian :
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu :
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Installation du logiciel:
Cela va être une section plus longue. Nous allons configurer Docker, puis via Docker, nous allons configurer les mises à jour automatiques des conteneurs Docker et installer plusieurs conteneurs Docker. Nous supposons également que vous utilisez le serveur ubuntu, mais les commandes pour le serveur ubuntu, le bureau ubuntu et raspbian doivent toutes être les mêmes.

*Pour cette section, nous supposons une certaine expérience technique de base et que vous avez déjà installé votre système d'exploitation et que vous savez comment accéder au terminal.*

### Installation de mises à jour:
Nous voulons d'abord nous assurer que notre système est entièrement à jour :
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Installation de Docker :
Nous devons désinstaller toutes les versions existantes qui sont préemballées avec le système d'exploitation et installer la dernière version du dépôt de Docker eux-mêmes.
```bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Installez Watchtower :
Ce conteneur Docker met automatiquement à jour tous vos conteneurs Docker avec les dernières images à intervalles réguliers et nettoie les anciennes images (périmées).
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Installer Bitping :
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping vous offre la possibilité d'être payé à Solana pour fournir un nœud permettant aux entreprises d'exécuter des tests réseau légers à partir de votre réseau.
Cela représente en moyenne environ 0,1 cents par jour et par nœud. Je ne sais pas grand-chose, mais il a du potentiel et les paiements sont faciles.

#### Créer un compte:
Créez un compte sur [bitping.com](https://bitping.com)

#### Installez le conteneur Docker :
Étape 1. Exécutez d'abord ces commandes car elles vous guident dans la configuration de votre conteneur et vous demandent de vous connecter.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Appuyez sur CTRL + C sur votre clavier pour échapper au conteneur après vous être connecté avec votre compte bitping.

Étape 2. Exécutez cette commande pour conserver le conteneur en arrière-plan
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Installez l'application Earn :
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/GCL9QzB5)

L'application Earn vous permet de partager votre Internet en tant que service VPN pour une quantité surprenante de récompenses. Moyenne d'environ 5 $ par mois par nœud et par adresse IP résidentielle. Offre des paiements via des cartes-cadeaux paypal et amazon.

#### Créer un compte d'application :
Créez un compte sur [earnapp.com](https://earnapp.com/i/GCL9QzB5)
*Attention, nécessite un compte google*

#### Installez la version non docker de l'application pour obtenir votre UUID :
Assurez-vous de désinstaller après avoir obtenu votre UUID, sinon vous finirez par l'exécuter deux fois sur le même hôte et sans mises à jour automatiques
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Installez le conteneur Docker :
Modifiez la chaîne avant de la coller dans votre terminal. Vous devez spécifier l'UUID de votre application de gain.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Didacticiel vidéo:
{{< youtube id="tt499o0OjGU" >}}

### Installez Honey Gain :
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Honey Gain vous permet de partager votre Internet en tant que service VPN pour une quantité surprenante de récompenses. Moyenne d'environ 5 $ par mois par nœud et par adresse IP résidentielle. Les paiements peuvent être compliqués. Lisez-le plus en détail avant de décider d'utiliser ce conteneur

#### Créez un compte Honey Gain :
Créez un compte sur [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Installez le conteneur Docker :
Modifiez la chaîne avec l'e-mail, le mot de passe et le nom de l'appareil évidents avant de la coller dans le terminal
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Instructions alternatives pour Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Didacticiel vidéo:
{{< youtube id="Wd11M0nSy1k" >}}

### Installez PawnsApp :
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
L'application Pawns, encore une fois similaire aux autres répertoriées ici, propose de vous payer pour le partage de votre Internet. Le paiement minimum est de 5 $. Le paiement moyen est de 0,50 USD par mois, par nœud et par IP.

#### Créez un compte PawnsApp :
Créez un compte sur [https://pawns.app](https://pawns.app/?r=2092882)

#### Installez le conteneur Docker :

Modifiez les éléments suivants avec votre e-mail, votre mot de passe, le nom de l'appareil et l'identifiant de l'appareil avant de copier sur votre terminal.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```


### Installer Repoche :
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Semblable à d'autres offres ici. Paiement minimum de 20 $. Les paiements peuvent être compliqués. Faites des recherches par vous-même pour voir si vous souhaitez utiliser ce service. Les paiements sont en moyenne d'environ 1 $ par nœud par boîte et par mois.

#### Créer un compte de remboursement :
Créez un compte sur [repocket.co](https://link.repocket.co/raqc) et récupérez votre clé API depuis votre tableau de bord.
#### Installez le conteneur Docker :
Modifiez la ligne suivante avec votre e-mail et votre clé API avant de la coller dans votre terminal.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Didacticiel vidéo:
{{< youtube id="171gWknfAbY" >}}

### Installer le monétiseur de trafic :
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Semblable à EarnApp et HoneyGain, TraffMonetizer vous paie pour partager votre Internet. Moyenne d'environ 2 $ par mois par nœud par adresse IP. Offre uniquement des paiements en BTC.

#### Créez votre compte Traff Monetizer :
Créez votre compte sur [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Une fois dans le tableau de bord, notez votre jeton d'application.

#### Installez le conteneur Docker :
Copiez la chaîne suivante et ajoutez votre jeton que vous avez obtenu du tableau de bord avant de le coller dans votre terminal.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### Installez Mysterium :
[Mysterium](https://www.mysterium.network/) est un VPN décentralisé et un service de webscraping construit sur les blockchains Etherium et Polygon.
Les paiements se situent en moyenne entre 1 $ et 20 $ par mois, en fonction de plusieurs facteurs par nœud et par IP. Coûte 1,XX $ pour configurer un nœud pour l'activation. Paiements en jeton MYST.


#### Installez le conteneur Docker :
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Configurez le conteneur Docker :
Allez sur http://"nodeip"/#/dashboard en remplaçant "nodeip" par l'adresse IP de votre node. Vous pouvez le trouver en tapant "ifconfig" dans le terminal.

Cliquez sur "Démarrer la configuration du nœud".

Collez l'adresse du portefeuille ERC20 dans lequel vous souhaitez recevoir des récompenses et cliquez sur "Suivant". Vous pouvez utiliser une adresse Ethereum standard comme l'une de vos adresses MetaMask.

Tapez un mot de passe que vous utiliserez pour accéder à ce tableau de bord de nœud à l'avenir. Cochez la case pour revendiquer le nœud de votre réseau.

Cliquez sur le lien "Obtenez-le ici" et trouvez votre clé API. Copiez-le. Revenez en arrière et collez-le. Cliquez sur "Enregistrer et continuer".

#### Transfert de port :
Nous ne pouvons pas décrire comment transférer le port pour le matériel spécifique de chacun. Voici quelques ressources pour apprendre à transférer des ports.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Redémarrage automatique des conteneurs Docker au démarrage :
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Configurations facultatives :
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Augmentez la sécurité en bloquant les logiciels malveillants et les trackers.
Forcez toutes les requêtes DNS aux logiciels malveillants Cloudflares et au DNS de protection de suivi.
Bloquez également les requêtes DNS/HTTPS.
* Si vous disposez d'un routeur ou d'un pare-feu plus avancé sur le réseau, vous pouvez même utiliser des packages tels que snort/securita pour créer des règles plus avancées afin de bloquer les adresses IP, l'accès tor, les torrents, le trafic p2p en général, etc. suggéré mais pas obligatoire.*
```bash
# Allow ssh still
sudo ufw allow 22
# Allow dns out
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp
# Redirect all dns back to 1.1.1.2 or 1.0.0.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.0.0.2 -j DNAT --to-destination 1.1.1.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.1.1.2 -j DNAT --to-destination 1.0.0.2
# Block DNS over HTTPS
sudo ufw deny out 853/tcp
sudo ufw deny out 853/udp 
iptables -A FORWARD -m string --string "get_peers" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "announce_peer" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "find_node" --algo bm -j LOGDROP
# Block Default ToR Ports
sudo ufw deny out 9050/tcp
sudo ufw deny out 9050/udp
sudo ufw deny out 9051/tcp
sudo ufw deny out 9051/udp
# Block Torrents
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
# Save the Changes and Enable the Firewall
sudo iptables-save
sudo ufw enable
```
Pour un blocage ToR plus avancé, vous pouvez procéder comme suit :
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## Profit?