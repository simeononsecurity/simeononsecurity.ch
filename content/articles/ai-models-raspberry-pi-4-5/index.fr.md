---
title: "Quels modèles d’IA fonctionnent sur un Raspberry Pi 4 ou 5 ?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Choisissez un modèle de langage local selon la mémoire, la vitesse et l’usage à partir de mesures sur Raspberry Pi 4 et 5, des petits modèles LFM2.5 aux options 3B et plus."
genre: ["Raspberry Pi", "Intelligence artificielle", "Auto-hébergement"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "IA locale", "petits modèles de langage", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "quantification de modèle", "IA de périphérie"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Deux ordinateurs Raspberry Pi sur un bureau sombre, avec des illustrations de réseaux neuronaux bleus et ambrés au-dessus"
coverCaption: "Illustration de modèles d’IA locaux exécutés sur du matériel Raspberry Pi."
---

Un Raspberry Pi peut exécuter localement un modèle de langage utile, à condition que celui-ci tienne dans la mémoire de la carte et réponde dans un délai acceptable pour votre application. Un Raspberry Pi 4 avec 2 Go convient surtout aux modèles de moins d’environ un milliard de paramètres. Un Raspberry Pi 5 avec 8 Go exécute confortablement des modèles compacts de 1B à 3B et peut charger quelques modèles quantifiés plus grands, avec des compromis importants.

Nous avons mesuré ces modèles nous-mêmes avec Ollama sur un **Pi 4B de 2 Go** et un **Pi 5 de 8 Go**, tous deux équipés d’une carte microSD. Les mesures des tableaux utilisent les mêmes cinq requêtes courtes d’assistant, le même prompt système, une seed fixe et une limite de sortie de 140 tokens. Nous avons déchargé les autres modèles avant chaque essai et mesuré le chargement à froid, le délai avant le premier token visible, le temps total de réponse, la vitesse de sortie et la mémoire résidente maximale. Ces essais à passage unique portent sur des réponses courtes. Ils servent à estimer les ressources nécessaires, pas à établir un classement universel de vitesse ou de qualité. Le [CPU Cortex-A76 et les configurations mémoire disponibles du Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) diffèrent aussi sensiblement de la [plateforme Cortex-A72 du Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Les types de modèles adaptés

| Type de modèle | Exemples mesurés | Usage pratique |
|---|---|---|
| Petits modèles de texte, environ 230M à 600M de paramètres | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Commandes locales courtes, résumés et questions à contraintes ; meilleur point de départ sur un Pi 4 de 2 Go |
| Modèles de texte compacts, environ 1B à 2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Instructions plus nuancées sur un Pi 5 ou un Pi 4 doté de plus de mémoire, avec des réponses plus lentes que les plus petits modèles |
| Modèles de texte quantifiés de 3B à 4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Candidats plus capables pour un Pi 5 de 8 Go si plusieurs secondes d’attente par réponse sont acceptables |
| Modèles clairsemés ou hybrides plus grands | LFM2.5 8B | Fonctionne techniquement sur le Pi 5 de 8 Go testé, mais occupe beaucoup de mémoire et démarre lentement |

Ces résultats concernent la **génération de texte**. Ils ne mesurent ni la génération d’images, ni la reconnaissance vocale, ni la vision, ni l’entraînement. « Fonctionner » ne signifie pas seulement que le fichier du modèle tient sur une carte : le runtime, le cache de contexte, le système d’exploitation et les autres services ont aussi besoin de RAM. La quantification réduit la taille des poids, mais peut diminuer la qualité des réponses, surtout avec des réglages extrêmes comme les poids sur 1 bit.

### Ce que mesurent les chiffres

Le test a envoyé à l’API de chat Ollama des requêtes courtes sur des faits, des procédures de sécurité, du contexte récupéré, la météo et l’aide. Chaque modèle a reçu le même jeu de requêtes et la même seed. Nous avons déchargé le modèle avant la mesure afin que la requête suivante inclue un démarrage à froid. Le **temps total** couvre la requête complète, tandis que les **tokens par seconde** décrivent uniquement la génération de sortie. Nous avons aussi relevé le premier token *visible*, un point important quand le modèle raisonne avant de répondre.

Pour la mémoire, nous avons relevé la RAM disponible et le swap du Pi, ainsi que la mémoire résidente d’Ollama et de son processus d’inférence pendant chaque requête. Les valeurs de **RSS** représentent la mémoire résidente du processus, pas les besoins totaux de l’hôte. Les pages issues de fichiers, le système, un navigateur ou un autre service local peuvent encore provoquer du swap avec un modèle qui semble tenir sur le papier. Les tableaux reprennent les premiers essais à cinq requêtes et un seul passage. Nous avons ensuite ajouté une requête d’actualité et des contrôles des règles de réponse. Ces contrôles précisent ce qu’il faut examiner, mais ne transforment pas les mesures précédentes en résultats de conformité sur six requêtes.

Ni les tokens par seconde ni le nombre de paramètres ne mesurent la qualité. Un modèle peut écrire vite, mais omettre une source demandée, dépasser une limite de mots ou laisser une phrase inachevée. Comparez les modèles avec les requêtes que vous comptez envoyer et lisez les réponses avant d’en choisir un pour une application.

## Raspberry Pi 4 : privilégier les plus petits modèles

Le Pi 4 de 2 Go testé disposait de peu de marge. Les plus petits modèles LFM2.5 ont terminé les cinq requêtes, tout comme `qwen2.5:0.5b`. Ils conviennent aux réponses hors ligne brèves ou à un petit assistant local.

| Modèle | Fichier du modèle | Vitesse de sortie mesurée | Temps de réponse moyen | Mémoire ou résultat observé |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF importé | 0.25 GB | 12.8 tokens/s | 7.2 s | 383 MB de mémoire résidente maximale ; 5/5 requêtes |
| LFM2.5-350M, GGUF importé | 0.38 GB | 8.6 tokens/s | 8.6 s | 516 MB de mémoire résidente maximale ; 5/5 requêtes |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 requêtes ; disponible directement dans Ollama |
| MiniCPM5-1B, GGUF importé, raisonnement désactivé | 0.69 GB | 5.9 tokens/s | 12.2 s | 883 MB de mémoire résidente maximale ; 5/5 requêtes |
| MiniCPM5-1B, GGUF importé, raisonnement par défaut | 0.69 GB | 5.7 tokens/s | 33.3 s | Une seule réponse visible utile sur cinq |
| `qwen3:0.6b`, raisonnement par défaut | 0.52 GB | 6.4 tokens/s | 40.4 s | Une réponse vide ; la carte a redémarré |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, aucun swap ni redémarrage ; lente mais stable |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | Swap important ; la carte a redémarré pendant le test |
| `qwen3.5:0.8b` | 1.04 GB | — | — | Essai inachevé ; la carte a redémarré |

Les résultats du Pi 4 dépendent fortement du reste du système. Nous avons observé des réinitialisations pendant les essais de modèles plus grands, notamment un test de `qwen3.5:0.8b` qui n’a jamais abouti. Cela décrit notre configuration de 2 Go, pas tous les Pi 4 ni tous les modèles 1B. Un Pi 4 de 4 ou 8 Go dispose de plus de mémoire, mais son CPU restera plus lent que celui du Pi 5 testé. Nous n’avons pas mesuré directement ces variantes mémoire du Pi 4.

Un premier essai sur Pi 4 semblait aussi nettement moins bon que les mesures finales : environ 625 MB de fichiers GGUF temporaires occupaient le `/tmp` en RAM, ne laissant que 500 à 600 MB disponibles et envoyant plusieurs centaines de mégaoctets dans le swap. Après le déplacement de ces fichiers vers un stockage persistant, les résultats des petits modèles ont mieux représenté la mémoire d’inférence. Sur une carte de 2 Go, *l’emplacement du téléchargement* peut fausser un test.

**Recommandation :** notre choix par défaut pour cette carte de 2 Go est le LFM2.5-350M importé. Il est resté stable à **516 MB RSS**, a laissé environ **1 GB de RAM disponible** et a réussi **5/6** contrôles des règles de réponse sur Pi 4. Lors des tests répétés sur Pi 5, il a parfois omis le nom de la source. Les applications qui exigent cette attribution doivent donc la vérifier. Choisissez LFM2.5-230M si la latence et la marge mémoire comptent le plus : il était plus rapide et plus léger, mais une réponse médicale a transformé « nausea or vomiting » en « nausea/ventilator use ». Cette erreur de contenu en fait un choix par défaut moins adapté aux réponses sur la santé ou la sécurité, malgré un meilleur score mécanique répété. Choisissez `qwen2.5:0.5b` si vous avez besoin d’un modèle du [registre Ollama](https://ollama.com/library/qwen2.5/tags), tout en tenant compte de sa conformité plus faible aux instructions. `granite4:350m` est resté stable, mais était plus lent et consommait davantage de mémoire ; MiniCPM5-1B convient uniquement si le client désactive le raisonnement. Évitez Gemma 3 1B et Qwen3.5 0.8B sur cette configuration précise de 2 Go, car nos essais ont provoqué des redémarrages.

## Raspberry Pi 5 : davantage de choix, avec un compromis de vitesse

Le Pi 5 de 8 Go a exécuté les **25 modèles** du test de vitesse et de mémoire. Le tableau comprend chaque essai, y compris les modèles que nous ne recommandons pas pour des réponses courtes. † indique un GGUF importé. « Think off » désigne le réglage du test de vitesse ; le test de conformité séparé n’a pas nécessairement utilisé ce réglage.

| Modèle | Fichier, GB | Sortie, tok/s | Réponse, s | RSS maximal, MB | Évaluation pour une réponse courte |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Latence la plus faible ; 78 % de conformité répétée |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | À éviter : poids 1 bit et 3/6 en conformité sur un seul passage |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Rapide, mais source absente dans 5 réponses sur 18 |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Option facile du registre ; 61 % de conformité répétée |
| `qwen3:0.6b`, raisonnement désactivé | 0.52 | 23.0 | 4.3 | 1,069 | Sous conditions : 4/6, le réglage de raisonnement compte |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Modèle 1 bit expérimental ; le 6/6 d’un seul passage n’est pas confirmé |
| `minicpm5-1b` †, raisonnement désactivé | 0.69 | 18.4 | 5.1 | 869 | Sous conditions : le raisonnement par défaut produisait des réponses vides |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Tient, mais est plus lent et plus grand que les petits LFM2.5 |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Meilleur pour notre usage ; 89 % de conformité répétée |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Alternative du registre ; 5/6 en conformité |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Meilleure conformité répétée des modèles du registre : 83 % |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6 ; Gemma 3 1B a mieux suivi les règles |
| `qwen3.5:0.8b`, raisonnement désactivé | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 avec le raisonnement par défaut ; à éviter sans contrôle de ce réglage |
| `spark-x2.5-1.7b` †, raisonnement désactivé | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 avec le raisonnement par défaut ; à éviter sans contrôle de ce réglage |
| `qwen3:1.7b`, raisonnement désactivé | 1.36 | 8.1 | 12.4 | 1,867 | Sous conditions ; plus de mémoire et de délai que les petits modèles |
| `minicpm5-2b` †, raisonnement désactivé | 1.56 | 7.7 | 10.9 | 1,787 | Sous conditions ; 5/6 sur un passage, avec trop de puces |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Modèle 3B à essayer ; 5/6 sur un passage |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | À éviter en interaction : décodage lent |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Autre option 3B ; aucun test de conformité rapporté |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Tient, mais répond plus lentement que les options compactes |
| `qwen3.5:2b`, raisonnement désactivé | 2.74 | 5.0 | 16.1 | 3,627 | Mémoire et délai élevés ; aucun test de conformité rapporté |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | À éviter pour des réponses réactives ; 14.3 s avant le premier token |
| `ling-3.0-tiny` †, raisonnement désactivé | 4.82 | 9.9 | 19.4 | 5,071 | Grande empreinte ; 5/6 sur un passage avec un échec d’ancrage |
| `lfm2.5:8b`, raisonnement désactivé | 5.16 | 8.7 | 54.6 | 5,317 | Tient de justesse ; chargement à froid de 34.4 s et réponses trop longues |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | À éviter : swap avec les autres services du Pi |

† GGUF importé. Les temps de réponse et valeurs mémoire viennent du test de vitesse Pi 5 à cinq requêtes ; les scores de conformité viennent de tests séparés à six requêtes. L’absence de score signifie que le respect des règles de réponse n’a pas été démontré.

Les petits modèles LFM2.5 étaient les plus rapides *pour cette charge de réponses courtes*. La version 1.2B offre un compromis pratique sur le Pi 5 testé. Gemma 3 1B est une alternative disponible dans le registre et a mieux respecté les règles de réponse que Qwen2.5 1.5B lors des tests répétés ultérieurs. Un modèle 3B peut valoir le délai supplémentaire pour des requêtes qui demandent plus de capacité, mais ces mesures ne disent pas à elles seules quel modèle répond le mieux.

Le délai de chargement à froid et celui du premier token changent l’expérience. Sur Pi 5, LFM2.5-230M se chargeait en environ **0.21 seconde** et produisait un token visible en **0.37 seconde**. Qwen2.5 1.5B mettait **2.59 secondes** à charger et **3.66 secondes** à afficher son premier token ; Qwen2.5 3B mettait **5.60** et **7.97 secondes**. Pour une question occasionnelle, ces délais peuvent compter davantage que le débit de sortie une fois la génération lancée. Un modèle toujours chargé réduit leur importance, mais occupe de la mémoire entre les requêtes.

D’autres candidats mesurés montrent pourquoi le nombre de paramètres ne suffit pas pour les classer. Avec le raisonnement désactivé, `qwen3:0.6b` a atteint **23.0 tokens/s** sur Pi 5 à **1,069 MB RSS**, tandis que MiniCPM5-1B importé a atteint **18.4 tokens/s** à **869 MB RSS**. `granite4:350m` nécessitait un téléchargement de **0.71 GB** et générait **12.1 tokens/s**, malgré son nom 350M. L’empaquetage et l’architecture changent le rapport entre le nom, la taille du fichier, la mémoire et la vitesse.

Si votre client peut envoyer `think: false` de façon fiable, Qwen3 0.6B et MiniCPM5-1B sont des essais raisonnables comme alternatives à LFM2.5. MiniCPM5-2B, Qwen3 1.7B et Spark-X2.5 1.7B fonctionnaient aussi sur Pi 5, mais sans avantage clair en vitesse et mémoire face à nos choix principaux. Le test de conformité utilisait le raisonnement par défaut pour MiniCPM5-1B et Spark-X2.5 ; leurs réponses vides ne décrivent pas leurs essais de vitesse avec raisonnement désactivé. À l’inverse, une mesure rapide avec raisonnement désactivé ne prouve pas qu’un pont qui omet ce réglage recevra une réponse exploitable.

Si la simplicité d’installation compte davantage que la vitesse brute, Gemma 3 1B et Llama 3.2 1B sont des options plausibles du registre sur Pi 5 de 8 Go. Gemma 3 1B a respecté les règles testées dans **15/18** réponses répétées. Llama 3.2 1B a réussi **5/6** sur un seul passage, ce qui rend son estimation moins certaine. Qwen2.5 1.5B chargeait et répondait plus vite que Gemma 3 1B lors de notre mesure de temps, mais n’a réussi que **4/6** contrôles sur un passage. Choisissez en fonction des besoins de vos propres requêtes.

Pour des requêtes textuelles plus longues ou difficiles, Qwen2.5 3B et Llama 3.2 3B quantifiés sont les options 3B à mémoire modérée sur notre Pi 5 de 8 Go. Nous avons mesuré vitesse et mémoire ; Qwen2.5 3B a réussi **5/6** sur un passage. Aucun test de conformité comparable n’a été rapporté pour Llama 3.2 3B. Leur nombre de paramètres supérieur donne une raison de les *tester* sur des tâches où les petits modèles échouent, mais ne prouve pas qu’ils les résolvent mieux. Granite 4 Micro et Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny et Gemma 3n E2B tenaient ou se chargeaient lors de nos essais Pi 5, mais offraient moins de latence favorable, de marge mémoire ou de fiabilité pour cette application courte.

Les deux modèles Bonsai montrent le coût d’une quantification extrême. Leurs fichiers Q1_0 étaient étonnamment petits pour des noms à 1.7B et 4B paramètres, mais le modèle 1.7B n’a réussi que **3/6** contrôles des règles. Le 4B a réussi un seul passage de six requêtes, mais prenait **18.1 secondes** par réponse et n’a pas été retesté en conformité. Considérez-les comme des expériences plutôt que des recommandations par défaut, surtout si la qualité compte.

Le résultat LFM2.5-8B mérite un contexte : son architecture hybride utilise moins de paramètres actifs par token, donc son débit de décodage a dépassé celui des modèles denses 3B mesurés. Il a tout de même fallu **34.4 secondes** pour le chargement à froid depuis la microSD, avec plus de **5.3 GB de mémoire résidente**. Cela montre ce qui peut tenir, mais n’en fait pas un choix confortable par défaut sur un Pi qui exécute aussi d’autres services. Le `gemma3n:e2b` mesuré utilisait lui aussi environ 5.3 GB de mémoire résidente et provoquait du swap avec les autres services de l’hôte de test.

L’essai LFM2.5 8B a également atteint la limite complète de **140 tokens** au lieu de rester bref. L’essai Gemma 3 4B a mis **14.3 secondes** à produire son premier token et **30.3 secondes** pour répondre entièrement. Les deux modèles se chargent sur ce Pi 5, mais n’ont pas ressemblé à de petits assistants réactifs pendant nos essais. Un très petit modèle avec une réponse courte adaptée peut mieux servir une interface radio ou de commande qu’un modèle plus grand dont le débit de décodage est meilleur sur le papier.

## Mémoire, raisonnement et format du modèle

Une première estimation tirée de nos mesures est **taille de téléchargement du modèle × 1.4** pour la mémoire résidente d’inférence. Ce n’est qu’une règle pratique : la longueur du contexte, les réglages du runtime, l’architecture et les autres processus changent le besoin. Vérifiez la mémoire disponible pendant la génération, gardez un seul modèle chargé sur un petit hôte et laissez de la marge pour l’OS. Une carte de 4 Go peut commencer avec des modèles petits ou compacts, mais nos recommandations 4 Go sont des extrapolations, pas des essais directs sur cette variante.

Par exemple, le fichier LFM2.5-1.2B de 0.73 GB correspondait à environ **967 MB RSS** sur Pi 5, tandis que le fichier Qwen2.5 1.5B de 0.99 GB atteignait **1,361 MB RSS**. La règle fonctionne assez bien pour ces modèles, mais ne constitue pas une limite fixe. Prévoyez plus que la mémoire mesurée du processus si le Pi exécute aussi une interface, un index de recherche, une bibliothèque locale ou un service d’arrière-plan. Surveillez le swap pendant une vraie requête : un modèle qui se charge techniquement mais échange constamment n’est pas exploitable en pratique.

Certains modèles produisent un bloc de raisonnement interne avant leur réponse visible. Lors de nos essais, `qwen3:0.6b` sur le Pi 4 de 2 Go prenait beaucoup plus de temps avant d’afficher du texte. MiniCPM5-1B n’a donné qu’une réponse utile sur cinq avec le raisonnement par défaut, contre cinq sur cinq une fois celui-ci désactivé. Pour un budget de réponse court, définissez `think: false` dans une requête API Ollama compatible, ou choisissez un modèle qui ne raisonne pas par défaut. Ce réglage s’applique aux modèles et clients pris en charge ; ce n’est pas un accélérateur universel.

Cette distinction compte, car la limite de tokens peut inclure ceux consacrés au raisonnement même si l’utilisateur ne voit aucune réponse. Sur Pi 4, `qwen3:0.6b` avec raisonnement par défaut mettait en moyenne **40.4 secondes par requête** ; une réponse visible était vide. MiniCPM5-1B mettait en moyenne **33.3 secondes** avec le réglage par défaut, contre **12.2 secondes** sans raisonnement. Pour les essais Pi 5, nous avons désactivé le raisonnement de Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 et Spark-X2.5 lorsque nos notes l’indiquaient. Comparez chaque modèle avec le réglage que votre client utilisera.

### Vérifier si la réponse est exploitable

Pour notre charge de travail d’assistant mesh à réponse courte, le contrat de réponse compte autant que la vitesse : au plus **90 mots**, pas plus de **trois puces**, du texte brut, une phrase terminée, et l’utilisation du contexte fourni avec son nom de source. Le pont découpe le texte en blocs de **180 caractères**. Une réponse longue occupe davantage le canal radio, même si le modèle l’a générée rapidement.

La version ultérieure du benchmark vérifie les réponses vides, la limite de mots propre au prompt, le nombre excessif de puces, les tableaux ou blocs de code Markdown, une fin inachevée, l’absence de termes du contexte et l’absence du nom de la source. Évalués face au prompt système de l’assistant déployé, les petits modèles enfreignaient souvent ces règles. Les échecs les plus importants étaient les **réponses vides** lorsque le raisonnement épuisait le budget de tokens, puis les réponses qui ignoraient le contexte récupéré ou omettaient sa source. Dépasser le nombre de mots ou de puces produisait quand même du texte visible, mais gaspillait du temps radio. Ces contrôles sont mécaniques et ne remplacent pas la lecture de la réponse : ils ne prouvent ni l’exactitude des faits ni la qualité des conseils de sécurité.

#### Résultats de conformité répétés sur Pi 5

Nous avons d’abord soumis six requêtes une fois par modèle, avec une limite de **220 tokens** et le prompt système déployé. Les modèles prometteurs ont ensuite été testés deux fois de plus avec une seed différente, soit **18 réponses par modèle**. Un passage parfait ne garantit pas des répétitions parfaites. Les résultats répétés ci-dessous offrent une comparaison plus solide pour les réponses mesh courtes testées :

| Modèle | Réponses respectant toutes les règles contrôlées | Principaux échecs observés |
|---|---:|---|
| LFM2.5-1.2B importé | 16/18 (89%) | Deux réponses inachevées |
| `gemma3:1b` | 15/18 (83%) | Trois réponses inachevées |
| LFM2.5-230M importé | 14/18 (78%) | Réponses inachevées et noms de source absents |
| LFM2.5-350M importé | 13/18 (72%) | Noms de source absents |
| `qwen2.5:0.5b` | 11/18 (61%) | Trop de puces et de mots, noms de source absents |

Sur le **Pi 4 de 2 Go**, le contrôle séparé à six requêtes a donné **5/6** à LFM2.5-350M, **4/6** à LFM2.5-230M et **2/6** à Qwen2.5-0.5B. MiniCPM5-1B est passé de **1/6** avec le raisonnement par défaut à **5/6** avec le raisonnement désactivé. Ces résultats Pi 4 ne viennent que d’un passage. Pour les affirmations générales sur le respect des instructions, nous donnons donc plus de poids aux résultats répétés de Pi 5, tout en utilisant les essais Pi 4 pour juger la stabilité et la vitesse sur cette carte.

Les échecs ont des conséquences différentes. Une réponse **vide** n’aide pas l’utilisateur ; une réponse qui ignore les éléments fournis peut induire en erreur. Sans nom de source, les lecteurs ne peuvent pas vérifier l’attribution. Les puces ou mots en trop consomment surtout des paquets supplémentaires de 180 caractères. Une phrase inachevée peut signaler une troncature. L’erreur sur un terme médical de LFM2.5-230M rappelle qu’une réponse peut réussir ces contrôles mécaniques tout en étant fausse. Aucun des cinq modèles testés en répétition n’a suivi toutes les règles dans ses 18 réponses. Une application exigeant une longueur ou un format strict doit aussi les imposer après génération et faire vérifier séparément les contenus à risque.

Nous avons aussi testé le véritable endpoint du pont, `/v1/chat/completions` compatible OpenAI d’Ollama, avec un contexte WikiMed récupéré. Sur Pi 5, LFM2.5-1.2B a donné une réponse de 28 mots avec six termes fournis ; Qwen2.5-0.5B en a donné 38 avec sept termes. Les deux tenaient dans deux paquets de 180 caractères. Ce contrôle confirme que le modèle LFM2.5 importé fonctionne dans le chemin de requête du pont, mais une réponse réussie ne garantit pas sa fiabilité.

Ollama publie de nombreux modèles prêts à télécharger, dont les [variantes Qwen2.5 de 0.5B, 1.5B et 3B](https://ollama.com/library/qwen2.5/tags). Nous avons importé les petits modèles LFM2.5 dans Ollama depuis les [versions GGUF de Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main). Vérifiez le tag précis ou le nom du fichier GGUF avant le téléchargement : les registres et dépôts changent. Gardez les fichiers GGUF sur un stockage persistant ; lors de nos essais, un `/tmp` en RAM consommait la mémoire rare du Pi 4.

### Tags du registre et imports GGUF

Un tag Ollama est le moyen le plus court de faire un premier essai : téléchargez le tag exact et lancez-le. Les petits LFM2.5 de nos tableaux étaient des **imports GGUF**, pas des tags `lfm2.5-230m`, `lfm2.5-350m` ou `lfm2.5-1.2b` dans la bibliothèque publique Ollama. GGUF est un format de fichier modèle ; des noms comme `Q8_0` et `Q4_K_M` indiquent des choix de quantification. Les fichiers LFM2.5 de 230M et 350M utilisés étaient en Q8_0, tandis que le fichier 1.2B était en Q4_K_M. Le même nombre de paramètres avec une autre quantification n’a donc pas nécessairement la même taille, la même mémoire ou la même qualité.

Pour importer la variante 350M testée, téléchargez le GGUF dans un répertoire sur stockage persistant, créez un Modelfile qui pointe vers ce fichier, puis laissez Ollama le copier dans son magasin de modèles :

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

L’import nécessite temporairement assez de place pour le fichier téléchargé et sa copie dans le stockage Ollama. Nous avons utilisé des téléchargements reprenables, car les longs transferts GGUF s’interrompaient parfois. Avant l’import, comparez le SHA-256 du téléchargement au hash publié par sa source ; un transfert incomplet peut autrement ressembler à un problème de modèle. Sur notre Pi, `/tmp` était en RAM : y placer un GGUF réduisait la mémoire disponible pour l’inférence.

## Un point de départ pratique

| Matériel et objectif | Premier modèle à essayer | Pourquoi |
|---|---|---|
| Pi 4 de 2 Go, choix par défaut | LFM2.5-350M importé | Stable à 516 MB RSS avec environ 1 GB disponible ; choisi après l’erreur de terme médical du 230M |
| Pi 4 de 2 Go, latence minimale | LFM2.5-230M importé | 383 MB RSS et 7.2 s de réponse moyenne ; vérifiez attentivement le contenu, surtout en santé ou sécurité |
| Pi 4 de 2 Go, registre uniquement | `qwen2.5:0.5b` | Téléchargement direct depuis Ollama et stabilité lors de notre essai Pi 4 à cinq requêtes ; 61 % de conformité répétée sur Pi 5 |
| Pi 4 de 4 Go ou Pi 5 | LFM2.5-1.2B importé, puis test local | 967 MB RSS et 89 % de conformité répétée sur notre Pi 5 de 8 Go ; variantes 4 Go non mesurées directement |
| Pi 5 de 8 Go, assistant réactif | LFM2.5-1.2B importé | 15.5 tokens/s, 4.7 s par réponse complète et meilleure conformité répétée mesurée |
| Pi 5 de 8 Go, installation via registre uniquement | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS et 83 % de conformité répétée |
| Pi 5 de 8 Go, essai d’un texte plus grand | Qwen2.5 3B ou Llama 3.2 3B quantifiés | Environ 5 tokens/s et 2.4–2.8 GB RSS pour les deux ; Qwen2.5 3B a réussi 5/6 sur un passage |

Ces options privilégient des réponses courtes et utiles sur un Pi susceptible d’exécuter d’autres services. Ce sont des points de départ, pas l’affirmation qu’un modèle est meilleur pour chaque tâche. Lors du contrôle de conformité à passage unique sur Pi 5, `qwen3.5:0.8b` et Spark-X2.5 avec raisonnement par défaut n’ont produit aucune réponse conforme ; MiniCPM5-1B a obtenu 1/6. Si votre client ne peut pas désactiver leur raisonnement, évitez-les pour cette charge de réponses courtes. Testez le modèle final avec le prompt, le contexte, la concurrence et la limite de réponse prévus.

Pour le modèle du registre, après [l’installation d’Ollama pour Linux](https://ollama.com/download/linux), exécutez :

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Testez vos requêtes, la longueur de réponse voulue et les autres services actifs. Notez le temps total de réponse et la mémoire utilisée. Cela indique mieux si un modèle convient à votre Pi que son nombre de paramètres seul.

Sur un nœud à mémoire limitée, surveillez le swap pendant les essais. Si un modèle plus grand rend la carte peu réactive, passez à un modèle plus petit et définissez une limite mémoire adaptée au service Ollama afin qu’un chargement excessif échoue avant d’épuiser l’hôte. Cette limite protège le système, elle ne permet pas de faire tenir un modèle trop grand. Les redémarrages du Pi 4 lors de nos essais montrent pourquoi la réactivité et la marge mémoire comptent autant que les tokens par seconde.

## Transformer le benchmark en décision de déploiement

Avant d’utiliser un modèle au quotidien, fixez quatre limites : **temps de réponse maximal, mémoire résidente maximale, format de réponse et comportement en cas d’échec**. Testez-les avec les services qui partageront la carte. Un modèle qui passe seul mais provoque du swap à côté de votre pont radio ou de votre tableau de bord ne respecte pas les exigences de déploiement.

Gardez un petit modèle de secours installé. Basculez dessus si le modèle principal dépasse sa limite mémoire, renvoie une réponse vide ou enfreint le contrat de réponse. Pour chaque comparaison, notez le tag du modèle, sa quantification, la version d’Ollama, le prompt, la longueur du contexte et la seed afin qu’une mise à jour ultérieure ne ressemble pas à une amélioration matérielle.
