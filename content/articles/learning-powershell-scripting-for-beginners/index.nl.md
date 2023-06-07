---
title: "PowerShell Scripting: Een stap-voor-stap handleiding voor beginners om taken te automatiseren"
draft: false
toc: true
date: 2023-02-25
description: "Leer de basis van PowerShell scripting en automatiseer taken met deze stap-voor-stap handleiding voor beginners, waarin cmdlets, loops, functies en meer aan bod komen."
genre: ["Technologie", "Programmeren", "Automatisering", "Windows", "Scripting", "IT", "Administratieve taken", "Computerbeheer", "Software Ontwikkeling", "Codering"]
tags: ["PowerShell-scripting", "PowerShell automatisering", "Windows scripting", "PowerShell cmdlets", "PowerShell-modules", "PowerShell-lussen", "PowerShell voorwaardelijke verklaringen", "PowerShell-functies", "PowerShell best practices", "PowerShell debugging", "PowerShell testen", "PowerShell-variabelen", "PowerShell ISE", "PowerShell Remoting", "Microsoft-technologieën", "IT-automatisering", "computerbeheer", "coderen voor beginners", "administratieve taken", "PowerShell script-ideeën", "geautomatiseerde back-ups", "bestandsbeheer", "systeeminformatie", "gebruikersbeheer", "software-installatie", "netwerkconfiguratie", "veiligheidsautomatisering", "taakplanning", "register manipulatie", "administratie op afstand"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "Een stripfiguurtje dat een script vasthoudt en voor een computer met PowerShell prompt staat, wat duidt op gemak in PowerShell scripting voor beginners"
coverCaption: ""
---
 PowerShell Scripting voor beginners**

PowerShell is een krachtige commandoregel-shell en scripttaal ontwikkeld door Microsoft. Het biedt een breed scala aan opdrachten en functies voor het beheren en automatiseren van verschillende aspecten van het Windows-besturingssysteem en andere Microsoft-technologieën. In dit artikel behandelen we de basisbeginselen van PowerShell-scripting voor beginners en geven we een stapsgewijze handleiding om aan de slag te gaan.

## Inleiding tot PowerShell

**PowerShell** is een commandoregel-shell waarmee gebruikers het Windows-besturingssysteem en andere Microsoft-technologieën kunnen automatiseren en beheren. Het biedt een uitgebreide set commando's en functies waarmee gebruikers verschillende administratieve taken kunnen uitvoeren, zoals het beheren van bestanden en mappen, netwerkconfiguratie en systeembeheer. PowerShell ondersteunt ook een scripttaal waarmee gebruikers complexe scripts kunnen maken en verschillende repetitieve taken kunnen automatiseren.

## Aan de slag met PowerShell

### PowerShell installeren

PowerShell is vooraf geïnstalleerd in de meeste versies van het Windows-besturingssysteem. Als u echter een oudere versie van Windows gebruikt of als u een nieuwere versie van PowerShell nodig hebt, kunt u deze downloaden van de Microsoft-website. Volg deze stappen om PowerShell te downloaden en te installeren:

1. Ga naar de [Microsoft PowerShell website](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) en selecteer de versie van PowerShell die je wilt installeren.
2. Download het installatiebestand en voer het uit.
3. Volg de instructies op het scherm om het installatieproces te voltooien.

### PowerShell starten

Nadat je PowerShell hebt geïnstalleerd, kun je het starten door de volgende stappen te volgen:

1. Klik op het menu Start en typ "PowerShell" in de zoekbalk.
2. Selecteer "Windows PowerShell" in de zoekresultaten.
3. PowerShell wordt geopend in een nieuw venster.

### Basiskennis PowerShell

PowerShell biedt een opdrachtregelinterface waarmee gebruikers kunnen communiceren met het besturingssysteem. De opdrachten in PowerShell worden cmdlets genoemd en ze zijn georganiseerd in modules. Gebruik de opdracht Get-Module om een lijst met beschikbare modules weer te geven:

```powershell
Get-Module
```

Gebruik de opdracht Get-Command om een lijst met beschikbare cmdlets in een module te bekijken:
```powershell
Get-Command -Module <module name>
```

Gebruik de opdracht Get-Help om hulp te krijgen bij een cmdlet:
```powershell
Get-Help <cmdlet name>
```

PowerShell ondersteunt ook aliassen, kortere namen voor cmdlets. Als je een lijst met beschikbare aliassen wilt bekijken, gebruik je de opdracht Get-Alias:
```powershell
Get-Alias
```

### PowerShell-scripting
PowerShell scripting is een krachtige functie waarmee gebruikers verschillende administratieve taken kunnen automatiseren. PowerShell-scripting ondersteunt variabelen, lussen, voorwaardelijke verklaringen en functies, waardoor het een krachtig hulpmiddel voor automatisering is.

#### Variabelen
Variabelen worden gebruikt om gegevens op te slaan in PowerShell-scripts. Variabelen in PowerShell beginnen met een dollarteken ($). Als u een waarde wilt toewijzen aan een variabele, gebruikt u de volgende syntaxis:
```powershell
$variable_name = value
```
Bijvoorbeeld:
```powershell
$name = "John"
```
#### Lussen
Lussen worden gebruikt om een blok code een bepaald aantal keren te herhalen. PowerShell ondersteunt de volgende soorten lussen:

- **For loop**: herhaalt een blok code een bepaald aantal keren.
- **While loop**: herhaalt een blok code zolang een voorwaarde waar is.
- **Do-While loop**: herhaalt een blok code minstens één keer en daarna zolang een voorwaarde waar is.
- **orEach loop**: herhaalt een blok code voor elk item in een verzameling.
  
De volgende code gebruikt bijvoorbeeld een For-lus om de getallen 1 tot en met 5 af te drukken:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Voorwaardelijke verklaringen

Voorwaardelijke verklaringen

Voorwaardelijke verklaringen worden gebruikt om een blok code uit te voeren als een bepaalde voorwaarde waar is. PowerShell ondersteunt de volgende typen voorwaardelijke verklaringen:

- **If-instructie**: voert een blok code uit als een voorwaarde waar is.
- **If-Else-instructie**: voert een blok code uit als een voorwaarde waar is en een ander blok code als de voorwaarde onwaar is.
- **Switch-instructie**: vergelijkt een waarde met een reeks mogelijke overeenkomsten en voert een codeblok uit voor de eerste overeenkomst die wordt gevonden.

De volgende code gebruikt bijvoorbeeld een If-instructie om te controleren of een getal groter is dan 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "The number is greater than 5"
}
```
#### Functies
Functies zijn herbruikbare blokken code die een specifieke taak uitvoeren. Functies nemen invoerparameters en retourneren uitvoerwaarden. PowerShell ondersteunt de volgende typen functies:

- **Script-blok**: een blok code dat kan worden uitgevoerd.
- **Geavanceerde functie**: een functie die metagegevens en parametervalidatie bevat.

De volgende code definieert bijvoorbeeld een functie die twee getallen optelt:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "The result is $result"
```
### PowerShell ISE
PowerShell ISE (Integrated Scripting Environment) is een grafische gebruikersinterface voor PowerShell-scripts. PowerShell ISE biedt een rijke teksteditor, foutopsporingstools en andere functies die het schrijven en testen van PowerShell-scripts vergemakkelijken. Voer de volgende stappen uit om PowerShell ISE te openen:

1. Klik op het menu Start en typ "PowerShell ISE" in de zoekbalk.
2. Selecteer "Windows PowerShell ISE" in de zoekresultaten.
3. PowerShell ISE wordt geopend in een nieuw venster.

### PowerShell Remoting
Met PowerShell Remoting kunnen gebruikers PowerShell-commando's en -scripts uitvoeren op externe computers. PowerShell Remoting vereist dat de WinRM-service wordt uitgevoerd op zowel de lokale als de externe computer. Voer de volgende stappen uit om PowerShell Remoting in te schakelen:

1. Open een PowerShell-prompt met beheerdersrechten.
2. Voer de volgende opdracht uit om PowerShell Remoting in te schakelen:
```powershell
   Enable-PSRemoting -Force
```
3. Voer het volgende commando uit om de externe computer toe te voegen aan de TrustedHosts lijst:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Herstart de WinRM-service
```powershell
Restart-Service WinRM
```

Gebruik het cmdlet Invoke-Command om een PowerShell-opdracht uit te voeren op een externe computer:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### PowerShell-modules
PowerShell-modules zijn verzamelingen cmdlets, functies en scripts die zijn ontworpen om specifieke taken uit te voeren. PowerShell-modules kunnen worden geïnstalleerd en beheerd via de PowerShell Gallery, een centrale opslagplaats voor PowerShell-modules.

Gebruik de volgende opdracht om een PowerShell-module te installeren vanuit de PowerShell Gallery:
```powershell
Install-Module <module name>
```

Gebruik de opdracht Get-InstalledModule om een lijst met geïnstalleerde PowerShell-modules weer te geven:
```powershell
Get-InstalledModule
```

### Beste praktijken voor PowerShell-scripting

Bij het schrijven van **PowerShell scripts** is het belangrijk om best practices te volgen om ervoor te zorgen dat de scripts **veilig**, **betrouwbaar** en **onderhoudbaar** zijn. Hier volgen enkele best practices om in gedachten te houden:

- **Gebruik beschrijvende namen voor variabelen**: Gebruik variabele namen die duidelijk hun doel aangeven.
- **Gebruik commentaar**: Gebruik commentaar om het doel van de code uit te leggen.
- **Gebruik foutafhandeling**: Gebruik foutafhandeling om fouten en uitzonderingen netjes af te handelen. De `Try...Catch...Finally` construct in PowerShell kun je uitzonderingen afhandelen en de juiste acties ondernemen. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Scripts grondig testen**: Test scripts grondig om ervoor te zorgen dat ze werken zoals verwacht. Je kunt **Pester**, een testframework voor PowerShell, gebruiken om eenheidstests voor je scripts te schrijven en uit te voeren. [Pester Documentation](https://pester.dev/)
- **Gebruik functies en modules**: Gebruik functies en modules om code te organiseren en herbruikbaarheid te verbeteren. Met functies kunt u uw code opdelen in kleinere, hanteerbare stukken, terwijl modules een manier bieden om uw code te verpakken en te verspreiden. [About Functions](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [About Modules](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Vermijd het coderen van waarden**: Vermijd het hardcoden van waarden in het script en gebruik in plaats daarvan parameters of variabelen. Dit maakt je scripts flexibeler en herbruikbaarder. Je kunt parameters aan je scripts doorgeven met de `param` trefwoord. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Use verbose output** gebruiken: Gebruik verbose uitvoer om extra informatie te geven over de voortgang van het script. U kunt de `Write-Verbose` cmdlet om uitgebreide berichten weer te geven tijdens het uitvoeren van het script. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

Als u deze best practices volgt, kunt u efficiëntere en beter onderhoudbare PowerShell-scripts schrijven, waardoor uw productiviteit toeneemt en de stabiliteit van uw automatiseringstaken wordt gegarandeerd.

### Uitwerking van best practices voor PowerShell-scripting

#### Foutafhandeling gebruiken
Foutafhandeling is een kritisch aspect van PowerShell-scripting, omdat het ervoor zorgt dat het script fouten en uitzonderingen netjes afhandelt. PowerShell biedt verschillende manieren om fouten af te handelen, waaronder de Try-Catch-instructie, de Trap-instructie en de parameter ErrorAction. De Try-Catch-instructie wordt gebruikt om uitzonderingen op te vangen en af te handelen, terwijl de Trap-instructie wordt gebruikt om fouten op te vangen en af te handelen. De parameter ErrorAction wordt gebruikt om te bepalen hoe het script fouten afhandelt.

Hier is een voorbeeld van het gebruik van het Try-Catch statement om een fout netjes af te handelen:
```powershell
try {
    # some code that might throw an error
}
catch {
    Write-Error "An error occurred: $_"
}
```

#### Testscripts grondig

Het testen van PowerShell-scripts is essentieel om ervoor te zorgen dat ze werken zoals verwacht. PowerShell biedt verschillende testtools en frameworks, zoals Pester, waarmee gebruikers tests voor hun scripts kunnen schrijven en uitvoeren. Deze tools helpen bij het identificeren en isoleren van problemen in de code en zorgen ervoor dat het script aan de gewenste eisen voldoet.

Hier volgt een voorbeeld van het gebruik van Pester om een PowerShell-script te testen:
```powershell
Describe "My PowerShell Script" {
    It "Does something" {
        # some code that should return the expected result
        $result = Do-Something
        $result | Should -Be "expected result"
    }
}
```

#### Functies en modules gebruiken
Functies en modules zijn essentieel voor het organiseren van code en het verbeteren van de herbruikbaarheid in PowerShell scripting. Functies stellen gebruikers in staat om code te groeperen in herbruikbare blokken, terwijl modules gebruikers in staat stellen om code te verpakken en te delen met anderen. Door functies en modules te gebruiken, kunnen PowerShell-scripts modulairder, efficiënter en beter onderhoudbaar worden gemaakt.

Hier volgt een voorbeeld van het gebruik van een functie in PowerShell:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "There are $count processes running."
```

#### Vermijd hardcodering van waarden
Het hardcoderen van waarden in een PowerShell script maakt het minder flexibel en moeilijker te onderhouden. In plaats van waarden hard te coderen, kun je het beste parameters of variabelen gebruiken, waarmee gebruikers tijdens runtime waarden aan het script kunnen doorgeven. Door parameters of variabelen te gebruiken, kan het script beter herbruikbaar worden gemaakt en worden aangepast aan veranderende omstandigheden.

Hier volgt een voorbeeld van het gebruik van een parameter in PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Hello, $name!"
```

#### Verbose uitvoer gebruiken
Verbose uitvoer geeft extra informatie over de voortgang van het script, wat handig kan zijn bij het debuggen en oplossen van problemen. PowerShell biedt het cmdlet Write-Verbose waarmee gebruikers verbose-informatie naar de console kunnen uitvoeren. Door verbose-uitvoer te gebruiken, kunnen PowerShell-scripts informatiever en eenvoudiger te debuggen worden gemaakt.

Hier volgt een voorbeeld van het gebruik van verbose-uitvoer in PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "Getting processes..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "There are $count processes running."
```

### Tien PowerShell Script-ideeën voor beginners

Als je een beginner bent in PowerShell scripting, zijn hier tien scriptideeën om je op weg te helpen:

- **Geautomatiseerde back-ups**: Maak een script dat het proces van het maken van back-ups van belangrijke bestanden en mappen naar een externe harde schijf of cloudopslagdienst automatiseert. Je kunt de `Copy-Item` cmdlet om bestanden te kopiëren en het `Start-Job` cmdlet om het back-upproces op de achtergrond uit te voeren. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **Bestandsbeheer**: Maak een script dat bestanden en mappen organiseert door ze in verschillende mappen te sorteren op basis van bestandstype, grootte of andere criteria. Je kunt de `Get-ChildItem` cmdlet om bestanden op te halen en de `Move-Item` cmdlet om ze naar de gewenste locatie te verplaatsen. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **Systeeminformatie**: Maak een script dat systeeminformatie ophaalt, zoals CPU- en geheugengebruik, schijfruimte en netwerkinstellingen, en dit weergeeft in een makkelijk te lezen formaat. Je kunt de `Get-WmiObject` cmdlet om systeeminformatie te verzamelen en op te maken met `Format-Table` of `Out-GridView` [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **Gebruikersbeheer**: Maak een script dat het toevoegen, wijzigen of verwijderen van gebruikers en groepen in het Windows-besturingssysteem automatiseert. Je kunt de `New-LocalUser` `Set-LocalUser` en `Remove-LocalUser` cmdlets om gebruikers te beheren en de `New-LocalGroup` `Add-LocalGroupMember` en `Remove-LocalGroup` cmdlets om groepen te beheren. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **Software-installatie**: Maak een script dat software op meerdere computers tegelijk installeert en configureert, waardoor je tijd en moeite bespaart. U kunt de `Invoke-Command` cmdlet om installatieopdrachten uit te voeren op computers op afstand. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **Netwerkconfiguratie**: Maak een script dat het proces voor het configureren van netwerkinstellingen automatiseert, zoals IP-adres, subnetmasker en standaardgateway. Je kunt de `Set-NetIPAddress` `Set-NetIPInterface` en `Set-DnsClientServerAddress` cmdlets om netwerkinstellingen te configureren. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Veiligheid**: Maak een script dat de beveiligingsinstellingen controleert en bewaakt en de gebruiker waarschuwt als er wijzigingen worden gedetecteerd. U kunt de `Get-AuditPolicy` cmdlet om auditbeleidslijnen op te halen en de `Send-MailMessage` cmdlet om e-mailmeldingen te versturen. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **Taken plannen**: Maak een script dat terugkerende taken plant en automatiseert, zoals back-ups, updates en systeemscans. U kunt de `Register-ScheduledTask` cmdlet om geplande taken te maken en de `Start-ScheduledTask` cmdlet om ze uit te voeren. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **Registry manipulatie**: Maak een script dat de registerwaarden voor specifieke sleutels of waarden wijzigt of ophaalt. Je kunt de `Get-ItemProperty` en `Set-ItemProperty` cmdlets voor interactie met het register. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **Op afstand beheren**: Maak een script waarmee Windows-computers op afstand kunnen worden beheerd, zodat gebruikers opdrachten en scripts kunnen uitvoeren op computers op afstand. U kunt de `Enter-PSSession` cmdlet of het `Invoke-Command` cmdlet om commando's uit te voeren op computers op afstand. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

Begin met het verkennen van deze scriptideeën om praktische ervaring op te doen en je PowerShell-vaardigheden uit te breiden.

## Conclusie

PowerShell is een krachtig hulpmiddel voor het beheren en automatiseren van het Windows-besturingssysteem en andere Microsoft-technologieën. In dit artikel hebben we de basisbeginselen van PowerShell-scripting voor beginners behandeld, waaronder het installeren en starten van PowerShell, het gebruik van cmdlets, variabelen, lussen, voorwaardelijke verklaringen en functies, en het gebruik van PowerShell ISE, PowerShell Remoting en PowerShell-modules. Door best practices te volgen, kunnen PowerShell scripts veilig, betrouwbaar en onderhoudbaar zijn. Met oefening kunt u zich bekwamen in PowerShell scripting en diverse administratieve taken met gemak automatiseren.
