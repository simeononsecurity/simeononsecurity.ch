---
title: "Guide du débutant : utiliser la ligne de commande Linux pour la cybersécurité"
date: 2023-03-13
lastmod: 2026-11-15
toc: true
draft: false
description: "Apprenez à utiliser la ligne de commande Linux pour la cybersécurité, avec des commandes de base et avancées."
tags: ["Linux", "Ligne de commande", "Cybersécurité", "Guide du débutant", "Analyse réseau", "Test de vulnérabilités", "Analyse de logiciels malveillants", "Permissions", "Trafic réseau", "État des processus", "Statistiques réseau", "Recherche de fichiers", "Wireshark", "TCPDump", "Nmap", "CLI Linux", "Sécurité", "Tests d’intrusion", "Analyse forensique numérique"]
cover: "/img/cover/a-beginners-guide-to-using-the-linux-command-line.webp"
coverAlt: "Illustration d’un écran affichant une ligne de commande Linux en texte vert sur fond sombre, entouré de cadenas numériques et de lignes réseau."
coverCaption: ""
---

**Linux** est un système d’exploitation polyvalent et sécurisé, largement utilisé dans le secteur de la cybersécurité grâce à sa nature open source. Pourtant, utiliser l’interface en ligne de commande de Linux (CLI) pour effectuer des tâches de cybersécurité peut sembler difficile aux débutants. Ce guide présente des commandes Linux de base et avancées utiles en cybersécurité.

## Commandes Linux de base pour la cybersécurité

### Afficher le répertoire de travail

La commande **pwd** (print working directory) affiche le répertoire de travail actuel dans la CLI. Il s’agit du répertoire où vous vous trouvez dans le système de fichiers. Cette commande aide à naviguer et à situer le répertoire courant par rapport aux autres. Par exemple, si vous êtes dans votre répertoire personnel et souhaitez accéder au répertoire des documents, utilisez les commandes suivantes :

```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```

Dans l’exemple ci-dessus, la première commande affiche le répertoire de travail actuel, qui est le répertoire personnel. La deuxième commande passe au répertoire des documents. La troisième affiche le nouveau répertoire de travail.

### Lister le contenu

La commande **ls** affiche le contenu d’un répertoire dans la CLI. Elle indique les noms des fichiers et sous-répertoires du répertoire courant. Elle permet d’identifier les éléments présents dans un emplacement précis. Pour afficher le contenu du répertoire des documents, utilisez la commande suivante :

```bash
$ ls documents
file1.txt file2.pdf file3.docx
```

Dans l’exemple ci-dessus, la commande liste le contenu du répertoire des documents, qui contient trois fichiers : file1.txt, file2.pdf et file3.docx. Vous pouvez aussi exécuter la commande sans argument pour lister le contenu du répertoire courant. Par exemple :

```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```

Dans l’exemple ci-dessus, la commande liste le contenu du répertoire personnel, qui comprend plusieurs sous-répertoires comme Desktop, Documents et Downloads.

### Changer de répertoire

La commande **cd** (change directory) change le répertoire de travail actuel dans la CLI. Elle permet de parcourir le système de fichiers et d’accéder à des fichiers situés ailleurs. Pour passer au répertoire des documents, utilisez la commande suivante :

```bash
$ cd documents
```

Dans l’exemple ci-dessus, la commande passe au répertoire des documents, situé dans le répertoire courant. Vous pouvez aussi utiliser un chemin absolu ou relatif pour accéder à un répertoire qui ne se trouve pas dans le répertoire courant. Par exemple :

```bash
$ cd /usr/local/bin
```

Dans l’exemple ci-dessus, la commande passe au répertoire /usr/local/bin à l’aide d’un chemin absolu. Vous pouvez également utiliser un chemin relatif. Par exemple :

```bash
$ cd ../..
```

Dans l’exemple ci-dessus, la commande remonte de deux niveaux depuis le répertoire courant. La notation ".." désigne le répertoire parent et permet de remonter dans l’arborescence.

### Concaténer des fichiers

La commande **cat** (concatenate) affiche le contenu d’un fichier dans la CLI. Elle sert à consulter des fichiers texte comme les journaux et les fichiers de configuration. Pour afficher le contenu d’un fichier nommé "file1.txt", utilisez la commande suivante :

```bash
$ cat file1.txt
```

Dans l’exemple ci-dessus, la commande affiche le contenu de "file1.txt". Vous pouvez aussi l’utiliser pour concaténer plusieurs fichiers et afficher leur contenu dans la CLI. Par exemple :

```bash
$ cat file1.txt file2.txt file3.txt
```

Dans l’exemple ci-dessus, la commande affiche le contenu de trois fichiers : file1.txt, file2.txt et file3.txt. Vous pouvez aussi utiliser des caractères génériques pour concaténer tous les fichiers correspondant à un motif. Par exemple :

```bash
$ cat *.txt
```

Dans l’exemple ci-dessus, la commande affiche le contenu de tous les fichiers dont l’extension est ".txt" dans le répertoire courant. Elle permet de consulter rapidement plusieurs fichiers sans les ouvrir séparément.

### Rechercher avec des expressions régulières

La commande **grep** (global regular expression print) recherche des chaînes ou des motifs dans un fichier ou un ensemble de fichiers depuis la CLI. Elle permet de repérer des motifs dans des journaux ou de trouver des informations précises dans des fichiers de configuration. Pour rechercher chaque occurrence du mot "error" dans un fichier nommé "logfile.txt", utilisez la commande suivante :

```bash
$ grep "error" logfile.txt
```

Dans l’exemple ci-dessus, la commande recherche chaque occurrence de "error" dans "logfile.txt" et affiche les lignes correspondantes. Vous pouvez aussi employer des expressions régulières pour rechercher des motifs plus complexes. Pour trouver les lignes contenant un mot qui commence par "p" et se termine par "y", utilisez la commande suivante :

```bash
$ grep "p.*y" logfile.txt
```

Dans l’exemple ci-dessus, la commande recherche dans "logfile.txt" les lignes contenant un mot qui commence par "p" et se termine par "y". L’expression régulière "p.*y" correspond à toute chaîne commençant par "p" et finissant par "y", avec un nombre quelconque de caractères entre les deux. Cette commande aide à trouver dans les journaux des motifs susceptibles de révéler des menaces ou des problèmes de performance.

### Modifier les permissions

La commande **chmod** (change mode) modifie les permissions d’un fichier ou d’un répertoire depuis la CLI. Elle est essentielle pour protéger les fichiers et les répertoires et contrôler qui peut y accéder. Trois chiffres représentent respectivement les permissions du propriétaire, du groupe et des autres utilisateurs. Leur valeur suit la formule suivante :

```
4 = lire
2 = écrire
1 = exécuter
```

Par exemple, pour donner au propriétaire les permissions de lecture et d’écriture, et au groupe ainsi qu’aux autres utilisateurs la lecture seule sur "file1.txt", utilisez la commande suivante :

```bash
$ chmod 644 file1.txt
```

Dans l’exemple ci-dessus, la commande définit les permissions de "file1.txt" à 644. Le premier chiffre (6) représente les permissions du propriétaire : lecture et écriture (4 + 2 = 6). Le deuxième chiffre (4) accorde la lecture seule au groupe. Le troisième chiffre (4) accorde aussi la lecture seule aux autres utilisateurs.

Vous pouvez également utiliser des lettres pour changer les permissions. Pour donner au propriétaire et au groupe la lecture et l’écriture, et retirer toutes les permissions aux autres utilisateurs sur "file2.txt", utilisez la commande suivante :

```bash
$ chmod ug=rw,o= file2.txt
```

Dans l’exemple ci-dessus, la commande définit les permissions de "file2.txt" sur ug=rw,o=. "ug" désigne le propriétaire et le groupe, "r" la lecture et "w" l’écriture. Le signe "=" signifie que les permissions sont définies sur les valeurs indiquées. "o=" retire toutes les permissions aux autres utilisateurs. Cette commande aide à contrôler l’accès aux fichiers et répertoires sensibles et à empêcher les accès non autorisés.

## Commandes Linux avancées pour la cybersécurité

{{< figure src="linux-cli-advanced-security-commands-overview.webp" alt="Schéma d’un terminal Linux exécutant nmap, netstat et find pour analyser le réseau, surveiller les processus et rechercher des fichiers en cybersécurité" >}}

### Cartographie réseau

La commande **nmap** est un puissant outil d’analyse réseau en CLI. Elle permet d’identifier les hôtes et les services sur un réseau, ainsi que des vulnérabilités potentielles. Elle propose plusieurs méthodes d’analyse, notamment la découverte d’hôtes, l’analyse de ports et la détection du système d’exploitation.

