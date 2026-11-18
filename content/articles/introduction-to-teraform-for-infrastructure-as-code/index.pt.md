---
title: "Comece a usar Terraform para infraestrutura como código"
date: 2023-05-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Aprenda os fundamentos do Terraform, uma ferramenta popular de infraestrutura como código, e como usá-la para gerenciar a infraestrutura com eficiência."
tags: ["Terraform", "Infraestrutura como código", "IaC", "Computação em nuvem", "DevOps", "Automação", "AWS", "Azure", "Google Cloud", "Provedores de nuvem", "Gerenciamento de configuração", "Implantação", "Provisionamento", "Gerenciamento de recursos", "Escalabilidade", "Resiliência", "Segurança", "Conformidade", "Boas práticas"]
cover: "/img/cover/A_cartoon_computer_monitor_with_multiple_network-connected.webp"
coverAlt: "Um monitor de computador ilustrado com vários dispositivos conectados à rede que aparecem como blocos de construção sendo adicionados ou removidos, representando o gerenciamento de infraestrutura com Terraform."
coverCaption: ""
---
**Introdução ao uso do TeraForm em aplicações de infraestrutura como código**

À medida que mais organizações migram sua infraestrutura para a nuvem, torna-se essencial gerenciá-la com eficiência. É aí que entra a infraestrutura como código (IaC), o processo de gerenciar e provisionar infraestrutura por meio de código em vez de processos manuais. Isso aumenta a consistência, a velocidade e a confiabilidade. Teraform é uma das ferramentas mais populares para IaC.

## O que é Teraform?

**Teraform** é uma ferramenta de software de código aberto para infraestrutura como código. Ela permite escrever, planejar e criar infraestrutura usando código. Desenvolvida pela HashiCorp, a ferramenta gerencia recursos em vários provedores de nuvem, incluindo AWS, Azure e Google Cloud Platform. Com Teraform, você define a infraestrutura em arquivos de configuração, aplica o código para criá-la ou atualizá-la e a destrói quando não precisar mais dela.

## Benefícios do uso de Teraform

Usar Teraform para aplicações de infraestrutura como código oferece vários benefícios:

- **Eficiência e velocidade:** Teraform torna o gerenciamento da infraestrutura mais rápido e eficiente ao eliminar processos manuais.

- **Consistência:** Definir a infraestrutura com código mantém a consistência entre ambientes.

- **Escalabilidade:** Teraform facilita a expansão da infraestrutura para atender à demanda crescente.

- **Colaboração:** Os arquivos de configuração de Teraform podem ser versionados e compartilhados pela equipe, o que facilita a colaboração.

- **Redução de custos:** O provisionamento e a remoção simples de recursos com Teraform podem reduzir custos.

## Primeiros passos com Teraform

Para começar a usar Teraform:

1. **Baixe o Teraform:** Faça o download do Teraform no [site oficial](https://www.terraform.io/downloads.html).

2. **Crie um arquivo de configuração:** Teraform usa arquivos escritos em HashiCorp Configuration Language (HCL) ou JSON. O arquivo define a infraestrutura que você deseja criar, atualizar ou excluir.

Para usar Terraform, crie um arquivo de configuração que defina a infraestrutura desejada, os recursos que serão criados, suas propriedades e dependências.

Os arquivos podem ser escritos em HashiCorp Configuration Language (HCL), uma linguagem projetada para ser legível e fácil de aprender, ou em JSON. A sintaxe HCL é semelhante à de outras linguagens de programação e usa blocos, atributos e valores.

Veja um exemplo básico de arquivo de configuração Terraform em HCL que cria uma instância AWS EC2:

```HCL
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```
Neste exemplo, o arquivo especifica o provedor aws e cria um recurso aws_instance com uma Amazon Machine Image (AMI) e um tipo de instância.

Para um exemplo mais avançado, veja a configuração de sistemas VMware com Terraform:
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
Neste exemplo, o arquivo especifica o provedor vsphere e cria um recurso vsphere_virtual_machine com nome, pasta, quantidade de CPUs, memória, sistema operacional convidado, tipo SCSI e configurações de disco. Ele também clona a máquina virtual de um modelo especificado.

O arquivo também usa blocos de dados para consultar a infraestrutura vSphere sobre o datacenter, o datastore e a interface de rede que o recurso da máquina virtual usará.

Depois de criar o arquivo de configuração, você poderá usá-lo para criar, atualizar ou excluir recursos de infraestrutura.

3. **Inicialize o Teraform:** Após criar o arquivo, execute `terraform init` para inicializar o Teraform. O comando baixará os plugins e módulos necessários.

Por exemplo, se `main.tf` estiver no diretório `terraform-example`, execute o comando abaixo nesse diretório: ```terraform init```

Isso baixará os plugins e módulos especificados no arquivo de configuração.

4. **Planeje e aplique a infraestrutura:** Após a inicialização, execute `terraform plan` para ver as alterações previstas e aplique-as com `terraform apply`.

O comando `terraform plan` mostra quais recursos serão criados, atualizados ou excluídos. Se `main.tf` estiver no diretório `terraform-example`, execute:

```terraform plan```

Isso exibirá uma prévia das alterações na infraestrutura.

Depois de revisar o plano, use `terraform apply` para aplicar as alterações. Se `main.tf` estiver no diretório `terraform-example`, execute:

```terraform apply```

Isso aplicará as alterações à infraestrutura. O processo pode levar algum tempo, dependendo do tamanho e da complexidade da infraestrutura.

## Boas práticas para usar Teraform

Para usar Teraform com eficiência, considere estas boas práticas:

- **Use controle de versão:** Armazene os arquivos de configuração em um sistema de controle de versão para facilitar a colaboração e acompanhar as alterações.

- **Use módulos:** Organize e reutilize o código com módulos de Teraform.

- **Separe as configurações:** Separe as configurações por ambiente, como dev, staging e prod, para manter a consistência e evitar desvios de configuração.

- **Valide as alterações:** Antes de aplicá-las à infraestrutura, valide-as com o comando `terraform plan`.

## Conclusão

Teraform é uma ferramenta poderosa de infraestrutura como código que permite gerenciar a infraestrutura com mais velocidade, eficiência e consistência. As organizações podem economizar tempo e dinheiro e melhorar a colaboração e a escalabilidade. Siga as boas práticas e comece a usar Teraform para gerenciar sua infraestrutura com mais eficiência.

---

**Referências:**

- [Site oficial do Teraform](https://www.terraform.io/)
- [Documentação do Teraform](https://www.terraform.io/docs/index.html)
- [Boas práticas da AWS para segurança, identidade e conformidade](https://aws.amazon.com/architecture/security-identity-compliance/)
