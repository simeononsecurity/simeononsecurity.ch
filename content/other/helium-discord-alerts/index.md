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

**Setting up HDS - Hotspot Discord Status tool**
*Helium Hotspot Activity and Reward Notifications sent to your Discord Channel*

Get Helium hotspot activity and reward notifications sent directly to your Discord channel with the Hotspot Discord Status (HDS) tool. The setup requires basic Linux knowledge, an Ubuntu VPS or Ubuntu VM, and a Helium Miner. The article provides step-by-step instructions on how to create the required Discord webhook, find the Helium hotspot name and address, install the required software, and set up a cron job. The article also includes a test to ensure your configuration is working properly. Keep track of your Helium blockchain rewards in real-time with HDS.

## Required:
- General Linux Knowledge
- A Ubuntu VPS or Ubuntu VM
- A Helium Miner
- Copy of the [HDS Software](https://github.com/co8/hds)

## Setting up a Linux VM:
I'm going to assume that you have some basic linux skills and know how to set up a VPS or linux vm. 
If you need some help, check out the following resources to create a ubuntu VPS for as little as $5/month:
 - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)
 - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)

## Setting up the Hotspot Discord Status tool:
### Creating the Required Discord Webhook:
 - [Discord - Intro to Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

### Finding the required Helium Hotspot name and Address:
 - [Hotspotty](https://app.hotspotty.net/workspace/hotspots)
 - [Helium Explorer](https://explorer.helium.com/)

### Installing the Required Software:
- This will install the required software and files to set up your HDS deployment. Lastly it will open the ```config.json``` file that you'll need to paste your discord webhook url and your hotspot address in.
```bash
sudo apt install git python python3-pip -y
git clone https://github.com/co8/hds
cd ~/hds
cp new-config.json config.json
cp new-activity_history.json activity_history.json
nano config.json
```
ex.:
```json
{
  "hotspot": "112MWdscG3DjHTxdCrtuLk...",
  "discord_webhook": "https://discord.com/api/webhooks/87869..."
}
```

- Now we need to install one dependency
```bash
#cd ~/hds
#pip install -r requirements.txt
python -m pip install discord-webhook
```
### Setting up the Cron Job:
- Run the following: ```crontab -e```
- Paste the following into your crontab file:
```
*/5 * * * * cd ~/hds; python3 hds.py >> cron.log 2>&1
20 4 * * 0 cd ~/hds; rm cron.log; echo "cron.log cleared (weekly)" >> cron.log 2>&1
```

### Test to see if your configuration is working:
```
cd ~/hds
python3 hds.py
```