---
title: "Hindsight găzduit local: memorie locală pentru agenți și rutarea privată a modelelor"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Studiu de caz despre Hindsight găzduit local, rutele Qwen locale observate și utilizarea GPU pentru cereri fără un abonament de inferență găzduită pe traseele inspectate."
genre: ["AI locală", "AI găzduită local", "Agenți AI", "Infrastructură AI", "Confidențialitate"]
tags: ["Hindsight", "Hindsight găzduit local", "memoria agenților", "AI locală", "LLM local", "Qwen3.5", "LiteLLM", "VPN privată", "gateway de modele", "embeddinguri", "reranking", "planificarea GPU", "inferență privată", "Docker", "bănci de memorie", "pagini de cunoștințe", "rutarea locală a modelelor"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Un serviciu privat abstract de memorie direcționează sarcini către servere locale de modele CPU și GPU"
coverCaption: "Stocarea și regăsirea memoriei, precum și rutele de modele inspectate, folosesc echipamente proprii"
---

**Serviciul nostru de memorie Hindsight rulează pe echipamente pe care le controlăm.** Motorul de memorie, baza de date, modelul de embeddinguri și rerankerul rulează într-o singură implementare găzduită local. Hindsight trimite cereri de generare către un gateway privat. Backendul Qwen partajat inspectat și ruta testată de reîmprospătare a paginilor folosesc servere locale de modele, fără un abonament de inferență găzduită.

Aceasta descrie o implementare funcțională. **Găzduirea locală nu înseamnă funcționare offline.** VPN-ul folosește un serviciu extern de coordonare, iar imaginile software și ponderile modelelor trebuie descărcate. Afirmația de aici se referă la procesarea memoriei și inferența modelelor, nu la fiecare conexiune de rețea inițiată de dispozitivele noastre sau de alte instrumente pentru agenți.

<!--more-->

## Idei principale

- **Hindsight gestionează fluxul de lucru al memoriei.** Un container Docker furnizează API-ul, procesele worker și planul de control, iar datele băncilor se află pe un volum persistent.
- **Modelele mici de regăsire rămân locale.** Embeddingurile și rerankingul rulează pe CPU în procesul Hindsight.
- **Qwen generează text.** Retain, Reflect și consolidarea solicită aliasul privat Qwen3.5-4B, cu raționamentul dezactivat și ieșirea limitată. Backendul inspectat servește local.
- **Reîmprospătările lungi de pagini primesc un GPU.** Un alias separat de model închiriază o placă pentru o cerere de fundal, apoi o eliberează.
- **Gateway-ul ascunde amplasarea fizică.** Hindsight selectează un alias de model. Serviciile private de rutare selectează un endpoint de servire.

## Stabilește limita înainte să alegi modelele

**Hindsight este motorul de memorie, nu serverul de modele.** Imaginea Docker completă include modele locale de embeddinguri și reranking, dar generarea cu un model lingvistic necesită un endpoint. [Ghidul de instalare Hindsight](https://hindsight.vectorize.io/developer/installation) descrie această separare și indică serverele locale llama.cpp, Ollama și vLLM ca alternative la furnizorii găzduiți.

**API-ul de memorie rămâne în rețeaua privată.** Planul de control web rămâne pe o interfață locală. Un volum persistent păstrează baza de date încorporată, astfel încât recrearea unui container să nu șteargă băncile. Autentificarea protejează API-ul, iar băncile separate organizează contextul proiectelor.

**Gateway-ul de generare oferă nume stabile pentru modele.** Hindsight trimite cereri compatibile cu OpenAI prin gateway-ul privat, folosind un VPN. Gateway-ul transmite cererile către endpointuri locale de servire. Ruta Qwen inspectată ajunge la o implementare LiteLLM asociată unui server local pe CPU. [Documentația routerului LiteLLM](https://docs.litellm.ai/docs/routing) descrie acest tipar de aliasuri de modele. Un router echivalent, compatibil cu OpenAI, îndeplinește același rol.

{{< figure src="hindsight-private-request-path.webp" alt="Diagramă cu agenți, un serviciu Hindsight privat, modele locale de regăsire, un gateway privat și servere Qwen locale" caption="Diagrama omite numele gazdelor, adresele, cheile de acces și etichetele gazdelor fizice" >}}

[Deschide diagrama completă a traseului cererii](hindsight-private-request-path.webp).

**Există în continuare un API intern.** Hindsight apelează un gateway privat folosind formatul compatibil cu OpenAI. Rutele inspectate ale modelelor servesc inferența local. Nu am auditat toate regulile de rezervă ale gateway-ului, așa că verifică politica acestuia înainte să tratezi procesarea locală ca pe o garanție pentru fiecare cerere.

## Atribuie fiecărei sarcini de memorie resursele potrivite

Operațiile Hindsight fac lucruri diferite. **Retain** extrage fapte din materiale noi. **Recall** găsește amintiri relevante. **Reflect** caută și redactează un răspuns sintetizat. **Consolidation** combină fapte asociate. Operația de fundal **knowledge-page refresh** reconstruiește un rezumat actual al băncii.

| Operație | Amplasarea modelului | Motiv |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B prin gateway-ul privat | Extragere structurată locală, cu buget de ieșire limitat |
| **Recall** | Embeddinguri și reranking locale pe CPU | Căutarea nu necesită un apel la API-ul de generare |
| **Reflect** | Qwen3.5-4B prin gateway-ul privat | Sinteza necesită generare după regăsirea amintirilor |
| **Consolidation** | Qwen3.5-4B prin gateway-ul privat | Loturile mici limitează răspunsurile structurate lungi |
| **Knowledge-page refresh** | Rută Qwen locală dedicată pe GPU | Sinteza amplă de fundal a depășit limita de timp a rutei CPU |

*Păstrează sarcinile mici de regăsire pe CPU și rezervă inferența GPU pentru lucrări de durată măsurată.*

Containerul Hindsight încarcă **BAAI/bge-small-en-v1.5** pentru embeddinguri și **hindsight-ai/hs-rerank-1** pentru reranking. Jurnalele de pornire confirmă că ambele rulează local pe CPU. [Referința de modele Hindsight](https://hindsight.vectorize.io/developer/models) descrie opțiunile de modele locale și ruta opțională pentru modelul de decizie.

Am păstrat modelul de embeddinguri existent, deoarece schimbarea spațiului de embeddinguri necesită reconstruirea vectorilor stocați. Rerankerul rulează deja local, așadar un serviciu de reranking găzduit ar adăuga o nouă graniță de date fără să rezolve timeoutul de generare observat. Un test pilot local cu **hs-decide-1-flash** a produs un răspuns Reflect corect, dar rezultatul a apărut aproape de limita de timp a testului. Datele sintetice de consolidare nu au exercitat ruta de decizie. Prin urmare, modelul de decizie lipsește din rutarea de producție.

## Oferă un GPU sarcinilor lente de fundal

**Numele obișnuit al modelului diferă de numele folosit la reîmprospătare.** Retain, Reflect și consolidarea folosesc aliasul Qwen partajat. Reîmprospătarea paginilor de fundal folosește un alias GPU specific nodului, cu un singur apel simultan către modelul lingvistic. Astfel, o sarcină lungă de mentenanță folosește cel mult un GPU odată.

**O rezervare per cerere limitează utilizarea GPU-ului.** Pool-ul GPU pornește un proces worker al modelului când sosește o cerere. Controlerul rezervă o placă, servește cererea, oprește procesul worker și eliberează rezervarea. Diagrama omite inventarul gazdelor fizice.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagramă care arată un GPU rezervat pentru reîmprospătarea unei pagini în fundal și eliberat la finalizarea cererii" caption="O rezervare per cerere atribuie un GPU pentru reîmprospătarea unei pagini" >}}

[Deschide diagrama completă a ciclului de închiriere GPU](hindsight-gpu-lease-cycle.webp).

Această separare a pornit de la un eșec măsurat. **O reîmprospătare de pagină cu prioritate CPU a atins limita de o oră.** După direcționarea reîmprospătărilor de fundal către pool-ul GPU local, cinci pagini care eșuaseră anterior s-au finalizat în aproximativ două până la șase minute într-o singură rundă de recuperare. Aceste cifre descriu paginile și setările respective. Nu reprezintă un benchmark general de debit Qwen.

## Ajustează valorile implicite și timeouturile

**Limitele de ieșire anterioare ale Hindsight nu se potriveau cu routerul nostru local.** Routerul acceptă cel mult 8.192 de tokeni de ieșire și aplică o limită de 256 de tokeni dacă o cerere nu specifică una. O limită Retain anterioară, de 64.000 de tokeni, a produs HTTP 400. Loturile de consolidare cu opt fapte s-au oprit la limita de lungime a ieșirii, iar Reflect a avut nevoie de o limită explicită pentru a evita valoarea implicită de 256 de tokeni a routerului.

**Am specificat limite explicite pentru fiecare sarcină.** Raționamentul Qwen este dezactivat pentru aceste operații de memorie. Hindsight permite acum patru apeluri LLM simultane în total, dintre care cel mult unul este un apel de reîmprospătare a paginilor de fundal. Timeoutul global LLM este de 1.800 de secunde, cu o reîncercare a modelului.

| Sarcină | Limită de ieșire sau de lot | Limitele apelurilor și operațiilor |
| --- | --- | --- |
| **Retain** | 8.192 de tokeni de ieșire | Timeout global de 1.800 de secunde pentru apel |
| **Reflect** | 4.096 de tokeni de ieșire | 900 de secunde per apel, 3.600 de secunde pentru operație |
| **Consolidation** | 4.096 de tokeni de ieșire, patru fapte per apel | 900 de secunde per apel, 14.400 de secunde pentru operație |
| **Page refresh** | Un apel simultan către model | 900 de secunde per apel, rută GPU dedicată |

*Aceste valori descriu implementarea și routerul nostru local din noiembrie 2026.*

**Timeoutul unui apel și limita totală a unei operații controlează etape diferite.** Unele apeluri Qwen valide au depășit vechiul timeout de 300 de secunde. Limitele mai lungi ale operației permit lucrul cu mai multe apeluri, în timp ce limita de 900 de secunde per apel restricționează fiecare încercare.

În runda de recuperare, mai multe sarcini Retain s-au încheiat cu **1.042 până la 2.076 de tokeni de ieșire**. Două runde de consolidare au finalizat **41 din 41**, respectiv **30 din 30** de elemente. O expirare ulterioară a limitei pentru reîmprospătarea paginii a dus la ruta GPU separată descrisă mai sus. Aceste rezultate de recuperare nu demonstrează fiabilitatea pe termen lung.

## Ce compromisuri implică proiectarea?

**Lipsa unei facturi pentru modele găzduite nu înseamnă cost zero.** Implementarea folosește echipamente proprii, electricitate, stocare, timp de mentenanță și timp GPU la reîmprospătarea paginilor. Fiecare alegere de amplasare schimbă capacitatea în favoarea latenței sau a simplității operaționale.

| Alegere | Avantaj | Compromis |
| --- | --- | --- |
| **Generare cu prioritate CPU** | Păstrează disponibilitatea GPU-ului | O reîmprospătare testată a atins limita de o oră |
| **Reîmprospătarea paginilor pe GPU** | Cinci pagini s-au finalizat în aproximativ două până la șase minute într-o rundă | Consumă capacitate GPU și depinde de ruta dedicată |
| **Bază de date încorporată** | Păstrează implementarea compactă | Restrânge domeniul de defectare și necesită testarea copiilor de siguranță |

*Folosește o rută de reîmprospătare GPU după ce latența CPU măsurată depășește fereastra de mentenanță.*

[Ghidul de instalare Hindsight](https://hindsight.vectorize.io/developer/installation) recomandă PostgreSQL separat pentru implementările de producție mai mari. **Baza noastră de date încorporată are nevoie de o procedură testată de backup și recuperare** pe măsură ce banca crește.

**Inferența privată este o proprietate a traseului.** Verifică furnizorul selectat de Hindsight, asocierea modelelor din gateway, regulile de rezervă, procesul local al modelului, păstrarea jurnalelor și traficul de ieșire din rețea. ID-urile de trasare Hindsight ajută la corelarea cererilor, iar Docker rotește jurnalele containerului. Niciuna dintre măsuri nu dovedește că o cerere ulterioară a rămas locală. Un audit al gateway-ului furnizează dovezile complete care lipsesc.

## Recomandare

**Începe cu modele locale de regăsire și limite explicite de generare.** Rulează Hindsight și modelele sale de embeddinguri și reranking pe echipamente proprii. Direcționează generarea printr-un gateway privat compatibil cu OpenAI, peste un VPN. Măsoară fiecare operație înainte de a aloca resurse CPU sau GPU și rezervă ruta GPU pentru sarcini de fundal a căror latență CPU depășește fereastra ta de mentenanță.

*Verifică fiecare regulă de rezervă din gateway și testează recuperarea băncii înainte să consideri implementarea privată și rezilientă.* [Ghidul despre limitele de confidențialitate pentru AI locală](/articles/local-ai-privacy-boundary/) oferă o listă inițială de verificare.

## Concluzie

**Această implementare păstrează memoria Hindsight și traseele de inferență inspectate pe echipamente proprii, fără un abonament de inferență găzduită.** Regăsirea pe CPU, apelurile Qwen limitate și ruta GPU cu un singur apel pentru reîmprospătarea paginilor servesc sarcini diferite. Rundele de recuperare au finalizat lucrările Retain, consolidare și reîmprospătare a paginilor în aceste condiții. Următoarele verificări sunt un audit complet al regulilor de rezervă din gateway, un test de backup și o observare mai lungă a fiabilității.
