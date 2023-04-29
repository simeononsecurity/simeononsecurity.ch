---
title: "Essential Do's and Don'ts for Hardening Your Linux System"
date: 2023-02-28
toc: true
draft: false
description: "Learn the essential dos and donts for hardening your Linux system, including updating, using firewalls, enabling SELinux or AppArmor, configuring password policies, and monitoring system logs."
tags: ["Linux security", "system hardening", "firewall", "SELinux", "AppArmor", "password policy", "system updates", "system logs", "security modules", "access control policies", "cybersecurity", "system security", "network security", "vulnerability management", "security best practices", "IT security", "information security", "software updates", "root access", "password manager"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "A cartoon lock holding a shield with the word Linux on it, while an arrow bounces off the shield."
coverCaption: ""
---
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade

```
```bash
sudo yum update
```
```bash
sudo yum autoremove
```
```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```
```bash
sudo ufw allow http
```
```bash
sudo ufw deny from <ip_address>
```
```bash
sudo ufw delete <rule_number>
```
```bash
sudo ufw status
```
```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```
```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --list-all
```
```bash
sestatus
```
```bash
sudo yum install selinux-policy selinux-policy-targeted
```
```bash
sudo nano /etc/selinux/config
```
```
SELINUX=enforcing
```
```bash
sudo apparmor_status
```
```bash
sudo apt-get install apparmor
```
```bash
sudo nano /etc/default/grub
```
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```
```bash
sudo update-grub
```
```bash
sudo apt-get install libpam-pwquality
```
```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```
```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```
```bash
sudo journalctl
```
```bash
sudo journalctl -u sshd
```
```bash
sudo journalctl --since "1 hour ago"
```

  Linux es un sistema operativo popular utilizado tanto por personas como por empresas. Si bien a menudo se considera más seguro que otros sistemas operativos debido a su naturaleza de código abierto, aún requiere un refuerzo adecuado para garantizar la seguridad del sistema y los datos que contiene. En este artículo repasaremos algunas cosas que se deben y no se deben hacer en el fortalecimiento general que pueden ayudar a mantener seguro su sistema Linux.  ## Qué hacer:  ### Mantenga su sistema actualizado  Mantener su sistema [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) actualizado es crucial para mantener su seguridad. Las actualizaciones periódicas ayudan a corregir las vulnerabilidades y los errores de seguridad, lo que garantiza que su sistema permanezca seguro contra posibles ataques. Estos son algunos ejemplos de cómo actualizar su sistema Linux usando el administrador de paquetes **apt-get** o **yum**:  #### Actualización de Ubuntu usando apt-get  Para actualizar su sistema Ubuntu usando **apt-get**, abra una ventana de terminal y escriba:  Esto descargará las últimas listas de paquetes de los repositorios de paquetes de Ubuntu. Una vez que se complete este comando, puede instalar cualquier actualización disponible usando el siguiente comando:   Esto descargará e instalará las actualizaciones disponibles para su sistema.  ### Actualizando CentOS usando yum  Para actualizar su sistema CentOS usando **yum**, abra una ventana de terminal y escriba:   Esto descargará e instalará las actualizaciones disponibles para su sistema. También es posible que desee utilizar el siguiente comando para limpiar los paquetes antiguos o no utilizados:   Esto eliminará cualquier paquete que ya no sea necesario en su sistema.  Recuerde verificar e instalar actualizaciones periódicas en su sistema Linux para garantizar su seguridad y estabilidad.   ### Usa un cortafuegos  Un firewall es una medida de seguridad esencial para cualquier sistema Linux, ya que ayuda a proteger contra el acceso no autorizado y otras amenazas cibernéticas. Aquí se explica cómo usar el cortafuegos **ufw** en su sistema Linux:  #### Instalación y habilitación de ufw para sistemas basados en Ubuntu  Para instalar y habilitar **ufw**, abra una ventana de terminal y escriba:   Para permitir el trafico HTTP entrante (puerto 80):   Para bloquear el tráfico entrante desde una dirección IP específica:   Para eliminar una regla:  Puede ver las reglas **ufw** actualmente escribiendo:    Esto muestra las reglas actuales y su estado.  Recuerde revisar y actualizar periódicamente sus reglas de **ufw** para asegurarse de que su sistema esté protegido contra posibles amenazas.   #### Instalación y activación de firewalld para sistemas basados en CentOS  Para instalar y habilitar el firewall predeterminado en CentOS, que es **firewalld**, puede usar los siguientes comandos:   Esto instalará **firewalld** y lo habilitará en su sistema.  #### Configuración de reglas de firewalld para sistemas basados en CentOS  Una vez que **firewalld** está habilitado, puede configurar sus reglas para permitir o bloquear el tráfico entrante y saliente. Aquí hay unos ejemplos:  Para permitir el tráfico SSH entrante (puerto 22):   Para permitir el trafico HTTP entrante (puerto 80):   Para bloquear el tráfico entrante desde una dirección IP específica:   Para eliminar una regla:   Puede ver las reglas actuales de **firewalld** escribiendo:   Esto muestra las reglas actuales y su estado.  Recuerde revisar y actualizar periódicamente sus reglas de **firewalld** para asegurarse de que su sistema  ### Habilitar SELinux o AppArmor  SELinux (Linux con seguridad mejorada) y AppArmor son dos módulos de seguridad que se pueden usar para hacer cumplir las políticas de control de acceso obligatorias en los sistemas Linux. De forma predeterminada, la mayoría de las distribuciones de Linux modernas vienen con SELinux o AppArmor instalados, y se pueden habilitar y configurar para mejorar la seguridad de su sistema.  #### Habilitación de SELinux para sistemas basados en CentOS  Para verificar si SELinux está habilitado en su sistema, ejecute el siguiente comando:   Si SELinux no está instalado, puede instalarlo usando el siguiente comando:   Para habilitar SELinux, debe editar el archivo **/etc/selinux/config** y configurar la variable **SELINUX** para **hacer cumplir**:  **Cambiar SELINUX=aplicar**  Guarde y salga del archivo, usando CTRL+X e Y, luego ingrese, luego reinicie su sistema.  #### Habilitación de AppArmor para sistemas basados en Ubuntu  Para verificar si AppArmor está habilitado en su sistema, ejecute el siguiente comando:   Si AppArmor no está instalado, puede instalarlo con el siguiente comando:  Para habilitar AppArmor, debe editar el archivo **/etc/default/grub** y agregar el parámetro **security=apparmor** a la variable **GRUB_CMDLINE_LINUX**:  **Añadir seguridad=equipo**  Guarde y salga del archivo, usando CTRL+X e Y, luego ingrese, luego ejecute el siguiente comando para actualizar la configuración del gestor de arranque de su sistema:   Finalmente, reinicie su sistema.  Una vez que SELinux o AppArmor estén habilitados, puede configurar sus políticas para restringir los privilegios de los procesos y limitar su acceso a los recursos del sistema. Esto puede ayudar a minimizar el impacto potencial de un ataque exitoso y mejorar la seguridad general de su sistema.   ### Configurar políticas de contraseñas  La configuración de políticas de contraseñas es un paso importante para fortalecer la seguridad de su sistema Linux. Al cumplir con los requisitos de contraseña segura, puede asegurarse de que las cuentas de usuario estén seguras y protegidas contra posibles ataques. Aquí le mostramos cómo configurar políticas de contraseña en su sistema Linux:  #### Configuración de políticas de contraseñas en Ubuntu  Para configurar políticas de contraseñas en Ubuntu, puede usar el módulo **pam_pwquality**. Este módulo proporciona un conjunto de comprobaciones de seguridad de contraseñas que se pueden utilizar para hacer cumplir las políticas de contraseñas. Para instalar el módulo **pam_pwquality**, abra una ventana de terminal y escriba:   Una vez que el módulo está instalado, puede configurar sus ajustes editando el archivo **/etc/pam.d/common-password**. Por ejemplo, para aplicar una longitud mínima de contraseña de 8 caracteres y requiere al menos una letra mayúscula, una letra minúscula, un dígito y un carácter especial, puede agregar la siguiente línea al archivo:   También puede configurar otras definiciones, como la antigüedad máxima de la contraseña, agregando líneas al archivo.  #### Configuración de políticas de contraseñas en CentOS  Para configurar políticas de contraseñas en CentOS, puede usar la herramienta **authconfig**. Esta herramienta proporciona un conjunto de opciones que se pueden utilizar para configurar políticas de contraseñas. Por ejemplo, para aplicar una longitud mínima de contraseña de 8 caracteres y requiere al menos una letra mayúscula, una letra minúscula, un dígito y un carácter especial, puede usar el siguiente comando:   Esto actualizará los archivos **/etc/pam.d/system-auth** y **/etc/pam.d/password-auth** del sistema para aplicar las políticas de contraseña especificadas.  Recuerde revisar y actualizar periódicamente sus políticas de contraseñas para asegurarse de que sigan siendo efectivas contra posibles ataques.   ### Supervisar los registros de su sistema  Supervisar los registros de su sistema es un aspecto importante para mantener la seguridad de su sistema Linux. Los registros del sistema registran la actividad del sistema, como intentos de inicio de sesión fallidos, errores y otros eventos importantes, y pueden proporcionar información valiosa sobre posibles amenazas a la seguridad u otros problemas que requieren atención. Aquí le mostramos cómo monitorear los registros de su sistema:  #### usando el comando journalctl  En la mayoría de las distribuciones modernas de Linux, puede usar el comando **journalctl** para ver los registros del sistema. Este comando proporciona una variedad de opciones que se pueden usar para filtrar y buscar entradas de registro.  Para ver todas las entradas de registro, simplemente ejecute el siguiente comando:   Esto muestra todas las entradas del registro, con las entradas más recientes en la parte inferior.  Para filtrar las entradas de registro por una unidad específica, como un servicio o un proceso, puede usar la opción **-u** seguida del nombre de la unidad. Por ejemplo, para ver las entradas de registro del servicio **sshd**, puede ejecutar el siguiente comando:   Para filtrar las entradas del registro por un rango de tiempo específico, puede usar las opciones **--since** y **--until** seguidas de una marca de tiempo o rango de tiempo. Por ejemplo, para ver las entradas de registro de la última hora, puede ejecutar el siguiente comando:   #### Uso de una herramienta de gestión de registros  Para sistemas más grandes o más complejos, puede ser útil usar una herramienta de administración de registros para recopilar y analizar los registros del sistema. Las herramientas de administración de registros pueden proporcionar funciones avanzadas, como monitoreo de registros en tiempo real, agregación de registros y análisis de registros, y pueden ayudar a identificar y responder a posibles amenazas de seguridad de manera más eficiente.  Los ejemplos de herramientas de administración de registros para Linux incluyen:  - **Logwatch**: una sencilla herramienta de análisis de registros que proporciona resúmenes diarios por correo electrónico de los registros del sistema - **Logrotate**: una herramienta que gira y comprime automáticamente los archivos de registro para ahorrar espacio en disco - **ELK stack**: una popular herramienta de administración de registros de código abierto que combina Elasticsearch, Logstash y Kibana para brindar capacidades de monitoreo y análisis de registros en tiempo real  Recuerde revisar y analizar periódicamente los registros de su sistema para detectar y responder a amenazas de seguridad de manera oportuna posibles.  ______  ## No hacer:  ### Usa contraseñas débiles  El uso de contraseñas débiles es un error común que puede dejar su sistema Linux vulnerable a los ataques. Los atacantes pueden usar herramientas para adivinar contraseñas que se basan en palabras, nombres o fechas comunes. Es importante utilizar contraseñas seguras y únicas que no sean fáciles de adivinar.  Puede crear contraseñas seguras usando una combinación de letras mayúsculas y minúsculas, números y caracteres especiales. También es una buena práctica usar un [administrador de contraseñas](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) para generar y almacenar contraseñas complejas de forma segura. [Administradores de contraseñas](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) también pueden ayudar a recordar sus contraseñas y evitar usar la misma contraseña para varias cuentas.  ### Permitir acceso SSH raíz  Permitir el acceso SSH raíz es un riesgo de seguridad que puede dar a los atacantes un control total sobre su sistema Linux. En su lugar, debe usar una cuenta de usuario que no sea root para iniciar sesión en su sistema y luego elevar los privilegios usando el comando **sudo**. Esto ayuda a limitar el impacto potencial de un ataque al restringir los privilegios de las cuentas de usuario.  ### Instalar software necesario  La instalación de software necesaria puede aumentar la superficie de ataque de su sistema Linux, haciéndolo más vulnerable a los ataques. Es importante instalar solo el software que sea necesario para su sistema y eliminar cualquier software necesario. Esto ayuda a reducir la cantidad de vulnerabilidades potenciales en su sistema y minimiza el riesgo de un ataque exitoso.  ### Usar software obsoleto  El uso de software obsoleto puede hacer que su sistema sea vulnerable a ataques que exploten vulnerabilidades conocidas. Es importante usar siempre la última versión del software y actualizarlo periódicamente para garantizar la seguridad. Esto ayuda a parchear vulnerabilidades conocidas y proteger su sistema contra posibles ataques.  ______  ## Conclusión  En conclusión, fortalecer su sistema Linux es fundamental para garantizar su seguridad y proteger los datos que contiene. Al seguir las recomendaciones que se describen en este artículo, puede tomar medidas importantes para proteger su sistema y reducir el riesgo de ciberamenazas. Recuerda siempre mantener tu sistema actualizado, usar un firewall, configurar políticas de contraseñas y monitorear los registros del sistema. Evite usar contraseñas débiles, deshabilitar las actualizaciones automáticas, permitir el acceso SSH raíz, instalar software necesario y usar software obsoleto. Con estas mejores prácticas en mente, puede asegurarse de que su sistema Linux permanezca seguro y protegido.  ## Referencias:  - [Guía de refuerzo de Linux del Centro para la seguridad en Internet] (https://www.cisecurity.org/cis-hardened-images/) - [Guía de seguridad de Red Hat Enterprise Linux](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index) - [Documentacion de seguridad de Ubuntu](https://ubuntu.com/security) - [Wiki de seguridad de Linux](https://en.wikibooks.org/wiki/Linux_Security)