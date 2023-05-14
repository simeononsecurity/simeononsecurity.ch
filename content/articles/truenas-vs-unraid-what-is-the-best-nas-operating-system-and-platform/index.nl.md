---
title: "Unraid vs TrueNas: Welk NAS-besturingssysteem is geschikt voor u?"
date: 2023-02-16
toc: true
draft: false
description: "Een uitgebreide vergelijking van Unraid en TrueNas, inclusief hun gebruiksvriendelijkheid, functies, documentatie en gemeenschap, om gebruikers te helpen een geïnformeerde beslissing te nemen over welk NAS-besturingssysteem het beste is voor hun behoeften."
tags: ["Unraid", "TrueNas", "NAS-besturingssysteem", "Vergelijking", "Gebruiksvriendelijkheid", "Kenmerken", "Documentatie", "Gemeenschap", "Open Bron", "Onderneming", "Gegevensbescherming", "Prestaties", "Flexibiliteit", "Gemakkelijk te gebruiken", "Toepassingen van derden"]
cover: "/img/cover/Two_computer_servers_facing_each_other_one_blue_one_green.png"
coverAlt: "Twee servers tegenover elkaar, één blauw, één groen. Aan de blauwe kant staat een persoon met een helm en veiligheidsvest. Aan de groene kant zit een persoon op de bank."
coverCaption: ""
---

Als het gaat om **het bouwen van een network-attached storage (NAS) systeem, zijn twee van de meest bekende besturingssystemen voor x86-gebaseerde computers TrueNas en Unraid**. Beide bieden krachtige functies voor het beheren van een NAS-systeem, maar hun voornaamste verschil ligt in hun methode voor opslagbeheer.

In dit artikel vergelijken we TrueNas en Unraid om u te helpen de beste beslissing voor uw behoeften te nemen.

## Overzicht van Unraid

**Unraid is een eigen NAS-besturingssysteem ontwikkeld door Lime Technology**, een softwarebedrijf uit Californië. Het is opgericht in 2005 en draait op het Linux platform. Het doel van Unraid is om RAID-technologie toegankelijker te maken door de beperkingen op schijfgrootte, snelheid, merk en protocol op te heffen. Dit maakt eenvoudige uitbreiding van RAID-arrays mogelijk en minimaliseert het risico van gegevensverlies.

______

## Inleiding tot TrueNas

**TrueNas, voorheen bekend als FreeNas, is een open-source NAS-besturingssysteem ontwikkeld door iXsystems**, een privébedrijf gevestigd in San Jose, Californië. Het werd gelanceerd in 2005 en is gebouwd op FreeBSD en Linux. De ontwikkelaars van TrueNas concentreren zich op de bedrijfsmarkt en de keuze van het standaard bestandssysteem (OpenZFS) weerspiegelt deze focus.

______

## Kosten

**Huisgebruikers die op zoek zijn naar het beste NAS-besturingssysteem maken zich vaak zorgen over de kosten**. In dit opzicht is TrueNas een duidelijke winnaar omdat het open-source is en volledig gratis, tenminste voor TrueNas CORE, de versie gericht op thuisgebruikers en niet-kritische opslagtoepassingen.

Unraid daarentegen is niet gratis, maar hanteert een eerlijk prijsmodel zonder abonnementen of verborgen kosten. U kunt kiezen uit drie Unraid-plannen, die alleen verschillen in het aantal opslagapparaten dat kan worden aangesloten. Het Basis-plan kost $59, het Plus-plan kost $89, en het Pro-plan kost $129.

______

## Gebruiksvriendelijkheid

**Unraid legt sterk de nadruk op gebruiksgemak en flexibiliteit**. Het heeft een uniek storage management systeem waarmee gebruikers verschillende diskgroottes en types kunnen mixen en matchen en schijven kunnen toevoegen of verwijderen zonder enige onderbreking. Het biedt ook een duidelijke en eenvoudige gebruikersinterface, waardoor het zelfs voor niet-technische gebruikers gemakkelijk is om een NAS-systeem op te zetten en te beheren.

