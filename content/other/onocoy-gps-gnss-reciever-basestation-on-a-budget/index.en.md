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
ref: ["/other/creating-profitable-low-powered-crypto-miners","/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980", "/other/onocoy-supported-rtcm-messages"]

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

### Ultra Low Power / Low Budget
If you're interested in a lower power and/or low budget setup, read our guide on [How to Set Up a GPS/GNSS Bases Station on an ESP32](https://simeononsecurity.com/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980/).

### Compute Notable Mentions
Older Raspberry Pi models (1, 2, 3) should be sufficient. But newer models should be significantly more efficient and allow you do run multiple [low powered mining setups](https://simeononsecurity.com/other/creating-profitable-low-powered-crypto-miners/) on a single device. This is why we recommend newer compute hardware.

## Recommended GPS Receivers for DIY Onocoy Deployments
There are many recievers on the market but at a bare minimum it must support [**RTCM (Radio Technical Commission for Maritime Services)**](https://en.wikipedia.org/wiki/RTCM_SC-104) and ideally have the ability to be hooked up to an antenna outside of the install location with 360 degree unobstructed view of the sky.

- **U-Blox Based Recievers**
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

- **Unicorecomm UM980**
Capable of up to 80% of the Onocoy rewards. 100% is possible after planned future firmware update.

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
Capable of up to 80% of the Onocoy rewards. 100% is possible after planned future firmware update.
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

## Recommended Antennas for Onocoy
### Basic Antennas for Onocoy
We can only recommend using these on the basic U-Blox based receivers we recommended earlier.
- [Bingfu GPS Navigation Antenna ](https://amzn.to/3qM9N36) - $9
  - Basic, simple, not the best, but it works.
- (**Preferred**)[Bingfu GPS Navigation External Antenna](https://amzn.to/3PcSGki) - $24
  - Outdoor Rated, Cheap, Allows view of the Sky.
- [SparkFun GNSS-RTK Accessory Kit](https://amzn.to/3ORbgxc) - $85
  - This is only recommended for those who can not properly install the antennas below. It will underperform against the others. 

### Advanced Antennas for Onocoy
For all other recommended Receivers above we recommend the antennas below. 
- (**Preferred**)[Beitian High Gain High Precision GPS/GNSS Antenna](https://amzn.to/47MWdxa) - $86
  - High Antenna Gain, High Precision, Builtin Anti-interference, IP67 Rated, High and Low Temp Ratings, UV Resistant Housing, Supports Most Bands.. 
- (**Preferred**)[Calibrated Survey GNSS Tripleband + L-band antenna (IP67)](https://www.ardusimple.com/product/calibrated-survey-gnss-quadband-antenna-ip67/) - $230
  - Calibrated Quad-Band, Extremely High Precision, Anti-interference, Supports All Bands
- [Multi-frequency High Precision Survey Antenna](https://hyfix.ai/products/multi-frequency-high-precision-survey-antenna) - $95
  - Strong Antenna Signal, High Precision, Builtin Anti-interference.
- [GNSS Surveying Antenna and Precise Navigation Antenna](https://amzn.to/47Mj4ZH) - $180
  - High Antenna Gain, Extremely High Precision, IP67 Rated.
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
{{< inarticle-dark >}}
______

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
      sudo apt install -y gpsd gpsd-dbg gpsd-clients gpsbabel minicom socat git make build-essential
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

    ```bash
    lsusb
    ```
    Ex. `Bus 00x Device 00x: ID xxxx:xxxx Prolific Technology, Inc. PL2303 Serial Port / Mobile Action MA-8910P` or `Bus xxx Device xxx: ID xxxx:xxxx U-Blox AG [u-blox 8]`

    **Note**: *Some devices may show up as `ttyUSB0`, `ttyACM0`, etc. You'll have to look this up per your device.*
`
    ```bash
    ls /dev/ttyUSB*
    ```

    ```bash
    sudo minicom -D /dev/ttyUSB0
    ```

1. Now we get to configure the software
   1. Test the configuration.

      ```bash
          ~/ntripserver/ntripserver -M 1 -i /dev/ttyUSB0 -b 19200 -O 1 -a servers.onocoy.com -p 2101 -m {{mountpointhere}} -n {{usernamehere}} -c {{passwordhere}}
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
        ExecStart=/path/to/ntripserver -M 1 -i /dev/ttyUSB0 -b 19200 -O 1 -a servers.onocoy.com -p 2101 -m {{mountpointhere}} -n {{usernamehere}} -c {{passwordhere}}
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
        ntripserver[815]: serial input: device = /dev/ttyUSB0, speed = 19200
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
      ```toml
      [serial]
      port = /dev/ttyUSB0
      bitrate = 19200
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
  - Seems to be a newer version of the software we used above. However it's more difficult to access. It is created and maintained by the [German Federal Agency for Cartography and Geodesy (BKG)](https://www.bkg.bund.de/EN/Home/home.html)
- [RTKLIB](https://github.com/rtklibexplorer/RTKLIB/releases)
  -  A more widely used Ntrip server. However it can be significantly more technically involved.
- [esp32-xbee](https://github.com/nebkat/esp32-xbee)
  -  Exclusive to the ESP32, this software enables you to build even cheaper base stations. Or more expensive... 

## Additional Configuration For Unicorecomm UM980 and UM982 Devices

To enable all the bands and base station mode on the Unicorecomm devices you'll need to serial into them using baud rate of `115200` and run the following commands. This can be done within terminal, putty, or the [Unicorecomm UPrecise](https://en.unicorecomm.com/download) software.

The provided configuration adjustments are made to ensure the proper functionality of the reference station receiver, specifically tailored for the [Onocoy system](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy).

1. `mode base time 60 2 2.5`: This line configures the reference station's operation mode, which is set to "base". In this configuration the base station will figure out it's actual location after receiving traffic for 60 seconds. 

2. `CONFIG SIGNALGROUP 2`: This command appears to configure the signal group for the UM980/UM982 devices. This enables all bands and frequencies on the device.

3. `rtcm1005 30 and rtcm1006 30`: These commands set the rate at which RTCM messages 1005 and 1006 are sent out from the reference station, respectively. The values "30" suggest a 30-second interval, which is optimized for [Onocoy system's requirements](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy).

4. `rtcm1033 1, rtcm1074 1, rtcm1077 1, rtcm1084 1, rtcm1087 1, rtcm1094 1, rtcm1097 1, and rtcm1117 1, rtcm1124 1 and rtcm1127 1`: These commands enable RTCM messages per [Onocoy system's requirements](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy), ensuring that the reference station transmits these specific messages. The value "1" enables these messages to happen every second..

5. `saveconfig`: This command saves the configured settings, ensuring that they persist and are applied whenever the reference station is operational.

### Unicorecomm UM980 and UM982 Configuration Script
```bash
# Set up automatic base configuration with automatic gps location 
mode base time 60 2 2.5

# Enable the Largest Signal Group
config signalgroup 2
config RTCMB1CB2a enable

# ONLY IF MODULE IS UM982
# CONFIG SIGNALGROUP 3 6

# Enable All GPS Messages
unlog
gngga 1
gpgll 1
gpgsa 1
gpgsv 1
gnrmc 1
gpvtg 1
gpzda 1
gpgst 1
saveconfig

#enable all bands
UNMASK GPS
UNMASK BDS
UNMASK GLO
UNMASK GAL
UNMASK B1
UNMASK E5A
saveconfig

#ONOCOY RTCM CONFIGURATION
rtcm1006 30
rtcm1033 30
rtcm1077 1
rtcm1087 1
rtcm1097 1
rtcm1117 1
rtcm1127 1
saveconfig

# ONLY CHANGE IF YOU WANT TO IMPROVE THE BAUDRATE
# config com1 921600
# saveconfig
```

*It should be noted that the Unicorecomm device does not have the ability to transmit the `RTCM 1230` message type as required per [Onocoy system's requirements](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy).*

### Unicorecomm UM980 and UM982 Commands Reference Manuals
For additional configuration guidance, consult the following documentation:
- [UM980 / UM982 Commands Reference Manual](https://en.unicorecomm.com/assets/upload/file/Unicore_Reference_Commands_Manual_For_N4_High_Precision_Products_V2_EN_R1_1.pdf)
- [NebulasIV Commands Reference Manual](https://gnss.store/index.php?controller=attachment&id_attachment=255)

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
## Conclusion

Setting up your **own DIY GPS Onocoy server** doesn't have to be a daunting task. With the **right hardware choices**, **reliable GPS receivers**, and a clear understanding of the process, you can achieve **remarkable precision and accuracy** in your *location-based applications*.

By following the **step-by-step instructions** outlined in this guide, you've unlocked the potential to **enhance your navigation, positioning, and surveying** endeavors. The **affordable hardware options**, such as *Raspberry Pi* and *Intel NUC*, coupled with **accurate GPS receivers**, pave the way for **effortless and efficient server setup**.

So, **go ahead and set up your Onocoy Reference Station**, refine your skills, and enjoy the **results** that await you. Whether you're **navigating remote terrains**, conducting **surveys**, or exploring new possibilities, your **DIY Onocoy Reference Station** will be your **trusty companion** in the pursuit of **precision**.

Stay inspired, stay innovative, and keep pushing the **boundaries of what's possible with technology**.

Lastly, check out our article on more [low powered mining setups](https://simeononsecurity.com/other/creating-profitable-low-powered-crypto-miners/).

## References

- [German Federal Agency for Cartography and Geodesy (BKG)](https://www.bkg.bund.de/EN/Home/home.html)
- [NebulasIV Commands Reference Manual](https://gnss.store/index.php?controller=attachment&id_attachment=255)
- [Ntrip Server](https://software.rtcm-ntrip.org/browser/ntrip/trunk/ntripserver)
- [Onocoy - Get GNSS correction data](https://docs.onocoy.com/documentation/quick-start-guides/get-gnss-correction-data)
- [Onocoy - Connect your station to onocoy](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy)
- [RTKLIB](https://github.com/rtklibexplorer/RTKLIB/releases)
- [UM980 / UM982 Commands Reference Manual](https://en.unicorecomm.com/assets/upload/file/Unicore_Reference_Commands_Manual_For_N4_High_Precision_Products_V2_EN_R1_1.pdf)
- [Unicorecomm UPrecise](https://en.unicorecomm.com/download)
- [esp32-xbee](https://github.com/nebkat/esp32-xbee)
- [WhoLovesBurrito - Chinese UM980 Dongle Implementation](https://wholovesburrito.com/2023/09/25/an-affordable-diy-gnss-station-for-onocoy/)
