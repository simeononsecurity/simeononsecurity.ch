---
title: "Privacy.com Virtuele Kaarten: Hoe Betalingsprivacy Werkt"
date: 2023-09-03
lastmod: 2026-11-13
toc: true
draft: false
description: Wat er op een betaalkaart wordt opgeslagen, waarom de magneetstrip het zwakste onderdeel is, wat een handelaar ziet wanneer je betaalt met een virtueel nummer, en hoe de kaarttypes en limieten van Privacy.com in de praktijk werken.
genre:
- Betalingsbeveiliging
- Digitale Privacy
- Virtuele Kaarten
- Financiële Privacy
- Fraudepreventie
- Consumentenbeveiliging
tags:
- privacy.com
- virtuele kaarten
- virtuele debetkaarten
- eenmalige kaarten
- handelaar-gebonden kaarten
- categorie-gebonden kaarten
- tokenisatie
- netwerk-token
- pan
- cvv
- kaartskimming
- magneetstrip
- track 1
- track 2
- betalingskaartbeveiliging
- creditcardfraude
- abonnementsbeheer
- uitgavenlimieten
- pci dss
- soc 2
- card not present fraude
- financiële privacy
- betalingsprivacy
- virtueel kaartnummer
- gemaskerde kaart
- kaartcontroles
cover: /img/cover/privacy_virtual_cards.webp
coverAlt: Een digitale illustratie die een afgeschermde virtuele kaart toont die een slot symbool beschermt, wat de beveiliging en privacy van virtuele debetkaarten vertegenwoordigt.
coverCaption: Bescherm, Beheer en Beveilig Je Online Transacties.
ref:
- /magnetic-stripe-decoder
- /articles/personal-security-checklist-prioritized-2026
- /personal-security-course/personal-finance
---

**Een virtuele kaart doet één specifieke ding: het verandert wat de handelaar ontvangt, niet wat jouw bank weet.** Dit is het hele mechanisme en het begrijpen ervan verklaart zowel de bescherming die je krijgt als de bescherming die je niet krijgt.

De meeste artikelen behandelen virtuele kaarten als een algemeen privacyhulpmiddel en slaan de technische details over. Dit artikel behandelt wat er op een kaart wordt opgeslagen, waarom de magneetstrip het zwakke punt is, en hoe de kaarttypes van Privacy.com zich in de praktijk gedragen.

*De praktische winst is beperkt en concreet: een gestolen nummer wordt nutteloos voor een dief, omdat het alleen werkt bij de handelaar waarvoor het is uitgegeven.*

## Het Korte Antwoord

| Vraag | Kort Antwoord |
|---|---|
| **Wat verandert een virtuele kaart?** | Het nummer dat de handelaar opslaat. Jouw echte kaartgegevens bereiken hen nooit |
| **Is de transactie privé?** | Nee. Jouw bank, het netwerk en de uitgever zien het nog steeds |
| **Wat voorkomt dat een datalek jou schaadt?** | Een handelaar-gebonden of eenmalig nummer, dat elders faalt |
| **Wat is het zwakste onderdeel van een fysieke kaart?** | De magneetstrip, die de volledige trackgegevens onversleuteld opslaat |
| **Bouwt het krediet op?** | Nee. Dit zijn geen kredietrekeningen en er vindt geen kredietcontrole plaats |
| **Wie komt in aanmerking voor Privacy.com?** | Amerikaanse burgers of legale inwoners, 18+, met een Amerikaanse bank- of credit union betaalrekening |

## Wat Staat Er Op Een Betaalkaart

**Drie dingen autoriseren een card-not-present transactie: het primaire rekeningnummer, de vervaldatum en de verificatiewaarde.**

| Element | Lengte | Waar Het Vandaan Komt |
|---|---|---|
| **Primair Rekeningnummer (PAN)** | Tot 19 cijfers | De uitgever, met leidende cijfers die het schema en de bank identificeren |
| **Vervaldatum** | Vier cijfers als MM/JJ | De uitgever |
| **CVV of CVC** | Drie of vier cijfers | Afgeleid van de PAN, vervaldatum en een sleutel die alleen de uitgever bezit |
| **Naam kaarthouder** | Tot 26 tekens | Verschijnt alleen op Track 1 van de magneetstrip |

**De PAN is geen willekeurige reeks.** Het eerste cijfer identificeert het schema, de volgende meerdere identificeren de uitgevende bank, en de rest identificeert de rekening. De structuur betekent dat een kaartnummer op plausibiliteit wordt gecontroleerd zonder iemand te hoeven contacteren, en waarom de Luhn-controlecijfer een enkele verwisselde cijfer detecteert.

**De CVV bewijst dat iemand de kaart fysiek vasthield** toen deze werd uitgegeven. Het wordt niet op de magneetstrip opgeslagen, wat precies de reden is waarom een skimmer die de strip kopieert deze nooit verkrijgt.

*Bekijk dit alles zelf met de **[Magneetstripdecoder en -encoder](/magnetic-stripe-decoder/)**, die Track 1 en Track 2 ontleedt, de servicecodecijfers decodeert en het resultaat opnieuw codeert. Het draait volledig in je browser, wat belangrijk is omdat dit de volledige inhoud van een betaalkaart is.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Diagram dat de elementen van een betaalkaart toont, inclusief het primaire rekeningnummer, vervaldatum, CVV en de drie magneetstriptracks met wat elk bevat" >}}

## Waarom De Magneetstrip Het Zwakke Punt Is

**De strip slaat rekeninggegevens in platte tekst op, en elke compatibele lezer kan deze lezen.**

Een magneetstrip bevat tot drie tracks. Track 1 bevat de PAN, de naam van de kaarthouder, de vervaldatum en een driecijferige servicecode, en het is de enige track met alfabetische tekst. Track 2 bevat de PAN, vervaldatum en servicecode in een dichtere numerieke codering, en **Track 2 is wat bijna elk verkooppuntterminal leest.** Track 3 wordt door de grote netwerken vrijwel niet gebruikt en is vaak helemaal niet op de kaart aanwezig.