**TrueNas, daarentegen, is gericht op de zakelijke markt en vereist meer geavanceerde kennis om in te stellen en te beheren**. De keuze voor het OpenZFS-bestandssysteem biedt geavanceerde functies voor gegevensbescherming, zoals snapshots, gegevenscompressie en checksumming om de integriteit van de gegevens te garanderen.

______

## Functies

**Zowel TrueNas als Unraid bieden ondersteuning** voor NFS-shares, SMB voor Windows en AFP voor macOS en iOS. Daarnaast biedt TrueNas iSCSI diensten, LDAP, Active Directory en Kerberos. Unraid biedt deze diensten niet, maar ondersteunt wel Docker-containers, waardoor gebruikers toegang krijgen tot een breed scala aan toepassingen.

**TrueNas heeft ook ingebouwde ondersteuning voor cloudopslagdiensten** zoals Amazon S3, Google Cloud en Microsoft Azure, waardoor het gemakkelijk is om gegevens naar de cloud te verplaatsen. Gebruikers van Unraid kunnen oplossingen van derden gebruiken, maar deze vereisen mogelijk extra installatie en configuratie.

**Het op Linux gebaseerde platform van Unraid maakt het ook mogelijk virtuele machines te configureren** met behulp van KVM en PCI/USB-apparaten, zoals grafische kaarten, toe te wijzen aan virtuele machines. Dit maakt het mogelijk om dezelfde computer te gebruiken voor zowel media center als gaming doeleinden.

**TrueNas bevat zijn eigen containerisatie-technologie**, Jails, en zijn eigen virtualisatie-optie, Bhyve. Hoewel TrueNas veel van de populaire toepassingen van derden aanbiedt, zoals Plex, kan de totale selectie van software kleiner zijn in vergelijking met Unraid.

______

## Documentatie en gemeenschap

TrueNas heeft een uitgebreide Documentation Hub, die alles omvat van setup tot API's en hardware platforms. De Unraid website heeft een minder uitgebreide documentatie sectie, maar is gemakkelijker te navigeren. Unraid heeft echter geen individuele ondersteuningspagina, maar gebruikers worden aangemoedigd om vragen te stellen op het officiële community forum, dat wordt beschreven als vriendelijk, informatief en behulpzaam.

TrueNas heeft ook zijn eigen officiële community forum, maar het is misschien niet zo gastvrij voor beginners als het Unraid forum. Dit komt omdat veel TrueNas-gebruikers IT-professionals zijn die zich richten op enterprise storage management.

______

## Conclusie

Zowel TrueNas als Unraid zijn krachtige en volwassen NAS-besturingssystemen, elk met hun eigen sterke en zwakke punten. TrueNas is ideaal voor mensen met geavanceerde kennis van opslagbeheer en die de geavanceerde gegevensbeschermingsfuncties van OpenZFS willen. Unraid, aan de andere kant, is het beste voor thuisgebruikers die een flexibel en gemakkelijk te gebruiken NAS-systeem willen.

Samengevat:

**TrueNas Voordelen:**
- Gratis en open-source
- Geavanceerde gegevensbescherming met OpenZFS
- Goede prestaties

**TrueNas Nadelen:**
- Moeilijker te gebruiken
- Onvriendelijke gemeenschap

**Unraid Voordelen:**
- Gemakkelijk te gebruiken
- Grote verscheidenheid aan toepassingen van derden
- Vriendelijke gemeenschap

**Unraid Nadelen:**
- Beperkte prestaties

Uiteindelijk zal de beslissing tussen TrueNas en Unraid afhangen van uw specifieke behoeften en uw niveau van technische expertise. Overweeg uw eisen, vergelijk de kenmerken en voordelen van elk en neem een weloverwogen beslissing.
