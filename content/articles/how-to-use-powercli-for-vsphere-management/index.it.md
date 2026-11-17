---
title: "Padroneggiare PowerCLI per gestire vSphere"
date: 2023-08-02
lastmod: 2026-11-12
toc: true
draft: false
description: "Scopri come usare PowerCLI per gestire VMware vSphere, automatizzare attività e migliorare la produttività."
genre: ["Tecnologia", "Virtualizzazione", "VMware", "Gestione IT", "Automazione", "Interfaccia a riga di comando", "Scripting", "Amministrazione di sistema", "Cloud computing", "Gestione dei data center"]
tags: ["PowerCLI", "VMware PowerCLI", "Installazione PowerCLI", "Installare PowerCLI", "Scaricare PowerCLI", "Download PowerCLI", "Connettere PowerCLI a vCenter", "Gestione vSphere", "Gestione macchine virtuali", "Gestione host", "Automazione", "Scripting", "Virtualizzazione", "Server vCenter", "Host ESXi", "Gestione datastore", "Gestione schede di rete", "Creazione macchine virtuali", "Rimozione macchine virtuali", "Impostazioni macchine virtuali", "Risorse host", "Allocazione CPU", "Allocazione memoria", "Impostazioni archiviazione", "Esempi PowerCLI", "Documentazione PowerCLI", "Gestione IT", "Amministrazione di sistema", "Cloud computing"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Illustrazione di una persona che usa comandi PowerCLI per gestire macchine virtuali e host in un ambiente vSphere."
coverCaption: "Migliora la gestione di vSphere con PowerCLI"
---

## Introduzione

**PowerCLI** è uno strumento di **interfaccia a riga di comando (CLI)** fornito da **VMware** per **gestire e automatizzare** gli ambienti **VMware vSphere**. I suoi numerosi **cmdlet** semplificano le attività amministrative e aumentano la produttività, sia per chi inizia sia per chi ha esperienza. L’articolo illustra installazione, connessione a vCenter e uso efficace di PowerCLI.

______

## Installare PowerCLI

Installa PowerCLI sul computer seguendo questi passaggi:

1. **Scarica** il programma di installazione dal sito ufficiale VMware. Il collegamento è nella [documentazione PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli). Scegli la versione adatta al sistema operativo.
2. **Esegui** il programma e segui le istruzioni. Scegli percorso e opzioni.
3. Fai clic su «Finish» per completare l’installazione. Ora puoi usare PowerCLI.

______

## Connettersi a vCenter con PowerCLI

Dopo l’installazione, collegati al server vCenter per gestire l’infrastruttura virtuale con i cmdlet PowerCLI.

1. Avvia PowerCLI dal menu Start o dal collegamento sul desktop.
2. Esegui questo comando per collegarti:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Sostituisci `<vCenter IP or hostname>` con l’indirizzo IP o il nome host effettivo del server vCenter.

3. Quando richiesto, inserisci le credenziali di un account con privilegi sufficienti per amministrare vCenter.
4. Verifica il collegamento con un comando semplice, ad esempio **Get-VMHost**. L’elenco degli host ESXi conferma la connessione.

______

## Usare PowerCLI per gestire vSphere

Una volta collegato a vCenter, puoi eseguire attività comuni.

### Recuperare informazioni

PowerCLI offre cmdlet per ottenere informazioni sull’ambiente vSphere:

- **Get-VM**: recupera informazioni sulle macchine virtuali.
- **Get-VMHost**: recupera informazioni sugli host ESXi.
- **Get-Datastore**: recupera informazioni sui datastore.
- **Get-NetworkAdapter**: recupera informazioni sulle schede di rete.

Usa i parametri per filtrare e formattare i risultati.

### Automatizzare attività

PowerCLI automatizza le attività ripetitive. Poche righe di codice eseguono operazioni complesse su più oggetti.

#### Creare snapshot di tutte le VM in una cartella

```PowerShell
## Power off all virtual machines on a specific host
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Take a snapshot of all virtual machines in a specific folder
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Questo script mostra come arrestare le VM di un host specifico e creare snapshot per le VM in una cartella.

#### Arrestare in sicurezza tutte le VM di una cartella

```PowerShell
## Retrieve the folder containing the virtual machines to be shutdown
$folder = Get-Folder -Name "MyFolder"

## Retrieve all virtual machines within the specified folder
$vms = Get-VM -Location $folder

## Shutdown all virtual machines gracefully
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

Lo script spegne correttamente tutte le VM della cartella. `Get-Folder` individua la cartella e `Get-VM` recupera le macchine al suo interno. Il ciclo `foreach` controlla ogni VM: se lo stato è «PoweredOn», `Shutdown-VMGuest` avvia lo spegnimento ordinato. `-Confirm:$false` evita la richiesta di conferma.

In questo modo tutte le VM vengono arrestate in ordine. Gli script PowerCLI permettono di creare flussi automatizzati adatti alle tue esigenze.

### Gestire macchine virtuali e host

PowerCLI supporta diverse attività di gestione:

- **Creare e rimuovere macchine virtuali**: usa **`New-VM`** e **`Remove-VM`**. **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** accetta parametri CPU, memoria, disco e rete durante la creazione.
- **Modificare le impostazioni delle VM**: cambia CPU, memoria, disco e rete. **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** consente di modificare l’allocazione CPU e memoria.
- **Gestire le risorse host**: amministra CPU, memoria, rete e archiviazione. **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** modifica le impostazioni di rete e archiviazione dell’host.

Questi sono alcuni esempi di gestione vSphere con PowerCLI. L’ampia raccolta di cmdlet semplifica e automatizza molte attività.

## Conclusione

**PowerCLI** è uno strumento utile per gestire e automatizzare VMware vSphere. I suoi cmdlet semplificano le attività amministrative e migliorano la produttività. Dopo l’installazione e la connessione a vCenter, puoi recuperare informazioni, automatizzare attività e gestire macchine virtuali e host in modo efficiente.

Esplora PowerCLI per semplificare la gestione di vSphere.


## Riferimenti
- [Documentazione PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: riferimento cmdlet VMware PowerCLI](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: riferimento cmdlet VMware PowerCLI](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
