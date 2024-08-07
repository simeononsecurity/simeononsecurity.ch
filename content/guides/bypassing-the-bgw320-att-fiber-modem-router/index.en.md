---
title: "Bypassing the BGW-320: Using an Azores COTS ONT - A Step-by-Step Guide"
draft: false
toc: true
date: 2023-04-30
description: "Learn how to bypass the BGW-320 and use a COTS ONT made by Azores to connect to your ISP's network with this easy-to-follow guide."
tags: ["COTS ONT", "BGW-320", "Azores", "fiber", "network", "XGS-PON", "Ethernet", "IP passthrough", "customization", "ISP", "ont ID", "MAC address", "equipment ID", "image version", "hardware version", "telnet", "CLI application", "web GUI", "factory configuration mode", "compatibility issues", "bypassing BGW-320", "Azores COTS ONT", "fiber network", "XGS-PON", "Ethernet connectivity", "IP passthrough", "customization guide", "ISP network", "ONT ID configuration", "MAC address settings", "equipment ID customization", "image version configuration", "hardware version setup", "telnet access", "CLI application usage", "web GUI functions", "factory configuration mode", "compatibility issues", "troubleshooting steps", "true IP passthrough", "BGW-320 bypass tutorial", "Azores WAG-D20 guide", "fiber network setup", "ISP connectivity solutions", "network equipment customization", "ONT configuration tutorial", "bypassing ISP gateway", "fiber-to-ONT setup", "COTS ONT usage tips", "network equipment compatibility", "IP passthrough troubleshooting"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "A cartoon technician holding a COTS ONT with a fiber cable in the background."
coverCaption: ""
---

## How to Bypass the BGW-320 and Using an Azores WAG-D20

Most people with fiber have two ways to connect to the internet - fiber to an ONT, Ethernet to a gateway or fiber directly to the gateway. In this article, we will focus on how to bypass the BGW-320 and use a COTS ONT made by Azores. 

### Technical Aspects

The [Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont).

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Device Access

The default IP address of the device is 192.168.1.1 and its Gateway address has a factory typo using a public IP address i.e. it shows 192.162.1.1 instead of 192.168.1.1.

Once it boots, you need to hit enter to get a login prompt on the TTL serial interface (115200 8N1). This device has an A/B image system with an overlay partition holding any files you customize.
 
### Credentials

- `admin`/`ADMIN123!@#` - Administrator login for web GUI
- `Guest`/`welcome` - Guest login
- `test`/`default` - Factory login 

### Ethernet Interface

Connect your client to the 10G ethernet port and configure it with an address in the 192.168.1.x/24 network like - 192.168.1.2/255.255.255.0.

Upon running a port scan from 1-65535, you will notice some open ports:

- Ports `23` & `8009` - Telnet, requires login, runs the CLI application.
- Port `10002` - Unknown
- Port `80` - WebUI, only two functions

### Customizing the ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Now comes the important part i.e. changing some device info to make it compatible with your ISP's network.

First, grab the following information from your ISP Gateway or ONT:

1. **ONT ID**
  -  **ATT BGW320-500**: `HUMAXXXXXXXX`
  -  **ATT BGW320-505**: `NOKAXXXXXXXX`
  -  **ATT 020**: <serial number>
3. **MAC Address** (From device label)
4. **Equipment ID**
  - **ATT BGW320-500 HUMAX**: `iONT320500G`
  - **ATT BGW320-505 NOKIA**: `iONT320505G`
  - **ATT 020**: BVMGZ00BRAXS020XA
5. **Image Version**
  - **ATT 320**: `BGW320_3.21.4`
6. **Hardware Version**
  - **HUMAX ATT 320**: `BGW320-500_2.1`
  - **NOKIA ATT 320**: `BGW320-505_2.2`

Note: These are the OMCI values and not the ones from the web UI.

Telnet to your personal ONT (telnet 192.168.1.1), login as **`test`** using the **`default`** password and run the command 'test' to drop into factory configuration mode.

Display the currently set values with the 'show' command:

- `show gpon mac`
- `show sn`
- `show equipment id`

Once done, customize the settings with the following commands replacing x with your device values:

- `set gpon mac xx:xx:xx:xx:xx:xx`
- `set sn <insert ONT ID here>`

For HUMAX:

- `set equipment id “iONT320500G”`
- `config ONU-G_Version "BGW320-500_2.1”`

For Nokia:

- `set equipment id “iONT320505G”`
- `config ONU-G_Version "BGW320-505_2.2”`

Note: The last two commands should be applied from telnet logged in as the **`test`** user.

### Reboot and Enjoy True IP Passthrough

After customizing, reboot the ONT and enjoy true IP passthrough.

### Troubleshooting and Additional Steps
For more information on this topic, please check out the [8311 discord](https://discord.com/servers/8311-886329492438671420) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/).

### Conclusion

By following these steps one can successfully bypass the BGW-320 and use COTS ONT made by Azores to connect to their ISP's network. However, be careful while entering commands and make sure to replace 'x' with your device values correctly otherwise, you may face compatibility issues which may result in connection failures.


