---
title: "Claude Cowork et Claude Code avec des modèles locaux : guide de configuration 2026"
date: 2026-09-22
lastmod: 2026-11-12
toc: true
draft: false
description: "Configurez Ollama avec Claude Desktop et Claude Code via une API compatible avec Anthropic. Découvrez les modèles et les fonctions réservées au cloud en 2026."
genre: ["IA locale", "Outils de programmation IA", "IA auto-hébergée", "Outils pour développeurs", "Confidentialité", "Modèles open source", "Automatisation", "Matériel pour IA"]
tags: ["claude cowork", "claude code", "modèles locaux claude desktop", "ollama claude code", "anthropic base url", "anthropic_auth_token", "modèle local claude code", "utiliser claude hors ligne", "agent de programmation IA local", "ollama launch claude", "claude desktop ollama", "programmation llm locale", "programmation IA privée", "programmation IA hors ligne", "agent IA local", "qwen3.8", "modèle cloud glm", "modèles avec appels d'outils", "configurer claude code", "claude code gratuit", "claude sans clé API", "fenêtre de contexte d'un modèle local", "llama.cpp", "ollama cloud", "confidentialité de la programmation IA", "IA isolée du réseau", "outils IA devops"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "Espace de travail moderne avec un ordinateur affichant une interface de programmation, une tablette et des enceintes connectées sur un fond bleu foncé aux accents lumineux colorés."
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Les outils agentiques de Claude fonctionnent désormais avec des modèles installés sur votre propre matériel, sans clé API, abonnement ni données qui quittent votre machine.** Ollama expose une API compatible avec Anthropic à laquelle Claude Code et Claude Desktop se connectent en quelques commandes.

*De nombreux guides omettent un détail important. Ils présentent Claude Cowork, puis donnent des étapes qui configurent l'outil en ligne de commande. Il s'agit de deux intégrations distinctes, et une seule donne accès à Cowork.*

Ce guide présente séparément les deux parcours, la variable d'environnement que les tutoriels populaires oublient, les modèles adaptés à chacun en septembre 2026 et les fonctionnalités qui restent réservées au cloud, quelle que soit votre configuration.

**À la fin du guide :** vous saurez quelle intégration choisir, vous la connecterez par le parcours Ollama documenté et vous vérifierez le point de terminaison avec un test d'appel d'outil. L'inférence locale garde les requêtes du modèle sur votre machine uniquement si vous choisissez un modèle local et évitez les fonctions liées au cloud.

## Réponse rapide

**Ollama se connecte à Claude de deux façons distinctes. Choisir la mauvaise est la raison la plus courante d'obtenir un terminal fonctionnel sans Cowork après avoir suivi un guide.**

| Intégration | Fonctions disponibles | Parcours de configuration | Plateforme |
|---|---|---|---|
| **Claude Desktop** | Cowork, sous-agents, recherche Web, mode automatique | Application Ollama, puis **Apps** et **Connect Claude** | **macOS uniquement** |
| **Claude Code** | Agent de programmation CLI avec appels d'outils et modification de fichiers | `ollama launch claude` ou variables d'environnement | macOS, Linux, Windows |

**Pour Cowork, utilisez l'intégration Claude Desktop.** Elle se configure dans l'interface graphique de l'application Ollama et fonctionne uniquement sur macOS. La prise en charge de Windows est annoncée pour plus tard.

**Pour un agent dans le terminal, utilisez Claude Code.** Une seule commande suffit.

*Les deux sont gratuits. Seuls le matériel et l'électricité coûtent quelque chose.*

## Deux intégrations distinctes

La confusion commence par les noms. **Claude Cowork est une fonctionnalité de Claude Desktop**, pas une application séparée ni un autre nom pour Claude Code.

La documentation d'Ollama les décrit sur deux pages et sous deux rubriques différentes. Claude Desktop figure dans **Assistants**, avec OpenClaw et Hermes. Claude Code se trouve dans **Coding**, avec OpenCode, Cline et Codex CLI.

Cette différence compte, car la configuration n'a rien à voir :

- **Claude Desktop** se configure dans l'application Ollama. Vous n'avez pas à modifier le profil du shell.
- **Claude Code** se configure avec des variables d'environnement ou une seule commande de lancement.

Un guide qui demande d'exporter `ANTHROPIC_BASE_URL` puis d'exécuter `claude` configure l'outil en ligne de commande. Si vous vous attendiez à l'expérience de bureau Cowork, **votre configuration n'est pas défectueuse. Vous avez configuré un autre produit.**

## Configurer Claude Desktop et Cowork

Ce parcours passe par l'application Ollama, pas par le terminal.

### Prérequis

- **Ollama installé** sous macOS. La prise en charge de Windows est annoncée pour plus tard.
- **Un modèle déjà téléchargé** pour une utilisation locale. Pour un modèle cloud, connectez-vous à Ollama et activez les modèles cloud. Certains demandent un abonnement payant.
- **Claude installé.** S'il manque, Ollama propose de le télécharger pendant la configuration.

### Étapes

1. Ouvrez Ollama et sélectionnez **Apps**.
2. Sélectionnez **Connect Claude**.
3. Suivez les instructions. Installez Claude si la demande apparaît, puis redémarrez-le lorsqu'on vous le demande.

C'est tout. Pour changer de modèle ensuite, ouvrez **Ollama Settings**, allez dans **Apps**, choisissez les modèles, puis sélectionnez **Restart Claude**.

### Fonctions disponibles

La documentation d'Ollama indique que cette intégration prend en charge quatre fonctions :

- **Cowork**, pour effectuer des tâches difficiles
- **Sous-agents**, pour répartir les tâches importantes entre plusieurs agents
- **Web search**, fourni par défaut via Ollama
- **Auto mode**, qui laisse l'agent décider quand demander l'autorisation avant d'apporter des modifications

*Cowork figure dans cette liste. Cette intégration le prend en charge, contrairement à celle en ligne de commande.*

### Déconnexion

La déconnexion restaure la configuration précédente de Claude. La modification n'est donc pas destructive.

- Dans l'interface, ouvrez **Apps**, déconnectez Claude, puis redémarrez-le si la demande apparaît.
- Dans un terminal, exécutez `ollama launch claude-desktop --restore`.
- **Quitter Ollama lorsque Claude est connecté restaure également sa configuration habituelle.** Laissez Ollama ouvert pour conserver la configuration locale.

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Diagramme montrant l'application Ollama connectée à Claude Desktop depuis le panneau Apps, le choix du modèle dans les paramètres Ollama et le retour à la configuration initiale" >}}

## Configurer Claude Code depuis la CLI

La plupart des guides couvrent ce parcours. C'est le bon choix pour travailler dans un terminal.

### Méthode en une commande

```bash
ollama launch claude
```

La commande définit les variables d'environnement requises, dirige Claude Code vers votre instance locale d'Ollama et lance le programme. Choisissez un modèle dans la liste et appuyez sur Entrée. Pour sélectionner le modèle à l'avance, ajoutez l'option :

```bash
ollama launch claude --model qwen3.5
```

*Le wrapper configure l'environnement à votre place. Lisez tout de même la section suivante, car savoir ce qu'il définit aide à résoudre les problèmes.*

### Définir les variables d'environnement manuellement

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**La deuxième ligne manque dans beaucoup de guides populaires.** Définir `ANTHROPIC_API_KEY` comme chaîne vide empêche une vraie clé déjà présente dans l'environnement de perturber la connexion locale. Si un guide publié omet cette ligne, les lecteurs qui ont déjà exporté une clé rencontrent une erreur difficile à comprendre.

Pour éviter de modifier le profil du shell, passez toutes les valeurs directement dans la commande :

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

Deux précisions de la documentation officielle :

- **`ANTHROPIC_AUTH_TOKEN` porte l'authentification bearer.** C'est pourquoi sa valeur littérale est `ollama` en mode local.
- **Les fichiers de paramètres de Claude prennent le dessus sur les variables du shell.** Si la connexion se comporte bizarrement après l'export de nouvelles valeurs, vérifiez ces paramètres puis exécutez `/status` dans Claude Code pour voir le point de terminaison actif.

### Connexion directe à Ollama Cloud

Vous n'avez pas besoin d'installer Ollama pour ce parcours. Définissez une clé API et indiquez à Claude Code le point de terminaison hébergé par Ollama :

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**Ce parcours comporte une limite.** Selon la documentation d'Ollama, la recherche Web hébergée et le contrôle avancé des outils ne sont pas entièrement pris en charge. Le chat de base, la modification de fichiers et les appels d'outils fonctionnent avec les modèles compatibles.

## Choix des modèles en septembre 2026

L'offre de modèles a beaucoup évolué en 2026. Les conseils publiés au printemps méritent une nouvelle vérification.

| Modèle | Type | Contexte | Pourquoi le choisir |
|---|---|---|---|
| **Qwen3.8 27B** | Local, 18 Go | 256K | Meilleur modèle local polyvalent du moment, avec vision, appels d'outils et réglage du mode de réflexion |
| **Qwen3 Coder Next** | Local, MoE 80B au total / 3B actifs | 256K | Conçu pour les agents de programmation actifs en permanence, avec un mode rapide sans réflexion |
| **Qwen3.6 35B A3B** | Local, MoE 35B / 3B actifs | 262K | Licence Apache 2.0 et efficacité avec peu de mémoire |
| **kimi-k2.7-code:cloud** | Cloud | Élevé | Modèle cloud orienté programmation qui ne demande aucun matériel local |
| **glm-5.3-flash** | Cloud | Élevé | Premier modèle proposé dans la documentation d'Ollama |

**Commencez par Qwen3.8 27B si vous avez assez de mémoire.** Il fonctionne localement avec une fenêtre de contexte de 256K, une vision native, des appels d'outils et un mode de réflexion activable pour chaque requête. Une carte d'au moins 24 Go en fait un outil quotidien confortable.

**Choisissez un modèle cloud si vous n'avez pas cette capacité.** Essayer Claude Code avec un modèle hébergé ne coûte rien et élimine la question du matériel, mais votre code quitte la machine.

### Attention aux modèles ternaires

Dans notre **[guide sur l'IA locale](/articles/local-ai-2026-build-your-rig-now/)**, nous expliquons que Bonsai 2 27B ternaire exécute un modèle complet de 27B dans **5,53 Gio**. La solution semble tentante ici aussi.

**Ce modèle ne fonctionne pas avec ce parcours.** Les noyaux ternaires sont intégrés au fork llama.cpp de Prism ML, et Ollama standard ne sait pas charger ces fichiers. Une commande comme `ollama launch claude --model Ternary-Bonsai-2-27B` échoue avant le début de l'inférence. Pour Claude Code, utilisez le paquet Qwen3.8 27B standard. Gardez les paquets ternaires pour un moteur compatible.

*Ici, la simplicité et l'efficacité maximale mènent à des choix différents. Les outils intégrés attendent un fichier GGUF standard.*

## Réglez le contexte sur 64K avant d'accuser le modèle

La documentation d'Ollama donne une instruction directe pour les dépôts : choisissez un modèle et **réglez sa fenêtre de contexte sur 64K ou plus**, en l'augmentant pour les dépôts plus grands.

Claude Code place les fichiers, les différences et la sortie des commandes dans la fenêtre de contexte. Avec une petite valeur par défaut, elle se remplit au milieu d'une tâche. Le problème ressemble alors à une difficulté de raisonnement, mais vient du réglage.

| Contexte | Utilisation |
|---|---|
| Moins de 32K | Modification d'un seul fichier et questions rapides |
| **64K** | Travail sur plusieurs fichiers dans un dépôt modeste |
| 128K | Dépôts plus grands et longues sorties de commandes |
| 256K | Fenêtre complète de Qwen3.8 27B |

*Si Claude Code perd le fil au milieu d'une tâche, vérifiez le contexte avant de changer de modèle.*

## Vérifier les appels d'outils en une commande

Les appels d'outils distinguent un agent d'un générateur de texte. Vérifiez leur fonctionnement au lieu de le supposer.

Une fois Claude Code lancé, demandez-lui :

```text
Lis le répertoire actuel et liste tous les fichiers
```

**S'il affiche de vrais fichiers, les appels d'outils fonctionnent.** S'il répond qu'il lirait le dossier et décrit ce qu'il s'attend à y trouver, la fonction n'est pas reliée. Vous parlez à un modèle de chat accompagné d'une consigne de programmation, pas à un agent. Aucun prompt supplémentaire ne résoudra ce problème.

Vérifiez les causes dans cet ordre :

1. **Passez à un modèle dont la prise en charge des outils est confirmée.** Tous les modèles ne l'offrent pas et le nombre de paramètres ne permet pas de le savoir.
2. **Vérifiez que l'environnement pointe vers Ollama.** Exécutez `ollama --version` et confirmez que `ANTHROPIC_BASE_URL` désigne votre point de terminaison local.
3. **Exécutez `/status` dans Claude Code.** Une URL de base ou des identifiants dans les paramètres de Claude prennent le dessus sur les variables du shell que vous venez d'exporter.

## Fonctions réservées au cloud

Connaissez cette limite avant de reconstruire un flux de travail autour de l'inférence locale.

| Fonction | Modèles locaux | Cloud |
|---|---|---|
| Chat et modification de fichiers | Oui | Oui |
| Appels d'outils | Selon le modèle | Oui |
| Sous-agents | Oui | Oui |
| Recherche Web | Fournie par Ollama | Oui |
| **Cowork** | Via l'intégration Claude Desktop | Oui |
| Mode automatique | Via l'intégration Claude Desktop | Oui |
| Prompts planifiés | Via `/loop` dans Claude Code | Oui |

Trois limites concernent l'utilisation locale :

- **Le raisonnement sur plusieurs fichiers se dégrade avant la vitesse.** Un modèle local gère bien un fichier, assez bien trois fichiers et mal un dépôt entier. Adaptez la taille des tâches.
- **Certains modèles cloud demandent un abonnement Ollama payant.** Il faut aussi être connecté et les avoir activés.
- **La connexion directe au cloud limite certaines fonctions.** Sans installation locale, la recherche Web hébergée et le contrôle avancé des outils ne sont pas entièrement pris en charge.

*L'inférence locale convient aux tâches délimitées et vérifiables, moins aux travaux vastes et ambigus. Organisez votre travail en tenant compte de cette limite.*

## Automatiser

Deux fonctions vont au-delà de l'utilisation interactive.

### Exécutions sans interface pour les scripts et la CI

L'option `--yes` ignore les sélecteurs interactifs et télécharge le modèle si nécessaire. Elle nécessite `--model`; tout ce qui suit `--` est transmis directement à Claude Code :

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Vérifiez les permissions.** Claude Code demande une confirmation avant la plupart des actions. Une exécution sans interface nécessite donc des règles de permission configurées ou un environnement isolé. Ne dirigez pas un agent sans supervision vers un dépôt auquel vous tenez.

### Prompts planifiés avec `/loop`

Dans une session Claude Code, `/loop` exécute périodiquement un prompt ou une commande slash :

```text
/loop 30m Vérifie mes PR ouvertes et résume leur état
/loop 1h Recherche les dernières actualités de l’IA et résume les évolutions importantes
/loop 15m Vérifie les nouveaux problèmes GitHub et classe-les par priorité
```

*La commande fonctionne tant que la session reste ouverte. Ce n'est pas un démon en arrière-plan et elle s'arrête avec la session.*

## Dépannage

| Symptôme | Cause probable | Solution |
|---|---|---|
| **Connexion refusée** | Ollama n'est pas lancé | Exécutez `ollama serve`, puis vérifiez avec `curl http://localhost:11434/api/tags` |
| **Le modèle décrit les actions au lieu de les effectuer** | Le modèle choisi ne prend pas en charge les appels d'outils | Choisissez un modèle dont la prise en charge des outils est confirmée |
| **Une vraie clé API est utilisée à la place du point de terminaison local** | `ANTHROPIC_API_KEY` est toujours exportée | Définissez-la comme chaîne vide, comme indiqué plus haut |
| **Cowork manque après la configuration** | La CLI Claude Code a été configurée à la place de Claude Desktop | Pour Cowork, utilisez le parcours **Apps** d'Ollama |
| **La génération est lente** | Le contexte est trop grand ou un modèle dense a été choisi alors qu'un modèle clairsemé suffit | Réduisez le contexte, puis essayez un modèle mixture-of-experts |
| **Les variables exportées n'ont aucun effet** | Les paramètres de Claude passent avant les variables du shell | Vérifiez les fichiers de paramètres, puis exécutez `/status` |
| **Les requêtes en arrière-plan échouent** | Claude Code utilise un petit modèle pour les tâches internes | Faites pointer la surcharge du petit modèle vers le même modèle local |

*Deux de ces sept problèmes ont la même cause. La plupart des erreurs de configuration viennent d'un mauvais point de terminaison ou d'un modèle sans appels d'outils.*

## À retenir

- **Claude Desktop et Claude Code sont deux intégrations distinctes.** Cowork se trouve dans Claude Desktop et se configure sous macOS dans le panneau **Apps** d'Ollama. Le parcours CLI ne donne pas accès à Cowork.
- **Une commande lance la voie CLI :** `ollama launch claude`. La méthode manuelle nécessite trois variables et **la plupart des guides omettent `ANTHROPIC_API_KEY=""`**.
- **Vous n'avez pas besoin d'une installation locale.** Indiquez `https://ollama.com` à Claude Code avec une clé API.
- **Réglez le contexte sur 64K ou plus avant d'évaluer un modèle.** Une petite fenêtre peut faire penser à un problème de raisonnement.
- **Vérifiez les appels d'outils avec une seule requête.** Si le modèle décrit ce qu'il ferait, vous utilisez un générateur de texte, pas un agent.
- **Les paquets Bonsai ternaires ne fonctionnent pas ici.** Ils nécessitent le fork llama.cpp de Prism ML, qu'Ollama standard ne peut pas charger.
- **La déconnexion est sûre.** Quitter Ollama restaure la configuration précédente de Claude. Dans le terminal, utilisez aussi `ollama launch claude-desktop --restore`.

## Étapes suivantes

1. **Installez Ollama et téléchargez un modèle dont la prise en charge des outils est confirmée** avant de configurer Claude : **[Bibliothèque de modèles Ollama](https://ollama.com/library)**
2. **Lisez la page d'Ollama sur Claude Code** pour connaître les options et modèles actuels : **[Intégration Claude Code](https://docs.ollama.com/integrations/claude-code)**
3. **Pour Cowork, consultez la page Claude Desktop :** **[Intégration Claude Desktop](https://docs.ollama.com/integrations/claude-desktop)**
4. **Dimensionnez le matériel avant de l'acheter**, à l'aide des catégories de mémoire de notre guide d'inférence locale : **[IA locale en 2026 : un modèle 27B dépasse Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. **Vérifiez ce que gère un matériel plus modeste** pour un agent permanent sur un appareil basse consommation : **[Quels modèles d'IA fonctionnent sur Raspberry Pi 4 ou 5 ?](/articles/ai-models-raspberry-pi-4-5/)**

## Articles associés

| Article | Contenu |
|---|---|
| **[IA locale en 2026 : un modèle 27B dépasse Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Comparatif d'inférence locale, quantification ternaire et choix matériel |
| **[Quels modèles d'IA fonctionnent sur Raspberry Pi 4 ou 5 ?](/articles/ai-models-raspberry-pi-4-5/)** | Inférence locale pour un petit assistant toujours actif |
| **[Créer un assistant IA respectueux de la vie privée pour Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Modèle local qui pilote une radio hors réseau, avec la confidentialité comme priorité |
| **[Meilleures extensions VS Code pour le développement IA](/articles/best-visual-studio-code-extensions-for-ai/)** | Outils d'éditeur à associer à un agent de programmation local |

## Références

1. [Intégration Claude Code - documentation Ollama](https://docs.ollama.com/integrations/claude-code)
2. [Intégration Claude Desktop - documentation Ollama](https://docs.ollama.com/integrations/claude-desktop)
3. [Bibliothèque de modèles Ollama](https://ollama.com/library)
4. [Qwen3.8 - bibliothèque de modèles Ollama](https://ollama.com/library/qwen3.8)
5. [Claude Cowork avec des modèles locaux - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Fork llama.cpp de Prism ML - noyaux ternaires](https://github.com/PrismML-Eng/llama.cpp)
