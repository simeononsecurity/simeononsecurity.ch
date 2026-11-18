---
title: "Cursa detectării camerelor Flock: ce s-a schimbat în 2026"
date: 2026-09-10
lastmod: 2026-11-14
toc: true
draft: false
description: "Analiză a schimbărilor raportate în detectarea Flock Safety, a reacțiilor comunității și a metodelor în infraroșu pentru identificarea sistemelor de camere."
genre: ["Tehnologie de confidențialitate", "Contraveghere", "Proiecte open-source", "Drepturi digitale", "Securitatea rețelelor", "Cercetare în securitate", "Modificare hardware", "Instrumente de confidențialitate"]
tags: ["Flock Safety", "ALPR", "Flock-You", "Detectare OUI", "Solicitare probe wildcard", "Mod WiFi promiscuu", "Monitorizare 802.11", "DeFlockJoplin", "NitekryDPaul", "Detectare BLE", "WiFi 5GHz", "MAC administrată local", "Potrivire tipare SSID", "Hardware de contraveghere", "STS Collective", "colonelpanichacks", "Evitarea detectării", "ESP32", "Detectare WiFi", "Conștientizarea supravegherii", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "Urmărirea problemelor GitHub", "Actualizare firmware", "Anti-fingerprinting", "Randomizare MAC", "Amprentarea elementelor de informație", "Salt între canale", "Susținerea confidențialității", "Securitate open-source", "Supraveghere în masă", "Firmware de detectare", "Cartografiere WiFi din mers", "Îndepărtarea camerelor", "Hardware de confidențialitate", "Detectare în infraroșu", "Iluminator IR", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Detectare optică", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Scenă urbană cu o cameră Flock pe un stâlp și un vehicul echipat cu un dispozitiv avansat de detectare. Semnalele luminoase ilustrează comunicația wireless pe un fundal întunecat."
coverCaption: "Cum schimbările de hardware Flock Safety continuă să strice instrumentele de detectare open-source și cum recuperează comunitatea decalajul"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Dacă detectorul tău Flock-You a amuțit pe un traseu unde înainte găsea camere de fiecare dată, nu ți se pare și probabil nici hardware-ul nu s-a stricat.** În ultimul an, hardware-ul și firmware-ul camerelor Flock Safety s-au schimbat de cel puțin două ori în moduri care au defectat metodele comunității. De fiecare dată, cercetătorii open-source au fost nevoiți să facă reverse engineering pentru un nou semn distinctiv.

*Situația se schimbă rapid. Metoda de detectare și lista OUI de mai jos reflectă proiectului `colonelpanichacks/flock-you`, ramura `main` din septembrie 2026. Verifică [depozitul GitHub](https://github.com/colonelpanichacks/flock-you) înainte să presupui că dispozitivul tău este defect.*

{{< youtube id="cVf-id71BuQ" >}}

*Videoclipul de mai sus, de la Valleytech Custom Solutions, documentează exact simptomul explicat în acest articol: o cursă obișnuită de wardriving returnează brusc zero detectări, cu mai multe versiuni de firmware. Camerele fuseseră detectate în mod fiabil pe traseu, deși în același comitat fuseseră îndepărtate fizic de pe stâlpi mai multe camere semnalate anterior.*

______

## O cursă de wardriving care nu mai găsește nimic

Tiparul apare la fel în aproape toate relatările. Un șofer parcurge un traseu pe care l-a făcut de zeci de ori. Detectorul său, cu firmware-ul actual, a găsit înainte aceleași camere. Apoi, într-o zi, nu mai găsește nimic. Niciun semnal sonor, nicio înregistrare în jurnal, cu fiecare versiune de firmware personalizat încercată.

Videoclipul Valleytech descrie exact situația: traseul zilnic spre poștă detecta mereu cel puțin o cameră Flock, apoi nu a mai detectat niciuna. Pe un al doilea traseu, pe lângă Micro Center, detectorul semnala înainte cinci camere, iar acum doar una mai este activă. Celelalte patru au fost smulse fizic de pe stâlpi.

**Două lucruri se petreceau în același timp și se confundă ușor:**

- **În unele zone, camerele sunt îndepărtate sau mutate fizic**, ceea ce reduce într-adevăr numărul dispozitivelor detectabile.
- **S-a schimbat semnătura wireless transmisă de camere**, astfel încât o cameră rămasă pe stâlp nu mai declanșează hardware de detectare cu firmware învechit.

Două probleme GitHub din depozitul `colonelpanichacks/flock-you`, înregistrate la câteva luni distanță, documentează detaliat a doua situație. Citite în ordine, ele arată cum comunitatea a trebuit să evolueze de două ori metoda de detectare.

______

## Problema #20: punctul de acces de administrare s-a oprit

Deschisă în ianuarie 2026, **[problema #20](https://github.com/colonelpanichacks/flock-you/issues/20)** a început cu o reclamație cunoscută: cineva și-a testat dispozitivul lângă o cameră Flock semnalată pe DeFlock, dar nu a detectat nimic. În săptămânile următoare, mai mulți utilizatori au raportat același rezultat, din Florida, Indiana, Atlanta și Midwest, cu hardware și antene diferite.

Un comentator a pus întrebarea esențială: **schimbase Flock ceva de partea sa, într-un mod care a stricat detectarea tuturor cam în același timp?**

Administratorul proiectului, colonelpanichacks, a confirmat în cele din urmă. **În jurul lunii decembrie 2025, Flock a dezactivat punctul de acces de administrare pe care îl emiteau camerele sale.** Acel AP era baza originală a detectării wireless. După dispariția lui, comunitatea a trecut la semnale Bluetooth Low Energy (BLE) ca înlocuitor. Nici această soluție nu a mai funcționat fiabil până în primăvara lui 2026.

| Suprafață de detectare | Stare |
|---|---|
| **AP WiFi de administrare** | Dezactivat de Flock, aproximativ în decembrie 2025 |
| **Emisie de balize BLE** | A încetat să funcționeze fiabil în primăvara lui 2026 |
| **Legătură celulară LTE** | Încă folosită pentru încărcare în cloud, dar nu poate fi detectată pasiv |
| **Solicitări probe wildcard 802.11** | Baza actuală a detectării (vezi mai jos) |

*Fiecare firmware personalizat bazat pe vechile metode AP sau BLE caută acum un semnal pe care camerele nu-l mai transmit. De aceea un dispozitiv care funcționa devine complet tăcut fără ca hardware-ul să aibă vreo problemă.*

______

## Metoda nouă: probe wildcard și amprentarea cadrelor

Firmware-ul actual `flock-you` rulează în mod promiscuu 802.11 dedicat. Radioul nu transmite niciodată și nu se conectează la nicio rețea. Doar ascultă, schimbând canalele WiFi 11, 6 și 1 la intervale de 250 de milisecunde pentru a ține pasul cu schimbările de canal ale camerelor.

**Pentru ca firmware-ul să emită acum o alertă, toate condițiile de mai jos trebuie să coincidă:**

1. Cadrul este o **solicitare probe de administrare** 802.11 (tip 0, subtip 4).
2. **Elementul de informație SSID este prezent și are lungimea 0**, adică este o probă wildcard, nu una care cere o rețea anume.
3. Adresa emițătorului (**addr2**) corespunde unuia dintre prefixele OUI cunoscute ale Flock.
4. Restul elementelor de informație din cadru corespund tiparului de amprentă documentat de comunitatea DeFlockJoplin, bazat pe cercetarea din 2022 a lui Pintor și Atzori despre **[amprentarea IE a solicitărilor probe WiFi](https://ieeexplore.ieee.org/document/10001618)**.

În firmware, metoda se numește `wifi_wildcard_probe_ie_sig`. Testele în teren ale comunității DeFlockJoplin au detectat **11 din 12 camere cunoscute, cu doar 2 rezultate fals pozitive** pe traseul testat. Acesta este același reper verificat în teren și citat în **[ghidul hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** al proiectului. OUI-ul celei de-a douăsprezecea camere a fost adăugat ulterior în lista de mai jos.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Diagramă cronologică a evoluției metodei de detectare a camerelor Flock: de la punctul de acces WiFi de administrare, prin balize Bluetooth Low Energy, până la solicitările probe wildcard și amprenta elementelor de informație folosite acum. A patra etapă arată noile metode de evitare prin SSID, 5GHz și adrese MAC." >}}

______

## Lista OUI actuală

Amprenta probe wildcard de mai sus se activează numai după ce adresa MAC a emițătorului corespunde unuia dintre prefixele OUI confirmate de comunitate pe hardware Flock real. Lista este întreținută în principal de cercetătorul **@NitekryDPaul**. Comunitatea **DeFlockJoplin** a contribuit a 31-a intrare după ce a detectat o cameră ratată de lista inițială de 30.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**Lista nu este statică.** Cercetarea upstream menționează mai multe prefixe testate și apoi retrogradate: unul aparținea unui player media Sony, iar altul era un substituent timpuriu care nu a corespuns niciodată cu ceva. Două intrări sunt marcate cu încredere scăzută. Prefixul `82:6b:f2` este păstrat intenționat, deși este o adresă administrată local, deoarece eliminarea lui ar fi omis fără urmă o detectare reală confirmată de DeFlockJoplin.

**O intrare are acum confirmare hardware independentă de la o cameră aflată în serviciul municipal.** Unitatea Flock ale cărei imagini de sistem de fișiere au fost publicate în septembrie 2026 avea adresa MAC **`f4:6a:dd:57:46:fb`**, iar `f4:6a:dd` este poziția 13 din listă. Nu era un dispozitiv de laborator sau o mostră cumpărată. Era montată pe un stâlp în Wauwatosa, Wisconsin, și fotografia traficul. Aceasta este cea mai puternică confirmare individuală primită de vreun prefix de aici.

*Dacă întreții propriul fork de firmware, preia lista OUI din directorul upstream `datasets/` în loc să copiezi lista hardcodată. Lista se modifică odată cu cercetarea, iar o copie învechită te face să ratezi camere în mod lent și tăcut.*

______

## Clasificarea semnalelor de detectare

Potrivirea OUI este metoda pe care se bazează cel mai mult firmware-ul actual și tot ea este cel mai slab dintre cele cinci semnale disponibile. Comunitatea de detectare de la **[WiFi Mothership](https://wifimothership.com/flock)** le ordonează după nivelul de încredere, folosind cercetarea de firmware GainSec.

| Încredere | Semnal | Note |
|------------|--------|-------|
| **RIDICATĂ** | **ID producător BLE `0x09C8`** (XUNTONG) | Cea mai puternică amprentă digitală. Apare la unitățile Raven și la orice Falcon sau Sparrow cu modul de baterie atașat |
| **RIDICATĂ** | **UUID-uri de serviciu BLE Raven `0x3100` până la `0x3500`** | Servicii GATT specifice Raven pentru GPS, alimentare, rețea, încărcare și erori. Se activează doar pe hardware Raven |
| **MEDIE** | **Tipar SSID WiFi `^Flock-[A-Z0-9]+$`** | Numele implicit al hotspotului de configurare. Alte SSID-uri găsite în firmware includ `FS Ext Battery`, `Penguin` și `Pigvision` |
| **MEDIE** | **Subșir din numele dispozitivului BLE** | Nume precum `FS Ext Battery` apar în pachetele de publicitate și nu necesită parsarea datelor producătorului |
| **SCĂZUTĂ** | **Potrivirea adresei MAC și a prefixului OUI** | **Metoda cu cel mai mult zgomot.** Prefixele furnizorilor de componente se găsesc în mii de produse fără legătură |

*Rândul de jos este semnalul de care depinde cel mai mult firmware-ul actual. Aceasta este problema centrală a detectării bazate mai întâi pe OUI.*

### De ce lista OUI este atât de zgomotoasă

Cele 31 de prefixe din lista de mai sus nu sunt 31 de identificatori Flock. WiFi Mothership urmărește un set paralel de **26 de prefixe și clasifică proprietarul real al fiecăruia**, ceea ce arată alcătuirea listei.

| Categorie | Număr | Proprietar |
|-------|-------|-------|
| **Flock Safety** | **1** | `B4:1E:52`, alocare IEEE pentru companie |
| **Module de baterie** | 10 | Componente Silicon Labs din pachete de baterii extinse |
| **Module de cameră** | 11 | Module de cameră WiFi Liteon Technology |
| **Infrastructură de calcul** | 4 | Raspberry Pi Foundation și Raspberry Pi Trading |

**Douăzeci și cinci din cele 26 de prefixe aparțin furnizorilor de componente**, iar piesele lor se livrează în volume uriașe în produse fără legătură. Un prefix de baterie Silicon Labs sau de modul de cameră Liteon apare în produse care nu au nicio legătură cu Flock Safety. Plăcile Raspberry Pi sunt peste tot.

**O potrivire cu oricare dintre ele este un indiciu, nu o identificare.** De aceea amprenta probe wildcard are atât de multă greutate în firmware-ul actual. Asocierea unei potriviri OUI cu o solicitare probe cu SSID gol ridică nivelul de încredere de la o presupunere la 62 pe scara proiectului.

*Doar `B4:1E:52` răspunde singur la întrebarea „este un dispozitiv Flock?”. Tratează celelalte 30 de prefixe drept dovezi auxiliare.*

### Câte camere expun un hotspot

Datele de wardriving oferă un prag inferior pentru populație. WiFi Mothership a numărat **cel puțin 900 de puncte de acces Flock pe WiGLE în 2025**. Un AP Flock înseamnă un dispozitiv care transmite SSID-ul implicit de hotspot `Flock-XXXX`.

Cifra descrie dispozitivele care expun un hotspot de configurare, nu numărul total instalat. Flock susține că are zeci de mii de instalări, iar majoritatea camerelor nu transmit nimic ce ar înregistra un wardriver aflat în trecere. **Harta este un eșantion și unul mic.**

______

## Problema #43: tipar SSID nou, 5GHz și antifingerprinting MAC

La trei luni după închiderea problemei #20, a apărut un al doilea raport care descrie ceea ce pare o contramăsură deliberată împotriva detectării, nu o schimbare accidentală de firmware. **[Problema #43](https://github.com/colonelpanichacks/flock-you/issues/43)**, depusă în mai 2026, se bazează pe date de wardriving WiGLE culese lângă o cameră deja confirmată pe DeFlock. Documentează trei constatări ignorate de instrumentele existente.

### Constatarea 1: alt format SSID

SSID-ul documentat pentru hotspotul Flock urma mereu tiparul `Flock-XXXXXX`. Camera din acest raport transmitea în schimb **`Flock Camera net.`**, o convenție de nume complet diferită. Cine căuta pe WiGLE wildcard-ul `Flock-*`, așa cum făceau mai mulți cercetători, nu ar fi găsit niciun rezultat pentru această cameră, deși aceasta transmitea activ.

### Constatarea 2: hotspot confirmat de 5GHz

Aceeași cameră transmitea simultan pe **canalul 1 de 2,4GHz** și **canalul 157 de 5GHz**, cu adrese MAC consecutive pe fiecare bandă (`...9f:a2:de` și `...9f:a2:df`). Acest fapt indică un singur modul WiFi dual-band care alocă adrese adiacente fiecărui radio, nu două dispozitive fără legătură. Un raport separat și independent al cercetătorului nsm_barii înregistrase deja o solicitare probe Flock pe canalul 149 de 5GHz. Există acum două puncte de date care confirmă funcționarea pe 5GHz, nu o configurare greșită izolată.

**Toate metodele de detectare descrise anterior în articol, inclusiv firmware-ul actual cu probe wildcard, ascultă doar pe 2,4GHz.** O cameră care transmite exclusiv sau în principal pe 5GHz este invizibilă pentru acel hardware, indiferent cât de corectă este lista OUI.

### Constatarea 3: adrese MAC administrate local pe hotspot

Ambele adrese MAC capturate au **bitul de administrare locală activat**, adică nu provin din blocul OUI real al Flock înregistrat la IEEE. Logica standard de detectare `flock-you` omite intenționat adresele administrate local, fiindcă aceasta este metoda obișnuită de a filtra telefoanele și laptopurile care randomizează MAC-ul.

**Filtrul creat special pentru reducerea alarmelor false elimină și o cameră Flock care folosește o adresă MAC administrată local pe interfața hotspotului.** Octeții finali consecutivi ai celor două adrese capturate exclud generarea aleatorie. Asta sugerează atribuirea structurată și intenționată a adreselor, nu o coincidență.

| Constatare | Ce funcționează în continuare |
|---|---|
| **Format SSID nou** (`Flock Camera net.`) | Potrivirea tiparului SSID funcționează dacă tiparul de căutare este extins |
| **Funcționare la 5GHz** | Nimic din firmware-ul WiFi actual, deoarece acesta scanează doar 2,4GHz |
| **MAC administrat local** | Potrivirea SSID, fiindcă nu depinde deloc de adresa MAC |

*Potrivirea SSID este singura metodă din tabel care funcționează indiferent de bandă sau de modul în care este atribuită adresa MAC. Acesta este argumentul practic pentru adăugarea unor tipare SSID mai largi în locul dependenței doar de OUI.*

______

## Evită Flock detectarea în mod intenționat?

Niciuna dintre cele două probleme GitHub nu dovedește intenția și trebuie să fim preciși. Autorul problemei #43 a ridicat întrebarea deschisă în loc să tragă o concluzie: se întâmplă asta la toate implementările Flock sau doar la o versiune de firmware și o cameră?

Dar privește împreună tiparul din ambele probleme. O suprafață de detectare dispare. Comunitatea găsește un înlocuitor. Punctele slabe ale înlocuitorului (scanare doar la 2,4GHz, potrivire OUI, filtrarea adreselor MAC administrate local) se aliniază cu proprietățile de care ar profita un SSID nou, un radio de 5GHz și o adresă MAC administrată local. **Poate fi o coincidență produsă de un ciclu obișnuit de actualizare a firmware-ului sau poate un furnizor își restrânge amprenta wireless într-un mod care, intenționat ori nu, blochează detectarea terților.**

*Poziția cea mai utilă nu este să te cerți care explicație e corectă. Construiește detectarea fără să depindă permanent de o singură presupunere, fiindcă în cei doi ani de existență ai proiectului niciuna nu a rezistat.*

### Confirmare vizuală: alimentată, dar fără transmisie

**[Un al treilea clip Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) lămurește explicația „poate camera a fost îndepărtată”.**

{{< youtube id="sjI8FB0cLk0" >}}

Creatorul s-a întors noaptea la aceeași cameră din primul videoclip și a confirmat vizual că **LED-urile IR încă funcționau**, ceea ce înseamnă că unitatea era pornită și ilumina activ pentru captură nocturnă. În același timp, **fiecare firmware personalizat testat a înregistrat zero detectări legitime** pentru acea cameră. S-a declanșat o alertă, dar a fost confirmată ca fals pozitiv. Nimic de la cameră nu ajungea în partea wireless.

**Asta separă clar cele două explicații posibile.** O cameră smulsă sau mutată nu explică o unitate vizibil pornită, care iluminează noaptea. O cameră activă, iluminată și totuși tăcută pentru toate metodele WiFi indică dispariția semnăturii wireless, nu îndepărtarea hardware-ului.

Creatorul a mai relatat, după ce a discutat cu alți dezvoltatori care investigau aceeași problemă, că rezultatul nu era izolat. **Mai multe persoane au observat același tipar cam în același timp**, ceea ce sugerează o schimbare coordonată la nivel național din partea Flock, nu o problemă locală a unei camere. *Afirmația este anecdotică, bazată pe conversații informale, nu pe un set de date publicat. Totuși, se potrivește cu perioadele din decembrie 2025 și primăvara 2026 menționate în problema #20 și merită publicată într-o problemă GitHub nouă, nu lăsată într-un fir de comentarii.*

______

## Ce înseamnă asta pentru hardware-ul tău de detectare

Dacă dispozitivul a amuțit, parcurge această listă înainte să presupui că s-a stricat:

1. **Actualizează mai întâi firmware-ul.** Dacă rulezi ceva mai vechi decât ramura `main` actuală, probabil încă urmărești AP-ul de administrare dezactivat sau balizele BLE moarte. Descarcă firmware-ul actual și reflashează-l.
2. **Confirmă că acea cameră încă există.** Unele relatări cu zero detectări s-au dovedit a fi despre hardware smuls sau mutat, nu despre o defecțiune de detectare. Compară cu **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** sau **[DeFlock](https://deflock.org/)** înainte să depanezi dispozitivul.
3. **Încetinește la intersecții.** Pauza de 250ms pe canal înseamnă că o trecere rapidă te poate duce dincolo de fereastra camerei înainte ca radioul să ajungă pe canalul potrivit. O oprire de 30–60 de secunde detectează mult mai multe camere decât o trecere în viteză cu o antenă mai mare.
4. **Raportează ce observi.** Un rezultat de zero detectări lângă o cameră verificată vizual este exact tipul de date care a dus la problemele #20 și #43. Deschide o problemă nouă în loc să presupui că altcineva a raportat deja.
5. **Cunoaște limitele actuale.** Firmware-ul exclusiv WiFi, limitat la 2,4GHz, nu va vedea o cameră mutată pe 5GHz sau care a amuțit pe benzile scanate. Este o limitare reală acum, nu un defect al versiunii tale.

**Nimic din toate acestea nu face hardware-ul inutil.** Lista OUI și amprenta probe wildcard încă detectează astăzi marea majoritate a camerelor instalate. Înseamnă să tratezi orice detector, construit acasă sau cumpărat, drept o fotografie de moment a unei curse în desfășurare, nu o soluție permanentă.

{{< stscollective-ad "flockyou" >}}

______

## Abordare paralelă: detectarea blițului infraroșu în locul semnalului WiFi

Detectarea wireless nu este singurul front al acestei curse. **[Un videoclip de continuare](https://www.youtube.com/shorts/mzpr6bslsYA) al aceluiași creator, Valleytech Custom Solutions, descrie o abordare complet diferită**: în loc să asculți un semnal radio, urmărești iluminatorul infraroșu al camerei.

{{< youtube id="mzpr6bslsYA" >}}

Majoritatea camerelor ALPR, inclusiv cele Flock, folosesc **iluminare infraroșie pentru a captura noaptea plăcuțe lizibile**, același motiv pentru care camerele obișnuite de securitate funcționează pe întuneric. Lumina IR nu este vizibilă pentru ochiul uman, dar poate fi văzută de un senzor de imagine fără filtru de tăiere în infraroșu. *Acest singur detaliu hardware, lipsa filtrului IR, transformă un modul de cameră obișnuit într-un detector Flock.*

### Cum arată prototipul

Abordarea din videoclip a trecut prin mai multe versiuni până a ajuns la o combinație viabilă:

- **Prima încercare**: receptoare dedicate cu fotodiodă IR. Funcționau tehnic, dar piesele erau prea scumpe pentru o opțiune DIY practică.
- **A doua încercare**: un **Jetson Nano asociat cu un modul de cameră Raspberry Pi**. A demonstrat că ideea funcționează, însă costul hardware-ului și consumul de energie îl făceau nepractic pentru o construcție portabilă sau montată în vehicul.
- **Configurația actuală**: un **modul de cameră bazat pe ESP32, fără lentilă de tăiere IR**. Creatorul a testat un **ESP32-CAM** și un **M5Stack S3 Cam**, apoi a ales **Seeed Studio XIAO ESP32S3 Sense**, asociat cu un **modul GNSS Seeed XIAO bazat pe cipul Quectel L76K** pentru etichetarea GPS a detectărilor, folosind același tipar GPS de wardriving ca tabloul de bord `flock-you` bazat pe WiFi.

| Cerință | De ce contează |
|---|---|
| **Modul de cameră fără filtru de tăiere IR** | Filtrul care face culorile fotografiilor obișnuite să pară corecte blochează exact lumina necesară metodei |
| **Cameră în loc de fotodiodă** | Receptoarele cu fotodiodă capabile să izoleze semnalul erau prea scumpe pentru un proiect DIY practic |
| **Înregistrare GPS** | Asociază detectările cu o locație, la fel ca tabloul Flask al firmware-ului WiFi |

### Tiparul de clipire al camerei

Metoda presupune că iluminatorul clipește într-un tipar repetitiv detectabil, în loc să rămână aprins continuu. Creatorul a raportat o **măsurare proprie de aproximativ 20 de milisecunde aprins și 80 de milisecunde stins, o perioadă de 100 de milisecunde, adică un ciclu de funcționare de 20% la 10Hz** și a precizat că valoarea nu este verificată și poate fi greșită. *Folosește numărul drept punct de pornire pentru propria măsurare, nu drept specificație confirmată. Flock nu l-a publicat, iar creatorul nu a pretins că este sigur.*

### Stadiul proiectului

**Este un prototip timpuriu, doar DIY, nu un produs finit.** Creatorul a descris software-ul drept „programat intuitiv cu ajutorul IA” și încă în lucru. Un buzzer pentru alerte sonore este planificat, dar încă nu a fost adăugat, iar o placă gata de utilizare echivalentă cu hardware-ul OUI-SPY nu există. Versiunea actuală încă cere ca **o persoană să confirme vizual** că o detectare semnalată este o cameră reală și nu o altă sursă de lumină IR. Prin urmare, este un instrument de triere, nu unul complet automatizat.

*Aceasta este o suprafață de detectare cu adevărat diferită de toate celelalte din articol. Nu depinde de WiFi, 2,4 sau 5GHz, potrivire OUI ori comportamentul adresei MAC, deci niciuna dintre tehnicile de evitare din problema #43 nu i se aplică. Are și limite proprii: linie vizuală directă, interferența luminii de zi și o ipoteză despre ciclul de funcționare care nu a fost confirmată independent.*

______

## Ce face comunitatea

Răspunsul la ambele probleme a urmat tiparul care a menținut proiectul util timp de doi ani: cineva raportează o lacună, altcineva contribuie cu o soluție, iar soluția este livrată ca actualizare în loc să rămână în așteptare.

- **Problema #20** s-a încheiat cu confirmarea cauzei principale și rescrierea firmware-ului în jurul semnăturii probe wildcard, pe baza cercetării în teren a comunității DeFlockJoplin.
- **Problema #43** este încă deschisă la momentul redactării, iar sugestia de potrivire a tiparelor SSID nu a fost implementată. *Dacă vrei să ajuți la remedierea lacunei, adăugarea lui `Flock Camera` ca tipar suplimentar de potrivire este o contribuție mică și bine delimitată pentru cine cunoaște logica firmware-ului.*
- Setul de date OUI de bază are versiuni și date în depozit. Intrările retrogradate și cele cu încredere scăzută sunt documentate, nu eliminate în tăcere, astfel încât oricine face un fork vede exact ce s-a schimbat și de ce.

*Acesta este avantajul practic al instrumentelor open-source față de o alternativă cu sursă închisă. Persoana care descoperă o lacună nu poate corecta un detector proprietar. Comunitatea acestui proiect a făcut-o deja de două ori.*

______

## Cealaltă reacție: preluarea hardware-ului

Detectarea wireless este o reacție la aceste camere. Un efort paralel a vizat hardware-ul în sine, iar în septembrie 2026 a produs cele mai detaliate dovezi publice despre funcționarea internă a unei camere Flock.

**Colectivul stegan0gram a îndepărtat o cameră de pe stâlp, i-a copiat stocarea internă și a publicat imaginile sistemului de fișiere prin Distributed Denial of Secrets.** Ei descriu munca direct:

> „De ce să le distrugem când le putem face reverse engineering și afla secretele celor care ne spionează? Am eliberat hardware-ul din teren, l-am dezarmat și am făcut reverse engineering camerelor și echipamentelor solare asociate.”

*Distincția contează. Distrugerea unei camere elimină o unitate. Reverse engineering-ul produce dovezi despre toate.*

### Ce a dezvăluit îndepărtarea

Setul de date publicat include o **partiție media de 18 GB**, o **imagine de sistem Android de 1,5 GB** și o **partiție de acreditări de 32 MB**, plus cheia recuperată pentru containerul media criptat. Din acestea, cercetătorii au stabilit versiunea sistemului de operare, versiunea kernelului, acreditările backend hardcodate și tokenurile de autentificare în text simplu stocate de cameră.

Aceste dovezi susțin acum cercetarea de securitate din **[Vulnerabilitățile camerelor Flock Safety: peste 50 de probleme găsite](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**, care se baza anterior pe dispozitive de laborator și unități cumpărate.

### Reacția la îndepărtare

Intervenția fizică are consecințe, iar situația este mixtă.

- **Mai multe persoane au fost arestate la nivel național** pentru presupusa manipulare sau sabotare a camerelor Flock.
- **Unele localități au anunțat că vor înceta să folosească camere Flock**, rezultatul dorit de opozanții camerelor.
- **Un departament de poliție a construit o carcasă Flock falsă, imprimată 3D**, pentru a atrage potențiali vandali și a genera arestări.

Noel Pichardo, fost polițist în Pawtucket, Rhode Island, a devenit critic al Flock după ce a contestat folosirea camerelor de către departamentul său. El argumentează direct împotriva sabotajului. I-a spus publicației WIRED că înțelege frustrarea, dar se teme că tactica se întoarce împotriva celor care o folosesc. „Cred că acest tip de vigilantism nu va face decât să consolideze convingerea poliției și a statului în ansamblu că instrumentul este necesar”, a spus el. „Cu cât statul continuă să ignore nemulțumirile cetățenilor care se opun acestui tip de supraveghere, cu atât se va întâmpla mai des.”

### Unde se încadrează detectarea

Demontarea nu schimbă problema de detectare tratată aici. Camera transmite în continuare în același fel, firmware-ul are nevoie de lista OUI și de semnătura probe, iar cele două întreruperi documentate rămân valabile.

Ce adaugă imaginea este **confirmarea identității hardware-ului**, inclusiv o intrare OUI verificată acum pe o unitate reală, și un memento despre ce fel de presiune schimbă instalările. **Camerele dispar de pe un traseu când consiliul local votează pentru încheierea contractului, nu când un detector amuțește.** Instrumentele wireless răspund la o întrebare personală despre împrejurimi. Lupta pentru politici publice răspunde la întrebarea mai largă, iar imaginea extrasă i-a oferit cele mai solide dovezi de până acum.

______

## Concluzie: detectarea este o țintă mobilă, nu un răspuns fix

Un detector tăcut pe un traseu unde înainte găsea camere nu dovedește că hardware-ul a cedat. Arată că semnătura wireless pe care trebuia să o recunoască s-a schimbat din nou, într-un tipar repetat deja de două ori într-un singur an. **AP-ul de administrare, balizele BLE și acum, posibil, presupunerile de 2,4GHz și OUI integrate în firmware-ul actual** au avut fiecare o durată de viață limitată.

**Soluția nu a fost niciodată renunțarea la detectarea wireless.** A fost păstrarea vizibilă și documentată a presupunerilor metodei, astfel încât să poată fi corectate la următoarea raportare precum problema #20 sau #43. Acesta este argumentul pentru firmware open-source în locul oricărei alternative închise: remedierea apare când comunitatea găsește lacuna, nu după programul furnizorului.

### Idei principale

- **Două suprafețe de detectare documentate au dispărut deja**: AP-ul WiFi de administrare (dezactivat în jurul lui decembrie 2025) și balizele BLE (nesigure până în primăvara lui 2026).
- **Metoda actuală combină solicitări probe wildcard cu potrivirea amprentei OUI și IE și a detectat în teren 11 din 12 camere**, dar funcționează doar pe WiFi și 2,4GHz.
- **Un raport în așteptare descrie un format SSID nou, un hotspot confirmat de 5GHz și adrese MAC administrate local** pe care metoda actuală, bazată pe OUI și limitată la 2,4GHz, nu le poate vedea.
- **Se conturează o abordare separată, non-wireless**: un modul de cameră ESP32 fără filtru de tăiere IR detectează iluminatorul infraroșu al camerei Flock. Ignoră complet WiFi-ul și nu este afectat de niciuna dintre tehnicile de evitare de mai sus.
- **Confirmarea vizuală susține lipsa semnalelor wireless**: o cameră vizibil pornită și iluminând noaptea a înregistrat în continuare zero detectări WiFi legitime, ceea ce exclude explicația „camera a fost îndepărtată” pentru acea unitate.
- **Zero detectări lângă o cameră cunoscută nu înseamnă automat că hardware-ul tău este defect.** Actualizează mai întâi firmware-ul, apoi confirmă că acea cameră este încă fizic acolo.
- **Acesta este un proiect open-source care continuă să livreze remedieri când comunitatea găsește lacune.** Citește problemele GitHub, nu doar README-ul, pentru starea actuală a detectării.

### Pașii următori

1. **Actualizează firmware-ul** la ramura `main` actuală înainte de orice depanare: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. Dacă nu ai făcut-o deja, **citește ghidul hardware complet**: **[Proiectul de detectare Flock-You: ghid de hardware de contraveghere](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Verifică zonele moarte suspecte** cu **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** înainte să presupui că dispozitivul tău a ratat ceva.
4. **Înțelege cu ce ai de-a face**: **[Supravegherea cu camere Flock Safety: răspândire, probleme de confidențialitate și strategii de protecție](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Asociază detectarea WiFi cu detectarea celulară** folosind **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)** pentru o imagine mai amplă a contravegherii, fiindcă niciuna dintre metodele acestui articol nu detectează simulatoare de stații de bază celulare.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Cumpără dispozitive FlockYou gata de utilizare, economisește 20%
{{< /centerbutton >}}

______

## Articole conexe

| Articol | Ce acoperă |
|---------|---------------|
| **[Proiectul de detectare Flock-You: ghid de hardware de contraveghere](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Ghidul tehnic complet al celor trei platforme hardware, configurarea firmware-ului și metodologia de detectare pe care se bazează acest articol |
| **[Flock Finder: cartografiază toate camerele Flock suspectate din apropiere](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Compară o zonă moartă suspectată cu peste 40.000 de locații de camere cartografiate înainte să depanezi dispozitivul |
| **[Camere Flock: instrument de siguranță publică sau mașină de supraveghere fără mandat?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Analiză independentă a ceea ce permite de fapt baza de date Flock și de ce întrebarea mandatului contează mai mult decât detectarea |
| **[Supravegherea cu camere Flock Safety: răspândire, probleme de confidențialitate și strategii de protecție](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Imagine completă privind amploarea implementărilor, cazurile de abuz documentate și resursele de organizare comunitară |
| **[Vulnerabilitățile camerelor Flock Safety: peste 50 de probleme găsite](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Cercetarea de securitate hardware și software a camerelor Flock, separată de problema detectării wireless din acest articol |
| **[Cum să instalezi Rayhunter: ghid complet](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detectează capturatoare IMSI și Stingray, echivalentul celular al lacunei de detectare WiFi descrise aici |

______

## Referințe

1. [Depozitul GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Problema GitHub #20 - Camerele Flock nu sunt detectate, dar alte dispozitive da](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [Problema GitHub #43 - Semnal de 5GHz? Filtrare OUI / adresă MAC nouă](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [Set de date pentru cercetarea OUI NitekryDPaul](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - Cercetare comunitară ALPR](https://deflockjoplin.today)
7. [Pintor, L. și Atzori, L. (2022) - Analiza solicitărilor probe Wi-Fi prin amprentarea elementelor de informație, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED și 404 Media - Hackerii au pătruns într-o cameră Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - Camerele Flock au multe vulnerabilități și acreditări hardcodate](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - Imagini ale sistemului de fișiere al unei camere Flock ALPR](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - Săptămâna aceasta în securitate: camerele Flock sunt vechi, patch-uri Microsoft, cercetătorii atacă SSH](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - Referință pentru detectarea și dispozitivele ALPR Flock Safety](https://wifimothership.com/flock)
13. [GainSec - Cercetări de firmware și recomandări de securitate](https://gainsec.com/)
8. [Vânătoarea probei ascunse - Comportamentul probe wildcard cu SSID ascuns](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
9. [DeFlock - Hartă colaborativă a camerelor ALPR](https://deflock.org/)
10. [Colonel Panic Tech - OUI-SPY și hardware de detectare](https://colonelpanic.tech)
11. [STS Collective - Dispozitive FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
12. [Se întâmplă ceva ciudat cu camerele Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
13. [Wardriving infraroșu pentru camerele Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
14. [Camerele Flock sunt pornite, dar nu transmit - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
15. [Recunoașterea automată a numerelor de înmatriculare - Wikipedia (iluminare infraroșie în sistemele ANPR/ALPR)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
16. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
17. [Modul GNSS L76K pentru Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)
