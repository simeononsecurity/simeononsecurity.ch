---
title: "Setting up HDS: Helium Hotspot Activity and Reward Notifications on Discord"
draft: false
toc: true
date: 2022-02-27
description: "Learn how to set up HDS, a tool that sends Helium hotspot activity and reward notifications to your Discord channel, with this step-by-step guide."
tags: ['Helium Miner Discord Notifications', 'Discord', 'Discord Notifications', 'Helium Notifications', 'Helium Miner', 'HNT', 'Helium Blockchain', 'Virtual Private Server', 'Cron', 'Cron Jobs']
cover: "/img/cover/A_3D_animated_art_style_image_of_a_computer_screen_display.png"
coverAlt: "A 3D animated art style image of a computer screen displaying a Helium hotspot dashboard with notifications popping up on the screen. The image is surrounded by icons representing Linux, Ubuntu, VPS, VM, and Git. "
coverCaption: ""
---
```bash
sudo apt install git python python3-pip -y
git clone https://github.com/co8/hds
cd ~/hds
cp new-config.json config.json
cp new-activity_history.json activity_history.json
nano config.json
```
```json
{
  "hotspot": "112MWdscG3DjHTxdCrtuLk...",
  "discord_webhook": "https://discord.com/api/webhooks/87869..."
}
```
```bash
#cd ~/hds
#pip install -r requirements.txt
python -m pip install discord-webhook
```
```
*/5 * * * * cd ~/hds; python3 hds.py >> cron.log 2>&1
20 4 * * 0 cd ~/hds; rm cron.log; echo "cron.log cleared (weekly)" >> cron.log 2>&1
```
```
cd ~/hds
python3 hds.py
```
 **Configuration de HDS - Outil d'état de la discorde du point d'accès** * Notifications d'activité et de récompense Helium Hotspot envoyées à votre canal Discord *  Recevez les notifications d'activité et de récompense sur les hotspots Helium directement sur votre canal Discord avec l'outil Hotspot Discord Status (HDS). La configuration nécessite des connaissances de base sur Linux, un VPS Ubuntu ou une machine virtuelle Ubuntu et un mineur d'hélium. L'article fournit des instructions étape par étape sur la façon de créer le webhook Discord requis, de trouver le nom et l'adresse du point d'accès Helium, d'installer le logiciel requis et de configurer une tâche cron. L'article comprend également un test pour s'assurer que votre configuration fonctionne correctement. Gardez une trace de vos récompenses blockchain Helium en temps réel avec HDS.  ## Requis : - Connaissance générale de Linux - Un VPS Ubuntu ou une VM Ubuntu - Un mineur d'hélium - Copie du [logiciel HDS] (https://github.com/co8/hds)  ## Configurer une VM Linux : Je vais supposer que vous avez des compétences de base en Linux et que vous savez comment configurer un VPS ou une machine virtuelle Linux. Si vous avez besoin d'aide, consultez les ressources suivantes pour créer un VPS Ubuntu pour aussi peu que 5 $/mois :  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup -avec-ubuntu-20-04)  ## Configuration de l'outil Hotspot Discord Status : ### Création du Webhook Discord requis :  - [Discord - Introduction aux Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)  ### Recherche du nom et de l'adresse du point d'accès Hélium requis :  - [Point d'accès] (https://app.hotspotty.net/workspace/hotspots)  - [Explorateur d'hélium](https://explorer.helium.com/)  ### Installation du logiciel requis : - Cela installera le logiciel et les fichiers requis pour configurer votre déployeur HDS. Enfin, il ouvrira le fichier ```config.json``` dans lequel vous devrez coller votre URL de webhook Discord et votre adresse de point d'accès. ex.:  - Maintenant, nous devons installer une dépendance ### Configuration de la tâche Cron : - Exécutez ce qui suit : ```crontab -e``` - Collez ce qui suit dans votre fichier crontab :  ### Testez pour voir si votre configuration fonctionne :