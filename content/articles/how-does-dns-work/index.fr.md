---
title: "Comment fonctionne le DNS : DNS racine, importance et dépannage"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Découvrez le fonctionnement du DNS et du DNS racine, leur hiérarchie, la résolution des noms, la mise en cache et le dépannage."
genre: ["Notions de base du DNS", "DNS racine", "Système de noms de domaine", "Résolution DNS", "Hiérarchie DNS", "Cache DNS", "Dépannage DNS", "Enregistrements DNS", "Gestion DNS", "Commandes DNS"]
tags: ["DNS", "DNS racine", "Système de noms de domaine", "Résolution DNS", "Hiérarchie DNS", "Cache DNS", "Enregistrements DNS", "Gestion DNS", "Dépannage DNS", "réseaux", "infrastructure Internet", "adresses IP", "accès aux sites", "requête récursive", "serveurs de noms faisant autorité", "TTL", "mécanismes de cache", "vider le cache DNS", "serveurs DNS racine", "routage anycast", "ICANN", "coopération DNS", "enregistrement A", "enregistrement AAAA", "enregistrement CNAME", "enregistrement MX", "enregistrement TXT", "enregistrement SRV", "enregistrement NS", "enregistrement PTR", "enregistrement SOA", "commandes de dépannage DNS", "Windows", "macOS", "Linux", "Invite de commandes", "terminal système"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Image de réseaux informatiques interconnectés avec des noms de domaine et des adresses IP, illustrant le fonctionnement du DNS et du DNS racine."
coverCaption: "Découvrez le DNS et maîtrisez le système de noms de domaine"
---

## Fonctionnement du DNS et du DNS racine

### Introduction

Le Domain Name System (DNS) est un élément essentiel de l’infrastructure Internet. Il permet d’accéder aux sites avec des noms de domaine plutôt qu’avec des adresses IP. Comme un annuaire, il convertit les noms lisibles par les personnes en adresses IP comprises par les ordinateurs. Le DNS racine est au cœur de ce système hiérarchique et distribué. Cet article présente le fonctionnement du DNS, du DNS racine et des enregistrements associés aux domaines.

{{< youtube id="mpQZVYPuDGU" >}}

## Le Domain Name System (DNS)

Le **Domain Name System (DNS)** est un système de nommage décentralisé qui associe des noms de domaine à des adresses IP. Il permet d’accéder aux sites et à d’autres ressources Internet en saisissant un nom dans le navigateur. Le DNS évite de mémoriser des adresses IP complexes.

### Hiérarchie DNS

Le DNS suit une structure hiérarchique à plusieurs niveaux. La zone racine se trouve au sommet, puis viennent les domaines de premier niveau (TLD), les domaines de deuxième niveau et les sous-domaines. Chaque niveau compose le nom complet. Dans `www.example.com`, « www » est le sous-domaine, « example » le domaine de deuxième niveau et « com » le TLD.

### Processus de résolution DNS

Quand vous saisissez un nom de domaine dans votre navigateur, la résolution DNS commence. Le navigateur envoie une requête à un résolveur DNS, généralement fourni par votre fournisseur d’accès à Internet (FAI). Le résolveur suit plusieurs étapes pour trouver l’adresse IP associée au nom.

1. **Cache DNS local** : le résolveur cherche d’abord le nom de domaine et l’adresse IP dans son cache local. S’il trouve les données, il renvoie directement le résultat.

2. **Requête récursive** : si le cache ne contient pas les données, le résolveur lance une requête récursive. Il contacte d’abord les serveurs DNS racine, responsables de la zone « . » (point). Ceux-ci renvoient les adresses IP des serveurs TLD correspondant au domaine demandé.

3. **Requête TLD** : le résolveur contacte les serveurs TLD identifiés à l’étape précédente et demande les adresses IP des serveurs de noms faisant autorité pour le domaine.

4. **Requête au serveur faisant autorité** : le résolveur interroge les serveurs faisant autorité reçus des serveurs TLD. Ces serveurs détiennent les enregistrements faisant autorité et répondent avec l’adresse IP associée au nom.

5. **Réponse au client** : le résolveur reçoit l’adresse IP des serveurs faisant autorité et la transmet au navigateur. Le navigateur peut alors se connecter au serveur Web avec cette adresse.

### Mise en cache DNS

Les résolveurs DNS utilisent un cache pour accélérer les réponses et réduire la charge des serveurs DNS. Après une réponse, le résolveur stocke localement l’association entre le nom de domaine et l’adresse IP. Les requêtes suivantes pour le même nom peuvent être résolues directement depuis ce cache.

La mise en cache se produit à plusieurs niveaux : résolveur local, résolveur du FAI, routeurs et systèmes d’exploitation. La valeur Time-to-Live (TTL) de la réponse DNS indique combien de temps l’enregistrement reste dans le cache. À l’expiration du TTL, le résolveur supprime l’enregistrement et effectue une nouvelle requête.

#### Vider votre cache DNS local

Vider le cache DNS aide à résoudre certains problèmes et permet au système de récupérer les enregistrements récents. Voici les étapes pour différents systèmes d’exploitation :

##### Windows

Pour vider le cache DNS sous Windows :

1. Appuyez sur `Win + R`, saisissez `cmd`, puis appuyez sur Entrée pour ouvrir l’Invite de commandes.

2. Saisissez la commande suivante, puis appuyez sur Entrée :

```bash
ipconfig /flushdns
```

Cette commande vide le cache du résolveur DNS de Windows.

##### macOS

Pour vider le cache DNS sous macOS :

1. Ouvrez Terminal dans Applications > Utilitaires ou recherchez-le avec Spotlight.

2. Saisissez la commande suivante dans Terminal, puis appuyez sur Entrée :

```bash
sudo killall -HUP mDNSResponder
```

Cette commande redémarre le processus mDNSResponder, responsable de la résolution DNS sous macOS.

##### Linux

La méthode varie selon la distribution et le résolveur DNS utilisé. Voici deux méthodes courantes :

1. **Systèmes utilisant systemd (par exemple Ubuntu et Fedora)** :

Ouvrez Terminal et exécutez la commande suivante avec les privilèges administrateur :

```bash
sudo systemd-resolve --flush-caches

```

Cette commande vide le cache DNS des systèmes qui utilisent systemd-resolved comme résolveur.

2. **Systèmes sans systemd** :

Ouvrez Terminal et exécutez la commande suivante avec les privilèges administrateur :

```bash
sudo /etc/init.d/nscd restart

```

Cette commande redémarre Name Service Cache Daemon (nscd), qui gère le cache DNS sur les distributions Linux sans systemd.

Ces étapes sont générales. Les commandes et méthodes peuvent varier légèrement selon la version du système. Vider le cache DNS aide pour certains problèmes, mais ne résout pas tous les problèmes de connectivité réseau.

## Fonctionnement du système DNS racine

Le système DNS racine est un élément fondamental de l’infrastructure DNS. Voici son fonctionnement :

### 1. Zone racine et serveurs racine

Le système DNS racine commence par la **zone racine**, le niveau supérieur de la hiérarchie DNS. Elle contient des informations sur les serveurs de noms faisant autorité pour tous les domaines de premier niveau (TLD), comme .com, .org, .net et les TLD nationaux comme .us et .uk.

Le système comprend 13 serveurs DNS racine, désignés par les lettres A à M. Ils sont répartis dans le monde pour assurer la redondance et la fiabilité.

### 2. Routage anycast

Pour gérer le volume élevé de trafic DNS, les serveurs racine utilisent le **routage anycast**. Plusieurs serveurs partagent la même adresse IP tout en étant répartis géographiquement. Les conditions du réseau orientent chaque requête vers un serveur approprié et répartissent la charge.

Lorsqu’un utilisateur lance une requête DNS, anycast l’achemine vers un serveur racine disponible à proximité. L’infrastructure réseau choisit le chemin le plus court selon les conditions du réseau. Anycast répartit efficacement la charge et limite les goulots d’étranglement.

### 3. Résolveurs DNS récursifs

Quand un résolveur DNS reçoit une requête pour un nom de domaine, il commence une résolution récursive en contactant l’un des serveurs racine.

Le serveur racine renvoie une référence vers les adresses IP des serveurs de noms TLD responsables du TLD demandé. Ces serveurs TLD possèdent des informations sur les serveurs faisant autorité des domaines de leur TLD.

### 4. Références et serveurs de noms faisant autorité

Après la référence du serveur racine, le résolveur contacte le serveur de noms TLD approprié.

Le serveur TLD renvoie une autre référence avec les adresses IP des serveurs faisant autorité pour le domaine demandé.

Le résolveur demande ensuite à ces serveurs l’adresse IP associée au nom de domaine.

### 5. Cache et TTL

Pendant la résolution DNS, le cache améliore les performances et réduit la charge des serveurs. Les résolveurs stockent les associations entre noms de domaine et adresses IP.

Les enregistrements DNS sont mis en cache pendant la durée définie par le Time-to-Live (TTL). Le TTL indique combien de temps un enregistrement reste valide. À son expiration, le résolveur le supprime et effectue une nouvelle requête pour obtenir l’adresse IP à jour.

### 6. Collaboration et gestion

Le système DNS racine est géré grâce à la collaboration entre l’Internet Corporation for Assigned Names and Numbers (ICANN) et les opérateurs des serveurs racine.

ICANN supervise la gestion générale et la coordination du DNS avec les opérateurs des serveurs racine. Ils entretiennent ensemble le fichier de la zone racine, qui contient les informations sur les 13 serveurs DNS racine et leurs adresses IP.

Les opérateurs des serveurs racine assurent le fonctionnement et la disponibilité des serveurs racine. Ils contribuent ainsi à la stabilité et à la résilience de l’infrastructure DNS.

Le système DNS racine est le point de départ de la résolution DNS. Il associe les noms de domaine à des adresses IP afin de permettre un accès efficace aux sites et aux ressources Internet.

#### Les 13 serveurs DNS racine

Les 13 serveurs DNS racine sont identifiés par les lettres A à M. Chaque serveur est hébergé dans plusieurs sites physiques pour assurer la redondance et la tolérance aux pannes. Ils traitent les requêtes concernant la zone racine, notamment les TLD .com, .org, .net et les TLD nationaux .us et .uk.

#### ICANN et la gestion du DNS racine

L’Internet Corporation for Assigned Names and Numbers (**ICANN**) gère et coordonne le DNS ainsi que l’attribution des adresses IP. Elle travaille avec les opérateurs des serveurs racine pour assurer la stabilité et la sécurité du DNS racine. Ensemble, ils entretiennent le fichier de la zone racine avec les informations sur les 13 serveurs racine et leurs adresses IP.

______

## Types d’enregistrements DNS et leur rôle

{{< youtube id="HnUDtycXSNE" >}}

Les enregistrements DNS sont des composants essentiels du Domain Name System (DNS). Ils fournissent différents types d’informations associés à un nom de domaine. Voici quelques types courants et leur rôle :

| Type d’enregistrement | Description | Exemple |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Associe un nom de domaine à une adresse IPv4. | `example.com     IN A 192.0.2.1` |
| AAAA | Associe un nom de domaine à une adresse IPv6. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Associe un alias (nom canonique) au nom de domaine réel. | `www.example.com IN CNAME example.com` |
| MX | Indique les serveurs de messagerie qui reçoivent les e-mails du domaine. | `example.com     IN MX 10 mail.example.com` |
| TXT | Stocke du texte arbitraire, souvent pour SPF, DKIM ou la vérification du domaine. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Indique les serveurs de noms faisant autorité pour le domaine. | `example.com     IN NS ns1.example.com` |
| SOA | Définit les propriétés générales de la zone (enregistrement start of authority). | `example.com     IN SOA ns1.example.com` |
| SRV | Définit l’emplacement d’un service spécifique du domaine. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Associe une adresse IP à un nom de domaine (recherche DNS inversée). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. Enregistrement A (enregistrement d’adresse)

L’**enregistrement A** associe un nom de domaine à une adresse IPv4. C’est le type d’enregistrement DNS le plus simple et le plus courant. Il aide le navigateur à trouver l’adresse IP du serveur Web qui héberge le site.

### 2. Enregistrement AAAA (enregistrement d’adresse IPv6)

L’**enregistrement AAAA** remplit le même rôle que l’enregistrement A, mais associe le domaine à une adresse IPv6. Avec la transition vers IPv6, il devient important pour la connectivité sur les réseaux IPv6.

### 3. Enregistrement CNAME (enregistrement de nom canonique)

L’**enregistrement CNAME** crée un alias ou un nom canonique pour un domaine. Il sert à faire pointer un domaine ou sous-domaine vers un autre. Par exemple, un CNAME peut faire pointer "www" vers "mywebsite.com".

### 4. Enregistrement MX (enregistrement d’échange de courrier)

L’**enregistrement MX** indique le serveur qui reçoit les messages pour un domaine. Plusieurs enregistrements MX peuvent avoir une priorité qui définit leur ordre d’utilisation si le serveur principal est indisponible.

### 5. Enregistrement TXT (enregistrement texte)

L’**enregistrement TXT** stocke des informations textuelles associées au domaine. Il sert notamment à la vérification de domaine, aux enregistrements SPF (Sender Policy Framework) pour l’authentification des e-mails et aux notes générales.

### 6. Enregistrement SRV (enregistrement de service)

L’**enregistrement SRV** définit l’emplacement d’un service ou d’une ressource du domaine. Il est utilisé pour la VoIP, la messagerie instantanée et les applications qui doivent localiser des services ou serveurs spécifiques.

### 7. Enregistrement NS (enregistrement de serveur de noms)

L’**enregistrement NS** indique les serveurs de noms faisant autorité pour un domaine. Ces serveurs détiennent ses enregistrements DNS. Le résolveur les consulte pour trouver les serveurs faisant autorité.

### 8. Enregistrement PTR (enregistrement pointeur)

L’**enregistrement PTR** associe une adresse IP à un nom de domaine lors d’une recherche DNS inversée. Il sert souvent à vérifier l’identité d’un serveur de messagerie et à limiter le spam. La recherche inversée aide à valider l’authenticité d’un serveur de messagerie.

### 9. Enregistrement SOA (enregistrement de début d’autorité)

L’**enregistrement SOA** contient des informations administratives sur un domaine, comme le serveur de noms faisant autorité principal, l’adresse e-mail du responsable et divers paramètres temporels des enregistrements DNS.

Ce ne sont que quelques exemples parmi les nombreux types d’enregistrements DNS. Chacun a un rôle précis et contribue à résoudre correctement les noms de domaine vers leurs ressources.

______

## Commandes de dépannage DNS selon le système d’exploitation

En cas de problème DNS, les commandes de diagnostic aident à en trouver la cause. Voici des commandes courantes selon le système d’exploitation :

### Windows

#### 1. `ipconfig /flushdns`

Cette commande vide le cache DNS de Windows et peut corriger les problèmes liés à des enregistrements obsolètes ou incorrects. Ouvrez l’Invite de commandes et exécutez-la.

#### 2. `ipconfig /all`

`ipconfig /all` affiche les détails des interfaces réseau Windows, y compris les serveurs DNS configurés. Cette commande permet de vérifier que les bons serveurs DNS sont utilisés.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Cette commande redémarre mDNSResponder sous macOS, le processus responsable de la résolution DNS. Elle peut actualiser les paramètres DNS et aider à résoudre certains problèmes. Ouvrez Terminal et exécutez-la avec les privilèges administrateur.

#### 2. `nslookup`

`nslookup` permet d’interroger les enregistrements DNS, de tester la résolution et de vérifier la connectivité aux serveurs DNS. Dans Terminal, exécutez `nslookup` suivi du nom de domaine ou de l’adresse IP à examiner.

### Linux

#### 1. `systemd-resolve --flush-caches`

Sur les systèmes Linux qui utilisent systemd comme résolveur DNS, `systemd-resolve --flush-caches` vide le cache DNS. Cela peut corriger les problèmes causés par des entrées obsolètes. Ouvrez Terminal et exécutez la commande avec les privilèges administrateur.

#### 2. `dig`

`dig` est un outil polyvalent de diagnostic DNS sous Linux. Il fournit des détails sur les requêtes, les réponses et la configuration des serveurs DNS. Utilisez `dig` pour interroger des enregistrements, tester la résolution et diagnostiquer les problèmes DNS. Dans Terminal, exécutez `dig` suivi du nom de domaine ou de l’adresse IP à examiner.

Ces commandes aident à diagnostiquer et résoudre les problèmes DNS. Elles renseignent sur la configuration DNS, les serveurs utilisés et les problèmes de connectivité.

Les commandes et leurs options peuvent varier selon la version du système et la distribution. Consultez la documentation de votre version pour connaître leur usage détaillé.
______


## Conclusion

Le Domain Name System (DNS) et le DNS racine jouent un rôle essentiel dans le fonctionnement d’Internet. Le DNS donne accès aux sites via des noms de domaine faciles à lire, et le DNS racine constitue la base de toute la hiérarchie. Comprendre leur fonctionnement aide à utiliser le Web et à mieux connaître l’infrastructure des services en ligne.

______

## Références

- [DNS sur Wikipédia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Comment fonctionne le DNS, par Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Site officiel d’ICANN](https://www.icann.org/)
- [opérateurs des serveurs racine](https://www.root-servers.org/)
