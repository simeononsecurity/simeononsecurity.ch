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

Este playbook usa un rol llamado "nginx" para instalar y configurar Nginx en el grupo de hosts "webservers".

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

Las variables pueden ser usadas para hacer tus playbooks Ansible más flexibles y reutilizables. Mediante el uso de variables, puede hacer que sus playbooks sean más genéricos y adaptables a diferentes entornos.

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


 Ansible es una herramienta de automatización de código abierto que permite a los administradores de sistemas automatizar la gestión de la infraestructura de TI. Ofrece un lenguaje sencillo para describir el estado deseado de la infraestructura y lo actualiza automáticamente. Esto reduce el trabajo y el tiempo necesarios para gestionar sistemas complejos y de gran tamaño.
 
 Si es nuevo en Ansible, este artículo le ofrece una introducción a la herramienta, incluyendo sus sencillos conceptos y los primeros pasos en su uso.
 
 ## Introducción a Ansible
 
 Ansible fue desarrollado en 2012 por Michael DeHaan y en 2015 por Red Hat. Se ha convertido en una de las herramientas de automatización más utilizadas del sector.
 
 Ansible utiliza un lenguaje sencillo y claro llamado YAML (abreviatura de "YAML Ain't Markup Language") para definir la estructura de la infraestructura. Sin embargo, también es un poco difícil y complicado para los no programadores.
 
 Ansible puede utilizarse para automatizar una gran variedad de tareas, entre las que se incluyen:
 
 - **Gestión de configuraciones**
 - Gestión de aplicaciones
 - Entrega continua
 - Servicio de asistencia técnica
 - Gestión de la seguridad de las instalaciones**
 - Gestión de recursos humanos
 
 ## Erste Schritte mit Ansible
 
 Para empezar con Ansible, debe instalarlo en su sistema. Ansible puede instalarse en una gran variedad de sistemas operativos, incluyendo Linux, macOS y Windows.
 
 Para instalar Ansible en Linux, en este caso Ubuntu, SIE puede utilizar las siguientes funciones:
 Andernfalls can SIE folgende Anleitungen verwenden, um ansible zu installieren:
 - [Ansible installieren](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
 - Manual de instalación](https://docs.ansible.com/ansible/latest/installation_guide/index.html)
 
 Cuando se instala Ansible, SIE puede comprobar si funciona, si SIE sigue el proceso:
 
 Esta es la versión de Ansible que SIE ha instalado.
 
 ## Ansible-Inventar
 
 El primer paso en el uso de Ansible es definir un Inventario. Un Inventario es una lista de servidores que Ansible puede configurar. Un Inventario puede definirse en varios formatos, por ejemplo INI, YAML y JSON.
 
 Este es un ejemplo de un Inventario en formato INI:
 
 
 Esta base de datos define dos grupos de servidores, "Servidor Web" y "Banco de Datos", y lista los nombres de host de los servidores de cada grupo.
 
 ## Ansible-Playbooks
 
 Una vez que ha definido un Inventario, el siguiente paso es definir un Playbook. Un Playbook es un archivo YAML que contiene una serie de tareas que Ansible puede realizar en los servidores del Inventario.
 
 Este es un ejemplo de un Playbook sencillo:
 
 Este Playbook instala el servidor web Nginx en todos los servidores del grupo "Webserver".
 
 El parámetro "Hosts" indica el grupo de servidores en el que debe ejecutarse el Playbook. El parámetro "become" indica si se deben habilitar las funciones con derechos ampliados (mediante "sudo" o "su").
 
 La sección "Aplicaciones" enumera las distintas aplicaciones que pueden utilizarse en el Playbook. En este caso, sólo existe una aplicación que instala el paquete Nginx junto con el módulo "apt".
 
 ## Módulo Ansible
 
 Los módulos Ansible son componentes de código modificables que se pueden utilizar para llevar a cabo distintas tareas. Ansible WIRD cuenta con una gran variedad de módulos integrados y también hay disponibles muchos módulos de otros fabricantes.
 
 Estos son algunos ejemplos de módulos integrados:
 
 - `apt` - Permite instalar paquetes en sistemas basados en Debian
 - `yum` - Se descargan paquetes en sistemas basados en Red Hat
 - file` - Comprueba datos
 - servicio` - Los servicios del sistema se actualizan
 - usuario` - Usuarios y grupos verificados
 - Copiar - Copia datos de la máquina de control al servidor gestionado
 
 Encontrará una lista completa de los módulos integrados en la [Documentación de Ansible] (https://docs.ansible.com/ansible/latest/modules/modules_by_category.html).
 
 ## Ansible Rollen und Ordnerstruktur
 
 Un rol ansible permite organizar y utilizar todas las tareas y configuraciones. Se trata de una estructura de clasificación que contiene tareas, gestores, procesos, datos y otros recursos.
 
 Este es un ejemplo de una sencilla rutina Ansible para instalar y configurar Nginx:
 En este ejemplo, la herramienta nginx contiene una tabla con varias tablas de servidores, cada una de las cuales tiene un valor diferente:
 
 - Funciones**: contiene las funciones asignadas a la función.
 - Manejador**: contiene el Manejador que las Tareas pueden asignar.
 - Opciones**: contiene las opciones de Jinja2 que se utilizan para generar los datos de configuración de Nginx.
 - **Dateien**: contiene todos los datos estadísticos necesarios.
 - *vars**: contiene variables de tipo variable.
 - **defaults**: contiene variables estándar para el rol.
 - **meta**: contiene metadatos sobre el rollo, p. ej. sus características.
 
 Los roles pueden ser fácilmente configurados y se pueden utilizar varios sobre las guías y proyectos.
 
 Este es un ejemplo de un archivo main.yml en el directorio de tareas:
