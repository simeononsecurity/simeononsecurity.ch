---
title: "Eye Spy : Détecteur de surveillance passif pour le M5Stack Atom Lite (ESP32)"
date: 2026-06-07
toc: true
draft: false
description: "Une référence technique complète pour Eye Spy v1.1 - un détecteur de surveillance passif BLE et WiFi open source fonctionnant sur le M5Stack Atom Lite (ESP32-PICO-D4) qui scanne les caméras corporelles, les systèmes ALPR, les AirTags, les drones et les caméras cachées avec un modèle de menace à score de confiance et une seule LED RGB."
genre: ["Outils de confidentialité", "Contre-surveillance", "Sécurité IoT", "Systèmes embarqués", "Recherche en sécurité", "Sécurité WiFi", "Sécurité Bluetooth", "Projets ESP32", "Sécurité matérielle", "Sécurité open source"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Détection de surveillance", "Contre-surveillance", "Détection BLE", "Scan WiFi", "Détection AirTag", "Détection ALPR", "Flock Safety", "Détection caméra corporelle", "Détection drone", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Open Source", "Confidentialité", "BLE passif", "Mode promiscuité", "Détection OUI", "Détection traceur", "Axon Body Camera", "Ray-Ban Meta", "Samsung SmartTag", "Tile Tracker", "Caméra cachée", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Une illustration d'un petit appareil M5Stack Atom Lite avec des ondes colorées de signaux autour de lui, sur fond bleu marine profond, représentant la détection de surveillance Bluetooth et WiFi."
coverCaption: ""
---

**Un capteur passif de la taille d'un pouce qui vous indique quand quelque chose vous observe**

## Introduction : Le paysage de surveillance que vous ne pouvez pas voir

Le monde physique est de plus en plus instrumenté avec des appareils qui observent, enregistrent et suivent. Des lecteurs de plaques sur les coins de rue, des caméras corporelles sur les forces de l'ordre, des caméras dans les logements en location, des traceurs commerciaux de type AirTag cachés dans des sacs ou des voitures, et des caméras de surveillance commerciales à chaque entrée de commerce. La plupart de ces appareils communiquent sans fil via **Bluetooth LE** ou **WiFi**, et *la plupart de ces communications sont diffusées en clair dans les airs pour que quiconque dispose du bon récepteur puisse les détecter*.

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) est un outil de détection de surveillance passif qui exploite exactement ce fait. Fonctionnant sur le **M5Stack Atom Lite**, une carte de développement ESP32-PICO-D4 à peu près de la taille d'un morceau de sucre, Eye Spy surveille continuellement les spectres BLE et WiFi pour détecter les signatures électroniques des appareils d'enregistrement, des caméras de surveillance, des systèmes **ALPR** (lecteurs automatiques de plaques d'immatriculation), des drones et des traceurs personnels. Quand il trouve quelque chose, sa LED RGB change de couleur.

*Il ne se connecte à rien. Il ne transmet rien.* Il observe, évalue et s'allume.

Cet article est une référence technique complète : ce qu'Eye Spy détecte, comment fonctionne le système de score de confiance, l'ingénierie derrière chaque moteur de détection, comment le construire et le flasher, et quelles sont ses limites pratiques.

---

## Indicateurs LED : L'interface utilisateur complète

Comme le [ESP32 WiFi Canary](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), la seule sortie d'Eye Spy est un unique SK6812 RGB NeoPixel sur GPIO 27 du M5Stack Atom Lite. La LED communique en tout temps un niveau de menace à quatre états :

| Couleur | Signification | Plage de score |
|---------|--------------|----------------|
| 🔵 Pulsation bleue | Démarrage / premier scan | -- |
| 🟢 Vert fixe | Clair - rien détecté | 0–2 |
| 🟡 Jaune fixe | Attention - possible appareil d'enregistrement à proximité | 3–5 |
| 🔴 Rouge clignotant | Alerte - appareil de surveillance/suivi définitif détecté | 6+ |

**Une seule détection à haute confiance (caméra corporelle Axon, caméra Flock Safety, correspondance OUI ALPR, AirTag) accumule suffisamment de points pour pousser immédiatement la LED au rouge en un seul cycle de détection.**

---

## Matériel

### Cible principale : M5Stack Atom Lite

| Composant | Détail |
|-----------|--------|
| Carte | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | SK6812 NeoPixel sur GPIO 27 |
| Bouton | GPIO 39 (entrée uniquement) |
| Flash | 4 Mo |

L'Atom Lite est une plateforme complète autonome. **Pas de soudure, pas de breadboard, pas de composants externes.** Branchez-le sur USB et il fonctionne.

---

## Le système de score

Eye Spy utilise un **modèle à score de confiance** qui agrège les signaux de tous les moteurs de détection en un seul entier. Le score pilote l'état de la LED (vert / jaune / rouge) et est soumis à deux mécanismes de gestion automatique :

### Décroissance du score

Le score diminue de **−1 point toutes les 60 secondes** sans nouvelles détections. Si vous vous éloignez d'un appareil détecté, la LED revient au vert en quelques minutes sans aucune intervention de l'utilisateur.

### Délai de rechargement

Chaque *type* de détection a un **délai de 120 secondes** avant de pouvoir ajouter à nouveau des points depuis la même source. *Cela empêche un seul appareil persistant d'empiler indéfiniment le score.*

---

## Moteurs de détection

Eye Spy fonctionne selon trois phases de scan distinctes en rotation continue :

**BLE passif (9 s) → Scan WiFi (~3 s) → Sniff promiscuité (5 s) → répétition**

---

### Moteur 1 : BLE - Scan passif

Le scan BLE est implémenté avec **NimBLE sans requêtes de scan transmises**. L'appareil écoute les paquets d'annonce BLE sans envoyer de réponse. *Cela rend Eye Spy électroniquement invisible pour l'équipement qu'il scanne.*

#### Tableau de détection BLE

| # | Cible | Méthode de détection | Score |
|---|-------|---------------------|-------|
| 1 | **Caméra corporelle Axon** | OUI MAC BLE `00:25:df` | +5 🔴 |
| 2 | **Ray-Ban Meta Smart Glasses** | UUID de service BLE `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE** | Nom de l'appareil BLE contenant `Flock`, `Penguin`, `Pigvision` ou `FS Ext Battery` | +5 🔴 |
| 4 | **Skimmer de carte (HC-03/05/06)** | Correspondance exacte du nom de l'appareil BLE | +5 🔴 |
| 5 | **Apple AirTag** | Données fabricant `0x004C` sous-type `0x12`/`0x1E` | +4 🔴 |
| 6 | **Drone (OpenDroneID BLE)** | UUID de service BLE `0xFFFA` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID de service BLE `0xFD5A` | +3 🟡 |
| 8 | **Tile tracker** | UUID de service BLE `0xFEED` ou `0xFEEC` | +3 🟡 |
| 9 | **Nœud MeshCore** | Préfixe du nom de l'appareil BLE `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (suivi en commerce/lieu)** | Données fabricant `0x004C 0x02 0x15` | +2 🟡 |
| 11 | **Appareil persistant inconnu** | MAC BLE non classifiée vue ≥3× sur ≥5 minutes | +2 🟡 |

---

### Moteur 2 : Scan WiFi - Scan de canaux actif

Le moteur de scan WiFi utilise l'interface de scan AP standard de l'ESP32 pour inventorier les points d'accès à proximité et comparer leurs BSSID et SSID aux empreintes d'appareils de surveillance connus.

#### Tableau de détection du scan WiFi

| # | Cible | Méthode de détection | Score |
|---|-------|---------------------|-------|
| 12 | **Caméra Flock Safety (OUI)** | BSSID correspond à la table OUI Flock Safety de 22 entrées | +5 🔴 |
| 13 | **Caméra ALPR / LPR (OUI)** | BSSID correspond à Motorola Solutions / Vigilant Solutions OUI `00:0e:58` | +5 🔴 |
| 14 | **SSID mot-clé Flock** | SSID contient : `flock`, `flocksafety`, `fs ext`, `penguin`, `pigvision` | +5 🔴 |
| 15 | **SSID mot-clé ALPR** | SSID contient : `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola`, `automate` | +4 🔴 |
| 16 | **Fournisseur de caméra de surveillance (OUI)** | BSSID correspond à la table OUI caméra de 31 entrées - Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix, Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID mot-clé caméra** | SSID contient : `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect`, `genetec` et plus | +2 🟡 |

---

### Moteur 3 : WiFi Promiscuité - Capture passive de trames

Le moteur promiscuité fait passer le radio ESP32 en **mode moniteur** et capture les trames de gestion 802.11 brutes. Cela permet la détection des appareils qui n'annoncent pas de SSID, notamment les drones utilisant le protocole **Remote ID** via **WiFi Neighbor Awareness Networking (NaN)**.

#### Tableau de détection en mode promiscuité

| # | Cible | Méthode de détection | Score |
|---|-------|---------------------|-------|
| 18 | **Drone (OpenDroneID WiFi NaN)** | Trame de gestion 802.11 vers la destination `51:6f:9a:01:00:00` | +4 🔴 |

---

## Construction et flashage

### Prérequis

- **PlatformIO** (CLI ou extension VS Code)
- **M5Stack Atom Lite** ou tout ESP32 DevKit
- Câble USB-C

### Flasher sur M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Construire et flasher pour Atom Lite
pio run -e atom-lite -t upload

# Moniteur série à 115200 bauds
pio device monitor -b 115200
```

### Flasher sur ESP32 DevKit générique

```bash
pio run -e esp32dev -t upload
```

---

## Notes de détection et limitations pratiques

### Ce qu'Eye Spy ne peut pas faire

**WiFi 5 GHz** : L'ESP32 est un appareil **uniquement 2,4 GHz**. Toute caméra de surveillance, système ALPR ou point d'accès fonctionnant exclusivement sur les bandes 5 GHz ne sera pas visible.

**BLE chiffré** : Plusieurs produits de surveillance haut de gamme chiffrent ou obscurcissent leurs annonces BLE.

**Caméras filaires** : **Les caméras IP connectées via Ethernet sans radio WiFi ne produisent aucune émission sans fil qu'Eye Spy puisse détecter.**

**Limites de portée** : L'antenne ESP32 a une portée de réception intérieure pratique de **20 à 40 mètres** pour les signaux forts.

### Faux positifs à prévoir

**Caméras de consommateurs chez les voisins** : Les caméras Ring, Nest, Wyze, Arlo et Reolink sont omniprésentes dans les quartiers résidentiels. Attendez-vous à des résultats jaunes (+3) depuis les caméras de sonnette des voisins.

**Déploiements iBeacon dans les commerces** : Les grandes enseignes déploient une infrastructure iBeacon dans pratiquement chaque magasin. Toute visite dans un centre commercial déclenchera probablement la détection iBeacon (+2).

---

## Cas d'utilisation

### Sensibilisation à la contre-surveillance

Le public principal d'Eye Spy est toute personne souhaitant une sensibilisation ambiante à l'infrastructure de surveillance dans son voisinage immédiat.

### Détection de stalking par AirTag

Le stalking par AirTag est un problème documenté. Le **moteur de détection de suiveur** d'Eye Spy (MAC BLE persistante inconnue vue ≥3× sur ≥5 minutes) cible spécifiquement les traceurs modifiés ou personnalisés.

### Inspection de location / chambre d'hôtel

Entrer dans une nouvelle chambre d'hôtel ou une location avec Eye Spy en fonctionnement donne une première indication des appareils BLE et WiFi inattendus.

### Sécurité en voyage

Comme le WiFi Canary, Eye Spy est conçu pour être portable. L'Atom Lite tient dans n'importe quelle poche.

---

## Conclusion

Eye Spy aborde un problème restreint mais significatif : l'environnement de surveillance physique autour de vous est de plus en plus instrumenté, et la majeure partie de cette instrumentation diffuse des signatures RF détectables. **Un M5Stack Atom Lite à 15 dollars exécutant le firmware Eye Spy devient un scanner ambiant continu** qui transforme la complexité de l'analyse des paquets BLE et des recherches OUI WiFi en une seule LED RGB.

**GitHub** : [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)
