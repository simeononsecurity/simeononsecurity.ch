---
title: "Cloudflare Tunnel et Access : avez-vous besoin des deux ?"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Comprenez la différence entre Cloudflare Tunnel et Access, choisissez une protection pour un tableau de bord domestique et évitez de publier une application privée sans authentification."
genre: ["Sécurité réseau", "Auto-hébergement", "Sécurité cloud"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel et Access", "Cloudflare Zero Trust", "cloudflared", "applications auto-hébergées", "sécurité homelab", "accès à distance", "fournisseur d'identité", "politiques d'accès", "authentification d'application", "nom d'hôte public", "protection de l'origine", "tunnel sortant", "jetons de service", "Service Auth", "MFA", "tableau de bord privé", "proxy inverse", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Un serveur domestique se connecte à une passerelle cloud par un passage transparent doté d'un point de vérification d'identité distinct."
coverCaption: ""
---

**Cloudflare Tunnel** connecte votre application à Cloudflare. **Cloudflare Access** contrôle qui peut y accéder. Pour un tableau de bord domestique privé exposé sur un nom d'hôte public, utilisez les deux. Un tunnel fonctionnel n'ajoute pas à lui seul de contrôle d'identité. Le [guide de publication d'applications de Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) explique cette distinction.

## À retenir

- **Expliquez le trajet :** distinguez le connecteur, l'origine et le contrôle d'identité.
- **Configurez une règle :** autorisez des personnes nommées à accéder à un tableau de bord privé.
- **Évaluez la protection :** testez les chemins d'accès autorisés, refusés et alternatifs.
- **Concevez l'accès :** documentez séparément les exigences des visiteurs et de l'automatisation.

## Avant de commencer

**Public :** propriétaires de serveurs domestiques qui veulent protéger un tableau de bord accessible par navigateur. L'exemple suppose un domaine actif sur Cloudflare, une application Web locale fonctionnelle et l'autorisation d'administrer les deux. **Effort estimé :** 20 à 30 minutes pour l'exercice sur les règles après la configuration du connecteur. **Difficulté :** débutant à intermédiaire.

**Parcours de lecture :** commencez par le rôle de chaque produit, suivez une requête, puis configurez et examinez une règle simple. Terminez en rédigeant une spécification d'accès pour votre service.

## Rôle de chaque produit

