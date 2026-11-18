---
title: "En 2026, les conteneurs ne sont plus une frontière de sécurité"
date: 2026-09-28
lastmod: 2026-11-13
toc: true
draft: false
description: "Les vulnérabilités du noyau de 2026 montrent pourquoi l’isolation des conteneurs multi-locataires ne suffit pas. Découvrez Copy Fail, Dirty Frag, Fragnesia et CVE-2026-80521, et comparez les conteneurs renforcés aux microVM."
genre: ["Sécurité des conteneurs", "Linux", "Sécurité du noyau", "Virtualisation", "Sécurité du cloud", "Recherche sur les menaces", "Équipe bleue", "DevSecOps"]
tags: ["Évasion de conteneur", "Frontière de sécurité des conteneurs", "CVE du noyau Linux", "Élévation locale de privilèges", "LPE 2026", "Copy Fail", "CVE-2026-31431", "Dirty Frag", "CVE-2026-43284", "CVE-2026-43500", "Fragnesia", "CVE-2026-46300", "CVE-2026-80521", "kernelCTF", "kvmCTF", "microVM", "Firecracker", "Kata Containers", "Corruption du cache de pages", "AF_ALG", "AF_UNIX", "XFRM ESP", "RxRPC", "Isolation des espaces de noms", "Appel système clone", "Découverte de vulnérabilités par IA", "Sécurité Docker", "Sécurité Kubernetes", "Isolation multi-locataire", "Évasion de sandbox", "nsjail", "Bubblewrap", "Firejail", "Dirty Pipe", "Tendance des CVE du noyau"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "Illustration numérique de plusieurs conteneurs lumineux reliés à un symbole central de noyau. Des éléments colorés représentent des vulnérabilités qui rayonnent depuis le noyau sur un fond sombre."
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---
**Les conteneurs partagent un même noyau. En 2026, quatre familles de vulnérabilités distinctes ont prouvé qu’un seul bogue du noyau suffit pour sortir d’un conteneur et atteindre l’hôte.** Copy Fail, Dirty Frag, Fragnesia et CVE-2026-80521 accordent chacune les droits root à un utilisateur local sans privilèges. Toutes franchissent la frontière du conteneur.

*Le plus inquiétant n’est pas les bogues eux-mêmes, mais le faible coût de leur découverte par l’IA et la façon dont un correctif en a créé un autre.*

Cet article explique comment les conteneurs isolent les charges de travail, pourquoi cet isolement repose désormais sur des fondations qui se réduisent, ce que fait chacune des vulnérabilités de 2026 et quelle technologie d’isolation mérite la confiance à la place.

**À retenir :** identifiez qui fournit le code de chaque charge de travail, déterminez les fonctions du noyau dont elle a besoin et choisissez entre conteneurs renforcés et frontière de microVM. Considérez les études de cas de 2026 comme des éléments de recherche datés. Vérifiez les avis actuels des fournisseurs avant de modifier un noyau de production.

## Réponse courte

| Question | Réponse courte |
|---|---|
| **Les conteneurs isolent-ils ?** | Oui, au niveau des processus et du système de fichiers. Tous partagent un noyau, donc les bogues du noyau représentent un risque commun |
| **Pourquoi maintenant ?** | La recherche de bogues assistée par IA a réduit le coût de découverte des failles du noyau. Près de **6 000 CVE du noyau** avaient été publiées en septembre 2026 |
| **Qu’est-ce qui brise la frontière ?** | Toute élévation locale de privilèges dans le noyau. Une mauvaise configuration du conteneur n’est pas nécessaire pour s’en échapper |
| **Les correctifs suffisent-ils ?** | Ils sont nécessaires, mais leur cadence ne suit plus. Un correctif de 2026 **a introduit une nouvelle faille exploitable** |
| **Qu’est-ce qui fonctionne mieux ?** | Les microVM comme Firecracker ou Kata Containers, qui fournissent leur propre noyau à chaque charge de travail |
| **L’alternative est-elle parfaite ?** | Non. L’hyperviseur est aussi du code. Sa surface d’attaque est beaucoup plus réduite, et c’est là la différence essentielle |

## Comment les conteneurs isolent

Pour comprendre la frontière, il faut d’abord comprendre ce qu’un conteneur n’est pas.

**Un conteneur n’est pas une machine virtuelle.** Il n’y a ni second noyau, ni matériel émulé, ni hyperviseur entre votre processus et le matériel. Lancer une image de conteneur revient à exécuter un processus sur le noyau existant, avec une vision modifiée du système.

Le mécanisme repose sur **l’appel système `clone`**. `fork` copie l’espace d’adressage d’un processus. `clone` crée un processus enfant et permet de contrôler précisément les parties du contexte d’exécution qui sont partagées ou remplacées. Docker transmet à `clone` un ensemble d’**espaces de noms** :

| Espace de noms | Ce qu’il simule |
|---|---|
| **Mount** | Une racine privée du système de fichiers, pour que le conteneur voie son propre arbre plutôt que le vôtre |
| **PID** | Sa propre numérotation des processus, de sorte que `PID 1` soit le premier processus du conteneur, et non `systemd` |
| **User** | Une correspondance d’identités où « root » dans le conteneur correspond à un utilisateur hôte sans privilèges |
| **Network** | Des interfaces, tables de routage et ports privés |
| **IPC** | Une mémoire partagée et des files de messages isolées |
| **UTS** | Son propre nom d’hôte et nom de domaine |
| **Cgroup** | Une vue privée des limites de ressources |

Ajoutez un système de fichiers **union** au-dessus d’une image et le résultat *semble* être un ordinateur séparé. `id` affiche `uid=0(root)` dans le conteneur. Le système de fichiers ressemble à une installation Ubuntu minimale. La liste des processus ne montre que les siens.

**Au niveau des appels système, ce n’est pas une frontière de sécurité.** Quand un processus du conteneur ouvre un fichier, alloue de la mémoire ou utilise un socket réseau, le même noyau traite la requête pour tous les conteneurs de l’hôte. Les espaces de noms changent *ce que voit le processus*, pas *ce que le noyau fera pour lui*.

*Le noyau est la véritable frontière entre le conteneur et l’hôte. Le reste n’est que présentation.*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="Schéma de trois conteneurs utilisant le même noyau. Les espaces de noms mount, PID, user et network séparent leurs vues, mais tous les appels système aboutissent au même noyau partagé" >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## La frontière est du code, et le code contient des bogues

Chaque action d’un conteneur passe par l’**interface des appels système**. Ouvrir un fichier, lire la mémoire, écrire dans un socket, modifier un UID : le noyau gère tout cela, car il ne veut pas que les processus accèdent directement au processeur, au système de fichiers ou au réseau.

Cette médiation constitue le modèle de sécurité et elle est implémentée en code. Plus précisément, elle compte environ **30 millions de lignes**.

Une élévation locale de privilèges (LPE) se produit lorsqu’un processus exploite une faille dans le code de médiation pour obtenir des privilèges qui ne lui ont jamais été accordés. **Les LPE ne sont pas nouvelles.** Elles existent depuis les premiers mécanismes de médiation du noyau. Le secteur a vécu avec leur flux régulier pendant des décennies.

**Dirty Pipe, en 2022**, est l’exemple de référence que la plupart connaissent. Elle exploitait une erreur de gestion des tampons pipe pour écraser des fichiers en lecture seule. Elle avait fait la une, car des bogues de cette gravité apparaissaient **environ tous les un ou deux ans**. On appliquait le correctif puis on continuait, en supposant qu’aucun défaut majeur ne dormait dans un code lu par un million de personnes.

*Cette hypothèse ne tient plus.*

## Ce qui a changé en 2026

Le changement ne concerne pas les compétences des attaquants. C’est **la recherche de bogues de corruption mémoire du noyau qui est devenue une tâche d’ingénierie plutôt qu’une carrière de recherche**.

Trois données de cette année illustrent le changement :

| Découverte | Auteur | Méthode |
|---|---|---|
| **Copy Fail** (CVE-2026-31431) | Taeyang Lee, Theori | Avec **Xint Code**, un outil d’analyse statique par IA. Environ **une heure de scan** du sous-système cryptographique de Linux |
| **CVE-2026-80521** | Zhenpeng (Leo) Lin, DepthFirst | Trouvée avec **dfs-large1**, un modèle d’IA interne entraîné à la détection de vulnérabilités |
| **CVE-2026-80521**, découverte indépendante | Kyle, **OpenAI** | Le même bogue, trouvé séparément et signalé le même jour |

Relisez la troisième ligne. Deux organisations utilisant des outils d’IA différents ont découvert **le même use-after-free dans AF_UNIX** et l’ont signalé à `security@kernel.org` le **même jour**. Ce n’est pas une coïncidence de talent. C’est un processus reproductible qui donne deux fois la même réponse.

DepthFirst indique directement l’ampleur : **près de 6 000 CVE du noyau avaient été publiées en septembre 2026**. Le nombre augmente avec la disponibilité de l’assistance par IA, pas avec le nombre de développeurs du noyau.

*Quand une heure d’analyse par IA découvre un bogue vieux de dix ans dans le sous-système cryptographique, l’économie de l’exploitation du noyau s’inverse.*

## Quatre évasions en un an

Chacune de ces vulnérabilités accorde root à un compte local sans privilèges. Aucune ne nécessite une mauvaise configuration du conteneur, un indicateur privilégié ou un accès initial par le réseau.

| Vulnérabilité | CVE | Sous-système | Primitive | Découverte par |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | Écriture de 4 octets dans le cache de pages de tout fichier lisible | Theori, avec l’aide de l’IA |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP, RxRPC | Écriture de 4 octets dans le cache de pages via deux variantes enchaînées | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP | Écritures d’un seul octet dans le cache de pages | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | Sockets AF_UNIX | Use-after-free dans le ramasse-miettes de `unix_vertex` | DepthFirst, avec l’aide de l’IA |

Les quatre partagent un schéma de conception à noter : **elles attaquent le cache de pages, et non le disque.**

### Copy Fail : une faille logique sans course

Copy Fail est la plus simple des quatre et la plus alarmante.

Presque toutes les LPE Linux nécessitent une fenêtre temporelle ou un décalage mémoire propre au noyau. **Copy Fail n’a besoin ni de l’un ni de l’autre.** Il s’agit d’une faille logique directe dans `algif_aead`, le module qui fournit à l’espace utilisateur un accès au chiffrement authentifié via AF_ALG.

La chaîne utilise `splice()` pour introduire une page du cache dans l’opération, puis détourne le chemin AEAD sur place pour écrire **quatre octets contrôlés** dans cette page. La page corrompue **n’est jamais marquée comme dirty**, donc elle n’est jamais réécrite sur le disque. Le fichier reste intact, ce qui permet aux contrôles de somme et d’intégrité de réussir tandis que sa copie en mémoire est modifiée.

Un **script Python de 732 octets** obtient root sur toutes les distributions Linux publiées depuis 2017. Le bogue a été introduit par une **optimisation de 2017** dans `algif_aead`, et le correctif de 2026 annule simplement cette optimisation. Commit mainline `a664bf3d603d`.

*Le bogue était présent dans toutes les grandes distributions depuis près d’une décennie. Un outil d’IA l’a trouvé en une heure environ.*

### Dirty Frag : deux variantes qui se complètent

Le nom Dirty Frag décrit bien son origine : **Dirty Pipe écrase `struct pipe_buffer`. Dirty Frag écrase le champ `frag` de `struct sk_buff`.**

Il s’agit de **deux vulnérabilités enchaînées**, et l’enchaînement est ingénieux :

- **CVE-2026-43284** profite du fait que `esp_input()` ignore le chemin copy-on-write avant de déchiffrer sur place un fragment inséré avec splice. Elle exige le privilège de créer un **user namespace**, que certaines distributions limitent.
- **CVE-2026-43500** exploite le déchiffrement sur place du fragment par `rxkad_verify_packet_1()`. Aucun privilège de namespace n’est requis, mais le module `rxrpc` est absent de la plupart des distributions. Ubuntu le charge par défaut.

**Chaque variante a son angle mort seule. Ensemble, elles se complètent.** Lorsque les user namespaces sont autorisés, le chemin ESP s’exécute d’abord. Lorsqu’ils sont bloqués mais que `rxrpc` est présent, le chemin RxRPC prend le relais. Un seul binaire d’exploitation fonctionne alors sur plusieurs distributions. La variante RxRPC obtient root en vidant un champ de `/etc/passwd` et en laissant PAM accepter un mot de passe vide avec `nullok`.

**La découverte essentielle pour les défenseurs :** Dirty Frag se déclenche **que `algif_aead` soit disponible ou non**. La mitigation Copy Fail largement diffusée, qui met le module sur liste noire, **ne protège absolument pas contre Dirty Frag**.

### Fragnesia : le correctif qui a créé un bogue

Fragnesia appartient à la même classe que Dirty Frag, mais cible le chemin **ESP-in-TCP** de XFRM. C’est le cas le plus instructif du groupe.

La vulnérabilité exploite la mauvaise gestion des fragments de page partagés lors de la coalescence de `skb`. L’attaquant insère des pages adossées à des fichiers dans la file de réception TCP avant que le socket passe en mode protocole de couche supérieure `espintcp`. Quand le traitement ESP s’active, le noyau déchiffre les données en attente **sur place**, et la manipulation du flot de clés AES-GCM corrompt le cache de pages sous-jacent. L’attaquant obtient des **écritures répétées d’un octet** dans les pages de fichiers en cache.

L’exploitation obtient root en écrasant les premiers octets de `/usr/bin/su` avec une petite charge utile ELF. **La modification reste uniquement en mémoire et ne touche pas au binaire sur disque.**

Les **user et network namespaces** non privilégiés donnent `CAP_NET_ADMIN` dans un espace isolé. NETLINK_XFRM installe ensuite une association de sécurité préparée.

*Prenez le temps de lire cette phrase :* Fragnesia est apparue comme **un effet secondaire involontaire d’un correctif des vulnérabilités Dirty Frag d’origine**. Le correctif de Dirty Frag a créé un nouveau bogue root exploitable indépendamment.

### CVE-2026-80521 : l’évasion de conteneur qui a gagné kernelCTF

La course AF_UNIX écarte tout argument selon lequel il s’agirait d’un scénario théorique.

La vulnérabilité est un **use-after-free sur le tas** dans le mécanisme de ramasse-miettes des messages `SCM_RIGHTS`, qui permettent aux processus de se transmettre des descripteurs de fichiers. Une course pendant le ramassage d’une référence circulaire de socket libère un `struct unix_vertex`, alors que l’anneau SCC d’un socket survivant conserve encore un pointeur vers celui-ci. Le ramassage suivant parcourt l’anneau périmé et déréférence la mémoire libérée.

Son importance dépasse Linux, car **AF_UNIX est au cœur de l’IPC local**. Les bases de données locales, `systemd` et Docker lui-même en dépendent. DepthFirst indique que la vulnérabilité affecte la plupart des sandbox système reposant sur le noyau, **dont `nsjail`, `Firejail` et `Bubblewrap`**, ainsi que les environnements d’exécution modernes de conteneurs.

DepthFirst a remporté une **place dans Google kernelCTF** avec cette vulnérabilité le **24 juillet 2026**, a reçu confirmation dans le créneau `lts-6.12.95` le **5 août**, l’a signalée à `security@kernel.org` le même jour, puis a appris que **Kyle d’OpenAI avait signalé le même bogue**. Le correctif upstream a été fusionné le **6 août**. La recherche a été publiée le **22 septembre**.

L’équipe a publié un exploit fonctionnel ciblant **Ubuntu 26.04**, ainsi qu’un second exploit pour CVE-2026-52910 permettant de s’évader d’**Ubuntu 24.04**.

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="Schéma montrant un processus sans privilèges dans un conteneur qui corrompt une page du cache pour modifier en mémoire un binaire setuid, obtenir root et franchir la frontière du conteneur jusqu’au noyau de l’hôte" >}}

## Pourquoi les conseils de mitigation continuent d’échouer

Les défenseurs ont reçu trois séries de solutions de contournement cette année, et chacune était partiellement erronée.

| Mitigation | Ce qu’elle arrête | Ce qu’elle rate |
|---|---|---|
| Mettre **`algif_aead`** sur liste noire | Copy Fail | **Rien dans Dirty Frag**, qui ignore complètement le module |
| Mettre **`esp4`, `esp6`, `rxrpc`** sur liste noire | Dirty Frag, Fragnesia | Les équipes qui ont besoin d’IPsec. Les tout nouveaux sous-systèmes restent aussi exposés |
| Restreindre les **user namespaces sans privilèges** | Les variantes ESP | La variante RxRPC n’a pas besoin de namespace. La politique AppArmor n’est qu’une mitigation **partielle** |
| **Corriger le noyau** | Le bogue corrigé | Le bogue suivant et tout bogue introduit par un correctif |

Deux tendances ressortent.

**D’abord, les solutions se contredisent.** Copy Fail est mitigée en désactivant `algif_aead`. Dirty Frag se déclenche **que le module existe ou non**. Fragnesia exige de désactiver `esp4` et `esp6`, ce qui pose problème à ceux qui utilisent IPsec. Aucune liste noire unique de modules ne couvre toute la famille.

