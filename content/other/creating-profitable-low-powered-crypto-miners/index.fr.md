---
title: "Build a Profitable Passive Income Box with Low-Powered Hardware: A Guide"
draft: false
toc: true
date: 2023-02-07
description: "Learn how to set up a low-powered passive income crypto miner using a Raspberry Pi or Intel NUC, and earn $10-$20 per month per box with this guide"
tags: ["Build a Profitable Passive Income Box", "Low-Powered Hardware", "Passive Income", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Guide", "Hardware Requirements", "OS Installation", "Software Installation", "Docker", "Automatic Docker Container Updates", "Ubuntu Server", "Ubuntu Desktop", "Raspbian", "Budget", "USFF", "Tiny", "Mini", "Micro PC", "Technical Experience", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Watchtower", "Bitping"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "a green, circuit board shaped like a box with internet connectivity symbols as wires connected to it."
coverCaption: ""
---
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```
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
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```
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
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```
 **Construire une boîte de revenus passif louable avec du matériel à faible puissance : un guide** Beaucoup de gens ces jours-ci sont dans l'extraction de crypto et les mineurs de faible puissance tels que les mineurs d'hélium. Ce sont super et tout, mais ils ne gagnent plus beaucoup et ils se concentrent sur un seul type de revenu. Aujourd'hui, nous allons construire une boîte à revenus passifs à faible puissance qui rapporte entre 10 et 20 $ par mois par boîte et IP résidentielle.  * Si vous avez la possibilité de configurer ce boîtier sur un réseau invité ou, mieux encore, sur un VLAN séparé, faites-le. Bien qu'il s'agisse d'un blog sur la sécurité, nous ne pouvons pas assumer les problèmes de sécurité et la tolérance au risque de chacun.*  ## Exigences matérielles : L'un des éléments suivants est requis. Nous avons simplement besoin d'un ordinateur efficace et peu puissant sur lequel nous pouvons mettre la main. N'importe quel Raspberry PI, Intel NUC ou similaire fera l'affaire. Ils n'ont pas besoin d'être si puissants. Cependant, je vous recommandeai d'avoir au moins 32g-64g de stockage, 4g de RAM et au moins 2 threads cpu. Pour cela, nous visons un budget d'environ 100 à 200 dollars pour le matériel, mais n'hésitez pas à augmenter si cela répond à vos besoins. Notre objectif de puissance est d'env. 25w en moyenne. ### Tarte aux framboises : Difficile à obtenir ces jours-ci, mais ils sont très peu puissants et sont assez personnalisables. Pour savoir comment installer raspian sur votre Raspberry PI - [Kit de bricolage Raspberry Pi 4B modèle B] (https://amzn.to/3x72kv0) - [Kit de démarrage GeeekPi Raspberry Pi 4 4 Go] (https://amzn.to/3jG2g2k) - [Kit de démarrage GeeekPi Raspberry Pi 4 8 Go] (https://amzn.to/3DQisF6) ### Nuc Intel : Grande variété de modèles disponibles. N'hésitez pas à choisir un plus récent. - [Intel NUC 12 Pro] (https://amzn.to/3JTzLc7) - [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8) - [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6) ### N'importe quel USFF/Tiny/Mini/Micro PC : - [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642) - [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978) ### Tout mini PC avec Intel N5100 ou similaire Pour l'équivalent Raspberry Pi super basse consommation mais sur plate-forme x64. - [Mini PC Beelink U59] (https://amzn.to/3YkFhcj) - [Mini-ordinateur TRIGKEY] (https://amzn.to/3XkbXkS)  ## Installation du système d'exploitation : Nous n'entrerons pas dans les détails techniques de l'installation d'un système d'exploitation ici. Cependant, voici quelques excellentes ressources pour vous aider à démarrer ### Raspbien : - [Mise en route](https://www.raspberrypi.com/documentation/computers/getting-started.html) - [La nouvelle méthode pour configurer Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns) ### Ubuntu : - [Installer le bureau Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) - [Serveur Ubuntu - Installation de base](https://ubuntu.com/server/docs/installation) - [Guide complet du débutant Ubuntu : Télécharger et installer Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)   ## Installation du logiciel : Cela va être une section plus longue. Nous allons configurer Docker, puis via Docker, nous allons configurer les mises à jour automatiques des conteneurs Docker et installer plusieurs conteneurs Docker. Nous supposons également que vous utilisez le serveur ubuntu, mais les commandes pour le serveur ubuntu, le bureau ubuntu et raspbian doivent toutes être les mêmes.  *Pour cette section, nous supposons une certaine expérience technique de base et que vous avez déjà installé votre système d'exploitation et que vous savez comment accéder au terminal.*  ### Installation de mises à jour : Nous voulons d'abord nous assurer que notre système est entièrement à jour :  ### Installation de Docker : Nous devons désinstaller toutes les versions existantes qui sont préemballées avec le système d'exploitation et installer la dernière version du dépôt de Docker eux-mêmes.  ### Installer la tour de guet : Ce conteneur Docker met automatiquement à jour tous vos conteneurs Docker avec les dernières images à intervalles réguliers et nettoie les anciennes images (périmées).  ### Bitping de l'installateur : [* Bitping est une solution de surveillance et d'optimisation des performances de sites Web qui fournit une surveillance en temps réel et réelle des utilisateurs et des commentaires instantanés sur les temps d'arrêt ou les performances dégradées, avec des capacités de test de stress et d'analyse comparative, un reroutage et un reprovisionnement dynamiques alimentés par une couche d'intelligence réseau distribuée et l'intégration avec les flux de travail existants via des webhooks.*](https://bitping.com)  Bitping vous offre la possibilité d'être payé à Solana pour fournir un nœud permettant aux entreprises d'exécuter des tests réseau légers à partir de votre réseau. Cela représente en moyenne environ 0,1 cents par jour et par nœud. Je ne sais pas grand-chose, mais il a du potentiel et les paiements sont faciles.  #### Créer un compte : Créer un compte sur [bitping.com](https://bitping.com)  #### Installer le conteneur Docker Étape 1. Exécutez d'abord ces commandes car elles vous guident dans la configuration de votre conteneur et vous demandent de vous connecter.  Appuyez sur CTRL + C sur le clavier pour échapper au conteneur après vous être connecté avec votre compte bitping.  Étape 2. Exécutez cette commande pour conserver le conteneur en arrière-plan   ### Installer l'application [*Profitez du temps d'inactivité de vos appareils en étant payé pour les ressources inutilisées de votre appareil*](https://earnapp.com/i/c1dllee)  L'application Earn vous permet de partager votre Internet en tant que service VPN pour une quantité surprenante de récompenses. Moyenne d'environ 5 $ par mois par nœud et par adresse IP résidentielle. Offre des paiements via des cartes-cadeaux paypal et amazon.  #### Créez un compte d'application : Créez un compte sur [earnapp.com](https://earnapp.com/i/c1dllee). *Attention, nécessite un compte google*  #### Installez la version non docker de l'application pour obtenir votre UUID : demandez-vous de désinstaller après avoir obtenu votre UUID, sinon vous finirez par l'exécuter deux fois sur le même hôte et sans mises à jour automatiques - [Instructions] (https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)  #### Installer le conteneur Docker Modifiez la chaîne avant de coller dans votre terminal. Vous devez spécifier l'UUID de votre application de gain. #### Vidéo didactique : {{< youtube id="tt499o0OjGU" >}}  ### Installer Honey Gain : [* Revenu passif - Sans effort avec Honeygain, vous pouvez gagner de l'argent en partageant simplement votre Internet. Commencez à gagner maintenant.*](https://r.honeygain.me/DAVID07A75)  Honey Gain vous permet de partager votre Internet en tant que service VPN pour une quantité surprenante de récompenses. Moyenne d'environ 5 $ par mois par nœud et par adresse IP résidentielle. Les paiements peuvent être compliqués. Lisez-le plus en détail avant de décider d'utiliser ce conteneur  #### Créer un compte Honey Gain : Créez un compte sur [honeygain.com](https://r.honeygain.me/DAVID07A75)  #### Installer le conteneur Docker Modifiez la chaîne avec l'e-mail, le mot de passe et le nom de l'appareil évident avant de la coller dans le terminal  #### Instructions alternatives pour Raspberry Pi - [Comment installer Honeygain sur un Raspberry Pi avec un système d'exploitation Raspberry Pi standard] (https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)  #### Vidéo didactique : {{< youtube id="Wd11M0nSy1k" >}}  ### Installer PawnsApp : [* Gagnez de l'argent passif en ligne en répondant à des sondages et en partageant votre connexion Internet *] (https://pawns.app/?r=sos) L'application Pions, encore une fois similaire aux autres répertoriées ici, vous propose de vous payer pour le partage de votre Internet. Le paiement minimum est de 5 $. Le paiement moyen est de 0,50 USD par mois, par nœud et par IP.  #### Créez un compte PawnsApp : Créez un compte sur [https://pawns.app](https://pawns.app/?r=sos)  #### Installer le conteneur Docker  Modifiez les éléments suivants avec votre e-mail, votre mot de passe, le nom de l'appareil et l'identifiant de l'appareil avant de copier sur votre terminal.  ### Bénéfice du pair installateur 2  : [*PARTAGEZ VOTRE TRAFIC ET PROFITEZ-EN !*](https://p2pr.me/16538445386293aa3aaec4e)  Semblable à EarnApp et HoneyGain, Peer2Profit partage votre Internet à des fins de VPN et de grattage. Gagné environ 1 $ par mois par nœud et par IP. Offre une variété de paiements, y compris les mandats, BTC, LTC, LTC, MATIC, etc.  #### Créer un compte Peer 2 Profit : Créer un compte sur [peer2profit.com](https://p2pr.me/16538445386293aa3aaec4e)  #### Installer le conteneur Docker #### Vidéo didactique : {{< youtube id="J_rSV5N8aQk" >}}   ### Repoche de l'installateur : [* Soyez payé pour votre Internet inutilisé *] (https://link.repocket.co/pyqL)  Semblable à d'autres offres ici. Paiement minimum de 20 $. Les paiements peuvent être compliqués. Faites des recherches par vous-même pour voir si vous souhaitez utiliser ce service. Les paiements sont en moyenne d'environ 1 $ par nœud par boîte et par mois.  #### Créer un compte de remboursement : Créez un compte sur [repocket.co](https://link.repocket.co/pyqL) et récupérez votre clé API depuis votre tableau de bord. #### Installer le conteneur Docker Modifiez la ligne suivante avec votre e-mail et votre clé API avant de coller dans votre terminal. #### Vidéo didactique : {{< youtube id="171gWknfAbY" >}}  ### Installer le monétiseur de trafic : [*Partagez votre connexion Internet et gagnez de l'argent en ligne*](https://traffmonetizer.com/?aff=242022)  Semblable à EarnApp et HoneyGain, TraffMonetizer vous paie pour partager votre Internet. Moyenne d'environ 2 $ par mois par nœud par adresse IP. Offre uniquement des paiements en BTC.  #### Créez votre compte Monétiseur de trafic : Créez votre compte sur [https://traffmonetizer.com](https://traffmonetizer.com/?aff=242022) Une fois dans le tableau de bord, notez votre jeton d'application.  #### Installer le conteneur Docker Copiez la chaîne suivante et complétez votre jeton que vous avez obtenu du tableau de bord avant de le coller dans votre terminal.   ### Installer Mysterium : [Mysterium](https://www.mysterium.network/) est un VPN décentralisé et un service de webscraping intégré sur les blockchains Etherium et Polygon. Les paiements se font en moyenne entre 1 $ et 20 $ par mois, en fonction de plusieurs facteurs par nœud et par IP. Coûte 1,XX $ pour configurer un nœud pour l'activation. Paiements en jeton MYST.   #### Installer le conteneur Docker  #### Configurez le conteneur : Allez sur http://"nodeip"/#/dashboard en remplaçant "nodeip" par l'adresse IP de votre node. Vous pouvez le trouver en tapant "ifconfig" dans le terminal.  Cliquez sur "Démarrer la configuration du nœud".  Collez l'adresse du portefeuille ERC20 dans laquelle vous souhaitez recevoir des récompenses et cliquez sur "Suivant". Vous pouvez utiliser une adresse Ethereum standard comme l'une de vos adresses MetaMask.  Tapez un mot de passe que vous utiliserez pour accéder à ce tableau de bord de nœud à l'avenir. Cochez la case pour réclamer le nœud de votre réseau.  Cliquez sur le lien "Obtenez-le ici" et trouvez votre clé API. Copiez-le. Revenez en arrière et collez-le. Cliquez sur "Enregistrer et continuer".  #### Redirection de port : Nous ne pouvons pas décrire comment transférer le port pour le matériel spécifique de chacun. Voici quelques ressources pour apprendre à transférer des ports. - [PortForward.com](https://portforward.com/) - [Mysterium - Redirection de port](https://docs.mysterium.network/troubleshooting/port-forwarding)   ### Redémarrage automatique des conteneurs Docker au démarrage :  ### Configurations facultatives : - [Mises à jour et montées automatiques d'Ubuntu] (https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/) - [Blocage du trafic ToR sur Ubuntu] (https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver) #### Augmentez la sécurité en bloquant les logiciels malveillants et les trackers. Forcez toutes les requêtes DNS aux logiciels malveillants Cloudflares et au DNS de protection de suivi. Bloquez également les requêtes DNS/HTTPS. * Si vous avez un routeur ou un pare-feu plus avancé sur le réseau, vous pouvez même utiliser des packages comme snort/securita pour créer des règles plus avancées pour bloquer les adresses IP, l'accès tor, les torrents, le trafic p2p en général, etc. recommandé mais pas obligatoire.* Pour un blocage ToR plus avancé, vous pouvez procéder comme suit :  ## Profit?