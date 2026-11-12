---
title: "DagShell Custom-Firmware für Orbic RCL400: Leitfaden 2026"
date: 2026-05-28
lastmod: 2026-11-11
toc: true
draft: false
description: "Technischer Leitfaden zur DagShell-Firmware für Orbic RCL400. Behandelt Installation, Datenschutzwerkzeuge, Wardriving und Forschungsgrenzen."
genre: ["Custom-Firmware", "Mobile Sicherheit", "Datenschutzwerkzeuge", "Netzwerksicherheit", "Wardriving", "Penetrationstests", "IoT-Hacking", "Sicherheitsforschung", "Hardware-Hacking", "Datenschutztechnik"]
tags: ["DagShell", "Orbic RCL400", "Custom-Firmware", "Hotspot-Hacking", "Datenschutzwerkzeuge", "TTL-Korrektur", "MAC-Spoofing", "Erkennung von IMSI-Catchern", "Wardriving", "GPS-Ortung", "Evil-Twin-Angriff", "Captive Portal", "DNS-Sniffer", "ARP-Scanner", "Portscanner", "Raspberry-Pi-Begleiter", "Wi-Fi-Sicherheit", "Mobiler Hotspot", "Netzwerküberwachung", "Penetrationstests", "Sicherheitsforschung", "Bluetooth-Scanning", "Deauth-Angriff", "Wi-Fi-Scanning", "OUI-Abfrage", "Wigle-Upload", "Mobilfunkmast-Überwachung", "AT-Befehle", "Firewall-Verwaltung", "Werbeblocker", "TLS-Verschlüsselung", "RayHunter-Integration", "STS Collective", "Mobiles Sicherheitslabor", "Netzwerkanalyse", "Datenschutz-Firmware", "Open-Source-Sicherheit", "ARM-Cross-Compilation", "Embedded Linux", "Sicherheits-Toolkit", "Hacker-Tools", "Red Team", "Netzwerkerkundung"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Illustration eines Orbic-RCL400-Mobilhotspots mit leuchtend grüner Oberfläche. Abstrakte Darstellungen von Sicherheitswerkzeugen wie Diagrammen und Karten umgeben das Gerät vor dunkelblauem Hintergrund."
coverCaption: ""
---

**Verwandle deinen Orbic RCL400 in ein mobiles Sicherheitsforschungslabor**

## Einführung: Ein Hotspot für Hacker

**DagShell** ist eine Open-Source-Custom-Firmware für den **mobilen Hotspot Orbic RCL400**. Sie verwandelt ein gewöhnliches Mobilfunkgerät in ein **tragbares Werkzeugset für Sicherheitsforschung und Datenschutz**. Der Sicherheitsforscher „dag“ entwickelte die Firmware mit einer terminalartigen Oberfläche. Sie bietet **Hacker-Tools, Datenschutzfunktionen und Netzwerküberwachung** in einer grünen Hacker-Optik auf schwarzem Hintergrund.

Dieser umfassende Leitfaden behandelt:
- **Was DagShell ist** und welche Funktionen sie bietet
- **Schrittweise Installationsanleitungen** für Webflasher und manuelle Installation
- **Alle Werkzeuge und Fähigkeiten** im Detail
- Die Einrichtung des **Raspberry-Pi-Begleitgeräts** für zusätzliche Funktionen
- **Warum DagShell mit RayHunter kombiniert werden sollte**
- **Praktische Anwendungsfälle** für Sicherheitsforscher und Datenschutzbefürworter
- **Rechtliche und ethische Aspekte**

**Kurzfassung:** DagShell und RayHunter auf dem Orbic RCL400 ergeben ein **vollständiges mobiles Sicherheitslabor** zur Erkennung von IMSI-Catchern, für Wardriving, Netzwerkanalyse und Datenschutz.

**Vorinstallierte Geräte:** Dieser Artikel wird von **STS Collective** gesponsert. Dort gibt es Orbic-RCL400-Hotspots mit vorinstalliertem RayHunter und DagShell, einsatzbereit: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Exklusiver Leserrabatt:** Spare bis zu 20 % auf STS-Collective-Produkte, einschließlich vorinstallierter Orbic-RCL400-Geräte. Verwende beim Bezahlen den Code **SIMEONONSECURITY** oder [kaufe mit angewendetem Rabatt](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Was ist DagShell?

### Überblick

**DagShell** ist eine Open-Source-Custom-Firmware, die die serienmäßige Weboberfläche des Orbic RCL400 durch ein **umfassendes Sicherheits-Toolkit** ersetzt. Es enthält:

- **Terminalartige Oberfläche** mit ASCII-Grafik und Hacker-Optik
- **TLS-1.2+-verschlüsselte Weboberfläche** mit selbstsigniertem Zertifikat
- **Datenschutzwerkzeuge** wie TTL-Maskierung, MAC-Spoofing und DNS-basiertes Werbeblocking
- **Netzwerküberwachung** aktiver Verbindungen, Routingtabellen und DNS-Abfragen
- **Hacker-Tools** zur IMSI-Catcher-Erkennung, Portscans und ARP-Erkennung
- **Angriffsmöglichkeiten** wie Evil-Twin-AP, Captive-Portal-Phishing und Deauth-Angriffe
- **GPS-Ortung und Wardriving** mit Wigle-kompatiblem CSV-Export
- **Raspberry-Pi-Begleiter** für GPS, Bluetooth-Scanning und WLAN-Erkundung
- **Dateisystemzugriff** über einen Dateimanager im Browser
- **SMS-Funktion** über AT-Befehle
- **Persistenz**, DagShell startet beim Booten automatisch

### Technische Daten

**Plattform:** Mobiler Hotspot Orbic RCL400\
**Architektur:** ARM Linux (Kernel 3.18)\
**Sprache:** C/C++ (statische ARM-Binärdatei)\
**Verschlüsselung:** TLS 1.2+ mit selbstsignierten Zertifikaten (zweistufige PKI)\
**Webserver:** Benutzerdefinierter eingebetteter HTTPS-Server (Port 8443)\
**Oberfläche:** Browserbasierte Terminaloberfläche\
**Lizenz:** MIT (Open Source)\
**GitHub:** [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Visuelles Design

DagShell verwendet eine **retroartige Hacker-Optik**:
- **ASCII-Logo** auf jeder Seite
- **Grüne Schrift auf schwarzem Hintergrund**, im Matrix-Stil
- **Monospace-Schrift** (Fira Code)
- **Scanline-Effekte** und leuchtender Text
- **Terminal-inspiriertes Layout**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="DagShell-Custom-Firmware auf dem Orbic RCL400 mit grüner Terminaloberfläche, ASCII-Grafik und Sicherheitswerkzeugmenü" >}}

______

## Vollständiger Funktionsüberblick

### 🏠 Übersicht

**Systemübersicht:**
- **Betriebszeit**, wie lange das Gerät läuft
- **AT-Befehlsschnittstelle** zur direkten Modemsteuerung für erfahrene Nutzer
- **Schnellstatus** mit IP-Adresse und Verbindungsstatus

**AT-Befehle** ermöglichen eine direkte Modemsteuerung auf niedriger Ebene:
```
Example AT Commands:
AT+CSQ       - Signal quality
AT+COPS?     - Current network operator  
AT+CREG?     - Network registration status
AT+CIMI      - Get IMSI (subscriber identity)
AT+CGSN      - Get IMEI (device identifier)
```

### 🌐 Netzwerkwerkzeuge

**Aktuelle Netzwerkinformationen:**
- **IP-Adresse und Schnittstelle**
- **Subnetzmaske, Gateway** und Broadcast-Adresse
- **Netzwerkstatistiken** zu gesendeten und empfangenen Paketen

**Routingtabellen-Ansicht:**
- Alle Netzwerkrouten anzeigen
- Informationen zum Standard-Gateway
- Zuordnung der Schnittstellen

**Monitor aktiver Verbindungen:**
- Echtzeitliste **aller TCP/UDP-Verbindungen**
- Lokale und entfernte IP-Adressen
- Portnummern und Verbindungsstatus
- Hilfreich zur **Überwachung der Gerätekommunikation**
+
### 🔒 Datenschutzwerkzeuge

#### TTL-Korrektur

**Zweck:** Hotspotverkehr vor der Erkennung durch den Mobilfunkanbieter maskieren

**Funktionsweise:**
- Setzt den **Time To Live (TTL)** in IP-Paketen auf **65**
- Anbieter erkennen Tethering über TTL-Abnahmen: Telefon=64, verbundenes Gerät=63
- Mit TTL 65 wirkt **der gesamte Datenverkehr lokal**

**Anwendungsfall:** Tethering-Beschränkungen oder Drosselungen des Anbieters umgehen

**Befehle:**
```bash
# Enable TTL fix
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Disable TTL fix  
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### MAC-Adresse fälschen

**Zweck:** MAC-Adresse des Geräts zum Schutz der Privatsphäre randomisieren

**Funktionsweise:**
- Ändert die MAC-Adresse von **wlan0**, der WLAN-Schnittstelle
- Erzeugt eine **zufällige MAC-Adresse** oder erlaubt eine eigene Eingabe
- Erschwert das **geräteübergreifende Tracking** zwischen Sitzungen

**Anwendungsfall:** MAC-basiertes Tracking durch verbundene Netzwerke verhindern

**Ablauf:**
1. Die Schnittstelle wird deaktiviert
2. Die neue MAC-Adresse wird gesetzt
3. Die Schnittstelle wird wieder aktiviert
4. Die Verbindung wird neu aufgebaut

#### DNS-basiertes Werbeblocking

**Zweck:** Werbung und Tracking auf DNS-Ebene blockieren

**Funktionsweise:**
- Ergänzt die **Blockliste** in der Datei `/etc/hosts`
- Listendomains werden auf **127.0.0.1** (localhost) aufgelöst
- Blockiert Werbung **für alle verbundenen Geräte**

**Anwendungsfall:** Werbung im gesamten Netzwerk ohne Gerätekonfiguration blockieren

**Quelle der Blockliste:** Gängige Werbe- und Trackingdomains, anpassbar

### 📱 SMS-Verwaltung

**SMS senden:**
- Sendet Textnachrichten per **AT-Befehl** an das Modem
- Nützlich für **Fernbenachrichtigungen** und Tests

**Nachrichten ansehen:**
- Link zum nativen Orbic-Posteingang
- Empfangene SMS lesen

**Verwendeter AT-Befehl:**
```
AT+CMGS="PHONE_NUMBER"
Message text here^Z
```

### 🔧 Hacker-Tools

#### IMSI-Catcher-Erkennung

**Zweck:** Mobilfunkmastinformationen auf Anomalien prüfen, die auf **IMSI-Catcher/Stingray-Geräte** hinweisen

**Funktionsweise:**
- Ruft **Mobilfunkmastdaten** vom Modem ab:
  - **Cell ID**, Kennung des Masts
  - **LAC**, Location Area Code
  - **MCC/MNC**, Länder- und Mobilfunknetzcode
  - **Signalstärke** (RSSI)
  - **Netzgeneration** (2G/3G/4G)
- **Protokolliert Änderungen**, um verdächtige Mastwechsel zu erkennen
- **Erstellt einen Ausgangswert** mit den normalen Masten in der Umgebung

**Erkennungsmerkmale:**
- **Plötzlicher Wechsel des Mobilfunkmasts**, obwohl das Gerät stillsteht
- **Wechsel zu 2G** *(IMSI-Catcher erzwingen häufig 2G, um Verschlüsselung zu entfernen)*
- Auftauchen einer **unbekannten Cell ID**
- **Schwaches Signal** eines gefälschten Masts
- **Häufige Neuverbindungen**

**Zusammenspiel mit RayHunter:** DagShell **überwacht Mobilfunkmasten**, RayHunter bietet eine **spezialisierte IMSI-Catcher-Erkennung** mit umfassenderer Analyse. Details stehen weiter unten.

#### Portscanner

**Zweck:** Ziel-IP-Adressen auf offene Ports prüfen

**Funktionsweise:**
- **TCP-SYN-Scan** sendet SYN-Pakete an Zielports
- **Timeout-Erkennung** bestimmt, ob Ports offen, geschlossen oder gefiltert sind
- **Bereichsunterstützung** für einzelne Ports oder Portbereiche

**Anwendungsfälle:**
- **Netzwerkerkundung**
- **IoT-Geräteerkennung**
- **Sicherheitsaudits** lokaler Netzwerke
- **Diensterkennung**

**Befehl:**
```bash
# Scan ports 1-1000 on target
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Firewall-Verwaltung

**Zweck:** IP-Adressen mit iptables blockieren oder freigeben

**Funktionsweise:**
- **iptables-Regeln** verwerfen Pakete von oder zu angegebenen IP-Adressen
- **Persistente Regeln** überstehen Neustarts, wenn sie gespeichert wurden
- Funktionen für **Positiv- und Negativlisten**

**Anwendungsfälle:**
- **Schädliche IP-Adressen blockieren**
- **Unbefugten Zugriff verhindern**
- **Datenverkehr formen oder filtern**
- **Kindersicherung**

**Befehle:**
```bash
# Block IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Unblock IP
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Angriffswerkzeuge

**WICHTIGER RECHTLICHER HINWEIS:** Diese Werkzeuge dienen **AUSSCHLIESSLICH autorisierten Sicherheitstests**. Ihre Verwendung gegen Netzwerke, die dir nicht gehören oder für die du keine ausdrückliche schriftliche Genehmigung hast, ist in den meisten Rechtsordnungen **ILLEGAL**, etwa nach dem Computer Fraud and Abuse Act in den USA oder dem Computer Misuse Act im Vereinigten Königreich. Nutze sie nur in **eigenen Netzwerken** oder **kontrollierten Laborumgebungen**.

#### DNS-Sniffer

**Zweck:** DNS-Abfragen verbundener Clients protokollieren

**Funktionsweise:**
- **iptables-Protokollierung** an Port 53 (DNS)
- **Kein Promiscuous-Modus erforderlich**
- Protokolliert alle DNS-Anfragen der Hotspot-Clients
- Zeigt, **welche Websites und Dienste** Clients aufrufen

**Anwendungsfälle** (autorisiert):
- **Netzwerkverkehr analysieren**
- **Elterliche Überwachung** im eigenen Haushalt
- **Sicherheitsforschung** an eigenen Geräten
- **Malwareverhalten untersuchen**

*Das Werkzeug erfasst Metadaten, also besuchte Domains, verbundener Clients. Nutze es nur in Netzwerken, die dir gehören oder die du verwaltest.*

#### ARP-Scanner

**Zweck:** Geräte im lokalen Netzwerk finden

**Funktionsweise:**
- Sendet **ARP-Anfragen** an alle IP-Adressen im Subnetz
- Geräte antworten mit ihren **MAC-Adressen**
- **OUI-Abfrage** ermittelt den Hersteller, etwa Apple oder Samsung
- Erstellt eine **Netzwerkkarte aktiver Geräte**

**Anwendungsfälle:**
- **Netzwerkinventar**
- **Unbekannte Geräte erkennen**
- **BYOD-Netzwerke analysieren**
- **IoT-Geräte finden**

**Beispielausgabe:**
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Zweck:** Netzwerkpfad zum Ziel anzeigen

**Funktionsweise:**
- Sendet Pakete mit **steigendem TTL**
- Jeder Hop verringert den TTL-Wert und antwortet mit **ICMP Time Exceeded**
- Zeigt **Router und Pfad** zum Ziel
- Misst die **Round-Trip-Zeit (RTT)** pro Hop

**Anwendungsfälle:**
- **Netzwerkprobleme beheben**
- **Routen analysieren**
- **Latenzdiagnose**
- **Peering zwischen Internetanbietern untersuchen**

#### Evil-Twin-AP

**Zweck:** Gefälschten WLAN-Zugangspunkt erstellen, der vorhandene SSIDs kopiert

**Funktionsweise:**
- Nutzt **wlan1**, die zweite WLAN-Schnittstelle, wenn sie über das Pi-Begleitgerät verfügbar ist
- Kopiert **SSID und Verschlüsselungstyp** des Zielnetzwerks
- **Fängt Clients ab**, die eine Verbindung herstellen wollen
- Zeigt ein **Captive Portal** zur Erfassung von Zugangsdaten

**Angriffsszenario** (Labor):
1. Suche nach legitimen WLAN-Netzwerken
2. Erstelle einen **gefälschten AP** mit derselben SSID
3. Nutze einen **Deauth-Angriff**, um Clients vom echten AP zu trennen
4. Clients verbinden sich automatisch erneut mit dem **gefälschten AP**
5. Das Captive Portal erfasst Zugangsdaten

*Erkennung: Clients sehen **doppelte SSIDs**, wenn beide APs gleichzeitig sichtbar sind.*

#### Captive Portal

**Zweck:** Phishing-Seitenvorlagen zur Erfassung von Zugangsdaten

**Enthaltene Vorlagen:**
- **WLAN-Anmeldeseite** im Stil von ISP oder Hotel
- **Social-Media-Anmeldeseiten**, Nachbildungen von Facebook, Twitter und Instagram
- **Unternehmensportale**
- **WLAN-Anmeldeseiten** von Flughäfen und Cafés

**Funktionsweise:**
1. Der Evil-Twin-AP leitet **den gesamten Datenverkehr** zum Portal um
2. Der Client sieht die **Anmeldeseite**
3. Der Client gibt Zugangsdaten ein
4. Die Zugangsdaten werden **in einer Datei protokolliert**
5. Der Client erhält Internetzugang oder sieht eine Fehlermeldung

**Lernziel:** Risiken von **Social Engineering** zeigen und erklären, warum Nutzer URLs prüfen sollten

### 📍 GPS-Tracker und Wardriving

#### GPS-Funktionen

**GPS-Quelle:** ausschließlich das **Raspberry-Pi-Begleitgerät**
- *Der Orbic RCL400 hat **kein integriertes GPS**. Ohne Pi-Begleitgerät werden keine Standortdaten erfasst.*
- Das Pi verbindet einen **USB-GPS-Empfänger** mit U-Blox-7-Chipsatz
- Das Pi sendet Koordinaten über **gemeinsam genutzte Dateien** an Orbic
- Die Umrechnung von **ECEF zu Breiten- und Längengrad** erfolgt automatisch

**Dashboard-Anzeige:**
- **Breiten- und Längengrad** in Dezimalgrad
- **Höhe** über dem Meeresspiegel
- **GPS-Fix-Status** und Genauigkeit
- **Automatische Aktualisierung** alle 5 Sekunden
- **Keine Browser-Geolokalisierungsabfrage**, die Browser-API wird nicht verwendet

**Gemeinsamer GPS-Status:**
- GPS-Daten stehen **allen DagShell-Prozessen** zur Verfügung
- Wardriving nutzt GPS automatisch
- Funktionen kommen sich nicht in die Quere

#### Wardriving-Modus

**Zweck:** WLAN-Netzwerke mit GPS-Koordinaten zur Kartierung scannen

**Funktionsweise:**
1. Wartet auf einen **gültigen GPS-Fix** und protokolliert keine Koordinaten 0,0
2. Scannt WLAN-Netzwerke fortlaufend alle **5 Sekunden**
3. Protokolliert Netzwerkdaten:
   - **SSID**, Netzwerkname
   - **BSSID**, MAC-Adresse
   - **Verschlüsselungstyp**, WPA2, WPA3 oder offen
   - **Signalstärke**, RSSI in dBm
   - **Kanalnummer**
   - **GPS-Koordinaten**, Breiten- und Längengrad
   - **Zeitstempel**
4. Exportiert im **Wigle-kompatiblen CSV-Format**

**Wigle-Integration:**
- **WiGLE** (wigle.net) ist ein weltweites WLAN-Kartierungsprojekt
- DagShell-CSV-Dateien lassen sich **direkt zu WiGLE hochladen**
- **Browserbasierter Upload** über die Dateiseite, ohne externe Werkzeuge
- Trägt zur **öffentlichen Datenbank** von WLAN-Standorten bei

**Anwendungsfälle:**
- **WLAN-Abdeckung kartieren**
- **Netzwerkerhebungen** für Internetanbieter
- **Signalstärke analysieren**
- **Sicherheitsforschung** zu offenen Netzwerken und schwacher Verschlüsselung
- **Standortbezogene Analysen**

**Beispiel für das CSV-Format:**
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="DagShell-Wardriving zeigt GPS-Koordinaten und gescannte WLAN-Netzwerke mit SSID, BSSID, Verschlüsselung und Signalstärke in einer Wigle-kompatiblen CSV-Datei." >}}

### 🥧 Raspberry-Pi-Begleitgerät

Das **Raspberry-Pi-Begleitgerät** erweitert DagShell mit **externer Hardware**:

#### Hardwareanforderungen
+**Minimum:**
- **Raspberry Pi 3B+** oder neuer. *(Pi Zero liefert über USB zu wenig Strom für Peripheriegeräte.)*
- **USB-GPS-Empfänger**, U-Blox-7-Chipsatz empfohlen
- **Netzteil**, *das Pi braucht eine eigene Stromversorgung. Der Orbic-USB-Anschluss reicht nicht aus.*

**Optional:**
- **WLAN-Adapter**, zweite Schnittstelle zum Scannen bei aktiver Verbindung
- **Bluetooth-Adapter**, falls das interne Bluetooth des Pi schwach ist

#### GPS-Modul (U-Blox 7)

**Verbindung:** USB-GPS-Empfänger am Pi\
**Protokoll:** NMEA-Sätze über serielle Verbindung\
**Umrechnung:** Das Pi rechnet ECEF automatisch in Breiten- und Längengrad um\
**Datenaustausch:** GPS-Koordinaten werden in eine **gemeinsam genutzte Datei** auf dem Orbic geschrieben

**NMEA-Satz analysieren:**
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Time    Latitude   Longitude   Fix Sats  Altitude
```

#### Bluetooth-Scanning (BLE)

**Zweck:** Bluetooth-Geräte in der Nähe erkennen

**Funktionsweise:**
- Sucht nach **BLE-Ankündigungen**
- Erfasst **MAC-Adressen**
- **OUI-Abfrage** zur Herstellererkennung
- Protokolliert Daten im **CSV-Format**

**Fernsteuerung:**
- Scannen über die DagShell-Weboberfläche **starten und stoppen**
- Keine SSH-Verbindung zum Pi nötig
- Statusaktualisierungen in Echtzeit

**Anwendungsfälle:**
- **Geräte verfolgen und zählen**
- **Passantenfrequenz analysieren**
- **Bluetooth-Geräte finden**
- **IoT-Sicherheitsforschung**

**CSV-Ausgabe:**
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### WLAN-Scanning

**Zweck:** Das Pi scannt WLAN-Netzwerke und sendet die Daten an Orbic

**Vorteil:** Eigene Schnittstelle zum Scannen, während **Orbic den Hotspot aufrechterhält**

**Funktionsweise:**
- Das Pi nutzt einen **zweiten WLAN-Adapter** oder das integrierte WLAN, sofern es nicht für die Verbindung gebraucht wird
- Scannt **alle Kanäle**: 1–14 bei 2,4 GHz und, falls unterstützt, 36–165 bei 5 GHz
- Sendet Ergebnisse über gemeinsamen Speicher an Orbic
- DagShell schreibt sie in die **Wardriver-CSV-Datei**

**Koordination:**
- Pi und Orbic **synchronisieren GPS-Zeitstempel**
- Verhindert doppelte Einträge
- Kombiniert **beide Scanquellen** in einem Protokoll

#### Deauth-Angriffe

**Zweck:** Clients für Labortests von WLAN-Netzwerken trennen

**Funktionsweise:**
- Sendet **802.11-Deauthentifizierungsframes**
- Täuscht die **MAC-Adresse des AP** vor
- Der Client erhält vom AP eine Trennungsnachricht
- Der Client **verliert die Verbindung** und versucht, sie wiederherzustellen

**Steuerungsmethoden:**
- **Einmaliger Deauth:** einzelne Folge von Frames
- **Dauerhafter Deauth:** verhindert erneute Verbindungen und verursacht DoS
- **Fernsteuerung:** Start über die DagShell-Scanseite

**Anwendungsfälle** (autorisiert):
- **Unbefugte Geräte** aus dem eigenen Netzwerk entfernen
- Autorisierte **Penetrationstests**
- **Evil-Twin-Angriffe** im Labor, um Clients zu einem gefälschten AP zu bewegen

**⚠️ Rechtlicher Hinweis:** Deauth-Angriffe sind **gegen fremde Netzwerke illegal**. Es drohen FCC-Verstöße und Anklagen nach dem CFAA.

#### Autostart-Dienst

**systemd-Dienst:** Das Pi-Begleitgerät startet beim Booten automatisch

**Dienstdatei** (`/etc/systemd/system/pi-companion.service`):
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**Befehle:**
```bash
# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

#### OUI-Datenbank

**Zweck:** Hersteller anhand der MAC-Adresse ermitteln

**Datenbank:** Präfixbasierte API der [OUI Master Database](https://standards.ieee.org/products-programs/regauth/)

**Funktionsweise:**
- Extrahiert die **ersten 3 Byte** der MAC-Adresse, das OUI-Präfix
- Fragt die API ab: `api.example.com/oui/A4:83:E7`
- Gibt den **Herstellernamen** zurück

**Beispiel:**
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Integration:** ARP-Scanner, BLE-Scanner und WLAN-Wardriving verwenden die Datenbank

### 📁 Dateimanager

**Zweck:** Dateien auf dem Gerät durchsuchen und verwalten

**Speicherort:** Verzeichnis `/data/`, beschreibbare Partition

**Funktionen:**
- **Dateien und Unterverzeichnisse durchsuchen**
- Dateien auf den Computer **herunterladen**
- Dateien nach Bestätigung **löschen**
- **Dateigrößen** und Zeitstempel anzeigen

**Häufige Dateien:**
- `wardrive_log.csv`: WLAN-Scandaten
- `bluetooth_scan.csv`: BLE-Gerätedaten
- `gps_track.gpx`: GPS-Routen
- `dns_queries.log`: erfasste DNS-Abfragen
- `arp_scan.txt`: Liste der Netzwerkgeräte

**Wigle-Upload:**
- **Direkter Browser-Upload** über die Dateiseite
- Anmeldung beim WiGLE-Konto
- CSV ohne vorherigen Download hochladen

______

{{< stscollective-ad "rayhunter" >}}
+
## Installationsanleitung

### Voraussetzungen

**Hardware:**
- **Mobiler Hotspot Orbic RCL400**
- **Computer** mit Windows, macOS oder Linux
- **USB-Kabel**, wenn die Firmware direkt aufgespielt wird

**Software:**
- **Python 3** mit den Modulen `requests` und `cryptography`
- **Webbrowser**, Chrome, Firefox, Edge oder Safari

**Optional:**
- **Raspberry Pi 3B+** oder neuer für GPS und erweiterte Funktionen
- **USB-GPS-Empfänger** mit U-Blox-7-Chipsatz

### Methode 1: Webflasher (empfohlen)

**Einfachste Methode**, keine Kommandozeile erforderlich.

**Schritt 1:** DagShell-Webflasher aufrufen.
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Schritt 2:** PKI-Zertifikate erstellen.
- Auf **„Generate Certificates“** klicken
- Der Browser erstellt eine **zweistufige PKI**, Root-CA und Serverzertifikat
- **Dateien herunterladen:** `root.der` und `server.der`

**Schritt 3:** Root-Shell auf Orbic aktivieren.
- Mit dem Orbic-WLAN verbinden
- Das **Administratorkennwort** im Webformular eingeben
- Auf **„Enable Shell“** klicken
- Die Seite nutzt die Orbic-API, um eine **Root-Shell auf Port 24** zu öffnen

**Schritt 4:** Firmware installieren.
- Auf **„Deploy DagShell“** klicken
- Das Skript lädt folgende Dateien hoch:
  - `orbic_app`, die Hauptbinärdatei der Firmware
  - `root.der`, das Root-Zertifikat
  - `server.der`, das TLS-Serverzertifikat
  - `dagshell_boot.sh`, das Persistenzskript
- Die Installation dauert **2–3 Minuten**

**Schritt 5:** Orbic neu starten.
- Gerät aus- und wieder einschalten
- DagShell startet automatisch

**Schritt 6:** DagShell öffnen.
- Im Browser `https://192.168.1.1:8443/` aufrufen
- Die **Sicherheitswarnung** akzeptieren. Das selbstsignierte Zertifikat ist erwartet.
- Falls eine Anmeldung erscheint, die Standardzugangsdaten verwenden

### Methode 2: Manuelle Installation

**Für erfahrene Nutzer**, die den Quellcode selbst bauen möchten.

#### Schritt 1: Abhängigkeiten installieren

**Windows:**
```powershell
# Install Python 3
# Download from python.org

# Install required modules
pip install requests cryptography

# ARM cross-compiler included in gcc_win/ folder
```

**macOS:**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3

# Install required modules
pip3 install requests cryptography

# ARM toolchain included in gcc_mac/ folder
```

**Linux:**
```bash
# Install Python 3 and pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Install required modules
pip3 install requests cryptography

# Install ARM cross-compiler
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Schritt 2: Repository klonen

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Schritt 3: Firmware bauen

**Windows:**
```powershell
cd orbic_fw_c
python gen_pki.py          # Generate certificates
.\build.ps1                # Compile firmware
```

**macOS/Linux:**
```bash
cd orbic_fw_c
python3 gen_pki.py         # Generate certificates
./build.sh                 # Compile firmware (auto-builds BearSSL)
```

**Ausgabe:** `orbic_app`, eine statische ARM-Binärdatei, sowie DER-Zertifikatsdateien.

**⚠️ Hinweis für macOS:** Der Ordner `gcc_mac/` enthält eine mit **crosstool-ng** erstellte ARM-Toolchain. Sie nutzt Header des **Linux-3.2-Kernels**, um mit dem Orbic-Kernel 3.18 kompatibel zu sein. *Standardmäßige ARM-Compiler aus Homebrew zielen auf neuere Kernel ab und **funktionieren nicht**.*

#### Schritt 4: Root-Shell auf Orbic aktivieren

```bash
# Connect to Orbic WiFi
# Replace YOUR_ADMIN_PASSWORD with actual password

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Das Skript nutzt die Orbic-Web-API, um eine Root-Shell auf **Port 24** zu öffnen.

#### Schritt 5: Firmware installieren

```bash
python deploy_base64.py
```

Das Skript lädt folgende Dateien hoch und installiert sie:
- `orbic_app` unter `/data/orbic_app`
- Zertifikate unter `/data/root.der` und `/data/server.der`
- Startskript unter `/etc/rc.d/dagshell_boot.sh`

**Persistenz:** Ein init-Skript startet die Firmware nach jedem Neustart automatisch.

#### Schritt 6: Neustarten und zugreifen

```bash
# Reboot Orbic (power cycle or via SSH)
reboot

# After reboot, access DagShell
# Browser: https://192.168.1.1:8443/
```

### Sicherheitswarnung zum Zertifikat

Beim Öffnen von DagShell erscheint die Warnung **„Not Secure“** oder **„Not Trusted“**.

**Desktopbrowser:**
- Auf **„Advanced“** klicken
- **„Proceed to 192.168.1.1 (unsafe)“** auswählen

**Mobile Browser:**
- Auf **„Show Details“** tippen
- **„visit this website“** antippen

**Grund:**
- Das Zertifikat ist **selbstsigniert**, nicht von einer vertrauenswürdigen CA wie Let's Encrypt
- Das Gerät hat das Root-Zertifikat nicht im Vertrauensspeicher
- *Das ist bei Custom-Firmware **erwartet** und kein Anzeichen für eine Kompromittierung*

**Ist die Verbindung sicher?**
- **Ja.** Die Verbindung ist mit **TLS 1.2+** verschlüsselt.
- Daten lassen sich nicht abfangen.
- *Das Zertifikat ist nicht über eine öffentliche CA vertrauenswürdig verkettet, aber die Verschlüsselung funktioniert.*

**Optional:** `root.der` im Vertrauensspeicher des Geräts installieren, um die Warnung zu entfernen.

______

## Raspberry-Pi-Begleitgerät einrichten

**Optional, aber für den vollen Funktionsumfang sehr empfohlen**

### Hardware einrichten

**Schritt 1:** Komponenten besorgen.
- **Raspberry Pi 3B+** oder neuer (35–55 USD)
- **USB-GPS-Empfänger** mit U-Blox-7-Chipsatz (15–30 USD)
- **microSD-Karte** mit mindestens 16 GB für Pi OS (10 USD)
- **Netzteil** für das Pi (10 USD)

**Schritt 2:** Raspberry Pi OS installieren.
```bash
# Download Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# Flash "Raspberry Pi OS Lite" to SD card
# Boot Pi and complete setup
```

**Schritt 3:** GPS-Empfänger verbinden.
- USB-GPS am Pi anschließen
- Erkennung prüfen: `lsusb`, das GPS-Gerät sollte erscheinen
- Seriellen Port prüfen: `ls /dev/ttyUSB*` oder `/dev/ttyACM*`

### Software installieren

**Schritt 1:** DagShell-Repository auf dem Pi klonen.

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Schritt 2:** Abhängigkeiten installieren.

```bash
# Update package list
sudo apt-get update

# Install required packages
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Install Python modules
pip3 install pyserial gps3 bluetooth pybluez
```

**Schritt 3:** GPS-Dienst konfigurieren.

```bash
# Edit gpsd config
sudo nano /etc/default/gpsd

# Set DEVICES line to your GPS serial port
DEVICES="/dev/ttyUSB0"  # Adjust if different

# Restart gpsd
sudo systemctl restart gpsd

# Test GPS
cgps -s  # Should show satellite data after ~30 seconds
```

**Schritt 4:** Pi-Begleitgerät konfigurieren.

```bash
# Edit configuration file
nano pi_companion/config.py

# Set Orbic IP address
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# Set GPS serial port
GPS_DEVICE = "/dev/ttyUSB0"

# Save and exit
```

**Schritt 5:** systemd-Dienst installieren.

```bash
# Copy service file
sudo cp pi_companion.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

**Schritt 6:** Kommunikation prüfen.

```bash
# Check logs
journalctl -u pi-companion -f

# Should see GPS coordinates being sent to Orbic
```

### Netzwerkeinrichtung

**Option A:** WLAN-Verbindung

```bash
# Pi connects to Orbic hotspot
# Edit wpa_supplicant config
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Add network
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# Restart WiFi
sudo systemctl restart networking
```

**Option B:** USB-Ethernet (empfohlen)

- Pi per **USB-Kabel** mit Orbic verbinden, Pi-USB-Port an Orbic-USB-Port
- **USB-Gadget-Modus** auf dem Pi aktivieren
- Pi arbeitet als **USB-Ethernet-Gerät**
- *Zuverlässiger als WLAN bei kontinuierlicher Datenübertragung*
- Das Pi greift über Orbic auf das Internet zu

**USB-Gadget-Konfiguration:**
```bash
# Edit config.txt
sudo nano /boot/config.txt

# Add at end
dtoverlay=dwc2

# Edit cmdline.txt
sudo nano /boot/cmdline.txt

# Add after rootwait
modules-load=dwc2,g_ether

# Reboot
sudo reboot
```

______

## Warum DagShell mit RayHunter kombinieren?
+
{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Vergleichsdiagramm der WLAN-Wardriving- und Netzwerkangriffswerkzeuge von DagShell mit RayHunters Erkennung von Anomalien in Mobilfunkprotokollen. Beide laufen auf demselben Orbic-RCL400-Hotspot." >}}

### Ergänzende Funktionen

**DagShell** und **RayHunter** sind **sinnvolle Ergänzungen** für unterschiedliche Bereiche der mobilen Sicherheitsforschung:

| Funktion | DagShell | RayHunter |
|---------|----------|-----------|
| **IMSI-Catcher-Erkennung** | Einfache Mobilfunkmastüberwachung | Erweiterte Musteranalyse |
| **GPS-Ortung** | Ja, über Pi | Ja, über Modem |
| **WLAN-Wardriving** | Ja | Nein |
| **Bluetooth-Scanning** | Ja, über Pi | Nein |
| **Netzwerkwerkzeuge** | Ja, DNS-Sniffer, ARP-Scan und Portscan | Nein |
| **Angriffswerkzeuge** | Ja, Evil Twin, Captive Portal, Deauth | Nein |
| **Datenschutzwerkzeuge** | Ja, TTL-Korrektur, MAC-Spoofing, Werbeblockierung | Wenige |
| **Mobilfunkmast-Datenbank** | Einfach | Umfassend |
| **KI/ML-Analyse** | Nein | Ja, Anomalieerkennung |
| **Mobilfunkprotokollanalyse** | Eingeschränkt | Detailliert, SS7/Diameter |

### Zusammenspiel in der Praxis

#### 1. **Vollständiger Schutz vor IMSI-Catchern**

**Szenario:** Reise in ein Gebiet mit verstärkter Überwachung

**DagShell-Beitrag:**
- **Mobilfunkmastwechsel in Echtzeit überwachen**
- **GPS-Standort** bei verdächtigen Wechseln erfassen
- **Mastdaten zur späteren Analyse protokollieren**

**RayHunter-Beitrag:**
- **ML-basierte Anomalieerkennung** in Mobilfunkprotokollen
- **SS7/Diameter-Pakete untersuchen**, um ausgefeilte Angriffe zu erkennen
- **Datenbank bekannter vertrauenswürdiger Masten** zum Vergleich

**Gemeinsamer Nutzen:** DagShell übernimmt die **laufende Überwachung**, RayHunter die **detaillierte Analyse**.

#### 2. **Wardriving mit Sicherheitsüberwachung**

**Szenario:** WLAN-Netzwerke in einer Stadt kartieren

**DagShell-Beitrag:**
- **WLAN-Scanning** mit GPS-Koordinaten
- **Netzwerkanalyse** von Signalstärke und Verschlüsselung
- **Wigle-CSV-Export** zur Kartierung

**RayHunter-Beitrag:**
- **Mobilfunkmasten beim Wardriving verfolgen**
- **IMSI-Catcher während der WLAN-Scans erkennen**
- **Bei beeinträchtigter Mobilfunksicherheit warnen**

**Gemeinsamer Nutzen:** Wardriving mit **Mobilfunksicherheitsbewusstsein**.

#### 3. **Sicherheitsforschungslabor**

**Szenario:** Red-Team-Übung oder Penetrationstest

**DagShell-Beitrag:**
- **Evil-Twin-AP** für WLAN-Tests
- **Captive Portal** für Social-Engineering-Demonstrationen
- **Deauth-Angriffe** für Belastungstests
- Werkzeuge zur **Netzwerkerkundung**

**RayHunter-Beitrag:**
- **Erkennt Überwachung** während der Tests
- Verbessert das Bewusstsein für **Mobilfunkmast-Sicherheit**
- **Begrenzt Gegenüberwachung** während der Tests

**Gemeinsamer Nutzen:** Offensive Werkzeuge mit **defensivem Bewusstsein**.

#### 4. **Datenschutzorientiertes Reisen**

**Szenario:** Journalist oder Aktivist in einer sensiblen Umgebung

**DagShell-Beitrag:**
- **TTL-Maskierung**, um Tethering zu verbergen
- **MAC-Spoofing** für Anonymität
- **Werbeblockierung** gegen Tracking
- **IMSI-Catcher-Überwachung**

**RayHunter-Beitrag:**
- **Erweiterte IMSI-Catcher-Erkennung**
- Erkennung von Angriffen **auf Protokollebene**
- **Mobilfunksicherheitswarnungen**

**Gemeinsamer Nutzen:** Mehr Privatsphäre durch **mehrschichtigen Schutz**.

### Gemeinsame Installation

**Vorinstallierte Option** (am einfachsten):
- Kauf bei **STS Collective**: [Vorinstallierter Orbic RCL400 mit RayHunter und DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **Sofort einsatzbereit**
- Beide Firmware-Versionen sind **getestet und geprüft**
- **Keine Installationsarbeit**

**Selbstinstallation:**
1. Zuerst **RayHunter installieren**, siehe [Anleitung zum Flashen von RayHunter-Geräten](/articles/how-to-flash-rayhunter-devices-complete-guide/)
2. Danach **DagShell installieren**, beide können zusammenarbeiten
3. **RayHunter** nutzt die Standardports
4. **DagShell** läuft auf Port 8443
5. Beide in unterschiedlichen Browser-Tabs öffnen

**Keine Konflikte:**
- RayHunter nutzt die Ports **80/443**
- DagShell nutzt Port **8443**
- Sie stören sich nicht
- Sie laufen **gleichzeitig**

Keine Selbstinstallation? Der **[Orbic RCL400 mit RayHunter und DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** ist vorinstalliert und sofort einsatzbereit. Der Lesercode **SIMEONONSECURITY** spart bis zu 20 % bei STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Vorinstallierten RCL400 kaufen und 20 % sparen
{{< /centerbutton >}}

______

## Praxisbeispiele

### Beispiel 1: Sicherheitsforscher

**Profil:** Penetrationstester bei einer WLAN-Sicherheitsbewertung

**Verwendete DagShell-Werkzeuge:**
- **WLAN-Wardriving**, um Kundennetzwerke zu kartieren
- **ARP-Scanner** zur Geräteerkennung
- **Portscanner** zur Diensterkennung
- **Evil Twin und Captive Portal** zum Testen der Widerstandsfähigkeit gegen Social Engineering
- **Dateimanager** zum Abrufen der Ergebnisse

**Arbeitsablauf:**
1. Den Rand des Kundengeländes abfahren
2. Die WLAN-Abdeckung per Wardriving kartieren
3. Mit Erlaubnis einen Evil Twin des Kundennetzes erstellen
4. Verbindungsversuche der Clients überwachen
5. Bericht mit den gesammelten Daten erstellen

**RayHunter-Integration:** hilft sicherzustellen, dass der Forscher während der Bewertung nicht überwacht wird.

### Beispiel 2: Datenschutzbefürworter

**Profil:** Journalist auf Auslandsreise

**Verwendete DagShell-Werkzeuge:**
- **TTL-Korrektur** zum Umgehen von Anbieterbeschränkungen
- **MAC-Spoofing** für Geräteanonymität
- **IMSI-Catcher-Erkennung** zur Überwachung von Risiken
- **DNS-Sniffer** zur Kontrolle auf Datenlecks
- **Werbeblockierung** gegen Tracking

**Arbeitsablauf:**
1. TTL-Korrektur vor der Nutzung aktivieren
2. MAC-Adresse randomisieren
3. IMSI-Catcher-Erkennung fortlaufend überwachen
4. Werbeblockierung für alle verbundenen Geräte verwenden
5. Verdächtige Mobilfunkaktivität protokollieren

**RayHunter-Integration:** erkennt IMSI-Catcher umfassender als die einfache Überwachung.

### Beispiel 3: Netzwerkadministrator

**Profil:** IT-Administrator mehrerer Standorte

**Verwendete DagShell-Werkzeuge:**
- **WLAN-Wardriving** zur Prüfung der Abdeckung
- **ARP-Scanner** für das Geräteinventar
- **Portscanner** für Sicherheitsaudits
- **Monitor aktiver Verbindungen** für unerlaubten Datenverkehr
- **Firewall-Verwaltung** zum Blockieren von IP-Adressen

**Arbeitsablauf:**
1. WLAN-Abdeckung am Standort per Wardriving prüfen
2. Alle Netzwerkgeräte per ARP-Scan finden
3. Server auf offene Dienste prüfen
4. Schädliche IP-Adressen über die Firewall blockieren
5. Berichte zur Dokumentation exportieren

**RayHunter-Integration:** überwacht Mobilfunksicherheit an Standorten mit mobilen Geräten.

### Beispiel 4: IoT-Sicherheitsforscher

**Profil:** Forscher zur Sicherheit von IoT-Geräten

**Verwendete DagShell-Werkzeuge:**
- **ARP-Scanner mit OUI-Abfrage** zur Erkennung von IoT-Geräten
- **Portscanner** zum Finden offener Dienste
- **DNS-Sniffer** zum Erfassen von IoT-Verkehrsmustern
- **Bluetooth-Scanner** auf dem Pi für BLE-IoT-Geräte
- **Traceroute** zur Verbindungsanalyse

**Arbeitsablauf:**
1. Orbic und Pi in einer Testumgebung einsetzen
2. IoT-Geräte per ARP-Scan entdecken
3. Verwundbare Dienste per Portscan suchen
4. Bluetooth-IoT-Geräte per BLE scannen
5. „Nach Hause telefonierenden“ Datenverkehr mit dem DNS-Sniffer analysieren
6. Schwachstellen dokumentieren

**RayHunter-Integration:** erkennt Mobilfunkverbindungen der IoT-Geräte und überwacht Anomalien.

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Diagramm mit vier realen Einsatzbereichen für DagShell und RayHunter: Sicherheitsforscher, Datenschutzbefürworter, Netzwerkadministrator und IoT-Forscher." >}}

______

## Rechtliche und ethische Aspekte

### Rechtlicher Rahmen

**Werkzeuge wie DagShell bewegen sich in rechtlichen Grauzonen.**

**Zulässige Nutzung:**
✅ **Eigene Netzwerke**, eigene Geräte und Netzwerke testen\
✅ **Autorisierte Tests**, vor Tests an fremden Systemen schriftliche Erlaubnis einholen\
✅ **Bildungszwecke**, in isolierten Laborumgebungen lernen\
✅ **Datenschutz**, TTL-Korrektur und MAC-Spoofing auf dem eigenen Gerät\
✅ **Sicherheitsforschung**, Schwachstellen verantwortungsvoll offenlegen\

**Unzulässige Nutzung:**
❌ **Unbefugter Zugriff**, Angriffe auf fremde Netzwerke können den CFAA verletzen\
❌ **Deauth-Angriffe** gegen fremde Netzwerke, FCC-Verstöße und mögliche Straftaten\
❌ **Evil-Twin-Angriffe** gegen die Öffentlichkeit, Betrug und Identitätsdiebstahl\
❌ **DNS-Sniffing** anderer ohne Einwilligung\
❌ **Sicherheitsmaßnahmen umgehen**, um Betrug zu begehen\

### Zu beachtende Gesetze

**Vereinigte Staaten:**
- **Computer Fraud and Abuse Act (CFAA)**, unbefugter Zugriff auf Computer und Netzwerke
- **Wiretap Act**, Abfangen elektronischer Kommunikation
- **FCC-Regeln**, Funkstörungen, einschließlich Deauth-Angriffen

**Vereinigtes Königreich:**
- **Computer Misuse Act 1990**, ähnlich dem CFAA
- **Regulation of Investigatory Powers Act (RIPA)**, Einschränkungen beim Abfangen

**Europäische Union:**
- **DSGVO**, Datenschutz, einschließlich identifizierbarer BLE- und WLAN-Daten
- *Lokale Vorschriften und deren Durchsetzung unterscheiden sich je nach Land.*

### Ethische Leitlinien

**TUN:**
- ✅ Nur auf **eigenen Geräten und Netzwerken** einsetzen
- ✅ Vor Tests an fremden Systemen **schriftliche Erlaubnis** einholen
- ✅ Schwachstellen **verantwortungsvoll melden**
- ✅ Werkzeuge zu **Bildungszwecken** in kontrollierten Umgebungen einsetzen
- ✅ Die **eigene Privatsphäre** schützen

**NICHT TUN:**
- ❌ Keine fremden Netzwerke angreifen
- ❌ Keine Zugangsdaten von Unbeteiligten sammeln
- ❌ Keine kritische Infrastruktur stören
- ❌ Werkzeuge nicht böswillig einsetzen
- ❌ Keine erfassten Daten verbreiten

### Erklärung zur verantwortungsvollen Nutzung

DagShell ist ein **Werkzeug für Sicherheitsforschung und Datenschutz**. Seine Möglichkeiten ähneln professionellen Penetrationstest-Werkzeugen wie **Kali Linux**, **WiFi Pineapple** oder **HackRF**.

**Die Absicht zählt:** Dieselben Werkzeuge nutzen **böswillige Hacker** und **Sicherheitsexperten**. Der Unterschied liegt in:
- **Autorisierung**, der Erlaubnis zum Testen
- **Absicht**, Sicherheit zu verbessern oder Schaden anzurichten
- **Offenlegung**, Ergebnisse zu melden oder auszunutzen

Nutze DagShell **verantwortungsvoll und ethisch**. *Wenn du nicht sicher bist, ob eine Handlung legal ist, halte an und frage vor dem Fortfahren einen Anwalt.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Rechtliche und ethische Rahmenbedingungen für Sicherheitsforschung mit DagShell, autorisierte und unzulässige Nutzung sowie geltende Gesetze." >}}

______

## Fehlerbehebung





### Installationsprobleme

**Problem**: `enable_shell.py` kann keine Verbindung herstellen

**Lösungen**:
- Prüfe, ob du mit dem **Orbic-WLAN** verbunden bist
- Prüfe die IP-Adresse **192.168.1.1** (Standardwert)
- Gib das Admin-Passwort erneut ein. Groß- und Kleinschreibung beachten.
- Prüfe, ob Port 80 erreichbar ist: `telnet 192.168.1.1 80`

**Problem**: Der Firmware-Upload schlägt fehl

**Lösungen**:
- Aktiviere zuerst die Root-Shell (`enable_shell.py` war erfolgreich)
- Prüfe die Netzwerkstabilität. Verwende nach Möglichkeit eine Kabelverbindung.
- Versuche `deploy_net.py` statt `deploy_base64.py`
- Prüfe, ob auf der `/data`-Partition Speicherplatz frei ist: `df -h /data`

**Problem**: Die Zertifikatswarnung verschwindet nicht

**Lösungen**:
- *Das ist **normal** bei selbstsignierten Zertifikaten. Die Verbindung ist weiterhin verschlüsselt.*
- Klicke jedes Mal auf „Erweitert“ -> „Trotzdem fortfahren“
- **Optional**: Installiere `root.der` im Zertifikatsspeicher des Geräts (für Fortgeschrittene)

### Laufzeitprobleme

**Problem**: DagShell startet beim Booten nicht

**Lösungen**:
- Prüfe das Bootskript: `ls -la /etc/rc.d/dagshell_boot.sh`
- Prüfe, ob es ausführbar ist: `chmod +x /etc/rc.d/dagshell_boot.sh`
- Prüfe die Protokolle: `logread | grep dagshell`
- Starte DagShell manuell: `/data/orbic_app &`

**Problem**: GPS funktioniert nicht

**Lösungen**:
- Prüfe, ob der **Pi-Begleiter** läuft: `systemctl status pi-companion`
- Prüfe, ob GPS Satellitenempfang hat: `cgps -s` (auf dem Pi)
- Prüfe, ob der GPS-Dongle angeschlossen ist: `lsusb`
- *Warte bei einem Kaltstart 5 bis 10 Minuten auf einen GPS-Fix. Beim ersten Start dauert es im Freien länger.*

**Problem**: Wardriving protokolliert keine Daten

**Lösungen**:
- Warte vor dem Start auf einen GPS-Fix
- Prüfe, ob `/data` Schreibrechte hat
- Prüfe, ob die CSV-Datei erstellt wird: `ls -la /data/wardrive_log.csv`
- Prüfe, ob die WLAN-Schnittstelle aktiv ist: `ifconfig wlan0`

**Problem**: Der Pi-Begleiter kommuniziert nicht mit dem Orbic

**Lösungen**:
- Prüfe die Netzwerkverbindung: `ping 192.168.1.1`
- Prüfe, ob die Konfigurationsdatei die richtige IP-Adresse enthält
- Prüfe, ob Port 8443 geöffnet ist: `telnet 192.168.1.1 8443`
- Prüfe die Protokolle des Pi-Begleiters: `journalctl -u pi-companion`

### Leistungsprobleme

**Problem**: Die Weboberfläche reagiert langsam oder verzögert

**Lösungen**:
- Leere den Browser-Cache
- Deaktiviere Browser-Erweiterungen. Werbeblocker können stören.
- Verbinde dich über **Kabel** statt WLAN mit dem Orbic
- Starte DagShell neu: `killall orbic_app && /data/orbic_app &`

**Problem**: Wardriving-Scans dauern zu lange

**Lösungen**:
- Erhöhe in den Einstellungen das Scanintervall. Dadurch sinkt die Scanfrequenz.
- Verringere die Zahl der gescannten Kanäle
- *Ein schwacher GPS-Fix verlangsamt Scans. Das System wartet auf gültige Koordinaten, bevor es Daten protokolliert.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="DagShell-Fehlerbehebung mit häufigen Installations-, GPS- und Wardriving-Problemen und schrittweisen Lösungen" >}}


______

## Erweiterte Konfiguration

### DagShell anpassen

**Quellcode ändern**:
- Bearbeite Dateien im Verzeichnis `orbic_fw_c/`
- Erstelle mit `build.sh` oder `build.ps1` einen neuen Build
- Spiele die Firmware erneut auf

**Eigene Seiten hinzufügen**:
- DagShell verwendet in C++-Code eingebettetes HTML
- Bearbeite `main.cpp`, um neue Routen hinzuzufügen
- Kompiliere und spiele die Firmware auf

**Eigenes Zertifikat**:
- Erstelle mit `gen_pki.py` eine eigene PKI
- Oder erstelle Zertifikate mit **OpenSSL**
- Ersetze `root.der` und `server.der`

### Integration mit anderen Werkzeugen

**Daten nach Wireshark exportieren**:
```bash
# Capture pcap file
tcpdump -i wlan0 -w /data/capture.pcap

# Download via file browser
# Open in Wireshark on PC
```

**GPS-Tracks in QGIS importieren**:
```bash
# Export GPX format
python gps_to_gpx.py /data/gps_coords.txt

# Import to QGIS as vector layer
```

**Mit einer externen Datenbank synchronisieren**:
```python
# Custom script to upload wardrive data to MySQL
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### Leistung optimieren

**Scan-Geschwindigkeit optimieren**:
```bash
# Edit wardrive scan interval
# In DagShell web UI, change from 5s to 3s for faster scanning
# Trade-off: Higher CPU usage, potential missed networks
```

**Akkulaufzeit optimieren** (bei Verwendung eines Akkupacks):
```bash
# Reduce screen brightness on Orbic
# Disable unused features (BT, GPS when not needed)
# Use sleep mode between wardrive sessions
```

______

## Vergleich mit Alternativen

### DagShell und WiFi Pineapple im Vergleich

| Funktion | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **Preis** | 60–80 $ plus Gerät | 99–299 $ |
| **Mobilfunk** | ✅ 4G LTE integriert | ❌ Nur WLAN |
| **GPS** | ✅ Über Pi-Begleiter | ⚠️ Über USB-Dongle |
| **Evil Twin** | ✅ Ja | ✅ Ja |
| **Captive Portal** | ✅ Ja | ✅ Ja |
| **Deauth** | ✅ Ja (über Pi) | ✅ Ja |
| **Wardriving** | ✅ Ja | ✅ Ja |
| **IMSI-Erkennung** | ✅ Einfach | ❌ Nein |
| **Mobilität** | ✅ Sehr mobil | ⚠️ Mittel |
| **Akku** | ✅ Integriert | ⚠️ Extern erforderlich |
| **Einarbeitung** | Mittel | Gering (ausgereifte Oberfläche) |

**Sieger**: DagShell für **mobile Mobilfunksicherheit**, Pineapple für **WLAN-spezifische** Tests mit einfacher Oberfläche

### DagShell und Kali Linux auf dem Pi im Vergleich

| Funktion | DagShell | Kali auf dem Pi |
|---------|----------|-----------|
| **Einrichtungszeit** | 15 Minuten | 2–3 Stunden |
| **LTE-Mobilfunk** | ✅ Integriert | ❌ USB-Modem erforderlich |
| **Weboberfläche** | ✅ Ja | ⚠️ Eingeschränkt (VNC oder SSH erforderlich) |
| **Zahl der Werkzeuge** | ~15 | 600+ |
| **Spezialisierung** | Mobile Sicherheit | Allgemeiner Penetrationstest |
| **Mobilität** | ✅ Passt in die Tasche | ⚠️ Bildschirm und Stromversorgung erforderlich |
| **Akkulaufzeit** | 8–10 Stunden | 2–4 Stunden |

**Sieger**: DagShell für **mobile Spezialaufgaben**, Kali für ein **umfassendes** Werkzeugset

### DagShell und die originale Orbic-Firmware im Vergleich

| Funktion | DagShell | Original-Firmware |
|---------|----------|----------------|
| **Sicherheitswerkzeuge** | ✅ Umfangreich | ❌ Keine |
| **Datenschutzfunktionen** | ✅ Ja | ❌ Minimal |
| **Anpassbarkeit** | ✅ Voll anpassbar | ❌ Gesperrt |
| **Wardriving** | ✅ Ja | ❌ Nein |
| **GPS** | ✅ Ja (über Pi) | ❌ Nein |
| **Open Source** | ✅ Ja | ❌ Proprietär |
| **Support** | ⚠️ Community | ✅ Offiziell |
| **Stabilität** | ⚠️ Beta | ✅ Produktionsreif |

**Sieger**: DagShell für **Forscher**, Original-Firmware für **Gelegenheitsnutzer**

______

## Fazit: Das ultimative mobile Labor

**DagShell** verwandelt den unscheinbaren **Orbic-RCL400-Hotspot** in ein **leistungsfähiges mobiles Sicherheitslabor** mit:

✅ **Datenschutz** (TTL-Anpassung, MAC-Spoofing, Werbeblocker)
✅ **Netzwerküberwachung** (Verbindungen, DNS, Routing)
✅ **Hacking-Werkzeugen** (IMSI-Erkennung, Portscans, ARP-Erkennung)
✅ **Angriffsfunktionen** (Evil Twin, Captive Portal, Deauth)
✅ **GPS-Wardriving** mit Wigle-Integration
✅ **Erweiterung durch Raspberry Pi** (BLE, WLAN, GPS)
✅ **Mobilität und Akkubetrieb**
✅ **Open Source und anpassbar**

### In Kombination mit RayHunter

**RayHunter + DagShell** = **vollständige mobile Sicherheitsplattform**:
- **RayHunter** erkennt IMSI-Catcher umfassender
- **DagShell** bietet offensive Werkzeuge und Datenschutzfunktionen
- Beide laufen **gleichzeitig** auf demselben Gerät
- **Ergänzende Funktionen** ohne Überschneidungen
- **Ein einziges mobiles Paket** für alle Anforderungen an mobile Sicherheit

### Jetzt starten

**Option 1: Mit vorinstallierter Firmware** (am einfachsten)
- **STS Collective**: [Orbic RCL400 mit RayHunter und DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- Wird **einsatzbereit** geliefert
- Keine Installation erforderlich
- Professionell konfiguriert

**Option 2: Selbst installieren**
- Folge dieser Anleitung
- **Kostenlos**, wenn du bereits einen Orbic RCL400 besitzt
- Lerne den Installationsprozess kennen
- Passe das System an deine Anforderungen an

### Weiterführende Lektüre

- **[RayHunter-Geräte flashen: vollständige Anleitung](/articles/how-to-flash-rayhunter-devices-complete-guide/)** - RayHunter zuerst installieren
- **[RayHunter-Gerätevergleich: vollständiger Test](/articles/rayhunter-device-comparison-2026-complete-review/)** - Wähle deine Plattform
- **[Flock-You-Erkennungsprojekt: Anleitung für Hardware zur Gegenüberwachung](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - Weitere Erkennungswerkzeuge

### Abschließende Gedanken

Ob **Sicherheitsforscher**, **Penetrationstester**, **Datenschutzbeauftragter** oder **Netzwerkadministrator**, DagShell bietet eine **mobile, leistungsfähige und erschwingliche** Plattform für mobile Sicherheitsarbeit.

**Haftungsausschluss**: Nutze das System verantwortungsvoll. Teste nur Netzwerke und Geräte, die dir gehören oder für die du eine ausdrückliche schriftliche Erlaubnis hast. Handle legal und ethisch. Viel Erfolg beim Hacken! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Orbic-RCL400-Hotspot mit DagShell-Firmware als vollständiges mobiles Labor für Sicherheitsforschung" >}}


______

## Referenzen

1. [DagShell-GitHub-Repository](https://github.com/dagnazty/DagShell)
2. [DagShell-Dokumentation](https://dagnazty.github.io/DagShell/)
3. [STS Collective - Geräte mit vorinstallierter Firmware](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE - WLAN-Kartierungsprojekt](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Offizielle Raspberry-Pi-Dokumentation](https://www.raspberrypi.org/documentation/)
7. [Dokumentation zum U-Blox-GPS-Modul](https://www.u-blox.com/)
8. [OUI-Datenbank - IEEE-Standards](https://standards.ieee.org/products-programs/regauth/)
9. [iptables-Anleitung](https://www.netfilter.org/documentation/)
10. [OpenSSL-Dokumentation](https://www.openssl.org/docs/)