Une utilisation simple de nmap consiste à analyser une seule adresse IP ou un seul hôte. Pour rechercher les ports ouverts sur l’adresse IP 192.168.1.1, utilisez la commande suivante :

```bash
$ nmap 192.168.1.1
```

La commande ci-dessus lance une analyse TCP SYN sur l’adresse IP cible et renvoie la liste des ports ouverts. Le résultat indique les ports ouverts, le service exécuté sur chacun d’eux et leur état (ouvert ou fermé). Il peut aussi fournir des renseignements supplémentaires, comme le système d’exploitation de la cible.

Nmap peut également analyser plusieurs hôtes ou adresses IP à la fois. Pour rechercher les ports ouverts sur une plage d’adresses IP (192.168.1.1-255), utilisez la commande suivante :

```bash
$ nmap 192.168.1.1-255
```

La commande ci-dessus analyse toutes les adresses IP de la plage et renvoie les ports ouverts et les services de chaque cible.

En plus de découvrir les hôtes et d’analyser les ports, nmap peut détecter les services et leurs versions, identifier les systèmes d’exploitation et rechercher des vulnérabilités. Ces analyses aident à repérer d’éventuelles failles sur un réseau et à le protéger contre les attaques.

### Captureur de paquets TCP

La commande **tcpdump** capture et analyse le trafic réseau depuis la CLI. Elle aide à résoudre des problèmes réseau, à analyser le comportement du réseau et à repérer des menaces potentielles. Elle capture les paquets en temps réel et peut les filtrer selon divers critères, comme l’adresse IP source ou destination, le protocole et le port.

Une utilisation simple de tcpdump consiste à capturer tout le trafic sur une interface donnée. Pour capturer le trafic de l’interface eth0, utilisez la commande suivante :

```bash
$ sudo tcpdump -i eth0
```

La commande ci-dessus capture tous les paquets sur eth0 et les affiche en temps réel dans la CLI. Le résultat indique les adresses IP source et destination, le protocole et d’autres informations sur chaque paquet.

Tcpdump peut aussi filtrer les paquets selon plusieurs critères. Pour capturer tous les paquets envoyés à une adresse IP précise ou provenant de cette adresse, utilisez la commande suivante :

```bash
$ sudo tcpdump host 192.168.1.1
```

La commande ci-dessus capture tous les paquets envoyés à l’adresse IP 192.168.1.1 ou reçus depuis cette adresse et les affiche en temps réel. Vous pouvez également filtrer par protocole (par exemple TCP ou UDP), numéro de port ou autre critère.

Tcpdump peut aussi enregistrer les paquets dans un fichier pour les analyser plus tard. Pour capturer tout le trafic d’eth0 et l’enregistrer dans "capture.pcap", utilisez la commande suivante :

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

La commande ci-dessus capture tous les paquets sur eth0 et les enregistre au format pcap dans "capture.pcap". Vous pourrez les analyser plus tard avec des outils comme Wireshark. Cette commande aide à analyser le comportement du réseau et à repérer des menaces potentielles.

### État des processus

La commande **ps** affiche des informations sur les processus en cours d’exécution sur un système Linux depuis la CLI. Elle aide à repérer les processus suspects qui pourraient compromettre la sécurité du système. Elle peut afficher leur identifiant (PID), l’utilisateur, l’utilisation du processeur et de la mémoire ainsi que le nom de la commande.

Une utilisation simple de ps consiste à afficher la liste de tous les processus en cours. Pour cela, utilisez la commande suivante :

```bash
$ ps aux
```

La commande ci-dessus affiche tous les processus en cours, avec leur PID, leur utilisateur, leur consommation de processeur et de mémoire et le nom de leur commande. Elle donne une vue d’ensemble du système et aide à repérer les processus suspects.

Ps peut aussi afficher les informations d’un processus ou d’un groupe précis. Pour afficher celles d’un processus dont le PID est connu, par exemple 1234, utilisez la commande suivante :

```bash
$ ps -p 1234
```

La commande ci-dessus affiche les informations du processus dont le PID est 1234, notamment son utilisateur, son utilisation du processeur et de la mémoire et le nom de sa commande. Vous pouvez aussi préciser plusieurs PID pour afficher un groupe de processus.

Ps peut également surveiller l’état des processus en temps réel. Pour suivre l’utilisation du processeur et de la mémoire d’un processus, par exemple celui dont le PID est 1234, utilisez la commande suivante :

