---
title: "Quin model d'IA local hauries d'executar? Guia de GPU, context i programació per a l'octubre de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Guia pràctica d'octubre de 2026 per triar models d'IA locals per a agents de programació. Compara la memòria de GPU, el creixement de la KV-cache, la mida del context, la qualitat de la quantització, el processament de prompts, la configuració del raonament i el cost del lloguer al núvol."
genre: ["IA local", "Maquinari d'IA", "IA autogestionada", "Benchmarking de GPU", "Eines per a desenvolupadors", "Economia de la IA"]
tags: ["models d'IA locals", "agents de programació", "guia de GPU", "VRAM", "KV cache", "finestra de context", "Qwen 27B", "mescla d'experts", "quantització", "llama.cpp", "Ollama", "decodificació especulativa", "predicció de diversos tokens", "LLM local", "lloguer de GPU", "estació de treball d'IA", "programació amb agents", "processament de prompts", "velocitat d'inferència"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Una estació de treball que mostra opcions de models d'IA locals, ús de memòria de GPU i finestres de context d'agents de programació"
coverCaption: ""
ref: ["/articles/32gb-vram-qwen-27b-hardware-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/local-ai-2026-build-your-rig-now"]
---

**El millor model local per programar és el que manté prou part del teu projecte en memòria i el llegeix prou ràpid per continuar sent útil.** La mida del model continua important, però un model que només encaixa després de passar dades a la RAM del sistema sovint funciona pitjor que un model més petit amb una finestra de context estable.

*Tria el model i el pressupost de memòria alhora. No triïs un model d'una llista de nivells i l'obliguis a funcionar en maquinari inadequat.*

Aquesta guia se centra en agents de programació, no en prompts curts d'autocompletat. Un agent llegeix fitxers, sortida d'eines, errors del compilador i resultats de proves abans d'escriure una solució. Aquestes entrades consumeixen context, i el context canvia la decisió sobre el maquinari.

## El vídeo és una referència

El vídeo següent compara models locals en diversos nivells de memòria de GPU. És útil per les seves observacions pràctiques sobre la selecció de models i els resultats de maquinari que presenta. Aquest article segueix un camí separat i organitza la decisió al voltant del comportament de la memòria, el context de l'agent, el processament de prompts i el cost total de propietat.

{{< youtube id="C9M6iUFtVB4" enable="true" title="I Tested Every Local AI Model So You Don't Have To" description="Comparació pràctica de models d'IA locals en diversos nivells de memòria de GPU, amb atenció a les càrregues de programació i als límits del maquinari." >}}

## Per què fallen les llistes de nivells

Una llista de nivells sol relacionar el nombre de paràmetres amb una xifra de memòria de GPU. El mètode serveix per a una primera estimació. Deixa de servir quan un agent de programació comença a llegir un repositori real.

Els pesos del model són la primera assignació. La **KV cache** és l'assignació que creix. Desa les claus i els valors d'atenció del context actiu perquè el temps d'execució no hagi de recalcular tot el prompt després de cada token generat.

| Consumidor de memòria | Què conté | Per què importa |
|---|---|---|
| **Pesos del model** | Els paràmetres quantitzats | Requisit de càrrega única |
| **KV cache** | Notes del context actiu | Creix amb el prompt i la conversa |
| **Buffers del temps d'execució** | Espai temporal de càlcul | Varia segons el backend i la mida del lot |
| **Instruccions de l'agent** | Prompts del sistema i definicions d'eines | Usa context abans que arribin els fitxers del projecte |

**Que el fitxer del model encaixi a la targeta no demostra que l'agent sigui usable.** El temps d'execució necessita espai per a la cache, els buffers temporals, les definicions d'eines i la resposta següent.

## El context és el pressupost real

Els agents de programació gasten context en més coses que els fitxers font. El pressupost també inclou instruccions del sistema, esquemes d'eines, llistats de directoris, sortida del shell, missatges del compilador, resultats de proves i torns anteriors de conversa.

Tres connexions MCP amb definicions d'eines detallades sovint consumeixen diversos milers de tokens abans que l'agent obri un fitxer del projecte. Un context per defecte petit deixa poc espai per al codi. L'agent continua responent, però perd el conjunt de treball necessari per a reparacions de diversos passos.

Les [preguntes freqüents del temps d'execució d'Ollama](https://docs.ollama.com/faq) indiquen un context per defecte de 4,096 tokens. `OLLAMA_CONTEXT_LENGTH` canvia el valor per defecte, mentre que `OLLAMA_NUM_PARALLEL` escala la memòria necessària amb el nombre de peticions simultànies. Anota tots dos valors abans de comparar un benchmark local amb un resultat d'una sola petició.

```bash
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_NUM_PARALLEL=1 ollama serve
```

Aquest exemple estableix un valor per defecte de 32K per a una petició activa. No reserva 32K tokens per als fitxers del projecte. Les instruccions, les definicions d'eines, l'entrada i la sortida comparteixen la finestra.

### Un registre de context senzill

Abans de comparar GPU, registra aquests valors:

- **Mida del projecte:** fitxers i nombre aproximat de línies font en una tasca normal.
- **Sobrecàrrega de les eines:** prompt del sistema, esquemes MCP, eines de shell i instruccions de l'editor.
- **Càrrega de l'error:** longitud normal de la sortida del compilador i de les proves.
- **Context objectiu:** el prompt més gran que vols mantenir sense truncament.
- **Marge de resposta:** espai reservat per al pedaç i l'explicació previstos.

Fes servir el resultat com una especificació de càrrega de treball. Un desenvolupador que edita un fitxer cada vegada té una necessitat de memòria diferent d'un desenvolupador que demana a un agent rastrejar una API en un monorepositori.

## La KV Cache canvia la classificació

Dos models amb un nombre de paràmetres semblant sovint tenen costos de context diferents. Un model dens amb totes les capes contribuint a la cache creixent sol necessitar més memòria que un model amb una arquitectura d'atenció híbrida.

Un model de programació de 27B tractat en el material de referència usa un conjunt limitat de capes d'atenció completa, mentre que les altres capes usen un resum de mida fixa. El cost de context de 128K indicat es manté per sota de 9GB per a la cache. Un model de mida semblant amb atenció completa creixent a totes les capes necessita, segons l'informe, més de 21GB amb la mateixa longitud de context.

Aquestes xifres descriuen arquitectures de models i configuracions de temps d'execució concretes. Tracta-les com un motiu per inspeccionar l'arquitectura, no com una fórmula universal de memòria.

| Comportament del model | Efecte sobre el context | Implicació per al maquinari |
|---|---|---|
| **Atenció completa a cada capa** | Gran creixement de la cache | Necessita més memòria per a prompts llargs |
| **Atenció híbrida o lliscant** | Menor creixement de la cache en algunes capes | Més marge de context amb la mateixa mida de model |
| **Mescla d'experts** | Menys paràmetres actius per token | Menys càlcul per token, però cal emmagatzemar tots els pesos |
| **Extensió de context llarg** | Finestra de treball més gran | Més memòria de cache i més treball de processament del prompt |

**Llegeix l'arquitectura del model abans de comprar memòria.** El nombre de paràmetres per si sol amaga el cost d'una sessió de programació llarga.

## Tria segons el nivell de memòria de GPU

### De quatre a vuit GB

Els models densos petits continuen sent l'opció pràctica. Encaixen a la targeta, responen ràpid i funcionen bé per a autocompletat, explicacions curtes i edicions de fitxers concrets.

Un model més gran amb offload a CPU pot generar text, però el temps de resposta sovint es converteix en el límit. Un agent de programació necessita lectures de fitxers i crides a eines repetides. Una configuració de quatre tokens per segon converteix cada reparació en una espera llarga, encara que el model funcioni tècnicament.

Els models de mescla d'experts ofereixen un altre camí. Una part activa petita redueix la pressió de càlcul, mentre que el conjunt complet de pesos viu parcialment a la memòria del sistema. Aquest enfocament recompensa un sistema amb molta RAM i rutes de transferència ràpides.

| Càrrega de treball | Direcció suggerida |
|---|---|
| **Autocompletat** | Model dens petit amb prompt curt |
| **Edicions d'un sol fitxer** | Model instruct petit amb suport d'eines |
| **Agent de tot el repositori** | Lloga una GPU més gran o augmenta primer la memòria del sistema |
| **Codi privat sota un NDA** | Usa un model local, però accepta un abast més petit o execucions més lentes |

**En aquest nivell, compra RAM del sistema abans de perseguir un model gran.** Un model petit estable supera un model gran que passa la major part del temps movent dades pel bus.

### De dotze a setze GB

Aquest nivell obre la porta a un model de programació de 27B, però la quantització es torna central. Una compilació estàndard de 4 bits propera als 17GB no encaixa en una targeta de 16GB quan s'afegeix la sobrecàrrega del temps d'execució.

Una compilació de 3 bits propera als 13GB deixa més espai per al context. Una targeta de 12GB empeny cap a una compilació de 2 bits o un model de mescla d'experts més petit. La qualitat depèn del quantitzador concret i del procés de calibratge, de manera que dues càrregues amb la mateixa profunditat de bits sovint donen resultats de programació diferents.

Comprova aquests punts abans de baixar un model quantitzat:

- **Autor del quantitzador i notes de la versió**
- **Dades de calibratge i resultats d'avaluació**
- **Compatibilitat del tokenitzador**
- **Proves de crida a eines**
- **Longitud de context amb la quantització triada**
- **Suport del temps d'execució a Ollama, llama.cpp o la interfície escollida**

**No tractis «2-bit» o «3-bit» com una descripció completa de qualitat.** El mètode d'empaquetatge i el registre de calibratge importen.

### De vint-i-quatre a trenta-dos GB

Aquest és el rang més flexible per a un model de programació de 27B. Una targeta de 24GB sol encaixar una compilació de 4 bits amb un context útil, però una finestra completa de 128K pot superar la memòria restant. Una targeta de 32GB dona més espai al temps d'execució per a la cache i les assignacions temporals.

Aquest rang també facilita justificar la propietat. Una GPU gestiona la càrrega sense la complexitat de dividir-la entre dues targetes. El sistema usa menys energia que una construcció amb diverses GPU, i el suport de programari és més fàcil de provar.

| Capacitat | Posició pràctica |
|---|---|
| **24GB** | Model de 4 bits fort amb límits de context que cal mesurar |
| **32GB** | Model de 4 o 6 bits de 27B amb més marge de context |
| **48GB** | Més precisió o cache més gran sense canviar el model principal |

**El rang de 24GB a 32GB és la zona lògica de propietat per a programació privada freqüent.** Evita el pitjor comportament d'offload sense obligar a posar maquinari de centre de dades en una caixa d'escriptori.

### Quaranta-vuit GB o més

Més memòria no implica automàticament un model nou. El mateix model de 27B pot funcionar amb precisió de 8 bits en una targeta de 48GB, amb una cache més gran i menys concessions. La millora és la consistència, l'espai de context i la qualitat de sortida, no un nivell nou de raonament.

A 128GB, la decisió canvia. Es fa possible un model de mescla d'experts molt més gran, però el processament del prompt es converteix en una preocupació seriosa. Un model sovint genera ràpid, però tarda molt a ingerir un repositori gran o un resultat d'eina nou.

**Per als models grans, mesura per separat la velocitat de preompliment i la de decodificació.** Una resposta ràpida després d'una lectura lenta del prompt continua sent lenta en un flux de treball d'agent.

## La velocitat de decodificació és només la meitat de la prova

La **velocitat de decodificació** mesura els tokens generats per segon. Respon: «A quina velocitat escriu el model?» La **velocitat de preompliment** mesura el processament del prompt. Respon: «A quina velocitat llegeix el model?»

Un agent passa bona part del temps llegint. Cada crida a una eina afegeix text nou. Un fitxer font llarg, un rastre de pila o un registre de proves entra al prompt abans que comenci la resposta següent.

| Mètrica | Experiència d'usuari |
|---|---|
| **Tokens de decodificació per segon** | Amb quina rapidesa apareix la resposta després del processament |
| **Tokens de prompt per segon** | Quant espera l'agent abans que comenci la resposta |
| **Temps fins al primer token** | Retard combinat del processament del prompt i la configuració |
| **Retenció del context** | Quanta informació del projecte continua disponible durant la tasca |

**Fes benchmarks amb les teves mides de prompt.** Un prompt sintètic curt amaga el cost que més importa durant el treball amb repositoris.

## Primer, les configuracions gratuïtes del temps d'execució

Les actualitzacions de maquinari no són el primer pas de rendiment. Prova les configuracions del temps d'execució abans d'obrir una pàgina de compra.

### Predicció de diversos tokens

Algunes combinacions de models i backends poden predir diversos tokens futurs i verificar-los en una sola passada. La funció sovint apareix com un indicador de temps d'execució o una configuració d'esborrany compatible.

Les proves indicades al material de referència mostren grans guanys en algunes targetes de gamma alta. Els resultats varien segons el fitxer del model, el backend, el controlador i la targeta. Les rutes d'Apple Metal poden no conservar la funció necessària durant la conversió.

### Nivell de raonament

Un model amb el raonament màxim activat dedica més temps al treball intern abans de tornar un resultat. El raonament mitjà sovint ofereix un equilibri millor per a reparar codi, sobretot quan la tasca ja inclou un missatge d'error clar i un fitxer objectiu concret.

Fes servir una matriu de prova senzilla:

1. Executa la mateixa tasca de correcció d'errors amb raonament baix, mitjà i alt.
2. Registra el temps fins al primer token, el temps total, l'èxit del pedaç i el resultat de la prova.
3. Repeteix amb un prompt curt i un prompt de mida de repositori.
4. Conserva la configuració que produeix la millor tasca acabada, no la taxa de tokens més alta.

**El raonament mitjà amb una ruta compatible de diversos tokens és un bon punt de partida.** Verifica la qualitat amb el teu codi abans de fer-lo predeterminat.

## Maquinari local o GPU de lloguer?

El càlcul de lloguer guanya per al treball ocasional. Pagues per sessions actives en lloc de comprar, refredar, actualitzar i alimentar una targeta tot l'any.

El maquinari propi guanya quan la càrrega és freqüent, privada o fora de línia. També elimina la cua i ofereix un entorn estable per a proves repetibles.

| Situació | Millor primer pas |
|---|---|
| **Unes poques sessions al mes** | Lloga una GPU o usa una API |
| **Programació privada diària** | Compra un sistema compatible de 24GB a 32GB |
| **Repositori gran amb recàrregues freqüents** | Lloga primer i mesura la velocitat de preompliment |
| **El codi no surt de l'edifici** | Compra el sistema més petit que compleixi l'objectiu de context |
| **Experimentar amb un model nou** | Lloga abans de comprar maquinari |

Calcula el punt d'equilibri amb hores actives, no amb hores del calendari. Inclou electricitat, emmagatzematge, refrigeració, manteniment i el temps necessari per mantenir funcionant el temps d'execució.

**Una GPU de gamma alta comprada per experimentar de tant en tant és una despesa d'afició.** Un sistema de 24GB a 32GB usat cada dia per a treball privat té un argument econòmic més fort.

## Una millor llista de compra

Segueix aquest ordre quan comparis un model i una GPU:

1. **Defineix la tasca.** Autocompletat, reparació d'un fitxer, agent de repositori o anàlisi de context llarg.
2. **Mesura el prompt.** Compta instruccions normals del sistema, esquemes d'eines, fitxers i sortida de proves.
3. **Inspecciona el comportament de la cache.** Busca notes de l'arquitectura i mesures de memòria de context.
4. **Tria una quantització.** Comprova els resultats de qualitat de la càrrega concreta, no només el nombre de bits.
5. **Prova el preompliment i la decodificació.** Usa prompts del teu repositori.
6. **Ajusta el raonament.** Compara el temps de tasca acabada en diversos nivells de raonament.
7. **Prova la privadesa i el manteniment.** Confirma on viatja el codi font i qui manté el backend.
8. **Compara el cost de lloguer.** Usa les hores actives previstes i inclou l'energia en l'estimació del sistema propi.

## Recomanació final

**Per sota de 12GB, executa un model més petit o un model de mescla d'experts amb prou RAM de sistema.** No obliguis un model dens de 27B a funcionar en una configuració que passa la major part del temps fent offload.

**De 12GB a 16GB, centra't en la qualitat de la quantització i en un objectiu de context controlat.** Una compilació de 2 o 3 bits ben provada i amb suport d'eines és més útil que un fitxer de 4 bits que mai encaixa netament.

**De 24GB a 32GB, un model de programació de 27B es converteix en el valor per defecte pràctic per al treball privat diari.** Mesura l'ús de context i la velocitat del prompt abans d'assumir que la finestra anunciada completa està disponible.

**A partir de 48GB, dedica la memòria extra a precisió, espai de cache i sessions estables abans de passar a un model més gran.** Quan el model entra en territori de 128GB, la velocitat de lectura del prompt i l'economia del lloguer mereixen més atenció que la capacitat bruta.

El nom del model només és el punt de partida. La pregunta útil és quant context del projecte queda després que el model, el temps d'execució, les eines i la cache n'agafin la seva part.

## Lectures relacionades

- [32GB de VRAM per a Qwen 27B: guia de maquinari d'IA local](/articles/32gb-vram-qwen-27b-hardware-guide/), centrada en camins de maquinari per a una càrrega de 27B.
- [Benchmarks de GPU de Llama 3.1 8B i Qwen3.8 27B a Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), resultats mesurats de GPU llogades i límits de context llarg.
- [IA local el 2026: un model de 27B supera Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), qualitat del model, quantització i economia del maquinari local.
