---
title: "WingBits Install and Setup Guide"
date: 2023-12-14
toc: true
draft: false
description: "Achieve success with our guide on WingBits setup, hardware tips, and gain optimization. Start earning now with efficient, budget-friendly solutions!"
genre: ["Cryptocurrency Mining", "Hardware Setup", "ADSB Technology", "WingBits Guide", "Raspberry Pi", "Intel NUC", "Mining Optimization", "Tech How-To", "ADS-B Receivers", "Crypto Investment", "Wingbits"]
tags: ["WingBits Mining", "WingBits Setup", "Cryptocurrency Hardware", "ADS-B Technology", "Raspberry Pi Setup", "Intel NUC Guide", "Mining Optimization Tips", "Low-Cost Mining", "ADSB Receivers", "Crypto Investment Strategies", "Efficient Mining Solutions", "Cryptocurrency Tech", "WingBits Setup Tutorial", "Budget-Friendly Mining", "Digital Currency Tips", "Hardware Recommendations", "Crypto Market Insights", "Mining Power Efficiency", "Blockchain Technology", "ADS-B Antennas", "Mining Hardware Budget", "Crypto Market Volatility", "Tech How-To Guide", "Mining Location Optimization", "Crypto Enthusiast Tips", "Mining Gain Levels", "Cryptocurrency Investments", "ADS-B Filters", "Mining Location Setup", "WingBits and DeFli Dual Mining", "Investment Caution"]
cover: "/img/cover/WingBits-Mining-Optimization.png"
coverAlt: "Your Journey to WingBits Mining Success Begins!"
ref: ["/other/effortless-dual-mining-wingbits-defli-guide", "/other/creating-profitable-low-powered-crypto-miners", "/other/adsb-sdr-adapter-performance-insights" ]
---

> **Note**: *This article does not contain or entail an endorsement of wingbits nor does it contain any financial advice. Please do your own research. This article is for educational purposes only.*

## Introduction

Cryptocurrency mining continues to evolve, and the WingBits technology stack offers an accessible pathway for enthusiasts. In this guide, we'll explore the hardware requirements, ADSB-specific equipment, and step-by-step instructions for setting up your WingBits mining rig. Whether you're diving into mining for the first time or optimizing your current setup, this comprehensive guide will walk you through the process, from selecting the right hardware to fine-tuning gain levels. Let's embark on a journey to efficient and budget-friendly cryptocurrency mining with WingBits.

{{< centerbutton href="https://simeononsecurity.com/other/wingbits-mining-guide-hardware-setup-optimization/#wingbits-hardware-requirements" >}}WingBits Hardware Requirements{{< /centerbutton >}}
{{< centerbutton href="https://simeononsecurity.com/other/wingbits-mining-guide-hardware-setup-optimization/#setup-instructions-for-installing-wingbits" >}}WingBits Setup Instructions{{< /centerbutton >}}

______

## The WingBits SkyHex: Revolutionizing ADS-B Data Coverage

#### WingBits Core Values

WingBits positions itself as a provider of flight tracking data feeds, catering to both live and historic flights. This valuable resource becomes instrumental for developers seeking real-time aircraft data integration into their applications. The clientele spans across various sectors, encompassing aviation companies, emergency services, and even aviation enthusiasts.

#### WingBitsCoverage - SkyHex

WingBits sets an ambitious target: global coverage. The innovative SkyHex system, inspired by air rights and leveraging Uber's h3 hex system, divides the global airspace into hexagons. This unique approach grants antennas exclusive rights to monitor specific sections of the sky, ensuring meticulous observation for enhanced air traffic management and safety.

#### WingBits Details

- **SkyHex NFT Ownership:** Antennas require a SkyHex NFT for full rewards, aligning with an ownership model reminiscent of air rights, while still rewarding, minimally, those without an NFT to promote redundant coverage.

- **Maximizing Coverage:** Multiple antennas within the same hex maximize coverage, with most of the rewards ideally based on unique data contributions.

- **Limited Supply:** With a maximum supply of [current maximum supply], exclusivity and scarcity are maintained.

- **Reclaiming Inactivity:** Inactive antennas for 30 days face NFT reclamation, exceptions granted for technical issues.

