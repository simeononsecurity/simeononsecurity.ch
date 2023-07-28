---
title: "Ansible 简介：自动化 IT 基础架构管理"
draft: false
toc: true
date: 2023-02-25
description: "学习 Ansible 的基础知识，这是一款开源自动化工具，通过声明式语言简化 IT 基础架构管理。"
tags: ["Ansible 简介", "IT 基础设施管理自动化", "Ansible 基础知识", "IT 基础设施自动化", "配置管理", "应用程序部署", "供应", "持续交付", "安全合规性", "编排", "YAML", "Ansible 模块", "角色", "最佳做法", "版本控制", "测试", "红帽", "系统管理员", "利纳克斯", "MacOS", "视窗", "Ansible 安装", "Ansible 清单", "Ansible 操作手册", "Ansible 模块", "Ansible 角色", "Ansible 最佳实践", "Ansible 测试", "IT 基础设施自动化工具", "Ansible 教程", "基础设施管理自动化"]
cover: "/img/cover/A_cartoon_character_sitting_at_a_desk_surrounded_by_servers.png"
coverAlt: "一个卡通人物坐在办公桌前，周围是服务器和线缆，电脑屏幕上显示着 Ansible 的标识，他微笑着完成自动化任务。"
coverCaption: ""
---

Ansible 是一款开源自动化工具，可帮助系统管理员实现 IT 基础架构管理自动化。它提供了一种简单的语言来描述基础设施的理想状态，并自动执行该状态。这减少了管理大规模复杂系统所需的时间和精力。

如果您是 Ansible 的新用户，本文将介绍该工具，包括其基本概念和如何开始使用。

## Ansible 简介

Ansible 由 Michael DeHaan 于 2012 年开发，2015 年被 Red Hat 收购。从那时起，它已成为业界最流行的自动化工具之一。

{{< youtube id="goclfp6a2IQ" >}}

Ansible 使用一种简单的声明式语言 YAML（"YAML 不是标记语言 "的缩写）来定义基础设施的理想状态。这使得它易于阅读和理解，即使是非程序员也不例外。

Ansible 可用于自动化各种任务，包括

- 配置管理
- 应用程序部署**
- 持续交付
- 配置管理
- 安全合规性
- 协调

## Ansible 入门

要开始使用 Ansible，你需要在系统上安装它。Ansible 可以安装在多种操作系统上，包括 Linux、macOS 和 Windows。

