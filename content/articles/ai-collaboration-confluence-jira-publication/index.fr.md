---
title: "Processus de publication IA pour GitHub, Confluence et Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Publiez une proposition fixe de durée de conservation dans Confluence, GitHub et Jira, avec contrôle des versions et reprise après publication partielle."
genre: ["Intelligence artificielle", "Collaboration d'équipe", "Génie logiciel"]
tags: ["cours de collaboration IA", "Confluence Cloud", "Jira Cloud", "publication intersystème", "contrôle des versions", "journal de publication", "publication partielle"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration de professionnels qui examinent ensemble un projet dans un espace de travail dédié à la cybersécurité"
coverCaption: ""
---

[Retour au cours sur la collaboration IA](/ai-collaboration-course-start/)

**Le contributeur fige PROP-042 avant son approbation par les responsables.** Un responsable de publication dans Confluence met à jour les exigences, un mainteneur GitHub fusionne l'implémentation et l'équipe des opérations publie le runbook. Jira consigne chaque étape. Procédez après avoir vérifié les autorisations, car ces trois systèmes ne forment pas une transaction atomique. Le journal de publication rend les livraisons incomplètes visibles.

## Points clés

- **L'intention approuvée** diffère du comportement livré.
- **Les révisions fixes de la proposition** lient la revue à une version.
- **Les journaux de publication** révèlent les étapes incomplètes.
- **De nouvelles lectures des sources** protègent contre les bases modifiées.

## Avant de commencer

**Prérequis :** la [configuration du poste de travail](/articles/ai-collaboration-confluence-jira-setup/), l'accès à la publication, des responsables et un mainteneur du dépôt. **Durée estimée :** deux heures. **Difficulté :** coordination avancée.

**Interface de base :** lecture dans le navigateur, rédaction facultative dans un chat approuvé et publication par une personne. Aucun abonnement à un connecteur n'est présumé. Avant d'ajouter une intégration, vérifiez sa disponibilité dans le tenant, ses périmètres, le traitement du fournisseur et la correspondance des identités. Ne partagez jamais les identifiants d'un responsable avec un contributeur.

**Résultat attendu :** vous terminerez avec une proposition figée, un journal de publication par système, des preuves de relecture et une décision de reprise après la première étape incomplète. L'exercice vérifie la procédure et la gestion des preuves, pas le comportement de conservation en production.

## Consigner les sources actuelles

1. **Lisez MAP-01**, puis ouvrez REQ-17 et RUN-04 à l'aide des identifiants de page associés.
2. **Ouvrez le menu de la page et son historique (Page History)**, puis consignez les numéros de version, le statut, le texte, le responsable et les exceptions.
3. **Lisez l'élément Jira** et joignez un export figé de la proposition ou un commit GitHub. La clé seule ne fige pas les preuves de revue.
4. **Lisez POL-01 approuvée** et la configuration de référence protégée.
5. **Fournissez au chat uniquement les extraits synthétiques nécessaires**, marquez-les comme instantanés et désactivez les actions d'écriture.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Les dossiers hors ligne restent des instantanés.** Le responsable de publication relit les données actuelles avant toute écriture. Un refus d'accès bloque la publication. Un ancien export ne remplace pas une autorisation actuelle.

## Figer la proposition

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Remplacez les versions de page illustratives par les versions réellement relevées.** Joignez le JSON figé et le texte proposé à Jira. Chaque responsable consigne son rôle, sa décision, la révision de la proposition, les versions des sources et l'heure de la revue. Toute modification importante renvoie le dossier à `Review`.

**L'équipe produit examine l'intention et le périmètre. L'équipe des opérations examine le nettoyage et la reprise.** Le mainteneur examine le diff. Les réactions à des messages de chat modifiables ne constituent pas des approbations liées à une révision.

## Publier et relire

1. **Passez Jira à `Publishing`** après vérification des deux revues des responsables et de l'absence de modification des bases sources.
2. **Publiez REQ-17** avec une durée de trente jours et un champ de livraison en attente. Consignez la version obtenue, le périmètre et les exceptions.
3. **Ouvrez la PR d'implémentation GitHub**, en référence à la version de page approuvée. Passez la configuration à trente jours et joignez un instantané non officiel de l'exigence.
4. **Fusionnez après la revue du dépôt** et relisez **`main`**. Consignez séparément le comportement enregistré dans le dépôt et celui à l'exécution.
5. **Publiez RUN-04**, relisez-le par son ID et consignez sa version. Le responsable de publication met à jour les références de livraison dans l'exigence.
6. **Terminez Jira** uniquement lorsque tous les enregistrements concordent et que la preuve de la dernière relecture est jointe.

**Utilisez le validateur local uniquement pour vérifier la cohérence des instantanés.** Copiez l'exigence Confluence d'avant modification dans le schéma JSON de base du laboratoire, capturez-la et passez la version candidate à trente jours. Incrémentez la révision locale de l'instantané tout en conservant séparément les versions réelles de Confluence dans Jira. Le processus fondé d'abord sur GitHub ne valide pas un Confluence actif. Son statut vert ne vérifie pas une autorité externe.

**Ne déployez pas de suppression dans cet exercice.** Un vrai service nécessite une preuve de déploiement, des données de test contrôlées, un mécanisme de suspension et des tests des limites d'exécution. Une fusion prouve l'état du dépôt, pas le comportement de conservation en production.

## Suivre une publication partielle

| Étape | État initial | Preuve d'achèvement |
|---|---|---|
| **REQ-17** | Pending | Version de page obtenue |
| **Configuration** | Pending | Commit fusionné et revue |
| **RUN-04** | Pending | Version de page obtenue |
| **Clôture Jira** | Pending | Relecture finale et transition |

**Consignez chaque résultat avant de tenter l'étape suivante.** PROP-042 relie les événements des systèmes. Une ligne terminée ne signifie jamais que toute la modification est achevée.

**Exemple d'échec :** Confluence publie trente jours, mais GitHub refuse la fusion. Laissez Jira sur `Blocked` et indiquez que la livraison de l'exigence est en attente. L'équipe produit choisit d'achever la publication ou de revenir à sept jours après revue. Ne faites pas d'une copie de secours dans README l'autorité de l'exigence.

## Gérer les modifications simultanées

**Base du processus dans le navigateur :** désignez une seule personne chargée de la publication pendant la période pilote. Rouvrez l'historique de la page juste avant la modification et après la publication. Si une autre personne modifie la source, arrêtez-vous, comparez et rapprochez les changements, puis demandez une nouvelle approbation. Une publication séquentielle est une procédure, pas une garantie de transaction atomique.

**Extension API :** la documentation Confluence v2 décrit **`GET /wiki/api/v2/pages/{id}?body-format=storage`** et **`PUT /wiki/api/v2/pages/{id}`** avec un objet de version. Une intégration de publication revue compare la version actuelle à la base approuvée, soumet la version suivante et relit le résultat. Ne rafraîchissez jamais automatiquement une version en échec pour réessayer avec un ancien contenu.

**La réussite de l'API ne suffit pas.** Vérifiez le contenu obtenu, l'ID source, le périmètre et la version. Ce cours ne fournit aucun client API doté d'un droit d'écriture. Pour les non-programmeurs, le processus exécutable de base est une publication humaine dans le navigateur.

## Vérifier les cas négatifs

| Injection | Raisonnement attendu |
|---|---|
| **Modifier la source après approbation** | Arrêter et faire approuver la nouvelle version |
| **Retirer le droit de modification au responsable** | Refuser la mise à jour et garder le journal en attente |
| **Régler Jira sur soixante jours** | Arrêter en cas de conflit et conserver Confluence comme référence |
| **Échec de publication du runbook** | Garder la livraison incomplète et attribuer la reprise |

**Consignez les résultats réels de la sandbox** avec le rôle de l'acteur et les révisions avant et après. N'incluez pas le contenu protégé d'une page dans les preuves destinées à un utilisateur dont l'accès a été refusé. Les résultats attendus ne sont pas des résultats mesurés.

## Constituer le dossier de revue

**Figez le contenu, pas seulement l'étiquette de la proposition.** PROP-042 apparaît dans chaque système, mais l'étiquette ne précise pas le corps examiné par le responsable. Réunissez dans un dossier fixe le texte exact de l'exigence, le diff d'implémentation, le texte du runbook, les versions sources et l'ordre de publication.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Le dossier doit rester lisible par les deux responsables.** L'équipe produit a besoin de connaître l'intention et les exclusions. L'équipe des opérations a besoin de comprendre la modification opérationnelle et la limite de reprise. Toutes deux doivent comprendre la période où l'intention approuvée diffère de la configuration livrée. Un simple diff de code ne suffit pas à un responsable qui ne connaît pas les fichiers du dépôt.

**Contenu rempli du dossier pour cet exemple synthétique :**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Ces chaînes sont des exemples de proposition, pas des enregistrements issus d'un tenant actif. Joignez le commit de base et les versions de pages réels avant la revue. Le dossier fixe doit contenir les corps proposés complets, pas un résumé qui obligerait le responsable à déduire le texte.

**Séparez l'instantané hors ligne de la publication en direct.** Un contrôle de cohérence montre l'accord entre les enregistrements capturés. Juste avant la première écriture, la personne chargée de publier revérifie les pages associées et le mainteneur revérifie la base protégée. Si l'une d'elles a changé, l'ancien dossier s'arrête à `Review`.

## Parcourir le journal

**Progression illustrative des états :** le tableau utilise des versions pédagogiques, pas des observations. Après chaque écriture dans la sandbox, saisissez les versions et commits réellement obtenus.

| Étape | État après une relecture réussie | Travail restant |
|---|---|---|
| **Revue des responsables terminée** | Dossier approuvé, toutes les valeurs publiées sont à sept | Toutes les étapes de publication |
| **REQ-17 publié** | Intention à trente, livraison en attente | Configuration et runbook |
| **Fusion GitHub relue** | Intention/configuration à trente, runbook à sept | Runbook et rapprochement final |
| **RUN-04 publié** | Tous les enregistrements applicables sont à trente | Relecture finale indépendante |
| **Livraison clôturée** | Journal complet avec preuves | Les lacunes d'exécution consignées restent présentes |

**La livraison en attente est un état utile.** Elle évite de décrire l'ancienne implémentation comme conforme à la nouvelle intention alors que la publication est incomplète. Pendant cette période, les lecteurs ont besoin des deux valeurs, pas d'un résumé affirmant que la conservation est de trente jours.

**Ajoutez les tentatives échouées comme événements distincts.** Si l'écriture du runbook échoue, conservez les résultats réussis de l'exigence et de la configuration. Consignez la tentative d'écriture du runbook, l'échec, la version inchangée, le rôle attribué et l'action suivante. Ne remettez pas les lignes terminées à `Pending` et n'effacez pas la séquence observée.

**Exemple de rejet d'une version obsolète :** le responsable lit REQ-17 v4, un autre éditeur autorisé publie v5, puis le responsable tente d'appliquer PROP-042 r1 à v4. La plateforme signale un conflit de version, ou la lecture avant écriture détecte v5. Consignez l'acteur `publisher`, la version initiale `v4`, la tentative `PROP-042 r1`, le conflit ou la nouvelle version actuelle détectés, la version finale `v5` inchangée par cette tentative et le responsable attribué `product owner`. Gardez Jira à `Review`. Relisez v5, rapprochez le texte et demandez la revue d'un nouveau dossier fixe avant d'écrire à nouveau. Pour un test en direct, utilisez la réponse réelle de la plateforme et l'historique de page. Cette ligne est un exemple pédagogique.

**Exemple pédagogique terminé, valeurs synthétiques uniquement :**

| Système | Source initiale | Revue fixe | Écriture et relecture | État final |
|---|---|---|---|---|
| Confluence REQ-17 | v4, sept jours | PROP-042 r1, Product a approuvé v4 vers v5 | Le responsable a écrit v5, le reviewer a rouvert v5 | Trente jours, sauvegardes et obligations légales exclues |
| Configuration GitHub | Commit `base-001` sur `main`, sept jours | PROP-042 r1, Operations a approuvé le diff candidat | PR fusionnée en `merge-002`, clone indépendant relu à trente | Trente jours dans la source protégée |
| Confluence RUN-04 | v2, sept jours | PROP-042 r1, Operations a approuvé v2 vers v3 | Le responsable a écrit v3, le reviewer a rouvert v3 | Procédure de trente jours avec retour arrière |
| Jira PROP-042 | In Review | Décisions des deux responsables liées à r1 | Le responsable de livraison a joint les preuves et passé à `Done` | Clôture après les trois relectures |

Les étiquettes ci-dessus sont illustratives et ne constituent pas des preuves de tenant. Votre journal doit contenir les liens natifs vers les versions de page et les ID de commit. Avant de passer Jira à `Done`, joignez la proposition figée, les deux revues de rôle, l'enregistrement de la base source, chaque preuve de lecture après publication, le résultat du test négatif et les limites d'exécution non résolues. S'il manque un élément, laissez la livraison ouverte ou `Blocked`.

**Vérification du dossier :** indiquez Supported ou Blocked pour chacun des cinq contrôles : les révisions sources sont récentes, les deux responsables ont approuvé la même révision fixe, toutes les publications requises correspondent aux relectures, les limites d'exécution restent explicites et l'état de reprise est rapproché. `Done` nécessite cinq contrôles `Supported` et aucune écriture non autorisée.

## Gérer une écriture incertaine

**Un délai d'attente laisse le résultat inconnu.** Il ne prouve ni la réussite ni l'échec. Dans le processus de base du navigateur, rouvrez la source associée et vérifiez son contenu actuel et son historique avant de décider de réessayer.

1. **Mettez l'étape suivante en pause :** gardez la livraison incomplète.
2. **Relisez la destination :** comparez le texte, la version et le périmètre actuels au dossier fixe.
3. **Consignez l'observation :** terminée, inchangée, contradictoire ou inaccessible.
4. **Choisissez la suite :** continuez depuis une étape vérifiée, réessayez une étape autorisée et inchangée, ou faites remonter un conflit.
5. **Conservez l'incertitude :** gardez la tentative échouée ou inconnue avec la relecture ultérieure.

**Ne rejouez pas toute la séquence à l'aveugle.** Répéter une étape déjà terminée ajoute des révisions et risque d'écraser des modifications sans rapport. Reprenez depuis l'état vérifié. Si la source est inaccessible, choisissez `Hold` plutôt que de déduire l'état de l'ancien journal.

## Comparer les décisions de reprise

| Situation | Décision à examiner | Motif |
|---|---|---|
| **Exigence modifiée, fusion refusée** | Continuer ou compenser l'exigence | L'intention et le comportement divergent |
| **Configuration modifiée, runbook refusé** | Terminer le runbook ou revenir sur la configuration | Les instructions opérationnelles sont obsolètes |
| **Un autre responsable modifie le périmètre** | Revenir à `Review` | L'approbation fixe décrit un autre contenu |
| **Résultat d'écriture inconnu** | Relire d'abord la destination | La nouvelle tentative dépend de l'état observé |
| **Le responsable de publication perd l'accès** | Suspendre et demander une administration autorisée | L'ancienne autorisation ne permet pas de nouvelles écritures |

**Décidez en fonction de l'état actuel et du choix du responsable.** Une poursuite nécessite des approbations récentes et des contrôles applicables. Une compensation exige d'évaluer la restauration avec les modifications intervenues. Une reprise est une nouvelle publication, pas une exception privilégiée au processus.

## Vérifier la fin de publication

**Fournissez un dossier qu'un reviewer indépendant peut rapprocher.** Il doit trouver la proposition exacte examinée, ses bases sources, les deux revues de rôle, chaque résultat d'écriture, les valeurs finales et les limites d'exécution restantes. Demandez-lui d'identifier la première étape incomplète après une interruption.

**Raisonnement attendu :** la prochaine action découle des sources actuelles et du journal, pas de la confiance du précédent assistant. Reportez les dernières références associées dans les tests de récupération, où la recherche doit préserver la même distinction entre autorités.

## Dépannage et reprise

**Version modifiée :** comparez l'historique et renouvelez la revue. **La vérification de l'instantané réussit mais le wiki diffère :** récupérez à nouveau les sources Confluence actuelles. **Jira a été clôturé trop tôt :** rouvrez-le par le processus autorisé et consignez les étapes manquantes.

**Reprise :** comparez l'historique des pages et effectuez une restauration ou une modification compensatoire approuvée par le responsable. Consignez la version obtenue au lieu de supposer que la restauration réinitialise la numérotation. Si Product choisit un retour arrière, restaurez la configuration au moyen d'une PR protégée. Les fichiers supprimés ne sont pas couverts par la promesse de retour arrière.

## Exercice et auto-évaluation

**Interrompez le processus après la publication de REQ-17** et ne donnez à une autre personne chargée de publier que la carte et le journal.

**Raisonnement attendu :** elle récupère les sources actuelles, confirme l'approbation fixe et reprend uniquement l'étape en attente autorisée. Les preuves manquantes renvoient le travail à `Review`.

## Références principales

- **Historique et restauration :** [documentation technique Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Opérations API versionnées :** [pages de l'API REST Confluence v2](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Contrôles de workflow :** [workflows avancés Jira](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Sécurité des intégrations :** [bonnes pratiques de sécurité MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Étapes suivantes

**Après une publication revue, continuez avec la [récupération guidée par carte](/articles/ai-collaboration-map-first-retrieval/).**
