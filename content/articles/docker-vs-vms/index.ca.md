---
title: "Docker i màquines virtuals: comparació de 2026"
date: 2023-02-02
lastmod: 2026-11-15
toc: true
draft: false
description: "Comparació de 2026 entre contenidors Docker i màquines virtuals pel que fa al rendiment, la seguretat, el cost, els casos d'ús i l'adequació al desplegament."
tags: ["Docker", "Màquines virtuals", "VM", "Computació al núvol", "Contenidors", "Kubernetes", "Simplicitat", "Escalabilitat", "Seguretat", "Rendibilitat", "Dockerfile", "Docker contra VM", "contenidors contra VM", "contenidors Docker", "virtualització", "contenidorització", "compilació, proves i desplegament", "aïllament", "historial de seguretat", "comparació de costos", "VMware", "Hyper-V", "KVM", "orquestració de contenidors", "microserveis", "DevOps", "infraestructura", "núvol natiu", "comparació de rendiment", "eficiència dels recursos", "enfocament híbrid", "rendiment de Docker", "rendiment de VM", "quan fer servir Docker", "quan fer servir VM"]
cover: "/img/cover/An_image_of_a_cargo_ship_shaped_like_a_blue_whale_carrying.webp"
coverAlt: "Un vaixell de càrrega amb forma de balena blava que transporta diversos contenidors Docker"
coverCaption: ""
---

## Docker i màquines virtuals: la comparació definitiva de 2026

Amb l'evolució ràpida de la computació al núvol i el desplegament d'aplicacions, l'elecció entre **contenidors Docker** i **màquines virtuals (VM)** és cada vegada més complexa. El debat original entre Docker i les VM presentava aquestes tecnologies com a rivals. El 2026, la realitat és més complexa: totes dues tenen funcions importants, però diferents, dins la infraestructura moderna.

Aquesta guia examina Docker i les VM des de les perspectives tècnica, operativa i empresarial per ajudar-te a triar la tecnologia més adequada per als teus casos d'ús.

## Conceptes fonamentals

### Què és Docker?

**Docker** és una plataforma de contenidors que agrupa aplicacions i les seves dependències en unitats estàndard anomenades contenidors. Docker ofereix:

- **Virtualització a nivell d'aplicació**: els contenidors comparteixen el nucli del sistema operatiu amfitrió.
- **Aïllament lleuger**: aïllament de processos i recursos sense la sobrecàrrega d'un sistema operatiu complet.
- **Infraestructura immutable**: els contenidors són efímers i reproduïbles.
- **Facilitat per als desenvolupadors**: configuració declarativa senzilla amb Dockerfiles.
- **Lideratge de l'ecosistema**: posició dominant en tecnologia de contenidors, amb més de 13 milions d'imatges a Docker Hub.

El 2026, Docker Engine 26.x ha evolucionat considerablement i ofereix funcions de seguretat millorades, una gestió dels recursos més bona i una integració fluida amb orquestradors com Kubernetes i Docker Swarm.

### Què són les màquines virtuals (VM)?

Les **màquines virtuals** emulen sistemes informàtics complets, inclòs el maquinari, i executen sistemes operatius sencers sobre un hipervisor. Les VM ofereixen:

- **Virtualització a nivell de maquinari**: aïllament complet del sistema operatiu, inclòs el nucli.
- **Límits d'aïllament forts**: cada VM s'executa independentment amb el seu propi sistema operatiu.
- **Compatibilitat amb sistemes antics**: executar qualsevol sistema operatiu en qualsevol maquinari.
- **Ecosistema madur**: dècades d'eines empresarials i solucions de gestió.
- **Fiabilitat provada**: tecnologia contrastada en entorns empresarials.

Les tecnologies modernes de VM inclouen VMware vSphere 9, Microsoft Hyper-V 2025, KVM (Kernel-based Virtual Machine) i Proxmox VE, que el 2026 ofereixen millores de rendiment i gestió.

### Comparació d'arquitectures

#### Arquitectura dels contenidors Docker

```
┌─────────────────────────────────────────┐
│            Cont. aplicació 1            │
│  ┌──────────────────────────────────┐  │
│  │        App + bibl. + dep.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│            Cont. aplicació 2            │
│  ┌──────────────────────────────────┐  │
│  │        App + bibl. + dep.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                 Docker                  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│               SO amfitrió               │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Maquinari                │
└─────────────────────────────────────────┘
```

#### Arquitectura de les màquines virtuals

```
┌─────────────────────────────────────────┐
│                  VM 1                   │
│  ┌──────────────────────────────────┐  │
│  │     SO convidat + app + dep.     │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                  VM 2                   │
│  ┌──────────────────────────────────┐  │
│  │     SO convidat + app + dep.     │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│             Hipervisor 1/2              │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│               SO amfitrió               │
│                (tipus 2)                │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Maquinari                │
└─────────────────────────────────────────┘
```

## Diferències clau: taula comparativa de Docker i les VM

