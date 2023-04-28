---
title: "Introduction to Ansible: Automating IT Infrastructure Management"
draft: false
toc: true
date: 2023-02-25
description: "Learn the basics of Ansible, an open-source automation tool that simplifies IT infrastructure management through a declarative language."
tags: ["Ansible", "IT infrastructure", "automation", "configuration management", "application deployment", "provisioning", "continuous delivery", "security compliance", "orchestration", "YAML", "modules", "roles", "best practices", "version control", "testing", "Red Hat", "system administrators", "Linux", "macOS", "Windows"]
cover: "/img/cover/A_cartoon_character_sitting_at_a_desk_surrounded_by_servers.png"
coverAlt: "A cartoon character sitting at a desk, surrounded by servers and cables, with Ansible's logo on the computer screen, smiling as tasks are automated."
coverCaption: ""
---
```bash
sudo apt-get update
sudo apt-get install ansible -y
```
```bash
ansible --version
```
```ini
[webservers]
webserver1.example.com
webserver2.example.com

[databases]
dbserver1.example.com
dbserver2.example.com
```
```yml
name: Install Nginx
hosts: webservers
become: yes

tasks:
    - name: Install Nginx package
        apt:
        name: nginx
        state: present
```
```
roles/
└── nginx/
    ├── tasks/
    │   ├── main.yml
    ├── handlers/
    │   ├── main.yml
    ├── templates/
    │   ├── nginx.conf.j2
    ├── files/
    ├── vars/
    ├── defaults/
    ├── meta/
```
```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
  notify: restart nginx

- name: Enable Nginx
  systemd:
    name: nginx
    enabled: yes
    state: started
```

This task installs Nginx using the apt module and enables and starts the Nginx service using the systemd module. It also notifies the restart nginx handler, which will restart Nginx if any changes were made to the configuration.

Using an Ansible role like this can simplify the process of managing and configuring software across multiple servers or environments. By separating the tasks, handlers, templates, and other resources into a single directory structure, you can more easily manage and reuse these components across different playbooks and projects.

## Best Practices for Ansible

Here are some best practices to follow when using Ansible:

### 1. Use Version Control

Storing your Ansible playbooks and roles in a version control system like Git is a best practice that can help you keep track of changes and collaborate with others. Version control provides a history of changes made to your codebase, allowing you to roll back to previous versions if needed. It also makes it easy to collaborate with others by sharing code and managing conflicts.

### 2. Use Roles to Organize Your Playbooks

Roles are a powerful way to organize your Ansible playbooks and tasks. By grouping related tasks together into roles, you can make your playbooks more modular and reusable. Roles also make it easy to share code across different projects.

Here's an example of a playbook that uses a role to install and configure Nginx:

```yml
name: Install and configure Nginx
hosts: webservers
become: yes
roles:
  - nginx
```

This playbook uses a role called "nginx" to install and configure Nginx on the "webservers" group of hosts.

### 3. Use Tags to Group Tasks

Tags can be used to group related tasks together in your Ansible playbooks. This makes it easier to run specific parts of a playbook, especially when working with large, complex playbooks.

Here's an example of how to use tags in an Ansible playbook:
```yml
name: Install and configure Nginx
hosts: webservers
become: yes
tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
    tags: nginx_install

  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    tags: nginx_config
```

This playbook has two tasks, one for installing Nginx and one for configuring Nginx. Each task has a tag associated with it, making it easy to run only the tasks that are needed.

### 4. Use Variables to Make Playbooks More Flexible

Variables can be used to make your Ansible playbooks more flexible and reusable. By using variables, you can make your playbooks more generic and adaptable to different environments.

Here's an example of how to use variables in an Ansible playbook:
```yml
name: Install and configure Nginx
hosts: webservers
become: yes

vars:
nginx_port: 80
nginx_user: www-data

tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    notify: restart nginx

handlers:
  - name: restart nginx
    service:
    name: nginx
    state: restarted
```

This playbook uses variables to specify the port that Nginx should listen on and the user that should run Nginx. This makes the playbook more flexible and adaptable to different environments.

### 5. Test Your Playbooks

Testing your Ansible playbooks is a best practice that can help you catch errors and ensure that your playbooks are working as expected. One popular tool for testing Ansible playbooks is Molecule.

Molecule is a testing framework that allows you to test your playbooks in a consistent and automated way. Molecule can create virtual machines, apply your playbook, and then verify that everything is working as expected. This can help you catch errors and ensure that your playbooks are working correctly before deploying to production.

Here's an example of how to use Molecule to test an Ansible role:

```bash
molecule init role myrole
cd myrole
molecule test
```

## Conclusion

In this article, we've introduced Ansible, a powerful automation tool that can help you manage complex IT infrastructure. We've covered the basic concepts of Ansible, including inventories, playbooks, modules, and roles.

We've also discussed best practices for using Ansible, including using version control, organizing playbooks with roles, using tags and variables, and testing your playbooks.

