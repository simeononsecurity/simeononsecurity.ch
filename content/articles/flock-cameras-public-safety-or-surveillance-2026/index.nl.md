---
title: "Flock-camera's: Instrument voor openbare veiligheid of machine voor bewaking zonder bevel?"
date: 2026-08-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Een onafhankelijke analyse van Flock Safety ALPR-camera's: hoe ze werkelijk functioneren, welke gegevens ze verzamelen buiten kentekenplaten, hoe gegevensdeling een schaduwdatabase op nationaal niveau creëert, en waarom de kwestie van het bevel de echte kernvraag is."
genre: ["Privacy", "Bewaking", "Burgerlijke vrijheden", "Technologie voor rechtshandhaving", "Digitale rechten"]
tags: ["Flock Safety","ALPR","kentekenlezers","bewaking","privacy","bewaking zonder bevel","konvooianalyse","Bluetooth-tracking","TPMS-tracking","gegevensdeling","Ring-camera’s","Vierde Amendement","niets te verbergen","LPR-nauwkeurigheid","onterechte beschuldiging","MFA","technologie voor rechtshandhaving","burgerlijke vrijheden","dataminimalisatie","DeFlock","tegenbewaking","openbare veiligheid","politiesurveillance","privacyrechten","Vierde Amendement","digitale bewaking","massabewaking","kentekenherkenning","cameranetwerken","gegevensbewaring"]
cover: "/img/cover/flock-safety-cameras-public-safety-surveillance.webp"
coverAlt: "Een donker straatkruispunt verlicht door een bewakingscamera op een paal, met kentekengegevens die over passerende auto's worden weergegeven."
coverCaption: ""
canonical: "https://simeononsecurity.com/articles/flock-cameras-public-safety-or-surveillance-2026/"
---

**Het debat over Flock Safety-camera's verdeelt mensen op een manier die bijna niets anders doet in het technologiebeleid. Degenen die een auto hebben laten stelen, zijn er doorgaans blij mee. Degenen die constitutioneel recht bestuderen, hebben er doorgaans een hekel aan. Beiden reageren op iets reëels.**

Dit is een onafhankelijke analyse van wat deze systemen feitelijk doen, wat het bewijs zegt over hun nauwkeurigheid en misbruik, en waarom de belangrijkste vraag niet is of camera's openbare straten mogen fotograferen — maar of de overheid een doorzoekbare, warrantloze database van ieders bewegingen moet opbouwen.

{{< youtube id="fFuE2-xtq2w" >}}

*Dit onderwerp leidde medio 2026 tot significante publieke discussie. De video hierboven behandelt een reeks perspectieven van kijkers en tegenargumenten die het waard zijn naast de hier gepresenteerde analyse te overwegen.*

______

## Waarom Flock-camera's anders zijn dan uw telefoon

De meest gangbare verdediging van Flock Safety-camera's luidt als volgt: uw telefoon volgt u al overal. De politie kan uw GPS-gegevens met een bevel opvragen. Flock-camera's zijn minder nauwkeurig dan dat. Dus waarom zou u zich zorgen maken?

Het argument is oppervlakkig redelijk en fundamenteel onjuist.

**Uw telefoon volgt u. Flock-camera's volgen iedereen.** Wanneer de politie uw celtorenlocatiegegevens of GPS-geschiedenis opvraagt, hebben ze een bevel, een specifiek doelwit en een gegronde reden nodig. Wanneer een agent de Flock-database raadpleegt, hoeft hij geen van deze dingen te hebben. Ze kunnen zoeken op kentekennummer, tijdvenster, locatie of voertuigbeschrijving — zonder bevel, zonder een benoemde verdachte, zonder enige verdenking.

Het resultaat is **massabewaking zonder bevel van een hele bevolking**, niet gerichte bewaking van een specifiek individu. Het Vierde Amendement was specifiek ontworpen om precies dit soort algemene zoekopdrachten te voorkomen.

Mobiele-telefoontracking bouwt ook geen permanente, doorzoekbare registratie op van elk voertuig dat de afgelopen 30 dagen elke kruising in uw stad is gepasseerd. Flock doet dat wel. Die aanhoudende, gestructureerde database is wat het kwalitatief anders maakt dan een agent die een kenteken opschrijft of een bedrijf dat een beveiligingscamera installeert.

**Een foto is geen bewakingssysteem. Een doorzoekbare, van tijdstempels voorziene database van foto's, gekoppeld via voertuigidentiteit over honderden camera's, is dat wel.**

______

## Wat "konvooianalyse" werkelijk betekent

Flock Safety verkoopt een functie genaamd **konvooianalyse** — de mogelijkheid om meerdere voertuigen te volgen die samen als groep reizen. De marketingtaal is saai. De implicaties zijn dat niet.

Konvooianalyse betekent dat Flock kan vaststellen wanneer twee of meer specifieke voertuigen samen bewegen, hun reispatronen in de loop van de tijd kan correleren, en kan signaleren wanneer een historisch geassocieerde groep opnieuw bijeenkomt. In een rechtshandhavingscontext zou dit kunnen betekenen: het volgen van demonstratieorganisatoren die naar dezelfde locaties rijden, het identificeren welke auto's politieke bijeenkomsten bijwonen, of het monitoren van mensen die regelmatig in dezelfde buurt samenkomen.

Geen van deze mensen hoeft iets illegaals te hebben gedaan voordat hun konvooiassociaties worden vastgelegd en opgeslagen.

De functie heeft legitieme toepassingen — het volgen van voertuigen van een vermoedelijke criminele organisatie, bijvoorbeeld. Maar dezelfde functie toegepast op een database zonder beveilvereiste betekent dat die op iedereen kan worden gebruikt. Het is de infrastructuur voor politieke bewaking, ongeacht of dat vandaag de bedoeling is.

______

## Wat Flock-camera's verzamelen buiten kentekenplaten

Het kenteken is het meest zichtbare datapunt, maar niet het enige. Dit is wat het bewijs laat zien over de bredere signaalverzameling door deze cameranetwerken.

### Bluetooth- en WiFi MAC-adresscanning

**Dit is reëel, gedocumenteerd en vaak onderbelicht.**

Veel ALPR-implementaties — niet alleen Flock — bevatten WiFi- en Bluetooth-scanmogelijkheden. Wanneer de WiFi of Bluetooth van uw telefoon is ingeschakeld maar niet verbonden, zendt het **probeaanvragen** uit die het MAC-adres van uw apparaat bevatten. Een camera met een WiFi-radio kan deze adressen passief registreren naast de kentekenlezing.

Dit is enorm belangrijk: uw MAC-adres is gekoppeld aan *u*, niet aan uw auto. Als u in iemand anders' voertuig rijdt, een auto huurt of een geleende auto bestuurt, blijft uw telefoon uw identiteit uitzenden. Konvooianalyse kan nu de apparaat-identiteiten van elke passagier bevatten, niet alleen van de bestuurder.

Zelfs als de implementatie waarover u zich zorgen maakt dit momenteel niet doet, bestaat de hardware- en softwarecapaciteit vaak wel. De vraag welke gegevens *worden verzameld* en welke gegevens *worden bewaard* zijn afzonderlijke kwesties, en naleving controleren is effectief onmogelijk zonder een publieke beveilvereiste.

### TPMS-sensortracering

**Bandenspanningsmonitoringsysteem (TPMS)-sensoren** zenden een unieke identificatie uit op UHF-radiofrequenties. Deze ID's zijn niet versleuteld en worden uitgezonden wanneer de band rolt. Onderzoekers hebben aangetoond dat passieve TPMS-sniffers langs de rijweg voertuigidentiteiten kunnen registreren — en in tegenstelling tot kentekenplaten zijn TPMS-ID's niet zichtbaar voor het publiek en kunnen ze niet worden gewijzigd zonder de sensoren te vervangen.

Een TPMS-ID correleert met een specifieke set banden. Wanneer die banden op een voertuig zijn gemonteerd, is de TPMS-ID functioneel equivalent aan een kenteken dat u niet wist dat u had en dat u niet anders kunt weergeven.

Dit is geen hypothetische toekomstige mogelijkheid. RTL-SDR-ontvangers die TPMS-signalen kunnen registreren, kosten ongeveer $40. De technische drempel voor het inzetten van passieve TPMS-monitoring naast een ALPR-netwerk is zeer laag.