**Ensuite, et c’est pire, appliquer des correctifs n’est pas une victoire sans risque.** Fragnesia a été introduite **par le correctif de Dirty Frag**. Chaque correctif peut créer de nouvelles erreurs logiques et, dans ce sous-système, une erreur logique devient un exploit root.

*La conclusion inquiétante : toutes ces vulnérabilités sont dans le cache de pages, accessibles à du code sans privilèges et découvertes par des outils qui progressent chaque trimestre. Aucune liste de blocage ne reste complète.*

## Réponse honnête au contre-argument

Une objection légitime mérite une réponse directe : **les hyperviseurs ont aussi des bogues.**

La surface d’attaque de KVM est réelle. Google gère **kvmCTF** précisément pour trouver ces bogues et les récompense généreusement :

| Niveau | Récompense |
|---|---|
| **Évasion complète de VM** | **$250,000** |
| Écriture mémoire arbitraire | $100,000 |
| Lecture mémoire arbitraire | $50,000 |
| Écriture mémoire relative | $50,000 |
| Déni de service | $20,000 |
| Lecture mémoire relative | $10,000 |

Les récompenses ne se cumulent pas. La cible est un noyau Linux LTS avec KVM, et l’invité est Debian 12.5. L’objectif est une **attaque de l’invité vers l’hôte**.

**Hyunwoo Kim, le même chercheur qui a trouvé Dirty Frag, reçoit aussi des primes KVM** et a gagné la récompense complète de $250,000 pour une évasion de VM. Le résumé honnête est donc que les deux couches ont des failles et qu’une même personne les découvre parfois.

**Mais comparons les ordres de grandeur :**

| | Noyau Linux | Hyperviseur KVM |
|---|---|---|
| **CVE en 2026** | Près de **6 000** | Quelques-unes, les chercheurs individuels en trouvant quelques-unes par an |
| **Accessible depuis** | Tout processus sans privilèges, via l’interface syscall | Seulement du code déjà exécuté dans un invité |
| **Surface d’attaque** | Tout : réseau, systèmes de fichiers, crypto, IPC, pilotes | Le périphérique virtuel et l’interface hypercall |
| **Classe de bogues** | Toute faille de sûreté mémoire ou logique parmi 30 millions de lignes | Limitée à la frontière de virtualisation |

*La différence se mesure en ordres de grandeur, pas en facteur deux. C’est pourquoi les microVM changent le calcul du risque.*

## Ce qui fournit une véritable frontière

Une **microVM** donne à chaque charge de travail sa **propre instance du noyau**, exécutée sur une virtualisation imposée par le matériel, au lieu de partager le noyau hôte par des espaces de noms.

