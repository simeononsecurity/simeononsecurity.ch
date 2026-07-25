---
title: "La cybersécurité OT, ICS et API est un problème que l'industrie ne peut pas honnêtement résoudre"
draft: false
toc: true
date: 2026-06-26
description: "Une opinion professionnelle sur pourquoi les orientations en cybersécurité OT, ICS et API ne peuvent pas suivre le problème réel. Ces systèmes n'ont jamais été conçus pour être sécurisés. La conformité aux normes écrites n'est pas la même chose que la sécurité."
tags: ["sécurité OT", "sécurité ICS", "sécurité API", "sécurité IoT", "cybersécurité industrielle", "sécurité SCADA", "NIST 800-82", "IEC 62443", "NERC CIP", "technologie opérationnelle", "infrastructure critique", "capteurs analogiques", "air gap", "systèmes hérités", "opinion cybersécurité", "systèmes de contrôle industriel", "SCADA", "Stuxnet", "sécurité des systèmes de contrôle", "sécurité cyber-physique", "sécurité de la chaîne d'approvisionnement", "chaîne d'approvisionnement OT"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Une illustration montrant un contraste entre un ancien automate programmable (API) avec des fonctionnalités analogiques d'un côté et un contrôleur moderne capable de cybersécurité avec des interfaces numériques de l'autre, sur fond sombre."
coverCaption: ""
---

J'ai passé assez de temps dans des environnements industriels pour dire clairement ceci : **la plupart des programmes de cybersécurité OT, ICS et API sont du théâtre**. Ils produisent des documentations de conformité. Ils ne produisent pas de sécurité. L'écart entre les deux est l'endroit où les infrastructures critiques se font toucher.

Ce n'est pas une attaque contre les personnes qui écrivent les normes. **NIST SP 800-82 Rev 3**, **IEC 62443** et **NERC CIP** sont des documents techniquement solides. Le problème n'est pas les orientations. *Le problème est ce à quoi les orientations sont appliquées.*

## Les systèmes ont été construits pour fonctionner, pas pour être sécurisés

**Les API, les systèmes SCADA, les systèmes de contrôle distribués (DCS) et les équipements IoT industriels hérités** ont été conçus pour une seule chose : fonctionner de manière fiable pendant très longtemps. **La disponibilité était le seul objectif de conception qui valait la peine d'être discuté.** La confidentialité, l'intégrité, l'authentification et la journalisation n'étaient pas des exigences. Dans de nombreux cas, ils n'étaient même pas des concepts sur la table quand ces systèmes ont été conçus.

NIST SP 800-82 Rev 3 (2023) est honnête à ce sujet. Il décrit les environnements OT comme ayant des *"exigences uniques de performance, de fiabilité et de sécurité"* où *"la sécurité ne peut pas interférer avec le fonctionnement du système."* Relisez ça. **Le principal document d'orientation sur la sécurité de la technologie opérationnelle reconnaît explicitement que la sécurité passe en second.** Ce n'est pas un défaut du document. C'est une description précise de l'environnement.

Vous ne pouvez pas appliquer un contrôle d'accès basé sur les rôles à un API qui n'a aucun concept de rôles utilisateur. Vous ne pouvez pas patcher le firmware sur du matériel dont le fabricant n'existe plus. **Les protocoles série hérités, Modbus RTU et Profibus DP parmi eux, ne fournissent aucune authentification native.** Ils transmettent des commandes et des données à quiconque demande. Il n'y a pas de vérification de qui demande.

*Les orientations sont solides. Les systèmes sont souvent incapables de les recevoir.* Ce ne sont pas les mêmes problèmes.

## Il existe deux catégories complètement différentes de systèmes OT

**Les API hérités des années 1980 au début des années 2000** ont été conçus pour un fonctionnement isolé, uniquement physique. Ils fonctionnent sur des systèmes d'exploitation propriétaires. Ils sont souvent gérés depuis des stations de travail d'ingénierie qui touchent également les réseaux d'entreprise. Leurs configurations sont stockées dans des formats sans vérification d'intégrité. Ces systèmes représentent une partie significative de l'infrastructure déployée dans le traitement des eaux, la production d'énergie, la fabrication et les transports.

**Les contrôleurs modernes capables de sécurité sont différents.** Siemens, Schneider, Rockwell, Beckhoff et Phoenix Contact proposent maintenant des plateformes avec démarrage sécurisé, firmware signé, contrôle d'accès basé sur les rôles, identité soutenue par TPM et communications chiffrées. EtherNet/IP CIP Security, PROFINET Security Class et OPC UA avec authentification existent comme fonctionnalités livrées sur le matériel actuel.

Je ne rejette pas l'ingénierie moderne de sécurité OT. Les progrès sont réels. **Le problème est que la plupart de la base déployée n'est pas moderne.** Quand les gens disent "cybersécurité OT", ils décrivent généralement quelqu'un qui essaie de sécuriser un contrôleur programmable vieux de 20 ans avec un cadre de cybersécurité écrit en 2023. C'est l'écart dont je parle.

## Ce qui fonctionne réellement

**La sécurité physique et l'isolation réseau sont les contrôles les plus fiables disponibles pour les environnements OT hérités.** Chaque grand cadre de sécurité ICS dit la même chose. IEC 62443 organise les environnements OT en zones de sécurité avec des conduits définis. L'intention est que le mouvement latéral passe par des frontières contrôlées plutôt que de glisser sur un réseau plat.

L'isolation réseau réduit considérablement la surface d'attaque réseau. Elle n'élimine pas tous les risques. Les supports amovibles, l'accès illicite, les ordinateurs portables de maintenance, les connexions d'ingénierie temporaires et la compromission de la chaîne d'approvisionnement représentent tous des vecteurs d'entrée documentés dans des systèmes sans exposition réseau. **Stuxnet**, qui a atteint l'installation iranienne de centrifuges à air gappé via des clés USB infectées, est l'exemple canonique. *L'isolation réseau est nécessaire. Elle n'est pas suffisante.*

**La surveillance humaine en boucle des paramètres physiques du processus** reste l'un des mécanismes de détection les plus fiables disponibles. Un opérateur formé qui observe la pression, la température et le débit en temps réel remarquera des choses qu'aucun système de détection d'intrusion ne verra, parce que l'IDS ne peut pas vérifier si la valeur numérique correspond à la réalité physique.

Contrôles qui réduisent le risque dans les bons contextes :

- **Les diodes de données** permettent la télémétrie sortante sans autoriser les connexions entrantes
- **La mise sur liste blanche des applications** sur les postes de travail IHM restreint ce qui s'exécute sur les machines ayant accès aux systèmes de contrôle
- **Les plateformes de détection d'anomalies passives** de Claroty, Dragos et Nozomi analysent le trafic sans toucher aux communications du plan de contrôle
- **La segmentation réseau** entre les zones OT ralentit le mouvement latéral sans exiger des air gaps complets
- **Les principes de confiance-zéro**, référencés dans NIST SP 800-82 Rev 3, ajoutent des exigences de vérification par session à certaines architectures OT modernes

*Aucun de ces éléments ne résout les contraintes de conception sous-jacentes. Ils réduisent le risque aux marges de systèmes qui n'ont jamais été construits pour cela.*

## Les signaux analogiques ne peuvent pas être authentifiés

**Les boucles de courant 4-20mA, les signaux 0-10V, les sorties de thermocouple et les lectures RTD transmettent sous forme de signaux électriques variables.** Il n'y a pas de mécanisme dans le signal physique pour vérifier l'authenticité. Quiconque met le bon signal sur le fil est cru.

Stuxnet l'a rendu concret. L'attaque a manipulé la logique API s'exécutant sur les contrôleurs Siemens S7 tout en rejoignant simultanément des données de processus normales enregistrées précédemment aux interfaces opérateur. **Les opérateurs regardaient des écrans montrant des lectures normales pendant que les centrifuges étaient poussées au-delà de leurs limites opérationnelles.** La tromperie a tenu suffisamment longtemps pour causer des dommages physiques qui apparaissaient comme une défaillance d'équipement plutôt qu'une attaque.

Les interférences électromagnétiques des câbles d'alimentation, des variateurs de fréquence, de la foudre et d'une mise à la terre inappropriée corrompent les mesures analogiques en fonctionnement normal. IEC 61000 existe pour cette raison. Les installations industrielles utilisent le câblage blindé, la mise à la terre appropriée, le filtrage et la séparation physique pour le gérer.

Les appareils de terrain intelligents modernes convertissent les mesures analogiques en forme numérique en interne avant de les transmettre via HART-IP, WirelessHART, EtherNet/IP CIP Security ou OPC UA. Des communications numériques authentifiées sont disponibles au niveau de l'appareil sur le matériel moderne. **Le fil 4-20mA analogique reliant un transmetteur hérité à une entrée API héritée ne porte aucune authentification et n'en portera jamais.** Pour une partie significative de l'instrumentation déployée, c'est encore le fil utilisé.

## La validation des capteurs est un contrôle de sécurité fonctionnelle, pas un contrôle de cybersécurité

Les systèmes de sécurité des processus effectuent un **vote redondant des capteurs**. Un arrangement 2-sur-3 avec deux capteurs lisant 230 PSI et un lisant 14 PSI signale l'aberrant. Cela offre une résilience limitée contre la manipulation d'un seul point de capteur. *C'est un contrôle d'ingénierie de sécurité fonctionnelle, pas un contrôle de cybersécurité.*

Les API standard n'ont pas de validation cryptographique pour leurs entrées analogiques. Un générateur de signal injecté sur la boucle est indiscernable d'un transmetteur légitime. L'API lit le courant et agit en conséquence.

**Les systèmes instrumentés de sécurité étaient censés être la dernière ligne de défense indépendante.** En 2017, **TRITON** (également connu sous le nom de **TRISIS**) a ciblé les unités Schneider Electric Triconex SIS avec l'objectif spécifique de désactiver cette couche. Les attaquants ont atteint le système de sécurité via le réseau des stations de travail d'ingénierie. *L'indépendance de la couche dépendait d'une séparation réseau qui n'avait pas été maintenue.*

IEC 62443-3-3, IEC 62443-4-2 et la coordination avec la sécurité fonctionnelle sous IEC 61511 reflètent maintenant cette leçon. **TRITON a démontré en pratique ce que l'analyse indépendante avait argumenté en théorie :** un attaquant qui neutralise le système de sécurité avant de déclencher la condition dangereuse supprime le dernier contrôle empêchant les conséquences physiques.

## Votre chaîne d'approvisionnement est le vecteur que vous ignorez probablement

**La plupart des programmes de sécurité OT se concentrent sur l'architecture réseau. La plupart des compromissions OT récentes ont utilisé des points d'entrée que l'architecture réseau n'arrête pas.**

Les risques de la chaîne d'approvisionnement OT comprennent :

- **L'intégrité du firmware avant l'installation** — si le matériel arrive avec un firmware non vérifié de l'usine ou du distributeur
- **Les sessions d'accès à distance des fournisseurs**, qui restent des expositions persistantes sur les sites dépendant du support des fabricants
- **Les stations de travail d'ingénierie** qui se connectent à la fois au réseau d'entreprise et au réseau OT, souvent pour des raisons de commodité opérationnelle
- L'absence de **nomenclatures logicielles (SBOM)** pour la plupart des déploiements OT hérités, rendant le suivi des composants logiciels largement impossible
- **Les entreprises de maintenance** qui apportent des ordinateurs portables et des supports USB dans des environnements opérationnellement isolés
- **Le support des mises à jour de firmware signé**, que la plupart des anciennes plateformes n'ont pas

*Si votre air gap est intact en interne mais que votre fournisseur d'équipement maintient un portail d'accès à distance persistant dans votre réseau d'ingénierie, vous n'avez pas d'air gap. Vous avez un gap avec une porte dedans que quelqu'un d'autre contrôle.*

## Renforcer les systèmes hérités coûte plus que prévu

Chaque programme API est écrit sur mesure pour un processus spécifique. La logique qui pilote le système de contrôle de surtension d'une raffinerie diffère entièrement de la logique qui pilote une séquence de chloration de traitement des eaux ou un régulateur de turbine. Ce n'est pas un choix. Les processus physiques sont différents.

**Le renforcement des systèmes OT hérités coûte souvent plus que prévu** en raison des exigences de validation en ingénierie, des temps d'arrêt nécessaires, des contraintes du support des fournisseurs, des lacunes de documentation et des cycles de test qui dépassent les estimations initiales. Dans certains cas impliquant du matériel sans support fournisseur, les coûts de renforcement approchent ou dépassent le coût de remplacement du système.

**La conformité NERC CIP pour les cyber-actifs du système électrique en vrac coûte des millions de dollars par an aux services publics individuels.** Une enquête de 2019 de l'American Public Power Association a documenté des coûts de conformité variant fortement, les petits services publics rapportant une charge disproportionnée par rapport à leur taille. De nombreux systèmes d'eau et petits services publics opèrent en dehors des exigences NERC CIP et ne font face à aucune obligation de conformité comparable.

## Les systèmes devraient être remplacés

**Remplacer les systèmes OT hérités est la bonne réponse.** Dans les grandes installations, cela signifie des dizaines de millions de dollars, des périodes de transition prolongées et le risque d'encoder incorrectement des connaissances opérationnelles complexes lors de la migration. Ce sont des coûts réels et des risques réels.

Ce que les orientations industrielles recommandent réellement, via CISA et ICS-CERT, c'est d'appliquer des contrôles compensatoires pendant que la planification du remplacement progresse. C'est une réponse rationnelle aux contraintes. *Lu clairement, cela reconnaît que la sécurité complète n'est pas atteignable sur les équipements hérités, donc appliquez les contrôles qui conviennent et planifiez un remplacement éventuel.*

**La réalité pratique est que beaucoup de ces systèmes resteront en service pendant des décennies.** C'est un problème de financement et de politique. La communauté technique a été claire sur ce qui doit se passer. Les budgets opérationnels et les calendriers de remplacement n'ont pas suivi.

## Ajouter une connectivité réseau aux systèmes OT aggrave souvent les choses

De nombreuses organisations ont ajouté des capacités d'accès à distance et de surveillance à des environnements OT qui étaient à l'origine isolés. L'argument opérationnel est simple : la visibilité à distance réduit le temps de réponse, et le support des fournisseurs est plus rapide avec une connexion à distance. **La conséquence en termes de sécurité est que des systèmes isolés sans surface d'attaque réseau en ont maintenant une.**

**L'incident de traitement des eaux d'Oldsmar en 2021** s'est produit via une connexion d'accès à distance TeamViewer. L'attaquant a modifié les paramètres de dosage en hydroxyde de sodium via un outil d'accès à distance légitime ajouté pour la commodité. **L'incident Colonial Pipeline de 2021** a commencé par une compromission du réseau informatique. L'opérateur a arrêté proactivement les opérations pipeline OT parce qu'il ne pouvait pas confirmer que le réseau OT n'était pas affecté. *L'attaque n'a pas directement violé le réseau OT. L'incertitude quant à savoir si elle l'avait fait a causé l'arrêt.*

Ajouter une connectivité réseau à des systèmes OT hérités pour des avantages opérationnels, sans architecturer cette connectivité selon des normes appropriées, **produit plus de risque que le bénéfice ne le justifie dans de nombreux cas**.

## La conformité aux normes écrites n'est pas la sécurité

NIST SP 800-82 Rev 3, IEC 62443 et NERC CIP décrivent les bons contrôles pour ce que sont ces systèmes. Je ne les rejette pas. Je souligne ce qu'ils disent explicitement : **tous les systèmes OT ne peuvent pas implémenter tous les contrôles.** Les cadres utilisent des niveaux de sécurité échelonnés et des dispositions de contrôles compensatoires précisément parce que les systèmes auxquels ils s'appliquent ne peuvent souvent pas satisfaire les exigences complètes.

L'écart entre ce que les normes décrivent et ce qu'un déploiement hérité donné peut atteindre n'est pas une erreur de documentation. Les systèmes ne supportent pas les contrôles. Les orientations le reconnaissent. **Atteindre un résultat d'audit conforme sur OT hérité ne signifie pas que l'environnement est sécurisé.** Cela signifie que vous avez documenté les contrôles compensatoires en place, et un auditeur les a acceptés.

**Quand quelqu'un vous dit que répondre aux exigences de conformité rend votre environnement OT sécurisé, il dit quelque chose que les cadres auxquels il se réfère ne soutiennent pas.**

## Ce que vous devriez faire avec les OT hérités

Si vous exploitez des environnements OT hérités :

- **Traitez l'isolation réseau comme votre contrôle principal** et auditez tout ce qui franchit la frontière OT
- **Donnez à vos stations de travail d'ingénierie leur propre plan de renforcement.** Elles touchent les deux mondes et sont fréquemment le point d'entrée
- **Contrôlez et journalisez tous les supports amovibles** dans les zones OT
- **Auditez l'accès à distance des fournisseurs** et fermez chaque session non activement utilisée
- Implémentez une surveillance redondante des capteurs là où la conception du processus le permet
- **Construisez un calendrier de remplacement avec de vraies estimations de coûts**, même si le remplacement est à des années
- **Arrêtez de traiter la complétion de l'audit de conformité comme un jalon de sécurité**

Si vous acquérez de nouveaux systèmes OT :

- **Inscrivez les exigences de sécurité dans le cahier des charges d'acquisition** avant que les fournisseurs ne répondent
- Choisissez des plateformes avec un support documenté pour les communications authentifiées, les mises à jour de firmware signées et le contrôle d'accès basé sur les rôles
- **Concevez les frontières IT/OT comme des conduits explicites selon IEC 62443**, pas comme une vague politique "gardez-les séparés"
- **Exigez des SBOM pour les composants logiciels OT** comme livrable contractuel

L'industrie a bien documenté le problème. Les normes sont techniquement précises. *Les systèmes sur le terrain ne peuvent souvent pas recevoir ce que les normes prescrivent.* Reconnaître cela ouvertement est le point de départ pour prendre des décisions sur la façon de gérer le risque résiduel.

## Références

- NIST SP 800-82 Rev 3: Guide to Operational Technology (OT) Security (2023)
- IEC 62443: Industrial Automation and Control Systems Security series
- IEC 62443-3-3: System security requirements and security levels
- IEC 62443-4-2: Technical security requirements for IACS components
- IEC 61511: Functional Safety for Safety Instrumented Systems
- NERC CIP: Critical Infrastructure Protection standards for the bulk electric system
- IEC 61000: Electromagnetic Compatibility standards
- CISA ICS-CERT Advisories and Best Practices
- MITRE ATT&CK for ICS framework
- Stuxnet technical analysis, Langner Communications, 2011
- TRITON/TRISIS technical analysis, Dragos, 2017
- Oldsmar Water Treatment incident review, CISA, 2021
- American Public Power Association NERC CIP Compliance Cost Survey, 2019
