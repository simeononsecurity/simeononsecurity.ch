---
title: "Les bases du réseau : commutateurs, routeurs, pare-feu et DMZ"
draft: false
toc: true
date: 2023-07-21
lastmod: 2026-11-15
description: "Découvrez comment les commutateurs, routeurs, passerelles, sous-réseaux, pare-feu et DMZ répartissent le trafic réseau et appliquent des limites de sécurité."
genre: ["Réseaux", "Infrastructure informatique", "Sécurité réseau", "Architecture réseau", "Cybersécurité", "Communication de données", "Technologies de l'information", "Notions fondamentales en informatique", "Gestion des réseaux", "Connectivité Internet"]
tags: ["bases des réseaux", "commutateurs", "routeurs", "passerelles", "sous-réseaux", "pare-feu", "DMZ", "réseau local", "LAN", "connectivité réseau", "accès Internet", "gestion des adresses IP", "segmentation réseau", "sécurité réseau", "sous-réseautage", "protection par pare-feu", "performances réseau", "architecture réseau", "communication de données", "gestion des réseaux", "cybersécurité", "infrastructure réseau", "notions fondamentales en informatique", "technologies de l'information", "gestion du trafic de données", "sécurité informatique", "conception réseau", "conformité informatique", "protocoles réseau", "dépannage réseau", "administration réseau"]
cover: "/img/cover/A_symbolic_illustration_showing_interconnected.webp"
coverAlt: "Illustration symbolique d'appareils interconnectés par des commutateurs, des routeurs, des passerelles et des pare-feu."
coverCaption: "Les bases des réseaux aident à créer des réseaux sûrs et fiables."
---

## Introduction

Dans un monde technologique en évolution rapide, les réseaux relient les appareils et permettent la communication. Comprendre les bases des réseaux est essentiel pour les professionnels de l'informatique et pour toute personne souhaitant approfondir ses connaissances. Cet article présente les principaux composants réseau, notamment les commutateurs, les routeurs, les passerelles, les sous-réseaux, les pare-feu et les DMZ. À la fin, vous comprendrez ces notions et leur importance pour construire des réseaux fiables et sûrs.

{{< youtube id="_IOZ8_cPgu8" >}}

## Commutateurs : améliorer les performances du réseau local

{{< youtube id="NDVImep5UBI" >}}

Un **commutateur** est un équipement réseau qui fonctionne au niveau liaison de données du modèle OSI. Il relie plusieurs appareils au sein d'un réseau local (LAN) et achemine des paquets de données entre eux. Contrairement aux concentrateurs, qui diffusent les données à tous les appareils connectés, les commutateurs transmettent les paquets uniquement à leur destinataire. Cela réduit les collisions et la congestion et améliore les performances du réseau.

Principales fonctions et avantages des commutateurs :

- **Transmission par port** : chaque port du commutateur reçoit une adresse unique de contrôle d'accès au support (MAC), ce qui permet d'acheminer les paquets directement vers l'appareil cible.
- **Réseaux locaux virtuels (VLAN)** : les VLAN permettent de segmenter le réseau et d'améliorer la sécurité en isolant le trafic de différents groupes d'appareils.
- **Qualité de service (QoS)** : les commutateurs peuvent donner la priorité à certains types de trafic afin que les applications sensibles à la latence, comme la voix et la vidéo, disposent d'une bande passante suffisante.

______

## Routeurs : relier des réseaux et permettre l'accès à Internet

{{< youtube id="lyIUgr9JOLs" >}}

Les commutateurs fonctionnent au sein d'un LAN, tandis que les **routeurs** relient plusieurs réseaux. Ils fonctionnent au niveau réseau du modèle OSI et utilisent des protocoles de routage pour choisir le meilleur chemin vers la destination des paquets. En plus d'interconnecter les réseaux, ils permettent aux appareils d'accéder à Internet.

Principales fonctions et avantages des routeurs :

- **Gestion des adresses IP** : ils utilisent les adresses IP pour identifier et acheminer les paquets entre différents réseaux.
- **Traduction d'adresses réseau (NAT)** : ils convertissent les adresses IP privées utilisées dans un LAN en adresses IP publiques lors des communications avec Internet.
- **Fonctions de pare-feu** : de nombreux routeurs intègrent des fonctions de pare-feu élémentaires qui protègent le réseau contre les accès non autorisés.
- **Protocole de configuration dynamique des hôtes (DHCP)** : ils peuvent agir comme serveurs DHCP et attribuer automatiquement des adresses IP aux appareils du réseau.

______

## Passerelles : relier différents types de réseaux

{{< youtube id="SXZC6D7TRfM" >}}

Une **passerelle** est un appareil ou un composant logiciel qui relie des réseaux utilisant des protocoles ou des architectures différents et permet leur communication. Elle joue un rôle d'intermédiaire et convertit les paquets d'un format réseau à un autre. Elle peut, par exemple, relier un réseau local à Internet.

Principales fonctions et avantages des passerelles :

