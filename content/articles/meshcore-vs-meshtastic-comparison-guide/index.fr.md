---
title: "MeshCore ou Meshtastic : comparaison"
date: 2026-06-26
lastmod: 2026-11-12
toc: true
draft: false
description: "Comparez MeshCore et Meshtastic selon le routage, la portée, le temps d’antenne, l’infrastructure, les appareils pris en charge et les usages adaptés."
genre: ["LoRa", "Réseaux maillés", "Communications hors réseau", "Communications d’urgence", "Communications tactiques", "Radioamateur", "Open source", "Préparation aux catastrophes", "Réseaux sans fil", "Vie privée"]
tags: ["meshcore contre meshtastic", "meshtastic", "meshcore", "réseau maillé lora", "communications hors réseau", "comparaison meshtastic", "comparaison meshcore", "radio lora", "réseaux maillés", "communications d’urgence", "maillage tactique", "radio hors réseau", "protocole meshtastic", "protocole meshcore", "lora meshtastic", "communications en cas de catastrophe", "radio maillée", "stockage et retransmission", "inondation lora", "maillage LoRa", "t-beam meshtastic", "heltec lora", "rak wisblock", "messagerie hors réseau", "protocole de réseau maillé", "meshtastic 2.6", "temps d’antenne lora", "radio de préparation aux urgences"]
cover: "/img/cover/meshcore-vs-meshtastic-comparison-guide.webp"
coverAlt: "Illustration de deux réseaux maillés LoRa : Meshtastic à gauche, avec des nœuds qui diffusent les paquets, et MeshCore à droite, avec un routage structuré, sur fond sombre."
coverCaption: ""
ref: ["/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide"]
---

## Réponse courte

Meshtastic et MeshCore fonctionnent tous deux sur le même matériel LoRa abordable. Ils permettent d’envoyer des messages chiffrés sans réseau cellulaire ni connexion Internet. **Les deux protocoles ne sont pas compatibles.**

**Leur philosophie de routage diffère.** Meshtastic diffuse les paquets à tous les nœuds proches. MeshCore achemine le trafic par une infrastructure planifiée. Ces approches entraînent des performances différentes lorsque le réseau grandit.

*Meshtastic convient à la plupart des utilisateurs.* Son application mobile est aboutie, sa communauté est vaste, sa documentation est solide et sa configuration prend moins de 20 minutes. MeshCore convient mieux aux déploiements planifiés où l’efficacité du temps d’antenne compte davantage que l’auto-organisation spontanée.

**Les principes radiofréquence comptent plus que le micrologiciel.** Aucun des deux protocoles ne compense une antenne mal placée.

______

## Fonctionnement de chaque système

### Meshtastic

**Meshtastic** est un projet open source lancé en 2020 par Kevin Hester. Son micrologiciel transforme du matériel LoRa courant en réseau maillé de messagerie texte, sans dépendre d’Internet ni du réseau cellulaire. Les diffusions utilisent une inondation contrôlée : chaque nœud retransmet les paquets jusqu’à une limite de sauts configurable. Depuis la version 2.6, **les messages directs utilisent le routage par prochain saut** après la découverte d’itinéraire, au lieu d’être inondés, ce qui réduit le temps d’antenne pour les échanges point à point.

Le micrologiciel fonctionne sur du matériel LoRa que beaucoup possèdent déjà ou achètent à bas prix. **LILYGO T-Beam, Heltec WiFi LoRa 32, RAK WisBlock et Seeed SenseCAP Indicator** acceptent Meshtastic sans outil spécialisé. Les applications iOS et Android sont bien entretenues. Un utilisateur non technique peut rejoindre le réseau en moins de dix minutes. L’écosystème comprend des passerelles MQTT, une intégration Home Assistant et des extensions ATAK.

### MeshCore

**MeshCore** a gagné en popularité en 2023 et 2024. Son micrologiciel fonctionne sur une grande partie du même matériel LoRa, mais utilise une **architecture de routage hybride**. Le réseau découvre d’abord les routes. Ensuite, le trafic passe par des répéteurs vers sa destination au lieu d’être diffusé à tout le monde. Ce n’est pas du stockage et retransmission au sens des réseaux tolérants aux délais.

