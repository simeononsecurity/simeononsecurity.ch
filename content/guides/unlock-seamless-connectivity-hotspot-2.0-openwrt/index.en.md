---
title: "Configuring Hotspot 2.0 / Passpoint 2.0 on OpenWRT"
date: 2024-02-02
toc: true
draft: false
description: "Explore the step-by-step guide to create Hotspot 2.0 on OpenWRT, ensuring seamless connections and enhanced security. Dive into the future of Wi-Fi effortlessly."
genre: ["Technology", "Networking", "Wireless Solutions", "OpenWRT Configuration", "Passpoint Setup", "Cybersecurity", "WiFi Standards", "Router Enhancements", "Internet Connectivity", "Network Optimization"]
tags: ["Hotspot 2.0", "OpenWRT", "Passpoint", "WiFi Configuration", "Wireless Networks", "Network Security", "Router Setup", "Internet Connectivity", "Tech Tutorials", "Cybersecurity Tips", "WiFi Standards", "Seamless Connection", "Wireless Solutions", "Network Optimization", "Router Enhancements", "Passpoint 2.0", "OpenWRT Tutorial", "WiFi Access Points", "RADIUS Server", "802.11 AX", "Troubleshooting Guide", "WiFi Adapters", "Network Management", "Network Infrastructure", "Tech How-To", "Secure WiFi", "WiFi Authentication", "WiFi Protocols", "WiFi Best Practices"]
cover: "/img/cover/hotspot2.0-openwrt-setup.png"
coverAlt: "A vibrant illustration depicting interconnected WiFi signals forming a seamless network"
coverCaption: "Empower Your Network: Hotspot 2.0 Unleashed on OpenWRT!"
---

**Creating Hotspot 2.0 / Passpoint 2.0 Hotspots on OpenWRT**

In today's connected world, providing seamless and secure Wi-Fi connectivity is essential for various industries and public spaces. One revolutionary technology that addresses this need is **Hotspot 2.0**, also known as **Passpoint 2.0**. In this article, we will explore how to set up Hotspot 2.0 on OpenWRT, a popular open-source router and access point firmware.

## Introduction

**Hotspot 2.0** brings enhanced security and convenience to Wi-Fi connectivity by automating the connection process and ensuring a secure exchange of credentials. Before diving into the technical details, let's address the key questions: What is Hotspot 2.0, and why is it crucial for modern Wi-Fi networks?

Hotspot 2.0, defined by the **IEEE 802.11u standard**, enables **seamless and secure Wi-Fi roaming** by allowing mobile devices to connect to Wi-Fi networks automatically. This technology eliminates the hassle of manually selecting and authenticating with each network, providing users with a more efficient and user-friendly experience.

______

## The Significance of Hotspot 2.0 and Passpoint 2.0

### Enhancing User Experience

One of the main goals of **Hotspot 2.0** is to enhance the user experience when connecting to Wi-Fi networks. With Passpoint certification, smartphones can automatically identify and connect to Passpoint-certified access points. This eliminates the need for users to navigate through network lists and enter credentials manually.

### Security and Authentication

Hotspot 2.0 addresses security concerns by implementing robust authentication protocols. The Passpoint profile on a smartphone contains essential information, including **MCC-MNC (Mobile Country Code – Mobile Network Code)**, **NAI realm**, and **OI (Organization Identifier)**. These elements, along with login credentials, establish a secure connection to the service provider.

### Interoperability and Roaming

Passpoint profiles are not tied to specific SSIDs, allowing them to work across any WLAN with appropriate Passpoint configuration. This interoperability ensures a consistent and reliable connection experience, especially in environments with multiple access points.

______

## Implementing Hotspot 2.0 on OpenWRT

### Prerequisites for Hotspot 2.0 on OpenWRT

Before configuring Passpoint on OpenWrt, ensure you have the following prerequisites:

- OpenWrt compatible device with a Passpoint-capable wireless device (PHY).
- OpenWrt 21.02, or newer, including `wpad` (hostapd) built with the `hs20` option.
- Full version of the `iw` package in OpenWrt.
- 802.1x infrastructure (RADIUS server).
- Information about the assigned RADIUS servers:
    - Server IP address
    - Port numbers
    - Shared secrets

