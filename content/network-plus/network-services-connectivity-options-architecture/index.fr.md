---
title: "Cours Réseau Plus : Exploration des services de réseau, des options de connectivité et de l'architecture"
date: 2023-07-04
toc: true
draft: false
description: "Découvrez les fonctionnalités des services DHCP, DNS et NTP, comprenez l'architecture des réseaux d'entreprise et des centres de données, et explorez les concepts de cloud et les options de connectivité pour une communication et une gestion des données transparentes."
genre: ["Technologie", "Mise en réseau", "Connectivité", "Échange de données", "Architecture du réseau", "Informatique en nuage", "Services de réseau", "DNS", "DHCP", "NTP"]
tags: ["services de réseau", "options de connectivité", "l'architecture", "DHCP", "DNS", "NTP", "réseau d'entreprise", "réseau de centres de données", "concepts de nuages", "connectivité", "architecture à trois niveaux", "réseau défini par logiciel", "architecture de la colonne vertébrale et des feuilles", "les flux de trafic", "succursale", "on-premises datacenter", "colocation", "réseaux de stockage", "Fibre Channel sur Ethernet", "iSCSI", "explorer le DHCP", "comprendre les DNS", "synchronisation de l'heure du réseau", "architecture des réseaux d'entreprise", "options de connectivité au nuage", "architecture de réseau à trois niveaux", "avantages des réseaux définis par logiciel", "l'architecture des réseaux de type spine et leaf (épine dorsale et feuille)", "connectivité en nuage pour les succursales", "les types de réseaux de stockage"]
cover: "/img/cover/A_cartoon_illustration_showcasing_various_networks.png"
coverAlt: "Illustration de bande dessinée présentant les différents composants du réseau et les options de connectivité en nuage"
coverCaption: "Libérer la puissance des services de réseau et de la connectivité en nuage"
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Introduction

Dans le monde des réseaux, divers services, options de connectivité et cadres architecturaux jouent un rôle crucial dans l'établissement d'une communication efficace et fiable. Cet article explore trois services réseau essentiels, à savoir le protocole de configuration dynamique des hôtes (DHCP), le système de noms de domaine (DNS) et le protocole de temps réseau (NTP). Nous nous pencherons sur leurs fonctionnalités, discuterons de l'architecture de base des réseaux d'entreprise et des centres de données, et donnerons un aperçu des concepts et des options de connectivité de l'informatique en nuage.

## DHCP : simplifier la configuration du réseau

{{< youtube id="e6-TaH5bkjo" >}}

**Le protocole DHCP (Dynamic Host Configuration Protocol) est un service réseau qui automatise l'attribution d'adresses IP et de paramètres de configuration réseau aux appareils connectés à un réseau. En attribuant dynamiquement des adresses IP, le DHCP simplifie le processus de configuration du réseau, en particulier dans les environnements à grande échelle.

### Portée et plages d'exclusion

Une portée DHCP définit une plage d'adresses IP pouvant être attribuées à des périphériques. À l'intérieur d'une étendue, des plages d'exclusion peuvent être définies pour réserver des adresses IP spécifiques à une attribution statique ou pour empêcher qu'elles soient attribuées dynamiquement à des périphériques.

### Réservation et attribution dynamique

Le protocole DHCP permet de réserver des adresses IP spécifiques pour les appareils nécessitant une attribution statique. Cela permet de s'assurer que les périphériques critiques, tels que les serveurs ou les imprimantes de réseau, reçoivent toujours la même adresse IP.

D'autre part, l'attribution dynamique consiste à attribuer les adresses IP disponibles à partir de l'étendue DHCP aux périphériques qui demandent une connectivité réseau. L'attribution dynamique est utile pour les périphériques qui n'ont pas besoin d'une adresse IP fixe.

### Temps de location et options d'étendue

Lorsqu'un appareil obtient une adresse IP d'un serveur DHCP, il le fait pour une période spécifique appelée durée du bail. Les délais de location peuvent être personnalisés pour répondre aux exigences de l'environnement réseau. En outre, les options d'étendue DHCP peuvent être configurées pour fournir des paramètres supplémentaires, tels que les adresses des serveurs DNS et les passerelles par défaut, aux appareils.

### Relais DHCP et aide IP/transfert UDP

Dans les grands réseaux, les agents de relais DHCP ou les adresses IP Helper sont utilisés pour transmettre les demandes et les réponses DHCP entre les clients et les serveurs DHCP situés dans des sous-réseaux différents. Cela permet de centraliser les services DHCP et d'assurer une attribution efficace des adresses IP sur plusieurs segments du réseau.

{{< inarticle-dark >}}

## DNS : Traduire les noms en adresses IP

{{< youtube id="mpQZVYPuDGU" >}}

**Le système de noms de domaine (DNS)** est un service réseau essentiel qui traduit les noms de domaine lisibles par l'homme en adresses IP correspondantes, ce qui permet aux appareils de se localiser et de communiquer entre eux sur l'internet et d'autres réseaux.

### Types d'enregistrements et hiérarchie globale

Le DNS utilise divers types d'enregistrements pour gérer différents types d'informations. Il s'agit notamment des types suivants

