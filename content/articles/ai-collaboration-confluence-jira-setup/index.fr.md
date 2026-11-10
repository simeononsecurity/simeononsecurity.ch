---
title: "Configurer l’IA dans Confluence et Jira : autorisations et responsabilités"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Configurez les pages de référence de Confluence et les autorisations Jira gérées par l’entreprise pour une collaboration interéquipes avec revue."
genre: ["Intelligence artificielle", "Collaboration d’équipe", "Ingénierie logicielle"]
tags: ["cours de collaboration avec l’IA", "Confluence Cloud", "Jira Cloud", "pages de référence", "schéma d’autorisations Jira", "transition de workflow", "tests d’accès"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration de professionnels qui examinent un projet partagé dans un espace de travail de cybersécurité"
coverCaption: ""
---

[Retour au cours de collaboration avec l’IA](/ai-collaboration-course-start/)

**L’administrateur définit les responsabilités au travail avant de connecter les outils de discussion.** Les responsables produit et opérations publient les exigences et les procédures dans Confluence Cloud. Jira Cloud coordonne la livraison. GitHub gère l’implémentation. Créez des environnements de test dédiés après avoir établi les bases, car une autorisation erronée expose des informations indépendamment du comportement du modèle.

## Points clés

- **Confluence** conserve la formulation approuvée des exigences.
- **Jira** gère l’état de livraison, pas la politique de conservation.
- **GitHub** gère la configuration et les politiques partagées.
- **Les tests d’autorisation** nécessitent des offres adaptées et des utilisateurs distincts.

## Avant de commencer

**Prérequis :** les [fondations](/articles/ai-collaboration-pilot-foundation/), le dépôt du laboratoire, l’administration des espaces Confluence et de Jira, ainsi que des utilisateurs distincts pour les rôles de contributeur, responsable et éditeur. **Durée estimée :** 90 à 120 minutes. **Difficulté :** administration avancée.

**Offre requise :** Confluence Free ne prend pas en charge les restrictions de contenu. Jira Free ne propose pas de schémas d’autorisations configurables, de rôles d’espace ni de schémas de sécurité des éléments de travail. Utilisez des environnements de test adaptés avec une offre Standard ou supérieure pour ce parcours. Avant les tests, vérifiez l’offre et les privilèges réels dans les références.

**Note de navigation :** la documentation Jira actuelle emploie « space » et « work item ». Certains tenants conservent « project » et « issue ». Choisissez une configuration gérée par l’entreprise. Cette procédure ne couvre pas le comportement des autorisations gérées par l’équipe. Rovo, les applications Marketplace, les approbations Jira Service Management et un connecteur de discussion payant ne sont pas nécessaires.

**Résultat attendu :** préparez une matrice d’autorisations, des pages de référence nommées, un workflow Jira réservé au laboratoire et des preuves de refus provenant d’utilisateurs distincts. Notez l’offre du tenant et les hypothèses sur les rôles à côté des résultats des tests.

**Vérifications avant de créer des enregistrements :**

| Vérification | Si disponible | Si indisponible |
|---|---|---|
| Restrictions de page et administration d’espace Confluence | Créez des pages approuvées et exclues distinctes | Marquez les tests de modification et de lecture refusée comme Bloqués |
| Schéma d’autorisations et éditeur de workflow Jira gérés par l’entreprise | Copiez un schéma et un workflow réservés au laboratoire | Marquez les tests de transition comme Bloqués |
| Utilisateurs distincts pour les rôles de contributeur, responsable, éditeur et utilisateur exclu | Effectuez des tests positifs et négatifs pour chaque rôle | Marquez les rôles non testés comme Bloqués |
| Responsable du dépôt et branche protégée | Associez le parcours d’implémentation examiné | Terminez d’abord le parcours GitHub-first avant toute publication mixte |

En octobre 2026, utilisez le bouton **Share** ou le contrôle de restriction pour gérer l’accès aux pages, la zone d’autorisations **Space settings** de Confluence pour les droits plus larges et **Settings > Work items > Permission schemes** dans Jira pour le schéma du laboratoire. L’éditeur de workflow de Jira géré par l’entreprise contrôle les transitions. Les libellés de l’interface et les fonctions des offres varient selon le tenant. Avant de suivre ces étapes, consignez le chemin réel et l’offre dans vos preuves. Consultez les [autorisations au niveau des pages Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) et les [schémas d’autorisations Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Créer les pages de référence

1. **Créez un espace Confluence** nommé **`Export Service Lab`**. Désactivez l’accès anonyme et le partage public au moyen des contrôles disponibles pour le site ou l’espace.
2. **Créez des pages publiées**, et non des documents dynamiques, nommées **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** et **`Decision Register`**.
3. En tant que responsable produit, **publiez l’exigence initiale** ci-dessous. Notez l’identifiant et la version réels de la page dans la carte du dépôt.
4. En tant que responsable des opérations, **publiez RUN-04** avec une conservation de sept jours et la mention qu’aucune tâche de suppression ne s’exécute dans ce laboratoire.
5. Sur chaque page de référence, **ouvrez Share**. Définissez un accès général en lecture seule pour les membres admissibles de l’espace et accordez des droits de modification précis aux responsables et éditeurs désignés. Enregistrez et vérifiez avec l’utilisateur contributeur.

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**Appliquez des restrictions à chaque page de référence.** Ne supposez pas qu’une restriction de modification sur une page parente protège ses pages enfants. L’héritage des droits de lecture et de modification diffère, et les autorisations de l’espace restent applicables. Un lien seul n’accorde aucun accès. Vérifiez toutes les appartenances si un utilisateur censé être en lecture seule peut toujours modifier les pages.

**Utilisez ces textes de départ pour les deux autres pages.** Remplacez les champs de revue temporaires par des preuves réelles de l’environnement de test avant d’approuver un enregistrement.

```text
Source ID: RUN-04
Owner role: operations-owner
Status: Approved baseline
Scope: synthetic export files only
Configured retention: 7 days
Procedure: compare REQ-17 with config.json before a reviewed change
Runtime limit: this lab has no deletion job and produces no deletion evidence
Recovery: restore the prior approved configuration through review
Recovery limit: restoring configuration does not restore deleted files
Review evidence: add actual reviewer, page version, and decision reference
```

```text
Page: Decision Register
Entry ID: DEC-12
Decision: use seven days as the synthetic baseline
Scope: export-service-lab only
Requirement: REQ-17 page version, record after publication
Runbook: RUN-04 page version, record after publication
Policy: POL-01 protected GitHub revision, record after review
Product review: pending until the named owner records a decision
Operations review: pending until the named owner records a decision
Status: draft example, replace with observed review evidence
```

## Mettre à jour la carte

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Ajoutez à la carte les emplacements privés réels de l’environnement de test et les identifiants de page.** Le modèle indique la source faisant autorité sans prétendre contenir des adresses actives. Supprimez du README les formulations qui attribuent l’autorité des exigences mixtes au fichier JSON copié.

**Conservez POL-01 dans GitHub** pour les deux parcours. Confluence renvoie à sa révision examinée. Déplacer la source de la politique pendant une tâche exige un nouveau transfert d’autorité examiné.

## Définir les autorisations Jira

1. **Créez un espace de laboratoire géré par l’entreprise** et copiez un schéma d’autorisations dans un schéma réservé au laboratoire. Ne modifiez pas un schéma de production partagé.
2. **Ouvrez Settings, Work items, Permission Schemes**, sélectionnez le schéma du laboratoire et mettez à jour les droits.
3. **Accordez aux contributeurs les droits de consultation, de création et de commentaire.** Limitez les privilèges d’administration. Vérifiez explicitement les droits de modification et **Transition work items**.
4. **Associez le schéma** à l’espace de laboratoire et vérifiez qu’aucun espace de production ne le partage.
5. **Créez PROP-042** comme élément de travail. Notez sa clé générée dans la carte et conservez PROP-042 comme identifiant logique de proposition dans sa description.

**Collez ce brouillon dans PROP-042.** L’élément Jira suit la livraison. Son texte ne remplace pas la formulation approuvée dans Confluence.

```text
Proposal ID: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 page version to record
Proposed value: 30 days for synthetic export files
Exclusions: production data, backups, legal holds
Affected records: REQ-17, RUN-04, config.json, proposal.json
Fixed proposal attachment: pending
Product-owner review: pending
Operations-owner review: pending
Publication ledger: pending
Stop on changed source version, missing review, or denied access
```

| Rôle | Confluence | Jira | GitHub |
|---|---|---|---|
| **Contributeur** | Lit les pages approuvées | Crée des brouillons et les commente | Branche de proposition ou Issue |
| **Responsable produit** | Examine l’exigence | Consigne l’examen de l’exigence | Examine les preuves de la PR |
| **Responsable des opérations** | Examine la procédure | Consigne l’examen opérationnel | Examine l’impact opérationnel |
| **Éditeur** | Modifie les pages approuvées | Consigne l’état de publication | Aucun droit automatique de fusion |
| **Mainteneur** | Lit l’exigence | Consigne l’implémentation | Examine et fusionne la PR protégée |

**Les droits accordés par différents groupes s’additionnent.** Supprimez les droits trop larges non souhaités dans le laboratoire au lieu de supposer qu’un droit restreint les remplace. N’ajoutez pas les identités des connecteurs aux groupes d’administration.

## Définir les états de livraison

**Copiez un workflow géré par l’entreprise** dans un workflow réservé au laboratoire. Ajoutez les états Brouillon, Révision, Approuvé, Publication, Terminé et Bloqué. Ajoutez des transitions pour la soumission, l’approbation, la publication, l’achèvement, le blocage et le retour en révision. Associez-le uniquement au type de travail du laboratoire.

1. **Sélectionnez la transition vers Approuvé** dans l’éditeur de workflow.
2. **Ajoutez une condition ou une restriction** qui limite l’action au rôle ou au groupe désigné de responsable/éditeur. Utilisez les contrôles de condition documentés et publiez le brouillon du workflow en tant qu’administrateur.
3. **Vérifiez manuellement les deux examens des responsables** avant la transition. Chaque examen identifie la proposition figée et les versions des sources.
4. **Limitez Terminé** au rôle responsable de la livraison. Supprimez les transitions alternatives ou globales qui contournent la limite.

**Une transition restreinte n’est pas une approbation à deux personnes.** Elle contrôle l’acteur qui effectue la transition. Dans ce pilote, la vérification des preuves des deux rôles reste une procédure manuelle. Consignez explicitement cette limite.

**Exemple d’enregistrement de transition :** pour **Révision vers Approuvé**, autorisez uniquement le groupe désigné de responsables/éditeurs à effectuer la transition. Avant de l’activer, l’acteur ouvre la pièce jointe figée de PROP-042 et vérifie les décisions du responsable produit et du responsable des opérations sur la même révision de proposition. Si une décision manque ou se rapporte à une ancienne révision, laissez l’élément en Révision et consignez l’écart. La restriction du workflow contrôle l’acteur. La vérification des preuves constitue une étape humaine distincte.

## Vérifier les refus d’accès

**En tant que contributeur**, lisez REQ-17, tentez de le modifier, créez le brouillon Jira et essayez la transition vers Approuvé. Les résultats attendus sont la lecture de l’exigence, le refus de modification, la création réussie de la proposition et le refus d’approbation. Comparez les versions sources avant et après le refus.

**En tant qu’utilisateur exclu**, ouvrez une page synthétique soumise à des restrictions distinctes. L’accès au contenu doit être refusé. Testez séparément les pages enfants. Ne collez pas le texte protégé dans la discussion de l’utilisateur exclu pour contourner le contrôle.

## Adapter la carte du dépôt

**Conservez les identifiants sources lorsque leur emplacement change.** REQ-17 désigne toujours l’intention approuvée de conservation, mais dans le parcours mixte, sa source est une page Confluence. Un instantané du dépôt aide aux contrôles et à la revue. Il ne remplace pas l’autorité de la page.

| Enregistrement | Source faisant autorité | Traitement dans le dépôt |
|---|---|---|
| **REQ-17** | Page d’exigence Confluence associée | Instantané avec preuve de révision de page |
| **RUN-04** | Page de procédure Confluence associée | Extrait opérationnel consigné pour cohérence |
| **POL-01** | Politique protégée dans GitHub | Les instructions partagées des agents y renvoient |
| **Configuration** | Enregistrement protégé dans GitHub | Différence d’implémentation proposée |
| **Livraison** | Élément de travail Jira | Lien de corrélation, pas copie de politique |

**Ajoutez la provenance aux instantanés.** Dans le dossier privé de proposition, consignez l’identifiant source, la référence de page, sa version, l’heure de capture et le rôle de la personne qui l’a capturée. N’incluez pas les identifiants natifs des pages dans les travaux publics du cours. Si l’éditeur trouve une version actuelle différente, réconciliez-les avant d’utiliser l’instantané.

**Ne renommez pas la source d’autorité pour l’adapter à l’outil.** La description Jira modifiable est pratique pour discuter, mais reste un dossier de livraison. Une phrase de trente jours dans Jira ne remplace pas une exigence de sept jours dans Confluence.

## Concevoir les tests d’accès

**Séparez lecture, brouillon et publication.** Un contributeur doit avoir assez d’accès pour comprendre l’exigence synthétique et soumettre une proposition. Il n’a besoin ni de modifier la page de référence ni d’approuver sa propre proposition.

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**Utilisez un enregistrement distinct pour le refus de lecture.** La lecture de l’exigence par le contributeur vérifie la séparation entre publication et modification. L’inaccessibilité de la page pour un utilisateur exclu vérifie la confidentialité. Regrouper les deux dans une ligne masque la limite testée.

**Vérifiez aussi les accès autorisés.** Les responsables et éditeurs doivent pouvoir suivre le parcours prévu. Si chaque utilisateur est refusé, l’environnement de test est restrictif mais inutilisable. Conservez une modification autorisée réussie sur une page de test jetable sans toucher à l’exigence approuvée pendant le diagnostic des autorisations.

## Répéter la revue Jira

**Considérez les noms d’état comme la conception de ce pilote.** Brouillon contient une demande. Révision contient un dossier figé. Approuvé signifie que les responsables ont terminé leur revue. Publication désigne une livraison incomplète. Terminé nécessite une relecture. Bloqué indique l’absence de preuves ou d’accès, ou un conflit non résolu.

| Transition | Dossier requis | Vérification responsable |
|---|---|---|
| **Brouillon vers Révision** | Proposition figée et versions sources | Le contributeur confirme l’exhaustivité |
| **Révision vers Approuvé** | Décisions produit et opérations | L’acteur autorisé vérifie les deux rôles |
| **Approuvé vers Publication** | Comparaison avec les sources actuelles | L’éditeur confirme que les bases n’ont pas changé |
| **Publication vers Terminé** | Registre complété pour chaque système | Le responsable de livraison vérifie la relecture |
| **Toute étape prise en charge vers Bloqué** | Échec et action en attente | Responsable de reprise désigné |

**Répétez l’exercice avec un dossier synthétique incomplet.** Soumettez uniquement une revue produit et demandez à l’acteur autorisé d’évaluer la transition. Le résultat attendu est de laisser le travail en Révision et de demander la revue des opérations. Cela teste la revue procédurale séparément du refus de la plateforme pour le contributeur.

**Testez volontairement les parcours alternatifs.** Dans la vue du workflow de votre environnement, inspectez chaque parcours vers Approuvé et Terminé. Une transition nommée et restreinte ne suffit pas si une autre voie disponible contourne la même limite de revue. Consignez les parcours examinés et l’acteur utilisé au lieu de prétendre à une couverture complète après un clic.

## Diagnostiquer un accès inattendu

**Commencez par l’identité effective.** Vérifiez que la session du navigateur appartient au rôle de test prévu. Examinez ensuite les groupes, les droits de l’espace, l’accès aux pages et l’association du workflow avec les outils d’administration du produit. Ne modifiez pas plusieurs contrôles à la fois, car le refus perdrait sa valeur diagnostique.

1. **Confirmez l’identité :** utilisez des sessions distinctes pour le contributeur, l’éditeur et l’utilisateur exclu.
2. **Trouvez l’autorisation :** identifiez l’appartenance ou le paramètre qui permet l’action tentée.
3. **Ajustez le contrôle du laboratoire :** préservez l’accès légitime des responsables.
4. **Répétez la même tentative :** après le refus, capturez la version source inchangée.
5. **Répétez le cas positif :** confirmez que la publication autorisée fonctionne toujours.

**Liste finale des preuves :** consignez l’arborescence Confluence et les ID des pages associées, l’association du schéma Jira de laboratoire, celle du workflow, les appartenances de chaque rôle testé aux groupes, une lecture autorisée de l’exigence, une modification refusée avec version inchangée, la création autorisée d’un brouillon, une transition vers Approuvé refusée sans changement d’état, une lecture refusée pour l’utilisateur exclu et le responsable du nettoyage. Pour chaque ligne, gardez le rôle de l’acteur, la version ou l’état initial et final, le résultat natif et le réviseur indépendant. Notez le chemin de navigation observé dans le tenant, car les libellés et contrôles disponibles varient selon l’offre.

**Vérification finale :** fournissez les pages de référence associées, le workflow réservé au laboratoire, la matrice des rôles prévue et les enregistrements d’autorisations observés. Si l’offre ne dispose pas d’un contrôle requis, marquez la ligne correspondante Bloqué. La leçon de publication suppose la réussite des tests, et pas seulement l’existence de captures d’écran des paramètres.

## Dépannage et retour arrière

**Le contributeur peut toujours modifier :** vérifiez l’accès à la page, les droits de l’espace et les appartenances. **La transition réussit encore :** vérifiez l’association du workflow et les voies de contournement. **Paramètres absents :** vérifiez le type de gestion, l’édition et les privilèges d’administration.

**Retour arrière :** supprimez les droits des connecteurs et archivez les brouillons. Détachez les schémas et workflows du laboratoire après avoir conservé les preuves. Rétablissez le texte approuvé de la page à partir de l’historique examiné ou d’une correction compensatoire. Ne supprimez pas les preuves d’audit.

## Exercice et autoévaluation

**Jira indique trente jours tandis que REQ-17 en indique sept.** Identifiez l’entrée de l’implémentation et le responsable de la réconciliation.

**Raisonnement attendu :** Confluence définit l’intention. Jira contient une erreur de proposition ou de livraison. Arrêtez la publication et demandez au responsable produit de réconcilier les valeurs au lieu de choisir l’horodatage le plus récent.

## Références principales

- **Restrictions et offre :** [autorisations Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Contrôles de partage :** [accès à un contenu spécifique](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Administration des schémas :** [schémas d’autorisations Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Conditions de transition :** [workflows avancés](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Étapes suivantes

**Après la réussite des tests d’accès, poursuivez avec [Publication intersystèmes](/articles/ai-collaboration-confluence-jira-publication/)**.
