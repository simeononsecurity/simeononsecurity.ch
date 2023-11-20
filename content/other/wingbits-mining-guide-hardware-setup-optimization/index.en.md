---
title: "Effortless WingBits Mining Guide: Low-Cost and Optimized Hardware Setup"
date: 2023-12-14
toc: true
draft: false
description: "Achieve success with our guide on WingBits setup, hardware tips, and gain optimization. Start earning now with efficient, budget-friendly solutions!"
genre: ["Cryptocurrency Mining", "Hardware Setup", "ADSB Technology", "WingBits Guide", "Raspberry Pi", "Intel NUC", "Mining Optimization", "Tech How-To", "ADS-B Receivers", "Crypto Investment"]
tags: ["WingBits Mining", "Cryptocurrency Hardware", "ADS-B Technology", "Raspberry Pi Setup", "Intel NUC Guide", "Mining Optimization Tips", "Low-Cost Mining", "ADSB Receivers", "Crypto Investment Strategies", "Efficient Mining Solutions", "Cryptocurrency Tech", "WingBits Setup Tutorial", "Budget-Friendly Mining", "Digital Currency Tips", "Hardware Recommendations", "Crypto Market Insights", "Mining Power Efficiency", "Blockchain Technology", "ADS-B Antennas", "Mining Hardware Budget", "Crypto Market Volatility", "Tech How-To Guide", "Mining Location Optimization", "Crypto Enthusiast Tips", "Mining Gain Levels", "Cryptocurrency Investments", "ADS-B Filters", "Mining Location Setup", "WingBits and DeFli Dual Mining", "Investment Caution"]
cover: "/img/cover/WingBits-Mining-Optimization.png"
coverAlt: "Your Journey to WingBits Mining Success Begins!"
coverCaption: "Effortless Dual Mining"
ref: ["/other/effortless-dual-mining-wingbits-defli-guide", "/other/creating-profitable-low-powered-crypto-miners", "/other/adsb-sdr-adapter-performance-insights" ]
---

> **Note**: *This article does not entail an endorsement of wingbits nor does it contain any financial advice. Please do your own research. This article is for educational purposes only.*

## Introduction

Cryptocurrency mining continues to evolve, and the WingBits technology stack offers an accessible pathway for enthusiasts. In this guide, we'll explore the hardware requirements, ADSB-specific equipment, and step-by-step instructions for setting up your WingBits mining rig. Whether you're diving into mining for the first time or optimizing your current setup, this comprehensive guide will walk you through the process, from selecting the right hardware to fine-tuning gain levels. Let's embark on a journey to efficient and budget-friendly cryptocurrency mining with WingBits.

## About Flight Tracking

Flight tracking involves the use of small computers, typically Raspberry Pi, connected to a software-defined radio (SDR) USB stick operating at 1090 MHz. This setup, known as a feeder or ADS-B receiver, captures aircraft positions transmitted on 1090 MHz, primarily through Automatic Dependent Surveillance–Broadcast (ADS-B). The essential components for building such a device are detailed below.

### Unique Identifiers and Aircraft History

