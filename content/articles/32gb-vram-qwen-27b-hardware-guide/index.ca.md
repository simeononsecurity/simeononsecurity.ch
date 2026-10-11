---
title: "32 GB de VRAM per a Qwen 27B: guia de maquinari d'IA local per a l'octubre de 2026"
date: 2026-10-03
lastmod: 2026-10-10
toc: true
draft: false
description: "Guia pràctica d'octubre de 2026 per executar un model Qwen 27B amb 32 GB de memòria utilitzable de l'accelerador. Compara GPU individuals, equips amb dues targetes, memòria unificada, targetes usades de centres de dades, còmput llogat, suport de programari i límits de context complet."
genre: ["IA local", "Maquinari d'IA", "Benchmarking de GPU", "IA autoallotjada", "Maquinari informàtic", "Economia de la IA"]
tags: ["32GB VRAM", "Qwen 27B", "Qwen3.8 27B", "IA local", "guia de compra de GPU", "VRAM", "llama.cpp", "RTX 5090", "RTX 5060 Ti", "Radeon AI PRO R9700", "Intel Arc Pro B70", "Tesla V100", "AMD Instinct MI50", "lloguer de GPU", "context llarg", "KV cache", "multi GPU", "tensor split", "CUDA", "ROCm", "Metal", "memòria unificada", "LLM local", "estació de treball d'IA"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Una estació de treball avançada amb una targeta gràfica i pantalles que mostren dades de rendiment d'un model d'IA local"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/dgx-spark-64gb-memory-crisis-2027"]
---

**Que l'etiqueta del producte indiqui 32 GB no vol dir que hi hagi 32 GB disponibles per a una càrrega Qwen 27B.** El sistema operatiu, el temps d'execució, la memòria cau KV, el format del model, els controladors i la distribució de les targetes canvien el resultat. Una targeta barata amb prou capacitat encara pot perdre clarament en el processament del prompt o en el temps de configuració.

*A l'octubre de 2026, compara la memòria utilitzable i la feina completada per dòlar, no només el nombre de VRAM.*

Aquesta guia presenta maneres pràctiques d'executar un model Qwen 27B amb qualitat de 6 bits i una finestra de context gran. Separa les especificacions publicades dels resultats de proves comunicats, perquè el resultat de tokens per segon d'una persona no és una propietat universal d'una GPU.

## Per què l'objectiu és 32 GB

La necessitat de memòria comença amb els pesos. Un model dens de 27B llegeix tot el conjunt de paràmetres durant la generació. Amb quantificació de 6 bits, els pesos ocupen aproximadament **20,5 GB** abans d'afegir les assignacions d'execució i la memòria de context.

Un context de 128K tokens afegeix una altra assignació gran. La mida exacta de la memòria cau KV depèn de l'arquitectura del model, la precisió de la memòria cau, els paràmetres dels lots i el backend. Una estimació pràctica d'uns **8 GB** situa els pesos i la memòria cau plegats prop dels **28,5 GB** abans que el sistema operatiu i el temps d'execució d'inferència prenguin la seva part.

| Configuració | Què permet |
|---|---|
| **GPU discreta de 24 GB** | Pesos de 4 bits amb menys context, o descàrrega parcial |
| **GPU discreta de 32 GB** | Pesos de 6 bits amb un objectiu útil de context 128K |
| **Dues GPU de 16 GB** | Model dividit amb menys marge per a la sobrecàrrega d'execució |
| **64 GB de memòria unificada** | Més opcions de context i model, subjectes al límit d'assignació de memòria de GPU |

**L'objectiu de 32 GB serveix per dimensionar, no és una garantia.** Un model es pot carregar i deixar massa poc espai per a un prompt llarg, un lot més gran, entrades multimodals o un segon procés.

## El vídeo és una referència de camp útil

El vídeo següent compara les vies principals per arribar a 32 GB per a la IA local. És útil com a referència de preus comunicats, dificultat de configuració i resultats d'execució. Aquest article fa una comparació independent amb especificacions de maquinari, comportament de memòria del model, suport de programari i cost total de propietat.

{{< youtube id="uavLRbbfM94" enable="true" title="Every Ways to Get 32GB VRAM for Local AI at Full Context" description="Comparació de camp de rutes amb una GPU, diverses GPU, memòria unificada, acceleradors usats i lloguer per a càrregues d'IA local de 32 GB." >}}

## La memòria utilitzable guanya a la memòria de la caixa

### Memòria unificada d'Apple

Apple silicon fa servir un grup compartit per a CPU i GPU. Apple ofereix configuracions del Mac mini amb 32 GB de memòria unificada, però tot el grup no és una assignació gràfica dedicada. macOS, l'aplicació i el temps d'execució d'inferència també necessiten espai.

Algunes sessions de llama.cpp indiquen aproximadament **22.906 MB disponibles** en un sistema de 32 GB. Això són prop de **21,3 GiB**, amb poc espai per a un model 27B de 6 bits i una memòria cau KV gran. El límit exacte depèn del sistema operatiu, l'executor del model, la pressió de memòria i les opcions d'inici.

Apple silicon continua sent atractiva per a sistemes silenciosos. llama.cpp tracta Metal com un backend principal, i Apple evita problemes de controladors i energia presents en moltes targetes usades de centres de dades. El compromís és menys rendiment que una GPU discreta de gamma alta i menys marge de memòria previsible.

### Dues targetes de 16 GB

Dues targetes de 16 GB proporcionen 32 GB de VRAM física, però el temps d'execució encara necessita buffers per dispositiu i espai de comunicació. Una targeta pot indicar 13,4 GB en ús i l'altra 14,4 GB. La capacitat restant no és una reserva neta de 4 GB per al context.

El mètode de divisió també importa. **La divisió per capes** assigna capes diferents del model a targetes diferents. Amplia la capacitat, però les targetes recorren el model per torns. **La divisió per tensors** posa el treball d'una mateixa capa en les dues targetes. Augmenta la comunicació, però permet una contribució més directa dels dos dispositius.

| Mètode de divisió | Benefici principal | Cost principal |
|---|---|---|
| **Divisió per capes** | Ampliació senzilla de capacitat | Una targeta sovint espera mentre l'altra treballa |
| **Divisió per tensors** | Millor càlcul paral·lel en algunes càrregues | Més ajustos i més trànsit entre interconnexions |
| **Descàrrega CPU i GPU** | Fa cabre models per damunt de la VRAM total | Gran penalització quan la CPU gestiona capes freqüents |

**Un pla de dues targetes necessita un backend provat abans de comprar.** La generació PCIe, la separació de ranures, l'alimentació, el suport de controladors i la quantificació exacta afecten el resultat.

## Opcions d'una sola targeta

### RTX 5090

NVIDIA llista la RTX 5090 amb **32 GB de GDDR7** i **1.792 GB/s d'amplada de banda de memòria**. Té suport CUDA ampli, eines madures i molts frontends provats. La taula actual de GPU CUDA situa la RTX 5090 en una capacitat de càlcul 12.0.

El problema és el preu. Una 5090 nova ofereix una via clara als 32 GB, però el cost de compra competeix amb mesos de lloguer d'un accelerador. També consumeix fins a **575 W de potència gràfica total**, de manera que el sistema necessita una font i una refrigeració serioses.

### Radeon AI PRO R9700

La R9700 és una opció AMD de 32 GB amb una amplada de banda alta i un preu d'entrada inferior al de la 5090 en molts anuncis. El seu valor depèn molt del temps d'execució. La ruta predeterminada de llama.cpp dona un resultat útil, mentre que un backend comunitari més ràpid dona un resultat molt més alt a la mateixa targeta en algunes proves comunicades.

Aquest és l'exemple més clar de per què una comparació de GPU necessita dues columnes de velocitat. **La velocitat de descodificació** mesura els tokens generats. **La velocitat de preompliment** mesura la rapidesa amb què el backend llegeix el prompt abans del primer token generat. Una base de codi de 50.000 tokens mostra un preompliment feble encara que la descodificació sembli acceptable.

### Intel Arc Pro B70

La Arc Pro B70 s'adreça a càrregues professionals amb 32 GB de memòria. És interessant per capacitat per dòlar, però la ruta de programari necessita més revisió que el maquinari CUDA. El suport GGUF estàndard, les compilacions corregides, els ajustos de draft-token i la maduresa del backend afecten el resultat.

**Un preu de compra més baix no compensa les hores dedicades a trobar una compilació que funcioni.** Per a un aficionat, aquesta feina forma part del projecte. Per a una estació d'ús diari, el suport de controladors i aplicacions té un valor real.

## Targetes usades de centres de dades

### Tesla V100

Les Tesla V100 usades de 32 GB criden l'atenció perquè el preu de la targeta sembla baix. El muntatge complet costa més. Una targeta passiva de centre de dades necessita flux d'aire, xassís o coberta adequats, adaptadors de corrent i un host amb prou espai PCIe.

L'altre problema és l'edat del programari. La taula actual de GPU CUDA se centra en arquitectures noves i no inclou la V100 a la taula actual d'arquitectures. Abans de comprar, cal revisar la versió exacta de CUDA, la branca del controlador, el backend i el fork comunitari.

