---
title: "Pourquoi Tailscale utilise un relais : connexions directes, DERP et relais pair à pair"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Découvrez pourquoi Tailscale utilise un relais, comment lire les sorties de status et netcheck, et quand examiner une connexion DERP ou par relais pair à pair."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "relais Tailscale", "DERP", "relais pair à pair Tailscale", "connexion directe", "WireGuard", "traversée NAT", "NAT difficile", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "performances VPN", "accès distant", "tailnet", "réseau homelab", "latence du relais", "chiffrement de bout en bout"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Deux ordinateurs portables sur des îles séparées échangent des paquets chiffrés via un relais central alors qu'une route directe est interrompue."
coverCaption: ""
---

**Tailscale utilise un relais** lorsque les appareils n'ont pas établi de connexion directe. Une brève connexion DERP au démarrage est normale. Le recours persistant à un relais indique souvent des conditions de NAT ou de pare-feu qui affectent la route entre les appareils. Les connexions directes, DERP et par relais pair à pair conservent toutes le chiffrement de bout en bout de WireGuard. [Types de connexion Tailscale](https://tailscale.com/docs/reference/connection-types).

## À retenir

- **Identifiez la route :** distinguez les connexions directes, DERP et par relais pair à pair.
- **Rassemblez des éléments :** lancez des sondes visant le pair et vérifiez le réseau aux deux extrémités.
- **Analysez la tendance :** comparez les paires d'appareils et les conditions réseau.
- **Choisissez une modification :** justifiez-la par une charge mesurée et un nouveau test.

## Avant de commencer

**Prérequis :** deux appareils inscrits et en ligne, et un terminal avec l'interface en ligne de commande de Tailscale, ou **CLI**. Un accès administrateur est nécessaire uniquement si l'enquête conduit à modifier la configuration.

**Durée estimée :** cinq minutes pour les vérifications de base, puis 15 à 20 minutes pour l'exercice de comparaison. **Difficulté :** débutant pour l'observation, intermédiaire pour les changements réseau. Définissez d'abord le problème, par exemple une sauvegarde lente ou une réponse tardive du terminal.

## Connexion directe, DERP et relais pair à pair

