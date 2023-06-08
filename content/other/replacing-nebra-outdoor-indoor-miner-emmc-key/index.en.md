---
title: "Replacing Nebra Helium Miner SD Card: Step-by-Step Guide"
draft: false
toc: true
date: 2022-02-13
description: "Learn how to replace or re-flash the Nebra Indoor and Outdoor, First and Second generation, EMMC Key SD Card and fix Helium Miner syncing issues with this guide."
genre: ["Technology", "Cryptocurrency", "Hardware", "Helium Mining", "Troubleshooting", "SD Card Replacement", "Syncing Issues", "Raspberry Pi", "Balena Etcher", "Nebra Helium Miner"]
tags: ["Nebra Helium Miner", "SD Card Replacement", "Syncing Issues", "Helium Mining", "Troubleshooting", "Raspberry Pi", "Balena Etcher", "Hardware Guide", "SD Card Upgrade", "Resolving Synchronization Issues", "Step-by-Step Guide", "Helium Miner Sync Fix", "Nebra Indoor Miner", "Nebra Outdoor Miner", "Raspberry Pi Compute Module 3", "Balena Raspberry Pi CM3 Image", "Troubleshooting Helium Miners", "Nebra Mining Equipment", "Balena Etcher Software", "Replacing EMMC Key on Nebra Miner", "SD Card Repair for Helium Miner", "Fixing Helium Miner Sync Issues", "Nebra Miner SD Card Replacement", "Guide to Nebra Helium Miner Troubleshooting", "Helium Mining Tips", "Upgrading Nebra Helium Miner SD Card", "How to Reimage Nebra Miner SD Card", "Troubleshooting Nebra Helium Miner Syncing Problems"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "A cartoon illustration of a person holding a Nebra Helium Miner with an open panel revealing the SD card slot and the steps of the guide appearing as a guidebook floating above the device."
coverCaption: "Solve sync issues and upgrade your Helium Miner with ease."
---

**Replacing and Reimaging the Nebra Indoor and Outdoor EMMC Key / SD Card**

This comprehensive guide will walk you through the process of replacing or re-flashing the Nebra Indoor and Outdoor EMMC Key/SD Card. By following these steps, you can resolve synchronization issues with your Helium Miner and ensure smooth operation. The guide provides a detailed explanation of the tools and software you'll need, as well as the necessary steps to acquire the config.json file, flash the new SD card using Balena Raspberry Pi CM3 Image, and transfer the original config file to the new SD card.

## Introduction

The Nebra Helium Miners, both the Indoor and Outdoor models, rely on the EMMC Key/SD Card for their functioning. Over time, it may become necessary to replace or re-flash this card to address syncing issues and maintain optimal performance. This guide will equip you with the knowledge and instructions required to carry out this task effectively.

To successfully replace the Nebra Helium Miner's SD Card, you will need specific tools and software. The tools include a Phillips Head Screwdriver or [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe). With these resources at hand, you'll be ready to proceed with the SD Card replacement or re-flashing.

## Required Tools:
- A Phillips Head Screwdriver or [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) for Nebra Outdoor Miner
- Strong fingernails, tweezers, or needle-nose pliers to remove the old SD card
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Required software:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- Latest Nebra Image For Your Specific Device:
*If you don't know what device you have, please consult the [nebra documentatio](https://support.nebra.com/support/home)n. If it's older, it's pretty safe to assume you have a first generation device.*
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## Inside the Nebra Helium Miners:
### Contents of the Nebra Indoor Miner:
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Contents of the Nebra Outdoor Miner:
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6.5MMx2.0MM Barrel Jack
 - 2.) Ethernet Connector
 - 3.) LED Indicator
 - 4.) Interface Button
 - 5.) 4G / LTE Module Connector
 - 6.) Sim Card Slot

## How to replace the SD Card
### Step 1: Optionally acquire the config.json file from the EMMC Key:
- Download and install [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe), you'll need this to boot the compute module as a usb file system
- Identify the and adjust jumper pins on the CM3 daughterboard for programming mode
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Micro USB Port used for Imaging
   - 7.) JP4 USB Jumper - Used to switch between normal operation and flash mode, ensure it is in position 1-2 for normal operation and 2-3 for programming.
   - 8.) JP3 Power Jumper - Allows the module to be powered from the Micro USB connector. Only connect when programming from PC and ensure mainboard is not connected.
 - Move the JP4 Jumper to position 2+3
 - Plug in a usb cable and run the [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) utility
 - Open your file explorer and you'll see a drive called "resin-boot". Retrieve the "config.json" file from the directory you may need that later and it should be backed up.
 - Unplug the usb cable and reset the JP4 jumper to position 1+2
### Step 2: Flash new sd card with the Balena Raspberry Pi CM3 Image:
- Download and extract your appropriate image
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Using [Balena Etcher](https://www.balena.io/etcher/) select the recently extracted .img file and your new microsd card as the target device
- Select Flash
### Step 3: Install the new sd card and reassemble the Nebra Miner:
 - Install the SD card in the slot in which the EMMC key was previously.
 - Reassemble the miner
 - When first powering the newly flashed Nebra Miner, plug it in with ethernet for 20-30 minutes before setting up wifi connections again.
### Step 4: Profit?




