---
title: "Gast- en IoT-isolatie op een mesh-wifi-netwerk testen"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Controleer of de gast- en IoT-netwerken van je mesh-wifi toegang tot je thuisapparaten blokkeren. Test elk netwerk met een werkende dienst en leg de grenzen vast."
genre: ["Thuisnetwerken", "Wifi-beveiliging", "Slimme woningen"]
tags: ["mesh-wifi-gastnetwerk", "gastnetwerk-isolatietest", "IoT-netwerkisolatie", "mesh-wifi-beveiliging", "clientisolatie", "gast-wifi-test", "IoT-SSID", "accesspointmodus", "routermodus", "LAN-toegang", "lokaal-netwerktest", "Deco-gastnetwerk", "Orbi-gastnetwerk", "ASUS-gastnetwerk", "Google Nest-gast-wifi", "Test-NetConnection", "TCP-connectiviteitstest", "smart-home-netwerk", "draadloze clientisolatie", "thuisnetwerksegmentatie"]
cover: "/img/cover/mesh-wifi-guest-iot-isolation-test.webp"
coverAlt: "Een huis met twee verdiepingen, twee meshrouters, gasttelefoons, IoT-lampen en camera’s, en een schild dat de route naar een vertrouwde laptop en NAS blokkeert."
coverCaption: "Test routes tussen gast, IoT en het hoofdnetwerk afzonderlijk."
---

Een aparte wifi-naam laat niet zien welke apparaten met elkaar communiceren. Een mesh-systeem behandelt het **gastnetwerk**, het **IoT-netwerk** en **draadloze clientisolatie** mogelijk als afzonderlijke instellingen. Deze handleiding helpt je routes op je eigen apparatuur te testen zonder aan te nemen dat het label van een fabrikant je beleid beschrijft.

<!--more-->

## Belangrijkste punten

- **Controleer eerst of het doel werkt:** bereik een bekende dienst vanaf het hoofdnetwerk voordat je een geblokkeerde route test.
- **Test elke grens:** gast naar hoofdnetwerk, IoT naar hoofdnetwerk en gast naar gast beantwoorden verschillende vragen.
- **Leg de configuratie vast:** model, firmware, router- of accesspointmodus en aangesloten mesh-node beïnvloeden de interpretatie.
- **Test opnieuw na wijzigingen:** een goed resultaat geldt alleen voor de geteste apparaten, dienst, adresfamilie en configuratie.

## Voor je begint

Trek ongeveer 20 minuten uit. Je hebt een laptop nodig die verbinding kan maken met je hoofd-, gast- en IoT-wifi. Ook heb je een vertrouwd apparaat op het hoofdnetwerk nodig met een **bekende open TCP-dienst**, zoals de webinterface van een NAS. Een TCP-dienst luistert op een genummerde poort, zoals poort 443 van een NAS-webpagina. Gebruik een dienst die van jou is of die je beheert. Noteer het lokale adres en de poort, maar publiceer ze niet. Laat de dienst tijdens de hele test actief.

Noteer het mesh-model, de firmwareversie, de bedrijfsmodus en de instellingen voor gasttoegang, IoT-toegang, gedeelde apparaten en clientisolatie. Controleer na elke wifi-wissel de wifi-naam van de laptop. Verbreek voor deze test van het lokale pad de VPN- of proxyverbinding als je normale beleid dit toestaat. Herstel die daarna. Een VPN verandert de route die je test.

> **Waarschuwing:** test alleen je eigen apparaten of apparaten die je mag beheren. De aanmeldpagina van de router is geen goede vervanging voor een host op het hoofdnetwerk, omdat gatewaytoegang andere regels volgt.

Een **lokaal netwerk (LAN)** is je privé-thuisnetwerk. **IoT**, of het Internet of Things, omvat apparaten zoals camera’s, luidsprekers en slimme stekkers. **Clientisolatie** blokkeert direct verkeer tussen apparaten op één wifi-netwerk.

## Bepaal de grens

Kies het gewenste resultaat voordat je een instelling wijzigt. Internettoegang en lokale toegang zijn afzonderlijke resultaten.

| Route | Vraag | Voorbeeld van verwacht resultaat |
|---|---|---|
| **Gast naar hoofd-LAN** | Is een computer of NAS bereikbaar? | Geblokkeerd, tenzij je een uitzondering koos |
| **IoT naar hoofd-LAN** | Zijn privéapparaten bereikbaar? | Afhankelijk van product en beleid |
| **Gast naar gast** | Zijn twee gasten bereikbaar voor elkaar? | Afhankelijk van clientisolatie |
| **Gast naar gedeeld apparaat** | Werkt een gedeelde printer of display? | Alleen toegestaan als bedoeld |
| **Gast naar internet** | Is een gewone openbare website bereikbaar? | Toegestaan als het gastbeleid internet omvat |

Deze rijen zijn afzonderlijke tests. TP-Links [Deco-handleiding voor apparaatisolatie](https://www.tp-link.com/us/support/faq/3968/) zegt dat geïsoleerde apparaten internettoegang en communicatie met andere geïsoleerde apparaten behouden, terwijl toegang tot apparaten op het hoofdnetwerk wordt geblokkeerd. ASUS beschrijft in de [handleiding voor AP-isolatie](https://www.asus.com/us/support/faq/1044821/) een draadloze peercontrole en merkt op dat een route via een upstream bekabelde router buiten die controle valt. **Eén geblokkeerde route bewijst niet dat alle andere grenzen werken.**

## Mesh-instellingen controleren

Zoek de functie die de te testen grens beheert. Menunamen en beschikbaarheid verschillen per model en firmware.

| Mesh-instelling | Wat je controleert |
|---|---|
| **TP-Link Deco-gastnetwerk** | De [routermodus isoleert gasten van het hoofdnetwerk](https://www.tp-link.com/us/support/faq/1460/). Controleer in accesspointmodus **Allow Local Access**. |
| **ASUS-gastprofiel** | [Access Intranet](https://www.asus.com/uk/support/faq/1009857/) beheert toegang tot het hoofdnetwerk in ondersteunde profielen. |
| **Google Nest-gast-wifi** | Controleer de lijst met [gedeelde apparaten](https://support.google.com/googlehome/answer/6327302?hl=en) voordat je verwacht dat een printer of display verborgen blijft. |
| **IoT-netwerk of apparaatisolatie** | Controleer of het product een afzonderlijke isolatie-instelling biedt. Een IoT-wifi-naam bepaalt de toegangsregel niet. |

Bij Deco vereist [apparaatisolatie](https://www.tp-link.com/us/support/faq/3968/) ondersteuning van de hoofdunit en satellietunits. Noteer welke node je testlaptop bedient. Ontbreekt een functie, raadpleeg dan de documentatie voor het exacte model en de firmware. Ga niet uit van dezelfde app-weergave als bij iemand anders.

## Stel een positieve controle in

Verbind de Windows-testlaptop met de **hoofd-wifi**. Controleer of de gekozen dienst vanaf die laptop werkt. Voer in PowerShell het adres van de host op het hoofdnetwerk en de bekende open poort in wanneer daarom wordt gevraagd:

```powershell
$targetAddress = Read-Host "Main-network test host address"
$targetPort = [int](Read-Host "Known open TCP port")
Test-NetConnection -ComputerName $targetAddress -Port $targetPort
```

Microsofts [Test-NetConnection-documentatie](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) definieert `-ComputerName` en `-Port` als een test voor een specifieke host en TCP-dienst. Noteer `TcpTestSucceeded`. Stel hier eerst `True` vast voordat je een latere `False` interpreteert. Faalt de test op het hoofdnetwerk, dan ligt het probleem mogelijk bij de dienst, het adres, de hostfirewall of de laptopconfiguratie. Los eerst de test op het hoofdnetwerk op.

Gebruik je een telefoon of een ander besturingssysteem, open dan dezelfde bekende dienst in de browser of app. Gebruik bij het wisselen van wifi exact dezelfde dienst en hetzelfde doeladres. Een lijst met ontdekte apparaten levert zwakker bewijs op, omdat ontdekking en directe TCP-toegang verschillende routes volgen.

## Gast- en IoT-toegang testen

Verbind dezelfde laptop met de **gast-wifi**. Controleer de wifinaam. Open een openbare website als internettoegang deel uitmaakt van je gastbeleid. Voer dezelfde opdracht `Test-NetConnection` opnieuw uit zonder `$targetAddress` of `$targetPort` te wijzigen. Noteer het resultaat.

Ga terug naar het hoofdnetwerk en controleer of de dienst nog steeds `True` oplevert. Faalt de hoofdtest nu, dan is de gasttest niet beslissend. Verbind daarna dezelfde laptop met de **IoT-wifi**, als je systeem laptopverbinding toestaat, en herhaal de test. Neem niet aan dat het IoT-resultaat gelijk is aan het gastresultaat. Een geslaagde verbinding van IoT naar het hoofdnetwerk betekent dat de gekozen lokale TCP-dienst in deze configuratie bereikbaar was vanaf het IoT-netwerk.

Wil je gasten onderling isoleren, gebruik dan twee apparaten die je beheert op het gastnetwerk. Test vanaf het ene apparaat een bekende dienst op het andere. Noteer dit apart van gasttoegang tot het hoofdnetwerk. Test ook de bedoelde uitzondering als een gedeelde printer of display moet werken. Cloudbediening van een slim apparaat bewijst geen direct lokaal pad.

Herhaal de gast-naar-hoofdtest bij elke mesh-node. Controleer in de app welke node je laptop bedient als de app dit meldt. **IPv6** is de nieuwere Internet Protocol-adresfamilie en gebruikt adressen van 128 bits. Ondersteunt de hoofdhost IPv6 en slaagt de positieve controle over IPv6, herhaal dan dezelfde adresfamilietest vanaf gast- en IoT-wifi. Een test met alleen IPv4 dekt geen IPv6-route.

## Een verschil interpreteren

| Waarneming | Volgende controle |
|---|---|
| **Hoofdnetwerk en gastnetwerk falen beide** | Controleer de doeldienst, het adres, de poort en de hostfirewall. Isolatie is niet aangetoond. |
| **Hoofdnetwerk en gastnetwerk slagen beide** | Controleer lokale gasttoegang, uitzonderingen voor gedeelde apparaten en router- versus accesspointmodus. |
| **Hoofdnetwerk slaagt, gastnetwerk faalt** | Leg bewijs vast voor dit doel en deze TCP-route. Test andere routes die je beleid vereist. |
| **Gast geblokkeerd, IoT slaagt** | Controleer of de IoT-naam een compatibiliteitsnetwerk aanduidt zonder overeenkomstige isolatieregel. |
| **Gast naar hoofdnetwerk geblokkeerd, gast naar gast slaagt** | Controleer draadloze clientisolatie afzonderlijk. |

Een mislukte **ping** beantwoordt de TCP-vraag niet. Een hostfirewall blokkeert mogelijk ping maar accepteert de gekozen dienst. Een mislukte TCP-test is ook beperkt: die zegt niets over andere poorten, apparaten, IPv6 of uitzonderingen voor gedeelde apparaten. Gebruik een verschil als reden om de ingestelde regel te controleren en de gecontroleerde test te herhalen.

## Het resultaat herstellen en vastleggen

Wijzig telkens één instelling. Controleer op een Deco in accesspointmodus **Allow Local Access**. Controleer bij een ASUS-gastprofiel **Access Intranet**. Verwijder op Google Nest Wifi een onbedoeld item uit **Shared devices**. Bepaal bij lokale smart-homebediening eerst welk apparaat welke dienst moet bereiken voordat je een uitzondering toevoegt. Een **VLAN** is een logisch netwerk dat via gedeelde hardware wordt vervoerd. Het [VLAN-segmentatieplan](/articles/homelab-vlan-segmentation-plan/) van de site behandelt beheerde netwerken wanneer een mesh voor consumenten niet de benodigde toegangsregel biedt.

Leg mesh-model, firmware, bedrijfsmodus, node, wifinaam, bronapparaat, doeldienst, adresfamilie, verwacht resultaat, werkelijk resultaat en de ene wijziging vast. Publiceer geen privéadressen of netwerkwachtwoorden. Herhaal dezelfde tests na firmware-updates, nodewijzigingen of een wissel tussen router- en accesspointmodus.

Kies je nog apparatuur, vergelijk dan de functies in de [koopgids voor mesh-wifi](/articles/best-wifi-mesh-system-for-consumers/). Gebruik daarna deze procedure om het geïnstalleerde netwerk te controleren. **Een label of app-schakelaar is een bewering. Een positieve controle en een hertest onder dezelfde omstandigheden leveren bewijs voor precies de route die je belangrijk vindt.**

## Volgende stappen

Herhaal de isolatietests na wijzigingen van firmware, nodes of bedrijfsmodus. Gebruik het [VLAN-segmentatieplan](/articles/homelab-vlan-segmentation-plan/) als mesh-instellingen de vereiste grens niet halen.
