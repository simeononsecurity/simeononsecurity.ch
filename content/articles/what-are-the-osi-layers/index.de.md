---
title: "Grundlagen der Netzwerktechnik: Verstehen der OSI-Schichten und des TCP-IP-Modells"
draft: false
toc: true
date: 2023-07-22
description: "Gewinnen Sie ein umfassendes Verständnis der OSI-Schichten und des TCP-IP-Modells, die für Netzwerke unerlässlich sind, um eine effektive Kommunikation und Fehlersuche zu ermöglichen."
genre: ["Grundlagen der Netzwerkarbeit", "OSI Layers", "TCP IP-Modell", "Netzwerk-Protokolle", "Kommunikationsmodelle", "Grundlagen der Netzwerkarbeit", "Datenübertragung", "Netzwerk-Fehlerbehebung", "Netzarchitektur", "Vernetzungskonzepte"]
tags: ["OSI-Schichten", "TCP-IP-Modell", "Netzwerk-Grundlagen", "Netzwerkprotokolle", "Kommunikationsmodelle", "Datenübertragung", "Netzwerk-Fehlersuche", "Netzarchitektur", "Netzwerkkonzepte", "Netzwerk-Grundlagen", "Netzwerk-Frameworks", "Erklärung von Netzwerkprotokollen", "Vernetzungsstandards", "physikalische Schicht", "Datenverbindungsschicht", "Netzwerkschicht", "Transportschicht", "Sitzungsschicht", "Präsentationsschicht", "Anwendungsschicht", "TCP-IP-Schichten", "Netzwerkschnittstellenschicht", "Internetschicht", "Transportschicht", "Anwendungsschicht", "Netzwerkprotokolle erklärt", "Netzwerkmodelle", "Netzwerk-Grundlagen erklärt", "Netzwerk-Leitfaden", "Netzwerk-Tutorial", "bewährte Netzwerkpraktiken"]
cover: "/img/cover/An_animated_illustration_showcasing_a_network.png"
coverAlt: "Eine animierte Illustration, die ein Netz miteinander verbundener Knotenpunkte zeigt, zwischen denen Daten fließen, und die effiziente Kommunikation und Vernetzung symbolisiert."
---
 Grundlagen der Netzwerktechnik: Die OSI-Schichten und das TCP-IP-Modell verstehen

### Einführung

In der Welt der Netzwerke ist das Verständnis der Protokolle und Modelle, die die Kommunikation regeln, unerlässlich. Zwei weit verbreitete Rahmenwerke sind das **OSI-Modell (Open Systems Interconnection)** und das **TCP IP-Modell (Transmission Control Protocol/Internet Protocol)**. Diese Modelle bieten einen strukturierten Ansatz für die Vernetzung und dienen als Grundlage für den Aufbau und die Fehlersuche bei Netzwerksystemen. In diesem Artikel werden die OSI-Schichten und das TCP-IP-Modell in klarer und prägnanter Form erläutert.

## Die OSI-Schichten

Das **OSI-Modell** ist ein konzeptioneller Rahmen, der beschreibt, wie Netzwerkprotokolle zusammenwirken und die Kommunikation zwischen verschiedenen Systemen ermöglichen. Es besteht aus sieben Schichten, von denen jede ihre eigenen Zuständigkeiten hat.


| OSI-Schicht | Schichtenbeschreibung | Beispiele | Protokolle | Standards |
|----------------|---------------------------------------------------------------|---------------------|------------------------------------------------|---------------------------------------------|
| Physikalische Schicht | Beschäftigt sich mit der physikalischen Übertragung von Daten | Kabel, Anschlüsse | Ethernet, USB, HDMI | IEEE 802.3, USB 3.0 |
| Data Link Layer | Sorgt für die zuverlässige Übertragung von Daten zwischen benachbarten Knoten | Switches, NICs | Ethernet, Wi-Fi (802.11), PPP | IEEE 802.3, IEEE 802.11, RFC 1662 |
| Netzwerkschicht | Leitet Datenpakete über verschiedene Netzwerke hinweg | Router | IP, ICMP, ARP | IPv4 (RFC 791), IPv6 (RFC 2460), ARP (RFC 826)|
| Transportschicht | Bietet zuverlässige End-to-End-Datenübertragung | Gateways | TCP, UDP | TCP (RFC 793), UDP (RFC 768) |
| Sitzungsschicht | Verwaltet Kommunikationssitzungen zwischen Anwendungen | NetBIOS | NetBIOS, SIP | RFC 1001, RFC 1002, RFC 3261 |
| Präsentationsschicht | Beschäftigt sich mit Syntax und Semantik des Informationsaustauschs | SSL, HTTP | SSL/TLS, HTTP | SSL/TLS (RFC 5246), HTTP (RFC 2616) |
| Anwendungsschicht | Interagiert direkt mit Endbenutzeranwendungen | Webbrowser, E-Mail-Clients | HTTP, FTP, SMTP, DNS | HTTP (RFC 2616), FTP (RFC 959), SMTP (RFC 5321), DNS (RFC 1035) |

