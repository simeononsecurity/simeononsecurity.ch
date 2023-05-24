---
title: "Guide ultime : mises à jour Linux hors ligne pour Ubuntu Debian et CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Mises à jour Linux", "Ubuntu", "DebianName", "CentOS", "RHEL", "mises à jour hors ligne", "référentiel local", "cache", "configuration du serveur", "configuration du client", "apt-miroir", "debmirror", "créer un dépôt", "apt-cacher-ng", "miam-cron", "Mises à jour du système Linux", "mises à jour de packages hors ligne", "mises à jour logicielles hors ligne", "référentiel de packages local", "cache de paquets locaux", "mises à jour Linux hors ligne", "gestion des mises à jour hors ligne", "méthodes de mise à jour hors ligne", "maintenance du système hors ligne", "Mises à jour du serveur Linux", "Mises à jour des clients Linux", "gestion des logiciels hors ligne", "gestion hors ligne des packages", "mettre à jour les stratégies", "Mises à jour de sécurité Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Une illustration de dessin animé représentant un serveur et plusieurs appareils clients échangeant des mises à jour hors ligne."
coverCaption: ""
---

**Meilleures façons de gérer l'installation des mises à jour Linux hors ligne pour Ubuntu/Debian et CentOS/RHEL**

Les mises à jour Linux sont essentielles pour maintenir la sécurité et la stabilité de votre système. Cependant, dans certains scénarios, vous devrez peut-être gérer des environnements hors ligne où la connectivité Internet est limitée ou inexistante. Dans de tels cas, il devient crucial de mettre en place une stratégie appropriée pour installer les mises à jour hors ligne. Cet article vous guidera à travers les ** meilleures façons de gérer l'installation des mises à jour Linux pour Ubuntu/Debian et CentOS/RHEL ** dans des environnements hors ligne, en se concentrant spécifiquement sur l'utilisation d'un référentiel ou d'un cache local.

## Configuration d'un référentiel local

L'un des moyens les plus efficaces de gérer les mises à jour hors ligne consiste à configurer un référentiel local. Un référentiel local contient tous les progiciels et mises à jour nécessaires, vous permettant de mettre à jour votre système sans connexion Internet. Voici comment configurer un référentiel local pour les distributions basées sur Debian et Red Hat :

### Pour Debian/Ubuntu

1. Commencez par configurer un **miroir de référentiel Debian** sur un serveur disposant d'un accès Internet. Vous pouvez utiliser des outils comme [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) pour créer un miroir local des dépôts officiels Debian ou Ubuntu.

#### Configurer un miroir de dépôt Debian avec apt-mirror :

```shell
# Install apt-mirror
sudo apt-get install apt-mirror

# Edit the apt-mirror configuration file
sudo nano /etc/apt/mirror.list

# Uncomment the deb line for the desired repository
# For example, uncomment the line for Ubuntu 20.04:
# deb http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse

# Specify the mirror location
# Modify the base_path to your desired location
set base_path /path/to/mirror

# Save and close the file

# Run apt-mirror to start the mirroring process
sudo apt-mirror

# Wait for the mirroring process to complete
```

#### Configurer un miroir de dépôt Debian avec debmirror :
```shell
# Install debmirror
sudo apt-get install debmirror

# Create a directory to store the mirror
sudo mkdir /path/to/mirror

# Run debmirror to start the mirroring process
# Replace <RELEASE> with the Debian or Ubuntu release and <MIRROR_URL> with the official repository URL
# For example, to mirror Ubuntu 20.04:
sudo debmirror --arch=amd64 --verbose --method=http --dist=<RELEASE> --root=<MIRROR_URL> /path/to/mirror

# Wait for the mirroring process to complete
```
#### Instructions du client Debian

2. Configurez votre référentiel local en modifiant le **`/etc/apt/sources.list` fichier sur le système hors ligne. Remplacez les URL de référentiel par défaut par l'URL de référentiel local. Par exemple, si votre référentiel local est hébergé sur `http://local-repo/ubuntu` mettre à jour le `sources.list` déposer en conséquence.

Exemple `/etc/apt/sources.list` déposer:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Une fois la configuration mise à jour, vous pouvez exécuter le **`apt update` sur le système hors ligne pour récupérer les listes de packages à partir du référentiel local.

```shell
sudo apt update
```

4. Enfin, vous pouvez utiliser le **`apt upgrade` commande pour installer les mises à jour disponibles à partir du référentiel local.

```shell
sudo apt upgrade
```

### Pour CentOS/RHEL

