---
title: "Netwerkbasis: subnetten, indeling van subnetten en VLAN-ontwerp"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Leer de basis van subnetten, indeling van subnetten en VLAN’s voor efficiënt netwerkbeheer en betere beveiliging."
genre: ["Netwerkbasisprincipes", "Subnetverdeling", "VLAN’s", "Netwerkbeheer", "Netwerkbeveiliging", "IP-adressering", "Netwerksegmentatie", "Efficiënt gebruik van bronnen", "Netwerkprestaties", "IPv4"]
tags: ["netwerkbasisprincipes", "subnetten", "subnetverdeling", "VLAN’s", "netwerkbeheer", "netwerkbeveiliging", "IP-adressering", "netwerksegmentatie", "efficiënt gebruik van bronnen", "netwerkprestaties", "IPv4", "subnetconfiguratie", "subnetmaskers", "IP-adrestoewijzing", "communicatie tussen VLAN’s", "switchpoorten", "VLAN-configuratie", "VLAN-koppelvlakken", "netwerkverbinding", "subnetwerken", "broadcastdomeinen", "beveiligingsmaatregelen", "IP-adresbereik", "subnetvoorbeelden", "VLAN-implementatie", "netwerkbeheer", "switchconfiguratie", "routerconfiguratie", "netwerkschaalbaarheid", "communicatie en gegevensoverdracht", "efficiënte netwerken"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Een symbolische afbeelding van verbonden computernetwerken met subnetten en VLAN’s"
coverCaption: "Efficiënte netwerken bouwen: subnetten en VLAN’s eenvoudig uitgelegd."
---

## Netwerkbasis: subnetten, indeling van subnetten en VLAN-ontwerp

### Inleiding

In de verbonden wereld van vandaag spelen computernetwerken een belangrijke rol bij communicatie en gegevensoverdracht. Kennis van netwerkbasisprincipes is nuttig voor IT-professionals en gewone gebruikers. Dit artikel behandelt subnetten, indeling van subnetten en VLAN’s, met uitleg over hun doel en werking.

## Subnetten: een nadere uitleg

### Wat is een subnetwerk?

{{< youtube id="nR5xCmXJE5E" >}}

Een **subnetwerk** is een logische onderverdeling van een IP-netwerk. Een netwerkbeheerder kan zo een groot netwerk opdelen in kleinere, beter beheersbare segmenten. Elk subnetwerk heeft een eigen IP-adresbereik. Dat helpt beschikbare IP-adressen efficiënt te gebruiken.

### Waarom subnetten gebruiken?

Computernetwerken gebruiken subnetten om verschillende redenen:

1. **Netwerksegmentatie:** Subnetten verdelen een groot netwerk in kleinere subnetwerken. Dat verbetert de prestaties en vermindert congestie.

2. **Betere beveiliging:** Door apparaten in aparte subnetten te plaatsen, kunnen beheerders firewalls en toegangsbeheerlijsten inzetten om verkeer te sturen en de beveiliging te verbeteren.

3. **Efficiënt gebruik van bronnen:** indeling van subnetten verdeelt IP-adressen beter. IPv4-adressen zijn beperkt beschikbaar.

### Hoe maak je subnetten?

{{< youtube id="LdSAaSHfK3M" >}}

indeling van subnetten deelt een netwerk op in kleinere subnetten. Volg hiervoor deze stappen:

1. **Bepaal de netwerkvereisten:** Bepaal hoeveel subnetten en hosts per subnetwerk nodig zijn.

2. **Kies een IP-adresseringsschema:** Kies een geschikt schema op basis van het benodigde aantal subnetten en hosts.

3. **Bereken subnetmaskers:** Bepaal de subnetmaskers aan de hand van het aantal vereiste subnetten en hosts.

4. **Wijs IP-adressen toe:** Ken IP-adressen aan elk subnetwerk toe en controleer of ze binnen het juiste bereik vallen.

5. **Test en controleer:** Test de netwerkverbinding en controleer de IP-toewijzingen om de configuratie te valideren.

### Voorbeelden van indeling van subnetten

Bekijk dit eenvoudige voorbeeld van indeling van subnetten:

Stel dat we het IP-adresbereik 192.168.0.0/24 hebben en vier subnetten met evenveel hosts willen maken. Zo kunnen we dit netwerk opdelen:

1. **Stap 1: Bepaal de netwerkvereisten:** We hebben vier subnetten met evenveel hosts nodig.

2. **Stap 2: Kies een IP-adresseringsschema:** We kiezen een subnetmasker van /26. Daarmee zijn 64 adressen per subnetwerk mogelijk.

3. **Stap 3: Bereken subnetmaskers:** Bij een /26-subnetmasker hoort het masker 255.255.255.192.

4. **Stap 4: Wijs IP-adressen toe:** We wijzen de volgende IP-adressen aan de subnetten toe:

   - subnetwerk 1: 192.168.0.0/26
   - subnetwerk 2: 192.168.0.64/26
   - subnetwerk 3: 192.168.0.128/26
   - subnetwerk 4: 192.168.0.192/26

5. **Stap 5: Test en controleer:** We controleren de netwerkverbinding tussen apparaten binnen elk subnetwerk.

### Handige subnettingtabellen

#### Referentietabel voor subnetberekeningen

| Subnetmasker | CIDR-notatie | Totaal aantal IP-adressen | Bruikbare IP-adressen |
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

#### Tabel met bruikbare subnetten

| CIDR-notatie | Aantal bruikbare subnetten |
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

#### Tabel met machten van twee

| Macht van twee | Waarde |
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

## VLAN’s: virtuele lokale netwerken

### Wat is een VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

Een **VLAN (Virtual Local Area Network)** is een logische groep apparaten binnen een netwerk, ongeacht hun fysieke locatie. VLAN’s vergroten de flexibiliteit, beveiliging en schaalbaarheid van een netwerk doordat ze afzonderlijke broadcastdomeinen maken.

### Waarom VLAN’s gebruiken?

VLAN’s bieden verschillende voordelen voor netwerkbeheer:

1. **Betere beveiliging:** VLAN’s kunnen gevoelige gegevens isoleren en onbevoegde toegang beperken. Verkeer blijft binnen bepaalde segmenten, zodat onbevoegde gebruikers geen toegang krijgen tot belangrijke bronnen.

2. **Betere prestaties:** VLAN’s scheiden netwerkverkeer logisch. Dat vermindert congestie en verbetert de prestaties. Broadcastverkeer blijft binnen het VLAN en beperkt onnodig netwerkverkeer.

3. **Eenvoudiger netwerkbeheer:** VLAN’s groeperen apparaten op functie, afdeling of een ander logisch criterium. Dat vereenvoudigt beheer en configuratie.

### VLAN-configuratie

Voor het configureren van een VLAN worden doorgaans deze stappen gevolgd:

1. **Bepaal de VLAN-vereisten:** Bepaal het doel en de omvang van de VLAN-implementatie. Noteer welke apparaten in welke VLAN’s komen.

2. **Wijs VLAN-ID’s toe:** Ken elk VLAN een unieke ID toe. VLAN-ID’s zijn meestal nummers van 1 tot en met 4094. Sommige ID’s zijn gereserveerd.

3. **Configureer switchpoorten:** Wijs switchpoorten aan de juiste VLAN’s toe. Stel een poort in als accesspoort of trunkpoort.

4. **Configureer VLAN-interfaces:** Als communicatie tussen VLAN’s nodig is, [configureer VLAN-interfaces](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/), bijvoorbeeld op een layer 3-switch of router.

5. **Test en controleer:** Test de verbinding tussen apparaten binnen elk VLAN om de configuratie te valideren.

### Tabel met gereserveerde VLAN’s

| VLAN-tags | Beschrijving |
|-------------------|----------------------------------------------------|
| VLAN 0 | Gereserveerde VLAN-ID, niet gebruiken |
| VLAN 1 | Standaard-VLAN voor veel netwerkapparaten |
| VLAN 2 | Standaard-VLAN voor beheerstransport |
| VLAN 3-4 | Gereserveerde VLAN-ID’s |
| VLAN 5 | Gereserveerd voor Token Ring-VLAN-ID |
| VLAN 6-1001 | Gereserveerde VLAN-ID’s |
| VLAN 1002-1005 | Standaard-VLAN’s die Cisco voor specifieke doelen gebruikt |
| VLAN 1006-1024 | Gereserveerde VLAN-ID’s |
| VLAN 1025-4094 | Gereserveerd voor uitgebreid VLAN-bereik |
| VLAN 4095 | Gereserveerde VLAN-ID, niet gebruiken |

## Conclusie

[Inzicht in subnetten](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) en VLAN’s is belangrijk voor het ontwerpen en beheren van efficiënte computernetwerken. Subnetten segmenteren netwerken en verbeteren prestaties en beveiliging. VLAN’s groeperen apparaten logisch en verbeteren flexibiliteit en beheer. Met de stappen in dit artikel kunnen netwerkbeheerders subnetten maken en VLAN’s configureren voor hun vereisten.

Netwerkbasisprincipes vormen de basis voor robuuste, schaalbare netwerken die voldoen aan de eisen van moderne communicatie en gegevensoverdracht.

## Bronnen

- [Basisprincipes van subnetting](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [VLAN’s begrijpen en configureren](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [IEEE 802.1Q-standaard](https://standards.ieee.org/standard/802_1Q-2018.html)