{{< youtube id="0y6FtKsg6J4" >}}

Schauen wir uns die einzelnen Ebenen im Detail an:

### Schicht 1: Physikalische Schicht

Die **Physikalische Schicht** ist die unterste Schicht des OSI-Modells und befasst sich mit der **physikalischen Übertragung** von Daten über ein Netzwerk. Sie definiert die **Hardware-Komponenten**, wie z. B. Kabel, Anschlüsse und Netzwerkschnittstellen, die **binäre Signale (0s und 1s)** übertragen. Beispiele für Protokolle auf dieser Schicht sind **Ethernet, USB und HDMI**.

### Schicht 2: Datenverbindungsschicht

Die **Datenverbindungsschicht** ist für die **zuverlässige Übertragung** von Daten zwischen benachbarten Netzwerkknoten, wie Switches und Netzwerkschnittstellenkarten (NICs), zuständig. Sie gewährleistet eine **fehlerfreie Übertragung** und bietet Mechanismen zur **Flusskontrolle** und **Fehlererkennung**. Zu den gängigen Protokollen auf dieser Schicht gehören **Ethernet, Wi-Fi (802.11) und Point-to-Point Protocol (PPP)**.

### Schicht 3: Netzwerkschicht

Die **Netzwerkschicht** ist für die **Weiterleitung von Datenpaketen** über verschiedene Netzwerke zuständig. Sie bestimmt den **optimalen Pfad** für die Datenübertragung auf der Grundlage von Netzbedingungen und Adressierungsschemata. Das **Internetprotokoll (IP)** ist ein grundlegendes Protokoll auf dieser Schicht und weist den Geräten **eindeutige IP-Adressen** zur Identifizierung und für das Routing zu.

### Schicht 4: Transportschicht

Die **Transportschicht** gewährleistet eine **zuverlässige und effiziente End-to-End-Datenübertragung** zwischen Anwendungen, die auf verschiedenen Geräten laufen. Sie stellt **Verbindungen** her, **segmentiert Daten** in kleinere Einheiten (falls erforderlich) und bietet Mechanismen zur **Fehlerbehebung** und **Flusskontrolle**. Das **Transmission Control Protocol (TCP)** und das **User Datagram Protocol (UDP)** sind die am häufigsten verwendeten Transportprotokolle.

### Schicht 5: Sitzungsschicht

Die **Sitzungsschicht** verwaltet die **Kommunikationssitzungen** zwischen Anwendungen, die auf verschiedenen Geräten laufen. Sie baut diese Sitzungen auf, unterhält und beendet sie und ermöglicht den **Datenaustausch** zwischen Prozessen. Diese Schicht ist für die **Synchronisation** und die **Dialogsteuerung** zuständig. Beispiele für Protokolle auf dieser Schicht sind **NetBIOS** und **Session Initiation Protocol (SIP)**.

### Schicht 6: Präsentationsschicht

Die **Präsentationsschicht** befasst sich mit der **Syntax und Semantik** der zwischen Systemen ausgetauschten Informationen. Sie stellt sicher, dass die Daten für eine sichere Übertragung ordnungsgemäß **formatiert**, **codiert** und **verschlüsselt** werden. Diese Schicht ist für die **Datenkomprimierung**, die **Verschlüsselung** und die **Protokollumsetzung** zuständig. Beispiele für Protokolle auf dieser Schicht sind **Secure Sockets Layer (SSL)** und **Hypertext Transfer Protocol (HTTP)**.

