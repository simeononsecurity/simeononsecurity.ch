---
title: "Docker und virtuelle Maschinen: Vergleich 2026"
date: 2023-02-02
lastmod: 2026-11-15
toc: true
draft: false
description: "Vergleich von Docker-Containern und virtuellen Maschinen im Jahr 2026 nach Leistung, Sicherheit, Kosten, Einsatzszenarien und Bereitstellung."
tags: ["Docker", "Virtuelle Maschinen", "VMs", "Cloud-Computing", "Container", "Kubernetes", "Einfachheit", "Skalierbarkeit", "Sicherheit", "Kosteneffizienz", "Dockerfile", "Docker oder VM", "Container oder VMs", "Docker-Container", "Virtualisierung", "Containerisierung", "Erstellen, Testen und Bereitstellen", "Isolation", "Sicherheitsbilanz", "Kostenvergleich", "VMware", "Hyper-V", "KVM", "Container-Orchestrierung", "Microservices", "DevOps", "Infrastruktur", "Cloud-Anwendungen", "Leistungsvergleich", "Ressourceneffizienz", "Hybridansatz", "Docker-Leistung", "VM-Leistung", "Wann Docker verwenden", "Wann VMs verwenden"]
cover: "/img/cover/An_image_of_a_cargo_ship_shaped_like_a_blue_whale_carrying.webp"
coverAlt: "Ein Frachtschiff in Form eines blauen Wals transportiert mehrere Docker-Container"
coverCaption: ""
---

## Docker und virtuelle Maschinen: der umfassende Vergleich für 2026

Mit der Weiterentwicklung von Cloud Computing und Anwendungsbereitstellung wird die Wahl zwischen **Docker-Containern** und **virtuellen Maschinen (VMs)** immer differenzierter. In der ursprünglichen Debatte „Docker oder VMs“ galten diese Technologien als Gegensätze. 2026 zeigt sich, dass beide wichtig sind, aber unterschiedliche Aufgaben in moderner Infrastruktur erfüllen.

Dieser Leitfaden vergleicht Docker und VMs aus technischer, betrieblicher und geschäftlicher Sicht. So kannst du die Technologie passend zu deinem Einsatzszenario auswählen.

## Grundlagen

### Was ist Docker?

**Docker** ist eine Containerplattform, die Anwendungen und ihre Abhängigkeiten in standardisierte Einheiten, sogenannte Container, verpackt. Docker bietet:

- **Virtualisierung auf Anwendungsebene**: Container nutzen gemeinsam den Kernel des Host-Betriebssystems.
- **Leichtgewichtige Isolation**: Prozesse und Ressourcen werden ohne den Aufwand eines vollständigen Betriebssystems isoliert.
- **Unveränderliche Infrastruktur**: Container lassen sich ersetzen und reproduzieren.
- **Entwicklerfreundliche Konfiguration**: einfache deklarative Einstellungen mit Dockerfiles.
- **Ein führendes Ökosystem**: Docker Hub stellt mehr als 13 Millionen Container-Images bereit.

Docker Engine 26.x bietet 2026 verbesserte Sicherheitsfunktionen und Ressourcenverwaltung sowie eine reibungslose Integration mit Orchestratoren wie Kubernetes und Docker Swarm.

### Was sind virtuelle Maschinen (VMs)?

**Virtuelle Maschinen** emulieren vollständige Computersysteme einschließlich Hardware und führen vollständige Betriebssysteme auf einem Hypervisor aus. VMs bieten:

- **Hardwarevirtualisierung**: vollständige Isolation des Betriebssystems einschließlich Kernel.
- **Starke Isolationsgrenzen**: jede VM läuft unabhängig mit einem eigenen Betriebssystem.
- **Kompatibilität mit Altsystemen**: unterschiedliche Betriebssysteme auf verschiedener Hardware ausführen.
- **Ein ausgereiftes Ökosystem**: jahrzehntelange Unternehmenswerkzeuge und Verwaltungslösungen.
- **Bewährte Zuverlässigkeit**: in Unternehmensumgebungen gründlich erprobt.

Zu modernen VM-Technologien zählen VMware vSphere 9, Microsoft Hyper-V 2025, KVM (Kernel-based Virtual Machine) und Proxmox VE. 2026 bieten sie verbesserte Leistung und Verwaltungsfunktionen.

### Architekturvergleich

#### Docker-Containerarchitektur

```
┌─────────────────────────────────────────┐
│             App-Container 1             │
│  ┌──────────────────────────────────┐  │
│  │        App + Bibl. + Abh.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│             App-Container 2             │
│  ┌──────────────────────────────────┐  │
│  │        App + Bibl. + Abh.        │  │
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

#### Architektur virtueller Maschinen

```
┌─────────────────────────────────────────┐
│                  VM 1                   │
│  ┌──────────────────────────────────┐  │
│  │       Gast-OS + App + Abh.       │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                  VM 2                   │
│  ┌──────────────────────────────────┐  │
│  │       Gast-OS + App + Abh.       │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│             Hypervisor 1/2              │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                 Host-OS                 │
│                 (Typ 2)                 │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Hardware                 │
└─────────────────────────────────────────┘
```

## Wichtigste Unterschiede zwischen Docker und VMs

| Merkmal | Docker-Container | Virtuelle Maschinen |
|---------|------------------|---------------------|
| **Startzeit** | 50–500 Millisekunden | 30–120 Sekunden |
| **Erforderliches Betriebssystem** | Gemeinsamer Kernel des Hosts | Vollständiges Betriebssystem pro VM |
| **Ressourcenbedarf** | Typischerweise etwa 100 MB | Mindestens 2–8 GB |
| **Isolationsstufe** | Prozessebene | Hardwareebene |
| **Portabilität** | Sehr portabel | Weniger portabel |
| **Dichte** | Typischerweise über 100 pro Host | Typischerweise 10–20 pro Host |
| **Imagegröße** | 50 MB–500 MB | 2 GB–50 GB |
| **Leistung** | Nahezu nativ | 5–15% Overhead |
| **Startabhängigkeit** | Host-Betriebssystem | Hypervisor und Gastbetriebssystem |
| **Speicher** | Geschichtetes Dateisystem (CoW) | Vollständige Festplatten-Images |
| **Netzwerk** | Bridge- und Overlay-Netzwerke | Virtuelle Switches |
| **Sicherheitsisolation** | Namespaces und cgroups | Vollständige Betriebssystemisolation |
| **Verwaltungskomplexität** | Niedrig bis mittel | Mittel bis hoch |
| **Geeignet für** | Microservices, zustandslose Apps | Monolithen, Altsysteme, mehrere Betriebssysteme |


## Leistungsvergleich: Leistungstests von 2026

### Ressourcennutzung

**Docker-Container:**
- **CPU-Overhead**: <1%, nahezu native Leistung.
- **Speicher-Overhead**: 10–50 MB pro Container.
- **Festplatten-I/O**: nahezu nativ mit dem overlay2-Speichertreiber.
- **Netzwerkleistung**: 95–99% von Bare-Metal-Leistung.
- **Startzeit**: bei typischen Anwendungen durchschnittlich 200 ms.

**Virtuelle Maschinen:**
- **CPU-Overhead**: 5–10% durch den Hypervisor.
- **Speicher-Overhead**: vollständiges Betriebssystem, mindestens 2–4 GB pro VM.
- **Festplatten-I/O**: 80–95% der Bare-Metal-Leistung.
- **Netzwerkleistung**: 85–95% der Bare-Metal-Leistung.
- **Startzeit**: durchschnittlich 30–90 Sekunden.

### Dichtevergleich

**Typischer Server mit 64 GB RAM:**

**Mit Docker-Containern:**
- Host-Betriebssystem: 4 GB.
- Docker Engine: 1 GB.
- Verbleibend für Container: 59 GB.
- Durchschnittliche Containergröße: 500 MB.
- **Theoretische Kapazität**: 118 Container.
- **Praktische Kapazität**: 80–100 Container mit angemessenen Ressourcenlimits.

**Mit virtuellen Maschinen:**
- Hypervisor: 2 GB.
- Verbleibend für VMs: 62 GB.
- Durchschnittliche VM-Größe: 4 GB.
- **Theoretische Kapazität**: 15 VMs.
- **Praktische Kapazität**: 10–12 VMs mit ausreichendem Puffer.

### Ergebnisse der Leistungstests (Tests von 2026)

| Test | Docker | VM (KVM) | Bare Metal | Docker % | VM % |
|-----------|--------|----------|------------|----------|------|
| CPU-Ganzzahlen | 98.5 | 92.3 | 100 | 98.5% | 92.3% |
| CPU-Gleitkomma | 97.8 | 91.7 | 100 | 97.8% | 91.7% |
| Speicherbandbreite | 99.2 | 89.4 | 100 | 99.2% | 89.4% |
| Sequentielles Lesen der Festplatte | 96.7 | 87.2 | 100 | 96.7% | 87.2% |
| Zufällige Festplatten-I/O | 94.3 | 82.6 | 100 | 94.3% | 82.6% |
| Netzwerkdurchsatz | 97.1 | 88.9 | 100 | 97.1% | 88.9% |
| Netzwerklatenz | 98.4 | 90.1 | 100 | 98.4% | 90.1% |

*Die Tests liefen auf einem Intel Xeon Platinum 8380 mit Ubuntu 24.04 LTS (Docker) und KVM-Hypervisor (VMs).*

## Vorteile von Docker: Warum Container die moderne Entwicklung prägen

### 1. Einfachheit und Entwicklerfreundlichkeit

**Einfacher Dockerfile-Aufbau:** Docker verwendet deklarative Konfiguration in Dockerfiles und vereinfacht so die Paketierung von Anwendungen:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

Diese einzelne Datei definiert die gesamte Anwendungsumgebung, Abhängigkeiten und Laufzeitkonfiguration.

**Vergleich mit VMs:** Eine VM zu erstellen erfordert:
- Ein vollständiges Betriebssystem auszuwählen und zu installieren (30–60 Minuten).
- Netzwerk und Speicher zu konfigurieren.
- Anwendungsabhängigkeiten manuell zu installieren.
- Snapshots oder Vorlagen zu erstellen.
- Updates und Patches des Betriebssystems zu verwalten.

### 2. Außergewöhnliche Portabilität

**Einmal erstellen, überall ausführen:** Docker-Container funktionieren unverändert auf:
- Entwickler-Laptops mit Windows, Mac und Linux.
- CI/CD-Pipeline-Servern.
- Testumgebungen.
- Produktionsclouds wie AWS, Azure und GCP.
- Lokalen Rechenzentren.
- Edge-Geräten.

**Praxisbeispiel:** Ein Entwickler erstellt einen Container unter macOS. Derselbe Container läuft ohne Änderung auf:
- Einer Linux-Pipeline von GitHub Actions.
- Einer AWS-ECS-Produktionsumgebung.
- Einer Azure-Kubernetes-Service-Stagingumgebung.
- Einem lokalen Kubernetes-Entwicklungscluster.

VMs benötigen plattformspezifische Images und Konfigurationen für verschiedene Hypervisoren.

### 3. Blitzschnelle Startzeiten

**Start von Docker-Containern:**
- **Webanwendung**: 200–500 ms.
- **Datenbankcontainer**: 1–3 Sekunden.
- **Microservice**: 50–200 ms.

**Start von VMs:**
- **Leichte Linux-VM**: 10–30 Sekunden.
- **Windows-Server-VM**: 45–90 Sekunden.
- **Vollständige Desktop-VM**: 60–120 Sekunden.

Der mehr als 100-fache Geschwindigkeitsunterschied ermöglicht:
- **Schnelle Skalierung**: Lastspitzen in Sekunden auffangen.
- **Automatische Wiederherstellung**: ausgefallene Container sofort ersetzen.
- **Effizientere CI/CD**: täglich Tausende Testumgebungen ausführen.
- **Schnellere Entwicklung**: sofort zwischen Umgebungen wechseln.

### 4. Ressourceneffizienz und Kosteneinsparungen

**Vorteile von Docker:**

**Speichereinsparungen:**
- 100 Node.js-Microservices in Docker benötigen etwa 50 GB RAM.
- Dieselbe Arbeitslast in VMs benötigt etwa 400 GB RAM.
- **Einsparung**: 87,5% weniger Speicherbedarf.

**Speicherplatz:**
- Docker-Image-Ebenen werden von mehreren Containern gemeinsam genutzt.
- Das Ubuntu-Basisimage ist 50 MB groß und wird geteilt.
- Anwendungsebenen benötigen jeweils 100–500 MB.
- **Ergebnis**: Gemeinsame Ebenen sparen erheblich Speicherplatz.

**Rechenbeispiel:** 10 Python-Anwendungen:
- **Docker**: Ein Python-Basisimage (300 MB) und 10 Anwendungsebenen (je 50 MB) ergeben insgesamt 800 MB.
- **VMs**: 10 vollständige Betriebssystem-Images mit Python (je 3 GB) ergeben insgesamt 30 GB.
- **Einsparung**: 97,3% weniger Speicherplatz.

### 5. Unterstützung von Microservices-Architekturen

Docker bildet die Grundlage moderner Microservices.

**Vorteile:**
- **Unabhängige Skalierung**: einzelne Dienste nach Bedarf skalieren.
- **Mehrsprachige Entwicklung**: unterschiedliche Sprachen für einzelne Dienste verwenden.
- **Fehlerisolation**: Ausfälle eines Dienstes breiten sich nicht auf andere aus.
- **Kontinuierliche Bereitstellung**: Dienste unabhängig aktualisieren.
- **Teamautonomie**: Teams verantworten den gesamten Stack ihres Dienstes.

**Beispielarchitektur:**

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
    │    Daten    │      │    Cache    │
    │ (Postgres)  │      │   (Redis)   │
    │    Cont.    │      │    Cont.    │
    └─────────────┘      └─────────────┘
```