De servicecode is het waard om te begrijpen, omdat het het toegestane gebruik van de kaart beschrijft. Cijfer één betreft de interchange-regels, cijfer twee de autorisatieafhandeling, en cijfer drie het dienstenbereik. Een kaart gecodeerd als `201` staat internationale interchange toe, heeft geen speciale autorisatie nodig en kent geen dienstbeperkingen.

De geschiedenis verklaart waarom de strip zo lang heeft standgehouden. In 1969 probeerde een IBM-ingenieur genaamd Forrest Parry magnetische tape op een plastic kaart te bevestigen, maar het lukte niet zonder schade. Zijn vrouw stelde voor een strijkijzer te gebruiken, en de hitte bond de tape aan de kaart. Deze improvisatie werd de standaard voor meer dan een halve eeuw.

Twee ontwikkelingen beëindigen dit:

| Mijlpaal | Status |
|---|---|
| **Mastercard kondigde de verwijdering van de strip aan** | Tegen 2033 zullen geen Mastercard credit- of debetkaarten er nog een hebben |
| **Europa** | Strips begonnen te verdwijnen van Mastercard-kaarten in 2024 |
| **Verenigde Staten** | Banken stoppen met uitgeven vanaf 2027 |

*De strip werd vervangen door chip- en contactloze betalingen omdat het kopiëren ervan geen vaardigheid vereist behalve het bezitten van een lezer. Onze **[magneetstriptool](/magnetic-stripe-decoder/)** toont hoe weinig data nodig is om een werkende track te reconstrueren.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Diagram van een magneetstrip die de fysieke positie van tracks één, twee en drie toont, met het veldindeling van elke track inclusief sentinels, PAN, naam, vervaldatum en servicecode" >}}

## Hoe Trackgegevens Te Lezen

**Een magneetstripstring is een reeks velden, geen tweede kaartnummer.** De lezer vindt de startsentinel, scheidt velden, leest de vervaldatum en servicecode, en controleert dan de eindsentinel en LRC.

| Spoor | Start | Hoofdvelden | Einde | Tekenset |
|---|---|---|---|---|
| **Spoor 1** | `%` | Formaatcode, PAN, naam, vervaldatum, servicecode, discretionaire gegevens | `?` plus LRC | Zes-bit ALPHA, dus het bevat letters |
| **Spoor 2** | `;` | PAN, vervaldatum, servicecode, discretionaire gegevens | `?` plus LRC | Vier-bit BCD, dus het bevat cijfers en een kleine set leestekens |

De optionele sentinels identificeren de fysieke recordgrenzen. Een decoder laat ze vaak weg bij het weergeven van de velden, maar een fysieke encoder heeft het volledige recordformaat nodig dat de lezer verwacht.

### Voorbeeld Spoor 1

Dit is een synthetisch voorbeeld. Het gebruikt de standaard test-PAN van de tool en nepnaam, vervaldatum, servicecode en discretionaire gegevens. Het is geen Privacy.com-kaart en het zijn geen geldige betalingsgegevens.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Lees het van links naar rechts:

| Segment | Waarde | Betekenis |
|---|---|---|
| **Start sentinel** | `%` | Spoor 1 record begint |
| **Formaatcode** | `B` | Financieel kaartformaat B |
| **PAN** | `4111111111111111` | Synthetisch primair rekeningnummer |
| **Veldscheidingsteken** | `^` | PAN eindigt en naam begint |
| **Naam** | `TEST/USER` | Achternaam, scheidingsteken, voornaam |
| **Veldscheidingsteken** | `^` | Naam eindigt en transactiedata begint |
| **Vervaldatum** | `2912` | December 2029 in YYMM-vorm |
| **Servicecode** | `501` | Nationale uitwisseling, normale verwerking, geen beperkingen |
| **Discretionaire gegevens** | `0000000` | Uitgever-gedefinieerde opvulling in dit voorbeeld |
| **Eind sentinel** | `?` | Spoor 1 data eindigt voor de LRC |

Het echt gecodeerde record bevat ook een LRC-teken na de eind sentinel wanneer de lezer dit verwacht. De zichtbare tekstvorm is nuttig om de structuur te bestuderen. De bitniveauweergave bevat ook oneven pariteit voor elk teken.

### Voorbeeld Spoor 2

Spoor 2 verwijdert de naam en formaatcode. Dezelfde synthetische waarden worden:

```text
;4111111111111111=291250100000000?
```

| Segment | Waarde | Betekenis |
|---|---|---|
| **Start sentinel** | `;` | Spoor 2 record begint |
| **PAN** | `4111111111111111` | Synthetisch primair rekeningnummer |
| **Scheidingsteken** | `=` | PAN eindigt en transactiedata begint |
| **Vervaldatum** | `2912` | December 2029 in YYMM-vorm |
| **Servicecode** | `501` | Zelfde synthetische servicecode als Spoor 1 |
| **Discretionaire gegevens** | `0000000` | Uitgever-gedefinieerde opvulling in dit voorbeeld |
| **Eind sentinel** | `?` | Spoor 2 data eindigt voor de LRC |

**Spoor 2 is korter omdat het geen kaarthoudernaam bevat.** Veel terminals lezen Spoor 2 voor gewone swipe-transacties, terwijl Spoor 1 het naamveld levert wanneer een lezer dit opvraagt.

### Servicecode Cijfers

**De drie servicecode cijfers beschrijven terminal- en autorisatiegedrag.** Ze bevatten niet de CVV, en het wijzigen ervan op een echte kaart zonder toestemming van de uitgever levert een verkeerd of misleidend betalingsbewijs op.

