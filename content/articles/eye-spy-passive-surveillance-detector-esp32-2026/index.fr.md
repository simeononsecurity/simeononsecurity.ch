---
title: "Eye Spy : détecteur passif de surveillance et de traceurs pour ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Référence technique d’Eye Spy v1.1, un détecteur passif BLE et WiFi sur ESP32 qui repère les caméras, traceurs, drones et signaux associés."
genre: ["Outils de confidentialité", "Contre-surveillance", "Sécurité IoT", "Systèmes embarqués", "Recherche en sécurité", "Sécurité WiFi", "Sécurité Bluetooth", "Projets ESP32", "Sécurité matérielle", "Sécurité open source"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Détection de surveillance", "Contre-surveillance", "Détection BLE", "Scan WiFi", "Détection AirTag", "Détection ALPR", "Flock Safety", "Détection de caméras-piétons", "Détection de drones", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Logiciel libre", "Confidentialité", "BLE passif", "Mode promiscuité", "Détection OUI", "Détection de traceurs", "Caméra-piéton Axon", "Ray-Ban Meta", "Samsung SmartTag", "Traceur Tile", "Caméra cachée", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Illustration d’un petit appareil M5Stack Atom Lite entouré d’ondes de signaux colorées sur un fond bleu nuit, représentant la détection de surveillance Bluetooth et WiFi."
coverCaption: ""
---

**Un capteur passif de la taille d’un pouce qui vous avertit lorsqu’un appareil vous observe**

## Introduction : le paysage de surveillance que vous ne voyez pas

Le monde physique est de plus en plus équipé d’appareils qui observent, enregistrent et suivent les personnes : lecteurs de plaques aux coins des rues, caméras-piétons des forces de l’ordre, caméras dans les logements loués, traceurs commerciaux semblables à des AirTag cachés dans des sacs ou des voitures et caméras de surveillance à chaque entrée de magasin. La plupart communiquent sans fil par **Bluetooth LE** ou **WiFi**. *La plupart de ces communications sont diffusées dans l’espace libre et peuvent être détectées par toute personne disposant du récepteur adapté.*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) est un outil passif de détection de surveillance qui exploite précisément ce fait. Exécuté sur le **M5Stack Atom Lite**, une carte de développement ESP32-PICO-D4 de la taille d’un morceau de sucre, Eye Spy surveille en continu les bandes BLE et WiFi à la recherche des signatures électroniques d’appareils d’enregistrement, de caméras de surveillance, de systèmes **ALPR** (automatic license plate reader), de drones et de traceurs personnels. Lorsqu’il détecte un signal, sa LED RVB change de couleur.

*Il ne se connecte à aucun appareil et n’émet rien.* Il observe, attribue un score et s’allume.

Cet article est une référence technique complète : appareils détectés, fonctionnement du modèle de score de confiance, conception des moteurs de détection, construction et flashage, et limites pratiques.

