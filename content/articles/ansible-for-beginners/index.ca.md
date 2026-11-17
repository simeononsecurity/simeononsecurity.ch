---
title: "Ansible per a principiants 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-13
description: "Guia d’Ansible per a 2026 sobre instal·lació, playbooks, rols, exemples, bones pràctiques i comparacions amb Terraform, Puppet i Chef."
tags: ["Introducció a Ansible", "Automatització de la gestió d’infraestructura de TI", "Conceptes bàsics d’Ansible", "Automatització d’infraestructura de TI", "Gestió de la configuració", "Desplegament d’aplicacions", "Aprovisionament", "Lliurament continu", "Seguretat i compliment", "Orquestració", "YAML", "Mòduls d’Ansible", "Rols", "Bones pràctiques", "Control de versions", "Proves", "Red Hat", "Administradors de sistemes", "Linux", "macOS", "Windows", "Instal·lació d’Ansible", "Inventari d’Ansible", "Playbooks d’Ansible", "Mòduls d’Ansible", "Rols d’Ansible", "Bones pràctiques d’Ansible", "Proves d’Ansible", "Eina d’automatització d’infraestructura de TI", "Tutorial d’Ansible", "Automatització de la gestió d’infraestructura", "Ansible per a principiants", "Aprendre Ansible", "Tutorial d’Ansible 2026", "Ansible i Terraform", "Ansible i Puppet", "Exemples de playbooks d’Ansible", "Automatització amb Ansible", "Eines DevOps", "Infraestructura com a codi", "Ansible AWX", "Ansible Tower", "Col·leccions d’Ansible", "Ansible Galaxy", "Ansible Vault", "Automatització del núvol amb Ansible"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "Il·lustració d’una infraestructura de TI moderna amb servidors i dispositius interconnectats. Mostra connexions SSH i WinRM, un fitxer YAML estilitzat i icones de serveis al núvol sobre un fons fosc."
coverCaption: ""
---

**Ansible per a principiants: guia completa d’automatització de TI per a 2026**

Ansible s’ha convertit en una plataforma d’automatització líder del sector. Segons la font, més del 80% de les empreses de Fortune 500 l’utilitzen per gestionar infraestructures de TI complexes. El 2026 continua sent una solució important, fàcil d’utilitzar i amb funcions per a empreses.

Aquesta guia completa t’acompanya des dels conceptes bàsics fins a un ús segur d’Ansible. Cobreix conceptes fonamentals, tècniques avançades, exemples pràctics i bones pràctiques per a 2026.

## Què és Ansible? Conceptes bàsics

**Ansible** és una plataforma d’automatització de codi obert que simplifica la gestió de la infraestructura de TI mitjançant automatització declarativa sense agents. A diferència de les eines tradicionals de gestió de configuració, no exigeix agents als nodes gestionats. Utilitza SSH per a Linux i Unix, o WinRM per a Windows, per gestionar sistemes remotament.

{{< youtube id="goclfp6a2IQ" >}}

### Característiques principals d’Ansible

**1. Arquitectura sense agents:**
- No cal instal·lar programari als nodes gestionats
- Utilitza els protocols SSH o WinRM existents
- Redueix la superfície d’atac i la càrrega de manteniment
- És més fàcil començar-hi que amb les eines basades en agents

**2. Llenguatge declaratiu (YAML):**
- Fitxers de configuració fàcils de llegir
- Infraestructura descrita com a estat desitjat
- Operacions idempotents, segures quan s’executen diverses vegades
- Fàcil d’entendre sense experiència en programació

**3. Model push:**
- El node de control envia configuracions als nodes gestionats
- Executa tasques immediatament, sense esperar agents
- Control i visibilitat centralitzats
- Adequat per a l’automatització sota demanda

**4. Biblioteca extensa de mòduls:**
- Més de 5.000 mòduls integrats (el 2026)
- Compatible amb Linux, Windows, dispositius de xarxa i plataformes al núvol
- Mòduls de la comunitat i dels proveïdors
- És fàcil escriure mòduls personalitzats en Python

### Què pot automatitzar Ansible?

Ansible és adequat per automatitzar:

- **Gestió de la configuració**: mantenir coherents les configuracions dels servidors
- **Desplegament d’aplicacions**: desplegar aplicacions en entorns diferents
- **Aprovisionament**: crear i configurar infraestructura
- **Lliurament continu**: integrar-se amb les pipelines de CI/CD
- **Seguretat i compliment**: aplicar polítiques de seguretat i compliment
- **Orquestració**: coordinar desplegaments complexos de diverses capes
- **Automatització del núvol**: gestionar AWS, Azure, GCP i altres serveis al núvol
- **Automatització de xarxes**: configurar commutadors, encaminadors i tallafocs
- **Automatització de Windows**: gestionar servidors i estacions de treball Windows

### Evolució d’Ansible: de 2012 a 2026

**Cronologia:**
- **2012**: Michael DeHaan crea Ansible
- **2015**: Red Hat adquireix Ansible
- **2019**: Ansible Engine 2.8 introdueix les col·leccions
- **2020**: Ansible 2.10+ es divideix en ansible-core i col·leccions
- **2023**: Ansible 8.x amplia les integracions amb el núvol
- **2026**: Ansible 10.x incorpora la generació de playbooks assistida per IA, un millor suport per a Windows i funcions de seguretat ampliades

## Comparació ràpida d’Ansible amb les alternatives

| Funció | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **Tipus** | Gestió de la configuració | Aprovisionament d’infraestructura | Gestió de la configuració | Gestió de la configuració |
| **Llenguatge** | YAML | HCL | Puppet DSL (semblant a Ruby) | Ruby DSL |
| **Requereix agent** | No | No | Sí | Sí |
| **Corba d’aprenentatge** | Fàcil | Moderada | Pronunciada | Pronunciada |
| **Ideal per a** | Gestió de la configuració, desplegament | Infraestructura al núvol | Grans empreses | Fluxos de treball complexos |
| **Gestió de l’estat** | Model push | Fitxer d’estat declaratiu | Model pull | Model pull |
| **Suport de Windows** | Excel·lent (2026) | Limitat | Bo | Bo |
| **Mida de la comunitat** | Molt gran | Molt gran | Gran | Mitjana |
| **Ús principal** | Operacions diàries | Aprovisionament d’infraestructura | Configuració empresarial | Desplegament d’aplicacions |

**Quan escollir Ansible:**
- ✅ Gestionar la configuració en entorns híbrids
- ✅ Automatitzar el desplegament d’aplicacions
- ✅ Cal una corba d’aprenentatge curta
- ✅ Es prefereix una arquitectura sense agents
- ✅ Es necessita una automatització sòlida de Windows (millores del 2026)
- ✅ Ja hi ha una infraestructura SSH

**Quan considerar alternatives:**
- Terraform: sobretot per aprovisionar infraestructura (AWS, Azure, GCP)
- Puppet: grans empreses amb milers de nodes
- Chef: fluxos de treball complexos centrats en aplicacions

## Primers passos: instal·lar Ansible el 2026

### Requisits del sistema

**Node de control, on s’executa Ansible:**
- Linux, macOS o WSL2 a Windows
- Python 3.9 o posterior (es recomana Python 3.11+ el 2026)
- 2 GB de RAM com a mínim, 4 GB o més recomanats
- 5 GB d’espai al disc per a les col·leccions

**Nodes gestionats:**
- Accés SSH (Linux/Unix) o WinRM (Windows)
- Python 2.7 o Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- No cal instal·lar cap agent

### Mètodes d’instal·lació

#### Mètode 1: gestor de paquets (recomanat per a principiants)

**Ubuntu/Debian:**
```bash
# Afegir el PPA d’Ansible per a la versió més recent
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux:**
```bash
# Habilitar el repositori EPEL
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS:**
```bash
# Utilitzar Homebrew
brew install ansible
```

#### Mètode 2: Python pip (funcions més recents)

```bash
# Instal·lar pipx (entorn aïllat recomanat)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Instal·lar Ansible amb pipx
pipx install --include-deps ansible

# Verificar la instal·lació
ansible --version
```

#### Mètode 3: Docker (portable)

```bash
# Descarregar el contenidor oficial d’Ansible
docker pull quay.io/ansible/ansible:latest

# Executar Ansible en un contenidor
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### Verificar la instal·lació

```bash
# Comprovar la versió d’Ansible
ansible --version

# Sortida esperada (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### Configuració inicial

Crea el fitxer de configuració d’Ansible:

```bash
# Crear el directori de configuració
mkdir -p ~/.ansible

# Crear ansible.cfg
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

## Conceptes essencials: components d’Ansible

### 1. Inventari: definir la infraestructura

Un **inventari** defineix els hosts i grups que gestiona Ansible. Pot ser estàtic (fitxer INI o YAML) o dinàmic (scripts o connectors).

#### Inventari estàtic (format INI)

```ini
# inventory/hosts.ini

# Grup de servidors web
[webservers]
web1.example.com
web2.example.com
web3.example.com

# Grup de servidors de bases de dades
[databases]
db1.example.com ansible_host=192.168.1.100
db2.example.com ansible_host=192.168.1.101

# Equilibradors de càrrega
[loadbalancers]
lb1.example.com

# Grup de grups
[production:children]
webservers
databases
loadbalancers

# Variables per a tots els servidors web
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# Variables per a tots els amfitrions
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### Inventari estàtic (format YAML, recomanat el 2026)

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

#### Inventari dinàmic (proveïdors de núvol)

En entorns al núvol, utilitza connectors d’inventari dinàmic:

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

### 2. Playbooks: plans d’automatització

Els **playbooks** són fitxers YAML que descriuen fluxos de treball d’automatització. Defineixen l’estat desitjat de la infraestructura.

#### Exemple senzill de playbook

```yaml
# simple_playbook.yml
---
- name: Configurar els servidors web
  hosts: webservers
  become: yes
  
  tasks:
    - name: Instal·lar Nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Iniciar i habilitar Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copiar el contingut del lloc web
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: Configurar el tallafoc
      ufw:
        rule: allow
        port: '{{ item }}'
        proto: tcp
      loop:
        - 80
        - 443
```

#### Executar playbooks

```bash
# Execució bàsica
ansible-playbook simple_playbook.yml

# Amb un inventari específic
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# Limitar a amfitrions específics
ansible-playbook simple_playbook.yml --limit web1.example.com

# Execució de prova (mode de comprovació)
ansible-playbook simple_playbook.yml --check

# Sortida detallada per resoldre problemes
ansible-playbook simple_playbook.yml -vvv
```

### 3. Mòduls: unitats de tasca reutilitzables

Els mòduls d’Ansible són els components bàsics de l’automatització. Cada mòdul executa una tasca específica.

#### Mòduls habituals (2026)

**Mòduls del sistema:**
```yaml
# Gestió de paquets
- name: Instal·lar paquets (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# Gestió de serveis
- name: Gestionar els serveis
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**Mòduls de fitxers:**
```yaml
# Operacions amb fitxers
- name: Crear un directori
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# Copiar fitxers
- name: Desplegar la configuració
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# Plantilla amb variables
- name: Desplegar la configuració de nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**Mòduls del núvol (exemple d’AWS):**
```yaml
# Crear una instància EC2
- name: Iniciar una instància EC2
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

# Crear un bucket S3
- name: Crear un bucket S3
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**Mòduls de bases de dades:**
```yaml
# Gestió de bases de dades MySQL
- name: Crear una base de dades MySQL
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: Crear un usuari MySQL
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. Variables: flexibilitzar els playbooks

Les variables permeten reutilitzar playbooks en entorns diferents.

#### Prioritat de les variables (de més alta a més baixa)

1. Variables addicionals (`-e` a la línia d’ordres)
2. Variables de tasca
3. Variables de bloc
4. Variables de rol i include
5. Variables del play
6. Fets de l’host
7. `host_vars` del playbook
8. `group_vars` del playbook
9. `host_vars` de l’inventari
10. `group_vars` de l’inventari
11. Valors per defecte dels rols

#### Exemples de variables

**Variables del playbook:**
```yaml
---
- name: Desplegar l’aplicació
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: Desplegar {{ app_name }} versió {{ app_version }}
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (específiques de l’entorn):**
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

**Ansible Vault (variables xifrades):**
```bash
# Crear un fitxer xifrat
ansible-vault create secrets.yml

# Editar un fitxer xifrat
ansible-vault edit secrets.yml

# Contingut de secrets.yml:
# db_password: supersecret123
# api_key: abc123xyz789

# Utilitzar al playbook
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. Rols: organitzar automatitzacions complexes

Els **rols** ofereixen una manera estructurada d’organitzar playbooks i fer-los modulars i reutilitzables.

#### Estructura completa d’un rol

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # Variables predeterminades
    ├── vars/
    │   └── main.yml          # Variables del rol
    ├── tasks/
    │   ├── main.yml          # Llista principal de tasques
    │   ├── install.yml       # Tasques d’instal·lació
    │   └── configure.yml     # Tasques de configuració
    ├── handlers/
    │   └── main.yml          # Controladors (reinici dels serveis)
    ├── templates/
    │   ├── nginx.conf.j2     # Plantilles Jinja2
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # Fitxers estàtics
    ├── meta/
    │   └── main.yml          # Dependències del rol
    └── README.md             # Documentació
```

#### Exemple de rol: nginx

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
- name: Incloure les variables específiques del sistema operatiu
  include_vars: "{{ ansible_os_family }}.yml"

- name: Instal·lar Nginx
  include_tasks: install.yml

- name: Configurar Nginx
  include_tasks: configure.yml

- name: Assegurar que Nginx estigui en execució
  service:
    name: nginx
    state: started
    enabled: yes
```

**tasks/install.yml:**
```yaml
---
- name: Instal·lar Nginx (Debian)
  apt:
    name: nginx
    state: present
    update_cache: yes
  when: ansible_os_family == "Debian"

- name: Instal·lar Nginx (RedHat)
  yum:
    name: nginx
    state: present
  when: ansible_os_family == "RedHat"
```

**handlers/main.yml:**
```yaml
---
- name: Reiniciar nginx
  service:
    name: nginx
    state: restarted

- name: Recarregar nginx
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

**Utilitzar el rol:**
```yaml
---
- name: Configurar servidors web amb el rol de Nginx
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## Conceptes avançats d’Ansible (2026)

### Col·leccions d’Ansible

Les **col·leccions** són un format de distribució de contingut d’Ansible, com ara mòduls, rols i connectors.

#### Instal·lar col·leccions

```bash
# Instal·lar des d’Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# Instal·lar des del fitxer de requisits
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### Utilitzar mòduls de col·leccions

```yaml
---
- name: Utilitzar mòduls de col·lecció
  hosts: localhost
  tasks:
    - name: Utilitzar el mòdul Docker de community.general
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: Utilitzar el mòdul AWS EC2
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (funcions empresarials)

**Ansible Tower** (comercial) i **AWX** (codi obert) ofereixen:

- Interfície web per executar playbooks
- Control d’accés basat en rols (RBAC)
- Planificació de tasques i fluxos de treball
- Registre i auditoria centralitzats
- API REST per a la integració
- Gestió de credencials
- Sincronització d’inventaris

**Instal·lació d’AWX amb Docker Compose:**
```bash
# Clonar el repositori AWX
git clone https://github.com/ansible/awx.git
cd awx

# Desplegar amb docker-compose
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# Accedir a http://localhost:80
# Inici de sessió predeterminat: admin / password
```

### Automatització de Windows amb Ansible

El 2026, Ansible ofereix un suport per a Windows molt millorat:

**Requisits previs de Windows:**
```powershell
# Al servidor Windows, habilitar WinRM
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Inventari per a Windows:**
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

**Playbook d’automatització de Windows:**
```yaml
---
- name: Configuració del servidor Windows
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: Instal·lar IIS
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: Desplegar el lloc web
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: Configurar el tallafoc
      win_firewall_rule:
        name: Permetre HTTP
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: Instal·lar programari amb Chocolatey
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### Automatització de xarxes amb Ansible

Ansible és compatible amb els principals proveïdors de xarxes, com Cisco, Juniper, Arista i F5.

**Playbook per a dispositius de xarxa:**
```yaml
---
- name: Configurar commutadors Cisco
  hosts: cisco_switches
  gather_facts: no
  connection: network_cli
  
  vars:
    ansible_network_os: ios
    ansible_user: admin
    ansible_password: "{{ vault_switch_password }}"
  
  tasks:
    - name: Configurar VLAN
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: DATA
          - vlan_id: 20
            name: VOICE
          - vlan_id: 30
            name: GUEST
        state: merged
    
    - name: Configurar la interfície
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Uplink to Core
            enabled: true
    
    - name: Desar la configuració
      cisco.ios.ios_config:
        save_when: always
```

## Casos d’ús i exemples reals

### Cas d’ús 1: desplegament complet d’una aplicació web

**Estructura del projecte:**
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

**site.yml (desplegament de tota la pila):**
```yaml
---
- name: Configurar tots els servidors
  hosts: all
  become: yes
  roles:
    - common

- name: Configurar els servidors de bases de dades
  hosts: databases
  become: yes
  roles:
    - postgresql

- name: Configurar els servidors web
  hosts: webservers
  become: yes
  roles:
    - nginx
    - application

- name: Configurar els equilibradors de càrrega
  hosts: loadbalancers
  become: yes
  roles:
    - haproxy
```

### Cas d’ús 2: configuració d’un clúster de Kubernetes

```yaml
---
- name: Configurar el clúster Kubernetes
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: Instal·lar Docker
      apt:
        name: docker.io
        state: present
    
    - name: Afegir la clau apt de Kubernetes
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: Afegir el repositori de Kubernetes
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: Instal·lar components de Kubernetes
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: Inicialitzar el node principal de Kubernetes
  hosts: k8s_master
  become: yes
  tasks:
    - name: Inicialitzar el clúster
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: Crear el directori .kube
      file:
        path: /home/{{ ansible_user }}/.kube
        state: directory
        owner: "{{ ansible_user }}"
    
    - name: Copiar admin.conf
      copy:
        src: /etc/kubernetes/admin.conf
        dest: /home/{{ ansible_user }}/.kube/config
        remote_src: yes
        owner: "{{ ansible_user }}"
```

### Cas d’ús 3: automatització del reforç de la seguretat

```yaml
---
- name: Reforçar la seguretat
  hosts: all
  become: yes
  
  tasks:
    - name: Actualitzar tots els paquets
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: Instal·lar eines de seguretat
      apt:
        name:
          - fail2ban
          - ufw
          - aide
        state: present
    
    - name: Configurar fail2ban
      copy:
        src: jail.local
        dest: /etc/fail2ban/jail.local
      notify: restart fail2ban
    
    - name: Configurar el tallafoc
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: Habilitar el tallafoc
      ufw:
        state: enabled
    
    - name: Desactivar l’inici de sessió de root
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: Establir la política de contrasenyes
      lineinfile:
        path: /etc/login.defs
        regexp: '^PASS_MAX_DAYS'
        line: 'PASS_MAX_DAYS   90'
  
  handlers:
    - name: Reiniciar fail2ban
      service:
        name: fail2ban
        state: restarted
    
    - name: Reiniciar sshd
      service:
        name: sshd
        state: restarted
```

## Bones pràctiques d’Ansible (edició 2026)

### 1. Utilitza el control de versions (Git)

**Estructura del repositori:**
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

### 2. Aplica la idempotència

**Incorrecte (no idempotent):**
```yaml
- name: Afegir una línia al fitxer
  shell: echo "new line" >> /etc/myconfig
```

**Correcte (idempotent):**
```yaml
- name: Assegurar que la línia sigui al fitxer
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. Utilitza Ansible Lint per a la qualitat del codi

```bash
# Instal·lar ansible-lint
pip install ansible-lint

# Executar el linter
ansible-lint playbook.yml

# Corregir automàticament els problemes habituals
ansible-lint --fix playbook.yml
```

### 4. Implementa proves amb Molecule

```bash
# Instal·lar Molecule
pip install molecule molecule-docker

# Inicialitzar un rol nou amb proves
molecule init role my_role --driver-name docker

# Executar les proves
cd my_role
molecule test

# Fases de prova:
# - Crear l’entorn de prova
# - Convergir (executar el playbook)
# - Verificar (executar les proves)
# - Destruir l’entorn
```

**Exemple de molecule.yml:**
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

### 5. Utilitza etiquetes per executar de manera selectiva

```yaml
---
- name: Configuració completa del servidor
  hosts: webservers
  become: yes
  
  tasks:
    - name: Instal·lar paquets
      apt:
        name: nginx
        state: present
      tags:
        - packages
        - nginx
    
    - name: Configurar Nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags:
        - configuration
        - nginx
    
    - name: Desplegar l’aplicació
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# Executar només les tasques de nginx
# ansible-playbook play.yml --tags nginx

# Ometre el desplegament
# ansible-playbook play.yml --skip-tags deployment
```

### 6. Gestió d’errors i depuració

```yaml
---
- name: Execució robusta de tasques
  hosts: webservers
  
  tasks:
    - name: Provar una operació arriscada
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: Sortida de depuració
      debug:
        var: result
        verbosity: 2
    
    - name: Gestionar l’error
      debug:
        msg: "L'ordre ha fallat, però l'execució continua..."
      when: result.rc != 0
    
    - name: Bloc amb recuperació
      block:
        - name: Provar això primer
          command: /may/fail
        
        - name: Si funciona, fer això
          debug:
            msg: "Èxit!"
      
      rescue:
        - name: Si falla, fer això en lloc seu
          debug:
            msg: "Recuperació després de l’error"
      
      always:
        - name: Executar-ho sempre
          debug:
            msg: "Operacions de neteja"
```

### 7. Optimitzar el rendiment

#### Activa el pipelining
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Utilitza Mitogen (rendiment de 3 a 7 vegades superior)
```bash
# Instal·lar Mitogen
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

#### Execució paral·lela
```yaml
---
- name: Actualitzacions en paral·lel
  hosts: all
  strategy: free  # No esperar tots els amfitrions
  serial: 10      # Processar 10 amfitrions cada vegada
  
  tasks:
    - name: Actualitzar paquets
      apt:
        upgrade: dist
```

## Resolució de problemes habituals

### Problema 1: errors de connexió SSH

**Problema:** no es pot connectar als hosts gestionats

**Solucions:**
```bash
# Provar la connexió SSH directa
ssh -vvv user@host

# Provar la connexió d’Ansible
ansible host -m ping -vvv

# Afegir a l’inventari
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### Problema 2: accés denegat (sudo)

**Problema:** les tasques fallen per errors de permisos

**Solució:**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: Tasca que requereix privilegis de root
      file:
        path: /etc/myconfig
        state: touch
```

### Problema 3: no s’ha trobat el mòdul

**Problema:** errors que indiquen que no s’ha trobat un mòdul

**Solució:**
```bash
# Assegurar que la col·lecció estigui instal·lada
ansible-galaxy collection install community.general

# Verificar la col·lecció
ansible-galaxy collection list

# Utilitzar FQCN (nom completament qualificat de la col·lecció)
community.general.docker_container:
  name: mycontainer
```

### Problema 4: execució lenta del playbook

**Solucions:**
1. Activa el pipelining (consulta la secció Rendiment)
2. Utilitza el connector d’estratègia Mitogen
3. Desactiva la recopilació de fets si no cal:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. Utilitza l’execució asíncrona per a tasques llargues:
   ```yaml
   - name: Tasca de llarga durada
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Trajectòria professional i certificacions d’Ansible

### Progressió d’habilitats

**Principiant (0-6 mesos):**
- Escriu playbooks bàsics
- Entén els inventaris i les variables
- Utilitza mòduls habituals
- Executa playbooks

**Intermedi (6-18 mesos):**
- Crea rols reutilitzables
- Implementa la gestió d’errors
- Utilitza Ansible Vault
- Integra Ansible amb CI/CD
- Gestiona diversos entorns

**Avançat (més de 18 mesos):**
- Dissenya marcs d’automatització complexos
- Crea mòduls i connectors personalitzats
- Dissenya desplegaments de Tower/AWX
- Optimitza el rendiment
- Fa de mentor d’altres persones

### Certificacions

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Demostra el domini d’Ansible
- Examen pràctic basat en tasques
- Vàlid durant 3 anys
- Reconegut al sector

**Recursos de preparació:**
- Red Hat Learning Subscription
- Documentació d’Ansible
- Laboratoris pràctics (A Cloud Guru, Udemy)
- Fòrums de la comunitat

### Mercat laboral (2026)

**Salaris mitjans als Estats Units:**
- Enginyer júnior d’Ansible: $75,000-$95,000
- Enginyer DevOps de nivell mitjà (Ansible): $110,000-$140,000
- Arquitecte sènior d’automatització: $150,000-$190,000

**Habilitats sol·licitades:**
- Ansible i Kubernetes
- Ansible i Terraform (IaC híbrida)
- Ansible i CI/CD (Jenkins, GitLab)
- Ansible i el núvol (AWS, Azure, GCP)
- Administració d’Ansible Tower/AWX

## Recursos d’aprenentatge i comunitat

### Documentació oficial
- [Documentació d’Ansible](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - plataforma per compartir rols
- [Ansible a GitHub](https://github.com/ansible/ansible)

### Cursos en línia
- Red Hat Learning Subscription
- Udemy: `Ansible per a principiants absoluts`
- A Cloud Guru: `Ansible pràctic`
- Linux Academy: `Inici ràpid d’Ansible`

### Llibres
- `Ansible for DevOps`, de Jeff Geerling (actualitzat el 2025)
- `Ansible: Up and Running`, de Lorin Hochstein
- `Mastering Ansible`, de James Freeman

### Comunitat
- [Llista de correu d’Ansible](https://groups.google.com/forum/#!forum/ansible-project)
- [Ansible a Reddit](https://reddit.com/r/ansible)
- [Servidor d’Ansible a Discord](https://discord.gg/ansible)
- Trobades locals i virtuals d’Ansible

### Plataformes per practicar
- [Escenaris d’Ansible de Katacoda](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Laboratori local amb Vagrant o Docker

## Conclusió: comença el teu recorregut amb Ansible

Ansible s’ha convertit en l’eina d’automatització preferida de moltes organitzacions arreu del món. El 2026 ofereix més funcions, una gestió de Windows més senzilla, millors integracions amb el núvol i generació de playbooks assistida per IA. Les habilitats que adquireixis et serviran durant tota la carrera de TI, tant si gestiones infraestructura tradicional com entorns al núvol o desplegaments híbrids.

**Punts principals:**

1. **Comença amb senzillesa**: crea playbooks bàsics per gestionar uns quants servidors
2. **Practica amb regularitat**: prepara un laboratori a casa i experimenta
3. **Aprèn fent**: automatitza tasques reals de la feina diària
4. **Segueix les bones pràctiques**: utilitza control de versions, proves i documentació
5. **Uneix-te a la comunitat**: aprèn dels altres i comparteix coneixements
6. **Mantén-te al dia**: Ansible evoluciona ràpidament, continua aprenent
7. **Combina eines**: Ansible, Terraform i Kubernetes permeten automatitzar un conjunt ampli de tasques

**Passos següents:**

1. Instal·la Ansible al teu sistema
2. Crea un inventari senzill de servidors de prova, màquines virtuals o contenidors
3. Escriu el teu primer playbook, per exemple per instal·lar un paquet
4. Afegeix progressivament plantilles, variables i rols
5. Contribueix als rols de la comunitat a Ansible Galaxy
6. Valora obtenir una certificació per validar les teves habilitats

El camí de principiant a expert en Ansible és gratificant i obre oportunitats en DevOps, SRE i enginyeria del núvol. Amb els conceptes d’aquesta guia, pots començar a automatitzar la infraestructura i desenvolupar habilitats valuoses per al sector de TI actual.

Et donem la benvinguda al món de l’automatització de la infraestructura amb Ansible!

______

## Referències

- [Documentació oficial d’Ansible](https://docs.ansible.com/)
- [Ansible Galaxy - repositori de rols](https://galaxy.ansible.com/)
- [Repositori d’Ansible a GitHub](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - Ansible Tower de codi obert](https://github.com/ansible/awx)
- [Bones pràctiques d’Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Framework de proves Molecule](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Ansible for DevOps de Jeff Geerling](https://www.ansiblefordevops.com/)
- [Índex de col·leccions d’Ansible](https://docs.ansible.com/ansible/latest/collections/index.html)