1. Pour configurer un référentiel local pour CentOS/RHEL, vous devez utiliser le [**`createrepo`**](https://linux.die.net/man/8/createrepo) outil. Cet outil crée les métadonnées nécessaires pour un référentiel local.

2. Créez un répertoire pour stocker les fichiers du référentiel sur un serveur avec accès à Internet. Par exemple, vous pouvez créer un répertoire appelé **`local-repo`

3. Copiez tous les fichiers de package RPM pertinents et les mises à jour vers le **`local-repo` annuaire.

#### Configuration d'un référentiel local avec createrepo :

```shell
# Install the createrepo tool
sudo yum install createrepo

# Create a directory to store the repository files
sudo mkdir /path/to/local-repo

# Move or copy the RPM package files and updates to the local-repo directory

# Run the createrepo command to generate the necessary repository metadata
sudo createrepo /path/to/local-repo

# Update the repository metadata whenever new packages are added or removed
sudo createrepo --update /path/to/local-repo
```
4. Une fois les métadonnées du référentiel générées, vous pouvez transférer `local-repo` répertoire au système hors ligne à l'aide d'une clé USB ou de tout autre moyen.

5. Sur le système hors ligne, créez un nouveau `.repo` dossier dans le `/etc/yum.repos.d/` annuaire. Fournissez les détails de configuration nécessaires, tels que le `baseurl` pointant vers le répertoire du référentiel local.

Par exemple, créez un fichier appelé `local.repo` dans le `/etc/yum.repos.d/` répertoire et ajoutez le contenu suivant :
```shell
sudo nano /etc/yum.repos.d/local.repo
```
```toml
[local]
name=Local Repository
baseurl=file:///path/to/local-repo
enabled=1
gpgcheck=0
```
6. Enregistrez le fichier et quittez l'éditeur.

7. Après avoir configuré le référentiel, vous pouvez utiliser la commande yum update pour installer les mises à jour à partir du référentiel local.

```shell
sudo yum update
```

Cette commande mettra à jour les packages sur le système en utilisant les packages du référentiel local.

N'oubliez pas de mettre à jour le référentiel local en exécutant le `createrepo` commande chaque fois que de nouveaux packages sont ajoutés ou supprimés du référentiel.

Veuillez noter que vous devrez remplacer `/path/to/local-repo` avec le chemin d'accès réel au répertoire où vous avez stocké les fichiers du référentiel.

## Configuration d'un cache local

Une autre approche pour gérer les mises à jour hors ligne consiste à configurer un cache local. Un cache local stocke les packages et les mises à jour téléchargés, vous permettant de les distribuer sur plusieurs systèmes sans avoir besoin de téléchargements individuels. Vous devez configurer ce cache sur un système en ligne, puis déplacer le répertoire vers un système hors ligne pour permettre à d'autres systèmes d'accéder aux packages. Voici comment configurer un cache local pour les distributions basées sur Debian et Red Hat :

### Pour Debian/Ubuntu

1. Installer et configurer [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) un proxy de mise en cache pour les packages Debian/Ubuntu. Vous pouvez l'installer en exécutant la commande **`sudo apt-get install apt-cacher-ng`

2. Une fois installé, modifiez le **`/etc/apt-cacher-ng/acng.conf` fichier pour configurer le comportement de mise en cache. Assurez-vous que le **`PassThroughPattern` Le paramètre inclut les URL de référentiel nécessaires.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Décommentez ou ajoutez les URL de référentiel nécessaires au paramètre PassThroughPattern. Par exemple, pour inclure les référentiels Ubuntu, ajoutez ou décommentez la ligne suivante :
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Enregistrez le fichier et quittez l'éditeur.

3. Démarrez le [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) service à l'aide de la commande **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. Sur les systèmes hors ligne, configurez le **`/etc/apt/apt.conf.d/02proxy` fichier pour pointer vers le cache local. Utilisez la ligne suivante : **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Ajoutez la ligne suivante au fichier, en remplaçant <cache-server-ip> par l'adresse IP du serveur de cache :
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Enregistrez le fichier et quittez l'éditeur

5. Maintenant, lorsque vous exécutez le **`apt update` et **`apt upgrade` commandes sur les systèmes hors ligne, ils récupéreront les packages à partir du cache local.

```shell
sudo apt update
sudo apt upgrade
```
Ces commandes récupèrent et installent les mises à jour à partir du cache local, réduisant ainsi le besoin d'accès à Internet sur les systèmes hors ligne.

Veuillez noter que vous devrez remplacer **`<cache-server-ip>` avec l'adresse IP réelle de la machine sur laquelle **apt-cacher-ng** est installé.

### Pour CentOS/RHEL

1. Pour CentOS/RHEL, vous pouvez utiliser [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) pour configurer un cache local. Installez-le en exécutant la commande **`sudo yum install yum-cron`

2. Modifiez le **`/etc/yum/yum-cron.conf` fichier et configurez le **`download_only` paramètre à **`yes` Cela garantit que les packages sont uniquement téléchargés et non installés automatiquement.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Démarrez le [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) service à l'aide de la commande **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. Sur les systèmes hors ligne, créez un répertoire local pour stocker les packages téléchargés, par exemple, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Copiez les packages téléchargés du système en ligne vers le répertoire de cache local.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Remplacer `/path/to/local/cache` avec le chemin d'accès au répertoire de cache local sur le système hors ligne.

6. Sur les systèmes hors ligne, créez un nouveau **`.repo` déposer dans le **`/etc/yum.repos.d/` répertoire, pointant vers le répertoire de cache local.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Ajoutez le contenu suivant au fichier, en remplaçant `<local-cache-path>` avec le chemin vers le répertoire du cache local :
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Enregistrez le fichier et quittez l'éditeur.

7. Enfin, vous pouvez utiliser le **`yum update` sur les systèmes hors ligne pour installer les mises à jour à partir du cache local.

```shell
sudo yum update
```

Cette commande mettra à jour les packages sur les systèmes hors ligne en utilisant les packages du cache local.

Veuillez noter que vous devrez remplacer **`<local-cache-path>` avec le chemin d'accès réel au répertoire de cache local sur le système hors ligne.

______

## Conclusion

La gestion des mises à jour Linux dans des environnements hors ligne peut être difficile, mais avec la bonne approche, vous pouvez vous assurer que vos systèmes restent à jour et sécurisés. Dans cet article, nous avons discuté des meilleures façons de gérer l'installation des mises à jour hors ligne pour Ubuntu/Debian et CentOS/RHEL. Nous avons exploré la configuration d'un référentiel local et la configuration d'un cache local, en fournissant des instructions étape par étape pour les distributions basées sur Debian et Red Hat.

En suivant ces méthodes, vous pouvez maintenir la sécurité et la stabilité de vos systèmes Linux, même dans des environnements hors ligne. N'oubliez pas de mettre à jour périodiquement votre référentiel local ou votre cache pour inclure les dernières mises à jour.

______

## Les références

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
