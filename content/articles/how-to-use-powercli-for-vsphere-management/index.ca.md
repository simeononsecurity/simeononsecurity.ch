---
title: "Domina PowerCLI per administrar vSphere"
date: 2023-08-02
lastmod: 2026-11-14
toc: true
draft: false
description: "Aprèn a fer servir PowerCLI per administrar VMware vSphere, automatitzar tasques i millorar la productivitat."
genre: ["Tecnologia", "Virtualització", "VMware", "Gestió de TI", "Automatització", "Interfície de línia d'ordres", "Creació de scripts", "Administració de sistemes", "Computació al núvol", "Gestió de centres de dades"]
tags: ["PowerCLI", "VMware PowerCLI", "Instal·lació de PowerCLI", "Instal·lar PowerCLI", "Baixar PowerCLI", "Descàrrega de PowerCLI", "Connectar PowerCLI a vCenter", "Gestió de vSphere", "Gestió de màquines virtuals", "Gestió d'amfitrions", "Automatització", "Creació de scripts", "Virtualització", "Servidor vCenter", "Amfitrions ESXi", "Gestió de datastores", "Gestió d'adaptadors de xarxa", "Creació de màquines virtuals", "Supressió de màquines virtuals", "Configuració de màquines virtuals", "Recursos de l'amfitrió", "Assignació de CPU", "Assignació de memòria", "Configuració d'emmagatzematge", "Exemples de PowerCLI", "Documentació de PowerCLI", "Gestió de TI", "Administració de sistemes", "Computació al núvol"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Il·lustració d'una persona que fa servir ordres PowerCLI per gestionar màquines virtuals i amfitrions en un entorn vSphere."
coverCaption: "Millora la gestió de vSphere amb PowerCLI"
---

## Introducció

**PowerCLI** és una eina d'**interfície de línia d'ordres (CLI)** de **VMware** que permet als administradors **gestionar i automatitzar** entorns **VMware vSphere**. Els seus nombrosos **cmdlets** simplifiquen les tasques d'administració i milloren la productivitat. Aquest article explica la instal·lació, la connexió a vCenter i l'ús eficaç de PowerCLI.

______

## Instal·lar PowerCLI

Instal·la PowerCLI a l'ordinador:

1. **Baixa** l'instal·lador del lloc oficial de VMware. Trobaràs l'enllaç a la [documentació de PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli). Tria la versió adequada per al sistema operatiu.
2. **Executa** l'instal·lador i segueix les instruccions. Tria la ubicació i les opcions.
3. Prem «Finish» per completar la instal·lació. Ja pots fer servir PowerCLI.

______

## Connectar-se a vCenter amb PowerCLI

Després d'instal·lar PowerCLI, connecta't al servidor vCenter per gestionar la infraestructura virtual amb els cmdlets.

1. Obre PowerCLI des del menú Inici o la drecera de l'escriptori.
2. Executa aquesta ordre per connectar-te:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Substitueix `<vCenter IP or hostname>` per l'adreça IP o el nom de l'amfitrió real del servidor vCenter.

3. Quan se't demani, introdueix les credencials d'un compte amb prou permisos per administrar vCenter.
4. Verifica la connexió amb una ordre senzilla, com **Get-VMHost**. Si apareix la llista d'amfitrions ESXi, la connexió s'ha establert.

______

## Fer servir PowerCLI per gestionar vSphere

Un cop connectat, pots dur a terme tasques habituals.

### Recuperar informació

PowerCLI ofereix cmdlets per consultar l'entorn vSphere:

- **Get-VM**: recupera informació de les màquines virtuals.
- **Get-VMHost**: recupera informació dels amfitrions ESXi.
- **Get-Datastore**: recupera informació dels datastores.
- **Get-NetworkAdapter**: recupera informació dels adaptadors de xarxa.

Fes servir paràmetres per filtrar i donar format als resultats.

### Automatitzar tasques

PowerCLI automatitza tasques repetitives. Unes quantes línies de codi poden executar operacions complexes en diversos objectes.

#### Crear instantànies de totes les VM d'una carpeta

```PowerShell
## Apaga totes les màquines virtuals d’un host concret
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Fes una instantània de totes les màquines virtuals d’una carpeta concreta
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Aquest script mostra com aturar les VM d'un amfitrió concret i crear instantànies de les màquines d'una carpeta.

#### Aturar amb seguretat totes les VM d'una carpeta

```PowerShell
## Recupera la carpeta que conté les màquines virtuals que s’han d’apagar
$folder = Get-Folder -Name "MyFolder"

## Recupera totes les màquines virtuals de la carpeta especificada
$vms = Get-VM -Location $folder

## Apaga totes les màquines virtuals de manera ordenada
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

L'script cerca la carpeta amb `Get-Folder` i n'obté les VM amb `Get-VM`. El bucle `foreach` comprova cada màquina. Si l'estat és «PoweredOn», `Shutdown-VMGuest` inicia l'aturada ordenada i `-Confirm:$false` omet la confirmació. Així pots apagar ordenadament totes les VM de la carpeta. Els scripts de PowerCLI permeten adaptar l'automatització a les teves necessitats.

### Gestionar màquines virtuals i amfitrions

PowerCLI permet diverses tasques de gestió:

- **Crear i suprimir màquines virtuals**: fes servir **`New-VM`** i **`Remove-VM`**. **[ordre New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** accepta paràmetres de CPU, memòria, disc i xarxa.
- **Modificar la configuració de les VM**: canvia CPU, memòria, disc i xarxa. **[ordre Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** modifica l'assignació de CPU i memòria.
- **Gestionar recursos de l'amfitrió**: administra CPU, memòria, xarxa i emmagatzematge. **[ordre Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** modifica la configuració de xarxa i emmagatzematge de l'amfitrió.

Aquests són alguns exemples. Els nombrosos cmdlets de PowerCLI automatitzen i simplifiquen tasques d'administració de vSphere.

## Conclusió

**PowerCLI** és una eina útil per gestionar i automatitzar entorns VMware vSphere. Els cmdlets simplifiquen l'administració i milloren la productivitat. Després d'instal·lar-lo i connectar-te a vCenter, pots obtenir informació, automatitzar tasques i gestionar màquines virtuals i amfitrions amb eficàcia.

Explora PowerCLI per simplificar la gestió de vSphere.


## Referències
- [Documentació de PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: referència del cmdlet VMware PowerCLI](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: referència del cmdlet VMware PowerCLI](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