Les répéteurs assurent l’essentiel du transfert. **Les serveurs de salle sont facultatifs.** Ils stockent les messages de groupe afin que les clients les récupèrent à leur reconnexion. Les clients utilisent une radio LoRa compagnon et se connectent à l’infrastructure lorsqu’elle existe, ou communiquent directement avec les nœuds proches en l’absence de répéteur.

______

## Différence technique principale

### Routage de Meshtastic

Les diffusions utilisent une **inondation contrôlée**. Chaque nœud retransmet un paquet jusqu’à la limite de sauts. Aucun nœud n’a besoin de connaître la topologie. Les nouveaux nœuds rejoignent le réseau sans configuration. Le réseau contourne automatiquement les nœuds hors service. Depuis la version 2.6, **les messages directs utilisent le routage par prochain saut** après découverte, ce qui réduit le temps d’antenne du trafic point à point.

**La contrainte réelle est le temps d’antenne, pas le nombre de nœuds.** LoRa utilise des bandes ISM partagées, avec des limites régionales de cycle d’émission, généralement de 1 % en Europe. Un réseau qui envoie souvent des balises GPS, de la télémétrie et du trafic actif sature le temps d’antenne avant d’atteindre une limite absolue de nœuds. Dix nœuds actifs qui envoient fréquemment de la télémétrie créent plus de contention que cinquante capteurs silencieux. Les maillages denses comptant plusieurs dizaines d’utilisateurs actifs connaissent souvent une contention accrue, mais il n’existe pas de plafond fixe. Le seuil dépend du facteur d’étalement, du préréglage de temps d’antenne, des intervalles de télémétrie, du terrain et de l’emplacement des répéteurs.

Meshtastic génère du trafic supplémentaire avec les annonces d’informations des nœuds, la télémétrie de batterie, les paquets GPS et la découverte des voisins. Les versions récentes du micrologiciel ont réduit cette charge. *Régler ces paramètres résout souvent les problèmes de performance avant qu’un changement de protocole soit nécessaire.*

### Routage de MeshCore

MeshCore découvre les routes, les mémorise, puis achemine le trafic vers l’infrastructure au lieu de le rediffuser à tous. **Les répéteurs transfèrent le trafic entre les nœuds.** Les serveurs de salle hébergent éventuellement des conversations de groupe et stockent les messages pour les clients qui se reconnectent plus tard.

L’occupation du canal dépend des conversations actives, pas du nombre total de nœuds. Un grand déploiement comprenant de nombreux nœuds silencieux ne perd pas en performance comme un réseau dense à diffusion généralisée et à forte surcharge. MeshCore vise par conception des déploiements bien plus vastes, même si la qualité réelle dépend du déploiement.

Sans répéteur, les clients communiquent directement lorsqu’ils sont à portée. *L’architecture fonctionne le mieux avec une infrastructure. Cette infrastructure n’est pas obligatoire.*

______

## Matériel

Les deux protocoles fonctionnent sur les mêmes cartes LoRa populaires.

| Carte | Meshtastic | MeshCore |
|---|---|---|
| LILYGO T-Beam (ESP32 + SX1276/SX1262) | Oui | Oui |
| LILYGO T-Echo (nRF52840 + SX1262) | Oui | Oui |
| Heltec WiFi LoRa 32 V3 | Oui | Oui |
| RAK WisBlock 4631 | Oui | Oui |
| Seeed SenseCAP Indicator | Oui | Partiel |
| Station G2 | Oui | Oui |

**Vous pouvez flasher le même appareil physique avec l’un ou l’autre micrologiciel.** Changer de protocole ne nécessite pas de nouveau matériel. L’expérimentation ne coûte que du temps.

______

## Facilité de configuration

### Configurer Meshtastic

1. Téléchargez le micrologiciel depuis meshtastic.org
2. Flashez-le avec l’outil Web flasher.meshtastic.org, sans pilote
3. Installez l’application Meshtastic sur votre téléphone
4. Jumelez l’appareil en Bluetooth
5. Rejoignez ou créez un canal avec un nom et un mot de passe partagés