| Característica | Contenidors Docker | Màquines virtuals |
|---------|-------------------|---------------------|
| **Temps d'inici** | 50-500 mil·lisegons | 30-120 segons |
| **Sistema operatiu necessari** | Comparteix el nucli del sistema amfitrió | Sistema operatiu complet per VM |
| **Sobrecàrrega de recursos** | Uns 100 MB normalment | 2-8 GB com a mínim |
| **Nivell d'aïllament** | A nivell de procés | A nivell de maquinari |
| **Portabilitat** | Molt portable | Menys portable |
| **Densitat** | Normalment, més de 100 per amfitrió | Normalment, 10-20 per amfitrió |
| **Mida de la imatge** | 50-500 MB | 2-50 GB |
| **Rendiment** | Gairebé natiu | Sobrecàrrega del 5-15% |
| **Dependència d'arrencada** | Sistema operatiu amfitrió | Hipervisor i sistema operatiu convidat |
| **Emmagatzematge** | Sistema de fitxers per capes (CoW) | Imatges de disc completes |
| **Xarxa** | Xarxes bridge/overlay | Commutadors virtuals |
| **Aïllament de seguretat** | Namespaces/cgroups | Aïllament complet del sistema operatiu |
| **Complexitat de gestió** | Baixa o moderada | Moderada o alta |
| **Ideal per a** | Microserveis, aplicacions sense estat | Monòlits, sistemes antics, diversos sistemes operatius |

## Comparació de rendiment: proves de 2026

### Ús de recursos

**Contenidors Docker:**
- **Sobrecàrrega de CPU**: menys de l'1%, rendiment gairebé natiu.
- **Sobrecàrrega de memòria**: 10-50 MB per contenidor.
- **E/S de disc**: gairebé nativa amb el controlador d'emmagatzematge overlay2.
- **Rendiment de xarxa**: 95-99% del maquinari físic.
- **Temps d'inici**: 200 ms de mitjana per a aplicacions habituals.

**Màquines virtuals:**
- **Sobrecàrrega de CPU**: 5-10% per a l'hipervisor.
- **Sobrecàrrega de memòria**: sistema operatiu complet, 2-4 GB com a mínim per VM.
- **E/S de disc**: 80-95% del rendiment del maquinari físic.
- **Rendiment de xarxa**: 85-95% del maquinari físic.
- **Temps d'inici**: 30-90 segons de mitjana.

### Comparació de densitat

**Servidor habitual amb 64 GB de RAM:**

**Amb contenidors Docker:**
- Sistema operatiu amfitrió: 4 GB.
- Docker Engine: 1 GB.
- Memòria restant per als contenidors: 59 GB.
- Mida mitjana d'un contenidor: 500 MB.
- **Capacitat teòrica**: 118 contenidors.
- **Capacitat pràctica**: 80-100 contenidors amb límits de recursos adequats.

**Amb màquines virtuals:**
- Hipervisor: 2 GB.
- Memòria restant per a les VM: 62 GB.
- Mida mitjana d'una VM: 4 GB.
- **Capacitat teòrica**: 15 VM.
- **Capacitat pràctica**: 10-12 VM amb un marge còmode.

### Resultats de les proves de rendiment (2026)

| Prova | Docker | VM (KVM) | Maquinari físic | Docker % | VM % |
|-----------|--------|----------|------------|----------|------|
| CPU amb nombres enters | 98.5 | 92.3 | 100 | 98.5% | 92.3% |
| CPU de coma flotant | 97.8 | 91.7 | 100 | 97.8% | 91.7% |
| Amplada de banda de memòria | 99.2 | 89.4 | 100 | 99.2% | 89.4% |
| Lectura seqüencial de disc | 96.7 | 87.2 | 100 | 96.7% | 87.2% |
| E/S aleatòria de disc | 94.3 | 82.6 | 100 | 94.3% | 82.6% |
| Cabal de xarxa | 97.1 | 88.9 | 100 | 97.1% | 88.9% |
| Latència de xarxa | 98.4 | 90.1 | 100 | 98.4% | 90.1% |

*Proves fetes amb Intel Xeon Platinum 8380 i Ubuntu 24.04 LTS (Docker) i l'hipervisor KVM (VM).*

## Avantatges de Docker: per què els contenidors dominen el desenvolupament modern

### 1. Simplicitat i experiència de desenvolupament

**Simplicitat del Dockerfile:**
Docker fa servir configuració declarativa mitjançant Dockerfiles, cosa que facilita l'empaquetatge d'aplicacions:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

Aquest únic fitxer defineix tot l'entorn de l'aplicació, les dependències i la configuració d'execució.

**Comparació amb les VM:**
Crear una VM requereix:
- Triar i instal·lar un sistema operatiu complet (30-60 minuts).
- Configurar la xarxa i l'emmagatzematge.
- Instal·lar manualment les dependències de l'aplicació.
- Crear instantànies o plantilles.
- Gestionar les actualitzacions i els pedaços del sistema operatiu.

### 2. Portabilitat excepcional

**«Construeix una vegada, executa a tot arreu»:**
Els contenidors Docker funcionen de la mateixa manera a:
- Ordinadors portàtils dels desenvolupadors (Windows, Mac, Linux).
- Servidors de canalitzacions CI/CD.
- Entorns de proves.
- Núvols de producció (AWS, Azure, GCP).
- Centres de dades locals.
- Dispositius de computació a la perifèria.

**Exemple real:**
Un desenvolupador crea un contenidor a macOS. El mateix contenidor s'executa sense canvis a:
- La canalització CI de GitHub Actions (Linux).
- L'entorn de producció AWS ECS.
- L'entorn de proves Azure Kubernetes Service.
- El clúster Kubernetes local de desenvolupament.

Les VM necessiten imatges i configuracions específiques per a cada plataforma d'hipervisor.

### 3. Inici rapidíssim

**Arrencada de contenidors Docker:**
- **Aplicació web**: 200-500 ms.
- **Contenidor de base de dades**: 1-3 segons.
- **Microservei**: 50-200 ms.

**Arrencada de VM:**
- **VM Linux lleugera**: 10-30 segons.
- **VM Windows Server**: 45-90 segons.
- **VM d'escriptori completa**: 60-120 segons.

Aquesta diferència de més de 100 vegades en velocitat permet:
- **Escalat ràpid**: respondre als pics de càrrega en segons.
- **Autoreparació**: substituir immediatament els contenidors que fallen.
- **Eficiència CI/CD**: executar milers d'entorns de proves cada dia.
- **Velocitat de desenvolupament**: canviar d'entorn a l'instant.

### 4. Eficiència dels recursos i estalvi de costos

**Avantatges de Docker:**

**Economia de memòria:**
- 100 microserveis Node.js amb Docker: uns 50 GB de RAM.
- La mateixa càrrega amb VM: uns 400 GB de RAM.
- **Estalvi**: reducció del 87,5% dels requisits de memòria.

**Economia d'emmagatzematge:**
- Les capes de les imatges Docker es comparteixen entre contenidors.
- Imatge base (Ubuntu): 50 MB, compartida per tots els contenidors.
- Capes d'aplicació: 100-500 MB cadascuna.
- **Resultat**: compartir les capes redueix molt l'espai necessari.

**Exemple de càlcul:**
10 aplicacions Python:
- **Docker**: 1 imatge base de Python (300 MB) + 10 capes d'aplicació (50 MB cadascuna) = 800 MB en total.
- **VM**: 10 imatges completes del sistema operatiu + Python (3 GB cadascuna) = 30 GB.
- **Estalvi**: reducció del 97,3% de l'emmagatzematge.

### 5. Admet l'arquitectura de microserveis

Docker és la base dels microserveis moderns:

**Avantatges:**
- **Escalat independent**: escalar serveis individuals segons la demanda.
- **Desenvolupament políglota**: fer servir llenguatges diferents per servei.
- **Aïllament d'errors**: els errors d'un servei no s'estenen als altres.
- **Desplegament continu**: actualitzar els serveis per separat.
- **Autonomia dels equips**: cada equip és responsable de tota la pila dels seus serveis.

**Exemple d'arquitectura:**
```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Interfície  │ │     API     │ │    Accés    │
│   (React)   │ │  (Node.js)  │ │    (Go)     │
│    Cont.    │ │    Cont.    │ │    Cont.    │
└─────────────┘ └─────────────┘ └─────────────┘
       │               │               │
       └───────────────┴───────────────┘
                       │
            ┌──────────┴──────────┐
            │                     │
    ┌─────────────┐      ┌─────────────┐
    │    Dades    │      │   Memòria   │
    │ (Postgres)  │      │   (Redis)   │
    │    Cont.    │      │    Cont.    │
    └─────────────┘      └─────────────┘
```

### 6. Integració amb DevOps i CI/CD

Docker ha revolucionat les canalitzacions CI/CD:

**Exemple de canalització moderna:**
1. **Commit**: el desenvolupador puja el codi.
2. **Build**: el servidor CI construeix una imatge Docker (1-3 minuts).
3. **Test**: s'inicien contenidors per a proves automatitzades (segons).
4. **Scan**: anàlisi de seguretat de les capes de la imatge.
5. **Push**: càrrega al registre de contenidors.
6. **Deploy**: desplegament a producció (segons per instància).
7. **Rollback**: retorn immediat a la imatge anterior si cal.

**Comparació amb les VM:**
Les canalitzacions tradicionals basades en VM:
1. **Commit**: el desenvolupador puja el codi.
2. **Build VM Image**: crear una imatge VM nova (15-30 minuts).
3. **Deploy VM**: preparar VM noves (5-10 minuts).
4. **Test**: executar les proves a les VM.
5. **Rollback**: recrear l'estat anterior de la VM (10-15 minuts).

**Resultat**: les canalitzacions Docker són entre 10 i 20 vegades més ràpides.

## Avantatges de les màquines virtuals: quan destaquen

Malgrat els avantatges de Docker, les VM continuen sent essencials per a casos d'ús concrets.

### 1. Aïllament de seguretat superior

**Aïllament a nivell de maquinari:**
Les VM ofereixen una separació completa a nivell de nucli:
- Cada VM té el seu propi nucli.
- L'hipervisor imposa límits protegits pel maquinari.
- Les vulnerabilitats del nucli no travessen els límits entre VM.
- Adequades per a entorns multiinquilí que executen codi no fiable.

**Comparació de seguretat:**

| Funció de seguretat | Docker | VM | Guanyador |
|-----------------|--------|-----|--------|
| Aïllament del nucli | Nucli compartit | Nuclis separats | VM |
| Dificultat de sortida | Possible sortida de namespace | Sortida de l'hipervisor poc habitual | VM |
| Atacs als recursos | Límits de cgroups | Límits de maquinari | VM |
| Preparació per al compliment | Cal reforçar-lo | Aïllament integrat | VM |
| Multiinquilí | No recomanat | Estàndard del sector | VM |

