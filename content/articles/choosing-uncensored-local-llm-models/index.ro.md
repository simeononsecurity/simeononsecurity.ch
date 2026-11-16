---
title: "Cum să alegi un model AI local fără cenzură"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Compară variantele locale după răspunsuri complete, capacități păstrate, utilizarea contextului, cuantizare și memoria VRAM necesară."
genre: ["AI local", "AI găzduit pe cont propriu", "Siguranța AI", "Echipamente GPU"]
tags: ["AI local fără cenzură", "abliterare", "LLM local", "VRAM", "lungimea contextului", "cuantizare", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Stație locală de lucru AI cu o placă grafică și monitoare care afișează vizualizări ale modelelor și inferenței"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Alegerea modelului:** evaluează fiecare variantă după răspunsurile utile pe care le finalizează, calitatea pe care o păstrează și memoria de care are nevoie volumul tău de lucru. Un număr mic de refuzuri sau o fișă populară a modelului nu demonstrează aceste rezultate.

Eticheta **fără cenzură** nu are o scară standard de performanță. Editorii modelelor o folosesc pentru modificări diferite ale ponderilor, reglaje fine și șabloane de conversație. Compară fiecare candidat cu modelul original și testează-l pe sarcinile pe care vrei să le rulezi.

{{< youtube id="j-VqPVjztJE" enable="true" title="Am testat toate modelele AI locale fără cenzură (de la 8 GB la 32 GB VRAM)" description="Comparație între variante de modele locale, finalizarea răspunsurilor, setări de context și niveluri de memorie GPU." >}}

## Ce îți spune eticheta

Un **model abliterat** a primit modificări ale ponderilor pentru a schimba anumite comportamente de refuz. Lucrarea din 2024 despre direcția refuzului a demonstrat o metodă pe 13 modele conversaționale deschise. Instrumentele mai noi oferă și alte metode. De exemplu, Heretic 2 documentează atât ablația de rang arbitrar, cât și ablația direcțională. Eticheta de pe fișa modelului nu spune ce comportament s-a schimbat sau ce efect a avut modificarea.

Separă aceste patru proprietăți când compari modele:

| Proprietate | Ce să verifici |
|---|---|
| **Comportamentul de refuz** | Ce solicitări primesc un refuz, un răspuns parțial sau un răspuns complet? |
| **Păstrarea capacităților** | Cum se compară cu modelul original sarcinile de cunoștințe, raționament, programare și formatare? |
| **Finalizarea răspunsului** | Cât de des se termină generarea înainte să expire limita de tokenuri sau de timp? |
| **Compatibilitatea cu mediul de execuție** | Fișierul cuantizat exact rulează cu suficientă memorie pentru contextul de care ai nevoie? |

Un model modificat rămâne probabilistic. **Verifică separat calitatea:** acuratețea, fiabilitatea și utilizarea sigură. Păstrează disponibil un model aliniat în mod obișnuit pentru sarcinile în care protecțiile lui contează.

## De ce numărul de refuzuri oferă o ierarhie slabă

**Un scor de refuz** măsoară un rezultat pe un set de solicitări. Spune puține despre acuratețea faptelor, lungimea răspunsurilor sau dacă modelul livrează un răspuns final înainte să-și epuizeze bugetul de generare.

**Comparația Qwen3.8-27B realizată de Sapwell în septembrie 2026** a testat modelul de bază și opt variante cu aceeași configurație de servire. Setul de 13 sarcini a măsurat cunoștințe, matematică, programare și veridicitate. Un set HarmBench separat conținea 400 de solicitări dăunătoare, iar un evaluator LLM a analizat răspunsurile complete. Aceste rezultate privesc o singură familie de modele, un GPU și un design de evaluare.

| Varianta Qwen3.8-27B din studiu | Refuzuri explicite din 400 | Răspunsuri cu raționament neterminat |
|---|---:|---:|
| **Model de bază** | 381 | 0% |
| **OrcaRouter** | 2 | 38% |
| **Trohrbaugh** | 122 | 15% |

Numărul mare de refuzuri al modelului de bază a coincis cu mai puține rezultate neterminate. Numărul mic de refuzuri al OrcaRouter a coincis cu o rată mai mare de răspunsuri incomplete. Trohrbaugh a păstrat mai multe refuzuri și a produs mai puține răspunsuri incomplete. **Alege în funcție de sarcina ta și de compromisurile acceptabile.**

**Un studiu cu 23 de variante Gemma 4 E4B** a găsit pierderi importante la unele măsurători ale capacităților pentru varianta cu cele mai multe descărcări, în timp ce o modificare mai mică a rămas aproape de modelul de bază în testul ei. Popularitatea și numărul de descărcări descriu adoptarea. Nu măsoară calitatea.

Nu combina aceste măsurători într-un singur scor. **Separă indicatorii:** refuzul, finalizarea, corectitudinea și latența. Înregistrează și setul de solicitări, revizia modelului, șablonul de conversație, mediul de execuție, contextul și limita de ieșire. Schimbarea oricărei setări modifică sensul comparației.

## Diagnostichează răspunsurile goale înainte să înlocuiești modelul

**Tokenurile de raționament** consumă limita de ieșire înainte să apară text vizibil. Dacă limita se termină în timpul raționamentului intern, unele medii de execuție returnează un răspuns gol sau trunchiat. Acest rezultat diferă de un refuz sau de un răspuns complet, dar greșit.

**Benchmarkul Qwen3.6-27B al lui Sapwell** a arătat cum afectează acest lucru scorurile generale. Scorurile brute la matematică au variat mult deoarece unele rulări nu au ajuns la răspunsul final. Între răspunsurile finalizate, valorile de acuratețe măsurate au fost mult mai apropiate. Benchmarkul a separat capacitatea de a răspunde de epuizarea bugetului de raționament.

**Când răspunsul e gol, verifică motivul opririi și jurnalele mediului de execuție.** Înregistrează lungimea solicitării, alocarea contextului, limita de tokenuri de ieșire, timpul scurs și dacă modelul a produs un marcator de răspuns final. Apoi repetă solicitarea cu o limită de ieșire mai mare dacă echipament-ul are suficient spațiu.

| Rezultat | Categorie probabilă de investigat |
|---|---|
| **Text de refuz** | Modelul a refuzat solicitarea. |
| **Ieșire goală la limita de tokenuri** | Generarea și-a epuizat bugetul înainte să producă un răspuns final. |
| **Ieșire trunchiată** | Limita de generare a oprit un răspuns incomplet. |
| **Eroare de execuție** | Serverul, fișierul modelului sau alocarea memoriei a eșuat. |
| **Răspuns complet, dar greșit** | Modelul a returnat text, dar nu a trecut verificarea corectitudinii. |

**Ieșire goală:** confirmă rezultatul mediului înainte să numești fiecare caz un defect al modelului. O fereastră de context mai mare nu repară automat o limită mică de ieșire, un șablon greșit sau expirarea timpului aplicației.

## Rezervă VRAM pentru ponderi și context

Fișierul modelului este doar un consumator de memorie. Mediul de execuție are nevoie și de spațiu pentru **memoria cache KV**, care păstrează starea de atenție a solicitării și răspunsului active, precum și pentru buffere de calcul și alte procese încărcate. Creșterea lungimii contextului mărește utilizarea memoriei.

**Documentația actuală Ollama** indică ferestre de context implicite de 4K sub 24 GiB VRAM, 32K între 24 și 48 GiB și 256K la 48 GiB sau mai mult. Aceste valori descriu comportamentul implicit al mediului. Verifică contextul alocat și plasarea procesorului cu `ollama ps`.

**Exemplu pentru Linux:** această comandă stabilește valoarea implicită de 16K pentru noile sesiuni ale serverului Ollama:

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Verifică contextul alocat** față de dimensiunile obișnuite ale intrărilor și răspunsurilor cu modelul încărcat:

```bash
ollama ps
```

Coloanele `CONTEXT` și `PROCESSOR` arată alocarea și dacă modelul rulează pe GPU sau este descărcat parțial. **Alocarea contextului:** o limită afișată nu garantează că întreaga fereastră încape în VRAM.

### Puncte de pornire după memoria GPU

**Candidați de pornire:** aceste familii de modele au apărut în comparațiile variantelor din 2026. Dimensiunile fișierelor provin din anumite depozite cuantizate. Confirmă fișierul exact, compatibilitatea mediului și memoria măsurată înainte să consideri potrivit un candidat.

| Memorie GPU | Candidat de pornire | Limitarea principală |
|---|---|---|
| **8 GB** | Gemma 4 E4B, de exemplu varianta `coder3101` | Păstrează mic fișierul ponderilor. Lasă memorie pentru context și bufferele mediului. |
| **12 GB** | Gemma 4 12B, de exemplu fișierul GGUF Q4 de 7,4 GB de la `TrevorJS` | Oferă modelului mai multă capacitate, dar mai puțin spațiu pentru context lung decât o variantă mai mică. |
| **16 GB** | Un model mai mic sau un fișier Q3 Qwen3.8-27B | Depozitul Qwen indică 13,72 GB pentru Q3_K_S. Editorul îl consideră de calitate scăzută. Spațiul pentru context va fi limitat. |
| **24 GB** | Qwen3.8-27B Q4_K_S sau Q4_K_M | Depozitul actual indică fișiere de 16,71 GB și 17,77 GB. Rezervă spațiu pentru cache și buffere. |
| **32 GB** | Qwen3.8-27B Q6_K | Depozitul actual indică un fișier de 23,46 GB. Un fișier mai mare lasă mai puțină memorie pentru context decât o cuantizare mai mică. |

*Folosește-le ca puncte de pornire. Depozitele și versiunile se schimbă, iar dimensiunea fișierului nu prezice singură alocarea memoriei mediului sau calitatea răspunsurilor.*

Etichetele de cuantizare GGUF rezumă o alegere de codificare. **Diferențe între depozite:** fișierele cu aceeași adâncime nominală în biți nu garantează aceeași calitate. Un depozit Qwen etichetează Q3_K_S drept calitate scăzută și Q4_K_M drept alegere implicită. Înainte de descărcare, verifică dimensiunea exactă, fișa modelului, formatul solicitării și rezultatele testelor.

**Pentru dimensiunea cache-ului și compatibilitatea cu un GPU local,** consultă [ghidul pentru modele locale, GPU și context](/articles/local-ai-model-gpu-context-guide/). Recomandările lui se concentrează pe programare. Această pagină tratează comportamentul de refuz modificat și evaluarea.

## Inspectează șablonul de conversație și sursa modelului

Un **șablon de conversație** împachetează mesajele în tokenurile și instrucțiunile așteptate de model. Un pachet de model poate include un șablon personalizat sau o instrucțiune de sistem. Aceste modificări influențează comportamentul măsurat chiar dacă ponderile de bază rămân la fel.

**Efectul șablonului:** Sapwell a găsit o variantă Qwen3.8 al cărei pachet conținea o personalitate ce îi cerea modelului să nu refuze și să nu avertizeze niciodată. Afirmația privind numărul mic de refuzuri depindea de șablon. Comparația a uniformizat șabloanele pentru ca testul să evidențieze diferențele dintre ponderi. Această măsură de control nu dovedește că șablonul inclus este rău intenționat sau inutilizabil.

**Înainte de instalare:** verifică editorul, modelul de bază, licența, procesul de conversie, cuantizorul, șablonul și istoricul reviziilor. Compară-l cu modelul original folosind același șablon și același mediu. Dacă fișa modelului nu descrie metoda sau configurația testului, înregistrează proveniența ca necunoscută.

## Rulează o evaluare mică pentru volumul tău de lucru

**Construiește un set repetabil de solicitări** din sarcini obișnuite care îți aparțin sau pentru care ai permisiunea să testezi. Include activitatea pe care o va face modelul, întrebări factuale cu răspunsuri cunoscute și solicitări de formatare cu condiții clare de reușită. Adaugă câteva cazuri-limită sigure pentru ca refuzul să rămână parte din decizie.

**Păstrează setările de test constante** pentru modelul original și varianta editată. Nu modifica instrucțiunea de sistem, șablonul, cuantizarea, versiunea mediului, contextul, limita de ieșire sau setările de eșantionare. Salvează revizia modelului sau hash-ul fișierului împreună cu rezultatele.

Înregistrează separat fiecare rezultat:

- **Finalizare:** răspuns final, refuz, ieșire goală, trunchiere sau eroare de execuție.
- **Corectitudine:** reușită sau eșec față de un răspuns așteptat ori o grilă de evaluare.
- **Utilitate:** dacă răspunsul îndeplinește cerințele sarcinii.
- **Latență:** timpul până la primul token și timpul total de generare.
- **Memorie:** contextul alocat, plasarea pe GPU și VRAM maxim.
- **Comportament de siguranță:** refuzul sau continuarea adecvată pentru fiecare caz-limită.

Repetă setul după schimbarea unei singure variabile. Dacă răspunsul se finalizează după ce mărești limita de ieșire, prima problemă a ținut de buget. Dacă răspunsurile rămân incomplete, verifică șablonul modelului, modul de raționament, mediul și revizia modelului. **Păstrează varianta numai dacă îmbunătățește sarcina vizată fără pierderi inacceptabile de acuratețe sau siguranță.**

## Izolează implementarea

**Confidențialitate:** inferența locală depinde de întregul tău ansamblu tehnic. Verifică interfața, jurnalele, extensiile, telemetria și rutele de rețea. Tratează ponderile de neîncredere și șabloanele personalizate ca pe cod și configurare de la terți.

**Acces public:** nu expune niciodată direct punctul final al modelului pe internetul public. Izolează accesul la instrumente și folosește variantele editate doar pentru activități autorizate. Pentru acces de la distanță, pune punctul final în spatele unui gateway privat cu autentificare, limite de solicitări și izolare de rețea. Lucrarea originală despre direcția refuzului menționează implicațiile de securitate ale editărilor care elimină refuzurile.

## Concluzie

**Regulă de decizie:** alege modelul cu cele mai bune rezultate verificate pe propriul set de sarcini. Folosește numărul de refuzuri ca un indicator, apoi verifică finalizarea răspunsurilor, corectitudinea, comportamentul șablonului și rezerva VRAM. Începe cu un fișier potrivit GPU-ului tău, setează contextul pentru volumul de lucru și compară-l cu modelul original în condiții identice.

**Pentru dimensionarea GPU-ului,** compară aceste rezultate cu [benchmarkul de închiriere GPU pentru Qwen 27B](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Închiriază sau împrumută echipament înainte de achiziție dacă nu ești sigur de fișierul exact sau de contextul vizat.

## Surse

- [Benchmarkul de abliterare Qwen3.8-27B](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6 septembrie 2026.
- [Benchmarkul de abliterare Qwen3.6-27B](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmarkul variantelor Gemma 4 E4B](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1 august 2026.
- [Benchmarkul variantelor Gemma 4 12B](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28 august 2026.
- [Refuzul în modelele lingvistice este mediat de o singură direcție](https://arxiv.org/abs/2406.11717), Arditi și alții, 2024.
- [Documentația proiectului Heretic](https://github.com/p-e-w/heretic/).
- [Fișa oficială a modelului Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Documentația Ollama despre lungimea contextului](https://docs.ollama.com/context-length).
- [Fișa modelului Gemma 4 E4B `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [Fișierele GGUF Gemma 4 12B de la TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [Fișierele GGUF OrcaRouter Qwen3.8-27B](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [Formatul GGUF și tipurile de cuantizare](https://huggingface.co/docs/hub/en/gguf), documentația Hugging Face.
- [Sursa video: Am testat toate modelele AI locale fără cenzură (de la 8 GB la 32 GB VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).