### Schicht 7: Anwendungsschicht

Die **Anwendungsschicht** ist die oberste Schicht des OSI-Modells und interagiert direkt mit **Endbenutzeranwendungen**. Sie bietet Dienste, die die **Benutzerkommunikation** und den **Datenaustausch** ermöglichen. Beispiele für Protokolle auf dieser Schicht sind **HTTP**, **FTP**, **SMTP** und **DNS**.

## Das TCP-IP-Modell

Während das OSI-Modell einen konzeptionellen Rahmen bildet, ist das TCP-IP-Modell die eigentliche Protokollsuite, die im Internet verwendet wird. Es besteht aus vier Schichten, die mit bestimmten Schichten des OSI-Modells übereinstimmen.


| TCP IP Schichten | Schichtenbeschreibung | Beispiele | Protokolle |
|---------------------|---------------------------------------------------------------|---------------------|-------------------------------------------------|
| Netzwerkschnittstellenschicht | Verantwortlich für die physikalische Übertragung von Daten | Netzwerkkarten, Ethernet-Kabel | Ethernet, Wi-Fi (802.11) |
| Internetschicht | Verantwortlich für Adressierung, Routing und Fragmentierung von Daten | Router | IP, ICMP, ARP |
| Transportschicht | Sorgt für zuverlässige und verbindungsorientierte Kommunikation | Gateways | TCP, UDP |
| Anwendungsschicht | Stellt die Schnittstelle zwischen Anwendungen und Protokollen dar | Webbrowser, E-Mail-Clients | HTTP, FTP, SMTP, DNS |

{{< youtube id="OTwp3xtd4dg" >}}

Lassen Sie uns diese Schichten erforschen:

### Schicht 1: Netzwerk-Schnittstellenschicht

Die **Netzwerkschnittstellenschicht** entspricht der Kombination aus der **Physikalischen** und der **Datenverbindungsschicht** im OSI-Modell. Sie wickelt die physische Übertragung von Daten über das Netz ab und stellt Protokolle für die Datenübertragungssteuerung bereit.

### Schicht 2: Internet-Schicht

Die **Internetschicht** entspricht der **Netzwerkschicht** im OSI-Modell. Sie umfasst das IP-Protokoll, das für die **Adressierung**, das **Routing** und die **Fragmentierung** von Datenpaketen für die Übertragung über Netzwerke zuständig ist.

### Schicht 3: Transportschicht

Die **Transportschicht** im TCP-IP-Modell entspricht der **Transportschicht** im OSI-Modell. Sie bietet **zuverlässige** und **verbindungsorientierte** Kommunikation mit dem **TCP**-Protokoll oder **leichtgewichtige, verbindungslose** Kommunikation mit dem **UDP**-Protokoll.

### Schicht 4: Anwendungsschicht

Die **Anwendungsschicht** im TCP-IP-Modell umfasst die Funktionalität der **Sitzungs-**, **Präsentations-** und **Anwendungsschicht** im OSI-Modell. Sie stellt die Schnittstelle zwischen Anwendungen und den zugrunde liegenden Netzwerkprotokollen dar.

## Schlussfolgerung

Das Verständnis der **OSI-Schichten** und des **TCP-IP-Modells** ist für jeden, der sich mit Netzwerken beschäftigt, von entscheidender Bedeutung. Diese Modelle bieten einen Rahmen, um zu verstehen, wie Netzwerke funktionieren und welche Protokolle die Kommunikation erleichtern. Indem sie die Funktionen jeder Schicht verstehen, können **Netzwerkadministratoren** und **Ingenieure** Probleme effektiv beheben und robuste Netzwerksysteme entwerfen.


Referenzen:
- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [TCP IP model](https://www.geeksforgeeks.org/tcp-ip-model/)
- [Ethernet](https://www.computernetworkingnotes.com/networking-tutorials/ethernet-standards-and-protocols-explained.html)
- [Wi-Fi](https://www.wi-fi.org/)
- [IP address](https://en.wikipedia.org/wiki IP_address)
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [User Datagram Protocol](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)
- [NetBIOS](https://en.wikipedia.org/wiki/NetBIOS)
- [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)
- [Hypertext Transfer Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
- [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)