| Cijfer | Waarden | Wat het beschrijft |
|---|---|---|
| **Eerste** | `0`, `1`, `2`, `5`, `6`, `7`, `9` | Uitwisselingsregels en chipvoorkeur |
| **Tweede** | `0`, `1`, `2`, `4` | Autorisatiepad |
| **Derde** | `0` tot `7` | PIN, contant, goederen-en-diensten beperkingen |

**Eerste cijfer** betreft uitwisseling en chipvoorkeur:

| Waarde | Betekenis |
|---|---|
| `0` | Nationaal gebruik |
| `1` | Internationale uitwisseling toegestaan |
| `2` | Internationale uitwisseling, gebruik IC (chip) waar mogelijk |
| `5` | Alleen nationale uitwisseling behalve onder bilaterale overeenkomst |
| `6` | Alleen nationale uitwisseling behalve onder bilaterale overeenkomst, gebruik IC waar mogelijk |
| `7` | Geen uitwisseling behalve onder bilaterale overeenkomst (gesloten lus) |
| `9` | Test |

**Tweede cijfer** betreft autorisatieverwerking:

| Waarde | Betekenis |
|---|---|
| `0` | Normale autorisatie |
| `1` | Normale autorisatie |
| `2` | Neem contact op met uitgever via online middelen |
| `4` | Neem contact op met uitgever via online middelen behalve onder bilaterale overeenkomst |

**Derde cijfer** betreft servicebeperkingen:

| Waarde | Betekenis |
|---|---|
| `0` | Geen beperkingen, PIN vereist |
| `1` | Geen beperkingen |
| `2` | Alleen goederen en diensten (geen contant) |
| `3` | Alleen geldautomaat, PIN vereist |
| `4` | Alleen contant |
| `5` | Alleen goederen en diensten (geen contant), PIN vereist |
| `6` | Geen beperkingen, gebruik PIN waar mogelijk |
| `7` | Alleen goederen en diensten (geen contant), gebruik PIN waar mogelijk |

Bijvoorbeeld, `201` betekent internationale uitwisseling met chipgebruik waar mogelijk, normale autorisatieverwerking en geen servicebeperkingen. De decoder toont elk cijfer apart zodat je de tabel niet uit je hoofd hoeft te leren.

### LRC en Pariteit

**De LRC is een controleteken, geen extra veld om te verzinnen.** De encoder XOR't de datawaarde van elk teken van de start sentinel tot de eind sentinel. Het zet het resultaat terug om in het afdrukbare tekenbereik van het spoor en rapporteert de gecodeerde oneven-pariteitsbits apart.

Spoor 1 gebruikt een zes-bit ALPHA-tekenset. De datawaarde is de ASCII-code minus `0x20`. Spoor 2 gebruikt een vier-bit BCD-tekenset. De datawaarde is de lage nibble van de ASCII-code. Toepassing van de Spoor 1 mapping op Spoor 2 geeft de verkeerde LRC.

De decoderoptie **Inclusief berekende LRC** voegt het afdrukbare LRC-teken toe aan de uitvoer. De uitsplitsing toont ook het LRC-bitpatroon met oneven pariteit. Gebruik dit om te leren hoe een lezer het record controleert, niet om de controles van een uitgever te omzeilen.

## Synthetische kaarten schrijven voor testen

**Gebruik de decoder om teststrings te schrijven, niet voor echte betaalkaarten.** De tool accepteert velden, bouwt Spoor 1 en Spoor 2 opnieuw op, voegt optionele sentinels toe en berekent de LRC. Het draait lokaal in de browser.

1. Open de **[Magneetstripdecoder en -encoder](/magnetic-stripe-decoder/)**.
2. Selecteer **Load Test Card**. Dit vult de tool met de synthetische PAN `4111111111111111`, de naam `TEST/USER`, vervaldatum `2912`, servicecode `201` en test discretionaire gegevens.
3. Schakel **Include start and end sentinels** in om de fysieke recordgrenzen weer te geven.
4. Schakel **Include calculated LRC** in om het berekende controleteken toe te voegen.
5. Schakel **Split discretionary data into PVKI, PVV and CVV** alleen in om te zien hoe een negencijferig synthetisch veld wordt weergegeven. Die labels zijn issuer-conventies, geen universele Track 1- of Track 2-indeling.
6. Wijzig de naam, vervaldatum, servicecode of synthetische discretionaire gegevens. De uitvoer wordt tijdens het typen bijgewerkt.
7. Vergelijk de gedecodeerde velden met de gegenereerde strings. Maak de velden leeg als je klaar bent.

Voor een synthetische Track 1-oefening, gebruik:

```text
PAN: 4111111111111111
Achternaam: TEST
Voornaam: USER
Vervaldatum: 12/29
Servicecode: 201
Discretionaire gegevens: 000000000
```

Voor een synthetische Track 2-oefening, gebruik dezelfde PAN, vervaldatum, servicecode en een numeriek discretionair veld. De gegenereerde Track 2-string laat de naam weg omdat Track 2 geen naamveld heeft.

**Kopieer geen live Privacy.com PAN, vervaldatum, CVV of discretionaire waarde naar een beschrijfbare kaart.** Privacy.com beschrijft zijn product als virtuele kaartnummers die via de website of app worden aangemaakt. De officiële pagina presenteert de dienst niet als een systeem voor het schrijven van magnetische strepen, terwijl een virtueel kaartnummer geen bewijs is van een door de issuer geautoriseerd fysiek streeprecord. Een beschrijfbare testkaart met een live credential creëert een duplicaat betaalinstrument en overtreedt issuer-voorwaarden of betalingsregels.

De veilige grens is eenvoudig: gebruik de ingebouwde synthetische voorbeeldkaart van de tool, gebruik een labkaart met dummywaarden en gebruik een door de issuer goedgekeurde fysieke kaart wanneer je persoonlijk wilt betalen. Probeer geen Privacy.com virtuele kaart om te zetten in een fysieke swipe-kaart.