La pile compte trois couches à nommer :

- **Le CPU** fournit des mécanismes matériels pour isoler une région mémoire d’une autre.
- **KVM** expose ces mécanismes au noyau Linux, qui agit alors comme hyperviseur.
- Un **VMM (moniteur de machine virtuelle)**, comme Firecracker ou QEMU, pilote KVM pour créer et exécuter l’invité.

Comme l’invité exécute son propre noyau, un exploit du noyau **dans l’invité** ne compromet que l’invité. Il n’y a pas de noyau partagé à attaquer. L’attaquant doit ensuite s’évader de l’hyperviseur lui-même, la surface plus réduite où se trouvent les bogues KVM.

Deux implémentations comptent dans la pratique et toutes deux figurent dans la recommandation de DepthFirst :

| Technologie | Approche | Notes |
|---|---|---|
| **Firecracker** | VMM dédié, modèle de périphériques minimal | Créé par AWS et conçu pour l’isolation multi-locataire à grande échelle |
| **Kata Containers** | Runtime compatible OCI qui encapsule une microVM | Exécute les images de conteneur standard avec une frontière VM en dessous |

Pour la plupart des équipes, Kata est la migration la plus facile car il accepte les images et outils de conteneur déjà utilisés. **Firecracker a une surface d’attaque plus petite**, car il émule beaucoup moins de périphériques qu’un VMM généraliste.

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="Schéma comparant l’isolation des conteneurs par espaces de noms sur noyau partagé avec l’isolation microVM, où chaque charge de travail exécute son propre noyau sur KVM et un moniteur de machine virtuelle" >}}

