---
title: "DIY Onocoy Ntrip Server and Reference Station Setup"
date: 2023-11-18
toc: true
draft: false
description: "Discover how to effortlessly set up a DIY GPS Onocoy Reference Station for precise location accuracy. Learn step-by-step with affordable hardware options and reliable receivers."
genre: ["Technology", "DIY", "GPS", "Hardware", "Location Accuracy", "Server Setup", "Precision", "Guides", "Tutorials", "Tech Solutions", "Onocoy", "Geodnet", "Reference Station", "ntrip", "GNSS", "GPS"]
tags: ["Onocoy", "Geodnet", "Reference Station", "ntrip", "GNSS", "GPS", "DIY GPS", "GPS Correction", "Location Accuracy", "Server Setup", "Precision Guides", "Tutorials", "Affordable Hardware", "Reliable Receivers", "Effortless Solutions", "Technology", "DIY Projects", "GPS Receivers", "Low-Power Computing", "Linux", "Raspberry Pi", "Intel NUC", "Budget Hardware", "Accuracy Enhancement", "Navigation", "Positioning", "DIY Technology", "GPS Correction Data", "Accurate Location", "Efficient Hardware", "GPS Accuracy", "NTRIP Server", "GNSS Receivers", "Low Power Consumption", "DIY Server Setup", "Enhance Precision", "Location-Based Applications"]
cover: "/img/cover/gps-satellite-setup.png"
coverAlt: "A symbolic image showcasing a GPS satellite in orbit."
coverCaption: "Unlock Ultimate Precision with DIY Onocoy Servers."
---
**DIY Onocoy Reference Station Setup Guide**

In this guide, we'll **walk you through the process** of **setting up your own GPS Onocoy server** using *cost-effective hardware options* and *reliable GPS receivers*. Whether you're interested in **enhancing the accuracy** of your *location-based applications*, conducting **precision surveys**, or simply **exploring the world of DIY technology**, this guide provides **step-by-step instructions** to help you get started with creating your DIY Onocoy reference station. 

______

## What is Onocoy?: Advancing GNSS Correction Data

**Onocoy** is an innovative platform that harnesses **GNSS devices** and **correction data** to create a **decentralized network** for precise positioning and navigation. It offers users the opportunity to contribute to this network while **earning rewards** based on their data contributions.

{{< youtube id="pzeMUD7EFTA" >}}

### Enhancing Your GNSS Setup

**Onocoy** offers a fresh perspective on **GNSS stations**. Beyond pinpoint accuracy, it's about becoming part of a **global network** that benefits users worldwide. Discover the key considerations for setting up your station: from selecting the right equipment to optimizing antenna placement and ensuring reliable internet connectivity.

### Contribution and Rewards

At its heart, **Onocoy** not only improves accuracy but also recognizes your contributions. Uncover how your role in enabling specific **NTRIP messages** and maintaining **low latency** translates into **tangible rewards**. **Onocoy's approach** ensures a fair distribution of rewards through **blockchain technology**, providing **transparency** in recognition.

______

## Hardware Requirements:
One of the following is **required**. We basically just need any **efficient and low powered computer** we can get our hands on that also runs Linux. Any **Raspberry PI**, **Intel NUC**, or similar will do. They don't have to be all that powerful. However, we will recommend you have at least **32g-64g of storage**, **4g of RAM**, and at least **2 CPU threads**. For this, we will be targeting a **budget of around $50-$200** for compute hardware, but feel free to go higher if it suits your needs. Our **power target** is approximately **10w average**.

### Raspberry Pi:
Hard to get ahold of these days but they are super low power and are quite customizable. For info on how to install raspian on your Raspberry PI 
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Any USFF/Tiny/Mini/Micro PC:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Any Mini PC with Intel N5100 or similar
For super low power Raspberry Pi equivalent but on x64 platform. 
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Recommended GPS Receivers for DIY Onocoy Deployments
You should ideally chose a receiver in your budget that is capable of using an external antenna. One that is capable of getting an unobstructed 360 degree view of the sky. 

