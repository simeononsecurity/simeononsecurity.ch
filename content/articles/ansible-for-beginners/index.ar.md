---
title: "دليل Ansible للمبتدئين 2026"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-13
description: "دليل Ansible لعام 2026، ويغطي التثبيت وملفات Playbook والأدوار والأمثلة وأفضل الممارسات ومقارنات Terraform وPuppet وChef."
tags: ["مقدمة إلى Ansible", "أتمتة إدارة بنية تقنية المعلومات", "أساسيات Ansible", "أتمتة بنية تقنية المعلومات", "إدارة الإعدادات", "نشر التطبيقات", "تجهيز البنية التحتية", "التسليم المستمر", "الأمان والامتثال", "التنسيق", "YAML", "وحدات Ansible", "الأدوار", "أفضل الممارسات", "التحكم في الإصدارات", "الاختبار", "Red Hat", "مسؤولو الأنظمة", "Linux", "macOS", "Windows", "تثبيت Ansible", "جرد Ansible", "ملفات Playbook في Ansible", "وحدات Ansible", "أدوار Ansible", "أفضل ممارسات Ansible", "اختبار Ansible", "أداة أتمتة بنية تقنية المعلومات", "شرح Ansible", "أتمتة إدارة البنية التحتية", "Ansible للمبتدئين", "تعلم Ansible", "شرح Ansible لعام 2026", "Ansible مقارنة بـ Terraform", "Ansible مقارنة بـ Puppet", "أمثلة على ملفات Playbook في Ansible", "أتمتة Ansible", "أدوات DevOps", "البنية التحتية كرمز", "Ansible AWX", "Ansible Tower", "مجموعات Ansible", "Ansible Galaxy", "Ansible Vault", "أتمتة السحابة باستخدام Ansible"]
cover: "/img/cover/ansible-for-beginners.webp"
coverAlt: "رسم توضيحي لبنية تقنية معلومات حديثة تضم خوادم وأجهزة مترابطة. يعرض اتصالات SSH وWinRM وملف YAML منمقًا وأيقونات لخدمات سحابية على خلفية داكنة."
coverCaption: ""
---

**Ansible للمبتدئين: دليل شامل لأتمتة تقنية المعلومات في 2026**

أصبحت Ansible منصة رائدة في مجال الأتمتة. ووفقًا للمصدر، تعتمد أكثر من 80% من شركات Fortune 500 عليها لإدارة بنى تقنية المعلومات المعقدة. وفي 2026، تظل Ansible حلًا مهمًا يجمع بين سهولة الاستخدام وميزات المؤسسات.

ينقلك هذا الدليل من المفاهيم الأساسية إلى استخدام Ansible بثقة. ويغطي الأساسيات والتقنيات المتقدمة والأمثلة العملية وأفضل الممارسات لعام 2026.

## ما Ansible؟ فهم الأساسيات

**Ansible** منصة أتمتة مفتوحة المصدر تبسّط إدارة بنية تقنية المعلومات من خلال أتمتة تعريفية بلا وكلاء. وعلى خلاف أدوات إدارة الإعدادات التقليدية، لا تتطلب تثبيت وكلاء على العقد المُدارة. وتستخدم SSH لإدارة أنظمة Linux وUnix عن بُعد، أو WinRM لإدارة Windows.

{{< youtube id="goclfp6a2IQ" >}}

### أبرز خصائص Ansible

**1. بنية بلا وكلاء:**
- لا تحتاج إلى تثبيت برامج على العقد المُدارة
- تستخدم بروتوكولات SSH أو WinRM الموجودة
- تقلل مساحة الهجوم وعبء الصيانة
- البدء بها أسهل من الأدوات التي تتطلب وكلاء

**2. لغة تعريفية (YAML):**
- ملفات إعدادات سهلة القراءة
- وصف البنية التحتية بالحالة المطلوبة
- عمليات تكرارية آمنة عند تشغيلها عدة مرات
- سهلة الفهم دون خبرة في البرمجة

**3. نموذج الدفع:**
- ترسل عقدة التحكم الإعدادات إلى العقد المُدارة
- تنفذ المهام فورًا دون انتظار الوكلاء
- تحكم ورؤية مركزيان
- مناسبة للأتمتة عند الطلب

**4. مكتبة واسعة من الوحدات:**
- أكثر من 5,000 وحدة مدمجة (حتى 2026)
- تدعم Linux وWindows وأجهزة الشبكات والمنصات السحابية
- وحدات من المجتمع والمورّدين
- إنشاء وحدات مخصصة بلغة Python أمر سهل

### ما الذي يمكن أتمتته باستخدام Ansible؟

تدعم Ansible أتمتة المجالات التالية:

