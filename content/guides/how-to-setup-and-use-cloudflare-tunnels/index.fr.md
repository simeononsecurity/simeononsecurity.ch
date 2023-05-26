---
title: "Configuration des tunnels Cloudflare : Rationaliser et sécuriser votre trafic réseau"
draft: false
toc: true
date: 2023-05-26
description: "Apprenez à configurer les tunnels Cloudflare pour rationaliser et protéger votre trafic réseau, en améliorant les performances et la sécurité."
tags: ["Tunnels Cloudflare", "Sécurité des réseaux", "Performance du site web", "Serveur Proxy", "Trafic web", "Configuration du réseau", "Serveur Ubuntu", "Compte Cloudflare", "Authentification", "Création d'un tunnel", "Acheminement du trafic", "Enregistrements DNS", "Connexion sécurisée", "Hébergement de sites web", "Service Proxy", "Protection du réseau", "Optimisation des performances", "Intégration de Cloudflare", "Configuration du serveur", "Chiffrement du trafic", "Gestion du trafic sur le réseau", "Hébergement Web sécurisé", "Sécurité du site web", "Installation d'Ubuntu", "Technologie des tunnels", "Services Cloudflare", "Performance du réseau", "Web Security", "Sécurité du serveur", "Gestion du trafic", "Proxy Cloudflare"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "Illustration d'un tunnel réseau reliant un serveur local au logo Cloudflare, symbolisant la sécurité et la rationalisation du trafic réseau."
coverCaption: ""
---

**Guide de configuration des tunnels Cloudflare

## Introduction
Les tunnels Cloudflare constituent un moyen sûr d'héberger des sites web en établissant une connexion directe entre votre réseau local et Cloudflare. Ce guide vous aidera à configurer les tunnels Cloudflare afin d'améliorer la sécurité et les performances de votre site web.

______

## Pourquoi les tunnels Cloudflare ?
Les tunnels Cloudflare offrent plusieurs avantages, notamment la réduction des vecteurs d'attaque et la simplification des configurations réseau. En utilisant Cloudflare comme proxy, vous pouvez fermer les ports externes et vous assurer que tout le trafic passe par le réseau sécurisé de Cloudflare. Cela fournit une couche supplémentaire de protection pour votre site web.

______

## Conditions préalables
Avant de configurer les tunnels Cloudflare, assurez-vous que vous disposez des éléments suivants :

1. Un compte Cloudflare actif.
2. Un serveur fonctionnant sous Ubuntu.

______

## Étape 1 : Installation
Pour commencer, vous devez installer le paquetage Cloudflare Tunnels sur votre serveur Ubuntu. Suivez les étapes suivantes :

1. Ouvrez le terminal sur votre serveur Ubuntu.
2. Téléchargez la dernière version du paquetage Cloudflare Tunnels en exécutant la commande suivante :

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Étape 2 : Authentification
Ensuite, vous devez authentifier votre compte Cloudflare avec le service Tunnels Cloudflare. Suivez les étapes suivantes :

1. Exécutez la commande suivante dans le terminal :

```shell
cloudflared tunnel login
```

2. Cliquez sur le site que vous souhaitez utiliser avec votre tunnel pour terminer la procédure d'authentification.

## Étape 3 : Création d'un tunnel

Il est maintenant temps de créer votre tunnel Cloudflare. Suivez les étapes suivantes :

1. Exécutez la commande suivante dans le terminal pour créer un tunnel :

```shell
cloudflared tunnel create name_of_tunnel
```

2. Choisissez un nom mémorable et descriptif pour votre tunnel. Notez que le nom du tunnel ne peut pas être modifié ultérieurement.

3. après avoir créé le tunnel, vous recevrez des informations importantes, y compris l'UUID de votre tunnel. Notez cet UUID car il sera nécessaire pour la suite de la configuration.

4. Pour afficher une liste de tous les tunnels actifs, utilisez la commande :

```shell
cloudflared tunnel list
```

Ceci affichera les noms et UUIDs de vos tunnels.

### Étape 4 : Configuration du tunnel

Pour configurer votre tunnel et commencer à acheminer le trafic, suivez les étapes suivantes :

1. Naviguez jusqu'au répertoire Cloudflare Tunnels sur votre serveur. L'emplacement par défaut est `/etc/cloudflared`

2. Dans ce répertoire, créez un nouveau fichier nommé `config.yml` en utilisant l'éditeur de texte de votre choix.

3. Remplissez le fichier config.yml avec le contenu suivant :

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Veillez à remplacer `<your_tunnels_uuid>` avec l'UUID de votre tunnel, et mettez à jour le chemin d'accès au fichier d'informations d'identification si nécessaire.

## Étape 5 : Routage du trafic

Pour spécifier les services internes que vous voulez servir à travers votre tunnel, suivez ces étapes :

1. `Open the ` à nouveau.

2. Ajoutez les paramètres d'entrée au fichier pour définir les services que vous souhaitez acheminer via Cloudflare. Par exemple :

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

Remplacer `<your_tunnels_uuid>` avec l'UUID de votre tunnel, et mettez à jour le nom d'hôte et les détails du service en fonction de votre configuration.

3. Enregistrez le fichier config.yml.


## Étape 6 : Création des enregistrements DNS

Pour créer des enregistrements DNS pour le nom d'hôte et les services de votre tunnel, suivez ces étapes :

1. Ouvrez le terminal.

2. Utilisez la commande suivante pour créer un enregistrement DNS :

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Remplacer `<UUID or NAME of tunnel>` avec l'UUID ou le nom de votre tunnel, et `<hostname>` avec le nom d'hôte souhaité pour votre service.

3. Par exemple, pour créer un enregistrement DNS pour exemple.com, exécutez la commande :

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Veuillez noter que les changements seront reflétés dans la section DNS de votre tableau de bord Cloudflare.

## Étape 7 : Démarrer le tunnel

Pour tester et démarrer votre tunnel Cloudflare, suivez les étapes suivantes :

1. Ouvrez le terminal.

2. Exécutez la commande suivante pour démarrer le tunnel :

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Remplacer `<UUID or NAME of tunnel>` avec l'UUID ou le nom de votre tunnel.

3. Cloudflared va maintenant configurer votre tunnel et afficher des informations sur son état. Une fois que le tunnel est opérationnel, vous pouvez passer à l'étape suivante.

4. Pour éviter que le tunnel ne se ferme lorsque vous quittez le terminal, vous devez exécuter Cloudflared en tant que service systemd. Utilisez la commande suivante :

```shell
cloudflared --config /path/to/config.yml service install
```

Remplacer `/path/to/config.yml` avec le chemin d'accès à votre `config.yml` fichier.

## Conclusion

Dans ce guide, nous avons couvert les étapes de la mise en place des tunnels Cloudflare sur Ubuntu. En suivant ces instructions, vous pouvez améliorer la sécurité et les performances de votre site web en tirant parti du réseau de Cloudflare. N'oubliez pas de surveiller régulièrement vos tunnels et d'ajuster la configuration si nécessaire.

Si vous rencontrez des problèmes ou si vous avez besoin d'une assistance supplémentaire, reportez-vous à la section [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## Références
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)