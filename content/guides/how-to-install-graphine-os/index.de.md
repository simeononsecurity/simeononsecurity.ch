---
title: "Ultimativer Leitfaden: GrapheneOS auf Ihrem Google Pixel installieren"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Erfahren Sie, wie Sie GrapheneOS auf Ihrem Google Pixel installieren – für mehr Privatsphäre und Sicherheit. Anleitung für Web-Installer und Kommandozeile (CLI)."
tags: ["GrapheneOS", "Google Pixel", "Privatsphäre", "Sicherheit", "Android", "mobile Geräte", "Betriebssystem", "Installationsanleitung", "Custom ROM", "datenschutzorientiert", "Datenschutz", "sicheres Betriebssystem", "Open Source", "Gerätesicherheit", "Datenschutzfunktionen", "persönliche Daten", "mobile Privatsphäre", "Datenprivatsphäre", "Geräteanpassung", "Technologie", "Pixelinstallation", "fastboot", "Bootloader", "Verified Boot", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "Eine abstrakte digitale Illustration eines Google Pixel-Smartphones, das per USB-C-Kabel mit einem Computer verbunden ist, umgeben von grafischen Elementen, die Datenübertragung und Sicherheit symbolisieren."
coverCaption: ""
---

**So installieren Sie GrapheneOS auf Ihrem Google Pixel-Gerät**

GrapheneOS ist ein quelloffenes, datenschutzorientiertes Betriebssystem auf Android-Basis. Es bietet erheblich verbesserte Sicherheitshärtung und Datenschutzfunktionen und ist damit eine ausgezeichnete Wahl für alle, denen Datenschutz und Sicherheit wichtig sind. Wenn Sie ein unterstütztes Google Pixel besitzen und zu GrapheneOS wechseln möchten, erklärt diese Anleitung sowohl die empfohlene **Web-Installer**-Methode als auch die klassische **Kommandozeilen-Methode (CLI)**.

> **Tipp:** Bei Problemen während der Installation fragen Sie im [offiziellen GrapheneOS-Chat](https://grapheneos.org/contact#community) nach Hilfe. Versuchen Sie zunächst, die Anleitung selbständig zu befolgen, und fragen Sie dann gezielt nach, wo Sie nicht weiterkommen.

## Voraussetzungen

### Hardware- und Systemanforderungen

- Ein Computer mit mindestens **2 GB freiem Arbeitsspeicher** und **32 GB freiem Speicherplatz**.
- Ein **hochwertiges USB-C-Kabel**, das dem Gerät beiliegt (oder ein USB-C-zu-USB-A-Kabel bei Bedarf). Vermeiden Sie USB-Hubs – verbinden Sie direkt mit einem hinteren Desktop-Port oder Laptop-Port.
- Die Installation aus einer virtuellen Maschine wird **nicht empfohlen**, da die USB-Weiterleitung unzuverlässig ist.

> Aktualisieren Sie Ihr Pixel-Gerät am besten vor der Installation von GrapheneOS, um die neueste Firmware zu haben. GrapheneOS flasht die aktuelle Firmware jedoch ohnehin zu Beginn des Installationsprozesses.

### Offiziell unterstützte Betriebssysteme

#### Web-Installer

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (Ubuntu-22.04-LTS-Anleitung befolgen), Linux Mint 22 (Ubuntu-24.04-LTS-Anleitung befolgen)
- Linux Mint Debian Edition 6 (Debian-12-Anleitung befolgen)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15 und 16 mit Play Protect-Zertifizierung

#### CLI-Methode

Alle oben genannten außer ChromeOS, GrapheneOS und Android (diese unterstützen nur den Web-Installer).

Ältere, nicht mehr unterstützte Versionen dieser Plattformen können ebenfalls verwendet werden, sind jedoch nicht offiziell unterstützt. **Stellen Sie sicher, dass Ihr Betriebssystem aktuell ist, bevor Sie fortfahren.**

### Offiziell unterstützte Browser (nur Web-Installer)

- **Chromium** (außer Ubuntu – deren Snap-Paket unterstützt WebUSB nicht korrekt)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (mit deaktiviertem Brave Shields – er begrenzt die Speichernutzung zur Fingerabdruckvermeidung)

> - Auf Android **deaktivieren Sie den Desktop-Modus** in Ihrem Browser. Der Desktop-Modus verhindert, dass der Web-Installer Android erkennt und nach Reboots die Verbindungserlaubnis anfordert. Auf großen Tablets mit 8 GB+ RAM (z. B. Pixel Tablet) ist er standardmäßig aktiviert.
> - Vermeiden Sie Flatpak- und Snap-Browserversionen – diese verursachen Probleme bei der Installation.
> - Verwenden Sie **keinen** Inkognito-/Privatmodus – diese Modi schränken den Speicherplatz ein, der zum Entpacken des Downloads benötigt wird.

### Unterstützte Geräte

Sie benötigen eines der [offiziell unterstützten Pixel-Geräte](https://grapheneos.org/faq#supported-devices). **Vermeiden Sie Carrier-Varianten** – Carrier-Pixels haben eine Carrier-ID ab Werk, die das Entsperren des Bootloaders verhindert. Verwenden Sie ein carrierunabhängiges (entsperrtes) Gerät.

---

## OEM-Entsperrung aktivieren

Die OEM-Entsperrung muss vom Betriebssystem aus aktiviert werden, bevor Sie fortfahren können.

1. Öffnen Sie **Einstellungen → Über das Telefon/Tablet** und tippen Sie wiederholt auf **Build-Nummer**, bis der Entwicklermodus aktiviert ist.
2. Öffnen Sie **Einstellungen → System → Entwickleroptionen** und aktivieren Sie **OEM-Entsperrung**. Bei einigen Carrier-fähigen SKUs ist dafür eine aktive Internetverbindung erforderlich, damit das Standard-OS prüfen kann, ob das Gerät nicht als carrier-gesperrt verkauft wurde.

> **Hinweis zu Pixel 6a:** Die OEM-Entsperrung funktioniert nicht mit der werksseitig vorinstallierten OS-Version. Aktualisieren Sie per OTA auf das Release vom **Juni 2022** oder neuer, führen Sie dann einen Werksreset durch, um die OEM-Entsperrung zu beheben.

---

## Installationsmethode 1: Web-Installer (Empfohlen)

Der [GrapheneOS Web-Installer](https://grapheneos.org/install/web) ist für die meisten Benutzer der empfohlene Ansatz. Er nutzt WebUSB direkt im Browser – keine Softwareinstallation erforderlich.

### Schritt 1: fwupd-Fehler umgehen (nur Linux)

Unter Linux ist bekannt, dass `fwupd` sich fälschlicherweise mit Geräten über das Fastboot-Protokoll verbindet und den Installer blockiert. Stoppen Sie es, bevor Sie Ihr Gerät anschließen:

```bash
sudo systemctl stop fwupd.service
```

Dies wird nach einem Neustart nicht mehr aktiv sein.

### Schritt 2: udev-Regeln einrichten (nur Linux)

Unter Arch Linux:

```bash
sudo pacman -S android-udev
```

Unter Debian und Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Schritt 3: Bootloader-Oberfläche starten

Halten Sie die **Lautstärke-runter**-Taste gedrückt, während das Gerät startet (entweder aus dem ausgeschalteten Zustand hochfahren oder neu starten und dabei die Taste halten). Das Gerät muss ein **rotes Warndreieck** und die Aufschrift **"Fastboot Mode"** anzeigen – drücken Sie nicht die Ein/Aus-Taste, um "Start" zu aktivieren.

### Schritt 4: Gerät anschließen

Schließen Sie das Gerät per USB an Ihren Computer an. Unter Linux schließen Sie das Kabel erneut an, falls die udev-Regeln nicht vor der ersten Verbindung eingerichtet wurden.

> **Pixel Tablet:** Trennen Sie das Tablet vom Ständer, bevor Sie es per USB verbinden – Tablet und Ständer können nicht gleichzeitig verwendet werden.

> **Windows:** Aktuelle Windows-10/11-Versionen enthalten einen generischen Fastboot-Treiber für Pixel 4a (5G) und neuere Modelle. Für ältere Pixels oder veraltetes Windows installieren Sie den Treiber über Windows Update (unter "Optionale Updates anzeigen" → "LeMobile Android Device").

### Schritt 5: Bootloader entsperren

Öffnen Sie [https://grapheneos.org/install/web](https://grapheneos.org/install/web) und klicken Sie auf die Schaltfläche **Bootloader entsperren**. Bestätigen Sie auf dem Gerät mit den Lautstärketasten zur Auswahl und der Ein/Aus-Taste zur Bestätigung. **Dadurch werden alle Daten gelöscht.**

### Schritt 6: Factory Images herunterladen und flashen

1. Klicken Sie auf **Release herunterladen**, um die Factory Images für Ihr Gerät herunterzuladen.
2. Klicken Sie auf **Factory Images flashen** und warten Sie, bis der Vorgang abgeschlossen ist. Er flasht automatisch die Firmware, startet neu in die Bootloader-Oberfläche und flasht das OS. **Interagieren Sie nicht mit dem Gerät, bis der Vorgang abgeschlossen ist.**

### Schritt 7: Bootloader sperren

Klicken Sie nach dem Flashen im Web-Installer auf **Bootloader sperren**. Bestätigen Sie auf dem Gerät. **Dadurch werden alle Daten erneut gelöscht** – das Sperren des Bootloaders aktiviert den vollständigen Verified Boot.

---

## Installationsmethode 2: Kommandozeile (CLI)

### Schritt 1: Terminal öffnen

Öffnen Sie unter Windows ein **normales (kein Administrator-) PowerShell**-Fenster. Entfernen Sie den alten `curl`-Alias:

```powershell
Remove-Item Alias:Curl
```

### Schritt 2: fastboot installieren

Sie benötigen fastboot Version **≥ 35.0.1**.

**Arch Linux:**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** – deren Pakete sind veraltet. Verwenden Sie das eigenständige Release:

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

Version prüfen:

```bash
fastboot --version
# Erwartet: fastboot version 35.0.2-12147458
```

### Schritt 3: udev-Regeln einrichten (nur Linux)

Arch Linux:

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Schritt 4: fwupd-Fehler umgehen (nur Linux)

```bash
sudo systemctl stop fwupd.service
```

### Schritt 5: Bootloader-Oberfläche starten

Halten Sie **Lautstärke runter** beim Starten gedrückt, bis das Gerät **"Fastboot Mode"** mit dem roten Warndreieck anzeigt.

### Schritt 6: Gerät anschließen und Bootloader entsperren

Verbinden Sie das Gerät per USB, dann führen Sie aus:

```bash
fastboot flashing unlock
```

Bestätigen Sie auf dem Gerät (Lautstärketasten zur Auswahl, Ein/Aus-Taste zur Bestätigung). **Dadurch werden alle Daten gelöscht.**

### Schritt 7: OpenSSH installieren (zur Image-Verifizierung)

macOS und Windows enthalten OpenSSH standardmäßig.

Arch Linux:

```bash
sudo pacman -S openssh
```

Debian / Ubuntu:

```bash
sudo apt install openssh-client
```

### Schritt 8: Factory Images herunterladen und verifizieren

Signierschlüssel herunterladen:

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Erwarteter Inhalt:

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Factory Images herunterladen (ersetzen Sie `DEVICE_NAME` und `VERSION` durch die tatsächlichen Werte):

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Signatur verifizieren (Linux / macOS):

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows:

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Erwartete Ausgabe:

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Schritt 9: Factory Images flashen

Images entpacken:

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

In das Verzeichnis wechseln und das Flash-Skript ausführen:

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Warten Sie, bis der Vorgang abgeschlossen ist. Er erledigt das Flashen der Firmware, Bootloader-Neustarts und das Flashen des OS automatisch. **Interagieren Sie nicht mit dem Gerät, bis der Vorgang abgeschlossen ist.**

> **Linux-tmpfs-Fehlersuche:** Wenn `/tmp` nicht genug Speicher hat, verwenden Sie:
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Schritt 10: Bootloader sperren

```bash
fastboot flashing lock
```

Bestätigen Sie auf dem Gerät. **Dadurch werden alle Daten erneut gelöscht.** Das Sperren aktiviert den vollständigen Verified Boot und verhindert, dass Fastboot Partitionen modifiziert.

---

## Nach der Installation

### Starten

Drücken Sie die Ein/Aus-Taste mit der standardmäßig ausgewählten Option **Start** in der Bootloader-Oberfläche, um GrapheneOS zu starten.

### OEM-Entsperrung deaktivieren

Beim ersten Setup enthält der letzte Bildschirm einen Schalter für die OEM-Entsperrung (standardmäßig aktiviert – aktiviert lassen **deaktiviert** die OEM-Entsperrung). Dies wird empfohlen. Sie können es später in den **Entwickleroptionen** ändern.

### Installation verifizieren

GrapheneOS nutzt Verified Boot und Hardware-Attestierung. Verified Boot prüft bei jedem Start alle Firmware- und OS-Images anhand von Schlüsseln, die in die SoC-Sicherungen gebrannt sind. GrapheneOS flasht seinen eigenen Verified-Boot-Schlüssel in das Sicherheitselement – bei jedem Start verifiziert dieser Schlüssel das OS.

#### Verified Boot Key Hashes

Wenn ein alternatives OS geladen wird, zeigt das Gerät einen **gelben Hinweis** mit der OS-Kennung (sha256 des Verified-Boot-Schlüssels). Pixel der 4. und 5. Generation zeigen nur die ersten 32 Bits; **Pixel der 6. Generation und neuer zeigen den vollständigen Hash**. Vergleichen Sie mit den offiziellen Hashes:

| Gerät | Verified Boot Key Hash |
|-------|----------------------|
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

#### Hardware-basierte Attestierung mit Auditor

GrapheneOS stellt die [Auditor-App](https://attestation.app/) bereit, um Hardware, Firmware und OS-Integrität mittels Verified Boot und Remote-Attestierung zu verifizieren. Ergebnisse werden auf einem zweiten Android-Gerät mit Auditor angezeigt (nicht auf dem zu verifizierenden Gerät), oder über den optionalen [Geräte-Integritäts-Überwachungsdienst](https://attestation.app/) für automatische geplante Überprüfungen mit E-Mail-Benachrichtigungen.

---

## GrapheneOS durch das Standard-OS ersetzen

Die Installation des Standard-OS über Googles [Web-Flash-Tool](https://flash.android.com/) ähnelt dem obigen Prozess. Bevor Sie jedoch flashen und sperren, müssen Sie den GrapheneOS Verified Boot Key löschen, um vollständig zum Standard zurückzukehren:

**Web-Installer:** Verwenden Sie die Schaltfläche "Nicht-Standard-Schlüssel löschen" im GrapheneOS Web-Installer.

**CLI:**

```bash
fastboot erase avb_custom_key
```

Flashen Sie dann die Standard-Factory-Images und sperren Sie den Bootloader.

---

## Fazit

Die Installation von GrapheneOS auf Ihrem Google Pixel bietet branchenführende Datenschutz- und Sicherheitsfunktionen. Verwenden Sie den **Web-Installer** unter [grapheneos.org/install/web](https://grapheneos.org/install/web) für die einfachste Erfahrung, oder folgen Sie den CLI-Schritten oben für einen klassischen Ansatz. Sperren Sie den Bootloader nach dem Flashen immer, um den vollständigen Verified Boot zu aktivieren, und verwenden Sie optional die Auditor-App, um die Integrität Ihrer Installation zu bestätigen.

## Referenzen

1. [GrapheneOS-Website](https://grapheneos.org/)
2. [GrapheneOS Web-Installer](https://grapheneos.org/install/web)
3. [GrapheneOS CLI-Installationsanleitung](https://grapheneos.org/install/cli)
4. [GrapheneOS Releases](https://grapheneos.org/releases)
5. [GrapheneOS Nutzungsanleitung](https://grapheneos.org/usage)
6. [GrapheneOS FAQ](https://grapheneos.org/faq)
7. [Auditor App](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
