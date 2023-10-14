---
title: "Ce qu'il faut faire et ne pas faire pour durcir votre système Linux"
date: 2023-02-28
toc: true
draft: false
description: "Apprenez les choses essentielles à faire et à ne pas faire pour renforcer votre système Linux, y compris la mise à jour, l'utilisation de pare-feu, l'activation de SELinux ou AppArmor, la configuration de politiques de mot de passe et la surveillance des journaux du système."
tags: ["Linux security", "durcissement du système", "pare-feu", "SELinux", "AppArmor", "politique en matière de mot de passe", "mises à jour du système", "journaux du système", "modules de sécurité", "les politiques de contrôle d'accès", "cybersécurité", "sécurité du système", "sécurité des réseaux", "gestion de la vulnérabilité", "meilleures pratiques en matière de sécurité", "Sécurité informatique", "la sécurité de l'information", "mises à jour du logiciel", "accès à la racine", "gestionnaire de mot de passe"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Un cadenas de dessin animé tient un bouclier sur lequel figure le mot Linux, tandis qu'une flèche rebondit sur le bouclier."
coverCaption: ""
---


Linux est un système d'exploitation populaire utilisé aussi bien par les particuliers que par les entreprises. Bien qu'il soit souvent considéré comme plus sûr que d'autres systèmes d'exploitation en raison de sa nature open-source, il nécessite néanmoins un durcissement approprié pour garantir la sécurité du système et des données qu'il contient. Dans cet article, nous allons passer en revue les choses à faire et à ne pas faire pour renforcer la sécurité de votre système Linux.

## A faire :

### Maintenir votre système à jour

Maintenir votre [Linux](https://simeononsecurity.com/articles/how-do-i-learn-linux/) La mise à jour du système est essentielle au maintien de sa sécurité. Des mises à jour régulières permettent de corriger les failles de sécurité et les bogues, garantissant ainsi la sécurité de votre système contre les attaques potentielles. Voici quelques exemples de mise à jour de votre système Linux à l'aide du gestionnaire de paquets **apt-get** ou **yum** :

#### Mise à jour d'Ubuntu à l'aide d'apt-get

Pour mettre à jour votre système Ubuntu à l'aide de **apt-get**, ouvrez une fenêtre de terminal et tapez :
```bash
sudo apt-get update
```

Cette commande téléchargera les dernières listes de paquets depuis les dépôts de paquets d'Ubuntu. Une fois cette commande terminée, vous pouvez installer toutes les mises à jour disponibles à l'aide de la commande suivante :

```bash
sudo apt-get upgrade

```

Cette opération permet de télécharger et d'installer toutes les mises à jour disponibles pour votre système.

### Mise à jour de CentOS avec yum

Pour mettre à jour votre système CentOS en utilisant **yum**, ouvrez une fenêtre de terminal et tapez :

```bash
sudo yum update
```

Cette commande téléchargera et installera toutes les mises à jour disponibles pour votre système. Vous pouvez également utiliser la commande suivante pour nettoyer les paquets anciens ou inutilisés :

```bash
sudo yum autoremove
```

Cela supprimera tous les paquets qui ne sont plus nécessaires sur votre système.

N'oubliez pas de vérifier et d'installer régulièrement les mises à jour sur votre système Linux afin de garantir sa sécurité et sa stabilité.


### Utiliser un pare-feu

Un pare-feu est une mesure de sécurité essentielle pour tout système Linux, car il permet de se protéger contre les accès non autorisés et d'autres cybermenaces. Voici comment utiliser le pare-feu **ufw** sur votre système Linux :

#### Installation et activation de ufw pour les systèmes basés sur Ubuntu

Pour installer et activer **ufw**, ouvrez une fenêtre de terminal et tapez :

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Pour autoriser le trafic HTTP entrant (port 80) :

```bash
sudo ufw allow http
```

Pour bloquer le trafic entrant en provenance d'une adresse IP spécifique :

```bash
sudo ufw deny from <ip_address>
```

Pour supprimer une règle :
```bash
sudo ufw delete <rule_number>
```

Vous pouvez afficher les règles **ufw** actuelles en tapant :

```bash
sudo ufw status
```


Les règles en vigueur et leur statut s'affichent.

N'oubliez pas de revoir et de mettre à jour régulièrement vos règles **ufw** pour vous assurer que votre système est protégé contre les menaces potentielles.


#### Installation et activation de firewalld pour les systèmes basés sur CentOS

Pour installer et activer le pare-feu par défaut sur CentOS, qui est **firewalld**, vous pouvez utiliser les commandes suivantes :

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Ceci installera **firewalld** et l'activera sur votre système.

#### Configuration des règles firewalld pour les systèmes basés sur CentOS

Une fois **firewalld** activé, vous pouvez configurer ses règles pour autoriser ou bloquer le trafic entrant et sortant. Voici quelques exemples :

Pour autoriser le trafic SSH entrant (port 22) :

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Pour autoriser le trafic HTTP entrant (port 80) :

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Pour bloquer le trafic entrant en provenance d'une adresse IP spécifique :

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

Pour supprimer une règle :

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

Vous pouvez afficher les règles **firewalld** actuelles en tapant :

```bash
sudo firewall-cmd --list-all
```

Les règles en vigueur et leur statut s'affichent.

N'oubliez pas de revoir et de mettre à jour régulièrement vos règles **firewalld** afin de vous assurer que votre système

### Activer SELinux ou AppArmor

SELinux (Security-Enhanced Linux) et AppArmor sont deux modules de sécurité qui peuvent être utilisés pour appliquer des politiques de contrôle d'accès obligatoires dans les systèmes Linux. Par défaut, la plupart des distributions Linux modernes sont équipées de SELinux ou d'AppArmor, qui peuvent être activés et configurés pour renforcer la sécurité de votre système.

#### Activation de SELinux pour les systèmes basés sur CentOS

Pour vérifier si SELinux est activé sur votre système, exécutez la commande suivante :

```bash
sestatus
```

Si SELinux n'est pas installé, vous pouvez l'installer à l'aide de la commande suivante :

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Pour activer SELinux, vous devez éditer le fichier **/etc/selinux/config** et définir la variable **SELINUX** sur **enforcing** :

```bash
sudo nano /etc/selinux/config
```
**Changez SELINUX=renforçant**
```
SELINUX=enforcing
```

Enregistrez et quittez le fichier en utilisant les touches CTRL+X et Y, puis entrez, et redémarrez votre système.

#### Activation d'AppArmor pour les systèmes basés sur Ubuntu

Pour vérifier si AppArmor est activé sur votre système, exécutez la commande suivante :
```bash
sudo apparmor_status
```


Si AppArmor n'est pas installé, vous pouvez l'installer à l'aide de la commande suivante :
```bash
sudo apt-get install apparmor
```

Pour activer AppArmor, vous devez éditer le fichier **/etc/default/grub** et ajouter le paramètre **security=apparmor** à la variable **GRUB_CMDLINE_LINUX** :

```bash
sudo nano /etc/default/grub
```
**Ajouter la sécurité=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Enregistrez et quittez le fichier en utilisant les touches CTRL+X et Y, puis entrez, et exécutez la commande suivante pour mettre à jour la configuration du chargeur de démarrage de votre système :

```bash
sudo update-grub
```

Enfin, redémarrez votre système.

Une fois SELinux ou AppArmor activé, vous pouvez configurer leurs stratégies pour restreindre les privilèges des processus et limiter leur accès aux ressources du système. Cela permet de minimiser l'impact potentiel d'une attaque réussie et de renforcer la sécurité globale de votre système.


### Configurer les stratégies de mot de passe

La configuration des stratégies de mot de passe est une étape importante dans le renforcement de la sécurité de votre système Linux. En imposant des exigences strictes en matière de mot de passe, vous pouvez vous assurer que les comptes utilisateurs sont sécurisés et protégés contre les attaques potentielles. Voici comment configurer les stratégies de mot de passe sur votre système Linux :

#### Configuration des politiques de mot de passe sur Ubuntu

Pour configurer les politiques de mot de passe sur Ubuntu, vous pouvez utiliser le module **pam_pwquality**. Ce module fournit un ensemble de vérifications de la force des mots de passe qui peuvent être utilisées pour appliquer les politiques de mot de passe. Pour installer le module **pam_pwquality**, ouvrez une fenêtre de terminal et tapez :

```bash
sudo apt-get install libpam-pwquality
```

Une fois le module installé, vous pouvez configurer ses paramètres en modifiant le fichier **/etc/pam.d/common-password**. Par exemple, pour imposer un mot de passe d'une longueur minimale de 8 caractères et exiger au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial, vous pouvez ajouter la ligne suivante au fichier :

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

Vous pouvez également configurer d'autres paramètres, tels que l'âge maximal du mot de passe, en ajoutant des lignes au fichier.

#### Configurer les politiques de mot de passe sur CentOS

Pour configurer les politiques de mot de passe sous CentOS, vous pouvez utiliser l'outil **authconfig**. Cet outil fournit un ensemble d'options qui peuvent être utilisées pour configurer les politiques de mot de passe. Par exemple, pour imposer un mot de passe d'une longueur minimale de 8 caractères et exiger au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial, vous pouvez utiliser la commande suivante :

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Cette opération met à jour les fichiers **/etc/pam.d/system-auth** et **/etc/pam.d/password-auth** du système afin d'appliquer les stratégies de mot de passe spécifiées.

N'oubliez pas de revoir et de mettre à jour régulièrement vos stratégies de mot de passe afin de vous assurer qu'elles restent efficaces contre les attaques potentielles.


### Surveillez les journaux de votre système

La surveillance des journaux système est un aspect important du maintien de la sécurité de votre système Linux. Les journaux système enregistrent l'activité du système, telle que les tentatives de connexion échouées, les erreurs et d'autres événements importants, et peuvent fournir des informations précieuses sur les menaces de sécurité potentielles ou d'autres problèmes nécessitant une attention particulière. Voici comment surveiller vos journaux système :

#### Utilisation de la commande journalctl

Sur la plupart des distributions Linux modernes, vous pouvez utiliser la commande **journalctl** pour afficher les journaux du système. Cette commande propose une série d'options qui peuvent être utilisées pour filtrer et rechercher des entrées dans les journaux.

Pour afficher toutes les entrées du journal, il suffit d'exécuter la commande suivante :

```bash
sudo journalctl
```

Cela permet d'afficher toutes les entrées du journal, les entrées les plus récentes se trouvant en bas de page.

Pour filtrer les entrées de journal par unité spécifique, telle qu'un service ou un processus, vous pouvez utiliser l'option **-u** suivie du nom de l'unité. Par exemple, pour afficher les entrées de journal du service **sshd**, vous pouvez exécuter la commande suivante :
```bash
sudo journalctl -u sshd
```


Pour filtrer les entrées du journal en fonction d'une période spécifique, vous pouvez utiliser les options **--since** et **--until** suivies d'un horodatage ou d'une période. Par exemple, pour afficher les entrées de journal de la dernière heure, vous pouvez exécuter la commande suivante :

```bash
sudo journalctl --since "1 hour ago"
```

#### Utilisation d'un outil de gestion des journaux

Pour les systèmes plus importants ou plus complexes, il peut être utile d'utiliser un outil de gestion des journaux pour collecter et analyser les journaux du système. Les outils de gestion des journaux peuvent offrir des fonctions avancées, telles que la surveillance en temps réel, l'agrégation et l'analyse des journaux, et peuvent vous aider à identifier les menaces potentielles à la sécurité et à y répondre plus efficacement.

Voici quelques exemples d'outils de gestion de journaux pour Linux :

- **Logwatch** : un outil simple d'analyse des journaux qui fournit des résumés quotidiens par courrier électronique des journaux du système.
- Logrotate** : un outil qui effectue automatiquement la rotation et la compression des fichiers journaux pour économiser de l'espace disque.
- ELK stack** : un outil de gestion de journaux open-source populaire qui combine Elasticsearch, Logstash et Kibana pour fournir des capacités de surveillance et d'analyse des journaux en temps réel.

N'oubliez pas d'examiner et d'analyser régulièrement les journaux de votre système afin de détecter les menaces de sécurité potentielles et d'y répondre à temps.

______

## À ne pas faire :

### Utiliser des mots de passe faibles

L'utilisation de mots de passe faibles est une erreur courante qui peut rendre votre système Linux vulnérable aux attaques. Les attaquants peuvent utiliser des outils pour deviner les mots de passe basés sur des mots, des noms ou des dates courants. Il est important d'utiliser des mots de passe forts et uniques qui ne sont pas facilement devinables.

Vous pouvez créer des mots de passe forts en utilisant une combinaison de lettres majuscules et minuscules, de chiffres et de caractères spéciaux. Il est également conseillé d'utiliser un [password manager](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) peut également vous aider à mémoriser vos mots de passe et à éviter d'utiliser le même mot de passe pour plusieurs comptes.

### Autoriser l'accès SSH à la racine

Autoriser l'accès SSH à la racine est un risque de sécurité qui peut donner aux attaquants un contrôle total sur votre système Linux. Vous devriez plutôt utiliser un compte utilisateur non root pour vous connecter à votre système, puis élever les privilèges à l'aide de la commande **sudo**. Cela permet de limiter l'impact potentiel d'une attaque en restreignant les privilèges des comptes d'utilisateurs.

### Installer des logiciels inutiles

L'installation de logiciels inutiles peut augmenter la surface d'attaque de votre système Linux et le rendre plus vulnérable aux attaques. Il est important de n'installer que les logiciels nécessaires à votre système et de supprimer tous les logiciels inutiles. Cela permet de réduire le nombre de vulnérabilités potentielles sur votre système et de minimiser le risque d'une attaque réussie.

### Utiliser des logiciels obsolètes

L'utilisation de logiciels obsolètes peut rendre votre système vulnérable à des attaques exploitant des vulnérabilités connues. Il est important de toujours utiliser la dernière version d'un logiciel et de la mettre à jour régulièrement pour garantir la sécurité. Cela permet de corriger les vulnérabilités connues et de protéger votre système contre les attaques potentielles.

______

## Conclusion

En conclusion, le durcissement de votre système Linux est essentiel pour garantir sa sécurité et protéger les données qu'il contient. En suivant les conseils de cet article, vous pouvez prendre des mesures importantes pour sécuriser votre système et réduire le risque de cybermenaces. N'oubliez pas de toujours tenir votre système à jour, d'utiliser un pare-feu, de configurer des politiques de mot de passe et de surveiller les journaux du système. Évitez d'utiliser des mots de passe faibles, de désactiver les mises à jour automatiques, d'autoriser l'accès SSH à la racine, d'installer des logiciels inutiles et d'utiliser des logiciels obsolètes. En gardant ces bonnes pratiques à l'esprit, vous pouvez vous assurer que votre système Linux reste sécurisé et protégé.

## Références :

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)