{{< figure src="flock-tpms-bluetooth-surveillance.webp" alt="Diagram van hoe een Flock-camera langs de weg tegelijk kentekenplaten, Bluetooth-MAC-adressen van telefoons en TPMS-sensor-ID’s van banden vastlegt" >}}

______

## Wat de camera vastlegde

**In september 2026 haalde een hackergroep een Flock-camera van een paal, kopieerde de opslag en publiceerde de bestandssysteemkopieën via Distributed Denial of Secrets.** De teruggevonden logboeken geven een volledig beeld van een echte installatie. De aantallen zijn groter dan de openbare marketing suggereert.

*De camera is niet gehackt. Hij is losgeschroefd.*

### Eenentwintig dagen verkeer

De terugvindbare logboeken bestrijken ongeveer **21 dagen** verspreid over meerdere perioden. De camera fotografeerde in die perioden ongeveer **50.200 voertuigen en maakte circa 1,6 miljoen afbeeldingen**.

| Maatstaf | Waarde |
|---------|-------|
| Gefotografeerde voertuigen | **50.200** |
| Gemaakte afbeeldingen | **~1,6 miljoen** |
| Typische dag | ~3.300 voertuigen |
| Drukste dag in de logboeken | **4.454 voertuigen** |
| Afbeeldingen per passerend voertuig | meestal ~28, **soms meer dan 100** |

Oudere logboeken waren op het apparaat overschreven. De camera draaide dus langer dan de bewaarde periode laat zien. **Eén plek langs de weg leverde in minder dan een maand meer dan een miljoen afbeeldingen op.**

### Elk voertuig krijgt tientallen foto's

Zodra beweging in beeld komt, maakt de camera snel achter elkaar foto's. Een doorsnee voertuig leverde ongeveer **28 afbeeldingen** op, en sommige meer dan 100.

De camera gebruikt **verschillende belichtingen** om de kentekenplaat en de bredere scène in aparte beelden vast te leggen. Daarna scant hij de beelden, snijdt bruikbare frames uit en uploadt ze via het mobiele netwerk. Het apparaat leest de kentekenplaat zelf niet. Er draaien ongeveer **20 door Flock gemaakte apps** voor bewegingsdetectie, beeldopname, objectclassificatie, uploads en updates op afstand. **Kentekenherkenning en voertuigidentificatie gebeuren op de servers van Flock, niet langs de weg.**

Dit onderscheid doet ertoe in het debat over bevelen. De camera neemt niet passief alleen een kentekennummer op. Hij levert gegevens aan een extern identificatiesysteem.

### De software detecteert ook mensen

Flock zegt dat de camera's voertuigen detecteren. De teruggevonden code laat meer zien.

**De software op het apparaat bevat uitdrukkelijk een persoonsdetector.** Wanneer die een persoon vindt, registreert hij diens positie in beeld en een betrouwbaarheidsscore. Deze detector staat los van de voertuig-, kenteken- en fietsedetectoren. Het is een bewuste productfunctie, geen bijwerking van een algemeen model.

WIRED testte de bewering door modellen van het apparaat te halen en ze op teruggevonden video en controlebeelden uit te voeren. **De modellen detecteerden zonder moeite mensen, ook op een selfie van een verslaggever.** Een analyse van **27.321 opgeslagen videoclips** vond personen in 11 clips, allemaal motorrijders. Het lage aantal komt door de hoge montage boven een weg, gericht op de rijstroken, niet door een beperking van de detector.

**Ook die clips zijn een belangrijke bevinding.** Het zijn **MP4-video's van één tot twee seconden, 1024 bij 768 pixels, zonder audio**. Ze staan los van de bursts met hoge-resolutiestilstaande beelden. De openbare beschrijvingen van Flock benadrukken foto's van kentekenplaten. Het apparaat neemt ook korte video's op.

*Flock zegt dat de camera's geen gezichtsherkenning uitvoeren. Het onderzoek vond geen bewijs voor gezichtsherkenning buiten functies die standaard in Android zitten. Die functies leken niet ingeschakeld of gebruikt.*

### De kentekendetector ziet overal platen

Hetzelfde onderzoek vond dat de kentekendetector afbeeldingen als kentekenplaten aanmerkt.

**Bumperstickers, dealerhouders en andere afbeeldingen op voertuigen werden uitgesneden alsof het kentekenplaten waren.** In een video van een passerende motorfiets selecteerde de detector een **Amerikaanse vlagpatch op de zadeltas** van de rijder en behandelde die als een kentekenplaat.

Dit is zowel een nauwkeurigheids- als een privacyprobleem. De classificatie is ruim genoeg om afbeeldingen te verzamelen die het systeem niet hoort te verzamelen. Die beelden gaan naar dezelfde servers als echte kentekenlezingen.

### De camera raakte vol

De logboeken tonen een apparaat dat voortdurend opslagruimte tekortkwam.

Bij het opslaan van beelden op volledige resolutie registreerden de logboeken **meer dan 27.000 fouten met de melding "no space left on device"**. Daarnaast waren er tienduizenden gerelateerde fouten, crashes en herstarts.

Twee logregels zeggen veel over het ontwerp:

- Ongeveer elke twee minuten controleerde een dienst of de camera nog draaide en schreef **"Who's a good boy?!"** in het logboek. Er staan meer dan **12.000** van zulke regels in de teruggevonden gegevens.
- Bij een herstart schreef een andere dienst **"A reboot was requested! ¡Adiós, Amigos!"**.

De toon is luchtig. De gevolgen zijn dat niet. Dit bewakingsapparaat mist al acht jaar updates voor het besturingssysteem. Het crasht en raakt vol tijdens het opslaan van de beelden waarvoor het is ontworpen.

______

## De productlijn verzamelt meer dan kentekenplaten

De teruggevonden camera was een Falcon. Het productaanbod is groter en nieuwere producten verzamelen signalen die een kentekenlezer nooit oppikte.

### De geluidssensor herkent nood

**Raven** is een apart gemonteerde geluidsdetector. Hij gebruikt een ESP32 met een Syntiant NDP120-B0 neurale DSP. Eerst onderscheidde hij vier geluidsklassen: schoten, banden, achtergrondgeluid en onbekend.

**Een firmware-update van oktober 2025 voegde een vijfde klasse toe: geluiden van menselijke nood.** De sensor beoordeelt of iemand in de buurt hulp nodig heeft en activeert via FlockOne automatisch de aanwezige Condor- en Falcon-camera's.

*Een apparaat dat als schotdetectie werd verkocht, werd stilletjes een akoestische noodmonitor.*

### De camera's vliegen nu

**Alpha** is de eigen drone van Flock. Hij werd in oktober 2025 onthuld en wordt al ingezet, waaronder in een **proef van de politie van South Bend in maart 2026**. Flock ontwierp hem, hij wordt in de VS geassembleerd en voldoet aan NDAA-eisen.

| Specificatie | Waarde |
|---------------|-------|
| Maximumsnelheid | **60 MPH** |
| Vliegtijd | ~45 minuten |
| Batterijwissel | **90 seconden** bij een dock met twee batterijen |
| Mobiele verbindingen | **4 onafhankelijke modems** voor failover |
| Hoogte voor kentekenlezing | **tot 2.000 voet** |
| Dekking | tot **50 vierkante mijl per dock** |

**Aerodome** is de oudere dronelijn, overgenomen via een **overname van 300 miljoen dollar in oktober 2024**. De lijn gebruikt DJI Matrice M350- en M300 RTK-luchtvaartuigen. Het Hextronics Atlas-nest houdt acht batterijen voor doorlopende inzet. Prosper Police en Scottsdale gebruiken ze nog.

### Het netwerk neemt camera's van anderen op

**Wing** is geen hardware. Het is een softwarebrug die in oktober 2025 werd aangekondigd. De brug voegt Flock-analyse toe aan bestaande IP-camera's van derden, zodat niet-Flock-camera's gegevens aan dezelfde onderzoeksomgeving **Nova** leveren.

**Dit vergroot de schaal van het probleem.** Een stad die Flock-camera's installeert, weet welke apparatuur ze heeft geplaatst. Met Wing verandert een stad haar bestaande cameranetwerk in Flock-sensoren zonder één nieuwe camera te kopen. De beelden komen in één doorzoekbaar systeem terecht.

### De trailer maakt inzet eenvoudig

De **LPR-trailer** monteert een Flock-camera op een All Traffic Solutions ATS-5-chassis met **120 watt zonne-energie**, een **47 ampère-uur accu** en radar met een informatiebord. Hij wordt aan een trekhaak van 2 inch bevestigd en kan door één persoon worden geplaatst.

De trailer meldt ook sabotage en een lage accu. Dat laat zien dat het bedrijf rekening houdt met ingrepen in het veld.


{{< figure src="flock-data-sharing-shadow-national-network.webp" alt="Kaart van stads- en county-netwerken met Flock-camera’s die via overeenkomsten voor gegevensdeling samenkomen in een groter regionaal en bijna landelijk doorzoekbaar bestand" >}}

______

## Het echte probleem: fotografie versus database

Een foto maken van een auto op een openbare weg is legaal. Een politieagent die een kenteken opschrijft is legaal. De beveiligingscamera van een buurman die verkeer opneemt is legaal.

Geen van deze activiteiten is hetzelfde als **het bouwen van een gecentraliseerde, doorzoekbare, voor onbepaalde tijd bewaarde database van alle voertuigbewegingen in een hele stad**.

Het wettelijke recht om openbare ruimten te observeren strekt zich niet automatisch uit tot het recht om die observaties samen te voegen tot een bewakingsinfrastructuur die functioneert als een 30-daagse continue schaduwing van elke persoon die rijdt.

Het Hooggerechtshof heeft dit onderscheid erkend. In *Carpenter v. United States* (2018) oordeelde het Hof dat zelfs als celtoren-gegevens bestaan uit gegevens die al aan een derde partij zijn verstrekt, het samenvoegen van die gegevens over tijd tot een uitgebreide registratie van iemands bewegingen een bevel vereist. Het Hof merkte expliciet op dat alomtegenwoordige tracking de constitutionele berekening verandert.

Flock Safety-camera's doen precies wat *Carpenter* voor waarschuwde — op grote schaal, automatisch, zonder bevelen, voor de hele bevolking.

______

## Gegevensdeling en het schaduw-nationale netwerk

Individuele Flock-cameranetwerken zijn niet geïsoleerd. Steden en gemeenten sluiten **gegevensdelingsovereenkomsten** met naburige rechtsgebieden, wat betekent dat een zoekopdracht in één stad gegevens uit tientallen andere steden kan ophalen. Sommige van deze deelovereenkomsten zijn ruim genoeg dat een enkel agentschap effectief toegang kan krijgen tot een regionale of quasi-nationale database.

**Dit is hoe een lokaal cameranetwerk een de facto nationaal bewakingssysteem wordt zonder dat het Congres er ooit over stemt.**

De gegevensdeling is vrijwillig en juridisch onduidelijk. Er is geen federale wet die het autoriseert. Er zijn geen gestandaardiseerde limieten voor gegevensbewaring. Er zijn geen verplichte auditverplichtingen. En er is geen mechanisme voor een burger om erachter te komen of de bewegingen van zijn voertuig zijn opgevraagd.

**De omvang van deze toegang is inmiddels gedocumenteerd.** In Alpharetta, Georgia, ontdekte WIRED dat gegevens van de Flock-camera’s van de stad bereikbaar waren voor **meer dan 2.000 instanties**, waaronder politiediensten, universiteiten, luchthavens en het Office of Inspector General van de federale General Services Administration. Dat aantal is geen bijzonderheid van de eigen overeenkomsten van Alpharetta. Het laat zien hoe Flock zijn landelijke netwerk standaard verbindt.

DeFlock.org, dat Flock-cameralocaties crowdsourcet, heeft meer dan **124.000 vermoedelijke LPR-implementaties** door de Verenigde Staten in kaart gebracht. De dekking in stedelijke en voorstedelijke gebieden is dicht genoeg dat rijden door de meeste Amerikaanse steden een bijna-continue bewakingsregistratie genereert.

______

## Ring-camera's, Flock en bevelen

Flock Safety en Amazon Ring zijn verschillende producten, maar ze delen een kritieke eigenschap: beide kunnen rechtshandhavingsinstanties toegang tot gegevens geven zonder dat een bevel vereist is.

