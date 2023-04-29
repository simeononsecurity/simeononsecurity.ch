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

 Ansible एक ओपन-टॉप ऑटोमेशन टूल जो सिस्टम एडमिनिस्ट्रेटर को अपना इंफ्रास्ट्रक्चर क्रिएट करने में सक्षम बनाता है। यह कार्यप्रणाली स्थिति का वर्णन करने के लिए एक सरल भाषा प्रदान करती है और उस स्थिति को स्वचालित रूप से लागू करती है। यह बड़े पैमाने पर मिश्रित प्रबंधन के लिए आवश्यक समय और प्रयास को कम करता है।  यदि आप Ansible के लिए नए हैं, तो यह लेख उपकरण का परिचय प्रदान करेगा, जिसकी मूल अवधारणाएँ और इसका उपयोग कैसे शुरू करें।  ## अन्सिबल का परिचय  Ansible को 2012 में Michael DeHaan द्वारा विकसित किया गया था और 2015 में Red Hat द्वारा अधिग्रहित किया गया था। तब से, यह उद्योग में सबसे लोकप्रिय डॉक्युमेंट डिवाइस बन गया।  एन्सिबल स्टैक की स्थिति को परिभाषित करने के लिए YAML ("YAML Ain't Markup Language" के लिए संक्षिप्त) नाम एक सरल, घोषणात्मक भाषा का उपयोग करता है। यह गैर-प्रोग्रामर के लिए पढ़ना और बनाना भी आसान है।  अन्सिबल का कार्य की एक विस्तृत श्रृंखला स्वचालित रूप से उपयोग करने के लिए बनाई जा सकती है, जिसमें निम्न शामिल हैं:  - **विनास प्रबंधन** - **आवेदन परिनियोजन** - **निरंतर अधिकार** - **प्रवधान ** - **सुरक्षा संगत** - **आक्षेप**  ## अन्सिबल के साथ शुरुआत करना  Ansible के साथ शुरुआत करने के लिए, आप इसे अपने सिस्टम पर माउंट करेंगे। लिंक्स, मैकोज़ और विंडोज सहित ऑपरेटिंग सिस्टम की एक विस्तृत श्रृंखला पर अन्सिबल स्थापित किया जा सकता है।  लिंक्स पर Ansible को स्थापित करने के लिए, इस मामले में Ubuntu, आप अपने कुछ कमांड का उपयोग कर सकते हैं: अन्यथा आप निम्नलिखित गाइडों का उपयोग करने योग्य बनाने के लिए कर सकते हैं: - [Ansible को रिकॉर्ड करना](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) - [अफसोस की आशंका](https://docs.ansible.com/ansible/latest/installation_guide/index.html)  एक बार अन्सिबल सर्किट हो जाने के बाद, आप सुनिश्चित कर सकते हैं कि यह विशिष्ट क्रम चल रहा है:  यह आपके द्वारा दर्ज किए गए Ansible के संस्करण की कल्पना करेगा।  ## अन्सिबल इन्वेंटरी  Ansible का करने में पहला कदम एक दृष्टिकोण को परिभाषित करना है। एक सूची सर्वरों की एक सूची है जिसे Ansible आपका करेगा। INI, YAML और JSON सहित विभिन्न स्वरूपों में एक सूची को परिभाषित किया जा सकता है।  आईएनआई प्रारूप में दस्तावेज़ का एक उदाहरण यहां दिया गया है:   यह प्रारूप प्रारूप संरक्षितों के डोमेन, "वेबसर्वर्स" और "डेटाबेस" को परिभाषित करता है, और प्रत्येक समूह में सर्वरों के होस्टनामों को सूचीबद्ध करता है।  ## अन्सिबल प्लेबुक  एक बार जब आप एक वस्तु-सूची को परिभाषित कर लेते हैं, तो अगले चरण को एक प्रकार से परिभाषित कर दिया जाता है। एक प्लेबुक एक YAML फ़ाइल है जो उन कार्यों के एक सेट का वर्णन करती है जो Ansible को रिकॉर्ड करने में सर्वर पर काम करते हैं।  यहाँ एक साधारण प्लेबुक का उदाहरण दिया गया है:  यह अजीब "वेबसर्वर" समूह के सभी सर्वर Nginx वेब सर्वर स्थापित करता है।  `मेजबान` संलग्नक संलग्नक है कि प्लेबुक को किस समूह पर नज़र रखना चाहिए। `बन` विवरण देता है कि कार्यों को अनुकूलन विशेषाधिकार (`सुडो` या `सु` का उपयोग करके) के साथ पहुँचना चाहिए।  `कार्य` अनुभाग उन अलग-अलग कार्यों को सूचीबद्ध करता है जिन्हें अलग-अलग कार्यों के द्वारा निष्पादित किया जाना चाहिए। इस मामले में, केवल एक कार्य है, जो `apt` मॉड्यूल का उपयोग करके Nginx Package को स्थापित करता है।  ## अन्सिबल मॉड्यूल  अन्सिबल मॉड्यूल कोड की पुन: रचना वास्तव में विशिष्ट कार्यों का उपयोग करने के लिए बनाई जा सकती हैं। Ansible बिल्ट-इन मॉड्यूल की एक विस्तृत श्रृंखला के साथ आता है, और कई तृतीय-पक्ष मॉड्यूल भी उपलब्ध हैं।  यहां बिल्ट-इन मॉड्यूल के कुछ उदाहरण दिए गए हैं:  - `apt` - डेबियन-आधारित सिस्टम पर संकुल करें - `yum` - Red Hat-आधारित सिस्टम पर आपका संकुल करें - `पासें` - फाइलें अपनी करें - `सेवा` - सिस्टम सेवाओं का प्रबंधन करें - `मोटापा` - लाइव और आपके लिए - `कॉपी` - माइक्रोलेटर से अपने सर्वर में कॉपी करें  आप [उत्तर देने योग्य दस्तावेज़ीकरण](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html) में बिल्ट-इन मॉड्यूल की पूरी सूची पा सकते हैं।  ## अन्सिबल रोल्स और फोल्डर स्ट्रक्चर  Ansible role सामान्य कार्य और अभ्यास को सरल और पुन: उपयोग करने का एक तरीका है। यह एक निर्देशिका है जिसमें कार्य, दस्तावेज़, फ़ाइलें और अन्य संसाधन शामिल हैं।  यहाँ Nginx को स्थापित और विलय करने के लिए एक सरल उत्तर भूमिका का एक उदाहरण दिया गया है: इस उदाहरण में, nginx भूमिका एक निर्देशिका है जिसमें कई उप-दुःख हैं, जिनमें से प्रत्येक एक विशिष्ट उद्देश्य को पूरा करती है:  - **कार्य**: इसमें वे कार्य शामिल हैं जिनकी भूमिका निभाई जाएगी। - **हैंडलर**: इसमें वे हैंडलर होते हैं जिन्हें कार्य सूचित कर सकते हैं। - **टेम्पलेट्स**: इसमें Jinja2 धब्बे शामिल हैं वास्तव में Nginx के लिए दर्शनीय स्थल को दर्शाने के लिए किया जाएगा। - **फाइलें**: भूमिका निभाने के लिए जरूरी सभी फाइलें शामिल हैं। - **vars**: इसमें वेरिएबल्स शामिल हैं जो भूमिका के लिए विशिष्ट हैं। - **डिफोल्ट**: भूमिका के लिए डिफ़ॉल्ट चर शामिल हैं। - **मेटा**: इसमें भूमिका के बारे में मेटाडेटा होता है, जैसे कि इसका लेखा।  मैं कई प्लेबुक और प्रोजेक्ट में आसानी से साझा और पुन: उपयोग किया जा सकता है।  यहाँ कार्य निर्देशिकाओं में main.yml फ़ाइल का उदाहरण दिया गया है: