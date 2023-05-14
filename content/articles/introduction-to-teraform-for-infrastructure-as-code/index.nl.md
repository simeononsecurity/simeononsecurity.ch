---
title: "Aan de slag met Terraform voor Infrastructure as Code"
date: 2023-05-04
toc: true
draft: false
description: "Leer de basis van Terraform, een populaire infrastructure as code tool, en hoe u deze kunt gebruiken om infrastructuur efficiënt te beheren."
tags: ["Terraform", "Infrastructuur als code", "IaC", "Cloud Computing", "DevOps", "Automatisering", "AWS", "Azuur", "Google Cloud", "Cloud aanbieders", "Configuratiebeheer", "Inzet", "Voorziening", "Beheer van middelen", "Schaalbaarheid", "Veerkracht", "Beveiliging", "Naleving", "Beste praktijken"]
cover: "/img/cover/A_cartoon_computer_monitor_with_multiple_network-connected.png"
coverAlt: "Een cartoonachtig computerscherm waarop meerdere op het netwerk aangesloten apparaten verschijnen als bouwstenen die worden toegevoegd of verwijderd, wat duidt op infrastructuurbeheer met Terraform."
coverCaption: ""
---

**Inleiding tot het gebruik van TeraForm voor Infrastructure as code toepassingen**

Naarmate meer organisaties hun infrastructuur naar de cloud verplaatsen, wordt de noodzaak om deze effectief te beheren steeds groter. Dit is waar Infrastructure as Code (IaC) om de hoek komt kijken. IaC is het proces van beheer en beschikbaarstelling van infrastructuur via code, in plaats van via handmatige processen. Dit zorgt voor meer consistentie, snelheid en betrouwbaarheid bij het beheer van de infrastructuur. Een van de populairste tools voor IaC is Teraform.

## Wat is Teraform?

**Teraform** is een open-source infrastructure as code software tool waarmee gebruikers infrastructuur als code kunnen schrijven, plannen en creëren. Teraform is ontwikkeld door HashiCorp en stelt gebruikers in staat om infrastructuur te beheren voor verschillende cloud providers, waaronder AWS, Azure en Google Cloud Platform. Met Teraform kunnen gebruikers hun infrastructuur als code definiëren in configuratiebestanden, de code toepassen om de infrastructuur te creëren of bij te werken, en vervolgens de infrastructuur vernietigen wanneer deze niet langer nodig is.

## Voordelen van het gebruik van Teraform

Het gebruik van Teraform voor infrastructuur als code toepassingen biedt verschillende voordelen, waaronder:

- **Efficiëntie en snelheid:** Teraform maakt sneller en efficiënter infrastructuurbeheer mogelijk doordat handmatige processen niet meer nodig zijn.

- Consistentie:** Door code te gebruiken om infrastructuur te definiëren, zorgt Teraform voor consistentie in verschillende omgevingen.

- Schaalbaarheid:** Teraform maakt het mogelijk de infrastructuur eenvoudig te schalen om aan groeiende eisen te voldoen.

- **Samenwerking:** Teraform configuratiebestanden kunnen versiebeheer krijgen en worden gedeeld door teamleden, wat de samenwerking vergemakkelijkt.

- Kostenbesparingen:** De mogelijkheid van Teraform om eenvoudig resources te leveren en te verwijderen kan leiden tot kostenbesparingen.

## Aan de slag met Teraform

Om met Teraform aan de slag te gaan, moet u:

1. **Download Teraform:** Teraform kan worden gedownload van de[official website](https://www.terraform.io/downloads.html)

2. **Maak een configuratiebestand:** Teraform gebruikt configuratiebestanden die zijn geschreven in HashiCorp Configuration Language (HCL) of JSON. Het configuratiebestand definieert de infrastructuur die u wilt aanmaken, bijwerken of verwijderen.

Om Terraform te gebruiken, moet een configuratiebestand worden gemaakt om de gewenste infrastructuur te definiëren. Het configuratiebestand specificeert de aan te maken resources, hun eigenschappen en hun afhankelijkheden.

Configuratiebestanden kunnen worden geschreven in HashiCorp Configuration Language (HCL), een taal die is ontworpen om menselijk leesbaar en gemakkelijk te leren te zijn, of in JSON-formaat. De HCL-syntaxis is vergelijkbaar met die van andere programmeertalen, met blokken, attributen en waarden.

Hier is een voorbeeld van een basis Terraform configuratiebestand in HCL formaat dat een AWS EC2 instantie creëert:

```HCL
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```
In dit voorbeeld specificeert het configuratiebestand de aws provider en maakt het een aws_instance resource aan met een Amazon Machine Image (AMI) en een instance type.

Voor een meer geavanceerd voorbeeld zie het volgende voorbeeld voor het gebruik van Terraform om systemen te configureren met behulp van VMWare:
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

In dit voorbeeld specificeert het configuratiebestand de vsphere provider en maakt het een vsphere_virtual_machine resource aan met een opgegeven naam, map, aantal CPU's, hoeveelheid geheugen, gastbesturingssysteem, SCSI-type en schijfinstellingen. Ook wordt de virtuele machine gekloond vanuit een opgegeven sjabloon.

Het configuratiebestand gebruikt ook gegevensblokken om de vSphere-infrastructuur te bevragen naar informatie over het datacenter, de datastore en de netwerkinterface die door de virtuele machine moeten worden gebruikt.

Zodra het configuratiebestand is aangemaakt, kan het worden gebruikt om infrastructuurbronnen aan te maken, bij te werken of te verwijderen.

3. **Initialiseer Teraform:** Nadat u een configuratiebestand hebt gemaakt, kunt u Teraform initialiseren door het volgende uit te voeren`terraform init` commando. Dit zal alle noodzakelijke plugins en modules downloaden.

Als u bijvoorbeeld een configuratiebestand hebt met de naam`main.tf` in een directory met de naam`terraform-example` kunt u Terraform initialiseren door het volgende commando uit te voeren in de`terraform-example` map:```terraform init```

Dit zal alle noodzakelijke plugins en modules downloaden die in het configuratiebestand zijn gespecificeerd.

1. **Plan en Infrastructuur toepassen:** Na initialisatie kunt u de`terraform plan` commando om te zien welke veranderingen in de infrastructuur zullen worden aangebracht, en pas dan de veranderingen toe met het`terraform apply` commando.

Na de initialisatie kunt u plannen welke wijzigingen in de infrastructuur zullen worden aangebracht met behulp van het commando`terraform plan` commando. Dit laat zien welke bronnen worden aangemaakt, bijgewerkt of verwijderd. Als u bijvoorbeeld een configuratiebestand hebt met de naam`main.tf` in een directory met de naam`terraform-example` kunt u uw infrastructuurwijzigingen plannen door het volgende commando uit te voeren:

```terraform plan```

Dit toont u een voorbeeld van de wijzigingen die in de infrastructuur zullen worden aangebracht.

Als u tevreden bent met de wijzigingen, kunt u ze toepassen met de knop`terraform apply` commando. Als u bijvoorbeeld een configuratiebestand hebt met de naam`main.tf` in een directory met de naam`terraform-example` kunt u uw infrastructuurwijzigingen toepassen door het volgende commando uit te voeren:

```terraform apply```

Hiermee worden de wijzigingen toegepast op uw infrastructuur. Merk op dat het toepassen van wijzigingen enige tijd kan duren, afhankelijk van de grootte en complexiteit van uw infrastructuur.

## Beste praktijken voor het gebruik van Teraform

Om ervoor te zorgen dat u Teraform effectief gebruikt, kunt u overwegen deze best practices te volgen:

- **Gebruik versiebeheer:** Sla uw Teraform configuratiebestanden op in versiebeheer om samenwerking mogelijk te maken en ervoor te zorgen dat wijzigingen worden bijgehouden.

- Gebruik modules van Teraform om code te organiseren en te hergebruiken.

- **Scheid configuraties:** Scheid uw configuraties per omgeving (bijv. dev, staging, prod) om consistentie te waarborgen en configuratiedrift te voorkomen.

- **Valideer wijzigingen:** Voordat u wijzigingen toepast op de infrastructuur, valideert u deze met behulp van de`terraform plan` commando.

## Conclusie

Teraform is een krachtige infrastructure as code tool die sneller, efficiënter en consistenter infrastructuurbeheer mogelijk maakt. Door Teraform te gebruiken kunnen organisaties tijd en geld besparen en tegelijkertijd de samenwerking en schaalbaarheid verbeteren. Door best practices te volgen en met Teraform aan de slag te gaan, kunt u van deze voordelen profiteren en uw infrastructuur effectiever beheren.

---

**Referenties:**

-[Teraform Official Website](https://www.terraform.io/)
-[Teraform Documentation](https://www.terraform.io/docs/index.html)
-[AWS Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/)
