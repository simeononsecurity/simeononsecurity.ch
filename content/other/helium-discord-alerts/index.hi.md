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
 ** एचडीएस की स्थापना - ज्ञात कलह स्थिति उपकरण ** *हीलियम स्थिति और पुरस्कार सूचनाएँ आपके डिस्कॉर्ड चैनल को देखी गईं*  Hotspot Discord Status (HDS) टूल से हीलियम ऐक्सिबिलिटी और अवार्ड सूचनाएँ सीधे अपने डिस्कॉर्ड चैनल पर प्राप्त करें। सब्सक्राइब के लिए कार्य लिंक ज्ञान, एक कारक वीपीएस या विशेषता विशिष्टता और एक हीलियम माइनर की आवश्यकता है। लेख आवश्यक डिस्कॉर्ड वेबहूक बनाना, हीलियम में शामिल नाम और विवरण, ही आवश्यक आवेदन बनाने और क्रॉन जॉब सेट करने के बारे में चरण-दर-चरण निर्देश प्रदान करता है। लेख में यह सुनिश्चित करने के लिए एक परीक्षण भी शामिल है कि आपका सक्सेस ठीक से काम कर रहा है। एचडीएस के साथ प्रामाणिक समय में हीलियम ब्लॉकचैन पुरस्कार का ट्रैक प्राप्त करें।  ##जरूरी है: - सामान्य लिंक ज्ञान - एक फ्रेम वीपीएस या फिर - एक हीलियम माइनर - [एचडीएस सॉफ्टवेयर] की प्रति (https://github.com/co8/hds)  ## एक लिंक की स्थापना: मैं यह सुनिश्चित कर रहा हूं कि आपके पास कुछ लिंक खर्च हो रहे हैं और जानते हैं कि वीपीएस या लिंक को कैसे स्थापित किया जाए। यदि आपको कुछ सहायता की आवश्यकता है, तो कम से कम $5/माह में एक ubuntu VPS बनाने के लिए निम्नलिखित रूपरेखा का विश्लेषण करें:  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup -साथ-उबंटू-20-04)  ## मर्माहत कलह स्थिति उपकरण की स्थापना: ### आवश्यक कलह वेबहुक बनाना:  - [डिसॉर्ड - वेबहुक का परिचय](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)  ### जरूरी हीलियम कनेक्शन से नाम और पता लगाना:  - [हॉटस्पॉटी](https://app.hotspotty.net/workspace/hotspots)  - [हीलियम जिक्र](https://explorer.helium.com/)  ### आवश्यक रिकॉर्ड बनाना: - यह आपके एचडीएस परिनियोजन को निर्धारित करने के लिए आवश्यक है और इसे स्थापित किया जाएगा। अंत में यह ``config.json``` फ़ाइल खोलेगा जिसमें आपका डिस्कॉर्ड वेबहुक url और आपके अन्य प्रवेश को पत्र बनाना होगा। पूर्व।:  - अब हमें एक रिकॉर्ड बनाने की जरूरत है ### क्रॉन जॉब की स्थापना: -निम्न चालें: ``क्रोंटैब -ए``` - निम्नलिखित को अपनी crontab फाइल में पेस्ट करें:  ### यह देखने के लिए परीक्षण करें कि आपका दृश्य काम कर रहा है या नहीं: