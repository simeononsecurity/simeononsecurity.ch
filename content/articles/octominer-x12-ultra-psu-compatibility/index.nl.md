---
title: "Voedingscompatibiliteit van de Octominer X12 Ultra: praktijktest van Chicony en LiteOn"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Een test met vijf ventilatoren en drie voedingen in een Octominer X12 Ultra liet zien dat een Chicony-voeding het systeem startte, terwijl geteste LiteOn-units amberkleurig licht toonden en niet startten."
genre: ["Mininghardware", "Computerhardware"]
tags: ["Octominer X12 Ultra", "servervoeding", "voedingscompatibiliteit", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Abstracte illustratie van drie servervoedingen in een behuizing met groene, amberkleurige en grijze statuslampjes"
coverCaption: ""
---

**De Chicony R12-1K6P2A startte mijn Octominer X12 Ultra met vijf ventilatoren en drie voedingen.** De LiteOn PS-2142-2L-voedingen die ik testte, toonden groen licht, schakelden over naar amber en startten het systeem niet. Dit resultaat geldt voor mijn exemplaar met een **OCTOMINER (12PIN) 3x DPS1200 rev. 20**-voedingsbackplane. Een gelijk wattage of een vermelding op een lijst voor een afzonderlijke X12-breakoutkaart bewijst geen compatibiliteit met een Octominer-backplane.

De behuizing werd verkocht als een **3.600 W-configuratie** met drie voedingssleuven. [Octominer vermeldt een optie met drie voedingen van 1.200 W](https://octominer.eu/product/octominer-x12-ultra-used/) voor de X12 Ultra, naast andere configuraties. Controleer het label en de voedingskaart in je eigen systeem voordat je deze resultaten toepast.

## Testresultaten

| Voeding | Resultaat in dit systeem |
|---|---|
| **Chicony R12-1K6P2A, 1.600 W** | Startte het systeem tijdens mijn test. Dit artikel heeft geen langdurige belasting of werking in alle sleuven gemeten. |
| **LiteOn PS-2142-2L, 1.400 W** | Geteste exemplaren brandden groen en daarna amber. Het systeem startte niet. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | De ongebruikelijke AC-ingang maakte het lastig een passend snoer te vinden. Voor deze voeding heb ik in deze test geen start- of belastingsresultaat vastgelegd. |
| **HP HSTNS-PD30, 1.200 W** | Getest in hetzelfde systeem. Het startte niet. |
| **Andere HP Common Slot-units** | De geteste Platinum Plus-kits van 1.200 W en 750 W HSTNS-PD22B-, HSTNS-PL22B- en HSTNS-PD18-units startten dit systeem niet. De exacte modelnummers van de voedingen in de kits zijn niet vastgelegd. |

**Beschouw het LiteOn-resultaat niet als een storingsdiagnose voor elke PS-2142-2L.** De waargenomen reeks toont een mislukte start in deze behuizing. De test heeft het inschakelsignaal, de telemetrie-uitwisseling, de pinout van de backplane en een defect in een afzonderlijke voeding niet geïsoleerd. Het Chicony-resultaat bewijst evenmin meer dan een geslaagde start. Het bevestigt geen gecertificeerd vermogen van 4.800 W voor de behuizing of langdurige betrouwbaarheid.

## Welke Chicony startte dit systeem?

Het werkende model was **Chicony R12-1K6P2A**, ook vermeld als onderdeel **R1K6A002L** in de [compatibiliteitstabel van Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Het [80 PLUS-testrapport](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) vermeldt een voeding van 1.600 W, geschikt voor **200 tot 240 V AC**, 10 A en 50 tot 60 Hz. Het rapport mat 94,19% efficiëntie bij halve belasting onder de testcondities van 230 V. Deze cijfers beschrijven de geteste voeding, niet de volledige mininginstallatie.

De classificatie van **200 tot 240 V is belangrijk**. Ga er niet van uit dat dit model zijn nominale vermogen levert via een 120 V-stopcontact. Volgens een [onderdelenvermelding voor servers met exact dit model](https://www.itcreations.com/product/142080) heeft de geteste voeding een standaard C14-ingang. Gebruik snoeren en verdeelapparatuur die geschikt zijn voor de ingangsspanning en -stroom.

Mijn test bevestigde een geslaagde start met de Chicony op deze specifieke backplane. Dit bewijst geen compatibiliteit met elke X12 Ultra-revisie. Controleer het volledige modelnummer en het label van de voeding voordat je extra exemplaren bestelt.

## Waarom de LiteOn-vermelding misleidde

De **LiteOn PS-2142-2L** staat in de [X12-breakoutkaart-compatibiliteitstabel van Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Het [80 PLUS-rapport](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) vermeldt een model van 1.400 W. Deze bronnen bevestigen het model en de opgegeven toepassing met de **X12-adapter van Parallel Miner**. Geen van beide test de OEM-voedingskaart van Octominer.

Mijn PS-2142-2L-units veranderden na plaatsing van **groen naar amber**, waarna het systeem niet startte. Vergelijkbare uitgangsbladen bewijzen geen gelijk start-, status- of communicatiegedrag. De ledreeks alleen bewijst niet welk verschil de mislukte start veroorzaakte.

Dezelfde [tabel van Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) groepeert **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** en **Chicony R12-1K6P2A** onder de achtpins-adapterfamilie. **HP HSTNS-PD30** en verschillende HP Common Slot-voedingen van 750 W staan bij een andere familie met zespins-adapters. Geen van de HP-units die ik probeerde, startte dit systeem. De tabel beschrijft kaarten van Parallel Miner, geen vervangingslijst voor de **OCTOMINER (12PIN)**-backplane.

## Controleer stroom en bekabeling

De [probleemoplossingsgids voor de Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) vermeldt dat de behuizing alleen tot **200 W** verbruikt wanneer de ventilatoren op volle snelheid draaien. De gids adviseert minstens **10% vermogensreserve** en waarschuwt om niet boven **90% van het nominale vermogen van de geïnstalleerde voedingen** te komen. Houd rekening met GPU-vermogen, de behuizing en het werkelijke uitgangsvermogen van de voeding bij jouw AC-spanning.

**Een label van 1.600 W op elke Chicony-voeding verhoogt de gepubliceerde behuizingsconfiguratie van 3.600 W niet naar 4.800 W.** De backplane, interne bedrading, connectoren, AC-verdeling en koeling begrenzen het systeem ook. Ik heb deze grenzen op dit exemplaar niet gemeten. Houd het systeem binnen de gedocumenteerde configuratie totdat Octominer een hoger vermogen voor de exacte backplanerevisie bevestigt.

De Dell/Delta **D1200E-S0 / 0F37X3** had een ander probleem: de AC-ingang aan de voedingszijde vereiste een minder gangbaar passend snoer. Tijdens eerder onderzoek identificeerde ik de ingang als **LS-25** en de connector aan de snoerzijde als **LS-26**, op basis van de unit en snoervermeldingen. Controleer de connectorvorm en elektrische markeringen voordat je een snoer koopt. Een vertrouwde C13-stekker vervangt de juiste passende connector niet.

## Controleer je eigen X12

1. **Leg de exacte hardware vast.** Fotografeer het label van de behuizing en voeding, de AC-ingang, het uitgangsblad en de revisie van de voedingskaart. Tel de ventilatoren en voedingssleuven.
2. **Controleer de AC-voeding.** Vergelijk de ingangsspecificatie van de voeding met de specificaties van stopcontact, snoer en PDU. Het rapport van de Chicony R12-1K6P2A vermeldt 200 tot 240 V AC.
3. **Test een minimale configuratie.** Schakel uit en koppel alle AC-voedingen los voordat je een voeding, GPU of PSON-aansluiting verandert. [De gids van Octominer](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) adviseert de plaatsing en leds van de voeding te controleren, de zespins-PSON-kabel tussen moederbord en voedingskaart te inspecteren en één voeding met één GPU te gebruiken om een startprobleem te isoleren.
4. **Leg het resultaat vast.** Noteer model, sleuf, ledreeks, of de kaart en ventilatoren startten en of het systeem opstartte. Herhaal de test in andere sleuven pas na een veilige uitschakeling.
5. **Meet voordat je belasting toevoegt.** Controleer voedingstelemetrie en het vermogen aan het stopcontact onder de beoogde GPU-belasting. De starttest in dit artikel vervangt geen belastingstest.

## Conclusie

**De Chicony R12-1K6P2A is in deze vergelijking de enige vervanging waarvan een geslaagde start in mijn X12 Ultra met drie sleuven is gemeld.** De geteste LiteOn PS-2142-2L-units veranderden van groen naar amber en startten niet. De geteste HP Common Slot-units startten het systeem evenmin. Behandel andere voedingslijsten als onderzoekssuggesties totdat het exacte model en de Octominer-backplane een gecontroleerde start- en belastingstest doorstaan. Begin met de modellabels en de revisie van de backplane. Controleer de voedingsrichtlijnen van Octominer voordat je de GPU-belasting verhoogt.
