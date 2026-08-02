---
title: "Caméras Flock : Outil de Sécurité Publique ou Machine de Surveillance sans Mandat ?"
date: 2026-08-01
toc: true
draft: false
description: "Une analyse indépendante des caméras ALPR de Flock Safety : comment elles fonctionnent réellement, quelles données elles collectent au-delà des plaques d'immatriculation, comment le partage de données crée une base de données nationale fantôme, et pourquoi la question du mandat est le véritable enjeu."
genre: ["Vie Privée", "Surveillance", "Libertés Civiles", "Technologie des Forces de l'Ordre", "Droits Numériques"]
tags: ["Flock Safety", "ALPR", "lecteurs de plaques d'immatriculation", "surveillance", "vie privée", "surveillance sans mandat", "analyse de convoi", "suivi Bluetooth", "suivi TPMS", "partage de données", "caméras Ring", "Quatrième Amendement", "rien à cacher", "précision LPR", "accusation erronée", "MFA", "technologie des forces de l'ordre", "libertés civiles", "minimisation des données", "DeFlock", "contre-surveillance", "sécurité publique", "surveillance policière", "droits à la vie privée", "Quatrième Amendement", "surveillance numérique", "surveillance de masse", "reconnaissance de plaques d'immatriculation", "réseaux de caméras", "conservation des données"]
cover: "/img/cover/flock-cameras-public-safety-or-surveillance-2026.webp"
coverAlt: "Une intersection sombre éclairée par une caméra de surveillance montée sur un poteau, avec des données de plaque d'immatriculation superposées sur les voitures qui passent."
coverCaption: ""
canonical: "https://simeononsecurity.com/articles/flock-cameras-public-safety-or-surveillance-2026/"
---

**Le débat sur les caméras de Flock Safety divise les gens d'une manière que presque rien d'autre ne fait dans la politique technologique. Ceux qui ont eu une voiture volée ont tendance à les adorer. Ceux qui étudient le droit constitutionnel ont tendance à les détester. Les deux réagissent à quelque chose de réel.**

Ceci est une analyse indépendante de ce que ces systèmes font réellement, de ce que les preuves disent sur leur précision et leur mauvais usage, et pourquoi la question la plus importante n'est pas de savoir si les caméras peuvent photographier les rues publiques — mais si le gouvernement devrait construire une base de données consultable et sans mandat des déplacements de tout le monde.

{{< youtube id="fFuE2-xtq2w" >}}

*Ce sujet a suscité un débat public important à la mi-2026. La vidéo ci-dessus couvre un éventail de perspectives de spectateurs et de contre-arguments qui méritent d'être considérés en parallèle avec l'analyse présentée ici.*

______

## Pourquoi les Caméras Flock Sont Différentes de Votre Téléphone

La défense la plus courante des caméras de Flock Safety est la suivante : votre téléphone vous suit déjà partout. La police peut obtenir vos données GPS avec un mandat. Les caméras Flock sont moins précises que cela. Alors pourquoi s'inquiéter ?

L'argument est superficiellement raisonnable et fondamentalement faux.

**Votre téléphone vous suit, vous. Les caméras Flock suivent tout le monde.** Lorsque la police obtient vos données de localisation par les tours de téléphonie mobile ou votre historique GPS, elle a besoin d'un mandat, d'une cible spécifique et d'une cause probable. Lorsqu'un agent interroge la base de données de Flock, il n'a besoin d'aucune de ces choses. Il peut effectuer des recherches par numéro de plaque, fenêtre temporelle, emplacement ou description du véhicule — sans mandat, sans suspect nommé, sans aucun soupçon.

Le résultat est une **surveillance de masse sans mandat d'une population entière**, et non une surveillance ciblée d'un individu spécifique. Le Quatrième Amendement a été spécifiquement conçu pour prévenir exactement ce type de recherche générale.

Le suivi des téléphones portables ne crée pas non plus d'enregistrement permanent et consultable de chaque véhicule ayant passé chaque intersection de votre ville au cours des 30 derniers jours. Flock le fait. Cette base de données persistante et structurée est ce qui la rend qualitativement différente d'un policier notant un numéro de plaque ou d'une entreprise installant une caméra de sécurité.

**Une photographie n'est pas un système de surveillance. Une base de données consultable et horodatée de photographies reliées par l'identité du véhicule sur des centaines de caméras en est un.**

______

## Ce que Signifie Réellement l'"Analyse de Convoi"

Flock Safety commercialise une fonctionnalité appelée **analyse de convoi** — la capacité de suivre plusieurs véhicules qui se déplacent ensemble en groupe. Le langage marketing est anodin. Les implications ne le sont pas.

L'analyse de convoi signifie que Flock peut identifier quand deux véhicules spécifiques ou plus se déplacent ensemble, corréler leurs schémas de déplacement dans le temps et signaler quand un groupe historiquement associé se réunit à nouveau. Dans un contexte d'application de la loi, cela pourrait signifier suivre des organisateurs de manifestations qui se rendent aux mêmes endroits, identifier quelles voitures assistent à des réunions politiques, ou surveiller des personnes qui se rassemblent régulièrement dans le même quartier.

Aucune de ces personnes n'a besoin d'avoir fait quoi que ce soit d'illégal pour que ses associations de convoi soient enregistrées et stockées.

La fonctionnalité a des applications légitimes — suivre les véhicules d'une organisation criminelle présumée, par exemple. Mais la même fonctionnalité appliquée à une base de données sans exigence de mandat signifie qu'elle peut être utilisée sur n'importe qui. C'est l'infrastructure de la surveillance politique, que ce soit ou non l'intention aujourd'hui.

______

## Ce que les Caméras Flock Collectent Au-delà des Plaques d'Immatriculation

La plaque d'immatriculation est le point de données le plus visible, mais ce n'est pas le seul. Voici ce que les preuves montrent sur la collecte de signaux plus large par ces réseaux de caméras.

### Détection des Adresses MAC Bluetooth et WiFi

**C'est réel, documenté et fréquemment sous-rapporté.**

De nombreux déploiements ALPR — pas seulement Flock — incluent une capacité de numérisation WiFi et Bluetooth. Lorsque le WiFi ou le Bluetooth de votre téléphone est activé et non connecté, il émet des **requêtes de sonde** incluant l'adresse MAC de votre appareil. Une caméra équipée d'une radio WiFi peut enregistrer passivement ces adresses en même temps que la lecture de la plaque.

Cela est d'une importance énorme : votre adresse MAC est liée à *vous*, pas à votre voiture. Si vous montez dans le véhicule de quelqu'un d'autre, louez une voiture ou conduisez une voiture empruntée, votre téléphone continue d'émettre votre identité. L'analyse de convoi peut désormais inclure les identités au niveau des appareils de chaque passager, pas seulement du conducteur.

Même si le déploiement qui vous préoccupe ne fait pas cela actuellement, la capacité matérielle et logicielle existe souvent. La question de quelles données sont *collectées* et quelles données sont *conservées* sont des questions distinctes, et l'audit de la conformité est pratiquement impossible sans exigence publique de mandat.

### Suivi des Capteurs TPMS

Les **capteurs du Système de Surveillance de la Pression des Pneumatiques (TPMS)** transmettent un identifiant unique sur des fréquences radio UHF. Ces identifiants ne sont pas chiffrés et sont émis lorsque le pneu roule. Des chercheurs ont démontré que des détecteurs TPMS passifs le long des routes peuvent enregistrer les identités des véhicules — et contrairement aux plaques d'immatriculation, les identifiants TPMS ne sont pas visibles du public et ne peuvent pas être changés sans remplacer les capteurs.

Un identifiant TPMS correspond à un ensemble spécifique de pneus. Lorsque ces pneus sont montés sur un véhicule, l'identifiant TPMS est fonctionnellement équivalent à une plaque d'immatriculation que vous ne saviez pas avoir et que vous ne pouvez pas afficher différemment.

Ce n'est pas une capacité hypothétique future. Les récepteurs RTL-SDR capables d'enregistrer les signaux TPMS coûtent environ 40 dollars. La barrière technique au déploiement d'une surveillance TPMS passive aux côtés d'un réseau ALPR est très faible.

______

## Le Vrai Problème : Photographie contre Base de Données

Prendre une photo d'une voiture dans une rue publique est légal. Un policier notant une plaque d'immatriculation est légal. La caméra de sécurité d'un voisin enregistrant la circulation est légale.

Aucune de ces activités n'est la même que **construire une base de données centralisée, consultable et conservée indéfiniment de tous les mouvements de véhicules dans une ville entière**.

Le droit légal d'observer les espaces publics ne s'étend pas automatiquement au droit d'agréger ces observations dans une infrastructure de surveillance qui fonctionne comme une filature continue de 30 jours de chaque personne qui conduit.

La Cour Suprême a reconnu cette distinction. Dans *Carpenter v. United States* (2018), la Cour a jugé que même si les données des tours de téléphonie mobile consistent en des enregistrements déjà fournis à un tiers, l'agrégation de ces données dans le temps en un enregistrement complet des déplacements d'une personne nécessite un mandat. La Cour a explicitement noté que la surveillance généralisée modifie le calcul constitutionnel.

Les caméras de Flock Safety font exactement ce dont *Carpenter* avait mis en garde — à grande échelle, automatiquement, sans mandats, sur l'ensemble de la population.

______

## Partage de Données et le Réseau National Fantôme

Les réseaux individuels de caméras Flock ne sont pas isolés. Les villes et les comtés concluent des **accords de partage de données** avec les juridictions voisines, ce qui signifie qu'une requête dans une ville peut récupérer des enregistrements de dizaines d'autres. Certains de ces accords de partage sont suffisamment permissifs pour qu'une seule agence puisse effectivement accéder à une base de données régionale ou quasi nationale.

**C'est ainsi qu'un réseau local de caméras devient de facto un système de surveillance national sans que le Congrès n'ait jamais voté sur la question.**

Le partage de données est volontaire et légalement flou. Il n'existe aucune loi fédérale l'autorisant. Il n'y a pas de limites standardisées de conservation des données. Il n'y a pas d'exigences d'audit obligatoires. Et il n'existe aucun mécanisme permettant à un citoyen de découvrir si les déplacements de son véhicule ont été consultés.

DeFlock.org, qui recense collaborativement les emplacements des caméras Flock, a cartographié plus de **124 000 déploiements LPR présumés** aux États-Unis. La couverture dans les zones urbaines et suburbaines est suffisamment dense pour que la conduite dans la plupart des villes américaines génère un enregistrement de surveillance quasi continu.

______

## Caméras Ring, Flock et Mandats

Flock Safety et Amazon Ring sont des produits différents, mais ils partagent une caractéristique critique : les deux peuvent donner aux forces de l'ordre accès à des données sans nécessiter de mandat.

Ring a suscité une controverse considérable lorsqu'il est devenu public qu'Amazon avait remis des images à des agences des forces de l'ordre des milliers de fois — dans de nombreux cas sans la connaissance ou le consentement du propriétaire de la caméra. Amazon a finalement modifié certaines de ses politiques après des pressions publiques, mais le cadre juridique sous-jacent n'a pas changé.

Flock fonctionne selon un modèle similaire. Les caméras sont généralement installées par des municipalités ou des associations de propriétaires, mais l'infrastructure de données est contrôlée par une entreprise privée. Lorsque la police demande des données, elle peut les obtenir via des dispositions d'accès d'urgence, des portails des forces de l'ordre, ou simplement parce que l'agence locale y a déjà accès.

**L'absence d'exigence de mandat n'est pas un bug dans ces systèmes. C'est le modèle économique.**

Les demandes de documents publics (FOIA aux États-Unis, FOI au Canada) peuvent parfois révéler quelles agences ont interrogé les systèmes Flock, mais de nombreuses agences traitent les journaux de requêtes Flock comme des dossiers d'enquête internes et en refusent l'accès.

______

## Démystifier le "Rien à Cacher"

L'argument du "rien à cacher" est la réponse la plus courante aux préoccupations en matière de surveillance, et il reflète une incompréhension profonde de ce à quoi sert la vie privée.

**La vie privée ne concerne pas le fait de cacher une culpabilité. Il s'agit de préserver l'autonomie.**

Les gens ont des intérêts légitimes en matière de vie privée dans des activités qui ne sont pas criminelles : assister à des réunions politiques, consulter des médecins, aller à des services religieux, parler à des journalistes, ou simplement conduire où ils veulent sans qu'un enregistrement permanent ne soit établi. Le fait que toutes ces activités soient légales ne signifie pas que le gouvernement a un intérêt légitime à les cataloguer.

L'histoire fournit une réponse directe à "rien à cacher". Les Américains d'origine japonaise qui ont été internés pendant la Seconde Guerre mondiale n'étaient pas des criminels. Les militants surveillés par COINTELPRO n'étaient pas des criminels. Les personnes figurant sur des listes d'interdiction de vol qui s'y trouvaient par erreur bureaucratique n'étaient pas des criminels. Les données qui ont permis ces abus ont été recueillies avec exactement la même logique — sécurité publique, évaluation des menaces, application efficace de la loi.

