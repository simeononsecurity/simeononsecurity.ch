---
title: "Ce modele AI rulează pe Raspberry Pi 4 sau 5?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Folosește măsurători pe Raspberry Pi 4 și 5 pentru a alege modele lingvistice locale după memorie, viteză și sarcină, de la modelele LFM2.5 mici la opțiuni 3B și mai mari."
genre: ["Raspberry Pi", "Inteligență artificială", "Auto-găzduire"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "AI local", "modele lingvistice mici", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "cuantizarea modelelor", "AI la margine"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Două computere Raspberry Pi pe un birou întunecat, cu ilustrații albastre și ambră ale unor rețele neuronale deasupra"
coverCaption: "Ilustrație cu modele AI locale care rulează pe hardware Raspberry Pi."
---

Un Raspberry Pi poate rula local un model lingvistic util, dar modelul trebuie să încapă în memoria plăcii și să răspundă într-un timp acceptabil pentru aplicația ta. Un Raspberry Pi 4 cu 2 GB se potrivește mai ales modelelor cu mai puțin de aproximativ un miliard de parametri. Un Raspberry Pi 5 cu 8 GB rulează confortabil modele compacte de 1B–3B și poate încărca unele modele cuantizate mai mari, cu compromisuri importante.

Am măsurat aceste modele cu Ollama pe un **Pi 4B de 2 GB** și un **Pi 5 de 8 GB**, ambele cu stocare microSD. Testele din tabele au folosit aceleași cinci prompturi scurte pentru asistent, același prompt de sistem, o seed fixă și o limită de ieșire de 140 de tokenuri. Am descărcat celelalte modele înaintea fiecărui test și am măsurat încărcarea la rece, timpul până la primul token vizibil, timpul total de răspuns, viteza de ieșire și memoria rezidentă maximă. Au fost teste cu o singură trecere pentru răspunsuri scurte. Rezultatele sunt exemple pentru dimensionarea resurselor, nu clasamente universale de viteză sau calitate. [CPU-ul Cortex-A76 și configurațiile de memorie disponibile ale Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) diferă semnificativ de [platforma Cortex-A72 a Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Tipuri de modele potrivite

| Tip de model | Exemple măsurate | Utilizare practică |
|---|---|---|
| Modele text mici, aproximativ 230M–600M de parametri | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Comenzi locale scurte, rezumate și întrebări cu constrângeri; cel mai bun început pentru un Pi 4 de 2 GB |
| Modele text compacte, aproximativ 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Mai mult spațiu pentru instrucțiuni nuanțate pe un Pi 5 sau Pi 4 cu mai multă memorie, dar răspunsuri mai lente decât la modelele cele mai mici |
| Modele text cuantizate de 3B–4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Candidați mai capabili pentru un Pi 5 de 8 GB dacă accepți câteva secunde de așteptare per răspuns |
| Modele sparse sau hibride mai mari | LFM2.5 8B | Rulează tehnic pe Pi 5 de 8 GB testat, dar folosește multă memorie și se încarcă lent la rece |

Aceste rezultate privesc **generarea de text**. Nu demonstrează performanța pentru generarea de imagini, recunoașterea vorbirii, viziune sau antrenare. „Rulează” înseamnă mai mult decât faptul că fișierul modelului încape pe card: runtime-ul, memoria cache a contextului, sistemul de operare și celelalte servicii au nevoie de RAM. Cuantizarea micșorează fișierul cu ponderi, dar poate reduce calitatea răspunsului, mai ales la setări extreme precum ponderile de 1 bit.

### Ce măsoară cifrele

Benchmarkul a trimis către API-ul de chat Ollama prompturi scurte despre fapte, proceduri de siguranță, context recuperat, vreme și ajutor. Toate modelele au primit același set de prompturi și aceeași seed. Am descărcat modelul înainte de cronometrare, astfel încât următoarea solicitare să includă o încărcare la rece. **Timpul total** este al cererii complete, în timp ce **tokenuri pe secundă** descrie doar generarea ieșirii. Am înregistrat și primul token *vizibil*, important când modelul raționează înainte să răspundă.

Pentru memorie, am eșantionat RAM-ul și swap-ul disponibil pe Pi, precum și memoria rezidentă a Ollama și a procesului de inferență în fiecare solicitare. Valorile **RSS** indică memoria rezidentă a procesului, nu cerința totală a gazdei. Paginile de fișiere, sistemul de operare, un browser sau alt serviciu local pot provoca swap chiar și la un model care pare să încapă. Tabelele folosesc testele inițiale cu cinci prompturi și o singură trecere. Ulterior am adăugat un prompt de știri și verificări ale regulilor de răspuns. Aceste verificări clarifică ce trebuie urmărit, dar nu transformă măsurătorile inițiale de viteză în rezultate de conformitate pentru șase prompturi.

Nici tokenurile pe secundă, nici numărul parametrilor nu sunt scoruri de calitate. Un model poate genera text repede și totuși să omită o sursă cerută, să depășească limita de cuvinte sau să lase o propoziție neterminată. Compară modelele cu prompturile pe care intenționezi să le trimiți și citește răspunsurile înainte de a alege unul pentru o aplicație.

## Raspberry Pi 4: alege modelele cele mai mici

Pi 4 de 2 GB testat avea puțină memorie liberă. Cele mai mici modele LFM2.5 au finalizat toate cele cinci prompturi, la fel și `qwen2.5:0.5b`. Sunt alegeri rezonabile pentru răspunsuri scurte offline sau un asistent local mic.

| Model | Fișierul modelului | Viteză de ieșire măsurată | Timp mediu de răspuns | Memorie sau rezultat observat |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF importat | 0.25 GB | 12.8 tokenuri/s | 7.2 s | Memorie rezidentă maximă 383 MB; 5/5 prompturi |
| LFM2.5-350M, GGUF importat | 0.38 GB | 8.6 tokenuri/s | 8.6 s | Memorie rezidentă maximă 516 MB; 5/5 prompturi |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokenuri/s | 9.7 s | 5/5 prompturi; disponibil direct din Ollama |
| MiniCPM5-1B, GGUF importat, raționament dezactivat | 0.69 GB | 5.9 tokenuri/s | 12.2 s | Memorie rezidentă maximă 883 MB; 5/5 prompturi |
| MiniCPM5-1B, GGUF importat, raționament implicit | 0.69 GB | 5.7 tokenuri/s | 33.3 s | Doar 1/5 prompturi a primit un răspuns vizibil util |
| `qwen3:0.6b`, raționament implicit | 0.52 GB | 6.4 tokenuri/s | 40.4 s | Un răspuns gol; placa a repornit |
| `granite4:350m` | 0.71 GB | 4.6 tokenuri/s | 15.5 s | 913 MB RSS, fără swap sau repornire; lent, dar stabil |
| `gemma3:1b` | 0.82 GB | 4.0 tokenuri/s | 30.7 s | Swap intens; placa a repornit în timpul testului |
| `qwen3.5:0.8b` | 1.04 GB | — | — | Nu a terminat; placa a repornit |

Rezultatele Pi 4 depind mai ales de restul sistemului. Am observat resetări în timpul testelor cu modele mai mari, inclusiv o rulare `qwen3.5:0.8b` care nu s-a încheiat. Aceasta descrie configurația noastră de 2 GB, nu afirmă că orice Pi 4 sau model 1B se va reporni. Un Pi 4 de 4 ori 8 GB are mai multă memorie, dar CPU-ul va face inferența mai lent decât pe Pi 5 testat. Nu am măsurat direct aceste variante de memorie Pi 4.

Un test inițial pe Pi 4 a părut mult mai slab decât măsurătorile finale: aproximativ 625 MB de fișiere GGUF temporare erau în `/tmp`, susținut de RAM, lăsând doar 500–600 MB liberi și împingând sute de megabytes în swap. După mutarea fișierelor pe stocare persistentă, rezultatele modelelor mici au ilustrat mai bine memoria de inferență. Pe o placă de 2 GB, chiar și *locul de stocare a descărcării* poate denatura un benchmark.

**Recomandare:** Modelul implicit pentru această placă de 2 GB este LFM2.5-350M importat. A rămas stabil la **516 MB RSS**, a lăsat aproximativ **1 GB RAM disponibil** și a trecut **5/6** verificări ale regulilor de răspuns pe Pi 4. În testele repetate pe Pi 5 a omis uneori numele sursei, deci aplicațiile care cer atribuire trebuie să verifice. Alege LFM2.5-230M când contează cel mai mult latența și rezerva de memorie: a fost mai rapid și mai ușor, dar într-un răspuns medical a transformat „nausea or vomiting” în „nausea/ventilator use”. Această eroare de conținut îl face o alegere implicită mai slabă pentru sănătate sau siguranță, deși scorul mecanic repetat a fost mai mare. Alege `qwen2.5:0.5b` dacă ai nevoie de un model din [registrul Ollama](https://ollama.com/library/qwen2.5/tags), ținând cont de conformitatea mai slabă cu instrucțiunile. `granite4:350m` a rămas stabil, dar a fost mai lent și a folosit mai multă memorie; MiniCPM5-1B este viabil doar când clientul dezactivează raționamentul. Evită Gemma 3 1B și Qwen3.5 0.8B pe această configurație specifică de 2 GB, deoarece testele noastre au provocat resetări.

## Raspberry Pi 5: mai multe opțiuni, cu un compromis de viteză

Pi 5 de 8 GB a rulat toate cele **25 de modele** din benchmarkul de viteză și memorie. Tabelul include fiecare rulare, inclusiv modelele pe care nu le recomandăm pentru răspunsuri scurte. † indică un GGUF importat. „Think off” descrie setarea pentru testul de viteză; testul separat de conformitate poate să nu fi folosit aceeași setare.

| Model | Fișier GB | Ieșire tok/s | Răspuns s | RSS maxim MB | Evaluare pentru răspunsuri scurte |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Latență minimă; conformitate repetată 78% |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Evită: ponderi 1 bit și 3/6 la conformitate într-o singură trecere |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Rapid, dar a omis sursa în 5 din 18 repetări |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Opțiune simplă din registru; conformitate repetată 61% |
| `qwen3:0.6b`, raționament dezactivat | 0.52 | 23.0 | 4.3 | 1,069 | Condiționat: 4/6; setarea de raționament contează |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Model 1 bit experimental; scorul unic 6/6 nu este confirmat |
| `minicpm5-1b` †, raționament dezactivat | 0.69 | 18.4 | 5.1 | 869 | Condiționat: raționamentul implicit a produs răspunsuri goale |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Încape, dar e mai lent și mai mare decât LFM2.5 mic |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Cel mai bun pentru sarcina noastră; conformitate repetată 89% |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Alternativă din registru; 5/6 la conformitate |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Cea mai bună conformitate repetată dintre modelele din registru: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6; Gemma 3 1B a urmat mai bine regulile |
| `qwen3.5:0.8b`, raționament dezactivat | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 cu raționament implicit; evită fără controlul raționamentului |
| `spark-x2.5-1.7b` †, raționament dezactivat | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 cu raționament implicit; evită fără controlul raționamentului |
| `qwen3:1.7b`, raționament dezactivat | 1.36 | 8.1 | 12.4 | 1,867 | Condiționat; mai multă memorie și întârziere decât opțiunile mici |
| `minicpm5-2b` †, raționament dezactivat | 1.56 | 7.7 | 10.9 | 1,787 | Condiționat; 5/6 într-o trecere, puncte suplimentare |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Opțiune 3B de încercat; 5/6 într-o trecere |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Evită pentru utilizare interactivă: decodare lentă |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Altă opțiune 3B; nu s-a raportat test de conformitate |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Încape, dar răspunde mai lent decât alternativele mici |
| `qwen3.5:2b`, raționament dezactivat | 2.74 | 5.0 | 16.1 | 3,627 | Multă memorie și întârziere; nu s-a raportat test de conformitate |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Evită pentru răspunsuri rapide; 14.3 s până la primul token |
| `ling-3.0-tiny` †, raționament dezactivat | 4.82 | 9.9 | 19.4 | 5,071 | Amprentă mare; 5/6 într-o trecere cu eșec de fundamentare |
| `lfm2.5:8b`, raționament dezactivat | 5.16 | 8.7 | 54.6 | 5,317 | Încape la limită; încărcare la rece de 34.4 s și răspunsuri prea lungi |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Evită: swap cu alte servicii Pi |

† GGUF importat. Timpii de răspuns și memoria provin din testul de viteză pe Pi 5 cu cinci prompturi; scorurile de conformitate provin din teste separate cu șase prompturi. Pentru un model fără scor nu s-a demonstrat că respectă regulile de răspuns.

Modelele LFM2.5 mici au fost cele mai rapide *pentru această sarcină de răspunsuri scurte*. Versiunea 1.2B oferă o cale de mijloc practică pe Pi 5 testat. Gemma 3 1B este o alternativă disponibilă doar în registru și a respectat mai bine regulile repetate decât Qwen2.5 1.5B în testele ulterioare. Un model 3B poate merita ieșirea mai lentă pentru prompturi care cer mai multă capacitate, dar timpii nu dovedesc singuri care model răspunde mai bine.

Întârzierile de încărcare la rece și până la primul token schimbă experiența. Pe Pi 5, LFM2.5-230M s-a încărcat în aproximativ **0.21 secunde** și a afișat un token vizibil în **0.37 secunde**. Qwen2.5 1.5B a avut nevoie de **2.59 secunde** pentru încărcare și **3.66 secunde** până la primul token vizibil; Qwen2.5 3B a avut nevoie de **5.60** și **7.97 secunde**. Pentru o întrebare ocazională, aceste întârzieri pot conta mai mult decât rata de ieșire după începerea generării. La un model încărcat permanent contează mai puțin, dar modelul ocupă memorie între solicitări.

Alți candidați măsurați arată de ce nu îi ordonăm doar după numărul de parametri. Cu raționamentul dezactivat, `qwen3:0.6b` a atins **23.0 tokenuri/s** pe Pi 5 la **1,069 MB RSS**, în timp ce MiniCPM5-1B importat a atins **18.4 tokenuri/s** la **869 MB RSS**. `granite4:350m` a necesitat o descărcare de **0.71 GB** și a generat **12.1 tokenuri/s**, în ciuda etichetei 350M. Împachetarea și arhitectura schimbă legătura dintre nume, dimensiunea fișierului, memorie și viteză.

Dacă clientul tău poate trimite fiabil `think: false`, Qwen3 0.6B și MiniCPM5-1B sunt experimente rezonabile ca alternative la LFM2.5. MiniCPM5-2B, Qwen3 1.7B și Spark-X2.5 1.7B au rulat și pe Pi 5, dar nu au oferit un avantaj clar de viteză și memorie față de alegerile noastre principale. Testul de conformitate a folosit raționamentul implicit pentru MiniCPM5-1B și Spark-X2.5; răspunsurile lor goale nu trebuie prezentate ca rezultat al rulărilor de viteză cu raționament oprit. Invers, o măsurătoare rapidă cu raționament oprit nu demonstrează că un pod fără acel indicator va primi un răspuns util.

Dacă simplitatea instalării contează mai mult decât viteza brută, Gemma 3 1B și Llama 3.2 1B sunt opțiuni plauzibile din registru pe Pi 5 de 8 GB. Gemma 3 1B a respectat regulile testate în **15/18** răspunsuri repetate. Llama 3.2 1B a trecut **5/6** într-o singură trecere, deci estimarea conformității este mai puțin sigură. Qwen2.5 1.5B s-a încărcat și a răspuns mai repede decât Gemma 3 1B în testul de timp, dar a trecut doar **4/6** verificări într-un singur test de conformitate. Alege după cerințele prompturilor tale.

Pentru prompturi text mai lungi sau dificile, Qwen2.5 3B și Llama 3.2 3B cuantizate sunt candidații 3B cu memorie moderată pe Pi 5 de 8 GB. Am măsurat viteza și memoria; Qwen2.5 3B a trecut **5/6** într-un singur test de conformitate. Nu a fost raportat un test comparabil pentru Llama 3.2 3B. Numărul mai mare de parametri oferă un motiv să le *testezi* la sarcini unde modelele mici nu reușesc, nu dovedește că le rezolvă mai bine. Granite 4 Micro și Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny și Gemma 3n E2B au încăput sau s-au încărcat în testele Pi 5, dar au oferit latență, rezervă de memorie sau fiabilitate mai puțin atractive pentru aplicația de răspuns scurt.

Cele două modele Bonsai arată costul cuantizării extreme. Fișierele lor Q1_0 erau surprinzător de mici pentru nume cu 1.7B și 4B parametri, totuși modelul 1.7B a trecut doar **3/6** verificări ale regulilor. Modelul 4B a trecut o singură verificare de șase prompturi, dar a avut nevoie de **18.1 secunde** pe răspuns și nu a fost confirmat repetat pentru conformitate. Tratează-le ca experimente, nu recomandări implicite, mai ales dacă răspunsul trebuie să fie de calitate.

Rezultatul LFM2.5-8B are nevoie de context: arhitectura hibridă folosește mai puțini parametri activi pentru fiecare token, astfel încât rata de decodare a depășit modelele dense 3B măsurate. Tot a durat **34.4 secunde** încărcarea la rece de pe microSD și a folosit peste **5.3 GB de memorie rezidentă**. Rezultatul arată ce încape, nu o alegere implicită comodă pentru un Pi cu alte servicii. Și `gemma3n:e2b` măsurat a folosit aproximativ 5.3 GB de memorie rezidentă și a provocat swap alături de celelalte servicii ale gazdei de test.

Rularea LFM2.5 8B a atins și limita completă de **140 tokenuri**, în loc să păstreze răspunsul scurt. Rularea Gemma 3 4B a avut nevoie de **14.3 secunde** până la primul token și de **30.3 secunde** pentru răspunsul complet. Ambele se pot încărca pe acest Pi 5, dar testele noastre nu s-au comportat ca un asistent mic și reactiv. Un model minuscul care răspunde suficient de scurt poate servi mai bine o interfață radio sau de comenzi decât un model mai mare cu decodare teoretic mai rapidă.

## Memorie, raționament și formatul modelului

O primă estimare utilă din măsurători este **dimensiunea descărcării modelului × 1.4** pentru memoria rezidentă de inferență. Este doar o regulă aproximativă: lungimea contextului, setările runtime-ului, arhitectura modelului și alte procese pot schimba necesarul. Verifică memoria disponibilă în timpul generării, păstrează un singur model încărcat pe o gazdă mică și lasă spațiu sistemului de operare. O placă de 4 GB poate începe cu modele mici sau compacte, dar recomandările noastre pentru 4 GB sunt extrapolări, nu teste directe pe varianta de 4 GB.

De exemplu, un fișier LFM2.5-1.2B de 0.73 GB a corespuns la aproximativ **967 MB RSS** pe Pi 5, în timp ce fișierul Qwen2.5 1.5B de 0.99 GB a ajuns la **1,361 MB RSS**. Regula funcționează rezonabil pentru aceste modele, dar nu este o limită fixă. Planifică mai mult decât memoria măsurată a procesului dacă Pi rulează și o interfață, un index de căutare, o bibliotecă locală sau un serviciu în fundal. Urmărește swap-ul într-o solicitare reală; un model care se încarcă, dar folosește mereu swap, nu este potrivit practic.

Unele modele generează un bloc intern de raționament înainte de răspunsul vizibil. În teste, `qwen3:0.6b` pe Pi 4 de 2 GB a avut nevoie de mult mai mult timp pentru a afișa text. MiniCPM5-1B a dat un răspuns util la doar unul dintre cinci prompturi cu raționamentul implicit, față de cinci din cinci cu raționamentul oprit. Pentru o limită scurtă a răspunsului, setează `think: false` într-o solicitare API Ollama compatibilă sau alege un model care nu raționează implicit. Setarea se aplică modelelor și clienților acceptați; nu este un comutator universal de viteză.

Distincția contează fiindcă limita de tokenuri poate include tokenuri de raționament chiar dacă utilizatorul nu vede un răspuns. Pe Pi 4, `qwen3:0.6b` cu raționamentul implicit a avut în medie **40.4 secunde pe solicitare**; un prompt a produs un răspuns vizibil gol. MiniCPM5-1B a avut în medie **33.3 secunde** cu setarea implicită și **12.2 secunde** cu raționamentul dezactivat. Pentru testele Pi 5 am dezactivat raționamentul la Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 și Spark-X2.5 unde indicau notele noastre. Compară fiecare model cu setarea pe care o va folosi clientul.

### Verifică dacă răspunsul este util

Pentru sarcina noastră de asistent mesh cu răspuns scurt, contractul răspunsului contează la fel de mult ca viteza: cel mult **90 de cuvinte**, maximum **trei puncte de listă**, text simplu, o propoziție completă și folosirea contextului recuperat furnizat cu numele sursei. Podul împarte textul în fragmente de **180 de caractere**. Un răspuns lung ocupă mai mult timp radio, chiar dacă modelul l-a generat repede.

Versiunea ulterioară a benchmarkului verifică răspunsuri goale, limita de cuvinte specifică promptului, prea multe puncte, tabele sau blocuri de cod Markdown, final neterminat, termeni lipsă din contextul furnizat și nume de sursă lipsă. Evaluând răspunsurile după promptul de sistem al asistentului implementat, modelele mici încălcau des regulile. Cele mai importante erau **răspunsurile goale** când raționamentul consuma limita de tokenuri, urmate de răspunsuri care ignorau contextul recuperat sau îi omiteau sursa. Depășirea numărului de cuvinte ori de puncte producea totuși text vizibil, dar irosea timpul radio. Aceste verificări sunt mecanice și nu înlocuiesc citirea răspunsului: nu demonstrează corectitudinea faptelor sau calitatea sfaturilor de siguranță.

#### Rezultate repetate de conformitate pe Pi 5

Mai întâi am rulat șase prompturi o dată pentru fiecare model, cu o limită de **220 de tokenuri** și promptul de sistem implementat. Modelele promițătoare au fost testate de încă două ori cu o seed diferită, adică **18 răspunsuri per model**. O trecere perfectă nu garantează repetiții perfecte. Rezultatele repetate de mai jos oferă o comparație mai solidă pentru răspunsurile mesh scurte testate:

| Model | Răspunsuri care au respectat toate regulile verificate | Principalele eșecuri observate |
|---|---:|---|
| LFM2.5-1.2B importat | 16/18 (89%) | Două răspunsuri neterminate |
| `gemma3:1b` | 15/18 (83%) | Trei răspunsuri neterminate |
| LFM2.5-230M importat | 14/18 (78%) | Răspunsuri neterminate și nume de surse lipsă |
| LFM2.5-350M importat | 13/18 (72%) | Nume de surse lipsă |
| `qwen2.5:0.5b` | 11/18 (61%) | Prea multe puncte și cuvinte, nume de surse lipsă |

Pe **Pi 4 de 2 GB**, testul separat de conformitate cu șase prompturi a obținut **5/6** pentru LFM2.5-350M, **4/6** pentru LFM2.5-230M și **2/6** pentru Qwen2.5-0.5B. MiniCPM5-1B a crescut de la **1/6** cu raționamentul implicit la **5/6** cu raționamentul oprit. Scorurile Pi 4 provin dintr-o singură trecere, deci acordăm mai multă greutate rezultatelor repetate Pi 5 când discutăm urmarea generală a instrucțiunilor și folosim testele Pi 4 pentru stabilitate și viteză pe acea placă.

Eșecurile au consecințe diferite. Un răspuns **gol** nu ajută utilizatorul; un răspuns care ignoră materialul furnizat poate induce în eroare. Lipsa numelui sursei împiedică cititorii să verifice atribuirea. Punctele sau cuvintele în plus consumă în principal pachete suplimentare de 180 de caractere. O propoziție neterminată poate indica trunchiere. Eroarea unui termen medical de la LFM2.5-230M ne amintește că un răspuns poate trece verificările mecanice și totuși să fie greșit. Niciunul dintre cei cinci candidați testați repetat nu a respectat toate regulile în toate cele 18 răspunsuri. O aplicație care cere limite stricte de lungime sau format trebuie să le impună și după generare și să verifice separat conținutul cu risc ridicat.

Am verificat și endpointul real al podului, `/v1/chat/completions` compatibil OpenAI din Ollama, cu context WikiMed recuperat. Pe Pi 5, LFM2.5-1.2B a dat un răspuns de 28 de cuvinte folosind șase termeni furnizați; Qwen2.5-0.5B a dat 38 de cuvinte cu șapte termeni. Ambele au încăput în două pachete de 180 de caractere. Verificarea confirmă că modelul LFM2.5 importat funcționează prin calea de solicitare a podului, dar un singur răspuns reușit nu garantează fiabilitatea.

Ollama publică multe modele gata de descărcat, inclusiv [variantele Qwen2.5 de 0.5B, 1.5B și 3B](https://ollama.com/library/qwen2.5/tags). Am importat modelele LFM2.5 mici în Ollama din [versiunile GGUF Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main). Verifică tagul exact sau numele fișierului GGUF înainte de descărcare: registrele și depozitele se pot schimba. Păstrează descărcările GGUF pe stocare persistentă; în testele noastre, `/tmp` susținut de RAM a consumat memoria limitată a Pi 4.

### Taguri de registru și importuri GGUF

Un tag Ollama este cea mai scurtă cale către primul test: descarcă tagul exact și rulează-l. Modelele LFM2.5 mici din tabele au fost **importuri GGUF**, nu taguri `lfm2.5-230m`, `lfm2.5-350m` sau `lfm2.5-1.2b` din biblioteca publică Ollama. GGUF este un format de fișier model; nume precum `Q8_0` și `Q4_K_M` indică opțiuni de cuantizare. Fișierele LFM2.5 de 230M și 350M folosite erau Q8_0, iar fișierul 1.2B era Q4_K_M. Prin urmare, același număr de parametri în altă cuantizare poate avea dimensiune, consum de memorie și calitate diferite.

Pentru a importa varianta 350M testată, descarcă GGUF într-un director de pe stocare persistentă, creează un Modelfile care indică fișierul și lasă Ollama să îl copieze în magazinul său de modele:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

Importul are nevoie temporar de spațiu atât pentru fișierul descărcat, cât și pentru copia stocată de Ollama. Am folosit descărcări reluabile deoarece transferurile GGUF lungi se întrerupeau uneori. Înainte de import, compară SHA-256 al descărcării cu hash-ul publicat de sursă; un transfer incomplet poate părea o problemă a modelului. Pe Pi-ul nostru, `/tmp` era susținut de RAM, așa că un GGUF salvat acolo reducea memoria disponibilă pentru inferență.

## Un punct de pornire practic

| Hardware și obiectiv | Primul model de încercat | Motiv |
|---|---|---|
| Pi 4 de 2 GB, alegere implicită | LFM2.5-350M importat | Stabil la 516 MB RSS și cu aproximativ 1 GB disponibil; ales după eroarea medicală a modelului 230M |
| Pi 4 de 2 GB, latență minimă | LFM2.5-230M importat | 383 MB RSS și răspuns mediu de 7.2 s; verifică atent conținutul, mai ales pentru sănătate și siguranță |
| Pi 4 de 2 GB, doar registru | `qwen2.5:0.5b` | Descărcare directă Ollama și stabil în testul nostru Pi 4 cu cinci prompturi; conformitate repetată 61% pe Pi 5 |
| Pi 4 de 4 GB sau Pi 5 | LFM2.5-1.2B importat, apoi test local | 967 MB RSS și conformitate repetată de 89% pe Pi 5 de 8 GB; nu am testat direct variante de 4 GB |
| Pi 5 de 8 GB, asistent reactiv | LFM2.5-1.2B importat | 15.5 tokenuri/s, răspuns total de 4.7 s și cea mai mare conformitate repetată măsurată |
| Pi 5 de 8 GB, numai configurare din registru | `gemma3:1b` | 11.2 tokenuri/s, 1,262 MB RSS și conformitate repetată de 83% |
| Pi 5 de 8 GB, încearcă un model text mai mare | Qwen2.5 3B sau Llama 3.2 3B cuantizate | Ambele au rulat la aproximativ 5 tokenuri/s și au folosit 2.4–2.8 GB RSS; Qwen2.5 3B a trecut 5/6 într-o singură verificare |

Aceste opțiuni prioritizează răspunsuri scurte și utile pe un Pi care poate rula și alte servicii. Sunt puncte de pornire, nu susținerea că un singur model este cel mai bun pentru orice sarcină. În verificarea de conformitate cu o singură trecere pe Pi 5, `qwen3.5:0.8b` și Spark-X2.5 cu raționament implicit nu au dat răspunsuri conforme, iar MiniCPM5-1B a obținut 1/6. Dacă clientul nu poate opri raționamentul, evită-le pentru această sarcină de răspunsuri scurte. Testează modelul final cu promptul, contextul, concurența și limita de răspuns prevăzute pentru implementare.

Pentru modelul din registru, după [instalarea Ollama pentru Linux](https://ollama.com/download/linux), rulează:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Testează prompturile tale, lungimea de răspuns dorită și celelalte servicii în funcțiune. Notează timpul total al răspunsului și consumul de memorie. Aceste valori arată mai bine decât numărul de parametri dacă un model se potrivește pe Pi.

Pe un nod cu memorie limitată, urmărește swap-ul în timpul testelor. Dacă un model mai mare face placa să nu răspundă, folosește unul mai mic și setează o limită de memorie potrivită pentru serviciul Ollama, astfel încât o încărcare prea mare să eșueze înainte să epuizeze memoria gazdei. O limită de serviciu este o protecție, nu o metodă de a face să încapă un model prea mare. Repornirile Pi 4 din testele noastre arată de ce reactivitatea și memoria disponibilă contează alături de tokenuri pe secundă.

## Transformă benchmarkul într-o decizie de implementare

Înainte să folosești zilnic un model, stabilește patru limite: **timp maxim de răspuns, memorie rezidentă maximă, formatul răspunsului și comportamentul la eșec**. Testează-le împreună cu serviciile care vor împărți placa. Un model care trece singur, dar provoacă swap lângă podul radio sau tabloul de bord, nu îndeplinește cerința de implementare.

Păstrează instalat un model mic de rezervă. Treci la el când modelul principal depășește limita de memorie, întoarce un răspuns gol sau încalcă formatul cerut. Notează la fiecare comparație tagul modelului, cuantizarea, versiunea Ollama, promptul, lungimea contextului și seed-ul, astfel încât o actualizare ulterioară să nu pară o îmbunătățire hardware.
