---
title: "Stăpânește PowerCLI pentru administrarea vSphere"
date: 2023-08-02
lastmod: 2026-11-14
toc: true
draft: false
description: "Află cum să folosești PowerCLI pentru a administra VMware vSphere, a automatiza sarcini și a crește productivitatea."
genre: ["Tehnologie", "Virtualizare", "VMware", "Administrare IT", "Automatizare", "Interfață în linie de comandă", "Scripting", "Administrare de sistem", "Cloud computing", "Administrarea centrelor de date"]
tags: ["PowerCLI", "VMware PowerCLI", "Instalare PowerCLI", "Instalează PowerCLI", "Descarcă PowerCLI", "Descărcare PowerCLI", "Conectare PowerCLI la vCenter", "Administrare vSphere", "Administrarea mașinilor virtuale", "Administrarea gazdelor", "Automatizare", "Scripting", "Virtualizare", "Server vCenter", "Gazde ESXi", "Administrarea datastore-urilor", "Administrarea adaptoarelor de rețea", "Crearea mașinilor virtuale", "Eliminarea mașinilor virtuale", "Setări pentru mașini virtuale", "Resursele gazdei", "Alocare CPU", "Alocare memorie", "Setări de stocare", "Exemple PowerCLI", "Documentație PowerCLI", "Administrare IT", "Administrare de sistem", "Cloud computing"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Ilustrație cu o persoană care folosește comenzi PowerCLI pentru a administra mașini virtuale și gazde într-un mediu vSphere."
coverCaption: "Îmbunătățește administrarea vSphere cu PowerCLI"
---

## Introducere

**PowerCLI** este un instrument de **interfață în linie de comandă (CLI)** oferit de **VMware**. Administratorii îl folosesc pentru a **gestiona și automatiza** mediile **VMware vSphere**. Numeroasele **cmdlet-uri** simplifică sarcinile administrative și cresc productivitatea, indiferent de experiență. Articolul prezintă instalarea, conectarea la vCenter și folosirea eficientă a PowerCLI.

______

## Instalarea PowerCLI

Instalează PowerCLI pe computer:

1. **Descarcă** programul de instalare de pe site-ul oficial VMware. Linkul se află în [documentația PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli). Alege versiunea potrivită sistemului de operare.
2. **Rulează** programul și urmează instrucțiunile de pe ecran. Alege locația și opțiunile dorite.
3. Apasă „Finish” pentru a finaliza instalarea. PowerCLI este gata de folosire.

______

## Conectarea la vCenter cu PowerCLI

După instalare, conectează-te la serverul vCenter pentru a gestiona infrastructura virtuală cu cmdlet-urile PowerCLI.

1. Deschide PowerCLI din meniul Start sau din scurtătura de pe desktop.
2. Rulează comanda de mai jos pentru conectare:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Înlocuiește `<vCenter IP or hostname>` cu adresa IP sau numele real al serverului vCenter.

3. Când ți se solicită, introdu datele unui cont cu privilegii suficiente pentru administrarea vCenter.
4. Verifică legătura folosind o comandă simplă, de exemplu **Get-VMHost**. Lista gazdelor ESXi confirmă conectarea.

______

## Folosirea PowerCLI pentru administrarea vSphere

După conectarea la vCenter, poți efectua sarcini uzuale.

### Obținerea informațiilor

PowerCLI oferă cmdlet-uri pentru a obține informații despre mediul vSphere:

- **Get-VM**: obține informații despre mașinile virtuale.
- **Get-VMHost**: obține informații despre gazdele ESXi.
- **Get-Datastore**: obține informații despre datastore-uri.
- **Get-NetworkAdapter**: obține informații despre adaptoarele de rețea.

Folosește parametri pentru a filtra și formata rezultatele.

### Automatizarea sarcinilor

PowerCLI automatizează sarcini repetitive. Câteva rânduri de cod pot efectua operațiuni complexe asupra mai multor obiecte.

#### Crearea instantaneelor tuturor VM-urilor dintr-un folder

```PowerShell
## Oprește toate mașinile virtuale de pe o gazdă specifică
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Creează un snapshot pentru toate mașinile virtuale dintr-un folder specific
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Scriptul arată cum să oprești VM-urile de pe o gazdă și să creezi instantanee pentru VM-urile dintr-un folder.

#### Oprirea în siguranță a tuturor VM-urilor dintr-un folder

```PowerShell
## Preia folderul care conține mașinile virtuale ce urmează să fie oprite
$folder = Get-Folder -Name "MyFolder"

## Preia toate mașinile virtuale din folderul specificat
$vms = Get-VM -Location $folder

## Oprește controlat toate mașinile virtuale
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

Scriptul găsește folderul cu `Get-Folder`, apoi obține VM-urile din el cu `Get-VM`. Bucla `foreach` verifică fiecare mașină. Dacă starea este „PoweredOn”, `Shutdown-VMGuest` inițiază oprirea normală, iar `-Confirm:$false` omite solicitarea de confirmare. Astfel, VM-urile se opresc ordonat. Scripturile PowerCLI permit fluxuri de automatizare adaptate cerințelor tale.

### Gestionarea mașinilor virtuale și a gazdelor

PowerCLI permite diverse sarcini administrative:

- **Crearea și eliminarea mașinilor virtuale**: folosește **`New-VM`** și **`Remove-VM`**. **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** acceptă parametri pentru CPU, memorie, disc și rețea.
- **Modificarea setărilor VM**: schimbă CPU, memoria, discul și rețeaua. **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** modifică alocarea CPU și memorie.
- **Gestionarea resurselor gazdei**: administrează CPU, memoria, rețeaua și stocarea. **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** schimbă setările de rețea și stocare ale gazdei.

Acestea sunt câteva exemple de administrare vSphere. Colecția amplă de cmdlet-uri PowerCLI automatizează și simplifică sarcinile administrative.

## Concluzie

**PowerCLI** este un instrument util pentru gestionarea și automatizarea mediilor VMware vSphere. Cmdlet-urile simplifică administrarea și cresc productivitatea. După instalare și conectarea la vCenter, poți obține informații, automatiza sarcini și gestiona eficient mașinile virtuale și gazdele.

Explorează PowerCLI pentru a simplifica administrarea vSphere.


## Referințe
- [Documentație PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: referință cmdlet VMware PowerCLI](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: referință cmdlet VMware PowerCLI](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
