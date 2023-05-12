---
title: "HP t740 ਥਿਨ ਕਲਾਇੰਟ 'ਤੇ pfSense ਚੱਲ ਰਿਹਾ ਹੈ: ਸੁਝਾਅ ਅਤੇ ਸਮੱਸਿਆ ਨਿਪਟਾਰਾ ਗਾਈਡ"
draft: false
toc: true
date: 2023-04-29
description: "ਸਿੱਖੋ ਕਿ HP t740 ਥਿਨ ਕਲਾਇੰਟ 'ਤੇ pfSense ਨੂੰ ਕਿਵੇਂ ਸੈੱਟ ਕਰਨਾ ਹੈ, ਅਤੇ ਸੰਭਾਵੀ ਸਮੱਸਿਆਵਾਂ ਜਿਵੇਂ ਕਿ ਫ੍ਰੀਜ਼ਿੰਗ ਅਤੇ SSD ਖੋਜ ਸਮੱਸਿਆਵਾਂ ਦਾ ਨਿਪਟਾਰਾ ਕਿਵੇਂ ਕਰਨਾ ਹੈ।"
tags: ["pfSense","OPNsense","HardenedBSD","HP t740","ਪਤਲੇ ਗਾਹਕ","ਹੋਮ ਸਰਵਰ","PPPoE","FreeBSD","ਬੂਟ ਪ੍ਰੋਂਪਟ","loader.conf.local", "ਨੈਨੋ ਸੰਪਾਦਕ","SSD ਖੋਜ","M.2 SSD","ਪੱਛਮੀ ਡਿਜੀਟਲ","ਸਮੱਸਿਆ ਨਿਪਟਾਰਾ","ਪੋਸਟ-ਇੰਸਟਾਲੇਸ਼ਨ","UART","ESXi","ਪ੍ਰੌਕਸਮੌਕਸ"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "ਇੱਕ ਵਿਜ਼ਾਰਡ ਦਾ ਇੱਕ ਕਾਰਟੂਨ ਇੱਕ ਫ੍ਰੀਜ਼ ਕੀਤੇ ਕੰਪਿਊਟਰ ਨੂੰ ਠੀਕ ਕਰਨ ਲਈ ਇੱਕ ਸਪੈੱਲ ਸੁੱਟ ਰਿਹਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਇੱਕ ਸਪੀਚ ਬੁਲਬੁਲਾ ਕਹਿੰਦਾ ਹੈ ਕਿ ਸਮੱਸਿਆ ਹੱਲ ਹੋ ਗਈ ਹੈ"
coverCaption: ""
---
 HP t740 ਥਿਨ ਕਲਾਇੰਟ** 'ਤੇ pfSense, OPNsense, ਜਾਂ HardenedBSD

ਜੇਕਰ ਤੁਸੀਂ pfSense, OPNsense, ਜਾਂ HardenedBSD ਨੂੰ ਚਲਾਉਣ ਲਈ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਡਿਵਾਈਸ ਲੱਭ ਰਹੇ ਹੋ, ਤਾਂ HP t740 ਥਿਨ ਕਲਾਇੰਟ ਤੁਹਾਡੇ ਲਈ ਇੱਕ ਢੁਕਵਾਂ ਵਿਕਲਪ ਹੋ ਸਕਦਾ ਹੈ।

## ਹੋਰ ਪਾਵਰ ਅਤੇ ਸੰਖੇਪ ਹੋਮ ਸਰਵਰ

HP t740 ਥਿਨ ਕਲਾਇੰਟ ਇੱਕ ਸੰਖੇਪ ਯੰਤਰ ਹੈ ਜੋ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ pfSense ਬਾਕਸ ਜਾਂ ਇੱਕ ਸੰਖੇਪ ਹੋਮ ਸਰਵਰ ਵਜੋਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ t730 ਜਾਂ t620 ਪਲੱਸ ਨਾਲੋਂ ਜ਼ਿਆਦਾ ਪਾਵਰ ਦੀ ਪੇਸ਼ਕਸ਼ ਕਰਦਾ ਹੈ, ਜੋ ਇਸਨੂੰ PPPoE ਚਲਾਉਣ ਲਈ ਇੱਕ ਢੁਕਵਾਂ ਵਿਕਲਪ ਬਣਾਉਂਦਾ ਹੈ, ਖਾਸ ਕਰਕੇ ਜੇਕਰ ਤੁਹਾਡੇ ਕੋਲ ਫਾਈਬਰ ਇੰਟਰਨੈਟ ਹੈ। ਇਹ 10 ਗੀਗਾਬਿਟ ਨੈੱਟਵਰਕਿੰਗ ਲਈ ਇੱਕ ਅੱਪਗਰੇਡ ਮਾਰਗ ਵੀ ਪੇਸ਼ ਕਰ ਸਕਦਾ ਹੈ।

## PS/2 ਫ੍ਰੀਜ਼

ਹਾਲਾਂਕਿ, ਜੇਕਰ ਤੁਸੀਂ FreeBSD ਜਾਂ ਇਸਦੇ ਡੈਰੀਵੇਟਿਵਜ਼ ਜਿਵੇਂ ਕਿ pfSense, OPNsense, ਜਾਂ HardenedBSD ਨੂੰ ਬੇਅਰ ਮੈਟਲ 'ਤੇ ਚਲਾਉਣ ਦੀ ਯੋਜਨਾ ਬਣਾਉਂਦੇ ਹੋ (ਜਿਵੇਂ ਕਿ ਅੰਦਰ ESXi ਜਾਂ Proxmox ਦੇ ਉਲਟ ਹੈ), ਤਾਂ ਤੁਹਾਨੂੰ ਇੱਕ ਸਮੱਸਿਆ ਆ ਸਕਦੀ ਹੈ ਜਿੱਥੇ ਸਿਸਟਮ 'atkbd0: [ ਸੁਨੇਹੇ ਨਾਲ ਬੂਟ ਹੋਣ 'ਤੇ ਫ੍ਰੀਜ਼ ਹੋ ਜਾਂਦਾ ਹੈ। GIANT-locked]`। ਖੁਸ਼ਕਿਸਮਤੀ ਨਾਲ, ਇਸ ਮੁੱਦੇ ਨੂੰ ਬੂਟ ਪ੍ਰੋਂਪਟ 'ਤੇ ਹੇਠ ਲਿਖੀਆਂ ਕਮਾਂਡਾਂ ਦਾਖਲ ਕਰਕੇ ਹੱਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:

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

ਇਹਨਾਂ ਕਦਮਾਂ ਨਾਲ ਜ਼ਿਆਦਾਤਰ ਮੁੱਦਿਆਂ ਨੂੰ ਹੱਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਜੋ ਇੰਸਟਾਲੇਸ਼ਨ ਪ੍ਰਕਿਰਿਆ ਦੌਰਾਨ ਅਤੇ ਬਾਅਦ ਵਿੱਚ ਪੈਦਾ ਹੋ ਸਕਦੇ ਹਨ।

### ਹਵਾਲੇ:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)