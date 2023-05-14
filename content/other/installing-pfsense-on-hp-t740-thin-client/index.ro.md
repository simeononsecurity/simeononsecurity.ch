---
title: "Rularea pfSense pe clientul subțire HP t740: sfaturi și ghid de depanare"
draft: false
toc: true
date: 2023-04-29
description: "Aflați cum să configurați pfSense pe clientul subțire HP t740 și cum să remediați problemele potențiale precum înghețarea și problemele de detectare a SSD-ului."
tags: ["pfSense", "OPNsense", "HardenedBSD", "HP t740", "client slab", "serverul de acasă", "PPPoE", "FreeBSD", "prompt de pornire", "loader.conf.local", "nano editor", "Detectare SSD", "SSD M.2", "Western Digital", "depanare", "post-instalare", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Un desen animat cu un vrăjitor care aruncă o vrajă pentru a repara un computer înghețat, cu un balon care spune Problema rezolvată"
coverCaption: ""
---
 pfSense, OPNsense sau HardenedBSD pe clientul subțire HP t740**

Dacă sunteți în căutarea unui dispozitiv puternic pentru a rula pfSense, OPNsense sau HardenedBSD, HP t740 Thin Client ar putea fi o alegere potrivită pentru dvs.

## Mai multă putere și compact Home Server

Clientul subțire HP t740 este un dispozitiv compact care poate fi folosit ca o cutie pfSense puternică sau ca un server de acasă compact. Oferă mai multă putere decât t730 sau t620 Plus, ceea ce îl face o alegere potrivită pentru rularea PPPoE, mai ales dacă aveți internet Fiber. De asemenea, poate oferi o cale de upgrade la rețeaua de 10 Gigabit.

## PS/2 îngheață

Cu toate acestea, dacă intenționați să rulați FreeBSD sau derivatele sale precum pfSense, OPNsense sau HardenedBSD pe bare metal (spre deosebire de ESXi sau Proxmox), este posibil să întâmpinați o problemă în care sistemul se blochează la pornire cu mesajul `atkbd0: [ GIANT-LOCKED]`. Din fericire, această problemă poate fi rezolvată prin introducerea următoarelor comenzi la promptul de pornire:

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

Acești pași ar trebui să rezolve majoritatea problemelor care pot apărea în timpul și după procesul de instalare.

### Referințe:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)