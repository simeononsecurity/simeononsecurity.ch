---
title: "Secure Apache Web Server: A Comprehensive Guide for System Administrators"
date: 2020-07-27T10:15:03-07:00
draft: false
description: "Learn how to harden your Apache web server and ensure maximum security with this comprehensive guide for system administrators."
tags: ["Apache Web Server", "Security", "SSL Encryption", "ModSecurity", "OWASP Core Rule Set", "Self-Signed Certificate", "LetsEncrypt", "Certbot", "Firewall", "Configuration", "System Administration", "Web Application Security", "Best Practices", "Common Attacks", "HTTPS", "Web Server Hardening", "Ubuntu", "Debian", "CentOS", "RHEL"]
---
```
sudo apt-get update -y
```
``` 
sudo yum update -y
```
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```
```
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
```
sudo nano /etc/modsecurity/modsecurity.conf
```
```
SecRuleEngine DetectionOnly
```
```
SecRuleEngine On
```
```
sudo systemctl restart apache2
```
```
sudo systemctl restart httpd.service
```
```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
```
sudo systemctl restart apache2
```
```
sudo systemctl restart httpd.service
```
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```
```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
```
sudo certbot --apache
```
```
sudo certbot certonly --apache
```
```
sudo certbot renew --dry-run
```

### Une collection d'exemples de configurations et de scripts pour aider les administrateurs système à activer les serveurs Web Apache.  Apache, prêt à l'emploi, est étonnamment peu sûr. De nombreuses bonnes pratiques et configurations de sécurité doivent être configurées manuellement avant de pouvoir Apache dans un environnement de production. Vous pouvez utiliser ce référentiel GitHub comme point de départ pour sécuriser vos instances Apache.   ## Installation de ModSecurity avec l'ensemble de règles de base OWASP  ### Étape 1 : Mettre à jour les référentiels **Sur Ubuntu/ Debian :** **Sur CentOS/RHEL :**  ### Étape 2 : Installer ModSecurity pour Apache **Sur Ubuntu/ Debian :** **Sur CentOS/RHEL :**  ### Étape 3 : Configurer ModSecurity  Par défaut, ModSecurity n'est configuré que pour consigner les événements à partir des règles par défaut. Nous devrons éditer le fichier de configuration pour modifier les règles de détection et de blocage du trafic erroné.  **Copiez et renommez le fichier :** **Changez le mode de détection ModSecurity en éditant le fichier de configuration :** Remplacez "Détection uniquement" par "Activé" Si vous utilisez nano, vous pouvez appuyer sur **CTRL+X**, puis sur **Y** et **Entrée** pour enregistrer et quitter.  **Redémarrer Apache**  Sur Ubuntu \ Debian :  Sur CentOS\RHEL : ### Étape 4 : Téléchargement et installation de l'ensemble de règles principales OWASP ModSecurity  **Redémarrer Apache**  Sur Ubuntu \ Debian :  Sur CentOS\RHEL : ### Étape 5 : Documents de lecture supplémentaires  **Instructions d'installation supplémentaires :**  [Installer l'ensemble de règles de base OWASP ModSecurity] (https://owasp.org/www-project-modsecurity-core-rule-set/)   [Installer ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)   ## Certificats SSL  ### Auto-signé  En suivant les instructions de [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16- 04 )  Pour ce tutoriel, je suppose que vous allez utiliser le fichier **example.com.conf** du référentiel.  #### Étape 1 : Créer le certificat SSL  ** remplir les invitations de manière appropriée. La ligne la plus importante est celle qui demande le nom commun (par exemple, le FQDN du serveur ou VOTRE nom). Vous devez entrer le nom de domaine associé à votre serveur ou, plus probablement, l'adresse IP publique de votre serveur.** Si vous l'utilisez pour le certificat d'accès IP uniquement dans example.com.conf, veuillez utiliser **"NA"** pour toutes les valeurs lorsque cela est possible.  #### Configuration parfaite de la confidentialité de transmission    ### Automatisez avec LetsEncrypt et Certbot  Suite du tutoriel de [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)  #### Étape 1 : Installer Certbot  ### Étape 2  : Choisissez la manière dont vous souhaitez désactiver Certbot  ##### Recevez et installez vos certificats...  ##### Ou, obtenez simplement un certificat   #### Étape 3 : testez le renouvellement automatique      