## Que faire maintenant

Tous les conteneurs n’ont pas besoin d’une microVM. La décision dépend de **qui exécute du code à l’intérieur**.

| Votre situation | Risque | Que faire |
|---|---|---|
| **Vous exécutez votre propre code**, locataire unique | Faible | Gardez les conteneurs. Appliquez rapidement les correctifs, retirez les capabilities et gardez le système de fichiers racine en lecture seule |
| **Hôtes multi-locataires**, accès shell pour les utilisateurs | **Élevé** | Déplacez les charges non fiables vers des microVM. C’est le premier cas signalé par DepthFirst |
| **Runners CI exécutant des PR non fiables** | **Élevé** | Une pull request devient root sur le runner. Isolez chaque tâche dans sa propre VM |
| **Notebooks, sandbox d’agents, serverless** | **Élevé** | Le code du locataire devient root sur l’hôte. Une microVM par locataire |
| **Clusters Kubernetes** | **Renforcé** | Le cache de pages est partagé sur l’hôte. Un pod doté des bonnes primitives compromet le nœud et traverse les frontières entre locataires |

Le principe commun est simple. **Les conteneurs sont d’excellents outils d’empaquetage et d’isolation de processus.** Ils n’ont jamais été conçus pour contenir du code hostile, mais le secteur les a discrètement détournés vers cet usage parce qu’ils étaient pratiques et peu coûteux.

### Renforcement utile dans tous les cas

Rien de tout cela ne remplace une frontière VM, mais tout élimine des voies faciles :

```bash
# Désactivez les modules exploités par la famille page-cache lorsqu’ils ne sont pas nécessaires
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# Limitez les espaces de noms utilisateur non privilégiés, ce qui bloque les variantes ESP
# Debian et Ubuntu : il s’agit d’une atténuation partielle, pas complète
sysctl -w kernel.unprivileged_userns_clone=0

# Si une exploitation est suspectée, videz le cache de pages pour éliminer les binaires modifiés en mémoire
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# Premiers indicateurs de détection
- Utilisation inattendue de unshare(CLONE_NEWUSER) par une charge de travail sans raison légitime
- Activité NETLINK_XFRM ou associations de sécurité XFRM hors des hôtes IPsec
- Demandes de liaison de sockets AF_ALG
- Chargement de esp4, esp6 ou rxrpc sur des hôtes sans IPsec ni AFS
```

> **Avertissement : `drop_caches` supprime la copie modifiée en mémoire et nettoie la corruption, mais n’élimine pas un attaquant déjà root. Traitez-le comme une réponse à incident, pas comme une remédiation.**

### Le problème de cadence des correctifs