**Pressuposta un sistema V100 funcional, no una targeta nua.** Una targeta anunciada prop dels 680 dòlars pot convertir-se en un projecte d'uns 1.000 dòlars després de refrigeració, adaptadors i plataforma host. Els preus d'ocasió també pugen quan una càrrega d'IA local popular porta compradors cap al mateix accelerador retirat.

### AMD Instinct MI50

La MI50 ofereix un preu usat atractiu per gigabyte, però el seu suport de programari actual és una limitació seriosa. Una targeta que necessita una pila ROCm antiga o un fork mantingut per la comunitat no equival a una targeta de consum actual amb suport d'aplicacions generalitzat.

La diferència comunicada en el processament del prompt importa més que el preu de l'etiqueta. Una comparació va mesurar uns **128 tokens per segon** en una MI50 contra aproximadament **2.652 tokens per segon** en una targeta més nova de 32 GB per a una càrrega de processament del prompt. Una base de codi de 50.000 tokens trigaria minuts en la ruta lenta i segons en la ràpida abans de començar la generació.

**La MI50 encaixa en un cas d'ús estret.** Serveix a qui prioritza la capacitat per damunt de la velocitat d'interacció i accepta mantenir els controladors. És una mala opció per a l'anàlisi ràpida de bases de codi quan el temps de preompliment importa.

## El programari forma part de la GPU

llama.cpp admet CUDA, HIP, Metal, Vulkan, SYCL i altres backends. També admet inferència híbrida CPU i GPU i l'ús de diverses GPU. Aquestes funcions no donen el mateix rendiment entre proveïdors ni formats de model.

La mateixa targeta física sovint mostra grans diferències entre:

- **Una compilació d'aplicació predeterminada** amb ajustos conservadors.
- **Una compilació ajustada de llama.cpp** amb kernels específics del backend.
- **Un fork comunitari** amb predicció especulativa o de diversos tokens.
- **Un format de model corregit** dissenyat per a una ruta d'accelerador.

Els resultats comunicats en la comparació inclouen uns **27 tokens per segon** per a una ruta AMD predeterminada de 32 GB, uns **46 tokens per segon** amb predicció de diversos tokens i resultats molt més alts en un backend especialitzat. El resultat mostra marge de programari. No és una promesa per a una instal·lació nova.

**Registra el backend, el commit, el fitxer del model, la quantificació, la longitud del context, la longitud del prompt, la mida del lot i l'estat d'energia amb cada benchmark.** Sense aquests camps, tokens per segon és una xifra publicitària.

## Llogar en lloc de comprar

Llogar una GPU ràpida canvia el càlcul. Un preu comunicat de lloguer d'una RTX 5090 prop dels **0,69 dòlars per hora** fa que una compra de 4.400 dòlars equivalgui a unes **6.377 hores de lloguer** abans d'afegir electricitat, maquinari host, manteniment i valor de revenda.

Això s'acosta a nou mesos de lloguer continu o uns dos anys a vuit hores diàries. Un escriptori amb dues targetes d'uns 1.560 dòlars equival a unes 2.261 hores al mateix preu. La 5090 llogada també evita calor, soroll, configuració de controladors i avaries locals.

| Patró d'ús | Primera prova millor |
|---|---|
| **Unes hores per setmana** | Model allotjat o GPU llogada |
| **Projecte curt** | Lloga una targeta de classe 5090 i mesura la càrrega real |
| **Ús interactiu diari** | Compra només després de provar el backend i el context |
| **Agents funcionant tota la nit** | El maquinari propi és més fàcil de justificar |
| **Dades privades amb càrrega estable** | Maquinari propi amb aïllament de xarxa |

**Lloga abans de comprar quan el model, el backend o la longitud de context encara siguin incerts.** Un cap de setmana mesurat costa menys que comprar una estació de treball equivocada.

## Recomanacions de compra

### Dues RTX 5060 Ti de 16 GB

Dues targetes de 16 GB ofereixen una ruta CUDA pràctica per a qui necessita 32 GB i vol tutorials, controladors i frontends habituals. Fes servir la divisió per tensors només després de verificar el format del model i el backend. La divisió per capes és més senzilla, però sovint deixa rendiment sense aprofitar.

Aquesta ruta també necessita una placa base amb dues ranures útils, prou potència i flux d'aire entre les targetes. Una parella de targetes ja no és un muntatge petit quan hi inclous el cost de la plataforma.

### Una targeta de 32 GB

Tria una targeta única de 32 GB quan la fiabilitat, la garantia i un desplegament senzill importin més que el preu de memòria més baix. La R9700 i la RTX 5090 representen opcions diferents. AMD posa l'accent en capacitat i preu. NVIDIA posa l'accent en l'amplitud del programari i el suport CUDA madur.