- **Transferability:** SkyHex NFTs can be sold or transferred after 30 days of use, introducing dynamism to the digital asset marketplace.

- **Penalties for Delays:** Slow antennas facing delays over 1 minute incur a 25% reward reduction for each minute compared to other hex owners.

Explore more about SkyHex [here](https://medium.com/@wingbits/%EF%B8%8Fa-world-of-hexes-4927fc304ba4).

______

### WingBits Rewards: An Overview of Participation Options

Before deciding on Core Network participation, please review the details provided below.

#### Supporter Network (default):

- **Open and Inclusive Participation:** The Supporter Network welcomes all participants without any associated charges. Every project member is automatically considered a Supporter.

- **Reward Structure:** Supporters receive rewards based on the percentage of messages they contribute for each hex, fostering an inclusive environment where all participants are eligible for rewards based on their data contributions.

#### Core Network (optional - $20/hex):

- **Enhanced Rewards for Hex Owners:** Core participants, who are hex owners, receive additional rewards on top of the regular rewards. This additional pool compensates for their investment in hex ownership, maintenance, and adherence to contribution standards.

- **Reward Calculation:** Core members are rewarded based on their message contribution percentage and system uptime for a hex. They also participate in Supporter network rewards, allowing them to benefit from both Core and Supporter reward pools for each hex they contribute data against.

- **Participation Cap:** The Core network maintains a maximum limit of three owners per hex, aligning with current Skyhex ownership rules.

- **Optimized Setups/Coverage:** Core participants are expected to play a crucial role in forming a robust project network. Their optimized setups and coverage contribute to the overall efficiency of the network, driven by the incentive of higher rewards and additional perks.

#### Examples of Reward Distribution:

*Note: Examples use a placeholder base rewards of 50 tokens. Exact base rewards have not been defined at this time. Examples assume all contributors provide equal data volume and equal uptime (for easier examples).*

| Example | Description | Core Participant Wings | Supporter Wings |
|---------|-------------|------------------------|-----------------|
| 1       | One Supporter covering a hex | N/A | 50 Wings |
| 2       | One Supporter and One Core participant covering a hex | 75 Wings (50 Core rewards + 25 Normal rewards) | 25 Wings |
| 3       | Two Supporters and Two Core participants covering a hex | 62.5 Wings each (50 Core rewards + 12.5 Normal rewards) | 12.5 Wings each |
| 4       | One Core participant covering a hex | 100 Wings (50 Core rewards + 50 Normal rewards) | N/A |

For more details on the formulas used in the examples, please refer to the [Supporter & Core Network Participation documentation](https://docs.wingbits.com/introduction/supporter-and-core-network-participation).

#### Additional Notes:

- Core network membership offers additional perks beyond what is available to Supporter Network members.
- Core network participants are expected to meet minimum standards in terms of uptime and data contribution for each hex they own.
- Supporter and Core network participation aims to build a more robust and efficient network by encouraging high-quality data coverage and appropriately rewarding both casual contributors and dedicated hex owners.

______

### Addressing WingBits Concerns: Ensuring Significance and Fairness

WingBits proactively acknowledges and addresses concerns related to the [fairness of ADS-B data monetization](https://hackaday.com/2023/01/26/ads-b-exchange-sells-up-contributors-unhappy/).

#### WingBits' Significance

WingBits' significance lies in offering a decentralized model that fairly rewards contributors. This ensures the authenticity and timeliness of ADS-B data, contributing to the efficiency and safety of the aviation industry.

#### WingBits' Fairness and Sufficiency

WingBits implements fairness through penalties for slow antennas, promoting active and responsive participation. The sufficiency of the model is evident in the transparent and equitable distribution of Wings, fostering a collaborative ecosystem.

## WingBits Hardware Requirements:

### Our Recommended WingBits Hardware Configuration

**Our Ideal Setup for WingBits Flight Tracking**

For aviation enthusiasts or those keen on monitoring aircraft movements, we recommend an ideal setup that combines the versatility of the Raspberry Pi 4B Model B DIY Kit with specialized components for ADS-B reception. The Raspberry Pi DIY Kit is perfect for enthusiasts seeking a customizable computing solution. Paired with the AirNav Radarbox Flightstick and SIGNALPLUS 1090MHz ADS-B Antenna, this setup ensures optimal performance, features, and reliability for accurate and detailed flight tracking.

| Model                                                                                                             | Description                                                                                         |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3x72kv0" >}}Raspberry Pi 4B Model B DIY Kit{{< /centerbutton >}}           | Consider this DIY kit for Raspberry Pi enthusiasts looking for a versatile and customizable computing solution.                                                  |
| {{< centerbutton href="https://amzn.to/3QIRhBV" >}}AirNav Radarbox Flightstick{{< /centerbutton >}}               | **Preferred Option:** With optimal performance and features, the AirNav Radarbox Flightstick is our top recommendation for ADS-B reception, ensuring reliable and accurate flight tracking.                                          |
| {{< centerbutton href="https://amzn.to/3SUgB99" >}}SIGNALPLUS 1090MHz ADS-B Antenna 5.5DB{{< /centerbutton >}}         | **Preferred Option:** The SIGNALPLUS 1090MHz ADS-B Antenna is our top recommendation, offering excellent performance and reliability for ADS-B reception, ensuring accurate and detailed flight tracking.                              |

> **Note:** Don't go for an antenna higher than 6 db unless you know specifically you need it. For wingbits you should optimize for reliable coverage, not distance. 

### WingBits System Requirements and Recommendations:
One of the following is required. We basically just need any efficient and low powered computer we can get our hands on. Any Raspberry PI, Intel NUC, or similar will do. They don't have to be all that powerful. However I will recommend you have at least 32g-64g of storage, 4g of ram, and at least 2 cpu threads. For this we will be targeting a budget of around $100-$200 for hardware but feel free to go higher if it suits your needs. Our power target is 25w or better on average.

{{< figure src="compute.jpeg" alt="Wingbits Compute Hardware" link="https://amzn.to/45IW4ZD" >}}

| Model                                                                                                              | Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3x72kv0" >}}Raspberry Pi 4B Model B DIY Kit{{< /centerbutton >}}            | Consider this DIY kit for Raspberry Pi enthusiasts looking for a versatile and customizable computing solution.                                               |
| {{< centerbutton href="https://amzn.to/3jG2g2k" >}}GeeekPi Raspberry Pi 4 4GB Starter Kit{{< /centerbutton >}}     | A ready-to-go starter kit for Raspberry Pi 4, suitable for those who prefer a convenient setup with moderate power.                                               |
| {{< centerbutton href="https://amzn.to/3DQisF6" >}}GeeekPi Raspberry Pi 4 8GB Starter Kit{{< /centerbutton >}}     | Similar to the 4GB kit but with more RAM, ideal for users with higher performance requirements on the Raspberry Pi 4.                                              |
| {{< centerbutton href="https://amzn.to/3YkFhcj" >}}Beelink U59 Mini PC{{< /centerbutton >}}                      | For those seeking a Raspberry Pi equivalent on an x64 platform, the Beelink U59 Mini PC offers a low-power alternative.                                             |
| {{< centerbutton href="https://amzn.to/3XkbXkS" >}}TRIGKEY Mini Computer{{< /centerbutton >}}                    | Another option for an x64 platform, the TRIGKEY Mini Computer provides a compact and efficient computing solution.                                                |

### ADSB Specific Equipment:
#### ADSB Receivers for WingBits
We go into this in much greater detail in our [Guide on Best ADSB RTL-SDR Recievers](https://simeononsecurity.com/other/adsb-sdr-adapter-performance-insights/)

{{< figure src="adsbreceiver.png" alt="AirNav RadarBox FlightStick Best ADSB Receiver for Wingbits" link="https://amzn.to/3FSSql1" >}}

| Model                                                                                                              | Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3QIRhBV" >}}AirNav Radarbox Flightstick{{< /centerbutton >}}            | **Preferred Option:** With optimal performance and features, the AirNav Radarbox Flightstick is our top recommendation for ADS-B reception, ensuring reliable and accurate flight tracking.                                               |
| {{< centerbutton href="https://amzn.to/3M7AwPd" >}}ADSBexchange.com Blue R820T2 RTL2832U{{< /centerbutton >}}  | An alternative option for ADS-B reception, the ADSBexchange.com Blue R820T2 RTL2832U provides an affordable solution for flight tracking.                                              |
#### ADSB Antennas for WingBits
| Model                                                                                                              | Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/496LcHN" >}}AirNav RadarBox ADS-B Antenna{{< /centerbutton >}}          | A reliable option for ADS-B reception, the AirNav RadarBox ADS-B Antenna provides solid performance for flight tracking applications.                                               |
| {{< centerbutton href="https://amzn.to/3FsGaaY" >}}SIGNALPLUS 1090MHz ADS-B Antenna{{< /centerbutton >}}      | **Preferred Option:** The SIGNALPLUS 1090MHz ADS-B Antenna is our top recommendation, offering excellent performance and reliability for ADS-B reception, ensuring accurate and detailed flight tracking.                                              |
| {{< centerbutton href="https://amzn.to/3QsOrlA" >}}1090MHz 978MHz Dual Band ADS-B Antenna{{< /centerbutton >}} | A dual-band option for ADS-B reception, the 1090MHz 978MHz Dual Band ADS-B Antenna provides flexibility for users interested in both frequency bands for flight tracking.                                                |
#### Optional Extras for WingBits
*The ADSB receivers linked above have LNA and Filters built in. Only consider using a LNA or Filters if you have a non specific SDR*
##### Nooelec SAWbird+ ADS-B
| Model                                                                                                              | Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/4737k3T" >}}Nooelec SAWbird+ ADS-B{{< /centerbutton >}}                 | A premium, dual-channel, cascaded ultra-low noise amplifier (LNA) and filter module designed for airplane tracking applications.                                             |

##### Band Pass and SAW Filters for WingBits
| Model                                                                                                              | Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3MewiFB" >}}ADSBexchange.com 1090 Mhz Saw Filter{{< /centerbutton >}}   | **Preferred Option:** The ADSBexchange.com 1090 Mhz Saw Filter is our top recommendation, providing optimal filtering for ADS-B reception in WingBits setups.                                              |
| {{< centerbutton href="https://amzn.to/3McmZFQ" >}}1090MHz Band Pass Filter{{< /centerbutton >}}               | A band pass filter designed for 1090MHz, the 1090MHz Band Pass Filter is suitable for WingBits applications requiring precise frequency filtering.                          |

##### Low Noise Amplifiers for WingBits
| Model                                                                                                              | Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3FsEAWv" >}}Nooelec Lana - Ultra Low-Noise Amplifier (LNA){{< /centerbutton >}} | **Preferred Option:** The Nooelec Lana LNA is our top recommendation for WingBits setups, offering ultra-low noise and high gain for enhanced ADS-B reception.                          |
| {{< centerbutton href="https://amzn.to/3FpF27S" >}}Low Noise Amplifier 20dB High Gain{{< /centerbutton >}}       | A high-gain low noise amplifier suitable for WingBits setups, providing improved signal reception for ADS-B tracking.                                              |

##### SMA Pigtails for WingBits
| Model                                                                                                              | Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3QcUHwa" >}}2 Pack 6inch SMA to SMA Adapter Cable{{< /centerbutton >}} | A set of two 6-inch SMA to SMA adapter cables, facilitating connectivity in WingBits configurations.                                                        |
| {{< centerbutton href="https://amzn.to/494WOeh" >}}5pcs RF Coaxial Coax SMA Male to SMA Male{{< /centerbutton >}}| A pack of five RF coaxial SMA male to SMA male cables, providing versatility and flexibility for SMA connections in WingBits setups.                                 |

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

{{< figure src="wingbits-website.webp" alt="Wingbits Home Page" caption="Wingbits Home Page" link="https://wingbits.com/" >}}

Wingbits technology stack currently operates like this.

 `readsb` -> `vector` -> `wingbits`

To get started is simple, just follow these steps:

### 1. Run the WingBits setup script by using the command:
```bash
curl -sL https://gitlab.com/wingbits/config/-/raw/master/download.sh | sudo bash
```
> **Note**: *Make sure you have your `device ID`/`antenna name`, which you can find in your original WingBits email or on the [WingBits dashboard](https://wingbits.com).*

### **2: Setting Up Your Location**
Setting your mining location is crucial. Use tools like [LatLong.net](https://www.latlong.net/convert-address-to-lat-long.html) to find the coordinates for your installation site. Replace the example coordinates with your own:
```bash
sudo readsb-set-location 50.12344 10.23429
```

### **3: Optimizing Gain Levels**

> **Note**: Read the Troubleshooting and Helpful Commands section below on how to set the gain levels more optimally.
> **Note**: **The WingBits community has specifically recommended to not use the autogain script**, mentioning issues with some receivers and issues with the script setting the gain too low. Read below for instructions on [how to set the readsb gain manually](https://simeononsecurity.com/other/wingbits-mining-guide-hardware-setup-optimization/#tuning-ads-b-gain-for-optimal-performance-for-wingbits).

Now, it's time to optimize your receiver's gain levels. Run the following command, if it fails, come back to this step after a few minutes.

```bash
# sudo bash -c "$(curl -L -o - https://github.com/wiedehopf/adsb-scripts/raw/master/autogain-install.sh)" hash -r
# sudo autogain1090
# Run ever 2 minutes, in the background, for an hour to optimize gain even further
# sudo for i in {0..30}; do sudo autogain1090; sleep 120; done &
```


### **4. Profit?**

At this point you're done. Sit back and relax.
However if you discover you are running into issues, or you'd like to learn more, read below.

______

## Troubleshooting and Helpful Commands for WingBits

### Tuning ADS-B Gain for Optimal Performance for WingBits

Understanding how to adjust the gain on your ADS-B receiver is crucial for optimizing performance and ensuring accurate data reception. Here's a step-by-step guide on tuning the gain for your system.

#### **Overview of Gain and its Analogy**

Gain, analogous to volume in audio terms, plays a pivotal role in receiving ADS-B signals. Similar to turning up the volume, increasing gain amplifies signals, but at a certain point, it can lead to distortion and signal loss.

#### **Avoiding Autotune and Checking Current Gain**

**Autotune is not recommended** for quick and precise gain adjustments. To view your current gain, check the "Misc" section in the graphs1090 interface. The gain value is displayed here.

#### **Changing Gain Manually**

Adjusting gain is straightforward and can be done using the Terminal. Enter the following command, replacing "xx.x" with your desired gain:

```bash
sudo readsb-gain xx.x
```

Available gain settings are limited to specific values. If you input a different value, it will snap to the nearest valid gain from the following list:

```python
0.0 0.9 1.4 2.7 3.7 7.7 8.7 12.5 14.4 15.7 16.6 19.7 20.7 22.9 25.4
28.0 29.7 32.8 33.8 36.4 37.2 38.6 40.2 42.1 43.4 43.9 44.5 48.0 49.6 -10
```

#### **Real-Time Gain Read and Verification**

For a real-time gain read over a specific time period since `readsb` started, use the following command:

```bash
grep -sh /run/{dump1090,dump1090-fa,readsb}/stats.json -e '' | jq '.total.local | ((.accepted | add), .strong_signals, .signal, .noise)' | xargs -n4 echo | awk '{printf "\nPercentage of strong messages: %.3f\nSignal: %.1f\nNoise: %.1f\n", $(2) * 100 / $(1), $(3), $(4)}'
```

This command provides crucial information such as the percentage of strong messages, signal strength, and noise level.

In the command you can change `.total.local` to any of the options below to get more recent data, if needed.

- `last1min `
- `last5min `
- `last15min`

#### **Verifying Gain Impact on Range**

To ensure your adjusted gain doesn't compromise range, utilize the ADS-B Range graph on the `x.x.x.x/graphs1090` page. Confirm that you're still receiving an adequate range even as you modify the gain.

{{< figure src="adsb-range.webp" alt="graphs1090 ADS-B Range Graph" caption="The number you should care about is Avg Max Range" >}}

#### **ADS-B Analysis with Dirk Beer**

For more detailed analysis, Dirk Beer's Python script can assess your range by assuming that aircraft will transmit again. Running Dirk's scripts helps evaluate the impact of gain adjustments on reception range.

The script provides easy to understand graphs to help you determine your maximum reliable range.

{{< figure src="adsb-range-graph.webp" alt="DirkBeer ADSB Script for tar1090 ADS-B Range Graph" caption="Average ADS-B Receiver Performance Graph for Indoor Setups." >}}

It is based on the theory that probability of detection P(D) of an aircraft's message in the current 8-second measurement interval, given that that the aircraft's message was received in the previous interval.

**Note**: Specific goals for ADS-B reception may vary, and striking a balance between maximum range, minimal "too hot" messages, and maximum aircraft reception is recommended.

**Setup Script**
```bash
curl -sSL https://raw.githubusercontent.com/dirkbeer/adsb-analysis/main/setup.sh | sudo bash
```
**Analysis Script**
```bash
sudo ~/adsb-analysis/run_analysis.sh
```

{{< figure src="adsb-range-graph-script-output.webp" alt="DirkBeer ADSB Script for tar1090 ADS-B Example Output" caption="Example Script Output" >}}

##### **Further Exploration with Dirk Beer's Scripts**

For an in-depth ADS-B analysis, Dirk Beer's scripts, available on his [GitHub](https://github.com/dirkbeer/adsb-analysis), provide additional insights into your system's range and reception capabilities. Running these scripts can complement the information obtained from other Python scripts.

Optimizing ADS-B gain involves continuous adjustment and monitoring, allowing you to tailor your setup for optimal performance based on your specific preferences and goals. Experimenting with gain levels and analyzing the impact on reception metrics is key to achieving the best results.

______

### Configuring Location in readsb for ADS-B Reception and for WingBits

**Introduction:**

Properly configuring the location is essential for accurate ADS-B data reception. This guide outlines the steps to configure the location in readsb on a Raspberry Pi. Additionally, it provides troubleshooting tips and information on changing the configuration.

---

#### Configure Location for WingBits:

To set the location, use the following command with the specified latitude and longitude:

```bash
sudo readsb-set-location 50.12344 10.23429
```

Alternatively, use the full path to readsb-set-location:

```bash
sudo /usr/local/bin/readsb-set-location 50.12344 10.23429
```

---

#### Troubleshooting and Checking Logs for WingBits:

If any issues arise, check the readsb logs using the following command:

```bash
sudo journalctl --no-pager -u readsb
```

If problems persist, try rebooting and rerunning the install script.

---

#### Reporting Issues with readsb:

- If issues persist, consider opening a GitHub issue with the provided logs and install script output.
- Alternatively, report issues with `readsb` via Discord by contacting wiedehopf [here](https://discord.gg/DxU4VG37JS).

---

#### Changing Configuration:

To modify `readsb` configuration, use a text editor such as nano:

```bash
sudo nano /etc/default/readsb
```

Make the necessary changes, save with Ctrl-O and Enter, then exit with Ctrl-X. Afterward, restart the `readsb` service:

```bash
sudo systemctl restart readsb
```

For a comprehensive list of available options, refer to the `readsb` help command:

```bash
readsb --help
```

---

**Conclusion:**

Configuring the location is a critical step in optimizing ADS-B reception with readsb. Following these steps ensures accurate data and provides troubleshooting avenues for any potential issues.

______

### Debug Commands for ADS-B Setup and for WingBits

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
#### readsb Debug Command:

- View dump1090-fa logs:
  ```bash
  sudo journalctl --no-pager -u readsb
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

## About Flight Tracking

For those interested, **Flight Tracking** involves the use of small computers, typically a Raspberry Pi, connected to a **software-defined radio (SDR)** USB stick operating at **1090 MHz**. This setup, known as a feeder or ADS-B receiver, captures aircraft positions transmitted on 1090 MHz, primarily through Automatic Dependent Surveillance–Broadcast (ADS-B). The essential components for building such a device are detailed below.

{{< figure src="ADS-B_graphic.jpg" alt="Simplified ADS-B Network Example" caption="Simplified ADS-B Network Example - southwestantennas.com" link="https://www.southwestantennas.com/articles/introduction-to-ads-b-technology" >}}

### Unique Identifiers and Aircraft History

Each aircraft transmitting its position on 1090 MHz is assigned a unique hexadecimal identifier, such as ABA7D9. This identifier remains constant, allowing users to track the historical data for a specific airframe. For example, the US-registered aircraft N850FD corresponds to the hex ID ABA7D9. The [aircraft history](https://tar1090.adsbexchange.com/?icao=aba7d9) for N850FD includes details such as its current callsign (e.g., FDX5235), which may be associated with a city pair for certain airlines.

### Detailed Aircraft Information

By selecting an aircraft on the [ADS-B Exchange map](https://tar1090.adsbexchange.com/), users can access detailed information on the left side of the page. Tooltips are available to explain various displayed elements. Additionally, users can explore the aircraft's history by clicking on the history tab, revealing a colored line indicating its flight path. Timestamps, speed in knots, altitude in feet, and other details are displayed, providing a comprehensive overview of the aircraft's journey.

##### Data Contribution and Real-Time Display

All the data presented on the ADS-B Exchange website is sourced from volunteers who have set up receivers, contributing real-time data. This data is collected and displayed on the online map, offering a collaborative and dynamic representation of aircraft movements globally.

##### ADS-B Aircraft Categories

{{< figure src="aircraft_types_illustration.png" alt="A vibrant cartoon illustration showcasing diverse aircraft types in flight." caption="Soar to New Heights with Varied Aircraft Types!" >}}

Flight tracking systems categorize ADS-B (Automatic Dependent Surveillance–Broadcast) equipped aircraft based on specific characteristics. These categories provide insights into the type and size of the aircraft, aiding in the identification and classification of air traffic. Here are the [defined ADS-B aircraft categories](https://mode-s.org/decode/content/ads-b/2-identification.html):

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

______


## WingBits Install and Setup Guide Conclusion

Congratulations on completing the setup of your WingBits mining system! By now, you've configured your hardware, fine-tuned your ADSB receiver, and optimized gain levels for maximum efficiency. Remember, cryptocurrency mining requires careful consideration of hardware, location, and market volatility. Always stay informed and adapt your strategy as needed. With your WingBits mining rig up and running, you're well-positioned to explore the exciting world of digital currency. Happy mining!

If you've made it this far, you might like to know you can actually dual mine [Wingbits](https://wingbits.com) and [Defli](https://defli.network/maclinux), read our [Guide on How to Dual Mine Wingbits and Defli](https://simeononsecurity.com/other/effortless-dual-mining-wingbits-defli-guide).

{{< centerbutton href="https://simeononsecurity.com/other/effortless-dual-mining-wingbits-defli-guide" >}}Read our Guide on How to Dual Mine Wingbits and Defli{{< /centerbutton >}}

______

## **References**
Here are some helpful links for reference:
- [WingBits](https://wingbits.com/#alpha)
- [WingBits Litepaper](https://wingbits.com/litepaper)
- [WingBits Map](https://wingbits.com/map)
- [WingBits Discord](https://discord.gg/zAt9m3aSm6)
- [WingBits Twitter](https://twitter.com/wingbits)
- [WingBits Documentation](https://medium.com/@wingbits)
- [DeFli](https://defli.network/maclinux)
- [readsB GitHub](https://github.com/wiedehopf/adsb-scripts)
- [graphs1090 Documentation](https://github.com/wiedehopf/graphs1090)
- [jq Command-Line JSON Processor](https://stedolan.github.io/jq/)
- [ADS-B Reception on Raspberry Pi](https://www.rtl-sdr.com/adsb-aircraft-radar-with-rtl-sdr/)
- [RTL-SDR Bias Tee Activation](https://www.rtl-sdr.com/getting-the-v3-bias-tee-to-activate-on-piaware-ads-b-images/)
- [RTL-SDR Receiver Test](https://github.com/wiedehopf/adsb-scripts/blob/master/rtl_test.sh)
- [dirkbeer/adsb-analysi](https://github.com/dirkbeer/adsb-analysis)
- [Graphs1090 ADSB Optimization Guide](https://gristleking.com/wingbits-optimization-graphs1090-plus/)
- [ADS-B Identification](https://mode-s.org/decode/content/ads-b/2-identification.html)
- [WingBits Docs](https://docs.wingbits.com/introduction/what-is-wingbits)