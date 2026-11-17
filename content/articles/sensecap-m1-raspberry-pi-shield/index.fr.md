---
title: "SenseCAP M1 Raspberry Pi Shield : brochage et réutilisation LoRaWAN"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "Comprenez le shield SenseCAP M1, comparez les brochages GPIO contradictoires, examinez son ATECC608 et préparez une passerelle LoRaWAN avec une version récente de Raspberry Pi OS."
genre: ["Raspberry Pi", "IoT", "Sécurité matérielle"]
tags: ["SenseCAP M1", "Shield SenseCAP M1", "Brochage SenseCAP M1", "Shield Raspberry Pi", "Raspberry Pi HAT", "Passerelle LoRaWAN", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Réutilisation d'un hotspot Helium", "Concentrateur LoRa", "SPI GPIO", "GPIO17", "LED GPIO22", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "Diagnostics I2C", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "Rétro-ingénierie matérielle"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Shield SenseCAP M1 avec un module Seeed WM1302, un connecteur Raspberry Pi, un câble d'antenne, une prise USB-C et un connecteur de ventilateur"
coverCaption: "Photo du circuit : Clockwork Bird, 2023. Source et attribution en fin d'article."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**Le shield SenseCAP M1 convient comme matériel de passerelle LoRaWAN, mais son câblage demande davantage de vérifications qu'un tutoriel générique sur les HAT Raspberry Pi.** Ce guide complète [l'étude de Clockwork Bird publiée en 2023](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) avec les documents du fabricant, l'examen d'un pilote amont et les recommandations GPIO actuelles. Vous identifierez le matériel, distinguerez les faits établis des informations incomplètes sur le brochage et créerez un relevé de mise en service reproductible.

> **Périmètre :** ce guide matériel s'appuie sur la documentation. Les commandes et les correspondances de broches n'ont pas été testées sur un M1 physique pour cet article.

## Points essentiels

- **Identifiez les deux cartes :** le support M1 et le concentrateur amovible ont chacun leurs propres informations de modèle et de révision.
- **Vérifiez les scripts de réinitialisation :** les valeurs CoreCell par défaut entrent en conflit avec les signaux du brochage M1 publié.
- **Contrôlez les interfaces du système :** les fichiers de périphérique SPI, la numérotation GPIO et les versions des outils GPIO répondent à des questions différentes.
- **Préservez le provisionnement de l'élément sécurisé :** lire les informations du périphérique ne revient pas à le configurer ni à générer des clés.
- **Vérifiez toute la chaîne :** détecter un concentrateur ne prouve pas que les données du capteur sont transmises.

## Avant de commencer

**Difficulté : intermédiaire.** Prévoyez environ une à deux heures pour l'inventaire, la préparation du système et les vérifications documentaires. La vérification électrique, l'adaptation du pilote et le déploiement du serveur réseau demandent du travail supplémentaire, surtout si la révision de la carte est inconnue.

| Élément | Rôle |
|---|---|
| **Shield M1 et concentrateur** | Relever la révision du support et l'étiquette complète du module |
| **Raspberry Pi 4** | Commencer avec l'hôte utilisé dans la conception M1 d'origine |
| **Carte microSD de rechange** | Préparer un système distinct tout en conservant l'installation d'origine |
| **Alimentation et antenne adaptées** | Correspondre au matériel assemblé et à la bande RF du module |
| **SSH ou console locale** | Enregistrer les diagnostics et modifier la configuration |
| **Capteur et serveur LoRaWAN** | Vérifier la transmission réelle à l'application après la mise en service matérielle |
| **Multimètre et expérience matérielle** | Résoudre les connexions non documentées avant de les piloter |

Photographiez les deux faces de l'assemblage hors tension avant de démonter quoi que ce soit. Notez l'orientation des connecteurs, les vis, les entretoises et le chemin de l'antenne. Gardez la carte et la configuration d'origine disponibles jusqu'à ce que la nouvelle installation réponde aux critères d'acceptation.

## Identifiez les trois couches

