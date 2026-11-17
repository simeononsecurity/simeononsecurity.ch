---
title: "Netzwerkgrundlagen: Subnetze, Subnetzbildung und VLAN-Design"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Erfahren Sie mehr über Subnetze, Subnetzbildung und VLANs für eine effiziente Netzwerkverwaltung und höhere Sicherheit."
genre: ["Netzwerkgrundlagen", "Subnetzbildung", "VLANs", "Netzwerkverwaltung", "Netzwerksicherheit", "IP-Adressierung", "Netzwerksegmentierung", "Effiziente Ressourcennutzung", "Netzwerkleistung", "IPv4"]
tags: ["Netzwerkgrundlagen", "Subnetze", "subnetzbildung", "VLANs", "Netzwerkverwaltung", "Netzwerksicherheit", "IP-Adressierung", "Netzwerksegmentierung", "effiziente Ressourcennutzung", "Netzwerkleistung", "IPv4", "Subnetzkonfiguration", "Subnetzmasken", "IP-Adresszuweisung", "VLAN-übergreifende Kommunikation", "Switchports", "VLAN-Konfiguration", "VLAN-Schnittstellen", "Netzwerkverbindung", "Teilnetze", "Broadcast-Domänen", "Sicherheitsmaßnahmen", "IP-Adressbereich", "Subnetzbeispiele", "VLAN-Bereitstellung", "Netzwerkadministration", "Switchkonfiguration", "Routerkonfiguration", "Netzwerkskalierbarkeit", "Kommunikation und Datenübertragung", "effiziente Netzwerke"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Symbolische Darstellung verbundener Computernetzwerke mit Subnetzen und VLANs"
coverCaption: "Effiziente Netzwerke aufbauen: Subnetze und VLANs einfach erklärt."
---

## Netzwerkgrundlagen: Subnetze, Subnetzbildung und VLAN-Design

### Einführung

In unserer vernetzten Welt sind Computernetzwerke entscheidend für Kommunikation und Datenübertragung. Netzwerkgrundlagen sind für IT-Fachleute und alltägliche Nutzer wichtig. Dieser Artikel erklärt Subnetze, Subnetzbildung und VLANs sowie ihren Zweck und ihre Funktionsweise.

## Subnetze: genauer erklärt

### Was ist ein Subnetz?

{{< youtube id="nR5xCmXJE5E" >}}

Ein **Subnetz** ist eine logische Unterteilung eines IP-Netzwerks. So kann ein Administrator ein großes Netzwerk in kleinere, leichter verwaltbare Segmente teilen. Jedes Subnetz hat einen eigenen IP-Adressbereich. Das erleichtert die effiziente Nutzung verfügbarer IP-Adressen.

### Warum Subnetze verwenden?

Computernetzwerke verwenden Subnetze aus mehreren Gründen:

1. **Netzwerksegmentierung:** Subnetze teilen ein großes Netzwerk in kleinere Teilnetze. Das verbessert die Leistung und reduziert Überlastungen.

2. **Mehr Sicherheit:** Getrennte Subnetze ermöglichen den Einsatz von Firewalls und Zugriffskontrolllisten, um den Datenverkehr zu steuern und die Netzwerksicherheit zu erhöhen.

3. **Ressourcen effizient nutzen:** Subnetzbildung verteilt IP-Adressen besser. IPv4-Adressen sind begrenzt verfügbar.

### Wie unterteilt man ein Netzwerk?

{{< youtube id="LdSAaSHfK3M" >}}

Bei der Subnetzbildung wird ein Netzwerk in kleinere Subnetze geteilt. Gehen Sie so vor:

1. **Netzwerkanforderungen bestimmen:** Ermitteln Sie die benötigte Anzahl an Subnetzen und Hosts pro Subnetz.

2. **IP-Adressierungsschema wählen:** Wählen Sie ein passendes Schema anhand der benötigten Subnetze und Hosts.

3. **Subnetzmasken berechnen:** Bestimmen Sie die Masken anhand der Anzahl benötigter Subnetze und Hosts.

4. **IP-Adressen zuweisen:** Weisen Sie jedem Subnetz Adressen zu und prüfen Sie, ob sie in den richtigen Bereich fallen.

5. **Testen und prüfen:** Testen Sie die Netzwerkverbindung und prüfen Sie die IP-Zuweisungen.

### Beispiele für die Subnetzbildung

Ein einfaches Beispiel veranschaulicht die Subnetzbildung:

Angenommen, wir haben den IP-Adressbereich 192.168.0.0/24 und möchten vier Subnetze mit gleich vielen Hosts erstellen. So teilen wir das Netzwerk auf:

1. **Schritt 1: Netzwerkanforderungen bestimmen:** Wir benötigen vier Subnetze mit gleich vielen Hosts.

2. **Schritt 2: IP-Adressierungsschema wählen:** Wir wählen eine /26-Maske. Damit sind 64 Adressen pro Subnetz möglich.

3. **Schritt 3: Subnetzmasken berechnen:** Die Maske für /26 lautet 255.255.255.192.

4. **Schritt 4: IP-Adressen zuweisen:** Wir weisen den Subnetzen folgende IP-Adressen zu:

   - Subnetz 1: 192.168.0.0/26
   - Subnetz 2: 192.168.0.64/26
   - Subnetz 3: 192.168.0.128/26
   - Subnetz 4: 192.168.0.192/26

5. **Schritt 5: Testen und prüfen:** Wir prüfen die Netzwerkverbindung zwischen Geräten innerhalb jedes Subnetzes.

### Nützliche Tabellen zur Subnetzbildung

#### Referenztabelle zur Subnetzberechnung

| Subnetzmaske | CIDR-Notation | IP-Adressen gesamt | Nutzbare IP-Adressen |
|-------------|---------------|--------------------|---------------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /19 | 255.255.224.0 | 8,192 | 8,190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32,768 | 32,766 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /15 | 255.254.0.0 | 131,072 | 131,070 |
| /14 | 255.252.0.0 | 262,144 | 262,142 |
| /13 | 255.248.0.0 | 524,288 | 524,286 |
| /12 | 255.240.0.0 | 1,048,576 | 1,048,574 |
| /11 | 255.224.0.0 | 2,097,152 | 2,097,150 |
| /10 | 255.192.0.0 | 4,194,304 | 4,194,302 |
| /9 | 255.128.0.0 | 8,388,608 | 8,388,606 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /7 | 254.0.0.0 | 33,554,432 | 33,554,430 |
| /6 | 252.0.0.0 | 67,108,864 | 67,108,862 |
| /5 | 248.0.0.0 | 134,217,728 | 134,217,726 |
| /4 | 240.0.0.0 | 268,435,456 | 268,435,454 |
| /3 | 224.0.0.0 | 536,870,912 | 536,870,910 |
| /2 | 192.0.0.0 | 1,073,741,824 | 1,073,741,822 |
| /1 | 128.0.0.0 | 2,147,483,648 | 2,147,483,646 |
| /0 | 0.0.0.0 | 4,294,967,296 | 4,294,967,294 |

#### Tabelle nutzbarer Subnetze

| CIDR-Notation | Anzahl nutzbarer Subnetze |
|---------------|-------------------------|
| /0 | 1 |
| /1 | 2 |
| /2 | 4 |
| /3 | 8 |
| /4 | 16 |
| /5 | 32 |
| /6 | 64 |
| /7 | 128 |
| /8 | 256 |
| /9 | 512 |
| /10 | 1024 |
| /11 | 2048 |
| /12 | 4096 |
| /13 | 8192 |
| /14 | 16384 |
| /15 | 32768 |
| /16 | 65536 |
| /17 | 131072 |
| /18 | 262144 |
| /19 | 524288 |
| /20 | 1048576 |
| /21 | 2097152 |
| /22 | 4194304 |
| /23 | 8388608 |
| /24 | 16777216 |
| /25 | 33554432 |
| /26 | 67108864 |
| /27 | 134217728 |
| /28 | 268435456 |
| /29 | 536870912 |
| /30 | 1073741824 |
| /31 | 2147483648 |
| /32 | 4294967296 |

#### Tabelle der Zweierpotenzen

| Zweierpotenz | Wert |
|--------------|-------|
| 2^32 | 4294967296 |
| 2^31 | 2147483648 |
| 2^30 | 1073741824 |
| 2^29 | 536870912 |
| 2^28 | 268435456 |
| 2^27 | 134217728 |
| 2^26 | 67108864 |
| 2^25 | 33554432 |
| 2^24 | 16777216 |
| 2^23 | 8388608 |
| 2^22 | 4194304 |
| 2^21 | 2097152 |
| 2^20 | 1048576 |
| 2^19 | 524288 |
| 2^18 | 262144 |
| 2^17 | 131072 |
| 2^16 | 65536 |
| 2^15 | 32768 |
| 2^14 | 16384 |
| 2^13 | 8192 |
| 2^12 | 4096 |
| 2^11 | 2048 |
| 2^10 | 1024 |
| 2^9 | 512 |
| 2^8 | 256 |
| 2^7 | 128 |
| 2^6 | 64 |
| 2^5 | 32 |
| 2^4 | 16 |
| 2^3 | 8 |
| 2^2 | 4 |
| 2^1 | 2 |
| 2^0 | 1 |

## VLANs: virtuelle lokale Netzwerke

### Was ist ein VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

Ein **VLAN (Virtual Local Area Network)** ist eine logische Gruppe von Geräten in einem Netzwerk, unabhängig von ihrem physischen Standort. VLANs schaffen getrennte Broadcast-Domänen und verbessern Flexibilität, Sicherheit und Skalierbarkeit.

### Warum VLANs verwenden?

VLANs bieten mehrere Vorteile für die Netzwerkverwaltung:

1. **Mehr Sicherheit:** VLANs isolieren vertrauliche Daten und beschränken unbefugten Zugriff. Der Datenverkehr bleibt in festgelegten Segmenten und schützt wichtige Ressourcen.

2. **Bessere Leistung:** VLANs trennen den Netzwerkverkehr logisch, verringern Überlastungen und verbessern die Leistung. Broadcasts bleiben auf das VLAN beschränkt.

3. **Einfachere Verwaltung:** VLANs gruppieren Geräte nach Funktion, Abteilung oder anderen Kriterien und vereinfachen so Administration und Konfiguration.

### VLAN-Konfiguration

Für die Konfiguration eines VLANs sind meist folgende Schritte nötig:

1. **VLAN-Anforderungen ermitteln:** Bestimmen Sie Zweck und Umfang der Bereitstellung. Legen Sie die Zuordnung der Geräte zu VLANs fest.

2. **VLAN-IDs zuweisen:** Vergeben Sie für jedes VLAN eine eindeutige ID. VLAN-IDs sind meist Zahlen von 1 bis 4094. Einige IDs sind reserviert.

3. **Switchports konfigurieren:** Weisen Sie Switchports den passenden VLANs zu. Konfigurieren Sie sie als Access- oder Trunk-Port.

4. **VLAN-Schnittstellen konfigurieren:** Wenn VLAN-übergreifende Kommunikation nötig ist, [konfigurieren Sie VLAN-Schnittstellen](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/), etwa auf einem Layer-3-Switch oder Router.

5. **Testen und prüfen:** Testen Sie die Verbindung zwischen Geräten innerhalb jedes VLANs.

### Tabelle reservierter VLANs

| VLAN-Tags | Beschreibung |
|-------------------|----------------------------------------------------|
| VLAN 0 | Reservierte VLAN-ID, nicht verwenden |
| VLAN 1 | Standard-VLAN vieler Netzwerkgeräte |
| VLAN 2 | Standard-VLAN für Verwaltungsverkehr |
| VLAN 3-4 | Reservierte VLAN-IDs |
| VLAN 5 | Für Token-Ring-VLAN-ID reserviert |
| VLAN 6-1001 | Reservierte VLAN-IDs |
| VLAN 1002-1005 | Cisco-Standard-VLANs für bestimmte Zwecke |
| VLAN 1006-1024 | Reservierte VLAN-IDs |
| VLAN 1025-4094 | Für den erweiterten VLAN-Bereich reserviert |
| VLAN 4095 | Reservierte VLAN-ID, nicht verwenden |

## Fazit

[Subnetze zu verstehen](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) und VLANs zu kennen ist wichtig, um effiziente Computernetzwerke zu planen und zu verwalten. Subnetze segmentieren Netzwerke und verbessern Leistung und Sicherheit. VLANs gruppieren Geräte logisch und erhöhen Flexibilität und Verwaltung. Mit den beschriebenen Schritten können Administratoren Netzwerke passend unterteilen und VLANs konfigurieren.

Netzwerkgrundlagen bilden das Fundament für robuste, skalierbare Netzwerke, die moderne Kommunikation und Datenübertragung unterstützen.

## Referenzen

- [Subnetting-Grundlagen](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [VLANs verstehen und konfigurieren](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [IEEE 802.1Q-Norm](https://standards.ieee.org/standard/802_1Q-2018.html)
