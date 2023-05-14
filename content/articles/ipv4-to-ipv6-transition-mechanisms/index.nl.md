---
title: "Overgangsmechanismen van IPv4 naar IPv6: Een uitgebreide gids"
date: 2023-02-18
toc: true
draft: false
description: "Leer over de verschillende mechanismen die worden gebruikt voor de overgang van IPv4 naar IPv6 in deze uitgebreide gids."
tags: ["IPv4", "IPv6", "netwerken", "overgangsmechanismen", "dubbele stapel", "NAT64", "DNS64", "IPv6-tunneling", "ISATAP", "6to4", "DS-lite", "MAP-T", "IPv6-migratie", "netwerkprotocollen", "internetprotocol", "netwerkarchitectuur", "routing", "subnetting", "gericht op"]
cover: "/img/cover/A_cartoon_image_of_a_person_standing_at_a_crossroads.png"
coverAlt: "Een cartoonbeeld van een persoon die op een kruispunt staat, met een wegwijzer met IPv4- en IPv6-richtingen, die de keuze en de overgang tussen de twee protocollen voorstelt."
coverCaption: ""
---
 naar IPv6-overgangsmechanismen**

Naarmate het aantal aangesloten apparaten en de hoeveelheid internetverkeer blijft toenemen, raken de beschikbare IPv4-adressen in de wereld uitgeput. IPv6 werd geïntroduceerd om dit probleem op te lossen en is door veel netwerken overgenomen, maar de overgang naar IPv6 is nog in volle gang. In dit artikel zullen we de verschillende overgangsmechanismen onderzoeken die kunnen worden gebruikt om van IPv4 naar IPv6 te migreren.

## Inleiding

**IPv4** was het oorspronkelijke IP-adresformaat en is in gebruik sinds de begindagen van het internet. Het gebruikt 32-bits adressen en kan tot 4,3 miljard unieke adressen ondersteunen. Met de toename van het aantal aangesloten apparaten is dit aantal echter onvoldoende gebleken. **IPv6 daarentegen gebruikt 128-bits adressen en kan een bijna oneindig aantal unieke adressen ondersteunen. De overgang naar IPv6 is noodzakelijk om ervoor te zorgen dat het internet kan blijven groeien en evolueren.

## Overgangsmechanismen

### Dual Stack

Het meest eenvoudige overgangsmechanisme is om zowel IPv4 als IPv6 op hetzelfde netwerk te gebruiken. Dit staat bekend als **Dual Stack**. In een Dual Stack-netwerk zijn beide protocollen ingeschakeld op alle netwerkapparaten en kunnen ze met elkaar communiceren via beide protocollen. Deze aanpak maakt een geleidelijke migratie naar IPv6 mogelijk en zorgt voor een soepele overgang.

### Tunneling

**Tunneling** is een methode om IPv6-pakketten in te kapselen in IPv4-pakketten om ze over een IPv4-netwerk te transporteren. Dit mechanisme wordt gebruikt om connectiviteit te bieden tussen IPv6-eilanden die gescheiden zijn door een IPv4-netwerk. Bij tunneling wordt het IPv6-pakket ingekapseld in een IPv4-pakket, en het IPv4-netwerk routeert het naar het andere eind van de tunnel, waar het wordt ingekapseld en afgeleverd op de plaats van bestemming.

### Vertaling

**Vertaling** is een mechanisme dat wordt gebruikt om de communicatie tussen IPv4- en IPv6-netwerken te vergemakkelijken. Er zijn twee soorten vertaling: Network Address Translation-Protocol Translation (NAT-PT) en Address Family Transition Router (AFTR). **NAT-PT** vertaalt IPv6-pakketten naar IPv4-pakketten en omgekeerd, terwijl **AFTR** IPv6-connectiviteit biedt aan IPv4-only hosts.

### 6e

**IPv6 Rapid Deployment (6rd)** is een mechanisme dat een snelle invoering van IPv6 in een IPv4-netwerk mogelijk maakt. Bij 6rd wordt een IPv6-prefix ingekapseld in een IPv4-pakket en over het IPv4-netwerk verzonden. Het IPv6-pakket wordt vervolgens aan de andere kant ingekapseld en op de plaats van bestemming afgeleverd. Dit mechanisme is nuttig voor dienstverleners die IPv6 snel en efficiënt willen invoeren.

### DS-Lite

**Dual-Stack Lite (DS-Lite)** is een mechanisme dat wordt gebruikt om IPv6-connectiviteit te bieden aan IPv4-only netwerken. In DS-Lite wordt een IPv6-pakket ingekapseld in een IPv4-pakket en over het IPv4-netwerk verzonden. Aan het andere eind wordt het IPv6-pakket ingekapseld en op de plaats van bestemming afgeleverd. Dit mechanisme maakt een geleidelijke migratie naar IPv6 mogelijk zonder de IPv4-connectiviteit te verstoren.

### NAT64

**NAT64** is een mechanisme dat wordt gebruikt om IPv6-connectiviteit te bieden aan IPv4-only hosts. Bij NAT64 wordt een IPv6-pakket vertaald in een IPv4-pakket, dat over een IPv4-netwerk kan worden verzonden. Aan de andere kant wordt het IPv4-pakket weer vertaald in een IPv6-pakket en afgeleverd op de plaats van bestemming. Dit mechanisme is nuttig om IPv6-connectiviteit te bieden aan hosts die niet kunnen worden opgewaardeerd om IPv6 te ondersteunen.

______

Kortom, de overgang naar IPv6 is noodzakelijk om de verdere groei en evolutie van het internet te waarborgen. Terwijl de migratie naar IPv6 nog aan de gang is, zijn er verschillende overgangsmechanismen beschikbaar
