---
title: "Tailscale versus Headscale"
date: 2026-05-24
lastmod: 2026-11-23
toc: true
draft: false
description: "Vergelijk Tailscale en Headscale op hostingmodel, identiteitsbeheer, functies, kosten, beheer en ondersteuning om een WireGuard-mesh-VPN te kiezen die bij je past."
genre: ["VPN", "Netwerkbeveiliging", "Zelfgehost", "WireGuard", "Zero Trust", "Meshnetwerken", "Openbronsoftware", "Cloudinfrastructuur", "Externe toegang", "Netwerkbeheer"]
tags: ["tailscale versus headscale", "headscale versus tailscale", "zelfgehoste vpn", "VPN op basis van WireGuard", "VPN in een meshnetwerk", "zero-trustnetwerken", "alternatief voor tailscale", "headscale instellen", "vpn-vergelijking", "VPN met openbroncode", "tailscale-prijzen", "headscale-functies", "WireGuard-meshnetwerk", "privénetwerk", "vpn-prestaties", "tailscale-functies", "headscale installeren", "meshnetwerken", "beveiligde externe toegang", "vpn-beveiliging", "netwerkcoördinatie", "tailnet", "vpn-implementatie", "bedrijfs-vpn", "vpn voor thuislabs", "zelfgehoste netwerken", "tailscale-kosten", "headscale met docker", "vpn-beheer", "wireguard-coördinatieserver"]
cover: "/img/cover/tailscale-vs-headscale-comparison-guide.webp"
coverAlt: "Een illustratie van een meshnetwerk waarin apparaten via oplichtende lijnen met elkaar verbonden zijn tegen een donkere achtergrond. De apparaten zijn afgebeeld als gestileerde pictogrammen in levendige kleuren die beveiligde verbindingen voorstellen."
coverCaption: ""
---

## Inleiding

**Tailscale** en **Headscale** zijn beide coördinatieservers voor het opzetten van beveiligde mesh-VPN's op basis van [WireGuard](https://www.wireguard.com/). Tailscale is een commerciële clouddienst met een ruim gratis abonnement. Headscale is een zelfgehost opensourcealternatief dat het besturingsprotocol van Tailscale implementeert. De verschillen tussen beide oplossingen helpen je bepalen welke aanpak bij de netwerkbehoeften van je organisatie past.

De belangrijkste keuze is **wie het besturingsvlak beheert**. Kies Tailscale als beheerd identiteitsbeheer, administratie en ondersteuning het zwaarst wegen. Overweeg Headscale als zelfhosting en zeggenschap over coördinatiegegevens het extra beheerwerk rechtvaardigen. De volgende secties vergelijken functies, prestaties, kosten, beveiliging en onderhoud.

______

## Mesh-VPN's en WireGuard begrijpen

Voor de vergelijking is het belangrijk om de onderliggende technologie te begrijpen:

### Wat is WireGuard?

**WireGuard** is een modern VPN-protocol dat hoge prestaties levert en het volgende biedt:
- **Uitzonderlijke prestaties:** Tot 10 keer sneller dan OpenVPN
- **Minimaal aanvalsoppervlak:** Slechts ~4,000 regels code (tegenover 100,000+ voor OpenVPN)
- **Moderne cryptografie:** Curve25519, ChaCha20, Poly1305
- **Ingebouwd in de Linux-kernel:** Sinds Linux 5.6 (2020)

### Wat is een mesh-VPN?

Een **mesh-VPN** zet peer-to-peerverbindingen tussen apparaten op in plaats van al het verkeer via een centrale server te leiden:
- **Directe verbindingen:** Apparaten maken waar mogelijk rechtstreeks verbinding met elkaar
- **NAT-traversal:** Passeert automatisch firewalls en NAT
- **Lagere latentie:** Geen onnodige tussenstappen via centrale servers
- **Betere prestaties:** Gebruikt de volledige bandbreedte tussen peers

### De rol van coördinatieservers

WireGuard zelf is alleen een protocol. Voor een mesh-VPN heb je een **coördinatieserver** (of besturingsvlak) nodig die:
- Authenticatie en autorisatie van apparaten beheert
- Versleutelingssleutels distribueert
- NAT-traversal ondersteunt en helpt peers te vinden
- Toegangsbeleid beheert
- DNS-naamomzetting binnen het netwerk verzorgt

**Tailscale** en **Headscale** zijn beide coördinatieservers die deze taken uitvoeren.

______

## Tailscale versus Headscale: overzicht

| Aspect | Tailscale | Headscale |
|--------|-----------|-----------|
| **Type** | Commerciële SaaS | Open source, zelfgehost |
| **Licentie** | Propriëtair (gratis abonnement beschikbaar) | BSD 3-Clause License |
| **Hosting** | In de cloud (Tailscale beheert de dienst) | Zelfgehost (je beheert de server zelf) |
| **Eerste release** | 2019 | 2020 |
| **Hoofdbeheerder** | Tailscale Inc. | Juan Font en de community |
| **GitHub-sterren** | N.v.t. (gesloten broncode) | 38.9k+ (stand in 2026) |
| **Complexiteit van de installatie** | Zeer laag (5 minuten) | Gemiddeld (30-60 minuten) |
| **Maandelijkse kosten (100 gebruikers)** | $0 (gratis) tot $18/gebruiker (Enterprise) | Alleen kosten voor serverhosting ($5-50/maand) |
| **Protocolcompatibiliteit** | Tailscale-protocol | Tailscale-protocol (compatibel) |

______

## Uitgebreide functievergelijking

### Basisnetwerkfuncties

| Functie | Tailscale | Headscale | Opmerkingen |
|---------|-----------|-----------|-------|
| **Mesh op basis van WireGuard** | ✅ Ja | ✅ Ja | Beide gebruiken WireGuard voor alle verbindingen tussen peers |
| **Automatische NAT-traversal** | ✅ Ja | ✅ Ja | STUN/DERP voor betrouwbare verbindingen |
| **Subnetroutering** | ✅ Ja | ✅ Ja | Krijg toegang tot netwerken achter een gateway |
| **Uitgangsknooppunten** | ✅ Ja | ✅ Ja | Leid al het internetverkeer via één knooppunt |
| **MagicDNS** | ✅ Ja | ✅ Ja | Naamomzetting binnen het meshnetwerk |
| **DNS per domein** | ✅ Ja | ✅ Ja | Gebruik afwijkende DNS-instellingen voor specifieke domeinen |
| **Routering met hoge beschikbaarheid** | ✅ Ja | ✅ Ja | Schakelt bij uitval automatisch over naar een andere route |
| **IPv6-ondersteuning** | ✅ Volledig | ✅ Volledig | Volledige IPv6-adressering in het meshnetwerk |
| **Multicastondersteuning** | ❌ Nee | ❌ Nee | Geen van beide ondersteunt momenteel multicast |

### Toegangsbeheer en beveiliging

| Functie | Tailscale | Headscale | Opmerkingen |
|---------|-----------|-----------|-------|
| **ACL-engine** | ✅ Geavanceerd | ✅ Compatibel | Headscale implementeert de ACL-syntaxis van Tailscale |
| **Toegangsbeheer op basis van tags** | ✅ Ja | ✅ Ja | Groepeer apparaten met tags |
| **Gebruikers- en groepsbeheer** | ✅ Ja | ✅ Ja | Headscale werkt met het concept 'gebruikers' |
| **OpenID Connect (OIDC)** | ✅ Ja | ✅ Ja | Meld je aan via Google, Okta, Keycloak enz. |
| **SAML-authenticatie** | ✅ Ja (Enterprise) | ❌ Nee | Alleen Tailscale |
| **Tailnet Lock** | ✅ Ja | ❌ Nee | Blokkeert onbevoegde coördinatieservers |
| **Controle van de apparaatstatus** | ✅ Ja (bèta) | ❌ Nee | Controleert vóór toegang of het apparaat aan de eisen voldoet |
| **Just-in-time-toegang** | ✅ Ja | ❌ Nee | Tijdelijk verhoogde rechten |
| **Auditlogboeken** | ✅ Uitgebreid | ⚠️ Basis | Tailscale biedt gedetailleerde logboeken |

### Beheer en administratie

| Functie | Tailscale | Headscale | Beperkingen |
|---------|-----------|-----------|-------------|
| **Webinterface** | ✅ Officieel | ⚠️ Community | Voor Headscale bestaan meerdere webinterfaces van de community |
| **Beheer via de CLI** | ✅ Ja | ✅ Ja | Beide bieden uitgebreide CLI-hulpmiddelen |
| **REST API** | ✅ Ja | ✅ Ja | Automatiseer beheertaken |
| **gRPC API** | ❌ Nee | ✅ Ja | Headscale biedt gRPC voor beheer op afstand |
| **Terraform-provider** | ✅ Officieel | ❌ Nee | Integratie voor infrastructuur als code |
| **Kubernetes-operator** | ✅ Officieel | ⚠️ Community | De community biedt een operator voor Headscale |
| **Mobiele apps** | ✅ iOS, Android | ✅ Compatibel | Gebruik Tailscale-apps met een Headscale-server |
| **Beheerconsole** | ✅ Uitgebreid | ❌ Nee | Headscale gebruikt de CLI of API |
| **Toegang voor meerdere beheerders** | ✅ Ja | ⚠️ Handmatig | Headscale vereist een eigen implementatie |

### Geavanceerde functies

| Functie | Tailscale | Headscale | Opmerkingen |
|---------|-----------|-----------|-------|
| **Tailscale SSH** | ✅ Ja | ⚠️ Alleen als server | Headscale-knooppunten kunnen als SSH-server dienen, maar niet als client |
| **Taildrop (bestanden delen)** | ✅ Ja | ⚠️ Onvolledig | Beperkte ondersteuning voor Taildrop in Headscale |
| **Funnel (publieke toegang)** | ✅ Ja | ❌ Nee | Maak diensten bereikbaar via het openbare internet |
| **Serve (privé delen)** | ✅ Ja | ❌ Nee | Deel diensten binnen het tailnet |
| **Inventarisatie van diensten** | ✅ Ja | ❌ Beperkt | Vind diensten op het netwerk |
| **Tailscale DERP** | ✅ Wereldwijd netwerk | ⚠️ Ingebouwd | Headscale heeft ingebouwde DERP-ondersteuning en je kunt een eigen server gebruiken |
| **Eigen DERP-servers** | ✅ Ja | ✅ Ja | Beide ondersteunen eigen relayservers |
| **Docker-extensie** | ✅ Ja | ❌ Nee | Docker-extensie van Tailscale voor containernetwerken |

______

## Prijsvergelijking (2026)

### Tailscale-prijzen

| Abonnement | Maandelijkse kosten | Jaarlijkse kosten | Apparaten | Functies |
|------|-------------|-------------|---------|----------|
| **Personal** | $0 | $0 | Tot 100 | 1 gebruiker, basisfuncties, ondersteuning door de community |
| **Personal Pro** | $6/gebruiker/maand | $48/gebruiker/jaar | Onbeperkt | Meerdere gebruikers, subnetroutering, ACL's |
| **Team** | $10/gebruiker/maand | $100/gebruiker/jaar | Onbeperkt | Beheerconsole, auditlogboeken, SSO |
| **Business** | $15/gebruiker/maand | $150/gebruiker/jaar | Onbeperkt | Geavanceerde ACL's, gebruikersgroepen, voorrang bij ondersteuning |
| **Enterprise** | $18+/gebruiker/maand | Op maat | Onbeperkt | Tailnet Lock, SAML, toegewijde ondersteuning, SLA |

**Opmerking:** Met het gratis Personal-abonnement van Tailscale kun je voor persoonlijk gebruik tot 100 apparaten aansluiten. Dat biedt veel ruimte voor thuislabs en kleine implementaties.

### Kosten van Headscale

Headscale is **gratis en open source**, maar je betaalt wel voor de infrastructuur:

| Middel | Maandelijkse kosten (bereik) | Opmerkingen |
|----------|-------------------|-------|
| **Kleine VPS** (1 CPU, 1GB RAM) | $5-10 | Geschikt voor <50 apparaten |
| **Middelgrote VPS** (2 CPU's, 4GB RAM) | $15-25 | Geschikt voor 50-200 apparaten |
| **Grote VPS** (4 CPU's, 8GB RAM) | $40-80 | Geschikt voor 200-1000+ apparaten |
| **Domeinnaam** | $10-15/jaar | Voor TLS-certificaten |
| **Bandbreedte** | Meestal inbegrepen | Controleer de limieten van je VPS-aanbieder |
| **Tijdsinvestering** | Variabel | Installatie, onderhoud, updates |

**Totale eigendomskosten (100 gebruikers):**
- **Tailscale:** $0 (gratis abonnement) of $1,000-1,800/maand (betaalde abonnementen)
- **Headscale:** $15-30/maand + 5-10 uur voor installatie + 2-5 uur/maand voor onderhoud

**Omslagpunt:** Voor organisaties met meer dan 3-5 betalende gebruikers wordt Headscale voordeliger als je werktijd waardeert op <$50/uur.

______

## Prestatievergelijking

### Latentie en doorvoersnelheid

Zowel Tailscale als Headscale gebruikt WireGuard voor het datavlak, dus **de peer-to-peerprestaties zijn identiek**:

| Meetwaarde | Tailscale | Headscale |
|--------|-----------|-----------|
| **Extra P2P-latentie** | <1ms | <1ms |
| **P2P-doorvoersnelheid** | Bijna gelijk aan zonder VPN (~900 Mbps op 1 Gbps) | Bijna gelijk aan zonder VPN |
| **Doorvoersnelheid via relay (DERP)** | 50-300 Mbps | 10-200 Mbps (afhankelijk van je server) |
| **Latentie via relay** | +10-50ms | +5-100ms (afhankelijk van de locatie) |
| **Verbinding opzetten** | 100-500ms | 200-800ms |
| **Verspreiding van wijzigingen in ACL-beleid** | <5 seconden | <30 seconden |

**Belangrijk verschil:** Tailscale beheert een wereldwijd DERP-netwerk met relayservers over de hele wereld. Daardoor presteren relayverbindingen beter als directe verbindingen mislukken. De ingebouwde DERP-server van Headscale draait op je eigen server. Zonder geografische spreiding kan de latentie hoger uitvallen.

### Schaalbaarheid

| Aspect | Tailscale | Headscale |
|--------|-----------|-----------|
| **Maximumaantal knooppunten** | 100,000+ (getest) | ~5,000 (gemeld door de community) |
| **Aanbevolen aantal knooppunten** | Onbeperkt | <1,000 voor één server |
| **Verzoeken per minuut (RPM) op het besturingsvlak** | Sterk geoptimaliseerd | Afhankelijk van de serverspecificaties |
| **Geheugen per knooppunt** | N.v.t. (beheerd) | ~1-5 MB (aan serverzijde) |
| **Database** | PostgreSQL (beheerd) | SQLite of PostgreSQL |

______

## Beveiligingsvergelijking

### Infrastructuurbeveiliging

| Aspect | Tailscale | Headscale | Beoordeling |
|--------|-----------|-----------|------------|
| **Vertrouwen in de coördinatieserver** | Je moet Tailscale Inc. vertrouwen | Je beheert de server zelf | Headscale biedt betere privacy |
| **Versleutelingssleutels** | Apparaten genereren de sleutels en sturen ze nooit naar Tailscale | Apparaten genereren de sleutels en sturen ze nooit naar de server | ✅ Beide uitstekend |
| **Beveiliging van het datavlak** | WireGuard (uitstekend) | WireGuard (uitstekend) | ✅ Beide uitstekend |
| **Beveiliging van het besturingsvlak** | HTTPS + attestatie | HTTPS + optioneel equivalent van Tailnet Lock | ⚠️ Tailscale iets sterker |
| **Audittrail** | Uitgebreide logboeken | Basislogboeken | ⚠️ Tailscale beter |
| **Bug-bountyprogramma** | ✅ Ja | ❌ Nee | Tailscale heeft beveiligingsonderzoekers betaald |
| **Beveiligingscertificeringen** | SOC 2 Type II | N.v.t. | Tailscale geschikt voor grote organisaties |

### Privacyoverwegingen

| Privacyaspect | Tailscale | Headscale |
|----------------|-----------|-----------|
| **Zichtbaarheid van metadata** | Tailscale ziet apparaatnamen, IP-adressen en verbindingsmetadata | Je beheert alle metadata zelf |
| **Zichtbaarheid van verkeer** | ❌ Geen inzage in verkeer (versleuteld) | ❌ Geen inzage in verkeer (versleuteld) |
| **Nalevingsvereisten** | Valt onder Amerikaanse jurisdictie | Valt onder de jurisdictie van je server |
| **Gegevenslocatie** | Cloudinfrastructuur van Tailscale | Datacenter van jouw keuze |

**Oordeel:** Beide oplossingen bieden **uitstekende versleuteling en een zero-knowledge-architectuur** voor het netwerkverkeer zelf. Headscale biedt betere **privacy** doordat je alle metadata zelf beheert. Tailscale biedt sterkere **beveiligingswaarborgen** via certificeringen, audits en bug-bountyprogramma's.

______

## Vergelijking van installatie en implementatie

### Tailscale instellen

**Benodigde tijd:** 5-10 minuten

1. **Maak een account aan** op [tailscale.com](https://tailscale.com/)
2. **Installeer de client** op elk apparaat (met één opdracht of door de app te downloaden)
3. **Meld je aan** via OAuth (Google, Microsoft, GitHub enz.)
4. **Configureer ACL's** (optioneel, dit kan ook later)
5. **Klaar!** Het netwerk werkt meteen

**Voorbeeldinstallatie (Linux):**

> **Controleer het installatiescript voordat je het uitvoert.** Download het naar een tijdelijk bestand, lees de inhoud en controleer de distributie van de host en de herkomst van het pakket. Voer na installatie `tailscale version` en `tailscale status` uit om het resultaat te controleren. Als de installatie mislukt, verwijder je het pakket met de pakketbeheerder van je distributie en herstel je de vorige pakketstatus vanuit je systeemback-up.

```bash
curl -fsSL https://tailscale.com/install.sh -o /tmp/tailscale-install.sh
less /tmp/tailscale-install.sh
sh /tmp/tailscale-install.sh
sudo tailscale up
```

### Headscale instellen

**Benodigde tijd:** 30-90 minuten (eerste keer)

1. **Richt een server in** (VPS met openbaar IP-adres, 1GB+ RAM aanbevolen)
2. **Configureer DNS** (A-record dat naar de server verwijst)
3. **Installeer Headscale** (via een pakketbeheerder of Docker)
4. **Configureer Headscale** (config.yaml met server-URL, database enz.)
5. **Stel TLS-certificaten in** (Let's Encrypt aanbevolen)
6. **Start de Headscale-dienst**
7. **Maak gebruikers aan** via de CLI: `headscale users create alice`
8. **Installeer de Tailscale-client** op elk apparaat
9. **Configureer clients** voor gebruik met je eigen coördinatieserver
10. **Registreer knooppunten** via webauthenticatie of vooraf aangemaakte authenticatiesleutels
11. **Configureer ACL's** (bestand policy.json)

**Voorbeeldinstallatie van Headscale (Ubuntu):**
```bash
# Headscale installeren
curl -fsSL https://pkgs.headscale.net/headscale_<VERSION>_linux_amd64.deb -o headscale.deb
sudo apt install ./headscale.deb

# Headscale configureren
sudo nano /etc/headscale/config.yaml
# Stel server_url in op https://headscale.example.com

# Start de service
sudo systemctl enable --now headscale

# Maak een gebruiker aan
headscale users create myuser

# Op de clientcomputer
sudo tailscale up --login-server=https://headscale.example.com
```

**Eenvoudigste installatie:** **Tailscale** is bij de eerste installatie veel eenvoudiger.

______

## Complexiteit van het beheer

### Dagelijks beheer

| Taak | Tailscale | Headscale | Winnaar |
|------|-----------|-----------|--------|
| **Nieuw apparaat toevoegen** | Klik op de link en meld je aan | Genereer een authenticatiesleutel of meld je aan via het web | Tailscale (eenvoudiger) |
| **ACL's bijwerken** | Bewerk ze in de webinterface, wijzigingen gelden meteen | Bewerk het bestand en laad de configuratie opnieuw | Tailscale (eenvoudiger) |
| **Verbindingsstatus bekijken** | Webdashboard | CLI of webinterface van de community | Tailscale (eenvoudiger) |
| **Problemen oplossen** | Gedetailleerde logboeken in het dashboard | Serverlogboeken + clientlogboeken | Tailscale (eenvoudiger) |
| **Software bijwerken** | Automatisch | Handmatige serverupdates | Tailscale (eenvoudiger) |
| **Back-up van de configuratie maken** | Automatisch | Handmatig (database + configuratie) | Tailscale (eenvoudiger) |
| **Herstel na een calamiteit** | Automatisch | Handmatig herstel vanuit een back-up | Tailscale (eenvoudiger) |

### Onderhoudswerk

**Tailscale (beheerde dienst):**
- ✅ Geen serveronderhoud
- ✅ Automatische updates en beveiligingspatches
- ✅ Ingebouwde redundantie en automatische overschakeling bij uitval
- ✅ Professionele ondersteuning beschikbaar
- ❌ Afhankelijk van de beschikbaarheid van de Tailscale-dienst

**Headscale (zelfgehost):**
- ⚠️ Updates en beveiligingspatches voor het serverbesturingssysteem (maandelijks)
- ⚠️ Updates voor Headscale (elke 1-3 maanden)
- ⚠️ Back-ups van de database (dagelijks aanbevolen)
- ⚠️ Vernieuwing van TLS-certificaten (geautomatiseerd met Let's Encrypt)
- ⚠️ Monitoring en waarschuwingen instellen
- ⚠️ Storingen zelf oplossen
- ✅ Volledige zeggenschap over de infrastructuur
- ✅ Geen afhankelijkheid van een externe dienst

**Geschatte maandelijkse tijdsinvestering:**
- **Tailscale:** 30 minuten (beleid nalopen, gebruikers toevoegen)
- **Headscale:** 2-5 uur (updates, monitoring, problemen oplossen)

______

## Aanbevelingen per gebruikssituatie

### Kies Tailscale als:

✅ **Je zo snel mogelijk aan de slag wilt** - 5 minuten van account aanmaken tot een werkend netwerk\
✅ **Je <100 apparaten hebt** - Het gratis abonnement dekt persoonlijk gebruik en gebruik door kleine bedrijven\
✅ **Gebruiksgemak vooropstaat** - De beste webinterface en gebruikerservaring in zijn klasse\
✅ **Je bedrijfsfuncties nodig hebt** - SSO, auditlogboeken, Tailnet Lock, controle van de apparaatstatus\
✅ **Je tijd wilt besparen** - Geen onderhoudswerk, automatische updates\
✅ **Je gegarandeerde beschikbaarheid nodig hebt** - Tailscale hanteert een SLA van 99.99% beschikbaarheid (Enterprise)\
✅ **Je officiële mobiele apps wilt** - Native apps voor iOS en Android met alle functies\
✅ **Je professionele ondersteuning nodig hebt** - Betaalde abonnementen geven voorrang bij ondersteuning\
✅ **Naleving van normen belangrijk is** - Gecertificeerd volgens SOC 2 Type II\
✅ **Je een commerciële organisatie bent** - Eenvoudige prijzen per gebruiker zonder verborgen kosten\

### Kies Headscale als:

✅ **Je volledige datasoevereiniteit nodig hebt** - Alle metadata blijft op je eigen infrastructuur\
✅ **Je aan privacy- of nalevingsvereisten moet voldoen** - Gegevens moeten binnen specifieke jurisdicties blijven\
✅ **Je technische kennis hebt** - Je bent vertrouwd met Linux-systeembeheer, Docker en het oplossen van storingen\
✅ **Je >10 betalende gebruikers hebt** - De kostenbesparing wordt aanzienlijk naarmate het aantal gebruikers groeit\
✅ **Je wilt leren** - Een geschikt project om mesh-VPN's te leren begrijpen\
✅ **Je de voorkeur geeft aan open source** - Je kunt de code controleren, fixes bijdragen en de software aanpassen\
✅ **Je op je budget let** - Lage terugkerende kosten ($5-30/maand voor de server)\
✅ **Je al infrastructuur hebt** - Je kunt Headscale op bestaande Kubernetes- of VM-infrastructuur draaien\
✅ **Je een gRPC API nodig hebt** - Headscale biedt gRPC voor geavanceerde automatisering\
✅ **Je al zelf diensten host** - Headscale past in je bestaande zelfgehoste omgeving\

### Hybride aanpak: gebruik beide

Sommige organisaties gebruiken **beide oplossingen**:

1. **Tailscale voor productie** - Kritieke infrastructuur met SLA en ondersteuning
2. **Headscale voor ontwikkeling en tests** - Voordelige ontwikkelomgevingen
3. **Tailscale voor niet-technische gebruikers** - Medewerkers kunnen eenvoudig aan de slag
4. **Headscale voor technische teams** - Technici die gewend zijn zelf diensten te hosten

______

## Migratiescenario's

### Migreren van Tailscale naar Headscale

**Motivatie:** Lagere kosten, datasoevereiniteit, meer zeggenschap

**Stappen:**
1. Richt een Headscale-server in en controleer of die werkt
2. Test Headscale met een deel van de niet-kritieke apparaten
3. Exporteer ACL's uit Tailscale en pas ze aan voor Headscale
4. Zet apparaten geleidelijk over naar de Headscale-coördinatieserver
5. Werk de DNS-configuratie en subnetroutes bij
6. Zeg het Tailscale-abonnement op

**Uitdagingen:**
- Geen geautomatiseerd migratiehulpmiddel
- Alle apparaten moeten zich opnieuw authenticeren
- Sommige functies (Funnel, Serve, Taildrop) werken niet op dezelfde manier
- De ACL-syntaxis is compatibel, maar je moet de regels testen

**Tijdsinvestering:** 5-20 uur, afhankelijk van de complexiteit

### Migreren van Headscale naar Tailscale

**Motivatie:** Minder beheerwerk, bedrijfsfuncties, betere ondersteuning

**Stappen:**
1. Maak een Tailscale-account aan en configureer ACL's
2. Installeer Tailscale-clients (op hetzelfde apparaat kan de nieuwe installatie de bestaande vervangen)
3. Zet apparaten over door `tailscale up` uit te voeren zonder eigen server op te geven
4. Controleer de verbindingen en toegangsregels
5. Stel de Headscale-server buiten gebruik

**Uitdagingen:**
- Alle apparaten moeten zich opnieuw authenticeren
- Sommige gebruikers hebben mogelijk Tailscale-accounts nodig (e-mail of SSO)
- Begeleiding van de overgang en communicatie met gebruikers

**Tijdsinvestering:** 2-8 uur, afhankelijk van de omvang

______

## Community en ecosysteem

### Tailscale-ecosysteem

| Bron | Beschikbaarheid |
|----------|--------------|
| **Officiële documentatie** | ✅ Uitgebreid en goed onderhouden |
| **Communityforum** | ✅ Actief forum met medewerkers van Tailscale |
| **Discord-community** | ✅ Zeer actief, medewerkers reageren op vragen |
| **GitHub Issues** | ❌ Gesloten broncode (feedback via het forum) |
| **Stack Overflow** | ✅ Actieve tag met 2,000+ vragen |
| **YouTube-handleidingen** | ✅ Officiële video's en video's van de community |
| **Integraties** | ✅ Docker, Kubernetes, Terraform, Synology, QNAP enz. |

### Headscale-ecosysteem

| Bron | Beschikbaarheid |
|----------|--------------|
| **Officiële documentatie** | ✅ Goed, de community onderhoudt de documentatie |
| **Communityforum** | ⚠️ GitHub Discussions dient als forum |
| **Discord-community** | ✅ Actieve communityserver |
| **GitHub Issues** | ✅ Open source, actief systeem voor het bijhouden van meldingen (38.9k+ sterren) |
| **Stack Overflow** | ⚠️ Kleinere community (~100 vragen) |
| **YouTube-handleidingen** | ⚠️ Video's van de community |
| **Webinterfaces** | ⚠️ Meerdere opties van de community (Headscale-UI, Headplane, ouroboros) |
| **Kubernetes-operator** | ⚠️ De community onderhoudt de operator |

**Omvang van de community (2026):**
- **Tailscale:** 100,000+ actieve leden, gesteund door een bedrijf met ruime financiering
- **Headscale:** 10,000+ actieve leden, opensourceproject

______

## Prestatiemetingen in de praktijk (2026)

Op basis van tests door de community en gepubliceerde benchmarks:

### Doorvoertests (peer-to-peer)

| Scenario | Tailscale | Headscale | Referentiewaarde (zonder VPN) |
|----------|-----------|-----------|-------------------|
| **Gigabit-LAN** | 940 Mbps | 940 Mbps | 945 Mbps |
| **WAN (100 Mbps)** | 98 Mbps | 98 Mbps | 100 Mbps |
| **WAN (1 Gbps glasvezel)** | 920 Mbps | 920 Mbps | 950 Mbps |
| **Tussen continenten (DERP)** | 180 Mbps | 95 Mbps | N.v.t. |

**Analyse:** Directe peer-to-peerverbindingen presteren identiek. Bij relayverbindingen presteert Tailscale beter dankzij het wereldwijde DERP-netwerk.

### Latentietests

| Scenario | Tailscale | Headscale | Referentiewaarde |
|----------|-----------|-----------|----------|
| **LAN-ping** | 1.2ms | 1.2ms | 0.8ms |
| **Regionaal WAN (100 mijl)** | 15ms | 15ms | 12ms |
| **Dwars door het land** | 48ms | 48ms | 45ms |
| **Tussen continenten (direct)** | 155ms | 155ms | 152ms |
| **Tussen continenten (DERP)** | 185ms | 220ms | N.v.t. |

**Analyse:** Beide voegen weinig latentie toe (~1-2ms) aan directe verbindingen. De DERP-latentie van Headscale hangt af van de serverlocatie.

### Verbruik van systeembronnen

| Meetwaarde | Tailscale-client | Headscale-client | Headscale-instantie |
|--------|------------------|------------------|------------------|
| **RAM-gebruik (in rust)** | 80-120 MB | 80-120 MB | 50-200 MB (afhankelijk van het aantal knooppunten) |
| **RAM-gebruik (actief)** | 120-200 MB | 120-200 MB | 100-500 MB |
| **CPU-gebruik (in rust)** | <1% | <1% | <1% |
| **CPU-gebruik (actief)** | 5-15% | 5-15% | 3-20% (afhankelijk van het aantal knooppunten) |
| **Schijfgebruik** | 100-500 MB | 100-500 MB | 100MB-2GB (database) |

______

## Geavanceerde configuratievoorbeelden

### Headscale met Docker Compose

```yaml
version: '3'
services:
  headscale:
    image: headscale/headscale:0.28.0
    container_name: headscale
    restart: unless-stopped
    ports:
      - "127.0.0.1:8080:8080"  # API/web
      - "443:443"              # HTTPS
      - "3478:3478/udp"        # STUN
    volumes:
      - ./config:/etc/headscale
      - ./data:/var/lib/headscale
    command: serve
    environment:
      - TZ=UTC
```

### ACL-voorbeeld voor Headscale

```json
{
  "groups": {
    "group:admin": ["alice@", "bob@"],
    "group:developers": ["charlie@", "diana@"]
  },
  "hosts": {
    "production-db": "100.64.0.10/32",
    "staging-db": "100.64.0.20/32"
  },
  "acls": [
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["*:*"]
    },
    {
      "action": "accept",
      "src": ["group:developers"],
      "dst": ["staging-db:5432", "autogroup:self:*"]
    }
  ]
}
```

### Tailscale-client configureren voor Headscale

```bash
# Linux
sudo tailscale up \
  --login-server=https://headscale.example.com \
  --accept-routes \
  --advertise-tags=tag:server

# Met een vooraf geauthenticeerde sleutel
headscale preauthkeys create --user engineering --expiration 1h

sudo tailscale up \
  --login-server=https://headscale.example.com \
  --authkey=<YOUR_AUTH_KEY>
```

______

## Veelvoorkomende problemen oplossen

### Problemen met Tailscale

| Probleem | Oplossing |
|---------|----------|
| **Geen verbinding met de coördinatieserver** | Controleer de firewall en de internetverbinding |
| **Directe verbinding mislukt** | Meestal schakelt Tailscale automatisch over op DERP. Controleer de NAT-instellingen |
| **Hoge latentie** | Controleer of de verbinding rechtstreeks loopt en geen relay gebruikt |
| **Sleutel verlopen** | Meld je opnieuw aan of schakel het verlopen van sleutels uit in de beheerconsole |
| **ACL blokkeert verkeer** | Controleer de ACL-regels en test de configuratie |

### Problemen met Headscale

| Probleem | Oplossing |
|---------|----------|
| **Knooppunten registreren zich niet** | Controleer of de Headscale-URL bereikbaar is en controleer het TLS-certificaat |
| **DNS-naamomzetting mislukt** | Controleer of MagicDNS correct is ingesteld in config.yaml |
| **DERP-relay werkt niet** | Controleer of de STUN-poort (3478/udp) openstaat en controleer de DERP-configuratie |
| **Knooppunten zijn offline na een herstart** | Stel clients zo in dat ze opstarten met het systeem |
| **ACL-wijzigingen worden niet toegepast** | Laad Headscale opnieuw met `systemctl reload headscale` |
| **Database beschadigd** | Herstel de database vanuit een back-up en overweeg PostgreSQL voor productie |

### Diagnoseopdrachten

```bash
# Tailscale-diagnostiek
tailscale status
tailscale netcheck
tailscale ping <hostname>
tailscale debug derp

# Headscale-diagnostiek
headscale nodes list
headscale nodes list-routes
headscale debug routes
journalctl -u headscale -f  # Bekijk logboeken
```

______

## Aanbevolen beveiligingsmaatregelen

### Voor beide oplossingen

1. **Laat sleutels verlopen** - Vereis dat gebruikers zich regelmatig opnieuw authenticeren
2. **Pas het principe van minimale rechten toe** - Verleen via ACL's alleen de noodzakelijke toegang
3. **Geef infrastructuurknooppunten tags** - Onderscheid gebruikersapparaten van servers
4. **Schakel MFA in** - Vereis multifactorauthenticatie bij het aanmelden
5. **Controleer toegangslogboeken** - Bekijk regelmatig verbindingspatronen
6. **Houd clients up-to-date** - Installeer beveiligingspatches snel

### Beveiliging specifiek voor Headscale

1. **Versterk de beveiliging van het serverbesturingssysteem** - Volg de CIS-benchmarks en schakel overbodige diensten uit
2. **Gebruik Let's Encrypt** - Automatiseer het beheer van TLS-certificaten
3. **Gebruik fail2ban** - Voorkom bruteforcepogingen
4. **Maak regelmatig back-ups** - Automatiseer databaseback-ups naar een aparte locatie
5. **Installeer updates snel** - Houd Headscale-releases in de gaten voor beveiligingspatches
6. **Segmenteer het netwerk** - Isoleer de Headscale-server op een beheer-VLAN
7. **Schakel de firewall in** - Stel alleen de nodige poorten open (443, 3478/udp)

______

## Toekomstplannen en ontwikkeling

### Ontwikkelplannen van Tailscale (2026)

Volgens openbare verklaringen van Tailscale:
- ✅ **Uitgebracht:** Aperture (gateway voor AI-governance), uitgebreidere controles van de apparaatstatus
- 🚧 **In ontwikkeling:** Geavanceerde dreigingsdetectie, ondersteuning voor meer platforms
- 📋 **Gepland:** Modus met alleen IPv6, beter inzicht in de werking van het systeem, meer integraties

### Stand van zaken bij Headscale (2026)

Op basis van GitHub-mijlpalen en discussies in de community:
- ✅ **Recent toegevoegd:** OIDC-authenticatie, verbeterde DERP, betere ACL-ondersteuning
- 🚧 **In ontwikkeling:** Verbeteringen aan Taildrop, betere integratie met webinterfaces
- 📋 **Verzoeken van de community:** Equivalent van Funnel/Serve, geavanceerde logboekregistratie, modus voor hoge beschikbaarheid

**Beoordeling van de volwassenheid:**
- **Tailscale:** Geschikt voor productie en grote organisaties, 5+ jaar ontwikkeling
- **Headscale:** Geschikt voor productie bij eenvoudig gebruik, actief ontwikkeld door de community

______

## Conclusie

Zowel **Tailscale** als **Headscale** biedt uitstekende mesh-VPN-functies op basis van WireGuard, maar beide richten zich op verschillende gebruikers en toepassingen.

**Kies Tailscale als:**
- Je eenvoud belangrijk vindt en binnen enkele minuten aan de slag wilt
- Je in een klein team werkt (<100 apparaten) dat baat heeft bij het ruime gratis abonnement
- Je bedrijfsfuncties nodig hebt, zoals SSO, auditlogboeken en professionele ondersteuning
- Je de voorkeur geeft aan beheerde diensten boven zelfhosting
- Nalevingscertificeringen (SOC 2) belangrijk zijn

**Kies Headscale als:**
- Je volledige zeggenschap over je infrastructuur en metadata nodig hebt
- Je technische kennis hebt en graag zelf diensten host
- Kostenbeheersing cruciaal is (>10 betalende gebruikers = aanzienlijke besparing)
- Datasoevereiniteit en privacy vooropstaan
- Je de voorkeur geeft aan opensourceoplossingen waarvan je de code kunt controleren en aanpassen

**Belangrijkste aanbevelingen voor 2026:**

1. **Start-ups en mkb:** Begin met **het gratis abonnement van Tailscale**. Voor 0-100 apparaten is het onovertroffen.
2. **IT-afdelingen van grote organisaties:** **Tailscale Enterprise** met SSO en ondersteuning levert de laagste totale eigendomskosten als je de werktijd van medewerkers meetelt.
3. **Privacybewuste gebruikers:** **Headscale** biedt maximale zeggenschap en privacy.
4. **Technische thuislabgebruikers:** **Headscale** biedt een uitstekende kans om ervaring op te doen.
5. **Organisaties met een hybride aanpak:** Gebruik **Tailscale voor productie** en **Headscale voor ontwikkeling en tests**.

Welke oplossing je ook kiest, je gebruikt WireGuard, technologie van topklasse voor moderne, beveiligde netwerken. De beslissing hangt af van je prioriteiten: **gemak tegenover zeggenschap**, **beheerd tegenover zelfgehost** en **kosten tegenover functies**.

Voor de meeste organisaties biedt **de beheerde dienst van Tailscale** in 2026 de beste balans tussen functionaliteit, gebruiksgemak en prijs-kwaliteitverhouding. Voor organisaties met specifieke eisen rond datasoevereiniteit, privacy of kosten **biedt Headscale een aantrekkelijk zelfgehost alternatief**.

______

## Bronnen en naslagmateriaal

1. [Officiële website van Tailscale](https://tailscale.com/)
2. [Tailscale-documentatie](https://tailscale.com/kb/)
3. [Officiële documentatie van Headscale](https://headscale.net/)
4. [GitHub-repository van Headscale](https://github.com/juanfont/headscale)
5. [Officiële website van WireGuard](https://www.wireguard.com/)
6. [Tailscale-blog - Hoe Tailscale werkt](https://tailscale.com/blog/how-tailscale-works/)
7. [Zero-trustarchitectuur van NIST](https://csrc.nist.gov/publications/detail/sp/800-207/final)
8. [Technische whitepaper van WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
