---
title: "PowerShell Scripting voor beginners: Een stap voor stap gids"
draft: false
toc: true
date: 2023-02-25
description: "Leer de basis van PowerShell scripting en ga aan de slag met automatisering met behulp van deze stap-voor-stap handleiding."
tags: ["PowerShell", "scripting", "Windows", "automatisering", "cmdlets", "modules", "lussen", "voorwaardelijke verklaringen", "functies", "beste praktijken", "foutopsporing", "testen", "variabelen", "PowerShell ISE", "PowerShell Remoting", "Microsoft-technologieën", "IT", "computerbeheer", "codering", "administratieve taken"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "Een stripfiguurtje dat een script vasthoudt en voor een computer staat met PowerShell prompt, wat duidt op gemak in PowerShell scripting voor beginners."
coverCaption: ""
---
 PowerShell Scripting voor beginners**

PowerShell is een krachtige commandoregel en scripttaal ontwikkeld door Microsoft. Het biedt een groot aantal opdrachten en functies voor het beheren en automatiseren van verschillende aspecten van het Windows-besturingssysteem en andere Microsoft-technologieën. In dit artikel behandelen we de basisbeginselen van PowerShell-scripting voor beginners en geven we een stapsgewijze handleiding om aan de slag te gaan.

## Inleiding tot PowerShell

PowerShell is een commandoregel-shell waarmee gebruikers het Windows-besturingssysteem en andere Microsoft-technologieën kunnen automatiseren en beheren. Het biedt een uitgebreide set commando's en functies waarmee gebruikers verschillende administratieve taken kunnen uitvoeren, zoals het beheren van bestanden en mappen, netwerkconfiguratie en systeembeheer. PowerShell ondersteunt ook een scripttaal waarmee gebruikers complexe scripts kunnen maken en verschillende repetitieve taken kunnen automatiseren.

## Aan de slag met PowerShell

### PowerShell installeren

PowerShell is vooraf geïnstalleerd in de meeste versies van het Windows-besturingssysteem. Als u echter een oudere versie van Windows gebruikt of een nieuwere versie van PowerShell nodig hebt, kunt u deze downloaden van de Microsoft-website. Volg deze stappen om PowerShell te downloaden en te installeren:

1. Ga naar de[Microsoft PowerShell website](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) en selecteer de versie van PowerShell die u wilt installeren.
2. Download het installatiebestand en voer het uit.
3. Volg de instructies op het scherm om het installatieproces te voltooien.

### PowerShell starten

Zodra u PowerShell hebt geïnstalleerd, kunt u het starten door de volgende stappen te volgen:

1. Klik op het menu Start en typ "PowerShell" in de zoekbalk.
2. Selecteer "Windows PowerShell" in de zoekresultaten.
3. PowerShell wordt geopend in een nieuw venster.

### Basiskennis PowerShell

PowerShell biedt een opdrachtregelinterface waarmee gebruikers kunnen communiceren met het besturingssysteem. De opdrachten in PowerShell worden cmdlets genoemd, en ze zijn georganiseerd in modules. Met de opdracht Get-Module kunt u een lijst met beschikbare modules bekijken:

```powershell
Get-Module
```

Voor een lijst van beschikbare cmdlets in een module gebruikt u de opdracht Get-Command:
```powershell
Get-Command -Module <module name>
```

Voor hulp bij een cmdlet gebruikt u de opdracht Get-Help:
```powershell
Get-Help <cmdlet name>
```

PowerShell ondersteunt ook aliassen, kortere namen voor cmdlets. Gebruik het commando Get-Alias om een lijst met beschikbare aliassen te bekijken:
```powershell
Get-Alias
```

### PowerShell-scripting
PowerShell-scripting is een krachtige functie waarmee gebruikers verschillende administratieve taken kunnen automatiseren. PowerShell-scripting ondersteunt variabelen, lussen, voorwaardelijke verklaringen en functies, waardoor het een krachtig hulpmiddel voor automatisering is.

#### Variabelen
Variabelen worden gebruikt om gegevens op te slaan in PowerShell-scripts. Variabelen in PowerShell beginnen met een dollarteken ($). Om een waarde aan een variabele toe te wijzen, gebruikt u de volgende syntaxis:
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
- **Do-While loop**: herhaalt een blok code minstens één keer en vervolgens zolang een voorwaarde waar is.
- **orEach loop**: herhaalt een blok code voor elk item in een verzameling.
  
De volgende code gebruikt bijvoorbeeld een For-lus om de nummers 1 tot 5 af te drukken:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Voorwaardelijke verklaringen

Voorwaardelijke verklaringen

Voorwaardelijke verklaringen worden gebruikt om een blok code uit te voeren als een bepaalde voorwaarde waar is. PowerShell ondersteunt de volgende typen voorwaardelijke verklaringen:

- **If statement**: voert een blok code uit als een voorwaarde waar is.
- **If-Else statement**: voert een blok code uit als een voorwaarde waar is, en een ander blok code als de voorwaarde onwaar is.
- **Switch-instructie**: vergelijkt een waarde met een reeks mogelijke overeenkomsten en voert een codeblok uit voor de eerste gevonden overeenkomst.

De volgende code gebruikt bijvoorbeeld een If-instructie om te controleren of een getal groter is dan 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "The number is greater than 5"
}
```
#### Functies
Functies zijn herbruikbare blokken code die een specifieke taak uitvoeren. Functies nemen invoerparameters en geven uitvoerwaarden terug. PowerShell ondersteunt de volgende typen functies:

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
PowerShell ISE (Integrated Scripting Environment) is een grafische gebruikersinterface voor PowerShell-scripts. PowerShell ISE biedt een rijke teksteditor, debuggereedschappen en andere functies die het schrijven en testen van PowerShell-scripts vergemakkelijken. Volg deze stappen om PowerShell ISE te openen:

1. Klik op het menu Start en typ "PowerShell ISE" in de zoekbalk.
2. Selecteer "Windows PowerShell ISE" in de zoekresultaten.
3. PowerShell ISE wordt geopend in een nieuw venster.

### PowerShell Remoting
Met PowerShell Remoting kunnen gebruikers PowerShell-opdrachten en -scripts uitvoeren op externe computers. PowerShell Remoting vereist dat de WinRM-service wordt uitgevoerd op zowel de lokale als de externe computer. Volg deze stappen om PowerShell Remoting in te schakelen:

1. Open een PowerShell-prompt met beheerdersrechten.
2. Voer de volgende opdracht uit om PowerShell Remoting in te schakelen:
```powershell
   Enable-PSRemoting -Force
