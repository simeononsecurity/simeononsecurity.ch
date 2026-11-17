---
title: "Quins models d’IA funcionen en una Raspberry Pi 4 o 5?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Tria models de llenguatge locals segons memòria, velocitat i càrrega de treball amb resultats mesurats en Raspberry Pi 4 i 5, des dels petits LFM2.5 fins a les opcions 3B i superiors."
genre: ["Raspberry Pi", "Intel·ligència artificial", "Autoallotjament"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "IA local", "models de llenguatge petits", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "quantització de models", "IA de perifèria"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Dos ordinadors Raspberry Pi en un escriptori fosc, amb il·lustracions blaves i ambre de xarxes neuronals a sobre"
coverCaption: "Il·lustració de models d’IA locals que s’executen en maquinari Raspberry Pi."
---

Una Raspberry Pi pot executar localment un model de llenguatge útil, però el model ha de cabre a la memòria de la placa i respondre en un temps acceptable per a la teva aplicació. Una Raspberry Pi 4 amb 2 GB és més adequada per a models de menys d’un miler de milions de paràmetres. Una Raspberry Pi 5 amb 8 GB executa còmodament models compactes d’1B–3B i pot carregar alguns models quantitzats més grans, amb compromisos importants.

Hem mesurat aquests models amb Ollama en una **Pi 4B de 2 GB** i una **Pi 5 de 8 GB**, totes dues amb emmagatzematge microSD. Les proves de les taules van fer servir els mateixos cinc prompts breus d’assistent, el mateix prompt de sistema, una seed fixa i un límit de sortida de 140 tokens. Vam descarregar els altres models abans de cada prova i vam mesurar el temps de càrrega en fred, el temps fins al primer token visible, el temps total de resposta, la velocitat de sortida i la memòria resident màxima. Van ser proves d’una sola passada per a càrregues de respostes breus. Els resultats serveixen per estimar recursos, no per establir una classificació universal de velocitat o qualitat. La [CPU Cortex-A76 i les configuracions de memòria disponibles de la Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) també difereixen força de la [plataforma Cortex-A72 de la Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Tipus de models adequats

| Tipus de model | Exemples mesurats | Ús pràctic |
|---|---|---|
| Models de text petits, d’uns 230M–600M paràmetres | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Ordres locals breus, resums i preguntes amb restriccions; millor punt de partida per a una Pi 4 de 2 GB |
| Models de text compactes, d’uns 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Més marge per seguir instruccions matisades en una Pi 5 o una Pi 4 amb més memòria, amb respostes més lentes que les dels models més petits |
| Models de text quantitzats de 3B–4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Candidats més capaços per a una Pi 5 de 8 GB si és acceptable esperar uns segons per resposta |
| Models més grans, dispersos o híbrids | LFM2.5 8B | Funciona tècnicament a la Pi 5 de 8 GB provada, però consumeix molta memòria i triga a carregar en fred |

Aquests són resultats de **generació de text**. No demostren el rendiment en generació d’imatges, reconeixement de veu, visió ni entrenament. «Funciona» vol dir més que el fitxer del model cabi en una targeta: el runtime, la memòria cau del context, el sistema operatiu i altres serveis també necessiten RAM. La quantització redueix la mida del fitxer de pesos, però pot reduir la qualitat de la resposta, sobretot amb ajustos extrems com els pesos d’1 bit.

### Què mesuren les xifres

El benchmark va enviar a l’API de xat d’Ollama prompts breus sobre fets, procediments de seguretat, context recuperat, temps i ajuda. Tots els models van rebre el mateix conjunt de prompts i la mateixa seed. Vam descarregar cada model abans de cronometrar-lo perquè la petició següent inclogués una càrrega en fred. El **temps total** és el de la petició completa; els **tokens per segon** descriuen només la generació de sortida. També vam registrar el primer token *visible*, important quan el model raona abans de respondre.

Per mesurar la memòria, vam registrar la RAM i el swap disponibles de la Pi, així com la memòria resident d’Ollama i del seu procés d’inferència durant cada petició. Les xifres de **RSS** corresponen a la memòria resident del procés, no a la demanda total de l’amfitrió. Les pàgines recolzades per fitxers, el sistema operatiu, un navegador o un altre servei local encara poden provocar swap en un model que aparentment hi cap. Les taules mostren les primeres proves de cinc prompts en una sola passada. Més endavant vam ampliar el banc de proves amb un prompt de notícies i comprovacions de les regles de resposta. Aquestes comprovacions ajuden a saber què observar, però no converteixen les mesures de velocitat anteriors en resultats de compliment amb sis prompts.

Ni els tokens per segon ni el nombre de paràmetres són una puntuació de qualitat. Un model pot generar text de pressa i ometre una font demanada, superar un límit de paraules o deixar una frase inacabada. Compara els models amb els prompts que tens previst enviar i llegeix les respostes abans de triar-ne un per a una aplicació.

## Raspberry Pi 4: prioritza els models més petits

La Pi 4 de 2 GB provada tenia poc marge. Els models LFM2.5 més petits van completar els cinc prompts, igual que `qwen2.5:0.5b`. Són opcions raonables per a respostes breus sense connexió o un petit assistent local.

| Model | Fitxer del model | Velocitat de sortida mesurada | Temps mitjà de resposta | Memòria o resultat observat |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF importat | 0.25 GB | 12.8 tokens/s | 7.2 s | Memòria resident màxima de 383 MB; 5/5 prompts |
| LFM2.5-350M, GGUF importat | 0.38 GB | 8.6 tokens/s | 8.6 s | Memòria resident màxima de 516 MB; 5/5 prompts |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 prompts; disponible directament a Ollama |
| MiniCPM5-1B, GGUF importat, raonament desactivat | 0.69 GB | 5.9 tokens/s | 12.2 s | Memòria resident màxima de 883 MB; 5/5 prompts |
| MiniCPM5-1B, GGUF importat, raonament predeterminat | 0.69 GB | 5.7 tokens/s | 33.3 s | Només 1/5 prompts va donar una resposta visible útil |
| `qwen3:0.6b`, raonament predeterminat | 0.52 GB | 6.4 tokens/s | 40.4 s | Una resposta buida; la placa es va reiniciar |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, sense swap ni reinici; lent però estable |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | Swap intens; la placa es va reiniciar durant la prova |
| `qwen3.5:0.8b` | 1.04 GB | — | — | No va acabar; la placa es va reiniciar |

Els resultats de la Pi 4 depenen especialment de la resta del sistema. Vam observar reinicis durant les proves de models més grans, inclosa una execució de `qwen3.5:0.8b` que no es va completar. Això descriu la nostra configuració de 2 GB, no vol dir que qualsevol Pi 4 o model 1B es reiniciï. Una Pi 4 de 4 o 8 GB té més memòria, però la CPU continuarà fent la inferència més lentament que la Pi 5 provada. No vam mesurar directament aquestes variants de memòria de la Pi 4.

Una prova inicial de la Pi 4 també va semblar molt pitjor que les mesures finals: uns 625 MB de fitxers GGUF temporals eren a `/tmp`, recolzat per RAM, i només quedaven 500–600 MB lliures; centenars de megabytes van passar al swap. Després de moure els fitxers a emmagatzematge persistent, els resultats dels models petits van reflectir millor la memòria d’inferència. En una placa de 2 GB, *el lloc on deses una descàrrega* també pot distorsionar un benchmark.

**Recomanació:** El nostre model predeterminat per a aquesta placa de 2 GB és el LFM2.5-350M importat. Va ser estable amb **516 MB RSS**, va deixar prop d’**1 GB de RAM disponible** i va superar **5/6** comprovacions de les regles de resposta a la prova de Pi 4. En les proves repetides de Pi 5 de vegades va ometre el nom de la font; les aplicacions que necessiten atribució ho han de comprovar. Tria LFM2.5-230M si la latència i el marge de memòria són prioritaris: era més ràpid i lleuger, però en una resposta mèdica va convertir “nausea or vomiting” en “nausea/ventilator use”. Aquest error de contingut el fa una opció predeterminada més feble per a respostes de salut o seguretat, tot i la puntuació mecànica repetida més alta. Tria `qwen2.5:0.5b` si necessites un model del [registre Ollama](https://ollama.com/library/qwen2.5/tags), tenint en compte que segueix pitjor les instruccions. `granite4:350m` va ser estable, però més lent i amb més consum de memòria; MiniCPM5-1B només és viable si el client desactiva el raonament. Evita Gemma 3 1B i Qwen3.5 0.8B en aquesta configuració concreta de 2 GB, perquè les nostres proves van provocar reinicis.

## Raspberry Pi 5: més opcions, amb un cost de velocitat

La Pi 5 de 8 GB va gestionar els **25 models** del benchmark de velocitat i memòria. La taula inclou totes les proves, també els models que no recomanem per a aquesta càrrega de respostes breus. † indica un GGUF importat. «Think off» assenyala la configuració de la prova de velocitat; la prova de compliment separada no necessàriament va utilitzar-la.

| Model | Fitxer GB | Sortida tok/s | Resposta s | RSS màxim MB | Valoració per a respostes breus |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Latència mínima; 78% de compliment repetit |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Evita’l: pesos d’1 bit i 3/6 en compliment d’una passada |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Ràpid, però va ometre la font en 5 de 18 repeticions |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Opció fàcil del registre; 61% de compliment repetit |
| `qwen3:0.6b`, raonament desactivat | 0.52 | 23.0 | 4.3 | 1,069 | Condicional: 4/6, la configuració de raonament és important |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Model experimental d’1 bit; el 6/6 d’una passada no està confirmat |
| `minicpm5-1b` †, raonament desactivat | 0.69 | 18.4 | 5.1 | 869 | Condicional: el raonament predeterminat donava respostes buides |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Hi cap, però és més lent i gran que LFM2.5 petit |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Millor per a la nostra càrrega; 89% de compliment repetit |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Alternativa del registre; 5/6 en compliment |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Millor compliment repetit dels models del registre: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6; Gemma 3 1B seguia millor les regles |
| `qwen3.5:0.8b`, raonament desactivat | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 amb raonament predeterminat; evita’l sense control del raonament |
| `spark-x2.5-1.7b` †, raonament desactivat | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 amb raonament predeterminat; evita’l sense control del raonament |
| `qwen3:1.7b`, raonament desactivat | 1.36 | 8.1 | 12.4 | 1,867 | Condicional; més memòria i retard que les opcions petites |
| `minicpm5-2b` †, raonament desactivat | 1.56 | 7.7 | 10.9 | 1,787 | Condicional; 5/6 en una passada, amb punts addicionals |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Opció 3B per provar; 5/6 en una passada |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Evita’l per a ús interactiu: descodificació lenta |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Una altra opció 3B; no s’ha comunicat cap prova de compliment |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Hi cap, però respon més lent que les alternatives petites |
| `qwen3.5:2b`, raonament desactivat | 2.74 | 5.0 | 16.1 | 3,627 | Memòria i retard elevats; no s’ha comunicat cap prova de compliment |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Evita’l per a respostes ràpides; 14.3 s fins al primer token |
| `ling-3.0-tiny` †, raonament desactivat | 4.82 | 9.9 | 19.4 | 5,071 | Gran ocupació; 5/6 en una passada amb fallada de fonamentació |
| `lfm2.5:8b`, raonament desactivat | 5.16 | 8.7 | 54.6 | 5,317 | Hi cap just; càrrega en fred de 34.4 s i respostes massa llargues |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Evita’l: swap amb altres serveis de la Pi |

† GGUF importat. Els temps de resposta i les xifres de memòria provenen de la prova de velocitat de Pi 5 amb cinc prompts; les dades de compliment venen de proves separades amb sis prompts. Si no hi ha puntuació, no s’ha demostrat que el model segueixi les regles de resposta.

Els LFM2.5 petits van ser els més ràpids *per a aquesta càrrega de respostes breus*. La versió 1.2B ofereix un terme mitjà pràctic a la Pi 5 provada. Gemma 3 1B és una alternativa disponible només al registre i, en proves posteriors, va seguir les regles de resposta repetidament millor que Qwen2.5 1.5B. Un model 3B pot compensar una sortida més lenta en prompts que necessiten més capacitat, però aquests temps no demostren per si sols quin model respon millor.

Les esperes per a la càrrega en fred i el primer token canvien l’experiència. A la Pi 5, LFM2.5-230M es carregava en uns **0.21 segons** i produïa un token visible en **0.37 segons**. Qwen2.5 1.5B trigava **2.59 segons** a carregar i **3.66 segons** fins al primer token visible; Qwen2.5 3B trigava **5.60** i **7.97 segons**. Per a una pregunta ocasional, aquestes esperes poden importar més que la velocitat de sortida un cop comença la generació. En un model carregat contínuament importen menys, però ocupa memòria entre peticions.

Altres candidats mesurats expliquen per què no els ordenem només pel recompte de paràmetres. Amb el raonament desactivat, `qwen3:0.6b` va arribar a **23.0 tokens/s** a la Pi 5 amb **1,069 MB RSS**, mentre que MiniCPM5-1B importat va arribar a **18.4 tokens/s** amb **869 MB RSS**. `granite4:350m` va necessitar una descàrrega de **0.71 GB** i va generar **12.1 tokens/s**, tot i l’etiqueta 350M. L’empaquetament i l’arquitectura canvien la relació entre nom, mida de fitxer, memòria i velocitat.

Si el client pot enviar `think: false` de manera fiable, Qwen3 0.6B i MiniCPM5-1B són experiments raonables com a alternatives a LFM2.5. MiniCPM5-2B, Qwen3 1.7B i Spark-X2.5 1.7B també van funcionar a la Pi 5, però no van oferir un avantatge clar de velocitat i memòria respecte de les opcions principals. La prova de compliment va fer servir el raonament predeterminat per a MiniCPM5-1B i Spark-X2.5; les seves respostes buides no s’han de presentar com el resultat de les proves de velocitat sense raonament. En canvi, una mesura ràpida amb el raonament desactivat tampoc demostra que un pont que no enviï aquesta opció rebi una resposta útil.

Si la simplicitat d’instal·lació importa més que la velocitat pura, Gemma 3 1B i Llama 3.2 1B són opcions raonables del registre en una Pi 5 de 8 GB. Gemma 3 1B va seguir les regles provades en **15/18** respostes repetides. Llama 3.2 1B va passar **5/6** en una passada, de manera que l’estimació de compliment és menys segura. Qwen2.5 1.5B es va carregar i va respondre més de pressa que Gemma 3 1B a la prova de temps, però només va passar **4/6** controls en la seva única prova de compliment. Tria segons els requisits dels teus prompts.

Per a prompts de text més llargs o difícils de tant en tant, Qwen2.5 3B i Llama 3.2 3B quantitzats són candidats 3B amb un ús moderat de memòria a la nostra Pi 5 de 8 GB. Vam mesurar velocitat i memòria; Qwen2.5 3B va passar **5/6** en una prova de compliment. No es va informar d’una prova comparable per a Llama 3.2 3B. Tenir més paràmetres és un motiu per *provar-los* en tasques on fallen els models petits, no una prova que les resolguin millor. Granite 4 Micro i Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny i Gemma 3n E2B van cabre o es van carregar en les proves Pi 5, però oferien una latència, marge de memòria o fiabilitat menys atractius per a aquesta aplicació breu.

Els dos models Bonsai mostren el cost de la quantització extrema. Els seus fitxers Q1_0 eren sorprenentment petits per a noms amb 1.7B i 4B paràmetres, però el model 1.7B només va passar **3/6** controls de les regles. El model 4B va passar una única prova de sis prompts, però trigava **18.1 segons** per resposta i no té confirmació repetida de compliment. Considera’ls experiments i no recomanacions predeterminades, especialment quan la qualitat importa.

El resultat LFM2.5-8B necessita context: la seva arquitectura híbrida fa servir menys paràmetres actius per token, així que la velocitat de descodificació va superar la dels models densos 3B mesurats. Tot i això, la càrrega en fred des de microSD va trigar **34.4 segons** i va usar més de **5.3 GB de memòria resident**. Mostra què hi cap, no és una opció predeterminada còmoda per a una Pi amb altres serveis. El `gemma3n:e2b` mesurat també va usar uns 5.3 GB de memòria resident i va provocar swap juntament amb els altres serveis de l’amfitrió de prova.

La prova de LFM2.5 8B també va arribar al límit complet de **140 tokens** en lloc de mantenir la resposta breu. La prova Gemma 3 4B va trigar **14.3 segons** fins al primer token i **30.3 segons** per completar la resposta. Tots dos es poden carregar en aquesta Pi 5, però en les proves no es van comportar com un assistent petit i reactiu. Un model diminut amb una resposta prou curta pot servir millor una interfície de ràdio o ordres que un model més gran amb descodificació teòricament més ràpida.

## Memòria, raonament i format del model

Una primera estimació útil de les nostres mesures és **mida de la descàrrega del model × 1.4** per a la memòria resident d’inferència. Només és una regla aproximada: la longitud del context, la configuració del runtime, l’arquitectura del model i altres processos poden canviar la necessitat. Comprova la memòria disponible durant la generació, mantén un únic model carregat en un host petit i deixa espai per al sistema operatiu. Una placa de 4 GB pot començar amb models petits o compactes, però les nostres recomanacions per a 4 GB són extrapolacions, no proves directes d’aquesta variant.

Per exemple, el fitxer LFM2.5-1.2B de 0.73 GB es corresponia amb aproximadament **967 MB RSS** a la Pi 5, mentre que el fitxer Qwen2.5 1.5B de 0.99 GB va arribar a **1,361 MB RSS**. La regla és força útil per a aquests models, però no és un límit fix. Reserva més memòria que la mesurada del procés si la Pi també executa una interfície, un índex de cerca, una biblioteca local o un servei de fons. Vigila el swap durant una petició real; un model que es carrega però fa swap constantment no és pràctic.

Alguns models generen un bloc de raonament intern abans de la resposta visible. En les proves, `qwen3:0.6b` a la Pi 4 de 2 GB trigava molt més a mostrar text. MiniCPM5-1B va donar una resposta útil a només un de cinc prompts amb el raonament predeterminat, enfront de cinc de cinc amb el raonament desactivat. Per a una resposta curta, estableix `think: false` en una petició API Ollama compatible o tria un model que no raoni per defecte. Aquesta opció funciona amb models i clients compatibles; no és un interruptor de velocitat universal.

La diferència importa perquè el límit de tokens pot incloure tokens de raonament encara que l’usuari no vegi cap resposta. A la Pi 4, `qwen3:0.6b` amb raonament predeterminat va trigar **40.4 segons per petició** de mitjana i un prompt va produir una resposta visible buida. MiniCPM5-1B va fer una mitjana de **33.3 segons** amb l’ajust predeterminat i **12.2 segons** amb el raonament desactivat. A les proves Pi 5 també vam desactivar el raonament per a Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 i Spark-X2.5 quan així ho indicaven els registres. Compara cada model amb l’ajust que farà servir el client.

### Comprova si la resposta és útil

Per a la nostra càrrega breu d’assistent mesh, el contracte de resposta importa tant com la velocitat: com a màxim **90 paraules**, no més de **tres vinyetes**, text pla, una frase completa i ús del context de recuperació proporcionat amb el nom de la font. El pont divideix el text en blocs de **180 caràcters**. Una resposta llarga ocupa més temps de ràdio, encara que el model la generi ràpidament.

La versió posterior del benchmark comprova respostes buides, el límit de paraules específic del prompt, massa vinyetes, taules o blocs de codi Markdown, un final inacabat, l’absència de termes del context proporcionat i el nom de la font. En puntuar les respostes segons el prompt de sistema de l’assistent desplegat, els models petits infringien les regles sovint. Les fallades més importants eren les **respostes buides** quan el raonament consumia el pressupost de tokens, seguides de respostes que ignoraven el context recuperat o n’ometien la font. Superar el límit de paraules o de vinyetes encara mostrava text, però malbaratava temps de ràdio. Són comprovacions mecàniques, no substitueixen la lectura de la resposta: no demostren exactitud factual ni qualitat dels consells de seguretat.

#### Resultats de compliment repetit a la Pi 5

Primer vam executar sis prompts una vegada per model, amb un límit de **220 tokens** i el prompt de sistema desplegat. Els models prometedors es van provar dues vegades més amb una seed diferent: **18 respostes per model**. Una passada perfecta no garantia repeticions perfectes. Els resultats repetits següents permeten comparar millor les respostes mesh breus provades:

| Model | Respostes que van seguir totes les regles comprovades | Principals fallades observades |
|---|---:|---|
| LFM2.5-1.2B importat | 16/18 (89%) | Dues respostes inacabades |
| `gemma3:1b` | 15/18 (83%) | Tres respostes inacabades |
| LFM2.5-230M importat | 14/18 (78%) | Respostes inacabades i noms de fonts absents |
| LFM2.5-350M importat | 13/18 (72%) | Noms de fonts absents |
| `qwen2.5:0.5b` | 11/18 (61%) | Massa vinyetes i paraules, noms de fonts absents |

A la **Pi 4 de 2 GB**, la prova separada de sis prompts va donar **5/6** a LFM2.5-350M, **4/6** a LFM2.5-230M i **2/6** a Qwen2.5-0.5B. MiniCPM5-1B va millorar d’**1/6** amb el raonament predeterminat a **5/6** amb el raonament desactivat. Aquests resultats de Pi 4 són d’una sola passada. Per parlar del seguiment general d’instruccions donem més pes als resultats repetits de Pi 5 i fem servir els de Pi 4 per jutjar estabilitat i velocitat en aquesta placa.

Les fallades tenen conseqüències diferents. Una resposta **buida** no ajuda l’usuari; ignorar el material proporcionat pot induir a error. Un nom de font absent impedeix verificar l’atribució. Les vinyetes o paraules addicionals consumeixen sobretot més paquets de 180 caràcters. Una frase inacabada pot indicar truncament. L’error de terme mèdic de LFM2.5-230M recorda que una resposta pot superar les comprovacions mecàniques i continuar sent incorrecta. Cap dels cinc candidats provats repetidament no va seguir totes les regles en les 18 respostes. Una aplicació amb límits estrictes de longitud o format també els hauria d’imposar després de generar i revisar a banda el contingut d’alt risc.

També vam comprovar l’endpoint real del pont, `/v1/chat/completions` compatible amb OpenAI d’Ollama, amb context WikiMed recuperat. A la Pi 5, LFM2.5-1.2B va retornar 28 paraules i va fer servir sis termes proporcionats; Qwen2.5-0.5B va retornar 38 paraules amb set termes. Totes dues cabien en dos paquets de 180 caràcters. Aquesta comprovació confirma que el model LFM2.5 importat funciona pel camí de peticions del pont, però una resposta correcta no en garanteix la fiabilitat.

Ollama publica molts models preparats per descarregar, incloses les [variants Qwen2.5 de 0.5B, 1.5B i 3B](https://ollama.com/library/qwen2.5/tags). Vam importar a Ollama els models LFM2.5 petits des dels [llançaments GGUF de Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main). Comprova l’etiqueta exacta o el nom del fitxer GGUF abans de descarregar: els registres i repositoris poden canviar. Desa les descàrregues GGUF en emmagatzematge persistent; en les proves, `/tmp` recolzat per RAM va consumir memòria escassa de la Pi 4.

### Etiquetes del registre i imports GGUF

Una etiqueta d’Ollama és el camí més curt per fer una primera prova: descarrega l’etiqueta exacta i executa-la. Els LFM2.5 petits de les taules eren **imports GGUF**, no etiquetes `lfm2.5-230m`, `lfm2.5-350m` o `lfm2.5-1.2b` de la biblioteca pública d’Ollama. GGUF és un format de fitxer de model; noms com `Q8_0` i `Q4_K_M` indiquen opcions de quantització. Els fitxers LFM2.5 de 230M i 350M que vam fer servir eren Q8_0, mentre que el fitxer 1.2B era Q4_K_M. Per tant, el mateix recompte de paràmetres amb una altra quantització no implica la mateixa mida de fitxer, ús de memòria o qualitat.

Per importar la variant 350M provada, descarrega el GGUF en un directori d’emmagatzematge persistent, crea un Modelfile que hi apunti i deixa que Ollama el copiï al seu magatzem de models:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

La importació necessita temporalment espai tant per al fitxer descarregat com per a la còpia desada per Ollama. Vam fer servir descàrregues que es reprenen perquè de vegades es tallaven transferències llargues de GGUF. Abans d’importar, compara el SHA-256 de la baixada amb el hash publicat per la font; una transferència parcial pot semblar un problema del model. Al nostre Pi, `/tmp` era recolzat per RAM, així que desar-hi un GGUF reduïa la memòria disponible per a la inferència.

## Un inici pràctic

| Maquinari i objectiu | Primer model per provar | Motiu |
|---|---|---|
| Pi 4 de 2 GB, opció predeterminada | LFM2.5-350M importat | Estable a 516 MB RSS amb prop d’1 GB disponible; triat després d’un error mèdic del 230M |
| Pi 4 de 2 GB, latència mínima | LFM2.5-230M importat | 383 MB RSS i resposta mitjana de 7.2 s; revisa bé el contingut, sobretot en salut o seguretat |
| Pi 4 de 2 GB, només registre | `qwen2.5:0.5b` | Descàrrega directa d’Ollama i estabilitat en la prova Pi 4 de cinc prompts; compliment repetit del 61% a Pi 5 |
| Pi 4 de 4 GB o Pi 5 | LFM2.5-1.2B importat i després prova local | 967 MB RSS i 89% de compliment repetit a la Pi 5 de 8 GB; no vam provar directament les variants de 4 GB |
| Pi 5 de 8 GB, assistent reactiu | LFM2.5-1.2B importat | 15.5 tokens/s, resposta total de 4.7 s i el compliment repetit més alt que vam mesurar |
| Pi 5 de 8 GB, només configuració del registre | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS i 83% de compliment repetit |
| Pi 5 de 8 GB, provar un model de text més gran | Qwen2.5 3B o Llama 3.2 3B quantitzats | Tots dos van funcionar a prop de 5 tokens/s i van usar 2.4–2.8 GB RSS; Qwen2.5 3B va passar 5/6 en una prova única |

Aquestes opcions prioritzen respostes curtes i útils en una Pi que pot executar altres serveis. Són punts de partida, no l’afirmació que un model sigui el millor per a qualsevol tasca. En la prova de compliment d’una sola passada a Pi 5, `qwen3.5:0.8b` i Spark-X2.5 amb raonament predeterminat no van donar respostes conformes; MiniCPM5-1B va obtenir 1/6. Si el client no pot desactivar el raonament, evita’ls per a aquesta càrrega breu. Prova el model final amb el prompt real, el context, la concurrència i el límit de resposta previstos per al desplegament.

Per al model del registre, després d’[instal·lar Ollama per a Linux](https://ollama.com/download/linux), executa:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Prova els teus prompts, la longitud de resposta desitjada i els altres serveis en funcionament. Registra tant el temps total de resposta com l’ús de memòria. Això indica millor que el nombre de paràmetres si el model és adequat per a la teva Pi.

En un node amb memòria limitada, vigila el swap durant les proves. Si un model més gran fa que la placa deixi de respondre, fes servir un model més petit i estableix un límit de memòria adequat per al servei Ollama perquè una càrrega massa gran falli abans d’esgotar la memòria de l’amfitrió. Un límit de servei protegeix el sistema, no fa que hi càpiga un model excessiu. Els reinicis de Pi 4 observats mostren per què la capacitat de resposta i el marge de memòria compten tant com els tokens per segon.

## Converteix el benchmark en una decisió de desplegament

Abans d’instal·lar un model per a ús diari, fixa quatre límits: **temps màxim de resposta, memòria resident màxima, format de resposta i comportament davant errors**. Prova’ls amb els serveis que compartiran la placa. Un model que funciona sol però provoca swap al costat del pont de ràdio o del tauler no compleix els requisits de desplegament.

Mantén instal·lat un model petit de reserva. Canvia-hi si el model principal supera el límit de memòria, retorna una resposta buida o incompleix el contracte de resposta. Registra a cada comparació l’etiqueta del model, la quantització, la versió d’Ollama, el prompt, la longitud del context i la seed perquè una actualització posterior no sembli una millora del maquinari.
