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
 **Einrichten von HDS – Hotspot Discord Status Tool** *An Ihren Discord-Kanal gesendete Helium-Hotspot-Aktivitäts- und Belohnungsbenachrichtigungen*  Erhalten Sie mit dem Hotspot Discord Status (HDS)-Tool Benachrichtigungen zu Helium-Hotspot-Aktivitäten und Belohnungen, die direkt an Ihren Discord-Kanal gesendet werden. Die Einrichtung erfordert grundlegende Linux-Kenntnisse, einen Ubuntu VPS oder eine Ubuntu VM und einen Helium Miner. Der Artikel Schritt-für-Schritt-Anleitungen, wie SIE den erforderlichen Discord-Webhook erstellen, den Namen und die Adresse des Helium-Hotspots finden, die erforderliche Software installieren und einen Cron-Job einrichten. Der Artikel enthält auch einen Test, um sicherzustellen, dass Ihre Konfiguration ordnungsgemäß funktioniert. Behalten Sie mit HDS den Überblick über Ihre Helium-Blockchain-Belohnungen in Echtzeit.  ## Erforderlich: - Allgemeine Linux-Kenntnisse - Ein Ubuntu-VPS oder eine Ubuntu-VM - Ein Heliumschürfer - Kopie der [HDS-Software] (https://github.com/co8/hds)  ## Einrichten einer Linux-VM: Ich gehe davon aus, dass Sie über einige klassische Linux-Kenntnisse verfügen und wissen, wie man einen VPS oder eine Linux-VM einrichtet. Wenn Sie Hilfe benötigen, sehen Sie sich sterbende Ressourcen an, um einen Ubuntu-VPS für nur 5 $/Monat zu erstellen:  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup -mit-ubuntu-20-04)  ## Einrichten des Hotspot-Discord-Status-Tools: ### Erstellen des erforderlichen Discord-Webhook:  - [Discord - Einführung in Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)  ### Ermitteln des Namens und der Adresse des erforderlichen Helium-Hotspots:  - [Hotspotty](https://app.hotspotty.net/workspace/hotspots)  - [Helium-Explorer](https://explorer.helium.com/)  ### Installieren der erforderlichen Software: - Dadurch werden die erforderliche Software und Dateien zum Einrichten Ihrer HDS-Bereitstellung installiert. Zuletzt wird die Datei „config.json“ geöffnet, in die SIE Ihre Discord-Webhook-URL und Ihre Hotspot-Adresse einfügen müssen. ex.:  - Jetzt müssen wir eine Abhängigkeit installieren ### Einrichtung des Cron-Jobs: - Führen Sie Folgendes aus: ```crontab -e``` - Fügen Sie Folgendes in Ihre Crontab-Datei ein:  ### Testen Sie, ob Ihre Konfiguration funktioniert: