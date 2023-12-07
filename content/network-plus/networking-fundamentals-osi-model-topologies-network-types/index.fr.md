---
title: "Cours Réseau Plus : Comprendre le modèle OSI, les topologies et les types de réseaux"
date: 2023-07-01
toc: true
draft: false
description: "Explorer l'importance des principes fondamentaux des réseaux, y compris le modèle OSI, les topologies de réseau et les différents types de réseaux, pour construire des infrastructures efficaces et fiables."
genre: ["Technologie", "Mise en réseau", "Infrastructure informatique", "Architecture du réseau", "Informatique", "Communication de données", "Technologie de l'information", "Sécurité des réseaux", "Gestion du réseau", "Internet"]
tags: ["principes fondamentaux de la mise en réseau", "Modèle OSI", "topologies de réseaux", "types de réseaux", "encapsulation des données", "couches du réseau", "topologie du maillage", "topologie en étoile", "topologie du bus", "topologie en anneau", "topologie hybride", "réseau peer-to-peer", "réseau client-serveur", "LAN", "MAN", "WAN", "WLAN", "PAN", "CAN", "SAN", "SDWAN", "MPLS", "mGRE", "vSwitch", "vNIC", "NFV", "hyperviseur", "liens satellites", "DSL", "internet par câble", "ligne louée", "métro-optique"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_nodes.png"
coverAlt: "Illustration symbolique de nœuds interconnectés formant un réseau."
coverCaption: "Libérer la puissance des fondamentaux de la mise en réseau."
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

Les principes fondamentaux de la mise en réseau jouent un rôle crucial dans le monde interconnecté d'aujourd'hui. Qu'il s'agisse de naviguer sur Internet, d'envoyer des courriers électroniques ou de diffuser des vidéos, toutes ces activités reposent sur une infrastructure réseau solide. Dans cet article, nous allons donner un aperçu des **fondamentaux des réseaux**, en commençant par le **modèle OSI** et les concepts d'**encapsulation**. Nous explorerons également les différentes **topologies de réseau** et leurs caractéristiques.

## Aperçu du modèle OSI et des concepts d'encapsulation

Le modèle **OSI (Open Systems Interconnection)** est un cadre conceptuel qui définit les fonctions d'un réseau en sept couches différentes. Chaque couche a des responsabilités spécifiques et interagit avec les couches supérieures et inférieures. Il est essentiel de comprendre le modèle OSI pour comprendre comment les données sont transmises et traitées sur un réseau.

### Couches du modèle OSI

{{< youtube id="G7aVKgGUe9c" >}}

1. **Couche 1 - Physique** : La couche physique traite de la transmission et de la réception de flux de bits bruts sur des supports physiques tels que des fils de cuivre, des câbles à fibres optiques ou des connexions sans fil.

2. **Couche 2 - Liaison de données** : La couche liaison de données est responsable de l'établissement et de la terminaison des connexions entre les périphériques du réseau. Elle gère également la détection et la correction des erreurs afin de garantir une transmission fiable des données.

3. **Couche 3 - Réseau** : La couche réseau facilite l'acheminement des paquets de données de la source à la destination à travers plusieurs nœuds du réseau. Elle traite les problèmes liés à la **congestion du réseau**, à l'**acheminement des paquets** et à l'**adressage IP**.

4. **Couche 4 - Transport** : La couche transport assure la distribution des données de bout en bout et établit une communication fiable entre la source et la destination. Elle gère la **segmentation des données**, le **contrôle du flux** et la **récupération des erreurs**.

5. **Couche 5 - Session** : La couche session établit, maintient et termine les sessions de communication entre les applications. Elle gère le **contrôle du dialogue** et la **synchronisation** entre les périphériques.

6. **Couche 6 - Présentation** : La couche présentation se concentre sur la **syntaxe** et la **sémantique** des informations échangées entre les applications. Elle gère le **chiffrement** des données, la **compression** et le **formatage** pour une interprétation correcte.

7. **Couche 7 - Application** : La couche application représente les applications et les services réseau réels utilisés par les utilisateurs finaux. Elle fournit des services tels que **le courrier électronique**, **le transfert de fichiers**, **la navigation sur le web** et **l'accès à distance**.

### Encapsulation et décapsulation des données dans le contexte du modèle OSI

{{< youtube id="_fPzeQ9PHhA" >}}

L'encapsulation des données est le processus qui consiste à ajouter des en-têtes et des bandes-annonces spécifiques au protocole à la charge utile à chaque couche du modèle OSI. Cette encapsulation permet aux données de traverser le réseau et d'atteindre la destination prévue. Inversement, la décapsulation consiste à retirer les en-têtes et les bandes-annonces ajoutés à chaque couche du modèle OSI pour extraire la charge utile d'origine.

Dans le contexte du modèle OSI, les éléments suivants contribuent à l'encapsulation et à la décapsulation des données :

- **En-tête Ethernet** : L'en-tête Ethernet contient des informations telles que les adresses MAC des appareils source et destination, le type de protocole Ethernet et les mécanismes de contrôle des erreurs.

- En-tête du protocole Internet (IP)** : L'en-tête IP comprend les adresses IP de la source et de la destination, l'identification des paquets, le temps de vie et d'autres paramètres essentiels pour la communication basée sur IP.

- En-tête du protocole de contrôle de transmission (TCP)/protocole de datagramme de l'utilisateur (UDP)** : Les en-têtes TCP et UDP contiennent les numéros de port, les numéros de séquence, les sommes de contrôle et d'autres informations pertinentes nécessaires à la communication de la couche transport.

- Drapeaux TCP** : Les drapeaux TCP indiquent des fonctions de contrôle et des options spécifiques au cours d'une session TCP. Il s'agit notamment de drapeaux permettant d'établir des connexions, d'accuser réception de données, de mettre fin à des connexions, etc.

- Charge utile** : Les données utiles sont les données réelles qui sont transmises, telles qu'une page web, un message électronique ou un fichier multimédia.

- **Maximum Transmission Unit (MTU)** : Le MTU représente la taille maximale d'un paquet de données qui peut être transmis sur un réseau sans fragmentation.

## Explorer les topologies de réseau et leurs caractéristiques

{{< youtube id="zbqrNg4C98U" >}}

Les topologies de réseau définissent la disposition physique ou logique des dispositifs de réseau et les interconnexions entre eux. Chaque topologie a ses propres forces et faiblesses, et le choix de la bonne topologie dépend de divers facteurs tels que l'évolutivité, la tolérance aux pannes et le coût.

### Topologie maillée

Dans une **topologie maillée**, chaque appareil est connecté à tous les autres appareils, formant ainsi un réseau entièrement interconnecté. Cette redondance offre une grande tolérance aux pannes, mais peut être coûteuse et complexe à mettre en œuvre. Les topologies maillées sont couramment utilisées dans les infrastructures critiques et les environnements informatiques à haute performance.

### Topologie en étoile/en étoile et en étoile

Dans une topologie **en étoile**, tous les appareils sont connectés à un concentrateur ou à un commutateur central. Le concentrateur agit comme un point central de connexion, facilitant la communication entre les appareils. Cette topologie est facile à gérer et offre un contrôle centralisé, mais elle peut créer un point de défaillance unique si le concentrateur tombe en panne.

### Topologie de bus

Dans une topologie **bus**, tous les appareils sont connectés à une seule ligne de communication, appelée bus. Les données sont transmises de manière séquentielle le long du bus et les appareils reçoivent les données qui leur sont destinées. Les topologies en bus sont simples et rentables, mais elles peuvent être confrontées à la congestion du réseau et leur évolutivité est limitée.

### Topologie en anneau

Dans une **topologie en anneau**, les appareils sont connectés en chaîne circulaire, chaque appareil se connectant au suivant et le dernier appareil se connectant au premier. Les données circulent dans une seule direction autour de l'anneau. Les topologies en anneau offrent un accès équitable et peuvent gérer des charges de trafic élevées, mais peuvent souffrir d'une interruption du réseau en cas de défaillance d'un appareil.

### Topologie hybride

Une **topologie hybride** combine plusieurs topologies pour former un réseau plus souple et plus évolutif. Par exemple, une combinaison de topologies en étoile et en anneau peut assurer la redondance et la tolérance aux pannes tout en maintenant l'évolutivité.

## Types et caractéristiques des réseaux

{{< youtube id="6a-roIeJ_a4" >}}

La mise en réseau englobe différents types de réseaux, chacun répondant à des besoins et à des cas d'utilisation spécifiques. Voici quelques types de réseaux courants :

### Réseau Peer-to-Peer (P2P)

Dans un **réseau pair à pair (P2P)**, les appareils se connectent directement les uns aux autres sans dépendre d'un serveur centralisé. Les réseaux P2P sont souvent utilisés pour le partage de fichiers, les applications collaboratives et les systèmes décentralisés.

### Réseau client-serveur

Un **réseau client-serveur** implique des clients, qui demandent des services ou des ressources, et des serveurs, qui fournissent ces services ou ces ressources. Les réseaux client-serveur sont largement utilisés dans les environnements d'entreprise, où le contrôle centralisé et la gestion des ressources sont essentiels.

### Réseau local (LAN)

Un **réseau local (LAN)** s'étend sur une petite zone géographique, comme un immeuble de bureaux ou une maison. Il permet aux appareils du réseau de communiquer et de partager des ressources. Les réseaux locaux sont généralement utilisés pour la communication interne, le partage de fichiers et d'imprimantes.

### Réseau métropolitain (MAN)

Un **réseau métropolitain (MAN)** couvre une zone géographique plus grande qu'un LAN mais plus petite qu'un WAN. Il relie plusieurs réseaux locaux au sein d'une ville ou d'une région métropolitaine. Les MAN sont souvent utilisés par les organisations qui ont besoin d'une connectivité à haut débit entre leurs succursales ou leurs campus.

### Réseau étendu (WAN)

Un **réseau étendu (WAN)** s'étend sur une vaste zone géographique, connectant plusieurs LAN ou MAN dans différentes villes, pays ou continents. Les WAN s'appuient sur diverses technologies de communication, telles que les lignes louées, les satellites et les réseaux optiques, pour transmettre des données sur de longues distances.

### Réseau local sans fil (WLAN)

Un **réseau local sans fil (WLAN)** fournit une connectivité sans fil dans une zone limitée, généralement à l'aide de la technologie Wi-Fi. Les WLAN sont couramment présents dans les foyers, les bureaux, les cafés et les espaces publics, permettant aux utilisateurs de connecter leurs appareils sans câbles physiques.

### Réseau personnel (PAN)

Un **réseau personnel (PAN)** couvre une petite zone, généralement dans l'espace de travail d'une personne ou dans son environnement immédiat. Il permet la communication entre les appareils personnels, tels que les smartphones, les tablettes et les appareils portables.

### Réseau de campus (CAN)

Un **réseau de campus (CAN)** est un réseau qui s'étend sur un campus universitaire ou un grand campus d'entreprise. Il fournit une connectivité aux différents bâtiments et installations du campus, facilitant ainsi la communication et le partage des ressources.

### Réseau de stockage (SAN)

Un **réseau de stockage (SAN)** est un réseau spécialisé conçu à des fins de stockage. Il permet à plusieurs serveurs d'accéder à des ressources de stockage partagées, telles que des baies de disques ou des bibliothèques de bandes, par le biais d'une connexion à haut débit.

### Réseau étendu défini par logiciel (SDWAN)

**Le réseau étendu défini par logiciel (SDWAN)** est une technologie qui simplifie la gestion et la configuration des réseaux étendus en séparant le plan de contrôle du réseau du matériel sous-jacent. Elle offre un contrôle centralisé et permet aux organisations de gérer dynamiquement leur infrastructure WAN.

### Commutation multiprotocole par étiquette (MPLS)

**La commutation multiprotocole par étiquette (MPLS)** est une technique de routage qui utilise des étiquettes pour acheminer efficacement les paquets de données sur un réseau. Elle permet une communication hautement performante, fiable et sécurisée, ce qui la rend adaptée aux fournisseurs de services et aux entreprises.

### Encapsulation de routage générique multipoint (mGRE)

**L'encapsulation générique multipoint (mGRE)** est une technique utilisée pour créer des réseaux privés virtuels (VPN) en encapsulant des paquets de données et en les envoyant sur un réseau multipoint. Elle permet une communication efficace entre plusieurs sites ou points d'extrémité.

## Concepts de réseaux virtuels

{{< youtube id="A29g5-Os-u8" >}}

Les technologies de virtualisation ont révolutionné la façon dont les réseaux sont conçus et gérés. Voici quelques concepts de réseaux virtuels :

### vSwitch

Un **vSwitch**, ou commutateur virtuel, est un commutateur réseau logiciel qui fonctionne dans un environnement virtualisé, tel qu'un hyperviseur. Il permet la communication entre les machines virtuelles (VM) et les connecte au réseau physique.

### Carte d'interface réseau virtuelle (vNIC)

Une **carte d'interface réseau virtuelle (vNIC)** est une carte d'interface réseau virtualisée qui émule un adaptateur réseau physique au sein d'une machine virtuelle. Elle permet aux machines virtuelles de communiquer avec le commutateur virtuel et le réseau physique.

### Virtualisation de la fonction réseau (NFV)

**La virtualisation des fonctions de réseau (NFV)** est une approche qui virtualise les fonctions de réseau, telles que les pare-feu, les routeurs et les équilibreurs de charge, en les exécutant sur des serveurs standard au lieu de dispositifs matériels dédiés. Elle offre une flexibilité, une évolutivité et une réduction des coûts dans l'infrastructure du réseau.

### Hyperviseur

Un **hyperviseur** est une couche logicielle qui permet la création et la gestion de machines virtuelles. Il fournit une abstraction matérielle, permettant à plusieurs machines virtuelles de fonctionner sur un seul serveur physique.

## Liens vers les fournisseurs

{{< youtube id="M2cJtZXJrpE" >}}

Les liens vers les fournisseurs font référence aux différents types d'options de connectivité proposées par les fournisseurs de services. Voici quelques liens de fournisseurs courants :

### Satellite

**Les liaisons par satellite** utilisent des satellites de communication pour transmettre des données sur de longues distances. Elles sont souvent utilisées dans les zones reculées où les autres options de connectivité sont limitées.

### Ligne d'abonné numérique (DSL)

**Ligne d'abonné numérique (DSL)** est une technologie qui permet d'accéder à l'internet à haut débit par l'intermédiaire des lignes téléphoniques existantes. Elle offre des vitesses plus élevées que les connexions commutées traditionnelles et est largement disponible dans les environnements résidentiels et professionnels.

### Câble

**L'internet par câble** utilise les mêmes câbles coaxiaux que ceux utilisés pour la télévision par câble afin de fournir un accès à l'internet à haut débit. Il est populaire dans les zones résidentielles et offre des vitesses plus élevées que le DSL.

### Ligne louée

Une **ligne louée** est une connexion point à point dédiée entre deux sites. Elle offre une connectivité fiable et sécurisée, ce qui la rend adaptée aux entreprises qui ont besoin d'une grande largeur de bande.

### Metro-Optical

**Les réseaux métro-optiques** utilisent la technologie de la fibre optique pour fournir une connectivité à haut débit au sein d'une zone métropolitaine. Ils offrent une grande largeur de bande et une faible latence, ce qui est idéal pour les applications à forte intensité de données.

______

En conclusion, il est essentiel de comprendre les principes fondamentaux des réseaux pour construire et maintenir des infrastructures de réseau fiables et efficaces. Le **modèle OSI** fournit un cadre permettant de comprendre comment les données sont transmises et traitées à travers les différentes couches du réseau. En outre, la connaissance des **topologies de réseau** aide à concevoir des réseaux qui répondent à des exigences spécifiques en matière d'évolutivité, de tolérance aux pannes et de rentabilité. En nous familiarisant avec les différents **types de réseaux**, les **concepts de réseaux virtuels** et les **liens avec les fournisseurs**, nous pouvons prendre des décisions éclairées lors de la mise en place et de la gestion des réseaux.

Références :
- [OSI Model - Cisco](https://learningnetwork.cisco.com/s/article/osi-model-reference-chart)
- [How Does the Internet Work? - Stanford University](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
