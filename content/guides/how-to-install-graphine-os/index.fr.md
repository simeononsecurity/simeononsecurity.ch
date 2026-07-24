---
title: "Guide Ultime : Installer GrapheneOS sur votre Google Pixel"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Apprenez à installer GrapheneOS sur votre Google Pixel pour une confidentialité et une sécurité renforcées, via l'installateur web ou la méthode CLI."
tags: ["GrapheneOS", "Google Pixel", "confidentialité", "sécurité", "Android", "appareils mobiles", "système d'exploitation", "guide d'installation", "ROM personnalisée", "axé sur la confidentialité", "protection des données", "OS sécurisé", "open source", "sécurité de l'appareil", "fonctionnalités de confidentialité", "données personnelles", "confidentialité mobile", "vie privée numérique", "personnalisation d'appareil", "technologie", "fastboot", "bootloader", "verified boot", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "Une illustration numérique abstraite montrant un smartphone Google Pixel connecté à un ordinateur via un câble USB-C, entouré d'éléments graphiques représentant le transfert de données et la sécurité."
coverCaption: ""
---

**Comment installer GrapheneOS sur votre Google Pixel**

GrapheneOS est un système d'exploitation open source axé sur la confidentialité, basé sur Android. Il offre un renforcement significatif de la sécurité et des protections de la vie privée, ce qui en fait un excellent choix pour toute personne soucieuse de la confidentialité et de la sécurité des données. Si vous possédez un Google Pixel compatible et souhaitez passer à GrapheneOS, ce guide couvre à la fois la méthode **installateur web** recommandée et la méthode traditionnelle **ligne de commande (CLI)**.

> **Conseil :** Si vous rencontrez des difficultés lors de l'installation, demandez de l'aide sur le [canal de discussion officiel de GrapheneOS](https://grapheneos.org/contact#community). Avant de demander de l'aide, essayez d'abord de suivre le guide par vous-même, puis posez des questions sur ce qui vous bloque.

## Prérequis

### Configuration matérielle et système

- Un ordinateur avec au moins **2 Go de mémoire libre** et **32 Go d'espace de stockage libre**.
- Un **câble USB-C de haute qualité** fourni avec l'appareil (ou un câble USB-C vers USB-A si nécessaire). Évitez les hubs USB – connectez directement à un port arrière de bureau ou à un port de laptop.
- L'installation depuis une machine virtuelle est **déconseillée** en raison de la transmission USB peu fiable.

> Il est recommandé de mettre à jour votre Pixel avant d'installer GrapheneOS pour disposer du dernier firmware. De toute façon, GrapheneOS flashe le dernier firmware au début du processus d'installation.

### Systèmes d'exploitation officiellement supportés

#### Installateur web

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (suivre les instructions d'Ubuntu 22.04 LTS), Linux Mint 22 (suivre les instructions d'Ubuntu 24.04 LTS)
- Linux Mint Debian Edition 6 (suivre les instructions de Debian 12)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15 et 16 avec certification Play Protect

#### Méthode CLI

Tous les systèmes ci-dessus sauf ChromeOS, GrapheneOS et Android (qui ne peuvent utiliser que l'installateur web).

Les versions plus anciennes et en fin de vie de ces plateformes peuvent aussi être utilisées, mais ne sont pas officiellement supportées. **Assurez-vous que votre système d'exploitation est à jour avant de continuer.**

### Navigateurs officiellement supportés (installateur web uniquement)

- **Chromium** (hors Ubuntu – leur paquet Snap n'a pas WebUSB fonctionnel)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (avec Brave Shields désactivé – il limite l'utilisation du stockage pour éviter le fingerprinting)

> - Sur Android, **désactivez le mode bureau** dans votre navigateur. Le mode bureau empêche l'installateur web de détecter Android et de demander la permission de reconnexion après les redémarrages. Il est activé par défaut sur les grandes tablettes avec 8 Go+ de RAM (ex. Pixel Tablet).
> - Évitez les versions Flatpak et Snap des navigateurs – ils causent des problèmes lors de l'installation.
> - N'utilisez **pas** le mode incognito/navigation privée – ces modes restreignent l'espace de stockage nécessaire pour extraire la version téléchargée.

### Appareils supportés

Vous avez besoin d'un des [appareils Pixel officiellement supportés](https://grapheneos.org/faq#supported-devices). **Évitez les variantes opérateur** – les Pixel opérateur ont un carrier ID non nul flashé en usine qui désactive le déverrouillage du bootloader. Procurez-vous un appareil indépendant des opérateurs (déverrouillé).

---

## Activer le déverrouillage OEM

Le déverrouillage OEM doit être activé depuis le système d'exploitation avant de pouvoir continuer.

1. Allez dans **Paramètres → À propos du téléphone/tablette** et appuyez plusieurs fois sur **Numéro de build** jusqu'à ce que le mode développeur soit activé.
2. Allez dans **Paramètres → Système → Options pour les développeurs** et activez **Déverrouillage OEM**. Sur certaines variantes compatibles opérateur, cela nécessite une connexion internet active pour que l'OS stock puisse vérifier que l'appareil n'a pas été vendu verrouillé par un opérateur.

> **Note Pixel 6a :** Le déverrouillage OEM ne fonctionnera pas avec la version OS stock d'usine. Mettez à jour via OTA vers la version de **juin 2022** ou ultérieure, puis effectuez une réinitialisation d'usine pour corriger le déverrouillage OEM.

---

## Méthode d'installation 1 : Installateur web (Recommandé)

L'[installateur web GrapheneOS](https://grapheneos.org/install/web) est l'approche recommandée pour la plupart des utilisateurs. Il utilise WebUSB directement dans votre navigateur – aucune installation de logiciel requise.

### Étape 1 : Contourner les bugs fwupd (Linux uniquement)

Sur Linux, `fwupd` se connecte incorrectement aux appareils via le protocole fastboot, bloquant l'installateur. Arrêtez-le avant de connecter votre appareil :

```bash
sudo systemctl stop fwupd.service
```

Cela ne persistera pas après un redémarrage.

### Étape 2 : Configurer les règles udev (Linux uniquement)

Sur Arch Linux :

```bash
sudo pacman -S android-udev
```

Sur Debian et Ubuntu :

```bash
sudo apt install android-sdk-platform-tools-common
```

### Étape 3 : Démarrer dans l'interface bootloader

Maintenez le bouton **volume bas** enfoncé pendant le démarrage de l'appareil (soit l'allumer depuis l'éteint en maintenant volume bas, soit redémarrer et maintenir volume bas). L'appareil doit afficher un **triangle d'avertissement rouge** et les mots **"Fastboot Mode"** – n'appuyez pas sur le bouton d'alimentation pour activer "Démarrer".

### Étape 4 : Connecter votre appareil

Connectez l'appareil à votre ordinateur via USB. Sur Linux, reconnectez le câble si les règles udev n'étaient pas configurées avant la première connexion.

> **Pixel Tablet :** Déconnectez-le du socle avant de le connecter via USB – la tablette ne peut pas utiliser les deux simultanément.

> **Windows :** Windows 10/11 actuel inclut un pilote fastboot générique pour Pixel 4a (5G) et ultérieur. Pour les anciens Pixel ou Windows obsolète, installez le pilote depuis Windows Update (cherchez sous "Afficher les mises à jour optionnelles" → "LeMobile Android Device").

### Étape 5 : Déverrouiller le bootloader

Allez sur [https://grapheneos.org/install/web](https://grapheneos.org/install/web) et cliquez sur le bouton **Déverrouiller le bootloader**. Confirmez sur l'appareil en utilisant les boutons de volume pour changer la sélection et le bouton d'alimentation pour confirmer. **Cela efface toutes les données.**

### Étape 6 : Télécharger et flasher les images d'usine

1. Cliquez sur **Télécharger la version** pour télécharger les images d'usine pour votre appareil.
2. Cliquez sur **Flasher les images d'usine** et attendez que le processus se termine. Il flashera automatiquement le firmware, redémarrera dans l'interface bootloader, et flashera l'OS. **N'interagissez pas avec l'appareil jusqu'à la fin.**

### Étape 7 : Verrouiller le bootloader

Après le flash, cliquez sur **Verrouiller le bootloader** dans l'installateur web. Confirmez sur l'appareil. **Cela efface à nouveau toutes les données** – verrouiller le bootloader active le verified boot complet.

---

## Méthode d'installation 2 : Ligne de commande (CLI)

### Étape 1 : Ouvrir un terminal

Sur Windows, ouvrez une fenêtre **PowerShell normale (non-administrateur)**. Supprimez l'ancien alias `curl` :

```powershell
Remove-Item Alias:Curl
```

### Étape 2 : Installer fastboot

Vous avez besoin de fastboot version **≥ 35.0.1**.

**Arch Linux :**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** – leurs paquets sont obsolètes. Utilisez la version autonome :

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS :**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows :**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

Vérifiez votre version :

```bash
fastboot --version
# Attendu : fastboot version 35.0.2-12147458
```

### Étape 3 : Configurer les règles udev (Linux uniquement)

Arch Linux :

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu :

```bash
sudo apt install android-sdk-platform-tools-common
```

### Étape 4 : Contourner les bugs fwupd (Linux uniquement)

```bash
sudo systemctl stop fwupd.service
```

### Étape 5 : Démarrer dans l'interface bootloader

Maintenez **volume bas** pendant le démarrage jusqu'à ce que l'appareil affiche **"Fastboot Mode"** avec le triangle d'avertissement rouge.

### Étape 6 : Connecter et déverrouiller le bootloader

Connectez via USB, puis exécutez :

```bash
fastboot flashing unlock
```

Confirmez sur l'appareil (boutons de volume pour changer la sélection, bouton d'alimentation pour confirmer). **Cela efface toutes les données.**

### Étape 7 : Installer OpenSSH (pour la vérification des images)

macOS et Windows incluent OpenSSH par défaut.

Arch Linux :

```bash
sudo pacman -S openssh
```

Debian / Ubuntu :

```bash
sudo apt install openssh-client
```

### Étape 8 : Télécharger et vérifier les images d'usine

Téléchargez la clé de signature :

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Contenu attendu :

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Téléchargez les images d'usine (remplacez `DEVICE_NAME` et `VERSION` par les valeurs réelles) :

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Vérifiez la signature (Linux / macOS) :

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows :

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Sortie attendue :

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Étape 9 : Flasher les images d'usine

Extraire les images :

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

Entrez dans le répertoire et exécutez le script flash :

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Attendez que le processus se termine. Il gère automatiquement le flash du firmware, les redémarrages du bootloader, et le flash de l'OS. **N'interagissez pas avec l'appareil jusqu'à la fin.**

> **Dépannage tmpfs Linux :** Si `/tmp` n'a pas assez d'espace, utilisez :
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Étape 10 : Verrouiller le bootloader

```bash
fastboot flashing lock
```

Confirmez sur l'appareil. **Cela efface à nouveau toutes les données.** Le verrouillage active le verified boot complet et empêche fastboot de modifier les partitions.

---

## Après l'installation

### Démarrage

Appuyez sur le bouton d'alimentation avec l'option **Démarrer** sélectionnée par défaut dans l'interface bootloader pour démarrer GrapheneOS.

### Désactiver le déverrouillage OEM

Lors de la première configuration, le dernier écran contient un interrupteur pour le déverrouillage OEM (coché par défaut – le laisser coché **désactive** le déverrouillage OEM). C'est recommandé. Vous pouvez le modifier plus tard dans les **Options pour les développeurs**.

### Vérifier l'installation

GrapheneOS exploite le verified boot et l'attestation matérielle. Le verified boot vérifie tous les firmwares et images OS à chaque démarrage par rapport aux clés gravées dans les fusibles SoC. GrapheneOS flashe sa propre clé publique de verified boot dans l'élément sécurisé – à chaque démarrage, cette clé vérifie l'OS.

#### Hachages de clés Verified Boot

Quand un OS alternatif est chargé, l'appareil affiche un **avis jaune** avec l'identifiant de l'OS (sha256 de la clé de verified boot). Les Pixel de 4e et 5e génération n'affichent que les 32 premiers bits ; **les Pixel de 6e génération et ultérieurs affichent le hachage complet**. Comparez avec les hachages officiels :

| Appareil | Hash de clé Verified Boot |
|---------|--------------------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### Attestation matérielle avec Auditor

GrapheneOS fournit l'[application Auditor](https://attestation.app/) pour vérifier l'intégrité du matériel, du firmware et de l'OS en utilisant le verified boot et l'attestation à distance. Les résultats sont affichés sur un second appareil Android exécutant Auditor (pas sur l'appareil en cours de vérification), ou via le [service de surveillance d'intégrité des appareils](https://attestation.app/) optionnel pour des vérifications automatiques programmées avec alertes par e-mail.

---

## Remplacer GrapheneOS par l'OS stock

L'installation de l'OS stock via l'[outil de flash web de Google](https://flash.android.com/) est similaire au processus ci-dessus. Cependant, avant de flasher et de verrouiller, vous devez effacer la clé de verified boot de GrapheneOS pour revenir complètement au stock :

**Installateur web :** Utilisez le bouton "Effacer la clé non-stock" sur l'installateur web GrapheneOS.

**CLI :**

```bash
fastboot erase avb_custom_key
```

Puis flashez les images d'usine stock et verrouillez le bootloader.

---

## Conclusion

Installer GrapheneOS sur votre Google Pixel offre des fonctionnalités de confidentialité et de sécurité de pointe. Utilisez l'**installateur web** sur [grapheneos.org/install/web](https://grapheneos.org/install/web) pour l'expérience la plus simple, ou suivez les étapes CLI ci-dessus pour une approche traditionnelle. Verrouillez toujours le bootloader après le flash pour activer le verified boot complet, et utilisez optionnellement l'application Auditor pour confirmer l'intégrité de votre installation.

## Références

1. [Site web GrapheneOS](https://grapheneos.org/)
2. [Installateur web GrapheneOS](https://grapheneos.org/install/web)
3. [Guide d'installation CLI GrapheneOS](https://grapheneos.org/install/cli)
4. [Versions GrapheneOS](https://grapheneos.org/releases)
5. [Guide d'utilisation GrapheneOS](https://grapheneos.org/usage)
6. [FAQ GrapheneOS](https://grapheneos.org/faq)
7. [Application Auditor](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
