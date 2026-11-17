---
title: "Benchmarkuri pentru modele locale Hermes: combinațiile de GPU și modele pe care le-aș folosi"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Recomandările mele de modele Hermes se bazează pe teste de context lung, instrumente, streaming și vedere pe sisteme RTX 5060 Ti, RTX 2000E Ada, RTX 3060 Ti și RTX 3070."
genre: ["Inteligență artificială", "AI locală", "Tehnologie hardware"]
tags: ["Hermes Agent", "modele lingvistice locale", "benchmarkuri LLM", "inferență GPU", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "calificarea modelului", "apelarea instrumentelor", "context lung", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Ilustrație cu plăci grafice cu două ventilatoare și profil redus lângă titlul Hermes Model Benchmarks pe un fundal albastru închis"
coverCaption: ""
---

Pentru activități Hermes cu context lung, aș începe cu Qwen3.5 35B pe două plăci RTX 5060 Ti de 16 GB. Ruta testată a păstrat 239.153 de tokenuri de intrare prin LiteLLM și a trecut verificări separate pentru instrumente, streaming, vedere, solicitări puse în coadă și anulare. Qwen3.6 este alternativa mea cu o singură placă. Pe sistemele RTX 3060 Ti și RTX 3070 aș începe cu Qwen3.5 2B sau 4B.

Aceste alegeri provin din rularea modelelor prin căile de inferență folosite de agent. Am testat păstrarea intrărilor lungi, schimburile dus-întors cu instrumente, răspunsurile transmise în streaming, întrebările despre imagini și eliberarea modelului. Am testat și modurile și setările de memorie din spatele rutelor, deoarece încărcarea reușită a unui model spune puțin despre utilitatea lui în timpul unei solicitări lungi de agent.

Hermes cere cel puțin 64.000 de tokenuri de context pentru utilizarea agentului cu instrumente. Am folosit 65.536 de tokenuri reale de intrare drept prag de calificare pentru context lung. Numărul de tokenuri de intrare contează mai mult decât dimensiunea contextului anunțată de server. ([Documentația furnizorilor Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## Ce GPU-uri avea fiecare sistem

Literele sistemelor identifică configurațiile hardware folosite în rezultate.

| Sistem | GPU-uri folosite pentru acest benchmark | Modelul cu care aș începe |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, câte 16 GB | Qwen3.5 35B pe ambele plăci sau Qwen3.6 pe o singură placă |
| B | 1 × RTX 2000E Ada, 16 GB | Qwen3.5 9B dacă procesarea intrării lungi timp de câteva minute se potrivește sarcinii |
| C | 1 × RTX 2000E Ada, 16 GB | Gemma 3 4B pentru calea testată cu intrare lungă, Qwen3.5 0.8B fără raționare pentru recuperare limitată |
| D | 1 × RTX 2000E Ada, 16 GB | Qwen3.5 9B, Gemma 4 12B-IT sau GPT-OSS 20B pentru sarcinile testate cu modele mai mari |
| E | 9 × GeForce RTX 3060 Ti, câte 8 GB | Qwen3.5 2B sau 4B |
| F | 8 × GeForce RTX 3060 Ti, câte 8 GB | Qwen3.5 2B sau 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B sau 4B |

Numărul de plăci instalate nu înseamnă că fiecare solicitare a folosit toate GPU-urile. Testele Qwen3.5 35B și Flash Next au folosit ambele plăci în sistemul A. Qwen3.6 a folosit una. Repetarea reușită a testului de vedere Qwen3.5 4B în sistemul E a folosit o placă selectată dintr-un grup de opt, iar a noua a rămas exclusă din activitățile AI.

Privește duratele de mai jos ca rezultate comune pentru modelul, mediul de execuție și sistemul testate. Aceste rulări compară configurații utilizabile. Nu izolează arhitectura GPU drept cauză a diferenței de viteză.

## Două RTX 5060 Ti fac din Qwen3.5 35B alegerea mea pentru context lung

Qwen3.5 35B a obținut cel mai mare rezultat de retenție a intrării din aceste teste. Progresia directă Ollama a păstrat 248.279 de tokenuri de intrare într-un context de execuție de 262.144 de tokenuri. O solicitare separată de gateway în streaming a păstrat 239.153 de tokenuri de intrare, a returnat marcatorul inițial și s-a încheiat normal după 31 de tokenuri de ieșire în 148,12 secunde.

Rezultatul gateway-ului contează pentru Hermes deoarece solicitarea a trecut prin broker și LiteLLM. Solicitări separate au finalizat o interacțiune cu un instrument, au recunoscut o imagine roșie și au returnat două răspunsuri corecte când au fost trimise împreună. Brokerul a pus cele două solicitări în coadă. Închiderea unei solicitări transmise în streaming a eliberat brokerul și a descărcat modelul în 60,31 secunde.

| Solicitare Qwen3.5 35B | Tokenuri de intrare | Tokenuri de ieșire | Durată | Rezultat |
|---|---:|---:|---:|---|
| Ollama direct, prima etapă progresivă | 69,429 | 31 | 38.783 s | Marcator inițial exact |
| Ollama direct, continuare cu prefix comun | 124,179 | 31 | 28.472 s | Marcator inițial exact |
| Ollama direct, continuare cu prefix comun | 182,579 | 31 | 38.974 s | Marcator inițial exact |
| Ollama direct, continuare cu prefix comun | 248,279 | 31 | 54.215 s | Marcator inițial exact |
| Solicitare în streaming prin broker | 69,427 | 29 | 38.872 s | Marcator inițial exact |
| Solicitare LiteLLM în streaming | 239,153 | 31 | 148.12 s | Marcator inițial exact, descărcare curată |

Solicitările directe progresive au reutilizat un prefix în creștere. Duratele descriu comportamentul de continuare cu modelul încălzit. Rezultatul de 54,215 secunde nu este o măsurare independentă la rece a procesării unui prompt nou de 248K.

La cea mai mare etapă directă, modelul a raportat aproximativ 27,3 miliarde de octeți rezidenți pe cele două GPU-uri. Vârfurile de memorie pe placă au ajuns la 14.964 și 12.386 MiB.

Temperaturile maxime au ajuns la 62 și 63 C, iar rularea nu a înregistrat erori OOM sau Xid. Intrarea a lăsat 13.865 de tokenuri în contextul configurat pentru continuare. Răspunsul scurt cu marcator a folosit 31 dintre acestea.

Aș folosi ruta când păstrarea unui set mare de lucru contează mai mult decât cel mai scurt răspuns inițial. Verificările pentru instrumente și vedere stabilesc comportamente utile ale agentului, iar testul de intrare lungă stabilește retenția. Sunt sarcini separate.

## Qwen3.6 este opțiunea cu o singură placă

Qwen3.6-35B-A3B UD-Q4_K_XL a păstrat 131.000 de tokenuri de intrare pe o singură RTX 5060 Ti. Cealaltă placă a rămas inactivă în timpul testului. Astfel, sistemul are o alternativă utilă când nu se dorește alocarea ambelor plăci unui singur model.

| Solicitare Qwen3.6 prin gateway | Tokenuri de intrare | Tokenuri de ieșire | Durată | Rezultat |
|---|---:|---:|---:|---|
| Solicitare lungă inițială | 66,007 |  | 167.82 s | Marcator inițial păstrat |
| Solicitare mai lungă | 90,000 | 11 | 159.92 s | Marcator inițial păstrat, zero intrări în cache |
| Solicitare mai lungă | 119,999 | 11 | 250.61 s | Marcator inițial păstrat, zero intrări în cache |
| Aproape de limita de execuție | 131,000 | 11 | 287.09 s | Marcator inițial păstrat, zero intrări în cache |

Solicitarea de 131.000 de tokenuri s-a apropiat de limita de execuție de 131.072. Pentru un agent aș lăsa mai mult spațiu pentru răspuns și mesajele ulterioare ale instrumentelor. Un rezultat de retenție aproape de limită oferă dovezi despre procesarea intrării, nu un buget implicit rezonabil.

Utilizarea instrumentelor a trecut cu raționarea dezactivată. Raționarea implicită a consumat alocația de test de 512 tokenuri înainte să emită apelul instrumentului. Pilotul reușit a trecut și solicitările rapide, în streaming și de vedere. Verificarea inițială de context de 65.845 de tokenuri a durat 139,57 secunde.

## Qwen3.8 27B câștigă comparația cu răspuns echivalent la 66K

Pentru aceeași sarcină cu marcator de 66.007 tokenuri pe sistemul A, Qwen3.8 27B a returnat răspunsul cel mai repede. Aș păstra ruta disponibilă pentru solicitări apropiate de dimensiunea testată, alături de Qwen3.5 35B pentru setul de lucru mai mare.

| Rută sistem A | Tokenuri de intrare | Durată | Rezultat |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Marcator inițial păstrat |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Marcator inițial păstrat |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Marcator inițial păstrat |
| Alias de compatibilitate Flash Next IQ4 | 66,007 | 213.25 s | Marcator păstrat |

Qwen3.8 27B a durat aproximativ o treime din timpul solicitărilor echivalente Qwen3.6 și Flash Next. Sunt observații despre solicitări complete cu mediile de execuție testate, nu o comparație exclusivă a hardware-ului.

Răspunsurile rapide, streamingul și utilizarea instrumentelor au trecut și ele. Modul fără raționare a completat secvența integrală de culori și interacțiunea cu instrumentul, în timp ce testul cu raționare a returnat doar o parte din secvență în limita de 512 tokenuri.

Flash Next rămâne o opțiune implicită mai puțin atractivă pe acest sistem din cauza presiunii memoriei. Pilotul său de 65.847 de tokenuri a trecut în 201,41 secunde la un context de execuție de 98.304. Două profiluri anterioare de 131.072 au atins limitele de memorie înainte de a fi gata.

Ruta ulterioară a atins limita cgroup de 54 GiB. Pentru activități nesupravegheate aș alege o rută cu mai multă rezervă de memorie.

Ruta etichetată `flash-iq2` a servit backendul de compatibilitate Flash Next IQ4. Numele nu identifică un rezultat IQ2.

## RTX 2000E Ada gestionează intrări lungi, dar modelul schimbă timpul de așteptare

Gemma 3 4B este ruta testată pe care o prefer pentru intrări lungi în sistemul C. Două căi au păstrat peste 84K de tokenuri de intrare în aproximativ 88 de secunde. Rutele pentru modele mai mari au trecut și verificări utile de retenție, dar solicitările lor au durat câteva minute.

| Sistem | Model și cale | Tokenuri de intrare | Durată | Rezultat |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, gateway | 72,265 | 263 s | Ambii santinele păstrați, verificarea ulterioară a revenirii la minare a trecut |
| C | Gemma 3 4B, gateway | 84,044 | 88.05 s | Marcator inițial păstrat |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Marcator inițial păstrat |
| C | Gemma 4 12B-IT, gateway | 67,254 | 263.07 s | Marcator inițial păstrat |
| C | Gemma 4 12B-IT, Aperture fără streaming | 67,255 | 274.24 s | Marcator inițial păstrat |
| C | Gemma 4 12B-IT, streaming Aperture | 67,255 | 282.16 s | Marcator inițial păstrat |
| C | Qwen3.5 9B, gateway | 75,648 | 319.36 s | Marcator inițial păstrat, model descărcat |
| C | GPT-OSS 20B, gateway | 84,099 | 315.83 s | Marcator inițial păstrat, model descărcat |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Retenție trecută pe artefactul instalat |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Retenție trecută pe artefactul instalat |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Retenție trecută pe artefactul instalat |

Streamingul nu a eliminat timpul lung de preumplere Gemma 4 pe sistemul C. Primul conținut transmis a sosit după 277,49 secunde, mai târziu decât răspunsul complet de 274,24 secunde fără streaming. O încercare anterioară fără streaming a expirat înaintea repetării reușite. Aș rezerva ruta sarcinilor care acceptă câteva minute de procesare inițială.

Gemma 3 4B arată și de ce aș califica fiecare sistem testat separat. Sistemul D a ratat marcatorul inițial în două încercări de recuperare 65K, inclusiv la repetarea cu temperatură zero și 67.252 de tokenuri de intrare. Solicitarea deterministă s-a încheiat natural în 62,07 secunde cu GPU-ul complet rezident.

Finalizarea rapidă și răspunsul normal al API-ului nu au făcut răspunsul corect. Aș folosi ruta reușită din sistemul C și aș exclude ruta eșuată din sistemul D din selecția Hermes.

## Modul de raționare determină dacă Qwen3.5 0.8B este util

Qwen3.5 0.8B a devenit un candidat util pentru recuperare restrânsă pe sistemul C după dezactivarea raționării. Modelul mic Q8_0 a păstrat 75.649 de tokenuri de intrare prin gateway în 65,92 secunde. Rezultatul aparține artefactului Q8_0 testat și rutei fără raționare, nu configurațiilor vechi cu context 16K din altă parte a tabelului.

| Solicitare Qwen3.5 0.8B pe sistemul C | Tokenuri de intrare | Tokenuri de ieșire | Durată | Rezultat |
|---|---:|---:|---:|---|
| Raționare implicită, diagnostic scurt | 9,050 | 3,391 | 66.56 s | Marcator inițial exact |
| Raționare dezactivată, diagnostic comparabil | 9,055 | 21 | 7.65 s | Marcator inițial exact, fără text de raționare |
| Raționare implicită, încercare lungă |  |  | timeout 600 s | Răspuns nefinalizat |
| Raționare dezactivată, Ollama nativ | 75,656 | 22 | 69.80 s | Marcator inițial exact |
| Endpoint compatibil OpenAI fără raționare | 75,646 | 12 | 69.09 s | Marcator inițial exact |
| Broker cu mod fără raționare impus | 75,647 | 13 | 66.83 s | Marcator inițial exact |
| LiteLLM din sistemul A către sistemul C | 75,649 | 15 | 65.92 s | Marcator inițial exact |

Diagnosticul comparabil a scăzut de la 66,56 la 7,65 secunde, de aproximativ 8,7 ori mai rapid, în timp ce ieșirea generată a scăzut de la 3.391 la 21 de tokenuri. De aceea aș seta explicit modul de raționare pentru sarcini simple de extragere și rutare. Raționarea implicită a folosit cea mai mare parte din procesare pentru ieșiri inutile sarcinii.

O sondă scurtă compatibilă OpenAI a ratat marcatorul înainte ca repetarea cu temperatură zero să treacă. Verificările reușite ale rutei au folosit modul fără raționare și terminarea naturală, fără limită de ieșire. Alte trei gateway-uri au trecut solicitări scurte cu marcator în 4,22, 4,37 și 3,85 secunde. Aceste verificări confirmă rutarea, în timp ce solicitarea de 75.649 de tokenuri confirmă retenția intrării lungi prin gateway.

Aș testa această rută pentru recuperare și extragere delimitate. Aș alege un model mai mare pentru raționare deschisă a agentului. Recuperarea unui marcator sintetic este o sarcină mai îngustă decât planificarea, programarea sau coordonarea mai multor instrumente.

## Sistemele RTX 3060 Ti și RTX 3070 favorizează Qwen3.5 2B și 4B

Qwen3.5 2B și 4B sunt alegerile mele practice de pornire pentru plăcile de 8 GB. Solicitările de context textual pe sistemele E, F și G au trecut cu 65.579 de tokenuri de intrare și durate de la 30,343 la 93,753 secunde. Rutele 4B testate au trecut și verificări de instrumente, streaming și imagine.

Repetarea contextului de vedere 4B pe sistemul E a păstrat ambii marcatori și ordinea culorilor imaginii la 65.637 de tokenuri de intrare în 44,88 secunde. Au trecut și solicitările cu ordinea directă și inversată a culorilor. Repetarea a folosit o placă sănătoasă după ce alta a suferit o eroare de legătură Xid 79 și sistemul a repornit.

| Sistem | Context textual Qwen3.5 2B | Context textual Qwen3.5 4B | Context de vedere Qwen3.5 4B |
|---|---|---|---|
| E, grup RTX 3060 Ti | 65,579 tokenuri, 30.343 s | 65,579 tokenuri, 53.787 s | 65,637 tokenuri, 44.88 s |
| F, grup RTX 3060 Ti | 65,579 tokenuri, 61.282 s | 65,579 tokenuri, 93.753 s | 65,635 tokenuri, 84.749 s |
| G, grup RTX 3070 | 65,579 tokenuri, 76.731 s | 65,579 tokenuri, 90.807 s | 65,635 tokenuri, 87.496 s |

Fiecare dintre aceste sisteme a înregistrat 29 de verificări trecute. Diferența de timp dintre cele două sisteme RTX 3060 Ti arată și de ce aș selecta un profil de sistem testat în loc să clasific plăcile după aceste durate de solicitare.

Toate cele șapte sisteme au revenit la minare după fereastra de inferență. Verificarea separată de revenire după oprire pentru sistemul B a trecut cu shares proaspete acceptate. Placa defectă din sistemul E a revenit ulterior la minare după o repornire și consolidarea legăturii PCIe, dar a rămas exclusă din grupul AI. Restabilirea minării la sfârșitul ferestrei este diferită de predarea automată după fiecare solicitare de inferență.

## Încărcarea unui model nu îl califică

Aș exclude DeepSeek Coder V2 16B din opțiunile Hermes testate la 65K. Rularea cu cache f16 a păstrat 50.477 de tokenuri de intrare, dar rularea țintă de 65K a atins protecția VRAM. Alternativele de cache Q4 și Q8 au încărcat ponderile pe GPU-uri, apoi au atins limitele memoriei gazdei sau un debit slab pentru prompturi lungi.

| Profil cache DeepSeek Coder V2 | Context de execuție | Rezultat observat | Evaluarea mea |
|---|---:|---|---|
| f16 | 81,920 | Recuperare de 50.477 de tokenuri trecută, solicitare supradimensionată respinsă | Rezultat util la context mai scurt |
| f16 | 73,728 | Preumplerea țintă 65K s-a oprit la utilizare GPU de 15.802 MiB | Nu se califică pentru 65K |
| Q4_0 | 98,304 | Preumplerea lungă a scăzut la 96.72 tokenuri/s înainte de oprirea controlată | Potrivire slabă pentru această sarcină |
| Q8_0 | 77,824 | Preumplerea lungă a scăzut la 120.12 tokenuri/s înainte de oprirea controlată | Potrivire slabă pentru această sarcină |
| Q4_0 / Q8_0, profiluri mai mari | 163,840 / 98,304 | Protecțiile memoriei gazdei au oprit testele | Potrivirea memoriei depinde de întregul sistem |

Lecția practică este să testezi solicitarea pe care intenționezi să o trimiți. Rezidența GPU, un răspuns scurt și un context configurat mare nu demonstrează retenția intrărilor lungi la o latență utilă.

Granite 4.2 8B și GPT-OSS 20B s-au îmbunătățit după lucrări de urmărire specifice rutelor pe sistemul A. Ruta Q6_K Granite a păstrat 66.082 de tokenuri de intrare în 88,636 secunde fără intrare în cache. GPT-OSS și-a finalizat interacțiunea cu instrumentul după remedierea brokerului, în 9,854 secunde pentru apel și 9,849 pentru urmărire. Aș păstra aceste verificări reușite ale rutelor distincte de încercările anterioare incomplete.

## Rezultatele complete ale benchmarkului

Tabelul conține 295 de verificări pentru 59 de combinații de modele și sisteme. Matricea înregistrează 273 de treceri, o verificare de recuperare eșuată și șapte rezultate incomplete, inconsistente sau incompatibile. Paisprezece verificări sunt în afara domeniului de calificare 65K. Fiecare rând păstrează rezultatul măsurat vizibil.

Recomandările mele se aplică rutelor și sarcinilor care au trecut. Un rând eșuat sau incomplet nu califică comportamentul corespunzător.

Trecerile pentru context scurt și embedding se aplică propriilor sarcini. O trecere la context 16K sau 32K nu califică o rută pentru sarcina Hermes cu 65.536 de tokenuri de intrare. Numele modelelor de aici sunt etichete de rută. Eticheta `flash-iq2` a servit backendul de compatibilitate IQ4.

Rândul de context Qwen3.5 35B din sistemul A este etapa finală cu prefix comun din progresia de mai sus. Duratele instrumentelor scrise cu semnul plus arată separat apelul și urmărirea.

Rândul de concurență oferă duratele celor două solicitări puse în coadă. Rândul de anulare oferă timpul de eliberare după închiderea fluxului de către client. Progresiile suplimentare de context și comparațiile rutei Qwen3.5 0.8B apar în tabelele proprii de mai sus.

### Sistem A

| Etichetă rută model | Verificare | Rezultat | Tokenuri de intrare | Durata solicitării |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Trecut | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Trecut | 57 | 6.429 s |
| bonsai-2-27b | stream | Trecut |  | 9.371 s |
| bonsai-2-27b | tools | Trecut |  | 10.478 s |
| deepseek-coder-v2:16b | context | Incompatibil | 50,477 |  |
| deepseek-coder-v2:16b | quick | Trecut | 77 | 43.239 s |
| flash-iq2 | context | Trecut | 66,007 | 213.25 s |
| flash-iq2 | quick | Trecut |  | 56.03 s |
| flash-iq2 | stream | Trecut |  | 1.35 s |
| flash-iq2 | tools | Trecut |  | 16.55 s |
| gemma-4-12b-it | context | Trecut | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Trecut | 21 | 5.166 s |
| gemma-4-12b-it | stream | Trecut |  | 4.653 s |
| gemma-4-12b-it | tools | Trecut |  | 18.72 s |
| gemma-4-12b-it | vision | Trecut | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Trecut | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Trecut | 115 | 7.467 s |
| gemma-4-e4b-it | context | Trecut | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Trecut | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Trecut |  | 4.25 s |
| gemma-4-e4b-it | tools | Trecut |  | 8.734 s |
| gpt-oss-20b | context | Trecut | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Trecut | 73 | 10.548 s |
| gpt-oss-20b | stream | Trecut |  | 20.594 s |
| gpt-oss-20b | tools | Trecut |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Trecut | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Trecut | 20 | 4.009 s |
| granite-4.2-3b | stream | Trecut |  | 5.365 s |
| granite-4.2-3b | tools | Trecut |  | 6.086 s |
| granite-4.2-8b | context | Trecut | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Trecut | 20 | 5.857 s |
| granite-4.2-8b | stream | Trecut |  | 11.826 s |
| granite-4.2-8b | tools | Trecut |  | 11.852 s |
| qwen27b | context | Trecut | 66,007 | 54.64 s |
| qwen27b | quick | Trecut | 57 | 31.5 s |
| qwen27b | stream | Trecut |  | 0.92 s |
| qwen27b | tools | Trecut |  | 4.25 s |
| qwen3-embedding-0.6b | context | Trecut | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Trecut | 14 | 2.125 s |
| qwen3.5-0.8b | context | Trecut | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Trecut | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Trecut |  | 2.125 s |
| qwen3.5-0.8b | tools | Trecut |  | 4.416 s |
| qwen3.5-2b | context | Trecut | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Trecut | 17 | 4.519 s |
| qwen3.5-2b | stream | Trecut |  | 3.736 s |
| qwen3.5-2b | tools | Trecut |  | 5.046 s |
| qwen3.5-4b | context | Trecut | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Trecut | 15 | 19.935 s |
| qwen3.5-4b | stream | Trecut |  | 17.496 s |
| qwen3.5-4b | tools | Trecut |  | 7.308 s |
| qwen3.5-4b | vision | Trecut | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Trecut | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Trecut | 70 | 4.386 s |
| qwen3.5-9b | context | Trecut | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Trecut | 17 | 3.88 s |
| qwen3.5-9b | stream | Trecut |  | 3.378 s |
| qwen3.5-9b | tools | Trecut |  | 10.204 s |
| qwen3.5-9b | vision | Trecut | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Trecut | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Trecut | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Trecut |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Trecut |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Trecut | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Trecut | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Trecut | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Trecut | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Trecut |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Trecut |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Trecut | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Trecut | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Trecut |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Trecut | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Trecut | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Trecut | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Trecut | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Trecut |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Trecut |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Trecut |  | 3.86 s |

### Sistem B

| Etichetă rută model | Verificare | Rezultat | Tokenuri de intrare | Durata solicitării |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Trecut | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Trecut | 21 | 15.261 s |
| gemma-4-12b-it | stream | Trecut |  | 148.792 s |
| gemma-4-12b-it | tools | Trecut |  | 34.124 s |
| gemma-4-12b-it | vision | Trecut | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Trecut | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Trecut | 120 | 32.511 s |
| gemma3-4b | context | Trecut | 65,584 | 67.382 s |
| gemma3-4b | quick | Trecut | 15 | 6.329 s |
| gemma3-4b | stream | Trecut |  | 24.138 s |
| gemma3-4b | vision | Trecut | 306 | 7.018 s |
| gemma3-4b | vision_context | Trecut | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Trecut | 306 | 5.762 s |
| gpt-oss-20b | context | Trecut | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Trecut | 72 | 16.583 s |
| gpt-oss-20b | stream | Trecut |  | 32.075 s |
| gpt-oss-20b | tools | Trecut |  | 28.102 s |
| nomic-embed-text | context | Incomplet | 2,048 |  |
| nomic-embed-text | quick | Trecut |  | 7.117 s |
| qwen3-14b | context | Incomplet |  | 1800.09 s |
| qwen3-14b | quick | Trecut | 15 | 37.199 s |
| qwen3-14b | stream | Trecut |  | 35.471 s |
| qwen3-14b | tools | Trecut |  | 87.554 s |
| qwen3-8b | context | În afara domeniului sub 65K, exclus |  |  |
| qwen3-8b | quick | În afara domeniului sub 65K, trecut | 15 | 21.059 s |
| qwen3-8b | stream | În afara domeniului sub 65K, exclus |  |  |
| qwen3-8b | tools | În afara domeniului sub 65K, exclus |  |  |
| qwen3.5-9b | context | Trecut | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Trecut | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Trecut |  |  |
| qwen3.5-9b | quick | Trecut | 15 | 25.881 s |
| qwen3.5-9b | stream | Trecut |  | 143.44 s |
| qwen3.5-9b | tools | Trecut |  | 31.812 s |
| qwen3.5-9b | vision | Trecut | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Trecut | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Trecut | 75 | 28.626 s |

### Sistem C

| Etichetă rută model | Verificare | Rezultat | Tokenuri de intrare | Durata solicitării |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Trecut | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Trecut | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Trecut | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Trecut | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Trecut | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Trecut | 27 | 20.98 s |
| gemma-4-12b-it | quick | Trecut | 21 | 16.447 s |
| gemma-4-12b-it | stream | Trecut |  | 15.175 s |
| gemma-4-12b-it | tools | Trecut |  | 37.821 s |
| gemma-4-12b-it | vision | Trecut | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Trecut | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Trecut | 120 | 31.25 s |
| gemma3-4b | aperture_context | Trecut | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Trecut | 24 | 5.42 s |
| gemma3-4b | aperture_short | Trecut | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Trecut |  | 3.72 s |
| gemma3-4b | context | Trecut | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Trecut | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Trecut |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Trecut |  |  |
| gemma3-4b | gateway_short_via_system_f | Trecut |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Trecut |  | 6.06 s |
| gemma3-4b | quick | Trecut | 15 | 5.163 s |
| gemma3-4b | stream | Trecut |  | 24.691 s |
| gemma3-4b | vision | Trecut | 306 | 7.318 s |
| gemma3-4b | vision_context | Trecut | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Trecut | 306 | 5.831 s |
| gpt-oss-20b | context | Trecut | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Trecut | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Inconsistent |  |  |
| gpt-oss-20b | quick | Trecut | 72 | 21.603 s |
| gpt-oss-20b | stream | Trecut |  | 31.957 s |
| gpt-oss-20b | tools | Trecut |  | 26.096 s |
| nomic-embed-text | context | În afara domeniului sub 65K, incomplet | 2,048 |  |
| nomic-embed-text | quick | În afara domeniului sub 65K, trecut |  | 4.178 s |
| qwen3-14b | context | În afara domeniului sub 65K, incomplet |  | 1800.06 s |
| qwen3-14b | quick | În afara domeniului sub 65K, trecut | 15 | 35.809 s |
| qwen3-14b | stream | În afara domeniului sub 65K, trecut |  | 35.43 s |
| qwen3-14b | tools | În afara domeniului sub 65K, trecut |  | 87.723 s |
| qwen3-8b | context | În afara domeniului sub 65K, exclus |  |  |
| qwen3-8b | quick | În afara domeniului sub 65K, trecut | 15 | 21.293 s |
| qwen3-8b | stream | În afara domeniului sub 65K, incomplet |  | 900.01 s |
| qwen3-8b | tools | În afara domeniului sub 65K, exclus |  |  |
| qwen3.5-9b | context | Trecut | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Trecut | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Trecut | 21 | 72.14 s |
| qwen3.5-9b | quick | Trecut | 15 | 24.635 s |
| qwen3.5-9b | stream | Trecut |  | 143.157 s |
| qwen3.5-9b | tools | Trecut |  | 30.395 s |
| qwen3.5-9b | vision | Trecut | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Trecut | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Trecut | 75 | 28.645 s |

### Sistem D

| Etichetă rută model | Verificare | Rezultat | Tokenuri de intrare | Durata solicitării |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Trecut | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Trecut | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Trecut | 34 | 30.74 s |
| gemma-4-12b-it | quick | Trecut | 21 | 15.05 s |
| gemma-4-12b-it | stream | Trecut |  | 14.722 s |
| gemma-4-12b-it | tools | Trecut |  | 33.869 s |
| gemma-4-12b-it | vision | Trecut | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Trecut | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Trecut | 120 | 29.978 s |
| gemma3-4b | context | Trecut | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Eșuat | 67,252 | 62.07 s |
| gemma3-4b | quick | Trecut | 15 | 5.151 s |
| gemma3-4b | stream | Trecut |  | 22.552 s |
| gemma3-4b | vision | Trecut | 306 | 8.276 s |
| gemma3-4b | vision_context | Trecut | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Trecut | 306 | 5.651 s |
| gpt-oss-20b | context | Trecut | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Trecut | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Trecut | 84 | 15.96 s |
| gpt-oss-20b | quick | Trecut | 72 | 15.431 s |
| gpt-oss-20b | stream | Trecut |  | 31.052 s |
| gpt-oss-20b | tools | Trecut |  | 23.65 s |
| nomic-embed-text | context | Incomplet | 2,048 |  |
| nomic-embed-text | quick | Trecut |  | 2.798 s |
| qwen3-14b | context | Incomplet | 40,939 | 872.209 s |
| qwen3-14b | quick | Trecut | 15 | 36.021 s |
| qwen3-14b | stream | Trecut |  | 33.491 s |
| qwen3-14b | tools | Trecut |  | 82.471 s |
| qwen3-8b | context | Incomplet |  | 1800.07 s |
| qwen3-8b | quick | Trecut | 15 | 19.283 s |
| qwen3-8b | stream | Trecut |  | 19.401 s |
| qwen3-8b | tools | Trecut |  | 65.054 s |
| qwen3.5-9b | context | Trecut | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Trecut | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Trecut | 29 | 94.48 s |
| qwen3.5-9b | quick | Trecut | 15 | 27.16 s |
| qwen3.5-9b | stream | Trecut |  | 28.62 s |
| qwen3.5-9b | tools | Trecut |  | 28.129 s |
| qwen3.5-9b | vision | Trecut | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Trecut | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Trecut | 75 | 27.602 s |

### Sistem E

| Etichetă rută model | Verificare | Rezultat | Tokenuri de intrare | Durata solicitării |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Trecut | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Trecut | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Trecut |  | 28.136 s |
| gemma-4-e4b-it | tools | Trecut |  | 56.756 s |
| granite-4.0-h-tiny | context | Trecut | 65,566 |  |
| granite-4.0-h-tiny | quick | Trecut | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Trecut |  | 27.798 s |
| granite-4.0-h-tiny | tools | Trecut |  | 43.304 s |
| granite-4.2-3b | context | Trecut | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Trecut | 20 | 14.569 s |
| granite-4.2-3b | stream | Trecut |  | 6.948 s |
| granite-4.2-3b | tools | Trecut |  | 56.376 s |
| qwen3-embedding-0.6b | context | Trecut | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Trecut | 14 | 9.592 s |
| qwen3.5-0.8b | context | Trecut | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Trecut | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Trecut |  | 11.163 s |
| qwen3.5-0.8b | tools | Trecut |  | 39.214 s |
| qwen3.5-2b | context | Trecut | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Trecut | 15 | 12.509 s |
| qwen3.5-2b | stream | Trecut |  | 26.165 s |
| qwen3.5-2b | tools | Trecut |  | 42.056 s |
| qwen3.5-4b | context | Trecut | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Trecut | 15 | 26.736 s |
| qwen3.5-4b | stream | Trecut |  | 26.02 s |
| qwen3.5-4b | tools | Trecut |  | 57.293 s |
| qwen3.5-4b | vision | Trecut | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Trecut | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Trecut | 72 | 9.96 s |

### Sistem F

| Etichetă rută model | Verificare | Rezultat | Tokenuri de intrare | Durata solicitării |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Trecut | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Trecut | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Trecut |  | 28.042 s |
| gemma-4-e4b-it | tools | Trecut |  | 73.891 s |
| granite-4.0-h-tiny | context | Trecut | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Trecut | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Trecut |  | 27.296 s |
| granite-4.0-h-tiny | tools | Trecut |  | 75.377 s |
| granite-4.2-3b | context | Trecut | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Trecut | 20 | 15.703 s |
| granite-4.2-3b | stream | Trecut |  | 35.482 s |
| granite-4.2-3b | tools | Trecut |  | 52.539 s |
| qwen3-embedding-0.6b | context | Trecut | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Trecut | 14 | 8.122 s |
| qwen3.5-0.8b | context | Trecut | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Trecut | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Trecut |  | 13.266 s |
| qwen3.5-0.8b | tools | Trecut |  | 40.825 s |
| qwen3.5-2b | context | Trecut | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Trecut | 15 | 16.738 s |
| qwen3.5-2b | stream | Trecut |  | 25.29 s |
| qwen3.5-2b | tools | Trecut |  | 47.444 s |
| qwen3.5-4b | context | Trecut | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Trecut | 15 | 33.039 s |
| qwen3.5-4b | stream | Trecut |  | 25.658 s |
| qwen3.5-4b | tools | Trecut |  | 71.731 s |
| qwen3.5-4b | vision | Trecut | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Trecut | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Trecut | 70 | 27.518 s |

### Sistem G

| Etichetă rută model | Verificare | Rezultat | Tokenuri de intrare | Durata solicitării |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Trecut | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Trecut | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Trecut |  | 43.549 s |
| gemma-4-e4b-it | tools | Trecut |  | 66.616 s |
| granite-4.0-h-tiny | context | Trecut | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Trecut | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Trecut |  | 31.751 s |
| granite-4.0-h-tiny | tools | Trecut |  | 63.338 s |
| granite-4.2-3b | context | Trecut | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Trecut | 20 | 23.355 s |
| granite-4.2-3b | stream | Trecut |  | 28.75 s |
| granite-4.2-3b | tools | Trecut |  | 44.226 s |
| qwen3-embedding-0.6b | context | Trecut | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Trecut | 14 | 8.924 s |
| qwen3.5-0.8b | context | Trecut | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Trecut | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Trecut |  | 15.095 s |
| qwen3.5-0.8b | tools | Trecut |  | 36.672 s |
| qwen3.5-2b | context | Trecut | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Trecut | 15 | 20.949 s |
| qwen3.5-2b | stream | Trecut |  | 25.194 s |
| qwen3.5-2b | tools | Trecut |  | 37.552 s |
| qwen3.5-4b | context | Trecut | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Trecut | 15 | 41.84 s |
| qwen3.5-4b | stream | Trecut |  | 40.812 s |
| qwen3.5-4b | tools | Trecut |  | 54.999 s |
| qwen3.5-4b | vision | Trecut | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Trecut | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Trecut | 70 | 26.283 s |

## Cum am testat viabilitatea Hermes

Am folosit un marcator sintetic aproape de începutul unui prompt lung și am cerut marcatorul după textul de umplere. Răspunsul trebuia să returneze valoarea așteptată. Numărul de tokenuri de intrare raportat de server a stabilit dimensiunea solicitării. Un model care răspundea normal după un prompt mare tot eșua dacă marcatorul inițial era greșit.

Progresia Qwen3.5 35B a folosit înregistrări de umplere numerotate, temperatura 0 și lungimi în creștere de 3.800, 6.800, 10.000 și 13.600 de înregistrări. Aceste etape au returnat 69.429, 124.179, 182.579 și 248.279 de tokenuri de prompt. Modelul a rămas încărcat între etape, ceea ce a permis reutilizarea prefixului. Verificările separate Qwen3.6 aproape de limită au raportat zero tokenuri în cache.

Promptul lung 0.8B a repetat `river stone lantern orchard circuit velvet compass marble` de 8.400 de ori între o cheie de răspuns inițială și o întrebare finală de recuperare. Rularea nativă a trimis `think:false`, `num_ctx:131072`, `stream:false` și `keep_alive:0`. Ruta compatibilă OpenAI a folosit `reasoning_effort:"none"`. Brokerul a impus modul fără raționare pentru ruta sa, astfel că apelanții gateway-ului nu au avut nevoie de o suprascriere din client.

### Verificări de instrumente, vedere și eliberare

Testele instrumentelor au verificat solicitarea și răspunsul după revenirea rezultatului instrumentului. Un test simplu a folosit `add_numbers(7, 11)` și a așteptat 18. Testul Qwen3.5 35B a folosit `lookup_square` și a așteptat 49. GPT-OSS a folosit o căutare de inventar și trebuia să includă rezultatul returnat.

Verificările de vedere au folosit întrebări despre imagini roșii și albastre, au inversat ordinea imaginilor și au inclus culorile imaginilor plus marcatori de început și sfârșit în prompturi lungi. Testul Qwen3.5 35B a folosit un PNG roșu de 256 × 256. A fost necesară o remediere a conversiei conținutului imaginii din broker înainte ca solicitarea să treacă. Testul lung de vedere 4B din sistemul E a cerut ca ambii marcatori și ordinea culorilor să supraviețuiască intrării.

Am verificat memoria GPU, rezidența modelului, temperaturile, presiunea memoriei gazdei, evenimentele OOM și erorile GPU în timpul și în jurul rulărilor lungi. Protecția Qwen3.5 35B a verificat și eliberarea după o întrerupere controlată. Verificările ulterioare de anulare de către client și solicitări puse în coadă au exercitat calea brokerului. Două solicitări în coadă dovedesc gestionarea solicitărilor sub sarcina testată, nu existența a două backenduri GPU independente care rulează simultan.

### Cum să citești rezultatele de performanță

Duratele solicitărilor includ preumplerea intrării lungi și răspunsul returnat. Nu reprezintă tokenuri generate pe secundă. Întârzierea până la primul conținut contează pentru streaming, iar progresiile prefixului în cache trebuie interpretate separat.

Rulările ulterioare reușite cu modele mai mari în sistemele A și C au folosit ferestre de inferență dedicate, cu minarea inactivă. Modelele au fost descărcate după aceste solicitări. Minarea a fost restabilită pe toate cele șapte sisteme la sfârșitul ferestrei de testare. Aceste rezultate descriu serviciul modelului într-o fereastră de inferență, nu minarea și inferența simultane.

## Profiluri de backend folosite în teste

Alege profilul asociat sarcinii pe care vrei să o reproduci. Cuantizarea, contextul de execuție, tipul cache-ului, modul de raționare și amplasarea GPU-urilor influențează rezultatul.

| Sistem și model | Profil de backend testat |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, cache KV f16, ambele plăci RTX 5060 Ti de 16 GB, 64 GiB RAM gazdă, context de execuție 262.144 pentru progresia mare. Solicitările native au folosit `think:false`, temperatura 0, streaming și păstrare activă cinci minute între etape. Solicitările gateway au folosit brokerul și LiteLLM. Fără limită de ieșire a solicitării. |
| A, Qwen3.8 27B | llama.cpp la cerere prin broker și LiteLLM, context de execuție 262.144, un slot de inferență, cache K/V Q4, ambele plăci RTX 5060 Ti. Solicitarea de 66.007 de tokenuri nu a avut limită de ieșire. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, context 131.072, cache KV INT8, un GPU selectat, limită de memorie a grupului de procese de 55 GiB, limită de execuție 30 de minute, încărcare leneșă, descărcare după 60 de secunde inactive. Răspunsul lung pilot: 217 tokenuri de ieșire. Răspunsul gateway aproape de limită: 11 tokenuri de ieșire, fără limită de ieșire a solicitării. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, context 98.304, cache KV Q4, cache rezident de experți 8 GiB, ambele plăci RTX 5060 Ti. Limita de memorie pilot 52 GiB, ruta ulterioară 54 GiB. Răspunsul lung pilot: 10 tokenuri de ieșire. Combinațiile anterioare cu context și cache mai mari s-au oprit la limitele de memorie. |
| A, Granite 4.2 8B | Greutăți GGUF Q6_K, proces de lucru partajat llama.cpp, context 131.072, cache K/V Q4_0, `--n-predict -1`. Solicitarea lungă a folosit temperatura 0, streaming pentru utilizare și fără limită de ieșire. |
| A, DeepSeek Coder V2 16B | Greutăți GGUF Q4_0, Ollama 0.34.2, două plăci RTX 5060 Ti, 64 GiB RAM gazdă. Testele separate pentru cache f16, Q4_0 și Q8_0 au folosit contextele de execuție din tabelul comparativ. Fără limită de ieșire a solicitării. |
| B, C, D, serviciu Ollama auditat | Ollama 0.34.2, context 131.072, paralelism 1, un model încărcat, coadă de dimensiune 128, menținere activă 0, Flash Attention, cache KV Q4_0. |
| B, pilot gateway Qwen3.5 9B | Timeout de rută LiteLLM 1.800 de secunde, zero reîncercări, fără limită de context sau tokenuri de ieșire. Ambii marcatori au fost păstrați la 72.265 de tokenuri de intrare. Verificarea separată a revenirii la minare a trecut. |
| C, Qwen3.5 0.8B | Greutăți Q8_0 pe o placă RTX 2000E Ada la profil de putere 30 W. Context de execuție 131.072. `think:false` nativ, `reasoning_effort:"none"` compatibil OpenAI, fără limită de ieșire. Aliasul brokerului a fixat contextul de execuție și a impus modul fără raționare. |
| C, Gemma 4 12B-IT | Profil Ollama cu un singur GPU, context de execuție 131.072, solicitări Aperture în și fără streaming, fără limită de ieșire. Rularea Aperture directă a atins un vârf de 75 C și 30,64 W sub profilul configurat de 30 W, apoi s-a descărcat. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Artefacte instalate exacte testate prin Aperture, context de execuție 131.072, rezidență completă pe un GPU, finalizare naturală fără limită de ieșire a solicitării. |
| E, F, G, procese de chat llama.cpp | Build 11669, 99 de straturi GPU, paralelism 1, Flash Attention, cache K/V Q4_0, `--n-predict -1`. Contextul de execuție a variat după familia modelului. |

Profilurile de serviciu înregistrate descriu propriile configurații de execuție. Profilul Qwen3.5 35B cu cache f16 testat separat în sistemul A nu moștenește setările cache Q4_0 ale sistemelor Ollama mai mici.

### Amprentele modelelor pentru noile rulări cu intrare păstrată

Acești identificatori disting artefactele testate de alte descărcări sau aliasuri cu nume asemănătoare.

| Artefact | Cuantizare | Digest înregistrat sau SHA-256 al fișierului |
|---|---|---|
| Etichetă Ollama Qwen3.5 35B-A3B | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Etichetă Ollama de bază Qwen3.5 0.8B | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Fișier GGUF Granite 4.2 8B | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Digesturile manifestului Ollama și valorile SHA-256 ale fișierelor de greutăți identifică obiecte diferite. Potrivește identificatorul cu tipul artefactului din tabel.

## Ce aș rula cu Hermes

Aș face din Qwen3.5 35B ruta principală de context mare pe sistemul cu două RTX 5060 Ti. Rezultatul de retenție de 239.153 de tokenuri prin gateway, testele separate de instrumente și vedere și eliberarea verificată a solicitărilor susțin alegerea mai bine decât un model promovat cu o fereastră mare de context. Aș păstra Qwen3.8 27B pentru răspunsul mai rapid din comparația 66K și Qwen3.6 când contează folosirea unei singure plăci.

Pe sistemele RTX 2000E Ada, aș alege ruta Gemma 3 4B verificată în sistemul C pentru sarcina testată de răspuns cu intrare lungă. Aș încerca ruta Qwen3.5 0.8B fără raționare pentru recuperare și extragere delimitate. Rutele mai mari Gemma, Qwen și GPT-OSS se potrivesc sarcinilor care acceptă răspunsul inițial testat de patru până la cinci minute. Aș exclude din selecție ruta Gemma 3 eșuată din sistemul D.

Pentru plăcile RTX 3060 Ti și RTX 3070 de 8 GB, aș începe cu Qwen3.5 2B sau 4B. Rezultatele textuale 65K și verificările de imagine 4B susțin o configurație inițială utilă fără să dedici cele două plăci de 16 GB fiecărei solicitări. Presiunea memoriei Flash Next și comportamentul incomplet 65K al DeepSeek Coder V2 le fac opțiuni implicite mai slabe în profilurile testate.

Testele susțin aceste alegeri de modele și sisteme pentru fluxuri de lucru specifice. Retenția intrării, o interacțiune corectă cu un instrument, recunoașterea imaginii și eliberarea curată răspund fiecare la o parte diferită din viabilitatea Hermes. O configurație fiabilă are nevoie de comportamentele folosite de agentul tău și de context suficient pentru răspuns și traficul instrumentelor.

## Surse și lecturi conexe

- [Configurarea furnizorilor și cerințele de context Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Specificații NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Specificații NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Prezentare Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Alegerea unui backend de model local](/hermes-local-ai-broker-course/02-choose-a-backend/)
