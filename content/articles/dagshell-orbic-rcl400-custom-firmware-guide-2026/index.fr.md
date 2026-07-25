---
title: "Firmware personnalisé DagShell pour Orbic RCL400 : Guide complet d'installation et d'utilisation 2026"
date: 2026-05-28
toc: true
draft: false
description: "Guide complet du firmware personnalisé DagShell pour le hotspot Orbic RCL400, incluant l'installation, les outils de confidentialité, les fonctionnalités de hacking, les capacités de wardriving et pourquoi il se combine parfaitement avec RayHunter pour la recherche en sécurité mobile."
genre: ["Firmware personnalisé", "Sécurité mobile", "Outils de confidentialité", "Sécurité réseau", "Wardriving", "Tests d'intrusion", "Hacking IoT", "Recherche en sécurité", "Hacking matériel", "Technologie de confidentialité"]
tags: ["DagShell", "Orbic RCL400", "Firmware personnalisé", "Hacking hotspot", "Outils de confidentialité", "Correction TTL", "Usurpation MAC", "Détection IMSI Catcher", "Wardriving", "Suivi GPS", "Attaque Evil Twin", "Portail captif", "Renifleur DNS", "Scanner ARP", "Scanner de ports", "Raspberry Pi Companion", "Sécurité WiFi", "Hotspot mobile", "Surveillance réseau", "Tests d'intrusion", "Recherche en sécurité", "Scan Bluetooth", "Attaque Deauth", "Scan WiFi", "Recherche OUI", "Upload Wigle", "Surveillance tour cellulaire", "Commandes AT", "Gestionnaire pare-feu", "AdBlock", "Chiffrement TLS", "Intégration RayHunter", "STS Collective", "Laboratoire de sécurité mobile", "Analyse réseau", "Firmware confidentialité", "Sécurité open source", "Compilation croisée ARM", "Linux embarqué", "Boîte à outils de sécurité", "Outils hacker", "Red Team", "Reconnaissance réseau"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Une illustration d'un hotspot mobile Orbic RCL400 avec une interface verte lumineuse, entourée de représentations abstraites d'outils de sécurité comme des graphiques et des cartes, sur fond bleu marine foncé."
coverCaption: ""
---

**Transformez votre Orbic RCL400 en laboratoire de recherche en sécurité mobile**

## Introduction : Un hotspot pour hackers

**DagShell** est un firmware personnalisé open source pour le **hotspot mobile Orbic RCL400** qui transforme un appareil cellulaire ordinaire en **boîte à outils portable de recherche en sécurité et de confidentialité**. Créé par le chercheur en sécurité "dag", ce firmware au style terminal fournit des **outils de hacking, des fonctionnalités de confidentialité et des capacités de surveillance réseau** dans une interface élégante avec une esthétique hacker vert sur noir.

Ce guide complet couvre :
- **Ce qu'est DagShell** et son ensemble complet de fonctionnalités
- **Instructions d'installation** étape par étape (méthodes webflasher et manuelle)
- **Tous les outils et capacités** expliqués en détail
- **Configuration du Raspberry Pi companion** pour des fonctionnalités étendues
- **Pourquoi combiner DagShell avec RayHunter** pour une sécurité mobile optimale
- **Cas d'utilisation réels** pour les chercheurs en sécurité et les défenseurs de la vie privée
- **Considérations légales et éthiques**

**En bref** : DagShell + RayHunter sur Orbic RCL400 = **Laboratoire de sécurité mobile complet** pour la détection d'IMSI catchers, le wardriving, l'analyse réseau et la protection de la vie privée.

**Appareils pré-flashés disponibles** : Cet article est sponsorisé par **STS Collective**, qui propose des hotspots Orbic RCL400 pré-flashés avec **RayHunter et DagShell** préinstallés et prêts à l'emploi : [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Réduction exclusive lecteurs** : Économisez jusqu'à 20% sur les produits STS Collective, y compris les appareils Orbic RCL400 pré-flashés - utilisez le code **SIMEONONSECURITY** à la caisse ou [achetez avec la réduction appliquée](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Qu'est-ce que DagShell ?

### Vue d'ensemble

**DagShell** est un firmware personnalisé open source qui remplace l'interface web standard de l'Orbic RCL400 par une **boîte à outils de sécurité complète** comprenant :

- **Interface de style terminal** avec art ASCII et esthétique hacker
- Interface web **chiffrée TLS 1.2+** (certificat auto-signé)
- **Outils de protection de la vie privée** (masquage TTL, usurpation MAC, blocage de publicités DNS)
- **Surveillance réseau** (connexions actives, tables de routage, requêtes DNS)
- **Outils de hacking** (détection d'IMSI catcher, scan de ports, découverte ARP)
- **Capacités d'attaque** (Evil Twin AP, phishing portail captif, attaques deauth)
- **Suivi GPS et wardriving** avec export CSV compatible Wigle
- **Raspberry Pi companion** pour GPS, scan Bluetooth et reconnaissance WiFi
- **Accès au système de fichiers** avec gestionnaire de fichiers dans le navigateur
- **Fonctionnalité SMS** via commandes AT
- **Persistance** - Démarrage automatique au démarrage

### Spécifications techniques

**Plateforme** : Hotspot mobile Orbic RCL400
**Architecture** : ARM Linux (noyau 3.18)
**Langage** : C/C++ (binaire ARM statique)
**Chiffrement** : TLS 1.2+ avec certificats auto-signés (PKI à 2 niveaux)
**Serveur web** : Serveur HTTPS embarqué personnalisé (port 8443)
**Interface** : Interface utilisateur terminal basée sur navigateur
**Licence** : MIT (open source)
**GitHub** : [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

______

## Description complète des fonctionnalités

### Suite de protection de la vie privée

#### Correction TTL

**Objectif** : Masquer le trafic du hotspot de la détection par l'opérateur

**Fonctionnement** :
- Modifie la valeur **Time To Live (TTL)** dans les paquets IP à **65**
- Les opérateurs détectent le tethering par les décréments TTL (téléphone=64, appareil connecté=63)
- Régler le TTL à 65 fait apparaître **tout le trafic comme local**

**Cas d'utilisation** : Contourner les restrictions/limitation du tethering de l'opérateur

#### Usurpation d'adresse MAC

**Objectif** : Randomiser l'adresse MAC de l'appareil pour la confidentialité

**Fonctionnement** :
- Change l'adresse MAC de **wlan0** (interface WiFi)
- Génère une **MAC aléatoire** ou permet une entrée personnalisée
- Rend l'appareil **introuvable** entre les sessions

#### Blocage de publicités basé sur DNS

**Objectif** : Bloquer les publicités et le suivi au niveau DNS

**Fonctionnement** :
- Modifie le fichier `/etc/hosts` avec une **liste de blocage**
- Les domaines sur la liste sont résolus vers **127.0.0.1** (localhost)
- Bloque les publicités **pour tous les appareils connectés**

### Outils de hacking

#### Détecteur d'IMSI Catcher

**Objectif** : Surveiller les informations des tours cellulaires pour détecter les anomalies indiquant des **IMSI catchers/Stingrays**

**Indicateurs de détection** :
- **Changement soudain de tour cellulaire** en position stationnaire
- **Rétrogradation vers 2G** *(les IMSI catchers forcent souvent la 2G pour supprimer le chiffrement)*
- **ID de cellule inconnu** apparaissant
- **Signal faible** de la fausse tour
- **Reconnexions fréquentes**

#### Scanner de ports

**Objectif** : Scanner des adresses IP cibles pour les ports ouverts

**Cas d'utilisation** :
- **Reconnaissance réseau**
- **Découverte d'appareils IoT**
- **Audit de sécurité** des réseaux locaux

### Outils d'attaque

**AVERTISSEMENT LÉGAL IMPORTANT** : Ces outils sont réservés aux **tests de sécurité autorisés UNIQUEMENT**. Les utiliser contre des réseaux que vous ne possédez pas ou pour lesquels vous n'avez pas d'autorisation écrite explicite est **ILLÉGAL** dans la plupart des juridictions.

#### Renifleur DNS

**Objectif** : Journaliser les requêtes DNS des clients connectés

*Ceci capture des métadonnées (domaines visités) des clients connectés. Déployez uniquement sur des réseaux que vous possédez ou administrez.*

#### Scanner ARP

**Objectif** : Découvrir les appareils sur le réseau local

#### Evil Twin AP

**Objectif** : Créer un faux point d'accès WiFi clonant les SSID existants

Utilisez ces scénarios d'attaque uniquement en **environnements de laboratoire**.

#### Portail captif

**Objectif** : Modèles de pages de phishing pour la capture d'identifiants

**Objectif pédagogique** : Démontre les **risques d'ingénierie sociale** et pourquoi les utilisateurs doivent vérifier les URL

### Tracker GPS et wardriving

#### Fonctionnalité GPS

**Source GPS** : **Raspberry Pi companion UNIQUEMENT**
- L'Orbic RCL400 n'a **pas de GPS intégré**
- Le Pi connecte un **dongle USB GPS** (chipset U-Blox 7)

#### Mode wardriving

**Objectif** : Scanner les réseaux WiFi avec des coordonnées GPS pour la cartographie

**Intégration Wigle** :
- Le CSV DagShell est **directement téléchargeable sur WiGLE**
- Contribue à la **base de données publique** des emplacements WiFi

**Exemple de format CSV** :
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

### Raspberry Pi Companion

Le **Raspberry Pi companion** étend les capacités de DagShell avec du **matériel externe** :

#### Exigences matérielles

**Minimum** :
- **Raspberry Pi 3B+** ou plus récent
- **Dongle USB GPS** (chipset U-Blox 7 recommandé)
- **Alimentation** *(le Pi nécessite une alimentation séparée)*

______

## Guide d'installation

### Méthode 1 : Flasheur web (recommandé)

**Méthode la plus simple** - Pas de ligne de commande requise

**Étape 1** : Visiter le Webflasher DagShell
- URL : [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Étape 2** : Générer les certificats PKI
- Cliquez sur le bouton **"Generate Certificates"**
- Le navigateur génère une **PKI à 2 niveaux** (CA racine + certificat serveur)
- **Téléchargez les fichiers** : `root.der` et `server.der`

**Étape 3** : Activer le shell root sur l'Orbic
- Connectez-vous au réseau WiFi de l'Orbic
- Entrez le **mot de passe administrateur** dans le formulaire web
- Cliquez sur **"Enable Shell"**

**Étape 4** : Déployer le firmware
- Cliquez sur le bouton **"Deploy DagShell"**

**Étape 5** : Redémarrer l'Orbic
- Mettez l'appareil hors puis sous tension
- DagShell démarre automatiquement

**Étape 6** : Accéder à DagShell
- Ouvrez le navigateur sur : `https://192.168.1.1:8443/`
- Acceptez l'**avertissement de sécurité** (certificat auto-signé - c'est attendu)

### Méthode 2 : Installation manuelle

**Pour les utilisateurs avancés** qui souhaitent construire depuis les sources

#### Étape 1 : Installer les dépendances

**macOS** :
```bash
brew install python3
pip3 install requests cryptography
```

**Linux** :
```bash
sudo apt-get install python3 python3-pip
pip3 install requests cryptography
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Étape 2 : Cloner le dépôt

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Étape 3 : Construire le firmware

```bash
cd orbic_fw_c
python3 gen_pki.py
./build.sh
```

#### Étape 4 : Activer le shell root

```bash
python enable_shell.py VOTRE_MOT_DE_PASSE_ADMIN
```

#### Étape 5 : Déployer le firmware

```bash
python deploy_base64.py
```

#### Étape 6 : Redémarrer et accéder

```bash
reboot
# Navigateur : https://192.168.1.1:8443/
```

______

## Pourquoi combiner DagShell avec RayHunter ?

### Capacités complémentaires

| Fonctionnalité | DagShell | RayHunter |
|----------------|----------|-----------|
| **Détection IMSI Catcher** | Surveillance basique des tours | Analyse avancée des patterns |
| **Suivi GPS** | Oui (via Pi) | Oui (via modem) |
| **WiFi Wardriving** | Oui | Non |
| **Scan Bluetooth** | Oui (via Pi) | Non |
| **Outils réseau** | Oui | Non |
| **Outils d'attaque** | Oui | Non |
| **Outils de confidentialité** | Oui | Minimal |

______

## Cas d'utilisation réels

### Cas 1 : Chercheur en sécurité

**Profil** : Testeur d'intrusion réalisant une évaluation de sécurité WiFi

**Flux de travail avec DagShell** :
1. Conduire autour du périmètre des locaux du client
2. Wardriving pour cartographier la couverture WiFi
3. Créer un Evil Twin du réseau client (avec permission)
4. Surveiller les tentatives de connexion des clients
5. Générer un rapport avec les données collectées

### Cas 2 : Défenseur de la vie privée

**Profil** : Journaliste voyageant à l'international

**Flux de travail avec DagShell** :
1. Activer le correctif TTL avant d'utiliser l'appareil
2. Randomiser l'adresse MAC
3. Surveiller continuellement le détecteur d'IMSI catcher
4. Utiliser AdBlock pour tous les appareils connectés
5. Journaliser les activités cellulaires suspectes

______

## Considérations légales et éthiques

### Cadre légal

**Utilisations légales** :
- Vos propres réseaux
- Tests autorisés avec permission écrite
- Objectifs éducatifs dans des environnements de laboratoire isolés
- Protection de la vie privée sur votre appareil

**Utilisations illégales** :
- Accès non autorisé à des réseaux (violation CFAA aux États-Unis)
- Attaques deauth sur d'autres réseaux (violation FCC)
- Attaques Evil Twin contre le public

### Utilisation responsable

DagShell est un **outil de recherche en sécurité et de confidentialité**. Utilisez-le **de manière responsable** et **éthique**. *Si vous n'êtes pas certain que quelque chose est légal, arrêtez-vous et consultez un avocat avant de continuer.*

______

## Conclusion : Le laboratoire mobile ultime

**DagShell** transforme le modeste **hotspot Orbic RCL400** en un **puissant laboratoire de sécurité mobile** combinant :

- Protection de la vie privée (masquage TTL, usurpation MAC, AdBlock)
- Surveillance réseau (connexions, DNS, routage)
- Outils de hacking (détection IMSI, scan de ports, découverte ARP)
- Capacités d'attaque (Evil Twin, portail captif, deauth)
- Wardriving GPS avec intégration Wigle
- Extension Raspberry Pi (BLE, WiFi, GPS)
- Portable et alimenté par batterie
- Open source et personnalisable

Que vous soyez un **chercheur en sécurité**, un **testeur d'intrusion**, un **défenseur de la vie privée** ou un **administrateur réseau**, DagShell offre une plateforme **portable, puissante et abordable** pour le travail de sécurité mobile.

**Avertissement** : Utilisez de manière responsable. Testez uniquement les réseaux et appareils que vous possédez ou pour lesquels vous avez une autorisation écrite explicite.

______

## Références

1. [DagShell GitHub Repository](https://github.com/dagnazty/DagShell)
2. [DagShell Documentation](https://dagnazty.github.io/DagShell/)
3. [STS Collective - Pre-Flashed Devices](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE - WiFi Mapping Project](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Raspberry Pi Official Documentation](https://www.raspberrypi.org/documentation/)
7. [U-Blox GPS Module Documentation](https://www.u-blox.com/)
8. [OUI Database - IEEE Standards](https://standards.ieee.org/products-programs/regauth/)
9. [iptables Tutorial](https://www.netfilter.org/documentation/)
10. [OpenSSL Documentation](https://www.openssl.org/docs/)
