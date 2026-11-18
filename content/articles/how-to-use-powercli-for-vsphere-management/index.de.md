---
title: "PowerCLI für die vSphere-Verwaltung meistern"
date: 2023-08-02
lastmod: 2026-11-14
toc: true
draft: false
description: "Erfahren Sie, wie Sie VMware vSphere mit PowerCLI verwalten, Aufgaben automatisieren und produktiver arbeiten."
genre: ["Technologie", "Virtualisierung", "VMware", "IT-Verwaltung", "Automatisierung", "Befehlszeilenschnittstelle", "Skripting", "Systemadministration", "Cloud Computing", "Rechenzentrumsverwaltung"]
tags: ["PowerCLI", "VMware PowerCLI", "PowerCLI installieren", "PowerCLI-Installation", "PowerCLI herunterladen", "PowerCLI-Download", "PowerCLI mit vCenter verbinden", "vSphere-Verwaltung", "Verwaltung virtueller Maschinen", "Hostverwaltung", "Automatisierung", "Skripting", "Virtualisierung", "vCenter-Server", "ESXi-Hosts", "Datastore-Verwaltung", "Netzwerkadapterverwaltung", "Erstellung virtueller Maschinen", "Entfernen virtueller Maschinen", "Einstellungen virtueller Maschinen", "Hostressourcenverwaltung", "CPU-Zuweisung", "Speicherzuweisung", "Speichereinstellungen", "PowerCLI-Beispiele", "PowerCLI-Dokumentation", "IT-Verwaltung", "Systemadministration", "Cloud Computing"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Eine Illustration zeigt eine Person, die PowerCLI-Befehle zur Verwaltung virtueller Maschinen und Hosts in einer vSphere-Umgebung verwendet."
coverCaption: "Verbessern Sie Ihre vSphere-Verwaltung mit PowerCLI"
---

## Einführung

**PowerCLI** ist eine von **VMware** bereitgestellte **Befehlszeilenschnittstelle (CLI)**. Administratoren können damit **VMware-vSphere-Umgebungen verwalten und automatisieren**. Die zahlreichen **Cmdlets** vereinfachen Verwaltungsaufgaben und steigern die Produktivität, unabhängig von Ihrer Erfahrung. Dieser Artikel behandelt Installation, Verbindung mit vCenter und den effektiven Einsatz von PowerCLI.

______

## PowerCLI installieren

Installieren Sie PowerCLI auf Ihrem Computer:

1. **Laden Sie** das Installationsprogramm von der offiziellen VMware-Website herunter. Den Link finden Sie in der [PowerCLI-Dokumentation](https://code.vmware.com/web/dp/tool/vmware-powercli). Wählen Sie die passende Version für Ihr Betriebssystem.
2. **Starten Sie** das Installationsprogramm und folgen Sie den Anweisungen. Wählen Sie Installationsort und Optionen.
3. Klicken Sie auf „Finish“, um die Installation abzuschließen. Danach können Sie PowerCLI verwenden.

______

## Mit PowerCLI eine Verbindung zu vCenter herstellen

Verbinden Sie sich nach der Installation mit Ihrem vCenter-Server, um Ihre virtuelle Infrastruktur mit PowerCLI-Cmdlets zu verwalten.

1. Starten Sie PowerCLI über das Startmenü oder die Desktopverknüpfung.
2. Verbinden Sie sich mit vCenter über diesen Befehl:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Ersetzen Sie `<vCenter IP or hostname>` durch die tatsächliche IP-Adresse oder den Hostnamen Ihres vCenter-Servers.

3. Geben Sie bei Aufforderung die Anmeldedaten eines Kontos mit ausreichenden Berechtigungen ein.
4. Prüfen Sie die Verbindung mit einem einfachen Befehl wie **Get-VMHost**. Eine Liste Ihrer ESXi-Hosts bestätigt die erfolgreiche Verbindung.

______

## PowerCLI zur vSphere-Verwaltung verwenden

Nach der Verbindung mit vCenter stehen Ihnen häufige Verwaltungsaufgaben zur Verfügung.

### Informationen abrufen

PowerCLI bietet Cmdlets zum Abrufen von Informationen über Ihre vSphere-Umgebung:

- **Get-VM**: ruft Informationen zu virtuellen Maschinen ab.
- **Get-VMHost**: ruft Informationen zu ESXi-Hosts ab.
- **Get-Datastore**: ruft Informationen zu Datastores ab.
- **Get-NetworkAdapter**: ruft Informationen zu Netzwerkadaptern ab.

Mit Parametern filtern und formatieren Sie die Ausgabe.

### Aufgaben automatisieren

PowerCLI automatisiert wiederkehrende Aufgaben. Wenige Codezeilen führen komplexe Vorgänge gleichzeitig für mehrere Objekte aus.

#### Snapshots aller VMs in einem Ordner erstellen

```PowerShell
## Alle virtuellen Maschinen auf einem bestimmten Host ausschalten
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Einen Snapshot aller virtuellen Maschinen in einem bestimmten Ordner erstellen
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Das Skript zeigt, wie PowerCLI alle virtuellen Maschinen eines Hosts ausschaltet und Snapshots der VMs in einem Ordner erstellt.

#### Alle VMs in einem Ordner sicher herunterfahren

```PowerShell
## Den Ordner abrufen, der die auszuschaltenden virtuellen Maschinen enthält
$folder = Get-Folder -Name "MyFolder"

## Alle virtuellen Maschinen im angegebenen Ordner abrufen
$vms = Get-VM -Location $folder

## Alle virtuellen Maschinen geordnet herunterfahren
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

Das Skript fährt alle virtuellen Maschinen im angegebenen Ordner ordnungsgemäß herunter. `Get-Folder` findet den Ordner und `Get-VM` ruft die enthaltenen VMs ab. Eine `foreach`-Schleife prüft jede VM. Bei „PoweredOn“ startet `Shutdown-VMGuest` das geregelte Herunterfahren. `-Confirm:$false` überspringt die Rückfrage.

So lassen sich alle VMs in einem Ordner geordnet herunterfahren. Mit PowerCLI-Skripten erstellen Sie Automatisierungsabläufe für Ihre Anforderungen.

### Virtuelle Maschinen und Hosts verwalten

PowerCLI unterstützt verschiedene Verwaltungsaufgaben:

- **Virtuelle Maschinen erstellen und entfernen**: Verwenden Sie **`New-VM`** und **`Remove-VM`**. **[Cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** nimmt bei der Erstellung Parameter für CPU, Arbeitsspeicher, Datenträger und Netzwerk entgegen.
- **VM-Einstellungen ändern**: Ändern Sie CPU, Arbeitsspeicher, Datenträger und Netzwerk. **[Cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** ändert etwa die CPU- und Speicherzuweisung.
- **Hostressourcen verwalten**: Verwalten Sie CPU, Arbeitsspeicher, Netzwerk und Speicher. **[Cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** ändert Netzwerkeinstellungen und Speicher des Hosts.

Dies sind einige Möglichkeiten zur vSphere-Verwaltung mit PowerCLI. Die vielen Cmdlets automatisieren und vereinfachen Verwaltungsaufgaben.

## Fazit

**PowerCLI** ist ein nützliches Werkzeug zur Verwaltung und Automatisierung von VMware-vSphere-Umgebungen. Seine Cmdlets vereinfachen Verwaltungsaufgaben und steigern die Produktivität. Nach der Installation und Verbindung mit vCenter können Sie Informationen abrufen, Aufgaben automatisieren sowie virtuelle Maschinen und Hosts effizient verwalten.

Entdecken Sie PowerCLI und vereinfachen Sie Ihre vSphere-Verwaltung.


## Quellen
- [PowerCLI-Dokumentation](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: VMware-PowerCLI-Cmdletreferenz](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: VMware-PowerCLI-Cmdletreferenz](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
