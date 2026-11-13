---
title: "Hoe DNS werkt: DNS-root, belang en probleemoplossing"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Lees hoe DNS en de DNS-root werken, met hun hiërarchie, resolutieproces, caching en tips voor probleemoplossing."
genre: ["DNS-basis", "DNS-root", "Domeinnaamsysteem", "DNS-resolutie", "DNS-hiërarchie", "DNS-opslag in cache", "DNS-probleemoplossing", "DNS-records", "DNS-beheer", "DNS-opdrachten"]
tags: ["DNS", "DNS-root", "Domeinnaamsysteem", "DNS-resolutie", "DNS-hiërarchie", "DNS-opslag in cache", "DNS-records", "DNS-beheer", "DNS-probleemoplossing", "netwerken", "internetinfrastructuur", "IP-adressen", "websitetoegang", "recursieve query", "authoritatieve naamservers", "TTL", "cachingmechanismen", "DNS-cache wissen", "DNS-rootservers", "anycast-routering", "ICANN", "DNS-samenwerking", "A-record", "AAAA-record", "CNAME-record", "MX-record", "TXT-record", "SRV-record", "NS-record", "PTR-record", "SOA-record", "DNS-opdrachten voor probleemoplossing", "Windows", "macOS", "Linux", "Opdrachtprompt", "terminalprogramma"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Een afbeelding van onderling verbonden computernetwerken met domeinnamen en IP-adressen, als weergave van DNS en de DNS-root."
coverCaption: "Ontdek DNS: beheers het domeinnaamsysteem"
---

## Hoe DNS en de DNS-root werken

### Inleiding

Het Domain Name System (DNS) is een essentieel onderdeel van de internetinfrastructuur. Het laat gebruikers websites openen met domeinnamen in plaats van IP-adressen. DNS werkt als een telefoonboek dat leesbare domeinnamen omzet in IP-adressen die computers begrijpen. De DNS-root vormt de top van de hiërarchische, gedistribueerde DNS. In dit artikel lees je hoe DNS en de DNS-root werken en welke records een domein kan hebben.

{{< youtube id="mpQZVYPuDGU" >}}

## Het Domain Name System (DNS)

Het **Domain Name System (DNS)** is een gedecentraliseerd naamgevingssysteem dat domeinnamen aan IP-adressen koppelt. Gebruikers openen hiermee websites en andere internetbronnen door een domeinnaam in hun browser te typen. DNS voorkomt dat je ingewikkelde IP-adressen moet onthouden.

### DNS-hiërarchie

DNS heeft een hiërarchische structuur met meerdere niveaus. Bovenaan staat de rootzone, gevolgd door topleveldomeinen (TLD's), domeinen op het tweede niveau en subdomeinen. Elk niveau vormt een deel van de volledige domeinnaam. In `www.example.com` is "www" het subdomein, "example" het domein op het tweede niveau en "com" het TLD.

### DNS-resolutieproces

Wanneer je een domeinnaam in je browser invoert, begint de DNS-resolutie. De browser stuurt een DNS-query naar een DNS-resolver, meestal van je internetprovider (ISP). De resolver doorloopt vervolgens stappen om de domeinnaam op te lossen en het bijbehorende IP-adres te vinden.

1. **Lokale DNS-cache**: De resolver controleert eerst zijn lokale cache op de gevraagde domeinnaam en het IP-adres. Staat de informatie erin, dan stuurt de resolver het resultaat meteen terug.

2. **Recursieve query**: Staat de informatie niet in de cache, dan start de resolver een recursieve query. Eerst neemt hij contact op met de DNS-rootservers, die verantwoordelijk zijn voor de zone "." (punt). De rootservers geven de IP-adressen terug van de TLD-servers voor het gevraagde domein.

3. **TLD-query**: De resolver neemt contact op met de TLD-servers uit de vorige stap en vraagt naar de authoritatieve naamservers voor het domein.

4. **Query aan de authoritatieve naamserver**: De resolver stuurt een query naar de authoritatieve naamservers die hij van de TLD-servers kreeg. Deze servers bevatten de authoritatieve records voor het domein. Ze antwoorden met het bijbehorende IP-adres.

5. **Antwoord aan de client**: De resolver ontvangt het IP-adres van de authoritatieve naamservers en stuurt het terug naar de browser. De browser kan daarna met dat IP-adres verbinding maken met de webserver.

### DNS-opslag in cache

DNS-resolvers gebruiken caching om de prestaties te verbeteren en de belasting op DNS-servers te verlagen. Na een antwoord slaat de resolver de koppeling tussen domeinnaam en IP-adres lokaal op. Volgende queries voor dezelfde domeinnaam komen dan rechtstreeks uit de cache.

Caching vindt op meerdere niveaus plaats, waaronder de lokale resolver, de resolver van de ISP en apparaten zoals routers en besturingssystemen. De Time-to-Live-waarde (TTL) in het DNS-antwoord bepaalt hoelang een record in de cache blijft. Na afloop van de TTL verwijdert de resolver het record en voert hij een nieuwe query uit.

#### Je lokale DNS-cache wissen

Het wissen van de DNS-cache helpt bij sommige DNS-problemen en zorgt ervoor dat je systeem actuele records ophaalt. Zo wis je de DNS-cache op verschillende besturingssystemen:

##### Windows

Wis de DNS-cache op Windows als volgt:

1. Open de Opdrachtprompt door op `Win + R` te drukken, `cmd` te typen en op Enter te drukken.

2. Typ in de Opdrachtprompt de volgende opdracht en druk op Enter:

```bash
ipconfig /flushdns
```

Met deze opdracht wis je de DNS-resolvercache op je Windows-systeem.

##### macOS

Wis de DNS-cache op macOS als volgt:

1. Open Terminal. Je vindt de app in Programma's > Hulpprogramma's of via Spotlight.

2. Typ in terminalprogramma de volgende opdracht en druk op Enter:

```bash
sudo killall -HUP mDNSResponder
```

Deze opdracht herstart het proces mDNSResponder, dat op macOS DNS-resolutie verzorgt.

##### Linux

De stappen om de DNS-cache op Linux te wissen verschillen per distributie en resolver. Dit zijn twee gangbare methoden:

1. **Systemd-systemen (zoals Ubuntu en Fedora)**:

Open Terminal en voer de volgende opdracht met beheerdersrechten uit:

```bash
sudo systemd-resolve --flush-caches

```

Deze opdracht wist de DNS-cache op systemen die systemd-resolved als resolver gebruiken.

2. **Systemen zonder systemd**:

Open Terminal en voer de volgende opdracht met beheerdersrechten uit:

```bash
sudo /etc/init.d/nscd restart

```

Deze opdracht herstart Name Service Cache Daemon (nscd), dat DNS-opslag in cache verzorgt op Linux-distributies zonder systemd.

De genoemde stappen zijn algemene richtlijnen. Opdrachten en methoden kunnen per versie verschillen. Het wissen van de DNS-cache kan sommige DNS-problemen oplossen, maar niet elk probleem met netwerkverbindingen.

## Hoe het DNS-rootsysteem werkt

Het DNS-rootsysteem is een fundamenteel onderdeel van de DNS-infrastructuur. Zo werkt het:

### 1. Rootzone en rootservers

Het DNS-rootsysteem begint bij de **rootzone**, de top van de DNS-hiërarchie. De rootzone bevat informatie over de authoritatieve naamservers van alle topleveldomeinen (TLD's), zoals .com, .org en .net, en landcode-TLD's zoals .us en .uk.

Het DNS-rootsysteem bestaat uit 13 rootservers met de letters A tot en met M. Ze zijn geografisch over de wereld verspreid voor redundantie en betrouwbaarheid.

### 2. Anycast-routering

Om veel DNS-verkeer te verwerken, gebruiken rootservers **anycast-routering**. Meerdere servers delen daarbij hetzelfde IP-adres, maar staan op verschillende locaties. Een query wordt op basis van netwerkomstandigheden naar een geschikte server geleid. Zo wordt het verkeer efficiënt verdeeld.

Wanneer een gebruiker een DNS-query start, leidt anycast-routering het verzoek naar een beschikbare rootserver in de buurt. De netwerkinfrastructuur stuurt de query naar de server met het kortste pad. Anycast verdeelt de belasting en helpt knelpunten voorkomen.

### 3. Recursieve DNS-resolvers

Wanneer een DNS-resolver een query voor een domeinnaam ontvangt, begint hij met een recursief resolutieproces en neemt hij contact op met een rootserver.

De rootserver antwoordt met een verwijzing naar de IP-adressen van de TLD-naamservers voor het gevraagde TLD. Die servers bevatten informatie over de authoritatieve naamservers voor domeinen binnen dat TLD.

### 4. Verwijzingen en authoritatieve naamservers

Na de verwijzing van de rootserver neemt de resolver contact op met de juiste TLD-naamserver.

De TLD-naamserver antwoordt met een nieuwe verwijzing naar de IP-adressen van de authoritatieve naamservers voor het gevraagde domein.

De resolver vraagt daarna aan de authoritatieve naamservers om het IP-adres dat bij de domeinnaam hoort.

### 5. Caching en TTL

Tijdens DNS-resolutie verbetert caching de prestaties en verlaagt het de belasting op DNS-servers. DNS-resolvers slaan koppelingen tussen domeinnamen en IP-adressen op.

DNS-records worden gedurende een vaste tijd gecachet. De Time-to-Live-waarde (TTL) bepaalt hoelang een record geldig blijft. Na afloop verwijdert de resolver het record en voert hij een nieuwe query uit voor het actuele IP-adres.

### 6. Samenwerking en beheer

De Internet Corporation for Assigned Names and Numbers (ICANN) en de beheerders van rootservers beheren het DNS-rootsysteem gezamenlijk.

ICANN houdt toezicht op het algemene beheer en de coördinatie van DNS en werkt samen met de beheerders van rootservers. Ze onderhouden het rootzonebestand, met informatie over de 13 DNS-rootservers en de bijbehorende IP-adressen.

De beheerders van rootservers zorgen ervoor dat de DNS-rootservers werken en beschikbaar blijven. Zo dragen ze bij aan de stabiliteit en veerkracht van de DNS-infrastructuur.

Het DNS-rootsysteem vormt het startpunt voor DNS-resolutie. Het helpt domeinnamen om te zetten in IP-adressen, zodat gebruikers efficiënt websites en andere internetbronnen kunnen bereiken.

#### De 13 DNS-rootservers

De 13 DNS-rootservers zijn aangeduid met de letters A tot en met M. Elke server wordt op verschillende fysieke locaties gehost voor redundantie en fouttolerantie. Ze verwerken queries voor de rootzone, waaronder topleveldomeinen (TLD's) zoals .com, .org, .net en landcode-TLD's zoals .us en .uk.

#### ICANN en DNS-rootbeheer

De Internet Corporation for Assigned Names and Numbers (**ICANN**) beheert en coördineert DNS en de toewijzing van IP-adressen. ICANN werkt met de beheerders van rootservers aan de stabiliteit en beveiliging van de DNS-root. Samen onderhouden ze het rootzonebestand met informatie over de 13 DNS-rootservers en hun IP-adressen.

______

## Soorten DNS-records en hun doelen

{{< youtube id="HnUDtycXSNE" >}}

DNS-records zijn essentiële onderdelen van het Domain Name System (DNS). Ze bevatten verschillende soorten informatie over een domeinnaam. Hieronder staan enkele veelvoorkomende recordtypen en hun doelen:

| DNS-recordtype | Beschrijving | Voorbeeld |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Koppelt een domeinnaam aan een IPv4-adres. | `example.com     IN A 192.0.2.1` |
| AAAA | Koppelt een domeinnaam aan een IPv6-adres. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Koppelt een alias (canonieke naam) aan de werkelijke domeinnaam. | `www.example.com IN CNAME example.com` |
| MX | Geeft aan welke mailservers inkomende e-mail voor het domein ontvangen. | `example.com     IN MX 10 mail.example.com` |
| TXT | Slaat willekeurige tekst op, vaak voor SPF, DKIM of domeinverificatie. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Geeft de authoritatieve naamservers voor het domein aan. | `example.com     IN NS ns1.example.com` |
| SOA | Legt globale zone-eigenschappen vast (start of authority-record). | `example.com     IN SOA ns1.example.com` |
| SRV | Geeft de locatie aan van een specifieke dienst van het domein. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Koppelt een IP-adres aan een domeinnaam (reverse DNS-lookup). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. A-record (Adresrecord)

Het **A-record** koppelt een domeinnaam aan een IPv4-adres. Dit is het eenvoudigste en meest gebruikte DNS-recordtype. Wanneer je een domeinnaam in een browser invoert, helpt het A-record de browser het IP-adres te vinden van de webserver die de site host.

### 2. AAAA-record (IPv6-adresrecord)

Het **AAAA-record** heeft hetzelfde doel als het A-record, maar koppelt een domeinnaam aan een IPv6-adres. Door de overgang naar IPv6 worden AAAA-records steeds belangrijker voor verbindingen via IPv6-netwerken.

### 3. CNAME-record (Canonieke-naamrecord)

Het **CNAME-record** maakt een alias of canonieke naam voor een domeinnaam. Gebruik het wanneer je een domein of subdomein naar een ander domein of subdomein wilt laten verwijzen. Je kunt bijvoorbeeld een CNAME-record maken dat "www" naar "mywebsite.com" laat verwijzen.

### 4. MX-record (Mailwisselrecord)

Het **MX-record** vermeldt de mailserver die inkomende berichten voor een domein ontvangt. Het geeft aan naar welke server e-mail moet worden bezorgd. Je kunt meerdere MX-records instellen met prioriteitswaarden. Die bepalen welke mailservers eerst worden geprobeerd als de primaire server niet beschikbaar is.

### 5. TXT-record (Tekstrecord)

Het **TXT-record** slaat tekstinformatie over een domein op. Het wordt vaak gebruikt voor domeinverificatie, SPF-records (Sender Policy Framework) voor e-mailauthenticatie en algemene informatie of notities.

### 6. SRV-record (Servicerecord)

Het **SRV-record** geeft de locatie aan van een specifieke dienst of bron binnen een domein. Het wordt gebruikt voor diensten zoals VoIP, chat en andere toepassingen die specifieke servers of diensten moeten vinden.

### 7. NS-record (Naamserverrecord)

Het **NS-record** vermeldt de authoritatieve naamservers voor een domein. Deze servers bevatten de DNS-records voor dat domein. Een DNS-resolver gebruikt de NS-records om de authoritatieve naamservers te vinden.

### 8. PTR-record (Verwijsrecord)

Het **PTR-record** koppelt bij reverse DNS-lookups een IP-adres aan een domeinnaam. Het wordt vaak gebruikt om de identiteit van een mailserver te controleren en spam te helpen voorkomen. Reverse DNS-lookups helpen de echtheid van een e-mailserver te valideren.

### 9. SOA-record (Start-van-bevoegdheidsrecord)

Het **SOA-record** bevat beheerinformatie over een domein. Het vermeldt onder meer de primaire authoritatieve naamserver, het e-mailadres van de domeinbeheerder en tijdsinstellingen voor de DNS-records.

Dit zijn enkele voorbeelden van de vele DNS-recordtypen. Elk record heeft een eigen functie en helpt domeinnamen efficiënt en nauwkeurig naar bijbehorende bronnen om te zetten.

______

## DNS-probleemoplossingsopdrachten voor verschillende besturingssystemen

Bij DNS-problemen helpen diagnostische opdrachten om de oorzaak te vinden. Hieronder staan veelgebruikte opdrachten voor verschillende besturingssystemen:

### Windows

#### 1. `ipconfig /flushdns`

Deze opdracht wist de DNS-cache in Windows en kan problemen met verouderde of onjuiste records oplossen. Open de Opdrachtprompt en voer de opdracht uit.

#### 2. `ipconfig /all`

Met `ipconfig /all` bekijk je gedetailleerde informatie over de netwerkinterfaces in Windows, inclusief de ingestelde DNS-servers. Zo controleer je of de juiste DNS-servers worden gebruikt.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Deze opdracht herstart mDNSResponder op macOS, het proces dat DNS-resolutie verzorgt. Zo vernieuw je de DNS-instellingen en los je soms DNS-problemen op. Open Terminal en voer de opdracht met beheerdersrechten uit.

#### 2. `nslookup`

Met de opdracht `nslookup` kun je DNS-records opvragen, DNS-resolutie testen en verbindingen met DNS-servers controleren. Open Terminal en voer `nslookup` uit, gevolgd door de domeinnaam of het IP-adres dat je wilt onderzoeken.

### Linux

#### 1. `systemd-resolve --flush-caches`

Op Linux-systemen die systemd als DNS-resolver gebruiken, wist `systemd-resolve --flush-caches` de DNS-cache. Dit kan problemen door verouderde cachevermeldingen oplossen. Open Terminal en voer de opdracht met beheerdersrechten uit.

#### 2. `dig`

De opdracht `dig` is een veelzijdig DNS-diagnosehulpmiddel voor Linux. Het geeft gedetailleerde informatie over DNS-query's, antwoorden en DNS-serverinstellingen. Gebruik `dig` om specifieke DNS-records op te vragen, DNS-resolutie te testen en DNS-problemen te onderzoeken. Open Terminal en voer `dig` uit, gevolgd door de domeinnaam of het IP-adres.

Deze opdrachten helpen DNS-problemen op verschillende besturingssystemen te diagnosticeren en op te lossen. Je krijgt inzicht in DNS-configuraties, DNS-serverinstellingen en verbindingsproblemen.

De opdrachten en opties verschillen mogelijk per versie of distributie. Raadpleeg de documentatie voor jouw versie van het besturingssysteem voor uitleg over de opdrachten en het gebruik ervan.
______


## Conclusie

Het Domain Name System (DNS) en de DNS-root spelen een centrale rol in de werking van internet. DNS geeft gebruikers toegang tot websites via leesbare domeinnamen. De DNS-root vormt de basis van de volledige DNS-hiërarchie. Als je begrijpt hoe DNS en de DNS-root werken, kun je het web beter gebruiken en de infrastructuur achter online diensten waarderen.

______

## Bronnen

- [DNS op Wikipedia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Hoe DNS werkt volgens Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Officiële website van ICANN](https://www.icann.org/)
- [beheerders van rootservers](https://www.root-servers.org/)
