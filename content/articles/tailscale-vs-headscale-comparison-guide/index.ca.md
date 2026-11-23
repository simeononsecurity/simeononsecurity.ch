---
title: "Comparació entre Tailscale i Headscale"
date: 2026-05-24
lastmod: 2026-11-23
toc: true
draft: false
description: "Compara Tailscale i Headscale segons el model d'allotjament, la identitat, les funcions, el cost, les operacions i l'assistència per triar una VPN de malla basada en WireGuard que s'adapti a les teves necessitats."
genre: ["VPN", "Seguretat de xarxa", "Allotjament propi", "WireGuard", "Confiança zero", "Xarxes de malla", "Codi obert", "Infraestructura al núvol", "Accés remot", "Gestió de xarxes"]
tags: ["tailscale en comparació amb headscale", "headscale en comparació amb tailscale", "vpn amb allotjament propi", "vpn amb wireguard", "vpn de malla", "xarxes de confiança zero", "alternativa a tailscale", "configuració de headscale", "comparació de vpn", "vpn de codi obert", "preus de tailscale", "funcions de headscale", "malla amb wireguard", "xarxa privada", "rendiment de la vpn", "funcions de tailscale", "instal·lació de headscale", "xarxes de malla", "accés remot segur", "seguretat de la vpn", "coordinació de xarxa", "tailnet", "desplegament de vpn", "vpn empresarial", "vpn per a laboratoris domèstics", "xarxes amb allotjament propi", "cost de tailscale", "headscale amb docker", "gestió de vpn", "servidor de coordinació de wireguard"]
cover: "/img/cover/tailscale-vs-headscale-comparison-guide.webp"
coverAlt: "Il·lustració d'una xarxa de malla amb dispositius interconnectats per línies lluminoses sobre un fons fosc. Els dispositius són icones estilitzades de colors vius que representen connexions segures."
coverCaption: ""
---

## Introducció

**Tailscale** i **Headscale** són servidors de coordinació que permeten crear VPN de malla segures basades en [WireGuard](https://www.wireguard.com/). Tailscale és un servei comercial allotjat al núvol amb un pla gratuït generós, mentre que Headscale és una alternativa de codi obert amb allotjament propi que implementa el protocol de control de Tailscale. Entendre les diferències entre aquestes solucions és essencial per triar l'opció que s'ajusti a les necessitats de xarxa de la teva organització.

La decisió principal és **qui controla el pla de control**. Tria Tailscale si la gestió de la identitat, l'administració i l'assistència són les prioritats. Valora Headscale si l'allotjament propi i el control de les dades de coordinació justifiquen la feina operativa addicional. Les seccions següents comparen les funcions, el rendiment, el cost, la seguretat i el manteniment.

______

## Com funcionen les VPN de malla i WireGuard

Abans de comparar les dues opcions, convé entendre la tecnologia en què es basen:

### Què és WireGuard?

**WireGuard** és un protocol VPN modern i d'alt rendiment que ofereix:
- **Rendiment excepcional:** Fins a 10 vegades més ràpid que OpenVPN
- **Superfície d'atac mínima:** Només unes 4.000 línies de codi (davant de més de 100.000 d'OpenVPN)
- **Criptografia moderna:** Curve25519, ChaCha20, Poly1305
- **Integrat al nucli de Linux:** Des de Linux 5.6 (2020)

### Què és una VPN de malla?

Una **VPN de malla** estableix connexions directes entre dispositius en comptes d'encaminar tot el trànsit a través d'un servidor central:
- **Connexions directes:** Els dispositius es connecten directament entre si quan és possible
- **Pas a través de NAT:** Travessa automàticament tallafocs i dispositius NAT
- **Menys latència:** Evita salts innecessaris per servidors centrals
- **Millor rendiment:** Aprofita tota l'amplada de banda entre iguals

### La funció dels servidors de coordinació

WireGuard, per si sol, és un protocol. Per crear una VPN de malla, necessites un **servidor de coordinació** (o pla de control) que:
- Gestioni l'autenticació i l'autorització dels dispositius
- Distribueixi les claus de xifratge
- Faciliti el pas a través de NAT i el descobriment d'iguals
- Gestioni les polítiques de control d'accés
- Proporcioni resolució DNS dins de la xarxa

Tant **Tailscale** com **Headscale** són servidors de coordinació que s'encarreguen d'aquestes tasques.

______

## Comparació entre Tailscale i Headscale: visió general