- **Adresse (A)** : Associe un nom de domaine à une adresse IPv4.
- **AAAA** : Associe un nom de domaine à une adresse IPv6.
- **Nom canonique (CNAME)** : Fournit un alias ou un nom alternatif pour un nom de domaine existant.
- **Échange de courrier (MX)** : Indique le serveur de messagerie responsable de l'acceptation des messages électroniques pour un domaine.
- **Start of authority (SOA)** : Contient des informations administratives sur une zone DNS.
- **Pointer (PTR)** : Effectue une recherche DNS inversée, en faisant correspondre une adresse IP à un nom de domaine.
- Texte (TXT)** : Stocke des données textuelles arbitraires associées à un domaine.
- Service (SRV)** : Définit l'emplacement de services spécifiques au sein d'un domaine.
- Serveur de noms (NS)** : Indique les serveurs DNS faisant autorité pour un domaine.

Ces enregistrements sont organisés dans une hiérarchie globale, en commençant par les serveurs DNS racine, qui stockent des informations sur les domaines de premier niveau (par exemple, .com, .org). Cette structure hiérarchique permet une résolution efficace et décentralisée des noms de domaine.

### DNS interne ou externe et transferts de zone

Le DNS peut être divisé en deux catégories : le DNS interne et le DNS externe. Le DNS interne gère la résolution des noms au sein du réseau privé d'une organisation, tandis que le DNS externe gère la résolution des domaines accessibles au public.

Les transferts de zone sont des mécanismes utilisés pour répliquer les données de la zone DNS entre les serveurs de noms faisant autorité. Ces transferts garantissent la cohérence et la mise à jour des informations sur plusieurs serveurs DNS.

### Mise en cache DNS et durée de vie (TTL)

La mise en cache DNS améliore les performances en stockant les correspondances entre les noms de domaine et les adresses IP récemment résolus. Les caches peuvent exister sur les serveurs DNS, les routeurs et même les appareils individuels. La valeur TTL (Time to Live) associée aux enregistrements DNS détermine la durée de validité des informations mises en cache avant qu'elles ne doivent être rafraîchies par les serveurs DNS faisant autorité.

### DNS inversé et recherche récursive

Le DNS inversé, également connu sous le nom de recherche inversée, est le processus de résolution d'une adresse IP vers son nom de domaine correspondant. La recherche récursive fait référence au processus de requête DNS au cours duquel un résolveur DNS parcourt la hiérarchie DNS pour obtenir l'adresse IP associée à un nom de domaine donné.

## NTP : Synchronisation du temps réseau

**Le protocole NTP (Network Time Protocol) est un protocole de réseau qui assure une synchronisation précise de l'heure entre les appareils et les réseaux. La précision de l'heure est essentielle pour de nombreuses fonctions du réseau, notamment l'authentification, la journalisation et la coordination entre les systèmes.

### Strate et sources de temps

NTP fonctionne sur la base d'un modèle hiérarchique appelé strate. La strate 0 représente la source de temps la plus précise, généralement fournie par des horloges atomiques ou des systèmes basés sur des satellites. Les serveurs de strate 1 synchronisent leur temps avec les sources de strate 0, et ainsi de suite.

### Clients et serveurs

Dans une infrastructure NTP, les clients interrogent les serveurs NTP pour obtenir des informations temporelles précises. Les serveurs NTP conservent des références temporelles précises et fournissent des services de synchronisation aux clients.

{{< inarticle-dark >}}

## Architecture des réseaux d'entreprise et des centres de données

{{< youtube id="23H0nA-_4YE" >}}

Pour garantir l'efficacité et l'évolutivité des opérations de réseau, les organisations mettent souvent en œuvre des cadres architecturaux spécifiques. Deux architectures de réseau couramment utilisées sont l'architecture à trois niveaux et l'architecture "spine and leaf".

### Architecture à trois niveaux

L'architecture à trois niveaux comprend les couches suivantes :

1. **Cœur** : La couche centrale assure une connectivité à haut débit entre les différentes parties du réseau et sert de colonne vertébrale pour la transmission des données.
2. **Couche de distribution/agrégation** : La couche de distribution regroupe les connexions provenant des commutateurs de la couche d'accès et assure l'application de la politique, le filtrage et les fonctions de sécurité.
3. **Couche d'accès/Edge** : La couche d'accès connecte au réseau les appareils des utilisateurs finaux, tels que les ordinateurs et les téléphones IP.

Cette architecture assure l'évolutivité, la tolérance aux pannes et la segmentation logique des services réseau.

### Réseau défini par logiciel

La mise en réseau définie par logiciel (SDN) est une approche architecturale qui sépare le plan de contrôle, responsable de la prise de décision sur le réseau, du plan de données, responsable de l'acheminement des données. Le SDN se compose des couches suivantes :