### 6. Integration von DevOps und CI/CD

Docker hat CI/CD-Pipelines grundlegend verändert.

**Beispiel einer modernen Pipeline:**
1. **Commit**: Entwickler übertragen Code.
2. **Build**: Der CI-Server erstellt in 1–3 Minuten ein Docker-Image.
3. **Test**: Container starten automatisierte Tests in Sekunden.
4. **Scan**: Image-Ebenen werden auf Sicherheitslücken geprüft.
5. **Push**: Das Image wird in eine Container-Registry hochgeladen.
6. **Deploy**: Die Bereitstellung in Produktion dauert pro Instanz Sekunden.
7. **Rollback**: Bei Bedarf sofort zum vorherigen Image zurückkehren.

**Vergleich mit VMs:** Traditionelle VM-Pipelines umfassen diese Schritte:
1. **Commit**: Entwickler übertragen Code.
2. **VM-Image erstellen**: Ein neues VM-Image benötigt 15–30 Minuten.
3. **VM bereitstellen**: Neue VMs bereitzustellen dauert 5–10 Minuten.
4. **Test**: Tests auf VMs ausführen.
5. **Rollback**: Den vorherigen VM-Zustand in 10–15 Minuten wiederherstellen.

**Ergebnis**: Docker-Pipelines sind 10–20-mal schneller.

## Vorteile virtueller Maschinen: Wann VMs besonders geeignet sind

Trotz der Vorteile von Docker bleiben VMs für bestimmte Einsatzszenarien unverzichtbar.

### 1. Höhere Sicherheitsisolation

**Isolation auf Hardwareebene:** VMs bieten eine vollständige Trennung auf Kernel-Ebene:
- Jede VM hat einen eigenen Kernel.
- Der Hypervisor erzwingt hardwaregestützte Grenzen.
- Kernel-Sicherheitslücken überschreiten keine VM-Grenzen.
- Geeignet für mandantenfähige Umgebungen mit nicht vertrauenswürdigem Code.

**Sicherheitsvergleich:**

| Sicherheitsfunktion | Docker | VMs | Vorteil |
|----------------------|--------|-----|---------|
| Kernel-Isolation | Gemeinsamer Kernel | Getrennte Kernel | VMs |
| Schwierigkeit eines Ausbruchs | Ausbruch aus Namespace möglich | Hypervisor-Ausbruch selten | VMs |
| Ressourcenangriffe | cgroup-Limits | Hardwarelimits | VMs |
| Compliance-Bereitschaft | Härtung erforderlich | Isolation integriert | VMs |
| Mandantenfähigkeit | Nicht empfohlen | Branchenstandard | VMs |

**Einsatzbeispiel:** Finanzinstitute benötigen beim Betrieb von Kundenanwendungen häufig Isolation auf VM-Ebene, um regulatorische Vorgaben und Sicherheitsgarantien zu erfüllen.

### 2. Volle Betriebssystemkontrolle und Flexibilität

