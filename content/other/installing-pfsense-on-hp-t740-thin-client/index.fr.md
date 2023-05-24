---
title: "Exécution de pfSense sur le client léger HP t740 : conseils et guide de dépannage"
draft: false
toc: true
date: 2023-04-29
description: "Découvrez comment configurer pfSense sur le client léger HP t740 et comment résoudre les problèmes potentiels tels que les problèmes de blocage et de détection de SSD."
tags: ["pfSense", "OPNsense", "BSD renforcé", "HP t740", "client léger", "serveur domestique", "PPPoE", "FreeBSD", "invite de démarrage", "loader.conf.local", "nano-éditeur", "Détection SSD", "SSD M.2", "Numérique occidental", "dépannage", "post-installation", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Un dessin animé d'un assistant jetant un sort pour réparer un ordinateur gelé, avec une bulle disant Problème résolu"
coverCaption: ""
---
 pfSense, OPNsense ou HardenedBSD sur le client léger HP t740**

Si vous recherchez un périphérique puissant pour exécuter pfSense, OPNsense ou HardenedBSD, le client léger HP t740 pourrait être un choix approprié pour vous.

## Plus de puissance et un serveur domestique compact

Le client léger HP t740 est un appareil compact qui peut être utilisé comme un puissant boîtier pfSense ou un serveur domestique compact. Il offre plus de puissance que le t730 ou le t620 Plus, ce qui en fait un choix approprié pour exécuter PPPoE, surtout si vous avez Internet par fibre. Il peut également offrir une voie de mise à niveau vers un réseau 10 Gigabit.

## PS/2 se fige

Cependant, si vous prévoyez d'exécuter FreeBSD ou ses dérivés comme pfSense, OPNsense ou HardenedBSD sur le métal nu (par opposition à ESXi ou Proxmox), vous pouvez rencontrer un problème où le système se fige au démarrage avec le message `atkbd0: [GIANT-LOCKED]` Heureusement, ce problème peut être résolu en saisissant les commandes suivantes à l'invite de démarrage :

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Notez que vous devez désactiver les deux, sinon, il se bloquera toujours au démarrage.*

Après avoir installé le système d'exploitation, ouvrez un shell de post-installation et exécutez la commande suivante :

```bash
vi /boot/loader.conf.local
```
Ensuite, ajoutez ces deux lignes :
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Persistance des modifications à l'aide de VI
Pour ceux qui ne connaissent pas vi, vous pouvez ajouter la ligne en procédant comme suit :

Ajout des lignes `hint.uart.0.disabled="1"` et `hint.uart.1.disabled="1"` au `/boot/loader.conf.local` fichier à l'aide de l'éditeur vi peut être effectué en procédant comme suit :

1. Ouvrez le terminal sur votre système FreeBSD.

2. Tapez `vi /boot/loader.conf.local` et appuyez sur Entrée pour ouvrir le fichier dans l'éditeur vi.

3. Appuyez sur la `i` touche pour entrer en mode insertion.

4. Déplacez le curseur vers le bas du fichier à l'aide des touches fléchées.

5. Tapez `hint.uart.0.disabled="1"` sans les guillemets.

6. Appuyez sur Entrée pour commencer une nouvelle ligne.

7. Tapez `hint.uart.1.disabled="1"` sans les guillemets.

8. Appuyez sur la `Esc` touche pour quitter le mode d'insertion.

9. Taper `:wq` et appuyez sur Entrée pour enregistrer et quitter le fichier.

Cela ajoutera les deux lignes au `/boot/loader.conf.local` fichier, qui désactivera les UART et résoudra le problème de blocage lors du démarrage sur certains appareils HP t740 "Client léger" lors de l'exécution de FreeBSD ou de ses dérivés comme pfSense, OPNsense ou HardenedBSD.

Cela résoudra le problème lors des redémarrages et des mises à niveau du micrologiciel sur pfSense/OPNsense.

## SSD

Si vous utilisez HP M.2 eMMC, il ne sera pas détecté sur une installation FreeBSD prête à l'emploi. Dans ce cas, vous aurez besoin d'un SSD M.2 tiers. N'importe quel SSD M.2 peut fonctionner, SATA ou NVMe.

Si vous recherchez un SSD M.2 tiers pour votre client léger HP t740, nous vous recommandons de considérer le [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Ces deux options sont fiables et devraient bien fonctionner avec votre appareil. Si vous souhaitez profiter des deux emplacements, vous aurez besoin des deux. Vous sacrifierez les vitesses du NVME, mais vous gagnerez une redondance si importante.

Notez que l'auteur de cet article a exécuté avec succès pfSense CE 2.5.2 et OPNsense 22.1 sur leur t740 sans aucun problème après avoir suivi les étapes ci-dessus.

## Dépannage et post-installation

Après l'installation, si vous rencontrez des problèmes avec l'édition de fichiers, vous pouvez installer l'éditeur nano à l'aide de `pkg update` et `pkg install nano` Cela vous aidera à éditer facilement des fichiers texte.

Pour s'assurer que les modifications apportées au `/boot/loader.conf.local` fichier persiste à travers les mises à niveau de version de pfSense, vous devez ajouter les lignes suivantes à `/boot/loader.conf` et `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

Cependant, parfois l'édition de `/boot/loader.conf.local` fichier avant le redémarrage ne résout pas le problème. Dans de tels cas, il peut être nécessaire d'ajouter les lignes suivantes au début du premier démarrage :

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Ces étapes devraient résoudre la plupart des problèmes pouvant survenir pendant et après le processus d'installation.

### Les références:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)