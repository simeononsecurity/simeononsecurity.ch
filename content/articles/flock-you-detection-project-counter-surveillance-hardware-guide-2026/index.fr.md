---
title: "Projet Flock-You : Guide complet de matériel et de configuration pour la contre-surveillance 2026"
date: 2026-05-24
lastmod: 2026-11-19
toc: true
draft: false
description: "Guide technique complet du projet open source Flock-You pour détecter les caméras ALPR Flock Safety à l'aide de matériel basé sur ESP32. Comprend les instructions de configuration, les détails du firmware et les options d'achat."
genre: ["Matériel de sécurité", "Contre-surveillance", "Technologie de confidentialité", "Projets open source", "Développement ESP32", "Surveillance WiFi", "Outils de confidentialité", "Droits numériques", "Bricolage matériel", "Sécurité réseau"]
tags: ["Projet Flock-You", "Détection ALPR", "ESP32-S3", "Détection OUI WiFi", "Matériel de contre-surveillance", "Détection Flock Safety", "Sécurité open source", "Matériel de protection de la vie privée", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "Mode promiscuité WiFi", "Surveillance 802.11", "Colonel Panic Tech", "STS Collective", "Appareils de protection de la vie privée", "Détection de surveillance", "Balayage WiFi", "Projet GitHub", "colonelpanichacks", "Micrologiciel ESP32", "Guide d’installation du matériel", "Outils DIY de protection de la vie privée", "Surveillance réseau", "Base de données OUI", "Détection des sondages génériques", "Analyse de trames", "Détection de caméras ALPR", "Technologie de protection de la vie privée", "Matériel de détection", "Arduino ESP32", "Platform.io", "Systèmes embarqués", "Détection RF", "Traitement du signal", "Ingénierie de la vie privée", "Technologie de contre-surveillance", "Recherche en sécurité", "Défense de la vie privée", "Matériel ouvert", "Protection de la vie privée", "Micrologiciel de détection", "Détection mobile", "Projets de protection de la vie privée", "Comparatif matériel"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Une illustration montrant un appareil basé sur ESP32 au premier plan, scannant des signaux WiFi. Des vagues colorées représentent différentes intensités de signal sur fond sombre."
coverCaption: "Solutions matérielles open source pour détecter les caméras de surveillance ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Guide technique complet pour construire et utiliser des appareils de détection Flock-You**

## Introduction : Contre-surveillance open source

Le **projet Flock-You** est une **initiative communautaire open source** pour détecter et cartographier l'infrastructure de surveillance ALPR de Flock Safety. Hébergé sur GitHub sous **colonelpanichacks/flock-you**, ce projet utilise du matériel ESP32 abordable pour identifier les caméras Flock par leurs **signatures réseau WiFi**.

**Flock-You détecte uniquement les caméras Flock Safety par Wi-Fi.** Il ne détecte ni les simulateurs de stations cellulaires de type Stingray ni les traceurs personnels qui se déplacent avec vous. Pour cela, consultez **[Flasher les appareils Rayhunter : guide complet](/articles/how-to-flash-rayhunter-devices-complete-guide/)** pour détecter les capteurs IMSI et **[Eye Spy : détecteur passif de surveillance et de traqueurs à base d’ESP32](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** pour détecter les AirTags et les traceurs. Les trois fonctionnent sur la même famille de matériel ESP32 abordable.

Ce guide complet couvre tout, de la **méthodologie technique** derrière la détection Flock aux **instructions de configuration étape par étape** pour trois plateformes matérielles, l'**installation du firmware** et les **informations d'achat auprès de fournisseurs autorisés**. Que vous soyez un défenseur de la vie privée, un chercheur en sécurité ou un citoyen concerné, ce guide vous permettra de construire ou d'acheter votre propre appareil de détection.


*Le matériel Flock Safety est déployé presque entièrement aux États-Unis, avec une présence moindre au Canada. En dehors de l'Amérique du Nord, la liste d'OUI et les signatures de sondes ci-dessous ne correspondront à aucun appareil à proximité. Ce matériel reste utile pour la recherche, mais ne détectera pas une infrastructure absente de la région.*

Pour le contexte sur l'importance de cette technologie, lisez notre article compagnon : **[Surveillance par caméras Flock Safety : Prévalence, préoccupations de confidentialité et stratégies de protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Vous voulez voir où les caméras Flock ont déjà été cartographiées ? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** est un outil open source qui trace 40.000+ caméras Flock Safety suspectées dans le monde en utilisant les données WiFi WiGLE et l'empreinte OUI, mis à jour quotidiennement. Source sur **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

### En un coup d’œil : trois plateformes

*Les caractéristiques complètes, les avantages et les inconvénients de chaque plateforme sont plus bas. Accédez aux [instructions de configuration](#instructions-de-configuration-étape-par-étape) si vous savez déjà laquelle choisir.*


| Plateforme | Prix | Configuration | Idéal pour |
|---|---|---|---|
| **DIY ESP32** | 5–12 $ | Plaque d’essai sans soudure, 10–15 min | Montages économiques et apprentissage de la détection |
| **M5 Atom Lite** (préflashé) | 49,99 $ | Brancher et utiliser, sans configuration | Utilisation immédiate sans montage DIY |
| **OUI-SPY** | 85 $ | Flasher une fois, puis choisir le mode dans le menu Wi-Fi | Détection multimode (ALPR, drones et BLE) |

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

Lorsqu’un appareil de détection analyse le trafic Wi-Fi en mode promiscuité, **il repère tout appareil qui diffuse des trames avec ces OUI**.

#### 2. Détection des requêtes de sonde wildcard

Les caméras Flock envoient périodiquement des **requêtes de sonde wildcard** pour rechercher les réseaux disponibles. Ces requêtes présentent des caractéristiques distinctives :

- **Trame de gestion 802.11** : Type=0, sous-type=4
- **Élément d'information SSID** : longueur=0 (vide/wildcard)
- **Structure de trame** : motif prévisible dans le rythme des sondes
- **Éléments d'information propres au fabricant** : indicateurs supplémentaires dans la charge utile de la trame

Le firmware analyse ces **motifs de requêtes de sonde** pour renforcer l'identification des caméras Flock au-delà d'une simple correspondance OUI.

#### 3. Surveillance Wi-Fi en mode promiscuité

Le fonctionnement Wi-Fi standard ne reçoit que les trames adressées à votre appareil. Le **mode promiscuité** capture toutes les trames Wi-Fi à portée :

- **Structure des trames 802.11** : analyse des champs addr1, addr2 et addr3
- **Trames de gestion** : requêtes de sonde, trames beacon et demandes d'association
- **Trames de données** : révèlent les habitudes d'activité du réseau
- **Trames de contrôle** : ACK, RTS et CTS fournissent des informations de temporisation

Les microcontrôleurs ESP32 prennent en charge le mode promiscuité par l'**API esp_wifi**, ce qui permet de construire du matériel de détection peu coûteux.

#### 4. Analyse de l'intensité du signal

Les appareils de détection mesurent le **RSSI (indicateur de puissance du signal reçu)** pour :
- **Estimer la distance** aux caméras détectées
- **Trianguler leur emplacement** à partir de plusieurs mesures
- **Filtrer les faux positifs** selon les caractéristiques attendues du signal
- **Créer des cartes thermiques** de densité des caméras

### Précision de détection et faux positifs

La précision dépend fortement de l'environnement. Un essai de terrain documenté fournit un repère concret : la communauté **DeFlockJoplin** a détecté **11 des 12 caméras Flock connues et relevé seulement 2 faux positifs** pendant un trajet de test.

- **Repère observé sur le terrain** : 11 caméras confirmées sur 12 détectées, 2 faux positifs (essai de DeFlockJoplin)
- **Portée de détection** : 50 à 300 pieds selon les obstacles et l'antenne
- **Score de confiance** : combiner la correspondance OUI, la signature de requête wildcard et le seuil RSSI réduit les fausses alertes
- **Les résultats varient** : l'environnement radio, l'antenne et la version du firmware influent sur la précision réelle

**Sources courantes de faux positifs** :
- **Cartes de développement ESP32** utilisées dans d'autres appareils IoT
- **Produits commerciaux basés sur ESP32**, comme des équipements domotiques et des capteurs
- **Autres caméras de surveillance** utilisant des composants similaires
- **Équipements de test Wi-Fi** utilisés par des techniciens

**Stratégies d'atténuation** :
- **Combiner plusieurs signatures** : correspondance OUI, motif de requête et vérification physique
- **Corréler les emplacements** : comparer les détections avec des emplacements de caméras connus
- **Confirmer visuellement** : vérifier le lieu depuis un endroit sûr et public après une détection électronique
- **Consulter une base communautaire** : valider les détections collectivement

{{< figure src="flockyou-oui-detection-methodology-overview.webp" alt="Schéma de détection Flock-You : l’ESP32 en mode Wi-Fi promiscu compare les MAC aux OUI connus, vérifie les sondes génériques et évalue le RSSI" >}}

{{< stscollective-ad "flockyou" >}}

## Comparaison des plateformes matérielles

Trois plateformes principales sont disponibles pour détecter Flock-You, chacune avec ses avantages.
*Les trois plateformes utilisent la même méthode de détection : un balayage passif du WiFi en mode promiscuité pour rechercher les OUI connus des caméras Flock et les signatures de requêtes de sonde génériques. Aucune ne détecte le Bluetooth. Le micrologiciel Flock-You a abandonné la détection BLE au printemps 2026, car elle ne fonctionnait plus de manière fiable. Toutes les plateformes présentées ici utilisent donc uniquement le WiFi.*
### Tableau de présentation des plateformes

| Fonctionnalité | DIY ESP32 | M5 Atom Lite (pré-flashé) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Fabricant** | DIY / Plusieurs fournisseurs | STS Collective | Colonel Panic Tech |
| **Prix** | $5-12 | $49.99 | $85 |
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
| **Difficulté de configuration** | Moyen-Avancé | Aucune configuration | Aucune configuration |
| **Poids** | 20–50 g selon le modèle | 18 g (nu) | ~40 g |
| **Dimensions** | Variables | 24 × 24 × 14 mm | Carte PCB |

### Analyse détaillée des plateformes

#### 1. Construction DIY ESP32 ($5-12)

**Aperçu** : Option la plus abordable utilisant des cartes de développement ESP32 standard avec firmware open source.


**Spécifications matérielles** :
- **Microcontrôleur** : ESP32-WROOM-32 ou équivalent (double cœur, 240 MHz)
- **Wi-Fi** : 802.11 b/g/n, compatible avec le mode promiscuité
- **Mémoire** : 520 Ko de SRAM, 4 Mo ou plus de mémoire flash
- **Affichage** : facultatif, la LED intégrée suffit
- **Alimentation** : USB ou batterie externe
- **Buzzer** : module de buzzer passif facultatif (KY-006)
- **Voyants** : LED intégrée et buzzer facultatif
- **Extension** : compatible avec une plaque d'essai et facile à modifier

**Firmware** : fork open source **simeononsecurity/flock-you-esp32** :
- Modifié pour matériel ESP32 standard (GPIO 25, 2, 17)
- Mélodie de démarrage Super Mario Bros. (confirme le fonctionnement du buzzer)
- Deux bips ascendants rapides lors d'une nouvelle détection
- Bips de heartbeat toutes les 10 secondes pendant le suivi actif
- Support tableau de bord Flask pour le repérage de réseaux Wi-Fi en voiture avec GPS
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
- ✅ Documentation et guides détaillés
- ✅ Fichiers disponibles pour imprimer un boîtier en 3D
- ✅ **Même précision de détection que les appareils premium**

**Inconvénients** :
- ❌ Nécessite un assemblage DIY
- ❌ Flash du firmware manuel requis
- ❌ Pas de batterie intégrée
- ❌ Retour audio basique uniquement, sans écran
- ❌ L’approvisionnement des composants prend du temps

**Meilleur pour** : Makers, étudiants, défenseurs de la vie privée avec un budget limité.

**Achat de composants** :
- **Amazon** : Rechercher "ESP32 DevKit" ou "ESP32 Breadboard Kit"
- **AliExpress/eBay** : remises sur les achats en quantité
- **Adafruit** : composants sélectionnés avec tutoriels

---

**Ressources de configuration** :
- **Dépôt GitHub** : [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Guide de montage** : assemblage sans soudure en 10 à 15 minutes
- **Fichiers du boîtier** : conception paramétrique OpenSCAD et fichiers STL

{{< figure src="flockyou-diy-esp32-solderless-breadboard-build.webp" alt="Montage Flock-You avec ESP32 sur plaque sans soudure, DevKit, buzzer passif et fils reliés aux GPIO 25, 2 et 17" >}}

#### 2. M5 Atom Lite Pré-flashé par STS Collective ($49.99)

**Aperçu** : Appareil de détection compact pré-flashé, prêt à l'emploi.

**Spécifications matérielles** :
- **Microcontrôleur** : ESP32-PICO-D4 (double cœur, 240 MHz)
- **Wi-Fi** : 802.11 b/g/n, compatible avec le mode promiscuité
- **Mémoire** : 520 Ko de SRAM et 4 Mo de mémoire flash
- **Affichage** : matrice LED RGB 5×5 (WS2812C NeoPixel)
- **Alimentation** : 5 V par USB-C ou connecteur Grove
- **Batterie** : non fournie, batterie USB externe recommandée
- **Voyant** : LED RGB programmable (bleu = détection)
- **Boutons** : un bouton programmable
- **E/S** : connecteur Grove pour l'extension
- **Taille** : ultracompact, 24 × 24 × 14 mm
- **Boîtier** : module en plastique résistant


**Firmware** : portage personnalisé de FlockYou par STS Collective (propriétaire) :
- Préchargé et prêt à l'emploi
- Alerte LED bleue lors de la détection d'une caméra Flock
- Basé sur les recherches FlockYou de colonelpanichacks
- Aucune configuration ni aucun flash requis
- Fonctionnement simple, prêt à l'emploi
- Prise en charge facultative du tableau de bord

**Avantages** :
- ✅ Préflashé, aucune configuration technique requise
- ✅ Solution abordable, prête à l'emploi
- ✅ Très compact et portable
- ✅ Plateforme matérielle éprouvée
- ✅ LED bleue simple pour signaler une détection
- ✅ Alimentation USB-C (voiture, batterie externe, ordinateur)
- ✅ Assistance d'un fournisseur qui effectue un contrôle qualité
- ✅ Prix habituel de $99.99, actuellement réduit à $49.99

**Inconvénients** :
- ❌ Pas de batterie intégrée (alimentation USB nécessaire)
- ❌ Affichage limité (LED RGB uniquement, sans écran)
- ❌ *Le firmware est propriétaire et n'est pas open source pour le moment*
- ❌ Aucun enregistrement de données sans connexion à un ordinateur
- ❌ Un seul bouton limite les fonctions

**Idéal pour** : les personnes qui veulent une détection immédiate et portable, et préfèrent une solution prête à l'emploi avec un simple signal LED.


**Achat** : [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Remise exclusive** : économisez jusqu'à 20 % sur les produits STS Collective. Utilisez le code **SIMEONONSECURITY** lors du paiement ou [achetez avec la remise appliquée](https://stscollective.com/discount/SIMEONONSECURITY).

{{< figure src="flockyou-m5-atom-lite-pocket-size-comparison.webp" alt="M5 Atom Lite préflashé entre deux doigts, montrant son format compact et sa LED RGB bleue de détection" >}}

---

#### 3. OUI-SPY par Colonel Panic Tech ($85)

**Aperçu** : carte de détection multimode avec quatre modes de firmware sélectionnables dans un menu Wi-Fi.


**Spécifications matérielles** :
- **Microcontrôleur** : ESP32-S3, double cœur Xtensa LX7, 8 Mo de mémoire flash
- **Wi-Fi** : 802.11 b/g/n, compatible avec le mode promiscuité
- **Mémoire** : 8 Mo de mémoire flash
- **Affichage** : aucun (carte PCB nue avec voyants LED)
- **Batterie** : non fournie
- **Alimentation** : USB-C pour l'alimentation et la programmation
- **Stockage** : aucun (modes dédiés à la détection)
- **Voyants** : buzzer PWM intégré avec tonalités propres à chaque mode
- **Boutons** : bouton BOOT pour changer de mode
- **Antenne** : antenne autocollante intégrée de 2,4 GHz, remplaçable pour gagner en portée
- **Boîtier** : aucun (carte nue avec motif imprimé)
- **Fonctionnalité unique** : adresse MAC randomisée à chaque démarrage

**Firmware** : OUI-SPY Unified Blue avec **4 modes sélectionnables** :
1. **Mode Detector** : Scanner BLE multi-cible avec filtrage OUI + portail de configuration web
2. **Mode Foxhunter** : Tracker RSSI proximité mono-cible pour la radiogoniométrie
3. **Mode Flock-You** : Détection de caméras Flock Safety & Raven avec repérage de réseaux Wi-Fi en voiture avec GPS, export JSON/CSV/KML
4. **Mode Sky Spy** : Détecteur RemoteID de drones (OpenDroneID / ASTM F3411) avec suivi multi-drones

**Sélection du mode** :
- Menu de démarrage Wi-Fi à l'adresse `192.168.4.1`
- Maintenez le bouton BOOT pendant deux secondes pour revenir au sélecteur
- Le dernier mode utilisé est mémorisé après un cycle d'alimentation
- Chaque mode possède sa tonalité de démarrage et ses alertes rétro
- Fonctionnement limité à la détection, aucune transmission

**Avantages** :
- ✅ Quatre modes firmware dans un seul appareil
- ✅ Antenne commutable (intégrée ou externe MMCX)
- ✅ Buzzer intégré avec mélodies de démarrage personnalisées
- ✅ Conception de PCB de qualité professionnelle
- ✅ Multi-usage : ALPR, drones, BLE et radiogoniométrie
- ✅ Développement et mises à jour actifs
- ✅ Du créateur original du projet Flock-You

**Inconvénients** :
- ❌ Prix le plus élevé pour la détection Flock uniquement
- ❌ Pas de boîtier (PCB nu)
- ❌ Pas de batterie intégrée
- ❌ Pas d’écran (retour audio uniquement pour la plupart des modes)
- ❌ Complexité inutile pour une détection de base
- ❌ GPS externe nécessaire pour le repérage de réseaux Wi-Fi en voiture

**Idéal pour** : la détection de surveillance polyvalente, les personnes qui veulent détecter drones, ALPR et BLE avec un seul appareil, la radiogoniométrie et celles qui souhaitent une antenne remplaçable et des fonctions avancées.

**Achat** : [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)

______

{{< figure src="flockyou-oui-spy-multimode-board-pcb.webp" alt="Circuit nu OUI-SPY ESP32-S3 avec antenne, buzzer et bouton de démarrage; un écran affiche le menu Wi-Fi à quatre modes" >}}

## Instructions de configuration étape par étape

### Guide de configuration 1 : montage DIY avec ESP32

**Consultez le guide détaillé** dans le [dépôt GitHub](https://github.com/simeononsecurity/flock-you-esp32).

#### Démarrage rapide

1. **Matériel nécessaire** :
   - Carte ESP32 DevKit ($5–6)
   - Câble USB (Micro-USB ou USB-C selon la carte)
   - En option : buzzer passif (KY-006), plaque d'essai et fils de connexion
   - En option : boîtier imprimé en 3D

2. **Préparer le logiciel** :
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

3. **Assembler le matériel** (si un buzzer est utilisé) :
   - Borne positive du buzzer → GPIO 25
   - Borne négative du buzzer → GND
   - Voyant LED → GPIO 2 (intégré)
   - Alimentation par USB

4. **Confirmer le démarrage** :
   - La mélodie de Super Mario Bros. 1-2 retentit si le buzzer est branché
   - La LED clignote pendant le balayage
   - Le moniteur série affiche l'initialisation de « Flock-You ESP32 »

5. **Alertes de détection** :
   - **Nouvelle détection** : deux bips rapides et ascendants (2000 → 2800 Hz)
   - **Signal périodique** : deux bips toutes les 10 secondes pendant le suivi
   - **LED** : clignote à chaque détection

6. **Repérage de réseaux Wi-Fi en voiture avec GPS** (facultatif) :
   - Reliez l'appareil à un ordinateur par USB
   - Lancez le tableau de bord Flask avec `cd api && python flockyou.py`
   - Ouvrez `http://localhost:5000`
   - Connectez un GPS ou utilisez la position du navigateur
   - Exportez les détections en JSON, CSV ou KML

**Guide de montage complet, fichiers du boîtier et dépannage** : consultez le README du dépôt GitHub.

---

### Guide de configuration 2 : M5 Atom Lite préflashé (STS Collective)

#### Démarrage rapide

1. **Vérifier le contenu** :
   - Appareil M5 Atom Lite préflashé avec le firmware FlockYou
   - Vérifiez si le câble USB-C est inclus dans la fiche produit

2. **Allumer** :
   - Branchez une source d'alimentation USB-C : batterie externe, port USB de voiture, adaptateur secteur ou ordinateur
   - L'appareil démarre automatiquement
   - La matrice LED RGB s'initialise

3. **Utilisation** :
   - **Veille/balayage** : la LED affiche un motif de balayage
   - **Détection** : la LED devient **BLEUE** quand une caméra Flock est détectée
   - **Bouton** : appuyez pour relancer un balayage ou réinitialiser l'appareil

4. **Utilisation mobile** :
   - Branchez une batterie USB (5000 mAh fournissent environ 20 heures)
   - Placez l'appareil dans un porte-gobelet, un sac ou une poche
   - La LED reste visible à travers le boîtier translucide

5. **Connexion au tableau de bord** (facultatif) :
   - Reliez l'appareil à un ordinateur avec un câble USB-C
   - Installez le tableau de bord FlockYou selon les instructions de STS Collective
   - Consultez les détections en direct dans le navigateur

**Avertissement** : *Ce firmware est propriétaire. Le reflasher avec une version open source supprimera définitivement le firmware de STS.*

---

### Guide de configuration 3 : carte multimode OUI-SPY

#### Configuration initiale

1. **Contenu du paquet** :
   - Carte PCB OUI-SPY nue
   - Câble USB-C
   - Guide de démarrage rapide

2. **Premier démarrage** :
   - Branchez l'alimentation USB-C à un ordinateur, un adaptateur secteur ou une batterie externe
   - L'appareil diffuse le réseau Wi-Fi `OUISPY-[ID]`
   - Le buzzer joue une tonalité de démarrage propre au mode choisi

3. **Choisir un mode Wi-Fi** :
   - Connectez le téléphone ou l'ordinateur au réseau Wi-Fi OUI-SPY
   - Ouvrez `http://192.168.4.1` dans le navigateur
   - L'interface web affiche quatre modes de firmware :
     1. **Detector** : scanner BLE multi-cibles
     2. **Foxhunter** : radiogoniométrie
     3. **Flock-You** : détection de caméras ALPR
     4. **Sky Spy** : détection de drones Remote ID
   - Choisissez le mode souhaité et cliquez sur « Activate »

4. **Utiliser le mode Flock-You** :
   - L'appareil redémarre en mode Flock-You
   - Le buzzer joue la tonalité de démarrage Flock-You
   - Il recherche 31 préfixes OUI connus
   - **Alerte de détection** : le buzzer émet un motif distinctif
   - Le dernier mode utilisé est mémorisé après un cycle d'alimentation

5. **Changer de mode** :
   - Maintenez le bouton **BOOT** pendant deux secondes
   - L'appareil revient au sélecteur de mode Wi-Fi
   - Reconnectez-vous au Wi-Fi et choisissez un autre mode

#### Option avancée : changer d'antenne

6. **Changer d'antenne** (pour augmenter la portée) :
   - L'antenne autocollante intégrée est utilisée par défaut
   - Des antennes à gain supérieur peuvent être soudées pour étendre la portée
   - Il s'agit d'une modification matérielle, pas d'un réglage logiciel. Vérifiez le connecteur en vigueur sur colonelpanic.tech avant de commander une antenne

#### Montage

7. **Installation dans un véhicule ou à poste fixe** :
   - *Aucun boîtier n'est fourni. Protégez la carte nue avant de la fixer.*
   - Options :
     - Imprimer un boîtier personnalisé en 3D
     - Fixer l'appareil au tableau de bord avec du Velcro
     - Utiliser du ruban adhésif double face
     - Utiliser un boîtier de projet
   - Laissez le port USB-C accessible pour l'alimentation

#### Exportation des données (mode Flock-You)

8. **Repérage de réseaux Wi-Fi en voiture avec GPS** :
   - Connectez un module GPS externe (non fourni)
   - L'appareil journalise les détections avec leurs coordonnées
   - Téléchargez les fichiers via l'interface web
   - Exportez les données en JSON, CSV ou KML

**Remarque** : consultez colonelpanic.tech pour les mises à jour du firmware et la documentation OUI-SPY Unified Blue.

______

## Guide d'achat et informations sur les fournisseurs

### Fournisseurs autorisés

#### Colonel Panic Tech (colonelpanic.tech)

**Produits proposés** :
- **OUI-SPY** ($85) : appareil de détection Flock prêt à l'emploi
- **Kits DIY** ($55) : composants, carte PCB et guide de montage
- **Module GPS en option** ($18) : module GPS-6M compatible
- **Accessoires** : antennes, boîtiers et batteries améliorées

**Pourquoi acheter chez Colonel Panic** :
- ✅ Directement auprès du développeur du matériel OUI-SPY
- ✅ Dernier firmware préinstallé
- ✅ Assistance technique incluse
- ✅ Approche open source, schémas disponibles
- ✅ Forum communautaire actif

**Livraison** :
- États-Unis : 3 à 5 jours ouvrables
- International : 7 à 14 jours
- Livraison gratuite pour toute commande supérieure à $100

**Garantie** : 90 jours sur le matériel, mises à jour du firmware à vie

**Site web** : [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Produits proposés** :
- **M5 Atom Lite préflashé** ($49.99) : appareil de détection Flock prêt à l'emploi
- **Accessoires** : compatibles avec différentes plateformes ESP32

**Pourquoi acheter chez STS Collective** :
- ✅ Appareils préflashés et prêts à l'emploi
- ✅ Contrôle qualité et tests
- ✅ Prix abordables
- ✅ Service client

**Livraison** :
- États-Unis : 2 à 4 jours ouvrables par Priority Mail
- International : 7 à 21 jours
- Options d'expédition express disponibles

**Garantie** : garantie standard sur le matériel

**Site web** : [https://stscollective.com](https://stscollective.com)

> 💰 **Réduction pour les lecteurs** : Utilisez le code **SIMEONONSECURITY** pour obtenir jusqu'à 20 % de réduction sur les produits STS Collective. [Acheter avec la réduction appliquée](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Autres sources pour le M5 Atom Lite

**Boutique officielle M5Stack** :
- Site web : [shop.m5stack.com](https://shop.m5stack.com)
- Prix : $9.95 pour un Atom Lite nu
- Accessoires : modules de batterie, capteurs Grove et boîtiers
- Livraison : internationale, 7 à 14 jours

**Amazon** : recherchez « M5Stack Atom Lite »
- Prix : environ $12–15 selon le vendeur
- Livraison Prime disponible
- Lots avec accessoires proposés

**Adafruit** : [adafruit.com](https://adafruit.com)
- Revendeur de composants électroniques avec sélection soignée
- Excellentes ressources pédagogiques
- Livraison rapide aux États-Unis

**Remarque** : *Un M5 Atom Lite nu nécessite une installation distincte du firmware, selon le guide DIY ci-dessus. La version préflashée de STS Collective est un produit différent.*

### Comparatif des prix

| Appareil | Prix de base | Options facultatives | Investissement total | Temps de configuration |
|--------|------------|---------------------|----------------------|------------------------|
| **DIY ESP32** | $5–12 | Boîtier 3D, batterie | $5–20 | 15–30 min |
| **M5 Atom Lite** | $49.99 | Batterie externe $10 | $50–60 | Prêt à l'emploi |
| **OUI-SPY** | $85 | Antenne externe $20, boîtier | $85–115 | Prêt à l'emploi |

______

## Utiliser le détecteur : mises en situation

{{< figure src="flockyou-detection-device-driving-scenario.webp" alt="Illustration d’un conducteur qui regarde un petit détecteur FlockYou posé dans le porte-gobelet, dont la LED signale une caméra Flock Safety à proximité" >}}

### Situation 1 : cartographier les trajets quotidiens

**Objectif** : relever l’emplacement des caméras Flock sur vos itinéraires habituels.

**Préparation** :
- Utilisez un appareil compatible GPS (ESP32 DIY avec module GPS ou OUI-SPY avec GPS).
- Activez l’enregistrement automatique.
- Installez l’appareil dans le véhicule ou gardez-le dans votre poche.
- Réglez la sensibilité sur MOYENNE pour réduire les faux positifs.

**Procédure** :
1. Démarrez le détecteur avant de partir.
2. Suivez votre trajet habituel.
3. L’appareil vous avertit lorsqu’il détecte des caméras Flock.
4. Les coordonnées GPS sont enregistrées automatiquement.
5. De retour chez vous, exportez les données.
6. Importez le fichier GPX/CSV dans un logiciel cartographique.
7. Créez votre carte personnelle des emplacements de caméras.

**Avantages** :
- Connaître la couverture de surveillance sur vos trajets.
- Repérer des itinéraires alternatifs sans caméra.
- Contribuer aux projets de cartographie communautaire.
- Suivre l’évolution des installations au fil du temps.

### Situation 2 : évaluer la surveillance du quartier

**Objectif** : déterminer la couverture des caméras Flock dans votre quartier résidentiel.

**Préparation** :
- Utilisez un appareil portable (M5 Atom Lite, ESP32 DIY ou OUI-SPY).
- Faites le parcours à pied ou à vélo.
- Effectuez des relevés statiques aux intersections importantes.

**Procédure** :
1. Parcourez les rues du quartier à pied ou à vélo.
2. Arrêtez-vous à chaque intersection pendant 30 à 60 secondes.
3. Notez les détections sur une carte.
4. Estimez la distance et la direction à l’aide de la puissance du signal.
5. Confirmez visuellement l’emplacement des caméras lorsque c’est possible.
6. Documentez les résultats avec des photos prises depuis l’espace public.

**Résultat** :
- Carte complète de l’infrastructure de surveillance locale.
- Éléments utiles à la mobilisation communautaire.
- Données pour les demandes de documents publics.
- Informations pour vos décisions personnelles en matière de vie privée.

*La vitesse de marche compte plus que beaucoup ne le pensent. Le micrologiciel change de canal WiFi environ toutes les 250 ms pour suivre la fréquence à laquelle la caméra change elle-même de canal. En marchant ou en pédalant vite, vous pouvez dépasser la fenêtre de détection avant que le changement de canal ne coïncide. Si les détections sont irrégulières pendant un relevé à pied, ralentissez aux intersections au lieu d’essayer d’abord une antenne à gain plus élevé. Une antenne standard avec une pause de 30 à 60 secondes à chaque arrêt détecte bien plus de caméras qu’une antenne à gain élevé utilisée en mouvement rapide.*

### Situation 3 : évaluer l’exposition à la surveillance en voyage

**Objectif** : comprendre votre exposition à la surveillance pendant vos déplacements.

**Préparation** :
- Emportez un appareil compact (M5 Atom Lite dans une poche ou ESP32 DIY).
- Activez l’enregistrement continu.
- Examinez les données après le voyage.

**Cas d’usage** :
- Rendez-vous médicaux : évaluez la surveillance près des cliniques.
- Consultations juridiques : vérifiez la couverture autour des cabinets d’avocats.
- Services religieux : identifiez la surveillance près des lieux de culte.
- Activités politiques : évaluez la surveillance lors de rassemblements et de manifestations.
- Situations domestiques : vérifiez si un domicile est surveillé.

### Situation 4 : mobilisation communautaire

**Objectif** : apporter des données aux débats sur les politiques publiques et à la sensibilisation.

**Applications** :
- Présenter les résultats aux réunions du conseil municipal.
- Les joindre aux demandes de documents publics.
- Les partager avec des organisations de défense de la vie privée.
- Contribuer à des projets de recherche.
- Informer les associations de quartier.

**Présentation des données** :
- Créer des cartes thermiques de la densité des caméras.
- Produire des rapports sur les inégalités de couverture.
- Établir des chronologies de l’expansion des installations.
- Comparer les données aux statistiques de la criminalité, ou à leur absence.

______


## Comment fonctionne réellement le code de détection

### Algorithme de détection de base (simplifié)

Pour les lecteurs intéressés par l’implémentation technique, voici une version simplifiée de la logique de détection :

```cpp
// Cœur de détection Flock-You (conceptuel, code incomplet)

// Base de données OUI (31 OUI associés à Flock connus)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // Variante Espressif ESP32-S3
    // ... 28 autres OUI ...
};

// Fonction de rappel du mode promiscuité
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;

    // Extraire l’adresse MAC de la trame
    uint8_t *mac = pkt->payload + 10; // Position du champ addr2

    // Comparer avec la base de données OUI
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // Correspondance OUI trouvée
            int rssi = pkt->rx_ctrl.rssi;

            // Vérifier le seuil de puissance du signal
            if (rssi > RSSI_THRESHOLD) {
                // Analyser la trame pour détecter d’autres signatures
                if (is_wildcard_probe_request(pkt)) {
                    // Détection à haute confiance
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // Correspondance OUI uniquement
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Détection des requêtes de sondage génériques
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Trame de gestion, sous-type requête de sondage
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;

    // Vérifier si l’élément SSID est vide (générique)
    // La position dépend de la structure de la trame
    uint8_t *ie = &pkt->payload[24]; // Début des éléments d’information
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Sondage générique
    }
    return false;
}
```

### Explication des principaux concepts techniques

**Mode promiscuité** : au lieu de recevoir uniquement les trames adressées à votre appareil, l’ESP32 capture toutes les trames WiFi à portée. **C’est indispensable pour détecter les appareils proches qui ne communiquent pas avec le détecteur.**

**Structure des adresses MAC** : chaque trame WiFi contient plusieurs adresses MAC :
- `addr1` : adresse du destinataire
- `addr2` : adresse de l’émetteur (contient l’OUI)
- `addr3` : adresse de la destination ou de la source finale

**RSSI (indicateur de puissance du signal reçu)** : puissance du signal en dBm (décibels négatifs par rapport à un milliwatt). Valeurs typiques :
- -30 dBm : extrêmement puissant (très proche)
- -50 dBm : signal puissant
- -70 dBm : faible, mais utilisable
- -90 dBm : très faible (limite de portée)

**Requêtes de sondage** : les appareils WiFi envoient des requêtes de sondage pour découvrir les réseaux disponibles. *Les sondages génériques (SSID vide) recherchent n’importe quel réseau. Ils sont courants avec les appareils IoT comme les caméras Flock, ce qui les rend facilement détectables.*

______


## Résoudre les problèmes courants

{{< figure src="flockyou-troubleshooting-firmware-flash-flowchart.webp" alt="Organigramme de dépannage du micrologiciel et de la détection FlockYou, des problèmes d’alimentation aux correspondances OUI erronées" >}}

### Problème : aucune détection malgré une caméra connue à proximité

**Causes possibles** :
1. **Caméra hors ligne ou éteinte** : les caméras Flock sont parfois temporairement inactives.
2. **Signal bloqué** : des matériaux comme le métal et le béton absorbent le WiFi.
3. **Hors de portée** : la portée utile est d’environ 100 à 300 pieds selon les obstacles.
4. **Déplacement trop rapide** : le changement de canal favorise une marche lente ou un arrêt plutôt qu’une marche rapide ou la vitesse d’un véhicule.
5. **Problème de micrologiciel** : une version ancienne peut manquer les nouvelles variantes OUI.

**Solutions** :
- Vérifiez que la caméra est visible et semble fonctionner (panneaux solaires, voyants).
- Rapprochez-vous de l’emplacement supposé ou arrêtez-vous 30 à 60 secondes au lieu de passer en marchant.
- Essayez différentes orientations de l’antenne.
- Installez la dernière version du micrologiciel Flock-You.
- **Vérifiez que l’appareil analyse activement les signaux**, notamment l’activité de la LED ou de l’écran.

### Problème : trop de faux positifs

**Causes possibles** :
1. **Forte densité d’appareils ESP32** : les appareils domotiques et IoT sont courants.
2. **Sensibilité trop élevée** : l’appareil détecte des appareils éloignés ou sans intérêt.
3. **Autres caméras de surveillance** : beaucoup utilisent des modules ESP32.

**Solutions** :
- Réduisez la sensibilité.
- Activez la détection des sondages génériques pour augmenter le niveau de confiance.
- Vérifiez physiquement les détections avant de les enregistrer.
- Filtrez selon la puissance du signal et ne déclenchez une alerte que pour les signaux forts.
- Mettez à jour la base OUI pour cibler les OUI Flock confirmés.

### Problème : la batterie se décharge rapidement

**Causes possibles** :
1. **Analyse continue** : aucun mode veille ou gestion d’énergie.
2. **Écran toujours allumé** : l’écran consomme beaucoup d’énergie.
3. **GPS activé** : les modules GPS consomment beaucoup.
4. **Batterie ancienne** : les batteries Li-Po se dégradent avec le temps.

**Solutions** :
- Activez le balayage passif intermittent au lieu de l’analyse continue.
- Réglez la mise en veille de l’écran.
- Désactivez le GPS lorsque la cartographie n’est pas nécessaire.
- Remplacez la batterie (OUI-SPY et mesh-detect v2 ont des batteries remplaçables).
- Utilisez une batterie externe pour les longues sessions.

### Problème : le GPS ne trouve pas de position

**Causes possibles** :
1. **Utilisation en intérieur** : le GPS doit avoir une vue dégagée du ciel.
2. **Antenne non connectée** : mesh-detect v2 nécessite une antenne externe connectée.
3. **Démarrage à froid** : le premier positionnement GPS prend 5 à 15 minutes.
4. **Interférences** : les appareils électroniques à proximité perturbent le signal.

**Solutions** :
- Placez-vous à un endroit où le ciel est dégagé.
- Vérifiez que l’antenne est bien raccordée au connecteur SMA.
- Attendez le premier positionnement, les suivants seront plus rapides.
- Éloignez-vous des sources de brouillage radiofréquence.
- Vérifiez que le GPS est activé dans les paramètres.

### Problème : les données ne sont pas enregistrées sur la carte SD

**Causes possibles** :
1. **Carte SD non formatée** : elle doit être en FAT32 pour assurer la compatibilité.
2. **Carte SD pleine** : il ne reste plus d’espace.
3. **Carte non détectée** : elle n’est pas complètement insérée.
4. **Système de fichiers endommagé** : la carte est défectueuse.

**Solutions** :
- **Formatez la carte SD en FAT32** (32 Go maximum pour assurer la compatibilité).
- Supprimez d’anciens journaux ou utilisez une carte de plus grande capacité.
- Réinsérez complètement la carte jusqu’à son enclenchement.
- Reformatez la carte ou remplacez-la si elle est endommagée.
- Vérifiez que l’appareil reconnaît la carte : le menu affiche son état.

______

## Considérations légales et éthiques

### Statut légal des appareils de détection

**Légalité du balayage Wi-Fi** :
- ✅ **Légal aux États-Unis** : la surveillance Wi-Fi passive, en réception seule, est légale
- ✅ **Aucune interception** : les appareils surveillent uniquement des trames diffusées publiquement
- ✅ **Aucun déchiffrement** : ils ne tentent pas de déchiffrer des données ni de se connecter à un réseau
- ✅ **Comparable aux scanners radio** : leur statut légal est similaire à celui des scanners de police

**Distinctions importantes** :
- ❌ **Illégal** : brouiller activement ou perturber le fonctionnement des caméras
- ❌ **Illégal** : tenter de pirater ou d'accéder aux systèmes de caméras
- ❌ **Illégal** : détruire ou altérer physiquement les caméras
- ⚠️ **Zone grise** : *Certaines juridictions ont des lois de confidentialité plus strictes. Vérifiez les règles locales avant toute utilisation.*

**Recommandation** : **Les appareils servent uniquement à informer. N'interférez pas avec le fonctionnement des caméras.**

### Règles d'utilisation éthique

**Usage responsable** :
- ✅ Utilisez l'appareil pour vous informer sur la surveillance autour de vous
- ✅ Documentez vos observations pour la défense des droits et les débats publics
- ✅ Partagez des données agrégées avec des organisations de protection de la vie privée
- ✅ Contribuez aux projets communautaires de cartographie
- ✅ Sensibilisez le public à l'infrastructure de surveillance

**À éviter** :
- ❌ Utiliser les données pour faciliter des activités illégales
- ❌ Harceler les propriétaires qui ont installé des caméras
- ❌ Entrer sur une propriété pour confirmer l'emplacement d'une caméra
- ❌ Agir en justicier contre l'infrastructure de surveillance

### Protection de la vie privée

**Confidentialité de vos données** :
- **Les appareils enregistrent VOTRE position** à l'aide du GPS
- Stockez ces données en sécurité
- **Pensez au risque de réquisition judiciaire** si vous êtes impliqué dans une procédure
- Envisagez de chiffrer les journaux sensibles
- Consultez les politiques de confidentialité des fournisseurs d'appareils connectés au cloud

**Respect des autres** :
- Soyez attentif lorsque vous utilisez l'appareil dans un espace privé
- Ne l'utilisez pas pour suivre d'autres personnes
- Évaluez les conséquences éthiques du partage des données

______

## Communauté et développement open source

### Contribuer au projet Flock-You

Le projet Flock-You repose sur les contributions de la communauté :

**Dépôt GitHub** : [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**Façons de contribuer** :
1. **Découverte de nouveaux OUI** : soumettez les OUI de caméras Flock récemment identifiés.
2. **Améliorations du code** : proposez des demandes de modification pour améliorer le micrologiciel.
3. **Conception matérielle** : partagez vos propres plans d’appareils de détection.
4. **Documentation** : améliorez les guides d’installation et les traductions.
5. **Tests** : signalez des bogues et vérifiez le fonctionnement sur différents appareils.
6. **Cartographie** : contribuez aux bases de données communautaires des emplacements de caméras.

### Ressources communautaires

**Forums et discussions** :
- **Reddit** : r/privacy, r/privacytoolsIO et discussions actives.
- **Discord** : serveur Colonel Panic Tech et conversations en temps réel.
- **GitHub Issues** : assistance technique et demandes de fonctionnalités.

**Travaux de recherche** :
- Études universitaires sur la surveillance ALPR.
- Évaluations de l’impact sur la vie privée.
- Analyses juridiques de la légalité des appareils de détection.

**Organisations de défense des droits** :
- **Electronic Frontier Foundation** (EFF) : suivi ALPR.
- **ACLU** : surveillance et droits à la vie privée.
- **Groupes locaux** : DeFlockJoplin et initiatives communautaires similaires.

### Feuille de route du développement

**Fonctionnalités prévues** (d’après le GitHub du projet) :
- **Apprentissage automatique** : reconnaissance de motifs pour améliorer la précision.
- **Synchronisation cloud** : base facultative de détections alimentée par la communauté.
- **Applications mobiles** : intégration aux smartphones et interfaces améliorées.
- **Modes de détection supplémentaires** : autres technologies de surveillance.
- **Alertes en temps réel** : notifications push sur réseau mobile ou WiFi.

______

## Conclusion : protéger la vie privée grâce au matériel open source

Le **projet de détection Flock-You** rend le matériel de contre-surveillance accessible à tous les budgets. Vous pouvez choisir le **montage DIY ESP32 ($5–12)**, le **M5 Atom Lite prêt à l'emploi ($49.99)** ou le **OUI-SPY multimode ($85)**. Chaque option transforme la détection des caméras Flock en appareil que vous pouvez assembler en une après-midi.

*Gardez à l'esprit les limites de ce matériel : il détecte les caméras Flock par Wi-Fi. Il ne détecte ni les Stingrays ni les traceurs personnels qui vous suivent. Associez-le à Rayhunter et Eye Spy, présentés ci-dessous, pour élargir cette couverture.*

### Points essentiels

- **Open source et librement modifiable** : le développement communautaire tient à jour la liste OUI et le firmware
- **Matériel abordable** : un ESP32 nu coûte $5–12. Les modèles plus chers ajoutent du confort, pas de nouvelles capacités de détection
- **Surveillance passive uniquement** : l'appareil reçoit des trames Wi-Fi diffusées publiquement et n'émet rien
- **Mises à jour régulières** : les nouvelles signatures OUI et recherches sur les requêtes wildcard sont intégrées au firmware avec l'évolution du matériel Flock
- **Vérifié sur le terrain** : la communauté DeFlockJoplin a détecté 11 des 12 caméras connues lors d'un vrai trajet en voiture

### Étapes suivantes

1. **Lire le contexte** : [Caméras Flock Safety : présence et problèmes de confidentialité](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Choisir une plateforme** : adaptez le montage DIY, le M5 Atom Lite ou l'OUI-SPY à votre budget et à vos compétences
3. **Commander le matériel** : achetez auprès d'un fournisseur autorisé indiqué ci-dessus
4. **Flasher et configurer** : suivez le guide de la plateforme choisie
5. **Rejoindre la communauté** : partagez vos observations et contribuez les détections au projet
6. **Combler les limites de l'appareil** : associez [Rayhunter pour détecter les capteurs IMSI](/articles/how-to-flash-rayhunter-devices-complete-guide/) pour détecter les capteurs IMSI et [Eye Spy pour détecter les AirTags et autres traceurs](/articles/eye-spy-passive-surveillance-detector-esp32-2026/) pour les AirTags et autres traceurs

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acheter un appareil FlockYou prêt à l'emploi, économiser 20 %
{{< /centerbutton >}}

La surveillance ALPR s'étend. Savoir où se trouvent les caméras vous aide à planifier un trajet, documenter un quartier ou contester une installation locale.

______

## Articles connexes

| Article | Résumé |
|---------|-------------|
| **[Surveillance par caméras Flock Safety : déploiement, atteintes à la vie privée et stratégies de protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Guide complet du réseau ALPR de Flock Safety, des abus documentés, des ressources de mobilisation communautaire et des moyens de se protéger |
| **[Flock Finder : repérer les caméras Flock Safety présumées près de chez vous](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Utiliser l’outil open source Flock Finder pour visualiser plus de 40 000 caméras Flock présumées à travers le monde à partir de données WiGLE et d’empreintes OUI |
| **[Eye Spy : détecteur passif de surveillance et de traqueurs à base d’ESP32](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** | Détecteur BLE et WiFi couvrant ce que Flock-You ne détecte pas : AirTags, traceurs Tile, caméras corporelles et drones sur la même famille de matériel |
| **[Flasher Rayhunter sur des appareils de détection d’capteurs IMSI](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Guide détaillé pour installer le micrologiciel Rayhunter et détecter les capteurs IMSI et stingrays sur un point d’accès mobile réutilisé plutôt que sur un ESP32 |
| **[Micrologiciel personnalisé DagShell pour l’Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Guide complet d’installation de DagShell sur l’Orbic RCL400 pour surveiller les réseaux mobiles et détecter des capteurs IMSI |
| **[Comparatif des appareils Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparaison des appareils compatibles avec Rayhunter pour choisir le matériel adapté à votre ensemble d’outils de contre-surveillance |

*Vous cherchez un outil qui neutralise activement les traceurs au lieu de seulement les détecter ? [Simulacra](https://github.com/Em3ritus/simulacra) est un projet open source indépendant qui sème des appareils BLE et WiFi leurres dans la zone afin de masquer le signal de votre appareil. Il répond à un autre besoin que les appareils de ce guide et peut être utile si la détection passive ne suffit pas à votre modèle de menace.*

______

## Références

1. [Dépôt GitHub de Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - carte interactive des caméras ALPR](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - dépôt GitHub](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - site officiel du fournisseur](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite avec micrologiciel préinstallé](https://stscollective.com)
6. [Documentation officielle du M5Stack Atom Lite](https://docs.m5stack.com/en/core/ATOM%20Lite)
7. [Documentation de l’API WiFi ESP32 d’Espressif](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html)
8. [Référence des requêtes et réponses Probe 802.11](https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/)
9. [DeFlock Joplin - recherche communautaire sur l’ALPR](https://deflockjoplin.today)
10. [DeFlock - carte et données ALPR participatives](https://deflock.me/)
11. [Electronic Frontier Foundation - qu’est-ce que l’ALPR ?](https://www.eff.org/pages/what-alpr)
12. [Téléchargement officiel de l’Arduino IDE](https://www.arduino.cc/en/software)
13. [Documentation de Platform.io](https://docs.platformio.org/)
14. [IEEE Registration Authority - grand bloc d’adresses MAC (OUI)](https://standards.ieee.org/products-programs/regauth/oui/)
15. [Référence de la structure des trames Beacon 802.11](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
