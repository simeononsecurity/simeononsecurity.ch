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

A continuación se muestra un ejemplo de un playbook que utiliza un rol para instalar y configurar Nginx:

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

Molecule es un marco de pruebas que permite probar los libros de reproducción de forma coherente y automatizada. Molecule puede crear máquinas virtuales, aplicar su playbook, y luego verificar que todo está funcionando como se esperaba. Esto puede ayudarle a detectar errores y asegurarse de que sus playbooks funcionan correctamente antes de desplegarlos en producción.

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


 أن تكون أداة أتمتة مفتوحة المصدر يوفر لغة بسيطة لوصف الحالة الحالة المرغوبة للبنية ، ويفرض هذه الحالة تلقائيًا. هذا القسم من الوقت والجهد
 
 تم تنفيذ هذا المقال في مقدمة عن برامج الوسائط المتعددة.
 
 ## مقدمة إلى أنسبل
 
 تم تطوير Ansible بواسطة Michael DeHaan في عام 2012 واستحوذت عليه Red Hat في عام 2015. فترة طويلة ، أصبحت واحدة من أكثر أدوات الأتمتة شيوعًا في الصناعة.
 
 تُستخدم ، تُعرف ، بغطاء خارجي ،
 
 يمكن استخدام Ansible لأتمتة مجموعة واسعة من المهام ، بما في ذلك:
 
 - ** إدارة التكوين **
 - ** نشر التطبيق **
 - ** التسليم المستمر **
 - ** التزويد **
 - ** الامتثال الأمني **
 - ** التنظيم **
 
 ## البدء مع أنسبل
 
 استخدام Ansible ، محرك كسادته إلى نظامه الأساسي. يمكن تثبيت Ansible على مجموعة واسعة من أنظمة التشغيل ، بما في ذلك Linux و macOS و Windows.
 
 لتثبيت Ansible على Linux ، في هذه الحالة الحالة الحالة Ubuntu ، يمكنك استخدام الأوامر التالية:
 يمكنك استخدام الدليل لتثبيت التالي غير مرغوب فيه:
 - [تثبيت أنسبل] (https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
 - [دليل التثبيت] (https://docs.ansible.com/ansible/latest/installation_guide/index.html)
 
 إجراء أخرى ، من ناحية أخرى ، من ناحية أخرى
 
 أن يعرض إصدار أنسبل الذي قمت بتثبيته.
 
 ## جرد أنسبل
 
 الخطوة الأولى في استخدام Ansible هي تحديد المخزون. الجرد هو قائمة الخوادم التي سيديرها أنسبل. يمكن تحديد المخزون في مجموعة من التنسيقات ، بما في ذلك INI و YAML و JSON.
 
 فيما يلي مثال على ملف جرد INI:
 
 
 ملف مجموعات الجرد ، "خوادم الويب" و "قواعد البيانات" ، ويسرد أسماء المضيفين للخوادم في كل مجموعة.
 
 ## Ansible Playbooks
 
 تحديد عمود النسخ ، الخطوة التالية هي تحديد دليل التشغيل. دليل التشغيل هو ملف YAML يصف مجموعة من المهام التي يؤديها يؤديها على الخوادم الموجودة في المخزون.
 
 فيما يلي مثال على دليل بسيط:
 
 يقوم دليل التشغيل هذا بتثبيت خادم الويب Nginx على جميع الخوادم في مجموعة "خوادم الويب".
 
 تحدد المعلمة `hosts` مجموعة الخوادم التي يجب تشغيلها. تعمل المعلمة `تصبح` مهام بامتيازات عالية (sudo` أو` su`)
 
 يسرد قسم "المهام" المهام الفردية التي يجب أن يؤديها دليل التشغيل. هذه الحالة ، هناك مهمة واحدة فقط ، وهي تثبيت حزمة Nginx ، وتوجدت الوحدة مع بعضهما البعض.
 
 ## وحدات أنسبل
 
 الوحدات الصالحة الصالحة المتوفرة مع أحجام كبيرة من الوحدات ، وهناك حجج من وحدات التخزين الخارجية.
 
 فيما يلي بعض العروض على الوحدات المدمجة:
 
 - `apt` - إدارة الحزم على الأنظمة القائمة على دبيان
 - "yum" - إدارة الحزم على الأنظمة المستندة إلى Red Hat
 - `file` - إدارة الملفات
 - "الخدمة" - إدارة خدمات النظام
 - "المستخدم" - إدارة الحالات والمشتريات
 - "نسخ" - نسخ الملفات من جهاز التحكم في الخوادم المدارة
 
 يمكنك العثور على أكثر للوحدات المدمجة في [وثائق أنسبل] (https://docs.ansible.com/ansible/latest/modules/modules_by_category.html).
 
 ## أدوار أنسبل وبنية المجلد
 
 أنسبل هو طريقة تشغيل المهام والتكوينات. تحتوي على تعليمات وترحيلات وقوالب والملفات الأخرى.
 
 فيما يلي مثال لدور Ansible البسيط لتثبيت Nginx وتكوينه:
 في هذا المثال ، يحتوي هذا المثال على حلقة مفرغة من فرط الهواء.
 
 - ** المهام **: تحتوي على المهام التي سينتها الدور.
 - ** المعالجات **: تحتوي على المعالجات التي يمكن أن تدمج لهامها.
 - ** قوالب **: تحتوي على قوالب Jinja2 التي سيتم تغليفها بتجميع محتويات التكوين لـ Nginx.
 - Archivos **: تحتوي على ملفات ثابتة يحتاجها الدور.
 - ** فارز **: يحتوي على متغيرات خاصة بالدور.
 - ** الافتراضيات **: يحتوي على متغيرات افتراضية للدور.
 - ** meta **: يحتوي على بيانات وصفية حول الدور ، مثل تبعياته.
 
 يمكن مشاركة الأدوار وفكه بسهولة عبر من كتب التشغيل والمشاريع.
 
 فيما يلي مثال على ملف main.yml في دليل المهام:
