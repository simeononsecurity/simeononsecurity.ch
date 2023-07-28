---
title: "Secure Apache Web Server: Kompleksowy przewodnik dla administratorów systemów"
date: 2020-07-27
---
 Zbiór przykładowych konfiguracji i skryptów pomagających administratorom systemów w zabezpieczaniu serwerów internetowych Apache.

Apache po wyjęciu z pudełka jest zaskakująco niezabezpieczony. Wiele najlepszych praktyk i konfiguracji bezpieczeństwa musi zostać skonfigurowanych ręcznie przed wdrożeniem Apache w środowisku produkcyjnym. Możesz użyć tego repozytorium GitHub jako punktu wyjścia do zabezpieczenia instancji Apache.


## Instalacja ModSecurity z OWASP Core Rule Set

### Krok 1: Aktualizacja repozytoriów
**Na Ubuntu/ Debianie:**.
```
sudo apt-get update -y
```
**Na CentOS/RHEL:**.
``` 
sudo yum update -y
```

### Krok 2: Instalacja ModSecurity dla Apache
**Na Ubuntu/ Debianie:**.
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
**Na CentOS/RHEL:**.
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```

### Krok 3: Konfiguracja ModSecurity

ModSecurity jest domyślnie skonfigurowany tylko do rejestrowania zdarzeń z domyślnych reguł. Będziemy musieli edytować plik konfiguracyjny, aby zmodyfikować reguły w celu wykrywania i blokowania złośliwego ruchu.

**Skopiuj i zmień nazwę pliku:**.
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
Jeśli używasz nano, możesz nacisnąć **CTRL+X**, a następnie **Y** i **Enter**, aby zapisać i wyjść.

**Restart Apache**

Na Ubuntu\ Debian:
```
sudo systemctl restart apache2
```

W systemie CentOS:
```
sudo systemctl restart httpd.service
```
### Krok 4: Pobieranie i instalacja zestawu podstawowych reguł OWASP ModSecurity

```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
**Restart Apache**

Na Ubuntu\ Debian:
```
sudo systemctl restart apache2
```

W systemie CentOS:
```
sudo systemctl restart httpd.service
```
### Krok 5: Dodatkowe materiały do czytania

**Dodatkowe instrukcje instalacji:**

[Install OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/)


[Install ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)


## Certyfikaty SSL

### Podpisany samodzielnie

Postępując zgodnie z instrukcjami [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04)

W tym poradniku zakładam, że będziesz używał pliku **example.com.conf** z repozytorium.

#### Krok 1: Utwórz certyfikat SSL
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

**Wypełnij odpowiednio podpowiedzi. Najważniejszą linią jest ta, która wymaga podania nazwy wspólnej (np. FQDN serwera lub TWOJA nazwa). Należy wprowadzić nazwę domeny powiązaną z serwerem lub, co bardziej prawdopodobne, publiczny adres IP serwera.
W przypadku korzystania z certyfikatu tylko dla dostępu IP w pliku example.com.conf należy użyć **"NA "** dla wszystkich możliwych wartości.

#### Konfiguracja Perfect Forward Secrecy
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```



### Automatyzacja za pomocą LetsEncrypt i Certbot

Postępując zgodnie z samouczkiem [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)

#### Krok 1: Zainstaluj Certbota

```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
### Krok 2: Wybierz sposób, w jaki chcesz uruchomić Certbota

##### Pobierz i zainstaluj swoje certyfikaty...
```
sudo certbot --apache
```

##### Lub po prostu uzyskać certyfikat

```
sudo certbot certonly --apache
```

#### Krok 3: Przetestuj automatyczne odnawianie

```
sudo certbot renew --dry-run
```





