---
title: "De meest voorkomende soorten cyberaanvallen en hoe verdedigers ze herkennen"
date: 2026-09-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Leer de meest voorkomende soorten cyberaanvallen herkennen, ontdek welk bewijs ze achterlaten in logs en telemetrie en oefen detectie in een thuislab voor beveiliging."
genre: ["Cyberbeveiliging", "Dreigingsdetectie", "Blue team", "Beveiligingsoperaties", "Loopbaanontwikkeling"]
tags: ["soorten cyberaanvallen", "malware", "ransomware", "phishing", "spearphishing", "social engineering", "spoofing", "identiteitsaanvallen", "credential stuffing", "password spraying", "SQL-injectie", "cross-site scripting", "supplychainaanval", "insiderdreiging", "DNS-tunneling", "IoT-aanvallen", "AI-aanvallen", "denial of service", "detectie-engineering", "SOC-analist", "blue team", "thuislab", "loganalyse", "incidentrespons", "MITRE ATT&CK", "carrière in cyberbeveiliging", "threathunting", "security operations center", "telemetrie", "waarschuwingen beoordelen"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "Digitale illustratie met kleurrijke abstracte pictogrammen voor verschillende soorten cyberaanvallen, zoals ransomware, phishing en denial of service, tegen een donkere achtergrond."
coverCaption: ""
---

Een **aanvalstype** is een categorie van technieken, geen afzonderlijk hulpmiddel. Ransomware, phishing en credential stuffing benoemen elk een methode die een aanvaller met kleine variaties op veel doelen toepast. Als je de categorieën leert kennen, krijg je een mentaal overzicht van de waarschuwingen die je in een beveiligingsteam tegenkomt.

*Afzonderlijke malwarefamilies verschijnen en verdwijnen binnen enkele maanden. De aanvalscategorieën hieronder blijven al jaren stabiel. Elk type laat herkenbare sporen achter in endpoint-, identiteits-, netwerk- of e-mailtelemetrie.*

<!--more-->

## Belangrijkste punten

- **Leer het patroon, niet de payload.** Aanvalscategorieën veranderen veel langzamer dan afzonderlijke hulpmiddelen.
- **Elke categorie laat sporen achter.** Detectie begint met weten welke telemetrie de activiteit vastlegt.
- **Reproduceer een aanval om deze te begrijpen.** Een thuislab maakt een abstracte categorie tot een waarneming met vastgelegde gegevens.
- **Documenteer je bevindingen.** Een korte onderzoeksnotitie toont je werk en legt het bewijs vast.

## De aanvalstypen in het kort

De tabel toont categorieën die beveiligingsteams vaak tegenkomen. De volgende secties beschrijven iedere categorie, veelvoorkomende varianten en de gegevens die een verdediger controleert.

| Aanvalstype | Wat het doet |
|---|---|
| **Malware** | Voert schadelijke software uit, zoals ransomware, spyware en trojans |
| **Dienstweigering** | Overbelast een dienst met verkeer zodat legitieme gebruikers geen toegang meer hebben |
| **Phishing** | Verleidt iemand om inloggegevens te delen of een schadelijk bestand uit te voeren |
| **Spoofing** | Doet zich voor als een vertrouwd systeem, een afzender of een adres |
| **Identiteitsaanvallen** | Misbruikt gestolen of vervalste inloggegevens om als geldige gebruiker op te treden |
| **Code-injectie** | Voegt schadelijke code in een toepassing in om het gedrag te veranderen |
| **Supplychainaanvallen** | Compromitteert een vertrouwde leverancier, bibliotheek of updatekanaal |
| **Social engineering** | Manipuleert iemand om een onveilige handeling uit te voeren |
| **Insiderdreiging** | Misbruikt toegang van een huidige of voormalige medewerker |
| **DNS-tunneling** | Verbergt gegevens in DNS-verzoeken om controles te omzeilen |
| **IoT-aanvallen** | Richt zich op verbonden apparaten om verder te komen, te spioneren of een botnet te vormen |
| **AI-aanvallen** | Gebruikt machine learning om inhoud te maken, mensen na te bootsen of filters te omzeilen |

**Afbakening:** deze categorieën overlappen. Een phishingbericht levert vaak malware af, en gestolen inloggegevens gaan vaak vooraf aan een identiteitsaanval. Zie de lijst als verschillende invalshoeken, niet als vaste vakjes.

______

## Malware

**Malware** is software die is gemaakt om een systeem te beschadigen, te besturen of er geld aan te verdienen. De term omvat ransomware, fileless malware, spyware, adware, trojans, wormen, rootkits, keyloggers en botnets.

| Subtype | Gedrag |
|---|---|
| **Ransomware** | Versleutelt bestanden en eist betaling voor de ontsleutelingssleutel |
| **Fileless malware** | Gebruikt ingebouwde systeemhulpmiddelen en schrijft weinig naar schijf |
| **Spyware** | Verzamelt activiteit zonder dat de gebruiker dit weet |
| **Trojan** | Doet zich voor als legitieme software om code te kunnen uitvoeren |
| **Worm** | Verspreidt zichzelf naar andere hosts zonder tussenkomst van de gebruiker |
| **Rootkit** | Verbergt zich in het besturingssysteem om blijvende controle te houden |

**Waar je bewijs vindt:** endpointdetectie- en responsmiddelen, of **EDR**, registreren procesbomen, opdrachtregels, bestandsschrijfacties en registerwijzigingen. Ook een fileless aanval produceert proces- en scriptblokkeringstelemetrie, omdat het besturingssysteem de misbruikte hulpmiddelen nog steeds start.

______

## Denial of service

Een **denial-of-serviceaanval (DoS)** overspoelt een doel met verzoeken totdat legitieme gebruikers geen toegang meer hebben. Een **distributed denial-of-serviceaanval (DDoS)** doet hetzelfde vanaf veel systemen tegelijk. Daardoor is het verkeer veel moeilijker op basis van bronadres te filteren.

| Kenmerk | DoS | DDoS |
|---|---|---|
| **Herkomst** | Eén systeem | Veel systemen |
| **Moeilijkheid van blokkeren** | Gemiddeld | Hoog, omdat bronnen uit veel netwerken komen |
| **Typisch effect** | Beschikbaarheid verloren | Beschikbaarheid op grotere schaal verloren |

**Waar je bewijs vindt:** verkeersvolume ten opzichte van de normale basislijn, verbindingen per bron, pieken in verzoeken en veranderingen in foutpercentages. Beschikbaarheidsbewaking waarschuwt vaak voordat het beveiligingsteam het incident ziet.

______

## Phishing

**Phishing** gebruikt e-mail, sms, telefoongesprekken of sociale media om iemand ertoe te bewegen inloggegevens te delen of een schadelijke bijlage uit te voeren. De varianten verschillen in doelwit en kanaal.

| Variant | Doelwit en kanaal |
|---|---|
| **Spearphishing** | Een specifieke persoon of groep, meestal via e-mail |
| **Whaling** | Leidinggevenden, vaak met als doel geld of gegevens te verplaatsen |
| **Smishing** | Frauduleuze sms-berichten |
| **Vishing** | Frauduleuze telefoongesprekken of spraakberichten |

**Waar je bewijs vindt:** logs van de e-mailgateway, resultaten van URL-analyse, onderzoek van bijlagen en meldingen van gebruikers. Een melding van een oplettende medewerker is een van de waardevolste signalen op deze lijst.

______

## Spoofing

**Spoofing** verbergt een aanvaller achter een vertrouwde identiteit, zodat het doelwit een verbinding, bericht of adres accepteert. De vermomming koopt tijd en omzeilt controles die op vertrouwen zijn gebaseerd.

| Type | Wat wordt vervalst |
|---|---|
| **Domeinspoofing** | Een nagemaakte website of e-maildomein dat een echt merk nabootst |
| **E-mailspoofing** | Het afzenderadres van een bericht |
| **ARP-spoofing** | Een lokaal netwerkadres om verkeer tussen twee hosts te onderscheppen |

**Waar je bewijs vindt:** SPF-, DKIM- en DMARC-resultaten in e-mailheaders, de registratiedatum van een domein, certificaatverschillen en waarschuwingen over dubbele adressen op een lokaal netwerk.

______

## Identiteitsaanvallen

**Identiteitsaanvallen** gebruiken een geldig account in plaats van een softwarefout. De aanvaller heeft werkende inloggegevens, waardoor de activiteit op normaal gebruik lijkt en in de achtergrond verdwijnt. Deze categorie veroorzaakt een groot deel van de waarschuwingen die een **security operations center (SOC)** dagelijks behandelt.

*Als je één categorie in een thuislab oefent, kies dan deze. Er zijn veel signalen, de oefeningen zijn herhaalbaar en de opzet blijft klein.*

| Techniek | Wat er gebeurt |
|---|---|
| **Kerberoasting** | Vraagt een serviceticket aan en kraakt daarna offline het versleutelde wachtwoord |
| **Man-in-the-middle-aanval (MITM)** | Plaatst zich tussen twee partijen om een sessie te lezen of aan te passen |
| **Aanval met hergebruik van de hash (Pass-the-Hash)** | Hergebruikt een gestolen wachtwoordhash om een nieuwe sessie te openen |
| **Golden ticket** | Vervalst een Kerberos-ticket-grantingticket voor brede domeintoegang |
| **Silver ticket** | Vervalst een serviceticket voor één specifieke dienst |
| **Inloggegevens verzamelen** | Verzamelt gebruikersnamen en wachtwoorden op grote schaal |
| **Credential stuffing** | Probeert dezelfde inloggegevens op veel niet-gerelateerde websites |
| **Password spraying** | Probeert één veelgebruikt wachtwoord op veel accounts |
| **Brute force** | Raadt veel wachtwoorden voor één account |
| **Downgrade** | Dwingt een verbinding naar een zwakkere protocolversie |

**Waar je bewijs vindt:** aanmeldingsregistraties, aantallen mislukte authenticaties, tokenafwijkingen, meldingen over onmogelijk reizen en identiteitsrisicodetecties. **Adversary-in-the-middle-phishing (AiTM)** hoort hier ook bij. De aanvaller steelt een actieve sessietoken in plaats van een wachtwoord; hergebruik vanaf onbekende infrastructuur activeert de identiteitsrisicodetectie.

______

## Code-injectie

**Code-injectie** plaatst door de aanvaller beheerde code in een kwetsbare toepassing, zodat de toepassing de code als onderdeel van normaal werk uitvoert. De toepassing voert de schadelijke actie uit, niet de aanvaller rechtstreeks.

| Type | Doelwit |
|---|---|
| **SQL-injectie** | Een databasequery die is opgebouwd uit niet-gevalideerde invoer |
| **Cross-site scripting (XSS)** | Een webpagina die een aanvallerscript in de browser van een bezoeker uitvoert |
| **Malvertising** | Een legitieme advertentieplek met schadelijke code |
| **Datavergiftiging** | Een trainingsset voor een AI- of machine-learningmodel |

**Waar je bewijs vindt:** logs van webtoepassingen, databasequery's, rapporten van het content security policy en verzoekpatronen die afwijken van normaal gebruik.

______

## Supplychainaanvallen

**Een supplychainaanval** richt zich op een vertrouwde derde partij waarvan het product of de dienst veel klanten bereikt. Een **software-supplychainaanval** voegt schadelijke code toe aan een toepassing, bibliotheek of update, zodat alle gebruikers van het product die ontvangen. Een **hardware-supplychainaanval** compromitteert een fysiek onderdeel voordat het wordt verzonden.

*Moderne software is afhankelijk van bibliotheken van derden. Eén gecompromitteerde afhankelijkheid bereikt daardoor veel meer gebruikers dan alleen de oorspronkelijke leverancier.*

**Waar je bewijs vindt:** software-compositieanalyse, buildpipelineregistraties, onverwachte uitgaande verbindingen vanuit een vertrouwde update en integriteitscontroles van gepubliceerde artefacten.

______

## Social engineering

**Social engineering** gebruikt psychologische druk om iemand tot een onveilige handeling te bewegen. De aanvaller speelt in op gezag, urgentie, angst, geld of vertrouwen.

| Techniek | Aanpak |
|---|---|
| **Pretexting** | Verzin een geloofwaardig scenario om vertrouwen te winnen |
| **Business email compromise (BEC)** | Doet zich voor als een vertrouwde collega om een betaling om te leiden of gegevens te delen |
| **Desinformatie** | Verspreidt valse verhalen via sociale media en bots |
| **Quid pro quo** | Biedt een beloning in ruil voor informatie of toegang |
| **Honeytrap** | Bouwt een valse relatie op om geld, gegevens of toegang te verkrijgen |
| **Tailgating** | Loopt achter een medewerker door een beveiligde deur |

**Waar je bewijs vindt:** resultaten van e-mailauthenticatie, ongebruikelijke verzoeken om betalingsgegevens te wijzigen, helpdeskregistraties en fysieke toegangslogs.

______

## Insiderdreigingen

**Een insiderdreiging** is misbruik van toegang door een huidige of voormalige medewerker, opdrachtnemer of partner. Sommige insiders handelen opzettelijk uit geldzucht of wrok. Anderen handelen onzorgvuldig, bijvoorbeeld door inloggegevens in een gedeeld document achter te laten.

*Onzorgvuldige insiders komen vaker voor dan kwaadwillende insiders in incidentrapporten. Voor beide geldt dezelfde detectiecontrole: vergelijk de toegang met de basislijn voor de rol.*

**Waar je bewijs vindt:** de hoeveelheid gegevensoverdracht, activiteit buiten normale werktijden, wijzigingen in bevoegdheden en grote downloads uit gevoelige opslagplaatsen.

______

## DNS-tunneling

**DNS-tunneling** codeert gegevens in DNS-verzoeken en -antwoorden. Bijna elk netwerk staat DNS toe, waardoor deze techniek gegevens langs controles kan verplaatsen die webverkeer inspecteren.

*Detectie kijkt naar volume en vorm. Eén host die duizenden verzoeken naar één domein stuurt, wijkt af van de normale basislijn. Ongewoon lange subdomeinen kunnen op een gecodeerde payload wijzen.*

**Waar je bewijs vindt:** DNS-queryregistraties, querylengte en -volume per host, ongebruikelijke recordtypen zoals TXT en zoekopdrachten naar domeinen die pas enkele dagen bestaan.

______

## IoT-aanvallen

**Een IoT-aanval** richt zich op een verbonden apparaat, zoals een camera, printer, thermostaat of sensor. Zwakke standaardwachtwoorden en zeldzame firmware-updates maken zulke apparaten tot een veelvoorkomend startpunt. Na een compromittering kan een apparaat zich bij een botnet aansluiten, gegevens lekken of toegang tot het bredere netwerk bieden.

*De uitrol van 5G voegt op grote schaal verbonden apparaten toe. Elk nieuw apparaat is een extra doelwit met een lange patchcyclus.*

**Waar je bewijs vindt:** de apparateninventaris, patronen van uitgaande verbindingen, afwijkende gegevensoverdracht door een apparaat met een vaste rol en verschillen in firmwareversies binnen een vloot.

______

## AI-aanvallen

**AI-aanvallen** gebruiken machine learning aan de kant van de aanvaller.

| Techniek | Gebruik |
|---|---|
| **Adversarial AI/ML** | Manipuleert trainingsgegevens of invoer om een model te misleiden |
| **Dark AI** | Gebruikt AI en machine learning specifiek om kwetsbaarheden uit te buiten |
| **Deepfake** | Maakt realistisch nep-audio, nepvideo of nepafbeeldingen |
| **Social engineering met AI** | Voert op grote schaal overtuigende chat- of spraakgesprekken |

*Een deepfake-telefoongesprek of een vloeiende phishingchat maakt een oude truc geloofwaardiger. De onderliggende techniek blijft herkenbaar. Daarom blijven detectievaardigheden die op gedrag zijn gebaseerd langer bruikbaar dan vaardigheden die aan één hulpmiddel zijn gekoppeld.*

**Waar je bewijs vindt:** signalen over de herkomst van inhoud, onafhankelijke verificatie van verzoeken om geld of toegang en gedragsafwijkingen rond identiteiten en betalingswijzigingen.

______

## Aanvallen koppelen aan telemetrie

Elke categorie levert gegevens aan een andere bron. De tabel koppelt de categorieën aan telemetrie en vormt een startpunt voor detectiewerk.

| Aanvalstype | Belangrijkste telemetrie |
|---|---|
| **Malware** | EDR-registraties van processen, bestanden en het register |
| **Dienstweigering** | Netwerkstromen en beschikbaarheidsbewaking |
| **Phishing** | E-mailgateway en URL-analyse |
| **Spoofing** | E-mailauthenticatie en netwerkadresregistraties |
| **Identiteitsaanvallen** | Aanmeldings- en identiteitsbeschermingsregistraties |
| **Code-injectie** | Logs van webtoepassingen en databasequery's |
| **Supplychain** | Buildpipeline en afhankelijkhedeninventaris |
| **Social engineering** | E-mail, helpdesk en fysieke toegangsregistraties |
| **Insiderdreiging** | Registraties van gegevenstoegang en overdracht |
| **DNS-tunneling** | DNS-queryregistraties |
| **IoT** | Apparateninventaris en uitgaande netwerkstromen |
| **AI-aanvallen** | Identiteit, betalingen en herkomstgegevens van inhoud |

*Begin detectiewerk met de kolom voor telemetrie. Een bruikbare regel komt voort uit een bekende gegevensbron en een bekend gedrag, niet uit een productnaam.*

**Categorieën overlappen tijdens een incident.** Een phishingbericht kan leiden tot diefstal van inloggegevens, malware-uitvoering en een identiteitsinbraak. Label de techniek voor de eerste toegang en noteer vervolgactiviteiten apart. Zo wordt één incident geen verzameling van vier losse waarschuwingen en krijgt het onderzoek een duidelijkere tijdlijn.

______

## Oefen de detectie in een lab

Een categorie blijft abstract totdat je de activiteit zelf ziet. Met een thuislab kun je de activiteit genereren, telemetrie vastleggen en de waarschuwing vergelijken met de ruwe registratie. De [loopbaanvideo over het bouwen van een security operations center](https://www.youtube.com/watch?v=s3g8o7Np1_g) toont hoe je een volledige omgeving bouwt om ervaring op te doen voordat je wordt aangenomen.

{{< youtube id="s3g8o7Np1_g" >}}

Begin met identiteitsaanvallen. Maak een testgebruiker, schakel aanmeldingsregistratie in en voer een reeks mislukte en geslaagde aanmeldingen uit. Lees daarna de aanmeldingsregistratie en noteer welke velden normaal gebruik onderscheiden van de oefening.

**Een herhaalbare oefening:**

1. **Kies één categorie** uit de telemetrietabel hierboven.
2. **Reproduceer een onschadelijke variant** van de activiteit op je eigen testsysteem of account.
3. **Verzamel de telemetrie** die de categorie oplevert.
4. **Schrijf een detectie-idee** als regel, opgeslagen zoekopdracht of query.
5. **Test de regel** met de oefening en controleer of deze op het bedoelde gedrag afgaat.
6. **Noteer de beperkingen** van de regel, inclusief de activiteit die deze mist.

De [Microsoft SOC Home Lab-gids](/articles/microsoft-soc-home-lab-2026/) beschrijft de omgevingsopbouw in detail: licenties, netwerksegmentatie, logverzameling en tests van identiteitsbeheer. De [gids voor Mad Hat Cyber Range](https://madhat.io/pages/cyber-range-guide) werkt hetzelfde idee uit tot een oefenomgeving met een aanval, detectie en verdediging.

Koppel het waargenomen gedrag aan de passende [MITRE ATT&CK-techniek](https://attack.mitre.org/) voor een consistente terminologie. Gebruik de koppeling als hulpmiddel voor analisten, niet als bewijs van toeschrijving. Bewaar het ruwe gebeurtenisrecord, de query, de regelversie en bekende blinde vlekken bij de oefening.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Lees de Microsoft SOC Home Lab-gids
{{< /centerbutton >}}

______

## Volgende stappen

Begin met één categorie en één oefening. Voeg een tweede categorie toe nadat je de eerste hebt afgerond en gedocumenteerd. Het doel is diepgang in één onderzoek, niet een checklist van hulpmiddelen.

- **[Microsoft SOC Home Lab-gids](/articles/microsoft-soc-home-lab-2026/)** bouwt de omgeving voor deze oefeningen.
- **[Een IT-thuislab bouwen](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** behandelt de infrastructuur onder een beveiligingslab.
- **[Tips voor een IT-cv](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** laat zien hoe je een gedocumenteerd lab als praktijkervaring presenteert.
- **[De vijf belangrijkste cyberaanvalsvectoren en maatregelen](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** beperkt de lijst tot de vaakst voorkomende aanvalsvectoren.

**Bronmateriaal:** de aanvalscategorieën en subtypen zijn gebaseerd op [CrowdStrike's overzicht van veelvoorkomende cyberaanvallen](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/) door Kurt Baker. Product- en referentielinks verwijzen naar Microsoft-documentatie.