**Cas d'ús:** les entitats financeres que executen aplicacions de clients sovint exigeixen aïllament a nivell de VM per complir la normativa i garantir la seguretat.

### 2. Control complet i flexibilitat del sistema operatiu

**Executar qualsevol sistema operatiu:**
Les VM poden executar:
- Famílies diferents de sistemes operatius al mateix maquinari (Windows i Linux).
- Sistemes operatius antics (Windows Server 2008, RHEL 5).
- Distribucions especialitzades (BSD, Solaris).
- Configuracions de nucli personalitzades.
- Sistemes operatius que necessiten mòduls específics del nucli.

**Exemples de situacions:**
- **Aplicacions Windows en amfitrions Linux**: executar VM Windows Server en un hipervisor Linux.
- **Sistemes antics**: mantenir aplicacions que necessiten versions concretes del sistema operatiu.
- **Proves del nucli**: provar nuclis Linux personalitzats amb seguretat.
- **Desenvolupament amb diversos sistemes operatius**: executar macOS, Windows i Linux simultàniament.

### 3. Millors per a aplicacions amb estat i sistemes antics

**Les VM destaquen per a:**

**Aplicacions amb estat:**
- Bases de dades SQL tradicionals (Oracle, SQL Server).
- Aplicacions empresarials (SAP, sistemes ERP antics).
- Sistemes de missatgeria amb estat.
- Aplicacions que esperen emmagatzematge local persistent.

**Monòlits antics:**
- Aplicacions empresarials grans que no s'han dissenyat per als contenidors.
- Aplicacions amb camins del sistema de fitxers codificats.
- Programari que necessita configuracions específiques del sistema operatiu.
- Programari llicenciat vinculat al maquinari o al sistema operatiu.

**Exemple:**
Una empresa executa SAP ERP:
- Necessita Windows o Linux amb paràmetres concrets del nucli.
- Requereix emmagatzematge persistent amb sistemes de fitxers específics.
- Té requisits de xarxa complexos.
- Necessita personalització a nivell de sistema operatiu.
- **Solució**: una màquina virtual és l'opció pràctica.

### 4. Gestió empresarial provada

**Eines madures:**
- **VMware vCenter**: gestió completa del centre de dades.
- **Microsoft System Center**: gestió del cicle de vida de VM empresarials.
- **Red Hat Virtualization**: virtualització empresarial de codi obert.
- **Proxmox**: gestió completa de VM.

**Funcions empresarials:**
- **Migració en calent**: moure VM en execució entre amfitrions sense interrupció.
- **Alta disponibilitat**: reiniciar VM automàticament quan falla el maquinari.
- **Recuperació davant desastres**: eines de còpia de seguretat, instantànies i rèplica.
- **Gestió de recursos**: assignació avançada de CPU i memòria.
- **Compliment**: auditoria i funcions de seguretat integrades.

### 5. Millors per a entorns amb diversos sistemes operatius

**Infraestructura heterogènia:**
Les VM admeten fàcilment, al mateix maquinari compartit:
- Aplicacions Windows Server.
- Serveis Linux.
- Sistemes Unix (AIX, Solaris).
- Aparells de xarxa.
- Tots aquests sistemes.

**Escenari real:**
Centre de dades empresarial:
- 50 VM Windows Server (AD, Exchange, SQL Server).
- 30 VM Linux (servidors web, bases de dades).
- 10 VM especialitzades (monitoratge de xarxa, seguretat).
- Totes gestionades des d'una plataforma unificada.
- Els contenidors no permeten aquesta combinació per les diferències entre nuclis dels sistemes operatius.

## Comparació detallada de seguretat: Docker i VM

### Model de seguretat de Docker

**Mecanismes d'aïllament:**
- **Namespaces**: aïllament de processos, xarxa, muntatges, IPC i UTS.
- **Cgroups**: limitació i recompte de recursos.
- **Seccomp**: filtratge de crides al sistema.
- **AppArmor/SELinux**: control d'accés obligatori.
- **Capabilities**: control granular dels privilegis.

**Bones pràctiques de seguretat Docker (2026):**
1. **Executar Docker sense privilegis root**: utilitzar un usuari no-root.
2. **Utilitzar imatges base mínimes**: com Alpine Linux o distroless.
3. **Analitzar les imatges**: buscar vulnerabilitats amb Trivy, Snyk o Clair.
4. **Signar les imatges**: verificar-ne l'autenticitat amb Docker Content Trust.
5. **Limitar les capabilities**: eliminar privilegis Linux innecessaris.
6. **Utilitzar sistemes de fitxers de només lectura**: muntar els contenidors en mode de només lectura.
7. **Segmentar la xarxa**: utilitzar xarxes aïllades.
8. **Gestionar els secrets**: utilitzar Docker secrets o una volta externa.

**Riscos de seguretat:**
- **Nucli compartit**: tots els contenidors comparteixen el nucli de l'amfitrió.
- **Escalada de privilegis**: contenidors mal configurats poden permetre una sortida.
- **Vulnerabilitats de les imatges**: les imatges base poden no estar corregides.
- **Atacs al dimoni**: el dimoni Docker s'executa com a root.

### Model de seguretat de les VM

