---
title: "Récupérer après une dérive d’agent IA et transmettre le travail"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Détectez les sources et adaptateurs de politique obsolètes, reprenez une publication interrompue et vérifiez les transmissions indépendantes entre agents."
genre: ["Intelligence artificielle", "Collaboration d’équipe", "Ingénierie logicielle"]
tags: ["cours de collaboration IA", "dérive des sources", "récupération de publication", "transmission entre agents", "vérification des sources actuelles", "compensation"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration de professionnels qui examinent ensemble un projet dans un espace de travail consacré à la cybersécurité"
coverCaption: ""
---
[Retour au cours sur la collaboration IA](/ai-collaboration-course-start/)

**Vérifiez les écarts avant les tâches et après une publication interrompue.** Comparez les versions des sources, celles des adaptateurs et l’état de livraison dans le dépôt ou le bac à sable de travail. Faites-le après avoir terminé un parcours. Vous éviterez ainsi que d’anciens résumés deviennent la référence actuelle et conserverez un historique de récupération vérifiable.

## Points clés

- **Un écart de source** diffère d’un écart d’adaptateur.
- **Une publication partielle** exige un registre pour chaque système.
- **La récupération** préserve l’historique et les changements examinés.
- **Les transmissions** exigent qu’un autre réviseur lise les sources actuelles de façon indépendante.

## Avant de commencer

**Prérequis :** le [flux GitHub dans le navigateur](/articles/ai-collaboration-github-browser-workflow/) ou le [flux de publication mixte](/articles/ai-collaboration-confluence-jira-publication/). **Durée estimée :** 60 à 90 minutes. **Difficulté :** examen avancé.

**Sécurité :** utilisez uniquement des données synthétiques. Suspendez la publication automatique avant les tests de récupération. Aucun service de suppression en cours d’exécution n’est fourni.

**Résultat pour le lecteur :** terminez avec un inventaire d’état, une décision du propriétaire, une réparation examinée et une transmission qu’un autre réviseur peut reconstituer à partir des sources actuelles. Un exercice terminé ne vaut pas autorisation de publication.

## Classifier les écarts

| Écart | Signal | Responsable de la réparation |
|---|---|---|
| **Exigence** | La source diffère du manifeste | Propriétaire produit |
| **Politique** | L’adaptateur diffère de POL-01 | Propriétaire de la politique |
| **Implémentation** | La configuration contredit l’intention | Mainteneur |
| **Runbook** | Les consignes contredisent le comportement approuvé | Responsable des opérations |
| **Accès** | La lecture d’une source auparavant accessible est refusée | Administrateur, tâche arrêtée |
| **Livraison** | Marquée comme terminée sans registre complet | Responsable de la livraison |

**Le texte le plus récent ne constitue pas forcément une référence approuvée.** Une modification récente non autorisée exige une enquête, pas une adoption automatique. Déterminez le statut et le propriétaire avant de copier des valeurs.

## Effectuer le contrôle préalable

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**Le contributeur effectue le contrôle préalable avant de rédiger. La personne qui publie le répète avant d’écrire.** Conservez la comparaison des versions avec la proposition. Les contrôles hebdomadaires complètent ces lectures, sans les remplacer.

**Exemple d’écart d’adaptateur :** POL-01 passe en version 2 alors que CLAUDE.md indique encore la version 1. Arrêtez-vous, lisez le changement de politique examiné, mettez à jour l’adaptateur par une PR protégée et démarrez une nouvelle session. Modifier uniquement le numéro de version sans charger la politique ne répare pas le contexte.

**Introduire un écart de source dans le laboratoire hors ligne :** extrayez une copie neuve du ZIP fourni dans un répertoire temporaire vide. Depuis sa racine, copiez `baseline/` vers `candidate/`, exécutez `python3 check.py capture --base baseline > candidate/context.json`, puis `python3 check.py validate --base baseline --candidate candidate`. Consignez le premier résultat `PASS`. Ouvrez `baseline/requirement.json` dans un éditeur de texte et remplacez uniquement `"retention_days": 7` par `"retention_days": 8`. Relancez la même commande validate. Le statut de sortie attendu est différent de zéro, avec le message `STALE_CONTEXT: capture the trusted base again`. Consignez les deux sorties et le chemin de la source modifiée. Supprimez cette extraction temporaire après avoir enregistré les preuves privées, puis extrayez une copie neuve pour réinitialiser l’environnement. N’appliquez pas la modification à huit jours au dépôt publié et ne considérez pas une nouvelle capture comme une approbation du propriétaire.

**Introduire un écart d’adaptateur dans le dépôt temporaire :** sur une nouvelle branche de proposition, copiez dans CLAUDE.md le texte approuvé de l’adaptateur POL-01 version 1 et indiquez la version 1. Dans une proposition de politique distincte et examinée, décrivez le passage à la version 2 avec une nouvelle condition d’arrêt précise. Laissez l’adaptateur en version 1. Demandez à un réviseur de comparer les deux éléments et de signaler l’obsolescence de l’adaptateur avant toute fusion ou exécution d’agent. Réinitialisez en fermant les propositions de test ou en mettant à jour l’adaptateur par une PR examinée, puis ouvrez une session neuve et vérifiez les deux versions et la nouvelle condition d’arrêt. Conservez les anciens diff et le diff corrigé. Il s’agit d’un test documentaire, pas d’une simulation de refus de plateforme.

## Récupérer une publication interrompue

1. **Suspendez la publication de PROP-042** et attribuez la responsabilité de la récupération.
2. **Lisez l’état réel** dans tous les systèmes concernés. Distinguez les actions terminées, échouées et non tentées.
3. **Demandez au produit de choisir** entre poursuivre, effectuer un retour arrière examiné ou suspendre.
4. **Préparez une proposition de récupération** fondée sur des versions actuelles et gardant le périmètre et les exceptions inchangés, sauf examen explicite.
5. **Appliquez une étape examinée à la fois**, en enregistrant et en relisant chaque résultat.
6. **Vérifiez l’état final** et les limites restantes avant la reprise du travail normal.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Remplacez les états illustratifs par des révisions et des valeurs observées.** Une ancienne entrée de registre ou une affirmation de l’assistant ne prouve pas une relecture.

| Choix | À utiliser quand | Limite |
|---|---|---|
| **Poursuivre** | L’approbation reste valide et les sources concordent | Une nouvelle vérification est nécessaire |
| **Retour arrière** | Le propriétaire retire le changement ou l’implémentation échoue | Ne récupère pas les données supprimées |
| **Suspendre** | Les preuves ou l’accès manquent | La livraison reste incomplète |

**Choisissez la suspension lorsque des preuves manquent.** Les exercices synthétiques ne justifient aucune écriture à l’aveugle. Nommez le prochain rôle et les preuves manquantes.

**La récupération GitHub** utilise un revert ou une compensation examinés. **La récupération Confluence** compare l’historique et applique une restauration ou une compensation examinée. **La récupération Jira** conserve l’historique de la proposition tout en rouvrant ou en bloquant la livraison. Lisez les révisions obtenues au lieu de supposer que la numérotation de l’historique repart de zéro.

## Vérifier une transmission indépendante

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Ouvrez un autre outil ou une session vierge** avec la carte et la transmission, sans reprendre la conversation précédente. Exigez de nouvelles lectures des sources, un nouveau manifeste et l’identification de l’action en attente. Les preuves issues d’un navigateur manuel restent valides si elles sont désignées comme instantané et vérifiées à nouveau avant l’écriture.

**Transmission négative :** refusez l’accès à REQ-17. Attendez-vous à un blocage explicite, pas à une valeur devinée ou à un extrait privilégié. Rétablissez uniquement l’accès approuvé via l’administration et répétez la vérification.

## Diagnostiquer avant de réparer

**Commencez par un inventaire d’état.** « Les assistants ne sont pas d’accord » décrit un symptôme de réponse, pas le problème de source sous-jacent. Lisez séparément l’exigence mappée, la configuration, le runbook, la politique et l’enregistrement de livraison avant de demander à un assistant de les réparer.

| Observation | Diagnostic | Première action |
|---|---|---|
| **Les deux sources concordent, l’ancienne réponse diffère** | Contexte de réponse périmé | Reconstituer l’état à partir de nouvelles lectures |
| **Exigence trente, configuration sept** | Écart de livraison ou d’implémentation | Examiner le paquet approuvé et le registre |
| **Adaptateur un, politique deux** | Écart de version des instructions | Lire le changement de politique et réparer l’adaptateur |
| **Source auparavant lisible, maintenant refusée** | Changement d’accès | Arrêter la tâche et demander un examen autorisé |
| **Registre complet, runbook sept** | Clôture sans relecture valide | Rouvrir ou bloquer la livraison et enquêter |

**Ne traitez pas chaque écart comme un problème de modèle.** Actualiser une session corrige un contexte conversationnel périmé. Cela ne publie pas un runbook, ne rétablit pas une permission manquante et ne résout pas des décisions contradictoires entre propriétaires. Nommez la personne responsable de la réparation avant de choisir une action dans un outil.

## Parcourir la compensation

**Interruption illustrative :** REQ-17 contient une intention approuvée de trente jours, mais la livraison reste en attente. La configuration et le runbook indiquent toujours sept jours. Le mainteneur signale un échec d’implémentation non résolu. Le produit choisit la restauration plutôt que la poursuite.

1. **Consignez les versions actuelles :** exigence trente, configuration sept, runbook sept, livraison bloquée.
2. **Gelez la proposition en attente :** conservez les examens et les preuves de l’échec de publication.
3. **Préparez une modification compensatoire de l’exigence :** rétablissez sept tout en conservant les exclusions et notes intermédiaires.
4. **Obtenez l’examen du propriétaire :** indiquez la version actuelle de la source et le texte exact de restauration.
5. **Publiez par la voie autorisée :** relisez la version résultante de l’exigence.
6. **Rapprochez le registre :** toutes les valeurs publiées applicables sont à sept, le changement initial n’a pas été livré.

**La compensation n’efface pas l’historique.** Conservez la tentative de passage à trente jours, son échec et la restauration ultérieure comme enregistrements distincts. La source finale indique sept, et l’historique de livraison explique pourquoi la proposition approuvée n’a pas abouti.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**Préservez explicitement toute exception ajoutée par un autre contributeur.** Coller aveuglément le contenu d’une ancienne page risque de supprimer une modification intermédiaire valide. Comparez le texte actuel et le texte visé, puis faites examiner une modification compensatoire minimale par rapport à la version actuelle.

## Tester une nouvelle transmission

**Utilisez une session vierge et un autre réviseur.** Fournissez la carte, le paquet fixé, le registre et la décision de récupération. Ne transmettez pas la conversation précédente. Demandez au destinataire d’indiquer l’intention actuelle, la configuration, les consignes opérationnelles et la prochaine action autorisée.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Raisonnement attendu :** le destinataire vérifie le résultat de la compensation avant de dire que la référence initiale est rétablie. S’il répète seulement « sept jours » à partir de la transmission, l’exigence de lecture indépendante n’a pas été testée. Demandez des preuves issues des sources plutôt qu’un nouveau résumé.

**Inventaire pédagogique terminé, interruption synthétique :**

| Enregistrement | État observé | Preuves à conserver | Prochain propriétaire |
|---|---|---|---|
| REQ-17 | v5 indique trente jours, sauvegardes exclues | Historique de page et nouvelle lecture | Produit |
| Configuration protégée | `main` sur `base-001` indique sept jours | Relecture du commit et événement de fusion refusée | Mainteneur du dépôt |
| RUN-04 | v2 indique toujours sept jours | Nouvelle lecture de page | Opérations |
| PROP-042 | r1 approuvée, livraison bloquée | Examens fixés et registre | Responsable de la livraison |

Remettez cet inventaire à un second lecteur sans l’ancienne conversation. La transmission est réussie uniquement si cette personne retrouve les quatre états, nomme l’exclusion des sauvegardes, identifie `base-001` comme révision protégée actuelle et recommande une étape de récupération examinée par le propriétaire. Un échec de révision, une exception manquante ou une reprise sans fondement entraîne un échec. Consignez les références aux sources du lecteur et toute correction avant une nouvelle écriture.

## Décider de reprendre

| Résultat du contrôle préalable | Décision de reprise |
|---|---|
| **Les sources correspondent à l’approbation fixée** | Continuer l’étape autorisée en attente |
| **La source a changé hors du périmètre examiné** | Arrêter pour comparaison et nouvel examen |
| **L’accès en lecture manque** | Suspendre avec un réviseur d’accès désigné |
| **La politique a changé** | Réparer les adaptateurs et réévaluer l’autorisation de la tâche |
| **Le résultat d’écriture est inconnu** | Lire la destination avant de réessayer |

**Définissez des critères d’acceptation concrets pour la récupération.** Exigez une relecture concordante, un objet d’examen actuel, un registre rapproché et une transmission neuve. Ne clôturez pas la récupération parce que l’assistant affirme que le problème est résolu.

**Contrôle de fin :** fournissez un inventaire d’état observé, la décision du propriétaire, la réparation examinée, la relecture finale et une reconstitution indépendante. Si l’accès empêche la lecture, documentez le blocage. Appliquez cette norme de preuve au projet final.

## Dépannage et retour arrière

**Conflits de revert :** préparez une modification compensatoire selon l’état actuel. **La restauration perd des exceptions :** comparez toute la section pertinente avant d’écrire. **L’ancienne mémoire contrôle la réponse :** repartez des sources approuvées et supprimez le contexte de brouillon périmé.

**Retour arrière de la récupération :** arrêtez-vous au dernier état vérifié et ajoutez une entrée au registre. N’effacez pas les événements d’audit natifs et ne réinitialisez pas de force l’historique protégé. Transmettez au produit les questions d’autorité non résolues.

## Exercice et autoévaluation

**Introduisez des preuves obsolètes, un adaptateur de politique périmé et une publication partielle.** Donnez les enregistrements à un autre réviseur sans commentaire et demandez-lui de nommer le responsable de la réparation.

**Raisonnement attendu :** le produit gère la conciliation des exigences, le propriétaire de la politique l’alignement de l’adaptateur et la coordination de la récupération de livraison la coordination des responsables concernés. « Actualiser le contexte » ne répare pas complètement toutes les situations.

## Références principales

- **Contrôles de récupération du dépôt :** [Branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Historique des pages :** [Documentation Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Inspection des instructions :** [Mémoire de Claude Code](https://code.claude.com/docs/en/memory).

## Étapes suivantes

**Terminez le [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** avec les deux parcours et un second lecteur. Montrez les lectures actuelles des sources, les écarts de version, le propriétaire de la décision, la récupération examinée, la relecture et la reconstitution indépendante.
