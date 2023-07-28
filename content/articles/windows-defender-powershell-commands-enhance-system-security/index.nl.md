---
title: "Verhoog de beveiliging van uw systeem met Windows Defender PowerShell-commando's"
date: 2023-07-27
toc: true
draft: false
description: "Ontdek de kracht van Windows Defender PowerShell-opdrachten en leer hoe u de beveiliging van uw systeem kunt verbeteren met opdrachtregelbediening."
genre: ["Windows Verdediger", "PowerShell-opdrachten", "systeemveiligheid", "commandoregelbesturing", "antivirus", "Windows-besturingssystemen", "bescherming tegen malware", "geavanceerde beveiligingsinstellingen", "beveiligingsactiviteiten automatiseren", "Windows PowerShell"]
tags: ["Technologie", "Cyberbeveiliging", "Besturingssystemen", "Windows", "Commandoregeltools", "Systeembeveiliging", "PowerShell", "Antivirus", "Bescherming tegen malware", "Scripting"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "Een geanimeerde illustratie van een schild dat een computersysteem beschermt tegen verschillende cyberbedreigingen."
coverCaption: "Versterk de beveiliging van uw systeem met Windows Defender PowerShell-commando's."
---

## Introductie

Windows Defender, ontwikkeld door Microsoft, is een geïntegreerde antivirus- en beveiligingsoplossing voor Windows-besturingssystemen. Het biedt een gebruiksvriendelijke interface om beveiligingsinstellingen effectief te beheren. Voor gevorderde gebruikers die de voorkeur geven aan opdrachtregelbediening, biedt Windows Defender echter een set krachtige PowerShell-opdrachten. In dit artikel duiken we in de wereld van **Windows Defender PowerShell-opdrachten** en onderzoeken we hoe ze de systeembeveiliging kunnen verbeteren en meer controle kunnen bieden over uw Windows-omgeving.

## De kracht van Windows Defender PowerShell-opdrachten

Windows Defender PowerShell-opdrachten geven gebruikers de mogelijkheid om geavanceerde beveiligingsbewerkingen uit te voeren met behulp van een opdrachtregelinterface. Deze opdrachten bieden een breed scala aan functionaliteiten, van eenvoudige bewerkingen zoals het scannen op malware tot complexe taken zoals het configureren van geavanceerde beveiligingsinstellingen. Door PowerShell te gebruiken, kunnen gebruikers beveiligingsbewerkingen automatiseren, aangepaste scripts maken en Windows Defender naadloos integreren in hun bestaande workflows.

## Aan de slag met Windows Defender PowerShell

Om toegang te krijgen tot Windows Defender PowerShell-opdrachten, moet u een PowerShell-sessie openen met beheerdersrechten. Zo kunt u aan de slag:

1. Druk op `Win + X` en selecteer **Windows PowerShell (Admin)** in het menu.
2. Als daarom wordt gevraagd, klikt u op **Ja** om de app toe te staan wijzigingen aan te brengen op uw apparaat.

Zodra u een PowerShell-sessie hebt geopend, kunt u de Windows Defender PowerShell-opdrachten gaan gebruiken.

## Algemene Windows Defender PowerShell-opdrachten

### 1. **Get-MpComputerStatus**: De Windows Defender-status controleren

De `Get-MpComputerStatus` geeft een overzicht van de huidige status van Windows Defender op uw systeem, inclusief de versie van de antivirusengine, de laatste scantijd en de realtime beschermingsstatus. Door deze opdracht uit te voeren, kunt u snel de algemene gezondheid van Windows Defender beoordelen en ervoor zorgen dat het optimaal functioneert.

Om de status van Windows Defender te controleren, opent u een PowerShell-sessie met beheerdersrechten en voert u de volgende opdracht uit:

```powershell
Get-MpComputerStatus
```

Dit commando geeft informatie weer zoals:

- **AntivirusEngineVersion**: Het versienummer van de antivirusengine die door Windows Defender wordt gebruikt.
- **LastFullScanTime**: De datum en tijd van de laatste volledige scan die door Windows Defender is uitgevoerd.
- **LastQuickScanTime**: De datum en tijd van de laatste snelle scan die is uitgevoerd door Windows Defender.
- **RealTimeProtectionEnabled**: Geeft aan of realtime bescherming is in- of uitgeschakeld.

De status van Windows Defender regelmatig controleren met `Get-MpComputerStatus` zorgt ervoor dat je op de hoogte blijft van het beschermingsniveau van je systeem tegen mogelijke bedreigingen.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

De `Update-MpSignature` Met de opdracht kunt u de antivirushandtekeningen die door Windows Defender worden gebruikt handmatig bijwerken. Antivirushandtekeningen bevatten cruciale informatie over bekende malware, waardoor Windows Defender effectief bedreigingen kan detecteren en blokkeren. Door deze opdracht uit te voeren, zorgt u ervoor dat uw systeem over de nieuwste handtekeningen beschikt, waardoor een betere bescherming tegen nieuwe bedreigingen wordt geboden.

Als u de handtekeningen van Windows Defender handmatig wilt bijwerken, opent u een PowerShell-sessie met beheerdersrechten en voert u de volgende opdracht uit:

```powershell
Update-MpSignature
```
Deze opdracht start het updateproces, waarbij **Windows Defender** verbinding maakt met **Microsoft-servers** om de nieuwste **antivirushandtekeningen** te downloaden. Zodra de update is voltooid, beschikt Windows Defender over de meest actuele informatie over bekende malware, waardoor het beter in staat is om bedreigingen te identificeren en te elimineren.

Het up-to-date houden van de Windows Defender-handtekeningen is essentieel voor het handhaven van het hoogste niveau van bescherming tegen het steeds veranderende landschap van **malware** en **cyberbedreigingen**. Door de handtekeningen regelmatig bij te werken met `Update-MpSignature` zorgt u ervoor dat Windows Defender uw systeem effectief kan beveiligen.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

De `Set-MpPreference` Met de opdracht kunt u verschillende **Windows Defender** instellingen aanpassen, zodat u het gedrag kunt afstemmen op uw specifieke beveiligingsvereisten. Deze opdracht biedt flexibiliteit bij het configureren van opties zoals **real-time bescherming**, **cloudgebaseerde bescherming** en **netwerkinspectiesysteeminstellingen**.

U kunt bijvoorbeeld realtime bescherming in- of uitschakelen met de opdracht `Set-MpPreference` opdracht. Realtime bescherming controleert je systeem actief op kwaadaardige activiteiten en reageert onmiddellijk op bedreigingen. Voer de volgende opdracht uit om realtime bescherming in te schakelen:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Daarnaast kunt u de opdracht gebruiken om instellingen voor cloudgebaseerde bescherming aan te passen. Cloudgebaseerde bescherming maakt gebruik van cloudbronnen om de detectie van bedreigingen te verbeteren en sneller te reageren op nieuwe bedreigingen. Gebruik de volgende opdracht om cloudgebaseerde bescherming in te schakelen:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Bovendien is de `Set-MpPreference` Met het commando kun je de instellingen van het netwerkinspectiesysteem aanpassen. Het netwerkinspectiesysteem analyseert netwerkverkeer op verdachte activiteiten en potentiële bedreigingen. Voer de volgende opdracht uit om de instellingen van het netwerkinspectiesysteem aan te passen:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Door deze instellingen te verfijnen met `Set-MpPreference` U kunt **Windows Defender** optimaliseren voor uw specifieke beveiligingsbehoeften en zorgen voor een robuuste bescherming tegen malware en andere schadelijke activiteiten.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

De `Start-MpScan` commando is een krachtig hulpmiddel voor het starten van malware scans op je systeem, waarmee je proactief schadelijke bestanden kunt identificeren en elimineren. Dit commando biedt flexibiliteit in het uitvoeren van verschillende soorten scans, waaronder **snelle scans**, **volledige scans** en **gewone scans** met specifieke paden.

Om een **snelle scan** uit te voeren met de `Start-MpScan` voer dan het volgende PowerShell commando uit:

```powershell
Start-MpScan -ScanType QuickScan
```

Een snelle scan richt zich op kritieke gebieden van je systeem waar malware vaak wordt aangetroffen en biedt een snelle beoordeling van potentiële bedreigingen.

Voor een uitgebreidere scan die alle bestanden en mappen op je systeem onderzoekt, kun je een **volledige scan** starten. Voer de volgende opdracht uit om een volledige scan uit te voeren met `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

Een volledige scan zorgt voor grondige detectie en verwijdering van malware van je systeem, maar het kan langer duren om te voltooien in vergelijking met een snelle scan.

Naast de vooraf gedefinieerde scantypen kunt u de `Start-MpScan` kun je aangepaste scans uitvoeren door specifieke paden of bestanden op te geven om te scannen. Je kunt bijvoorbeeld een specifieke map op je systeem scannen met de volgende opdracht:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Deze opdracht start een aangepaste scan op de opgegeven map, zodat u specifieke gebieden van uw systeem kunt scannen op malware.

Door gebruik te maken van de veelzijdigheid van de `Start-MpScan` commando kunt u scans plannen, beveiligingsprocessen automatiseren en zorgen voor regelmatige detectie en beperking van malware op uw systeem.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

De `Get-MpThreatCatalog` commando is een waardevolle bron voor het verkrijgen van gedetailleerde informatie over bekende bedreigingen en hun attributen. Door deze opdracht uit te voeren, krijg je toegang tot een uitgebreide catalogus van bedreigingen, inclusief gegevens over de ernst ervan, bijbehorende bestandsnamen en aanbevolen acties voor beperking.

Om informatie over specifieke bedreigingen op te halen met `Get-MpThreatCatalog` volg deze stappen:

1. Open een PowerShell-sessie met beheerdersrechten.
2. Voer de volgende opdracht uit:

```powershell
   Get-MpThreatCatalog
```
Deze opdracht toont een lijst met bekende bedreigingen samen met de bijbehorende details.

De uitvoer van de `Get-MpThreatCatalog` De opdracht bevat essentiële informatie zoals:

- **ThreatID**: Een unieke identificatiecode voor de bedreiging.
- **Severity**: Geeft het ernstniveau van de bedreiging aan, variërend van Laag tot Ernstig.
- **Naam**: De naam of beschrijving van de bedreiging.
- **Path**: Het pad van het bestand dat aan de bedreiging is gekoppeld.
- **AanbevolenActie**: Geeft richtlijnen voor de aanbevolen actie om de bedreiging te beperken.

Door gebruik te maken van de informatie die is verkregen uit `Get-MpThreatCatalog` kunt u waardevolle inzichten krijgen in potentiële bedreigingen en weloverwogen beslissingen nemen over de juiste acties om ze te beperken. Of het nu gaat om het isoleren, verwijderen of monitoren van een specifieke bedreiging, de gedetailleerde catalogus stelt u in staat om effectief te reageren op beveiligingsincidenten.

Voor meer informatie over het gebruik van `Get-MpThreatCatalog` en het interpreteren van de resultaten, raadpleeg dan de officiële documentatie van Microsoft.

Blijf waakzaam en gebruik regelmatig de `Get-MpThreatCatalog` opdracht om op de hoogte te blijven van het veranderende bedreigingslandschap en de beveiliging van uw systeem te verbeteren.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

De `Add-MpPreference` Met de opdracht uitsluitingen kunt u uitsluitingen toevoegen aan Windows Defender, zodat u het scangedrag en de realtime bescherming kunt aanpassen. Door uitsluitingen toe te voegen, kunt u bestanden, mappen of processen opgeven die Windows Defender moet negeren tijdens beveiligingsscans of realtime bescherming.

Om een uitsluiting toe te voegen met `Add-MpPreference` moet je het pad of de naam opgeven van het bestand, de map of het proces dat je wilt uitsluiten. Hier is een voorbeeld van het toevoegen van een uitsluiting voor een map:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Deze opdracht zorgt ervoor dat Windows Defender het scannen van de opgegeven map overslaat, waardoor onnodige waarschuwingen en mogelijke onderbrekingen van uw workflow worden verminderd.

Uitsluitingen kunnen nuttig zijn in verschillende scenario's, zoals het uitsluiten van vertrouwde toepassingen, ontwikkelomgevingen of specifieke bestanden die valse positieven kunnen veroorzaken. Door gebruik te maken van de flexibiliteit van `Add-MpPreference` kunt u Windows Defender afstemmen op uw specifieke beveiligingsbehoeften en de prestaties optimaliseren.

Bescherm uw systeem effectief en minimaliseer vals-positieven en onnodige scanonderbrekingen door gebruik te maken van de krachtige uitsluitingsmogelijkheden van `Add-MpPreference`

## Conclusie

Windows Defender PowerShell-opdrachten bieden een **robuuste set hulpprogramma's** voor het beheren en verbeteren van de beveiliging van uw Windows-systeem. Door gebruik te maken van deze commando's kunt u *beveiligingsbewerkingen automatiseren*, * geavanceerde instellingen configureren* en Windows Defender naadloos opnemen in uw workflows. Of u nu een **systeembeheerder** of een **krachtige gebruiker** bent, het verkennen van de mogelijkheden van Windows Defender PowerShell-opdrachten kan de beveiliging van uw systeem aanzienlijk verbeteren.

Onthoud dat grote macht grote verantwoordelijkheid met zich meebrengt. Wees voorzichtig bij het gebruik van PowerShell-opdrachten en zorg ervoor dat u de impact van de opdrachten begrijpt voordat u ze uitvoert. Door uw kennis te combineren met de kracht van Windows Defender PowerShell-opdrachten, kunt u proactieve maatregelen nemen om uw systeem te beschermen tegen nieuwe bedreigingen.

## Referenties

1. Microsoft Docs - [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
