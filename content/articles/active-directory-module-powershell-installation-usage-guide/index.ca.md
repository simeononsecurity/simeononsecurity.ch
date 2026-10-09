---
title: "Administració d'Active Directory amb PowerShell"
date: 2023-07-25
toc: true
draft: false
description: Descobreix com instal·lar i utilitzar eficaçment el mòdul d'Active Directory per a PowerShell per simplificar les teves tasques d'administració de Windows Active Directory.
genre:
- Tecnologia
- Windows
- PowerShell
- Active Directory
- Administració
- Scripting
- TI
- Automatització
- Windows Server
- Microsoft
tags:
- mòdul d'Active Directory per a PowerShell
- importar mòdul active directory a PowerShell
- mòdul d'Active Directory per a Windows PowerShell
- instal·lació active directory PowerShell
- instal·lar active directory PowerShell
- PowerShell instal·lar mòdul active directory Windows 10
- instal·lar mòdul active directory PowerShell Windows 10
- obtenir mòdul active directory PowerShell
- administració AD
- Windows Active Directory
- cmdlets de PowerShell
- recuperar informació AD
- crear objectes AD
- modificar objectes AD
- gestionar seguretat AD
- gestió d'usuaris AD
- gestió de grups AD
- gestió d'unitats organitzatives AD
- scripting PowerShell
- administració Windows Server
- Microsoft PowerShell
- automatitzar tasques AD
- instal·lació de mòduls PowerShell
- guia d'administració AD
- gestió d'Active Directory
- gestió de seguretat AD
- automatització PowerShell
- comandes PowerShell d'Active Directory
- referència de cmdlets PowerShell
cover: /img/cover/active-directory-module-powershell-installation-usage-guide.webp
coverAlt: Una il·lustració d'una pantalla d'ordinador mostrant una consola de PowerShell amb cmdlets acolorits, envoltada de representacions abstractes de comptes d'usuari i grups, sobre un fons fosc.
coverCaption: Desbloqueja el poder de l'administració d'Active Directory amb PowerShell.
lastmod: 2026-10-08
---

## Introducció

Avui dia, gestionar i mantenir comptes d'usuari, grups de seguretat i altres recursos en un entorn Windows Active Directory (AD) requereix processos eficients i simplificats. PowerShell, un potent llenguatge de scripting desenvolupat per Microsoft, ofereix el **mòdul d'Active Directory** per facilitar les tasques d'administració d'AD. Aquest mòdul proporciona molts cmdlets que permeten als administradors automatitzar diverses operacions i gestionar AD de manera efectiva. En aquest article, explorarem la instal·lació i l'ús del mòdul d'Active Directory per a PowerShell.

## Instal·lació del mòdul d'Active Directory per a PowerShell

Per començar a utilitzar el mòdul d'Active Directory per a PowerShell, cal assegurar-se que està instal·lat al sistema. El procés d'instal·lació pot variar segons el sistema operatiu. Aquí tens els passos per instal·lar el mòdul a **Windows 10**, **Windows 11** i **Windows Server**:

### Windows 10 i Windows 11 - PowerShell
1. Obre **Windows PowerShell** amb privilegis d'administrador.
2. Executa la següent comanda per instal·lar el mòdul:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Espera que la instal·lació finalitzi. Un cop acabada, podràs començar a utilitzar el mòdul d'Active Directory.

### Windows Server 
1. Obre **Windows PowerShell** amb privilegis d'administrador.
2. Executa la següent comanda per instal·lar el mòdul:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Espera que la instal·lació finalitzi. Un cop acabada, podràs començar a utilitzar el mòdul d'Active Directory.

### Sistemes fora de línia

Els sistemes fora de línia són una mica més complicats. Hi ha diverses maneres, però la que recomanem és mitjançant l'ús del següent script:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Importació del mòdul d'Active Directory a PowerShell

Abans de poder utilitzar el mòdul d'Active Directory a PowerShell, cal importar-lo a la sessió actual. Segueix aquests passos per importar el mòdul:

1. Obre **Windows PowerShell** amb drets d'administrador.
2. Executa la següent comanda per importar el mòdul:

```powershell
Import-Module ActiveDirectory
```

3. El mòdul d'Active Directory s'importarà i ara podràs accedir als seus cmdlets i funcions.

## Ús del mòdul d'Active Directory per a PowerShell

Amb el mòdul d'Active Directory importat, pots aprofitar el seu ampli conjunt de cmdlets per realitzar diverses tasques administratives. Aquí tens una mirada a alguns cmdlets habituals i les seves funcionalitats:

### Recuperació d'informació d'Active Directory

Per gestionar eficaçment un entorn Active Directory (AD), cal recuperar informació sobre diversos objectes AD, com usuaris, grups i unitats organitzatives (OUs). PowerShell proporciona cmdlets potents que simplifiquen aquest procés de recuperació.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps): Aquest cmdlet permet recuperar informació detallada sobre usuaris AD. Pots obtenir atributs com nom d'usuari, nom per mostrar, adreça de correu electrònic i més. Per exemple, per recuperar tots els usuaris els noms d'usuari dels quals comencen per "johndoe", pots executar la següent comanda:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Aquesta comanda retornarà una llista d'objectes d'usuari que coincideixin amb el filtre especificat.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps): Amb el cmdlet Get-ADGroup, pots obtenir informació sobre grups AD. Proporciona accés a detalls com nom del grup, membres, descripció i més. Per exemple, per recuperar tots els grups de seguretat de l'entorn AD, pots executar la següent comanda:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Això proporcionarà una llista de grups de seguretat a l'Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps): El cmdlet Get-ADOrganizationalUnit s'utilitza per recuperar informació sobre les unitats organitzatives (OUs) d'AD. Permet accedir a propietats com nom de la OU, descripció, OU pare i més. Per obtenir totes les OUs del domini, pots utilitzar la següent comanda:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  Executar aquesta comanda mostrarà una llista de totes les OUs a l'Active Directory.

Utilitzant aquests cmdlets potents, pots recuperar fàcilment informació específica sobre usuaris, grups i OUs d'AD, permetent una administració i gestió eficient del teu entorn Active Directory.


Aquests cmdlets permeten recuperar atributs específics, filtrar resultats i realitzar consultes avançades per obtenir la informació desitjada.

### Creació i gestió d'objectes d'Active Directory

Quan treballes amb Active Directory (AD), el mòdul d'Active Directory a PowerShell ofereix cmdlets potents per crear i gestionar objectes AD. Aquí tens una mirada a alguns cmdlets essencials per crear usuaris, grups i unitats organitzatives (OUs) d'AD.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps): Aquest cmdlet permet crear un nou usuari AD. Pots especificar atributs com nom d'usuari, contrasenya, adreça de correu electrònic i més. Per exemple, per crear un nou usuari amb el nom d'usuari "john.doe" i el nom per mostrar "John Doe", pots utilitzar la següent comanda:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Aquesta comanda crearà un nou usuari a l'Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps): El cmdlet New-ADGroup et permet crear un nou grup AD. Pots establir propietats com nom del grup, descripció, àmbit del grup i més. Per crear un nou grup anomenat "Marketing" amb una descripció, pots executar la següent comanda:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Aquesta comanda crearà un nou grup a l'Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps): Amb el cmdlet New-ADOrganizationalUnit, pots crear una nova UO d'AD. Pots especificar propietats com el nom de la UO, la UO pare i més. Per exemple, per crear una nova UO anomenada "Sales" sota la UO "Departments", pots executar la següent comanda:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Aquesta comanda crearà una nova UO a la jerarquia d'Active Directory.

Utilitzant aquests cmdlets, pots crear fàcilment nous usuaris, grups i UO d'AD amb les propietats i configuracions desitjades, permetent una gestió eficient del teu entorn d'Active Directory.


### Modificació d'objectes d'Active Directory

