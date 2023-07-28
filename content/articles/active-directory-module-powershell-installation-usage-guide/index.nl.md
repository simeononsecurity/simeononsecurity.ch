---
title: "Mastering Active Directory Administration met PowerShell: Installatie- en gebruikshandleiding"
date: 2023-07-25
toc: true
draft: false
description: "Ontdek hoe u de Active Directory module voor PowerShell effectief kunt installeren en gebruiken om uw Windows Active Directory beheertaken te stroomlijnen."
genre: ["Technologie", "Windows", "PowerShell", "Active Directory", "Administratie", "Scripting", "IT", "Automatisering", "Windows server", "Microsoft"]
tags: ["Active Directory-module voor PowerShell", "module active directory importeren in PowerShell", "Active Directory-module voor Windows PowerShell", "actieve map PowerShell installeren", "actieve map installeren PowerShell", "PowerShell active directory module installeren Windows 10", "Active Directory installeren PowerShell-module Windows 10", "PowerShell-module voor actieve map ophalen", "AD administratie", "Windows Active Directory", "PowerShell cmdlets", "AD-informatie ophalen", "AD-objecten maken", "AD-objecten wijzigen", "AD-beveiliging beheren", "AD-gebruikersbeheer", "AD groepsbeheer", "AD OR beheer", "PowerShell-scripting", "Windows Server-beheer", "Microsoft PowerShell", "AD-taken automatiseren", "PowerShell-module installeren", "AD administratiegids", "Beheer van Active Directory", "AD beveiligingsbeheer", "PowerShell automatisering", "Active Directory PowerShell-opdrachten", "PowerShell cmdlet referentie"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "Een afbeelding van een netwerk van onderling verbonden servers en gebruikerspictogrammen, die het beheer en de automatisering van Active Directory symboliseert."
coverCaption: "Ontgrendel de kracht van Active Directory-beheer met PowerShell."
---

## Introductie

In het huidige digitale landschap vereist het beheren en onderhouden van gebruikersaccounts, beveiligingsgroepen en andere bronnen in een Windows Active Directory (AD) omgeving efficiënte en gestroomlijnde processen. PowerShell, een krachtige scripttaal ontwikkeld door Microsoft, biedt de **Active Directory module** om AD-administratietaken te vergemakkelijken. Deze module biedt een breed scala aan cmdlets waarmee beheerders verschillende bewerkingen kunnen automatiseren en AD effectief kunnen beheren. In dit artikel gaan we dieper in op de installatie en het gebruik van de Active Directory module voor PowerShell.

## Installatie van de Active Directory-module voor PowerShell

Om te beginnen met het gebruik van de Active Directory module voor PowerShell, moet je ervoor zorgen dat deze is geïnstalleerd op je systeem. Het installatieproces kan verschillen afhankelijk van uw besturingssysteem. Hier volgen de stappen voor de installatie van de module op **Windows 10**, **Windows 11** en **Windows Server**:

### Windows 10 en Windows 11 - PowerShell
1. Open **Windows PowerShell** met beheerdersrechten.
2. Voer de volgende opdracht uit om de module te installeren:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Wacht tot de installatie is voltooid. Zodra de installatie is voltooid, kunt u de Active Directory module gebruiken.

### Windows Server
1. Open **Windows PowerShell** met beheerdersrechten.
2. Voer de volgende opdracht uit om de module te installeren:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Wacht tot de installatie is voltooid. Zodra de installatie is voltooid, kunt u de Active Directory module gebruiken.

### Offline systemen

Offline systemen worden iets gecompliceerder. Er zijn een paar methoden, maar degene die we aanraden is het gebruik van het volgende script:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## De Active Directory-module importeren in PowerShell

Voordat je de Active Directory module kunt gebruiken in PowerShell, moet je deze importeren in je huidige sessie. Volg deze stappen om de module te importeren:

1. Start **Windows PowerShell** met beheerdersrechten.
2. Voer de volgende opdracht uit om de module te importeren:

```powershell
Import-Module ActiveDirectory
```

3. De Active Directory module wordt geïmporteerd en u hebt nu toegang tot de cmdlets en functies.

## De Active Directory-module voor PowerShell gebruiken

Als de Active Directory module is geïmporteerd, kunt u de uitgebreide set cmdlets gebruiken om verschillende beheertaken uit te voeren. Laten we eens kijken naar een aantal veelgebruikte cmdlets en hun functies:

### Opvragen van Active Directory informatie

Om een Active Directory (AD) omgeving effectief te beheren, is het cruciaal om informatie op te halen over verschillende AD objecten, zoals gebruikers, groepen en organisatorische eenheden (OU's). PowerShell biedt krachtige cmdlets die het opvraagproces vereenvoudigen.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) Met dit cmdlet kun je gedetailleerde informatie ophalen over AD-gebruikers. Je kunt attributen opvragen zoals gebruikersnaam, weergavenaam, e-mailadres en meer. Om bijvoorbeeld alle gebruikers op te halen waarvan de gebruikersnaam begint met "johndoe", kun je het volgende commando uitvoeren:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Dit commando geeft een lijst terug van gebruikersobjecten die overeenkomen met het gespecificeerde filter.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) Met het cmdlet Get-ADGroup kun je informatie ophalen over AD-groepen. Het geeft toegang tot details zoals groepsnaam, leden, beschrijving en meer. Om bijvoorbeeld alle beveiligingsgroepen in de AD-omgeving op te halen, kun je het volgende commando uitvoeren:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Dit geeft een lijst met beveiligingsgroepen in de Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) Het cmdlet Get-ADOrganizationalUnit wordt gebruikt om informatie op te halen over AD OU's. Hiermee heb je toegang tot eigenschappen zoals OU naam, beschrijving, OU ouder en meer. Om alle OU's in het domein op te halen, kun je het volgende commando gebruiken:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  Als dit commando wordt uitgevoerd, wordt een lijst met alle OU's in de Active Directory weergegeven.

Door deze krachtige cmdlets te gebruiken, kunt u eenvoudig specifieke informatie ophalen over AD-gebruikers, groepen en OU's, zodat u uw Active Directory-omgeving efficiënt kunt beheren.

{{< inarticle-dark >}}


Met deze cmdlets kun je specifieke attributen ophalen, resultaten filteren en geavanceerde query's uitvoeren om de gewenste informatie op te halen.

### Creëren en beheren van Active Directory objecten

Wanneer u met Active Directory (AD) werkt, biedt de Active Directory-module in PowerShell krachtige cmdlets voor het maken en beheren van AD-objecten. Laten we eens kijken naar enkele essentiële cmdlets voor het maken van AD-gebruikers, groepen en organisatorische eenheden (OU's).

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) Met dit cmdlet kun je een nieuwe AD-gebruiker aanmaken. Je kunt attributen specificeren zoals gebruikersnaam, wachtwoord, e-mailadres en meer. Om bijvoorbeeld een nieuwe gebruiker aan te maken met de gebruikersnaam "john.doe" en de weergavenaam "John Doe", kun je het volgende commando gebruiken:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Deze opdracht maakt een nieuwe gebruiker aan in de Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) Met het cmdlet New-ADGroup kun je een nieuwe AD groep aanmaken. Je kunt eigenschappen instellen zoals groepsnaam, beschrijving, groepsbereik en meer. Om een nieuwe groep met de naam "Marketing" en een beschrijving te maken, kun je het volgende commando uitvoeren:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Dit commando maakt een nieuwe groep aan in de Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) Met het cmdlet New-ADOrganizationalUnit kun je een nieuwe AD OU maken. Je kunt eigenschappen opgeven zoals OU naam, OU ouder en meer. Als je bijvoorbeeld een nieuwe OU met de naam "Sales" wilt maken onder de OU "Departments", kun je het volgende commando uitvoeren:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Deze opdracht maakt een nieuwe OU aan in de Active Directory hiërarchie.

