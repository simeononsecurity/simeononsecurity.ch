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

> **Note:** This article does not contain financial advice nor does it consist of any endorsement of the RTKDirect project.

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

| Model                               | Description                                                    |
|--------------------------------------|----------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/45IW4ZD" >}}Orange Pi 5 4GB{{< /centerbutton >}}     | **Preferred Option:** If available, the Orange Pi 5 is recommended for its super low power and high customizability.    |
| {{< centerbutton href="https://amzn.to/3x72kv0" >}}Raspberry Pi 4B Model B DIY Kit{{< /centerbutton >}} | Consider this DIY kit for Raspberry Pi enthusiasts looking for a versatile and customizable computing solution.       |
| {{< centerbutton href="https://amzn.to/3jG2g2k" >}}GeeekPi Raspberry Pi 4 4GB Starter Kit{{< /centerbutton >}} | A ready-to-go starter kit for Raspberry Pi 4, suitable for those who prefer a convenient setup with moderate power.     |
| {{< centerbutton href="https://amzn.to/3DQisF6" >}}GeeekPi Raspberry Pi 4 8GB Starter Kit{{< /centerbutton >}} | Similar to the 4GB kit but with more RAM, ideal for users with higher performance requirements on the Raspberry Pi 4.    |
| {{< centerbutton href="https://amzn.to/3YkFhcj" >}}Beelink U59 Mini PC{{< /centerbutton >}}   | For those seeking a Raspberry Pi equivalent on an x64 platform, the Beelink U59 Mini PC offers a low-power alternative. |
| {{< centerbutton href="https://amzn.to/3XkbXkS" >}}TRIGKEY Mini Computer{{< /centerbutton >}} | Another option for an x64 platform, the TRIGKEY Mini Computer provides a compact and efficient computing solution.     |

