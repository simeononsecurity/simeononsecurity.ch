---
title: "Terraform 入门：将基础设施作为代码管理"
date: 2023-05-04
lastmod: 2026-11-13
toc: true
draft: false
description: "了解 Terraform 这款常用基础设施即代码工具的基础知识，以及如何用它高效管理基础设施。"
tags: ["Terraform", "基础设施即代码", "IaC", "云计算", "DevOps", "自动化", "AWS", "Azure", "Google Cloud", "云服务提供商", "配置管理", "部署", "资源配置", "资源管理", "可扩展性", "弹性", "安全", "合规", "最佳实践"]
cover: "/img/cover/A_cartoon_computer_monitor_with_multiple_network-connected.webp"
coverAlt: "卡通电脑显示器上显示多个联网设备，设备像积木一样被添加或移除，体现使用 Terraform 管理基础设施。"
coverCaption: ""
---
**使用 TeraForm 将基础设施作为代码管理**

随着更多组织将基础设施迁移到云端，高效管理基础设施变得十分重要。基础设施即代码（IaC）通过代码而非手动流程来管理和配置基础设施，可提升管理的一致性、速度和可靠性。Teraform 是常用的 IaC 工具之一。

## 什么是 Teraform？

**Teraform** 是一款开源的基础设施即代码软件工具，用户可用代码编写、规划并创建基础设施。Teraform 由 HashiCorp 开发，可管理 AWS、Azure 和 Google Cloud Platform 等多个云服务提供商上的基础设施。用户在配置文件中定义基础设施，再应用代码来创建或更新资源，并在不再需要时销毁资源。

## 使用 Teraform 的好处

使用 Teraform 管理基础设施即代码有多项好处：

- **效率和速度：** Teraform 通过减少手动流程，让基础设施管理更快、更高效。

- **一致性：** 用代码定义基础设施有助于保持不同环境之间的一致性。

- **可扩展性：** Teraform 便于扩展基础设施，以满足不断增长的需求。

- **协作：** Teraform 配置文件可纳入版本控制并与团队成员共享，从而简化协作。

- **节省成本：** Teraform 可轻松配置和移除资源，帮助降低成本。

## 开始使用 Teraform

开始使用 Teraform，需要完成以下步骤：

1. **下载 Teraform：** 从[官方网站](https://www.terraform.io/downloads.html)下载 Teraform。

2. **创建配置文件：** Teraform 使用以 HashiCorp Configuration Language (HCL) 或 JSON 编写的配置文件。文件中定义要创建、更新或删除的基础设施。

使用 Terraform 时，需要创建配置文件来描述目标基础设施、要创建的资源、资源属性及其依赖关系。

配置文件可使用 HashiCorp Configuration Language (HCL) 或 JSON 编写。HCL 旨在便于阅读和学习，语法与其他编程语言相似，使用块、属性和值。

下面是一个使用 HCL 创建 AWS EC2 实例的基本 Terraform 配置示例：

```HCL
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```
此配置指定 aws 提供商，并创建一个包含 Amazon Machine Image (AMI) 和实例类型的 aws_instance 资源。

下面是使用 Terraform 配置 VMware 系统的进阶示例：
```HCL
provider "vsphere" {
  user           = "user@domain.com"
  password       = "password"
  vsphere_server = "vcenter.example.com"
}

data "vsphere_datacenter" "dc" {
  name = "Datacenter"
}

data "vsphere_datastore" "ds" {
  name          = "Datastore"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_network_interface" "nic" {
  label          = "Network adapter 1"
  datacenter_id  = data.vsphere_datacenter.dc.id
  network_id     = "VM Network"
}

resource "vsphere_virtual_machine" "vm" {
  name             = "terraform-vm"
  folder           = "/terraform"
  num_cpus         = 2
  memory           = 2048
  guest_id         = "otherLinux64Guest"
  scsi_type        = "pvscsi"
  datastore_id     = data.vsphere_datastore.ds.id

  network_interface {
    network_id = data.vsphere_network_interface.nic.network_id
  }

  disk {
    label            = "disk0"
    size             = 20
    eagerly_scrub    = true
    thin_provisioned = true
  }

  clone {
    template_uuid = "template-uuid"
  }
}

```
此配置指定 vsphere 提供商，并创建一个 vsphere_virtual_machine 资源，设置名称、文件夹、CPU 数量、内存、客户机操作系统、SCSI 类型和磁盘参数。它还会从指定模板克隆虚拟机。

配置还使用数据块查询 vSphere 基础设施，以获取虚拟机资源所需的数据中心、数据存储和网络接口信息。

创建配置文件后，可用它创建、更新或删除基础设施资源。

3. **初始化 Teraform：** 创建配置文件后，运行 `terraform init` 初始化 Teraform。此命令会下载所需的插件和模块。

例如，如果 `main.tf` 位于 `terraform-example` 目录中，请在该目录运行：```terraform init```

此命令会下载配置文件中指定的插件和模块。

4. **规划并应用基础设施变更：** 初始化后，运行 `terraform plan` 查看将要进行的变更，再使用 `terraform apply` 应用变更。

`terraform plan` 会显示将创建、更新或删除的资源。如果 `main.tf` 位于 `terraform-example` 目录中，请运行：

```terraform plan```

命令会预览基础设施变更。

确认计划后，使用 `terraform apply` 应用变更。如果 `main.tf` 位于 `terraform-example` 目录中，请运行：

```terraform apply```

该命令会应用基础设施变更。根据基础设施的规模和复杂程度，操作可能需要一些时间。

## 使用 Teraform 的最佳实践

为有效使用 Teraform，请遵循以下最佳实践：

- **使用版本控制：** 将 Teraform 配置文件存入版本控制系统，以便协作并跟踪变更。

- **使用模块：** 使用 Teraform 模块组织和复用代码。

- **分离配置：** 按环境分开配置，例如 dev、staging 和 prod，以保持一致并避免配置漂移。

- **验证变更：** 应用基础设施变更之前，使用 `terraform plan` 验证变更。

## 结论

Teraform 是一款强大的基础设施即代码工具，可帮助更快速、高效、一致地管理基础设施。组织可借此节省时间和成本，并改善协作与扩展能力。遵循最佳实践并开始使用 Teraform，可更有效地管理基础设施。

---

**参考资料：**

- [Teraform 官方网站](https://www.terraform.io/)
- [Teraform 文档](https://www.terraform.io/docs/index.html)
- [AWS 安全、身份与合规最佳实践](https://aws.amazon.com/architecture/security-identity-compliance/)
