---
title: "Introducción a Ansible: Automatización de la gestión de la infraestructura de TI"
draft: false
toc: true
date: 2023-02-25
descripción: "Aprende los fundamentos de Ansible, una herramienta de automatización de código abierto que simplifica la gestión de la infraestructura de TI a través de un lenguaje declarativo."
tags: ["Ansible", "infraestructura TI", "automatización", "gestión de configuración", "despliegue de aplicaciones", "aprovisionamiento", "entrega continua", "cumplimiento de seguridad", "orquestación", "YAML", "módulos", "roles", "buenas prácticas", "control de versiones", "pruebas", "Red Hat", "administradores de sistemas", "Linux", "macOS", "Windows"].
cover: "/img/cover/A_cartoon_character_sitting_at_a_desk_surrounded_by_servers.png"
coverAlt: "Un personaje de dibujos animados sentado en un escritorio, rodeado de servidores y cables, con el logotipo de Ansible en la pantalla del ordenador, sonriendo mientras se automatizan tareas."
coverCaption: ""
---
```bash
sudo apt-get update
sudo apt-get install ansible -y
```
```bash
ansible --version
```
``ini
[webservers]
webserver1.ejemplo.com
servidor2.ejemplo.com

[bases de datos]
dbserver1.ejemplo.com
dbserver2.ejemplo.com
```
```yml
nombre: Instalar Nginx
hosts: servidores web
become: yes

tareas:
    - name: Instalar paquete Nginx
        apt
        nombre: nginx
        estado: presente
```
```
roles/
└── nginx/
    ├── tasks/
    │├── main.yml
    ├── handlers/
    │├── main.yml
    ├── plantillas/
    │ ├── nginx.conf.j2
    ├── archivos/
    ├── vars/
    ├── defaults/
    ├── meta/
```
``yaml
---
- name: Instalar Nginx
  apt:
    nombre: nginx
    estado: presente
  notificar: reiniciar nginx

- nombre: Enable Nginx
  systemd
    nombre: nginx
    habilitado: yes
    estado: iniciado
```

Esta tarea instala Nginx usando el módulo apt y habilita e inicia el servicio Nginx usando el módulo systemd. También notifica al gestor de reinicio de nginx, que reiniciará Nginx si se ha realizado algún cambio en la configuración.

El uso de un rol Ansible como este puede simplificar el proceso de gestión y configuración de software a través de múltiples servidores o entornos. Al separar las tareas, manejadores, plantillas y otros recursos en una única estructura de directorios, puedes gestionar y reutilizar más fácilmente estos componentes en diferentes playbooks y proyectos.

## Mejores prácticas para Ansible

Estas son algunas de las mejores prácticas a seguir cuando se utiliza Ansible:

### 1. Usar control de versiones

Almacenar tus playbooks y roles de Ansible en un sistema de control de versiones como Git es una buena práctica que puede ayudarte a realizar un seguimiento de los cambios y colaborar con otros. El control de versiones proporciona un historial de los cambios realizados en su código base, lo que le permite volver a versiones anteriores si es necesario. También facilita la colaboración con otras personas compartiendo código y gestionando conflictos.

### 2. Utiliza roles para organizar tus guías

Los roles son una poderosa forma de organizar tus playbooks y tareas Ansible. Agrupando tareas relacionadas en roles, puedes hacer tus playbooks más modulares y reutilizables. Los roles también facilitan compartir código entre diferentes proyectos.

Aquí hay un ejemplo de un libro de jugadas que utiliza un rol para instalar y configurar Nginx:

```yml
name: Instalar y configurar Nginx
hosts: servidores web
become: yes
roles:
  - nginx
```

Este playbook utiliza un rol llamado "nginx" para instalar y configurar Nginx en el grupo de hosts "webservers".

### 3. Usar etiquetas para agrupar tareas

Las etiquetas se pueden utilizar para agrupar tareas relacionadas entre sí en los playbooks de Ansible. Esto facilita la ejecución de partes específicas de un playbook, especialmente cuando se trabaja con playbooks grandes y complejos.