**Aïllament més fort:**
- **Nuclis separats**: cada VM té un nucli independent.
- **Aplicació per l'hipervisor**: aïllament reforçat pel maquinari.
- **Sense nucli compartit**: les vulnerabilitats del nucli queden limitades a una VM.
- **Seguretat madura**: reforçada durant dècades.

**Bones pràctiques de seguretat de les VM:**
1. **Utilitzar hipervisors de tipus 1**: VMware ESXi, KVM, Hyper-V.
2. **Protegir l'hipervisor**: mantenir-lo actualitzat amb pedaços.
3. **Aïllar la xarxa**: utilitzar VLAN i regles del tallafoc.
4. **Xifrar les dades**: xifrar l'emmagatzematge i la memòria.
5. **Controlar l'accés**: exigir autenticació forta a l'administració.
6. **Reforçar el sistema operatiu convidat**: instal·lar un sistema mínim.
7. **Aplicar pedaços regularment**: actualitzar l'hipervisor i el sistema operatiu convidat.

**Avantatge de seguretat:**
Les VM són adequades per a:
- Plataformes SaaS multiinquilí.
- Sectors regulats (finances, salut).
- Execució de codi no fiable.
- Entorns amb requisits d'alta seguretat.

## Anàlisi de costos: comparació del cost total de propietat

### Costos d'infraestructura

**Escenari**: allotjar 100 microserveis.

**Solució Docker:**
- **Maquinari**: 4 servidors × $5,000 = $20,000.
- **Llicències**: Docker Enterprise $150/mes × 4 = $7,200/any.
- **Total d'infraestructura**: $27,200 el primer any, $7,200/any després.

**Solució VM:**
- **Maquinari**: 20 servidors × $5,000 = $100,000.
- **VMware vSphere**: $3,000/CPU × 40 CPU = $120,000.
- **Total d'infraestructura**: $220,000 el primer any, $24,000/any en suport.

**Estalvi**: $192,800 el primer any, $16,800/any després.

### Costos operatius

**Temps de gestió:**

**Docker:**
- Temps d'instal·lació: 2-4 hores per aplicació.
- Desplegament d'actualitzacions: 1-5 minuts.
- Operacions d'escalat: automatitzades.
- Resolució d'incidències: registres centralitzats.
- **Eficiència de l'equip**: 1 enginyer gestiona més de 500 contenidors.

**VM:**
- Temps d'instal·lació: 4-8 hores per VM.
- Desplegament d'actualitzacions: 15-30 minuts.
- Operacions d'escalat: 10-30 minuts.
- Resolució d'incidències: iniciar sessió a cada VM.
- **Eficiència de l'equip**: 1 enginyer gestiona 50-100 VM.

**Exemple de costos al núvol (AWS):**

**Executar 10 aplicacions web les 24 hores del dia:**

**Docker a ECS Fargate:**
- Contenidors petits: 2 vCPU i 4 GB de RAM cadascun.
- Cost per contenidor: aproximadament $50/mes.
- **Total**: $500/mes.

**VM EC2:**
- Instàncies t3.large: 2 vCPU i 8 GB de RAM.
- Cost per instància: aproximadament $60/mes.
- **Total**: $600/mes.
- Els costos d'emmagatzematge EBS són addicionals.

**Estalvi anual**: $1,200 i reducció de la càrrega de gestió.

## Quan fer servir Docker: casos d'ús ideals

### 1. Aplicacions de microserveis
✅ **Docker és ideal**

**Característiques:**
- Serveis petits i independents.
- Disseny sense estat.
- Necessitat d'escalabilitat ràpida.
- Actualitzacions freqüents.

**Exemple:**
Plataforma de comerç electrònic:
- Servei frontal (React).
- Servei d'usuaris (Node.js).
- Catàleg de productes (Python).
- Processament de comandes (Go).
- Servei de pagament (Java).
- Cada servei s'escala independentment segons la càrrega.

### 2. Integració i desplegament continus
✅ **Docker és ideal**

**Avantatges:**
- Entorns de compilació consistents.
- Execució ràpida de proves.
- Proves en paral·lel.
- Desplegaments reproduïbles.

**Canalització CI:**
```
git push → Creeu imatge → Proveu contenidors →
Pugeu al registre → Desplegueu a staging →
Desplegament a producció (blau-verd)
```

### 3. Entorns de desenvolupament
✅ **Docker és una opció excel·lent**

**Avantatges:**
- Entorns de desenvolupament idèntics als de producció.
- Preparació ràpida de l'entorn.
- Incorporació fàcil de desenvolupadors nous.
- Evita el problema «a la meva màquina funciona».

**Experiència del desenvolupador:**
```bash
git clone repo
docker-compose up
# Entorn preparat en 30 segons
```

### 4. Aplicacions natives del núvol
✅ **Docker és l'estàndard**

Les aplicacions modernes al núvol es construeixen per a:
- Orquestració amb Kubernetes.
- Arquitectura de malla de serveis.
- Funcions sense servidor.
- Disseny basat en esdeveniments.

### 5. Escalat horitzontal
✅ **Docker hi destaca**

Aplicacions que necessiten:
- Escalat immediat durant pics de trànsit.
- Distribució geogràfica.
- Escalat automàtic segons la càrrega.
- Escalat econòmic.

