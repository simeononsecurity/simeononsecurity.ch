---
title: "Budget DIY GPS/GNSS Base Station / Receiver Setup with ESP32 and UM980"
date: 2023-12-05
toc: true
draft: false
description: "Effortlessly set up a budget DIY GPS/GNSS base station using ESP32 and the Unicorecomm UM980 for accurate positioning."
genre: ["DIY Electronics", "GNSS Technology", "ESP32 Projects", "IoT Applications", "Budget Hardware", "DIY Tutorials", "Wireless Connectivity", "GPS Solutions", "GNSS Receivers", "Embedded Systems"]
tags: ["DIY GPS base station", "ESP32 tutorial", "UM980 GNSS receiver", "GNSS setup guide", "budget hardware", "IoT applications", "GNSS technology", "embedded systems", "wireless connectivity", "ESP32 development board", "GNSS accuracy", "DIY electronics", "GNSS modules", "GPS solutions", "ESP32 firmware", "budget GNSS setup", "GNSS base station", "GPS project", "GNSS reference station", "ESP32 GNSS integration", "GNSS antenna", "DIY hardware", "GNSS calibration", "GNSS accuracy improvement", "GNSS troubleshooting", "ESP32 configuration", "GNSS data logging", "GNSS monitoring", "ESP32 community support"]
cover: "/img/cover/Budget_DIY_GPS_GNSS_Base_Station_Setup.png"
coverAlt: "An illustration of an ESP32 board connected to various accessories."
coverCaption: "ESP32 for all the things!"
canonical: ""
ref: "https://simeononsecurity.ch/other/onocoy-gps-gnss-reciever-basestation-on-a-budget/"
---

**Best Budget DIY GPS/GNSS Base Station using the UM980 and a ESP32**

## Introduction
The ESP32 is a versatile microcontroller renowned for its WiFi and Bluetooth capabilities. In this guide, we'll walk you through setting up the your **ESP32 development board** with the [**Unicorecomm UM980**](https://en.unicorecomm.com/products/detail/26) and various accessories. We'll also cover flashing the ESP32 with the desired firmware.

{{< figure src="esp32pinout.jpg" alt="ESP32 Wroom DevKit Full Pinout" caption="ESP32 Wroom DevKit Full Pinout - mischianti.org" link="https://mischianti.org/2021/07/17/esp32-devkitc-v4-high-resolution-pinout-and-specs/" >}}

### Alternate Instructions
**Want to use a linux distro or a raspberry pi?**