**Vous préférez ne pas en fabriquer un ?** Des **[détecteurs Eye Spy](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** préflashés et prêts à l’emploi sont disponibles chez STS Collective. Le code lecteur **SIMEONONSECURITY** donne jusqu’à 20 % de réduction.

{{< stscollective-ad "eyespy" >}}

---

## Voyants LED : toute l’interface utilisateur

Comme l’[ESP32 WiFi Canary (détecteur passif de menaces WiFi)](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), Eye Spy transmet toutes ses informations par un seul NeoPixel RVB SK6812 connecté à GPIO 27 du M5Stack Atom Lite. La LED affiche en permanence l’un des quatre niveaux de menace :

| Couleur | Signification | Plage du score |
|---------|---------------|----------------|
| 🔵 Pulsation bleue | Démarrage / premier scan | -- |
| 🟢 Vert fixe | Rien de détecté | 0–2 |
| 🟡 Jaune fixe | Prudence : appareil d’enregistrement possible à proximité | 3–5 |
| 🔴 Rouge clignotant | Alerte : appareil de surveillance ou de suivi détecté | 6+ |

**Une seule détection à forte confiance, par exemple une caméra-piéton Axon, une caméra Flock Safety, une correspondance OUI ALPR ou un AirTag, suffit à faire passer immédiatement la LED au rouge pendant un cycle.** Plusieurs détections de confiance moyenne s’additionnent jusqu’au jaune et peuvent atteindre le rouge.

---

## Matériel

### Cible principale : M5Stack Atom Lite

| Composant | Détail |
|-----------|--------|
| Carte | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | NeoPixel SK6812 sur GPIO 27 |
| Bouton | GPIO 39 (entrée uniquement) |
| Flash | 4 MB |

L’Atom Lite constitue une plateforme autonome. **Aucune soudure, plaque d’essai ou pièce externe n’est nécessaire.** Branchez-le en USB : il fonctionne.

### ESP32 DevKit générique

Un second environnement de compilation PlatformIO (`esp32dev`) prend en charge tout ESP32 DevKit standard équipé d’une LED intégrée sur GPIO 2. La logique de détection est identique. Cette version convient au développement, aux tests et aux déploiements qui n’exigent pas le format compact de l’Atom Lite.

---

## Le système de score

Eye Spy utilise un **modèle de score de confiance** qui regroupe les signaux de tous les moteurs de détection en un seul entier. Le score détermine l’état de la LED (vert, jaune ou rouge) et fait l’objet de deux mécanismes de gestion automatiques :

### Décroissance du score

Sans nouvelle détection, le score baisse de **1 point toutes les 60 secondes**. Si vous vous éloignez d’un appareil détecté, la LED repasse au vert en quelques minutes sans intervention.

### Délai avant un nouveau score

Chaque *type* de détection est soumis à un **délai de 120 secondes** avant qu’une même source puisse ajouter à nouveau des points pour ce type. *Un appareil persistant ne peut donc pas faire grimper le score indéfiniment.* Une caméra Flock Safety qui reste à portée ajoute +5 une fois, puis doit attendre 120 secondes avant de contribuer de nouveau.

Ces mécanismes impliquent que :

- **Les détections temporaires**, comme une voiture équipée d’un AirTag qui passe, se résolvent automatiquement.
- **Une surveillance persistante**, comme un déploiement fixe de caméras-piétons, maintient la LED en état d’alerte tant que vous restez à portée.
- **Un appareil détecté à répétition ne fait pas exploser le score.**

---

## Moteurs de détection

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Schéma des moteurs parallèles BLE et WiFi d’Eye Spy, qui recherchent AirTag, caméras-piétons, systèmes ALPR et drones, puis transmettent les signaux au modèle de menace fondé sur un score de confiance" >}}

Eye Spy alterne en continu entre trois phases de scan :

**BLE passif (9 s) → scan WiFi (~3 s) → capture promiscuité (5 s) → répétition**

Le BLE est explicitement arrêté avant toute opération WiFi afin de respecter le partage de la radio ESP32. Il redémarre au début du cycle suivant.

---

### Moteur 1 : scan BLE passif

Le scan BLE utilise **NimBLE sans transmettre de requêtes de scan**. L’appareil écoute les paquets publicitaires BLE sans répondre. *Eye Spy reste ainsi électroniquement invisible pour les appareils recherchés.* Un scanner passif ne peut pas être détecté par la cible.

Les appareils dont le signal est inférieur à **−90 dBm** sont ignorés pour réduire les faux positifs dans les environnements denses.

#### Tableau de détection BLE

| # | Cible | Méthode de détection | Points |
|---|-------|----------------------|-------|
| 1 | **Caméra-piéton Axon** | OUI MAC BLE `00:25:df` (Axon : caméras-piétons, pistolets à impulsion électrique et équipements des forces de l’ordre) | +5 🔴 |
| 2 | **Lunettes connectées Ray-Ban Meta** | UUID de service BLE `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE** | Nom d’appareil BLE contenant `Flock`, `Penguin`, `Pigvision` ou `FS Ext Battery` | +5 🔴 |
| 4 | **Skimmer de carte (HC-03/05/06)** | Correspondance exacte du nom BLE : modules Bluetooth courants dans les skimmers de terminaux de paiement | +5 🔴 |
| 5 | **Apple AirTag** | Sous-type fabricant `0x12`/`0x1E` de `0x004C`, ou charge utile brute `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Drone (OpenDroneID BLE)** | UUID de service BLE `0xFFFA` ou charge utile AD brute avec code d’application `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID de service BLE `0xFD5A` | +3 🟡 |
| 8 | **Traceur Tile** | UUID de service BLE `0xFEED` ou `0xFEEC` | +3 🟡 |
| 9 | **Nœud MeshCore** | Nom BLE avec le préfixe `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (suivi en magasin ou sur un site)** | Données fabricant `0x004C 0x02 0x15`, déployées en magasin, aéroport et stade pour suivre les déplacements | +2 🟡 |
| 11 | **Appareil persistant inconnu** | Adresse MAC BLE non classée vue au moins 3 fois en 5 minutes (détection d’un appareil de repérage ou d’un suiveur) | +2 🟡 |

#### Détail de quelques détections BLE notables

**Caméra-piéton Axon (+5)** : Axon (anciennement TASER International) fabrique les systèmes de caméras-piétons les plus répandus auprès des forces de l’ordre aux États-Unis. L’OUI `00:25:df` est enregistré au nom d’Axon et apparaît dans ses équipements portables. **Une seule détection atteint immédiatement le seuil d’alerte.**

**Lunettes connectées Ray-Ban Meta (+5)** : La collaboration Ray-Ban Meta produit des lunettes grand public capables d’enregistrer des vidéos et des photos. L’UUID BLE `0xFD5F` est la publicité caractéristique de ces appareils. *Il s’agit d’un produit grand public qui peut se trouver dans des lieux publics fréquentés.* Une détection à ce niveau de score mérite votre attention, quelle que soit l’intention de la personne qui les porte.

**Modules Bluetooth de skimmers de cartes (+5)** : HC-03, HC-05 et HC-06 sont des modules série Bluetooth bon marché que l’on retrouve souvent dans des overlays de terminaux de paiement et des skimmers de distributeurs automatiques. La détection compare le nom exact de l’appareil aux noms par défaut connus du micrologiciel de ces modules. **Une alerte rouge doit conduire à inspecter immédiatement les terminaux de paiement à proximité.**

**Apple AirTag (+4)** : Les AirTag diffusent des annonces au moyen du protocole propriétaire **Nearby Interaction** d’Apple. La détection recherche l’en-tête fabricant propre à Apple (`0x004C`) et les sous-types AirTag (`0x12` pour l’annonce standard, `0x1E` pour un objet déclaré perdu). Les motifs de charge utile brute ajoutent une détection redondante.

**OpenDroneID BLE (+4)** : La norme **ASTM F3411 Remote ID**, également adoptée par la FAA pour les drones commerciaux aux États-Unis, définit un protocole de diffusion qui permet aux drones d’annoncer leur identité et leur position. Eye Spy recherche l’UUID de service GATT `0xFFFA` (le service Remote ID désigné) et le code d’application `0x0D` dans les charges utiles AD des données de service. *Tout drone commercial conforme en fonctionnement à proximité déclenche cette détection.*

**Appareil persistant inconnu (+2)** : C’est le moteur de **détection des suiveurs**. Eye Spy suit toute adresse MAC BLE qui n’est pas classée par les détections spécifiques ci-dessus. La même adresse MAC non classée obtient un score si elle apparaît au moins trois fois sur une période d’au moins cinq minutes. Le suivi de persistance observe jusqu’à 50 adresses MAC inconnues simultanément et supprime les entrées après 30 minutes d’absence. **Il détecte ainsi les traceurs modifiés ou personnalisés qui ne correspondent à aucun UUID de service ni motif fabricant connu.**

**iBeacon (+2)** : Des commerçants, aéroports et stades utilisent le format iBeacon d’Apple (`0x4C 0x00 0x02 0x15`) pour suivre les déplacements dans les espaces physiques. La détection se déclenche sur le format publicitaire standard, quel que soit l’UUID. Elle cible le type de déploiement, pas un UUID particulier. *Un résultat positif indique que vous vous trouvez probablement dans un lieu qui suit activement la présence des appareils Bluetooth.*

---

### Moteur 2 : scan WiFi, balayage actif des canaux

Le moteur de scan WiFi utilise l’interface standard de scan des points d’accès de l’ESP32 pour répertorier les points d’accès proches et comparer leurs BSSID et SSID aux signatures connues des appareils de surveillance.

#### Tableau des détections par scan WiFi

| # | Cible | Méthode de détection | Points |
|---|-------|----------------------|-------|
| 12 | **Caméra Flock Safety (OUI)** | Le BSSID correspond à la table de 22 OUI Flock Safety (`d4:bb:e6`, `3c:61:05`, préfixes FS-Ext-Battery) | +5 🔴 |
| 13 | **Caméra ALPR / LPR (OUI)** | Le BSSID correspond à l’OUI Motorola Solutions / Vigilant Solutions `00:0e:58` | +5 🔴 |
| 14 | **SSID avec mot-clé Flock** | Le SSID contient `flock`, `flocksafety`, `fs ext`, `penguin` ou `pigvision` | +5 🔴 |
| 15 | **SSID avec mot-clé ALPR** | Le SSID contient `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` ou `automate` | +4 🔴 |
| 16 | **Fabricant de caméra de surveillance (OUI)** | Le BSSID correspond à la table de 31 OUI de caméras : Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix, Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID avec mot-clé de caméra** | Le SSID contient entre autres `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` et `genetec` | +2 🟡 |

#### La table OUI de Flock Safety

La table `FLOCK_OUIS` à 22 entrées est la recherche la plus détaillée du projet. Elle comprend :

- `d4:bb:e6`, OUI Flock Safety enregistré auprès de l’IEEE
- `3c:61:05`, OUI Flock Safety enregistré auprès de l’IEEE
- 20 autres préfixes MAC observés sur le terrain dans les batteries Flock FS-Ext et les caméras WiFi Flock

Ces 22 entrées représentent des plages d’adresses MAC de matériel observé dans des systèmes de caméras ALPR Flock Safety en service. **La détection par OUI est indépendante du SSID.** Une caméra Flock dont le SSID ne contient aucun mot-clé obtient tout de même +5 si l’OUI de son BSSID correspond.

Les OUI de Flock Safety et de Vigilant Solutions figurent dans des tables distinctes afin que les deux puissent être détectés indépendamment au cours du même cycle de scan. *Un lieu équipé des deux types de fournisseurs peut cumuler +10 pendant un seul scan WiFi.*

#### Table OUI des fabricants de caméras de surveillance

La table de 31 OUI couvre les principaux fabricants de caméras IP susceptibles d’être présents dans des installations de surveillance commerciales, résidentielles ou dans des magasins :

- **Entreprise et commerce** : Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix, Genetec
- **Particuliers et petites entreprises** : Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex, Amcrest
- **Infrastructure** : Ubiquiti UniFi (les points d’accès et les caméras partagent des plages OUI), FLIR

Une correspondance rapporte +3 (niveau Prudence), même sans confirmation par mot-clé. Si le SSID contient aussi un mot-clé, le même réseau de caméras obtient d’abord +5 pour l’OUI, puis +2 pour le SSID, et atteint le niveau Alerte au cours d’un seul cycle.

---

### Moteur 3 : mode promiscuité WiFi, capture passive de trames

Le moteur promiscuité place la radio ESP32 en **mode moniteur** et capture les trames de gestion 802.11 brutes. Il détecte ainsi les appareils qui ne diffusent pas de SSID, en particulier les drones qui utilisent le protocole **Remote ID** via **WiFi Neighbor Awareness Networking (NaN)**.

Pendant cette phase, la radio **change de canal** toutes les 400 ms parmi `{1, 6, 11, 3, 8, 13}` afin de couvrir autant que possible les canaux de diffusion NaN des drones.

#### Tableau de détection en mode promiscuité

| # | Cible | Méthode de détection | Points |
|---|-------|----------------------|-------|
| 18 | **Drone (OpenDroneID WiFi NaN)** | Trame de gestion 802.11 destinée à `51:6f:9a:01:00:00`, diffusion ASTM F3411 Remote ID | +4 🔴 |

**OpenDroneID WiFi NaN (+4)** : La norme ASTM F3411 définit l’adresse de destination multicast `51:6f:9a:01:00:00` pour toutes les trames WiFi NaN Remote ID. Toute drone commercial réglementé qui diffuse sa position et son identité en WiFi envoie des trames à cette adresse. Eye Spy surveille simplement les trames de gestion visant cette adresse MAC multicast. La détection est passive, fiable et *impossible à neutraliser depuis la commande du drone sans désactiver complètement Remote ID, ce qui constituerait en soi une infraction réglementaire*.

Cette détection complète le moteur BLE OpenDroneID (détection nº 6). *Selon son matériel et sa configuration, un drone peut annoncer sa présence en BLE, en WiFi ou dans les deux.* Eye Spy couvre les deux.

---

## Calendrier des phases et gestion radio

```
BLE passif (9 s) → scan WiFi (~3 s) → capture promiscuité (5 s) → répétition
```

L’ESP32-PICO-D4 dispose d’une **seule radio 2,4 GHz partagée** entre BLE et WiFi. Eye Spy gère soigneusement son utilisation :

1. **Phase BLE** (9 secondes) : pile NimBLE active, scan passif en cours, aucune requête de scan transmise
2. **Arrêt du BLE** : la pile BLE est explicitement arrêtée avant l’utilisation du WiFi
3. **Scan WiFi** (~3 secondes) : scan actif des points d’accès sur tous les canaux, comparaison OUI et SSID
4. **Capture promiscuité** (5 secondes) : capture passive de trames 802.11 avec changement de canal
5. **Arrêt du WiFi** : arrêt du WiFi et redémarrage du BLE pour le cycle suivant

Cette gestion explicite des phases évite les conflits radio et permet aux moteurs BLE et WiFi d’utiliser correctement la radio à chaque cycle.

---

## Sortie série

Toutes les sorties commencent par `[eyespy]` pour faciliter le filtrage. Le moniteur série fonctionne à **115200 bauds**.

### Démarrage

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Cycle normal

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Événements de détection

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

Le champ `tracked=N` indique combien d’adresses MAC BLE uniques se trouvent actuellement dans le suivi de persistance. Il aide à comprendre la densité des appareils BLE dans l’environnement.

### Champs du score

Chaque ligne d’état comprend :
- **score** : score de menace actuel
- **state** : `CLEAR` / `CAUTION` / `ALERT`
- **phase** : moteur actif (`BLE` / `WIFI` / `PROMISC`)
- **tracked** : nombre d’adresses MAC BLE uniques dans la table de persistance

---

## Construire et flasher

### Prérequis

- **PlatformIO** (CLI ou extension VS Code)
- **M5Stack Atom Lite** ou n’importe quel ESP32 DevKit
- Câble USB-C

### Dépendances

PlatformIO installe automatiquement ces dépendances :

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** commande la LED RVB SK6812. **NimBLE-Arduino** fournit la pile de scan BLE passif. Elle est préférable à la bibliothèque BLE ESP32 par défaut : elle gère correctement le mode de scan passif, n’envoie pas de requêtes de scan et consomme moins de mémoire.

### Flasher sur M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Construire et flasher pour Atom Lite
pio run -e atom-lite -t upload

# Moniteur série à 115200 bauds
pio device monitor -b 115200
```

### Flasher sur un ESP32 DevKit générique

```bash
pio run -e esp32dev -t upload
```

### Structure du projet

```
eye-spy/
├── src/
│   └── main.cpp          # Toute la logique du micrologiciel
├── platformio.ini         # Environnements de compilation (atom-lite, esp32dev)
├── partitions_4mb.csv     # Table de partitions flash de 4 MB
└── README.md
```

### platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

*L’environnement `atom-lite` utilise la définition de carte `m5stick-c`.* Il repose sur la même puce ESP32-PICO-D4 et un brochage compatible avec le NeoPixel sur GPIO 27.

---

## Notes de détection et limites pratiques

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Illustration de style photo du détecteur Eye Spy M5Stack Atom Lite, de la taille d’un morceau de sucre, tenu entre deux doigts pour montrer son format compact" >}}

### Ce qu’Eye Spy ne peut pas faire

**WiFi 5 GHz** : L’ESP32 fonctionne uniquement en **2,4 GHz**. Les caméras, systèmes ALPR et points d’accès qui utilisent exclusivement la bande 5 GHz sont invisibles aux moteurs de scan WiFi et de capture promiscuité. *De nombreuses caméras IP modernes prennent en charge le 2,4 GHz même si elles gèrent aussi le 5 GHz ; les installations dédiées uniquement au 5 GHz ne seront toutefois pas détectées.*

**BLE chiffré** : Certains produits de surveillance haut de gamme chiffrent ou masquent leurs annonces BLE. Eye Spy détecte les appareils qui diffusent en clair des signatures identifiables (OUI, UUID de service, données fabricant). *Les appareils qui font tourner leur adresse MAC, une fonction de confidentialité courante sur les traceurs grand public, échappent à la détection fondée sur la MAC.* Le suivi de persistance peut les détecter seulement si la rotation est plus lente que cinq minutes.

**Caméras filaires** : **Les caméras IP reliées par Ethernet et dépourvues de radio WiFi n’émettent aucun signal sans fil détectable par Eye Spy.** Les caméras cachées sans connexion réseau qui enregistrent uniquement en local n’émettent pas non plus de signature RF.

**Limites de portée** : En intérieur, l’antenne ESP32 reçoit les signaux puissants jusqu’à **20–40 mètres** environ. La portée diminue pour les signaux faibles ou masqués. *Un appareil en limite de portée ou derrière un blindage RF important peut obtenir zéro point ou passer sous le seuil RSSI de −90 dBm.*

### Faux positifs à prévoir

**Caméras grand public chez les voisins** : Ring, Nest, Wyze, Arlo et Reolink sont omniprésentes dans les quartiers résidentiels. Leurs OUI figurent dans la table de 31 OUI de caméras. *Dans un quartier résidentiel, attendez-vous à quelques alertes jaunes (Prudence, +3) liées aux sonnettes vidéo des voisins.* Techniquement, ce ne sont pas de faux positifs : *l’appareil détecte bien une caméra*. Le contexte compte.

**Déploiements iBeacon dans le commerce** : Les grandes enseignes utilisent une infrastructure iBeacon dans presque tous leurs magasins. *Une visite au centre commercial ou à l’épicerie déclenchera probablement la détection iBeacon (+2).* Là encore, l’appareil fonctionne comme prévu : l’infrastructure de suivi du magasin est bien présente.

**Infrastructure Ubiquiti UniFi** : Les points d’accès UniFi figurent dans la table OUI des caméras de surveillance car Ubiquiti fabrique des équipements réseau et des caméras de sécurité dont les plages OUI se chevauchent. *Une installation réseau UniFi obtient +3 lors d’une correspondance OUI du moteur de scan WiFi.*

**Samsung SmartTag et appareils grand public** : L’UUID du SmartTag (`0xFD5A`) correspond à un service enregistré par Samsung. *Les Samsung SmartTag sont des traceurs grand public destinés à un usage personnel légitime.* La présence d’un SmartTag Samsung à proximité déclenche cette détection.

### Signification pratique des niveaux de score

| Points | Situation probable sur le terrain |
|-------|-----------------------------------|
| 6–10 (🔴) | Détection crédible à forte confiance : caméra Axon à environ 30 m, caméra Flock Safety avec OUI correspondante, AirTag suivant la cible ou drone diffusant son Remote ID |
| 3–5 (🟡) | Plusieurs traceurs grand public, accumulation de caméras voisines, caméra Flock possible ou détection OpenDroneID unique |
| 0–2 (🟢) | Aucun signal de surveillance important ; les signaux ordinaires des appareils grand public restent sous le seuil |

---

## Comparaison avec des projets similaires

Eye Spy cible la surveillance physique dans l’environnement. L’[ESP32 WiFi Canary (détecteur passif de menaces WiFi)](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) cible les attaques WiFi au niveau réseau contre vos propres appareils. *Ces outils sont complémentaires et couvrent des modèles de menace différents.*

| Fonctionnalité | Eye Spy | ESP32 WiFi Canary |
|----------------|---------|-------------------|
| Détection d’AirTag et de traceurs | ✅ | ❌ |
| Détection de caméras ALPR / Flock | ✅ | ❌ |
| Détection de caméras-piétons | ✅ | ❌ |
| Détection de drones (Remote ID) | ✅ | ❌ |
| Détection de faux points d’accès | ❌ | ✅ |
| Détection d’attaques de désauthentification | ❌ | ✅ |
| Détection d’une rétrogradation de sécurité | ❌ | ✅ |
| Apprentissage d’une référence | ❌ | ✅ |
| BLE passif | ✅ | ❌ |
| Même plateforme matérielle | ✅ | ✅ |

Les deux projets fonctionnent sur le même matériel M5Stack Atom Lite, avec les mêmes voyants LED et le même système de compilation PlatformIO. Pour une trousse complète de détection de surveillance physique et réseau, vous pouvez flasher les deux sur des appareils Atom Lite différents et les transporter simultanément.

Eye Spy complète aussi le [projet de détection Flock You](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) pour les personnes qui s’intéressent particulièrement aux infrastructures ALPR.

---

## Cas d’utilisation

### Sensibilisation à la contre-surveillance

Eye Spy s’adresse principalement aux personnes qui veulent connaître les infrastructures de surveillance à proximité immédiate. En marchant dans un quartier, en passant devant un carrefour ou en assistant à un événement public, Eye Spy transforme une analyse RF complexe en **un seul état de LED** et fournit un signal en temps réel.

### Détection du harcèlement par AirTag

Le harcèlement au moyen d’AirTag est un problème documenté. Le **moteur de détection des suiveurs** d’Eye Spy repère les adresses MAC BLE inconnues et persistantes, vues au moins trois fois sur cinq minutes. Il cible notamment les traceurs modifiés ou personnalisés qui ne suivent pas le format publicitaire Apple connu. Avec la détection directe d’AirTag, il offre **deux moyens indépendants de repérer un traceur qui vous suit**.

### Inspection d’un logement loué ou d’une chambre d’hôtel

Entrer dans un nouvel hôtel ou logement avec Eye Spy en marche donne un premier indice sur les appareils inattendus qui diffusent en BLE ou WiFi. Une SSID contenant un mot-clé de caméra ou un OUI de surveillance repéré par le moteur WiFi ajoute des points de prudence. *Cela ne remplace pas une inspection RF complète*, mais ajoute une surveillance passive de l’environnement à toute inspection physique.

### Déploiements ALPR et recherche sur la confidentialité

Eye Spy fournit un appareil de détection portable et peu coûteux aux chercheurs qui documentent les infrastructures de surveillance, aux journalistes travaillant dans des environnements surveillés et aux défenseurs de la confidentialité qui cartographient les installations ALPR. La sortie série journalise chaque détection avec le RSSI et permet une collecte de données simple.

### Sécurité en voyage

Comme le WiFi Canary, Eye Spy est conçu pour être transporté. L’Atom Lite tient dans une poche ou s’accroche à un sac. Dans les aéroports, gares ou événements publics où la surveillance est dense, il fournit une surveillance passive continue sans interaction.

---

## Notes sur l’architecture

### Pourquoi le BLE passif est important

Le choix du scan BLE passif (sans paquets de requête de scan) a des conséquences importantes pour la sécurité. En scan BLE standard, le scanner transmet un paquet **SCAN_REQ** pour demander des données publicitaires supplémentaires à chaque annonceur. *Le scan BLE actif est donc observable par les deux appareils.* L’appareil scanné voit l’adresse du scanner dans la requête.

Le mode passif NimBLE écoute uniquement les annonces non dirigées (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) et ne transmet jamais de SCAN_REQ. **Eye Spy n’émet aucune transmission BLE pendant sa phase de scan.** Une caméra-piéton Axon, un appareil Flock ou un AirTag détecté ne peut ni voir le scanner ni réagir à sa présence.

### Conception du suivi de persistance

Le suivi des appareils inconnus conserve une table pouvant contenir jusqu’à **50 adresses MAC BLE**, avec les heures de première et de dernière détection. La détection se déclenche lorsqu’une adresse apparaît au moins trois fois pendant une période d’au moins cinq minutes.

La limite de 50 entrées et la purge après 30 minutes sont des choix d’ingénierie qui équilibrent sensibilité et mémoire vive disponible sur l’ESP32. *Dans un environnement BLE dense (transports, conférence, centre commercial), la table peut vite se remplir d’appareils grand public.* Le seuil RSSI de −90 dBm filtre les appareils éloignés et concentre le suivi sur les sources persistantes proches.

### Interaction entre la décroissance et le délai de nouveau score

Le **délai de 120 secondes** empêche un appareil qui reste en permanence à portée d’accumuler des points à chaque cycle BLE de neuf secondes. Sans délai, une seule caméra Flock ajouterait +5 toutes les 15 secondes et atteindrait des centaines de points en quelques minutes.

La **décroissance de 1 point toutes les 60 secondes** fait baisser le score après qu’un appareil quitte la portée et que le délai expire sans nouvelle détection. *Une détection unique de +5 qui ne se répète pas retombe à zéro en cinq minutes.* L’appareil retrouve ainsi naturellement un état « tout va bien » adapté aux scénarios de déplacement plausibles.

---

## Contributions et état du projet

Eye Spy est disponible sous licence Apache-2.0 à l’adresse [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy).

Les extensions possibles comprennent :

- **Ajouter des entrées OUI** : enrichir les tables OUI Flock Safety et caméras lorsque de nouvelles adresses MAC sont documentées sur le terrain.
- **Ajouter des UUID de service BLE** : de nouvelles lunettes connectées, caméras et traceurs apportent de nouveaux UUID.
- **Ajuster le suivi de persistance** : la limite de 50 entrées, le seuil de trois observations et la fenêtre de cinq minutes sont des constantes modifiables.
- **Journaliser les données série** : le format de sortie série est conçu pour une analyse programmatique. Un enregistreur externe peut agréger les événements de plusieurs appareils Eye Spy.

Le micrologiciel se trouve dans un seul fichier `main.cpp` du répertoire `src/`, ce qui facilite sa lecture, son audit et sa modification.

---

## Conclusion

Eye Spy traite un problème précis mais important : l’environnement physique autour de vous est de plus en plus équipé pour la surveillance, et la plupart de ces équipements diffusent des signatures RF détectables. **Un M5Stack Atom Lite à 15 $ exécutant le micrologiciel Eye Spy devient un scanner ambiant continu.** Il réduit la complexité de l’analyse des paquets BLE et de la recherche d’OUI WiFi à une simple LED RVB.

Le modèle de score reflète une pondération réaliste des menaces : une caméra-piéton Axon à proximité d’une opération policière obtient +5 et allume immédiatement la LED en rouge ; un iBeacon commercial obtient +2 et contribue à la sensibilisation sans déclencher seul une fausse alerte. La décroissance du score et les délais empêchent l’appareil de sonner l’alarme pour des signaux temporaires ou faibles.

Pour la contre-surveillance, la sécurité en voyage, la détection d’AirTag ou simplement pour savoir si un appareil à proximité vous observe, Eye Spy est un outil pratique, open source et passif qui mérite sa place dans la trousse des professionnels de la sécurité.

**GitHub** : [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acheter des détecteurs Eye Spy et économiser 20 %
{{< /centerbutton >}}