L'**origine** est le serveur qui exécute votre application. Le connecteur **`cloudflared`** établit des connexions depuis votre infrastructure vers Cloudflare. L'origine n'a donc pas besoin d'une adresse IP joignable publiquement. Les requêtes et les réponses circulent ensuite sur la connexion établie. [Présentation de Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Critère | Tunnel | Access |
|---|---|---|
| **Comment Cloudflare atteint-il mon serveur ?** | Établit la connexion | Ne remplace pas la connectivité avec l'origine |
| **Qui obtient l'accès ?** | Ne fournit pas seul une connexion utilisateur | Évalue les règles d'accès configurées |
| **Que dois-je configurer ?** | Connecteur et route d'application | Application, fournisseur d'identité et règles |
| **Que prouve la réussite ?** | L'origine est accessible par la route | Une requête respecte la règle configurée |

Un **fournisseur d'identité (IdP)** authentifie le visiteur. Une **règle Access** définit une action et des critères de correspondance. Allow autorise les utilisateurs correspondants. Bypass désactive l'application d'Access pour le trafic correspondant. [Référence des règles Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Suivez une requête du navigateur

Pour **`dashboard.example.com`**, le trajet logique d'une requête est le suivant :

```text
Navigateur -> Cloudflare Access -> connexion du tunnel -> cloudflared -> tableau de bord
                      |
                      +-> fournisseur d’identité lorsque l’authentification est nécessaire
```

Le **connecteur initie la connexion sortante du tunnel** depuis votre réseau. Les requêtes du navigateur empruntent ensuite cette connexion établie jusqu'à l'origine. Une connexion sortante qui transporte des requêtes entrantes de l'application explique principalement pourquoi Tunnel fonctionne sans redirection de port classique vers l'origine. [Modèle de connexion Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Les autorisations de l'application** constituent une décision distincte. L'accès au tableau de bord ne détermine pas automatiquement qui peut modifier ses paramètres ou supprimer ses données. Si l'application distingue les rôles de lecteur et d'administrateur, configurez-les et testez-les séparément.

Par exemple, **un membre de la famille en lecture seule** doit pouvoir consulter l'état des sauvegardes, tandis que vous devez pouvoir changer leur destination. Notez ces besoins avant de choisir les identités. Deux personnes qui passent le même contrôle Access ne devraient pas automatiquement recevoir les mêmes privilèges dans l'application.

## Quand utiliser les deux

**Le public détermine la protection.** Comparez ces configurations avant de publier une route :

| Public visé | Configuration suggérée | À vérifier avant usage |
|---|---|---|
| **Toute personne consultant un site public** | Tunnel si nécessaire pour joindre l'origine | L'exposition publique est intentionnelle |
| **Vous et quelques proches** | Tunnel et Access | N'autorisez que les identités prévues |
| **Une origine déjà publique** | Access avec une protection distincte de l'origine | Un accès direct à l'origine ne doit pas contourner le contrôle |
| **Un script planifié** | Tunnel et règle Service Auth | Le client prend en charge la méthode d'authentification |

**Access sans Tunnel** fonctionne avec une origine déjà accessible. Protégez également les autres routes vers le serveur. Cloudflare recommande de créer d'abord l'application Access lors de la publication d'une nouvelle route Tunnel. [Exigences relatives aux applications auto-hébergées](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*Pour un tableau de bord domestique privé accessible sur un nom d'hôte public, commencez par Tunnel et Access.*

## Configurez une règle de tableau de bord

Utilisez cette **configuration guidée** pour deux visiteurs prévus. Remplacez les deux adresses d'exemple par des identités que vous contrôlez. Créez l'application Access avant d'ajouter la route publique du tunnel.

1. **Application :** ouvrez Zero Trust → Access controls → Applications et créez une application auto-hébergée avec un nom d'hôte public.
2. **Nom d'hôte :** saisissez le nom dédié au tableau de bord. Pour cet exemple couvrant tout le nom d'hôte, ne limitez pas le chemin.
3. **Règle :** créez une règle Allow nommée `Dashboard viewers`.
4. **Sélecteur d'identité :** ajoutez une règle Include avec Emails. Remplacez `alice@example.com` et `bob@example.com` par les deux adresses prévues.
5. **Connexion :** choisissez le fournisseur d'identité utilisé par ces visiteurs et définissez volontairement la durée de session.
6. **Route :** enregistrez l'application, puis reliez le nom d'hôte au tableau de bord par le tunnel.

Le [flux officiel de configuration d'application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) décrit ces paramètres. **Résultat attendu :** tout nouveau visiteur doit s'authentifier avant d'atteindre l'application. Effectuez le test avec une identité refusée ci-dessous avant de vous fier à la règle.

## Comprenez la logique des règles

**Include** combine les alternatives avec OR. **Require** ajoute des conditions obligatoires avec AND. **Exclude** écarte les utilisateurs correspondants. Ajouter une condition Include supplémentaire élargit le groupe autorisé. [Sémantique des règles Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Fragment de règle | Effet logique |
|---|---|
| **Include Alice or Bob** | L'une des deux identités nommées suffit |
| **Include Alice, Include a country** | Les personnes correspondant au pays sont aussi autorisées |
| **Include Alice, Require a country** | Alice doit également respecter la condition du pays |

**Exercice de révision :** votre exigence ne nomme qu'Alice et Bob, mais un collègue ajoute un pays comme condition Include supplémentaire. Refusez cette modification, car elle autorise une population supplémentaire. La géographie ne prouve pas qu'une personne appartient à votre foyer.

## Authentifiez les scripts planifiés

Un **jeton de service** comprend un Client ID et un Client Secret pour les requêtes automatisées. Configurez la règle de l'application pour accepter ce jeton avec **Service Auth**. Créer un jeton sans la règle correspondante n'accorde pas l'accès à l'application. [Jetons de service Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Pour un script de sauvegarde ou un contrôle de surveillance, conservez le **secret** dans le stockage sécurisé des identifiants de l'outil. Donnez à chaque intégration un nom de jeton distinct et une date d'expiration réfléchie. Renouvelez ou révoquez le jeton lorsque vous retirez l'intégration. La documentation des jetons de service décrit ces opérations de cycle de vie.

**Vérifiez explicitement la compatibilité du client.** Un outil qui attend une réponse d'API ne sait pas forcément gérer une connexion interactive dans un navigateur. Avant de choisir la règle, confirmez qu'il prend en charge les en-têtes de requête ou une autre méthode d'authentification prévue.

## Testez les décisions d'accès

Utilisez ces **contrôles d'acceptation** pour votre déploiement :

| Contrôle | Preuve à noter |
|---|---|
| **Visiteur déconnecté** | Access intercepte une requête issue d'une nouvelle session du navigateur |
| **Identité autorisée** | L'application prévue se charge après la connexion |
| **Identité refusée** | Un compte non répertorié n'accède pas à l'application |
| **Route alternative** | Les anciens noms DNS et ports de l'origine ne donnent aucun accès imprévu |
| **Automatisation** | Le client approuvé fonctionne, et une requête sans identifiant échoue |

**Un écran de connexion visible** prouve uniquement qu'une route a rencontré l'authentification. Testez aussi le refus et les routes alternatives. Ce sont des contrôles suggérés, pas des résultats issus d'un exemple déployé.

## Vérifiez la frontière de l'origine

Une **origine qui fait confiance à l'identité Access** doit valider le jeton d'application signé. Cloudflare le transmet dans l'en-tête **`Cf-Access-Jwt-Assertion`**. La présence de cet en-tête ne prouve pas à elle seule son authenticité. [Validation JWT de Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

Un **JSON Web Token (JWT)** contient des affirmations signées. Pour intégrer l'identité Access à une origine, utilisez la méthode de validation documentée, avec l'émetteur attendu et l'audience de l'application. Décoder un jeton et lire son champ d'adresse e-mail ne suffit pas à le valider.

**Issuer** désigne l'autorité qui émet le jeton. **Audience** désigne l'application visée. Vérifiez la validité et l'expiration avec une bibliothèque de validation prise en charge au lieu de coder vous-même la vérification des signatures.

**Définissez clairement la frontière :** indiquez où la validation a lieu et quelles routes atteignent l'application. Un ancien transfert de port ou un nom d'hôte secondaire mérite une vérification distincte, même après la réussite de tous les tests du nom d'hôte principal.

## Corrigez les écarts de règles

| Observation | Vérification suivante |
|---|---|
| **Un visiteur inattendu passe** | Examinez les conditions Include, les règles Bypass et la couverture des noms d'hôte |
| **Un visiteur prévu est refusé** | Comparez l'identité connectée avec les valeurs exactes du sélecteur |
| **Un script reçoit une page de connexion** | Vérifiez son identifiant et la règle Service Auth |
| **Un lecteur autorisé modifie les paramètres** | Examinez les rôles définis dans l'application elle-même |

**Le comportement des sessions** compte aussi lors des nouveaux tests. Access propose plusieurs durées, notamment des sessions d'application et globales. Notez le paramètre et utilisez une nouvelle session pour vérifier une autre identité. [Gestion des sessions Access](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Rédigez votre spécification d'accès

Préparez une **courte spécification** avant d'ajouter un autre service :

```text
Service et nom d'hôte :
Identités humaines autorisées :
Rôles requis dans l'application :
Identifiant d'automatisation et expiration :
Autres routes vers l'origine :
Emplacement de validation des jetons Access :
Résultat du test avec identité autorisée :
Résultat du test avec identité refusée :
```

**Critère d'achèvement :** un autre administrateur doit comprendre qui obtient l'accès, comment chaque client s'authentifie et quelle preuve établit le refus. Si vous ajoutez ensuite une intégration de surveillance, mettez à jour son identifiant et répétez le contrôle avec une requête non authentifiée.

## Étapes suivantes

Suivez le [guide de configuration de Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) pour configurer le connecteur, puis appliquez le [flux officiel de l'application Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). Pour une connexion cellulaire, consultez les [limites de redirection de ports de T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/) avant de choisir votre accès à distance.
