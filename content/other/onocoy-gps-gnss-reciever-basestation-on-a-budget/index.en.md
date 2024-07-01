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
ref: ["/other/triple-mining-geodnet-onocoy-rtkdirect-gps-revolution", "/other/diy-rtkdirect-reference-station-guide", "/other/creating-profitable-low-powered-crypto-miners","/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980", "/other/onocoy-supported-rtcm-messages"]

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

## Ideal Setup Setup For Onocoy

For Onocoy, we recommend the following components for an optimal setup. This combination ensures high precision, versatility, and reliable performance.

| Name                                                                                          | Description                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3YkFhcj" >}}Beelink U59 Mini PC{{< /centerbutton >}}    | The Beelink U59 Mini PC offers a low-power alternative for those seeking a Raspberry Pi equivalent on an x64 platform. It provides a compact and efficient computing solution with the power of Intel N5100.                                                                                                                                                              |
| {{< centerbutton href="https://gnss.store/unicore-gnss-modules/247-elt0222.html" >}}UM980 RTK GNSS USB Dongle{{< /centerbutton >}} | Unicorecomm UM980 Based, Triple Band L1, L2, and L5, All-Constellation, High Precision, 1408 Channels, 20Hz pull rate, 80% Rewards. Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.                                                                                                                                               |
| {{< centerbutton href="https://www.gns-electronics.de/product/harxon-csx627a/" >}}HARXON CSX627A Antenna{{< /centerbutton >}}              | Calibrated Triple Band RTK Antenna, IP67, Supports All Bands                                                                                                                                                                                                                                                   |

This combination ensures a powerful computing platform with the Beelink U59 Mini PC, coupled with the high-precision positioning provided by the UM980 RTK GNSS USB Dongle and the reliable performance of the HARXON CSX627A Triple Band RTK Antenna. The recommended GNSS USB Dongle is our preferred choice for its exceptional precision and features, making it the ideal solution for Onocoy applications. 

*Below we've included other alternatives.*

## Recommended Hardware for Onocoy:
One of the following is **required**. We basically just need any **efficient and low powered computer** we can get our hands on that also runs Linux. Any **Raspberry PI**, **Intel NUC**, or similar will do. They don't have to be all that powerful. However, we will recommend you have at least **32g-64g of flash-based storage** (for longevity of the SSD). For this, we will be targeting a **budget of around $50-$200** for compute hardware, but feel free to go higher if it suits your needs. Our **power target** is approximately **10w average**. 

{{< figure src="compute.jpeg" alt="Onocoy DIY Compute for Receivers" link="https://amzn.to/45IW4ZD" >}}

### Raspberry Pi and Pi Clones:

Hard to get ahold of these days but they are super low power and are quite customizable. For info on how to install Raspbian on your Raspberry PI.

| Name                                                                                          | Description                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/45IW4ZD" >}}Orange Pi 5 4GB{{< /centerbutton >}}       | The Orange Pi 5 is recommended for its super low power and high customizability. It provides up to 4GB of RAM and offers a cost-effective solution for various projects.                                                                                                                                   |
| {{< centerbutton href="https://amzn.to/3x72kv0" >}}Raspberry Pi 4B Model B DIY Kit{{< /centerbutton >}} | **Preferred Option:** If available, the Raspberry Pi 4B Model B DIY Kit is recommended for Raspberry Pi enthusiasts. It offers a versatile and customizable computing solution, suitable for various applications and projects.                                                                                |
| {{< centerbutton href="https://amzn.to/3jG2g2k" >}}GeeekPi Raspberry Pi 4 4GB Starter Kit{{< /centerbutton >}} | A ready-to-go starter kit for Raspberry Pi 4, suitable for those who prefer a convenient setup with moderate power. It includes essential components to kickstart your Raspberry Pi projects.                                                                                                                     |
| {{< centerbutton href="https://amzn.to/3DQisF6" >}}GeeekPi Raspberry Pi 4 8GB Starter Kit{{< /centerbutton >}} | Another kit variant with 8GB of RAM, ideal for users with higher performance requirements on the Raspberry Pi 4. It provides additional memory for more demanding applications and projects.                                                                                                              |

### Any Mini PC with Intel N5100 or similar:

For super low power Raspberry Pi equivalent but on x64 platform.

| Name                                                                                          | Description                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3YkFhcj" >}}Beelink U59 Mini PC{{< /centerbutton >}}    | The Beelink U59 Mini PC offers a low-power alternative for those seeking a Raspberry Pi equivalent on an x64 platform. It provides a compact and efficient computing solution with the power of Intel N5100.                                                                                             |
| {{< centerbutton href="https://amzn.to/3XkbXkS" >}}TRIGKEY Mini Computer{{< /centerbutton >}} | Another option for an x64 platform, the TRIGKEY Mini Computer provides a compact and efficient computing solution. It is suitable for various applications and projects, offering versatility in a small form factor.                                                                                   |

### Ultra Low Power / Low Budget

{{< centerbutton href="https://simeononsecurity.com/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980/" >}}How to Set Up a GPS/GNSS Bases Station on an ESP32{{< /centerbutton >}}

