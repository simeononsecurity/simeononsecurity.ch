---
title: "Docker versus virtuele machines in 2026"
date: 2023-02-02
lastmod: 2026-11-15
toc: true
draft: false
description: "Een vergelijking van Docker-containers en virtuele machines in 2026 op prestaties, beveiliging, kosten, gebruikssituaties en inzetbaarheid."
tags: ["Docker", "Virtuele machines", "VM's", "Cloudcomputing", "Containers", "Kubernetes", "Eenvoud", "Schaalbaarheid", "Beveiliging", "Kosteneffectiviteit", "Dockerfile", "Docker versus VM", "Containers versus VM's", "Docker-containers", "Virtualisatie", "Containerisatie", "Bouwen, testen en uitrollen", "Isolatie", "Beveiligingsgeschiedenis", "Kostenvergelijking", "VMware", "Hyper-V", "KVM", "Containerorkestratie", "Microservices", "DevOps", "Infrastructuur", "Cloudapplicaties", "Prestatievergelijking", "Efficiënt gebruik van middelen", "Hybride aanpak", "Docker-prestaties", "VM-prestaties", "Wanneer Docker gebruiken", "Wanneer VM's gebruiken"]
cover: "/img/cover/An_image_of_a_cargo_ship_shaped_like_a_blue_whale_carrying.webp"
coverAlt: "Een vrachtschip in de vorm van een blauwe walvis met meerdere Docker-containers aan boord"
coverCaption: ""
---

## Docker versus virtuele machines: de complete vergelijking voor 2026

