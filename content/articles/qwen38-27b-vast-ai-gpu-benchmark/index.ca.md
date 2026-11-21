---
title: "Proves de GPU de Llama 3.1 8B i Qwen3.8 27B a Vast.ai"
date: 2026-10-02
lastmod: 2026-11-20
toc: true
draft: false
description: "Compara els resultats mesurats d'Ollama per a Llama 3.1 8B i Qwen3.8 27B en GPU de Vast.ai, amb costos i opcions d'allotjament."
genre: ["IA local", "Proves de GPU", "IA allotjada pròpiament", "Computació al núvol", "Intel·ligència artificial", "Economia de la IA"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "prova de GPU", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "LLM local", "context llarg", "lloguer de GPU", "IA allotjada pròpiament", "models sense refusos", "models sense censura", "crèdits d'API", "subscripció d'IA", "Q4_K_M", "tokens per segon"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Espai de treball d'alta tecnologia amb una targeta gràfica i pantalles que mostren resultats de proves d'IA local"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**L'H100 SXM va ser la targeta més ràpida en les dues proves amb Ollama, però no va oferir la millor relació qualitat-preu.** La RTX PRO 5000 i la RTX 6000 Ada van equilibrar millor la velocitat i el cost de lloguer. La CMP 170HX va tenir la tarifa horària més baixa entre les proves completades de Qwen3.8 27B.

*Aquests resultats mesuren un model, una capa d'Ollama, la quantització predeterminada i una sola forma de servei. Fes-los servir per dimensionar aquesta càrrega, no com una classificació universal de GPU.*

Aquest article compara **Llama 3.1:8b**, una compilació Q4_K_M d'Ollama amb 8.03B paràmetres, amb **Qwen3.8:27b**, una compilació Q4_K_M d'Ollama amb uns 27.3B paràmetres. Hem provat tots dos en instàncies de GPU llogades a Vast.ai. Les proves se centren en el cabal de descodificació amb longituds reals de sol·licitud, fins al límit de context admès.

## Resposta breu

**Lloga una RTX PRO 5000 o una RTX 6000 Ada per a un ús habitual d'una sola persona.** La RTX PRO 5000 va oferir el millor valor amb contextos curts i mitjans. La RTX 6000 Ada costava menys i mantenia un avantatge útil davant les A100. Lloga una H100 SXM si la rapidesa de resposta importa més que el preu per hora o si fas servir sol·licituds llargues.

| Objectiu | Recomanació | Motiu |
|---|---|---|
| **Cost de prova més baix** | CMP 170HX | $0.420 per hora i prou VRAM per als models Q4_K_M provats |
| **Millor valor per sota de $1.25/hr** | RTX PRO 5000 o RTX 6000 Ada | Bona velocitat de descodificació sense pagar el lloguer d'una H100 |
| **Respostes més ràpides** | H100 SXM | La velocitat de descodificació més alta en les dues proves |
| **Qwen amb context llarg** | H100 SXM o RTX PRO 6000 Max-Q | Totes dues van completar la prova Qwen d'uns 131k tokens amb marge ampli de VRAM |
| **Model de referència popular de 8B** | Llama 3.1:8b | Comparació pràctica de 8B amb un límit de context de 128K |
| **Càrrega recurrent petita** | Crèdits d'API o subscripció de xat | Sense cost per una GPU aturada, manteniment ni feina de desplegament |
| **Càrrega privada i freqüent** | Estació de treball pròpia amb GPU | Amb un ús sostingut és més fàcil justificar el cost del maquinari |
| **Proves de models sense refusos o censura** | Lloga primer i compra només després d'un ús sostingut | Abans de comprar maquinari convé provar el comportament, la llicència i el risc operatiu |

## Què hem provat

**La prova ha fet servir Ollama amb la compilació Q4_K_M predeterminada del model.** No hi hem afegit quantització especial, descodificació especulativa, samplers personalitzats ni cap altra pila de servei. L'objectiu era comparar de manera senzilla i reproduïble les instàncies de GPU.

Vast.ai descriu el servei com un mercat de GPU al núvol que connecta proveïdors de computació i usuaris. La documentació enumera opcions sota demanda, reservades, interrompibles i sense servidor, amb filtres per model de GPU, memòria, preu i disponibilitat. Les tarifes horàries següents corresponen a les instàncies triades durant aquesta sessió, no a una llista de preus permanent de Vast.ai.

La mesura és el **cabal de descodificació**, expressat en tokens generats per segon. El cabal de preompliment es mostra per separat perquè descriu el processament de la sol·licitud, no la velocitat amb què apareix la resposta. Una sol·licitud llarga pot trigar força a processar-se encara que la descodificació sigui ràpida.

Hem fet dues proves vàlides per context i n'hem calculat la mediana de descodificació. Els nivells completats es basen en els valors reals de prompt_eval_count:

- **Uns 16.4k tokens de sol·licitud**
- **Uns 32.8k tokens de sol·licitud**
- **Uns 65.5k tokens de sol·licitud**
- **Uns 131k tokens de sol·licitud**

La prova sol·licitada de 256k tokens no es va completar. Les A100 de 40 GB i diverses targetes més petites encara processaven la sol·licitud o no van arribar a la longitud de context prevista.

> **Límit de la prova:** Les xifres descriuen dues càrregues Q4_K_M d'Ollama amb una sola forma de servei. No prediuen la velocitat d'entrenament, el cabal amb diversos usuaris, la generació d'imatges, el rendiment de vLLM ni el resultat d'un altre model.

## Nova prova de Llama 3.1 8B

**Llama 3.1:8b és una referència pràctica útil per al mateix grup de GPU.** Ollama indica uns 120 milions de descàrregues, cosa que el converteix en una opció raonable per a una segona prova basada en popularitat. La [pàgina oficial del model a Ollama](https://ollama.com/library/llama3.1:8b) indica una compilació Q4_K_M de 4.9 GB, 8.03B paràmetres i una finestra de context de 128K.

La nova prova ha fet servir un executor específic per al model i un generador de sol·licituds calibrat amb el tokenitzador d'Ollama. Les etiquetes següents mostren els recomptes reals, no els contextos demanats:

- **Uns 32,676 tokens reals** per a l'objectiu de 32k
- **Uns 65,342 tokens reals** per a l'objectiu de 64k
- **Uns 130,671 tokens reals** per a l'objectiu de 128k

El nivell de 256k no és compatible amb Llama 3.1 8B perquè el límit de context indicat és de 128K. L'executor ara gestiona reintents i mostra files d'estat, de manera que els temps d'espera es veuen en lloc de desaparèixer de la taula.

### Resultats de Llama 3.1 8B

| GPU | Descodificació ~32k tokens/s | Descodificació ~64k tokens/s | Descodificació ~128k tokens/s |
|---|---:|---:|---:|
| **H100 SXM** | **163.5** | **124.0** | **82.4** |
| **H100 SXM** | **158.6** | **121.2** | **80.6** |
| **RTX PRO 5000** | 110.1 | 79.8 | 49.9 |
| **CMP 170HX 64GB** | 91.9 | 71.0 | 50.1 |
| **RTX 6000 Ada** | 88.3 | 53.9 | 29.3 |
| **RTX PRO 6000 Max-Q** | 66.7 | 53.0 | 40.3 |
| **RTX PRO 6000 S** | 60.3 | 42.5 | 33.9 |
| **A100 SXM4 40GB** | 2.0 | 40.6 | 38.5 |
| **A100 PCIe 40GB** | 1.2 | 20.3 | 20.3 |
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Temps esgotat |

Les dues files H100 corresponen a instàncies vàlides separades de la mateixa classe de GPU. Totes dues van superar clarament les altres targetes. A 32k van ser entre un 44% i un 48% més ràpides que la RTX PRO 5000, i a 128k entre un 61% i un 65% més ràpides.

Els resultats de 32k de les A100 i de la RTX 5060 Ti són massa baixos per representar una execució comparable en GPU per a aquesta càrrega. L'amfitrió amb la RTX 5060 Ti també va esgotar el temps durant la segona prova de 128k. Considera'l inadequat per comparar el cabal real de GPU, no pas un resultat vàlid de classificació.

| Objectiu de context | Estat |
|---|---|
| **32k** | Completat als 10 amfitrions |
| **64k** | Completat als 10 amfitrions |
| **128k** | Completat a 9 amfitrions. El de 2x RTX 5060 Ti va esgotar el temps a la segona prova |
| **256k** | No admès a cap amfitrió, perquè Llama 3.1 8B admet fins a 128K de context |

## Comparació dels dos models

**El Llama més petit va ser més ràpid en totes les GPU comparables, però la mida i la qualitat del model són coses diferents.** Llama 3.1 8B és una referència popular que demana menys memòria. Qwen3.8 27B necessita més memòria i ofereix un perfil de capacitats diferent. Fes servir les xifres per triar maquinari, no per afirmar que un model sempre és millor.

| Cas d'ús | Referència més adequada | Motiu |
|---|---|---|
| **Assistent ràpid de 8B** | Llama 3.1:8b | Més velocitat de descodificació i menys memòria per al model |
| **Dimensionar un model local de 27B** | Qwen3.8:27b | S'assembla més a una càrrega gran en una sola GPU |
| **Límit de context de 128K** | Llama 3.1:8b | Té un límit explícit de 128K, així que 256k no és un objectiu vàlid |
| **Provar el marge de VRAM** | Qwen3.8:27b | El model més gran mostra abans els límits de memòria i de context llarg |
| **Referència entre proveïdors** | Llama 3.1:8b | La popularitat i la mida faciliten repetir el resultat |

La prova anterior de Qwen també va corregir els recomptes reals de sol·licitud a uns **32,770**, **65,538** i **131,074** tokens en els nivells de context admesos. Fes servir aquestes etiquetes corregides en lloc dels valors num_ctx sol·licitats quan comparis proves de Qwen.

## Uns 16k tokens

**L'H100 SXM va liderar la prova de context curt amb 134.4 tokens de descodificació per segon.** La RTX PRO 5000 la va seguir amb 113.9 tokens per segon i costava menys de la meitat per hora.

| Posició | GPU | VRAM | Descodificació tokens/s | Preompliment tokens/s | Tarifa de lloguer |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

Amb aquesta longitud, la RTX PRO 5000 va oferir aproximadament el 84.7% de la velocitat de descodificació de l'H100 per un 37.3% de la tarifa horària. La RTX 6000 Ada va oferir el 66.3% de la velocitat de l'H100 per un 30.2% del cost horari.

## Uns 32.8k tokens

**La classificació es va mantenir estable amb el context mitjà.** L'H100 SXM va baixar a 120.0 tokens per segon, la RTX PRO 5000 en va assolir 105.0 i la RTX 6000 Ada, 75.7.

| Posició | GPU | VRAM | Descodificació tokens/s | Preompliment tokens/s | Tarifa de lloguer |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

La RTX PRO 5000 continuava sent el lloguer més atractiu del grup. Només era un 12.5% més lenta que l'H100 i costava un 62.7% menys per hora.

## Uns 65.5k tokens

**Les sol·licituds llargues van fer més visible la diferència entre les targetes amb molta memòria i les que tenen menys marge.** L'H100 es va mantenir primera amb 112.0 tokens per segon. La RTX PRO 6000 Max-Q va superar la RTX 6000 Ada en velocitat de descodificació.

| Posició | GPU | VRAM | Descodificació tokens/s | Preompliment tokens/s | Tarifa de lloguer |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | N/D | N/D | $0.565/hr |

La RTX PRO 5000 encara oferia el millor equilibri entre els resultats completats. La RTX 6000 Ada era més lenta, però el preu de lloguer més baix l'afavoria quan la disponibilitat importa més que la velocitat màxima.

## Uns 131k tokens

**L'H100 va ser l'única targeta per sobre de 100 tokens de descodificació per segon amb aquest context.** La RTX PRO 6000 Max-Q va completar la prova a 73.4 tokens per segon, seguida de la RTX 6000 Ada a 61.7.

| Posició | GPU | VRAM | Descodificació tokens/s | Preompliment tokens/s | Tarifa de lloguer |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | N/D | N/D | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | N/D | N/D | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | N/D | N/D | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | N/D | N/D | $0.565/hr |

La RTX PRO 6000 Max-Q és l'alternativa pràctica a l'H100 amb sol·licituds llargues. Va assolir el 67.8% de la velocitat de descodificació de l'H100 al 56.0% del preu horari. La RTX 6000 Ada costava menys, però els seus 48 GB de VRAM deixen menys marge per a sol·licituds llargues, lots grans o una altra configuració de model.

## Comparació general de descodificació

| GPU | ~16k | ~32.8k | ~65.5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | N/D |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | N/D |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | N/D |
| **A100 PCIe** | 38.4 | 36.1 | N/D | N/D |

**L'H100 va liderar tots els contextos completats.** El seu avantatge sobre la RTX PRO 5000 va baixar de 20.5 tokens per segon amb uns 16k tokens a 12.0 amb uns 32.8k. El millor valor depèn de si necessites la resposta inicial més ràpida o el cost més baix en una sessió llarga.

## Cost per milió de tokens descodificats

**El preu horari per si sol amaga una comparació útil.** Dividir la tarifa per hora pel cabal de descodificació dona una estimació del cost de lloguer per generar un milió de tokens. No inclou el processament de sol·licituds, el temps inactiu, l'emmagatzematge, la transferència de dades, els impostos, els descomptes ni les proves fallides o interrompudes.

| GPU | Tarifa amb context curt | Cost aproximat per 1M de tokens descodificats |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**La CMP 170HX va guanyar aquesta comparació aritmètica limitada.** La RTX PRO 5000 i la RTX 6000 Ada van quedar a prop i totes dues oferien més cabal que la CMP 170HX. En un ús interactiu, l'espera sovint importa més que el cost mínim per token.

## Llogar, comprar crèdits, subscriure's o comprar maquinari?

**L'opció adequada depèn de la freqüència d'ús i del control que necessitis.** Llogar una GPU és una despesa variable de computació. Els crèdits d'API són una despesa variable de model. Una subscripció de xat és una quota fixa d'accés amb límits d'ús. Comprar maquinari és una inversió inicial, seguida d'electricitat, refrigeració, manteniment i depreciació.

| Pressupost mensual i càrrega | Opció recomanada | Motiu | Principal renúncia |
|---|---|---|---|
| **Menys de $10** | Compra crèdits d'API o fes servir un model local gratuït | Valida el flux de treball sense pagar una GPU aturada | Menys control sobre l'allotjament del model i els límits de peticions |
| **De $10 a $30** | Crèdits d'API per a ús ocasional o subscripció de xat per a ús interactiu diari | La subscripció encaixa amb el xat; els crèdits, amb scripts i peticions mesurades | Cap de les dues opcions dona per defecte un punt final privat de 27B |
| **De $30 a $100** | Lloga una RTX 6000 Ada o RTX PRO 5000 només durant les sessions actives | Cobreix períodes curts de recerca i evita les despeses de propietat | Cal configurar, emmagatzemar, supervisar i apagar bé la instància |
| **De $100 a $250** | Lloga una targeta ràpida per a tasques programades o prova un pla d'estació pròpia | L'ús mensual sostingut comença a mostrar el valor de la utilització | Canvien la disponibilitat i les tarifes horàries |
| **De $250 a $600** | Compara un mes de lloguer de RTX PRO 5000 amb una GPU local nova o usada | És el punt de decisió per a inferència privada freqüent | El maquinari afegeix riscos d'energia, calor, assistència i revenda |
| **Més de $600** | Compra maquinari només amb molta utilització o reserva lloguer de classe H100 per a pics | Un model mixt evita tenir maquinari car per a una demanda esporàdica | El capital queda vinculat a una sola configuració |

Aquests trams orienten la decisió, no són pressupostos dels proveïdors. Les tarifes de la prova mostren el punt d'equilibri: una H100 a $2.693 per hora costa uns $64.63 per un dia continu de 24 hores i uns $1,941.00 per 30 dies, abans d'emmagatzematge o altres càrrecs. Una RTX PRO 5000 a $1.005 per hora costa uns $24.12 per dia i $723.60 per 30 dies continus. El total d'una GPU llogada només per a sessions actives és diferent del d'una GPU en marxa tot el mes.

### Quan convé comprar crèdits d'API

**Els crèdits d'API convenen quan l'ús és irregular, l'automatització és important i la tasca no exigeix un model local concret.** Eviten preparar la GPU, descarregar models, resoldre problemes de controladors i pagar hores inactives. També permeten comparar diversos models allotjats abans d'invertir en maquinari.

Els preus d'API varien segons el model i el proveïdor. El catàleg de models d'OpenRouter serveix per comparar longituds de context, proveïdors i preus per token. Consulta la calculadora actual del proveïdor abans de comparar una factura d'API amb aquesta prova. Una GPU local genera tokens sense una tarifa per token del proveïdor, però l'hora de lloguer continua mentre la instància espera.

### Quan convé una subscripció

**Una subscripció és adequada per a qui fa servir cada dia un assistent allotjat.** Els plans individuals actuals de Claude, per exemple, separen l'accés gratuït, Pro i Max amb diferents límits i funcions. Una subscripció no és el mateix que l'accés a l'API. Sovint ofereix una interfície polida i eines agrupades, mentre que els crèdits d'API permeten control programàtic.

Tria una subscripció si la feina és sobretot escriptura interactiva, recerca, programació o revisió de fitxers. Tria crèdits d'API si un script, una aplicació o un agent necessita un punt final amb consum mesurat.

### Quan convé Vast.ai

**Vast.ai és adequada si necessites un model obert, control privat de l'entorn o un pic breu de cabal alt.** Tria la GPU, inicia una instància, executa Ollama, prova el model i apaga-la en acabar. És una bona opció per a Qwen3.8 27B, variants sense refusos i altres fitxers de model massa grans per a un portàtil de consum.

El cost és la feina operativa. Has de confirmar que el model fa servir la GPU, vigilar la VRAM, protegir el servei exposat, conservar els fitxers de model necessaris i aturar la instància després de la prova. Una tarifa horària baixa no compensa oblidar-se d'una instància en marxa.

### Quan convé comprar una GPU

**Comprar maquinari convé quan l'ús és sostingut, les necessitats del model són estables i cal control local.** La compra elimina el risc de disponibilitat del lloguer i et dona un entorn persistent. També permet tractar dades privades sense enviar les sol·licituds a un proveïdor allotjat.

El preu de compra és només una part de la factura. Afegeix-hi el sistema amfitrió, la font d'alimentació, l'emmagatzematge, la refrigeració, l'electricitat, el risc de substitució i el temps de configuració. Una targeta de gamma alta també pot estar aturada quan els crèdits d'API o una subscripció costarien menys.

Les especificacions de referència de NVIDIA per a la RTX 4090 indiquen 24 GB de memòria, 450 W de potència gràfica total i una recomanació mínima de 850 W per al sistema. És una referència útil per a inferència local, però els 24 GB queden per sota de les configuracions Q4_K_M de 27B provades aquí. Comprova la memòria real que fa servir el model en lloc de suposar que una targeta hi cap només pel nombre de paràmetres.

## Models sense refusos ni censura

**Les variants sense refusos o censura canvien la decisió de compra.** Sovint atreuen perquè es neguen menys o tenen menys restriccions integrades. També poden tenir una seguretat més feble, procedència incerta, formats de sol·licitud inconsistents, més necessitats de revisió i límits de llicència o ús acceptable.

Amb aquests models, lloga abans de comprar. Una prova d'un dia amb RTX PRO 5000 a la tarifa indicada costa uns $24.12 abans d'altres càrrecs. N'hi ha prou per confirmar l'encaix del model, l'ús de GPU, la qualitat de les respostes i el risc operatiu.

**No exposis directament un model sense censura a Internet.** Posa-hi al davant autenticació, límits de peticions, controls de registre i aïllament de xarxa. No hi enviïs dades personals, confidencials o regulades a un model que no hagis revisat.

Si el model esdevé una eina diària, compara el lloguer mensual amb el cost complet d'una estació pròpia. Si l'ús és esporàdic, el lloguer continua sent més fàcil d'aturar i substituir.

## Advertiments sobre la prova

**Els resultats absents també formen part del resultat.** Un valor N/D vol dir que l'execució no va donar una mesura vàlida. No vol dir que la GPU sigui tan lenta com suggereix la puntuació d'una altra targeta.

- **La segona instància H100 no va produir un conjunt de proves vàlid** perquè la descàrrega del model va acabar massa tard.
- **La instància de 2x RTX 5060 Ti es va excloure** perquè Ollama va carregar el model a la CPU en lloc de fer servir les GPU.
- **La sol·licitud de 256k tokens de Qwen3.8 27B no es va completar.** El nivell vàlid més alt va ser d'uns 131k tokens reals. Llama 3.1 8B indica que 256k no és admès perquè el seu límit de context és de 128K.
- **No s'ha fet servir num_ctx com a etiqueta de classificació.** Les taules finals fan servir els valors reals de prompt_eval_count.
- **S'ha resumit la mediana de descodificació de dues proves vàlides per context.** Això redueix l'efecte d'una prova lenta, però no substitueix una mostra més gran.
- **La capa de servei era senzilla expressament.** Un desplegament ajustat de vLLM o llama.cpp donarà una classificació diferent.

## Recomanació final

**Comença llogant una RTX 6000 Ada o una RTX PRO 5000.** La RTX 6000 Ada és l'opció econòmica quan està disponible a $0.813 per hora. La RTX PRO 5000 ofereix més velocitat per sota del preu d'una H100. Fes servir una H100 SXM per a sol·licituds llargues, latència interactiva exigent o una finestra breu de prova en què el temps importi més que el cost. Per a un model de 8B, val la pena provar una CMP 170HX si importa més pagar menys per hora que obtenir la velocitat màxima.

**No compris una GPU després d'una sola prova reeixida.** Lloga-la durant un mes de càrregues reals, registra les hores actives, les longituds de sol·licitud, la concurrència i els canvis de model, i compara el total amb el cost complet de propietat. Compra maquinari quan la càrrega sigui prou freqüent per mantenir la targeta ocupada i prou estable per justificar menys flexibilitat.

Per a usos ocasionals, els crèdits d'API o una subscripció de xat són més simples. Per a inferència local privada, proves de models oberts o models sense refusos, Vast.ai ofereix una opció amb menys compromís que comprar una estació de treball immediatament. Fes servir Llama 3.1 8B com a referència de menys memòria i Qwen3.8 27B quan el model més gran sigui l'objectiu real del desplegament.

## Passos següents

Repeteix la comparació amb les teves longituds de sol·licitud i una estimació de les hores actives. Verifica l'ús de GPU, registra la revisió del model i la versió de l'entorn, atura la instància després de cada prova i compara el lloguer mensual amb el cost total de propietat abans de comprar maquinari.

## Referències

1. [Mercat de GPU al núvol de Vast.ai](https://vast.ai/)
2. [Documentació de Vast.ai: mercat, instàncies, preus i tipus de lloguer](https://docs.vast.ai/)
3. [Catàleg de models Qwen3 d'Ollama](https://ollama.com/library/qwen3)
4. [Pàgina del model Llama 3.1 8B d'Ollama](https://ollama.com/library/llama3.1:8b)
5. [Catàleg de models d'OpenRouter i comparació de preus](https://openrouter.ai/models)
6. [Preus de Claude i plans de subscripció individuals](https://www.anthropic.com/pricing)
7. [Especificacions de NVIDIA GeForce RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [IA local el 2026: Qwen3.8 27B i maquinari per allotjar models](/articles/local-ai-2026-build-your-rig-now/)
9. [Proves de models Ollama amb maquinari Raspberry Pi](/articles/ai-models-raspberry-pi-4-5/)