**Exemple:**
Servei de vídeo en streaming:
- Base: 50 contenidors.
- Trànsit màxim: escalat automàtic a 500 contenidors en 2 minuts.
- Després del pic: reducció a 50 contenidors en 5 minuts.

## Quan fer servir màquines virtuals: casos d'ús ideals

### 1. Aplicacions empresarials antigues
✅ **Les VM són necessàries**

**Característiques:**
- Arquitectura monolítica.
- Funcions dependents del sistema operatiu.
- Procediments d'instal·lació complexos.
- No es poden contenidoritzar.

**Exemples:**
- Sistemes ERP tradicionals (SAP, Oracle EBS).
- Aplicacions .NET antigues a Windows Server.
- Aplicacions que necessiten versions concretes del sistema operatiu.
- Programari amb llicència a nivell de sistema operatiu.

### 2. Requisits de diversos sistemes operatius
✅ **Només les VM ho permeten**

**Situacions:**
- Executar aplicacions Windows al costat de Linux.
- Provar programari amb diverses versions de sistema operatiu.
- Desenvolupar amb diverses plataformes de sistema operatiu.
- Mantenir el suport de sistemes antics.

**Exemple:**
Conjunt de proves d'una empresa de programari:
- VM Windows Server 2016, 2019 i 2022.
- Distribucions Linux diverses.
- VM macOS per provar el client Mac.
- Tot plegat sobre una infraestructura física.

### 3. Requisits d'aïllament fort
✅ **Les VM ofereixen un aïllament millor**

**Casos d'ús:**
- Plataformes SaaS multiinquilí.
- Sectors regulats (salut, finances).
- Aplicacions crítiques per a la seguretat.
- Execució de codi no fiable.

**Exemple:**
Servei d'IDE al núvol:
- Cada client rep una VM dedicada.
- L'aïllament complet evita filtracions de dades.
- Seguretat a nivell de nucli.
- Compliment de les normes de protecció de dades.

### 4. Bases de dades tradicionals amb estat
✅ **Les VM són més fiables**

**Tipus de bases de dades:**
- SQL tradicional: Oracle, SQL Server, MySQL, PostgreSQL.
- Bases de dades monolítiques grans.
- Bases que necessiten ajustos específics del sistema operatiu.
- Bases de dades llicenciades vinculades al maquinari.

**Per què fer servir VM:**
- Integració amb emmagatzematge persistent.
- Millor rendiment per a càrregues intensives d'E/S.
- Eines de còpia de seguretat i recuperació.
- Menys complexitat que les bases de dades contenidoritzades.

### 5. Recuperació davant desastres i proves
✅ **Les VM ofereixen avantatges**

**Avantatges de les VM:**
- Instantànies completes del sistema.
- Conversió P2V (de físic a virtual).
- Capacitats de migració en calent.
- Solucions de còpia de seguretat provades.

**Escenari de recuperació davant desastres:**
- VM de producció replicades en un centre de recuperació.
- Canvi immediat amb un temps d'inactivitat mínim.
- Proves fàcils dels procediments de recuperació.
- Preservació completa de l'estat del sistema.

## Enfocament híbrid: fer servir totes dues tecnologies

La infraestructura moderna fa servir cada cop més **Docker i les VM** de manera estratègica:

### Arquitectura híbrida habitual

