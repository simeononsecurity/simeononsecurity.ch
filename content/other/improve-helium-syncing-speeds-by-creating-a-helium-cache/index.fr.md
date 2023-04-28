---
title: "Enhancing Helium Syncing Speeds with a Blockchain Cache"
draft: false
toc: true
date: 2022-02-19
description: "Learn how to install a Helium Miner Docker container on a VPS or Linux virtual machine for faster syncing speeds."
tags: ['Resolve Helium Miner Syncing Problems', 'Helium Mining', 'Helium Network Token (HNT)', 'Solve Synchronization Problems', 'Blockchain Technology for Helium', 'Docker Container', 'Docker Watchtower Monitoring', 'Virtual Private Server (VPS)', 'Automated Task Scheduler (Cron)', 'Automated Tasks with Cron Jobs']
cover: "/img/cover/A_cartoon_or_3d_animated_image_of_a_computer_with_a_chain.png"
coverAlt: "A cartoon or 3d animated image of a computer with a chain symbolizing the blockchain, connected to multiple other computer symbols representing the peers in the network, all connected to a central hub symbolizing the centralized cache setup."
coverCaption: ""
---
```bash
#Install Docker
#https://docs.docker.com/engine/install/ubuntu/
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

#Install the helium docker container
sudo mkdir /root/miner_data
docker run -d --env REGION_OVERRIDE=US915 --restart always --publish 1680:1680/udp --publish 44158:44158/tcp --name miner --mount type=bind,source=/root/miner_data,target=/var/data quay.io/team-helium/miner:latest-amd64

#Set the miner to auto restart when the host restarts
sudo docker update --restart unless-stopped $(docker ps | grep miner | awk '{print $1}')

#Install Watchtower for auto docker container updates
#https://github.com/containrrr/watchtower
docker run --detach --name watchtower --volume /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower
```
```bash
docker exec miner miner peer connect /ip4/xxx.xxx.xxx.xxx/tcp/44158 

docker exec miner miner peer sync /ip4/xxx.xxx.xxx.xxx/tcp/44158

docker exec miner miner peer fastforward /ip4/xxx.xxx.xxx.xxx/tcp/44158

docker exec miner miner peer book -s

docker exec miner miner repair sync_state
docker exec miner miner info p2p_status
docker exec miner miner info height
docker exec miner miner versions
docker exec miner miner info summary
```
```bash
chmod +x ~/miner_sync.sh
~/miner_sync.sh
```
```bash
crontab -e
```
```*/30 * * * * ~/miner_sync.sh >> ~/synclog.txt```
Save the file and exit.

Now the script will run every thirty minutes and sync from and to each of your miners.

### Profit?

 **Améliorez les vitesses de synchronisation d'hélium en accordant un cache de chaîne de blocs d'hélium**  Aujourd'hui, nous allons vous montrer comment installer le conteneur officiel Helium Miner Docker sur une machine virtuelle VPS ou Linux. Cette approche offre l'avantage d'avoir une copie centralisée et sécurisée de la blockchain Helium, sous notre contrôle. En mettant en œuvre cette configuration, nous améliorerons également les vitesses de synchronisation en permettant à plusieurs appareils de télécharger les données de la blockchain. Cette solution est hautement évolutive et peut accueillir plusieurs mineurs, simplement en dupliquant le script cron décrit ci-dessous.   ## Requis : - Connaissance générale de Linux - Un mineur d'hélium à port redirigé et non relayé - Une VM VPS ou Linux  ## Configurer une VM Linux : Je vais supposer que vous avez des compétences de base en Linux et que vous savez comment configurer un VPS ou une machine virtuelle Linux. Si vous avez besoin d'aide, consultez les ressources suivantes pour créer un VPS Ubuntu pour aussi peu que 5 $/mois :  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup -avec-ubuntu-20-04)  ## Mise en place du "Cache" de la Blockchain Helium : ### Installation du logiciel requis : ***Remarque :*** Partout où vous voyez "xxx.xxx.xxx.xxx", remplacez-le par l'adresse IPv4 publique de votre mineur d'hélium. Exécutez les commandes suivantes pour installer docker et installez le docker, le conteneur docker hélium et la tour de guet pour les mises à jour automatiques : ### Création du script de synchronisation : Maintenant que nous avons la configuration du conteneur Docker du mineur, nous devons configurer la synchronisation vers et depuis vos mineurs d'hélium. Modifiez ce script avec les adresses IPv4 publiques de vos mineurs d'hélium : puis lancez ```nano ./miner_sync.sh``` collez votre script modifié et appuyez sur ```ctrl+x``` et ```y``` pour enregistrer.  ### Test du script :  ### Configuration de la tâche Cron : Nous devons maintenant configurer une tâche cron pour l'exécuter toutes les 30 minutes au moins. Combien de temps dépend de vous, mais utilisez [crontab guru](https://crontab.guru/) pour comprendre la syntaxe cron afin de modifier l'intervalle si vous le souhaitez.  Exécutez la commande suivante : Sélectionnez l'éditeur de votre choix, puis collez ce qui convient comme dernière ligne du script.