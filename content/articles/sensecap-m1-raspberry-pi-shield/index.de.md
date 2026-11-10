---
title: "SenseCAP M1 Raspberry Pi Shield: Pinbelegung und LoRaWAN-Weiterverwendung"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "Lerne den SenseCAP M1 Shield kennen, vergleiche widersprüchliche GPIO-Belegungen, untersuche den ATECC608 und plane ein LoRaWAN-Gateway mit modernem Raspberry Pi OS."
genre: ["Raspberry Pi", "IoT", "Hardwaresicherheit"]
tags: ["SenseCAP M1", "SenseCAP M1 Shield", "SenseCAP M1 Pinbelegung", "Raspberry Pi Shield", "Raspberry Pi HAT", "LoRaWAN-Gateway", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Helium-Hotspot-Weiterverwendung", "LoRa-Konzentrator", "SPI GPIO", "GPIO17", "GPIO22 LED", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "I2C-Diagnose", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "Hardware-Reverse-Engineering"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "SenseCAP M1 Shield mit Seeed-WM1302-Modul, Raspberry-Pi-Header, Antennenkabel, USB-C-Anschluss und Lüfterstecker"
coverCaption: "Board-Foto: Clockwork Bird, 2023. Quelle und Namensnennung stehen weiter unten."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**Der SenseCAP M1 Shield eignet sich als LoRaWAN-Gateway-Hardware, doch seine Verdrahtung erfordert mehr Prüfung als eine allgemeine Raspberry-Pi-HAT-Anleitung.** Dieser Leitfaden erweitert [Clockwork Birds Untersuchung von 2023](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) um Herstellerunterlagen, eine Prüfung des Upstream-Treibers und aktuelle GPIO-Hinweise. Du identifizierst die Hardware, trennst gesicherte Fakten von unvollständigen Pinout-Angaben und erstellst ein wiederholbares Inbetriebnahmeprotokoll.

> **Umfang:** Dies ist ein dokumentationsbasierter Hardwareleitfaden. Befehle und Board-Zuordnungen wurden für diesen Artikel nicht an einem physischen M1 getestet.

## Wichtigste Erkenntnisse

- **Identifiziere beide Boards:** Trägerplatine und entfernbarer Konzentrator haben eigene Modell- und Revisionsangaben.
- **Prüfe Reset-Skripte:** CoreCell-Standardwerte widersprechen Signalen im veröffentlichten M1-Pinout.
- **Prüfe OS-Schnittstellen:** SPI-Gerätedateien, GPIO-Nummerierung und Werkzeugversionen beantworten verschiedene Fragen.
- **Erhalte die Provisionierung des Secure Elements:** Geräteinformationen auszulesen unterscheidet sich vom Konfigurieren oder Erzeugen von Schlüsseln.
- **Belege den vollständigen Pfad:** Ein erkannter Konzentrator beweist keine erfolgreiche Sensordatenübertragung.

## Vor dem Start

**Schwierigkeitsgrad: mittel.** Plane etwa ein bis zwei Stunden für Inventarisierung, OS-Vorbereitung und Dokumentationsprüfungen ein. Elektrische Verifikation, Treiberanpassungen und Serverbereitstellung erfordern zusätzliche Arbeit, besonders bei einer unbekannten Board-Revision.

| Gegenstand | Zweck |
|---|---|
| **M1 Shield und Konzentrator** | Trägerrevision und vollständige Modulbeschriftung ablesen |
| **Raspberry Pi 4** | Mit dem Host aus dem ursprünglichen M1-Design beginnen |
| **Ersatz-microSD-Karte** | Separates OS vorbereiten und ursprüngliche Installation erhalten |
| **Passendes Netzteil und Antenne** | Hardwareaufbau und RF-Band des Moduls berücksichtigen |
| **SSH oder lokale Konsole** | Diagnosedaten erfassen und Konfiguration bearbeiten |
| **LoRaWAN-Sensor und -Server** | Anwendungsauslieferung nach der Inbetriebnahme verifizieren |
| **Messgerät und Hardwarekenntnisse** | Nicht dokumentierte Verbindungen vor dem Ansteuern untersuchen |

Fotografiere beide Seiten der stromlosen Baugruppe, bevor du etwas entfernst. Notiere Steckerausrichtung, Schrauben, Abstandshalter und Antennenführung. Bewahre Originalkarte und Konfiguration auf, bis die Ersatzinstallation die Abnahmekriterien erfüllt.

## Die drei Ebenen identifizieren

**Der komplette M1, sein Träger-Shield und sein Konzentrator sind verschiedene Komponenten.** Seeed beschreibt den Hotspot als Raspberry Pi 4 mit einem WM1302/SX1302- oder WM1303/SX1303-Konzentrator. Ein Angebot mit dem Titel „SenseCAP M1 Shield“ belegt nicht, welches Teil mit der Trägerplatine geliefert wird. [Seeeds M1-Übersicht](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Der **Träger** verbindet Stromversorgung und Peripheriesignale zwischen Pi und Modul. Der **Konzentrator** übernimmt Funkempfang und -übertragung. Ein **Packet Forwarder** läuft auf dem Host und tauscht empfangene Funkpakete sowie geplante Downlinks mit einem Server aus. [Semtechs SX1302-HAL-Übersicht](https://github.com/Lora-net/sx1302_hal)

Ein Temperatursensor sendet zum Beispiel ein Uplink-Paket per Funk. Der Konzentrator empfängt es, der Host leitet es weiter und Netzwerk- sowie Anwendungsdienste verarbeiten es. Ein erfolgreicher Linux-Start bestätigt nur den Host-Teil dieser Kette.

Clockwork Birds Foto zeigt eine M1-Trägerplatine v1.1 mit einem als <code>WM1302-SPI-EU868</code> beschrifteten Modul. Nutze das Foto, um Beschriftungen deiner eigenen Hardware zu finden. Seriennummern identifizieren das fotografierte Gerät, nicht die Konfiguration eines anderen Gateways.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Grüne M1-Trägerplatine mit beschriftetem WM1302-SPI-EU868-Modul neben USB-C, Taste, Lüfteranschluss und Antennenkabel" caption="M1-v1.1-Hardware von Clockwork Bird, auch für das Titelbild verwendet" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Stromversorgung und Funkverbindungen

**Behandle den USB-C-Anschluss des M1 als Stromeingang.** Der Hersteller nennt für das komplette Gateway 5 V DC und 3 A und führt USB-C als Stromversorgungsanschluss auf. Die Bezeichnung Ladeanschluss deutet eine Akkufunktion an, die diese Spezifikation nicht nennt. [SenseCAP-M1-Spezifikationen](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Das Blockdiagramm trennt die 5-V-Versorgung von der geregelten 3,3-V-Schiene des Moduls. Ein laufender Pi bei gleichzeitig stromlosem Konzentrator ist möglich. Lege niemals 5 V an einen Signalpin an und gehe nicht von isolierten Stromeingängen aus.

**SPI- und USB-Modulvarianten benötigen unterschiedliche Hostverbindungen.** Seeeds WM1302-Dokumentation beschreibt direkten SPI-Zugriff für das SPI-Modell und eine STM32L4-USB-Brücke für das USB-Modell. Mini-PCIe beschreibt den Formfaktor; die dokumentierten elektrischen Schnittstellen sind SPI oder USB. Ein mechanisch passender Laptop-Steckplatz belegt keine Kompatibilität. [Seeeds WM1302-Dokumentation](https://github.com/seeed-lora/WM1302-doc)

Setze das Modul bei getrennter Stromversorgung ein und schließe eine geeignete Antenne an. Stimme Funkhardware, Antenne und Netzwerkplan aufeinander ab. Eine Konfigurationsänderung ersetzt keine Funkkomponenten. Der M1-Stromanschluss belegt auch keine Unterstützung einer USB-Konzentratorvariante.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Blockdiagramm mit Raspberry Pi 4 und M1 Shield, verbunden über Stromversorgung, SPI, GPIO und I2C" caption="SenseCAP-Herstellerdiagramm aus Clockwork Birds Originalartikel zum WM1302-Design" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Pinout sorgfältig prüfen

**Führe BCM-GPIO-Nummern und physische Header-Pinnummern getrennt auf.** BCM GPIO17 liegt beispielsweise am physischen Pin 11 des Pi-Headers. Der Modulstecker verwendet eine dritte Nummerierung. Seine Reset-Pinnummer ist keine Raspberry-Pi-GPIO-Nummer.

Die Tabelle überträgt Verbindungen aus Clockwork Birds annotierter Headergrafik. Sie ist eine **Community-Referenz**, kein vollständiger Hersteller-Schaltplan und keine Messung jeder M1-Revision. Die Grafik nennt SX1262, während Semtechs allgemeines Reset-Skript SX1261 aufführt.

| Signal in der Grafik | BCM / physischer Pin | Interpretation |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Gemeinsamer Verwaltungsbus |
| **SX1302-Reset** | GPIO17 / 11 | Möglicher Konzentrator-Reset |
| **Benutzer-LED** | GPIO22 / 15 | M1-Markierung |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | SPI-Datensignale |
| **SPI-Takt** | GPIO11 / 23 | SPI-Taktsignal |
| **SX1302-Chip-Select** | GPIO8 / 24 | SPI0 CE0 |
| **SX1262-Reset** | GPIO5 / 29 | Möglicher Zusatzfunk-Reset |
| **SX1262-Chip-Select** | GPIO6 / 31 | GPIO6, verschieden von SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Statusausgang des Zusatzfunks |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Zusätzliche Signale, vor Nutzung prüfen |

Durchgestrichene GPS-/UART-Markierungen belegen keinen GPS-fähigen M1. Lasse GPS-Einrichtung weg, sofern deine Hardware sie nicht unterstützt. Die Grafik klärt auch Benutzertaste und Lüftersteuerung nicht. [Clockwork Birds Pinout-Untersuchung](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Annotierte Raspberry-Pi-Headerzeichnung mit M1-LED, Konzentrator-Reset, SPI-Signalen und durchgestrichenen GPS-Verbindungen" caption="Community-Referenz ohne vollständige Abdeckung der Board-Revisionen, kein vollständiger M1-Schaltplan" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Konflikte in Reset-Skripten auflösen

**Ein Reset-Skript wählt elektrische Ausgänge, nicht nur Softwarepräferenzen.** Semtechs Upstream-Resetdatei <code>reset_lgw.sh</code> zielt auf das CoreCell-Referenzdesign. Zu den Standardwerten gehören GPIO23 für Konzentrator-Reset, GPIO18 für Stromfreigabe, GPIO22 für Zusatz-Reset und GPIO13 für den Reset eines AD5338R. [Semtech-Reset-Skript](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Seeeds ältere Einrichtung ändert die beiden Reset-Zuordnungen auf GPIO17 und GPIO5, lässt aber die übrigen Referenzwerte bestehen. Vergleiche sie mit der M1-Grafik, bevor du das Beispiel verwendest. [Seeed-WM1302-Einrichtung](https://github.com/seeed-lora/WM1302-doc)

| Zuordnung | Widersprüchlicher Beleg | Erforderliche Entscheidung |
|---|---|---|
| **GPIO22 als Zusatz-Reset** | M1-Grafik bezeichnet ihn als Benutzer-LED | Annahme vor LED-Aktivierung entfernen |
| **GPIO18 als Stromfreigabe** | M1-Grafik bezeichnet ihn als BUSY-Ausgang | Netz und Richtung vor Ansteuerung prüfen |
| **GPIO13 als DAC-Reset** | Allgemeines Skript nennt ein anderes Referenzdesign | Prüfen, ob die Schaltung vorhanden ist |
| **Zusätzliches SPI-Gerät** | M1-Grafik verwendet GPIO6 statt CE1 | Chip-Select und Treiberunterstützung prüfen |

**Ableitung:** Falls GPIO18 wie abgebildet mit einem Ausgang des Zusatzfunkmoduls verbunden ist, entsteht beim Konfigurieren des Pi-Pins als Ausgang ein Risiko elektrischer Konflikte. Die widersprüchlichen Angaben begründen eine Prüfung, aber keinen Schadensnachweis und kein universelles Pinout für alle Revisionen.

Verfolge zugängliche Verbindungen zwischen Header und Modulstecker bei ausgeschalteter Stromversorgung. Notiere Revision und Endpunkte. Eine Durchgangsmessung belegt eine Verbindung; Bauteilunterlagen erklären Signalrichtung und Grenzwerte.

Nutze das Herstellerdiagramm, um Modulstecker-Pins nicht mit Pi-Header-Pins zu verwechseln. Die Zusatzfunksignale beschreiben die veröffentlichte Modulreferenz, nicht identische Chips oder Funktionen jeder Revision. [Seeed-WM1302-Modul-Pinout](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Seeed-Diagramm mit beiden Seiten des WM1302-Modulsteckers für Strom, SPI, I2C und Zusatzfunksignale" caption="Die Nummerierung des Modulsteckers unterscheidet sich von der Raspberry-Pi-Headernummerierung" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Raspberry Pi OS vorbereiten

Erfasse die Hostumgebung auf deiner Ersatzinstallation:

~~~bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
~~~

OS-Version, Kernel und Pi-Modell bilden die reproduzierbare Ausgangsbasis. Notiere sie vor dem Vergleich mit älteren Tutorials.

Installiere Prüf- und Build-Werkzeuge:

~~~bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
~~~

Aktiviere unter **Interface Options** SPI und I2C und starte neu. SPI dient dem Konzentratorpfad; I2C unterstützt Verwaltungsgeräte. Übernimm keine unnötigen GPS-Änderungen für serielle Schnittstellen aus anderen HAT-Anleitungen.

Prüfe verfügbare Schnittstellen:

~~~bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
~~~

Diese Befehle listen Gerätedateien, Adapter, GPIO-Controller, Leitungsinformationen und die Werkzeugversion auf. **<code>i2cdetect -l</code> listet Adapter, ohne Geräteadressen abzufragen.** Eine Datei wie <code>/dev/spidev0.0</code> belegt eine Schnittstelle, aber keine Kommunikation mit einem funktionierenden Konzentrator. [i2c-tools-Handbuch](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Raspberry-Pi-GPIO-Leitfaden](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### GPIO-Versionen berücksichtigen

**Übernimm keine globalen GPIO-Nummern eines anderen Computers.** Ältere Skripte schreiben über <code>/sys/class/gpio</code>, eine vom Kernel als veraltet markierte Schnittstelle. Neue Userspace-Integrationen sollten die GPIO-Character-Device-Schnittstelle mit korrektem Controller und Leitungsindex verwenden. [Linux-GPIO-Dokumentation](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

Prüfe <code>gpioset --help</code> vor einer Skriptanpassung. Version 1 und 2 unterscheiden sich in Syntax und Prozessverhalten. Das aktuelle Werkzeug hält Leitungen standardmäßig reserviert; sein portabler Vertrag garantiert den Zustand nach Prozessende nicht. [libgpiod-gpioset-Dokumentation](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi dokumentiert Kernelverhalten, bei dem Ausgänge ihren Zustand beibehalten können. Erfasse die echte Kernelkonfiguration, statt identisches Verhalten auf allen Linux-Systemen anzunehmen. Neuere Nummerierung oder ein anderes GPIO-Werkzeug behebt keine falsche elektrische Zuordnung. [Raspberry-Pi-GPIO-Leitfaden](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## Benutzer-LED testen

Nachdem du GPIO22 der LED zugeordnet und widersprüchliche GPIO-Verwender entfernt hast, bearbeite die Boot-Konfiguration:

~~~bash
sudoedit /boot/firmware/config.txt
~~~

Aktuelle Raspberry-Pi-OS-Versionen mounten die Boot-Konfiguration unter **<code>/boot/firmware/config.txt</code>**. Ältere Images nutzen <code>/boot/config.txt</code>, den Pfad im Artikel von 2023. Sichere die aktive Datei. [Raspberry-Pi-config.txt-Dokumentation](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Füge das LED-Overlay in einem für deinen Pi geltenden Abschnitt wie <code>[all]</code> hinzu:

~~~ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
~~~

**<code>gpio</code>** verwendet BCM-Nummerierung. **<code>label</code>** benennt das Linux-LED-Gerät, und **<code>trigger=heartbeat</code>** weist den Kernel-Heartbeat-Trigger zu. Clockwork Bird berichtet diese M1-Zuordnung; Raspberry Pi dokumentiert die Parameter. [Ursprüngliche LED-Beobachtung](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [gpio-led-Overlay-Referenz](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Prüfe nach dem Neustart die registrierte LED:

~~~bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
~~~

Erwartet wird ein <code>lorawan</code>-Eintrag mit <code>heartbeat</code> in eckigen Klammern. Eine blinkende LED belegt diesen GPIO-/Treiberpfad. Sie meldet weder LoRaWAN-Registrierung noch Funkempfang oder Helium-Status.

## I2C-Geräte untersuchen

**Eine I2C-Adresse ist ein Hinweis, keine Geräteidentität.** Clockwork Bird beobachtete Antworten an <code>0x60</code> und <code>0x39</code> und las danach ATECC608-Informationen über die Kryptobibliothek aus. Die Identifizierung des Temperatursensors blieb vorläufig.

Beginne mit der Adapterliste. Breite <code>i2cdetect</code>-Scans senden Prüftransaktionen, statt den Bus passiv zu beobachten. Das Upstream-Handbuch warnt vor Störungen. Scanne laufende Gateways und unbekannte Geräte nicht routinemäßig. [i2c-tools-Abfrageverhalten](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Beobachtung | Belegte Schlussfolgerung | Offene Frage |
|---|---|---|
| **Antwort an <code>0x60</code>** | Ein Gerät bestätigte die Abfrage | Ist es das erwartete Secure Element? |
| **Antwort an <code>0x39</code>** | Ein Gerät bestätigte die Abfrage | Welche Komponente und Revision antworteten? |
| **<code>UU</code> im Scan** | Ein Treiber besitzt die Adresse; Abfrage übersprungen | Welcher Treiber hat sie belegt? |
| **Keine Antwort** | Keine Bestätigung empfangen | Strom, Bus, Belegung oder Geräteprotokoll? |

### Besserer Hinweis auf den Temperatursensor

**STTS751 ist ein belegter Kandidat für <code>0x39</code>.** Semtechs Temperaturtreiber-Header ordnet diese Adresse ausdrücklich <code>STTS751-0DP3F</code> zu. Das stärkt die Hypothese, identifiziert aber nicht jedes Board. [Semtech-STTS751-Treiberheader](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

Nach Identifizierung eines kompatiblen Bauteils und Prüfung der Belegung kannst du Identifikationsregister auslesen:

~~~bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
~~~

**<code>1</code>** wählt den geprüften Bus, **<code>0x39</code>** das Gerät und **<code>b</code>** einen SMBus-Byte-Datenzugriff. Beim STTS751-0 ist die Produkt-ID an <code>0xFD</code> <code>0x00</code>; die Hersteller-ID an <code>0xFE</code> lautet <code>0x53</code>. Die Transaktionen lesen Register, schreiben aber keine Konfigurationswerte. [STTS751-Datenblatt](https://www.st.com/resource/en/datasheet/stts751.pdf)

Vergleiche die Werte mit Bauteilmarkierung und Dokumentation. Ein passendes Paar stärkt die Identifizierung. Bei Fehlern prüfst du Bus und Belegung, bevor du die Konfiguration änderst. Der Sensor misst lokale Temperatur, nicht die CPU-Temperatur des Pi.

## Secure Element untersuchen

**Der ATECC608 ist eine separate Authentifizierungskomponente.** Konfiguration, Seriennummer, öffentlicher Schlüssel und geschütztes Schlüsselmaterial sind unterschiedliche Dinge. Ein lesbarer öffentlicher Schlüssel gibt den privaten Schlüssel nicht preis.

Microchips **CryptoAuthLib** stellt die Geräteschnittstelle bereit. Das Repository **cryptoauthtools** enthält Beispiele. Bereite native Bibliothek und Python-Bindings nach den Projektanleitungen für dein System vor. Eine beliebige Python-Bibliothek oder ein kopiertes Skript belegt kein funktionierendes I2C-Backend. [Microchip CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [Microchip cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools)

Im vorbereiteten Verzeichnis <code>cryptoauthtools/python/examples</code> lautet der Inspektionsbefehl:

~~~bash
sudo python3 info.py -i i2c
~~~

**<code>-i i2c</code>** wählt die Schnittstelle. Bei einer virtuellen Umgebung verwende ihren Python-Interpreter und stelle sicher, dass er die native Bibliothek findet. <code>sudo python3</code> wählt oft den Systeminterpreter, was Importfehler erklärt.

Die geprüfte Datei <code>info.py</code> liest Revision, Seriennummer, Konfiguration und Sperrstatus. Bei gesperrtem Datenbereich versucht sie, den öffentlichen Schlüssel aus Slot 0 zu lesen. Sie führt nicht die Provisionierung des Beispiels aus. Ein fehlgeschlagener Slot-0-Schlüsselabruf allein belegt kein defektes Gerät. [Microchip-info.py-Quellcode](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Ausgabe oder Vorgang | Bedeutung |
|---|---|
| **Konfiguration gesperrt** | Konfigurationseinschränkungen gelten |
| **Datenbereich gesperrt** | Zugriff anhand der Slot-Richtlinien beurteilen |
| **Öffentlicher Schlüssel angezeigt** | Öffentliche Information gelesen, kein privater Schlüssel exportiert |
| **<code>config.py</code> ausgeführt** | Provisionierungsbeispiel mit Änderungen, Sperren und Schlüsselerzeugung |

**Führe <code>config.py</code> nicht aus, um einen Inspektionsfehler zu beheben.** Der Quellcode enthält Konfigurationsschreibvorgänge, Zonensperren und Schlüsselerzeugung. Auch der Standardschlüsselerzeugungspfad ist bei einem bereits konfigurierten Gerät relevant. [Microchip-config.py-Quellcode](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Microchips Provisionierungsprofile zeigen, dass ein gesperrter Datenbereich nicht bedeutet, alle Slots hätten dieselben Zugriffsrechte. Sie belegen nicht die M1-Konfiguration. Erhalte die bestehende Konfiguration und prüfe die passenden Bauteilunterlagen, bevor du eine Schlüsselweiterverwendung planst. [Microchip-Speicher- und Slot-Zugriffsrichtlinien](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## Unbekanntes zu Lüfter und Taste klären

**Ein dreipoliger Lüfteranschluss belegt weder Spannung noch Polarität oder Steuerungsmethode.** Fotografiere Pinnummerierung und Lüfterbeschriftung. Kläre Versorgungs- und Steuerleitungen, bevor du Ersatz anschließt oder ein GPIO-Overlay auswählst.

Auch die GPIO-Leitung der Taste ist unbekannt. Suche nach einem Treiber oder einer Konfiguration für deine Board-Revision und prüfe die Verbindung bei ausgeschaltetem Gerät. Weise nicht jeden scheinbar freien GPIO als Ausgang zu, um die Taste zu finden.

| Peripheriegerät | Zu erfassender Nachweis | Abnahmekriterium |
|---|---|---|
| **Lüfterversorgung** | Lüfterangabe, Masse und Versorgung am Anschluss | Messwert entspricht der Spezifikation |
| **Lüftersteuerung** | Treiber, Konfiguration oder nachverfolgte Schaltung | Definiertes Verhalten beim Start und bei Hitze |
| **Benutzertaste** | Verdrahtung, GPIO-Zuordnung und Eingangslogik | Ein Tastendruck erzeugt das erwartete Ereignis |

Ein frisches OS übernimmt nicht automatisch die Kühlungssteuerung des ursprünglichen Geräts. Beobachte Lüfter und Temperaturen während eines längeren Tests. Erhalte den Luftstrom und brich bei unzureichender Kühlung ab.

## Gateway-Stack auswählen

**Trenne Board-Unterstützung vom Serverprotokoll.** Ein kompatibler LoRaWAN-Server behebt weder eine falsche Reset-Routine noch RF-Kalibrierung. Wähle Software, die Konzentrator, Trägerverdrahtung, OS und regionale Konfiguration unterstützt.

| Softwarepfad | Nützliche Rolle | Vor Bereitstellung prüfen |
|---|---|---|
| **Semtech SX1302 HAL** | Quelltextbasierte Inbetriebnahme und Diagnosetools | Board-Reset-Routine und Modulkonfiguration |
| **LoRa Basics Station** | Authentifizierte Gatewayverbindung | Board-Integration und Serverzugangsdaten |
| **ChirpStack Concentratord** | Dedizierter Konzentrator-Dienst | Modell, Kalibrierung und GPIO-Zuordnung |

ChirpStack listet das SPI-Modell **<code>seeed_wm1302</code>**. Dies belegt Modulunterstützung, kein vollständiges M1-Image und keine Unterstützung jeder Revision. Verwechsle SenseCAP-M2-Anleitungen nicht mit M1-Firmwareanleitungen. [ChirpStack-Hardwareunterstützung](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [Seeed-Installationsziel](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Für The Things Stack empfiehlt die Dokumentation **LoRa Basics Station** statt des älteren Semtech-UDP-Forwarders. Station bietet TLS, Token-Authentifizierung und zentrale Konfiguration. UDP-Beispiele erklären Paketweiterleitung, bieten diesen Schutz aber nicht. [The-Things-Stack-UDP-Hinweise](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa-Basics-Station-Dokumentation](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Upstream-Werkzeuge vorbereiten

Baue auf dem Ziel-Pi in einem neuen Arbeitsverzeichnis:

~~~bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
~~~

Speichere die Commit-ID mit den Build-Ausgaben. Ein erfolgreicher Build belegt Compilerkompatibilität; das Funkmodul braucht weiterhin eine verifizierte Reset-Implementierung und korrekte Konfiguration. [SX1302-HAL-Build- und Werkzeugdokumentation](https://github.com/Lora-net/sx1302_hal)

Prüfe das Reset-Skript vor Hardwarewerkzeugen:

~~~bash
sed -n '1,180p' tools/reset_lgw.sh
~~~

Kopiere es nicht unverändert in das Laufzeitverzeichnis. Semtech dokumentiert, dass Hardwarewerkzeuge einschließlich Identifikationsprogramme Reset-Skripte automatisch verwenden. Prüfe jeden Pin, Signalrichtung, GPIO-API und Zustand beim Starten und Beenden.

Nach der Board-Verifikation liest du laut Stack-Anleitung die Konzentrator-EUI aus und registrierst das Gateway. Erhalte Modulkalibrierung und RF-Einstellungen. In Semtech UDP ist <code>gateway_ID</code> die EUI; die Gateway-ID in der The-Things-Stack-Konsole ist eine menschenlesbare Kennung. [The-Things-Stack-Gatewaykonfiguration](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## Sensordatenübertragung nachweisen

**Nutze gestufte Nachweise, um die erste fehlerhafte Ebene zu finden.** Ein online markiertes Gateway belegt eine Serververbindung. Die Abnahme braucht zusätzlich einen bekannten Sensor, passenden Frequenzplan und dekodierte Nutzlast. Dies ist ein Testvorschlag, keine M1-Messung:

| Prüfpunkt | Zu speichernder Nachweis | Bedeutung |
|---|---|---|
| **Host bereit** | OS, Kernel, Stromversorgung und Schnittstelleninventar | Linux-Vorbereitung abgeschlossen |
| **Konzentrator antwortet** | EUI und erfolgreiche Initialisierung | Host-Kommunikation funktioniert |
| **Funkempfang** | Sensorpaket und Empfangsmetadaten | Empfangspfad funktioniert |
| **Server nimmt an** | Gatewayereignis zum Sensor | Weiterleitung und Routing funktionieren |
| **Anwendung dekodiert** | Erwarteter Messwert und Zeitstempel | Anwendungspfad funktioniert |
| **Neustartwiederherstellung** | Dieselben Prüfungen nach Neustart | Startkonfiguration reproduzierbar |

Bei einem **OTAA**-Sensor prüfst du zusätzlich Aktivierungsaustausch und anschließenden Uplink. OTAA bedeutet Over-the-Air Activation, das Verfahren zum Einrichten einer Sitzung. Eine empfangene Join-Anfrage belegt weder erfolgreichen Beitritt noch Downlink. [The-Things-Stack-Aktivierungsdokumentation](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Beispieldiagnose:** Das Gateway verbindet sich mit dem Server und meldet die EUI, aber der Sensor erscheint nicht. Prüfe Sendeeinstellungen, Empfangskanäle, Antennenpfad und Funkprotokolle. Eine Neuprogrammierung des ATECC608 behebt den fehlenden Nachweis nicht.

**Zweite Diagnose:** Ein Sensorpaket erscheint lokal, erreicht aber nicht die Anwendung. Vergleiche Zeitstempel mit Gateway- und Serverereignissen; prüfe Routing, Registrierung und Dekodierung. Ein Funkpaket im Protokoll reicht nicht, um den Decoder verantwortlich zu machen, bevor der Server das Ereignis annimmt.

## Fehlersuche nach Symptom

| Symptom | Zuerst prüfen | Nächster Schritt |
|---|---|---|
| **Keine SPI-Gerätedatei** | Boot-Konfiguration und Schnittstelleneinstellungen | Schnittstelle aktivieren und neu starten |
| **SPI vorhanden, Funk fällt aus** | Strom, Sitz, Reset-Sequenz, Chip-Select | Elektrischen Pfad vor Serveränderungen prüfen |
| **GPIO-Exportfehler** | Alte sysfs-Annahmen und Kernel | Geprüfte GPIO-API-Implementierung verwenden |
| **GPIO bereits belegt** | Verbraucher in <code>gpioinfo</code> | Belegung vor erneutem Versuch klären |
| **LED fällt nach Einrichtung aus** | Overlay und GPIO22-Konflikte | LED-Geräte und Reset-Skript prüfen |
| **I2C-Gerät fehlt** | Busnummer, Strom, Belegung | Ohne wiederholte breite Scans untersuchen |
| **Kryptobibliothek importiert nicht** | Interpreter, Bindings, native Bibliothek | Softwareumgebung reparieren |
| **Öffentlicher Schlüssel nicht lesbar** | Slot-Rechte und erfolgreiche frühere Lesevorgänge | Konfiguration prüfen, nicht provisionieren |
| **Lüfter läuft nicht** | Versorgung und Kühlungssteuerung | Kühlung vor Dauerlast wiederherstellen |
| **Uplinks kommen an, Join scheitert** | Downlinkpfad und Funkplan | Join-Antwort und Empfangsfenster verfolgen |

Behandle jede Korrektur als einzelnes Experiment. Sichere die vorherige Konfiguration, ändere eine Variable, wiederhole dieselbe Prüfung und notiere, ob der erwartete Nachweis erschien.

## Hardwareprotokoll erstellen

Nutze diese Vorlage für eine reproduzierbare Übergabe:

~~~text
Trägerrevision und Fotos:
Konzentrator-Modell, Schnittstelle und RF-Band:
Host-Modell / OS / Kernel / GPIO-Werkzeugversion:
Stromversorgung / Antenne / Kühlung:
Verifizierte Pinbelegung und Nachweis:
Ungeklärte Leitungen und ausgeschlossene Funktionen:
Software-Repository und Commit:
Reset-Implementierung und GPIO-Belegung:
Gateway-EUI / Server / Frequenzplan:
Sensoraktivierung und dekodierter Uplink-Nachweis:
Ergebnis nach Neustart:
Aufbewahrungsort der Originalkarte und Rollback-Verfahren:
~~~

**Entscheidungsübung:** Du hast eine günstige Trägerplatine ohne Modulbeschriftung und eine teurere Baugruppe mit lesbaren Kennzeichnungen und dokumentiertem Betrieb. Vergleiche Kosten für fehlenden Pi, Konzentrator, Antenne, Netzteil und Prüfzeit. Entscheidend sind Gesamtkosten und Nachweise für deinen Dienst, nicht nur der beworbene Trägerpreis.

**Erwartete Begründung:** Ein Lernprojekt toleriert ungeklärte Verdrahtung, wenn Messgeräte und Zeit verfügbar sind. Ein Gateway für produktive Sensoren braucht reproduzierbaren Start, Kühlung, Softwareunterstützung und nachgewiesene Übertragung. Notiere, welcher ungeklärte Zustand die Bereitstellung verhindert.

## Nächste Schritte

Vervollständige zuerst das Hardwareprotokoll und kläre Reset-Skript-Konflikte. Nimm danach einen bekannten Sensor in Betrieb und sichere Nachweise bis zur Dekodierung in der Anwendung, bevor du weitere Geräte hinzufügst.

**Abnahmeprotokoll:** Speichere Board-Revision, Modulbeschriftung, Funkband, gemessene Versorgung, aktives SPI-Gerät, GPIO-Leitungsnamen, Reset-Sequenz, Konzentratorprotokoll, Serververbindung und einen dekodierten Uplink. Kennzeichne jeden Wert als beobachtet, dokumentiert oder angenommen. Ein gestarteter Prozess beweist weder RF-Leistung noch Anwendungsauslieferung.

Wenn du Mesh-Nachrichten senden willst, vergleiche die Protokollrollen in unserem [Leitfaden zu Meshtastic, MeshCore und Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Gemeinsame LoRa-Funktechnik belegt keine Firmwarekompatibilität. Für Messaging nutze die [Dokumentation unterstützter MeshtasticD-Hardware](https://meshtastic.org/docs/meshtasticd/), nicht dieses LoRaWAN-Verfahren.

## Quellen und Bildnachweise

Recherche geprüft am 12. September 2026. Undatierte Dokumentation und Repository-Links beziehen sich auf geprüfte Versionen. Lokale Abbildungen behalten ihre ursprünglichen Beschriftungen und Herkunftsnachweise.

| Herausgeber | Quelle und Datum |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 03.05.2023. Board-Foto, Headerzeichnung und Hersteller-Blockdiagramm |
| **Seeed Studio / SenseCAP** | [M1-Übersicht und Spezifikationen](https://www.sensecapmx.com/docs/sensecap-m1/overview/), undatiert. Ursprung des Blockdiagramms |
| **Seeed Studio** | [WM1302-Dokumentation und Modul-Pinout](https://github.com/seeed-lora/WM1302-doc), Repository |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), einschließlich Reset-Skript und Temperaturtreiber |
| **Raspberry Pi** | [Boot-Konfiguration](https://www.raspberrypi.com/documentation/computers/config_txt.html), [GPIO-Leitfaden](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) und [Overlay-Referenz](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Veraltete GPIO-sysfs-Schnittstelle](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) und [gpioset-Handbuch](https://libgpiod.readthedocs.io/en/master/gpioset.html), August 2026 |
| **i2c-tools** | [i2cdetect-Handbuch](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), Quellcode v4.3 |
| **STMicroelectronics** | [STTS751-Datenblatt](https://www.st.com/resource/en/datasheet/stts751.pdf), Revision 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) und [Slot-Zugriffsrichtlinien](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Concentratord-Hardwareunterstützung](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) und [Seeed-Installationsziel](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [UDP-Forwarder](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) und [Geräteaktivierung](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [MeshtasticD-Dokumentation](https://meshtastic.org/docs/meshtasticd/), undatiert |
