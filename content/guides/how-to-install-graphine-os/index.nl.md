---
title: "Ultieme Gids: GrapheneOS Installeren op uw Google Pixel"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Leer hoe u GrapheneOS installeert op uw Google Pixel voor verbeterde privacy en beveiliging via de webinstaller of de CLI-methode."
tags: ["GrapheneOS", "Google Pixel", "privacy", "beveiliging", "Android", "mobiele apparaten", "besturingssysteem", "installatiegids", "custom ROM", "privacygericht", "gegevensbescherming", "veilig OS", "open source", "apparaatbeveiliging", "privacyfuncties", "persoonlijke gegevens", "mobiele privacy", "digitale privacy", "apparaataanpassing", "technologie", "fastboot", "bootloader", "verified boot", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "Een abstracte digitale illustratie van een Google Pixel-smartphone verbonden met een computer via een USB-C-kabel, omgeven door kleurrijke grafische elementen die gegevensoverdracht en beveiliging voorstellen."
coverCaption: ""
---

**Hoe GrapheneOS installeren op uw Google Pixel**

GrapheneOS is een open source, privacygericht besturingssysteem gebaseerd op Android. Het biedt aanzienlijk verbeterde beveiligingsharding en privacybescherming, waardoor het een uitstekende keuze is voor iedereen die bezorgd is over gegevensprivacy en beveiliging. Als u een ondersteund Google Pixel-apparaat bezit en wilt overstappen naar GrapheneOS, behandelt deze gids zowel de aanbevolen **webinstaller**-methode als de traditionele **commandoregel-methode (CLI)**.

> **Tip:** Als u problemen heeft met het installatieproces, vraag dan om hulp op het [officiële GrapheneOS-chatkanaal](https://grapheneos.org/contact#community). Probeer de gids eerst zelf te volgen en vraag dan specifiek waar u vastloopt.

## Vereisten

### Hardware- en systeemvereisten

- Een computer met minimaal **2 GB vrij geheugen** en **32 GB vrije opslagruimte**.
- Een **hoogwaardig USB-C-kabel** dat bij het apparaat wordt geleverd (of een USB-C naar USB-A kabel indien nodig). Vermijd USB-hubs – verbind rechtstreeks met een achterste desktoppoort of laptoppoort.
- Installatie vanuit een virtuele machine wordt **niet aanbevolen** vanwege onbetrouwbare USB-doorvoer.

> Het is best practice om uw Pixel-apparaat bij te werken vóór de installatie van GrapheneOS om de nieuwste firmware te hebben. GrapheneOS flasht overigens de nieuwste firmware aan het begin van het installatieproces.

### Officieel ondersteunde besturingssystemen

#### Webinstaller

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (volg Ubuntu 22.04 LTS-instructies), Linux Mint 22 (volg Ubuntu 24.04 LTS-instructies)
- Linux Mint Debian Edition 6 (volg Debian 12-instructies)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15 en 16 met Play Protect-certificering

#### CLI-methode

Alle bovenstaande behalve ChromeOS, GrapheneOS en Android (die alleen de webinstaller kunnen gebruiken).

Oudere, end-of-life versies van deze platforms kunnen ook worden gebruikt maar worden niet officieel ondersteund. **Zorg ervoor dat uw besturingssysteem up-to-date is voordat u doorgaat.**

### Officieel ondersteunde browsers (alleen webinstaller)

- **Chromium** (buiten Ubuntu – hun Snap-pakket mist werkende WebUSB)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (met Brave Shields uitgeschakeld – het beperkt opslaggebruik om fingerprinting te vermijden)

> - Op Android **schakel de bureaubladmodus uit** in uw browser. Bureaubladmodus verhindert dat de webinstaller Android detecteert en na herstarts verbindingstoestemming vraagt. Het is standaard ingeschakeld op grote tablets met 8 GB+ RAM (bijv. Pixel Tablet).
> - Vermijd Flatpak- en Snap-browserversies – deze veroorzaken problemen tijdens de installatie.
> - Gebruik **geen** incognito-/privébrowsemodus – deze modi beperken de opslagruimte die nodig is om de gedownloade release uit te pakken.

### Ondersteunde apparaten

U heeft een van de [officieel ondersteunde Pixel-apparaten](https://grapheneos.org/faq#supported-devices) nodig. **Vermijd carrier-varianten** – carrier-Pixels hebben een niet-nul carrier-ID in de fabriek geflasht die bootloader- en carrier-ontgrendeling uitschakelt. Koop een carrier-onafhankelijk (ontgrendeld) apparaat.

---

## OEM-ontgrendeling inschakelen

OEM-ontgrendeling moet worden ingeschakeld vanuit het besturingssysteem voordat u kunt doorgaan.

1. Ga naar **Instellingen → Over de telefoon/tablet** en tik herhaaldelijk op **Buildnummer** totdat de ontwikkelaarsmodus is ingeschakeld.
2. Ga naar **Instellingen → Systeem → Opties voor ontwikkelaars** en schakel **OEM-ontgrendeling** in. Op sommige carrier-compatibele SKU's vereist dit een actieve internetverbinding zodat het standaard-OS kan verifiëren dat het apparaat niet als carrier-geblokkeerd is verkocht.

> **Pixel 6a-opmerking:** OEM-ontgrendeling werkt niet met de fabrieks-stock-OS-versie. Update via OTA naar de release van **juni 2022** of later, voer dan een fabrieksreset uit om OEM-ontgrendeling te herstellen.

---

## Installatiemethode 1: Webinstaller (Aanbevolen)

De [GrapheneOS Webinstaller](https://grapheneos.org/install/web) is de aanbevolen aanpak voor de meeste gebruikers. Hij gebruikt WebUSB rechtstreeks in uw browser – geen software-installatie vereist.

### Stap 1: fwupd-bugs omzeilen (alleen Linux)

Op Linux verbindt `fwupd` zich onjuist met apparaten via het fastboot-protocol, waardoor de installer wordt geblokkeerd. Stop het voordat u uw apparaat aansluit:

```bash
sudo systemctl stop fwupd.service
```

Dit blijft niet behouden na herstarts.

### Stap 2: udev-regels instellen (alleen Linux)

Op Arch Linux:

```bash
sudo pacman -S android-udev
```

Op Debian en Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Stap 3: Opstarten in de bootloader-interface

Houd de **volumeknop omlaag** ingedrukt terwijl het apparaat opstart (start het op vanuit uitgeschakeld terwijl u volume omlaag ingedrukt houdt, of herstart en houd volume omlaag). Het apparaat moet een **rood waarschuwingsdriehoek** tonen met de woorden **"Fastboot Mode"** – druk niet op de aan/uit-knop om "Start" te activeren.

### Stap 4: Apparaat verbinden

Verbind het apparaat via USB met uw computer. Op Linux, sluit de kabel opnieuw aan als de udev-regels niet vóór de eerste verbinding waren ingesteld.

> **Pixel Tablet:** Ontkoppel van de standaard voordat u via USB verbindt – de tablet kan beide niet tegelijkertijd gebruiken.

> **Windows:** Huidige Windows 10/11 bevat een generiek fastboot-stuurprogramma voor Pixel 4a (5G) en later. Voor oudere Pixels of verouderd Windows, installeer het stuurprogramma via Windows Update (zoek onder "Optionele updates weergeven" → "LeMobile Android Device").

### Stap 5: Bootloader ontgrendelen

Ga naar [https://grapheneos.org/install/web](https://grapheneos.org/install/web) en klik op de knop **Bootloader ontgrendelen**. Bevestig op het apparaat met de volumeknoppen om de selectie te wisselen en de aan/uit-knop om te bevestigen. **Dit wist alle gegevens.**

### Stap 6: Factory Images downloaden en flashen

1. Klik op **Release downloaden** om de factory images voor uw apparaat te downloaden.
2. Klik op **Factory images flashen** en wacht tot het proces is voltooid. Het flasht automatisch firmware, herstart naar de bootloader-interface en flasht het OS. **Interact niet met het apparaat totdat het klaar is.**

### Stap 7: Bootloader vergrendelen

Klik na het flashen op **Bootloader vergrendelen** in de webinstaller. Bevestig op het apparaat. **Dit wist nogmaals alle gegevens** – het vergrendelen van de bootloader schakelt volledig verified boot in.

---

## Installatiemethode 2: Commandoregel (CLI)

### Stap 1: Terminal openen

Open op Windows een **normaal (niet-administrator) PowerShell**-venster. Verwijder de legacy `curl`-alias:

```powershell
Remove-Item Alias:Curl
```

### Stap 2: fastboot installeren

U heeft fastboot versie **≥ 35.0.1** nodig.

**Arch Linux:**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** – hun pakketten zijn verouderd. Gebruik de standalone release:

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS:**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows:**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

Controleer uw versie:

```bash
fastboot --version
# Verwacht: fastboot version 35.0.2-12147458
```

### Stap 3: udev-regels instellen (alleen Linux)

Arch Linux:

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Stap 4: fwupd-bugs omzeilen (alleen Linux)

```bash
sudo systemctl stop fwupd.service
```

### Stap 5: Opstarten in de bootloader-interface

Houd **volume omlaag** tijdens opstarten totdat het apparaat **"Fastboot Mode"** toont met het rode waarschuwingsdriehoek.

### Stap 6: Verbinden en bootloader ontgrendelen

Verbind via USB, voer dan uit:

```bash
fastboot flashing unlock
```

Bevestig op het apparaat (volumeknoppen voor selectie, aan/uit-knop voor bevestiging). **Dit wist alle gegevens.**

### Stap 7: OpenSSH installeren (voor image-verificatie)

macOS en Windows bevatten standaard OpenSSH.

Arch Linux:

```bash
sudo pacman -S openssh
```

Debian / Ubuntu:

```bash
sudo apt install openssh-client
```

### Stap 8: Factory Images downloaden en verifiëren

Download de ondertekeningssleutel:

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Verwachte inhoud:

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Download de factory images (vervang `DEVICE_NAME` en `VERSION` door de werkelijke waarden):

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Verifieer de handtekening (Linux / macOS):

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows:

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Verwachte uitvoer:

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Stap 9: Factory Images flashen

Pak de images uit:

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

Ga naar de map en voer het flashscript uit:

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Wacht tot het proces is voltooid. Het verwerkt firmware-flashen, bootloader-herstarts en OS-flashen automatisch. **Interact niet met het apparaat totdat het klaar is.**

> **Linux tmpfs-probleemoplossing:** Als `/tmp` niet genoeg ruimte heeft, gebruik:
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Stap 10: Bootloader vergrendelen

```bash
fastboot flashing lock
```

Bevestig op het apparaat. **Dit wist nogmaals alle gegevens.** Vergrendelen schakelt volledig verified boot in en voorkomt dat fastboot partities wijzigt.

---

## Na de installatie

### Opstarten

Druk op de aan/uit-knop met de standaard **Start**-optie geselecteerd in de bootloader-interface om GrapheneOS op te starten.

### OEM-ontgrendeling uitschakelen

Tijdens de eerste installatie bevat het laatste scherm een schakelaar voor OEM-ontgrendeling (standaard aangevinkt – aangevinkt laten **schakelt** OEM-ontgrendeling uit). Dit wordt aanbevolen. U kunt het later wijzigen in **Opties voor ontwikkelaars**.

### De installatie verifiëren

GrapheneOS maakt gebruik van verified boot en hardware-attestatie. Verified boot controleert bij elke opstart alle firmware- en OS-images aan de hand van sleutels die in de SoC-zekeringen zijn gebrand. GrapheneOS flasht zijn eigen verified boot public key naar het beveiligingselement – bij elke opstart verifieert deze sleutel het OS.

#### Verified Boot Key Hashes

Wanneer een alternatief OS wordt geladen, toont het apparaat een **gele melding** met de OS-identificatie (sha256 van de verified boot-sleutel). Pixels van de 4e en 5e generatie tonen alleen de eerste 32 bits; **Pixels van de 6e generatie en later tonen de volledige hash**. Vergelijk met de officiële hashes:

| Apparaat | Verified Boot Key Hash |
|---------|----------------------|
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

#### Hardware-gebaseerde attestatie met Auditor

GrapheneOS biedt de [Auditor-app](https://attestation.app/) om hardware-, firmware- en OS-integriteit te verifiëren via verified boot en remote attestatie. Resultaten worden weergegeven op een tweede Android-apparaat met Auditor (niet op het te verifiëren apparaat), of via de optionele [apparaat-integriteitsmonitoringservice](https://attestation.app/) voor automatische geplande verificaties met e-mailwaarschuwingen.

---

## GrapheneOS vervangen door het standaard-OS

De installatie van het standaard-OS via Googles [web-flashtool](https://flash.android.com/) is vergelijkbaar met het bovenstaande proces. Echter, voordat u flasht en vergrendelt, moet u de GrapheneOS verified boot-sleutel wissen om volledig terug te keren naar stock:

**Webinstaller:** Gebruik de knop "Niet-stock sleutel wissen" op de GrapheneOS webinstaller.

**CLI:**

```bash
fastboot erase avb_custom_key
```

Flash dan de stock factory images en vergrendel de bootloader.

---

## Conclusie

Het installeren van GrapheneOS op uw Google Pixel biedt toonaangevende privacy- en beveiligingsfuncties. Gebruik de **webinstaller** op [grapheneos.org/install/web](https://grapheneos.org/install/web) voor de eenvoudigste ervaring, of volg de CLI-stappen hierboven voor een traditionele aanpak. Vergrendel altijd de bootloader na het flashen om volledig verified boot in te schakelen, en gebruik optioneel de Auditor-app om de integriteit van uw installatie te bevestigen.

## Referenties

1. [GrapheneOS Website](https://grapheneos.org/)
2. [GrapheneOS Webinstaller](https://grapheneos.org/install/web)
3. [GrapheneOS CLI-installatiegids](https://grapheneos.org/install/cli)
4. [GrapheneOS Releases](https://grapheneos.org/releases)
5. [GrapheneOS Gebruiksgids](https://grapheneos.org/usage)
6. [GrapheneOS FAQ](https://grapheneos.org/faq)
7. [Auditor App](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
