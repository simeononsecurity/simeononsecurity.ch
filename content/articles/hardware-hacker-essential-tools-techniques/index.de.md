---
title: "Die Welt der Hardware-Manipulation entdecken"
date: 2023-07-02
lastmod: 2026-11-15
toc: true
draft: false
description: "Lerne Hardware-Manipulation kennen und entdecke die wichtigsten Werkzeuge und Techniken dafür."
genre: ["Technologie und Hacking", "Cybersicherheit", "Hardware-Manipulation", "Hacker-Werkzeuge", "Elektronik", "Internet der Dinge", "Elektronik zum Selbermachen", "Rückentwicklung", "Mikrocontroller", "Funkangriffe"]
tags: ["Hardware-Angreifer", "Hardware-Manipulation", "Hardware für Angreifer", "Werkzeuge für Hardware-Angreifer", "Werkzeuge zur Hardware-Manipulation", "Werkzeuge zur Manipulation von Hardware", "JTAG-Diagnosegerät", "Logikanalysator", "Bus Pirate", "softwaredefinierter Funk", "SDR", "Lötkolben", "Mikrocontroller", "Arduino", "Raspberry Pi", "ESP8266", "Rückentwicklung", "Funkangriffe", "Elektronik", "Cybersicherheit", "Elektronik zum Selbermachen", "HackRF", "RTL-SDR", "OpenOCD", "J-Link", "Saleae Logic", "Sigrok", "Technologie", "Sicherheit"]
cover: "/img/cover/A_symbolic_art_style_depicting_a_hacker_surrou.webp"
coverAlt: "Eine symbolische Darstellung eines Hackers zwischen elektronischen Geräten als Sinnbild für Hardware-Manipulation."
coverCaption: "Neue Möglichkeiten erschließen: die Welt der Hardware-Manipulation."
---

## Einleitung