- [RCmall forM8N USB GPS Module](https://amzn.to/3sspf53) - $22
  - Cheap and tested by many on other projects, however accuracy and channel support are both limited. Rewards are limited. 

- [GlobalSat BU-353-S4 USB GPS Receiver](https://amzn.to/3YY7bMo) - $60
  -  Cheap, offers external antenna support,  however accuracy and channel support are both extremely limited. Rewards are limited. 

- [NEO-M8N GPS GNSS receiver board with SMA and mini USB for UAV, Robots](https://gnss.store/neo-m8n-gnss-modules/44-elt0031.html) - $70
  - 72 Channels, supports USB; I2C; and UART, Accurate within 6 feet, 10hz pull rate. Rewards will be limited, but should perform quite well given the cost.

- [NEO-F9P-15B Multi-band L1,L5 RTK GNSS USB Dongle with SMA antenna connector](https://gnss.store/gnss-gps-modules/222-elt0185.html) - $220
  - 184 Channels, 20hz pull rate, USB Only. We believe this will be your **best choice**. Rewards shouldn't be limited.

## Recommended Antennas for Onocoy

- [GNSS Surveying Antenna and Precise Navigation Antenna](https://amzn.to/47Mj4ZH)
- [Beitian High Gain High Precision GNSS Antenna](https://amzn.to/47MWdxa)

______

## OS Installation:
We won't go into the technical details of how to install an operating system here. However here are some great resources to get you started.
### Raspbian:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)

______

## Setting up the ntrip server software
Once you've set up your device and [properly placed your antenna](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/2.-install-your-station), you can start configuring the required software. 

*For this section we assume some basic technical experience and that you have installed your operating system already as well as know how to get into the terminal.*

1. We need to create an account and get our credentials from the [onocoy website](https://console.onocoy.com/explorer). You will need to grab the server address, username, password, and port number from this step. 
   Refer to the [Onocoy documentation](https://docs.onocoy.com/documentation/quick-start-guides/get-gnss-correction-data) if you need help.

2. On your linux device download the [ntripserver](https://github.com/nunojpg/ntripserver) software.
    ```bash
    git clone https://github.com/nunojpg/ntripserver.git
    cd ./ntripserver
    make
    ```
3. Identify the USB Source

    ```bash
    lsusb
    ```
    Ex. `Bus 00x Device 00x: ID xxxx:xxxx Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P`
    ```bash
    ls /dev/ttyUSB*
    ```

    ```bash
    sudo minicom -D /dev/ttyUSB0
    ```

4. Now we get to configure the software
   1. Test the configuration.

      ```bash
          `~/ntripserver/ntripserver -M 1 -i /dev/ttyUSB0 -b 19200 -O 1 -a servers.onocoy.com -p 2101 -m Mount1 -n {{usernamehere}} -c {{passwordhere}}'
      ```

   2. Now that you confirmed it works. We need to create a service to have it restart on boot.
      1. **Create a Service File**:
        ```bash
        sudo nano /etc/systemd/system/ntripserver.service
        ``` 
        Remember to replace `/path/to/ntripserver` with the actual path to your ntripserver executable.
        ```bash
        [Unit]
        Description=NTRIP Server Service
        After=network.target

        [Service]
        ExecStart=/path/to/ntripserver -M 1 -i /dev/ttyUSB0 -b 19200 -O 1 -a servers.onocoy.com -p 2101 -m Mount1 -n {{usernamehere}} -c {{passwordhere}}
        Restart=always
        User=root

        [Install]
        WantedBy=default.target
        ```
      2. **Enable and Start the Service**:
        ```bash
        sudo systemctl enable ntripserver.service
        sudo systemctl start ntripserver.service
        ```
      3. **Check the Service Status**:
        ```bash
        sudo systemctl status ntripserver.service
        ```
        ex.
        ```bash
        ntripserver[815]: serial input: device = /dev/ttyUSB0, speed = 19200
        systemd[1]: Started NTRIP Server Service.
        ntripserver[815]: caster output: host = xxx.xxx.xxx.xxx, port = 2101, mountpoint = Mount1, mode = http
        ntripserver[815]: transfering data ...
        ```
5. Wait and Verify Your Station on the Onocoy Dashboard
   1.  Visit the [Onocoy Console Dashboard](https://console.onocoy.com/servers) and check to see your device has finished it's validation period. If it hasn't check back later, it can take up to 3 days.

6. Profit?
   1. You can view the following [Onocoy documentation](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/4.-receive-rewards) to learn more.

## Notible Mentions for Alternative Ntrip Server Software.
While reviewing this topic and discussing with the Onocoy team on their discord, I came across the following. These may work better for you but we didn't cover them here. We may review them another time.
- [Ntrip Server](https://software.rtcm-ntrip.org/browser/ntrip/trunk/ntripserver)
  - Seems to be a newer version of the software we used above. However it's more difficult to access. It is created and maintained by the German Federal Agency for [Cartography and Geodesy (BKG)](https://www.bkg.bund.de/EN/Home/home.html)
- [RTKLIB](https://www.rtklib.com/rtklib.htm)
  -  A more widely used Ntrip server. However is significantly more technically involved.
- [esp32-xbee](https://github.com/nebkat/esp32-xbee)
  -  Exclusive to the ESP32, this software enables you to build even cheaper base stations. Or more expensive... 

## Conclusion

Setting up your **own DIY GPS Onocoy server** doesn't have to be a daunting task. With the **right hardware choices**, **reliable GPS receivers**, and a clear understanding of the process, you can achieve **remarkable precision and accuracy** in your *location-based applications*.

By following the **step-by-step instructions** outlined in this guide, you've unlocked the potential to **enhance your navigation, positioning, and surveying** endeavors. The **affordable hardware options**, such as *Raspberry Pi* and *Intel NUC*, coupled with **accurate GPS receivers**, pave the way for **effortless and efficient server setup**.

So, **go ahead and set up your Onocoy Reference Station**, refine your skills, and enjoy the **results** that await you. Whether you're **navigating remote terrains**, conducting **surveys**, or exploring new possibilities, your **DIY Onocoy Reference Station** will be your **trusty companion** in the pursuit of **precision**.

Stay inspired, stay innovative, and keep pushing the **boundaries of what's possible with technology**.
