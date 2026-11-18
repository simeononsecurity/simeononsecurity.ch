---
title: "PowerCLI beheersen voor vSphere-beheer"
date: 2023-08-02
lastmod: 2026-11-14
toc: true
draft: false
description: "Leer VMware vSphere beheren met PowerCLI, taken automatiseren en productiever werken."
genre: ["Technologie", "Virtualisatie", "VMware", "IT-beheer", "Automatisering", "Opdrachtregelinterface", "Scripting", "Systeembeheer", "Cloudcomputing", "Datacenterbeheer"]
tags: ["PowerCLI", "VMware PowerCLI", "PowerCLI installeren", "PowerCLI-installatie", "PowerCLI downloaden", "PowerCLI-download", "PowerCLI verbinden met vCenter", "vSphere-beheer", "Virtuele machines beheren", "Hosts beheren", "Automatisering", "Scripting", "Virtualisatie", "vCenter Server", "ESXi-hosts", "Datastores beheren", "Netwerkadapters beheren", "Virtuele machines maken", "Virtuele machines verwijderen", "Instellingen voor virtuele machines", "Hostbronnen beheren", "CPU-toewijzing", "Geheugentoewijzing", "Opslaginstellingen", "PowerCLI-voorbeelden", "PowerCLI-documentatie", "IT-beheer", "Systeembeheer", "Cloudcomputing"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Illustratie van iemand die PowerCLI-opdrachten gebruikt om virtuele machines en hosts in een vSphere-omgeving te beheren."
coverCaption: "Verbeter vSphere-beheer met PowerCLI"
---

## Inleiding

**PowerCLI** is een **opdrachtregelinterface (CLI)** van **VMware** waarmee beheerders **VMware vSphere-omgevingen beheren en automatiseren**. De uitgebreide set **cmdlets** vereenvoudigt beheertaken en verhoogt de productiviteit, voor beginners en ervaren gebruikers. Dit artikel behandelt de installatie, verbinding met vCenter en het effectieve gebruik van PowerCLI.

______

## PowerCLI installeren

Installeer PowerCLI op je computer:

1. **Download** de PowerCLI-installer van de officiële VMware-website. De link staat in de [PowerCLI-documentatie](https://code.vmware.com/web/dp/tool/vmware-powercli). Kies de versie voor je besturingssysteem.
2. **Start** de installer en volg de instructies. Kies de installatiemap en opties.
3. Klik op “Finish” om de installatie af te ronden. PowerCLI is klaar voor gebruik.

______

## Verbinding maken met vCenter via PowerCLI

Maak na de installatie verbinding met je vCenter-server om de virtuele infrastructuur met PowerCLI-cmdlets te beheren.

1. Start PowerCLI via het Startmenu of de snelkoppeling op het bureaublad.
2. Voer deze opdracht uit om verbinding te maken:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Vervang `<vCenter IP or hostname>` door het echte IP-adres of de hostnaam van je vCenter-server.

3. Voer de aanmeldgegevens in van een account met voldoende rechten voor vCenter-beheer.
4. Controleer de verbinding met bijvoorbeeld **Get-VMHost**. De lijst met ESXi-hosts bevestigt dat de verbinding werkt.

______

## PowerCLI gebruiken voor vSphere-beheer

Na verbinding met vCenter kun je algemene beheertaken uitvoeren.

### Informatie ophalen

PowerCLI bevat cmdlets voor informatie over je vSphere-omgeving:

- **Get-VM**: haalt informatie over virtuele machines op.
- **Get-VMHost**: haalt informatie over ESXi-hosts op.
- **Get-Datastore**: haalt informatie over datastores op.
- **Get-NetworkAdapter**: haalt informatie over netwerkadapters op.

Gebruik parameters om uitvoer te filteren en op te maken.

### Taken automatiseren

PowerCLI automatiseert terugkerende taken. Met enkele regels code voer je complexe bewerkingen uit op meerdere objecten.

#### Snapshots maken van alle VM's in een map

```PowerShell
## Alle virtuele machines op een bepaalde host uitschakelen
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Een momentopname maken van alle virtuele machines in een bepaalde map
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Dit script laat zien hoe je VM's op een host uitschakelt en snapshots maakt van de VM's in een map.

#### Alle VM's in een map veilig afsluiten

```PowerShell
## De map ophalen met de virtuele machines die worden uitgeschakeld
$folder = Get-Folder -Name "MyFolder"

## Alle virtuele machines in de opgegeven map ophalen
$vms = Get-VM -Location $folder

## Alle virtuele machines netjes afsluiten
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

Het script zoekt de map met `Get-Folder` en haalt de VM's erin op met `Get-VM`. De `foreach`-lus controleert elke VM. Bij de status “PoweredOn” start `Shutdown-VMGuest` een nette afsluiting. `-Confirm:$false` slaat de bevestigingsvraag over. Zo sluit je alle VM's in de map ordelijk af. PowerCLI-scripts helpen je automatisering aan te passen aan je behoeften.

### Virtuele machines en hosts beheren

PowerCLI ondersteunt verschillende beheertaken:

- **Virtuele machines maken en verwijderen**: gebruik **`New-VM`** en **`Remove-VM`**. **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** accepteert CPU-, geheugen-, schijf- en netwerkparameters.
- **VM-instellingen wijzigen**: pas CPU, geheugen, schijf en netwerk aan. **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** wijzigt de CPU- en geheugentoewijzing.
- **Hostbronnen beheren**: beheer CPU, geheugen, netwerk en opslag. **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** wijzigt netwerk- en opslaginstellingen van de host.

Dit zijn enkele voorbeelden. De ruime cmdlet-set van PowerCLI automatiseert en vereenvoudigt vSphere-beheertaken.

## Conclusie

**PowerCLI** is een nuttig hulpmiddel voor beheer en automatisering van VMware vSphere. De cmdlets vereenvoudigen beheertaken en verhogen de productiviteit. Na installatie en verbinding met vCenter kun je informatie ophalen, taken automatiseren en VM's en hosts efficiënt beheren.

Verken PowerCLI om vSphere-beheer te vereenvoudigen.


## Bronnen
- [PowerCLI-documentatie](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: referentie voor VMware PowerCLI-cmdlet](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: referentie voor VMware PowerCLI-cmdlet](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
