---
title: "Cartes Virtuelles Privacy.com : Comment Fonctionne la Confidentialité des Paiements"
date: 2023-09-03
lastmod: 2026-10-08
toc: true
draft: false
description: Ce qui est stocké sur une carte de paiement, pourquoi la bande magnétique est la partie la plus faible, ce qu’un commerçant voit lorsque vous payez avec un numéro virtuel, et comment les types et limites de cartes de Privacy.com fonctionnent en pratique.
genre:
- Sécurité des Paiements
- Confidentialité Numérique
- Cartes Virtuelles
- Confidentialité Financière
- Prévention de la Fraude
- Sécurité des Consommateurs
tags:
- privacy.com
- cartes virtuelles
- cartes de débit virtuelles
- cartes à usage unique
- cartes verrouillées sur un commerçant
- cartes verrouillées par catégorie
- tokenisation
- jeton réseau
- numéro de compte principal
- cvv
- skimming de carte
- bande magnétique
- piste 1
- piste 2
- sécurité des cartes de paiement
- fraude à la carte de crédit
- gestion des abonnements
- limites de dépenses
- pci dss
- soc 2
- fraude sans présentation de carte
- confidentialité financière
- confidentialité des paiements
- numéro de carte virtuelle
- carte masquée
- contrôles de carte
cover: /img/cover/privacy_virtual_cards.webp
coverAlt: Une illustration numérique montrant une carte virtuelle protégée par un bouclier protégeant un symbole de cadenas, représentant la sécurité et la confidentialité offertes par les cartes de débit virtuelles.
coverCaption: Protégez, Contrôlez et Sécurisez Vos Transactions en Ligne.
ref:
- /magnetic-stripe-decoder
- /articles/personal-security-checklist-prioritized-2026
- /personal-security-course/personal-finance
---

**Une carte virtuelle fait une chose spécifique : elle change ce que le commerçant reçoit, pas ce que votre banque sait.** C’est tout le mécanisme, et le comprendre explique à la fois la protection que vous obtenez et celle que vous n’obtenez pas.

La plupart des articles traitent les cartes virtuelles comme un outil général de confidentialité et évitent les détails techniques. Cet article couvre ce qui est stocké sur une carte, pourquoi la bande magnétique est le point faible, et comment les types de cartes de Privacy.com se comportent en pratique.

*Le bénéfice pratique est étroit et réel : un numéro volé devient inutile pour un voleur, car il ne fonctionne qu’avec le commerçant pour lequel il a été émis.*

## La Réponse Courte

| Question | Réponse Courte |
|---|---|
| **Qu’est-ce qu’une carte virtuelle change ?** | Le numéro que le commerçant stocke. Vos vraies informations de carte ne leur parviennent jamais |
| **La transaction est-elle privée ?** | Non. Votre banque, le réseau et l’émetteur la voient toujours |
| **Qu’est-ce qui empêche une faille de vous nuire ?** | Un numéro verrouillé sur un commerçant ou à usage unique, qui échoue ailleurs |
| **Quelle est la partie la plus faible d’une carte physique ?** | La bande magnétique, qui stocke les données complètes des pistes en clair |
| **Cela construit-il du crédit ?** | Non. Ce ne sont pas des comptes de crédit et aucun contrôle de crédit n’a lieu |
| **Qui peut utiliser Privacy.com ?** | Citoyens ou résidents légaux américains, 18 ans et plus, avec un compte courant bancaire ou coopérative de crédit aux États-Unis |

## Ce Qui Se Trouve sur une Carte de Paiement

**Trois éléments autorisent une transaction sans présentation de carte : le numéro de compte principal, la date d’expiration, et la valeur de vérification.**

| Élément | Longueur | Origine |
|---|---|---|
| **Numéro de Compte Principal (PAN)** | Jusqu’à 19 chiffres | L’émetteur, avec des chiffres initiaux identifiant le réseau et la banque |
| **Expiration** | Quatre chiffres au format MM/AA | L’émetteur |
| **CVV ou CVC** | Trois ou quatre chiffres | Dérivé du PAN, de l’expiration, et d’une clé détenue uniquement par l’émetteur |
| **Nom du titulaire** | Jusqu’à 26 caractères | Apparaît seulement sur la piste 1 de la bande magnétique |

