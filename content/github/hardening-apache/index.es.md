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

### Una colección de ejemplos de configuraciones y scripts para ayudar a los administradores de sistemas a fortalecer los web Apache.  Apache, fuera de la caja, es sorprendentemente inseguro. Muchas mejores prácticas y configuraciones de seguridad deben configurarse manualmente antes de implementar Apache en un entorno de producción. Puede utilizar este repositorio de GitHub como punto de partida para proteger sus instancias de Apache.   ## Instalación de ModSecurity con el conjunto de reglas básicas de OWASP  ### Paso 1: Actualizar repositorios **En Ubuntu/Debian:** **En CentOS/RHEL:**  ### Paso 2: Instalación de ModSecurity para Apache **En Ubuntu/Debian:** **En CentOS/RHEL:**  ### Paso 3: Configurar ModSecurity  ModSecurity por defecto solo está configurado para registrar eventos de las reglas establecidas. Tendremos que editar el archivo de configuración para modificar las reglas para detectar y bloquear el tráfico malicioso.  **Copiar y renombrar el archivo:** **Cambia el modo de detección de ModSecurity editando el archivo de configuración:** Cambie "Solo detección" a "Activado" Si está usando nano, puede presionar **CTRL+X**, luego **Y** y **Enter** para guardar y salir.  **Reiniciar Apache**  En Ubuntu\Debian:  En CentOS\RHEL: ### Paso 4: Descargar e instalar el conjunto de reglas básicas de OWASP ModSecurity  **Reiniciar Apache**  En Ubuntu\Debian:  En CentOS\RHEL: ### Paso 5: Material de lectura adicional  **Instrucciones de instalación adicionales:**  [Instalar conjunto de reglas básicas de OWASP ModSecurity] (https://owasp.org/www-project-modsecurity-core-rule-set/)   [Instalar ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)   ##Certificados SSL  ### Autofirmado  Siguiendo las instrucciones de [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04 )  Para este tutorial, supongo que usará el archivo **example.com.conf** del repositorio.  #### Paso 1: Crear el certificado SSL  **Llene las instrucciones apropiadamente. La línea más importante es la que solicita el nombre común (por ejemplo, servidor FQDN o SU nombre). Debe ingresar el nombre de dominio asociado con su servidor o, más probablemente, la dirección IP pública de su servidor.** Si se utiliza para el certificado de acceso IP únicamente en el ejemplo.com.conf, utilice **"NA"** para todos los valores donde sea posible.  #### Configuración Perfect Forward Secrecy    ### Automático con LetsEncrypt y Certbot  Siguiendo el tutorial de [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)  #### Paso 1: Instalar Certbot  ### Paso 2: elige cómo te gustaría ejecutar Certbot  ##### Obtenga e instale sus certificados...  ##### O simplemente obtenga un certificado   #### Paso 3: Probar la renovación automática      