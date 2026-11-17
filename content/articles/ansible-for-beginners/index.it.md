---
title: "Ansible per principianti 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-13
description: "Guida ad Ansible per il 2026: installazione, playbook, ruoli, esempi, buone pratiche e confronti con Terraform, Puppet e Chef."
tags: ["Introduzione ad Ansible", "Automazione della gestione dell'infrastruttura IT", "Nozioni di base su Ansible", "Automazione dell'infrastruttura IT", "Gestione della configurazione", "Distribuzione delle applicazioni", "Approvvigionamento", "Consegna continua", "Sicurezza e conformità", "Orchestrazione", "YAML", "Moduli Ansible", "Ruoli", "Buone pratiche", "Controllo delle versioni", "Test", "Red Hat", "Amministratori di sistema", "Linux", "macOS", "Windows", "Installazione di Ansible", "Inventario Ansible", "Playbook Ansible", "Moduli Ansible", "Ruoli Ansible", "Buone pratiche Ansible", "Test di Ansible", "Strumento di automazione dell'infrastruttura IT", "Tutorial su Ansible", "Automazione della gestione dell'infrastruttura", "Ansible per principianti", "Imparare Ansible", "Tutorial Ansible 2026", "Ansible e Terraform", "Ansible e Puppet", "Esempi di playbook Ansible", "Automazione Ansible", "Strumenti DevOps", "Infrastruttura come codice", "Ansible AWX", "Ansible Tower", "Raccolte Ansible", "Ansible Galaxy", "Ansible Vault", "Automazione cloud con Ansible"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "Illustrazione di una moderna infrastruttura IT con server e dispositivi interconnessi. Mostra connessioni SSH e WinRM, un file YAML stilizzato e icone di servizi cloud su sfondo scuro."
coverCaption: ""
---

**Ansible per principianti: guida completa all'automazione IT nel 2026**

Ansible è diventata una piattaforma di automazione leader nel settore. Secondo la fonte, oltre l'80% delle aziende Fortune 500 si affida ad Ansible per gestire infrastrutture IT complesse. Nel 2026 rimane una soluzione importante, semplice da usare e dotata di funzionalità adatte alle grandi aziende.

Questa guida completa ti porta dalle basi a un uso sicuro di Ansible. Tratta i concetti fondamentali, le tecniche avanzate, esempi pratici e buone pratiche per il 2026.

## Che cos'è Ansible? Le basi

**Ansible** è una piattaforma open source di automazione che semplifica la gestione dell'infrastruttura IT con un modello dichiarativo senza agenti. A differenza dei tradizionali strumenti di gestione della configurazione, non richiede agenti sui nodi gestiti. Usa SSH per Linux e Unix oppure WinRM per Windows per la gestione remota.

{{< youtube id="goclfp6a2IQ" >}}

### Caratteristiche principali di Ansible

**1. Architettura senza agenti:**
- Non richiede l'installazione di software sui nodi gestiti
- Usa i protocolli SSH o WinRM già disponibili
- Riduce la superficie di attacco e il carico di manutenzione
- È più semplice da avviare rispetto agli strumenti basati su agenti

**2. Linguaggio dichiarativo (YAML):**
- File di configurazione leggibili
- Infrastruttura descritta come stato desiderato
- Operazioni idempotenti, sicure da eseguire più volte
- Comprensibile anche senza esperienza di programmazione

**3. Modello push:**
- Il nodo di controllo invia le configurazioni ai nodi gestiti
- Esegue subito le attività, senza attendere gli agenti
- Offre controllo e visibilità centralizzati
- È adatto all'automazione su richiesta

**4. Ampia libreria di moduli:**
- Oltre 5.000 moduli integrati (dato del 2026)
- Supporta Linux, Windows, dispositivi di rete e piattaforme cloud
- Moduli sviluppati dalla community e dai fornitori
- È facile scrivere moduli personalizzati in Python

### Che cosa può automatizzare Ansible?

Ansible è adatto ad automatizzare:

- **Gestione della configurazione**: mantenere coerenti le configurazioni dei server
- **Distribuzione delle applicazioni**: distribuire applicazioni in ambienti diversi
- **Preparazione dell’infrastruttura**: creare e configurare l'infrastruttura
- **Consegna continua**: integrarsi con le pipeline CI/CD
- **Sicurezza e conformità**: applicare criteri di sicurezza e conformità
- **Orchestrazione**: coordinare distribuzioni complesse a più livelli
- **Automazione cloud**: gestire AWS, Azure, GCP e altri cloud
- **Automazione di rete**: configurare switch, router e firewall
- **Automazione Windows**: gestire server e workstation Windows

### Evoluzione di Ansible: dal 2012 al 2026

**Cronologia:**
- **2012**: Michael DeHaan crea Ansible
- **2015**: Red Hat acquisisce Ansible
- **2019**: Ansible Engine 2.8 introduce le raccolte
- **2020**: Ansible 2.10+ si divide in ansible-core e raccolte
- **2023**: Ansible 8.x amplia le integrazioni cloud
- **2026**: Ansible 10.x introduce la generazione di playbook assistita dall'IA, un migliore supporto Windows e funzionalità di sicurezza più ampie

## Ansible a confronto con i concorrenti

| Funzione | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **Tipo** | Gestione della configurazione | Preparazione dell'infrastruttura | Gestione della configurazione | Gestione della configurazione |
| **Linguaggio** | YAML | HCL | Puppet DSL (simile a Ruby) | Ruby DSL |
| **Richiede un agente** | No | No | Sì | Sì |
| **Curva di apprendimento** | Facile | Moderata | Ripida | Ripida |
| **Ideale per** | Gestione della configurazione, distribuzione | Infrastruttura cloud | Grandi aziende | Flussi di lavoro complessi |
| **Gestione dello stato** | Modello push | File di stato dichiarativo | Modello pull | Modello pull |
| **Supporto Windows** | Eccellente (2026) | Limitato | Buono | Buono |
| **Dimensione della community** | Molto grande | Molto grande | Grande | Media |
| **Caso d'uso principale** | Gestione operativa quotidiana | Preparazione dell'infrastruttura | Configurazione aziendale | Distribuzione delle applicazioni |

**Quando scegliere Ansible:**
- ✅ Gestione della configurazione in ambienti ibridi
- ✅ Automazione della distribuzione di applicazioni
- ✅ È necessaria una curva di apprendimento breve
- ✅ Si preferisce un'architettura senza agenti
- ✅ Serve una solida automazione Windows (miglioramenti del 2026)
- ✅ È già disponibile un'infrastruttura SSH

**Quando valutare le alternative:**
- Terraform: soprattutto per il provisioning dell'infrastruttura (AWS, Azure, GCP)
- Puppet: grandi aziende con migliaia di nodi
- Chef: flussi di lavoro complessi incentrati sulle applicazioni

## Primi passi: installare Ansible nel 2026

### Requisiti di sistema

**Nodo di controllo, dove viene eseguito Ansible:**
- Linux, macOS o WSL2 su Windows
- Python 3.9 o versioni successive (consigliato Python 3.11+ per il 2026)
- Almeno 2 GB di RAM, 4 GB o più consigliati
- 5 GB di spazio su disco per le raccolte

**Nodi gestiti:**
- Accesso SSH (Linux/Unix) oppure WinRM (Windows)
- Python 2.7 o Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- Non richiedono l'installazione di agenti

### Metodi di installazione

#### Metodo 1: gestore di pacchetti (consigliato ai principianti)

**Ubuntu/Debian:**
```bash
# Aggiungere il PPA Ansible per la versione più recente
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux:**
```bash
# Abilitare il repository EPEL
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS:**
```bash
# Usare Homebrew
brew install ansible
```

#### Metodo 2: Python pip (funzionalità più recenti)

```bash
# Installare pipx (ambiente isolato consigliato)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Installare Ansible con pipx
pipx install --include-deps ansible

# Verificare l’installazione
ansible --version
```

#### Metodo 3: Docker (portatile)

```bash
# Recuperare il container ufficiale Ansible
docker pull quay.io/ansible/ansible:latest

# Eseguire Ansible in un container
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### Verificare l'installazione

```bash
# Controllare la versione di Ansible
ansible --version

# Output previsto (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### Configurazione iniziale

Crea il file di configurazione di Ansible:

```bash
# Creare la directory di configurazione
mkdir -p ~/.ansible

# Creare ansible.cfg
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

## Concetti essenziali: gli elementi di Ansible

### 1. Inventario: definire l'infrastruttura

Un **inventario** definisce gli host e i gruppi gestiti da Ansible. Può essere statico (file INI o YAML) oppure dinamico (script o plugin).

#### Inventario statico (formato INI)

```ini
# inventory/hosts.ini

# Gruppo di server web
[webservers]
web1.example.com
web2.example.com
web3.example.com

# Gruppo di server database
[databases]
db1.example.com ansible_host=192.168.1.100
db2.example.com ansible_host=192.168.1.101

# Bilanciatori di carico
[loadbalancers]
lb1.example.com

# Gruppo di gruppi
[production:children]
webservers
databases
loadbalancers

# Variabili per tutti i server web
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# Variabili per tutti gli host
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### Inventario statico (formato YAML, consigliato nel 2026)

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

#### Inventario dinamico (provider cloud)

Per gli ambienti cloud, usa i plugin di inventario dinamico:

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

### 2. Playbook: schemi per l'automazione

I **playbook** sono file YAML che descrivono i flussi di lavoro di automazione. Definiscono lo stato desiderato dell'infrastruttura.

#### Esempio semplice di playbook

```yaml
# simple_playbook.yml
---
- name: Configurare i server web
  hosts: webservers
  become: yes
  
  tasks:
    - name: Installare Nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Avviare e abilitare Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copiare i contenuti del sito web
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: Configurare il firewall
      ufw:
        rule: allow
        port: '{{ item }}'
        proto: tcp
      loop:
        - 80
        - 443
```

#### Eseguire i playbook

```bash
# Esecuzione di base
ansible-playbook simple_playbook.yml

# Con inventario specifico
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# Limitare a host specifici
ansible-playbook simple_playbook.yml --limit web1.example.com

# Esecuzione di prova (modalità di controllo)
ansible-playbook simple_playbook.yml --check

# Output dettagliato per la risoluzione dei problemi
ansible-playbook simple_playbook.yml -vvv
```

### 3. Moduli: unità di attività riutilizzabili

I moduli Ansible sono gli elementi di base dell'automazione. Ogni modulo svolge un'attività specifica.

#### Moduli più usati (2026)

**Moduli di sistema:**
```yaml
# Gestione dei pacchetti
- name: Installare i pacchetti (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# Gestione dei servizi
- name: Gestire i servizi
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**Moduli per i file:**
```yaml
# Operazioni sui file
- name: Creare una directory
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# Copiare file
- name: Distribuire la configurazione
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# Modello con variabili
- name: Distribuire la configurazione nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**Moduli cloud (esempio AWS):**
```yaml
# Creare un’istanza EC2
- name: Avviare un’istanza EC2
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

# Creare un bucket S3
- name: Creare un bucket S3
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**Moduli di database:**
```yaml
# Gestione database MySQL
- name: Creare un database MySQL
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: Creare un utente MySQL
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. Variabili: rendere flessibili i playbook

Le variabili permettono di riutilizzare i playbook in ambienti diversi.

#### Priorità delle variabili (dalla più alta)

1. Variabili aggiuntive (`-e` nella riga di comando)
2. Variabili di attività
3. Variabili di blocco
4. Variabili di ruolo e include
5. Variabili del play
6. Fatti dell'host
7. `host_vars` del playbook
8. `group_vars` del playbook
9. `host_vars` dell'inventario
10. `group_vars` dell'inventario
11. Valori predefiniti dei ruoli

#### Esempi di variabili

**Variabili del playbook:**
```yaml
---
- name: Distribuire l’applicazione
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: Distribuire {{ app_name }} versione {{ app_version }}
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (specifiche per ambiente):**
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

**Ansible Vault (variabili crittografate):**
```bash
# Creare un file crittografato
ansible-vault create secrets.yml

# Modificare un file crittografato
ansible-vault edit secrets.yml

# Contenuto di secrets.yml:
# db_password: supersecret123
# api_key: abc123xyz789

# Usare nel playbook
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. Ruoli: organizzare l'automazione complessa

I **ruoli** offrono un modo strutturato per organizzare i playbook, rendendoli modulari e riutilizzabili.

#### Struttura completa di un ruolo

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # Variabili predefinite
    ├── vars/
    │   └── main.yml          # Variabili del ruolo
    ├── tasks/
    │   ├── main.yml          # Elenco principale delle attività
    │   ├── install.yml       # Attività di installazione
    │   └── configure.yml     # Attività di configurazione
    ├── handlers/
    │   └── main.yml          # Handler (riavvio dei servizi)
    ├── templates/
    │   ├── nginx.conf.j2     # Modelli Jinja2
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # File statici
    ├── meta/
    │   └── main.yml          # Dipendenze del ruolo
    └── README.md             # Documentazione
```

#### Ruolo di esempio: nginx

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
- name: Includere le variabili specifiche del sistema operativo
  include_vars: "{{ ansible_os_family }}.yml"

- name: Installare Nginx
  include_tasks: install.yml

- name: Configurare Nginx
  include_tasks: configure.yml

- name: Assicurarsi che Nginx sia in esecuzione
  service:
    name: nginx
    state: started
    enabled: yes
```

**tasks/install.yml:**
```yaml
---
- name: Installare Nginx (Debian)
  apt:
    name: nginx
    state: present
    update_cache: yes
  when: ansible_os_family == "Debian"

- name: Installare Nginx (RedHat)
  yum:
    name: nginx
    state: present
  when: ansible_os_family == "RedHat"
```

**handlers/main.yml:**
```yaml
---
- name: Riavviare nginx
  service:
    name: nginx
    state: restarted

- name: Ricaricare nginx
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

**Usare il ruolo:**
```yaml
---
- name: Configurare i server web con il ruolo Nginx
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## Concetti avanzati di Ansible (2026)

### Raccolte Ansible

Le **raccolte** sono un formato di distribuzione dei contenuti Ansible, come moduli, ruoli e plugin.

#### Installare le raccolte

```bash
# Installare da Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# Installare dal file dei requisiti
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### Usare i moduli delle raccolte

```yaml
---
- name: Usare i moduli delle collection
  hosts: localhost
  tasks:
    - name: Usare il modulo Docker di community.general
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: Usare il modulo AWS EC2
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (funzionalità aziendali)

**Ansible Tower** (commerciale) e **AWX** (open source) offrono:

- Interfaccia web per eseguire playbook
- Controllo degli accessi basato sui ruoli (RBAC)
- Pianificazione delle attività e flussi di lavoro
- Registrazione e audit centralizzati
- API REST per l'integrazione
- Gestione delle credenziali
- Sincronizzazione dell'inventario

**Installazione di AWX (Docker Compose):**
```bash
# Clonare il repository AWX
git clone https://github.com/ansible/awx.git
cd awx

# Distribuire con docker-compose
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# Accedere a http://localhost:80
# Accesso predefinito: admin / password
```

### Automazione Windows con Ansible

Nel 2026 Ansible offre un supporto Windows notevolmente migliorato:

**Prerequisiti Windows:**
```powershell
# Abilitare WinRM sull’host Windows
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Inventario per Windows:**
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

**Playbook di automazione Windows:**
```yaml
---
- name: Configurazione del server Windows
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: Installare IIS
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: Distribuire il sito web
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: Configurare il firewall
      win_firewall_rule:
        name: Consentire HTTP
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: Installare software tramite Chocolatey
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### Automazione di rete con Ansible

Ansible supporta i principali fornitori di apparati di rete, tra cui Cisco, Juniper, Arista e F5.

**Playbook per dispositivi di rete:**
```yaml
---
- name: Configurare gli switch Cisco
  hosts: cisco_switches
  gather_facts: no
  connection: network_cli
  
  vars:
    ansible_network_os: ios
    ansible_user: admin
    ansible_password: "{{ vault_switch_password }}"
  
  tasks:
    - name: Configurare le VLAN
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: DATA
          - vlan_id: 20
            name: VOICE
          - vlan_id: 30
            name: GUEST
        state: merged
    
    - name: Configurare l’interfaccia
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Uplink to Core
            enabled: true
    
    - name: Salvare la configurazione
      cisco.ios.ios_config:
        save_when: always
```

## Casi d'uso ed esempi pratici

### Caso d'uso 1: distribuzione completa di un'applicazione web

**Struttura del progetto:**
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

**site.yml (distribuzione dello stack completo):**
```yaml
---
- name: Configurare tutti i server
  hosts: all
  become: yes
  roles:
    - common

- name: Configurare i server di database
  hosts: databases
  become: yes
  roles:
    - postgresql

- name: Configurare i server web
  hosts: webservers
  become: yes
  roles:
    - nginx
    - application

- name: Configurare i bilanciatori di carico
  hosts: loadbalancers
  become: yes
  roles:
    - haproxy
```

### Caso d'uso 2: configurazione di un cluster Kubernetes

```yaml
---
- name: Configurare il cluster Kubernetes
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: Installare Docker
      apt:
        name: docker.io
        state: present
    
    - name: Aggiungere la chiave apt di Kubernetes
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: Aggiungere il repository Kubernetes
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: Installare i componenti Kubernetes
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: Inizializzare il master Kubernetes
  hosts: k8s_master
  become: yes
  tasks:
    - name: Inizializzare il cluster
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: Creare la directory .kube
      file:
        path: /home/{{ ansible_user }}/.kube
        state: directory
        owner: "{{ ansible_user }}"
    
    - name: Copiare admin.conf
      copy:
        src: /etc/kubernetes/admin.conf
        dest: /home/{{ ansible_user }}/.kube/config
        remote_src: yes
        owner: "{{ ansible_user }}"
```

### Caso d'uso 3: automazione del rafforzamento della sicurezza

```yaml
---
- name: Rafforzare la sicurezza
  hosts: all
  become: yes
  
  tasks:
    - name: Aggiornare tutti i pacchetti
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: Installare strumenti di sicurezza
      apt:
        name:
          - fail2ban
          - ufw
          - aide
        state: present
    
    - name: Configurare fail2ban
      copy:
        src: jail.local
        dest: /etc/fail2ban/jail.local
      notify: restart fail2ban
    
    - name: Configurare il firewall
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: Abilitare il firewall
      ufw:
        state: enabled
    
    - name: Disabilitare l’accesso root
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: Impostare la policy delle password
      lineinfile:
        path: /etc/login.defs
        regexp: '^PASS_MAX_DAYS'
        line: 'PASS_MAX_DAYS   90'
  
  handlers:
    - name: Riavviare fail2ban
      service:
        name: fail2ban
        state: restarted
    
    - name: Riavviare sshd
      service:
        name: sshd
        state: restarted
```

## Buone pratiche per Ansible (edizione 2026)

### 1. Usa il controllo delle versioni (Git)

**Struttura del repository:**
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

### 2. Implementa l'idempotenza

**Sbagliato (non idempotente):**
```yaml
- name: Aggiungere una riga al file
  shell: echo "new line" >> /etc/myconfig
```

**Corretto (idempotente):**
```yaml
- name: Verificare che la riga sia nel file
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. Usa Ansible Lint per la qualità del codice

```bash
# Installare ansible-lint
pip install ansible-lint

# Eseguire il linter
ansible-lint playbook.yml

# Correggere automaticamente i problemi comuni
ansible-lint --fix playbook.yml
```

### 4. Implementa i test con Molecule

```bash
# Installare Molecule
pip install molecule molecule-docker

# Inizializzare un nuovo ruolo con test
molecule init role my_role --driver-name docker

# Eseguire i test
cd my_role
molecule test

# Fasi di test:
# - Creare ambiente di test
# - Convergere (eseguire il playbook)
# - Verificare (eseguire i test)
# - Eliminare l’ambiente
```

**Esempio di molecule.yml:**
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

### 5. Usa i tag per un'esecuzione selettiva

```yaml
---
- name: Configurazione completa del server
  hosts: webservers
  become: yes
  
  tasks:
    - name: Installare i pacchetti
      apt:
        name: nginx
        state: present
      tags:
        - packages
        - nginx
    
    - name: Configurare Nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags:
        - configuration
        - nginx
    
    - name: Distribuire l’applicazione
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# Eseguire solo le attività nginx
# ansible-playbook play.yml --tags nginx

# Saltare la distribuzione
# ansible-playbook play.yml --skip-tags deployment
```

### 6. Gestione degli errori e debug

```yaml
---
- name: Esecuzione robusta delle attività
  hosts: webservers
  
  tasks:
    - name: Tentare un’operazione rischiosa
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: Output di debug
      debug:
        var: result
        verbosity: 2
    
    - name: Gestire l’errore
      debug:
        msg: "Il comando non è riuscito, ma l’esecuzione continua..."
      when: result.rc != 0
    
    - name: Blocco con recupero
      block:
        - name: Provare prima questo
          command: /may/fail
        
        - name: In caso di successo, eseguire questo
          debug:
            msg: "Completato!"
      
      rescue:
        - name: In caso di errore, eseguire questo invece
          debug:
            msg: "Ripristino dopo l’errore"
      
      always:
        - name: Eseguire sempre questo
          debug:
            msg: "Operazioni di pulizia"
```

### 7. Ottimizzazione delle prestazioni

#### Abilita il pipelining
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Usa Mitogen (prestazioni da 3 a 7 volte superiori)
```bash
# Installare Mitogen
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

#### Esecuzione parallela
```yaml
---
- name: Aggiornamenti paralleli
  hosts: all
  strategy: free  # Non attendere tutti gli host
  serial: 10      # Elaborare 10 host alla volta
  
  tasks:
    - name: Aggiornare i pacchetti
      apt:
        upgrade: dist
```

## Risolvere i problemi più comuni

### Problema 1: errori di connessione SSH

**Problema:** impossibile connettersi agli host gestiti

**Soluzioni:**
```bash
# Testare la connessione SSH diretta
ssh -vvv user@host

# Testare la connessione Ansible
ansible host -m ping -vvv

# Aggiungere all’inventario
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### Problema 2: accesso negato (sudo)

**Problema:** le attività falliscono per errori di autorizzazione

**Soluzione:**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: Attività che richiede privilegi root
      file:
        path: /etc/myconfig
        state: touch
```

### Problema 3: modulo non trovato

**Problema:** errori "modulo non trovato"

**Soluzione:**
```bash
# Verificare che la collection sia installata
ansible-galaxy collection install community.general

# Verificare la collection
ansible-galaxy collection list

# Usare FQCN (nome completo qualificato della collection)
community.general.docker_container:
  name: mycontainer
```

### Problema 4: playbook lento

**Soluzioni:**
1. Abilita il pipelining (vedi la sezione Prestazioni)
2. Usa il plugin di strategia Mitogen
3. Disabilita la raccolta dei fatti se non serve:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. Usa l'esecuzione asincrona per le attività lunghe:
   ```yaml
   - name: Attività di lunga durata
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Percorso professionale e certificazioni Ansible

### Progressione delle competenze

**Principiante (0-6 mesi):**
- Scrivi playbook di base
- Comprendi inventario e variabili
- Usa i moduli più comuni
- Esegui playbook

**Intermedio (6-18 mesi):**
- Crea ruoli riutilizzabili
- Implementa la gestione degli errori
- Usa Ansible Vault
- Integra Ansible con CI/CD
- Gestisci più ambienti

**Avanzato (oltre 18 mesi):**
- Progetta framework di automazione complessi
- Crea moduli e plugin personalizzati
- Progetta distribuzioni Tower/AWX
- Ottimizza le prestazioni
- Fai da mentore ad altre persone

### Certificazioni

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Dimostra la competenza in Ansible
- Esame pratico basato sulle prestazioni
- Valido per 3 anni
- Riconosciuto nel settore

**Risorse per la preparazione:**
- Red Hat Learning Subscription
- Documentazione Ansible
- Laboratori pratici (A Cloud Guru, Udemy)
- Forum della community

### Mercato del lavoro (2026)

**Stipendi medi negli Stati Uniti:**
- Ingegnere Ansible junior: $75.000-$95.000
- Ingegnere DevOps di livello intermedio (Ansible): $110.000-$140.000
- Architetto senior dell'automazione: $150.000-$190.000

**Competenze richieste:**
- Ansible e Kubernetes
- Ansible e Terraform (IaC ibrida)
- Ansible e CI/CD (Jenkins, GitLab)
- Ansible e cloud (AWS, Azure, GCP)
- Amministrazione di Ansible Tower/AWX

## Risorse di apprendimento e community

### Documentazione ufficiale
- [Documentazione Ansible](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - piattaforma per condividere ruoli
- [Ansible su GitHub](https://github.com/ansible/ansible)

### Corsi online
- Red Hat Learning Subscription
- Udemy: "Ansible per principianti assoluti"
- A Cloud Guru: "Ansible pratico"
- Linux Academy: "Avvio rapido ad Ansible"

### Libri
- "Ansible for DevOps" di Jeff Geerling (aggiornato nel 2025)
- "Ansible: Up and Running" di Lorin Hochstein
- "Mastering Ansible" di James Freeman

### Community
- [Mailing list di Ansible](https://groups.google.com/forum/#!forum/ansible-project)
- [Ansible su Reddit](https://reddit.com/r/ansible)
- [Server Discord di Ansible](https://discord.gg/ansible)
- Incontri Ansible, locali e online

### Piattaforme per esercitarsi
- [Scenari Ansible di Katacoda](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Un laboratorio locale con Vagrant o Docker

## Conclusione: inizia il tuo percorso con Ansible

Ansible è diventata la scelta di molte organizzazioni per l'automazione. Nel 2026 offre più funzionalità, una gestione Windows più semplice, migliori integrazioni cloud e generazione di playbook assistita dall'IA. Le competenze acquisite ti saranno utili durante la carriera IT, sia che tu gestisca infrastrutture tradizionali, ambienti cloud o distribuzioni ibride.

**Punti principali:**

1. **Inizia dalle basi**: crea playbook semplici per gestire alcuni server
2. **Esercitati con regolarità**: configura un laboratorio domestico e fai prove
3. **Impara facendo**: automatizza attività reali del tuo lavoro quotidiano
4. **Segui le buone pratiche**: controllo delle versioni, test e documentazione
5. **Partecipa alla community**: impara dagli altri e condividi ciò che sai
6. **Resta aggiornato**: Ansible si evolve rapidamente, continua a imparare
7. **Combina gli strumenti**: Ansible, Terraform e Kubernetes offrono un'automazione completa

**Prossimi passi:**

1. Installa Ansible sul tuo sistema
2. Crea un inventario semplice di server di prova, macchine virtuali o container
3. Scrivi il tuo primo playbook, per esempio per installare un pacchetto
4. Aggiungi gradualmente complessità con modelli, variabili e ruoli
5. Contribuisci ai ruoli della community su Ansible Galaxy
6. Valuta una certificazione per attestare le tue competenze

Il percorso da principiante a esperto di Ansible è gratificante e apre opportunità nei ruoli DevOps, SRE e di ingegneria cloud. Con le basi presentate in questa guida, sei pronto a iniziare ad automatizzare l'infrastruttura e a sviluppare competenze preziose per il settore IT moderno.

Benvenuto nel mondo dell'automazione dell'infrastruttura con Ansible!

______

## Riferimenti

- [Documentazione ufficiale di Ansible](https://docs.ansible.com/)
- [Ansible Galaxy - repository dei ruoli](https://galaxy.ansible.com/)
- [Repository di Ansible su GitHub](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - Ansible Tower open source](https://github.com/ansible/awx)
- [Buone pratiche per Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Framework di test Molecule](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Ansible for DevOps di Jeff Geerling](https://www.ansiblefordevops.com/)
- [Indice delle raccolte Ansible](https://docs.ansible.com/ansible/latest/collections/index.html)