> **Note:** This information can be obtained through an email or document through your provider. If you're using [Google Orion](https://orion.google/) like we are in our examples below, you'll be self hosting a [freeradius based radsec proxy](https://github.com/simeononsecurity/orion-radsec/tree/sos-dev). We won't be going into this in this article so **please read your providers instructions carefully**.

#### Overview of Hotspot 2.0 on OpenWRT

Passpoint configuration on OpenWrt requires specific preparations and package installations. Here is an overview of the necessary steps:

1. **Check `wpad` for Hotspot 2.0 Capability:**
   
   Verify if `wpad` has Hotspot 2.0 capability by running the following command:

   ```bash
   strings /usr/sbin/wpad | grep hs20
   ```

   If nothing shows up, it indicates that `wpad` lacks Hotspot 2.0 support. In this case, the default package (`wpad-basic`) needs to be replaced with a full version, such as `wpad-openssl`. We have commands that will do this for you below.

2. **Hostapd Configuration with UCI:**

   Unlike manual editing of `hostapd.conf` on a Linux box, OpenWrt uses UCI (Unified Configuration Interface) to auto-generate the configuration. The shell script "/lib/netifd/hostapd.sh" generates "/var/run/hostapd-phyX.conf" based on the wireless configuration file "/etc/config/wireless" in the UCI.

   Ensure the wireless configuration in "/etc/config/wireless" is correctly set up to align with Passpoint requirements.

By following these steps, you set up the necessary prerequisites and configurations for Passpoint on OpenWrt, enabling your device to support Hotspot 2.0 seamlessly.

### Recommended OpenWRT Devices with Hotspot 2.0 and Passpoint 2.0 Support

Are you searching for the perfect OpenWRT device with robust Hotspot 2.0 and Passpoint 2.0 support? Look no further! We've curated a list of highly recommended devices that seamlessly integrate these advanced features into your network. From the [GL-MT6000 (Flint 2)](https://amzn.to/3UnfDEw) with WiFi 6 capabilities to the pocket-sized [GL-AXT1800 (Slate AX)](https://amzn.to/48ZFYNn) offering gigabit travel convenience, explore the best options for enhanced connectivity and security. Upgrade your router experience with these top-notch devices tailored for Hotspot 2.0 enthusiasts and professionals alike.

- [GL.iNet GL-MT6000 (Flint 2) WiFi 6 Router](https://amzn.to/3UnfDEw)

{{< centerbutton href="https://amzn.to/3UnfDEw">}}Get Your GL.iNet GL-MT6000(Flint 2) Today!{{< /centerbutton >}}

- [GL.iNet GL-AXT1800 (Slate AX)](https://amzn.to/48ZFYNn)

{{< centerbutton href="https://amzn.to/48ZFYNn">}}Get Your GL.iNet GL-AXT1800 (Slate AX) Today!{{< /centerbutton >}}

- [GL.iNet GL-MT3000 (Beryl AX)](https://amzn.to/49knV4o)

{{< centerbutton href="https://amzn.to/49knV4o">}}Get Your GL.iNet GL-MT3000 (Beryl AX) Today!{{< /centerbutton >}}

- [GL.iNet GL-SFT1200 (Opal)](https://amzn.to/3UkHVQ5)

{{< centerbutton href="https://amzn.to/3UkHVQ5">}}Get Your GL.iNet GL-SFT1200 (Opal) Today!{{< /centerbutton >}}

### Updating OpenWRT Packages for Hotspot 2.0 Support on OpenWRT

Before configuring Hotspot 2.0 on OpenWRT, ensure that your system is up to date. Use the following commands to update packages and install necessary components:

```bash
opkg update
opkg --force-removal-of-dependent-packages remove iw wpad-basic gl-sdk4-repeater hostapd-basic hostapd-openssl 
opkg --force-overwrite --force-removal-of-dependent-packages install iw-full hostapd-common wpad-openssl nano
```

If you've purchased one of the [GL.iNet devices](https://amzn.to/3UnfDEw) we recommended above you'll also run the following command:

```bash
opkg --force-overwrite install kmod-ath10k-smallbuffers kmod-ath9k kmod-ath9k-common kmod-ath kmod-mac80211 kmod-cfg80211
```

### Configuring Wireless Interfaces for Hotspot 2.0 on OpenWRT

In the `/etc/config/wireless` file, customize the settings for your Hotspot 2.0-enabled interface. Ensure the correct device, encryption type, and other parameters are set. Pay attention to the **WAN Metrics**, **NAI Realm**, and **Domain Names** sections to tailor them to your service provider. 

> We have many of these options already configured in the details below. **Read the code comments carefully, this section is not copy and paste.** It requires a lot of customization for your environment.

Copy and modify the following carefully. Once working, mirror it for the **2.4ghz, 5ghz, and 6ghz** radios while adjusting the `wifi-iface config name`, `ifname`, and `device` (radio) options **for each radio**.

`nano /etc/config/wireless`
```bash
config wifi-iface 'radio1_orion5g'
    #Modify to your radsec proxy server / radius server
    option acct_secret 'radsec'
    option acct_server 'xxx.xxx.xxx.xxx'
    option auth_secret 'radsec'
    option auth_server 'xxx.xxx.xxx.xxx'
    # Likely radio0 or radio1 if using built in radios, if using a usb device it'll likely be radio 2
    option device 'radio1'
    # Change between either wpa2-mixed or wpa3-mixed
    option encryption 'wpa3-mixed'
    # first number matches the radio, second is the ssid number. Both start at 0
    # Ex wlan1-2 would be radio 1, ssid 2.
    option ifname 'wlan1-2'
    
    #Table E-4 of IEEE Std 802.11-2012 Annex E define the values that can be used in this. (Likely just use 5173)
    # https://ieeexplore.ieee.org/iel5/6361246/6361247/06361248.pdf
    # https://mentor.ieee.org/802.11/dcn/10/11-10-0564-00-0s1g-operating-classes.ppt
    #format: hexdump of operating class octets
    option hs20_operating_class '5173'
    # See Instructions Below (Optional, omit if you want.)
    option hs20_wan_metrics '01:3e80:3e80:33:99:3000'
    # Venue Info 
    # The available values are defined in IEEE Std 802.11u-2011, 7.3.1.34
    option iw_venue_group '1'
    option iw_venue_type '7'
    # Specify the same nasid for both 2.4ghz and 5ghz. Use any time the network is different. Normally it'll be the same across the board for all AP's in the same location.
    option nasid 'OrionWRT'
    # Likely leave as guest, but customize if needed
    option network 'guest'
    # Likely Leave as Orion or OrionWiFi if using orion. But SSID can be anything you want.
    option ssid 'OrionWiFi'
    # Specify the IP address type availability as '11'.
    # IP Address Type Availability (ANQP) setting that indicates the availability of IP address types on the Passpoint network.
    # The value '11' informs Passpoint clients that both IPv4 and IPv6 addresses are available on the network.
    # It helps clients understand the network's IP address capabilities.
    # Refer to IEEE Std 802.11-2016, Section 9.4.2.72 for more details on IP Address Type Availability.
    option iw_ipaddr_type_availability '11'
    # Local time zone as specified in 8.3 of IEEE Std 1003.1-2004
    # Set as CST, Feel free to customize or omit.
    # stdoffset[dst[offset][,start[/time],end[/time]]]
    # We've defaulted it to Central Standard Time (most of our US based readers are in CST/CDT.)
    option time_zone 'CST6CDT,M3.2.0,M11.1.0'
    # Specify the access network type as '2' (Chargeable public network).
    # Access Network Type (ANQP) is set to '2' indicating a Chargeable public network.
    # This value informs clients that the network requires payment for access.
    # Refer to IEEE Std 802.11-2016, Section 9.4.2.72 for more details.
    option iw_access_network_type '2'
    # Specify the network authentication type as '00'.
    # Network Authentication Type (ANQP) setting that specifies the network's authentication type for Passpoint.
    # The value '00' indicates that the network authentication is open or unspecified.
    # It informs Passpoint clients about the type of authentication used by the network.
    # Refer to IEEE Std 802.11-2016, Section 9.4.2.72 for more details on Network Authentication Type.
    option iw_network_auth_type '00'
    # Operator-friendly name for Hotspot 2.0. (Can be anything you'd like as long as it is prefixed with your lang code.)
    option hs20_oper_friendly_name 'eng:Orion'
    # List of venue names associated with the Passpoint network, specifying language code and venue information. (Can be anything you'd like as long as it is prefixed with your lang code.)
    list iw_venue_name 'eng:Orion'
    # List of venue URLs associated with the Passpoint network, specifying language code and URL. (Can be any https url. Will Popup as notification on devices that connect.)
    list iw_venue_url '1:https://orionwifi.com'
    # List of operator icons, specifying width, height, language code, image format, and icon filename. (This doesn't need to be a valid path but must be specified on OpenWRT)
    list operator_icon '64:64:eng:image/png:operator_icon:operator_icon.png'

    #ProxyARP and 80211k are not supported on all devices, remove if you have issues.
    option proxy_arp '1'
    option ieee80211k '1'

    # Comment out what you don't need and uncomment/modify what you do.
    #AT&T / Orion 3gpp
    list iw_anqp_3gpp_cell_net '310,150'
    list iw_anqp_3gpp_cell_net '310,280'
    list iw_anqp_3gpp_cell_net '310,410'
    list iw_anqp_3gpp_cell_net '313,100'
    #T-Mobile 3gpp 
	# list iw_anqp_3gpp_cell_net '310,240'
	# list iw_anqp_3gpp_cell_net '310,260'
    # list iw_anqp_3gpp_cell_net '310,310'
    #Orion domain Names
    list iw_domain_name 'orion.area120.com'
    list iw_domain_name 'orionwifi.com'
    list iw_domain_name 'dogwood120.net'
    list iw_domain_name 'openroaming.goog'
    list iw_domain_name 'wifi.fi.google.com'
    #AT&T Domain Names
    #list iw_domain_name 'attwifi.com'
    #list iw_domain_name 'att.com'
    #list iw_domain_name 'attwireless.com'
    #T-Mobile Domain Names
    #list iw_domain_name 't-mobile.com'
    #OpenRoaming / IronWiFi Domain Names
    #list iw_domain_name 'ironwifi.net'
    #list iw_domain_name 'openroaming.org'
    #list iw_domain_name 'apple.openroaming.net'
    #list iw_domain_name 'google.openroaming.net'
    #list iw_domain_name 'ciscooneid.openroaming.net'
    # Orion / AT&T / OpenRoaming Default Consortium
    list iw_roaming_consortium 'f4f5e8f5f4'
    #EDURoam Consortium
    #list iw_roaming_consortium '5a03ba0000'
    #list iw_roaming_consortium '5a03ba0800'
    #IronWiFi Consortium
    #list iw_roaming_consortium 'AA146B0000'
    #list iw_roaming_consortium 'BAA2D00000'
    #list iw_roaming_consortium '5A03BA0000'
    #Orion NAI Realm
    list iw_nai_realm '0,*.orion.area120.com,13[5:6],21[2:4][5:7],23[5:1][5:2],50[5:1][5:2],18[5:1][5:2]'
    #AT&T NAI Realm
    #list iw_nai_realm '0,*wlan.mnc410.mcc310.3gppnetwork.org,13[5:6],21[2:4][5:7],23[5:1][5:2],50[5:1][5:2],18[5:1][5:2]'
    #T-Mobile NAI Realm
    #list iw_nai_realm '0,*wlan.mnc260.mcc310.3gppnetwork.org,13[5:6],21[2:4][5:7],23[5:1][5:2],50[5:1][5:2],18[5:1][5:2]'
    #IronWiFi Realm
    #list iw_nai_realm '0,ironwifi,13[5:6],21[2:4][5:7]'

    # Don't Touch
    # Some options are repeated for legacy support
    # ANQP (Access Network Query Protocol) Domain ID, used to uniquely identify the Passpoint domain.
    option anqp_domain_id '0'
    # Enable BSS (Basic Service Set) transition support for efficient handovers between APs.
    option bss_transition '1'
    # Disable Directed Group Address Forwarding (DGAF) support.
    option disable_dgaf '1'
    # Set disabled to '0' to enable the interface.
    option disabled '0'
    # Identify the ap as a guest access point.
    option guest '1'
    # Enable Hotspot 2.0 support in Passpoint.
    option hotspot20 '1'
    # Enable Hotspot 2.0 (HS2) support in Passpoint.
    option hs20 '1'
    # Set the deauthentication request timeout for Hotspot 2.0.
    option hs20_deauth_req_timeout '60'
    # Enable internet access for the Passpoint network.
    option internet '1'
    # Isolate clients on the Passpoint network for enhanced security.
    option isolate '1'
    # Enable or disable ASRA (ANQP Service Required for Access).
    option iw_asra '0'
    # Disable Directed Group Address Forwarding (DGAF) for Passpoint.
    option iw_disable_dgaf '1'
    # Enable Passpoint functionality.
    option iw_enabled '1'
    # Enable or disable Emergency Services Reachability (ESR) for Passpoint.
    option iw_esr '0'
    # Enable internet access for Passpoint.
    option iw_internet '1'
    # Enable interworking with external networks for Passpoint.
    option iw_interworking '1'
    # Disable UESA (Unauthenticated Emergency Service Availability)
    option iw_uesa '0'
    # Set the mode to 'ap', indicating that the wireless interface is operating in Access Point mode.
    option mode 'ap'
    # Enable the Requested Connectivity to User Information (CUI) feature.
    # CUI is used to request user-specific information during the network selection process and is mandatory for Google Orion.
    option request_cui '1'
    # Enable the WNM (Wireless Network Management) Sleep Mode Transition with No Keys option.
    # This option allows the device to perform sleep mode transitions without exchanging keys, improving efficiency.
    option wnm_sleep_mode_no_keys '1'
```

Afterwards we need to run two commands:

#### Fixing 3GPP Bug for Hotspot 2.0 Support on OpenWRT

OpenWRT doesn't configure `hostapd` directly. It uses a script at `/lib/netifd/hostapd.sh` to convert your config at `/etc/config/wireless` to the appropriate `hostapd` config. On some distros of OpenWRT there is a bug that prevents 3GPP configurations. 

Run the following command on your device to resolve it:

```bash
sed -i '/append_iw_anqp_3gpp_cell_net() {/,/}/c\
append_iw_anqp_3gpp_cell_net() {\
    if [ -z "$iw_anqp_3gpp_cell_net_conf" ]; then\
        iw_anqp_3gpp_cell_net_conf="$1";\
    else\
        iw_anqp_3gpp_cell_net_conf="$iw_anqp_3gpp_cell_net_conf;$1";\
    fi\
}' /lib/netifd/hostapd.sh
```

> *Just one character is the issue. The script above is fine to run on all devices. It won't make any changes if the bug isn't there.*

After configuring your interface and performing the 3gpp fix, you'll run the following command to **reload your wireless config**.

```bash
wifi
```
### OpenWRT Wireless Config Options Explained


### Access Network Type

Configure the Access Network Type using the following format:

| Access Network Type | Description                           |
|---------------------|---------------------------------------|
| 0                   | Private network                       |
| 1                   | Private network with guest access     |
| 2                   | Chargeable public network             |
| 3                   | Free public network                   |
| 4                   | Personal device network               |
| 5                   | Emergency services only network       |
| 14                  | Test or experimental                  |
| 15                  | Wildcard                              |

**Explanation**:

- The 'Access Network Type' specifies the nature of the network, helping devices categorize and interact appropriately.
- Choose the appropriate number to define the desired network type.

##### Example Usage:

To set the Access Network Type to 'Chargeable public network':

```bash
option iw_access_network_type '2'
```

This example illustrates how to configure the Access Network Type. Adjust the value based on the characteristics of your network.

Configuring the Access Network Type provides crucial information about the nature of the network, aiding devices in understanding the available services and connectivity options.

#### Venue Info (Optional)

Configure Venue Information using the following format:

> **Group, Type**

##### Values:

|  Group  |  Type  |                Description               |
|:-------:|:------:|:-----------------------------------------:|
|    0    |    0   |                 Unspecified                |
|    1    |    7   |             Convention Center             |
|    1    |   13   |                Coffee Shop                 |
|    2    |    0   |         Unspecified Business              |
|    7    |    1   |           Private Residence               |

**Explanation**:

- Venue Information allows you to specify the group and type based on IEEE Std 802.11u-2011, 7.3.1.34.
- The 'Group' parameter represents a broader category, while 'Type' specifies the specific venue type within that group.

##### Example Usage:

- To set the Venue Group to 'Convention Center':
```plaintext
option iw_venue_group '1'
```
- To set the Venue Type to 'Coffee Shop':
```plaintext
option iw_venue_type '13'
```

These examples demonstrate how to configure Venue Information. Adjust the values according to your specific venue details.

This configuration provides additional information about the network, helping devices identify and connect based on the specified venue characteristics.

#### NAI Realm Information

One or more realms can be advertised, with each `nai_realm` line adding a new realm to the set. These parameters provide information for stations using Interworking network selection to facilitate automatic connection to a network based on credentials.

> Format: `<Encoding>,<NAI Realm(s)>[,<EAP Method 1>][,<EAP Method 2>][,...]`

##### Encoding

Choose the encoding format for the realm. The following options are available:

| Realm Format | Description                                               |
|--------------|-----------------------------------------------------------|
| 0            | Realm formatted in accordance with IETF RFC 4282           |
| 1            | UTF-8 formatted character string not following RFC 4282  |

**NAI Realm(s): Semi-colon delimited NAI Realm(s)**

> EAP Method: `<EAP Method>[:<[AuthParam1:Val1]>][<[AuthParam2:Val2]>][...]`

For EAP Method types, refer to [AuthParam (Table 8-188 in IEEE Std 802.11-2012)](http://www.iana.org/assignments/eap-numbers/eap-numbers.xhtml#eap-numbers-4).

**ID 2 = Non-EAP Inner Authentication Type**

|  ID  |      Authentication Type     |
|:----:|:-----------------------------:|
|   1  |             PAP               |
|   2  |             CHAP              |
|   3  |            MSCHAP             |
|   4  |           MSCHAPV2            |

**ID 3 = Inner Authentication EAP Method Type**

*No specific values.*

**ID 5 = Credential Type**

|  ID  |         Credential Type          |
|:----:|:--------------------------------:|
|   1  |               SIM                |
|   2  |              USIM                |
|   3  | NFC Secure Element                |
|   4  |          Hardware Token          |
|   5  |            Softoken              |
|   6  |            Certificate           |
|   7  |      Username/Password           |
|   9  |            Anonymous              |
|  10  |       Vendor Specific             |

**Examples:**

- `list iw_nai_realm '0,example.com;example.net'`
- `list iw_nai_realm '0,example.org,13[5:6],21[2:4][5:7]'`

These examples demonstrate configuring EAP methods such as EAP-TLS with a certificate and EAP-TTLS/MSCHAPv2 with a username/password. Adjust the parameters based on your specific requirements.

#### WAN Metrics (Optional)

Configure WAN Metrics using the following format:

> `<WAN Info>:<DL Speed>:<UL Speed>:<DL Load>:<UL Load>:<LMD>`

**WAN Info**: B0-B1: Link Status, B2: Symmetric Link, B3: Capability (encoded as two hex digits)

- **Link Status**: 1 = Link up, 2 = Link down, 3 = Link in test state

- **Downlink Speed**: Estimate of WAN backhaul link current downlink speed in kbps (1..4294967295; 0 = unknown)

- **Uplink Speed**: Estimate of WAN backhaul link current uplink speed in kbps (1..4294967295; 0 = unknown)

- **Downlink Load**: Current load of downlink WAN connection (scaled to 255 = 100%)

- **Uplink Load**: Current load of uplink WAN connection (scaled to 255 = 100%)

- **Load Measurement Duration**: Duration for measuring downlink/uplink load in tenths of a second (1..65535); 0 if load cannot be determined

**Example**: 

```bash
option hs20_wan_metrics '01:8000:1000:80:240:3000'
```

This example sets WAN Metrics with link status up, downlink speed of 8000 kbps, uplink speed of 1000 kbps, 80% downlink load, 24% uplink load, and a load measurement duration of 3000 tenths of a second. Adjust the values based on your specific WAN characteristics.

#### IP Address Type Availability

Configure IP Address Type Availability using the following format:

> `<1-octet encoded value as hex str>` 
`((ipv4_type & 0x3f) << 2) | (ipv6_type & 0x3)`

##### ipv4 type:

|  IPv4 Type  |             Description            |
|:------------:|:----------------------------------:|
|      0       |    Address type not available     |
|      1       |    Public IPv4 address available  |
|      2       | Port-restricted IPv4 address available  |
|      3       | Single NATed private IPv4 address available |
|      4       | Double NATed private IPv4 address available |
|      5       | Port-restricted IPv4 address and single NATed IPv4 address available |
|      6       | Port-restricted IPv4 address and double NATed IPv4 address available |
|      7       | Availability of the address type is not known |

##### ipv6 type:

|  IPv6 Type  |             Description            |
|:------------:|:----------------------------------:|
|      0       |    Address type not available     |
|      1       |      Address type available       |
|      2       | Availability of the address type not known |

**Explanation**:

- The configuration format involves a 1-octet encoded value as a hexadecimal string.
- For IPv4 type, it combines bits using bitwise operations to represent the type of IPv4 address availability.
- For IPv6 type, it represents the availability of the address type.

**Example Usage**: 

```bash
option iw_ipaddr_type_availability '11'
```

This example sets IP Address Type Availability with IPv4 type available and IPv6 type available. Adjust the values based on your specific requirements.

This configuration informs the system that both public IPv4 and available IPv6 addresses can be used. The '11' is a combination of the binary representation for IPv4 availability (01) and IPv6 availability (01).

### Troubleshooting OpenWRT and Best Practices for Hotspot 2.0

#### Hostapd Configuration Checks

Before delving into troubleshooting, it's crucial to perform thorough checks on the Hostapd configuration. Start by examining the configuration file located at `/var/run/hostapd-phyX.conf` for any errors or inconsistencies. Use the following command to review the specific configuration file for a particular interface:

```bash
cat /var/run/hostapd-phyX.conf | grep bssid
```

Ensure that the MAC address specified in the configuration matches the actual MAC address of the wireless interface. Verify this by checking the MAC address in both `/sys/class/ieee80211/phyX/macaddress` and `/var/run/hostapd-phyX.conf`.

#### Debugging Hostapd Execution

When encountering issues, it's beneficial to run Hostapd in debug mode to gather detailed information about the initialization process. Execute the following commands for the respective interfaces, replacing `X` with the appropriate interface number:

```bash
hostapd -dddd -B -P /var/run/hostapd-phyX.pid /var/run/hostapd-phyX.conf
```
Examine the debug output for any error messages or warnings that might provide insights into the cause of the problem.

#### Luci Configuration Page

If the wireless interface fails to start, the Luci configuration page offers a convenient way to troubleshoot and resolve issues. Follow these steps:

1. Access the Luci web interface.
2. Navigate to the configuration page for the problematic wireless interface.
3. Disable the `proxyarp` option, save the configuration changes.
4. Click "Save & Apply"

Check the system logs using `logread` for any error messages during this reconfiguration phase.

> **Note:** *We understand that per spec that proxyarp should be left on if at all possible. However, we did have a number of OpenWRT devices have issues with this.*

#### Channel and Power Level Settings

Some devices and radios may require specific channel and power level configurations for optimal performance. Verify that the channel and power settings align with the hardware specifications of your wireless device. Incorrect settings can lead to interface startup failures.

Always consult the device documentation or specifications to determine the recommended channel and power level configurations. Adjust the settings accordingly in the wireless configuration file or luci interface.

By meticulously examining these aspects and following the outlined steps, you can troubleshoot common issues associated with Hostapd and enhance the stability of your Hotspot 2.0 implementation.

## Using USB External WiFi Cards on OpenWRT

When it comes to enhancing your OpenWRT setup with external WiFi adapters, especially for HotSpot 2.0 support, choosing the right hardware is crucial. Below, we recommend some top-performing external WiFi adapters known for their OpenWRT compatibility and 802.11 AX support.

### Recommended External WiFi Adapters for HotSpot 2.0 Support on OpenWRT

We recommend these adapters for their overall OpenWRT compatibility and 802.11 AX Support. Top down, best to worst.

- [ALFA AWUS036AXML 802.11axe WiFi 6E USB 3.0 Adapter AXE3000, Tri Band 6 GHz](https://amzn.to/3vYvHT4)

{{< centerbutton href="https://amzn.to/3vYvHT4">}}Get Your ALFA AWUS036AXML Today!{{< /centerbutton >}}

- [ALFA AWUS036AXM WiFi 6E USB 3.0 USB Adapter, AXE3000 Tri-Band 6Ghz/5.8GHz/2.4GHz](https://amzn.to/3UrQVTG)

{{< centerbutton href="https://amzn.to/3UrQVTG">}}Get Your ALFA AWUS036AXM Today!{{< /centerbutton >}}

- [NETGEAR WiFi AC1200 USB 3.0 Adapter (A6210)](https://amzn.to/42m7EJZ)

{{< centerbutton href="https://amzn.to/42m7EJZ">}}Get Your NETGEAR A6210 Today!{{< /centerbutton >}}

> *For a list of other documented adapters that have support on Linux and OpenWRT See the [USB-WiFi Documentation Repo](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)*

### Installing Drivers

```bash
#Add any more drivers you may need. 
#The most popular WiFi 5 and WiFi 6 adapters, including our recommended should be covered below.
#Command order and seperation matters.
opkg --force-removal-of-dependent-packages remove kmod-mt7921-common kmod-mt7921-firmware kmod-mt7921e kmod-mt7921s kmod-mt7921u kmod-mt76x2u
opkg --force-overwrite install kmod-mt7921-common kmod-mt7921-firmware kmod-mt7921e kmod-mt7921s kmod-mt7921u kmod-mt76x2u kmod-ath10k-smallbuffers kmod-ath9k kmod-ath9k-common kmod-ath kmod-mac80211 kmod-cfg80211
opkg --force-overwrite install kmod-thermal kmod-cfg80211 kmod-mac80211 kmod-mt76-connac kmod-mt76-core kmod-mt76-usb kmod-mt7615-common kmod-mt7615-firmware kmod-mt7615e kmod-mt76x0-common kmod-mt76x02-common kmod-mt76x02-usb kmod-mt76x0u kmod-mt76x2-common kmod-mt76x2u kmod-mt7915e kmod-mt7916-firmware
```

## Q&A Section

### Q1: What is Hotspot 2.0 / Passpoint 2.0?

Hotspot 2.0, also known as Passpoint 2.0, is a Wi-Fi Alliance certification program that enhances the connectivity experience by providing seamless and secure Wi-Fi access. It simplifies the process of connecting to Wi-Fi networks, especially in public spaces, by automating the authentication and connection procedures.

### Q2: Why is Hotspot 2.0 relevant for OpenWRT users?

OpenWRT users can benefit from Hotspot 2.0 by creating advanced wireless networks that offer improved security, automatic connection, and a seamless user experience. It is particularly useful for environments where multiple access points are deployed, such as public spaces, businesses, and large-scale deployments.

### Q3: What are the prerequisites for setting up Hotspot 2.0 on OpenWRT?

Before configuring Hotspot 2.0 on OpenWRT, ensure the following prerequisites are met:
- OpenWRT-compatible device with a Passpoint-capable wireless device (PHY).
- OpenWRT version 21.02 or newer, including wpad built with the hs20 option.
- Full version of the iw package in OpenWRT.
- An 802.1x infrastructure with a RADIUS server.
- Information about the assigned RADIUS servers, including IP address, port numbers, and shared secrets.
- Advanced command line experience (prefered but optional)
- Linux and troubleshooting experience (prefered but optional)

### Q4: How can I check if my device supports Hotspot 2.0?

You can check if your device supports Hotspot 2.0 by examining the installed wpad package. Run the following command:
```bash
strings /usr/sbin/wpad | grep hs20
```
If nothing shows up, your wpad version doesn't support Hotspot 2.0, and you may need to install a compatible version.

### Q5: Can I use USB external WiFi cards for Hotspot 2.0 support on OpenWRT?

Yes, USB external WiFi cards can be used on OpenWRT for Hotspot 2.0 support. We recommend specific adapters with OpenWRT compatibility and 802.11 AX support for an optimal experience.

{{< centerbutton href="https://amzn.to/3vYvHT4">}}Get Your ALFA AWUS036AXML Today!{{< /centerbutton >}}

### Q6: How do I troubleshoot issues with Hotspot 2.0 on OpenWRT?

If you encounter issues, you can troubleshoot by checking the configuration files, verifying MAC addresses, and ensuring proper settings in the Luci configuration page. Additionally, for interface startup issues, disable and re-enable proxyarp in the Luci configuration.
______

## Conclusion

Implementing Hotspot 2.0 on OpenWRT provides a robust solution for enhancing Wi-Fi connectivity. From improving user experience to addressing security concerns, this technology plays a pivotal role in modern wireless networks. By following the outlined steps and best practices, you can create a seamless and secure Hotspot 2.0-enabled environment.

{{< centerbutton href="https://amzn.to/3UnfDEw" description="GL.iNet GL-MT6000(Flint 2) WiFi 6 Router | Gaming WiFi Router | 2 x 2.5G Multi-Gig Port+4 x 1G Ethernet Ports | Mass Device Connectivity | Rapid OpenVpn & WireGuard | 802.11ax | Long Range Coverage " >}}Get Your GL.iNet GL-MT6000(Flint 2) Today!{{< /centerbutton >}}

## References
- [802.11 Operating Classes](https://mentor.ieee.org/802.11/dcn/10/11-10-0564-00-0s1g-operating-classes.ppt)
- [Android - Passpoint (Hotspot 2.0)](https://source.android.com/docs/core/connect/wifi-passpoint)
- [Apple Platform Deployment - Intro to mobile device management profiles](https://support.apple.com/guide/deployment/intro-to-mdm-profiles-depc0aadd3fe/1/web/1.0)
- [AuthParam (Table 8-188 in IEEE Std 802.11-2012)](http://www.iana.org/assignments/eap-numbers/eap-numbers.xhtml#eap-numbers-4)
- [Cambium Enterprise Wi-Fi and Google Orion Wi-Fi Deployment Guide](https://www.cambiumnetworks.com/wp-content/uploads/2020/10/Cambium-Enterprise-Wi-Fi-and-Google-Orion-Wi-Fi-Deployment-Guide.pdf)
- [Configure Juniper Mist Cloud](https://www.mist.com/wp-content/uploads/Example-Configure-Hotspot-2.0-with-Orion-WiFi.pdf)
- [Configure RUCKUS wireless LAN controller 5](https://docs.google.com/document/d/e/2PACX-1vRh81adM12GG7lY3vauxEd-rID4A6xbc91mzurin8bGVW9L80XqRnRBgTYOJ75CHwOGl-8v-o6OByrP/pub)
- [Configure Wi-Fi APs for Orion](https://support.google.com/orion-wifi/answer/14528189?hl=en&ref_topic=12673678&sjid=4937468210388342306-NA)
- [Configuring Hotspot 2.0 (Passpoint) on OpenWrt](https://hgot07.hatenablog.com/entry/2022/03/21/231715)
- [EAP Method Types](https://www.iana.org/assignments/eap-numbers/eap-numbers.xhtml#eap-numbers-4)
- [Freeradius](https://wiki.freeradius.org/guide/Getting-Started)
- [HotSpot 2.0 MDM settings for Apple devices](https://support.apple.com/guide/deployment/hotspot-20-settings-depea26c29b9/web)
- [IEEE 802.11u Standard](https://www.ieee.org/)
- [MikroTik - Configuration guide using native RadSec and Orion Wifi](https://help.mikrotik.com/docs/display/ROS/Interworking+Profiles#InterworkingProfiles-ConfigurationguideusingnativeRadSecandOrionWifi:)
- [Mobile Country Code (MCC) and Mobile Network Code (MNC)](https://www.itu.int/en/ITU-T/inr/nnp/Pages/mcc-mnc.aspx)
- [OpenWRT Documentation](https://openwrt.org/)
- [OpenWrt - Passpoint configuration](https://www.ironwifi.com/help/openwrt-passpoint)
- [Orion - Ubiquiti UniFi Deployment Guide](https://support.google.com/orion-wifi/answer/12759869)
- [Passpoint Certification](https://www.wi-fi.org/discover-wi-fi/wi-fi-certified-passpoint)
- [RFC 7542](https://datatracker.ietf.org/doc/html/rfc7542)
- [WBA specification for PPS-MO extensions](https://wballiance.com/resource/wba-pps-mo-extensions/)
- [Wi-Fi Alliance (WFA) - PassPoint](https://www.wi-fi.org/discover-wi-fi/passpoint)
- [Wi-Fi Alliance (WFA)](https://www.wi-fi.org/)
- [Wikipedia - Wi-Fi hotspot](https://en.wikipedia.org/wiki/Wi-Fi_hotspot)
- [Windows - Passpoint](https://learn.microsoft.com/en-us/windows-hardware/drivers/mobilebroadband/passpoint)
- [Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications](https://ieeexplore.ieee.org/iel5/6361246/6361247/06361248.pdf)
- [[Orion 2022 Guide] ArubaOS Initial Setup](https://docs.google.com/document/u/0/d/e/2PACX-1vSiHM7Rof4YaX2h5NheiD4RWDnw376BFedgnGJmk_rhgctreFDv3vvFRR3sem45pUGJ3TBiAh7r2qh0/pub?pli=1)
- [[Orion 2022 Guide] Cisco 9800 Initial Setup](https://docs.google.com/document/d/e/2PACX-1vRVlZKhmzivG8kJI2PSSTrQGN6CLGym1DkFzEYsF8Y6PfhklDQF7Sp_hdRYFtoh20vf-k9eAATiM7tz/pub)
- [[Orion 2022 Guide] FortiGate Initial Setup](https://docs.google.com/document/u/1/d/e/2PACX-1vTFGddllsSXmXfbmNlJ2MP8TciMqqBKbOKXDSqYLc9qxm3iPELX_kbpkDtkwJpK2kdQi_lztd6l2Ue8/pub)
- [[Orion 2022 Guide] Meraki Hotspot 2.0 Initial Setup](https://docs.google.com/document/d/e/2PACX-1vQTTIC6OKwvURbqyO29ZK6pgofAe1D-AsnNodyrnFnxZmY8h4Ln_SbLRoH0xzQKG1kNcpzT3eNstehQ/pub)
- [aosp/718508](https://android-review.googlesource.com/c/platform/frameworks/opt/net/wifi/+/718508)
- [google-area120/orion-radsec](https://github.com/google-area120/orion-radsec)
- [hostap default config](https://w1.fi/cgit/hostap/plain/hostapd/hostapd.conf)
- [morrownr/USB-WiFi](https://github.com/morrownr/USB-WiFi)
- [simeononsecurity/orion-radsec](https://github.com/simeononsecurity/orion-radsec/tree/sos-dev)