### Una V100 o MI50 usada

Tria maquinari de centre de dades usat només quan el projecte inclogui proves de controladors, refrigeració i manteniment del backend. El preu de la targeta és la primera línia del pressupost, no l'última.

### Apple silicon

Tria un sistema Apple silicon de 32 GB quan el silenci, el baix consum en repòs i un escriptori compacte importin més que el màxim rendiment. Comprova l'assignació de memòria que indica l'executor exacte abans d'assumir que els 32 GB estan disponibles per al model.

### Lloguer al núvol

Tria lloguer quan la càrrega sigui ocasional, el model canviï sovint o una resposta ràpida al prompt importi més que la propietat local. Atura la instància després de la prova. El temps inactiu elimina ràpidament l'avantatge de preu.

## Una millor fitxa de comparació

Abans de comprar, registra aquests valors per a cada candidat:

- **Memòria de model utilitzable** després de la sobrecàrrega d'execució.
- **Format dels pesos** i mida prevista del model.
- **Mida de la memòria cau KV** a la longitud de context objectiu.
- **Velocitat de preompliment** per a un prompt representatiu.
- **Velocitat de descodificació** quan el context és ple.
- **Versió del backend i del controlador** necessària per al resultat.
- **Consum en repòs i carregat** segons la tarifa elèctrica local.
- **Cost de l'host**, refrigeració, adaptadors, emmagatzematge i garantia.
- **Equivalent de lloguer** per al nombre d'hores que preveus usar el sistema.

La prova més útil fa servir un prompt de la teva càrrega real. Per programar, usa una base de codi representativa. Per investigar, usa un document llarg amb el flux normal de recuperació o enganxat. Mesura el temps fins al primer token, el processament del prompt, la velocitat de generació, l'ús de memòria i la qualitat de sortida.

## Recomanació final

**Compra dues RTX 5060 Ti de 16 GB per a la ruta CUDA de 32 GB amb menys fricció.** Usa una configuració de divisió per tensors només després que una prova curta confirmi el backend.

**Compra una targeta de 32 GB quan necessitis una estació més neta.** Prefereix la targeta amb la ruta de programari més forta per al teu executor, no la targeta amb el valor més baix de dòlars per gigabyte.

**Usa una V100 o MI50 només si acceptes el projecte de manteniment.** Un accelerador barat amb preompliment feble no és una ganga per a prompts llargs de bases de codi.

**Lloga una GPU de classe 5090 quan l'ús sigui irregular.** La prova llogada proporciona dades reals de memòria, velocitat i context abans d'una compra gran.

La pregunta dels 32 GB no és «quina targeta té el gigabyte més barat?». És «quin sistema deixa prou memòria utilitzable, llegeix ràpid la meva càrrega, funciona amb el meu programari i compensa el preu de compra amb un ús regular?»

## Referències

- [Totes les maneres d'obtenir 32 GB de VRAM per a IA local amb context complet](https://www.youtube.com/watch?v=uavLRbbfM94), referència de vídeo per a la comparació de camp anterior.
- [Especificacions de NVIDIA GeForce RTX 5090](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/), detalls oficials de VRAM, amplada de banda, potència i capacitat CUDA.
- [Capacitat de càlcul de GPU CUDA de NVIDIA](https://developer.nvidia.com/cuda/gpus), taula actual d'arquitectures i capacitats.
- [Especificacions tècniques de l'Apple Mac mini](https://www.apple.com/mac-mini/specs/), configuracions oficials de memòria unificada i dades d'amplada de banda.
- [llama.cpp](https://github.com/ggml-org/llama.cpp), backends d'inferència admesos i documentació multi-GPU.
- [Fitxa del model Qwen3.5 27B](https://huggingface.co/Qwen/Qwen3.5-27B), referència oficial per a la família 27B actual i el comportament de context llarg.
- [IA local el 2026: un model 27B supera Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), anàlisi relacionada de models i maquinari local.
- [Benchmarks de GPU de Llama 3.1 8B i Qwen3.8 27B a Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), anàlisi relacionada de GPU llogada.
- [El DGX Spark de 64 GB és un senyal d'alerta per als preus del maquinari d'IA local](/articles/dgx-spark-64gb-memory-crisis-2027/), anàlisi relacionada de capacitat i oferta.

## Passos següents

Fes servir la fitxa amb un prompt representatiu abans de comprar. Compara el temps fins al primer token, el processament del prompt, la descodificació, la memòria, la potència i el cost total de la plataforma. Per a un projecte curt, lloga primer i conserva el resultat mesurat amb la decisió de compra.
