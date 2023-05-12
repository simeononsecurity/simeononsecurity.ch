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

 **Verbessern Sie die Synchronisierungsgeschwindigkeit von Helium, indem Sie einen Helium-Blockchain-Cache erstellen**  Heute zeigen wir Ihnen, wie Sie den offiziellen Helium Miner Docker-Container auf einer virtuellen VPS- oder Linux-Maschine installieren. Dieser Ansatz bietet den Vorteil, dass wir eine zentralisierte und sichere Kopie der Helium-Blockchain unter unserer Kontrolle haben. Durch die Implementierung dieses Setups verbessern wir auch die Synchronisierungsgeschwindigkeit, indem mehrere Geräte Blockchain-Daten herunterladen. Diese Lösung ist hochgradig skalierbar und kann mehrere Miner aufnehmen, ohne dass einfach das unten beschriebene Cron-Skript dupliziert wird.   ## Erforderlich: - Allgemeine Linux-Kenntnisse - Ein Port-weitergeleiteter und nicht-weitergeleiteter Helium-Miner - Ein VPS oder eine Linux-VM  ## Einrichten einer Linux-VM: Ich gehe davon aus, dass Sie über einige klassische Linux-Kenntnisse verfügen und wissen, wie man einen VPS oder eine Linux-VM einrichtet. Wenn Sie Hilfe benötigen, sehen Sie sich sterbende Ressourcen an, um einen Ubuntu-VPS für nur 5 $/Monat zu erstellen:  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup -mit-ubuntu-20-04)  ## Helium-Blockchain "Cache" einrichten: ### Installieren der erforderlichen Software: ***Hinweis:*** Überall dort, wo SIE "xxx.xxx.xxx.xxx" sehen, ersetzen SIE es durch die öffentliche IPv4-Adresse Ihres Helium-Miners. Führen SIE die folgenden Befehle aus, um Docker zu installieren und Docker, den Helium-Docker-Container und Watchtower für automatische Updates zu installieren: ### Erstellen des Synchronisierungsskripts: Jetzt haben wir das Miner-Docker-Container-Setup, wir müssen die Synchronisierung zu und von Ihren Helium-Minern einrichten. Ändern Sie dieses Skript mit den öffentlichen IPv4-Adressen Ihres Helium-Miner: Führen Sie dann ```nano ./miner_sync.sh``` aus, fügen Sie Ihr modifiziertes Skript ein und drücken Sie zum Speichern ```ctrl+x``` und ```y```.  ### Testen des Skripts:  ### Einrichtung des Cron-Jobs: Jetzt müssen wir einen Cron-Job einrichten, um diesen mindestens alle 30 Minuten auszuführen. Wie lange bleibt Ihnen überlassen, aber verwenden Sie [crontab guru](https://crontab.guru/), um die Cron-Syntax herauszufinden, um das Intervall zu ändern, wenn Sie möchten.  Führen SIE den folgenden Befehl aus: Wählen Sie den Editor Ihrer Wahl aus und fügen Sie dann Folgendes als letzte Zeile des Skripts ein.