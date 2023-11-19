---
title: "Unlock Precision: Build Your DIY RTKDirect Reference Station Today!"
date: 2023-12-31
toc: true
draft: false
description: "Explore DIY RTKDirect setup for enhanced GPS precision. Save costs, customize, and join a global network. Ready to revolutionize your navigation?"
genre: ["Technology", "DIY", "Navigation", "GPS", "Precision", "Geolocation", "Blockchain", "Networking", "Innovation", "Global Connectivity"]
tags: ["DIY technology", "GPS precision", "RTKDirect setup", "Global navigation", "Cost-effective solutions", "Customization", "Blockchain rewards", "Geolocation networks", "Innovative GNSS", "Networking guide", "Location-based applications", "Navigation systems", "RTK Rovers", "GNSS capabilities", "Data contributions", "Internet connectivity", "Signal-to-Noise Ratio", "Precision surveys", "DIY innovation", "Location accuracy", "GNSS correction data", "Satellite navigation", "RTKDirect rewards", "3D animated setup", "Global technology community", "Navigation advancements", "DIY enthusiasts", "Location-based rewards", "Navigation solutions"]
cover: "/img/cover/diy_rtkdirect_setup.png"
coverAlt: "A symbolic representation of a DIY RTKDirect setup, showcasing precise satellite navigation."
coverCaption: "Precision Unleashed: Your DIY RTKDirect Journey Begins Now!"
ref: ["/other/triple-mining-geodnet-onocoy-rtkdirect-gps-revolution", "/other/onocoy-gps-gnss-reciever-basestation-on-a-budget", "/other/diy-rtkdirect-reference-station-guide", "/other/creating-profitable-low-powered-crypto-miners"]
---

**RTKDirect DIY Reference Station Setup Guide**

In this comprehensive guide, we'll take you through the process of establishing your own GPS RTKDirect server using cost-effective hardware options and reliable GPS receivers. Whether you're interested in elevating the precision of your location-based applications, conducting accurate surveys, or delving into the world of **DIY technology**, this guide provides step-by-step instructions to assist you in creating your DIY RTKDirect reference station.

> **Note:** This article does not contain financial advice nor does it condone any endorsement of the RTKDirect project.

______

## What is RTKDirect?: Advancing GNSS Correction Data

**RTKDirect** is an innovative platform that utilizes GNSS devices and correction data to build a decentralized network for precise positioning and navigation. It provides users with the opportunity to contribute to this network while earning rewards based on their data contributions. 

  {{< figure src="rtkdirectwebsite.webp" alt="RTKDirect Website" link="https://rtkdirect.com/" >}}

______

## Enhancing Your GNSS and RTK Setup

RTKDirect offers a fresh perspective on GNSS stations. Beyond achieving pinpoint accuracy, it's about becoming part of a global network that benefits users worldwide. Discover the key considerations for setting up your station: from selecting the right equipment to optimizing antenna placement and ensuring reliable internet connectivity.

### Key Considerations for Setup

When setting up your RTKDirect station, consider the following:

- **Cost-Effective Hardware:** Choose hardware options that are both effective and budget-friendly.
- **Optimized Antenna Placement:** Ensure your antenna is placed optimally for reliable signals.
- **Internet Connectivity:** Establish a robust internet connection for seamless data contributions.

______

## RTKDirect Contribution and Rewards

At its core, RTKDirect not only improves accuracy but also acknowledges your contributions. Learn how your role in enabling specific RTCM3 messages and maintaining low latency translates into tangible rewards. RTKDirect's approach ensures a fair distribution of rewards through blockchain technology, providing transparency in recognition.

### RTKDirect Reward Calculation

### Understanding RTKDirect’s GNSS Capabilities and Requirements