Door gebruik te maken van deze cmdlets kun je eenvoudig nieuwe AD gebruikers, groepen en OU's maken met de gewenste eigenschappen en configuraties, waardoor je je Active Directory omgeving efficiënt kunt beheren.

{{< inarticle-dark >}}


### Active Directory-objecten wijzigen

Als het gaat om het wijzigen van de eigenschappen en kenmerken van bestaande Active Directory (AD)-objecten, biedt de Active Directory-module in PowerShell verschillende handige cmdlets. Laten we eens kijken naar deze cmdlets voor het wijzigen van AD-gebruikers, groepen en organisatorische eenheden (OU's).

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps) Met het Set-ADUser cmdlet kun je eigenschappen van een AD-gebruiker wijzigen. Je kunt eigenschappen zoals de weergavenaam, het e-mailadres, het telefoonnummer en meer wijzigen. Om bijvoorbeeld het telefoonnummer van een gebruiker met de gebruikersnaam "john.doe" te wijzigen, kunt u de volgende opdracht gebruiken:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Dit commando wijzigt het telefoonnummer van de opgegeven gebruiker in de Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps) Met het Set-ADGroup cmdlet kun je eigenschappen van een AD groep wijzigen. Je kunt attributen zoals groepsbeschrijving, lidmaatschap, groepsbereik en meer bijwerken. Om de beschrijving van een groep met de naam "Marketing" te wijzigen in "Marketing Team", kun je het volgende commando uitvoeren:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Met deze opdracht wordt de beschrijving van de opgegeven groep in de Active Directory bijgewerkt.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps) Met het cmdlet Set-ADOrganizationalUnit kun je eigenschappen van een AD OU wijzigen. Je kunt kenmerken zoals de OU naam, beschrijving en meer wijzigen. Om bijvoorbeeld de beschrijving van een OU met de naam "Sales" te wijzigen in "Sales Department", kun je de volgende opdracht uitvoeren:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Met deze opdracht wordt de beschrijving van de opgegeven OU in de Active Directory-hiërarchie bijgewerkt.

Door deze cmdlets te gebruiken, kunt u eenvoudig de eigenschappen en kenmerken van AD-objecten wijzigen en de nodige updates en aanpassingen maken om te voldoen aan de vereisten van uw organisatie.

{{< inarticle-dark >}}


### Beveiliging van Active Directory beheren

Naast het beheren en administreren van Active Directory (AD)-objecten, biedt de Active Directory-module in PowerShell cmdlets die specifiek zijn ontworpen om beveiligingsgerelateerde aspecten van AD af te handelen. Met deze cmdlets kunnen beheerders efficiënt gebruikerstoegang, groepslidmaatschappen en wachtwoordgerelateerde taken binnen de AD-omgeving beheren.

Hier volgen enkele veelgebruikte cmdlets voor beveiliging:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps) Met dit cmdlet kun je leden toevoegen aan een AD-groep. Door de AD-groep en de gebruikersaccounts of groepen die je wilt toevoegen op te geven, kun je eenvoudig de toegangscontrole beheren. Om bijvoorbeeld een gebruiker met de naam "JohnDoe" toe te voegen aan de groep "Managers", kun je het volgende commando gebruiken:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps) Met dit cmdlet kun je leden verwijderen uit een AD-groep. Door de AD-groep en de gebruikersaccounts of groepen die je wilt verwijderen op te geven, kun je effectief groepslidmaatschappen beheren. Om bijvoorbeeld een gebruiker met de naam "JaneSmith" te verwijderen uit de groep "Developers", kun je het volgende commando gebruiken:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps) Met dit cmdlet kun je het wachtwoord voor een AD-gebruiker instellen. Door het gebruikersaccount op te geven en een nieuw wachtwoord in te stellen, kun je het wachtwoordbeleid afdwingen en zorgen voor een veilige gebruikersauthenticatie. Hier is een voorbeeld van het instellen van een nieuw wachtwoord voor een gebruiker met de naam "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Door deze beveiligingsgerelateerde cmdlets te gebruiken, kunnen beheerders effectief gebruikerstoegang, groepslidmaatschappen en wachtwoordbeleid beheren binnen de Active Directory omgeving.

## Voorbeeld van Active Directory module script voor PowerShell
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

## Conclusie

Concluderend kan worden gesteld dat de **Active Directory module voor PowerShell** een krachtig hulpmiddel is waarmee Windows Active Directory efficiënt en gemakkelijk kan worden beheerd. Door de module te installeren en te importeren, krijg je toegang tot een uitgebreide set **cmdlets** die verschillende AD-gerelateerde taken vereenvoudigen.

Met de Active Directory module kunt u een breed scala aan bewerkingen uitvoeren, zoals het ophalen van informatie over AD-objecten, het maken van nieuwe objecten, het wijzigen van eigenschappen en het beheren van beveiliging. Deze module stelt beheerders in staat om administratieve taken te automatiseren, workflows te stroomlijnen en het soepel functioneren van Active Directory omgevingen te garanderen.

Door gebruik te maken van **PowerShell** en de **Active Directory module**, kunt u uw AD beheermogelijkheden uitbreiden en de efficiëntie van AD beheerprocessen verbeteren. Of u nu een systeembeheerder, IT professional of Active Directory manager bent, de Active Directory module voorziet u van de benodigde tools om uw AD infrastructuur effectief te beheren.

Gebruik de kracht van **PowerShell** en de **Active Directory module** om uw AD beheertaken te stroomlijnen, uw productiviteit te verhogen en een veilige en goed georganiseerde Active Directory omgeving te onderhouden.

{{< inarticle-dark >}}

## Referenties

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