Ring veroorzaakte aanzienlijke controverse toen het publiek werd dat Amazon duizenden keren beeldmateriaal aan rechtshandhavingsinstanties had gegeven — in veel gevallen zonder medeweten of toestemming van de camera-eigenaar. Amazon veranderde uiteindelijk een deel van zijn beleid na publieke druk, maar het onderliggende juridische kader is niet veranderd.

Flock werkt op een vergelijkbaar model. De camera's worden doorgaans geïnstalleerd door gemeenten of VvE's, maar de data-infrastructuur wordt beheerd door een particulier bedrijf. Wanneer de politie om gegevens vraagt, kunnen ze die krijgen via noodtoegangsprocedures, rechtshandhavingsportalen, of simpelweg doordat het lokale agentschap al toegang heeft.

**De afwezigheid van een beveilvereiste is geen fout in deze systemen. Het is het bedrijfsmodel.**

Verzoeken om openbare documenten (FOIA in de VS, FOI in Canada) kunnen soms onthullen welke agentschappen Flock-systemen hebben geraadpleegd, maar veel agentschappen behandelen Flock-querylogboeken als interne onderzoeksregistraties en weigeren toegang daartoe.

______

## 'Niets te verbergen' ontkracht

Het argument 'niets te verbergen' is de meest voorkomende reactie op zorgen over bewaking, en het weerspiegelt een fundamenteel misverstand over waar privacy voor is.

**Privacy gaat niet over het verbergen van schuld. Het gaat over het bewaren van autonomie.**

Mensen hebben legitieme privacybelangen bij activiteiten die niet crimineel zijn: deelnemen aan politieke bijeenkomsten, artsen bezoeken, naar religieuze diensten gaan, met journalisten spreken, of simpelweg rijden waar ze willen zonder dat er een permanente registratie wordt gemaakt. Het feit dat al deze activiteiten legaal zijn, betekent niet dat de overheid een legitiem belang heeft bij het catalogiseren ervan.

De geschiedenis geeft een direct antwoord op 'niets te verbergen.' Japanse Amerikanen die tijdens de Tweede Wereldoorlog werden geïnterneerd, waren geen criminelen. Activisten die door COINTELPRO werden bewaakt, waren geen criminelen. Mensen op No-Fly-lijsten die er door bureaucratische fouten op bleken te staan, waren geen criminelen. De gegevens die die misbruiken mogelijk maakten, werden verzameld op exact dezelfde redenering — openbare veiligheid, dreigingsbeoordeling, efficiënte rechtshandhaving.

**Bewakingsinfrastructuur die vandaag wordt gebouwd, zal worden gebruikt door wie morgen de macht heeft.** De vraag of de huidige regering betrouwbaar is, is irrelevant. De vraag is of u het prettig zou vinden als de meest vijandige toekomstige regering die u zich kunt voorstellen toegang zou hebben tot een permanente registratie van overal waar u de afgelopen tien jaar heeft gereden.

______

## Wanneer kentekenherkenning het fout heeft

ALPR-systemen zijn niet perfect nauwkeurig, en de gevolgen van een fout zijn ernstig.

Fouten bij kentekenherkenning vallen in verschillende categorieën:

- **Verkeerd gelezen tekens** — letters en cijfers die er vergelijkbaar uitzien bij slechte belichting of hoge snelheid (0/O, 1/I, 8/B, M/N/H)
- **Gedeeltelijke lezingen** — vuile, afgeschermde of beschadigde platen die slechts gedeeltelijk overeenkomen
- **Databasefouten** — platen die als gestolen zijn gemarkeerd maar sindsdien zijn vrijgegeven
- **Regionale plaatbotsingen** — twee staten of landen kunnen dezelfde platencombinatie uitgeven, en een treffer op een Californische plaat kan ten onrechte een voertuig uit een staat met dezelfde alfanumerieke reeks markeren

Reële voorbeelden documenteren al deze gevallen. Mensen hebben met getrokken wapens te maken gehad bij verkeersstops omdat hun voertuig ten onrechte werd gekoppeld aan een gestolen auto. Mensen hebben tolgelden ontvangen voor wegen waarop ze nooit hebben gereden. Iemand die een poederblauw Hyundai reed, ontving een tolrekening voor een Harley-Davidson bereden door iemand met een kenteken dat twee letters verschilde.

**Het foutenpercentage vermenigvuldigd met het leesvolume levert een significant aantal echte mensen op die ten onrechte worden gemarkeerd, gestopt, doorzocht of erger.**

Omdat de meeste van deze zoekopdrachten zonder bevelen plaatsvinden, is er geen rechterlijke controle op de nauwkeurigheid van de onderliggende gegevens voordat actie wordt ondernomen.

______

## Beveiligingsfouten: MFA en gedeelde logins

De beveiligingspraktijken van Flock Safety zijn om meerdere redenen publiekelijk bekritiseerd:

- **Geen verplichte meervoudige authenticatie** voor rechtshandhavingsaccounts in veel implementaties
- **Gedeelde inloggegevens** tussen meerdere agenten bij sommige agentschappen
- **Geen automatische sessietime-outs** in sommige configuraties
- **Geen waarschuwing wanneer accounts worden benaderd vanuit ongebruikelijke locaties of tijden**

Dit zijn geen kleine implementatiedetails. Ze betekenen dat een enkele gecompromitteerde inloggegevens — verkregen via phishing, social engineering of eenvoudige hergebruik van wachtwoorden — een aanvaller toegang kunnen geven om een regionaal Flock-netwerk te doorzoeken dat miljoenen kentekenplaatuitlezingen omvat.

Voor overlevenden van huiselijk geweld, slachtoffers van stalking of journalisten is het bestaan van een gedeelde, minimaal beveiligde database van hun voertuigbewegingen geen abstracte zorg. Het is een direct fysiek veiligheidsrisico.

Het argument dat 'de camera's slechts openbare gegevens zijn', negeert de beveiligingsvereiste voor de *databaselaag* die die gegevens samenvoegt. Zelfs als elke individuele foto legaal is te nemen, vereist de geaggregeerde database sterkere bescherming dan een gedeeld wachtwoord.

______

## Kan het systeem beter worden ontworpen?

**Technische controles alleen zijn niet voldoende, maar ze zijn het overwegen waard.**

Er zijn verschillende voorstellen besproken om ALPR-systemen moeilijker te misbruiken te maken:

**Gegevensminimalisatie by design**: In plaats van volledige kentekenafbeeldingen met tijdstempels en GPS-coördinaten op te slaan, zou het systeem een **cryptografische hash** van het kenteken kunnen opslaan, gecombineerd met een geschatte locatie en tijd. Een rechtshandhavingszoekopdracht zou bevestigen of een specifiek kenteken in een bepaald tijdvenster in een bepaald gebied is gezien, maar kan geen lijst ophalen van alle plaatsen waar dat kenteken is gezien. Dit beperkt het nut voor algemene visserij-expedities terwijl het de mogelijkheid behoudt om gerichte onderzoeksvragen te beantwoorden.

**Tijdsbeperkte bewaring**: Kentekens die niet zijn geassocieerd met een open onderzoek, kunnen na 24-72 uur automatisch worden verwijderd in plaats van 30 dagen of langer te worden bewaard. De meeste legitieme onderzoeksgebruiken vereisen bijna real-time gegevens. Langdurige bewaring creëert een onevenredig risico voor burgerlijke vrijheden.

**Beveilvereisten met rechterlijke toetsing**: De belangrijkste controle is juridisch van aard, niet technisch. Het vereisen van een bevel voor elke zoekopdracht naar de kentekengeschiedenis van een benoemde persoon zou noodgebruik niet voorkomen (uitzonderingen voor dringende omstandigheden bestaan al in de wet), maar zou het routinematige warrantloze datamining voorkomen dat momenteel geen enkele controle heeft.

**Auditlogboeken met publieke transparantie**: Elke zoekopdracht moet worden geregistreerd, die logboeken moeten worden gecontroleerd door toezichthoudende instanties, en geaggregeerde statistieken moeten openbaar worden gerapporteerd.

Deze maatregelen zouden ALPR niet risicovrij maken, maar zouden het potentieel voor routinematig misbruik dramatisch verminderen terwijl het onderzoeknut dat voorstanders waarderen, behouden blijft.

______

## Het debat hoeft niet alles-of-niets te zijn

De discussie over Flock-camera's vervalt vaak in twee extreme standpunten: camera's zijn essentiële misdaadbestrijdingsinstrumenten en elke kritiek helpt criminelen, of camera's zijn een ongrondwettelijke bewakingsstaat en moeten onmiddellijk worden verwijderd.

Beide standpunten zijn onjuist, en de polarisering maakt het moeilijker om het gesprek te voeren dat er werkelijk toe doet.

**De camera's mogen openbare straten fotograferen. De gegevens moeten door de wet worden geregeld.**

De technologie verdwijnt niet. De legitieme toepassingen voor openbare veiligheid zijn reëel. Maar het huidige implementatiemodel — waarbij een particulier bedrijf een quasi-nationale bewakingsdatabase bouwt en beheert die rechtshandhaving zonder bevel kan raadplegen — is constitutioneel verdacht en historisch gevaarlijk.

De weg vooruit is niet om de camera's te vernietigen. Het is het vereisen van bevelen voor individuele zoekopdrachten, het verplichten van korte gegevensbewaringstermijnen, het verbieden van open-ended gegevensdeling zonder zaakspecifieke rechtvaardiging, en het creëren van afdwingbare audit- en toezichtsmechanismen.

Dat is een saai, procedureel antwoord. Het wekt aan geen van beide kanten verontwaardiging op. Maar het is het enige antwoord dat zowel openbare veiligheid als constitutionele vrijheid serieus neemt.

Wie wil weten wanneer die dicht bij zo’n camera is, hoeft niet op beleidsverandering te wachten. Speciale detectiehardware is er al.

{{< stscollective-ad "flockyou" >}}

______

## Gerelateerde artikelen




| Artikel | Wat u leert |
|---------|------------------|
| **[Flock Safety Camera-bewaking: Prevalentie, privacyzorgen en beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Volledige diepgaande analyse van het Flock-netwerk, gedocumenteerde misbruikgevallen en praktische beschermingsstappen |
| **[Flock Finder: Breng elke vermoedelijke Flock-camera bij u in de buurt in kaart](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Hoe u de open-source tool gebruikt om 40.000+ vermoedelijke camera's te visualiseren met WiGLE-gegevens |
| **[Flock-You Detectiehardwaregids](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Bouw of koop een ESP32-gebaseerd apparaat om Flock-camera's in real time te detecteren |
| **[Hoe Rayhunter te flashen op IMSI Catcher-detectieapparaten](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detecteer stingrays en IMSI-catchers — het mobiele equivalent van ALPR-tracking |
| **[Rayhunter Apparaatvergelijking 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Kies de juiste hardware voor een volledig contra-bewakingstoolkit |

______

## Referenties

1. [Carpenter v. United States, 585 U.S. 296 (2018)](https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf)
2. [ACLU: Automatische kentekenlezers](https://www.aclu.org/news/by-issue/automatic-license-plate-readers)
3. [Electronic Frontier Foundation: Wat is ALPR?](https://www.eff.org/pages/what-alpr)
4. [DeFlock](https://deflock.org/)
5. [Interactieve kaart van DeFlock](https://maps.deflock.org/)
6. [Officiële website van Flock Safety](https://www.flocksafety.com/)
7. [Beveiligings- en privacyproblemen in draadloze netwerken in auto’s: casestudy van een TPMS](https://www.winlab.rutgers.edu/~gruteser/papers/xu_tpms10.pdf)
8. [FBI Vault: COINTELPRO](https://vault.fbi.gov/cointel-pro)
9. [MuckRock: Flock Safety](https://www.muckrock.com/tags/flock-safety/)
10. [Flock Finder op GitHub](https://github.com/simeononsecurity/flock-finder)
11. [WIRED en 404 Media: hackers drongen een Flock-camera binnen](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
12. [Micah Lee: Flock-camera’s zitten vol kwetsbaarheden en hardgecodeerde inloggegevens](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
13. [Distributed Denial of Secrets: bestandssysteemkopieën van een Flock-ALPR-camera](https://ddosecrets.org/article/flock-alpr-camera)
14. [Hackaday: deze week in beveiliging, Flock-camera’s zijn oud](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
15. [WiFi Mothership: referentie voor detectie van Flock Safety-ALPR-apparaten](https://wifimothership.com/flock)
16. [Interactieve kaart van Flock Finder](https://simeononsecurity.github.io/flock-finder/)