Exploring the GNSS capabilities of RTKDirect sheds light on the diverse channels and bands it supports. A broader range of bands and constellations translates to enhanced rewards within the network. For an in-depth understanding, refer to the insights shared in their [official website](https://rtkdirect.com/).

Update rates, a crucial factor, cater differently to miners and RTK Rovers, who are the data consumers utilizing the RTKDirect service. Miners find stability with a rate of 1Hz, ensuring steady data contribution. In contrast, higher update rates like 10Hz, 20Hz, or even 100Hz predominantly serve RTK Rovers’ needs for real-time precision.

Addressing the notion of minimum required position accuracy, RTKDirect adopts a pragmatic approach. Straying from stringent demands, the system’s meticulous processing accurately determines device positions during validation steps, ensuring reliability without undue accuracy expectations.

#### Signal-to-Noise Ratio (SNR) and Signal Levels

{{< figure src="installedantenna.png" caption="Installed Antenna - doc.onocoy.com" alt="An Installed Tri-Band GPS Antenna" link="https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/2.-install-your-station" >}}

Signal-to-Noise Ratio (SNR) and signal levels emerge as pivotal factors. SNR above 40 dBHz, preferably reaching around 45 dBHz, signifies optimal performance. Lower SNR values, stemming from factors like extended cables or antenna quality, can elevate code/carrier noise, potentially affecting measurement quality. Two fundamental principles guide this aspect:

- Ensuring an unobstructed 360-degree sky view for the antenna, ensuring unhindered signal access.
- Aiming for a secure and stable antenna mount to counteract vibrations and instability.

This comprehensive approach forms the bedrock of reliable and robust data contribution to the RTKDirect network.

______

## Why DIY an RTKDirect Reference Station?

Creating your own DIY RTKDirect reference station offers several compelling advantages. Firstly, it provides a **cost-effective solution**, enabling you to save on setup expenses while achieving high precision in location-based applications. Secondly, the customization options allow you to tailor the hardware and software to your specific needs, enhancing flexibility and adaptability. Moreover, DIY setup empowers you with a deeper understanding of the technology, enabling you to troubleshoot and innovate. Lastly, contributing to the RTKDirect network not only improves your own accuracy but also lets you play a vital role in advancing global navigation systems while earning rewards for your data contributions.

______


## Hardware Requirements:
One of the following is **required**. We basically just need any **efficient and low powered computer** we can get our hands on that also runs Linux. Any **Raspberry PI**, **Intel NUC**, or similar will do. They don't have to be all that powerful. However, we will recommend you have at least **32g-64g of flash-based storage** (for longevity of the SSD). For this, we will be targeting a **budget of around $50-$200** for compute hardware, but feel free to go higher if it suits your needs. Our **power target** is approximately **10w average**. 

{{< figure src="compute.jpeg" alt="RTKDirect DIY Compute for Receivers" link="https://amzn.to/45IW4ZD" >}}

### Raspberry Pi and Pi Clones:
Hard to get ahold of these days but they are super low power and are quite customizable. For info on how to install raspian on your Raspberry PI 
- [Orange Pi 5 4GB](https://amzn.to/45IW4ZD)
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)

### Any Mini PC with Intel N5100 or similar
For super low power Raspberry Pi equivalent but on x64 platform. 
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

### Ultra Low Power / Low Budget
If you're interested in a lower power and/or low budget setup, read our guide on [How to Set Up a GPS/GNSS Bases Station on an ESP32](https://simeononsecurity.com/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980/).

### Compute Notable Mentions
Older Raspberry Pi models (1, 2, 3) should be sufficient. But newer models should be significantly more efficient and allow you do run multiple [low powered mining setups](https://simeononsecurity.com/other/creating-profitable-low-powered-crypto-miners/) on a single device. This is why we recommend newer compute hardware.

## Recommended GPS Receivers DIY RTKDirect Deployments
There are many receivers on the market but at a bare minimum it must support [**RTCM (Radio Technical Commission for Maritime Services)**](https://en.wikipedia.org/wiki/RTCM_SC-104) and ideally have the ability to be hooked up to an antenna outside of the install location with 360 degree unobstructed view of the sky.

These are all going to be devices that are Triple-Band, High Pull Rate, Extreme Position Receivers. Most won't support USB. They will require PCI-E, UART, I2C, or Serial Connections. THey will allow you to be capable of at most of the RTKDirect rewards. While you'll be able to use the same software we mention below, the instructions we've provided may not exactly line up. Be advised that things like COM ports and the dongle specific instructions may be different for you.

{{< figure src="advanced-receivers.jpeg" alt="The Best GPS Receivers for RTKDirect" >}}

- **Unicorecomm UM980/UM982 Based USB Receivers**
The preferred option overall and by far for almost every setup.
Requires [FTDI Drivers](https://ftdichip.com/drivers/vcp-drivers/).
  - (**Preferred**)[UM980 RTK GNSS USB Dongle](https://gnss.store/unicore-gnss-modules/247-elt0222.html) - $225
    - Unicorecomm UM980 Based, Triple Band L1, L2 and L5, All-Constellation, High Precision, 1408 Channels, 20hz pull rate, 80% Rewards.
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.
  - (**Preferred**)[UM982 Dual Channel RTK GNSS USB Dongle](https://gnss.store/um982-gnss-modules/239-elt0212.html) - $235
    - Unicorecomm UM982 Based, Triple Band L1, L2 and L5, All-Constellation, High Precision, 1408 Channels, 20hz pull rate, 80% Rewards.
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.

  - [UM980 module](https://www.aliexpress.us/item/3256805035445904.html) + [DSD TECH SH-U05A USB to I2C](https://amzn.to/3tptGOk) + [GH1.25 to Dupont2.54 Pre-Crimped Cables](https://amzn.to/3tptGOk)- $180 - $220
    - Unicorecomm UM980 Based, Triple Band L1, L2 and L5.
    - For more details on how to install this, we recommend you read this article on [how to set up the I2C connection on the UM980](https://wholovesburrito.com/2023/09/25/an-affordable-diy-gnss-station-for-onocoy/)
  - [UM980 M.2](https://gnss.store/unicore-gnss-modules/250-elt0225.html)
    - Unicorecomm UM980 Based, Triple Band L1, L2 and L5. 
    - May not be recognized by all systems, it uses USB protocols over M.2
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.
  - [UM980 mPCIe](https://gnss.store/unicore-gnss-modules/251-elt0226.html)
    - Unicorecomm UM980 Based, Triple Band L1, L2 and L5. 
    - May not be recognized by all systems, it uses USB protocols over mPCIe
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.

- **Unicorecomm UM982**
  - [UM982 M.2](https://gnss.store/um982-gnss-modules/242-elt0215.html)
    - Unicorecomm UM982 Based, Triple Band L1, L2 and L5. 
    - May not be recognized by all systems, it uses USB protocols over M.2
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.
  - [UM982 mPICe](https://gnss.store/um982-gnss-modules/243-elt0216.html)
    - Unicorecomm UM982 Based, Triple Band L1, L2 and L5. 
    - May not be recognized by all systems, it uses USB protocols over mPCIe
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.

- **Septentrio Mosaic X5**
Capable of up to 100% of the Onocoy rewards. Requires already available [firmware update](https://www.septentrio.com/en/products/gps/gnss-receiver-modules/mosaic-x5).
  - [mosaic-go GNSS module receiver evaluation kit](https://shop.septentrio.com/en/shop/mosaic-go-gnss-module-receiver-evaluation-kit) - $645
    - Septentrio Mosaic X5 Based, 50-100hz Pull Rate, Anti-Interference, Anti-Jamming, Anti-Spoofing.
  - (**Preferred**)[simpleRTK3B mPCIe](https://www.ardusimple.com/product/simplertk3b-mpcie-septentrio-mosaic/)
    - Septentrio Mosaic X5 Based, 50-100hz Pull Rate, Anti-Interference, Anti-Jamming, Anti-Spoofing.

## Recommended Antennas for RTKDirect

We've covered this in a more in depth guide about the [Best GPS Base Station Antennas](https://simeononsecurity.com/other/unveiling-best-gps-antennas-onocoy-geodnet/).

{{< figure src="surveying-antenna.jpeg" alt="Ardusimple and GNSS.STORE Surveying Antennas" link="https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html" >}}

- (**Preferred**)[Calibrated Survey GNSS Tripleband + L-band antenna (IP67)](https://www.ardusimple.com/product/calibrated-survey-gnss-quadband-antenna-ip67/) - $230
  - Calibrated Quad-Band, Extremely High Precision, Anti-interference, Supports All Bands
- [Multi-frequency High Precision Survey Antenna](https://hyfix.ai/products/multi-frequency-high-precision-survey-antenna) - $95
  - Strong Antenna Signal, High Precision, Builtin Anti-interference.
- [HARXON CSX627A](https://www.gns-electronics.de/product/harxon-csx627a/) - $135
  - Calibrated Triple Band RTK Antenna, IP67, Supports All Bands
- [L1/L2/L5 GPS, G1/G2/G3 GLONASS, B1/B2/B3 BDS, Galileo E1/E5/E6 38dB Antenna](https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html) - $205
  - Supports Most Bands, IP67 Rated
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

## RTK Direct Setup Instructions

### Linux


#### 1. Install RTKBase

```bash
cd ~
wget https://raw.githubusercontent.com/Stefal/rtkbase/master/tools/install.sh -O install.sh
chmod +x install.sh
sudo ./install.sh --all release #must not be run as root
#RTKbase comes with a web element that doesn't work for our purposes.
sudo systemctl disable rtkbase_web 
sudo systemctl stop rtkbase_web
```

#### Set up STR2STR

1. **Set up USB to local TCP server**
  > **Note:** When setting up USB to a local TCP server using the `str2str` command, ensure you specify your serial settings correctly. In the provided example:

  ```bash
  str2str -in serial://ttyUSB0:921600:8:n:1#rtcm3 -out tcpsvr://:5015 -b 1 -t 0
  ```
   - **ttyUSB0**: Specifies the USB port. Adjust this based on your system configuration.
   - **921600**: Represents the baud rate. Modify this value if your device requires a different baud rate.
   - **8**: Indicates the data bits.
   - **n**: Represents no parity.
   - **1**: Indicates one stop bit.

  Make sure to customize these settings according to your specific hardware and communication requirements.


2. **Set Up TCP Forwarding to RTKDirect**

  You'll need the IP and portnumber from the [RTKDirect Console](https://cloud.rtkdirect.com/hotspots)

  ```bash
  str2str -in tcpcli://localhost:5015#rtcm3 -msg "1006(10), 1033(10), 1077, 1087, 1097, 1117, 1127, 1137, 1230" -out tcpcli://ntrip.rtkdirect.com:portnumber#rtcm3 -msg "1006(10), 1033(10), 1077, 1087, 1097, 1117, 1127, 1137, 1230" -p lat long elevation(m) -i "RTKBase UM980,2.4.2 " -a "GNSS.STORE ELT0123" -t 0
  ```

   **Notes**: 

     - Be sure to replace the message numbers if you know you don't use [MSMv7 RTCM3 messages](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/). Otherwise, don't touch them.
  
     - Be sure to replace the values for -p, -i, and -a with your, geo cords, receiver model and your antenna if applicable. If you don't know them, obmit this information from the command.
  
     - Under `-out` be sure to specify the port number the dashboard gives you.

1. **Set Up RTKDirect STR2STR SYSTMCTL Service**

  To make sure that it starts up on boot, we need to create a service.


  Using the commands we created earlier, you're going to create two services. Use the commands and template below to do that.

  ```bash
  sudo nano /etc/systemd/system/rtkdirect-str2str1.service
  ```

  ```toml

  [Unit]
  Description=STR2STR Service for RTKDirect 1
  After=network.target
  Wants=network-online.target
  After=network-online.target

  [Service]
  ExecStart=str2str -in serial://ttyUSB0:921600:8:n:1#rtcm3 -out tcpsvr://:5015 -b 1 -t 0
  Restart=always
  RestartSec=30
  StartLimitBurst=10
  StartLimitInterval=5min
  TimeoutStartSec=600
  User=root

  [Install]
  WantedBy=default.target
  ```

  ```bash
  sudo nano /etc/systemd/system/rtkdirect-str2str2.service
  ```
  ```toml

  [Unit]
  Description=STR2STR Service for RTKDirect 2
  After=network.target
  Wants=network-online.target
  After=network-online.target

  [Service]
  ExecStart=str2str -in tcpcli://localhost:5015#rtcm3 -msg "1006(10), 1033(10), 1077, 1087, 1097, 1117, 1127, 1137, 1230" -out tcpcli://ntrip.rtkdirect.com:portnumber#rtcm3 -msg "1006(10), 1033(10), 1077, 1087, 1097, 1117, 1127, 1137, 1230" -p lat long elevation(m) -i "RTKBase UM980,2.4.2 " -a "GNSS.STORE ELT0123" -t 0
  Restart=always
  RestartSec=30
  StartLimitBurst=10
  StartLimitInterval=5min
  TimeoutStartSec=600
  User=root

  [Install]
  WantedBy=default.target
  ```

  Enable and start the services.

  ```bash
  sudo systemctl daemon-reload
  sudo systemctl enable rtkdirect-str2str1 rtkdirect-str2str2
  sudo systemctl start rtkdirect-str2str1 rtkdirect-str2str2
  ```

### Windows

Please see the [Windows instructions for Onocoy instructions](https://simeononsecurity.com/other/onocoy-gps-gnss-reciever-basestation-on-a-budget/#windows-option-1-strsvr), they will be pretty much the exact same.

### Verification:

The RTKDirect Dashboard has a few minutes of delay. For best results, you should wait 5-30 minutes before checking to see if it populates in the [RTKDirect Dashboard](https://cloud.rtkdirect.com/hotspots).

  {{< figure src="rtkdirectconsole.webp" alt="RTKDirect Dashboard" link="https://cloud.rtkdirect.com/hotspots" >}}

______

## Conclusion

In conclusion, establishing your DIY RTKDirect reference station opens up a world of possibilities for precise positioning and navigation. The benefits include cost-effectiveness, customization, and active participation in a global network. By following the steps outlined in this guide, you can contribute to the advancement of GNSS technology while reaping the rewards of your data contributions.

______

## References

1. [RTKDirect Official Website](https://rtkdirect.com/)
2. [RTKDirect About Page](https://rtkdirect.com/the-team/)