**Temps total pour une première configuration : moins de 20 minutes.** Le chiffrement des canaux utilise des clés prépartagées AES-256. Le canal public par défaut vous connecte immédiatement à tout nœud Meshtastic à portée. L’application affiche les positions GPS sur une carte lorsque les nœuds ont activé le GPS.

### Configurer MeshCore

1. Flashez votre nœud d’infrastructure, répéteur ou serveur de salle, avec PlatformIO ou un binaire précompilé
2. Flashez la radio compagnon du client
3. Installez l’application MeshCore
4. Configurez l’application avec l’adresse et les identifiants de votre infrastructure
5. Connectez la radio compagnon en Bluetooth

**La configuration demande davantage de planification.** Vous devez comprendre les rôles des nœuds avant le déploiement. Les serveurs de salle sont facultatifs, mais ajoutent la persistance des messages pour les clients hors ligne. *Deux amis qui veulent communiquer rapidement devraient choisir Meshtastic. Une équipe qui déploie une station de base avec un répéteur sur le toit devrait choisir MeshCore.*

______

## Le temps d’antenne est la vraie contrainte

Les deux protocoles fonctionnent sur LoRa. **La capacité LoRa dépend du temps d’antenne et du budget de cycle d’émission, pas du nombre de nœuds.**

Les variables qui déterminent les performances du réseau :

- **Facteur d’étalement.** Une valeur élevée améliore la portée, mais ralentit le débit et réduit la capacité totale.
- **Préréglage de temps d’antenne.** Les préréglages longue portée consomment davantage de cycle d’émission par message.
- **Intervalle de télémétrie.** Le GPS, la batterie et les données environnementales de Meshtastic ajoutent une charge continue.
- **Fréquence des messages.** Les utilisateurs actifs qui envoient souvent affectent davantage les performances que les nœuds passifs.
- **Emplacement des répéteurs.** Un répéteur bien placé répartit la charge. Un répéteur mal placé augmente la congestion.
- **Terrain.** Les nœuds qui ne s’entendent pas ajoutent du trafic sans créer de contention. Ceux qui sont à portée de nombreux autres nœuds en créent.

*Meshtastic réduit la planification et accepte une certaine surcharge de temps d’antenne en échange de l’auto-organisation. MeshCore demande de la planification et récompense cet effort par une meilleure efficacité prévisible. Passer de Meshtastic à MeshCore sans améliorer la planification du réseau ne garantit pas un gain de performance.*

______

## Réglementation

Les comparaisons de performances varient selon les régions, car les réglementations diffèrent :

- **915 MHz (États-Unis) :** pas de plafond fixe de cycle d’émission selon la FCC Part 15, mais des limites de puissance s’appliquent.
- **868 MHz (UE) :** cycle d’émission de 1 % selon l’ETSI, soit 36 secondes d’émission par heure et par canal.
- **433 MHz (UE/Asie) :** limites plus strictes dans de nombreuses régions, souvent 10 % sur certaines sous-bandes.

**La restriction de cycle d’émission de 1 % en Europe est une contrainte réglementaire stricte.** Les maillages Meshtastic denses dans l’UE atteignent les limites plus vite que des déploiements équivalents aux États-Unis. L’usage plus efficace du temps d’antenne par MeshCore apporte un avantage proportionnellement plus important dans les régions soumises à ces limites.

______

## Vie privée et sécurité

### Meshtastic

Meshtastic chiffre le trafic des canaux privés avec des **clés prépartagées AES-256**. Tous les messages d’un canal partagent la même clé. Toute personne qui détient cette clé lit tous les messages, y compris les positions GPS. **Le canal public par défaut utilise une clé connue, distribuée avec le micrologiciel.** Il ne protège donc pas la confidentialité du trafic contre les personnes qui exécutent Meshtastic à proximité.

Les positions GPS sur un canal privé chiffré ne sont visibles que par les nœuds qui détiennent la clé. Sur le canal public, elles sont visibles par tous. *Cela compte lorsque le suivi a des conséquences opérationnelles.*

Meshtastic 2.6 a amélioré le routage des messages directs. Le trafic de groupe utilise toujours une clé de canal prépartagée. Les messages directs offrent une meilleure isolation, mais ne sont pas chiffrés de bout en bout au sens du protocole Signal.

