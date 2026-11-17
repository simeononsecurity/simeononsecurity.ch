---
title: "Introducció a Packer per a la infraestructura com a codi"
date: 2023-05-04
lastmod: 2026-11-16
toc: true
draft: false
description: "Aprèn a fer servir Packer per crear imatges de màquina fàcils de mantenir i segures."
tags: ["Packer", "Infraestructura com a codi", "Desenvolupament i operacions", "Automatització", "Seguretat", "Repetibilitat", "Escalabilitat", "Multiplataforma", "Control de versions", "Computació al núvol", "Imatges de màquina", "Virtualització", "Gestió de la configuració", "Integració contínua", "Lliurament continu", "Desenvolupament de programari", "Bones pràctiques", "Proves", "Codi obert", "Multicloud"]
cover: "/img/cover/A_cartoon-style_image_of_a_packer_creating_different_machines.webp"
coverAlt: "Il·lustració de dibuixos animats d'un empaquetador que crea imatges de màquina per a diverses plataformes, amb un portàtil i núvols al fons."
coverCaption: ""
---

**Introducció a l'ús de Packer en aplicacions d'infraestructura com a codi**

**Packer** és una eina popular per crear **imatges de màquina** o **plantilles de màquines virtuals**, que permeten desplegar entorns idèntics en diverses plataformes. Automatitza la creació d'imatges per a plataformes com **AWS, Google Cloud Platform, Azure i VMware**. Packer és una eina de codi obert creada per HashiCorp, l'empresa responsable d'eines populars com Vagrant, Consul i Terraform.

En aquest article coneixeràs Packer i aprendràs a fer-lo servir per crear imatges de màquina per a diferents plataformes. També parlarem dels avantatges de l'eina i d'algunes bones pràctiques.

## Què és Packer?

Packer automatitza el procés de creació d'imatges de màquina per a diferents plataformes. És una eina de codi obert creada per HashiCorp, l'empresa responsable d'altres eines populars com Vagrant, Consul i Terraform.

Amb Packer, els desenvolupadors poden crear imatges de màquina o plantilles de màquines virtuals per a AWS, Google Cloud Platform, Azure i VMware. Després poden fer servir aquestes imatges per desplegar entorns idèntics en diverses plataformes.

## Avantatges de fer servir Packer

Packer ofereix diversos avantatges:

- **Repetibilitat**: crea les imatges de màquina de la mateixa manera cada vegada, amb repetibilitat i coherència entre entorns.
- **Automatització**: automatitza la creació de les imatges, estalvia temps i redueix la possibilitat d'error humà.
- **Compatibilitat multiplataforma**: facilita la creació d'imatges de màquina per a entorns diferents.
- **Integració amb altres eines**: s'integra amb Ansible, Chef i Puppet, de manera que pots fer servir les eines que ja coneixes.
- **Escalabilitat**: crea diverses imatges de màquina en paral·lel i facilita ampliar el procés.

## Com començar amb Packer

Per començar, baixa i instal·la Packer. Està disponible per a Windows, macOS i Linux.

Baixa Packer des del lloc web oficial: [https://www.packer.io/downloads](https://www.packer.io/downloads)

Quan l'hagis instal·lat, podràs començar a crear imatges de màquina per a diferents plataformes.

## Crear una imatge de màquina amb Packer

Per crear una imatge de màquina, defineix una **plantilla** que en descrigui la configuració. La plantilla està escrita en format JSON i especifica els passos necessaris per crear la imatge.

Aquest és un exemple de plantilla Packer per crear una imatge de màquina d'AWS:

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

En aquest exemple, la plantilla indica a Packer que creï una imatge basada en Amazon EBS a partir d'una AMI d'Ubuntu. La imatge resultant s'anomenarà "my-image" i inclourà una marca de temps al final.

Després de definir la plantilla, executa l'ordre `packer build` per crear la imatge:

```bash
$ packer build template.json
```

### AMI d'AWS amb el provisionador Ansible
Pots fer servir el provisionador Ansible amb Packer per crear una imatge de màquina d'AWS. Aquí tens una plantilla d'exemple:

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
En aquest exemple, la plantilla crea una imatge d'AWS i fa servir Ansible per provisionar-la. La secció `provisioners` especifica el playbook d'Ansible que s'ha d'utilitzar.

### Imatge de Google Cloud Platform
També pots fer servir Packer per crear imatges a Google Cloud Platform. Aquí tens una plantilla d'exemple:
```json
{
  "builders": [{
    "type": "googlecompute",
    "project_id": "PROJECT_ID",
    "source_image_family": "ubuntu-1604-lts",
    "zone": "us-central1-f",
    "image_name": "my-image",
    "image_description": "La meva imatge personalitzada"
  }],
  "provisioners": [{
    "type": "shell",
    "inline": [
      "echo 'Hello, World!' > /tmp/hello.txt"
    ]
  }]
}
```
Aquesta plantilla crea una imatge de Google Cloud Platform i fa servir un provisionador de shell per afegir-hi un fitxer. La imatge resultant tindrà el nom "my-image" i la descripció "La meva imatge personalitzada".

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
En aquest exemple, la plantilla crea una imatge de VMware amb una ISO d'Ubuntu Server. La imatge resultant tindrà 4 GB de RAM, 2 CPU i un disc de 40 GB. Durant el provisionament també instal·larà el servidor web nginx.

Aquests són només alguns exemples del que pots fer amb Packer. Pots crear imatges de màquina per a moltes plataformes i fer servir diversos provisionadors per configurar-les.

## Bones pràctiques per fer servir Packer

Segueix aquestes bones pràctiques:

- **Fes servir el control de versions**: desa les plantilles Packer al control de versions per seguir-ne els canvis i facilitar la col·laboració.
- **Parametritza les plantilles**: fes servir variables perquè siguin més reutilitzables i fàcils de mantenir.
- **Prova les plantilles**: comprova que creen les imatges de màquina esperades.
- **Segueix les bones pràctiques de seguretat**: protegeix els entorns resultants quan creïs imatges de màquina.
- **Mantén les plantilles senzilles**: evita les plantilles complexes, difícils de mantenir i depurar.
- **Fes servir l'ordre `packer init`**: inicialitza una plantilla nova amb la configuració necessària.

## Conclusió

Packer és una eina útil per crear imatges de màquina per a plataformes diferents. Ofereix repetibilitat, automatització, compatibilitat multiplataforma i escalabilitat. Segueix les bones pràctiques per crear imatges segures i fàcils de mantenir.

En aquest article hem presentat Packer i hem explicat com crear imatges de màquina per a diverses plataformes. També hem repassat els avantatges de l'eina i algunes bones pràctiques.

Per obtenir més informació sobre Packer, consulta la [documentació oficial](https://www.packer.io/docs).
