---
title: "Rayhunter-apparaten flashen: complete handleiding"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Flash en configureer Rayhunter voor detectie van IMSI-catchers. Bekijk ondersteunde apparaten, installeer de firmware, controleer de werking en los veelvoorkomende problemen op."
tags: ["Rayhunter", "IMSI-catcher", "celsitesimulator", "mobiele beveiliging", "surveillancedetectie", "privacybescherming", "Orbic RC400L", "TP-Link M7350", "mobiele hotspot", "apparaten flashen", "cyberbeveiliging", "draadloze beveiliging", "maatregelen tegen surveillance", "EFF", "privacytools", "Rayhunter kopen", "installatiehandleiding", "configuratie", "ondersteunde apparaten", "netwerkbeveiliging"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Een Rayhunter-apparaat detecteert draadloze signalen en IMSI-catchers, met beveiligingsschilden eromheen"
coverCaption: "Rayhunter-systeem voor IMSI-catcherdetectie, ter bescherming van mobiele communicatie tegen surveillance"
---

**Complete handleiding voor het flashen en configureren van Rayhunter, het detectiesysteem voor IMSI-catchers.**

## Kort samengevat

**Rayhunter** is een opensource detectiesysteem voor IMSI-catchers dat op aangepaste mobiele hotspots draait. Het waarschuwt je wanneer surveillanceapparatuur mobiele communicatie probeert te onderscheppen. Deze handleiding behandelt de volledige installatie op de Orbic RC400L en TP-Link M7350, de configuratie, dreigingsanalyse en werking op 5G-netwerken. Je hebt een compatibel apparaat met een Qualcomm-modem nodig. Het systeem detecteert surveillance op 2G-, 3G- en 4G-netwerken met meerdere heuristieken. Het blijft nuttig ondanks de opkomst van 5G, omdat aanvallen die apparaten naar oudere netwerken terugschakelen nog steeds voorkomen. Rayhunter biedt bescherming aan journalisten, activisten en privacybewuste mensen tegen overheidssurveillance, criminelen en bedrijven.

**Rayhunter** detecteert IMSI-catchers, ook wel celsitesimulators genoemd, die mobiele communicatie kunnen onderscheppen. Zoek je **Rayhunter te koop**, of wil je weten hoe je deze apparaten flasht en configureert? Deze handleiding behandelt de installatie, configuratie en het gebruik van **Rayhunter**.

**Sponsorvermelding:** Dit artikel wordt gesponsord door [STS Collective](https://stscollective.com), de belangrijkste leverancier van Rayhunter-compatibele apparaten. Ondanks deze sponsoring zijn alle technische informatie, analyses en aanbevelingen in deze handleiding gebaseerd op de officiële Rayhunter-documentatie, feedback van de community en een objectieve technische beoordeling.

> 💰 **Exclusieve lezerskorting:** Bespaar tot 20% op Rayhunter-apparaten en producten van STS Collective. Gebruik code **SIMEONONSECURITY** bij het afrekenen of [winkel direct met de korting](https://stscollective.com/discount/SIMEONONSECURITY).

## Kennismaking met Rayhunter

**Rayhunter** is een geavanceerd detectiesysteem voor IMSI-catchers, ontwikkeld door de **Electronic Frontier Foundation (EFF)**, een vooraanstaande non-profitorganisatie die burgerrechten in de digitale wereld verdedigt. Sinds 1990 zet EFF zich in voor digitale privacy, vrije meningsuiting en innovatie via rechtszaken, beleidsanalyses, activisme en technologieontwikkeling.

De tool draait op compatibele mobiele hotspotapparaten en controleert voortdurend mobiele netwerken op verdachte activiteit die kan wijzen op celsitesimulators of Stingrays die voor surveillance worden gebruikt. **Rayhunter** weerspiegelt het streven van EFF om praktische hulpmiddelen voor privacybescherming te bieden aan mensen en organisaties die bescherming tegen surveillance nodig hebben.

**Rayhunter** geeft direct een waarschuwing wanneer mogelijk schadelijk gedrag op het mobiele netwerk wordt gedetecteerd. Daarmee is het een belangrijk hulpmiddel voor journalisten, activisten, beveiligingsprofessionals en privacybewuste mensen. Compatibele apparaten zijn **[te koop met Rayhunter](https://stscollective.com/collections/rayhunter)** bij STS Collective, de belangrijkste leverancier van deze gespecialiseerde apparaten.

### Het Rayhunter-project steunen

**Rayhunter** is een opensourceproject dat baat heeft bij steun uit de community. Je kunt op verschillende manieren bijdragen aan de verdere ontwikkeling:

- **Aankopen via STS Collective**: STS Collective schenkt een deel van de winst van elk verkocht Rayhunter-apparaat aan EFF, ter ondersteuning van de verdere ontwikkeling van **Rayhunter** en privacyonderzoek.
- **Rechtstreeks doneren**: Steun de bredere inzet van EFF voor privacy en de ontwikkeling van **Rayhunter** via **[Doneer aan EFF](https://supporters.eff.org/donate/donate)**.
- **Deelnemen aan de gemeenschap**: Draag bij aan gesprekken, documentatie en tests via de officiële GitHub-repository.

Met je steun blijft **Rayhunter** gratis, opensource en voortdurend verbeterd om op nieuwe surveillancedreigingen te reageren.

## Ondersteuning, reacties en gemeenschap

**Rayhunter** wordt ondersteund door een actieve community van beveiligingsonderzoekers, privacyvoorvechters en betrokken burgers. Je kunt via verschillende kanalen ondersteuning krijgen en bijdragen:

- **Officiële documentatie**: [Rayhunter-documentatie](https://efforg.github.io/rayhunter/introduction.html), met volledige handleidingen voor installatie, configuratie en gebruik
- **GitHub-repository**: [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Communitygesprekken**: Open GitHub-discussies over apparaatcompatibiliteit en probleemoplossing
- **Beveiligingsonderzoek**: Werk met onderzoekers samen om de detectiemogelijkheden van **Rayhunter** te verbeteren

Compatibele apparaten zijn **[te koop met Rayhunter](https://stscollective.com/collections/rayhunter)** bij STS Collective.

## Veelgestelde vragen

### Heb ik een actieve simkaart nodig voor Rayhunter?

**Rayhunter** vereist een simkaart in het apparaat, maar de kaart heeft geen actief abonnement nodig. De simkaart is nodig om verbinding te maken met mobiele netwerken en verdachte activiteit te controleren. Als je het apparaat tijdens het gebruik van **Rayhunter** als hotspot wilt gebruiken, heb je wel een actief abonnement nodig.

### Hoe controleer ik of mijn Rayhunter-apparaat werkt?

Schakel de testheuristiek in via de configuratie-instellingen van **Rayhunter**. Het apparaat geeft dan telkens een waarschuwing wanneer het een zendmast detecteert, zodat je kunt controleren of het systeem werkt. Deze test veroorzaakt veel meldingen. Schakel hem na de test weer uit.

### Moet ik een vergrendeld of ontgrendeld apparaat kopen?

Voor **Rayhunter** hebben ontgrendelde apparaten meestal de voorkeur, vooral als je simkaarten van andere providers dan Verizon wilt gebruiken. De meeste Orbic-apparaten van Verizon zijn in werkelijkheid ontgrendeld, maar controleer de compatibiliteit voor aankoop. Gecontroleerde compatibele apparaten zijn **[te koop met Rayhunter](https://stscollective.com/collections/rayhunter)** bij STS Collective.

{{< stscollective-ad "rayhunter" >}}

## Installatiehandleiding

### Installeren vanuit de nieuwste versie

De installatie van **Rayhunter** is getest op macOS en Ubuntu 24.04. Als je problemen ondervindt met vooraf gebouwde releases, moet je het mogelijk vanuit de broncode installeren.

#### Benodigdheden

Controleer vóór installatie van **Rayhunter** of je een compatibel apparaat hebt. Plaats bij TP-Link-apparaten een SD-kaart die met FAT is geformatteerd om opnamen op te slaan.

#### Downloaden en instellen

1. **Download de nieuwste release**: haal het juiste bestand `rayhunter-vX.X.X-PLATFORM.zip` op via de officiële pagina met versies:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Pak het bestand uit en open de map**:
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Maak verbinding met je apparaat**: Zet het apparaat aan en verbind via WiFi of USB-tethering. Je moet toegang hebben tot:
   - Orbic-apparaten: `http://192.168.1.1`
   - TP-Link-apparaten: `http://192.168.0.1`

#### Installatie per apparaat

**Voor Orbic RC400L-apparaten** (verkrijgbaar **[met Rayhunter](https://stscollective.com)**):

**Rayhunter** ondersteunt twee installatiemethoden voor Orbic RC400L-apparaten. De WiFi-methode wordt voor de meeste gebruikers aanbevolen. De USB-methode biedt extra mogelijkheden om fouten op te sporen.

**Installatie via WiFi (aanbevolen)**:
```bash
# macOS-gebruikers moeten dit eerst uitvoeren:
xattr -d com.apple.quarantine installer

# Voor Verizon RC400L (beheerderswachtwoord is gelijk aan het WiFi-wachtwoord):
./installer orbic --admin-password 'YourWiFiPassword'

# Voor Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Voor Moxee-apparaten (wachtwoordnotatie: 12$ + laatste 3 cijfers van het WiFi-wachtwoord):
./installer orbic --admin-password='12$XXX'
```

**Installatie via USB (gevorderde gebruikers)**:
De USB-methode biedt toegang tot ADB (Android Debug Bridge) voor geavanceerde foutopsporing, maar wordt afgeraden voor standaardinstallaties:

```bash
# WAARSCHUWING: de USB-installer wordt voor de meeste toepassingen afgeraden
./installer orbic-usb
```

Deze methode zet het apparaat in de foutopsporingsmodus om ADB-toegang mogelijk te maken, installeert rootshell en **Rayhunter** en start het apparaat opnieuw op. Gebruik deze methode alleen als je voor andere doeleinden ADB-toegang nodig hebt.

**Voor TP-Link M7350-apparaten** (verkrijgbaar **[met Rayhunter](https://stscollective.com)**):
```bash
./installer tplink
```

De installer voltooit het flashen van **Rayhunter** en start het apparaat opnieuw op. Een groene lijn op het scherm geeft aan dat **Rayhunter** actief is.

### Installeren vanuit de broncode

Voor ontwikkelaars en gebruikers die **Rayhunter** zelf willen bouwen, bevat het project:

- **Frontend**: SvelteKit-applicatie in JavaScript (`./daemon/web/`)
- **Backend**: Rust-binary `rayhunter-daemon` (`./daemon/`)
- **Installer**: Rust-binary met alle onderdelen (`./installer`)

#### Afhankelijkheden voor bouwen

Installeer de volgende afhankelijkheden:
- De programmeertaal Rust
- Node.js/npm
- Hulpmiddelen voor C-compilatie (`build-essential` op Linux, `xcode-select --install` op macOS)

#### Bouwproces

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Vervang 'orbic' door het type apparaat
```

Voor frontendontwikkeling met automatisch herladen:
```bash
cd daemon/web
npm run dev
# Of met een aangepast doel:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Rayhunter updaten

**Rayhunter** bijwerken verloopt hetzelfde als de installatie. Herhaal de installatiestappen met de nieuwste release om je apparaat naar de nieuwste versie van **Rayhunter** bij te werken.

## Configuratie

Je kunt **Rayhunter** configureren via de webinterface of door `/data/rayhunter/config.toml` rechtstreeks op het apparaat te bewerken.

### Configuratie via de webinterface

Open de webinterface van **Rayhunter** door verbinding te maken met het netwerk van je apparaat en naar het volgende adres te gaan:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Dashboard van de Rayhunter-webinterface" caption="De Rayhunter-webinterface biedt uitgebreide bewakings- en configuratieopties" >}}

#### Belangrijke configuratieopties

**Schermniveau apparaat**: bepaalt wat **Rayhunter** op het apparaatscherm toont:
- **Onzichtbare modus**: geen weergave
- **Subtiele modus**: gekleurde indicator (groen = veilig, rood = waarschuwing, wit = gepauzeerd)
- **Demomodus**: toont afbeeldingen van een orka met een statusregel
- **EFF-logo**: toont het EFF-logo met een statusregel
- **Hoge zichtbaarheid**: schermvullende kleurweergave

**Invoermodus apparaat**: configureer de werking van de aan-uitknop:
- **Knopbediening uitschakelen**: de aan-uitknop is uitgeschakeld voor **Rayhunter**
- **Dubbeltikken om opname opnieuw te starten**: wis waarschuwingen en start de bewaking opnieuw

**Meldingsinstellingen**: stel de ntfy-URL voor meldingen op afstand in en schakel meldingstypen voor waarschuwingen en een bijna lege batterij in of uit.

**Analyzer-heuristieken**: schakel specifieke detectiealgoritmen van **Rayhunter** in of uit op basis van je omgeving en dreigingsmodel.

## Rayhunter verwijderen

### Orbic-apparaten

Verwijder **Rayhunter** van Orbic-apparaten met:

```bash
./installer util orbic-shell --admin-password mypassword
```

Voer in de shell het volgende uit:

> **Waarschuwing:** Met de volgende opdrachten verwijder je Rayhunter-bestanden en de opstartkoppelingen definitief. Controleer of je in de juiste apparaatshell zit, kopieer benodigde opnamen of configuratie en houd de installer en compatibele firmware bij de hand voordat je doorgaat. Controleer na afloop of de bestanden ontbreken en of het apparaat opnieuw opstart zonder de Rayhunter-service. Installeer de bijpassende release opnieuw vanuit de officiële repository als je wilt terugdraaien.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### TP-Link-apparaten

Verwijder Rayhunter van een TP-Link-apparaat met:

> **Waarschuwing:** Deze opdrachten verwijderen Rayhunter-bestanden en de opstartkoppeling van het TP-Link-apparaat. Exporteer eerst opnamen en configuratie. Voer de opdrachten alleen uit in de apparaatshell, controleer daarna of de paden ontbreken en of het apparaat normaal opstart. Installeer de bijpassende release opnieuw vanuit de officiële repository om terug te draaien.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Verwijder eventuele resterende poorttriggers in de TP-Link-beheerinterface onder Settings > NAT Settings > Port Triggers.

## Rayhunter gebruiken

Na installatie start **Rayhunter** automatisch en controleert het voortdurend mobiele netwerken op verdachte activiteit. Bij normaal gebruik toont het apparaatscherm een groene lijn. Bij mogelijke IMSI-catchers verandert die in gele stippen, oranje streepjes of een ononderbroken rode lijn.

### Detectieheuristieken van Rayhunter

**Rayhunter** gebruikt meerdere geavanceerde detectiealgoritmen om mogelijke activiteit van IMSI-catchers vast te stellen:

#### Detectie van IMSI-verzoeken
Deze heuristiek herkent verdachte reeksen waarin zendmasten de apparaatidentiteit opvragen (IMSI, International Mobile Subscriber Identity) zonder de juiste authenticatieprocedures te volgen. **Rayhunter** controleert de timing en context van deze verzoeken en markeert afwijkende patronen die op surveillanceapparatuur kunnen wijzen.

Legitieme mobiele netwerken volgen gestandaardiseerde authenticatieprocedures voordat ze gevoelige identificatiegegevens opvragen. IMSI-catchers omzeilen deze procedures vaak om apparaatidentiteiten snel te verzamelen. Dat veroorzaakt herkenbare afwijkingen in de authenticatiereeks. Deze detectiemethode werkt vooral goed tegen eenvoudige "passieve" IMSI-catchers die alleen apparaatgegevens verzamelen.

#### Detectie van verbindingsverbreking en terugschakelen naar 2G
**Rayhunter** controleert voortdurend op verdachte pogingen om mobiele apparaten de verbinding met beveiligde 4G- of 5G-netwerken te laten verbreken en opnieuw verbinding te laten maken met minder veilige 2G-netwerken. IMSI-catchers gebruiken deze aanval vaak, omdat 2G-netwerken zwakkere versleuteling hebben en makkelijker te onderscheppen zijn.

Het systeem analyseert patronen in verbindingsverbrekingen en let op afwijkende frequentie, timing en context die op kwaadwillige bedoelingen kunnen wijzen in plaats van normale netwerkoptimalisatie. Legitieme netwerken stellen soms voor om terug te schakelen vanwege dekking of capaciteit, maar **Rayhunter** kan dit onderscheiden van mogelijke surveillance.

#### Detectie van terugschakelen via LTE SIB6/7
System Information Blocks (SIB's) zijn broadcastberichten waarmee mobiele netwerken configuratiegegevens naar apparaten sturen. **Rayhunter** controleert specifiek berichten SIB6 en SIB7, die informatie over naburige cellen en frequentieomleiding bevatten.

Kwaadwillenden kunnen valse SIB6/7-berichten uitzenden om apparaten beveiligde 4G-verbindingen te laten verlaten en verbinding te laten maken met 2G-netwerken die zij beheren. **Rayhunter** analyseert deze uitzendingen op tegenstrijdigheden, afwijkende omleidingspatronen en andere aanwijzingen voor malafide basisstations die apparaten voor onderschepping proberen terug te schakelen.

#### Detectie van nulversleuteling
Deze belangrijke detectiemethode herkent wanneer een mobiel netwerk voorstelt om communicatie zonder versleuteling te verzenden, met een nulversleuteling. Legitieme commerciële mobiele netwerken horen nooit onversleutelde verbindingen voor te stellen, omdat dit beveiligingsnormen en regelgeving schendt.

**Rayhunter** markeert elk netwerk dat nulversleuteling voorstelt als zeer verdacht. *Een legitiem netwerk stelt nooit nulversleuteling voor.* Dit wijst duidelijk op surveillanceapparatuur die communicatie als platte tekst probeert te onderscheppen. Deze heuristiek werkt vooral goed tegen IMSI-catchers die gegevensverzameling belangrijker vinden dan een legitiem netwerk nabootsen.

#### Detectie van onvolledige SIB's
Legitieme mobiele basisstations zenden volledige System Information Blocks uit met essentiële netwerkconfiguratiegegevens. **Rayhunter** controleert op basisstations die onvolledige of ontbrekende systeeminformatie versturen. Dit wijst vaak op haastig ingezette of onjuist geconfigureerde surveillanceapparatuur.

IMSI-catchers implementeren vaak niet alle functies van een mobiel netwerk. Ze richten zich op de minimale functies die nodig zijn om apparaten te verbinden en gegevens te onderscheppen. Door zulke onvolledige implementaties te detecteren, kan **Rayhunter** mogelijk malafide basisstations vinden die niet de volledige functieset van legitieme mobiele infrastructuur hebben.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Diagram met de vijf detectieheuristieken van Rayhunter: een IMSI-verzoek zonder authenticatie, terugschakelen naar 2G, LTE SIB6/7-omleiding, voorstel voor nulversleuteling en onvolledige systeeminformatie" >}}
## Dreigingsactoren en mogelijke doelwitten

Het is belangrijk te begrijpen wie IMSI-catchers inzet en op wie die zijn gericht. Zo bepaal je je persoonlijke dreigingsmodel en de juiste configuratie van **Rayhunter**. Dreigingsactoren verschillen in technische verfijning. Hun doelwitten bepalen mede welke vormen van surveillance **Rayhunter** kan detecteren.

### Overheidsdiensten en politie

**Technisch niveau van de dreiging**: geavanceerd tot professioneel
**Belangrijkste doelwitten**:
- Verdachten die worden onderzocht
- Personen van belang in zaken rond nationale veiligheid
- Demonstranten en activisten tijdens protesten
- Algemene surveillance in gebieden met hoge beveiliging
- Buitenlandse onderdanen en diplomatiek personeel

**Detectiepatronen**: IMSI-catchers van overheidsdiensten gebruiken vaak geavanceerde apparatuur die eenvoudige detectieheuristieken kan omzeilen. Ze zetten echter geregeld **aanvallen in die verbindingen naar 2G terugschakelen** en **patronen met verbindingsverbrekingen** in om apparaten naar minder veilige netwerken te dwingen en zo eenvoudiger communicatie te onderscheppen. De detectie van terugschakeling via LTE SIB6/7 en de controle op verbindingsverbrekingen door **Rayhunter** zijn bijzonder effectief tegen surveillancetechnieken van politie en opsporingsdiensten.

**Veelvoorkomende scenario's**:
- Surveillance tijdens protesten, demonstraties of openbare bijeenkomsten
- Locatiegebonden controle bij overheidsgebouwen of gevoelige infrastructuur
- Gerichte surveillance van specifieke personen die worden onderzocht
- Surveillance bij grenzen en luchthavens

### Inlichtingendiensten in binnen- en buitenland

**Technisch niveau van de dreiging**: professioneel tot militair
**Belangrijkste doelwitten**:
- Buitenlandse inlichtingenagenten en bronnen
- Overheidsfunctionarissen en diplomatiek personeel
- Defensieaannemers en onderzoekers
- Bestuurders in strategische sectoren
- Journalisten die over nationale veiligheid schrijven
- Activisten die aan gevoelige politieke kwesties werken

**Detectiepatronen**: apparatuur van inlichtingendiensten is ontworpen om onopvallend te werken, maar de detectie van nulversleuteling en onvolledige SIB's door **Rayhunter** kan zelfs geavanceerde surveillance aantonen. Inlichtingendiensten gebruiken tijdens gerichte operaties vaak apparatuur die **IMSI-informatie** opvraagt. Daardoor worden de detectiealgoritmen van **Rayhunter** voor IMSI-verzoeken geactiveerd.

**Veelvoorkomende scenario's**:
- Langdurige surveillance van waardevolle inlichtingendoelwitten
- Industriële spionage bij bedrijfshoofdkantoren
- Bewaking van diplomatieke missies en ambassades
- Contra-inlichtingenoperaties
- Buitenlandse inlichtingendiensten die binnenlandse bronnen als doelwit kiezen

### Criminele organisaties

**Technisch niveau van de dreiging**: basis tot gemiddeld
**Belangrijkste doelwitten**:
- Vermogende personen voor ontvoering of afpersing
- Bedrijfsconcurrenten voor bedrijfsinformatie
- Opsporingsambtenaren die georganiseerde misdaad onderzoeken
- Getuigen en informanten in strafzaken
- Slachtoffers van stalking, intimidatie of huiselijk geweld

**Detectiepatronen**: criminele organisaties gebruiken vaak goedkopere, commercieel verkrijgbare IMSI-catchers die meerdere detectieheuristieken van **Rayhunter** tegelijk activeren. Deze apparaten hebben vaak **onvolledige SIB-implementaties**, gebruiken **nulversleuteling** om zoveel mogelijk gegevens te verzamelen en voeren agressieve **aanvallen uit die naar 2G terugschakelen**, omdat hun technische kennis beperkt is.

**Veelvoorkomende scenario's**:
- Mogelijke slachtoffers van ontvoering of beroving volgen
- Mobiele communicatie van politie tijdens criminele operaties controleren
- Industriële spionage en informatie over concurrenten verzamelen
- Stalking en intimidatie
- Getuigen intimideren en hun locatie volgen

### Bedrijfsspionage en particuliere inlichtingendiensten

**Technisch niveau van de dreiging**: gemiddeld tot geavanceerd
**Belangrijkste doelwitten**:
- Bestuurders van concurrerende bedrijven
- Onderzoeks- en ontwikkelingsteams
- Onderhandelaars bij fusies en overnames
- Eigenaren van intellectueel eigendom
- Beheerders van bedrijfsgeheimen
- Klokkenluiders en bronnen van interne dreigingen

**Detectiepatronen**: bedrijfssurveillance gebruikt vaak apparatuur uit het middensegment, met een balans tussen kosten en mogelijkheden. Zulke inzet activeert geregeld **detectie van verbindingsverbrekingen** en **waarschuwingen voor IMSI-verzoeken** wanneer specifieke personen tijdens zakelijke onderhandelingen of productontwikkelingscycli doelwit zijn.

**Veelvoorkomende scenario's**:
- Surveillance tijdens onderhandelingen over fusies en overnames
- Informatie over concurrenten verzamelen op vakbeurzen en congressen
- Diefstal van intellectueel eigendom
- Werknemers controleren en interne dreigingen opsporen
- Klantgegevens verzamelen om een concurrentievoordeel te behalen

### Particuliere onderzoekers en surveillancebedrijven

**Technisch niveau van de dreiging**: basis tot gemiddeld
**Belangrijkste doelwitten**:
- Personen die worden onderzocht wegens verzekeringsfraude
- Partners tijdens echtscheidingsprocedures
- Werknemers die van wangedrag worden verdacht
- Personen die betrokken zijn bij juridische geschillen
- Beroemdheden en andere prominente doelwitten

**Detectiepatronen**: particuliere surveillance gebruikt doorgaans commercieel verkrijgbare apparatuur met beperkte aanpassingsmogelijkheden. Door kosten en technische beperkingen activeren deze systemen vaak de basisheuristieken van **Rayhunter**, met name **detectie van nulversleuteling** en **controle op onvolledige SIB's**.

**Veelvoorkomende scenario's**:
- Onderzoeken bij echtscheidings- en voogdijzaken
- Surveillance bij verzekeringsfraude
- Onderzoeken naar wangedrag van werknemers
- Stalking van beroemdheden en paparazzi-activiteiten
- Juridische onderzoeken en bewijs verzamelen

### Kwaadwillende personen en hacktivisten

**Technisch niveau van de dreiging**: basis tot gemiddeld
**Belangrijkste doelwitten**:
- Persoonlijke vijanden of romantische partners
- Publieke figuren en beroemdheden
- Willekeurige slachtoffers in openbare ruimten
- Deelnemers aan bepaalde evenementen of personen op specifieke locaties
- Leden van doelgerichte gemeenschappen of groepen

**Detectiepatronen**: individuele daders gebruiken vaak eenvoudige, soms geïmproviseerde IMSI-catchers die meerdere detectiealgoritmen van **Rayhunter** tegelijk activeren. Deze apparaten vertonen geregeld **gebruik van nulversleuteling**, **onvolledige SIB-uitzendingen** en primitieve **pogingen om naar 2G terug te schakelen**.

**Veelvoorkomende scenario's**:
- Stalking en intimidatie
- Identiteitsdiefstal en financiële fraude
- Politiek activisme verstoren en protesten hinderen
- Algemene cybercriminaliteit
- Opportunistische surveillance tijdens openbare evenementen

### Dreigingsbeoordeling en Rayhunter configureren

**Mensen met een hoog risico** (journalisten, activisten, overheidsfunctionarissen en bestuurders) schakelen alle heuristieken van **Rayhunter** in en kiezen de weergavemodus **hoge zichtbaarheid** voor maximale detectie.

**Mensen met een gemiddeld risico** (algemene privacybewuste gebruikers) kunnen voor dagelijkse bescherming de **subtiele modus** gebruiken en de belangrijkste detectieheuristieken inschakelen zonder aandacht te trekken.

**Bescherming tijdens evenementen** (protesten, gevoelige bijeenkomsten en reizen) is gebaat bij tijdelijke activering van alle detectiemethoden en meldingssystemen, voor volledig inzicht in surveillance.

Als je je dreigingsmodel begrijpt, kun je **Rayhunter** op je specifieke risicoprofiel afstemmen. Zo krijg je passende detectiedekking tegen dreigingsactoren die jou of je activiteiten waarschijnlijk als doelwit kiezen.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Diagram met verschillende dreigingsactoren die IMSI-catchers gebruiken, zoals overheidsdiensten, criminele organisaties en bedrijfsspionnen die mobiele apparaten als doelwit kiezen" >}}

## Werking van Rayhunter in het 5G-tijdperk

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Diagram van een 5G-geschikte telefoon die via een terugschakelaanval naar een gecontroleerd 4G- of 3G-netwerk wordt gedwongen, een techniek die Rayhunter ook in het 5G-tijdperk detecteert" >}}

Bij de overgang naar 5G rijst de vraag hoe effectief **Rayhunter** blijft. Het ondersteunt detectie op 2G-, 3G- en 4G/LTE-netwerken, maar geen oorspronkelijke surveillancemethoden voor 5G. Voor een langetermijnstrategie voor surveillancedetectie is inzicht nodig in de huidige beperkingen en blijvende relevantie van **Rayhunter**.

### Waarom Rayhunter op 5G-netwerken relevant blijft

#### Aanvallen die terugschakelen blijven bestaan
De aanvalsmethode die **Rayhunter** detecteert, namelijk apparaten dwingen verbinding te maken met minder veilige netwerken, blijft relevant bij de uitrol van 5G. **IMSI-catchers blijven aanvallen gebruiken die naar 2G en 3G terugschakelen**, omdat:

- **Lagere ontwikkelkosten**: apparatuur voor oudere protocollen bouwen vergt veel minder investering dan een systeem geschikt maken voor 5G.
- **Meer apparaten ondersteunen**: met 2G/3G-surveillance zijn ook oudere apparaten zonder 5G-ondersteuning kwetsbaar.
- **Bewezen aanvalsmethoden**: surveillancetechnieken voor 2G/3G zijn goed gedocumenteerd en getest.
- **Regelgevingsvoordelen**: voor sommige oudere surveillancetechnologieën gelden mogelijk minder juridische beperkingen dan voor geavanceerde 5G-onderschepping.

#### Achterwaartse netwerkcompatibiliteit
5G-netwerken behouden **achterwaartse compatibiliteit met 4G/LTE** en de meeste mobiele apparaten ondersteunen meerdere generaties tegelijk. Hierdoor blijven er mogelijkheden bestaan voor de aanvallen die **Rayhunter** juist detecteert:

- **Automatisch terugvallen**: apparaten schakelen vanzelf terug naar 4G als de 5G-dekking slecht is. Surveillanceapparatuur kan deze overgang onderscheppen.
- **Kwetsbaarheden bij protocolonderhandeling**: geavanceerde IMSI-catchers kunnen de handdruk tussen netwerkgeneraties manipuleren.
- **Misbruik van dekkingsgaten**: apparatuur op plekken met onvolledige 5G-dekking kan apparaten naar gecontroleerde 4G/LTE-netwerken dwingen.

#### Geleidelijke uitrol van 5G
De **trage uitrol van volledige 5G-dekking** zorgt ervoor dat **Rayhunter** nog jaren relevant blijft:

- **Verschillen tussen stad en platteland**: veel gebieden zijn nog vooral afhankelijk van 4G/LTE, waar de detectie van **Rayhunter** direct toepasbaar blijft.
- **Beperkte binnendekking**: 5G-signalen dringen gebouwen vaak minder goed binnen. Apparaten vallen daardoor terug naar 4G, dat **Rayhunter** effectief kan controleren.
- **Reizen naar het buitenland**: de uitrol van 5G verschilt sterk per land, waardoor surveillance via 4G/LTE voor reizigers een risico blijft.

#### Achterstand in technologie bij dreigingsactoren
De **aanschaf en inzet van surveillanceapparatuur** lopen vaak achter op commerciële netwerktechnologie:

- **Overheidsaankopen**: politie en inlichtingendiensten blijven mogelijk nog jaren na de uitrol van 5G bestaande surveillanceapparatuur voor 4G gebruiken.
- **Kosten-batenafweging**: veel surveillanceoperaties bereiken hun doel met goedkopere onderschepping via 4G/LTE. Daardoor ontbreekt soms de prikkel om naar 5G-systemen over te stappen.
- **Training en expertise**: voor surveillance via 5G is gespecialiseerde kennis nodig, die organisaties mogelijk pas na verloop van tijd opbouwen.

### Beperkingen van Rayhunter in echte 5G-omgevingen

#### Blinde vlekken voor oorspronkelijke 5G-surveillance
*Dit is de belangrijkste beperking van Rayhunter.* **Rayhunter kan geen oorspronkelijke IMSI-catcheroperaties via 5G detecteren** als die geen terugschakelaanval gebruiken:

- **Zelfstandige 5G-netwerken (SA)**: wanneer apparaten verbinding maken met een volledig 5G-netwerk zonder terug te vallen op 4G, kan **Rayhunter** deze communicatie niet controleren.
- **Geavanceerde 5G-surveillanceapparatuur**: geavanceerde dreigingsactoren kunnen met geschikte technologie mogelijk 5G-communicatie onderscheppen zonder de detectieheuristieken van **Rayhunter** te activeren.
- **Misbruik van netwerkslicing**: functies voor netwerkslicing in 5G kunnen mogelijk voor surveillance worden misbruikt op manieren die **Rayhunter** niet detecteert.

#### Verbeterde beveiliging in 5G
5G-netwerken gebruiken **betere beveiligingsmaatregelen** die traditionele surveillancetechnieken mogelijk minder effectief maken:

- **Sterkere versleutelingsprotocollen**: 5G gebruikt robuustere standaarden die moeilijker te kraken zijn dan de voorgaande generaties.
- **Verbeterde authenticatie**: betere apparaatverificatie op 5G-netwerken kan het verzamelen van IMSI's bemoeilijken.
- **Netwerkbeveiligingscontrole**: 5G-infrastructuur heeft betere mogelijkheden om indringing te detecteren en surveillancepogingen te herkennen en tegen te gaan.

#### Veranderingen in apparaatgebruik
Naarmate 5G algemener wordt, **kan het gedrag van mobiele apparaten veranderen** en daarmee de detectiemogelijkheden van **Rayhunter** beïnvloeden:

- **Minder bereidheid om terug te schakelen**: toekomstige software-updates kunnen apparaten beter tegen terugschakelaanvallen beschermen als 5G-dekking verbetert.
- **Voorkeur voor 5G**: apparaten geven mogelijk steeds vaker voorrang aan 5G en reageren wantrouwiger op verzoeken om oudere netwerkprotocollen te gebruiken.
- **Meer aandacht voor beveiliging**: mobiele besturingssystemen kunnen verdachte netwerkactiviteit mogelijk beter herkennen.

### Strategische overwegingen voor de inzet van Rayhunter

#### Aanbevelingen voor inzet op korte termijn
Voor direct en nabij gebruik biedt **Rayhunter** **uitgebreide mogelijkheden voor surveillancedetectie**:

- **In stedelijke gebieden**: zelfs in grote steden met brede 5G-dekking detecteert **Rayhunter** surveillancepogingen op 4G/LTE.
- **Bescherming bij belangrijke evenementen**: tijdens protesten, gevoelige bijeenkomsten of activiteiten met een hoog risico biedt **Rayhunter** belangrijke detectie, ongeacht de beschikbaarheid van 5G.
- **Veilig reizen**: **Rayhunter** blijft zeer effectief bij detectie van surveillance tijdens binnenlandse en buitenlandse reizen.

#### Voorbereiden op de toekomst
Organisaties en personen die hun surveillancedetectie op lange termijn plannen, doen er goed aan het volgende te overwegen:

- **Hybride detectiemethoden**: combineer **Rayhunter** met andere beveiligingshulpmiddelen en controletechnieken voor brede dekking van meerdere dreigingsbronnen.
- **Dreigingsbeoordelingen regelmatig bijwerken**: volg de ontwikkeling van surveillancetechnologie om te bepalen wanneer je de mogelijkheden van **Rayhunter** aanvult of vervangt.
- **Ontwikkeling door de community steunen**: steun voor de opensourceontwikkeling van **Rayhunter** vergroot de kans dat toekomstige releases detectie van 5G toevoegen.

#### Technologische ontwikkelingen volgen
De **Rayhunter**-community en EFF onderzoeken nog steeds **detectie van 5G-surveillance**:

- **Onderzoek naar protocolanalyse**: doorlopend onderzoek naar 5G-protocollen kan nieuwe detectiemogelijkheden voor toekomstige versies van **Rayhunter** opleveren.
- **Onderzoek naar hardwarecompatibiliteit**: onderzoekers beoordelen of huidige apparaten die met **Rayhunter** werken kunnen worden uitgebreid om surveillance via 5G te detecteren.
- **Dreigingslandschap volgen**: inzicht in de ontwikkeling en inzet van surveillanceapparatuur voor 5G helpt om toekomstige ontwikkelprioriteiten voor **Rayhunter** te bepalen.

**Rayhunter** blijft een **belangrijk hulpmiddel voor surveillancedetectie** in de huidige telecommunicatieomgeving. Het zal naar verwachting nog jaren relevant zijn terwijl 5G geleidelijk wordt uitgerold en dreigingsactoren bewezen terugschakelaanvallen blijven gebruiken.

### Opnamen opnieuw analyseren

**Rayhunter** verbetert zijn detectiemogelijkheden voortdurend. Je kunt oude opnamen opnieuw analyseren met bijgewerkte heuristieken. Klik hiervoor in de webinterface op "N warnings" en selecteer "re-analyze".

### Analyse op een computer

Voor gevorderde gebruikers bevat **Rayhunter** de CLI-tool `rayhunter-check` om PCAP- en QMDL-bestanden op computers te analyseren:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Foutopsporingsmodus
```

## Ondersteunde apparaten

**Rayhunter** ondersteunt verschillende mobiele hotspotapparaten met Qualcomm-modems die de interface `/dev/diag` beschikbaar stellen.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Compatibiliteit van Rayhunter-apparaten per regio" caption="Apparaatcompatibiliteit en regionale aanbevelingen voor installaties van Rayhunter" >}}
### Aanbevolen apparaten

Deze apparaten zijn uitgebreid getest en worden veel gebruikt binnen de **Rayhunter**-community:

#### Orbic RC400L (soms verkocht als Kajeet RC400L)
- **Aanbevolen regio**: Amerika's
- **Ondersteunde banden**:
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Wereldwijd en roaming: n257/n78
- **Beschikbaarheid**: compatibele apparaten zijn verkrijgbaar, waaronder **[nieuwe Orbic RC400L met Rayhunter](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** en **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**
- **Prijsindicatie**: professionele modellen zijn verkrijgbaar via STS Collective

#### TP-Link M7350
- **Aanbevolen regio**: Afrika, Europa en het Midden-Oosten (werkt ook in Amerika's, maar is daar meestal duurder)
- **Speciale vereisten**: voor opnamen is een SD-kaart met FAT-indeling nodig
- **Beschikbaarheid**: gecontroleerde compatibele modellen zijn verkrijgbaar als **[TP-Link M7350 met Rayhunter](https://stscollective.com/collections/rayhunter)**

### Werkende apparaten

Er is bevestigd dat **Rayhunter** ook op de volgende apparaten werkt:

- **Wingtech CT2MHS01** (Amerika's), **[verkrijgbaar met Rayhunter](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Amerika's), **[verkrijgbaar met Rayhunter](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (Afrika, Europa en Midden-Oosten), **[verkrijgbaar met Rayhunter](https://stscollective.com)**
- **PinePhone en PinePhone Pro** (wereldwijd), **[verkrijgbaar met Rayhunter](https://stscollective.com)**
- **FY UZ801** (Azië en Europa), **[verkrijgbaar met Rayhunter](https://stscollective.com)**
- **Moxee-hotspot** (Amerika's), **[Moxee K779HSDL met Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Installatienotities per apparaat

#### Orbic/Kajeet RC400L

De Orbic RC400L is het oorspronkelijke apparaat waarvoor **Rayhunter** is ontwikkeld. Het is **[verkrijgbaar met Rayhunter](https://stscollective.com)** via STS Collective.

**Installatiemethoden**:
- **Via het netwerk**: `./installer orbic` (aanbevolen, werkt via WiFi)
- **Via USB**: `./installer orbic-usb` (biedt ADB-toegang en een rootshell)

**Standaardwachtwoorden**:
- **Verizon RC400L**: het beheerderswachtwoord is altijd gelijk aan het WiFi-wachtwoord (te vinden in het apparaatmenu)
- **Kajeet/Smartspot RC400L**: `$m@rt$p0tc0nf!g`
- **Moxee-apparaten**: de wachtwoordnotatie is `12$XXX`, waarbij XXX de laatste 3 cijfers van het WiFi-wachtwoord bevat (controleer het WiFi-wachtwoord onder de batterij)

**Shell-toegang**: gebruik na de installatie `./installer util orbic-shell`.

#### TP-Link M7350/M7310

Deze apparaten werken betrouwbaar met **Rayhunter** en zijn **[verkrijgbaar met Rayhunter](https://stscollective.com)**.

**Installatie**: `./installer tplink` (geen beheerderswachtwoord nodig)
**Opslag**: plaats vóór installatie een SD-kaart met FAT-indeling
**Shell-toegang**: `./installer util tplink-shell`

#### Gespecialiseerde apparaten

**PinePhone en PinePhone Pro**: wereldwijd compatibel en **[verkrijgbaar met Rayhunter](https://stscollective.com)**
**UZ801**: populair in Azië en Europa en **[verkrijgbaar met Rayhunter](https://stscollective.com)**
**Wingtech CT2MHS01**: apparaat voor Amerika's en **[verkrijgbaar met Rayhunter](https://stscollective.com)**

### Nieuwe apparaten toevoegen

**Rayhunter** kan mogelijk werken op elk apparaat met een Qualcomm-modem dat de interface `/dev/diag` beschikbaar stelt. Wil je dat **Rayhunter** jouw apparaat ondersteunt, start dan een discussie in de officiële GitHub-repository.

## Documentatie van de REST API

**Rayhunter** biedt een uitgebreide REST API voor programmatische toegang tot de apparaatstatus, opnamen en configuratie. De API maakt integratie met andere beveiligingstools en geautomatiseerde bewakingssystemen mogelijk.

### Officiële API-documentatie

Raadpleeg voor de volledige API-naslag, met gedetailleerde specificaties van eindpunten, voorbeelden van verzoeken en antwoorden en authenticatiemethoden, de **[officiële documentatie van de Rayhunter REST API](https://efforg.github.io/rayhunter/api-docs/)**.

### Eindpunten van de API

De **Rayhunter**-API is bereikbaar op `http://[device-ip]:8080/api/` en biedt eindpunten voor:

- **Systeemstatus**: controleer de apparaatstatus en werking van **Rayhunter**
- **Opnamen beheren**: start, stop en download opnamen
- **Waarschuwingen ophalen**: bekijk detectiewaarschuwingen en analyseresultaten
- **Configuratie**: werk **Rayhunter**-instellingen programmatisch bij
- **Heuristieken beheren**: schakel specifieke detectiealgoritmen in of uit
- **Apparaatgegevens**: haal apparaatspecificaties en mogelijkheden op
- **Netwerkbewaking**: bekijk actuele gegevens van het mobiele netwerk
- **Gebeurtenissenlogboek**: raadpleeg eerdere detectiegebeurtenissen en waarschuwingen

### Authenticatie

API-toegang gebruikt dezelfde authenticatie als de webinterface. Beveilig je **Rayhunter**-apparaat goed en geef alleen bevoegde gebruikers toegang.

### Integratievoorbeelden

Je kunt de **Rayhunter REST API** integreren met verschillende platforms voor beveiligingsbewaking, SIEM-systemen en eigen automatiseringstools. Raadpleeg de **[officiële API-documentatie](https://efforg.github.io/rayhunter/api-docs/)** voor volledige implementatievoorbeelden en aanbevolen werkwijzen.

## Problemen oplossen

### Veelvoorkomende installatieproblemen

**USB-verbindingsproblemen**: probeer andere USB-kabels of poorten. Defecte USB-verbindingen veroorzaken vaak installatieproblemen. *Dit is de meest voorkomende oorzaak van mislukte installaties.*

**Beveiligingsproblemen in macOS**: als je "No Orbic device found" ziet, wijzig dan tijdelijk de instelling "Allow accessories to connect" in de beveiligingsinstellingen naar "Always".

**Apparaatdetectie**: schakel na installatie de testheuristiek in om te controleren of **Rayhunter** goed werkt.

### Hulp krijgen

Voor hulp bij installatie en probleemoplossing:
- Raadpleeg de officiële documentatie van **Rayhunter**
- Gebruik `./installer --help` en `./installer util --help` voor de opdrachtopties
- Stel vragen in de GitHub-discussies van de community
- Neem voor vragen over apparaatcompatibiliteit contact op met **[STS Collective](https://stscollective.com)**

## Veelgestelde vragen (FAQ)

### Algemene vragen

#### Wat is een IMSI-catcher precies en hoe werkt die?
Een IMSI-catcher, ook bekend als StingRay, celsitesimulator of nepzendmast, is surveillanceapparatuur die legitieme zendmasten nabootst om mobiele communicatie te onderscheppen. Apparaten in de buurt worden gedwongen verbinding te maken met deze apparatuur in plaats van met legitieme zendmasten. Zo kunnen operators apparaatidentificaties (IMSI-nummers), locatiegegevens, gespreksmetadata en mogelijk communicatie-inhoud verzamelen. **Rayhunter** detecteert deze apparaten aan de hand van afwijkende gedragspatronen op het mobiele netwerk.

#### Kan Rayhunter alle soorten surveillanceapparatuur detecteren?
**Rayhunter** detecteert specifiek IMSI-catchers en celsitesimulators op 2G-, 3G- en 4G/LTE-netwerken. Het detecteert geen andere vormen van surveillance, zoals WiFi-monitoring, GPS-trackers, fysieke surveillance of oorspronkelijke surveillance via 5G zonder terugschakelaanvallen. **Rayhunter** is één onderdeel van een bredere strategie voor privacybescherming.

#### Is het legaal om Rayhunter te gebruiken?
Het is in de meeste rechtsgebieden legaal om **Rayhunter** te gebruiken als passief bewakingshulpmiddel. Het verstoort mobiele netwerken of andere apparaten niet, maar analyseert alleen de mobiele signalen die je apparaat normaal ontvangt. Lokale wetten verschillen. Controleer daarom de regelgeving in je omgeving. EFF ontwikkelde **Rayhunter** als een legitiem hulpmiddel voor privacybescherming.

### Technische vragen

#### Waarom heeft Rayhunter een simkaart nodig als een actief abonnement niet nodig is?
De simkaart bevat de International Mobile Subscriber Identity (IMSI) die nodig is om je apparaat op mobiele netwerken te authenticeren en deel te nemen aan de protocoluitwisselingen die **Rayhunter** controleert. Zonder simkaart kan het apparaat geen verbinding maken met mobiele netwerken. **Rayhunter** heeft dan geen netwerkactiviteit om op verdachte patronen te analyseren.

#### Hoeveel gegevens verbruikt Rayhunter tijdens normaal gebruik?
**Rayhunter** gebruikt weinig data voor basisbewaking, omdat het vooral informatie over mobiele protocollen analyseert en geen internetverkeer. Het dataverbruik neemt wel toe als je meldingen op afstand via ntfy inschakelt of het apparaat tegelijk als hotspot gebruikt. De bewaking zelf verbruikt vrijwel geen bandbreedte.

#### Kan ik Rayhunter gebruiken terwijl het apparaat als mobiele hotspot werkt?
Ja, **Rayhunter** kan tegelijk draaien met de hotspotfunctie. Daarvoor heb je wel een actief mobiel abonnement nodig. De bewaking van **Rayhunter** werkt onafhankelijk van de hotspot, maar beide functies tegelijk gebruiken kost meer batterijvermogen.

#### Wat is het verschil tussen installatie via WiFi en via USB?
Met de **WiFi-methode** (aanbevolen voor de meeste gebruikers) installeer je **Rayhunter** via de draadloze interface van het apparaat. Deze methode biedt de standaardfuncties. De **USB-methode** biedt gevorderde gebruikers toegang tot Android Debug Bridge (ADB) voor foutopsporing. Deze methode is ingewikkelder en voor standaardinstallaties niet nodig.

### Vragen over apparaten en compatibiliteit

#### Waarom ondersteunt Rayhunter maar bepaalde apparaten?
**Rayhunter** vereist een apparaat met een Qualcomm-modem dat de interface `/dev/diag` beschikbaar stelt. Deze interface biedt toegang tot informatie over mobiele protocollen. De meeste consumentenapparaten stellen deze interface om veiligheidsredenen niet beschikbaar. De ondersteunde apparaten zijn specifiek getest en voldoen aan de vereisten van **Rayhunter**.

#### Kan ik Rayhunter op mijn gewone smartphone installeren?
Nee. **Rayhunter** werkt niet op gewone smartphones. Het vereist gespecialiseerde mobiele hotspots met specifieke Qualcomm-modems die diagnostische interfaces beschikbaar stellen. Ondersteunde modellen zijn onder meer de Orbic RC400L, TP-Link M7350 en verschillende andere mobiele hotspots.

#### Wat gebeurt er als ik Rayhunter op een incompatibel apparaat probeer te installeren?
De installer van **Rayhunter** detecteert het apparaat en weigert doorgaans te installeren op incompatibele hardware. Een installatie forceren op een niet-ondersteund apparaat kan het beschadigen of onbruikbaar maken. Controleer vóór installatie altijd de compatibiliteit.

#### Heb ik verschillende apparaten nodig voor verschillende regio's?
Ja. Mobiele frequentiebanden verschillen per regio. De Orbic RC400L is afgestemd op netwerken in Amerika's, terwijl de TP-Link M7350 goed werkt in Europa, Afrika en het Midden-Oosten. De compatibiliteitsinformatie voor **Rayhunter** bevat regionale aanbevelingen, zodat je een geschikt apparaat voor jouw locatie kiest.

### Vragen over gebruik en configuratie

#### Hoe weet ik of mijn Rayhunter-apparaat goed werkt?
Schakel de testheuristiek in via de configuratie van **Rayhunter**. Het apparaat geeft dan een waarschuwing af telkens wanneer het een zendmast detecteert. Zo controleer je of het systeem werkt. Tijdens normaal gebruik hoort het scherm een groene lijn te tonen. Schakel de testheuristiek na de controle weer uit, want die veroorzaakt veel waarschuwingen.

#### Wat moet ik doen als Rayhunter een waarschuwing geeft?
Noteer eerst je locatie en de omstandigheden wanneer **Rayhunter** verdachte activiteit detecteert. Door netwerkoptimalisatie of apparatuurproblemen kunnen foutpositieven ontstaan. Blijven waarschuwingen op dezelfde plek of tijdens gevoelige activiteiten terugkomen, overweeg dan om naar een andere locatie te gaan en de details in de webinterface te bekijken.

#### Hoe vaak moet ik Rayhunter bijwerken?
**Werk Rayhunter maandelijks bij.** Controleer de releasepagina op nieuwe heuristieken en compatibiliteitsverbeteringen. Deze worden regelmatig toegevoegd. EFF verbetert de mogelijkheden van **Rayhunter** voortdurend om op veranderende surveillancetechnieken te reageren. Bijwerken verloopt hetzelfde als de eerste installatie.

#### Kan Rayhunter meerdere mensen tegelijk beschermen?
**Rayhunter** detecteert IMSI-catchers in de omgeving en kan daardoor mogelijk meerdere mensen binnen bereik beschermen, meestal enkele honderden meters afhankelijk van de signaalsterkte. Iedereen die surveillance serieus wil detecteren, doet er wel goed aan een eigen **Rayhunter**-apparaat te overwegen voor maximale bescherming en controle over de configuratie.

### Vragen over beveiliging en privacy

#### Val ik door Rayhunter meer op bij surveillancediensten?
**Rayhunter** werkt passief en zendt geen signalen uit waarmee surveillanceapparatuur het kan herkennen. Het gebruik van beveiligingstools toont wel privacybewustzijn. De voordelen van detectie wegen doorgaans zwaarder, vooral voor mensen met een hoger risico, zoals journalisten en activisten.

#### Kunnen surveillancediensten zien dat ik Rayhunter gebruik?
**Rayhunter** is een passief bewakingssysteem en verzendt geen identificerende signalen. Op protocolniveau van het mobiele netwerk kunnen operators niet zien dat je **Rayhunter** gebruikt. Fysieke observatie van het apparaat of analyse van netwerkverkeer kan het gebruik van **Rayhunter** aan het licht brengen als meldingen op afstand zijn ingeschakeld.

#### Welke informatie verzamelt Rayhunter over mij?
**Rayhunter** analyseert informatie over mobiele protocollen en slaat detectiewaarschuwingen lokaal op het apparaat op. Het verzamelt geen persoonlijke informatie, inhoud van communicatie of locatiegegevens buiten wat de detectiealgoritmen nodig hebben. Alle gegevens blijven op je apparaat, tenzij je meldingen op afstand inschakelt.

### Gevorderde vragen

#### Kan ik Rayhunter-gegevens op mijn computer analyseren?
Ja. **Rayhunter** bevat de opdrachtregeltool `rayhunter-check` om opgenomen PCAP- en QMDL-bestanden op desktopcomputers te analyseren. Zo kunnen gevorderde gebruikers detectiegebeurtenissen in detail onderzoeken en verdachte activiteit analyseren met alle beschikbare computerbronnen.

#### Hoe presteert Rayhunter in dichtbebouwde stedelijke gebieden?
In dichtbebouwde steden staan veel legitieme zendmasten. Netwerkoptimalisatie en frequente overdrachten tussen zendmasten kunnen het aantal foutpositieven verhogen. De algoritmen van **Rayhunter** onderscheiden normaal netwerkgedrag van surveillanceactiviteit, maar gebruikers in dichtbebouwde gebieden moeten de gevoeligheid mogelijk aanpassen.

#### Werkt Rayhunter tijdens buitenlandse reizen?
De werking van **Rayhunter** tijdens reizen hangt af van de compatibiliteit van je apparaat met lokale frequentiebanden en roamingovereenkomsten. De detectiealgoritmen werken wereldwijd, maar controleer of je apparaat de frequentiebanden in je bestemming ondersteunt. Voor volledige werking is mogelijk internationale roaming nodig.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="Iemand bekijkt Rayhunter-waarschuwingen op een laptop en draagt een mobiele hotspot in een stedelijke omgeving met zendmasten in de buurt" >}}

______

**Rayhunter** is een belangrijke vooruitgang in persoonlijke privacybescherming en surveillancedetectie. Door **Rayhunter** correct op compatibele apparaten te flashen en configureren, kun je IMSI-catchers detecteren en mobiele communicatie tegen onbevoegde surveillance beschermen.

Of je nu journalist, activist, beveiligingsprofessional of privacybewust bent, **Rayhunter** biedt hulpmiddelen om mobiele beveiliging te behouden in een wereld waarin surveillance toeneemt. Bekijk voor gecontroleerde compatibele apparaten de mogelijkheden om **[Rayhunter te kopen](https://stscollective.com)** bij betrouwbare leveranciers van beveiligingsapparatuur.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Koop Rayhunter-apparaten en bespaar 20%
{{< /centerbutton >}}

## Bronnen

- [Officiële GitHub-repository van Rayhunter](https://github.com/EFForg/rayhunter)
- [Nieuwste Rayhunter-release](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, leverancier van Rayhunter-apparatuur](https://stscollective.com)
