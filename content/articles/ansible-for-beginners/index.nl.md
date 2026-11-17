---
title: "Ansible voor beginners 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-13
description: "Een Ansible-gids voor 2026 over installatie, playbooks, rollen, voorbeelden, aanbevolen werkwijzen en vergelijkingen met Terraform, Puppet en Chef."
tags: ["Introductie tot Ansible", "IT-infrastructuurbeheer automatiseren", "Ansible-basis", "IT-infrastructuurautomatisering", "Configuratiebeheer", "Applicatie-implementatie", "Inrichting", "Continue levering", "Naleving van beveiligingseisen", "Orkestratie", "YAML", "Ansible-modules", "Rollen", "Aanbevolen werkwijzen", "Versiebeheer", "Testen", "Red Hat", "Systeembeheerders", "Linux", "macOS", "Windows", "Ansible-installatie", "Ansible-inventaris", "Ansible-playbooks", "Ansible-modules", "Ansible-rollen", "Ansible-aanbevelingen", "Ansible-testen", "IT-infrastructuurautomatiseringstool", "Ansible-handleiding", "Automatisering van infrastructuurbeheer", "Ansible voor beginners", "Ansible leren", "Ansible-handleiding 2026", "Ansible versus Terraform", "Ansible versus Puppet", "Voorbeelden van Ansible-playbooks", "Ansible-automatisering", "DevOps-hulpmiddelen", "Infrastructuur als code", "Ansible AWX", "Ansible Tower", "Ansible-collecties", "Ansible Galaxy", "Ansible Vault", "Ansible-cloudautomatisering"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "Een illustratie van moderne IT-infrastructuur met verbonden servers en apparaten, waarop SSH- en WinRM-verbindingen, een gestileerd YAML-bestand en pictogrammen voor clouddiensten tegen een donkere achtergrond staan."
coverCaption: ""
---

**Ansible voor beginners: complete gids voor IT-automatisering in 2026**

Ansible is uitgegroeid tot een toonaangevend automatiseringsplatform dat volgens de bron door meer dan 80% van de Fortune 500-bedrijven wordt vertrouwd voor het beheer van complexe IT-infrastructuur. In 2026 blijft Ansible een belangrijke automatiseringsoplossing, met eenvoudige bediening en functies voor grote organisaties.

Deze uitgebreide handleiding brengt je van beginner tot zelfverzekerde Ansible-gebruiker. Je leert de basis, geavanceerde technieken, praktijkvoorbeelden en aanbevolen werkwijzen voor 2026.

## Wat is Ansible? De basis begrijpen

**Ansible** is een opensource-automatiseringsplatform dat het beheer van IT-infrastructuur vereenvoudigt met agentloze, declaratieve automatisering. Anders dan traditionele configuratiebeheertools vereist Ansible geen agenten op beheerde nodes. Het gebruikt SSH voor Linux en Unix of WinRM voor Windows voor beheer op afstand.

{{< youtube id="goclfp6a2IQ" >}}

### Belangrijkste kenmerken van Ansible

**1. Architectuur zonder agenten:**
- Geen software-installatie nodig op beheerde nodes
- Gebruikt bestaande SSH- of WinRM-protocollen
- Verkleint het aanvalsoppervlak en de onderhoudslast
- Eenvoudiger om mee te beginnen dan met tools die agenten vereisen

**2. Declaratieve taal (YAML):**
- Configuratiebestanden die mensen kunnen lezen
- Infrastructuur beschreven als gewenste toestand
- Idempotente bewerkingen, veilig meerdere keren uit te voeren
- Begrijpelijk voor mensen zonder programmeerervaring

**3. Pushmodel:**
- Het controlenode stuurt configuraties naar beheerde nodes
- Voert taken direct uit, zonder op agenten te wachten
- Gecentraliseerde controle en zichtbaarheid
- Geschikt voor automatisering op aanvraag

**4. Uitgebreide modulebibliotheek:**
- Meer dan 5.000 ingebouwde modules (stand 2026)
- Ondersteunt Linux, Windows, netwerkapparaten en cloudplatforms
- Modules van de community en leveranciers
- Eenvoudig eigen modules in Python schrijven

### Wat kan Ansible automatiseren?

Ansible is geschikt voor automatisering van:

- **Configuratiebeheer**: serverconfiguraties consistent houden
- **Applicatie-implementatie**: applicaties in verschillende omgevingen uitrollen
- **Inrichting**: infrastructuur aanmaken en configureren
- **Continue levering**: integreren met CI/CD-pijplijnen
- **Beveiliging en naleving**: beveiligingsbeleid en naleving afdwingen
- **Orkestratie**: complexe implementaties met meerdere lagen coördineren
- **Cloudautomatisering**: AWS, Azure, GCP en andere clouds beheren
- **Netwerkautomatisering**: switches, routers en firewalls configureren
- **Windows-automatisering**: Windows-servers en werkstations beheren

### De ontwikkeling van Ansible: 2012 tot 2026

**Tijdlijn:**
- **2012**: Michael DeHaan maakt Ansible
- **2015**: Red Hat neemt Ansible over
- **2019**: Ansible Engine 2.8 introduceert Collections
- **2020**: Ansible 2.10+ wordt opgesplitst in ansible-core en Collections
- **2023**: Ansible 8.x krijgt uitgebreidere cloudintegraties
- **2026**: Ansible 10.x krijgt AI-ondersteunde generatie van playbooks, betere Windows-ondersteuning en uitgebreidere beveiligingsfuncties

## Ansible vergelijken met concurrenten

| Functie | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **Type** | Configuratiebeheer | Infrastructuurinrichting | Configuratiebeheer | Configuratiebeheer |
| **Taal** | YAML | HCL | Puppet DSL (Ruby-achtig) | Ruby DSL |
| **Agent vereist** | Nee | Nee | Ja | Ja |
| **Leercurve** | Eenvoudig | Gemiddeld | Steil | Steil |
| **Geschikt voor** | Configuratiebeheer, implementatie | Cloudinfrastructuur | Grote organisaties | Complexe workflows |
| **Statusbeheer** | Pushmodel | Declaratief statusbestand | Pullmodel | Pullmodel |
| **Windows-ondersteuning** | Uitstekend (2026) | Beperkt | Goed | Goed |
| **Communityomvang** | Zeer groot | Zeer groot | Groot | Gemiddeld |
| **Belangrijkste toepassing** | Dagelijks beheer | Inrichting van infrastructuur | Configuratie voor grote organisaties | Applicatie-implementatie |

**Wanneer kies je Ansible?**
- ✅ Configuratiebeheer in hybride omgevingen
- ✅ Automatisering van applicatie-implementaties
- ✅ Een korte leercurve is nodig
- ✅ De voorkeur gaat uit naar een architectuur zonder agenten
- ✅ Sterke Windows-automatisering nodig is (verbeteringen in 2026)
- ✅ Er al SSH-infrastructuur is

**Wanneer overweeg je alternatieven?**
- Terraform: vooral voor infrastructuurinrichting (AWS, Azure, GCP)
- Puppet: grote organisaties met duizenden nodes
- Chef: complexe workflows rond applicaties

## Aan de slag: Ansible installeren in 2026

### Systeemvereisten

**Controlenode (waar Ansible draait):**
- Linux, macOS of WSL2 op Windows
- Python 3.9 of hoger (Python 3.11+ aanbevolen voor 2026)
- Minimaal 2 GB RAM, 4 GB of meer aanbevolen
- 5 GB schijfruimte voor Collections

**Beheerde nodes:**
- SSH-toegang (Linux/Unix) of WinRM (Windows)
- Python 2.7 of Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- Geen agentinstallatie nodig

### Installatiemethoden

#### Methode 1: pakketbeheerder (aanbevolen voor beginners)

**Ubuntu/Debian:**
```bash
# Ansible-PPA voor de nieuwste versie toevoegen
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux:**
```bash
# EPEL-repository inschakelen
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS:**
```bash
# Homebrew gebruiken
brew install ansible
```

#### Methode 2: Python pip (nieuwste functies)

```bash
# pipx installeren (aanbevolen geïsoleerde omgeving)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Ansible installeren met pipx
pipx install --include-deps ansible

# Installatie controleren
ansible --version
```

#### Methode 3: Docker (draagbaar)

```bash
# Officiële Ansible-container ophalen
docker pull quay.io/ansible/ansible:latest

# Ansible in een container uitvoeren
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### De installatie controleren

```bash
# Ansible-versie controleren
ansible --version

# Verwachte uitvoer (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### Eerste configuratie

Maak het configuratiebestand voor Ansible aan:

```bash
# Configuratiemap aanmaken
mkdir -p ~/.ansible

# ansible.cfg aanmaken
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

## Essentiële concepten: de bouwstenen van Ansible

### 1. Inventaris: je infrastructuur definiëren

Een **inventaris** bevat de hosts en groepen die Ansible beheert. Een inventaris kan statisch zijn (INI- of YAML-bestand) of dynamisch (scripts of plugins).

#### Statische inventaris (INI-indeling)

```ini
# inventory/hosts.ini

# Webservergroep
[webservers]
web1.example.com
web2.example.com
web3.example.com

# Databaseservergroep
[databases]
db1.example.com ansible_host=192.168.1.100
db2.example.com ansible_host=192.168.1.101

# Loadbalancers
[loadbalancers]
lb1.example.com

# Groep van groepen
[production:children]
webservers
databases
loadbalancers

# Variabelen voor alle webservers
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# Variabelen voor alle hosts
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### Statische inventaris (YAML-indeling, aanbevolen in 2026)

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

#### Dynamische inventaris (cloudproviders)

Gebruik voor cloudomgevingen dynamische inventarisplugins:

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

### 2. Playbooks: blauwdrukken voor automatisering

**Playbooks** zijn YAML-bestanden die automatiseringsworkflows beschrijven. Ze leggen de gewenste toestand van je infrastructuur vast.

#### Eenvoudig voorbeeld van een playbook

```yaml
# simple_playbook.yml
---
- name: Webservers configureren
  hosts: webservers
  become: yes
  
  tasks:
    - name: Nginx installeren
      apt:
        name: nginx
        state: present
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Nginx starten en inschakelen
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Website-inhoud kopiëren
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: Firewall configureren
      ufw:
        rule: allow
        port: '{{ item }}'
        proto: tcp
      loop:
        - 80
        - 443
```

#### Playbooks uitvoeren

```bash
# Basisuitvoering
ansible-playbook simple_playbook.yml

# Met specifieke inventaris
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# Beperken tot specifieke hosts
ansible-playbook simple_playbook.yml --limit web1.example.com

# Proefrun (checkmodus)
ansible-playbook simple_playbook.yml --check

# Uitgebreide uitvoer voor probleemoplossing
ansible-playbook simple_playbook.yml -vvv
```

### 3. Modules: herbruikbare taakeenheden

Ansible-modules vormen de bouwstenen van automatisering. Elke module voert een specifieke taak uit.

#### Veelgebruikte modules (2026)

**Systeemmodules:**
```yaml
# Pakketbeheer
- name: Pakketten installeren (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# Servicebeheer
- name: Services beheren
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**Bestandsmodules:**
```yaml
# Bestandsbewerkingen
- name: Map aanmaken
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# Bestanden kopiëren
- name: Configuratie implementeren
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# Sjabloon met variabelen
- name: nginx-configuratie implementeren
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**Cloudmodules (AWS-voorbeeld):**
```yaml
# EC2-instantie aanmaken
- name: EC2-instantie starten
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

# S3-bucket aanmaken
- name: S3-bucket aanmaken
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**Databasemodules:**
```yaml
# MySQL-databasebeheer
- name: MySQL-database aanmaken
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: MySQL-gebruiker aanmaken
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. Variabelen: playbooks flexibel maken

Met variabelen kun je playbooks in verschillende omgevingen hergebruiken.

#### Prioriteit van variabelen (hoog naar laag)

1. Extra variabelen (`-e` op de opdrachtregel)
2. Taakvariabelen
3. Blokvariabelen
4. Rol- en includevariabelen
5. Playvariabelen
6. Hostfeiten
7. `host_vars` van het playbook
8. `group_vars` van het playbook
9. `host_vars` van de inventaris
10. `group_vars` van de inventaris
11. Standaardwaarden van rollen

#### Voorbeelden van variabelen

**Playbookvariabelen:**
```yaml
---
- name: Applicatie implementeren
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: "{{ app_name }} versie {{ app_version }} implementeren"
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (omgevingsspecifiek):**
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

**Ansible Vault (versleutelde variabelen):**
```bash
# Versleuteld bestand aanmaken
ansible-vault create secrets.yml

# Versleuteld bestand bewerken
ansible-vault edit secrets.yml

# Inhoud van secrets.yml:
# db_password: supersecret123
# api_key: abc123xyz789

# In playbook gebruiken
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. Rollen: complexe automatisering ordenen

**Rollen** bieden een gestructureerde manier om playbooks te ordenen. Zo worden ze modulair en herbruikbaar.

#### Complete rolstructuur

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # Standaardvariabelen
    ├── vars/
    │   └── main.yml          # Rolvariabelen
    ├── tasks/
    │   ├── main.yml          # Hoofdtakenlijst
    │   ├── install.yml       # Installatietaken
    │   └── configure.yml     # Configuratietaken
    ├── handlers/
    │   └── main.yml          # Handlers (services opnieuw starten)
    ├── templates/
    │   ├── nginx.conf.j2     # Jinja2-sjablonen
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # Statische bestanden
    ├── meta/
    │   └── main.yml          # Rolafhankelijkheden
    └── README.md             # Documentatie
```

#### Voorbeeldrol: nginx

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
- name: OS-specifieke variabelen opnemen
  include_vars: "{{ ansible_os_family }}.yml"

- name: Nginx installeren
  include_tasks: install.yml

- name: Nginx configureren
  include_tasks: configure.yml

- name: Controleren of Nginx actief is
  service:
    name: nginx
    state: started
    enabled: yes
```

**tasks/install.yml:**
```yaml
---
- name: Nginx installeren (Debian)
  apt:
    name: nginx
    state: present
    update_cache: yes
  when: ansible_os_family == "Debian"

- name: Nginx installeren (RedHat)
  yum:
    name: nginx
    state: present
  when: ansible_os_family == "RedHat"
```

**handlers/main.yml:**
```yaml
---
- name: nginx opnieuw starten
  service:
    name: nginx
    state: restarted

- name: nginx opnieuw laden
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

**De rol gebruiken:**
```yaml
---
- name: Webservers configureren met de Nginx-rol
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## Geavanceerde Ansible-concepten (2026)

### Ansible-collecties

**Collecties** zijn een distributieformaat voor Ansible-inhoud, zoals modules, rollen en plug-ins.

#### Collecties installeren

```bash
# Installeren via Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# Installeren vanuit requirements-bestand
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### Modules uit collecties gebruiken

```yaml
---
- name: Collectiemodules gebruiken
  hosts: localhost
  tasks:
    - name: Docker-module van community.general gebruiken
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: AWS EC2-module gebruiken
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (functies voor bedrijven)

**Ansible Tower** (commercieel) en **AWX** (open source) bieden:

- Een webinterface om playbooks uit te voeren
- Toegangsbeheer op basis van rollen (RBAC)
- Taakplanning en workflows
- Gecentraliseerde logging en controle
- Een REST-API voor integratie
- Beheer van inloggegevens
- Synchronisatie van inventarissen

**AWX installeren met Docker Compose:**
```bash
# AWX-repository klonen
git clone https://github.com/ansible/awx.git
cd awx

# Implementeren met docker-compose
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# Ga naar http://localhost:80
# Standaardaanmelding: admin / password
```

### Ansible voor Windows-automatisering

Ansible biedt in 2026 aanzienlijk betere ondersteuning voor Windows:

**Vereisten voor Windows:**
```powershell
# WinRM inschakelen op Windows-host
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Inventaris voor Windows:**
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

**Playbook voor Windows-automatisering:**
```yaml
---
- name: Windows-serverconfiguratie
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: IIS installeren
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: Website implementeren
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: Firewall configureren
      win_firewall_rule:
        name: HTTP toestaan
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: Software installeren via Chocolatey
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### Netwerkautomatisering met Ansible

Ansible ondersteunt grote netwerkleveranciers, waaronder Cisco, Juniper, Arista en F5.

**Playbook voor netwerkapparaten:**
```yaml
---
- name: Cisco-switches configureren
  hosts: cisco_switches
  gather_facts: no
  connection: network_cli
  
  vars:
    ansible_network_os: ios
    ansible_user: admin
    ansible_password: "{{ vault_switch_password }}"
  
  tasks:
    - name: VLANs configureren
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: DATA
          - vlan_id: 20
            name: VOICE
          - vlan_id: 30
            name: GUEST
        state: merged
    
    - name: Interface configureren
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Uplink to Core
            enabled: true
    
    - name: Configuratie opslaan
      cisco.ios.ios_config:
        save_when: always
```

## Praktijkvoorbeelden en toepassingen

### Toepassing 1: een complete webapplicatie implementeren

**Projectstructuur:**
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

**site.yml (implementatie van de volledige stack):**
```yaml
---
- name: Alle servers configureren
  hosts: all
  become: yes
  roles:
    - common

- name: Databaseservers configureren
  hosts: databases
  become: yes
  roles:
    - postgresql

- name: Webservers configureren
  hosts: webservers
  become: yes
  roles:
    - nginx
    - application

- name: Loadbalancers configureren
  hosts: loadbalancers
  become: yes
  roles:
    - haproxy
```

### Toepassing 2: een Kubernetes-cluster opzetten

```yaml
---
- name: Kubernetes-cluster instellen
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: Docker installeren
      apt:
        name: docker.io
        state: present
    
    - name: Kubernetes apt-sleutel toevoegen
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: Kubernetes-repository toevoegen
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: Kubernetes-componenten installeren
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: Kubernetes-master initialiseren
  hosts: k8s_master
  become: yes
  tasks:
    - name: Cluster initialiseren
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: .kube-map aanmaken
      file:
        path: /home/{{ ansible_user }}/.kube
        state: directory
        owner: "{{ ansible_user }}"
    
    - name: admin.conf kopiëren
      copy:
        src: /etc/kubernetes/admin.conf
        dest: /home/{{ ansible_user }}/.kube/config
        remote_src: yes
        owner: "{{ ansible_user }}"
```

### Toepassing 3: beveiliging automatiseren

```yaml
---
- name: Beveiliging versterken
  hosts: all
  become: yes
  
  tasks:
    - name: Alle pakketten bijwerken
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: Beveiligingstools installeren
      apt:
        name:
          - fail2ban
          - ufw
          - aide
        state: present
    
    - name: fail2ban configureren
      copy:
        src: jail.local
        dest: /etc/fail2ban/jail.local
      notify: restart fail2ban
    
    - name: Firewall configureren
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: Firewall inschakelen
      ufw:
        state: enabled
    
    - name: Rootaanmelding uitschakelen
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: Wachtwoordbeleid instellen
      lineinfile:
        path: /etc/login.defs
        regexp: '^PASS_MAX_DAYS'
        line: 'PASS_MAX_DAYS   90'
  
  handlers:
    - name: fail2ban opnieuw starten
      service:
        name: fail2ban
        state: restarted
    
    - name: sshd opnieuw starten
      service:
        name: sshd
        state: restarted
```

## Aanbevolen werkwijzen voor Ansible (editie 2026)

### 1. Gebruik versiebeheer (Git)

**Structuur van de repository:**
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

### 2. Maak bewerkingen idempotent

**Slecht (niet-idempotent):**
```yaml
- name: Regel aan bestand toevoegen
  shell: echo "new line" >> /etc/myconfig
```

**Goed (idempotent):**
```yaml
- name: Controleren of de regel in het bestand staat
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. Gebruik Ansible Lint voor codekwaliteit

```bash
# ansible-lint installeren
pip install ansible-lint

# Linter uitvoeren
ansible-lint playbook.yml

# Veelvoorkomende problemen automatisch oplossen
ansible-lint --fix playbook.yml
```

### 4. Test met Molecule

```bash
# Molecule installeren
pip install molecule molecule-docker

# Nieuwe rol met tests initialiseren
molecule init role my_role --driver-name docker

# Tests uitvoeren
cd my_role
molecule test

# Testfasen:
# - Testomgeving aanmaken
# - Convergeren (playbook uitvoeren)
# - Verifiëren (tests uitvoeren)
# - Omgeving vernietigen
```

**Voorbeeld van molecule.yml:**
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

### 5. Gebruik tags voor selectieve uitvoering

```yaml
---
- name: Volledige server instellen
  hosts: webservers
  become: yes
  
  tasks:
    - name: Pakketten installeren
      apt:
        name: nginx
        state: present
      tags:
        - packages
        - nginx
    
    - name: Nginx configureren
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags:
        - configuration
        - nginx
    
    - name: Applicatie implementeren
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# Alleen nginx-taken uitvoeren
# ansible-playbook play.yml --tags nginx

# Implementatie overslaan
# ansible-playbook play.yml --skip-tags deployment
```

### 6. Foutafhandeling en foutopsporing

```yaml
---
- name: Robuuste taakuitvoering
  hosts: webservers
  
  tasks:
    - name: Riskante bewerking proberen
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: Debuguitvoer
      debug:
        var: result
        verbosity: 2
    
    - name: Fout afhandelen
      debug:
        msg: "Opdracht mislukt, maar wordt voortgezet..."
      when: result.rc != 0
    
    - name: Blok met herstel
      block:
        - name: Probeer dit eerst
          command: /may/fail
        
        - name: Voer dit uit bij succes
          debug:
            msg: "Geslaagd!"
      
      rescue:
        - name: Voer dit in plaats daarvan uit bij een fout
          debug:
            msg: "Hersteld na de fout"
      
      always:
        - name: Altijd uitvoeren
          debug:
            msg: "Opschoonwerkzaamheden"
```

### 7. Prestaties verbeteren

#### Pipelining inschakelen
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Mitogen gebruiken (3-7 keer sneller)
```bash
# Mitogen installeren
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

#### Parallelle uitvoering
```yaml
---
- name: Parallelle updates
  hosts: all
  strategy: free  # Niet op alle hosts wachten
  serial: 10      # 10 hosts tegelijk verwerken
  
  tasks:
    - name: Pakketten bijwerken
      apt:
        upgrade: dist
```

## Veelvoorkomende problemen oplossen

### Probleem 1: SSH-verbindingsfouten

**Probleem:** je kunt geen verbinding maken met beheerde hosts

**Oplossingen:**
```bash
# Ruwe SSH-verbinding testen
ssh -vvv user@host

# Ansible-verbinding testen
ansible host -m ping -vvv

# Aan inventaris toevoegen
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### Probleem 2: Toegang geweigerd (sudo)

**Probleem:** taken mislukken door machtigingsfouten

**Oplossing:**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: Taak waarvoor rootrechten nodig zijn
      file:
        path: /etc/myconfig
        state: touch
```

### Probleem 3: Module niet gevonden

**Probleem:** meldingen dat een module niet is gevonden

**Oplossing:**
```bash
# Controleren of de collectie is geïnstalleerd
ansible-galaxy collection install community.general

# Collectie verifiëren
ansible-galaxy collection list

# FQCN (volledig gekwalificeerde collectienaam) gebruiken
community.general.docker_container:
  name: mycontainer
```

### Probleem 4: Playbook wordt langzaam uitgevoerd

**Oplossingen:**
1. Schakel pipelining in (zie het gedeelte Prestaties)
2. Gebruik de Mitogen-strategieplug-in
3. Schakel feiten verzamelen uit als je dit niet nodig hebt:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. Gebruik asynchrone uitvoering voor langlopende taken:
   ```yaml
   - name: Langlopende taak
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Loopbaanpad en certificeringen voor Ansible

### Vaardigheden opbouwen

**Beginner (0-6 maanden):**
- Schrijf eenvoudige playbooks
- Begrijp inventarissen en variabelen
- Gebruik gangbare modules
- Voer playbooks uit

**Gevorderd (6-18 maanden):**
- Maak herbruikbare rollen
- Implementeer foutafhandeling
- Gebruik Ansible Vault
- Integreer met CI/CD
- Beheer meerdere omgevingen

**Expert (18+ maanden):**
- Ontwerp complexe automatiseringsframeworks
- Maak eigen modules en plug-ins
- Ontwerp Tower/AWX-implementaties
- Optimaliseer prestaties
- Begeleid anderen

### Certificeringen

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Toont kennis van Ansible aan
- Praktijkgericht examen
- Drie jaar geldig
- Erkend in de branche

**Studiemateriaal:**
- Red Hat Learning Subscription
- Ansible-documentatie
- Oefenlabs (A Cloud Guru, Udemy)
- Communityforums

### Arbeidsmarkt (2026)

**Gemiddelde salarissen in de VS:**
- Junior Ansible-engineer: $75.000-$95.000
- DevOps-engineer op mediorniveau (Ansible): $110.000-$140.000
- Senior automatiseringsarchitect: $150.000-$190.000

**Veelgevraagde vaardigheden:**
- Ansible en Kubernetes
- Ansible en Terraform (hybride IaC)
- Ansible en CI/CD (Jenkins, GitLab)
- Ansible en cloud (AWS, Azure, GCP)
- Beheer van Ansible Tower/AWX

## Leermiddelen en community

### Officiële documentatie
- [Ansible-documentatie](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - platform om rollen te delen
- [Ansible op GitHub](https://github.com/ansible/ansible)

### Onlinecursussen
- Red Hat Learning Subscription
- Udemy: "Ansible voor absolute beginners"
- A Cloud Guru: "Praktisch aan de slag met Ansible"
- Linux Academy: "Ansible snelstart"

### Boeken
- "Ansible for DevOps" van Jeff Geerling (bijgewerkt in 2025)
- "Ansible: Up and Running" van Lorin Hochstein
- "Mastering Ansible" van James Freeman

### Community
- [Ansible-mailinglijst](https://groups.google.com/forum/#!forum/ansible-project)
- [Ansible op Reddit](https://reddit.com/r/ansible)
- [Ansible Discord-server](https://discord.gg/ansible)
- Ansible-bijeenkomsten, lokaal en online

### Oefenplatforms
- [Katacoda Ansible-scenario's](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Een lokaal lab met Vagrant of Docker

## Conclusie: begin met je Ansible-traject

Ansible is uitgegroeid tot een veelgebruikte automatiseringstool voor organisaties. In 2026 biedt het meer mogelijkheden, eenvoudiger Windows-beheer, betere cloudintegraties en AI-ondersteunde generatie van playbooks. De vaardigheden die je met Ansible opdoet, zijn bruikbaar in je IT-loopbaan. Je kunt traditionele infrastructuur, cloudomgevingen of hybride implementaties beheren.

**Belangrijkste punten:**

1. **Begin eenvoudig**: start met eenvoudige playbooks voor enkele servers
2. **Oefen regelmatig**: richt een homelab in en experimenteer
3. **Leer door te doen**: automatiseer echte taken uit je dagelijkse werk
4. **Volg aanbevolen werkwijzen**: gebruik versiebeheer, tests en documentatie
5. **Sluit je aan bij de community**: leer van anderen en deel je kennis
6. **Blijf bij**: Ansible verandert snel, blijf leren
7. **Combineer tools**: Ansible, Terraform en Kubernetes bieden samen uitgebreide automatisering

**Volgende stappen:**

1. Installeer Ansible op je systeem
2. Maak een eenvoudige inventaris met testservers, zoals virtuele machines of containers
3. Schrijf je eerste playbook voor de installatie van een pakket
4. Voeg stap voor stap complexiteit toe met sjablonen, variabelen en rollen
5. Draag bij aan communityrollen op Ansible Galaxy
6. Overweeg een certificering om je vaardigheden aan te tonen

De reis van Ansible-beginner naar expert is lonend en biedt toegang tot functies in DevOps, SRE en cloud engineering. Met de basis uit deze handleiding kun je infrastructuur automatiseren en vaardigheden opbouwen die waardevol zijn in de moderne IT-sector.

Welkom in de wereld van infrastructuurautomatisering met Ansible!

______

## Bronnen

- [Officiële Ansible-documentatie](https://docs.ansible.com/)
- [Ansible Galaxy - repository voor rollen](https://galaxy.ansible.com/)
- [Ansible-repository op GitHub](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - opensource-Ansible Tower](https://github.com/ansible/awx)
- [Aanbevolen werkwijzen voor Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Testframework Molecule](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Ansible for DevOps van Jeff Geerling](https://www.ansiblefordevops.com/)
- [Index van Ansible-collecties](https://docs.ansible.com/ansible/latest/collections/index.html)