**Le M1 complet, son shield support et son concentrateur sont des composants distincts.** Seeed décrit le hotspot assemblé comme un Raspberry Pi 4 avec un concentrateur WM1302/SX1302 ou WM1303/SX1303. Une annonce intitulée « SenseCAP M1 shield » ne précise pas lequel accompagne le support. [Présentation du M1 par Seeed Studio](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Le **support** relie l'alimentation et les signaux périphériques entre le Pi et le module. Le **concentrateur** gère la réception et l'émission radio. Un **transmetteur de paquets** sur l'hôte échange les paquets radio reçus et les liaisons descendantes planifiées avec un serveur. [Présentation du HAL SX1302 par Semtech](https://github.com/Lora-net/sx1302_hal)

Par exemple, un capteur de température d'étagère envoie une liaison montante par radio. Le concentrateur la reçoit, l'hôte la transmet, puis les services réseau et applicatifs la traitent. Un démarrage réussi de Linux prouve uniquement le fonctionnement de la partie hôte de cette chaîne.

La photo de Clockwork Bird montre un support M1 v1.1 avec un module portant explicitement l'étiquette `WM1302-SPI-EU868`. Utilisez-la pour repérer les étiquettes de votre matériel. Les numéros de série identifient l'équipement photographié, pas la configuration d'une autre passerelle.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Support M1 vert avec module WM1302 SPI EU868 étiqueté, à côté de l'USB-C, du bouton, du connecteur de ventilateur et du câble d'antenne" caption="Matériel M1 v1.1 photographié par Clockwork Bird, également utilisé pour la couverture de cet article" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Connexions d'alimentation et radio

**Considérez le connecteur USB-C du M1 comme une entrée d'alimentation.** Le fabricant spécifie 5 V CC, 3 A pour la passerelle complète et identifie l'USB-C comme interface d'alimentation. Le terme « port de charge » suggère une batterie absente de ces spécifications. [Spécifications du SenseCAP M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Le schéma fonctionnel du fabricant sépare l'alimentation 5 V du rail régulé 3,3 V du module. Cette distinction compte lors du dépannage : un Pi en fonctionnement peut coexister avec un concentrateur sans alimentation. N'injectez pas 5 V dans une broche de signal et ne supposez pas que les deux entrées d'alimentation sont isolées.

**Les variantes de module SPI et USB demandent des connexions hôte différentes.** La documentation WM1302 de Seeed décrit un accès SPI direct pour le modèle SPI et un pont USB STM32L4 pour le modèle USB. La forme mini-PCIe indique le format du module, tandis que les interfaces électriques documentées sont SPI ou USB. Une prise d'ordinateur portable de forme identique ne suffit pas à prouver la compatibilité. [Documentation WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc)

Avant de mettre l'assemblage sous tension, insérez le module hors tension et connectez une antenne adaptée. Faites correspondre le matériel RF, l'antenne et le plan régional prévu. Modifier le nom d'un fichier de configuration ne change pas les composants RF du module, et la prise d'alimentation M1 ne prouve pas la prise en charge d'une variante de concentrateur USB.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Schéma reliant le Raspberry Pi 4 au shield M1 par l'alimentation, SPI, GPIO et I2C" caption="Schéma du fabricant SenseCAP repris dans l'article original de Clockwork Bird, montrant la conception WM1302" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Lisez attentivement le brochage

**Notez séparément les numéros GPIO BCM et les broches physiques du connecteur.** Par exemple, le GPIO17 BCM correspond à la broche physique 11 du connecteur Pi. Le connecteur de bord du module ajoute un troisième système de numérotation : le numéro de sa broche de réinitialisation n'est pas un numéro GPIO Raspberry Pi.

Le tableau ci-dessous retranscrit les connexions de l'image annotée de Clockwork Bird. C'est une **référence communautaire**, pas un schéma complet publié par le fabricant ni une mesure de toutes les révisions M1. Le dessin porte aussi des étiquettes `SX1262`, alors que le script générique de réinitialisation Semtech utilise les noms `SX1261`.

| Signal sur le dessin | BCM / broche physique | Interprétation |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Bus de gestion partagé |
| **Réinitialisation SX1302** | GPIO17 / 11 | Candidat pour réinitialiser le concentrateur |
| **LED utilisateur** | GPIO22 / 15 | Annotation M1 |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | Signaux de données SPI |
| **Horloge SPI** | GPIO11 / 23 | Signal d'horloge SPI |
| **Sélection du SX1302** | GPIO8 / 24 | SPI0 CE0 |
| **Réinitialisation SX1262** | GPIO5 / 29 | Candidat pour réinitialiser la radio auxiliaire |
| **Sélection SX1262** | GPIO6 / 31 | GPIO6, distinct de SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Sortie d'état de la radio auxiliaire |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Signaux auxiliaires à vérifier avant usage |

Les annotations GPS/UART barrées ne prouvent pas que le M1 comporte un GPS. N'ajoutez pas de configuration GPS sauf si votre matériel en comporte un. Le schéma publié ne précise pas non plus le bouton utilisateur ni la commande du ventilateur. [Étude du brochage par Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Dessin annoté du connecteur Raspberry Pi montrant la LED M1, la réinitialisation du concentrateur, les signaux SPI et les connexions GPS barrées" caption="Référence annotée par la communauté avec une couverture incomplète des révisions, pas un schéma M1 complet" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Résolvez les conflits des scripts de réinitialisation

**Un script de réinitialisation sélectionne des sorties électriques, pas de simples préférences logicielles.** Le `reset_lgw.sh` amont de Semtech cible la conception de référence CoreCell. Ses valeurs par défaut comprennent GPIO23 pour la réinitialisation du concentrateur, GPIO18 pour l'activation de l'alimentation, GPIO22 pour la réinitialisation auxiliaire et GPIO13 pour la réinitialisation d'un AD5338R. [Source du script de réinitialisation Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Les anciennes instructions de configuration Seeed remplacent les deux affectations de réinitialisation par GPIO17 et GPIO5, mais conservent les autres entrées de référence. Comparez ces valeurs à l'image annotée M1 avant de suivre l'exemple. [Instructions de configuration WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc)

| Affectation | Éléments contradictoires | Décision requise |
|---|---|---|
| **GPIO22 comme réinitialisation auxiliaire** | L'image M1 l'identifie comme LED utilisateur | Écarter cette hypothèse avant d'activer la LED |
| **GPIO18 comme activation d'alimentation** | L'image M1 l'identifie comme BUSY auxiliaire | Vérifier le net et son sens avant de le piloter |
| **GPIO13 comme réinitialisation du DAC** | Le script générique nomme une autre conception de référence | Vérifier si le circuit existe |
| **Périphérique SPI auxiliaire** | L'image M1 sélectionne GPIO6 plutôt que CE1 | Confirmer le routage de sélection et la prise en charge du pilote |

**Déduction :** si GPIO18 est relié à une sortie de radio auxiliaire comme le montre le dessin, configurer la broche côté Pi en sortie crée un risque de contention électrique. Cette divergence impose une vérification. Elle ne prouve ni un dommage ni un brochage universel pour tous les M1.

Toutes alimentations débranchées, suivez les connexions accessibles entre le connecteur et le module. Notez la révision de la carte et les deux extrémités. Un test de continuité établit la connexion, tandis que la documentation du composant établit le sens du signal et ses limites électriques.

Utilisez le schéma du module ci-dessous pour ne pas confondre les broches de bord et celles du connecteur Pi. Les noms des signaux radio auxiliaires décrivent la référence publiée du module. Ils ne prouvent pas que toutes les révisions utilisent le même silicium ou les mêmes fonctions. [Brochage du module WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Schéma Seeed indiquant les deux faces du connecteur de bord WM1302, avec alimentation, SPI, I2C et signaux radio auxiliaires" caption="La numérotation du connecteur de bord du module diffère de celle du connecteur Raspberry Pi" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Préparez Raspberry Pi OS

Relevez l'environnement de l'hôte sur votre installation de rechange :

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

La version du système, le noyau et le modèle de Pi constituent le point de départ reproductible. Notez-les avant de comparer vos résultats à un ancien tutoriel.

Installez les outils d'inspection et de compilation :

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

Dans **Interface Options**, activez SPI et I2C, puis redémarrez. SPI sert à la chaîne du concentrateur et I2C aux périphériques de gestion abordés plus loin. N'importez pas les changements sans rapport avec le port série GPS d'un tutoriel consacré à un autre HAT.

Inspectez les interfaces exposées :

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

Ces commandes listent les fichiers de périphérique, les adaptateurs, les contrôleurs GPIO, leurs lignes et la version de l'outil GPIO installé. **`i2cdetect -l` liste les adaptateurs sans sonder les adresses.** Le fichier `/dev/spidev0.0` prouve qu'une interface SPI est exposée, pas qu'elle communique avec un concentrateur fonctionnel. [Manuel i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Recommandations GPIO de Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### Tenez compte des versions GPIO

**Ne copiez pas les numéros GPIO globaux d'une autre machine.** Les anciens scripts écrivent dans `/sys/class/gpio`, une interface que le noyau déclare obsolète. Les nouvelles intégrations en espace utilisateur doivent utiliser l'interface GPIO character device avec le contrôleur et le décalage de ligne corrects. [Documentation Linux GPIO](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

Consultez aussi `gpioset --help` avant d'adapter un script. Les versions 1 et 2 diffèrent par leur syntaxe et le comportement de leurs processus. L'outil actuel conserve par défaut les lignes demandées, mais son contrat portable ne garantit pas leur état après la fin du processus. [Documentation gpioset de libgpiod](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi décrit un comportement de persistance des sorties dans son noyau, avec des options pour le modifier. Relevez la configuration du noyau utilisé plutôt que de supposer que tous les systèmes Linux se comportent de la même façon. Une nouvelle numérotation ou un outil GPIO plus récent ne corrige pas une mauvaise correspondance électrique. [Guide d'utilisation GPIO de Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## Testez la LED utilisateur

Après avoir vérifié que GPIO22 est relié à la LED et supprimé les utilisations GPIO concurrentes, modifiez la configuration de démarrage :

```bash
sudoedit /boot/firmware/config.txt
```

Les versions récentes de Raspberry Pi OS montent la configuration de démarrage sous **`/boot/firmware/config.txt`**. Les anciennes images utilisent `/boot/config.txt`, le chemin de l'article de 2023. Sauvegardez le fichier actif avant de le modifier. [Documentation config.txt de Raspberry Pi](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Ajoutez l'overlay LED dans une section applicable à votre Pi, par exemple `[all]` :

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

Le paramètre **`gpio`** utilise la numérotation BCM. **`label`** nomme le périphérique LED Linux et **`trigger=heartbeat`** sélectionne le déclencheur heartbeat du noyau. Clockwork Bird indique cette affectation pour le M1, et la référence des overlays Raspberry Pi documente ces paramètres. [Observation LED d'origine](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [Référence de l'overlay gpio-led](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Après le redémarrage, inspectez la LED enregistrée :

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

Le résultat attendu est une entrée LED `lorawan` avec `heartbeat` sélectionné entre crochets. Le clignotement valide la chaîne GPIO/pilote. Il ne prouve ni l'enregistrement LoRaWAN, ni la réception radio, ni l'état Helium.

## Examinez les périphériques I2C

**Une adresse I2C est un indice, pas une identité de périphérique.** Clockwork Bird a observé des réponses en `0x60` et `0x39`, puis lu les informations ATECC608 avec la bibliothèque cryptographique. L'identification du capteur de température restait hypothétique dans l'article d'origine.

Commencez par la liste des adaptateurs de la section précédente. Les balayages larges `i2cdetect` envoient des transactions de sondage, ils ne se contentent pas d'observer passivement le bus, et le manuel amont avertit qu'ils peuvent perturber des périphériques. Évitez les balayages réguliers d'une passerelle en fonctionnement ou de périphériques inconnus. [Comportement de sondage i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Observation | Conclusion étayée | Question non résolue |
|---|---|---|
| **Réponse en `0x60`** | Un périphérique a acquitté la requête | Est-ce l'élément sécurisé attendu ? |
| **Réponse en `0x39`** | Un périphérique a acquitté la requête | Quel composant et quelle révision ont répondu ? |
| **`UU` dans un balayage** | Un pilote possède l'adresse, le sondage a été ignoré | Quel pilote en est propriétaire ? |
| **Aucune réponse** | Le sondage n'a reçu aucun acquittement | Alimentation, bus, propriétaire ou protocole ? |

### Affinez la piste du capteur de température

**STTS751 est un candidat pour `0x39` appuyé par la documentation.** L'en-tête du pilote de température Semtech associe explicitement `0x39` au `STTS751-0DP3F`. Cela renforce l'hypothèse d'origine sans identifier tous les circuits installés sur cette adresse. [En-tête du pilote STTS751 Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

Après avoir identifié un composant compatible et vérifié qu'aucun autre processus ne le possède, lisez ses registres d'identification :

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

Ici, **`1`** sélectionne le bus vérifié, **`0x39`** le périphérique et **`b`** une lecture SMBus de données octet. Pour le STTS751-0, l'identifiant produit documenté à `0xFD` est `0x00` et l'identifiant fabricant à `0xFE` est `0x53`. Ces transactions sélectionnent des adresses de registre, elles n'écrivent aucune configuration. [Fiche technique STTS751, plan des registres et registres d'identification](https://www.st.com/resource/en/datasheet/stts751.pdf)

Comparez les lectures au marquage de la puce et à sa documentation. Une paire correspondante renforce l'identification. En cas d'erreur, vérifiez le bus et son propriétaire avant de modifier la configuration matérielle. Le capteur mesure sa température locale, différente de celle du processeur Pi.

## Inspectez l'élément sécurisé

**L'ATECC608 est un composant d'authentification distinct.** Distinguez sa configuration, son numéro de série, sa clé publique et les clés protégées. Lire une clé publique ne révèle pas la clé privée correspondante.

La **CryptoAuthLib** de Microchip fournit l'interface du périphérique. Le dépôt **cryptoauthtools** contient des exemples fondés sur cette bibliothèque. Préparez la bibliothèque native et les bindings Python pour votre système en suivant les instructions de ces projets avant de lancer un exemple. Installer un paquet Python sans rapport ou copier un script isolé ne prouve pas que le backend I2C fonctionne. [CryptoAuthLib de Microchip](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools de Microchip](https://github.com/MicrochipTech/cryptoauthtools)

Depuis un répertoire `cryptoauthtools/python/examples` préparé, lancez la commande d'inspection de l'article d'origine :

```bash
sudo python3 info.py -i i2c
```

L'argument **`-i i2c`** sélectionne l'interface. Avec un environnement virtuel, utilisez son interpréteur Python explicite et vérifiez qu'il trouve la bibliothèque native correspondante. Dans beaucoup d'installations, `sudo python3` sélectionne l'interpréteur système, ce qui explique certains échecs d'importation de modules.

Le fichier `info.py` examiné lit les informations de révision, le numéro de série, la configuration et l'état des verrous. Si la zone de données est verrouillée, il tente de lire la clé publique du slot 0. Il n'exécute pas la séquence de provisionnement de l'exemple. L'échec isolé de lecture de la clé publique du slot 0 ne prouve pas que le périphérique est en panne. [Source de info.py Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Sortie ou opération | Signification |
|---|---|
| **Configuration verrouillée** | Les restrictions de configuration s'appliquent |
| **Zone de données verrouillée** | Interpréter les accès selon les politiques configurées des slots |
| **Clé publique affichée** | Des informations publiques ont été lues, pas une clé privée exportée |
| **Exécution de `config.py`** | Exemple de provisionnement avec écriture, verrouillage et génération de clés |

**N'exécutez pas `config.py` pour corriger une erreur d'inspection.** Son code comprend des écritures de configuration, le verrouillage de zones et la génération de clés. Le chemin de génération de clé par défaut compte également sur un périphérique déjà configuré. [Source de config.py Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Les profils de provisionnement documentés par Microchip montrent pourquoi une zone de données verrouillée ne signifie pas que tous les slots ont les mêmes droits d'accès. Ces profils n'établissent pas la configuration exacte du M1. Conservez la configuration existante et consultez la documentation du composant correspondant avant de prévoir une réutilisation impliquant des clés. [Politiques Microchip de mémoire et d'accès aux slots](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## Examinez les inconnues du ventilateur et du bouton

**Une prise de ventilateur à trois broches ne précise ni sa tension, ni sa polarité, ni son mode de commande.** Photographiez la numérotation et lisez l'étiquette du ventilateur. Déterminez les connexions d'alimentation et de commande avant de brancher un remplacement ou de choisir un overlay GPIO.

De même, l'enquête d'origine ne détermine pas le GPIO du bouton. Recherchez un pilote ou une configuration adaptée à la révision de votre carte, puis vérifiez la continuité hors tension. Ne configurez pas toutes les broches apparemment libres en sortie pour trouver le bouton.

| Périphérique | Éléments à recueillir | Critère d'acceptation |
|---|---|---|
| **Alimentation du ventilateur** | Caractéristiques du ventilateur, masse et alimentation du connecteur | L'alimentation mesurée correspond aux spécifications du ventilateur |
| **Commande du ventilateur** | Pilote/configuration ou circuit de commande tracé | Comportement défini au démarrage et à température élevée |
| **Bouton utilisateur** | Câblage des contacts, mapping GPIO, polarité d'entrée | Une pression volontaire produit l'événement attendu |

Une nouvelle installation ne reproduit pas automatiquement la politique de refroidissement de l'appareil d'origine. Lors du premier test prolongé, observez ensemble le ventilateur et les températures. Préservez le flux d'air du boîtier et arrêtez le test si le montage perd le refroidissement nécessaire.

## Choisissez une pile de passerelle

**Distinguez la prise en charge de la carte du protocole serveur.** Un serveur LoRaWAN compatible ne corrige ni une séquence de réinitialisation inadaptée ni le calibrage RF. Choisissez d'abord un logiciel compatible avec le concentrateur, le câblage du support, le système et la configuration régionale.

| Piste logicielle | Rôle utile | Vérification avant déploiement |
|---|---|---|
| **Semtech SX1302 HAL** | Mise en service au niveau source et outils de diagnostic | Script de réinitialisation de carte et configuration du module |
| **LoRa Basics Station** | Connexion authentifiée d'une passerelle au serveur | Intégration fonctionnelle de la carte et identifiants du serveur |
| **ChirpStack Concentratord** | Service dédié au concentrateur | Modèle pris en charge, calibrage et mapping GPIO |

ChirpStack répertorie un modèle SPI **`seeed_wm1302`**. Cela prouve la prise en charge du module, pas celle d'une image M1 complète ni de toutes les révisions M1. N'utilisez pas les instructions d'installation séparées du SenseCAP M2 comme instructions de firmware pour le M1. [Prise en charge matérielle de ChirpStack](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [cible d'installation Seeed de ChirpStack](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Pour The Things Stack, la documentation recommande **LoRa Basics Station** plutôt que l'ancien transmetteur UDP Semtech. Station fournit TLS et l'authentification par jeton, ainsi que des fonctions de configuration centralisée. Les exemples UDP existants aident à comprendre la transmission de paquets, mais leurs paramètres d'adresse serveur n'apportent pas ces protections. [Conseils UDP de The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [Documentation LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Préparez les outils amont

Compilez sur le Pi cible dans un nouveau répertoire de travail :

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Enregistrez l'identifiant du commit avec la sortie de compilation. Une compilation réussie valide la compatibilité du compilateur, mais la radio exige encore une procédure de réinitialisation vérifiée et une configuration correcte. La documentation Semtech explique le rôle du HAL et des programmes auxiliaires. [Documentation de compilation et des outils SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Examinez le fichier de réinitialisation avant de lancer des outils d'accès matériel :

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

Ne copiez pas ce fichier tel quel dans le répertoire d'exécution. Semtech documente l'utilisation automatique du script par ses programmes d'accès matériel, notamment des outils d'identification. Votre examen doit couvrir chaque broche affectée, le sens du signal, l'API GPIO et l'état au démarrage et à l'arrêt.

Après vérification de la carte, suivez les instructions de la pile choisie pour lire l'EUI du concentrateur et enregistrer la passerelle. Préservez le calibrage du module et les réglages RF lors de l'ajout de la configuration serveur. Dans la configuration UDP Semtech, `gateway_ID` représente l'EUI. Le Gateway ID dans la console The Things Stack est l'identifiant lisible attribué à l'enregistrement. [Configuration de passerelle The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## Prouvez la transmission des capteurs

**Utilisez des preuves par étapes pour trouver la première couche défaillante.** Une passerelle indiquée en ligne prouve une connexion au serveur. Votre test d'acceptation doit aussi utiliser un capteur connu, un plan de fréquences correspondant et une charge utile applicative décodée.

La séquence suivante est un plan de test proposé, pas un résultat mesuré sur M1 :

| Étape de contrôle | Preuve à enregistrer | Signification |
|---|---|---|
| **Hôte prêt** | Système, noyau, alimentation et inventaire des interfaces | Préparation Linux terminée |
| **Réponse du concentrateur** | EUI et journal d'initialisation réussi | La communication hôte-concentrateur fonctionne |
| **Réception radio** | Paquet du capteur attendu et métadonnées de réception | La chaîne de réception configurée fonctionne |
| **Acceptation serveur** | Événement de passerelle associé au capteur | Le transfert et le routage serveur fonctionnent |
| **Décodage applicatif** | Mesure attendue et horodatage | La chaîne applicative fonctionne |
| **Récupération après redémarrage** | Mêmes contrôles après redémarrage | La configuration de démarrage est reproductible |

Pour un capteur **OTAA**, vérifiez aussi l'échange d'activation et la liaison montante qui suit. OTAA signifie « activation par liaison radio », la procédure de jonction qui établit une session. Recevoir une demande de jonction ne prouve ni une jonction réussie ni une voie descendante fonctionnelle. [Documentation d'activation The Things Stack](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Diagnostic pratique :** la passerelle se connecte au serveur et signale son EUI, mais le capteur n'apparaît pas. Examinez en priorité la configuration d'émission du capteur, les canaux de réception sélectionnés, le chemin d'antenne et les journaux radio. Reprogrammer l'ATECC608 ne résoudrait pas le manque de preuves dans ce scénario.

**Autre diagnostic :** un paquet du capteur apparaît localement, mais n'atteint pas l'application. Corrélez son heure avec les événements de la passerelle et du serveur, puis vérifiez le routage, l'enregistrement du périphérique et le décodage. Un paquet RF dans un journal ne suffit pas à accuser le décodeur avant l'acceptation de l'événement par le serveur.

## Dépannez selon le symptôme

| Symptôme | Première vérification | Action suivante |
|---|---|---|
| **Aucun fichier de périphérique SPI** | Configuration de démarrage active et options d'interface | Activer l'interface voulue et redémarrer |
| **SPI présent, radio en échec** | Alimentation, insertion, séquence de réinitialisation et sélection de puce | Vérifier le chemin électrique avant les changements serveur |
| **Erreur d'export GPIO** | Anciennes hypothèses sysfs et noyau installé | Utiliser une implémentation vérifiée pour l'API GPIO |
| **GPIO déjà utilisé** | Utilisateur indiqué par `gpioinfo` | Résoudre le conflit avant de réessayer |
| **LED inactive après configuration** | Application de l'overlay et conflits GPIO22 | Examiner les LED enregistrées et le script de réinitialisation |
| **Périphérique I2C absent** | Numéro de bus, alimentation et propriétaire actuel | Enquêter sans répéter de balayage large |
| **Échec d'importation de bibliothèque crypto** | Interpréteur, bindings et chemin de la bibliothèque native | Corriger l'environnement logiciel |
| **Lecture de clé publique en échec** | Politique du slot et lectures précédentes réussies | Examiner la configuration sans provisionner |
| **Ventilateur inactif** | Alimentation vérifiée et commande de refroidissement | Rétablir le refroidissement avant un test prolongé |
| **Liaisons montantes reçues, jonction en échec** | Voie descendante et paramètres régionaux/de périphérique | Suivre la réponse de jonction et les fenêtres de réception |

Traitez chaque correction comme une seule expérience. Enregistrez la configuration précédente, modifiez une variable, répétez le même contrôle et notez si la preuve attendue apparaît.

## Créez votre relevé matériel

Utilisez ce modèle pour transformer l'enquête en compte rendu reproductible :

```text
Révision du support et photos :
Modèle du concentrateur, interface et bande RF :
Modèle hôte / système / noyau / version de l'outil GPIO :
Alimentation / antenne / configuration de refroidissement :
Mapping des broches vérifié et preuves :
Connexions non résolues et fonctions exclues :
Dépôt logiciel et commit :
Procédure de réinitialisation et propriétaire GPIO :
EUI de la passerelle / serveur / plan de fréquences :
Activation du capteur et preuve de liaison montante décodée :
Résultat de récupération après redémarrage :
Emplacement de la carte d'origine et procédure de retour arrière :
```

**Exercice de décision :** vous avez un support nu bon marché sans étiquette de module et un ensemble plus coûteux avec des étiquettes lisibles et un fonctionnement documenté. Déterminez lequel convient au projet en ajoutant au comparatif le Pi, le concentrateur, l'antenne, l'alimentation et le temps de vérification nécessaires. Le meilleur choix dépend du coût total et des preuves requises pour le service prévu, pas du prix affiché du support seul.

**Raisonnement attendu :** un projet d'apprentissage tolère des connexions non résolues si vous avez les outils de mesure et le temps nécessaires. Une passerelle qui dessert des capteurs en exploitation exige un démarrage reproductible, un refroidissement correct, une prise en charge logicielle et une transmission démontrée. Notez quelle incertitude arrêterait le déploiement.

## Étapes suivantes

Commencez par compléter le relevé matériel et résoudre les divergences du script de réinitialisation. Mettez ensuite en service un capteur connu et enregistrez les preuves jusqu'au décodage par l'application avant d'en ajouter d'autres.

**Relevé d'acceptation :** enregistrez la révision de la carte, l'étiquette du module, la bande radio, la mesure d'alimentation, le périphérique SPI actif, les noms des lignes GPIO, la séquence de réinitialisation, le journal du concentrateur, la connexion serveur et une liaison montante décodée. Marquez chaque valeur comme observée, documentée ou encore supposée. Ne considérez pas le démarrage d'un processus comme une preuve de performance RF ou de transmission à l'application.

Si votre objectif est la messagerie maillée, comparez d'abord les rôles des protocoles dans notre [guide Meshtastic, MeshCore et Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Utiliser la même technologie radio LoRa ne prouve pas la compatibilité du firmware. Pour une messagerie, consultez la [documentation du matériel pris en charge par MeshtasticD](https://meshtastic.org/docs/meshtasticd/) au lieu de convertir cette procédure LoRaWAN en procédure Meshtastic.

## Sources et crédits des images

Recherche vérifiée le 12 septembre 2026. Les liens vers des documents et dépôts sans date renvoient aux versions examinées pour cet article. Les figures locales conservent leurs légendes et leur provenance d'origine.

| Éditeur | Source et date |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03. Photo de la carte, connecteur annoté et schéma fonctionnel du fabricant reproduit |
| **Seeed Studio / SenseCAP** | [Présentation et spécifications M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/), sans date. Attribution du schéma fonctionnel d'origine |
| **Seeed Studio** | [Documentation WM1302 et brochage du module](https://github.com/seeed-lora/WM1302-doc), dépôt |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), avec les sources liées du script de réinitialisation et du pilote de température |
| **Raspberry Pi** | [Configuration de démarrage](https://www.raspberrypi.com/documentation/computers/config_txt.html), [guide d'utilisation GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) et [référence des overlays](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Interface GPIO sysfs obsolète](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) et [manuel gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html), ce dernier daté d'août 2026 |
| **i2c-tools** | [Manuel i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), source v4.3 |
| **STMicroelectronics** | [Fiche technique STTS751](https://www.st.com/resource/en/datasheet/stts751.pdf), révision 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) et [documentation des politiques d'accès aux slots](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Prise en charge matérielle Concentratord](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) et [cible d'installation Seeed](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [Transmetteur UDP](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) et [activation des périphériques](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [Documentation MeshtasticD](https://meshtastic.org/docs/meshtasticd/), sans date |
