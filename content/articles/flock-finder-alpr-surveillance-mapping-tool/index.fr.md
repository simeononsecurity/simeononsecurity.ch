---
title: "Flock Finder : outil open source pour cartographier les caméras de surveillance ALPR Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder est un outil open source qui cartographie plus de 40 000 caméras ALPR Flock Safety dans le monde en utilisant les données WiFi WiGLE et le fingerprinting OUI. Découvrez son fonctionnement, ses limites et les outils matériels pour la détection en temps réel."
genre: ["Technologie de confidentialité", "Contre-surveillance", "Projets open source", "Droits numériques", "Sécurité réseau", "Outils de confidentialité", "Bidouillage matériel", "Recherche en sécurité"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "lecteur de plaques", "fingerprinting OUI", "WiGLE", "surveillance WiFi", "contre-surveillance", "STS Collective", "FlockYou", "ESP32", "outils de confidentialité", "NitekryDPaul", "DeFlockJoplin", "détection ALPR", "sécurité open source", "cartographie de surveillance", "surveillance de masse", "OUI WiFi", "protection de la vie privée", "adresse MAC", "mode promiscuité", "802.11", "détection en temps réel", "wardriving", "droits numériques", "libertés civiles", "sensibilisation à la surveillance", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Une carte interactive affichant des marqueurs colorés indiquant les emplacements des caméras ALPR Flock Safety, avec des signaux WiFi abstraits émanant des marqueurs sur un fond sombre."
coverCaption: "Flock Finder cartographie plus de 40 000 caméras ALPR Flock Safety suspectées en utilisant les données WiFi WiGLE et le fingerprinting OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Un outil de sensibilisation à la surveillance open source qui cartographie les caméras ALPR Flock Safety en utilisant des données WiFi participatives.**

## Qu'est-ce que Flock Finder ?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** est un projet open source qui cartographie les **caméras ALPR (lecteur automatique de plaques d'immatriculation) Flock Safety** aux États-Unis et dans 108 autres pays. Il combine **31 préfixes OUI (Organizationally Unique Identifier) WiFi Flock Safety connus** avec la **base de données WiFi participative WiGLE** pour identifier et représenter les emplacements suspectés de caméras sur une carte interactive.

Le projet se trouve sur **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, se met à jour automatiquement chaque jour via GitHub Actions et, en juillet 2026, a cartographié **plus de 40 000 caméras suspectées** dans 964 régions à travers le monde.

| Métrique | Valeur |
|--------|-------|
| **Caméras cartographiées** | 40 026+ |
| **Préfixes OUI connus** | 31 |
| **Pays couverts** | 109 |
| **Régions couvertes** | 964 |
| **Conservation des données** | 730 jours (2 ans) |
| **Fréquence de mise à jour automatique** | Quotidienne |

*Il s'agit d'un outil de sensibilisation générale, pas d'un inventaire définitif. Lisez la section sur les limites avant de tirer des conclusions des données.*

______

## Comment ça fonctionne : fingerprinting OUI via WiGLE

### L'idée centrale

Les caméras Flock Safety contiennent des **émetteurs-récepteurs WiFi** qui se réveillent périodiquement pour télécharger les données de plaques capturées vers le cloud. Pendant ces brèves fenêtres actives, la caméra diffuse des trames WiFi contenant son **adresse MAC**. Les trois premiers octets de chaque adresse MAC identifient le fabricant. C'est l'**OUI (Organizationally Unique Identifier)**.

Le chercheur en sécurité **@NitekryDPaul** a découvert **30 préfixes OUI** constamment associés au matériel des caméras Flock Safety grâce à l'**analyse en mode promiscuité sur 2,4 GHz**. Un 31e préfixe (`82:6B:F2`) a été contribué par **Michael / DeFlockJoplin** lors de tests de terrain à Joplin, MO.

Flock Finder prend ces 31 OUI, interroge WiGLE pour tous les réseaux WiFi enregistrés correspondant à ces préfixes, et représente les résultats sur une carte.

### La technique de détection addr1

La découverte clé de @NitekryDPaul va au-delà de la simple correspondance sur l'adresse MAC de l'émetteur. Les caméras Flock passent la majeure partie de leur cycle de service en **veille**. Lorsqu'un point d'accès à proximité envoie une trame adressée *à* une caméra, l'adresse MAC de la caméra apparaît comme **addr1 (l'adresse du destinataire)** dans les trames 802.11, même lorsque la caméra elle-même ne transmet pas activement.

Combinée à la **détection de requêtes sonde génériques** (trames de gestion 802.11 type=0, sous-type=4, SSID vide), cette méthode produit une signature de détection très précise. Les tests de terrain à Joplin, MO ont permis **de détecter 11 caméras sur 12 avec seulement 2 faux positifs**.

> ⚠️ **Important** : la carte Flock Finder basée sur WiGLE n'implémente **pas** la technique addr1. WiGLE est un ensemble de données historiques, collecté passivement. Il n'enregistre que les émetteurs, pas les récepteurs. Pour la détection en temps réel utilisant réellement la méthode de @NitekryDPaul, vous avez besoin d'un matériel dédié sur le terrain.

______

## Utiliser la carte en direct

La carte interactive est disponible en direct sur **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Elle affiche :

- **Marqueurs de caméras groupés** codés par couleur selon le préfixe OUI
- **Recherche** par ville, état ou BSSID
- **Tableau de données OUI** avec le nombre de caméras par préfixe
- **Panneau de statistiques** affichant le total des caméras, des régions et l'horodatage de la dernière mise à jour
- **Page sur les ALPR** avec les préjudices documentés pour la vie privée, le contexte juridique et les ressources communautaires

Les exports de données de la carte sont également disponibles directement :

- `data/flock_cameras.geojson` — GeoJSON pour utilisation dans QGIS, Leaflet ou d'autres outils
- `data/flock_cameras.csv` — format compatible avec les tableurs
- `data/scan_stats.json` — statistiques et comptages des scans

### Limites importantes

**Prenez la carte avec du recul.** WiGLE est un ensemble de données participatif et sporadiquement mis à jour, pas un flux en direct.

- **Les caméras Flock ne diffusent pas en permanence.** Elles se réveillent brièvement pour télécharger des données, donc les enregistrements WiGLE dépendent entièrement d'un wardriver se trouvant à proximité exactement au bon moment.
- **Les données peuvent dater de plusieurs mois ou années.** Des caméras déplacées ou retirées peuvent encore apparaître.
- **La correspondance OUI est une heuristique.** Les OUI peuvent être partagés, réaffectés ou falsifiés. Chaque résultat est un appareil Flock *suspecté*, pas confirmé.
- **La couverture est inégale.** Les zones métropolitaines denses ont plus de données WiGLE ; les zones rurales en ont beaucoup moins.

*Utilisez la carte pour développer une sensibilisation générale à la densité de surveillance dans votre zone. Pour une détection en temps réel basée sur des données terrain, consultez les options matérielles ci-dessous.*

______

## Exécuter Flock Finder vous-même

### Prérequis

