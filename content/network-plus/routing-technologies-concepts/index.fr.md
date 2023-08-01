---
title: "Cours Réseau Plus : Protocoles de routage, concepts et optimisation"
date: 2023-07-07
toc: true
draft: false
description: "Explorer le monde des technologies et des concepts de routage, des protocoles de routage dynamiques tels que RIP, OSPF, EIGRP et BGP aux protocoles de routage à état de liens, à vecteur de distance et hybrides, ainsi que la configuration du routage statique et des itinéraires par défaut."
genre: ["Technologie", "Mise en réseau", "Routage", "Protocoles de réseau", "Gestion du réseau", "Routage dynamique", "Routage statique", "Gestion de la bande passante", "Qualité du service", "Dispositifs de réseau"]
tags: ["technologies de routage", "les protocoles de routage dynamique", "RIP", "OSPF", "EIGRP", "BGP", "état du lien", "vecteur de distance", "protocoles de routage hybrides", "routage statique", "routes par défaut", "distance administrative", "routage extérieur", "routage intérieur", "le temps de vivre", "gestion de la bande passante", "mise en forme du trafic", "la qualité du service", "dispositifs de réseau", "routeurs", "interrupteurs", "pare-feu", "équilibreurs de charge", "points d'accès", "optimisation du réseau", "performance du réseau", "sécurité des réseaux", "architecture du réseau", "le trafic sur le réseau"]
cover: "/img/cover/An_illustration_of_interconnected_network_devi.png"
coverAlt: "Illustration de dispositifs de réseau interconnectés entre lesquels circulent des données."
coverCaption: "Naviguer sur l'autoroute numérique : Optimiser le routage des réseaux pour des performances maximales"
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Introduction

Dans le monde interconnecté d'aujourd'hui, un routage efficace des réseaux est essentiel pour une transmission et une communication fluides des données. Les technologies et les concepts de routage jouent un rôle crucial dans l'orientation du trafic réseau et l'optimisation des performances du réseau. Cet article explore différents protocoles de routage, tels que RIP, OSPF, EIGRP et BGP, ainsi que les protocoles de routage à état de liens, à vecteur de distance et hybrides. Nous nous pencherons également sur la configuration et l'utilisation du routage statique et des routes par défaut. En outre, nous comparerons et opposerons différents dispositifs et leur emplacement sur le réseau.

{{< youtube id="YRzr56cwgCg" >}}

## Protocoles de routage dynamique

Les protocoles de routage dynamique sont conçus pour automatiser le processus d'échange d'informations de routage entre les routeurs. Ils s'adaptent aux changements du réseau, tels que les modifications de la topologie ou les défaillances de liaison, en mettant à jour les tables de routage de manière dynamique. Examinons de plus près certains protocoles de routage dynamique couramment utilisés :

### Routage Internet Protocol (RIP)

Le Routing Internet Protocol (RIP) est un protocole de routage à vecteur de distance qui fonctionne sur la base du nombre de sauts entre les routeurs. Il utilise la métrique du nombre de sauts pour déterminer le meilleur chemin vers un réseau de destination. Le RIP prend en charge les protocoles IPv4 et IPv6 et convient aux réseaux de petite et moyenne taille.

### Open Shortest Path First (OSPF)

Open Shortest Path First (OSPF) est un protocole de routage à état de liens qui calcule le chemin le plus court vers une destination à l'aide de l'algorithme de Dijkstra. Il prend en compte diverses mesures, telles que la largeur de bande, le délai et la fiabilité, pour déterminer l'itinéraire optimal. OSPF est largement utilisé dans les grands réseaux d'entreprise en raison de son évolutivité et de sa convergence rapide.

### Protocole de routage de passerelle intérieure amélioré (EIGRP)

Le protocole EIGRP (Enhanced Interior Gateway Routing Protocol) est un protocole de routage hybride développé par Cisco. Il combine les meilleures caractéristiques des protocoles à vecteur de distance et à état de liens. L'EIGRP utilise l'algorithme de mise à jour par diffusion (DUAL) pour calculer les itinéraires et offre des fonctions avancées telles que l'équilibrage de la charge à coût inégal et le résumé des itinéraires.

### Protocole de passerelle frontalière (BGP)

