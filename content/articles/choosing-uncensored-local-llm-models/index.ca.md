---
title: "Com triar un model local d’IA sense censura"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Compara variants locals segons les respostes completes, les capacitats conservades, l’ús del context, la quantització i la VRAM necessària."
genre: ["IA local", "IA autoallotjada", "Seguretat de la IA", "Maquinari GPU"]
tags: ["IA local sense censura", "abliteració", "LLM local", "VRAM", "longitud del context", "quantització", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Estació de treball local d’IA amb una targeta gràfica i monitors que mostren visualitzacions de models i inferència"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Tria del model:** avalua cada variant segons les respostes útils que completa, la qualitat que conserva i la memòria que necessita la teva càrrega de treball. Un nombre baix de denegacions o una fitxa de model popular no demostren aquests resultats.

L’etiqueta **sense censura** no té una escala de rendiment estàndard. Els editors de models la fan servir per descriure modificacions diferents dels pesos, ajustos fins i plantilles de conversa. Compara cada candidat amb el model original i prova’l amb les tasques que preveus executar.

{{< youtube id="j-VqPVjztJE" enable="true" title="He provat tots els models locals d’IA sense censura (de 8 GB a 32 GB de VRAM)" description="Comparació de variants de models locals, respostes completes, ajustos de context i nivells de memòria GPU." >}}

## Què t’indica l’etiqueta

Un **model abliterat** ha rebut modificacions als pesos per canviar alguns comportaments de denegació. L’article de 2024 sobre la direcció de denegació va demostrar un mètode en 13 models de conversa oberts. Les eines més recents ofereixen altres mètodes. Per exemple, Heretic 2 documenta tant l’ablació de rang arbitrari com l’ablació direccional. L’etiqueta de la fitxa del model no indica quin comportament ha canviat ni què ha afectat la modificació.

Separa aquestes quatre propietats quan comparis models:

| Propietat | Què cal comprovar |
|---|---|
| **Comportament de denegació** | Quines sol·licituds reben una denegació, una resposta parcial o una resposta completa? |
| **Conservació de capacitats** | Com es comparen les tasques de coneixement, raonament, programació i format amb el model original? |
| **Compleció de la resposta** | Amb quina freqüència la generació acaba abans del límit de tokens o de temps? |
| **Adequació al motor d’execució** | El fitxer quantitzat exacte funciona amb prou memòria per al context que necessites? |

Un model modificat continua sent probabilístic. **Separa les comprovacions de qualitat:** exactitud, fiabilitat i ús segur. Mantén disponible un model alineat de manera habitual per a les tasques en què les seves proteccions siguin importants.

## Per què el nombre de denegacions és un indicador feble

**Una puntuació de denegació** mesura un resultat en un conjunt d’indicacions. Diu poca cosa sobre l’exactitud factual, la llargada de les respostes o si el model produeix una resposta final abans d’esgotar el pressupost de generació.

**La comparació de Qwen3.8-27B de Sapwell, del setembre de 2026,** va provar el model base i vuit variants amb la mateixa configuració de servei. El conjunt de 13 tasques mesurava coneixement, matemàtiques, programació i veracitat. Un conjunt de HarmBench separat contenia 400 sol·licituds nocives, i un jutge LLM va revisar les respostes completes. Aquests resultats corresponen a una família de models, una GPU i un disseny d’avaluació.

| Variant de Qwen3.8-27B de l’estudi | Denegacions explícites de 400 | Respostes amb el raonament inacabat |
|---|---:|---:|
| **Model base** | 381 | 0% |
| **OrcaRouter** | 2 | 38% |
| **Trohrbaugh** | 122 | 15% |

L’elevat nombre de denegacions del model base coincidia amb menys resultats inacabats. El nombre baix de denegacions d’OrcaRouter coincidia amb una proporció més alta de respostes incompletes. Trohrbaugh va conservar més denegacions i va tenir menys respostes incompletes. **Tria segons la teva tasca i els compromisos que acceptis.**

**Un estudi de 23 variants de Gemma 4 E4B** va trobar pèrdues importants en algunes mesures de capacitat de la variant més descarregada, mentre que una modificació menor es mantenia a prop del model base en les proves. La popularitat i les descàrregues descriuen l’adopció. No mesuren la qualitat.

No combinis aquestes mesures en una única puntuació. **Separa les mesures:** denegació, compleció, correcció i latència. Anota també el conjunt d’indicacions, la revisió del model, la plantilla de conversa, el motor d’execució, el context i el límit de sortida. Canviar qualsevol d’aquests ajustos canvia el significat de la comparació.

## Diagnostica les respostes buides abans de substituir un model

**Els tokens de raonament** compten dins del límit de sortida abans que aparegui text visible. Si el límit s’esgota durant el raonament intern, alguns motors retornen una resposta buida o truncada. Aquest resultat és diferent d’una denegació o d’una resposta completa però incorrecta.

**El benchmark de Qwen3.6-27B de Sapwell** va mostrar com això afecta les puntuacions principals. Les puntuacions matemàtiques sense processar variaven molt perquè algunes execucions no arribaven a una resposta final. Entre les respostes completes, els valors d’exactitud mesurats eren molt més propers. El benchmark separava la capacitat de respondre de l’esgotament del pressupost de raonament.

**Quan una resposta sigui buida, comprova el motiu d’aturada i els registres del motor.** Anota la llargada de la indicació, l’assignació del context, el límit de tokens de sortida, el temps transcorregut i si el model ha generat un marcador de resposta final. Després repeteix la indicació amb un límit de sortida més alt si el maquinari té espai disponible.

| Resultat | Categoria probable que cal investigar |
|---|---|
| **Text de denegació** | El model ha rebutjat la sol·licitud. |
| **Sortida buida en arribar al límit de tokens** | La generació ha esgotat el pressupost de sortida abans d’una resposta final. |
| **Sortida truncada** | El límit de generació ha aturat una resposta incompleta. |
| **Error del motor** | Ha fallat el servidor, el fitxer del model o l’assignació de memòria. |
| **Resposta completa però incorrecta** | El model ha retornat text, però no ha superat la comprovació de correcció. |

**Sortida buida:** confirma el resultat del motor abans de considerar cada cas un defecte del model. Una finestra de context més gran no resol automàticament un límit de sortida petit, una plantilla mal formada o un temps d’espera de l’aplicació esgotat.

## Reserva VRAM per als pesos i el context

El fitxer del model és només un consumidor de memòria. El motor també necessita espai per a la **memòria cau KV**, que desa l’estat d’atenció de la indicació i la resposta actives, a més dels buffers de càlcul i altres processos carregats. Augmentar la llargada del context incrementa l’ús de memòria.

**La documentació actual d’Ollama** indica finestres de context predeterminades de 4K amb menys de 24 GiB de VRAM, de 32K entre 24 i 48 GiB i de 256K amb 48 GiB o més. Aquests valors descriuen el comportament predeterminat del motor. Comprova el context assignat i la ubicació del processador amb `ollama ps`.

**Exemple per a Linux:** aquesta ordre estableix 16K com a valor predeterminat per a les noves sessions del servidor Ollama:

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Comprova el context assignat** en relació amb les mides habituals d’entrada i resposta amb el model carregat:

```bash
ollama ps
```

Les columnes `CONTEXT` i `PROCESSOR` mostren l’assignació i si el model s’executa a la GPU o s’ha descarregat parcialment. **Assignació del context:** un límit indicat no garanteix que tota la finestra càpiga a la VRAM.

### Punts de partida segons la memòria de la GPU

**Candidats inicials:** aquestes famílies de models van aparèixer en comparacions de variants de 2026. Les mides dels fitxers provenen de repositoris quantitzats concrets. Confirma el fitxer exacte, la compatibilitat amb el motor i la memòria mesurada abans de considerar que un candidat s’hi adiu.

| Memòria GPU | Candidat inicial | Restricció principal |
|---|---|---|
| **8 GB** | Gemma 4 E4B, com ara la variant `coder3101` | Manté petit el fitxer dels pesos. Deixa memòria per al context i els buffers del motor. |
| **12 GB** | Gemma 4 12B, com ara el fitxer GGUF Q4 de 7,4 GB de `TrevorJS` | Ofereix més capacitat al model, però menys espai per a un context llarg que una variant més petita. |
| **16 GB** | Un model més petit o un fitxer Q3 de Qwen3.8-27B | El repositori de Qwen indica 13,72 GB per a Q3_K_S. El seu editor qualifica aquest fitxer de baixa qualitat. L’espai per al context serà limitat. |
| **24 GB** | Qwen3.8-27B Q4_K_S o Q4_K_M | El repositori actual indica fitxers de 16,71 GB i 17,77 GB. Reserva espai per a la memòria cau i els buffers. |
| **32 GB** | Qwen3.8-27B Q6_K | El repositori actual indica un fitxer de 23,46 GB. Un fitxer més gran deixa menys memòria per al context que una quantització més petita. |

*Fes servir aquestes opcions com a punt de partida. Els repositoris i les versions canvien, i la mida del fitxer, per si sola, no prediu l’assignació de memòria del motor ni la qualitat de les respostes.*

Les etiquetes de quantització GGUF resumeixen una opció de codificació. **Diferències entre repositoris:** els fitxers amb la mateixa profunditat de bits nominal no garanteixen una qualitat equivalent. Un repositori de Qwen etiqueta Q3_K_S com a baixa qualitat i Q4_K_M com a opció predeterminada. Abans de baixar-los, comprova la mida exacta, la fitxa del model, el format de les indicacions i els resultats de les proves.

**Per dimensionar la memòria cau i comprovar l’ajust a una GPU local,** consulta la [guia de models locals, GPU i context](/articles/local-ai-model-gpu-context-guide/). Les recomanacions se centren en tasques de programació. Aquesta pàgina se centra en el comportament de denegació modificat i l’avaluació.

## Inspecciona la plantilla de conversa i l’origen del model

Una **plantilla de conversa** embolcalla els missatges amb els tokens i les instruccions que espera el model. Un paquet del model pot incloure una plantilla personalitzada o una instrucció de sistema. Aquests canvis afecten el comportament mesurat encara que els pesos subjacents no canviïn.

**Efecte de la plantilla:** Sapwell va trobar una variant de Qwen3.8 el paquet de la qual incloïa una personalitat que indicava al model que no denegués ni advertís mai. La seva afirmació sobre poques denegacions depenia de la plantilla. La comparació va uniformitzar les plantilles perquè la prova se centrés en les diferències entre els pesos. Aquest control no demostra que la plantilla proporcionada sigui maliciosa o inutilitzable.

**Abans d’instal·lar:** verifica l’editor, el model base, la llicència, el procés de conversió, el quantitzador, la plantilla i l’historial de revisions. Compara’l amb el model original amb la mateixa plantilla i el mateix motor. Si la fitxa del model no descriu el mètode o la configuració de la prova, registra l’origen com a desconegut.

## Executa una avaluació breu per a la teva càrrega de treball

**Prepara un conjunt repetible d’indicacions** amb tasques habituals que siguin teves o que tinguis permís per provar. Inclou la feina que farà el model, preguntes factuals amb respostes conegudes i peticions de format amb criteris de superació clars. Afegeix uns quants casos límit segurs perquè el comportament de denegació també formi part de la decisió.

**Mantén constants els ajustos de prova** entre el model original i la variant modificada. No canviïs la instrucció de sistema, la plantilla, la quantització, la versió del motor, el context, el límit de sortida ni els ajustos de mostreig. Desa la revisió del model o l’empremta del fitxer amb els resultats.

Registra cada resultat per separat:

- **Compleció:** resposta final, denegació, sortida buida, truncament o error del motor.
- **Correcció:** superació o fallada segons la resposta esperada o una rúbrica.
- **Utilitat:** si la resposta satisfà els requisits de la tasca.
- **Latència:** temps fins al primer token i temps total de generació.
- **Memòria:** context assignat, ubicació a la GPU i VRAM màxima.
- **Comportament de seguretat:** denegació o continuació adequades per a cada cas límit.

Repeteix el conjunt després de canviar una variable. Si la resposta es completa en augmentar el límit de sortida, la primera fallada es devia al pressupost. Si les respostes continuen incompletes, revisa la plantilla del model, el mode de raonament, el motor i la revisió del model. **Conserva la variant només si millora la tasca objectiu sense pèrdues inacceptables d’exactitud o seguretat.**

## Mantén el desplegament aïllat

**Privadesa:** la inferència local depèn de tota la teva pila. Revisa la interfície, els registres, les extensions, la telemetria i les rutes de xarxa. Tracta els pesos no fiables i les plantilles personalitzades com a codi i configuració de tercers.

**Accés públic:** no exposis mai directament el punt final del model a Internet. Aïlla l’accés a les eines i fes servir variants modificades només per a tasques autoritzades. Per a l’accés remot, col·loca el punt final darrere d’una passarel·la privada amb autenticació, límits de peticions i aïllament de xarxa. L’article original sobre la direcció de denegació assenyala les implicacions de seguretat de les modificacions que eliminen denegacions.

## Conclusió

**Regla de decisió:** tria el model amb els resultats verificats més sòlids per al teu conjunt de tasques. Fes servir el nombre de denegacions com una mesura i després comprova la compleció de les respostes, la correcció, el comportament de la plantilla i el marge de VRAM. Comença amb un fitxer adequat per a la teva GPU, estableix el context per a la teva càrrega de treball i compara’l amb el model original amb els mateixos ajustos.

**Per dimensionar la GPU,** compara aquests resultats amb el [benchmark de lloguer de GPU per a Qwen 27B](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Lloga o demana maquinari abans de comprar-lo si no tens clar el fitxer de model o el context objectiu.

## Fonts

- [Benchmark d’abliteració de Qwen3.8-27B](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6 de setembre de 2026.
- [Benchmark d’abliteració de Qwen3.6-27B](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmark de variants de Gemma 4 E4B](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1 d’agost de 2026.
- [Benchmark de variants de Gemma 4 12B](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28 d’agost de 2026.
- [La denegació en els models lingüístics està mediada per una sola direcció](https://arxiv.org/abs/2406.11717), Arditi i altres, 2024.
- [Documentació del projecte Heretic](https://github.com/p-e-w/heretic/).
- [Fitxa oficial del model Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Documentació d’Ollama sobre la llargada del context](https://docs.ollama.com/context-length).
- [Fitxa del model Gemma 4 E4B `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [Fitxers GGUF de Gemma 4 12B de TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [Fitxers GGUF d’OrcaRouter Qwen3.8-27B](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [Format GGUF i tipus de quantització](https://huggingface.co/docs/hub/en/gguf), documentació de Hugging Face.
- [Font en vídeo: He provat tots els models locals d’IA sense censura (de 8 GB a 32 GB de VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).