Même avec les meilleures intentions, la correction du noyau est devenue une course :

- Près de **6 000 CVE** publiées cette année dépassent, par leur volume, la plupart des fenêtres de maintenance.
- **Un correctif introduit un bogue.** Fragnesia l’a prouvé dans ce sous-système précis.
- **La liste des mitigations expire.** `algif_aead` était la réponse en avril. En mai, il ne couvrait plus rien de Dirty Frag.

*La rapidité des correctifs est nécessaire, mais insuffisante. L’architecture détermine si un correctif manqué provoque un incident contenu ou compromet l’hôte.*

## La question la plus difficile : qui est l’adversaire ?

La réponse technique est claire. La réponse stratégique dépend d’une question que la plupart des équipes évitent.

**Si votre modèle de menace est un utilisateur curieux ou un développeur négligent, les conteneurs restent adéquats.** Une évasion nécessite une exécution de code locale et un exploit du noyau. Rien de tout cela n’est anodin, et le coût opérationnel d’un transfert généralisé vers des microVM est réel.

**Si votre modèle de menace inclut un adversaire qui exécute du code sur votre infrastructure, les conteneurs ne sont plus qu’un petit obstacle.** La conclusion de DepthFirst mérite d’être citée directement :

> « Le seuil d’entrée pour transformer ces vulnérabilités en armes a tellement baissé qu’il faut supposer que les attaquants peuvent déjà s’évader à volonté des conteneurs standards. »

C’est un fournisseur de sécurité qui a un produit à vendre et défend une architecture précise. Le scepticisme est justifié. **Mais l’argument ne dépend pas du fournisseur.** Le nombre de 6 000 CVE est public, les exploits sont publiés et le noyau est partagé par conception.

*Pour le dire honnêtement : la valeur du conteneur comme frontière diminue face à un attaquant déjà présent, et reste intacte face au reste.*

## Verdict

**Les conteneurs restent adaptés à l’empaquetage, au déploiement et à la séparation des processus. Ils ne constituent plus une frontière de sécurité fiable contre le code hostile.**

Trois affirmations, par niveau de confiance :

1. **Le principe technique est établi.** Les conteneurs partagent le noyau hôte. Chacune des quatre vulnérabilités de cet article a franchi la frontière depuis un compte sans privilèges, et les exploits sont publics.

2. **L’IA a changé le rythme, pas le principe.** Les LPE du noyau ont toujours existé. En trouver une coûte désormais environ **une heure de scan par IA** plutôt que des mois d’effort expert, et deux organisations ont trouvé indépendamment le même zero-day le même jour.

3. **La migration a un coût, comme l’absence de migration.** Firecracker et Kata ajoutent de la surcharge, de la complexité opérationnelle et de nouvelles compétences. Le choix est direct : accepter la surcharge ou le risque qu’un bogue du noyau compromette l’hôte.

**Si vous exploitez une infrastructure multi-locataire ou exécutez du code non fiable, commencez à planifier la migration vers les microVM.** Non parce qu’une catastrophe est imminente, mais parce que la trajectoire est claire et que la migration prend des trimestres, pas des semaines.

**Si vous exécutez vos propres conteneurs en locataire unique, gardez-les.** Corrigez le noyau plus rapidement qu’avant, désactivez les modules inutiles et réévaluez votre décision dès que du code non fiable entre dans l’environnement.

*L’époque où l’on considérait le noyau comme une frontière de confiance inconditionnelle s’achève. Une infrastructure qui prévoit la compromission du noyau est celle qui y survit.*

## Points clés

