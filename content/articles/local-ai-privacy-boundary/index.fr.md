---
title: "Confidentialité de l'IA locale : ce qui reste sur votre ordinateur et ce qui n'y reste pas"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Suivez les invites, fichiers de modèle, outils, journaux, exposition réseau et coûts d'électricité avant de choisir l'inférence locale ou un service d'IA hébergé."
genre: ["IA locale", "Confidentialité", "IA auto-hébergée", "Cybersécurité", "Économie de l'IA"]
tags: ["confidentialité de l'IA locale", "inférence locale", "IA cloud", "confidentialité des données d'IA", "IA auto-hébergée", "confidentialité des LLM", "coût de possession d'un GPU", "coût de l'électricité pour l'IA", "RTX 5070", "Claude Haiku 5.5", "confidentialité d'Ollama", "llama.cpp", "sécurité de l'IA", "IA hors ligne", "modèles de langage locaux", "confidentialité des invites", "modèle de menace IA", "seuil de rentabilité du GPU", "frontière des données IA", "IA privée"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Un poste de travail d'IA locale relié à un service cloud par des chemins de données visibles"
coverCaption: "Illustration des chemins de données d'une IA locale et hébergée"
---

**L'IA locale réduit votre périmètre de données.** Une invite traitée par un runtime local reste sur votre appareil lorsque le modèle, les outils, les journaux et le chemin réseau restent locaux. Un GPU local ne transforme pas un ordinateur en système isolé.

Les runtimes de modèles, les plugins d'outils, les extensions de navigateur, l'accès distant, les API exposées et les téléchargements de modèles définissent encore votre risque. Le coût compte aussi. L'électricité peut être moins chère qu'un prix de tokens hébergé, tandis que la possession du matériel repousse le seuil de rentabilité complet loin dans le futur.

Ce guide cartographie d'abord la frontière de confidentialité. Il vérifie ensuite le coût avec les prix actuels des fournisseurs, une hypothèse explicite de puissance et les chiffres rapportés par la vidéo fournie.

<!--more-->

Cette comparaison des coûts local contre hébergé donne le contexte des formules ci-dessous. Ne copiez pas ses chiffres de débit sans tester le même fichier de modèle et le même runtime sur votre matériel.

{{< youtube id="DmkuFpoMYmc" enable="true" title="L'IA locale en vaut-elle la peine ? Nous avons comparé les coûts à Claude Haiku 5.5" description="Comparaison des coûts d'une IA locale et hébergée." >}}

La vidéo indique une durée de 2 minutes 31 secondes. J'ai vérifié son titre et sa durée sur la page de visionnage. Je n'ai pas reproduit le test matériel, ses vitesses restent donc des mesures rapportées par la source.

## La réponse courte

- **Choisissez l'inférence locale pour un chemin de données contrôlé.** Gardez le serveur de modèles sur l'appareil, liez-le à loopback et limitez l'accès aux outils.
- **Choisissez l'inférence hébergée pour un usage occasionnel.** Évitez une dépense matérielle lorsque votre charge est faible ou que votre modèle préféré ne tient pas sur votre système.
- **Traitez le coût local comme deux nombres.** Séparez l'électricité par heure active de la possession du matériel.
- **Traitez la confidentialité comme une propriété du système.** Un modèle privé perd son intérêt lorsqu'un plugin téléverse des fichiers ou qu'une API locale écoute sur chaque interface réseau.

L'inférence locale aide lorsque du texte sensible doit rester dans un poste de travail ou un réseau isolé. Elle aide aussi pour le fonctionnement hors ligne, une version fixe du modèle ou un accès prévisible sans quota fournisseur.

Ces avantages ne prouvent pas de meilleures réponses. Un modèle hébergé peut mieux convenir à une tâche, terminer plus vite ou demander moins de maintenance. Mesurez la charge avant d'acheter du matériel.

## Suivez le chemin des données

Cartographiez chaque composant impliqué dans une requête. Le nom du modèle seul ne montre pas où les données circulent.

| Composant | Question de confidentialité | Éléments de preuve à collecter |
|---|---|---|
| **Serveur de modèle local** | L'invite reste-t-elle sur l'hôte ? | Configuration du processus, adresse d'écoute et trafic sortant |
| **Modèle cloud** | Quels textes, fichiers et résultats d'outils quittent l'hôte ? | Endpoint API, conditions du fournisseur, journaux de requêtes et paramètres du compte |
| **Mode cloud dans une application locale** | Le modèle sélectionné s'exécute-t-il sur l'appareil ? | Identifiant du modèle, libellé du fournisseur et connexion réseau |
| **Plugin d'outil** | Le modèle reçoit-il des fichiers, une sortie shell ou du contenu du navigateur ? | Liste des outils, permissions et données de requêtes capturées |
| **Téléchargement du modèle** | Quel code et quels poids entrent sur l'hôte ? | Dépôt source, licence, somme de contrôle de la version et chemin de téléchargement |
| **Journaux locaux** | Où les invites et résultats d'outils persistent-ils ? | Journaux du runtime, historique shell, rapports de plantage et périmètre des sauvegardes |

**Un modèle local retire un fournisseur du chemin de l'invite.** Il ne retire pas la nécessité d'examiner le reste du chemin.

## Local ne signifie pas privé par défaut

[La politique de confidentialité d'Ollama](https://ollama.com/privacy) indique qu'Ollama ne voit pas les invites ni les données lorsqu'un modèle s'exécute localement. La politique sépare aussi l'utilisation locale des modèles hébergés dans le cloud. Un modèle cloud crée toujours une frontière de service, même lorsque la même application lance les deux modes.

[La documentation du serveur llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) montre qu'un serveur local écoute par défaut sur `127.0.0.1:8080`. Ses exemples Docker montrent aussi `--host 0.0.0.0`, qui expose le service sur toutes les interfaces. Une adresse d'écoute plus large change la frontière d'accès.

Vérifiez l'adresse d'écoute avant d'envoyer du texte sensible :

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

`127.0.0.1` ou `localhost` limite normalement l'accès au même hôte. Une adresse LAN ou `0.0.0.0` demande une règle de pare-feu et un plan d'authentification. N'exposez pas un endpoint de modèle à un réseau avant d'avoir testé les deux.

Vérifiez aussi le nom du modèle sélectionné. La documentation cloud d'Ollama décrit les modèles cloud comme un chemin de service distinct. Une interface locale ne prouve pas une exécution locale.

La [FAQ d'Ollama](https://docs.ollama.com/faq) documente un mode réservé au local. Définissez `disable_ollama_cloud` dans `~/.ollama/server.json`, ou définissez `OLLAMA_NO_CLOUD=1` avant de redémarrer le service. Cela retire les modèles cloud et la recherche web d'Ollama du runtime sélectionné. Cela ne limite pas les autres applications, outils de navigateur, plugins ou accès réseau de l'hôte.

```json
{
  "disable_ollama_cloud": true
}
```

Vérifiez le paramètre après le redémarrage. Un runtime local uniquement réduit un chemin. Il n'établit pas un hôte privé.

## Comptez le coût hébergé

Les prix des tokens séparent l'entrée de la sortie. [Anthropic indique Claude Haiku 5.5 à 0,10 $ par million de tokens d'entrée et 0,50 $ par million de tokens de sortie pour les invites jusqu'à 100 000 tokens](https://www.anthropic.com/claude/haiku). Les invites dépassant 100 000 tokens utilisent les tarifs supérieurs indiqués.

[Le guide des tokens d'OpenAI](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) explique pourquoi un nombre de mots n'est pas égal à un nombre de tokens. Il sépare aussi les tokens d'entrée, de sortie, d'entrée mis en cache et de raisonnement. Utilisez les champs d'utilisation de votre fournisseur plutôt qu'une estimation basée sur les mots.

Pour une comparaison simple, utilisez séparément un million de tokens générés et un million de tokens d'entrée. Un agent de codage envoie souvent un contexte répété et produit une réponse plus petite, donc un seul total de tokens masque le mélange des coûts.

## Calculez la puissance locale

[L'annonce de lancement de la RTX 5070 de NVIDIA](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) indiquait un prix de départ de 549 $. [La page de la famille RTX 5070 de NVIDIA](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) indique 12 Go de mémoire et une puissance graphique totale de 250 W pour la conception de référence Founders Edition. La page produit de NVIDIA indique toujours 549 $ et affichait la carte en rupture de stock pendant cette vérification.

La puissance du GPU n'est pas la puissance de tout le système. Utilisez un wattmètre pour votre PC. L'exemple ci-dessous suppose une **consommation système totale de 400 W**, GPU, processeur, mémoire, stockage, ventilateurs et pertes de l'alimentation compris. Il s'agit d'une hypothèse arithmétique, pas d'une mesure.

[Les prévisions de l'U.S. Energy Information Administration](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) utilisaient 18,2 cents par kilowatt-heure comme prix résidentiel moyen de l'électricité en 2026. Votre tarif local change le résultat.

Utilisez cette formule pour la sortie générée :

```text
local cost per 1M output tokens =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

À 400 W et 0,182 $ par kilowatt-heure, le système coûte 0,0728 $ par heure active.

| Vitesse de sortie | Temps pour 1M de tokens | Coût énergétique pour 1M de tokens |
|---:|---:|---:|
| **20 tokens par seconde** | 13 heures 53 minutes | **1,01 $** |
| **50 tokens par seconde** | 5 heures 33 minutes | **0,40 $** |
| **94 tokens par seconde** | 2 heures 57 minutes | **0,22 $** |

À 50 tokens de sortie par seconde, l'électricité locale coûte moins que le prix de sortie de 0,50 $ de Haiku 5.5. À 20 tokens de sortie par seconde, elle coûte plus. Le seuil de vitesse de sortie dans ces hypothèses est d'environ 40 tokens par seconde.

Le calcul d'entrée utilise la même formule. À 2 650 tokens d'entrée par seconde, un million de tokens d'entrée prend environ 6 minutes 17 secondes et coûte environ 0,008 $ d'électricité. À 1 000 tokens d'entrée par seconde, le même travail coûte environ 0,020 $.

La transcription fournie indique 94 tokens de sortie par seconde et 2 650 tokens d'entrée par seconde pour son exemple RTX 5070. Les calculs ci-dessus concordent avec ces chiffres sous l'hypothèse de 400 W. La transcription ne fournit ni relevé indépendant de laboratoire, ni somme de contrôle du fichier de modèle, ni version du runtime, ni invite, ni mesure au wattmètre. Traitez ces vitesses comme un résultat de référence, pas comme une garantie d'achat.

## Le matériel modifie le seuil de rentabilité

Les économies d'électricité ne remboursent pas le matériel seules. Comparez l'achat complet avec l'écart entre le coût de sortie hébergé et le coût variable local.

À 50 tokens de sortie par seconde :

```text
$0.50 hosted output price - $0.40 local power = $0.10 saved per 1M tokens
$549 GPU price / $0.10 = about 5.5 billion output tokens
```

À 94 tokens de sortie par seconde, l'économie arrondie monte à environ 0,28 $ par million de tokens. Récupérer un GPU à 549 $ demande alors environ 2 milliards de tokens de sortie. Les deux chiffres excluent la mémoire système, le stockage, la carte mère, l'alimentation, le refroidissement, la maintenance et la valeur de revente.

Le prix de lancement n'est pas un devis d'achat universel. La page actuelle de NVIDIA affichait le prix officiel sans stock. Une annonce à 819 $ demande une vérification séparée avant son intégration dans un modèle de seuil de rentabilité. Utilisez votre facture réelle et la puissance mesurée au mur.

**Le matériel existant change la décision.** Si votre poste possède déjà assez de mémoire et un GPU adapté, le coût matériel est amorti pour la prochaine tâche. Comparez la puissance, le temps, la qualité, la confidentialité et la maintenance. Si vous devez acheter un système complet, comparez le système complet à l'usage hébergé.

Pour les détails d'adéquation des modèles, lisez le [guide des modèles d'IA locale et du contexte GPU](/articles/local-ai-model-gpu-context-guide/) et le [guide de dimensionnement de 16 Go de VRAM](/articles/is-16gb-vram-enough-local-llm/). Pour une configuration d'agent de codage local rapportée, lisez le [guide Strata et OpenCode](/articles/strata-opencode-local-coding-agent-16gb/).

## Ce que la confidentialité locale vous apporte

- **Un chemin de données plus court :** l'invite n'a pas besoin d'atteindre un fournisseur de modèle lorsque l'inférence reste locale.
- **Le fonctionnement hors ligne :** un modèle téléchargé et un runtime local n'ont pas besoin d'une connexion fournisseur active pour générer du texte.
- **Le contrôle des versions :** vous choisissez le fichier de modèle et la version du runtime au lieu de recevoir automatiquement un changement du fournisseur.
- **Le contrôle de l'utilisation :** l'inférence locale évite un compteur cloud par requête après prise en compte de la possession du matériel et de l'électricité.
- **Le contrôle de la politique réseau :** votre pare-feu et les contrôles de l'hôte définissent qui atteint l'endpoint du modèle.

Ces gains comptent surtout pour le code source, les dossiers clients, les designs non publiés, les notes privées et le travail dans un environnement déconnecté. L'inférence locale demande toujours le chiffrement du disque, les mises à jour de l'hôte, la séparation des comptes et des outils limités.

## Ce que la confidentialité locale ne vous apporte pas

- **Une garantie de qualité :** les modèles plus petits ou quantifiés demandent des tests avec vos critères d'acceptation réels.
- **Une garantie de chaîne d'approvisionnement :** les fichiers de modèles, runtimes, plugins et images de conteneur demandent des sources fiables et des contrôles d'intégrité.
- **Un hôte propre :** les logiciels malveillants, extensions de navigateur, sauvegardes, rapporteurs de plantage et outils d'administration distante voient encore les données de l'hôte.
- **Un endpoint réseau sûr :** un serveur lié à toutes les interfaces crée un nouveau service à défendre.
- **Un système gratuit :** l'électricité, le stockage, le refroidissement, l'usure du matériel et la maintenance ont toujours un coût.

Le [guide d'agent de codage local Strata](/articles/strata-opencode-local-coding-agent-16gb/) montre pourquoi la mémoire système, le contexte, l'accès aux outils et les paramètres du runtime appartiennent à l'évaluation. La mémoire du GPU seule ne définit ni la frontière de confidentialité ni celle des performances.

## Choisissez la bonne frontière

| Situation | Premier choix préférable | Raison |
|---|---|---|
| **Documents sensibles et PC compatible existant** | Inférence locale | Garder les invites dans un hôte contrôlé et éviter une nouvelle dépense matérielle |
| **Rédaction générique occasionnelle** | API ou service de chat hébergé | Payer la petite charge et éviter la maintenance |
| **Modèle de pointe ou outil cloud spécialisé** | Service hébergé | Le modèle ou l'outil requis n'est pas disponible sur l'hôte local |
| **Volume récurrent important avec modèle local vérifié** | Local ou hybride | Comparer la puissance, la qualité, le temps de support et les prix fournisseur |
| **Charges mixtes** | Routage hybride | Garder les tâches sensibles en local et envoyer les tâches génériques approuvées à un modèle hébergé |

**Le routage hybride demande une règle de classification explicite.** Marquez les données comme réservées au local, approuvées pour un traitement hébergé ou interdites jusqu'à examen. Ne comptez pas sur un nom de modèle ou une icône d'application pour appliquer la règle.

## Vérifiez avant de faire confiance

1. **Nommez le chemin du modèle.** Notez l'identifiant du modèle, le runtime, la version et la source de téléchargement.
2. **Vérifiez l'adresse d'écoute.** Confirmez que le serveur écoute sur loopback, sauf si un chemin plus large possède un besoin documenté.
3. **Listez chaque outil.** Examinez l'accès aux fichiers, au shell, au navigateur, au réseau et aux plugins.
4. **Inspectez la persistance.** Trouvez les journaux d'invites, sorties d'outils, rapports de plantage, sauvegardes et répertoires de modèles partagés.
5. **Testez le comportement réseau.** Observez les connexions pendant un test sensible avec une invite représentative.
6. **Mesurez le système.** Notez la puissance au mur, la vitesse de sortie, la vitesse d'entrée, la longueur du contexte et les nouvelles tentatives.
7. **Testez le travail accepté.** Comparez les tâches terminées et l'effort de revue, pas seulement les tokens par seconde.

Le [guide IA locale contre ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/) couvre les compromis de capacité des modèles. Utilisez cette liste de confidentialité avec le test de qualité.

## Références

- [Vidéo, L'IA locale en vaut-elle la peine ? Nous avons comparé les coûts à Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [Annonce de lancement NVIDIA Blackwell GeForce RTX 50 Series](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [Spécifications de la famille NVIDIA GeForce RTX 5070](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [Page produit NVIDIA GeForce RTX 5070](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, Short-Term Energy Outlook d'octobre 2026](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Tarification de la plateforme Anthropic Claude](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, Comprendre et compter les tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Politique de confidentialité d'Ollama](https://ollama.com/privacy)
- [Documentation du serveur llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
