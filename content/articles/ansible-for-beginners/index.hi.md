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


 Ansible एक ओपन-टॉप ऑटोमेशन टूल जो सिस्टम एडमिनिस्ट्रेटर को अपना इंफ्रास्ट्रक्चर क्रिएट करने में सक्षम बनाता है। यह कार्यप्रणाली स्थिति का वर्णन करने के लिए एक सरल भाषा प्रदान करती है और उस स्थिति को स्वचालित रूप से लागू करती है। यह बड़े पैमाने पर मिश्रित प्रबंधन के लिए आवश्यक समय और प्रयास को कम करता है।
 
 यदि आप Ansible के लिए नए हैं, तो यह लेख उपकरण का परिचय प्रदान करेगा, जिसकी मूल अवधारणाएँ और इसका उपयोग कैसे शुरू करें।
 
 ## अन्सिबल का परिचय
 
 Ansible को 2012 में Michael DeHaan द्वारा विकसित किया गया था और 2015 में Red Hat द्वारा अधिग्रहित किया गया था। तब से, यह उद्योग में सबसे लोकप्रिय डॉक्युमेंट डिवाइस बन गया।
 
 एन्सिबल स्टैक की स्थिति को परिभाषित करने के लिए YAML ("YAML Ain't Markup Language" के लिए संक्षिप्त) नाम एक सरल, घोषणात्मक भाषा का उपयोग करता है। यह गैर-प्रोग्रामर के लिए पढ़ना और बनाना भी आसान है।
 
 अन्सिबल का कार्य की एक विस्तृत श्रृंखला स्वचालित रूप से उपयोग करने के लिए बनाई जा सकती है, जिसमें निम्न शामिल हैं:
 
 - **विनास प्रबंधन**
 - **आवेदन परिनियोजन**
 - **निरंतर अधिकार**
 - **प्रवधान **
 - **सुरक्षा संगत**
 - **आक्षेप**
 
 ## अन्सिबल के साथ शुरुआत करना
 
 Ansible के साथ शुरुआत करने के लिए, आप इसे अपने सिस्टम पर माउंट करेंगे। लिंक्स, मैकोज़ और विंडोज सहित ऑपरेटिंग सिस्टम की एक विस्तृत श्रृंखला पर अन्सिबल स्थापित किया जा सकता है।
 
 लिंक्स पर Ansible को स्थापित करने के लिए, इस मामले में Ubuntu, आप अपने कुछ कमांड का उपयोग कर सकते हैं:
 अन्यथा आप निम्नलिखित गाइडों का उपयोग करने योग्य बनाने के लिए कर सकते हैं:
 - [Ansible को रिकॉर्ड करना](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
 - [अफसोस की आशंका](https://docs.ansible.com/ansible/latest/installation_guide/index.html)
 
 एक बार अन्सिबल सर्किट हो जाने के बाद, आप सुनिश्चित कर सकते हैं कि यह विशिष्ट क्रम चल रहा है:
 
 यह आपके द्वारा दर्ज किए गए Ansible के संस्करण की कल्पना करेगा।
 
 ## अन्सिबल इन्वेंटरी
 
 Ansible का करने में पहला कदम एक दृष्टिकोण को परिभाषित करना है। एक सूची सर्वरों की एक सूची है जिसे Ansible आपका करेगा। INI, YAML और JSON सहित विभिन्न स्वरूपों में एक सूची को परिभाषित किया जा सकता है।
 
 आईएनआई प्रारूप में दस्तावेज़ का एक उदाहरण यहां दिया गया है:
 
 
 यह प्रारूप प्रारूप संरक्षितों के डोमेन, "वेबसर्वर्स" और "डेटाबेस" को परिभाषित करता है, और प्रत्येक समूह में सर्वरों के होस्टनामों को सूचीबद्ध करता है।
 
 ## अन्सिबल प्लेबुक
 
 एक बार जब आप एक वस्तु-सूची को परिभाषित कर लेते हैं, तो अगले चरण को एक प्रकार से परिभाषित कर दिया जाता है। एक प्लेबुक एक YAML फ़ाइल है जो उन कार्यों के एक सेट का वर्णन करती है जो Ansible को रिकॉर्ड करने में सर्वर पर काम करते हैं।
 
 यहाँ एक साधारण प्लेबुक का उदाहरण दिया गया है:
 
 यह अजीब "वेबसर्वर" समूह के सभी सर्वर Nginx वेब सर्वर स्थापित करता है।
 
 `मेजबान` संलग्नक संलग्नक है कि प्लेबुक को किस समूह पर नज़र रखना चाहिए। `बन` विवरण देता है कि कार्यों को अनुकूलन विशेषाधिकार (`सुडो` या `सु` का उपयोग करके) के साथ पहुँचना चाहिए।
 
 `कार्य` अनुभाग उन अलग-अलग कार्यों को सूचीबद्ध करता है जिन्हें अलग-अलग कार्यों के द्वारा निष्पादित किया जाना चाहिए। इस मामले में, केवल एक कार्य है, जो `apt` मॉड्यूल का उपयोग करके Paquete Nginx को स्थापित करता है।
 
 ## अन्सिबल मॉड्यूल
 
 अन्सिबल मॉड्यूल कोड की पुन: रचना वास्तव में विशिष्ट कार्यों का उपयोग करने के लिए बनाई जा सकती हैं। Ansible बिल्ट-इन मॉड्यूल की एक विस्तृत श्रृंखला के साथ आता है, और कई तृतीय-पक्ष मॉड्यूल भी उपलब्ध हैं।
 
 यहां बिल्ट-इन मॉड्यूल के कुछ उदाहरण दिए गए हैं:
 
 - `apt` - डेबियन-आधारित सिस्टम पर संकुल करें
 - `yum` - Red Hat-आधारित सिस्टम पर आपका संकुल करें
 - `पासें` - फाइलें अपनी करें
 - `सेवा` - सिस्टम सेवाओं का प्रबंधन करें
 - `मोटापा` - लाइव और आपके लिए
 - `कॉपी` - माइक्रोलेटर से अपने सर्वर में कॉपी करें
 
 आप [उत्तर देने योग्य दस्तावेज़ीकरण](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html) में बिल्ट-इन मॉड्यूल की पूरी सूची पा सकते हैं।
 
 ## अन्सिबल रोल्स और फोल्डर स्ट्रक्चर
 
 Ansible role सामान्य कार्य और अभ्यास को सरल और पुन: उपयोग करने का एक तरीका है। यह एक निर्देशिका है जिसमें कार्य, दस्तावेज़, फ़ाइलें और अन्य संसाधन शामिल हैं।
 
 यहाँ Nginx को स्थापित और विलय करने के लिए एक सरल उत्तर भूमिका का एक उदाहरण दिया गया है:
 इस उदाहरण में, nginx भूमिका एक निर्देशिका है जिसमें कई उप-दुःख हैं, जिनमें से प्रत्येक एक विशिष्ट उद्देश्य को पूरा करती है:
 
 - **कार्य**: इसमें वे कार्य शामिल हैं जिनकी भूमिका निभाई जाएगी।
 - **हैंडलर**: इसमें वे हैंडलर होते हैं जिन्हें कार्य सूचित कर सकते हैं।
 - **टेम्पलेट्स**: इसमें Jinja2 धब्बे शामिल हैं वास्तव में Nginx के लिए दर्शनीय स्थल को दर्शाने के लिए किया जाएगा।
 - **फाइलें**: भूमिका निभाने के लिए जरूरी सभी फाइलें शामिल हैं।
 - **vars**: इसमें वेरिएबल्स शामिल हैं जो भूमिका के लिए विशिष्ट हैं।
 - **डिफोल्ट**: भूमिका के लिए डिफ़ॉल्ट चर शामिल हैं।
 - **मेटा**: इसमें भूमिका के बारे में मेटाडेटा होता है, जैसे कि इसका लेखा।
 
 मैं कई प्लेबुक और प्रोजेक्ट में आसानी से साझा और पुन: उपयोग किया जा सकता है।
 
 यहाँ कार्य निर्देशिकाओं में main.yml फ़ाइल का उदाहरण दिया गया है:
