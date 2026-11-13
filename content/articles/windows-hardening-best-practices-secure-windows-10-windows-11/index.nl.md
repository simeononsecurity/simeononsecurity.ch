---
title: "Beste praktijken voor Windows-hardening voor Windows 10 en 11"
date: 2023-07-27
lastmod: 2026-11-13
toc: true
draft: false
description: "Ontdek effectieve strategieën om de beveiliging van uw Windows 10- en Windows 11-systemen te verbeteren met behulp van uitgebreide hardeningtechnieken en best practices."
genre: ["Windows beveiligen", "Windows beveiliging", "Windows 10 beveiligen", "Windows 11 beveiligen", "Best practices voor Windows-beveiliging", "Beveiligingstips voor Windows", "Windows beveiligingsrichtlijnen", "Windows-besturingssystemen beveiligen", "Beveiliging van Windows-systemen", "Beveiligingsmaatregelen voor Windows"]
tags: ["Windows beveiligen", "Windows beveiliging", "Windows 10", "Windows 11", "beveiliging van het besturingssysteem", "Windows Defender", "Gebruikersaccountbeheer", "BitLocker encryptie", "firewallconfiguratie", "AppLocker beleid", "Updates voor Windows", "sterke wachtwoorden", "gegevensback-up", "Windows Hello", "Beveiligd opstarten", "TPM", "Microsoft Defender Antivirus", "Windows Sandbox", "Microsoft Defender Application Guard", "Gecontroleerde maptoegang", "Beste werkwijzen voor het beveiligen van Windows 10 en Windows 11", "Windows-besturingssystemen beveiligen", "Windows beveiligingsmaatregelen voor individuen en organisaties", "De systeembeveiliging van Windows verbeteren", "Gegevens beschermen met BitLocker-encryptie", "Browsersessies isoleren met Microsoft Defender Application Guard", "Beveiligingstips en -richtlijnen voor Windows 10", "Beveiligingsfuncties van Windows implementeren", "Windows beveiligen met isolatie op basis van hardware", "De systeemintegriteit van Windows waarborgen"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.webp"
coverAlt: "Een cartoonillustratie van een schild dat een Windows-logo beschermt tegen verschillende cyberbedreigingen."
coverCaption: "Beveilig je Windows-fort met effectieve hardeningtechnieken."
---

## Introductie

Windows besturingssystemen worden op grote schaal gebruikt door individuen en organisaties over de hele wereld. Om de veiligheid en integriteit van deze systemen te waarborgen, is het essentieel om **Windows hardening best practices** te implementeren. Hardening houdt in het beveiligen van het besturingssysteem door het aanvalsoppervlak te verkleinen en mogelijke kwetsbaarheden te verminderen. Dit artikel gaat in op de best practices voor het harden van zowel **Windows 10** als de nieuwere **Windows 11** besturingssystemen en biedt waardevolle inzichten om de beveiliging van uw Windows-omgeving te verbeteren.

______

## Windows hardening begrijpen

Windows hardening is het proces van het versterken van de beveiliging van een Windows besturingssysteem. Het omvat het configureren van verschillende instellingen en het implementeren van beveiligingsmaatregelen om bescherming te bieden tegen ongeautoriseerde toegang, malware en andere bedreigingen. Door je Windows-systeem te harden, kun je de risico's van cyberaanvallen minimaliseren en de vertrouwelijkheid, integriteit en beschikbaarheid van je gegevens garanderen.

### [Windows 10 beveiligen](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 10 is wereldwijd een van de meest gebruikte besturingssystemen. Overweeg de volgende best practices om je Windows 10-omgeving te harden:

#### 1. [**Windows Defender inschakelen**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

Windows Defender is een **robuuste antivirusoplossing** die bij Windows 10 wordt geleverd. Het biedt een reeks beveiligingsfuncties om uw systeem te beschermen tegen verschillende soorten **malware**, waaronder **virussen, spyware en ransomware**. Door Windows Defender in te schakelen, kunt u de beveiliging van uw Windows 10-omgeving aanzienlijk verbeteren.

Voer de volgende stappen uit om Windows Defender in te schakelen:

- Open de **Windows Security** app door te klikken op het Windows Security icoon in de taakbalk of door te zoeken naar "Windows Security" in het Start menu.
- Klik in de Windows Security-app op "**Virus- en bedreigingsbescherming**" in het navigatiedeelvenster aan de linkerkant.
- Klik op "**Instellingen beheren**" onder de sectie "Instellingen voor virus- en bescherming tegen bedreigingen".
- Zorg ervoor dat de schakelaar "**Real-time bescherming**" is ingesteld op "**Aan**". Hierdoor kan Windows Defender actief scannen en uw systeem in realtime beschermen.
- Bovendien kunt u de scanopties en uitsluitingen aanpassen door respectievelijk op "**Scanopties**" en "**Uitzonderingen toevoegen of verwijderen**" te klikken.

Het is cruciaal om Windows Defender **regelmatig** bij te werken om er zeker van te zijn dat het over de laatste **malwaredefinities** en **veiligheidsverbeteringen** beschikt. Microsoft brengt regelmatig updates uit om nieuwe bedreigingen en kwetsbaarheden aan te pakken. Volg deze stappen om Windows Defender bij te werken:

- Open de Windows Beveiligingsapp.
- Ga naar "**Virus- en bedreigingsbescherming**" in het navigatiedeelvenster aan de linkerkant.
- Klik op "**Controleren op updates**" onder het gedeelte "Virus- en bedreigingsbeschermingsupdates".
- Windows zal controleren op beschikbare updates en deze indien nodig downloaden/installeren.

Door Windows Defender in te schakelen en up-to-date te houden, kun je je Windows 10-systeem proactief beschermen tegen malware en andere beveiligingsbedreigingen. Het wordt ook aanbevolen om **regelmatig systeemscans** uit te voeren met Windows Defender om ervoor te zorgen dat alle potentiële bedreigingen worden opgespoord en verwijderd.

Onthoud dat Windows Defender weliswaar een solide beschermingsniveau biedt, maar dat het essentieel is om dit aan te vullen met **veilige surfgewoonten**, **regelmatige software-updates** en andere beveiligingsmaatregelen om een veilige Windows 10-omgeving te behouden.

#### 2. [**Windows 10 up-to-date houden**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)
Het regelmatig installeren van Windows-updates is een cruciaal aspect van **het verbeteren van Windows 10**. Deze updates bevatten **beveiligingspatches**, bugfixes en prestatieverbeteringen die helpen **kwetsbaarheden in de beveiliging te verhelpen** en de stabiliteit van het systeem te verbeteren.

Microsoft brengt regelmatig **updates** uit voor Windows 10 om nieuw ontdekte beveiligingsproblemen aan te pakken en de algemene gebruikerservaring te verbeteren. Door uw systeem up-to-date te houden, zorgt u ervoor dat uw besturingssysteem over de nieuwste **beveiligingsverbeteringen** beschikt om u te verdedigen tegen nieuwe bedreigingen.

Om Windows 10 up-to-date te houden, kunt u de volgende stappen volgen:

1. **Automatische updates** inschakelen: Windows 10 is standaard geconfigureerd om updates automatisch te downloaden en te installeren. Dit zorgt ervoor dat uw systeem de nodige updates ontvangt zonder handmatige tussenkomst. Volg deze stappen om te controleren of automatische updates zijn ingeschakeld:
   - Ga naar **Instellingen** door op het menu Start te klikken en het tandwielpictogram te selecteren.
   - Klik op **Update en beveiliging**.
   - Klik in het linker navigatiedeelvenster op **Windows Update**.
   - Controleer of de optie **"Automatisch"** is geselecteerd onder **"Instellingen Windows Update"**. Als deze niet is geselecteerd, klik dan op de link **"Actieve uren wijzigen"** om de actieve uren aan te passen waarop Windows moet voorkomen dat updates worden geïnstalleerd.

2. **Handmatig updates installeren**: Als je liever meer controle hebt over het updateproces, kun je handmatig updates installeren op je Windows 10-systeem. Dit doe je als volgt:
   - Ga naar **Instellingen** > **Update & beveiliging** > **Windows Update**.
   - Klik op **"Controleren op updates"** om te zien of er updates beschikbaar zijn voor uw systeem.
   - Als er updates gevonden zijn, klik dan op **"Downloaden"** en **"Installeren"** om het installatieproces te starten.

Het is belangrijk om te benadrukken dat het belangrijk is om **regelmatig uw systeem opnieuw op te starten** na het installeren van updates. Sommige updates vereisen mogelijk een herstart van het systeem om de wijzigingen volledig toe te passen en de effectiviteit ervan te garanderen.

Door **uw Windows 10-systeem up-to-date te houden**, verbetert u niet alleen de beveiliging, maar profiteert u ook van de nieuwste functies, prestatieverbeteringen en compatibiliteitsoplossingen. Het is een proactieve maatregel om ervoor te zorgen dat je systeem bestand blijft tegen mogelijke beveiligingsrisico's.

#### 3. [**User Account Control (UAC) configureren**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)
User Account Control (UAC) is een beveiligingsfunctie in Windows 10 die helpt ongeautoriseerde wijzigingen aan je systeem te voorkomen door zo nodig om goedkeuring van de beheerder te vragen. Het fungeert als een beveiliging tegen kwaadaardige software of ongeautoriseerde gebruikers die wijzigingen proberen aan te brengen die de veiligheid of stabiliteit van het systeem kunnen beïnvloeden.

Het configureren van UAC-instellingen op een geschikt niveau is cruciaal voor **het versterken van Windows 10**. Het gaat erom een balans te vinden tussen beveiliging en bruikbaarheid om ervoor te zorgen dat UAC uw systeem effectief beschermt zonder onnodige onderbrekingen te veroorzaken.

Om de UAC-instellingen in Windows 10 te configureren, kunt u de volgende stappen volgen:

1. Open het **Configuratiescherm** door "Configuratiescherm" in de zoekbalk te typen en het te selecteren in de zoekresultaten.

2. Klik in het Configuratiescherm op **"Gebruikersaccounts"**.

3. Klik op **"Instellingen voor gebruikersaccountbeheer wijzigen"**.

4. Je ziet een schuifbalk met verschillende niveaus van UAC-instellingen. Dit zijn de beschikbare opties:
   - **"Altijd waarschuwen"**: Dit is het hoogste niveau van UAC-beveiliging waarbij u om toestemming wordt gevraagd voor elke systeemwijziging, zelfs voor eenvoudige taken.
   - **"Alleen waarschuwen als apps wijzigingen in mijn computer proberen aan te brengen (standaard)"**: Dit is de aanbevolen instelling die een balans biedt tussen beveiliging en bruikbaarheid. U wordt om toestemming gevraagd wanneer apps wijzigingen aanbrengen, maar niet voor wijzigingen in Windows-instellingen.
   - **"Waarschuw me alleen wanneer apps proberen wijzigingen aan te brengen op mijn computer (mijn bureaublad niet dimmen)"**: Vergelijkbaar met de vorige optie, maar het bureaublad wordt niet gedimd wanneer UAC-verzoeken verschijnen.
   - **"Nooit waarschuwen"**: Dit is het laagste niveau van UAC-beveiliging, waarbij u niet wordt gevraagd om systeemwijzigingen door te voeren.

5. Kies het UAC-beveiligingsniveau dat aan uw behoeften voldoet door de schuifknop naar de gewenste positie te verplaatsen.

6. Klik op **"OK"** om de wijzigingen op te slaan.

Het wordt aanbevolen om UAC ingeschakeld te laten en in te stellen op een niveau dat een goede balans biedt tussen beveiliging en bruikbaarheid. UAC volledig uitschakelen kan uw systeem kwetsbaarder maken voor ongeoorloofde wijzigingen en mogelijk de beveiliging in gevaar brengen.

Door UAC-instellingen te configureren, verbeter je de beveiliging van je Windows 10-systeem door ervoor te zorgen dat beheerdersrechten vereist zijn voor kritieke systeemwijzigingen, waardoor het risico op ongeoorloofde toegang en malware-infecties afneemt.

{{< figure src="windows-10-uac-bitlocker-security-overview.webp" alt="Diagram van Windows 10-niveaus voor Gebruikersaccountbeheer en BitLocker-versleuteling die de systeemintegriteit en gevoelige gegevens beschermen" >}}

#### 4. [**Gebruik sterke wachtwoorden**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)
Het gebruik van sterke wachtwoorden is essentieel voor het handhaven van de beveiliging van je Windows 10-systeem en de bescherming tegen onbevoegde toegang. Zwakke of gemakkelijk te raden wachtwoorden kunnen je systeem kwetsbaar maken voor aanvallen, zoals brute-force aanvallen of het kraken van wachtwoorden.

Volg deze best practices voor wachtwoorden om ervoor te zorgen dat alle gebruikersaccounts op je Windows 10-systeem sterke wachtwoorden hebben:

1. **Complexiteit**: Moedig gebruikers aan om wachtwoorden te maken die complex en niet gemakkelijk te raden zijn. Een sterk wachtwoord moet een combinatie van hoofdletters en kleine letters, cijfers en speciale tekens bevatten. Vermijd het gebruik van gewone woorden of voorspelbare patronen.

2. **lengte**: Langere wachtwoorden zijn over het algemeen veiliger. Moedig gebruikers aan om wachtwoorden te maken die minstens 8 tekens lang zijn, maar bij voorkeur langer. Hoe meer tekens een wachtwoord bevat, hoe moeilijker het te kraken is.

3. **Uniekheid**: Elk gebruikersaccount moet een uniek wachtwoord hebben. Hetzelfde wachtwoord gebruiken voor meerdere accounts verhoogt het risico op een inbreuk op de beveiliging. Moedig gebruikers aan om verschillende wachtwoorden te gebruiken voor verschillende accounts.

4. **Vermijd persoonlijke informatie**: Adviseer gebruikers om geen persoonlijke informatie zoals namen, geboortedata of adressen te gebruiken in hun wachtwoorden. Deze informatie kan gemakkelijk worden verkregen of geraden door aanvallers.

5. **Wachtwoordbeheerders**: Overweeg het gebruik van een wachtwoordmanager om wachtwoorden veilig op te slaan en te beheren. Wachtwoordmanagers kunnen sterke, unieke wachtwoorden genereren voor elke account en deze opslaan in een versleutelde database.

6. **Wijzig wachtwoorden regelmatig**: Moedig gebruikers aan om regelmatig hun wachtwoorden te wijzigen om de beveiliging te handhaven. Stel een beleid op voor het verlopen van wachtwoorden en wijs gebruikers op het belang van het regelmatig bijwerken van hun wachtwoorden.

Door sterke wachtwoordpraktijken te implementeren, verbetert u de beveiliging van uw Windows 10-systeem aanzienlijk en verlaagt u het risico op onbevoegde toegang of inbreuken op gegevens. Informeer gebruikers regelmatig over wachtwoordbeveiliging en bied hulpmiddelen, zoals wachtwoordsterktemeters of richtlijnen voor het maken van wachtwoorden, om hen te helpen bij het maken van sterke wachtwoorden.

Voor meer gedetailleerde informatie over het maken van sterke wachtwoorden en best practices, kunt u dit raadplegen [artikel](https://simeononsecurity.com/articles/how-to-create-strong-passwords/) Het biedt uitgebreide richtlijnen voor het beveiligen van wachtwoorden en tips voor het maken van sterke en memorabele wachtwoorden.

Onthoud dat het gebruik van sterke wachtwoorden een fundamenteel aspect van systeembeveiliging is en prioriteit moet krijgen om gevoelige gegevens te beschermen en de integriteit van je Windows 10-omgeving te waarborgen.

#### 5. [**BitLocker-versleuteling inschakelen**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
Een van de meest effectieve manieren om gevoelige gegevens op je Windows 10-systeem te beschermen is door BitLocker-encryptie in te schakelen. BitLocker biedt volledige schijfversleuteling, zodat zelfs als je apparaat zoekraakt of wordt gestolen, je gegevens veilig en ontoegankelijk blijven voor onbevoegden.

Volg deze stappen om BitLocker-encryptie in te schakelen en je gevoelige informatie te beveiligen:

1. **Controleer de systeemvereisten**: Controleer of uw Windows 10-editie BitLocker-encryptie ondersteunt. BitLocker is beschikbaar in Windows 10 Pro, Enterprise en Education edities.

2. **BitLocker inschakelen**: Open het Configuratiescherm en navigeer naar de categorie "Systeem en beveiliging". Klik op "BitLocker Drive Encryption" en selecteer de schijf of schijven die u wilt versleutelen. Volg de instructies op het scherm om het versleutelingsproces te starten.

3. **Kies coderingsopties**: Tijdens de installatie van BitLocker kunt u kiezen uit verschillende versleutelingsmethoden, zoals het gebruik van een wachtwoord, een smartcard of beide. Selecteer de juiste methode op basis van uw beveiligingseisen en voorkeuren.

4. **Back-up herstelsleutel**: Het is cruciaal om een back-up te maken van de BitLocker herstelsleutel. Deze sleutel fungeert als noodbeveiliging voor het geval u uw wachtwoord vergeet of problemen ondervindt bij de toegang tot de versleutelde schijf. Bewaar de herstelsleutel op een veilige locatie, los van je apparaat.

5. **Beheer BitLocker-instellingen**: Nadat u BitLocker hebt ingeschakeld, kunt u extra instellingen aanpassen, zoals het automatisch deblokkeren van specifieke schijven of het configureren van het gebruik van TPM (Trusted Platform Module) voor extra beveiliging. Deze instellingen zijn toegankelijk via de BitLocker-beheersinterface.

Door BitLocker-encryptie in te schakelen, voeg je een extra beschermingslaag toe aan je Windows 10-systeem, zodat je gegevens veilig en ontoegankelijk blijven, zelfs als je apparaat in verkeerde handen valt. Het is belangrijk om je BitLocker-instellingen regelmatig bij te werken en te onderhouden om op de hoogte te blijven van de beste beveiligingspraktijken.

Voor meer gedetailleerde informatie over het inschakelen en beheren van BitLocker-encryptie, kunt u de officiële [Microsoft-documentatie](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) Het biedt uitgebreide richtlijnen voor BitLocker-encryptie, inclusief geavanceerde functies en configuratieopties.

Vergeet niet dat het inschakelen van BitLocker-encryptie uw gevoelige gegevens helpt beschermen en u gemoedsrust geeft in de wetenschap dat uw informatie veilig is, zelfs in het geval van verlies of diefstal.

#### 6. **Onnodige services en functies uitschakelen**
Om de beveiliging van uw Windows 10-systeem te verbeteren, is het essentieel om onnodige services en functies te controleren en uit te schakelen. Door dit te doen, verkleint u het aanvalsoppervlak en minimaliseert u de kans op uitbuiting door kwaadwillenden.

Hier volgen de stappen om onnodige services en functies op je Windows 10-systeem uit te schakelen:

1. **Identificeer onnodige services**: Begin met het identificeren van de services die op je systeem worden uitgevoerd. Open de beheerconsole "Services" door op **Windows-toets + R** te drukken, **services.msc** in te typen en op **Enter** te drukken. Bekijk de lijst met services en onderzoek hun doel om te bepalen welke essentieel zijn voor de functionaliteit van uw systeem.

2. **Schakel onnodige services uit**: Zodra u de onnodige services hebt geïdentificeerd, klikt u met de rechtermuisknop op elke service en selecteert u **Eigenschappen**. Wijzig in het venster Eigenschappen het **Opstarttype** in **Uitgeschakeld**. Dit voorkomt dat de service automatisch start wanneer je systeem opstart. Wees voorzichtig en zorg ervoor dat u alleen services uitschakelt die niet nodig zijn voor de normale werking van uw systeem.

3. **Schakel onnodige functies uit**: Naast services bevat Windows 10 ook verschillende functies die mogelijk niet nodig zijn voor uw systeem. Open het Configuratiescherm&#8203;**, navigeer naar**&#8203; Programma's &#8203;**of**&#8203; Programma's en onderdelen &#8203;**en klik op**&#8203; Windowsfuncties in- of uitschakelen. Vink alle functies uit die u niet nodig hebt. Deze stap helpt het aanvalsoppervlak verder te verkleinen en minimaliseert de bronnen die door onnodige functies worden verbruikt.

4. **Regelmatig controleren en bijwerken**: Het is cruciaal om de lijst met services en functies die zijn ingeschakeld op je Windows 10-systeem regelmatig te controleren. Als de vereisten van je systeem na verloop van tijd veranderen, moet je mogelijk de services en functies die nodig zijn opnieuw evalueren. Blijf waakzaam en werk je configuratie zo nodig bij.

Door onnodige services en functies uit te schakelen, beperkt u de potentiële toegangspunten voor aanvallers en verkleint u het totale aanvalsoppervlak van uw Windows 10-systeem. Deze praktijk verbetert de beveiliging van je systeem en vermindert het risico op uitbuiting.

{{< figure src="windows-10-firewall-applocker-attack-surface-reduction.webp" alt="Diagram van Windows 10-firewallregels, AppLocker-beleidsregels voor toepassingsbeheer en aanvalsoppervlakreductie die samen onbevoegde toegang blokkeren" >}}

Voor meer informatie over het beheren van services en functies in Windows 10 kunt u het volgende raadplegen [artikel](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20) voor gedetailleerde richtlijnen.

Onthoud dat het cruciaal is om voorzichtig te zijn met het uitschakelen van services en functies, omdat het uitschakelen van essentiële onderdelen de functionaliteit van je systeem negatief kan beïnvloeden. Onderzoek en begrijp altijd het doel van een service of functie voordat u wijzigingen aanbrengt.

#### 7. **Implementeer firewallregels**
De ingebouwde firewall in Windows 10 fungeert als een cruciale verdedigingslinie tegen ongeautoriseerd netwerkverkeer. Door firewallregels in te stellen, kunt u bepalen welke inkomende en uitgaande verbindingen worden toegestaan en zo de beveiliging van uw systeem verbeteren.

Volg deze stappen om firewallregels te implementeren op je Windows 10-systeem:

1. **Toegang tot firewallinstellingen**: Om toegang te krijgen tot de firewallinstellingen open je het **Configuratiescherm**, zoek je naar **Windows Defender Firewall** en klik je op het betreffende resultaat. U kunt ook met de rechtermuisknop klikken op de knop **Start**, **Instellingen** selecteren en navigeren naar **Netwerk en internet > Windows Firewall**.

2. **Configureer Inkomende regels**: Inkomende regels controleren inkomende netwerkverbindingen naar uw systeem. Klik op **Uitgebreide instellingen** in het venster van Windows Defender Firewall. Selecteer in het nieuwe venster **Inkomende regels** en klik op **Nieuwe regel**. Volg de instructies op het scherm om regels te maken die alleen noodzakelijke inkomende verbindingen toestaan. Denk na over de services en applicaties die toegang tot het netwerk vereisen en maak de regels dienovereenkomstig.

3. **Configureer uitgaande regels**: Uitgaande regels regelen de uitgaande netwerkverbindingen van je systeem. Volg dezelfde stappen als hierboven, maar selecteer in plaats daarvan **Uitgaande regels**. Maak regels om uitgaande verbindingen toe te staan voor essentiële services en applicaties terwijl verdachte of onnodige verbindingen worden geblokkeerd.

4. **Regelmatig controleren en bijwerken**: Het is belangrijk om uw firewallregels regelmatig te herzien en bij te werken om ervoor te zorgen dat ze in lijn zijn met de vereisten van uw systeem. Als uw netwerkomgeving en gebruikspatronen veranderen, kan het nodig zijn om regels aan te passen of nieuwe regels te maken. Blijf waakzaam en houd uw regels up-to-date om een effectieve firewallconfiguratie te behouden.

Door firewallregels te implementeren en te onderhouden, kunt u het risico op onbevoegde toegang tot het netwerk aanzienlijk verkleinen en de beveiliging van uw Windows 10-systeem verbeteren. Overweeg daarnaast om de optie **Stealthmodus** in de firewallinstellingen in te schakelen om je systeem minder zichtbaar te maken voor potentiële aanvallers.

Voor meer gedetailleerde informatie over het configureren van firewallregels in Windows 10, kunt u de officiële [Microsoft-documentatie](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring) voor stapsgewijze instructies.

Onthoud dat een goed geconfigureerde firewall een essentieel onderdeel is van een alomvattende beveiligingsstrategie, maar dat deze gebruikt moet worden in combinatie met andere beveiligingsmaatregelen om een robuuste bescherming voor je systeem te bieden.

#### 8. [**AppLocker gebruiken**](https://github.com/simeononsecurity/AppLocker)
[AppLocker](https://simeononsecurity.com/github/applocker-hardening/) is een krachtige functie in Windows 10 waarmee je kunt bepalen welke toepassingen op je systeem kunnen worden uitgevoerd. Door AppLocker-beleidsregels te implementeren, kunt u de uitvoering van niet-geautoriseerde of mogelijk schadelijke toepassingen beperken en zo de beveiliging van uw Windows 10-omgeving verbeteren.

Volg deze stappen om AppLocker te gebruiken op je Windows 10-systeem:

1. **Toegang tot AppLocker instellingen**: Om toegang te krijgen tot de AppLocker instellingen open je de **Local Group Policy Editor** door op **Windows toets + R** te drukken, **gpedit.msc** in te typen en op **OK** te klikken. U kunt ook zoeken naar **Groepsbeleideditor** in het **Start** menu.

2. **Configureer AppLocker beleid**: Navigeer in de Editor voor lokaal groepsbeleid naar **Computerconfiguratie > Windows-instellingen > Beveiligingsinstellingen > Toepassingsbeheerbeleid > AppLocker**. Hier kunt u verschillende beleidsregels configureren, zoals **Executable Rules**, **Windows Installer Rules**, **Script Rules** en **Packaged App Rules**.

3. **Maak AppLocker regels**: Om een AppLocker regel aan te maken, klikt u met de rechtermuisknop op de gewenste beleidsmap (bijvoorbeeld **Executable Rules**) en selecteert u **Create New Rule**. Volg de instructies op het scherm om de voorwaarden en uitzonderingen voor de regel op te geven. U kunt regels maken op basis van bestandspad, uitgever, bestandshash of andere attributen om de uitvoering van applicaties toe te staan of te weigeren.

4. **Beleid testen en verfijnen**: Na het maken van AppLocker regels is het belangrijk om ze te testen om er zeker van te zijn dat ze werken zoals bedoeld. Implementeer het beleid op een testgroep of systeem en controleer of alleen geautoriseerde applicaties mogen draaien. Verfijn de regels indien nodig op basis van de testresultaten.

5. **Regelmatig herzien en bijwerken**: Als uw applicatielandschap evolueert, is het cruciaal om uw AppLocker beleid regelmatig te herzien en bij te werken. Nieuwe applicaties kunnen toestemming nodig hebben om te draaien, terwijl andere verouderd kunnen zijn of beveiligingsrisico's met zich meebrengen. Blijf proactief en houd uw beleid up-to-date om een effectief mechanisme voor applicatiecontrole te behouden.

AppLocker biedt granulaire controle over de uitvoering van toepassingen en helpt voorkomen dat niet-geautoriseerde of schadelijke software wordt uitgevoerd op uw Windows 10-systeem. Door AppLocker te gebruiken, kunt u het risico op malware-infecties, ongeautoriseerde software-installaties en andere beveiligingsincidenten verminderen.

Voor meer gedetailleerde informatie over het implementeren van AppLocker-beleidsregels kunt u de officiële [Microsoft-documentatie](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) or visit our [AppLocker-repository op GitHub](https://github.com/simeononsecurity/AppLocker) voor aanvullende bronnen en voorbeelden.

Vergeet niet om je AppLocker beleid regelmatig te herzien en bij te werken om je aan te passen aan veranderende applicatie-eisen en nieuwe beveiligingsrisico's. AppLocker is een waardevol hulpmiddel in je verdediging tegen ongeautoriseerde en mogelijk schadelijke toepassingen op je Windows 10-systeem.

#### 9. [**Maak regelmatig een back-up van je gegevens**](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)
Het regelmatig maken van back-ups van je gegevens is essentieel om je te beschermen tegen gegevensverlies door beveiligingsincidenten, hardwarestoringen of andere onverwachte gebeurtenissen. Door regelmatig back-ups te maken en de integriteit ervan te controleren, kun je ervoor zorgen dat je belangrijke gegevens veilig blijven en kunnen worden hersteld in het geval van een ramp.

Volg deze stappen om regelmatig een back-up te maken van je gegevens op een Windows 10-systeem:

1. **Identificeer kritieke gegevens**: Begin met het identificeren van de gegevens die kritisch zijn en waarvan een back-up moet worden gemaakt. Dit kunnen belangrijke documenten, persoonlijke bestanden, systeemconfiguraties, applicatie-instellingen en andere gegevens zijn die je als waardevol beschouwt.

2. **Kies een back-upoplossing**: Selecteer een betrouwbare back-upoplossing die aan uw eisen voldoet. Windows 10 biedt ingebouwde back-uphulpmiddelen zoals **Bestandsgeschiedenis** en **Windows Back-up en Herstel**. Je kunt ook kiezen voor back-upsoftware van derden die extra functies en flexibiliteit biedt.

3. **Back-upfrequentie** bepalen: Bepaal hoe vaak je back-ups wilt maken op basis van de kriticiteit van je gegevens en de frequentie van wijzigingen. Voor sommige gegevens kan een dagelijkse back-up nodig zijn, terwijl je voor andere gegevens een wekelijkse of maandelijkse back-up kunt maken.

4. **Selecteer back-upopslag**: Kies een geschikt opslagmedium om je back-ups op te slaan. Dit kunnen externe harde schijven zijn, NAS-apparaten (Network Attached Storage), cloudopslagdiensten of een combinatie van meerdere opslagopties. Zorg ervoor dat het opslagmedium veilig en betrouwbaar is.

5. **Back-upinstellingen configureren**: Stel de back-upoplossing in volgens uw voorkeuren. Specificeer de gegevens waarvan een back-up moet worden gemaakt, de back-upbestemming en eventuele aanvullende instellingen zoals codering of compressie.

6. **Verricht testherstel**: Test het herstelproces regelmatig door testherstel uit te voeren vanaf uw back-ups. Dit zorgt ervoor dat uw back-ups correct werken en dat u uw gegevens met succes kunt herstellen wanneer dat nodig is.

7. **Monitor en update**: Controleer het back-upproces regelmatig om er zeker van te zijn dat het verloopt zoals verwacht. Werk uw back-upoplossing bij en pas de back-upinstellingen aan als uw gegevens en vereisten veranderen.

Door deze stappen te volgen en een regelmatige back-uproutine aan te houden, kunt u de impact van gegevensverlies minimaliseren en de beschikbaarheid van uw belangrijke informatie behouden. Vergeet niet om uw back-ups veilig op te slaan, niet in de buurt van de oorspronkelijke gegevens, en overweeg om de **3-2-1 back-upregel** toe te passen door ten minste drie kopieën van uw gegevens te bewaren op twee verschillende opslagmedia, met één kopie op een andere locatie.

Voor meer gedetailleerde informatie over best practices voor back-ups en de **3-2-1 back-upregel** kunt u het artikel op [Wat is de 3-2-1-back-upregel en waarom pas je die toe?](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) Het biedt waardevolle inzichten en aanbevelingen voor het implementeren van een effectieve back-upstrategie.

Vergeet niet dat regelmatige back-ups cruciaal zijn om je gegevens te beschermen en de beschikbaarheid ervan te garanderen in geval van onvoorziene gebeurtenissen. Maak het maken van back-ups een integraal onderdeel van je Windows 10 hardening inspanningen om je waardevolle informatie te beschermen.

______

### [Windows 11 beveiligen](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 11 is de nieuwste versie van het Windows-besturingssysteem en biedt verbeterde functies en een betere beveiliging. Overweeg de volgende best practices om je Windows 11-omgeving te harden:

#### 1. **Secure Boot en TPM**
Secure Boot en TPM (Trusted Platform Module) zijn essentiële beveiligingsfuncties die beschikbaar zijn in Windows 11 en die helpen beschermen tegen onbevoegde toegang en de integriteit van het besturingssysteem waarborgen. Door Secure Boot en TPM in te schakelen, kunt u de beveiliging van uw Windows 11-systeem verbeteren.

Volg deze stappen om Secure Boot en TPM in te schakelen op uw Windows 11-apparaat:

1. **Controleer compatibiliteit**: Voordat u Secure Boot en TPM inschakelt, moet u controleren of uw apparaat deze functies ondersteunt. Controleer of de hardware en firmware van uw systeem voldoen aan de vereisten voor Secure Boot- en TPM-functionaliteit.

2. **Toegang tot UEFI/BIOS-instellingen**: Start uw Windows 11-apparaat opnieuw op en ga naar de UEFI- (Unified Extensible Firmware Interface) of BIOS-instellingen (Basic Input/Output System). De specifieke toets of toetsencombinatie om toegang te krijgen tot deze instellingen kan per apparaat verschillen. Veelgebruikte toetsen zijn Del, F2, F10 of Esc. Raadpleeg de documentatie van het apparaat of de website van de fabrikant voor gedetailleerde instructies.

3. **Schakel Secure Boot** in: Navigeer in de UEFI/BIOS-instellingen naar de instellingen voor Secure Boot. Schakel Secure Boot in om ervoor te zorgen dat alleen vertrouwde besturingssystemen en componenten mogen worden uitgevoerd tijdens het opstartproces. Dit voorkomt het laden van ongeautoriseerde of kwaadaardige software die de beveiliging van het systeem in gevaar kan brengen.

4. **TPM inschakelen**: Zoek de TPM-instellingen in het UEFI/BIOS en schakel TPM in. TPM is een speciale microchip op het moederbord die hardwarematige beveiligingsfuncties biedt. Door TPM in te schakelen kan Windows 11 de mogelijkheden ervan benutten voor een betere systeembeveiliging.

5. **Configureer TPM-beveiliging**: Nadat u TPM hebt ingeschakeld, hebt u mogelijk extra opties om de beveiligingsinstellingen te configureren. Afhankelijk van uw apparaat en firmware kunt u mogelijk een TPM-wachtwoord instellen, TPM-firmware-updates inschakelen of andere gerelateerde instellingen aanpassen. Bekijk de beschikbare opties en configureer ze op basis van uw beveiligingsvereisten.

6. **Opslaan en afsluiten**: Zodra u Secure Boot en TPM hebt ingeschakeld en de nodige configuraties hebt gemaakt, slaat u de wijzigingen in de UEFI/BIOS-instellingen op en sluit u het systeem af. Het systeem start opnieuw op en de nieuwe instellingen worden van kracht.

Het inschakelen van Secure Boot en TPM in Windows 11 helpt je apparaat te beschermen tegen ongeoorloofde wijzigingen, rootkits en andere beveiligingsbedreigingen. Deze functies vormen een basis van vertrouwen voor het besturingssysteem en dragen bij aan een veiligere computeromgeving.

Merk op dat de beschikbaarheid en specifieke stappen om Secure Boot en TPM in te schakelen kunnen verschillen, afhankelijk van de fabrikant en firmwareversie van je apparaat. Het is aanbevolen om de documentatie van je apparaat of de website van de fabrikant te raadplegen voor nauwkeurige instructies op maat van je systeem.

Door Secure Boot en TPM in te schakelen op je Windows 11-apparaat, verbeter je de algemene beveiliging en versterk je de bescherming van je besturingssysteem en gevoelige gegevens.

#### 2. [**Microsoft Defender Antivirus inschakelen**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Windows 11 wordt geleverd met ingebouwde antivirusbescherming genaamd **Microsoft Defender Antivirus**. Het biedt uitgebreide beveiliging tegen verschillende soorten **malware**, waaronder virussen, ransomware en spyware. Door **Microsoft Defender Antivirus** in te schakelen &#8203;**en** regelmatig bij te werken&#8203;**, kunt u ervoor zorgen dat bedreigingen** op uw Windows 11-systeem in realtime worden opgespoord en voorkomen.

Volg deze stappen om Microsoft Defender Antivirus in te schakelen en bij te werken op uw Windows 11-apparaat:

1. **Controleer de antivirusstatus**: Controleer eerst de status van Microsoft Defender Antivirus op uw systeem. Open de app **Windows Beveiliging** door in het menu Start te klikken, te zoeken naar "Windows Beveiliging" en de app te selecteren in de zoekresultaten. Zodra de toepassing is geopend, navigeert u naar het gedeelte **"Virus- en bedreigingsbescherming"** om de status van Microsoft Defender Antivirus te controleren. Het zou standaard **ingeschakeld** moeten zijn op een nieuwe installatie van Windows 11.

2. **2. Schakel Real-Time Protection** in: Zorg er in de Windows Beveiligingsapp voor dat **Realtime bescherming** is ingeschakeld voor Microsoft Defender Antivirus. Realtime bescherming controleert uw systeem voortdurend op malware en andere schadelijke activiteiten en biedt **onmiddellijke reacties** en **blokkeert bedreigingen** in realtime. Als realtime bescherming niet is ingeschakeld, klik dan op de schakelaar om deze in te schakelen.

3. 3. **definities bijwerken**: Het regelmatig bijwerken van de **virusdefinities** is cruciaal om ervoor te zorgen dat Microsoft Defender Antivirus de nieuwste bedreigingen kan detecteren en er bescherming tegen kan bieden. Navigeer in de Windows Beveiligingsapp naar de sectie **"Virus- en bedreigingsbescherming"** en klik op de knop **"Controleren op updates"** om de antivirusdefinities bij te werken. Dit proces zorgt ervoor dat je systeem is uitgerust met de **laatste handtekeningen** en **detectiemogelijkheden**.

4. **Plan scans**: Met Microsoft Defender Antivirus kunt u regelmatig **systeemscans** plannen om potentiële bedreigingen proactief te detecteren en te verwijderen. Ga in de Windows Beveiligingsapp naar de sectie **"Virus- en bedreigingsbescherming"** en klik op de optie **"Snelle scan"** of **"Volledige scan"** om een scan te starten. Je kunt ook op de link **"Scanopties"** klikken om de scaninstellingen aan te passen en regelmatige scans te plannen volgens jouw voorkeur.

5. **Aanvullende instellingen** configureren: Microsoft Defender Antivirus biedt extra instellingen en functies die u kunt configureren op basis van uw beveiligingsvereisten. Verken in de Windows Beveiligingsapp de verschillende secties zoals **"Controle van apps en browsers", "Apparaatbeveiliging"** en **"Firewall en netwerkbeveiliging"** om de antivirusinstellingen aan te passen en gebruik te maken van geavanceerde beveiligingsfuncties.

Het inschakelen en regelmatig bijwerken van Microsoft Defender Antivirus in Windows 11 is essentieel voor een sterke verdediging tegen malware en andere beveiligingsbedreigingen. Door deze stappen te volgen en Microsoft Defender Antivirus up-to-date te houden, kunt u ervoor zorgen dat uw Windows 11-systeem goed beschermd is.

Hoewel Microsoft Defender Antivirus robuuste bescherming biedt, is het altijd aan te raden om **veilige surfgewoonten** te gebruiken, voorzichtig te zijn met **het downloaden van bestanden** of **het openen van e-mailbijlagen**, en uw **besturingssysteem en toepassingen** up-to-date te houden om uw algemene beveiliging verder te verbeteren.

{{< figure src="windows-11-secure-boot-tpm-defender-security-stack.webp" alt="Diagram van de Windows 11-beveiligingsstack met Secure Boot, TPM-hardwarebeveiliging, Microsoft Defender Antivirus en virtualisatiegebaseerde beveiliging" >}}

#### 3. **Standaard hardware-gebaseerde isolatie** toepassen
Windows 11 maakt gebruik van op hardware gebaseerde isolatiefuncties zoals **Virtualization-based Security (VBS)** en **Hypervisor-protected Code Integrity (HVCI)** om verbeterde beveiliging te bieden en kritieke systeemonderdelen te beschermen.

Door deze standaard hardwaregebaseerde isolatiefuncties in te schakelen en toe te passen, kunt u robuuste beveiligingsgrenzen instellen en verschillende aanvalsvectoren beperken. Hier volgen enkele belangrijke stappen voor een juiste configuratie:

1. **Schakel virtualisatietechnologie** in: Eerst moet u controleren of uw systeem virtualisatietechnologie ondersteunt en of deze is ingeschakeld in de **BIOS** of **UEFI firmware** instellingen van het systeem. De stappen om toegang te krijgen tot virtualisatietechnologie en deze in te schakelen kunnen verschillen per fabrikant van het moederbord of de firmware. Raadpleeg de systeemdocumentatie of de website van de fabrikant voor specifieke instructies.

2. **Schakel Beveiliging op basis van virtualisatie (VBS)** in: Windows 11 bevat VBS, dat hardwarevirtualisatiemogelijkheden gebruikt om geïsoleerde containers te maken met de naam **Virtual Secure Mode (VSM)**. VSM biedt een veilige uitvoeringsomgeving voor kritieke systeemonderdelen en beschermt deze tegen mogelijke aanvallen. Voer de volgende stappen uit om VBS in te schakelen:

   - Druk op de **Windows-toets + R** om het dialoogvenster Uitvoeren te openen.
   - Typ "**gpedit.msc**" en druk op **Enter** om de Editor voor lokaal groepsbeleid te openen.
   - Navigeer naar **Computerconfiguratie -> Administratieve sjablonen -> Systeem -> Apparaatbewaking**.
   - Dubbelklik op het beleid **"Beveiliging op basis van virtualisatie inschakelen"**.
   - Selecteer **"Enabled"** en klik **OK** om de wijzigingen toe te passen.

   Het inschakelen van VBS kan compatibele hardware en bepaalde systeemvereisten vereisen. Raadpleeg de officiële **Microsoft documentatie** voor meer informatie.

3. **Schakel Hypervisor-beschermde code-integriteit (HVCI)** in: HVCI is een functie die de hypervisor gebruikt om beleidsregels voor code-integriteit af te dwingen, waardoor ongeoorloofde uitvoering van code wordt voorkomen en de algehele beveiligingsstatus wordt verbeterd. Voer de volgende stappen uit om HVCI in te schakelen:

   - Druk op **Windows-toets + R** om het dialoogvenster Uitvoeren te openen.
   - Typ "**msconfig**" en druk op **Enter** om het hulpprogramma Systeemconfiguratie te openen.
   - Navigeer naar het tabblad **"Opstarten"**.
   - Klik op **"Geavanceerde opties"**.
   - Vink de optie **"Enable Hypervisor-protected Code Integrity"** aan.
   - Klik op **OK** om de wijzigingen op te slaan en het systeem opnieuw op te starten.

   Het inschakelen van HVCI vereist compatibele hardware en bepaalde systeemvereisten. Raadpleeg de officiële **Microsoft documentatie** voor meer informatie.

Door standaard hardwarematige isolatiefuncties toe te passen, zoals VBS en HVCI, kunt u de beveiliging van uw Windows 11-systeem aanzienlijk verbeteren. Deze functies helpen om kritieke systeemonderdelen te beschermen tegen verschillende aanvallen, waaronder aanvallen die systeemcode en configuraties proberen te wijzigen of misbruiken.

Zorg ervoor dat u uw systeem regelmatig bijwerkt met de nieuwste beveiligingspatches en firmware-updates om te profiteren van de meest actuele beveiligingsverbeteringen en -beperkingen die deze hardwarematige isolatiefuncties bieden.

Houd er rekening mee dat de beschikbaarheid en vereisten van hardwarematige isolatiefuncties kunnen variëren afhankelijk van uw systeemconfiguratie en editie van Windows 11. Het wordt aanbevolen om de officiële **Microsoft documentatie** te raadplegen en compatibiliteitscontroles uit te voeren om de juiste implementatie van deze beveiligingsfuncties te garanderen.

#### 4. [**Windows Sandbox gebruiken**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)
**Windows Sandbox** is een waardevol hulpmiddel waarmee u niet-vertrouwde toepassingen of testsoftware kunt uitvoeren in een geïsoleerde omgeving, waardoor uw systeem een extra beveiligingslaag krijgt. Door Windows Sandbox te gebruiken, kunt u potentiële risico's beperken die gepaard gaan met het uitvoeren van niet-vertrouwde programma's.

Windows Sandbox creëert een lichte, tijdelijke bureaubladomgeving die volledig gescheiden is van uw hoofdbesturingssysteem. Alle wijzigingen die in de Sandbox worden gemaakt, worden verwijderd zodra je deze afsluit, zodat je primaire systeem onaangetast blijft.

Volg deze stappen om Windows Sandbox te gebruiken:

1. **Controleer de systeemvereisten**: Controleer voordat u verdergaat of uw systeem voldoet aan de vereisten voor het uitvoeren van Windows Sandbox. Over het algemeen heb je een Windows 10 Pro of Enterprise editie nodig en een processor met virtualisatiemogelijkheden ingeschakeld in de BIOS/UEFI firmware. Raadpleeg de officiële [**Microsoft-documentatie**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) voor specifieke systeemvereisten.

2. **Schakel Windows Sandbox** in: Windows Sandbox is een ingebouwde functie in Windows 10 Pro en Enterprise edities. Voer de volgende stappen uit om Windows Sandbox in te schakelen:

   - Druk op de **Windows-toets + R** om het dialoogvenster Uitvoeren te openen.
   - Typ "**appwiz.cpl**" en druk op **Enter** om het venster Programma's en onderdelen te openen.
   - Klik op **"Windows-functies in- of uitschakelen"** aan de linkerkant.
   - Scroll naar beneden en zoek **"Windows Sandbox"** in de lijst met functies.
   - Vink het vakje naast **"Windows Sandbox"** aan en klik op **OK** om het in te schakelen.
   - Windows installeert de benodigde onderdelen en mogelijk moet u het systeem opnieuw opstarten om de wijzigingen door te voeren.

3. **Start Windows Sandbox**: Zodra Windows Sandbox is ingeschakeld, kunt u het starten door de volgende stappen te volgen:

   - Open het **Start** menu en zoek naar **"Windows Sandbox"**.
   - Klik op de toepassing **"Windows Sandbox"** om deze te openen.
   - De Sandbox wordt gestart in een apart venster en biedt u een veilige omgeving om niet-vertrouwde toepassingen of testsoftware uit te voeren.

Houd er tijdens het uitvoeren van toepassingen in Windows Sandbox rekening mee dat de Sandbox-omgeving geïsoleerd is en ontworpen is om alle wijzigingen die erin worden gemaakt te verwijderen. Daarom is het cruciaal om je bestanden of gegevens buiten de Sandbox op te slaan als je ze moet bewaren.

Windows Sandbox is een effectief hulpmiddel voor het testen van onbekende software, het openen van verdachte bestanden of het verkennen van potentieel riskante websites. Het voegt een extra beschermingslaag toe door ervoor te zorgen dat alle kwaadaardige activiteiten of ongewenste wijzigingen beperkt blijven tot de Sandbox en geen invloed hebben op je hoofdbesturingssysteem.

Door Windows Sandbox op te nemen in je beveiligingspraktijken, kun je de risico's die gepaard gaan met het uitvoeren van niet-vertrouwde toepassingen aanzienlijk beperken en je systeem beschermen tegen potentiële bedreigingen.

{{< figure src="windows-sandbox-application-guard-isolation-architecture.webp" alt="Diagram van Windows Sandbox en Microsoft Defender Application Guard met geïsoleerde virtuele containers die het hostsysteem beschermen tegen niet-vertrouwde toepassingen en browsersessies" >}}

Raadpleeg voor meer informatie over Windows Sandbox en het gebruik ervan de officiële [**Microsoft-documentatie**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

#### 5. [**Microsoft Defender Application Guard implementeren**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)
Microsoft Defender Application Guard is een krachtige beveiligingsfunctie die browsersessies van Microsoft Edge isoleert van het onderliggende besturingssysteem. Door Edge in een veilige, geïsoleerde omgeving uit te voeren, helpt Application Guard je systeem te beschermen tegen browsergebaseerde aanvallen en schadelijke websites.

Volg deze stappen om Microsoft Defender Application Guard te implementeren en de beveiliging van uw browser te verbeteren:

1. **Controleer compatibiliteit**: Controleer voordat u verdergaat of uw systeem voldoet aan de vereisten voor het uitvoeren van Microsoft Defender Application Guard. Meestal hebt u een Windows 10 Pro of Enterprise-editie nodig, een compatibele processor met virtualisatiemogelijkheden en minstens 8 GB RAM. Raadpleeg de officiële [**Microsoft-documentatie**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) voor specifieke systeemvereisten.

2. **Schakel Application Guard** in: Application Guard is beschikbaar als optionele functie in Windows 10. Voer de volgende stappen uit om Microsoft Defender Application Guard in te schakelen:

   - Druk op de **Windows-toets + R** om het dialoogvenster Uitvoeren te openen.
   - Typ "**appwiz.cpl**" en druk op **Enter** om het venster Programma's en onderdelen te openen.
   - Klik op **"Windows-functies in- of uitschakelen"** aan de linkerkant.
   - Scroll naar beneden en zoek **"Microsoft Defender Application Guard"** in de lijst met functies.
   - Vink het vakje naast **"Microsoft Defender Application Guard"** aan en klik op **OK** om het in te schakelen.
   - Windows installeert de benodigde onderdelen en mogelijk moet u het systeem opnieuw opstarten om de wijzigingen door te voeren.

3. **Configureer Application Guard**: Zodra Application Guard is ingeschakeld, kunt u de instellingen configureren volgens uw beveiligingsbehoeften. Met Application Guard kunt u het isolatieniveau bepalen en bepalen hoe het omgaat met niet-vertrouwde websites en bestanden. Je kunt deze instellingen aanpassen via de app **Windows Security** of de instellingen voor Groepsbeleid.

4. **Testen en verifiëren**: Na het inschakelen en configureren van Microsoft Defender Application Guard is het essentieel om de functionaliteit te testen en te verifiëren. Open Microsoft Edge en bezoek een bekende schadelijke website of een site met potentiële risico's om te controleren of Application Guard de browsersessie met succes isoleert en potentiële aanvallen voorkomt.

Door Microsoft Defender Application Guard te implementeren, voegt u een extra beschermingslaag toe aan uw systeem door de browsersessies te isoleren en potentiële bedreigingen binnen de beveiligde omgeving te houden. Dit helpt uw systeem en gegevens te beschermen tegen browsergebaseerde aanvallen, zoals drive-by downloads, schadelijke scripts en zero-day exploits.

Raadpleeg voor meer gedetailleerde informatie over het configureren en gebruiken van Microsoft Defender Application Guard de officiële [**Microsoft-documentatie**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard)

#### 6. [**Controlled Folder Access**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Controlled Folder Access is een krachtige beveiligingsfunctie die beschikbaar is in Windows 11 en die belangrijke mappen helpt beschermen tegen ongeoorloofde wijzigingen door ransomware en andere kwaadaardige software. Door Toegang tot gecontroleerde mappen in te schakelen en de benodigde mappen toe te voegen aan de lijst met beveiligde mappen, kun je de beveiliging van je systeem verbeteren en mogelijk gegevensverlies voorkomen.

Volg deze stappen om Toegang tot gecontroleerde mappen te implementeren en uw belangrijke mappen te beschermen:

1. **Open Windows Beveiliging**: Druk op de **Windows-toets** op uw toetsenbord, typ "**Windows Beveiliging**" en selecteer de app **Windows Beveiliging** in de zoekresultaten.

2. **Navigeer naar Instellingen voor virus- en bedreigingsbescherming**: Klik in de Windows Security-app op het tabblad **"Virus- en bedreigingsbeveiliging"** in het linkermenu.

3. **Configureer gecontroleerde maptoegang**: Klik onder het gedeelte **"Bescherming tegen ransomware"** op **"Bescherming tegen ransomware beheren"** om de instellingen voor Toegang tot gecontroleerde mappen te openen.

4. **Schakel Toegang tot gecontroleerde mappen in**: Zet in de instellingen voor Toegang tot gecontroleerde mappen de schakelaar op **"Aan"** om de functie in te schakelen. Windows geeft een waarschuwing weer dat alleen vertrouwde toepassingen toegang hebben tot beveiligde mappen.

5. 5. **Beschermde mappen toevoegen**: Om aan te geven welke mappen moeten worden beschermd, klikt u op **"Beschermde mappen"** en selecteert u **"Een beschermde map toevoegen"**. Kies de mappen die u wilt beveiligen en klik op **"OK"**.

   - Het wordt aanbevolen om belangrijke mappen toe te voegen, zoals Documenten, Afbeeldingen, Video's en andere mappen met waardevolle gegevens.

6. **Applicaties toestaan of blokkeren**: Standaard geeft gecontroleerde maptoegang vertrouwde toepassingen toegang tot beveiligde mappen. U kunt dit gedrag echter aanpassen door te klikken op **"Een app toestaan via gecontroleerde maptoegang"**. Van daaruit kunt u specifieke toepassingen toestaan of blokkeren voor toegang tot de beveiligde mappen.

7. **Bewaken en controleren**: Nadat u Toegang tot gecontroleerde mappen hebt ingeschakeld, bewaakt Windows continu alle pogingen van niet-geautoriseerde toepassingen om toegang te krijgen tot beschermde mappen en registreert deze. U kunt deze logboeken bekijken door te klikken op **"Bekijken"** onder het gedeelte **"Onlangs geblokkeerde toepassingen"** in de instellingen voor Toegang tot gecontroleerde mappen.

Door de gecontroleerde maptoegang te implementeren, voegt u een extra beschermingslaag toe aan uw belangrijke mappen en beperkt u het risico op onbevoegde wijzigingen en mogelijk gegevensverlies door ransomware-aanvallen. Controleer regelmatig de instellingen voor Toegang tot gecontroleerde mappen om ervoor te zorgen dat de beveiligde mappen voldoen aan uw beveiligingsvereisten.

Raadpleeg voor meer gedetailleerde informatie over het configureren en gebruiken van gecontroleerde maptoegang de officiële [**Microsoft-documentatie**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide)

#### 7. **Automatisch onderhoud van Windows inschakelen**
Windows 11 bevat een handige functie met de naam Automatisch onderhoud die helpt om je systeem geoptimaliseerd en beschermd te houden door regelmatig onderhoudstaken uit te voeren. Door Automatisch onderhoud in te schakelen, zorgt u ervoor dat uw systeem soepel draait en veilig blijft.

Voer de volgende stappen uit om automatisch onderhoud van Windows in te schakelen:

1. **Open Windows Instellingen**: Druk op de **Windows-toets** op uw toetsenbord, typ "**Instellingen**" en selecteer de app **Instellingen** in de zoekresultaten.

2. **Toegang krijgen tot de Onderhoudsinstellingen**: Klik in de Instellingen-app op de categorie **"Systeem"** en selecteer vervolgens **"Over"** in het linkermenu. Scroll naar beneden en klik op de link **"Systeeminfo"**.

3. **Open Onderhoudsinstellingen**: Klik in het venster Systeeminfo op de link **"Onderhoud"** onderaan de pagina.

4. 4. **Automatisch onderhoud inschakelen**: Zet in de Onderhoudsinstellingen de schakelaar naast **"Automatisch onderhoud"** op de stand **"Aan"**.

5. **De onderhoudsinstellingen configureren**: Standaard plant Windows de onderhoudstaken automatisch dagelijks om 2:00 uur. Als u de voorkeur geeft aan een ander schema, klikt u op **"Onderhoudsinstellingen wijzigen"** en past u de gewenste opties aan, zoals de starttijd van het onderhoud en de frequentie van de onderhoudstaken.

6. **Bekijk extra instellingen**: Onder de schakelaar Automatisch onderhoud vindt u aanvullende instellingen met betrekking tot onderhoud, zoals **"Laat gepland onderhoud mijn computer op het geplande tijdstip wekken"** en **"Laat gepland onderhoud zelfs uitvoeren als ik op de batterij werk"**. Pas deze instellingen aan volgens je voorkeuren en vereisten.

7. **Monitor onderhoudsactiviteiten**: Zodra Automatisch onderhoud is ingeschakeld, voert Windows automatisch onderhoudstaken uit op de achtergrond op het geplande tijdstip. U kunt deze activiteiten controleren door de **"Onderhoud"** sectie in de **"Windows Beveiliging"** app te controleren of door de **"Onderhoud"** logs in de Event Viewer te bekijken.

Het inschakelen van Windows Automatisch Onderhoud zorgt ervoor dat uw systeem geoptimaliseerd en beschermd blijft door regelmatig essentiële onderhoudstaken uit te voeren, zoals software-updates, schijfoptimalisatie en beveiligingsscans. Door uw systeem gezond te houden, kunt u genieten van een soepelere en veiligere computerervaring.

Raadpleeg voor meer gedetailleerde informatie over Windows automatisch onderhoud en de configuratieopties de officiële [**Microsoft-documentatie**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence)

______

## Aanbevolen volgorde voor hardening

Pas beveiligingsmaatregelen toe in een volgorde die eerst de toegang en het herstel beschermt:

1. Controleer de Windows-editie en build, de ondersteuningsstatus, beschikbare hardwarebeveiliging en herstelopties.
2. Installeer de actuele beveiligingsupdates en start opnieuw op tijdens een gepland onderhoudsvenster.
3. Maak een geteste back-up en leg de huidige status vast van de firewall, Defender, BitLocker, services en lokaal beleid.
4. Houd UAC ingeschakeld, gebruik aparte beheerdersaccounts en vereis MFA voor ondersteunde externe toegang en cloudtoegang.
5. Schakel Defender-beveiliging, firewallprofielen, Secure Boot, BitLocker en hardware-isolatie in als de editie en hardware deze ondersteunen.
6. Test ASR-regels, Controlled Folder Access, AppLocker en servicewijzigingen eerst in audit- of pilotmodus voordat je ze breed blokkeert of uitschakelt.
7. Centraliseer logboeken en controleer mislukte aanmeldingen, beleidswijzigingen, Defender-gebeurtenissen en geblokkeerd firewallverkeer.
8. Start opnieuw op, test vereiste toepassingen, controleer de toegang tot herstel en documenteer de eindstatus.

De [Microsoft Security Compliance Toolkit](https://learn.microsoft.com/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10) biedt versiegebonden baselines voor Windows 10, Windows 11 en Windows Server. Gebruik de passende baseline als beoordeeld startpunt. Microsoft adviseert wijzigingen aan baselines te testen voordat je ze in productie inzet.

## Ondersteuningsgrens van Windows 10

Microsoft heeft de ondersteuning voor Windows 10 versie 22H2 op 14 oktober 2025 beëindigd. Een geharde Windows 10-installatie ontvangt na die datum geen reguliere beveiligingsupdates, tenzij een afzonderlijke levenscyclus- of Extended Security Update-regeling geldt. Neem migratie, vervanging of een goedgekeurde uitzondering op in het beveiligingsplan. Hardening verlengt de productlevenscyclus niet. Zie Microsofts [bericht over het einde van ondersteuning voor Windows 10](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).

## Wijzigingen aan services en functies terugdraaien

Een service uitschakelen vereist tests van afhankelijkheden en workloads. Schakel **RPC**, **Windows Update**, **Windows Event Log** of een andere service niet uit omdat een algemene lijst deze overbodig noemt. De servicenaam alleen beschrijft de rol op jouw systeem niet.

Exporteer vóór een wijziging de serviceconfiguratie en noteer afhankelijke services:

```powershell
$name = 'Spooler'
Get-CimInstance Win32_Service -Filter "Name='$name'" |
    Select-Object Name, DisplayName, State, StartMode, StartName, PathName |
    Export-Csv "C:\Temp\$name-before.csv" -NoTypeInformation
Get-Service -Name $name -DependentServices
Get-Service -Name $name -RequiredServices
```

Wijzig één service tegelijk. Kies **Manual** vóór **Disabled** wanneer een workload de service op aanvraag start. Noteer het eerdere opstarttype. Controleer na de test het gedrag van toepassingen, Logboeken, Windows Update, afdrukken, extern beheer, VPN-toegang en geplande taken.

Draai de wijziging terug door het vastgelegde opstarttype te herstellen. Start de service pas nadat je de afhankelijkheden hebt gecontroleerd:

```powershell
Set-Service -Name $name -StartupType Manual
Start-Service -Name $name
Get-Service -Name $name
```

Herstel bij een bredere beleidswijziging de opgeslagen GPO- of registerback-up met hetzelfde beheertool waarmee je die hebt gemaakt. Zorg vóór wijzigingen op afstand voor een offline herstelroute en de gegevens van een lokaal beheerdersaccount. Microsoft documenteert de syntaxis voor serviceconfiguratie bij [`sc.exe config`](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-config).

## Validatierecord voor maatregelen

Noteer voor elke hardeningwijziging de maatregel, scope, vorige waarde, nieuwe waarde, testresultaat, gecontroleerde gebeurtenis-ID's, eigenaar en opdracht om terug te draaien. Een geblokkeerde toepassing of defecte printer is een operationele bevinding, geen bewijs dat de maatregel verkeerd is. Pas de scope, uitzonderingen of implementatiering aan nadat je de gegevens hebt beoordeeld.

______

## Conclusie

Deze **best practices voor Windows-hardening** toepassen is essentieel om je Windows-systemen te beveiligen. Door je besturingssysteem regelmatig **bij te werken**, dicht je beveiligingslekken en verbeter je de stabiliteit. Beveiligingsfuncties zoals **antivirus** en **versleuteling** voegen bescherming toe aan je gegevens. Passende **toegangscontroles** helpen ongeautoriseerde wijzigingen voorkomen en beperken toegang tot gevoelige bronnen.

Met deze best practices verbeter je de beveiliging van je **Windows-omgeving**, bescherm je je gegevens en behoud je de integriteit van je **digitale infrastructuur**. Blijf **proactief** en beoordeel en actualiseer je beveiligingsmaatregelen regelmatig om potentiële bedreigingen voor te blijven.

Onthoud dat **Windows-hardening** een doorlopend proces is. Blijf op de hoogte van de nieuwste beveiligingsupdates en werkwijzen. Door proactief te blijven en deze best practices toe te passen, beperk je beveiligingsrisico's en bescherm je je Windows-systemen.

Raadpleeg voor meer informatie over Windows-hardening en best practices betrouwbare bronnen zoals **Microsoft-documentatie**, **beveiligingsforums** en vertrouwde **cybersecuritywebsites**.

______

## Referenties:

- [Microsoft Windows Security](https://www.microsoft.com/en-us/security)
- [NIST Special Publication 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [CIS Microsoft Windows 10 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [CIS Microsoft Windows 11 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_11/)
