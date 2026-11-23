---
title: "Ansible para principiantes 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-22
description: "Guía de Ansible para 2026 sobre instalación, playbooks, roles, ejemplos, buenas prácticas y comparaciones con Terraform, Puppet y Chef."
tags: ["Introducción a Ansible", "Automatización de la gestión de infraestructura de TI", "Fundamentos de Ansible", "Automatización de infraestructura de TI", "Gestión de configuración", "Implementación de aplicaciones", "Aprovisionamiento", "Entrega continua", "Seguridad y cumplimiento", "Orquestación", "YAML", "Módulos de Ansible", "Roles", "Buenas prácticas", "Control de versiones", "Pruebas", "Red Hat", "Administradores de sistemas", "Linux", "macOS", "Windows", "Instalación de Ansible", "Inventario de Ansible", "Playbooks de Ansible", "Módulos de Ansible", "Roles de Ansible", "Buenas prácticas de Ansible", "Pruebas de Ansible", "Herramienta de automatización de infraestructura de TI", "Tutorial de Ansible", "Automatización de la gestión de infraestructura", "Ansible para principiantes", "Aprender Ansible", "Tutorial de Ansible 2026", "Ansible frente a Terraform", "Ansible frente a Puppet", "Ejemplos de playbooks de Ansible", "Automatización con Ansible", "Herramientas DevOps", "Infraestructura como código", "Ansible AWX", "Ansible Tower", "Colecciones de Ansible", "Ansible Galaxy", "Ansible Vault", "Automatización de nube con Ansible"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "Ilustración de una infraestructura de TI moderna con servidores y dispositivos interconectados. Muestra conexiones SSH y WinRM, un archivo YAML estilizado e iconos de servicios en la nube sobre un fondo oscuro."
coverCaption: ""
---

**Ansible para principiantes: guía completa de automatización de TI para 2026**

Ansible se ha convertido en una plataforma de automatización líder. Según la fuente, más del 80 % de las empresas de Fortune 500 confían en Ansible para administrar infraestructuras de TI complejas. En 2026 sigue siendo una solución importante, fácil de usar y con funciones para empresas.

Esta guía completa te lleva desde los conceptos básicos hasta un uso seguro de Ansible. Incluye conceptos fundamentales, técnicas avanzadas, ejemplos prácticos y buenas prácticas para 2026.

## ¿Qué es Ansible? Conceptos básicos

**Ansible** es una plataforma de automatización de código abierto que simplifica la gestión de infraestructura de TI mediante automatización declarativa sin agentes. A diferencia de las herramientas tradicionales de gestión de configuración, no requiere agentes en los nodos administrados. Usa SSH para Linux y Unix, o WinRM para Windows, para la administración remota.

{{< youtube id="goclfp6a2IQ" >}}

### Características clave de Ansible

**1. Arquitectura sin agentes:**
- No requiere instalar software en los nodos administrados
- Usa los protocolos SSH o WinRM existentes
- Reduce la superficie de ataque y la carga de mantenimiento
- Es más fácil empezar que con herramientas basadas en agentes

**2. Lenguaje declarativo (YAML):**
- Archivos de configuración legibles
- Infraestructura descrita como estado deseado
- Operaciones idempotentes, seguras al ejecutarse varias veces
- Fácil de entender sin experiencia en programación

**3. Modelo push:**
- El nodo de control envía configuraciones a los nodos administrados
- Ejecuta tareas de inmediato, sin esperar a los agentes
- Control y visibilidad centralizados
- Adecuado para automatización bajo demanda

**4. Amplia biblioteca de módulos:**
- Más de 5.000 módulos integrados (en 2026)
- Admite Linux, Windows, dispositivos de red y plataformas en la nube
- Módulos de la comunidad y de proveedores
- Es fácil escribir módulos personalizados en Python

### ¿Qué se puede automatizar con Ansible?

Ansible es adecuado para automatizar:

- **Gestión de configuración**: mantener configuraciones de servidor coherentes
- **Implementación de aplicaciones**: implementar aplicaciones en distintos entornos
- **Aprovisionamiento**: crear y configurar infraestructura
- **Entrega continua**: integrar canalizaciones de CI/CD
- **Seguridad y cumplimiento**: aplicar políticas de seguridad y cumplimiento
- **Orquestación**: coordinar implementaciones complejas de varias capas
- **Automatización de nube**: administrar AWS, Azure, GCP y otras nubes
- **Automatización de redes**: configurar switches, routers y firewalls
- **Automatización de Windows**: administrar servidores y estaciones de trabajo Windows

### Evolución de Ansible: de 2012 a 2026

**Cronología:**
- **2012**: Michael DeHaan crea Ansible
- **2015**: Red Hat adquiere Ansible
- **2019**: Ansible Engine 2.8 introduce las colecciones
- **2020**: Ansible 2.10+ se divide en ansible-core y colecciones
- **2023**: Ansible 8.x amplía las integraciones con la nube
- **2026**: Ansible 10.x incorpora generación de playbooks asistida por IA, mejor compatibilidad con Windows y funciones de seguridad ampliadas

## Comparación rápida de Ansible con sus competidores

| Función | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **Tipo** | Gestión de configuración | Aprovisionamiento de infraestructura | Gestión de configuración | Gestión de configuración |
| **Lenguaje** | YAML | HCL | Puppet DSL (similar a Ruby) | Ruby DSL |
| **Requiere agente** | No | No | Sí | Sí |
| **Curva de aprendizaje** | Fácil | Moderada | Pronunciada | Pronunciada |
| **Ideal para** | Gestión de configuración, implementación | Infraestructura en la nube | Grandes empresas | Flujos de trabajo complejos |
| **Gestión del estado** | Modelo push | Archivo de estado declarativo | Modelo pull | Modelo pull |
| **Compatibilidad con Windows** | Excelente (2026) | Limitada | Buena | Buena |
| **Tamaño de la comunidad** | Muy grande | Muy grande | Grande | Mediana |
| **Uso principal** | Operaciones diarias | Aprovisionamiento de infraestructura | Configuración empresarial | Implementación de aplicaciones |

**Cuándo elegir Ansible:**
- ✅ Gestionar la configuración en entornos híbridos
- ✅ Automatizar la implementación de aplicaciones
- ✅ Se necesita una curva de aprendizaje corta
- ✅ Se prefiere una arquitectura sin agentes
- ✅ Se necesita una automatización sólida de Windows (mejoras de 2026)
- ✅ Ya existe una infraestructura SSH

**Cuándo considerar alternativas:**
- Terraform: principalmente para aprovisionar infraestructura (AWS, Azure, GCP)
- Puppet: grandes empresas con miles de nodos
- Chef: flujos de trabajo complejos centrados en aplicaciones

## Primeros pasos: instalar Ansible en 2026

### Requisitos del sistema

**Nodo de control, donde se ejecuta Ansible:**
- Linux, macOS o WSL2 en Windows
- Python 3.9 o posterior (se recomienda Python 3.11+ para 2026)
- 2 GB de RAM como mínimo, se recomiendan 4 GB o más
- 5 GB de espacio en disco para colecciones

**Nodos administrados:**
- Acceso SSH (Linux/Unix) o WinRM (Windows)
- Python 2.7 o Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- No requieren instalar agentes

### Métodos de instalación

#### Método 1: gestor de paquetes (recomendado para principiantes)

**Ubuntu/Debian:**
```bash
# Añadir el PPA de Ansible para la versión más reciente
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux:**
```bash
# Habilitar el repositorio EPEL
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS:**
```bash
# Usar Homebrew
brew install ansible
```

#### Método 2: Python pip (funciones más recientes)

```bash
# Instalar pipx (entorno aislado recomendado)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Instalar Ansible con pipx
pipx install --include-deps ansible

# Verificar la instalación
ansible --version
```

#### Método 3: Docker (portátil)

```bash
# Descargar el contenedor oficial de Ansible
docker pull quay.io/ansible/ansible:latest

# Ejecutar Ansible en un contenedor
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### Verificar la instalación

```bash
# Comprobar la versión de Ansible
ansible --version

# Salida esperada (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### Configuración inicial

Crea el archivo de configuración de Ansible:

```bash
# Crear directorio de configuración
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

## Conceptos esenciales: componentes de Ansible

### 1. Inventario: definir tu infraestructura

Un **inventario** define los hosts y grupos que administra Ansible. Puede ser estático (archivo INI o YAML) o dinámico (scripts o complementos).

#### Inventario estático (formato INI)

```ini
# inventory/hosts.ini

# Grupo de servidores web
[webservers]
web1.example.com
web2.example.com
web3.example.com

# Grupo de servidores de bases de datos
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

# Variables para todos los servidores web
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# Variables para todos los hosts
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### Inventario estático (formato YAML, recomendado en 2026)

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

#### Inventario dinámico (proveedores de nube)

En entornos de nube, usa complementos de inventario dinámico:

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

### 2. Playbooks: planos de automatización

Los **playbooks** son archivos YAML que describen flujos de trabajo de automatización. Definen el estado deseado de tu infraestructura.

#### Ejemplo sencillo de playbook

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
    
    - name: Iniciar y habilitar Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copiar el contenido del sitio web
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: Configurar el cortafuegos
      ufw:
        rule: allow
        port: '{{ item }}'
        proto: tcp
      loop:
        - 80
        - 443
```

#### Ejecutar playbooks

```bash
# Ejecución básica
ansible-playbook simple_playbook.yml

# Con un inventario específico
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# Limitar a hosts específicos
ansible-playbook simple_playbook.yml --limit web1.example.com

# Prueba en seco (modo de comprobación)
ansible-playbook simple_playbook.yml --check

# Salida detallada para solucionar problemas
ansible-playbook simple_playbook.yml -vvv
```

### 3. Módulos: unidades de tareas reutilizables

Los módulos de Ansible son los componentes básicos de la automatización. Cada módulo realiza una tarea específica.

#### Módulos comunes (2026)

**Módulos del sistema:**
```yaml
# Administración de paquetes
- name: Instalar paquetes (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# Administración de servicios
- name: Administrar servicios
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**Módulos de archivos:**
```yaml
# Operaciones con archivos
- name: Crear un directorio
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# Copiar archivos
- name: Implementar la configuración
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# Plantilla con variables
- name: Implementar la configuración de nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**Módulos de nube (ejemplo de AWS):**
```yaml
# Crear una instancia EC2
- name: Iniciar una instancia EC2
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
- name: Crear un bucket de S3
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**Módulos de bases de datos:**
```yaml
# Administración de bases de datos MySQL
- name: Crear una base de datos MySQL
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: Crear un usuario de MySQL
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. Variables: hacer flexibles los playbooks

Las variables permiten reutilizar playbooks en distintos entornos.

#### Prioridad de variables (de mayor a menor)

1. Variables adicionales (`-e` en la línea de comandos)
2. Variables de tarea
3. Variables de bloque
4. Variables de rol e inclusión
5. Variables de play
6. Datos del host
7. `host_vars` del playbook
8. `group_vars` del playbook
9. `host_vars` del inventario
10. `group_vars` del inventario
11. Valores predeterminados de los roles

#### Ejemplos de variables

**Variables del playbook:**
```yaml
---
- name: Implementar la aplicación
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: Implementar {{ app_name }} versión {{ app_version }}
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (específicas del entorno):**
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

**Ansible Vault (variables cifradas):**
```bash
# Crear archivo cifrado
ansible-vault create secrets.yml

# Editar archivo cifrado
ansible-vault edit secrets.yml

# Contenido de secrets.yml:
# db_password: supersecret123
# api_key: abc123xyz789

# Usar en el playbook
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. Roles: organizar automatizaciones complejas

Los **roles** ofrecen una forma estructurada de organizar playbooks y hacerlos modulares y reutilizables.

#### Estructura completa de un rol

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # Variables predeterminadas
    ├── vars/
    │   └── main.yml          # Variables del rol
    ├── tasks/
    │   ├── main.yml          # Lista principal de tareas
    │   ├── install.yml       # Tareas de instalación
    │   └── configure.yml     # Tareas de configuración
    ├── handlers/
    │   └── main.yml          # Manejadores (reiniciar servicios)
    ├── templates/
    │   ├── nginx.conf.j2     # Plantillas Jinja2
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # Archivos estáticos
    ├── meta/
    │   └── main.yml          # Dependencias del rol
    └── README.md             # Documentación
```

#### Ejemplo de rol: nginx

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
- name: Incluir variables específicas del sistema operativo
  include_vars: "{{ ansible_os_family }}.yml"

- name: Instalar Nginx
  include_tasks: install.yml

- name: Configurar Nginx
  include_tasks: configure.yml

- name: Asegurar que Nginx esté en ejecución
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

- name: Recargar nginx
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

**Uso del rol:**
```yaml
---
- name: Configurar servidores web con el rol de Nginx
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## Conceptos avanzados de Ansible (2026)

### Colecciones de Ansible

Las **colecciones** son un formato de distribución de contenido de Ansible, como módulos, roles y complementos.

#### Instalar colecciones

```bash
# Instalar desde Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# Instalar desde el archivo de requisitos
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### Usar módulos de colecciones

```yaml
---
- name: Usar módulos de colecciones
  hosts: localhost
  tasks:
    - name: Usar el módulo Docker de community.general
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: Usar el módulo AWS EC2
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (funciones empresariales)

**Ansible Tower** (comercial) y **AWX** (código abierto) ofrecen:

- Interfaz web para ejecutar playbooks
- Control de acceso basado en roles (RBAC)
- Programación de tareas y flujos de trabajo
- Registro y auditoría centralizados
- API REST para integraciones
- Gestión de credenciales
- Sincronización de inventarios

**Instalación de AWX con Docker Compose:**
```bash
# Clonar el repositorio AWX
git clone https://github.com/ansible/awx.git
cd awx

# Implementar con docker-compose
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# Acceder a http://localhost:80
# Inicio de sesión predeterminado: admin / password
```

### Automatización de Windows con Ansible

En 2026, Ansible ofrece una compatibilidad con Windows mucho mejor:

**Requisitos previos de Windows:**
```powershell
# Habilitar WinRM en el host Windows
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Inventario para Windows:**
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

**Playbook de automatización de Windows:**
```yaml
---
- name: Configuración del servidor Windows
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: Instalar IIS
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: Implementar el sitio web
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: Configurar el cortafuegos
      win_firewall_rule:
        name: Permitir HTTP
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: Instalar software mediante Chocolatey
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### Automatización de redes con Ansible

Ansible es compatible con proveedores de redes importantes, incluidos Cisco, Juniper, Arista y F5.

**Playbook para dispositivos de red:**
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
    
    - name: Configurar interfaz
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Enlace ascendente al núcleo
            enabled: true
    
    - name: Guardar configuración
      cisco.ios.ios_config:
        save_when: always
```

## Casos de uso y ejemplos reales

### Caso de uso 1: implementación completa de una aplicación web

**Estructura del proyecto:**
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

**site.yml (implementación de toda la pila):**
```yaml
---
- name: Configurar todos los servidores
  hosts: all
  become: yes
  roles:
    - common

- name: Configurar servidores de bases de datos
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

### Caso de uso 2: configurar un clúster de Kubernetes

```yaml
---
- name: Configurar clúster de Kubernetes
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: Instalar Docker
      apt:
        name: docker.io
        state: present
    
    - name: Añadir clave apt de Kubernetes
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: Añadir repositorio de Kubernetes
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: Instalar componentes de Kubernetes
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: Inicializar el maestro de Kubernetes
  hosts: k8s_master
  become: yes
  tasks:
    - name: Inicializar clúster
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: Crear directorio .kube
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

### Caso de uso 3: automatizar el refuerzo de la seguridad

```yaml
---
- name: Reforzar la seguridad
  hosts: all
  become: yes
  
  tasks:
    - name: Actualizar todos los paquetes
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: Instalar herramientas de seguridad
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
    
    - name: Configurar el cortafuegos
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: Habilitar cortafuegos
      ufw:
        state: enabled
    
    - name: Deshabilitar inicio de sesión de root
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: Establecer política de contraseñas
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

## Buenas prácticas de Ansible (edición 2026)

### 1. Usa el control de versiones (Git)

**Estructura del repositorio:**
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

### 2. Implementa la idempotencia

**Incorrecto (no idempotente):**
```yaml
- name: Añadir línea al archivo
  shell: echo "new line" >> /etc/myconfig
```

**Correcto (idempotente):**
```yaml
- name: Asegurarse de que la línea esté en el archivo
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. Usa Ansible Lint para revisar la calidad del código

```bash
# Instalar ansible-lint
pip install ansible-lint

# Ejecutar el linter
ansible-lint playbook.yml

# Corregir problemas comunes automáticamente
ansible-lint --fix playbook.yml
```

### 4. Implementa pruebas con Molecule

```bash
# Instalar Molecule
pip install molecule molecule-docker

# Inicializar un rol nuevo con pruebas
molecule init role my_role --driver-name docker

# Ejecutar pruebas
cd my_role
molecule test

# Etapas de prueba:
# - Crear entorno de prueba
# - Converger (ejecutar playbook)
# - Verificar (ejecutar pruebas)
# - Destruir el entorno
```

**Ejemplo de molecule.yml:**
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

### 5. Usa etiquetas para ejecutar tareas selectivamente

```yaml
---
- name: Configuración completa del servidor
  hosts: webservers
  become: yes
  
  tasks:
    - name: Instalar paquetes
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
    
    - name: Implementar la aplicación
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# Ejecutar solo las tareas de nginx
# ansible-playbook play.yml --tags nginx

# Omitir implementación
# ansible-playbook play.yml --skip-tags deployment
```

### 6. Gestión de errores y depuración

```yaml
---
- name: Ejecución robusta de tareas
  hosts: webservers
  
  tasks:
    - name: Intentar una operación arriesgada
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: Salida de depuración
      debug:
        var: result
        verbosity: 2
    
    - name: Gestionar el fallo
      debug:
        msg: "El comando falló, pero la ejecución continúa..."
      when: result.rc != 0
    
    - name: Bloque con recuperación
      block:
        - name: Probar esto primero
          command: /may/fail
        
        - name: Si funciona, hacer esto
          debug:
            msg: "¡Éxito!"
      
      rescue:
        - name: Si falla, hacer esto en su lugar
          debug:
            msg: "Recuperación tras el error"
      
      always:
        - name: Ejecutar siempre esto
          debug:
            msg: "Operaciones de limpieza"
```

### 7. Optimizar el rendimiento

#### Habilitar pipelining
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Usar Mitogen (rendimiento de 3 a 7 veces mayor)
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

#### Ejecución en paralelo
```yaml
---
- name: Actualizaciones en paralelo
  hosts: all
  strategy: free  # No esperar a todos los hosts
  serial: 10      # Procesar 10 hosts a la vez
  
  tasks:
    - name: Actualizar paquetes
      apt:
        upgrade: dist
```

## Solucionar problemas comunes

### Problema 1: fallos de conexión SSH

**Problema:** no se puede conectar a los hosts administrados

**Soluciones:**
```bash
# Probar conexión SSH directa
ssh -vvv user@host

# Probar conexión de Ansible
ansible host -m ping -vvv

# Añadir al inventario
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### Problema 2: permiso denegado (sudo)

**Problema:** las tareas fallan debido a errores de permisos

**Solución:**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: Tarea que requiere root
      file:
        path: /etc/myconfig
        state: touch
```

### Problema 3: módulo no encontrado

**Problema:** errores de módulo no encontrado

**Solución:**
```bash
# Asegurarse de que la colección esté instalada
ansible-galaxy collection install community.general

# Verificar colección
ansible-galaxy collection list

# Usar FQCN (nombre de colección completo)
community.general.docker_container:
  name: mycontainer
```

### Problema 4: playbook lento

**Soluciones:**
1. Habilita pipelining (consulta la sección Rendimiento)
2. Usa el complemento de estrategia Mitogen
3. Deshabilita la recopilación de datos si no se necesita:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. Usa la ejecución asíncrona para tareas largas:
   ```yaml
   - name: tarea de larga duración
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Trayectoria profesional y certificaciones de Ansible

### Progresión de habilidades

**Principiante (0-6 meses):**
- Escribe playbooks básicos
- Comprende los inventarios y las variables
- Usa módulos comunes
- Ejecuta playbooks

**Intermedio (6-18 meses):**
- Crea roles reutilizables
- Implementa la gestión de errores
- Usa Ansible Vault
- Integra Ansible con CI/CD
- Administra varios entornos

**Avanzado (más de 18 meses):**
- Diseña marcos de automatización complejos
- Crea módulos y complementos personalizados
- Diseña implementaciones de Tower/AWX
- Optimiza el rendimiento
- Orienta a otras personas

### Certificaciones

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Demuestra dominio de Ansible
- Examen práctico basado en tareas
- Válido durante 3 años
- Reconocido en el sector

**Recursos de preparación:**
- Red Hat Learning Subscription
- Documentación de Ansible
- Laboratorios prácticos (A Cloud Guru, Udemy)
- Foros de la comunidad

### Mercado laboral (2026)

**Salarios promedio en EE. UU.:**
- Ingeniero junior de Ansible: $75,000-$95,000
- Ingeniero DevOps de nivel medio (Ansible): $110,000-$140,000
- Arquitecto sénior de automatización: $150,000-$190,000

**Habilidades solicitadas:**
- Ansible y Kubernetes
- Ansible y Terraform (IaC híbrida)
- Ansible y CI/CD (Jenkins, GitLab)
- Ansible y la nube (AWS, Azure, GCP)
- Administración de Ansible Tower/AWX

## Recursos de aprendizaje y comunidad

### Documentación oficial
- [Documentación de Ansible](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - plataforma para compartir roles
- [Ansible en GitHub](https://github.com/ansible/ansible)

### Cursos en línea
- Red Hat Learning Subscription
- Udemy: `Ansible para principiantes absolutos`
- A Cloud Guru: `Ansible práctico`
- Linux Academy: `Inicio rápido de Ansible`

### Libros
- `Ansible for DevOps`, de Jeff Geerling (actualizado en 2025)
- `Ansible: Up and Running`, de Lorin Hochstein
- `Mastering Ansible`, de James Freeman

### Comunidad
- [Lista de correo de Ansible](https://groups.google.com/forum/#!forum/ansible-project)
- [Ansible en Reddit](https://reddit.com/r/ansible)
- [Servidor de Ansible en Discord](https://discord.gg/ansible)
- Encuentros locales y virtuales de Ansible

### Plataformas de práctica
- [Escenarios de Ansible en Katacoda](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Laboratorio local con Vagrant o Docker

## Conclusión: comienza tu recorrido con Ansible

Ansible se ha convertido en la herramienta de automatización preferida por organizaciones de todo el mundo. En 2026 ofrece más capacidades, una administración de Windows más sencilla, mejores integraciones con la nube y generación de playbooks asistida por IA. Las habilidades que desarrolles te servirán durante tu carrera de TI, tanto si administras infraestructura tradicional como entornos en la nube o implementaciones híbridas.

**Puntos principales:**

1. **Empieza de forma sencilla**: crea playbooks básicos para administrar unos pocos servidores
2. **Practica con regularidad**: configura un laboratorio doméstico y experimenta
3. **Aprende haciendo**: automatiza tareas reales de tu trabajo diario
4. **Sigue buenas prácticas**: usa control de versiones, pruebas y documentación
5. **Únete a la comunidad**: aprende de otras personas y comparte tus conocimientos
6. **Mantente al día**: Ansible evoluciona rápido, así que sigue aprendiendo
7. **Combina herramientas**: Ansible, Terraform y Kubernetes permiten automatizar más tareas

**Próximos pasos:**

1. Instala Ansible en tu sistema
2. Crea un inventario sencillo de servidores de prueba, máquinas virtuales o contenedores
3. Escribe tu primer playbook, por ejemplo, para instalar un paquete
4. Añade complejidad de forma gradual con plantillas, variables y roles
5. Contribuye a los roles de la comunidad en Ansible Galaxy
6. Considera una certificación para validar tus habilidades

El recorrido de principiante a experto en Ansible es gratificante y abre oportunidades en DevOps, SRE e ingeniería de nube. Con los fundamentos de esta guía, ya puedes empezar a automatizar la infraestructura y desarrollar habilidades valiosas para el sector de TI moderno.

Te damos la bienvenida al mundo de la automatización de infraestructura con Ansible.

______

## Referencias

- [Documentación oficial de Ansible](https://docs.ansible.com/)
- [Ansible Galaxy - repositorio de roles](https://galaxy.ansible.com/)
- [Repositorio de Ansible en GitHub](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - Ansible Tower de código abierto](https://github.com/ansible/awx)
- [Buenas prácticas de Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Framework de pruebas Molecule](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Ansible for DevOps, de Jeff Geerling](https://www.ansiblefordevops.com/)
- [Índice de colecciones de Ansible](https://docs.ansible.com/ansible/latest/collections/index.html)
