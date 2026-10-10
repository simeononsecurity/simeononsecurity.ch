---
title: "10 plugins, compétences et outils MCP pour Claude Code : guide pratique"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Choisissez des extensions Claude Code pour la planification, la revue de code, la gestion des connaissances, le design et l'automatisation. Comparez dix outils, leurs dépendances et des contrôles pratiques."
genre: ["Intelligence artificielle", "Outils pour développeurs", "Développement logiciel"]
tags: ["plugins Claude Code", "compétences Claude Code", "outils MCP", "Graphify", "grill-me", "grill-with-docs", "grill-me-codex", "Claudex Loop", "plugin Codex", "revue de code", "claude-obsidian", "Obsidian", "CLAUDE.md", "directives Karpathy", "Impeccable", "Higgsfield", "NotebookLM", "notebooklm-py", "n8n MCP", "flux de développement IA", "instructions d'agent", "graphes de connaissances"]
cover: "/img/cover/claude-code-plugins-workflow-management-tools.webp"
coverAlt: "Icônes d'outils bleues et violettes, dossiers et panneaux de graphiques abstraits reliés à un centre géométrique sur fond sombre"
coverCaption: "Illustration conceptuelle d'un flux de travail. Les formes de graphiques ne représentent aucun résultat mesuré."
---

**Choisissez une extension Claude Code autour d'un problème précis de votre flux de travail.** Des exigences floues demandent une conversation de planification. Des défauts manqués demandent une revue et des tests. Des recherches répétées demandent des sources traçables. Installer plus d'outils aide seulement lorsque leurs responsabilités sont claires.

Ce guide compare **dix projets** pour ces tâches, avec des exemples de configuration et un exercice d'évaluation guidé. L'analyse s'appuie sur la documentation actuelle des projets et sur la vidéo Chase AI fournie. Les recommandations sont des jugements éditoriaux. Elles ne constituent ni des mesures de performance pratiques ni une preuve d'une hausse de productivité décuplée.

<!--more-->

## Points clés

- **Choisissez selon le résultat :** un plan revu, une carte du code et une image générée demandent des outils différents.
- **Séparez les couches d'installation :** les instructions, les programmes exécutables, les plugins et les connexions aux services ont des dépendances différentes.
- **Vérifiez les noms actuels :** Graphify et grill-me-codex ont désormais des emplacements de dépôt canoniques différents.
- **Allez au-delà de l'accord :** deux modèles qui acceptent un plan ne prouvent pas que l'implémentation est correcte.
- **Mesurez le travail accepté :** incluez la configuration, l'utilisation des services, les tentatives échouées et les corrections humaines.

## Avant de commencer

**Prérequis :** une installation Claude Code fonctionnelle, un projet ou une branche jetable et l'autorisation d'utiliser les services externes sélectionnés. Les exemples CLI supposent un terminal et le gestionnaire de paquets nommé. Les intégrations cloud exigent leurs propres comptes et authentification.

**Temps estimé :** 15 minutes de lecture, puis 30 à 60 minutes pour un essai limité. **Difficulté :** intermédiaire pour la configuration CLI et l'intégration de services. La lecture des compétences d'instruction demande moins de préparation.

**Documentation vérifiée le 10 octobre 2026.** Les commandes et règles d'accès reflètent les sources liées. Revérifiez votre version installée avant de suivre un ancien tutoriel. Cet article traite des extensions utilisées depuis Claude Code et signale les différences entre hôtes lorsque nécessaire.

**Vérifiez par couches après l'installation.** Contrôlez séparément les fichiers, la détection par l'hôte, les dépendances exécutables, les identifiants et une tâche représentative. Un installateur réussi ne prouve pas qu'un navigateur, un serveur MCP, un outil média ou un compte externe fonctionne. Faites le premier test sur des données synthétiques et notez la révision amont.

## Connaître le type d'extension

| Type | Rôle | Exemple |
|---|---|---|
| **Fichier d'instructions** | Définit les attentes persistantes du projet | CLAUDE.md |
| **Compétence** | Fournit une procédure pour une tâche choisie | grill-me |
| **Plugin** | Regroupe des commandes enregistrées et des intégrations | Plugin Codex |
| **CLI** | Exécute des commandes depuis un terminal | Graphify |
| **Serveur MCP** | Expose des outils appelables à un client d'agent | Intégration d'instance n8n |