A continuación se muestra un ejemplo de cómo utilizar etiquetas en un playbook de Ansible:
```yml
name: Instalar y configurar Nginx
hosts: webservers
become: yes
tasks:
  - name: Instalar Nginx
    apt:
    nombre: nginx
    estado: presente
    etiquetas: nginx_install

  - name: Configurar Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    tags: nginx_config
```

Este playbook tiene dos tareas, una para instalar Nginx y otra para configurarlo. Cada tarea tiene una etiqueta asociada, lo que facilita la ejecución de sólo las tareas necesarias.

### 4. Utilizar variables para hacer más flexibles los playbooks

Las variables se pueden utilizar para hacer sus playbooks Ansible más flexibles y reutilizables. Mediante el uso de variables, puede hacer que sus playbooks sean más genéricos y adaptables a diferentes entornos.

He aquí un ejemplo de cómo utilizar variables en un libro de reproducción de Ansible:
```yml
name: Instalar y configurar Nginx
hosts: webservers
become: yes

vars:
nginx_port: 80
nginx_user: www-data

tasks:
  - name: Instalar Nginx
    apt
    nombre: nginx
    estado: presente
  - nombre: Configurar Nginx
    plantilla:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    notify: reiniciar nginx

handlers:
  - nombre: reiniciar nginx
    servicio:
    nombre: nginx
    estado: reiniciado
```

Este playbook utiliza variables para especificar el puerto en el que Nginx debe escuchar y el usuario que debe ejecutar Nginx. Esto hace que el playbook sea más flexible y adaptable a diferentes entornos.

### 5. Pruebe sus Playbooks

Probar tus playbooks de Ansible es una buena práctica que puede ayudarte a detectar errores y asegurar que tus playbooks funcionan como se espera. Molecule es una herramienta muy popular para probar los playbooks de Ansible.

Molecule es un marco de pruebas que permite probar los libros de reproducción de forma coherente y automatizada. Molecule puede crear máquinas virtuales, aplicar su playbook, y luego verificar que todo está funcionando como se esperaba. Esto puede ayudarle a detectar errores y asegurarse de que sus libros de jugadas funcionan correctamente antes de desplegarlos en producción.

He aquí un ejemplo de cómo utilizar Molecule para probar un rol de Ansible:

```bash
molecule init role myrole
cd mi rol
molecule test
```

## Conclusión

En este artículo hemos presentado Ansible, una potente herramienta de automatización que puede ayudarte a gestionar infraestructuras de TI complejas. Hemos cubierto los conceptos básicos de Ansible, incluyendo inventarios, playbooks, módulos y roles.

También hemos discutido las mejores prácticas para el uso de Ansible, incluyendo el uso de control de versiones, la organización de playbooks con roles, el uso de etiquetas y variables, y la prueba de sus playbooks.

