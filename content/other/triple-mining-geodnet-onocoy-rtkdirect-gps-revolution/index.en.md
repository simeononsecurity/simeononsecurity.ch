---
title: "Triple Mining GPS Revolution: Geodnet, Onocoy, and RTKDirect Unleashed!"
date: 2024-01-01
toc: true
draft: false
description: "Embark on a GPS revolution! Discover DIY triple mining with Geodnet, Onocoy, and RTKDirect for enhanced precision. Join a global network and save costs. Explore the future of navigation now!"
genre: ["Technology", "DIY", "Navigation", "GPS", "Precision", "Geolocation", "Blockchain", "Networking", "Innovation", "Global Connectivity"]
tags: ["Triple mining", "Geodnet", "Onocoy", "RTKDirect", "DIY technology", "GPS precision", "Navigation solutions", "Cost-effective setups", "Customization", "Blockchain rewards", "Geolocation networks", "Innovative GNSS", "Networking guide", "Location-based applications", "RTK Rovers", "GNSS capabilities", "Data contributions", "Internet connectivity", "Signal-to-Noise Ratio", "Precision surveys", "DIY innovation", "Location accuracy", "GNSS correction data", "Satellite navigation", "Global technology community", "Navigation advancements", "DIY enthusiasts", "Location-based rewards"]
cover: "/img/cover/triple_mining_geodnet_onocoy_rtkdirect.png"
coverAlt: "A symbolic representation of triple mining with Geodnet, Onocoy, and RTKDirect, revolutionizing GPS precision."
coverCaption: "Triple Mining GPS Revolution: Unleash Precision with Geodnet, Onocoy, RTKDirect!"
ref: ["/other/triple-mining-geodnet-onocoy-rtkdirect-gps-revolution", "/other/onocoy-gps-gnss-reciever-basestation-on-a-budget", "/other/diy-rtkdirect-reference-station-guide", "/other/creating-profitable-low-powered-crypto-miners","/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980", "/other/onocoy-supported-rtcm-messages"]
---

## Introduction

Welcome to the forefront of GPS precision – a realm where innovation meets DIY enthusiasm. In this comprehensive guide, we'll delve into the exciting realm of triple mining, bringing together the powerful forces of Geodnet, Onocoy, and RTKDirect. Join us on a journey where technology meets customization, and global navigation takes a leap forward. Whether you're a DIY enthusiast or a tech-savvy navigator, this guide is your gateway to revolutionizing your GPS experience.

______

## Hardware Requirements:

For this project we need a few things.

