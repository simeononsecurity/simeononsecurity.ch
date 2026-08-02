---
title: "Flock Finder: Mapa de càmeres ALPR de Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder és una eina de codi obert que mapeja més de 40.000 càmeres Flock Safety ALPR arreu del món utilitzant dades WiFi de WiGLE i empremta OUI. Aprèn com funciona, les seves limitacions i les eines de maquinari per a la detecció en temps real."
genre: ["Tecnologia de privacitat", "Contravigil·lància", "Projectes de codi obert", "Drets digitals", "Seguretat de xarxes", "Eines de privacitat", "Pirateria de maquinari", "Recerca de seguretat"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Lector de matrícules", "Empremta OUI", "WiGLE", "Vigilància WiFi", "Contravigil·lància", "STS Collective", "FlockYou", "ESP32", "Eines de privacitat", "NitekryDPaul", "DeFlockJoplin", "Detecció ALPR", "Seguretat de codi obert", "Mapeig de vigilància", "Vigilància massiva", "WiFi OUI", "Protecció de la privacitat", "Adreça MAC", "Mode promiscu", "802.11", "Detecció en temps real", "Wardriving", "Drets digitals", "Llibertats civils", "Consciència de vigilància", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Un mapa interactiu que mostra marcadors de colors que indiquen les ubicacions de les càmeres Flock Safety ALPR, amb senyals WiFi abstractes emanant dels marcadors sobre un fons fosc."
coverCaption: "Flock Finder mapeja més de 40.000 presumptes càmeres Flock Safety ALPR utilitzant dades WiFi de WiGLE i empremta OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Una eina de consciència sobre la vigilància de codi obert que mapeja les càmeres Flock Safety ALPR utilitzant dades WiFi de col·laboració ciutadana.**

## Què és Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** és un projecte de codi obert que mapeja les **càmeres Flock Safety ALPR (Lector Automàtic de Matrícules)** als Estats Units i en 108 altres països. Combina **31 prefixos OUI (Identificador Únic Organitzacional) WiFi de Flock Safety coneguts** amb la **base de dades WiFi col·laborativa WiGLE** per identificar i representar les ubicacions de càmeres sospitoses en un mapa interactiu.

El projecte es troba a **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, s'actualitza automàticament cada dia mitjançant GitHub Actions i, a partir del juliol de 2026, ha mapejat **més de 40.000 càmeres sospitoses** en 964 regions d'arreu del món.

| Mètrica | Valor |
|--------|-------|
| **Càmeres mapejades** | 40.026+ |
| **Prefixos OUI coneguts** | 31 |
| **Països coberts** | 109 |
| **Regions cobertes** | 964 |
| **Retenció de dades** | 730 dies (2 anys) |
| **Freqüència d'actualització automàtica** | Diàriament |

*Aquesta és una eina de consciència general, no un inventari definitiu. Llegiu la secció de limitacions abans de treure conclusions de les dades.*

Per obtenir context sobre per què la vigilància ALPR de Flock Safety és important per a la privacitat, llegiu **[Vigilància de càmeres Flock Safety: Prevalença, preocupacions de privacitat i estratègies de protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## Com funciona: Empremta OUI via WiGLE

### La idea central

Les càmeres Flock Safety contenen **transceivers WiFi** que es desperten periòdicament del son per pujar les dades de matrícula capturades al núvol. Durant aquestes breus finestres actives, la càmera emet trames WiFi que contenen la seva **adreça MAC** — i els primers tres bytes de cada adreça MAC identifiquen el fabricant. Això és l'**OUI (Identificador Únic Organitzacional)**.

L'investigador de seguretat **@NitekryDPaul** va descobrir **30 prefixos OUI** consistentment associats amb el maquinari de les càmeres Flock Safety mitjançant **anàlisi 2,4 GHz en mode promiscu**. Un 31è prefix (`82:6B:F2`) va ser aportat per **Michael / DeFlockJoplin** durant les proves de camp a Joplin, MO.

Flock Finder agafa aquests 31 OUIs, consulta WiGLE per a qualsevol xarxa WiFi registrada que coincideixi amb aquests prefixos i representa els resultats en un mapa.

### Els 31 prefixos OUI coneguts de Flock Safety

| # | Prefix OUI | Font | # | Prefix OUI | Font |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### La tècnica de detecció addr1

El descobriment clau de @NitekryDPaul va més enllà de simplement fer coincidir l'adreça MAC del transmissor. Les càmeres Flock passen la major part del seu cicle de treball **dormides**. Quan un punt d'accés proper envia una trama dirigida *a* una càmera, la MAC de la càmera apareix com **addr1 (l'adreça del receptor)** a les trames 802.11 — fins i tot mentre la pròpia càmera no transmet activament.

Combinat amb la **detecció de sol·licituds de sonda wildcard** (trames de gestió 802.11 type=0, subtype=4, SSID buit), això dona una signatura de detecció molt precisa. Les proves de camp a Joplin, MO van aconseguir **11 de 12 càmeres detectades amb només 2 falsos positius**.

> ⚠️ **Important**: El mapa Flock Finder basat en WiGLE **no** implementa la tècnica addr1. WiGLE és un conjunt de dades històriques, recopilades passivament — només registra transmissors, no receptors. Per a la detecció en temps real que realment utilitza el mètode de @NitekryDPaul, necessiteu maquinari dedicat funcionant al camp.

______

## Ús del mapa en viu

El mapa interactiu és accessible a **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Mostra:

- **Marcadors de càmeres agrupats** codificats per color per prefix OUI
- **Cerca** per ciutat, estat o BSSID
- **Taula de dades OUI** amb comptadors de càmeres per prefix
- **Panell d'estadístiques** que mostra el total de càmeres, regions i l'última marca de temps d'actualització
- **Pàgina sobre ALPRs** amb danys de privacitat documentats, context legal i recursos comunitaris

Les exportacions de dades del mapa també estan disponibles directament:

- `data/flock_cameras.geojson` — GeoJSON per a ús en QGIS, Leaflet o altres eines
- `data/flock_cameras.csv` — format compatible amb fulls de càlcul
- `data/scan_stats.json` — estadístiques i comptadors d'escaneig

### Limitacions clau

**Preneu el mapa amb precaució.** WiGLE és un conjunt de dades col·laboratiu i actualitzat esporàdicament, no una transmissió en directe.

- **Les càmeres Flock no transmeten contínuament.** Es desperten breument per pujar dades, de manera que els registres de WiGLE depenen completament que un conductor de wardriving estigui a prop exactament en el moment adequat.
- **Les dades poden tenir mesos o anys d'antiguitat.** Les càmeres que han estat traslladades o eliminades encara poden aparèixer.
- **La coincidència OUI és una heurística.** Els OUIs es poden compartir, reassignar o falsificar. Cada resultat és un dispositiu Flock *sospitós*, no confirmat.
- **La cobertura és desigual.** Les àrees metropolitanes denses tenen més dades de WiGLE; les zones rurals en tenen molt menys.

*Utilitzeu el mapa per desenvolupar una consciència general de la densitat de vigilància a la vostra àrea. Per a la detecció en temps real amb dades sobre el terreny, vegeu les opcions de maquinari a continuació.*

______

## Executar Flock Finder vosaltres mateixos

### Requisits previs

- Python 3.8+
- Un compte gratuït de [WiGLE](https://wigle.net/account) amb credencials API

### Configuració

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### Execució de l'escàner

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### Visualització del mapa localment

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### Actualitzacions diàries automatitzades via GitHub Actions

Feu un fork del repositori i afegiu les vostres credencials de WiGLE com a **secrets del repositori** (`WIGLE_API_NAME` i `WIGLE_API_TOKEN`). El flux de treball inclòs s'executa a les 6 AM UTC diàriament i confirma automàticament els fitxers de dades actualitzats sempre que es troben noves càmeres.

______

## Detecció en temps real: Maquinari STS Collective FlockYou

El mapa de WiGLE us diu on s'han *observat* les càmeres. Per a la detecció en temps real mentre conduïu — utilitzant el mètode real de coincidència OUI de @NitekryDPaul sobre trànsit WiFi en directe — necessiteu maquinari dedicat.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** fabrica detectors portàtils basats en ESP32 que escanegen les signatures OUI de Flock i us alerten en el moment en què es detecta una signatura coincident.

### Gamma de dispositius FlockYou

| Dispositiu | Descripció |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Detector Flock compacte, de mida de butxaca. Pre-flashejat, plug-and-play. Alertes LED en la detecció. |
| **FlockYou Pro — LED + Audio** | Afegeix alertes d'àudio juntament amb indicadors LED. No us perdeu mai una càmera mentre conduïu. |
| **FlockYou Atom VoiceS3R** | Detector amb veu amb alertes d'àudio parlades per a una operació de mans lliures amb els ulls a la carretera. |

Tots els dispositius:
- **Pre-flashejats**, llestos per utilitzar directament de la caixa
- Escanegen el trànsit WiFi en viu per als 31 OUIs de Flock coneguts
- Compactes i portàtils — cap en un portavases o una butxaca
- Alimentats via USB-C (adaptador de cotxe, bateria externa o portàtil)

> 💰 **Descomptes exclusius**: Utilitzeu el codi **FLOCKFINDER** per a un **20% de descompte** en tots els dispositius STS Collective FlockYou — o utilitzeu el codi **SIMEONONSECURITY** per a un descompte de fins al 20% en tota la vostra comanda. [Compreu a stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Per a una anàlisi tècnica completa d'aquests dispositius i alternatives DIY, llegiu la **[Guia completa de maquinari i configuració del Projecte de Detecció Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Estructura del projecte

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## Preguntes freqüents

### És legal?

Sí. **Flock Finder utilitza únicament dades disponibles públicament** de la base de dades de WiGLE, que agrega dades d'enquesta WiFi contribuïdes voluntàriament. No hi ha hacking, accés no autoritzat ni sistemes propietaris implicats. El monitoratge WiFi passiu per a signatures OUI és legal als Estats Units.

### Totes les càmeres mapejades són definitivament càmeres Flock?

No. La coincidència OUI és una **heurística**. Els prefixos OUI es poden compartir entre fabricants, reassignar o falsificar. Cada registre a la base de dades és un dispositiu Flock *sospitós* — no confirmat. Llegiu la [Política de dades](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) per a detalls sobre com sol·licitar una correcció.

### Per què alguns prefixos OUI no mostren cap càmera?

La cobertura de WiGLE és desigual. Si cap conductor de wardriving ha escanejat una àrea determinada amb aquell OUI específic actiu, no hi haurà registres. *L'absència de dades no significa l'absència de càmeres.*

### Quant de temps fa que les dades?

El flux de treball de GitHub Actions s'executa diàriament i obté els últims resultats de WiGLE. No obstant això, WiGLE en si pot tenir registres que van des de dies fins a anys d'antiguitat per a qualsevol ubicació determinada. Comproveu el fitxer `scan_stats.json` per a la marca de temps de l'exploració més recent.

### Puc contribuir amb les meves pròpies dades de wardrive?

Sí. Pengeu les vostres dades de wardrive a [WiGLE](https://wigle.net) — s'incorpora automàticament a la propera exploració diària de Flock Finder. També podeu contribuir amb prefixos OUI o millores de codi mitjançant la [Guia de contribució](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Comunitat i projectes relacionats

Flock Finder no actua sol. Un ecosistema creixent d'eines i organitzacions treballa per documentar i combatre la vigilància ALPR:

- **[DeFlock.org](https://deflockjoplin.org/)** — Seguiment, documentació i defensa d'ALPR impulsats per la comunitat
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Comproveu si la vostra matrícula ha estat cercada al sistema de Flock
- **[FlockHopper](https://flockhopper.com/)** — Planificació de rutes que evita les càmeres ALPR conegudes
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Base de dades de l'EFF sobre tecnologia de vigilància utilitzada per les forces de l'ordre
- **[NoALPRs.com](https://noalprs.com/)** — Recursos per a comunitats que lluiten contra els desplegaments d'ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Firmware de codi obert i recerca de camp; va contribuir amb el 31è prefix OUI

______

## Crèdits

- **Recerca OUI**: @NitekryDPaul — tots els 30 prefixos OUI originals i l'estratègia de detecció addr1/mode promiscu
- **Proves de camp**: Michael / DeFlockJoplin — 31è prefix OUI (`82:6B:F2`) i ajust de sonda wildcard
- **Font de dades**: [WiGLE](https://wigle.net) — base de dades WiFi/xarxa cel·lular de col·laboració ciutadana
- **Inspirat per**: [DeFlock](https://deflockjoplin.org/) i track-openroaming-passpoint
- **Soci de maquinari**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — detectors FlockYou ESP32

______

## Conclusió

**Flock Finder** dóna a qualsevol persona una idea ràpida i visual de fins a quin punt s'han desplegat les càmeres Flock Safety ALPR — més de 40.000 ubicacions estimades en 109 països, actualitzades automàticament cada dia a partir de dades WiFi de col·laboració ciutadana.

És una **eina de transparència**, no un rastrejador en directe. Les seves dades són històriques, incompletes i probabilístiques. Però fa visible l'escala de la vigilància ALPR d'una manera que els resums i els informes no poden.

Per a una protecció genuïna en temps real mentre us moveu per zones vigilades, combineu el mapa amb maquinari dedicat. **[Els dispositius FlockYou de STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implementen el mètode de detecció de @NitekryDPaul directament en un ESP32 i us alerten en el moment en què es detecta una signatura de càmera en viu — disponibles a **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** amb el codi **FLOCKFINDER** o **SIMEONONSECURITY** per a un descompte de fins al 20%.

### Articles relacionats

| Article | Què cobreix |
|---------|---------------|
| **[Vigilància de càmeres Flock Safety: Privacitat i protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | El quadre complet: estadístiques de prevalença, qüestions de llibertats civils, kit d'eines ACLU, estadístiques DeFlock, guia FOIA i estratègies de protecció |
| **[Projecte de Detecció Flock-You: Guia de maquinari de contravigil·lància](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guia tècnica completa dels detectors Flock basats en ESP32 — OUI-SPY, M5 Atom Lite, construcció DIY, configuració de firmware pas a pas |
| **[Com flashejar dispositius Rayhunter: Guia completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detectar captadors IMSI (simuladors de llocs cel·lulars) al costat de càmeres ALPR per a una consciència completa de contravigil·lància |
| **[Firmware personalitzat DagShell per a Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Convertir un punt d'accés mòbil en una plataforma de recerca de seguretat — s'integra bé amb el maquinari de detecció Flock |
| **[Comparació de dispositius Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparar opcions de maquinari de detecció entre categories de threats ALPR i de vigilància cel·lular |

______

## Referències

1. [Repositori GitHub de Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Mapa interactiu de Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — Dispositius FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Mapeig de xarxes sense fil](https://wigle.net)
5. [DeFlock — Consciència comunitària d'ALPR](https://deflockjoplin.org/)
6. [DeFlockJoplin — Firmware de detecció de codi obert](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Esteu sent rastrejats](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