**Le PAN n’est pas une chaîne aléatoire.** Le premier chiffre identifie le réseau, les suivants identifient la banque émettrice, et le reste identifie le compte. Cette structure permet de vérifier la plausibilité d’un numéro de carte sans contacter personne, et explique pourquoi le chiffre de contrôle de Luhn détecte une seule erreur de chiffre.

**Le CVV prouve que quelqu’un a physiquement tenu la carte** lors de son émission. Il n’est pas stocké sur la bande magnétique, ce qui explique pourquoi un skimmer copiant la bande ne l’obtient jamais.

*Inspectez tout cela vous-même avec le **[Décodeur et Encodeur de Bande Magnétique](/magnetic-stripe-decoder/)**, qui analyse les pistes 1 et 2, décode les chiffres du code de service, et réencode le résultat. Il fonctionne entièrement dans votre navigateur, ce qui est important car c’est le contenu complet d’une carte de paiement.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Schéma montrant les éléments d’une carte de paiement incluant le numéro de compte principal, la date d’expiration, le CVV, et les trois pistes de la bande magnétique avec ce que chacune contient" >}}

## Pourquoi la Bande Magnétique Est le Point Faible

**La bande stocke les données du compte en clair, et tout lecteur compatible peut les lire.**

Une bande magnétique contient jusqu’à trois pistes. La piste 1 porte le PAN, le nom du titulaire, l’expiration, et un code de service à trois chiffres, et c’est la seule piste contenant du texte alphabétique. La piste 2 porte le PAN, l’expiration, et le code de service dans un encodage numérique plus dense, et **c’est la piste 2 que presque tous les terminaux de point de vente lisent.** La piste 3 est pratiquement inutilisée par les grands réseaux et souvent absente de la carte.

Le code de service mérite d’être compris, car il décrit l’usage autorisé de la carte. Le premier chiffre couvre les règles d’interchange, le deuxième la gestion des autorisations, et le troisième la gamme de services. Une carte codée `201` permet l’interchange international, ne nécessite pas de chemin d’autorisation spécial, et n’a pas de restrictions de service.

L’histoire explique pourquoi la bande a duré si longtemps. En 1969, un ingénieur IBM nommé Forrest Parry a essayé de coller une bande magnétique sur une carte plastique et n’a pas réussi à la faire adhérer sans l’endommager. Sa femme a suggéré d’utiliser un fer à repasser, et la chaleur a collé la bande à la carte. Cette improvisation est devenue la norme pendant plus d’un demi-siècle.

Deux évolutions y mettent fin :

| Étape clé | Statut |
|---|---|
| **Mastercard a annoncé la suppression de la bande** | D’ici 2033, aucune carte Mastercard crédit ou débit n’en portera |
| **Europe** | Les bandes ont commencé à disparaître des cartes Mastercard en 2024 |
| **États-Unis** | Les banques cesseront de les émettre à partir de 2027 |

*La bande a été remplacée par la puce et le paiement sans contact car copier une bande ne demande aucune compétence autre que posséder un lecteur. Notre **[outil de bande magnétique](/magnetic-stripe-decoder/)** montre combien peu de données suffisent à reconstruire une piste fonctionnelle.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Schéma d’une bande magnétique montrant la position physique des pistes un, deux et trois, avec la disposition des champs de chaque piste incluant les sentinelles, le PAN, le nom, l’expiration et le code de service" >}}

## Comment Lire les Données des Pistes

**Une chaîne de bande magnétique est une séquence de champs, pas un second numéro de carte.** Le lecteur trouve la sentinelle de début, sépare les champs, lit l’expiration et le code de service, puis vérifie la sentinelle de fin et le LRC.

