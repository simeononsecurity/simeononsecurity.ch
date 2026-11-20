---
title: "Windows Defender PowerShell-opdrachten voor systeembeveiliging"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Ontdek de kracht van Windows Defender PowerShell-opdrachten en leer hoe u de beveiliging van uw systeem kunt verbeteren met opdrachtregelbediening."
genre: ["Windows Defender", "PowerShell-opdrachten", "systeemveiligheid", "commandoregelbesturing", "antivirus", "Windows-besturingssystemen", "bescherming tegen malware", "geavanceerde beveiligingsinstellingen", "beveiligingsactiviteiten automatiseren", "Windows PowerShell"]
tags: ["Technologie", "Cyberbeveiliging", "Besturingssystemen", "Windows", "Commandoregeltools", "Systeembeveiliging", "PowerShell", "Antivirus", "Bescherming tegen malware", "Scripts schrijven"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "Een geanimeerde illustratie van een schild dat een computersysteem beschermt tegen verschillende cyberbedreigingen."
coverCaption: "Versterk de beveiliging van uw systeem met Windows Defender PowerShell-commando's."
---

## Introductie

Windows Defender, ontwikkeld door Microsoft, is een geïntegreerde antivirus- en beveiligingsoplossing voor Windows-besturingssystemen. Het biedt een gebruiksvriendelijke interface om beveiligingsinstellingen effectief te beheren. Voor gevorderde gebruikers die de voorkeur geven aan opdrachtregelbediening, biedt Windows Defender echter een set krachtige PowerShell-opdrachten. In dit artikel duiken we in de wereld van **Windows Defender PowerShell-opdrachten** en onderzoeken we hoe ze de systeembeveiliging kunnen verbeteren en meer controle kunnen bieden over uw Windows-omgeving.

## De kracht van Windows Defender PowerShell-opdrachten

Windows Defender PowerShell-opdrachten geven gebruikers de mogelijkheid om geavanceerde beveiligingsbewerkingen uit te voeren met behulp van een opdrachtregelinterface. Deze opdrachten bieden een breed scala aan functionaliteiten, van eenvoudige bewerkingen zoals het scannen op malware tot complexe taken zoals het configureren van geavanceerde beveiligingsinstellingen. Door PowerShell te gebruiken, kunnen gebruikers beveiligingsbewerkingen automatiseren, aangepaste scripts maken en Windows Defender naadloos integreren in hun bestaande workflows.

## Aan de slag met Windows Defender PowerShell

Om toegang te krijgen tot Windows Defender PowerShell-opdrachten, moet u een PowerShell-sessie openen met beheerdersrechten. Zo kunt u aan de slag:

1. Druk op `Win + X` en selecteer **Windows PowerShell (Admin)** (als beheerder) in het menu.
2. Als daarom wordt gevraagd, klikt u op **Yes** (Ja) om de app toe te staan wijzigingen aan te brengen op uw apparaat.

Zodra u een PowerShell-sessie hebt geopend, kunt u de Windows Defender PowerShell-opdrachten gaan gebruiken.

## Algemene Windows Defender PowerShell-opdrachten

### 1. **Get-MpComputerStatus**: De Windows Defender-status controleren

Met de opdracht `Get-MpComputerStatus` krijgt u een overzicht van de huidige status van Windows Defender op uw systeem, waaronder de versie van de antivirusengine, het tijdstip van de laatste scan en de status van realtimebescherming. Zo kunt u snel controleren of Windows Defender goed werkt.

Om de status van Windows Defender te controleren, opent u een PowerShell-sessie met beheerdersrechten en voert u de volgende opdracht uit:

```powershell
Get-MpComputerStatus
```

Dit commando geeft informatie weer zoals:

- **AntivirusEngineVersion**: Het versienummer van de antivirusengine die door Windows Defender wordt gebruikt.
- **LastFullScanTime**: De datum en tijd van de laatste volledige scan die door Windows Defender is uitgevoerd.
- **LastQuickScanTime**: De datum en tijd van de laatste snelle scan die is uitgevoerd door Windows Defender.
- **RealTimeProtectionEnabled**: Geeft aan of realtime bescherming is in- of uitgeschakeld.

De status van Windows Defender regelmatig controleren met `Get-MpComputerStatus` zorgt ervoor dat u op de hoogte blijft van het beschermingsniveau van uw systeem tegen mogelijke bedreigingen.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

Met de opdracht `Update-MpSignature` kunt u de antivirushandtekeningen van Windows Defender handmatig bijwerken. Deze handtekeningen bevatten belangrijke informatie over bekende malware en helpen bedreigingen te detecteren en te blokkeren. Na uitvoering beschikt uw systeem over de nieuwste handtekeningen en betere bescherming tegen nieuwe bedreigingen.

Als u de handtekeningen van Windows Defender handmatig wilt bijwerken, opent u een PowerShell-sessie met beheerdersrechten en voert u de volgende opdracht uit:

```powershell
Update-MpSignature
```
Deze opdracht start het updateproces, waarbij **Windows Defender** verbinding maakt met **Microsoft-servers** om de nieuwste **antivirushandtekeningen** te downloaden. Zodra de update is voltooid, beschikt Windows Defender over de meest actuele informatie over bekende malware, waardoor het beter in staat is om bedreigingen te identificeren en te elimineren.

Het up-to-date houden van de Windows Defender-handtekeningen is essentieel voor het handhaven van het hoogste niveau van bescherming tegen het steeds veranderende landschap van **malware** en **cyberbedreigingen**. Door de handtekeningen regelmatig bij te werken met `Update-MpSignature` zorgt u ervoor dat Windows Defender uw systeem effectief kan beveiligen.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Met de opdracht `Set-MpPreference` kunt u verschillende instellingen van **Windows Defender** aanpassen aan uw beveiligingsvereisten. U kunt onder meer **realtimebescherming**, **cloudgebaseerde bescherming** en **instellingen voor het netwerkinspectiesysteem** configureren.

U kunt realtimebescherming bijvoorbeeld in- of uitschakelen met `Set-MpPreference`. Deze functie controleert uw systeem actief op schadelijke activiteiten en reageert direct op bedreigingen. Voer de volgende opdracht uit om realtimebescherming in te schakelen:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Daarnaast kunt u de opdracht gebruiken om instellingen voor cloudgebaseerde bescherming aan te passen. Cloudgebaseerde bescherming maakt gebruik van cloudbronnen om de detectie van bedreigingen te verbeteren en sneller te reageren op nieuwe bedreigingen. Gebruik de volgende opdracht om cloudgebaseerde bescherming in te schakelen:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Met `Set-MpPreference` kunt u ook de instellingen van het netwerkinspectiesysteem aanpassen. Dit systeem analyseert netwerkverkeer op verdachte activiteiten en mogelijke bedreigingen. Voer de volgende opdracht uit om de instellingen te wijzigen:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Door deze instellingen met `Set-MpPreference` af te stemmen, kunt u **Windows Defender** optimaliseren voor uw beveiligingsbehoeften en uw systeem beschermen tegen malware en andere schadelijke activiteiten.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

De opdracht `Start-MpScan` start malwarescans op uw systeem, zodat u schadelijke bestanden proactief kunt opsporen en verwijderen. U kunt verschillende soorten scans uitvoeren, waaronder **snelle scans**, **volledige scans** en **aangepaste scans** voor specifieke paden.

Voer de volgende PowerShell-opdracht uit om met `Start-MpScan` een **snelle scan** uit te voeren:

```powershell
Start-MpScan -ScanType QuickScan
```

Een snelle scan richt zich op kritieke gebieden van uw systeem waar malware vaak wordt aangetroffen en biedt u een snelle beoordeling van potentiële bedreigingen.

Voor een uitgebreidere scan die alle bestanden en mappen op uw systeem onderzoekt, kunt u een **volledige scan** starten. Voer de volgende opdracht uit om een volledige scan uit te voeren met `Start-MpScan`:

```powershell
Start-MpScan -ScanType FullScan
```

Een volledige scan zorgt voor grondige detectie en verwijdering van malware van uw systeem, maar het kan langer duren dan een snelle scan.

Naast de vooraf gedefinieerde scantypen kunt u met `Start-MpScan` aangepaste scans uitvoeren door specifieke paden of bestanden op te geven. Met de volgende opdracht scant u bijvoorbeeld een bepaalde map:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Deze opdracht start een aangepaste scan op de opgegeven map, zodat u specifieke gebieden van uw systeem kunt scannen op malware.

Met `Start-MpScan` kunt u scans plannen, beveiligingsprocessen automatiseren en malware op uw systeem regelmatig detecteren en beperken.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

De opdracht `Get-MpThreatCatalog` biedt gedetailleerde informatie over bekende bedreigingen en hun kenmerken. De catalogus bevat onder meer de ernst van bedreigingen, bijbehorende bestandsnamen en aanbevolen maatregelen.

Volg deze stappen om met `Get-MpThreatCatalog` informatie over specifieke bedreigingen op te halen:

1. Open een PowerShell-sessie met beheerdersrechten.
2. Voer de volgende opdracht uit:

```powershell
   Get-MpThreatCatalog
```
Deze opdracht toont een lijst met bekende bedreigingen samen met de bijbehorende details.

De uitvoer van `Get-MpThreatCatalog` bevat belangrijke informatie, zoals:

- **ThreatID**: Een unieke identificatiecode voor de bedreiging.
- **Severity**: Geeft het ernstniveau van de bedreiging aan, variërend van Low (laag) tot Severe (ernstig).
- **Name**: De naam of beschrijving van de bedreiging.
- **Path**: Het pad van het bestand dat aan de bedreiging is gekoppeld.
- **RecommendedAction**: De aanbevolen actie om de bedreiging te beperken.

Door gebruik te maken van de informatie die is verkregen uit `Get-MpThreatCatalog` kunt u waardevolle inzichten krijgen in potentiële bedreigingen en weloverwogen beslissingen nemen over de juiste acties om ze te beperken. Of het nu gaat om het isoleren, verwijderen of monitoren van een specifieke bedreiging, de gedetailleerde catalogus stelt u in staat om effectief te reageren op beveiligingsincidenten.

Voor meer informatie over het gebruik van `Get-MpThreatCatalog` en het interpreteren van de resultaten, raadpleeg dan de officiële documentatie van Microsoft.

Blijf waakzaam en gebruik regelmatig de `Get-MpThreatCatalog` opdracht om op de hoogte te blijven van het veranderende bedreigingslandschap en de beveiliging van uw systeem te verbeteren.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Met `Add-MpPreference` kunt u uitsluitingen toevoegen aan Windows Defender en het scan- en realtimebeschermingsgedrag aanpassen. U kunt bestanden, mappen of processen opgeven die Windows Defender tijdens scans of realtimebescherming moet negeren.

Als u met `Add-MpPreference` een uitsluiting toevoegt, geeft u het pad of de naam op van het bestand, de map of het proces dat u wilt uitsluiten. Dit voorbeeld voegt een map toe:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Deze opdracht zorgt ervoor dat Windows Defender het scannen van de opgegeven map overslaat, waardoor onnodige waarschuwingen en mogelijke onderbrekingen van uw workflow worden verminderd.

Uitsluitingen kunnen nuttig zijn in verschillende scenario's, zoals het uitsluiten van vertrouwde toepassingen, ontwikkelomgevingen of specifieke bestanden die valse positieven kunnen veroorzaken. Door gebruik te maken van de flexibiliteit van `Add-MpPreference` kunt u Windows Defender afstemmen op uw specifieke beveiligingsbehoeften en de prestaties optimaliseren.

Bescherm uw systeem effectief en minimaliseer vals-positieven en onnodige scanonderbrekingen door gebruik te maken van de krachtige uitsluitingsmogelijkheden van `Add-MpPreference`.

## Defender-opdrachten controleren in 2026

Voer Defender-opdrachten alleen uit vanuit een sessie met verhoogde rechten wanneer de taak die rechten vereist. Raadpleeg de actuele modulehelp voor de doelversie van Windows voordat u een parameter gebruikt. Leg de huidige configuratie vast, wijzig één instelling tegelijk, controleer het resultaat en noteer de opdracht om terug te draaien.

Nuttige controles zijn de beveiligingsstatus, de ouderdom van handtekeningen, uitsluitingen, voorkeuren, scangeschiedenis en recente detecties. Houd uitsluitingen beperkt en noteer de verantwoordelijke en vervaldatum. Raadpleeg de [documentatie van de Microsoft Defender PowerShell-module](https://learn.microsoft.com/en-us/powershell/module/defender/) en de [Microsoft Defender Antivirus-documentatie](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows) voor actuele cmdlets en werking.

## Conclusie

Windows Defender PowerShell-opdrachten bieden een **robuuste set hulpprogramma's** voor het beheren en verbeteren van de beveiliging van uw Windows-systeem. Door deze opdrachten te gebruiken kunt u *beveiligingstaken automatiseren*, *geavanceerde instellingen configureren* en Windows Defender soepel in uw werkstromen integreren. Of u nu een **systeembeheerder** of een **ervaren gebruiker** bent, het verkennen van de mogelijkheden van Windows Defender PowerShell-opdrachten kan de beveiliging van uw systeem aanzienlijk verbeteren.

Onthoud dat grote macht grote verantwoordelijkheid met zich meebrengt. Wees voorzichtig bij het gebruik van PowerShell-opdrachten en zorg ervoor dat u de impact van de opdrachten begrijpt voordat u ze uitvoert. Door uw kennis te combineren met de kracht van Windows Defender PowerShell-opdrachten, kunt u proactieve maatregelen nemen om uw systeem te beschermen tegen nieuwe bedreigingen.

## Referenties

1. Microsoft Docs - [Windows Defender-cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Inleiding tot Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
