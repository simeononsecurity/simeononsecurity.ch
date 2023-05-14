---
title: "Beveiligde Apache-webserver: Een uitgebreide gids voor systeembeheerders"
date: 2020-07-27
---
 Een verzameling voorbeeldconfiguraties en scripts om systeembeheerders te helpen bij het hardenen van Apache webservers.

Apache is uit de doos verrassend onveilig. Veel best practices en beveiligingsconfiguraties moeten handmatig worden geconfigureerd voordat Apache in een productieomgeving wordt uitgerold. U kunt deze GitHub repository gebruiken als startpunt voor het beveiligen van uw Apache instanties.


## ModSecurity installeren met OWASP Core Rule Set

### Stap 1: Repositories bijwerken
**Op Ubuntu/Debian:**
```
sudo apt-get update -y
```
**Op CentOS/RHEL:**
``` 
sudo yum update -y
```

### Stap 2: ModSecurity voor Apache installeren
**Op Ubuntu/Debian:**
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
**Op CentOS/RHEL:**
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```

### Stap 3: ModSecurity configureren

ModSecurity is standaard alleen geconfigureerd om gebeurtenissen van de standaardregels te loggen. We moeten het configuratiebestand bewerken om de regels aan te passen om kwaadaardig verkeer te detecteren en te blokkeren.

**Kopieer en hernoem het bestand:**
```
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
**Wijzig de ModSecurity-detectiemodus door het configuratiebestand te bewerken:**
```
sudo nano /etc/modsecurity/modsecurity.conf
```
Verander "DetectionOnly" in "On".
```
SecRuleEngine DetectionOnly
```
```
SecRuleEngine On
```
Als u nano gebruikt, kunt u op **CTRL+X** drukken, dan **Y** en **Enter** om op te slaan en af te sluiten.

**Herstart Apache**

Op Ubuntu en Debian:
```
sudo systemctl restart apache2
```

Op CentOS:
```
sudo systemctl restart httpd.service
```
### Stap 4: Downloaden en installeren van OWASP ModSecurity Core Rule Set

```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
**Restart Apache**

Op Ubuntu en Debian:
```
sudo systemctl restart apache2
```

Op CentOS:
```
sudo systemctl restart httpd.service
```
### Stap 5: Extra leesmateriaal

**Toegevoegde installatie-instructies:**

[Install OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/)


[Install ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)


## SSL Certificaten

### Zelf ondertekend

Volgens de instructies van[Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04)

Voor deze tutorial ga ik ervan uit dat je het **example.com.conf** bestand uit het archief gaat gebruiken.

#### Stap 1: Maak het SSL-certificaat aan
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

**Vul de prompts op de juiste manier in. De belangrijkste regel is die met de Common Name (bijv. server FQDN of UW naam). U moet de domeinnaam invoeren die bij uw server hoort of, waarschijnlijker, het openbare IP-adres van uw server.**
Als u een certificaat voor alleen IP-toegang gebruikt in example.com.conf, gebruik dan waar mogelijk **"NA"** voor alle waarden.

#### Perfect Forward Secrecy Configuratie
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```



### Automatiseren met LetsEncrypt en Certbot

Volg de handleiding van[Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)

#### Step 1: Install Certbot

```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
### Stap 2: Kies hoe u Certbot wilt gebruiken

##### Ofwel haalt en installeert u uw certificaten...
```
sudo certbot --apache
```

##### Of, gewoon een certificaat halen

```
sudo certbot certonly --apache
```

#### Stap 3: Test automatische verlenging

```
sudo certbot renew --dry-run
```





