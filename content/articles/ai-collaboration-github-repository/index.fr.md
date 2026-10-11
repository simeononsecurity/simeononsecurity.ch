---
title: "Collaboration IA avec GitHub : limites du dépôt et des revues"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Construisez une carte des sources centrée sur GitHub, attribuez la responsabilité des fichiers et définissez une limite de publication protégée pour les contributions IA révisées."
genre: ["Intelligence artificielle", "Collaboration d'équipe", "Génie logiciel"]
tags: ["cours de collaboration IA", "dépôt GitHub", "protection de branche", "CODEOWNERS", "carte des sources", "revue de pull request", "contrôles de publication"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration de professionnels examinant un projet partagé dans un environnement de cybersécurité"
coverCaption: ""
---

[Retour au cours de collaboration IA](/ai-collaboration-course-start/)

**Le mainteneur construit la limite de publication centrée sur GitHub** après l'approbation de la charte. Les exigences, la configuration, la politique et les runbooks vivent dans un dépôt jetable. Les contributeurs proposent leur travail par des Issues et des pull requests. Vous définissez où se trouvent les faits approuvés et bloquez les changements non révisés avant de connecter des agents.

## Points clés

- **`main` protégé** est la limite de publication.
- Les **Issues** recueillent le travail proposé sans approuver la politique.
- **CODEOWNERS** attribue les réviseurs admissibles pour les fichiers.
- Des **utilisateurs distincts** démontrent les contrôles de revue et de refus.

## Avant de commencer

**Prérequis :** la [fondation du pilote](/articles/ai-collaboration-pilot-foundation/), le laboratoire extrait, un administrateur du dépôt et des réviseurs distincts pour le produit et les opérations. **Temps estimé :** 60 minutes. **Difficulté :** modérée.

**Limite du plan :** GitHub documente les branches protégées pour les dépôts publics avec Free et pour les dépôts privés avec Pro, Team ou Enterprise. Utilisez uniquement des dépôts publics pour le contenu synthétique. Vérifiez la visibilité et le plan dans la référence des branches protégées avant de compter sur l'application de la règle.

**Résultat attendu :** vous terminez avec une branche de publication protégée, des propriétaires de fichiers, une carte des sources et un test de refus enregistré comme preuve.

## Créer le dépôt

1. **Créez `export-service-lab`** avec un README et la branche par défaut **`main`**.
2. **Copiez le laboratoire extrait** à la racine du dépôt en conservant **`check.py`**, **`test_check.py`** et **`baseline/`**. Copiez les fichiers d'enregistrement de la base à la racine comme premiers enregistrements.
3. **Créez `docs/project-map.md`** avec le registre de la fondation. Ajoutez **`docs/policy.md`** avec POL-01 approuvée.
4. **Créez `docs/decisions/DEC-12.md`** avec l'approbation de la charte, les rôles, la décision de base et le statut.
5. **Validez l'amorçage** en tant qu'administrateur. Enregistrez cette exception initiale. Activez la protection avant les contributions suivantes.

**Procédure d'amorçage locale pour Git Bash, le Terminal macOS ou un shell Linux :** Connectez-vous à GitHub dans un navigateur, ouvrez le nouveau dépôt, sélectionnez **Code** et copiez son URL de clonage HTTPS. Dans un répertoire de travail jetable, exécutez les commandes ci-dessous. Remplacez les deux chemins factices par l'URL et le chemin de l'archive ZIP du laboratoire téléchargée. Ne placez pas de jeton dans l'URL.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

La commande de clonage doit donner le nom du répertoire du dépôt. Si `unzip` est indisponible, extrayez le ZIP avec votre gestionnaire de fichiers et copiez son contenu dans cette copie de travail en conservant le README du dépôt. Enregistrez `docs/project-map.md`, `docs/policy.md` et `docs/decisions/DEC-12.md` depuis le dossier de fondation avec un éditeur de texte. Exécutez ensuite :

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git doit afficher un nouvel identifiant de commit, puis confirmer la réussite de l'envoi vers `main`. Le statut court final doit être vide. Ouvrez le dépôt GitHub dans une nouvelle vue du navigateur et confirmez que les fichiers et l'identifiant du commit apparaissent sur `main`. Enregistrez l'URL du commit comme preuve d'amorçage. Si Git demande l'identité de l'auteur, suivez le pont de configuration du hub du cours. Si l'authentification échoue, utilisez le flux d'identifiants pris en charge par GitHub, puis réessayez le même envoi. Si la branche ou le dépôt distant est incorrect, arrêtez-vous et examinez `git branch --show-current` et `git remote -v` avant toute autre écriture. Si l'envoi est refusé parce que la protection est déjà activée, ouvrez une branche de proposition et une PR au lieu de contourner la règle. La procédure réservée au navigateur ci-dessous reste disponible pour un mainteneur.

| Enregistrement | Emplacement | Propriétaire |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Responsable de la politique |
| **REQ-17** | `requirement.json` | Responsable produit |
| **RUN-04** | `runbook.md` | Responsable des opérations |
| **Comportement** | `config.json` | Mainteneur |
| **Décisions** | `docs/decisions/` | Responsable du projet |

**La carte relie les emplacements au lieu de copier les valeurs.** Gardez le README centré sur la configuration et la carte. La répétition des exigences de conservation crée une dérive, même dans un seul dépôt.

## Attribuer les propriétaires des fichiers

**Générez `.github/CODEOWNERS`** localement avec les identifiants réels du bac à sable. Saisissez les identifiants sans le **`@`** initial. Gardez les identités des comptes dans votre laboratoire privé, et non dans les preuves publiques de l'exercice.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

Les propriétaires ont besoin d'un accès en écriture pour que GitHub les reconnaisse. Vérifiez les erreurs du fichier CODEOWNERS dans le navigateur. Protégez les fichiers de propriété et les définitions de workflow avec le contenu ordinaire.

**Plusieurs noms sur une ligne n'exigent pas l'approbation de tous les propriétaires listés.** GitHub accepte l'approbation d'un seul propriétaire admissible pour le chemin correspondant. Utilisez des propriétaires désignés distincts pour les chemins des exigences et du runbook. Le pilote exige aussi des attestations du propriétaire produit et du propriétaire opérations liées à la proposition finale.

## Protéger la publication

1. **Ouvrez Settings, Branches** et ajoutez une règle de protection de branche pour **`main`**. Utilisez toujours le parcours de protection de branche au lieu de le mélanger avec les rulesets dans cet exercice.
2. **Exigez une pull request**, deux approbations et une revue des code owners.
3. **Rejetez les approbations obsolètes** après de nouveaux commits et exigez la résolution des conversations.
4. **Activez l'option d'interdiction de contournement des réglages ci-dessus.** Désactivez les push forcés et la suppression.
5. **Ajoutez le contrôle de cohérence** après son premier passage dans le module suivant. Exigez que les branches soient à jour avant la fusion.

**Deux approbations imposent un nombre, pas l'appartenance à un rôle métier.** CODEOWNERS ajoute une couverture par chemin. Le mainteneur vérifie aussi les deux attestations de rôle. Enregistrez explicitement ce contrôle procédural au lieu de le décrire comme une application automatisée de deux rôles.

**Les administrateurs gèrent encore la configuration.** Capturez la règle avant et après les tests. N'accordez pas un accès administrateur à un agent et n'utilisez pas de jeton privilégié pour démontrer le refus du contributeur.

## Vérifier la limite

| Tentative | Résultat attendu |
|---|---|
| **Le contributeur soumet une branche** | Proposition autorisée |
| **Le contributeur publie directement** | Publication protégée refusée |
| **Un réviseur approuve** | Fusion bloquée par le seuil de revue |
| **Un nouveau commit suit la revue** | Nouvelle approbation requise |
| **Un fichier sensible n'a pas de couverture de propriétaire** | Réparer avant publication |

**Utilisez la session navigateur du contributeur pour examiner le parcours.** L'éditeur web de GitHub ne modifie pas une branche **`main`** protégée. Une invite proposant de créer une branche montre le parcours navigateur pris en charge. Elle ne prouve pas que le serveur a rejeté un push direct. Pour obtenir une preuve de refus par la plateforme, demandez à un contributeur disposant d'un accès Git local approuvé d'essayer un push direct inoffensif vers **`main`** protégée et conservez la réponse du serveur. Marquez ce test de refus comme Bloqué lorsque l'accès local est indisponible.

**Lisez `main` après le refus** et confirmez que la révision n'a pas changé. Enregistrez le rôle de l'acteur, l'action tentée, le résultat et la révision source. La promesse d'un assistant de ne pas publier est une preuve comportementale, pas un test des permissions de la plateforme.

**Utilisez le clone local authentifié du contributeur pour le test de push direct.** Un jeton de mainteneur testerait la mauvaise identité. Cette réponse illustrative montre le type de preuve serveur à conserver. La formulation exacte varie selon les règles du dépôt.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Si l'authentification Git locale est indisponible, marquez le refus côté serveur comme Bloqué.** Conservez l'invite de branche du navigateur comme preuve du parcours, puis demandez au mainteneur d'organiser un test séparé avec un contributeur. Ne considérez pas l'invite du parcours comme un push direct rejeté.

## Construire une carte des sources utile

**Une carte des sources est un document de routage**, pas un second document d'exigences. Une personne arrivant depuis une conversation doit trouver l'intention actuelle, le comportement implémenté et les instructions opérationnelles sans choisir entre plusieurs résumés concurrents.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Ne placez pas la valeur actuelle de conservation dans chaque entrée de la carte.** Une carte contenant « sept jours » devient une valeur supplémentaire à synchroniser après PROP-042. Gardez les identifiants stables et les emplacements dans la carte, puis lisez la valeur depuis l'enregistrement faisant autorité.

**Protégez les changements de la carte comme des changements de routage.** Rediriger REQ-17 vers un fichier brouillon modifie la sélection de la source, même si l'exigence approuvée reste intacte. Examinez la destination, le propriétaire et la portée de l'autorité à chaque changement de la carte.

## Séparer la base et la candidate

**La racine du dépôt contient les enregistrements actifs du laboratoire.** Le répertoire **`baseline/`** téléchargé est un support pédagogique. Il ne devient pas automatiquement la base protégée de chaque PR ultérieure. Une fois le travail révisé arrivé sur **`main`**, les enregistrements protégés de la racine définissent la base de la proposition suivante.

| Emplacement | Objectif | Modifier pendant PROP-042 ? |
|---|---|---|
| **Exigence/configuration/runbook racine** | Enregistrements actifs proposés sur la branche | Oui, via des changements révisés |
| **`baseline/`** | Support d'exercice hors ligne d'origine | Non |
| **Espace de travail approuvé détaché** | Enregistrements racine protégés capturés | Non |
| **`context.json`** | Preuve des octets de la base capturée | Régénérer après rapprochement |

**Gardez les changements de contrôle séparés des changements de conservation.** Amorcez d'abord le vérificateur et les règles de revue. Proposez ensuite le changement de sept à trente jours. Mélanger une réécriture de politique, de workflow et de valeur rend plus difficile la distinction entre contrôles réparés et contournés.

## Réviser le changement complet

**Ouvrez Files changed avant d'accepter la description d'une PR.** La description explique l'intention de l'auteur. Le diff révèle le changement soumis. Pour PROP-042, examinez la révision de l'exigence, les exclusions de portée, la configuration, le runbook, la base de la proposition et les preuves du manifeste.

1. **Revue produit :** confirmez l'intention de trente jours et les exclusions inchangées.
2. **Revue opérations :** confirmez que le runbook correspond à la configuration proposée et conserve la limitation d'exécution.
3. **Revue mainteneur :** examinez le JSON, la capture de source, les résultats du contrôle et les changements sans rapport.
4. **Revue des contrôles :** examinez séparément tout changement de carte, de politique, de CODEOWNERS ou de workflow.

**Un contrôle vert n'explique pas une suppression sans rapport.** Si la branche supprime le document de politique tout en modifiant la conservation, demandez une proposition distincte ou une revue par un propriétaire précis. Limiter la portée rend l'objet de la revue compréhensible.

## Diagnostiquer un test de refus

**Utilisez une seule action tentée par ligne de preuve.** « Le contributeur a échoué » est ambigu. L'utilisateur peut ne pas disposer de l'accès ordinaire en écriture, rencontrer une limitation du navigateur ou subir la règle de branche prévue. Ces observations établissent des limites différentes.

| Observation | Interprétation | Suivi |
|---|---|---|
| **Impossible de créer une branche** | L'accès aux contributions est absent | Utiliser une Issue approuvée ou un fork |
| **Branche créée, publication vers main impossible** | Le parcours de publication testé est restreint | Capturer la révision inchangée de main |
| **Fusion bloquée avec une revue** | Le nombre de revues s'applique à la PR testée | Ajouter une preuve propre au rôle |
| **L'administrateur publie malgré la règle** | L'identité testée contourne la limite | Examiner les réglages de contournement et les droits |

**Enregistrez le rôle et l'action sans exposer les détails du compte** dans les preuves partagées du cours. Gardez les enregistrements natifs de l'acteur disponibles en privé pour le réviseur. Capturez ensemble la configuration de la règle, l'opération tentée, le refus et la révision protégée résultante.

## Contrôle de fin du dépôt

**Livrez un dépôt qu'un autre contributeur peut parcourir seul.** Le README renvoie à la carte, la carte résout les enregistrements faisant autorité, la couverture des propriétaires inclut les chemins sensibles et la protection s'applique à **`main`**. Conservez une proposition autorisée et une tentative de publication refusée.

**Ne revendiquez pas l'application de la règle à partir des seuls réglages.** Les réglages établissent la configuration prévue. La tentative dans le bac à sable établit le comportement observé pour un rôle et un parcours précis. Transmettez les deux à la leçon sur les agents et les Actions.

## Dépannage et restauration

**Demande de propriétaire manquante :** confirmez l'accès en écriture et la couverture du chemin de branche de base. **Protection absente :** vérifiez le plan et la visibilité. **Fusion toujours activée :** examinez la cible de la règle, la configuration de contournement et le nombre de revues.

**Restauration :** fermez les propositions non fusionnées et désactivez l'automatisation du laboratoire. Annulez le contenu fusionné par une autre PR révisée. Conservez les preuves avant de supprimer le dépôt jetable. N'affaiblissez pas la protection pour terminer un test en échec.

## Exercice et auto-évaluation

**Proposez une modification de `docs/policy.md`** en tant que contributeur. Décidez si l'approbation du mainteneur seule établit l'approbation du propriétaire de la politique.

**Raisonnement attendu :** le nombre de revues n'établit pas à lui seul l'autorité. Le chemin a besoin de la couverture du propriétaire de la politique et d'une revue actuelle du rôle. Listez les exigences propres aux rôles qui ne sont pas appliquées comme des contrôles procéduraux.

## Références principales

- **Contrôles du plan et de la revue :** [Branches protégées](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Admissibilité des propriétaires :** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Contribution dans le navigateur :** [Modification de fichiers](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Étapes suivantes

**Continuez avec [Adaptateurs d'agents et Actions](/articles/ai-collaboration-github-agents-actions/)** pour relier les preuves des sources aux contrôles exécutables.