1. [Geodnet Miner](https://hyfix.ai/products/mobilecm-triple-band-gnss-base-station)
2. Any [system running linux](https://amzn.to/45IW4ZD)
3. A [UM980](https://gnss.store/unicore-gnss-modules/247-elt0222.html) or [Mosaic-X5](https://shop.septentrio.com/en/shop/mosaic-go-gnss-module-receiver-evaluation-kit) Based GPS Receiver
4. A [GPS Antenna](https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html) (You can use the one that came with your geodnet device)
5. A really good [Power Blocking Antenna Splitter](https://www.gns-electronics.de/product/11359)

{{< figure src="compute.jpeg" alt="RTKDirect DIY Compute for Receivers" link="https://amzn.to/45IW4ZD" >}}

{{< centerbutton href="https://amzn.to/45IW4ZD" >}}Get the Orange Pi 5 Today!{{< /centerbutton >}}


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

{{< centerbutton href="https://simeononsecurity.com/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980/" >}}How to Set Up a GPS/GNSS Bases Station on an ESP32{{< /centerbutton >}}


### Compute Notable Mentions
Older Raspberry Pi models (1, 2, 3) should be sufficient. But newer models should be significantly more efficient and allow you do run multiple [low powered mining setups](https://simeononsecurity.com/other/creating-profitable-low-powered-crypto-miners/) on a single device. This is why we recommend newer compute hardware.

## Recommended GPS Receivers DIY RTKDirect Deployments
There are many receivers on the market but at a bare minimum it must support [**RTCM (Radio Technical Commission for Maritime Services)**](https://en.wikipedia.org/wiki/RTCM_SC-104) and ideally have the ability to be hooked up to an antenna outside of the install location with 360 degree unobstructed view of the sky.

These are all going to be devices that are Triple-Band, High Pull Rate, Extreme Position Receivers. Most won't support USB. They will require PCI-E, UART, I2C, or Serial Connections. THey will allow you to be capable of at most of the RTKDirect rewards. While you'll be able to use the same software we mention below, the instructions we've provided may not exactly line up. Be advised that things like COM ports and the dongle specific instructions may be different for you.

{{< figure src="advanced-receivers.jpeg" alt="The Best GPS Receivers" >}}

{{< centerbutton href="https://gnss.store/unicore-gnss-modules/247-elt0222.html" >}}Get your GNSS.STORE UM980 RTK GNSS USB Dongle Today!{{< /centerbutton >}}

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

## Recommended Antennas

We've covered this in a more in depth guide about the [Best GPS Base Station Antennas](https://simeononsecurity.com/other/unveiling-best-gps-antennas-onocoy-geodnet/).

{{< figure src="surveying-antenna.jpeg" alt="Ardusimple and GNSS.STORE Surveying Antennas" link="https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html" >}}

{{< centerbutton href="https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html" >}}Get the GNSS.STORE Triple Band Survey Antenna Today!{{< /centerbutton >}}

- (**Preferred**)[Calibrated Survey GNSS Tripleband + L-band antenna (IP67)](https://www.ardusimple.com/product/calibrated-survey-gnss-quadband-antenna-ip67/) - $230
  - Calibrated Quad-Band, Extremely High Precision, Anti-interference, Supports All Bands
- [Multi-frequency High Precision Survey Antenna](https://hyfix.ai/products/multi-frequency-high-precision-survey-antenna) - $95
  - Strong Antenna Signal, High Precision, Builtin Anti-interference.
- [HARXON CSX627A](https://www.gns-electronics.de/product/harxon-csx627a/) - $135
  - Calibrated Triple Band RTK Antenna, IP67, Supports All Bands
- [L1/L2/L5 GPS, G1/G2/G3 GLONASS, B1/B2/B3 BDS, Galileo E1/E5/E6 38dB Antenna](https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html) - $205
  - Supports Most Bands, IP67 Rated

## Recommended Antenna Splitters

When choosing antenna splitters for your setup, it's crucial to avoid options that may harm your radios, such as the one linked [here](https://amzn.to/3QryASQ). This type of splitter can potentially damage your equipment.

Instead, consider opting for antenna splitters that intelligently split the signal without affecting the DC power. 

{{< centerbutton href="https://www.gns-electronics.de/product/11359" >}}Get your GPS Antenna Splitter Today!{{< /centerbutton >}}

Here are two recommended options:

- [GNS Electronics Antenna Signal Splitter](https://www.gns-electronics.de/product/11359)
- [ArduSimple GPS/GNSS Antenna Signal Splitter](https://www.ardusimple.com/product/gps-gnss-antenna-signal-splitter/)

These alternatives provide a reliable solution for signal splitting without the risk of damaging your equipment.



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

## Triple Mining Setup Instructions

### Wiring

You'll take the [Power Blocking GPS Splitter](https://www.gns-electronics.de/product/11359) and split your [antenna](https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html) connection going between the [Geodnet MobileCM Miner](https://hyfix.ai/products/mobilecm-triple-band-gnss-base-station) and whatever [GPS Receiver](https://gnss.store/unicore-gnss-modules/247-elt0222.html) you have connected to your [Linux system](https://amzn.to/45IW4ZD).

`Geodnet MobileCM Miner` <-----> `Power Blocking GPS Splitter` <-----> `Antenna`


`Linux System` <---> `GPS Receiver` <-----> `Power Blocking GPS Splitter`

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
or if you're on Ubuntu specifically

```bash
sudo apt install -y rtklib
```

#### 2. Set up STR2STR

1. **Test Set up USB to local TCP server**
  > **Note:** When setting up USB to a local TCP server using the `str2str` command, ensure you specify your serial settings correctly. In the provided example:

  ```bash
  str2str -in serial://ttyUSB0:921600:8:n:1#rtcm3 -out tcpsvr://:5015 -b 1 -t 0
  ```
   - **ttyUSB0**: Specifies the USB port. Adjust this based on your system configuration.
   - **921600**: Represents the baud rate. Modify this value if your device requires a different baud rate. Another common baud rate for GPS receivers is `115200`.
   - **8**: Indicates the data bits.
   - **n**: Represents no parity.
   - **1**: Indicates one stop bit.

  Make sure to customize these settings according to your specific hardware and communication requirements.

  > *For those who aren't following my guide exactly and are using a standalone NTRIP device, like the NTRIP-X or Ardusimple Devices with the Wifi Master, or have followed our ESP32 guide, you'll end up doing something like the following `str2str -in ntrip://your-ntrip-source-here#rtcm3 -out tcpsvr://:5015#rtcm3`  in combination with a service like [Emlid Caster](https://emlid.com/ntrip-caster/). Play around with the `--help`. You goal should be to take NTRIP in and do local TCP out. Unfortunately the two software packages available for Linux don't let you take in NTRIP in as a caster directly, so we have to go through a middle man and access it as a NTRIP client.*


2. **Test Set Up TCP Forwarding to RTKDirect**

  You'll need the IP and portnumber from the [RTKDirect Console](https://cloud.rtkdirect.com/hotspots).

  ```bash
  str2str -in tcpcli://localhost:5015#rtcm3 -out tcpcli://ntrip.rtkdirect.com:portnumber#rtcm3 -msg -msg "1006(30), 1008(30), 1012(30), 1033(30), 1077, 1087, 1097, 1107, 1117, 1127, 1137, 1230" -p lat long elevation(m) -i "SimeonOnSecurity UM980 RTKLIB  DIY" -a "GEODNET ANTENNA" -t 0
  ```

   **Notes**: 

  - Be sure to replace the message numbers if you know you don't use [MSMv7 RTCM3 messages](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/). Otherwise, don't touch them.
  - Be sure to replace the values for -p, -i, and -a with your, geo cords, receiver model and your antenna if applicable. If you don't know them, omit this information from the command.
   - Elevation relative to sea level in meters. 
   - Use tools like [gps-coordinates.net](https://www.gps-coordinates.net/) to get your coordinates and [FreeMapTools](https://www.freemaptools.com/elevation-finder.htm) to get your elevation.
   - Under `-out` be sure to specify the port number the dashboard gives you.
     - The IP provided in the dashboard, at least for now, is the same as `ntrip.rtkdirect.com`. They point to the same space.

1. **Test Set Up NTRIPv1 for Onocoy**

  You'll need the Mountpoint Username and Password from the [Onocoy Console](https://console.onocoy.com/)

  ```bash
  str2str -in tcpcli://localhost:5015#rtcm3 -out ntrips://:password@servers.onocoy.com:2101/username#rtcm3 -msg "1006(30), 1033(30), 1077, 1087, 1097, 1117, 1127, 1137, 1230" -p lat long elevation(m) -i "SimeonOnSecurity UM980 RTKLIB DIY" -a "GEODNET ANTENNA" -t 0
  ```

  **Notes**: 
  
  - Be sure to replace the message numbers if you know you don't use [MSMv7 RTCM3 messages](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/). Otherwise, don't touch them.

  - Be sure to replace the values for -p, -i, and -a with your, geo cords, receiver model and your antenna if applicable. If you don't know them, omit this information from the command.
   - Elevation relative to sea level in meters. 
   - Use tools like [gps-coordinates.net](https://www.gps-coordinates.net/) to get your coordinates and [FreeMapTools](https://www.freemaptools.com/elevation-finder.htm) to get your elevation.
   - Under `-out` be sure to specify the password and username number the onocoy console gives you.

1. **Set Up STR2STR SYSTMCTL Services**

  To make sure that it starts up on boot, we need to create a service.


  Using the commands we created earlier, you're going to create two services. Use the commands and template below to do that.

  - **Set Up TCP Server Service**

      ```bash
      sudo nano /etc/systemd/system/rtkdirect-str2str1.service
      ```

      ```toml

      [Unit]
      Description=STR2STR Service 1
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
  - **Set Up RTK Direct TCP CLient Service**
      ```bash
      sudo nano /etc/systemd/system/rtkdirect-str2str2.service
      ```
      ```toml

      [Unit]
      Description=STR2STR Service 2
      After=network.target
      Wants=network-online.target
      After=network-online.target

      [Service]
      ExecStart=str2str -in tcpcli://localhost:5015#rtcm3 -out tcpcli://ntrip.rtkdirect.com:portnumber#rtcm3 -msg -msg "1006(30), 1008(30), 1012(30), 1033(30), 1077, 1087, 1097, 1107, 1117, 1127, 1137, 1230" -p lat long elevation(m) -i "SimeonOnSecurity UM980 RTKLIB  DIY" -a "GEODNET ANTENNA" -t 0
      Restart=always
      RestartSec=30
      StartLimitBurst=10
      StartLimitInterval=5min
      TimeoutStartSec=600
      User=root

      [Install]
      WantedBy=default.target
      ```
  - **Set Up Onocoy NTRIP v1 Service**
      ```bash
      sudo nano /etc/systemd/system/rtkdirect-str2str3.service
      ```
      ```toml

      [Unit]
      Description=STR2STR Service 3
      After=network.target
      Wants=network-online.target
      After=network-online.target

      [Service]
      ExecStart=str2str -in tcpcli://localhost:5015#rtcm3 -out ntrips://:password@servers.onocoy.com:2101/username#rtcm3 -msg "1006(30), 1033(30), 1077, 1087, 1097, 1107, 1117, 1127, 1137, 1230" -p lat long elevation(m) -i "RTKBase UM980,2.4.2" -a "GEODNET ANTENNA" -t 0
      Restart=always
      RestartSec=30
      StartLimitBurst=10
      StartLimitInterval=5min
      TimeoutStartSec=600
      User=root

      [Install]
      WantedBy=default.target
      ```

      **Enable and start the services.**

      ```bash
      sudo systemctl daemon-reload
      sudo systemctl enable rtkdirect-str2str1 rtkdirect-str2str2 rtkdirect-str2str3
      sudo systemctl start rtkdirect-str2str1 rtkdirect-str2str2 rtkdirect-str2str3
      ```

### Windows

Please see the [Windows instructions for Onocoy instructions](https://simeononsecurity.com/other/onocoy-gps-gnss-reciever-basestation-on-a-budget/#windows-option-1-strsvr), use `STR2SRV` to output to one **NTRIPServer for onocoy** and one **tcpclient for RTKDirect**.

______

## Conclusion

As we conclude our exploration into triple mining with Geodnet, Onocoy, and RTKDirect, envision a world where GPS precision is not just a necessity but a customizable, cost-effective, and rewarding adventure. The DIY spirit intertwines with cutting-edge technology, creating a tapestry of possibilities for navigation enthusiasts worldwide. The journey doesn't end here – it's an ongoing revolution. Unleash the potential of your GPS navigation, contribute to a global network, and embrace the future of geolocation. Precision awaits; your adventure begins now!

______

# References

- [RTKDirect Official Website](https://rtkdirect.com/)
- [RTKDirect About Page](https://rtkdirect.com/the-team/)
- [Onocoy - Get GNSS correction data](https://docs.onocoy.com/documentation/quick-start-guides/get-gnss-correction-data)
- [Onocoy - Connect your station to onocoy](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy)
- [RTKLIB.com](https://www.rtklib.com/)
- [str2str](https://github.com/tomojitakasu/RTKLIB/blob/master/app/str2str/str2str.c)