```
┌─────────────────────────────────────────┐
│              Infra. física              │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │           VM 1: node K8s           │ │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ │ │
│  │  │Docker││Docker││Docker││Docker│ │ │
│  │  │Cont. ││Cont. ││Cont. ││Cont. │ │ │
│  │  └─────┘ └─────┘ └─────┘ └─────┘ │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 2: BD Oracle           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 3: Windows AD          │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### Casos d'ús híbrids

**1. Kubernetes en VM:**
- Executar clústers Kubernetes en VM.
- Executar contenidors Docker dins de Kubernetes.
- Aïllar els clústers a nivell de VM.
- Facilitar la migració de clústers i la recuperació davant desastres.

**2. Sistemes antics i moderns:**
- Executar aplicacions antigues en VM (SAP, Oracle).
- Executar microserveis nous en contenidors.
- Migrar gradualment als contenidors.
- Aprofitar les dues tecnologies.

**3. Flux de desenvolupament:**
- Els desenvolupadors fan servir Docker localment.
- La CI/CD s'executa en contenidors.
- La preproducció i la producció fan servir Kubernetes basat en VM.
- Mantenir la seguretat i el compliment.

**4. Estratègia del núvol:**
- Migrar inicialment les càrregues a VM amb lift-and-shift.
- Refactoritzar-les per als contenidors amb el temps.
- Desplegar en un núvol híbrid.
- Flexibilitat en el ritme de modernització.

## Eines d'orquestració i gestió

### Orquestració Docker

**Kubernetes (estàndard del sector):**
- Desplegament, escalat i gestió automatitzats.
- Més del 90% de quota de mercat en orquestració de contenidors.
- Independent del núvol (AWS EKS, Azure AKS, GCP GKE).
- Autoreparació i escalat automàtic.
- Descobriment de serveis i equilibratge de càrrega.
- Actualitzacions progressives i reversions.

**Docker Swarm:**
- Orquestració nativa de Docker.
- Més senzill que Kubernetes.
- Adequat per a desplegaments petits.
- Popularitat decreixent.

**Amazon ECS/Fargate:**
- Orquestració de contenidors específica d'AWS.
- Execució de contenidors sense servidor.
- Integració profunda amb AWS.
- Fargate elimina la gestió dels clústers.

### Orquestració de VM

**VMware vSphere:**
- Estàndard empresarial per a la gestió de VM.
- vMotion per a la migració en calent.
- DRS per a l'equilibri de recursos.
- HA per al canvi automàtic en cas d'error.

**Microsoft Hyper-V + SCVMM:**
- Virtualització integrada a Windows.
- System Center Virtual Machine Manager.
- Integració amb Azure.
- Ideal per a entorns centrats en Windows.

**OpenStack:**
- Plataforma de núvol de codi obert.
- Suport per a diversos hipervisors.
- Infraestructura de núvol privat.
- Gestió de VM a gran escala.

**Proxmox VE:**
- Plataforma de virtualització de codi obert.
- Suport de KVM i LXC.
- Gestió basada en web.
- Econòmic per a petites i mitjanes empreses.

## Estratègies de migració

### Migrar de VM a contenidors

**Enfocament pas a pas:**

**Fase 1: avaluació (2-4 setmanes)**
1. Inventariar totes les aplicacions.
2. Identificar les candidates a contenidorització.
3. Avaluar les dependències i l'estat.
4. Planificar l'ordre de migració.

**Fase 2: projecte pilot (1-2 mesos)**
1. Seleccionar 3-5 aplicacions adequades.
2. Contenidoritzar les aplicacions pilot.
3. Provar-les a fons en preproducció.
4. Desplegar-les a producció.
5. Mesurar els resultats i aprendre'n.

**Fase 3: migració gradual (6-18 mesos)**
1. Contenidoritzar aplicacions per prioritat.
2. Mantenir una infraestructura híbrida.
3. Actualitzar les canalitzacions CI/CD.
4. Formar l'equip d'operacions.
5. Documentar els aprenentatges.

**Fase 4: optimització (contínua)**
1. Refactoritzar per a patrons natius del núvol.
2. Implementar una arquitectura de microserveis.
3. Optimitzar les imatges dels contenidors.
4. Millorar el monitoratge i l'observabilitat.

**Aplicacions adequades per començar:**
- Aplicacions web sense estat.
- Serveis d'API.
- Microserveis.
- Projectes de desenvolupament nous.

**Mantenir en VM:**
- Monòlits antics.
- Bases de dades amb estat (inicialment).
- Aplicacions només per a Windows.
- Programari amb llicència.

### Migrar de contenidors a VM

**Quan tornar a les VM:**
- Canvien els requisits de seguretat o compliment.
- Hi ha problemes de rendiment amb els contenidors.
- Apareixen limitacions de llicència.
- Cal un aïllament més fort.

**Enfocament:**
1. Crear plantilles de VM.
2. Instal·lar les dependències de l'aplicació.
3. Desplegar l'aplicació contenidoritzada a la VM.
4. Provar-ne a fons la funcionalitat.
5. Fer el canvi amb el mínim temps d'inactivitat.

## Marc de decisió: Docker o VM?

### Arbre de decisió ràpid

```
Inici: cal desplegar una aplicació
    │
    ├─ Calen diversos SO? (Windows + Linux)
    │   └─ Sí → Feu servir VM
    │
    ├─ Aplicació monolítica antiga?
    │   └─ Sí → Feu servir VM
    │
    ├─ Cal un aïllament fort? (multiinquilí)
    │   └─ Sí → Feu servir VM
    │
    ├─ Cal escalar ràpidament?
    │   └─ Sí → Feu servir Docker
    │
    ├─ Arquitectura de microserveis?
    │   └─ Sí → Feu servir Docker
    │
    ├─ Es prioritza DevOps/CI-CD?
    │   └─ Sí → Feu servir Docker
    │
    └─ Aplicació moderna nativa del núvol?
        └─ Sí → Feu servir Docker