**L'infrastructure de surveillance construite aujourd'hui sera utilisée par quiconque détiendra le pouvoir demain.** La question de savoir si le gouvernement actuel est digne de confiance est sans pertinence. La question est de savoir si vous seriez à l'aise avec l'idée que le gouvernement futur le plus hostile imaginable ait accès à un enregistrement permanent de partout où vous avez conduit au cours de la dernière décennie.

______

## Quand la Reconnaissance des Plaques d'Immatriculation Se Trompe

Les systèmes ALPR ne sont pas parfaitement précis, et les conséquences d'une erreur sont sérieuses.

Les erreurs de reconnaissance des plaques d'immatriculation tombent dans plusieurs catégories :

- **Caractères mal lus** — des lettres et des chiffres qui se ressemblent sous un mauvais éclairage ou à grande vitesse (0/O, 1/I, 8/B, M/N/H)
- **Lectures partielles** — des plaques sales, obstruées ou endommagées qui ne correspondent que partiellement
- **Erreurs de base de données** — des plaques signalées comme volées qui ont depuis été effacées
- **Collisions de plaques régionales** — deux États ou pays peuvent émettre la même combinaison de plaque, et un résultat sur une plaque californienne peut signaler à tort un véhicule d'un État avec la même chaîne alphanumérique

Des exemples réels documentent tous ces cas. Des personnes ont eu des armes pointées sur elles lors d'arrêts de circulation parce que leur véhicule a été incorrectement associé à une voiture volée. Des personnes ont reçu des factures de péage pour des routes sur lesquelles elles n'ont jamais conduit. Une personne conduisant une Hyundai bleu ciel a reçu une facture de péage pour une Harley-Davidson conduite par quelqu'un avec une plaque différant de deux lettres.

**Le taux d'erreur multiplié par le volume de lectures produit un nombre significatif de personnes réelles qui seront incorrectement signalées, arrêtées, fouillées ou pire.**

Comme la plupart de ces requêtes se produisent sans mandats, il n'y a aucun contrôle judiciaire sur l'exactitude des données sous-jacentes avant qu'une action soit prise.

______

## Défaillances de Sécurité : MFA et Identifiants Partagés

Les pratiques de sécurité de Flock Safety ont été publiquement critiquées sur plusieurs points :

- **Pas d'authentification multi-facteurs obligatoire** pour les comptes des forces de l'ordre dans de nombreux déploiements
- **Identifiants de connexion partagés** entre plusieurs agents dans certaines agences
- **Pas de délai d'expiration automatique de session** dans certaines configurations
- **Aucune alerte lorsque les comptes sont consultés depuis des emplacements ou à des heures inhabituels**

Ce ne sont pas des détails d'implémentation mineurs. Ils signifient qu'un seul identifiant compromis — obtenu par hameçonnage, ingénierie sociale ou simple réutilisation de mot de passe — pourrait donner à un attaquant accès pour interroger un réseau Flock régional couvrant des millions de lectures de plaques d'immatriculation.

Pour les victimes de violence domestique, les victimes de harcèlement, ou les journalistes, l'existence d'une base de données partagée et minimalement sécurisée de leurs déplacements en véhicule n'est pas une préoccupation abstraite. C'est un risque direct pour la sécurité physique.

L'argument selon lequel "les caméras ne font que collecter des données publiques" ignore l'exigence de sécurité pour la *couche de base de données* qui agrège ces données. Même si chaque photographie individuelle est légalement prise, la base de données agrégée nécessite une protection plus forte qu'un mot de passe partagé.

______

## Le Système Pourrait-il Être Mieux Conçu ?

**Les contrôles techniques seuls ne sont pas suffisants, mais ils valent la peine d'être envisagés.**

Plusieurs propositions ont été discutées pour rendre les systèmes ALPR plus difficiles à abuser :

**Minimisation des données par conception** : Au lieu de stocker des images complètes de plaques d'immatriculation avec des horodatages et des coordonnées GPS, le système pourrait stocker un **hachage cryptographique** de la plaque associé à une localisation et un temps approximatifs. Une requête des forces de l'ordre confirmerait si une plaque spécifique a été vue dans une zone spécifique dans une fenêtre temporelle spécifique, mais ne pourrait pas récupérer une liste de tous les endroits où cette plaque a été vue. Cela limite l'utilité pour les enquêtes générales tout en préservant la capacité de répondre à des questions d'investigation ciblées.

**Conservation limitée dans le temps** : Les plaques non associées à une enquête ouverte pourraient être automatiquement supprimées après 24 à 72 heures plutôt qu'être conservées pendant 30 jours ou plus. La plupart des utilisations investigatives légitimes nécessitent des données en quasi temps réel. La conservation à long terme crée un risque disproportionné pour les libertés civiles.

