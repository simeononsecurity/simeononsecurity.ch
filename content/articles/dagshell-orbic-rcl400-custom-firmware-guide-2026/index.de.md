---
title: "DagShell Custom Firmware für Orbic RCL400: Vollständige Installations- und Nutzungsanleitung 2026"
date: 2026-05-28
toc: true
draft: false
description: "Umfassende Anleitung zur DagShell Custom Firmware für den Orbic RCL400 Hotspot, einschließlich Installation, Datenschutz-Tools, Hacking-Funktionen, Wardriving-Fähigkeiten und warum es sich perfekt mit RayHunter für mobile Sicherheitsforschung kombiniert."
genre: ["Custom Firmware", "Mobile Sicherheit", "Datenschutz-Tools", "Netzwerksicherheit", "Wardriving", "Penetrationstests", "IoT-Hacking", "Sicherheitsforschung", "Hardware-Hacking", "Datenschutztechnologie"]
tags: ["DagShell", "Orbic RCL400", "Custom Firmware", "Hotspot-Hacking", "Datenschutz-Tools", "TTL-Fix", "MAC-Spoofing", "IMSI-Catcher-Erkennung", "Wardriving", "GPS-Tracking", "Evil-Twin-Angriff", "Captive Portal", "DNS-Sniffer", "ARP-Scanner", "Port-Scanner", "Raspberry Pi Companion", "WiFi-Sicherheit", "Mobiler Hotspot", "Netzwerküberwachung", "Penetrationstests", "Sicherheitsforschung", "Bluetooth-Scanning", "Deauth-Angriff", "WiFi-Scanning", "OUI-Lookup", "Wigle-Upload", "Mobilfunkturm-Monitoring", "AT-Befehle", "Firewall-Manager", "AdBlock", "TLS-Verschlüsselung", "RayHunter-Integration", "STS Collective", "Mobiles Sicherheitslabor", "Netzwerkanalyse", "Datenschutz-Firmware", "Open-Source-Sicherheit", "ARM-Cross-Compilation", "Embedded Linux", "Sicherheits-Toolkit", "Hacker-Tools", "Red Team", "Netzwerk-Aufklärung"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Eine Illustration eines Orbic RCL400 mobilen Hotspots mit einer glühenden grünen Oberfläche, umgeben von abstrakten Darstellungen von Sicherheits-Tools wie Diagrammen und Karten, vor einem dunklen Marineblau-Hintergrund."
coverCaption: ""
---

**Verwandeln Sie Ihren Orbic RCL400 in ein mobiles Sicherheitsforschungslabor**

## Einführung: Ein Hacker-Hotspot

**DagShell** ist Open-Source-Custom-Firmware für den **Orbic RCL400 mobilen Hotspot**, die ein gewöhnliches Mobilfunkgerät in ein **tragbares Sicherheitsforschungs- und Datenschutz-Toolkit** verwandelt. Vom Sicherheitsforscher "dag" erstellt, bietet diese terminal-stilisierte Firmware **Hacking-Tools, Datenschutzfunktionen und Netzwerküberwachungsfähigkeiten** in einer schlanken, grün-auf-schwarz Hacker-Ästhetik-Oberfläche.

Dieser umfassende Leitfaden deckt ab:
- **Was DagShell ist** und sein vollständiges Feature-Set
- **Schritt-für-Schritt-Installations**-Anweisungen (Webflasher und manuelle Methoden)
- **Alle Tools und Fähigkeiten** im Detail erklärt
- **Raspberry Pi Companion**-Setup für erweiterte Funktionalität
- **Warum DagShell mit RayHunter kombinieren** für ultimative mobile Sicherheit
- **Reale Anwendungsfälle** für Sicherheitsforscher und Datenschutzbefürworter
- **Rechtliche und ethische Überlegungen**

**Kurzfassung**: DagShell + RayHunter auf Orbic RCL400 = **Vollständiges mobiles Sicherheitslabor** für IMSI-Catcher-Erkennung, Wardriving, Netzwerkanalyse und Datenschutzschutz.

**Vorgeflashte Geräte erhältlich**: Dieser Artikel wird von **STS Collective** gesponsert, das vorgeflashte Orbic RCL400 Hotspots mit sowohl **RayHunter und DagShell** vorinstalliert und einsatzbereit anbietet: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Exklusiver Lesernachlass**: Sparen Sie bis zu 20% auf STS Collective-Produkte einschließlich vorgeflashter Orbic RCL400-Geräte - verwenden Sie den Code **SIMEONONSECURITY** beim Checkout oder [kaufen Sie mit angewendetem Rabatt](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Was ist DagShell?

### Überblick

**DagShell** ist Open-Source-Custom-Firmware, die die Standard-Orbic-RCL400-Weboberfläche durch ein **umfassendes Sicherheits-Toolkit** ersetzt mit:

- **Terminal-Stil-Oberfläche** mit ASCII-Kunst und Hacker-Ästhetik
- **TLS 1.2+ verschlüsselte** Weboberfläche (selbstsigniertes Zertifikat)
- **Datenschutz-Tools** (TTL-Maskierung, MAC-Spoofing, DNS-basierter Ad-Block)
- **Netzwerküberwachung** (aktive Verbindungen, Routing-Tabellen, DNS-Abfragen)
- **Hacking-Tools** (IMSI-Catcher-Erkennung, Port-Scanning, ARP-Erkennung)
- **Angriffsfähigkeiten** (Evil-Twin-AP, Captive-Portal-Phishing, Deauth-Angriffe)
- **GPS-Tracking und Wardriving** mit Wigle-kompatiblem CSV-Export
- **Raspberry Pi Companion** für GPS, Bluetooth-Scanning und WiFi-Aufklärung
- **Dateisystemzugriff** mit browserbasiertem Dateimanager
- **SMS-Funktionalität** via AT-Befehle
- **Persistenz** - Automatischer Start beim Booten

### Technische Spezifikationen

**Plattform**: Orbic RCL400 mobiler Hotspot
**Architektur**: ARM Linux (Kernel 3.18)
**Sprache**: C/C++ (statisches ARM-Binary)
**Verschlüsselung**: TLS 1.2+ mit selbstsignierten Zertifikaten (2-Tier-PKI)
**Webserver**: Benutzerdefinierter eingebetteter HTTPS-Server (Port 8443)
**Oberfläche**: Browserbasierte Terminal-UI
**Lizenz**: MIT (Open-Source)
**GitHub**: [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

______

## Vollständige Feature-Übersicht

### Datenschutzschutz-Suite

#### TTL-Fix

**Zweck**: Hotspot-Traffic vor Carrier-Erkennung maskieren

**Funktionsweise**:
- Modifiziert den **Time To Live (TTL)**-Wert in IP-Paketen auf **65**
- Carrier erkennen Tethering durch TTL-Dekremente (Telefon=64, gebundenes Gerät=63)
- TTL auf 65 setzen lässt **allen Traffic lokal erscheinen**

**Anwendungsfall**: Carrier-Tethering-Beschränkungen/Drosselung umgehen

#### MAC-Adress-Spoofing

**Zweck**: Geräte-MAC-Adresse für Datenschutz randomisieren

**Funktionsweise**:
- Ändert MAC-Adresse von **wlan0** (WiFi-Schnittstelle)
- Generiert **zufällige MAC** oder erlaubt benutzerdefinierte Eingabe
- Macht Gerät **nicht verfolgbar** über Sitzungen hinweg

#### DNS-basierter AdBlock

**Zweck**: Werbung und Tracking auf DNS-Ebene blockieren

**Funktionsweise**:
- Modifiziert `/etc/hosts`-Datei mit **Blockliste**
- Domains auf der Liste lösen zu **127.0.0.1** (localhost) auf
- Blockiert Werbung **für alle verbundenen Geräte**

### Hacking-Tools

#### IMSI-Catcher-Detektor

**Zweck**: Mobilfunkturm-Informationen auf Anomalien überwachen, die **IMSI-Catcher/Stingray**-Geräte anzeigen

**Erkennungsindikatoren**:
- **Plötzlicher Mobilfunktsurmwechsel** im Stillstand
- **Downgrade auf 2G** *(IMSI-Catcher erzwingen oft 2G, um Verschlüsselung zu entfernen)*
- **Unbekannte Cell ID** erscheint
- **Schwaches Signal** vom Fake-Turm
- **Häufige Wiederverbindungen**

#### Port-Scanner

**Zweck**: Ziel-IP-Adressen auf offene Ports scannen

**Anwendungsfälle**:
- **Netzwerkaufklärung**
- **IoT-Geräteerkennung**
- **Sicherheitsaudit** lokaler Netzwerke
- **Dienst-Identifikation**

#### Firewall-Manager

**Zweck**: IP-Adressen mit iptables blockieren oder entsperren

### Angriffs-Tools

**WICHTIGER RECHTLICHER HINWEIS**: Diese Tools sind ausschließlich für **autorisierte Sicherheitstests**. Sie gegen Netzwerke einzusetzen, die Sie nicht besitzen oder für die Sie keine ausdrückliche schriftliche Genehmigung haben, ist in den meisten Rechtsordnungen **ILLEGAL**.

#### DNS-Sniffer

**Zweck**: DNS-Abfragen von verbundenen Clients protokollieren

*Dies erfasst Metadaten (besuchte Domains) von verbundenen Clients. Setzen Sie es nur auf Netzwerken ein, die Sie besitzen oder verwalten.*

#### ARP-Scanner

**Zweck**: Geräte im lokalen Netzwerk entdecken

**Ausgabe-Beispiel**:
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.
```

#### Evil-Twin-AP

**Zweck**: Gefälschten WiFi-Access-Point erstellen, der vorhandene SSIDs klont

**Angriffsszenarien** nur in **Labor-Umgebungen** verwenden.

#### Captive Portal

**Zweck**: Phishing-Seitenvorlagen für Anmeldedaten-Erfassung

**Bildungszweck**: Zeigt **Social-Engineering-Risiken** und warum Benutzer URLs überprüfen sollten

### GPS-Tracker & Wardriving

#### GPS-Funktionalität

**GPS-Quelle**: **Nur Raspberry Pi Companion**
- Der Orbic RCL400 hat **kein integriertes GPS**
- Pi verbindet **USB-GPS-Dongle** (U-Blox 7-Chipsatz)

#### Wardriving-Modus

**Zweck**: WiFi-Netzwerke mit GPS-Koordinaten für die Kartierung scannen

**Wigle-Integration**:
- DagShell CSV ist **direkt auf WiGLE hochladbar**
- Trägt zur **öffentlichen Datenbank** von WiFi-Standorten bei

**CSV-Format-Beispiel**:
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

### Raspberry Pi Companion

Der **Raspberry Pi Companion** erweitert DagShell-Fähigkeiten mit **externer Hardware**:

#### Hardware-Anforderungen

**Minimum**:
- **Raspberry Pi 3B+** oder neuer
- **USB-GPS-Dongle** (U-Blox 7-Chipsatz empfohlen)
- **Stromversorgung** *(Pi benötigt separate Stromversorgung)*

______

## Installationsanleitung

### Methode 1: Web-Flasher (Empfohlen)

**Einfachste Methode** - Keine Befehlszeile erforderlich

**Schritt 1**: DagShell Webflasher besuchen
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Schritt 2**: PKI-Zertifikate generieren
- Klicken Sie auf **"Generate Certificates"** Schaltfläche
- Browser generiert **2-Tier-PKI** (Root CA + Server-Zertifikat)
- **Dateien herunterladen**: `root.der` und `server.der`

**Schritt 3**: Root-Shell auf Orbic aktivieren
- Mit Orbic WiFi-Netzwerk verbinden
- **Admin-Passwort** im Webformular eingeben
- Auf **"Enable Shell"** klicken

**Schritt 4**: Firmware deployen
- Auf **"Deploy DagShell"** Schaltfläche klicken

**Schritt 5**: Orbic neu starten
- Gerät aus- und einschalten
- DagShell startet automatisch beim Booten

**Schritt 6**: DagShell aufrufen
- Browser auf: `https://192.168.1.1:8443/` öffnen
- **Sicherheitswarnung** akzeptieren (selbstsigniertes Zertifikat - das ist erwartet)

### Methode 2: Manuelle Installation

**Für fortgeschrittene Benutzer**, die aus dem Quellcode erstellen möchten

#### Schritt 1: Abhängigkeiten installieren

**Windows**:
```powershell
pip install requests cryptography
```

**macOS**:
```bash
brew install python3
pip3 install requests cryptography
```

**Linux**:
```bash
sudo apt-get install python3 python3-pip
pip3 install requests cryptography
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Schritt 2: Repository klonen

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Schritt 3: Firmware erstellen

**macOS/Linux**:
```bash
cd orbic_fw_c
python3 gen_pki.py
./build.sh
```

#### Schritt 4: Root-Shell auf Orbic aktivieren

```bash
python enable_shell.py IHR_ADMIN_PASSWORT
```

#### Schritt 5: Firmware deployen

```bash
python deploy_base64.py
```

#### Schritt 6: Neu starten und aufrufen

```bash
reboot
# Browser: https://192.168.1.1:8443/
```

______

## Warum DagShell mit RayHunter kombinieren?

### Komplementäre Fähigkeiten

| Feature | DagShell | RayHunter |
|---------|----------|-----------|
| **IMSI-Catcher-Erkennung** | Grundlegendes Mobilfunkturm-Monitoring | Erweiterte Musteranalyse |
| **GPS-Tracking** | Ja (via Pi) | Ja (via Modem) |
| **WiFi-Wardriving** | Ja | Nein |
| **Bluetooth-Scanning** | Ja (via Pi) | Nein |
| **Netzwerk-Tools** | Ja | Nein |
| **Angriffs-Tools** | Ja | Nein |
| **Datenschutz-Tools** | Ja | Minimal |

______

## Reale Anwendungsfälle

### Anwendungsfall 1: Sicherheitsforscher

**Profil**: Penetrationstester, der WiFi-Sicherheitsbewertung durchführt

**DagShell-Workflow**:
1. Um das Clientgelände fahren
2. Wardriving zur Kartierung der WiFi-Abdeckung
3. Evil-Twin des Client-Netzwerks erstellen (mit Erlaubnis)
4. Client-Verbindungsversuche überwachen
5. Bericht mit gesammelten Daten erstellen

### Anwendungsfall 2: Datenschutzbefürworter

**Profil**: International reisender Journalist

**DagShell-Workflow**:
1. TTL-Fix vor Gerätenutzung aktivieren
2. MAC-Adresse randomisieren
3. IMSI-Catcher-Detektor kontinuierlich überwachen
4. AdBlock für alle verbundenen Geräte verwenden
5. Verdächtige Mobilfunkaktivitäten protokollieren

______

## Rechtliche und ethische Überlegungen

### Rechtlicher Rahmen

**Legale Verwendungen**:
- Eigene Netzwerke testen
- Autorisierte Tests mit schriftlicher Erlaubnis
- Bildungszwecke in isolierten Lab-Umgebungen
- Datenschutzschutz auf dem eigenen Gerät

**Illegale Verwendungen**:
- Unbefugter Zugriff auf fremde Netzwerke (CFAA-Verletzung in den USA)
- Deauth-Angriffe auf fremde Netzwerke (FCC-Verletzung)
- Evil-Twin-Angriffe gegen die Öffentlichkeit

### Verantwortungsvoller Einsatz

DagShell ist ein **Sicherheitsforschungs- und Datenschutz-Tool**. Verwenden Sie es **verantwortungsvoll** und **ethisch**. *Wenn Sie unsicher sind, ob etwas legal ist, hören Sie auf und konsultieren Sie einen Anwalt, bevor Sie fortfahren.*

______

## Fazit: Das ultimative mobile Labor

**DagShell** verwandelt den bescheidenen **Orbic RCL400 Hotspot** in ein **leistungsstarkes mobiles Sicherheitslabor** mit:

- Datenschutzschutz (TTL-Maskierung, MAC-Spoofing, AdBlock)
- Netzwerküberwachung (Verbindungen, DNS, Routing)
- Hacking-Tools (IMSI-Erkennung, Port-Scanning, ARP-Erkennung)
- Angriffsfähigkeiten (Evil-Twin, Captive-Portal, Deauth)
- GPS-Wardriving mit Wigle-Integration
- Raspberry Pi-Erweiterung (BLE, WiFi, GPS)
- Tragbar und batteriebetrieben
- Open-Source und anpassbar

Wenn Sie ein **Sicherheitsforscher**, **Penetrationstester**, **Datenschutzbefürworter** oder **Netzwerkadministrator** sind, bietet DagShell eine **tragbare, leistungsstarke und erschwingliche** Plattform für mobile Sicherheitsarbeit.

**Haftungsausschluss**: Verantwortungsvoll einsetzen. Nur Netzwerke und Geräte testen, die Sie besitzen oder für die Sie ausdrückliche schriftliche Genehmigung haben. Bleiben Sie legal und ethisch!

______

## Referenzen

1. [DagShell GitHub Repository](https://github.com/dagnazty/DagShell)
2. [DagShell Documentation](https://dagnazty.github.io/DagShell/)
3. [STS Collective - Pre-Flashed Devices](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE - WiFi Mapping Project](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Raspberry Pi Official Documentation](https://www.raspberrypi.org/documentation/)
7. [U-Blox GPS Module Documentation](https://www.u-blox.com/)
8. [OUI Database - IEEE Standards](https://standards.ieee.org/products-programs/regauth/)
9. [iptables Tutorial](https://www.netfilter.org/documentation/)
10. [OpenSSL Documentation](https://www.openssl.org/docs/)
