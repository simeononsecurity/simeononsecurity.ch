---
title: "নতুনদের জন্য Ansible গাইড ২০২৬"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-08
description: "২০২৬ সালের Ansible গাইড। এতে ইনস্টলেশন, প্লেবুক, রোল, উদাহরণ, সেরা অনুশীলন এবং Terraform, Puppet ও Chef-এর সঙ্গে তুলনা রয়েছে।"
tags: ["Ansible পরিচিতি", "IT অবকাঠামো ব্যবস্থাপনা স্বয়ংক্রিয়করণ", "Ansible-এর মৌলিক বিষয়", "IT অবকাঠামো স্বয়ংক্রিয়করণ", "কনফিগারেশন ব্যবস্থাপনা", "অ্যাপ্লিকেশন স্থাপন", "প্রভিশনিং", "ধারাবাহিক ডেলিভারি", "নিরাপত্তা ও সম্মতি", "অর্কেস্ট্রেশন", "YAML", "Ansible মডিউল", "রোল", "সেরা অনুশীলন", "সংস্করণ নিয়ন্ত্রণ", "পরীক্ষা", "Red Hat", "সিস্টেম অ্যাডমিনিস্ট্রেটর", "Linux", "macOS", "Windows", "Ansible ইনস্টলেশন", "Ansible ইনভেন্টরি", "Ansible প্লেবুক", "Ansible মডিউল", "Ansible রোল", "Ansible-এর সেরা অনুশীলন", "Ansible পরীক্ষা", "IT অবকাঠামো স্বয়ংক্রিয়করণ টুল", "Ansible টিউটোরিয়াল", "অবকাঠামো ব্যবস্থাপনা স্বয়ংক্রিয়করণ", "নতুনদের জন্য Ansible", "Ansible শেখা", "Ansible টিউটোরিয়াল ২০২৬", "Ansible ও Terraform", "Ansible ও Puppet", "Ansible প্লেবুকের উদাহরণ", "Ansible স্বয়ংক্রিয়করণ", "DevOps টুল", "Infrastructure as Code", "Ansible AWX", "Ansible Tower", "Ansible কালেকশন", "Ansible Galaxy", "Ansible Vault", "Ansible ক্লাউড স্বয়ংক্রিয়করণ"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "আধুনিক IT অবকাঠামোর একটি চিত্র, যেখানে পরস্পর-সংযুক্ত সার্ভার ও ডিভাইস, SSH এবং WinRM সংযোগ, একটি নকশা করা YAML ফাইল এবং গাঢ় পটভূমিতে ক্লাউড পরিষেবার আইকন দেখা যায়।"
coverCaption: ""
---

**নতুনদের জন্য Ansible: ২০২৬ সালের IT স্বয়ংক্রিয়করণের পূর্ণাঙ্গ গাইড**

Ansible শিল্পের শীর্ষস্থানীয় স্বয়ংক্রিয়করণ প্ল্যাটফর্মে পরিণত হয়েছে। উৎস অনুযায়ী, Fortune 500 কোম্পানির ৮০ শতাংশেরও বেশি জটিল IT অবকাঠামো পরিচালনায় Ansible ব্যবহার করে। ২০২৬ সালেও এটি সহজ ব্যবহার ও এন্টারপ্রাইজ বৈশিষ্ট্যসহ একটি গুরুত্বপূর্ণ সমাধান।

এই পূর্ণাঙ্গ গাইডে আপনি প্রাথমিক ধারণা থেকে আত্মবিশ্বাসের সঙ্গে Ansible ব্যবহার করা পর্যন্ত শিখবেন। এতে মৌলিক ধারণা, উন্নত কৌশল, বাস্তব উদাহরণ এবং ২০২৬ সালের সেরা অনুশীলন রয়েছে।

## Ansible কী? মৌলিক ধারণা জানুন

**Ansible** একটি ওপেন-সোর্স স্বয়ংক্রিয়করণ প্ল্যাটফর্ম, যা এজেন্টবিহীন ঘোষণামূলক স্বয়ংক্রিয়করণের মাধ্যমে IT অবকাঠামো পরিচালনা সহজ করে। প্রচলিত কনফিগারেশন ব্যবস্থাপনা টুলের বিপরীতে, পরিচালিত নোডে এজেন্ট ইনস্টল করার দরকার হয় না। দূরবর্তী ব্যবস্থাপনার জন্য Linux ও Unix-এ SSH এবং Windows-এ WinRM ব্যবহার করে।

{{< youtube id="goclfp6a2IQ" >}}

### Ansible-এর প্রধান বৈশিষ্ট্য

**১. এজেন্টবিহীন স্থাপত্য:**
- পরিচালিত নোডে সফটওয়্যার ইনস্টল করার প্রয়োজন নেই
- বিদ্যমান SSH বা WinRM প্রোটোকল ব্যবহার করে
- আক্রমণের ক্ষেত্র ও রক্ষণাবেক্ষণের কাজ কমায়
- এজেন্টভিত্তিক টুলের চেয়ে শুরু করা সহজ

**২. ঘোষণামূলক ভাষা (YAML):**
- মানুষের পড়ার উপযোগী কনফিগারেশন ফাইল
- অবকাঠামোকে কাঙ্ক্ষিত অবস্থারূপে বর্ণনা করে
- ইডেম্পোটেন্ট কাজ, একাধিকবার চালানো নিরাপদ
- প্রোগ্রামিং অভিজ্ঞতা ছাড়াই বোঝা সহজ

**৩. পুশ মডেল:**
- কন্ট্রোল নোড পরিচালিত নোডে কনফিগারেশন পাঠায়
- এজেন্টের জন্য অপেক্ষা না করে সঙ্গে সঙ্গে কাজ চালায়
- কেন্দ্রীভূত নিয়ন্ত্রণ ও দৃশ্যমানতা
- প্রয়োজনমতো স্বয়ংক্রিয়করণের জন্য উপযোগী

**৪. বিস্তৃত মডিউল লাইব্রেরি:**
- ৫,০০০-এর বেশি বিল্ট-ইন মডিউল (২০২৬ সালের হিসাবে)
- Linux, Windows, নেটওয়ার্ক ডিভাইস ও ক্লাউড প্ল্যাটফর্ম সমর্থন করে
- কমিউনিটি ও বিক্রেতাদের তৈরি মডিউল
- Python-এ কাস্টম মডিউল লেখা সহজ

### Ansible দিয়ে কী স্বয়ংক্রিয় করা যায়?

Ansible দিয়ে এই কাজগুলো স্বয়ংক্রিয় করা যায়:

- **কনফিগারেশন ব্যবস্থাপনা**: সার্ভারের কনফিগারেশন একরকম রাখা
- **অ্যাপ্লিকেশন স্থাপন**: বিভিন্ন পরিবেশে অ্যাপ্লিকেশন স্থাপন
- **প্রভিশনিং**: অবকাঠামো তৈরি ও কনফিগার করা
- **ধারাবাহিক ডেলিভারি**: CI/CD পাইপলাইনের সঙ্গে যুক্ত করা
- **নিরাপত্তা ও সম্মতি**: নিরাপত্তা নীতি ও সম্মতির শর্ত কার্যকর করা
- **অর্কেস্ট্রেশন**: জটিল বহুস্তরীয় স্থাপন সমন্বয় করা
- **ক্লাউড স্বয়ংক্রিয়করণ**: AWS, Azure, GCP ও অন্যান্য ক্লাউড পরিচালনা
- **নেটওয়ার্ক স্বয়ংক্রিয়করণ**: সুইচ, রাউটার ও ফায়ারওয়াল কনফিগার করা
- **Windows স্বয়ংক্রিয়করণ**: Windows সার্ভার ও ওয়ার্কস্টেশন পরিচালনা

### Ansible-এর বিবর্তন: ২০১২ থেকে ২০২৬

**সময়রেখা:**
- **২০১২**: Michael DeHaan Ansible তৈরি করেন
- **২০১৫**: Red Hat Ansible অধিগ্রহণ করে
- **২০১৯**: Ansible Engine 2.8 কালেকশন চালু করে
- **২০২০**: Ansible 2.10+ ansible-core ও কালেকশনে বিভক্ত হয়
- **২০২৩**: Ansible 8.x ক্লাউড সংযোগ বাড়ায়
- **২০২৬**: Ansible 10.x-এ AI-সহায়তায় প্লেবুক তৈরি, উন্নত Windows সমর্থন এবং বিস্তৃত নিরাপত্তা বৈশিষ্ট্য যুক্ত হয়

## প্রতিযোগী টুলের সঙ্গে Ansible-এর সংক্ষিপ্ত তুলনা

| বৈশিষ্ট্য | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **ধরন** | কনফিগারেশন ব্যবস্থাপনা | অবকাঠামো প্রভিশনিং | কনফিগারেশন ব্যবস্থাপনা | কনফিগারেশন ব্যবস্থাপনা |
| **ভাষা** | YAML | HCL | Puppet DSL (Ruby-এর মতো) | Ruby DSL |
| **এজেন্ট প্রয়োজন** | না | না | হ্যাঁ | হ্যাঁ |
| **শেখার কঠিনতা** | সহজ | মাঝারি | কঠিন | কঠিন |
| **উপযোগী ক্ষেত্র** | কনফিগারেশন ব্যবস্থাপনা, স্থাপন | ক্লাউড অবকাঠামো | বড় প্রতিষ্ঠান | জটিল কর্মপ্রবাহ |
| **অবস্থা ব্যবস্থাপনা** | পুশ মডেল | ঘোষণামূলক অবস্থা ফাইল | পুল মডেল | পুল মডেল |
| **Windows সমর্থন** | চমৎকার (২০২৬) | সীমিত | ভালো | ভালো |
| **কমিউনিটির আকার** | খুব বড় | খুব বড় | বড় | মাঝারি |
| **প্রধান ব্যবহার** | দৈনন্দিন পরিচালনা | অবকাঠামো প্রভিশনিং | এন্টারপ্রাইজ কনফিগারেশন | অ্যাপ্লিকেশন স্থাপন |

**কখন Ansible বেছে নেবেন:**
- ✅ হাইব্রিড পরিবেশে কনফিগারেশন পরিচালনা
- ✅ অ্যাপ্লিকেশন স্থাপন স্বয়ংক্রিয় করা
- ✅ দ্রুত শেখা জরুরি
- ✅ এজেন্টবিহীন স্থাপত্য পছন্দ
- ✅ উন্নত Windows স্বয়ংক্রিয়করণ দরকার (২০২৬ সালের উন্নতি)
- ✅ আগে থেকেই SSH অবকাঠামো আছে

**কখন বিকল্প বিবেচনা করবেন:**
- Terraform: মূলত অবকাঠামো প্রভিশনিংয়ের জন্য (AWS, Azure, GCP)
- Puppet: হাজারো নোডসহ বড় প্রতিষ্ঠানের জন্য
- Chef: অ্যাপ্লিকেশনকেন্দ্রিক জটিল কর্মপ্রবাহের জন্য

## শুরু করুন: ২০২৬ সালে Ansible ইনস্টল করা

### সিস্টেমের প্রয়োজনীয়তা

**কন্ট্রোল নোড, যেখানে Ansible চলে:**
- Linux, macOS বা Windows-এ WSL2
- Python 3.9 বা পরবর্তী সংস্করণ (২০২৬ সালের জন্য Python 3.11+ সুপারিশকৃত)
- ন্যূনতম 2 GB RAM, 4 GB বা বেশি সুপারিশকৃত
- কালেকশনের জন্য 5 GB ডিস্ক স্থান

**পরিচালিত নোড:**
- SSH অ্যাক্সেস (Linux/Unix) অথবা WinRM (Windows)
- Python 2.7 অথবা Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- এজেন্ট ইনস্টল করার প্রয়োজন নেই

### ইনস্টলেশনের পদ্ধতি

#### পদ্ধতি ১: প্যাকেজ ম্যানেজার (নতুনদের জন্য সুপারিশকৃত)

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

#### পদ্ধতি ২: Python pip (নতুন বৈশিষ্ট্য)

```bash
# Install pipx (recommended isolated environment)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install Ansible using pipx
pipx install --include-deps ansible

# Verify installation
ansible --version
```

#### পদ্ধতি ৩: Docker (বহনযোগ্য)

```bash
# Pull official Ansible container
docker pull quay.io/ansible/ansible:latest

# Run Ansible in container
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### ইনস্টলেশন যাচাই

```bash
# Check Ansible version
ansible --version

# Expected output (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### প্রাথমিক কনফিগারেশন

Ansible কনফিগারেশন ফাইল তৈরি করুন:

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

## মৌলিক ধারণা: Ansible-এর উপাদান

### ১. ইনভেন্টরি: অবকাঠামো নির্ধারণ

**ইনভেন্টরি** Ansible-এর পরিচালিত হোস্ট ও গ্রুপ নির্ধারণ করে। এটি স্থির (INI বা YAML ফাইল) অথবা গতিশীল (স্ক্রিপ্ট বা প্লাগইন) হতে পারে।

#### স্থির ইনভেন্টরি (INI ফরম্যাট)

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

#### স্থির ইনভেন্টরি (YAML ফরম্যাট, ২০২৬ সালে সুপারিশকৃত)

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

#### গতিশীল ইনভেন্টরি (ক্লাউড প্রদানকারী)

ক্লাউড পরিবেশে গতিশীল ইনভেন্টরি প্লাগইন ব্যবহার করুন:

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

### ২. প্লেবুক: স্বয়ংক্রিয়করণের নকশা

**প্লেবুক** হলো YAML ফাইল, যা স্বয়ংক্রিয়করণের কর্মপ্রবাহ বর্ণনা করে এবং অবকাঠামোর কাঙ্ক্ষিত অবস্থা নির্ধারণ করে।

#### সহজ প্লেবুকের উদাহরণ

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

#### প্লেবুক চালানো

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

### ৩. মডিউল: পুনর্ব্যবহারযোগ্য কাজের একক

Ansible মডিউল স্বয়ংক্রিয়করণের মৌলিক উপাদান। প্রতিটি মডিউল নির্দিষ্ট কাজ করে।

#### প্রচলিত মডিউল (২০২৬)

**সিস্টেম মডিউল:**
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

**ফাইল মডিউল:**
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

**ক্লাউড মডিউল (AWS উদাহরণ):**
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

**ডেটাবেস মডিউল:**
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

### ৪. ভেরিয়েবল: প্লেবুক নমনীয় করা

ভেরিয়েবল আপনাকে বিভিন্ন পরিবেশে প্লেবুক পুনর্ব্যবহার করতে দেয়।

#### ভেরিয়েবলের অগ্রাধিকার (উচ্চ থেকে নিম্ন)

1. অতিরিক্ত ভেরিয়েবল (কমান্ড লাইনে `-e`)
2. টাস্ক ভেরিয়েবল
3. ব্লক ভেরিয়েবল
4. রোল ও include ভেরিয়েবল
5. প্লে ভেরিয়েবল
6. হোস্ট ফ্যাক্ট
7. প্লেবুকের `host_vars`
8. প্লেবুকের `group_vars`
9. ইনভেন্টরির `host_vars`
10. ইনভেন্টরির `group_vars`
11. রোলের ডিফল্ট মান

#### ভেরিয়েবলের উদাহরণ

**প্লেবুক ভেরিয়েবল:**
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

**group_vars (পরিবেশভিত্তিক):**
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

**Ansible Vault (এনক্রিপ্ট করা ভেরিয়েবল):**
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

### ৫. রোল: জটিল স্বয়ংক্রিয়করণ সাজানো

**রোল** প্লেবুক সাজানোর কাঠামোবদ্ধ উপায় দেয়, ফলে সেগুলো মডিউলার ও পুনর্ব্যবহারযোগ্য হয়।

#### রোলের পূর্ণ কাঠামো

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

#### রোলের উদাহরণ: nginx

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

**রোল ব্যবহার:**
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

## Ansible-এর উন্নত ধারণা (২০২৬)

### Ansible কালেকশন

**কালেকশন** হলো মডিউল, রোল ও প্লাগইনের মতো Ansible বিষয়বস্তু বিতরণের ফরম্যাট।

#### কালেকশন ইনস্টল

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

#### কালেকশন মডিউল ব্যবহার

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

### Ansible Tower / AWX (এন্টারপ্রাইজ বৈশিষ্ট্য)

**Ansible Tower** (বাণিজ্যিক) এবং **AWX** (ওপেন সোর্স) দেয়:

- প্লেবুক চালানোর ওয়েব ইন্টারফেস
- রোলভিত্তিক অ্যাক্সেস নিয়ন্ত্রণ (RBAC)
- কাজের সময়সূচি ও কর্মপ্রবাহ
- কেন্দ্রীভূত লগিং ও অডিট
- ইন্টিগ্রেশনের জন্য REST API
- ক্রেডেনশিয়াল ব্যবস্থাপনা
- ইনভেন্টরি সিঙ্ক্রোনাইজেশন

**Docker Compose দিয়ে AWX ইনস্টল:**
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

### Ansible দিয়ে Windows স্বয়ংক্রিয়করণ

২০২৬ সালে Ansible-এর Windows সমর্থন অনেক উন্নত হয়েছে:

**Windows-এর পূর্বশর্ত:**
```powershell
# On Windows host, enable WinRM
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**Windows ইনভেন্টরি:**
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

**Windows স্বয়ংক্রিয়করণ প্লেবুক:**
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

### Ansible দিয়ে নেটওয়ার্ক স্বয়ংক্রিয়করণ

Ansible Cisco, Juniper, Arista ও F5-সহ প্রধান নেটওয়ার্ক সরবরাহকারীদের সমর্থন করে।

**নেটওয়ার্ক ডিভাইসের প্লেবুক:**
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

## বাস্তব ব্যবহার ও উদাহরণ

### ব্যবহার ১: সম্পূর্ণ ওয়েব অ্যাপ্লিকেশন স্থাপন

**প্রকল্পের কাঠামো:**
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

**site.yml (সম্পূর্ণ স্ট্যাক স্থাপন):**
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

### ব্যবহার ২: Kubernetes ক্লাস্টার সেটআপ

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

### ব্যবহার ৩: নিরাপত্তা শক্তিশালীকরণ স্বয়ংক্রিয় করা

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

## Ansible-এর সেরা অনুশীলন (২০২৬ সংস্করণ)

### ১. সংস্করণ নিয়ন্ত্রণ (Git) ব্যবহার করুন

**রিপোজিটরির কাঠামো:**
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

### ২. ইডেম্পোটেন্সি বাস্তবায়ন করুন

**ভুল (ইডেম্পোটেন্ট নয়):**
```yaml
- name: Add line to file
  shell: echo "new line" >> /etc/myconfig
```

**সঠিক (ইডেম্পোটেন্ট):**
```yaml
- name: Ensure line in file
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### ৩. কোডের গুণমানের জন্য Ansible Lint ব্যবহার করুন

```bash
# Install ansible-lint
pip install ansible-lint

# Run linter
ansible-lint playbook.yml

# Fix common issues automatically
ansible-lint --fix playbook.yml
```

### ৪. Molecule দিয়ে পরীক্ষা করুন

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

**molecule.yml উদাহরণ:**
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

### ৫. নির্দিষ্ট কাজ চালাতে ট্যাগ ব্যবহার করুন

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

### ৬. ত্রুটি সামলানো ও ডিবাগ করা

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

### ৭. কর্মদক্ষতা উন্নত করা

#### Pipelining সক্রিয় করুন
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### Mitogen ব্যবহার করুন (৩-৭ গুণ দ্রুত)
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

#### সমান্তরালভাবে চালানো
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

## সাধারণ সমস্যা সমাধান

### সমস্যা ১: SSH সংযোগ ব্যর্থ

**সমস্যা:** পরিচালিত হোস্টে সংযোগ করা যাচ্ছে না

**সমাধান:**
```bash
# Test raw SSH connection
ssh -vvv user@host

# Test Ansible connection
ansible host -m ping -vvv

# Add to inventory
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### সমস্যা ২: অনুমতি প্রত্যাখ্যাত (sudo)

**সমস্যা:** অনুমতি-সংক্রান্ত ত্রুটিতে কাজ ব্যর্থ হয়

**সমাধান:**
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

### সমস্যা ৩: মডিউল পাওয়া যায়নি

**সমস্যা:** মডিউল না পাওয়ার ত্রুটি

**সমাধান:**
```bash
# Ensure collection is installed
ansible-galaxy collection install community.general

# Verify collection
ansible-galaxy collection list

# Use FQCN (Fully Qualified Collection Name)
community.general.docker_container:
  name: mycontainer
```

### সমস্যা ৪: প্লেবুক ধীরে চলে

**সমাধান:**
1. Pipelining সক্রিয় করুন (কর্মদক্ষতা অংশ দেখুন)
2. Mitogen কৌশল প্লাগইন ব্যবহার করুন
3. প্রয়োজন না হলে ফ্যাক্ট সংগ্রহ বন্ধ করুন:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. দীর্ঘ সময় চলা কাজের জন্য অ্যাসিঙ্ক্রোনাস রান ব্যবহার করুন:
   ```yaml
   - name: Long running task
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## Ansible পেশা ও সার্টিফিকেশন

### দক্ষতার অগ্রগতি

**শুরুর স্তর (০-৬ মাস):**
- সাধারণ প্লেবুক লিখুন
- ইনভেন্টরি ও ভেরিয়েবল বুঝুন
- প্রচলিত মডিউল ব্যবহার করুন
- প্লেবুক চালান

**মধ্যবর্তী স্তর (৬-১৮ মাস):**
- পুনর্ব্যবহারযোগ্য রোল তৈরি করুন
- ত্রুটি ব্যবস্থাপনা বাস্তবায়ন করুন
- Ansible Vault ব্যবহার করুন
- CI/CD-এর সঙ্গে যুক্ত করুন
- একাধিক পরিবেশ পরিচালনা করুন

**উন্নত স্তর (১৮ মাসের বেশি):**
- জটিল স্বয়ংক্রিয়করণ কাঠামো নকশা করুন
- কাস্টম মডিউল ও প্লাগইন তৈরি করুন
- Tower/AWX স্থাপনার নকশা করুন
- কর্মদক্ষতা উন্নত করুন
- অন্যদের পরামর্শ দিন

### সার্টিফিকেশন

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- Ansible দক্ষতার প্রমাণ দেয়
- কাজভিত্তিক ব্যবহারিক পরীক্ষা
- ৩ বছর বৈধ
- শিল্পে স্বীকৃত

**প্রস্তুতির উপকরণ:**
- Red Hat Learning Subscription
- Ansible ডকুমেন্টেশন
- অনুশীলনের ল্যাব (A Cloud Guru, Udemy)
- কমিউনিটি ফোরাম

### চাকরির বাজার (২০২৬)

**যুক্তরাষ্ট্রে গড় বেতন:**
- জুনিয়র Ansible ইঞ্জিনিয়ার: $75,000-$95,000
- মধ্য-স্তরের DevOps ইঞ্জিনিয়ার (Ansible): $110,000-$140,000
- সিনিয়র স্বয়ংক্রিয়করণ আর্কিটেক্ট: $150,000-$190,000

**চাহিদাসম্পন্ন দক্ষতা:**
- Ansible ও Kubernetes
- Ansible ও Terraform (হাইব্রিড IaC)
- Ansible ও CI/CD (Jenkins, GitLab)
- Ansible ও ক্লাউড (AWS, Azure, GCP)
- Ansible Tower/AWX প্রশাসন

## শেখার উপকরণ ও কমিউনিটি

### সরকারি ডকুমেন্টেশন
- [Ansible ডকুমেন্টেশন](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - রোল ভাগ করার প্ল্যাটফর্ম
- [GitHub-এ Ansible](https://github.com/ansible/ansible)

### অনলাইন কোর্স
- Red Hat Learning Subscription
- Udemy: `একেবারে নতুনদের জন্য Ansible`
- A Cloud Guru: `হাতে-কলমে Ansible`
- Linux Academy: `Ansible দ্রুত শুরু`

### বই
- Jeff Geerling-এর `Ansible for DevOps` (২০২৫ সালে হালনাগাদ)
- Lorin Hochstein-এর `Ansible: Up and Running`
- James Freeman-এর `Mastering Ansible`

### কমিউনিটি
- [Ansible মেইলিং তালিকা](https://groups.google.com/forum/#!forum/ansible-project)
- [Reddit-এ Ansible](https://reddit.com/r/ansible)
- [Ansible Discord সার্ভার](https://discord.gg/ansible)
- স্থানীয় ও অনলাইন Ansible মিটআপ

### অনুশীলনের প্ল্যাটফর্ম
- [Katacoda Ansible পরিস্থিতি](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- Vagrant বা Docker দিয়ে স্থানীয় ল্যাব

## উপসংহার: Ansible দিয়ে শুরু করুন

বিশ্বজুড়ে প্রতিষ্ঠানগুলোর পছন্দের স্বয়ংক্রিয়করণ টুলে Ansible পরিণত হয়েছে। ২০২৬ সালে এতে আরও সক্ষমতা, সহজ Windows ব্যবস্থাপনা, উন্নত ক্লাউড সংযোগ এবং AI-সহায়তায় প্লেবুক তৈরি রয়েছে। প্রচলিত অবকাঠামো, ক্লাউড পরিবেশ বা হাইব্রিড স্থাপন পরিচালনা করুন, Ansible-এর দক্ষতা আপনার IT কর্মজীবনে কাজে লাগবে।

**মূল বিষয়গুলো:**

1. **সহজভাবে শুরু করুন**: কয়েকটি সার্ভার পরিচালনার জন্য সাধারণ প্লেবুক তৈরি করুন
2. **নিয়মিত অনুশীলন করুন**: বাড়িতে ল্যাব তৈরি করে পরীক্ষা করুন
3. **কাজ করে শিখুন**: দৈনন্দিন কাজের বাস্তব কাজগুলো স্বয়ংক্রিয় করুন
4. **সেরা অনুশীলন অনুসরণ করুন**: সংস্করণ নিয়ন্ত্রণ, পরীক্ষা ও ডকুমেন্টেশন ব্যবহার করুন
5. **কমিউনিটিতে যোগ দিন**: অন্যদের কাছ থেকে শিখুন এবং জ্ঞান ভাগ করুন
6. **হালনাগাদ থাকুন**: Ansible দ্রুত বদলায়, শেখা চালিয়ে যান
7. **টুল একসঙ্গে ব্যবহার করুন**: Ansible, Terraform ও Kubernetes বিস্তৃত স্বয়ংক্রিয়করণে সহায়তা করে

**পরবর্তী ধাপ:**

1. আপনার সিস্টেমে Ansible ইনস্টল করুন
2. পরীক্ষার সার্ভার, ভার্চুয়াল মেশিন বা কন্টেইনারের সাধারণ ইনভেন্টরি তৈরি করুন
3. প্যাকেজ ইনস্টল করার জন্য প্রথম প্লেবুক লিখুন
4. টেমপ্লেট, ভেরিয়েবল ও রোল যোগ করে ধীরে ধীরে জটিলতা বাড়ান
5. Ansible Galaxy-তে কমিউনিটি রোলে অবদান রাখুন
6. দক্ষতা যাচাইয়ের জন্য সার্টিফিকেশনের কথা ভাবুন

Ansible-এ নতুন ব্যবহারকারী থেকে বিশেষজ্ঞ হওয়ার পথটি সন্তোষজনক এবং DevOps, SRE ও ক্লাউড ইঞ্জিনিয়ারিংয়ের সুযোগ দেয়। এই গাইডের ভিত্তি কাজে লাগিয়ে আপনি অবকাঠামো স্বয়ংক্রিয় করতে এবং আধুনিক IT খাতের জন্য মূল্যবান দক্ষতা তৈরি করতে পারবেন।

Ansible দিয়ে অবকাঠামো স্বয়ংক্রিয়করণের জগতে স্বাগতম!

______

## তথ্যসূত্র

- [Ansible-এর সরকারি ডকুমেন্টেশন](https://docs.ansible.com/)
- [Ansible Galaxy - রোল রিপোজিটরি](https://galaxy.ansible.com/)
- [GitHub-এ Ansible রিপোজিটরি](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - ওপেন-সোর্স Ansible Tower](https://github.com/ansible/awx)
- [Ansible-এর সেরা অনুশীলন](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Molecule পরীক্ষা কাঠামো](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- Jeff Geerling-এর [Ansible for DevOps](https://www.ansiblefordevops.com/)
- [Ansible কালেকশন সূচি](https://docs.ansible.com/ansible/latest/collections/index.html)
