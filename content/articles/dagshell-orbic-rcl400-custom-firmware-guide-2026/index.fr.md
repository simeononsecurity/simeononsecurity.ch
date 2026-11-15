---
title: "Firmware personnalisé DagShell pour Orbic RCL400 : guide 2026"
date: 2026-05-28
lastmod: 2026-11-15
toc: true
draft: false
description: "Guide technique du firmware DagShell pour Orbic RCL400. Installation, outils de confidentialité, wardriving et limites de la recherche."
genre: ["Firmware personnalisé", "Sécurité mobile", "Outils de confidentialité", "Sécurité réseau", "Wardriving", "Tests d’intrusion", "Sécurité IoT", "Recherche en sécurité", "Sécurité matérielle", "Technologie de confidentialité"]
tags: ["DagShell", "Orbic RCL400", "Firmware personnalisé", "Sécurité des hotspots", "Outils de confidentialité", "Correction TTL", "Usurpation MAC", "Détection des IMSI catchers", "Wardriving", "Suivi GPS", "Attaque Evil Twin", "Portail captif", "Sniffer DNS", "Scanner ARP", "Scanner de ports", "Extension Raspberry Pi", "Sécurité WiFi", "Hotspot mobile", "Surveillance réseau", "Tests d’intrusion", "Recherche en sécurité", "Scan Bluetooth", "Attaque de désauthentification", "Scan WiFi", "Recherche OUI", "Envoi vers Wigle", "Surveillance des antennes cellulaires", "Commandes AT", "Gestionnaire de pare-feu", "Blocage des publicités", "Chiffrement TLS", "Intégration RayHunter", "STS Collective", "Laboratoire de sécurité mobile", "Analyse réseau", "Firmware de confidentialité", "Sécurité open source", "Compilation croisée ARM", "Linux embarqué", "Boîte à outils de sécurité", "Outils de hacking", "Équipe rouge", "Reconnaissance réseau"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Illustration d’un hotspot Orbic RCL400 avec une interface verte lumineuse, entouré de représentations abstraites d’outils de sécurité, comme des graphiques et des cartes, sur fond bleu marine sombre."
coverCaption: ""
---

**Transformez votre Orbic RCL400 en laboratoire mobile de recherche en sécurité**

## Introduction : le hotspot des hackers

**DagShell** est un firmware personnalisé open source pour le **hotspot mobile Orbic RCL400**. Il transforme un appareil cellulaire ordinaire en **boîte à outils portable pour la recherche en sécurité et la confidentialité**. Créé par le chercheur en sécurité « dag », ce firmware au style terminal propose des **outils de hacking, des fonctions de confidentialité et des capacités de surveillance réseau**, dans une interface esthétique vert sur noir.

Ce guide présente :
- **DagShell** et l’ensemble de ses fonctions
- Les étapes d’**installation**, avec le webflasher et les méthodes manuelles
- Les **outils et capacités** disponibles
- La configuration d’un **Raspberry Pi compagnon** pour étendre les fonctions
- **Pourquoi associer DagShell à RayHunter** pour la sécurité mobile
- Des **cas d’usage réels** pour les chercheurs en sécurité et les défenseurs de la vie privée
- Les **considérations juridiques et éthiques**

**En bref** : DagShell et RayHunter sur un Orbic RCL400 forment un **laboratoire de sécurité mobile** pour détecter les IMSI catchers, faire du wardriving, analyser les réseaux et protéger la vie privée.

**Appareils préconfigurés** : cet article est sponsorisé par **STS Collective**, qui propose des hotspots Orbic RCL400 préconfigurés avec **RayHunter et DagShell** : [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Remise exclusive pour les lecteurs** : économisez jusqu’à 20 % sur les produits STS Collective, y compris les Orbic RCL400 préconfigurés. Utilisez le code **SIMEONONSECURITY** au paiement ou [achetez avec la remise appliquée](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Qu’est-ce que DagShell ?

### Présentation

**DagShell** est un firmware personnalisé open source qui remplace l’interface Web d’origine de l’Orbic RCL400 par une **boîte à outils de sécurité complète**, comprenant :

- **Interface de type terminal** avec art ASCII et esthétique de hacker
- **Interface Web chiffrée TLS 1.2 ou supérieur** (certificat auto-signé)
- **Outils de protection de la vie privée** (masquage TTL, usurpation MAC et blocage DNS des publicités)
- **Surveillance réseau** (connexions actives, tables de routage et requêtes DNS)
- **Outils de hacking** (détection d’IMSI catchers, scan de ports et découverte ARP)
- **Capacités d’attaque** (point d’accès Evil Twin, hameçonnage par portail captif et attaques de désauthentification)
- **Suivi GPS et wardriving** avec export CSV compatible avec Wigle
- **Raspberry Pi compagnon** pour le GPS, le scan Bluetooth et la reconnaissance WiFi
- **Accès au système de fichiers** avec gestionnaire de fichiers dans le navigateur
- **Fonctions SMS** via les commandes AT
- **Persistance** : démarrage automatique au lancement

### Spécifications techniques

**Plateforme** : hotspot mobile Orbic RCL400\
**Architecture** : ARM Linux (kernel 3.18)\
**Langage** : C/C++ (binaire ARM statique)\
**Chiffrement** : TLS 1.2 ou supérieur avec certificats auto-signés (PKI à deux niveaux)\
**Serveur Web** : serveur HTTPS embarqué personnalisé (port 8443)\
**Interface** : interface terminal dans le navigateur\
**Licence** : MIT (open source)\
**GitHub** : [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Design visuel

DagShell adopte une **esthétique rétro de hacker** :
- **Logo ASCII** sur chaque page
- **Palette vert sur noir** (style Matrix)
- **Police monospace** (Fira Code)
- **Effets de lignes de balayage** et texte lumineux
- **Mise en page inspirée d’un terminal**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Firmware DagShell exécuté sur Orbic RCL400. L’interface terminal vert sur noir affiche un art ASCII et un menu d’outils de sécurité" >}}

______

## Présentation complète des fonctions

### 🏠 Tableau de bord

**Vue d’ensemble du système** :
- **Durée de fonctionnement** : temps écoulé depuis le démarrage de l’appareil
- **Interface de commandes AT** : contrôle direct du modem pour les utilisateurs avancés
- **État rapide** : adresse IP et état de connexion

Les **commandes AT** permettent le contrôle du modem à bas niveau :
```
Exemples de commandes AT :
AT+CSQ       - Qualité du signal
AT+COPS?     - Opérateur réseau actuel
AT+CREG?     - État de l’enregistrement réseau
AT+CIMI      - Obtenir l’IMSI (identité de l’abonné)
AT+CGSN      - Obtenir l’IMEI (identifiant de l’appareil)
```

### 🌐 Outils réseau

**Informations sur le réseau actuel** :
- Détails de l’**adresse IP et de l’interface**
- **Masque de sous-réseau, passerelle** et adresse de diffusion
- **Statistiques réseau** (paquets envoyés et reçus)

**Affichage de la table de routage** :
- Affiche toutes les routes réseau
- Informations sur la passerelle par défaut
- Correspondance des interfaces

**Surveillance des connexions actives** :
- Liste en temps réel de **toutes les connexions TCP/UDP**
- Adresses IP locales et distantes
- Numéros de port et états des connexions
- Utile pour **surveiller les communications de l’appareil**

### 🔒 Ensemble de protection de la vie privée

#### Correction TTL

**Objectif** : masquer le trafic du hotspot pour éviter sa détection par l’opérateur

**Fonctionnement** :
- Modifie à **65** la valeur **Time To Live (TTL)** des paquets IP
- Les opérateurs détectent le partage de connexion par la diminution du TTL (téléphone = 64, appareil connecté = 63)
- Régler le TTL sur 65 donne l’impression que **tout le trafic est local**

**Cas d’usage** : contourner les restrictions ou limitations de partage de connexion de l’opérateur

**Commandes** :
```bash
# Activer la correction TTL
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Désactiver la correction TTL
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### Usurpation d’adresse MAC

**Objectif** : randomiser l’adresse MAC de l’appareil pour protéger la vie privée

**Fonctionnement** :
- Modifie l’adresse MAC de **wlan0** (interface WiFi)
- Génère une **adresse MAC aléatoire** ou accepte une valeur personnalisée
- Rend l’appareil **difficile à suivre** d’une session à l’autre

**Cas d’usage** : empêcher le suivi par MAC sur les réseaux auxquels vous vous connectez

**Étapes** :
1. L’interface est désactivée
2. Une nouvelle adresse MAC est appliquée
3. L’interface est réactivée
4. La connexion est rétablie

#### Blocage des publicités par DNS

**Objectif** : bloquer les publicités et le suivi au niveau DNS

**Fonctionnement** :
- Modifie le fichier `/etc/hosts` avec une **liste de blocage**
- Les domaines de la liste sont résolus en **127.0.0.1** (localhost)
- Bloque les publicités **sur tous les appareils connectés**

**Cas d’usage** : bloquer les publicités sur tout le réseau sans configurer chaque appareil

**Source de la liste** : domaines publicitaires et de suivi courants (personnalisable)

### 📱 Gestion des SMS

**Envoyer un SMS** :
- Envoie des messages texte au modem via des **commandes AT**
- Utile pour les **notifications à distance** ou les tests

**Voir les messages** :
- Lien vers la boîte de réception native de l’Orbic
- Permet de lire les SMS reçus

**Commande AT utilisée** :
```
AT+CMGS="PHONE_NUMBER"
Texte du message ici^Z
```

### 🔧 Outils de hacking

#### Détecteur d’IMSI catchers

**Objectif** : surveiller les informations des antennes cellulaires et repérer les anomalies pouvant signaler des dispositifs **IMSI catcher ou Stingray**

**Fonctionnement** :
- Interroge le modem pour obtenir les **données de l’antenne cellulaire** :
  - **Cell ID** (identifiant de l’antenne)
  - **LAC** (code de zone de localisation)
  - **MCC/MNC** (code pays mobile et code réseau mobile)
  - **Puissance du signal** (RSSI)
  - **Génération du réseau** (2G/3G/4G)
- **Consigne les changements** pour repérer les changements suspects d’antenne
- **Suivi de référence** : établit quelles antennes sont habituelles dans la zone

**Indicateurs de détection** :
- **Changement soudain d’antenne cellulaire** à l’arrêt
- **Passage à la 2G** *(les IMSI catchers forcent souvent la 2G pour retirer le chiffrement)*
- Apparition d’un **Cell ID inconnu**
- **Signal faible** provenant d’une fausse antenne
- **Reconnexions fréquentes**

**Complémentarité avec RayHunter** : DagShell fournit une **surveillance des antennes cellulaires**. RayHunter offre une **détection dédiée des IMSI catchers**, avec une analyse plus poussée (voir la section ci-dessous).

#### Scanner de ports

**Objectif** : rechercher les ports ouverts sur des adresses IP cibles

**Fonctionnement** :
- **Scan TCP SYN** : envoie des paquets SYN aux ports visés
- **Détection par délai d’attente** : détermine si les ports sont ouverts, fermés ou filtrés
- **Prise en charge des plages** : scan d’un port ou d’une plage de ports

**Cas d’usage** :
- **Reconnaissance réseau**
- **Découverte d’appareils IoT**
- **Audit de sécurité** des réseaux locaux
- **Identification des services**

**Commande** :
```bash
# Scanner les ports 1 à 1000 de la cible
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Gestionnaire de pare-feu

**Objectif** : bloquer ou débloquer des adresses IP avec iptables

**Fonctionnement** :
- Utilise des **règles iptables** pour abandonner les paquets vers ou depuis les IP indiquées
- Les **règles persistantes** survivent aux redémarrages si elles sont enregistrées
- Comprend des **listes d’autorisation et de blocage**

**Cas d’usage** :
- **Bloquer des IP malveillantes**
- **Empêcher les accès non autorisés**
- **Façonner ou filtrer le trafic**
- **Contrôle parental**

**Commandes** :
```bash
# Bloquer l'adresse IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Débloquer l'adresse IP
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Outils d’attaque

**AVERTISSEMENT JURIDIQUE IMPORTANT** : ces outils sont réservés **aux tests de sécurité autorisés**. Les utiliser contre des réseaux qui ne vous appartiennent pas ou sans autorisation écrite explicite est **illégal** dans de nombreuses juridictions (Computer Fraud and Abuse Act aux États-Unis, Computer Misuse Act au Royaume-Uni, etc.). Utilisez-les uniquement sur **vos propres réseaux** ou dans des **environnements de laboratoire contrôlés**.

#### Sniffer DNS

**Objectif** : enregistrer les requêtes DNS des clients connectés

**Fonctionnement** :
- **Journalisation iptables** sur le port 53 (DNS)
- **Le mode promiscuous n’est pas nécessaire**
- Enregistre toutes les requêtes DNS des clients du hotspot
- Révèle **les sites et services** consultés par les clients

**Cas d’usage autorisés** :
- **Analyse du trafic réseau**
- **Surveillance parentale** (pour sa propre famille)
- **Recherche en sécurité** sur ses propres appareils
- **Analyse du comportement d’un malware**

*Cette fonction capture des métadonnées (les domaines visités) des clients connectés. Déployez-la uniquement sur des réseaux qui vous appartiennent ou que vous administrez.*

#### Scanner ARP

**Objectif** : découvrir les appareils du réseau local

**Fonctionnement** :
- Envoie des **requêtes ARP** à toutes les IP du sous-réseau
- Les appareils répondent avec leur **adresse MAC**
- La **recherche OUI** identifie le fabricant (Apple, Samsung, etc.)
- Crée une **carte réseau** des appareils actifs

**Cas d’usage** :
- **Inventaire réseau**
- **Détection d’appareils inconnus**
- **Analyse des réseaux BYOD**
- **Découverte d’appareils IoT**

**Exemple de sortie** :
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Objectif** : visualiser le chemin réseau vers une destination

**Fonctionnement** :
- Envoie des paquets avec un **TTL croissant**
- Chaque saut diminue le TTL et renvoie un message **ICMP Time Exceeded**
- Révèle les **routeurs et le chemin** vers la destination
- Mesure le **temps aller-retour (RTT)** à chaque saut

**Cas d’usage** :
- **Dépannage réseau**
- **Analyse des routes**
- **Diagnostic de latence**
- **Étude du peering des fournisseurs d’accès**

#### Point d’accès Evil Twin

**Objectif** : créer un faux point d’accès WiFi qui imite des SSID existants

**Fonctionnement** :
- Utilise **wlan1** (seconde interface WiFi, si le Pi compagnon la fournit)
- Reproduit le **SSID et le type de chiffrement** du réseau ciblé
- **Capture les clients** qui tentent de se connecter
- Affiche un **portail captif** pour récupérer des identifiants

**Scénario d’attaque** (en laboratoire) :
1. Rechercher les réseaux WiFi légitimes
2. Créer un **faux point d’accès** avec le même SSID
3. Utiliser une **attaque de désauthentification** pour déconnecter les clients du vrai point d’accès
4. Les clients se reconnectent automatiquement au **faux point d’accès**
5. Le portail captif récupère les identifiants

*Détection : si les deux points d’accès sont visibles en même temps, les clients voient des **SSID en double**.*

#### Portail captif

**Objectif** : proposer des modèles de pages d’hameçonnage pour récupérer des identifiants

**Modèles inclus** :
- **Page de connexion WiFi** (style fournisseur d’accès ou hôtel générique)
- **Pages de connexion de réseaux sociaux** (imitations de Facebook, Twitter et Instagram)
- Portails de **connexion d’entreprise**
- Portails WiFi d’**aéroport ou de café**

**Fonctionnement** :
1. Le point d’accès Evil Twin redirige **tout le trafic** vers le portail
2. Le client voit une **page de connexion**
3. Le client saisit ses identifiants
4. Les identifiants sont **enregistrés dans un fichier**
5. L’accès à Internet est accordé ou une erreur s’affiche

**Objectif pédagogique** : montrer les **risques de l’ingénierie sociale** et l’importance de vérifier les URL

### 📍 Suivi GPS et wardriving

#### Fonction GPS

**Source GPS** : uniquement le **Raspberry Pi compagnon**
- *L’Orbic RCL400 n’a **pas de GPS intégré**. Sans le Pi compagnon, aucune donnée de localisation n’est disponible.*
- Le Pi connecte un **dongle GPS USB** (chipset U-Blox 7 recommandé)
- Le Pi transmet les coordonnées à l’Orbic via des **fichiers de données partagés**
- La conversion **ECEF vers latitude/longitude** est automatique

**Affichage du tableau de bord** :
- **Latitude/longitude** en degrés décimaux
- **Altitude** au-dessus du niveau de la mer
- **État du signal GPS** (précision)
- **Actualisation automatique** toutes les 5 secondes
- **Aucune demande de géolocalisation du navigateur** (l’API du navigateur n’est pas utilisée)

**État GPS partagé** :
- Les données GPS sont accessibles à **tous les processus DagShell**
- Le wardriving utilise automatiquement le GPS
- Les fonctions ne se chevauchent pas

#### Mode wardriving

**Objectif** : rechercher des réseaux WiFi et enregistrer leurs coordonnées GPS pour les cartographier

**Fonctionnement** :
1. Attend un **signal GPS valide** (aucune coordonnée 0,0 n’est enregistrée)
2. Recherche les réseaux WiFi toutes les **5 secondes**, en continu
3. Consigne les données réseau :
   - **SSID** (nom du réseau)
   - **BSSID** (adresse MAC)
   - **Type de chiffrement** (WPA2, WPA3 ou ouvert)
   - **Puissance du signal** (RSSI en dBm)
   - **Numéro de canal**
   - **Coordonnées GPS** (latitude/longitude)
   - **Horodatage**
4. Exporte au format **CSV compatible avec Wigle**

**Intégration Wigle** :
- **WiGLE** (wigle.net) est un projet mondial de cartographie WiFi
- Le CSV DagShell peut être **téléversé directement** sur WiGLE
- **Téléversement depuis le navigateur** dans la page Files, sans outil externe
- Contribue à une **base de données publique** des emplacements WiFi

**Cas d’usage** :
- **Cartographie de la couverture WiFi**
- **Relevé de réseaux** pour les fournisseurs d’accès
- **Analyse de puissance du signal**
- **Recherche en sécurité** (réseaux ouverts et chiffrement faible)
- **Analyse géographique**

**Exemple de format CSV** :
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="Mode wardriving DagShell avec coordonnées GPS et réseaux WiFi détectés. Le CSV compatible avec Wigle consigne SSID, BSSID, chiffrement et puissance du signal" >}}

### 🥧 Raspberry Pi compagnon

Le **Raspberry Pi compagnon** étend les capacités de DagShell avec du **matériel externe**.

#### Configuration matérielle requise

**Minimum** :
- **Raspberry Pi 3B+** ou plus récent *(le Pi Zero ne fournit pas assez d’alimentation USB aux périphériques)*
- **Dongle GPS USB** (chipset U-Blox 7 recommandé)
- **Alimentation** *(le Pi a besoin d’une alimentation distincte. Le port USB de l’Orbic ne fournit pas assez de puissance)*

**Facultatif** :
- **Adaptateur WiFi** (seconde interface pour scanner tout en maintenant la connexion)
- **Dongle Bluetooth** (si le Bluetooth intégré au Pi est faible)

#### Module GPS (U-Blox 7)

**Connexion** : dongle GPS USB vers le Pi\
**Protocole** : phrases NMEA sur port série\
**Conversion** : le Pi convertit automatiquement ECEF en latitude/longitude\
**Partage des données** : écrit les coordonnées GPS dans un **fichier partagé** sur l’Orbic

**Analyse des phrases** :
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Heure  Latitude  Longitude  État  Satellites  Altitude
```

#### Scan Bluetooth (BLE)

**Objectif** : découvrir les appareils Bluetooth à proximité

**Fonctionnement** :
- Recherche les **annonces BLE**
- Capture les **adresses MAC**
- Recherche l’**OUI** pour identifier le fabricant
- Enregistre les données en **format CSV**

**Contrôle à distance** :
- Démarre ou arrête le scan depuis l’interface Web de DagShell
- Aucune connexion SSH au Pi n’est nécessaire
- Affiche l’état en temps réel

**Cas d’usage** :
- **Suivi et comptage des appareils**
- **Analyse de fréquentation**
- **Découverte d’appareils Bluetooth**
- **Recherche en sécurité IoT**

**Sortie CSV** :
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### Scan WiFi

**Objectif** : le Pi recherche des réseaux WiFi et transmet les données à l’Orbic

**Avantage** : une interface dédiée au scan permet à **l’Orbic de conserver son hotspot**

**Fonctionnement** :
- Le Pi utilise un **second adaptateur WiFi** ou son WiFi intégré, s’il n’est pas nécessaire à la connexion
- Parcourt **tous les canaux** (1 à 14 en 2,4 GHz et 36 à 165 en 5 GHz si le matériel le permet)
- Transmet les résultats à l’Orbic via le stockage partagé
- DagShell les enregistre dans le **CSV de wardriving**

**Coordination** :
- Le Pi et l’Orbic se **synchronisent** sur l’heure GPS
- Évite les doublons
- Combine les **deux sources de scan** dans un seul journal

#### Attaques de désauthentification

**Objectif** : déconnecter des clients des réseaux WiFi (pour des tests en laboratoire)

**Fonctionnement** :
- Envoie des **trames de désauthentification 802.11**
- Usurpe l’**adresse MAC du point d’accès**
- Le client reçoit une notification de déconnexion du point d’accès
- Le client **perd sa connexion** et tente de se reconnecter

**Méthodes de contrôle** :
- **Désauthentification ponctuelle** : rafale unique de trames
- **Désauthentification continue** : bloque les reconnexions (DoS)
- **Contrôle à distance** : déclenché depuis la page de scan DagShell

**Cas d’usage autorisés** :
- **Retrait d’un appareil indésirable** de son propre réseau
- **Test d’intrusion** avec autorisation
- **Attaques Evil Twin** en laboratoire (forcer la connexion des clients au faux point d’accès)

**⚠️ Avertissement juridique** : les attaques de désauthentification sont **illégales contre les réseaux qui ne vous appartiennent pas**. Elles peuvent entraîner des infractions aux règles de la FCC et des poursuites au titre de la CFAA.

#### Service de démarrage automatique

**Service systemd** : le compagnon Pi démarre automatiquement au lancement

**Fichier de service** (`/etc/systemd/system/pi-companion.service`) :
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**Commandes** :
```bash
# Activer le démarrage automatique
sudo systemctl enable pi-companion

# Démarrer le service
sudo systemctl start pi-companion

# Vérifier l'état
sudo systemctl status pi-companion
```

#### Base de données OUI

**Objectif** : rechercher le fournisseur ou fabricant associé à une adresse MAC

**Base de données** : API des préfixes de la [base de données OUI Master](https://standards.ieee.org/products-programs/regauth/)

**Fonctionnement** :
- Extrait les **3 premiers octets** de l’adresse MAC (préfixe OUI)
- Interroge l’API : `api.example.com/oui/A4:83:E7`
- Renvoie le **nom du fabricant**

**Exemple** :
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Intégration** : utilisé par le scanner ARP, le scanner BLE et le wardriving WiFi

### 📁 Explorateur de fichiers

**Objectif** : parcourir et gérer les fichiers de l’appareil

**Emplacement** : répertoire `/data/` (partition accessible en écriture)

**Fonctions** :
- **Parcourir les fichiers** et sous-répertoires
- **Télécharger** des fichiers sur votre ordinateur
- **Supprimer** des fichiers (avec confirmation)
- **Afficher la taille et l’horodatage** des fichiers

**Fichiers courants** :
- `wardrive_log.csv` : données de scan WiFi
- `bluetooth_scan.csv` : données des appareils BLE
- `gps_track.gpx` : traces GPS
- `dns_queries.log` : requêtes DNS capturées
- `arp_scan.txt` : liste des appareils réseau

**Envoi vers Wigle** :
- **Envoi direct depuis le navigateur** sur la page Files
- Authentification avec un compte WiGLE
- Envoie le CSV sans téléchargement préalable

______

{{< stscollective-ad "rayhunter" >}}

## Guide d’installation

### Prérequis

**Matériel** :
- **Hotspot mobile Orbic RCL400**
- **Ordinateur** (Windows, macOS ou Linux)
- **Câble USB** (pour flasher directement le firmware)

**Logiciels** :
- **Python 3** avec les modules `requests` et `cryptography`
- **Navigateur Web** (Chrome, Firefox, Edge ou Safari)

**Facultatif** :
- **Raspberry Pi 3B+** ou plus récent (pour le GPS et les fonctions avancées)
- **Dongle GPS USB** (chipset U-Blox 7)

### Méthode 1 : Webflasher (recommandé)

**Méthode la plus simple** : aucune ligne de commande requise

**Étape 1** : ouvrir DagShell Webflasher
- URL : [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Étape 2** : générer les certificats PKI
- Cliquer sur le bouton **"Generate Certificates"**
- Le navigateur génère une **PKI à deux niveaux** (CA racine et certificat serveur)
- **Télécharger les fichiers** : `root.der` et `server.der`

**Étape 3** : activer le shell root sur Orbic
- Se connecter au réseau WiFi de l’Orbic
- Saisir le **mot de passe administrateur** dans le formulaire Web
- Cliquer sur **"Enable Shell"**
- La page Web exploite l’API de l’Orbic pour ouvrir un **shell root sur le port 24**

**Étape 4** : déployer le firmware
- Cliquer sur le bouton **"Deploy DagShell"**
- Le script téléverse :
  - `orbic_app` (binaire principal du firmware)
  - `root.der` (certificat racine)
  - `server.der` (certificat TLS du serveur)
  - `dagshell_boot.sh` (script de persistance)
- L’installation prend **2 à 3 minutes**

**Étape 5** : redémarrer l’Orbic
- Éteindre puis rallumer l’appareil
- DagShell démarre automatiquement

**Étape 6** : accéder à DagShell
- Ouvrir le navigateur à l’adresse : `https://192.168.1.1:8443/`
- Accepter l’**avertissement de sécurité** (le certificat auto-signé est attendu)
- Se connecter avec les identifiants par défaut, si le système les demande

### Méthode 2 : installation manuelle

Pour les **utilisateurs avancés** qui souhaitent compiler le code source.

#### Étape 1 : installer les dépendances

**Windows** :
```powershell
# Installer Python 3
# Télécharger depuis python.org

# Installer les modules requis
pip install requests cryptography

# Le compilateur croisé ARM est dans le dossier gcc_win
```

**macOS** :
```bash
# Installer Homebrew s'il n'est pas déjà installé
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installer Python 3
brew install python3

# Installer les modules requis
pip3 install requests cryptography

# La chaîne d'outils ARM est dans le dossier gcc_mac
```

**Linux** :
```bash
# Installer Python 3 et pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Installer les modules requis
pip3 install requests cryptography

# Installer le compilateur croisé ARM
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Étape 2 : cloner le dépôt

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Étape 3 : compiler le firmware

**Windows** :
```powershell
cd orbic_fw_c
python gen_pki.py          # Générer les certificats
.\build.ps1                # Compiler le micrologiciel
```

**macOS/Linux** :
```bash
cd orbic_fw_c
python3 gen_pki.py         # Générer les certificats
./build.sh                 # Compiler le micrologiciel, BearSSL est compilé automatiquement
```

**Résultat** : `orbic_app` (binaire ARM statique) et fichiers de certificats DER

**⚠️ Note pour macOS** : le dossier `gcc_mac/` contient une chaîne d’outils ARM personnalisée, compilée avec **crosstool-ng** pour cibler les en-têtes du **kernel Linux 3.2**, compatibles avec le kernel 3.18 de l’Orbic. *Les compilateurs ARM standard de Homebrew ciblent des kernels plus récents et **ne fonctionnent pas**.*

#### Étape 4 : activer le shell root sur Orbic

```bash
# Se connecter au WiFi Orbic
# Remplacer YOUR_ADMIN_PASSWORD par le vrai mot de passe

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Cette commande exploite l’API Web de l’Orbic pour ouvrir un shell root sur le **port 24**.

#### Étape 5 : déployer le firmware

```bash
python deploy_base64.py
```

Le script téléverse et installe :
- `orbic_app` dans `/data/orbic_app`
- Les certificats dans `/data/root.der` et `/data/server.der`
- Le script de démarrage dans `/etc/rc.d/dagshell_boot.sh`

**Persistance** : le firmware démarre automatiquement après redémarrage grâce à un script init.

#### Étape 6 : redémarrer et accéder à DagShell

```bash
# Redémarrer Orbic (couper puis remettre l'alimentation ou utiliser SSH)
reboot

# Après le redémarrage, accéder à DagShell
# Navigateur : https://192.168.1.1:8443/
```

### Avertissement concernant le certificat de sécurité

En accédant à DagShell, vous verrez un avertissement **"Not Secure"** ou **"Not Trusted"** :

**Navigateurs de bureau** :
- Cliquer sur **"Advanced"**
- Cliquer sur **"Proceed to 192.168.1.1 (unsafe)"**

**Navigateurs mobiles** :
- Appuyer sur **"Show Details"**
- Appuyer sur **"visit this website"**

**Pourquoi cet avertissement ?** :
- Le certificat est **auto-signé** (il ne vient pas d’une autorité reconnue telle que Let's Encrypt)
- Le certificat racine n’est pas dans le magasin de certificats approuvés de l’appareil
- *C’est un comportement **normal** pour un firmware personnalisé, et non un signe de compromission.*

**La connexion est-elle sécurisée ?** :
- **Oui**. La connexion est bien chiffrée avec **TLS 1.2 ou supérieur**
- Les données ne peuvent pas être interceptées
- *Le certificat n’est pas lié à une autorité publique de confiance, mais le chiffrement est réel.*

**Facultatif** : installer `root.der` dans le magasin de certificats de l’appareil pour supprimer l’avertissement.

______

## Configuration du Raspberry Pi compagnon

**Facultatif, mais fortement recommandé** pour profiter de toutes les fonctions.

### Configuration matérielle

**Étape 1** : obtenir le matériel
- **Raspberry Pi 3B+** ou plus récent (35 à 55 $)
- **Dongle GPS USB** avec chipset U-Blox 7 (15 à 30 $)
- **Carte microSD** de 16 Go ou plus pour Raspberry Pi OS (10 $)
- **Alimentation** pour le Pi (10 $)

**Étape 2** : installer Raspberry Pi OS
```bash
# Télécharger Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# Flasher Raspberry Pi OS Lite sur la carte SD
# Démarrer la Pi et terminer la configuration
```

**Étape 3** : connecter le dongle GPS
- Brancher le GPS USB au Pi
- Vérifier sa détection : `lsusb` (l’appareil GPS doit apparaître)
- Vérifier le port série : `ls /dev/ttyUSB*` ou `ls /dev/ttyACM*`

### Installation logicielle

**Étape 1** : cloner le dépôt DagShell sur le Pi

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Étape 2** : installer les dépendances

```bash
# Mettre à jour la liste des paquets
sudo apt-get update

# Installer les paquets requis
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Installer les modules Python
pip3 install pyserial gps3 bluetooth pybluez
```

**Étape 3** : configurer le service GPS

```bash
# Modifier la configuration de gpsd
sudo nano /etc/default/gpsd

# Définir la ligne DEVICES sur le port série du GPS
DEVICES="/dev/ttyUSB0"  # Ajuster si nécessaire

# Redémarrer gpsd
sudo systemctl restart gpsd

# Tester le GPS
cgps -s  # Les données des satellites devraient apparaître après environ 30 secondes
```

**Étape 4** : configurer le compagnon Pi

```bash
# Modifier le fichier de configuration
nano pi_companion/config.py

# Définir l'adresse IP d'Orbic
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# Définir le port série du GPS
GPS_DEVICE = "/dev/ttyUSB0"

# Enregistrer et quitter
```

**Étape 5** : installer le service systemd

```bash
# Copier le fichier de service
sudo cp pi_companion.service /etc/systemd/system/

# Recharger systemd
sudo systemctl daemon-reload

# Activer le démarrage automatique
sudo systemctl enable pi-companion

# Démarrer le service
sudo systemctl start pi-companion

# Vérifier l'état
sudo systemctl status pi-companion
```

**Étape 6** : vérifier la communication

```bash
# Vérifier les journaux
journalctl -u pi-companion -f

# Les coordonnées GPS devraient être envoyées à Orbic
```

### Configuration réseau

**Option A** : connexion WiFi

```bash
# La Pi se connecte au point d'accès Orbic
# Modifier la configuration wpa_supplicant
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Ajouter un réseau
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# Redémarrer le WiFi
sudo systemctl restart networking
```

**Option B** : Ethernet USB (recommandé)

- Connecter le Pi à l’Orbic avec un **câble USB** (port USB du Pi vers celui de l’Orbic)
- Activer le **mode USB gadget** sur le Pi
- Le Pi se comporte comme un **périphérique Ethernet USB**
- *Cette méthode est plus fiable que le WiFi pour un transfert continu des données.*
- Le Pi accède à Internet via l’Orbic

**Configuration USB gadget** :
```bash
# Modifier config.txt
sudo nano /boot/config.txt

# Ajouter à la fin
dtoverlay=dwc2

# Modifier cmdline.txt
sudo nano /boot/cmdline.txt

# Ajouter après rootwait
modules-load=dwc2,g_ether

# Redémarrer
sudo reboot
```

______

## Pourquoi associer DagShell à RayHunter ?

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Schéma comparant les outils de wardriving WiFi et d’attaque réseau de DagShell à la détection des anomalies des protocoles cellulaires de RayHunter. Les deux fonctionnent sur le même hotspot Orbic RCL400" >}}

### Capacités complémentaires

**DagShell** et **RayHunter** sont des outils de sécurité **complémentaires** qui couvrent différents aspects de la recherche en sécurité mobile :

| Fonction | DagShell | RayHunter |
|---------|----------|-----------|
| **Détection d’IMSI catchers** | Surveillance élémentaire des antennes cellulaires | Analyse avancée de motifs |
| **Suivi GPS** | Oui (avec le Pi) | Oui (avec le modem) |
| **Wardriving WiFi** | Oui | Non |
| **Scan Bluetooth** | Oui (avec le Pi) | Non |
| **Outils réseau** | Oui (sniffer DNS, scan ARP et scan de ports) | Non |
| **Outils d’attaque** | Oui (Evil Twin, portail captif, désauthentification) | Non |
| **Outils de confidentialité** | Oui (correction TTL, usurpation MAC, AdBlock) | Limités |
| **Base de données d’antennes cellulaires** | Élémentaire | Complète |
| **Analyse IA/ML** | Non | Oui (détection d’anomalies) |
| **Analyse des protocoles opérateur** | Limitée | Approfondie (SS7/Diameter) |

### Cas d’usage complémentaires

#### 1. **Défense complète contre les IMSI catchers**

**Scénario** : déplacement dans une zone fortement surveillée

**Apport de DagShell** :
- **Surveille en temps réel** les changements d’antenne cellulaire
- **Suit la position GPS** lors des changements suspects
- **Enregistre les données d’antenne** pour une analyse ultérieure

**Apport de RayHunter** :
- **Détection d’anomalies par apprentissage automatique** des protocoles cellulaires
- **Inspection des paquets SS7/Diameter** pour repérer des attaques sophistiquées
- Comparaison avec une **base de données d’antennes fiables connues**

**Ensemble** : DagShell assure une **surveillance continue**, RayHunter apporte une **analyse approfondie**.

#### 2. **Wardriving et sécurité cellulaire**

**Scénario** : cartographier les réseaux WiFi d’une zone urbaine

**Apport de DagShell** :
- **Scan WiFi** avec coordonnées GPS
- Outils d’**analyse réseau** (puissance du signal, chiffrement)
- Export CSV **Wigle** pour la cartographie

**Apport de RayHunter** :
- **Suivi des antennes cellulaires** pendant le wardriving
- **Détection d’IMSI catchers** pendant le scan WiFi
- **Alerte en cas de compromission de la sécurité cellulaire**

**Ensemble** : wardriving avec **surveillance de la sécurité cellulaire**.

#### 3. **Laboratoire de recherche en sécurité**

**Scénario** : équipe rouge ou test d’intrusion

**Apport de DagShell** :
- **Point d’accès Evil Twin** pour tester le WiFi
- **Portail captif** pour les démonstrations d’ingénierie sociale
- **Attaques de désauthentification** pour tester la résilience
- Outils de **reconnaissance réseau**

**Apport de RayHunter** :
- **Détecte si vous êtes surveillé** pendant les tests
- Alerte sur la **sécurité des antennes cellulaires**
- Aide à prévenir la **contre-surveillance** pendant les tests

**Ensemble** : outils offensifs avec une **vision défensive**.

#### 4. **Voyage axé sur la confidentialité**

**Scénario** : journaliste ou activiste dans un environnement sensible

**Apport de DagShell** :
- **Masquage TTL** pour dissimuler le partage de connexion
- **Usurpation MAC** pour limiter l’identification de l’appareil
- **AdBlock** pour empêcher le suivi
- **Surveillance des IMSI catchers**

**Apport de RayHunter** :
- **Détection avancée des IMSI catchers**
- **Détection des attaques au niveau protocole**
- **Alertes de sécurité cellulaire**

**Ensemble** : confidentialité renforcée grâce à une **protection multicouche**.

### Installation conjointe

**Option préconfigurée** (la plus simple) :
- Achat chez **STS Collective** : [Orbic RCL400 préconfiguré avec RayHunter et DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **Prêt à l’emploi** dès la sortie de la boîte
- Les deux firmwares sont **testés et vérifiés**
- **Aucune installation à effectuer**

**Installation manuelle** :
1. **Installer d’abord RayHunter** (voir le [guide complet pour flasher les appareils RayHunter](/articles/how-to-flash-rayhunter-devices-complete-guide/))
2. **Installer DagShell ensuite** (les deux peuvent coexister)
3. **RayHunter** utilise les ports par défaut
4. **DagShell** utilise le port 8443
5. Accéder à chacun dans un onglet différent du navigateur

**Pas de conflit** :
- RayHunter utilise les ports **80/443**
- DagShell utilise le port **8443**
- Ils n’interfèrent pas l’un avec l’autre
- Ils fonctionnent **simultanément**

Vous ne souhaitez pas effectuer l’installation manuelle ? L’**[Orbic RCL400 avec RayHunter et DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** préconfiguré est prêt à l’emploi. Le code lecteur **SIMEONONSECURITY** offre jusqu’à 20 % de remise chez STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acheter un RCL400 préconfiguré et économiser 20 %
{{< /centerbutton >}}

______

## Cas d’usage concrets

### Cas d’usage 1 : chercheur en sécurité

**Profil** : testeur d’intrusion réalisant une évaluation de la sécurité WiFi

**Outils DagShell utilisés** :
- **Wardriving WiFi** pour cartographier les réseaux du client
- **Scanner ARP** pour découvrir les appareils
- **Scanner de ports** pour identifier les services
- **Evil Twin et portail captif** pour tester la résistance à l’ingénierie sociale
- **Explorateur de fichiers** pour récupérer les résultats

**Déroulement** :
1. Parcourir le périmètre du site du client
2. Effectuer un wardriving pour cartographier la couverture WiFi
3. Créer, avec autorisation, un Evil Twin du réseau du client
4. Surveiller les tentatives de connexion des clients
5. Produire un rapport avec les données recueillies

**Intégration RayHunter** : aide à vérifier que le chercheur n’est pas surveillé pendant l’évaluation.

### Cas d’usage 2 : défenseur de la vie privée

**Profil** : journaliste en déplacement à l’étranger

**Outils DagShell utilisés** :
- **Correction TTL** pour contourner les restrictions de l’opérateur
- **Usurpation MAC** pour préserver l’anonymat de l’appareil
- **Détecteur d’IMSI catchers** pour surveiller les risques d’espionnage
- **Sniffer DNS** pour vérifier qu’aucun appareil ne divulgue de données
- **AdBlock** pour limiter le suivi

**Déroulement** :
1. Activer la correction TTL avant d’utiliser l’appareil
2. Randomiser l’adresse MAC
3. Laisser le détecteur d’IMSI catchers surveiller en continu
4. Activer AdBlock pour tous les appareils connectés
5. Consigner les activités cellulaires suspectes

**Intégration RayHunter** : détection avancée des IMSI catchers, au-delà de la surveillance de base.

### Cas d’usage 3 : administrateur réseau

**Profil** : administrateur informatique gérant plusieurs sites

**Outils DagShell utilisés** :
- **Wardriving WiFi** pour vérifier la couverture
- **Scanner ARP** pour inventorier les appareils
- **Scanner de ports** pour les audits de sécurité
- **Surveillance des connexions actives** pour repérer le trafic non autorisé
- **Gestionnaire de pare-feu** pour bloquer des IP

**Déroulement** :
1. Parcourir le site pour vérifier la couverture WiFi
2. Effectuer un scan ARP pour découvrir tous les appareils réseau
3. Scanner les serveurs pour repérer les services exposés
4. Bloquer les IP malveillantes avec le pare-feu
5. Exporter les rapports pour la documentation

**Intégration RayHunter** : surveillance de la sécurité cellulaire sur les sites équipés d’appareils mobiles.

### Cas d’usage 4 : chercheur en sécurité IoT

**Profil** : chercheur analysant la sécurité d’appareils IoT

**Outils DagShell utilisés** :
- **Scanner ARP** avec recherche OUI pour identifier les appareils IoT
- **Scanner de ports** pour trouver les services ouverts
- **Sniffer DNS** pour capturer les habitudes de trafic IoT
- **Scanner Bluetooth** (Pi) pour les appareils IoT BLE
- **Traceroute** pour analyser la connectivité

**Déroulement** :
1. Déployer l’Orbic et le Pi dans un environnement de test
2. Effectuer un scan ARP pour découvrir les appareils IoT
3. Rechercher des services vulnérables avec le scanner de ports
4. Scanner les appareils IoT Bluetooth avec BLE
5. Analyser les requêtes DNS pour étudier les connexions sortantes des appareils
6. Documenter les vulnérabilités

**Intégration RayHunter** : détecte si les appareils IoT disposent d’une connexion cellulaire et surveille les anomalies.

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Schéma présentant quatre cas d’usage combinés de DagShell et RayHunter : recherche en sécurité, défense de la vie privée, administration réseau et recherche IoT" >}}

______

## Considérations juridiques et éthiques

### Cadre juridique

**Des outils comme DagShell se situent parfois dans une zone juridique complexe** :

**Usages légaux** :
✅ **Vos propres réseaux** : tester vos appareils et réseaux\
✅ **Tests autorisés** : effectuer des tests d’intrusion avec une autorisation écrite\
✅ **Objectifs pédagogiques** : apprendre dans des laboratoires isolés\
✅ **Protection de la vie privée** : utiliser la correction TTL et l’usurpation MAC sur votre appareil\
✅ **Recherche en sécurité** : étudier les vulnérabilités et les signaler de manière responsable

**Usages illégaux** :
❌ **Accès non autorisé** : attaquer les réseaux d’autrui (infraction à la CFAA)\
❌ **Attaques de désauthentification** contre d’autres réseaux (infraction aux règles de la FCC et risque de poursuites pénales)\
❌ Attaques **Evil Twin** contre le public (fraude électronique et usurpation d’identité)\
❌ **Sniffing DNS** sans consentement (interception de communications)\
❌ **Contourner la sécurité** pour commettre une fraude

### Lois à connaître

**États-Unis** :
- **Computer Fraud and Abuse Act (CFAA)** : accès non autorisé à des ordinateurs et réseaux
- **Wiretap Act** : interception des communications électroniques
- **Règles de la FCC** : interférences radio (attaques de désauthentification)

**Royaume-Uni** :
- **Computer Misuse Act 1990** : loi similaire à la CFAA
- **Regulation of Investigatory Powers Act (RIPA)** : restrictions sur l’interception

**Union européenne** :
- **RGPD** : protection des données (scan Bluetooth ou WiFi de données identifiables)
- *Les règles locales varient selon le pays, tout comme leur application.*

### Principes éthiques

**À faire** :
- ✅ Utiliser les outils sur **vos appareils et réseaux**
- ✅ Obtenir une **autorisation écrite** avant de tester les systèmes d’autrui
- ✅ Procéder à une **divulgation responsable** si vous découvrez des vulnérabilités
- ✅ Limiter l’**usage pédagogique** à des environnements contrôlés
- ✅ Protéger **votre vie privée**

**À éviter** :
- ❌ Attaquer des réseaux qui ne vous appartiennent pas
- ❌ Voler les identifiants de personnes inconnues
- ❌ Perturber des infrastructures critiques
- ❌ Utiliser les outils à des fins malveillantes
- ❌ Diffuser des données capturées

### Engagement d’utilisation responsable

DagShell est un **outil de recherche en sécurité et de confidentialité**. Ses capacités sont comparables à celles d’outils professionnels de test d’intrusion comme **Kali Linux**, **WiFi Pineapple** ou **HackRF**.

**L’intention compte** : les mêmes outils servent aux **hackers malveillants** et aux **professionnels de la sécurité**. La différence tient à :
- **L’autorisation** (permission de tester)
- **L’intention** (améliorer la sécurité ou causer un préjudice)
- **La divulgation** (signaler les résultats ou les exploiter)

Utilisez DagShell de manière **responsable** et **éthique**. *Si vous ne savez pas si une action est légale, arrêtez-vous et consultez un avocat avant de continuer.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Cadre juridique et éthique pour la recherche en sécurité avec DagShell, présentant les usages autorisés et non autorisés ainsi que les lois applicables" >}}

______

## Dépannage

### Problèmes d’installation

**Problème** : `enable_shell.py` ne parvient pas à se connecter

**Solutions** :
- Vérifier que vous êtes connecté au **WiFi de l’Orbic**
- Vérifier que l’adresse IP est **192.168.1.1** (valeur par défaut)
- Réessayer le mot de passe administrateur (sensible à la casse)
- Vérifier l’accès au port 80 : `telnet 192.168.1.1 80`

**Problème** : l’envoi du firmware échoue

**Solutions** :
- Activer d’abord le shell root (`enable_shell.py` doit réussir)
- Vérifier la stabilité du réseau (utiliser une connexion filaire si possible)
- Essayer `deploy_net.py` à la place de `deploy_base64.py`
- Vérifier l’espace disponible sur la partition `/data` : `df -h /data`

**Problème** : l’avertissement du certificat persiste

**Solutions** :
- *C’est **normal** avec un certificat auto-signé. La connexion reste chiffrée.*
- Cliquer sur « Advanced », puis « Proceed anyway » à chaque visite
- **Facultatif** : installer `root.der` dans le magasin de certificats de l’appareil (option avancée)

### Problèmes d’exécution

**Problème** : DagShell ne démarre pas au lancement

**Solutions** :
- Vérifier le script de démarrage : `ls -la /etc/rc.d/dagshell_boot.sh`
- Vérifier qu’il est exécutable : `chmod +x /etc/rc.d/dagshell_boot.sh`
- Consulter les journaux : `logread | grep dagshell`
- Démarrer manuellement : `/data/orbic_app &`

**Problème** : le GPS ne fonctionne pas

**Solutions** :
- Vérifier que le **Pi compagnon** fonctionne : `systemctl status pi-companion`
- Vérifier que le GPS capte les satellites : `cgps -s` (sur le Pi)
- Vérifier que le dongle GPS est connecté : `lsusb`
- *Attendre 5 à 10 minutes pour obtenir un premier signal GPS à froid. La première acquisition peut prendre plus longtemps à l’extérieur.*

**Problème** : le wardriving n’enregistre rien

**Solutions** :
- Attendre le signal GPS avant de commencer
- Vérifier les droits d’écriture sur `/data`
- Vérifier que le fichier CSV est créé : `ls -la /data/wardrive_log.csv`
- Vérifier que l’interface WiFi est active : `ifconfig wlan0`

**Problème** : le Pi compagnon ne communique pas avec l’Orbic

**Solutions** :
- Vérifier la connectivité réseau : `ping 192.168.1.1`
- Vérifier que l’adresse IP du fichier de configuration est correcte
- Vérifier que le port 8443 est ouvert : `telnet 192.168.1.1 8443`
- Consulter les journaux du Pi compagnon : `journalctl -u pi-companion`

### Problèmes de performances

**Problème** : l’interface Web est lente ou saccadée

**Solutions** :
- Vider le cache du navigateur
- Désactiver les extensions du navigateur (les bloqueurs de publicités interfèrent)
- Connecter l’Orbic **par câble** plutôt qu’en WiFi
- Redémarrer DagShell : `killall orbic_app && /data/orbic_app &`

**Problème** : les scans de wardriving prennent trop de temps

**Solutions** :
- Augmenter l’intervalle de scan dans les paramètres (réduire la fréquence pour améliorer les performances)
- Réduire le nombre de canaux analysés
- *Un signal GPS faible ralentit les scans : le système attend des coordonnées valides avant de les enregistrer.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="Procédure de dépannage DagShell présentant les problèmes courants d’installation, de GPS et de wardriving, avec des solutions étape par étape" >}}

______

## Configuration avancée

### Personnaliser DagShell

**Modifier le code source** :
- Modifier les fichiers du dossier `orbic_fw_c/`
- Recompiler avec `build.sh` ou `build.ps1`
- Redéployer le firmware

**Ajouter des pages personnalisées** :
- DagShell intègre du HTML dans le code C++
- Modifier `main.cpp` pour ajouter des routes
- Recompiler et déployer

**Certificat personnalisé** :
- Générer sa propre PKI avec `gen_pki.py`
- Utiliser **OpenSSL** pour créer des certificats
- Remplacer `root.der` et `server.der`

### Intégration avec d’autres outils

**Exporter des données vers Wireshark** :
```bash
# Capturer le fichier pcap
tcpdump -i wlan0 -w /data/capture.pcap

# Télécharger avec le navigateur de fichiers
# Ouvrir dans Wireshark sur le PC
```

**Importer des traces GPS dans QGIS** :
```bash
# Exporter au format GPX
python gps_to_gpx.py /data/gps_coords.txt

# Importer dans QGIS comme couche vectorielle
```

**Synchroniser avec une base de données externe** :
```python
# Script personnalisé pour envoyer les données wardrive vers MySQL
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### Optimisation des performances

**Accélérer le scan** :
```bash
# Modifier l'intervalle de scan wardrive
# Dans l'interface Web DagShell, passer de 5 s à 3 s pour accélérer le scan
# En contrepartie, l'utilisation du CPU augmente et des réseaux peuvent être manqués
```

**Optimiser la batterie** (avec une batterie externe) :
```bash
# Réduire la luminosité de l'écran Orbic
# Désactiver les fonctions inutilisées (BT et GPS lorsqu'ils ne sont pas nécessaires)
# Utiliser le mode veille entre les sessions wardrive
```

______

## Comparaison avec des alternatives

### DagShell ou WiFi Pineapple

| Fonction | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **Prix** | 60 à 80 $ + appareil | 99 à 299 $ |
| **Cellulaire** | ✅ 4G LTE intégré | ❌ Non (WiFi uniquement) |
| **GPS** | ✅ Via le Pi compagnon | ⚠️ Via dongle USB |
| **Evil Twin** | ✅ Oui | ✅ Oui |
| **Portail captif** | ✅ Oui | ✅ Oui |
| **Désauthentification** | ✅ Oui (via le Pi) | ✅ Oui |
| **Wardriving** | ✅ Oui | ✅ Oui |
| **Détection IMSI** | ✅ Élémentaire | ❌ Non |
| **Portabilité** | ✅ Très portable | ⚠️ Moyenne |
| **Batterie** | ✅ Intégrée | ⚠️ Externe nécessaire |
| **Prise en main** | Moyenne | Facile (interface aboutie) |

**Meilleur choix** : DagShell pour la **sécurité cellulaire mobile**, Pineapple pour les tests **WiFi uniquement** avec une interface simple.

### DagShell ou Kali Linux sur Pi

| Fonction | DagShell | Kali sur Pi |
|---------|----------|-----------|
| **Temps de configuration** | 15 minutes | 2 à 3 heures |
| **LTE cellulaire** | ✅ Intégré | ❌ Modem USB requis |
| **Interface Web** | ✅ Oui | ⚠️ Limitée (VNC ou SSH nécessaire) |
| **Nombre d’outils** | ~15 | 600+ |
| **Spécialisation** | Sécurité mobile | Tests d’intrusion généralistes |
| **Portabilité** | ✅ Format poche | ⚠️ Écran et alimentation requis |
| **Autonomie** | 8 à 10 heures | 2 à 4 heures |

**Meilleur choix** : DagShell pour les tâches **mobiles spécifiques**, Kali pour une **boîte à outils complète**.

### DagShell ou firmware d’origine de l’Orbic

| Fonction | DagShell | Firmware d’origine |
|---------|----------|--------------------|
| **Outils de sécurité** | ✅ Nombreux | ❌ Aucun |
| **Fonctions de confidentialité** | ✅ Oui | ❌ Minimales |
| **Personnalisation** | ✅ Complète | ❌ Verrouillée |
| **Wardriving** | ✅ Oui | ❌ Non |
| **GPS** | ✅ Oui (via le Pi) | ❌ Non |
| **Open source** | ✅ Oui | ❌ Propriétaire |
| **Assistance** | ⚠️ Communautaire | ✅ Officielle |
| **Stabilité** | ⚠️ Bêta | ✅ Production |

**Meilleur choix** : DagShell pour les **chercheurs**, le firmware d’origine pour les **utilisateurs occasionnels**.

______

## Conclusion : le laboratoire mobile ultime

**DagShell** transforme le **hotspot Orbic RCL400** en un **laboratoire mobile de sécurité** qui réunit :

✅ **Protection de la vie privée** (masquage TTL, usurpation MAC, AdBlock)\
✅ **Surveillance réseau** (connexions, DNS, routage)\
✅ **Outils de hacking** (détection IMSI, scan de ports, découverte ARP)\
✅ **Capacités d’attaque** (Evil Twin, portail captif, désauthentification)\
✅ **Wardriving GPS** avec intégration Wigle\
✅ **Extension Raspberry Pi** (BLE, WiFi, GPS)\
✅ **Portable et alimenté par batterie**\
✅ **Open source et personnalisable**

### Avec RayHunter

**RayHunter et DagShell** forment une **plateforme complète de sécurité mobile** :
- **RayHunter** détecte les IMSI catchers par une analyse avancée
- **DagShell** fournit des outils offensifs et de confidentialité
- Les deux fonctionnent **simultanément** sur le même appareil
- Leurs **capacités se complètent sans se chevaucher**
- Un **seul équipement portable** couvre de nombreux besoins de sécurité mobile

### Pour commencer

**Option 1 : préconfigurée** (la plus simple)
- **STS Collective** : [Orbic RCL400 avec RayHunter et DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- Arrive **prêt à l’emploi**
- Aucune installation à effectuer
- Configuration professionnelle

**Option 2 : installation manuelle**
- Suivre ce guide
- **Gratuit** si vous possédez déjà un Orbic RCL400
- Apprendre la procédure d’installation
- Personnaliser selon vos besoins

### Pour aller plus loin

- **[Flasher des appareils RayHunter : guide complet](/articles/how-to-flash-rayhunter-devices-complete-guide/)** : installer RayHunter en premier
- **[Comparatif d’appareils RayHunter : revue complète](/articles/rayhunter-device-comparison-2026-complete-review/)** : choisir une plateforme
- **[Projet Flock-You : guide du matériel de contre-surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** : autres outils de détection

### Dernières réflexions

DagShell offre une plateforme **portable, complète et abordable** pour la sécurité mobile, que vous soyez **chercheur en sécurité**, **testeur d’intrusion**, **défenseur de la vie privée** ou **administrateur réseau**.

**Avertissement** : utilisez DagShell de façon responsable. Testez uniquement les réseaux et appareils qui vous appartiennent ou pour lesquels vous disposez d’une autorisation écrite explicite. Respectez la loi et l’éthique. Bon hacking ! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Hotspot Orbic RCL400 équipé du firmware DagShell comme laboratoire portable complet de recherche en sécurité mobile" >}}

______

## Références

1. [Dépôt DagShell sur GitHub](https://github.com/dagnazty/DagShell)
2. [Documentation DagShell](https://dagnazty.github.io/DagShell/)
3. [STS Collective : appareils préconfigurés](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE : projet de cartographie WiFi](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Documentation officielle Raspberry Pi](https://www.raspberrypi.org/documentation/)
7. [Documentation du module GPS U-Blox](https://www.u-blox.com/)
8. [Base de données OUI : normes IEEE](https://standards.ieee.org/products-programs/regauth/)
9. [Tutoriel iptables](https://www.netfilter.org/documentation/)
10. [Documentation OpenSSL](https://www.openssl.org/docs/)
