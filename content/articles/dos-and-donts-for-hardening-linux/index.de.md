---
title: "Qué hacer y qué no hacer esencial para endurecer tu sistema Linux"
date: 2023-02-28
toc: true
draft: false
description: "Aprende lo esencial que debes y no debes hacer para endurecer tu sistema Linux, incluyendo actualizaciones, uso de cortafuegos, habilitación de SELinux o AppArmor, configuración de políticas de contraseñas y monitorización de registros del sistema."
tags: ["seguridad Linux", "endurecimiento del sistema", "cortafuegos", "SELinux", "AppArmor", "política de contraseñas", "actualizaciones del sistema", "registros del sistema", "módulos de seguridad", "políticas de control de acceso", "ciberseguridad", "seguridad del sistema", "seguridad de la red", "gestión de vulnerabilidades", "buenas prácticas de seguridad", "seguridad informática", "seguridad de la información", "actualizaciones de software", "acceso root", "gestor de contraseñas"].
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Un candado de dibujos animados sosteniendo un escudo con la palabra Linux en él, mientras una flecha rebota en el escudo".
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
Bash
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
Bash
sudo ufw deny from <dirección_ip>
```
Bash
sudo ufw delete <número_de_regla>
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
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<dirección_ip>" reject'
sudo firewall-cmd --reload
```
Bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```
Bash
sudo firewall-cmd --list-all
```
Bash
sestatus
```
Bash
sudo yum install selinux-policy selinux-policy-targeted
```
```bash
sudo nano /etc/selinux/config
```
```
SELINUX=forzar
```
Bash
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
``bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```
```bash
sudo journalctl
```
Bash
sudo journalctl -u sshd
```
Bash
sudo journalctl --since "hace 1 hora"
```


 
 Linux es un sistema operativo muy popular, utilizado por empresas e instituciones. Aunque su naturaleza de código abierto lo hace a menudo más seguro que otros sistemas operativos, también ofrece una herramienta para mejorar la seguridad de los sistemas y de los datos que contienen. En este artículo nos centraremos en algunos aspectos generales de la seguridad que le ayudarán a mantener su sistema Linux seguro.
 
 ## Aufgaben:
 
 ### Mantener su sistema en el nivel más reciente
 
 Es importante mantener su sistema [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/)en el nivel más reciente para garantizar su seguridad. Las actualizaciones periódicas ayudan a mantener la seguridad y a evitar problemas, asegurando que su sistema está protegido contra posibles amenazas. Estos son algunos ejemplos de cómo actualizar su sistema Linux con el gestor de paquetes **apt-get** o **yum**:
 
 #### Actualizar Ubuntu con apt-get
 
 Para actualizar su sistema Ubuntu con **apt-get**, abra un terminal y haga lo siguiente:
 
 A continuación se mostrarán las listas de paquetes más recientes de los repositorios de paquetes de Ubuntu. Si este problema no se ha solucionado, puede instalar todas las actualizaciones con la siguiente instalación:
 
 
 Por favor, descargue e instale todas las actualizaciones disponibles para su sistema.
 
 ### Aktualisieren von CentOS mit lecker
 
 Para actualizar su sistema CentOS con **yum**, abra un terminal y haga lo siguiente:
 
 
 A continuación se mostrarán e instalarán todas las actualizaciones disponibles para su sistema. También puede utilizar el siguiente símbolo para eliminar los paquetes antiguos o que no utilice:
 
 
 Por lo tanto, se eliminarán todas las tarjetas que no estén disponibles en el sistema.
 
 Asegúrese de recibir actualizaciones periódicas para su sistema Linux e instalarlas para mejorar su seguridad y estabilidad.
 
 
 ### Verwenden Sie eine Firewall
 
 Un cortafuegos es una medida de seguridad obligatoria para cualquier sistema Linux, ya que protege contra ataques no autorizados y otras amenazas cibernéticas. También puede utilizar SIE **ufw**-Firewall en su sistema Linux:
 
 #### ufw für Ubuntu-basierte Systeme installieren und aktivieren
 
 Para instalar y activar **ufw**, abre un terminal y escribe lo siguiente:
 
 
 De este modo, podrá acceder a la conexión de datos HTTP (puerto 80):
 
 
 Para bloquear la entrada de datos de una dirección IP diferente:
 
 
 Así se cancela una regla:
 
 SIE kann die aktuellen **ufw**-Regeln anzeigen, gibt SIE dafür Folgendes ein:
 
 
 
 A continuación se muestran las normas actuales y su estado.
 
 SIE DARAN, Ihre **ufw**-Regeln regelmäßig zu denken und zu aktualisieren, um sicherzustellen, dass Ihr System vor potenziellen Bedrohungen geschützt ist.
 
 
 #### Firewalld para sistemas basados en CentOS instalar y activar
 
 Para instalar y activar el cortafuegos estándar **firewalld** de CentOS, puede seguir estos pasos:
 
 
 Instale **firewalld** y actívelo en su sistema.
 
 #### Configuración de cortafuegos para sistemas basados en CentOS
 
 Cuando **firewalld** está activado, el SIE puede configurar sus reglas para bloquear o eliminar el tráfico de datos entrante y saliente. Estos son algunos ejemplos:
 
 Así podrá acceder a la conexión de datos SSH (Puerto 22):
 
 
 Para acceder a los datos HTTP (Puerto 80):
 
 
 Para bloquear la entrada de datos de una dirección IP diferente:
 
 
 Así se cancela una regla:
 
 
 Puede consultar los últimos **firewalld**-Regeln, a continuación, seleccione SIE Folgendes ein:
 
 
 A continuación, se muestran las normas actuales y su estado.
 
 SIE DARAN, Ihre **firewalld**-Regeln zu Denken regelmäßig zu überprüfen und zu aktualisieren, um sicherzustellen, dass Ihr System
 
 ### Aktivieren Sie SELinux or AppArmor
 
 SELinux (Security-Enhanced Linux) y AppArmor son dos módulos de seguridad que se pueden utilizar para aplicar las directivas de control de seguridad obligatorias en sistemas Linux. En la mayoría de las distribuciones modernas de Linux se instalan SELinux o AppArmor, que pueden activarse y configurarse para mejorar la seguridad del sistema.
 
 #### Activación de SELinux para sistemas basados en CentOS
 
 Siga estos pasos para saber si SELinux está activado en su sistema:
 
 
 Si SELinux no está instalado, puede instalarlo con la siguiente configuración:
 
 
 Para activar SELinux, debe cargar la carpeta **/etc/selinux/config** y configurar la variable **SELinux** en **enforcing**:
 
 **Ajuste SELINUX=reforzar**.
 
 Seleccione y verifique los datos con STRG+X e Y, guárdelos y arranque su sistema de nuevo.
 
 #### Activación de AppArmor para sistemas basados en Ubuntu
 
 Siga los siguientes pasos para saber si AppArmor está activado en su sistema:
 
 
 Si el icono de AppArmor no está instalado, puede instalarlo a continuación:
 
 Para activar AppArmor, debe cargar la carpeta **/etc/default/grub** e introducir el parámetro **security=apparmor** en la variable **GRUB_CMDLINE_LINUX**:
 
 **Sicherheit hinzufügen=apparmor**
 
 Introduzca y envíe los datos con STRG+X e Y, guárdelos y haga lo siguiente para actualizar la configuración del cargador de arranque de su sistema:
 
 
 Arranque su sistema de nuevo.
 
 Si SELinux o AppArmor están activados, SIE puede configurar sus parámetros para mejorar las capacidades de los procesos y su acceso a los recursos del sistema. Esto puede ayudar a minimizar los efectos potenciales de una aplicación exitosa y a mejorar la seguridad de su sistema.
 
 
 ### Kennwortrichtlinien konfigurieren
 
 La configuración de las líneas de comandos es un paso importante para mejorar la seguridad de su sistema Linux. Si se establecen requisitos de seguridad muy estrictos, se puede garantizar que los usuarios están protegidos contra posibles amenazas. Para ello, configure las líneas de comandos de su sistema Linux:
 
 #### Cómo configurar las líneas de comandos en Ubuntu
 
 Para configurar las contraseñas en Ubuntu, puede utilizar el módulo **pam_pwquality**. Este módulo proporciona una serie de configuraciones de contraseña que se pueden utilizar para configurar las contraseñas. Para instalar el módulo **pam_pwquality**, abra un terminal y haga lo siguiente:
 
 
 Si ha instalado el módulo, puede configurar sus parámetros y modificar la carpeta **/etc/pam.d/common-password**. Para configurar, por ejemplo, una contraseña mínima de 8 dígitos y, como mínimo, una pestaña grande, una pestaña pequeña, un marcador y una pestaña de respuesta, puede introducir la siguiente secuencia en la base de datos:
 
 
 Sie können auch andere Einstellungen konfiguren, z. B. das maximale Kennwortalter, indem Sie der Datei Zeilen hinzufügen.
 
 #### Configuración de contraseñas en CentOS
 
 Para configurar las contraseñas en CentOS, puede utilizar la herramienta **authconfig**. Esta herramienta proporciona una serie de opciones que se pueden utilizar para configurar las arquitecturas de red. Para configurar, por ejemplo, un ancho de banda de 8 zonas y, como mínimo, una ficha de tabla grande, una ficha de tabla pequeña, un marcador y una ficha de sonido, SIE puede utilizar las siguientes opciones:
 
 
 Se actualizarán los ficheros **/etc/pam.d/system-auth** y **/etc/pam.d/password-auth** de los sistemas, para que se apliquen las reglas de acceso descritas.
 
 Por favor, compruebe y actualice periódicamente sus parámetros de acceso para asegurarse de que están protegidos contra posibles amenazas.
 
 
 ### Überwachen Sie Ihre Systemprotokolle
 
 La seguridad de sus protocolos de sistema es un aspecto importante para la seguridad de sus sistemas Linux. Los protocolos de sistema identifican actividades del sistema tales como errores de funcionamiento, fallos y otros problemas importantes, y pueden proporcionar información útil sobre posibles problemas de seguridad u otros problemas que pueden afectar a la seguridad. Por lo tanto, conozca sus protocolos de sistema:
 
 #### Con la palabra journalctl
 
 En la mayoría de las distribuciones modernas de Linux puede utilizar la función **journalctl** para acceder a los protocolos del sistema. Esta función ofrece una gran variedad de opciones que se pueden utilizar para filtrar y buscar cadenas de protocolos.
 
 Para acceder a todas las funciones de protocolo, basta con pulsar el siguiente botón:
 
 
 A continuación, se mostrarán todas las secuencias de programa, aunque las nuevas secuencias aparecerán completamente abiertas.
 
 Para filtrar entradas de protocolo de un origen distinto, por ejemplo, un destino o un proceso, SIE puede utilizar la opción de bloqueo **-u ** más allá del nombre del origen. Por ejemplo, SIE puede seleccionar la opción **-u ** para el nombre de la entrada:
 
 
 Para filtrar datos de protocolo en un intervalo de tiempo diferente, puede utilizar las opciones **--seit** y **--until** de una date o intervalo de tiempo. Para ver, por ejemplo, los resultados de la última hora, seleccione lo siguiente:
 
 
 #### Verwenden eines Protokollverwaltungstools
 
 En sistemas grandes o complejos puede ser muy útil utilizar una herramienta de gestión de protocolos para la recopilación y el análisis de protocolos de sistema. Las herramientas de gestión de protocolos pueden ofrecer funciones ampliadas, como la gestión de protocolos en tiempo real, la agregación de protocolos y el análisis de protocolos, y ayudarle a identificar de forma más eficaz los posibles problemas de seguridad y a tomar las medidas oportunas.
 
 Los ejemplos de herramientas de gestión de protocolos para Linux son:
 
 - Logwatch**: una sencilla herramienta de análisis de protocolos, que recopila información de los protocolos del sistema en un solo mensaje de correo electrónico.
 - Logrotate**: una herramienta que actualiza y comprime automáticamente los datos de protocolos para ahorrar espacio.
 - ELK-Stack**: Una conocida herramienta de gestión de protocolos de código abierto que combina Elasticsearch, Logstash y Kibana para ofrecer funciones de seguimiento y análisis de protocolos en tiempo real.
 
 Asegúrese de que sus protocolos de sistema se comprueban y analizan de forma periódica, para detectar y corregir posibles problemas de seguridad en todo momento.
 
 ______
 
 ## Verbote:
 
 ### Verwenden Sie schwache Passwörter
 
 El uso de contraseñas no válidas es un error común que puede causar problemas en su sistema Linux. Los usuarios pueden utilizar herramientas para corregir contraseñas que se basan en palabras, nombres o datos personales. Es importante utilizar contraseñas seguras y eficaces que no sean fáciles de descifrar.
 
 Puede crear contraseñas seguras si utiliza una combinación de letras mayúsculas y minúsculas, números y cifras. También es una buena práctica utilizar un [Administrador de contraseñas] (https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) para generar y especificar con seguridad contraseñas complejas. El [Administrador de contraseñas] (https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) también puede ayudarle a combinar sus contraseñas y a verificar que utiliza la misma contraseña para varios contactos.
 
 ### Root-SSH-Zugriff zulassen
 
 La desactivación de la conexión Root-SSH es un riesgo de seguridad que permite a los intrusos tener un control total sobre su sistema Linux. Por lo tanto, SIE debe utilizar una cuenta de usuario que no sea raíz, para poder acceder a su sistema y eliminar las restricciones con la contraseña **sudo**. Se trata, por tanto, de reducir las posibles consecuencias de un ataque, si se han eliminado las opciones de bloqueo de los botones de ayuda.
 
 ### Unnötige Software installieren
 
 La instalación de software inapropiado puede aumentar el ancho de banda de su sistema Linux y hacer que sea más difícil para los usuarios. Es importante que sólo instale software que sea necesario para su sistema y que evite el uso de software inadecuado. Se trata, por tanto, de reducir el número de posibles amenazas en su sistema y minimizar el riesgo de una amenaza exitosa.
 
 ### Verwenden Sie veraltete Software
 
 El uso de software de monitorización puede ayudar a su sistema a mejorar la seguridad de los usuarios. Es importante utilizar siempre la versión más reciente del software y actualizarla periódicamente para mejorar la seguridad. Esto ayuda a evitar errores conocidos y a proteger su sistema de posibles ataques.
 
 ______
 
 ## Inicio
 
 En general, se puede decir que la configuración de su sistema Linux es esencial para mejorar su seguridad y proteger los datos que contiene. Si adopta las medidas y acciones descritas en este artículo, podrá tomar medidas importantes para proteger su sistema y reducir el riesgo de ciberataques. Asegúrese de que su sistema está siempre actualizado, de que utiliza un cortafuegos, de que configura las líneas de comandos y de que supera las protocolos del sistema. Evite el uso de contraseñas fraudulentas, la desactivación de actualizaciones automáticas, la desactivación del acceso Root-SSH, la instalación de software inadecuado y el uso de software obsoleto. Con estas Buenas Prácticas puedes asegurarte de que tu sistema Linux está seguro y protegido.
 
 ## Verweise:
 
 - [Linux Hardening Guide des Center for Internet Security](https://www.cisecurity.org/cis-hardened-images/)
 - Manual de seguridad para Red Hat Enterprise Linux] (https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
 - Documentación sobre seguridad de Ubuntu] (https://ubuntu.com/security)
 - Linux-Sicherheits-Wiki](https://en.wikibooks.org/wiki/Linux_Security)
