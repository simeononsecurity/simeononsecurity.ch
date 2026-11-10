---
title: "Welke AI-modellen draaien op een Raspberry Pi 4 of 5?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Gebruik gemeten resultaten van Raspberry Pi 4 en 5 om lokale taalmodellen te kiezen op basis van geheugen, snelheid en werklast, van kleine LFM2.5-modellen tot opties van 3B en groter."
genre: ["Raspberry Pi", "Kunstmatige intelligentie", "Zelf hosten"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "lokale AI", "kleine taalmodellen", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "modelkwantisatie", "edge-AI"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Twee Raspberry Pi-computers op een donker bureau met blauwe en amberkleurige illustraties van neurale netwerken erboven"
coverCaption: "Illustratie van lokale AI-modellen op Raspberry Pi-hardware."
---

Een Raspberry Pi kan lokaal een bruikbaar taalmodel uitvoeren, maar het model moet in het geheugen van het bord passen en binnen de responstijd blijven die je toepassing aankan. Een Raspberry Pi 4 met 2 GB is vooral geschikt voor modellen met minder dan ongeveer één miljard parameters. Een Raspberry Pi 5 met 8 GB kan compacte modellen van 1B–3B comfortabel uitvoeren en enkele grotere gekwantiseerde modellen laden, met flinke compromissen.

We hebben deze modellen zelf met Ollama getest op een **Pi 4B met 2 GB** en een **Pi 5 met 8 GB**, beide met microSD-opslag. De metingen achter de tabellen gebruikten dezelfde vijf korte assistentprompts, systeemprompt, vaste seed en uitvoerlimiet van 140 tokens. Voor elke test ontlaadden we andere modellen en maten we de koude laadtijd, tijd tot de eerste zichtbare token, totale antwoordtijd, uitvoersnelheid en piek van het resident geheugen. Dit waren eenmalige tests van een werklast met korte antwoorden. De resultaten zijn dus voorbeelden voor dimensionering, geen universele ranglijst van snelheid of antwoordkwaliteit. De [Cortex-A76-CPU en beschikbare geheugenconfiguraties van de Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) verschillen bovendien duidelijk van het [Cortex-A72-platform van de Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Welke modeltypen zijn geschikt?

| Modeltype | Voorbeelden uit de metingen | Praktisch gebruik |
|---|---|---|
| Kleine tekstmodellen, ongeveer 230M–600M parameters | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Korte lokale opdrachten, samenvattingen en vraagbeantwoording met beperkingen; beste startpunt voor een Pi 4 met 2 GB |
| Compacte tekstmodellen, ongeveer 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Meer ruimte voor genuanceerde instructies op een Pi 5 of Pi 4 met meer geheugen, met tragere antwoorden dan de kleinste modellen |
| Gekwantiseerde tekstmodellen van 3B–4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Capabelere kandidaten voor een Pi 5 met 8 GB als enkele seconden wachten per antwoord acceptabel is |
| Grotere schaarse of hybride modellen | LFM2.5 8B | Technisch uitvoerbaar op de geteste Pi 5 met 8 GB, maar met groot geheugengebruik en lange koude laadtijd |

Dit zijn resultaten voor **tekstgeneratie**. Ze zeggen niets over beeldgeneratie, spraakherkenning, visie of training. “Draait” betekent ook meer dan dat het modelbestand op een kaart past: de runtime, contextcache, het besturingssysteem en andere diensten hebben RAM nodig. Kwantisatie verkleint het gewichtsbestand, maar kan de antwoordkwaliteit verlagen, vooral bij extreme instellingen zoals 1-bit-gewichten.

### Wat onze cijfers meten

De benchmark stuurde korte feitelijke prompts, prompts over procedurele veiligheid, prompts met opgehaalde context, een weerprompt en een hulpvraag naar de chat-API van Ollama. Elk model kreeg dezelfde promptset en seed. Voor de tijdmeting ontlaadden we het model, zodat het volgende verzoek een koude laadbeurt omvatte. De gerapporteerde **wandkloktijd** is de volledige aanvraag; **tokens per seconde** beschrijft alleen de uitvoergeneratie. We registreerden ook de eerste *zichtbare* token, omdat een model eerst tijd kan besteden aan redeneren voordat het antwoord verschijnt.

Voor het geheugen namen we tijdens elk verzoek metingen van het beschikbare RAM en swapgeheugen van de Pi, naast het resident geheugen van Ollama en het inferentieproces. De waarden voor **RSS** zijn resident geheugen van het proces, niet de volledige geheugenvraag van de host. Bestandspagina's, het besturingssysteem, een browser of een andere lokale dienst kunnen een model dat op papier past toch laten swappen. De tabellen gebruiken de oorspronkelijke eenmalige test met vijf prompts. Later breidden we de testharnas uit met een nieuwsprompt en controles op antwoordregels. Die controles verduidelijken wat je moet beoordelen, maar maken van de eerdere tijden geen resultaten voor naleving met zes prompts.

Tokens per seconde en het aantal parameters zijn geen kwaliteitsscores. Een model kan snel tekst produceren en toch een gevraagde bron weglaten, een woordlimiet overschrijden of een onafgemaakte zin geven. We zouden modellen vergelijken met de prompts die we echt willen gebruiken en de antwoorden bekijken voordat we er een toepassing op laten steunen.

## Raspberry Pi 4: kies de kleinste modellen

De geteste Pi 4 met 2 GB had weinig geheugenruimte over. De kleinste LFM2.5-modellen voltooiden alle vijf prompts, net als `qwen2.5:0.5b`. Dit zijn logische keuzes voor korte offline antwoorden of een kleine lokale assistent.

| Model | Modelbestand | Gemeten uitvoersnelheid | Gemiddelde antwoordtijd | Waargenomen geheugen of resultaat |
|---|---:|---:|---:|---|
| LFM2.5-230M, geïmporteerde GGUF | 0.25 GB | 12.8 tokens/s | 7.2 s | Piek RSS 383 MB; 5/5 prompts |
| LFM2.5-350M, geïmporteerde GGUF | 0.38 GB | 8.6 tokens/s | 8.6 s | Piek RSS 516 MB; 5/5 prompts |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 prompts; rechtstreeks beschikbaar in Ollama |
| MiniCPM5-1B, geïmporteerde GGUF, redeneren uit | 0.69 GB | 5.9 tokens/s | 12.2 s | Piek RSS 883 MB; 5/5 prompts |
| MiniCPM5-1B, geïmporteerde GGUF, standaard redeneren | 0.69 GB | 5.7 tokens/s | 33.3 s | Slechts 1/5 prompts gaf een bruikbaar zichtbaar antwoord |
| `qwen3:0.6b`, standaard redeneren | 0.52 GB | 6.4 tokens/s | 40.4 s | Eén leeg antwoord; het bord startte opnieuw op |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, geen swap of herstart; traag maar stabiel |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | Veel swapping; bord startte tijdens de test opnieuw op |
| `qwen3.5:0.8b` | 1.04 GB | — | — | Voltooide niet; het bord startte opnieuw op |

De resultaten van de Pi 4 zijn extra gevoelig voor wat er verder op het systeem draait. Tijdens tests met grotere modellen zagen we herstarts, waaronder bij een `qwen3.5:0.8b`-test die nooit werd voltooid. Dat zegt iets over onze configuratie met 2 GB, niet dat elke Pi 4 of elk model van 1B opnieuw zal opstarten. Een Pi 4 met 4 GB of 8 GB heeft meer geheugen, maar de CPU maakt inferentie nog steeds trager dan op de geteste Pi 5. We hebben die geheugenvarianten van de Pi 4 niet rechtstreeks getest.

Een vroege Pi 4-test leek veel slechter dan de uiteindelijke metingen: ongeveer 625 MB aan tijdelijke GGUF-bestanden stond in een RAM-gekoppelde `/tmp`, waardoor slechts zo'n 500–600 MB vrij bleef en honderden megabytes naar swap gingen. Nadat we de bestanden naar permanente opslag verplaatsten, gaven de resultaten van de kleine modellen hierboven een bruikbaarder beeld van het inferentiegeheugen. Op een bord met 2 GB kan zelfs de *locatie van een download* een benchmark vertekenen.

**Aanbeveling:** De geïmporteerde LFM2.5-350M is onze standaardkeuze voor dit bord met 2 GB. Het model bleef stabiel op **516 MB RSS**, liet ongeveer **1 GB RAM beschikbaar** en slaagde voor **5/6** antwoordregelcontroles in de nalevingstest op de Pi 4. Bij herhaalde tests op de Pi 5 liet het wel bronvermeldingen weg. Toepassingen die bronvermelding vereisen, moeten dit controleren. Kies LFM2.5-230M als lage vertraging en geheugenruimte het belangrijkst zijn: het was sneller en kleiner, maar vervormde in één antwoord over medische context “misselijkheid of braken” tot “misselijkheid/ventilatorgebruik”. Door die inhoudelijke fout is het ondanks de hogere herhaalde score op mechanische naleving een minder goede standaardkeuze voor antwoorden over veiligheid of gezondheid. Kies `qwen2.5:0.5b` als je een model uit het [Ollama-register](https://ollama.com/library/qwen2.5/tags) nodig hebt, maar houd rekening met zwakkere naleving van instructies. `granite4:350m` bleef stabiel, maar was trager en gebruikte meer geheugen; MiniCPM5-1B is alleen haalbaar als de client redeneren uitschakelt. Vermijd Gemma 3 1B en Qwen3.5 0.8B op deze specifieke Pi-configuratie met 2 GB, omdat onze tests herstarts veroorzaakten.

## Raspberry Pi 5: meer keuze, met een snelheidscompromis

De Pi 5 met 8 GB verwerkte alle **25 modellen** in onze snelheids- en geheugentest. De tabel bevat elke run, ook modellen die we niet aanraden voor deze werklast met korte antwoorden. Een dolk geeft een geïmporteerde GGUF aan. “Think off” betekent dat deze instelling voor de snelheidsrun is gebruikt; de aparte nalevingstest gebruikte die instelling niet altijd.

| Model | Bestand GB | Uitvoer tok/s | Antwoord s | Piek RSS MB | Beoordeling voor korte antwoorden |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Laagste vertraging; 78% herhaalde naleving |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Overslaan: 1-bit-gewichten en 3/6 naleving in één test |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Snel, maar miste bronvermelding in 5/18 herhalingen |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Eenvoudig uit het register; 61% herhaalde naleving |
| `qwen3:0.6b`, redeneren uit | 0.52 | 23.0 | 4.3 | 1,069 | Voorwaardelijk: 4/6 in nalevingstest, redeneringsinstelling telt |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Experimenteel 1-bit-model; 6/6 in één run niet bevestigd |
| `minicpm5-1b` †, redeneren uit | 0.69 | 18.4 | 5.1 | 869 | Voorwaardelijk: standaard redeneren gaf lege antwoorden |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Past, maar trager en groter dan kleine LFM2.5 |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Beste totaalkeuze voor onze werklast; 89% herhaalde naleving |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Alternatief uit het register; 5/6 in nalevingstest |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Beste herhaalde naleving onder registermodellen: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6 in nalevingstest; Gemma 3 1B volgde regels beter |
| `qwen3.5:0.8b`, redeneren uit | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 met standaard redeneren; vermijden zonder controle daarover |
| `spark-x2.5-1.7b` †, redeneren uit | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 met standaard redeneren; vermijden zonder controle daarover |
| `qwen3:1.7b`, redeneren uit | 1.36 | 8.1 | 12.4 | 1,867 | Voorwaardelijk; meer geheugen en vertraging dan kleinere keuzes |
| `minicpm5-2b` †, redeneren uit | 1.56 | 7.7 | 10.9 | 1,787 | Voorwaardelijk; 5/6 in één run, extra opsommingstekens |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Proefmodel van 3B; 5/6 in één run |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Overslaan voor interactief gebruik: trage generatie |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Alternatief van 3B; geen nalevingstest gerapporteerd |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Past, maar antwoorden zijn trager dan bij kleinere alternatieven |
| `qwen3.5:2b`, redeneren uit | 2.74 | 5.0 | 16.1 | 3,627 | Veel geheugen en vertraging; geen nalevingstest gerapporteerd |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Overslaan voor snelle antwoorden; 14.3 s tot eerste token |
| `ling-3.0-tiny` †, redeneren uit | 4.82 | 9.9 | 19.4 | 5,071 | Groot geheugengebruik; 5/6 in één run met fout in onderbouwing |
| `lfm2.5:8b`, redeneren uit | 5.16 | 8.7 | 54.6 | 5,317 | Past krap; 34.4 s koude laadtijd en te lange antwoorden |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Overslaan: swapdruk naast andere Pi-diensten |

† Geïmporteerde GGUF. Antwoordtijden en geheugenwaarden komen uit de vijfpromptrun op de Pi 5; nalevingsscores komen uit aparte tests met zes prompts. Als er geen nalevingsscore staat, is niet aangetoond dat het model de antwoordregels volgt.

De kleine LFM2.5-modellen waren het snelst voor deze werklast met korte antwoorden. De 1.2B-versie is een praktische middenweg op de geteste Pi 5. Gemma 3 1B is een alternatief uit het register met betere herhaalde naleving van antwoordregels dan Qwen2.5 1.5B in onze latere tests. Een model van 3B kan de lagere snelheid waard zijn voor prompts die meer capaciteit vragen, maar alleen deze timings bewijzen niet welk model de beste antwoorden geeft.

De koude laadtijd en vertraging tot de eerste token beïnvloeden de ervaring. LFM2.5-230M laadde op de Pi 5 in ongeveer **0.21 seconden** en gaf binnen **0.37 seconden** een zichtbare token. Bij Qwen2.5 1.5B duurde laden **2.59 seconden** en kwam de eerste zichtbare token na **3.66 seconden**; bij Qwen2.5 3B waren dat respectievelijk **5.60** en **7.97 seconden**. Voor een losse vraag kunnen die vertragingen zwaarder wegen dan de uitvoersnelheid zodra de generatie begint. Bij een continu geladen model tellen ze minder, maar een model dat resident blijft, gebruikt ook tussen aanvragen geheugen.

Andere gemeten kandidaten laten zien waarom we niet alleen op het aantal parameters rangschikken. Met redeneren uit haalde `qwen3:0.6b` op de Pi 5 **23.0 tokens/s** bij **1,069 MB RSS**, terwijl de geïmporteerde MiniCPM5-1B **18.4 tokens/s** haalde bij **869 MB RSS**. `granite4:350m` vereiste een download van **0.71 GB** en genereerde **12.1 tokens/s**, ondanks de aanduiding 350M. Modelverpakking en architectuur veranderen de verhouding tussen naam, bestandsgrootte, geheugen en snelheid.

Als je client betrouwbaar `think: false` kan versturen, zijn Qwen3 0.6B en MiniCPM5-1B redelijke experimenten als je alternatieven voor LFM2.5 wilt. MiniCPM5-2B, Qwen3 1.7B en Spark-X2.5 1.7B draaiden ook op de Pi 5, maar geen daarvan bood een duidelijk voordeel in snelheid en geheugen tegenover onze eerste keuzes. De nalevingstest gebruikte standaard redeneren voor MiniCPM5-1B en Spark-X2.5; de lege antwoorden mogen niet worden gepresenteerd als resultaat van hun snelheidsruns met redeneren uit. Andersom bewijst een snelle timing met redeneren uit niet dat een bridge die deze vlag weglaat een bruikbaar antwoord krijgt.

Als eenvoudige installatie belangrijker is dan ruwe snelheid, zijn Gemma 3 1B en Llama 3.2 1B plausibele registermodellen voor de Pi 5 met 8 GB. Gemma 3 1B volgde de geteste antwoordregels in **15/18** herhaalde antwoorden. Llama 3.2 1B slaagde in één run voor **5/6**, dus die nalevingsschatting is minder zeker. Qwen2.5 1.5B laadde en antwoordde in onze timingrun sneller dan Gemma 3 1B, maar slaagde in de eenmalige nalevingstest slechts voor **4/6** antwoordregels. Kies op basis van de eis die voor jouw prompts telt.

Voor af en toe langere of moeilijkere tekstprompts zijn de gekwantiseerde Qwen2.5 3B en Llama 3.2 3B kandidaten met beheersbaar geheugengebruik op onze Pi 5 met 8 GB. We maten snelheid en geheugen; Qwen2.5 3B slaagde in één nalevingstest voor **5/6**. Voor Llama 3.2 3B publiceerden we geen vergelijkbare nalevingstest. Meer parameters zijn een reden om ze te *testen* voor taken waarop kleinere modellen tekortschieten, niet het bewijs dat ze die taken beter uitvoeren. Granite 4 Micro en Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny en Gemma 3n E2B pasten of laadden in onze Pi 5-tests, maar hadden minder aantrekkelijke vertraging, geheugenruimte of betrouwbaarheid van antwoorden voor deze toepassing met korte antwoorden.

De twee Bonsai-modellen tonen de prijs van extreme kwantisatie. Hun Q1_0-bestanden waren opvallend klein voor namen met 1.7B en 4B parameters, maar het 1.7B-model slaagde slechts voor **3/6** antwoordregelcontroles. Het 4B-model slaagde in één test met zes prompts, maar had **18.1 seconden** per antwoord nodig en heeft geen bevestiging met herhaalde naleving. We beschouwen beide als experimenten in plaats van standaardaanbevelingen, vooral wanneer antwoordkwaliteit telt.

De LFM2.5 8B-uitkomst vraagt om context: het hybride ontwerp gebruikt minder actieve parameters per token, waardoor de decodeersnelheid hoger lag dan bij de gemeten dichte modellen van 3B. Toch duurde koud laden vanaf microSD **34.4 seconden** en gebruikte het model meer dan **5.3 GB resident geheugen**. Het toont wat er past, maar is geen comfortabele standaardkeuze voor een Pi waarop ook andere diensten draaien. De gemeten `gemma3n:e2b` gebruikte eveneens ongeveer 5.3 GB resident geheugen en veroorzaakte swapping naast de andere diensten op de testhost.

De LFM2.5 8B-run gebruikte ook de volledige limiet van **140 tokens** in plaats van kort te antwoorden. De Gemma 3-run van 4B deed **14.3 seconden** over de eerste token en **30.3 seconden** over het volledige antwoord. Beide modellen kunnen op deze Pi 5 worden geladen, maar gedroegen zich in onze tests niet als een vlotte kleine assistent. Een klein model met een passend kort antwoord kan voor een radio- of opdrachtinterface beter werken dan een groter model met op papier een hogere decodeersnelheid.

## Geheugen, redeneren en modelindeling

Een bruikbare eerste schatting op basis van onze metingen is **de downloadgrootte van het model × 1.4** voor resident inferentiegeheugen. Dit is slechts een vuistregel: contextlengte, runtime-instellingen, modelarchitectuur en andere processen kunnen de behoefte veranderen. Controleer het beschikbare geheugen tijdens generatie, laad op een kleine host maar één model tegelijk en houd ruimte vrij voor het besturingssysteem. Een bord met 4 GB kan redelijkerwijs beginnen met kleine of compacte modellen, maar onze aanbevelingen voor 4 GB zijn extrapolaties en geen directe tests met 4 GB.

Een bestand van 0.73 GB voor LFM2.5-1.2B kwam bijvoorbeeld overeen met ongeveer **967 MB RSS** op de Pi 5, terwijl het bestand van 0.99 GB voor Qwen2.5 1.5B **1,361 MB RSS** bereikte. De regel werkt redelijk voor die modellen, maar vormt geen harde grens. Reken op meer dan het gemeten procesgeheugen als de Pi ook een interface, zoekindex, lokale bibliotheek of achtergrondservice draait. Houd swapgebruik bij tijdens een echt verzoek. Een model dat technisch laadt maar voortdurend swap gebruikt, past niet goed.

Sommige modellen genereren eerst intern een redeneringsblok voordat het zichtbare antwoord verschijnt. In onze tests duurde het bij `qwen3:0.6b` op de Pi 4 met 2 GB veel langer voordat tekst zichtbaar werd. MiniCPM5-1B gaf met de standaardinstelling voor redeneren maar één bruikbaar antwoord op vijf prompts, tegenover vijf van vijf met redeneren uit. Stel voor een korte antwoordlimiet `think: false` in bij een compatibel Ollama API-verzoek, of kies een model dat niet standaard redeneert. Deze instelling geldt voor ondersteunde modellen en clients; het is geen universele snelheidsknop.

Dit verschil is belangrijk omdat een tokenlimiet tokens kan omvatten die aan redeneren worden besteed, zelfs wanneer de gebruiker geen antwoord ziet. Op de Pi 4 duurde `qwen3:0.6b` met standaard redeneren gemiddeld **40.4 seconden per verzoek** en leverde één prompt een leeg zichtbaar antwoord op. MiniCPM5-1B deed gemiddeld **33.3 seconden** met de standaardinstelling tegenover **12.2 seconden** met redeneren uit. Ook bij de Pi 5-tests schakelden we redeneren uit voor Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 en Spark-X2.5 waar dat in onze gegevens staat. Vergelijk modellen met precies de redeneerinstelling die je client zal gebruiken.

### Controleer of het antwoord bruikbaar is

Voor onze werklast met een korte antwoordtermijn voor een mesh-assistent zijn de antwoordregels net zo belangrijk als de snelheid: maximaal **90 woorden**, hoogstens **drie opsommingstekens**, platte tekst, een afgeronde zin en gebruik van opgehaalde context met bronvermelding. De bridge verdeelt tekst in stukken van **180 tekens**. Een lang antwoord gebruikt meer zendtijd via de radio, zelfs als het model het snel heeft gegenereerd.

De latere testversie controleert op lege antwoorden, een promptspecifieke woordlimiet, te veel opsommingstekens, Markdown-tabellen of codeblokken, een onafgemaakte afsluiting, ontbrekende termen uit de aangeleverde context en een ontbrekende bronvermelding. Toen we antwoorden beoordeelden aan de hand van de systeemprompt van de uitgerolde assistent, overtraden kleine modellen deze regels geregeld. De ernstigste fouten waren **lege antwoorden** doordat redeneren de tokenlimiet gebruikte, gevolgd door antwoorden die de opgehaalde context negeerden of de bron niet noemden. Meer woorden of opsommingstekens leverden nog wel zichtbare tekst op, maar verspilden zendtijd. Dit zijn mechanische controles, geen vervanging voor het lezen van het antwoord: ze stellen geen feitelijke juistheid vast en beoordelen niet of veiligheidsadvies deugt.

#### Herhaalde nalevingsresultaten op de Pi 5

Eerst voerden we zes prompts eenmaal per model uit met een limiet van **220 tokens** en de uitgerolde systeemprompt. Modellen die veelbelovend leken, testten we nog twee keer met een andere seed, wat **18 antwoorden per model** opleverde. Een perfecte eenmalige run garandeerde geen perfecte herhaling. De herhaalde resultaten hieronder geven een stevigere vergelijking voor de korte mesh-antwoorden die we testten:

| Model | Antwoorden die alle gecontroleerde regels volgden | Belangrijkste waargenomen fouten |
|---|---:|---|
| Geïmporteerde LFM2.5-1.2B | 16/18 (89%) | Twee onafgemaakte antwoorden |
| `gemma3:1b` | 15/18 (83%) | Drie onafgemaakte antwoorden |
| Geïmporteerde LFM2.5-230M | 14/18 (78%) | Onvolledige antwoorden en ontbrekende bronvermelding |
| Geïmporteerde LFM2.5-350M | 13/18 (72%) | Ontbrekende bronvermelding |
| `qwen2.5:0.5b` | 11/18 (61%) | Te veel opsommingstekens, te veel woorden, ontbrekende bronvermelding |

Op de **Pi 4 met 2 GB** vond de aparte nalevingstest met zes prompts **5/6** voor LFM2.5-350M, **4/6** voor LFM2.5-230M en **2/6** voor Qwen2.5-0.5B. MiniCPM5-1B verbeterde van **1/6** met standaard redeneren tot **5/6** met redeneren uit. Deze scores van de Pi 4 zijn eenmalige resultaten. Daarom wegen we de herhaalde Pi 5-resultaten zwaarder wanneer we gedrag bij het opvolgen van instructies bespreken, en gebruiken we de Pi 4-tests om stabiliteit en snelheid op dat bord te beoordelen.

De fouten hebben verschillende gevolgen. Een **leeg** antwoord helpt de gebruiker niet; een antwoord dat aangeleverd materiaal negeert, kan misleiden. Zonder bronvermelding kunnen lezers de herkomst niet controleren. Extra opsommingstekens of woorden gebruiken vooral meer pakketten van 180 tekens. Een onafgemaakte zin kan op afkapping wijzen. De fout van LFM2.5-230M met medische termen herinnert eraan dat een antwoord voor deze mechanische controles kan slagen en toch onjuist zijn. Geen van de vijf herhaald geteste modellen volgde alle regels in alle 18 antwoorden. Een toepassing die strikte lengte- of opmaakregels vereist, moet deze na generatie afdwingen en inhoud met grote gevolgen afzonderlijk beoordelen.

We controleerden ook het bridge-eindpunt zelf, Ollama's OpenAI-compatibele `/v1/chat/completions`, met opgehaalde WikiMed-context. Op de Pi 5 gaf LFM2.5-1.2B een antwoord van 28 woorden waarin zes aangeleverde termen werden gebruikt; Qwen2.5-0.5B gaf er een van 38 woorden met zeven termen. Beide pasten binnen twee pakketten van 180 tekens. Die eindpuntcontrole bevestigt dat het geïmporteerde LFM2.5-model via de aanvraagroute van de bridge werkt, maar één geslaagd antwoord garandeert geen betrouwbaarheid.

Ollama publiceert veel modellen die je meteen kunt ophalen, waaronder [Qwen2.5-varianten van 0.5B, 1.5B en 3B](https://ollama.com/library/qwen2.5/tags). We hebben de kleine LFM2.5-modellen uit [GGUF-releases van Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main) in Ollama geïmporteerd. Controleer de exacte tag of GGUF-bestandsnaam voordat je downloadt: modelregisters en repositories kunnen veranderen. Bewaar GGUF-downloads op permanente opslag. In onze tests gebruikte het tijdelijke RAM-bestandssysteem `/tmp` kostbaar geheugen op de Pi 4.

### Tags uit het register en GGUF-imports

Een Ollama-tag is de kortste route naar een eerste test: haal de exacte tag op en voer het model uit. De kleine LFM2.5-modellen in onze tabellen waren **GGUF-imports**, geen tags met de namen `lfm2.5-230m`, `lfm2.5-350m` of `lfm2.5-1.2b` in de openbare Ollama-bibliotheek. GGUF is een bestandsindeling voor modellen; namen zoals `Q8_0` en `Q4_K_M` geven kwantisatiekeuzes aan. De LFM2.5-bestanden van 230M en 350M die wij gebruikten waren Q8_0; het bestand van 1.2B was Q4_K_M. Daarom heeft dezelfde parameteromvang in een andere kwantisatie niet noodzakelijk dezelfde bestandsgrootte, hetzelfde geheugengebruik of dezelfde kwaliteit.

Importeer de geteste 350M-variant door de GGUF naar een map op permanente opslag te downloaden, een Modelfile te maken dat ernaar verwijst en Ollama het bestand naar de modelopslag te laten kopiëren:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

Voor de import is tijdelijk ruimte nodig voor zowel het gedownloade bestand als de kopie in Ollama. We gebruikten hervatbare downloads omdat lange GGUF-overdrachten soms halverwege werden onderbroken. Vergelijk vóór het importeren de SHA-256 van een gedownloade GGUF met de hash van het bestand die de bron publiceert. Een gedeeltelijke overdracht kan anders op een modelprobleem lijken. Op onze Pi-configuratie was `/tmp` gekoppeld aan RAM, dus GGUF daar opslaan verminderde het geheugen dat beschikbaar was voor inferentie.

## Een praktisch startpunt

| Hardware en doel | Eerste model om te proberen | Waarom |
|---|---|---|
| Pi 4 met 2 GB, standaardkeuze | Geïmporteerde LFM2.5-350M | Stabiel bij 516 MB RSS met ongeveer 1 GB beschikbaar; gekozen na een fout met medische termen in 230M |
| Pi 4 met 2 GB, laagste vertraging | Geïmporteerde LFM2.5-230M | 383 MB RSS en gemiddeld antwoord van 7.2 seconden; controleer de inhoud zorgvuldig, vooral bij gezondheids- of veiligheidsvragen |
| Pi 4 met 2 GB, alleen registermodellen | `qwen2.5:0.5b` | Rechtstreeks uit Ollama op te halen en stabiel in onze test met vijf prompts op de Pi 4; 61% herhaalde naleving op de Pi 5 |
| Pi 4 met 4 GB of Pi 5 | Geïmporteerde LFM2.5-1.2B en lokaal testen | 967 MB RSS en 89% herhaalde naleving op onze Pi 5 met 8 GB; varianten met 4 GB zijn niet rechtstreeks getest |
| Pi 5 met 8 GB, responsieve assistent | Geïmporteerde LFM2.5-1.2B | 15.5 tokens/s, antwoordtijd 4.7 seconden en de hoogste gemeten herhaalde naleving |
| Pi 5 met 8 GB, alleen modellen uit het register | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS en 83% herhaalde naleving |
| Pi 5 met 8 GB, groter tekstmodel proberen | Gekwantiseerde Qwen2.5 3B of Llama 3.2 3B | Beide draaiden rond 5 tokens/s en gebruikten 2.4–2.8 GB RSS; Qwen2.5 3B slaagde in één nalevingstest voor 5/6 |

Deze keuzes richten zich op korte, bruikbare antwoorden op een Pi waarop ook andere diensten kunnen draaien. Het zijn startpunten, geen claim dat één model voor elke taak het beste is. In onze eenmalige nalevingstest op de Pi 5 gaven `qwen3.5:0.8b` en Spark-X2.5 met standaard redeneren geen antwoorden die aan alle regels voldeden; MiniCPM5-1B haalde 1/6. Vermijd deze modellen voor korte antwoorden als de client redeneren niet kan uitschakelen. Test het uiteindelijke model met de echte prompt, contextlengte, gelijktijdigheid en antwoordlimiet die je voor implementatie plant.

Voer voor het registermodel na [Ollama voor Linux installeren](https://ollama.com/download/linux) uit:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Test met je eigen prompts, gewenste antwoordlengte en andere draaiende diensten. Noteer zowel de totale antwoordtijd als het geheugengebruik. Dat vertelt je meer over de geschiktheid van een model voor je Pi dan alleen het aantal parameters.

Houd bij een host met weinig geheugen swapgebruik tijdens tests in de gaten. Als een groter model het bord niet meer reageert, gebruik dan een kleiner model en stel een Ollama-geheugenlimiet in die bij dat model past, zodat een te grote laadbeurt mislukt voordat de host geen geheugen meer heeft. Een servicelimiet is een beveiliging, geen manier om een te groot model passend te maken. De herstarts van de Pi 4 tijdens onze tests laten zien waarom reactiesnelheid en geheugenruimte naast tokens per seconde meewegen bij de keuze.

## Zet de benchmark om in een implementatiebesluit

Schrijf vóór je een model dagelijks gaat gebruiken vier grenzen op: **maximale antwoordtijd, maximaal resident geheugen, antwoordindeling en gedrag bij fouten**. Test deze grenzen terwijl de diensten draaien die het bord gaan delen. Een model dat alleen slaagt maar naast je radiobridge of dashboard swap veroorzaakt, voldoet niet aan de implementatie-eis.

Houd één klein terugvalmodel geïnstalleerd. Schakel ernaar over wanneer het hoofdmodel de geheugenlimiet overschrijdt, een leeg antwoord geeft of de antwoordregels niet volgt. Noteer bij elke vergelijking de modeltag, kwantisatie, Ollama-versie, prompt, contextlengte en seed, zodat een latere modelupdate niet voor een hardwareverbetering wordt aangezien.