1. **Couche d'application** : Cette couche comprend les applications et services réseau qui interagissent avec le contrôleur SDN.
2. **Couche de contrôle** : La couche de contrôle comprend le contrôleur SDN, qui gère les politiques et la configuration du réseau.
3. **Couche infrastructure** : La couche infrastructure comprend les commutateurs et les routeurs du réseau qui transmettent les paquets de données selon les instructions du contrôleur SDN.
4. **Plan de gestion** : Le plan de gestion gère les tâches de gestion du réseau, telles que la surveillance, l'approvisionnement et la sécurité.

Le SDN offre flexibilité, gestion centralisée et programmabilité, ce qui permet aux entreprises d'adapter leur infrastructure réseau à l'évolution de leurs besoins.

### Architecture de l'épine dorsale et de la feuille

L'architecture "spine and leaf" est une solution évolutive et à large bande passante pour les réseaux de centres de données. Elle se compose des éléments suivants :

- **Réseau défini par logiciel** : L'architecture spine and leaf s'appuie souvent sur les principes SDN pour un contrôle centralisé et la programmabilité.
- **Commutation au sommet du rack** : Chaque rack du centre de données est connecté à un commutateur en tête de rack, qui fournit une connectivité aux serveurs et autres dispositifs.
- Backbone** : La couche dorsale est constituée de commutateurs à grande vitesse qui interconnectent tous les commutateurs secondaires.
- Flux de trafic** : Dans l'architecture "spine" et "leaf", les flux de trafic se produisent à la fois dans le sens nord-sud (entre le centre de données et les réseaux externes) et dans le sens est-ouest (entre les serveurs au sein du centre de données).

Cette architecture permet d'améliorer les performances, l'évolutivité et la tolérance aux pannes dans les environnements de centres de données.

## Concepts du cloud et options de connectivité

L'informatique en nuage a révolutionné la manière dont les entreprises stockent, traitent et accèdent aux données et aux applications. Il est essentiel de comprendre les concepts de l'informatique en nuage et les options de connectivité pour tirer parti des avantages des services en nuage.

### Branch Office vs. On-Premises Datacenter vs. Colocation

{{< youtube id="-V2NJCS6qSE" >}}

Lorsqu'elles envisagent de recourir à la connectivité en nuage, les entreprises doivent choisir entre différentes options de déploiement, notamment :

- **Les succursales** : Les succursales se connectent généralement au nuage par le biais de connexions réseau dédiées, telles que des tunnels MPLS ou VPN.
- **Centre de données sur site** : Les centres de données sur site peuvent établir des connexions directes avec les fournisseurs de services en nuage, ce qui permet une connectivité sécurisée et à faible latence.
- **Colocation** : Les entreprises qui hébergent leur infrastructure dans des centres de données tiers peuvent exploiter les options de connectivité du centre de données, telles que les connexions croisées directes avec les fournisseurs de services en nuage.

Chaque option de déploiement comporte des considérations uniques en matière de conception, de sécurité et de performance du réseau.

### Réseaux de stockage

{{< youtube id="prkPpAPm4lA" >}}

Les réseaux de stockage (SAN) offrent une connectivité de stockage haute performance sur des réseaux dédiés. Les SAN prennent en charge différents types de connexion, notamment

- **Fibre Channel over Ethernet (FCoE)** : FCoE permet de transporter le trafic de stockage Fibre Channel sur des réseaux Ethernet, réduisant ainsi le besoin de réseaux séparés spécifiques au stockage.
- **Fibre Channel** : Fibre Channel est un protocole de stockage à grande vitesse qui facilite les transferts de données rapides et fiables entre les serveurs et les dispositifs de stockage.
- iSCSI (Internet Small Computer Systems Interface) : iSCSI permet un accès au stockage au niveau du bloc sur les réseaux IP, ce qui en fait une alternative abordable et flexible à Fibre Channel.

Les réseaux de stockage SAN sont essentiels pour les applications nécessitant un accès rapide et à faible latence aux ressources de stockage.

## Conclusion

Les services de réseau, les options de connectivité et les cadres architecturaux constituent la base de la communication moderne et de l'échange de données. Le protocole DHCP simplifie la configuration du réseau, le protocole DNS traduit les noms de domaine en adresses IP et le protocole NTP assure une synchronisation précise du temps. La compréhension de l'architecture des réseaux d'entreprise et des centres de données, comme l'architecture à trois niveaux et l'architecture spine et leaf, permet de concevoir des réseaux évolutifs et efficaces. En outre, une bonne connaissance des concepts du cloud et des options de connectivité permet aux entreprises de prendre des décisions éclairées quant à l'utilisation des services du cloud. En maîtrisant ces concepts fondamentaux, les administrateurs réseau peuvent construire des infrastructures réseau robustes et fiables qui répondent aux besoins évolutifs des entreprises.

## Références

- DHCP : [https://www.ietf.org/rfc/rfc2131.txt](https://www.ietf.org/rfc/rfc2131.txt)
- DNS : [https://www.ietf.org/rfc/rfc1035.txt](https://www.ietf.org/rfc/rfc1035.txt)
- NTP : [https://www.ietf.org/rfc/rfc958.txt](https://www.ietf.org/rfc/rfc958.txt)
- Concepts de l'informatique en nuage : [https://aws.amazon.com/what-is-cloud-computing/](https://aws.amazon.com/what-is-cloud-computing/)