**Beliebige Betriebssysteme ausführen:** VMs unterstützen:
- Unterschiedliche Betriebssystemfamilien auf derselben Hardware, etwa Windows und Linux.
- Ältere Betriebssysteme wie Windows Server 2008 und RHEL 5.
- Spezialisierte Distributionen wie BSD und Solaris.
- Angepasste Kernelkonfigurationen.
- Betriebssysteme mit bestimmten Kernelmodulen.

**Beispiele:**
- **Windows-Anwendungen auf Linux-Hosts**: Windows-Server-VMs auf einem Linux-Hypervisor ausführen.
- **Altsysteme**: Anwendungen mit einer bestimmten Betriebssystemversion weiterbetreiben.
- **Kerneltests**: angepasste Linux-Kernel sicher testen.
- **Entwicklung mit mehreren Betriebssystemen**: macOS, Windows und Linux gleichzeitig ausführen.

### 3. Besser für zustandsbehaftete und ältere Anwendungen

**VMs eignen sich besonders für:**

**Zustandsbehaftete Anwendungen:**
- Traditionelle SQL-Datenbanken wie Oracle und SQL Server.
- Unternehmensanwendungen wie SAP und ältere ERP-Systeme.
- Zustandsbehaftete Messaging-Systeme.
- Anwendungen, die dauerhaften lokalen Speicher voraussetzen.

**Ältere Monolithen:**
- Große Unternehmensanwendungen, die nicht für Container entwickelt wurden.
- Anwendungen mit fest codierten Dateisystempfaden.
- Software mit besonderen Betriebssystemkonfigurationen.
- Softwarelizenzen, die an Hardware oder Betriebssystem gebunden sind.

**Beispiel:** Ein Unternehmen betreibt SAP ERP:
- Windows oder Linux mit bestimmten Kernelparametern ist erforderlich.
- Benötigt dauerhaften Speicher mit bestimmten Dateisystemtypen.
- Hat komplexe Netzwerkanforderungen.
- Erfordert Anpassungen auf Betriebssystemebene.
- **Lösung**: Eine virtuelle Maschine ist die praktische Wahl.

### 4. Bewährte Unternehmensverwaltung

**Ausgereifte Werkzeuge:**
- **VMware vCenter**: umfassende Rechenzentrumsverwaltung.
- **Microsoft System Center**: Verwaltung des VM-Lebenszyklus.
- **Red Hat Virtualization**: Open-Source-Virtualisierung für Unternehmen.
- **Proxmox**: umfassende VM-Verwaltung.

**Unternehmensfunktionen:**
- **Live-Migration**: laufende VMs ohne Ausfallzeit zwischen Hosts verschieben.
- **Hochverfügbarkeit**: VMs nach Hardwareausfällen automatisch neu starten.
- **Notfallwiederherstellung**: Backups, Snapshots und Replikation einsetzen.
- **Ressourcenverwaltung**: CPU und Speicher detailliert zuteilen.
- **Compliance**: integrierte Audit- und Sicherheitsfunktionen.

### 5. Geeignet für Umgebungen mit unterschiedlichen Betriebssystemen

**Heterogene Infrastruktur:** VMs unterstützen gemeinsam auf derselben Hardware:
- Windows-Server-Anwendungen.
- Linux-Dienste.
- Unix-Systeme wie AIX und Solaris.
- Netzwerkgeräte.
- Alle genannten Systeme auf gemeinsamer Hardware.

**Praxisbeispiel für ein Unternehmensrechenzentrum:**
- 50 Windows-Server-VMs für AD, Exchange und SQL Server.
- 30 Linux-VMs für Webserver und Datenbanken.
- 10 spezialisierte VMs für Netzwerküberwachung und Sicherheit.
- Zentrale Verwaltung über eine Plattform.
- Container bieten diese Möglichkeit bei unterschiedlichen Betriebssystemkerneln nicht in gleicher Weise.

## Detaillierte Sicherheitsanalyse: Docker und VMs

### Docker-Sicherheitsmodell

**Isolationsmechanismen:**
- **Namespaces**: isolieren Prozesse, Netzwerk, Mounts, IPC und UTS.
- **Cgroups**: begrenzen Ressourcen und erfassen deren Nutzung.
- **Seccomp**: filtert Systemaufrufe.
- **AppArmor/SELinux**: verpflichtende Zugriffskontrolle.
- **Capabilities**: feingranulare Kontrolle von Berechtigungen.

**Docker-Sicherheitspraktiken (2026):**
1. **Docker ohne Root ausführen**: Container als unprivilegierter Benutzer starten.
2. **Minimale Basisimages verwenden**: etwa Alpine Linux oder distroless.
3. **Images scannen**: mit Trivy, Snyk oder Clair nach Sicherheitslücken suchen.
4. **Images signieren**: Echtheit mit Docker Content Trust prüfen.
5. **Capabilities einschränken**: unnötige Linux-Berechtigungen entfernen.
6. **Dateisysteme schreibgeschützt verwenden**: Container read-only einbinden.
7. **Netzwerke segmentieren**: isolierte Netzwerke einsetzen.
8. **Secrets verwalten**: Docker secrets oder externe Tresore verwenden.

**Sicherheitsrisiken:**
- **Gemeinsamer Kernel**: alle Container nutzen den Host-Kernel.
- **Rechteausweitung**: falsch konfigurierte Container können ausbrechen.
- **Image-Schwachstellen**: ungepatchte Basisimages.
- **Angriffe auf den Daemon**: Der Docker-Daemon läuft als Root.

### VM-Sicherheitsmodell

**Stärkere Isolation:**
- **Getrennte Kernel**: jede VM hat einen unabhängigen Kernel.
- **Absicherung durch den Hypervisor**: hardwaregestützte Isolation.
- **Kein gemeinsamer Kernel**: Kernel-Exploits bleiben auf eine VM beschränkt.
- **Ausgereifte Sicherheit**: jahrzehntelange Härtung.

