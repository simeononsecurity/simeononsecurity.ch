---
title: "Com començar amb Terraform per a la infraestructura com a codi"
date: 2023-05-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Aprèn els conceptes bàsics de Terraform, una eina popular d'infraestructura com a codi, i com fer-la servir per gestionar la infraestructura amb eficàcia."
tags: ["Terraform", "Infraestructura com a codi", "IaC", "Computació al núvol", "DevOps", "Automatització", "AWS", "Azure", "Google Cloud", "Proveïdors de núvol", "Gestió de la configuració", "Desplegament", "Aprovisionament", "Gestió de recursos", "Escalabilitat", "Resiliència", "Seguretat", "Compliment", "Bones pràctiques"]
cover: "/img/cover/A_cartoon_computer_monitor_with_multiple_network-connected.webp"
coverAlt: "Un monitor d'ordinador dibuixat amb diversos dispositius connectats a la xarxa que apareixen com blocs que s'afegeixen o s'eliminen, una representació de la gestió d'infraestructura amb Terraform."
coverCaption: ""
---
**Introducció a l'ús de TeraForm per a aplicacions d'infraestructura com a codi**

A mesura que més organitzacions traslladen la infraestructura al núvol, cada cop és més important gestionar-la de manera eficaç. Aquí és on entra en joc la infraestructura com a codi (IaC). La IaC consisteix a gestionar i aprovisionar infraestructura mitjançant codi en lloc de processos manuals. Això aporta més coherència, rapidesa i fiabilitat. Teraform és una de les eines més populars per a la IaC.

## Què és Teraform?

**Teraform** és una eina de programari de codi obert d'infraestructura com a codi que permet escriure, planificar i crear infraestructura amb codi. HashiCorp la va desenvolupar per gestionar infraestructura en diversos proveïdors de núvol, com AWS, Azure i Google Cloud Platform. Amb Teraform, pots definir la infraestructura en fitxers de configuració, aplicar el codi per crear-la o actualitzar-la i destruir-la quan ja no calgui.

## Avantatges d'utilitzar Teraform

L'ús de Teraform per a aplicacions d'infraestructura com a codi ofereix diversos avantatges:

- **Eficiència i rapidesa:** Teraform permet gestionar la infraestructura amb més rapidesa i eficiència perquè elimina processos manuals.

- **Coherència:** Definir la infraestructura amb codi manté la coherència entre entorns.

- **Escalabilitat:** Teraform facilita l'ampliació de la infraestructura per satisfer la demanda creixent.

- **Col·laboració:** Els fitxers de configuració de Teraform es poden controlar amb versions i compartir amb l'equip, cosa que facilita la col·laboració.

- **Estalvi de costos:** La facilitat amb què Teraform aprovisiona i elimina recursos pot reduir les despeses.

## Primers passos amb Teraform

Per començar amb Teraform, hauràs de:

1. **Descarregar Teraform:** Pots baixar Teraform des del [lloc web oficial](https://www.terraform.io/downloads.html).

2. **Crear un fitxer de configuració:** Teraform utilitza fitxers escrits en HashiCorp Configuration Language (HCL) o JSON. El fitxer defineix la infraestructura que vols crear, actualitzar o eliminar.

Per fer servir Terraform, crea un fitxer de configuració que defineixi la infraestructura desitjada, els recursos que cal crear, les seves propietats i les dependències.

Els fitxers es poden escriure en HashiCorp Configuration Language (HCL), un llenguatge dissenyat per ser llegible i fàcil d'aprendre, o en format JSON. La sintaxi d'HCL s'assembla a la d'altres llenguatges de programació i utilitza blocs, atributs i valors.

Aquest és un exemple bàsic d'un fitxer de configuració Terraform en HCL que crea una instància AWS EC2:

```HCL
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```
En aquest exemple, el fitxer especifica el proveïdor aws i crea un recurs aws_instance amb una imatge de màquina d'Amazon (AMI) i un tipus d'instància.

Per veure un exemple més avançat, consulta aquest exemple de configuració de sistemes amb VMware mitjançant Terraform:
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
En aquest exemple, el fitxer especifica el proveïdor vsphere i crea un recurs vsphere_virtual_machine amb un nom, una carpeta, el nombre de CPU, la memòria, el sistema operatiu convidat, el tipus SCSI i la configuració del disc. També clona la màquina virtual a partir d'una plantilla.

El fitxer també fa servir blocs de dades per consultar a la infraestructura vSphere el centre de dades, el magatzem de dades i la interfície de xarxa que farà servir la màquina virtual.

Un cop creat el fitxer de configuració, el pots utilitzar per crear, actualitzar o eliminar recursos d'infraestructura.

3. **Inicialitzar Teraform:** Després de crear el fitxer, executa `terraform init` per inicialitzar Teraform. Es descarregaran els connectors i mòduls necessaris.

Per exemple, si tens un fitxer `main.tf` dins del directori `terraform-example`, executa-hi aquesta ordre: ```terraform init```

Aquesta ordre descarregarà els connectors i mòduls definits al fitxer de configuració.

4. **Planificar i aplicar la infraestructura:** Després de la inicialització, executa `terraform plan` per veure els canvis previstos i aplica'ls amb `terraform apply`.

L'ordre `terraform plan` mostra quins recursos es crearan, s'actualitzaran o s'eliminaran. Si `main.tf` és dins de `terraform-example`, executa-hi:

```terraform plan```

Això mostra una vista prèvia dels canvis que s'aplicaran.

Quan n'estiguis satisfet, utilitza `terraform apply` per aplicar els canvis. Si `main.tf` és dins de `terraform-example`, executa:

```terraform apply```

Això aplicarà els canvis a la infraestructura. El procés pot trigar una estona, segons la mida i la complexitat de la infraestructura.

## Bones pràctiques per utilitzar Teraform

Per utilitzar Teraform amb eficàcia, segueix aquestes bones pràctiques:

- **Fes servir el control de versions:** Desa els fitxers de configuració en un sistema de control de versions per facilitar la col·laboració i fer un seguiment dels canvis.

- **Fes servir mòduls:** Organitza i reutilitza el codi amb mòduls de Teraform.

- **Separa les configuracions:** Separa la configuració de cada entorn, com ara dev, staging i prod, per mantenir la coherència i evitar divergències.

- **Valida els canvis:** Abans d'aplicar-los a la infraestructura, valida'ls amb l'ordre `terraform plan`.

## Conclusió

Teraform és una eina potent d'infraestructura com a codi que permet gestionar-la amb més rapidesa, eficiència i coherència. Les organitzacions poden estalviar temps i diners i millorar la col·laboració i l'escalabilitat. Segueix les bones pràctiques i comença a utilitzar Teraform per gestionar la infraestructura amb més eficàcia.

---

**Referències:**

- [Lloc web oficial de Teraform](https://www.terraform.io/)
- [Documentació de Teraform](https://www.terraform.io/docs/index.html)
- [Bones pràctiques d'AWS per a seguretat, identitat i compliment](https://aws.amazon.com/architecture/security-identity-compliance/)
