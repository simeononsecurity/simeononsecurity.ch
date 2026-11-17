---
title: "शुरुआती लोगों के लिए Ansible गाइड 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-13
description: "2026 के लिए Ansible गाइड। इसमें इंस्टॉलेशन, प्लेबुक, रोल, उदाहरण, श्रेष्ठ तरीके और Terraform, Puppet तथा Chef से तुलना शामिल है।"
tags: ["Ansible का परिचय", "IT इंफ्रास्ट्रक्चर प्रबंधन का स्वचालन", "Ansible की मूल बातें", "IT इंफ्रास्ट्रक्चर स्वचालन", "कॉन्फ़िगरेशन प्रबंधन", "एप्लिकेशन परिनियोजन", "प्रोविज़निंग", "निरंतर डिलीवरी", "सुरक्षा और अनुपालन", "ऑर्केस्ट्रेशन", "YAML", "Ansible मॉड्यूल", "रोल", "श्रेष्ठ तरीके", "वर्ज़न नियंत्रण", "परीक्षण", "Red Hat", "सिस्टम प्रशासक", "Linux", "macOS", "Windows", "Ansible इंस्टॉलेशन", "Ansible इन्वेंटरी", "Ansible प्लेबुक", "Ansible मॉड्यूल", "Ansible रोल", "Ansible के श्रेष्ठ तरीके", "Ansible परीक्षण", "IT इंफ्रास्ट्रक्चर स्वचालन टूल", "Ansible ट्यूटोरियल", "इंफ्रास्ट्रक्चर प्रबंधन स्वचालन", "शुरुआती लोगों के लिए Ansible", "Ansible सीखें", "Ansible ट्यूटोरियल 2026", "Ansible और Terraform", "Ansible और Puppet", "Ansible प्लेबुक के उदाहरण", "Ansible स्वचालन", "DevOps टूल", "कोड के रूप में इंफ्रास्ट्रक्चर", "Ansible AWX", "Ansible Tower", "Ansible संग्रह", "Ansible Galaxy", "Ansible Vault", "Ansible क्लाउड स्वचालन"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "आधुनिक IT इंफ्रास्ट्रक्चर का चित्र, जिसमें जुड़े हुए सर्वर और उपकरण, SSH और WinRM कनेक्शन, शैलीबद्ध YAML फ़ाइल और गहरे रंग की पृष्ठभूमि पर क्लाउड सेवा आइकन दिखाए गए हैं।"
coverCaption: ""
---

**शुरुआती लोगों के लिए Ansible: 2026 में IT स्वचालन की पूरी गाइड**

Ansible उद्योग के अग्रणी स्वचालन प्लेटफ़ॉर्म के रूप में विकसित हुआ है। स्रोत के अनुसार, Fortune 500 की 80% से अधिक कंपनियाँ जटिल IT इंफ्रास्ट्रक्चर के प्रबंधन के लिए Ansible पर भरोसा करती हैं। 2026 में भी यह सरल उपयोग और एंटरप्राइज़ सुविधाओं वाला एक महत्वपूर्ण समाधान है।

यह विस्तृत गाइड आपको बुनियादी जानकारी से Ansible के आत्मविश्वासपूर्ण उपयोग तक ले जाती है। इसमें मूल अवधारणाएँ, उन्नत तकनीकें, व्यावहारिक उदाहरण और 2026 के श्रेष्ठ तरीके शामिल हैं।

## Ansible क्या है? मूल बातें समझें

**Ansible** एक ओपन-सोर्स स्वचालन प्लेटफ़ॉर्म है, जो एजेंट-रहित घोषणात्मक स्वचालन से IT इंफ्रास्ट्रक्चर प्रबंधन को सरल बनाता है। पारंपरिक कॉन्फ़िगरेशन प्रबंधन टूल के विपरीत, इसे प्रबंधित नोड पर एजेंट इंस्टॉल करने की आवश्यकता नहीं होती। यह दूरस्थ प्रबंधन के लिए Linux और Unix में SSH, और Windows में WinRM का उपयोग करता है।

{{< youtube id="goclfp6a2IQ" >}}

### Ansible की प्रमुख विशेषताएँ

**1. एजेंट-रहित आर्किटेक्चर:**
- प्रबंधित नोड पर सॉफ़्टवेयर इंस्टॉल करने की आवश्यकता नहीं
- मौजूदा SSH या WinRM प्रोटोकॉल का उपयोग
- हमले की सतह और रखरखाव का बोझ घटाता है
- एजेंट-आधारित टूल की तुलना में शुरुआत करना आसान

**2. घोषणात्मक भाषा (YAML):**
- मनुष्यों के लिए पढ़ने योग्य कॉन्फ़िगरेशन फ़ाइलें
- इंफ्रास्ट्रक्चर को वांछित स्थिति के रूप में वर्णित करना
- इडेम्पोटेंट ऑपरेशन, जिन्हें कई बार सुरक्षित रूप से चलाया जा सकता है
- प्रोग्रामिंग अनुभव के बिना भी समझना आसान

**3. पुश मॉडल:**
- कंट्रोल नोड प्रबंधित नोड को कॉन्फ़िगरेशन भेजता है
- एजेंट की प्रतीक्षा किए बिना काम तुरंत चलाता है
- केंद्रीकृत नियंत्रण और दृश्यता
- मांग पर स्वचालन के लिए उपयुक्त

**4. विस्तृत मॉड्यूल लाइब्रेरी:**
- 5,000 से अधिक अंतर्निहित मॉड्यूल (2026 तक)
- Linux, Windows, नेटवर्क उपकरण और क्लाउड प्लेटफ़ॉर्म का समर्थन
- समुदाय और विक्रेताओं के मॉड्यूल
- Python में कस्टम मॉड्यूल लिखना आसान

### Ansible किन कामों को स्वचालित कर सकता है?

Ansible इन कामों के स्वचालन के लिए उपयुक्त है:

- **कॉन्फ़िगरेशन प्रबंधन**: सर्वर कॉन्फ़िगरेशन को एकसमान रखना
- **एप्लिकेशन परिनियोजन**: अलग-अलग वातावरण में एप्लिकेशन तैनात करना
- **प्रोविज़निंग**: इंफ्रास्ट्रक्चर बनाना और कॉन्फ़िगर करना
- **निरंतर डिलीवरी**: CI/CD पाइपलाइन के साथ एकीकरण
- **सुरक्षा और अनुपालन**: सुरक्षा नीतियाँ और अनुपालन लागू करना
- **ऑर्केस्ट्रेशन**: जटिल बहु-स्तरीय परिनियोजन का समन्वय
- **क्लाउड स्वचालन**: AWS, Azure, GCP और अन्य क्लाउड प्रबंधित करना
- **नेटवर्क स्वचालन**: स्विच, राउटर और फ़ायरवॉल कॉन्फ़िगर करना
- **Windows स्वचालन**: Windows सर्वर और वर्कस्टेशन प्रबंधित करना

### Ansible का विकास: 2012 से 2026

**समयरेखा:**
- **2012**: Michael DeHaan ने Ansible बनाया
- **2015**: Red Hat ने Ansible का अधिग्रहण किया
- **2019**: Ansible Engine 2.8 ने संग्रह प्रस्तुत किए
- **2020**: Ansible 2.10+ को ansible-core और संग्रह में बाँटा गया
- **2023**: Ansible 8.x ने क्लाउड एकीकरण बढ़ाया
- **2026**: Ansible 10.x में AI-सहायता वाला प्लेबुक निर्माण, बेहतर Windows समर्थन और विस्तारित सुरक्षा सुविधाएँ शामिल हैं

## Ansible और विकल्प: त्वरित तुलना

| सुविधा | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **प्रकार** | कॉन्फ़िगरेशन प्रबंधन | इंफ्रास्ट्रक्चर प्रोविज़निंग | कॉन्फ़िगरेशन प्रबंधन | कॉन्फ़िगरेशन प्रबंधन |
| **भाषा** | YAML | HCL | Puppet DSL (Ruby जैसी) | Ruby DSL |
| **एजेंट आवश्यक** | नहीं | नहीं | हाँ | हाँ |
| **सीखने की कठिनाई** | आसान | मध्यम | कठिन | कठिन |
| **उपयुक्त काम** | कॉन्फ़िगरेशन प्रबंधन, परिनियोजन | क्लाउड इंफ्रास्ट्रक्चर | बड़े उद्यम | जटिल वर्कफ़्लो |
| **स्थिति प्रबंधन** | पुश मॉडल | घोषणात्मक स्थिति फ़ाइल | पुल मॉडल | पुल मॉडल |
| **Windows समर्थन** | उत्कृष्ट (2026) | सीमित | अच्छा | अच्छा |
| **समुदाय का आकार** | बहुत बड़ा | बहुत बड़ा | बड़ा | मध्यम |
| **मुख्य उपयोग** | दैनिक संचालन | इंफ्रास्ट्रक्चर प्रोविज़निंग | एंटरप्राइज़ कॉन्फ़िगरेशन | एप्लिकेशन परिनियोजन |

**Ansible कब चुनें:**
- ✅ हाइब्रिड वातावरण में कॉन्फ़िगरेशन प्रबंधित करना
- ✅ एप्लिकेशन परिनियोजन स्वचालित करना
- ✅ जल्दी सीखना आवश्यक हो
- ✅ एजेंट-रहित आर्किटेक्चर पसंद हो
- ✅ बेहतर Windows स्वचालन चाहिए (2026 के सुधार)
- ✅ SSH इंफ्रास्ट्रक्चर पहले से मौजूद हो

**विकल्प कब विचारें:**
- Terraform: मुख्य रूप से इंफ्रास्ट्रक्चर प्रोविज़निंग के लिए (AWS, Azure, GCP)
- Puppet: हज़ारों नोड वाले बड़े उद्यमों के लिए
- Chef: एप्लिकेशन-केंद्रित जटिल वर्कफ़्लो के लिए

## शुरुआत करें: 2026 में Ansible इंस्टॉल करना

### सिस्टम आवश्यकताएँ

**कंट्रोल नोड, जहाँ Ansible चलता है:**
- Linux, macOS या Windows पर WSL2
- Python 3.9 या नया (2026 के लिए Python 3.11+ अनुशंसित)
- न्यूनतम 2 GB RAM, 4 GB या अधिक अनुशंसित
- संग्रहों के लिए 5 GB डिस्क स्थान

**प्रबंधित नोड:**
- SSH एक्सेस (Linux/Unix) या WinRM (Windows)
- Python 2.7 या Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- एजेंट इंस्टॉलेशन आवश्यक नहीं

### इंस्टॉलेशन के तरीके

#### तरीका 1: पैकेज मैनेजर (शुरुआती लोगों के लिए अनुशंसित)

**Ubuntu/Debian:**
```bash
# नवीनतम संस्करण के लिए Ansible PPA जोड़ें
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux:**
```bash
# EPEL रिपॉज़िटरी सक्षम करें
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS:**
```bash
# Homebrew का उपयोग
brew install ansible
```

#### तरीका 2: Python pip (नई सुविधाएँ)

```bash
# pipx इंस्टॉल करें (अनुशंसित पृथक वातावरण)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# pipx से Ansible इंस्टॉल करें
pipx install --include-deps ansible

# इंस्टॉलेशन सत्यापित करें
ansible --version
```

#### तरीका 3: Docker (पोर्टेबल)

```bash
# आधिकारिक Ansible कंटेनर प्राप्त करें
docker pull quay.io/ansible/ansible:latest

# कंटेनर में Ansible चलाएँ
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### इंस्टॉलेशन सत्यापित करें

```bash
# Ansible संस्करण जाँचें
ansible --version

# अपेक्षित आउटपुट (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### प्रारंभिक कॉन्फ़िगरेशन

Ansible कॉन्फ़िगरेशन फ़ाइल बनाएँ:

```bash
# कॉन्फ़िग डायरेक्टरी बनाएँ
mkdir -p ~/.ansible

# ansible.cfg बनाएँ
cat > ~/.ansible/ansible.cfg << 'EOF'
[defaults]
inventory = ~/ansible/inventory
host_key_checking = False
retry_files_enabled = False
gathering = smart
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts
fact_caching_timeout = 3600

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False
EOF
```

## आवश्यक अवधारणाएँ: Ansible के घटक

### 1. इन्वेंटरी: अपना इंफ्रास्ट्रक्चर परिभाषित करें

**इन्वेंटरी** उन होस्ट और समूहों को परिभाषित करती है जिन्हें Ansible प्रबंधित करता है। यह स्थिर (INI या YAML फ़ाइल) या गतिशील (स्क्रिप्ट या प्लगइन) हो सकती है।

#### स्थिर इन्वेंटरी (INI प्रारूप)

```ini
# inventory/hosts.ini

# वेब सर्वर समूह
[webservers]
web1.example.com
web2.example.com
web3.example.com

# डेटाबेस सर्वर समूह
[databases]
db1.example.com ansible_host=192.168.1.100
db2.example.com ansible_host=192.168.1.101

# लोड बैलेंसर
[loadbalancers]
lb1.example.com

# समूहों का समूह
[production:children]
webservers
databases
loadbalancers

# सभी वेब सर्वर के लिए वेरिएबल
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# सभी होस्ट के लिए वेरिएबल
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### स्थिर इन्वेंटरी (YAML प्रारूप, 2026 में अनुशंसित)

```yaml
# inventory/hosts.yml
all:
  vars:
    ansible_python_interpreter: /usr/bin/python3
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
        web3.example.com:
      vars:
        ansible_user: deploy
        http_port: 80
        https_port: 443
    databases:
      hosts:
        db1.example.com:
          ansible_host: 192.168.1.100
        db2.example.com:
          ansible_host: 192.168.1.101
      vars:
        ansible_user: dbadmin
    production:
      children:
        webservers:
        databases:
```

#### गतिशील इन्वेंटरी (क्लाउड प्रदाता)

क्लाउड वातावरण के लिए गतिशील इन्वेंटरी प्लगइन का उपयोग करें:

**AWS EC2:**
```yaml
# inventory/aws_ec2.yml
plugin: amazon.aws.ec2
regions:
  - us-east-1
  - us-west-2
filters:
  tag:Environment: production
keyed_groups:
  - key: tags.Application
    prefix: app
```

**Azure:**
```yaml
# inventory/azure_rm.yml
plugin: azure.azcollection.azure_rm
include_vm_resource_groups:
  - production-rg
keyed_groups:
  - key: tags.role
    prefix: role
```

### 2. प्लेबुक: स्वचालन की रूपरेखा

**प्लेबुक** YAML फ़ाइलें हैं, जो स्वचालन वर्कफ़्लो का वर्णन करती हैं और इंफ्रास्ट्रक्चर की वांछित स्थिति तय करती हैं।

#### सरल प्लेबुक उदाहरण

```yaml
# simple_playbook.yml
---
- name: वेब सर्वर कॉन्फ़िगर करें
  hosts: webservers
  become: yes
  
  tasks:
    - name: Nginx इंस्टॉल करें
      apt:
        name: nginx
        state: present
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Nginx शुरू और सक्षम करें
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: वेबसाइट की सामग्री कॉपी करें
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: फ़ायरवॉल कॉन्फ़िगर करें
      ufw:
        rule: allow
        port: '{{ item }}'
        proto: tcp
      loop:
        - 80
        - 443
```

#### प्लेबुक चलाना

```bash
# मूल निष्पादन
ansible-playbook simple_playbook.yml

# विशिष्ट इन्वेंटरी के साथ
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# विशिष्ट होस्ट तक सीमित करें
ansible-playbook simple_playbook.yml --limit web1.example.com

# ड्राई रन (चेक मोड)
ansible-playbook simple_playbook.yml --check

# समस्या निवारण के लिए विस्तृत आउटपुट
ansible-playbook simple_playbook.yml -vvv
```

### 3. मॉड्यूल: दोबारा इस्तेमाल होने वाली कार्य इकाइयाँ

Ansible मॉड्यूल स्वचालन के मूल घटक हैं। हर मॉड्यूल एक विशिष्ट काम करता है।

#### आम मॉड्यूल (2026)

**सिस्टम मॉड्यूल:**
```yaml
# पैकेज प्रबंधन
- name: पैकेज इंस्टॉल करें (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# सेवा प्रबंधन
- name: सेवाओं का प्रबंधन करें
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**फ़ाइल मॉड्यूल:**
```yaml
# फ़ाइल संचालन
- name: डायरेक्टरी बनाएँ
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# फ़ाइलें कॉपी करें
- name: कॉन्फ़िगरेशन तैनात करें
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# वेरिएबल वाला टेम्पलेट
- name: nginx कॉन्फ़िगरेशन तैनात करें
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**क्लाउड मॉड्यूल (AWS उदाहरण):**
```yaml
# EC2 इंस्टेंस बनाएँ
- name: EC2 इंस्टेंस लॉन्च करें
  amazon.aws.ec2_instance:
    name: webserver-01
    instance_type: t3.medium
    image_id: ami-0c55b159cbfafe1f0
    region: us-east-1
    vpc_subnet_id: subnet-12345678
    security_group: web-sg
    key_name: my-keypair
    tags:
      Environment: production
      Application: web

# S3 बकेट बनाएँ
- name: S3 बकेट बनाएँ
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**डेटाबेस मॉड्यूल:**
```yaml
# MySQL डेटाबेस प्रबंधन
- name: MySQL डेटाबेस बनाएँ
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: MySQL उपयोगकर्ता बनाएँ
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. चर: प्लेबुक को लचीला बनाएँ

चर आपको अलग-अलग वातावरण में प्लेबुक का पुनः उपयोग करने देते हैं।

#### चर प्राथमिकता (उच्च से निम्न)

1. अतिरिक्त चर (कमांड लाइन पर `-e`)
2. कार्य चर
3. ब्लॉक चर
4. रोल और include चर
5. प्ले चर
6. होस्ट फ़ैक्ट
7. प्लेबुक के `host_vars`
8. प्लेबुक के `group_vars`
9. इन्वेंटरी के `host_vars`
10. इन्वेंटरी के `group_vars`
11. रोल के डिफ़ॉल्ट मान

#### चर के उदाहरण

**प्लेबुक चर:**
```yaml
---
- name: एप्लिकेशन तैनात करें
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: "{{ app_name }} संस्करण {{ app_version }} तैनात करें"
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (पर्यावरण-विशिष्ट):**
```yaml
# group_vars/production.yml
app_environment: production
db_host: prod-db.example.com
db_port: 3306
log_level: warning
max_connections: 1000

# group_vars/development.yml
app_environment: development
db_host: dev-db.example.com
db_port: 3306
log_level: debug
max_connections: 100
```

**Ansible Vault (एन्क्रिप्ट किए गए चर):**
```bash
# एन्क्रिप्टेड फ़ाइल बनाएँ
ansible-vault create secrets.yml

# एन्क्रिप्टेड फ़ाइल संपादित करें
ansible-vault edit secrets.yml

# secrets.yml की सामग्री:
# db_password: supersecret123
# api_key: abc123xyz789

# प्लेबुक में उपयोग
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. रोल: जटिल स्वचालन व्यवस्थित करें

**रोल** प्लेबुक को व्यवस्थित करने का संरचित तरीका देते हैं, जिससे वे मॉड्यूलर और पुनः उपयोग योग्य बनते हैं।

#### पूरी रोल संरचना

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # डिफ़ॉल्ट वेरिएबल
    ├── vars/
    │   └── main.yml          # रोल वेरिएबल
    ├── tasks/
    │   ├── main.yml          # मुख्य टास्क सूची
    │   ├── install.yml       # इंस्टॉलेशन टास्क
    │   └── configure.yml     # कॉन्फ़िगरेशन टास्क
    ├── handlers/
    │   └── main.yml          # हैंडलर (सेवाएँ रीस्टार्ट करें)
    ├── templates/
    │   ├── nginx.conf.j2     # Jinja2 टेम्पलेट
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # स्थिर फ़ाइलें
    ├── meta/
    │   └── main.yml          # रोल निर्भरताएँ
    └── README.md             # दस्तावेज़ीकरण
```

#### रोल का उदाहरण: nginx

**defaults/main.yml:**
```yaml
---
nginx_port: 80
nginx_user: www-data
nginx_worker_processes: auto
nginx_worker_connections: 1024
```

**tasks/main.yml:**
```yaml
---
- name: OS-विशिष्ट वेरिएबल शामिल करें
  include_vars: "{{ ansible_os_family }}.yml"

- name: Nginx इंस्टॉल करें
  include_tasks: install.yml

- name: Nginx कॉन्फ़िगर करें
  include_tasks: configure.yml

- name: सुनिश्चित करें कि Nginx चल रहा है
  service:
    name: nginx
    state: started
    enabled: yes
```

**tasks/install.yml:**
```yaml
---
- name: Nginx इंस्टॉल करें (Debian)
  apt:
    name: nginx
    state: present
    update_cache: yes
  when: ansible_os_family == "Debian"

- name: Nginx इंस्टॉल करें (RedHat)
  yum:
    name: nginx
    state: present
  when: ansible_os_family == "RedHat"
```

**handlers/main.yml:**
```yaml
---
- name: nginx रीस्टार्ट करें
  service:
    name: nginx
    state: restarted

- name: nginx री-लोड करें
  service:
    name: nginx
    state: reloaded
```

**templates/nginx.conf.j2:**
```nginx
user {{ nginx_user }};
worker_processes {{ nginx_worker_processes }};

events {
    worker_connections {{ nginx_worker_connections }};
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    
    server {
        listen {{ nginx_port }};
        server_name {{ ansible_fqdn }};
        
        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

**रोल का उपयोग:**
```yaml
---
- name: Nginx भूमिका से वेब सर्वर कॉन्फ़िगर करें
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## उन्नत Ansible अवधारणाएँ (2026)

### Ansible संग्रह

**संग्रह** Ansible सामग्री, जैसे मॉड्यूल, रोल और प्लगइन, के वितरण का प्रारूप हैं।

#### संग्रह इंस्टॉल करें

```bash
# Ansible Galaxy से इंस्टॉल करें
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# requirements फ़ाइल से इंस्टॉल करें
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### संग्रह मॉड्यूल का उपयोग करें

```yaml
---
- name: कलेक्शन मॉड्यूल का उपयोग करें
  hosts: localhost
  tasks:
    - name: community.general का Docker मॉड्यूल उपयोग करें
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: AWS EC2 मॉड्यूल उपयोग करें
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (एंटरप्राइज़ सुविधाएँ)

**Ansible Tower** (वाणिज्यिक) और **AWX** (ओपन सोर्स) ये सुविधाएँ देते हैं:

- प्लेबुक चलाने के लिए वेब UI
- रोल-आधारित एक्सेस नियंत्रण (RBAC)
- कार्य शेड्यूलिंग और वर्कफ़्लो
- केंद्रीकृत लॉगिंग और ऑडिटिंग
- एकीकरण के लिए REST API
- क्रेडेंशियल प्रबंधन
- इन्वेंटरी सिंक्रोनाइज़ेशन

**Docker Compose से AWX इंस्टॉल करें:**
```bash
# AWX रिपॉज़िटरी क्लोन करें
git clone https://github.com/ansible/awx.git
cd awx

# docker-compose से तैनात करें
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# http://localhost:80 पर जाएँ
# डिफ़ॉल्ट लॉगिन: admin / password
```

### Ansible से Windows स्वचालन

2026 में Ansible का Windows समर्थन काफी बेहतर हुआ है:

**Windows की पूर्वापेक्षाएँ:**
```powershell
# Windows होस्ट पर WinRM सक्षम करें
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Windows इन्वेंटरी:**
```ini
[windows]
win1.example.com

[windows:vars]
ansible_user=Administrator
ansible_password=SecurePassword123
ansible_connection=winrm
ansible_winrm_transport=ntlm
ansible_winrm_server_cert_validation=ignore
ansible_port=5986
```

**Windows स्वचालन प्लेबुक:**
```yaml
---
- name: Windows सर्वर कॉन्फ़िगरेशन
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: IIS इंस्टॉल करें
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: वेबसाइट तैनात करें
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: फ़ायरवॉल कॉन्फ़िगर करें
      win_firewall_rule:
        name: HTTP की अनुमति दें
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: Chocolatey से सॉफ़्टवेयर इंस्टॉल करें
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### Ansible से नेटवर्क स्वचालन

Ansible Cisco, Juniper, Arista और F5 सहित प्रमुख नेटवर्क विक्रेताओं का समर्थन करता है।

**नेटवर्क उपकरण प्लेबुक:**
```yaml
---
- name: Cisco स्विच कॉन्फ़िगर करें
  hosts: cisco_switches
  gather_facts: no
  connection: network_cli
  
  vars:
    ansible_network_os: ios
    ansible_user: admin
    ansible_password: "{{ vault_switch_password }}"
  
  tasks:
    - name: VLAN कॉन्फ़िगर करें
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: DATA
          - vlan_id: 20
            name: VOICE
          - vlan_id: 30
            name: GUEST
        state: merged
    
    - name: इंटरफ़ेस कॉन्फ़िगर करें
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Uplink to Core
            enabled: true
    
    - name: कॉन्फ़िगरेशन सहेजें
      cisco.ios.ios_config:
        save_when: always
```

## वास्तविक उपयोग के मामले और उदाहरण

### उपयोग का मामला 1: पूरा वेब एप्लिकेशन परिनियोजन

**प्रोजेक्ट संरचना:**
```
webapp-deployment/
├── ansible.cfg
├── inventory/
│   ├── production
│   └── staging
├── group_vars/
│   ├── all.yml
│   ├── production.yml
│   └── staging.yml
├── roles/
│   ├── common/
│   ├── nginx/
│   ├── postgresql/
│   └── application/
└── playbooks/
    ├── site.yml
    └── deploy.yml
```

**site.yml (पूरा स्टैक परिनियोजन):**
```yaml
---
- name: सभी सर्वर कॉन्फ़िगर करें
  hosts: all
  become: yes
  roles:
    - common

- name: डेटाबेस सर्वर कॉन्फ़िगर करें
  hosts: databases
  become: yes
  roles:
    - postgresql

- name: वेब सर्वर कॉन्फ़िगर करें
  hosts: webservers
  become: yes
  roles:
    - nginx
    - application

- name: लोड बैलेंसर कॉन्फ़िगर करें
  hosts: loadbalancers
  become: yes
  roles:
    - haproxy
```

### उपयोग का मामला 2: Kubernetes क्लस्टर सेटअप

```yaml
---
- name: Kubernetes क्लस्टर सेटअप करें
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: Docker इंस्टॉल करें
      apt:
        name: docker.io
        state: present
    
    - name: Kubernetes apt कुंजी जोड़ें
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: Kubernetes रिपॉज़िटरी जोड़ें
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: Kubernetes घटक इंस्टॉल करें
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: Kubernetes मास्टर प्रारंभ करें
  hosts: k8s_master
  become: yes
  tasks:
    - name: क्लस्टर प्रारंभ करें
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: .kube डायरेक्टरी बनाएँ
      file:
        path: /home/{{ ansible_user }}/.kube
        state: directory
        owner: "{{ ansible_user }}"
    
    - name: admin.conf कॉपी करें
      copy:
        src: /etc/kubernetes/admin.conf
        dest: /home/{{ ansible_user }}/.kube/config
        remote_src: yes
        owner: "{{ ansible_user }}"
```

### उपयोग का मामला 3: सुरक्षा सख्त करने का स्वचालन

```yaml
---
- name: सुरक्षा सुदृढ़ करें
  hosts: all
  become: yes
  
  tasks:
    - name: सभी पैकेज अपडेट करें
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: सुरक्षा उपकरण इंस्टॉल करें
      apt:
        name:
          - fail2ban
          - ufw
          - aide
        state: present
    
    - name: fail2ban कॉन्फ़िगर करें
      copy:
        src: jail.local
        dest: /etc/fail2ban/jail.local
      notify: restart fail2ban
    
    - name: फ़ायरवॉल कॉन्फ़िगर करें
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: फ़ायरवॉल सक्षम करें
      ufw:
        state: enabled
    
    - name: root लॉगिन अक्षम करें
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: पासवर्ड नीति निर्धारित करें
      lineinfile:
        path: /etc/login.defs
        regexp: '^PASS_MAX_DAYS'
        line: 'PASS_MAX_DAYS   90'
  
  handlers:
    - name: fail2ban रीस्टार्ट करें
      service:
        name: fail2ban
        state: restarted
    
    - name: sshd रीस्टार्ट करें
      service:
        name: sshd
        state: restarted
```

## Ansible के श्रेष्ठ तरीके (2026 संस्करण)

### 1. वर्ज़न नियंत्रण (Git) का उपयोग करें

**रिपॉज़िटरी संरचना:**
```
ansible-infrastructure/
├── .gitignore
├── README.md
├── ansible.cfg
├── inventory/
├── group_vars/
├── host_vars/
├── roles/
├── playbooks/
└── files/
```

**.gitignore:**
```
*.retry
*.pyc
.vault_pass
secrets.yml
*.log
```

### 2. इडेम्पोटेंसी लागू करें

**गलत (इडेम्पोटेंट नहीं):**
```yaml
- name: फ़ाइल में पंक्ति जोड़ें
  shell: echo "new line" >> /etc/myconfig
```

**सही (इडेम्पोटेंट):**
```yaml
- name: सुनिश्चित करें कि पंक्ति फ़ाइल में है
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. कोड गुणवत्ता के लिए Ansible Lint का उपयोग करें

```bash
# ansible-lint इंस्टॉल करें
pip install ansible-lint

# लिंटर चलाएँ
ansible-lint playbook.yml

# सामान्य समस्याएँ अपने आप ठीक करें
ansible-lint --fix playbook.yml
```

### 4. Molecule से परीक्षण करें

```bash
# Molecule इंस्टॉल करें
pip install molecule molecule-docker

# परीक्षणों के साथ नई भूमिका शुरू करें
molecule init role my_role --driver-name docker

# परीक्षण चलाएँ
cd my_role
molecule test

# परीक्षण चरण:
# - परीक्षण वातावरण बनाएँ
# - कन्वर्ज करें (प्लेबुक चलाएँ)
# - सत्यापित करें (परीक्षण चलाएँ)
# - वातावरण नष्ट करें
```

**molecule.yml उदाहरण:**
```yaml
---
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: ubuntu2204
    image: geerlingguy/docker-ubuntu2204-ansible:latest
    pre_build_image: true
provisioner:
  name: ansible
verifier:
  name: ansible
```

### 5. चुनिंदा निष्पादन के लिए टैग का उपयोग करें

```yaml
---
- name: पूरा सर्वर सेटअप
  hosts: webservers
  become: yes
  
  tasks:
    - name: पैकेज इंस्टॉल करें
      apt:
        name: nginx
        state: present
      tags:
        - packages
        - nginx
    
    - name: Nginx कॉन्फ़िगर करें
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags:
        - configuration
        - nginx
    
    - name: एप्लिकेशन तैनात करें
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# केवल nginx टास्क चलाएँ
# ansible-playbook play.yml --tags nginx

# डिप्लॉयमेंट छोड़ें
# ansible-playbook play.yml --skip-tags deployment
```

### 6. त्रुटि प्रबंधन और डिबगिंग

```yaml
---
- name: मज़बूत टास्क निष्पादन
  hosts: webservers
  
  tasks:
    - name: जोखिम भरा ऑपरेशन आज़माएँ
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: डीबग आउटपुट
      debug:
        var: result
        verbosity: 2
    
    - name: विफलता संभालें
      debug:
        msg: "कमांड विफल हुआ, लेकिन निष्पादन जारी है..."
      when: result.rc != 0
    
    - name: rescue ब्लॉक
      block:
        - name: पहले यह आज़माएँ
          command: /may/fail
        
        - name: सफल होने पर यह करें
          debug:
            msg: "सफलता!"
      
      rescue:
        - name: विफल होने पर इसके बजाय यह करें
          debug:
            msg: "विफलता से उबर गया"
      
      always:
        - name: इसे हमेशा चलाएँ
          debug:
            msg: "सफ़ाई के कार्य"
```

### 7. प्रदर्शन अनुकूलित करें

#### Pipelining सक्षम करें
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Mitogen का उपयोग करें (3-7 गुना बेहतर प्रदर्शन)
```bash
# Mitogen इंस्टॉल करें
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

#### समानांतर निष्पादन
```yaml
---
- name: समानांतर अपडेट
  hosts: all
  strategy: free  # सभी होस्ट की प्रतीक्षा न करें
  serial: 10      # एक बार में 10 होस्ट प्रोसेस करें
  
  tasks:
    - name: पैकेज अपडेट करें
      apt:
        upgrade: dist
```

## आम समस्याओं का निवारण

### समस्या 1: SSH कनेक्शन विफलता

**समस्या:** प्रबंधित होस्ट से कनेक्ट नहीं हो पा रहा

**समाधान:**
```bash
# कच्चे SSH कनेक्शन का परीक्षण करें
ssh -vvv user@host

# Ansible कनेक्शन का परीक्षण करें
ansible host -m ping -vvv

# इन्वेंटरी में जोड़ें
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### समस्या 2: अनुमति अस्वीकृत (sudo)

**समस्या:** अनुमति त्रुटियों के कारण कार्य विफल होते हैं

**समाधान:**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: root अधिकार आवश्यक टास्क
      file:
        path: /etc/myconfig
        state: touch
```

### समस्या 3: मॉड्यूल नहीं मिला

**समस्या:** मॉड्यूल नहीं मिलने की त्रुटि

**समाधान:**
```bash
# सुनिश्चित करें कि कलेक्शन इंस्टॉल है
ansible-galaxy collection install community.general

# कलेक्शन सत्यापित करें
ansible-galaxy collection list

# FQCN (पूरी तरह योग्य कलेक्शन नाम) का उपयोग करें
community.general.docker_container:
  name: mycontainer
```

### समस्या 4: प्लेबुक धीमा चलना

**समाधान:**
1. Pipelining सक्षम करें (प्रदर्शन अनुभाग देखें)
2. Mitogen रणनीति प्लगइन का उपयोग करें
3. आवश्यकता न हो तो फ़ैक्ट संग्रह बंद करें:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. लंबे समय वाले काम के लिए असिंक्रोनस निष्पादन उपयोग करें:
   ```yaml
   - name: लंबा चलने वाला टास्क
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Ansible करियर मार्ग और प्रमाणपत्र

### कौशल की प्रगति

**शुरुआती (0-6 महीने):**
- बुनियादी प्लेबुक लिखें
- इन्वेंटरी और चर समझें
- सामान्य मॉड्यूल का उपयोग करें
- प्लेबुक चलाएँ

**मध्यवर्ती (6-18 महीने):**
- पुनः उपयोग योग्य रोल बनाएँ
- त्रुटि प्रबंधन लागू करें
- Ansible Vault का उपयोग करें
- CI/CD के साथ एकीकरण करें
- कई वातावरण प्रबंधित करें

**उन्नत (18 महीने से अधिक):**
- जटिल स्वचालन ढाँचे डिज़ाइन करें
- कस्टम मॉड्यूल और प्लगइन बनाएँ
- Tower/AWX परिनियोजन की रूपरेखा बनाएँ
- प्रदर्शन अनुकूलित करें
- दूसरों को मार्गदर्शन दें

### प्रमाणपत्र

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Ansible में दक्षता दिखाता है
- व्यावहारिक कार्य-आधारित परीक्षा
- 3 वर्ष के लिए मान्य
- उद्योग में मान्यता प्राप्त

**तैयारी के संसाधन:**
- Red Hat Learning Subscription
- Ansible दस्तावेज़
- अभ्यास लैब (A Cloud Guru, Udemy)
- समुदाय फ़ोरम

### नौकरी का बाज़ार (2026)

**अमेरिका में औसत वेतन:**
- जूनियर Ansible इंजीनियर: $75,000-$95,000
- मध्य-स्तर DevOps इंजीनियर (Ansible): $110,000-$140,000
- वरिष्ठ स्वचालन आर्किटेक्ट: $150,000-$190,000

**मांग वाले कौशल:**
- Ansible और Kubernetes
- Ansible और Terraform (हाइब्रिड IaC)
- Ansible और CI/CD (Jenkins, GitLab)
- Ansible और क्लाउड (AWS, Azure, GCP)
- Ansible Tower/AWX प्रशासन

## सीखने के संसाधन और समुदाय

### आधिकारिक दस्तावेज़
- [Ansible दस्तावेज़](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - रोल साझा करने का प्लेटफ़ॉर्म
- [GitHub पर Ansible](https://github.com/ansible/ansible)

### ऑनलाइन पाठ्यक्रम
- Red Hat Learning Subscription
- Udemy: `बिल्कुल शुरुआती लोगों के लिए Ansible`
- A Cloud Guru: `व्यावहारिक Ansible`
- Linux Academy: `Ansible क्विक स्टार्ट`

### पुस्तकें
- Jeff Geerling की `Ansible for DevOps` (2025 में अपडेट)
- Lorin Hochstein की `Ansible: Up and Running`
- James Freeman की `Mastering Ansible`

### समुदाय
- [Ansible मेलिंग सूची](https://groups.google.com/forum/#!forum/ansible-project)
- [Reddit पर Ansible](https://reddit.com/r/ansible)
- [Ansible Discord सर्वर](https://discord.gg/ansible)
- स्थानीय और ऑनलाइन Ansible मीटअप

### अभ्यास प्लेटफ़ॉर्म
- [Katacoda Ansible परिदृश्य](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Vagrant या Docker से स्थानीय लैब

## निष्कर्ष: Ansible के साथ शुरुआत करें

Ansible दुनिया भर के संगठनों का पसंदीदा स्वचालन टूल बन गया है। 2026 में इसमें अधिक क्षमताएँ, आसान Windows प्रबंधन, बेहतर क्लाउड एकीकरण और AI-सहायता वाला प्लेबुक निर्माण शामिल है। पारंपरिक इंफ्रास्ट्रक्चर, क्लाउड वातावरण या हाइब्रिड परिनियोजन प्रबंधित करने पर भी Ansible कौशल आपके IT करियर में उपयोगी रहेंगे।

**मुख्य बातें:**

1. **सरल शुरुआत करें**: कुछ सर्वर प्रबंधित करने वाले बुनियादी प्लेबुक बनाएँ
2. **नियमित अभ्यास करें**: घर पर लैब सेट करें और प्रयोग करें
3. **करके सीखें**: रोज़मर्रा के वास्तविक काम स्वचालित करें
4. **श्रेष्ठ तरीकों का पालन करें**: वर्ज़न नियंत्रण, परीक्षण और दस्तावेज़ीकरण करें
5. **समुदाय से जुड़ें**: दूसरों से सीखें और ज्ञान साझा करें
6. **अपडेट रहें**: Ansible तेज़ी से विकसित होता है, सीखते रहें
7. **टूल मिलाएँ**: Ansible, Terraform और Kubernetes से व्यापक स्वचालन संभव होता है

**अगले कदम:**

1. अपने सिस्टम पर Ansible इंस्टॉल करें
2. परीक्षण सर्वर, वर्चुअल मशीन या कंटेनर की सरल इन्वेंटरी बनाएँ
3. पैकेज इंस्टॉल करने वाला अपना पहला प्लेबुक लिखें
4. टेम्पलेट, चर और रोल जोड़कर धीरे-धीरे जटिलता बढ़ाएँ
5. Ansible Galaxy पर समुदाय के रोल में योगदान दें
6. अपने कौशल की पुष्टि के लिए प्रमाणपत्र पर विचार करें

Ansible के शुरुआती उपयोगकर्ता से विशेषज्ञ तक का सफर संतोषजनक है और DevOps, SRE तथा क्लाउड इंजीनियरिंग के अवसर खोलता है। इस गाइड की मूल बातों से आप इंफ्रास्ट्रक्चर स्वचालन शुरू कर सकते हैं और आधुनिक IT क्षेत्र के लिए उपयोगी कौशल बना सकते हैं।

Ansible के साथ इंफ्रास्ट्रक्चर स्वचालन की दुनिया में आपका स्वागत है!

______

## संदर्भ

- [Ansible आधिकारिक दस्तावेज़](https://docs.ansible.com/)
- [Ansible Galaxy - रोल रिपॉज़िटरी](https://galaxy.ansible.com/)
- [GitHub पर Ansible रिपॉज़िटरी](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - ओपन-सोर्स Ansible Tower](https://github.com/ansible/awx)
- [Ansible के श्रेष्ठ तरीके](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Molecule परीक्षण ढाँचा](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Jeff Geerling की Ansible for DevOps](https://www.ansiblefordevops.com/)
- [Ansible संग्रह सूची](https://docs.ansible.com/ansible/latest/collections/index.html)
