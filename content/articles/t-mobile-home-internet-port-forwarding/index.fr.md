---
title: "Pourquoi le transfert de ports ne fonctionne pas avec T-Mobile Home Internet"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Comprenez les limites du transfert de ports sur T-Mobile 5G Home Internet, le NAT opérateur et les moyens pratiques d'accéder à un serveur domestique sans port entrant public."
genre: ["Networking", "Self-Hosted", "Network Security"]
tags: ["T-Mobile Home Internet", "transfert de ports T-Mobile", "5G Home Internet", "CGNAT", "NAT opérateur", "NAT", "accès distant", "serveur domestique", "homelab", "passerelle T-Mobile", "mode pont", "IP dynamique", "IPv4 public", "double NAT", "Tailscale", "Cloudflare Tunnel", "Cloudflare Access", "réseau privé", "connexions entrantes", "Internet mobile"]
cover: "/img/cover/t-mobile-home-internet-port-forwarding.webp"
coverAlt: "Une passerelle cellulaire domestique se connecte à une tour distante et à une limite réseau partagée, près d'une connexion cloud lumineuse."
coverCaption: ""
---

**Les passerelles grand public de T-Mobile 5G Home Internet** ne proposent pas de transfert de ports configurable. Ajouter une règle sur un second routeur ne modifie pas les paramètres de la passerelle de l'opérateur et ne crée pas de route entrante publique. T-Mobile ne documente pas non plus de bascule vers le mode pont ni de réglage du type de traduction d'adresses réseau (NAT). [Paramètres de la passerelle T-Mobile](https://www.t-mobile.com/support/home-internet/connect).

Cet article porte sur **Home Internet par réseau cellulaire**. Traitez la fibre et les produits professionnels comme des services distincts avec leurs propres fonctionnalités documentées.

## À retenir

- **Repérez la limite :** distinguez une fonction de la passerelle de la traduction d'adresses en amont.
- **Examinez la route :** notez à quel appareil appartient chaque adresse et chaque port.
- **Comparez les solutions :** associez les besoins des clients et du protocole à une méthode d'hébergement.
- **Consignez la décision :** préparez un plan de connexion comprenant un test et une solution de repli.

## Avant de commencer

**Public visé :** les abonnés de T-Mobile Home Internet cellulaire qui veulent accéder à un service domestique depuis l'extérieur. **Prérequis :** accès au serveur, à ses paramètres réseau locaux et aux informations d'état de la passerelle fournie. Une seconde connexion Internet est utile pour le dernier test à distance.

**Durée estimée :** 15 à 20 minutes pour recueillir les besoins et effectuer les vérifications locales. Configurer une autre méthode d'accès demande davantage de temps. **Difficulté :** débutant à intermédiaire. L'objectif est de choisir une connexion en connaissance de cause, pas d'ajouter une autre règle inutilisée au routeur.

## Pourquoi une règle de port locale ne suffit pas

Le **transfert de ports** dirige le trafic entrant d'un routeur vers une destination interne. Pour recevoir du trafic Internet non sollicité, un serveur domestique doit être accessible à travers chaque appareil concerné en amont. Une connexion locale réussie confirme que le serveur est joignable depuis le réseau domestique, pas depuis l'extérieur.

Le **NAT opérateur (CGNAT)** ajoute une traduction d'adresses dans le réseau du fournisseur. Les abonnés partagent la capacité IPv4 publique, tandis que le fournisseur contrôle la traduction externe. La RFC 6598 réserve **`100.64.0.0/10`** à l'espace d'adresses partagé utilisé pour ce type de déploiement. [RFC 6598](https://www.rfc-editor.org/rfc/rfc6598.html).

**La prise en charge par la passerelle et le NAT opérateur sont deux problèmes distincts.** La page d'assistance de T-Mobile établit la restriction de la passerelle. Le CGNAT explique pourquoi configurer votre propre routeur ne suffit pas non plus lorsque la traduction en amont échappe à votre contrôle. L'absence d'un menu de transfert de ports ne révèle pas à elle seule l'architecture complète du réseau de l'opérateur.

**En pratique, vous devez choisir un modèle de connexion.** Utilisez un réseau overlay pour l'accès privé, un tunnel sortant pour un service HTTP ou un endpoint hébergé si les utilisateurs externes ont besoin d'un accès public. Testez la méthode choisie depuis un autre réseau. Une requête LAN réussie ne prouve pas l'accessibilité depuis Internet.

| Changement | Effet | Point non résolu |
|---|---|---|
| **Règle sur un second routeur** | Redirection sur votre routeur | Passerelle de l'opérateur et route en amont |
| **Autre résolveur DNS** | Résolution des noms | Connectivité entrante |
| **Nom DNS dynamique** | Nom suivant une adresse | Route entrante utilisable |
| **Wi-Fi plus rapide** | Performances sans fil locales | Accès depuis Internet |

L'**adressage dynamique** signifie qu'une adresse change au fil du temps. Il ne s'agit pas du partage d'adresse par NAT. T-Mobile documente l'adressage dynamique et ne décrit pas sur cette page d'assistance d'option grand public pour rendre l'adresse Home Internet statique. [Limites de connexion de T-Mobile](https://www.t-mobile.com/support/home-internet/connect).

## Suivre la propriété des adresses

Dans un **exemple de NAT opérateur**, le trajet traverse plusieurs frontières distinctes :

```text
Client distant -> traduction opérateur -> passerelle domestique -> routeur facultatif -> serveur
                     contrôlée par l'opérateur   appareils et paramètres locaux
```

**Une adresse visible par un site web** décrit la connexion qui atteint ce site. Elle n'établit pas de mappage entrant vers votre serveur. Les exigences CGN décrivent les mappages à l'aide de l'identité de l'abonné, de l'adresse externe, du port et de l'heure. [RFC 6888](https://www.rfc-editor.org/rfc/rfc6888.html).

**Notez l'interface :** distinguez l'adresse locale du serveur, l'adresse WAN du second routeur, l'adresse indiquée par la passerelle cellulaire et l'observation d'un service externe. Ici, **WAN** désigne le côté amont d'un routeur. Une adresse sans nom d'interface constitue un indice de diagnostic faible.

Examinez cette **observation illustrative**, avec des adresses réservées à la documentation côté public :

| Point d'observation | Exemple | Interprétation |
|---|---|---|
| **LAN du serveur** | `192.168.50.10` | Destination locale |
| **WAN du second routeur** | `192.168.12.20` | Un autre réseau privé se trouve en amont |
| **Vérification IPv4 externe** | `203.0.113.25` | Adresse visible de l'extérieur |

**Conclusion étayée :** le second routeur se trouve derrière un autre réseau privé. **Conclusion non étayée :** sa valeur WAN révèle précisément la configuration de traduction de l'opérateur. Examinez séparément la passerelle cellulaire si sa page d'état affiche l'adresse pertinente.

**Indice sur la plage d'adresses :** une adresse côté fournisseur dans `100.64.0.0/10` appartient à l'espace partagé. Notez l'interface qui la signale. Si un outil de réseau privé attribue aussi des adresses de cette plage, une capture d'écran sans étiquette est ambiguë. La plage est définie par [RFC 6598](https://www.rfc-editor.org/rfc/rfc6598.html).

## Vérifier le service local

Pour un **tableau de bord HTTP**, lancez cette requête depuis un autre appareil Linux ou macOS du réseau domestique. Remplacez l'adresse et le port d'exemple par ceux de votre serveur :

```bash
curl --connect-timeout 5 --max-time 10 --output /dev/null --write-out '%{http_code}\n' http://192.168.50.10:8080/
```

**`--connect-timeout`** limite le temps d'établissement de la connexion. **`--max-time`** limite la durée totale de la requête. **`--output`** ignore le corps de la réponse et **`--write-out`** affiche le statut HTTP. Ces options figurent dans le [manuel de curl](https://curl.se/docs/manpage.html).

**Interpréter le résultat :** une réponse HTTP, y compris une réponse d'authentification, indique qu'un endpoint HTTP a répondu sur cette route. Vérifiez son identité dans le navigateur. Un délai d'attente ne permet pas d'identifier la couche défaillante. Vérifiez ensuite l'adresse d'écoute, le port et le pare-feu de l'hôte.

*Cette vérification concerne HTTP. Un jeu utilisant UDP requiert un test adapté à son protocole.*

## Choisir une solution adaptée au service

**L'accès privé** et **l'hébergement public** ont des exigences différentes. Commencez par décider qui doit se connecter et si ces personnes acceptent d'installer un client.

**TCP** transporte un flux ordonné au sein d'une connexion. **UDP** transporte des datagrammes individuels. L'hébergement doit prendre en charge le transport utilisé par l'application, même si deux services utilisent le même numéro de port.

| Besoin | Approche à évaluer | Contrainte principale |
|---|---|---|
| **Votre ordinateur portable doit accéder au serveur domestique** | Réseau privé Tailscale | Inscrire les appareils et configurer les règles d'accès |
| **Tableau de bord privé dans le navigateur** | Cloudflare Tunnel avec Access | Configurer le nom d'hôte et la politique d'identité |
| **Site web pour visiteurs publics** | Hébergement public ou tunnel adapté | Examiner le protocole, la capacité et les besoins du service |
| **Serveur de jeu pour des clients classiques** | Hébergement avec prise en charge documentée des ports entrants | Respecter les besoins TCP/UDP du jeu |

**Tailscale** tente une connexion directe et prend en charge le trafic relayé si la communication directe échoue. Vous évitez ainsi de transférer manuellement un port domestique, même si le trajet obtenu influe sur les performances. Lisez la [présentation des connexions Tailscale](https://tailscale.com/docs/reference/connection-types) et notre [explication des relais](/articles/why-tailscale-uses-a-relay/).

**Cloudflare Tunnel** établit une connexion sortante depuis votre serveur. Pour un tableau de bord privé, associez-le à une politique Access. Un nom d'hôte publié sans cette politique n'ajoute aucune vérification d'identité. Consultez la [connectivité Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) et la comparaison [Tunnel et Access](/articles/cloudflare-tunnel-vs-access/).

**Un abonnement VPN seul** ne définit pas un dispositif d'hébergement entrant. Avant d'acheter un service, vérifiez les protocoles pris en charge, les ports exposés, les options d'authentification et les restrictions. Pour un serveur de jeu, demandez précisément quels ports UDP il exige.

## Et IPv6 ?

**L'adressage IPv6 et l'autorisation du trafic entrant** sont deux exigences distinctes. IPv6 réduit la dépendance à la traduction des adresses IPv4, tandis que le filtrage avec état de la passerelle contrôle toujours les connexions entrantes. La RFC 6092 décrit le filtrage IPv6 résidentiel, notamment le traitement du trafic non sollicité. Elle ne documente pas les paramètres de votre passerelle T-Mobile. [Recommandations de sécurité pour l'IPv6 résidentiel](https://www.rfc-editor.org/rfc/rfc6092.html).

**Évaluez toute la route :** le client distant doit disposer d'une connectivité IPv6, le serveur doit avoir une adresse et un écouteur adaptés, et le réseau doit autoriser le trafic. Une navigation IPv6 réussie confirme un trajet sortant. Elle ne prouve pas qu'un client Internet peut atteindre votre serveur.

| Élément | Ce qu'il établit |
|---|---|
| **Adresse IPv6 du serveur** | Une adresse est attribuée à une interface |
| **Requête IPv6 sortante réussie** | Ce client a atteint un service externe |
| **Réponse d'une application distante** | La route entrante testée fonctionne |

**Règle de décision :** choisissez l'hébergement IPv6 uniquement après avoir confirmé toute la route entrante et la compatibilité de vos clients. Ne prenez pas l'attribution d'adresse pour un test applicatif à distance.

## Vérifier l'application avant de modifier le réseau

Suivez ces **étapes de diagnostic** pour distinguer les pannes locales des limites d'accès distant :

1. **Connexion locale :** vérifiez qu'un autre appareil domestique atteint l'adresse locale et le port prévu du serveur.
2. **Configuration du service :** confirmez que l'application écoute sur l'interface prévue et que le pare-feu de l'hôte autorise le client choisi.
3. **Public visé :** décidez si l'accès doit être privé ou public.
4. **Test distant :** testez le tunnel ou le réseau privé choisi depuis une autre connexion Internet.
5. **Performances :** mesurez la charge réelle une fois la connectivité établie.

**Un test local qui échoue** doit être examiné avant de choisir un service d'accès distant. Le transfert de ports ne corrigera pas une application qui écoute sur la mauvaise interface.

## Choisir une solution d'hébergement

**Scénario :** vous voulez consulter un tableau de bord domestique en déplacement et deux amis veulent rejoindre un serveur de jeu. Le tableau de bord utilise HTTP. Le jeu exige UDP et vos amis veulent utiliser des clients classiques sans installer un autre client réseau.

**Séparez les besoins.** Un tableau de bord dans le navigateur avec une petite liste d'identités convient à une publication web authentifiée. Le jeu a besoin d'une route publique compatible avec son transport et ses clients. Résoudre le premier besoin ne prouve pas que le second est pris en charge.

| Besoin | Choix justifié |
|---|---|
| **Tableau de bord privé dans le navigateur** | Évaluer Tunnel avec Access |
| **Accès personnel avec des appareils inscrits** | Évaluer un réseau overlay privé |
| **Clients de jeu UDP publics** | Évaluer un hébergement avec une accessibilité UDP documentée |

**Question de contrôle :** le DNS dynamique rend-il le jeu accessible par une route entrante indisponible ? Non. La mise à jour du nom d'hôte ne crée ni le mappage requis ni l'écouteur. Écartez les propositions qui ne changent que le nom sans expliquer la route.

**Notez le compromis :** déplacer le jeu vers un hébergement externe entraîne des coûts récurrents et de l'administration. Demander aux amis de rejoindre un réseau privé change leurs exigences de configuration. Choisissez après avoir déterminé quelle contrainte peut être assouplie.

## Préparer un plan de connexion

Créez un **plan pour un seul service** avec les champs suivants :

```text
Application et ports TCP/UDP requis :
Personnes ou appareils nécessitant un accès :
Installation d'un client acceptable :
Résultat du test du service local :
Route entrante disponible :
Méthode d'accès choisie :
Méthode d'authentification :
Test distant et critère de réussite :
Solution de repli en cas d'échec :
```

**Critère d'achèvement :** chaque étape du client distant à l'application a un responsable et un mécanisme pris en charge. Pour un tunnel domestique, indiquez le connecteur. Pour un hébergement externe, incluez le pare-feu de l'hôte et l'écouteur public. Laissez les hypothèses non vérifiées visibles jusqu'à leur confirmation.

## Étapes suivantes

Pour un tableau de bord dans le navigateur, commencez par le [guide de configuration de Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) et ajoutez Access. Pour une présentation générale du service, lisez l'[aperçu de T-Mobile Home Internet](/other/t-mobile-home-internet-benefits-connectivity-features/).
