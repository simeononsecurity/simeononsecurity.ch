---
title: "Introdução ao Packer para Infraestrutura como Código"
date: 2023-05-04
lastmod: 2026-11-16
toc: true
draft: false
description: "Aprenda a usar o Packer para criar imagens de máquinas fáceis de manter e seguras."
tags: ["Packer", "Infraestrutura como Código", "Desenvolvimento e operações", "Automação", "Segurança", "Repetibilidade", "Escalabilidade", "Multiplataforma", "Controle de Versão", "Computação em Nuvem", "Imagens de Máquina", "Virtualização", "Gerenciamento de Configuração", "Integração Contínua", "Entrega Contínua", "Desenvolvimento de Software", "Boas Práticas", "Testes", "Código Aberto", "Multinuvem"]
cover: "/img/cover/A_cartoon-style_image_of_a_packer_creating_different_machines.webp"
coverAlt: "Ilustração em estilo de desenho animado de um empacotador criando imagens de máquinas para várias plataformas, com um laptop e nuvens ao fundo."
coverCaption: ""
---

**Introdução ao uso do Packer em aplicações de Infraestrutura como Código**

**Packer** é uma ferramenta popular para criar **imagens de máquinas** ou **modelos de máquinas virtuais**, usados para implantar ambientes idênticos em várias plataformas. Ela permite automatizar a criação de imagens para plataformas como **AWS, Google Cloud Platform, Azure e VMware**. O Packer é uma ferramenta de código aberto criada pela HashiCorp, empresa responsável por ferramentas conhecidas como Vagrant, Consul e Terraform.

Neste artigo, você conhecerá o Packer e verá como criar imagens de máquinas para diferentes plataformas. Também aprenderá sobre os benefícios da ferramenta e algumas boas práticas.

## O que é o Packer?

O Packer automatiza a criação de imagens de máquinas para diferentes plataformas. É uma ferramenta de código aberto criada pela HashiCorp, empresa responsável por outras ferramentas conhecidas, como Vagrant, Consul e Terraform.

Com o Packer, desenvolvedores criam imagens de máquinas ou modelos de máquinas virtuais para plataformas como AWS, Google Cloud Platform, Azure e VMware. Depois, podem usar essas imagens para implantar ambientes idênticos em várias plataformas.

## Benefícios do uso do Packer

O Packer oferece vários benefícios:

- **Repetibilidade**: cria imagens de máquinas sempre da mesma forma, com repetibilidade e consistência entre ambientes.
- **Automação**: automatiza a criação de imagens de máquinas, economiza tempo e reduz a possibilidade de erro humano.
- **Suporte multiplataforma**: permite criar imagens de máquinas para uso em diferentes ambientes.
- **Integração com outras ferramentas**: funciona com Ansible, Chef e Puppet, facilitando a criação de imagens com ferramentas que você já usa.
- **Escalabilidade**: cria várias imagens de máquinas em paralelo e facilita aumentar a escala do processo.

## Começar a usar o Packer

Para começar, baixe e instale o Packer. Ele está disponível para Windows, macOS e Linux.

Baixe o Packer no site oficial: [https://www.packer.io/downloads](https://www.packer.io/downloads)

Depois da instalação, você poderá criar imagens de máquinas para diferentes plataformas.

## Criar uma imagem de máquina com o Packer

Para criar uma imagem de máquina, defina um **modelo** que descreva sua configuração. O modelo usa o formato JSON e especifica as etapas necessárias para criar a imagem.

Este é um modelo Packer de exemplo para criar uma imagem de máquina da AWS:

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

Neste exemplo, o modelo instrui o Packer a criar uma imagem baseada no Amazon EBS usando uma AMI do Ubuntu. O nome da imagem resultante será "my-image", seguido de um carimbo de data e hora.

Depois de definir o modelo, execute o comando `packer build` para criar a imagem:

```bash
$ packer build template.json
```

### AMI da AWS com provisionador Ansible
Você pode usar o provisionador Ansible com o Packer para criar uma imagem de máquina da AWS. Veja um modelo de exemplo:

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
Neste exemplo, o modelo cria uma imagem da AWS e usa o Ansible para provisioná-la. A seção `provisioners` especifica o playbook do Ansible que será usado.

### Imagem do Google Cloud Platform
Você também pode usar o Packer para criar imagens no Google Cloud Platform. Veja este modelo de exemplo:
```json
{
  "builders": [{
    "type": "googlecompute",
    "project_id": "PROJECT_ID",
    "source_image_family": "ubuntu-1604-lts",
    "zone": "us-central1-f",
    "image_name": "my-image",
    "image_description": "Minha imagem personalizada"
  }],
  "provisioners": [{
    "type": "shell",
    "inline": [
      "echo 'Hello, World!' > /tmp/hello.txt"
    ]
  }]
}
```
Este modelo cria uma imagem no Google Cloud Platform e usa um provisionador de shell para adicionar um arquivo. A imagem resultante terá o nome "my-image" e a descrição "Minha imagem personalizada".

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
Neste exemplo, o modelo cria uma imagem de máquina VMware usando uma ISO do Ubuntu Server. A imagem terá 4 GB de RAM, 2 CPUs e um disco de 40 GB. Durante o provisionamento, também instalará o servidor web nginx.

Esses são apenas alguns exemplos do que você pode fazer com o Packer. A ferramenta permite criar imagens de máquinas para muitas plataformas e usar vários provisionadores para configurá-las.

## Boas práticas para usar o Packer

Siga estas boas práticas ao usar o Packer:

- **Use controle de versão**: armazene os modelos Packer sob controle de versão para acompanhar alterações e permitir a colaboração.
- **Parametrize seus modelos**: use variáveis para torná-los mais reutilizáveis e fáceis de manter.
- **Teste seus modelos**: confirme se eles criam as imagens de máquinas esperadas.
- **Siga as práticas recomendadas de segurança**: proteja os ambientes resultantes ao criar imagens de máquinas.
- **Mantenha os modelos simples**: evite modelos complexos, difíceis de manter e depurar.
- **Use o comando `packer init`**: inicialize um novo modelo com a configuração necessária.

## Conclusão

O Packer é uma ferramenta útil para criar imagens de máquinas em diferentes plataformas. Ele oferece repetibilidade, automação, suporte multiplataforma e escalabilidade. Siga as boas práticas para criar imagens de máquinas fáceis de manter e seguras.

Neste artigo, apresentamos o Packer e mostramos como criar imagens de máquinas para diferentes plataformas. Também discutimos os benefícios da ferramenta e algumas boas práticas.

Para saber mais sobre o Packer, consulte a documentação oficial: [https://www.packer.io/docs](https://www.packer.io/docs).