要在 Linux（这里是 Ubuntu）上安装 Ansible，可以使用以下命令：
```bash
sudo apt-get update
sudo apt-get install ansible -y
```
否则，您可以使用以下指南安装 ansible：
- [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

Ansible 安装完成后，可以运行以下命令验证其是否正常运行：
```bash
ansible --version
```

这将显示已安装的 Ansible 版本。

## Ansible 目录

使用 Ansible 的第一步是定义清单。清单是 Ansible 要管理的服务器列表。清单可以多种格式定义，包括 INI、YAML 和 JSON。

下面是一个 INI 格式的清单文件示例：

```ini
[webservers]
webserver1.example.com
webserver2.example.com

[databases]
dbserver1.example.com
dbserver2.example.com
```

该清单文件定义了两组服务器，即 "网络服务器 "和 "数据库"，并列出了每组服务器的主机名。

## Ansible 操作手册

定义了清单后，下一步就是定义一个 playbook。playbook 是一个 YAML 文件，描述了 Ansible 应在清单中的服务器上执行的一系列任务。

下面是一个简单的示例：
```yml
name: Install Nginx
hosts: webservers
become: yes

tasks:
    - name: Install Nginx package
        apt:
        name: nginx
        state: present
```

此播放本将在 "webservers "组中的所有服务器上安装 Nginx 网络服务器。

该 `hosts`参数指定游戏本应在哪组服务器上运行。参数 `become`参数指定任务应以提升的权限运行（使用 `sudo`或 `su`

"(《世界人权宣言》) `tasks`部分列出了游戏本应执行的各个任务。在本例中，只有一个任务，即使用 `apt`模块。

## Ansible 模块

Ansible 模块是可重复使用的代码单元，可用于执行特定任务。Ansible 自带大量内置模块，也有许多第三方模块可用。

下面是一些内置模块的例子：

- `apt`- 在基于 Debian 的系统上管理软件包
- `yum`- 管理基于 Red Hat 的系统上的软件包
- `file`- 管理文件
- `service`- 管理系统服务
- `user`- 管理用户和组
- `copy`- 将文件从控制机复制到受管服务器

内置模块的完整列表可在 [Ansible documentation](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Ansible 角色和文件夹结构

Ansible 角色是组织和重用常见任务和配置的一种方式。它是一个包含任务、处理程序、模板、文件和其他资源的目录结构。

下面是一个简单的 Ansible 角色示例，用于安装和配置 Nginx：
```
roles/
└── nginx/
    ├── tasks/
    │   ├── main.yml
    ├── handlers/
    │   ├── main.yml
    ├── templates/
    │   ├── nginx.conf.j2
    ├── files/
    ├── vars/
    ├── defaults/
    ├── meta/
```
在本例中，nginx 角色是一个包含多个子目录的目录，每个子目录都有特定用途：

- 任务**：包含角色将执行的任务。
- 处理程序**：包含任务可以通知的处理程序。
- templates**：包含用于生成 Nginx 配置文件的 Jinja2 模板。
- files**：包含角色需要的静态文件。
- vars**：包含角色专用的变量。
- **defaults**：包含角色的默认变量。
- **meta**：包含角色的元数据，例如其依赖关系。

角色可以在多个游戏本和项目中轻松共享和重用。

下面是 tasks 目录中 main.yml 文件的示例：
```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
  notify: restart nginx

- name: Enable Nginx
  systemd:
    name: nginx
    enabled: yes
    state: started
```

该任务使用 apt 模块安装 Nginx，并使用 systemd 模块启用和启动 Nginx 服务。它还会通知重启 Nginx 处理程序，如果配置有任何更改，该处理程序将重启 Nginx。

使用这样的 Ansible 角色可以简化跨多个服务器或环境管理和配置软件的过程。通过将任务、处理程序、模板和其他资源分离到一个目录结构中，你可以更轻松地管理这些组件，并在不同的游戏本和项目中重复使用。

## Ansible 最佳实践

以下是使用 Ansible 时应遵循的一些最佳实践：

### 1.使用版本控制

在版本控制系统（如 Git）中存储 Ansible 操作手册和角色是一种最佳实践，它能帮助你跟踪更改并与他人协作。版本控制提供了对代码库所做更改的历史记录，允许你在需要时回滚到以前的版本。通过共享代码和管理冲突，它还能让你轻松地与他人协作。

### 2.使用角色来组织你的游戏手册

角色是组织 Ansible 操作手册和任务的强大方法。通过将相关任务归类到角色中，可以使你的游戏本更加模块化和可重用。角色还能让你在不同项目间轻松共享代码。

下面是一个使用角色安装和配置 Nginx 的示例：

```yml
name: Install and configure Nginx
hosts: webservers
become: yes
roles:
  - nginx
```

本游戏手册使用名为 "nginx "的角色在 "webservers "主机组上安装和配置 Nginx。

### 3.使用标签分组任务

标签可用于在 Ansible 管理程序中将相关任务分组。这样就能更容易地运行一个 playbook 的特定部分，尤其是在处理大型、复杂的 playbook 时。

下面举例说明如何在 Ansible 管理程序中使用标签：
```yml
name: Install and configure Nginx
hosts: webservers
become: yes
tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
    tags: nginx_install

  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    tags: nginx_config
```

该 playbook 有两个任务，一个用于安装 Nginx，另一个用于配置 Nginx。每个任务都有一个关联标签，这样就可以只运行需要的任务。

### 4.使用变量使游戏本更灵活

变量可用于使你的 Ansible playbooks 更灵活、更可重用。通过使用变量，你可以使你的播放列表更通用，并适应不同的环境。

下面举例说明如何在 Ansible playbook 中使用变量：
```yml
name: Install and configure Nginx
hosts: webservers
become: yes

vars:
nginx_port: 80
nginx_user: www-data

tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    notify: restart nginx

handlers:
  - name: restart nginx
    service:
    name: nginx
    state: restarted
```

该剧本使用变量指定 Nginx 应监听的端口和运行 Nginx 的用户。这使得该播放列表更加灵活，可适应不同环境。

### 5.测试播放书

测试你的 Ansible playbook 是一种最佳做法，它能帮助你发现错误并确保你的 playbook 按预期运行。Molecule 是一款常用的 Ansible 操作手册测试工具。

Molecule 是一个测试框架，可以让你以一致和自动化的方式测试你的游戏本。Molecule 可以创建虚拟机，应用你的 playbook，然后验证一切是否按预期运行。这可以帮助你捕捉错误，并确保你的游戏本在部署到生产之前工作正常。

下面是一个如何使用 Molecule 测试 Ansible 角色的示例：

```bash
molecule init role myrole
cd myrole
molecule test
```

## 结论

在本文中，我们介绍了 Ansible 这款强大的自动化工具，它可以帮助你管理复杂的 IT 基础架构。我们介绍了 Ansible 的基本概念，包括清单、播放本、模块和角色。

我们还讨论了使用 Ansible 的最佳实践，包括使用版本控制、用角色组织 playbook、使用标签和变量以及测试 playbook。

如果你是 Ansible 的新手，我们建议你从尝试使用一些简单的游戏本开始，随着时间的推移逐步积累你的技能和知识。通过练习，即使是最复杂的基础架构任务，您也能轻松实现自动化！
