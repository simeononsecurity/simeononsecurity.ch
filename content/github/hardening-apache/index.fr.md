---
title: "Serveur Web Apache sécurisé : Un guide complet pour les administrateurs système"
date: 2020-07-27
---
 Une collection d'exemples de configurations et de scripts pour aider les administrateurs système à renforcer les serveurs web Apache.

Apache, dans sa version initiale, est étonnamment peu sûr. De nombreuses bonnes pratiques et configurations de sécurité doivent être configurées manuellement avant de déployer Apache dans un environnement de production. Vous pouvez utiliser ce dépôt GitHub comme point de départ pour sécuriser vos instances Apache.


## Installer ModSecurity avec le jeu de règles OWASP Core

### Étape 1 : Mise à jour des dépôts
**Sur Ubuntu/ Debian:**
```
sudo apt-get update -y
```
**Sur CentOS/RHEL:**
``` 
sudo yum update -y
```

### Étape 2 : Installation de ModSecurity pour Apache
**Sur Ubuntu/ Debian:**
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
**Sur CentOS/RHEL:**
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```

### Étape 3 : Configurer ModSecurity

Par défaut, ModSecurity n'est configuré que pour enregistrer les événements des règles par défaut. Nous devrons éditer le fichier de configuration pour modifier les règles afin de détecter et de bloquer le trafic malveillant.

**Copiez et renommez le fichier:**.
```
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
**Changer le mode de détection de ModSecurity en éditant le fichier de configuration:**
```
sudo nano /etc/modsecurity/modsecurity.conf
```
Remplacer "DetectionOnly" par "On".
```
SecRuleEngine DetectionOnly
```
```
SecRuleEngine On
```
Si vous utilisez nano, vous pouvez appuyer sur **CTRL+X**, puis **Y** et **Enter** pour sauvegarder et quitter.

**Redémarrer Apache

Sur Ubuntu et Debian :
```
sudo systemctl restart apache2
```

Sur CentOS :
```
sudo systemctl restart httpd.service
```
### Étape 4 : Téléchargement et installation de l'ensemble de règles de base OWASP ModSecurity

```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
**Redémarrer Apache**

Sur Ubuntu et Debian :
```
sudo systemctl restart apache2
```

Sur CentOS :
```
sudo systemctl restart httpd.service
```
### Étape 5 : Matériel de lecture supplémentaire

**Instructions d'installation supplémentaires:**

[Install OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/)


[Install ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)


## Certificats SSL

### Autosigné

En suivant les instructions de [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04)

Pour ce tutoriel, je suppose que vous allez utiliser le fichier **example.com.conf** du référentiel.

#### Etape 1 : Créer le certificat SSL
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

**Remplissez les invites de manière appropriée. La ligne la plus importante est celle qui demande le nom commun (par exemple, le FQDN du serveur ou VOTRE nom). Vous devez saisir le nom de domaine associé à votre serveur ou, plus probablement, l'adresse IP publique de votre serveur**.
Si vous utilisez le certificat d'accès IP uniquement dans le fichier example.com.conf, veuillez utiliser **"NA "** pour toutes les valeurs lorsque cela est possible.

#### Configuration du Perfect Forward Secrecy
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```



### Automatiser avec LetsEncrypt et Certbot

En suivant le tutoriel de [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)

#### Étape 1 : Installer Certbot

```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
### Étape 2 : Choisissez comment vous souhaitez faire fonctionner Certbot

##### Soit vous obtenez et installez vos certificats...
```
sudo certbot --apache
```

##### Ou bien, il suffit d'obtenir un certificat

```
sudo certbot certonly --apache
```

#### Étape 3 : Tester le renouvellement automatique

```
sudo certbot renew --dry-run
```





