---
title: "Netzwerkgrundlagen: Was ist eine IP-Adresse und was sind IPv4 und IPv6?"
draft: false
toc: true
date: 2023-07-22
lastmod: 2026-11-20
description: "Erfahre, was IP-Adressen sind, worin sich IPv4 und IPv6 unterscheiden und warum die Einführung von IPv6 wichtig ist."
genre: ["Netzwerke", "IP-Adressen", "Internetprotokolle", "IPv4", "IPv6", "Netzwerkkommunikation", "Internetverbindung", "Technologie", "Netzwerkinfrastruktur", "Internetsicherheit"]
tags: ["IP-Adresse", "IPv4", "IPv6", "Internetprotokoll", "Netzwerke", "Adressraum", "Adressformat", "Adresskonfiguration", "Sicherheit", "Dienstgüte", "Internetverbindung", "Netzwerkinfrastruktur", "Technologie", "IPv4-Adressmangel", "Internetwachstum", "staatliche Vorschriften", "Netzwerkkommunikation", "Internetsicherheit", "Internet Assigned Numbers Authority", "IPv6-Vorgaben für Bundesbehörden", "dynamische Zuweisung", "DHCP", "IPsec", "QoS", "Netzwerk-Autokonfiguration", "Adresskomprimierung", "Adressnotation", "IP-Adressarten", "IP-Adressierungsschema"]
cover: "/img/cover/A_cartoon_image_of_two_devices_with_speech_bub.webp"
coverAlt: "Eine Zeichnung zweier Geräte mit Sprechblasen, die Daten austauschen und Netzwerkkommunikation darstellen"
coverCaption: "Mit IPv6 sicherst du dir eine reibungslose Internetverbindung und Wachstumsspielraum für die Zukunft."
---

## Netzwerkgrundlagen: Was ist eine IP-Adresse und was sind IPv4 und IPv6?

### Einleitung

In Netzwerken identifizieren IP-Adressen Geräte, die mit dem Internet verbunden sind, und ermöglichen ihre Kommunikation. Jedes Gerät mit Internetverbindung, etwa ein Computer, Smartphone oder Smart-Home-Gerät, erhält eine eindeutige IP-Adresse. Dieser Artikel erklärt IP-Adressen, den Unterschied zwischen IPv4 und IPv6 und die Bedeutung dieser Grundlagen für Privatpersonen und Unternehmen.

## IP-Adressen verstehen

### Was ist eine IP-Adresse?

Eine **IP-Adresse** (Internet Protocol-Adresse) ist eine numerische Kennzeichnung für jedes Gerät in einem Computernetzwerk. Sie erfüllt zwei Hauptaufgaben: Sie identifiziert den Host oder die Netzwerkschnittstelle und gibt den Standort des Geräts im Netzwerk an. IP-Adressen sind nötig, damit Geräte miteinander kommunizieren und Daten über das Internet austauschen.

IPv4-Adressen bestehen typischerweise aus vier durch Punkte getrennten Zahlengruppen, zum Beispiel 192.168.0.1. Jede Gruppe reicht von 0 bis 255. So ergeben sich insgesamt etwa 4,3 Milliarden eindeutige Kombinationen. Da immer mehr Geräte eine Internetverbindung nutzen, wird der IPv4-Adressraum knapp. Das führte zur Entwicklung von IPv6.

{{< youtube id="8zEVA-Bxs-0" >}}

### IPv4: der alte Standard

{{< youtube id="O48yc2nYBRA" >}}

IPv4, das **Internet Protocol Version 4**, ist die vierte Ausführung des Internetprotokolls und war viele Jahre das vorherrschende IP-Adressierungsschema im Internet. IPv4-Adressen sind 32 Bit lang und werden wie im Beispiel oben im Dezimalformat dargestellt: 192.168.0.1.

Die weltweite Verbreitung des Internets und die rasch wachsende Zahl verbundener Geräte haben die verfügbaren IPv4-Adressen aufgebraucht. Mit etwa 4,3 Milliarden eindeutigen Kombinationen reicht der Bestand für die steigende Zahl von Geräten weltweit nicht mehr aus.

### IPv6: die neue Generation

{{< youtube id="pUrdDelghwA" >}}

