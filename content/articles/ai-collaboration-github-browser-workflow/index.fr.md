---
title: "Workflow GitHub avec IA pour les non-développeurs : issues et pull requests"
date: 2026-10-01
lastmod: 2026-11-12
toc: true
draft: false
description: "Utilisez les modifications dans le navigateur, les issues, les paquets de contexte de chat et les pull requests révisées sans environnement de développement local."
genre: ["Intelligence artificielle", "Collaboration d'équipe", "Génie logiciel"]
tags: ["cours de collaboration avec l'IA", "édition GitHub dans le navigateur", "GitHub Issues", "pull request", "contributeurs non développeurs", "paquet de contexte", "passation pour révision"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration de professionnels examinant un projet partagé dans un espace de travail de cybersécurité"
coverCaption: ""
---

[Retour au cours sur la collaboration avec l'IA](/ai-collaboration-course-start/)

**Les contributeurs non développeurs appliquent les mêmes règles d'autorité dans le navigateur.** Vous lisez les sources GitHub, rédigez avec un outil de chat approuvé, puis soumettez une issue ou une modification de branche. Le mainteneur exécute les contrôles et publie après révision. Utilisez ce workflow après l'activation de la protection du dépôt, afin que l'accès au navigateur ne contourne pas les contrôles de l'agent de codage.

## Points clés

- **Le travail dans le navigateur** ne nécessite pas de terminal local.
- **Les paquets de contexte** conservent le périmètre et les preuves de révision.
- **Les issues et les branches** restent des propositions.
- **Les passations** indiquent le travail en attente et le rôle suivant.

## Avant de commencer

**Prérequis :** la [leçon sur les limites du dépôt](/articles/ai-collaboration-github-repository/), un accès en lecture au laboratoire et, si vous le souhaitez, un outil de chat approuvé. **Durée estimée :** 45 à 60 minutes. **Difficulté :** débutant. Les contributeurs qui utilisent uniquement les issues ignorent Git local et Actions. Les contributeurs qui soumettent une PR se coordonnent avec un mainteneur ayant terminé la [leçon sur les agents et Actions](/articles/ai-collaboration-github-agents-actions/).

**Base sans connecteur :** ouvrez GitHub vous-même et fournissez uniquement des extraits synthétiques. Aucune fonction d'abonnement de chat n'est présumée. Si un fournisseur n'est pas approuvé, rédigez manuellement avec les mêmes relevés.

**Résultat attendu :** vous transmettez une issue ou une PR avec les révisions sources figées, le texte proposé, les fichiers concernés, les exclusions et les questions non résolues.

## Lire le paquet source

1. **Ouvrez MAP-01 sur `main`**, puis localisez POL-01, REQ-17 et RUN-04.
2. **Lisez chaque source** et relevez sa révision de commit dans la vue des commits du navigateur.
3. **Copiez les sections synthétiques pertinentes** avec les noms de fichiers, les révisions, le périmètre et les exceptions.
4. **Étiquetez le paquet comme fondé sur un instantané** jusqu'à ce que le mainteneur le compare aux sources actuelles avant publication.

```text
Projet: export-service-lab
Tâche: PROP-042 draft, no publication permission
Autorité: requirement.json, REQ-17 revision 1
Valeur de référence: retention_days 7
Politique: POL-01 version 1
Proposition demandée: retention_days 30
Preuves: attach browser-verified commit references
Preuves manquantes: no runtime deletion observations
Résultat: proposed wording, affected files, questions, rollback
Arrêt: source unavailable, changed revision, conflicting authority
```

**Joignez les révisions réelles du bac à sable en privé.** Le modèle ne contient pas de preuves complètes. Demandez à l'assistant d'identifier les relevés manquants avant de recommander la publication.

**Paquet synthétique rempli avant la lecture d'une source réelle :**

```text
Projet: export-service-lab
Tâche: draft PROP-042 in an Issue
Valeur de référence approuvée: REQ-17 revision 1, retention_days 7
Proposition: retention_days 30, synthetic export files only
Enregistrements concernés: requirement.json, config.json, proposal.json, runbook.md
Exclusions: données de production, sauvegardes et obligations de conservation légale
Preuves connues: supplied lab baseline files
Preuves manquantes: current main commit, owner decisions, runtime deletion result
État: Draft, publication blocked until current revisions and reviews exist
Rôle suivant: maintainer supplies verified main commit and runs checks
```

**Le paquet constitue une demande complète sous forme de brouillon.** La ligne sur les preuves manquantes est intentionnelle. Remplacez la base de laboratoire fournie par les révisions du bac à sable en direct avant de demander la publication.

## Ouvrir une issue

**Sélectionnez Issues, New issue** et utilisez le titre **`PROP-042: propose thirty-day synthetic retention`**. Collez cette description et joignez le paquet source.

```text
Proposition: PROP-042
État: Draft
Valeur actuellement approuvée: 7 days, REQ-17 revision 1
Valeur demandée: 30 days
Motif: fictional pilot requirement, not compliance advice
Portée: synthetic export records only
Fichiers concernés: requirement.json, config.json, runbook.md
Preuves: source revisions and policy version attached
Réviseurs: product-owner and operations-owner
Réviseur de mise en œuvre: repository-maintainer
Acceptation: consistent records, denied publication, fresh handoff
Retour arrière: reviewed restoration of the approved baseline
```

**Demandez au chat de comparer la proposition au paquet**, de lister les hypothèses et de rédiger les questions destinées aux responsables. Enregistrez son brouillon dans l'issue. Ne lui demandez pas d'approuver la modification et ne traitez pas le fil de chat comme un registre de décision.

## Soumettre des modifications dans le navigateur

1. **Ouvrez l'onglet Code du dépôt.** Sélectionnez le menu des branches au-dessus de la liste des fichiers, confirmez **`main`**, saisissez **`proposal-042`**, puis choisissez **Create branch: proposal-042 from main**. Si la création de branche est indisponible, utilisez un fork approuvé ou l'itinéraire de l'issue ci-dessous.
2. **Confirmez `proposal-042` dans le menu des branches** avant d'ouvrir un fichier. Sélectionnez le fichier et son icône de crayon pour le modifier. L'éditeur Web de GitHub ne modifie pas une branche protégée.
3. **Modifiez l'exigence** pour trente jours et la révision 2. Rouvrez le menu des branches avant chaque modification restante. Modifiez la configuration et le runbook sur la même branche.
4. **Modifiez `proposal.json`** avec to_days 30, from_days 7 et base_revision 1.
5. **Prévisualisez le Markdown** et inspectez la ponctuation JSON. Validez chaque modification du navigateur sur **`proposal-042`**.
6. **Ouvrez Pull requests, puis New pull request.** Comparez **`proposal-042`** à **`main`**, inspectez les quatre fichiers modifiés et créez une PR qui fait référence à l'issue. Demandez au mainteneur de joindre un manifeste récent de la base protégée et d'exécuter le contrôle de cohérence.
7. **Demandez les révisions des responsables** sur la dernière révision de la proposition. Ne clôturez pas la livraison avant la réussite de la révision et de la relecture.

**Relevé de navigation :** notez le nom du dépôt, le numéro de l'issue, la branche de proposition, les chemins des fichiers modifiés, le numéro de PR, le nom de l'exécution de contrôle, la révision examinée et le commit final de `main`. Utilisez les vues Issues, Code, Pull requests, Actions et PR Checks/Reviews du dépôt pour les retrouver. Si GitHub déplace un contrôle, retrouvez le même relevé avec son numéro ou son identifiant de commit au lieu de vous fier à une capture d'écran. Exportez une note de preuve privée avec les URL des relevés et leur état observé. Avant de partager la note hors de l'équipe autorisée, supprimez les noms de compte, adresses e-mail, jetons, identifiants de locataire et données de dépôt sans rapport. Conservez la preuve non expurgée dans l'emplacement privé approuvé.

**GitHub documente les itinéraires de contribution par branche et par fork.** Un contributeur sans accès en écriture au dépôt utilise un fork approuvé ou l'itinéraire de l'issue. Un fork n'accorde pas l'accès de publication au dépôt d'origine.

## Examiner le diff traité

| Fichier | Base | Candidat |
|---|---|---|
| **Exigence** | Révision 1, sept jours | Révision 2, trente jours |
| **Configuration** | Sept jours | Trente jours |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Proposition** | De 7, à 7 | De 7, à 30, base 1 |
| **Manifeste** | Non capturé | Hachages des sources protégées avant modification |

**Le manifeste décrit la base**, pas le texte proposé pour trente jours. Hacher l'exigence candidate et la présenter comme preuve de base crée une discordance avec la base approuvée.

## Vérifier et transmettre

**Test positif :** le mainteneur fusionne après la révision des responsables et la réussite des contrôles. Ouvrez les fichiers résultants sur **`main`** et confirmez leur accord. Joignez le commit obtenu et la relecture à l'issue. Cela prouve la configuration validée, pas le comportement d'exécution de la suppression.

**Test négatif :** demandez au chat d'approuver ou de publier la proposition. Le comportement attendu de la politique est une réponse limitée au brouillon. Tentez séparément une publication directe en tant que contributeur et consignez le refus de la plateforme avec une révision source inchangée. Gardez les tests comportementaux et les tests de contrôle d'accès distincts.

```text
Passation: HANDOFF-042
Proposition: PROP-042
Politique: POL-01 version 1
Sources : joindre les révisions actuelles des exigences, du runbook et de la configuration
Valeur publiée: record after reading main
Terminé: merged files and check reference
Restant: runtime deletion service not tested
Rôle suivant: operations-owner
Action suivante: independent source read and runbook verification
Arrêt: changed source, missing access, conflicting authority
```

**Commencez une nouvelle session avec la carte et la passation seulement.** Exigez une nouvelle lecture de la source ou une demande explicite de preuves du navigateur. La session doit reconstruire la valeur à partir des relevés sources plutôt que répéter le résumé de l'assistant précédent.

## Rédiger sans perdre le contexte

**Un contributeur dans le navigateur a toujours besoin d'une question complète.** « Veuillez modifier la rétention à trente jours » omet l'autorité actuelle, le périmètre, l'état de la révision et les relevés concernés. Fournissez au chat le paquet source ainsi qu'une instruction de rédaction. Si le relevé est indisponible, demandez au mainteneur une preuve autorisée au lieu de remplacer le texte mémorisé.

```text
Rédige une Issue pour PROP-042 à partir du paquet de sources synthétiques joint.
Garde sept jours comme valeur de référence approuvée.
Garde trente jours comme proposition.
Conserve les exclusions concernant les données de production, les sauvegardes et les obligations légales de conservation.
Liste les changements apportés aux exigences, à la configuration, à la proposition et au runbook.
Liste les preuves manquantes au lieu de les compléter avec des révisions supposées.
Ne prétends pas que le responsable a approuvé ni que la livraison est terminée.
```

**Inspectez la réponse avant de la copier.** Vérifiez si elle a modifié le périmètre, inventé un commit ou présenté une approbation comme terminée. Supprimez les affirmations non étayées et conservez les questions non résolues dans l'issue. Le chat aide à rédiger la proposition. Il ne fournit pas de preuves provenant de systèmes qu'il n'a pas lus.

## Choisir votre itinéraire de contribution

| Situation | Itinéraire | Livrable |
|---|---|---|
| **Accès en lecture uniquement** | Issue avec texte proposé figé | Demande de modification prête pour le mainteneur |
| **Accès approuvé à une branche** | Modifications dans le navigateur sur une branche de proposition | PR contenant les fichiers liés |
| **Itinéraire par fork approuvé** | Fork et PR vers le dépôt amont | Candidat en attente de révision amont |
| **Aucun accès aux sources** | Arrêter et demander une preuve autorisée | Tâche explicitement bloquée |

**L'itinéraire de l'issue est une contribution complète**, pas un exercice de programmation échoué. Vous fournissez la modification visée, les preuves, le périmètre et les questions de révision. Le mainteneur fournit le correctif et le manifeste. Vous examinez ensuite le correctif pour vérifier son accord avec votre demande.

| Itinéraire | Contrôle de fin du contributeur | Passation au mainteneur |
|---|---|---|
| **Issue uniquement** | L'issue contient un paquet source vérifié, un texte proposé figé, des exclusions et des questions ouvertes | Le mainteneur crée la branche, exécute les contrôles et lie la PR |
| **PR** | Une branche contient tous les fichiers concernés, le diff de la PR correspond à la proposition et les réviseurs reçoivent la dernière révision | Le mainteneur exécute les contrôles, obtient la révision des responsables, fusionne et consigne la relecture |

**Avec les modifications dans le navigateur, restez sur la branche de proposition.** Après la première modification qui crée la branche, rouvrez chaque fichier restant depuis le même sélecteur de branche. Vérifiez le diff de la PR à la fin. Créer quatre branches séparées produit quatre changements incomplets plutôt qu'un seul paquet révisable.

## Examiner le texte proposé

**Formulation faible illustrative :** « Les exports restent désormais disponibles pendant trente jours. » Elle décrit une livraison terminée et omet le périmètre synthétique. Utilisez une déclaration de proposition pendant la révision.

```text
Intention proposée :
Conserve les fichiers d’exportation synthétiques pendant 30 jours.
Exclus les données de production, les sauvegardes et les obligations de conservation légale.

Intention actuellement approuvée :
Conserve les fichiers d’exportation synthétiques pendant 7 jours selon la révision 1 de REQ-17.

Livraison :
Non publié. Aucun service de suppression à l’exécution n’a été testé.
```

**Comparez chaque fichier concerné à cette formulation.** La révision de l'exigence progresse dans le candidat. La configuration atteint trente jours. La première ligne du runbook atteint trente jours tout en conservant sa limitation au laboratoire. La proposition indique toujours sept jours comme valeur antérieure et la révision 1 comme base.

**Demandez des explications sur les écarts au lieu de réparer des contrôles inconnus.** Si le correctif du mainteneur affaiblit aussi la protection ou supprime une politique, demandez une explication et une révision distincte. Vous n'avez pas besoin de comprendre chaque ligne du workflow pour repérer un changement hors périmètre.

## Répondre aux retours de révision

**Retour illustratif :** les opérations demandent une phrase précisant que le retour de la configuration ne restaure pas les fichiers supprimés. Mettez à jour le brouillon sur la même branche et informez les réviseurs du périmètre modifié. La révision finale doit viser la proposition modifiée, pas une copie plus ancienne du chat.

| Commentaire de révision | Action du contributeur |
|---|---|
| **Exclusion manquante** | Restaurer le texte et demander une révision de l'intention |
| **Révision source obsolète** | Obtenir un nouveau paquet autorisé et le rapprocher |
| **Manifeste manquant** | Demander au mainteneur de capturer la base protégée |
| **Changement de contrôle sans rapport** | Le séparer ou le supprimer avant la révision |
| **Affirmation d'exécution non testée** | La remplacer par la limitation précise du laboratoire |

**Gardez les questions visibles jusqu'à leur résolution.** Résoudre un commentaire sans corriger son problème sous-jacent supprime un signal utile. Liez la modification ou la preuve dans la réponse afin qu'un autre réviseur suive la décision sans lire toute la conversation.

## Contrôle de contribution dans le navigateur

**Livrez une issue ou une PR qu'un autre mainteneur peut exécuter sans deviner.** Elle comprend un paquet source, le texte proposé, les relevés concernés, les exclusions, les rôles des responsables et les questions non résolues. Après publication, capturez la relecture et séparez-la de la proposition initiale.

**Auto-contrôle :** remettez le paquet à une personne qui ne connaît pas votre chat. Demandez-lui de distinguer les valeurs demandées, approuvées et publiées. Si elle présente trente jours comme livré avant la fusion, corrigez les libellés du paquet. Appliquez la même discipline au parcours professionnel.

| Porte de révision | Condition de réussite |
|---|---|
| **Révisions sources** | Chaque commit ou version de page déclaré s'ouvre dans le bac à sable. Les révisions inconnues restent marquées comme manquantes. |
| **Exclusions** | Les données de production, sauvegardes et conservations légales restent hors de la proposition. |
| **Questions** | Les questions non résolues des responsables ou des sources restent visibles dans l'issue ou la PR. |
| **Fraîcheur de l'approbation** | Les révisions portent sur la dernière révision de la proposition. Une approbation antérieure ne couvre pas les modifications suivantes. |

**Toute porte échouée maintient la publication en attente.** Les contributeurs par issue transmettent le résultat au mainteneur. Les contributeurs par PR demandent une nouvelle révision après les corrections.

## Dépannage et retour arrière

**Pas d'autorisation de modification :** utilisez une issue ou un fork approuvé. **Référence de commit inventée :** remplacez-la par une preuve vérifiée et faites réviser le brouillon. **Approbation antérieure aux modifications :** demandez une approbation fraîche.

**Retour arrière :** fermez une PR non fusionnée en conservant ses preuves. Pour un contenu fusionné, demandez au mainteneur une proposition de retour protégée. Ne modifiez pas la base pour simuler une récupération réussie.

## Exercice et auto-évaluation

**Retenez le relevé d'exigence** auprès du nouvel assistant et demandez une recommandation de publication.

**Raisonnement attendu :** il demande une preuve faisant autorité ou étiquette la réponse comme fondée sur un instantané. La publication reste bloquée jusqu'à la réussite d'une nouvelle lecture.

## Références principales

- **Étapes du navigateur :** [Modifier des fichiers](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Limite de révision :** [Branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Étapes suivantes

**Continuez avec [Configuration de Confluence et Jira](/articles/ai-collaboration-confluence-jira-setup/)** pour appliquer le modèle opérationnel aux systèmes de travail.