```

### Matriu de decisió detallada

| Consideració | Triar Docker | Triar VM |
|--------------|---------------|------------|
| **Arquitectura** | Microserveis, sense estat | Monolítica, amb estat |
| **Necessitats d'escalabilitat** | Escalat automàtic ràpid | Escalat predictible |
| **Temps d'inici** | Els segons són importants | Uns minuts són acceptables |
| **Eficiència dels recursos** | Maximitzar la densitat | Prioritzar l'aïllament |
| **Velocitat de desenvolupament** | Iteració ràpida | Versions estables |
| **Pila tecnològica** | Centrada en Linux | Diversos sistemes operatius |
| **Model de seguretat** | Nucli compartit acceptable | Cal aïllament del nucli |
| **Maduresa operativa** | Cultura DevOps | TI tradicional |
| **Pressupost** | Optimització de costos | Prioritat al compliment |
| **Infraestructura existent** | Nativa del núvol | Centre de dades tradicional |

## Bones pràctiques de 2026

### Bones pràctiques Docker

**1. Optimització de les imatges:**
```dockerfile
# Utilitza compilacions en diverses etapes
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Imatge de producció
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/server.js"]
```

**2. Reforçar la seguretat:**
- Executar com a usuari no-root.
- Fer servir imatges base oficials.
- Cercar vulnerabilitats regularment.
- Aplicar el principi de mínim privilegi.
- Gestionar secrets (Vault, AWS Secrets Manager).

**3. Monitoratge i registre:**
- Registre centralitzat (ELK, Loki).
- Recollida de mètriques (Prometheus).
- Seguiment distribuït (Jaeger, Zipkin).
- Comprovacions de salut i sondes de disponibilitat.

**4. Xarxa:**
- Fer servir xarxes overlay entre diversos amfitrions.
- Implementar una malla de serveis (Istio, Linkerd).
- Definir polítiques de xarxa per a la seguretat.
- Descoberta de serveis basada en DNS.

### Bones pràctiques per a les VM

**1. Assignació de recursos:**
- Ajustar les dimensions de les VM i evitar el sobreaprovisionament.
- Fer servir grups i límits de recursos.
- Implementar plantilles de VM.
- Monitorar l'ús de recursos.

**2. Alta disponibilitat:**
- Agrupar VM entre amfitrions.
- Implementar canvi automàtic en cas d'error.
- Fer servir emmagatzematge compartit (SAN, NAS).
- Fer còpies de seguretat i proves regularment.

**3. Seguretat:**
- Segmentació de xarxa (VLAN).
- Calendari regular d'actualitzacions.
- Xifratge de l'emmagatzematge i les comunicacions.
- Control d'accés i auditoria.

**4. Rendiment:**
- Fer servir controladors paravirtualitzats.
- Assignar recursos dedicats a VM crítiques.
- Tenir en compte NUMA per a VM grans.
- Optimitzar el rendiment de l'emmagatzematge.

## Tendències futures: què ve després?

### Evolució dels contenidors

**1. Contenidors sense root i no privilegiats:**
- Seguretat més gran sense privilegis root.
- Adopció més àmplia en sectors regulats.
- Reducció de la superfície d'atac.

**2. Contenidors WebAssembly (Wasm):**
- Execució ultralleugera.
- Format binari multiplataforma.
- Inici més ràpid que els contenidors tradicionals.
- Integració creixent de Docker i Wasm.

**3. Integració d'eBPF:**
- Xarxes i seguretat avançades.
- Observabilitat a nivell de nucli.
- Monitoratge del rendiment millorat.

**4. Acceleració de GPU i IA/ML:**
- Millor ús compartit de GPU entre contenidors.
- Optimització de càrregues de treball d'IA/ML.
- Plataformes d'ML natives de contenidors.

### Innovacions de les VM

**1. Computació confidencial:**
- Memòria de VM xifrada pel maquinari.
- Enclavaments segurs per a dades sensibles.
- Integració d'AMD SEV i Intel SGX.

**2. Híbrid de VM i contenidors:**
- Kata Containers i gVisor.
- Aïllament a nivell de VM amb l'experiència dels contenidors.
- Avantatges de totes dues tecnologies.

**3. Computació a la perifèria:**
- Hipervisors lleugers.
- MicroVM (Firecracker).
- Virtualització optimitzada per a la perifèria.

## Conclusió: triar l'opció adequada

El 2026, el debat sobre **Docker contra les VM** no tracta de quina tecnologia és «millor», sinó de saber quina eina s'ajusta a les teves necessitats concretes.

**Tria Docker quan:**
- Desenvolupis aplicacions modernes de microserveis.
- Vulguis maximitzar l'eficiència i la densitat dels recursos.
- Necessitis escalat i desplegament ràpids.
- Adoptis DevOps i pràctiques natives del núvol.
- Executis aplicacions sense estat.
- Prioritzis la productivitat dels desenvolupadors.

**Tria VM quan:**
- Executis aplicacions monolítiques antigues.
- Necessitis un aïllament de seguretat fort.
- Donis suport a entorns amb diversos sistemes operatius.
- Gestionis bases de dades tradicionals amb estat.
- Compleixis requisits estrictes de compliment.
- Treballis en entorns empresarials tradicionals.

**Fes servir totes dues quan:**
- Migris gradualment als contenidors.
- Executis càrregues mixtes.
- Necessitis flexibilitat i opcions.
- Construeixis infraestructura de núvol híbrid.

Les organitzacions amb més èxit el 2026 segueixen un **enfocament pragmàtic**: contenidors per a aplicacions noves natives del núvol i càrregues existents adequades, VM per a sistemes antics i casos que necessiten els seus avantatges. Aquesta estratègia híbrida permet optimitzar cada càrrega de treball individualment i mantenir l'eficiència operativa.

Conèixer totes dues tecnologies t'ajuda a prendre decisions d'arquitectura informades que equilibrin el rendiment, la seguretat, el cost i les necessitats operatives del teu entorn.

______

## Referències

- [Documentació oficial de Docker](https://docs.docker.com/)
- [Documentació de Kubernetes](https://kubernetes.io/docs/)
- [Documentació de VMware vSphere](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Documentació de Microsoft Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/)
- [Virtualització KVM](https://www.linux-kvm.org/)
- [CNCF Cloud Native Landscape](https://landscape.cncf.io/)
- [Bones pràctiques de seguretat de Docker](https://docs.docker.com/engine/security/)
- [Guia de seguretat dels contenidors d'aplicació del NIST](https://www.nist.gov/publications/application-container-security-guide)
- [Proxmox VE](https://www.proxmox.com/en/proxmox-ve)
- [Serveis de contenidors AWS](https://aws.amazon.com/containers/)
