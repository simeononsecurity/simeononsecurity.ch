---
title: "Tailscale Aperture : configurer des clients IA pour l’inférence et MCP en 2026"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Faites transiter les requêtes des modèles et les outils MCP par Tailscale Aperture. Configurez Codex, Claude Code, Claude Desktop, OpenCode et Hermes sur un autre appareil ou une autre passerelle."
genre: ["Intelligence artificielle", "Outils de développement", "Réseaux"]
tags: ["Tailscale Aperture", "Configuration Aperture", "Proxy IA", "Passerelle LLM", "Passerelle MCP", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "Proxy d’inférence IA", "API Responses", "API Anthropic Messages", "MCP distant", "HTTP Streamable", "Tailscale", "IA auto-hébergée", "Agents de programmation", "Configuration de client IA"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture relie les panneaux clients aux services de modèles et d’outils MCP par des routes distinctes, bleue pour l’inférence et verte pour les outils"
coverCaption: ""
---

## Introduction

Tailscale Aperture fournit aux clients IA une passerelle connectée au tailnet pour l’inférence de modèles et les outils Model Context Protocol (MCP). Chaque client doit emprunter une route correspondant à son protocole d’API. Les outils MCP utilisent un endpoint distinct, et les autorisations Aperture déterminent les modèles et connecteurs accessibles à chaque identité Tailscale.

Ce guide explique comment configurer Codex, Claude Code, Claude Desktop, OpenCode et Hermes sous macOS, Linux et Windows. Il présente les réglages de ligne de commande et de bureau, explique comment rechercher les ID de modèles accessibles à votre identité et inclut une consigne anonymisée réutilisable pour configurer un autre appareil ou une autre instance Aperture.

**Choix de route :** Les chemins des endpoints dépendent de votre passerelle et de chaque protocole d’API. Une route Responses telle que `/codex` ne traite ni le trafic Anthropic Messages ni le trafic MCP. Confirmez le nom d’hôte de la passerelle et la route d’inférence de chaque client. Consultez les ID de modèles via votre propre accès Aperture avant de modifier les réglages des clients.

## Points essentiels

- **Le trafic des modèles** nécessite la route d’API correspondant au protocole du client.
- **Le trafic MCP** utilise l’endpoint distinct `/v1/mcp`.
- **Les autorisations de la passerelle** doivent permettre à votre identité Tailscale d’utiliser chaque modèle et connecteur.
- **La configuration du client** prouve seulement que les réglages sont enregistrés. Vérifiez une vraie requête et un appel d’outil MCP.

## Fonctionnement des routes

| Objectif | Requête du client | Route Aperture | Service fourni par la route |
|---|---|---|---|
| Codex et modèles compatibles avec Responses | API OpenAI Responses | Généralement `/v1`. Un chemin personnalisé tel que `/codex` dépend du déploiement. | Inférence de modèles |
| Inférence de modèles Claude | API Anthropic Messages | URL de base de la passerelle. Aperture traite `/v1/messages` | Inférence compatible avec Claude |
| Outils MCP | MCP HTTP Streamable | `/v1/mcp` | Outils et ressources des connecteurs configurés |

{{< figure src="aperture-client-routes.webp" alt="Codex et Hermes empruntent une route Responses, Claude utilise Anthropic Messages, et les clients MCP utilisent la route distincte /v1/mcp pour accéder aux connecteurs Aperture" caption="L’inférence de modèles et le trafic MCP empruntent des endpoints Aperture distincts" >}}

**Racines des fournisseurs :** Aperture ajoute les chemins des requêtes client à l’URL de base du fournisseur. Définissez `baseurl` sur la racine de l’API du fournisseur. N’ajoutez pas `/v1` à une URL de base en amont lorsque le chemin entrant contient déjà `/v1`. Consultez la [référence de configuration Aperture](https://tailscale.com/docs/aperture/configuration) pour la construction des URL, l’enregistrement des modèles et les autorisations.

## Préparer la passerelle

**Avant toute modification,** demandez à un administrateur Aperture les valeurs suivantes :

- **Nom d’hôte de la passerelle :** Utilisez `http://` pour la plupart des clients connectés au tailnet. L’inférence de Claude Desktop exige `https://` avec un certificat de confiance.
- **Routes d’inférence :** OpenAI Responses et Anthropic Messages utilisent des formats de requête différents.
- **ID des modèles :** Recherchez les modèles accessibles à votre identité Tailscale avec l’endpoint ci-dessous. Utilisez les ID exacts renvoyés pour cette identité.
- **Authentification :** Vérifiez si le client envoie une clé API fictive ou un identifiant utilisateur.
- **Endpoint MCP :** Généralement `http://<APERTURE_HOST>/v1/mcp` pour les clients du tailnet. L’inférence Claude Desktop exige HTTPS avec un certificat de confiance.
- **Autorisations d’accès :** Vérifiez les droits sur les modèles et connecteurs associés à votre identité Tailscale.

**Accès réseau :** L’appareil client doit joindre la passerelle par le tailnet. Un nom d’hôte seul n’accorde aucun accès aux modèles ni aux outils. Aperture refuse l’accès en l’absence d’une autorisation correspondante pour le modèle ou le connecteur.

### Trouver les modèles accessibles à votre utilisateur

**Interrogez la liste des modèles** depuis un appareil connecté au même tailnet. Aperture utilise l’identité Tailscale de l’appareil et renvoie les modèles accordés à cet utilisateur, comme indiqué dans le [guide des autorisations de modèles](https://tailscale.com/docs/aperture/how-to/grant-model-access) :

```sh
# macOS ou Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, utilisez curl.exe pour éviter l’ancien alias curl
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**Lire le résultat :** Utilisez chaque `id` renvoyé comme ID de modèle. Vérifiez `metadata.provider.id` pour identifier le fournisseur Aperture. Choisissez un modèle qui prend en charge le format d’API du client. Par exemple, Claude Desktop exige un modèle Anthropic Messages. Le [répertoire des modèles](https://tailscale.com/docs/aperture/reference/chat) Aperture répertorie également les identifiants accessibles à l’utilisateur connecté.

**Modèles manquants :** Si un modèle attendu n’apparaît pas, demandez à un administrateur Aperture de vérifier la configuration du fournisseur et votre autorisation de modèle. L’endpoint ne permet pas aux utilisateurs de s’accorder eux-mêmes un accès.

**Schéma d’URL :** Tailscale recommande `http://` pour la plupart des clients connectés au même tailnet. WireGuard chiffre ce trafic. Claude Desktop exige `https://` et un certificat approuvé par le système d’exploitation. Utilisez le schéma indiqué pour chaque client ci-dessous.

### Ajouter un fournisseur d’inférence

**OpenAI Responses :** Ajoutez le fournisseur amont à Aperture et activez le format d’API utilisé par le client. Pour un fournisseur OpenAI, ajoutez un fragment de ce type :

```json
{
  "providers": {
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "models": ["<MODEL_ID>"],
      "compatibility": {
        "openai_chat": true,
        "openai_responses": true
      }
    }
  }
}
```

**Anthropic Messages :** Utilisez la racine d’API Anthropic, le format d’autorisation `x-api-key` et la compatibilité `anthropic_messages`. L’ID du modèle doit également figurer dans la liste `models` du fournisseur. Ajoutez un fragment de ce type :

```json
{
  "providers": {
    "anthropic": {
      "baseurl": "https://api.anthropic.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "authorization": "x-api-key",
      "models": ["<CLAUDE_MODEL_ID>"],
      "compatibility": {
        "anthropic_messages": true
      }
    }
  }
}
```

**Modifications de configuration :** Remplacez chaque valeur fictive par les valeurs de votre fournisseur amont. Ajoutez les fragments à la configuration Aperture existante. Conservez le reste du fichier actuel. Activez les indicateurs de compatibilité pour les API prises en charge par votre fournisseur.

**Autorisations d’accès :** Aperture contrôle l’accès de chaque utilisateur à chaque modèle ou connecteur. Accordez à chaque utilisateur Tailscale concerné uniquement les droits nécessaires. Cet exemple autorise un utilisateur à accéder à un modèle d’un fournisseur et à un connecteur :

```json
{
  "grants": [
    {
      "src": ["<TAILSCALE_USER>"],
      "app": {
        "tailscale.com/cap/aperture": [
          {"role": "user", "models": "openai/<MODEL_ID>"},
          {"connectors": ["teamtools/**"]}
        ]
      }
    }
  ]
}
```

**Autorisation de modèle :** Utilisez l’ID du fournisseur et l’ID du modèle dans le motif d’autorisation. Le [guide de configuration des connecteurs](https://tailscale.com/docs/aperture/connectors/get-started) présente la configuration actuelle `connectors.servers`. L’ancienne configuration de premier niveau `mcp.servers` est obsolète.

### Ajouter un connecteur MCP

**Connecteur MCP :** Aperture se connecte aux serveurs MCP amont et expose leurs outils sur `/v1/mcp` :

```json
{
  "connectors": {
    "servers": {
      "teamtools": {
        "protocol": "mcp",
        "url": "<UPSTREAM_MCP_ENDPOINT>"
      }
    }
  }
}
```

**URL du connecteur :** Utilisez l’endpoint MCP complet du serveur amont. Autorisez ensuite votre utilisateur Tailscale à accéder à `teamtools/**` ou à un motif d’outil plus restreint. La [référence du proxy MCP](https://tailscale.com/docs/aperture/mcp-server) explique l’endpoint unique du client et le comportement des connecteurs.

## Codex CLI et application de bureau

**Réglages partagés :** Codex CLI et l’application de bureau utilisent la même configuration. Sous macOS et Linux, modifiez `~/.codex/config.toml`. Sous Windows, modifiez `%USERPROFILE%\.codex\config.toml` (les shells qui développent le répertoire personnel acceptent également `~/.codex/config.toml`). La [présentation de l’application Codex](https://openai.com/index/introducing-the-codex-app/) indique que l’application de bureau reprend la configuration de Codex CLI. Les réglages utilisateur Codex se trouvent dans `~/.codex/config.toml`. La documentation des [principes de configuration](https://learn.chatgpt.com/docs/config-file/config-basic) décrit les champs fournisseur et MCP au niveau utilisateur. Ajoutez le fournisseur dans ce fichier, redémarrez l’application, puis vérifiez que le fournisseur et le modèle apparaissent dans l’interface.

```toml
model = "<MODEL_ID>"
model_provider = "aperture"

[model_providers.aperture]
name = "Aperture Proxy"
base_url = "http://<APERTURE_HOST>/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false
```

**Champs facultatifs :** Ces deux valeurs correspondent à une configuration fournisseur Codex. Conservez-les uniquement si votre passerelle et votre configuration Codex l’exigent. Le [guide Codex Aperture actuel de Tailscale](https://tailscale.com/docs/aperture/how-to/use-codex) les omet, utilise `wire_api = "responses"` et précise qu’Aperture injecte les identifiants amont. Utilisez l’URL Responses exacte fournie par l’administrateur de la passerelle. `/codex` est une route propre au déploiement. La route par défaut documentée par Tailscale est `/v1`.

**Configuration MCP :** Ajoutez le serveur à la même configuration utilisateur :

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Vérifier Codex :** Exécutez `codex mcp list`, démarrez une nouvelle session et inspectez `/mcp`. La liste des serveurs confirme l’enregistrement. Un outil affiché et un appel réussi confirment sa découverte et son exécution. La [référence de configuration Codex](https://learn.chatgpt.com/docs/config-file/config-reference) décrit les réglages utilisateur du fournisseur et de MCP.

## Claude Code CLI

**Protocole :** Claude Code utilise Anthropic Messages. Configurez le fichier de réglages global Claude Code pour pointer vers la passerelle Aperture compatible avec Anthropic. Utilisez `~/.claude/settings.json` sous macOS et Linux, ou `%USERPROFILE%\.claude\settings.json` sous Windows. Dans PowerShell, utilisez le chemin équivalent `$HOME\.claude\settings.json`. La route doit servir `/v1/messages`. Codex Responses utilise un protocole et une route différents. Tailscale recommande HTTP pour Claude Code sur le tailnet, car WireGuard chiffre la connexion.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Authentification du client :** Le guide client Aperture utilise une valeur fictive dans `apiKeyHelper`, car Aperture injecte l’identifiant amont. Pour transmettre un abonnement Claude, le fournisseur Anthropic Aperture doit transférer l’identifiant Claude de l’utilisateur. Dans ce cas, laissez `ANTHROPIC_API_KEY` et `ANTHROPIC_AUTH_TOKEN` non définies. Ces variables remplacent l’identifiant d’abonnement. Consultez les instructions actuelles [Claude Code avec Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-code) correspondant à votre version de Claude Code et le [guide des passerelles Anthropic](https://code.claude.com/docs/en/llm-gateway-connect) pour les options d’authentification.

**MCP sur HTTP :** Ajoutez l’endpoint avec ces commandes :

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Vérifier Claude Code :** Démarrez une session et exécutez `/mcp` pour confirmer la connexion. Dans sa [documentation MCP](https://code.claude.com/docs/en/mcp), Anthropic recommande HTTP pour les serveurs MCP distants.

## Interface graphique Claude Desktop

**Réglages distincts :** Claude Desktop dispose d’un écran d’inférence tiers. Ce réglage fait passer les requêtes de modèles Claude Desktop par Aperture. La configuration MCP est une étape distincte.

1. Dans Claude Desktop pour macOS ou Windows, sélectionnez **Aide > Dépannage > Activer le mode développeur**. Dans la bêta Linux, utilisez le même menu s’il existe. Redémarrez l’application si demandé. Si le menu est absent, mettez Claude Desktop à jour et consultez les notes de version de votre plateforme.
2. Sélectionnez **Développeur > Configurer l’inférence tierce**.
3. Choisissez **Passerelle** pour le **Type de connexion** et **Clé API statique** pour le **Type d’identifiant**.
4. Saisissez `https://<APERTURE_HOST>` comme **URL de base de la passerelle**. Utilisez le nom d’hôte complet couvert par un certificat TLS de confiance.
5. Saisissez une valeur fictive non vide, par exemple `aperture`, comme clé de passerelle. Aperture ignore cette valeur et s’authentifie via le tailnet.
6. Laissez vides les en-têtes d’inférence personnalisés.
7. Ajoutez un modèle activé avec un ID exact renvoyé par `GET /v1/models` pour votre identité Tailscale. Filtrez les modèles Anthropic Messages. Saisissez manuellement son ID, son nom d’affichage et son alias de niveau facultatif. Claude Desktop ne recherche pas les modèles sur cet écran.
8. Sélectionnez **Enregistrer les modifications**, puis **Appliquer les modifications**. Quittez Claude Desktop et rouvrez-le.

**Vérification du protocole :** Le [guide Claude Desktop Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) indique que Claude Desktop utilise Anthropic Messages sur `/v1/messages`. N’indiquez pas la route Codex `/codex` et ne choisissez pas un type de connexion compatible OpenAI.

### Connecter Claude Desktop à MCP

**Accès MCP privé :** Exécutez un pont local de type stdio sur le même ordinateur que Claude Desktop. Ajoutez ceci à la configuration MCP locale de Claude Desktop :

```json
{
  "mcpServers": {
    "aperture": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://<APERTURE_HOST>/v1/mcp"]
    }
  }
}
```

**Fonctionnement du pont :** Le processus local atteint Aperture par la connexion Tailscale de l’ordinateur. Utilisez le chemin de configuration de votre système : macOS, `~/Library/Application Support/Claude/claude_desktop_config.json` ; Windows, `%APPDATA%\Claude\claude_desktop_config.json` ; bêta Linux, ouvrez **Paramètres > Développeur > Modifier la configuration** et utilisez le chemin ouvert par Claude Desktop. Le chemin Linux dépend du paquet. Redémarrez Claude Desktop, inspectez la liste des connecteurs et exécutez un appel d’outil sans risque. Le [projet `mcp-remote`](https://github.com/punkpeye/mcp-remote) décrit ce pont local-distant.

**Connecteurs distants :** Le flux Paramètres > Connecteurs d’Anthropic nécessite un serveur distant accessible depuis le service Anthropic. Un nom d’hôte limité au tailnet est privé à vos appareils ; utilisez donc le pont local pour l’endpoint privé. Si vous exposez un service MCP public, configurez son authentification et ses autorisations avant de l’ajouter comme connecteur cloud. Consultez le [guide des connecteurs MCP distants](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) d’Anthropic.

## OpenCode CLI et application de bureau

**Réglages partagés :** OpenCode CLI et l’application de bureau lisent la même configuration OpenCode. La documentation actuelle OpenCode V2 utilise la map `providers` pour les fournisseurs personnalisés et place les serveurs MCP dans `mcp.servers`. Cet exemple utilise l’endpoint de chat compatible OpenAI sur `/v1`. Vérifiez la prise en charge d’OpenAI Chat Completions par votre fournisseur Aperture avant d’utiliser cette route de modèle.

**Configuration globale :** Sous macOS et Linux, modifiez `~/.config/opencode/opencode.json`. Sous Windows, utilisez `%USERPROFILE%\.config\opencode\opencode.json`. Ajoutez un fournisseur compatible OpenAI et remplacez `<MODEL_ID>` par l’ID exact du modèle Aperture. OpenCode accepte aussi `opencode.jsonc` dans le même dossier pour les commentaires. La [référence de configuration](https://opencode.ai/docs/config/) explique la priorité entre réglages globaux et réglages du projet.

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aperture/<MODEL_ID>",
  "providers": {
    "aperture": {
      "env": ["APERTURE_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://<APERTURE_HOST>/v1"
      },
      "models": {
        "<MODEL_ID>": { "modelID": "<MODEL_ID>" }
      }
    }
  },
  "mcp": {
    "servers": {
      "aperture": {
        "type": "remote",
        "url": "http://<APERTURE_HOST>/v1/mcp",
        "oauth": false
      }
    }
  }
}
```

**Authentification du client :** `oauth: false` ignore le flux OAuth par défaut d’OpenCode. Aperture identifie l’appelant par Tailscale. OpenCode exige aussi une entrée d’authentification du fournisseur ; définissez donc `APERTURE_API_KEY=-` dans l’environnement local. L’application de bureau doit également recevoir cette variable. Si elle n’hérite pas de l’environnement de votre shell, exécutez `/connect` dans l’application et saisissez `-` pour Aperture. Ne placez pas la clé du fournisseur amont dans ce fichier. Le [guide des fournisseurs](https://opencode.ai/docs/providers/) et le [guide MCP](https://opencode.ai/docs/mcp-servers/) OpenCode décrivent le format actuel. Exécutez `opencode mcp list` pour vérifier le serveur, puis utilisez `/mcps` dans l’application pour consulter son état.

## Hermes CLI et application de bureau

**Réglages partagés :** Hermes Agent stocke les fournisseurs nommés et les serveurs MCP dans `~/.hermes/config.yaml` sous macOS et Linux. Les installations Windows natives utilisent `%LOCALAPPDATA%\hermes\config.yaml`. Exécutez `hermes config path` pour confirmer le fichier actif sur votre système. `HERMES_HOME` peut remplacer l’emplacement par défaut. Hermes Desktop local utilise le même dossier Hermes et le même profil que la CLI. Si Desktop se connecte à une passerelle Hermes distante, configurez Aperture sur la machine qui exécute Hermes, puis vérifiez que le serveur rejoint le tailnet. Consultez le [guide Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) pour les configurations locales et distantes.

**Fournisseur Responses :** Ajoutez un fournisseur nommé. La valeur `api` doit correspondre à l’endpoint Responses de votre instance Aperture :

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Ajoutez key_env uniquement si votre configuration Aperture exige une clé client.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Choix du protocole :** Pour OpenAI Chat Completions, définissez `transport: chat_completions`. Pour Anthropic Messages, choisissez `transport: anthropic_messages` et utilisez l’URL de passerelle Anthropic Messages. Le guide actuel des [fournisseurs](https://hermes-agent.nousresearch.com/docs/integrations/providers) indique que Hermes utilise les champs `api`, `transport` et `default_model` d’un fournisseur nommé.

**Configuration MCP :** Ajoutez Aperture MCP dans le même fichier YAML :

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Vérifier Hermes :** Exécutez `hermes mcp` et inspectez chaque connexion dans le sélecteur interactif de serveurs. Desktop local expose le même profil de configuration. Hermes documente les [serveurs HTTP MCP distants](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) et la [référence complète de configuration MCP](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Vérifier les deux chemins

**Effectuez des vérifications distinctes** pour l’inférence de modèles et MCP :

1. Confirmez que l’appareil est connecté à Tailscale et peut joindre la passerelle. Pour Claude Desktop, vérifiez que la passerelle présente un certificat TLS de confiance.
2. Envoyez une courte consigne depuis chaque client configuré. Vérifiez qu’une requête correspondante apparaît dans la liste des sessions Aperture.
3. Confirmez que l’ID de modèle choisi correspond à un modèle autorisé pour votre identité Tailscale.
4. Ouvrez l’écran d’état MCP de chaque client ou utilisez sa commande de liste. Vérifiez que le serveur Aperture se connecte et expose les outils attendus.
5. Appelez un outil en lecture seule. Comparez le contenu renvoyé à la source amont.
6. Consultez les journaux Aperture si l’appel au modèle ou à l’outil échoue. Un fichier de configuration enregistré ne prouve pas qu’une requête a réussi.

| Symptôme | Vérification |
|---|---|
| La requête de modèle renvoie 404 ou 405 | Vérifiez que l’endpoint du client utilise la bonne route et le bon protocole. Ne réutilisez pas `/codex` pour Anthropic Messages ou MCP. |
| Modèle indisponible | Interrogez `/v1/models` en tant qu’utilisateur Tailscale prévu. Vérifiez la présence de l’ID exact et la compatibilité du format d’API avec le client. Demandez à un administrateur de vérifier les fournisseurs ou autorisations manquants. |
| Requête non autorisée | Vérifiez si le client exige une valeur fictive, un jeton bearer ou le transfert d’abonnement. Ne copiez jamais une clé fournisseur amont dans un fichier de projet public. |
| Serveur MCP répertorié, mais aucun outil visible | Vérifiez `/v1/mcp`, l’état du connecteur, ses autorisations et le chemin réseau entre le client et Aperture. |
| Claude Desktop ne se connecte pas à une URL MCP privée | Exécutez un pont local comme `mcp-remote` ou utilisez un connecteur public approuvé avec une authentification adaptée. |

## Recréer la configuration sur un autre appareil

**Nouvel appareil :** Installez le même client et connectez d’abord l’appareil au tailnet. Interrogez `/v1/models` depuis ce nouvel appareil pour connaître les modèles autorisés à son identité Tailscale. Copiez la structure de configuration et conservez les identifiants localement. Remplacez `<APERTURE_HOST>`, `<MODEL_ID>` et `<UPSTREAM_MCP_ENDPOINT>` par les valeurs de l’instance Aperture cible. Utilisez un endpoint distinct pour chaque protocole d’API, puis configurez le chemin `/v1/mcp` pour les outils. Enfin, vérifiez une requête de modèle et un appel d’outil MCP.

**Plusieurs passerelles :** Utilisez une configuration distincte pour chaque instance Aperture. Un appareil nécessite un endpoint Responses pour Codex et Hermes, un endpoint Anthropic Messages pour Claude et l’endpoint d’agrégation MCP pour les outils. Enregistrez les identifiants API dans le coffre local de chaque client ou dans une variable d’environnement. Ne copiez pas les clés API dans des fichiers partagés `config.toml`, `opencode.json`, `config.yaml` ou dans un dépôt public.

## Consigne Aperture réutilisable

**Copiez cette consigne anonymisée** dans votre assistant de programmation. Remplacez les valeurs fictives par les détails de votre passerelle. L’assistant doit interroger Aperture en tant que votre identité Tailscale avant de choisir les ID de modèles.

```text
Configure ma passerelle Tailscale Aperture existante et les clients IA installés sur cet appareil.

Clients concernés : Codex CLI et bureau, Claude Code, Claude Desktop, OpenCode CLI et bureau, Hermes CLI et bureau.

Commence par détecter si cet appareil utilise macOS, Linux ou Windows, identifier le shell actif (par exemple zsh, bash ou PowerShell) et utiliser partout les chemins et la syntaxe de commandes de cette plateforme. Inspecte d’abord la passerelle actuelle, la connexion Tailscale, les versions des clients et leurs réglages existants. Consulte la documentation officielle actuelle. Préserve les réglages sans rapport et sauvegarde chaque fichier avant modification. Ne devine pas les noms d’hôte, les ID de modèles, les routes d’API ou les identifiants. Conserve les clés des fournisseurs amont dans Aperture, jamais dans les fichiers client ni dans ce dépôt.

Recherche les modèles disponibles depuis cet appareil connecté à Tailscale :
1. Interroge `http://<APERTURE_HOST>/v1/models` en utilisant l’identité Tailscale de mes clients. Utilise l’URL personnalisée documentée pour la liste des modèles de la passerelle si elle diffère.
2. Lis les champs `id` et `metadata.provider.id` de chaque modèle. Cette liste reflète les modèles autorisés pour mon identité. Ne remplace pas la liste par celle de l’administrateur et n’invente pas d’ID.
3. Fais correspondre la compatibilité d’API de chaque modèle aux clients. Codex utilise OpenAI Responses. Les clients Claude utilisent Anthropic Messages. OpenCode et Hermes exigent un fournisseur et un transport compatibles configurés.
4. Réutilise autant que possible le modèle par défaut existant du client. Si un client a besoin d’une valeur par défaut et que je n’ai aucune préférence, présente-moi les modèles compatibles et demande-moi de choisir. Claude Desktop exige la saisie manuelle de l’ID exact du modèle.
5. Si l’endpoint ne renvoie aucun modèle adapté, vérifie la configuration du fournisseur et les autorisations uniquement si j’ai les droits d’administration. Sinon, indique quel accès modèle un administrateur doit ajouter. Ne t’accorde aucun accès.

Localise le déploiement Aperture et la source de sa configuration. Ne suppose pas de chemin de fichier et ne remplace pas toute la configuration. OpenAI Responses exige `openai_responses`. Les clients Anthropic exigent `anthropic_messages`. Les connecteurs MCP utilisent la configuration actuelle `connectors.servers` et les clients se connectent via `/v1/mcp`.

Avant de modifier une passerelle partagée, prépare le diff minimal pour les fournisseurs, connecteurs et autorisations. Applique-le uniquement si j’ai les droits d’administration et si cette demande autorise les changements de passerelle. Si je n’ai pas ces droits, indique les changements exacts proposés au propriétaire de l’instance. Ne crée pas d’autorisation et n’en élargis aucune sans l’autorisation explicite du propriétaire. Préserve tous les réglages existants de la passerelle.

Configure chaque client installé avec son format officiel actuel et son emplacement propre au système d’exploitation :
- Codex CLI et bureau partagent `~/.codex/config.toml` sous macOS/Linux et `%USERPROFILE%\.codex\config.toml` sous Windows. Configure le fournisseur Aperture, un modèle compatible, `wire_api = "responses"` et MCP dans `mcp_servers`.
- Claude Code utilise `ANTHROPIC_BASE_URL` et MCP distant par HTTP. Utilise `~/.claude/settings.json` sous macOS/Linux et `%USERPROFILE%\.claude\settings.json` sous Windows.
- Claude Desktop utilise le mode développeur, Configurer l’inférence tierce, Passerelle, Clé API statique, une URL HTTPS de passerelle avec certificat de confiance et un ID modèle trouvé pour mon utilisateur. Utilise un pont local `mcp-remote` pour MCP privé sur le tailnet. Cherche la configuration MCP dans Paramètres > Développeur > Modifier la configuration lorsque disponible. Sinon, utilise le chemin documenté pour le système détecté.
- OpenCode utilise le schéma V2 actuel `providers` et `mcp.servers`. Sa configuration globale se trouve dans `~/.config/opencode/opencode.json` sous macOS/Linux et `%USERPROFILE%\.config\opencode\opencode.json` sous Windows. Définis `oauth: false` pour le MCP Aperture. Utilise une clé API fictive locale si nécessaire.
- Hermes utilise un fournisseur nommé, un transport correspondant à l’API du modèle et `mcp_servers`. Utilise `~/.hermes/config.yaml` sous macOS/Linux. Sous Windows, vérifie `hermes config path`, généralement `%LOCALAPPDATA%\hermes\config.yaml`. Vérifie si Hermes Desktop partage le profil Hermes local.

Utilise HTTP pour le trafic tailnet lorsque le client le prend en charge. L’inférence de Claude Desktop exige HTTPS avec un certificat de confiance. Utilise `/v1` sauf si cette passerelle documente une autre route.

Redémarre les clients configurés. Vérifie une requête de modèle par client dans Aperture et un appel d’outil MCP inoffensif en lecture seule. Indique les modèles trouvés pour mon identité, les clients et fichiers modifiés, les résultats de vérification et les éventuelles actions d’administration restantes. N’installe aucun logiciel, n’expose pas la passerelle au public, ne fais aucun commit et ne publie rien.
```

## Conclusion

Une configuration Aperture fonctionnelle repose sur trois éléments : une passerelle accessible, une route modèle correspondant au protocole du client et les autorisations nécessaires pour les modèles et connecteurs MCP. Les mêmes modèles de configuration conviennent à macOS, Linux et Windows, mais chaque client stocke ses réglages dans un emplacement propre à son système d’exploitation.

Recherchez les ID de modèles en utilisant l’identité Tailscale qui les utilisera. Configurez séparément l’inférence de modèles et `/v1/mcp`, puis vérifiez une vraie requête et un appel d’outil en lecture seule. Lors du passage à un autre appareil ou à une autre instance Aperture, réutilisez la structure de ce guide, confirmez les routes et autorisations de cette instance et gardez les identifiants dans le coffre local.

## Étapes suivantes

**Mise en pratique de MCP :** Pour distinguer un serveur enregistré d’un appel d’outil vérifié, lisez [Configuration d’un serveur MCP : autorisations, tests d’outils et suppression sûre](/articles/effective-ai-mcp-server-setup/). Pour l’architecture auto-hébergée plus générale, consultez [Flotte d’agents IA hybride : Tailscale, LiteLLM et Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).
