---
title: "VLAN-segmentatie voor een homelab plannen en testen"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Maak een VLAN-plan om vertrouwde apparaten, servers, IoT en gasten in je homelab te scheiden. Leg toegestaan verkeer vast, configureer het netwerk stap voor stap en test de isolatie."
genre: ["Homelab", "Netwerkbeveiliging", "Netwerken"]
tags: ["homelab VLAN", "VLAN-segmentatie", "IoT-netwerk", "gastnetwerk", "homelab-firewall", "inter-VLAN-routering", "802.1Q", "netwerkisolatie", "VLAN-test", "pfSense VLAN", "accesspoort", "trunkpoort", "firewallregels", "homelab-beveiliging", "netwerkplan", "subnet", "DHCP", "DNS", "managed switch", "draadloze SSID"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Een homelab-router en -switch scheiden laptops, servers, IoT-apparaten en gasten in beveiligde netwerkzones."
coverCaption: "Plan de VLAN-grenzen en test daarna elk toegestaan en geblokkeerd pad."
---

Een homelab plaatst laptops, servers, camera's en gastapparaten vaak op één netwerk. **VLAN-segmentatie** verdeelt deze groepen over afzonderlijke netwerken. Een router, firewall of layer-3-switch routeert verkeer ertussen. Firewallregels of toegangscontrolelijsten van de switch bepalen welke gerouteerde stromen zijn toegestaan. Deze handleiding helpt je een plan op te stellen, één wijziging tegelijk uit te voeren en het resultaat te testen.

## Belangrijkste punten

- **Groepeer op basis van vertrouwen:** plaats beheerapparaten, servers, IoT en gasten op afzonderlijke netwerken als hun toegangsbehoeften verschillen.
- **Leg toegestane paden vast:** noteer de bron, bestemming, dienst en reden voor elke verbinding tussen netwerken.
- **Configureer beide lagen:** VLAN-instellingen van de switch en het access point plaatsen apparaten. Firewallregels of toegangscontrolelijsten van de switch beheren gerouteerd verkeer.
- **Test beide uitkomsten:** controleer vanaf elk relevant netwerk een toegestane en een geblokkeerde verbinding.

## Voordat je begint

Je hebt een router of firewall met VLAN-interfaces nodig, of een layer-3-switch die VLAN-routering en toegangscontrolelijsten ondersteunt. Een managed switch transporteert bekabelde VLAN's. Als je draadloze clients scheidt, heb je ook een access point met VLAN-gekoppelde draadloze netwerken nodig. Houd tijdens de configuratiewijziging een apparaat op het huidige beheernetwerk. Sla eerst de instellingen van de router, switch en het access point op. De stappen hieronder gebruiken een **voorbeeldplan**. Pas adressen en poorten dus aan je apparatuur aan.

Een **VLAN-interface** is de verbinding van de gateway met een VLAN. De gateway kan een router, firewall of layer-3-switch zijn. Een **DHCP-scope** is het adresbereik dat een DHCP-service aanbiedt aan apparaten op dat netwerk. Een **DHCP-relay** stuurt adresverzoeken van een VLAN door naar een DHCP-server op een ander netwerk. Gebruik een relay als de gateway geen adressen voor dat VLAN uitdeelt en de DHCP-server elders staat. De [DHCP-relaygids van Juniper](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) beschrijft dit pad. Een draadloze **SSID** is de netwerknaam waarmee clients verbinding maken. Als je apparatuur geen managed switch of VLAN-geschikt access point heeft, begin dan met het ingebouwde gastnetwerk en controleer de isolatie voordat je hardware koopt of wijzigt.

Lees eerst [subnetten en VLAN's](/articles/networking-basics-what-are-subnets-and-vlans/) als je de basistermen nodig hebt. De [gids voor netwerksegmentatie](/articles/how-to-perform-network-segmentation-for-improved-security/) van de site behandelt het bredere beveiligingsconcept. CISA beschrijft aparte thuisnetwerken voor gasten en Internet of Things-apparaten in de [beveiligingsrichtlijn voor mobiele federale werkplekken](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Waarschuwing:** Een VLAN-wijziging op de poort voor je beheerverbinding kan je buitensluiten. Houd fysieke toegang en een bekende herstelroute beschikbaar totdat alle netwerken de tests doorstaan.

Exporteer vóór je een kabel verplaatst de configuratie van elk apparaat en noteer het huidige beheer-IP-adres, de switchpoort, de VLAN-instelling en de beheerderslogin. Laat één werkende beheerpoort en laptop op het oorspronkelijke netwerk staan. Als een wijziging de toegang verbreekt, sluit de laptop weer aan op die poort, herstel de opgeslagen instelling of configuratie en controleer of de oude gateway reageert voordat je het opnieuw probeert. Als het beheernetwerk van de switch onbereikbaar is, gebruik dan de gedocumenteerde console- of lokale herstelprocedure. Reset apparatuur niet voordat je weet wat die reset wist.

## Apparaten en verkeer inventariseren

Noteer elk apparaat, het huidige adres, de eigenaar en de benodigde diensten. Geef elk apparaat een reden om een ander netwerk te bereiken. Een laptop kan bijvoorbeeld een server beheren, terwijl een camera alleen een recorder en DNS-server nodig heeft. Een gasttelefoon heeft internet nodig, maar geen toegang tot servers.

| Apparaatgroep | Voorbeelden | Vereiste toegang |
|---|---|---|
| **Beheer** | Beheerlaptop, beheer van switch en access point | Router, switch, access point, serverbeheer |
| **Servers** | Hypervisor, NAS, back-updoel | Updates, DNS, goedgekeurd applicatieverkeer |
| **IoT** | Camera's, slimme stekkers, media-apparaten | DNS, tijdservice, specifieke controller of recorder |
| **Gasten** | Telefoons en laptops van bezoekers | Internet, DNS, geen toegang tot privénetwerken |

Noteer uitzonderingen voordat je regels toevoegt. Lokale ontdekkingsfuncties, zoals casten naar een scherm, zijn vaak afhankelijk van multicastverkeer dat standaard geen gerouteerde grens passeert. Sta niet al het verkeer tussen VLAN's toe om één ontdekkingsprobleem op te lossen. Stel het protocol vast en voeg de kleinst mogelijke ondersteunde uitzondering toe.

## VLAN's en adressen toewijzen

Geef elke groep een VLAN-ID en een apart IP-subnet. Dit **voorbeeldplan** gebruikt adressen die zijn gereserveerd voor documentatie en gaat ervan uit dat de router DHCP en DNS levert. Neem de tabel niet over in een actief netwerk zonder adresconflicten te controleren.

| Netwerk | VLAN-ID | Subnet | Voorbeeldgateway |
|---|---:|---|---|
| **Beheer** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Servers** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Gasten** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Deze documentatieranges illustreren alleen de indeling, zoals vastgelegd in [RFC 5737](https://www.rfc-editor.org/info/rfc5737). Gebruik privé-adressen uit [RFC 1918](https://www.rfc-editor.org/info/rfc1918) voor je lab, met een niet-overlappend subnet per VLAN. Noteer elk echt gatewayadres, DHCP-pool, DNS-adres en apparaatreservering in je plan.

**Accesspoorten** vervoeren het netwerk van één apparaat zonder VLAN-tag. **Trunkpoorten** vervoeren geselecteerde getagde VLAN's tussen router, switch en access point. Stel aan beide kanten dezelfde VLAN-ID en dezelfde native of ongemarkeerde instelling in. De [VLAN-switchgids van Netgate](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) beschrijft getagde trunks, ongemarkeerde accesspoorten en poort-VLAN-ID's. Gebruik standaard-VLAN 1 niet voor beheer als je hardware een apart VLAN ondersteunt, zoals beschreven in de [VLAN-beveiligingsgids van Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/security.html).

**Native** of **ongemarkeerd** verkeer op een trunk heeft geen VLAN-tag. Beide uiteinden moeten dit aan hetzelfde VLAN toewijzen, anders kan een apparaat in het verkeerde netwerk terechtkomen. Sta alleen VLAN's toe die de verbinding nodig heeft. Schakel ongebruikte switchpoorten uit of wijs ze toe aan een beperkt netwerk. Netgate raadt ook af om een VLAN als volledige beveiligingsgrens te behandelen wanneer een aanvaller een switchpoort beheert. Bescherm fysieke poorten en apparaatwachtwoorden naast gerouteerd verkeer.

## Een verkeersmatrix opstellen

Een VLAN scheidt op zichzelf alleen broadcastdomeinen. **Inter-VLAN-routering** op de router of layer-3-switch vereist nog steeds toegangsregels. Bepaal welk apparaat tussen VLAN's routeert. Als een layer-3-switch lokaal routeert, bereikt verkeer tussen zijn VLAN's mogelijk nooit de routerfirewall. Pas gelijkwaardige toegangscontrolelijsten toe op de switch of routeer via de firewall, en test daarna op het echte handhavingspunt. Controleer de richting van de switch-ACL en of deze verbindingsstatus bijhoudt. Veel switch-ACL's beoordelen pakketten per richting afzonderlijk, waardoor een toegestane verbinding een beperkte regel voor retourverkeer nodig kan hebben. De [ACL-gids van Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) beschrijft interfaceriale richting en geordende pakketmatches. Gebruik de apparaatlijst om de verbindingen vast te leggen die je wilt toestaan. De onderstaande regels zijn voorbeelden, geen universele regelset.

| Bron | Bestemming | Dienst | Beslissing |
|---|---|---|---|
| **Beheer** | Beheerinterface van server | TCP 443 | Toestaan voor goedgekeurde beheerapparaten |
| **Beheer** | Beheerinterfaces van router, switch en access point | Hun gedocumenteerde beheerpoorten | Toestaan voor goedgekeurde beheerapparaten |
| **IoT** | Camerarecorder | Gedocumenteerde poort van de recorder | Alleen toestaan indien nodig |
| **IoT** | Goedgekeurde DNS- en tijdservice | DNS en NTP | Alleen toestaan naar de gekozen diensten |
| **IoT** | Beheernetwerk | Alles | Weigeren |
| **Gasten** | Privénetwerken | Alles | Weigeren |
| **Gasten** | DNS en internet | DNS, webverkeer | Toestaan via goedgekeurde resolver en gateway |

Neem ook de eigen diensten van de router op in het plan. Een regel die IoT-toegang tot andere VLAN's blokkeert, kan de beheerinterface van de router nog steeds bereikbaar laten. Beperk beheerdiensten tot het beheernetwerk. Begin met alleen de vereiste toestaanregels en een standaardblokkade voor ander gerouteerd verkeer. Controleer bestaande brede toestaanregels voordat je ervan uitgaat dat de standaard alles weigert. De [firewallrichtlijnen van Netgate](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) wijzen erop dat een standaard pfSense-LAN een toestaanregel heeft. De [regelmethodiek van pfSense](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) legt uit dat interfaceregels verkeer filteren dat de interface binnenkomt en dat toegestane verbindingen een status voor retourverkeer aanmaken.

De voorbeeldtabel behandelt IPv4. Als je netwerk IPv6 gebruikt, wijs dan elk VLAN een IPv6-prefix en -beleid toe, controleer routeradvertenties en test ook toegestane en geblokkeerde IPv6-paden. Een IPv4-blokkade bewijst geen IPv6-isolatie. Als je IPv6 niet wilt routeren, controleer dan de IPv6-instellingen van de router en clientadressen in plaats van aan te nemen dat IPv6 ontbreekt. Netgate documenteert [IPv6-firewallgedrag](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) en [routeradvertenties](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Eén netwerk tegelijk configureren

1. Kies de gateway voor het VLAN. Als de router of firewall routeert, maak daar dan een VLAN-interface en wijs het gatewayadres toe. Routeert een layer-3-switch het VLAN, maak de interface dan op die switch. Configureer een DHCP-scope op de gateway of een DHCP-relay naar je bestaande DHCP-server. Controleer of een goedgekeurde DNS-resolver bereikbaar is. De [VLAN-configuratiegids van Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) beschrijft interface- en servicestappen voor een pfSense-gateway.
2. Als de router de VLAN-gateway is, voeg het VLAN dan toe aan de trunk tussen router en switch. Als de layer-3-switch de gateway is, laat de switch het gatewayadres voor dat VLAN beheren en routeer naar de router of firewall via een apart transitnetwerk of gerouteerde uplink. Geef de switch een standaardroute naar de upstreamrouter. Geef de router via de switch een retourroute voor elk VLAN waarvan de gateway op de switch staat. Controleer het firewallbeleid van de router en uitgaande NAT voor die subnetten als ze internet nodig hebben. Maak niet op beide apparaten hetzelfde gatewayadres of dezelfde DHCP-scope aan. De [inter-VLAN-routeringsgids van Cisco](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) toont VLAN-gateways op de switch. Netgate documenteert [retourroutes](https://docs.netgate.com/pfsense/en/latest/routing/static.html) en [uitgaande NAT](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) voor netwerken achter een interne router. Voeg het VLAN toe aan de relevante switch-access-point-trunk als draadloze clients dat netwerk nodig hebben.
3. Wijs een test-accesspoort of draadloze SSID aan het VLAN toe. Sluit een niet-kritiek testapparaat aan op die poort of SSID.
4. Voeg de bedoelde firewallregels of switch-ACL's toe op het apparaat dat het VLAN routeert. Controleer of ander gerouteerd verkeer wordt geweigerd. Controleer ACL-richting en retourverkeer als de switch geen status bijhoudt. Test toegang tot elke gateway en beheerinterface, elk lokaal subnet en IPv6 waar aanwezig. Sta alleen de paden uit je verkeersmatrix toe. Beperk beheer tot het beheernetwerk. Controleer de volgorde van regels en verwijder of beperk bestaande brede toestaanregels pas nadat het testbeheerpad werkt.
5. Controleer of het testapparaat een adres, gateway en DNS-server uit het bedoelde subnet ontvangt. Voer daarna de verbindingscontroles hieronder uit voordat je meer apparaten verplaatst.

Verplaats het laatste beheerapparaat pas als het vervangende pad werkt. Sla de werkende configuratie op nadat elk netwerk de tests doorstaat. Als DHCP, DNS of beheeruit toegang faalt, sluit het testapparaat dan opnieuw aan op de oorspronkelijke poort of SSID, herstel de laatste switch- of routerwijziging vanuit de opgeslagen configuratie en test het oorspronkelijke netwerk opnieuw voordat je verdergaat.

## Isolatie en toegang testen

Gebruik een dienst die je beheert en waarvan je weet dat die op de bestemming luistert. Vervang op een Windows-testapparaat het voorbeeldadres en de poort door een echte server en voer uit:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

Het veld **`TcpTestSucceeded`** geeft aan of een TCP-verbinding tot stand kwam. De [Microsoft-referentie voor Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) beschrijft de parameters `-ComputerName` en `-Port`. Een mislukte verbinding bewijst op zichzelf niet dat een firewallregel werkte. De dienst kan gestopt zijn of de hostfirewall kan het verkeer weigeren. Controleer de doeldienst en het netwerkfirewalllog voordat je een conclusie trekt.

Test vanaf een apparaat dat werkelijk met elk bron-VLAN is verbonden. Noteer vóór elke test het bronadres, de gateway en de DNS-server. Controleer een toegestane verbinding naar de bedoelde dienst, een geblokkeerde verbinding naar een interne dienst buiten de matrix, een DNS-query via de bedoelde resolver en internettoegang waar gepland. Controleer bij een VLAN met een gateway op de switch de standaardroute van de switch, de retourroute van de router en het pad terug vanaf de bestemming als een toegestane verbinding faalt. Herhaal toegestane en geblokkeerde tests met IPv6-adressen als IPv6 actief is. In pfSense tonen **Status > Systeemlogboeken > Firewall** de gelogde toestaan- en blokkeeracties. De [firewallloggids van Netgate](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) beschrijft deze weergave. Vergelijk bron, bestemming, poort en regel in het log met je test. Als de test onverwacht slaagt, controleer dan brede toestaanregels en bestaande statusvermeldingen. Start na regelwijzigingen een nieuwe verbinding, omdat een bestaande verbinding via de eerdere status kan blijven werken.

Voer voor een DNS-controle op Windows `nslookup example.com` uit en vergelijk de weergegeven server met je geplande resolver. Probeer daarna een query vanaf een gast- of IoT-client waar DNS beperkt is. Een geslaagde query bewijst niet dat de client de gekozen resolver heeft gebruikt. Controleer daarom de getoonde server en een firewall- of resolverlog. Test afzonderlijk als te blokkeren geval directe toegang tot het beheeradres van de router vanaf een IoT- of gastapparaat.

Apparaten op **hetzelfde VLAN** kunnen verkeer uitwisselen zonder de routerfirewall te passeren. Test clientisolatie op het lokale netwerk afzonderlijk als je access point dat biedt en gebruik hostfirewalls op servers. Firewalltests tussen VLAN's bewijzen geen isolatie binnen hetzelfde VLAN.

> **Verwacht resultaat:** Elk apparaat ontvangt een adres uit het geplande subnet. Toegestane diensten werken. Geblokkeerde pogingen komen overeen met een firewallblokkade of een gelijkwaardige gedocumenteerde controle.

## Problemen oplossen

- **Geen adres:** controleer het VLAN van de accesspoort of SSID, trunk-tags, DHCP-scope en gateway-interface.
- **Adres werkt, DNS niet:** controleer het resolveradres, de servicebinding van de router en de firewallregel voor DNS-verkeer.
- **Een apparaat bereikt onverwacht een ander VLAN:** controleer routerregels, brede toestaanregels en of beide apparaten nog hetzelfde ongemarkeerde netwerk delen.
- **Geen firewalllog voor gerouteerd verkeer:** controleer of een layer-3-switch of alternatieve gateway de verbinding routeerde voordat deze de firewall bereikte.
- **Een VLAN met gateway op de switch bereikt lokale netwerken, maar geen internet:** controleer de standaardroute van de switch, retourroutes van de router, firewallbeleid en uitgaande NAT voor het VLAN-subnet.
- **IPv4 is geblokkeerd, maar de verbinding werkt:** controleer IPv6-adressen, routeradvertenties, IPv6-regels en bestaande statusvermeldingen.
- **Een geblokkeerde test loopt vast zonder firewalllog:** bevestig dat de doeldienst luistert. Controleer daarna routering en loginstellingen. De [firewallprobleemgids van Netgate](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) beschrijft controles van logs en status.
- **Casten of ontdekken werkt niet meer:** stel het ontdekkingsprotocol en het controllerpad vast voordat je een beperkte uitzondering toevoegt.

## Volgende stappen

Bewaar de apparaatlijst en verkeersmatrix bij je netwerkdiagram. Bekijk regels opnieuw wanneer je een server of IoT-apparaat toevoegt. Herhaal na elke relevante netwerkwijziging een toegestane en een geblokkeerde verbindingstest. Lees voor de bredere ontwerpprincipes verder bij [netwerksegmentatie](/articles/how-to-perform-network-segmentation-for-improved-security/).