Un **tailnet** est votre réseau Tailscale. Ses appareils tentent d'établir une connectivité UDP directe. Des relais sont disponibles lorsque la route directe échoue. Tailscale réévalue périodiquement les options de connexion. [Établissement d'une connexion](https://tailscale.com/docs/reference/connection-types).

| Route | Trajet du trafic | Conséquence habituelle |
|---|---|---|
| **Directe** | Entre les deux appareils | Généralement la route privilégiée pour les performances |
| **Relais DERP** | Par l'infrastructure de relais Tailscale | Ajoute un intermédiaire lorsque l'accès direct échoue |
| **Relais pair à pair** | Par un appareil configuré dans votre tailnet | Une autre option de relais que vous administrez |

Les **performances DERP** dépendent en partie du trajet supplémentaire et de la capacité partagée du service. Tailscale documente des limites de débit destinées à partager équitablement les ressources DERP. Aucune vitesse de relais universelle ne permet de prévoir la durée d'un transfert de fichiers. [Résoudre les problèmes de performances Tailscale](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Comprendre la négociation de connexion

La **traversée NAT** consiste à établir une route utilisable à travers des appareils qui traduisent les adresses. Tailscale commence la communication via DERP tout en négociant une route directe. Si la connectivité directe échoue, un relais pair à pair configuré et disponible offre une autre option. Tailscale réévalue ses options au fil du temps. [Établissement d'une connexion](https://tailscale.com/docs/reference/connection-types).

Un **NAT difficile** décrit un comportement de mappage qui complique la traversée. Les conditions aux deux extrémités comptent. Deux appareils derrière des routeurs différents ne se comportent pas nécessairement de la même façon, même si les deux réseaux utilisent des adresses privées. [Connectivité des appareils](https://tailscale.com/docs/reference/device-connectivity).

Pour **un ordinateur portable mobile**, la route vers votre serveur domestique peut changer lorsque vous passez du Wi-Fi de la maison au réseau d'un hôtel. Notez le réseau utilisé pendant l'observation. Une connexion directe observée hier ne décrit pas la route d'aujourd'hui.

## Vérifier la connexion actuelle

Remplacez **`home-server`** par le nom Tailscale ou l'adresse de votre pair :

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** teste la connectivité avec le pair indiqué. **`tailscale status`** affiche les pairs et les détails de connexion. **`tailscale netcheck`** signale les conditions sur l'appareil où vous exécutez la commande. Le [référentiel CLI de Tailscale](https://tailscale.com/docs/reference/tailscale-cli) décrit ces commandes.

| Indicateur de sortie | Interprétation |
|---|---|
| **`direct`** | Le trafic vers ce pair emprunte une route directe |
| **`relay`** | Le trafic vers ce pair passe par DERP |
| **`peer-relay`** | Le trafic emprunte un relais pair à pair configuré |
| **Un premier pong DERP** | Examinez les résultats suivants avant de conclure que la route est restée relayée |

Ces libellés proviennent de la [documentation sur les types de connexion](https://tailscale.com/docs/reference/connection-types). **Générez d'abord du trafic**, puis examinez le pair concerné. Les commandes ci-dessus sont des exemples, pas des résultats issus d'un benchmark.

## Interpréter un changement de route

Cette **séquence illustrative** omet les adresses et les durées pour mettre en évidence le changement de connexion :

```text
Première réponse : réponse via DERP
Réponse suivante : via un point de terminaison direct
État ensuite : connexion directe
```

**Interprétation :** la négociation a abouti pendant cette observation. La première réponse seule aurait mené à un mauvais diagnostic. Si les réponses suivantes et l'état indiquent toujours un relais, consignez le recours persistant à un relais pour cette paire d'appareils et cette période de test.

**Portée de la sonde :** la réussite d'un ping Tailscale confirme la connectivité avec le pair pour cette sonde. Elle ne prouve pas que votre tableau de bord, service de fichiers ou démon SSH accepte le trafic applicatif. Testez séparément l'application défaillante avant de déclarer le problème résolu.

## Ce que révèle netcheck

Exécutez **`tailscale netcheck` sur les deux appareils**. Comparez ces champs avec la [référence sur la connectivité des appareils](https://tailscale.com/docs/reference/device-connectivity) :

| Champ | Interprétation utile |
|---|---|
| **`UDP`** | La sonde a-t-elle observé une connectivité UDP sortante ? |
| **`MappingVariesByDestIP`** | Des mappages externes variables peuvent compliquer la traversée NAT |
| **`IPv6`** | Cet appareil dispose-t-il d'une connectivité IPv6 utilisable ? |
| **`PortMapping`** | Un mécanisme de mappage de port pris en charge est-il disponible ? |

**Un seul champ ne suffit pas à trancher.** La disponibilité d'un mécanisme de mappage ne prouve pas qu'une route vers un pair donné fonctionne. L'étiquette de relais ne permet pas non plus d'identifier le routeur en cause. Comparez les deux extrémités et les résultats réels des pings.

Le **NAT opérateur** compte lorsque la traduction en amont échappe à votre contrôle, comme l'explique notre article sur le [transfert de port de T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/). Ne supposez pas que toutes les connexions derrière le NAT d'un opérateur se comportent de la même manière.

## Comparer trois paires d'appareils

Si possible, utilisez un **troisième appareil inscrit** pour enrichir les éléments disponibles. Le modèle suivant est hypothétique, il ne s'agit pas d'un résultat mesuré :

| Paire d'appareils | Route observée |
|---|---|
| **Ordinateur portable vers serveur domestique** | DERP |
| **Ordinateur portable vers un autre serveur** | Directe |
| **Serveur domestique vers un autre serveur** | DERP |

**Hypothèse de travail :** examinez d'abord le réseau du serveur domestique, car les deux routes observées qui l'impliquent sont passées par un relais. C'est un indice, pas une preuve. Chaque paire négocie séparément et le serveur de comparaison a ses propres conditions réseau.

**Prochaine observation :** recueillez les résultats de netcheck sur les trois appareils et répétez le test entre l'ordinateur portable et le serveur domestique depuis un autre réseau que vous contrôlez. Si la route change, notez précisément le réseau qui a changé. N'attribuez pas le résultat à une règle de pare-feu avant de l'avoir testée.

**Exercice :** la connexion entre l'ordinateur portable et le serveur domestique est directe, mais le transfert de fichiers reste lent. L'explication par un relais ne correspond plus à cette observation. Avant de modifier les paramètres du relais, vérifiez la connexion montante sous-jacente, la charge du serveur, le stockage et le comportement de l'application.

## Choisir une modification ciblée

Commencez par un **test comparatif** sur un autre réseau que vous contrôlez. Si le même pair devient accessible directement, vous obtenez un élément utile sur la route réseau initiale. Examinez les restrictions UDP et la configuration NAT avant de modifier des paramètres DNS ou applicatifs sans rapport.

**Ne modifiez qu'une variable**, relancez les vérifications et mesurez la même charge. Notez le sens du transfert, la taille du fichier, la durée écoulée et le type de connexion. Vous pourrez ainsi distinguer l'amélioration de la route d'un changement indépendant de la charge du serveur ou du stockage.

Les **modifications du pare-feu** doivent suivre les recommandations propres à la plateforme et s'appuyer sur les éléments recueillis. Ouvrir un port applicatif à l'Internet public n'améliore pas à lui seul le transport Tailscale. Limitez les modifications au trafic nécessaire et au réseau que vous administrez. [Recommandations de Tailscale sur les pare-feu](https://tailscale.com/docs/integrations/firewalls).

| Constat | Modification à évaluer |
|---|---|
| **La sonde UDP échoue** | Examinez les restrictions UDP sortantes de ce réseau |
| **Le mappage varie selon la destination** | Examinez le comportement NAT des équipements que vous gérez |
| **Route directe, application lente** | Examinez l'hôte, la connexion sous-jacente et la charge |
| **Relais fonctionnel, expérience acceptable** | Conservez la configuration et notez la valeur de référence |

*Privilégiez une amélioration mesurée plutôt qu'une modification visant uniquement à supprimer l'étiquette de relais.*

## Évaluer un relais pair à pair

Un **relais pair à pair** nécessite un hôte adapté, un port UDP accessible et une politique d'accès qui autorise son utilisation. Le relais et les clients participants doivent tous utiliser Tailscale 1.86 ou une version ultérieure. Vérifiez les plateformes hôtes prises en charge avant d'affecter un appareil à cette fonction. [Exigences des relais pair à pair](https://tailscale.com/docs/features/peer-relay).

**L'emplacement détermine son utilité.** Un appareil derrière la même limite réseau inaccessible n'aide pas les autres pairs tant que le port du relais n'est pas accessible.

**Coût de maintenance :** une personne doit maintenir le relais en ligne, à jour et suffisamment dimensionné. Pour une administration occasionnelle avec une latence acceptable, comparez cette charge au bénéfice mesuré. En cas de transferts volumineux répétés, mesurez la charge via le relais envisagé avant de l'adopter.

## Vérifier les effets du trafic partagé

Le **trafic agrégé** mérite attention lorsqu'un routeur de sous-réseau ou un nœud de sortie transporte plusieurs charges via DERP. Tailscale documente des cas où un important trafic relayé retarde le trafic sensible à la latence qui partage la connexion. [Résoudre les problèmes de NAT difficile](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Exercice de comparaison :** observez votre session interactive avant, pendant et après une sauvegarde volumineuse. Gardez la même paire de points de terminaison et notez la route à chaque étape. Les délais qui apparaissent pendant le transfert justifient d'étudier la charge partagée, mais ne permettent pas d'en établir la cause exacte.

**Choisissez le test suivant** à partir de l'observation. Vérifiez la saturation du lien et la charge de l'hôte, puis évaluez une route directe ou la séparation des services sensibles à la latence si la topologie le permet. Ne considérez pas un symptôme DNS comme une preuve automatique d'une erreur de configuration DNS.

## Un relais est-il un nœud de sortie ?

Un **nœud de sortie** achemine le trafic Internet général d'un client via un appareil sélectionné du tailnet. Un relais transporte le trafic entre des pairs Tailscale. Le choix d'un nœud de sortie ne garantit pas une route directe vers celui-ci. [Documentation sur les nœuds de sortie](https://tailscale.com/docs/features/exit-nodes).

## Créer un relevé de diagnostic

Conservez un **court relevé avant et après** pour le problème réel :

```text
Date et versions de Tailscale :
Appareils source et destination :
Réseaux utilisés par chaque appareil :
Routes initiale et stabilisée :
Observations netcheck aux deux extrémités :
Charge, direction et durée :
Modification unique testée :
Résultat du nouveau test :
Décision de conserver ou d'annuler la modification :
```

**Critère d'achèvement :** le relevé relie un symptôme précis à des observations, une hypothèse et un nouveau test mesuré. « Le relais a disparu » ne suffit pas si l'application reste lente. « La sauvegarde respecte le délai requis via DERP » constitue un résultat valide si le délai est explicite.

**Utilisez `tailscale netcheck` comme élément de preuve, pas comme verdict.** La commande décrit le réseau vu par un seul appareil. La route stabilisée dépend d'une paire d'appareils et d'une charge. Avant de modifier le pare-feu ou le NAT, consignez les deux extrémités, la dernière ligne de `tailscale status` et la mesure de l'application.

## Étapes suivantes

Notez la route vers votre pair important et testez la charge avant de modifier les paramètres réseau. Pour savoir séparément qui exploite votre infrastructure de coordination, consultez [Tailscale ou Headscale](/articles/tailscale-vs-headscale-comparison-guide/).
