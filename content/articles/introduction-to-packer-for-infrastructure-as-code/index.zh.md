---
title: "使用 Packer 实现基础设施即代码"
date: 2023-05-04
lastmod: 2026-11-16
toc: true
draft: false
description: "了解如何使用 Packer 创建易于维护且安全的机器映像。"
tags: ["Packer", "基础设施即代码", "开发与运维", "自动化", "安全", "可重复性", "可扩展性", "多平台", "版本控制", "云计算", "机器映像", "虚拟化", "配置管理", "持续集成", "持续交付", "软件开发", "最佳实践", "测试", "开源", "多云"]
cover: "/img/cover/A_cartoon-style_image_of_a_packer_creating_different_machines.webp"
coverAlt: "卡通风格插图展示一名打包者为多个平台创建机器映像，背景中有笔记本电脑和云朵。"
coverCaption: ""
---

**Packer 基础设施即代码应用简介**

**Packer** 是一款常用工具，可用于创建**机器映像**或**虚拟机模板**，以便在多个平台上部署相同的环境。它能够自动为 **AWS、Google Cloud Platform、Azure 和 VMware** 等平台创建映像。Packer 是 HashiCorp 开发的开源工具。HashiCorp 还开发了 Vagrant、Consul 和 Terraform 等常用工具。

本文将介绍 Packer，并说明如何使用它为不同平台创建机器映像。我们还会介绍 Packer 的优势和一些最佳实践。

## 什么是 Packer？

Packer 是一款自动为不同平台创建机器映像的工具。它由 HashiCorp 开发并以开源方式发布，该公司还开发了 Vagrant、Consul 和 Terraform 等工具。

开发人员可使用 Packer 为 AWS、Google Cloud Platform、Azure 和 VMware 等平台创建机器映像或虚拟机模板，然后在多个平台上部署相同的环境。

## 使用 Packer 的优势

使用 Packer 有以下优势：

- **可重复性**：每次都以相同方式创建机器映像，使不同环境保持一致且可重复。
- **自动化**：自动创建机器映像，节省时间并减少人为错误。
- **多平台支持**：帮助开发人员创建可用于不同环境的机器映像。
- **与其他工具集成**：可与 Ansible、Chef 和 Puppet 集成，便于使用现有工具创建机器映像。
- **可扩展性**：可并行创建多个机器映像，便于扩大创建流程的规模。

## 开始使用 Packer

首先下载并安装 Packer。Packer 支持 Windows、macOS 和 Linux。

从官方网站下载 Packer：[https://www.packer.io/downloads](https://www.packer.io/downloads)

安装完成后，即可开始为不同平台创建机器映像。

## 使用 Packer 创建机器映像

使用 Packer 创建机器映像时，需要定义一个描述映像配置的**模板**。模板采用 JSON 格式，并列出创建机器映像所需的步骤。

下面是一个用于创建 AWS 机器映像的 Packer 模板示例：

```json
{
"builders": [{
"type": "amazon-ebs",
"access_key": "ACCESS_KEY",
"secret_key": "SECRET_KEY",
"region": "us-west-2",
"source_ami": "ami-0c55b159cbfafe1f0",
"instance_type": "t2.micro",
"ssh_username": "ubuntu",
"ami_name": "my-image-{{timestamp}}"
}]
}
```

此模板指示 Packer 使用 Ubuntu AMI 创建由 Amazon EBS 支持的机器映像。生成的映像名称为“my-image”，后面附加时间戳。

定义模板后，运行 `packer build` 命令创建机器映像：

```bash
$ packer build template.json
```

### 使用 Ansible 配置器创建 AWS AMI
你可以将 Ansible 配置器与 Packer 配合使用来创建 AWS 机器映像。以下是模板示例：

```json
{
  "builders": [{
    "type": "amazon-ebs",
    "access_key": "ACCESS_KEY",
    "secret_key": "SECRET_KEY",
    "region": "us-west-2",
    "source_ami": "ami-0c55b159cbfafe1f0",
    "instance_type": "t2.micro",
    "ssh_username": "ubuntu",
    "ami_name": "my-image-{{timestamp}}"
  }],
  "provisioners": [{
    "type": "ansible",
    "playbook_file": "playbook.yml"
  }]
}
```
此模板创建 AWS 机器映像并使用 Ansible 进行配置。模板的 `provisioners` 部分指定要使用的 Ansible playbook。

### Google Cloud Platform 映像
你也可以使用 Packer 在 Google Cloud Platform 上创建机器映像。示例如下：
```json
{
  "builders": [{
    "type": "googlecompute",
    "project_id": "PROJECT_ID",
    "source_image_family": "ubuntu-1604-lts",
    "zone": "us-central1-f",
    "image_name": "my-image",
    "image_description": "我的自定义机器映像"
  }],
  "provisioners": [{
    "type": "shell",
    "inline": [
      "echo 'Hello, World!' > /tmp/hello.txt"
    ]
  }]
}
```
此模板在 Google Cloud Platform 上创建映像，并通过 shell 配置器添加文件。生成的映像名称为“my-image”，描述为“我的自定义机器映像”。

### VMware

```json
{
  "builders": [
    {
      "type": "vmware-iso",
      "iso_url": "https://releases.ubuntu.com/20.04.2/ubuntu-20.04.2-live-server-amd64.iso",
      "iso_checksum_type": "sha256",
      "iso_checksum": "a244fe4adcc2ad92d15c12e47ca4ea97fb5b5d67b1ba50880c9e420ae3f3c083",
      "guest_os_type": "ubuntu-64",
      "disk_size": 40960,
      "vm_name": "ubuntu-20.04.2-server-amd64",
      "ssh_username": "ubuntu",
      "ssh_password": "ubuntu",
      "ssh_port": 22,
      "ssh_wait_timeout": "60m",
      "shutdown_command": "sudo shutdown -P now",
      "vmx_data": {
        "memsize": "4096",
        "numvcpus": "2"
      }
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "sudo apt-get update",
        "sudo apt-get install -y nginx"
      ]
    }
  ]
}
```
此模板使用 Ubuntu Server ISO 创建 VMware 机器映像。生成的机器拥有 4 GB 内存、2 个 CPU 和 40 GB 磁盘。配置过程中还会安装 nginx Web 服务器。

这些只是 Packer 的部分用途示例。你可以为许多平台创建机器映像，并使用各种配置器进行配置。

## 使用 Packer 的最佳实践

使用 Packer 时，请遵循以下最佳实践：

- **使用版本控制**：将 Packer 模板保存在版本控制系统中，以跟踪更改并支持协作。
- **参数化模板**：使用变量提高模板的可复用性和可维护性。
- **测试模板**：确认模板能够创建预期的机器映像。
- **遵循安全最佳实践**：创建机器映像时保护生成的环境。
- **保持模板简单**：避免创建难以维护和调试的复杂模板。
- **使用 `packer init` 命令**：使用该命令初始化包含所需配置的新模板。

## 总结

Packer 是一款实用工具，可为不同平台创建机器映像。它提供可重复性、自动化、多平台支持和可扩展性。遵循最佳实践，有助于创建易于维护且安全的机器映像。

本文介绍了 Packer，并说明如何使用它为不同平台创建机器映像。我们也讨论了它的优势和一些最佳实践。

如需进一步了解 Packer，请参阅[官方文档](https://www.packer.io/docs)。
