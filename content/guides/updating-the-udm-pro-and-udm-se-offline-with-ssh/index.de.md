---
title: "Offline-Firmware-Update für Ubiquiti Unifi UDM Pro und UDM SE über Befehlszeilen-SSH"
draft: false
toc: true
date: 2023-05-28
description: "Erfahren Sie, wie Sie die Firmware von Ubiquiti Unifi UDM Pro und UDM SE offline über die Befehlszeile SSH aktualisieren, um optimale Leistung und Sicherheit zu gewährleisten."
tags: ["Ubiquiti-Firmware-Update", "UDM Pro", "UDM SE", "Offline-Firmware-Update", "Befehlszeilen-SSH", "Netzwerk Management", "Netzwerksicherheit", "Firmware-Upgrade", "SSH-Verbindung", "Firmware-Datei", "UniFi-Netzwerkcontroller", "Fehlerbehebung", "Leistungsverbesserungen", "Sicherheitspatches", "Vernetzung", "Netzwerkgeräte", "Technologie", "IT-Management", "Firmware-Update-Prozess", "Netzwerkoptimierung", "Ubiquiti Networks-Firmware-Update", "UDM Pro-Firmware-Update", "UDM SE-Firmware-Update", "Offline-Firmware-Aktualisierungsprozess", "SSH-Firmware-Update", "Verwaltung von Netzwerkgeräten", "Netzwerksicherheitsupdates", "Firmware-Update-Strategien", "Offline-Firmware-Verwaltung", "Optimierung der Netzwerkleistung", "Verwaltung von Sicherheitspatches", "Aktualisierungen der Netzwerktechnologie"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "Eine farbenfrohe Illustration, die einen Computer zeigt, der über SSH eine Verbindung zu einem Router herstellt und den Offline-Firmware-Aktualisierungsprozess für Ubiquiti Unifi UDM Pro- und UDM SE-Geräte symbolisiert."
coverCaption: ""
---

**Aktualisieren Sie Ubiquiti Unifi UDM Pro und UDM SE offline über SSH**

In der Welt der Netzwerke hat **Ubiquiti Networks** für seine innovativen Lösungen Anerkennung gefunden. **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** und **Unifi Dream Machine SE (UDM SE)** sind zwei beliebte Produkte, die umfassende Netzwerkverwaltungsfunktionen bieten. Die Aktualisierung der Firmware dieser Geräte ist entscheidend, um optimale Leistung und Sicherheit zu gewährleisten. In diesem Artikel erfahren Sie, wie Sie die Firmware von UDM Pro und UDM SE **offline** mithilfe von Befehlszeilen-SSH aktualisieren.

______

## Warum Firmware aktualisieren?

Firmware-Updates sind für jedes Netzwerkgerät unerlässlich, da sie häufig Fehlerbehebungen, Leistungsverbesserungen und Sicherheitspatches enthalten. Die regelmäßige Aktualisierung der Firmware Ihres UDM Pro und UDM SE ist entscheidend, um sicherzustellen, dass Ihr Netzwerk sicher bleibt und reibungslos funktioniert.

______

## Offline-Firmware-Update

Das Aktualisieren der Firmware von UDM Pro und UDM SE kann über das **UniFi Dashboard** erfolgen. In einigen Szenarien ist jedoch möglicherweise keine Internetverbindung verfügbar oder wünschenswert. In solchen Fällen bietet ein Offline-Update über Befehlszeilen-SSH eine alternative Lösung.

______

## Vorbereitung auf das Offline-Update

Bevor Sie mit dem Offline-Update fortfahren, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

1. Ein Computer oder Gerät mit installiertem SSH-Client.
2. Die neueste Firmware-Datei für Ihr UDM Pro oder UDM SE. Die Firmware-Datei erhalten Sie unter [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) Konto

______

## SSH-Verbindung herstellen

Um UDM Pro oder UDM SE über Befehlszeilen-SSH zu aktualisieren, führen Sie die folgenden Schritte aus:

1. Stellen Sie sicher, dass Ihr Computer oder Gerät mit demselben Netzwerk wie UDM Pro oder UDM SE verbunden ist.
2. Öffnen Sie Ihren bevorzugten SSH-Client und stellen Sie eine SSH-Verbindung zur **IP-Adresse von UDM Pro oder UDM SE** her. Wenn Sie beispielsweise den **OpenSSH-Client** unter Linux oder macOS verwenden, können Sie den folgenden Befehl verwenden:

```bash
ssh root@<UDM_IP_ADDRESS>
```

Ersetzen `<UDM_IP_ADDRESS>` mit der tatsächlichen IP-Adresse Ihres UDM Pro oder UDM SE.

3. Geben Sie den **Benutzernamen** und das **Passwort** ein, wenn Sie dazu aufgefordert werden. Die Standardanmeldeinformationen für Ubiquiti-Geräte lauten normalerweise `ubnt` sowohl für den Benutzernamen als auch für das Passwort.

______

## Firmware aktualisieren

Sobald Sie die SSH-Verbindung hergestellt haben, können Sie mit dem Firmware-Update fortfahren:

1. Laden Sie die Firmware-Datei mit **SCP (Secure Copy)** auf das UDM Pro oder UDM SE hoch. SCP ermöglicht eine sichere Dateiübertragung über SSH. Vorausgesetzt, die Firmware-Datei befindet sich auf Ihrem lokalen Computer, können Sie den folgenden Befehl verwenden:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Ersetzen `<FIRMWARE_FILE_PATH>` mit dem Pfad zur Firmware-Datei auf Ihrem lokalen Computer und `<UDM_IP_ADDRESS>` mit der IP-Adresse Ihres UDM Pro oder UDM SE.

2. Sobald die Firmware-Datei hochgeladen ist, können Sie den Firmware-Aktualisierungsprozess starten. Führen Sie den folgenden Befehl aus:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. Das UDM Pro oder UDM SE startet den Firmware-Aktualisierungsprozess. Das kann mehrere Minuten dauern. **Unterbrechen Sie den Vorgang nicht**, bis das Update abgeschlossen ist.

4. Nachdem das Update abgeschlossen ist, können Sie die Firmware-Version überprüfen, indem Sie sich beim UniFi Network Controller anmelden oder den folgenden Befehl ausführen:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Bitte beachten Sie, dass der obige Vorgang davon ausgeht, dass Sie über die erforderliche Firmware-Datei für Ihr UDM Pro oder UDM SE verfügen. Stellen Sie sicher, dass Sie über die richtige Firmware-Datei für Ihr spezifisches Gerätemodell und Ihre spezifische Geräteversion verfügen.

## Abschluss

Das Aktualisieren der Firmware Ihrer Ubiquiti Unifi UDM Pro- und UDM SE-Geräte ist ein entscheidender Schritt, um optimale Leistung und Sicherheit zu gewährleisten. Während der UniFi Network Controller eine bequeme Möglichkeit zum Aktualisieren der Firmware bietet, bietet die Durchführung eines Offline-Updates über die Befehlszeile SSH eine praktikable Lösung, wenn keine Internetverbindung verfügbar oder wünschenswert ist.

Wenn Sie die in diesem Artikel beschriebenen Schritte befolgen, können Sie die Firmware Ihrer UDM Pro- und UDM SE-Geräte mithilfe der Befehlszeilen-SSH erfolgreich aktualisieren. Denken Sie daran, immer die neueste Firmware-Version von Ubiquiti Networks zu verwenden, um von Fehlerbehebungen, Leistungsverbesserungen und Sicherheitspatches zu profitieren.

## Verweise

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Offizielle Ubiquiti-Downloadseite für Firmware-Dateien.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)
