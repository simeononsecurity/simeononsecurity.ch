---
title: "Geodnet MobileCM UM980 Upgrade & Alternative Mini-PCIe Cards"
date: 2023-12-28
toc: true
draft: false
description: "Discover how the UM980 upgrade card and alternative Mini-PCIe cards can supercharge your GNSS capabilities. Are MobileCM Base Stations ready for a revolution?"
genre: ["Technology", "Navigation Systems", "GNSS Upgrades", "Space Weather Stations", "Alternative GNSS Cards", "Hyfix UM980", "GNSS Reception", "Geodnet Solutions", "Satellite Technology", "Precision Positioning"]
tags: ["GNSS", "GNSS Mini-PCIe", "MobileCM Base Station", "UM980 Upgrade Card", "GNSS Correction Services", "Triple-Band GNSS", "Hyfix", "Global Navigation Satellite Systems", "USB over mPCIe", "Geodnet", "Space Weather Station", "GNSS Reception", "Alternative GNSS Cards", "Technology Solutions", "Hyfix Products", "GNSS Upgrade", "Satellite Signals", "Precision Positioning", "GNSS Testing", "Industry Standards", "Anti-Competitive Issue", "GNSS Mini-PCIe Compatibility", "UM980 Review", "Hyfix UM980 Upgrade", "GNSS Technology Landscape", "Hyfix UM980 Compatibility", "MobileCM Base Station Upgrade", "Geodnet Challenges", "GNSS Mini-PCIe Cards", "MobileCM Base Station Testing"]
cover: "/img/cover/GNSS-Satellite-Precision.png"
coverAlt: "A stylized GNSS satellite in orbit, symbolizing precision."
coverCaption: "Unlock Precision - GNSS Revolution"
ref: ["/other/onocoy-gps-gnss-reciever-basestation-on-a-budget"]
---

# Exploring Alternative Mini-PCIe GNSS Cards for MobileCM Base Stations

In the world of Global Navigation Satellite Systems (GNSS) correction services, the Global Earth Observation Decentralized Network (GEODNET) has been a game-changer, offering precision and cost-efficiency to clients. To become a part of this network, you typically need a MobileCM GNSS Base Station, which not only serves as a space weather station but also provides GNSS correction data. However, if you initially purchased the Dual-Band base station, you might be missing out on some rewards and advantages. Hyfix presents a solution, the **UM980 MobileCM Triple-Band MiniPCIe Upgrade Card**, which promises a transition to triple-band support and additional bands and channels. 

## Unlocking GNSS Potential with UM980

The [UM980 upgrade card from Hyfix](https://hyfix.ai/products/mobilecm-triple-band-minipcie-upgrade-card) is a compelling solution for MobileCM base station owners who aspire to enhance their GNSS capabilities. This upgrade offers a range of benefits, including support for **triple-band GNSS**, which encompasses the modern L5 signal and a broader spectrum of bands and channels. This significant expansion is poised to greatly enhance the precision and performance of GNSS reception.

### Assessing Alternative GNSS Mini-PCIe Cards

To evaluate the practicality of this upgrade, we embarked on a journey to explore various options and subjected them to testing. The products we procured or received for review include:

- **[GNSS.STORE UM980 Mini PCIe Receiver ELT0226](https://gnss.store/unicore-gnss-modules/251-elt0226.html)**
- **[GNSS.STORE UM982 Mini PCIe Receiver ELT0216](https://gnss.store/um982-gnss-modules/243-elt0216.html)**

### The Challenges Encountered

Our testing involved comprehensive trials of these alternative GNSS Mini-PCIe cards in both the [MobileCM Base Station](https://hyfix.ai/products/mobilecm-triple-band-gnss-base-station) and the [EVK USB-C Rover Kit](https://hyfix.ai/products/evk-usb-c-rover-kit). Regrettably, the results were unexpected. These cards were neither recognized nor operating as intended within these setups.

{{< figure src="rtkrover-mpcie-test.jpeg" alt="Trying UM980 mPCIe Card in the Hyfix USB C RTK Rover" caption="Trying UM980 mPCIe Card in the Hyfix USB C RTK Rover" >}}

However, when we tested the same cards in well-established USB over mPCIe systems and adapters, they performed admirably. When testing the Hyfix upgrade card in the same systems, it did not work. This disparity in performance left us with a puzzling conclusion.

{{< figure src="mpcie-adapter-test.jpeg" alt="Trying UM980 mPCIe Card in WWAN to USB Adapter" caption="Trying UM980 mPCIe Card in WWAN to USB Adapter" >}}

### USB Over mPCIe Standard

The most plausible explanation for this anomaly is that the MobileCM base stations may not be employing or implementing the [**industry-standard USB over mPCIe standard**](https://en.wikipedia.org/wiki/PCI_Express), also known as WWAN, commonly used by gps receiver modules, cellular modules, and wifi modules. This inconsistency in compatibility with alternative cards is unfortunate and poses a challenge for users looking to expand their GNSS capabilities.

While our testing was basic and of limited scope, we remain committed to staying updated on any developments in this regard. We will revisit this topic and update our article if changes occur or if solutions become available for MobileCM base station owners keen to explore alternatives.

### Note: Manufacturer Disclaimer

It's crucial to emphasize that this issue is not attributed to the manufacturers of the Mini PCIe cards. This is likely an **anti-competitive issue** associated with the **Geodnet/Hyfix products**.

To an extent, we can confirm this based on their LC29H Based Module Schematics, which also includes the UM980 Pinout.

{{< figure src="MCM_MINI-PCIE_SCH.jpeg" alt="Hyfix LC29H Rover mPCIe Card Schematics" caption="Hyfix LC29H Rover mPCIe Card Schematics" link="https://github.com/HYFIX/rtk_rover/blob/main/schematic/MCM_MINI-PCIE_SCH.pdf" >}}

> **Update**: *We received confirmation from gnss.store that the Hyfix MobileCM Upgrade Card itself is using a non-standard pinout that utilizes the mPCIe form factor.*

In conclusion, the GNSS technology landscape is continually evolving, and the quest for innovative solutions remains paramount. As the industry advances, we may unearth novel methods to augment the capabilities of MobileCM base stations, and we are committed to sharing these insights with the GNSS community.

______

# Conclusion

The quest for enhanced GNSS capabilities with MobileCM base stations leads us to explore the UM980 upgrade card from Hyfix and alternative Mini-PCIe cards. Our testing revealed a surprising lack of compatibility with certain Mini-PCIe cards, hinting at a potential deviation from industry standards. However, it's essential to note that this issue isn't due to the Mini PCIe card manufacturers but rather appears to be an anti-competitive matter related to the Geodnet/Hyfix products. The GNSS technology field continues to evolve, and solutions may emerge in the future. Stay updated for the latest developments in this ever-changing landscape.

______

# References

- [Hyfix UM980 MobileCM Triple-Band MiniPCIe Upgrade Card](https://hyfix.ai/products/mobilecm-triple-band-minipcie-upgrade-card)
- [GNSS.STORE UM980 Mini PCIe Receiver](https://gnss.store/unicore-gnss-modules/251-elt0226.html)
- [GNSS.STORE UM982 Mini PCIe Receiver](https://gnss.store/um982-gnss-modules/243-elt0216.html)
- [simpleRTK3b mPCIe Receiver](https://www.ardusimple.com/product/simplertk3b-mpcie-septentrio-mosaic/)

