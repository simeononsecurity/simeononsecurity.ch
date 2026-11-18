---
title: "Docker in LXC op Proxmox: betrouwbaarheid, bewijs en VM-migratie"
date: 2026-09-16
lastmod: 2026-11-13
toc: true
draft: false
description: "Beoordeel Docker binnen Proxmox LXC aan de hand van een gedocumenteerde AppArmor-fout, een zorgvuldige lezing van een melding over een vastlopende host, diagnosecommando’s en een migratieplan naar een VM."
genre: ["Virtualisatie", "Linux-beheer", "thuislab"]
tags: ["Docker in een LXC-container", "Docker op Proxmox", "LXC-container op Proxmox", "Docker-virtuele machine", "betrouwbaarheid van homelabs", "Proxmox-host loopt vast", "Debian-VM voor Docker", "niet-geprivilegieerde containers", "geneste containers", "isolatie van de Linux-kernel", "AppArmor", "runc", "lxc-pve", "Docker Compose", "Docker-opslagstuurprogramma’s", "containerd-imageopslag", "geheugendruk", "Linux PSI", "persistent journaal", "Proxmox-back-ups", "back-ups van bind mounts", "VM-migratie", "foutdomeinen", "GPU-doorvoer", "problemen met de thuisserver oplossen"]
cover: "/img/cover/docker-lxc-vm-homelab-isolation.webp"
coverAlt: "Isometrische illustratie van een thuisserver met geneste workloadvakken en een afzonderlijk VM-compartiment dat op gedeelde hardware is aangesloten"
coverCaption: "Conceptuele illustratie van gedeelde hardware en verschillende grenzen voor workloadisolatie"
---
**Docker binnen Linux Containers (LXC)** vraagt weinig extra infrastructuur, maar vergroot het aantal interacties tussen de applicatieruntime en de Proxmox-host. Voor Docker-diensten waar je huishouden op rekent, is een Debian-**virtuele machine (VM)** een praktisch vertrekpunt. De gastkernel staat los van de hostkernel en maakt de omgeving die je tijdens probleemoplossing moet nabouwen eenvoudiger. Dit artikel bekijkt de aangeleverde video, controleert het onderliggende incidentverslag en voegt gedocumenteerde fouten en een migratieplan toe.

<!--more-->

## Belangrijkste punten

- **Onderscheid fouttypen:** Een Docker-startfout, een vastgelopen VM en een niet-reagerende fysieke host vragen elk om een ander onderzoek.
- **Beoordeel het bewijs:** Stabiliteit na een migratie ondersteunt een herstelbesluit, maar bewijst de oorspronkelijke oorzaak niet.
- **Controleer actuele documentatie:** Native ondersteuning voor OCI-images en Docker binnen LXC zijn verschillende implementatieroutes.
- **Bescherm persistente gegevens:** Proxmox-back-ups en Compose-bestanden dekken niet automatisch elke locatie met applicatiegegevens.
- **Test het herstelplan:** Meet herstel, gedrag na opnieuw opstarten en beschikbaarheid voordat je de oude implementatie buiten gebruik stelt.

## Voordat je begint

**Niveau:** Gemiddeld. **Doelgroep:** Proxmox-beheerders die kiezen tussen geneste Docker en Docker in een VM. Je moet een Compose-project, een containermount en een Linux-shellprompt herkennen voordat je de diagnosevoorbeelden volgt.

**Geschatte inspanning:** Reken op 30–60 minuten voor inventarisatie en bewijsverzameling. De migratietijd hangt af van de databasegrootte, opslagdoorvoer, hardwaretoegang en het onderhoudsvenster dat je kiest. De voorbeelden hieronder zijn gedocumenteerde procedures en illustratieve redeneringen, geen benchmarks uit een lab voor dit artikel.

| Vereiste | Waarom dit belangrijk is |
|---|---|
| **Toegang tot de hostconsole** | Onderscheidt een netwerkstoring van een vastloper van de hele host |
| **Actuele back-ups** | Biedt een herstelroute voordat je de implementatie wijzigt |
| **Container- en VM-ID’s** | Richt hostcommando’s op de bedoelde workload |
| **Inventaris van applicatiegegevens** | Brengt volumes, bind mounts, databases en externe afhankelijkheden in kaart |
| **Afzonderlijke testomgeving** | Maakt een migratierepetitie mogelijk zonder dubbele schrijvers in productie |