- **Les conteneurs partagent le noyau hôte.** L’isolation vient des espaces de noms de l’appel `clone`, pas de la virtualisation matérielle. Un bogue du noyau est donc aussi un bogue du conteneur.
- **Quatre vulnérabilités de 2026 ont franchi la frontière** depuis des comptes locaux sans privilèges : Copy Fail, Dirty Frag, Fragnesia et CVE-2026-80521. Toutes ciblent le cache de pages.
- **Près de 6 000 CVE du noyau** avaient été publiées en septembre 2026, et les outils d’IA accélèrent les découvertes. **Copy Fail a été trouvée en environ une heure de scan IA.**
- **Fragnesia a été introduite par le correctif de Dirty Frag.** Le correctif a produit un nouveau bogue root dans le même sous-système.
- **La mitigation de Copy Fail n’arrête pas Dirty Frag.** La liste noire `algif_aead` couvre une vulnérabilité, pas le reste de la famille.
- **CVE-2026-80521 a aussi brisé `nsjail`, `Firejail` et `Bubblewrap`**, pas seulement les runtimes de conteneur.
- **Les microVM changent le calcul du risque** en donnant à chaque charge son propre noyau. KVM a des bogues, mais sa surface est beaucoup plus petite.
- **Choisissez selon qui exécute le code.** Votre code dans un conteneur mono-locataire présente peu de risques. Du code non fiable sur un hôte partagé peut compromettre l’hôte.

## Étapes suivantes

1. **Lisez l’analyse du problème et l’exploit publié :** **[Les conteneurs ne sont plus une frontière de sécurité - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **Consultez l’avis officiel et les mesures de mitigation pour Copy Fail :** **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **Lisez l’analyse technique de Dirty Frag** pour comprendre l’enchaînement et l’échec de la mitigation `algif_aead` : **[Analyse technique de Dirty Frag](https://github.com/V4bel/dirtyfrag)**
4. **Consultez les règles et récompenses kvmCTF** pour comprendre la surface d’attaque de l’hyperviseur : **[Présentation de kvmCTF](https://google.github.io/security-research/kvmctf/rules.html)**
5. **Évaluez ces CVE dans votre environnement** avec notre outil côté navigateur : **[Calculateur CVSS v3.1](/cvss-calculator/)**
6. **Renforcez ce que vous exécutez :** **[Comment sécuriser votre environnement Docker et Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **Comprenez les compromis d’isolation :** **[Docker ou machines virtuelles 2026](/articles/docker-vs-vms/)**
8. **Réduisez les privilèges lorsque vous ne pouvez pas ajouter de frontière :** **[Contrôle d’accès au moindre privilège sous Linux](/articles/mastering-least-privilege-access-control-linux/)**

## Articles connexes

| Article | Contenu |
|---|---|
| **[Docker ou machines virtuelles 2026](/articles/docker-vs-vms/)** | Comparaison architecturale de base, y compris les compromis de performance et de sécurité |
| **[Comment sécuriser votre environnement Docker et Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | Renforcement pratique de la couche conteneur, toujours utile dans une microVM |
| **[Docker dans LXC sur Proxmox : fiabilité, preuves et migration vers une VM](/articles/docker-in-lxc-proxmox-reliability/)** | Conteneurs imbriqués, preuves et moment où déplacer une charge dans une VM complète |
| **[Comprendre la virtualisation : concepts et applications](/articles/understanding-virtualization_-concepts-and-applications/)** | Fondamentaux de l’hyperviseur, dont les fonctions CPU nécessaires aux microVM |
| **[Contrôle d’accès au moindre privilège sous Linux](/articles/mastering-least-privilege-access-control-linux/)** | Réduction des privilèges accordés par une évasion pour limiter son impact |

## Références

1. [Les conteneurs ne sont plus une frontière de sécurité - DepthFirst (Zhenpeng Lin, 22 septembre 2026)](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [CERT/CC Vulnerability Note VU#260001 - Copy Fail (CVE-2026-31431)](https://www.kb.cert.org/vuls/id/260001/)
3. [Site officiel de divulgation de Copy Fail et analyse de l’exploit](https://copy.fail/)
4. [Analyse technique de Dirty Frag - Hyunwoo Kim (CVE-2026-43284, CVE-2026-43500)](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia : élévation locale de privilèges dans le noyau Linux via ESP-in-TCP - Wiz (CVE-2026-46300)](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [Présentation et niveaux de récompense kvmCTF - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [Entrée NVD pour CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Commit upstream mainline corrigeant Copy Fail](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Avis de sécurité Ubuntu sur les correctifs Copy Fail](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [Exploits et soumissions KernelCTF - Google Security Research](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)