### MeshCore

Le routage hybride de MeshCore signifie qu’**un observateur passif ne peut pas reconstituer toute la topologie du réseau** en l’écoutant. Le trafic est acheminé vers une infrastructure précise au lieu d’être diffusé à tous. **Les messages directs utilisent un chiffrement par contact**, plutôt qu’une clé de canal partagée. Les autres nœuds de la même infrastructure ne peuvent pas déchiffrer votre conversation directe, même s’ils utilisent le même répéteur.

Les nœuds d’infrastructure relaient le trafic chiffré. Pour les messages directs chiffrés par contact, le répéteur transfère le texte chiffré sans le déchiffrer. Pour les conversations de salle, les serveurs de salle voient le contenu des salles qu’ils hébergent. *La question pertinente est de savoir si vous contrôlez le serveur de salle.*

MeshCore n’offre pas le chiffrement de bout en bout strict du protocole Signal. **Le chiffrement par contact des messages directs améliore nettement la protection par rapport à une clé de canal partagée.** Les usages opérationnels à forts enjeux doivent examiner les détails de l’implémentation.

______

## Consommation électrique

Avec les paramètres par défaut, MeshCore génère moins de transmissions radio supplémentaires que Meshtastic. **Moins d’émissions signifie une meilleure autonomie des nœuds clients.** Les paquets de télémétrie, les diffusions GPS et l’inondation contrôlée de Meshtastic consomment du temps d’émission. Vous réduisez fortement cette charge en réglant les intervalles de télémétrie et en désactivant la diffusion GPS sur les nœuds sans GPS. À paramètres par défaut comparables, **MeshCore émet moins**.

Un déploiement Meshtastic bien réglé, avec une télémétrie minimale, offre une autonomie proche de MeshCore. Les paramètres par défaut favorisent MeshCore pour l’autonomie.

______

## Résilience du réseau

**L’inondation contrôlée de Meshtastic résiste bien aux pannes.** La perte d’un relais a souvent peu d’effet opérationnel, car les autres nœuds réacheminent naturellement le trafic. Il n’est pas nécessaire de connaître les nœuds disponibles à l’avance. Le maillage se rétablit de lui-même.

**MeshCore dépend davantage de l’emplacement des répéteurs.** Un réseau MeshCore bien conçu, avec une bonne couverture de répéteurs, offre des performances prévisibles. Si le seul répéteur d’une zone de couverture tombe en panne, les nœuds qui en dépendent perdent leur connectivité. *MeshCore récompense la planification préalable. Meshtastic tolère mieux les pannes de nœuds.*

Meshtastic accepte une surcharge de temps d’antenne en échange de la résilience. MeshCore accepte une dépendance à l’infrastructure en échange de l’efficacité.

______

## GPS et suivi des positions

**L’écosystème GPS de Meshtastic est plus développé.** L’application mobile comprend une carte. Des nœuds communautaires alimentent des cartes publiques de suivi comme meshmap.net via des passerelles MQTT. La télémétrie de position est une fonction centrale. Le partage de position pour les randonnées, la coordination des secours et le suivi d’événements est bien développé.

MeshCore ne se concentre pas sur le suivi des positions. *Si la visibilité GPS est une exigence principale, l’écosystème Meshtastic est plus développé et plus mature en 2026.*

______

## Écosystème et communauté

La communauté Meshtastic est **plus vaste** :

- Discord actif avec des milliers de membres
- Subreddit actif à r/meshtastic
- Documentation complète sur meshtastic.org
- Intégrations tierces : MQTT, Home Assistant, Node-RED, ATAK et bibliothèques Python
- Versions régulières du micrologiciel
- Grand nombre de guides matériels créés par la communauté

MeshCore grandit, mais sa communauté reste plus petite. *Il existe moins de discussions, de tutoriels et d’intégrations tierces. En cas de panne, vous chercherez des réponses dans le code source du micrologiciel ou sur le Discord du projet plutôt que dans des solutions existantes.*

