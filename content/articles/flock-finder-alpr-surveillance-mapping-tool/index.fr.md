---
title: "Flock Finder : Carte des caméras ALPR Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder est un outil open-source qui cartographie plus de 40 000 caméras Flock Safety ALPR dans le monde entier en utilisant les données WiFi de WiGLE et l'empreinte OUI. Découvrez comment il fonctionne, ses limites et les outils matériels pour la détection en temps réel."
genre: ["Technologie de confidentialité", "Contre-surveillance", "Projets open-source", "Droits numériques", "Sécurité des réseaux", "Outils de confidentialité", "Piratage matériel", "Recherche en sécurité"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Lecteur de plaques d'immatriculation", "Empreinte OUI", "WiGLE", "Surveillance WiFi", "Contre-surveillance", "STS Collective", "FlockYou", "ESP32", "Outils de confidentialité", "NitekryDPaul", "DeFlockJoplin", "Détection ALPR", "Sécurité open-source", "Cartographie de surveillance", "Surveillance de masse", "WiFi OUI", "Protection de la vie privée", "Adresse MAC", "Mode promiscuité", "802.11", "Détection en temps réel", "Wardriving", "Droits numériques", "Libertés civiles", "Sensibilisation à la surveillance", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Une carte interactive affichant des marqueurs colorés indiquant les emplacements des caméras Flock Safety ALPR, avec des signaux WiFi abstraits émanant des marqueurs sur un fond sombre."
coverCaption: "Flock Finder cartographie plus de 40 000 caméras Flock Safety ALPR présumées en utilisant les données WiFi de WiGLE et l'empreinte OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Un outil open-source de sensibilisation à la surveillance qui cartographie les caméras Flock Safety ALPR à l'aide de données WiFi participatives.**

## Qu'est-ce que Flock Finder ?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** est un projet open-source qui cartographie les **caméras Flock Safety ALPR (Lecteur Automatique de Plaques d'Immatriculation)** aux États-Unis et dans 108 autres pays. Il combine **31 préfixes OUI (Identificateur Unique Organisationnel) WiFi de Flock Safety connus** avec la **base de données WiFi participative WiGLE** pour identifier et représenter les emplacements présumés de caméras sur une carte interactive.

Le projet est hébergé sur **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, se met à jour automatiquement chaque jour via GitHub Actions et, en juillet 2026, a cartographié **plus de 40 000 caméras présumées** dans 964 régions du monde entier.

| Métrique | Valeur |
|--------|-------|
| **Caméras cartographiées** | 40 026+ |
| **Préfixes OUI connus** | 31 |
| **Pays couverts** | 109 |
| **Régions couvertes** | 964 |
| **Conservation des données** | 730 jours (2 ans) |
| **Fréquence de mise à jour automatique** | Quotidiennement |

*Il s'agit d'un outil de sensibilisation générale, pas d'un inventaire définitif. Lisez la section sur les limitations avant de tirer des conclusions des données.*

Pour comprendre pourquoi la surveillance ALPR de Flock Safety est importante pour la vie privée, lisez **[Surveillance par caméras Flock Safety : Prévalence, problèmes de confidentialité et stratégies de protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## Comment ça fonctionne : Empreinte OUI via WiGLE

### L'idée centrale

Les caméras Flock Safety contiennent des **émetteurs-récepteurs WiFi** qui se réveillent périodiquement du sommeil pour télécharger les données de plaques d'immatriculation capturées vers le cloud. Pendant ces brèves fenêtres actives, la caméra émet des trames WiFi contenant son **adresse MAC** — et les trois premiers octets de chaque adresse MAC identifient le fabricant. C'est l'**OUI (Identificateur Unique Organisationnel)**.

Le chercheur en sécurité **@NitekryDPaul** a découvert **30 préfixes OUI** systématiquement associés au matériel des caméras Flock Safety grâce à une **analyse 2,4 GHz en mode promiscuité**. Un 31e préfixe (`82:6B:F2`) a été contribué par **Michael / DeFlockJoplin** lors des tests terrain à Joplin, MO.

Flock Finder prend ces 31 OUIs, interroge WiGLE pour trouver des réseaux WiFi enregistrés correspondant à ces préfixes et représente les résultats sur une carte.

### Les 31 préfixes OUI connus de Flock Safety

| # | Préfixe OUI | Source | # | Préfixe OUI | Source |
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

### La technique de détection addr1

La découverte clé de @NitekryDPaul va au-delà de la simple correspondance sur l'adresse MAC de l'émetteur. Les caméras Flock passent la majeure partie de leur cycle de fonctionnement **en veille**. Lorsqu'un point d'accès voisin envoie une trame adressée *à* une caméra, la MAC de la caméra apparaît comme **addr1 (l'adresse du récepteur)** dans les trames 802.11 — même lorsque la caméra elle-même ne transmet pas activement.

Combiné avec la **détection de requêtes de sonde wildcard** (trames de gestion 802.11 type=0, sous-type=4, SSID vide), cela donne une signature de détection très précise. Les tests terrain à Joplin, MO ont permis de **détecter 11 caméras sur 12 avec seulement 2 faux positifs**.

> ⚠️ **Important** : La carte Flock Finder basée sur WiGLE **n'implémente pas** la technique addr1. WiGLE est un ensemble de données historiques, collectées passivement — il enregistre uniquement les émetteurs, pas les récepteurs. Pour une détection en temps réel utilisant réellement la méthode de @NitekryDPaul, vous avez besoin d'un matériel dédié déployé sur le terrain.

______

## Utilisation de la carte en direct

La carte interactive est disponible sur **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Elle affiche :

- **Marqueurs de caméra regroupés** codés par couleur selon le préfixe OUI
- **Recherche** par ville, état ou BSSID
- **Tableau de données OUI** avec le nombre de caméras par préfixe
- **Panneau de statistiques** affichant le total des caméras, des régions et l'horodatage de la dernière mise à jour
- **Page sur les ALPR** avec les atteintes documentées à la vie privée, le contexte juridique et les ressources communautaires

Les exports de données de la carte sont également disponibles directement :

- `data/flock_cameras.geojson` — GeoJSON pour utilisation dans QGIS, Leaflet ou d'autres outils
- `data/flock_cameras.csv` — format compatible avec les tableurs
- `data/scan_stats.json` — statistiques et comptages de scan

### Limitations clés

**Prenez la carte avec précaution.** WiGLE est un ensemble de données participatif, mis à jour sporadiquement, pas un flux en direct.

- **Les caméras Flock ne transmettent pas continuellement.** Elles se réveillent brièvement pour télécharger des données, donc les enregistrements WiGLE dépendent entièrement d'un conducteur wardriver se trouvant à proximité exactement au bon moment.
- **Les données peuvent avoir des mois ou des années d'ancienneté.** Les caméras qui ont été déplacées ou supprimées peuvent encore apparaître.
- **La correspondance OUI est une heuristique.** Les OUIs peuvent être partagés, réassignés ou usurpés. Chaque résultat est un appareil Flock *présumé*, pas confirmé.
- **La couverture est inégale.** Les zones métropolitaines denses ont plus de données WiGLE ; les zones rurales en ont beaucoup moins.

*Utilisez la carte pour développer une conscience générale de la densité de surveillance dans votre région. Pour une détection en temps réel avec des données terrain, consultez les options matérielles ci-dessous.*

______

## Exécuter Flock Finder vous-même

### Prérequis

- Python 3.8+
- Un compte [WiGLE](https://wigle.net/account) gratuit avec des identifiants API

### Configuration

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

### Exécution du scanner

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

### Visualiser la carte localement

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### Mises à jour quotidiennes automatisées via GitHub Actions

Forkez le dépôt et ajoutez vos identifiants WiGLE comme **secrets du dépôt** (`WIGLE_API_NAME` et `WIGLE_API_TOKEN`). Le workflow inclus s'exécute à 6h00 UTC quotidiennement et valide automatiquement les fichiers de données mis à jour chaque fois que de nouvelles caméras sont trouvées.

______

## Détection en temps réel : Matériel STS Collective FlockYou

La carte WiGLE vous indique où des caméras *ont été observées*. Pour une détection en temps réel pendant la conduite — en utilisant la véritable méthode de correspondance OUI de @NitekryDPaul sur le trafic WiFi en direct — vous avez besoin d'un matériel dédié.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** fabrique des détecteurs portables basés sur ESP32 qui recherchent les signatures OUI de Flock et vous alertent au moment où une signature correspondante est détectée.

### Gamme de dispositifs FlockYou

| Dispositif | Description |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Détecteur Flock compact, de poche. Pré-flashé, plug-and-play. Alertes LED lors de la détection. |
| **FlockYou Pro — LED + Audio** | Ajoute des alertes audio en plus des indicateurs LED. Ne manquez jamais une caméra en conduisant. |
| **FlockYou Atom VoiceS3R** | Détecteur vocal avec alertes audio parlées pour une utilisation mains libres, yeux sur la route. |

Tous les appareils :
- **Pré-flashés**, prêts à l'emploi dès la sortie de la boîte
- Analysent le trafic WiFi en direct pour tous les 31 OUIs Flock connus
- Compacts et portables — s'adaptent à un porte-gobelet ou une poche
- Alimentés via USB-C (adaptateur voiture, batterie externe ou ordinateur portable)

> 💰 **Réductions exclusives** : Utilisez le code **FLOCKFINDER** pour **20% de réduction** sur tous les appareils STS Collective FlockYou — ou utilisez le code **SIMEONONSECURITY** pour jusqu'à 20% de réduction sur toute votre commande. [Achetez sur stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Pour une analyse technique complète de ces appareils et des alternatives DIY, lisez le **[Projet de Détection Flock-You : Guide complet du matériel de contre-surveillance et de configuration](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Structure du projet

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

## Questions fréquemment posées

### Est-ce légal ?

Oui. **Flock Finder utilise uniquement des données accessibles au public** de la base de données WiGLE, qui agrège des données d'enquête WiFi contribuées volontairement. Aucun piratage, accès non autorisé ou système propriétaire n'est impliqué. La surveillance WiFi passive pour les signatures OUI est légale aux États-Unis.

### Chaque caméra cartographiée est-elle définitivement une caméra Flock ?

Non. La correspondance OUI est une **heuristique**. Les préfixes OUI peuvent être partagés entre fabricants, réassignés ou usurpés. Chaque enregistrement dans la base de données est un appareil Flock *présumé* — pas confirmé. Lisez la [Politique de données](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) pour plus de détails sur la façon de demander une correction.

### Pourquoi certains préfixes OUI ne montrent-ils aucune caméra ?

La couverture WiGLE est inégale. Si aucun wardriver n'a scanné une zone donnée avec cet OUI spécifique actif, il n'y aura aucun enregistrement. *L'absence de données ne signifie pas l'absence de caméras.*

### Dans quelle mesure les données sont-elles à jour ?

Le workflow GitHub Actions s'exécute quotidiennement et récupère les derniers résultats WiGLE. Cependant, WiGLE lui-même peut avoir des enregistrements allant de quelques jours à plusieurs années pour n'importe quel emplacement donné. Vérifiez le fichier `scan_stats.json` pour l'horodatage du scan le plus récent.

### Puis-je contribuer avec mes propres données de wardrive ?

Oui. Téléchargez vos données de wardrive sur [WiGLE](https://wigle.net) — elles sont automatiquement intégrées dans le prochain scan quotidien de Flock Finder. Vous pouvez également contribuer des préfixes OUI ou des améliorations de code via le [Guide de contribution](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Communauté et projets connexes

Flock Finder n'agit pas seul. Un écosystème croissant d'outils et d'organisations travaille à documenter et à contrer la surveillance ALPR :

- **[DeFlock.org](https://deflockjoplin.org/)** — Suivi, documentation et plaidoyer ALPR pilotés par la communauté
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Vérifiez si votre plaque a été recherchée dans le système Flock
- **[FlockHopper](https://flockhopper.com/)** — Planification d'itinéraires évitant les caméras ALPR connues
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Base de données de l'EFF sur les technologies de surveillance utilisées par les forces de l'ordre
- **[NoALPRs.com](https://noalprs.com/)** — Ressources pour les communautés luttant contre les déploiements d'ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Firmware open-source et recherche terrain ; a contribué le 31e préfixe OUI

______

## Crédits

- **Recherche OUI** : @NitekryDPaul — tous les 30 préfixes OUI originaux et la stratégie de détection addr1/mode promiscuité
- **Tests terrain** : Michael / DeFlockJoplin — 31e préfixe OUI (`82:6B:F2`) et resserrement des sondes wildcard
- **Source de données** : [WiGLE](https://wigle.net) — base de données WiFi/réseau cellulaire participative
- **Inspiré par** : [DeFlock](https://deflockjoplin.org/) et track-openroaming-passpoint
- **Partenaire matériel** : [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — détecteurs FlockYou ESP32

______

## Conclusion

**Flock Finder** donne à n'importe qui une idée rapide et visuelle de l'ampleur du déploiement des caméras Flock Safety ALPR — plus de 40 000 emplacements estimés dans 109 pays, mis à jour automatiquement chaque jour à partir de données WiFi participatives.

C'est un **outil de transparence**, pas un tracker en direct. Ses données sont historiques, incomplètes et probabilistes. Mais il rend visible l'échelle de la surveillance ALPR d'une manière que les résumés et les rapports ne peuvent pas faire.

Pour une véritable protection en temps réel lors de vos déplacements dans des zones surveillées, associez la carte à du matériel dédié. **[Les appareils FlockYou de STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implémentent la méthode de détection de @NitekryDPaul directement sur un ESP32 et vous alertent au moment où une signature de caméra en direct est détectée — disponibles sur **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** avec le code **FLOCKFINDER** ou **SIMEONONSECURITY** pour jusqu'à 20% de réduction.

### Articles connexes

| Article | Ce qu'il couvre |
|---------|---------------|
| **[Surveillance par caméras Flock Safety : Confidentialité et protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Le tableau complet : statistiques de prévalence, questions de libertés civiles, kit d'outils ACLU, statistiques DeFlock, guide FOIA et stratégies de protection |
| **[Projet de Détection Flock-You : Guide du matériel de contre-surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guide technique complet des détecteurs Flock basés sur ESP32 — OUI-SPY, M5 Atom Lite, construction DIY, configuration du firmware étape par étape |
| **[Comment flasher les appareils Rayhunter : Guide complet](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Détecter les capteurs IMSI (simulateurs de stations de base cellulaires) aux côtés des caméras ALPR pour une sensibilisation complète à la contre-surveillance |
| **[Firmware personnalisé DagShell pour Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Transformer un point d'accès mobile en plateforme de recherche en sécurité — se couple bien avec le matériel de détection Flock |
| **[Comparaison des appareils Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparer les options de matériel de détection entre les catégories de menaces ALPR et de surveillance cellulaire |

______

## Références

1. [Dépôt GitHub de Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Carte interactive de Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — Appareils FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Cartographie des réseaux sans fil](https://wigle.net)
5. [DeFlock — Sensibilisation communautaire aux ALPR](https://deflockjoplin.org/)
6. [DeFlockJoplin — Firmware de détection open-source](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Vous êtes suivi](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
