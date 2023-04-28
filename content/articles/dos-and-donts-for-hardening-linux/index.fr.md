---
title: "Essential Do's and Don'ts for Hardening Your Linux System"
date: 2023-02-28
toc: true
draft: false
description: "Learn the essential dos and donts for hardening your Linux system, including updating, using firewalls, enabling SELinux or AppArmor, configuring password policies, and monitoring system logs."
tags: ["Linux security", "system hardening", "firewall", "SELinux", "AppArmor", "password policy", "system updates", "system logs", "security modules", "access control policies", "cybersecurity", "system security", "network security", "vulnerability management", "security best practices", "IT security", "information security", "software updates", "root access", "password manager"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "A cartoon lock holding a shield with the word Linux on it, while an arrow bounces off the shield."
coverCaption: ""
---
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade

```
```bash
sudo yum update
```
```bash
sudo yum autoremove
```
```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```
```bash
sudo ufw allow http
```
```bash
sudo ufw deny from <ip_address>
```
```bash
sudo ufw delete <rule_number>
```
```bash
sudo ufw status
```
```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```
```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --list-all
```
```bash
sestatus
```
```bash
sudo yum install selinux-policy selinux-policy-targeted
```
```bash
sudo nano /etc/selinux/config
```
```
SELINUX=enforcing
```
```bash
sudo apparmor_status
```
```bash
sudo apt-get install apparmor
```
```bash
sudo nano /etc/default/grub
```
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```
```bash
sudo update-grub
```
```bash
sudo apt-get install libpam-pwquality
```
```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```
```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```
```bash
sudo journalctl
```
```bash
sudo journalctl -u sshd
```
```bash
sudo journalctl --since "1 hour ago"
```

  Linux est un système d'exploitation populaire utilisé par les particuliers et les entreprises. Bien qu'il soit souvent considéré comme plus sûr que d'autres systèmes d'exploitation en raison de sa nature open source, il nécessite toujours un renforcement approprié pour garantir la sécurité du système et des données qu'il contient. Dans cet article, nous passerons en revue certaines choses à faire et à ne pas faire pour renforcer la sécurité de votre système Linux.  ## À faire :  ### Maintenez votre système à jour  Maintenir votre système [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) à jour est crucial pour maintenir sa sécurité. Des mises à jour régulières aident à corriger les vulnérabilités et les bogues de sécurité, garantissant que votre système reste protégé contre les attaques potentielles. Voici quelques exemples de mise à jour de votre système Linux à l'aide du gestionnaire de packages **apt-get** ou **yum** :  #### Mise à jour d'Ubuntu avec apt-get  Pour mettre à jour votre système Ubuntu en utilisant **apt-get**, ouvrez une fenêtre de terminal et saisissez :  Cela téléchargera les dernières listes de packages à partir des référentiels de packages Ubuntu. Une fois cette commande terminée, vous pouvez installer toutes les mises à jour disponibles à l'aide de la commande suivante :   Cela téléchargera et installera toutes les mises à jour disponibles pour votre système.  ### Mise à jour de CentOS à l'aide de yum  Pour mettre à jour votre système CentOS à l'aide de **yum**, ouvrez une fenêtre de terminal et enregistrez :   Cela téléchargera et installera toutes les mises à jour disponibles pour votre système. Vous pouvez également utiliser la commande suivante pour nettoyer tous les packages anciens ou inutilisés :   Cela supprimera tous les packages qui ne sont plus nécessaires sur votre système.  N'oubliez pas de vérifier et d'installer régulièrement les mises à jour sur votre système Linux pour assurer sa sécurité et sa stabilité.   ### Utiliser un pare-feu  Un pare-feu est une mesure de sécurité essentielle pour tout système Linux, car il aide à se protéger contre les accès non autorisés et autres cybermenaces. Voici comment utiliser le pare-feu **ufw** sur votre système Linux :  #### Installation et activation d'ufw pour les systèmes basés sur Ubuntu  Pour installer et activer **ufw**, ouvrez une fenêtre de terminal et notez :   Pour autoriser le trafic HTTP entrant (port 80) :   Pour bloquer le trafic entrant à partir d'une adresse IP spécifique :   Pour supprimer une règle :  Vous pouvez afficher les règles **ufw** actuelles en saisissant :    Cela affichera les règles actuelles et leur statut.  N'oubliez pas de revoir et de mettre à jour régulièrement vos règles **ufw** pour vous assurer que votre système est protégé contre les menaces potentielles.   #### Installation et activation du pare-feu pour les systèmes basés sur CentOS  Pour installer et activer le pare-feu par défaut sur CentOS, qui est **firewalld**, vous pouvez utiliser les commandes suivantes :   Ceci installera **firewalld** et l'activera sur votre système.  #### Configuration des règles de pare-feu pour les systèmes basés sur CentOS  Une fois **firewalld** activé, vous pouvez configurer ses règles pour autoriser ou bloquer le trafic entrant et sortant. Voici quelques exemples :  Pour autoriser le trafic SSH entrant (port 22) :   Pour autoriser le trafic HTTP entrant (port 80) :   Pour bloquer le trafic entrant à partir d'une adresse IP spécifique :   Pour supprimer une règle :   Vous pouvez afficher les règles **firewalld** actuelles en saisissant :   Cela affichera les règles actuelles et leur statut.  N'oubliez pas de revoir et de mettre à jour régulièrement vos règles **firewalld** pour vous assurer que votre système  ### Activer SELinux ou AppArmor  SELinux (Security-Enhanced Linux) et AppArmor sont deux modules de sécurité qui peuvent être utilisés pour appliquer des politiques de contrôle d'accès obligatoires dans les systèmes Linux. Par défaut, la plupart des distributions Linux modernes sont livrées avec SELinux ou AppArmor, et elles peuvent être activées et configurées pour améliorer la sécurité de votre système.  #### Activation de SELinux pour les systèmes basés sur CentOS  Pour vérifier si SELinux est activé sur votre système, validez la commande suivante :   Si SELinux n'est pas installé, vous pouvez l'installer à l'aide de la commande suivante :   Pour activer SELinux, vous devez modifier le fichier **/etc/selinux/config** et définir la variable **SELINUX** sur **enforcing** :  **Modificateur SELINUX=appliquer**  Enregistrez et quittez le fichier en utilisant CTRL + X et Y puis entrez, puis remplacez votre système.  #### Activation d'AppArmor pour les systèmes basés sur Ubuntu  Pour vérifier si AppArmor est activé sur votre système, validez la commande suivante :   Si AppArmor n'est pas installé, vous pouvez l'installer à l'aide de la commande suivante :  Pour activer AppArmor, vous devez modifier le fichier **/etc/default/grub** et ajouter le paramètre **security=apparmor** à la variable **GRUB_CMDLINE_LINUX** :  **Ajouter security=apparmor**  Enregistrez et quittez le fichier en utilisant CTRL+X et Y puis enregistrez, puis désactivez la commande suivante pour mettre à jour la configuration du chargeur de démarrage de votre système :   Enfin, remplacez votre système.  Une fois SELinux ou AppArmor activés, vous pouvez configurer leurs politiques pour réduire les privilèges des processus et limiter leur accès aux ressources système. Cela peut aider à minimiser l'impact potentiel d'une attaque réussie et à améliorer la sécurité globale de votre système.   ### Configurer les politiques de mot de passe  La configuration des politiques de mot de passe est une étape importante dans le renforcement de la sécurité de votre système Linux. En appliquant des exigences de mot de passe fort, vous pouvez vous assurer que les comptes d'utilisateurs sont sécurisés et protégés contre les attaques potentielles. Voici comment configurer les stratégies de mot de passe sur votre système Linux :  #### Configuration des politiques de mot de passe sur Ubuntu  Pour configurer les politiques de mot de passe sur Ubuntu, vous pouvez utiliser le module **pam_pwquality**. Ce module fournit un ensemble de vérifications de la force du mot de passe qui peut être utilisé pour appliquer les politiques de mot de passe. Pour installer le module **pam_pwquality**, ouvrez une fenêtre de terminal et saisissez :   Une fois le module installé, vous pouvez configurer ses paramètres en éditant le fichier **/etc/pam.d/common-password**. Par exemple, pour appliquer une longueur minimale de mot de passe de 8 caractères et exiger au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial, vous pouvez ajouter la ligne suivante au fichier :   Vous pouvez également configurer d'autres paramètres, tels que l'âge maximal du mot de passe, en ajoutant des lignes au fichier.  #### Configuration des politiques de mot de passe sur CentOS  Pour configurer les politiques de mot de passe sur CentOS, vous pouvez utiliser l'outil **authconfig**. Cet outil fournit un ensemble d'options qui peuvent être utilisées pour configurer des stratégies de mot de passe. Par exemple, pour appliquer un mot de passe d'une longueur minimale de 8 caractères et exiger au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial, vous pouvez utiliser la commande suivante :   Cela mettra à jour les fichiers **/etc/pam.d/system-auth** et **/etc/pam.d/password-auth** du système pour appliquer les politiques de mot de passe souhaités.  N'oubliez pas de revoir et de mettre à jour régulièrement vos politiques de mot de passe pour vous assurer qu'elles restent efficaces contre les attaques potentielles.   ### Surveillez vos journaux système  La surveillance de vos journaux système est un aspect important du maintien de la sécurité de votre système Linux. Les journaux système enregistrent l'activité du système, comme les tentatives de connexion infructueuses, les erreurs et d'autres événements importants, et peuvent fournir des informations précieuses sur les menaces de sécurité potentielles ou d'autres problèmes nécessitant une attention particulière. Voici comment surveillez vos journaux système :  #### Utilisation de la commande journalctl  Sur la plupart des distributions Linux modernes, vous pouvez utiliser la commande **journalctl** pour afficher les journaux système. Cette commande fournit une variété d'options qui peuvent être utilisées pour filtrer et rechercher des entrées de journal.  Pour afficher toutes les entrées du journal, déclinez simplement la commande suivante :   Cela affichera toutes les entrées du journal, avec les entrées les plus récentes en bas.  Pour filtrer les entrées de journal par une unité spécifique, telle qu'un service ou un processus, vous pouvez utiliser l'option **-u** suivie du nom de l'unité. Par exemple, pour afficher les entrées de journal du service **sshd**, vous pouvez effectuer la commande suivante :   Pour filtrer les entrées de journal selon une plage horaire spécifique, vous pouvez utiliser les options **--depuis** et **--jusqu'à** suivies d'un horodatage ou d'une plage horaire. Par exemple, pour afficher les entrées de journal de la dernière heure, vous pouvez effectuer la commande suivante :   #### Utilisation d'un outil de gestion des logs  Pour les systèmes plus grands ou plus complexes, il peut être utile d'utiliser un outil de gestion des journaux pour collecter et analyser les journaux système. Les outils de gestion des journaux peuvent fournir des fonctionnalités avancées, telles que la surveillance des journaux en temps réel, l'agrégation des journaux et l'analyse des journaux, et peuvent vous aider à identifier et à répondre plus efficacement aux menaces de sécurité potentielles .  Voici des exemples d'outils de gestion des journaux pour Linux :  - **Logwatch** : un outil simple d'analyse des journaux qui fournit des CV quotidiens par e-mail des journaux système - **Logrotate** : un outil qui fait pivoter et compresser automatiquement les fichiers journaux pour économiser de l'espace disque - ** Pile ELK ** : un outil de gestion des journaux open source populaire qui combine Elasticsearch, Logstash et Kibana pour fournir des capacités de surveillance et d'analyse des journaux en temps réel  N'oubliez pas de consulter et d'analyser régulièrement vos journaux système pour détecter et répondre aux menaces de sécurité potentielles en temps opportun.  ______  ## À ne pas faire :  ### Utilisez des mots de passe faibles  L'utilisation de mots de passe faibles est une erreur courante qui peut rendre votre système Linux vulnérable aux attaques. Les attaquants peuvent utiliser des outils pour deviner les mots de passe basés sur des mots, des noms ou des dates courants. Il est important d'utiliser des mots de passe forts et uniques qui ne sont pas facilement devinables.  Vous pouvez créer des mots de passe forts en utilisant une combinaison de lettres majuscules et minuscules, de chiffres et de caractères spéciaux. Il est également recommandé d'utiliser un [gestionnaire de mots de passe](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) pour générer et stocker en toute sécurité des mots de passe complexes. Les [gestionnaires de mots de passe](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) peuvent également vous aider à vous souvenir de vos mots de passe et à éviter d'utiliser le même mot de passe pour plusieurs comptes.  ### Autoriser l'accès root SSH  Autoriser l'accès root SSH est un risque de sécurité qui peut donner aux attaquants un contrôle total sur votre système Linux. Au lieu de cela, vous devez utiliser un compte d'utilisateur non root pour vous connecter à votre système, puis élever les privilèges à l'aide de la commande **sudo**. Cela permet de limiter l'impact potentiel d'une attaque en restreignant les privilèges des comptes d'utilisateurs.  ### Installer des logiciels inutiles  L'installation de logiciels inutiles peut augmenter la surface d'attaque de votre système Linux, le rendant plus vulnérable aux attaques. Il est important d'installer uniquement les logiciels nécessaires à votre système et de supprimer tout logiciel inutile. Cela permet de réduire le nombre de vulnérabilités potentielles sur votre système et de minimiser le risque d'une attaque réussie.  ### Utiliser un logiciel obsolète  L'utilisation de logiciels obsolètes peut rendre votre système vulnérable aux attaques qui exploitent des vulnérabilités connues. Il est important de toujours utiliser la dernière version du logiciel et de la mettre à jour régulièrement pour garantir la sécurité. Cela permet de corriger les vulnérabilités connues et de protéger votre système contre les attaques potentielles.  ______  ## Conclusion  En conclusion, le renforcement de votre système Linux est essentiel pour assurer sa sécurité et protéger les données qu'il contient. En suivant les choses à faire et à ne pas faire décrites dans cet article, vous pouvez prendre des mesures importantes pour protéger votre système et réduire le risque de cybermenaces. N'oubliez pas de toujours garder votre système à jour, d'utiliser un pare-feu, de configurer des politiques de mot de passe et de surveiller les journaux système. Évitez d'utiliser des mots de passe faibles, de désactiver les mises à jour automatiques, d'autoriser l'accès root SSH, d'installer des logiciels inutiles et d'utiliser des logiciels obsolètes. Avec ces meilleures pratiques à l'esprit, vous pouvez vous assurer que votre système Linux reste sécurisé et protégé.  ## Les références :  - [Guide de durcissement Linux du Center for Internet Security](https://www.cisecurity.org/cis-hardened-images/) - [Guide de sécurité Red Hat Enterprise Linux](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index) - [Documentation sur la sécurité d'Ubuntu](https://ubuntu.com/security) - [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)