```
3. Voer het volgende commando uit om de externe computer toe te voegen aan de TrustedHosts lijst:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Herstart de WinRM service
```powershell
Restart-Service WinRM
```

Gebruik het cmdlet Invoke-Command om een PowerShell-opdracht uit te voeren op een externe computer:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### PowerShell-modules
PowerShell-modules zijn verzamelingen cmdlets, functies en scripts die zijn ontworpen om specifieke taken uit te voeren. PowerShell-modules kunnen worden geïnstalleerd en beheerd via de PowerShell Gallery, een centrale opslagplaats voor PowerShell-modules.

Als u een PowerShell-module wilt installeren vanuit de PowerShell Gallery, gebruikt u de volgende opdracht:
```powershell
Install-Module <module name>
```

Gebruik de opdracht Get-InstalledModule om een lijst met geïnstalleerde PowerShell-modules te bekijken:
```powershell
Get-InstalledModule
```

### Beste praktijken voor PowerShell-scripting
Bij het schrijven van PowerShell-scripts is het belangrijk best practices te volgen om ervoor te zorgen dat de scripts veilig, betrouwbaar en onderhoudbaar zijn. Hier zijn enkele best practices om in gedachten te houden:

Gebruik beschrijvende namen voor variabelen: Gebruik variabele namen die duidelijk hun doel aangeven.
Gebruik commentaar: Gebruik commentaar om het doel van de code uit te leggen.
- Gebruik foutafhandeling**: Gebruik foutafhandeling om fouten en uitzonderingen netjes af te handelen.
- **Test scripts grondig**: Test scripts grondig om er zeker van te zijn dat ze werken zoals verwacht.
- **Gebruik functies en modules**: Gebruik functies en modules om code te organiseren en herbruikbaarheid te verbeteren.
- **Vermijd hardcoding waarden**: Vermijd hardcoding van waarden in het script en gebruik in plaats daarvan parameters of variabelen.
- **Gebruik uitgebreide uitvoer**: Gebruik verbose output om extra informatie te geven over de voortgang van het script.

### Uitwerking van beste praktijken voor PowerShell-scripting

#### Foutafhandeling gebruiken
Foutafhandeling is een cruciaal aspect van PowerShell-scripting, omdat het ervoor zorgt dat het script fouten en uitzonderingen netjes afhandelt. PowerShell biedt verschillende manieren om fouten af te handelen, waaronder de Try-Catch-instructie, de Trap-instructie en de parameter ErrorAction. Het Try-Catch statement wordt gebruikt om uitzonderingen op te vangen en af te handelen, terwijl het Trap statement wordt gebruikt om fouten op te vangen en af te handelen. De parameter ErrorAction wordt gebruikt om te bepalen hoe het script fouten afhandelt.

Hier is een voorbeeld van het gebruik van het Try-Catch statement om een fout netjes af te handelen:
```powershell
try {
    # some code that might throw an error
}
catch {
    Write-Error "An error occurred: $_"
}
```

#### Test Scripts grondig

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
Functies en modules zijn essentieel voor het organiseren van code en het verbeteren van de herbruikbaarheid in PowerShell-scripting. Met functies kunnen gebruikers code groeperen in herbruikbare blokken en met modules kunnen gebruikers code verpakken en delen met anderen. Door functies en modules te gebruiken, kunnen PowerShell-scripts modulairder, efficiënter en beter onderhoudbaar worden gemaakt.

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
Het hardcoderen van waarden in een PowerShell-script maakt het minder flexibel en moeilijker te onderhouden. In plaats van waarden hard te coderen, kunt u het beste parameters of variabelen gebruiken, waarmee gebruikers tijdens runtime waarden aan het script kunnen doorgeven. Door parameters of variabelen te gebruiken, kan het script beter worden hergebruikt en aangepast aan veranderende omstandigheden.

Hier volgt een voorbeeld van het gebruik van een parameter in PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Hello, $name!"
```