Les deux projets sont open source, mais leurs licences diffèrent. **Meshtastic utilise une licence de type BSD. MeshCore utilise la GPL.** Certaines organisations en tiennent compte pour le déploiement et la distribution.

______

## Quand Meshtastic est le meilleur choix

**Petits groupes informels.** Un club de randonnée qui veut échanger des messages hors réseau et partager les positions devrait choisir Meshtastic. La configuration est simple, la carte fonctionne bien et le réseau s’organise seul.

**Déploiements mobiles.** Meshtastic convient aux utilisateurs qui traversent un terrain et rejoignent ou quittent le réseau de façon imprévisible grâce à son inondation auto-organisée. L’infrastructure n’a pas besoin d’être planifiée pour les nœuds mobiles.

**Déploiements destinés au grand public.** Les personnes sans connaissances techniques peuvent configurer leur appareil sans aide. La prise en main de Meshtastic est accessible.

**Déploiement rapide pour un événement.** Communications lors d’un festival, coordination d’une course ou secours déployés aujourd’hui et démontés la semaine suivante. La configuration rapide et l’absence de dépendance à une infrastructure rendent Meshtastic pratique.

**Suivi GPS.** En 2026, Meshtastic est le bon choix si la visibilité de position constitue l’usage principal.

______

## Quand MeshCore est le meilleur choix

**Déploiements avec infrastructure planifiée.** Vous disposez d’un répéteur sur un toit ou d’un serveur de salle alimenté de façon fiable. Le routage hybride de MeshCore tire parti de cette infrastructure fixe.

**Grands réseaux avec infrastructure dédiée.** Choisissez-le lorsque l’efficacité du temps d’antenne et des performances prévisibles à grande échelle comptent davantage que l’auto-organisation spontanée.

**Persistance des messages en cas de connectivité intermittente.** Les serveurs de salle stockent les messages et les transmettent quand les clients se reconnectent. **C’est l’un des avantages pratiques les plus concrets de MeshCore sur Meshtastic.**

**Séparation des nœuds fixes et mobiles.** Certains nœuds servent d’infrastructure et d’autres de clients. Le modèle de rôles de MeshCore est conçu pour cette séparation.

**Régions soumises à des limites de cycle d’émission.** Les déploiements européens soumis à la limite ETSI de 1 % profitent davantage de l’usage efficace du temps d’antenne par MeshCore.

**Chiffrement par contact.** Pour chiffrer les messages directs, le modèle MeshCore est nettement supérieur à l’approche de Meshtastic fondée sur une clé de canal partagée.

______

## Limites de chaque système

### Faiblesses de Meshtastic

- **Contention du temps d’antenne à grande échelle.** Les maillages denses avec des paramètres très bavards, des diffusions GPS fréquentes et des canaux actifs se dégradent. Commencez par corriger la configuration avant de changer de protocole.
- **Pas de persistance des messages sans infrastructure.** Sans passerelle MQTT, les messages manqués sont perdus.
- **Confidentialité de position sur le canal public.** Tout auditeur voit toutes les diffusions GPS. C’est acceptable pour un usage occasionnel, mais inadapté aux exigences de sécurité opérationnelle.
- Les versions majeures du micrologiciel entraînent parfois des incompatibilités jusqu’à ce que le réseau passe à une version cohérente.

### Faiblesses de MeshCore

- **Configuration complexe.** Vous devez comprendre les rôles d’infrastructure avant de déployer efficacement.
- **Communauté plus petite.** La documentation, les tutoriels et les intégrations tierces de Meshtastic sont plus développés.
- **Moins de choix de matériel.** MeshCore prend en charge une liste plus réduite de matériel.
- **Applications mobiles moins abouties.** Elles sont fonctionnelles, mais moins soignées que les applications iOS et Android de Meshtastic.
- **Dépendance à l’infrastructure pour des performances optimales.** Sans répéteurs, les clients communiquent directement, mais l’efficacité du routage disparaît. Si votre groupe ne s’engage pas à maintenir une infrastructure fixe, l’avantage architectural ne se concrétise pas.
- **Rétablissement du réseau.** La perte d’un répéteur dans une zone de couverture coupe la connexion des nœuds qui en dépendent. L’inondation de Meshtastic tolère mieux les pannes de nœuds.
- **Aucune interopérabilité entre protocoles.** MeshCore et Meshtastic n’échangent pas de messages. Le même matériel accepte l’un ou l’autre micrologiciel, mais faire fonctionner les deux crée deux réseaux distincts.

______

## La radiofréquence compte plus que le micrologiciel

**La qualité et la hauteur de l’antenne, les pertes de la ligne d’alimentation, le terrain et les réglages radio influent davantage sur les performances que le choix du micrologiciel.**

Un nœud Meshtastic bien placé sur une colline, avec une bonne antenne, dépasse un répéteur MeshCore mal placé dans un boîtier métallique au sous-sol. La comparaison des protocoles suppose une qualité de déploiement physique à peu près équivalente.

Avant de changer de protocole pour résoudre un problème de performance, vérifiez les points suivants :

- Les connexions d’antenne sont propres et entraînent peu de pertes.
- Les nœuds sont aussi hauts que possible.
- Le préréglage de temps d’antenne correspond à vos besoins de portée.
- **Les intervalles de télémétrie ne saturent pas le canal.**
- Le facteur d’étalement correspond à la densité de nœuds.

______

## Résumé comparatif

| Critère | Meshtastic | MeshCore |
|---|---|---|
| Modèle de réseau | Inondation contrôlée et routage par prochain saut des messages directs | Découverte de routes hybride et transfert dirigé |
| Difficulté de configuration | Facile | Moyenne à élevée |
| Conception pour l’échelle | Flexible, se dégrade avec la contention du temps d’antenne | Conçu pour des réseaux planifiés plus vastes |
| Qualité de l’application mobile | Excellente | Fonctionnelle |
| Taille de la communauté | Très grande | En croissance |
| Suivi GPS et de position | Écosystème développé | Peu d’accent |
| Persistance des messages | Non, nécessite une passerelle MQTT | Oui, via des serveurs de salle facultatifs |
| Chiffrement des messages directs | Clé prépartagée de canal | Chiffrement par contact |
| Besoin d’infrastructure | Aucune exigence | Optimisé pour les nœuds d’infrastructure |
| Rétablissement du réseau | Résilient et auto-réparateur | Dépend de l’emplacement des répéteurs |
| Matériel pris en charge | Large choix | Sous-ensemble ciblé |
| Idéal pour | Groupes mobiles, spontanés et petits | Déploiements planifiés à infrastructure fixe |

______

## Lequel choisir

**Commencez par Meshtastic.** Vous serez opérationnel en une après-midi. Vous trouverez des personnes avec qui tester. L’application fonctionne et la documentation est excellente. Le routage par prochain saut de Meshtastic 2.6 pour les messages directs réduit l’écart d’efficacité du trafic point à point.

**Passez à MeshCore lorsque les paramètres par défaut de Meshtastic ne répondent pas aux besoins de votre déploiement.** Si vous disposez de répéteurs dédiés, avez besoin de conserver les messages pour les utilisateurs intermittents ou construisez un grand réseau planifié où l’efficacité du temps d’antenne prime sur l’auto-organisation, l’architecture de MeshCore convient et justifie l’effort de configuration.

Avant de changer de protocole, **réglez votre déploiement Meshtastic**. Réduisez les intervalles de télémétrie. Désactivez la diffusion GPS sur les nœuds sans GPS. Ajustez le préréglage de temps d’antenne à la densité du réseau. *Les problèmes de performance de nombreux réseaux viennent de la configuration, pas du protocole.*

Les deux protocoles répondent à des besoins différents sur l’axe planification et spontanéité. Meshtastic réduit la planification et accepte la surcharge d’antenne liée à l’auto-organisation. MeshCore exige une planification et la récompense par des performances plus prévisibles. **Aucun ne remplacera l’autre, car leurs usages diffèrent.**

*Vous construisez un réseau qui doit relier LoRa à la radio par paquets, au Wi-Fi ou à Internet, au lieu de rester sur un seul maillage LoRa ?* Consultez le **[guide comparatif Meshtastic, MeshCore et Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)** pour comprendre où s’intègrent les réseaux indépendants du transport et où ils ajoutent une complexité inutile.
