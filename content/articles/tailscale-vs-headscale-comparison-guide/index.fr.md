---
title: "Tailscale ou Headscale ?"
date: 2026-05-24
lastmod: 2026-11-23
toc: true
draft: false
description: "Comparez Tailscale et Headscale selon leur mode d’hébergement, leur gestion des identités, leurs fonctionnalités, leurs coûts, leur exploitation et leur assistance pour choisir un VPN maillé WireGuard adapté à vos besoins."
genre: ["VPN", "Sécurité réseau", "Auto-hébergement", "WireGuard", "Confiance zéro", "Réseaux maillés", "Logiciel libre", "Infrastructure cloud", "Accès à distance", "Gestion réseau"]
tags: ["Tailscale ou Headscale", "Headscale ou Tailscale", "VPN auto-hébergé", "VPN WireGuard", "VPN maillé", "réseau à confiance zéro", "alternative à Tailscale", "configuration de Headscale", "comparatif de VPN", "VPN à code source ouvert", "tarifs de Tailscale", "fonctionnalités de Headscale", "maillage WireGuard", "réseau privé", "performances des VPN", "fonctionnalités de Tailscale", "installation de Headscale", "réseaux maillés", "accès à distance sécurisé", "sécurité des VPN", "coordination réseau", "tailnet", "déploiement de VPN", "VPN d’entreprise", "VPN pour laboratoire domestique", "réseaux auto-hébergés", "coût de Tailscale", "Headscale avec Docker", "gestion de VPN", "serveur de coordination WireGuard"]
cover: "/img/cover/tailscale-vs-headscale-comparison-guide.webp"
coverAlt: "Illustration d’un réseau maillé où des lignes lumineuses relient des appareils sur un fond sombre. Les appareils sont représentés par des icônes stylisées aux couleurs vives, qui symbolisent des connexions sécurisées."
coverCaption: ""
---

## Introduction

**Tailscale** et **Headscale** sont deux serveurs de coordination qui permettent de créer des VPN maillés sécurisés fondés sur [WireGuard](https://www.wireguard.com/). Tailscale est un service commercial hébergé dans le cloud avec une offre gratuite généreuse. Headscale est une solution open source et auto-hébergée qui implémente le protocole de contrôle de Tailscale. Comprendre les différences entre ces solutions vous aide à choisir celle qui répond aux besoins réseau de votre organisation.

La décision principale concerne **la maîtrise du plan de contrôle**. Choisissez Tailscale si la gestion des identités, l’administration et l’assistance sont vos priorités. Évaluez Headscale si l’auto-hébergement et la maîtrise des données de coordination justifient la charge d’exploitation supplémentaire. Les sections suivantes comparent les fonctionnalités, les performances, les coûts, la sécurité et la maintenance.

______

## Comprendre les VPN maillés et WireGuard

Pour comparer les deux solutions, il faut d’abord comprendre la technologie sur laquelle elles reposent.

### Qu’est-ce que WireGuard ?

**WireGuard** est un protocole VPN moderne et performant qui offre les avantages suivants.
- **Performances exceptionnelles** avec une vitesse jusqu’à 10 fois supérieure à celle d’OpenVPN
- **Surface d’attaque réduite** avec seulement ~4 000 lignes de code (contre plus de 100 000 pour OpenVPN)
- **Cryptographie moderne** avec Curve25519, ChaCha20 et Poly1305
- **Intégration au noyau Linux** depuis Linux 5.6 (2020)

### Qu’est-ce qu’un VPN maillé ?

Un **VPN maillé** établit des connexions pair à pair entre les appareils sans faire transiter tout le trafic par un serveur central.
- **Connexions directes** entre appareils lorsque c’est possible
- **Traversée du NAT** et des pare-feu de façon automatique
- **Latence réduite** grâce à l’absence de sauts inutiles par des serveurs centraux
- **Meilleures performances** grâce à l’utilisation de toute la bande passante entre pairs

### Le rôle des serveurs de coordination

WireGuard est un protocole. Pour créer un VPN maillé, vous avez besoin d’un **serveur de coordination** (ou plan de contrôle) qui assure les fonctions suivantes.
- Gère l’authentification et l’autorisation des appareils
- Distribue les clés de chiffrement
- Facilite la traversée du NAT et la découverte des pairs
- Gère les politiques de contrôle d’accès
- Assure la résolution DNS au sein du réseau

**Tailscale** et **Headscale** sont deux serveurs de coordination qui remplissent ces fonctions.

______

## Vue d’ensemble de Tailscale et Headscale

| Aspect | Tailscale | Headscale |
|--------|-----------|-----------|
| **Type** | SaaS commercial | Open source et auto-hébergé |
| **Licence** | Propriétaire (offre gratuite disponible) | Licence BSD à 3 clauses |
| **Hébergement** | Dans le cloud (géré par Tailscale) | Auto-hébergé (géré par vos soins) |
| **Première version** | 2019 | 2020 |
| **Responsable principal de la maintenance** | Tailscale Inc. | Juan Font et la communauté |
| **Étoiles GitHub** | S. O. (code source fermé) | Plus de 38 900 (en 2026) |
| **Complexité de la configuration** | Très faible (5 minutes) | Modérée (30 à 60 minutes) |
| **Coût mensuel (100 utilisateurs)** | De 0 $ (gratuit) à 18 $ par utilisateur (Enterprise) | Coût d’hébergement du serveur uniquement (5 à 50 $ par mois) |
| **Compatibilité des protocoles** | Protocole Tailscale | Protocole Tailscale (compatible) |

______

## Comparaison détaillée des fonctionnalités

### Fonctionnalités réseau essentielles

| Fonctionnalité | Tailscale | Headscale | Observations |
|---------|-----------|-----------|-------|
| **Maillage fondé sur WireGuard** | ✅ Oui | ✅ Oui | Les deux utilisent WireGuard pour toutes les connexions entre pairs |
| **Traversée automatique du NAT** | ✅ Oui | ✅ Oui | STUN/DERP pour une connectivité fiable |
| **Routage de sous-réseaux** | ✅ Oui | ✅ Oui | Accès aux réseaux derrière une passerelle |
| **Nœuds de sortie** | ✅ Oui | ✅ Oui | Acheminement de tout le trafic Internet par un nœud |
| **MagicDNS** | ✅ Oui | ✅ Oui | Résolution des noms dans le réseau maillé |
| **DNS scindé** | ✅ Oui | ✅ Oui | Remplacement des paramètres DNS pour certains domaines |
| **Routage à haute disponibilité** | ✅ Oui | ✅ Oui | Basculement automatique entre les routes |
| **Prise en charge d’IPv6** | ✅ Complète | ✅ Complète | Adressage IPv6 complet dans le maillage |
| **Prise en charge du multicast** | ❌ Non | ❌ Non | Aucune des deux solutions ne prend actuellement en charge le multicast |

### Contrôle d’accès et sécurité

| Fonctionnalité | Tailscale | Headscale | Observations |
|---------|-----------|-----------|-------|
| **Moteur ACL** | ✅ Avancé | ✅ Compatible | Headscale implémente la syntaxe ACL de Tailscale |
| **Contrôle d’accès par étiquettes** | ✅ Oui | ✅ Oui | Regroupement des appareils à l’aide d’étiquettes |
| **Gestion des utilisateurs et des groupes** | ✅ Oui | ✅ Oui | Headscale repose sur la notion d’« utilisateurs » |
| **OpenID Connect (OIDC)** | ✅ Oui | ✅ Oui | Authentification avec Google, Okta, Keycloak, etc. |
| **Authentification SAML** | ✅ Oui (Enterprise) | ❌ Non | Tailscale uniquement |
| **Tailnet Lock** | ✅ Oui | ❌ Non | Empêche le recours à des serveurs de coordination non autorisés |
| **Contrôles de conformité des appareils** | ✅ Oui (bêta) | ❌ Non | Vérification de la conformité de l’appareil avant l’accès |
| **Accès juste à temps** | ✅ Oui | ❌ Non | Autorisations élevées temporaires |
| **Journalisation d’audit** | ✅ Étendue | ⚠️ De base | Tailscale fournit des journaux détaillés |

### Gestion et administration

| Fonctionnalité | Tailscale | Headscale | Limites |
|---------|-----------|-----------|-------------|
| **Interface web** | ✅ Officielle | ⚠️ Communautaire | Plusieurs interfaces communautaires existent pour Headscale |
| **Gestion en ligne de commande** | ✅ Oui | ✅ Oui | Les deux proposent des outils complets en ligne de commande |
| **API REST** | ✅ Oui | ✅ Oui | Automatisation des tâches de gestion |
| **API gRPC** | ❌ Non | ✅ Oui | Headscale fournit une API gRPC pour l’administration à distance |
| **Fournisseur Terraform** | ✅ Officiel | ❌ Non | Intégration de l’infrastructure en tant que code |
| **Opérateur Kubernetes** | ✅ Officiel | ⚠️ Communautaire | Opérateur communautaire pour Headscale |
| **Applications mobiles** | ✅ iOS, Android | ✅ Compatibles | Utilisation des applications Tailscale avec un serveur Headscale |
| **Console d’administration** | ✅ Complète | ❌ Non | Headscale repose sur la ligne de commande et l’API |
| **Accès pour plusieurs administrateurs** | ✅ Oui | ⚠️ Manuel | Headscale exige une mise en œuvre personnalisée |

### Fonctionnalités avancées

| Fonctionnalité | Tailscale | Headscale | Observations |
|---------|-----------|-----------|-------|
| **Tailscale SSH** | ✅ Oui | ⚠️ Côté serveur uniquement | Les nœuds Headscale prennent uniquement le rôle de serveur SSH |
| **Taildrop (partage de fichiers)** | ✅ Oui | ⚠️ Incomplète | Prise en charge limitée de Taildrop dans Headscale |
| **Funnel (accès entrant public)** | ✅ Oui | ❌ Non | Exposition de services à l’Internet public |
| **Serve (partage privé)** | ✅ Oui | ❌ Non | Partage de services au sein du tailnet |
| **Collecte des services** | ✅ Oui | ❌ Limitée | Découverte des services sur le réseau |
| **Tailscale DERP** | ✅ Réseau mondial | ⚠️ Intégré | Headscale intègre DERP et permet aussi d’utiliser un relais personnalisé |
| **Serveurs DERP personnalisés** | ✅ Oui | ✅ Oui | Les deux prennent en charge les serveurs relais personnalisés |
| **Extension Docker** | ✅ Oui | ❌ Non | Extension Docker de Tailscale pour la mise en réseau des conteneurs |

______

## Comparaison des tarifs (2026)

### Tarifs de Tailscale

| Offre | Coût mensuel | Coût annuel | Appareils | Fonctionnalités |
|------|-------------|-------------|---------|----------|
| **Personal** | 0 $ | 0 $ | Jusqu’à 100 | 1 utilisateur, fonctionnalités de base, assistance communautaire |
| **Personal Pro** | 6 $ par utilisateur et par mois | 48 $ par utilisateur et par an | Illimités | Plusieurs utilisateurs, routage de sous-réseaux, ACL |
| **Team** | 10 $ par utilisateur et par mois | 100 $ par utilisateur et par an | Illimités | Console d’administration, journaux d’audit, SSO |
| **Business** | 15 $ par utilisateur et par mois | 150 $ par utilisateur et par an | Illimités | ACL avancées, groupes d’utilisateurs, assistance prioritaire |
| **Enterprise** | 18 $ ou plus par utilisateur et par mois | Sur mesure | Illimités | Tailnet Lock, SAML, assistance dédiée, SLA |

**À noter.** L’offre gratuite Personal de Tailscale prend en charge jusqu’à 100 appareils pour un usage personnel, ce qui la rend particulièrement généreuse pour les laboratoires domestiques et les petits déploiements.

### Coûts de Headscale

Headscale est **gratuit et open source**, avec des coûts d’infrastructure à votre charge.

| Ressource | Fourchette de coût mensuel | Observations |
|----------|-------------------|-------|
| **Petit VPS** (1 CPU, 1 Go de RAM) | 5 à 10 $ | Adapté à moins de 50 appareils |
| **VPS moyen** (2 CPU, 4 Go de RAM) | 15 à 25 $ | Adapté à 50 à 200 appareils |
| **Grand VPS** (4 CPU, 8 Go de RAM) | 40 à 80 $ | Adapté à 200 à 1 000 appareils ou plus |
| **Nom de domaine** | 10 à 15 $ par an | Pour les certificats TLS |
| **Bande passante** | Généralement incluse | Vérifiez les limites fixées par le fournisseur du VPS |
| **Temps à consacrer** | Variable | Configuration, maintenance, mises à jour |

**Coût total de possession (100 utilisateurs)**
- **Tailscale** coûte 0 $ (offre gratuite) ou 1 000 à 1 800 $ par mois (offres payantes)
- **Headscale** coûte 15 à 30 $ par mois et demande 5 à 10 heures de configuration et 2 à 5 heures de maintenance par mois

**Seuil de rentabilité.** Pour les organisations qui comptent plus de 3 à 5 utilisateurs payants, Headscale devient rentable si vous évaluez votre temps à moins de 50 $ de l’heure.

______

## Comparaison des performances

### Latence et débit

Tailscale et Headscale utilisent WireGuard pour le plan de données. Leurs **performances en pair à pair sont donc identiques**.

| Indicateur | Tailscale | Headscale |
|--------|-----------|-----------|
| **Latence supplémentaire en pair à pair** | <1 ms | <1 ms |
| **Débit en pair à pair** | Proche du débit natif (~900 Mbit/s sur 1 Gbit/s) | Proche du débit natif |
| **Débit du trafic relayé (DERP)** | 50 à 300 Mbit/s | 10 à 200 Mbit/s (selon votre serveur) |
| **Latence du trafic relayé** | +10 à 50 ms | +5 à 100 ms (selon l’emplacement) |
| **Établissement de la connexion** | 100 à 500 ms | 200 à 800 ms |
| **Propagation des mises à jour des politiques ACL** | <5 secondes | <30 secondes |

**Différence principale.** Tailscale exploite un réseau mondial de relais DERP, avec des serveurs répartis dans le monde entier. Ce réseau offre de meilleures performances de secours lorsque les connexions directes échouent. Le relais DERP intégré à Headscale s’exécute sur votre serveur, ce qui risque d’augmenter la latence en l’absence de répartition géographique.

### Capacité de mise à l’échelle

| Aspect | Tailscale | Headscale |
|--------|-----------|-----------|
| **Nombre maximal de nœuds** | 100 000 ou plus (testé) | ~5 000 (d’après les retours de la communauté) |
| **Nombre de nœuds recommandé** | Illimité | <1 000 pour un seul serveur |
| **Requêtes par minute du plan de contrôle (RPM)** | Fortement optimisées | Selon les caractéristiques du serveur |
| **Mémoire par nœud** | S. O. (service géré) | ~1 à 5 Mo (côté serveur) |
| **Base de données** | PostgreSQL (gérée) | SQLite ou PostgreSQL |

______

## Comparaison de la sécurité

### Sécurité de l’infrastructure

| Aspect | Tailscale | Headscale | Évaluation |
|--------|-----------|-----------|------------|
| **Confiance dans le serveur de coordination** | Vous devez faire confiance à Tailscale Inc. | Vous contrôlez le serveur | Headscale protège mieux la confidentialité |
| **Clés de chiffrement** | Les appareils les génèrent et ne les transmettent jamais à Tailscale | Les appareils les génèrent et ne les transmettent jamais au serveur | ✅ Excellente gestion dans les deux cas |
| **Sécurité du plan de données** | WireGuard (excellente) | WireGuard (excellente) | ✅ Excellente dans les deux cas |
| **Sécurité du plan de contrôle** | HTTPS + attestation | HTTPS + équivalent facultatif de Tailnet Lock | ⚠️ Tailscale est légèrement plus robuste |
| **Piste d’audit** | Journalisation complète | Journalisation de base | ⚠️ Tailscale offre une meilleure traçabilité |
| **Programme de primes aux vulnérabilités** | ✅ Oui | ❌ Non | Tailscale a rémunéré des chercheurs en sécurité |
| **Certifications de sécurité** | SOC 2 Type II | S. O. | Tailscale répond aux besoins des entreprises |

### Confidentialité

| Aspect lié à la confidentialité | Tailscale | Headscale |
|----------------|-----------|-----------|
| **Visibilité des métadonnées** | Tailscale voit les noms des appareils, les adresses IP et les métadonnées de connexion | Vous contrôlez toutes les métadonnées |
| **Visibilité du trafic** | ❌ Trafic invisible (chiffré) | ❌ Trafic invisible (chiffré) |
| **Exigences de conformité** | Relève de la juridiction américaine | Relève de la juridiction où se trouve votre serveur |
| **Résidence des données** | Infrastructure cloud de Tailscale | Centre de données de votre choix |

**Verdict.** Les deux solutions offrent **un excellent chiffrement et une architecture à connaissance nulle** pour le trafic lui-même. Headscale offre une meilleure **confidentialité**, car vous contrôlez toutes les métadonnées. Tailscale offre de meilleures **garanties de sécurité** grâce aux certifications, aux audits et aux primes aux vulnérabilités.

______

## Comparaison de la configuration et du déploiement

### Configuration de Tailscale

**Temps nécessaire** estimé à 5 à 10 minutes

1. **Créez un compte** sur [tailscale.com](https://tailscale.com/)
2. **Installez le client** sur chaque appareil (une commande ou le téléchargement d’une application)
3. **Authentifiez-vous** avec OAuth (Google, Microsoft, GitHub, etc.)
4. **Configurez les ACL** (facultatif, possible ultérieurement)
5. **C’est terminé !** Le réseau est immédiatement opérationnel

**Exemple d’installation (Linux)**

> **Examinez le programme d’installation avant de l’exécuter.** Téléchargez-le dans un fichier temporaire, inspectez-le et confirmez la distribution de la machine hôte ainsi que la provenance du paquet. Après l’installation, exécutez `tailscale version` et `tailscale status` pour vérifier le résultat. Si l’installation échoue, supprimez le paquet avec le gestionnaire de paquets de votre distribution et restaurez l’état précédent des paquets à partir de votre sauvegarde système.

```bash
curl -fsSL https://tailscale.com/install.sh -o /tmp/tailscale-install.sh
less /tmp/tailscale-install.sh
sh /tmp/tailscale-install.sh
sudo tailscale up
```

### Configuration de Headscale

**Temps nécessaire** estimé à 30 à 90 minutes (première installation)

1. **Préparez un serveur** (VPS avec une adresse IP publique, au moins 1 Go de RAM recommandé)
2. **Configurez le DNS** (enregistrement A qui pointe vers le serveur)
3. **Installez Headscale** (avec le gestionnaire de paquets ou Docker)
4. **Configurez Headscale** (config.yaml avec l’URL du serveur, la base de données, etc.)
5. **Configurez les certificats TLS** (Let's Encrypt recommandé)
6. **Démarrez le service Headscale**
7. **Créez les utilisateurs** en ligne de commande avec `headscale users create alice`
8. **Installez le client Tailscale** sur chaque appareil
9. **Configurez les clients** pour utiliser le serveur de coordination personnalisé
10. **Enregistrez les nœuds** par authentification web ou avec des clés de préauthentification
11. **Configurez les ACL** (fichier policy.json)

**Exemple d’installation de Headscale (Ubuntu)**
```bash
# Installer Headscale
curl -fsSL https://pkgs.headscale.net/headscale_<VERSION>_linux_amd64.deb -o headscale.deb
sudo apt install ./headscale.deb

# Configurer Headscale
sudo nano /etc/headscale/config.yaml
# Définir server_url sur https://headscale.example.com

# Démarrer le service
sudo systemctl enable --now headscale

# Créer un utilisateur
headscale users create myuser

# Sur la machine cliente
sudo tailscale up --login-server=https://headscale.example.com
```

**Solution la plus simple à configurer.** La configuration initiale de **Tailscale** est nettement plus simple.

______

## Complexité de l’exploitation

### Gestion au quotidien

| Tâche | Tailscale | Headscale | Solution la plus simple |
|------|-----------|-----------|--------|
| **Ajouter un appareil** | Cliquer sur un lien et s’authentifier | Générer une clé d’authentification ou s’authentifier sur le web | Tailscale (plus simple) |
| **Mettre à jour les ACL** | Modifier les ACL dans l’interface web, avec effet immédiat | Modifier le fichier et recharger la configuration | Tailscale (plus simple) |
| **Consulter l’état de la connectivité** | Tableau de bord web | Ligne de commande ou interface communautaire | Tailscale (plus simple) |
| **Diagnostiquer les problèmes** | Journaux détaillés dans le tableau de bord | Journaux du serveur et des clients | Tailscale (plus simple) |
| **Mettre à jour le logiciel** | Automatique | Mises à jour manuelles du serveur | Tailscale (plus simple) |
| **Sauvegarder la configuration** | Automatique | Manuel (base de données et configuration) | Tailscale (plus simple) |
| **Reprendre l’activité après un sinistre** | Automatique | Restauration manuelle à partir d’une sauvegarde | Tailscale (plus simple) |

### Charge de maintenance

**Tailscale (service géré)**
- ✅ Aucune maintenance du serveur
- ✅ Mises à jour et correctifs de sécurité automatiques
- ✅ Redondance et basculement intégrés
- ✅ Assistance professionnelle disponible
- ❌ Dépendance à la disponibilité du service Tailscale

**Headscale (auto-hébergé)**
- ⚠️ Mises à jour et correctifs de sécurité du système d’exploitation du serveur (chaque mois)
- ⚠️ Mises à jour du logiciel Headscale (tous les 1 à 3 mois)
- ⚠️ Sauvegardes de la base de données (fréquence quotidienne recommandée)
- ⚠️ Renouvellement des certificats TLS (automatisé avec Let's Encrypt)
- ⚠️ Mise en place de la supervision et des alertes
- ⚠️ Dépannage en cas de problème
- ✅ Maîtrise complète de l’infrastructure
- ✅ Aucune dépendance à un service tiers

**Estimation du temps à consacrer chaque mois**
- **Tailscale** demande 30 minutes (examen des politiques, ajout d’utilisateurs)
- **Headscale** demande 2 à 5 heures (mises à jour, supervision, dépannage)

______

## Recommandations par cas d’usage

### Dans quels cas choisir Tailscale ?

✅ **Vous voulez la configuration la plus rapide** - 5 minutes entre la création du compte et la mise en service du réseau\
✅ **Vous avez moins de 100 appareils** - L’offre gratuite couvre l’usage personnel et celui des petites entreprises\
✅ **Vous privilégiez la facilité d’utilisation** - Une interface web et une expérience utilisateur parmi les meilleures de leur catégorie\
✅ **Vous avez besoin de fonctionnalités d’entreprise** - SSO, journaux d’audit, Tailnet Lock, contrôles de conformité des appareils\
✅ **Vous voulez gagner du temps** - Aucune maintenance à votre charge et mises à jour automatiques\
✅ **Vous avez besoin d’une disponibilité garantie** - Le SLA de Tailscale prévoit une disponibilité de 99,99 % (Enterprise)\
✅ **Vous voulez des applications mobiles officielles** - Applications natives iOS et Android avec toutes les fonctionnalités\
✅ **Vous avez besoin d’une assistance professionnelle** - Les offres payantes incluent une assistance prioritaire\
✅ **La conformité compte pour vous** - Certification SOC 2 Type II\
✅ **Vous exercez une activité commerciale** - Tarification simple par utilisateur, sans frais cachés\

### Dans quels cas choisir Headscale ?

✅ **Vous exigez une souveraineté totale sur vos données** - Toutes les métadonnées restent sur votre infrastructure\
✅ **Vous avez des contraintes de confidentialité ou de conformité** - Les données doivent rester dans certaines juridictions\
✅ **Vous avez les compétences techniques** - Vous maîtrisez l’administration de systèmes Linux, Docker et le dépannage\
✅ **Vous avez plus de 10 utilisateurs payants** - Les économies deviennent importantes à grande échelle\
✅ **Vous voulez apprendre** - Un projet formateur pour comprendre les VPN maillés\
✅ **Vous préférez l’open source** - Vous pouvez auditer le code, contribuer aux corrections et le personnaliser\
✅ **Vous surveillez votre budget** - Faibles coûts récurrents (5 à 30 $ par mois pour le serveur)\
✅ **Vous disposez déjà d’une infrastructure** - Déploiement possible sur votre infrastructure Kubernetes ou vos machines virtuelles\
✅ **Vous avez besoin d’une API gRPC** - Headscale fournit une API gRPC pour l’automatisation avancée\
✅ **Vous pratiquez déjà l’auto-hébergement** - Headscale s’intègre à votre environnement auto-hébergé\

### Approche hybride avec les deux solutions

Certaines organisations utilisent **les deux solutions**.

1. **Tailscale pour la production** - Infrastructure critique avec SLA et assistance
2. **Headscale pour le développement et les tests** - Environnements de développement économiques
3. **Tailscale pour les utilisateurs sans profil technique** - Prise en main facile pour le personnel
4. **Headscale pour les équipes techniques** - Ingénieurs à l’aise avec l’auto-hébergement

______

## Scénarios de migration

### Migrer de Tailscale vers Headscale

**Motivations** possibles pour la migration : réduction des coûts, souveraineté des données, maîtrise accrue

**Étapes**
1. Déployez le serveur Headscale et validez son fonctionnement
2. Testez Headscale avec un sous-ensemble d’appareils non critiques
3. Exportez les ACL de Tailscale et adaptez-les à Headscale
4. Migrez progressivement les appareils vers le serveur de coordination Headscale
5. Mettez à jour les configurations DNS et les routes de sous-réseaux
6. Résiliez l’abonnement Tailscale

**Difficultés**
- Aucun outil de migration automatisée
- Tous les appareils doivent s’authentifier à nouveau
- Certaines fonctionnalités (Funnel, Serve, Taildrop) se comportent différemment
- La syntaxe des ACL est compatible et doit être testée

**Temps à prévoir** entre 5 et 20 heures selon la complexité

### Migrer de Headscale vers Tailscale

**Motivations** possibles pour la migration : réduction de la charge d’exploitation, fonctionnalités d’entreprise, meilleure assistance

**Étapes**
1. Créez un compte Tailscale et configurez les ACL
2. Installez les clients Tailscale (ils peuvent remplacer les clients existants sur les mêmes appareils)
3. Migrez les appareils en exécutant `tailscale up` sans spécifier de serveur personnalisé
4. Vérifiez la connectivité et les contrôles d’accès
5. Mettez le serveur Headscale hors service

**Difficultés**
- Tous les appareils doivent s’authentifier à nouveau
- Certains utilisateurs auront peut-être besoin d’un compte Tailscale (e-mail ou SSO)
- Il faut gérer le changement et communiquer avec les utilisateurs

**Temps à prévoir** entre 2 et 8 heures selon la taille du déploiement

______

## Communauté et écosystème

### Écosystème de Tailscale

| Ressource | Disponibilité |
|----------|--------------|
| **Documentation officielle** | ✅ Complète et bien tenue à jour |
| **Forum communautaire** | ✅ Forum actif avec la participation de l’équipe Tailscale |
| **Serveur Discord** | ✅ Très actif, avec une équipe réactive |
| **Tickets GitHub** | ❌ Code source fermé (retours via le forum) |
| **Stack Overflow** | ✅ Étiquette active avec plus de 2 000 questions |
| **Tutoriels YouTube** | ✅ Contenus officiels et communautaires |
| **Intégrations** | ✅ Docker, Kubernetes, Terraform, Synology, QNAP, etc. |

### Écosystème de Headscale

| Ressource | Disponibilité |
|----------|--------------|
| **Documentation officielle** | ✅ De bonne qualité, tenue à jour par la communauté |
| **Forum communautaire** | ⚠️ GitHub Discussions sert de forum |
| **Serveur Discord** | ✅ Serveur communautaire actif |
| **Tickets GitHub** | ✅ Open source, suivi des tickets actif (plus de 38 900 étoiles) |
| **Stack Overflow** | ⚠️ Communauté plus petite (~100 questions) |
| **Tutoriels YouTube** | ⚠️ Contenus créés par la communauté |
| **Interfaces web** | ⚠️ Plusieurs options communautaires (Headscale-UI, Headplane, ouroboros) |
| **Opérateur Kubernetes** | ⚠️ Opérateur maintenu par la communauté |

**Taille des communautés (2026)**
- **Tailscale** compte plus de 100 000 membres actifs et bénéficie du soutien d’une entreprise bien financée
- **Headscale** est un projet open source qui compte plus de 10 000 membres actifs

______

## Mesures de performances en conditions réelles (2026)

Les résultats s’appuient sur les tests de la communauté et les mesures publiées.

### Tests de débit (pair à pair)

| Scénario | Tailscale | Headscale | Référence (sans VPN) |
|----------|-----------|-----------|-------------------|
| **LAN gigabit** | 940 Mbit/s | 940 Mbit/s | 945 Mbit/s |
| **WAN (100 Mbit/s)** | 98 Mbit/s | 98 Mbit/s | 100 Mbit/s |
| **WAN (fibre à 1 Gbit/s)** | 920 Mbit/s | 920 Mbit/s | 950 Mbit/s |
| **Intercontinental (DERP)** | 180 Mbit/s | 95 Mbit/s | S. O. |

**Analyse.** Les connexions directes en pair à pair offrent des performances identiques. Tailscale obtient de meilleurs résultats sur les connexions relayées grâce à son réseau mondial de relais DERP.

### Tests de latence

| Scénario | Tailscale | Headscale | Référence |
|----------|-----------|-----------|----------|
| **Ping sur le LAN** | 1,2 ms | 1,2 ms | 0,8 ms |
| **WAN régional (100 miles)** | 15 ms | 15 ms | 12 ms |
| **D’un bout à l’autre du pays** | 48 ms | 48 ms | 45 ms |
| **Intercontinental (connexion directe)** | 155 ms | 155 ms | 152 ms |
| **Intercontinental (DERP)** | 185 ms | 220 ms | S. O. |

**Analyse.** Les deux solutions ajoutent une faible latence (~1 à 2 ms) aux connexions directes. La latence du relais DERP de Headscale varie selon l’emplacement du serveur.

### Utilisation des ressources

| Indicateur | Client Tailscale | Client Headscale | Serveur Headscale |
|--------|------------------|------------------|------------------|
| **Utilisation de la RAM (au repos)** | 80 à 120 Mo | 80 à 120 Mo | 50 à 200 Mo (selon le nombre de nœuds) |
| **Utilisation de la RAM (en activité)** | 120 à 200 Mo | 120 à 200 Mo | 100 à 500 Mo |
| **Utilisation du CPU (au repos)** | <1 % | <1 % | <1 % |
| **Utilisation du CPU (en activité)** | 5 à 15 % | 5 à 15 % | 3 à 20 % (selon le nombre de nœuds) |
| **Espace disque utilisé** | 100 à 500 Mo | 100 à 500 Mo | 100 Mo à 2 Go (base de données) |

______

## Exemples de configuration avancée

### Headscale avec Docker Compose

```yaml
version: '3'
services:
  headscale:
    image: headscale/headscale:0.28.0
    container_name: headscale
    restart: unless-stopped
    ports:
      - "127.0.0.1:8080:8080"  # API/web
      - "443:443"              # HTTPS
      - "3478:3478/udp"        # STUN
    volumes:
      - ./config:/etc/headscale
      - ./data:/var/lib/headscale
    command: serve
    environment:
      - TZ=UTC
```

### Exemple d’ACL pour Headscale

```json
{
  "groups": {
    "group:admin": ["alice@", "bob@"],
    "group:developers": ["charlie@", "diana@"]
  },
  "hosts": {
    "production-db": "100.64.0.10/32",
    "staging-db": "100.64.0.20/32"
  },
  "acls": [
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["*:*"]
    },
    {
      "action": "accept",
      "src": ["group:developers"],
      "dst": ["staging-db:5432", "autogroup:self:*"]
    }
  ]
}
```

### Configuration du client Tailscale (avec Headscale)

```bash
# Linux
sudo tailscale up \
  --login-server=https://headscale.example.com \
  --accept-routes \
  --advertise-tags=tag:server

# Avec une clé de préauthentification
headscale preauthkeys create --user engineering --expiration 1h

sudo tailscale up \
  --login-server=https://headscale.example.com \
  --authkey=<YOUR_AUTH_KEY>
```

______

## Résolution des problèmes courants

### Problèmes avec Tailscale

| Problème | Solution |
|---------|----------|
| **Impossible de se connecter au serveur de coordination** | Vérifiez le pare-feu et la connexion Internet |
| **Échec de la connexion directe** | Le basculement vers DERP est généralement automatique. Vérifiez les paramètres NAT |
| **Latence élevée** | Vérifiez que la connexion s’établit directement, sans passer par un relais |
| **Clé expirée** | Authentifiez-vous à nouveau ou désactivez l’expiration des clés dans la console d’administration |
| **Les ACL bloquent le trafic** | Examinez les règles ACL et testez la configuration |

### Problèmes avec Headscale

| Problème | Solution |
|---------|----------|
| **Les nœuds ne s’enregistrent pas** | Vérifiez que l’URL de Headscale est accessible et contrôlez le certificat TLS |
| **Échec de la résolution DNS** | Vérifiez la configuration de MagicDNS dans config.yaml |
| **Le relais DERP ne fonctionne pas** | Vérifiez que le port STUN (3478/udp) est ouvert et contrôlez la configuration DERP |
| **Nœuds hors ligne après le redémarrage** | Vérifiez que les clients se lancent au démarrage |
| **Les modifications des ACL ne s’appliquent pas** | Rechargez Headscale avec `systemctl reload headscale` |
| **Base de données corrompue** | Restaurez la base à partir d’une sauvegarde et envisagez PostgreSQL pour la production |

### Commandes de diagnostic

```bash
# Diagnostics de Tailscale
tailscale status
tailscale netcheck
tailscale ping <hostname>
tailscale debug derp

# Diagnostics de Headscale
headscale nodes list
headscale nodes list-routes
headscale debug routes
journalctl -u headscale -f  # Afficher les journaux
```

______

## Bonnes pratiques de sécurité

### Pour les deux solutions

1. **Activez l’expiration des clés** - Exigez une nouvelle authentification à intervalles réguliers
2. **Appliquez le principe du moindre privilège** - Accordez uniquement les accès nécessaires dans les ACL
3. **Étiquetez les nœuds d’infrastructure** - Distinguez les appareils des utilisateurs des serveurs
4. **Activez la MFA** - Exigez une authentification multifacteur à la connexion des utilisateurs
5. **Surveillez les journaux d’accès** - Examinez régulièrement les habitudes de connexion
6. **Maintenez les clients à jour** - Appliquez rapidement les correctifs de sécurité

### Sécurité propre à Headscale

1. **Durcissez le système d’exploitation du serveur** - Suivez les référentiels CIS et désactivez les services inutiles
2. **Utilisez Let's Encrypt** - Automatisez la gestion des certificats TLS
3. **Déployez fail2ban** - Bloquez les tentatives par force brute
4. **Effectuez des sauvegardes régulières** - Automatisez les sauvegardes de la base de données vers un emplacement distinct
5. **Installez rapidement les mises à jour** - Suivez les versions de Headscale pour repérer les correctifs de sécurité
6. **Segmentez le réseau** - Isolez le serveur Headscale sur un VLAN d’administration
7. **Activez le pare-feu** - Exposez uniquement les ports nécessaires (443, 3478/udp)

______

## Feuille de route et développements à venir

### Feuille de route de Tailscale (2026)

D’après les déclarations publiques de Tailscale.
- ✅ **Disponible** : Aperture (passerelle de gouvernance de l’IA), contrôles de conformité des appareils améliorés
- 🚧 **En développement** : détection avancée des menaces, prise en charge de davantage de plateformes
- 📋 **Prévu** : mode IPv6 uniquement, meilleure observabilité, intégrations supplémentaires

### État de Headscale (2026)

D’après les jalons GitHub et les discussions de la communauté.
- ✅ **Ajouts récents** : authentification OIDC, améliorations de DERP et meilleure prise en charge des ACL
- 🚧 **En développement** : améliorations de Taildrop, meilleure intégration des interfaces web
- 📋 **Demandes de la communauté** : équivalent de Funnel/Serve, journalisation avancée, mode haute disponibilité

**Évaluation de la maturité**
- **Tailscale** est conçu pour la production, répond aux besoins des entreprises et bénéficie de plus de 5 ans de développement
- **Headscale** est prêt pour la production dans les cas d’usage courants et bénéficie d’un développement actif assuré par la communauté

______

## Conclusion

**Tailscale** et **Headscale** offrent tous deux d’excellentes fonctionnalités de VPN maillé fondées sur WireGuard. Ils répondent aux besoins de publics et de cas d’usage différents.

**Dans quels cas choisir Tailscale ?**
- Vous privilégiez la simplicité et souhaitez être opérationnel en quelques minutes
- Votre équipe est de petite taille (moins de 100 appareils) et bénéficie de l’offre gratuite généreuse
- Vous avez besoin de fonctionnalités d’entreprise comme le SSO, la journalisation d’audit et l’assistance professionnelle
- Vous préférez les services gérés à l’auto-hébergement
- Les certifications de conformité (SOC 2) comptent pour vous

**Dans quels cas choisir Headscale ?**
- Vous exigez une maîtrise totale de votre infrastructure et de vos métadonnées
- Vous avez les compétences techniques et appréciez l’auto-hébergement
- La réduction des coûts est essentielle (économies importantes au-delà de 10 utilisateurs payants)
- La souveraineté des données et la confidentialité sont prioritaires
- Vous préférez les solutions open source que vous pouvez auditer et personnaliser

**Principales recommandations pour 2026**

1. **Startups et PME.** Commencez par **l’offre gratuite de Tailscale**. Elle est imbattable pour 0 à 100 appareils.
2. **Services informatiques des grandes entreprises.** Avec le SSO et l’assistance, **Tailscale Enterprise** offre le meilleur coût total de possession si vous tenez compte du temps de travail du personnel.
3. **Utilisateurs soucieux de la confidentialité.** **Headscale** offre un maximum de maîtrise et de confidentialité.
4. **Utilisateurs expérimentés de laboratoires domestiques.** **Headscale** est une excellente occasion d’apprendre.
5. **Organisations qui adoptent une approche hybride.** Utilisez **Tailscale pour la production** et **Headscale pour le développement et les tests**.

Dans les deux cas, vous bénéficiez de WireGuard, une technologie de premier plan pour des réseaux modernes et sécurisés. Le choix dépend de vos priorités et des compromis entre **simplicité et maîtrise**, **service géré et auto-hébergement**, et **coût et fonctionnalités**.

Pour la plupart des organisations en 2026, **le service géré de Tailscale** offre le meilleur équilibre entre fonctionnalités, facilité d’utilisation et rapport qualité-prix. Pour les organisations qui ont des exigences précises en matière de souveraineté, de confidentialité ou de coûts, **Headscale constitue une alternative auto-hébergée intéressante**.

______

## Références et ressources

1. [Site officiel de Tailscale](https://tailscale.com/)
2. [Documentation de Tailscale](https://tailscale.com/kb/)
3. [Documentation officielle de Headscale](https://headscale.net/)
4. [Dépôt GitHub de Headscale](https://github.com/juanfont/headscale)
5. [Site officiel de WireGuard](https://www.wireguard.com/)
6. [Blog de Tailscale - Fonctionnement de Tailscale](https://tailscale.com/blog/how-tailscale-works/)
7. [Architecture à confiance zéro du NIST](https://csrc.nist.gov/publications/detail/sp/800-207/final)
8. [Livre blanc technique de WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
