---
title: "HP t740 থিন ক্লায়েন্টে pfSense চালানো: টিপস এবং ট্রাবলশুটিং গাইড"
draft: false
toc: true
date: 2023-04-29
description: "HP t740 থিন ক্লায়েন্টে কীভাবে pfSense সেট আপ করবেন এবং হিমায়িত এবং SSD সনাক্তকরণ সমস্যার মতো সম্ভাব্য সমস্যাগুলি কীভাবে সমাধান করবেন তা শিখুন।"
tags: ["pfSense", "OPNsense", "শক্ত বিএসডি", "HP t740", "পাতলা ক্লায়েন্ট", "হোম সার্ভার", "PPPoE", "ফ্রিবিএসডি", "বুট প্রম্পট", "loader.conf.local", "ন্যানো সম্পাদক", "এসএসডি সনাক্তকরণ", "M.2 SSD", "পশ্চিমা ডিজিটাল", "সমস্যা সমাধান", "পোস্ট-ইনস্টলেশন", "UART", "ESXi", "প্রক্সমক্স"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "একটি জাদুকরের একটি কার্টুন একটি হিমায়িত কম্পিউটার ঠিক করার জন্য একটি বানান কাস্ট করছে, একটি বক্তৃতা বুদ্বুদ সহ বলছে সমস্যা সমাধান"
coverCaption: ""
---
 HP t740 থিন ক্লায়েন্টে pfSense, OPNsense, বা HardenedBSD**

আপনি যদি pfSense, OPNsense বা HardenedBSD চালানোর জন্য একটি শক্তিশালী ডিভাইস খুঁজছেন, তাহলে HP t740 Thin Client আপনার জন্য উপযুক্ত পছন্দ হতে পারে।

## আরও পাওয়ার এবং কমপ্যাক্ট হোম সার্ভার

HP t740 Thin Client হল একটি কমপ্যাক্ট ডিভাইস যা একটি শক্তিশালী pfSense বক্স বা একটি কমপ্যাক্ট হোম সার্ভার হিসাবে ব্যবহার করা যেতে পারে। এটি t730 বা t620 প্লাসের চেয়ে বেশি শক্তি সরবরাহ করে, যা এটিকে PPPoE চালানোর জন্য একটি উপযুক্ত পছন্দ করে তোলে, বিশেষ করে যদি আপনার কাছে ফাইবার ইন্টারনেট থাকে। এটি 10 গিগাবিট নেটওয়ার্কিং-এ একটি আপগ্রেড পথও অফার করতে পারে।

## PS/2 হিমায়িত

যাইহোক, যদি আপনি FreeBSD বা এর ডেরিভেটিভ যেমন pfSense, OPNsense, বা HardenedBSD চালানোর পরিকল্পনা করেন (যেমন ESXi বা Proxmox এর ভিতরে), তাহলে আপনি একটি সমস্যার সম্মুখীন হতে পারেন যেখানে সিস্টেম বুট করার সময় `atkbd0: [ মেসেজ দিয়ে জমে যায়। জায়ান্ট-লকড]`। সৌভাগ্যবশত, বুট প্রম্পটে নিম্নলিখিত কমান্ডগুলি প্রবেশ করে এই সমস্যাটি সমাধান করা যেতে পারে:

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

এই পদক্ষেপগুলি ইনস্টলেশন প্রক্রিয়া চলাকালীন এবং পরে দেখা দিতে পারে এমন বেশিরভাগ সমস্যার সমাধান করা উচিত।

### তথ্যসূত্র:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)