---
title: "Projet Flock-You : Guide complet de matériel et de configuration pour la contre-surveillance 2026"
date: 2026-05-24
lastmod: 2026-05-24
toc: true
draft: false
description: "Guide technique complet du projet open source Flock-You pour détecter les caméras ALPR Flock Safety à l'aide de matériel basé sur ESP32. Comprend les instructions de configuration, les détails du firmware et les options d'achat."
genre: ["Matériel de sécurité", "Contre-surveillance", "Technologie de confidentialité", "Projets open source", "Développement ESP32", "Surveillance WiFi", "Outils de confidentialité", "Droits numériques", "Bricolage matériel", "Sécurité réseau"]
tags: ["Projet Flock-You", "Détection ALPR", "ESP32-S3", "Détection WiFi OUI", "Matériel contre-surveillance", "Détection Flock Safety", "Sécurité open source", "Matériel de confidentialité", "M5 Atom Lite", "OUI-SPY", "Mode promiscuité WiFi", "Surveillance 802.11", "Colonel Panic Tech", "STS Collective", "Appareils de confidentialité", "Détection de surveillance", "Scan WiFi", "Projet GitHub"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Une illustration montrant un appareil basé sur ESP32 au premier plan, scannant des signaux WiFi. Des vagues colorées représentent différentes intensités de signal sur fond sombre."
coverCaption: "Solutions matérielles open source pour détecter les caméras de surveillance ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Guide technique complet pour construire et utiliser des appareils de détection Flock-You**

## Introduction : Contre-surveillance open source

Le **projet Flock-You** est une **initiative communautaire open source** pour détecter et cartographier l'infrastructure de surveillance ALPR de Flock Safety. Hébergé sur GitHub sous **colonelpanichacks/flock-you**, ce projet utilise du matériel ESP32 abordable pour identifier les caméras Flock par leurs **signatures réseau WiFi**.

Ce guide complet couvre tout, de la **méthodologie technique** derrière la détection Flock aux **instructions de configuration étape par étape** pour trois plateformes matérielles, l'**installation du firmware** et les **informations d'achat auprès de fournisseurs autorisés**. Que vous soyez un défenseur de la vie privée, un chercheur en sécurité ou un citoyen concerné, ce guide vous permettra de construire ou d'acheter votre propre appareil de détection.

Pour le contexte sur l'importance de cette technologie, lisez notre article compagnon : **[Surveillance par caméras Flock Safety : Prévalence, préoccupations de confidentialité et stratégies de protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Vous voulez voir où les caméras Flock ont déjà été cartographiées ? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** est un outil open source qui trace 40.000+ caméras Flock Safety suspectées dans le monde en utilisant les données WiFi WiGLE et l'empreinte OUI, mis à jour quotidiennement. Source sur **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

______

## Comprendre la méthodologie de détection Flock-You

### La base technique

Les caméras Flock Safety contiennent des **modules WiFi embarqués** pour la connectivité et la gestion à distance. Ces modules diffusent des signatures réseau identifiables détectables par des appareils fonctionnant en **mode de surveillance promiscuité WiFi**. Le projet Flock-You exploite cette caractéristique à travers :

#### 1. Détection WiFi OUI (Organizationally Unique Identifier)

Chaque interface réseau a une **adresse MAC** composée de :
- **3 premiers octets (24 bits)** : OUI, qui identifie le fabricant
- **3 derniers octets** : Identifiant spécifique à l'appareil

Les chercheurs **@NitekryDPaul** et la communauté **DeFlockJoplin** ont découvert **31 OUI spécifiques** systématiquement présents dans les déploiements de caméras Flock Safety :

```
OUI Espressif primaires (modules basés sur ESP32) :
D4:AD:FC - Espressif Inc. (ESP32-S3 courant)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (variantes ESP32-S3)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (basé ESP32)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (basé ESP32)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

OUI supplémentaires identifiés dans les déploiements Flock :
[... 21 OUI de fabricants supplémentaires ...]
```

#### 2. Détection des requêtes de sonde wildcard

Les caméras Flock envoient périodiquement des **requêtes de sonde wildcard** à la recherche de réseaux disponibles. Celles-ci ont des caractéristiques distinctives :

- **Frame de gestion 802.11** : Type=0, Sous-type=4
- **Élément d'information SSID** : Longueur=0 (vide/wildcard)
- **Structure de frame** : Motif prévisible dans le timing des sondes

#### 3. Surveillance WiFi en mode promiscuité

Le mode promiscuité capture toutes les frames WiFi à portée, et les microcontrôleurs ESP32 le supportent via l'**esp_wifi API**.

#### 4. Analyse de la puissance du signal

Les appareils de détection mesurent le **RSSI** pour estimer la distance aux caméras détectées, filtrer les faux positifs et créer des cartes thermiques de densité.

______

## Comparaison des plateformes matérielles

### Tableau de présentation des plateformes

| Fonctionnalité | DIY ESP32 | M5 Atom Lite (pré-flashé) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Fabricant** | DIY / Plusieurs fournisseurs | STS Collective | Colonel Panic Tech |
| **Prix** | $5-12 | $39,99 | $85 |
| **Processeur** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Prêt à l'emploi** | Non (DIY) | Oui (pré-flashé) | Oui (multi-mode) |
| **Affichage** | Optionnel | LED RGB (matrice 5×5) | Aucun |
| **Batterie** | Optionnelle | Externe recommandée | Aucune incluse |
| **GPS** | Optionnel | Non | Non |
| **Alertes** | Buzzer + LED | LED RGB (bleu=détection) | Buzzer intégré |
| **Journalisation** | Optionnelle | Non | Non |
| **Boîtier** | Impression 3D ou aucun | Module plastique compact | Aucun (PCB nu) |
| **Firmware** | Flash manuel | FlockYou préchargé | Multi-mode (4 firmwares) |
| **Meilleur pour** | Passionnés DIY, apprentissage | Budget prêt à l'emploi | Détection multi-usage |
| **Difficulté de configuration** | Moyen-Avancé | Plug-and-play | Plug-and-play |

### Analyse détaillée des plateformes

#### 1. Construction DIY ESP32 ($5-12)

**Aperçu** : Option la plus abordable utilisant des cartes de développement ESP32 standard avec firmware open source.

**Firmware** : Fork open source sur **simeononsecurity/flock-you-esp32** :
- Modifié pour matériel ESP32 standard (GPIO 25, 2, 17)
- Mélodie de démarrage Super Mario Bros. (confirme le fonctionnement du buzzer)
- Deux bips ascendants rapides lors d'une nouvelle détection
- Bips de heartbeat toutes les 10 secondes pendant le suivi actif
- Support tableau de bord Flask pour le wardriving GPS
- Export aux formats JSON, CSV, KML

**Options de construction** :
- **LED uniquement ($5)** : ESP32 nu + câble USB, retour visuel uniquement
- **Breadboard ($9-11)** : Ajouter buzzer passif + breadboard + cavaliers, alertes audio
- **Avec boîtier ($10-12)** : Ajouter boîtier imprimé en 3D

**Avantages** :
- ✅ Option la moins chère (85-95% d'économies vs OUI-SPY)
- ✅ Entièrement open source et modifiable
- ✅ Utilise des cartes ESP32 largement disponibles
- ✅ Éducatif, enseigne les systèmes embarqués
- ✅ **Même précision de détection que les appareils premium**

**Inconvénients** :
- ❌ Nécessite un assemblage DIY
- ❌ Flash du firmware manuel requis
- ❌ Pas de batterie intégrée

**Meilleur pour** : Makers, étudiants, défenseurs de la vie privée avec un budget limité.

**Achat de composants** :
- **Amazon** : Rechercher "ESP32 DevKit" ou "ESP32 Breadboard Kit"
- **Adafruit** : Pièces de qualité avec tutoriels

---

#### 2. M5 Atom Lite Pré-flashé par STS Collective ($39,99)

**Aperçu** : Appareil de détection compact pré-flashé, prêt à l'emploi.

**Firmware** : Port FlockYou personnalisé par STS Collective (propriétaire) :
- Préchargé et prêt à l'emploi
- Alerte LED bleue lors de la détection d'une caméra Flock
- Basé sur la recherche FlockYou de colonelpanichacks
- Pas de configuration ni de flash requis

**Avantages** :
- ✅ Pré-flashé, aucune configuration technique requise
- ✅ Solution prête à l'emploi abordable
- ✅ Extrêmement compact et portable
- ✅ Simple LED bleue = détection

**Inconvénients** :
- ❌ Pas de batterie intégrée (nécessite l'alimentation USB)
- ❌ Affichage limité (LED RGB uniquement)
- ❌ *Le firmware est propriétaire*

**Achat** : [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Remise exclusive** : Économisez jusqu'à 20% sur les produits STS Collective - utilisez le code **SIMEONONSECURITY** à la caisse ou [cliquez ici pour magasiner avec la remise appliquée](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### 3. OUI-SPY par Colonel Panic Tech ($85)

**Aperçu** : Carte de détection de surveillance multi-mode avec quatre modes firmware sélectionnables via le menu WiFi.

**Spécifications matérielles** :
- **Microcontrôleur** : ESP32-S3 double cœur Xtensa LX7, 8 Mo de flash
- **Antenne** : **Commutable**, céramique 2,4 GHz intégrée OU externe via connecteur MMCX
- **Fonctionnalité unique** : Randomisation MAC à chaque démarrage

**Firmware** : OUI-SPY Unified Blue avec **4 modes sélectionnables** :
1. **Mode Detector** : Scanner BLE multi-cible avec filtrage OUI + portail de configuration web
2. **Mode Foxhunter** : Tracker RSSI proximité mono-cible pour la radiogoniométrie
3. **Mode Flock-You** : Détection de caméras Flock Safety & Raven avec wardriving GPS, export JSON/CSV/KML
4. **Mode Sky Spy** : Détecteur RemoteID de drones (OpenDroneID / ASTM F3411) avec suivi multi-drones

**Avantages** :
- ✅ Quatre modes firmware dans un seul appareil
- ✅ Antenne commutable (intégrée ou externe MMCX)
- ✅ Buzzer intégré avec mélodies de démarrage personnalisées
- ✅ Multi-usage : ALPR, drones, BLE, radiogoniométrie
- ✅ Du créateur original du projet Flock-You

**Inconvénients** :
- ❌ Prix le plus élevé pour la détection Flock uniquement
- ❌ Pas de boîtier (PCB nu)
- ❌ Pas de batterie intégrée

**Achat** : [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)

______

## Instructions de configuration étape par étape

### Guide de configuration 1 : Construction DIY ESP32

```bash
# Installer PlatformIO
pip install platformio

# Cloner le dépôt
git clone https://github.com/simeononsecurity/flock-you-esp32.git
cd flock-you-esp32

# Flasher le firmware
pio run -t upload
pio device monitor
```

**Connexions matérielles** (si vous utilisez un buzzer) :
- Buzzer positif → GPIO 25
- Buzzer négatif → GND
- LED indicateur → GPIO 2 (intégré)

### Guide de configuration 2 : M5 Atom Lite Pré-flashé

**Démarrage rapide** :
1. Connecter à une source d'alimentation USB-C
2. L'appareil démarre automatiquement
3. La LED RGB s'initialise
4. **Détection** : LED devient **BLEUE** quand une caméra Flock est détectée

### Guide de configuration 3 : OUI-SPY Multi-Mode

**Configuration initiale** :
1. Connecter l'alimentation USB-C
2. L'appareil diffuse le réseau WiFi : `OUISPY-[ID]`
3. Connecter à ce réseau et ouvrir `http://192.168.4.1`
4. Sélectionner le mode Flock-You dans l'interface web
5. L'appareil redémarre et commence à scanner

______

## Guide d'achat et informations sur les fournisseurs

### Fournisseurs autorisés

**Colonel Panic Tech** (colonelpanic.tech) :
- OUI-SPY ($85), kits DIY ($55), module GPS ($18)
- Livraison US : 3-5 jours ouvrables
- Garantie matérielle 90 jours, mises à jour firmware à vie

**STS Collective** (stscollective.com) :
- M5 Atom Lite pré-flashé ($39,99)
- Livraison US : 2-4 jours ouvrables

> 💰 **Remise lecteur** : Code **SIMEONONSECURITY** pour jusqu'à 20% - [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Considérations légales et éthiques

### Statut légal des appareils de détection

- ✅ **Légal aux États-Unis** : La surveillance WiFi passive (réception uniquement) est légale
- ✅ **Pas d'interception** : Les appareils surveillent uniquement les frames diffusées publiquement
- ✅ **Pas de décryptage** : Aucune tentative de décrypter des données
- ❌ **Illégal** : Brouillage actif ou interférence avec le fonctionnement de la caméra
- ⚠️ **Zone grise** : *Certaines juridictions ont des lois sur la vie privée plus strictes. Vérifier les réglementations locales avant utilisation.*

______

## Conclusion : Favoriser la vie privée grâce à la technologie

Le **projet de détection Flock-You** représente une démocratisation puissante de la technologie de contre-surveillance. Pour moins du coût d'un abonnement mensuel de streaming, les individus prennent conscience de l'infrastructure de surveillance qui les entoure. Que vous choisissiez la **construction DIY ESP32 ($5-12)**, le **M5 Atom Lite prêt à l'emploi ($40)** ou l'**OUI-SPY multi-mode ($85)**, vous investissez dans la sensibilisation à la vie privée et l'autonomie numérique.

______

## Références

1. [Dépôt GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - Carte interactive des caméras ALPR](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - Dépôt GitHub](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - Fournisseur officiel](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite Pré-flashé](https://stscollective.com)
6. [Documentation officielle M5Stack](https://docs.m5stack.com/en/core/atom_lite)
7. [Documentation technique Espressif ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
8. [DeFlockJoplin Community Research](https://deflockjoplin.org/)
9. [Electronic Frontier Foundation - ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [Documentation Platform.io](https://docs.platformio.org/)
