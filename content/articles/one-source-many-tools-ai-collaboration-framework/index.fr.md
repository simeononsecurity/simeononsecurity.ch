---
title: "Une source, de nombreux outils : construire un cadre de collaboration IA pour des équipes mixtes"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Construisez un cadre de collaboration IA partagé pour les développeurs et les non-développeurs. Définissez les sources de vérité, suivez les versions du contexte, examinez les changements durables et choisissez une carte de projet, du RAG ou les deux."
genre: ["Intelligence artificielle", "Gestion des connaissances", "Génie logiciel", "Collaboration d'équipe"]
tags: ["cadre de collaboration IA", "équipes mixtes", "source de vérité", "agents IA", "AGENTS.md", "CLAUDE.md", "règles Cline", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "génération augmentée par récupération", "RAG", "Model Context Protocol", "carte de projet", "manifeste de contexte", "gestion des connaissances", "dérive documentaire", "approbation humaine", "registre des décisions", "transfert entre agents", "versionnage des politiques", "worktrees Git", "gates de pull request"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration d'un groupe de professionnels collaborant sur un projet de cybersécurité"
coverCaption: ""
---

**Deux personnes posent la même question à deux outils IA :** combien de temps le service doit-il conserver un export ? Dans cet exemple, l'agent de l'IDE du développeur répond sept jours en lisant un README. L'assistant de discussion du responsable des opérations répond trente jours en lisant une page wiki. Les deux réponses semblent sûres. Chaque outil a lu une copie différente de la vérité.

**Le problème vient de la propriété**, pas de la qualité du prompt. L'exigence du wiki a changé la semaine dernière, mais personne n'a mis à jour le README. Le développeur demande à l'agent de corriger le traitement de rétention. L'agent suit l'ancien document et produit un correctif propre qui rétablit le mauvais comportement. Les réviseurs examinent le code sans voir la version de l'exigence utilisée.

**Donnez un lieu unique à chaque fait.** Faites lire ce lieu par chaque outil et faites repasser tout changement durable par une personne. Le dépôt, le wiki et le tracker gardent des rôles différents. Ils ont besoin d'une autorité explicite, de responsables nommés et d'une procédure commune pour déplacer l'information.

**Ce guide fournit un modèle applicable cette semaine**, avec ou sans génération augmentée par récupération. Commencez par une carte de projet, des instructions versionnées, des registres de preuve et des propositions examinées. Ajoutez une infrastructure de recherche seulement quand le problème de récupération le justifie.

**Votre premier livrable est un registre des sources**, pas un connecteur. Listez chaque type de fait, son emplacement de référence, son responsable, sa révision actuelle et la personne qui approuve les changements.

## Points essentiels

- **Attribuez l'autorité selon le type d'information**, au lieu de tout imposer dans une application.
- **Traitez la mémoire et les index de récupération comme des caches**, jamais comme des sources de politique indépendantes.
- **Joignez les versions des sources aux propositions**, afin que les réviseurs voient les faits utilisés.
- **Faites respecter l'approbation en dehors des prompts**, avec des contrôles d'accès et des gates de revue.
- **Partagez la procédure entre les outils**, tout en adaptant sa présentation à chaque interface.

## Avant de commencer

**Prérequis :** choisissez un projet pilote avec un dépôt, un wiki ou système documentaire, un tracker et des responsables prêts à examiner les changements. Une équipe sans wiki peut utiliser un stockage documentaire versionné. Gardez le même modèle de responsabilité.

**Temps estimé :** prévoyez deux à quatre heures pour la carte et les modèles initiaux, puis une semaine de pilote. **Difficulté :** modérée. Le point difficile est l'accord sur l'autorité, pas l'installation d'un outil IA.

**Périmètre :** il s'agit d'un modèle de fonctionnement proposé. Ses règles d'approbation et ses conventions de nommage sont des recommandations. Elles ne sont pas garanties par Claude Code, Codex, Cline, Cowork, Copilot ou ChatGPT. La table des matières automatique renvoie aux étapes.

## Outils mixtes, contexte séparé

**Les développeurs et les non-développeurs partagent un projet**, mais utilisent des interfaces différentes. Le développeur travaille dans un IDE ou avec un agent de terminal. Le responsable produit utilise un projet de discussion. Le responsable des opérations travaille avec un wiki et un tracker. Choisissez l'interface selon la tâche, jamais selon l'accès aux faits de référence.

**Le contexte désigne le contenu disponible pour la réponse actuelle.** Examinez les fichiers du dépôt, documents importés, historiques de discussion, mémoires enregistrées, résultats de connecteurs et extraits récupérés. Deux sessions disposant de preuves différentes peuvent diverger.

| Échec | Ce que vous observez |
|---|---|
| **Dérive documentaire** | Un README répète une exigence obsolète |
| **Promotion d'un résumé** | Un compte rendu devient une preuve sans sa source |
| **Écritures concurrentes** | Deux agents remplacent la même page depuis des versions différentes |
| **Décisions perdues** | Un accord de réunion n'arrive jamais au registre |
| **Provenance absente** | Une réponse plausible ne cite ni version de page ni commit |

**L'exemple de rétention montre la différence.** Le wiki décrit le comportement approuvé. Le code décrit le comportement implémenté. Aucun des deux ne doit réécrire l'autre en silence. Enregistrez le désaccord et demandez au responsable nommé de décider.

> **Point essentiel :** l'accord sur l'autorité vient avant l'accord sur l'outil IA. Commencez par définir le vocabulaire.

### Encadré : cinq termes communs

| Terme | Signification dans ce cadre |
|---|---|
| **Source** | Enregistrement faisant autorité pour un type d'information |
| **Cache** | Copie dérivée utilisée pour accélérer l'accès |
| **Proposition** | Changement suggéré qui attend l'approbation du responsable |
| **Carte de projet** | Index des emplacements, identifiants et responsables des sources |
| **Manifeste** | Preuves exactes utilisées pour une réponse ou une proposition |

## Donnez un lieu unique aux faits

**Une source signifie une autorité par fait**, pas une base unique pour toute l'organisation. Établissez cette répartition pendant le pilote et remplacez les rôles d'exemple par les responsables réels.

| Type d'information | Système de référence | Responsable | Qui écrit | Comment les agents lisent |
|---|---|---|---|---|
| **Code, tests, configuration, schémas** | Dépôt | Responsable ingénierie | Contributeurs via PR revue | Fichiers d'un commit enregistré |
| **Documentation publiée et ADR** | Dépôt | Responsable technique | Contributeurs via la même PR | Fichiers versionnés |
| **Exigences** | Wiki | Responsable produit | Responsable ou éditeur approuvé | ID et révision de page |
| **Runbooks** | Wiki | Responsable opérations | Éditeur approuvé | ID et révision de page |
| **Politique** | Wiki | Responsable politique | Éditeur approuvé après revue | Page canonique et adaptateur local |
| **Décisions interéquipes** | Registre des décisions wiki | Responsable nommé | Responsable après approbation | ID et statut de décision |
| **Tâches et constats** | Tracker | Responsable de tâche | Personnes ou intake autorisé | Clé et révision du ticket |
| **Discussions, résumés, embeddings** | Cache uniquement | Responsable de session ou d'index | Outils et participants | Référence, puis contrôle de la source |

**Un enregistrement de décision d'architecture (ADR)** reste près du code quand il gouverne l'architecture du dépôt. Une décision interéquipe appartient au registre commun. Reliez les deux quand la décision couvre les deux périmètres.

**Les copies locales de politique restent subordonnées** à la page canonique. Les tests et schémas du dépôt sont des sources dans leur propre périmètre. L'emplacement seul ne définit pas l'autorité. La carte le fait.

**Un cache ne remplace jamais une source.** Si un résumé indique sept jours et l'exigence approuvée trente, utilisez l'exigence. Conservez le résumé contradictoire comme preuve de dérive. Définissez ensuite le chemin d'écriture.

## Le cache descend, la proposition monte

**Les agents récupèrent les preuves dans le contexte de session**, puis rédigent des propositions. Ils n'approuvent pas seuls les faits durables. Modifier une branche ou envoyer un brouillon ne revient pas à publier une politique, fusionner du code ou accepter une décision.

```text
Source -> lecture contrôlée par permissions -> contexte de session
Contexte de session -> proposition + version de base -> revue du responsable
Approbation du responsable -> publication contrôlée -> journal des changements
Version de base modifiée -> réconciliation de la proposition -> nouvelle revue
```

**Joignez la version de base** avant de demander une revue. Le réviseur a besoin de l'ancienne valeur, de la valeur proposée, de la raison, des preuves et des systèmes touchés. L'approbation doit viser une révision précise.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Retain exports for thirty days instead of seven."
evidence:
  - "decision:DEC-12 accepted"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**Les identifiants sont illustratifs.** Stockez une ligne de journal par changement logique approuvé, avec l'ID de proposition, les versions précédente et finale, l'approbateur, l'heure et la référence de fusion ou de publication. Reliez les audits natifs au journal.

**La décision appartient aux personnes.** Un éditeur autorisé ou une automatisation limitée applique la révision approuvée. Limitez les identifiants d'écriture. Les instructions seules ne séparent pas la rédaction de la publication.

## Contexte partagé sans RAG

**Une carte de projet est le premier index de récupération.** Maintenez une page par projet avec les IDs de sources, emplacements du dépôt, clés du tracker, périmètres d'autorité et responsables. Lisez la carte, puis récupérez l'enregistrement par ID. Utilisez la recherche lorsque l'ID est inconnu.

### Encadré : exemple de carte de projet

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Les connecteurs directs réduisent la copie manuelle.** Le Model Context Protocol (MCP) est un protocole d'intégration pour exposer des outils et du contexte aux applications IA. Utilisez les connecteurs approuvés quand ils existent. Une récupération ciblée réduit le bruit, mais ne remplace ni l'autorisation ni le contrôle de fraîcheur.

**La récupération exacte demande peu de préparation.** Elle fournit des preuves citables sans base vectorielle. Elle exige toutefois une carte maintenue. Récupérez la section utile avec ses contraintes voisines.

**Le travail hors ligne utilise des instantanés explicites.** Enregistrez la révision exportée et marquez les réponses comme basées sur un instantané. Ne publiez pas avant le contrôle de la source actuelle.

## Une politique, des adaptateurs différents

**Gardez une politique commune**, puis distribuez de courts adaptateurs propres aux outils. Placez la version approuvée en première ligne de chaque adaptateur. Ajoutez l'ID de source et un instantané local contrôlé.

**Le chargement varie selon l'outil.** Codex découvre les instructions `AGENTS.md`. Claude Code utilise `CLAUDE.md`, les imports et la mémoire du projet. Cline utilise `.clinerules/` et ses contrôles. Vérifiez le comportement installé au lieu de supposer que les noms de fichiers sont identiques.

### Encadré : en-tête AGENTS.md

```markdown
Policy-Version: v3 | Source: wiki:POL-01 | Status: approved

# Project instructions

Read the project map MAP-01 before starting a task.
Load docs/policy-snapshot.md and record its source revision.
Treat chat memory and search excerpts as caches.
Attach source revisions to every factual proposal.
Use one task and one worktree per coding task.
Do not publish policy, approve decisions, or merge your own code.
Stop on unresolved source conflicts or overlapping writes.
Required checks: tests, documentation review, policy freshness.
Owners: engineering maintainer, product owner, policy owner.
```

**Les instructions d'un projet de discussion reçoivent la même procédure.** Un non-développeur reçoit la carte et l'instantané par des importations ou connecteurs approuvés. Sans accès direct, une personne fournit l'export versionné et note la limite.

**Une étiquette de version ne prouve pas l'identité du contenu.** Générez les adaptateurs depuis l'instantané approuvé ou comparez leur partie politique à un condensat. Examinez les exceptions propres à chaque outil et les remplacements locaux.

## Enregistrez un manifeste de contexte

**Un manifeste de contexte explique les preuves de la réponse.** Notez les IDs de pages et révisions, les clés de tickets, les révisions des tickets et le commit complet du dépôt. Ajoutez l'heure de récupération et les sections utilisées.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook not retrieved. No runbook change proposed."
```

**La valeur du commit est synthétique.** Remplacez-la par le commit inspecté dans un vrai manifeste. Une fiche créée avant l'inspection reste une liste de contrôle.

**Les citations servent à contrôler.** Reliez chaque affirmation importante à sa source et à sa section. En cas de désaccord, gardez les deux preuves et signalez l'écart. Ne choisissez pas la révision la plus récente sans vérifier son périmètre et son approbation.

## Contexte partagé avec RAG

**La génération augmentée par récupération (RAG)** fournit des documents récupérés au modèle pendant la production de la réponse. Un index sémantique trouve des passages malgré des formulations différentes. La documentation Microsoft RAG citée dans les références décrit l'ancrage, les contraintes de récupération et les contrôles d'accès.

**Utilisez le RAG pour explorer de grandes collections**, comme les documents anciens, comptes rendus et transcriptions. Étiquetez les classes de documents et leur statut d'approbation. Une transcription est une source de paroles, pas une autorité sur une exigence approuvée.

| Règle d'index | Comportement requis |
|---|---|
| **Ingérer les sources, pas les caches** | Exclure les résumés générés et les copies non suivies |
| **Conserver la provenance** | Stocker l'ID, la révision, la section et le statut de chaque fragment |
| **Actualiser au changement** | Réindexer les modifications et invalider les fragments obsolètes |
| **Respecter les changements d'accès** | Mettre à jour les permissions et retirer le contenu révoqué |
| **Renvoyer les citations** | Exposer les références avec le texte récupéré |
| **Contrôler le document actif** | Récupérer la preuve actuelle avant toute proposition conséquente |

**Un fragment récupéré est un pointeur.** Son texte aide à trouver la preuve. La source active confirme la formulation, les exceptions et l'accès. Si la récupération active échoue, marquez l'instantané et arrêtez l'action durable.

**Les embeddings périmés et le contexte manquant créent deux risques.** Un ancien fragment ignore une révision. Un fragment actuel trompe encore si l'exception se trouve à la section suivante. Conservez les titres et récupérez les contraintes adjacentes.

**La fuite de permissions mérite un test séparé.** Autorisez l'accès avant de renvoyer les fragments au modèle. Filtrez les données sensibles avant l'indexation ou l'appel d'un service d'embedding. Tenez compte des copies dans les journaux, requêtes et traces.

## Choisir une carte, le RAG ou les deux

**Adaptez la récupération à la question.** Un ID connu favorise l'accès direct. Une question ouverte sur des archives dispersées favorise la recherche. Commencez par la carte lorsque la découverte ne pose pas encore un problème mesuré.

### Encadré : RAG ou non ?

```text
Les tâches nomment-elles généralement un projet, une page, un ticket ou un fichier ?
  Oui -> La récupération directe suffit-elle au pilote ?
           Oui -> CARTE SEULE
           Non -> HYBRIDE : carte pour les IDs connus, RAG pour la découverte
  Non -> Les preuves sont-elles dispersées dans une grande collection ?
           Non -> CARTE SEULE, avec recherche native
           Oui -> Le travail est-il exploratoire et en lecture seule ?
                    Oui -> RAG EN PREMIER pour la découverte
                    Non -> HYBRIDE avec contrôle de la source active

Chaque option conserve les responsables, l'autorisation et la provenance.
La découverte par RAG vérifie encore les sources avant toute action durable.
```

**RAG seul décrit une interface de récupération**, pas une permission d'ignorer la gouvernance. Le modèle hybride sépare découverte et vérification. La carte répond « où ». La source répond « quoi ». Récupérez directement `REQ-17` pour l'exemple de rétention, puis cherchez le registre pour les anciennes décisions.

## Informations dans le dépôt

**Les connaissances du dépôt évoluent avec l'implémentation.** Gardez une structure compacte afin que l'agent et le réviseur sachent où chercher.

| Fichier ou répertoire | Responsabilité |
|---|---|
| **`CONTEXT.md`** | Termes du projet et liens vers les sources |
| **`docs/adr/`** | Décisions d'architecture acceptées |
| **`docs/design/`** | Descriptions approuvées du comportement |
| **`docs/plans/`** | Plans d'implémentation proposés avec statut |
| **`AGENTS.md`** | Gates de revue, limites et rôles |
| **`README.md`** | Installation et points d'entrée, sans exigences dupliquées |

**Appliquez la règle de la même PR :** modifiez le code et la documentation touchée ensemble. Si aucune mise à jour n'est nécessaire, inscrivez l'exception dans la PR.

```text
KB-Update: none (reason: internal refactor preserves documented behavior)
```

**Le pipeline fait respecter la déclaration.** Un contrôle obligatoire refuse les changements de comportement sans documentation ou exception. Une revue humaine examine l'exception. Un contrôle de chemin détecte les candidats, mais ne prouve pas la complétude.

**Une gate absente du pipeline n'est pas une gate.** Testez le contrôle avec une PR volontairement incomplète. Utilisez une tâche, une branche et un worktree par travail. Les worktrees réduisent les collisions locales, mais ne règlent pas les écritures concurrentes dans un wiki.

**Ne commitez jamais directement sur la branche par défaut.** Signalez les écarts entre exigence et code dans le tracker. Joignez les sources en conflit et laissez leurs responsables décider.

## Informations hors du dépôt

**Le wiki a besoin d'un standard documentaire.** Chaque page de référence porte son but, son statut, son responsable, sa révision, sa date de revue et ses IDs liés. Placez les propositions dans un espace de brouillons clairement non autoritaire.

**Les mises à jour suivent cinq étapes :**

1. **Relire** la page actuelle et ses contraintes voisines.
2. **Comparer** sa version avec la version de base de la proposition.
3. **Réconcilier** les modifications intermédiaires et renouveler l'approbation.
4. **Écrire** la version approuvée avec une condition sur la version attendue.
5. **Vérifier** la page enregistrée et ajouter la référence du journal.

**Relire ne suffit pas à supprimer les courses.** Utilisez une mise à jour conditionnelle quand le système la propose. Sinon, sérialisez la publication et vérifiez le résultat.

**Les constats du tracker portent des preuves.** Notez l'observation, la commande, le commit inspecté, le comportement attendu, le comportement réel et le critère d'acceptation. Retirez les secrets et les données sensibles.

```text
Finding: retention implementation disagrees with approved requirement
Evidence: REQ-17 v8 and inspected config/retention.yaml
Inspection command: git show HEAD:config/retention.yaml
Commit: full inspected commit ID recorded in the manifest
Acceptance: approved duration matches code, tests, and runbook
Status: awaiting product and engineering owner review
```

**Le registre des décisions sépare les règles du raisonnement.** Enregistrez la question, les options, la recommandation, les compromis, le responsable et l'approbation. Les agents proposent. Les personnes décident.

## Relier les deux systèmes

**La synchronisation après fusion transmet les changements.** Créez une tâche wiki liée au commit fusionné, à l'exigence approuvée et au runbook. Le propriétaire du wiki vérifie et publie. Gardez la tâche ouverte jusqu'à la vérification.

**La fraîcheur des politiques est un audit distinct.** Comparez chaque adaptateur du dépôt et chaque copie d'instructions à la version canonique. L'audit repère la version `v2`, les étiquettes absentes et les divergences de contenu.

| Contrôle | Preuve d'achèvement |
|---|---|
| **Fraîcheur de la politique** | Comparaison de la version canonique et du condensat de l'adaptateur |
| **Réconciliation des exigences** | Révision de l'exigence comparée au code et aux tests |
| **Synchronisation après fusion** | Commit fusionné lié à la révision wiki publiée |
| **Résolution des conflits** | Décision approuvée liée aux deux enregistrements |

**Réconciliez selon un calendrier ou au moment de la PR.** Un audit hebdomadaire convient au pilote. Une PR qui modifie le comportement exige un contrôle des exigences avant fusion. Le changement de trente jours passe par l'approbation produit, la mise à jour du code et des tests, la revue de la PR et la publication du runbook.

## Une procédure pour chaque outil

**Emballez les étapes répétées comme des skills ou des prompts**, avec un ID de procédure versionné. Partagez le contrat, pas un format de fichier supposé universel.

| Procédure | Sortie requise |
|---|---|
| **Démarrer une tâche** | Responsable, périmètre, version de politique, manifeste, réservation d'écriture |
| **Linter la documentation** | Métadonnées absentes, autorité dupliquée, références cassées |
| **Contrôler les connaissances** | Écarts exigence-code avec révisions justificatives |
| **Transférer** | Preuves actuelles, propositions, contrôles terminés, questions ouvertes |

**Les non-développeurs travaillent sans Git.** Ils récupèrent les sources autorisées dans les projets de discussion, remplissent le même modèle de proposition et l'envoient au responsable par une page brouillon ou une tâche.

**Les développeurs utilisent les fichiers du dépôt et les gates de PR.** Ils lient la proposition approuvée, enregistrent les commits inspectés et lancent les contrôles requis. Les deux groupes transmettent la même structure de preuves.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "Attached source IDs, revisions, and inspected commit"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["RUN-04 publication assigned to operations-owner"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**Un transfert reste un cache.** La personne suivante relit les sources et enregistre les nouvelles révisions. Ne prenez pas « terminé » comme preuve sans vérifier l'approbation ou le test lié.

## Garde-fous avant chaque écriture

**Filtrez les données avant leur sortie.** Vérifiez la classification, les permissions, les destinations approuvées, le traitement par le fournisseur de modèle et les journaux. Envoyez le minimum nécessaire. Gardez les enregistrements restreints hors des projets et services d'embedding non autorisés.

**Le texte récupéré est une preuve, pas un canal d'instructions.** Une page wiki qui demande d'ignorer une politique ne change pas son autorité. Séparez les instructions issues du contenu de la politique approuvée.

**Attribuez un responsable actif à chaque page ou fichier.** Enregistrez la réservation, sa portée et son expiration. Relisez avant l'écriture et utilisez les contrôles de version.

| Déclencheur d'arrêt | Réponse requise |
|---|---|
| **Les sources divergent sans responsable** | Suspendre et demander une attribution d'autorité |
| **Une autre tâche réserve la cible** | Négocier la propriété avant de modifier |
| **La version de base a changé** | Réconcilier et demander une nouvelle approbation |
| **Une affirmation importante manque de preuve** | La marquer non vérifiée et demander une source |
| **Le traitement des données reste flou** | Garder le contenu dans son système d'origine |
| **La source active est inaccessible** | Noter les limites de l'instantané et suspendre l'action durable |

**Les prompts ne sont pas des contrôles de sécurité.** Testez le refus de permission, les branches protégées, le rejet d'une base périmée et la propriété des écritures hors du modèle.

## Piloter avant de généraliser

**Commencez par un brouillon.** Pilotez un projet avec un développeur, un non-développeur et des responsables de sources. Posez la même question avec deux outils, puis provoquez un conflit de source. Évaluez les manifestes et propositions, pas seulement la fluidité.

| Mesure | Définition |
|---|---|
| **Taux de citation** | Affirmations importantes soutenues par une source, divisées par les affirmations importantes échantillonnées |
| **Constats de dérive hebdomadaires** | Écarts d'autorité ou de version confirmés par type de source |
| **Délai de proposition** | Temps médian entre une proposition prête et la décision enregistrée |
| **Retouches dues au contexte périmé** | Tâches rouvertes à cause de preuves obsolètes ou non vérifiées |

**Mesurez une base avant de fixer des cibles.** Une hausse des constats la première semaine peut signaler une meilleure détection. Suivez la récurrence et le délai de résolution. Exportez les preuves sensibles avec prudence.

**Livrez un dépôt d'exemple pendant le déploiement.** Ajoutez une carte synthétique, des adaptateurs, des manifestes, des modèles de propositions, des exceptions et des contrôles exécutables. Utilisez des données fictives. Montrez un refus de publication, un rejet de base modifiée, une dérive de version et un transfert réussi.

**Un dépôt de modèles est un livrable de déploiement**, pas un élément fourni par cet article. Généralisez après la revue des résultats par la direction et les responsables des sources.

## Dépanner le contexte partagé

| Symptôme | Première correction |
|---|---|
| **Deux outils répondent différemment** | Comparer les IDs, révisions, périmètres et statuts d'approbation |
| **Les instructions semblent actuelles mais le comportement diverge** | Inspecter les adaptateurs chargés, les options et les remplacements locaux |
| **Le RAG renvoie des exigences anciennes** | Contrôler l'actualisation de l'index et récupérer la page active |
| **Une modification wiki efface une autre modification** | Exiger des écritures conditionnelles ou une publication sérialisée |
| **Les contrôles documentaires acceptent un texte périmé** | Ajouter la revue du responsable et la réconciliation des exigences |
| **Les décisions restent dans la discussion** | Attribuer l'intake des propositions et le responsable du registre |

**Corrigez le chemin des preuves avant de réécrire le prompt.** Rejouez ensuite le cas du pilote et enregistrez le résultat.

## Dix étapes cette semaine

1. **Choisir un projet pilote** et les personnes et outils participants.
2. **Attribuer un lieu et un responsable** à chaque type d'information.
3. **Publier une carte de projet** avec IDs et périmètres d'autorité.
4. **Rédiger une politique commune** et obtenir la revue du responsable.
5. **Versionner chaque adaptateur** sur sa première ligne et vérifier son chargement.
6. **Exiger un manifeste de contexte** pour les réponses et propositions factuelles.
7. **Créer une voie d'intake** avec versions de base et approbateurs nommés.
8. **Appliquer les contrôles d'écriture** et la règle documentaire de la même PR.
9. **Tester dérive, conflit et transfert** avec des enregistrements synthétiques.
10. **Examiner les mesures du pilote** et approuver l'étape suivante.

**Donnez un lieu unique à chaque fait, faites lire ce lieu par chaque outil et faites passer chaque changement durable par une personne.**

## Références et prochaines étapes

**La documentation officielle couvre les composants techniques**, pas les règles organisationnelles de ce cadre. Vérifiez le comportement des outils installés et les permissions des connecteurs pendant le pilote.

- **Instructions Codex :** [Instructions personnalisées avec AGENTS.md](https://developers.openai.com/codex/guides/agents-md), pour la découverte et la vérification des instructions.
- **Instructions Claude Code :** [Comment Claude mémorise votre projet](https://code.claude.com/docs/en/memory), pour les instructions de projet et la mémoire.
- **Instructions Cline :** [Règles](https://docs.cline.bot/customization/cline-rules), pour les règles du workspace et les contrôles d'activation.
- **Conception de la récupération :** [Génération augmentée par récupération dans Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), pour l'ancrage, les contraintes et la sécurité.
- **Sécurité des connecteurs :** [MCP Security Best Practices](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), pour l'autorisation et les risques des connecteurs.
- **Isolation des worktrees :** [Documentation Git worktree](https://git-scm.com/docs/git-worktree), pour les worktrees séparés et l'état partagé du dépôt.

**Pour planifier l'inférence locale**, lisez le [Guide du contexte GPU pour l'IA locale](/articles/local-ai-model-gpu-context-guide/). La capacité matérielle et la gouvernance des sources partagées répondent à des problèmes différents. Une fenêtre de contexte plus grande ne corrige pas une autorité contradictoire.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Lire le Guide du contexte GPU pour l'IA locale
{{< /centerbutton >}}
