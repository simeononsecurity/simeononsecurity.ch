---
title: "1Password SSH Agent and CLI: Accès en lecture seule pour les agents IA"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Concevez un flux de travail SSH en lecture seule avec 1Password CLI, l'agent SSH et MCP. Utilisez des commandes synthétiques, des permissions restreintes et une approbation humaine avant les tests en direct."
genre: ["Administration système", "Sécurité cloud", "Automatisation"]
tags: ["1Password CLI", "Clés SSH", "1Password SSH Agent", "MCP", "Model Context Protocol", "Administration d'agents", "Administration des systèmes", "Bitbucket Cloud", "Git via SSH", "Références de secrets", "Comptes de service", "Privilèges minimaux", "Authentification par clé publique", "Gestion des secrets", "Sécurité de la ligne de commande", "Sécurité de l'automatisation"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Diagramme abstrait d'un agent utilisant une référence de secret, un agent SSH et des outils MCP sans afficher de clés privées."
coverCaption: ""
---

**Un agent en ligne de commande a besoin d'un accès utile, pas d'une copie de chaque identifiant.** Ce guide présente une conception bornée pour 1Password CLI, l'Agent SSH 1Password, l'accès Git Bitbucket et le Model Context Protocol (MCP). Le premier flux de travail utilise des noms synthétiques, des actions en lecture seule et une approbation humaine à la frontière SSH.

<!--more-->

La distinction clé est simple. **L'SSH interactif utilise le consentement via l'Agent SSH 1Password. L'automatisation non supervisée nécessite une identité distincte, un accès restreint et un cycle de vie des clés différent.** Ne considérez pas une connexion MCP comme une autorisation d'exécuter l'un ou l'autre des flux de travail.

## Points clés

- **Protection des clés privées :** L'Agent SSH 1Password effectue l'authentification SSH tout en conservant les clés privées dans l'application 1Password.
- **Gestion des clés publiques :** Publiez uniquement une clé publique sur Bitbucket ou un compte distant. Conservez la moitié privée dans un élément Clé SSH.
- **Consentement interactif :** Une personne approuve une session client ou terminal avant que l'Agent SSH n'utilise une clé.
- **Séparation non supervisée :** Un travail planifié nécessite un compte de service dédié et un périmètre de coffre-fort restreint. Une approbation de l'Agent SSH interactif ne satisfait pas ce besoin.
- **Limites du MCP :** Le MCP connecte un agent aux outils et aux ressources. Le client, le serveur, le système d'exploitation et la politique 1Password contrôlent toujours l'accès.

## Avant de commencer

**Prérequis :** Installez 1Password 8 et 1Password CLI 2.20.0 ou une version ultérieure. Connectez-vous via un compte 1Password pris en charge. Utilisez un client OpenSSH. Créez un dépôt Bitbucket de test ou une autre cible non de production. Gardez un chemin administratif secondaire disponible pour le retour arrière.

**Durée :** 30 à 45 minutes pour une revue de conception et une démonstration synthétique.

**Difficulté :** Intermédiaire. Vous avez besoin de connaissances de base en Git, SSH, shell et contrôle d'accès.

Ce guide couvre la conception et la planification. L'article Bitbucket lié couvre les limites d'accès spécifiques à Bitbucket. Ce guide ne teste pas de compte en direct, ne crée pas de clé réelle, ne se connecte pas à un hôte réel et n'enregistre pas de serveur MCP réel. Tous les identifiants ci-dessous sont synthétiques. **Remplacez les espaces réservés uniquement dans votre propre environnement contrôlé.**

**Posture de version :** Utilisez 1Password 8 et [1Password CLI 2.20.0 ou ultérieur](https://www.1password.dev/ssh/manage-keys) pour ce flux de travail. [1Password CLI 1 est obsolète](https://www.1password.dev/cli/upgrade/). [1Password 7 prendra sa retraite au début de 2027](https://support.1password.com/add-account/). La génération, l'importation et le partage de clés SSH nécessitent 1Password 8. Confirmez les versions de Git, OpenSSH, de l'hôte MCP et du serveur MCP installés avant de tester. Les exemples ci-dessous restent non testés.

Un **coffre-fort** est une collection protégée d’éléments 1Password. **OpenSSH** est le logiciel client et serveur SSH utilisé par de nombreux systèmes d’exploitation. **MCP**, ou Model Context Protocol, connecte un agent à des outils ou des ressources approuvés.

## Pourquoi conserver les clés privées illisibles

Une paire de clés SSH comprend une clé publique et une clé privée. Un service Git distant ou un serveur stocke la clé publique. Le client prouve la possession de la clé privée lors de l’authentification. La clé privée n’a pas besoin de voyager vers le service distant.

L’[Agent SSH 1Password](https://www.1password.dev/ssh/agent) étend ce modèle. Sa documentation indique que les clients SSH et Git s’authentifient via l’agent, tandis que la clé privée reste dans l’application 1Password. Le client reçoit un résultat de signature, et non un fichier de clé privée.

Cette limite réduit plusieurs vecteurs d’exposition :

- **Contrôle de version :** Une clé privée n’entre pas dans un dépôt ou une demande de fusion (pull request).
- **Historique de shell :** La valeur d’une clé privée n’apparaît pas dans un argument de commande.
- **Fichiers temporaires :** Un script n’a pas besoin d’écrire une clé privée dans `~/.ssh/`.
- **Contexte de l’agent :** Un grand modèle de langage (LLM) n’a pas besoin du texte de la clé privée pour demander une opération SSH.
- **Réutilisation accidentelle :** Une clé copiée ne reste pas dans un ancien espace de travail après la fin d’une tâche.

Cette limite ne rend pas SSH inoffensif. Un processus ayant la permission d’utiliser le socket de l’agent pourrait effectuer des actions au nom de la clé approuvée. La vérification des clés d’hôte, les limites des comptes distants, les permissions des dépôts, la politique de commandes et l’isolation des processus restent importants.

*La limite de la clé privée protège le matériel de la clé. La limite n’approuve pas une commande distante ni ne prouve que l’hôte cible est de confiance.*

## Consentement SSH interactif

Configurez un coffre-fort dédié pour les clés d’agent. Utilisez le fichier de configuration de l’Agent SSH pour sélectionner le plus petit ensemble de clés et une clé spécifique à l’hôte. N’exposez pas toutes les clés éligibles de tous les coffres-forts intégrés à un processus d’automatisation.

Le [modèle de sécurité de l’Agent SSH 1Password](https://www.1password.dev/ssh/agent/security) lie l’approbation à une clé et à un processus demandeur. L’invite d’identification identifie le processus et la clé. La personne approuve ensuite la demande via la méthode d’authentification configurée.

1Password documente plusieurs étendues d’approbation. L’approbation par clé et par application est la valeur par défaut. Une étendue de session de terminal restreint l’approbation à un onglet ou à une session. L’approbation par demande demande à nouveau pour chaque demande. Une option d’approbation pour tous les processus existe, mais cette option accorde à tous les processus sous l’utilisateur du système d’exploitation actuel un accès pour la session.

**Utilisez la portée d’approbation la plus étroite adaptée à la tâche.** Un agent d’administration système doit s’exécuter dans un terminal dédié ou un bac à sable. N’approuvez pas tous les processus si une seule session de terminal suffit.

La session d’approbation n’est pas une autorisation permanente. 1Password enregistre l’autorisation pour la période configurée ou jusqu’à ce que l’application soit verrouillée ou fermée. Lorsque l’application est verrouillée, l’agent ne conserve pas les clés privées pour une utilisation ultérieure. Le processus SSH Agent continue en arrière-plan lorsque le paramètre pris en charge est activé pendant que 1Password est fermé, mais une nouvelle demande de signature nécessite que 1Password soit déverrouillé.

Le [guide de configuration SSH de 1Password](https://www.1password.dev/ssh/get-started) présente le flux général : générer ou importer une clé, publier la clé publique, activer l’agent SSH, configurer le client SSH, exécuter une commande SSH ou Git, et approuver la demande. Le chemin de socket exact varie selon le système d’exploitation. Utilisez les instructions de la plateforme actuelle au lieu de copier un chemin depuis une autre machine.

L’application 1Password doit être déverrouillée avant qu’une nouvelle demande de signature ne réussisse. Le processus agent peut continuer en arrière-plan pendant que l’application est fermée. Une application verrouillée ne libère pas les données de clé privée pour la signature.

## Clés publiques et Bitbucket

Le [guide de gestion des clés de 1Password](https://www.1password.dev/ssh/manage-keys) documente les éléments de clé SSH, la génération de clés, l’importation de clés, les clés publiques, les empreintes et les clés privées. L’exemple CLI utilise `op item create --category ssh` pour créer un élément de clé SSH. 1Password CLI génère une clé Ed25519 par défaut pour cet exemple et masque la clé privée dans sa sortie.

Bitbucket Cloud utilise le flux de travail en ligne de commande Git et OpenSSH standard. Son [guide en ligne de commande](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) décrit les opérations Git depuis un dépôt local. Son [guide de configuration SSH](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) énumère les formes distantes SSH et les formats de clé publique pris en charge.

**Considérez Bitbucket comme le consommateur de la clé publique.** Enregistrez la clé publique ou l’empreinte via le compte Bitbucket approuvé ou le paramètre de dépôt. Conservez la clé privée dans 1Password. Le client Git demande à l’agent SSH de signer. Le client ne lit pas de fichier de clé privée.

Pour la portée de la clé d’accès Bitbucket, le chemin d’enregistrement et le test Git en lecture seule, consultez [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

La documentation de Bitbucket appelle cela un flux de travail Git CLI. Cet article ne suppose pas un serveur MCP Bitbucket distinct ou un produit nommé Bitbucket CLI. Un CLI spécifique à Bitbucket nécessite sa propre documentation à jour et sa propre revue des permissions.

## La frontière entre l’agent et MCP

Utilisez la spécification MCP actuelle](https://modelcontextprotocol.io/specification/2026-07-28) lors de l'examen d'un nouveau serveur.

L'URL de la spécification du 18-06-2025 dans le paragraphe de contexte suivant est une version historique. Utilisez la spécification du 28-07-2026 pour les nouveaux examens.

[MCP](https://modelcontextprotocol.io/specification/2025-06-18) standardise les connexions entre une application LLM, un connecteur client et un serveur. Un serveur propose des outils, des ressources ou des invites. La spécification indique également que les hôtes doivent obtenir le consentement de l'utilisateur avant d'exposer des données ou d'invoquer des outils.

**MCP lui-même n'accorde pas de permissions.** Un outil MCP s'exécute toujours dans le cadre des permissions de son processus serveur, de l'utilisateur du système d'exploitation, du chemin réseau, du compte cloud et des identifiants configurés. Une description d'outil n'est pas une politique d'autorisation.

La [documentation 1Password Security for AI](https://www.1password.dev/security-for-ai) décrit un serveur MCP Environments et des modèles de configuration MCP sécurisés. La même page décrit le chargement à l'exécution des valeurs de configuration MCP depuis 1Password. Ces pages ne définissent pas un produit MCP générique de clé SSH 1Password ni un flux de travail SSH universel pour chaque client agent.

Utilisez MCP comme une surface de contrôle étroite :

- **Outils de lecture :** Inspecter l'état du service, les métadonnées du dépôt ou les journaux approuvés.
- **Outils de planification :** Préparer une commande ou un enregistrement de modification sans exécuter la commande.
- **Outils d'approbation :** Demander une décision humaine avant une écriture distante.
- **Outils d'écriture :** Garder désactivés jusqu'à ce que la cible, la commande, la portée et le plan de retour arrière soient explicites.

L'agent doit recevoir des références, des métadonnées et des résultats d'opération. **L'agent ne doit pas recevoir le texte d'une clé privée, un déversement complet d'un coffre-fort ou un shell sans restriction.**

## Une première politique sûre

Commencez par une politique écrite avant d'activer un agent. Gardez la politique proche de la configuration MCP, mais ne placez pas d'identifiants dans le fichier.

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

Cette politique est un exemple, et non un format de configuration 1Password. Stockez la politique réelle dans le plan de contrôle utilisé par votre client agent. Examinez chaque outil par rapport à la politique avant d'activer chaque outil.

## Comptes de service et références de secrets

Un **compte de service** confère à un processus automatisé son propre identifiant. Le [guide des scripts 1Password CLI](https://www.1password.dev/cli/secrets-scripts) recommande les comptes de service pour un accès à privilèges minimaux à des coffres-forts sélectionnés. Cela sépare un job non supervisé du SSO, de la MFA, de l'inventaire des coffres-forts et du compte quotidien d'une personne.

Une **référence secrète** désigne une valeur sans la placer dans le code source. La [référence CLI 1Password](https://www.1password.dev/cli/reference) utilise la forme `op://vault/item/field`. La référence est sûre à stocker uniquement lorsque le processus environnant conserve un accès restreint. Une référence ne contourne pas la politique.

Utilisez `op read` lorsqu'une commande a besoin d'une seule valeur. Utilisez `op run` lorsqu'un processus enfant a besoin d'un ensemble contrôlé de valeurs d'exécution. Utilisez `op item create` lorsqu'une nouvelle entrée de clé SSH doit exister dans le coffre approuvé.

Ne confondez pas l'injection d'exécution avec la protection de la clé privée. Un jeton API passé en tant que variable d'environnement reste visible par le processus enfant. Une clé privée passée via une variable d'environnement est pire, car la valeur étend l'exposition à l'inspection des processus, aux rapports de plantage, aux sorties de débogage, au traçage du shell et à la journalisation accidentelle.

**Privilégiez une référence dans le code source et une valeur d'exécution dans le processus le plus petit possible.** Maintenez le processus à durée de vie courte. Désactivez le traçage du shell. N'affichez pas l'environnement. Supprimez les fichiers temporaires après une exécution échouée.

## Flux de travail initial sûr

La séquence ci-dessous sépare l'enregistrement de la clé publique, SSH interactif, la découverte MCP et la conception non supervisée.

### 1. Définir la cible

Notez la classe de cible, le compte distant, le dépôt ou la commande prévue, la source de la clé hôte, le propriétaire de l'approbation et l'action de retour arrière. Utilisez un enregistrement synthétique lors du premier exercice.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Résultat attendu, non testé :** L'enregistrement identifie une cible et une opération. L'enregistrement ne contient pas d'hôte, d'adresse IP, de jeton, de clé privée ou de données personnelles.

### 2. Créer ou sélectionner l'entrée de clé SSH

Le [guide officiel des clés SSH 1Password](https://www.1password.dev/ssh/manage-keys) documente le modèle de création CLI. La commande ci-dessous utilise un titre synthétique et un coffre de test nommé.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Sortie attendue, non testée :** 1Password crée une entrée de clé SSH dans le coffre de test nommé et masque la clé privée dans la sortie du terminal. La commande modifie l'état de 1Password. La sortie lisible exacte dépend de la version du CLI et de l'état de connexion.

Capturez l'identifiant d'entrée retourné dans l'enregistrement de test sans copier le champ de la clé privée. Utilisez l'identifiant ou le titre exact de l'entrée pour les lectures spécifiques aux champs uniquement après confirmation du schéma de l'entrée.

Ne redirigez pas cette sortie vers un journal partagé. Capturez uniquement l'identifiant de l'entrée, l'empreinte de la clé publique et l'enregistrement d'approbation lorsque la procédure locale prend en charge une sortie structurée sûre.

### 3. Gérer la clé publique

Ouvrez l’élément Clé SSH dans 1Password et utilisez l’action Copier la clé publique. N’utilisez une référence spécifique à un champ qu’après avoir confirmé l’étiquette du champ de clé publique dans votre propre compte. Ne déversez pas l’élément complet.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Sortie attendue, non testée :** Une ligne synthétique de clé publique OpenSSH ou une valeur de clé publique issue du champ confirmé. Le nom de champ fictif ci-dessus n’est pas une garantie quant à l’étiquette du champ de votre élément.

Enregistrez la clé publique dans le compte Bitbucket approuvé, le dépôt Bitbucket ou le compte distant. Ne collez jamais la clé privée correspondante dans Bitbucket. Le [guide SSH de Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) recommande également d’enregistrer la clé hôte de Bitbucket avant la première connexion.

Pour Bitbucket, récupérez l’enregistrement de clé hôte publié et comparez cet enregistrement avec une copie de confiance indépendante avant d’ajouter une ligne à `~/.ssh/known_hosts`. Utilisez une vérification stricte de l’hôte après que la comparaison a réussi. N’acceptez pas une clé hôte modifiée pendant l’exécution d’un agent.

### 4. Activer SSH interactif

Activez l’Agent SSH 1Password dans l’application de bureau. Configurez OpenSSH avec la valeur spécifique à la plateforme `IdentityAgent` ou `SSH_AUTH_SOCK` issue du [guide de configuration officiel](https://www.1password.dev/ssh/get-started). Limitez le premier test à un seul dépôt ou à un seul compte non de production.

Sur macOS ou Linux, définissez le socket à partir du guide de configuration de la plateforme et exécutez `ssh-add -l`. Sur Windows, utilisez la configuration de tube nommé prise en charge et vérifiez les clés disponibles via l’interface de l’Agent SSH 1Password ou un test SSH Windows documenté. Ne présentez pas `ssh-add -l` comme une commande de vérification multiplateforme.

Uniquement sur macOS ou Linux :

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Sortie attendue, non testée :** Sur macOS ou Linux, `ssh-add -l` liste les empreintes numériques de l’agent actif. Sur Windows, utilisez le test de tube nommé documenté ou l’interface de l’Agent SSH 1Password. Une lecture Git réussie renvoie une référence de commit. Le dépôt fictif ci-dessus doit être remplacé lors d’un test contrôlé.

La commande utilise un emplacement réservé pour le dépôt. Remplacez l’emplacement réservé uniquement lors d’un test contrôlé. **N’approuvez pas une invite pour une cible ou un processus que vous n’attendiez pas.**

### 5. Ajouter MCP après que le chemin SSH fonctionne

Vérifiez d’abord le client SSH et la cible sans MCP. Ajoutez ensuite un seul serveur MCP en lecture seule ou un connecteur local. Fournissez à l’agent un outil tel que `read_status` ou `prepare_command`. Ne commencez pas avec un outil de shell général.

La configuration MCP doit référencer les valeurs d'exécution via le mécanisme d'environnement pris en charge par le client. Le [guide de sécurité IA de 1Password](https://www.1password.dev/security-for-ai) décrit le remplacement des jetons de configuration MCP en texte brut par des variables d'environnement chargées depuis 1Password. **Conservez la référence ou le nom de variable dans la configuration. Excluez la valeur résolue de la transcription de l'agent.**

Cette section décrit une conception, et non une configuration MCP testée. Aucun client, serveur, transport, version ou fixture n'est fixé ici. Validez un serveur en lecture seule dans un profil de test distinct avant de connecter un agent à un système de production.

### 6. Enregistrer le résultat

Enregistrez la classe cible, le nom de l'outil, la décision d'approbation, l'empreinte de la clé publique, le résultat de la commande et le résultat du nettoyage. Omettez les valeurs secrètes. Marquez chaque sortie comme observée ou attendue.

**Résultat attendu, non testé :** L'agent lit l'état, propose une commande bornée, reçoit une approbation explicite pour la demande SSH, complète l'opération en lecture seule et produit un enregistrement sans texte de clé privée.

## Séquence de commandes synthétique

La séquence suivante montre l'ordre sans utiliser d'infrastructure réelle. Ces commandes sont des exemples uniquement. Elles n'ont pas été exécutées lors de la préparation de l'article.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Sortie attendue, non testée :**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

Le bloc de sortie est illustratif. Le bloc ne représente pas une exécution contre un compte 1Password, Bitbucket, un fournisseur Git ou un hôte distant. Un enregistrement de production doit stocker uniquement les métadonnées approuvées et un état de succès ou d'échec.

## Accès interactif versus non surveillé

| Mode d'accès | Identité | Chemin de la clé privée | Modèle d'approbation |
|---|---|---|---|
| **SSH interactif** | Compte humain via l'Agent SSH 1Password | La clé privée reste dans l'application 1Password | Un humain approuve un processus, une session terminal ou une demande |
| **Lecture planifiée** | Compte de service dédié | `op run` fournit des valeurs d'exécution restreintes | Politique du travail et portée du compte de service |
| **SSH planifié** | Identité d'automatisation dédiée | L'exportation de la clé reste une conception de dernier recours | Isolation du travail, durée de vie courte, restriction d'hôte et rotation |
| **Écriture par agent** | Identité humaine ou spécifique à la tâche | Dépend de l'intégration approuvée | Approbation humaine avant chaque modification définie |

*Ne planifiez pas un flux de travail autour d'une invite de l'Agent SSH interactif. Utilisez une conception d'automatisation distincte ou maintenez l'étape opérée par un humain.*

Pour les tâches non supervisées, créez un compte de service avec accès à un seul coffre-fort ou à un petit ensemble d’éléments. Attribuez à la tâche un objectif unique. Utilisez un dépôt ou un compte serveur dédié. Ajoutez la vérification de la clé hôte. Définissez une temporisation d’exécution. Journalisez les métadonnées des actions sans inclure de secrets. Révoquez ou faites pivoter l’identité après le test.

Si une tâche non supervisée a réellement besoin d’une clé privée SSH, utilisez une clé d’automatisation dédiée avec un compte distant restreint et une date de fin documentée. La récupération de la clé privée via `op read` exporte toujours le matériel de clé à travers une frontière de processus. Cette conception présente un rayon d’impact plus large que l’Agent SSH de 1Password. Privilégiez une identité de plateforme, un service de déploiement ou une autre identité de charge de travail lorsque la cible le prend en charge.

## Pourquoi les variables d’environnement en texte brut augmentent le risque

Les variables d’environnement maintiennent les secrets hors des fichiers sources, mais elles ne les rendent pas invisibles. Un processus enfant lit son environnement. L’inspection des processus, les gestionnaires de plantage, les sorties de débogage, la traçabilité du shell et les enregistrements de commandes copiés peuvent exposer les valeurs.

1Password documente `op run` comme méthode d’exécution pour charger des références dans un sous-processus. Utilisez `op run` pour les valeurs dont un processus a réellement besoin. Maintenez le processus enfant de courte durée et restreignez sa commande. Ne transmettez pas une clé privée via `SSH_PRIVATE_KEY`, `KEY` ou une variable similaire lorsque l’Agent SSH élimine le besoin d’exportation.

L’ordre plus sûr est le suivant :

1. **Utiliser l’Agent SSH** pour SSH interactif.
2. **Utiliser l’enregistrement de clé publique** pour Bitbucket ou le compte distant.
3. **Utiliser `op run`** pour un processus enfant non supervisé restreint.
4. **Utiliser `op read`** pour une seule valeur lorsqu’un processus enfant n’a pas besoin d’un environnement complet.
5. **Exporter une clé privée** uniquement après une exception écrite, un périmètre restreint, un plan de nettoyage et un plan de rotation.

## Tableau de décision

| Besoin | Cheminement privilégié | Raison d'arrêt ou de refonte |
|---|---|---|
| L'utilisateur exécute Git via SSH | Agent SSH 1Password | Arrêter si l'invite mentionne un processus ou une clé inattendus |
| Enregistrer une clé de dépôt | Lire ou préremplir la clé publique | Ne jamais copier la clé privée dans le service de dépôt |
| L'agent lit l'état du service | Outil MCP en lecture seule avec portée au niveau du système d'exploitation | Arrêter si l'outil expose un shell non restreint |
| L'agent propose une modification distante | Outil de planification suivi d'une approbation humaine | Arrêter si la cible, la commande ou le retour arrière est flou |
| Le travail lit un jeton d'API | Compte de service plus `op read` ou `op run` | Arrêter si le jeton entre dans le code source, les journaux ou un profil global |
| Le travail a besoin d'un accès SSH | Identité de charge de travail ou clé d'automatisation dédiée | Arrêter si le travail nécessite une clé personnelle ou un compte large |
| La configuration MCP a besoin d'un jeton | Référence d'exécution chargée par le client pris en charge | Arrêter si un jeton en texte brut est engagé dans la configuration |

## Gestion des pannes

**Invite de consentement SSH inattendue :** Refuser l'invite. Vérifier le nom du processus, la session du terminal, l'empreinte de la clé, la cible du dépôt et la clé d'hôte. Examiner la configuration du client SSH avant de réessayer.

**Absence de socket Agent SSH :** Confirmer que l'application de bureau 1Password est installée par une méthode prise en charge, que l'Agent SSH est activé et que le client utilise le socket spécifique à la plateforme. La [page officielle de l'Agent SSH](https://www.1password.dev/ssh/agent)] liste les exigences du système d'exploitation et les liens de configuration du socket.

**Échec de l'authentification par clé publique :** Vérifier la clé publique sélectionnée, le compte distant, l'autorisation du dépôt, la clé d'hôte et la configuration SSH. Utiliser une comparaison d'empreinte publique. Ne pas résoudre l'erreur en exportant une clé privée non liée.

**`op read` refuse l'accès :** Vérifier la portée du coffre-fort du compte de service, l'identifiant de l'élément, la référence du champ, l'état de connexion et le statut de l'élément. Réduire la référence à un seul élément approuvé. Ne pas élargir l'octroi du coffre-fort en première réponse.

**`op run` expose une valeur :** Arrêter le travail. Conserver uniquement l'enregistrement minimal de l'incident. Supprimer les journaux copiés et les fichiers temporaires conformément à votre procédure de rétention. Faire pivoter le secret ou la clé affecté. Examiner le traçage du shell, l'inspection des processus, les rapports de plantage et la rétention des transcriptions MCP.

**Comportement inattendu de l’outil MCP :** Traitez la sortie de l’outil comme des données non fiables. Arrêtez-vous avant d’exécuter les commandes suggérées par la sortie. Inspectez la source du serveur, la configuration, les autorisations et le transport. L’hôte MCP doit obtenir le consentement de l’utilisateur. La spécification fournit également des conseils aux implémenteurs concernant le consentement et les contrôles d’accès, mais le protocole ne remplace pas votre revue.

## Annulation et suppression

L’annulation commence par la suppression de l’accès, et non par la suppression de fichiers.

1. **Arrêtez l’agent ou le travail planifié.** Désactivez l’entrée du serveur MCP ou déconnectez le client.
2. **Verrouillez 1Password.** Mettez fin à la session d’autorisation SSH interactive.
3. **Supprimez la clé publique.** Supprimez la clé de test depuis Bitbucket, le dépôt ou le compte distant.
4. **Révoquez le compte de service.** Supprimez son accès au coffre-fort et invalidez son jeton.
5. **Supprimez l’élément Clé SSH de test** après avoir confirmé qu’aucun flux de travail approuvé n’utilise cet élément.
6. **Supprimez la configuration temporaire.** Supprimez les références de test, les substitutions de socket locales et les journaux générés.
7. **Examinez les preuves.** Confirmez que l’enregistrement de l’annulation ne contient aucune clé privée, aucun jeton et aucun déchargement d’environnement.

*La suppression d’un fichier local ne révoque pas une clé publique, un compte de service, un jeton en cache ou une autorisation distante. Supprimez chaque autorisation à sa source.*

## Dépannage

### L’agent demande une clé à chaque commande

Vérifiez l’étendue d’autorisation sélectionnée. L’approbation par requête est plus restrictive. Une session de terminal ou d’application peut s’être terminée. 1Password demande également à nouveau après un événement de verrouillage ou de fermeture.

### L’agent voit une clé privée dans sa transcription

Arrêtez le flux de travail et faites pivoter la clé. Inspectez la réponse du serveur MCP, la commande shell, le journal de débogage et l’enveloppe de l’outil. Remplacez les lectures de clés privées par l’utilisation de l’Agent SSH pour les tâches interactives. Pour les travaux, remplacez une clé personnelle par une identité dédiée et une exception documentée.

### Une liste de clés contient trop d’identités

L’Agent SSH 1Password expose les clés éligibles de ses coffres-forts configurés. Utilisez une configuration d’agent à portée limitée ou une configuration SSH spécifique à l’hôte. La [documentation de l’agent](https://www.1password.dev/ssh/agent) note également la limite de six clés du serveur OpenSSH.

### Une commande fonctionne manuellement mais échoue dans un travail

Comparez l’identité, l’étendue du coffre-fort, l’environnement, les données de clé d’hôte, le répertoire de travail et les hypothèses d’approbation. Une session 1Password interactive inclut le consentement humain. Un travail planifié ne l’inclut pas. Concevez le travail comme un mode d’accès distinct.

### Le serveur MCP est connecté mais la tâche échoue

La connexion ne prouve pas l'autorisation. Vérifiez la découverte des outils, les identifiants du serveur, le consentement du client, les autorisations du système d'exploitation, l'accès réseau et les autorisations côté cible dans des étapes distinctes. Maintenez le premier test en lecture seule.

## Étapes suivantes

Utilisez la spécification MCP actuelle du 2026-07-28 pour les nouvelles approbations. Tout lien vers la spécification du 2025-06-18 dans cet article est un contexte historique.

Commencez par un dépôt synthétique et un outil MCP en lecture seule. Enregistrez chaque résultat attendu comme non testé jusqu'à ce qu'un environnement contrôlé produise des preuves. Répétez ensuite le flux de travail avec une cible non de production, un opérateur nommé, une clé hôte vérifiée et un enregistrement écrit de la procédure de retour arrière.

Lisez la [référence CLI 1Password](https://www.1password.dev/cli/reference) pour les drapeaux de commande actuels. Lisez [Charger les secrets dans les scripts](https://www.1password.dev/cli/secrets-scripts) avant de créer une automatisation de compte de service. Lisez la [spécification MCP](https://modelcontextprotocol.io/specification/2026-07-28) avant d'approuver des outils provenant d'un nouveau serveur.

**Gardez l'SSH interactif approuvé par un humain. Gardez l'accès non supervisé séparé. Gardez les clés privées non lisibles chaque fois que la cible prend en charge l'authentification basée sur un agent.**
