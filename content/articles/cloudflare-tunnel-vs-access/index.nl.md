---
title: "Cloudflare Tunnel versus Access: heb je beide nodig?"
date: 2026-09-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Leer het verschil tussen Cloudflare Tunnel en Access, kies bescherming voor een thuisdashboard en voorkom dat je een privéapp zonder authenticatie publiceert."
genre: ["Netwerkbeveiliging", "Zelf hosten", "Cloudbeveiliging"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel versus Access", "Cloudflare Zero Trust", "cloudflared", "zelf gehoste applicaties", "homelabbeveiliging", "externe toegang", "identiteitsprovider", "toegangsbeleid", "applicatieauthenticatie", "publieke hostnaam", "beveiliging van de origin", "uitgaande tunnel", "servicetokens", "Service Auth", "MFA", "privédashboard", "omgekeerde proxy", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Een thuisserver maakt via een transparante doorgang verbinding met een cloudgateway met een afzonderlijk identiteitscontrolepunt."
coverCaption: ""
---

**Cloudflare Tunnel** verbindt je applicatie met Cloudflare. **Cloudflare Access** bepaalt wie er toegang toe krijgt. Gebruik beide voor een privéthuisdashboard dat via een publieke hostnaam bereikbaar is. Een werkende tunnel voegt zelf geen identiteitscontrole toe. [Cloudflares handleiding voor het publiceren van applicaties](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) legt dit verschil uit.

## Belangrijkste punten

- **Leg de route uit:** onderscheid de connector, origin en identiteitscontrole.
- **Configureer een beleid:** geef specifieke mensen toegang tot één privédashboard.
- **Evalueer de bescherming:** test toegestane, geweigerde en alternatieve toegangsroutes.
- **Ontwerp toegang:** documenteer afzonderlijke eisen voor bezoekers en automatisering.

## Voordat je begint

**Doelgroep:** eigenaren van een homeserver die willen bepalen hoe ze een browserdashboard beveiligen. Het voorbeeld gaat uit van een actief domein op Cloudflare, een werkende lokale webapplicatie en toestemming om beide te beheren. **Geschatte inspanning:** 20–30 minuten voor de beleidsoefening nadat de connector is ingesteld. **Moeilijkheid:** beginner tot gemiddeld.

**Leesroute:** begin met de productrollen, volg één aanvraag en configureer en controleer daarna een klein beleid. Sluit af met een toegangspecificatie voor je eigen dienst.

## Wat elk product doet

De **origin** is de server waarop je applicatie draait. De connector **`cloudflared`** start verbindingen vanuit je infrastructuur naar Cloudflare, zodat de origin geen publiek routeerbaar IP-adres nodig heeft. Aanvragen en antwoorden reizen vervolgens via de bestaande verbinding. [Overzicht van Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Vraag | Tunnel | Access |
|---|---|---|
| **Hoe bereikt Cloudflare mijn server?** | Brengt de verbinding tot stand | Vervangt de verbinding met de origin niet |
| **Wie krijgt toegang?** | Levert zelf geen gebruikerslogin | Beoordeelt de ingestelde toegangsbeleidsregels |
| **Wat configureer ik?** | Connector en applicatieroute | Applicatie, identiteitsprovider en beleidsregels |
| **Wat bewijst succes?** | De origin is via de route bereikbaar | Een aanvraag voldeed aan het ingestelde beleid |

Een **identiteitsprovider (IdP)** verifieert de bezoeker. Een **Access-beleidsregel** bepaalt een actie en de voorwaarden waaraan moet worden voldaan. Allow geeft passende gebruikers toegang. Bypass schakelt Access-handhaving uit voor passend verkeer. [Naslag voor Access-beleid](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Volg één browseraanvraag

Voor **`dashboard.example.com`** is de logische aanvraagroute:

```text
Webbrowser -> Cloudflare Access -> tunnelverbinding -> cloudflared -> beheerpaneel
                      |
                      +-> identiteitsprovider wanneer authenticatie nodig is
```

De **connector start de tunnelverbinding naar buiten** vanuit je netwerk. Browseraanvragen reizen daarna via deze bestaande verbinding naar de origin. Een uitgaande verbinding die inkomende applicatieaanvragen draagt, is de belangrijkste reden waarom Tunnel werkt zonder een gewone doorgestuurde poort op de origin. [Verbindingsmodel van Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Applicatierechten** zijn een aparte beslissing. Toegang tot een dashboard bepaalt niet automatisch wie de instellingen mag wijzigen of gegevens mag verwijderen. Als de applicatie kijkers- en beheerdersrollen heeft, configureer en test die rollen afzonderlijk.

Een **gezinslid met alleen kijkrechten** moet bijvoorbeeld de back-upstatus kunnen zien, terwijl jij de bestemmingen wilt kunnen wijzigen. Leg deze eisen vast voordat je identiteiten kiest. Twee mensen die dezelfde Access-controle doorstaan, horen niet automatisch dezelfde applicatierechten te krijgen.

## Wanneer je beide nodig hebt

**Het publiek bepaalt de bescherming.** Vergelijk deze opties voordat je een route publiceert:

| Beoogd publiek | Voorgestelde inrichting | Controleer vóór gebruik |
|---|---|---|
| **Iedereen die een openbare website leest** | Tunnel indien nodig voor verbinding met de origin | Openbare toegang is bewust gekozen |
| **Jij en enkele gezinsleden** | Tunnel plus Access | Sta alleen de bedoelde identiteiten toe |
| **Een bestaande openbare origin** | Access met afzonderlijke originbescherming | Directe toegang tot de origin mag de controle niet omzeilen |
| **Een gepland script** | Tunnel plus een Service Auth-beleidsregel | De client ondersteunt de authenticatiemethode |

**Access zonder Tunnel** werkt ook met een origin die al bereikbaar is. Beveilig ook alternatieve routes naar de server. Cloudflare adviseert om eerst de Access-applicatie te maken wanneer je een nieuwe tunnelroute publiceert. [Vereisten voor zelf gehoste applicaties](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*Gebruik Tunnel plus Access voor een privéthuisdashboard dat je via een publieke hostnaam bereikt.*

## Configureer een dashboardbeleid

Gebruik deze **uitgewerkte configuratie** voor twee beoogde bezoekers. Vervang beide voorbeeldadressen door identiteiten die je beheert. Maak de Access-applicatie voordat je de publieke tunnelroute toevoegt.

1. **Applicatie:** open Zero Trust → Access controls → Applications en maak een zelf gehoste applicatie met een publieke hostnaam.
2. **Hostnaam:** voer de aparte dashboardhostnaam in. Laat het pad onbeperkt voor dit voorbeeld dat de hele hostnaam gebruikt.
3. **Beleid:** maak een Allow-beleid met de naam `Dashboard viewers`.
4. **Identiteitsselector:** voeg een Include-regel toe met Emails. Vervang `alice@example.com` en `bob@example.com` door de twee bedoelde adressen.
5. **Aanmelding:** selecteer de identiteitsprovider die deze bezoekers gebruiken en kies bewust de sessieduur.
6. **Route:** sla de applicatie op en verbind daarna de hostnaam via je tunnel met het dashboard.

De [officiële applicatieworkflow](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) beschrijft deze instellingen. **Verwacht resultaat:** een nieuwe bezoeker moet zich authenticeren voordat de applicatie bereikbaar is. Voer de test met een geweigerde identiteit hieronder uit voordat je op het beleid vertrouwt.

## Begrijp de beleidslogica

**Include** combineert alternatieven met OR. **Require** voegt verplichte voorwaarden toe met AND. **Exclude** verwijdert overeenkomende gebruikers. Een extra Include-voorwaarde vergroot de groep die toegang krijgt. [Semantiek van Access-regels](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Beleidsfragment | Logisch effect |
|---|---|
| **Include Alice or Bob** | Een van beide genoemde identiteiten voldoet |
| **Include Alice, Include a country** | Ook mensen uit dat land voldoen |
| **Include Alice, Require a country** | Alice moet ook aan de landvoorwaarde voldoen |

**Oefening in beleidscontrole:** je eis noemt alleen Alice en Bob, maar een collega voegt een land toe als extra Include-voorwaarde. Wijs de wijziging af, want hierdoor krijgt een grotere groep toegang. Een locatie bewijst niet dat iemand bij je huishouden hoort.

## Authenticeer geplande scripts

Een **servicetoken** bevat een Client ID en Client Secret voor geautomatiseerde aanvragen. Stel het applicatiebeleid in om het token via **Service Auth** te accepteren. Een token aanmaken zonder het bijbehorende beleid geeft geen toegang tot de applicatie. [Cloudflare-servicetokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Bewaar het **geheim** voor een back-upscript of controle in de beveiligde opslag voor inloggegevens van de tool. Geef elke integratie een eigen tokennaam en een bewuste vervaldatum. Roteer of trek het token in wanneer je de integratie buiten gebruik stelt. De documentatie over servicetokens beschrijft deze levenscyclusstappen.

**Controleer expliciet of de client compatibel is.** Een tool die een API-antwoord verwacht, kan niet vanzelfsprekend overweg met een interactieve browserlogin. Controleer of de tool aanvraagheaders of een andere ondersteunde authenticatiemethode gebruikt voordat je het beleid kiest.

## Test toegangsbeslissingen

Behandel deze punten als **acceptatiecontroles** voor je implementatie:

| Controle | Vast te leggen bewijs |
|---|---|
| **Bezoeker zonder aanmelding** | Access onderschept een aanvraag vanuit een nieuwe browsersessie |
| **Toegestane identiteit** | De bedoelde applicatie wordt na aanmelding geladen |
| **Geweigerde identiteit** | Een niet-vermeld account krijgt geen toegang tot de applicatie |
| **Alternatieve route** | Oude DNS-namen en originpoorten geven geen onbedoelde toegang |
| **Automatisering** | De goedgekeurde client werkt en een aanvraag zonder inloggegeven mislukt |

**Een zichtbaar aanmeldscherm** bewijst alleen dat één route authenticatie tegenkwam. Test ook de geweigerde situatie en alternatieve routes. Dit zijn aanbevolen controles, geen resultaten van een geïmplementeerd voorbeeld.

## Controleer de origin-grens

Een **origin die Access-identiteit vertrouwt** moet het ondertekende applicatietoken controleren. Cloudflare stuurt het door in de header **`Cf-Access-Jwt-Assertion`**. Alleen de aanwezigheid van een header bewijst de echtheid ervan niet. [Cloudflare JWT-validatie](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

Een **JSON Web Token (JWT)** bevat ondertekende claims. Gebruik de gedocumenteerde validatiemethode, inclusief de verwachte issuer en applicatie-audience, wanneer je Access-identiteit met een origin verbindt. Een token decoderen en een e-mailadres uitlezen is onvoldoende validatie.

**Issuer** duidt de autoriteit aan die het token uitgeeft. **Audience** duidt de beoogde applicatie aan. Controleer de geldigheid en vervaldatum van het token met een ondersteunde validatiebibliotheek. Implementeer handtekeningcontroles niet zelf.

**Maak de grens expliciet:** leg vast waar validatie plaatsvindt en welke routes de applicatie bereiken. Beoordeel een oude poortdoorschakeling of alternatieve hostnaam afzonderlijk, ook nadat de hoofdhostnaam alle browsercontroles doorstaat.

## Los verschillen in beleid op

| Waarneming | Volgende controle |
|---|---|
| **Een onverwachte bezoeker krijgt toegang** | Controleer Include-voorwaarden, Bypass-beleid en dekking van de hostnaam |
| **Een bedoelde bezoeker wordt geweigerd** | Vergelijk de aangemelde identiteit met de exacte selectorwaarden |
| **Een script ontvangt een aanmeldpagina** | Controleer de inloggegevens en het Service Auth-beleid |
| **Een toegelaten kijker kan instellingen wijzigen** | Controleer de eigen roltoewijzingen van de applicatie |

**Sessies** beïnvloeden ook hertests. Access heeft verschillende sessieduren, waaronder sessies voor applicaties en globale sessies. Noteer de sessie-instelling en gebruik een nieuwe sessie wanneer je een nieuwe identiteit controleert. [Sessiebeheer van Access](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Stel je toegangspecificatie op

Maak een **korte specificatie** voordat je nog een dienst toevoegt:

```text
Dienst en hostnaam:
Toegestane menselijke identiteiten:
Vereiste applicatierollen:
Inloggegeven voor automatisering en vervaldatum:
Andere routes naar de origin:
Locatie waar Access-tokens worden gevalideerd:
Testresultaat voor toegestane identiteit:
Testresultaat voor geweigerde identiteit:
```

**Voltooiingscriterium:** een andere beheerder moet begrijpen wie toegang krijgt, hoe elke client zich authenticeert en welk bewijs een weigering aantoont. Voeg je later een monitoringintegratie toe, werk dan het onderdeel over inloggegevens bij en herhaal de controle met een aanvraag zonder authenticatie.

## Volgende stappen

Volg de [Cloudflare Tunnel-installatiegids](/guides/how-to-setup-and-use-cloudflare-tunnels/) voor het instellen van de connector. Pas daarna de [officiële Access-applicatieworkflow](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) toe. Lees bij een mobiele verbinding eerst over de [beperkingen voor poortdoorschakeling van T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/) voordat je een route voor externe toegang kiest.