De keuze tussen **Docker-containers** en **virtuele machines (VM's)** wordt steeds specifieker naarmate cloudcomputing en het uitrollen van applicaties veranderen. Het debat over "Docker versus VM's" zette deze technologieën ooit tegenover elkaar. In 2026 is het beeld genuanceerder: beide technologieën zijn belangrijk, maar dienen verschillende doelen in moderne infrastructuur.

Deze gids vergelijkt Docker en VM's vanuit technisch, operationeel en zakelijk perspectief. Zo kun je de technologie kiezen die bij jouw gebruikssituatie past.

## De basis begrijpen

### Wat is Docker?

**Docker** is een containerplatform dat applicaties en hun afhankelijkheden verpakt in gestandaardiseerde eenheden: containers. Docker biedt:

- **Virtualisatie op applicatieniveau**: containers delen de kernel van het hostbesturingssysteem.
- **Lichtgewicht isolatie**: processen en middelen worden geïsoleerd zonder de overhead van een volledig besturingssysteem.
- **Onveranderlijke infrastructuur**: containers zijn vervangbaar en reproduceerbaar.
- **Gebruiksgemak voor ontwikkelaars**: eenvoudige declaratieve configuratie met Dockerfiles.
- **Een leidend ecosysteem**: Docker Hub biedt meer dan 13 miljoen containerimages.

In 2026 biedt Docker Engine 26.x verbeterde beveiligingsfuncties, beter middelenbeheer en goede integratie met orkestrators zoals Kubernetes en Docker Swarm.

### Wat zijn virtuele machines (VM's)?

**Virtuele machines** bootsen complete computersystemen na, inclusief hardware. Ze draaien volledige besturingssystemen boven op een hypervisor. VM's bieden:

- **Virtualisatie op hardwareniveau**: volledige isolatie van het besturingssysteem, inclusief de kernel.
- **Sterke isolatiegrenzen**: elke VM draait onafhankelijk met een eigen besturingssysteem.
- **Compatibiliteit met oudere systemen**: elk besturingssysteem op uiteenlopende hardware draaien.
- **Een volwassen ecosysteem**: decennia aan zakelijke beheer- en ondersteuningsoplossingen.
- **Bewezen betrouwbaarheid**: uitgebreid gebruikt en beproefd in bedrijfsomgevingen.

Moderne VM-technologieën zijn onder meer VMware vSphere 9, Microsoft Hyper-V 2025, KVM (Kernel-based Virtual Machine) en Proxmox VE. In 2026 bieden ze verbeterde prestaties en beheerfuncties.

### Architectuurvergelijking

#### Architectuur van Docker-containers

```
┌─────────────────────────────────────────┐
│             Appcontainer 1              │
│  ┌──────────────────────────────────┐  │
│  │        App + bibl. + afh.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│             Appcontainer 2              │
│  ┌──────────────────────────────────┐  │
│  │        App + bibl. + afh.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                 Docker                  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                 Host-OS                 │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Hardware                 │
└─────────────────────────────────────────┘
```

#### Architectuur van virtuele machines

```
┌─────────────────────────────────────────┐
│                  VM 1                   │
│  ┌──────────────────────────────────┐  │
│  │       Gast-OS + app + afh.       │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                  VM 2                   │
│  ┌──────────────────────────────────┐  │
│  │       Gast-OS + app + afh.       │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│             Hypervisor 1/2              │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                 Host-OS                 │
│                (type 2)                 │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Hardware                 │
└─────────────────────────────────────────┘
```

## Belangrijkste verschillen tussen Docker en VM's

| Kenmerk | Docker-containers | Virtuele machines |
|---------|-------------------|-------------------|
| **Opstarttijd** | 50–500 milliseconden | 30–120 seconden |
| **Vereist besturingssysteem** | Gedeelde kernel van het hostbesturingssysteem | Volledig besturingssysteem per VM |
| **Overhead van middelen** | Doorgaans circa 100 MB | Minimaal 2–8 GB |
| **Isolatieniveau** | Procesniveau | Hardwareniveau |
| **Overdraagbaarheid** | Zeer goed overdraagbaar | Minder goed overdraagbaar |
| **Dichtheid** | Doorgaans meer dan 100 per host | Doorgaans 10–20 per host |
| **Imagegrootte** | 50 MB–500 MB | 2 GB–50 GB |
| **Prestaties** | Bijna native | 5–15% overhead |
| **Afhankelijkheid bij het opstarten** | Hostbesturingssysteem | Hypervisor en gastbesturingssysteem |
| **Opslag** | Gelaagd bestandssysteem (CoW) | Volledige schijfimages |
| **Netwerken** | Bridge- en overlaynetwerken | Virtuele switches |
| **Beveiligingsisolatie** | Namespaces en cgroups | Volledige isolatie van besturingssystemen |
| **Beheercomplexiteit** | Laag tot gemiddeld | Gemiddeld tot hoog |
| **Geschikt voor** | Microservices en zonder status-apps | Monolieten, oudere systemen en meerdere besturingssystemen |

## Prestatievergelijking: benchmarks voor 2026

### Gebruik van middelen

**Docker-containers:**
- **CPU-overhead**: <1%, vrijwel native prestaties.
- **Geheugenoverhead**: 10–50 MB per container.
- **Schijf-I/O**: bijna native met de opslagdriver overlay2.
- **Netwerkprestaties**: 95–99% van bare metal.
- **Opstarttijd**: gemiddeld 200 ms voor gewone applicaties.

**Virtuele machines:**
- **CPU-overhead**: 5–10% voor de hypervisor.
- **Geheugenoverhead**: volledig besturingssysteem, minimaal 2–4 GB per VM.
- **Schijf-I/O**: 80–95% van de prestaties van bare metal.
- **Netwerkprestaties**: 85–95% van bare metal.
- **Opstarttijd**: gemiddeld 30–90 seconden.

### Vergelijking van de dichtheid

**Typische server met 64 GB RAM:**

**Met Docker-containers:**
- Hostbesturingssysteem: 4 GB.
- Docker Engine: 1 GB.
- Resterend voor containers: 59 GB.
- Gemiddelde containergrootte: 500 MB.
- **Theoretische capaciteit**: 118 containers.
- **Praktische capaciteit**: 80–100 containers met passende resourcelimieten.

**Met virtuele machines:**
- Hypervisor: 2 GB.
- Resterend voor VM's: 62 GB.
- Gemiddelde VM-grootte: 4 GB.
- **Theoretische capaciteit**: 15 VM's.
- **Praktische capaciteit**: 10–12 VM's met voldoende overhead.

### Resultaten van prestatietests (tests uit 2026)

| Test | Docker | VM (KVM) | Bare metal | Docker % | VM % |
|-----------|--------|----------|------------|----------|------|
| Gehele CPU-getallen | 98.5 | 92.3 | 100 | 98.5% | 92.3% |
| Zwevendekomma-CPU | 97.8 | 91.7 | 100 | 97.8% | 91.7% |
| Geheugenbandbreedte | 99.2 | 89.4 | 100 | 99.2% | 89.4% |
| Sequentieel lezen van schijf | 96.7 | 87.2 | 100 | 96.7% | 87.2% |
| Willekeurige schijf-I/O | 94.3 | 82.6 | 100 | 94.3% | 82.6% |
| Netwerkdoorvoer | 97.1 | 88.9 | 100 | 97.1% | 88.9% |
| Netwerklatentie | 98.4 | 90.1 | 100 | 98.4% | 90.1% |

*De tests zijn uitgevoerd op een Intel Xeon Platinum 8380 met Ubuntu 24.04 LTS (Docker) en een KVM-hypervisor (VM's).*


## Voordelen van Docker: waarom containers moderne ontwikkeling domineren

### 1. Eenvoud en ontwikkelervaring

**Eenvoud van Dockerfiles:** Docker gebruikt declaratieve configuratie via Dockerfiles. Zo wordt het verpakken van applicaties eenvoudiger:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

Met dit ene bestand leg je de volledige applicatieomgeving, afhankelijkheden en runtimeconfiguratie vast.

**Vergelijking met VM's:** om een VM te maken moet je:
- Een volledig besturingssysteem kiezen en installeren (30–60 minuten).
- Netwerken en opslag configureren.
- Afhankelijkheden van de applicatie handmatig installeren.
- Snapshots of templates maken.
- Updates en patches van het besturingssysteem beheren.

### 2. Uitstekende overdraagbaarheid

**Een keer bouwen, overal uitvoeren:** Docker-containers werken hetzelfde op:
- Laptops van ontwikkelaars met Windows, Mac en Linux.
- CI/CD-pipelineservers.
- Testomgevingen.
- Productieclouds zoals AWS, Azure en GCP.
- On-premises datacenters.
- Edge-apparaten.

**Praktijkvoorbeeld:** een ontwikkelaar bouwt een container op macOS. Dezelfde container draait zonder aanpassingen op:
- Een Linux-pipeline van GitHub Actions.
- AWS ECS voor productie.
- Azure Kubernetes Service voor staging.
- Een lokaal Kubernetes-ontwikkelcluster.

VM's vereisen platformspecifieke images en configuraties voor verschillende hypervisors.

### 3. Zeer snelle opstarttijden

**Docker-containers starten op in:**
- **Webapplicatie**: 200–500 ms.
- **Databasecontainer**: 1–3 seconden.
- **Microservice**: 50–200 ms.

**VM's starten op in:**
- **Lichte Linux-VM**: 10–30 seconden.
- **Windows Server-VM**: 45–90 seconden.
- **Volledige desktop-VM**: 60–120 seconden.

Het snelheidsverschil van meer dan 100 keer maakt het volgende mogelijk:
- **Snel schalen**: binnen enkele seconden op piekbelasting reageren.
- **Automatisch herstellen**: defecte containers direct vervangen.
- **Efficiënte CI/CD**: dagelijks duizenden testomgevingen uitvoeren.
- **Sneller ontwikkelen**: direct tussen ontwikkelomgevingen wisselen.

### 4. Efficiënt gebruik van middelen en lagere kosten

**Voordelen van Docker:**

**Geheugenbesparing:**
- 100 Node.js-microservices in Docker gebruiken ongeveer 50 GB RAM.
- Dezelfde werklast in VM's gebruikt ongeveer 400 GB RAM.
- **Besparing**: 87,5% minder geheugen nodig.

**Opslagbesparing:**
- Docker-imagelagen worden gedeeld tussen containers.
- De Ubuntu-basisimage is 50 MB en wordt gedeeld.
- Applicatielagen zijn elk 100–500 MB.
- **Resultaat**: gedeelde lagen besparen veel opslagruimte.

**Rekenvoorbeeld:** 10 Python-applicaties:
- **Docker**: één Python-basisimage van 300 MB plus 10 applicatielagen van elk 50 MB is in totaal 800 MB.
- **VM's**: 10 volledige OS-images met Python van elk 3 GB zijn samen 30 GB.
- **Besparing**: 97,3% minder opslag.

### 5. Ondersteuning voor microservicesarchitectuur

Docker vormt de basis van moderne microservices.

**Voordelen:**
- **Onafhankelijk schalen**: schaal afzonderlijke services op basis van de vraag.
- **Meerdere programmeertalen**: gebruik per service een andere taal.
- **Foutisolatie**: storingen in een service verspreiden zich niet naar andere services.
- **Continu uitrollen**: werk services afzonderlijk bij.
- **Autonomie van teams**: teams beheren de volledige stack van hun service.

**Voorbeeld van een architectuur:**

```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Frontend   │ │     API     │ │    Login    │
│   (React)   │ │  (Node.js)  │ │    (Go)     │
│    Cont.    │ │    Cont.    │ │    Cont.    │
└─────────────┘ └─────────────┘ └─────────────┘
       │               │               │
       └───────────────┴───────────────┘
                       │
            ┌──────────┴──────────┐
            │                     │
    ┌─────────────┐      ┌─────────────┐
    │    Data     │      │    Cache    │
    │ (Postgres)  │      │   (Redis)   │
    │    Cont.    │      │    Cont.    │
    └─────────────┘      └─────────────┘
```

### 6. Integratie met DevOps en CI/CD

Docker heeft CI/CD-pipelines ingrijpend veranderd.

**Voorbeeld van een moderne pipeline:**
1. **Commit**: de ontwikkelaar pusht code.
2. **Build**: de CI-server bouwt in 1–3 minuten een Docker-image.
3. **Test**: containers voeren binnen seconden geautomatiseerde tests uit.
4. **Scan**: de imagelagen worden op beveiligingsproblemen gescand.
5. **Push**: upload het image naar een containerregister.
6. **Deploy**: rol de release per instantie binnen seconden uit naar productie.
7. **Rollback**: keer zo nodig direct terug naar het vorige image.

**Vergelijking met VM's:** traditionele pipelines op basis van VM's doorlopen deze stappen:
1. **Commit**: de ontwikkelaar pusht code.
2. **VM-image bouwen**: een nieuw VM-image maken duurt 15–30 minuten.
3. **VM uitrollen**: nieuwe VM's inrichten duurt 5–10 minuten.
4. **Testen**: voer tests uit op VM's.
5. **Rollback**: de vorige VM-status herstellen duurt 10–15 minuten.

**Resultaat**: Docker-pipelines zijn 10–20 keer sneller.


## Voordelen van virtuele machines: wanneer VM's uitblinken

Ondanks de voordelen van Docker blijven VM's nodig voor specifieke situaties.

### 1. Sterkere beveiligingsisolatie

**Isolatie op hardwareniveau:** VM's bieden volledige scheiding op kernelniveau:
- Elke VM heeft een eigen kernel.
- De hypervisor dwingt grenzen af met hardwareondersteuning.
- Kwetsbaarheden in de kernel steken de grens tussen VM's niet over.
- Geschikt voor multi-tenantomgevingen met niet-vertrouwde code.

**Beveiligingsvergelijking:**

| Beveiligingsfunctie | Docker | VM's | Voordeel |
|---------------------|--------|------|----------|
| Kernelisolatie | Gedeelde kernel | Afzonderlijke kernels | VM's |
| Moeilijkheid van ontsnappen | Uitbraak uit namespace mogelijk | Ontsnappen uit hypervisor zeldzaam | VM's |
| Aanvallen op middelen | cgroup-limieten | Hardwarelimieten | VM's |
| Geschikt voor compliance | Versterking vereist | Isolatie ingebouwd | VM's |
| Multi-tenancy | Niet aanbevolen | Industriestandaard | VM's |

**Gebruikssituatie:** financiële instellingen die klantapplicaties uitvoeren, hebben vaak VM-isolatie nodig voor naleving van regelgeving en beveiligingsgaranties.

### 2. Volledige controle over het besturingssysteem en flexibiliteit

**Elk besturingssysteem uitvoeren:** VM's ondersteunen:
- Verschillende OS-families op dezelfde hardware, zoals Windows en Linux.
- Verouderde besturingssystemen, zoals Windows Server 2008 en RHEL 5.
- Gespecialiseerde distributies, zoals BSD en Solaris.
- Aangepaste kernelconfiguraties.
- Besturingssystemen met specifieke kernelmodules.

**Voorbeelden:**
- **Windows-apps op Linux-hosts**: voer Windows Server-VM's uit op een Linux-hypervisor.
- **Verouderde systemen**: behoud applicaties die een specifieke OS-versie vereisen.
- **Kerneltesten**: test aangepaste Linux-kernels veilig.
- **Ontwikkeling voor meerdere besturingssystemen**: voer macOS, Windows en Linux tegelijk uit.

### 3. Beter voor statusbehoudende en verouderde applicaties

**VM's zijn geschikt voor:**

**Statusbehoudende applicaties:**
- Traditionele SQL-databases, zoals Oracle en SQL Server.
- Bedrijfsapplicaties, zoals SAP en verouderde ERP-systemen.
- Statusbehoudende berichtensystemen.
- Applicaties die permanente lokale opslag verwachten.

**Verouderde monolieten:**
- Grote bedrijfsapplicaties die niet voor containers zijn ontworpen.
- Applicaties met hardgecodeerde bestandssysteempaden.
- Software die specifieke OS-configuraties vereist.
- Softwarelicenties die aan hardware of een OS zijn gekoppeld.

**Voorbeeld:** een bedrijf dat SAP ERP gebruikt:
- Heeft Windows of Linux met specifieke kernelparameters nodig.
- Vereist permanente opslag met bepaalde bestandssysteemtypen.
- Heeft complexe netwerkvereisten.
- Vereist aanpassingen op OS-niveau.
- **Oplossing**: een virtuele machine is de praktische keuze.

### 4. Bewezen beheer voor ondernemingen

**Volwassen beheertools:**
- **VMware vCenter**: uitgebreid beheer van datacenters.
- **Microsoft System Center**: beheer van de levenscyclus van VM's.
- **Red Hat Virtualization**: open virtualisatie voor ondernemingen.
- **Proxmox**: volledig VM-beheer.

**Functies voor ondernemingen:**
- **Live migration**: verplaats actieve VM's zonder uitval tussen hosts.
- **Hoge beschikbaarheid**: start VM's automatisch opnieuw na hardwarestoringen.
- **Disaster recovery**: maak gebruik van back-ups, snapshots en replicatie.
- **Middelenbeheer**: wijs CPU en geheugen geavanceerd toe.
- **Compliance**: ingebouwde audit- en beveiligingsfuncties.

### 5. Beter voor omgevingen met verschillende besturingssystemen

**Heterogene infrastructuur:** VM's ondersteunen soepel, op gedeelde hardware:
- Windows Server-applicaties.
- Linux-services.
- Unix-systemen, zoals AIX en Solaris.
- Netwerkapparaten.
- Alle systemen op gedeelde hardware.

**Praktijkvoorbeeld van een datacenter:**
- 50 Windows Server-VM's voor AD, Exchange en SQL Server.
- 30 Linux-VM's voor webservers en databases.
- 10 gespecialiseerde VM's voor netwerkbewaking en beveiliging.
- Alles wordt via één platform beheerd.
- Containers bieden dit niet op dezelfde manier door verschillen tussen OS-kernels.

## Gedetailleerde beveiligingsvergelijking: Docker versus VM's

### Beveiligingsmodel van Docker

**Isolatiemechanismen:**
- **Namespaces**: isolatie van processen, netwerken, mountpunten, IPC en UTS.
- **Cgroups**: middelen beperken en het gebruik ervan bijhouden.
- **Seccomp**: systeemaanroepen filteren.
- **AppArmor/SELinux**: verplichte toegangscontrole.
- **Capabilities**: fijnmazige controle over privileges.

**Aanbevolen beveiligingsmaatregelen voor Docker (2026):**
1. **Gebruik Docker zonder root**: voer containers uit als niet-rootgebruiker.
2. **Gebruik minimale basisimages**: zoals Alpine Linux en distroless.
3. **Scan images**: controleer met Trivy, Snyk of Clair op kwetsbaarheden.
4. **Onderteken images**: verifieer ze met Docker Content Trust.
5. **Beperk capabilities**: verwijder onnodige Linux-privileges.
6. **Gebruik alleen-lezenbestandssystemen**: mount containers als read-only.
7. **Segmenteer het netwerk**: gebruik geïsoleerde netwerken.
8. **Beheer geheimen**: gebruik Docker secrets of externe kluizen.

**Beveiligingsrisico's:**
- **Gedeelde kernel**: alle containers delen de hostkernel.
- **Privilege escalation**: verkeerd geconfigureerde containers kunnen ontsnappen.
- **Kwetsbaarheden in images**: niet-gepatchte basisimages.
- **Aanvallen op de daemon**: de Docker-daemon draait als root.

### Beveiligingsmodel van VM's

**Sterkere isolatie:**
- **Afzonderlijke kernels**: elke VM heeft een eigen kernel.
- **Afdwinging door hypervisor**: isolatie wordt door hardware ondersteund.
- **Geen gedeelde kernel**: kernel-exploits blijven beperkt tot één VM.
- **Volwassen beveiliging**: de beveiliging is decennialang versterkt.

**Aanbevolen beveiligingsmaatregelen voor VM's:**
1. **Gebruik Type 1-hypervisors**: VMware ESXi, KVM of Hyper-V.
2. **Beveilig de hypervisor**: houd de hypervisor gepatcht.
3. **Isoleer netwerken**: gebruik VLAN's en firewallregels.
4. **Versleutel gegevens**: versleutel opslag en geheugen.
5. **Beheer toegang**: bescherm beheer met sterke authenticatie.
6. **Versterk het gastbesturingssysteem**: installeer een minimale OS-configuratie.
7. **Patch regelmatig**: werk zowel de hypervisor als het gastbesturingssysteem bij.

**Beveiligingsvoordeel:** VM's zijn geschikt voor:
- Multi-tenant-SaaS-platforms.
- Gereguleerde sectoren, zoals financiën en gezondheidszorg.
- Het uitvoeren van niet-vertrouwde code.
- Omgevingen met hoge beveiligingseisen.

## Kostenanalyse: vergelijking van de totale eigendomskosten

### Infrastructuurkosten

**Scenario**: 100 microservices hosten.

**Docker-oplossing:**
- **Hardware**: 4 servers × $5.000 = $20.000.
- **Licenties**: Docker Enterprise, $150 per maand × 4 = $7.200 per jaar.
- **Totale infrastructuurkosten**: $27.200 in het eerste jaar, daarna $7.200 per jaar.

**VM-oplossing:**
- **Hardware**: 20 servers × $5.000 = $100.000.
- **VMware vSphere**: $3.000 per CPU × 40 CPU's = $120.000.
- **Totale infrastructuurkosten**: $220.000 in het eerste jaar, daarna $24.000 per jaar voor ondersteuning.

**Besparing**: $192.800 in het eerste jaar en daarna $16.800 per jaar.

### Operationele kosten

**Beheertijd:**

**Docker:**
- Installatie: 2–4 uur per applicatie.
- Update uitrollen: 1–5 minuten.
- Schaalactiviteiten: geautomatiseerd.
- Problemen oplossen: logs worden centraal verzameld.
- **Personeelsefficiëntie**: één engineer beheert meer dan 500 containers.

**VM's:**
- Installatie: 4–8 uur per VM.
- Update uitrollen: 15–30 minuten.
- Schaalactiviteiten: 10–30 minuten.
- Problemen oplossen: aanmelden bij elke VM.
- **Personeelsefficiëntie**: één engineer beheert 50–100 VM's.

**Voorbeeld van cloudkosten (AWS):**

**10 webapplicaties dag en nacht uitvoeren:**

**Docker op ECS Fargate:**
- Kleine containers: elk 2 vCPU en 4 GB RAM.
- Kosten per container: circa $50 per maand.
- **Totaal**: $500 per maand.

**EC2-VM's:**
- t3.large-instanties: 2 vCPU en 8 GB RAM.
- Kosten per instantie: circa $60 per maand.
- **Totaal**: $600 per maand.
- EBS-opslagkosten komen daar nog bij.

**Jaarlijkse besparing**: $1.200 plus lagere beheerkosten.

## Wanneer Docker gebruiken: geschikte situaties

### 1. Microserviceapplicaties

✅ **Ideaal voor Docker.**

**Kenmerken:**
- Kleine, onafhankelijke services.
- Ontwerp zonder status.
- Snelle schaalvergroting vereist.
- Regelmatige updates.

**Voorbeeld:** een e-commerceplatform:
- Frontendservice (React).
- Gebruikersservice (Node.js).
- Productcatalogus (Python).
- Orderverwerking (Go).
- Betaalservice (Java).
- Elke service wordt op basis van de belasting onafhankelijk geschaald.

### 2. Continue integratie en uitrol

✅ **Ideaal voor Docker.**

**Voordelen:**
- Consistente buildomgevingen.
- Tests voeren snel uit.
- Parallel testen.
- Reproduceerbare uitrol.

**CI-pipeline:**
```
git push → Image bouwen → Containers testen →
Naar register pushen → Naar staging uitrollen →
Productierollout (blue-green)
```

### 3. Ontwikkelomgevingen

✅ **Uitstekend geschikt voor Docker.**

**Voordelen:**
- Identieke ontwikkel- en productieomgevingen.
- Omgevingen snel beschikbaar maken.
- Nieuwe ontwikkelaars eenvoudig laten beginnen.
- Geen problemen van het type "werkt op mijn machine".

**Ontwikkelervaring:**
```bash
git clone repo
docker-compose up
# Omgeving klaar in 30 seconden
```

### 4. Cloudapplicaties

✅ **Docker is de standaard.**

Moderne cloudapplicaties zijn gebouwd voor:
- Kubernetes-orkestratie.
- Een service-mesharchitectuur.
- Serverless-functies.
- Een event-gedreven ontwerp.

### 5. Horizontaal schalen

✅ **Docker blinkt uit.**

Geschikt voor applicaties die nodig hebben:
- Direct opschalen tijdens verkeerspieken.
- Geografische distributie.
- Automatisch schalen op basis van belasting.
- Kosteneffectief schalen.

**Voorbeeld:** een videostreamingdienst:
- Basiscapaciteit: 50 containers.
- Piekverkeer: automatisch schalen naar 500 containers in 2 minuten.
- Na de piek: binnen 5 minuten terugschalen naar 50.

## Wanneer virtuele machines gebruiken: geschikte situaties

### 1. Verouderde bedrijfsapplicaties

✅ **VM's zijn noodzakelijk.**

**Kenmerken:**
- Monolithische architectuur.
- Functionaliteit die afhankelijk is van het besturingssysteem.
- Complexe installatieprocedures.
- Niet te containeriseren.

**Voorbeelden:**
- Traditionele ERP-systemen, zoals SAP en Oracle EBS.
- Verouderde .NET-applicaties op Windows Server.
- Applicaties die een specifieke OS-versie vereisen.
- Software met licenties op OS-niveau.

### 2. Meerdere besturingssystemen vereist

✅ **Alleen VM's werken.**

**Situaties:**
- Windows-applicaties naast Linux uitvoeren.
- Software testen op verschillende OS-versies.
- Ontwikkeling voor meerdere OS-platforms.
- Ondersteuning voor verouderde besturingssystemen behouden.

**Voorbeeld:** een softwarebedrijf test op één fysieke infrastructuur:
- Windows Server 2016-, 2019- en 2022-VM's.
- Verschillende Linux-distributies.
- Een macOS-VM voor tests van de Mac-client.
- Alle systemen op dezelfde fysieke infrastructuur.

### 3. Sterke isolatie vereist

✅ **VM's bieden sterkere isolatie.**

**Situaties:**
- Multi-tenant-SaaS-platforms.
- Gereguleerde sectoren, zoals gezondheidszorg en financiën.
- Beveiligingskritieke applicaties.
- Niet-vertrouwde code uitvoeren.

**Voorbeeld:** een cloud-IDE-dienst:
- Elke klant krijgt een eigen VM.
- Volledige isolatie voorkomt datalekken.
- Beveiliging op kernelniveau.
- Voldoet aan regels voor gegevensbescherming.

### 4. Traditionele statusbehoudende databases

✅ **VM's zijn betrouwbaarder.**

**Soorten databases:**
- Traditionele SQL-databases: Oracle, SQL Server, MySQL en PostgreSQL.
- Grote monolithische databases.
- Databases die specifieke OS-afstemming vereisen.
- Gelicentieerde databases die aan hardware zijn gekoppeld.

**Waarom VM's:**
- Integratie met permanente opslag.
- Betere prestaties voor intensieve I/O.
- Hulpmiddelen voor back-up en herstel.
- Minder complex dan databases in containers.

### 5. Noodherstel en testen

✅ **VM's bieden voordelen.**

**Voordelen van VM's:**
- Volledige systeemsnapshots.
- P2V-conversie (fysiek naar virtueel).
- Live-migratie.
- Bewezen back-upoplossingen.

**Scenario voor noodherstel:**
- Productie-VM's worden naar een noodherstelsite gerepliceerd.
- Directe failover met minimale uitvaltijd.
- Herstelprocedures zijn eenvoudig te testen.
- De volledige systeemstatus blijft behouden.


## Hybride aanpak: beide technologieën combineren

Moderne infrastructuur gebruikt steeds vaker **zowel Docker als VM's**, elk op de plek waar het past.

### Gebruikelijke hybride architectuur

```
┌─────────────────────────────────────────┐
│             Fysieke infra.              │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │        VM 1: K8s-knooppunt         │ │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ │ │
│  │  │Docker││Docker││Docker││Docker│ │ │
│  │  │Cont. ││Cont. ││Cont. ││Cont. │ │ │
│  │  └─────┘ └─────┘ └─────┘ └─────┘ │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 2: DB Oracle           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 3: Windows AD          │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### Hybride gebruikssituaties

**1. Kubernetes op VM's:**
- Voer Kubernetes-clusters uit in VM's.
- Draai Docker-containers binnen Kubernetes.
- Isoleer clusters op VM-niveau.
- Migreer clusters en voer noodherstel eenvoudiger uit.

**2. Oud en nieuw combineren:**
- Draai oudere applicaties, zoals SAP en Oracle, in VM's.
- Voer nieuwe microservices uit in containers.
- Migreer geleidelijk naar containers.
- Combineer de sterke kanten van beide technologieën.

**3. Ontwikkelworkflow:**
- Ontwikkelaars gebruiken Docker lokaal.
- CI/CD draait in containers.
- Staging en productie gebruiken Kubernetes op VM's.
- Beveiliging en compliance blijven behouden.

**4. Cloudstrategie:**
- Verplaats workloads eerst ongewijzigd naar VM's.
- Herbouw ze later geleidelijk voor containers.
- Gebruik een hybride clouduitrol.
- Kies zelf het tempo van modernisering.

## Orkestratie- en beheertools

### Docker-orkestratie

**Kubernetes (industriestandaard):**
- Geautomatiseerde uitrol, schaling en beheer.
- Meer dan 90% van de markt voor containerorkestratie.
- Cloudonafhankelijk: AWS EKS, Azure AKS en GCP GKE.
- Zelfherstel en automatisch schalen.
- Servicedetectie en load balancing.
- Rolling updates en terugdraaien.

**Docker Swarm:**
- Standaardorkestratie voor Docker.
- Eenvoudiger dan Kubernetes.
- Geschikt voor kleinere implementaties.
- Neemt in populariteit af.

**Amazon ECS/Fargate:**
- Containerorkestratie voor AWS.
- Serverless uitvoering van containers.
- Diepe integratie met AWS.
- Fargate neemt clusterbeheer uit handen.

### VM-orkestratie

**VMware vSphere:**
- Industriestandaard voor VM-beheer.
- vMotion voor live migration.
- DRS voor verdeling van middelen.
- HA voor automatische failover.

**Microsoft Hyper-V en SCVMM:**
- Met Windows geïntegreerde virtualisatie.
- System Center Virtual Machine Manager.
- Integratie met Azure.
- Ideaal voor omgevingen met veel Windows-systemen.

**OpenStack:**
- Open-sourcecloudplatform.
- Ondersteuning voor meerdere hypervisors.
- Infrastructuur voor private clouds.
- Beheer van grote VM-omgevingen.

**Proxmox VE:**
- Open-sourcevirtualisatieplatform.
- Ondersteuning voor KVM en LXC.
- Webgebaseerd beheer.
- Kosteneffectief voor mkb-bedrijven.

## Migratiestrategieën

### Migreren van VM's naar containers

**Stapsgewijze aanpak:**

**Fase 1: inventarisatie (2–4 weken)**
1. Breng alle applicaties in kaart.
2. Bepaal welke applicaties geschikt zijn voor containers.
3. Beoordeel afhankelijkheden en status.
4. Plan de migratievolgorde.

**Fase 2: pilot (1–2 maanden)**
1. Selecteer 3–5 geschikte applicaties.
2. Containeriseer de pilotapplicaties.
3. Test ze grondig in staging.
4. Rol ze uit naar productie.
5. Meet de resultaten en leer ervan.

**Fase 3: geleidelijke migratie (6–18 maanden)**
1. Containeriseer applicaties op basis van prioriteit.
2. Behoud een hybride infrastructuur.
3. Werk CI/CD-pipelines bij.
4. Train het beheerteam.
5. Leg de opgedane kennis vast.

**Fase 4: optimalisatie (doorlopend)**
1. Herstructureer applicaties volgens cloud-native patronen.
2. Implementeer een microservicesarchitectuur.
3. Optimaliseer containerimages.
4. Verbeter monitoring en observability.

**Geschikte applicaties om mee te beginnen:**
- Stateless-webapplicaties.
- API-services.
- Microservices.
- Nieuwe ontwikkelprojecten.

**Behoud in VM's:**
- Verouderde monolieten.
- Statusbehoudende databases, in eerste instantie.
- Applicaties die alleen op Windows draaien.
- Gelicentieerde software.

### Migreren van containers naar VM's

**Wanneer terugschakelen:**
- Beveiligings- of compliance-eisen veranderen.
- Er ontstaan prestatieproblemen met containers.
- Er gelden nieuwe licentiebeperkingen.
- Sterkere isolatie is nodig.

**Aanpak:**
1. Maak VM-templates.
2. Installeer de afhankelijkheden van de applicatie.
3. Rol de containerapplicatie uit op een VM.
4. Test de werking grondig.
5. Schakel over met zo min mogelijk downtime.

## Besliskader: Docker of VM?

### Snelle beslisboom

```
Start: applicatie moet worden geïmplementeerd
    │
    ├─ Meerdere OS nodig? (Windows + Linux)
    │   └─ Ja → Gebruik VM’s
    │
    ├─ Verouderde monolithische applicatie?
    │   └─ Ja → Gebruik VM’s
    │
    ├─ Sterke isolatie nodig? (multi-tenant)
    │   └─ Ja → Gebruik VM’s
    │
    ├─ Snelle schaalvergroting nodig?
    │   └─ Ja → Gebruik Docker
    │
    ├─ Microservicesarchitectuur?
    │   └─ Ja → Gebruik Docker
    │
    ├─ Focus op DevOps/CI-CD?
    │   └─ Ja → Gebruik Docker
    │
    └─ Moderne cloud-native app?
        └─ Ja → Gebruik Docker
```

### Uitgebreide beslismatrix

| Overweging | Kies Docker | Kies VM's |
|-------------|-------------|-----------|
| **Architectuur** | Microservices, zonder status | Monolithisch, statusbehoudend |
| **Schaalbehoefte** | Snel automatisch schalen | Voorspelbaar schalen |
| **Opstarttijd** | Seconden zijn belangrijk | Minuten zijn acceptabel |
| **Efficiënt gebruik van middelen** | Maximale dichtheid | Isolatie heeft prioriteit |
| **Ontwikkelsnelheid** | Snel itereren | Stabiele releases |
| **Technologiestack** | Linuxgericht | Meerdere besturingssystemen |
| **Beveiligingsmodel** | Gedeelde kernel acceptabel | Kernelisolatie vereist |
| **Operationele volwassenheid** | DevOps-cultuur | Traditionele IT |
| **Budget** | Kosten optimaliseren | Compliance prioriteit |
| **Bestaande infrastructuur** | Cloud-native | Traditioneel datacenter |


## Aanbevolen werkwijzen voor 2026

### Aanbevolen werkwijzen voor Docker

**1. Images optimaliseren:**
```dockerfile
# Gebruik builds met meerdere fasen
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Productie-image
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/server.js"]
```

**2. Beveiliging versterken:**
- Voer containers uit als niet-rootgebruiker.
- Gebruik officiële basisimages.
- Scan regelmatig op kwetsbaarheden.
- Pas het principe van minimale privileges toe.
- Beheer geheimen met Vault, AWS Secrets Manager of een vergelijkbare oplossing.

**3. Monitoring en logging:**
- Verzamel logs centraal met ELK of Loki.
- Verzamel metrieken met Prometheus.
- Gebruik distributed tracing met Jaeger of Zipkin.
- Stel health checks en readiness probes in.

**4. Netwerken:**
- Gebruik overlaynetwerken voor meerdere hosts.
- Implementeer een service mesh, zoals Istio of Linkerd.
- Gebruik netwerkbeleid voor beveiliging.
- Laat services via DNS ontdekken.

### Aanbevolen werkwijzen voor VM's

**1. Middelen toewijzen:**
- Kies VM-formaten die passen en voorkom overprovisioning.
- Gebruik resourcepools en limieten.
- Werk met VM-templates.
- Houd het gebruik van middelen in de gaten.

**2. Hoge beschikbaarheid:**
- Cluster VM's over meerdere hosts.
- Implementeer automatische failover.
- Gebruik gedeelde opslag, zoals SAN of NAS.
- Maak regelmatig back-ups en test ze.

**3. Beveiliging:**
- Segmenteer het netwerk met VLAN's.
- Volg een regelmatig patchschema.
- Versleutel opslag en gegevensoverdracht.
- Beheer toegang en voer audits uit.

**4. Prestaties:**
- Gebruik paravirtualized drivers.
- Wijs kritieke VM's aparte middelen toe.
- Houd bij grote VM's rekening met NUMA.
- Optimaliseer opslagprestaties.

## Toekomstige trends: wat komt hierna?

### Ontwikkeling van containers

**1. Rootless en niet-geprivilegieerde containers:**
- Betere beveiliging zonder rootprivileges.
- Meer gebruik in gereguleerde sectoren.
- Kleiner aanvalsoppervlak.

**2. WebAssembly-containers (Wasm):**
- Zeer lichtgewicht uitvoering.
- Platformonafhankelijk binair formaat.
- Snellere start dan traditionele containers.
- De integratie tussen Docker en Wasm breidt uit.

**3. Integratie van eBPF:**
- Geavanceerdere netwerk- en beveiligingsfuncties.
- Observability op kernelniveau.
- Verbeterde prestatiebewaking.

**4. GPU- en AI/ML-versnelling:**
- Beter GPU-gebruik tussen containers.
- Optimalisatie voor AI/ML-workloads.
- ML-platforms die op containers zijn gebaseerd.

### Vernieuwingen in VM's

**1. Vertrouwelijke computing:**
- Geheugen van VM's versleuteld met hardware.
- Secure enclaves voor gevoelige gegevens.
- Integratie met AMD SEV en Intel SGX.

**2. Combinatie van VM's en containers:**
- Kata Containers en gVisor.
- Isolatie op VM-niveau met het gebruiksgemak van containers.
- De beste eigenschappen van beide technologieën.

**3. Edge computing:**
- Lichtgewicht hypervisors.
- Micro-VM's, zoals Firecracker.
- Virtualisatie die voor edge-apparaten is geoptimaliseerd.

## Conclusie: kies de juiste technologie

In 2026 gaat de discussie over **Docker versus VM's** niet over welke technologie "beter" is. Het gaat erom welke oplossing bij jouw behoeften past.

**Kies Docker wanneer je:**
- Moderne microserviceapplicaties bouwt.
- Middelen efficiënt wilt gebruiken en de dichtheid wilt verhogen.
- Snel wilt schalen en uitrollen.
- DevOps- en cloud-native werkwijzen omarmt.
- Stateless-applicaties uitvoert.
- De productiviteit van ontwikkelaars vooropstelt.

**Kies VM's wanneer je:**
- Verouderde monolithische applicaties uitvoert.
- Sterke beveiligingsisolatie nodig hebt.
- Meerdere besturingssystemen ondersteunt.
- Traditionele statusbehoudende databases beheert.
- Aan strikte compliance-eisen moet voldoen.
- In traditionele bedrijfsomgevingen werkt.

**Gebruik beide wanneer je:**
- Geleidelijk naar containers migreert.
- Verschillende soorten workloads uitvoert.
- Flexibiliteit en keuzemogelijkheden nodig hebt.
- Een hybride cloudinfrastructuur bouwt.

De succesvolste organisaties in 2026 hanteren een **praktische aanpak**: containers voor nieuwe cloud-native applicaties en geschikte bestaande workloads, en VM's voor oudere systemen en situaties waarin hun sterke punten nodig zijn. Met deze hybride strategie kun je elke workload afzonderlijk optimaliseren en tegelijk efficiënt blijven werken.

Als je beide technologieën begrijpt, kun je voor jouw omgeving onderbouwde architectuurkeuzes maken die prestaties, beveiliging, kosten en beheer met elkaar in balans brengen.

______

## Bronnen

- [Officiële Docker-documentatie](https://docs.docker.com/)
- [Kubernetes-documentatie](https://kubernetes.io/docs/)
- [VMware vSphere-documentatie](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Microsoft Hyper-V-documentatie](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/)
- [KVM-virtualisatie](https://www.linux-kvm.org/)
- [CNCF Cloud Native Landscape](https://landscape.cncf.io/)
- [Best practices voor Docker-beveiliging](https://docs.docker.com/engine/security/)
- [NIST-gids voor containerbeveiliging van applicaties](https://www.nist.gov/publications/application-container-security-guide)
- [Proxmox VE](https://www.proxmox.com/en/proxmox-ve)
- [Containerdiensten van AWS](https://aws.amazon.com/containers/)