#### Verbose uitvoer gebruiken
Verbose uitvoer geeft extra informatie over de voortgang van het script, wat handig kan zijn bij het debuggen en oplossen van problemen. PowerShell biedt het cmdlet Write-Verbose, waarmee gebruikers verbose-informatie naar de console kunnen uitvoeren. Door verbose-uitvoer te gebruiken, kunnen PowerShell-scripts informatiever en gemakkelijker te debuggen worden gemaakt.

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

### Tien Powershell Script Ideeën voor Beginners

- **Geautomatiseerde back-ups**: Maak een script dat het proces van het maken van back-ups van belangrijke bestanden en mappen naar een externe harde schijf of cloudopslagdienst automatiseert.
- **Bestandsbeheer**: Maak een script dat bestanden en mappen organiseert door ze te sorteren in verschillende mappen op basis van bestandstype, grootte of andere criteria.
- **Systeeminformatie**: Maak een script dat systeeminformatie ophaalt, zoals CPU- en geheugengebruik, schijfruimte en netwerkinstellingen, en deze in een overzichtelijk formaat weergeeft.
- **Gebruikersbeheer**: Maak een script dat het toevoegen, wijzigen of verwijderen van gebruikers en groepen in het Windows-besturingssysteem automatiseert.
- **Software installatie**: Maak een script dat software op meerdere computers tegelijk installeert en configureert, wat tijd en moeite bespaart.
- **Netwerkconfiguratie**: Maak een script dat de configuratie van netwerkinstellingen automatiseert, zoals IP-adres, subnetmasker en standaardgateway.
- **Veiligheid**: Maak een script dat beveiligingsinstellingen controleert en bewaakt en de gebruiker waarschuwt als er wijzigingen worden gedetecteerd.
- **Task scheduling**: Maak een script dat terugkerende taken plant en automatiseert, zoals back-ups, updates en systeemscans.
- **Register manipulatie**: Maak een script dat registerwaarden wijzigt of ophaalt voor specifieke sleutels of waarden.
- **Op afstand beheren**: Maak een script waarmee Windows-computers op afstand kunnen worden beheerd, zodat gebruikers opdrachten en scripts kunnen uitvoeren op externe machines.

## Conclusie

PowerShell is een krachtig hulpmiddel voor het beheren en automatiseren van het Windows-besturingssysteem en andere Microsoft-technologieën. In dit artikel hebben we de basisbeginselen van PowerShell-scripting voor beginners behandeld, waaronder het installeren en starten van PowerShell, het gebruik van cmdlets, variabelen, lussen, voorwaardelijke verklaringen en functies, en het gebruik van PowerShell ISE, PowerShell Remoting en PowerShell-modules. Door best practices te volgen kunnen PowerShell-scripts veilig, betrouwbaar en onderhoudbaar zijn. Door oefening kunt u zich bekwamen in PowerShell scripting en diverse administratieve taken met gemak automatiseren.
