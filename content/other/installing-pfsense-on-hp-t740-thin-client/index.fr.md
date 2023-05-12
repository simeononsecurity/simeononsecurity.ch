---
title: "Exécution de pfSense sur le client léger HP t740 : conseils et guide de dépannage"
draft: false
toc: true
date: 2023-04-29
description: "Découvrez comment configurer pfSense sur le client léger HP t740 et comment résoudre les problèmes potentiels tels que les problèmes de blocage et de détection de SSD."
tags: ["pfSense","OPNsense","BSD renforcé","HP t740","client léger","serveur domestique","PPPoE","FreeBSD","invite de démarrage","loader.conf.local", "nano-éditeur","Détection SSD","SSD M.2",« Numérique occidental »,"dépannage","post-installation","UART","ESXi","Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Un dessin animé d'un sorcier jetant un sort pour réparer un ordinateur gelé, avec une bulle disant "Problème résolu"
coverCaption: ""
---
 pfSense, OPNsense ou HardenedBSD sur le client léger HP t740**

Si vous recherchez un périphérique puissant pour exécuter pfSense, OPNsense ou HardenedBSD, le client léger HP t740 pourrait être un choix approprié pour vous.

## Plus de puissance et un serveur domestique compact

Le client léger HP t740 est un appareil compact qui peut être utilisé comme un puissant boîtier pfSense ou un serveur domestique compact. Il offre plus de puissance que le t730 ou le t620 Plus, ce qui en fait un choix approprié pour exécuter PPPoE, surtout si vous avez Internet par fibre. Il peut également offrir une voie de mise à niveau vers un réseau 10 Gigabit.

## PS/2 se fige

Cependant, si vous envisagez d'exécuter FreeBSD ou ses dérivés comme pfSense, OPNsense ou HardenedBSD sur le métal nu (par opposition à ESXi ou Proxmox), vous pouvez rencontrer un problème où le système se fige au démarrage avec le message `atkbd0 : [ GÉANT-VERROUILLÉ]`. Heureusement, ce problème peut être résolu en saisissant les commandes suivantes à l'invite de démarrage :

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

Ces étapes devraient résoudre la plupart des problèmes pouvant survenir pendant et après le processus d'installation.

### Les références:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)