- **إدارة الإعدادات**: الحفاظ على اتساق إعدادات الخوادم
- **نشر التطبيقات**: نشر التطبيقات عبر بيئات مختلفة
- **تجهيز البنية التحتية**: إنشاء البنية التحتية وإعدادها
- **التسليم المستمر**: التكامل مع مسارات CI/CD
- **الأمان والامتثال**: تطبيق سياسات الأمان والامتثال
- **التنسيق**: تنسيق عمليات النشر المعقدة متعددة الطبقات
- **أتمتة السحابة**: إدارة AWS وAzure وGCP وغيرها من الخدمات السحابية
- **أتمتة الشبكات**: إعداد المحولات والموجّهات والجدران النارية
- **أتمتة Windows**: إدارة خوادم ومحطات عمل Windows

### تطور Ansible من 2012 إلى 2026

**الجدول الزمني:**
- **2012**: أنشأ Michael DeHaan مشروع Ansible
- **2015**: استحوذت Red Hat على Ansible
- **2019**: قدم Ansible Engine 2.8 المجموعات
- **2020**: انقسم Ansible 2.10+ إلى ansible-core ومجموعات
- **2023**: وسّع Ansible 8.x تكاملات الخدمات السحابية
- **2026**: أضاف Ansible 10.x إنشاء ملفات Playbook بمساعدة الذكاء الاصطناعي ودعمًا أفضل لـ Windows وميزات أمان موسعة

## مقارنة سريعة بين Ansible والبدائل

| الميزة | Ansible | Terraform | Puppet | Chef |
|---------|---------|-----------|--------|------|
| **النوع** | إدارة الإعدادات | تجهيز البنية التحتية | إدارة الإعدادات | إدارة الإعدادات |
| **اللغة** | YAML | HCL | Puppet DSL (تشبه Ruby) | Ruby DSL |
| **هل يلزم وكيل؟** | لا | لا | نعم | نعم |
| **سهولة التعلم** | سهلة | متوسطة | صعبة | صعبة |
| **الأفضل لـ** | إدارة الإعدادات والنشر | البنية التحتية السحابية | المؤسسات الكبيرة | مسارات العمل المعقدة |
| **إدارة الحالة** | نموذج الدفع | ملف حالة تعريفي | نموذج السحب | نموذج السحب |
| **دعم Windows** | ممتاز (2026) | محدود | جيد | جيد |
| **حجم المجتمع** | كبير جدًا | كبير جدًا | كبير | متوسط |
| **الاستخدام الرئيسي** | العمليات اليومية | تجهيز البنية التحتية | إعدادات المؤسسات | نشر التطبيقات |

**متى تختار Ansible:**
- ✅ إدارة الإعدادات في البيئات الهجينة
- ✅ أتمتة نشر التطبيقات
- ✅ الحاجة إلى سهولة وسرعة التعلم
- ✅ تفضيل بنية بلا وكلاء
- ✅ الحاجة إلى أتمتة Windows متقدمة (تحسينات 2026)
- ✅ وجود بنية SSH مسبقًا

**متى تفكر في البدائل:**
- Terraform: لتجهيز البنية التحتية أساسًا (AWS وAzure وGCP)
- Puppet: للمؤسسات الكبيرة التي تضم آلاف العقد
- Chef: لمسارات العمل المعقدة التي تركز على التطبيقات

## بدء الاستخدام: تثبيت Ansible في 2026

### متطلبات النظام

**عقدة التحكم التي تشغّل Ansible:**
- Linux أو macOS أو WSL2 على Windows
- Python 3.9 أو أحدث (يوصى بـ Python 3.11+ لعام 2026)
- ذاكرة RAM بسعة 2 GB على الأقل، ويوصى بـ 4 GB أو أكثر
- مساحة قرص 5 GB للمجموعات

**العقد المُدارة:**
- الوصول عبر SSH (Linux/Unix) أو WinRM (Windows)
- Python 2.7 أو Python 3.6+ (Linux)
- PowerShell 5.1+ (Windows)
- لا تتطلب تثبيت وكيل

### طرق التثبيت

#### الطريقة 1: مدير الحزم (موصى بها للمبتدئين)

**Ubuntu/Debian:**
```bash
# إضافة مستودع Ansible PPA لأحدث إصدار
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible -y
```

**RHEL/CentOS/Rocky Linux:**
```bash
# تمكين مستودع EPEL
sudo dnf install epel-release -y
sudo dnf install ansible -y
```

**macOS:**
```bash
# استخدام Homebrew
brew install ansible
```

#### الطريقة 2: Python pip (أحدث الميزات)

```bash
# تثبيت pipx (بيئة معزولة موصى بها)
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# تثبيت Ansible باستخدام pipx
pipx install --include-deps ansible

# التحقق من التثبيت
ansible --version
```

#### الطريقة 3: Docker (قابل للنقل)

```bash
# سحب حاوية Ansible الرسمية
docker pull quay.io/ansible/ansible:latest

# تشغيل Ansible داخل حاوية
docker run --rm -it quay.io/ansible/ansible:latest ansible --version
```

### التحقق من التثبيت

```bash
# التحقق من إصدار Ansible
ansible --version

# المخرجات المتوقعة (2026):
# ansible [core 2.16.5]
#   config file = /etc/ansible/ansible.cfg
#   python version = 3.11.8
#   jinja version = 3.1.3
```

### الإعداد الأولي

أنشئ ملف إعداد Ansible:

```bash
# إنشاء مجلد الإعدادات
mkdir -p ~/.ansible

# إنشاء ansible.cfg
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

## المفاهيم الأساسية: مكونات Ansible

### 1. الجرد: تعريف بنيتك التحتية

يحدد **الجرد** المضيفين والمجموعات التي تديرها Ansible. ويمكن أن يكون ثابتًا (ملف INI أو YAML) أو ديناميكيًا (برامج نصية أو مكونات إضافية).

#### الجرد الثابت (تنسيق INI)

```ini
# inventory/hosts.ini

# مجموعة خوادم الويب
[webservers]
web1.example.com
web2.example.com
web3.example.com

# مجموعة خوادم قواعد البيانات
[databases]
db1.example.com ansible_host=192.168.1.100
db2.example.com ansible_host=192.168.1.101

# موازنات التحميل
[loadbalancers]
lb1.example.com

# مجموعة من المجموعات
[production:children]
webservers
databases
loadbalancers

# المتغيرات لجميع خوادم الويب
[webservers:vars]
ansible_user=deploy
ansible_port=22
http_port=80
https_port=443