## Bekijk de bronvideo

{{< youtube id="XyPBHhZg0Ok" enable="true" title="Proxmox: The Hidden Danger of Running Docker Inside LXC" description="Een uitleg over Docker genest in Proxmox LXC, terugkerende hostvastlopers en een migratie naar Debian-VM’s" uploadDate="2026-09-15T17:00:09-07:00" >}}

**Bronvideo:** [Proxmox: The Hidden Danger of Running Docker Inside LXC](https://www.youtube.com/watch?v=XyPBHhZg0Ok), gepubliceerd op 15 september 2026 door *Proxmox x Kubernetes x Homelab x Backup*. De centrale vraag is hoeveel operationele onzekerheid een architectuur met lager resourcegebruik met zich meebrengt.

**Afbakening van het bewijs:** De video vertelt over een incident en stelt lessen voor. De volgende secties onderscheiden de waarnemingen van de eigenaar, gedocumenteerd softwaregedrag en aanbevelingen die daaruit volgen.

## Wat het incident aantoont

Het oorspronkelijke verslag beschrijft een **host met een Intel Core i3-13100 en BIOSTAR H610MHP**. De eigenaar meldde terugkerende vastlopers die beheerstoegang en LXC-diensten troffen. Een aangesloten beeldscherm reageerde niet meer, hoewel het verslag uitdrukkelijk vermeldt dat syslog uitvoer bleef produceren. Dat is specifieker dan stellen dat er helemaal geen logs waren. [Oorspronkelijk Proxmox-forumverslag](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

De eigenaar meldde later **verbetering na de migratie**. In een vervolgbericht van 3 augustus beschreef die de verplaatsing van Docker-workloads naar Debian-VM’s en het stopzetten van de LXC’s met Docker. Op het moment van de update waren er volgens de eigenaar geen nieuwe vastlopers. De video noemt een stabiele periode van 16 dagen. Geen van beide uitspraken bevat een gecontroleerde reproductie of wijst een specifiek defect onderdeel aan. [Vervolgbericht van de eigenaar in dezelfde discussie](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

| Waarneming | Wat dit ondersteunt | Wat dit niet aantoont |
|---|---|---|
| **Lange uptime in het begin** | De eerdere combinatie van workload en software werkte succesvol | Betrouwbaarheid na elke latere update |
| **Host en diensten lopen vast** | De uitval gaat verder dan één applicatie | Docker als hoofdoorzaak |
| **Migratie gaat vooraf aan verbetering** | Een bruikbare operationele workaround | Welke gewijzigde interactie de trigger wegnam |
| **Zestien stabiele dagen** | Een begrensde observatieperiode | Oplossing van elk storingspatroon van twee tot drie weken |

De **observatieperiode** verdient aandacht. Zestien dagen valt binnen een terugkeerinterval van 14–21 dagen. Een langere observatieperiode over meerdere eerdere storingsintervallen, met vergelijkbare workloads en regulier onderhoud, vergroot het vertrouwen. Ook dan ontbreekt nog een gecontroleerde demonstratie van oorzaak en gevolg.

**Operationeel succes en bewijs van de hoofdoorzaak** zijn aparte uitkomsten. Het herstellen van betrouwbare diensten in huis is een geldige reden om te migreren. Beschrijf het resultaat als verbeterde waargenomen betrouwbaarheid totdat sterker bewijs het mechanisme aantoont.

## Bepaal de kernelgrens

```text
Docker in LXC:
Applicatie -> Docker-runtime -> LXC-naamruimten en beleid
                -> Proxmox-hostkernel -> fysieke hardware

Docker in een VM:
Applicatie -> Docker-runtime -> gast-Linuxkernel
                -> virtuele hardware / KVM-QEMU
                -> Proxmox-hostkernel -> fysieke hardware
```

**LXC** gebruikt de hostkernel. Namespaces, control groups, capabilities, seccomp en beveiligingsprofielen beperken processen zonder een aparte kernel te leveren. Docker binnen LXC voegt een extra containerlaag toe rond workloads die dezelfde onderliggende hostkernel gebruiken. [LXC-architectuur en isolatiefuncties](https://linuxcontainers.org/lxc/introduction/)

Een **VM** voegt een gastkernel toe. Een storing in de gastkernel treft normaal gesproken de VM, terwijl Proxmox de andere gasten blijft beheren. De VM blijft afhankelijk van de fysieke host, hypervisor, opslag en het netwerk. Hardwarestoringen en defecten in de hostkernel blijven gedeelde afhankelijkheden.

| Grens | Docker binnen LXC | Docker binnen een VM |
|---|---|---|
| **Kernel die applicaties gebruiken** | Proxmox-hostkernel | Gastkernel |
| **Omgeving van de Docker-runtime** | Beperkt door het beleid van de buitenste container | Geïnstalleerd in een conventioneel gastbesturingssysteem |
| **Updates van de gastkernel** | Gekoppeld aan de hostkernel | Beheerd binnen de gast |
| **Uitval van de fysieke host** | Stopt afhankelijke workloads | Stopt afhankelijke workloads |

Een VM beperkt **een deel van de foutdoorgifte**, maar niet alles. Een crash van een applicatieproces binnen LXC laat Proxmox niet automatisch crashen. Als je alle thuisdiensten in één Docker-VM zet, blijven ze wel afhankelijk van één gastbesturingssysteem en één onderhoudsschema.

Lees voor de **bredere conceptuele vergelijking** [Docker-containers versus virtuele machines](/articles/docker-vs-vms/). Hier gaat de keuze over de plaats van Docker binnen Proxmox en de gevolgen daarvan voor de grenzen van probleemoplossing.

## Omschrijf ondersteuning precies

**“Niet ondersteund”** vereist een benoemd onderdeel en een versie. Onderscheid een door de leverancier aanbevolen implementatie, gedocumenteerde functies, onderhoud door de distributie en een contractueel recht op ondersteuning. Een werkende geneste stack bewijst niet dat alle combinaties even goed worden getest. Een aanbeveling voor VM’s betekent ook niet dat beheerders elke fout rond nesting afwijzen.

**De actuele Proxmox-documentatie** maakt een belangrijk onderscheid. De broncode voor de container-toolkit beschrijft ondersteuning voor **Open Container Initiative (OCI)**-applicatie-images als een technologiepreview. De images worden daarbij omgezet naar het LXC-framework. Voor eisen rond isolatie en live migratie raadt Proxmox ook containers binnen een QEMU-VM aan. Een OCI-image in dit framework importeren verschilt van Docker Engine installeren en Compose uitvoeren in een LXC-gast. [Documentatie van de Proxmox-containerhulpmiddelen](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

| Implementatie | Te controleren vraag |
|---|---|
| **Traditionele LXC-gast** | Passen het OS-template en de applicatie binnen de gedocumenteerde containerbeperkingen? |
| **Docker genest in LXC** | Welke combinaties van kernel, runtime, beveiligingsbeleid en opslag zijn getest? |
| **Native import van een OCI-image** | Biedt de geïnstalleerde Proxmox-versie de gedocumenteerde functie en het benodigde gedrag? |
| **Docker binnen een Debian-VM** | Voldoet de gastrelease aan de installatievereisten van Docker? |

Docker publiceert een **installatieroute voor Debian**. Gebruik de lijst met ondersteunde releases en de repository-instructies voor de gast. Leg vast welke versies je installeert in plaats van ervan uit te gaan dat een oudere handleiding nog klopt. Dit biedt een gedocumenteerde installatiebasis, geen uptimegarantie of automatisch betaald ondersteuningscontract. [Docker Engine op Debian](https://docs.docker.com/engine/install/debian/)

## Een bevestigde nestingfout

De **runc/AppArmor-incompatibiliteit uit 2025** is een verifieerbaar voorbeeld. De runc-beheerders documenteerden een fout bij het opnieuw openen van een descriptor binnen een buitenste container met een AppArmor-profiel. AppArmor zag toegang onder **`/proc/sys`** ten onrechte als toegang onder **`/sys`**, waardoor het beleid de toegang weigerde. [runc-probleem 4968](https://github.com/opencontainers/runc/issues/4968)

Bij een **getroffen startpoging** verscheen dit foutfragment:

```text
open sysctl net.ipv4.ip_unprivileged_port_start file: reopen fd 8: permission denied
```

De vastgelegde fout voorkwam het **starten van containers**. Ze verklaart de hostvastlopers van de eigenaar uit het forum niet. In de issue staat **`lxc-pve 6.0.5-2`** als Proxmox-oplossing voor dit specifieke probleem. De bijbehorende upstreamwijziging in LXC is op 20 november 2025 samengevoegd. *Dit zijn historische verwijzingen naar oplossingen, geen advies om een huidige installatie op een pakketversie vast te zetten.* [Samenvatting van de beheerders over de oplossing](https://github.com/opencontainers/runc/issues/4968), [samengevoegde LXC-wijziging](https://github.com/lxc/lxc/pull/4609)

De les is **afstemming tussen afhankelijkheden**. Een wijziging in runtimebeveiliging botste met het beleid van de buitenste container. De oplossing vereiste werk in een andere laag. Installeer de passende onderhouden pakketupdate voor jouw release. Schakel AppArmor niet blijvend uit en behoud geen oude, kwetsbare runtime.

> **Belangrijkste punt:** Dit incident toont een echt compatibiliteitsprobleem met geneste containers en een echte reactie van de beheerders. Het bewijst geen algemene instabiliteit van LXC en verklaart geen afzonderlijke hostvastloper.

## Vergelijk de werkelijke kosten

Meet efficiëntie met je **eigen workload**. Vergelijk onder gelijke omstandigheden de geheugendruk op de host, CPU-belasting, opslaglatentie, reactietijden van applicaties en herstelwerk. Toegewezen VM-geheugen, vrij geheugen in de gast en resident geheugen op de host zijn verschillende metingen.

| Vermeende besparing | Te verzamelen meting | Extra kosten om vast te leggen |
|---|---|---|
| **Minder geheugenoverhead** | Geheugengebruik en druk op de host bij dezelfde workload | Tijd voor het beheren van geneste limieten en het diagnosticeren van conflicten |
| **Snellere implementatie** | Tijd tot een werkende dienst met herstelde gegevens | Tijd om na een mislukte update opnieuw op te bouwen |
| **Eenvoudiger hardware delen** | Benodigde apparaten, rechten en succesvolle werking van de applicatie | Afhankelijkheid van hostdrivers en migratiebeperkingen |
| **Eenvoudiger back-ups** | Een succesvolle hersteltest van alle vereiste gegevens | Externe mounts en consistentie van applicatiegegevens |

Docker documenteert standaard **onbeperkt CPU- en geheugengebruik**, tenzij je limieten instelt. Bij LXC voegt de buitenste container eigen limieten toe. Bij een VM vormt de geheugentoewijzing aan de gast een extra capaciteitsgrens. De gast heeft ook capaciteit nodig voor het besturingssysteem, Docker, caches en piekbelasting van applicaties. [Docker-resourcebeperkingen](https://docs.docker.com/engine/containers/resource_constraints/)

**Hardwaretoegang** is een eis van de workload. Een grafisch apparaat van de host met een container delen en een PCI-apparaat aan een VM toewijzen vereisen verschillende driver- en isolatieconfiguraties. Noteer het exacte apparaat en de toepassingseis voordat je kiest. Een mediaworkload die hardwaredecodering vereist, heeft bijvoorbeeld na de migratie een geslaagde decodeertest nodig, naast gewone HTTP-gezondheidscontroles.

Vermijd **algemene overheadcijfers**. Dit artikel noemt geen vaste geheugentoeslag of prestatiepercentage. Daarvoor zijn een gecontroleerde workload, configuratie en meetmethode nodig. Gebruik hieronder in je beslisdocument een resultaat uit je eigen vergelijking.

## Verzamel bewijs per laag

**Begin op de Proxmox-host** met een beheerdersshell. Vervang **`101`** door het ID van de LXC die je onderzoekt:

```bash
pveversion -v
uname -r
pct config 101
journalctl --list-boots
journalctl -k -b -1 --no-pager
```

**`pveversion -v`** registreert de versies van de geïnstalleerde Proxmox-onderdelen. **`pct config`** registreert de configuratie van de buitenste container. In **`journalctl`** selecteert **`-k`** kernelmeldingen, **`-b -1`** selecteert de vorige boot en **`--no-pager`** geeft gewone terminaluitvoer. Meldingen van de vorige boot vereisen bewaarde journalgegevens. [Proxmox-hulpmiddelen](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), [journalctl-referentie van systemd](https://github.com/systemd/systemd/blob/main/man/journalctl.xml)

**Inspecteer daarna de Docker-host** binnen de LXC of VM waar de daemon draait:

```bash
docker version
docker info
docker compose version
docker ps -a
docker stats --no-stream
```

Leg **beide omgevingen** vast. Alleen de container-imagetag vermeldt Docker, containerd, runc, de hostkernel, het beveiligingsbeleid en de opslagbackend niet. Noteer het tijdstip van het incident, recente updates en of de lokale hostconsole reageerde. Verwijder aanmeldgegevens en privégegevens over applicaties voordat je diagnosemateriaal publiceert.

**Inspecteer een specifieke workload** en vervang **`app`** door de containernaam:

```bash
docker inspect --format '{{json .State}}' app
docker inspect --format '{{.RestartCount}}' app
docker inspect --format '{{json .Mounts}}' app
```

**`docker inspect`** toont de status, het aantal herstarts en mountgegevens van de genoemde container. Gebruik het aantal herstarts als aanwijzing om met logs te vergelijken, niet als bewijs van een defect op hostniveau. Een opnieuw aangemaakte container begint ook een nieuwe geschiedenis. [Naslag voor docker inspect](https://docs.docker.com/reference/cli/docker/inspect/)

## Onderscheid druk van vastlopers

**Leg op de host Linux-drukgegevens vast** terwijl het probleem zich ontwikkelt:

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

**Pressure Stall Information**, oftewel PSI, rapporteert hoeveel tijd taken verliezen doordat ze op resources wachten. De velden **`some`** en **`full`** beschrijven verschillende stallcondities. **`avg10`**, **`avg60`** en **`avg300`** vatten recente intervallen samen. Geheugendruk verschilt van geheugengebruik. Een grote cache alleen toont geen tekort aan. [Linux-PSI-documentatie](https://docs.kernel.org/accounting/psi.html)

| Bewijs | Bruikbare interpretatie | Volgende controle |
|---|---|---|
| **Eén container stopt herhaaldelijk** | Fout in de applicatie of containerruntime | Afsluitstatus, servicelogs, herstartbeleid |
| **SSH faalt, console werkt** | Fout in het netwerk of beheerkanaal | Linkstatus, NIC-driver, bridge, firewall |
| **Memory PSI stijgt onder belasting** | Taken verliezen tijd door geheugenconflicten | Limieten, reclaim-activiteit, OOM-registraties, groei van de workload |
| **Opslagverzoeken lopen vast** | Een I/O-afhankelijkheid vertraagt werk | Apparaatstatus, opslaglogs, latentie en wachtrijen |
| **Watchdog meldt een lockup** | De kernel-detector zag een gedefinieerde stallconditie | Volledige trace, kernelversie, reproduceerbare trigger |
| **Geen laatste logregel** | Het verzamelen van bewijs stopte voordat bruikbare uitvoer verscheen | Persistente of externe registratie vóór een herhaling |

Een **Linux-lockupmelding** heeft een technische betekenis. Kernel-watchdogs onderscheiden soft- en hard-lockups. Een time-out in een browser bewijst geen van beide. Het ontbreken van een watchdogmelding bewijst evenmin dat de host gezond bleef. [Documentatie over Linux-lockupdetectie](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)

**Wijzigingen in firmware en energietoestanden** zijn experimenten. Noteer de vorige instelling, de reden voor de wijziging en de observatieperiode. Een CPU-idletoestand uitschakelen verandert het energieverbruik en thermisch gedrag. Een melding over een andere machine is onvoldoende bewijs om overal dezelfde instelling aan te raden.

## Bruikbare logs bewaren

**Persistente journaling** vergroot de kans dat bewijs na een herstart beschikbaar blijft. Een configuratiebestand voor journald gebruikt deze instelling:

```ini
[Journal]
Storage=persistent
```

**`Storage=persistent`** vraagt om opslag van journalgegevens op schijf wanneer die beschikbaar is. Stel tegelijk retentielimieten en beschikbare schijfruimte in. Controleer daarna of eerdere boots verschijnen in **`journalctl --list-boots`**. Persistente logging is nog steeds afhankelijk van de host die schrijfacties voltooit voordat de storing optreedt. [Configuratie van systemd-journald](https://github.com/systemd/systemd/blob/main/man/journald.conf.xml)

**Externe observatie** voegt een ander perspectief toe. Monitor de dienst vanaf een andere machine en noteer tijdstempels. Een monitor op de falende Proxmox-host valt bij dezelfde storing weg. Daardoor helpt die minder om downtime van ontbrekende telemetrie te onderscheiden.

**Illustratieve test:** Plan vanaf een ander systeem een lichte HTTP-controle en vergelijk storingen vervolgens met de bereikbaarheid van de host en het gedrag van de lokale console. Een time-out van de applicatie terwijl de host reageert vraagt om een ander onderzoek dan gelijktijdige uitval van applicatie, beheer en console. Dit is een diagnostisch ontwerp, geen waargenomen resultaat van het bronincident.

## Plan een gecontroleerde migratie

Begin met **één Compose-project met laag risico**. Bereid een Debian-VM voor met een release uit de installatiedocumentatie van Docker. Regel back-ups en stel de resourcetoewijzing in. Houd de oorspronkelijke implementatie beschikbaar voor terugdraaien totdat de vervanging de tests doorstaat. [Installatie-instructies van Docker voor Debian](https://docs.docker.com/engine/install/debian/)

**Inventariseer het Compose-project** vanuit de werkmap:

```bash
docker compose config --quiet
docker compose config --images
docker compose config --volumes
```

**`--quiet`** valideert de configuratie zonder uitvoer te tonen. **`--images`** toont gebruikte images en **`--volumes`** toont benoemde volumes. Deze commando’s exporteren geen applicatiegegevens en leveren geen volledige inventaris van bind mounts. Bekijk ook het Compose-bestand en de mounts van elke container. [Referentie voor docker compose config](https://docs.docker.com/reference/cli/docker/compose/config/)

| Gegevens of afhankelijkheid | Migratieactie |
|---|---|
| **Compose-definities** | Verplaats projectbestanden en behoud de geteste configuratie |
| **Geheimen en omgevingsvariabelen** | Maak vereiste waarden opnieuw aan met het gekozen proces voor geheimbeheer |
| **Benoemde volumes** | Maak back-ups en herstel de inhoud volgens applicatieconsistente procedures |
| **Paden met bind mounts** | Verplaats of koppel de brongegevens opnieuw en controleer het eigenaarschap |
| **Databases** | Gebruik de ondersteunde back-up- en herstelprocedure of een procedure voor een stilgelegde kopie |
| **Apparaten en gedeelde opslag** | Herstel de toegang en test het gedrag van de applicatie |
| **Poorten en DNS** | Bereid het vervangende adres voor en plan de omschakeling |

**Volumes** blijven bestaan nadat containers verdwijnen, maar migreren niet vanzelf. Een Compose-bestand benoemt resources en definieert diensten. De volume-documentatie van Docker beschrijft aparte procedures voor het maken van back-ups en het herstellen van persistente inhoud. Ga er niet van uit dat het opnieuw aanmaken van het project de gegevens herstelt. [Levenscyclus en back-ups van Docker-volumes](https://docs.docker.com/engine/storage/volumes/)

Controleer apart de **dekking van Proxmox-back-ups**. De back-updocumentatie sluit de inhoud van apparaten en bind mounts uit van containerback-ups. Een geslaagde back-up van het rootbestandssysteem van een LXC bewijst dus niet dat elke daarin gekoppelde map is beschermd. [Proxmox-back-updocumentatie](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

### Controleer opslag vóór kopiëren

**Controleer de echte opslagconfiguratie van Docker** op elke Docker-host:

```bash
docker info
findmnt -T /var/lib/docker
```

**`findmnt`** geeft het bestandssysteem aan waarin het opgegeven pad staat. Vervang **`/var/lib/docker`** als je daemon een andere dataroot gebruikt. Controleer indien nodig ook het opslagpad van containerd. Docker beschrijft het verschil tussen de containerd-imageopslag en klassieke storage drivers, met vereisten per backend. [Keuze van Docker-opslagbackend](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

**Maak images opnieuw aan en herstel applicatiegegevens** volgens de gedocumenteerde procedures van de gekozen backend. Een actieve Docker-datamap kopiëren tussen verschillende opslagconfiguraties veronderstelt meer over metadata, mountstatus en consistentie. Dit verschilt van een back-up van een gegevensvolume nadat de applicatie is gestopt.

### Schakel om met terugdraaiplan

1. **Oefen het herstel** in de VM met aparte adressen en waar nodig testgegevens.
2. **Stop schrijfacties in productie** tijdens het afgesproken onderhoudsvenster en maak de laatste consistente back-up.
3. **Herstel en valideer** applicatiegegevens, rechten, aanmeldgegevens en vereiste hardwaretoegang.
4. **Schakel de routering van diensten om** nadat de vervanging de applicatiespecifieke controles doorstaat.
5. **Laat het origineel gestopt** en bewaar de configuratie en herstelgegevens.
6. **Leg terugdraaiafspraken vast** voor gegevens die na de omschakeling zijn geschreven, voordat je het oude systeem opnieuw start.

Voorkom **twee actieve schrijvers** naar dezelfde databaseopslag. Bij terugdraaien na nieuwe productiegegevens is een plan nodig om die schrijfacties te bewaren of bewust te verwerpen. Een oude container opnieuw starten brengt twee uiteenlopende gegevensgeschiedenissen niet samen.

## Test meer dan uptime

**Acceptatietests** volgen het doel van de dienst. Een groene containerstatus toont dat een proces draait. Een bruikbare dienst vereist ook de gegevens, netwerktoegang, afhankelijkheden en herstelmogelijkheden.

| Controle | Te bewaren bewijs |
|---|---|
| **Werking van de applicatie** | Een geslaagde echte transactie, query of mediahandeling |
| **Volledigheid van gegevens** | Verwachte records, bestanden, rechten en recente wijzigingen |
| **Herstart van de gast** | Diensten komen terug zonder handmatige reparatie |
| **Herstel uit een back-up** | De herstelde kopie doorstaat dezelfde functionele controle |
| **Representatieve belasting** | Latentie, CPU, geheugendruk en opslaggedrag |
| **Onderhoudsrepetitie** | Een geteste update en een bruikbare herstelprocedure |
| **Langere observatie** | Beschikbaarheidsregistraties over meerdere eerdere storingsintervallen |

**Voorbeeldbesluit:** Een cameraservice en een experimentele downloader delen nu één geneste stack. Beide naar één VM verplaatsen verbetert de scheiding van kernels, maar houdt de gastonderhoudsgrens gedeeld. Als beschikbaarheid van de camera prioriteit heeft, beoordeel dan afzonderlijke onderhoudsgroepen en resourcelimieten. Test vervolgens de continuïteit van opnamen tijdens updates van de downloader.

**Verwachte redenering:** Kies de plaats op basis van de serviceafhankelijkheid die je wilt isoleren. Twee VM’s op één fysieke server delen nog steeds stroom, opslag en hostkernel. Als de serverstoring ook moet worden overleefd, is een extra onafhankelijk systeem of een aanvaardbare handmatige terugval nodig.

## Leg je besluit vast

**Gebruik gemeten bewijs** om een implementatie te kiezen en vast te leggen wanneer je die opnieuw beoordeelt:

```text
Gevolgen voor dienst en huishouden:
Huidige versies van host / kernel / LXC / Docker:
Vereiste toegang tot GPU, apparaten en netwerk:
Gemeten geheugen, CPU, opslag en latentie:
Bekend storingssignaal en herhalingsinterval:
Back-updekking en bewijs van geslaagde herstelactie:
Gekozen architectuur en reden:
Toegestane onderbrekingsperiode en hersteldoel:
Procedure voor omschakeling en gegevensrollback achteraf:
Acceptatietests en observatieperiode:
Voorwaarde die een nieuwe architectuurbeoordeling vereist:
```

**Kies bewust voor LXC-nesting** als de voordelen het integratiewerk rechtvaardigen en je de herstelroute hebt getest. Kies een VM als een conventionele Docker-gastomgeving en aparte gastkernel de dienst eenvoudiger maken. Geen van beide keuzes vervangt back-ups, monitoring en hostonderhoud.

## Gebruik een wijzigingspoort vóór migratie

Behandel migratie als een **gecontroleerde wijziging**, niet als bewijs voor de oorzaak van het oorspronkelijke incident. Leg vóór de omschakeling de containerconfiguratie, image-digests, bind-mountpaden, omgevingssleutels, apparaatkoppelingen en de laatste geslaagde hersteltest vast. Vergelijk na de omschakeling dezelfde servicecontroles en resourcemetingen. Laat de oude workload gestopt totdat de nieuwe kopie de acceptatieperiode doorstaat.

Keert het incident na de migratie terug, vergelijk dan de hostkernel, opslag, geheugendruk, apparaattoegang en Docker-versies van beide implementaties. De vergelijking vernauwt het onderzoek. Een geslaagde migratie wordt pas een oorzakelijk experiment als de relevante variabelen onder controle bleven.

## Volgende stappen

**Inventariseer eerst één dienst.** Breng de persistente gegevens, fysieke afhankelijkheden, storingssymptomen en het hersteldoel in kaart. Oefen een herstel voordat je beslist of migratie nodig is.

Bekijk voor **verwant werk** de [Proxmox VE-upgradegids](/articles/proxmox-ve-8-to-9-upgrade-guide/) voor upgradeplanning en de [beveiligingsgids voor Docker en Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/) voor het beveiligen van workloads. Houd architectuurkeuze, upgrade-uitvoering en incidentdiagnose gescheiden en baseer elke beslissing op eigen bewijs.

## Bronnen en bewijs

**Onderzoek gecontroleerd:** 16 september 2026. Het aangeleverde transcript bepaalde het onderwerp. De videometadata, het oorspronkelijke incidentverslag, de upstream-issue en de officiële documentatie zijn afzonderlijk gecontroleerd. Illustratieve oefeningen en voorgestelde validatiestappen zijn in de tekst aangeduid.

| Bron | Rol |
|---|---|
| **[Bronvideo](https://www.youtube.com/watch?v=XyPBHhZg0Ok)** | Oorspronkelijke uitleg en de gemelde stabiliteitsperiode |
| **[Proxmox-forumdiscussie over de storing](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)** | Waarnemingen uit de eerste hand en de migratie-update |
| **[Proxmox-containerhulpmiddelen](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)** | Containerarchitectuur en huidig OCI-onderscheid |
| **[runc-probleem 4968](https://github.com/opencontainers/runc/issues/4968)** | Gedocumenteerde startfout en historische pakketoplossing |
| **[LXC-wijzigingsverzoek 4609](https://github.com/lxc/lxc/pull/4609)** | Samengevoegde upstreamwijziging in AppArmor |
| **[Docker-documentatie](https://docs.docker.com/engine/install/debian/)** | Installatiebasis voor de gast, met specifieke verwijzingen naar runtime en opslag hierboven |
| **[Linux-PSI-documentatie](https://docs.kernel.org/accounting/psi.html)** | Interpretatie van resourcebelasting |
| **[Linux-watchdogdocumentatie](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)** | Gedefinieerde kernel-lockupcondities |
| **[Proxmox-back-updocumentatie](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)** | Uitsluitingen voor containermounts en back-upgedrag |