```bash
$ ps -p 1234 -o %cpu,%mem
```

La commande ci-dessus affiche l’utilisation du processeur et de la mémoire du processus dont le PID est 1234 et actualise le résultat chaque seconde. Elle aide à surveiller les processus essentiels et à repérer d’éventuels goulots d’étranglement.

### Statistiques réseau

La commande **netstat** affiche les connexions réseau actives sur un système Linux depuis la CLI. Elle aide à repérer les connexions non autorisées et les menaces potentielles. Elle peut afficher les adresses locales et distantes, le protocole utilisé (par exemple TCP ou UDP) et l’état de chaque connexion.

Une utilisation simple de netstat consiste à afficher toutes les connexions réseau actives. Utilisez la commande suivante :

```bash
$ netstat -a
```

La commande ci-dessus affiche les connexions réseau actives, avec leurs adresses locales et distantes, leur protocole et leur état. Cette vue d’ensemble aide à repérer les connexions non autorisées.

Netstat peut aussi afficher les connexions d’un protocole précis, comme TCP. Pour afficher les connexions TCP actives, utilisez la commande suivante :

```bash
$ netstat -at
```

La commande ci-dessus affiche les connexions TCP actives ainsi que leurs adresses locales et distantes et leur état.

Netstat peut également afficher les statistiques d’un protocole donné. Pour consulter les statistiques de toutes les connexions TCP, utilisez la commande suivante :

```bash
$ netstat -st
```

La commande ci-dessus affiche les statistiques des connexions TCP, notamment le nombre de connexions actives, le nombre de connexions dans chaque état et le nombre d’erreurs. Elle aide à surveiller l’état général du réseau et à repérer des problèmes de performance.

### Rechercher des fichiers

La commande **find** recherche des fichiers et des répertoires sur un système Linux depuis la CLI. Elle aide à localiser des éléments cachés ou difficiles à trouver. Elle peut effectuer une recherche selon plusieurs critères, notamment le nom, la taille, la date de modification et les permissions.

Une utilisation simple de find consiste à rechercher des fichiers par leur nom. Pour trouver tous les fichiers nommés "example.txt" dans le répertoire courant et ses sous-répertoires, utilisez la commande suivante :

```bash
$ find . -name example.txt
```

La commande ci-dessus recherche les fichiers nommés "example.txt" dans le répertoire courant et ses sous-répertoires, puis affiche leur chemin complet.

Find peut aussi rechercher selon la taille. Pour trouver les fichiers de plus de 1 Mo dans le répertoire courant et ses sous-répertoires, utilisez la commande suivante :

```bash
$ find . -size +1M
```

La commande ci-dessus recherche les fichiers de plus de 1 Mo dans le répertoire courant et ses sous-répertoires, puis affiche leur chemin complet.

En plus du nom et de la taille, find peut rechercher selon la date de modification et les permissions. Pour trouver les fichiers modifiés au cours des sept derniers jours, utilisez la commande suivante :

```bash
$ find . -mtime -7
```

La commande ci-dessus recherche les fichiers modifiés au cours des sept derniers jours dans le répertoire courant et ses sous-répertoires, puis affiche leur chemin complet.

La commande find est un outil puissant qui recherche des fichiers et des répertoires selon de nombreux critères. Elle est utile pour l’administration système et la cybersécurité.

______

Utiliser la ligne de commande Linux pour la cybersécurité peut sembler intimidant aux débutants. Les commandes de base et avancées de ce guide vous aideront à tirer parti de la CLI. Soyez prudent lorsque vous exécutez une commande et comprenez son fonctionnement avant de l’utiliser.

Pour en savoir plus sur Linux en cybersécurité, téléchargez le système d’exploitation **[Kali Linux](https://www.kali.org/downloads/)**, conçu pour les tests d’intrusion et l’analyse forensique numérique.

## Conclusion

L’interface en ligne de commande de Linux est un outil puissant pour les professionnels de la cybersécurité, mais elle peut sembler difficile aux débutants. En apprenant les commandes de base et avancées de ce guide, vous pourrez tirer parti de la CLI. Soyez toujours prudent et comprenez chaque commande avant de l’exécuter. Avec de la pratique et de l’expérience, vous maîtriserez la ligne de commande Linux et développerez vos compétences en cybersécurité.
