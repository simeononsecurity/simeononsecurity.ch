---
title: "Benchmarks GPU de Llama 3.1 8B et Qwen3.8 27B sur Vast.ai"
date: 2026-10-02
lastmod: 2026-10-10
toc: true
draft: false
description: "Benchmarks Ollama mesurés de Llama 3.1 8B et Qwen3.8 27B sur les principaux GPU Vast.ai. Comparez la vitesse de décodage, le long contexte, le coût de location, l'auto-hébergement, les crédits API et les abonnements."
genre: ["IA locale", "Benchmarks GPU", "IA auto-hébergée", "Cloud computing", "Intelligence artificielle", "Économie de l'IA"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "benchmark GPU", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "LLM local", "long contexte", "location GPU", "IA auto-hébergée", "modèles abliterated", "modèles sans censure", "crédits API", "abonnement IA", "Q4_K_M", "jetons par seconde"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Espace de travail high-tech avec une carte graphique et des écrans affichant des résultats de benchmark d'IA locale"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Le H100 SXM a été la carte la plus rapide dans les deux tests Ollama, mais pas la plus rentable.** Les RTX PRO 5000 et RTX 6000 Ada ont offert un meilleur équilibre entre vitesse et coût de location. La CMP 170HX affichait le tarif horaire le plus bas parmi les exécutions Qwen3.8 27B terminées.

*Ces résultats mesurent un modèle, un wrapper Ollama, une quantification par défaut et un mode de service. Utilisez-les pour dimensionner cette charge de travail, pas pour classer les GPU de façon universelle.*

Cet article compare **Llama 3.1:8b**, une version Ollama Q4_K_M de 8,03 milliards de paramètres, à **Qwen3.8:27b**, une version Ollama Q4_K_M d'environ 27,3 milliards de paramètres. Les deux modèles ont été testés sur des instances GPU louées auprès de Vast.ai. Les tests mesuraient le débit de décodage à des longueurs de prompt réelles allant jusqu'à la limite de contexte prise en charge.

## Réponse courte

**Louez une RTX PRO 5000 ou une RTX 6000 Ada pour un usage régulier par une seule personne.** La RTX PRO 5000 dominait la comparaison de valeur aux contextes courts et moyens. La RTX 6000 Ada coûtait moins cher et gardait une avance utile sur les cartes A100. Louez un H100 SXM lorsque la vitesse compte plus que le tarif horaire ou lorsque les prompts longs font partie de la charge.

| Objectif | Recommandation | Raison |
|---|---|---|
| **Coût de test minimal** | CMP 170HX | 0,420 $ par heure et assez de VRAM pour les modèles Q4_K_M testés |
| **Meilleure valeur sous 1,25 $/h** | RTX PRO 5000 ou RTX 6000 Ada | Débit de décodage élevé sans le coût de location d'un H100 |
| **Réponses les plus rapides** | H100 SXM | Débit de décodage le plus élevé dans les deux tests |
| **Travail Qwen à long contexte** | H100 SXM ou RTX PRO 6000 Max-Q | Les deux ont terminé l'exécution Qwen d'environ 131k jetons avec une marge VRAM importante |
| **Référence 8B populaire** | Llama 3.1:8b | Comparaison pratique en 8B avec une limite de contexte de 128K |
| **Petite charge récurrente** | Crédits API ou abonnement de chat | Aucun coût GPU à l'arrêt, ni maintenance, ni travail de déploiement |
| **Charge privée et fréquente** | Station de travail GPU personnelle | L'achat devient plus facile à justifier avec une utilisation soutenue |
| **Essais de modèles abliterated ou sans censure** | Louer d'abord, acheter seulement après un usage soutenu | Le comportement, la licence et le risque opérationnel exigent un test séparé avant l'achat |

## Ce qui a été testé

**Le benchmark utilisait Ollama avec la version Q4_K_M par défaut.** Aucune quantification spéciale, aucun décodage spéculatif, sampler personnalisé ou serveur particulier n'a été ajouté. L'objectif était une comparaison simple et reproductible des instances GPU.

Vast.ai décrit son service comme une place de marché cloud reliant des fournisseurs de calcul à des utilisateurs. Sa documentation présente des options à la demande, réservées, interruptibles et serverless, avec des filtres pour le modèle GPU, la mémoire, le prix et la disponibilité. Les tarifs horaires ci-dessous viennent des instances sélectionnées pendant cette session, pas d'une liste de prix permanente de Vast.ai.

La sortie mesurée était le **débit de décodage**, exprimé en jetons générés par seconde. Le débit de préremplissage est séparé, car il décrit le traitement du prompt et non la vitesse d'affichage de la réponse. Un prompt long prend souvent beaucoup de temps à traiter même lorsque le décodage reste rapide.

Le benchmark utilisait deux essais valides par contexte et enregistrait la médiane du décodage. Les niveaux terminés reposaient sur les valeurs réelles de `prompt_eval_count` :

- **Environ 16,4k jetons de prompt**
- **Environ 32,8k jetons de prompt**
- **Environ 65,5k jetons de prompt**
- **Environ 131k jetons de prompt**

Le test demandé à 256k jetons n'a pas abouti. Les cartes A100 de 40 Go et plusieurs cartes plus petites traitaient encore le prompt ou n'ont pas terminé à cette longueur.

> **Limite du benchmark :** ces chiffres décrivent deux charges Ollama Q4_K_M avec un seul mode de service. Ils ne prédisent ni la vitesse d'entraînement, ni le débit multi-utilisateur, ni la génération d'images, ni les performances vLLM, ni le résultat d'un autre modèle.

## Nouveau test de Llama 3.1 8B

**Llama 3.1:8b fournit une référence pratique pour le même parc GPU.** Ollama indique environ 120 millions de téléchargements, ce qui en fait un choix raisonnable pour un second benchmark fondé sur la popularité. La [page officielle du modèle Ollama](https://ollama.com/library/llama3.1:8b) indique une version Q4_K_M de 4,9 Go, 8,03 milliards de paramètres et une fenêtre de contexte de 128K.

Le nouveau test utilisait un exécuteur propre au modèle et un générateur de prompts calibré sur le tokenizer d'Ollama. Les libellés ci-dessous utilisent les comptes réels plutôt que les paramètres de contexte demandés :

- **Environ 32 676 jetons de prompt réels** pour la cible 32k
- **Environ 65 342 jetons de prompt réels** pour la cible 64k
- **Environ 130 671 jetons de prompt réels** pour la cible 128k

Le niveau 256k est explicitement non pris en charge pour Llama 3.1 8B, car la limite publiée est de 128K. L'exécuteur ajoutait des tentatives et des lignes d'état. Un délai d'attente reste donc visible au lieu de disparaître.

### Résultats de Llama 3.1 8B

| GPU | ~32k décodage jet/s | ~64k décodage jet/s | ~128k décodage jet/s |
|---|---:|---:|---:|
| **H100 SXM** | **163.5** | **124.0** | **82.4** |
| **H100 SXM** | **158.6** | **121.2** | **80.6** |
| **RTX PRO 5000** | 110.1 | 79.8 | 49.9 |
| **CMP 170HX 64GB** | 91.9 | 71.0 | 50.1 |
| **RTX 6000 Ada** | 88.3 | 53.9 | 29.3 |
| **RTX PRO 6000 Max-Q** | 66.7 | 53.0 | 40.3 |
| **RTX PRO 6000 S** | 60.3 | 42.5 | 33.9 |
| **A100 SXM4 40GB** | 2.0 | 40.6 | 38.5 |
| **A100 PCIe 40GB** | 1.2 | 20.3 | 20.3 |
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Timeout |

Les deux lignes H100 venaient d'instances valides distinctes de la même classe GPU. Les deux devançaient nettement les autres cartes. Leurs résultats à 32k étaient 44 % à 48 % plus rapides que ceux de la RTX PRO 5000. À 128k, l'avance atteignait environ 61 % à 65 %.

Les résultats A100 et RTX 5060 Ti à 32k sont trop faibles pour représenter une exécution GPU comparable dans cette charge. L'hôte RTX 5060 Ti a aussi expiré lors du second essai à 128k. Considérez cet hôte comme impropre à une comparaison GPU valide, et non comme un résultat de classement réel.

| Cible de contexte | État |
|---|---|
| **32k** | Terminé sur les 10 hôtes |
| **64k** | Terminé sur les 10 hôtes |
| **128k** | Terminé sur 9 hôtes. L'hôte 2x RTX 5060 Ti a expiré lors de son second essai |
| **256k** | Non pris en charge sur tous les hôtes, car Llama 3.1 8B accepte au maximum le contexte 128K |

## Comparaison des deux modèles

**Le modèle Llama, plus petit, était plus rapide sur chaque GPU comparable, mais la taille et la qualité du modèle ne sont pas interchangeables.** Llama 3.1 8B sert de référence populaire nécessitant moins de mémoire. Qwen3.8 27B exige davantage de mémoire et présente un profil de capacités différent. Les chiffres servent donc à choisir le matériel, pas à déclarer un modèle universellement supérieur.

| Cas d'usage | Meilleure référence | Pourquoi |
|---|---|---|
| **Assistant 8B rapide** | Llama 3.1:8b | Débit plus élevé et besoin mémoire plus faible |
| **Dimensionnement d'un modèle local 27B** | Qwen3.8:27b | Plus représentatif d'une charge importante sur un seul GPU |
| **Plafond de contexte 128K** | Llama 3.1:8b | La limite explicite de 128K rend la cible 256k invalide |
| **Test de marge VRAM** | Qwen3.8:27b | Le modèle plus grand révèle plus tôt les limites de mémoire et de long contexte |
| **Référence entre fournisseurs** | Llama 3.1:8b | Sa popularité et sa taille facilitent la reproduction du résultat |

Les essais Qwen précédents ont aussi corrigé les comptes réels à environ **32 770**, **65 538** et **131 074** jetons aux niveaux pris en charge. Ces libellés corrigés remplacent les valeurs `num_ctx` demandées lors de la comparaison des essais Qwen.

## Environ 16k jetons

**Le H100 SXM dominait le test à contexte court avec 134,4 jetons décodés par seconde.** La RTX PRO 5000 suivait avec 113,9 jetons par seconde, pour moins de la moitié du prix horaire.

| Rang | GPU | VRAM | Décodage jet/s | Préremplissage jet/s | Tarif |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

À cette longueur, la RTX PRO 5000 atteignait environ 84,7 % de la vitesse du H100 pour 37,3 % de son tarif horaire. La RTX 6000 Ada atteignait environ 66,3 % de la vitesse du H100 pour 30,2 % de son tarif.

## Environ 32,8k jetons

**Le classement restait stable à contexte moyen.** Le H100 SXM descendait à 120,0 jetons par seconde. La RTX PRO 5000 atteignait 105,0 et la RTX 6000 Ada 75,7.

| Rang | GPU | VRAM | Décodage jet/s | Préremplissage jet/s | Tarif |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

La RTX PRO 5000 restait la location la plus intéressante de ce groupe. Elle était seulement 12,5 % plus lente que le H100 et coûtait 62,7 % de moins par heure.

## Environ 65,5k jetons

**Les prompts plus longs ont creusé l'écart entre les cartes à grande capacité mémoire et celles disposant de moins de marge.** Le H100 restait premier à 112,0 jetons par seconde. La RTX PRO 6000 Max-Q passait devant la RTX 6000 Ada en décodage.

| Rang | GPU | VRAM | Décodage jet/s | Préremplissage jet/s | Tarif |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

La RTX PRO 5000 restait le meilleur compromis du tableau terminé. La RTX 6000 Ada était plus lente, mais son tarif inférieur la rendait intéressante lorsque la disponibilité comptait plus que la vitesse maximale.

## Environ 131k jetons

**Le H100 était la seule carte au-dessus de 100 jetons décodés par seconde à cette longueur.** La RTX PRO 6000 Max-Q terminait à 73,4 jetons par seconde, suivie par la RTX 6000 Ada à 61,7.

| Rang | GPU | VRAM | Décodage jet/s | Préremplissage jet/s | Tarif |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | N/A | N/A | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | N/A | N/A | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | N/A | N/A | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

La RTX PRO 6000 Max-Q devenait l'alternative pratique au H100 pour les prompts longs. Elle fournissait 67,8 % de sa vitesse de décodage à 56,0 % du tarif horaire. La RTX 6000 Ada coûtait moins cher, mais ses 48 Go de VRAM laissaient moins de marge pour les longs prompts, les lots plus grands ou une autre configuration.

## Comparaison globale du décodage

| GPU | ~16k | ~32,8k | ~65,5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | N/A |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | N/A |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | N/A |
| **A100 PCIe** | 38.4 | 36.1 | N/A | N/A |

**Le H100 menait à chaque longueur de contexte terminée.** Son avantage passait de 20,5 jetons par seconde sur la RTX PRO 5000 à environ 16k jetons à 12,0 à environ 32,8k. Le choix de valeur dépend de votre priorité entre la première réponse rapide et le coût minimal d'une session longue.

## Coût par million de jetons décodés

**Le tarif horaire seul masque la comparaison utile.** Diviser le tarif fourni par le débit de décodage donne un coût locatif approximatif pour un million de jetons générés. Ce calcul ignore le traitement du prompt, le temps d'inactivité, le stockage, le transfert, les taxes, les remises et les exécutions échouées ou interrompues.

| GPU | Tarif à contexte court | Coût approximatif par million de jetons |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**La CMP 170HX gagnait cette comparaison arithmétique étroite.** Les RTX PRO 5000 et RTX 6000 Ada suivaient de près et offraient toutes deux plus de débit. Pour un usage interactif, le temps d'attente supplémentaire compte souvent davantage que le coût minimal par jeton.

## Louer, acheter des crédits, s'abonner ou acheter du matériel ?

**Le bon choix dépend de l'utilisation et du niveau de contrôle requis.** Une location GPU est une facture de calcul variable. Les crédits API sont une facture de modèle variable. Un abonnement de chat est un accès fixe avec des limites d'utilisation. Le matériel personnel est un achat suivi d'électricité, de refroidissement, de maintenance et de dépréciation.

| Budget mensuel et charge | Choix recommandé | Pourquoi | Principal compromis |
|---|---|---|---|
| **Moins de 10 $** | Acheter des crédits API ou utiliser un modèle local gratuit | Valide le flux sans coût GPU à l'arrêt | Moins de contrôle sur l'hébergement et les limites de débit |
| **10 à 30 $** | Crédits API pour un usage occasionnel, ou abonnement de chat au quotidien | L'abonnement convient au chat humain, les crédits aux scripts et appels mesurés | Aucun des deux ne fournit par défaut un endpoint privé 27B |
| **30 à 100 $** | Louer une RTX 6000 Ada ou PRO 5000 pendant les sessions actives | Couvre de courtes recherches et évite les frais de propriété | L'instance exige préparation, stockage, surveillance et arrêt correct |
| **100 à 250 $** | Louer une carte rapide pour les tâches planifiées, ou tester un poste personnel | L'usage soutenu rend l'utilisation mensuelle visible | La disponibilité et les tarifs changent |
| **250 à 600 $** | Comparer un mois de RTX PRO 5000 louée à un GPU local neuf ou d'occasion | C'est le point de décision pour l'inférence privée fréquente | Le matériel ajoute énergie, chaleur, support et risque de revente |
| **Plus de 600 $** | Acheter seulement avec forte utilisation, ou réserver une location H100 pour les pics | Une stratégie mixte évite de posséder le matériel de pointe pour une demande occasionnelle | Le capital reste immobilisé dans une configuration |

Ces fourchettes guident une décision, elles ne constituent pas un devis fournisseur. Les tarifs montrent le seuil important : un H100 à 2,693 $/h coûte environ 64,63 $ pour une journée continue de 24 heures et 1 941,00 $ pour 30 jours, avant stockage ou autres frais. La RTX PRO 5000 à 1,005 $/h coûte environ 24,12 $ par jour et 723,60 $ pour 30 jours continus. Une carte louée uniquement pendant les sessions actives produit un total différent d'une carte laissée allumée tout le mois.

### Quand les crédits API gagnent

**Les crédits API gagnent lorsque l'usage est irrégulier, l'automatisation compte et aucune exigence ne porte sur un modèle local précis.** Ils évitent le provisionnement GPU, les téléchargements, les problèmes de pilotes et le temps d'inactivité. Ils permettent aussi de comparer plusieurs modèles hébergés avant d'acheter du matériel.

Les prix API varient selon le modèle et le fournisseur. Le catalogue de modèles OpenRouter compare les contextes, fournisseurs et tarifs par jeton. Utilisez le calculateur en direct du fournisseur avant de comparer une facture API à ce benchmark. Un GPU local produit des jetons sans facturation par jeton, mais l'heure de location continue pendant l'attente de l'instance.

### Quand l'abonnement gagne

**Un abonnement convient à une personne qui utilise chaque jour un assistant hébergé.** Les offres individuelles actuelles de Claude séparent par exemple les accès Free, Pro et Max, avec des limites et fonctions différentes. Un abonnement n'est pas un accès API. Il fournit souvent une interface soignée et des outils intégrés, tandis que les crédits API donnent un contrôle programmatique.

Choisissez un abonnement pour l'écriture interactive, la recherche, le code ou l'examen de fichiers. Choisissez les crédits API lorsqu'un script, une application ou un agent a besoin d'un endpoint mesuré.

### Quand Vast.ai gagne

**Vast.ai gagne lorsque vous avez besoin d'un modèle ouvert, d'un runtime privé contrôlable ou d'un pic de débit court.** Sélectionnez le GPU, lancez une instance, exécutez Ollama, testez un modèle, puis arrêtez l'instance. C'est une bonne voie pour Qwen3.8 27B, les variantes abliterated et les autres fichiers de modèles trop grands pour un ordinateur portable.

Le prix est le travail opérationnel. Vérifiez l'utilisation du GPU, surveillez la VRAM, protégez le service exposé, conservez les fichiers requis et arrêtez l'instance après l'exécution. Un tarif horaire bas ne corrige pas une instance oubliée.

### Quand acheter un GPU gagne

**Acheter du matériel devient intéressant après une utilisation soutenue, des modèles stables et un besoin de contrôle local.** L'achat supprime le risque de disponibilité et fournit un environnement persistant. Il permet aussi d'exécuter des données privées sans envoyer les prompts à un fournisseur hébergé.

Le prix d'achat n'est qu'une partie de la facture. Ajoutez le système hôte, l'alimentation, le stockage, le refroidissement, l'électricité, le risque de remplacement et la valeur de votre temps d'installation. Une carte haut de gamme reste aussi inactive pendant les périodes où les crédits API ou un abonnement coûtent moins cher.

Les spécifications de référence NVIDIA de la RTX 4090 indiquent 24 Go de mémoire, une puissance graphique totale de 450 W et une recommandation de système de 850 W. C'est un repère utile pour l'inférence locale, mais sa capacité de 24 Go est inférieure aux configurations Q4_K_M 27B testées ici. Vérifiez l'utilisation mémoire réelle du modèle au lieu de supposer qu'une carte suffit à partir du seul nombre de paramètres.

## Modèles abliterated et sans censure

**Les variantes abliterated et sans censure changent la décision d'achat.** Elles attirent souvent par des refus moins fréquents ou moins de restrictions intégrées. Leurs coûts incluent un comportement de sécurité plus faible, une provenance incertaine, un format de prompt irrégulier, un besoin de revue accru et d'éventuelles limites de licence ou d'utilisation acceptable.

Pour ces modèles, louez avant d'acheter. Un test d'une journée sur RTX PRO 5000 au tarif fourni coûte environ 24,12 $ avant les autres frais. Cela suffit pour confirmer l'adéquation du modèle, l'utilisation du GPU, la qualité des réponses et le risque opérationnel.

**N'exposez pas directement un modèle sans censure à Internet.** Placez une authentification, des limites de débit, des contrôles de journalisation et une isolation réseau devant lui. N'envoyez pas de données personnelles, confidentielles ou réglementées à une source de modèle que vous n'avez pas examinée.

Si le modèle devient un outil quotidien, comparez le total mensuel de location au coût complet d'une station personnelle. Pour un usage occasionnel, la location reste plus facile à arrêter et à remplacer.

## Réserves du benchmark

**Les résultats manquants font partie du résultat.** Une valeur `N/A` signifie que l'exécution n'a pas produit de mesure valide. Elle ne signifie pas que le GPU est lent selon le score implicite d'une autre carte.

- **La seconde instance H100 n'a produit aucun jeu de mesures valide**, car le téléchargement du modèle s'est terminé trop tard.
- **L'instance 2x RTX 5060 Ti a été exclue**, car Ollama a chargé le modèle sur le CPU au lieu d'utiliser les GPU.
- **Le prompt Qwen3.8 27B de 256k jetons n'a pas été terminé.** Son niveau valide maximal était d'environ 131k jetons réels. Llama 3.1 8B considère 256k comme non pris en charge, car sa limite est 128K.
- **Le `num_ctx` demandé n'a pas servi de libellé de classement.** Les tableaux finaux utilisent les valeurs réelles de `prompt_eval_count`.
- **Deux essais valides par contexte ont été résumés par la médiane du décodage.** Cela réduit l'effet d'un essai lent, sans remplacer un jeu de tests plus large.
- **Le wrapper restait volontairement simple.** Un déploiement vLLM ou llama.cpp réglé différemment produira un autre classement.

## Recommandation finale

**Commencez par louer une RTX 6000 Ada ou une RTX PRO 5000.** La RTX 6000 Ada est le choix économique lorsque son tarif de 0,813 $/h est disponible. La RTX PRO 5000 offre plus de vitesse sous le prix d'un H100. Utilisez le H100 SXM pour les prompts longs, une latence interactive exigeante ou une courte fenêtre de benchmark où le temps compte plus que le coût. Pour un modèle 8B, testez la CMP 170HX lorsque son tarif inférieur compte plus que la vitesse maximale.

**N'achetez pas un GPU après un seul test réussi.** Louez-le pendant un mois de charges réelles, notez les heures actives, les longueurs de prompts, la concurrence et les changements de modèle, puis comparez le total à la facture complète de propriété. Achetez lorsque la charge occupe assez souvent la carte et reste assez stable pour justifier la perte de flexibilité.

Pour un usage occasionnel, les crédits API ou un abonnement de chat sont plus simples. Pour l'inférence locale privée, l'expérimentation avec des modèles ouverts ou les essais de modèles abliterated, Vast.ai offre une voie avec moins d'engagement qu'un achat immédiat. Utilisez Llama 3.1 8B comme référence à faible mémoire et Qwen3.8 27B lorsque le grand modèle est la cible réelle.

## Prochaines étapes

Répétez la comparaison avec vos propres longueurs de prompts et votre estimation d'heures actives. Vérifiez l'utilisation du GPU, notez la révision du modèle et la version du runtime, arrêtez l'instance après chaque exécution et comparez le total mensuel de location au coût complet de propriété avant d'acheter.

## Références

1. [Place de marché cloud GPU Vast.ai](https://vast.ai/)
2. [Documentation Vast.ai : place de marché, instances, tarifs et types de location](https://docs.vast.ai/)
3. [Bibliothèque de modèles Qwen3 d'Ollama](https://ollama.com/library/qwen3)
4. [Page du modèle Llama 3.1 8B d'Ollama](https://ollama.com/library/llama3.1:8b)
5. [Catalogue de modèles et comparaison des tarifs OpenRouter](https://openrouter.ai/models)
6. [Tarifs Claude et abonnements individuels](https://www.anthropic.com/pricing)
7. [Spécifications NVIDIA GeForce RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [IA locale en 2026 : Qwen3.8 27B et matériel pour modèles auto-hébergés](/articles/local-ai-2026-build-your-rig-now/)
9. [Tests de modèles Ollama sur matériel Raspberry Pi](/articles/ai-models-raspberry-pi-4-5/)
