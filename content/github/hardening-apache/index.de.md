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

### Eine Sammlung von Beispielkonfigurationen und Skripten zur Unterstützung von Systemadministratoren beim Härten von Apache-Webservern.  Apache ist von Haus aus überraschend unsicher. Viele Best Practices und Sicherheitskonfigurationen müssen manuell konfiguriert werden, bevor Apache in einer Produktionsumgebung eingeführt wird. Sie können dieses GitHub-Repository als Ausgangspunkt für die Sicherung Ihrer Apache-Instanzen verwenden.   ## ModSecurity mit OWASP Core Rule Set installieren  ### Schritt 1: Repositories aktualisieren **Auf Ubuntu/Debian:** **Auf CentOS/RHEL:**  ### Schritt 2: ModSecurity für Apache installieren **Auf Ubuntu/Debian:** **Auf CentOS/RHEL:**  ### Schritt 3: Konfigurieren Sie ModSecurity  ModSecurity ist standardmäßig nur so konfiguriert, dass Ereignisse von den Standardregeln protokolliert werden. Wir & sterbende Konfigurationsdatei bearbeiten, um sterbende Regeln zum Erkennen und Blockieren von unerwünschtem Datenverkehr zu ändern.  **Datei kopieren und umbenennen:** **Ändern Sie den ModSecurity-Erkennungsmodus, während SIE sterben Konfigurationsdatei bearbeiten:** Ändern Sie "Nur Erkennung" auf "Ein". Wenn Sie Nano verwenden, können Sie **CTRL+X**, dann **Y** und **Enter** drücken, um zu speichern und zu beenden.  **Apache neu starten**  Unter Ubuntu\ Debian:  Auf CentOS\RHEL: ### Schritt 4: OWASP ModSecurity Core Rule Set herunterladen und installieren  **Apache neu starten**  Unter Ubuntu\Debian:  Auf CentOS\RHEL: ### Schritt 5: Zusätzliches Lesematerial  **Zusätzliche Installationsanweisungen:**  [Installieren Sie OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/)   [ModSecurity installieren](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)   ## SSL-Zertifikate  ### Selbstsigniert  Befolgen Sie die Anweisungen von [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16- 04 )  Für dieses Tutorial gehe ich davon aus, dass SIE die Datei **example.com.conf** aus dem Repository verwenden Werden.  #### Schritt 1: Erstellen Sie das SSL-Zertifikat  **Füllen Sie die Eingabeaufforderungen entsprechend aus. Die einige Zeile ist diejenige, die den Common Name abfragt (z. B. Server-FQDN oder IHR Name). Sie müssen den mit Ihrem Server verknüpften Domänennamen oder, was wahrscheinlicher ist, die öffentliche IP-Adresse Ihres Servers eingeben.** Wenn Sie das Zertifikat nur für den IP-Zugriff in example.com.conf verwenden, verwenden Sie bitte **"NA"** für alle Werte, sofern möglich.  #### Perfect Forward Secrecy-Konfiguration    ### Automatisieren mit LetsEncrypt und Certbot  Folgen Sie dem Tutorial von [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)  #### Schritt 1: Certbot installieren  ### Schritt 2: Wählen Sie aus, wie Sie Certbot ausführen möchten  ##### Holen Sie sich entweder Ihre Zertifikate und installieren Sie sie...  ##### Oder holen Sie sich einfach ein Zertifikat   #### Schritt 3: Testen Sie die automatische Verlängerung      