If you're new to Ansible, we recommend that you start by experimenting with some simple playbooks and gradually build up your skills and knowledge over time. With practice, you'll be able to automate even the most complex infrastructure tasks with ease!

 Ansible es una herramienta de automatización de código abierto que permite a los administradores de sistemas automatizar la gestión de la infraestructura de TI. Proporcione un lenguaje simple para describir el estado deseado de la infraestructura y aplica automáticamente ese estado. Esto reduce el tiempo y el esfuerzo necesario para administrar sistemas complejos a gran escala.  Si es nuevo en Ansible, este artículo le brindará una introducción a la herramienta, incluidos sus conceptos básicos y cómo comenzar a usarla.  ## Introducción a Ansible  Ansible fue desarrollado por Michael DeHaan en 2012 y adquirido por Red Hat en 2015. Desde entonces, se ha convertido en una de las herramientas de automatización más populares de la industria.  Ansible usa un lenguaje declarativo simple llamado YAML (abreviatura de "YAML no es lenguaje de marcado") para definir el estado deseado de la infraestructura. Esto hace que sea fácil de leer y comprender, incluso para quienes no son programadores.  Ansible se puede utilizar para automatizar una amplia gama de tareas, que incluyen:  - **Gestión de configuración** - **Despliegue de aplicaciones** - **Entrega continua** - **Aprovisionamiento** - **Cumplimiento de seguridad** - **Orquestación**  ## Primeros pasos con Ansible  Para comenzar con Ansible, deberá instalarlo en su sistema. Ansible se puede instalar en una amplia gama de sistemas operativos, incluidos Linux, macOS y Windows.  Para instalar Ansible en Linux, en este caso Ubuntu, puedes usar los siguientes comandos: Por el contrario, puede usar las siguientes guías para instalar ansible: - [Instalación de Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) - [Guía de instalación](https://docs.ansible.com/ansible/latest/installation_guide/index.html)  Una vez que Ansible está instalado, puede verificar que oculta el siguiente comando:  Esto debería mostrar la versión de Ansible que ha instalado.  ## Inventario de Ansible  El primer paso para usar Ansible es definir un inventario. Un inventario es una lista de servidores que administrará Ansible. Un inventario se puede definir en una variedad de formatos, incluidos INI, YAML y JSON.  Aquí hay un ejemplo de un archivo de inventario en formato INI:   Este archivo de inventario define dos grupos de servidores, "servidores web" y "bases de datos", y enumera los nombres de host de los servidores en cada grupo.  ## Libros de jugadas de Ansible  Una vez que haya definido un inventario, el siguiente paso es definir un libro de jugadas. Un libro de jugadas es un archivo YAML que describe un conjunto de tareas que Ansible debe realizar en los servidores del inventario.  Aquí hay un ejemplo de un libro de jugadas sencillas:  Este libro de jugadas instala el servidor web Nginx en todos los servidores del grupo "servidores web".  El parámetro `hosts` especifica en qué grupo de servidores debe ejecutarse el libro de jugadas. El parámetro `become` especifica que las tareas deben ejecutarse con privilegios elevados (usando `sudo` o `su`).  La sección "tareas" enumera las tareas individuales que debe realizar el libro de jugadas. En este caso, solo hay una tarea, que instala el paquete Nginx usando el módulo `apt`.  ## Módulos Ansible  Los módulos de Ansible son unidades de código reutilizables que se pueden usar para realizar tareas específicas. Ansible viene con una amplia gama de módulos integrados y también hay muchos módulos de terceros disponibles.  Estos son algunos ejemplos de módulos integrados:  - `apt` - Administrar paquetes en sistemas basados en Debian - `yum` - Administrar paquetes en sistemas basados en Red Hat - `archivo` - Administrar archivos - `servicio` - Administrar los servicios del sistema - `usuario` - Administrar usuarios y grupos - `copiar` - Copiar archivos de la máquina de control a los servidores administrados  Puede encontrar una lista completa de módulos integrados en la [documentación de Ansible] (https://docs.ansible.com/ansible/latest/modules/modules_by_category.html).  ## Roles de Ansible y estructura de carpetas  Un rol de Ansible es una forma de organizar y reutilizar tareas y configuraciones comunes. Es una estructura de directorio que contiene tareas, controladores, plantillas, archivos y otros recursos.  Aquí hay un ejemplo de un rol de Ansible simple para instalar y configurar Nginx: En este ejemplo, la función nginx es un directorio que contiene varios subdirectorios, cada uno de los cuales tiene un propósito específico:  - **tareas**: contiene las tareas que serán ejecutadas por el rol. - **handlers**: contiene los handlers que pueden notificar las tareas. - **plantillas**: contiene las plantillas Jinja2 que se utilizarán para generar los archivos de configuración para Nginx. - **archivos**: contiene los archivos estáticos que necesita el rol. - **vars**: contiene variables que son específicas del rol. - **predeterminados**: contiene variables predeterminadas para el rol. - **meta**: contiene metadatos sobre el rol, como sus dependencias.  Los roles se pueden compartir y reutilizar fácilmente en múltiples playbooks y proyectos.  Aquí hay un ejemplo de un archivo main.yml en el directorio de tareas: