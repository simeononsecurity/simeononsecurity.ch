---
title: "Een alleen-lezen Active Directory-inventaris maken met PowerShell"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Inventariseer Active Directory-OU's, gebruikers en computers met afgebakende PowerShell-query's. Exporteer controleerbare CSV-bestanden zonder directoryobjecten te wijzigen."
genre: ["Active Directory", "PowerShell", "System Administration"]
tags: ["Active Directory-inventaris", "PowerShell AD-inventaris", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "zoekbasis", "alleen-lezen AD", "AD-gebruikersexport", "AD-computerexport", "AD-OU-export", "Export-Csv", "RSAT", "directory-audit", "AD-rapportage", "OU-inventaris", "Windows Server", "PowerShell-script", "AD-module", "directoryhygiëne"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Een Active Directory-structuur met gebruikers-, computer- en organisatie-eenheidrecords die naar drie controlebestanden worden geëxporteerd."
coverCaption: "Beperk de query tot de juiste scope en exporteer alleen de velden die je nodig hebt."
---

Een Active Directory-opschoning begint met een betrouwbare lijst van bestaande objecten. Deze **alleen-lezen inventaris** verzamelt organisatie-eenheden, gebruikers en computers binnen één gekozen scope. De inventaris exporteert drie bestanden met door komma's gescheiden waarden (CSV) voor controle, zonder directoryobjecten te wijzigen. Bescherm deze bestanden, want namen en apparaatgegevens geven informatie over je omgeving.

<!--more-->

## Belangrijkste punten

- **Kies een scope:** Query één organisatie-eenheid voordat je uitbreidt naar een heel domein.
- **Gebruik leesopdrachten:** `Get-ADOrganizationalUnit`, `Get-ADUser` en `Get-ADComputer` halen objecten op.
- **Selecteer velden:** Exporteer alleen de eigenschappen die je voor de taak nodig hebt.
- **Controleer de uitvoer:** Vergelijk aantallen en voorbeeldrijen voordat je op een rapport vertrouwt.

## Voordat je begint

Je hebt een Windows-beheerhost nodig met werkende DNS en netwerktoegang tot een domeincontroller, de PowerShell-module **ActiveDirectory**, een account met goedgekeurde leesrechten voor de geselecteerde objecten en een beveiligde map voor de CSV-uitvoer. Op een Windows-client komt de module uit de Active Directory-hulpprogramma's in Remote Server Administration Tools (RSAT). De [Active Directory-moduulgids](/articles/active-directory-module-powershell-installation-usage-guide/) van deze site beschrijft de installatie. Microsoft biedt de [cmdletreferentie](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) voor de module en [installatieopties voor RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). Deze gids gebruikt Windows PowerShell-syntaxis en wijzigt geen directoryobjecten.

Directorymachtigingen blijven van toepassing. Microsoft legt in zijn richtlijnen voor [bevoorrechte accounts](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory) uit dat toegangsbeheerlijsten voor objecten geverifieerde gebruikers vaak leestoegang geven tot algemene informatie, terwijl gevoelige velden en wijzigingen worden beperkt. Gebruik eerst een goedgekeurd account en een test-OU. Verhoog je rechten niet tot Domain Admin om de inventaris te laten slagen.

> **Waarschuwing:** De CSV-bestanden bevatten account- en computernamen. Bewaar ze op een goedgekeurde locatie, beperk de toegang en verwijder extra kopieën na de controle. Publiceer geen ruwe export en voeg die niet toe aan een openbare issue.

## De zoekbasis kiezen

Een **organisatie-eenheid (OU)** groepeert directoryobjecten. De **distinguished name (DN)** geeft de positie ervan in de directorystructuur aan. De parameter `-SearchBase` beperkt een query tot een gekozen DN. Zonder een bewuste scope kan een breed filter veel meer objecten opleveren dan je nodig hebt.

Laad eerst de module en bekijk de DN van het huidige domein:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft documenteert [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) en de domeinuitvoer ervan. Zoek de OU die je wilt controleren voordat je de zoekbasis instelt:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Kopieer de exacte DN uit het resultaat. Vervang voor de resterende voorbeelden deze documentatiewaarde door de DN van jouw OU:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` is een domein voor documentatie. Kopieer de DN niet naar een live query. Als je bewust een inventaris voor het hele domein nodig hebt, stel `$SearchBase` dan in op de domein-DN en vermeld die ruimere scope in het rapport. De [referentie voor Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) van Microsoft documenteert `-Filter` en `-SearchBase`.

## OU's, gebruikers en computers inventariseren

Begin met aantallen. Zo merk je snel of je een verkeerde zoekbasis gebruikt of onverwacht geen resultaten krijgt:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` betekent alle overeenkomende objecten binnen de zoekbasis. Microsoft beschrijft [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) en [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) als opdrachten om objecten op te halen. Een aantal van nul kan kloppen, maar controleer de DN, machtigingen en het doeldomein voordat je de inventaris als volledig beschouwt.

Bekijk nu enkele rijen in de console. Sla de geselecteerde velden op, zodat de voorbeeldweergave en de latere CSV-export dezelfde kolommen gebruiken:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

Vraag voor computers alleen het extra veld voor het besturingssysteem op als je controle dat nodig heeft:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

De parameter `-Properties` vraagt eigenschappen op buiten de standaardset van de cmdlet. De [referentie voor de computer-cmdlet](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) van Microsoft beschrijft deze parameter. Behandel namen van besturingssystemen als directorygegevens, niet als bewijs van de momenteel geïnstalleerde versie. Een computerobject kan verouderd zijn of het kenmerk kan niet zijn bijgewerkt.

## Een controleerbare CSV exporteren

Kies een goedgekeurde uitvoermap met voldoende ruimte. De volgende opdrachten schrijven **lokale CSV-bestanden** en laten directoryobjecten ongewijzigd. Voer ze in die map uit. `-NoClobber` voorkomt dat een bestaand bestand wordt overschreven. Gebruik voor elke uitvoering een nieuwe map of bestandsnaam.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

De [referentie voor Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) van Microsoft licht `-NoTypeInformation`, `-Encoding` en `-NoClobber` toe. Open elk CSV-bestand in een teksteditor of goedgekeurde spreadsheetapp. Controleer de kopregel, enkele rijen en het aantal records aan de hand van de eerdere tellingen. Een mislukte opdracht of een bestand van nul bytes bewijst niet dat het rapport volledig is.

> **Verwacht resultaat:** Je hebt drie CSV-bestanden met OU-, gebruikers- en computerrecords binnen de gekozen scope. De aantallen rijen en voorbeeldrecords komen overeen met die scope.

## Controleren zonder objecten te wijzigen

Gebruik de inventaris om gerichte vragen te beantwoorden: Welke OU bevat een computer? Welke gebruikers zijn uitgeschakeld? Welke apparaten hebben nog een eigenaar nodig? Noteer bevindingen in een apart controlerapport. Ga er niet van uit dat een `Enabled`-waarde bepaalt of een account nog nodig is. Verwijder of schakel een object niet uit op basis van alleen een export.

Leg voor een terugkerend rapport de querydatum, het domein, de OU-DN, de geselecteerde eigenschappen, de uitvoerder en de CSV-locatie vast. Controleer bij het vergelijken van twee exports of ze dezelfde scope en velden gebruiken. Anders kan een verschil door de query komen in plaats van door een wijziging in de directory.

Dit is een **inventaris**, geen controle van bevoorrechte accounts of aanmeldingsactiviteit. Microsoft merkt op dat Active Directory-eigenschappen en machtigingen per object en omgeving verschillen. Controleer een kenmerk voor het besturingssysteem of een weergavenaam bij de systeemeigenaar voordat je handelt. De [Active Directory-beveiligingsgids](/articles/active-directory-security-best-practices/) van deze site behandelt de bredere beveiligingsmaatregelen.

## Problemen oplossen

- **Module wordt niet geïmporteerd:** Controleer of de Active Directory-hulpprogramma's uit RSAT of de Windows Server-beheerhulpprogramma's op de host zijn geïnstalleerd. Volg de [installatiegids voor de module](/articles/active-directory-module-powershell-installation-usage-guide/).
- **Query levert geen objecten op:** Controleer de exacte DN, het huidige domein, de inhoud van de OU en de leesmachtigingen. Probeer een bekende kleine OU voordat je de scope vergroot.
- **Een eigenschap is leeg:** Controleer of het kenmerk bestaat en of je account het mag lezen. Vul ontbrekende velden niet met aannames in.
- **Export meldt dat het bestand bestaat:** `-NoClobber` heeft het eerdere rapport beschermd. Kies een nieuwe bestandsnaam of map en voer de opdracht opnieuw uit.
- **Aantallen wijken af van de verwachting:** Controleer of gebruikers of computers in een andere OU staan, of je scope is gewijzigd en of de directory tijdens de query veranderde.

## Volgende stappen

Bewaar het ruwe CSV-bestand gedurende de afgesproken controleperiode op een beveiligde locatie. Deel alleen de velden die de controleur nodig heeft. Plan wijzigingen via het normale goedkeurings- en rollbackproces nadat eigenaren de bevindingen hebben geverifieerd. Voer dezelfde inventaris met dezelfde scope opnieuw uit na goedgekeurde wijzigingen om het resultaat te controleren.
