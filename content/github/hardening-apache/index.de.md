---
title: "Sicherer Apache-Webserver: Ein umfassendes Handbuch für Systemadministratoren"
date: 2020-07-27
---
 Eine Sammlung von Beispielkonfigurationen und Skripten, die Systemadministratoren bei der Absicherung von Apache-Webservern helfen.

Apache ist im Auslieferungszustand überraschend unsicher. Viele Best Practices und Sicherheitskonfigurationen müssen manuell konfiguriert werden, bevor Apache in einer Produktionsumgebung eingesetzt werden kann. Sie können dieses GitHub-Repository als Ausgangspunkt für die Sicherung Ihrer Apache-Instanzen verwenden.


## Installation von ModSecurity mit OWASP Core Rule Set

### Schritt 1: Repositories aktualisieren
**Unter Ubuntu/Debian:**
```
sudo apt-get update -y
```
**Auf CentOS/RHEL:**
``` 
sudo yum update -y
```

### Schritt 2: Installation von ModSecurity für Apache
**Unter Ubuntu/Debian:**
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
**Auf CentOS/RHEL:**
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```

### Schritt 3: ModSecurity konfigurieren

ModSecurity ist standardmäßig so konfiguriert, dass es nur die Ereignisse der Standardregeln protokolliert. Wir müssen die Konfigurationsdatei bearbeiten, um die Regeln zur Erkennung und Blockierung von bösartigem Datenverkehr zu ändern.

**Kopieren Sie die Datei und benennen Sie sie um:**
```
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
**Ändern Sie den ModSecurity-Erkennungsmodus durch Bearbeiten der Konfigurationsdatei:**
```
sudo nano /etc/modsecurity/modsecurity.conf
```
Ändern Sie "DetectionOnly" in "On"
```
SecRuleEngine DetectionOnly
```
```
SecRuleEngine On
```
Wenn Sie nano verwenden, können Sie **CTRL+X** drücken, dann **Y** und **Enter**, um zu speichern und zu beenden.

**Apache neu starten**

Unter Ubuntu und Debian:
```
sudo systemctl restart apache2
```

Unter CentOS:
```
sudo systemctl restart httpd.service
```
### Schritt 4: Herunterladen und Installieren von OWASP ModSecurity Core Rule Set

```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
**Apache neu starten**

Unter Ubuntu und Debian:
```
sudo systemctl restart apache2
```

Unter CentOS:
```
sudo systemctl restart httpd.service
```
### Schritt 5: Zusätzliches Lesematerial

**Zusätzliche Installationsanweisungen:**

[Install OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/)


[Install ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)


## SSL-Zertifikate

### Selbst signiert

Folgen Sie den Anweisungen von [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04)

Für dieses Tutorial gehe ich davon aus, dass Sie die Datei **example.com.conf** aus dem Repository verwenden werden.

#### Schritt 1: Erstellen des SSL-Zertifikats
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

**Füllen Sie die Eingabeaufforderungen entsprechend aus. Die wichtigste Zeile ist diejenige, in der der Common Name abgefragt wird (z. B. der FQDN des Servers oder IHR Name). Sie müssen den mit Ihrem Server verbundenen Domänennamen oder, was wahrscheinlicher ist, die öffentliche IP-Adresse Ihres Servers eingeben.**
Wenn Sie in der Datei example.com.conf ein Zertifikat verwenden, das nur für den IP-Zugriff bestimmt ist, verwenden Sie bitte **"NA "** für alle Werte, wo dies möglich ist.

#### Perfect Forward Secrecy Konfiguration
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```



### Automatisieren mit LetsEncrypt und Certbot

Nach der Anleitung von [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)

#### Schritt 1: Certbot installieren

```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
### Schritt 2: Wählen Sie aus, wie Sie Certbot ausführen möchten

##### Holen Sie entweder Ihre Zertifikate und installieren Sie sie...
```
sudo certbot --apache
```

##### Oder besorgen Sie sich einfach ein Zertifikat

```
sudo certbot certonly --apache
```

#### Schritt 3: Automatische Erneuerung testen

```
sudo certbot renew --dry-run
```





