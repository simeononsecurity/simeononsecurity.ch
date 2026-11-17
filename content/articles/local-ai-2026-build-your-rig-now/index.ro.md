---
title: "IA locală în 2026: un model 27B îl depășește pe Sonnet 4.6, iar fereastra de cumpărare a echipamentelor se închide"
date: 2026-09-22
lastmod: 2026-11-15
toc: true
draft: false
description: "Planifică un sistem local de IA pentru 2026 în funcție de mărimea modelului, VRAM, lățimea de bandă a memoriei, energie, cost și opțiuni de actualizare."
genre: ["IA locală", "IA găzduită local", "Modele cu sursă deschisă", "Echipamente pentru IA", "Învățare automată", "Cuantizare", "Laborator casnic", "Confidențialitate", "Economia IA", "Echipamente de consum"]
tags: ["IA locală", "rulare llm local", "qwen3.8", "qwen3.8 27b", "bonsai 2 27b", "ternary bonsai", "prism ml", "cuantizare ternară", "1,58 biți", "cuantizarea llm", "claude sonnet 4.6", "sonnet 4.6 față de model local", "ponderi deschise", "model moe", "amestec de experți", "ollama", "llama.cpp", "rtx 5090", "vram", "inferență locală", "prețuri gpu 2026", "deficit dram", "prețuri memorie", "construire sistem IA", "IA pentru laborator casnic", "cost abonament IA", "openrouter", "artificial analysis", "ghid de cumpărare gpu", "llm găzduit local", "IA care păstrează confidențialitatea", "echipamente IA 2026"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Spațiu de lucru modern cu o placă video și mai multe ecrane luminoase care afișează rezultate și vizualizări IA pe un fundal bleumarin închis."
coverCaption: ""
ref: ["/articles/ai-models-raspberry-pi-4-5", "/articles/building-a-privacy-preserving-meshtastic-ai-assistant"]
---

**Un model descărcabil, care încape pe o singură placă video de consum, depășește acum un model API de vârf în indicele agregat de inteligență.** Qwen3.8 27B este un model open-weight de viziune și limbaj lansat în august 2026. Reîmpachetarea sa ternară, Bonsai 2 27B, comprimă aceleași ponderi în 5.53 GiB. Împreună, arată momentul în care inferența locală a încetat să mai fie un compromis pentru pasionați și a devenit o alternativă reală la un API plătit.

*Fereastra pentru cumpărarea hardware-ului se închide rapid. Prețurile memoriei sunt cele mai rele din ultimele două decenii și scumpesc și plăcile video.*

Articolul prezintă rezultatele testelor, ce sunt cele două modele, unde pierde încă modelul deschis și de ce următoarele douăsprezece luni nu sunt un moment bun să aștepți.

**Ce vei obține:** alege un model și o capacitate de memorie potrivite sarcinii tale. Înainte să cumperi, compară costul hardware-ului și al energiei, dimensiunea contextului și debitul măsurat. Testele nu prezic calitatea pentru sarcinile tale sau prețul viitor al plăcii video.

## Răspunsul scurt

**Diferența de inteligență dintre un model local 27B și un API plătit apropiat de modelele de vârf s-a închis. Avantajele rămase ale modelului plătit sunt mai mici decât sugerează diferența de preț.**

Trei lucruri s-au schimbat simultan:

- **Modelele deschise 27B au ajuns la scoruri apropiate de cele de vârf.** Qwen3.8 27B obține 33.7 în Intelligence Index, față de 30.1 pentru Sonnet 4.6, în aceeași suită de evaluare.
- **Cuantizarea ternară a redus necesarul de memorie cu aproximativ două treimi.** Bonsai 2 27B rulează întregul model 27B în **5.53 GiB**, o capacitate disponibilă pe plăci de câteva sute de dolari.
- **Oferta de memorie s-a deteriorat.** Prețurile contractuale ale DRAM convenționale au crescut cu **90 până la 95 la sută** față de trimestrul anterior la începutul lui 2026, cea mai mare creștere trimestrială înregistrată de TrendForce. GPU-urile de generație următoare au fost amânate până în 2028.

*Să cumperi sau să construiești acum este opțiunea ieftină. Nu este un mesaj comercial, ci ceea ce arată datele de aprovizionare.*

## Privește testul cu un singur GPU

Afirmația de mai sus merită o demonstrație, nu doar un tabel. Bijan Bowen a testat Bonsai 2 27B pe o mașină cu un singur GPU și a întrebat dacă este cel mai bun model disponibil astăzi pentru o singură placă.

{{< youtube id="OA5cICIzD-c" enable="true" title="Primul test Bonsai 2 27B: este cel mai bun model IA pentru un singur GPU?" description="Prima analiză a modelului ternar Bonsai 2 27B rulat pe un GPU de consum, cu viteza, calitatea și alternativele prezentate." >}}

*Urmărește calitatea răspunsurilor, nu numărul de tokeni pe secundă. Viteza este partea ușor de îmbunătățit.*

## Două nume, un singur model

Cele două modele importante aici nu sunt concurente. **Sunt aceleași ponderi la două niveluri de precizie diferite.**

| | Qwen3.8 27B | Bonsai 2 27B ternar |
|---|---|---|
| **Ce este** | Modelul open-weight original de la Qwen | Reîmpachetare ternară a Qwen3.8-27B de către Prism ML |
| **Ponderi pe disc** | **18 GB** | **5.53 GiB** (PTQ1_0) sau **6.70 GiB** (PQ2_0) |
| **Parametri** | 27B dens | 26.90B, aceeași arhitectură |
| **Context** | 256K | 262,144 tokeni |
| **Viziune** | Da, nativă | Da, pachet separat de proiecție CLIP |
| **Apelarea instrumentelor** | Da | Da |
| **Licență** | Apache 2.0 | Apache 2.0 |
| **Mediu de execuție** | Ollama, llama.cpp, MLX | **Doar fork-ul llama.cpp al Prism ML** |

Pagina bibliotecii Ollama pentru `qwen3.8` indică modelul 27B la **18 GB**, cu context de 256K, suport vizual și apelarea instrumentelor, plus o compilare MLX separată pentru Apple Silicon. Versiunea ternară din Ollama oglindește pachetele GGUF Apache-2.0 ale Prism ML, republicate cu aceleași checksum-uri.

**Așadar, întrebarea practică nu este ce model să alegi.** Ci câtă memorie vrei să cheltuiești pentru aceeași inteligență. Versiunea ternară folosește aproximativ o treime din memorie și pierde puțin.

{{< figure src="local-ai-architecture-comparison.webp" alt="Diagramă care compară amprenta de memorie a aceluiași model 27B: 18 GB la precizie standard și 5.53 GiB cu ponderi ternare; ambele încape pe un singur GPU de consum" >}}

## Comparația testelor

Artificial Analysis evaluează ambele modele cu aceeași suită. Citește rezultatele rând cu rând, nu doar rezumatul, fiindcă modelele câștigă în domenii diferite.

| Test | Qwen3.8 27B | Claude Sonnet 4.6 | Lider |
|---|---|---|---|
| **Intelligence Index** | **33.7** | 30.1 | Deschis |
| **Coding Index** | **68.1** | 63.0 | Deschis |
| **Agentic Index** | **45.8** | 31.8 | Deschis |
| **GPQA Diamond** | **90.5%** | 87.5% | Deschis |
| **Humanity's Last Exam** | **33.9%** | 33.6% | Deschis |
| **AA-LCR (context lung)** | **82.0%** | 80.0% | Deschis |
| **GDPval-AA** | **45.4%** | 36.0% | Deschis |
| **CritPt (fizică de cercetare)** | **5.4%** | 3.1% | Deschis |
| **Rată fără halucinații** | **69.7%** | 51.6% | Deschis |
| **SciCode** | 46.6% | **50.1%** | Sonnet |
| **Precizie AA-Omniscience** | 15.6% | **40.9%** | Sonnet |

*Modelul deschis conduce în nouă din unsprezece rânduri comparabile, inclusiv la toți indicii agregați.*

### Unde conduce modelul deschis

Cei trei indici agregați rezumă rezultatul. **Inteligență 33.7 față de 30.1, programare 68.1 față de 63.0 și agenți 45.8 față de 31.8.** Diferența cea mai mare este la indicele agenților. Contează mai ales pentru cei care rulează fluxuri automatizate cu mai mulți pași, nu solicitări individuale.

Ca reper procentual, Artificial Analysis plasează Qwen3.8 27B **peste 86 la sută dintre modele** la indicele agenților și peste 76 la sută la programare. Sonnet 4.6 se află la 68, respectiv 72 la sută. La raționament științific de nivel postuniversitar, modelul deschis obține **90.5 la sută** la GPQA Diamond.

### Unde conduce încă Sonnet 4.6

Două rezultate favorizează cealaltă parte, și niciunul nu este minor.

**AA-Omniscience măsoară dacă un model răspunde corect de la prima încercare la întrebări de cunoștințe. Sonnet 4.6 obține 40.9 la sută, față de 15.6 la sută.** Este o diferență mare în fiabilitatea factuală și cel mai puternic argument individual pentru plata unui model de top.

Rândul privind evitarea halucinațiilor cere atenție. 69.7 la sută pentru Qwen față de 51.6 la sută pentru Sonnet pare o victorie clară, și este dacă îl privești izolat. Dar metrica descrie proporția răspunsurilor *incorecte* care nu inventează informații. Un model mai puțin precis produce mai multe răspunsuri greșite, deci procentele descriu grupuri diferite și nu se compară direct. **Citește mai întâi rândul preciziei.**

Sonnet câștigă și la SciCode, cu 50.1 la sută față de 46.6 la sută, și publică rezultate pentru două evaluări care nu apar în fișa modelului deschis: IFBench și Terminal-Bench Hard. Acestea nu se pot compara.

### Două rezerve oneste

**Datele lansării sunt la șase luni distanță.** Sonnet 4.6 a fost lansat în februarie 2026. Qwen3.8 27B a apărut în august 2026. Compararea unui model de vârf din februarie cu unul deschis din august nu este o competiție echivalentă.

**Sonnet 4.6 nu mai este modelul de vârf al Anthropic.** Sonnet 5 și Opus 5 se află acum deasupra lui în gamă. Modelul deschis 27B a ajuns din urmă un produs de vârf de la mijlocul lui 2026, nu cel mai bun model actual. A susține contrariul înseamnă să citești prea mult în tabel.

*Testele măsoară performanța în teste. Singurul scor care contează este cel al propriei tale sarcini.*

## Ce schimbă ponderile ternare

Bonsai 2 nu este un model mai mic. Este același model 26.90B la o precizie numerică mult mai mică, iar metadatele GGUF publicate arată clar compromisul.

| Proprietate | Valoare |
|---|---|
| **Arhitectură** | `qwen35`, atenție hibridă cu atenție completă la fiecare a patra strat și straturi state-space |
| **Parametri** | 26.90B |
| **Blocuri** | 64 |
| **Lățimea embeddingului** | 5120 |
| **Atenție** | 24 capete de interogare, 4 capete KV, lungime cheie/valoare 256 |
| **Context** | 262,144 tokeni, bază RoPE 1e7 |
| **Formatul ponderilor** | Ternar, grup de 128. PQ2_0 la 2.13 biți pe pondere, PTQ1_0 la 1.75 |
| **Turnul vizual** | CLIP, 460.73M parametri, distribuit într-un pachet separat de proiecție |
| **Licență** | Apache 2.0 |

**Ponderile ternare înseamnă că fiecare parametru are una dintre trei valori în loc de șaisprezece.** Aceasta este esența compresiei și motivul pentru care un model complet 27B încape în 5.53 GiB în loc de 18 GB.

### Debit măsurat

Măsurat cu `llama-bench` pe RTX 5090 de 32 GB, toate straturile transferate pe GPU, flash attention activată, media a trei rulări:

| Pachet | Ponderi | Prefill (pp512) | Decodare (tg128) |
|---|---|---|---|
| **PQ2_0** | 6.70 GiB | **3802.74 tok/s** | **135.41 tok/s** |
| **PTQ1_0** | 5.53 GiB | 1876.31 tok/s | 131.41 tok/s |

PQ2_0 face prefill **de 2.03 ori mai repede** decât PTQ1_0, în timp ce decodarea este egală statistic. De aceea PQ2_0 este alegerea implicită rezonabilă. PTQ1_0 este util când contează ultimii 1.2 GiB. Cu `llama-server` și context de 65K, decodarea s-a menținut la **136.5 tok/s** pentru o singură cerere transmisă continuu.

**Viteza de decodare este cifra pe care o simți zilnic.** 135 de tokeni pe secundă depășesc cu mult viteza de citire. Latența nu este motivul pentru inferență locală, fiindcă un API găzduit este suficient de rapid. Motivele sunt costul, confidențialitatea și controlul.

### Capcana despre care nu vorbește nimeni

**Ollama standard nu poate încărca aceste fișiere.** Nucleele ternare sunt în fork-ul llama.cpp al Prism ML. Verificarea pe Ollama 0.34.2 eșuează cu mesajul `unsupported tensor "output.weight" size overflows`. Runtime-ul recunoaște arhitectura `qwen35`, dar bibliotecile nu au `pq2_0` sau `ptq1_0` și nici runtime pentru activarea Hadamard.

Există o a doua capcană pe care trebuie s-o știi înainte să pierzi o seară. **Pachetul F16 al acestei familii pare o alternativă sigură, dar nu este.** Tenzorii sunt F16 și F32 obișnuiți, deci pachetul se parsează și se încarcă fără eroare, apoi decodifică text incoerent. Ponderile folosesc o bază rotită, declarată în metadatele `prism.hadamard.*`; runtime-ul trebuie să aplice rotația corespunzătoare, altfel rezultatul este fără sens. La 50.1 GiB, pachetul F16 nici nu încape integral pe o placă de 32 GB.

*Citește fișa modelului înainte de descărcare. O oglindă comunitară nu este o compilare acceptată, iar pagina spune asta clar.*

## Valul MoE din spatele acestei schimbări

Modelele dense 27B sunt doar jumătate din poveste. Modelele mixture-of-experts activează o mică parte din parametri pentru fiecare token, ceea ce schimbă din nou costurile.

| Tipul modelului | Total / activi | Context | Notă |
|---|---|---|---|
| **Qwen3.8 2.4T A95B** | 2.4T / 95B | 1.0M | Frate open-weight al Qwen3.8 Max |
| **Qwen3.6 35B A3B** | 35B / 3B | 262K | Apache 2.0, MoE rar hibrid |
| **Qwen3 Coder Next** | 80B / 3B | 256K | Ponderi deschise, creat pentru agenți de programare permanent activi |

**Qwen3 Coder Next este modelul de urmărit pentru lucru local.** Are 80B de parametri în total, dar activează numai 3B pentru fiecare token, fiind conceput pentru agenți mereu activi în medii CLI și IDE. Un model care activează 3B de parametri generează la viteza unui model 3B, dar folosește capacitatea stocată a unui model de 80B. Notele proiectului spun că performanța se compară cu modele care folosesc de 10 până la 20 de ori mai mult calcul activ.

*Modelul dens 27B este alegerea sigură astăzi. Modelele rare sunt locul în care curba eficienței încă se îmbunătățește.*

{{< figure src="local-ai-moe-dense-tradeoff.webp" alt="Grafic care compară un model dens 27B, ce activează toți parametrii pentru fiecare token, cu un model mixture-of-experts rar, ce activează numai 3 miliarde din 80 de miliarde de parametri" >}}

## Fereastra de cumpărare a echipamentelor se închide

Aceasta este partea poveștii cu termen limită.

Inferența locală s-a ieftinit exact când memoria de care depinde a început să se scumpească. Cele două tendințe se ciocnesc, iar efectul se vede deja în prețurile de vânzare.

### Ce s-a întâmplat cu prețurile memoriei

**Prețurile contractuale ale DRAM convenționale au crescut cu 90 până la 95 la sută față de trimestrul anterior în primul trimestru din 2026**, cea mai mare creștere trimestrială înregistrată de TrendForce. NAND flash a crescut cu 55 până la 60 la sută în aceeași perioadă.

Presiunea nu s-a redus. Datele TrendForce arată o nouă creștere a DRAM de **58 până la 63 la sută** și a NAND de 70 până la 75 la sută în trimestrul al doilea. Chiar și temperarea din trimestrul al treilea, DRAM în creștere cu 13 până la 18 la sută și NAND cu 10 până la 15 la sută, adaugă inflație peste două trimestre record, nu aduce o scădere.

Cauza este structurală, nu ciclică. Extinderea centrelor de date IA absoarbe memoria care deservea telefoane, laptopuri și console. Producătorii de memorie alocă mai întâi capacitatea comenzilor cu marjă mai mare. Analiștii care urmăresc oferta de module estimează că livrările de cipuri DRAM către producătorii de module vor scădea cu peste 70 la sută în 2027.

**Directorul general Intel a cuantificat problema.** La AI Infrastructure Summit din Santa Clara, pe 15 septembrie 2026, Lip-Bu Tan a spus că prețurile memoriei crescuseră deja „de cinci, șase și șapte ori” față de nivelurile anterioare. A avertizat că memoria reprezintă acum 70 până la 80 la sută din lista de materiale a unui laptop ieftin. A mai spus separat că nu va exista o ameliorare înainte de 2028.

*Relatarea independentă despre comparația pe suprafață dintre plachetele DRAM și plachetele logice de ultimă generație include o rezervă importantă. Prețurile spot nu sunt prețuri contractuale, iar achizițiile spot DDR5 sunt atât de mici încât comparația sugerează o tendință, nu o concluzie certă. Direcția generală este clară.*

{{< figure src="local-ai-memory-price-trend-2026.webp" alt="Grafic cu creșterile trimestriale ale prețurilor contractuale DRAM în 2026: salt de 90 până la 95 la sută în primul trimestru și temperare la 13 până la 18 la sută în al treilea" >}}

### Efectul asupra plăcilor video

Memoria reprezintă o parte importantă din costul componentelor unei plăci video, deci prețurile DRAM se transferă direct în prețul GPU-urilor.

| Placă | Începutul lui 2025 | Septembrie 2026 |
|---|---|---|
| **Nvidia RTX 5090** | $1,999 | **peste $5,000** |
| **Asus RTX 5080** | $1,199 | $1,595 |
| **AMD RX 9070 XT** | aproximativ $830 | **peste $1,037** |

Creșterile au venit în valuri coordonate pe parcursul lui 2026, nu ca salturi izolate. Nvidia a ridicat prețurile în ianuarie, din nou în mai la RTX 5090 și iar mai târziu în an. AMD a urmat în august cu o creștere de cel puțin 10 la sută pentru anumite plăci Radeon și kituri de memorie GDDR6, atribuită direct costurilor memoriei.

**Următoarea generație a fost amânată, nu lansată.** Seria RTX 60 de la Nvidia este acum așteptată în 2028, anul 2027 fiind eliminat complet din cauza disponibilității memoriei.

*Placa pe care o cumperi astăzi nu concurează cu una mai ieftină anul viitor. Concurează cu o versiune mai scumpă a ei însăși.*

## De ce așteptarea costă mai mult

Sfatul obișnuit despre hardware este să aștepți următoarea generație. Pe o piață cu ofertă limitată de memorie, acest sfat lucrează împotriva ta.

Trei puncte susțin argumentul.

**Prețurile au crescut deja și continuă să urce.** O majorare de 90 până la 95 la sută a prețului contractual DRAM într-un singur trimestru nu este o fluctuație care se inversează în trimestrul următor. TrendForce prevede creșteri suplimentare în al treilea trimestru, nu scăderi, iar CEO-ul Intel estimează că ameliorarea va veni în 2028.

**Nu există un produs din 2027 pentru care să aștepți.** Când GPU-urile de consum de generație următoare se amână până în 2028, strategia de așteptare durează doi ani. Este aproape întregul ciclu de actualizare hardware pierdut fără rezultat.

**Modelele sunt deja suficient de bune.** Asta s-a schimbat în 2026. Acum doi ani, hardware-ul local oferea o experiență vizibil compromisă. Astăzi, aceiași bani cumpără un model 27B la 135 de tokeni pe secundă, cu o fereastră de context 262K, care depășește un API de top în indicele agregat de inteligență.

*Dacă așteptai ca modelele locale să devină bune, nu mai trebuie să aștepți. Dacă aștepți hardware mai ieftin, datele de aprovizionare indică 2028.*

## Ce să construiești

Potrivirea hardware-ului cu modelele de mai sus este simplă, fiindcă ponderile ternare au redus cerințele.

| Nivel | Memorie | Ce rulează confortabil |
|---|---|---|
| **Începător** | 8 până la 12 GB VRAM | Ternar 27B de 5.53 până la 6.70 GiB, cu rezervă pentru context |
| **Practic** | 16 până la 24 GB VRAM | Qwen3.8 27B complet de 18 GB sau pachetul ternar cu context lung |
| **Confortabil** | 32 GB VRAM | Ternar 27B la întregul context 262K sau MoE 80B cu 3B activi |
| **Memorie unificată** | 64 până la 128 GB | Modele MoE rare mai mari pe Apple Silicon sau un desktop cu memorie unificată |

Câteva observații practice contează mai mult decât tabelul de niveluri:

- **Cumpără memorie, nu GPU-ul emblematic.** Pachetul ternar de 5.53 GiB face nivelul de bază cu adevărat utilizabil. La prețurile din 2026, investește diferența în RAM și stocare, nu într-o placă de top.
- **Sistemele cu memorie unificată oferă valoare.** O mașină cu cel puțin 64 GB de memorie partajată rulează modele rare mai mari la o fracțiune din costul unei plăci dedicate de aceeași capacitate.
- **Energia și răcirea contează.** Un sistem care face inferență ore întregi se comportă diferit de unul care rulează teste câteva minute.
- **Rulează pachetul ternar alături de un model mai mic.** Modelul 3B răspunde întrebărilor rapide, iar 27B se ocupă de cele dificile.

{{< centerbutton href="https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B" >}}
Descarcă Ternary Bonsai 2 27B
{{< /centerbutton >}}

## Când își mai justifică prețul modelele de top

Argumentul pentru gama de top este real, dar mai îngust decât sugerează marketingul.

**Răspunsul sincer este fiabilitatea factuală.** Precizia AA-Omniscience este 40.9 la sută pentru Sonnet 4.6 și 15.6 la sută pentru modelul deschis 27B. Când un răspuns greșit te costă un client, un diagnostic sau o poziție juridică, diferența de 25 de puncte contează mai mult decât orice indice agregat.

**Lanțurile lungi de agenți sunt al doilea răspuns.** Sonnet 4.6 raportează 53.0 la sută la Terminal-Bench Hard și 75.7 la sută la τ²-Bench Telecom, teste care măsoară utilizarea susținută a instrumentelor și comportamentul unui agent cu mai multe interacțiuni. Fișa modelului deschis nu raportează rezultate comparabile, iar absența lor nu încurajează.

**Al treilea răspuns ține de operare.** Un API găzduit nu cere actualizări de drivere, depanarea cuantizării, urmărirea unui fork llama.cpp sau corectarea bazei rotite a ponderilor. Altă echipă se ocupă de disponibilitate și primește alerta la trei dimineața.

### Întrebarea care merită pusă

Unde se justifică gama de top în afara companiilor mari?

**Încă se justifică pentru munca ce cere informații de încredere.** Cercetare, analiză juridică, întrebări medicale, modelare financiară și orice sarcină în care un răspuns sigur pe sine, dar greșit, este costisitor. Categoria este reală, iar diferența de precizie este un motiv real să plătești.

**Pentru munca generativă, justificarea slăbește repede.** Redactarea, rezumarea, refactorizarea codului, reformatatea datelor, clasificarea documentelor și fluxurile automate sunt sarcini ale căror rezultate sunt verificate înainte de a fi acceptate. Diferența de precizie costă puțin când un om sau o suită de teste verifică rezultatul. Pentru aceste sarcini, e greu să justifici plata per token pentru un indice 30.1 când un indice 33.7 rulează gratuit pe hardware-ul pe care îl deții deja.

**Decizia s-a mutat de la capacitate la consecințe.** Acum doi ani întrebarea era dacă modelul local putea face treaba. Astăzi întrebarea este cât costă o greșeală și cum o depistezi.

*Suplimentul pentru companii cumpără fiabilitate, conformitate și tura de gardă a altcuiva. Ceilalți plătesc pentru o diferență care încetează să conteze când rulează o suită de teste.*

## Idei principale

- **Un model local 27B îl depășește acum pe Claude Sonnet 4.6 în indicele agregat de inteligență**, 33.7 față de 30.1, și conduce la programare, sarcini agentice, context lung și raționament științific de nivel postuniversitar.
- **Sonnet 4.6 câștigă încă la precizia factuală**, 40.9 față de 15.6 la sută la AA-Omniscience, cel mai puternic argument rămas pentru gama de top.
- **Cuantizarea ternară face acest lucru practic.** Bonsai 2 27B rulează același model 26.90B în 5.53 GiB, nu 18 GB, iar ambele au licență Apache 2.0.
- **Ollama standard nu poate rula pachetele ternare.** Au nevoie de fork-ul llama.cpp al Prism ML, iar alternativa F16 produce în tăcere rezultate incoerente în loc să eșueze.
- **Viteza măsurată de decodare este 135 de tokeni pe secundă** pe RTX 5090, cu mult peste viteza de citire.
- **Prețurile memoriei sunt motivul să acționezi acum.** Prețurile contractuale DRAM au crescut cu 90 până la 95 la sută într-un singur trimestru din 2026, iar GPU-urile de consum de generație următoare au fost amânate până în 2028.
- **RTX 5090 a crescut de la $1,999 la peste $5,000** în mai puțin de doi ani, iar toate celelalte niveluri s-au scumpit.

## Pașii următori

1. **Descarcă modelul și testează-l cu propria sarcină**: **[Ternary Bonsai 2 27B în Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)**
2. Dacă ai suficientă memorie, **obține ponderile originale** la precizie completă: **[Qwen3.8 în Ollama](https://ollama.com/library/qwen3.8)**
3. **Încearcă modelul înainte să construiești ceva** prin endpoint-ul găzduit gratuit: **[Qwen3.8 27B gratuit în OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)**
4. **Compară-l cu opțiunea plătită folosind aceleași solicitări**: **[Claude Sonnet 4.6 în OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)**
5. **Dimensionează sistemul pentru nivelul de care ai nevoie din tabelul de memorie** și cumpără memoria înaintea plăcii video.
6. **Dacă ai un Raspberry Pi nefolosit, vezi dacă poate găzdui un model mai mic**: **[Ce modele IA pot rula pe Raspberry Pi 4 sau 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Articole conexe

| Articol | Ce acoperă |
|---|---|
| **[Ce modele IA pot rula pe Raspberry Pi 4 sau 5?](/articles/ai-models-raspberry-pi-4-5/)** | Limita inferioară a inferenței locale și ce pot rula cu adevărat plăcile mici |
| **[Construirea unui asistent IA care păstrează confidențialitatea pentru Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un asistent local pe hardware fără conexiune, unde confidențialitatea este obligatorie |
| **[Rolul memoriei ECC în reducerea coruperii datelor](/articles/the-role-of-ecc-memory-in-mitigating-data-corruption/)** | De ce contează mai mult calitatea memoriei când găzduiește un model mare |
| **[Ce este un laborator casnic și ai nevoie de unul?](/articles/what-is-a-homelab-and-should-you-have-one/)** | Planificarea spațiului, energiei și răcirii pentru hardware care se încinge |

## Referințe

1. [Ternary Bonsai 2 27B - oglinda modelului Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)
2. [Qwen3.8 - biblioteca de modele Ollama](https://ollama.com/library/qwen3.8)
3. [Qwen3.8 27B (gratuit) - teste și prețuri OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)
4. [Claude Sonnet 4.6 - teste și prețuri OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)
5. [Primul test Bonsai 2 27B: este cel mai bun model IA pentru un singur GPU? - Bijan Bowen](https://www.youtube.com/watch?v=OA5cICIzD-c)
6. [Artificial Analysis - evaluări independente ale modelelor](https://artificialanalysis.ai/)
7. [TrendForce - prognoze privind prețurile contractuale DRAM și NAND](https://www.trendforce.com/)
8. [Cipurile de memorie sunt acum mai scumpe decât cipurile de calcul pe unitatea de suprafață - Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon)
9. [Scăderea prețurilor GPU amânată în 2028 după o creștere DRAM record de 95% - Tech Insider](https://tech-insider.org/gpu-relief-pushed-2028-dram-price-jump-2026/)
10. [Tan de la Intel: memoria s-a scumpit de 7 ori, fără ameliorare până în 2028 - shattered.io](https://shattered.io/intel-ceo-memory-shortage-no-relief-until-2028-2026/)
11. [Fork-ul llama.cpp de la Prism ML - nuclee ternare](https://github.com/PrismML-Eng/llama.cpp)
12. [Ternary-Bonsai-2-27B-gguf - ponderile sursă](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