| Aspecte | Tailscale | Headscale |
|--------|-----------|-----------|
| **Tipus** | SaaS comercial | Codi obert, allotjament propi |
| **Llicència** | Propietària (amb pla gratuït) | Llicència BSD de 3 clàusules |
| **Allotjament** | Al núvol (gestionat per Tailscale) | Propi (el gestiones tu) |
| **Primera versió** | 2019 | 2020 |
| **Responsable principal del manteniment** | Tailscale Inc. | Juan Font i la comunitat |
| **Estrelles a GitHub** | No aplicable (codi tancat) | Més de 38.900 (el 2026) |
| **Complexitat de la configuració** | Molt baixa (5 minuts) | Moderada (30-60 minuts) |
| **Cost mensual (100 usuaris)** | De $0 (gratuït) a $18 per usuari (empresarial) | Només el cost d'allotjar el servidor ($5-50 al mes) |
| **Compatibilitat del protocol** | Protocol de Tailscale | Protocol de Tailscale (compatible) |

______

## Comparació detallada de funcions

### Funcions bàsiques de xarxa

| Funció | Tailscale | Headscale | Observacions |
|---------|-----------|-----------|-------|
| **Malla basada en WireGuard** | ✅ Sí | ✅ Sí | Tots dos fan servir WireGuard per a totes les connexions entre iguals |
| **Pas automàtic a través de NAT** | ✅ Sí | ✅ Sí | STUN/DERP per garantir una connexió fiable |
| **Encaminament de subxarxes** | ✅ Sí | ✅ Sí | Accés a xarxes situades rere una passarel·la |
| **Nodes de sortida** | ✅ Sí | ✅ Sí | Encaminament de tot el trànsit d'internet a través d'un node |
| **MagicDNS** | ✅ Sí | ✅ Sí | Resolució de noms dins de la xarxa de malla |
| **DNS dividit** | ✅ Sí | ✅ Sí | Configuració de DNS específica per a determinats dominis |
| **Encaminament d'alta disponibilitat** | ✅ Sí | ✅ Sí | Commutació automàtica entre rutes en cas de fallada |
| **Compatibilitat amb IPv6** | ✅ Completa | ✅ Completa | Adreçament IPv6 complet a la malla |
| **Compatibilitat amb multidifusió** | ❌ No | ❌ No | Actualment, cap dels dos admet la multidifusió |

### Control d'accés i seguretat

| Funció | Tailscale | Headscale | Observacions |
|---------|-----------|-----------|-------|
| **Motor d'ACL** | ✅ Avançat | ✅ Compatible | Headscale implementa la sintaxi d'ACL de Tailscale |
| **Control d'accés basat en etiquetes** | ✅ Sí | ✅ Sí | Agrupa dispositius mitjançant etiquetes |
| **Gestió d'usuaris i grups** | ✅ Sí | ✅ Sí | Headscale fa servir el concepte d'«usuaris» |
| **OpenID Connect (OIDC)** | ✅ Sí | ✅ Sí | Autenticació amb Google, Okta, Keycloak, etc. |
| **Autenticació SAML** | ✅ Sí (Enterprise) | ❌ No | Només Tailscale |
| **Tailnet Lock** | ✅ Sí | ❌ No | Impedeix l'ús de servidors de coordinació no autoritzats |
| **Comprovacions de l'estat de seguretat dels dispositius** | ✅ Sí (beta) | ❌ No | Verifica que els dispositius compleixin els requisits abans de donar-los accés |
| **Accés puntual** | ✅ Sí | ❌ No | Permisos elevats temporals |
| **Registres d'auditoria** | ✅ Detallats | ⚠️ Bàsics | Tailscale proporciona registres detallats |

### Gestió i administració

| Funció | Tailscale | Headscale | Limitacions |
|---------|-----------|-----------|-------------|
| **Interfície web** | ✅ Oficial | ⚠️ De la comunitat | Headscale té diverses interfícies creades per la comunitat |
| **Gestió per CLI** | ✅ Sí | ✅ Sí | Tots dos ofereixen eines completes de línia d'ordres |
| **API REST** | ✅ Sí | ✅ Sí | Automatitza tasques de gestió |
| **API gRPC** | ❌ No | ✅ Sí | Headscale ofereix gRPC per al control remot |
| **Proveïdor de Terraform** | ✅ Oficial | ❌ No | Integració amb la infraestructura com a codi |
| **Operador de Kubernetes** | ✅ Oficial | ⚠️ De la comunitat | Operador de la comunitat per a Headscale |
| **Aplicacions mòbils** | ✅ iOS, Android | ✅ Compatibles | Fes servir les aplicacions de Tailscale amb el servidor de Headscale |
| **Consola d'administració** | ✅ Completa | ❌ No | Headscale depèn de la CLI o l'API |
| **Accés per a diversos administradors** | ✅ Sí | ⚠️ Manual | Headscale requereix una implementació a mida |

### Funcions avançades