### Compute Notable Mentions
Older Raspberry Pi models (1, 2, 3) should be sufficient. But newer models should be significantly more efficient and allow you do run multiple [low powered mining setups](https://simeononsecurity.com/other/creating-profitable-low-powered-crypto-miners/) on a single device. This is why we recommend newer compute hardware.

## Recommended GPS Receivers for DIY Onocoy Deployments
There are many receivers on the market but at a bare minimum it must support [**RTCM (Radio Technical Commission for Maritime Services)**](https://en.wikipedia.org/wiki/RTCM_SC-104) and ideally have the ability to be hooked up to an antenna outside of the install location with 360 degree unobstructed view of the sky.

{{< figure src="basic-receivers.jpeg" alt="Basic GPS Receivers for Onocoy" >}}

{{< centerbutton href="https://gnss.store/unicore-gnss-modules/247-elt0222.html" >}}Get your GNSS.STORE UM980 RTK GNSS USB Dongle Today!{{< /centerbutton >}}


- **U-Blox Based Receivers**
  - [NEO-M8P RTK GPS GNSS receiver board with SMA and mini USB for UAV, Robots](https://gnss.store/neo-m8p-gnss-modules/90-elt0078.html) - $150
    - Single-Band (L1 only), 72 Channels, supports USB; I2C; and UART, Accurate within 6 feet, 10hz pull rate. Rewards will be limited, 8-10% only.
    - Shows up as `/dev/ttyACM0` instead of `/dev/ttyUSB0` in the instructions below. Same goes for all U-BLOX based devices.
  - [NEO-F9P-15B Multi-band](https://gnss.store/gnss-gps-modules/222-elt0185.html) - $220
    - Dual-Band L1+L2 (or L1+L5), 184 Channels, supports USB only, Accurate within 6 feet, 20hz pull rate. Rewards will be limited, 30% of possibly maximum rewards.
  - [SparkFun GPS-RTK Board - NEO-M8P-2 (Qwiic)](https://www.sparkfun.com/products/15005) - $180
    - NEO-M8P-2 Based, Single-Band (L1 only), 6 Foot Accuracy. Rewards will be limited, 8-10% only.
  - [SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://www.sparkfun.com/products/16481) - $275
    - ZED-F9P Based, Dual-Band L1+L2 (or L1+L5), 184 Channels, 20hz pull rate, USB or GPIO Breakout. Rewards are limited, 30% of possibly maximum rewards.
  - [ZED-F9P RTK GNSS receiver board with SMA Base or Rover](https://gnss.store/zed-f9p-gnss-modules/99-13-elt0087.html#/27-add_antenna-without_antenna) - $210
    - ZED-F9P Based, Dual-Band L1+L2 (or L1+L5), 184 Channels, 20hz pull rate, USB Only. Rewards are limited, 30% of possibly maximum rewards.
- **Unicorecomm UM980/UM982 Based USB Receivers**
The preferred option overall and by far for almost every setup.
Requires [FTDI Drivers](https://ftdichip.com/drivers/vcp-drivers/).
  - (**Preferred**)[UM980 RTK GNSS USB Dongle](https://gnss.store/unicore-gnss-modules/247-elt0222.html) - $225
    - Unicorecomm UM980 Based, Triple Band L1, L2 and L5, All-Constellation, High Precision, 1408 Channels, 20hz pull rate, 80% Rewards.
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.
  - (**Preferred**)[UM982 Dual Channel RTK GNSS USB Dongle](https://gnss.store/um982-gnss-modules/239-elt0212.html) - $235
    - Unicorecomm UM982 Based, Triple Band L1, L2 and L5, All-Constellation, High Precision, 1408 Channels, 20hz pull rate, 80% Rewards.
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.

### Advanced Receivers for DIY Onocoy Deployments
These are all going to be devices that are Triple-Band, High Pull Rate, Extreme Position Receivers. They likely won't support USB. They will require PCI-E, UART, I2C, or Serial Connections. 
If you don't know what that is or you aren't experienced, please use the options above. However these will allow you to be capable of at most 80% of Onocoy Rewards in the case of the [Unicorecomm UM980](https://en.unicorecomm.com/products/detail/26) and [Unicorecomm UM982](https://en.unicorecomm.com/products/detail/24) based boards and 100% of rewards in the [Septentrio Mosaic X5](https://www.septentrio.com/en/products/gps/gnss-receiver-modules/mosaic-x5) based boards. While you'll be able to use the same software we mention below, the instructions we've provided won't exactly line up. Be advised.

{{< figure src="advanced-receivers.jpeg" alt="Basic GPS Receivers for Onocoy" >}}

{{< centerbutton href="https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html" >}}Get the GNSS.STORE Triple Band Survey Antenna Today!{{< /centerbutton >}}

- **Unicorecomm UM980**
Capable of 80%-90% of the Onocoy rewards if installed correctly. 100% is possible after planned future firmware update. Fimware updates are dependent on the manufacture of the device providing them. Unicorecomm will not provide them to the public.

  - [UM980 module](https://www.aliexpress.us/item/3256805035445904.html) + [DSD TECH SH-U05A USB to I2C](https://amzn.to/3tptGOk) + [GH1.25 to Dupont2.54 Pre-Crimped Cables](https://amzn.to/3tptGOk)- $180 - $220
    - Unicorecomm UM980 Based, Triple Band L1, L2 and L5.
    - For more details on how to install this, we recommend you read this article on [how to set up the I2C connection on the UM980](https://wholovesburrito.com/2023/09/25/an-affordable-diy-gnss-station-for-onocoy/)
    - ***Don't expect the aliexpress manufactures to be able to provide firmware updates.***
  - [UM980 M.2](https://gnss.store/unicore-gnss-modules/250-elt0225.html)
    - Unicorecomm UM980 Based, Triple Band L1, L2 and L5. 
    - May not be recognized by all systems, it uses USB protocols over M.2
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.
  - [UM980 mPCIe](https://gnss.store/unicore-gnss-modules/251-elt0226.html)
    - Unicorecomm UM980 Based, Triple Band L1, L2 and L5. 
    - May not be recognized by all systems, it uses USB protocols over mPCIe
    - Use discount code `SIMEONSECURITY_GNSS` for an additional 5% discount.

- **Unicorecomm UM982**
Capable of 80%-90% of the Onocoy rewards if installed correctly. 100% is possible after planned future firmware update. Fimware updates are dependent on the manufacture of the device providing them. Unicorecomm will not provide them to the public.
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
  - [mosaic-go GNSS module receiver evaluation kit](https://shop.septentrio.com/en/shop/mosaic-go-gnss-module-receiver-evaluation-kit)
    - Septentrio Mosaic X5 Based, 50-100hz Pull Rate, Anti-Interference, Anti-Jamming, Anti-Spoofing.
  - (**Preferred**)[simpleRTK3B mPCIe](https://www.ardusimple.com/product/simplertk3b-mpcie-septentrio-mosaic/)
    - Septentrio Mosaic X5 Based, 50-100hz Pull Rate, Anti-Interference, Anti-Jamming, Anti-Spoofing.

## Recommended Antennas for Onocoy

We've covered this in a more in depth guide about the [Best GPS Base Station Antennas](https://simeononsecurity.com/other/unveiling-best-gps-antennas-onocoy-geodnet/).

### Basic Antennas for Onocoy

{{< figure src="BT-800D.jpeg" alt="Beitian BT-800D High Gain High Precision GPS/GNSS Antenna" link="https://amzn.to/47MWdxa" >}}

For U-Blox based receivers, we recommend the following antenna options to enhance GPS navigation accuracy.

| Name                                                                                                              | Description                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3qM9N36" >}}Bingfu GPS Navigation Antenna{{< /centerbutton >}}         | Basic, simple, and budget-friendly, the Bingfu GPS Navigation Antenna is a reliable choice for users looking for a functional solution at an affordable price of $9.                                                                              |
| {{< centerbutton href="https://amzn.to/3PcSGki" >}}Preferred - Bingfu GPS Navigation External Antenna{{< /centerbutton >}} | Our preferred option, the Bingfu GPS Navigation External Antenna at $24, is outdoor-rated, cost-effective, and provides an unobstructed view of the sky, ensuring optimal GPS signal reception.                                                        |
| {{< centerbutton href="https://amzn.to/3ORbgxc" >}}SparkFun GNSS-RTK Accessory Kit{{< /centerbutton >}}        | Priced at $85, the SparkFun GNSS-RTK Accessory Kit is recommended for users facing challenges in properly installing other antennas. Note that it may underperform compared to the preferred options and should be chosen as a last resort. |

### Advanced Antennas for Onocoy

{{< figure src="surveying-antenna.jpeg" alt="Ardusimple and GNSS.STORE Surveying Antennas" link="https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html" >}}

### Antenna Options for Recommended GNSS Receivers:

For optimal performance with the recommended GNSS receivers, we suggest the following antenna options to ensure accurate and reliable navigation.

| Name                                                                                                              | Description                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/47MWdxa" >}}Preferred - Beitian High Gain High Precision GPS/GNSS Antenna{{< /centerbutton >}}                   | Our top recommendation, the Beitian High Gain High Precision GPS/GNSS Antenna priced at $86, offers high antenna gain, precision, anti-interference features, IP67 rating, and wide band support. It's suitable for various applications with exceptional performance.                                                          |
| {{< centerbutton href="https://www.ardusimple.com/product/calibrated-survey-gnss-quadband-antenna-ip67/" >}}Preferred - Calibrated Survey GNSS Quad-Band Antenna{{< /centerbutton >}} | The Calibrated Survey GNSS Quad-Band Antenna, priced at $230, is another preferred option known for its extremely high precision, anti-interference capability, and support for all bands. It provides reliable performance and is suitable for surveying applications.                                                     |
| {{< centerbutton href="https://hyfix.ai/products/multi-frequency-high-precision-survey-antenna" >}}Multi-frequency High Precision Survey Antenna{{< /centerbutton >}}    | Priced at $95, the Multi-frequency High Precision Survey Antenna offers a strong signal, high precision, and built-in anti-interference features. It provides reliable performance and is suitable for various applications requiring accurate GNSS reception.                                                                     |
| {{< centerbutton href="https://amzn.to/47Mj4ZH" >}}GNSS Surveying Antenna and Precise Navigation Antenna{{< /centerbutton >}}                             | Priced at $180, the GNSS Surveying Antenna and Precise Navigation Antenna features high antenna gain, extremely high precision, and an IP67 rating. It is designed for precise navigation applications, providing reliable performance in challenging environments.                                                             |
| {{< centerbutton href="https://www.gns-electronics.de/product/harxon-csx627a/" >}}HARXON CSX627A{{< /centerbutton >}}                         | The HARXON CSX627A, priced at $135, is a calibrated triple-band RTK antenna with an IP67 rating. It supports all bands, making it a versatile option for various GNSS applications requiring precise navigation and reliability in different environmental conditions.                                                               |
| {{< centerbutton href="https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html" >}}L1/L2/L5 GPS, G1/G2/G3 GLONASS, B1/B2/B3 BDS, Galileo E1/E5/E6 38dB Antenna{{< /centerbutton >}}  | Priced at $205, this antenna supports a wide range of bands, including L1/L2/L5 GPS, G1/G2/G3 GLONASS, B1/B2/B3 BDS, and Galileo E1/E5/E6. With a 38dB gain, it is suitable for applications requiring support for multiple constellations and high precision.                                                                                  |
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


## Proper Onocoy Base Station Antenna Placement

{{< figure src="installedantenna.png" caption="Installed Antenna - doc.onocoy.com" alt="An Installed Tri-Band GPS Antenna" link="https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/2.-install-your-station" >}}

Onocoy has published [antenna placement requirements](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/2.-install-your-station), but to summarize you should understand the following:

1. **Optimal Location Selection**: To optimize station placement,** choose a location at least 20 kilometers away from the nearest Onocoy station**. Stations located close to three or more others will receive reduced rewards. Utilize the [Onocoy Explore function](https://console.onocoy.com/explorer) to easily check the distance to the nearest Onocoy station for any location.
  {{< figure src="onocoy-explorer.webp" caption="Onocoy Explorer - doc.onocoy.com" alt="onocoy Explorer" link="https://docs.onocoy.com/documentation/topics/explorer" >}}

2. **Ideal Surroundings**: **Ensure that the antenna has an unobstructed 360-degree view of the sky**, with no obstructions such as buildings, trees, or mountains above 10 degrees elevation. Limited sky visibility or signal multipath can result in scaled-down rewards. **The antenna must be rigidly mounted to prevent movement exceeding 1-2 millimeters**, as excessive vibrations or movement can lead to reward pausing.

3. **Stable Internet Connection**: Maintain a stable and permanent internet connection for the station. The required bandwidth is relatively low, typically around **1 kB/s**, and **no inbound traffic is necessary**. There is no need to open ports on typical firewalls, as connections are established from inside-out.

## Setting up the Onocoy Base Station and NTRIP Software
Once you've set up your device and [properly placed your antenna](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/2.-install-your-station), you can start configuring the required software. 

*For this section we assume some basic technical experience and that you have installed your operating system already as well as know how to get into the terminal.*

1. We need to create an account and get our credentials from the [onocoy website](https://console.onocoy.com/explorer). You will need to grab the server address, username, password, and port number from this step. Once it is completed, go to the reference station tab and grab the mount point, which we also need.
- Refer to the [Onocoy documentation](https://docs.onocoy.com/documentation/quick-start-guides/get-gnss-correction-data) if you need help.

2. Install some base dependencies.
      ```bash
      sudo apt install -y gpsd gpsd-clients minicom socat git make build-essential
      ```

3. Follow one of the Options Below. Either **NTRIP Server** or **RTKLIB**

4. Wait and Verify Your Station on the Onocoy Dashboard
   1.  Visit the [Onocoy Console Dashboard](https://console.onocoy.com/servers) and check to see your device has finished it's validation period. If it hasn't check back later, it can take up to 3 days.

5. Profit?
   1. You can view the following [Onocoy documentation](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/4.-receive-rewards) to learn more.

### Option 1: NTRIP Server
1. On your linux device download the [ntripserver](https://github.com/simeononsecurity/ntripserver) software.
    ```bash
    git clone https://github.com/simeononsecurity/ntripserver.git
    cd ./ntripserver
    make
    ```
2. Identify the USB Source
    1. Idendify that linux recognizes the device is plugged in. 
    ```bash
    lsusb
    ```
    Ex. `Bus 00x Device 00x: ID xxxx:xxxx Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P` or `Bus xxx Device xxx: ID xxxx:xxxx U-Blox AG [u-blox 8]`

   2. Identify the propper ttyUSB/ttyACM path.
   **Note**: *Some devices may show up as `ttyUSB0`, `ttyACM0`, etc. You'll have to look this up per your device.**
    ```bash
    ls /dev/ttyUSB*
    ```
    
    **Note:** Minicom is a tool used to view the serial output of devices. To use it, you'll need to read this [guide on using minicom](https://wiki.emacinc.com/wiki/Getting_Started_With_Minicom). If this sounds difficult to you, skip this step.

    ```bash
    sudo minicom -D /dev/ttyUSB0
    ```

1. Now we get to configure the software

> **Note:** The onocoy dashboard/explorer won't provide you with the mountpoint information until they verify you can send them data. Omit the mountpoint details from this section until after you initially get past that window. Then test it again.

   1. Test the configuration.

      ```bash
          ~/ntripserver/ntripserver -M 1 -i /dev/ttyUSB0 -b 921600 -O 1 -a servers.onocoy.com -p 2101 -m {{mountpointhere}} -n {{usernamehere}} -c {{passwordhere}}
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
        Wants=network-online.target
        After=network-online.target

        [Service]
        ExecStart=/path/to/ntripserver -M 1 -i /dev/ttyUSB0 -b 921600 -O 1 -a servers.onocoy.com -p 2101 -m {{mountpointhere}} -n {{usernamehere}} -c {{passwordhere}}
        Restart=always
        RestartSec=120  # 2 minutes (in seconds)
        TimeoutStartSec=300 # Set a 5-minute timeout (adjust as needed)
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
        ntripserver[815]: serial input: device = /dev/ttyUSB0, speed = 921600
        systemd[1]: Started NTRIP Server Service.
        ntripserver[815]: caster output: host = xxx.xxx.xxx.xxx, port = 2101, mountpoint = Mount1, mode = http
        ntripserver[815]: transfering data ...
        ```
### Option 2: RTKLIB
1. On your linux device install the [rtklib](https://rtklib.com/) software.
    ```bash
    sudo apt-get update
    sudo apt-get -y install rtklib
    ```
2. Identify the USB Source

    ```bash
    lsusb
    ```
    Ex. `Bus 00x Device 00x: ID xxxx:xxxx Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P` or `Bus xxx Device xxx: ID xxxx:xxxx U-Blox AG [u-blox 8]`

    **Note**: *Some devices may show up as `ttyUSB0`, `ttyACM0`, etc. You'll have to look this up per your device.*

    ```bash
    ls /dev/ttyUSB*
    ```

    ```bash
    sudo minicom -D /dev/ttyUSB0
    ```
3. Create a Rtkrcv.conf RTKLIB Configuration File
    1. Create the paths and conf file
      ```bash
      sudo mkdir ~/rtklib/
      sudo nano ~/rtklib/rtkrcv.conf
      ```
    2. Conf File Contents
    > **Note:** The onocoy dashboard/explorer won't provide you with the mountpoint information until they verify you can send them data. Omit the mountpoint details from this section until after you initially get past that window. Then test it again.
      ```toml
      [serial]
      port = /dev/ttyUSB0
      bitrate = 921600
      [ntrip]
      caster = servers.onocoy.com
      port = 2101
      mountpoint = {{mountpointhere}} 
      user = {{usernamehere}}
      passwd = {{passwordhere}}
      [output]  
      format = rtcm3
      path = /path/to/output/file.rtcm
      ```
    3. Test the RTKLIB config
      ```bash
        rtkrcv -s -o ~/rtklib/rtkrcv.conf
      ```
4. Create the RTKLIB Service
  1. Create the Service Unit File
    ```bash
    sudo nano /etc/systemd/system/rtklib.service
    ```
  2. Add the Service Configuration
    ```toml
    [Unit]
    Description=RTKLIB Service
    After=network.target
    Wants=network-online.target
    After=network-online.target

    [Service]
    ExecStart=/path/to/rtkrcv -s -o /path/to/rtkrcv.conf
    Restart=always
    RestartSec=120  # 2 minutes (in seconds)
    TimeoutStartSec=300 # Set a 5-minute timeout (adjust as needed)
    User=root

    [Install]
    WantedBy=default.target
    ```
  3. Enable and Start The Service
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable rtklib.service
    sudo systemctl start rtklib.service
    ```
  4. Verify the Service
    ```bash
    sudo systemctl status rtklib.service
    ```   
### Option 3: Docker Container

#### 1. Install Docker

Consult the following guides for more information on how to install docker

- https://www.digitalocean.com/community/tutorial-collections/how-to-install-and-use-docker
- https://docs.docker.com/engine/install/
- https://docs.docker.com/engine/install/ubuntu/

#### 2. Run the Docker Container

   Run the Docker container, ensuring that you provide the necessary environment variables and parameters:

    > You don't have to specify both Onocoy and RTKDirect credentials. The backend script is smart and looks to see if they have been set. You can use one or both and this should function perfectly.

   > If the environment variable `ONCOCOY_MOUNTPOINT` or `ONOCOY_USE_NTRIPSERVER` or `RTKDIRECT_USE_NTRIPSERVER` is specified, the docker container will use **NTRIPSERVER** for Onocoy or RTKDirect respectively, otherwise it'll use **RTKLIB** for the connection to Onocoy and/or RTKDirect. The container will still use RTKLIB for the splitting of the feed no matter what.
   > `LAT`, `LONG`, `ELEVATION`, `INSTRAMENT`, and `ANTENNA` are all optional and are only used if RTKLIB is being used and NTRIPSERVER is not.

   > You may specify `TCP_OUTPUT_PORT` to change the tcp server's output port if using docker's [host networking mode](https://docs.docker.com/network/#drivers). Otherwise use the appropriate docker [port mappings](https://docs.docker.com/network/#published-ports).

   > You can host any RTKLIB or tcp server instance on another machine and retreive the data using our dockers tcp client mode by defining `TCP_INPUT_IP` and `TCP_INPUT_PORT`. In which you'll specify your tcp servers ip and port.

> **Note:** The onocoy dashboard/explorer won't provide you with the mountpoint information until they verify you can send them data. Omit the mountpoint details from this section until after you initially get past that window. Then run the command again.

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
      -e ONOCOY_MOUNTPOINT=<YOUR_ONOCOY_MOUNTPOINT> \
      -e ONOCOY_USERNAME=<YOUR_ONOCOY_MOUNTPOINT_USERNAME> \
      -e ONOCOY_PASSWORD=<YOUR_ONOCOY_MOUNTPOINT_PASSWORD> \
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
     -e ONOCOY_MOUNTPOINT=YOUR_ONOCOY_MOUNTPOINT \
     -e ONOCOY_USERNAME=YOUR_ONOCOY_MOUNTPOINT_USERNAME \
     -e ONOCOY_PASSWORD=YOUR_ONOCOY_MOUNTPOINT_PASSWORD \
     -e PORT_NUMBER=32377 \
     -e LAT=37.7749 \
     -e LONG=-122.4194 \
     -e ELEVATION=50 \
     -e INSTRUMENT="Your GPS Receiver" \
     -e ANTENNA="Your Antenna" \
     simeononsecurity/docker-rtklib-onocoy-rtkdirect:latest
   ```

### **Windows Option 1: STRSVR** 

On windows, one of our best options and arguably our best free option is [STRSVR](https://github.com/Aceinna/rtklib_aceinna/releases), which is based on RTKLIB.

1. Download and save [`STRSVR.exe`](https://github.com/Aceinna/rtklib_aceinna/releases) from the [github releases page](https://github.com/Aceinna/rtklib_aceinna/releases). Be sure to save it to a good location that you can easily find again later.

2. Execute `STRSVR.exe`, select `Serial` as your input device, and configure the correct **COM Port** for your serial reciever.

  {{< figure src="strsvr-serial.jpeg" alt="STRSVR Serial Configuration" caption="STRSVR Serial Configuration" link="https://github.com/Aceinna/rtklib_aceinna/releases" >}}

  > **Note**: *Your com port will be different on your device. Consult your manufactures documentation and the Windows **Device Manager** on to identify the correct com port* 

3. Select `NTRIP Server` as one of your output devices and configure it using the credentials and settings you got from the [onocoy console](https://console.onocoy.com).

{{< figure src="strsvr-ntrip-server.jpeg" alt="STRSVR NTRIP Server Configuration" caption="STRSVR NTRIP Server Configuration" link="https://github.com/Aceinna/rtklib_aceinna/releases" >}}

4. Hit the `Start Button`

{{< figure src="strsvr-demo.jpeg" alt="STRSVR DEMO" caption="STRSVR DEMO" link="https://github.com/Aceinna/rtklib_aceinna/releases" >}}

### **Windows Option 2: SNIP** 

On windows, our options are limited. One of the NTRIP communities favorite options for Windows is [Snip](https://www.use-snip.com/). While there is a trial available, you'll need to purchase the software long term if you plan on ever using it for more than an hour at any given time.

1. Download and install Snip from the [download page](https://www.use-snip.com/download/).

{{< figure src="snipdownload.jpeg" alt="Snip Download Page" caption="Snip Download Page" link="https://www.use-snip.com/download/" >}}

  > *You'll have to give them an email and get the download link in your email. Use a service like [10minutemail](https:/10minutemail.com) to avoid getting spam in your email.*

2. Once installed, go to the [**relay streams tab**](https://www.use-snip.com/kb/knowledge-base/the-relay-streams-tab/#:~:text=The%20Relay%20Stream%20tab%20is,their%20overall%20operational%20up%20time.) tab and delete all options from that page.

  {{< figure src="relaystreams.jpeg" alt="Snip Relay Streams Menu" caption="Snip Relay Streams Menu - use-snip.com" link="https://www.use-snip.com/kb/knowledge-base/the-relay-streams-tab/#:~:text=The%20Relay%20Stream%20tab%20is,their%20overall%20operational%20up%20time." >}}

3. Under the [**Serial Streams Tab**](https://www.use-snip.com/kb/knowledge-base/the-serial-streams-tab/) add your COM device and create a serial stream device.

  {{< figure src="serialstreams.jpeg" alt="Snip Serial Streams Menu" caption="Snip Serial Streams Menu - use-snip.com" link="https://www.use-snip.com/kb/knowledge-base/the-serial-streams-tab/" >}}

  > [Learn more about how to add a serial stream source device on Snip](https://www.use-snip.com/kb/knowledge-base/adding-serial-uart-data-streams/)

4. On the [**Pushed-Out Data Tab**](https://www.use-snip.com/kb/knowledge-base/the-pushed-out-streams-tab-output-data/) manually add the Ntrip server information from the [onocoy console](https://console.onocoy.com).

  {{< figure src="pushoutdata.jpeg" alt="Snip Pushed-Out Data Menu" caption="Snip Pushed-Out Data Menu - use-snip.com" link="https://www.use-snip.com/kb/knowledge-base/the-pushed-out-streams-tab-output-data/" >}}

  > [Learn more on how to add pushed-out data streams on snip](https://www.use-snip.com/kb/knowledge-base/sending-pushed-out-data/)


## Troubleshooting and Verifying GPS Connectivity on Linux
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
  - Seems to be a newer version of the software we used above. However it's more difficult to access. It is created and maintained by the [German Federal Agency for Cartography and Geodesy (BKG)](https://www.bkg.bund.de/EN/Home/home.html)
- [RTKLIB STR2STR](https://github.com/rtklibexplorer/RTKLIB/releases)
  -  A more widely used Ntrip server. However it can be significantly more technically involved.
- [rtklibexplorer/RTKLIB](https://github.com/rtklibexplorer/RTKLIB)
  - A version of RTKLIB optimized for single and dual frequency low cost GPS receivers, especially u-blox receivers. It is based on RTKLIB 2.4.3 and is kept reasonably closely synced to that branch.
  - A fork of the original RTKLIB that is known to be more frequently updated and more optimized than the original RTKLIB.
  - The variant of RTKLIB we use in our docker container.
- [esp32-xbee](https://github.com/nebkat/esp32-xbee)
  -  Exclusive to the ESP32, this software enables you to build even cheaper base stations. Or more expensive... 

## Additional Configuration For Unicorecomm UM980 and UM982 Devices

To enable all the bands and base station mode on the Unicorecomm devices you'll need to serial into them using baud rate of `115200` and run the following commands. This can be done within terminal, putty, or the [Unicorecomm UPrecise](https://en.unicorecomm.com/download) software.

- [Alternate (More up to date) U-Precise Installer](http://www.eltehs.lv/UPrecise-V2.0.802.zip)

The provided configuration adjustments are made to ensure the proper functionality of the reference station receiver, specifically tailored for the [Onocoy system](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy). [Click here understand What RTCM Messages Onocoy supports](https://simeononsecurity.com/other/onocoy-supported-rtcm-messages/).

### Unicorecomm UM980 and UM982 Configuration Script

> **Note:** Not all of these commands will work on all UM980 or UM982 varients. Some commands are firmware specific some are redundant. Not all commands are required. These are just what we determined to be "most optimal" for most situations for both Onocoy and for any other service you may use your UM98x with. If there is a feature missing that you want, contact your device manufacture for firmware update instructions.

```bash
#RESET ALL SETTINGS TO FACTORY DEFAULTS
#FReset

#DISABLE ALL MESSAGE TYPES
UNLOG
UNILOGLIST
saveconfig

# Enable anti-jamming function
CONFIG ANTIJAM FORCE
saveconfig

# Maximum age of RTK data*, in seconds
CONFIG RTK TIMEOUT 600

# High reliability for RTK Positioning and ADR
CONFIG RTK RELIABILITY 4 4

# High threshold for CN0
#CONFIG RTK CN0THD 1

# High threshold for multi-path mitigation
#CONFIG RTK MMPL 1

# Enable multi-path mitigation
CONFIG MMP ENABLE

# RTCM Clock Offset Compensation
CONFIG RTCMCLOCKOFFSET ENABLE
saveconfig

# Doppler Position Prediction Configuration
CONFIG PSRVELDRPOS ENABLE

# Set up automatic base configuration with automatic gps location 
mode base time 60 2 2.5

# Enable the Largest Signal Group
config signalgroup 2
saveconfig
config RTCMB1CB2a enable
saveconfig

# ONLY IF MODULE IS UM982
# CONFIG SIGNALGROUP 3 6
# IF ABOVE COMMAND DOESN'T WORK TRY
# CONFIG SIGNALGROUP 7 0

#Disable Undulation Fixes per GNSS.STORE Recommended Configuration
saveconfig
CONFIG UNDULATION 0
saveconfig

# Enable All bands
UNMASK GPS
UNMASK BDS
UNMASK GLO
UNMASK GAL
UNMASK QZSS
UNMASK IRNSS
UNMASK ALL
saveconfig

# ONOCOY RTCM CONFIGURATION
rtcm1005 30
rtcm1033 30
rtcm1077 1
rtcm1087 1
rtcm1097 1
rtcm1117 1
rtcm1127 1
saveconfig

# Full RTCM 3.2 Configuration (Skip if only doing onocoy)
rtcm1006 30
rtcm1007 30
rtcm1019 1
rtcm1020 1
rtcm1033 30
rtcm1042 1
rtcm1044 1
rtcm1045 1
rtcm1046 1
rtcm1077 1
rtcm1087 1
rtcm1097 1
rtcm1107 1
rtcm1117 1
rtcm1127 1
rtcm1137 1
saveconfig

# Only configure if you know SBAS is available in your region
# Onocoy ignores SBAS you do not need to enable this unless you know what you're doing or you're following our dual or triple mining guides.
# CONFIG SBAS ENABLE Auto
# CONFIG SBAS TIMEOUT 600
# saveconfig

# ONLY CHANGE IF YOU WANT TO IMPROVE THE BAUDRATE OR IF YOU RUN INTO STABILITY ISSUES WITHOUT IT
# config com1 921600
# saveconfig
```

*It should be noted that the Unicorecomm device does not have the ability to transmit the `RTCM 1230` message type as required per [Onocoy system's requirements](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy).*

### Unicorecomm UM980 and UM982 Commands Reference Manuals
For additional configuration guidance, consult the following documentation:
- [UM980 / UM982 Commands Reference Manual](https://en.unicorecomm.com/assets/upload/file/Unicore_Reference_Commands_Manual_For_N4_High_Precision_Products_V2_EN_R1_1.pdf)
- [NebulasIV Commands Reference Manual](https://gnss.store/index.php?controller=attachment&id_attachment=255)

### Symlinking Serial Devices to Hardcoded Path

In order to make the device appear as ttyUM980 instead of ttyUSB0:

`$ cat /etc/udev/rules.d/00-um980.rules`
```bash
KERNEL=="ttyUSB[0-9]", \
ATTRS{idVendor}=="0403",ATTRS{idProduct}=="6015", \
SYMLINK+="ttyUM980"
```

### Maintaining UPrecise Access with Linux using Socat

To ensure uninterrupted UPrecise access when using Linux, you can utilize the `socat` application to connect to the UM980's serial interface from a Windows machine.

Here's the command to achieve this:

*Replace `{{portnumber}}` with a port number of your choosing*

```bash
sudo socat tcp-listen:{{portnumber}},reuseaddr /dev/ttyUSB0,b115200,raw,echo=0
```
Next, follow these steps to set up UPrecise on a Windows PC within the same network:

1. Launch UPrecise.
2. Navigate to the "Connections" menu.
3. Select "TCP/IP" as the connection type.
4. Enter the IP address of your Linux host and the port number specified in the previous command.
5. You will now have access to the Data Stream and can continue sending commands as usual.

{{< figure src="uprecise.png" alt="unicorecom uprecise tcp window" caption="Unicorecomm Uprecise TCP Window - wholovesburrito.com" link="https://wholovesburrito.com/2023/09/25/an-affordable-diy-gnss-station-for-onocoy/" >}}

______

## Onocoy FAQ
### **Onocoy Setup**

**Q1: Which equipment can be used to set up a station?**
  - A1: Any GNSS device capable of data transfer via NTRIP is recommended, with featured bundles listed on the [dedicated onocoy device page](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/1.-get-a-station) or recommended in this [article above](https://simeononsecurity.com/other/onocoy-gps-gnss-reciever-basestation-on-a-budget/#recommended-hardware-for-onocoy).

**Q2: Where should the antenna be placed?**
  - A2: Ideally, fix the antenna in a location with a full sky view, such as a roof, chimney, or open field. Ensure no obstructions exist above 10 degrees elevation angle, and secure the antenna against movement during adverse weather.

**Q3: What is needed to connect the device, and is WiFi necessary?**
  - A3: A stable internet connection is required, whether through WiFi or Ethernet, depending on the device.

**Q4: What happens if I want to change the location of my station/antenna/receiver?**
  - A4: Moving the device to another location is not a problem; you just need to successfully pass the data validation process again.

### **Onocoy Devices & Streams**

**Q5: Can streams be retrieved directly if my station only supports NTRIP caster and is exposed on the internet?**
  - A5: No, due to complexities, it is not a reliable method. Contact your station manufacturer to add NTRIP server functionality.

**Q6: What NTRIP Messages need to be enabled on my GNSS reference receivers for the best rewards?**
  - A6: Enable **RTCM 3.0 MSM7 Messages for optimal rewards**, including messages for various constellations. Lower tier messages are supported, while certain message types are ignored.

**Q7: What latency is tolerable from the GNSS receiver to the onocoy system?**
  - A7: The **end-to-end latency should be below 1 second**; larger latencies result in reduced rewards and potential disconnection.

**Q8: Do I have to set the receiver in a special Reference station mode to determine its accurate location?**
  - A8: No, the onocoy system's validation procedures determine the precise location of your station.

**Q9: How does onocoy prevent fraudulent correction streams?**
  - A9: onocoy employs sophisticated methods, including regular data consistency checks, real-time supervision, and checks over long-term periods to detect fraudulent streams.

**Q10: Can I provide data from a 3rd party service, such as public networks like IGS or other networks?**
  - A10: Yes, with acceptance of terms and conditions, provided you have the rights. Multiple submissions from free networks may result in banning.

**Q11: My station frequently disconnects. What can I do?**
  - A11: Disconnections are observed due to updates but should not affect operations. No action is needed on the user's network side.

### **Onocoy Rewards**

**Q12: My wallet is not connecting. What can I do?**
  - A12: Ensure you are using Chrome or Brave Browser on a Desktop device. Follow instructions on the page, and if issues persist, contact support through the [onocoy discord](https://discord.gg/CHKxSpPQ8p).

**Q13: How is the location scale calculated?**
  - A13: Factors include the number and distance of nearby stations, with the quality of neighboring stations influencing rewards.

**Q14: How much will I earn streaming RTK correction data to onocoy?**
  - A14: Earnings depend on factors like signals, satellites, and location. Specific numbers are yet to be decided, but users can earn tokens even before they are officially listed.

**Q15: Why does onocoy use blockchain technology?**
  - A15: onocoy uses blockchain to stabilize token prices, with mechanisms like required tokens for data access, constant burn, locked tokens for governance, a capped maximum supply, and a staking function.

**Q16: How do I claim my rewards?**
  - A16: Click the "Claim Rewards" button in your NTRIP server list in the Onocoy Dashboard. Rewards can be claimed anytime, and changes in the reward factor trigger automatic claiming. Review your current balance in the upper right corner of the validator.

______
## Conclusion

Setting up your **own DIY GPS Onocoy server** doesn't have to be a daunting task. With the **right hardware choices**, **reliable GPS receivers**, and a clear understanding of the process, you can achieve **remarkable precision and accuracy** in your *location-based applications*.

By following the **step-by-step instructions** outlined in this guide, you've unlocked the potential to **enhance your navigation, positioning, and surveying** endeavors. The **affordable hardware options**, such as [*Raspberry Pi*](https://amzn.to/3x72kv0) and [*Intel NUC*](https://amzn.to/4avlJbr), coupled with **accurate GPS receivers**, pave the way for **effortless and efficient server setup**.

So, **go ahead and set up your Onocoy Reference Station**, refine your skills, and enjoy the **results** that await you. Whether you're **navigating remote terrains**, conducting **surveys**, or exploring new possibilities, your **DIY Onocoy Reference Station** will be your **trusty companion** in the pursuit of **precision**.

Stay inspired, stay innovative, and keep pushing the **boundaries of what's possible with technology**.

Lastly, check out our article on more [low powered mining setups](https://simeononsecurity.com/other/creating-profitable-low-powered-crypto-miners/).

{{< centerbutton href="https://simeononsecurity.com/other/triple-mining-geodnet-onocoy-rtkdirect-gps-revolution/" >}}Read our guide on Triple Mining Geodnet, Onocoy, and RTKDirect{{< /centerbutton >}}

or

{{< centerbutton href="https://simeononsecurity.com/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980/" >}}How to Set Up a GPS/GNSS Bases Station on an ESP32{{< /centerbutton >}}

## References

- [German Federal Agency for Cartography and Geodesy (BKG)](https://www.bkg.bund.de/EN/Home/home.html)
- [NebulasIV Commands Reference Manual](https://gnss.store/index.php?controller=attachment&id_attachment=255)
- [Ntrip Server](https://software.rtcm-ntrip.org/browser/ntrip/trunk/ntripserver)
- [Onocoy - Get GNSS correction data](https://docs.onocoy.com/documentation/quick-start-guides/get-gnss-correction-data)
- [Onocoy - Connect your station to onocoy](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy)
- [Onocoy - Whitepaper](https://www.onocoy.com/s/20230825_whitepaper_onocoy_final.pdf)
- [Onocoy - Linkedin](https://www.linkedin.com/company/onocoy/)
- [Onocoy - Twitter](https://twitter.com/onocoyRTK)
- [Onocoy - Discord](https://discord.gg/2NQJuuFTpV)
- [Onocoy - YouTube](https://www.youtube.com/@onocoy)
- [RTKLIB](https://github.com/rtklibexplorer/RTKLIB/releases)
- [UM980 / UM982 Commands Reference Manual](https://en.unicorecomm.com/assets/upload/file/Unicore_Reference_Commands_Manual_For_N4_High_Precision_Products_V2_EN_R1_1.pdf)
- [Unicorecomm UPrecise](https://en.unicorecomm.com/download)
- [esp32-xbee](https://github.com/nebkat/esp32-xbee)
- [WhoLovesBurrito - Chinese UM980 Dongle Implementation](https://wholovesburrito.com/2023/09/25/an-affordable-diy-gnss-station-for-onocoy/)
