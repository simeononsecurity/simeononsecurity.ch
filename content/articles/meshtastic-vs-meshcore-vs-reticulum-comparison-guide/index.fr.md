---
title: "Meshtastic vs MeshCore vs Reticulum"
date: 2026-09-01
lastmod: 2026-11-12
toc: true
draft: false
description: "Comparez Meshtastic, MeshCore et Reticulum selon le routage, le temps d’émission, l’infrastructure, le transport et les usages hors réseau."
genre: ["LoRa", "Réseaux maillés", "Communications hors réseau", "Communications d’urgence", "Radioamateur", "Open source", "Préparation aux catastrophes", "Réseaux sans fil", "Vie privée", "Réseaux"]
tags: ["meshtastic vs meshcore vs reticulum", "réseau reticulum", "meshtastic", "meshcore", "reticulum", "lxmf", "réseau maillé LoRa", "communications hors réseau", "rnode", "radio par paquets", "réseau indépendant du transport", "réseaux maillés", "communications d’urgence", "réseau maillé communautaire", "temps d’émission LoRa", "inondation contrôlée", "limite de sauts", "nœud répéteur", "serveur de salon", "application Sideband", "nomadnet", "meshchat", "communications en cas de catastrophe", "radio hors réseau", "protocole de réseau maillé", "réseau maillé régional", "ingénierie RF"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Illustration comparant trois systèmes de réseau maillé avec des nœuds, des antennes et des lignes de connexion sur fond sombre et coloré, représentant leurs fonctionnalités distinctes."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## En bref

**Ces trois projets ne répondent pas au même besoin.** Meshtastic et MeshCore sont des systèmes de réseau maillé LoRa qui suivent des philosophies de routage différentes. Reticulum est plus large. Cette couche réseau indépendante du transport fonctionne simultanément sur LoRa, la radio par paquets, le Wi-Fi, Ethernet, les liaisons série et Internet.

**La bonne question n’est pas « lequel est le meilleur ? »** C’est « quelle architecture convient au réseau que je veux construire ? »

*Meshtastic convient aux réseaux ad hoc et aux utilisateurs itinérants.* **MeshCore convient à une infrastructure fixe, déployée délibérément.** **Reticulum convient aux réseaux qui doivent relier différents moyens de transport ou réunir des réseaux autrement séparés.** La plupart des personnes qui construisent un seul réseau LoRa régional n’ont besoin que de l’une des deux premières options.

______

## Définissez le réseau à construire

Avant de comparer les protocoles, notez les besoins du réseau. Voici une cible utile pour la plupart des déploiements communautaires et de communications d’urgence :

- **Fonctionnement sans licence**, pour que chacun puisse participer sans licence radioamateur
- **Matériel abordable**, qu’une communauté peut déployer à grande échelle
- **Faible consommation**, avec idéalement une alimentation solaire ou par batterie
- **Communications longue portée** sans dépendre du réseau mobile ni d’Internet
- **Indépendance vis-à-vis des infrastructures**, du réseau électrique, des FAI et des opérateurs
- **Configuration et utilisation assez simples pour les non-spécialistes radio**
- **Adapté à un déploiement communautaire**, et pas seulement au sous-sol d’un opérateur
- **Capable de dépasser quelques nœuds** sans s’effondrer
- **Utile en cas de panne des infrastructures**, quand les antennes mobiles et Internet ne fonctionnent plus
- **Livraison fiable des messages plutôt que portée record**

Gardez cette liste à l’esprit pendant la suite de l’article. Nous évaluerons chaque compromis d’architecture selon ces critères.

______

## Meshtastic

**Meshtastic** est l’option la plus mature et la plus répandue. Elle répond bien aux besoins de la plupart des utilisateurs.

- **Écosystème mature** et développé depuis plusieurs années
- **Grande communauté**, Discord actif et documentation complète
- **Large compatibilité matérielle** avec les cartes LILYGO, Heltec, RAK et Seeed
- **Bonnes applications mobiles** pour iOS et Android
- **Prise en main facile**, la première configuration prend moins de 20 minutes
- **Bonne prise en charge des utilisateurs portables et itinérants** qui rejoignent et quittent le réseau de manière imprévisible
- **Fonctions GPS et télémétrie** avec un écosystème développé autour d’elles
- **Déploiements existants** dans la plupart des zones métropolitaines, ce qui facilite l’adoption puisqu’on rejoint un réseau au lieu d’en construire un de zéro

Pour une analyse détaillée du routage, de la compatibilité matérielle et de la configuration de Meshtastic par rapport à MeshCore, consultez le **[guide comparatif MeshCore vs Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)**. Cet article se concentre sur la question d’architecture la plus importante pour les grands déploiements : **l’inondation contrôlée et les limites de sauts**.

### L’inondation contrôlée et l’importance des sauts

Meshtastic diffuse ses messages par **inondation contrôlée**. Lorsqu’un nœud envoie un message, tous les nœuds qui le reçoivent rediffusent le paquet, jusqu’à la limite de sauts configurée. Aucun nœud n’a besoin de connaître la topologie du réseau. Les nouveaux nœuds rejoignent le réseau sans configuration, et les nœuds hors service sont contournés automatiquement puisque l’inondation emprunte d’autres chemins.

La limite de sauts par défaut est **3**. Le maximum est **7**. Évitez de dire « Meshtastic ne dépasse pas sept sauts ». *La vraie question est le coût d’une augmentation de cette valeur.*

Chaque saut supplémentaire fait rediffuser le message par tous les nœuds à portée. La multiplication des retransmissions entraîne :

- **Plus de temps d’émission** consommé par message
- **Plus de transmissions en double**, car chaque nœud à portée répète les retransmissions
- **Plus de contention** pour le canal partagé
- **Plus de risques de collision** quand davantage de radios transmettent dans la même fenêtre
- **Plus de consommation de batterie** pour chaque nœud qui reçoit et retransmet
- **Moins de capacité disponible sur le canal** pour les vrais messages

La capacité LoRa dépend du temps d’émission et des limites régionales du cycle d’utilisation, pas du nombre de nœuds. Un réseau de dix nœuds bavards qui diffusent souvent leur position GPS et leur télémétrie peut saturer un canal que cinquante capteurs discrets n’utiliseraient presque jamais. C’est pourquoi un réseau maillé dense avec une limite de sauts élevée se dégrade plus vite que le même nombre de nœuds avec une limite plus basse et des intervalles de télémétrie maîtrisés. **Meshtastic 2.6 a amélioré ce point pour les messages directs** en passant au routage par prochain saut après la découverte de la route. Le trafic point à point n’inonde donc plus toute la zone de sauts. Les diffusions continuent de l’inonder.

Pour un réseau de petite ou moyenne taille, comme celui d’un club de randonnée, c’est rarement un problème. Pour un **réseau régional conçu pour couvrir une ville ou plusieurs communes**, c’est la principale contrainte de conception.

______

## MeshCore

**MeshCore fait un autre pari architectural :** au lieu de traiter chaque appareil comme un participant équivalent à la propagation des messages, il construit une couche d’infrastructure délibérée et dirige le trafic vers elle.

### Rôles des nœuds

Les déploiements MeshCore reposent sur des rôles distincts, et non sur un ensemble plat de nœuds équivalents :

- **Nœuds compagnons ou clients** équipés d’une radio LoRa reliée à un téléphone ou un ordinateur portable. Ils passent par l’infrastructure proche lorsqu’elle existe
- **Répéteurs** chargés de transférer le trafic entre les clients et les autres éléments d’infrastructure. Ils font l’essentiel du travail de routage
- **Serveurs de salon** (facultatifs) qui hébergent les conversations de groupe et remettent aux clients les messages stockés lorsqu’ils se reconnectent

La découverte de route a lieu en premier. Le trafic suit ensuite le chemin découvert jusqu’à sa destination, au lieu de se propager à tous les nœuds à portée. L’occupation du canal évolue en fonction des conversations actives, pas du nombre total de nœuds. Sa croissance diffère donc nettement de celle du modèle d’inondation de Meshtastic.

### Pourquoi ce modèle convient à une infrastructure fixe

*C’est l’argument principal en faveur de MeshCore.* Le modèle d’inondation de Meshtastic présente de vrais avantages pour les réseaux ad hoc et itinérants : aucune planification, aucune infrastructure à maintenir, et une bonne adaptation aux entrées et sorties de nœuds. Le routage de MeshCore prend l’avantage lorsque **les utilisateurs déploient volontairement une infrastructure**.

Un réseau organisé autour de répéteurs connus et placés en hauteur permet de concevoir précisément la couverture. Il ne dépend pas des nœuds qui se trouvent à portée les uns des autres un jour donné. Cette différence compte pour :

- **Les nœuds permanents sur les toits** avec une alimentation fiable
- **Les tours** et les infrastructures de communication existantes
- **Les répéteurs solaires** sur des sites sans surveillance
- **Les sites relais en montagne ou en hauteur**
- **Les infrastructures communautaires** partagées par plusieurs groupes
- **Les réseaux régionaux** qui couvrent plus d’un quartier
- **Les communications d’urgence** où la couverture prévisible prime sur la flexibilité

Revenez aux principes fondamentaux de la RF : **des liaisons fiables entre des infrastructures bien placées comptent plus que la maximisation du gain d’antenne, de la puissance d’émission ou de la portée théorique.** Un protocole organisé autour de répéteurs dédiés récompense le travail d’ingénierie RF nécessaire pour bien les placer. Un protocole fondé sur l’inondation en tire moins parti, puisque tous les nœuds remplissent à peu près le même rôle, quel que soit leur emplacement.

______

## L’argument des nœuds itinérants et son coût

Une suggestion courante ressemble à ceci : *« Meshtastic est meilleur pour les nœuds itinérants, MeshCore pour les nœuds fixes. Utilisons donc Meshtastic pour les utilisateurs et MeshCore comme réseau dorsal. »*

Sur le papier, l’idée semble séduisante. En pratique, mélanger les deux ne combine pas automatiquement leurs avantages, car **Meshtastic et MeshCore utilisent des architectures réseau et de routage différentes, et n’échangent pas de messages.** Les relier ajoute une couche de traduction entre deux systèmes incompatibles. On ne se contente pas de choisir le meilleur de chacun.

Une fois les deux systèmes reliés, vous gérez :

- **Deux réseaux distincts**, chacun avec sa propre topologie et son propre comportement
- **Deux modèles de routage** qui ne partagent aucun état
- **Une couche de traduction** qui exige du développement et une maintenance continue
- **Plus d’infrastructure** pour héberger la passerelle
- **Plus de configuration** entre deux écosystèmes de micrologiciels au lieu d’un seul
- **Plus de points de défaillance**, puisque la passerelle peut tomber indépendamment de chaque réseau maillé
- **Des diagnostics plus difficiles**, car un échec de livraison peut provenir de l’un des réseaux ou de leur passerelle

Avant d’adopter cette architecture, posez-vous directement la question : **la complexité ajoutée résout-elle un problème qu’un seul protocole bien réglé ne résout pas ?** Souvent, un déploiement MeshCore bien configuré avec quelques nœuds compagnons adaptés aux utilisateurs mobiles, ou un déploiement Meshtastic avec quelques relais bien placés et une limite de sauts élevée, apporte l’essentiel des avantages sans faire fonctionner deux réseaux reliés artificiellement.

______

## Reticulum

Reticulum mérite sa propre catégorie, plutôt qu’une place de « troisième option de réseau maillé LoRa », car ce n’est pas principalement un protocole de réseau maillé LoRa. **Sa caractéristique principale est l’indépendance du transport.**

Reticulum est une pile réseau fondée sur la cryptographie. Elle n’utilise pas d’adresses source : les paquets ne contiennent donc aucune information sur leur origine. Chaque adresse est souveraine. Une fois générée, elle devient joignable dans le monde entier en quelques secondes ou minutes et le reste même si l’appareil change de région du réseau. Toutes les communications sont chiffrées par défaut avec des clés éphémères et une confidentialité persistante. Reticulum supprime les paquets non chiffrés au lieu de les livrer. Aucun pilote du noyau n’est nécessaire. Reticulum fonctionne en espace utilisateur sur tout système exécutant Python 3, y compris un Raspberry Pi Zero.

Reticulum prend en charge les interfaces suivantes :

- **LoRa**, avec du matériel compatible RNode (une conception définie et ouverte d’émetteur-récepteur LoRa, constructible, installable sur des cartes courantes ou disponible prêt à l’emploi)
- **Radio par paquets**, avec tout TNC fonctionnant en mode KISS, adapté à la radioamateur VHF et UHF
- **Wi-Fi et Ethernet filaire**, avec découverte automatique des pairs sans routeur ni serveur DHCP
- **Liaisons série**, pour des connexions directes entre appareils
- **TCP et UDP sur les réseaux IP existants**, y compris Internet
- **Le réseau I2P**, ainsi que des interfaces personnalisées pour toute autre technologie reliée par un pont Python

Reticulum héberge des applications comme **LXMF** (un protocole de messagerie tolérant les retards) et des outils destinés aux utilisateurs comme **Sideband**, **NomadNet** et les clients communautaires **MeshChat**. Ils ajoutent aux réseaux Reticulum une couche de messagerie et de navigation comparable à celle que Meshtastic et MeshCore fournissent d’origine.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Schéma montrant Reticulum reliant un réseau maillé LoRa, un réseau radio par paquets et une liaison Internet en un seul réseau chiffré adressable" >}}

### Quand Reticulum est adapté

Reticulum révèle sa valeur dans une configuration hétérogène, par exemple :

**Réseau maillé LoRa → nœud Reticulum → liaison IP → nœud Reticulum → réseau radio**

Reticulum réalise ici une fonction que ni Meshtastic ni MeshCore ne fournissent : réunir deux systèmes de communication distincts dans un seul réseau adressable. Il s’agit d’un besoin concret, pas d’une amélioration générique. Reticulum convient notamment pour :

- **Relier des réseaux géographiquement éloignés** sans liaison radio directe entre eux
- **Faire communiquer différents moyens de transport physiques**, comme un réseau maillé LoRa d’un côté et un réseau radio par paquets de l’autre
- **Des passerelles radio-IP** qui transfèrent le trafic entre un réseau radio de terrain et Internet
- **Des réseaux expérimentaux et de recherche**, où la possibilité de mélanger les transports compte plus que la simplicité du déploiement
- **Des réseaux où aucun moyen de transport ne répond à tous les besoins**, et où il faut relier les différents éléments

### Quand Reticulum ajoute une complexité inutile

Si tout le monde utilise du matériel LoRa compatible et que l’objectif réel est **un seul réseau maillé LoRa régional**, ajouter Reticulum apporte peu d’avantages et a un coût réel. Chaque couche supplémentaire de la pile réseau entraîne davantage de :

- **Configuration** à régler correctement et à garder cohérente sur tous les nœuds
- **Logiciels** à installer, mettre à jour et dépanner
- **Matériel** dans certaines configurations, selon la façon dont les interfaces sont reliées
- **Points de diagnostic** lorsqu’un message n’est pas livré
- **Connaissances nécessaires** pour que les opérateurs comprennent un troisième modèle réseau

*Utilisez Reticulum lorsque l’indépendance du transport répond à un besoin réel, pas simplement parce qu’il prend en charge plus d’interfaces que l’alternative.* Un problème de limite de sauts dans un réseau maillé LoRa relève du réglage de Meshtastic ou MeshCore. Ce n’est pas un problème d’indépendance du transport, et Reticulum ne le transforme pas en tel problème.

______

## Construisez un réseau maillé sain avant d’en fragmenter trois

Si un protocole répond déjà à vos besoins, **construisez un réseau unique et sain** au lieu de créer plusieurs petits réseaux reliés par des passerelles. Ce principe, « un réseau d’abord », doit guider la plupart des décisions précédentes.

Pour un réseau communautaire, **l’interopérabilité entre les personnes qui l’utilisent déjà compte souvent plus que la flexibilité de l’architecture.** Un grand réseau fonctionnel fondé sur un seul protocole a plus de valeur pratique que trois réseaux intéressants sur le plan technique, mais fragmentés et seulement partiellement interconnectés.

### Les réseaux Meshtastic existants comptent

**Ne rejetez pas Meshtastic simplement parce que MeshCore présente des avantages architecturaux pour une infrastructure fixe.** Si une ville compte déjà des dizaines ou des centaines de nœuds Meshtastic, cette base installée constitue une véritable infrastructure et une véritable communauté. La migration a un coût qu’une comparaison de fiches techniques ne prend pas en compte :

- **Le matériel installé** à reflasher ou à remplacer
- **Les utilisateurs existants** qui savent déjà utiliser le réseau
- **Les connaissances communautaires** accumulées autour du déploiement actuel
- **Les répéteurs déjà installés** et placés, parfois grâce à un accès difficilement obtenu à un toit ou une tour
- **L’expérience de configuration** acquise par les personnes qui exploitent le réseau
- **Les canaux établis** que les membres surveillent déjà
- **La formation nécessaire** pour les personnes qui doivent apprendre un deuxième système

Le choix du protocole est **à la fois un problème d’ingénierie et un problème d’adoption par la communauté.** La meilleure architecture sur le papier ne gagne pas automatiquement si elle demande à une communauté active de tout recommencer.

______

## Le défi des réseaux régionaux

Considérez un déploiement hypothétique dans plusieurs villes :

**Ville A, répéteur, répéteur, relais rural, répéteur, Ville B, répéteur, Ville C**

Demandez-vous comment chaque architecture gère cette chaîne lorsque le réseau grandit. Un réseau maillé par inondation avec une limite de sept sauts a du mal à couvrir une telle distance de façon fiable, car chaque saut augmente le temps d’émission et chaque nœud actif supplémentaire ajoute de la contention. Une architecture structurée autour de répéteurs, comme MeshCore, est conçue pour ce type de déploiement : des relais connus, un placement délibéré et un routage qui évolue avec les conversations actives plutôt qu’avec le nombre total de nœuds.

C’est dans ce scénario que **les limites de sauts, le budget de temps d’émission, le comportement du routage et la conception de l’infrastructure cessent d’être théoriques** et déterminent le fonctionnement de bout en bout du réseau. À l’échelle géographique, les différences d’architecture entre Meshtastic et MeshCore ne sont plus académiques.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Schéma d’un réseau maillé régional reliant trois villes par une chaîne de répéteurs et un relais rural, illustrant l’accumulation du temps d’émission et des sauts avec la distance" >}}

______

## La RF compte plus que le protocole

**Aucun logiciel de routage ingénieux ne crée une liaison RF là où il n’en existe pas physiquement.** Avant d’accuser un protocole d’un problème de couverture, vérifiez les fondamentaux :

- **Hauteur de l’antenne** par rapport aux obstacles
- **Visibilité directe** entre les deux extrémités de la liaison
- **Dégagement de la zone de Fresnel**, qui diffère de la visibilité à l’œil nu
- **Pertes dans la ligne d’alimentation**, dues à un câble coaxial bon marché ou trop long
- **Qualité de l’antenne** et adéquation à la bande utilisée
- **Niveau de bruit** sur le site de réception
- **Relief** entre les nœuds
- **Position des nœuds**, et marge de progression réaliste
- **Marge de liaison**, l’écart entre le signal reçu et le niveau minimal requis pour le décoder

*Une antenne de 2 dBi bien placée sur un bon mât dépasse souvent une antenne à gain élevé mal placée derrière la fenêtre d’un sous-sol.* Le choix du protocole détermine comment le réseau gère les liaisons disponibles. Il ne crée pas de liaison lorsque les lois physiques l’empêchent.

### La fiabilité plutôt que la portée maximale

**Ne concevez pas un réseau autour de la portée maximale qu’une liaison atteint occasionnellement.** Concevez-le pour que les liaisons fonctionnent régulièrement.

Pour un réseau communautaire ou de communications d’urgence, **une livraison prévisible à 15 miles a plus de valeur pratique qu’une liaison qui atteint parfois 40 miles et échoue le reste du temps.** Créez une couverture qui se chevauche avec une infrastructure fiable plutôt que de rechercher des liaisons record. Ce principe s’applique quel que soit le protocole utilisé.

______

## Lequel choisir ?

**Meshtastic convient** si vous privilégiez la maturité de l’écosystème, la facilité d’adoption, les utilisateurs portables et itinérants et la compatibilité avec une communauté Meshtastic existante. C’est le choix par défaut pour la plupart des personnes qui partent de zéro.

**MeshCore devient intéressant** si vous construisez délibérément une infrastructure LoRa permanente et voulez que des répéteurs dédiés forment un réseau structuré plus étendu. Il récompense davantage la planification et le bon placement des répéteurs qu’une architecture fondée sur l’inondation.

**Reticulum convient** lorsque le besoin dépasse un seul réseau maillé LoRa et qu’il faut connecter plusieurs transports ou réseaux autrement séparés dans un système adressable unique.

Pour une **infrastructure communautaire sans licence, longue portée, basse consommation et principalement basée sur des répéteurs fixes**, privilégiez MeshCore. *Si un réseau Meshtastic sain existe déjà dans votre région, il faut des avantages suffisants pour justifier de fragmenter la communauté existante avant de le remplacer.* Reticulum devient pertinent lorsqu’un seul protocole maillé ou un seul transport physique ne répond plus au besoin, pas simplement parce qu’il sait faire plus de choses.

______

## Références

1. [Algorithme de diffusion maillée Meshtastic](https://meshtastic.org/docs/overview/mesh-algo/)
2. [Configuration LoRa de Meshtastic (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Site officiel de MeshCore](https://meshcore.co.uk/)
4. [Pile réseau Reticulum](https://reticulum.network/)
5. [Qu’est-ce que Reticulum ?](https://reticulum.network/manual/whatis.html)
6. [Configuration des interfaces Reticulum](https://reticulum.network/manual/interfaces.html)
7. [Guide comparatif MeshCore vs Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)
