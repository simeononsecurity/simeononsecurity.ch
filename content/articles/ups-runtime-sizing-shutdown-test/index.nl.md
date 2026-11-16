---
title: "Een homelab-UPS dimensioneren en automatische uitschakeling testen"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Meet het stroomverbruik van je homelab, vergelijk de watt- en VA-limieten van een UPS, controleer de gebruiksduur bij jouw belasting en test een nette uitschakeling voordat je op de batterij vertrouwt."
genre: ["Thuislab", "Stroombeveiliging", "Systeembeheer"]
tags: ["UPS voor thuislab", "UPS dimensioneren", "UPS-gebruiksduur", "automatische uitschakeling", "Network UPS Tools", "UPS-watt", "UPS-vermogen in VA", "arbeidsfactor", "noodstroom", "serveruitschakeling", "NAS-uitschakeling", "stroomstoring", "UPS-proef", "gebruiksduurcurve", "vermogensmeter", "UPS-bewaking", "batterij vervangen", "overspanningsbeveiliging", "netjes uitschakelen", "stroomvoorziening thuislab"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Een homelab-UPS voedt een server, NAS, router en switch boven een tijdlijn van stroomuitval tot uitschakeling."
coverCaption: "Meet de belasting, controleer de gebruiksduur en test de uitschakeling voordat de stroom uitvalt."
---

Een **UPS** (noodstroomvoorziening) geeft je homelab tijdens een stroomstoring tijd om werk op te slaan en systemen uit te schakelen. Alleen het label vertelt niet hoelang je servers blijven werken. Je hebt het stroomverbruik van de apparatuur nodig, de watt- en VA-limieten van de UPS, een gebruiksduurschatting bij die belasting en een geteste uitschakelroute.

## Belangrijkste punten

- **Meet de belasting:** Noteer het normale en hoge wattverbruik van elk apparaat dat op batterij moet blijven werken.
- **Controleer beide waarden:** De UPS moet voldoen aan de watt- en VA-eisen van de aangesloten apparatuur.
- **Lees de gebruiksduurcurve:** De gebruiksduur hangt af van de belasting en de batterijconditie. Gebruik een schatting voor het specifieke model.
- **Test de uitschakeling:** Controleer of het UPS-signaal elke host bereikt en of hosts stoppen voordat de batterij leeg is.

## Voordat je begint

Je hebt een vermogensmeter nodig die geschikt is voor jouw netspanning, een lijst met apparaten en voedingsadapters, en toegang tot de specificaties en gebruiksduurcurve van elk overwogen UPS-model. Voor een automatische uitschakeltest heb je ook een ondersteunde USB- of netwerkbeheerverbinding en software voor elke host nodig. Plan tijd voor een meting bij normale belasting, een observatie bij hoge belasting en een geplande onderhoudstest. Dit is een homelab-taak voor gevorderden, omdat een volledige uitschakeltest diensten onderbreekt.

De [gids voor overspanningsbeveiliging](/articles/protecting-your-tech_-the-best-surge-protectors/) behandelt bescherming tegen spanningspieken. Het [overzicht van UPS-modellen](/articles/best-ups-models-for-uninterrupted-connectivity/) noemt producten. Deze gids behandelt dimensionering en controle van jouw eigen belasting. Zowel Eatons [gids voor UPS-dimensionering](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html) als Schneiders [koopgids voor UPS-systemen](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) maakt onderscheid tussen uitgangsvermogen en batterijduur.

> **Waarschuwing:** Gebruik alleen de uitgangen en belastingen die de UPS-fabrikant toestaat. Houd de test binnen de nominale capaciteit van de UPS. Een echte uitschakeltest stopt het aangesloten lab.

## Meet wat ingeschakeld blijft

Beslis welke apparaten tot aan de uitschakeling moeten blijven werken. Neem de hypervisor, opslag, netwerkswitch en router mee als een host netwerktoegang nodig heeft om een uitschakelsignaal te ontvangen. Sluit beeldschermen, printers en andere optionele apparaten niet aan op batterij-uitgangen, tenzij je plan ze nodig heeft.

Meet de beoogde groep apparaten op batterijvoeding bij het stopcontact. Noteer het **normale wattverbruik** en het hoogste wattverbruik dat je ziet tijdens representatief werk, zoals het starten van hosts of virtuele machines. Een label op een voeding vermeldt de capaciteit, niet het gemeten verbruik van het systeem. Controleer toch de labels van apparaten op ingangsstroom- en inschakelstroomlimieten. Noteer de meetomstandigheden in je werkblad.

| Apparaat | Normaal wattverbruik | Waargenomen piekverbruik in watt | Batterij-uitgang? |
|---|---:|---:|---|
| **Router en switch** | 30 | 35 | Ja |
| **NAS** | 60 | 90 | Ja |
| **Kleine server** | 90 | 135 | Ja |
| **Illustratief totaal** | **180** | **260** | Drie apparaten |

De waarden hierboven zijn **illustratief** en geen metingen van een specifiek lab. Je belasting verandert door schijven, GPU's, energie-instellingen en aangesloten apparatuur. Meet opnieuw na grote hardwarewijzigingen.

## Vergelijk watt en VA

**Watt** beschrijven het werkelijke vermogen dat de apparatuur gebruikt. **Voltampère (VA)** beschrijven het schijnbare vermogen. De verhouding hangt af van de **arbeidsfactor**: watt gedeeld door de arbeidsfactor is gelijk aan VA. Eaton legt deze berekening uit in de [dimensioneringsgids](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). Behandel een label van 1000 VA niet als 1000 watt. Controleer het aparte wattvermogen van de UPS.

Bij het illustratieve piekverbruik van 260 W geeft een capaciteitsmarge van 25% **325 W**. Schneider Electric adviseert een uitgangsvermogen dat ongeveer [20% tot 25% hoger ligt dan de belasting](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Kies een UPS waarvan het continue wattvermogen hoger ligt dan de geplande piekbelasting plus marge. Als je de gecombineerde arbeidsfactor kent, deel je het piekvermogen in watt door die factor om piek-VA te schatten. Pas daarna ook je gekozen marge toe op VA. Gebruik anders een geschikte meter of de selectietool van de fabrikant om de VA-eis en benodigde ruimte te bepalen. Verzin geen arbeidsfactor als je die niet hebt gemeten.

Een capaciteitsmarge bepaalt de gebruiksduur niet. Een UPS met een hoge wattlimiet maar een kleine batterij kan de belasting slechts kort ondersteunen. Controleer de uitgangen, het stekkertype, de ingangsspanning, de communicatie-interface en de mogelijkheid om de batterij te vervangen voordat je een model kiest.

## Stel een doel voor de gebruiksduur vast

Noteer hoelang het lab nodig heeft om veilig te stoppen. Neem de tijd mee voor het ontvangen van een uitschakelwaarschuwing door hosts, het stoppen van virtuele machines, het wegschrijven van opslag en het uitschakelen van de UPS-uitgang. Reserveer extra tijd voor een trage uitschakeling en een oudere batterij. Een lab dat korte storingen moet overbruggen, heeft een ander doel nodig dan een lab dat alleen netjes moet afsluiten.

Neem als **illustratief** voorbeeld een geteste uitschakeling van 6 minuten en 5 minuten reserve. De vereiste gebruiksduur bij de verwachte belasting is dan minstens 11 minuten. Dit is een planningsvoorbeeld, geen universele grenswaarde. Vergelijk het doel met de gebruiksduurcurve of selectietool van het gekozen model bij jouw **gemeten normale en hoge belasting**. Controleer de uitkomst opnieuw naarmate de batterij ouder wordt. Schneiders [UPS-selectietool](https://www.se.com/us/en/work/products/tools/ups-selector/) baseert de gebruiksduur op de ingevoerde belasting en modelspecificaties. Eaton verwijst ook naar modelspecifieke gebruiksduurgegevens in zijn [gids voor desktop-UPS-systemen](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Kopieer dit **werkblad** voor je lab. Vul de apparaatregels in op basis van je metingen met de vermogensmeter. Tel normaal en hoog wattverbruik op, voeg je gekozen marge toe aan het hoge totaal en pas dezelfde marge toe op gemeten of berekende piek-VA. Vergelijk beide uitkomsten met een geschikte UPS. Noteer bij gebruik van een selectietool de VA-uitkomst en de reserve. Gebruik de curve van het model om de gebruiksduur te schatten. Vul de tijd- en herstelregels tijdens de test in.

| Veld | Jouw resultaat |
|---|---|
| **Apparaten en batterij-uitgangen** | Apparaatnamen en de toegewezen uitgang |
| **Normaal wattverbruik per apparaat en totaal** | Gemeten waarden en som |
| **Hoog wattverbruik per apparaat en totaal** | Hoogste waargenomen waarden en som |
| **Gemeten of opgegeven arbeidsfactor** | Waarde en bron, of „onbekend” |
| **Gemeten of berekende piek-VA** | Piekvermogen in watt gedeeld door de gecombineerde arbeidsfactor, indien bekend |
| **Capaciteitsmarge** | Gekozen percentage, watt en VA na toepassing van de marge |
| **Specificaties van de beoogde UPS** | Model, uitgangsvermogen in watt en VA, en limieten per uitgang |
| **Gebruiksduurdoel en curve-uitkomst** | Benodigde minuten en modelschatting bij jouw belasting |
| **Waarschuwings- en uitschakeltijden** | Tijdstip van de batterijwaarschuwing en het stoppen van de laatste host |
| **Herstelresultaat** | Hoststart, opslag, toepassingen en bewaking |

Als de arbeidsfactor onbekend is, gebruik je de selectietool van de fabrikant of meet je het schijnbare vermogen met een geschikte meter. Rapporteer geen berekende VA-waarde die op een geschatte factor berust. Het werkblad is pas compleet als het model aan beide uitgangslimieten voldoet en de geschatte gebruiksduur langer is dan je uitschakeldoel.

> **Verwacht resultaat:** Je werkblad vermeldt de aangesloten apparaten, gemeten belastingen, watt- en VA-limieten van de UPS, het doel voor de gebruiksduur en de modelspecifieke schatting.

## Bereid automatische uitschakeling voor

Een UPS houdt apparatuur tijdelijk ingeschakeld. De host heeft nog steeds een **uitschakelsignaal** nodig. Controleer of je UPS USB, een netwerkbeheerkaart of een andere ondersteunde interface biedt. Controleer of elke host die moet stoppen een compatibele bewakingsroute heeft. Eaton vermeldt dat veel modellen USB- of netwerkcommunicatie ondersteunen voor een [nette uitschakeling van een NAS of server](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

In een Linux-lab met **Network UPS Tools (NUT)** leest de UPS-driver het apparaat uit, deelt `upsd` de status en start `upsmon` de hostuitschakeling wanneer de voeding kritiek wordt. Een host die rechtstreeks met een USB- of seriële UPS is verbonden, voert normaal gesproken de driver, `upsd` en `upsmon` uit in de modus **Primair**. Andere hosts gebruiken `upsmon` in de modus **Secundair** tegen die server. Een netwerk-UPS heeft een compatibele driver en een modelspecifieke primaire configuratie nodig. De [NUT-topologiegids](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) beschrijft deze rollen. Configureer router en switch zo dat bewakingshosts verbonden blijven op batterijvoeding. Beperk het uitschakelcommando en de bijbehorende rechten tot beheerders.

Controleer vóór een uitschakeltest of de driver actuele statusgegevens rapporteert. Vervang `myupsname` door de UPS-naam in je NUT-configuratie:

```bash
upsc myupsname@localhost ups.status
```

NUTs [configuratiegids](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) verwacht `OL` bij normale netvoeding en beschrijft `OB` voor batterijvoeding. Voer de statuscontrole uit op elke host die de UPS bewaakt en gebruik voor externe clients de juiste servernaam. Verouderde of ontbrekende gegevens betekenen dat je de signaalroute moet herstellen voordat je een uitschakeltest uitvoert.

Noteer de **uitschakelvolgorde**. Stop bijvoorbeeld eerst toepassings-VM's, daarna opslagclients en vervolgens de hypervisor en NAS. Test of elke service en elk bestandssysteem na terugkeer van de stroom normaal herstelt. Een host die wel stopt maar waarna toepassingen niet goed herstellen, is geen geslaagde test.

## Controleer zonder te gokken

Begin met een **proefrun** op de host met de geconfigureerde UPS-driver. NUT documenteert `upsdrvctl -t shutdown` als voorbeeld van de driveruitschakelreeks. Dit commando start de drivers niet en schakelt de stroom niet uit:

```bash
upsdrvctl -t shutdown
```

Deze **driver-proefrun** bewijst niet dat een stroomstoringsmelding elke host bereikt. Controleer elke bewakingsservice en de bijbehorende logboeken. Tijdens een onderhoudsvenster beschrijft NUTs [handleiding voor uitschakeltests](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) een geforceerde uitschakeltest met `upsmon -c fsd` op de primaire NUT-host. Deze **FSD-test** start een echte uitschakelreeks. De FSD-vlag blijft actief totdat `upsd` opnieuw start. Controleer na het opstarten van de systemen of `upsd` opnieuw is gestart en de status geen FSD meer toont voordat je weer op bewaking vertrouwt. Lees de actuele [handleiding voor upsmon](https://networkupstools.org/docs/man/upsmon.html), bereid herstel voor en voer de test pas uit nadat je werk hebt opgeslagen en labgebruikers hebt geïnformeerd.

Volg voor een gecontroleerde **batterijgebeurtenistest** eerst de testprocedure van de fabrikant met niet-kritieke apparatuur. Zo'n test met lage belasting controleert de signaaloverdracht, maar bewijst niet de gebruiksduur voor je lab. Test later tijdens een onderhoudsvenster met een representatieve geplande belasting op batterijvoeding. Iemand moet de UPS bewaken en de netvoeding kunnen herstellen als de reserve te klein wordt. Noteer de belasting die de UPS toont, het moment waarop die batterijvoeding meldt, het moment waarop elke host begint met uitschakelen en het tijdstip waarop de laatste host stopt. Controleer dat de batterij niet leeg raakt voordat de hosts zijn gestopt. Controleer na terugkeer van de netvoeding het opstarten van hosts, de gezondheid van toepassingen, de opslagintegriteit en de bewakingsstatus. NUT beschrijft een geslaagde reeks als een stop van het besturingssysteem vóór het einde van de batterijduur, gevolgd door herstel wanneer de stroom terugkeert.

| Controle | Noteer |
|---|---|
| **Signaalroute** | UPS-gebeurtenis zichtbaar voor elke bewakingshost |
| **Uitschakeltiming** | Laatste host gestopt voordat de batterij leeg is |
| **Herstel** | Hosts, opslag en toepassingen starten goed op |
| **Capaciteit** | UPS-belasting blijft binnen de watt- en VA-limieten |

## Problemen oplossen

- **Overbelastingsalarm van de UPS:** Verwijder optionele apparatuur. Vergelijk de gemeten hoge belasting met beide UPS-limieten en de uitgangslimieten van het model.
- **Gebruiksduur korter dan verwacht:** Controleer de huidige belasting, batterijleeftijd, modelspecifieke gebruiksduurgegevens en recente batterijtestresultaten. Extrapoleer niet lineair op basis van alleen VA.
- **Een host blijft actief:** Controleer de bewakingsservice, netwerkroute, uitschakelrechten en logboeken.
- **Hosts stoppen maar starten niet opnieuw:** Controleer het gedrag van de UPS-uitgang bij herstel, de firmware-instelling voor terugkerende netvoeding en NUTs gedocumenteerde [aandachtspunten voor stroomracecondities](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **De proefrun slaagt, maar de stroomtest niet:** De driverproef controleert een kleiner deel van de route. Bekijk de gebeurtenisoverdracht en de werkelijke uitschakelvolgorde van hosts.

## Volgende stappen

Bewaar het werkblad bij je homelab-inventaris. Meet de belasting opnieuw na hardware-uitbreidingen en herhaal de uitschakeltest na wijzigingen aan de UPS, bewakingssoftware, opstartbeleid van hosts of opslagstack. Controleer je back-up- en herstelplan afzonderlijk. Batterijvoeding beschermt het uitschakelvenster; een [geteste homelab-back-up](/articles/what-is-a-homelab-and-should-you-have-one/) beschermt je gegevens bij andere storingen.
