---
title: "Waarom Tailscale een relay gebruikt: directe verbindingen, DERP en peer-relays"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Lees waarom Tailscale een relay gebruikt, hoe je status- en netcheck-uitvoer leest en wanneer een DERP- of peer-relayverbinding onderzoek verdient."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "Tailscale-relay", "DERP", "Tailscale-peer-relay", "directe verbinding", "WireGuard", "NAT-traversal", "hard NAT", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "VPN-prestaties", "externe toegang", "tailnet", "homelabnetwerken", "relaylatentie", "end-to-end-versleuteling"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Twee laptops op afzonderlijke eilanden wisselen versleutelde pakketten uit via een centrale relay terwijl een directe route is onderbroken."
coverCaption: ""
---

**Tailscale gebruikt een relay** wanneer apparaten geen directe verbinding hebben gemaakt. Een korte DERP-verbinding tijdens het opstarten is normaal. Langdurig gebruik van een relay wijst vaak op NAT- of firewallomstandigheden die de route tussen de apparaten beïnvloeden. Directe verbindingen, DERP en peer-relays behouden allemaal de end-to-end-versleuteling van WireGuard. [Tailscale-verbindingstypen](https://tailscale.com/docs/reference/connection-types).

## Belangrijkste punten

- **Herken de route:** maak onderscheid tussen directe verbindingen, DERP en peer-relays.
- **Verzamel bewijs:** voer apparaatspecifieke probes en netwerkcontroles aan beide kanten uit.
- **Analyseer het patroon:** vergelijk apparaatparen en netwerkomstandigheden.
- **Kies een wijziging:** onderbouw die met een gemeten workload en een hertest.

## Voordat je begint

**Vereisten:** twee ingeschreven apparaten die online zijn en een terminal met de opdrachtregelinterface van Tailscale, oftewel **CLI**. Je hebt alleen beheerdersrechten nodig als het onderzoek tot configuratiewijzigingen leidt.

**Geschatte tijd:** vijf minuten voor basiscontroles en daarna 15–20 minuten voor de vergelijkingsoefening. **Moeilijkheid:** beginner voor observatie en gemiddeld voor netwerkwijzigingen. Beschrijf eerst het probleem, bijvoorbeeld een trage back-up of vertraagde terminalreactie.

## Direct, DERP en peer-relay

Een **tailnet** is je Tailscale-netwerk. De apparaten proberen directe UDP-connectiviteit tot stand te brengen. Relays zijn beschikbaar als de directe route mislukt. Tailscale controleert de verbindingsopties periodiek opnieuw. [Verbindingsopbouw](https://tailscale.com/docs/reference/connection-types).

| Route | Verkeersroute | Gebruikelijke betekenis |
|---|---|---|
| **Direct** | Tussen de twee apparaten | Gewoonlijk de voorkeursroute voor prestaties |
| **DERP-relay** | Via de relayinfrastructuur van Tailscale | Voegt een tussenstation toe wanneer directe toegang mislukt |
| **Peer-relay** | Via een geconfigureerd apparaat in je tailnet | Een alternatieve relay onder jouw beheer |

**DERP-prestaties** hangen deels af van de extra route en de gedeelde servicecapaciteit. Tailscale documenteert doorvoerlimieten om DERP-resources eerlijk te delen. Er bestaat geen universele relaysnelheid waarmee je de overdrachtstijd van bestanden kunt voorspellen. [Problemen met Tailscale-prestaties oplossen](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Begrijp de verbindingsonderhandeling

**NAT-traversal** is het proces waarbij een bruikbare route door adresvertalende apparaten tot stand komt. Tailscale begint de communicatie via DERP terwijl het een directe route probeert te onderhandelen. Als directe connectiviteit mislukt, biedt een beschikbare, geconfigureerde peer-relay een andere optie. Tailscale controleert de opties na verloop van tijd opnieuw. [Verbindingsopbouw](https://tailscale.com/docs/reference/connection-types).

**Hard NAT** beschrijft mappinggedrag dat traversal bemoeilijkt. De omstandigheden aan beide kanten zijn van belang. Twee apparaten achter verschillende routers gedragen zich niet noodzakelijk hetzelfde, ook niet als beide netwerken privé-adressen gebruiken. [Apparaatconnectiviteit](https://tailscale.com/docs/reference/device-connectivity).

Voor **een laptop die van netwerk wisselt** kan de route naar je homeserver veranderen nadat je van wifi thuis naar een hotelnetwerk gaat. Noteer welk netwerk je tijdens de observatie gebruikte. Een directe verbinding van gisteren zegt niets over de route van vandaag.

## Controleer je huidige verbinding

Vervang **`home-server`** door de Tailscale-naam of het adres van je peer:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** controleert de connectiviteit met de genoemde peer. **`tailscale status`** toont peers en verbindingsdetails. **`tailscale netcheck`** rapporteert omstandigheden op het apparaat waarop je de opdracht uitvoert. De [Tailscale CLI-referentie](https://tailscale.com/docs/reference/tailscale-cli) beschrijft deze opdrachten.

| Uitvoerindicator | Betekenis |
|---|---|
| **`direct`** | Verkeer naar deze peer gebruikt een directe route |
| **`relay`** | Verkeer naar deze peer gebruikt DERP |
| **`peer-relay`** | Verkeer gebruikt een geconfigureerde peer-relay |
| **Een eerste DERP-pong** | Bekijk de volgende resultaten voordat je beslist dat de route relayed bleef |

Deze labels komen uit de [documentatie over verbindingstypen](https://tailscale.com/docs/reference/connection-types). **Genereer eerst verkeer** en controleer daarna de peer die je onderzoekt. De opdrachten hierboven zijn voorbeelden, geen vastgelegde benchmarkresultaten.

## Interpreteer een routewijziging

Deze **illustratieve reeks** laat adressen en tijden weg, zodat de overgang van de verbinding centraal staat:

```text
Eerste antwoord:    via DERP
Later antwoord:     via een direct eindpunt
Status daarna:      direct
```

**Interpretatie:** tijdens deze observatie slaagde de onderhandeling. Op basis van alleen het eerste antwoord zou je de verkeerde diagnose stellen. Als latere antwoorden en de status relayed blijven, noteer dan een aanhoudende relay voor dit apparaatpaar en deze testperiode.

**Reikwijdte van de probe:** een geslaagde Tailscale-ping bevestigt connectiviteit met de peer voor die probe. De ping bewijst niet dat je dashboard, bestandsservice of SSH-daemon applicatieverkeer accepteert. Test de falende applicatie afzonderlijk voordat je concludeert dat het probleem is opgelost.

## Wat netcheck vertelt

Voer **`tailscale netcheck` op beide apparaten uit**. Vergelijk deze velden met de [referentie voor apparaatconnectiviteit](https://tailscale.com/docs/reference/device-connectivity):

| Veld | Nuttige interpretatie |
|---|---|
| **`UDP`** | Of de probe uitgaande UDP-connectiviteit heeft waargenomen |
| **`MappingVariesByDestIP`** | Wisselende externe mappings kunnen op lastige NAT-traversal wijzen |
| **`IPv6`** | Of dit apparaat bruikbare IPv6-connectiviteit heeft |
| **`PortMapping`** | Of een ondersteund mechanisme voor poortmapping beschikbaar is |

**Eén veld geeft geen definitief oordeel.** Een beschikbaar mappingmechanisme bewijst niet dat een route naar een bepaalde peer werkt. Een relaylabel wijst evenmin aan welke router de oorzaak is. Vergelijk beide eindpunten en de daadwerkelijke pingresultaten.

**Carrier NAT** is relevant wanneer upstream-adresvertaling buiten je beheer valt, zoals besproken in onze uitleg over [poortdoorschakeling bij T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/). Ga er niet van uit dat elke verbinding achter carrier NAT hetzelfde traversalgedrag vertoont.

## Vergelijk drie apparaatparen

Gebruik zo mogelijk een **derde ingeschreven apparaat** om het bewijs te verbeteren. Het volgende patroon is hypothetisch en geen gemeten resultaat:

| Apparaatpaar | Waargenomen route |
|---|---|
| **Laptop naar homeserver** | DERP |
| **Laptop naar een andere server** | Direct |
| **Homeserver naar een andere server** | DERP |

**Werkhypothese:** onderzoek eerst het netwerk van de homeserver, omdat beide waargenomen routes waarbij die server betrokken is via relay bleven lopen. Dit is een aanwijzing, geen bewijs. Elk paar onderhandelt afzonderlijk en de vergelijkingsserver heeft eigen netwerkomstandigheden.

**Volgende observatie:** verzamel netcheck-uitvoer op alle drie apparaten en herhaal de test van laptop naar homeserver vanaf een ander netwerk dat je beheert. Als de route verandert, noteer dan precies welk netwerk is gewijzigd. Schrijf het resultaat niet toe aan een bepaalde firewallinstelling voordat je die hebt getest.

**Oefening:** de verbinding van laptop naar homeserver is direct, maar een bestandsoverdracht blijft traag. Een relayverklaring past dan niet meer bij deze waarneming. Controleer de onderliggende uploadverbinding, serverbelasting, opslag en applicatiegedrag voordat je relayinstellingen wijzigt.

## Kies een gerichte wijziging

Begin met een **vergelijkingstest** op een ander netwerk dat je beheert. Als dezelfde peer daar direct bereikbaar wordt, heb je bruikbaar bewijs over de oorspronkelijke netwerkroute. Bekijk de UDP-beperkingen en NAT-configuratie voordat je ongerelateerde DNS- of applicatie-instellingen wijzigt.

**Wijzig één variabele**, voer de controles opnieuw uit en meet dezelfde workload. Noteer de overdrachtsrichting, bestandsgrootte, verstreken tijd en het verbindingstype. Zo kun je een verbeterde route onderscheiden van een losstaande wijziging in server- of opslagbelasting.

**Firewallwijzigingen** moeten aansluiten op platformspecifieke richtlijnen en het verzamelde bewijs. Een applicatiepoort openstellen op het publieke internet verbetert op zichzelf de transportroute van Tailscale niet. Beperk wijzigingen tot het vereiste verkeer en het netwerk dat je beheert. [Firewallrichtlijnen van Tailscale](https://tailscale.com/docs/integrations/firewalls).

| Bevinding | Wijziging om te beoordelen |
|---|---|
| **UDP-probe mislukt** | Bekijk uitgaande UDP-beperkingen op dit netwerk |
| **Mapping verschilt per bestemming** | Bekijk het NAT-gedrag op apparatuur die je beheert |
| **Directe route, trage applicatie** | Onderzoek de host, onderliggende verbinding en workload |
| **Werkende relay, aanvaardbare ervaring** | Behoud de configuratie en documenteer de basiswaarde |

*Geef de voorkeur aan een gemeten verbetering boven het wijzigen van instellingen om alleen een relaylabel te verwijderen.*

## Evalueer een peer-relay

Een **peer-relay** vereist een geschikte host, een bereikbaar UDP-poortnummer en een toegangsbeleid dat gebruik toestaat. Zowel de relay als de deelnemende clients moeten Tailscale 1.86 of later gebruiken. Controleer de ondersteunde hostplatforms voordat je een apparaat aanwijst. [Vereisten voor peer-relays](https://tailscale.com/docs/features/peer-relay).

**De plaatsing bepaalt het nut.** Een apparaat achter dezelfde ontoegankelijke netwerkgrens helpt andere peers niet voordat de relaypoort bereikbaar is.

**Onderhoudsafweging:** iemand moet de relay online, bijgewerkt en voldoende krachtig houden. Vergelijk die inspanning met het gemeten voordeel wanneer je Tailscale af en toe beheert en de latentie aanvaardbaar is. Meet bij herhaalde grote overdrachten eerst de workload via de voorgestelde relay.

## Controleer gedeelde verkeerseffecten

**Geaggregeerd verkeer** verdient aandacht wanneer een subnetrouter of exit-node meerdere workloads via DERP vervoert. Tailscale documenteert situaties waarin veel relayverkeer latencygevoelig verkeer op dezelfde verbinding vertraagt. [Problemen met hard NAT oplossen](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Vergelijkingsoefening:** observeer je interactieve sessie vóór, tijdens en na een grote back-up. Houd het apparaatpaar gelijk en noteer telkens de route. Vertraging die tijdens de overdracht ontstaat, rechtvaardigt onderzoek naar gedeelde belasting, maar bewijst de precieze oorzaak niet.

**Kies de volgende test** op basis van de waarneming. Controleer de linkverzadiging en hostbelasting. Evalueer daarna een directe route of het scheiden van latencygevoelige diensten als de topologie dit ondersteunt. Behandel een DNS-symptoom niet automatisch als bewijs van een DNS-configuratiefout.

## Is een relay een exit-node?

Een **exit-node** routeert het algemene internetverkeer van een client via een gekozen apparaat in het tailnet. Een relay vervoert verkeer tussen Tailscale-peers. Het selecteren van een exit-node garandeert geen directe route ernaartoe. [Documentatie over exit-nodes](https://tailscale.com/docs/features/exit-nodes).

## Maak een diagnoserapport

Bewaar een **kort voor-en-na-rapport** voor het werkelijke probleem:

```text
Datum en Tailscale-versies:
Bron- en doelapparaten:
Gebruikte netwerken per apparaat:
Eerste en uiteindelijke verbindingsroutes:
Netcheck-waarnemingen aan beide kanten:
Workload, richting en verstreken tijd:
Geteste enkele wijziging:
Resultaat van de hertest:
Besluit om te behouden of terug te draaien:
```

**Voltooiingscriterium:** het rapport verbindt een specifiek symptoom met waarnemingen, een hypothese en een gemeten hertest. “De relay is verdwenen” is onvolledig als de applicatie nog steeds traag is. “De back-up voldoet via DERP aan de tijdseis” is een geldig resultaat als de eis expliciet is.

**Gebruik `tailscale netcheck` als bewijs, niet als oordeel.** De opdracht beschrijft het netwerk zoals één apparaat dat ziet. De uiteindelijke route hoort bij een apparaatpaar en een workload. Leg beide eindpunten, de laatste `tailscale status`-regel en de applicatiemeting vast voordat je firewall- of NAT-instellingen wijzigt.

## Volgende stappen

Noteer de route naar je belangrijke peer en test de workload voordat je netwerkinstellingen wijzigt. Lees [Tailscale versus Headscale](/articles/tailscale-vs-headscale-comparison-guide/) voor de aparte vraag wie je coördinatie-infrastructuur beheert.
