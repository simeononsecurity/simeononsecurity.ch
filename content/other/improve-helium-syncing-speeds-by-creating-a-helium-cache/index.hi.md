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

 **हीलियम ब्लॉकचैन कैश रहने हीलियम डूबने की गति में सुधार करें**  आज, हम देखते हैं कि VPS या Linux सरफेसर आधिकारिक हीलियम माइनर डॉकटर कंटेनर को कैसे स्थापित किया जाए। यह दृष्टिकोण हमारे नियंत्रण में हीलियम ब्लॉकचैन की एक केंद्रीकृत और सुरक्षित प्रति होने का लाभ प्रदान करता है। इस संदेश को लागू करने से, हम कई डिवाइस ब्लॉकचैन डेटा डाउनलोड करके सिंकिंग स्पीड भी बढ़ा देते हैं। यह समाधान अत्यधिक स्केलेबल है और नीचे सिंक क्रॉन स्क्रिप्ट के अनुसार कई खनिकों को समायोजित किया जा सकता है।   ##जरूरी है: - सामान्य लिंक ज्ञान - एक पोर्टेड और रिलेटेड हीलियम माइनर - एक वीपीएस या लिंक्स विवि  ## एक लिंक की स्थापना: मैं यह सुनिश्चित कर रहा हूं कि आपके पास कुछ लिंक खर्च हो रहे हैं और जानते हैं कि वीपीएस या लिंक को कैसे स्थापित किया जाए। यदि आपको कुछ सहायता की आवश्यकता है, तो कम से कम $5/माह में एक ubuntu VPS बनाने के लिए निम्नलिखित रूपरेखा का विश्लेषण करें:  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup -साथ-उबंटू-20-04)  ## हीलियम ब्लॉकेन "कैश" की स्थापना: ### आवश्यक रिकॉर्ड बनाना: ***ध्यान दें:*** जहां भी आप "xxx.xxx.xxx.xxx" देखते हैं, उसे अपने हीलियम माइनर के सार्वजनिक लाभ से बढ़ाया जाता है। डॉकर को स्थापित करने और स्वचालित रूप से अपडेट करने के लिए डॉकर, हीलियम डॉकटर कंटेनर और वॉचटावर को स्थापित करने के लिए निम्न आदेश हैं: ### सिंकिंग स्क्रिप्ट बनाना: अब हमारे पास माइनर डॉकटर कंटेनर मैसेज है, हमें आपके हीलियम खनिकों से सिंकिंग सेट अप करने की आवश्यकता होगी। इस स्क्रिप्ट को अपने हीलियम खनिक सार्वजनिक IPv4 पाटन के साथ अनुमापी करें: फिर चलाएँ ``नैनो ./miner_sync.sh`` अपना अनुरुप स्क्रिप्ट पेस्ट करें और बनाने के लिए ```ctrl+x``` और ``y``` आकर्षित करें।  ### स्क्रिप्ट का परीक्षण:  ### क्रॉन जॉब की स्थापना: अब हमें कम से कम हर 30 मिनट में इसे चलाने के लिए क्रॉन जॉब सेट करने की आवश्यकता है। आप कितने समय पर स्थायी होते हैं, लेकिन यदि आप चमक को बदलने के लिए क्रॉन सिंटैक्स का पता लगाने के लिए [crontab guru](https://crontab.guru/) का उपयोग करें।  निम्नलिखित आदेश चलाएँ: अपनी पसंद के संपादक का चयन करें, फिर स्क्रिप्ट की अंतिम पंक्ति के रूप में पेस्ट करें।