IPv6 (Internet Protocol Version 6) wurde entwickelt, um die Grenzen von IPv4 zu überwinden. **IPv6** verwendet 128-Bit-Adressen und bietet einen deutlich größeren Adressraum als IPv4. Statt des vertrauten Dezimalformats werden IPv6-Adressen hexadezimal geschrieben und durch Doppelpunkte getrennt, zum Beispiel 2001:0db8:85a3:0000:0000:8a2e:0370:7334.

Mit IPv6 steht praktisch eine unbegrenzte Zahl eindeutiger IP-Adressen zur Verfügung. So kann die Zahl der Geräte mit Internetverbindung weiter wachsen. IPv6 bietet weitere Vorteile, darunter bessere Sicherheit, mehr Unterstützung für Mobilfunknetze und verbesserte Netzwerk-Autokonfiguration.

### Wichtige Unterschiede zwischen IPv4 und IPv6

{{< youtube id="ThdO9beHhpA" >}}

#### Adressraum

Der wichtigste Unterschied zwischen IPv4 und IPv6 liegt im Adressraum. IPv4 stellt etwa 4,3 Milliarden eindeutige Adressen bereit. IPv6 bietet dagegen rund 3,4 × 10^38 eindeutige Adressen. Dieser große Adressraum erlaubt es dem Internet, weiter zu wachsen und immer mehr Geräte zu verbinden.

#### Adressformat

Auch das Format unterscheidet sich. IPv4-Adressen bestehen aus vier Dezimalzahlengruppen, IPv6-Adressen aus acht hexadezimalen Gruppen. IPv6-Adressen dürfen außerdem aufeinanderfolgende Nullen enthalten, die sich mit der Schreibweise "::" komprimieren lassen. Dadurch werden IPv6-Adressen kürzer und einfacher darstellbar.

#### Adresskonfiguration

IPv4-Adressen werden oft manuell oder dynamisch über das Dynamic Host Configuration Protocol (DHCP) zugewiesen. IPv6-Adressen verwenden häufig eine Kombination aus zustandsloser Autokonfiguration und DHCPv6 (Dynamic Host Configuration Protocol Version 6), um Adressen automatisch zuzuweisen und einzurichten.

#### Sicherheit und Dienstgüte

IPv6 verbessert Sicherheit und Dienstgüte gegenüber IPv4. Dazu gehört die Integration von IPsec (Internet Protocol Security), das Verschlüsselung und Authentifizierung für die Ende-zu-Ende-Kommunikation im Netzwerk bereitstellt. IPv6 unterstützt auch Dienstgüte-Mechanismen (QoS), mit denen sich bestimmte Arten von Netzwerkverkehr priorisieren lassen.

### Warum die Einführung von IPv6 wichtig ist

Der [Wechsel von IPv4 zu IPv6](https://simeononsecurity.com/articles/ipv4-to-ipv6-transition-mechanisms/) ist wichtig für das künftige Wachstum und die Nachhaltigkeit des Internets. Mit der steigenden Zahl verbundener Geräte wird der Mangel an IPv4-Adressen zu einem dringenden Problem. Privatpersonen und Unternehmen erhalten mit IPv6 eine zuverlässige Verbindung ihrer Geräte und können die erweiterten Funktionen des neuen Protokolls nutzen.

Auch Regierungen und Aufsichtsbehörden weltweit erkennen die Bedeutung von IPv6 und haben Initiativen und Vorschriften zur Unterstützung des Wechsels eingeführt. So erließ die US-Regierung 2020 eine Richtlinie, nach der alle Bundesbehörden IPv6 auf öffentlich erreichbaren Websites und Diensten aktivieren müssen.

## Fazit

IP-Adressen sind nötig, damit Geräte über das Internet kommunizieren und Daten austauschen. IPv4 und IPv6 sind zwei Versionen des Internetprotokolls. IPv4 ist der ältere Standard. IPv6 ist die neuere, besser skalierbare Lösung. Der Wechsel zu IPv6 ist entscheidend, damit das Internet weiter wachsen und immer mehr Geräte verbinden kann. Wenn du die Grundlagen der IP-Adressierung und die Unterschiede zwischen IPv4 und IPv6 kennst, kannst du fundierte Entscheidungen zu deiner Netzwerkinfrastruktur und künftigen Internetverbindung treffen.

## Quellen

- [RFC 791 - Internet Protocol](https://tools.ietf.org/html/rfc791)
- [RFC 2460 - Spezifikation des Internet Protocol Version 6 (IPv6)](https://tools.ietf.org/html/rfc2460)
- [Internet Assigned Numbers Authority (IANA) - IPv6-Adressraum](https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml)
