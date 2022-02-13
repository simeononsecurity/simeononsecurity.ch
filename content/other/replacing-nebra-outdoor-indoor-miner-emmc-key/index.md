---
title: "Replacing and Reimaging the Nebra Indoor and Outdoor EMMC Key / SD Card"
draft: false
toc: true
description: "In the event that your microSD card fails, here are the steps to re-flash it or
replace it with a brand new one"
tags: ['Replacing Nebra Helium Miner SD Card', 'SD Card Upgrade', 'Fix Helium Miner Syncing Issues', 'Nebra', 'Nebra Indoor Miner', 'Nebra Outdoor Miner', 'Balena Etcher', 'Helium Miner', 'Raspberry Pi Compute Module 3', 'RPiBoot']
---

# Replacing and Reimaging the Nebra Indoor and Outdoor EMMC Key / SD Card

## Required Tools:
- A Phillips Head Screwdriver or [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) for Nebra Outdoor Miner
- Strong fingernails, tweezers, or needle-nose pliers to remove the old SD card
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Required software:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Balena Raspberry Pi Image](https://api.balena-cloud.com/download?deviceType=raspberrypi3-64&version=2.80.3+rev1.prod&fileType=.zip)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
 
## Inside the Nebra Helium Miners:
### Contents of the Nebra Indoor Miner:
![Nebra Indoor Miner](https://helium.nebra.com/media/photos/indoor/Indoor-internal-lights.png)
### Contents of the Nebra Outdoor Miner:
![Nebra Outdoor Miner](https://helium.nebra.com/media/photos/outdoor/Inside-Interfaces.jpg)
 - 1.) 9-16V @ 15W DC 6.5MMx2.0MM Barrel Jack
 - 2.) Ethernet Connector
 - 3.) LED Indicator
 - 4.) Interface Button
 - 5.) 4G / LTE Module Connector
 - 6.) Sim Card Slot

## How to replace the SD Card
### Step 1: Acquire the config.json file from the EMMC Key:
- Download and install [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe), you'll need this to boot the compute module as a usb file system
- Identify the and adjust jumper pins on the CM3 daughterboard for programming mode
 - ![Daughterboard Overview](https://helium.nebra.com/media/photos/outdoor/daughterboardBreakdown.png)
   - 5.) Micro USB Port used for Imaging
   - 7.) JP4 USB Jumper - Used to switch between normal operation and flash mode, ensure it is in position 1-2 for normal operation and 2-3 for programming.
   - 8.) JP3 Power Jumper - Allows the module to be powered from the Micro USB connector. Only connect when programming from PC and ensure mainboard is not connected.
 - Move the JP4 Jumper to position 2+3
 - Plug in a usb cable and run the [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) utility
 - Open your file explorer and you'll see a drive called "resin-boot". Retrieve the "config.json" file from the directory
 - Unplug the usb cable and reset the JP4 jumper to position 1+2
### Step 2: Flash new sd card with the Balena Raspberry Pi CM3 Image:
- Download and extract [Balena Raspberry Pi Image](https://api.balena-cloud.com/download?deviceType=raspberrypi3-64&version=2.80.3+rev1.prod&fileType=.zip)
- Using [Balena Etcher](https://www.balena.io/etcher/) select the recently extracted .img file and your new microsd card as the target device
- Select Flash
### Step 3: Copy the original config file to the new sd card:
- Unplug your micro sd card reader and plug it back in after finishing step 2
- You'll now see a drive in explorer called "resin-boot". 
 - Copy the config.json file you copied earlier and overwrite the config.json file that is already on the sd card.
### Step 4: Install the new sd card and reassemble the Nebra Miner:
 - Install the SD card in the slot in which the EMMC key was previously.
 - Reassemble the miner
 - When first powering the newly flashed Nebra Miner, plug it in with ethernet for 20-30 minutes before setting up wifi connections again.
### Step 5: Profit?