| Piste | Début | Champs principaux | Fin | Jeu de caractères |
|---|---|---|---|---|
| **Piste 1** | `%` | Code de format, PAN, nom, date d'expiration, code de service, données discrétionnaires | `?` plus LRC | ALPHA six bits, donc il contient des lettres |
| **Piste 2** | `;` | PAN, date d'expiration, code de service, données discrétionnaires | `?` plus LRC | BCD quatre bits, donc il contient des chiffres et un petit ensemble de ponctuation |

Les sentinelles optionnelles identifient les limites physiques de l'enregistrement. Un décodeur les omet souvent lorsqu'il affiche les champs, mais un encodeur physique a besoin du format complet de l'enregistrement attendu par le lecteur.

### Exemple de Piste 1

Ceci est un exemple synthétique. Il utilise le PAN de test standard de l'outil ainsi qu'un faux nom, une fausse date d'expiration, un code de service et des données discrétionnaires. Ce n'est pas une carte Privacy.com et ce ne sont pas des données de paiement valides.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Lisez-le de gauche à droite :

| Segment | Valeur | Signification |
|---|---|---|
| **Sentinelle de début** | `%` | Début de l'enregistrement de la Piste 1 |
| **Code de format** | `B` | Format de carte financière B |
| **PAN** | `4111111111111111` | Numéro de compte principal synthétique |
| **Séparateur de champ** | `^` | Fin du PAN et début du nom |
| **Nom** | `TEST/USER` | Nom de famille, séparateur, prénom |
| **Séparateur de champ** | `^` | Fin du nom et début des champs de transaction |
| **Date d'expiration** | `2912` | Décembre 2029 au format AA/MM |
| **Code de service** | `501` | Interchange national, traitement normal, aucune restriction |
| **Données discrétionnaires** | `0000000` | Remplissage défini par l'émetteur dans cet exemple |
| **Sentinelle de fin** | `?` | Fin des données de la Piste 1 avant le LRC |

L'enregistrement encodé réel porte aussi un caractère LRC après la sentinelle de fin lorsque le lecteur l'attend. La forme texte visible est utile pour étudier la structure. La représentation au niveau des bits porte aussi une parité impaire pour chaque caractère.

### Exemple de Piste 2

La Piste 2 supprime le nom et le code de format. Les mêmes valeurs synthétiques deviennent :

```text
;4111111111111111=291250100000000?
```

| Segment | Valeur | Signification |
|---|---|---|
| **Sentinelle de début** | `;` | Début de l'enregistrement de la Piste 2 |
| **PAN** | `4111111111111111` | Numéro de compte principal synthétique |
| **Séparateur** | `=` | Fin du PAN et début des champs de transaction |
| **Date d'expiration** | `2912` | Décembre 2029 au format AA/MM |
| **Code de service** | `501` | Même code de service synthétique que la Piste 1 |
| **Données discrétionnaires** | `0000000` | Remplissage défini par l'émetteur dans cet exemple |
| **Sentinelle de fin** | `?` | Fin des données de la Piste 2 avant le LRC |

**La Piste 2 est plus courte car elle ne contient pas le nom du titulaire.** De nombreux terminaux lisent la Piste 2 pour les transactions par glissement ordinaires, tandis que la Piste 1 fournit le champ nom lorsqu'un lecteur le demande.

### Chiffres du Code de Service

**Les trois chiffres du code de service décrivent le comportement du terminal et de l'autorisation.** Ils ne contiennent pas le CVV, et les modifier sur une vraie carte sans autorisation de l'émetteur produit un identifiant de paiement mal formé ou trompeur.

| Chiffre | Valeurs | Ce qu'il décrit |
|---|---|---|
| **Premier** | `0`, `1`, `2`, `5`, `6`, `7`, `9` | Règles d'interchange et préférence puce |
| **Deuxième** | `0`, `1`, `2`, `4` | Chemin d'autorisation |
| **Troisième** | `0` à `7` | Restrictions sur PIN, espèces, biens et services |

**Le premier chiffre** couvre l'interchange et la préférence puce :