Border Gateway Protocol (BGP) est un protocole de passerelle extérieure utilisé pour le routage entre les systèmes autonomes (AS) sur Internet. Le BGP est très évolutif et permet aux systèmes autonomes d'échanger des informations de routage. Il utilise des attributs de chemin et des politiques pour prendre des décisions de routage basées sur des facteurs tels que les politiques de réseau, la longueur du chemin et le chemin AS.

## Protocoles de routage à état de liens, à vecteur de distance et hybrides

Les protocoles de routage peuvent être classés en protocoles à état de liens, à vecteur de distance et hybrides en fonction de leur fonctionnement et des informations qu'ils utilisent pour déterminer les itinéraires.

### Protocoles de routage à état de liens

Les protocoles de routage à état de liens, comme OSPF, maintiennent une carte détaillée de l'ensemble du réseau en échangeant des informations sur l'état des liens entre les routeurs. Chaque routeur construit une base de données topologique, ce qui lui permet de calculer le meilleur chemin vers un réseau de destination en fonction de diverses mesures.

### Protocoles de routage à vecteur de distance

Les protocoles de routage à vecteur de distance, tels que RIP, utilisent une métrique simple (comme le nombre de sauts) et échangent des informations de routage avec les routeurs voisins. Les routeurs annoncent périodiquement leurs tables de routage aux routeurs voisins, ce qui leur permet de se faire une idée du réseau. Les protocoles à vecteur de distance ont une connaissance limitée de l'ensemble du réseau et peuvent être sujets à des boucles de routage.

### Protocoles de routage hybrides

Les protocoles de routage hybrides, comme l'EIGRP, combinent les caractéristiques des protocoles à état de liens et des protocoles à vecteur de distance. Ils maintiennent une table topologique similaire à celle des protocoles à état de liens, mais utilisent des algorithmes à vecteur de distance pour calculer les itinéraires. Les protocoles hybrides offrent les avantages d'une convergence plus rapide et d'une réduction des frais généraux.

{{< inarticle-dark >}}

## Routage statique et routes par défaut

Le routage statique consiste à configurer manuellement la table de routage des routeurs, en spécifiant les chemins d'accès à des réseaux spécifiques. Il est généralement utilisé dans des scénarios où les changements de topologie du réseau sont minimes ou prévisibles. Les routes statiques sont faciles à configurer et peuvent être utiles pour les petits réseaux ou les segments de réseau spécifiques.

Une route par défaut, également connue sous le nom de passerelle de dernier recours, est utilisée lorsqu'il n'existe pas de route explicite pour un réseau de destination. Elle agit comme une route fourre-tout et est configurée sur les routeurs pour diriger le trafic vers une passerelle par défaut lorsque le routeur ne connaît pas le réseau de destination.

## Distance administrative, extérieur vs intérieur, et durée de vie

{{< youtube id="HR59xk4umWY" >}}

### Distance administrative

La distance administrative (AD) est une valeur attribuée aux protocoles de routage pour déterminer la priorité des itinéraires lorsque plusieurs protocoles sont exécutés sur un routeur. Des valeurs de distance administrative plus faibles indiquent une priorité plus élevée pour un protocole de routage particulier. Par exemple, la distance administrative de l'OSPF (110) est inférieure à celle du RIP (120), de sorte que les itinéraires OSPF seront préférés aux itinéraires RIP.

### Routage extérieur et routage intérieur

Les protocoles de routage extérieur, comme BGP, sont utilisés pour échanger des informations de routage entre les systèmes autonomes (AS). Ils gèrent le routage entre différentes organisations et fournisseurs de services. En revanche, les protocoles de routage intérieur, tels que RIP, OSPF et EIGRP, sont utilisés pour le routage au sein d'un système autonome.

### Temps de vie (TTL)

Le TTL (Time to Live) est un champ dans les paquets IP qui spécifie le nombre maximum de sauts qu'un paquet peut parcourir avant d'être rejeté. Il empêche les paquets de circuler indéfiniment dans le réseau en cas de boucle de routage ou d'autres problèmes. Chaque routeur décrémente la valeur TTL au fur et à mesure que le paquet traverse le réseau.

## Gestion de la bande passante

