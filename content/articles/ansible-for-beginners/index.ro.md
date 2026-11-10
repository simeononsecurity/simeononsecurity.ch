---
title: "Ansible pentru începători 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-08
description: "Ghid Ansible pentru 2026 despre instalare, playbook-uri, roluri, exemple, bune practici și comparații cu Terraform, Puppet și Chef."
tags: ["Introducere în Ansible", "Automatizarea gestionării infrastructurii IT", "Noțiuni de bază despre Ansible", "Automatizarea infrastructurii IT", "Gestionarea configurației", "Implementarea aplicațiilor", "Provisionare", "Livrare continuă", "Securitate și conformitate", "Orchestrare", "YAML", "Module Ansible", "Roluri", "Bune practici", "Controlul versiunilor", "Testare", "Red Hat", "Administratori de sistem", "Linux", "macOS", "Windows", "Instalarea Ansible", "Inventar Ansible", "Playbook-uri Ansible", "Module Ansible", "Roluri Ansible", "Bune practici Ansible", "Testarea Ansible", "Instrument de automatizare a infrastructurii IT", "Tutorial Ansible", "Automatizarea gestionării infrastructurii", "Ansible pentru începători", "Învățarea Ansible", "Tutorial Ansible 2026", "Ansible și Terraform", "Ansible și Puppet", "Exemple de playbook-uri Ansible", "Automatizare cu Ansible", "Instrumente DevOps", "Infrastructure as Code", "Ansible AWX", "Ansible Tower", "Colecții Ansible", "Ansible Galaxy", "Ansible Vault", "Automatizare cloud cu Ansible"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "Ilustrație a unei infrastructuri IT moderne, cu servere și dispozitive interconectate. Prezintă conexiuni SSH și WinRM, un fișier YAML stilizat și pictograme ale serviciilor cloud pe un fundal întunecat."
coverCaption: ""
---

**Ansible pentru începători: ghid complet de automatizare IT pentru 2026**

Ansible a devenit o platformă de automatizare de top. Potrivit sursei, peste 80% dintre companiile Fortune 500 o folosesc pentru a gestiona infrastructuri IT complexe. În 2026, Ansible rămâne o soluție importantă, ușor de utilizat și cu funcții pentru companii.

Acest ghid te ajută să treci de la noțiunile de bază la utilizarea sigură a Ansible. Acoperă conceptele fundamentale, tehnicile avansate, exemplele practice și bunele practici pentru 2026.

## Ce este Ansible? Noțiuni de bază

**Ansible** este o platformă open source de automatizare care simplifică gestionarea infrastructurii IT prin automatizare declarativă fără agenți. Spre deosebire de instrumentele tradiționale de gestionare a configurației, nu necesită agenți pe nodurile gestionate. Folosește SSH pentru Linux și Unix sau WinRM pentru Windows pentru gestionarea de la distanță.

{{< youtube id="goclfp6a2IQ" >}}

### Caracteristici principale ale Ansible

**1. Arhitectură fără agenți:**
- Nu necesită instalarea de software pe nodurile gestionate
- Folosește protocoalele SSH sau WinRM existente
- Reduce suprafața de atac și efortul de întreținere
- Este mai ușor de folosit decât instrumentele bazate pe agenți

**2. Limbaj declarativ (YAML):**
- Fișiere de configurare ușor de citit
- Infrastructura este descrisă ca stare dorită
- Operațiuni idempotente, sigure la rulări repetate
- Ușor de înțeles fără experiență de programare

**3. Model push:**
- Nodul de control trimite configurațiile către nodurile gestionate
- Execută sarcinile imediat, fără să aștepte agenții
- Control și vizibilitate centralizate
- Potrivit pentru automatizare la cerere

**4. Bibliotecă extinsă de module:**
- Peste 5.000 de module integrate (în 2026)
- Suportă Linux, Windows, dispozitive de rețea și platforme cloud
- Module create de comunitate și furnizori
- Modulele personalizate se scriu ușor în Python

### Ce poate automatiza Ansible?

Ansible este potrivit pentru automatizarea:

- **Gestionării configurației**: menținerea unor configurații consecvente ale serverelor
- **Implementării aplicațiilor**: implementarea aplicațiilor în medii diferite
- **Provisionării**: crearea și configurarea infrastructurii
- **Livrării continue**: integrarea cu pipeline-uri CI/CD
- **Securității și conformității**: aplicarea politicilor de securitate și conformitate
- **Orchestrării**: coordonarea implementărilor complexe, pe mai multe niveluri
- **Automatizării cloud**: gestionarea AWS, Azure, GCP și a altor servicii cloud
- **Automatizării rețelelor**: configurarea switch-urilor, routerelor și firewall-urilor
- **Automatizării Windows**: gestionarea serverelor și stațiilor de lucru Windows

### Evoluția Ansible: 2012-2026

**Cronologie:**
- **2012**: Michael DeHaan creează Ansible
- **2015**: Red Hat achiziționează Ansible
- **2019**: Ansible Engine 2.8 introduce colecțiile
- **2020**: Ansible 2.10+ se împarte în ansible-core și colecții
- **2023**: Ansible 8.x extinde integrările cloud
- **2026**: Ansible 10.x adaugă generarea de playbook-uri asistată de AI, suport Windows îmbunătățit și funcții de securitate extinse

## Comparație rapidă între Ansible și alternative

| Funcție | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **Tip** | Gestionarea configurației | Provisionarea infrastructurii | Gestionarea configurației | Gestionarea configurației |
| **Limbaj** | YAML | HCL | Puppet DSL (similar cu Ruby) | Ruby DSL |
| **Necesită agent** | Nu | Nu | Da | Da |
| **Curba de învățare** | Ușoară | Moderată | Abruptă | Abruptă |
| **Potrivit pentru** | Gestionarea configurației, implementare | Infrastructură cloud | Companii mari | Fluxuri de lucru complexe |
| **Gestionarea stării** | Model push | Fișier declarativ de stare | Model pull | Model pull |
| **Suport Windows** | Excelent (2026) | Limitat | Bun | Bun |
| **Dimensiunea comunității** | Foarte mare | Foarte mare | Mare | Medie |
| **Utilizare principală** | Operațiuni zilnice | Provisionarea infrastructurii | Configurații enterprise | Implementarea aplicațiilor |

**Când să alegi Ansible:**
- ✅ Gestionarea configurațiilor în medii hibride
- ✅ Automatizarea implementării aplicațiilor
- ✅ Este necesară o curbă de învățare scurtă
- ✅ Este preferată o arhitectură fără agenți
- ✅ Este nevoie de automatizare Windows avansată (îmbunătățiri din 2026)
- ✅ Există deja o infrastructură SSH

**Când să iei în considerare alternative:**
- Terraform: în principal pentru provisionarea infrastructurii (AWS, Azure, GCP)
- Puppet: companii mari cu mii de noduri
- Chef: fluxuri de lucru complexe centrate pe aplicații

## Primii pași: instalarea Ansible în 2026

### Cerințe de sistem

**Nodul de control, unde rulează Ansible:**
- Linux, macOS sau WSL2 pe Windows
- Python 3.9 sau mai nou (Python 3.11+ recomandat pentru 2026)
- Minimum 2 GB RAM, se recomandă 4 GB sau mai mult
- 5 GB spațiu pe disc pentru colecții

**Noduri gestionate:**
- Acces SSH (Linux/Unix) sau WinRM (Windows)
- Python 2.7 sau Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- Nu necesită instalarea unui agent

### Metode de instalare

#### Metoda 1: manager de pachete (recomandat începătorilor)

**Ubuntu/Debian:**
```bash
# Add Ansible PPA for latest version
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux:**
```bash
# Enable EPEL repository
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS:**
```bash
# Using Homebrew
brew install ansible
```

#### Metoda 2: Python pip (funcții mai noi)

```bash
# Install pipx (recommended isolated environment)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install Ansible using pipx
pipx install --include-deps ansible

# Verify installation
ansible --version
```

#### Metoda 3: Docker (portabil)

```bash
# Pull official Ansible container
docker pull quay.io/ansible/ansible:latest

# Run Ansible in container
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### Verificarea instalării

```bash
# Check Ansible version
ansible --version

# Expected output (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### Configurarea inițială

Creează fișierul de configurare Ansible:

```bash
# Create config directory
mkdir -p ~/.ansible

# Create ansible.cfg
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

## Concepte esențiale: componentele Ansible

### 1. Inventar: definirea infrastructurii

Un **inventar** definește gazdele și grupurile gestionate de Ansible. Poate fi static (fișier INI sau YAML) ori dinamic (scripturi sau pluginuri).

#### Inventar static (format INI)

```ini
# inventory/hosts.ini

# Web servers group
[webservers]
web1.example.com
web2.example.com
web3.example.com

# Database servers group
[databases]
db1.example.com ansible_host=192.168.1.100
db2.example.com ansible_host=192.168.1.101

# Load balancers
[loadbalancers]
lb1.example.com

# Group of groups
[production:children]
webservers
databases
loadbalancers

# Variables for all webservers
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# Variables for all hosts
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### Inventar static (format YAML, recomandat în 2026)

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

#### Inventar dinamic (furnizori cloud)

Pentru medii cloud, folosește pluginuri de inventar dinamic:

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

### 2. Playbook-uri: planuri de automatizare

**Playbook-urile** sunt fișiere YAML care descriu fluxuri de automatizare și starea dorită a infrastructurii.

#### Exemplu simplu de playbook

```yaml
# simple_playbook.yml
---
- name: Configure Web Servers
  hosts: webservers
  become: yes
  
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Start and enable Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copy website content
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: Configure firewall
      ufw:
        rule: allow
        port: '{{ item }}'
        proto: tcp
      loop:
        - 80
        - 443
```

#### Rularea playbook-urilor

```bash
# Basic execution
ansible-playbook simple_playbook.yml

# With specific inventory
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# Limit to specific hosts
ansible-playbook simple_playbook.yml --limit web1.example.com

# Dry run (check mode)
ansible-playbook simple_playbook.yml --check

# Verbose output for troubleshooting
ansible-playbook simple_playbook.yml -vvv
```

### 3. Module: unități reutilizabile de sarcini

Modulele Ansible sunt elementele de bază ale automatizării. Fiecare modul execută o sarcină specifică.

#### Module frecvent folosite (2026)

**Module de sistem:**
```yaml
# Package management
- name: Install packages (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# Service management
- name: Manage services
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**Module pentru fișiere:**
```yaml
# File operations
- name: Create directory
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# Copy files
- name: Deploy configuration
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# Template with variables
- name: Deploy nginx config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**Module cloud (exemplu AWS):**
```yaml
# Create EC2 instance
- name: Launch EC2 instance
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

# Create S3 bucket
- name: Create S3 bucket
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**Module pentru baze de date:**
```yaml
# MySQL database management
- name: Create MySQL database
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: Create MySQL user
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. Variabile: playbook-uri flexibile

Variabilele permit reutilizarea playbook-urilor în medii diferite.

#### Prioritatea variabilelor (de la cea mai mare)

1. Variabile suplimentare (`-e` în linia de comandă)
2. Variabile de sarcină
3. Variabile de bloc
4. Variabile de rol și include
5. Variabile de play
6. Fapte despre gazdă
7. `host_vars` ale playbook-ului
8. `group_vars` ale playbook-ului
9. `host_vars` ale inventarului
10. `group_vars` ale inventarului
11. Valori implicite pentru roluri

#### Exemple de variabile

**Variabile de playbook:**
```yaml
---
- name: Deploy Application
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: Deploy {{ app_name }} version {{ app_version }}
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (specifice mediului):**
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

**Ansible Vault (variabile criptate):**
```bash
# Create encrypted file
ansible-vault create secrets.yml

# Edit encrypted file
ansible-vault edit secrets.yml

# secrets.yml content:
# db_password: supersecret123
# api_key: abc123xyz789

# Use in playbook
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. Roluri: organizarea automatizării complexe

**Rolurile** oferă o modalitate structurată de organizare a playbook-urilor, făcându-le modulare și reutilizabile.

#### Structura completă a unui rol

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # Default variables
    ├── vars/
    │   └── main.yml          # Role variables
    ├── tasks/
    │   ├── main.yml          # Main task list
    │   ├── install.yml       # Installation tasks
    │   └── configure.yml     # Configuration tasks
    ├── handlers/
    │   └── main.yml          # Handlers (restart services)
    ├── templates/
    │   ├── nginx.conf.j2     # Jinja2 templates
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # Static files
    ├── meta/
    │   └── main.yml          # Role dependencies
    └── README.md             # Documentation
```

#### Exemplu de rol: nginx

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
- name: Include OS-specific variables
  include_vars: "{{ ansible_os_family }}.yml"

- name: Install Nginx
  include_tasks: install.yml

- name: Configure Nginx
  include_tasks: configure.yml

- name: Ensure Nginx is running
  service:
    name: nginx
    state: started
    enabled: yes
```

**tasks/install.yml:**
```yaml
---
- name: Install Nginx (Debian)
  apt:
    name: nginx
    state: present
    update_cache: yes
  when: ansible_os_family == "Debian"

- name: Install Nginx (RedHat)
  yum:
    name: nginx
    state: present
  when: ansible_os_family == "RedHat"
```

**handlers/main.yml:**
```yaml
---
- name: restart nginx
  service:
    name: nginx
    state: restarted

- name: reload nginx
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

**Utilizarea rolului:**
```yaml
---
- name: Configure Web Servers with Nginx Role
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## Concepte avansate Ansible (2026)

### Colecții Ansible

**Colecțiile** sunt un format de distribuție pentru conținut Ansible, precum module, roluri și pluginuri.

#### Instalarea colecțiilor

```bash
# Install from Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# Install from requirements file
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### Utilizarea modulelor din colecții

```yaml
---
- name: Use collection modules
  hosts: localhost
  tasks:
    - name: Use docker module from community.general
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: Use AWS EC2 module
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (funcții pentru companii)

**Ansible Tower** (comercial) și **AWX** (open source) oferă:

- Interfață web pentru executarea playbook-urilor
- Controlul accesului bazat pe roluri (RBAC)
- Programarea sarcinilor și fluxuri de lucru
- Înregistrare și audit centralizate
- API REST pentru integrare
- Gestionarea acreditărilor
- Sincronizarea inventarelor

**Instalarea AWX cu Docker Compose:**
```bash
# Clone AWX repository
git clone https://github.com/ansible/awx.git
cd awx

# Deploy using docker-compose
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# Access at http://localhost:80
# Default login: admin / password
```

### Automatizarea Windows cu Ansible

În 2026, Ansible oferă un suport Windows mult îmbunătățit:

**Cerințe Windows:**
```powershell
# On Windows host, enable WinRM
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Inventar pentru Windows:**
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

**Playbook de automatizare Windows:**
```yaml
---
- name: Windows Server Configuration
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: Install IIS
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: Deploy website
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: Configure firewall
      win_firewall_rule:
        name: Allow HTTP
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: Install software via Chocolatey
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### Automatizarea rețelelor cu Ansible

Ansible acceptă principalii furnizori de echipamente de rețea, inclusiv Cisco, Juniper, Arista și F5.

**Playbook pentru dispozitive de rețea:**
```yaml
---
- name: Configure Cisco Switches
  hosts: cisco_switches
  gather_facts: no
  connection: network_cli
  
  vars:
    ansible_network_os: ios
    ansible_user: admin
    ansible_password: "{{ vault_switch_password }}"
  
  tasks:
    - name: Configure VLANs
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: DATA
          - vlan_id: 20
            name: VOICE
          - vlan_id: 30
            name: GUEST
        state: merged
    
    - name: Configure interface
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Uplink to Core
            enabled: true
    
    - name: Save configuration
      cisco.ios.ios_config:
        save_when: always
```

## Exemple și scenarii reale de utilizare

### Scenariu 1: implementarea completă a unei aplicații web

**Structura proiectului:**
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

**site.yml (implementarea întregii stive):**
```yaml
---
- name: Configure all servers
  hosts: all
  become: yes
  roles:
    - common

- name: Configure database servers
  hosts: databases
  become: yes
  roles:
    - postgresql

- name: Configure web servers
  hosts: webservers
  become: yes
  roles:
    - nginx
    - application

- name: Configure load balancers
  hosts: loadbalancers
  become: yes
  roles:
    - haproxy
```

### Scenariu 2: configurarea unui cluster Kubernetes

```yaml
---
- name: Setup Kubernetes Cluster
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: Install Docker
      apt:
        name: docker.io
        state: present
    
    - name: Add Kubernetes apt key
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: Add Kubernetes repository
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: Install Kubernetes components
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: Initialize Kubernetes master
  hosts: k8s_master
  become: yes
  tasks:
    - name: Initialize cluster
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: Create .kube directory
      file:
        path: /home/{{ ansible_user }}/.kube
        state: directory
        owner: "{{ ansible_user }}"
    
    - name: Copy admin.conf
      copy:
        src: /etc/kubernetes/admin.conf
        dest: /home/{{ ansible_user }}/.kube/config
        remote_src: yes
        owner: "{{ ansible_user }}"
```

### Scenariu 3: automatizarea consolidării securității

```yaml
---
- name: Security Hardening
  hosts: all
  become: yes
  
  tasks:
    - name: Update all packages
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: Install security tools
      apt:
        name:
          - fail2ban
          - ufw
          - aide
        state: present
    
    - name: Configure fail2ban
      copy:
        src: jail.local
        dest: /etc/fail2ban/jail.local
      notify: restart fail2ban
    
    - name: Configure firewall
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: Enable firewall
      ufw:
        state: enabled
    
    - name: Disable root login
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: Set password policy
      lineinfile:
        path: /etc/login.defs
        regexp: '^PASS_MAX_DAYS'
        line: 'PASS_MAX_DAYS   90'
  
  handlers:
    - name: restart fail2ban
      service:
        name: fail2ban
        state: restarted
    
    - name: restart sshd
      service:
        name: sshd
        state: restarted
```

## Bune practici Ansible (ediția 2026)

### 1. Folosește controlul versiunilor (Git)

**Structura depozitului:**
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

### 2. Aplică idempotenta

**Greșit (nu este idempotent):**
```yaml
- name: Add line to file
  shell: echo "new line" >> /etc/myconfig
```

**Corect (idempotent):**
```yaml
- name: Ensure line in file
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. Folosește Ansible Lint pentru calitatea codului

```bash
# Install ansible-lint
pip install ansible-lint

# Run linter
ansible-lint playbook.yml

# Fix common issues automatically
ansible-lint --fix playbook.yml
```

### 4. Implementează testarea cu Molecule

```bash
# Install Molecule
pip install molecule molecule-docker

# Initialize new role with tests
molecule init role my_role --driver-name docker

# Run tests
cd my_role
molecule test

# Test stages:
# - Create test environment
# - Converge (run playbook)
# - Verify (run tests)
# - Destroy environment
```

**Exemplu molecule.yml:**
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

### 5. Folosește etichete pentru execuție selectivă

```yaml
---
- name: Full Server Setup
  hosts: webservers
  become: yes
  
  tasks:
    - name: Install packages
      apt:
        name: nginx
        state: present
      tags:
        - packages
        - nginx
    
    - name: Configure Nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags:
        - configuration
        - nginx
    
    - name: Deploy application
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# Run only nginx tasks
# ansible-playbook play.yml --tags nginx

# Skip deployment
# ansible-playbook play.yml --skip-tags deployment
```

### 6. Gestionarea erorilor și depanare

```yaml
---
- name: Robust Task Execution
  hosts: webservers
  
  tasks:
    - name: Attempt risky operation
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: Debug output
      debug:
        var: result
        verbosity: 2
    
    - name: Handle failure
      debug:
        msg: "Command failed but continuing..."
      when: result.rc != 0
    
    - name: Block with rescue
      block:
        - name: Try this first
          command: /may/fail
        
        - name: If successful, do this
          debug:
            msg: "Success!"
      
      rescue:
        - name: If failed, do this instead
          debug:
            msg: "Recovered from failure"
      
      always:
        - name: Always run this
          debug:
            msg: "Cleanup operations"
```

### 7. Optimizarea performanței

#### Activarea pipelining
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Folosește Mitogen (performanță de 3-7 ori mai bună)
```bash
# Install Mitogen
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

#### Execuție paralelă
```yaml
---
- name: Parallel Updates
  hosts: all
  strategy: free  # Don't wait for all hosts
  serial: 10      # Process 10 hosts at a time
  
  tasks:
    - name: Update packages
      apt:
        upgrade: dist
```

## Depanarea problemelor comune

### Problema 1: erori de conexiune SSH

**Problema:** nu te poți conecta la gazdele gestionate

**Soluții:**
```bash
# Test raw SSH connection
ssh -vvv user@host

# Test Ansible connection
ansible host -m ping -vvv

# Add to inventory
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### Problema 2: acces refuzat (sudo)

**Problema:** sarcinile eșuează din cauza erorilor de permisiune

**Soluție:**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: Task requiring root
      file:
        path: /etc/myconfig
        state: touch
```

### Problema 3: modul negăsit

**Problema:** erori care indică lipsa modulului

**Soluție:**
```bash
# Ensure collection is installed
ansible-galaxy collection install community.general

# Verify collection
ansible-galaxy collection list

# Use FQCN (Fully Qualified Collection Name)
community.general.docker_container:
  name: mycontainer
```

### Problema 4: executarea lentă a playbook-ului

**Soluții:**
1. Activează pipelining (vezi secțiunea Performanță)
2. Folosește pluginul de strategie Mitogen
3. Dezactivează colectarea faptelor dacă nu este necesară:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. Folosește execuția asincronă pentru sarcini de durată:
   ```yaml
   - name: Long running task
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Parcurs profesional și certificări Ansible

### Evoluția competențelor

**Începător (0-6 luni):**
- Scrie playbook-uri de bază
- Înțelege inventarul și variabilele
- Folosește module comune
- Execută playbook-uri

**Intermediar (6-18 luni):**
- Creează roluri reutilizabile
- Implementează gestionarea erorilor
- Folosește Ansible Vault
- Integrează cu CI/CD
- Gestionează mai multe medii

**Avansat (peste 18 luni):**
- Proiectează framework-uri complexe de automatizare
- Creează module și pluginuri personalizate
- Proiectează implementări Tower/AWX
- Optimizează performanța
- Îi îndrumă pe alții

### Certificări

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Demonstrează competența în Ansible
- Examen practic, bazat pe performanță
- Valabilă 3 ani
- Recunoscută în industrie

**Resurse de pregătire:**
- Red Hat Learning Subscription
- Documentația Ansible
- Laboratoare practice (A Cloud Guru, Udemy)
- Forumuri ale comunității

### Piața muncii (2026)

**Salarii medii în SUA:**
- Inginer Ansible junior: $75,000-$95,000
- Inginer DevOps de nivel mediu (Ansible): $110,000-$140,000
- Arhitect senior de automatizare: $150,000-$190,000

**Competențe căutate:**
- Ansible și Kubernetes
- Ansible și Terraform (IaC hibrid)
- Ansible și CI/CD (Jenkins, GitLab)
- Ansible și cloud (AWS, Azure, GCP)
- Administrarea Ansible Tower/AWX

## Resurse de învățare și comunitate

### Documentație oficială
- [Documentația Ansible](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - platformă de partajare a rolurilor
- [Ansible pe GitHub](https://github.com/ansible/ansible)

### Cursuri online
- Red Hat Learning Subscription
- Udemy: `Ansible pentru începători absoluți`
- A Cloud Guru: `Ansible practic`
- Linux Academy: `Pornire rapidă cu Ansible`

### Cărți
- `Ansible for DevOps` de Jeff Geerling (actualizată în 2025)
- `Ansible: Up and Running` de Lorin Hochstein
- `Mastering Ansible` de James Freeman

### Comunitate
- [Lista de distribuție Ansible](https://groups.google.com/forum/#!forum/ansible-project)
- [Ansible pe Reddit](https://reddit.com/r/ansible)
- [Serverul Ansible pe Discord](https://discord.gg/ansible)
- Întâlniri Ansible locale și online

### Platforme de practică
- [Scenarii Ansible pe Katacoda](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Laborator local cu Vagrant sau Docker

## Concluzie: începe parcursul tău cu Ansible

Ansible a devenit instrumentul de automatizare ales de organizații din întreaga lume. În 2026 oferă mai multe funcționalități, gestionare Windows mai simplă, integrări cloud îmbunătățite și generarea de playbook-uri asistată de AI. Competențele dobândite îți vor fi utile de-a lungul carierei IT, indiferent dacă gestionezi infrastructură tradițională, medii cloud sau implementări hibride.

**Idei principale:**

1. **Începe simplu**: creează playbook-uri de bază pentru câteva servere
2. **Exersează regulat**: configurează un laborator acasă și experimentează
3. **Învață prin practică**: automatizează sarcini reale din activitatea zilnică
4. **Respectă bunele practici**: folosește controlul versiunilor, teste și documentație
5. **Alătură-te comunității**: învață de la alții și împărtășește ce știi
6. **Ține pasul**: Ansible evoluează rapid, continuă să înveți
7. **Combină instrumente**: Ansible, Terraform și Kubernetes oferă împreună automatizare extinsă

**Pașii următori:**

1. Instalează Ansible pe sistemul tău
2. Creează un inventar simplu cu servere de test, mașini virtuale sau containere
3. Scrie primul playbook, de exemplu pentru instalarea unui pachet
4. Adaugă treptat șabloane, variabile și roluri
5. Contribuie cu roluri comunitare pe Ansible Galaxy
6. Ia în considerare o certificare pentru a-ți valida competențele

Parcursul de la începător la expert Ansible este satisfăcător și deschide oportunități în DevOps, SRE și ingineria cloud. Cu noțiunile de bază din acest ghid, poți începe să automatizezi infrastructura și să dezvolți competențe valoroase pentru domeniul IT modern.

Bine ai venit în lumea automatizării infrastructurii cu Ansible!

______

## Referințe

- [Documentația oficială Ansible](https://docs.ansible.com/)
- [Ansible Galaxy - depozit de roluri](https://galaxy.ansible.com/)
- [Depozitul Ansible pe GitHub](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - Ansible Tower open source](https://github.com/ansible/awx)
- [Bune practici Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Framework-ul de testare Molecule](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Ansible for DevOps de Jeff Geerling](https://www.ansiblefordevops.com/)
- [Indexul colecțiilor Ansible](https://docs.ansible.com/ansible/latest/collections/index.html)
