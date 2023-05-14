---
title: "Windows-updates stroomlijnen met automatisering met Chocolatey, PSWindowsUpdate en opstartscripts"
date: 2020-07-22
---
 Windows Updates met Chocolatey, PSWindowsUpdate en Startup Scripts**.

In de huidige snelle bedrijfsomgeving is tijd van essentieel belang voor systeembeheerders. Het updaten van Windows machines, een kritisch aspect van systeembeheer, kan een extreem tijdrovende taak zijn die tot een week kan duren, als er genoeg systemen zijn. Echter, met wat hulp van Chocolatey, PSWindowsUpdates en Startup Scripts is het nu mogelijk om updates uit te rollen met slechts een enkele reboot van elke machine, waardoor de tijd die nodig is om updates uit te voeren aanzienlijk wordt verkort.

## Windows updates stroomlijnen met automatisering

Windows-updates zijn essentieel voor het behoud van de stabiliteit en veiligheid van Windows-machines. Het uitvoeren van updates op een groot aantal machines kan een tijdrovende klus zijn, vooral voor systeembeheerders met beperkte middelen. Met behulp van automatiseringstools zoals Chocolatey, PSWindowsUpdate en Startup Scripts kan dit proces echter worden gestroomlijnd, zodat beheerders met minimale inspanning updates kunnen uitvoeren.

### Chocolatey

[Chocolatey](https://chocolatey.org/) is een pakketbeheerder voor Windows die kan worden gebruikt om de installatie van software op Windows-machines te automatiseren. Het is vergelijkbaar met apt-get op Ubuntu of homebrew op macOS, en het kan worden gebruikt om een breed scala aan softwarepakketten te installeren en te beheren. Chocolatey kan worden gebruikt om pakketten stil te installeren, wat betekent dat ze kunnen worden geïnstalleerd zonder tussenkomst van de gebruiker.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) is een PowerShell-module die kan worden gebruikt om de installatie van Windows-updates te automatiseren. Het biedt cmdlets die kunnen worden gebruikt voor het installeren, verwijderen en inventariseren van Windows-updates. PSWindowsUpdate is een krachtig hulpmiddel waarmee Windows-updates op meerdere machines kunnen worden beheerd, waardoor het ideaal is voor systeembeheerders die grote aantallen machines moeten beheren.

### Opstart scripts

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) zijn scripts die kunnen worden gebruikt om taken te automatiseren die moeten worden uitgevoerd wanneer een machine opstart of afsluit. Deze scripts kunnen worden gebruikt om taken uit te voeren zoals het installeren van software, het configureren van instellingen en het beheren van Windows updates.

## Windows updates automatiseren met een enkele herstart

Om Windows updates te automatiseren met behulp van Chocolatey, PSWindowsUpdate en Startup Scripts, kunnen beheerders de onderstaande stap-voor-stap handleiding volgen.

### Het Shutdown Script instellen
Download alle ondersteunende bestanden van de[GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Open de Editor voor lokaal groepsbeleid door op **"Win + R"** te drukken en **"gpedit.msc"** in te typen, gevolgd door **"Ctrl + Shift + Enter"**.
2. Navigeer naar Computer **Configuratie/WindowsinstellingenScripts (Opstarten/Shutdown)**.
3. Dubbelklik in het resultatenvenster op Shutdown.
4. Selecteer het tabblad PowerShell.
5. Klik in het dialoogvenster Shutdown Properties op Add.
6. Typ in het vak Scriptnaam het pad naar het script of klik op Bladeren om "*chocoautomatewindowsupdates.ps1*" te zoeken in de gedeelde map Netlogon op de domeincontroller.
7. Herstart.

Nu hoeft een beheerder alleen nog maar de computer opnieuw op te starten om Windows-updates uit te voeren.

### Het script begrijpen

Het script dat wordt gebruikt om Windows-updates te automatiseren is getiteld "*chocoautomatewindowsupdates.ps1*". Het voert de volgende taken uit:

1. Installeert Chocolatey package manager.
2. Maakt een paar voorkeursinstellingen voor Chocolatey mogelijk.
3. Upgrade alle geïnstalleerde Chocolatey pakketten.
4. Installeert PSWindowsUpdate PowerShell module.
5. Voegt Windows Update service manager toe.
6. Installeert alle beschikbare Windows-updates.
7. Installeert alle ontbrekende stuurprogramma's of updates die vereist zijn door eerder geïnstalleerde updates.

### Voordelen van het automatiseren van Windows-updates

Het automatiseren van Windows-updates met Chocolatey, PSWindowsUpdate en Startup Scripts heeft verschillende voordelen voor systeembeheerders. Deze voordelen omvatten:

- **Tijdbesparend**: Het automatiseren van Windows updates vermindert de tijd die nodig is om updates uit te voeren aanzienlijk. Beheerders hoeven niet langer handmatig op elke machine updates te installeren.
- **Consistentie**: Het automatiseren van Windows-updates zorgt ervoor dat updates consistent op alle machines worden geïnstalleerd. Dit verkleint de kans op fouten en beveiligingsproblemen.
- **Gecentraliseerd beheer**: Door Windows-updates te automatiseren kunnen beheerders updates vanaf een centrale locatie beheren, waardoor het eenvoudiger wordt om bij te houden welke updates zijn geïnstalleerd en welke machines updates nodig hebben.
- **Verhoogde beveiliging**: Het automatiseren van Windows-updates zorgt ervoor dat machines up-to-date blijven met de laatste beveiligingspatches, waardoor het risico op beveiligingslekken afneemt.

### Conclusie

Het automatiseren van Windows-updates met behulp van Chocolatey, PSWindowsUpdate en Startup Scripts is een krachtig hulpmiddel dat systeembeheerders veel tijd en moeite kan besparen. Het zorgt ervoor dat updates consistent en efficiënt worden geïnstalleerd, zodat machines up-to-date zijn met de laatste beveiligingspatches. Door de stappen in deze tutorial te volgen, kunnen beheerders Windows-updates automatiseren met slechts één reboot, waardoor het proces van het updaten van Windows-machines veel sneller en eenvoudiger wordt.