Le **Model Context Protocol (MCP)** relie une application d'agent aux outils et aux données exposés par un serveur. Une interface de ligne de commande, ou **CLI**, exécute des commandes. Une compétence apprend souvent à l'agent à utiliser l'une ou l'autre interface, mais sa présence ne prouve pas qu'une connexion fonctionne.

**Commencez par la capacité manquante.** Si votre agent possède déjà une recherche dans le dépôt, une nouvelle procédure de recherche doit produire un bénéfice observable. Si l'agent n'accède pas à une plateforme d'automatisation, un simple fichier d'instructions ne fournit pas cet accès authentifié. Le [guide des environnements d'agents](/articles/best-ai-agent-harnesses/) présente le logiciel qui entoure les appels au modèle et l'exécution des outils.

## Choisir votre premier outil

| Problème | Outil | Premier contrôle d'acceptation |
|---|---|---|
| **Exigences ambiguës** | grill-me / grill-with-docs | Décisions explicites et critères d'acceptation |
| **Dérive répétée du périmètre** | CLAUDE.md inspiré de Karpathy | Chaque modification sert le changement demandé |
| **Plan d'implémentation risqué** | Claudex Loop | Constats de revue résolus avec des preuves |
| **Changements de code non revus** | Plugin OpenAI Codex | Constats liés au code et aux cas d'échec |
| **Dépôt inconnu** | Graphify | Relations conformes aux fichiers source |
| **Connaissances dispersées du projet** | claude-obsidian | Les affirmations gardent des liens vers les preuves originales |
| **Synthèse répétée de sources** | notebooklm-py | Réponses citant les sources prévues |
| **Interface confuse** | Impeccable | Les utilisateurs terminent l'interaction prévue |
| **Ressources visuelles manquantes** | Higgsfield | Résultat conforme au brief approuvé |
| **Flux de service répétable** | n8n MCP | L'exécution de test produit le résultat attendu |

**Point de départ recommandé :** choisissez une ligne et enregistrez une tâche de référence avant l'installation. Ajoutez un second outil seulement s'il apporte une contribution distincte et mesurable.

## Clarifier le travail

### grill-me et grill-with-docs

**Les compétences de Matt Pocock** transforment une idée incomplète en décisions. Le [point d'entrée grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) appelle la compétence de questionnement partagée. [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) appelle le questionnement et la modélisation du domaine. La [documentation de la collection](https://github.com/mattpocock/skills) décrit la terminologie partagée et les registres de décisions d'architecture associés à l'entretien.

**Utilisez la variante avec documentation** lorsque les termes métier influencent l'implémentation. Pour un importateur CSV illustratif, tranchez la définition d'un client existant : même adresse e-mail, même identifiant externe, ou les deux. Notez la définition choisie avant d'écrire la détection des doublons.

**Gardez l'entretien proportionné.** Une session utile résout une incertitude matérielle. L'entretien ne doit pas demander de répéter des réponses déjà disponibles dans le dépôt. Terminez par un plan, les questions non résolues et des contrôles de fin observables.

### CLAUDE.md inspiré de Karpathy

**Les directives maintenues par Multica** traduisent les observations de Karpathy en quatre thèmes : hypothèses explicites, solutions simples, changements ciblés et objectifs vérifiables. Le [dépôt](https://github.com/multica-ai/andrej-karpathy-skills) est une implémentation communautaire inspirée de ses observations. Présenter le projet comme un plugin personnel maintenu par Karpathy serait inexact.

**Intégrez les conseils utiles dans la politique existante du projet.** Conservez les commandes de build, les conventions de contenu et les restrictions de déploiement. Un fichier d'instructions de remplacement qui supprime ces détails crée de nouvelles sources d'erreurs.

**Exemple de règle de projet :** exiger qu'une modification de l'importateur conserve la gestion existante des doublons et explique toute modification volontaire avec un fixture. Cette règle transforme une préférence générale pour la prudence en un contrôle compréhensible par un réviseur. Les instructions expriment des attentes. Les tests et les contrôles d'exécution fournissent des preuves distinctes.

| Élément de planification | But |
|---|---|
| **Exigence** | Nomme le résultat visible par l'utilisateur |
| **Entrée de glossaire** | Donne un seul sens à un terme ambigu |
| **Registre de décision** | Conserve la raison d'un choix important |
| **Contrôle d'acceptation** | Établit comment évaluer la fin |

## Revoir les plans et le code

### grill-me-codex, désormais Claudex Loop

**Claudex Loop** est la destination actuelle du dépôt grill-me-codex original. Sa [documentation](https://github.com/chaseai-yt/claudex-loop) décrit la reconnaissance du dépôt, les exigences, la revue par l'autre fournisseur, l'implémentation et l'inspection indépendante. La boucle complète exige les deux CLI et Python 3.10 ou une version ultérieure.

**Utilisez Claudex Loop pour les plans lourds de conséquences** dont les hypothèses méritent une contestation avant l'implémentation. Le flux actuel accepte un démarrage depuis Claude Code ou Codex. Il enregistre les constats et leurs décisions, puis distingue l'autorisation de revoir de l'autorisation de construire. L'ancienne description vidéo en cinq tours ne remplace pas le budget actuel du flux installé.

**Demandez une preuve pour chaque objection.** Pour l'importateur CSV, la revue doit identifier un doublon concret ou un cas de nouvelle tentative et son comportement attendu. L'accord des modèles est un résultat de revue, pas une preuve. Conservez les constats non résolus lorsque le budget de revue se termine.

### Plugin OpenAI Codex

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**Le plugin Codex d'OpenAI pour Claude Code** ajoute la revue de code et la délégation de tâches dans Claude Code. Ce sont des commandes Claude Code, pas des commandes shell. Le [dépôt officiel](https://github.com/openai/codex-plugin-cc) documente Node.js 18.18 ou une version ultérieure et un accès Codex authentifié via ChatGPT ou une clé API OpenAI.

```text
/codex:review --background
/codex:status
/codex:result
```

**Utilisez la revue ordinaire** pour les changements actuels ou une comparaison de branche. Utilisez **`/codex:adversarial-review`** pour une contestation ciblée. Les commandes de délégation comme **`/codex:rescue`** ont un rôle différent d'une revue en lecture seule. Précisez donc l'autorité visée.

**Budgétez séparément l'utilisation de Codex.** Le projet cite ChatGPT Free parmi les comptes pris en charge, mais des limites d'utilisation s'appliquent. Installer le plugin ne crée pas un accès illimité.

**Règle de sélection :** utilisez une revue bornée du plugin pour un patch existant. Choisissez la boucle plus large lorsque les exigences et la révision du plan ont besoin de leur propre processus enregistré.

## Préserver le contexte utile

### Graphify

```bash
uv tool install graphifyy
graphify install --project
graphify extract . --code-only
graphify query "show the authentication flow"
```

**Graphify** cartographie les relations d'un dépôt dans un graphe de connaissances interrogeable. Son [dépôt canonique](https://github.com/Graphify-Labs/graphify) se trouve désormais sous Graphify-Labs. Le nom du paquet est **`graphifyy`**, avec deux lettres y finales. L'exécutable reste **`graphify`**.

**L'extraction limitée au code** utilise l'analyse syntaxique abstraite locale, qui lit la structure du code. L'interprétation des documents et des médias utilise un chemin séparé fondé sur un modèle. N'étendez pas l'affirmation de confidentialité ou de coût local à tous les modes.

**Les hooks optionnels** reconstruisent le graphe après les commits et les changements de branche. Après un pull ou une fusion, le flux documenté appelle **`graphify update .`**. Les changements de documentation demandent aussi une actualisation. L'export Obsidian offre une autre vue du graphe.

**Utilisez Graphify pour les questions de relations**, puis inspectez la source concernée. Un graphe aide à sélectionner les fichiers. La structure du graphe ne prouve pas le comportement à l'exécution et ne remplace pas les tests. Mesurez les économies de tokens selon vos propres questions, y compris la construction et la maintenance du graphe.

### claude-obsidian

**claude-obsidian** organise les sources en pages Obsidian liées et citées. Son [dépôt](https://github.com/AgriciDaniel/claude-obsidian) décrit l'ingestion, la récupération, la maintenance des connaissances, la conservation des sources et les traces de soutien ou de contradiction. Le coffre reste composé de fichiers locaux ordinaires.

**Utilisez claude-obsidian pour les connaissances durables du projet :** décisions de conception, documents sources et notes de recherche qui doivent survivre aux conversations individuelles. Le résultat utile est un registre maintenable avec une provenance, c'est-à-dire une origine traçable pour chaque affirmation importante.

**Revoyez le coffre après l'ingestion.** Choisissez quelques affirmations et suivez leurs citations jusqu'aux sources originales. Conservez les preuves contradictoires au lieu de fusionner le désaccord en résumé assuré. Le stockage local ne prouve pas une inférence locale. Vérifiez l'hôte et la configuration du modèle avant de fournir des documents sensibles.

| Système de contexte | Première question utile |
|---|---|
| **Graphify** | Quels composants source sont reliés ? |
| **claude-obsidian** | Quelles preuves conservées soutiennent cette décision ? |
| **notebooklm-py** | Que disent ces sources de recherche sélectionnées ? |

### notebooklm-py

```bash
uv tool install "notebooklm-py[browser]"
notebooklm login
notebooklm auth check --test --json
notebooklm skill install
```

**notebooklm-py** fournit une bibliothèque Python, une CLI et une compétence d'agent pour le service de recherche par notebooks de Google. Le [projet](https://github.com/teng-lin/notebooklm-py) documente l'importation de sources, les questions fondées, les artefacts générés et les téléchargements par lot. L'extra browser prend en charge son flux de connexion interactif.

**Il s'agit d'une intégration non officielle.** La bibliothèque dépend d'interfaces Google non documentées et reste exposée aux ruptures et aux limites de débit. Ne présentez pas la bibliothèque comme une API publique prise en charge par Google.

**Utilisez notebooklm-py pour un corpus de recherche limité**, comme les notes de version et les guides de migration d'une dépendance. Vérifiez les citations contre le texte source avant d'intégrer les résultats à un plan. Protégez l'état d'authentification enregistré comme un élément d'accès au compte.

**La délocalisation de la recherche change le lieu d'exécution du travail.** Elle ne supprime ni les tokens d'orchestration, ni les quotas de service, ni l'effort de revue, ni les obligations de traitement des données. Traitez les économies de tokens comme une mesure à recueillir, pas comme une propriété automatique de l'installation.

## Concevoir et générer des ressources

### Impeccable

```text
/impeccable critique settings
/impeccable audit settings
/impeccable polish settings
```

**Impeccable** fournit un vocabulaire de design pour un travail ciblé sur les interfaces. Sa [documentation](https://github.com/pbakaus/impeccable) couvre la critique, la mise en page, la typographie, les contrôles d'accessibilité, le mouvement et l'itération visuelle dans le navigateur. Les exemples supposent une compétence installée et un projet doté d'une surface de réglages.

**Commencez par un problème d'interaction.** Pour l'importateur, demandez pourquoi les utilisateurs manquent les erreurs de validation ou comprennent mal le choix de gestion des doublons. Examinez les changements proposés avant d'appliquer une passe de finition visuelle. Un espacement agréable ne corrige pas une action ambiguë.

**L'itération en direct** aide à comparer les variantes dans le navigateur. Vérifiez la navigation au clavier, la mise en page mobile, les messages d'erreur et le contraste. Le nombre de commandes change entre les versions. Utilisez donc la liste fournie par votre version installée au lieu de mémoriser le nombre de la vidéo.

### Higgsfield

**L'intégration MCP de Higgsfield** relie les agents à son service de génération d'images et de vidéos. Sa [page d'intégration officielle](https://higgsfield.ai/mcp) répertorie Claude Code et les options de connexion CLI avec des flux créatifs. Utilisez le flux de configuration actuel pour votre compte et votre interface.

**Choisissez Higgsfield lorsque le livrable manquant est un média.** Pour une page produit illustrative, précisez le format, la composition, les contraintes de marque et l'emplacement de la ressource avant de générer des variantes. Gardez le brief visuel séparé de l'implémentation de la page.

**Vérifiez d'abord l'accès au service et la consommation.** Une liste d'intégration ne prouve pas l'accès à chaque modèle, la génération illimitée ou un droit commercial précis. Examinez les conditions du compte et le modèle sélectionné avant de retenir un flux de production.

**Revoyez le fichier final** à sa taille d'affichage prévue. Contrôlez le texte visible, les symboles involontaires, le recadrage et la cohérence avec le produit. Les écrans de terminal et les diagrammes générés ne doivent pas servir de preuve d'un test réussi.

| Livrable de design | Preuve de fin |
|---|---|
| **Révision d'interface** | Les actions requises fonctionnent sur les fenêtres visées |
| **Ressource image** | Les dimensions, le recadrage et le contenu correspondent au brief |
| **Ressource vidéo** | Le rythme, le mouvement et l'export final correspondent au brief |

## Connecter des flux répétables

### n8n MCP

**Le serveur MCP intégré de n8n** expose les opérations de flux aux clients connectés. La [documentation actuelle de connexion](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) couvre les instances Cloud et auto-hébergées. La création et la modification de flux sont documentées à partir de n8n 2.13.0. Cet article parle du serveur n8n lui-même, pas d'un paquet communautaire sans lien portant un nom proche.

**Utilisez l'accès au niveau de l'instance** pour l'intégration décrite ici. Le nœud MCP Server Trigger a une portée différente : les outils exposés par un flux. Comparez la [référence des outils](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) à votre version déployée.

**Activez l'accès volontairement.** Les flux existants exigent une exposition MCP pour un accès complet. Les aperçus de recherche ont une visibilité plus large dans les permissions existantes de l'utilisateur. L'exposition d'un flux n'est pas une liste d'autorisation distincte par client, même si les permissions accordées au client gouvernent aussi les opérations.

**Inspectez le mode d'exécution.** La valeur par défaut documentée de **`execute_workflow`** lance la version de production publiée. Le mode manuel lance la version actuelle non publiée. Vérifiez les entrées et les actions en aval avant l'exécution.

**Premier essai utile :** classez des demandes d'assistance synthétiques et écrivez les résultats dans une destination de test. Confirmez la gestion des champs manquants et des nouvelles tentatives. L'auto-hébergement exige aussi du calcul, de la maintenance et les éventuels services aval payants.

## Effectuer un essai contrôlé

**Exercice illustratif :** ajoutez un importateur CSV à une petite application. L'importateur prévisualise les lignes, signale les champs e-mail invalides et empêche la création de doublons. Aucun enregistrement client ni destination externe active n'est nécessaire.

```yaml
# Evaluation worksheet, not a tool configuration file
task: "add CSV import preview"
inputs:
  - "valid rows"
  - "invalid email field"
  - "repeated customer identifier"
  - "same import submitted twice"
acceptance:
  - "preview creates no records"
  - "invalid rows receive useful messages"
  - "duplicate policy matches the written requirement"
  - "repeat submission creates no extra records"
record:
  - "source revision and selected skill version"
  - "model and service configuration"
  - "elapsed time and billed usage"
  - "failed checks and human corrections"
```

**Établissez d'abord la référence.** Enregistrez la révision de départ et demandez à l'agent de terminer la tâche avec votre flux existant. Exécutez des contrôles d'acceptation indépendants et gardez le résultat. Répétez depuis la même révision de départ avec une extension choisie et les mêmes exigences.

**Faites correspondre l'expérience au problème supposé.** Si la gestion des doublons est souvent mal comprise, testez une compétence d'exigences. Si l'agent ignore un validateur existant, testez la cartographie du dépôt. Si les utilisateurs manquent les erreurs, testez la critique d'interface. Charger les dix outils à la fois empêche d'attribuer une amélioration.

**Raisonnement attendu :** une seconde tentative réussie fournit une preuve utile, mais un seul essai n'établit pas un multiplicateur général de productivité. Des essais répétés aident à séparer la valeur de l'outil de la variabilité du modèle. Comparez les résultats acceptés, y compris votre effort de revue et les tentatives échouées.

| Observation | Interprétation |
|---|---|
| **Réponse plus rapide, tests échoués** | Temps de réponse réduit sans tâche terminée |
| **Exécution plus longue, moins de corrections** | Bénéfice possible sur l'effort total de livraison |
| **Deux réviseurs d'accord** | Accord qui exige une vérification indépendante |
| **Usage d'agent inférieur, nouveaux frais de service** | Coût déplacé entre fournisseurs |

**Créez un registre de décision conservé.** Nommez le problème, l'outil choisi, le bénéfice observé, le problème non résolu et les conditions d'un autre essai. Gardez un outil lorsque sa contribution résiste à ce contrôle. Une grande collection installée n'exige pas un grand flux actif.

## Dépannage

| Symptôme | Contrôle suivant |
|---|---|
| **La compétence existe mais la commande échoue** | Installation de l'exécutable, PATH et fichiers auxiliaires requis |
| **Les noms d'un ancien tutoriel n'ont plus les commandes** | Version installée et instructions amont canoniques |
| **Le graphe ignore les changements récents** | Fraîcheur du graphe et actualisation séparée des documents |
| **Le réviseur répète des objections résolues** | Révision exacte du plan, preuves et budget de revue |
| **L'authentification du notebook échoue** | Diagnostic d'authentification, validité de session et problèmes amont |
| **La connexion n8n n'offre pas les opérations attendues** | Version déployée, réglages d'exposition et permissions accordées |
| **Le design paraît meilleur mais fonctionne moins bien** | Critères d'acceptation initiaux et contrôles d'interaction |

**Contrôlez les couches d'installation dans l'ordre :** fichiers présents, détection par l'hôte, dépendances prêtes, authentification fonctionnelle et tâche représentative vérifiée. Un installateur réussi n'établit qu'une partie de cette chaîne.

**Inspectez les compétences qui se chevauchent avant d'ajouter une autre copie.** Les entretiens d'exigences, les suites de planification, les outils de design et les paquets de revue expriment parfois des valeurs par défaut concurrentes. Sélectionnez une procédure principale pour la tâche, puis ajoutez des outils de soutien pour des contributions nommées. Préservez la politique du dépôt et le périmètre demandé.

## Présentation vidéo

{{< youtube id="IShdbDP4Jgg" enable="true" title="The Top 10 Claude Code Plugins to 10x Your Next Project (June '26)" >}}

**La présentation de Chase AI** présente les dix projets étudiés ici. [Regardez la vidéo originale](https://www.youtube.com/watch?v=IShdbDP4Jgg) pour ses démonstrations. Utilisez la documentation liée des projets pour l'installation et le comportement actuels. Le titre de la vidéo exprime une affirmation promotionnelle, pas un résultat mesuré établi par ce guide.

## Prochaines étapes

**Choisissez un problème récurrent et un test d'acceptation.** Testez l'extension correspondante sur un projet jetable, puis gardez la combinaison minimale qui améliore le résultat. Ajoutez la gestion des connaissances, la génération de médias ou l'automatisation lorsque le travail exige ces sorties.

**Pour des conseils associés**, lisez la [comparaison des agents de programmation CLI](/articles/cli-coding-agents-comparison/) lors du choix de l'agent. Utilisez le [cours sur la collaboration avec l'IA](/ai-collaboration-course-start/) pour travailler concrètement sur les exigences, les preuves et les responsabilités de revue.

{{< centerbutton href="/ai-collaboration-course-start/" >}}
Lire le cours sur la collaboration avec l'IA
{{< /centerbutton >}}

## Références

- [Graphify : graphes de code et installation](https://github.com/Graphify-Labs/graphify)
- [Matt Pocock : collection de compétences](https://github.com/mattpocock/skills)
- [Claudex Loop : projet grill-me-codex actuel](https://github.com/chaseai-yt/claudex-loop)
- [OpenAI : plugin Codex pour Claude Code](https://github.com/openai/codex-plugin-cc)
- [claude-obsidian : gestion des connaissances liée aux sources](https://github.com/AgriciDaniel/claude-obsidian)
- [Multica : directives de programmation inspirées de Karpathy](https://github.com/multica-ai/andrej-karpathy-skills)
- [Impeccable : commandes de design et installation](https://github.com/pbakaus/impeccable)
- [Higgsfield : intégration d'agent](https://higgsfield.ai/mcp)
- [notebooklm-py : bibliothèque, CLI et compétence non officieuses](https://github.com/teng-lin/notebooklm-py)
- [n8n : guide officiel de connexion MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