Check out our guide on [**Setting up a NTRIP server on Linux**](https://simeononsecurity.ch/other/onocoy-gps-gnss-reciever-basestation-on-a-budget/)

### Looking for how to use this with Onocoy?

Check out our guide on [**DIY Onocoy Ntrip Server and Reference Station Setup**](https://simeononsecurity.ch/other/onocoy-gps-gnss-reciever-basestation-on-a-budget/)

### Hardware Components
Before we begin, let's take a look at the hardware components you'll need:

1. **ESP32 Development Board**: [AITRIP 2 Sets ESP-WROOM-32 ESP32](https://amzn.to/3rEMIjr)

2. **Power Supply**: [CanaKit 3.5A Raspberry Pi 4 Power Supply (USB-C)](https://amzn.to/3ZOpDao)

3. **Adapter Cables**: (Choose one):
   - [elechawk 9 PCS 1.25mm to Dupont 2.54mm Pitch Adapter Cables](https://amzn.to/3PGI5xc)
   - [PB1.25 to Dupont 2.54mm Connectors and Cables Kit Compatible with Molex PicoBlade 1.25mm Pitch Connectors 20cm Wires](https://amzn.to/3PUgiJY)
   - [2Pcs 1.25mm to 2.54mm dupont cable 1pin female 2.54mm wire connector 1.25mm 2/3/4/5/6P wire harness 28AWG Length 20cm](https://www.aliexpress.us/item/3256805267757221.html) - **Choose the 4P Option**

4. **Enclosure Kit**: [qBoxMini DIY IOT Enclosure Plus Kit (One SMA)](https://amzn.to/3PIvwl7)

5. **GNSS Receiver Board** (Choose one):
   - [UM980 RTK InCase PIN GNSS receiver board with USB C](https://gnss.store/unicore-gnss-modules/246-152-elt0221.html#/58-connector-ipex) - If you choose this option, you'll need some [male to male dupont wires](https://amzn.to/3Q7VKyH). 
   - [Full Frequency Centimeter Level Low-power and High-precision UM980 Module RTK Differential Drone GPS Module GNSS Whole System](https://www.aliexpress.us/item/3256805781651631.html)

6. **Firmware**: [ESP32-XBee Firmware](https://github.com/nebkat/esp32-xbee/releases/tag/v0.5.2)

## Step-by-Step Setup

### 1. Assemble Your Workstation / Desktop / Laptop
Ensure you have a computer with a USB port and internet access. You'll need this for downloading [firmware](https://github.com/nebkat/esp32-xbee/wiki/Firmware-Update) and drivers.

### 2. Connect Hardware Components
- If applicable, plug the ESP32 into the breakout board.
  - {{< figure src="connectesp32todevboard.jpg" alt="Connecting ESP32 to Dev Board" caption="ESP32 Dev Board" >}}
  - {{< figure src="esp32.jpg" alt="ESP32 Dev Board" caption="ESP32 Dev Board" >}}
- Connect the [ESP32 development board](https://amzn.to/3rEMIjr) to your computer using a [Type-C USB cable](https://amzn.to/3ttZS33).

### 3. Use Adapter Cables
Utilize the [elechawk adapter cables](https://amzn.to/3PUgiJY) or alternatives as necessary to connect the [UM980](https://gnss.store/unicore-gnss-modules/246-152-elt0221.html#/58-connector-ipex) to your [ESP32 board](https://amzn.to/3rEMIjr). These cables offer compatibility with various connectors for expanding your project.

- [UM980 RTK InCase PIN GNSS receiver board with USB C](https://gnss.store/unicore-gnss-modules/246-152-elt0221.html#/58-connector-ipex) 
  - If you choose this option, again, you'll need some [male to male dupont wires](https://amzn.to/3Q7VKyH)
  - Wiring
    - `UM980 +5V` to `ESP32 5V` (or 3V3) for power.
    - `UM980 GND` to `ESP32 GND` for ground.
    - `UM980 TXD2` to `ESP32 GPIO pin` designated for receiving data (e.g., `GPIO pin 16`, `RX1`, `RX0`).
    - `UM980 RXD2` to `ESP32 GPIO pin` designated for transmitting data (e.g., `GPIO pin 17`, `TX1`, `TX0`).
    - {{< figure src="gnssstoreum980.png" alt="Connecting the GNSS.store UM980 Module to The ESP32 Devboard" caption="GNSS.store UM980 to ESP32 Dev Board Breakout Pin Diagram" >}}
- [Full Frequency Centimeter Level Low-power and High-precision UM980 Module RTK Differential Drone GPS Module GNSS Whole System](https://www.aliexpress.us/item/3256805781651631.html)
  - Wiring
    - `UM980 UART VCC (Pin 1)` to `ESP32 3.3V` (or 3V3) for power.
    - `UM980 UART GND (Pin 2)` to `ESP32 GND` for ground.
    - `UM980 UART TXD (Pin 3)` to `ESP32 GPIO pin` designated for receiving data (e.g., `GPIO pin 16`, `RX1`, `RX0`).
    - `UM980 UART RXD (Pin 4)` to `ESP32 GPIO pin` designated for transmitting data (e.g., `GPIO pin 17`, `TX1`, `TX0`).
    - {{< figure src="aliexpressum980.png" alt="Connecting the AliExpress UM980 Module to The ESP32 Devboard" caption="AliExpress UM980 to ESP32 Dev Board Breakout Pin Diagram" >}}


### 4. Employ the Enclosure Kit
For environmental protection, consider using the [qBoxMini DIY IOT Enclosure Kit](https://amzn.to/3PIvwl7). It offers waterproof protection and includes connectors and a prototyping PCB for easy integration.

### 5. Choose the GNSS Receiver
Depending on your project needs, timeline, and budget, select the appropriate [GNSS receiver board](https://gnss.store/unicore-gnss-modules/246-152-elt0221.html#/58-connector-ipex). 
Follow the wiring diagram above for implementation.

### 6. Flash the Firmware
To flash the [ESP32](https://amzn.to/3rEMIjr) with the [ESP32-XBee firmware](https://github.com/nebkat/esp32-xbee), follow these steps:
1. Download the firmware from the provided [GitHub release](https://github.com/nebkat/esp32-xbee/releases/latest).
  - Go to the [latest stable firmware release](https://github.com/nebkat/esp32-xbee/releases/latest) and download:

    - `bootloader.bin`
    - `partition-table.bin`
    - `esp32-xbee.bin`
    - `www.bin`

If you would like to reset the device configuration, you should also download:

    - `wipe_config.bin`

2. Install necessary flashing tools like the ESP-IDF framework and Espressif's ESP Flash Download Tool.
  - Windows
    - **Windows Flash Tools** from [Espressif](https://www.espressif.com/en/support/download/other-tools)
  - Linux
    - If you have not already done so, install the ESP flashing tool, `esptool`:

      - **Ubuntu/Debian**: `sudo apt-get install esptool`

      - **Arch**: `sudo pacman -S esptool`
3. Connect the ESP32 to your computer.
   - While plugging into your computer, hold down the `BOOT` button to prepare the ESP32 for Flashing.
     - {{< figure src="esp32boot.webp" alt="ESP32 Boot Button" caption="ESP32 Boot Button - randomnerdtutorials.com" link="https://randomnerdtutorials.com/boot-button-1/" >}}
4. Flash the XBEE ESP32 Firmware
  *Note*: Your COM device location will be different than mine. You'll need to identify it first before continuing.
  - Windows
    - Open the ESP Flash Download Tool, select the firmware files, set flashing options, and click "Start" to flash the firmware onto the ESP32.
      - {{< figure src="windowsloadfirmware.png" alt="loading ESP32 Firmware on Windows" caption="Loading ESP32 Firmware on Windows - github.com/nebkat/esp32-xbee/" link="https://github.com/nebkat/esp32-xbee/wiki/Firmware-Update" >}}
      - It is important that the offsets exactly match the files:
        - `bootloader.bin` @ `0x1000`
        - `partition-table.bin` @ `0x8000`
        - `esp32-xbee.bin` @ `0x10000`
        - `www.bin` @ `0x210000`
      - If you would like to reset the device configuration, you should also include:
        - `wipe_config.bin` @ `0x0`
    - {{< figure src="windowsflashfirmware.png" alt="Flashing ESP32 Firmware on Windows" caption="Flashing ESP32 Firmware on Windows - github.com/nebkat/esp32-xbee/" link="https://github.com/nebkat/esp32-xbee/wiki/Firmware-Update" >}}
    - Alternatively, copy the firmware files to the extracted esptool.exe's folder and run the following as an administrator
      - 
      ```powershell
         .\esptool.exe --before default_reset --after hard_reset --chip esp32 --port COM10 --baud 115200 write_flash --flash_mode dio --flash_size detect --flash_freq 40m -z 0x1000 ./bootloader.bin 0x8000 ./partition-table.bin 0x10000 ./esp32-xbee.bin 0x210000 ./www.bin
      ```
  - Linux
    - ```bash
         esptool.py -b 460800 --after hard_reset write_flash --flash_mode dio --flash_freq 40m --flash_size 4MB 0x8000 partition-table.bin 0x1000 bootloader.bin 0x10000 esp32-xbee.bin 0x210000 www.bin
      ```
     - If you would like to reset the device configuration, also include: `0x0 wipe_config.bin`
   - 
      ```esptool.py v2.8
      Found 1 serial ports
      Serial port /dev/ttyUSB0
      Connecting....
      Detecting chip type... ESP32
      Chip is ESP32D0WDQ5 (revision 1)
      Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
      Crystal is 40MHz
      MAC: 4c:11:ae:6e:30:6c
      Uploading stub...
      Running stub...
      Stub running...
      Configuring flash size...
      Compressed 3072 bytes to 110...
      Wrote 3072 bytes (110 compressed) at 0x00008000 in 0.0 seconds (effective 1540.7 kbit/s)...
      Hash of data verified.
      Compressed 17216 bytes to 11168...
      Wrote 17216 bytes (11168 compressed) at 0x00001000 in 1.0 seconds (effective 138.8 kbit/s)...
      Hash of data verified.
      Compressed 788768 bytes to 493546...
      Wrote 788768 bytes (493546 compressed) at 0x00010000 in 43.9 seconds (effective 143.8 kbit/s)...
      Hash of data verified.
      Compressed 1048576 bytes to 93902...
      Wrote 1048576 bytes (93902 compressed) at 0x00210000 in 8.4 seconds (effective 1004.1 kbit/s)...
      Hash of data verified.

      Leaving...
      Hard resetting via RTS pin...
      ```
5. Restart the ESP32
  - Hit the "EN" button
  - Or Power Cycle the Device

### 7. **Configuration**

1. **Step 1: Connect to the XBee Hotspot**
   1. Using your phone or PC, **connect to the ESP32's WiFi Hotspot** which will be called `ESP_XBee_XXXXXX` where `XXXXXX` are some random numbers/letters unique to your device.

2. **Step 2: Browse to the Configuration Page**
   1. Open your browser and navigate to http://192.168.4.1/. You should see a page similar to: {{< figure src="xbeeesp32config.png" alt="XBee ESP32 Configuration Page" caption="XBee ESP32 Configuration Page - github.com/nebkat/esp32-xbee/" link="https://github.com/nebkat/esp32-xbee/wiki/Getting-Started/" >}}

3. **Step 3: Configure WiFi**
   1. **Enable the WiFi section**, press Scan to search for networks, **choose your home WiFi network** (or phone hotspot) and enter the password.
   
      The ESP32 does not have very good WiFi reception, so make sure you are relatively close to the network you are connecting to, especially when indoors, to avoid problems.
   
      Press the Submit button, and follow the instructions on screen. You may need to reconnect to the ESP32 XBee hotspot after it restarts.
   
      The WiFi section will now show its connection status: {{< figure src="xbeeesp32wificonfig.png" alt="XBee ESP32 Wifi Configuration Page" caption="XBee ESP32 Wifi Configuration Page - github.com/nebkat/esp32-xbee/" link="https://github.com/nebkat/esp32-xbee/wiki/Getting-Started/" >}}

   2. If you are connected to the device using a serial terminal, the device will output information about its WiFi connection.
   
      ```shell
      $PESP,WIFI,STA,CONNECTING,S10,P*71
      $PESP,WIFI,STA,CONNECTED,S10*4C
      $PESP,WIFI,STA,IP,192.168.43.100/24,192.168.43.1*5D
      ```

4. **Step 4: Improve Security Configuration**
   1. **Hotspot**
   
      To prevent others from accessing your ESP32 XBee, you may want to adjust the settings of the WiFi hotspot section.
   
      There are three ways to do this:
   
         1. Change from **Open security to WPA/2-PSK and enter a password** (recommended).
         2. **Hide the SSID** by toggling the Hidden setting.
            - **Note**: *This will not prevent connections, but will hide the hotspot from WiFi scans on other devices*.
         3. **Disable the hotspot entirely** by toggling the WiFi hotspot section
            - **Note**: *You will not be able to access the ESP32 XBee if there is a problem with its connection to your home WiFi network, unless you perform a* [*Full Reset*](https://github.com/nebkat/esp32-xbee/wiki/Getting-Started/f89fa4ad06a50b2e248109c73be7c6389f9f1716#full-reset).
   
         {{< figure src="xbeeesp32securewificonfig.png" alt="XBee ESP32 Secure Wifi Configuration Page" caption="XBee ESP32 Secure Wifi Configuration Page - github.com/nebkat/esp32-xbee/" link="https://github.com/nebkat/esp32-xbee/wiki/Getting-Started/" >}}
   
   2. **Configuration**
   
      If you would like to prevent others on your home network from modifying the ESP32 XBee configuration, you can also adjust the settings of the Admin section.
   
      You can choose between only allowing devices connected to the hotspot, or a username/password.
   
      The new IP address will be the first address in the 3rd line as above, i.e. 192.168.43.100.
   
      {{< figure src="xbeeesp32adminuserconfig.png" alt="XBee ESP32 Admin User Configuration Page" caption="XBee ESP32 Admin User Configuration Page - github.com/nebkat/esp32-xbee/" link="https://github.com/nebkat/esp32-xbee/wiki/Getting-Started/" >}}

5. **Step 5: Improve Security Configuration**

   1. You can now proceed to **configure the available protocols**.

      **Note**: *Do not enable all protocols at once. The ESP32 is not able to handle an unlimited amount of open sockets/connections, so only enable the protocols you are actually using.*

      The small color selector beside each section's toggle button will determine the color of the RGB LED on the ESP32 XBee for that feature, so that you can keep track of its status. Setting the color to black will disable the LED for that feature. Typically, a fading LED means the feature is working correctly/connected, while a blinking LED or no LED means the feature is awaiting a connection or could not connect to its target.

### 7. Profit?

### 8. Extras
   1. **Full Reset**: In case you encounter any problems and are unable to connect to the device, simply hold the `BOOT` button for 5 seconds, and the ESP32 will be reset to its default configuration.

      {{< figure src="esp32boot.webp" alt="ESP32 Boot Button" caption="ESP32 Boot Button - randomnerdtutorials.com" link="https://randomnerdtutorials.com/boot-button-1/" >}}
      
      If this procedure does not work for any reason, an alternative method to perform a full reset is to follow the [Firmware Update](https://github.com/nebkat/esp32-xbee/wiki/Firmware-Update) procedure, including the `wipe_config.bin` file as described.

### 9. Testing
Once the firmware is successfully flashed, your ESP32 board is ready for testing. Begin developing and running IoT applications, making the most of the board's WiFi, Bluetooth, and GNSS capabilities.

This is where you'll unplug the ESP32 from your desktop and Plug the [CanaKit Raspberry Pi 4 power supply](https://amzn.to/3ZOpDao) into a power source and connect it to the [ESP32 board](https://amzn.to/3rEMIjr) via USB-C.

Testing is going to depend on multiple factors. This part is up to you. 
I suggest using [Onocoy](https://console.onocoy.com/explorer) and using their service to test your configuration if you're setting up an NTRIP Server.

