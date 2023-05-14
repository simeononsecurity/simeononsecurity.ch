---
title: "Secure Apache Web Server: A Comprehensive Guide for System Administrators"
date: 2020-07-27
---
 Zbiór przykładowych konfiguracji i skryptów wspomagających administratorów systemu w utwardzaniu serwerów internetowych Apache.

Apache, po wyjęciu z pudełka, jest zaskakująco mało bezpieczny. Wiele najlepszych praktyk i konfiguracji bezpieczeństwa musi być skonfigurowanych ręcznie przed uruchomieniem Apache'a w środowisku produkcyjnym. Możesz użyć tego repozytorium GitHub jako punktu wyjścia do zabezpieczenia swoich instancji Apache.


## Instalacja ModSecurity z OWASP Core Rule Set

# Krok 1: Zaktualizuj Repozytoria
**Na Ubuntu/ Debianie:**
```
sudo apt-get update -y
```
**Na CentOS/RHEL:**
``` 
sudo yum update -y
```

### Krok 2: Instalacja ModSecurity dla Apache'a
**Na Ubuntu/ Debian:**
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
**Na CentOS/RHEL:**
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```

### Krok 3: Konfiguracja ModSecurity

ModSecurity domyślnie jest skonfigurowany tylko do rejestrowania zdarzeń z domyślnych reguł. Będziemy musieli edytować plik konfiguracyjny, aby zmodyfikować reguły w celu wykrycia i zablokowania złośliwego ruchu.

**Kopiuj i zmień nazwę pliku:**.
```
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
**Zmień tryb wykrywania ModSecurity poprzez edycję pliku konfiguracyjnego:**.
```
sudo nano /etc/modsecurity/modsecurity.conf
```
Zmień "DetectionOnly" na "On"
```
SecRuleEngine DetectionOnly
```
```
SecRuleEngine On
```
Jeśli używasz nano, możesz nacisnąć **CTRL+X**, następnie **Y** i **Enter**, aby zapisać i wyjść.

**Restart Apache**

Na Ubuntu i Debianie:
```
sudo systemctl restart apache2
```

Na CentOS:
```
sudo systemctl restart httpd.service
```
### Krok 4: Pobranie i instalacja OWASP ModSecurity Core Rule Set

```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
**Restart Apache**

Na Ubuntu / Debiana:
```
sudo systemctl restart apache2
```

Na CentOS:
```
sudo systemctl restart httpd.service
```
### Krok 5: Dodatkowy materiał do czytania

**Dodatkowa instrukcja montażu:**

[Install OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/)


[Install ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)


## Certyfikaty SSL

### Self Signed

Postępując zgodnie z instrukcjami z[Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04)

W tym poradniku zakładam, że będziesz używał pliku **example.com.conf** z repozytorium.

#### Krok 1: Utworzenie certyfikatu SSL
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

**Wypełnij odpowiednio polecenia. Najważniejszą linią jest ta, która prosi o podanie Common Name (np. FQDN serwera lub nazwa YOUR). Musisz wpisać nazwę domeny związanej z Twoim serwerem lub, co bardziej prawdopodobne, publiczny adres IP Twojego serwera.**
Jeśli używasz certyfikatu tylko dla dostępu IP w example.com.conf, użyj **"NA "** dla wszystkich wartości, jeśli to możliwe.

#### Konfiguracja Perfect Forward Secrecy
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```



### Automatyzacja za pomocą LetsEncrypt i Certbot

Podążając za tutorialem z[Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)

#### Krok 1: Zainstaluj Certbot

```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
### Krok 2: Wybierz sposób, w jaki chcesz uruchomić Certbota

##### Albo pobierz i zainstaluj swoje certyfikaty...
```
sudo certbot --apache
```

##### Albo po prostu zdobądź certyfikat

```
sudo certbot certonly --apache
```

#### Krok 3: Przetestuj automatyczne odnawianie.

```
sudo certbot renew --dry-run
```





