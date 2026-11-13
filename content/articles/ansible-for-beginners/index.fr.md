---
title: "Ansible pour débutants 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-13
description: "Guide Ansible 2026 sur l’installation, les playbooks, les rôles, les exemples, les bonnes pratiques et les comparaisons avec Terraform, Puppet et Chef."
tags: ["Introduction à Ansible", "Automatisation de la gestion de l’infrastructure informatique", "Notions de base sur Ansible", "Automatisation de l’infrastructure informatique", "Gestion de configuration", "Déploiement d’applications", "Provisionnement", "Livraison continue", "Sécurité et conformité", "Orchestration", "YAML", "Modules Ansible", "Rôles", "Bonnes pratiques", "Gestion de versions", "Tests", "Red Hat", "Administrateurs système", "Linux", "macOS", "Windows", "Installation d’Ansible", "Inventaire Ansible", "Playbooks Ansible", "Modules Ansible", "Rôles Ansible", "Bonnes pratiques Ansible", "Tests Ansible", "Outil d’automatisation de l’infrastructure informatique", "Tutoriel Ansible", "Automatisation de la gestion de l’infrastructure", "Ansible pour débutants", "Apprendre Ansible", "Tutoriel Ansible 2026", "Ansible et Terraform", "Ansible et Puppet", "Exemples de playbooks Ansible", "Automatisation avec Ansible", "Outils DevOps", "Infrastructure sous forme de code", "Ansible AWX", "Ansible Tower", "Collections Ansible", "Ansible Galaxy", "Ansible Vault", "Automatisation du cloud avec Ansible"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "Illustration d’une infrastructure informatique moderne avec des serveurs et des appareils interconnectés. Elle montre des connexions SSH et WinRM, un fichier YAML stylisé et des icônes de services cloud sur fond sombre."
coverCaption: ""
---

**Ansible pour débutants : guide complet de l’automatisation informatique en 2026**

Ansible est devenu une plateforme d’automatisation de premier plan. Selon la source, plus de 80 % des entreprises du Fortune 500 l’utilisent pour gérer des infrastructures informatiques complexes. En 2026, Ansible reste une solution importante, simple à prendre en main et dotée de fonctions adaptées aux grandes entreprises.

Ce guide complet vous accompagne des bases à une utilisation assurée d’Ansible. Il couvre les concepts fondamentaux, les techniques avancées, des exemples concrets et les bonnes pratiques pour 2026.

## Qu’est-ce qu’Ansible ? Comprendre les bases

**Ansible** est une plateforme d’automatisation open source qui simplifie la gestion de l’infrastructure informatique grâce à une automatisation déclarative sans agent. Contrairement aux outils traditionnels de gestion de configuration, Ansible ne nécessite aucun agent sur les nœuds gérés. Il utilise SSH pour Linux et Unix, ou WinRM pour Windows, afin d’assurer la gestion à distance.

{{< youtube id="goclfp6a2IQ" >}}

### Principales caractéristiques d’Ansible

**1. Architecture sans agent :**
- Aucun logiciel à installer sur les nœuds gérés
- Utilise les protocoles SSH ou WinRM existants
- Réduit la surface d’attaque et la charge de maintenance
- Plus simple à prendre en main que les outils avec agents

**2. Langage déclaratif (YAML) :**
- Fichiers de configuration lisibles
- Infrastructure décrite selon l’état souhaité
- Opérations idempotentes, sans risque lors d’exécutions répétées
- Compréhensible sans expérience en programmation

**3. Modèle push :**
- Le nœud de contrôle envoie les configurations aux nœuds gérés
- Exécute les tâches immédiatement, sans attendre les agents
- Contrôle et visibilité centralisés
- Adapté à l’automatisation à la demande

**4. Vaste bibliothèque de modules :**
- Plus de 5 000 modules intégrés (en 2026)
- Prend en charge Linux, Windows, les équipements réseau et les plateformes cloud
- Modules fournis par la communauté et les éditeurs
- Création facile de modules personnalisés en Python

### Que peut automatiser Ansible ?

Ansible convient à l’automatisation des domaines suivants :

- **Gestion de configuration** : maintenir des configurations de serveur cohérentes
- **Déploiement d’applications** : déployer des applications dans plusieurs environnements
- **Provisionnement** : créer et configurer l’infrastructure
- **Livraison continue** : intégrer les pipelines CI/CD
- **Sécurité et conformité** : appliquer les politiques de sécurité et de conformité
- **Orchestration** : coordonner des déploiements complexes à plusieurs niveaux
- **Automatisation cloud** : gérer AWS, Azure, GCP et d’autres clouds
- **Automatisation réseau** : configurer les commutateurs, routeurs et pare-feu
- **Automatisation Windows** : gérer les serveurs et postes de travail Windows

### Évolution d’Ansible : de 2012 à 2026

**Chronologie :**
- **2012** : Michael DeHaan crée Ansible
- **2015** : Red Hat acquiert Ansible
- **2019** : Ansible Engine 2.8 introduit les collections
- **2020** : Ansible 2.10+ est divisé entre ansible-core et les collections
- **2023** : Ansible 8.x étend les intégrations cloud
- **2026** : Ansible 10.x ajoute la génération de playbooks assistée par IA, une meilleure prise en charge de Windows et des fonctions de sécurité avancées

## Comparaison rapide d’Ansible avec ses concurrents

| Fonction | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **Type** | Gestion de configuration | Provisionnement de l’infrastructure | Gestion de configuration | Gestion de configuration |
| **Langage** | YAML | HCL | Puppet DSL (proche de Ruby) | Ruby DSL |
| **Agent requis** | Non | Non | Oui | Oui |
| **Courbe d’apprentissage** | Facile | Modérée | Raide | Raide |
| **Adapté à** | Gestion de configuration, déploiement | Infrastructure cloud | Grandes entreprises | Flux de travail complexes |
| **Gestion de l’état** | Modèle push | Fichier d’état déclaratif | Modèle pull | Modèle pull |
| **Prise en charge de Windows** | Excellente (2026) | Limitée | Bonne | Bonne |
| **Taille de la communauté** | Très grande | Très grande | Grande | Moyenne |
| **Usage principal** | Exploitation quotidienne | Provisionnement de l’infrastructure | Configuration en entreprise | Déploiement d’applications |

**Quand choisir Ansible :**
- ✅ Gérer la configuration dans des environnements hybrides
- ✅ Automatiser le déploiement d’applications
- ✅ Apprendre rapidement
- ✅ Préférer une architecture sans agent
- ✅ Automatiser fortement Windows (améliorations de 2026)
- ✅ Disposer déjà d’une infrastructure SSH

**Quand envisager une alternative :**
- Terraform : surtout pour le provisionnement de l’infrastructure (AWS, Azure, GCP)
- Puppet : grandes entreprises comptant des milliers de nœuds
- Chef : flux de travail complexes centrés sur les applications

## Premiers pas : installer Ansible en 2026

### Configuration requise

**Nœud de contrôle, où Ansible s’exécute :**
- Linux, macOS ou WSL2 sur Windows
- Python 3.9 ou ultérieur (Python 3.11+ recommandé en 2026)
- 2 Go de RAM au minimum, 4 Go ou plus recommandés
- 5 Go d’espace disque pour les collections

**Nœuds gérés :**
- Accès SSH (Linux/Unix) ou WinRM (Windows)
- Python 2.7 ou Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- Aucune installation d’agent requise

### Méthodes d’installation

#### Méthode 1 : gestionnaire de paquets (recommandé aux débutants)

**Ubuntu/Debian :**
```bash
# Ajouter le PPA Ansible pour la dernière version
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux :**
```bash
# Activer le dépôt EPEL
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS :**
```bash
# Utiliser Homebrew
brew install ansible
```

#### Méthode 2 : Python pip (fonctions récentes)

```bash
# Installer pipx (environnement isolé recommandé)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Installer Ansible avec pipx
pipx install --include-deps ansible

# Vérifier l’installation
ansible --version
```

#### Méthode 3 : Docker (portable)

```bash
# Récupérer le conteneur officiel Ansible
docker pull quay.io/ansible/ansible:latest

# Exécuter Ansible dans un conteneur
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### Vérifier l’installation

```bash
# Vérifier la version d’Ansible
ansible --version

# Sortie attendue (2026) :
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### Configuration initiale

Créez le fichier de configuration Ansible :

```bash
# Créer le répertoire de configuration
mkdir -p ~/.ansible

# Créer ansible.cfg
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

## Concepts essentiels : les composants d’Ansible

### 1. Inventaire : définir l’infrastructure

Un **inventaire** définit les hôtes et les groupes gérés par Ansible. Il peut être statique (fichier INI ou YAML) ou dynamique (scripts ou plugins).

#### Inventaire statique (format INI)

```ini
# inventory/hosts.ini

# Groupe de serveurs Web
[webservers]
web1.example.com
web2.example.com
web3.example.com

# Groupe de serveurs de bases de données
[databases]
db1.example.com ansible_host=192.168.1.100
db2.example.com ansible_host=192.168.1.101

# Répartiteurs de charge
[loadbalancers]
lb1.example.com

# Groupe de groupes
[production:children]
webservers
databases
loadbalancers

# Variables pour tous les serveurs Web
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# Variables pour tous les hôtes
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### Inventaire statique (format YAML, recommandé en 2026)

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

#### Inventaire dynamique (fournisseurs cloud)

Pour les environnements cloud, utilisez des plugins d’inventaire dynamique :

**AWS EC2 :**
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

**Azure :**
```yaml
# inventory/azure_rm.yml
plugin: azure.azcollection.azure_rm
include_vm_resource_groups:
  - production-rg
keyed_groups:
  - key: tags.role
    prefix: role
```

### 2. Playbooks : plans d’automatisation

Les **playbooks** sont des fichiers YAML qui décrivent des flux d’automatisation. Ils définissent l’état souhaité de votre infrastructure.

#### Exemple simple de playbook

```yaml
# simple_playbook.yml
---
- name: Configurer les serveurs Web
  hosts: webservers
  become: yes
  
  tasks:
    - name: Installer Nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Démarrer et activer Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copier le contenu du site Web
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: Configurer le pare-feu
      ufw:
        rule: allow
        port: '{{ item }}'
        proto: tcp
      loop:
        - 80
        - 443
```

#### Exécuter des playbooks

```bash
# Exécution de base
ansible-playbook simple_playbook.yml

# Avec un inventaire spécifique
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# Limiter à des hôtes spécifiques
ansible-playbook simple_playbook.yml --limit web1.example.com

# Simulation (mode vérification)
ansible-playbook simple_playbook.yml --check

# Sortie détaillée pour le dépannage
ansible-playbook simple_playbook.yml -vvv
```

### 3. Modules : unités de tâche réutilisables

Les modules Ansible sont les composants de base de l’automatisation. Chaque module effectue une tâche précise.

#### Modules courants (2026)

**Modules système :**
```yaml
# Gestion des paquets
- name: Installer les paquets (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# Gestion des services
- name: Gérer les services
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**Modules de fichiers :**
```yaml
# Opérations sur les fichiers
- name: Créer un répertoire
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# Copier des fichiers
- name: Déployer la configuration
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# Modèle avec variables
- name: Déployer la configuration nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**Modules cloud (exemple AWS) :**
```yaml
# Créer une instance EC2
- name: Lancer une instance EC2
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

# Créer un compartiment S3
- name: Créer un compartiment S3
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**Modules de base de données :**
```yaml
# Gestion de base de données MySQL
- name: Créer une base de données MySQL
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: Créer un utilisateur MySQL
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. Variables : rendre les playbooks flexibles

Les variables permettent de réutiliser les playbooks dans plusieurs environnements.

#### Priorité des variables (de la plus élevée à la plus faible)

1. Variables supplémentaires (`-e` dans la ligne de commande)
2. Variables de tâche
3. Variables de bloc
4. Variables de rôle et d’inclusion
5. Variables de play
6. Faits de l’hôte
7. `host_vars` du playbook
8. `group_vars` du playbook
9. `host_vars` de l’inventaire
10. `group_vars` de l’inventaire
11. Valeurs par défaut des rôles

#### Exemples de variables

**Variables de playbook :**
```yaml
---
- name: Déployer l’application
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: Déployer {{ app_name }} version {{ app_version }}
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (propres à l’environnement) :**
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

**Ansible Vault (variables chiffrées) :**
```bash
# Créer un fichier chiffré
ansible-vault create secrets.yml

# Modifier un fichier chiffré
ansible-vault edit secrets.yml

# Contenu de secrets.yml :
# db_password: supersecret123
# api_key: abc123xyz789

# Utiliser dans le playbook
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. Rôles : organiser l’automatisation complexe

Les **rôles** structurent les playbooks et les rendent modulaires et réutilisables.

#### Structure complète d’un rôle

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # Variables par défaut
    ├── vars/
    │   └── main.yml          # Variables du rôle
    ├── tasks/
    │   ├── main.yml          # Liste principale des tâches
    │   ├── install.yml       # Tâches d’installation
    │   └── configure.yml     # Tâches de configuration
    ├── handlers/
    │   └── main.yml          # Gestionnaires (redémarrage des services)
    ├── templates/
    │   ├── nginx.conf.j2     # Modèles Jinja2
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # Fichiers statiques
    ├── meta/
    │   └── main.yml          # Dépendances du rôle
    └── README.md             # Documentation
```

#### Exemple de rôle : nginx

**defaults/main.yml :**
```yaml
---
nginx_port: 80
nginx_user: www-data
nginx_worker_processes: auto
nginx_worker_connections: 1024
```

**tasks/main.yml :**
```yaml
---
- name: Inclure les variables propres au système d’exploitation
  include_vars: "{{ ansible_os_family }}.yml"

- name: Installer Nginx
  include_tasks: install.yml

- name: Configurer Nginx
  include_tasks: configure.yml

- name: Vérifier que Nginx est en cours d’exécution
  service:
    name: nginx
    state: started
    enabled: yes
```

**tasks/install.yml :**
```yaml
---
- name: Installer Nginx (Debian)
  apt:
    name: nginx
    state: present
    update_cache: yes
  when: ansible_os_family == "Debian"

- name: Installer Nginx (RedHat)
  yum:
    name: nginx
    state: present
  when: ansible_os_family == "RedHat"
```

**handlers/main.yml :**
```yaml
---
- name: Redémarrer nginx
  service:
    name: nginx
    state: restarted

- name: Recharger nginx
  service:
    name: nginx
    state: reloaded
```

**templates/nginx.conf.j2 :**
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

**Utiliser le rôle :**
```yaml
---
- name: Configurer les serveurs Web avec le rôle Nginx
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## Concepts avancés d’Ansible (2026)

### Collections Ansible

Les **collections** sont un format de distribution du contenu Ansible, comme les modules, les rôles et les plugins.

#### Installer des collections

```bash
# Installer depuis Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# Installer depuis le fichier de dépendances
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### Utiliser les modules d’une collection

```yaml
---
- name: Utiliser les modules de collection
  hosts: localhost
  tasks:
    - name: Utiliser le module Docker de community.general
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: Utiliser le module AWS EC2
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (fonctions pour les entreprises)

**Ansible Tower** (commercial) et **AWX** (open source) fournissent :

- Interface web d’exécution des playbooks
- Contrôle d’accès basé sur les rôles (RBAC)
- Planification des tâches et flux de travail
- Journalisation et audit centralisés
- API REST pour l’intégration
- Gestion des identifiants
- Synchronisation des inventaires

**Installer AWX avec Docker Compose :**
```bash
# Cloner le dépôt AWX
git clone https://github.com/ansible/awx.git
cd awx

# Déployer avec docker-compose
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# Accéder à http://localhost:80
# Connexion par défaut : admin / password
```

### Automatisation de Windows avec Ansible

En 2026, Ansible prend beaucoup mieux en charge Windows :

**Prérequis Windows :**
```powershell
# Activer WinRM sur l’hôte Windows
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Inventaire Windows :**
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

**Playbook d’automatisation Windows :**
```yaml
---
- name: Configuration du serveur Windows
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: Installer IIS
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: Déployer le site Web
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: Configurer le pare-feu
      win_firewall_rule:
        name: Autoriser HTTP
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: Installer le logiciel via Chocolatey
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### Automatisation réseau avec Ansible

Ansible prend en charge les principaux fournisseurs réseau, dont Cisco, Juniper, Arista et F5.

**Playbook pour les équipements réseau :**
```yaml
---
- name: Configurer les commutateurs Cisco
  hosts: cisco_switches
  gather_facts: no
  connection: network_cli
  
  vars:
    ansible_network_os: ios
    ansible_user: admin
    ansible_password: "{{ vault_switch_password }}"
  
  tasks:
    - name: Configurer les VLAN
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: DATA
          - vlan_id: 20
            name: VOICE
          - vlan_id: 30
            name: GUEST
        state: merged
    
    - name: Configurer l’interface
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Uplink to Core
            enabled: true
    
    - name: Enregistrer la configuration
      cisco.ios.ios_config:
        save_when: always
```

## Cas d’usage et exemples concrets

### Cas d’usage 1 : déploiement complet d’une application web

**Structure du projet :**
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

**site.yml (déploiement de toute la pile) :**
```yaml
---
- name: Configurer tous les serveurs
  hosts: all
  become: yes
  roles:
    - common

- name: Configurer les serveurs de bases de données
  hosts: databases
  become: yes
  roles:
    - postgresql

- name: Configurer les serveurs Web
  hosts: webservers
  become: yes
  roles:
    - nginx
    - application

- name: Configurer les répartiteurs de charge
  hosts: loadbalancers
  become: yes
  roles:
    - haproxy
```

### Cas d’usage 2 : configuration d’un cluster Kubernetes

```yaml
---
- name: Configurer le cluster Kubernetes
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: Installer Docker
      apt:
        name: docker.io
        state: present
    
    - name: Ajouter la clé apt de Kubernetes
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: Ajouter le dépôt Kubernetes
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: Installer les composants Kubernetes
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: Initialiser le maître Kubernetes
  hosts: k8s_master
  become: yes
  tasks:
    - name: Initialiser le cluster
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: Créer le répertoire .kube
      file:
        path: /home/{{ ansible_user }}/.kube
        state: directory
        owner: "{{ ansible_user }}"
    
    - name: Copier admin.conf
      copy:
        src: /etc/kubernetes/admin.conf
        dest: /home/{{ ansible_user }}/.kube/config
        remote_src: yes
        owner: "{{ ansible_user }}"
```

### Cas d’usage 3 : automatisation du renforcement de la sécurité

```yaml
---
- name: Renforcer la sécurité
  hosts: all
  become: yes
  
  tasks:
    - name: Mettre à jour tous les paquets
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: Installer les outils de sécurité
      apt:
        name:
          - fail2ban
          - ufw
          - aide
        state: present
    
    - name: Configurer fail2ban
      copy:
        src: jail.local
        dest: /etc/fail2ban/jail.local
      notify: restart fail2ban
    
    - name: Configurer le pare-feu
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: Activer le pare-feu
      ufw:
        state: enabled
    
    - name: Désactiver la connexion root
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: Définir la politique de mots de passe
      lineinfile:
        path: /etc/login.defs
        regexp: '^PASS_MAX_DAYS'
        line: 'PASS_MAX_DAYS   90'
  
  handlers:
    - name: Redémarrer fail2ban
      service:
        name: fail2ban
        state: restarted
    
    - name: Redémarrer sshd
      service:
        name: sshd
        state: restarted
```

## Bonnes pratiques Ansible (édition 2026)

### 1. Utiliser le contrôle de version (Git)

**Structure du dépôt :**
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

**.gitignore :**
```
*.retry
*.pyc
.vault_pass
secrets.yml
*.log
```

### 2. Rendre les opérations idempotentes

**Mauvais exemple (non idempotent) :**
```yaml
- name: Ajouter une ligne au fichier
  shell: echo "new line" >> /etc/myconfig
```

**Bon exemple (idempotent) :**
```yaml
- name: Vérifier que la ligne figure dans le fichier
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. Utiliser Ansible Lint pour la qualité du code

```bash
# Installer ansible-lint
pip install ansible-lint

# Exécuter le linter
ansible-lint playbook.yml

# Corriger automatiquement les problèmes courants
ansible-lint --fix playbook.yml
```

### 4. Tester avec Molecule

```bash
# Installer Molecule
pip install molecule molecule-docker

# Initialiser un nouveau rôle avec des tests
molecule init role my_role --driver-name docker

# Exécuter les tests
cd my_role
molecule test

# Étapes de test :
# - Créer un environnement de test
# - Converger (exécuter le playbook)
# - Vérifier (exécuter les tests)
# - Détruire l’environnement
```

**Exemple de molecule.yml :**
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

### 5. Utiliser des tags pour cibler l’exécution

```yaml
---
- name: Configuration complète du serveur
  hosts: webservers
  become: yes
  
  tasks:
    - name: Installer les paquets
      apt:
        name: nginx
        state: present
      tags:
        - packages
        - nginx
    
    - name: Configurer Nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags:
        - configuration
        - nginx
    
    - name: Déployer l’application
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# Exécuter uniquement les tâches nginx
# ansible-playbook play.yml --tags nginx

# Ignorer le déploiement
# ansible-playbook play.yml --skip-tags deployment
```

### 6. Gestion des erreurs et débogage

```yaml
---
- name: Exécution robuste des tâches
  hosts: webservers
  
  tasks:
    - name: Tenter une opération risquée
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: Sortie de débogage
      debug:
        var: result
        verbosity: 2
    
    - name: Gérer l’échec
      debug:
        msg: "La commande a échoué, mais l’exécution continue..."
      when: result.rc != 0
    
    - name: Bloc avec reprise
      block:
        - name: Essayer ceci d’abord
          command: /may/fail
        
        - name: En cas de succès, faire ceci
          debug:
            msg: "Réussite !"
      
      rescue:
        - name: En cas d’échec, faire ceci à la place
          debug:
            msg: "Récupération après l’échec"
      
      always:
        - name: Toujours exécuter ceci
          debug:
            msg: "Opérations de nettoyage"
```

### 7. Optimiser les performances

#### Activer le pipelining
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Utiliser Mitogen (performances multipliées par 3 à 7)
```bash
# Installer Mitogen
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

#### Exécution parallèle
```yaml
---
- name: Mises à jour parallèles
  hosts: all
  strategy: free  # Ne pas attendre tous les hôtes
  serial: 10      # Traiter 10 hôtes à la fois
  
  tasks:
    - name: Mettre à jour les paquets
      apt:
        upgrade: dist
```

## Résoudre les problèmes courants

### Problème 1 : échec de la connexion SSH

**Problème :** impossible de se connecter aux hôtes gérés

**Solutions :**
```bash
# Tester la connexion SSH brute
ssh -vvv user@host

# Tester la connexion Ansible
ansible host -m ping -vvv

# Ajouter à l’inventaire
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### Problème 2 : accès refusé (sudo)

**Problème :** les tâches échouent en raison d’erreurs d’autorisation

**Solution :**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: Tâche nécessitant les privilèges root
      file:
        path: /etc/myconfig
        state: touch
```

### Problème 3 : module introuvable

**Problème :** message d’erreur indiquant qu’un module est introuvable

**Solution :**
```bash
# Vérifier que la collection est installée
ansible-galaxy collection install community.general

# Vérifier la collection
ansible-galaxy collection list

# Utiliser FQCN (nom complet qualifié de collection)
community.general.docker_container:
  name: mycontainer
```

### Problème 4 : exécution lente du playbook

**Solutions :**
1. Activez le pipelining (voir la section Performances)
2. Utilisez le plugin de stratégie Mitogen
3. Désactivez la collecte de faits si elle n’est pas nécessaire :
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. Utilisez l’exécution asynchrone pour les tâches longues :
   ```yaml
   - name: Tâche de longue durée
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Parcours professionnel et certifications Ansible

### Progression des compétences

**Débutant (0 à 6 mois) :**
- Écrire des playbooks simples
- Comprendre les inventaires et les variables
- Utiliser les modules courants
- Exécuter des playbooks

**Intermédiaire (6 à 18 mois) :**
- Créer des rôles réutilisables
- Mettre en place la gestion des erreurs
- Utiliser Ansible Vault
- Intégrer Ansible à CI/CD
- Gérer plusieurs environnements

**Avancé (plus de 18 mois) :**
- Concevoir des cadres d’automatisation complexes
- Créer des modules et plugins personnalisés
- Concevoir des déploiements Tower/AWX
- Optimiser les performances
- Accompagner d’autres personnes

### Certifications

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Atteste la maîtrise d’Ansible
- Examen pratique fondé sur des tâches
- Valide pendant trois ans
- Reconnu dans le secteur

**Ressources de préparation :**
- Red Hat Learning Subscription
- Documentation Ansible
- Environnements pratiques (A Cloud Guru, Udemy)
- Forums communautaires

### Marché de l’emploi (2026)

**Salaires moyens aux États-Unis :**
- Ingénieur Ansible junior : $75,000-$95,000
- Ingénieur DevOps intermédiaire (Ansible) : $110,000-$140,000
- Architecte senior en automatisation : $150,000-$190,000

**Compétences recherchées :**
- Ansible et Kubernetes
- Ansible et Terraform (IaC hybride)
- Ansible et CI/CD (Jenkins, GitLab)
- Ansible et cloud (AWS, Azure, GCP)
- Administration d’Ansible Tower/AWX

## Ressources d’apprentissage et communauté

### Documentation officielle
- [Documentation Ansible](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - plateforme de partage des rôles
- [Ansible sur GitHub](https://github.com/ansible/ansible)

### Cours en ligne
- Red Hat Learning Subscription
- Udemy : `Ansible pour les débutants absolus`
- A Cloud Guru : `Ansible pratique`
- Linux Academy : `Démarrage rapide avec Ansible`

### Livres
- `Ansible for DevOps` de Jeff Geerling (mis à jour en 2025)
- `Ansible: Up and Running` de Lorin Hochstein
- `Mastering Ansible` de James Freeman

### Communauté
- [Liste de diffusion Ansible](https://groups.google.com/forum/#!forum/ansible-project)
- [Ansible sur Reddit](https://reddit.com/r/ansible)
- [Serveur Discord Ansible](https://discord.gg/ansible)
- Rencontres Ansible locales et en ligne

### Plateformes de pratique
- [Scénarios Ansible de Katacoda](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Laboratoire local avec Vagrant ou Docker

## Conclusion : commencez votre parcours Ansible

Ansible est devenu l’outil d’automatisation privilégié des organisations dans le monde entier. En 2026, il offre plus de fonctionnalités, une gestion de Windows simplifiée, de meilleures intégrations cloud et la génération de playbooks assistée par IA. Les compétences acquises vous serviront tout au long de votre carrière informatique, que vous gériez une infrastructure traditionnelle, des environnements cloud ou des déploiements hybrides.

**Points clés :**

1. **Commencez simplement** : créez des playbooks de base pour gérer quelques serveurs
2. **Entraînez-vous régulièrement** : mettez en place un laboratoire chez vous et expérimentez
3. **Apprenez par la pratique** : automatisez des tâches réelles de votre travail quotidien
4. **Appliquez les bonnes pratiques** : contrôle de version, tests et documentation
5. **Rejoignez la communauté** : apprenez des autres et partagez vos connaissances
6. **Restez à jour** : Ansible évolue vite, poursuivez votre apprentissage
7. **Combinez les outils** : Ansible, Terraform et Kubernetes permettent ensemble une automatisation étendue

**Étapes suivantes :**

1. Installez Ansible sur votre système
2. Créez un inventaire simple de serveurs de test, de machines virtuelles ou de conteneurs
3. Écrivez votre premier playbook, par exemple pour installer un paquet
4. Ajoutez progressivement des modèles, des variables et des rôles
5. Contribuez aux rôles communautaires sur Ansible Galaxy
6. Envisagez une certification pour valider vos compétences

Le parcours de débutant à expert Ansible est gratifiant et ouvre des perspectives en DevOps, SRE et ingénierie cloud. Grâce aux bases présentées dans ce guide, vous pourrez commencer à automatiser l’infrastructure et à développer des compétences utiles dans l’informatique moderne.

Bienvenue dans le monde de l’automatisation de l’infrastructure avec Ansible !

______

## Références

- [Documentation officielle d’Ansible](https://docs.ansible.com/)
- [Ansible Galaxy - dépôt de rôles](https://galaxy.ansible.com/)
- [Dépôt Ansible sur GitHub](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - Ansible Tower open source](https://github.com/ansible/awx)
- [Bonnes pratiques Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Cadre de test Molecule](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Ansible for DevOps de Jeff Geerling](https://www.ansiblefordevops.com/)
- [Index des collections Ansible](https://docs.ansible.com/ansible/latest/collections/index.html)
