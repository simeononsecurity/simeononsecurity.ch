---
title: "La cybersécurité de l'IA et les certifications de gouvernance ne suivent pas le rythme du problème"
draft: false
toc: true
date: 2026-06-26
description: "Une opinion professionnelle sur l'écart entre les certifications de gouvernance de l'IA et la pratique réelle de la sécurité de l'IA. Nous en avons passé plusieurs et sommes repartis déçus. Les frameworks sont récents et axés sur la gouvernance. La surface d'attaque a évolué plus vite."
tags: ["sécurité IA", "gouvernance IA", "certifications IA", "NIST AI RMF", "NIST AI 600-1", "ISO 42001", "IAPP AIGP", "injection de prompt", "cybersécurité IA", "sécurité LLM", "OWASP LLM Top 10", "MITRE ATLAS", "gestion des risques IA", "conformité IA", "sécurité machine learning", "chaîne d'approvisionnement modèle", "IA adversariale", "agents IA", "sécurité MCP", "red teaming IA", "certifications gouvernance IA", "IA agentique", "Google SAIF"]
cover: "/img/cover/ai-cybersecurity-governance-certifications-disappointing.webp"
coverAlt: "L'image montre une scène divisée : d'un côté, des professionnels dans un bureau discutant de documents de gouvernance ; de l'autre, des visuels numériques chaotiques représentant des systèmes d'IA sous cyberattaque, avec des couleurs vives soulignant le contraste."
coverCaption: ""
---

Nous avons passé les examens. Nous avons réussi. Nous sommes repartis avec des certificats et un niveau de déception que je souhaite formuler avec précision.

Ce n'est pas une critique envers les personnes qui ont conçu ces programmes. Elles travaillent avec du matériel incomplet. La sécurité de l'IA en tant que discipline est jeune. La recherche sur les attaques progresse plus vite que les outils défensifs. Les frameworks de gouvernance sont arrivés avant les conseils d'ingénierie.

Le problème est l'écart entre ce que les certifications enseignent et ce que vous devez savoir pour réellement sécuriser des systèmes d'IA en production.

## Trois couches fréquemment confondues

Avant d'expliquer ce qui manque, il est utile de distinguer ce qui existe actuellement.

La première couche est la gouvernance. Les documents comme le NIST AI Risk Management Framework (AI RMF 1.0, 2023), ISO/IEC 42001:2023 et l'EU AI Act fonctionnent au niveau organisationnel et processuel. Ils décrivent comment gérer les risques liés à l'IA, structurer la surveillance et documenter la responsabilité. Ils sont délibérément axés sur la gouvernance plutôt que sur la prescription de contrôles. C'est voulu.

La deuxième couche est la taxonomie des menaces. MITRE ATLAS documente les tactiques adversariales contre les systèmes d'IA dans le même format qu'ATT&CK. Le OWASP Top 10 pour les applications de grands modèles de langage énumère les classes d'attaques les plus pertinentes pour les LLMs déployés. Ces documents nomment les attaques et décrivent leur fonctionnement. Ils ne prescrivent pas de défenses.

La troisième couche est le guide technique. Cela comprend le Secure AI Framework (SAIF) de Google, l'AI Security SDL de Microsoft, OWASP AI Exchange, NIST AI 600-1 (le profil d'IA générative) et la documentation de sécurité spécifique aux fournisseurs d'Anthropic, OpenAI, Meta et d'autres. Ces ressources fournissent des conseils d'ingénierie sur le déploiement sécurisé, les pratiques d'évaluation et les contrôles d'exécution.

La plupart des certifications de gouvernance de l'IA couvrent la première couche de manière approfondie. Elles référencent la deuxième couche à un niveau sommaire. Elles touchent rarement la troisième.

## Ce que les certifications couvrent

Les certifications de gouvernance et de sécurité de l'IA actuellement disponibles, notamment IAPP AI Governance Professional (AIGP), le certificat AI Fundamentals d'ISACA, les certifications ISO 42001 et CompTIA AI+, couvrent un ensemble cohérent de sujets.

Vous apprenez le NIST AI RMF et comment mapper ses quatre fonctions, Govern, Map, Measure et Manage, au déploiement de l'IA de votre organisation. Vous apprenez les classifications des niveaux de risque de l'EU AI Act et à quoi ressemble l'évaluation de conformité pour les systèmes à haut risque. Vous apprenez les principes de gouvernance que sont le biais, l'équité, la transparence et la responsabilité. Vous apprenez à rédiger des politiques de gouvernance de l'IA et à mener des analyses d'impact.

Ce sont de vraies compétences. Les organisations ont besoin de personnes qui comprennent les frameworks de gouvernance. Elles ont besoin de personnes qui lisent le NIST AI RMF et savent ce qu'il leur demande de construire.

Ce que les certifications n'enseignent pas avec la même profondeur :

- Comment les attaquants compromettent actuellement les systèmes d'IA en production
- À quoi ressemble la défense en profondeur contre l'injection de prompt de manière opérationnelle et pourquoi aucun contrôle unique ne l'élimine
- Comment vérifier l'intégrité des modèles avant le déploiement
- Ce qu'implique le red teaming spécifique à l'IA et comment le délimiter
- Comment évaluer le comportement d'un modèle face aux entrées adversariales avant le lancement
- À quoi ressemble l'observabilité de l'IA au moment de l'inférence
- En quoi la réponse aux incidents IA diffère des playbooks IR standard
- Ce que la sécurisation des agents IA avec accès aux outils et intégrations externes requiert

## Le NIST AI RMF est de la gouvernance, pas de l'ingénierie

Le NIST AI RMF est un document bien construit. NIST l'a conçu pour être neutre technologiquement, agnostique au secteur et applicable à différentes approches de développement de l'IA. Cela produit un framework d'application large.

Cela signifie aussi que le framework ne prescrit pas de contrôles techniques pour des classes d'attaques spécifiques. Si votre organisation adopte pleinement l'AI RMF et mappe toutes ses fonctions à votre déploiement d'IA, vous aurez des processus de risque documentés. Vous n'aurez pas nécessairement une défense contre l'injection de prompt sur votre modèle de langage déployé.

NIST le reconnaît. NIST AI 600-1, le profil d'IA générative publié en 2024, étend l'AI RMF spécifiquement pour l'IA générative et les grands modèles de langage. Il couvre des risques incluant l'injection de prompt, l'empoisonnement des données et les risques informationnels à un niveau de spécificité que l'AI RMF de base n'atteint pas. Si votre certification couvrait l'AI RMF de base sans AI 600-1, vous avez manqué le document le plus pertinent pour les systèmes actuellement déployés.

## ISO 42001 et la comparaison avec le système de management

ISO 42001:2023 est une norme de système de management de l'IA. Elle fournit une structure pour gouverner le développement et le déploiement de l'IA au niveau organisationnel. Les professionnels de la sécurité reconnaîtront le parallèle avec ISO 27001 pour la sécurité de l'information.

ISO 27001 est largement adoptée. Les organisations certifiées se font encore compromettre. La certification documente qu'un système de management existe, suit un processus défini et fait l'objet d'une révision. Elle ne certifie pas que les systèmes gouvernés par ce processus résistent aux attaques utilisées contre eux.

ISO 42001 apporte de la discipline organisationnelle. Obtenir la certification indique aux parties prenantes que vos processus d'IA sont documentés, révisés et soumis à la gouvernance. Cela ne leur dit pas si vos modèles déployés produisent des sorties cohérentes dans des conditions adversariales, si vos agents opèrent dans des limites de confiance définies, ou si vos modèles affinés ont été construits à partir de données d'entraînement vérifiées.

C'est la même lacune qu'ISO 27001. En cybersécurité traditionnelle, nous avons appris à vivre avec. Nous ne devrions pas prétendre que les certifications de gouvernance de l'IA la comblent alors qu'elles partagent la même limitation structurelle.

## L'EU AI Act crée des exigences de résultats sans spécifications d'ingénierie

L'EU AI Act classe les systèmes d'IA par niveau de risque : inacceptable (interdit), haut risque (évaluation de conformité requise), risque limité (obligations de transparence) et risque minimal (pas d'exigences spécifiques).

Les systèmes à haut risque, notamment ceux utilisés dans les infrastructures critiques, l'identification biométrique, le filtrage de l'emploi, l'éducation et l'application de la loi, font face à des exigences de documentation technique, des obligations de surveillance humaine et des exigences de robustesse. L'Acte exige explicitement que les systèmes d'IA à haut risque soient robustes contre les tentatives de modification de leur comportement par manipulation adversariale.

Cette exigence figure dans le texte. L'Acte spécifie intentionnellement des résultats plutôt que de prescrire des contrôles techniques. Les méthodes techniques pour démontrer la robustesse adversariale dans tous les contextes de déploiement n'ont pas encore de réponses consensuelles pour chaque type de système et chaque cas d'usage.

Les certifications construites autour de l'EU AI Act vous préparent à classer les systèmes d'IA, à rédiger la documentation technique et à structurer les protocoles de surveillance. Elles vous préparent pour l'audit. Le travail d'ingénierie qui produit un système conforme aux exigences de robustesse de l'Acte relève d'une discipline différente de celle que couvrent actuellement les certifications.

## Ce qui attaque réellement les systèmes d'IA

MITRE ATLAS et OWASP LLM Top 10 documentent le paysage opérationnel des menaces. Ce sont les ressources qui énumèrent les attaques à un niveau de détail utile. Les frameworks de gouvernance référencent les menaces à un niveau d'abstraction plus élevé. Ce qui suit provient de ces sources spécifiques à la sécurité.

L'injection de prompt fonctionne en fournissant des entrées à un modèle de langage qui écrasent ou manipulent les instructions système. L'injection directe cible directement l'entrée du modèle. L'injection indirecte intègre des instructions malveillantes dans le contenu que le modèle récupère, traite ou résume. Votre pipeline RAG lit un document contrôlé par un attaquant et agit sur des instructions qui y sont cachées. Votre agent de navigation visite une page contrôlée par un attaquant et suit ses directives intégrées. Votre bot de support client résume un article de support contenant des instructions pour ignorer ses directives de sécurité.

Il n'existe pas de mitigation universellement efficace contre l'injection de prompt en 2026. La défense en profondeur réduit le risque : filtrage des entrées, validation des sorties, périmètres d'outils à privilèges limités, environnements d'exécution en sandbox et portails d'approbation humaine pour les actions conséquentes. Aucun de ces éléments n'élimine la classe d'attaque. NIST, OWASP, Anthropic, OpenAI, Google et Microsoft recommandent tous des contrôles en couches plutôt que des solutions uniques.

L'empoisonnement des données d'entraînement introduit des exemples malveillants dans les données d'entraînement pour dégrader le comportement du modèle, introduire des portes dérobées ou implanter des comportements basés sur des déclencheurs. Le signal d'un empoisonnement réussi est souvent absent jusqu'à ce que le modèle rencontre des entrées de déclenchement spécifiques. Si votre organisation affine des modèles sur du contenu généré par les utilisateurs, des documents récupérés ou des ensembles de données tiers sans vérifier leur provenance, vous faites face à ce risque.

La compromission de la chaîne d'approvisionnement des modèles est la menace que la plupart des organisations traitent comme secondaire. Les dépôts de modèles distribuent souvent du code exécutable aux côtés des poids du modèle, et des formats de sérialisation non sécurisés comme pickle ont créé à plusieurs reprises des risques pour la chaîne d'approvisionnement. Les packages accompagnant les téléchargements de modèles peuvent installer des dépendances avec leurs propres vulnérabilités. De nombreuses organisations téléchargent des modèles en appliquant beaucoup moins de scrutin à la chaîne d'approvisionnement qu'elles n'en appliquent aux dépendances logicielles. La surface d'attaque est comparable à npm, mais la culture de sécurité qui l'entoure est beaucoup plus précoce.

L'extraction de modèles permet aux attaquants de reconstruire des modèles fonctionnellement similaires par des requêtes d'inférence répétées contre votre API. Cela représente à la fois une perte de propriété intellectuelle et un moyen d'étudier votre modèle hors ligne pour développer des attaques plus ciblées.

L'inférence d'appartenance permet aux attaquants de déterminer avec diverses certitudes si des enregistrements de données spécifiques étaient dans votre ensemble d'entraînement, selon l'architecture du modèle et le régime d'entraînement. Cela crée un risque de confidentialité pour les organisations qui ont entraîné sur des informations personnelles.

Les entrées adversariales manipulent les sorties du modèle par des perturbations construites. La technique est la plus étudiée dans la classification d'images, mais s'applique au texte, à l'audio et aux systèmes multimodaux. Si votre IA prend des décisions sur la détection de fraude, la solvabilité, l'imagerie médicale ou l'accès physique, la robustesse adversariale est une propriété de sécurité que vous devez tester, pas seulement documenter.

La fuite de données par les systèmes d'IA est une catégorie qui mérite une attention directe. Les pipelines RAG exposent des documents de votre base de connaissances, parfois à des utilisateurs qui ne devraient pas y avoir accès. La fuite de prompt à partir des instructions système révèle des détails opérationnels que vous vouliez garder confidentiels. Les déploiements d'IA multi-locataires créent des exigences d'isolation que les ingénieurs de sécurité applicative traditionnels sous-estiment parfois. Ce sont des risques opérationnels qui apparaissent régulièrement dans les systèmes déployés.

## Les agents IA changent complètement la surface d'attaque

La plupart des certifications de sécurité de l'IA ont été rédigées quand les systèmes d'IA signifiaient principalement des chatbots et des classificateurs. L'IA d'entreprise en 2026 signifie de plus en plus des agents.

Les agents diffèrent des chatbots sur un point opérationnellement important : ils prennent des actions. Un agent avec accès aux outils de votre système de messagerie, aux bases de données internes, aux systèmes de fichiers, au navigateur et aux environnements d'exécution de code n'est pas un chatbot avec plus de fonctionnalités. C'est un processus autonome avec un accès significatif aux systèmes réels, opérant sur la base des sorties du modèle de langage.

OWASP maintient maintenant un Agentic AI Top 10 séparé parce que le modèle de menace pour les agents diffère suffisamment des applications de chat LLM pour nécessiter une documentation séparée.

L'injection de prompt dans un contexte agent ne produit pas une réponse textuelle indésirable. Elle produit une action indésirable. Une injection indirecte dans un document récupéré ordonne à l'agent de supprimer des fichiers, d'exfiltrer des données ou d'envoyer des e-mails. La conséquence n'est pas une réponse inappropriée. C'est une action non autorisée effectuée contre des systèmes auxquels l'agent a accès.

La surface d'attaque pour les agents comprend :

- Les limites d'invocation d'outils : si l'agent est restreint à un ensemble minimal d'outils appropriés pour chaque tâche
- La portée des identifiants : si les identifiants détenus par l'agent sont limités à ce que chaque tâche exige
- La réversibilité des actions : si les actions conséquentes nécessitent une approbation humaine avant exécution
- Le filtrage des sorties : si les sorties de l'agent sont validées avant de déclencher des actions en aval
- Le sandboxing : si l'environnement d'exécution de l'agent empêche un accès non intentionnel aux systèmes connectés

La plupart des certifications de gouvernance de l'IA ne couvrent pas la conception de la sécurité des agents à ce niveau de spécificité.

## Le Model Context Protocol crée une nouvelle surface d'attaque pour les entreprises

Le Model Context Protocol (MCP) est devenu une norme largement adoptée pour connecter les agents IA aux outils externes, sources de données et services. Les serveurs MCP exposent des capacités que les agents découvrent et utilisent. L'intégration est rapide et flexible. Les implications en matière de sécurité ne reçoivent pas toujours une attention équivalente.

Les risques spécifiques au MCP comprennent :

- Les serveurs MCP malveillants qui déforment leurs capacités auprès d'un agent et exécutent des actions non prévues
- L'empoisonnement d'outils où un serveur MCP légitime renvoie des données contrôlées par un attaquant et intègre des instructions dans ce qui devrait être des sorties de données
- Les outils sur-privilégiés où les intégrations MCP détiennent des permissions au-delà de ce que la tâche exige
- La confusion des limites de confiance où les agents reçoivent des instructions d'outils MCP attachés qui semblent équivalentes aux instructions utilisateur

Les organisations déployant des agents avec des intégrations MCP ont besoin d'un framework pour évaluer la confiance des serveurs MCP, auditer les permissions des outils et valider que les réponses des outils sont traitées comme des données plutôt que comme des instructions.

## L'évaluation est la pratique opérationnelle que les certifications ignorent

Le red teaming de l'IA et les suites d'évaluation remplacent les évaluations de sécurité statiques comme méthodes principales pour comprendre le risque des modèles d'IA avant et après le déploiement.

Le red teaming pour l'IA implique :

- Des tests adversariaux structurés du comportement du modèle contre des techniques d'attaque connues
- Des benchmarks de jailbreak contre des ensembles de données d'attaques de prompt établis
- Des tests de robustesse adversariale qui mesurent la dérive des sorties sous des entrées perturbées
- Des tests de régression comportementale entre les versions du modèle
- L'évaluation de benchmarks de sécurité contre des suites d'évaluation publiées

NIST, Anthropic, OpenAI, Microsoft, Google et CISA recommandent tous le red teaming spécifique à l'IA avant le déploiement pour les systèmes à haut risque. Cela devient une attente standard, pas une pratique optionnelle.

Aucune des certifications actuelles de gouvernance de l'IA ne prépare adéquatement les praticiens à délimiter, exécuter ou interpréter un exercice de red teaming contre un modèle ou un système d'agent déployé. Elles décrivent ce qu'est le red teaming. Elles ne vous apprennent pas à le faire.

## L'observabilité de l'IA est une discipline distincte

La journalisation de sécurité traditionnelle ne se transfère pas directement aux systèmes d'IA. Surveiller un LLM ou un agent en production nécessite une collecte de données différente et une analyse différente.

L'infrastructure d'observabilité de l'IA couvre :

- La télémétrie des prompts et des sorties pour la détection d'anomalies et l'identification des violations de politique
- Les journaux d'invocation d'outils pour les agents, y compris quels outils ont été appelés avec quels arguments
- La surveillance de la qualité de récupération pour les pipelines RAG
- La détection et la classification des tentatives de jailbreak
- La surveillance de la cohérence des sorties pour détecter la dérive du modèle entre les versions
- Le suivi du taux d'hallucination pour les applications où la précision factuelle est importante
- Les patterns de latence qui peuvent indiquer des tentatives d'injection de prompt gonflant la taille du contexte

C'est une discipline émergente. La plupart des organisations déployant de l'IA en 2026 ont significativement moins de visibilité sur leurs composants d'IA que sur leur infrastructure traditionnelle. La plupart des certifications de gouvernance ne décrivent pas à quoi ressemble une observabilité adéquate pour les systèmes d'IA.

## La réponse aux incidents IA n'est pas comme la réponse IR habituelle

Quand un système traditionnel est compromis, votre playbook IR couvre le confinement, la forensique et la récupération. Les incidents IA introduisent des questions que le playbook standard n'adresse pas.

Questions pour lesquelles vous avez besoin de playbooks avant d'en avoir besoin :

- Comment déterminer si un modèle a été empoisonné lors de l'affinage
- Comment évaluer si une récupération RAG a été utilisée pour retourner du contenu contrôlé par un attaquant
- Comment identifier si un agent a exécuté des actions non autorisées et quelle en était la portée
- Comment vérifier si une mise à jour de modèle d'un fournisseur tiers a modifié le comportement de manière pertinente pour la sécurité
- Comment établir quel était le comportement d'un modèle avant un incident pour le comparer au comportement post-incident

Cela nécessite une préparation avant l'incident. Cela nécessite des journaux et une télémétrie que vous devez configurer à l'avance. Cela nécessite des runbooks spécifiques à l'IA qui consacrent de l'espace à la forensique sur le comportement du modèle, pas seulement au trafic réseau et aux journaux d'endpoint.

## Le problème de mise à jour des certifications

Une raison structurelle pour laquelle les certifications sont en retard sur la pratique actuelle : la sécurité de l'IA évolue plus vite que les cycles de mise à jour des certifications ne le permettent.

Security+, CISSP et ISO 27001 couvrent des domaines qui évoluent sur des années. Les surfaces d'attaque de base des réseaux, endpoints et applications sont relativement stables. Les techniques d'attaque de l'IA évoluent en quelques mois. Les techniques d'injection de prompt, les méthodes d'attaque adversariale et les surfaces d'attaque agentiques en 2026 sont différentes de ce qui existait quand les premières certifications IA ont été lancées en 2023 et 2024.

Les organismes de certification mettent à jour les matériaux selon des calendriers. Le OWASP LLM Top 10 a publié une révision significative dans sa première année. MCP n'existait pas comme préoccupation d'entreprise quand de nombreuses certifications IA actuelles ont été conçues. Les frameworks de sécurité de l'IA agentique postdatent la plupart des programmes de certification actuels.

C'est un problème structurel, pas un échec d'intention. Vous devez lire les sources primaires de manière continue plutôt que de traiter une certification comme un corpus fixe de connaissances.

## Ce qui doit figurer dans le contenu des certifications de sécurité de l'IA

Pour que les programmes de certification reflètent la pratique actuelle de la sécurité de l'IA, ils doivent couvrir :

- La défense en profondeur contre l'injection de prompt : filtrage des entrées, validation des sorties, délimitation des outils, sandboxing et portails d'approbation humaine, ainsi que les limitations documentées de chacun
- La vérification de la chaîne d'approvisionnement des modèles : risques de sérialisation non sécurisée, exigences SBOM, documentation de provenance et vérification des artefacts signés
- L'architecture de sécurité des agents IA : limites de confiance, accès aux outils à privilèges minimaux, réversibilité des actions et exigences de surveillance
- La sécurité MCP et des intégrations externes : évaluation de la confiance pour les serveurs d'outils, audit des permissions des outils et séparation données vs. instructions
- L'évaluation et le red teaming : comment délimiter une évaluation adversariale, quels benchmarks et ensembles de données d'évaluation existent et comment interpréter les résultats
- L'observabilité de l'IA : quels journaux et quelle télémétrie les systèmes d'IA nécessitent, et comment les utiliser pour la détection d'incidents et la réponse
- La réponse aux incidents spécifique à l'IA : planification préalable pour les scénarios d'incidents IA, collecte de preuves pour les questions de comportement des modèles et considérations de récupération uniques aux systèmes d'IA
- La prévention des fuites de données : isolation RAG, confidentialité des prompts, contrôles d'accès multi-locataires et filtrage des sorties

## Ce que vous devriez faire maintenant

Si vous êtes responsable de systèmes d'IA dans votre organisation :

Lisez le OWASP Top 10 pour les applications de grands modèles de langage et le OWASP Agentic AI Top 10. Ils sont gratuits. Ils sont plus spécifiques opérationnellement que tout programme de certification payant actuel.

Examinez MITRE ATLAS avant votre prochaine session de modélisation des menaces sur tout composant IA. Sachez quelles tactiques adversariales s'appliquent à votre architecture avant de finaliser votre conception de déploiement.

Lisez NIST AI 600-1. Il étend l'AI RMF de base spécifiquement pour l'IA générative et est significativement plus pertinent pour les déploiements LLM et agents que le framework de base seul.

Examinez Google SAIF, l'AI SDL de Microsoft et OWASP AI Exchange pour des conseils au niveau d'ingénierie que les frameworks de gouvernance ne fournissent pas.

Vérifiez la provenance de chaque modèle que votre organisation déploie. Vérifiez les fiches de modèle. Analysez les formats de sérialisation pour les classes d'exploits connues avant de charger les poids.

Cartographiez chaque agent IA dans votre environnement par rapport aux accès qu'il détient. Un agent avec accès en lecture et écriture à votre base de connaissances interne, à votre messagerie et à votre système de fichiers est un amplificateur d'injection de prompt. Minimisez ses identifiants à ce que chaque tâche exige.

Exigez un red teaming spécifique à l'IA avant de déployer tout modèle ou agent dans un contexte à fort impact. Traitez-le comme obligatoire, pas optionnel.

Construisez des runbooks de réponse aux incidents spécifiques à l'IA maintenant, avant d'en avoir besoin.

Traitez votre certification de gouvernance comme la documentation de votre couche de processus. Ce n'est pas la documentation de votre posture de sécurité.

## Références

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- NIST SP 1270: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL documentation
- CISA Guidance on AI Cybersecurity, 2024
- Barreno et al., Can Machine Learning Be Secure?, 2006
- Biggio et al., Poisoning Attacks Against Support Vector Machines, 2012
- Goodfellow et al., Explaining and Harnessing Adversarial Examples, ICLR 2015
- IAPP AI Governance Professional (AIGP) program documentation
- ISACA AI Fundamentals Certificate program documentation
