---
title: "Projet final de collaboration IA : GitHub, Confluence et Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Livrez une modification synthétique de rétention avec des workflows GitHub-first et Confluence/Jira, des preuves d'échec et une revue indépendante."
genre: ["Intelligence artificielle", "Collaboration d'équipe", "Génie logiciel"]
tags: ["cours de collaboration IA", "proposition de rétention", "revue GitHub", "workflow Confluence Jira", "matrice d'échecs", "acceptation indépendante"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration de professionnels examinant un projet partagé dans un espace de travail de cybersécurité"
coverCaption: ""
---

[Retour au cours de collaboration IA](/ai-collaboration-course-start/)

**Livrez PROP-042 deux fois**, avec GitHub-first puis avec GitHub et Confluence/Jira. Vous contribuez, des responsables distincts révisent, et des éditeurs autorisés appliquent la modification. Utilisez des bacs à sable synthétiques isolés après les leçons précédentes. Le projet final teste toute la procédure, y compris le rejet, la récupération et la passation indépendante, plutôt que la qualité de la prose de l'assistant.

## Points clés

- **Une modification partagée** compare les deux modèles d'autorité.
- **Les tests négatifs** comptent autant que la livraison réussie.
- **Les paquets de preuves** permettent une revue indépendante.
- **La fin du laboratoire** n'autorise pas un déploiement en production.

## Avant de commencer

**Prérequis :** [modules du cours](/ai-collaboration-course-start/) précédents, accès approuvé au bac à sable et réviseurs distincts. **Temps de planification :** huit à douze heures sur plusieurs sessions, plus une revue indépendante. Le temps réel dépend de la configuration des comptes et des réparations. **Difficulté :** avancée.

**Artefacts requis :** charte, carte, politique, adaptateurs, référence, manifeste, proposition corrigée, revues des responsables, registre, dossier de récupération et passation. Des permissions dépendantes du plan manquantes bloquent la fin au lieu de devenir des validations supposées.

**Préparez un répertoire de preuves par piste avant les tests.** Un réviseur doit identifier l'acteur, les révisions sources, l'action tentée, le résultat observé et l'état final sans dépendre d'un résumé de discussion.

## Établir deux références

1. **Créez des exécutions isolées** nommées GitHub-first et Mixed. Gardez les révisions et les revues séparées.
2. **Restaurez la référence de sept jours** avec la procédure approuvée de chaque piste et capturez les révisions obtenues.
3. **Vérifiez les contrôles de refus** avec des comptes de contributeur et d'utilisateur exclu.
4. **Capturez le contexte actuel** et confirmez l'accord entre adaptateur et politique.
5. **Déclarez la portée :** rétention synthétique de l'export pendant trente jours, hors données réelles, sauvegardes et obligations légales de conservation.

**PROP-042 est une étiquette de corrélation, pas une approbation réutilisable.** Chaque exécution a besoin de sa propre révision figée et de ses preuves sources. Incluez les identifiants d'exécution dans les rapports.

## Livrer avec GitHub-first

**Ouvrez l'Issue et la PR candidate** avec les leçons GitHub. Modifiez ensemble l'exigence, la configuration, la proposition et le runbook. Capturez la base protégée, exécutez les contrôles fiables et obtenez les revues produit et opérations sur le commit final.

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**Remplissez les références réelles depuis le bac à sable.** Le plan indique la correspondance attendue, pas des preuves terminées. Le mainteneur ne fusionne qu'après la revue, puis lit indépendamment **`main`**. Fermez l'Issue après avoir lié les enregistrements finaux.

## Livrer la piste Mixed

**Lisez les versions Confluence et figez la proposition Jira.** Obtenez les deux revues des responsables. Publiez l'exigence avec la livraison en attente, fusionnez la configuration, publiez le runbook et relisez tous les systèmes avant de passer à Done.

**Enregistrez chaque publication** avec une version de page, un commit ou une preuve de transition. Les copies d'exigences du dépôt restent des instantanés. Le vérificateur local n'établit pas l'autorité actuelle de Confluence.

| Comparaison | GitHub-first | Environnement de travail mixte |
|---|---|---|
| **Exigence** | Revue du dépôt protégé | Publication revue par le responsable Confluence |
| **Coordination** | Issue/PR | Proposition Jira figée |
| **Unité de publication** | Fusion du dépôt | Écritures de pages séparées et fusion |
| **Fraîcheur** | Commit protégé | Versions de page et commit |
| **Récupération** | Revert ou compensation revue | Compensation guidée par le registre |

**Choisissez un workflow selon les besoins de propriété.** GitHub-first réduit la coordination entre systèmes. La piste Mixed conserve les espaces de travail habituels et ajoute des contrôles de publication et d'accès.

## Exécuter la matrice d'échecs

| Cas | Injection | Preuve observée requise |
|---|---|---|
| **Modification approuvée** | Soumettre une proposition de trente jours revue | Relecture cohérente et revue |
| **Contexte obsolète** | Modifier la source après capture | Rejet, rapprochement, nouvelle approbation |
| **Écriture non autorisée** | Le contributeur publie | Refus et révision inchangée |
| **Conflit** | Jira indique soixante, Confluence sept | Blocage et rapprochement par le responsable |
| **Publication partielle** | Interrompre après une écriture | Registre en attente et récupération |
| **Refus d'accès** | Retirer l'accès de lecture à la tâche | Aucun texte protégé ni publication |
| **Récupération** | Achèvement ou retour approuvé | Nouvelles révisions examinées |
| **Passation** | Une nouvelle session ne reçoit que la carte et le registre | Nouvelle lecture et action suivante correcte |

**Un conflit entre systèmes appartient à Mixed.** Dans GitHub-first, testez une description d'Issue en conflit avec le fichier approuvé. Exécutez les autres cas applicables dans les deux pistes. Un échec du validateur local ne remplace pas une preuve de permission en direct.

| Cas et fichier de preuve | Exécution GitHub-first | Exécution Mixed |
|---|---|---|
| **Modification approuvée** `01-approved-change.md` | PR revue et relecture | Pages revues, fusion et registre |
| **Contexte obsolète** `02-stale-context.md` | Modifier la base protégée après capture | Modifier une page d'autorité après capture |
| **Écriture non autorisée** `03-unauthorized-write.md` | Refus du push direct du contributeur | Refus de modification de page et de transition |
| **Conflit** `04-conflict.md` | L'Issue contredit le fichier approuvé | Le texte Jira contredit Confluence |
| **Publication partielle** `05-partial-publication.md` | S'arrêter avant la fusion ou la relecture | S'arrêter après une écriture de page |
| **Refus d'accès** `06-access-denial.md` | Retenir une source protégée du dépôt | Exclure un utilisateur d'une page restreinte |
| **Récupération** `07-recovery.md` | Retour ou achèvement revu | Compensation guidée par le registre |
| **Passation** `08-handoff.md` | Une nouvelle session lit les fichiers protégés | Une nouvelle session lit les pages et le registre cartographiés |

**Créez chaque fichier avant son test.** Notez le résultat attendu, le résultat observé, le rôle de l'acteur, les révisions initiale et finale, la référence de preuve native et la décision du réviseur. Une invite de route navigateur ne prouve pas le refus d'un push direct. Gardez les deux répertoires de piste séparés.

**Séparez les résultats attendus et observés.** Pour chaque cas, notez l'identifiant d'exécution, le rôle de l'acteur, les révisions initiales, l'action tentée, l'attente, l'observation, les révisions obtenues et la décision du réviseur. Supprimez les identifiants de compte et les identifiants secrets des rapports partagés.

## Évaluer la fin

**La réussite exige une preuve observée pour chaque ligne applicable** et une acceptation indépendante. Les réviseurs inspectent les permissions, la fraîcheur des sources, la revue des rôles, la publication partielle et la reconstruction lors de la passation, ainsi que les journaux de cohérence.

**Échouez immédiatement** en cas de publication non autorisée, de texte refusé transmis au modèle ou de remplacement silencieux d'une base modifiée. Gardez le travail bloqué jusqu'à ce que les contrôles corrigés réussissent un nouveau test. Ne faites pas la moyenne de ces échecs pour obtenir un score favorable.

**Mesurez les cas terminés et bloqués, les propositions obsolètes rejetées, les écritures refusées, les récupérations et le temps de revue.** Les résultats proposés restent attendus jusqu'à leur observation. Les dix tests unitaires fournis couvrent la cohérence, pas la sécurité réelle du locataire.

## Planifier les deux exécutions

**Ne réutilisez pas une approbation entre les pistes.** La valeur demandée est identique, mais les espaces sources, les révisions capturées, les permissions et la séquence de publication diffèrent. Donnez à chaque exécution son propre répertoire de preuves et son dossier de revue.

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**Ces noms sont un exemple d'organisation**, pas des fichiers d'archive fournis. Stockez les preuves réelles en privé dans le bac à sable approuvé. Les travaux partagés doivent utiliser des rôles et des références expurgées, tandis que les réviseurs gardent l'accès aux enregistrements natifs.

**Désignez un observateur des tests avant les échecs.** Le contributeur effectue l'action tentée. L'observateur note l'état initial, le résultat et l'état obtenu. Un réviseur décide ensuite si les preuves soutiennent l'affirmation. Déclarez le chevauchement des rôles au lieu de suggérer une acceptation indépendante.

## Exécuter les échecs isolément

**Réinitialisez à un état vérifié et revu entre les cas.** Injecter une dérive de source, une révocation d'accès et une divergence du runbook ensemble masque le contrôle qui a rejeté la proposition. Un échec par exécution donne au réviseur une raison traçable pour le résultat.

1. **Capturez l'état initial :** révisions sources, configuration, état de livraison et rôle de l'acteur.
2. **Appliquez une injection synthétique :** modifiez une condition pertinente par une route de test autorisée.
3. **Tentez l'action bornée :** validation, lecture, publication ou passation.
4. **Enregistrez l'observation :** sortie réelle et état source obtenu.
5. **Réparez par la revue :** conservez les preuves d'échec avant de restaurer les contrôles.
6. **Répétez le cas positif :** confirmez que le workflow corrigé livre encore le travail autorisé.

**Un échec planifié reste une observation d'échec.** Ne qualifiez pas une publication non autorisée de test réussi simplement parce que vous vouliez sonder le contrôle. Le test a réussi à exposer un défaut, mais la limite de publication a échoué et exige une réparation.

## Interpréter un résultat mixte

**Paquet de preuves illustratif :** les contrôles de cohérence locaux réussissent, les équipes produit et opérations examinent le paquet figé, la publication de l'exigence réussit et l'accès de modification du runbook est refusé. La configuration n'est pas encore fusionnée. Jira reste bloqué.

| Affirmation | Verdict | Motif |
|---|---|---|
| **Les enregistrements candidats concordent** | Étayé par le contrôle local | Les enregistrements fournis ont passé les comparaisons |
| **Les responsables ont accepté l'intention et les opérations** | Exige des revues natives figées | Les seuls rôles ne suffisent pas |
| **La livraison de trente jours est terminée** | Non étayé | Des étapes de publication requises restent en attente |
| **La limite de permission fonctionne pour chaque rôle** | Non étayé | Une action refusée a une portée limitée |
| **Le responsable de récupération doit agir** | Étayé comme prochaine étape | Une livraison partielle exige une décision revue |

**Raisonnement attendu :** gardez l'exécution incomplète, vérifiez les sources actuelles et demandez la décision du responsable approprié. Ne terminez pas en affaiblissant les permissions ou en décrivant le contrôle d'instantané comme une preuve de publication en direct.

## Revoir avec un lecteur indépendant

**Demandez au réviseur de reconstruire les événements**, pas seulement de lire votre conclusion. Il doit trouver la référence approuvée, la proposition figée, les décisions des responsables, les révisions obtenues, les tentatives échouées, la réparation et les lacunes restantes sans votre narration.

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**Notez chaque exigence séparément.** Utilisez Supported, Failed, Blocked ou Not run avec une référence de preuve. Cohérence, approbation, permissions, récupération et passation sont des exigences distinctes. Une collection de tests locaux au vert ne compense pas une limite de publication en direct défaillante.

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported signifie que le réviseur a trouvé une preuve observée pour chaque cas applicable.** Notez Failed pour un échec de contrôle observé, Blocked pour un accès ou contrôle manquant et Not run pour un cas non tenté. Gardez chaque référence native dans son fichier de preuve nommé.

**Porte de réussite du cours :** terminez les pistes GitHub-first et Mixed. Dans chaque piste, les huit cas applicables ci-dessus doivent être Supported. Une limite Failed ou une relecture native manquante bloque la piste. Un plan payant ou une identité de test manquante produit Blocked, jamais une réussite supposée. Une piste terminée donne un résultat partiel documenté, pas la fin du cours.

**Paquet de modèle expurgé, illustratif uniquement :**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

Remplacez chaque référence illustrative par un artefact observé du bac à sable. Répétez le paquet complet pour la piste Mixed avec ses propres versions sources et revues. Le réviseur doit rejeter une approbation GitHub copiée dans le paquet Mixed.

## Écrire une décision bornée

**Une décision utile nomme le prochain pilote**, pas un déploiement sans restriction. Par exemple, choisissez un autre réglage d'export synthétique avec les mêmes rôles et la même route de consultation directe, tout en excluant les données réelles et la publication automatisée.

| Élément de décision | Détail requis |
|---|---|
| **Portée** | Une modification suivante et ses exclusions explicites |
| **Preuves** | Cas étayés et échecs non résolus |
| **Contrôles** | Exigences imposées par la plateforme et exigences procédurales séparées |
| **Responsables** | Rôle responsable de chaque lacune restante |
| **Lacune d'exécution** | Comportement de suppression ou de déploiement non testé |
| **Conditions d'arrêt** | Accès manquant, autorité modifiée, publication non autorisée |

**Contrôle de fin :** les deux paquets résistent à une reconstruction indépendante, les cas d'échec applicables ont des preuves observées et les contrôles non résolus restent visibles. Si seule la piste GitHub est terminée, signalez une fin partielle du cours au lieu de supposer que la piste Mixed se comporterait pareil.

## Dépannage et retour arrière

**Preuves du seul chemin heureux :** relancez les tests de refus et d'interruption. **Rôles qui se chevauchent :** déclarez-les et répétez avec des utilisateurs distincts. **Contrôles du plan absents :** arrêtez et obtenez un bac à sable approuvé.

**Retour arrière :** restaurez la référence avec des PR revues et des modifications Confluence, révoquez les intégrations temporaires, archivez les preuves Jira et effectuez le nettoyage synthétique approuvé par les responsables après la conservation des preuves. Conservez l'historique de récupération.

## Créer la décision de déploiement

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**Raisonnement attendu :** une réussite synthétique justifie un autre pilote borné. La production exige une approbation distincte pour les données réelles, le déploiement, le traitement par le fournisseur et le comportement à l'exécution. Une réponse réussie de l'assistant n'est pas une autorisation de déploiement.

## Références principales

- **Contrôles du dépôt :** [Branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Accès à l'espace de travail :** [Permissions Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Contrôles de livraison :** [Schémas de permissions Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Étapes suivantes

**Retournez au [hub du cours](/ai-collaboration-course-start/)** pour revoir les contrôles manquants. Comparez votre implémentation avec [l'article sur le framework](/articles/one-source-many-tools-ai-collaboration-framework/) avant de choisir un autre pilote.