## Wat een Virtuele Kaart Verandert

**Een virtuele kaart is een tweede nummer dat voor het eerste staat.**

Wanneer je betaalt met een virtuele kaart, ontvangt de handelaar een nummer, vervaldatum en CVV die bij de virtuele kaart horen. Je echte PAN bereikt hen nooit. Praktisch gezien wordt het verschil duidelijk na een datalek:

| Scenario | Met Je Echte Kaart | Met een Merchant-Locked Virtuele Kaart |
|---|---|---|
| **Handelaar database gelekt** | Het nummer is geldig overal waar het wordt geaccepteerd | Het nummer faalt bij elke andere handelaar |
| **Abonnement dat je hebt geannuleerd** | Incasso gaat door tot je het betwist | Je sluit de kaart en de incasso faalt |
| **Proefperiode die stil converteert** | Ongewenste incasso op je afschrift | De limiet of sluiting stopt het |
| **Kaartgegevens verkocht op een forum** | Bruikbaar voor card-not-present fraude | Alleen bruikbaar bij één handelaar, als dat al |

**Wat het niet verandert** is net zo belangrijk. Je bank ziet de transactie nog steeds. Het kaartnetwerk verwerkt het nog steeds. De issuer kent je identiteit nog steeds, omdat anti-witwasregels verificatie vereisen. **Een virtuele kaart vermindert de blootstelling aan de handelaar. Het is geen manier om anoniem te betalen.**

*Het onderscheid verwart mensen constant. Als je dreigingsmodel de issuer of het netwerk omvat, verandert een virtuele kaart daar niets aan.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Diagram dat toont hoe een virtueel kaartnummer naar de handelaar gaat terwijl het echte kaartnummer tussen de kaarthouder en de uitgevende bank blijft" >}}

## Wat de winkelier nog ziet

**Een virtuele kaart schermt de betaalrekening en het oorspronkelijke PAN af.** De wijziging wist de gegevens van het afrekenen niet.

Volgens de ondersteuningsdocumentatie van Privacy deelt de kaart de volgende gegevens met een winkelier: het kaartnummer van 16 cijfers, de vervaldatum, de CVV en het factuuradres dat je bij het afrekenen invoert. De winkelier ziet ook de naam die je opgeeft. Lees de [officiële uitleg over zichtbare winkeliergegevens](https://support.privacy.com/hc/en-us/articles/24450438423063-What-information-does-Privacy-share-with-the-merchant) voordat je een virtuele kaart als bescherming van je identiteit beschouwt.

| Laag | Gegevens die zichtbaar blijven of worden bewaard |
|---|---|
| **Winkelier** | Virtueel kaartnummer, vervaldatum, CVV, factuuradres en naam die bij het afrekenen zijn opgegeven, bestelgegevens en gegevens van het winkelaccount |
| **Privacy.com** | Identiteitsgegevens, financieringsbron, kaartgegevens, transactiegegevens en apparaatgegevens volgens het [privacybeleid](https://www.privacy.com/privacy-policy) |
| **Financieringsbank** | Transactiedatum, bedrag en een omschrijving met Privacy.com of `PWP*`; de bank bepaalt de exacte weergave |
| **Betaalnetwerk en uitgever** | Autorisatie-, vereffenings-, fraude- en geschilgegevens die nodig zijn om de betaling te verwerken |

De praktische grens is eenvoudig. Een virtuele kaart beperkt hergebruik van kaartgegevens. Je naam, verzendadres, winkelaccount, browsersessie en andere gegevens die je buiten de kaartvelden invult, blijven zichtbaar voor de winkelier. Afzonderlijke winkelaccounts en e-mailaliassen helpen koppeling van je identiteit tussen sites te beperken. Een virtuele kaart biedt die scheiding op zichzelf niet.

## De Drie Soorten Kaartvormige Dingen

De terminologie wordt inconsistent gebruikt en het verschil is belangrijk als je kiest wat je aan een handelaar geeft.

| Type | Kaartnummer | Fysieke Versie | Typisch Gebruik |
|---|---|---|---|
| **Digitale kaart** | Zelfde als je fysieke kaart | Ja | Je bestaande kaart toevoegen aan een mobiele portemonnee |
| **Virtuele kaart** | Verschillend van elke fysieke kaart | Nee | Online aankopen, abonnementen, eenmalige handelaren |
| **Digital-first kaart** | Verschillend, met optionele gekoppelde fysieke kaart | Optioneel | Fintech-accounts waar de fysieke kaart geen geprinte gegevens draagt |

**Een mobiele portemonnee gebruikt een geheel vierde mechanisme.** Wanneer je een kaart aan een portemonnee toevoegt, slaat de portemonnee een apparaat-specifieke token op in plaats van je PAN, en ontvangt de handelaar die token. Dit heet tokenisatie en het is waarom betalen met een telefoon veiliger is dan het plastic overhandigen, zelfs zonder virtuele kaart.

*Netwerktokenisatie en virtuele kaarten lossen overlappende delen van hetzelfde probleem op. Tokenisatie beschermt het nummer tijdens verzending en opslag. Een virtuele kaart beschermt je tegen wat de handelaar daarna bewaart.*

## Privacy.com Kaarttypes

**Privacy.com biedt vier kaartgedragingen en ze zijn niet uitwisselbaar.**

| Kaarttype | Gedrag | Beste Voor |
|---|---|---|
| **Eenmalig gebruik** | Sluit automatisch na één transactie | Eenmalige aankopen en onbekende handelaren |
| **Merchant-Locked** | Vergrendelt op de eerste handelaar die het gebruikt en faalt elders | Dagelijks online winkelen |
| **Categoriegebonden** | Beperkt tot een uitgavencategorie | Het beheersen van een hele klasse uitgaven |
| **Everywhere** | Een fysieke kaart met hetzelfde beschermingsmodel | Aankopen in persoon |

**Merchant locking is het mechanisme dat het meeste waarde biedt.** Een vergrendelde kaart faalt bij elke handelaar behalve degene waarmee het eerst werd gebruikt, wat betekent dat een datalek bij die handelaar een nummer oplevert dat elders nutteloos is.

**Single-use is de sterkere optie waar van toepassing.** Een kaart die sluit na één incasso kan helemaal niet worden hergebruikt en het verwijdert de noodzaak om later te onthouden het te sluiten.

Twee operationele details die het waard zijn om te weten:

- **Gedeelde kaarten vergrendelen op de eerste handelaar waarmee ze worden gebruikt**, dus het delen met een familielid of werknemer draagt nog steeds de handelaarbeperking.
- **Een kaart wordt gepauzeerd in plaats van gesloten.** Pauzeren is omkeerbaar, wat handig is als je een abonnement tijdelijk wilt stoppen zonder de kaartgegevens te verliezen.

## Uitgavelimieten en Controle

**Elke kaart heeft een uitgavelimiet, wat een aparte controle is van merchant locking.**

| Controle | Wat Het Voorkomt |
|---|---|
| **Limiet per transactie** | Eén enkele incasso groter dan je hebt toegestaan |
| **Maandelijkse limiet** | Opeenstapeling van incasso's over een factureringsperiode |
| **Pauzeren** | Elke incasso, omkeerbaar |
| **Sluiten** | Elke toekomstige incasso, permanent |

**Stel zowel een limiet per transactie als een maandelijkse limiet in op elke kaart die aan een abonnement is gekoppeld.** Een handelaar die stilletjes zijn prijs verhoogt, raakt de limiet in plaats van je saldo, en je merkt het aan een mislukte incasso in plaats van een ontbrekende afschriftregel.

*Onze **[Persoonlijke Financiële Veiligheid](/personal-security-course/personal-finance/)** module plaatst dit naast kredietbevriezingen en kaarttokenisatie als de drie controles die beperken wat een enkele gecompromitteerde handelaar kan bereiken.*

## Terugkerende kosten en autorisaties

**Kaartbediening werkt op het moment van autorisatie.** Privacy beschrijft een transactie in behandeling als toestemming voor de winkelier om een afgesproken bedrag af te schrijven. Een autorisatie van $0 controleert of een kaart actief is. Ze is geen voltooide aankoop. Bij transacties via een bank volgt eerst een vereffeningsfase voordat de afschrijving is afgerond. Zie de [officiële uitleg over transactiestatussen](https://support.privacy.com/hc/en-us/articles/360012287514-Transaction-states-pending-settling-settled-and-authorized).

| Gebeurtenis | Wat er gebeurt | Grens van de instelling |
|---|---|---|
| **Kaart toevoegen aan een dienst** | De winkelier stuurt een autorisatie van $0 om de kaart te controleren | Een geldige kaartcontrole bewijst niet dat een bestelling is betaald |
| **Aankoop geautoriseerd** | Privacy registreert een bedrag in behandeling en geeft de winkelier toestemming om het afgesproken bedrag te innen | Beschikbare middelen en latere autorisaties houden rekening met de transactie in behandeling |
| **Aankoop vereffend** | De financieringsbron wordt afgeschreven nadat de winkelier de transactie heeft verwerkt | Wijzigingen in de bestelling of een extra fooi kunnen het eindbedrag anders maken dan de eerste autorisatie |
| **Kaart gepauzeerd of gesloten na autorisatie** | Toekomstige autorisaties worden tegengehouden | Een eerdere autorisatie blijft onder de regels van het betaalnetwerk vallen |
| **Bestedingslimiet gewijzigd na autorisatie** | De nieuwe limiet geldt voor toekomstige pogingen | De eerdere autorisatie behoudt haar bestaande status |

**Een kaartlimiet is geen vooruitbetaald saldo.** Volgens de specifieke kaartgids van Privacy blokkeert de limiet autorisatiepogingen boven het gekozen bedrag. De financieringsbron wordt afgeschreven wanneer transacties worden afgerond. De voortschrijdende perioden omvatten 24 uur voor daglimieten, 30 dagen voor maandlimieten en 364 dagen voor jaarlimieten, met voor sommige abonnementsperioden een buffer van zes dagen. De [officiële gids over bestedingslimieten](https://support.privacy.com/hc/en-us/articles/360012285094-How-do-Privacy-Card-specific-spending-limits-work) beschrijft deze regels.

Stel voor abonnementen vóór de eerste afschrijving een terugkerende limiet in, controleer transacties in behandeling en tijdens vereffening, en zeg het abonnement ook bij de winkelier op. Een kaart sluiten blokkeert toekomstige autorisaties. Het annuleert geen reeds geautoriseerde aankoop en levert geen terugbetaling op. De [gids voor pauzeren en sluiten](https://support.privacy.com/hc/en-us/articles/360039148094-How-do-I-pause-close-Privacy-Cards) van Privacy beschrijft dezelfde grens.

## Plannen en Wat Elk Ontgrendelt

Privacy.com biedt een gratis abonnement naast drie betaalde plannen. Prijzen en functielimieten kunnen veranderen, dus controleer de actuele voorwaarden voordat je je abonneert.

| Plan | Prijs | Opvallende toevoegingen |
|---|---|---|
| **Persoonlijk (gratis)** | $0 | Virtuele kaarten, koppeling aan handelaar, bestedingslimieten, geen kosten voor binnenlandse transacties |
| **Plus** | $5/maand | Categoriekaarten, kaartnotities voor het organiseren van uitgaven |
| **Pro** | $10/maand | Cashback op in aanmerking komende aankopen, fysieke Everywhere-kaarten |
| **Premium** | $25/maand | Alles in Pro, met een verhoogde maandelijkse limiet voor kaartaanmaak tot 60 |

**De gratis laag dekt het kernvoordeel op het gebied van beveiliging.** Koppeling aan handelaar, eenmalige kaarten en bestedingslimieten zijn de mechanismen die blootstelling verminderen, en deze zijn beschikbaar zonder te betalen. De betaalde lagen voegen organisatie en gemak toe, niet extra bescherming.

**Buitenlandse transactiekosten verschillen per laag.** De gratis laag rekent 3% op buitenlandse transacties met een minimum van $0,50, terwijl de betaalde lagen dit niet doen.

Lees de [actuele voorwaarden van Privacy.com](https://www.privacy.com/terms) voordat je je abonneert.

## Wat Privacy.com Niet Doet

**Duidelijkheid over de beperkingen is nuttiger dan een lijst met functies.**

| Beperking | Detail |
|---|---|
| **Het maakt je niet anoniem** | Je identiteit wordt geverifieerd bij aanmelding en de uitgever bewaart deze |
| **Het verbergt de transactie niet voor je bank** | Je bank ziet de overboeking en het netwerk ziet de afschrijving |
| **Het bouwt geen krediet op** | Dit zijn geen kredietrekeningen en er vindt geen kredietcontrole plaats |
| **Het is alleen voor de VS** | Vereist Amerikaans staatsburgerschap of legaal verblijf en een Amerikaanse bank- of credit union-rekening |
| **Het vereist identiteitsverificatie** | Know Your Customer-controles zijn verplicht volgens anti-witwasregels |
| **Het dekt niet elke handelaar** | Sommige handelaren blokkeren prepaid- en virtuele kaartreeksen |

**Het punt over het blokkeren door handelaren is in de praktijk belangrijk.** Sommige abonnementsdiensten en luchtvaartmaatschappijen weigeren kaartreeksen die zij associëren met virtuele of prepaidkaarten, en geen enkele configuratie lost dit op. Houd een echte kaart achter de hand als noodoplossing voor die gevallen.

*De eerlijke samenvatting: een virtuele kaart is een beheersmaatregel om blootstelling aan de kant van de handelaar te beperken, geen anonimiteitstool. Als je anonimiteit nodig hebt, is dat een ander probleem met andere hulpmiddelen.*

## Wie Geeft de Kaart Uit en Waarom Dat Belangrijk Is

**Een virtuele kaart is nog steeds een echte kaart, uitgegeven door een echte bank, onder een echte schemalicentie.**

| Detail | Waarde |
|---|---|
| **Uitgevende bank** | Patriot Bank, N.A., lid FDIC |
| **Schemalicenties** | Mastercard en Visa |
| **Waar het wordt geaccepteerd** | Overal waar Mastercard en Visa worden geaccepteerd |
| **Financiering** | Overgemaakt vanaf je gekoppelde Amerikaanse betaalrekening |

**Dit is waarom de bescherming echt is.** De kaart heeft dezelfde schema-beschermingen als elk ander Mastercard- of Visa-product, wat betekent dat rechten op terugboekingen en fraudeprocedures normaal van toepassing zijn. Het is geen cadeaubon of een gesloten winkelkrediet.

Twee certificeringen zijn het noemen waard omdat ze onafhankelijk verifieerbaar zijn in plaats van marketingclaims:

- **PCI-DSS-naleving**, de standaard van de betaalkaartindustrie voor het omgaan met kaartgegevens
- **SOC 2 Type II**, een geaudit rapport dat beveiligingscontroles over een periode behandelt in plaats van een momentopname

**Over het bedrijfsmodel:** het bedrijf geeft aan inkomsten te genereren uit interchange van handelaren en verkoopt geen klantgegevens aan adverteerders of derden. Dit is hetzelfde verdienmodel als elke andere kaartuitgever, wat het waard is om te begrijpen in plaats van als ongewoon te beschouwen.

*De praktische reden om de uitgevende bank te controleren is verificatie. Iedereen beweert een kaartprogramma te runnen, en de naam van de uitgever op de kaart is wat je verifieert met de bank die in de documenten staat.*

Controleer het schema en de bank via het PAN-prefix met de **[Magneetstripdecoder](/magnetic-stripe-decoder/)**, die het hoofdschema-gebied rapporteert en de Luhn-controlecijfer valideert.

## Accountherstel en afhankelijkheid van de aanbieder

**Toegang tot je account is een afzonderlijke beveiliging naast kaartscheiding.** Bij niet-herkende activiteit adviseert Privacy contact op te nemen met de winkelier, 2FA en gedeelde kaarten te controleren, inlogcodes voor nieuwe apparaten na te kijken, het wachtwoord opnieuw in te stellen en ondersteuning te contacteren. De [beveiligingsgids voor accounts](https://support.privacy.com/hc/en-us/articles/7971053265815-What-should-I-do-if-I-don-t-recognize-activity-on-my-Privacy-Account) noemt deze stappen.

Houd het hersteladres en je Amerikaanse telefoonnummer actueel. Volgens Privacy is bevestiging nodig wanneer een van deze gegevens verandert. Zie de [gids voor accountgegevens](https://support.privacy.com/hc/en-us/articles/7970949442583-How-do-I-update-my-email-address-or-phone-number). Schakel 2FA in en bewaar winkelnamen en de laatste vier kaartcijfers in een wachtwoordbeheerder. Zet een volledig PAN of CVV niet in een gewone notitie-app.

Je account sluiten verwijdert niet alle gegevens. Het beleid van Privacy, voor het laatst bijgewerkt op 8 juni 2026, noemt bewaartermijnen van minstens vijf jaar voor identiteitsverificatie- en betaalkaartgegevens, zes jaar voor gegevens van de financieringsbank en ACH-transacties, en drie jaar voor auditlogboeken. Lees het onderdeel over bewaren in het [privacybeleid van Privacy](https://www.privacy.com/privacy-policy) voordat je accountsluiting als gegevensverwijdering beschouwt.

**Privacy blijft afhankelijk van de financieringsbank, Plaid, ACH, kaartnetwerken en de eigen accountsystemen.** Bankfinanciering gebruikt ACH via Plaid. Privacy vermeldt een alternatieve financiering met een betaalkaart voor banken die niet worden ondersteund, maar toegang blijft afhankelijk van een Amerikaanse bank of kredietunie en een Amerikaans telefoonnummer. De [gids voor bankkoppeling](https://support.privacy.com/hc/en-us/articles/360040584834-How-do-I-connect-a-bank-account) en de [toelatingsgids](https://support.privacy.com/hc/en-us/articles/360012046934-Who-can-use-Privacy) beschrijven deze voorwaarden.

Financieringsproblemen kunnen betalingen onderbreken. Privacy documenteert tijdelijke accountpauzes wanneer de dienst een financieringsbron niet kan afschrijven, bijvoorbeeld door onvoldoende saldo of een gesloten account. De ondersteuningspagina vermeldt ook dat het verwijderen van een financieringsbron transacties die al tegen die bron zijn geautoriseerd niet stopt. Lees de [gids voor niet-vereffende transacties](https://support.privacy.com/hc/en-us/articles/34877696240535-How-do-I-resolve-an-unsettled-transaction) en de [gids voor het verwijderen van een financieringsbron](https://support.privacy.com/hc/en-us/articles/360041454834-How-do-I-remove-a-funding-source-from-my-Privacy-Account) voordat je een bank of betaalkaart verwijdert.

| Afhankelijkheid | Foutscenario | Praktische reactie |
|---|---|---|
| **Financieringsbank of Plaid** | Niet-ondersteunde, gesloten of verouderde koppeling | Houd een geschikte alternatieve bron aan en controleer de accountstatus |
| **Privacy-account** | Nieuwe identiteitscontrole, verloren herstelkanaal of accountopschorting | Houd 2FA en herstelgegevens actueel |
| **Winkelier** | Virtuele of prepaid kaartreeks geweigerd, of terugkerende afschrijving blijft doorgaan | Houd voor uitzonderingen een echte kaart achter de hand en zeg op bij de winkelier |
| **Netwerk of uitgever** | Vertraging bij autorisatie, vereffening, terugbetaling of geschil | Bewaar bonnen, afschriften en transactiegegevens |

De voorwaarden van Privacy beschrijven diensten die het bedrijf en zijn financiële partners afzonderlijk leveren. De voorwaarden staan ook toe dat aanvullende identiteitsgegevens worden opgevraagd en accounts worden beperkt. Neem toegang tot de aanbieder en accountgegevens mee in je dreigingsmodel. Laat niet al je essentiële rekeningen via één kaartaanbieder lopen.

## Virtuele Kaarten Goed Gebruiken

**De controles helpen alleen als je ze instelt.** Zes gewoonten leveren het meeste voordeel op.

1. **Koppel elke kaart aan een handelaar** tenzij er een reden is om dat niet te doen. De koppeling maakt een gelekt nummer nutteloos.
2. **Gebruik eenmalige kaarten voor alles wat onbekend is**, inclusief proefperiodes en eenmalige aankopen bij kleinere sites.
3. **Stel beide bestedingslimieten in** op abonnementskaarten, zodat een prijsverhoging mislukt in plaats van wordt afgeschreven.
4. **Noem elke kaart naar de handelaar**, zodat een transactielijst leesbaar is en een onverwachte afschrijving opvalt.
5. **Pauzeer in plaats van sluit** als je van plan bent een dienst te hervatten, en sluit als je dat niet doet.
6. **Houd een echte kaart achter de hand voor handelaren die virtuele reeksen weigeren**, zodat een geblokkeerde kassa geen noodsituatie wordt.

> **Veelgemaakte fout: een virtuele kaart zien als vervanging voor het controleren van je afschriften.** Koppeling aan handelaar voorkomt één soort schade. Het detecteert geen gecompromitteerde rekening bij je bank, geen ongeautoriseerde overboeking of frauduleuze afschrijving op de echte kaart erachter.

## Huidige grenzen van de bediening

De huidige ondersteuningsdocumentatie van Privacy.com zegt dat een specifieke bestedingslimiet autorisatiepogingen boven die limiet blokkeert. De [gids voor bestedingslimieten](https://support.privacy.com/hc/en-us/articles/360012285094-How-do-Privacy-Card-specific-spending-limits-work) beschrijft ook voortschrijdende perioden. De [kaartdocumentatie voor ontwikkelaars](https://developers.privacy.com/docs/cards) noemt kaarten die aan een winkelier zijn gebonden en velden voor bestedingslimieten.

| Instelling | Helpt tegen | Lost niet op |
|---|---|---|
| Aan een winkelier gebonden kaart | Hergebruik van een nummer bij een andere winkelier | Een gehackt Privacy.com-account of een frauduleuze transactie bij de bedoelde winkelier |
| Bestedingslimiet | Onverwachte autorisatiebedragen en afwijkingen bij terugkerende afschrijvingen | Een afschrijving vóór je de limiet wijzigt of een gehackte financieringsrekening |
| Virtuele kaart sluiten | Toekomstige autorisaties op dat nummer | Een terugbetaling, geschil of al aangemaakt winkelierrecord |
| Afzonderlijke kaart per dienst | Een transactie snel herkennen en de kaart intrekken | Uitval bij de aanbieder, identiteitscontroles of gegevens bij de bank |

Controleer de financieringsrekening, accountherstelmethoden, waarschuwingen en kaartenlijst als één geheel. Een virtueel nummer verandert welk nummer je met een winkelier deelt. Het verbergt de transactie niet voor de uitgevende bank, kaartaanbieder, winkelier, betaalnetwerken, belastinggegevens of een rechtbank met wettelijke bevoegdheid. Het maakt van een betaalkaart geen kredietlijn en garandeert geen gunstige uitkomst van een geschil.

## Belangrijkste Punten

- **Een virtuele kaart verandert het nummer dat de handelaar opslaat.** Je echte PAN bereikt hen nooit, dat is het hele mechanisme.
- **Het maakt de transactie niet privé.** Je bank, het netwerk en de uitgever zien het nog steeds, en identiteitsverificatie is verplicht.
- **Koppeling aan handelaar is de meest waardevolle functie**, omdat een gelekt nummer dan nergens anders werkt.
- **De gratis laag bevat de beveiligingscontroles.** Betaalde plannen voegen organisatie en gemak toe, geen extra bescherming.
- **De magneetstrip slaat kaartgegevens in platte tekst op** en wordt tegen 2033 verwijderd, met Amerikaanse banken die uitgifte stoppen in 2027.
- **De CVV staat niet op de strip**, daarom mist een skimmer die tracks kopieert wat veel online handelaren vereisen.
- **Sommige handelaren weigeren virtuele kaartreeksen.** Houd een echte kaart als noodoplossing.
- **Verifieer de uitgevende bank** in plaats van te vertrouwen op een kaartprogramma-claim, en controleer het PAN-prefix zelf.

## Volgende Stappen

1. **Inspecteer de trackgegevens van je eigen kaart** en zie precies wat een magneetstrip bevat: **[Magneetstripdecoder en -encoder](/magnetic-stripe-decoder/)**
2. **Bevries je krediet** als je dat nog niet hebt gedaan, dit is de sterkere maatregel tegen fraude bij nieuwe accounts: **[Beveiliging van persoonlijke financiën](/personal-security-course/personal-finance/)**
3. **Pas de tiering-discipline toe** om te bepalen hoeveel moeite dit voor jouw situatie waard is: **[Geprioriteerde checklist voor persoonlijke beveiliging](/articles/personal-security-checklist-prioritized-2026/)**
4. **Bekijk de Privacy.com-abonnementen en actuele voorwaarden** voordat je je aanmeldt: **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Controleer of je gegevens al in een datalek voorkomen** voordat je aanneemt dat je niet bent getroffen: **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Lees de checklist voor betalingsbeveiliging** voor de organisatorische tegenhanger: **[Checklist voor incidentrespons](/checklists/incident-response-checklist/)**

## Referenties

1. [Privacy.com - wat virtuele kaarten zijn, merchant locking en bestedingslimieten](https://www.privacy.com/virtual-card)
2. [Digital card - Wikipedia, over digitale versus virtuele kaarten, magneetstriptracks, servicecodes, pariteit en LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 - identificatiekaarten, financiële transactiekaarten, tracks 1 en 2 datastructuur](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 - trackveldindeling in detail, inclusief sentinels en servicecodes](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [PCI Security Standards Council - vereisten voor de cardholder data environment](https://www.pcisecuritystandards.org/)
6. [Consumer Financial Protection Bureau - kredietrapporten en scores](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [ANSI/ISO ALPHA data-encoding, de Track 1-tekenset en pariteitstabel](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [ISO-tekens voor magnetische kaarten, de Track 1- en Track 2-sets naast elkaar](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Magnetische kaartgegevens lezen, een praktische walkthrough met een live kaartscan](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)
10. [Privacy-ontwikkelaarsdocumentatie: kaarttypen, statussen en bestedingslimieten](https://developers.privacy.com/docs/cards)
11. [Privacy-ondersteuning: gegevens die met winkeliers worden gedeeld](https://support.privacy.com/hc/en-us/articles/24450438423063-What-information-does-Privacy-share-with-the-merchant)
12. [Privacy-ondersteuning: bestedingslimieten voor afzonderlijke kaarten](https://support.privacy.com/hc/en-us/articles/360012285094-How-do-Privacy-Card-specific-spending-limits-work)
13. [Privacy-ondersteuning: transactiestatussen en autorisaties](https://support.privacy.com/hc/en-us/articles/360012287514-Transaction-states-pending-settling-settled-and-authorized)
14. [Privacy-ondersteuning: kaarten pauzeren en sluiten](https://support.privacy.com/hc/en-us/articles/360039148094-How-do-I-pause-close-Privacy-Cards)
15. [Privacy-ondersteuning: omschrijvingen op bankafschriften](https://support.privacy.com/hc/en-us/articles/360012407533-What-will-I-see-on-my-bank-statement-when-I-make-a-purchase-with-Privacy)
16. [Privacy-ondersteuning: een bankrekening koppelen via Plaid](https://support.privacy.com/hc/en-us/articles/360040584834-How-do-I-connect-a-bank-account)
17. [Privacy-ondersteuning: accountactiviteit en herstelcontroles](https://support.privacy.com/hc/en-us/articles/7971053265815-What-should-I-do-if-I-don-t-recognize-activity-on-my-Privacy-Account)
18. [Privacy-ondersteuning: e-mailadres en telefoonnummer van het account bijwerken](https://support.privacy.com/hc/en-us/articles/7970949442583-How-do-I-update-my-email-address-or-phone-number)
19. [Privacy-ondersteuning: voorwaarden om een account te gebruiken](https://support.privacy.com/hc/en-us/articles/360012046934-Who-can-use-Privacy)
20. [Privacy-ondersteuning: niet-vereffende transacties](https://support.privacy.com/hc/en-us/articles/34877696240535-How-do-I-resolve-an-unsettled-transaction)
21. [Privacy-ondersteuning: een financieringsbron verwijderen](https://support.privacy.com/hc/en-us/articles/360041454834-How-do-I-remove-a-funding-source-from-my-Privacy-Account)
22. [Privacy.com-privacybeleid](https://www.privacy.com/privacy-policy)
23. [Gebruiksvoorwaarden van Privacy.com](https://www.privacy.com/terms)