- **Traduction des protocoles** : elles convertissent les paquets afin que des réseaux utilisant des protocoles de communication différents puissent échanger des informations.
- **Intégration des réseaux** : elles intègrent des réseaux aux architectures différentes et facilitent leur communication.
- **Application de mesures de sécurité** : elles mettent souvent en œuvre le filtrage des paquets ou le chiffrement afin de sécuriser les transmissions entre réseaux.

______

## Sous-réseaux : organiser les réseaux pour communiquer efficacement

{{< youtube id="nR5xCmXJE5E" >}}

Un **sous-réseau** est une subdivision logique d'un réseau IP. Le découpage d'un réseau en sous-réseaux plus petits et plus faciles à gérer peut améliorer les performances et la sécurité. Le masque de sous-réseau définit chaque sous-réseau et la plage d'adresses IP qui lui est attribuée.

Avantages des sous-réseaux :

- **Meilleures performances** : la division d'un grand réseau en sous-réseaux localise le trafic, réduit la congestion générale et améliore les performances.
- **Sécurité renforcée** : des règles de contrôle d'accès peuvent limiter les communications entre sous-réseaux et ajouter une couche de protection.
- **Gestion simplifiée** : le regroupement logique des appareils facilite l'attribution des adresses IP, le routage et le dépannage.

______

## Pare-feu : protéger les réseaux contre les accès non autorisés

{{< youtube id="kDEX1HXybrU" >}}

Un **pare-feu** est un équipement de sécurité réseau qui surveille et contrôle le trafic entrant et sortant selon des règles de sécurité prédéfinies. Il forme une barrière entre les réseaux internes et les réseaux externes, comme Internet, afin d'empêcher les accès non autorisés et les menaces potentielles.

Principales fonctions et avantages des pare-feu :

- **Filtrage des paquets** : ils inspectent les paquets entrants et sortants et filtrent le trafic potentiellement malveillant selon des règles établies.
- **Système de prévention des intrusions (IPS)** : les pare-feu dotés d'un IPS peuvent détecter et empêcher des attaques réseau, notamment les infections par des logiciels malveillants et les tentatives d'intrusion.
- **Prise en charge des réseaux privés virtuels (VPN)** : de nombreux pare-feu prennent en charge les VPN pour fournir un accès distant sécurisé via Internet.
- **Contrôle des applications** : les pare-feu avancés inspectent la couche applicative et permettent un contrôle précis des applications et de leur utilisation du réseau.

______

## DMZ : renforcer la sécurité du réseau

{{< youtube id="dqlzQXo1wqo" >}}

Une **zone démilitarisée (DMZ)** est un segment réseau situé entre un réseau interne et des réseaux externes comme Internet. Elle isole du réseau interne les services accessibles au public, tels que les serveurs Web ou de messagerie, et ajoute une couche de sécurité supplémentaire.

Principaux avantages et usages des DMZ :

- **Sécurité améliorée** : l'hébergement des services publics dans une DMZ réduit le risque que des attaquants atteignent le réseau interne.
- **Surface d'attaque réduite** : seuls les services nécessaires sont exposés à Internet, ce qui limite les voies d'attaque possibles.
- **Conformité réglementaire** : des normes telles que Payment Card Industry Data Security Standard (PCI DSS) exigent souvent une DMZ afin de protéger les données sensibles des clients.

______

## Séquence de dépannage 2026

Effectuez les vérifications du client vers l'extérieur. Vérifiez l'état de la liaison, l'attribution de l'adresse, la passerelle par défaut, la résolution DNS, le choix de la route, la règle du pare-feu et le service applicatif. Avant de modifier une règle, consignez l'adresse source, la destination, le protocole, le port, l'horodatage et l'erreur observée.

Effectuez des captures de paquets uniquement sur les réseaux que vous possédez ou administrez. Placez les interfaces de gestion sur un réseau à accès restreint, segmentez les appareils invités et IoT, puis examinez le chemin créé par chaque redirection de port. Le [glossaire réseau du NIST](https://csrc.nist.gov/glossary) et les [avis de la CISA](https://www.cisa.gov/news-events/cybersecurity-advisories) sont des références utiles sur la terminologie et les risques actuels.

## Conclusion

Comprendre les composants réseau est essentiel pour créer et maintenir des réseaux efficaces, sûrs et fiables. Cet article a présenté les fonctions et les avantages des commutateurs, des routeurs, des passerelles, des sous-réseaux, des pare-feu et des DMZ. Ces notions vous aideront à concevoir et à gérer des réseaux répondant aux besoins actuels de connectivité.

Tenez toujours compte des exigences propres à votre réseau et consultez la documentation et les réglementations gouvernementales pertinentes, comme les normes **Federal Information Processing Standards (FIPS)** et les directives du **National Institute of Standards and Technology (NIST)**, pour respecter les bonnes pratiques et les exigences de conformité.

## Références

- Federal Information Processing Standards (FIPS) : [https://www.nist.gov/itl/fips](https://www.nist.gov/itl/fips)
- National Institute of Standards and Technology (NIST) : [https://www.nist.gov/](https://www.nist.gov/)