Une gestion efficace de la bande passante est essentielle pour optimiser les performances du réseau et garantir un flux de trafic fluide. Deux aspects importants de la gestion de la bande passante sont la mise en forme du trafic et la qualité de service (QoS).

### Mise en forme du trafic

La mise en forme du trafic est une technique utilisée pour contrôler le taux de transmission des données sur un réseau. Elle permet aux administrateurs de réseau de modeler le flux de trafic en définissant des limites de bande passante et en donnant la priorité à certains types de trafic. Cela permet d'éviter la congestion du réseau et de s'assurer que les applications critiques bénéficient d'une bande passante suffisante.

### Qualité de service (QoS)

La qualité de service (QoS) désigne la capacité d'un réseau à hiérarchiser et à allouer des ressources à différents types de trafic en fonction de leur importance et de leurs besoins. Les mécanismes de QoS, tels que la priorisation du trafic, l'allocation de la bande passante et la gestion de la congestion, contribuent à garantir des performances optimales pour les applications en temps réel telles que la voix et la vidéo.

{{< inarticle-dark >}}

## Comparaison et placement des dispositifs

Différents dispositifs jouent des rôles spécifiques dans un réseau et présentent des caractéristiques variées qui les rendent adaptés à des tâches particulières. Comparons et opposons certains dispositifs réseau courants et discutons de leur emplacement approprié :

- **Routers** : Les routeurs sont chargés de diriger le trafic entre les différents réseaux. Ils opèrent au niveau de la couche réseau (couche 3) et utilisent des protocoles de routage pour déterminer le meilleur chemin pour la transmission des données.

- Commutateurs** : Les commutateurs fonctionnent au niveau de la couche liaison de données (couche 2) et facilitent la communication entre les appareils au sein d'un réseau local (LAN). Ils utilisent les adresses MAC pour transmettre les paquets de données à leur destinataire.

- Pare-feu** : Les pare-feu protègent les réseaux contre les accès non autorisés et le trafic malveillant. Ils mettent en œuvre des politiques de sécurité en inspectant le trafic réseau et en autorisant ou en bloquant des connexions spécifiques sur la base de règles prédéfinies.

- Équilibreurs de charge** : Les répartiteurs de charge distribuent le trafic réseau entrant sur plusieurs serveurs afin d'optimiser l'utilisation des ressources, d'améliorer les performances et d'assurer une haute disponibilité.

- Points d'accès** : Les points d'accès (AP) fournissent une connectivité sans fil aux appareils au sein d'un réseau. Ils permettent la communication sans fil en transmettant et en recevant des données entre les appareils sans fil et le réseau câblé.

L'emplacement de ces dispositifs dépend de l'architecture et des besoins du réseau. Les **routeurs** sont généralement placés à la périphérie du réseau pour gérer le trafic entre les réseaux. Les **commutateurs** sont déployés au sein des réseaux locaux pour connecter les appareils et faciliter la communication locale. **Les pare-feu sont placés entre les réseaux pour les protéger contre les menaces extérieures. Les **équilibreurs de charge** sont placés devant les serveurs web pour répartir efficacement le trafic. Les **points d'accès** sont placés stratégiquement pour fournir une couverture sans fil dans les zones souhaitées.

______

## Conclusion

La compréhension des **technologies et concepts de routage** est cruciale pour les administrateurs de réseaux et les professionnels de l'informatique. **Les protocoles de routage dynamique** comme **RIP, OSPF, EIGRP et BGP** automatisent le processus d'échange d'informations de routage et s'adaptent aux changements du réseau. **Les protocoles de routage à état de lien, à vecteur de distance et hybrides** offrent différentes approches pour déterminer les itinéraires optimaux. **Le routage statique et les itinéraires par défaut** permettent un contrôle manuel des décisions de routage. **Les techniques de gestion de la bande passante** telles que **la mise en forme du trafic et la qualité de service** garantissent une utilisation efficace du réseau. Comparer et placer les équipements réseau de manière appropriée permet d'améliorer les performances et la sécurité du réseau.

En maîtrisant les **technologies et concepts de routage**, les administrateurs réseau peuvent construire des **réseaux robustes et efficaces** qui répondent aux exigences de la connectivité moderne.

______