# المتغيرات لجميع المضيفين
[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

#### الجرد الثابت (تنسيق YAML، موصى به في 2026)

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

#### الجرد الديناميكي (موفرو الخدمات السحابية)

استخدم مكونات الجرد الديناميكي الإضافية للبيئات السحابية:

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

### 2. ملفات Playbook: مخططات الأتمتة

**ملفات Playbook** هي ملفات YAML تصف مسارات عمل الأتمتة وتحدد الحالة المطلوبة للبنية التحتية.

#### مثال بسيط على Playbook

```yaml
# simple_playbook.yml
---
- name: إعداد خوادم الويب
  hosts: webservers
  become: yes
  
  tasks:
    - name: تثبيت Nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: تشغيل Nginx وتمكينه
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: نسخ محتوى الموقع
      copy:
        src: ./website/
        dest: /var/www/html/
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: إعداد جدار الحماية
      ufw:
        rule: allow
        port: '{{ item }}'
        proto: tcp
      loop:
        - 80
        - 443
```

#### تشغيل ملفات Playbook

```bash
# التنفيذ الأساسي
ansible-playbook simple_playbook.yml

# باستخدام مخزون محدد
ansible-playbook -i inventory/hosts.yml simple_playbook.yml

# تقييد التشغيل على مضيفين محددين
ansible-playbook simple_playbook.yml --limit web1.example.com

# تشغيل تجريبي (وضع الفحص)
ansible-playbook simple_playbook.yml --check

# مخرجات تفصيلية لاستكشاف الأخطاء
ansible-playbook simple_playbook.yml -vvv
```

### 3. الوحدات: وحدات مهام قابلة لإعادة الاستخدام

وحدات Ansible هي مكونات الأتمتة الأساسية. تنفذ كل وحدة مهمة محددة.

#### الوحدات الشائعة (2026)

**وحدات النظام:**
```yaml
# إدارة الحزم
- name: تثبيت الحزم (apt)
  apt:
    name:
      - nginx
      - git
      - python3-pip
    state: present

# إدارة الخدمات
- name: إدارة الخدمات
  systemd:
    name: nginx
    state: started
    enabled: yes
```

**وحدات الملفات:**
```yaml
# عمليات الملفات
- name: إنشاء مجلد
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    mode: '0755'

# نسخ الملفات
- name: نشر الإعدادات
  copy:
    src: config.yml
    dest: /etc/myapp/config.yml
    backup: yes

# قالب مع متغيرات
- name: نشر إعدادات nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

**الوحدات السحابية (مثال AWS):**
```yaml
# إنشاء مثيل EC2
- name: إنشاء مثيل EC2
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

# إنشاء حاوية S3
- name: إنشاء حاوية S3
  amazon.aws.s3_bucket:
    name: my-app-bucket
    region: us-east-1
    versioning: yes
    encryption: AES256
```

**وحدات قواعد البيانات:**
```yaml
# إدارة قاعدة بيانات MySQL
- name: إنشاء قاعدة بيانات MySQL
  mysql_db:
    name: webapp_db
    state: present
    login_user: root
    login_password: "{{ mysql_root_password }}"

- name: إنشاء مستخدم MySQL
  mysql_user:
    name: webapp_user
    password: "{{ db_password }}"
    priv: 'webapp_db.*:ALL'
    state: present
```

### 4. المتغيرات: جعل ملفات Playbook مرنة

تتيح لك المتغيرات إعادة استخدام ملفات Playbook في بيئات مختلفة.

#### أولوية المتغيرات (من الأعلى إلى الأدنى)

1. متغيرات إضافية (`-e` في سطر الأوامر)
2. متغيرات المهام
3. متغيرات الكتل
4. متغيرات الأدوار وinclude
5. متغيرات Play
6. حقائق المضيف
7. `host_vars` الخاصة بملف Playbook
8. `group_vars` الخاصة بملف Playbook
9. `host_vars` الخاصة بالجرد
10. `group_vars` الخاصة بالجرد
11. القيم الافتراضية للأدوار

#### أمثلة على المتغيرات

**متغيرات Playbook:**
```yaml
---
- name: نشر التطبيق
  hosts: webservers
  vars:
    app_name: myapp
    app_version: 2.5.0
    app_port: 8080
  
  tasks:
    - name: نشر {{ app_name }} الإصدار {{ app_version }}
      docker_container:
        name: "{{ app_name }}"
        image: "registry.example.com/{{ app_name }}:{{ app_version }}"
        ports:
          - "{{ app_port }}:8080"
```

**group_vars (خاصة بالبيئة):**
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

**Ansible Vault (متغيرات مشفّرة):**
```bash
# إنشاء ملف مشفر
ansible-vault create secrets.yml

# تحرير ملف مشفر
ansible-vault edit secrets.yml

# محتوى secrets.yml:
# db_password: supersecret123
# api_key: abc123xyz789

# الاستخدام في playbook
ansible-playbook deploy.yml --ask-vault-pass
```

### 5. الأدوار: تنظيم الأتمتة المعقدة

توفر **الأدوار** طريقة منظمة لترتيب ملفات Playbook، مما يجعلها وحدات قابلة لإعادة الاستخدام.

#### البنية الكاملة للدور

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml          # المتغيرات الافتراضية
    ├── vars/
    │   └── main.yml          # متغيرات الدور
    ├── tasks/
    │   ├── main.yml          # قائمة المهام الرئيسية
    │   ├── install.yml       # مهام التثبيت
    │   └── configure.yml     # مهام الإعداد
    ├── handlers/
    │   └── main.yml          # المعالجات (إعادة تشغيل الخدمات)
    ├── templates/
    │   ├── nginx.conf.j2     # قوالب Jinja2
    │   └── site.conf.j2
    ├── files/
    │   └── custom_module.sh  # ملفات ثابتة
    ├── meta/
    │   └── main.yml          # اعتماديات الدور
    └── README.md             # التوثيق
```

#### مثال على دور: nginx

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
- name: تضمين متغيرات نظام التشغيل الخاصة
  include_vars: "{{ ansible_os_family }}.yml"

- name: تثبيت Nginx
  include_tasks: install.yml

- name: إعداد Nginx
  include_tasks: configure.yml

- name: التأكد من تشغيل Nginx
  service:
    name: nginx
    state: started
    enabled: yes
```

**tasks/install.yml:**
```yaml
---
- name: تثبيت Nginx (Debian)
  apt:
    name: nginx
    state: present
    update_cache: yes
  when: ansible_os_family == "Debian"

- name: تثبيت Nginx (RedHat)
  yum:
    name: nginx
    state: present
  when: ansible_os_family == "RedHat"
```

**handlers/main.yml:**
```yaml
---
- name: إعادة تشغيل nginx
  service:
    name: nginx
    state: restarted

- name: إعادة تحميل nginx
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

**استخدام الدور:**
```yaml
---
- name: إعداد خوادم الويب باستخدام دور Nginx
  hosts: webservers
  become: yes
  
  roles:
    - role: nginx
      vars:
        nginx_port: 8080
        nginx_worker_processes: 4
```

## مفاهيم متقدمة في Ansible (2026)

### مجموعات Ansible

**المجموعات** تنسيق لتوزيع محتوى Ansible، مثل الوحدات والأدوار والمكونات الإضافية.

#### تثبيت المجموعات

```bash
# التثبيت من Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install ansible.windows

# التثبيت من ملف المتطلبات
# requirements.yml:
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: amazon.aws
    version: "5.2.0"

ansible-galaxy collection install -r requirements.yml
```

#### استخدام وحدات المجموعات

```yaml
---
- name: استخدام وحدات المجموعات
  hosts: localhost
  tasks:
    - name: استخدام وحدة Docker من community.general
      community.general.docker_container:
        name: webapp
        image: nginx:latest
    
    - name: استخدام وحدة AWS EC2
      amazon.aws.ec2_instance:
        name: webserver
        instance_type: t3.micro
```

### Ansible Tower / AWX (ميزات المؤسسات)

يوفر كل من **Ansible Tower** (تجاري) و**AWX** (مفتوح المصدر):

- واجهة ويب لتنفيذ ملفات Playbook
- التحكم في الوصول المستند إلى الأدوار (RBAC)
- جدولة المهام ومسارات العمل
- تسجيل مركزي ومراجعة
- واجهة REST API للتكامل
- إدارة بيانات الاعتماد
- مزامنة الجرد

**تثبيت AWX باستخدام Docker Compose:**
```bash
# استنساخ مستودع AWX
git clone https://github.com/ansible/awx.git
cd awx

# النشر باستخدام docker-compose
cd tools/docker-compose
docker-compose -f docker-compose.yml up -d

# الوصول عبر http://localhost:80
# تسجيل الدخول الافتراضي: admin / password
```

### أتمتة Windows باستخدام Ansible

تحسّن دعم Ansible لـ Windows بشكل كبير في 2026:

**متطلبات Windows:**
```powershell
# على مضيف Windows، تمكين WinRM
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
```

**جرد Windows:**
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

**ملف Playbook لأتمتة Windows:**
```yaml
---
- name: إعداد خادم Windows
  hosts: windows
  gather_facts: yes
  
  tasks:
    - name: تثبيت IIS
      win_feature:
        name: Web-Server
        state: present
        include_management_tools: yes
    
    - name: نشر الموقع
      win_copy:
        src: ./website/
        dest: C:\inetpub\wwwroot\
    
    - name: إعداد جدار الحماية
      win_firewall_rule:
        name: السماح بـ HTTP
        localport: 80
        protocol: tcp
        action: allow
        direction: in
        enabled: yes
    
    - name: تثبيت البرامج عبر Chocolatey
      win_chocolatey:
        name:
          - googlechrome
          - 7zip
          - notepadplusplus
        state: present
```

### أتمتة الشبكات باستخدام Ansible

تدعم Ansible كبار موردي معدات الشبكات، منهم Cisco وJuniper وArista وF5.

**ملف Playbook لأجهزة الشبكة:**
```yaml
---
- name: إعداد محولات Cisco
  hosts: cisco_switches
  gather_facts: no
  connection: network_cli
  
  vars:
    ansible_network_os: ios
    ansible_user: admin
    ansible_password: "{{ vault_switch_password }}"
  
  tasks:
    - name: إعداد شبكات VLAN
      cisco.ios.ios_vlans:
        config:
          - vlan_id: 10
            name: DATA
          - vlan_id: 20
            name: VOICE
          - vlan_id: 30
            name: GUEST
        state: merged
    
    - name: إعداد الواجهة
      cisco.ios.ios_interfaces:
        config:
          - name: GigabitEthernet1/0/1
            description: Uplink to Core
            enabled: true
    
    - name: حفظ الإعدادات
      cisco.ios.ios_config:
        save_when: always
```

## حالات استخدام وأمثلة من الواقع

### حالة الاستخدام 1: نشر تطبيق ويب كامل

**بنية المشروع:**
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

**site.yml (نشر المكدس الكامل):**
```yaml
---
- name: إعداد جميع الخوادم
  hosts: all
  become: yes
  roles:
    - common

- name: إعداد خوادم قواعد البيانات
  hosts: databases
  become: yes
  roles:
    - postgresql

- name: إعداد خوادم الويب
  hosts: webservers
  become: yes
  roles:
    - nginx
    - application

- name: إعداد موازنات التحميل
  hosts: loadbalancers
  become: yes
  roles:
    - haproxy
```

### حالة الاستخدام 2: إعداد مجموعة Kubernetes

```yaml
---
- name: إعداد مجموعة Kubernetes
  hosts: k8s_cluster
  become: yes
  
  tasks:
    - name: تثبيت Docker
      apt:
        name: docker.io
        state: present
    
    - name: إضافة مفتاح apt لـ Kubernetes
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present
    
    - name: إضافة مستودع Kubernetes
      apt_repository:
        repo: deb https://apt.kubernetes.io/ kubernetes-xenial main
        state: present
    
    - name: تثبيت مكونات Kubernetes
      apt:
        name:
          - kubelet=1.28.0-00
          - kubeadm=1.28.0-00
          - kubectl=1.28.0-00
        state: present

- name: تهيئة Kubernetes master
  hosts: k8s_master
  become: yes
  tasks:
    - name: تهيئة المجموعة
      command: kubeadm init --pod-network-cidr=10.244.0.0/16
      args:
        creates: /etc/kubernetes/admin.conf
    
    - name: إنشاء مجلد .kube
      file:
        path: /home/{{ ansible_user }}/.kube
        state: directory
        owner: "{{ ansible_user }}"
    
    - name: نسخ admin.conf
      copy:
        src: /etc/kubernetes/admin.conf
        dest: /home/{{ ansible_user }}/.kube/config
        remote_src: yes
        owner: "{{ ansible_user }}"
```

### حالة الاستخدام 3: أتمتة تقوية الأمان

```yaml
---
- name: تعزيز الأمان
  hosts: all
  become: yes
  
  tasks:
    - name: تحديث جميع الحزم
      apt:
        upgrade: dist
        update_cache: yes
    
    - name: تثبيت أدوات الأمان
      apt:
        name:
          - fail2ban
          - ufw
          - aide
        state: present
    
    - name: إعداد fail2ban
      copy:
        src: jail.local
        dest: /etc/fail2ban/jail.local
      notify: restart fail2ban
    
    - name: إعداد جدار الحماية
      ufw:
        rule: "{{ item.rule }}"
        port: "{{ item.port }}"
        proto: "{{ item.proto }}"
      loop:
        - { rule: 'allow', port: '22', proto: 'tcp' }
        - { rule: 'allow', port: '80', proto: 'tcp' }
        - { rule: 'allow', port: '443', proto: 'tcp' }
        - { rule: 'deny', port: '3306', proto: 'tcp' }
    
    - name: تمكين جدار الحماية
      ufw:
        state: enabled
    
    - name: تعطيل تسجيل دخول root
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: restart sshd
    
    - name: تعيين سياسة كلمات المرور
      lineinfile:
        path: /etc/login.defs
        regexp: '^PASS_MAX_DAYS'
        line: 'PASS_MAX_DAYS   90'
  
  handlers:
    - name: إعادة تشغيل fail2ban
      service:
        name: fail2ban
        state: restarted
    
    - name: إعادة تشغيل sshd
      service:
        name: sshd
        state: restarted
```

## أفضل ممارسات Ansible (إصدار 2026)

### 1. استخدم التحكم في الإصدارات (Git)

**بنية المستودع:**
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

### 2. طبّق خاصية التكرار الآمن

**مثال سيئ (غير آمن عند التكرار):**
```yaml
- name: إضافة سطر إلى ملف
  shell: echo "new line" >> /etc/myconfig
```

**مثال جيد (آمن عند التكرار):**
```yaml
- name: التأكد من وجود السطر في الملف
  lineinfile:
    path: /etc/myconfig
    line: "new line"
    state: present
```

### 3. استخدم Ansible Lint لضمان جودة الكود

```bash
# تثبيت ansible-lint
pip install ansible-lint

# تشغيل المدقق
ansible-lint playbook.yml

# إصلاح المشكلات الشائعة تلقائياً
ansible-lint --fix playbook.yml
```

### 4. نفّذ الاختبارات باستخدام Molecule

```bash
# تثبيت Molecule
pip install molecule molecule-docker

# تهيئة دور جديد مع الاختبارات
molecule init role my_role --driver-name docker

# تشغيل الاختبارات
cd my_role
molecule test

# مراحل الاختبار:
# - إنشاء بيئة اختبار
# - التنفيذ (تشغيل playbook)
# - التحقق (تشغيل الاختبارات)
# - تدمير البيئة
```

**مثال molecule.yml:**
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

### 5. استخدم الوسوم للتنفيذ الانتقائي

```yaml
---
- name: إعداد الخادم بالكامل
  hosts: webservers
  become: yes
  
  tasks:
    - name: تثبيت الحزم
      apt:
        name: nginx
        state: present
      tags:
        - packages
        - nginx
    
    - name: إعداد Nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      tags:
        - configuration
        - nginx
    
    - name: نشر التطبيق
      copy:
        src: app/
        dest: /var/www/html/
      tags:
        - deployment
        - application

# تشغيل مهام nginx فقط
# ansible-playbook play.yml --tags nginx

# تخطي النشر
# ansible-playbook play.yml --skip-tags deployment
```

### 6. معالجة الأخطاء وتصحيحها

```yaml
---
- name: تنفيذ المهام بمتانة
  hosts: webservers
  
  tasks:
    - name: محاولة عملية محفوفة بالمخاطر
      command: /usr/bin/risky_command
      register: result
      failed_when: false
      changed_when: result.rc == 0
    
    - name: مخرجات التصحيح
      debug:
        var: result
        verbosity: 2
    
    - name: معالجة الفشل
      debug:
        msg: "فشل الأمر، لكن التنفيذ مستمر..."
      when: result.rc != 0
    
    - name: كتلة مع إجراء استرداد
      block:
        - name: جرّب هذا أولاً
          command: /may/fail
        
        - name: إذا نجح، نفّذ هذا
          debug:
            msg: "نجاح!"
      
      rescue:
        - name: إذا فشل، نفّذ هذا بدلاً منه
          debug:
            msg: "تم التعافي من الفشل"
      
      always:
        - name: شغّل هذا دائماً
          debug:
            msg: "عمليات التنظيف"
```

### 7. تحسين الأداء

#### تفعيل pipelining
```ini
# ansible.cfg
[defaults]
pipelining = True
```

#### استخدام Mitogen (أداء أسرع من 3 إلى 7 مرات)
```bash
# تثبيت Mitogen
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

#### التنفيذ المتوازي
```yaml
---
- name: تحديثات متوازية
  hosts: all
  strategy: free  # لا تنتظر جميع المضيفين
  serial: 10      # معالجة 10 مضيفين في كل مرة
  
  tasks:
    - name: تحديث الحزم
      apt:
        upgrade: dist
```

## استكشاف المشكلات الشائعة وإصلاحها

### المشكلة 1: تعذر اتصال SSH

**المشكلة:** تعذر الاتصال بالمضيفين المُدارين

**الحلول:**
```bash
# اختبار اتصال SSH مباشر
ssh -vvv user@host

# اختبار اتصال Ansible
ansible host -m ping -vvv

# الإضافة إلى المخزون
[all:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### المشكلة 2: رفض الإذن (sudo)

**المشكلة:** فشل المهام بسبب أخطاء الصلاحيات

**الحل:**
```yaml
---
- hosts: webservers
  become: yes
  become_method: sudo
  become_user: root
  
  tasks:
    - name: مهمة تتطلب صلاحيات root
      file:
        path: /etc/myconfig
        state: touch
```

### المشكلة 3: لم يتم العثور على الوحدة

**المشكلة:** ظهور أخطاء تفيد بعدم العثور على الوحدة

**الحل:**
```bash
# التأكد من تثبيت المجموعة
ansible-galaxy collection install community.general

# التحقق من المجموعة
ansible-galaxy collection list

# استخدام FQCN (الاسم المؤهل بالكامل للمجموعة)
community.general.docker_container:
  name: mycontainer
```

### المشكلة 4: بطء تنفيذ ملف Playbook

**الحلول:**
1. فعّل pipelining (راجع قسم الأداء)
2. استخدم مكون استراتيجية Mitogen الإضافي
3. عطّل جمع الحقائق إذا لم تكن بحاجة إليه:
   ```yaml
   - hosts: all
     gather_facts: no
   ```
4. استخدم التنفيذ غير المتزامن للمهام الطويلة:
   ```yaml
   - name: مهمة طويلة التشغيل
     command: /usr/bin/long_task
     async: 3600
     poll: 0
   ```

## المسار المهني والشهادات في Ansible

### التدرج في المهارات

**مبتدئ (0-6 أشهر):**
- اكتب ملفات Playbook أساسية
- افهم الجرد والمتغيرات
- استخدم الوحدات الشائعة
- نفّذ ملفات Playbook

**متوسط (6-18 شهرًا):**
- أنشئ أدوارًا قابلة لإعادة الاستخدام
- طبّق معالجة الأخطاء
- استخدم Ansible Vault
- ادمج Ansible مع CI/CD
- أدر بيئات متعددة

**متقدم (أكثر من 18 شهرًا):**
- صمّم أطر أتمتة معقدة
- أنشئ وحدات ومكونات إضافية مخصصة
- خطّط لعمليات نشر Tower/AWX
- حسّن الأداء
- أرشد الآخرين

### الشهادات

**Red Hat Certified Specialist in Ansible Automation (EX407)**
- تثبت الكفاءة في Ansible
- اختبار عملي قائم على الأداء
- صالحة لمدة 3 سنوات
- معترف بها في المجال

**موارد التحضير:**
- Red Hat Learning Subscription
- وثائق Ansible
- مختبرات تدريبية (A Cloud Guru وUdemy)
- منتديات المجتمع

### سوق العمل (2026)

**متوسط الرواتب في الولايات المتحدة:**
- مهندس Ansible مبتدئ: $75,000-$95,000
- مهندس DevOps متوسط الخبرة (Ansible): $110,000-$140,000
- مهندس معماري أول للأتمتة: $150,000-$190,000

**المهارات المطلوبة:**
- Ansible وKubernetes
- Ansible وTerraform (IaC هجين)
- Ansible وCI/CD (Jenkins وGitLab)
- Ansible والسحابة (AWS وAzure وGCP)
- إدارة Ansible Tower/AWX

## موارد التعلم والمجتمع

### الوثائق الرسمية
- [وثائق Ansible](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/) - منصة لمشاركة الأدوار
- [Ansible على GitHub](https://github.com/ansible/ansible)

### دورات عبر الإنترنت
- Red Hat Learning Subscription
- Udemy: `Ansible للمبتدئين تمامًا`
- A Cloud Guru: `تطبيقات عملية على Ansible`
- Linux Academy: `البدء السريع مع Ansible`

### كتب
- `Ansible for DevOps` بقلم Jeff Geerling (تحديث 2025)
- `Ansible: Up and Running` بقلم Lorin Hochstein
- `Mastering Ansible` بقلم James Freeman

### المجتمع
- [قائمة Ansible البريدية](https://groups.google.com/forum/#!forum/ansible-project)
- [Ansible على Reddit](https://reddit.com/r/ansible)
- [خادم Ansible على Discord](https://discord.gg/ansible)
- لقاءات Ansible المحلية والافتراضية

### منصات التدريب
- [سيناريوهات Ansible في Katacoda](https://katacoda.com/ansible)
- [Ansible Playground](https://www.ansible-playground.com/)
- مختبر محلي باستخدام Vagrant أو Docker

## الخلاصة: ابدأ رحلتك مع Ansible

أصبحت Ansible أداة الأتمتة المفضلة لدى المؤسسات حول العالم. وفي 2026، تقدم إمكانات أكثر وإدارة أسهل لـ Windows وتكاملات سحابية محسّنة وإنشاء ملفات Playbook بمساعدة الذكاء الاصطناعي. ستفيدك مهارات Ansible طوال مسيرتك في تقنية المعلومات، سواء أدرت بنية تقليدية أو بيئات سحابية أو عمليات نشر هجينة.

**أهم النقاط:**

1. **ابدأ ببساطة**: أنشئ ملفات Playbook أساسية لإدارة عدد قليل من الخوادم
2. **تدرّب بانتظام**: جهّز مختبرًا منزليًا وجرّب
3. **تعلم بالممارسة**: أتمت المهام الفعلية من عملك اليومي
4. **اتبع أفضل الممارسات**: استخدم التحكم في الإصدارات والاختبارات والوثائق
5. **انضم إلى المجتمع**: تعلم من الآخرين وشارك معرفتك
6. **واكب التغييرات**: تتطور Ansible بسرعة، فواصل التعلم
7. **اجمع الأدوات**: تتيح Ansible وTerraform وKubernetes معًا أتمتة واسعة

**الخطوات التالية:**

1. ثبّت Ansible على نظامك
2. أنشئ جردًا بسيطًا لخوادم الاختبار أو الأجهزة الافتراضية أو الحاويات
3. اكتب أول ملف Playbook، مثل ملف لتثبيت حزمة
4. أضف التعقيد تدريجيًا باستخدام القوالب والمتغيرات والأدوار
5. ساهم في أدوار المجتمع على Ansible Galaxy
6. فكّر في الحصول على شهادة للتحقق من مهاراتك

الانتقال من مبتدئ إلى خبير في Ansible مجزٍ ويفتح فرصًا في DevOps وSRE وهندسة السحابة. تساعدك أساسيات هذا الدليل على بدء أتمتة البنية التحتية وتطوير مهارات قيّمة في مجال تقنية المعلومات الحديث.

مرحبًا بك في عالم أتمتة البنية التحتية باستخدام Ansible!

______

## المراجع

- [وثائق Ansible الرسمية](https://docs.ansible.com/)
- [Ansible Galaxy - مستودع الأدوار](https://galaxy.ansible.com/)
- [مستودع Ansible على GitHub](https://github.com/ansible/ansible)
- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [AWX - Ansible Tower مفتوح المصدر](https://github.com/ansible/awx)
- [أفضل ممارسات Ansible](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [إطار اختبار Molecule](https://molecule.readthedocs.io/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [كتاب Ansible for DevOps بقلم Jeff Geerling](https://www.ansiblefordevops.com/)
- [فهرس مجموعات Ansible](https://docs.ansible.com/ansible/latest/collections/index.html)
