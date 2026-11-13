---
title: "Notions de réseau : sous-réseaux, découpage en sous-réseaux et conception des VLAN"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Découvrez les bases des sous-réseaux, du découpage en sous-réseaux et des VLAN pour gérer efficacement votre réseau et renforcer sa sécurité."
genre: ["Notions de réseau", "Découpage en sous-réseaux", "VLAN", "Gestion réseau", "Sécurité réseau", "Adressage IP", "Segmentation réseau", "Utilisation efficace des ressources", "Performances réseau", "IPv4"]
tags: ["notions de réseau", "sous-réseaux", "découpage en sous-réseaux", "VLAN", "gestion réseau", "sécurité réseau", "adressage IP", "segmentation réseau", "utilisation efficace des ressources", "performances réseau", "IPv4", "configuration de sous-réseau", "masques de sous-réseau", "attribution d’adresses IP", "communication inter-VLAN", "ports de commutateur", "configuration VLAN", "interfaces VLAN", "connectivité réseau", "réseaux subdivisés", "domaines de diffusion", "mesures de sécurité", "plage d’adresses IP", "exemples de sous-réseaux", "déploiement VLAN", "administration réseau", "configuration de commutateur", "configuration de routeur", "évolutivité réseau", "communication et transfert de données", "réseaux efficaces"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Illustration symbolique de réseaux informatiques interconnectés avec des sous-réseaux et des VLAN"
coverCaption: "Créer des réseaux efficaces : les sous-réseaux et VLAN en termes simples."
---

## Notions de réseau : sous-réseaux, découpage en sous-réseaux et conception des VLAN

### Introduction

Dans notre monde connecté, les réseaux informatiques jouent un rôle essentiel dans la communication et le transfert des données. Les bases du réseau sont utiles aux professionnels de l’informatique comme aux utilisateurs. Cet article présente les sous-réseaux, le découpage en sous-réseaux et les VLAN, leur objectif et leur fonctionnement.

## Sous-réseaux : explication détaillée

### Qu’est-ce qu’un sous-réseau ?

{{< youtube id="nR5xCmXJE5E" >}}

Un **sous-réseau** est une subdivision logique d’un réseau IP. Il permet à l’administrateur de diviser un grand réseau en segments plus petits et plus faciles à gérer. Chaque sous-réseau possède sa propre plage d’adresses IP, ce qui favorise leur utilisation efficace.

### Pourquoi utiliser des sous-réseaux ?

Les réseaux informatiques utilisent les sous-réseaux pour plusieurs raisons :

1. **Segmentation du réseau :** Les sous-réseaux divisent un grand réseau en réseaux plus petits. Cela améliore les performances et réduit la congestion.

2. **Sécurité renforcée :** La séparation des appareils en sous-réseaux permet d’appliquer des pare-feu et des listes de contrôle d’accès pour gérer le trafic et renforcer la sécurité.

3. **Utilisation efficace des ressources :** Le découpage en sous-réseaux répartit mieux les adresses IP, une ressource limitée en IPv4.

### Comment créer des sous-réseaux ?

{{< youtube id="LdSAaSHfK3M" >}}

Le découpage en sous-réseaux consiste à diviser un réseau en sous-réseaux plus petits. Suivez ces étapes :

1. **Définir les besoins du réseau :** Déterminez le nombre de sous-réseaux et d’hôtes nécessaires dans chacun.

2. **Choisir un plan d’adressage IP :** Sélectionnez un plan adapté au nombre de sous-réseaux et d’hôtes requis.

3. **Calculer les masques de sous-réseau :** Déterminez les masques selon le nombre de sous-réseaux et d’hôtes nécessaires.

4. **Attribuer les adresses IP :** Affectez des adresses à chaque sous-réseau et vérifiez leur appartenance à la bonne plage.

5. **Tester et vérifier :** Testez la connectivité et contrôlez les adresses IP attribuées.

### Exemples de découpage en sous-réseaux

Prenons un exemple simple de découpage en sous-réseaux :

Supposons que nous disposions de la plage 192.168.0.0/24 et souhaitions créer quatre sous-réseaux avec le même nombre d’hôtes. Voici comment diviser ce réseau :

1. **Étape 1 : Définir les besoins du réseau :** Il nous faut quatre sous-réseaux avec le même nombre d’hôtes.

2. **Étape 2 : Choisir un plan d’adressage IP :** Nous choisissons un masque /26, qui fournit 64 adresses par sous-réseau.

3. **Étape 3 : Calculer les masques de sous-réseau :** Le masque /26 est 255.255.255.192.

4. **Étape 4 : Attribuer les adresses IP :** Nous attribuons les adresses suivantes aux sous-réseaux :

   - sous-réseau 1: 192.168.0.0/26
   - sous-réseau 2: 192.168.0.64/26
   - sous-réseau 3: 192.168.0.128/26
   - sous-réseau 4: 192.168.0.192/26

5. **Étape 5 : Tester et vérifier :** Nous vérifions la connectivité entre les appareils de chaque sous-réseau.

### Tableaux utiles de découpage en sous-réseaux

#### Tableau de référence pour le calcul des sous-réseaux

| Masque de sous-réseau | Notation CIDR | Nombre total d’adresses IP | Adresses IP utilisables |
|-------------|---------------|--------------------|---------------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /19 | 255.255.224.0 | 8,192 | 8,190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32,768 | 32,766 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /15 | 255.254.0.0 | 131,072 | 131,070 |
| /14 | 255.252.0.0 | 262,144 | 262,142 |
| /13 | 255.248.0.0 | 524,288 | 524,286 |
| /12 | 255.240.0.0 | 1,048,576 | 1,048,574 |
| /11 | 255.224.0.0 | 2,097,152 | 2,097,150 |
| /10 | 255.192.0.0 | 4,194,304 | 4,194,302 |
| /9 | 255.128.0.0 | 8,388,608 | 8,388,606 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /7 | 254.0.0.0 | 33,554,432 | 33,554,430 |
| /6 | 252.0.0.0 | 67,108,864 | 67,108,862 |
| /5 | 248.0.0.0 | 134,217,728 | 134,217,726 |
| /4 | 240.0.0.0 | 268,435,456 | 268,435,454 |
| /3 | 224.0.0.0 | 536,870,912 | 536,870,910 |
| /2 | 192.0.0.0 | 1,073,741,824 | 1,073,741,822 |
| /1 | 128.0.0.0 | 2,147,483,648 | 2,147,483,646 |
| /0 | 0.0.0.0 | 4,294,967,296 | 4,294,967,294 |

#### Tableau des sous-réseaux utilisables

| Notation CIDR | Nombre de sous-réseaux utilisables |
|---------------|-------------------------|
| /0 | 1 |
| /1 | 2 |
| /2 | 4 |
| /3 | 8 |
| /4 | 16 |
| /5 | 32 |
| /6 | 64 |
| /7 | 128 |
| /8 | 256 |
| /9 | 512 |
| /10 | 1024 |
| /11 | 2048 |
| /12 | 4096 |
| /13 | 8192 |
| /14 | 16384 |
| /15 | 32768 |
| /16 | 65536 |
| /17 | 131072 |
| /18 | 262144 |
| /19 | 524288 |
| /20 | 1048576 |
| /21 | 2097152 |
| /22 | 4194304 |
| /23 | 8388608 |
| /24 | 16777216 |
| /25 | 33554432 |
| /26 | 67108864 |
| /27 | 134217728 |
| /28 | 268435456 |
| /29 | 536870912 |
| /30 | 1073741824 |
| /31 | 2147483648 |
| /32 | 4294967296 |

#### Tableau des puissances de deux

| Puissance de deux | Valeur |
|--------------|-------|
| 2^32 | 4294967296 |
| 2^31 | 2147483648 |
| 2^30 | 1073741824 |
| 2^29 | 536870912 |
| 2^28 | 268435456 |
| 2^27 | 134217728 |
| 2^26 | 67108864 |
| 2^25 | 33554432 |
| 2^24 | 16777216 |
| 2^23 | 8388608 |
| 2^22 | 4194304 |
| 2^21 | 2097152 |
| 2^20 | 1048576 |
| 2^19 | 524288 |
| 2^18 | 262144 |
| 2^17 | 131072 |
| 2^16 | 65536 |
| 2^15 | 32768 |
| 2^14 | 16384 |
| 2^13 | 8192 |
| 2^12 | 4096 |
| 2^11 | 2048 |
| 2^10 | 1024 |
| 2^9 | 512 |
| 2^8 | 256 |
| 2^7 | 128 |
| 2^6 | 64 |
| 2^5 | 32 |
| 2^4 | 16 |
| 2^3 | 8 |
| 2^2 | 4 |
| 2^1 | 2 |
| 2^0 | 1 |

## VLAN : réseaux locaux virtuels

### Qu’est-ce qu’un VLAN ?

{{< youtube id="jC6MJTh9fRE" >}}

Un **VLAN (Virtual Local Area Network)** est un groupe logique d’appareils dans un réseau, quelle que soit leur position physique. Les VLAN créent des domaines de diffusion distincts et améliorent la flexibilité, la sécurité et l’évolutivité du réseau.

### Pourquoi utiliser des VLAN ?

Les VLAN présentent plusieurs avantages pour la gestion des réseaux :

1. **Sécurité renforcée :** Les VLAN isolent les données sensibles et limitent les accès non autorisés. Le trafic reste dans des segments définis, ce qui protège les ressources importantes.

2. **Meilleures performances :** Les VLAN séparent logiquement le trafic, réduisent la congestion et améliorent les performances. Le trafic de diffusion reste limité au VLAN.

3. **Gestion simplifiée :** Les VLAN regroupent les appareils par fonction, service ou autre critère logique, ce qui simplifie l’administration et la configuration.

### Configuration des VLAN

La configuration d’un VLAN suit généralement ces étapes :

1. **Définir les besoins du VLAN :** Déterminez son objectif et son périmètre. Identifiez les appareils et leur affectation aux VLAN.

2. **Attribuer des ID VLAN :** Attribuez un ID unique à chaque VLAN. Les ID sont généralement compris entre 1 et 4094, certains étant réservés.

3. **Configurer les ports du commutateur :** Affectez les ports aux VLAN appropriés en mode access ou trunk.

4. **Configurer les interfaces VLAN :** Si la communication entre VLAN est nécessaire, [configurez les interfaces VLAN](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/) sur un commutateur de couche 3 ou un routeur.

5. **Tester et vérifier :** Vérifiez la connectivité entre les appareils de chaque VLAN.

### Tableau des VLAN réservés

| Étiquettes VLAN | Description |
|-------------------|----------------------------------------------------|
| VLAN 0 | ID VLAN réservé, ne pas utiliser |
| VLAN 1 | VLAN par défaut de nombreux équipements réseau |
| VLAN 2 | VLAN par défaut pour le trafic de gestion |
| VLAN 3-4 | ID VLAN réservés |
| VLAN 5 | Réservé à l’ID VLAN Token Ring |
| VLAN 6-1001 | ID VLAN réservés |
| VLAN 1002-1005 | VLAN par défaut de Cisco pour des usages spécifiques |
| VLAN 1006-1024 | ID VLAN réservés |
| VLAN 1025-4094 | Réservé à la plage VLAN étendue |
| VLAN 4095 | ID VLAN réservé, ne pas utiliser |

## Conclusion

[Comprendre les sous-réseaux](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) et les VLAN est essentiel pour concevoir et gérer des réseaux informatiques efficaces. Les sous-réseaux segmentent le réseau pour améliorer ses performances et sa sécurité. Les VLAN regroupent logiquement les appareils et facilitent la gestion. Les étapes de cet article aident les administrateurs à découper leur réseau et à configurer les VLAN selon leurs besoins.

Les bases du réseau constituent le socle de réseaux robustes et évolutifs, adaptés aux besoins actuels de communication et de transfert de données.

## Références

- [Bases du subnetting](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Comprendre et configurer les VLAN](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [Norme IEEE 802.1Q](https://standards.ieee.org/standard/802_1Q-2018.html)
