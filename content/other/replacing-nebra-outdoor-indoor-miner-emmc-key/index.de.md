---
title: "Ersetzen der Nebra Helium Miner SD-Karte: Schritt-für-Schritt-Anleitung"
draft: false
toc: true
date: 2022-02-13
description: "In dieser Anleitung erfährst du, wie du die Nebra Indoor und Outdoor, erste und zweite Generation, EMMC Key SD-Karte ersetzen oder neu flashen kannst und wie du Probleme mit der Synchronisierung von Helium Miner behebst."
genre: ["Technologie", "Kryptowährung", "Hardware", "Helium Mining", "Fehlersuche", "SD-Karten-Ersatz", "Probleme mit der Synchronisierung", "Raspberry Pi", "Balena Etcher", "Nebra Helium Miner"]
tags: ["Nebra Helium Miner", "SD-Karten-Ersatz", "Probleme mit der Synchronisierung", "Helium Mining", "Fehlersuche", "Raspberry Pi", "Balena Etcher", "Hardware-Anleitung", "SD-Karten-Upgrade", "Behebung von Synchronisierungsproblemen", "Schritt-für-Schritt-Anleitung", "Helium Miner Sync Fix", "Nebra Indoor Bergmann", "Nebra Outdoor Bergmann", "Raspberry Pi Compute Module 3", "Balena Raspberry Pi CM3 Image", "Fehlersuche bei Heliumbergwerken", "Nebra Bergbauausrüstung", "Balena Etcher Software", "Ersetzen des EMMC-Schlüssels auf dem Nebra Miner", "SD-Karten-Reparatur für Helium Miner", "Behebung von Helium Miner Sync-Problemen", "Nebra Miner SD-Karten-Ersatz", "Anleitung zur Fehlerbehebung bei Nebra Helium Miner", "Tipps zum Heliumabbau", "Upgrading Nebra Helium Miner SD Card", "Wie man die Nebra Miner SD-Karte neu importiert", "Fehlerbehebung bei Nebra Helium Miner Synchronisierungsproblemen"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "Eine Cartoon-Illustration einer Person, die einen Nebra Helium Miner in der Hand hält, mit einer geöffneten Klappe, die den SD-Kartensteckplatz und die Schritte des Leitfadens zeigt, der als Leitfaden über dem Gerät schwebt."
coverCaption: "Lösen Sie Synchronisierungsprobleme und aktualisieren Sie Ihren Helium Miner mit Leichtigkeit."
---

**Ersetzen und Neu-Imaging des Nebra Indoor und Outdoor EMMC Key / SD Card**

Diese umfassende Anleitung führt Sie durch den Prozess des Austauschs oder Reflashen des Nebra Indoor und Outdoor EMMC Key/SD Card. Wenn Sie diese Schritte befolgen, können Sie Synchronisationsprobleme mit Ihrem Helium Miner beheben und einen reibungslosen Betrieb sicherstellen. Die Anleitung enthält eine detaillierte Erklärung der benötigten Tools und Software sowie die notwendigen Schritte, um die config.json-Datei zu beschaffen, die neue SD-Karte mit Balena Raspberry Pi CM3 Image zu flashen und die ursprüngliche Konfigurationsdatei auf die neue SD-Karte zu übertragen.

## Einführung

Die Nebra Helium Miner, sowohl die Indoor- als auch die Outdoor-Modelle, sind auf die EMMC Key/SD-Karte angewiesen, damit sie funktionieren. Im Laufe der Zeit kann es notwendig werden, diese Karte zu ersetzen oder neu zu flashen, um Synchronisierungsprobleme zu beheben und eine optimale Leistung zu erhalten. Dieser Leitfaden vermittelt Ihnen das Wissen und die Anleitungen, die Sie benötigen, um diese Aufgabe effektiv auszuführen.

Um die SD-Karte des Nebra Helium Miners erfolgreich auszutauschen, benötigen Sie spezielle Werkzeuge und Software. Zu den Werkzeugen gehören ein Kreuzschlitzschraubendreher oder [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Mit diesen Informationen können Sie die SD-Karte austauschen oder neu flashen.

## Erforderliche Werkzeuge:
- Ein Kreuzschlitzschraubendreher oder [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) für Nebra Outdoor Miner
- Starke Fingernägel, eine Pinzette oder eine Spitzzange zum Entfernen der alten SD-Karte
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Erforderliche Software:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- Aktuelles Nebra-Bild für Ihr spezifisches Gerät:
*Wenn Sie nicht wissen, welches Gerät Sie haben, konsultieren Sie bitte die [nebra documentatio](https://support.nebra.com/support/home) Wenn es älter ist, können Sie davon ausgehen, dass Sie ein Gerät der ersten Generation haben.
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## Das Innere des Nebra Helium Miners:
### Inhalt des Nebra Indoor Miners:
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Inhalt des Nebra Outdoor Miners:
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6,5MMx2,0MM Klinkenstecker
 - 2.) Ethernet-Anschluss
 - 3.) LED-Anzeige
 - 4.) Interface-Taste
 - 5.) 4G / LTE-Modul-Anschluss
 - 6.) Sim-Karten-Steckplatz

## So tauschen Sie die SD-Karte aus
### Schritt 1: Erwerben Sie optional die config.json Datei vom EMMC Key:
- Herunterladen und installieren [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Sie benötigen dies, um das Compute Module als USB-Dateisystem zu booten
- Identifizieren Sie die Jumper-Pins auf der CM3-Tochterplatine und passen Sie sie für den Programmiermodus an
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Micro-USB-Anschluss für die Bildgebung
   - 7.) JP4 USB-Jumper - Dient zum Umschalten zwischen Normalbetrieb und Flash-Modus. Stellen Sie sicher, dass er sich in Position 1-2 für Normalbetrieb und 2-3 für die Programmierung befindet.
   - 8.) JP3 Power Jumper - Ermöglicht die Stromversorgung des Moduls über den Micro-USB-Anschluss. Schließen Sie ihn nur an, wenn Sie vom PC aus programmieren und stellen Sie sicher, dass die Hauptplatine nicht angeschlossen ist.
 - Schieben Sie den JP4 Jumper auf Position 2+3
 - Stecken Sie ein USB-Kabel ein und führen Sie das [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Dienstprogramm
 - Öffnen Sie Ihren Dateiexplorer und Sie werden ein Laufwerk namens "resin-boot" sehen. Rufen Sie die Datei "config.json" aus dem Verzeichnis ab, da Sie diese später benötigen und sie gesichert sein sollte.
 - Ziehen Sie das USB-Kabel ab und setzen Sie den JP4-Jumper auf Position 1+2.
### Schritt 2: Flashen Sie die neue sd-Karte mit dem Balena Raspberry Pi CM3 Image:
- Downloaden und entpacken Sie das entsprechende Image
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Verwendung [Balena Etcher](https://www.balena.io/etcher/) Wählen Sie die kürzlich extrahierte .img-Datei und Ihre neue MicroSD-Karte als Zielgerät aus
- Wählen Sie Flash
### Schritt 3: Installieren Sie die neue SD-Karte und bauen Sie den Nebra Miner wieder zusammen:
 - Installieren Sie die SD-Karte in dem Steckplatz, in dem sich zuvor der EMMC-Schlüssel befand.
 - Bauen Sie den Miner wieder zusammen
 - Wenn Sie den neu geflashten Nebra Miner zum ersten Mal mit Strom versorgen, schließen Sie ihn für 20-30 Minuten an die Ethernet-Verbindung an, bevor Sie wieder eine WLAN-Verbindung herstellen.
### Schritt 4: Gewinn?