Si eres nuevo en Ansible, te recomendamos que empieces experimentando con algunos playbooks sencillos y que aumentes gradualmente tus habilidades y conocimientos con el tiempo. Con la práctica, serás capaz de automatizar incluso las tareas de infraestructura más complejas con facilidad.


 Ansible es una herramienta de automatización de código abierto que permite a los administradores de sistemas automatizar la gestión de la infraestructura informática. Ofrece un lenguaje sencillo para describir el estado deseado de la infraestructura y aplicarlo automáticamente. Esto reduce el tiempo y los esfuerzos necesarios para gestionar sistemas complejos a gran escala.
 
 Si eres nuevo en Ansible, este artículo te ofrece una introducción a la herramienta, sus conceptos básicos y cómo empezar a utilizarla.
 
 ## Introducción a Ansible
 
 Ansible fue desarrollado por Michael DeHaan en 2012 y adquirido por Red Hat en 2015. Desde entonces, se ha convertido en una de las herramientas de automatización más populares del sector.
 
 Ansible utiliza un lenguaje declarativo sencillo llamado YAML (abreviatura de "YAML Ain't Markup Language") para definir el estado deseado de la infraestructura. Es fácil de leer y comprender, incluso para los no programadores.
 
 Ansible puede utilizarse para automatizar un gran número de tareas, entre las que se incluyen :
 
 - Gestión de la configuración
 - Despliegue de aplicaciones
 - Vida útil continua
 - Aprovisionamiento
 - Conformidad de seguridad
 - Organización
 
 ## Premier pas avec Ansible
 
 Para trabajar con Ansible, debe instalarlo en su sistema. Ansible puede instalarse en una amplia gama de sistemas operativos, como Linux, macOS y Windows.
 
 Para instalar Ansible en Linux, en este caso Ubuntu, puedes utilizar los siguientes comandos :
 Sin embargo, puede utilizar las siguientes guías para instalar Ansible :
 - Instalación de Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
 - Guía de instalación] (https://docs.ansible.com/ansible/latest/installation_guide/index.html)
 
 Una vez instalado Ansible, puede comprobar que funciona ejecutando el siguiente comando :
 
 Debe mostrar la versión de Ansible que tiene instalada.
 
 ## Crear Ansible
 
 La primera etapa en el uso de Ansible consiste en definir un inventario. Un inventario es una lista de servidores generada por Ansible. Puede definirse en varios formatos, como INI, YAML y JSON.
 
 Este es un ejemplo de un fichero de inventario en formato INI :
 
 
 Este fichero de inventario define dos grupos de servidores, "servidores web" y "bases de datos", y contiene los nombres de los servidores de cada grupo.
 
 ## Libros Ansibles
 
 Una vez que hayas definido un invento, la siguiente etapa consiste en definir un libro de jugadas. Un playbook es un fichero YAML que describe un conjunto de tareas que Ansible debe realizar en los servidores del invento.
 
 Este es un ejemplo de playbook simple :
 
 Este playbook instala el servidor web Nginx en todos los servidores del grupo "webservers".
 
 El parámetro `hosts` especifica en qué grupo de servidores debe aplicarse el playbook. El parámetro `devient` especifica que las tareas deben ejecutarse con privilegios elevados (usando `sudo` o `su`).
 
 La sección "tareas" describe las tareas individuales que debe realizar el libro de jugadas. En este caso, sólo hay una tarea, que instala el paquete Nginx con ayuda del módulo `apt`.
 
 ## Módulos Ansibles
 
 Los módulos Ansible son unidades de código reutilizables que pueden usarse para realizar tareas específicas. Ansible viene con una amplia gama de módulos integrados, y también hay disponibles muchos módulos adicionales.
 
 Vea algunos ejemplos de módulos integrados:
 
 - `apt` - Para gestionar los paquetes de los sistemas basados en Debian
 - `yum` - Genera los paquetes de los sistemas basados en Red Hat
 - `fichier` - Generar ficheros
 - `service` - Gestiona los servicios del sistema
 - Usuario - Generar usuarios y grupos
 - Copiar` - Copiar los ficheros de la máquina de control a los servidores gestionados
 
 Puede encontrar una lista completa de los módulos integrados en la [documentación de Ansible](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html).
 
 ## Funciones de Ansible y estructura de expedientes
 
 Un rol Ansible es una forma de organizar y reutilizar tareas y configuraciones actuales. Se trata de una estructura de informes que contiene tareas, gestores, modelos, archivos y otros recursos.
 
 Este es un ejemplo sencillo de cómo instalar y configurar Nginx con Ansible:
 En este ejemplo, el rol nginx es un directorio que contiene varios sub-repertorios, cada uno sirviendo a un objetivo específico:
 
 - Tareas: contiene las tareas que realiza el servidor.
 - Manejadores: contiene los manejadores que los procesos pueden notificar.
 - Plantillas: los modelos Jinja2 que se utilizarán para crear los ficheros de configuración de Nginx.
 - Ficheros** : todos los ficheros de estadísticas necesarios para el sistema.
 - Variables: variables específicas del rol.
 - **defaults** : contiene las variables por defecto del rol.
 - Meta: funciones necesarias para el rol, como sus dependencias.
 
 Los roles pueden ser fácilmente compartidos y reutilizados en varios libros de jugadas y proyectos.
 
 Vea un ejemplo del archivo main.yml en la lista de tareas :