Quan es tracta de modificar les propietats i atributs d'objectes existents d'Active Directory (AD), el mòdul d'Active Directory a PowerShell ofereix diversos cmdlets útils. Aquí tens una visió d'aquests cmdlets per modificar usuaris, grups i unitats organitzatives (UO) d'AD.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps): El cmdlet Set-ADUser permet modificar propietats d'un usuari d'AD. Pots actualitzar atributs com el nom per mostrar, l'adreça de correu electrònic, el número de telèfon i més. Per exemple, per canviar el número de telèfon d'un usuari amb el nom d'usuari "john.doe", pots utilitzar la següent comanda:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Aquesta comanda modificarà el número de telèfon de l'usuari especificat a l'Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps): Amb el cmdlet Set-ADGroup, pots modificar propietats d'un grup d'AD. Pots actualitzar atributs com la descripció del grup, la membresia, l'abast del grup i més. Per canviar la descripció d'un grup anomenat "Marketing" a "Marketing Team", pots executar la següent comanda:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Aquesta comanda actualitzarà la descripció del grup especificat a l'Active Directory.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps): El cmdlet Set-ADOrganizationalUnit permet modificar propietats d'una UO d'AD. Pots canviar atributs com el nom de la UO, la descripció i més. Per exemple, per modificar la descripció d'una UO anomenada "Sales" a "Sales Department", pots executar la següent comanda:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Aquesta comanda actualitzarà la descripció de la UO especificada a la jerarquia d'Active Directory.

Utilitzant aquests cmdlets, pots modificar fàcilment les propietats i atributs dels objectes d'AD, fent les actualitzacions i ajustos necessaris per complir amb els requisits de la teva organització.


### Gestió de la seguretat d'Active Directory

A més de gestionar i administrar objectes d'Active Directory (AD), el mòdul d'Active Directory a PowerShell proporciona cmdlets específicament dissenyats per gestionar aspectes relacionats amb la seguretat d'AD. Aquests cmdlets ajuden els administradors a gestionar eficientment l'accés d'usuaris, les membresies de grups i les tasques relacionades amb contrasenyes dins de l'entorn d'AD.

Aquí tens alguns cmdlets relacionats amb la seguretat que s'utilitzen habitualment:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps): Aquest cmdlet permet afegir membres a un grup d'AD. Especificant el grup d'AD i els comptes d'usuari o grups que vols afegir, pots gestionar fàcilment el control d'accés. Per exemple, per afegir un usuari anomenat "JohnDoe" al grup "Managers", pots utilitzar la següent comanda:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps): Amb aquest cmdlet, pots eliminar membres d'un grup d'AD. Especificant el grup d'AD i els comptes d'usuari o grups que vols eliminar, pots gestionar eficaçment les membresies de grup. Per exemple, per eliminar un usuari anomenat "JaneSmith" del grup "Developers", pots utilitzar la següent comanda:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps): Aquest cmdlet et permet establir la contrasenya d'un usuari d'AD. Especificant el compte d'usuari i proporcionant una nova contrasenya, pots aplicar polítiques de contrasenya i assegurar una autenticació segura de l'usuari. Aquí tens un exemple d'establir una nova contrasenya per a un usuari anomenat "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Utilitzant aquests cmdlets relacionats amb la seguretat, els administradors poden gestionar eficaçment l'accés d'usuaris, les membresies de grups i les polítiques de contrasenyes dins de l'entorn d'Active Directory.

## Exemple d'script del mòdul d'Active Directory per PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## Conclusió

Per concloure, el **mòdul d'Active Directory per PowerShell** és una eina potent que permet una gestió eficient i còmoda de l'Active Directory de Windows. Instal·lant i important el mòdul, tens accés a un conjunt complet de **cmdlets** que simplifiquen diverses tasques relacionades amb AD.

Amb el mòdul d'Active Directory, pots realitzar moltes operacions com recuperar informació sobre objectes d'AD, crear nous objectes, modificar propietats i gestionar la seguretat. Aquest mòdul ajuda els administradors a automatitzar tasques administratives, simplificar fluxos de treball i assegurar el bon funcionament dels entorns d'Active Directory.

Utilitzant **PowerShell** i el **mòdul d'Active Directory**, pots millorar les teves capacitats d'administració d'AD i augmentar l'eficiència dels processos de gestió d'AD. Siguis administrador de sistemes, professional de TI o gestor d'Active Directory, el mòdul d'Active Directory t'equiparà amb les eines necessàries per gestionar eficaçment la teva infraestructura d'AD.

Aprofita el poder de **PowerShell** i el **mòdul d'Active Directory** per simplificar les teves tasques d'administració d'AD, augmentar la productivitat i mantenir un entorn d'Active Directory segur i ben organitzat.

## Referències

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