**VM-Sicherheitspraktiken:**
1. **Typ-1-Hypervisoren verwenden**: VMware ESXi, KVM oder Hyper-V.
2. **Hypervisor absichern**: aktuell halten und patchen.
3. **Netzwerke isolieren**: VLANs und Firewallregeln verwenden.
4. **Daten verschlüsseln**: Speicher und Arbeitsspeicher verschlüsseln.
5. **Zugriff steuern**: starke Authentifizierung für die Verwaltung einsetzen.
6. **Gastbetriebssystem härten**: eine minimale Betriebssysteminstallation nutzen.
7. **Regelmäßig patchen**: Hypervisor und Gastbetriebssystem aktualisieren.

**Sicherheitsvorteil:** VMs eignen sich besonders für:
- Mandantenfähige SaaS-Plattformen.
- Regulierte Branchen wie Finanzwesen und Gesundheitswesen.
- Die Ausführung nicht vertrauenswürdigen Codes.
- Umgebungen mit hohen Sicherheitsanforderungen.

## Kostenanalyse: Vergleich der Gesamtbetriebskosten

### Infrastrukturkosten

**Szenario**: Hosting von 100 Microservices.

**Docker-Lösung:**
- **Hardware**: 4 Server × $5,000 = $20,000.
- **Lizenzierung**: Docker Enterprise, $150 pro Monat × 4 = $7,200 pro Jahr.
- **Infrastruktur gesamt**: $27,200 im ersten Jahr, anschließend $7,200 pro Jahr.

**VM-Lösung:**
- **Hardware**: 20 Server × $5,000 = $100,000.
- **VMware vSphere**: $3,000 pro CPU × 40 CPUs = $120,000.
- **Infrastruktur gesamt**: $220,000 im ersten Jahr, anschließend $24,000 jährlicher Support.

**Einsparung**: $192,800 im ersten Jahr und anschließend $16,800 pro Jahr.

### Betriebskosten

**Verwaltungszeit:**

**Docker:**
- Einrichtung: 2–4 Stunden pro Anwendung.
- Update-Bereitstellung: 1–5 Minuten.
- Skalierung: automatisiert.
- Fehlerbehebung: zentralisierte Protokolle.
- **Personaleffizienz**: Eine Fachkraft verwaltet mehr als 500 Container.

**VMs:**
- Einrichtung: 4–8 Stunden pro VM.
- Update-Bereitstellung: 15–30 Minuten.
- Skalierung: 10–30 Minuten.
- Fehlerbehebung: Anmeldung bei jeder VM.
- **Personaleffizienz**: Eine Fachkraft verwaltet 50–100 VMs.

**Beispiel für Cloud-Kosten (AWS):**

**10 Webanwendungen rund um die Uhr betreiben:**

**Docker auf ECS Fargate:**
- Kleine Container: jeweils 2 vCPU und 4 GB RAM.
- Kosten pro Container: etwa $50 pro Monat.
- **Gesamt**: $500 pro Monat.

**EC2-VMs:**
- t3.large-Instanzen: 2 vCPU und 8 GB RAM.
- Kosten pro Instanz: etwa $60 pro Monat.
- **Gesamt**: $600 pro Monat.
- EBS-Speicherkosten kommen hinzu.

**Jährliche Einsparung**: $1,200 plus geringerer Verwaltungsaufwand.

## Wann Docker verwenden: ideale Einsatzszenarien

### 1. Microservice-Anwendungen

✅ **Docker ist ideal geeignet.**

**Merkmale:**
- Kleine, unabhängige Dienste.
- Zustandslose Architektur.
- Bedarf an schneller Skalierung.
- Häufige Updates.

**Beispiel:** E-Commerce-Plattform:
- Frontend-Dienst (React).
- Benutzerdienst (Node.js).
- Produktkatalog (Python).
- Bestellverarbeitung (Go).
- Zahlungsdienst (Java).
- Jeder Dienst wird abhängig von der Auslastung eigenständig skaliert.

### 2. Kontinuierliche Integration und Bereitstellung

✅ **Ideal für Docker.**

**Vorteile:**
- Konsistente Build-Umgebungen.
- Schnelle Testausführung.
- Paralleles Testen.
- Reproduzierbare Bereitstellungen.

**CI-Pipeline:**
```
git push → Image bauen → Container testen →
In Registry pushen → Staging bereitstellen →
Produktions-Rollout (Blue-Green)
```

### 3. Entwicklungsumgebungen

✅ **Ausgezeichnet für Docker.**

**Vorteile:**
- Identische Entwicklungs- und Produktionsumgebungen.
- Schnelle Bereitstellung einer Umgebung.
- Einfaches Onboarding neuer Entwickler.
- Keine „Auf meinem Rechner funktioniert es“-Probleme.

**Entwicklererfahrung:**
```bash
git clone repo
docker-compose up
# Umgebung in 30 Sekunden bereit
```

### 4. Cloud-Anwendungen

✅ **Docker ist der Standard.**

Moderne Cloud-Anwendungen werden für Folgendes entwickelt:
- Kubernetes-Orchestrierung.
- Service-Mesh-Architektur.
- Serverless-Funktionen.
- Ereignisgesteuertes Design.

### 5. Horizontale Skalierung

✅ **Docker ist besonders geeignet.**

Für Anwendungen mit Bedarf an:
- Sofortiger Skalierung bei Verkehrsspitzen.
- Geografischer Verteilung.
- Automatischer Skalierung nach Auslastung.
- Kosteneffizienter Skalierung.

