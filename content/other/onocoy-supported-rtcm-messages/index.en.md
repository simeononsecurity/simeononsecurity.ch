
---
title: "Unlocking Precision: Onocoy's Supported RTCM Messages"
date: 2023-12-10
toc: true
draft: false
description: "Discover how Onocoy supports RTCM messages, enhancing location accuracy."
genre: ["GNSS Technology", "RTK Services", "Precision Location Determination", "RTCM Messages", "Onocoy Platform", "Satellite Navigation", "Geospatial Data", "Navigation Corrections", "GNSS Receivers", "Geolocation Accuracy"]
tags: ["Onocoy Supported RTCM Messages", "RTCM3-MSM", "High-Precision Location", "RTK Services", "GNSS Receivers", "Geospatial Data", "Satellite Navigation", "Navigation Corrections", "RTCM Message Format", "GNSS Constellations", "RTK Solutions", "RTCM Standards", "Precision GPS Data", "Location Determination", "Geolocation Accuracy", "Onocoy Platform", "RTCM Messages Overview", "RTCM Message Types", "RTCM Corrections", "Location-Based Services", "GNSS Technology", "RTCM Guidelines", "RTCM Data", "RTCM Compliance", "RTCM Support", "Geospatial Accuracy", "GNSS Data", "Onocoy Solutions", "RTCM Message Prerequisites", "RTCM Information"]
cover: "/img/cover/gps-satellite-world-accuracy.png"
coverAlt: "A GPS satellite beaming accuracy onto a world map."
coverCaption: "Precision at Your Fingertips"
ref: ["/other/onocoy-gps-gnss-reciever-basestation-on-a-budget", "/guides/budget-diy-gps-gnss-base-station-setup-esp32-um980"]
---

**Understanding Onocoy's Support for RTCM Messages**

## Introduction

Real-Time Kinematic (RTK) positioning relies on precise correction data provided through RTCM (Radio Technical Commission for Maritime Services) messages. These messages play a pivotal role in ensuring the accuracy of GNSS (Global Navigation Satellite System) receivers. Onocoy, a leading RTK service or platform, provides support for specific RTCM messages. In this article, we'll explore Onocoy's support for RTCM messages and its implications for achieving high-precision location determination.

### RTCM3-MSM Messages: Deciphering the Format

RTCM3-MSM (Multi-Signal Messages) is a family of RTCM messages that carry crucial correction data. These messages are numbered from 1071 to 1137 and adhere to a specific format:

`1[CC][M]`

Here's what these elements represent:

- **CC - GNSS Constellation**: The two-digit code signifies the GNSS constellation associated with the message. Common codes include:
   - 07 = GPS (United States)
   - 08 = Glonass (Russia)
   - 09 = Galileo (European Union)
   - 10 = SBAS (Satellite-Based Augmentation System, various)
   - 11 = QZSS (Japan)
   - 12 = Beidou (China)
   - 13 = IRNSS (Indian Regional Navigation Satellite System)

- **M - MSM Type**: A numeric value between 1 and 7, indicating the MSM type. While different MSM types convey similar data, they differ in precision and data payload size. Higher MSM types generally provide more accurate information.

### Onocoy's Approach to RTCM Messages

Onocoy adopts a carefully tailored approach to RTCM3-MSM messages. Let's delve into the key aspects:

#### Excluding SBAS Messages

Onocoy consciously disregards RTCM3-MSM messages related to SBAS constellations, while actively supporting and rewarding the use of RTCM3-MSM messages from other GNSS constellations. 
This means that RTCM messages like `1104` and `1107` are ignored.

#### Minimum Requirement: MSM Type 4

Onocoy sets a prerequisite for a minimum MSM type 4 message. Any lower MSM types, such as MSM1, MSM2, or MSM3, are not processed, ensuring that only high-precision data is considered.

#### Avoiding Redundancy

Simultaneously sending multiple MSM messages, like both MSM 4 and MSM 7, serves no practical purpose. Onocoy filters out lower-quality MSM messages, prioritizing accuracy.

#### Ideal Message Configuration

For an optimal GNSS receiver setup, the transmission of RTCM messages `1077`, `1087`, `1097`, `1117`, `1127`, and `1137` is recommended. If these aren't available, using their MSM type 4 counterparts (`1074`, `1084`, `1094`, `1114`, `1124`, and `1134`) is a suitable alternative. It's essential to select messages aligning with the supported constellations of your receiver, excluding irrelevant ones.

##### Ideal MSM7 Configuration

- `1006` (Optional): Provides GPS Network Real-Time Kinematic (RTK) Station Information.
- `1033` (Optional): Conveys information about the GNSS antenna and receiver.
- `1077`: Delivers GPS RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections.
- `1087`: Provides GLONASS RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections.
- `1097`: Conveys Galileo RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections.
- `1117`: Transmits QZSS RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections.
- `1127`: Delivers BeiDou RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections.
- `1137`: Provides IRNSS RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections.
- `1230`: Contains Glonass Code-Phase Biases, which are vital when sending Glonass MSM messages like 1087.

##### Ideal MSM4 Baseline / Legacy Configuration

- `1074`: Delivers GPS RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections using MSM type 4.
- `1084`: Provides GLONASS RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections using MSM type 4.
- `1094`: Conveys Galileo RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections using MSM type 4.
- `1114`: Transmits QZSS RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections using MSM type 4.
- `1124`: Delivers BeiDou RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections using MSM type 4.
- `1134`: Provides IRNSS RTK Network Real-Time Kinematic (RTK) reference station parameters and network corrections using MSM type 4.
- `1230`: Contains Glonass Code-Phase Biases, which are vital when sending Glonass MSM messages like 1084.


#### Legacy RTK Messages

In cases where a receiver lacks support for MSM messages but can process legacy RTK messages such as `1004` and `1012`, they can be transmitted. However, it's crucial to note that this may lead to lower rewards, as it provides GPS+GLO dual-frequency data, which is less precise.

### Additional Supported Messages

Apart from RTCM3-MSM messages, Onocoy also extends support to these RTCM messages:

- **1005/1006**: A choice between either 1005 or 1006 (not both).
- **1230**: Glonass Biases, particularly vital when sending Glonass MSM messages like 1084 or 1087.
- **1033**: Antenna/Receiver description.



## Conclusion

Onocoy's support for RTCM messages is instrumental in ensuring the utmost accuracy and reliability of GNSS receivers across a variety of applications. Understanding the specific RTCM3-MSM message types and their alignment with supported GNSS constellations, as well as the minimum MSM type requirement, is paramount for optimizing the use of Onocoy's RTK solutions. By adhering to these guidelines, users can harness the full potential of their GNSS receivers, be it for surveying, agriculture, or any precision location-based task.

## References

1. [RTCM Official Website](https://www.rtcm.org/)
2. [Government Regulations for GNSS Usage](https://www.gsa.europa.eu/regulations)
3. [RTCM Standard 10403.3](https://rtcm.myshopify.com/)
4. [Onocoy Documentation](https://docs.onocoy.com/documentation/quick-start-guides/mine-rewards/3.-connect-your-station-to-onocoy)
5. [RTCM3 Message List](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/)
6. [RTCM messages v2.3](https://ge0mlib.com/papers/Protocols/RTCM_SC-104_v2.3.pdf)
7. [RTCM messages v3.2](https://ge0mlib.com/papers/Protocols/RTCM_SC-104_v3.2.pdf)
8. [GNSS (RTK) -- RTCM protocol's descriptions and standards](https://ge0mlib.com/papers.html#Standards)
