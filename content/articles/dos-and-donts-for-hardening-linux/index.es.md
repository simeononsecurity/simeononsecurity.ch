---
title: "Qué hacer y qué no hacer para reforzar su sistema Linux"
date: 2023-02-28
toc: true
draft: false
description: "Aprenda lo que debe y no debe hacer para reforzar su sistema Linux, incluidas las actualizaciones, el uso de cortafuegos, la activación de SELinux o AppArmor, la configuración de políticas de contraseñas y la supervisión de los registros del sistema."
tags: ["Seguridad en Linux", "endurecimiento del sistema", "cortafuegos", "SELinux", "AppArmor", "política de contraseñas", "actualizaciones del sistema", "registros del sistema", "módulos de seguridad", "políticas de control de acceso", "ciberseguridad", "seguridad del sistema", "seguridad de la red", "gestión de vulnerabilidades", "buenas prácticas de seguridad", "Seguridad informática", "seguridad de la información", "actualizaciones de software", "acceso root", "gestor de contraseñas"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Un candado de dibujos animados sostiene un escudo con la palabra Linux, mientras una flecha rebota en el escudo."
coverCaption: ""
---


Linux es un sistema operativo popular utilizado tanto por particulares como por empresas. Aunque a menudo se considera más seguro que otros sistemas operativos debido a su naturaleza de código abierto, todavía requiere un endurecimiento adecuado para garantizar la seguridad del sistema y los datos que contiene. En este artículo, vamos a repasar algunas cosas que hacer y no hacer en el endurecimiento general que puede ayudar a mantener su sistema Linux seguro.

## Hacer:

### Mantenga su sistema actualizado

Mantenga su [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) es crucial para mantener su seguridad. Las actualizaciones periódicas ayudan a corregir vulnerabilidades y errores de seguridad, garantizando que su sistema permanezca seguro frente a posibles ataques. Aquí tienes algunos ejemplos de cómo actualizar tu sistema Linux utilizando el gestor de paquetes **apt-get** o **yum**:

#### Actualización de Ubuntu mediante apt-get

Para actualizar su sistema Ubuntu utilizando **apt-get**, abra una ventana de terminal y escriba:
```bash
sudo apt-get update
```

Esto descargará las últimas listas de paquetes de los repositorios de paquetes de Ubuntu. Una vez completado este comando, puede instalar cualquier actualización disponible utilizando el siguiente comando:

```bash
sudo apt-get upgrade

```

Esto descargará e instalará cualquier actualización disponible para su sistema.

### Actualizar CentOS usando yum

Para actualizar su sistema CentOS usando **yum**, abra una ventana de terminal y escriba:

```bash
sudo yum update
```

Esto descargará e instalará cualquier actualización disponible para su sistema. También puede utilizar el siguiente comando para limpiar los paquetes antiguos o no utilizados:

```bash
sudo yum autoremove
```

Esto eliminará cualquier paquete que ya no sea necesario en su sistema.

Recuerde comprobar e instalar actualizaciones en su sistema Linux con regularidad para garantizar su seguridad y estabilidad.


### Use un cortafuegos

Un cortafuegos es una medida de seguridad esencial para cualquier sistema Linux, ya que ayuda a proteger contra el acceso no autorizado y otras amenazas cibernéticas. A continuación te explicamos cómo utilizar el cortafuegos **ufw** en tu sistema Linux:

#### Instalar y habilitar ufw para sistemas basados en Ubuntu

Para instalar y habilitar **ufw**, abra una ventana de terminal y escriba:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Para permitir el tráfico HTTP entrante (puerto 80):

```bash
sudo ufw allow http
```

Para bloquear el tráfico entrante de una dirección IP específica:

```bash
sudo ufw deny from <ip_address>
```

Para eliminar una regla:
```bash
sudo ufw delete <rule_number>
```

Puedes ver las reglas **ufw** actuales escribiendo:

```bash
sudo ufw status
```


Esto mostrará las reglas actuales y su estado.

Recuerde revisar y actualizar regularmente sus reglas **ufw** para asegurarse de que su sistema está protegido contra posibles amenazas.


#### Instalar y habilitar firewalld para sistemas basados en CentOS

Para instalar y habilitar el firewall por defecto en CentOS, que es **firewalld**, puedes usar los siguientes comandos:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Esto instalará **firewalld** y lo habilitará en su sistema.

#### Configuración de reglas firewalld para sistemas basados en CentOS

Una vez que **firewalld** está habilitado, puedes configurar sus reglas para permitir o bloquear el tráfico entrante y saliente. Aquí tienes algunos ejemplos:

Para permitir el tráfico SSH entrante (puerto 22):

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Para permitir el tráfico HTTP entrante (puerto 80):

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Para bloquear el tráfico entrante de una dirección IP específica:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

Para eliminar una regla:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

Puedes ver las reglas actuales de **firewalld** escribiendo:

```bash
sudo firewall-cmd --list-all
```

Esto mostrará las reglas actuales y su estado.

Recuerde revisar y actualizar regularmente sus reglas **firewalld** para asegurarse de que su sistema

### Habilite SELinux o AppArmor

SELinux (Security-Enhanced Linux) y AppArmor son dos módulos de seguridad que pueden utilizarse para aplicar políticas de control de acceso obligatorias en sistemas Linux. Por defecto, la mayoría de las distribuciones Linux modernas vienen con SELinux o AppArmor instalados, y pueden ser habilitados y configurados para mejorar la seguridad de su sistema.

#### Activación de SELinux para sistemas basados en CentOS

Para comprobar si SELinux está habilitado en su sistema, ejecute el siguiente comando:

```bash
sestatus
```

Si SELinux no está instalado, puede instalarlo utilizando el siguiente comando:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Para activar SELinux, necesitas editar el archivo **/etc/selinux/config** y establecer la variable **SELINUX** a **enforcing**:

```bash
sudo nano /etc/selinux/config
```
**Cambiar SELINUX=obligatorio**
```
SELINUX=enforcing
```

Guarde y salga del archivo, usando CTRL+X e Y luego enter, luego reinicie su sistema.

#### Activación de AppArmor para sistemas basados en Ubuntu

Para comprobar si AppArmor está habilitado en su sistema, ejecute el siguiente comando:
```bash
sudo apparmor_status
```


Si AppArmor no está instalado, puede instalarlo utilizando el siguiente comando:
```bash
sudo apt-get install apparmor
```

Para activar AppArmor, es necesario editar el archivo **/etc/default/grub** y añadir el parámetro **security=apparmor** a la variable **GRUB_CMDLINE_LINUX**:

```bash
sudo nano /etc/default/grub
```
**Agregar seguridad=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Guarda y sal del archivo, usando CTRL+X e Y luego enter, luego ejecuta el siguiente comando para actualizar la configuración del cargador de arranque de tu sistema:

```bash
sudo update-grub
```

Por último, reinicie el sistema.

Una vez habilitados SELinux o AppArmor, puedes configurar sus políticas para restringir los privilegios de los procesos y limitar su acceso a los recursos del sistema. Esto puede ayudar a minimizar el impacto potencial de un ataque exitoso y mejorar la seguridad general de su sistema.


### Configurar políticas de contraseñas

Configurar políticas de contraseñas es un paso importante para reforzar la seguridad de su sistema Linux. Mediante la aplicación de fuertes requisitos de contraseña, puede asegurarse de que las cuentas de usuario son seguras y están protegidas contra posibles ataques. A continuación se explica cómo configurar políticas de contraseñas en su sistema Linux:

#### Configuración de políticas de contraseñas en Ubuntu

Para configurar políticas de contraseñas en Ubuntu, puede utilizar el módulo **pam_pwquality**. Este módulo proporciona un conjunto de comprobaciones de la seguridad de las contraseñas que se pueden utilizar para aplicar políticas de contraseñas. Para instalar el módulo **pam_pwquality**, abra una ventana de terminal y escriba:

```bash
sudo apt-get install libpam-pwquality
```

Una vez instalado el módulo, puede configurar sus parámetros editando el archivo **/etc/pam.d/common-password**. Por ejemplo, para imponer una longitud mínima de contraseña de 8 caracteres y requerir al menos una letra mayúscula, una letra minúscula, un dígito y un carácter especial, puede añadir la siguiente línea al archivo:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

También puede configurar otros parámetros, como la antigüedad máxima de la contraseña, añadiendo líneas al archivo.

#### Configuración de políticas de contraseñas en CentOS

Para configurar políticas de contraseñas en CentOS, puede utilizar la herramienta **authconfig**. Esta herramienta proporciona un conjunto de opciones que se pueden utilizar para configurar las políticas de contraseñas. Por ejemplo, para imponer una longitud mínima de contraseña de 8 caracteres y requerir al menos una letra mayúscula, una letra minúscula, un dígito y un carácter especial, puede utilizar el siguiente comando:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Esto actualizará los archivos **/etc/pam.d/system-auth** y **/etc/pam.d/password-auth** del sistema para aplicar las políticas de contraseñas especificadas.

Recuerda revisar y actualizar regularmente tus políticas de contraseñas para asegurarte de que siguen siendo efectivas contra posibles ataques.


### Monitorice los registros de su sistema

Monitorizar los registros del sistema es un aspecto importante para mantener la seguridad de tu sistema Linux. Los registros del sistema registran la actividad del sistema, como intentos fallidos de inicio de sesión, errores y otros eventos importantes, y pueden proporcionar información valiosa sobre posibles amenazas a la seguridad u otros problemas que requieren atención. A continuación se explica cómo monitorizar los registros del sistema:

#### Usando el comando journalctl

En la mayoría de las distribuciones modernas de Linux, puede utilizar el comando **journalctl** para ver los registros del sistema. Este comando proporciona una variedad de opciones que se pueden utilizar para filtrar y buscar entradas de registro.

Para ver todas las entradas de registro, simplemente ejecute el siguiente comando:

```bash
sudo journalctl
```

Esto mostrará todas las entradas de registro, con las más recientes en la parte inferior.

Para filtrar las entradas de registro por una unidad específica, como un servicio o un proceso, puede utilizar la opción **-u** seguida del nombre de la unidad. Por ejemplo, para ver las entradas de registro del servicio **sshd**, puede ejecutar el siguiente comando:
```bash
sudo journalctl -u sshd
```


Para filtrar las entradas de registro por un intervalo de tiempo específico, puede utilizar las opciones **--desde** y **--hasta** seguidas de una marca de tiempo o intervalo de tiempo. Por ejemplo, para ver las entradas de registro de la última hora, puede ejecutar el siguiente comando:

```bash
sudo journalctl --since "1 hour ago"
```

#### Utilizar una herramienta de gestión de registros

Para sistemas más grandes o complejos, puede ser útil utilizar una herramienta de gestión de registros para recopilar y analizar los registros del sistema. Las herramientas de gestión de registros pueden proporcionar funciones avanzadas, como la supervisión de registros en tiempo real, la agregación de registros y el análisis de registros, y pueden ayudarle a identificar y responder a posibles amenazas de seguridad de forma más eficaz.

Algunos ejemplos de herramientas de gestión de registros para Linux son:

- **Logwatch**: una sencilla herramienta de análisis de registros que proporciona resúmenes diarios por correo electrónico de los registros del sistema.
- Logrotate**: una herramienta que rota y comprime automáticamente los archivos de registro para conservar espacio en disco.
- ELK stack**: una popular herramienta de gestión de registros de código abierto que combina Elasticsearch, Logstash y Kibana para proporcionar capacidades de monitorización y análisis de registros en tiempo real.

Recuerde revisar y analizar regularmente los registros de su sistema para detectar y responder a las posibles amenazas de seguridad de manera oportuna.

______

## No hacer:

### Usar contraseñas débiles

Usar contraseñas débiles es un error común que puede dejar su sistema Linux vulnerable a ataques. Los atacantes pueden utilizar herramientas para adivinar contraseñas basadas en palabras comunes, nombres o fechas. Es importante utilizar contraseñas fuertes y únicas que no sean fáciles de adivinar.

Puedes crear contraseñas seguras utilizando una combinación de letras mayúsculas y minúsculas, números y caracteres especiales. También es una buena práctica utilizar una [password manager](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) también puede ayudarte a recordar tus contraseñas y evitar que utilices la misma contraseña para varias cuentas.

### Permitir acceso root SSH

Permitir el acceso root SSH es un riesgo de seguridad que puede dar a los atacantes el control completo sobre su sistema Linux. En su lugar, debe utilizar una cuenta de usuario no root para iniciar sesión en su sistema y luego elevar los privilegios utilizando el comando **sudo**. Esto ayuda a limitar el impacto potencial de un ataque al restringir los privilegios de las cuentas de usuario.

### Instalar software innecesario

Instalar software innecesario puede incrementar la superficie de ataque de su sistema Linux, haciéndolo más vulnerable a ataques. Es importante instalar sólo el software necesario para su sistema y eliminar cualquier software innecesario. Esto ayuda a reducir el número de vulnerabilidades potenciales en su sistema y minimiza el riesgo de un ataque exitoso.

### Usar software obsoleto

El uso de software obsoleto puede hacer que su sistema sea vulnerable a ataques que aprovechan vulnerabilidades conocidas. Es importante utilizar siempre la última versión del software y actualizarlo periódicamente para garantizar la seguridad. Esto ayuda a parchear vulnerabilidades conocidas y a proteger su sistema frente a posibles ataques.

______

## Conclusión

En conclusión, reforzar tu sistema Linux es fundamental para garantizar su seguridad y proteger los datos que contiene. Siguiendo las recomendaciones de este artículo, puedes tomar medidas importantes para asegurar tu sistema y reducir el riesgo de ciberamenazas. Recuerda mantener siempre actualizado tu sistema, utilizar un cortafuegos, configurar políticas de contraseñas y controlar los registros del sistema. Evita utilizar contraseñas débiles, desactivar las actualizaciones automáticas, permitir el acceso root SSH, instalar software innecesario y utilizar software obsoleto. Con estas buenas prácticas en mente, puedes asegurarte de que tu sistema Linux permanece seguro y protegido.

## Referencias:

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)