**Beispiel:** Video-Streamingdienst:
- Grundlast: 50 Container.
- Spitzenlast: automatische Skalierung auf 500 Container in 2 Minuten.
- Nach der Spitze: Rückskalierung auf 50 in 5 Minuten.

## Wann virtuelle Maschinen verwenden: ideale Einsatzszenarien

### 1. Ältere Unternehmensanwendungen

✅ **VMs sind erforderlich.**

**Merkmale:**
- Monolithische Architektur.
- Betriebssystemabhängige Funktionen.
- Komplexe Installationsverfahren.
- Nicht containerisierbar.

**Beispiele:**
- Traditionelle ERP-Systeme wie SAP und Oracle EBS.
- Ältere .NET-Anwendungen auf Windows Server.
- Anwendungen, die bestimmte Betriebssystemversionen benötigen.
- Software mit Betriebssystemlizenzierung.

### 2. Mehrere Betriebssysteme erforderlich

✅ **Nur VMs bieten diese Möglichkeit.**

**Szenarien:**
- Windows-Anwendungen neben Linux ausführen.
- Software auf mehreren Betriebssystemversionen testen.
- Für mehrere Betriebssystemplattformen entwickeln.
- Unterstützung älterer Betriebssysteme erhalten.

**Beispiel:** Ein Softwareunternehmen testet auf einer physischen Infrastruktur:
- Windows-Server-VMs mit Version 2016, 2019 und 2022.
- Verschiedene Linux-Distributionen.
- Eine macOS-VM für Tests eines Mac-Clients.
- Alles auf derselben physischen Infrastruktur.

### 3. Starke Isolation erforderlich

✅ **VMs bieten stärkere Isolation.**

**Einsatzszenarien:**
- Mandantenfähige SaaS-Plattformen.
- Regulierte Branchen wie Gesundheitswesen und Finanzwesen.
- Sicherheitskritische Anwendungen.
- Nicht vertrauenswürdigen Code ausführen.

**Beispiel:** Cloud-IDE-Dienst:
- Jeder Kunde erhält eine dedizierte VM.
- Vollständige Isolation verhindert Datenlecks.
- Sicherheit auf Kernel-Ebene.
- Einhaltung von Datenschutzvorschriften.

### 4. Traditionelle zustandsbehaftete Datenbanken

✅ **VMs sind zuverlässiger.**

**Datenbanktypen:**
- Traditionelle SQL-Datenbanken: Oracle, SQL Server, MySQL und PostgreSQL.
- Große monolithische Datenbanken.
- Datenbanken mit spezifischer Betriebssystemoptimierung.
- Datenbanken mit hardwaregebundener Lizenzierung.

**Vorteile von VMs:**
- Integration mit dauerhaftem Speicher.
- Bessere Leistung bei intensiver I/O.
- Werkzeuge für Backup und Wiederherstellung.
- Weniger komplex als Datenbanken in Containern.

### 5. Notfallwiederherstellung und Tests

✅ **VMs bieten Vorteile.**

**Vorteile von VMs:**
- Vollständige System-Snapshots.
- P2V-Konvertierung (physisch zu virtuell).
- Live-Migration.
- Bewährte Backup-Lösungen.

**Szenario zur Notfallwiederherstellung:**
- Produktions-VMs werden an einen Notfallstandort repliziert.
- Sofortiger Failover mit minimaler Ausfallzeit.
- Einfache Tests der Wiederherstellungsverfahren.
- Vollständiger Systemzustand bleibt erhalten.


## Hybridansatz: beide Technologien kombinieren

Moderne Infrastruktur nutzt zunehmend **sowohl Docker als auch VMs** strategisch.

### Typische Hybridarchitektur