Each aircraft transmitting its position on 1090 MHz is assigned a unique hexadecimal identifier, such as ABA7D9. This identifier remains constant, allowing users to track the historical data for a specific airframe. For example, the US-registered aircraft N850FD corresponds to the hex ID ABA7D9. The [aircraft history](https://tar1090.adsbexchange.com/?icao=aba7d9) for N850FD includes details such as its current callsign (e.g., FDX5235), which may be associated with a city pair for certain airlines.

### Detailed Aircraft Information

By selecting an aircraft on the [ADS-B Exchange map](https://tar1090.adsbexchange.com/), users can access detailed information on the left side of the page. Tooltips are available to explain various displayed elements. Additionally, users can explore the aircraft's history by clicking on the history tab, revealing a colored line indicating its flight path. Timestamps, speed in knots, altitude in feet, and other details are displayed, providing a comprehensive overview of the aircraft's journey.

### Data Contribution and Real-Time Display

All the data presented on the ADS-B Exchange website is sourced from volunteers who have set up receivers, contributing real-time data. This data is collected and displayed on the online map, offering a collaborative and dynamic representation of aircraft movements globally.

### ADS-B Aircraft Categories

Flight tracking systems categorize ADS-B (Automatic Dependent Surveillance–Broadcast) equipped aircraft based on specific characteristics. These categories provide insights into the type and size of the aircraft, aiding in the identification and classification of air traffic. Here are the defined ADS-B aircraft categories:

- **A-**: Unspecified powered aircraft
- **A1**: Light (< 15,500 lbs.)
- **A2**: Small (15,500 to 75,000 lbs.)
- **A3**: Large (75,000 to 300,000 lbs.)
- **A4**: High Vortex Large (e.g., B-757)
- **A5**: Heavy (> 300,000 lbs.)
- **A6**: High Performance (> 5g acceleration and > 400kts)
- **A7**: Rotorcraft
- **B-**: Unspecified unpowered aircraft, UAV, or spacecraft
- **B1**: Glider/sailplane
- **B2**: Lighter-than-Air
- **B3**: Parachutist/Skydiver
- **B4**: Ultralight/hang-glider/paraglider
- **B5**: Reserved
- **B6**: Unmanned Aerial Vehicle (UAV)
- **B7**: Space/Trans-atmospheric vehicle
- **C-**: Unspecified ground installation or vehicle
- **C1**: Surface Vehicle - Emergency Vehicle
- **C2**: Surface Vehicle - Service Vehicle
- **C3**: Fixed Ground or Tethered Obstruction

## Hardware Requirements:
### System Requirements:
One of the following is required. We basically just need any efficient and low powered computer we can get our hands on. Any Raspberry PI, Intel NUC, or similar will do. They don't have to be all that powerful. However I will recommend you have at least 32g-64g of storage, 4g of ram, and at least 2 cpu threads. For this we will be targeting a budget of around $100-$200 for hardware but feel free to go higher if it suits your needs. Our power target is 25w or better on average.
#### Raspberry Pi:
Hard to get ahold of these days but they are super low power and are quite customizable. 

{{< centerbutton href="https://amzn.to/3x72kv0" >}}Get your Raspberry Pi 4B today! {{< /centerbutton >}}

- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
#### Intel Nuc:
Wide variety of models out there. Feel Free to choose a newer one.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
#### Any Mini PC with Intel N5100 or similar
For super low power Raspberry Pi equivalent but on x64 platform. 
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)
### ADSB Specific Equipment:
#### ADSB Receivers
We go into this in much greater detail in our [Guide on Best ADSB RTL-SDR Recievers](https://simeononsecurity.com/other/adsb-sdr-adapter-performance-insights/)

{{< centerbutton href="https://amzn.to/3QIRhBV" >}}Get your AirNav Radarbox Flightstick today!{{< /centerbutton >}}

- (**Preferred**)[AirNav Radarbox Flightstick](https://amzn.to/3QIRhBV)
- [ADSBexchange.com Blue R820T2 RTL2832U](https://amzn.to/3M7AwPd)
#### ADSB Antennas
- (**Preferred**)[AirNav RadarBox ADS-B Antenna](https://amzn.to/496LcHN)
- [SIGNALPLUS 1090MHz ADS-B Antenna](https://amzn.to/3FsGaaY)
- [1090MHz 978MHz Dual Band ADS-B Antenna](https://amzn.to/3QsOrlA)
#### Optional Extras
*The ADSB receivers linked above have LNA and Filters built in. Only consider using a LNA or Filters if you have a non specific SDR*
- [Nooelec SAWbird+ ADS-B: Premium, Dual-Channel, Cascaded Ultra-Low Noise Amplifier (LNA) & Filter Module for Airplane Tracking Applications. ](https://amzn.to/4737k3T)
##### Band Pass and SAW Filters
- (**Preferred**)[ADSBexchange.com 1090 Mhz Saw Filter ](https://amzn.to/3MewiFB)
- [1090MHz Band Pass Filter, Saw Band Pass Filter](https://amzn.to/3McmZFQ)
##### Low Noise Amplifiers
- (**Preferred**)[Nooelec Lana - Ultra Low-Noise Amplifier (LNA)](https://amzn.to/3FsEAWv)
- [Low Noise Amplifier 20dB High Gain](https://amzn.to/3FpF27S)
##### SMA Pigtails
- [2 Pack 6inch SMA to SMA Adapter Cable](https://amzn.to/3QcUHwa)
- [5pcs RF Coaxial Coax SMA Male to SMA Male](https://amzn.to/494WOeh)

## OS Installation:
We won't go into the technical details of how to install an operating system here. However here are some great resources to get you started.
### Raspbian:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)

## Setup Instructions for Installing WingBits

Wingbits technology stack currently operates like this.

 `readsb` -> `vector` -> `wingbits`

To get started is simple, just follow these steps:

### 1. Run the WingBits setup script by using the command:
```bash
curl -sL https://gitlab.com/wingbits/config/-/raw/master/download.sh | sudo bash
```
> **Note**: *Make sure you have your device ID, which you can find in your original WingBits email or on the [WingBits dashboard](https://wingbits.com).*

### **2: Setting Up Your Location**
Setting your mining location is crucial. Use tools like [LatLong.net](https://www.latlong.net/convert-address-to-lat-long.html) to find the coordinates for your installation site. Replace the example coordinates with your own:
```bash
sudo readsb-set-location 50.12344 10.23429
```

### **3: Optimizing Gain Levels**
Now, it's time to optimize your receiver's gain levels. Run the following command, if it fails, come back to this step after a few minutes.

```bash
sudo bash -c "$(curl -L -o - https://github.com/wiedehopf/adsb-scripts/raw/master/autogain-install.sh)" hash -r
sudo autogain1090
# Run ever 2 minutes, in the background, for an hour to optimize gain even further
sudo for i in {0..30}; do sudo autogain1090; sleep 120; done &
```

## Troubleshooting and Helpful Commands

### Configuring Location in readsb for ADS-B Reception

**Introduction:**

Properly configuring the location is essential for accurate ADS-B data reception. This guide outlines the steps to configure the location in readsb on a Raspberry Pi. Additionally, it provides troubleshooting tips and information on changing the configuration.

---

#### Configure Location:

To set the location, use the following command with the specified latitude and longitude:

```bash
sudo readsb-set-location 50.12344 10.23429
```

Alternatively, use the full path to readsb-set-location:

```bash
sudo /usr/local/bin/readsb-set-location 50.12344 10.23429
```

---

#### Troubleshooting and Checking Logs:

If any issues arise, check the readsb logs using the following command:

```bash
sudo journalctl --no-pager -u readsb
```

If problems persist, try rebooting and rerunning the install script.

---

#### Reporting Issues:

- If issues persist, consider opening a GitHub issue with the provided logs and install script output.
- Alternatively, report issues via Discord by contacting wiedehopf [here](https://discord.gg/DxU4VG37JS).

---

#### Changing Configuration:

To modify readsb configuration, use a text editor such as nano:

```bash
sudo nano /etc/default/readsb
```

Make the necessary changes, save with Ctrl-O and Enter, then exit with Ctrl-X. Afterward, restart the readsb service:

```bash
sudo systemctl restart readsb
```

For a comprehensive list of available options, refer to the readsb help command:

```bash
readsb --help
```

---

**Conclusion:**

Configuring the location is a critical step in optimizing ADS-B reception with readsb. Following these steps ensures accurate data and provides troubleshooting avenues for any potential issues.

______

### Debug Commands for ADS-B Setup

**Introduction:**

Debugging is an essential aspect of maintaining an ADS-B setup on a Raspberry Pi. This guide provides various debug commands for different components, ensuring the smooth operation of readsb, dump1090-fa, and related services.

---

#### Lighttpd Debug Commands:

- View lighttpd logs:
  ```bash
  sudo journalctl --no-pager -u lighttpd
  ```

- List enabled lighttpd configurations:
  ```bash
  ls /etc/lighttpd/conf-enabled 
  ```

---

#### dump1090-fa Debug Command:

- View dump1090-fa logs:
  ```bash
  sudo journalctl --no-pager -u dump1090-fa
  ```

---

#### Test the RTL-SDR Receiver:

To test the RTL-SDR receiver, run the following command:
  ```bash
  sudo bash -c "$(wget -q -O - https://raw.githubusercontent.com/wiedehopf/adsb-scripts/master/rtl_test.sh)"
  ```

---

### Optimizing Gain for ADS-B Reception with readsb

**Introduction:**

Receiving and decoding ADS-B signals on a Raspberry Pi using readsb involves optimizing the gain settings to achieve optimal performance. This article provides a detailed guide for both automatic and manual gain optimization methods.

---

#### Automatic Method:

1. **Check Percentage of Strong Messages:**
   Use the following command to obtain the percentage of strong messages:
   ```bash
   grep -sh /run/{dump1090,dump1090-fa,readsb}/stats.json -e '' | jq '.total.local | ((.accepted | add), .strong_signals, .signal, .noise)' | xargs -n4 echo | awk '{printf "\nPercentage of strong messages: %.3f\nSignal: %.1f\nNoise: %.1f\n", $(2) * 100 / $(1), $(3), $(4)}'
   ```

2. **Adjust Gain Based on Percentage:**
   - Percentages from 0.5% to 5% are recommended.
   - Experiment until an optimal value is found.
   - If using graphs1090, adjust gain so the weakest signal is between -25 to -30 dBFS.

---

#### Manual Method:

1. **Check Percentage After Waiting:**
   After waiting at least 5 minutes, check the percentage using the command mentioned in the automatic method.

2. **Adjust Gain:**
   - If the percentage is too high, reduce the gain.
   - If too low, increase it. Aim for around 2% if unsure.

3. **Available Gain Settings:**
   ```
   0.0 0.9 1.4 2.7 3.7 7.7 8.7 12.5 14.4 15.7 16.6 19.7 20.7 22.9 25.4
   28.0 29.7 32.8 33.8 36.4 37.2 38.6 40.2 42.1 43.4 43.9 44.5 48.0 49.6
   -10
   ```

4. **Using AGC (Automatic Gain Control):**
   - A gain of -10 turns on AGC, resulting in the maximum possible gain for ADS-B.
   - Repeat the process until a suitable gain value is found.

5. **Caution on Maximum Range:**
   - If aiming for maximum range, be cautious about setting the gain too high.
   - Amplifying noise may not result in extra range.

6. **Check Back After a Day or Two:**
   - After adjustments, check back after a day or two to get a more precise percentage.
   - The percentage is only reset when dump1090 is restarted.

---

**Conclusion:**

Optimizing gain settings is crucial for achieving optimal ADS-B reception on a Raspberry Pi using readsb. Whether using the automatic or manual method, users can fine-tune their settings based on their specific environment and preferences, ensuring reliable and efficient aircraft tracking.

### Activating RTL Bias Tee with readsb and dump1090-fa

**Introduction:**

Activating the RTL Bias Tee is a crucial step in enhancing the performance of your ADS-B setup when using readsb or dump1090-fa on a Raspberry Pi. This guide provides instructions on enabling and disabling the Bias Tee while the readsb/dump1090-fa service is running.

---

#### Enabling Bias Tee:

To enable the Bias Tee while the readsb or dump1090-fa service is running, use the following script:

```bash
curl https://raw.githubusercontent.com/wiedehopf/adsb-scripts/master/biastee-enable.sh | sudo bash
```

This script facilitates the activation of the Bias Tee, ensuring that your RTL-SDR device receives power through the coaxial cable.

---

#### Disabling Bias Tee:

In cases where automatic Bias Tee enabling is not desired, use the following script to disable it:

```bash
curl https://raw.githubusercontent.com/wiedehopf/adsb-scripts/master/biastee-disable.sh | sudo bash
```

Disabling the automatic Bias Tee enables users to have more control over the powering of their RTL-SDR device.

**Note:** These scripts roughly follow the method outlined [here](https://www.rtl-sdr.com/getting-the-v3-bias-tee-to-activate-on-piaware-ads-b-images/).

---

### Displaying RSSI Signal Strength Column in dump1090-fa Web Interface

**Introduction:**

By default, the RSSI (Received Signal Strength Indicator) column in the dump1090-fa web interface table is hidden when the map is displayed. This guide provides instructions on how to modify the configuration to always display the RSSI column, enhancing visibility and providing valuable signal strength information.

---

#### Modification Commands:

To always show the RSSI column in the dump1090-fa web interface, execute the following command:

```bash
sudo sed -iE -e 's/showColumn(infoTable, "#rssi"/\/\/showColumn(infoTable, "#rssi"/g' /usr/share/dump1090-fa/html/script.js
```

To revert the change and hide the RSSI column only when the map is displayed, use the following command:

```bash
sudo sed -iE -e 's/\/*showColumn(infoTable, "#rssi"/showColumn(infoTable, "#rssi"/g' /usr/share/dump1090-fa/html/script.js
```

If you prefer using an editor to make these changes:

1. Locate the following line (Line 1573 in version 3.6.3):
   ```javascript
   showColumn(infoTable, "#rssi", !mapIsVisible);
   ```

2. Add `//` at the beginning of the line to always show the RSSI column:
   ```javascript
   //showColumn(infoTable, "#rssi", !mapIsVisible);
   ```

---

**Conclusion:**

Enhancing the dump1090-fa web interface by always displaying the RSSI column provides valuable insight into signal strength. These modification commands offer a straightforward way to customize the interface based on user preferences.

______

### Automatic Reboot on Internet Connection Failure with pingfail

**Introduction:**

Ensuring a stable internet connection is crucial for the continuous operation of ADS-B setups. This guide introduces pingfail, a tool that automatically reboots the computer when the internet connection is lost for an extended period. This helps maintain a reliable connection and prevents interruptions in data reception.

---

#### Installation:

To install pingfail and set up automatic reboots on internet connection failure, use the following command:

```bash
sudo bash -c "$(wget -q -O - raw.githubusercontent.com/wiedehopf/adsb-scripts/master/pingfail-install.sh)"
```

**Note:** This installation is configured to reboot the computer if the internet is unreachable for at least 5 minutes.

---

#### Deactivation:

To deactivate pingfail and stop automatic reboots, use the following command:

```bash
sudo systemctl disable --now pingfail
```

**Note:** Deactivating pingfail is recommended if you encounter issues or want to temporarily suspend automatic reboots.

---

**Conclusion:**

pingfail provides a simple yet effective solution for maintaining a stable internet connection for ADS-B setups. By automatically rebooting the computer in the event of extended internet unavailability, users can ensure continuous data reception and minimize downtime.

______


## Conclusion

Congratulations on completing the setup of your WingBits mining system! By now, you've configured your hardware, fine-tuned your ADSB receiver, and optimized gain levels for maximum efficiency. Remember, cryptocurrency mining requires careful consideration of hardware, location, and market volatility. Always stay informed and adapt your strategy as needed. With your WingBits mining rig up and running, you're well-positioned to explore the exciting world of digital currency. Happy mining!

If you've made it this far, you might like to know you can actually dual mine [Wingbits](https://wingbits.com) and [Defli](https://defli.network/maclinux), read our [Guide on How to Dual Mine Wingbits and Defli](https://simeononsecurity.com/other/effortless-dual-mining-wingbits-defli-guide).

{{< centerbutton href="https://simeononsecurity.com/other/effortless-dual-mining-wingbits-defli-guide" >}}Read our Guide on How to Dual Mine Wingbits and Defli{{< /centerbutton >}}


______

### **References**
Here are some helpful links for reference:
- [WingBits](https://wingbits.com/#alpha)
- [DeFli](https://defli.network/maclinux)
- [readsB GitHub](https://github.com/wiedehopf/adsb-scripts)
- [graphs1090 Documentation](https://github.com/wiedehopf/graphs1090)
- [jq Command-Line JSON Processor](https://stedolan.github.io/jq/)
- [ADS-B Reception on Raspberry Pi](https://www.rtl-sdr.com/adsb-aircraft-radar-with-rtl-sdr/)
- [RTL-SDR Bias Tee Activation](https://www.rtl-sdr.com/getting-the-v3-bias-tee-to-activate-on-piaware-ads-b-images/)
- [RTL-SDR Receiver Test](https://github.com/wiedehopf/adsb-scripts/blob/master/rtl_test.sh)