## Recommended GPS Receivers DIY RTKDirect Deployments
There are many receivers on the market but at a bare minimum it must support [**RTCM (Radio Technical Commission for Maritime Services)**](https://en.wikipedia.org/wiki/RTCM_SC-104) and ideally have the ability to be hooked up to an antenna outside of the install location with 360 degree unobstructed view of the sky.

{{< figure src="advanced-receivers.jpeg" alt="The Best GPS Receivers for RTKDirect" >}}

| Model                                                | Description                                                                                                               |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://gnss.store/unicore-gnss-modules/247-elt0222.html" >}}UM980 RTK GNSS USB Dongle{{< /centerbutton >}}   | **Preferred Option:** Unicorecomm UM980 Based, Triple Band L1, L2, and L5, High Precision, 1408 Channels, 20Hz pull rate. Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount. |
| {{< centerbutton href="https://gnss.store/um982-gnss-modules/239-elt0212.html" >}}UM982 Dual Channel RTK GNSS USB Dongle{{< /centerbutton >}} | **Preferred Option:** Unicorecomm UM982 Based, Triple Band L1, L2, and L5, High Precision, 1408 Channels, 20Hz pull rate. Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount. |
| {{< centerbutton href="https://shop.septentrio.com/en/shop/mosaic-go-gnss-module-receiver-evaluation-kit" >}}mosaic-go GNSS module receiver evaluation kit{{< /centerbutton >}} | Septentrio Mosaic X5 Based, 50-100Hz Pull Rate, Anti-Interference, Anti-Jamming, Anti-Spoofing. Firmware update required.      |

## Recommended Antennas for RTKDirect

We've covered this in a more in depth guide about the [Best GPS Base Station Antennas](https://simeononsecurity.com/other/unveiling-best-gps-antennas-onocoy-geodnet/).

{{< figure src="surveying-antenna.jpeg" alt="Ardusimple and GNSS.STORE Surveying Antennas" link="https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html" >}}

| Model                                                                                                       | Description                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://www.ardusimple.com/product/calibrated-survey-gnss-quadband-antenna-ip67/" >}}Calibrated Survey GNSS Tripleband + L-band antenna (IP67){{< /centerbutton >}} | **Preferred Option:** Calibrated Quad-Band, Extremely High Precision, Anti-interference, Supports All Bands.                        |
| {{< centerbutton href="https://hyfix.ai/products/multi-frequency-high-precision-survey-antenna" >}}Multi-frequency High Precision Survey Antenna{{< /centerbutton >}}                 | Strong Antenna Signal, High Precision, Built-in Anti-interference.                                                                   |
| {{< centerbutton href="https://www.gns-electronics.de/product/harxon-csx627a/" >}}HARXON CSX627A{{< /centerbutton >}}                                            | Calibrated Triple Band RTK Antenna, IP67, Supports All Bands.                                                                       |
| {{< centerbutton href="https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html" >}}L1/L2/L5 GPS, G1/G2/G3 GLONASS, B1/B2/B3 BDS, Galileo E1/E5/E6 38dB Antenna{{< /centerbutton >}} | Supports Most Bands, IP67 Rated.                                                                                                  |
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

### Linux - Docker Container 

#### 1. Install Docker

Consult the following guides for more information on how to install docker

- https://www.digitalocean.com/community/tutorial-collections/how-to-install-and-use-docker
- https://docs.docker.com/engine/install/
- https://docs.docker.com/engine/install/ubuntu/

#### 2. Run the Docker Container

  Run our [Docker container](https://github.com/simeononsecurity/docker-rtklib-onocoy-rtkdirect), ensuring that you provide the necessary environment variables and parameters:

   ```bash
   docker run \
     -td \
     --restart unless-stopped \
     --name sosrtk \
     --device=/dev/<YOUR_USB_PORT> \
     -e USB_PORT=<YOUR_USB_PORT> \
     -e BAUD_RATE=<YOUR_SERIAL_BAUD_RATE> \
     -e DATA_BITS=<YOUR_SERIAL_DATA_BITS> \
     -e PARITY=<YOUR_SERIAL_PARITY> \
     -e STOP_BITS=<YOUR_SERIAL_STOP_BITS> \
     -e PORT_NUMBER=<YOUR_RTKLIB_PORT_NUMBER> \
     -e LAT=<OPTIONAL_YOUR_LATITUDE> \
     -e LONG=<OPTIONAL_YOUR_LONGITUDE> \
     -e ELEVATION=<OPTIONAL_YOUR_ELEVATION_FROM_SEA_LEVEL_IN_METERS> \
     -e INSTRUMENT=<OPTIONAL_YOUR_GPS_RECEIVER_DESCRIPTION> \
     -e ANTENNA=<OPTIONAL_YOUR_ANTENNA_DESCRIPTION> \
     simeononsecurity/docker-rtklib-onocoy-rtkdirect:latest
   ```

   Ensure you replace the placeholder values (`<...>`) with your specific configuration.

   Ex.
   ```bash
   docker run \
    -td \
    --restart unless-stopped \
    --name sosrtk \
    --device=/dev/ttyUSB0 \
    -e USB_PORT=ttyUSB0 \
    -e BAUD_RATE=921600 \
    -e DATA_BITS=8 \
    -e PARITY=n \
    -e STOP_BITS=1 \
    -e PORT_NUMBER=32377 \
    -e LAT=37.7749 \
    -e LONG=-122.4194 \
    -e ELEVATION=50 \
    -e INSTRUMENT="Your GPS Receiver" \
    -e ANTENNA="Your Antenna" \
    simeononsecurity/docker-rtklib-onocoy-rtkdirect:latest
   ```


### Linux - Manual Instructions

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
  str2str -in tcpcli://localhost:5015#rtcm3 -msg "1006(10), 1033(10), 1077, 1087, 1097, 1107, 1117, 1127, 1137, 1230" -out tcpcli://ntrip.rtkdirect.com:portnumber#rtcm3 -msg "1006(10), 1033(10), 1077, 1087, 1097, 1107,1117, 1127, 1137, 1230" -p lat long elevation(m) -i "RTKBase UM980,2.4.2 " -a "GNSS.STORE ELT0123" -t 0
  ```

   **Notes**: 

     - Be sure to replace the message numbers if you know you don't use [MSMv7 RTCM3 messages](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/). Otherwise, don't touch them.
  
  - Be sure to replace the values for -p, -i, and -a with your, geo cords, receiver model and your antenna if applicable. If you don't know them, omit this information from the command.
   - Elevation relative to sea level in meters. 
   - Use tools like [gps-coordinates.net](https://www.gps-coordinates.net/) to get your coordinates and [FreeMapTools](https://www.freemaptools.com/elevation-finder.htm) to get your elevation.
   - Under `-out` be sure to specify the port number the dashboard gives you.
     - The IP provided in the dashboard, at least for now, is the same as `ntrip.rtkdirect.com`. They point to the same space.

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
  ExecStart=str2str -in tcpcli://localhost:5015#rtcm3 -msg "1006(10), 1033(10), 1077, 1087, 1097, 1107,1117, 1127, 1137, 1230" -out tcpcli://ntrip.rtkdirect.com:portnumber#rtcm3 -msg "1006(10), 1033(10), 1077, 1087, 1097, 1107, 1117, 1127, 1137, 1230" -p lat long elevation(m) -i "RTKBase UM980,2.4.2 " -a "GNSS.STORE ELT0123" -t 0
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

{{< centerbutton href="https://simeononsecurity.com/other/triple-mining-geodnet-onocoy-rtkdirect-gps-revolution/" >}}Read our guide on Triple Mining Geodnet, Onocoy, and RTKDirect{{< /centerbutton >}}

______

## References

1. [RTKDirect Official Website](https://rtkdirect.com/)
2. [RTKDirect About Page](https://rtkdirect.com/the-team/)