**Exigences de mandat avec contrôle judiciaire** : Le contrôle le plus important est juridique plutôt que technique. Exiger un mandat pour toute consultation de l'historique des plaques d'un individu nommé n'empêcherait pas les utilisations d'urgence (des exceptions pour circonstances urgentes existent déjà dans la loi) mais empêcherait l'exploration de données routinière sans mandat qui n'a actuellement aucun contrôle.

**Journalisation d'audit avec transparence publique** : Chaque requête devrait être enregistrée, ces journaux devraient être auditables par des organes de contrôle, et les statistiques agrégées devraient être publiées.

Ces mesures ne rendraient pas ALPR sans risque, mais réduiraient considérablement le potentiel d'abus routinier tout en préservant l'utilité investigative que les partisans valorisent.

______

## Le Débat n'A Pas à Être Tout ou Rien

La discussion autour des caméras Flock s'effondre souvent dans deux positions extrêmes : les caméras sont des outils essentiels de lutte contre la criminalité et toute critique aide les criminels, ou les caméras sont un État de surveillance inconstitutionnel et doivent être retirées immédiatement.

Ces deux positions sont erronées, et la polarisation rend plus difficile d'avoir la conversation qui compte vraiment.

**Les caméras peuvent photographier les rues publiques. Les données doivent être encadrées par la loi.**

La technologie ne va pas disparaître. Les applications légitimes de sécurité publique sont réelles. Mais le modèle de déploiement actuel — dans lequel une entreprise privée construit et contrôle une base de données de surveillance quasi nationale que les forces de l'ordre peuvent interroger sans mandat — est constitutionnellement suspect et historiquement dangereux.

La voie à suivre n'est pas de détruire les caméras. C'est d'exiger des mandats pour les recherches individuelles, de mandater de courtes fenêtres de conservation des données, d'interdire le partage de données ouvert sans justification spécifique au cas, et de créer des mécanismes d'audit et de supervision applicables.

C'est une réponse ennuyeuse et procédurale. Elle ne génère pas d'indignation des deux côtés. Mais c'est la seule réponse qui prend au sérieux à la fois la sécurité publique et la liberté constitutionnelle.

______

## Articles Connexes

| Article | Ce que Vous Apprendrez |
|---------|------------------|
| **[Surveillance par Caméras Flock Safety : Prévalence, Préoccupations en Matière de Vie Privée et Stratégies de Protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Analyse complète du réseau Flock, cas d'abus documentés et étapes pratiques de protection |
| **[Flock Finder : Cartographiez Chaque Caméra Flock Présumée Près de Vous](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Comment utiliser l'outil open-source pour visualiser plus de 40 000 caméras présumées à l'aide des données WiGLE |
| **[Guide du Matériel de Détection Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Construisez ou achetez un appareil basé sur ESP32 pour détecter les caméras Flock en temps réel |
| **[Comment Flasher Rayhunter sur les Appareils de Détection d'IMSI Catcher](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Détectez les stingrays et les IMSI catchers — l'équivalent cellulaire du suivi ALPR |
| **[Comparaison des Appareils Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Choisissez le bon matériel pour une boîte à outils complète de contre-surveillance |

______

## Références

1. [Carpenter v. United States, 585 U.S. 296 (2018)](https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf)
2. [ACLU — Lecteurs Automatiques de Plaques d'Immatriculation](https://www.aclu.org/news/by-issue/automatic-license-plate-readers)
3. [Electronic Frontier Foundation — Qu'est-ce que l'ALPR ?](https://www.eff.org/pages/what-alpr)
4. [DeFlock](https://deflock.org/)
5. [Carte Interactive DeFlock](https://maps.deflock.org/)
6. [Site Officiel de Flock Safety](https://www.flocksafety.com/)
7. [Vulnérabilités de Sécurité et de Confidentialité des Réseaux Sans Fil en Voiture : Étude de Cas du Système de Surveillance de la Pression des Pneumatiques](https://www.winlab.rutgers.edu/~gruteser/papers/xu_tpms10.pdf)
8. [FBI Vault — COINTELPRO](https://vault.fbi.gov/cointel-pro)
9. [MuckRock — Flock Safety](https://www.muckrock.com/tags/flock-safety/)
10. [Flock Finder GitHub](https://github.com/simeononsecurity/flock-finder)
11. [Carte Interactive Flock Finder](https://simeononsecurity.github.io/flock-finder/)
