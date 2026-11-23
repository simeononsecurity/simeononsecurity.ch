---
title: "Ansible para iniciantes 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-22
description: "Guia de Ansible para 2026 sobre instalação, playbooks, roles, exemplos, boas práticas e comparação com Terraform, Puppet e Chef."
tags: ["Introdução ao Ansible", "Automação da gestão de infraestrutura de TI", "Fundamentos do Ansible", "Automação de infraestrutura de TI", "Gestão de configuração", "Implantação de aplicações", "Provisionamento", "Entrega contínua", "Segurança e conformidade", "Orquestração", "YAML", "Módulos do Ansible", "Roles", "Boas práticas", "Controle de versão", "Testes", "Red Hat", "Administradores de sistemas", "Linux", "macOS", "Windows", "Instalação do Ansible", "Inventário do Ansible", "Playbooks do Ansible", "Módulos do Ansible", "Roles do Ansible", "Boas práticas do Ansible", "Testes do Ansible", "Ferramenta de automação de infraestrutura de TI", "Tutorial do Ansible", "Automação da gestão de infraestrutura", "Ansible para iniciantes", "Aprender Ansible", "Tutorial do Ansible 2026", "Ansible e Terraform", "Ansible e Puppet", "Exemplos de playbooks do Ansible", "Automação do Ansible", "Ferramentas DevOps", "Infraestrutura como código", "Ansible AWX", "Ansible Tower", "Coleções do Ansible", "Ansible Galaxy", "Ansible Vault", "Automação de nuvem com Ansible"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "Ilustração de uma infraestrutura de TI moderna com servidores e dispositivos interligados. Mostra ligações SSH e WinRM, um ficheiro YAML estilizado e ícones de serviços na nuvem sobre um fundo escuro."
coverCaption: ""
---

**Ansible para iniciantes: guia completo de automação de TI em 2026**

O Ansible tornou-se uma plataforma de automação líder no setor. Segundo a fonte, mais de 80% das empresas da Fortune 500 confiam nele para gerir infraestruturas de TI complexas. Em 2026, continua a ser uma solução importante, simples de utilizar e com funcionalidades para empresas.

Este guia completo leva-te dos conceitos básicos à utilização confiante do Ansible. Abrange conceitos fundamentais, técnicas avançadas, exemplos práticos e boas práticas para 2026.

## O que é o Ansible? Conceitos básicos

**Ansible** é uma plataforma de automação de código aberto que simplifica a gestão da infraestrutura de TI com automação declarativa sem agentes. Ao contrário das ferramentas tradicionais de gestão de configuração, não exige agentes nos nós geridos. Utiliza SSH para Linux e Unix, ou WinRM para Windows, para gerir sistemas remotamente.

{{< youtube id="goclfp6a2IQ" >}}

### Principais características do Ansible

**1. Arquitetura sem agentes:**
- Não exige a instalação de software nos nós geridos
- Utiliza os protocolos SSH ou WinRM existentes
- Reduz a superfície de ataque e o esforço de manutenção
- É mais fácil de começar a utilizar do que ferramentas com agentes

**2. Linguagem declarativa (YAML):**
- Ficheiros de configuração legíveis
- Infraestrutura descrita como estado pretendido
- Operações idempotentes, seguras em execuções repetidas
- Fácil de compreender sem experiência em programação

**3. Modelo push:**
- O nó de controlo envia configurações para os nós geridos
- Executa tarefas de imediato, sem esperar por agentes
- Controlo e visibilidade centralizados
- Adequado para automação a pedido

**4. Biblioteca extensa de módulos:**
- Mais de 5.000 módulos integrados (em 2026)
- Suporta Linux, Windows, dispositivos de rede e plataformas na nuvem
- Módulos da comunidade e dos fornecedores
- É simples escrever módulos personalizados em Python

### O que pode ser automatizado com o Ansible?

O Ansible é adequado para automatizar:

- **Gestão de configuração**: manter configurações de servidores consistentes
- **Implantação de aplicações**: implantar aplicações em vários ambientes
- **Provisionamento**: criar e configurar infraestrutura
- **Entrega contínua**: integrar com pipelines CI/CD
- **Segurança e conformidade**: aplicar políticas de segurança e conformidade
- **Orquestração**: coordenar implantações complexas em várias camadas
- **Automação de nuvem**: gerir AWS, Azure, GCP e outras nuvens
- **Automação de redes**: configurar switches, routers e firewalls
- **Automação de Windows**: gerir servidores e estações de trabalho Windows

### Evolução do Ansible: de 2012 a 2026

**Cronologia:**
- **2012**: Michael DeHaan cria o Ansible
- **2015**: a Red Hat adquire o Ansible
- **2019**: o Ansible Engine 2.8 introduz coleções
- **2020**: o Ansible 2.10+ divide-se em ansible-core e coleções
- **2023**: o Ansible 8.x amplia integrações com a nuvem
- **2026**: o Ansible 10.x inclui geração de playbooks assistida por IA, melhor suporte a Windows e funcionalidades de segurança reforçadas

## Comparação rápida do Ansible com alternativas

| Funcionalidade | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **Tipo** | Gestão de configuração | Provisionamento de infraestrutura | Gestão de configuração | Gestão de configuração |
| **Linguagem** | YAML | HCL | Puppet DSL (semelhante a Ruby) | Ruby DSL |
| **Exige agente** | Não | Não | Sim | Sim |
| **Curva de aprendizagem** | Fácil | Moderada | Íngreme | Íngreme |
| **Ideal para** | Gestão de configuração, implantação | Infraestrutura na nuvem | Grandes empresas | Fluxos de trabalho complexos |
| **Gestão de estado** | Modelo push | Ficheiro de estado declarativo | Modelo pull | Modelo pull |
| **Suporte a Windows** | Excelente (2026) | Limitado | Bom | Bom |
| **Dimensão da comunidade** | Muito grande | Muito grande | Grande | Média |
| **Principal utilização** | Operações diárias | Provisionamento de infraestrutura | Configuração empresarial | Implantação de aplicações |

**Quando escolher Ansible:**
- ✅ Gerir configurações em ambientes híbridos
- ✅ Automatizar a implantação de aplicações
- ✅ É necessária uma curva de aprendizagem curta
- ✅ Preferes uma arquitetura sem agentes
- ✅ É necessária automação avançada de Windows (melhorias em 2026)
- ✅ Já existe uma infraestrutura SSH

**Quando considerar alternativas:**
- Terraform: sobretudo para provisionar infraestrutura (AWS, Azure, GCP)
- Puppet: grandes empresas com milhares de nós
- Chef: fluxos de trabalho complexos centrados em aplicações

## Primeiros passos: instalar o Ansible em 2026

### Requisitos do sistema

**Nó de controlo, onde o Ansible é executado:**
- Linux, macOS ou WSL2 no Windows
- Python 3.9 ou posterior (Python 3.11+ recomendado para 2026)
- 2 GB de RAM no mínimo, 4 GB ou mais recomendados
- 5 GB de espaço em disco para coleções

**Nós geridos:**
- Acesso SSH (Linux/Unix) ou WinRM (Windows)
- Python 2.7 ou Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- Não exigem instalação de agentes

### Métodos de instalação

#### Método 1: gestor de pacotes (recomendado para iniciantes)

**Ubuntu/Debian:**
```bash
# Adicionar o PPA do Ansible para a versão mais recente
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux:**
```bash
# Habilitar o repositório EPEL
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS:**
```bash
# Usar Homebrew
brew install ansible
```

#### Método 2: Python pip (funcionalidades mais recentes)

```bash
# Instalar pipx (ambiente isolado recomendado)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Instalar Ansible com pipx
pipx install --include-deps ansible

# Verificar a instalação
ansible --version
```

#### Método 3: Docker (portátil)

```bash
# Obter o contêiner oficial do Ansible
docker pull quay.io/ansible/ansible:latest

# Executar Ansible em um contêiner
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### Verificar a instalação

```bash
# Verificar a versão do Ansible
ansible --version

# Saída esperada (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### Configuração inicial

Cria o ficheiro de configuração do Ansible:

```bash
# Criar diretório de configuração
mkdir -p ~/.ansible

# Criar ansible.cfg
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

## Conceitos essenciais: componentes do Ansible

### 1. Inventário: definir a infraestrutura

Um **inventário** define os anfitriões e grupos geridos pelo Ansible. Pode ser estático (ficheiro INI ou YAML) ou dinâmico (scripts ou plug-ins).

#### Inventário estático (formato INI)

```ini
# inventory/hosts.ini

# Grupo de servidores web
[webservers]
web1.example.com
web2.example.com
web3.example.com

# Grupo de servidores de banco de dados
[databases]
db1.example.com ansible_host=192.168.1.100
db2.example.com ansible_host=192.168.1.101

# Balanceadores de carga
[loadbalancers]
lb1.example.com

# Grupo de grupos
[production:children]
webservers
databases
loadbalancers

# Variáveis para todos os servidores web
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# Variáveis para todos os hosts
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### Inventário estático (formato YAML, recomendado em 2026)

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

#### Inventário dinâmico (fornecedores de nuvem)

Para ambientes na nuvem, utiliza plug-ins de inventário dinâmico:

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

### 2. Playbooks: planos de automação

Os **playbooks** são ficheiros YAML que descrevem fluxos de trabalho de automação. Definem o estado pretendido da infraestrutura.

#### Exemplo simples de playbook

```yaml
# simple_playbook.yml
---
- name: Configurar servidores web
  hosts: webservers
  become: yes
  
  tasks:
    - name: Instalar Nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Iniciar e habilitar o Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copiar o conteúdo do site
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: Configurar o firewall
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
# Execução básica
ansible-playbook simple_playbook.yml

# Com inventário específico
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# Limitar a hosts específicos
ansible-playbook simple_playbook.yml --limit web1.example.com

# Execução de teste (modo de verificação)
ansible-playbook simple_playbook.yml --check

# Saída detalhada para solução de problemas
ansible-playbook simple_playbook.yml -vvv
```

### 3. Módulos: unidades de tarefa reutilizáveis

Os módulos do Ansible são os componentes básicos da automação. Cada módulo executa uma tarefa específica.

#### Módulos comuns (2026)

**Módulos do sistema:**
```yaml
# Gerenciamento de pacotes
- name: Instalar pacotes (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# Gerenciamento de serviços
- name: Gerenciar serviços
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**Módulos de ficheiros:**
```yaml
# Operações com arquivos
- name: Criar diretório
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# Copiar arquivos
- name: Implantar a configuração
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# Modelo com variáveis
- name: Implantar a configuração do nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**Módulos de nuvem (exemplo AWS):**
```yaml
# Criar instância EC2
- name: Iniciar uma instância EC2
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

# Criar bucket S3
- name: Criar bucket do S3
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**Módulos de bases de dados:**
```yaml
# Gerenciamento de banco de dados MySQL
- name: Criar banco de dados MySQL
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: Criar usuário MySQL
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. Variáveis: flexibilizar os playbooks

As variáveis permitem reutilizar playbooks em vários ambientes.

#### Prioridade das variáveis (da mais alta para a mais baixa)

1. Variáveis adicionais (`-e` na linha de comandos)
2. Variáveis de tarefa
3. Variáveis de bloco
4. Variáveis de role e include
5. Variáveis de play
6. Factos do anfitrião
7. `host_vars` do playbook
8. `group_vars` do playbook
9. `host_vars` do inventário
10. `group_vars` do inventário
11. Valores predefinidos das roles

#### Exemplos de variáveis

**Variáveis do playbook:**
```yaml
---
- name: Implantar o aplicativo
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: Implantar {{ app_name }} versão {{ app_version }}
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (específicas do ambiente):**
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

**Ansible Vault (variáveis encriptadas):**
```bash
# Criar arquivo criptografado
ansible-vault create secrets.yml

# Editar arquivo criptografado
ansible-vault edit secrets.yml

# Conteúdo de secrets.yml:
# db_password: supersecret123
# api_key: abc123xyz789

# Usar no playbook
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. Roles: organizar automação complexa

As **roles** oferecem uma forma estruturada de organizar playbooks e torná-los modulares e reutilizáveis.

#### Estrutura completa de uma role

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # Variáveis padrão
    ├── vars/
    │   └── main.yml          # Variáveis da função
    ├── tasks/
    │   ├── main.yml          # Lista principal de tarefas
    │   ├── install.yml       # Tarefas de instalação
    │   └── configure.yml     # Tarefas de configuração
    ├── handlers/
    │   └── main.yml          # Manipuladores (reiniciar serviços)
    ├── templates/
    │   ├── nginx.conf.j2     # Modelos Jinja2
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # Arquivos estáticos
    ├── meta/
    │   └── main.yml          # Dependências da função
    └── README.md             # Documentação
```

#### Exemplo de role: nginx

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
- name: Incluir variáveis específicas do sistema operacional
  include_vars: "{{ ansible_os_family }}.yml"

- name: Instalar Nginx
  include_tasks: install.yml

- name: Configurar o Nginx
  include_tasks: configure.yml

- name: Garantir que o Nginx esteja em execução
  service:
    name: nginx
    state: started
    enabled: yes
```

**tasks/install.yml:**
```yaml
---
- name: Instalar Nginx (Debian)
  apt:
    name: nginx
    state: present
    update_cache: yes
  when: ansible_os_family == "Debian"

- name: Instalar Nginx (RedHat)
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

**Utilizar a role:**
```yaml
---
- name: Configurar servidores web com a função Nginx
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## Conceitos avançados do Ansible (2026)

### Coleções do Ansible

As **coleções** são um formato de distribuição de conteúdo do Ansible, como módulos, roles e plug-ins.

#### Instalar coleções

```bash
# Instalar pelo Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# Instalar pelo arquivo de requisitos
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### Utilizar módulos de coleções

```yaml
---
- name: Usar módulos de coleção
  hosts: localhost
  tasks:
    - name: Usar o módulo Docker de community.general
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: Usar o módulo AWS EC2
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (funcionalidades empresariais)

O **Ansible Tower** (comercial) e o **AWX** (código aberto) oferecem:

- Interface Web para executar playbooks
- Controlo de acesso baseado em roles (RBAC)
- Agendamento de tarefas e fluxos de trabalho
- Registo e auditoria centralizados
- API REST para integração
- Gestão de credenciais
- Sincronização de inventários

**Instalação do AWX (Docker Compose):**
```bash
# Clonar repositório AWX
git clone https://github.com/ansible/awx.git
cd awx

# Implantar usando docker-compose
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# Acessar http://localhost:80
# Login padrão: admin / password
```

### Automação de Windows com Ansible

Em 2026, o Ansible oferece um suporte muito melhor a Windows:

**Pré-requisitos de Windows:**
```powershell
# Habilitar WinRM no host Windows
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Inventário para Windows:**
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

**Playbook de automação de Windows:**
```yaml
---
- name: Configuração do servidor Windows
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: Instalar IIS
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: Implantar o site
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: Configurar o firewall
      win_firewall_rule:
        name: Permitir HTTP
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: Instalar software pelo Chocolatey
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### Automação de redes com Ansible

O Ansible suporta os principais fornecedores de redes, incluindo Cisco, Juniper, Arista e F5.

**Playbook para dispositivos de rede:**
```yaml
---
- name: Configurar switches Cisco
  hosts: cisco_switches
  gather_facts: no
  connection: network_cli
  
  vars:
    ansible_network_os: ios
    ansible_user: admin
    ansible_password: "{{ vault_switch_password }}"
  
  tasks:
    - name: Configurar VLANs
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: DATA
          - vlan_id: 20
            name: VOICE
          - vlan_id: 30
            name: GUEST
        state: merged
    
    - name: Configurar a interface
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Ligação ascendente para o núcleo
            enabled: true
    
    - name: Salvar a configuração
      cisco.ios.ios_config:
        save_when: always
```

## Casos de utilização e exemplos reais

### Caso de utilização 1: implantação completa de uma aplicação Web

**Estrutura do projeto:**
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

**site.yml (implantação de toda a pilha):**
```yaml
---
- name: Configurar todos os servidores
  hosts: all
  become: yes
  roles:
    - common

- name: Configurar servidores de banco de dados
  hosts: databases
  become: yes
  roles:
    - postgresql

- name: Configurar servidores web
  hosts: webservers
  become: yes
  roles:
    - nginx
    - application

- name: Configurar balanceadores de carga
  hosts: loadbalancers
  become: yes
  roles:
    - haproxy
```

### Caso de utilização 2: configurar um cluster Kubernetes

```yaml
---
- name: Configurar cluster Kubernetes
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: Instalar Docker
      apt:
        name: docker.io
        state: present
    
    - name: Adicionar chave apt do Kubernetes
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: Adicionar repositório Kubernetes
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: Instalar componentes do Kubernetes
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: Inicializar o mestre Kubernetes
  hosts: k8s_master
  become: yes
  tasks:
    - name: Inicializar cluster
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: Criar diretório .kube
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

### Caso de utilização 3: automatizar o reforço da segurança

```yaml
---
- name: Reforçar a segurança
  hosts: all
  become: yes
  
  tasks:
    - name: Atualizar todos os pacotes
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: Instalar ferramentas de segurança
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
    
    - name: Configurar o firewall
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: Ativar firewall
      ufw:
        state: enabled
    
    - name: Desativar login root
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: Definir política de senhas
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

## Boas práticas do Ansible (edição de 2026)

### 1. Utilizar controlo de versões (Git)

**Estrutura do repositório:**
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

### 2. Implementar idempotência

**Incorreto (não idempotente):**
```yaml
- name: Adicionar linha ao arquivo
  shell: echo "new line" >> /etc/myconfig
```

**Correto (idempotente):**
```yaml
- name: Garantir que a linha esteja no arquivo
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. Utilizar Ansible Lint para a qualidade do código

```bash
# Instalar ansible-lint
pip install ansible-lint

# Executar o linter
ansible-lint playbook.yml

# Corrigir problemas comuns automaticamente
ansible-lint --fix playbook.yml
```

### 4. Implementar testes com Molecule

```bash
# Instalar Molecule
pip install molecule molecule-docker

# Inicializar nova função com testes
molecule init role my_role --driver-name docker

# Executar testes
cd my_role
molecule test

# Etapas de teste:
# - Criar ambiente de teste
# - Convergir (executar playbook)
# - Verificar (executar testes)
# - Destruir ambiente
```

**Exemplo de molecule.yml:**
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

### 5. Utilizar etiquetas para execução seletiva

```yaml
---
- name: Configuração completa do servidor
  hosts: webservers
  become: yes
  
  tasks:
    - name: Instalar pacotes
      apt:
        name: nginx
        state: present
      tags:
        - packages
        - nginx
    
    - name: Configurar o Nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags:
        - configuration
        - nginx
    
    - name: Implantar aplicativo
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# Executar apenas tarefas nginx
# ansible-playbook play.yml --tags nginx

# Ignorar implantação
# ansible-playbook play.yml --skip-tags deployment
```

### 6. Tratamento de erros e depuração

```yaml
---
- name: Execução robusta de tarefas
  hosts: webservers
  
  tasks:
    - name: Tentar operação arriscada
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: Saída de depuração
      debug:
        var: result
        verbosity: 2
    
    - name: Lidar com falha
      debug:
        msg: "O comando falhou, mas a execução continua..."
      when: result.rc != 0
    
    - name: Bloco com recuperação
      block:
        - name: Tentar isto primeiro
          command: /may/fail
        
        - name: Se funcionar, faça isto
          debug:
            msg: "Sucesso!"
      
      rescue:
        - name: Se falhar, faça isto em vez disso
          debug:
            msg: "Recuperado após a falha"
      
      always:
        - name: Sempre executar isto
          debug:
            msg: "Operações de limpeza"
```

### 7. Otimizar o desempenho

#### Ativar o pipelining
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Utilizar Mitogen (desempenho 3 a 7 vezes superior)
```bash
# Instalar Mitogen
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

#### Execução paralela
```yaml
---
- name: Atualizações paralelas
  hosts: all
  strategy: free  # Não esperar todos os hosts
  serial: 10      # Processar 10 hosts por vez
  
  tasks:
    - name: Atualizar pacotes
      apt:
        upgrade: dist
```

## Resolução de problemas comuns

### Problema 1: falhas na ligação SSH

**Problema:** não é possível ligar aos anfitriões geridos

**Soluções:**
```bash
# Testar conexão SSH bruta
ssh -vvv user@host

# Testar conexão do Ansible
ansible host -m ping -vvv

# Adicionar ao inventário
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### Problema 2: acesso negado (sudo)

**Problema:** as tarefas falham devido a erros de permissões

**Solução:**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: Tarefa que exige root
      file:
        path: /etc/myconfig
        state: touch
```

### Problema 3: módulo não encontrado

**Problema:** erros de módulo não encontrado

**Solução:**
```bash
# Garantir que a coleção esteja instalada
ansible-galaxy collection install community.general

# Verificar a coleção
ansible-galaxy collection list

# Usar FQCN (nome totalmente qualificado da coleção)
community.general.docker_container:
  name: mycontainer
```

### Problema 4: execução lenta do playbook

**Soluções:**
1. Ativa o pipelining (consulta a secção Desempenho)
2. Utiliza o plug-in de estratégia Mitogen
3. Desativa a recolha de factos se não for necessária:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. Utiliza execução assíncrona para tarefas demoradas:
   ```yaml
   - name: Tarefa de longa duração
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Percurso profissional e certificações Ansible

### Progressão de competências

**Iniciante (0-6 meses):**
- Escreve playbooks básicos
- Compreende inventários e variáveis
- Utiliza módulos comuns
- Executa playbooks

**Intermédio (6-18 meses):**
- Cria roles reutilizáveis
- Implementa tratamento de erros
- Utiliza Ansible Vault
- Integra com CI/CD
- Gere vários ambientes

**Avançado (mais de 18 meses):**
- Concebe estruturas de automação complexas
- Cria módulos e plug-ins personalizados
- Concebe implantações do Tower/AWX
- Otimiza o desempenho
- Orienta outras pessoas

### Certificações

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Demonstra competências em Ansible
- Exame prático baseado no desempenho
- Válido por 3 anos
- Reconhecido pelo setor

**Recursos de preparação:**
- Red Hat Learning Subscription
- Documentação do Ansible
- Laboratórios práticos (A Cloud Guru, Udemy)
- Fóruns da comunidade

### Mercado de trabalho (2026)

**Salários médios nos EUA:**
- Engenheiro Ansible júnior: $75,000-$95,000
- Engenheiro DevOps de nível intermédio (Ansible): $110,000-$140,000
- Arquiteto sénior de automação: $150,000-$190,000

**Competências procuradas:**
- Ansible e Kubernetes
- Ansible e Terraform (IaC híbrida)
- Ansible e CI/CD (Jenkins, GitLab)
- Ansible e nuvem (AWS, Azure, GCP)
- Administração do Ansible Tower/AWX

## Recursos de aprendizagem e comunidade

### Documentação oficial
- [Documentação do Ansible](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - plataforma de partilha de roles
- [Ansible no GitHub](https://github.com/ansible/ansible)

### Cursos online
- Red Hat Learning Subscription
- Udemy: `Ansible para iniciantes absolutos`
- A Cloud Guru: `Ansible prático`
- Linux Academy: `Início rápido do Ansible`

### Livros
- `Ansible for DevOps` de Jeff Geerling (atualizado em 2025)
- `Ansible: Up and Running` de Lorin Hochstein
- `Mastering Ansible` de James Freeman

### Comunidade
- [Lista de correio do Ansible](https://groups.google.com/forum/#!forum/ansible-project)
- [Ansible no Reddit](https://reddit.com/r/ansible)
- [Servidor do Ansible no Discord](https://discord.gg/ansible)
- Encontros Ansible locais e virtuais

### Plataformas de prática
- [Cenários Ansible da Katacoda](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Laboratório local com Vagrant ou Docker

## Conclusão: começa o teu percurso com Ansible

O Ansible tornou-se a ferramenta de automação escolhida por organizações em todo o mundo. Em 2026, oferece mais capacidades, gestão de Windows simplificada, melhores integrações com a nuvem e geração de playbooks assistida por IA. As competências que desenvolveres serão úteis ao longo da tua carreira em TI, quer gerias infraestrutura tradicional, ambientes na nuvem ou implantações híbridas.

**Pontos principais:**

1. **Começa pelo simples**: cria playbooks básicos para gerir alguns servidores
2. **Pratica regularmente**: configura um laboratório em casa e experimenta
3. **Aprende fazendo**: automatiza tarefas reais do teu trabalho diário
4. **Segue boas práticas**: controlo de versões, testes e documentação
5. **Junta-te à comunidade**: aprende com outras pessoas e partilha o que sabes
6. **Mantém-te atualizado**: o Ansible evolui rapidamente, continua a aprender
7. **Combina ferramentas**: Ansible, Terraform e Kubernetes permitem automatizar mais tarefas

**Próximos passos:**

1. Instala o Ansible no teu sistema
2. Cria um inventário simples de servidores de teste, máquinas virtuais ou contentores
3. Escreve o teu primeiro playbook, por exemplo para instalar um pacote
4. Acrescenta complexidade gradualmente com modelos, variáveis e roles
5. Contribui para roles comunitárias no Ansible Galaxy
6. Considera uma certificação para validar as tuas competências

O percurso de iniciante a especialista em Ansible é gratificante e abre oportunidades em DevOps, SRE e engenharia de nuvem. Com os conceitos fundamentais deste guia, podes começar a automatizar a infraestrutura e desenvolver competências valiosas para o setor de TI moderno.

Bem-vindo ao mundo da automação de infraestrutura com Ansible!

______

## Referências

- [Documentação oficial do Ansible](https://docs.ansible.com/)
- [Ansible Galaxy - repositório de roles](https://galaxy.ansible.com/)
- [Repositório do Ansible no GitHub](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - Ansible Tower de código aberto](https://github.com/ansible/awx)
- [Boas práticas do Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Estrutura de testes Molecule](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Ansible for DevOps de Jeff Geerling](https://www.ansiblefordevops.com/)
- [Índice de coleções do Ansible](https://docs.ansible.com/ansible/latest/collections/index.html)
