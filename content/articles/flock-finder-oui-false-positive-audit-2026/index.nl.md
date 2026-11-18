---
title: "We brachten 146.526 ‘Flock-camera’s’ in kaart. 50.278 waren ClickShare-systemen"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Een audit van Flock Finder vindt ClickShare en andere fout-positieven, legt het bewijs uit en documenteert de wijzigingen."
genre: ["Beveiligingsonderzoek", "Privacytechnologie", "Open-sourceprojecten", "Datajournalistiek", "Tegentoezicht"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "OUI-fingerprinting", "WiGLE", "Fout-positieven", "Datakwaliteit", "Barco ClickShare", "MAC-adres", "IEEE OUI", "Fingerprinting van informatie-elementen", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Open-sourceverantwoording", "Toezichtskaarten", "WiFi", "Probe Request", "MAC-randomisatie"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "Een donkere stadskaart vol rode markeringen die kantoor-WiFi-apparaten blijken te zijn, terwijl enkele groene markeringen sterkere detecties aangeven"
coverCaption: "Een audit van 146.526 Flock Finder-records liet zien hoe een nuttige veldwaarneming veranderde in een te stellige kaartclaim."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**We plaatsten 146.526 punten op een kaart met bewakingscamera’s. Minstens 50.278 daarvan waren Barco ClickShare-presentatiesystemen. Apparatuur in vergaderruimten vormde meer dan een derde van wat onze kop ‘In kaart gebrachte camera’s’ noemde.**

Dit was ons project, onze datapijplijn en onze fout. Flock Finder vroeg WiGLE dagelijks naar MAC-prefixen die op Flock Safety-camera’s waren waargenomen, publiceerde resultaten met volledige coördinaatprecisie en gaf alle resultaten dezelfde markering. De metadata bevatte het woord `suspected` en de documentatie noemde fout-positieven. Toch straalden de kaart en de kop zekerheid uit.

**Wat je leert:** reproduceer de audit, scheid waarneming van toeschrijving en toon vertrouwen bij zowel de markering als de kop. Een prefixovereenkomst is een aanknopingspunt voor onderzoek, geen bewijs van een camera.

Toen we eindelijk een frequentiehistogram van de SSID-kolom maakten, legde de dataset de fout binnen enkele minuten bloot. ClickShare was alleen de grootste categorie. Nog eens 6.099 records heetten `SMARTGATE_*`, 3.801 begonnen met de algemene WiFi Direct-prefix `DIRECT-`, 314 hadden exact de naam `AndroidAP`, 138 vermeldden `Audi HUD`, 133 `MAX-PRINTER`, en 30 bevatten het oordeel van een andere detector. In totaal **voldeden 60.793 rijen, of 41,5%, aan de bekende naamregels voor andere apparaten uit de oorspronkelijke audit.**

Flock Finder publiceert nu een bewijsklasse per record, sluit bekende andere apparatuur standaard uit van kaart en kop, biedt filters, markeert records buiten de primaire markt en scheidt prefixen met hoog vertrouwen van prefixen van contractfabrikanten. Dit artikel beschrijft de fout, het bewijs en de resterende beperkingen.

______

## Hoe community-ALPR-detectie werkt

Door de community gebouwde Flock-detectoren combineren meestal drie soorten draadloos bewijs:

1. **WiFi MAC/OUI-prefixen.** De eerste bytes van een wereldwijd beheerd MAC-adres kunnen de organisatie aanwijzen waaraan het adresblok is toegewezen.
2. **WiFi-gedrag.** Een SSID, wildcard-probeverzoek, ontvangeradres, kanaalpatroon of reeks 802.11-informatie-elementen kan de apparaatklasse nader bepalen.
3. **Bluetooth-bewijs.** Fabrikant-ID’s en service-UUID’s kunnen radio’s identificeren die een product of firmwaregeneratie uitzendt.

OUI-matching werd populair omdat het goedkoop en passief is. Een betaalbare ESP32 kan nabijgelegen 802.11-frames bekijken zonder verbinding te maken met een netwerk. Een historische database zoals [WiGLE](https://wigle.net/) laat projecten ook eerdere waarnemingen doorzoeken zonder eigen scanners te plaatsen.

De aanpak volgde een communitylijn: het kaartwerk en de lokale organisatie van [DeFlock](https://deflock.org/), [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), forks en verwante projecten zoals onze [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32), en uiteindelijk [Flock Finder](https://github.com/simeononsecurity/flock-finder), dat de prefixlijst wereldwijd op WiGLE-data toepaste.

Het oorspronkelijke veldwerk verdient duidelijke erkenning. [@NitekryDPaul](https://github.com/NitekryDPaul) zag 30 prefixen op echte Flock-apparatuur tijdens onderzoek in promiscuous mode. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) droeg er tijdens veldtests nog een bij. Die waarnemingen waren legitiem. Onze fout achteraf was dat we **‘waargenomen op een Flock-camera’ behandelden alsof het ‘exclusief voor Flock-camera’s’ betekende.**

______

## De structurele fout: een OUI is een toeleveringsketenfeit

IEEE beschrijft een OUI als een 24-bits identificatie die aan een leverancier, fabrikant of andere organisatie wordt toegewezen. Samen met 24 bits die de ontvanger kiest, vormt die een MAC-adres. De [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/) publiceert het register.

Dit vertelt wie een adresblok kreeg, niet noodzakelijk welk merk op een eindproduct staat. Contractfabrikanten bouwen radiomodules voor veel klanten. Eén chipfabrikant kan dus voorkomen in camera’s, projectoren, printers, voertuigen en hobbyborden.

De registertoewijzingen achter onze lijst maakten het risico zichtbaar:

| Registrant | Prefixen in de gecontroleerde lijst |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` en andere |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

De Espressif-vermeldingen hadden ons moeten waarschuwen. Twee prefixen in een vermeende cameralijst behoorden toe aan de maker van een van ’s werelds meest gebruikte ingebouwde WiFi-platforms, waaronder de chips die veel communitydetectoren gebruiken.

`B4:1E:52` is anders, want het staat rechtstreeks op naam van Flock Safety. Het werd toegevoegd aan de lijst van 38 prefixen in de gecontroleerde commit, **maar was nog niet bevraagd**: `scan_stats.json` meldde 31 bevraagde prefixen. Dat gold ook voor zes nieuw toegevoegde batterijprefixen. De momentopname bewijst dus niet hoe vaak of zeldzaam Flocks eigen prefix voorkomt. We maken van ‘niet bevraagd’ geen ‘nul resultaten’.

De huidige repository bevat 39 prefixen na toevoeging van `E0:0A:F6` om aan te sluiten op de detectorfirmware. De bewaarde scansamenvatting bevat nog gegevens voor 31 prefixen. De nieuwe vermeldingen wachten dus op een volledige herberekening, ze zijn geen bewezen prefixen met nul resultaten.

______

## De dataset controleerde zichzelf

Alle historische auditcijfers hieronder zijn opnieuw gemaakt uit `data/flock_cameras.csv` in Flock Finder-commit [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829), met `csv` en `collections.Counter` uit de standaardbibliotheek van Python. Een nieuwe testrit was niet nodig. Namen, geografie en prefixsamenstelling spraken de kop al tegen. Cijfers over de gecorrigeerde implementatie komen uit de bewaarde samenvatting `scan_stats.json` in de huidige repository.

### Geografie was een vroeg waarschuwingssignaal

Van 146.526 rijen lagen er 75.818 in de Verenigde Staten, 70.674 daarbuiten en 34 zonder landwaarde. Duitsland had 13.491 records, gevolgd door Canada met 6.251, Frankrijk met 5.839, Groot-Brittannië met 4.836, Nederland met 4.636 en Zwitserland met 4.515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Gestapelde balk met 75.818 records uit de Verenigde Staten, 70.674 daarbuiten en 34 zonder landwaarde" caption="Het landenhistogram telt op tot 146.492 omdat 34 rijen een null-land hebben." >}}

Geografie is een selectiesignaal, geen bewijs. Flock omschrijft zijn netwerk als ‘landelijk’ en zegt klanten te verbinden in [49 Amerikaanse staten](https://www.flocksafety.com/flock-ecosystem). Internationale uitbreiding kan de marktgrens ook veranderen. Daarom markeren we records buiten de markt voor controle in plaats van ze te verwijderen of alle records buiten de VS onjuist te noemen.

De voorzichtige conclusie volstaat: bijna de helft van de records lag buiten de primaire Amerikaanse markt van het project. Zonder aanvullend signaal kon een wereldwijde OUI-hit niet even plausibel worden geacht.

### Meer dan 60.000 apparaten noemden zichzelf

| SSID-familie in de oorspronkelijke audit | Records | Aandeel | Wat de naam aanduidt |
|---|---:|---:|---|
| Bevat `ClickShare` | 50.278 | 34,3% | Draadloze Barco-presentatieapparatuur |
| `SMARTGATE_*` | 6.099 | 4,2% | Gateway- of OBD-achtige apparaatfamilie |
| `DIRECT-*` | 3.801 | 2,6% | WiFi Direct-apparaten zoals printers, tv’s en adapters |
| Exacte naam `AndroidAP` | 314 | 0,2% | Android-hotspots |
| Exacte naam `Audi HUD` | 138 | 0,1% | WiFi voor Audi-infotainment of head-updisplay |
| Exacte naam `MAX-PRINTER` | 133 | 0,1% | Kantoorprinters |
| `Flock ALPR [...]` | 30 | <0,1% | Oordeel van een andere detector opgeslagen als SSID |
| **Gecombineerde oorspronkelijke audit** | **60.793** | **41,5%** | Herkenbaar als andere apparatuur of detectoruitvoer |

Barco’s supportdocumentatie noemt de standaardnetwerknaam van een ClickShare-basiseenheid: [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). Dat is bevestiging uit de eerste hand van de productfamilie, zonder te gokken op basis van geografie of leveranciersregistratie.

De productieclassificator verving de exacte naamcontroles door reguliere expressies die geen onderscheid maken tussen hoofdletters en kleine letters. Hij omvat ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER en detectoruitvoerlabels. Op dezelfde 146.526 rijen vindt hij 629 AndroidAP-varianten, 139 Audi HUD-varianten en 134 MAX-PRINTER-varianten. De huidige repository meldt daarom **61.110 `identified_other`-records**, iets meer dan de 60.793 uit de oorspronkelijke audit.

### Het bevestigende signaal was slechts 2,4%

Slechts **3.502 rijen** hadden een echte SSID met een Flock-patroon. Nog eens 24.964 hadden geen SSID. De resterende records wezen op andere apparatuur of combineerden een OUI met een niet-geclassificeerde naam.

De 3.502 bevestigde rijen bevatten 161 echte SSID-varianten: 3.342 keer de eenvoudige naam `Flock`, 157 eenmalige provisioningnamen `Flock-XXXXXX` of `FLOCK-XXXXXX` en nog drie namen met `flock`. Een eerdere README-telling van 166 varianten bevatte vijf verschillende detectorannotaties `Flock ALPR [...]`. Die vijf zijn bewijs van de detector, niet van de camera.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="100%-gestapelde balk verdeelt 146.526 records in 3.502 bevestigd via SSID, 57.267 benoemd maar ongeclassificeerd, 24.964 alleen verborgen OUI, 60.763 geïdentificeerd als anders en 30 detectorfeedbackrecords" caption="De oude kop vatte vijf wezenlijk verschillende bewijsklassen samen in één telling." >}}

### De kwaliteit van prefixen verschilde sterk

Het fout-positiefpercentage was niet overal gelijk. Sommige prefixen behielden een bruikbaar Flock-signaal, andere bestonden vooral uit benoemde kantoor- of consumentenapparaten.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Horizontale gestapelde balken voor 31 OUI-prefixen: Flock-SSID’s groen, bekende andere SSID’s rood, verborgen SSID’s lichtgrijs en ongeclassificeerde records donkergrijs" caption="De grootste prefixen bevatten vaak de meeste bekende andere apparaten. Aantallen uit de auditmomentopname van 146.526 rijen." >}}

Vergelijk twee prefixen die de oude kaart hetzelfde label gaf:

- `70:C9:4E` had 495 rijen: 133 namen met een Flock-patroon en 29 bekende namen van andere apparaten.
- `74:4C:A1` had 11.872 rijen: 211 namen met een Flock-patroon en 8.385 bekende namen van andere apparaten.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Vergelijking: prefix 70 C9 4E met 26,9% Flock-SSID en 5,9% bekend anders, prefix 74 4C A1 met 1,8% Flock-SSID en 70,6% bekend anders" caption="Eén label verborg tegengestelde signaal-ruisverhoudingen." >}}

Hetzelfde patroon komt voor bij de grootste groepen: `F4:6A:DD` had 8.422 bekende andere namen tegenover 327 Flock-namen, `D0:39:57` had 8.270 tegenover 473, en `E0:4F:43` bevatte 6.238 bekende andere namen tegenover 66 Flock-namen. Het volume van een prefix bewees niets over de kwaliteit.

______

## De feedbacklus verborgen in 30 rijen

Dertig records uit Texas hadden SSID’s die duidelijk uitvoer van een andere detector waren:

| Detectorlabel opgeslagen als SSID | Vertrouwen van de tool | Records |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | laag | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | gemiddeld | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | laag | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | laag | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | laag | 1 |

De tool die 26 van de 30 records maakte, labelde ze met laag vertrouwen. Een WiGLE-upload sloeg het oordeel van de tool daarna op in het SSID-veld. Onze pijplijn vond het woord `Flock` en had het label als onafhankelijke bevestiging kunnen behandelen.

Dertig rijen zijn statistisch weinig. Het mechanisme is belangrijk: tools met een gedeelde crowdsourcedatabase kunnen elkaars uitvoer opnemen en een gok met laag vertrouwen omzetten in schijnbare bevestiging. De correctie blokkeert het hele patroon `Flock ALPR [` voordat de bevestigende subtekenreeks `flock` wordt gecontroleerd.

______

## Wat we verkeerd deden

De README-kop luidde **‘Camera’s in kaart | 146.526’**. De kaart publiceerde coördinaten met volledige precisie en gaf elk resultaat hetzelfde type markering. Een schema via GitHub Actions gaf een zwakke heuristiek de schijn van een onderhouden inventaris.

We hadden wel kanttekeningen. Elk item had `match_confidence: "suspected"`. De README noemde ClickShare als mogelijk meelifter en het project hield een apart kandidaatspoor voor SSID-vondsten bij. Die kanttekeningen bepaalden niet het aantal, de markering of het standaardbeeld dat lezers zagen.

In de tekst waren we voorzichtig, in de kop gaven we een getal. De kaart deed de bewering.

Het meest vermijdbare was dat onze [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)-firmware al identificatoren met hoog vertrouwen scheidde van die van contractfabrikanten en zwak bewijs onder de waarschuwingsdrempel scoorde. Het idee bestond binnen dezelfde organisatie, maar de kaartpijplijn nam het niet over.

We ontdekten de omvang van de fout met een histogram van onze eigen SSID-kolom. Dat duurde minuten. Elke dag committen we 146.526 bewijsregels die onze presentatie tegenspraken.

______

## Wat we hebben aangepast

De correctie staat in het gegevensmodel en de interface van Flock Finder:

- **Bewijs per record:** `ssid_confirmed`, `oui_high`, `oui_mfr` of `identified_other`.
- **OUI-niveaus:** prefixen zijn verdeeld in veldwaargenomen hoog vertrouwen en gedeelde niveaus voor contractfabrikanten.
- **Uitsluiting van bekende andere apparatuur:** ClickShare, SmartGate, WiFi Direct, Android-hotspots, Audi HUD, MAX-PRINTER en SSID’s van detectoruitvoer worden standaard uit kaart en kop geweerd.
- **Zichtbare onzekerheid:** markeerkleuren, pop-ups, tellingen en filters tonen de bewijsklasse.
- **Marktmarkering:** records buiten de primaire Amerikaanse markt krijgen `out_of_market: true` en blijven beschikbaar voor controle.
- **Uitgesplitste kop:** 3.502 bevestigd via SSID, 73.691 vermoed via OUI van hoog niveau, 8.223 vermoed via OUI van contractfabrikanten en 61.110 geïdentificeerd als anders.

Het gecorrigeerde, bruikbare aantal is **85.416** en bevat nog steeds 81.914 onbevestigde OUI-matches. Het is een verdedigbare telling van wat aan de huidige regels voldoet, geen geverifieerde camera-inventaris.

`identified_other` is ook een operationele classificator, geen alwetend oordeel. ClickShare heeft sterke primaire documentatie over zijn standaard-SSID, terwijl een breed patroon als `DIRECT-` een WiFi Direct-naamgevingsconventie beschrijft die veel productklassen gebruiken. Door de matchregel en het veld `blocked_reason` te publiceren, kunnen onderzoekers uitsluitingen controleren en aanpassen wanneer het bewijs verbetert.

### De langetermijnoplossing is firmwarefingerprinting

OUI-niveaus beperken de schade, maar maken een gedeeld fabrikantprefix niet productspecifiek. Een sterker pad is de geordende structuur van informatie-elementen in 802.11-probeverzoeken. Eerder werk documenteert deze TLV-signatuur:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

Die reeks beschrijft het gedrag van een bepaalde firmwarestack, niet het eigendom van een MAC-blok. Fingerprinting van probeverzoeken is een gevestigde techniek voor apparaatidentificatie. [Gepubliceerd onderzoek naar 802.11 MAC-layerfingerprinting](https://doi.org/10.1155/2017/6235484) laat zien dat informatie-elementen van probeverzoeken herkenbaar kunnen blijven wanneer MAC-adressen wisselen. Het gaat ook in op het concrete probleem uit [flock-you-issue #43](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` verschijnt op opeenvolgende lokaal beheerde MAC-adressen op 2,4 en 5 GHz.

De signatuur vereist nog onafhankelijke veldvalidatie op uiteenlopende hardware- en firmwareversies. Misvormde captures vragen om defensieve verwerking. Toch is dit de juiste richting. MAC-randomisatie maakt matchen op alleen OUI tot een aangekondigde doodlopende weg.

______

## Waarom dit buiten één repository belangrijk is

Mensen gebruiken toezichtskaarten om te beslissen waar ze rijden, parkeren, melden, onderzoeken en zich organiseren. Een foutieve markering leidt aandacht af. Tienduizenden kunnen nauwkeurige waarnemingen ernaast ongeloofwaardig maken.

Er is ook een geloofwaardigheidsasymmetrie. Een leverancier of criticus heeft maar één aantoonbaar foutieve ClickShare-markering nodig om de hele dataset aan te vechten. Wij leverden er 50.278. Journalisten en belangenorganisaties kunnen een eenvoudige kop sneller herhalen dan een latere correctie kan volgen.

Open-sourcetransparantie verdient vertrouwen met controleerbare methoden en zichtbare onzekerheid. De ruwe data hielpen onze fout blootleggen, maar toegang tot ruwe data rechtvaardigde geen interface die de conclusie overdreef. De correctie hoort op elke plek waar lezers de claim tegenkomen: veld, filter, markering, legenda en kop.

### Een verzoek aan alle Flock- en ALPR-kaarten

Andere Flock- en ALPR-kaartprojecten moeten hun datasets ook controleren. Dit is een uitnodiging om methoden te vergelijken, geen beschuldiging dat elke kaart onze fout heeft overgenomen.

[WiGLE](https://www.wigle.net/stats/) is de breedste openbaar toegankelijke, wereldwijd doorzoekbare WiFi-waarnemingsdataset die we kennen. Dat bereik maakte Flock Finder aantrekkelijk: één API kon een in het veld onderzochte signatuurlijst omzetten in een wereldkaart. Het maakte de fout ook meetbaar groot. Een wereldwijde database retourneert elk ongerelateerd product dat hetzelfde adresbereik van een radiotoeleverancier deelt, niet alleen het product dat aanleiding gaf tot de zoekopdracht.

Andere kaarten gebruiken ander bewijs. Sommige vertrouwen op foto’s en waarnemingen van vrijwilligers. Andere importeren bewakingstags uit OpenStreetMap, openbare documenten, leveranciersmeldingen of gegevens van een ander communityproject. Hun totalen zijn niet rechtstreeks vergelijkbaar met onze WiGLE-resultaten, en onze 2,4% SSID-bevestiging mag niet worden toegepast op veldgeverifieerde data. Het gezamenlijke risico is dat de classificatie van het ene project in de brondata van een ander belandt en daarna als onafhankelijke bevestiging verschijnt.

Elke openbare kaart moet een korte audit kunnen beantwoorden:

1. **Wat betekent één markering?** Een gefotografeerd apparaat, overheidsrecord, OUI-match, gebruikersmelding of import van een andere kaart?
2. **Hoeveel records hebben direct productbewijs?** Publiceer tellingen per bewijsklasse in plaats van één totaal aantal camera’s.
3. **Welke bronnen zijn onafhankelijk?** Volg de herkomst van imports zodat één waarneming niet als meerdere bevestigingen telt.
4. **Wat spreekt de classificatie tegen?** Maak frequentietabellen van SSID’s, leveranciers, landen, bijdragerslabels en andere categorische velden.
5. **Hoe worden onzekerheid en geschillen weergegeven?** Toon vertrouwen en correctiestatus bij markeringen, filters, exports en koppen.
6. **Kan een andere onderzoeker de telling reproduceren?** Publiceer de query, bronmomentopname, classificatieregels en datum.

Deze audit maakt het Flock-probleem niet kleiner. Een ALPR-cameranetwerk kan nog steeds verplaatsingen vastleggen, zoekopdrachten tussen jurisdicties ondersteunen en mensen raken die nooit met de verzameling instemden. Nauwkeurige tellingen maken kritiek moeilijker af te wijzen. Als we toezichtsystemen bekritiseren, moeten onze kaarten onderscheiden wat we zagen, afleidden en bevestigden.

We maakten een goed geïnformeerde fout. De prefixen kwamen uit legitiem veldonderzoek, de pijplijn was reproduceerbaar en de kanttekeningen waren echt. De gevolgtrekking ging toch verder dan het bewijs. Goede bedoelingen en goede invoer ontslaan ons niet van de plicht om systeemuitvoer op schaal te testen.

______

## Reproduceer de audit

Check commit `5551829` uit en voer het volgende uit vanuit de repository-root. Het gebruikt alleen de standaardbibliotheek van Python en toont het totaal, de geografie, veelvoorkomende SSID’s en geselecteerde families van benoemde apparaten.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("rijen", len(rows))
print("VS", countries["US"])
print("buiten de VS", sum(countries.values()) - countries["US"] - countries[""])
print("land ontbreekt", countries[""])
print("meest voorkomende SSID’s", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Gebruik voor de exacte historische invoer de CSV uit die commit, niet een huidige gegenereerde dataset. Na de audit stopte het project met het vastleggen van de grote CSV, GeoJSON en bestanden per OUI, omdat elke scan honderden megabytes herschreef en de repository sterk deed groeien. De huidige gegenereerde data worden hersteld en gepubliceerd via de doorlopende release [`data-latest`](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest). De kleine samenvatting `scan_stats.json` blijft in Git. Een ontbrekend gegenereerd bestand in de huidige branch betekent dus niet dat historische gegevens zijn verwijderd of dat het aantal nul is.

______

## De les

**Een heuristiek die in metadata als ‘verdacht’ staat maar op de kaart als zekere markering verschijnt, is een claim.** De aanduiding hoort in het datamodel en de visualisatie, niet alleen in de documentatie.