- Python 3.8+
- Un compte [WiGLE](https://wigle.net/account) gratuit avec des identifiants API

### Configuration

```bash
# Cloner le dépôt
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Installer les dépendances
pip install -r requirements.txt

# Configurer vos identifiants API WiGLE
cp .env.example .env
# Modifiez .env avec votre nom API WiGLE et votre token
```

### Exécuter le scanner

```bash
# Scan complet — tous les 31 préfixes OUI, dans le monde entier
python3 scripts/wigle_query.py

# Test OUI unique
python3 scripts/wigle_query.py --oui 70:C9:4E

# États-Unis uniquement
python3 scripts/wigle_query.py --country US

# Boîte englobante spécifique (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Simulation — vérifier l'auth, sans requêtes API
python3 scripts/wigle_query.py --dry-run
```

### Afficher la carte localement

```bash
python3 -m http.server 8080 --directory docs/
# Ouvrir http://localhost:8080 dans votre navigateur
```

### Mises à jour quotidiennes automatiques via GitHub Actions

Forkez le dépôt et ajoutez vos identifiants WiGLE comme **secrets du dépôt** (`WIGLE_API_NAME` et `WIGLE_API_TOKEN`). Le workflow inclus s'exécute à 6h UTC chaque jour et valide automatiquement les fichiers de données mis à jour lorsque de nouvelles caméras sont trouvées.

______

## Détection en temps réel : matériel FlockYou de STS Collective

La carte WiGLE vous indique où les caméras *ont été observées*. Pour la détection en temps réel pendant que vous conduisez, en utilisant la méthode de correspondance OUI de @NitekryDPaul sur du trafic WiFi en direct, vous avez besoin de matériel dédié.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** fabrique des détecteurs portables basés sur ESP32 qui recherchent les signatures OUI Flock et vous alertent dès qu'une signature correspondante est détectée.

### Gamme de produits FlockYou

| Appareil | Description |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Détecteur Flock compact, format poche. Pré-flashé, plug-and-play. Alertes LED à la détection. |
| **FlockYou Pro — LED + Audio** | Ajoute des alertes audio en plus des indicateurs LED. Ne manquez jamais une caméra en conduisant. |
| **FlockYou Atom VoiceS3R** | Détecteur vocal avec alertes audio parlées pour une utilisation mains libres, yeux sur la route. |

Tous les appareils :
- **Pré-flashés**, prêts à l'emploi
- Analysent le trafic WiFi en direct pour les 31 OUI Flock connus
- Compacts et portables — tiennent dans un porte-gobelet ou une poche
- Alimentés via USB-C (adaptateur voiture, batterie externe ou ordinateur portable)

> 💰 **Réductions exclusives** : utilisez le code **FLOCKFINDER** pour **20% de réduction** sur tous les appareils FlockYou de STS Collective, ou utilisez le code **SIMEONONSECURITY** pour jusqu'à 20% de réduction sur toute votre commande. [Achetez sur stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Structure du projet

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # Requête API WiGLE et pipeline de données
├── data/
│   ├── flock_ouis.csv         # 31 préfixes OUI Flock Safety connus
│   ├── flock_cameras.geojson  # Emplacements des caméras (GeoJSON)
│   ├── flock_cameras.csv      # Emplacements des caméras (CSV)
│   └── scan_stats.json        # Statistiques des scans
├── docs/
│   └── index.html             # Carte interactive Leaflet
└── .github/workflows/
    └── update-data.yml        # Workflow de mise à jour automatique quotidien
```

______

## Questions fréquentes

### Est-ce légal ?

Oui. **Flock Finder utilise uniquement des données publiquement disponibles** de la base de données WiGLE, qui agrège des données d'enquête WiFi contribuées volontairement. Aucun piratage, accès non autorisé ou système propriétaire n'est impliqué. La surveillance WiFi passive pour les signatures OUI est légale aux États-Unis.

### Chaque caméra cartographiée est-elle définitivement une caméra Flock ?

Non. La correspondance OUI est une **heuristique**. Les préfixes OUI peuvent être partagés entre fabricants, réaffectés ou falsifiés. Chaque entrée dans la base de données est un appareil Flock *suspecté*, pas confirmé.

### Pourquoi certains préfixes OUI ne montrent-ils aucune caméra ?

La couverture WiGLE est inégale. Si aucun wardriver n'a analysé une zone donnée avec cet OUI spécifique actif, il n'y aura pas d'enregistrements. *L'absence de données ne signifie pas l'absence de caméras.*

### Quelle est la fraîcheur des données ?

Le workflow GitHub Actions s'exécute quotidiennement et récupère les derniers résultats WiGLE. Cependant, WiGLE lui-même peut avoir des enregistrements allant de quelques jours à plusieurs années pour un emplacement donné. Consultez le fichier `scan_stats.json` pour l'horodatage du scan le plus récent.

### Puis-je contribuer mes propres données de wardrive ?

Oui. Téléchargez vos données de wardrive sur [WiGLE](https://wigle.net). Elles alimentent automatiquement le prochain scan quotidien de Flock Finder. Vous pouvez également contribuer des préfixes OUI ou des améliorations de code via le [Guide de contribution](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Communauté et projets connexes

Flock Finder n'est pas seul. Un écosystème croissant d'outils et d'organisations travaille à documenter et contrer la surveillance ALPR :

- **[DeFlock.org](https://deflockjoplin.org/)** — Suivi de l'ALPR par la communauté, documentation et plaidoyer
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Vérifiez si votre plaque a été recherchée dans le système Flock
- **[FlockHopper](https://flockhopper.com/)** — Planification d'itinéraire évitant les caméras ALPR connues
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Base de données de l'EFF sur les technologies de surveillance utilisées par les forces de l'ordre
- **[NoALPRs.com](https://noalprs.com/)** — Ressources pour les communautés luttant contre les déploiements ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Firmware open source et recherche de terrain ; a contribué le 31e préfixe OUI

______

## Crédits

- **Recherche OUI** : @NitekryDPaul — les 30 préfixes OUI originaux et la stratégie de détection addr1/mode promiscuité
- **Tests de terrain** : Michael / DeFlockJoplin — 31e préfixe OUI (`82:6B:F2`) et affinement de la sonde générique
- **Source de données** : [WiGLE](https://wigle.net) — base de données WiFi/réseaux cellulaires participative
- **Inspiré par** : [DeFlock](https://deflockjoplin.org/) et track-openroaming-passpoint
- **Partenaire matériel** : [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — détecteurs FlockYou ESP32

______

## Conclusion

**Flock Finder** donne à chacun une idée rapide et visuelle de l'ampleur du déploiement des caméras ALPR Flock Safety : plus de 40 000 emplacements estimés dans 109 pays, mis à jour automatiquement chaque jour à partir de données WiFi participatives.

C'est un **outil de transparence**, pas un traceur en direct. Ses données sont historiques, incomplètes et probabilistes. Mais il rend visible l'échelle de la surveillance ALPR d'une manière que les abstraits et les rapports ne peuvent pas.

Pour une protection réelle en temps réel lorsque vous traversez des zones surveillées, associez la carte à du matériel dédié. **[Les appareils FlockYou de STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implémentent la méthode de détection de @NitekryDPaul directement sur un ESP32 et vous alertent dès qu'une signature de caméra en direct est détectée. Disponibles sur **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** avec le code **FLOCKFINDER** ou **SIMEONONSECURITY** pour jusqu'à 20% de réduction.

______

## Références

1. [Dépôt GitHub Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Carte interactive Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — appareils FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — cartographie des réseaux sans fil](https://wigle.net)
5. [DeFlock — sensibilisation communautaire à l'ALPR](https://deflockjoplin.org/)
6. [DeFlockJoplin — firmware de détection open source](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Vous êtes suivi](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
