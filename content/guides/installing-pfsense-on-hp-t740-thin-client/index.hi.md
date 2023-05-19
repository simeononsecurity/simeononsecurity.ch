---
title: "HP t740 थिन क्लाइंट पर pfSense चलाना: टिप्स और ट्रबलशूटिंग गाइड"
draft: false
toc: true
date: 2023-04-29
description: "जानें कि HP t740 थिन क्लाइंट पर pfSense कैसे सेट अप करें, और फ्रीजिंग और SSD डिटेक्शन जैसी संभावित समस्याओं का निवारण कैसे करें।"
tags: ["pfSense", "ओपीएनसेंस", "कठोरबीएसडी", "एचपी टी740", "दूसरे कंप्यूटर पर निर्भर रहने वाला कंप्यूटर प्रोग्राम", "होम सर्वर", "पीपीपीओई", "FreeBSD", "बूट प्रांप्ट", "loader.conf.local", "नैनो संपादक", "एसएसडी का पता लगाने", "एम.2 एसएसडी", "पश्चिमी डिजिटल", "समस्या निवारण", "स्थापना के बाद", "यूएआरटी", "ESXi", "प्रॉक्समॉक्स"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "जमे हुए कंप्यूटर को ठीक करने के लिए जादू करने वाले जादूगर का कार्टून, जिसमें स्पीच बबल कह रहा है प्रॉब्लम सॉल्व्ड"
coverCaption: ""
---
 HP t740 थिन क्लाइंट** पर pfSense, OPNsense, या HardenedBSD**

यदि आप pfSense, OPNsense, या HardenedBSD को चलाने के लिए एक शक्तिशाली उपकरण की तलाश कर रहे हैं, तो HP t740 Thin Client आपके लिए एक उपयुक्त विकल्प हो सकता है।

## अधिक पावर और कॉम्पैक्ट होम सर्वर

HP t740 थिन क्लाइंट एक कॉम्पैक्ट डिवाइस है जिसे एक शक्तिशाली pfSense बॉक्स या एक कॉम्पैक्ट होम सर्वर के रूप में इस्तेमाल किया जा सकता है। यह t730 या t620 प्लस की तुलना में अधिक शक्ति प्रदान करता है, जो इसे PPPoE चलाने के लिए एक उपयुक्त विकल्प बनाता है, खासकर यदि आपके पास फाइबर इंटरनेट है। यह 10 गीगाबिट नेटवर्किंग के लिए अपग्रेड पथ भी प्रदान कर सकता है।

## पी एस / 2 जमा देता है

हालाँकि, यदि आप FreeBSD या इसके डेरिवेटिव जैसे pfSense, OPNsense, या HardenedBSD को नंगे धातु (ESXi या Proxmox के विपरीत) पर चलाने की योजना बनाते हैं, तो आप एक समस्या का सामना कर सकते हैं जहाँ सिस्टम 'atkbd0:' संदेश के साथ बूट पर जमा देता है। GIANT-LOCKED]`। सौभाग्य से, बूट प्रांप्ट पर निम्नलिखित कमांड दर्ज करके इस समस्या को हल किया जा सकता है:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Note that you need to unset both, otherwise, it will still lock up at boot.*

After you install the OS, open a post-installation shell and run the following command:

```bash
vi /boot/loader.conf.local
```
Then, add these two lines:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Persist Changes using VI
For those not familiar with vi, you can add the line by doing the following :

Adding the lines `hint.uart.0.disabled="1"` and `hint.uart.1.disabled="1"` to the `/boot/loader.conf.local` file using the vi editor can be done with the following steps:

1. Open the terminal on your FreeBSD system.

2. Type `vi /boot/loader.conf.local` and press Enter to open the file in the vi editor.

3. Press the `i` key to enter insert mode.

4. Move the cursor to the bottom of the file using the arrow keys.

5. Type `hint.uart.0.disabled="1"` without the quotes.

6. Press Enter to start a new line.

7. Type `hint.uart.1.disabled="1"` without the quotes.

8. Press the `Esc` key to exit insert mode.

9. Type `:wq` and press Enter to save and exit the file.

This will add the two lines to the `/boot/loader.conf.local` file, which will disable the UARTs and fix the freezing issue during boot on certain HP t740 "Thin Client" devices when running FreeBSD or its derivatives like pfSense, OPNsense, or HardenedBSD.

This will fix the issue across reboots and firmware upgrades on pfSense/OPNsense. 

## SSD

If you're using the HP M.2 eMMC, it will not be detected on an out-of-the-box FreeBSD installation. In that case, you will need a third-party M.2 SSD. Any M.2 SSD can work, SATA or NVMe. 

If you are looking for a third-party M.2 SSD for your HP t740 thin client, we recommend considering the [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V). Both of these options are reliable and should work well with your device. If you want to take advantage of both slots, you'll need both. You'll sacrifice the speeds of the NVME, but you'll gain some redundancy that's oh so important.

Note that the author of this article has successfully run pfSense CE 2.5.2 and OPNsense 22.1 on their t740 without any issues after following the above steps. 

## Troubleshooting and Post Install

After installation, if you encounter any issues with editing files, you can install the nano editor using `pkg update` and `pkg install nano`. This will help you edit text files with ease.

To ensure that the changes made to the `/boot/loader.conf.local` file persist across pfSense version upgrades, you need to add the following lines to `/boot/loader.conf` and `/etc/rc.conf.local`: 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

However, sometimes the editing of `/boot/loader.conf.local` file before rebooting doesn't fix the issue. In such cases, it may be necessary to add the following lines at the beginning of the first boot:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

इन चरणों को उन अधिकांश समस्याओं को हल करना चाहिए जो स्थापना प्रक्रिया के दौरान और बाद में उत्पन्न हो सकती हैं।

### संदर्भ:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)