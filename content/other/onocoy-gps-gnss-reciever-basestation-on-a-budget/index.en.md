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

### Enhancing Your GNSS and RTK Setup

**Onocoy** offers a fresh perspective on **GNSS stations**. Beyond pinpoint accuracy, it's about becoming part of a **global network** that benefits users worldwide. Discover the key considerations for setting up your station: from selecting the right equipment to optimizing antenna placement and ensuring reliable internet connectivity.

{{< figure src="onocoy-rtk.webp" alt="Onocoy RTK" link="https://docs.onocoy.com/documentation/fundamentals/what-is-rtk" >}}

### Contribution and Rewards

At its heart, **Onocoy** not only improves accuracy but also recognizes your contributions. Uncover how your role in enabling specific **NTRIP messages** and maintaining **low latency** translates into **tangible rewards**. **Onocoy's approach** ensures a fair distribution of rewards through **blockchain technology**, providing **transparency** in recognition.

{{< figure src="onocoy-rewards.jpg" alt="Onocoy Reward calculation" link="https://docs.onocoy.com/documentation/topics/reward-calculation" >}}

______

## Understanding Onocoy's GNSS Capabilities and Requirements.

Exploring the GNSS capabilities of **Onocoy** sheds light on the diverse channels and bands it supports. As a rule of thumb, a broader range of **bands and constellations** translates to enhanced rewards within the network. For an in-depth understanding, refer to the insights shared in **section 4.2.1** of the whitepaper, which is accessible on **LinkedIn** [here](https://www.linkedin.com/posts/onocoy_onocoys-whitepaper-activity-7100819491936169985-EZmo?utm_source=share&utm_medium=member_desktop) and soon on the official website.

**Update rates**, a crucial factor, cater differently to miners and **RTK Rovers**, who are the data consumers utilizing the Onocoy service. Miners find stability with a rate of **1Hz**, ensuring steady data contribution. In contrast, higher update rates like 10Hz, 20Hz, or even 100Hz predominantly serve RTK Rovers' needs for real-time precision.

Addressing the notion of **minimum required position accuracy**, Onocoy adopts a pragmatic approach. Straying from stringent demands, the system's meticulous processing accurately determines device positions during validation steps, ensuring reliability without undue accuracy expectations.

**Signal-to-Noise Ratio (SNR)** and **signal levels** emerge as pivotal factors. **SNR above 40 dBHz**, preferably reaching around 45 dBHz, signifies optimal performance. Lower SNR values, stemming from factors like extended cables or antenna quality, can elevate code/carrier noise, potentially affecting measurement quality. Two fundamental principles guide this aspect:

- Ensuring an unobstructed **360-degree sky view** for the antenna, ensuring unhindered signal access.
- Aiming for a **secure and stable antenna mount** to counteract vibrations and instability.

This comprehensive approach forms the bedrock of reliable and robust data contribution to the Onocoy network.

____

## Why DIY a Onocoy Reference Station?

Creating your own **DIY Onocoy reference station** offers several compelling advantages. Firstly, it provides a **cost-effective solution**, enabling you to save on setup expenses while achieving **high precision** in *location-based applications*. Secondly, the customization options allow you to tailor the **hardware and software** to your specific needs, enhancing **flexibility and adaptability**. Moreover, **DIY setup empowers you** with a deeper understanding of the technology, enabling you to **troubleshoot and innovate**. Lastly, contributing to the **Onocoy network** not only improves your own accuracy but also lets you play a vital role in advancing **global navigation systems** while **earning rewards** for your data contributions.

______
{{< inarticle-dark >}}
______


## Hardware Requirements:
One of the following is **required**. We basically just need any **efficient and low powered computer** we can get our hands on that also runs Linux. Any **Raspberry PI**, **Intel NUC**, or similar will do. They don't have to be all that powerful. However, we will recommend you have at least **32g-64g of flash-based storage** (for longevity of the SSD). For this, we will be targeting a **budget of around $50-$200** for compute hardware, but feel free to go higher if it suits your needs. Our **power target** is approximately **10w average**. 
### Raspberry Pi and Pi Clones:
Hard to get ahold of these days but they are super low power and are quite customizable. For info on how to install raspian on your Raspberry PI 
- [Orange Pi 5 4GB](https://amzn.to/45IW4ZD)
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

### Compute Notable Mentions
Older Raspberry Pi models (1, 2, 3) should be sufficient. But newer models should be significantly more efficient and allow you do run multiple [low powered mining setups](https://simeononsecurity.ch/other/creating-profitable-low-powered-crypto-miners/) on a single device. This is why we recommend newer compute hardware.


## Recommended GPS Receivers for DIY Onocoy Deployments
You should ideally chose a receiver in your budget that is capable of using an external antenna. One that is capable of getting an unobstructed 360 degree view of the sky. But additionally at a bare minimum it must support [RTCM (Radio Technical Commission for Maritime Services)](https://en.wikipedia.org/wiki/RTCM_SC-104).

- [NEO-M8P RTK GPS GNSS receiver board with SMA and mini USB for UAV, Robots](https://gnss.store/neo-m8p-gnss-modules/90-elt0078.html) - $150
  - Single-Band (L1 only), 72 Channels, supports USB; I2C; and UART, Accurate within 6 feet, 10hz pull rate. Rewards will be limited, 8% only.
  - Shows up as `/dev/ttyACM0` instead of `/dev/ttyUSB0` in the instructions below. Same goes for all U-BLOX based devices.

- (**Prefered**)[NEO-F9P-15B Multi-band](https://gnss.store/gnss-gps-modules/194-elt0164.html) - $220
  - Single-Band (L1 only), 92 Channels, supports USB; I2C; and UART, Accurate within 6 feet, 50hz pull rate. Rewards will be limited, 8-10% only.

- (**Prefered**)[SparkFun GPS-RTK Board - NEO-M8P-2 (Qwiic)](https://www.sparkfun.com/products/15005) - $179.95
  - NEO-M8P-2 Based, Single-Band (L1 only), 6 Foot Accuracy. Rewards will be limited, 8-10% only.

- (**Prefered**)[SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://www.sparkfun.com/products/16481) - $274.95
  - ZED-F9P Based, Dual-Band L1+L2 (or L1+L5), 184 Channels, 20hz pull rate, USB Only. Rewards are limited, 30% of possibly maximum rewards.

- [ZED-F9P RTK GNSS receiver board with SMA Base or Rover](https://gnss.store/zed-f9p-gnss-modules/99-13-elt0087.html#/27-add_antenna-without_antenna) - $210
  - ZED-F9P Based, Dual-Band L1+L2 (or L1+L5), 184 Channels, 20hz pull rate, USB Only. Rewards are limited, 30% of possibly maximum rewards.

### Advanced Receivers for DIY Onocoy Deployments
These are all going to be devices that are Triple-Band, High Pull Rate, Extreme Position Receivers. They won't support USB. They will require PCI-E, UART, I2C, or Serial Connections. 
If you don't know what that is or you aren't experienced, please use the options above. However these will allow you to be capable of at least 80% of Onocoy Rewards in the case of the [Unicorecomm UM980](https://en.unicorecomm.com/products/detail/26) based boards and 100% of rewards in the [Septentrio Mosaic X5](https://www.septentrio.com/en/products/gps/gnss-receiver-modules/mosaic-x5) based boards. While you'll be able to use the same software we mention below, the instructions we've provided won't exactly line up. Be advised.

- (**Prefered**)[UM980 module](https://www.aliexpress.us/item/3256805035445904.html) + [DSD TECH SH-U05A USB to I2C](https://amzn.to/3OPABrj) + [I2C Qwiic Cable Kit](https://amzn.to/44szcg9)- $180
  - Unicorecomm UM980 Based, Triple Band L1, L2 and L5. 

- [MobileCM Triple-Band MiniPCIe Card](https://hyfix.ai/products/mobilecm-triple-band-minipcie-upgrade-card) - $295
  - Unicorecomm UM980 Based, Triple Band L1, L2 and L5.

- [mosaic-go GNSS module receiver evaluation kit](https://shop.septentrio.com/en/shop/mosaic-go-gnss-module-receiver-evaluation-kit) - $645
  - Septentrio Mosaic X5 Based, 50-100hz Pull Rate, Anti-Interference, Anti-Jamming, Anti-Spoofing.

- [simpleRTK3B mPCIe](https://www.ardusimple.com/product/simplertk3b-mpcie-septentrio-mosaic/)
  - Septentrio Mosaic X5 Based, 50-100hz Pull Rate, Anti-Interference, Anti-Jamming, Anti-Spoofing.

## Recommended Antennas for Onocoy
### Basic Antennas for Onocoy
We can only recommend using these on the [RCmall forM8N USB GPS Module](https://amzn.to/3sspf53) and [NEO-M8N GPS GNSS receiver board with SMA and mini USB for UAV, Robots](https://gnss.store/neo-m8n-gnss-modules/44-elt0031.html) receivers we recommended earlier.
- [Bingfu GPS Navigation Antenna ](https://amzn.to/3qM9N36) - $9
  - Basic, simple, not the best, but it works.
- (**Prefered**)[Bingfu GPS Navigation External Antenna](https://amzn.to/3PcSGki) - $24
  - Outdoor Rated, Cheap, Allows view of the Sky.
- [SparkFun GNSS-RTK Accessory Kit](https://amzn.to/3ORbgxc) - $85
  - This is only recommended for those who can not properly install the antennas below. It will underperform against the others. 

### Advanced Antennas for Onocoy
For all other recommended Receivers above we recommend the antennas below. 
- (**Prefered**)[Beitian High Gain High Precision GPS/GNSS Antenna](https://amzn.to/47MWdxa) - $86
  - High Antenna Gain, High Precision, Builtin Anti-interference, IP67 Rated, High and Low Temp Ratings, UV Resistant Housing.
- [Multi-frequency High Precision Survey Antenna](https://hyfix.ai/products/multi-frequency-high-precision-survey-antenna) - $95
  - Strong Antenna Signal, High Precision, Builtin Anti-interference.
- [GNSS Surveying Antenna and Precise Navigation Antenna](https://amzn.to/47Mj4ZH) - $180
  - High Antenna Gain, Extremely High Precision, IP67 Rated.
  
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
{{< inarticle-dark >}}
______

## Setting up the ntrip server software
Once you've set up your device and [properly placed your antenna](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/2.-install-your-station), you can start configuring the required software. 

*For this section we assume some basic technical experience and that you have installed your operating system already as well as know how to get into the terminal.*

1. We need to create an account and get our credentials from the [onocoy website](https://console.onocoy.com/explorer). You will need to grab the server address, username, password, and port number from this step. Once it is completed, go to the reference station tab and grab the mount point, which we also need.
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
    Ex. `Bus 00x Device 00x: ID xxxx:xxxx Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P` or `Bus xxx Device xxx: ID xxxx:xxxx U-Blox AG [u-blox 8]`

    Note: Some devices may show up as `ttyUSB0`, `ttyACM0`, etc. You'll have to look this up per your device.
`
    ```bash
    ls /dev/ttyUSB*
    ```

    ```bash
    sudo minicom -D /dev/ttyUSB0
    ```

4. Now we get to configure the software
   1. Test the configuration.

      ```bash
          `~/ntripserver/ntripserver -M 1 -i /dev/ttyUSB0 -b 19200 -O 1 -a servers.onocoy.com -p 2101 -m {{mountpointhere}} -n {{usernamehere}} -c {{passwordhere}}'
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
        ExecStart=/path/to/ntripserver -M 1 -i /dev/ttyUSB0 -b 19200 -O 1 -a servers.onocoy.com -p 2101 -m {{mountpointhere}} -n {{usernamehere}} -c {{passwordhere}}
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

## Troubleshooting and Verifying GPS Connectivity
1. Stop the ntripserver service
  ```bash
    sudo systemctl stop ntripserver.service
  ```
2. Use a GPS tool to verify connectivity
   1. First, make sure you have gpsd installed:
      ```bash
      sudo apt-get install gpsd
      ```
   2. Then start gpsd to connect to your GPS device:
      ```bash
      sudo gpsd /dev/ttyACM0 -F /var/run/gpsd.sock
      gpsmon
      ```
3. When finished either reboot your device or run
  ```bash
  sudo systemctl start ntripserver.service
  ```

## Notible Mentions for Alternative Ntrip Server Software.
While reviewing this topic and discussing with the Onocoy team on their discord, I came across the following. These may work better for you but we didn't cover them here. We may review them another time.
- [Ntrip Server](https://software.rtcm-ntrip.org/browser/ntrip/trunk/ntripserver)
  - Seems to be a newer version of the software we used above. However it's more difficult to access. It is created and maintained by the German Federal Agency for [Cartography and Geodesy (BKG)](https://www.bkg.bund.de/EN/Home/home.html)
- [RTKLIB](https://github.com/rtklibexplorer/RTKLIB/releases)
  -  A more widely used Ntrip server. However is significantly more technically involved.
- [esp32-xbee](https://github.com/nebkat/esp32-xbee)
  -  Exclusive to the ESP32, this software enables you to build even cheaper base stations. Or more expensive... 

## Conclusion

Setting up your **own DIY GPS Onocoy server** doesn't have to be a daunting task. With the **right hardware choices**, **reliable GPS receivers**, and a clear understanding of the process, you can achieve **remarkable precision and accuracy** in your *location-based applications*.

By following the **step-by-step instructions** outlined in this guide, you've unlocked the potential to **enhance your navigation, positioning, and surveying** endeavors. The **affordable hardware options**, such as *Raspberry Pi* and *Intel NUC*, coupled with **accurate GPS receivers**, pave the way for **effortless and efficient server setup**.

So, **go ahead and set up your Onocoy Reference Station**, refine your skills, and enjoy the **results** that await you. Whether you're **navigating remote terrains**, conducting **surveys**, or exploring new possibilities, your **DIY Onocoy Reference Station** will be your **trusty companion** in the pursuit of **precision**.

Stay inspired, stay innovative, and keep pushing the **boundaries of what's possible with technology**.

Lastly, check out our article on more [low powered mining setups](https://simeononsecurity.ch/other/creating-profitable-low-powered-crypto-miners/).