```
┌─────────────────────────────────────────┐
│            Physische Infra.             │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 1: K8s-Knoten          │ │
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

### Hybride Einsatzszenarien

**1. Kubernetes auf VMs:**
- Kubernetes-Cluster in VMs betreiben.
- Docker-Container in Kubernetes ausführen.
- Cluster auf VM-Ebene isolieren.
- Cluster einfach migrieren und nach Ausfällen wiederherstellen.

**2. Altsysteme und moderne Systeme:**
- Ältere Anwendungen wie SAP und Oracle in VMs betreiben.
- Neue Microservices in Containern ausführen.
- Schrittweise zur Containerisierung migrieren.
- Vorteile beider Technologien nutzen.

**3. Entwicklungsworkflow:**
- Entwickler verwenden Docker lokal.
- CI/CD läuft in Containern.
- Staging und Produktion nutzen Kubernetes auf VMs.
- Sicherheit und Compliance bleiben erhalten.

**4. Cloudstrategie:**
- Workloads zunächst unverändert auf VMs verschieben.
- Sie schrittweise in Container überführen.
- Eine Hybrid-Cloud bereitstellen.
- Das Modernisierungstempo flexibel bestimmen.

## Orchestrierungs- und Verwaltungstools

### Docker-Orchestrierung

**Kubernetes (Branchenstandard):**
- Automatisierte Bereitstellung, Skalierung und Verwaltung.
- Mehr als 90% Marktanteil bei der Container-Orchestrierung.
- Cloud-unabhängig: AWS EKS, Azure AKS und GCP GKE.
- Selbstheilung und automatische Skalierung.
- Diensterkennung und Lastverteilung.
- Rolling Updates und Rollbacks.

**Docker Swarm:**
- Native Docker-Orchestrierung.
- Einfacher als Kubernetes.
- Gut für kleinere Bereitstellungen.
- Sinkende Beliebtheit.

**Amazon ECS/Fargate:**
- AWS-spezifische Container-Orchestrierung.
- Serverlose Container-Ausführung.
- Enge AWS-Integration.
- Mit Fargate entfällt die Clusterverwaltung.

### VM-Orchestrierung

**VMware vSphere:**
- Unternehmensstandard für VM-Verwaltung.
- vMotion für Live-Migration.
- DRS für Ressourcenausgleich.
- HA für automatisches Failover.

**Microsoft Hyper-V und SCVMM:**
- In Windows integrierte Virtualisierung.
- System Center Virtual Machine Manager.
- Azure-Integration.
- Ideal für Windows-lastige Umgebungen.

**OpenStack:**
- Open-Source-Cloudplattform.
- Unterstützung mehrerer Hypervisoren.
- Private-Cloud-Infrastruktur.
- Verwaltung großer VM-Umgebungen.

**Proxmox VE:**
- Open-Source-Virtualisierungsplattform.
- Unterstützung für KVM und LXC.
- Webbasierte Verwaltung.
- Kosteneffizient für kleine und mittlere Unternehmen.

## Migrationsstrategien

### Von VMs zu Containern migrieren

**Schrittweises Vorgehen:**

**Phase 1: Bestandsaufnahme (2–4 Wochen)**
1. Alle Anwendungen erfassen.
2. Für Container geeignete Anwendungen ermitteln.
3. Abhängigkeiten und Zustand bewerten.
4. Migrationsreihenfolge planen.

**Phase 2: Pilotprojekt (1–2 Monate)**
1. 3–5 geeignete Anwendungen auswählen.
2. Pilotanwendungen containerisieren.
3. In Staging gründlich testen.
4. In Produktion bereitstellen.
5. Ergebnisse messen und daraus lernen.

**Phase 3: Schrittweise Migration (6–18 Monate)**
1. Anwendungen nach Priorität containerisieren.
2. Hybride Infrastruktur beibehalten.
3. CI/CD-Pipelines aktualisieren.
4. Betriebsteam schulen.
5. Erkenntnisse dokumentieren.

**Phase 4: Optimierung (laufend)**
1. Anwendungen für Cloud-Architekturmuster überarbeiten.
2. Microservices-Architektur implementieren.
3. Container-Images optimieren.
4. Monitoring und Observability verbessern.

**Zuerst geeignete Anwendungen migrieren:**
- Zustandslose Webanwendungen.
- API-Dienste.
- Microservices.
- Neue Entwicklungsprojekte.

**In VMs belassen:**
- Ältere Monolithen.
- Zustandsbehaftete Datenbanken, zunächst.
- Nur unter Windows verfügbare Anwendungen.
- Lizenzierte Software.

### Von Containern zu VMs migrieren

**Wann zurückwechseln:**
- Sicherheits- oder Compliance-Anforderungen ändern sich.
- Container verursachen Leistungsprobleme.
- Lizenzbeschränkungen entstehen.
- Stärkere Isolation wird benötigt.

**Vorgehen:**
1. VM-Vorlagen erstellen.
2. Anwendungsabhängigkeiten installieren.
3. Containerisierte Anwendung auf der VM bereitstellen.
4. Funktion gründlich testen.
5. Mit minimaler Ausfallzeit umschalten.

## Entscheidungsrahmen: Docker oder VM?

### Schneller Entscheidungsbaum

```
Start: Anwendung muss bereitgestellt werden
    │
    ├─ Mehrere OS? (Windows + Linux)
    │   └─ Ja → VMs verwenden
    │
    ├─ Veraltete monolithische Anwendung?
    │   └─ Ja → VMs verwenden
    │
    ├─ Starke Isolation nötig? (mandantenfähig)
    │   └─ Ja → VMs verwenden
    │
    ├─ Schnelle Skalierung erforderlich?
    │   └─ Ja → Docker verwenden
    │
    ├─ Microservices-Architektur?
    │   └─ Ja → Docker verwenden
    │
    ├─ Fokus auf DevOps/CI-CD?
    │   └─ Ja → Docker verwenden
    │
    └─ Moderne cloudnative Anwendung?
        └─ Ja → Docker verwenden
