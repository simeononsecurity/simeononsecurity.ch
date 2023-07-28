---
title: "Servidor Web Apache Seguro: Guía completa para administradores de sistemas"
date: 2020-07-27
---
 Una colección de configuraciones y scripts de ejemplo para ayudar a los administradores de sistemas a reforzar los servidores web Apache.

Apache, fuera de la caja, es sorprendentemente inseguro. Muchas de las mejores prácticas y configuraciones de seguridad tienen que ser configuradas manualmente antes de desplegar Apache en un entorno de producción. Puedes usar este repositorio de GitHub como punto de partida para asegurar tus instancias de Apache.


## Instalando ModSecurity con OWASP Core Rule Set

### Paso 1: Actualizar Repositorios
**En Ubuntu/Debian:**
```
sudo apt-get update -y
```
**On CentOS/RHEL:**
``` 
sudo yum update -y
```

### Paso 2: Instalar ModSecurity para Apache
**En Ubuntu/Debian:**
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
**On CentOS/RHEL:**
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```

### Paso 3: Configurar ModSecurity

ModSecurity por defecto sólo está configurado para registrar eventos de las reglas por defecto. Tendremos que editar el fichero de configuración para modificar las reglas para detectar y bloquear tráfico malicioso.

**Copie y renombre el fichero:**
```
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
**Cambiar el modo de detección de ModSecurity editando el fichero de configuración:**
```
sudo nano /etc/modsecurity/modsecurity.conf
```
Cambiar "DetectionOnly" a "On".
```
SecRuleEngine DetectionOnly
```
```
SecRuleEngine On
```
Si estás usando nano puedes pulsar **CTRL+X**, luego **Y** y **Enter** para guardar y salir.

**Reiniciar Apache

En Ubuntu\ Debian:
```
sudo systemctl restart apache2
```

On CentOS\ RHEL:
```
sudo systemctl restart httpd.service
```
### Paso 4: Descarga e Instalación del Conjunto de Reglas OWASP ModSecurity Core

```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
**Reiniciar Apache

En Ubuntu\ Debian:
```
sudo systemctl restart apache2
```

On CentOS\ RHEL:
```
sudo systemctl restart httpd.service
```
### Paso 5: Material de lectura adicional

**Instrucciones de instalación adicionales

[Install OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/)


[Install ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)


## Certificados SSL

### Autofirmado

Siguiendo las instrucciones de [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04)

Para este tutorial, asumo que vas a usar el archivo **ejemplo.com.conf** del repositorio.

#### Paso 1: Crear el certificado SSL
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

**Rellene los campos correctamente. La línea más importante es la que solicita el Nombre Común (por ejemplo, FQDN del servidor o SU nombre). Debe introducir el nombre de dominio asociado a su servidor o, más probablemente, la dirección IP pública de su servidor.**
Si utiliza para el certificado de acceso sólo IP en el ejemplo.com.conf por favor utilice **"NA "** para todos los valores donde sea posible.

#### Configuración de Perfect Forward Secrecy
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```



### Automatizar con LetsEncrypt y Certbot

Siguiendo el tutorial de [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)

#### Paso 1: Instalar Certbot

```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
### Paso 2: Elige cómo quieres ejecutar Certbot

##### Obtenga e instale sus certificados...
```
sudo certbot --apache
```

##### O, simplemente consigue un certificado

```
sudo certbot certonly --apache
```

#### Paso 3: Probar la renovación automática

```
sudo certbot renew --dry-run
```





