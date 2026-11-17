---
title: "Usare Packer per l’infrastruttura come codice: vantaggi e buone pratiche"
date: 2023-05-04
lastmod: 2026-11-16
toc: true
draft: false
description: "Imparate a usare Packer per creare immagini di macchine facili da mantenere e sicure."
tags: ["Packer", "Infrastruttura come codice", "Sviluppo e operazioni", "Automazione", "Sicurezza", "Ripetibilità", "Scalabilità", "Multipiattaforma", "Controllo delle versioni", "Informatica nella nuvola", "Immagini di macchine", "Virtualizzazione", "Gestione della configurazione", "Integrazione continua", "Consegna continua", "Sviluppo software", "Buone pratiche", "Test", "Codice aperto", "Nuvole multiple"]
cover: "/img/cover/A_cartoon-style_image_of_a_packer_creating_different_machines.webp"
coverAlt: "Un'immagine in stile cartone animato di un addetto al confezionamento che crea diverse immagini di macchine per più piattaforme, con un computer portatile e nuvole sullo sfondo."
coverCaption: ""
---

**Introduzione a Packer per le applicazioni di infrastruttura come codice**

**Packer** è un popolare strumento per la creazione di **immagini di macchine** o **modelli di macchine virtuali** che possono essere utilizzati per distribuire ambienti identici su più piattaforme. Consente agli sviluppatori di automatizzare il processo di creazione di immagini per varie piattaforme come **AWS, Google Cloud Platform, Azure e VMware**. Packer è uno strumento open-source creato da HashiCorp, l'azienda dietro a strumenti popolari come Vagrant, Consul e Terraform.

In questo articolo vi presenteremo Packer e vi mostreremo come utilizzarlo per creare immagini macchina per diverse piattaforme. Discuteremo anche i vantaggi dell'uso di Packer e alcune best practice per il suo utilizzo.

## Che cos'è Packer?

Packer è uno strumento che automatizza il processo di creazione di immagini macchina per diverse piattaforme. È uno strumento open-source creato da HashiCorp, l'azienda che ha creato altri strumenti popolari come Vagrant, Consul e Terraform.

Utilizzando Packer, gli sviluppatori possono creare immagini macchina o modelli di macchine virtuali per diverse piattaforme come AWS, Google Cloud Platform, Azure e VMware. Queste immagini macchina possono poi essere utilizzate per distribuire ambienti identici su più piattaforme.

## Vantaggi dell'uso di Packer

L'uso di Packer offre diversi vantaggi, tra cui:

- **Ripetibilità**: Packer crea le immagini macchina sempre nello stesso modo e garantisce coerenza tra gli ambienti.
- **Automazione**: Packer automatizza la creazione delle immagini, fa risparmiare tempo e riduce il rischio di errori umani.
- **Supporto multipiattaforma**: semplifica la creazione di immagini macchina utilizzabili in ambienti diversi.
- **Integrazione con altri strumenti**: Packer si integra con Ansible, Chef e Puppet, così puoi usare gli strumenti che conosci già.
- **Scalabilità**: Packer crea più immagini macchina in parallelo e facilita la crescita del processo.

## Iniziare con Packer

Per iniziare a usare Packer, è necessario scaricarlo e installarlo. Packer è disponibile per Windows, macOS e Linux.

È possibile scaricare Packer dal sito web ufficiale:[https://www.packer.io/downloads](https://www.packer.io/downloads)

Una volta installato Packer, è possibile iniziare a creare immagini della macchina per diverse piattaforme.

## Creare un'immagine macchina con Packer

La creazione di un'immagine macchina con Packer comporta la definizione di un **template** che descrive la configurazione dell'immagine. Il modello è scritto in formato JSON e specifica i passaggi necessari per creare l'immagine macchina.

Ecco un esempio di modello di Packer per la creazione di un'immagine macchina AWS:

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

In questo esempio, il modello specifica che Packer deve creare un'immagine macchina supportata da Amazon EBS utilizzando una AMI di Ubuntu. L'immagine macchina risultante sarà denominata "my-image" con un timestamp aggiunto alla fine.

Una volta definito il modello di Packer, si può usare il comando `packer build` per creare l'immagine del computer:

```bash
$ packer build template.json
```

### AWS AMI con Ansible Provisioner
È possibile utilizzare il provisioner di Ansible con Packer per creare un'immagine della macchina AWS. Ecco un esempio di modello di Packer:

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
In questo esempio, il modello Packer crea un'immagine di macchina AWS e utilizza Ansible per il provisioning. La sezione `provisioners` del modello specifica il playbook Ansible da utilizzare.

### Immagine della piattaforma cloud di Google
È possibile utilizzare Packer anche per creare immagini macchina su Google Cloud Platform. Ecco un esempio di modello Packer:
```json
{
  "builders": [{
    "type": "googlecompute",
    "project_id": "PROJECT_ID",
    "source_image_family": "ubuntu-1604-lts",
    "zone": "us-central1-f",
    "image_name": "my-image",
    "image_description": "La mia immagine personalizzata"
  }],
  "provisioners": [{
    "type": "shell",
    "inline": [
      "echo 'Hello, World!' > /tmp/hello.txt"
    ]
  }]
}
```

Questo modello di Packer crea un'immagine di Google Cloud Platform e utilizza un provisioner shell per aggiungere un file all'immagine. L'immagine macchina risultante sarà denominata "my-image" con la descrizione "La mia immagine personalizzata".

### VMWare

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

In questo esempio, il modello specifica che Packer deve creare un'immagine macchina VMware utilizzando una ISO di un server Ubuntu. L'immagine macchina risultante avrà 4 GB di RAM, 2 CPU e 40 GB di spazio su disco. Durante il provisioning verrà inoltre installato il server web nginx.

Questi sono solo alcuni esempi di ciò che si può fare con Packer. Con Packer è possibile creare immagini macchina per un'ampia gamma di piattaforme e utilizzare una serie di provisioning per configurarle.

## Migliori pratiche per l'uso di Packer

Ecco alcune buone pratiche per l'utilizzo di Packer:

- **Usa il controllo delle versioni**: conserva i modelli Packer nel sistema di controllo per seguire le modifiche e collaborare.
- **Parametrizza i modelli**: usa variabili per renderli riutilizzabili e facili da mantenere.
- **Testa i modelli**: verifica che creino le immagini macchina previste.
- **Segui le buone pratiche di sicurezza**: proteggi gli ambienti creati a partire dalle immagini.
- **Mantieni semplici i modelli**: evita modelli complessi, difficili da mantenere e correggere.
- **Usa il comando `packer init`**: inizializza un nuovo modello con la configurazione necessaria.

## Conclusione

Packer è uno strumento potente per creare immagini di macchine per diverse piattaforme. Offre ripetibilità, automazione, supporto multipiattaforma e scalabilità. Seguendo le migliori pratiche, è possibile utilizzare Packer per creare immagini macchina facili da mantenere e sicure.

In questo articolo vi abbiamo presentato Packer e vi abbiamo mostrato come usarlo per creare immagini macchina per diverse piattaforme. Abbiamo anche discusso i vantaggi dell'uso di Packer e alcune best practice per il suo utilizzo.

Se siete interessati a saperne di più su Packer, consultate la documentazione ufficiale all'indirizzo[https://www.packer.io/docs](https://www.packer.io/docs)