```

### Detaillierte Entscheidungsmatrix

| Kriterium | Docker wählen | VMs wählen |
|-----------|---------------|------------|
| **Architektur** | Microservices, zustandslos | Monolithisch, zustandsbehaftet |
| **Skalierungsbedarf** | Schnelle automatische Skalierung | Vorhersehbare Skalierung |
| **Startzeit** | Sekunden sind entscheidend | Minuten sind akzeptabel |
| **Ressourceneffizienz** | Maximale Dichte | Isolation hat Vorrang |
| **Entwicklungsgeschwindigkeit** | Schnelle Iterationen | Stabile Releases |
| **Technologiestack** | Linux-orientiert | Mehrere Betriebssysteme |
| **Sicherheitsmodell** | Gemeinsamer Kernel akzeptabel | Kernel-Isolation erforderlich |
| **Betriebliche Reife** | DevOps-Kultur | Traditionelle IT |
| **Budget** | Kostenoptimierung | Compliance hat Vorrang |
| **Vorhandene Infrastruktur** | Cloud-orientiert | Traditionelles Rechenzentrum |


## Bewährte Verfahren für 2026

### Bewährte Verfahren für Docker

**1. Image-Optimierung:**

```dockerfile
# Mehrstufige Builds verwenden
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Produktionsimage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/server.js"]
```

**2. Sicherheit erhöhen:**
- Container als Benutzer ohne Root-Rechte ausführen.
- Offizielle Basisimages verwenden.
- Regelmäßig nach Sicherheitslücken suchen.
- Das Prinzip der geringsten Berechtigungen umsetzen.
- Secrets mit Vault, AWS Secrets Manager oder ähnlichen Lösungen verwalten.

**3. Monitoring und Protokollierung:**
- Protokolle zentral mit ELK oder Loki sammeln.
- Metriken mit Prometheus erfassen.
- Verteiltes Tracing mit Jaeger oder Zipkin nutzen.
- Zustandsprüfungen und Readiness-Probes einrichten.

**4. Netzwerk:**
- Overlay-Netzwerke für mehrere Hosts nutzen.
- Ein Service Mesh wie Istio oder Linkerd einsetzen.
- Netzwerkregeln für mehr Sicherheit festlegen.
- Dienste über DNS erkennen lassen.

### Bewährte Verfahren für VMs

**1. Ressourcen zuweisen:**
- VMs passend dimensionieren und Überprovisionierung vermeiden.
- Ressourcenpools und Limits verwenden.
- VM-Vorlagen einsetzen.
- Ressourcennutzung überwachen.

**2. Hochverfügbarkeit:**
- VMs hostübergreifend clustern.
- Automatisches Failover einrichten.
- Gemeinsamen Speicher wie SAN oder NAS verwenden.
- Regelmäßig Backups erstellen und testen.

**3. Sicherheit:**
- Netzwerke mit VLANs segmentieren.
- Regelmäßig Patches installieren.
- Speicher und Übertragung verschlüsseln.
- Zugriffe kontrollieren und Audits durchführen.

**4. Leistung:**
- Paravirtualisierte Treiber verwenden.
- Kritischen VMs dedizierte Ressourcen zuweisen.
- NUMA bei großen VMs berücksichtigen.
- Speicherleistung optimieren.

## Zukunftstrends: Was kommt als Nächstes?

### Entwicklung der Container

**1. Rootless- und nicht privilegierte Container:**
- Bessere Sicherheit ohne Root-Rechte.
- Weitere Verbreitung in regulierten Branchen.
- Kleinere Angriffsfläche.

**2. WebAssembly-Container (Wasm):**
- Sehr leichtgewichtige Ausführung.
- Plattformübergreifendes Binärformat.
- Schnellere Starts als bei herkömmlichen Containern.
- Wachsende Integration von Docker und Wasm.

**3. eBPF-Integration:**
- Erweiterte Netzwerk- und Sicherheitsfunktionen.
- Beobachtbarkeit auf Kernel-Ebene.
- Verbessertes Leistungsmonitoring.

**4. GPU- und KI/ML-Beschleunigung:**
- Bessere gemeinsame GPU-Nutzung in Containern.
- Optimierung von KI/ML-Workloads.
- ML-Plattformen für Container.

### Innovationen bei VMs

**1. Vertrauliches Computing:**
- Hardwareverschlüsselter VM-Speicher.
- Sichere Enklaven für sensible Daten.
- Integration von AMD SEV und Intel SGX.

**2. VM-Container-Hybrid:**
- Kata Containers und gVisor.
- Isolation auf VM-Ebene mit der Benutzerfreundlichkeit von Containern.
- Vorteile beider Technologien verbinden.

**3. Edge Computing:**
- Leichtgewichtige Hypervisoren.
- Micro-VMs wie Firecracker.
- Für Edge optimierte Virtualisierung.

## Fazit: Die richtige Technologie wählen

2026 geht es bei der Debatte **Docker oder VMs** nicht darum, welche Technologie „besser“ ist. Entscheidend ist, welches Werkzeug zu den eigenen Anforderungen passt.

**Docker wählen, wenn du:**
- Moderne Microservice-Anwendungen entwickelst.
- Ressourceneffizienz und Dichte maximieren willst.
- Schnell skalieren und bereitstellen musst.
- DevOps- und Cloud-Architekturpraktiken nutzt.
- Zustandslose Anwendungen ausführst.
- Die Produktivität von Entwicklern priorisierst.

**VMs wählen, wenn du:**
- Ältere monolithische Anwendungen ausführst.
- Starke Sicherheitsisolation benötigst.
- Umgebungen mit mehreren Betriebssystemen unterstützt.
- Traditionelle zustandsbehaftete Datenbanken verwaltest.
- Strenge Compliance-Anforderungen erfüllen musst.
- In klassischen Unternehmensumgebungen arbeitest.

**Beides nutzen, wenn du:**
- Schrittweise zu Containern migrierst.
- Gemischte Workloads betreibst.
- Flexibilität und Wahlmöglichkeiten brauchst.
- Eine Hybrid-Cloud-Infrastruktur aufbaust.

Die erfolgreichsten Unternehmen verfolgen 2026 einen **pragmatischen Ansatz**: Container für neue für die Cloud entwickelte Anwendungen und geeignete bestehende Workloads, VMs für Altsysteme und Einsatzfälle, die ihre Stärken erfordern. Diese Hybridstrategie ermöglicht es, jeden Workload einzeln zu optimieren und gleichzeitig den Betrieb effizient zu halten.

Wenn du beide Technologien verstehst, kannst du fundierte Architekturentscheidungen treffen und Leistung, Sicherheit, Kosten und Betrieb für deine Umgebung abwägen.

______

## Quellen

- [Offizielle Docker-Dokumentation](https://docs.docker.com/)
- [Kubernetes-Dokumentation](https://kubernetes.io/docs/)
- [VMware-vSphere-Dokumentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Microsoft-Hyper-V-Dokumentation](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/)
- [KVM-Virtualisierung](https://www.linux-kvm.org/)
- [CNCF Cloud Native Landscape](https://landscape.cncf.io/)
- [Bewährte Verfahren zur Docker-Sicherheit](https://docs.docker.com/engine/security/)
- [NIST-Leitfaden zur Sicherheit von Anwendungscontainern](https://www.nist.gov/publications/application-container-security-guide)
- [Proxmox VE](https://www.proxmox.com/en/proxmox-ve)
- [AWS-Containerdienste](https://aws.amazon.com/containers/)
