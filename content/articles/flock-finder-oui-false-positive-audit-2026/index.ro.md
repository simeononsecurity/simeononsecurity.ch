---
title: "Am cartografiat 146.526 de „camere Flock”. 50.278 erau sisteme ClickShare"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Un audit al Flock Finder identifică ClickShare și alte rezultate fals pozitive, explică dovezile și documentează schimbările."
genre: ["Cercetare în securitate", "Tehnologie pentru confidențialitate", "Proiecte open source", "Jurnalism de date", "Contraveghere"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Amprentare OUI", "WiGLE", "Rezultate fals pozitive", "Calitatea datelor", "Barco ClickShare", "Adresă MAC", "IEEE OUI", "Amprentarea elementelor informaționale", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Responsabilitate open source", "Cartografierea supravegherii", "WiFi", "Cerere de sondare", "Randomizarea MAC"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "O hartă urbană întunecată plină de marcaje roșii care se dovedesc a fi dispozitive WiFi de birou, în timp ce câteva marcaje verzi indică detectări mai solide"
coverCaption: "Auditul a 146.526 de înregistrări Flock Finder a arătat cum o observație utilă din teren a devenit o afirmație prea sigură pe hartă."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**Am plasat 146.526 de puncte pe o hartă a camerelor de supraveghere. Cel puțin 50.278 erau sisteme de prezentare Barco ClickShare. Echipamentele din sălile de conferințe reprezentau mai mult de o treime din ceea ce titlul nostru numea „camere cartografiate”.**

Acesta era proiectul nostru, conducta noastră de date și greșeala noastră. Flock Finder interoga zilnic WiGLE pentru prefixe MAC observate pe camere Flock Safety, publica rezultatele cu coordonate de precizie completă și le afișa cu marcaje identice. Metadatele conțineau cuvântul `suspected`, iar documentația menționa rezultatele fals pozitive. Harta și titlul transmiteau totuși certitudine.

**Rezultatul pentru cititor:** reproduce auditul, separă observația de atribuire și afișează nivelul de încredere lângă marcaj și titlu. O potrivire de prefix este un indiciu pentru investigație, nu dovada unei camere.

Când am creat în sfârșit o histogramă de frecvență pentru coloana SSID, setul de date a explicat problema în câteva minute. ClickShare era doar categoria cea mai mare. Alte 6.099 de înregistrări se numeau `SMARTGATE_*`, 3.801 începeau cu prefixul generic WiFi Direct `DIRECT-`, 314 aveau numele exact `AndroidAP`, 138 indicau `Audi HUD`, 133, `MAX-PRINTER`, iar 30 includeau șirul de verdict al altui detector. În total, **60.793 de rânduri, adică 41,5%, respectau regulile cunoscute de denumire pentru alte dispozitive din auditul inițial.**

Acum Flock Finder publică o clasă de dovezi pentru fiecare înregistrare, exclude implicit echipamentele cunoscute ca fiind altele din hartă și titlu, oferă filtre, marchează înregistrările din afara pieței principale și separă prefixele de înaltă încredere de cele ale producătorilor contractuali. Articolul documentează greșeala, dovezile și limitele rămase.

______

## Cum funcționează detectarea ALPR comunitară

Detectoarele Flock construite de comunitate combină de obicei trei tipuri de dovezi wireless:

1. **Prefixe WiFi MAC/OUI.** Primii octeți ai unei adrese MAC administrate global pot identifica organizația căreia i-a fost atribuit blocul de adrese.
2. **Comportamentul WiFi.** Un SSID, o cerere de sondare wildcard, adresa receptorului, modelul canalelor sau o secvență de elemente informaționale 802.11 pot restrânge clasa dispozitivului.
3. **Dovezi Bluetooth.** ID-urile producătorului și UUID-urile serviciilor pot identifica radiourile expuse de un produs sau de o generație de firmware.

Potrivirea OUI a devenit comună deoarece este ieftină și pasivă. Un ESP32 accesibil poate inspecta cadrele 802.11 din apropiere fără a se conecta la o rețea. O bază istorică precum [WiGLE](https://wigle.net/) permite și căutarea observațiilor trecute fără instalarea propriilor scanere.

Metoda a urmat o genealogie comunitară: cartografierea și organizarea locală [DeFlock](https://deflock.org/), [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), fork-uri și proiecte conexe precum [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32), apoi [Flock Finder](https://github.com/simeononsecurity/flock-finder), care a aplicat lista de prefixe la date WiGLE la scară globală.

Munca inițială din teren merită recunoaștere clară. [@NitekryDPaul](https://github.com/NitekryDPaul) a observat 30 de prefixe pe echipamente Flock reale prin cercetare în modul promiscuu. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) a contribuit cu încă unul în timpul testelor din teren. Observațiile au fost legitime. Greșeala noastră ulterioară a fost tratarea **„observat pe o cameră Flock” ca și cum ar fi însemnat „exclusiv camerelor Flock”.**

______

## Defectul structural: un OUI descrie lanțul de aprovizionare

IEEE descrie un OUI ca pe un identificator de 24 de biți atribuit unui furnizor, producător sau altei organizații. Împreună cu alți 24 de biți aleși de destinatar, acesta formează o adresă MAC. Registrul este publicat de [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/).

Asta arată cine a primit blocul de adrese, nu neapărat ce marcă apare pe produsul finit. Producătorii contractuali construiesc module radio pentru mulți clienți. Același furnizor de cipuri poate apărea în camere, proiectoare, imprimante, vehicule și plăci pentru pasionați.

Atribuirile din registrul din spatele listei noastre făceau riscul vizibil:

| Registrant | Prefixe din lista auditată |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` și altele |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

Înregistrările Espressif ar fi trebuit să ne alerteze. Două prefixe dintr-o presupusă listă de camere aparțineau producătorului uneia dintre cele mai comune platforme WiFi încorporate din lume, inclusiv cipurile folosite de multe detectoare comunitare.

`B4:1E:52` este diferit deoarece este înregistrat direct la Flock Safety. Fusese adăugat la lista de 38 de prefixe în commitul auditat, **dar încă nu fusese interogat**: `scan_stats.json` indica 31 de prefixe interogate. Același lucru era valabil pentru șase prefixe nou adăugate pentru baterii. Instantaneul nu dovedește dacă prefixul propriu Flock este comun sau rar. Nu vom transforma „neinterogat” în „zero rezultate”.

Depozitul curent conține 39 de prefixe după adăugarea `E0:0A:F6` pentru paritate cu firmware-ul detectorului. Rezumatul de scanare păstrat încă raportează date pentru 31 de prefixe. Prin urmare, intrările noi așteaptă o recalculare completă și nu sunt prefixe cu zero rezultate dovedit.

______

## Setul de date s-a auditat singur

Fiecare cifră istorică de audit de mai jos a fost regenerată din `data/flock_cameras.csv` la commitul Flock Finder [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829), folosind `csv` și `collections.Counter` din biblioteca standard Python. Nu a fost nevoie de un nou test rutier. Numele, geografia și compoziția prefixelor contraziceau deja titlul. Cifrele implementării corectate provin din rezumatul `scan_stats.json` păstrat în depozitul curent.

### Geografia a fost un avertisment timpuriu

Din 146.526 de rânduri, 75.818 erau în Statele Unite, 70.674 în afara lor, iar 34 nu aveau valoare pentru țară. Germania avea 13.491 de înregistrări, urmată de Canada cu 6.251, Franța cu 5.839, Marea Britanie cu 4.836, Țările de Jos cu 4.636 și Elveția cu 4.515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Diagramă cu bare stivuite: 75.818 de înregistrări din SUA, 70.674 din afara SUA și 34 fără valoare pentru țară" caption="Histograma țărilor însumează 146.492 deoarece 34 de rânduri au țara nulă." >}}

Geografia este un semnal de triere, nu o dovadă. Flock descrie rețeaua drept „națională” și spune că leagă clienți din [49 de state americane](https://www.flocksafety.com/flock-ecosystem). Extinderea internațională poate schimba și limitele pieței. Marcăm înregistrările din afara pieței pentru revizuire, în loc să le ștergem sau să declarăm false toate înregistrările din afara SUA.

Concluzia prudentă este suficientă: aproape jumătate din înregistrări se aflau în afara pieței principale din SUA a proiectului. Fără un alt semnal, o potrivire OUI globală nu putea fi considerată la fel de plauzibilă.

### Peste 60.000 de dispozitive și-au spus numele

| Familia SSID din auditul inițial | Înregistrări | Pondere | Ce indică numele |
|---|---:|---:|---|
| Conține `ClickShare` | 50.278 | 34,3% | Echipamente wireless de prezentare Barco |
| `SMARTGATE_*` | 6.099 | 4,2% | Familie de gateway-uri sau dispozitive de tip OBD |
| `DIRECT-*` | 3.801 | 2,6% | Dispozitive WiFi Direct precum imprimante, televizoare și adaptoare |
| Numele exact `AndroidAP` | 314 | 0,2% | Hotspoturi Android |
| Numele exact `Audi HUD` | 138 | 0,1% | WiFi pentru infotainment sau afișaj frontal Audi |
| Numele exact `MAX-PRINTER` | 133 | 0,1% | Imprimante de birou |
| `Flock ALPR [...]` | 30 | <0,1% | Verdictul altui detector stocat ca SSID |
| **Totalul auditului inițial** | **60.793** | **41,5%** | Identificabile ca alte echipamente sau ieșire de detector |

Documentația de asistență Barco spune că numele de rețea implicit al unei unități ClickShare Base este [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). Aceasta confirmă direct familia produsului, fără presupuneri bazate pe geografie sau registrul furnizorilor.

Clasificatorul de producție a înlocuit verificările exacte ale numelor cu expresii regulate insensibile la majuscule/minuscule. Include ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER și etichete de ieșire ale detectorului. În aceleași 146.526 de rânduri, detectează 629 de variante AndroidAP, 139 Audi HUD și 134 MAX-PRINTER. Așadar, depozitul curent raportează **61.110 înregistrări `identified_other`**, puțin peste cele 60.793 din auditul inițial.

### Semnalul de confirmare a fost doar 2,4%

Doar **3.502 de rânduri** aveau un SSID autentic cu tiparul Flock. Alte 24.964 nu aveau SSID. Restul indicau alte echipamente sau combinau un OUI cu un nume neclasificat.

Cele 3.502 de rânduri confirmate conțineau 161 de variante reale de SSID: 3.342 de apariții ale numelui simplu `Flock`, 157 de nume unice de configurare `Flock-XXXXXX` sau `FLOCK-XXXXXX` și alte trei nume care conțineau `flock`. Un număr anterior de 166 de variante din README includea cinci șiruri distincte de adnotare ale detectorului, `Flock ALPR [...]`. Acestea dovedesc detectorul, nu camera.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="Bară stivuită 100% care împarte 146.526 de înregistrări în 3.502 confirmate prin SSID, 57.267 numite dar neclasificate, 24.964 doar OUI ascuns, 60.763 identificate ca altele și 30 de înregistrări de feedback ale detectorului" caption="Titlul vechi a redus cinci clase de dovezi substanțial diferite la un singur număr." >}}

### Calitatea prefixelor varia mult

Rata rezultatelor fals pozitive nu era uniformă. Unele prefixe păstrau un semnal Flock util. Altele erau dominate de dispozitive de birou sau de consum cu nume.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Bare orizontale stivuite pentru 31 de prefixe OUI: SSID-uri Flock verzi, SSID-uri cunoscute ca alte dispozitive roșii, SSID-uri ascunse gri deschis și înregistrări neclasificate gri închis" caption="Prefixele cele mai mari conțineau adesea cele mai multe dispozitive cunoscute ca altele. Numerele provin din instantaneul de audit cu 146.526 de rânduri." >}}

Compară două prefixe pe care harta veche le eticheta la fel:

- `70:C9:4E` avea 495 de rânduri: 133 de nume cu tipar Flock și 29 de nume cunoscute ca alte dispozitive.
- `74:4C:A1` avea 11.872 de rânduri: 211 nume cu tipar Flock și 8.385 de nume cunoscute ca alte dispozitive.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Comparație: prefixul 70 C9 4E cu 26,9% SSID Flock și 5,9% cunoscute ca altele, prefixul 74 4C A1 cu 1,8% SSID Flock și 70,6% cunoscute ca altele" caption="O etichetă unică ascundea rapoarte semnal-zgomot opuse." >}}

Același tipar apare în cele mai mari grupuri: `F4:6A:DD` avea 8.422 de nume cunoscute ca altele față de 327 de nume Flock, `D0:39:57` avea 8.270 față de 473, iar `E0:4F:43` includea 6.238 de nume cunoscute ca altele față de 66 de nume Flock. Volumul unui prefix nu demonstra calitatea dovezilor.

______

## Bucla de feedback ascunsă în 30 de rânduri

Treizeci de înregistrări din Texas aveau SSID-uri care erau clar ieșirea altui detector:

| Eticheta detectorului stocată ca SSID | Încrederea indicată de instrument | Înregistrări |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | scăzută | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | medie | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | scăzută | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | scăzută | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | scăzută | 1 |

Instrumentul care le-a creat a marcat 26 din 30 cu încredere scăzută. O încărcare în WiGLE a salvat apoi verdictul instrumentului în câmpul SSID. Conducta noastră a găsit cuvântul `Flock` și ar fi putut trata eticheta ca o confirmare independentă.

Treizeci de rânduri reprezintă puțin statistic. Mecanismul contează: instrumentele care folosesc o bază de date participativă pot prelua rezultatele unele de la altele și pot transforma o presupunere cu încredere scăzută într-o coroborare aparentă. Corecția exclude întregul tipar `Flock ALPR [` înainte de a căuta subșirul de confirmare `flock`.

______

## Unde am greșit

Titlul README-ului spunea **„Camere cartografiate | 146.526”**. Harta publica coordonate cu precizie completă și desena fiecare rezultat cu același marcaj. Actualizările programate prin GitHub Actions făceau o euristică slabă să pară un inventar întreținut.

Am inclus rezerve. Fiecare element avea `match_confidence: "suspected"`. README-ul menționa ClickShare ca posibil dispozitiv prezent în apropiere, iar proiectul păstra o pistă separată pentru candidații găsiți prin SSID. Aceste rezerve nu influențau numărul, marcajul sau vizualizarea implicită pe care o vedeau cititorii.

În text ne-am exprimat cu rezerve, iar în titlu am dat un număr. Harta a făcut afirmația.

Partea cea mai ușor de evitat era că firmware-ul [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) separa deja identificatorii de înaltă încredere de cei ai producătorilor contractuali și evalua dovezile slabe sub pragul de alertă. Conceptul exista în aceeași organizație, dar conducta cartografică nu l-a preluat.

Am aflat amploarea erorii rulând o histogramă pe propria coloană SSID. A durat câteva minute. În fiecare zi publicam 146.526 de rânduri de dovezi împotriva propriei prezentări.

______

## Ce am schimbat

Corecția este implementată în modelul de date și interfața Flock Finder:

- **Dovezi per înregistrare:** `ssid_confirmed`, `oui_high`, `oui_mfr` sau `identified_other`.
- **Niveluri OUI:** prefixele sunt separate între încredere ridicată observată în teren și niveluri comune ale producătorilor contractuali.
- **Excluderea altor echipamente cunoscute:** ClickShare, SmartGate, WiFi Direct, hotspoturi Android, Audi HUD, MAX-PRINTER și SSID-uri generate de detectoare sunt excluse implicit din hartă și titlu.
- **Incertitudine vizibilă:** culorile marcajelor, ferestrele pop-up, numărătorile și filtrele indică clasa de dovezi.
- **Marcarea pieței:** înregistrările din afara pieței principale din SUA primesc `out_of_market: true` și rămân disponibile pentru revizuire.
- **Titlu detaliat:** 3.502 confirmate prin SSID, 73.691 suspecte pe baza OUI de nivel înalt, 8.223 suspecte pe baza OUI-urilor producătorilor contractuali și 61.110 identificate ca altele.

Numărul corectat util pentru acțiune este **85.416** și include încă 81.914 potriviri OUI neconfirmate. Este o evidență justificabilă a ceea ce a trecut de regulile actuale, nu un inventar verificat de camere.

`identified_other` este tot un clasificator operațional, nu un oracol. ClickShare are documentație primară solidă despre SSID-ul implicit, în timp ce un tipar larg precum `DIRECT-` descrie o convenție WiFi Direct utilizată de multe clase de produse. Publicarea regulii de potrivire și a câmpului `blocked_reason` le permite cercetătorilor să auditeze excluderile și să le revizuiască atunci când apar dovezi mai bune.

### Răspunsul pe termen lung este amprentarea firmware-ului

Gruparea OUI limitează daunele, dar nu transformă un prefix de producător partajat într-unul specific unui produs. O cale mai puternică este structura ordonată a elementelor informaționale din cererile de sondare 802.11. Lucrările din amonte documentează această semnătură TLV:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

Secvența descrie comportamentul unei anumite stive de firmware, nu proprietarul unui bloc MAC. Amprentarea cererilor de sondare este o tehnică consacrată de identificare a dispozitivelor. [Cercetarea publicată privind amprentarea la nivelul MAC 802.11](https://doi.org/10.1155/2017/6235484) arată că elementele informaționale ale cererilor pot rămâne identificabile când adresele MAC se schimbă. Tratează și problema specifică din [flock-you issue #43](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` apare pe adrese MAC locale secvențiale în benzile de 2,4 și 5 GHz.

Semnătura încă necesită validare independentă pe teren, pe diverse echipamente și versiuni firmware, iar capturile malformate cer analiză defensivă. Totuși, aceasta este direcția potrivită. Randomizarea MAC face ca potrivirea bazată doar pe OUI să ajungă la un impas previzibil.

______

## De ce contează dincolo de un singur depozit

Oamenii folosesc hărți de supraveghere pentru a decide unde să conducă, să parcheze, să raporteze, să cerceteze și să se organizeze. Un marcaj fals mută atenția. Zeci de mii de marcaje false pot discredita observațiile corecte din apropiere.

Există și o asimetrie a credibilității. Un furnizor sau un critic are nevoie de un singur marcaj ClickShare demonstrabil fals pentru a contesta întregul set de date. Noi am furnizat 50.278. Jurnaliștii și grupurile civice pot repeta un titlu clar mai repede decât poate ajunge o corecție ulterioară.

Transparența open source câștigă încredere prin metode verificabile și incertitudine vizibilă. Publicarea datelor brute ne-a ajutat să găsim eroarea, dar accesul la date nu justifică o interfață care exagerează concluzia. Corecția trebuie să apară oriunde întâlnește cititorul afirmația: câmp, filtru, marcaj, legendă și titlu.

### Un apel către toate hărțile Flock și ALPR

Și alte proiecte de cartografiere Flock și ALPR ar trebui să-și auditeze seturile de date. Este o invitație de a compara metode, nu o acuzație că toate hărțile au moștenit greșeala noastră.

[WiGLE](https://www.wigle.net/stats/) este cel mai amplu set public de observații WiFi cu căutare globală pe care îl cunoaștem. Această acoperire a făcut Flock Finder atractiv: un API putea transforma o listă de semnături cercetate pe teren într-o hartă globală. A făcut și eroarea suficient de mare pentru a fi măsurată. O bază globală returnează orice produs fără legătură care împarte spațiul de adrese al unui furnizor radio, nu doar produsul care a motivat căutarea.

Alte hărți folosesc dovezi diferite. Unele se bazează pe fotografii și observații voluntare din teren. Altele importă etichete de supraveghere OpenStreetMap, înregistrări publice, dezvăluiri ale furnizorilor sau date de la alt proiect comunitar. Totalurile lor nu se compară direct cu rezultatele noastre WiGLE, iar rata de 2,4% confirmată prin SSID nu trebuie extrapolată la date verificate pe teren. Riscul comun este ca o clasificare a unui proiect să ajungă în datele sursă ale altuia și să pară o coroborare independentă.

Fiecare hartă publică ar trebui să poată răspunde unui audit scurt:

1. **Ce înseamnă un marcaj?** Un dispozitiv fotografiat, un document guvernamental, o potrivire OUI, un raport de utilizator sau un import din altă hartă?
2. **Câte înregistrări au dovezi directe despre produs?** Publică numărul pe clase de dovezi, nu un singur total agregat de camere.
3. **Care surse sunt independente?** Urmărește proveniența importurilor pentru a nu număra aceeași observație drept mai multe confirmări.
4. **Ce contrazice clasificarea?** Generează tabele de frecvență pentru SSID-uri, furnizori, țări, etichete ale contribuitorilor și alte câmpuri categoriale.
5. **Cum sunt afișate incertitudinea și disputele?** Arată încrederea și starea corecției în marcaje, filtre, exporturi și titluri.
6. **Poate alt cercetător reproduce numărul?** Publică interogarea, instantaneul sursă, regulile de clasificare și data.

Acest audit nu micșorează problema Flock. O rețea de camere ALPR poate înregistra în continuare deplasările, sprijini căutări între jurisdicții și afecta persoane care nu au consimțit la colectare. Numerele exacte fac critica mai greu de respins. Dacă contestăm sistemele de supraveghere, hărțile noastre trebuie să distingă între ce am observat, ce am dedus și ce am confirmat.

Am făcut o greșeală deși aveam informații bune. Prefixele proveneau din cercetare legitimă pe teren, conducta era reproductibilă, iar rezervele erau reale. Totuși, inferența depășea dovezile. Intențiile bune și datele inițiale bune nu elimină obligația de a testa rezultatele unui sistem la scară.

______

## Reproduce auditul

Verifică commitul `5551829`, apoi rulează comenzile următoare din rădăcina depozitului. Folosesc doar biblioteca standard Python și afișează totalul, geografia, SSID-urile frecvente și familii selectate de dispozitive denumite.

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

print("rânduri", len(rows))
print("SUA", countries["US"])
print("în afara SUA", sum(countries.values()) - countries["US"] - countries[""])
print("țară lipsă", countries[""])
print("SSID-uri de top", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Pentru intrarea istorică exactă, folosește CSV-ul din acel commit, nu un set de date generat curent. După audit, proiectul a încetat să includă în Git CSV-ul mare, fișierul GeoJSON și fișierele pe OUI, deoarece fiecare scanare rescria sute de megabyți și mărise considerabil depozitul. Datele generate curente sunt restaurate și publicate în versiunea continuă [`data-latest`](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest), iar rezumatul mic `scan_stats.json` rămâne în Git. Lipsa unui fișier generat din ramura curentă nu înseamnă că dovezile istorice au fost șterse sau că numărul lor este zero.

______

## Lecția

**O euristică etichetată „suspectă” în metadate, dar afișată ca marcaj sigur pe hartă, este o afirmație.** Eticheta trebuie să existe în modelul de date și în vizualizare, nu doar în documentație.