| Valeur | Signification |
|---|---|
| `0` | Usage national |
| `1` | Interchange international autorisé |
| `2` | Interchange international, utiliser IC (puce) si possible |
| `5` | Interchange national uniquement sauf accord bilatéral |
| `6` | Interchange national uniquement sauf accord bilatéral, utiliser IC si possible |
| `7` | Pas d'interchange sauf accord bilatéral (boucle fermée) |
| `9` | Test |

**Le deuxième chiffre** couvre la gestion de l'autorisation :

| Valeur | Signification |
|---|---|
| `0` | Autorisation normale |
| `1` | Autorisation normale |
| `2` | Contacter l'émetteur en ligne |
| `4` | Contacter l'émetteur en ligne sauf accord bilatéral |

**Le troisième chiffre** couvre les restrictions de service :

| Valeur | Signification |
|---|---|
| `0` | Aucune restriction, PIN requis |
| `1` | Aucune restriction |
| `2` | Biens et services uniquement (pas d'espèces) |
| `3` | Guichet automatique uniquement, PIN requis |
| `4` | Espèces uniquement |
| `5` | Biens et services uniquement (pas d'espèces), PIN requis |
| `6` | Aucune restriction, utiliser le PIN si possible |
| `7` | Biens et services uniquement (pas d'espèces), utiliser le PIN si possible |

Par exemple, `201` signifie interchange international avec utilisation de la puce si possible, traitement normal de l'autorisation, et aucune restriction de service. Le décodeur expose chaque chiffre séparément pour que vous n'ayez pas à mémoriser le tableau.

### LRC et Parité

**Le LRC est un caractère de contrôle, pas un autre champ à inventer.** L'encodeur fait un XOR des valeurs de données de chaque caractère depuis la sentinelle de début jusqu'à la sentinelle de fin. Il convertit le résultat dans la plage de caractères imprimables de la piste et rapporte séparément les bits de parité impaire encodés.

La Piste 1 utilise un jeu de caractères ALPHA à six bits. Sa valeur de données est le code ASCII moins `0x20`. La Piste 2 utilise un jeu de caractères BCD à quatre bits. Sa valeur de données est le nibble bas du code ASCII. Appliquer la correspondance de la Piste 1 à la Piste 2 produit un LRC incorrect.

L'option **Inclure le LRC calculé** du décodeur ajoute le caractère LRC imprimable à la sortie. Sa décomposition montre aussi le motif de bits LRC avec parité impaire. Utilisez ceci pour apprendre comment un lecteur vérifie l'enregistrement, pas pour contourner les contrôles d'un émetteur.

## Écriture de Cartes Synthétiques pour Tests

**Utilisez le décodeur pour écrire des chaînes de test, pas des cartes de paiement réelles.** L'outil accepte des champs, reconstruit les Pistes 1 et 2, ajoute les sentinelles optionnelles et calcule le LRC. Il fonctionne localement dans le navigateur.

1. Ouvrez le **[Décodeur et Encodeur de Bande Magnétique](/magnetic-stripe-decoder/)**.
2. Sélectionnez **Charger la carte de test**. Cela remplit l'outil avec le PAN synthétique `4111111111111111`, le nom `TEST/USER`, la date d'expiration `2912`, le code service `201`, et les données discrétionnaires de test.
3. Activez **Inclure les sentinelles de début et de fin** pour afficher les limites physiques de l'enregistrement.
4. Activez **Inclure le LRC calculé** pour ajouter le caractère de contrôle calculé.
5. Activez **Diviser les données discrétionnaires en PVKI, PVV et CVV** uniquement pour voir comment un champ synthétique de neuf chiffres est affiché. Ces étiquettes sont des conventions de l'émetteur, pas une disposition universelle de la piste 1 ou piste 2.
6. Modifiez le nom, la date d'expiration, le code service ou les données discrétionnaires synthétiques. La sortie se met à jour au fur et à mesure de la saisie.
7. Comparez les champs décodés avec les chaînes générées. Effacez les champs une fois terminé.

Pour un exercice sur une piste 1 synthétique, utilisez :

```text
PAN: 4111111111111111
Surname: TEST
First name: USER
Expiry: 12/29
Service code: 201
Discretionary data: 000000000
```

Pour un exercice sur une piste 2 synthétique, utilisez le même PAN, la même date d'expiration, le même code service, et un champ discrétionnaire numérique. La chaîne générée pour la piste 2 omet le nom car la piste 2 ne comporte pas de champ nom.

**Ne copiez pas un PAN, une date d'expiration, un CVV ou une valeur discrétionnaire Privacy.com en direct dans une carte réinscriptible.** Privacy.com décrit son produit comme des numéros de carte virtuels créés via son site web ou son application. Sa page officielle ne présente pas le service comme un système d’écriture de bande magnétique, et un numéro de carte virtuel n’est pas une preuve d’un enregistrement physique autorisé par l’émetteur. Une carte de test réinscriptible contenant un identifiant en direct crée un instrument de paiement dupliqué et viole les conditions de l’émetteur ou les règles de paiement.

La limite de sécurité est simple : utilisez l’échantillon synthétique intégré à l’outil, utilisez une carte de laboratoire avec des valeurs factices, et utilisez une carte physique approuvée par l’émetteur lorsque vous devez payer en personne. N’essayez pas de transformer une carte virtuelle Privacy.com en carte à bande magnétique physique.

## Ce que change une carte virtuelle

**Une carte virtuelle est un second numéro qui se place devant le premier.**

Lorsque vous payez avec une carte virtuelle, le commerçant reçoit un numéro, une date d’expiration et un CVV appartenant à la carte virtuelle. Votre vrai PAN ne leur parvient jamais. En pratique, le changement se manifeste après une fuite de données :

| Scénario | Avec votre vraie carte | Avec une carte virtuelle verrouillée sur un commerçant |
|---|---|---|
| **Base de données du commerçant divulguée** | Le numéro est valide partout où il est accepté | Le numéro échoue chez tous les autres commerçants |
| **Abonnement que vous avez annulé** | Les prélèvements continuent jusqu’à contestation | Vous fermez la carte et le prélèvement échoue |
| **Essai converti silencieusement** | Prélèvement non désiré sur votre relevé | La limite ou la fermeture l’empêche |
| **Détails de carte vendus sur un forum** | Utilisable pour fraude sans présence de la carte | Utilisable chez un seul commerçant, si tant est |


**Ce que cela ne change pas** est tout aussi important. Votre banque voit toujours la transaction. Le réseau de paiement la traite toujours. L’émetteur détient toujours votre identité, car les règles anti-blanchiment exigent une vérification. **Une carte virtuelle réduit l’exposition côté commerçant. Ce n’est pas un moyen de dépenser anonymement.**

*Cette distinction embrouille constamment les gens. Si votre modèle de menace inclut l’émetteur ou le réseau, une carte virtuelle ne change rien à cela.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Schéma montrant un numéro de carte virtuelle envoyé au commerçant tandis que le vrai numéro de carte reste entre le titulaire et la banque émettrice" >}}

## Les trois types d’objet en forme de carte

La terminologie est utilisée de manière incohérente, et la différence importe lorsque vous choisissez ce que vous remettez à un commerçant.

| Type | Numéro de carte | Version physique | Usage typique |
|---|---|---|---|
| **Carte numérique** | Identique à votre carte physique | Oui | Ajouter votre carte existante à un portefeuille mobile |
| **Carte virtuelle** | Différente de toute carte physique | Non | Achats en ligne, abonnements, commerçants ponctuels |
| **Carte numérique d’abord** | Différente, avec une carte physique liée optionnelle | Optionnelle | Comptes fintech où la carte physique ne porte aucun détail imprimé |

**Un portefeuille mobile utilise un mécanisme entièrement différent.** Lorsque vous ajoutez une carte à un portefeuille, celui-ci stocke un jeton spécifique à l’appareil plutôt que votre PAN, et le commerçant reçoit ce jeton. Cela s’appelle la tokenisation, et c’est pourquoi payer avec un téléphone est plus sûr que de remettre la carte plastique même sans carte virtuelle.

*La tokenisation réseau et les cartes virtuelles résolvent des parties qui se chevauchent du même problème. La tokenisation protège le numéro en transit et au repos. Une carte virtuelle vous protège de ce que le commerçant conserve ensuite.*

## Types de cartes Privacy.com

**Privacy.com propose quatre comportements de carte, et ils ne sont pas interchangeables.**

| Type de carte | Comportement | Idéal pour |
|---|---|---|
| **Usage unique** | Se ferme automatiquement après une transaction | Achats ponctuels et commerçants inconnus |
| **Verrouillée sur commerçant** | Verrouille sur le premier commerçant qui la débite et échoue ailleurs | Achats en ligne quotidiens |
| **Verrouillée par catégorie** | Restreinte à une catégorie de dépenses | Contenir une classe entière de dépenses |
| **Partout** | Carte physique avec le même modèle de protection | Achats en personne |

**Le verrouillage sur commerçant est le mécanisme qui apporte le plus de valeur.** Une carte verrouillée échoue chez tout commerçant autre que celui avec lequel elle a été utilisée en premier, ce qui signifie qu’une fuite chez ce commerçant rend le numéro inutile ailleurs.

**L’usage unique est l’option la plus forte là où elle s’applique.** Une carte qui se ferme après un débit ne peut pas être rejouée, et elle supprime le besoin de penser à la fermer plus tard.

Deux détails opérationnels à connaître :

- **Les cartes partagées se verrouillent sur le premier commerçant avec lequel elles sont utilisées**, donc les partager avec un membre de la famille ou un employé conserve la restriction commerçant.
- **Une carte est mise en pause plutôt que fermée.** La pause est réversible, ce qui est utile quand vous voulez arrêter temporairement un abonnement sans perdre les détails de la carte.

## Limites de dépenses et contrôles

**Chaque carte porte une limite de dépense, qui est un contrôle distinct du verrouillage commerçant.**

| Contrôle | Ce qu’il empêche |
|---|---|
| **Limite par transaction** | Un débit unique supérieur à ce que vous avez autorisé |
| **Limite mensuelle** | Des débits cumulés sur une période de facturation |
| **Pause** | Tout débit, de manière réversible |
| **Fermeture** | Tout débit futur, de manière permanente |

**Définissez à la fois une limite par transaction et une limite mensuelle sur toute carte liée à un abonnement.** Une augmentation silencieuse du prix par un commerçant atteint la limite plutôt que votre solde, et vous le remarquez grâce à un débit échoué plutôt qu’une ligne manquante sur le relevé.

*Notre module **[Sécurité des Finances Personnelles](/personal-security-course/personal-finance/)** place cela aux côtés des gels de crédit et de la tokenisation des cartes comme les trois contrôles limitant ce qu’un commerçant compromis unique peut atteindre.*

## Plans et ce que chacun débloque

Privacy.com propose un niveau gratuit ainsi que trois formules payantes. Les prix et les limites des fonctionnalités évoluent, vérifiez donc les conditions actuelles avant de vous abonner.

| Forfait | Prix | Ajouts Notables |
|---|---|---|
| **Personnel (gratuit)** | 0 $ | Cartes virtuelles, verrouillage commerçant, limites de dépenses, pas de frais sur les transactions nationales |
| **Plus** | 5 $/mois | Cartes par catégorie, notes sur les cartes pour organiser les dépenses |
| **Pro** | 10 $/mois | Cashback sur achats éligibles, cartes physiques Everywhere |
| **Premium** | 25 $/mois | Tout ce qui est dans Pro, avec la limite mensuelle de création de cartes portée à 60 |

**Le niveau gratuit couvre le bénéfice principal en matière de sécurité.** Le verrouillage commerçant, les cartes à usage unique et les limites de dépenses sont les mécanismes qui réduisent l’exposition, et ils sont disponibles sans paiement. Les formules payantes ajoutent de l’organisation et de la commodité plutôt qu’une protection supplémentaire.

**Les frais de transaction à l’étranger varient selon le forfait.** Le niveau gratuit applique 3 % sur les transactions étrangères avec un minimum de 0,50 $, tandis que les formules payantes n’en appliquent pas.

## Ce que Privacy.com ne fait pas

**Être clair sur les limites est plus utile qu’une liste de fonctionnalités.**

| Limitation | Détail |
|---|---|
| **Il ne vous rend pas anonyme** | Votre identité est vérifiée à l’inscription et l’émetteur la détient |
| **Il ne cache pas la transaction à votre banque** | Votre banque voit le transfert de fonds, et le réseau voit la charge |
| **Il ne construit pas de crédit** | Ce ne sont pas des comptes de crédit, et aucun contrôle de crédit n’a lieu |
| **Il est réservé aux États-Unis** | Nécessite la citoyenneté ou la résidence légale américaine et un compte bancaire ou coopérative de crédit US |
| **Il exige une vérification d’identité** | Les contrôles Know Your Customer sont obligatoires selon les règles anti-blanchiment |
| **Il ne couvre pas tous les commerçants** | Certains commerçants bloquent les plages de cartes prépayées et virtuelles |

**Le point sur le blocage des commerçants est important en pratique.** Certains services d’abonnement et compagnies aériennes rejettent les plages de cartes qu’ils associent aux cartes virtuelles ou prépayées, et aucune configuration ne résout ce problème. Gardez une carte réelle disponible en secours dans ces cas.

*Résumé honnête : une carte virtuelle est un contrôle de confinement pour l’exposition côté commerçant, pas un outil d’anonymat. Si vous avez besoin d’anonymat, c’est un problème différent avec des outils différents.*

## Qui émet la carte et pourquoi c’est important

**Une carte virtuelle reste une vraie carte, émise par une vraie banque, sous une vraie licence de réseau.**

| Détail | Valeur |
|---|---|
| **Banque émettrice** | Patriot Bank, N.A., membre FDIC |
| **Licences de réseau** | Mastercard et Visa |
| **Où elle est acceptée** | Partout où Mastercard et Visa sont acceptés |
| **Financement** | Transféré depuis votre compte courant US lié |

**C’est pourquoi la protection est réelle.** La carte bénéficie des mêmes protections réseau que tout autre produit Mastercard ou Visa, ce qui signifie que les droits de rétrofacturation et les procédures de contestation de fraude s’appliquent normalement. Ce n’est pas une carte cadeau ni un crédit magasin fermé.

Deux certifications méritent d’être citées car elles sont vérifiables indépendamment et non de simples arguments marketing :

- **Conformité PCI-DSS**, la norme de l’industrie des cartes de paiement pour la gestion des données des titulaires
- **SOC 2 Type II**, un rapport audité couvrant les contrôles de sécurité sur une période plutôt qu’une simple déclaration ponctuelle

**Sur le modèle économique :** la société déclare gagner des commissions d’interchange auprès des commerçants et ne vend pas les données clients à des annonceurs ou tiers. C’est le même modèle de revenus que tous les autres émetteurs de cartes, ce qui mérite d’être compris plutôt que perçu comme inhabituel.

*La raison pratique de vérifier la banque émettrice est la vérification. N’importe qui peut prétendre gérer un programme de cartes, et le nom de l’émetteur sur la carte est ce que vous confirmez par rapport à la banque indiquée dans les documents.*

Inspectez le réseau et la banque via le préfixe PAN avec le **[Décodeur de bande magnétique](/magnetic-stripe-decoder/)**, qui indique la plage majeure du réseau et valide le chiffre de contrôle Luhn.

## Bien utiliser les cartes virtuelles

**Les contrôles ne servent que si vous les configurez.** Six habitudes apportent la majeure partie du bénéfice.

1. **Verrouillez chaque carte à un commerçant** sauf raison contraire. Le verrouillage rend un numéro divulgué inutile.
2. **Utilisez l’usage unique pour tout ce qui est inconnu**, y compris les essais et achats ponctuels sur des sites plus petits.
3. **Fixez les deux limites de dépenses** sur les cartes d’abonnement, pour qu’une augmentation de prix échoue plutôt que d’être débitée.
4. **Nommez chaque carte d’après le commerçant**, pour que la liste des transactions soit lisible et qu’une charge inattendue ressorte.
5. **Mettez en pause plutôt que fermez** quand vous prévoyez de reprendre un service, et fermez quand vous ne le ferez pas.
6. **Gardez une carte réelle pour les commerçants qui rejettent les plages virtuelles**, afin qu’un paiement bloqué ne devienne pas une urgence.

> **Erreur courante : considérer une carte virtuelle comme un substitut à la vigilance sur vos relevés.** Le verrouillage commerçant empêche une catégorie de dommages. Il ne détecte pas un compte compromis à votre banque, un transfert non autorisé ou une charge frauduleuse sur la vraie carte associée.

## Points clés à retenir

- **Une carte virtuelle change le numéro que le commerçant stocke.** Votre vrai PAN ne leur parvient jamais, c’est tout le mécanisme.
- **Elle ne rend pas la transaction privée.** Votre banque, le réseau et l’émetteur la voient toujours, et la vérification d’identité est obligatoire.
- **Le verrouillage commerçant est la fonctionnalité la plus précieuse**, car un numéro divulgué échoue alors partout ailleurs.
- **Le niveau gratuit inclut les contrôles de sécurité.** Les plans payants ajoutent organisation et commodité plutôt que protection.
- **La bande magnétique stocke les données de la carte en clair** et sera supprimée d’ici 2033, les banques US arrêtant l’émission en 2027.
- **Le CVV n’est pas sur la bande**, c’est pourquoi un skimmer copiant les pistes ne dispose pas de ce que beaucoup de commerçants en ligne exigent.
- **Certains commerçants rejettent les plages de cartes virtuelles.** Gardez une carte réelle en secours.
- **Vérifiez la banque émettrice** plutôt que de faire confiance à une affirmation de programme de cartes, et contrôlez vous-même le préfixe PAN.

## Étapes suivantes

1. **Inspectez les données de piste de votre propre carte** et voyez exactement ce que contient une bande magnétique : **[Décodeur et encodeur de bande magnétique](/magnetic-stripe-decoder/)**
2. **Gelez votre crédit** si ce n'est pas déjà fait, c'est le contrôle le plus efficace contre la fraude liée à l'ouverture de nouveaux comptes : **[Sécurité financière personnelle](/personal-security-course/personal-finance/)**
3. **Appliquez la discipline de hiérarchisation** pour décider de l'effort à consacrer selon votre situation : **[Liste de contrôle de sécurité personnelle priorisée](/articles/personal-security-checklist-prioritized-2026/)**
4. **Examinez les plans et conditions actuelles de Privacy.com** avant de vous abonner : **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Vérifiez si vos données apparaissent déjà dans une fuite** avant de supposer que vous n’êtes pas affecté : **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Lisez la liste de contrôle de sécurité des paiements** pour la contrepartie organisationnelle : **[Liste de contrôle de réponse aux incidents](/checklists/incident-response-checklist/)**

## Références

1. [Privacy.com - ce que sont les cartes virtuelles, verrouillage commerçant et limites de dépenses](https://www.privacy.com/virtual-card)
2. [Carte numérique - Wikipédia, couvrant cartes numériques versus virtuelles, pistes de bande magnétique, codes de service, parité et LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 - cartes d'identification, cartes de transaction financière, structure des données des pistes 1 et 2](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 - disposition détaillée des champs de piste, incluant sentinelles et codes de service](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [Conseil des normes de sécurité PCI - exigences pour l’environnement des données des titulaires de carte](https://www.pcisecuritystandards.org/)
6. [Bureau de protection financière des consommateurs - rapports et scores de crédit](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [Encodage de données ANSI/ISO ALPHA, jeu de caractères de la piste 1 et tableau de parité](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [Caractères ISO des cartes magnétiques, jeux de la piste 1 et piste 2 côte à côte](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Lecture des données de carte magnétique, guide pratique avec scan en direct d’une carte](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)