| Funció | Tailscale | Headscale | Observacions |
|---------|-----------|-----------|-------|
| **Tailscale SSH** | ✅ Sí | ⚠️ Només com a servidor | Els nodes de Headscale poden actuar com a servidors SSH, però no com a clients |
| **Taildrop (compartició de fitxers)** | ✅ Sí | ⚠️ Incomplet | Compatibilitat limitada amb Taildrop a Headscale |
| **Funnel (accés públic entrant)** | ✅ Sí | ❌ No | Exposa serveis a la internet pública |
| **Serve (compartició privada)** | ✅ Sí | ❌ No | Comparteix serveis dins de la tailnet |
| **Recopilació de serveis** | ✅ Sí | ❌ Limitada | Descobreix serveis a la xarxa |
| **Tailscale DERP** | ✅ Xarxa mundial | ⚠️ Integrat | Headscale incorpora DERP i permet fer-ne servir un de propi |
| **Servidors DERP personalitzats** | ✅ Sí | ✅ Sí | Tots dos admeten servidors de retransmissió personalitzats |
| **Extensió de Docker** | ✅ Sí | ❌ No | Extensió de Tailscale per a Docker que connecta contenidors en xarxa |

______

## Comparació de preus (2026)

### Preus de Tailscale

| Pla | Cost mensual | Cost anual | Dispositius | Funcions |
|------|-------------|-------------|---------|----------|
| **Personal** | $0 | $0 | Fins a 100 | 1 usuari, funcions bàsiques i assistència de la comunitat |
| **Personal Pro** | $6 per usuari al mes | $48 per usuari a l'any | Il·limitats | Diversos usuaris, encaminament de subxarxes i ACL |
| **Team** | $10 per usuari al mes | $100 per usuari a l'any | Il·limitats | Consola d'administració, registres d'auditoria i SSO |
| **Business** | $15 per usuari al mes | $150 per usuari a l'any | Il·limitats | ACL avançades, grups d'usuaris i assistència prioritària |
| **Enterprise** | $18+ per usuari al mes | A mida | Il·limitats | Tailnet Lock, SAML, assistència dedicada i SLA |

**Nota:** El pla gratuït Personal de Tailscale admet fins a 100 dispositius per a ús personal, un límit molt generós per a laboratoris domèstics i desplegaments petits.

### Costos de Headscale

Headscale és **gratuït i de codi obert**, però has d'assumir els costos de la infraestructura:

| Recurs | Rang de cost mensual | Observacions |
|----------|-------------------|-------|
| **VPS petit** (1 CPU, 1 GB de RAM) | $5-10 | Adequat per a menys de 50 dispositius |
| **VPS mitjà** (2 CPU, 4 GB de RAM) | $15-25 | Adequat per a 50-200 dispositius |
| **VPS gran** (4 CPU, 8 GB de RAM) | $40-80 | Adequat per a 200-1.000 dispositius o més |
| **Nom de domini** | $10-15 a l'any | Per als certificats TLS |
| **Amplada de banda** | Normalment inclosa | Consulta els límits del proveïdor del VPS |
| **Temps necessari** | Variable | Configuració, manteniment i actualitzacions |

**Cost total de propietat (100 usuaris):**
- **Tailscale:** $0 (pla gratuït) o $1.000-1.800 al mes (plans de pagament)
- **Headscale:** $15-30 al mes + 5-10 hores de configuració + 2-5 hores de manteniment al mes

**Llindar de rendibilitat:** Per a les organitzacions amb més de 3-5 usuaris de pagament, Headscale surt a compte si valores el teu temps per sota de $50 per hora.

______

## Comparació del rendiment

### Latència i taxa de transferència

Tant Tailscale com Headscale fan servir WireGuard al pla de dades, de manera que **el rendiment entre iguals és idèntic**:

| Mètrica | Tailscale | Headscale |
|--------|-----------|-----------|
| **Latència addicional P2P** | <1 ms | <1 ms |
| **Taxa de transferència P2P** | Gairebé la de la connexió sense VPN (~900 Mbps en un enllaç d'1 Gbps) | Gairebé la de la connexió sense VPN |
| **Taxa de transferència del trànsit retransmès (DERP)** | 50-300 Mbps | 10-200 Mbps (depèn del teu servidor) |
| **Latència del trànsit retransmès** | +10-50 ms | +5-100 ms (depèn de la ubicació) |
| **Establiment de la connexió** | 100-500 ms | 200-800 ms |
| **Propagació de les actualitzacions de les polítiques d'ACL** | <5 segons | <30 segons |

**Diferència principal:** Tailscale opera una xarxa de retransmissió DERP amb servidors repartits arreu del món, cosa que millora el rendiment quan fallen les connexions directes. El DERP integrat de Headscale s'executa al teu servidor i pot tenir més latència si no el desplegues en diverses ubicacions geogràfiques.

### Escalabilitat

| Aspecte | Tailscale | Headscale |
|--------|-----------|-----------|
| **Màxim de nodes** | Més de 100.000 (en proves) | Uns 5.000 (segons la comunitat) |
| **Nombre recomanat de nodes** | Il·limitat | Menys de 1.000 per a un sol servidor |
| **Sol·licituds per minut (RPM) del pla de control** | Molt optimitzades | Depenen de les especificacions del servidor |
| **Memòria per node** | No aplicable (servei gestionat) | Uns 1-5 MB (al servidor) |
| **Base de dades** | PostgreSQL (gestionat) | SQLite o PostgreSQL |

______

## Comparació de la seguretat

### Seguretat de la infraestructura

| Aspecte | Tailscale | Headscale | Valoració |
|--------|-----------|-----------|------------|
| **Confiança en el servidor de coordinació** | Has de confiar en Tailscale Inc. | Tu controles el servidor | Headscale ofereix més privadesa |
| **Claus de xifratge** | Es generen als dispositius i mai s'envien a Tailscale | Es generen als dispositius i mai s'envien al servidor | ✅ Excel·lent en tots dos casos |
| **Seguretat del pla de dades** | WireGuard (excel·lent) | WireGuard (excel·lent) | ✅ Excel·lent en tots dos casos |
| **Seguretat del pla de control** | HTTPS + atestació | HTTPS + equivalent opcional de Tailnet Lock | ⚠️ Tailscale és lleugerament més robust |
| **Traça d'auditoria** | Registres complets | Registres bàsics | ⚠️ Tailscale és superior |
| **Programa de recompenses per errors** | ✅ Sí | ❌ No | Tailscale ha pagat investigadors de seguretat |
| **Certificacions de seguretat** | SOC 2 tipus II | No aplicable | Tailscale està preparat per a entorns empresarials |

### Consideracions sobre la privadesa

| Aspecte de privadesa | Tailscale | Headscale |
|----------------|-----------|-----------|
| **Visibilitat de les metadades** | Tailscale pot veure els noms dels dispositius, les adreces IP i les metadades de connexió | Tu controles totes les metadades |
| **Visibilitat del trànsit** | ❌ No pot veure el trànsit (xifrat) | ❌ No pot veure el trànsit (xifrat) |
| **Requisits de compliment normatiu** | Subjecte a la jurisdicció dels Estats Units | Subjecte a la jurisdicció del teu servidor |
| **Residència de les dades** | Infraestructura al núvol de Tailscale | El centre de dades que triïs |

**Veredicte:** Totes dues solucions ofereixen **un xifratge excel·lent i una arquitectura de coneixement zero** per al trànsit pròpiament dit. Headscale ofereix més **privadesa** perquè controles totes les metadades. Tailscale ofereix més **garanties de seguretat** gràcies a les certificacions, les auditories i les recompenses per errors.

______

## Comparació de la configuració i el desplegament

### Com configurar Tailscale

**Temps necessari:** 5-10 minuts

1. **Crea un compte** a [tailscale.com](https://tailscale.com/)
2. **Instal·la el client** a cada dispositiu (amb una ordre o baixant l'aplicació)
3. **Autentica't** amb OAuth (Google, Microsoft, GitHub, etc.)
4. **Configura les ACL** (opcional, ho pots fer més endavant)
5. **Fet!** La xarxa funciona immediatament

**Exemple d'instal·lació (Linux):**

> **Revisa l'instal·lador abans d'executar-lo.** Baixa'l en un fitxer temporal, inspecciona'l i confirma la distribució del sistema i l'origen del paquet. Després de la instal·lació, executa `tailscale version` i `tailscale status` per verificar el resultat. Si la instal·lació falla, elimina el paquet amb el gestor de paquets de la teva distribució i restaura l'estat anterior del paquet a partir de la còpia de seguretat del sistema.

```bash
curl -fsSL https://tailscale.com/install.sh -o /tmp/tailscale-install.sh
less /tmp/tailscale-install.sh
sh /tmp/tailscale-install.sh
sudo tailscale up
```

### Com configurar Headscale

**Temps necessari:** 30-90 minuts (la primera vegada)

1. **Prepara el servidor** (es recomana un VPS amb IP pública i 1 GB de RAM o més)
2. **Configura el DNS** (un registre A que apunti al servidor)
3. **Instal·la Headscale** (amb el gestor de paquets o Docker)
4. **Configura Headscale** (config.yaml amb l'URL del servidor, la base de dades, etc.)
5. **Configura els certificats TLS** (es recomana Let's Encrypt)
6. **Inicia el servei de Headscale**
7. **Crea usuaris** amb la CLI: `headscale users create alice`
8. **Instal·la el client de Tailscale** a cada dispositiu
9. **Configura els clients** perquè facin servir el servidor de coordinació personalitzat
10. **Registra els nodes** amb autenticació web o claus de preautenticació
11. **Configura les ACL** (fitxer policy.json)

**Exemple d'instal·lació de Headscale (Ubuntu):**
```bash
# Instal·la Headscale
curl -fsSL https://pkgs.headscale.net/headscale_<VERSION>_linux_amd64.deb -o headscale.deb
sudo apt install ./headscale.deb

# Configura Headscale
sudo nano /etc/headscale/config.yaml
# Defineix server_url com https://headscale.example.com

# Inicia el servei
sudo systemctl enable --now headscale

# Crea un usuari
headscale users create myuser

# Al dispositiu client
sudo tailscale up --login-server=https://headscale.example.com
```

**Opció més fàcil de configurar:** La configuració inicial és molt més senzilla amb **Tailscale**.

______

## Complexitat operativa

### Gestió diària

| Tasca | Tailscale | Headscale | Guanyador |
|------|-----------|-----------|--------|
| **Afegir un dispositiu nou** | Fes clic a l'enllaç i autentica't | Genera una clau d'autenticació o autentica't al web | Tailscale (més fàcil) |
| **Actualitzar les ACL** | Edita-les a la interfície web i els canvis s'apliquen a l'instant | Edita el fitxer i torna a carregar la configuració | Tailscale (més fàcil) |
| **Consultar l'estat de la connectivitat** | Tauler web | CLI o interfície de la comunitat | Tailscale (més fàcil) |
| **Diagnosticar i resoldre incidències** | Registres detallats al tauler | Registres del servidor i del client | Tailscale (més fàcil) |
| **Actualitzar el programari** | Actualitzacions automàtiques | Actualitzacions manuals del servidor | Tailscale (més fàcil) |
| **Fer còpies de seguretat de la configuració** | Automàtiques | Manuals (base de dades i configuració) | Tailscale (més fàcil) |
| **Recuperar-se d'un desastre** | Recuperació automàtica | Restauració manual des d'una còpia de seguretat | Tailscale (més fàcil) |

### Feina de manteniment

**Tailscale (servei gestionat):**
- ✅ Cap manteniment del servidor
- ✅ Actualitzacions i pedaços de seguretat automàtics
- ✅ Redundància i commutació en cas de fallada integrades
- ✅ Assistència professional disponible
- ❌ Dependència de la disponibilitat del servei de Tailscale

**Headscale (allotjament propi):**
- ⚠️ Actualitzacions del sistema operatiu del servidor i pedaços de seguretat (cada mes)
- ⚠️ Actualitzacions del programari de Headscale (cada 1-3 mesos)
- ⚠️ Còpies de seguretat de la base de dades (es recomana fer-ne cada dia)
- ⚠️ Renovació dels certificats TLS (automatitzada amb Let's Encrypt)
- ⚠️ Configuració del monitoratge i les alertes
- ⚠️ Diagnòstic i resolució d'incidències
- ✅ Control total de la infraestructura
- ✅ Cap dependència de serveis de tercers

**Temps mensual estimat:**
- **Tailscale:** 30 minuts (revisar polítiques i afegir usuaris)
- **Headscale:** 2-5 hores (actualitzacions, monitoratge i resolució d'incidències)

______

## Recomanacions segons el cas d'ús

### Tria Tailscale si:

✅ **Vols la configuració més ràpida** - 5 minuts des de la creació del compte fins a tenir la xarxa operativa\
✅ **Tens menys de 100 dispositius** - El pla gratuït cobreix l'ús personal i el de les empreses petites\
✅ **Prioritzes la facilitat d'ús** - Interfície web i experiència d'usuari de primer nivell\
✅ **Necessites funcions empresarials** - SSO, registres d'auditoria, Tailnet Lock i comprovacions de l'estat de seguretat dels dispositius\
✅ **Valores el teu temps** - Cap feina de manteniment i actualitzacions automàtiques\
✅ **Necessites disponibilitat garantida** - Tailscale ofereix un SLA del 99,99% de disponibilitat (Enterprise)\
✅ **Vols aplicacions mòbils oficials** - Aplicacions natives per a iOS i Android amb totes les funcions\
✅ **Necessites assistència professional** - Els plans de pagament inclouen assistència prioritària\
✅ **Dones importància al compliment normatiu** - Certificació SOC 2 tipus II\
✅ **Ets una entitat comercial** - Preus senzills per usuari i sense costos ocults\

### Tria Headscale si:

✅ **Necessites plena sobirania sobre les dades** - Totes les metadades es queden a la teva infraestructura\
✅ **Tens restriccions de privadesa o de compliment normatiu** - Les dades han de romandre en jurisdiccions concretes\
✅ **Tens coneixements tècnics** - Et mous amb facilitat en l'administració de sistemes Linux, el treball amb Docker i la resolució d'incidències\
✅ **Tens més de 10 usuaris de pagament** - L'estalvi esdevé significatiu a mesura que augmenta l'escala\
✅ **Vols aprendre** - És un bon projecte per entendre com funcionen les VPN de malla\
✅ **Prefereixes el codi obert** - Pots auditar el codi, contribuir-hi amb correccions i personalitzar-lo\
✅ **Vigiles el pressupost** - Costos recurrents mínims ($5-30 al mes pel servidor)\
✅ **Ja tens infraestructura** - El pots desplegar en una infraestructura de Kubernetes o de màquines virtuals existent\
✅ **Necessites una API gRPC** - Headscale ofereix gRPC per a l'automatització avançada\
✅ **Ja allotges els teus serveis** - Encaixa amb el teu ecosistema d'allotjament propi\

### Enfocament híbrid: fes servir totes dues opcions

Algunes organitzacions fan servir **totes dues solucions**:

1. **Tailscale per a producció** - Infraestructura crítica amb SLA i assistència
2. **Headscale per al desenvolupament i les proves** - Entorns de desenvolupament de baix cost
3. **Tailscale per a usuaris sense perfil tècnic** - Incorporació senzilla del personal
4. **Headscale per als equips tècnics** - Personal d'enginyeria familiaritzat amb l'allotjament propi

______

## Escenaris de migració

### Migrar de Tailscale a Headscale

**Motivació:** Reduir costos, guanyar sobirania sobre les dades i augmentar el control

**Procés:**
1. Desplega el servidor de Headscale i comprova que funcioni
2. Prova Headscale amb un subconjunt de dispositius no crítics
3. Exporta les ACL de Tailscale i adapta-les a Headscale
4. Migra els dispositius gradualment al servidor de coordinació de Headscale
5. Actualitza la configuració DNS i les rutes de subxarxa
6. Cancel·la la subscripció a Tailscale

**Reptes:**
- No hi ha cap eina de migració automatitzada
- Cal tornar a autenticar tots els dispositius
- Algunes funcions (Funnel, Serve, Taildrop) no funcionaran de la mateixa manera
- La sintaxi de les ACL és compatible, però cal provar-la

**Temps necessari:** 5-20 hores, segons la complexitat

### Migrar de Headscale a Tailscale

**Motivació:** Reduir la feina operativa, obtenir funcions empresarials i disposar de més assistència

**Procés:**
1. Crea un compte de Tailscale i configura les ACL
2. Instal·la els clients de Tailscale (poden substituir els clients existents si són al mateix dispositiu)
3. Migra els dispositius executant `tailscale up` sense indicar-hi un servidor personalitzat
4. Verifica la connectivitat i els controls d'accés
5. Retira el servidor de Headscale

**Reptes:**
- Cal tornar a autenticar tots els dispositius
- Alguns usuaris podrien necessitar comptes de Tailscale (correu electrònic o SSO)
- Cal gestionar el canvi i comunicar-lo als usuaris

**Temps necessari:** 2-8 hores, segons la mida del desplegament

______

## Comunitat i ecosistema

### Ecosistema de Tailscale

| Recurs | Disponibilitat |
|----------|--------------|
| **Documentació oficial** | ✅ Completa i ben mantinguda |
| **Fòrum de la comunitat** | ✅ Fòrum actiu amb participació del personal de Tailscale |
| **Servidor de Discord** | ✅ Molt actiu, amb personal que respon |
| **Incidències a GitHub** | ❌ Codi tancat (les aportacions es fan al fòrum) |
| **Stack Overflow** | ✅ Etiqueta activa amb més de 2.000 preguntes |
| **Tutorials de YouTube** | ✅ Contingut oficial i de la comunitat |
| **Integracions** | ✅ Docker, Kubernetes, Terraform, Synology, QNAP, etc. |

### Ecosistema de Headscale

| Recurs | Disponibilitat |
|----------|--------------|
| **Documentació oficial** | ✅ Bona, mantinguda per la comunitat |
| **Fòrum de la comunitat** | ⚠️ GitHub Discussions fa de fòrum |
| **Servidor de Discord** | ✅ Servidor actiu de la comunitat |
| **Incidències a GitHub** | ✅ Codi obert, seguiment actiu d'incidències (més de 38.900 estrelles) |
| **Stack Overflow** | ⚠️ Comunitat més petita (unes 100 preguntes) |
| **Tutorials de YouTube** | ⚠️ Contingut creat per la comunitat |
| **Interfícies web** | ⚠️ Diverses opcions de la comunitat (Headscale-UI, Headplane, ouroboros) |
| **Operador de Kubernetes** | ⚠️ Operador mantingut per la comunitat |

**Mida de la comunitat (2026):**
- **Tailscale:** Més de 100.000 membres actius a la comunitat, amb el suport d'una empresa ben finançada
- **Headscale:** Més de 10.000 membres actius a la comunitat, projecte de codi obert

______

## Proves de rendiment en condicions reals (2026)

A partir de les proves de la comunitat i de les proves comparatives publicades:

### Proves de taxa de transferència (entre iguals)

| Escenari | Tailscale | Headscale | Referència (sense VPN) |
|----------|-----------|-----------|-------------------|
| **LAN d'1 Gbps** | 940 Mbps | 940 Mbps | 945 Mbps |
| **WAN (100 Mbps)** | 98 Mbps | 98 Mbps | 100 Mbps |
| **WAN (fibra d'1 Gbps)** | 920 Mbps | 920 Mbps | 950 Mbps |
| **Entre continents (DERP)** | 180 Mbps | 95 Mbps | No aplicable |

**Anàlisi:** Les connexions directes entre iguals tenen un rendiment idèntic. Tailscale obté millors resultats en les connexions retransmeses gràcies a la infraestructura mundial de la seva xarxa DERP.

### Proves de latència

| Escenari | Tailscale | Headscale | Referència |
|----------|-----------|-----------|----------|
| **Ping a la LAN** | 1,2 ms | 1,2 ms | 0,8 ms |
| **WAN regional (100 milles)** | 15 ms | 15 ms | 12 ms |
| **D'un extrem a l'altre del país** | 48 ms | 48 ms | 45 ms |
| **Entre continents (connexió directa)** | 155 ms | 155 ms | 152 ms |
| **Entre continents (DERP)** | 185 ms | 220 ms | No aplicable |

**Anàlisi:** Tots dos afegeixen una latència mínima (d'uns 1-2 ms) a les connexions directes. La latència del DERP de Headscale varia segons la ubicació del servidor.

### Ús de recursos

| Mètrica | Client de Tailscale | Client de Headscale | Servidor de Headscale |
|--------|------------------|------------------|------------------|
| **Ús de RAM (en repòs)** | 80-120 MB | 80-120 MB | 50-200 MB (varia segons el nombre de nodes) |
| **Ús de RAM (en activitat)** | 120-200 MB | 120-200 MB | 100-500 MB |
| **Ús de CPU (en repòs)** | <1% | <1% | <1% |
| **Ús de CPU (en activitat)** | 5-15% | 5-15% | 3-20% (depèn del nombre de nodes) |
| **Ús de disc** | 100-500 MB | 100-500 MB | 100 MB-2 GB (base de dades) |

______

## Exemples de configuració avançada

### Headscale amb Docker Compose

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

### Exemple d'ACL de Headscale

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

### Configuració del client de Tailscale (amb Headscale)

```bash
# Linux
sudo tailscale up \
  --login-server=https://headscale.example.com \
  --accept-routes \
  --advertise-tags=tag:server

# Amb una clau de preautenticació
headscale preauthkeys create --user engineering --expiration 1h

sudo tailscale up \
  --login-server=https://headscale.example.com \
  --authkey=<YOUR_AUTH_KEY>
```

______

## Resolució d'incidències habituals

### Incidències de Tailscale

| Problema | Solució |
|---------|----------|
| **No es pot connectar al servidor de coordinació** | Revisa el tallafoc i comprova la connexió a internet |
| **La connexió directa falla** | Normalment passa a fer servir DERP automàticament. Revisa la configuració de NAT |
| **Latència alta** | Comprova que s'hagi establert una connexió directa (sense retransmissió) |
| **La clau ha caducat** | Torna a autenticar-te o desactiva la caducitat de les claus a la consola d'administració |
| **Una ACL bloqueja el trànsit** | Revisa les regles de les ACL i prova la configuració |

### Incidències de Headscale

| Problema | Solució |
|---------|----------|
| **Els nodes no es registren** | Comprova que es pugui accedir a l'URL de Headscale i revisa el certificat TLS |
| **La resolució DNS falla** | Comprova que MagicDNS estigui ben configurat a config.yaml |
| **El retransmissor DERP no funciona** | Comprova que el port STUN (3478/udp) estigui obert i revisa la configuració de DERP |
| **Els nodes queden fora de línia després de reiniciar** | Comprova que els clients estiguin configurats per executar-se a l'inici del sistema |
| **Els canvis de les ACL no s'apliquen** | Torna a carregar Headscale amb `systemctl reload headscale` |
| **La base de dades s'ha corromput** | Restaura-la a partir d'una còpia de seguretat i valora fer servir PostgreSQL en producció |

### Ordres de diagnòstic

```bash
# Diagnòstics de Tailscale
tailscale status
tailscale netcheck
tailscale ping <hostname>
tailscale debug derp

# Diagnòstics de Headscale
headscale nodes list
headscale nodes list-routes
headscale debug routes
journalctl -u headscale -f  # Mostra els registres
```

______

## Bones pràctiques de seguretat

### Per a totes dues solucions

1. **Activa la caducitat de les claus** - Obliga els usuaris a tornar-se a autenticar periòdicament
2. **Aplica el principi del mínim privilegi** - Concedeix només els permisos d'accés necessaris a les ACL
3. **Etiqueta els nodes d'infraestructura** - Separa els dispositius dels usuaris dels servidors
4. **Activa l'MFA** - Exigeix autenticació multifactor quan els usuaris iniciïn sessió
5. **Supervisa els registres d'accés** - Revisa regularment els patrons de connexió
6. **Mantén els clients actualitzats** - Aplica els pedaços de seguretat de seguida

### Seguretat específica de Headscale

1. **Reforça el sistema operatiu del servidor** - Segueix les guies CIS Benchmarks i desactiva els serveis innecessaris
2. **Fes servir Let's Encrypt** - Automatitza la gestió dels certificats TLS
3. **Implementa fail2ban** - Evita els intents d'accés per força bruta
4. **Fes còpies de seguretat periòdiques** - Automatitza les còpies de seguretat de la base de dades i desa-les en una ubicació separada
5. **Actualitza de seguida** - Fes el seguiment de les versions de Headscale per detectar pedaços de seguretat
6. **Segmenta la xarxa** - Aïlla el servidor de Headscale en una VLAN de gestió
7. **Activa el tallafoc** - Exposa només els ports necessaris (443, 3478/udp)

______

## Full de ruta i desenvolupament futur

### Full de ruta de Tailscale (2026)

Segons les declaracions públiques de Tailscale:
- ✅ **Publicat:** Aperture (passarel·la de governança de la IA) i millores en les comprovacions de l'estat de seguretat dels dispositius
- 🚧 **En desenvolupament:** Detecció avançada d'amenaces i compatibilitat amb més plataformes
- 📋 **Planificat:** Mode només IPv6, millores d'observabilitat i més integracions

### Estat de Headscale (2026)

Segons les fites a GitHub i els debats de la comunitat:
- ✅ **Afegit recentment:** Autenticació OIDC, millores a DERP i més compatibilitat amb ACL
- 🚧 **En desenvolupament:** Millores a Taildrop i millor integració amb la interfície web
- 📋 **Peticions de la comunitat:** Un equivalent de Funnel/Serve, registres avançats i mode d'alta disponibilitat

**Avaluació de la maduresa:**
- **Tailscale:** Apte per a producció, preparat per a entorns empresarials i amb 5 anys o més de desenvolupament
- **Headscale:** Apte per a producció en casos d'ús bàsics, amb desenvolupament actiu i impulsat per la comunitat

______

## Conclusió

Tant **Tailscale** com **Headscale** ofereixen funcions excel·lents de VPN de malla basada en WireGuard, però s'adrecen a públics i casos d'ús diferents.

**Tria Tailscale si:**
- Valores la simplicitat i vols començar a treballar en pocs minuts
- Formes part d'un equip petit (menys de 100 dispositius) que es pot beneficiar del pla gratuït generós
- Necessites funcions empresarials com l'SSO, els registres d'auditoria i l'assistència professional
- Prefereixes els serveis gestionats a l'allotjament propi
- Dones importància a les certificacions de compliment normatiu (SOC 2)

**Tria Headscale si:**
- Necessites un control total de la infraestructura i les metadades
- Tens coneixements tècnics i t'agrada allotjar els teus serveis
- Optimitzar els costos és essencial (més de 10 usuaris de pagament = estalvi significatiu)
- La sobirania sobre les dades i la privadesa són prioritàries
- Prefereixes solucions de codi obert que puguis auditar i personalitzar

**Recomanacions principals per al 2026:**

1. **Empreses emergents i pimes:** Comença amb el **pla gratuït de Tailscale**. És imbatible per a 0-100 dispositius.
2. **Equips informàtics d'empresa:** **Tailscale Enterprise** amb SSO i assistència ofereix el millor cost total de propietat si tens en compte el temps del personal.
3. **Usuaris que prioritzen la privadesa:** **Headscale** ofereix el màxim control i privadesa.
4. **Usuaris de laboratoris domèstics amb coneixements tècnics:** **Headscale** és una oportunitat excel·lent per aprendre.
5. **Organitzacions amb un enfocament híbrid:** Fes servir **Tailscale per a producció** i **Headscale per al desenvolupament i les proves**.

Triïs l'opció que triïs, faràs servir la tecnologia WireGuard, de primer nivell per a xarxes segures i modernes. La tria depèn del pes que donis a cada parell de prioritats: **comoditat o control**, **servei gestionat o allotjament propi**, i **cost o funcions**.

Per a la majoria d'organitzacions el 2026, el **servei gestionat de Tailscale** ofereix el millor equilibri entre funcions, facilitat d'ús i relació qualitat-preu. Per a les organitzacions amb requisits específics de sobirania sobre les dades, privadesa o cost, **Headscale ofereix una alternativa atractiva amb allotjament propi**.

______

## Referències i recursos

1. [Lloc web oficial de Tailscale](https://tailscale.com/)
2. [Documentació de Tailscale](https://tailscale.com/kb/)
3. [Documentació oficial de Headscale](https://headscale.net/)
4. [Repositori de Headscale a GitHub](https://github.com/juanfont/headscale)
5. [Lloc web oficial de WireGuard](https://www.wireguard.com/)
6. [Blog de Tailscale - Com funciona Tailscale](https://tailscale.com/blog/how-tailscale-works/)
7. [Arquitectura de confiança zero del NIST](https://csrc.nist.gov/publications/detail/sp/800-207/final)
8. [Llibre blanc tècnic de WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
