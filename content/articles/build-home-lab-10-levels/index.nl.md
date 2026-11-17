---
title: "Bouw een homelab in 10 niveaus, van Pi-hole tot lokale AI"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Bouw een homelab in tien praktische stappen, van netwerkbrede DNS-filtering tot lokale AI, met hardware, kosten, vaardigheden en afwegingen per niveau."
genre: ["Homelab", "Zelf hosten", "Lokale AI", "Thuisnetwerken"]
tags: ["homelab", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "lokale AI", "stroomverbruik"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Een homelab groeit van een kleine Raspberry Pi en router uit tot opslag, servers, netwerkapparatuur en een werkstation voor lokale AI."
coverCaption: ""
---

Bouw een homelab in 10 niveaus, van Pi-hole tot lokale AI
=========================================================

Een **homelab** is een verzameling computers en diensten die je zelf beheert om alledaagse problemen op te lossen en echte systemen te leren beheren. Je kunt advertenties blokkeren, lampen automatiseren, media voor je gezin opslaan of virtuele machines testen. **Begin met één nuttige taak.** Voeg hardware toe zodra je een echte beperking merkt.

Deze gids loopt van een kleine Raspberry Pi met Pi-hole tot een server met lokale AI-modellen. **Elk niveau voegt mogelijkheden en een nieuwe verantwoordelijkheid toe.** De kostenramingen hieronder gebruiken een illustratief stroomverbruik en een voorbeeldtarief van $0.15 per kilowattuur. Controleer je lokale tarief en meet je apparatuur voordat je meer koopt.

## Niveau 1: Blokkeer advertenties op je thuisnetwerk

Installeer [Pi-hole](https://docs.pi-hole.net/) op een Raspberry Pi of een andere kleine Linux-computer. Pi-hole werkt als een **DNS-sinkhole**. Wanneer een apparaat het adres opvraagt van een domein op een blokkeerlijst, geeft Pi-hole geen bruikbare bestemming terug. Je browser, telefoon en smart-tv gebruiken hetzelfde filter wanneer je router of DHCP-server clients naar Pi-hole verwijst.

**DNS-filtering** werkt ook buiten webbrowsers, waaronder bij sommige advertenties in apps en smart-tv's. Inhoud op paginaniveau valt buiten het filter, dus advertenties die vanaf hetzelfde domein als een site of app worden geleverd, komen door. Een blokkeerlijst verhindert soms dat een aanmelding, video of betaling laadt. Controleer het querylogboek van Pi-hole, sta zo nodig het specifieke domein toe en houd een terugvalplan voor DNS klaar bij storingen.

Het stroomverbruik is bescheiden. Voor een apparaat van 8 watt dat een hele maand draait, is de schatting 8 W × 24 uur × 30 dagen ÷ 1.000 × $0.15 = **ongeveer $0.86 per maand**. Meet de volledige voeding aan het stopcontact. Een tweede computer, USB-schijf of inefficiënte adapter verandert het totaal.

**Je leert:** DNS, DHCP, blokkeerlijsten en basisonderhoud van Linux.

## Niveau 2: Automatiseer slimme apparaten lokaal

Voeg [Home Assistant](https://www.home-assistant.io/) toe. Het brengt compatibele slimme apparaten en automatiseringen samen in één systeem. Plan dat lampen bij bedtijd uitgaan. Zet een ventilator aan wanneer een temperatuursensor een ingestelde waarde overschrijdt. Stuur jezelf een melding wanneer een leksensor water detecteert. **Deze kleine automatiseringen leveren direct voordeel op.**

**Lokale bediening** houdt veel automatiseringen in huis actief wanneer een externe dienst of internetverbinding uitvalt. Het gedrag hangt af van het apparaat. Sommige producten vereisen nog steeds een leveranciersaccount, clouddienst of internetverbinding voor de installatie en functies op afstand. Controleer de vereisten van de integratie voordat je hardware koopt.

**Maak een back-up van Home Assistant** en bewaar een kopie buiten de host. Documenteer integraties en herstelstappen. Een defecte SD-kaart of mini-pc mag je configuratie niet wissen.

**Je leert:** apparaat-integraties, triggers, voorwaarden en herstel vanaf back-ups.

## Niveau 3: Draai meerdere diensten op één mini-pc

Een **gebruikte zakelijke mini-pc** biedt vaak uitbreidbaar geheugen, vervangbare opslag en bruikbare poorten voor een lage tweedehandsprijs. Een Intel N100-mini-pc verbruikt vaak minder stroom en neemt weinig ruimte in. Intel noemt de N100 een processor met vier cores, vier threads, een TDP van 6 watt en ondersteuning voor maximaal 16 GB geheugen. De processorrating is niet hetzelfde als het stroomverbruik van het complete systeem aan het stopcontact. Vergelijk de exacte computer, het geheugen, de opslag, de garantie en de netwerkpoorten.

Installeer Linux en gebruik [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) om afzonderlijke diensten als **containers** uit te voeren. Een container verpakt een toepassing en de bijbehorende afhankelijkheden, terwijl die de kernel van het hostbesturingssysteem deelt. Je kunt bijvoorbeeld een wachtwoordbeheerder zoals het door de community onderhouden project Vaultwarden draaien, samen met een uptime-monitor zoals Uptime Kuma. **Behandel de wachtwoordbeheerder als een gevoelige dienst:** beperk de toegang, gebruik sterke authenticatie, installeer updates en bewaar een versleutelde back-up.

**Containers vervangen updates of back-ups niet.** Geef elke dienst een vaste opslaglocatie en leg herstelstappen vast. Een kleine mini-pc heeft ook grenzen. Meerdere databases, mediaconversies of grote toepassingen kunnen geheugen, opslag of CPU-tijd uitputten.

**Je leert:** Linux-beheer, containers, volumes, updates en herstel van diensten.

## Niveau 4: Bouw een thuisbibliotheek met media

[Jellyfin](https://jellyfin.org/docs/) is een opensource-mediaserver. [Plex](https://support.plex.tv/) biedt een gepolijst ecosysteem van clients en optionele functies op basis van een account. Beide ordenen persoonlijke bibliotheken en streamen media naar ondersteunde clients. **Kies op basis van je clients**, je model voor toegang op afstand, hardwareondersteuning en benodigde functies.

**Je opslagbehoefte** hangt af van de omvang en kwaliteit van je verzameling. Begin alleen met één schijf als je al een apart back-upplan hebt. Gebruik consistente mapnamen en metadata zodat de server films en afleveringen correct herkent.

**Direct afspelen** stuurt een compatibel bestand naar de client zonder de videostream te wijzigen. **Transcodering** zet audio of video om wanneer de client, verbinding, ondertiteling of kwaliteitsinstelling een ander formaat vereist. Transcodering belast de server extra. Test je apparaten en netwerk voordat je een GPU of snellere CPU koopt. **Sla een aparte mediaserver over** wanneer alle clients je bestanden direct afspelen en één host aan je behoeften voldoet.

**Je leert:** mediaformaten, opslagplanning, netwerkdoorvoer en workloadtests.

## Niveau 5: Voeg opslagredundantie en een aparte back-up toe

Een NAS met twee schijven en **gespiegelde opslag** schrijft gegevens naar beide schijven. Valt één schijf uit, dan bevat de andere een actuele kopie terwijl je de defecte schijf vervangt en de spiegel opnieuw opbouwt. Spiegelen beschermt de beschikbaarheid bij uitval van één schijf. **Een spiegel herstelt geen** verwijderd bestand, draait geen versleuteling door ransomware terug en beschermt niet tegen diefstal, brand of een stroomincident dat beide schijven beschadigt.

Bewaar een **aparte back-up** op een ander apparaat of een andere locatie. Neem belangrijke documenten, foto's, configuratie-exporten en servicegegevens op. Gebruik een back-upschema en bewaar versies zodat onbedoelde wijzigingen niet elke goede kopie overschrijven.

**Test een herstel.** Kies een paar bestanden, herstel ze naar een aparte map en open ze. Herstel bij een dienst de gegevens naar een testinstantie of documenteer de stappen en controleer elk bestand. Een back-up die je nooit hebt teruggezet, is een aanname en geen herstelplan.

**Je leert:** bestandssystemen, schijven vervangen, back-ups roteren en herstel testen.

## Niveau 6: Leer virtualisatie met een klein Proxmox-cluster

[Proxmox VE](https://pve.proxmox.com/pve-docs/) draait virtuele machines en containers op serverhardware. Meerdere mini-pc's die als **cluster** zijn gekoppeld, delen één beheerweergave en bieden gelegenheid om nodes, opslag en migratie te leren kennen. Een cluster is een groep servers die is ingesteld om samen te werken. De leden voegen hun geheugen niet samen tot één grote pool. **Voor hoge beschikbaarheid is** extra planning en geschikte gedeelde of gerepliceerde opslag nodig.

Een **snapshot** registreert de staat van een virtuele machine op een bepaald moment. Zo kun je terugkeren naar een eerdere staat na een wijziging in je lab. Snapshots zijn meestal afhankelijk van de oorspronkelijke opslag. Het zijn geen zelfstandige back-ups. **Kopieer belangrijke gegevens naar een afzonderlijk back-updoel** en test het herstel.

Elke node voegt stroomverbruik, netwerkpoorten, kabels en updates toe. Drie kleine computers betekenen ook drie systemen om bij te werken en problemen mee op te lossen. Eén mini-pc met enkele virtuele machines leert veel van dezelfde basisprincipes tegen lagere kosten. **Voeg nodes toe wanneer** experimenten isolatie vereisen of je clusterbeheer wilt oefenen.

**Je leert:** virtuele machines, opslagpools, snapshots, lidmaatschap van het cluster en node-onderhoud.

## Niveau 7: Voeg privétoegang op afstand en netwerkscheiding toe

[Tailscale](https://tailscale.com/kb/) verbindt je goedgekeurde apparaten via een privénetwerk. Zo krijg je onderweg toegang tot geselecteerde diensten thuis. **Beperk de toegang** tot de apparaten en diensten die ieder nodig heeft. Beveilig accounts met multifactorauthenticatie en controleer oude apparaten en sleutels.

Een beheerde switch of router met **VLAN-ondersteuning** scheidt groepen apparaten. Zet slimme stekkers en andere apparaten met weinig vertrouwen op een ander netwerk dan computers met persoonlijke bestanden. Plaats opslag op een netwerk dat alleen bereikbaar is voor systemen die toegang nodig hebben. Segmentatie beperkt welke apparaten met elkaar communiceren. Houd ook updates, sterke wachtwoorden en toegangsregels bij.

**Stel het beheerpaneel niet rechtstreeks bloot aan het openbare internet** tenzij je de authenticatie-, patch- en firewallvereisten van de dienst begrijpt. Ook een hulpmiddel voor privénetwerktoegang vereist zorgvuldig beheer van accounts en apparaten.

**Je leert:** privétoegang, identiteitsgebonden machtigingen, VLAN's, firewallregels en vertrouwensgrenzen voor apparaten.

## Niveau 8: Voeg een bedrijfsserver toe

Stap over op een grotere server wanneer je meetbaar meer CPU-cores, geheugen, schijfbays, PCIe-slots of netwerkcapaciteit nodig hebt. Oudere bedrijfsservers kosten tweedehands vaak minder, maar hun ventilatoren maken veel geluid en **het verbruik in rust loopt op tot ongeveer 100 à 160 watt**, afhankelijk van het model en de onderdelen. Zie deze bandbreedte als een schatting, niet als een specificatie.

Bereken vóór aankoop een jaarlijkse schatting voor stroomkosten:

`gemeten watt ÷ 1.000 × 24 × 365 × elektriciteitstarief per kWh`

Bij 120 watt en $0.15 per kWh is de schatting 1.051 kWh per jaar, oftewel ongeveer **$158 per jaar**. Meet de exacte server in rust en tijdens je gebruikelijke workload. Neem ook schijven, koeling en UPS-verbruik mee.

Controleer de diepte van de behuizing, schijfcompatibiliteit, geluid, ventilatorregeling, voeding en uitbreidingskaarten. Een server die je ruimte- of stroomlimiet overschrijdt, is geen praktische upgrade.

**Je leert:** serverhardware, beheer op afstand, uitbreidingen, koeling en schattingen van gebruikskosten.

## Niveau 9: Meet het stroomverbruik en schaal je lab passend

Gebruik een **stekker-wattmeter** om elke computer in rust en tijdens normaal werk te meten. Maak een lijst van de grootste verbruikers. Bekijk de energie-instellingen van het BIOS, verwijder ongebruikte kaarten en schijven en verplaats dagelijkse diensten terug naar efficiënte mini-pc's wanneer bedrijfsserverhardware niet nodig is.

Laat de grote server alleen draaien wanneer een workload zijn capaciteit nodig heeft. Documenteer bij een wake-on-LAN-schema of bediening op afstand de herstelstappen bij netwerk- of stroomstoringen. Houd een **lijst van serviceafhankelijkheden** bij zodat uitschakelingen geen opslag of netwerk onderbreken die andere systemen nodig hebben.

Een rack helpt apparatuur en luchtstromen te organiseren wanneer rackmount-hardware de ruimte rechtvaardigt. Een UPS overbrugt korte storingen en geeft systemen tijd om netjes af te sluiten. Beide kosten extra geld, ruimte en stroom. **Meet hun verbruik** en neem batterijvervanging mee in het langetermijnbudget.

**Je leert:** energie meten, energiebeheer, afhankelijkheden in kaart brengen en capaciteit plannen.

## Niveau 10: Draai AI-modellen lokaal

[Ollama](https://docs.ollama.com/) downloadt ondersteunde taalmodellen en draait ze op je computer. **Lokale inferentie** houdt prompts en uitvoer op hardware die jij beheert wanneer je een lokaal model en een lokale toepassing gebruikt. Controleer of het volledige softwarepad lokaal blijft. Een verbonden toepassing, telemetrieoptie of cloudmodel stuurt gegevens buiten je netwerk.

Hardwarevereisten hangen af van modelgrootte, kwantisatie, contextlengte en gewenste snelheid. **Systeemgeheugen of GPU-geheugen moet** modelgewichten en werkcontext kunnen bevatten. Kleine computers draaien kleinere modellen. Grotere modellen en langere contexten vereisen meer geheugen en vaak een geschikte GPU. Meet het stroomverbruik tijdens inferentie. Een systeem met GPU verbruikt vaak veel meer stroom dan een mini-pc in rust.

Lokale modellen zijn geschikt voor taken als concepten schrijven, privénotities samenvatten en eenvoudige classificatie wanneer de kwaliteit aan je eisen voldoet. Ze geven onjuiste antwoorden en kleinere modellen hebben vaak moeite met complex redeneren of actuele feiten. Cloudmodellen presteren soms beter op specifieke taken. **Vergelijk kwaliteit, privacy, latentie, kosten en stroomverbruik** voordat je beslist waar een workload draait.

**Je leert:** modelgeheugen, kwantisatie, inferentie, privacygrenzen en workloadbeoordeling.

## Vergelijk de tien niveaus

**Kosten zijn schattingen, geen offertes.** Hardwareprijzen verschillen per regio, staat en opslagconfiguratie. Bereken elektriciteitskosten met `watt ÷ 1.000 × uren × dagen × tarief per kWh`. Meet waar mogelijk bij het stopcontact en neem uren in rust mee, omdat veel homelabservers de klok rond draaien.

### Mogelijkheden en hardware

| Niveau | Nieuwe mogelijkheid | Typische hardware |
|---|---|---|
| **1** | DNS-filtering voor het netwerk | Raspberry Pi of kleine Linux-host |
| **2** | Lokale automatisering van apparaten | Pi of mini-pc, compatibele apparaten |
| **3** | Meerdere zelfgehoste apps | Gebruikte zakelijke mini-pc of N100-systeem |
| **4** | Persoonlijke mediastreaming | Mini-pc met mediaopslag |
| **5** | Tolerantie voor schijfuitval en herstel | NAS met twee schijven plus aparte back-up |
| **6** | Lab met virtuele servers | Twee of meer mini-pc's |
| **7** | Privétoegang en segmentatie | Tailscale, beheerde router of switch |
| **8** | Hoge capaciteit en uitbreidingen | Bedrijfsserver |
| **9** | Lager energieverbruik van het lab | Wattmeter, afgestemde systemen |
| **10** | Lokale modelinferentie | Pc met veel geheugen, optionele GPU |

### Vaardigheden, kosten en afwegingen

| Niveau | Aangeleerde vaardigheden | Schatting van terugkerende kosten | Belangrijkste afweging |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Ongeveer $1 per maand bij 8 W en $0.15/kWh | Sommige advertenties blijven, foutieve blokkeringen vragen aandacht |
| **2** | Integraties, triggers, back-ups | Hoststroom plus apparaatkosten | Compatibiliteit en werk aan back-ups |
| **3** | Docker, updates, opslag | Hangt af van gemeten systeemverbruik | Grenzen van CPU, geheugen en schijf |
| **4** | Formaten, organisatie, transcoding | Opslag en serverstroom | Transcoding vereist soms krachtigere hardware |
| **5** | Spiegelen, bewaren, herstellen | NAS-stroom, schijven, back-updoel | Een spiegel is geen back-up |
| **6** | Proxmox, VM's, clusters | Elke node voegt stroom en onderhoud toe | Meer nodes betekenen meer onderhoud |
| **7** | Toegangsregels, VLAN's, firewall | Netwerkapparatuur en servicekosten | Verkeerd ingestelde regels stellen diensten bloot |
| **8** | Hardware, koeling, beheer op afstand | Verschilt per server, bereken op basis van gemeten verbruik | Geluid, warmte en verbruik in rust |
| **9** | Meten, plannen, passend schalen | Eenmalige kosten van de meter, besparing varieert | Planning voegt operationele stappen toe |
| **10** | Modellen inzetten en beoordelen | Stroomverbruik van computers en opslag | Kwaliteit en snelheid hangen af van hardware |

## Kies de volgende nuttige upgrade

**Stop op het niveau dat aan je huidige behoeften voldoet.** Pi-hole en één mini-pc kunnen genoeg zijn voor je diensten. Een NAS is nuttig wanneer je gedeelde opslag en een getest herstelplan nodig hebt. Voeg een cluster of bedrijfsserver toe wanneer een workload of leerdoel dat rechtvaardigt.

Noteer **waar de gegevens van elke dienst staan, hoe je updates uitvoert en hoe je herstelt.** Test back-ups voordat je apparatuur toevoegt. Laat de volgende echte beperking je volgende aankoop bepalen.

## Bronnen

- [Pi-hole-documentatie](https://docs.pi-hole.net/)
- [Home Assistant-documentatie](https://www.home-assistant.io/docs/)
- [Intel Processor N100-specificaties](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker: Wat is een container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Jellyfin-documentatie](https://jellyfin.org/docs/)
- [Plex-ondersteuning](https://support.plex.tv/)
- [Proxmox VE-documentatie](https://pve.proxmox.com/pve-docs/)
- [Tailscale-documentatie](https://tailscale.com/kb/)
- [Ollama-documentatie](https://docs.ollama.com/)
