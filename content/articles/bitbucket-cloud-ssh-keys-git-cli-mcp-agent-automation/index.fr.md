---
title: "Clés SSH Bitbucket Cloud : accès Git en lecture seule pour les agents IA"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Configurez les clés SSH Bitbucket Cloud, l’accès Git CLI, les jetons REST API, 1Password et les outils MCP pour des workflows d’agents IA en lecture seule."
genre: ["Sécurité cloud", "Outils de développement", "Administration système"]
tags: ["Bitbucket Cloud", "clés SSH Bitbucket", "clés d’accès au dépôt", "clés d’accès au projet", "clés d’accès à l’espace de travail", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "portées des jetons API", "autorisations des agents", "automatisation en lecture seule", "clés hôtes SSH"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Workflow de terminal reliant l’accès Git à Bitbucket Cloud, des clés SSH à portée limitée, 1Password, les lectures REST API et les outils MCP"
coverCaption: ""
---

**Un workflow d’agent limité sépare la lecture du dépôt, la lecture de l’API, la gestion des secrets et les écritures distantes.** Utilisez Git via Secure Shell (SSH) pour accéder aux sources, une clé d’accès Bitbucket en lecture seule pour les extractions automatisées, REST API pour les métadonnées et un serveur Model Context Protocol (MCP) pour les outils approuvés. Stockez les clés privées et les jetons API dans 1Password. Soumettez toute écriture à l’approbation d’une personne.

<!--more-->

## Points clés

- **Lecture seule par défaut :** utilisez une clé d’accès au dépôt ou au projet pour l’extraction par l’agent. Aucune des deux ne permet le push.
- **Identité personnelle :** utilisez une clé SSH personnelle pour les opérations interactives liées à un compte utilisateur.
- **Conservation des secrets :** utilisez 1Password SSH Agent afin que Git demande une signature autorisée sans lire la clé privée.
- **Sens de CLI :** considérez `git`, `curl` et un petit wrapper API audité comme l’interface pratique en ligne de commande de Bitbucket.
- **Limite MCP :** exposez un ensemble restreint d’outils de lecture. Désactivez les outils d’écriture ou placez-les derrière une approbation distincte.
- **Validation des écritures :** laissez l’agent inspecter, comparer et préparer une modification. Exigez l’approbation d’une personne avant un push, une pull request, une fusion ou une modification des paramètres.

## Avant de commencer

**Prérequis :** accès à Bitbucket Cloud, Git, un client OpenSSH, 1Password 8, 1Password CLI, une CLI connectée ou un compte de service approuvé, ainsi qu’un hôte MCP avec contrôle d’approbation des serveurs. Prévoyez 45 minutes. Niveau intermédiaire.

Utilisez un dépôt de test pour le premier essai. Remplacez chaque espace réservé dans les exemples. Les commandes ci-dessous sont des exemples non testés. Elles ne correspondent pas à un compte ou dépôt Bitbucket actif.

**Versions :** cet article fournit des recommandations de conception, pas une procédure liée à des versions précises. Vérifiez les versions installées de Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, de l’hôte MCP et du serveur MCP avant les essais. Configurez 1Password SSH Agent pour le système d’exploitation courant avant d’utiliser `ssh-add -l`.

**Gardez les identifiants hors des shells, journaux, URL, dépôts Git distants et fichiers sources.** Utilisez des espaces réservés comme `<workspace>`, `<repository>`, `<api-token>` et `<socket-path>`. Ne collez pas de vraie clé privée dans une transcription de terminal.

## Choisir la limite d’accès

Bitbucket Cloud prend en charge les clés d’accès aux niveaux du dépôt, du projet et de l’espace de travail. La portée détermine les conséquences d’une copie de la clé. La [comparaison officielle des clés d’accès](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) décrit directement les différences d’autorisation.

| Mode d’accès | Portée | Droit d’écriture | Usage adapté |
|---|---|---:|---|
| **Clé d’accès au dépôt** | Un dépôt | Non | Extraction standard par un agent |
| **Clé d’accès au projet** | Dépôts d’un projet | Non | Tâches en lecture seule sur un petit groupe de dépôts |
| **Clé d’accès à l’espace de travail** | Dépôts d’un espace de travail | Oui | Automatisation de service contrôlée avec un plan d’écriture séparé |
| **Clé SSH personnelle** | Dépôts autorisés pour un utilisateur | Suit le compte utilisateur | Administration interactive |
| **Jeton API** | Portées API liées à l’utilisateur et accès du compte | Dépend des portées | Lectures REST API ou tâche d’écriture temporaire |

**Commencez par la limite la plus restreinte qui convient.** Choisissez une clé de dépôt si un seul dépôt suffit. Choisissez une clé de projet si plusieurs dépôts appartiennent au même projet et si la lecture seule suffit. Traitez une clé d’espace de travail comme une identité d’écriture, pas comme une option par défaut.

Créez et enregistrez la clé la plus restreinte via le chemin correspondant dans les paramètres Bitbucket :

1. Ouvrez Repository settings, Access keys, puis Add key pour un dépôt. Collez la clé publique et gardez la clé en lecture seule.
2. Ouvrez Project settings, Access keys, puis Add key si plusieurs dépôts ont besoin d’une identité de lecture limitée au projet.
3. Utilisez une clé d’espace de travail uniquement dans un espace partagé avec une conception d’écriture approuvée. Les espaces de travail personnels ne proposent pas le même chemin au niveau de l’espace de travail.
4. Notez le libellé de la clé, sa portée, l’empreinte de la clé publique, son propriétaire et sa date de rotation. Gardez la clé privée dans 1Password.

Après l’enregistrement, exécutez un test exact de connexion en lecture seule :

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Résultat attendu :** une référence de commit pour `HEAD`. Exemple non testé. Un résultat positif prouve qu’une identité SSH autorisée a atteint le dépôt nommé. Il ne prouve ni que la clé enregistrée a été choisie ni qu’elle dispose d’un droit d’écriture. Relancez le test après la configuration d’une clé par dépôt.

Pour la conservation des clés privées et le consentement de 1Password SSH Agent, consultez [1Password CLI et SSH Agent : sécuriser les clés SSH pour les agents IA](/articles/1password-cli-ssh-keys-mcp-agent-administration/).

## Définir correctement « Bitbucket CLI »

L’expression **Bitbucket CLI** mélange souvent trois interfaces différentes. Distinguez-les.

- **Git CLI :** `git clone` et `git fetch` transfèrent les données du dépôt via SSH ou HTTPS. `git diff` compare les fichiers locaux ou les révisions.
- **Client REST :** `curl` ou un wrapper examiné appelle l’API Representational State Transfer (REST) de Bitbucket Cloud. Une API est une interface programmatique pour demander des données ou des actions. La [référence REST API de Bitbucket Cloud](https://developer.atlassian.com/cloud/bitbucket/rest/) répertorie les ressources de dépôt, source, branche, pull request, pipeline et statut.
- **Atlassian CLI :** `acli` est la ligne de commande officielle d’Atlassian. Son [introduction](https://developer.atlassian.com/cloud/acli/guides/introduction/) présente le produit, tandis que sa [référence des commandes](https://developer.atlassian.com/cloud/acli/reference/commands/) répertorie les interfaces `admin`, `jira`, `feedback` et `rovodev`. La référence ne documente pas de commandes Bitbucket Cloud.

**La référence officielle des commandes `acli` d’Atlassian ne documente aucune commande Bitbucket Cloud.** N’inventez pas une commande comme `acli bitbucket clone`. Utilisez Git pour les opérations Git et REST API pour les données Bitbucket Cloud.

### CLI Teamwork Graph en option

**Atlassian publie également la CLI Teamwork Graph, appelée `twg`.** Sa [présentation](https://developer.atlassian.com/cloud/twg-cli/) et son [catalogue de commandes](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) documentent des familles de commandes Bitbucket. La commande de configuration est :

```bash
twg setup
```

La commande de configuration modifie l’état d’authentification local. Suivez les invites de la version installée pour configurer éventuellement un jeton Bitbucket. Le chemin du jeton Bitbucket dans la CLI est distinct de l’authentification OAuth Atlassian. Respectez la syntaxe exacte de la version installée et du catalogue courant. Utilisez un profil séparé, un jeton restreint, des compétences installées examinées et une approbation humaine pour les commandes modificatrices.

**Résultat attendu, non testé :** le profil isolé reçoit les paramètres d’authentification Bitbucket. Notez l’état précédent du profil avant la configuration. Lors du retour arrière, supprimez l’identifiant enregistré via la procédure de déconnexion ou de retrait de configuration documentée pour la version installée.

Si un projet tiers se présente comme une CLI Bitbucket, auditez son code source, son processus de publication, ses sommes de contrôle, sa procédure de mise à jour, son flux d’authentification, les portées demandées, les destinations réseau, la gestion des journaux et les commandes d’écriture. Un nom de binaire familier ne prouve ni la prise en charge par le fournisseur ni des autorisations sûres.

## Garder les clés SSH sous le contrôle de 1Password

[1Password SSH Agent](https://www.1password.dev/ssh/agent) met les clés SSH stockées dans 1Password à disposition de Git et des clients SSH. Le client effectue une demande de signature autorisée. La clé privée reste dans l’application 1Password, qui demande un consentement avant qu’un client approuvé utilise une clé.

La [référence 1Password CLI](https://www.1password.dev/cli/reference) a un autre rôle. Utilisez `op` pour accéder de manière contrôlée aux éléments, jetons API, comptes de service et paramètres d’automatisation. Utilisez SSH Agent pour la signature SSH. Évitez d’exporter une clé privée dans un fichier temporaire pour simplifier le workflow d’un agent.

Vérifiez l’état local de la CLI et de l’agent avec des commandes en lecture seule :

```bash
op --version
ssh-add -l
```

**Résultat attendu :** une version de 1Password CLI et une ou plusieurs empreintes de clés publiques de l’agent actif. Exemple non testé. Un résultat vide de `ssh-add -l` signifie qu’aucune clé n’est disponible via le socket d’agent sélectionné.

Pour une nouvelle clé, créez un élément SSH Key Ed25519 dans 1Password ou importez une clé générée par un processus local de confiance. Choisissez un libellé selon l’usage, la portée et la date de rotation. Ajoutez uniquement la clé publique à Bitbucket Cloud. Le [guide Linux des clés d’accès aux dépôts](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) décrit le chemin des paramètres du dépôt et la limite en lecture seule.

## Vérifier d’abord la clé hôte Bitbucket

L’authentification SSH de l’utilisateur ne prouve pas l’identité du serveur. Le client doit vérifier la clé hôte de Bitbucket Cloud avant d’envoyer une demande d’authentification. Le [guide Atlassian sur SSH et la vérification en deux étapes](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) répertorie les clés hôtes publiques et indique le point de terminaison officiel pour récupérer les entrées known_hosts.

Récupérez les données de clé hôte publique pour les comparer :

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Résultat attendu :** des lignes OpenSSH `known_hosts` pour `bitbucket.org`. Exemple non testé. Comparez la clé ou l’empreinte renvoyée avec une copie indépendante et fiable avant de placer la ligne dans `~/.ssh/known_hosts`.

Utilisez la vérification stricte de l’hôte après avoir ajouté l’entrée approuvée :

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**N’acceptez pas une clé hôte modifiée pendant une exécution d’agent.** Arrêtez l’exécution, vérifiez la fiche actuelle des clés hôtes Bitbucket Cloud et examinez l’entrée locale `known_hosts`. Une acceptation automatique supprime une limite de sécurité liée aux clés.

## Sélectionner une clé par dépôt

Un appareil contient souvent plusieurs clés Bitbucket. Un agent SSH général propose plusieurs identités lors d’une connexion. Un serveur ou une stratégie avec une limite basse de tentatives d’authentification risque de rejeter la bonne clé après l’échec des précédentes.

Le [guide Atlassian sur plusieurs clés d’accès aux dépôts](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) utilise `core.sshCommand` dans un fichier de configuration Git du dépôt et `includeIf` dans la configuration Git globale. Reprenez ce modèle pour utiliser une clé par dépôt.

Exemple portable avec fichiers :

```ini
# .gitconfig dans un dépôt local
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

Le bloc ci-dessus est une exception avec fichier de clé privée pour une identité d’automatisation dédiée. Il ne configure pas 1Password SSH Agent. Pour 1Password SSH Agent, configurez la valeur `IdentityAgent` ou `SSH_AUTH_SOCK` propre à la plateforme depuis le [guide de configuration 1Password](https://www.1password.dev/ssh/get-started). Certaines configurations OpenSSH utilisent un fichier `.pub` comme sélecteur d’identité d’agent. Vérifiez la prise en charge de la plateforme avant de l’utiliser. Une configuration avec fichier nécessite le chemin de la clé privée correspondante. Ne passez jamais un fichier `.pub` à une commande qui attend une clé privée et n’exportez jamais une clé privée personnelle.

Utilisez une configuration explicite du dépôt lorsqu’un clone local nécessite une clé particulière. Utilisez `includeIf` lorsqu’un répertoire contient plusieurs clones relevant de la même limite d’accès. Le [guide sur plusieurs clés](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) présente les deux paramètres dans le workflow Bitbucket.

Clonez avec Git via SSH :

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Résultat attendu :** Git crée `<local-directory>` et récupère le dépôt via `bitbucket.org`. Exemple non testé. Une clé d’accès au dépôt permet uniquement le clonage et le pull.

## Utiliser des jetons API pour des lectures REST ciblées

Utilisez SSH pour le transport Git. Utilisez REST API pour les métadonnées ou les opérations hors transport Git. Le [guide des autorisations des jetons API](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) répertorie les portées du dépôt, comme Read, Write, Admin et Delete. Repository Read correspond à `read:repository:bitbucket` et n’inclut pas l’accès aux pull requests.

Pour l’automatisation en lecture, préférez un jeton d’accès de dépôt ou de projet Bitbucket si la cible prend en charge le point de terminaison nécessaire. Un jeton API lié à un utilisateur conserve l’accès plus large de son compte. N’utilisez un jeton d’espace de travail que si le ticket de tâche précise cette portée plus large. Consultez le [guide des jetons d’accès Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) avant de choisir le type de jeton.

Pour la lecture par un agent, commencez par `read:repository:bitbucket`. Ajoutez `read:pullrequest:bitbucket` uniquement si l’agent a besoin des données de pull request. N’ajoutez des portées d’espace de travail ou de pipeline que si le ticket précise le point de terminaison et le résultat attendus. Les portées d’écriture et d’administration exigent une approbation distincte.

Créez chaque jeton API pour un seul usage, définissez une date d’expiration, inscrivez-la dans le registre de rotation et remplacez le jeton avant son expiration. Le [guide Atlassian de création des jetons API](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) exige un nom, une date d’expiration, une application et des portées. Le jeton ne s’affiche qu’une fois après sa création.

Conservez la valeur dans 1Password ou dans un secret d’exécution géré. Ne placez pas cette valeur dans une URL distante. Transmettez un jeton bearer par variable d’environnement uniquement au processus qui doit effectuer une lecture :

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Gardez `/path/to/agent.env` hors du dépôt. Stockez dans le fichier une référence telle que `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`. `op run` résout la référence et expose la valeur au processus enfant curl pendant la durée du sous-processus. Cela n’empêche pas le processus enfant de lire la valeur de la variable d’environnement ou de l’écrire dans un journal. Ne remplacez pas l’espace réservé par un jeton littéral.

**Résultat attendu :** métadonnées JSON du dépôt sélectionné. Exemple non testé. L’espace réservé ne doit jamais devenir un vrai jeton dans un fichier validé ou un journal.

Pour une automatisation plus longue, laissez 1Password injecter un secret dans l’environnement du processus via le flux CLI ou compte de service pris en charge. Gardez la durée du jeton adaptée à la tâche. Révoquez-le si la tâche se termine plus tôt ou si le propriétaire de l’hôte change.

## Fournir à MCP une petite surface de lecture

Utilisez la [spécification MCP actuelle](https://modelcontextprotocol.io/specification/2026-07-28) et ses [règles d’autorisation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) pour examiner un nouveau serveur. Les serveurs HTTP doivent vérifier l’audience du jeton et gérer clairement les réponses 401 et 403.

L’hôte MCP obtient le consentement de l’utilisateur. Le client maintient une connexion à un serveur. Le serveur expose des outils, des ressources ou des prompts. Traitez chaque serveur comme du code non fiable jusqu’à ce que sa source, son transport, son compte et ses autorisations aient été examinés.

L’URL de spécification 2025-06-18 du paragraphe suivant désigne une version historique. Utilisez la spécification actuelle 2026-07-28 pour les nouveaux examens.

La [spécification MCP](https://modelcontextprotocol.io/specification/2025-06-18) définit la communication entre un hôte MCP, un client et un serveur. Un serveur expose des outils, des ressources ou des prompts via le protocole. MCP normalise le format de connexion. L’hôte, l’implémentation du serveur, le compte, la portée du jeton et la politique d’approbation déterminent toujours ce qu’un appel permet d’atteindre.

Utilisez un serveur MCP comme adaptateur restreint au-dessus de Git et de REST API Bitbucket Cloud.

Protégez cet adaptateur contre le transfert de jetons, la falsification de requêtes côté serveur (SSRF) et le comportement de mandataire confus. Le SSRF permet à un serveur d’envoyer des requêtes vers des destinations non prévues. Un mandataire confus utilise des privilèges plus larges au nom d’un appelant. Protégez aussi le système contre les serveurs locaux malveillants, les redirections OAuth dangereuses et les réponses de données sources excessivement volumineuses. Fixez les origines Bitbucket autorisées et les identifiants de dépôt. Exécutez les serveurs locaux dans un bac à sable sous un compte de système d’exploitation dédié. Masquez les secrets dans les résultats des outils et les journaux.

Cette section décrit une conception, pas une configuration MCP testée. Aucun client, serveur, transport, version ou jeu de données de test n’est spécifié. Validez un serveur en lecture seule dans un profil de test séparé avant de connecter un agent à un dépôt de production.

Exemples d’outils de lecture :

| Outil | Résultat limité |
|---|---|
| **`get_repository_metadata`** | Renvoie les métadonnées d’un dépôt |
| **`read_source_file`** | Lit un chemin donné à une révision donnée |
| **`list_branches`** | Liste les branches d’un dépôt |
| **`get_pull_request`** | Renvoie une pull request si le jeton inclut la portée de lecture des pull requests |
| **`get_build_status`** | Renvoie le statut d’un commit |

Ces noms décrivent une conception. Ce ne sont pas des commandes Atlassian. Empêchez le serveur d’accepter des URL arbitraires, des commandes shell arbitraires, des jetons bruts, des demandes d’export de clés privées ou des identifiants de dépôt sans restriction.

Définissez les autorisations à quatre niveaux :

1. **Bitbucket Cloud :** clé de lecture de dépôt ou de projet pour Git, avec les portées minimales de jeton API pour les lectures REST.
2. **1Password :** un coffre ou compte de service dédié à la tâche, sans possibilité d’exporter les clés privées.
3. **Serveur MCP :** liste autorisée d’outils de lecture, points de terminaison Bitbucket Cloud fixes, validation des entrées, délais d’expiration et journaux masqués.
4. **Hôte MCP :** approbation de l’utilisateur pour le serveur et chaque action permettant une écriture, avec les outils d’écriture désactivés dans le profil par défaut.

*Une liste d’outils MCP prouve leur découverte. Elle ne prouve ni l’autorisation, ni la portée correcte, ni la sûreté des entrées, ni l’exactitude du résultat.*

## Dérouler le workflow de l’agent

Gardez le workflow explicite. Chaque étape fournit des éléments probants à la suivante.

| Étape | Action de l’agent | Autorisation | Validation humaine |
|---|---|---|---|
| **Préparer** | Lire la configuration, la fiche de clé hôte, le libellé de clé, la portée du jeton et l’expiration | Lecture locale | Approuver la fiche de configuration |
| **Inspecter** | Cloner ou récupérer via Git sur SSH et interroger les métadonnées REST | Lecture du dépôt et de l’API | Aucune après la configuration |
| **Analyser** | Lire les fichiers, branches, pull requests et statuts de build avec les outils approuvés | Outils MCP en lecture seule | Aucune pour les lectures limitées |
| **Préparer la modification** | Produire un correctif, un plan de branche ou un brouillon de pull request dans un espace local | Écriture locale uniquement | Examiner le diff et la cible |
| **Approuver l’écriture** | Présenter l’action distante exacte, sa portée et la procédure de retour arrière | Pas encore d’écriture distante | Approbation humaine |
| **Exécuter l’écriture** | Pousser une branche, créer une pull request ou appeler un point de terminaison d’écriture | Identité d’écriture de courte durée | Confirmer chaque action |
| **Vérifier** | Lire le commit, la pull request ou le statut obtenu | De nouveau en lecture seule | Confirmer le résultat attendu |

Le profil d’agent par défaut devrait s’arrêter après **Analyser** ou **Préparer la modification**. Un profil d’écriture séparé devrait utiliser un autre jeton ou une autre clé, une expiration courte, une cible fixe et une demande d’approbation. Une clé d’accès au dépôt ne permet pas l’étape d’écriture, ce qui crée une limite technique utile.

## Retour arrière et suppression

Commencez le retour arrière par la suppression des accès, puis nettoyez la configuration locale :

1. Supprimez la clé d’accès au dépôt, au projet ou à l’espace de travail dans la page de paramètres Bitbucket correspondante.
2. Révoquez le jeton API de dépôt, de projet, d’espace de travail ou d’utilisateur dans la page de sécurité Bitbucket correspondante.
3. Supprimez l’identifiant Teamwork Graph enregistré via la [procédure d’authentification documentée](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) pour la version de CLI installée. Conservez l’identifiant antérieur uniquement dans le gestionnaire de secrets approuvé. Vérifiez que le profil isolé ne répertorie plus l’identifiant de test.
4. Après le test, supprimez le fichier `.gitconfig` du dépôt et son entrée `includeIf`. Conservez les autres paramètres Git inchangés.
5. Supprimez uniquement la ligne de clé hôte Bitbucket vérifiée et ajoutée pour le test. Conservez les autres clés hôtes approuvées.
6. Supprimez le fichier externe `agent.env` et les sorties temporaires. Retirez l’entrée du serveur MCP de la configuration de l’hôte, puis redémarrez ce dernier.

Consignez chaque suppression, l’opérateur et l’heure. Faites tourner une clé ou un jeton si une valeur apparaît dans un journal, un enregistrement de processus ou une transcription inattendus.

## Boucle de lecture distante avec mises à jour locales des références

Utilisez une petite boucle pour inspecter régulièrement un dépôt :

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` désigne la référence actuellement extraite du dépôt. Un résultat positif prouve qu’une identité SSH autorisée a atteint le dépôt nommé. Il ne prouve pas quelle clé a été sélectionnée ni l’existence d’un droit de push.

**Résultat attendu :** résultat de fetch, statut de branche et une ligne de commit. Exemple non testé. `fetch` n’effectue aucune écriture distante, mais met à jour les références locales et `FETCH_HEAD`. La boucle ne pousse rien et ne change pas de branche.

Le serveur MCP devrait exposer la même limite de lecture par des opérations nommées. Un wrapper shell local ou un outil MCP devrait rejeter tout verbe d’écriture avant l’envoi d’une requête. Consignez le nom de l’outil, l’espace réservé du dépôt, la révision, la catégorie du résultat et la durée. Masquez les jetons, cookies, chemins privés et contenus de fichiers, sauf si la tâche exige explicitement un fichier.

## Dépannage

### `Permission denied (publickey)`

Vérifiez le socket de l’agent actif, la clé publique sélectionnée, l’entrée de clé d’accès au dépôt et `IdentitiesOnly`. Une clé de dépôt doit être enregistrée sur le dépôt ou le projet cible. Une clé personnelle exige les autorisations du compte. Une clé d’espace de travail possède une limite d’écriture différente.

### La mauvaise clé de dépôt est proposée

Utilisez une clé par dépôt avec `core.sshCommand`, ou regroupez les clones dans un répertoire contrôlé par `includeIf`. Listez les clés de l’agent avec `ssh-add -l`. Si plusieurs clés 1Password sont disponibles, utilisez un sélecteur d’identité explicite ou un signet SSH 1Password. Le [guide 1Password Agent](https://www.1password.dev/ssh/agent) documente le nombre de clés et l’usage des signets.

### SSH signale une clé hôte modifiée

Arrêtez l’agent. Ne supprimez pas `known_hosts` en première réaction. Comparez la fiche actuelle des clés hôtes Bitbucket Cloud avec l’entrée locale via un canal indépendant. Ne supprimez ou ne remplacez une entrée qu’après validation de la comparaison.

### L’API renvoie `401` ou `403`

Vérifiez l’expiration et le type du jeton, la portée du point de terminaison et la limite du compte ou de l’espace de travail. Une portée de lecture du dépôt n’inclut pas les pull requests. Un point de terminaison d’écriture exige une portée d’écriture et un profil d’écriture approuvé. N’élargissez pas les portées avant d’avoir identifié le point de terminaison en échec.

### L’API renvoie les données du dépôt, mais aucune pull request

Ajoutez la portée minimale de lecture des pull requests à un jeton neuf ou renouvelé. Ne réutilisez pas un jeton utilisateur étendu pour un serveur MCP en lecture seule.

### Le serveur MCP répertorie des outils, mais un appel échoue

Distinguez l’enregistrement du serveur, la connexion, la découverte des outils, leur exécution et la vérification du résultat. Consultez le journal du serveur sans exposer le jeton. Vérifiez le point de terminaison et la forme des entrées. Réessayez une fois après avoir vérifié la connectivité. Déclarez l’opération incomplète si le second appel échoue.

### Une CLI Bitbucket tierce demande un accès étendu

Arrêtez l’installation. Comparez l’accès demandé avec le ticket de tâche. Examinez le code source, les signatures ou sommes de contrôle des publications, les destinations réseau, le stockage des secrets et les comportements d’écriture. La référence officielle des commandes Atlassian CLI ne prouve pas la prise en charge d’un binaire Bitbucket tiers.

## Étapes suivantes

Créez une fiche d’accès concise indiquant la portée du dépôt ou du projet, le libellé de la clé, la date de vérification de la clé hôte, les portées API, l’expiration du jeton, le propriétaire 1Password, la liste autorisée des outils MCP, la politique de journalisation et la personne qui approuve les écritures.

Effectuez un clone en lecture seule, une lecture des métadonnées REST et une lecture d’outil MCP avec des espaces réservés dans la transcription. Comparez les résultats. Gardez le profil de l’agent en lecture seule jusqu’à validation de la fiche et des journaux.

Lorsqu’une tâche d’écriture arrive, préparez d’abord un diff local. Présentez la branche cible, les chemins modifiés, la méthode API demandée, la portée du jeton et l’étape de retour arrière. N’utilisez une identité d’écriture distincte et de courte durée qu’après l’approbation humaine de l’action exacte.
