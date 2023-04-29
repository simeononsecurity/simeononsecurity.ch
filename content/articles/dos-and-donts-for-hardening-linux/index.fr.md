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


 
 Linux es un sistema de explotación popular utilizado por particulares y empresas. Aunque a menudo se le considera más seguro que otros sistemas de explotación debido a su naturaleza de código abierto, siempre necesita un refuerzo adecuado para garantizar la seguridad del sistema y de los datos que contiene. En este artículo, repasaremos algunas cosas que hay que hacer y que no hay que hacer para reforzar la seguridad de tu sistema Linux.
 
 ## À faire :
 
 ### Maintenez votre système à jour
 
 Mantener su sistema [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) al día es crucial para mantener su seguridad. Unas revisiones periódicas ayudan a corregir las vulnerabilidades y los fallos de seguridad, garantizando que su sistema esté protegido frente a posibles ataques. Vea algunos ejemplos de cómo poner al día su sistema Linux con la ayuda del gestor de paquetes **apt-get** o **yum** :
 
 #### Actualización de Ubuntu con apt-get
 
 Para poner al día tu sistema Ubuntu utilizando **apt-get**, abre una ventana de terminal y selecciona :
 
 Esto descargará las últimas listas de paquetes a partir de las referencias de paquetes de Ubuntu. Una vez que termine este comando, podrá instalar todos los paquetes disponibles mediante el siguiente comando :
 
 
 Esto descargará e instalará todos los paquetes disponibles para su sistema.
 
 ### Actualización de CentOS con yum
 
 Para actualizar su sistema CentOS con **yum**, abra una ventana de terminal y registre :
 
 
 Esto descargará e instalará todas las actualizaciones disponibles para tu sistema. También puedes utilizar el siguiente comando para limpiar todos los paquetes antiguos o en desuso:
 
 
 Esto eliminará todos los paquetes que no sean necesarios en tu sistema.
 
 No dejes de comprobar e instalar regularmente los cambios en tu sistema Linux para asegurar su seguridad y estabilidad.
 
 
 ### Utiliser un pare-feu
 
 Un pare-feu es una medida de seguridad esencial para cualquier sistema Linux, ya que ayuda a protegerse contra accesos no autorizados y otros cibermenazas. Vea cómo utilizar el parámetro **ufw** en su sistema Linux :
 
 #### Instalación y activación de ufw para sistemas basados en Ubuntu
 
 Para instalar y activar **ufw**, abre una ventana de terminal y observa :
 
 
 Para autorizar el tráfico HTTP entrante (puerto 80) :
 
 
 Para bloquear el tráfico entrante desde una dirección IP específica :
 
 
 Para suprimir una regla :
 
 Si desea ver las reglas actuales, haga clic en :
 
 
 
 Aquí se muestran las normas vigentes y su estado.
 
 No deje de consultar y actualizar periódicamente sus normas **ufw** para asegurarse de que su sistema está protegido contra las amenazas potenciales.
 
 
 #### Instalación y activación del pare-feu para sistemas basados en CentOS
 
 Para instalar y activar el pare-feu por defecto en CentOS, que es **firewalld**, puede utilizar los siguientes comandos :
 
 
 Esto instalará **firewalld** y lo activará en tu sistema.
 
 #### Configuración de las reglas de pare-feu para sistemas basados en CentOS
 
 Una vez activado **firewalld**, puedes configurar sus reglas para autorizar o bloquear el tráfico de entrada y salida. Vea algunos ejemplos :
 
 Para autorizar el tráfico SSH entrante (puerto 22) :
 
 
 Para autorizar el tráfico HTTP entrante (puerto 80) :
 
 
 Para bloquear el tráfico entrante desde una dirección IP específica :
 
 
 Para suprimir una regla :
 
 
 Puede consultar las normas **firewalld** vigentes en la actualidad pulsando :
 
 
 Aquí se muestran las normas vigentes y su estado.
 
 No deje de revisar y actualizar periódicamente sus reglas **firewalld** para asegurarse de que su sistema funciona correctamente.
 
 ### Activer SELinux ou AppArmor
 
 SELinux (Security-Enhanced Linux) y AppArmor son dos módulos de seguridad que pueden utilizarse para aplicar políticas de control de acceso obligatorias en los sistemas Linux. De hecho, la mayoría de las distribuciones Linux modernas vienen con SELinux o AppArmor, y pueden activarse y configurarse para mejorar la seguridad de su sistema.
 
 #### Activación de SELinux para sistemas basados en CentOS
 
 Para comprobar si SELinux está activado en su sistema, ejecute el siguiente comando :
 
 
 Si SELinux no está instalado, puede instalarlo con el siguiente comando :
 
 
 Para activar SELinux, debe modificar el archivo **/etc/selinux/config** y definir la variable **SELINUX** en **enforcing** :
 
 **Modificador SELINUX=aplicar**.
 
 Registre y salga del archivo usando CTRL + X e Y y luego entre y vuelva a colocar su sistema.
 
 #### Activación de AppArmor para sistemas basados en Ubuntu
 
 Para comprobar si AppArmor está activado en su sistema, ejecute el siguiente comando :
 
 
 Si AppArmor no está instalado, puede instalarlo con el siguiente comando :
 
 Para activar AppArmor, modifique el archivo **/etc/default/grub** y añada el parámetro **security=apparmor** a la variable **GRUB_CMDLINE_LINUX**:
 
 Añade security=apparmor** a la variable **GRUB_CMDLINE_LINUX**.
 
 Registre y salga del archivo pulsando CTRL+X e Y, registre y desactive el siguiente comando para actualizar la configuración del cargador de arranque de su sistema:
 
 
 Por último, reemplace su sistema.
 
 Una vez activados SELinux o AppArmor, puedes configurar sus políticas para reducir los privilegios de los procesos y limitar su acceso a los recursos del sistema. Esto puede ayudar a minimizar el impacto potencial de un ataque real y a mejorar la seguridad global de su sistema.
 
 
 ### Configurar las políticas de contraseña
 
 La configuración de las políticas de contraseña es un paso importante en el fortalecimiento de la seguridad de su sistema Linux. Aplicando unas estrictas políticas de contraseña, puedes asegurarte de que las cuentas de los usuarios están seguras y protegidas frente a posibles ataques. Vea cómo configurar las estrategias de contraseña en su sistema Linux:
 
 #### Configuración de las políticas de contraseña en Ubuntu
 
 Para configurar las políticas de contraseña en Ubuntu, puede utilizar el módulo **pam_pwquality**. Este módulo proporciona un conjunto de comprobaciones de la fuerza de la contraseña que puede utilizarse para aplicar las políticas de contraseña. Para instalar el módulo **pam_pwquality**, abra la ventana del terminal y seleccione :
 
 
 Una vez instalado el módulo, puede configurar sus parámetros editando el archivo **/etc/pam.d/common-password**. Por ejemplo, para aplicar una longitud mínima de contraseña de 8 caracteres y añadir al menos una letra mayúscula, una letra minúscula, un número y un carácter especial, puede añadir la siguiente línea al fichero :
 
 
 También puede configurar otros parámetros, como la edad máxima de la palabra clave, añadiendo líneas al archivo.
 
 #### Configuración de políticas de contraseña en CentOS
 
 Para configurar las políticas de contraseña en CentOS, puede utilizar la herramienta **authconfig**. Esta herramienta proporciona un conjunto de opciones que pueden utilizarse para configurar las estrategias de contraseña. Por ejemplo, para aplicar una contraseña con una longitud mínima de 8 caracteres y que incluya al menos una letra mayúscula, una letra minúscula, una cifra y un carácter especial, puede utilizar el siguiente comando :
 
 
 Esto actualiza los ficheros **/etc/pam.d/system-auth** y **/etc/pam.d/password-auth** del sistema para aplicar las políticas de contraseña deseadas.
 
 No dejes de revisar y actualizar regularmente tus políticas de contraseña para asegurarte de que siguen siendo eficaces contra los ataques potenciales.
 
 
 ### Surveillez your journaux système
 
 La vigilancia de tu sistema de diarios es un aspecto importante del mantenimiento de la seguridad de tu sistema Linux. Los diarios de sistema registran la actividad del sistema, como los intentos de conexión infructuosos, los errores y otros eventos importantes, y pueden proporcionar información valiosa sobre amenazas potenciales de seguridad u otros problemas que requieran una atención especial. Vea cómo vigilar su sistema de periódicos :
 
 #### Uso del comando journalctl
 
 En la mayoría de las distribuciones Linux modernas, puedes usar el comando **journalctl** para acceder a los diarios del sistema. Este comando proporciona una variedad de opciones que pueden usarse para filtrar y buscar entradas de diarios.
 
 Para mostrar todas las entradas del diario, simplemente desactive el siguiente comando :
 
 
 Se mostrarán todas las entradas del diario, con las más recientes en la parte inferior.
 
 Para filtrar las entradas del diario por una unidad específica, como un servicio o un proceso, puedes utilizar la opción **-u** seguida del nombre de la unidad. Por ejemplo, para mostrar las entradas del diario del servicio **sshd**, puede ejecutar el siguiente comando :
 
 
 Para filtrar las entradas del diario según una hora de llegada específica, puede utilizar las opciones **--depuis** y **--jusqu'à** seguidas de un horodatage o de una hora de llegada. Por ejemplo, para mostrar las entradas del diario de la última hora, puede ejecutar el siguiente comando :
 
 
 #### Utilización de una herramienta de gestión de registros
 
 Para los sistemas más grandes o complejos, puede ser útil utilizar una herramienta de gestión de diarios para recopilar y analizar los diarios del sistema. Las herramientas de gestión de boletines pueden proporcionar funciones avanzadas, como la vigilancia de boletines en tiempo real, la agregación de boletines y el análisis de boletines, y pueden ayudarle a identificar y responder más eficazmente a amenazas de seguridad potenciales.
 
 Vea ejemplos de herramientas de gestión de diarios para Linux :
 
 - Logwatch**: una sencilla herramienta de análisis de diarios que proporciona CVs actualizados por correo electrónico de los diarios del sistema.
 - **Logrotate** : una herramienta que pivota y comprime automáticamente los archivos de los diarios para ahorrar espacio en disco
 - Pile ELK **: una herramienta de gestión de diarios de código abierto popular que combina Elasticsearch, Logstash y Kibana para proporcionar capacidades de vigilancia y análisis de diarios en tiempo real.
 
 No deje de consultar y analizar regularmente su sistema de diarios para detectar y responder a las amenazas de seguridad potenciales en el momento oportuno.
 
 ______
 
 ## À ne pas faire :
 
 ### Utilisez des mots de passe faibles
 
 El uso de palabras clave incorrectas es un error común que puede hacer que su sistema Linux sea vulnerable a ataques. Los atacantes pueden utilizar herramientas para descifrar palabras de paso basadas en palabras, nombres o dates. Es importante utilizar palabras de paso fuertes y únicas que no sean fácilmente descifrables.
 
 Puede crear palabras clave utilizando una combinación de letras mayúsculas y minúsculas, cifras y caracteres especiales. También se recomienda utilizar un [gestor de palabras de paso](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) para generar y almacenar con total seguridad las palabras de paso complejas. Los [gestores de contraseña](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) también pueden ayudarte a recordar tus contraseñas y a evitar que utilices la misma contraseña en varias cuentas.
 
 ### Autorizar el acceso root SSH
 
 Autorizar el acceso root SSH es un riesgo de seguridad que puede dar a los atacantes un control total sobre tu sistema Linux. En lugar de esto, debes usar una cuenta de usuario no root para conectarte a tu sistema, y luego obtener los privilegios con la ayuda del comando **sudo**. Esto permite limitar el impacto potencial de un ataque al restaurar los privilegios de las cuentas de usuario.
 
 ### Installer des logiciels inutiles
 
 La instalación de programas inútiles puede aumentar la superficie de ataque de tu sistema Linux, haciéndolo más vulnerable a los ataques. Es importante que instales sólo los programas necesarios para tu sistema y que elimines todos los programas inútiles. Esto permitirá reducir el número de vulnerabilidades potenciales de su sistema y minimizar el riesgo de un ataque seguro.
 
 ### Utilizar un software obsoleto
 
 El uso de software obsoleto puede hacer que su sistema sea vulnerable a ataques que exploten vulnerabilidades conocidas. Es importante utilizar siempre la última versión del software y actualizarla regularmente para garantizar la seguridad. Esto le permitirá corregir las vulnerabilidades conocidas y proteger su sistema frente a posibles ataques.
 
 ______
 
 ## Conclusión
 
 En conclusión, el reforzamiento de tu sistema Linux es esencial para asegurar su seguridad y proteger los datos que contiene. Siguiendo las pautas descritas en este artículo, puedes tomar medidas importantes para proteger tu sistema y reducir el riesgo de ciberamenazas. No dejes de mantener tu sistema siempre a punto, de utilizar un parche, de configurar políticas de contraseña y de vigilar los diarios del sistema. Evita utilizar contraseñas incorrectas, desactivar los cambios automáticos, autorizar el acceso root SSH, instalar programas inútiles y utilizar programas obsoletos. Con estas buenas prácticas en mente, puedes asegurarte de que tu sistema Linux permanece seguro y protegido.
 
 ## Referencias :
 
 - Guía de seguridad Linux del Centro para la Seguridad en Internet](https://www.cisecurity.org/cis-hardened-images/)
 - Guía de seguridad de Red Hat Enterprise Linux](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
 - Documentación sobre la seguridad de Ubuntu](https://ubuntu.com/security)
 - Wiki de seguridad de Linux](https://en.wikibooks.org/wiki/Linux_Security)