Technik wird immer komplexer, und vernetzte Geräte sind weit verbreitet. Deshalb richten sich Angriffe heute gegen Software und Hardware. Unter Hardware-Manipulation versteht man Eingriffe in elektronische Geräte, um unbefugten Zugriff zu erhalten, Informationen auszulesen oder Gerätefunktionen zu steuern. In diesem Artikel geht es um [Hardware für Angreifer](https://simeononsecurity.com/recommendations/hacker_hardware/) und die wichtigsten Werkzeuge für [Hardware-Angreifer](https://simeononsecurity.com/recommendations/hacker_hardware/).

## Der Aufstieg der Hardware-Manipulation

In den vergangenen Jahren ist Hardware-Manipulation stärker in den Fokus gerückt, weil immer mehr Geräte vernetzt und für Sicherheitsverletzungen anfällig sind. Dabei manipulieren Angreifer elektronische Komponenten wie Leiterplatten, Mikrocontroller, Sensoren und Aktoren, um Schwachstellen auszunutzen und unbefugten Zugriff auf Systeme zu erhalten.

Software-Schwachstellen lassen sich vergleichsweise einfach beheben. Hardware-Schwachstellen sind oft schwieriger zu beseitigen. Bei der Hardware-Manipulation können Angreifer Geräte physisch manipulieren, um vertrauliche Informationen auszulesen, schädlichen Code einzuschleusen oder den Betrieb des Geräts zu kontrollieren. Das birgt erhebliche Risiken für Einzelpersonen, Unternehmen und sogar kritische Infrastrukturen.

## Wichtige Werkzeuge für die Hardware-Manipulation

### 1. JTAG-Diagnosegerät

Ein JTAG-Diagnosegerät (Joint Test Action Group) ist ein Hardware-Werkzeug, mit dem Angreifer auf digitale Schaltungen elektronischer Geräte zugreifen und diese manipulieren. Es bietet eine standardisierte Schnittstelle zum Testen und Debuggen integrierter Schaltungen und eignet sich damit für die Hardware-Manipulation. Damit lassen sich Sicherheitsmaßnahmen umgehen, Firmware auslesen oder das Verhalten eines Geräts verändern.

{{< youtube id="_FSM_10JXsM" >}}

Zu den bekannten JTAG-Diagnosegeräten gehören:

- [OpenOCD](https://github.com/sysprogs/openocd)
- [J-Link](https://www.segger.com/products/debug-probes/j-link/)

### 2. Logikanalysator

Ein Logikanalysator erfasst und analysiert digitale Signale in elektronischen Systemen. Damit lassen sich digitale Schaltungen eines Geräts beobachten und verstehen, Schwachstellen erkennen und Hardware rückentwickeln. Aus der Signalanalyse können Angreifer Verschlüsselungsschlüssel auslesen, Kommunikationsprotokolle erkennen und Hintertüren im System finden.

{{< youtube id="u1DYs2I-_lU" >}}

Beliebte Logikanalysatoren für Hardware-Angreifer sind:

- [Saleae Logic](https://www.saleae.com/)
- [Sigrok](https://sigrok.org/)

### 3. Bus Pirate

Bus Pirate ist ein vielseitiges Werkzeug für die Verbindung mit verschiedenen elektronischen Kommunikationsbussen wie I2C, SPI und UART. Es dient als Brücke zwischen einem Computer und dem Zielgerät. So lassen sich Daten direkt über den Kommunikationsbus des Geräts lesen und schreiben. Das Werkzeug eignet sich zum Abhören von Kommunikation, zum Einspeisen von Daten und zum Untersuchen des Geräteinneren.

{{< youtube id="lP8vMvBu3Bg" >}}

Die offizielle Website von Bus Pirate ist [hier](http://dangerousprototypes.com/docs/Bus_Pirate).

### 4. Softwaredefinierter Funk (SDR)

Ein softwaredefiniertes Funkgerät (SDR) ist ein Funkkommunikationssystem, dessen Funktionen durch Software festgelegt werden, statt sich auf herkömmliche Hardwarekomponenten zu stützen. Mit SDR lassen sich drahtlose Kommunikation abfangen, analysieren und manipulieren. Besonders nützlich sind SDRs für funkferngesteuerte Geräte, drahtlose Schlüsselsysteme und andere Funkprotokolle.

{{< youtube id="nB6XQSEFwVA" >}}

Beliebte SDR-Werkzeuge für die Hardware-Manipulation sind:

- [HackRF](https://amzn.to/40aBO1F)
- [RTL-SDR](https://amzn.to/3Mh9HrP)

### 5. Lötkolben und Zubehör

Löten ist eine wichtige Fähigkeit für Hardware-Angreifer, denn damit lassen sich elektronische Schaltungen verändern oder reparieren. Ein Lötkolben erhitzt und schmilzt Lot, um elektrische Verbindungen zwischen Bauteilen herzustellen. Für Projekte zur Hardware-Manipulation braucht man außerdem Zubehör wie [Lötdraht](https://amzn.to/46FrAZu), [Flussmittel](https://amzn.to/3FucA4H) und [Entlötwerkzeuge](https://amzn.to/3Sejnau).

{{< youtube id="R2sPDQeGlj8" >}}

Diese beiden Lötkolben empfehlen wir:
- [Digitale Lötstation von Merece](https://amzn.to/46zZVct)
- [PINECIL, kompakter intelligenter Lötkolben](https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/)

### 6. Mikrocontroller und Entwicklungsplatinen

Mikrocontroller sind kleine programmierbare Geräte. Hardware-Angreifer können damit eigene Werkzeuge entwickeln oder vorhandene Geräte verändern. Sie bieten eine flexible Plattform, um verschiedene Techniken auszuprobieren. Beliebte Mikrocontroller und Entwicklungsplatinen sind [Arduino](https://amzn.to/476dh03), [Raspberry Pi](https://amzn.to/3Fw1Ann), [ESP8266](https://amzn.to/3s86pAn) und [ESP32](https://amzn.to/3Ftyxkz).

{{< youtube id="RmD7UgKvUnY" >}}

## Fazit

Hardware-Manipulation stellt in unserer vernetzten Welt eine erhebliche Sicherheitsherausforderung dar. Mit dem technischen Fortschritt sollten Sie die Werkzeuge und Methoden kennen, mit denen Angreifer Hardware kompromittieren. Dieser Artikel hat wichtige Werkzeuge vorgestellt: JTAG-Diagnosegerät, Logikanalysatoren, Bus Pirate, SDR, Lötgeräte und Mikrocontroller. Wer diese Werkzeuge versteht, kann Systeme besser schützen und potenzielle Risiken verringern.

## Quellen

- [OpenOCD - On-Chip-Debugger](https://github.com/sysprogs/openocd)
- [SEGGER - J-Link](https://www.segger.com/products/debug-probes/j-link/)
- [Saleae Logic](https://www.saleae.com/)
- [Sigrok](https://sigrok.org/)
- [Bus Pirate](http://dangerousprototypes.com/docs/Bus_Pirate)
- [Great Scott Gadgets - HackRF](https://greatscottgadgets.com/hackrf/)
- [RTL-SDR](https://www.rtl-sdr.com/)
