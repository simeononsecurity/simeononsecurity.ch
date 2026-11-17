---
title: "AI locale nel 2026: un modello 27B supera Sonnet 4.6 mentre la finestra hardware si chiude"
date: 2026-09-22
lastmod: 2026-11-14
toc: true
draft: false
description: "Pianifica un sistema AI locale per il 2026 in base a dimensioni del modello, VRAM, banda di memoria, potenza, costo e opzioni di aggiornamento."
genre: ["AI locale", "AI self-hosted", "Modelli a pesi aperti", "Hardware AI", "Apprendimento automatico", "Quantizzazione", "Laboratorio domestico", "Riservatezza", "Economia dell'AI", "Hardware consumer"]
tags: ["ai locale", "eseguire llm in locale", "qwen3.8", "qwen3.8 27b", "bonsai 2 27b", "ternary bonsai", "prism ml", "quantizzazione ternaria", "quantizzazione a 1.58 bit", "quantizzazione llm", "claude sonnet 4.6", "sonnet 4.6 contro modello locale", "pesi aperti", "modello moe", "miscela di esperti", "ollama", "llama.cpp", "rtx 5090", "vram", "inferenza locale", "prezzi gpu 2026", "carenza dram", "prezzi della memoria", "assemblare un pc ai", "ai per homelab", "costo abbonamento ai", "openrouter", "artificial analysis", "guida all'acquisto gpu", "llm self-hosted", "ai rispettosa della privacy", "hardware ai 2026"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Una postazione high-tech con una scheda grafica e diversi schermi luminosi che mostrano benchmark e visualizzazioni AI, su uno sfondo blu navy."
coverCaption: ""
ref: ["/articles/ai-models-raspberry-pi-4-5", "/articles/building-a-privacy-preserving-meshtastic-ai-assistant"]
---

**Un modello scaricabile che entra in una singola scheda grafica consumer supera ora un modello API all’avanguardia nell'indice complessivo di intelligenza.** Qwen3.8 27B è un modello multimodale di visione e linguaggio con pesi aperti, pubblicato nell'agosto 2026. La sua ripacchettizzazione ternaria, Bonsai 2 27B, comprime gli stessi pesi in 5.53 GiB. Insieme segnano il momento in cui l'inferenza locale ha smesso di essere un compromesso da appassionati ed è diventata una valida alternativa a un'API a pagamento.

*La finestra per acquistare hardware si sta chiudendo rapidamente. La memoria non è mai stata così costosa negli ultimi vent'anni e i suoi prezzi stanno trascinando verso l'alto anche quelli delle schede grafiche.*

Questo articolo spiega cosa mostrano i benchmark, cosa distingue i due modelli, dove il modello aperto perde ancora e perché i prossimi dodici mesi non sono il momento giusto per aspettare.

**Cosa otterrai:** scegli un modello e una capacità di memoria in base al tuo carico di lavoro. Prima di acquistare, confronta costo dell'hardware, energia, dimensione del contesto e throughput misurato. Il confronto tra benchmark non predice la qualità sul tuo compito né il prezzo futuro della GPU.

## La risposta breve

**Il divario di intelligenza tra un modello locale 27B e un'API a pagamento vicina ai modelli all’avanguardia si è chiuso. I vantaggi residui del modello a pagamento sono più ridotti di quanto suggerisca la differenza di prezzo.**

Sono cambiate tre cose insieme:

- **I modelli aperti 27B hanno raggiunto punteggi vicini ai modelli di punta.** Qwen3.8 27B ottiene 33.7 nell'Intelligence Index contro 30.1 di Sonnet 4.6, sulla stessa suite di valutazione.
- **La quantizzazione ternaria ha ridotto il fabbisogno di memoria di circa due terzi.** Bonsai 2 27B esegue il modello 27B completo in **5.53 GiB**, una capacità disponibile su schede da poche centinaia di dollari.
- **La disponibilità di memoria è peggiorata.** Nel primo trimestre 2026 i prezzi contrattuali della DRAM convenzionale sono aumentati del **90-95 percento** rispetto al trimestre precedente. È il maggior rincaro trimestrale registrato da TrendForce e ha spostato le GPU di nuova generazione al 2028.

*Acquistare o assemblare ora costa meno. Non è una promozione, sono i dati sull'offerta.*

## Guarda la dimostrazione con una sola GPU

L'affermazione qui sopra merita una dimostrazione, non una tabella. Bijan Bowen ha provato Bonsai 2 27B su un sistema con una sola GPU e si è chiesto se oggi sia il miglior modello disponibile per una singola scheda.

{{< youtube id="OA5cICIzD-c" enable="true" title="Primo test di Bonsai 2 27B: è davvero il MIGLIOR modello AI per una singola GPU?" description="Una prima prova del modello ternario Bonsai 2 27B su una singola GPU consumer, con attenzione a velocità, qualità e alternative." >}}

*Valuta la qualità dell'output, non il numero di token al secondo. La velocità è la parte più facile da migliorare.*

## Due nomi, un solo modello

I due modelli da conoscere non sono concorrenti. **Sono gli stessi pesi a due livelli di precisione diversi.**

| | Qwen3.8 27B | Bonsai 2 27B ternario |
|---|---|---|
| **Che cos'è** | Il modello originale Qwen a pesi aperti | Una ripacchettizzazione ternaria di Qwen3.8-27B realizzata da Prism ML |
| **Pesi su disco** | **18 GB** | **5.53 GiB** (PTQ1_0) oppure **6.70 GiB** (PQ2_0) |
| **Parametri** | 27B densi | 26.90B, stessa architettura |
| **Contesto** | 256K | 262,144 token |
| **Visione** | Sì, nativa | Sì, pacchetto separato con proiettore CLIP |
| **Uso degli strumenti** | Sì | Sì |
| **Licenza** | Apache 2.0 | Apache 2.0 |
| **Ambiente di esecuzione** | Ollama, llama.cpp, MLX | Solo **il fork llama.cpp di Prism ML** |

La pagina della libreria Ollama per `qwen3.8` indica che il modello 27B occupa **18 GB**, supporta una finestra di contesto 256K, la visione e l'uso di strumenti, e offre una build MLX separata per Apple Silicon. La ripacchettizzazione ternaria disponibile su Ollama è una copia dei pacchetti GGUF Apache-2.0 di Prism ML, ripubblicata con checksum corrispondenti.

**La domanda pratica non è quale modello scegliere.** È quanta memoria vuoi spendere per la stessa intelligenza. La versione ternaria ne usa circa un terzo e rinuncia a poco.

{{< figure src="local-ai-architecture-comparison.webp" alt="Diagramma che confronta l'ingombro in memoria dello stesso modello 27B: 18 GB a precisione standard contro 5.53 GiB con pesi ternari, entrambi adatti a una GPU consumer" >}}

## Confronto dei risultati

Artificial Analysis valuta entrambi i modelli con la stessa suite. Conviene leggere i risultati riga per riga invece di riassumerli, perché i due modelli eccellono in aree diverse.

| Misura | Qwen3.8 27B | Claude Sonnet 4.6 | Primo |
|---|---|---|---|
| **Intelligence Index** | **33.7** | 30.1 | Aperto |
| **Coding Index** | **68.1** | 63.0 | Aperto |
| **Agentic Index** | **45.8** | 31.8 | Aperto |
| **GPQA Diamond** | **90.5%** | 87.5% | Aperto |
| **Humanity's Last Exam** | **33.9%** | 33.6% | Aperto |
| **AA-LCR (contesto lungo)** | **82.0%** | 80.0% | Aperto |
| **GDPval-AA** | **45.4%** | 36.0% | Aperto |
| **CritPt (fisica di ricerca)** | **5.4%** | 3.1% | Aperto |
| **Tasso senza allucinazioni** | **69.7%** | 51.6% | Aperto |
| **SciCode** | 46.6% | **50.1%** | Sonnet |
| **Accuratezza AA-Omniscience** | 15.6% | **40.9%** | Sonnet |

*Il modello aperto guida nove delle undici righe confrontabili, compresi tutti gli indici complessivi.*

### Dove prevale il modello aperto

I tre indici complessivi riassumono il risultato. **Intelligence 33.7 contro 30.1, Coding 68.1 contro 63.0, Agentic 45.8 contro 31.8.** Il divario nell'indice agentico è il più ampio. Conta soprattutto per chi esegue flussi di lavoro automatici in più passaggi anziché prompt singoli.

Per dare un riferimento percentilico, Artificial Analysis colloca Qwen3.8 27B **sopra l'86 percento dei modelli** nell'indice agentico e sopra il 76 percento in quello di programmazione. Sonnet 4.6 si ferma rispettivamente al 68 e 72 percento. Nel ragionamento scientifico di livello universitario avanzato, il modello aperto ottiene **90.5 percento** in GPQA Diamond.

### Dove Sonnet 4.6 mantiene il vantaggio

Due risultati vanno nella direzione opposta, ed entrambi contano.

**AA-Omniscience misura se un modello risponde correttamente alle domande di conoscenza al primo tentativo. Sonnet 4.6 raggiunge il 40.9 percento contro il 15.6 percento.** È un divario ampio nell'affidabilità fattuale e l'argomento singolo più forte per pagare un modello premium.

Il dato sulle risposte senza allucinazioni richiede attenzione. Il 69.7 percento di Qwen contro il 51.6 percento di Sonnet sembra una vittoria netta e, preso da solo, lo è. Ma la metrica indica la quota di risposte *non corrette* che evita di inventare informazioni. Un modello meno accurato produce più risposte non corrette, quindi le percentuali descrivono popolazioni diverse e non sono direttamente confrontabili. **Leggi prima la riga sull'accuratezza.**

Sonnet ottiene anche il 50.1 percento in SciCode contro il 46.6 percento e riporta risultati in due valutazioni che la scheda del modello aperto non elenca: IFBench e Terminal-Bench Hard. Non è possibile confrontarli.

### Due precisazioni corrette

**Le date di rilascio sono distanti sei mesi.** Sonnet 4.6 è uscito a febbraio 2026. Qwen3.8 27B è uscito ad agosto 2026. Un modello di punta di febbraio contro un modello aperto di agosto non è un confronto alla pari.

**Sonnet 4.6 non è più il modello di punta di Anthropic.** Sonnet 5 e Opus 5 si trovano ora più in alto nella gamma. Il 27B aperto ha raggiunto un modello di punta della metà del 2026, non l'attuale vertice. Chi sostiene il contrario legge troppo nei dati.

*I test comparativi misurano le prestazioni nei test comparativi. Conta solo il punteggio ottenuto dal tuo carico di lavoro.*

## Cosa cambia con i pesi ternari

Bonsai 2 non è un modello più piccolo. È lo stesso modello da 26.90B a una precisione numerica molto inferiore, e i metadati GGUF pubblicati rendono esplicito il compromesso.

| Proprietà | Valore |
|---|---|
| **Architettura** | `qwen35`, attenzione ibrida con attenzione completa ogni quattro livelli e livelli state-space |
| **Parametri** | 26.90B |
| **Blocchi** | 64 |
| **Ampiezza embedding** | 5120 |
| **Attenzione** | 24 teste query, 4 teste KV, lunghezza key/value 256 |
| **Contesto** | 262,144 token, base RoPE 1e7 |
| **Formato dei pesi** | Ternario, gruppo 128. PQ2_0 a 2.13 bit per peso, PTQ1_0 a 1.75 |
| **Torre visiva** | CLIP, 460.73M parametri, distribuita in un pacchetto proiettore separato |
| **Licenza** | Apache 2.0 |

**Con i pesi ternari ogni parametro assume uno di tre valori invece di sedici.** È questa compressione che permette al modello 27B completo di stare in 5.53 GiB anziché in 18 GB.

### Velocità di elaborazione misurata

Test eseguito con `llama-bench` su una RTX 5090 da 32 GB, tutti i livelli trasferiti sulla GPU, flash attention attiva e media di tre esecuzioni:

| Pacchetto | Pesi | Prefill (pp512) | Decodifica (tg128) |
|---|---|---|---|
| **PQ2_0** | 6.70 GiB | **3802.74 tok/s** | **135.41 tok/s** |
| **PTQ1_0** | 5.53 GiB | 1876.31 tok/s | 131.41 tok/s |

PQ2_0 esegue il prefill **2.03 volte più velocemente** di PTQ1_0, mentre la decodifica è statisticamente equivalente. Perciò PQ2_0 è la scelta predefinita sensata. PTQ1_0 serve quando l'ultimo 1.2 GiB fa la differenza. Con `llama-server` e contesto 65K, la decodifica ha mantenuto **136.5 tok/s** su una singola richiesta in streaming.

**La velocità di decodifica si nota nell'uso quotidiano.** 135 token generati in un secondo superano ampiamente la velocità di lettura. La latenza non è il motivo per eseguire inferenza in locale, perché un'API ospitata è già abbastanza veloce. I motivi sono costo, privacy e controllo.

### La trappola di cui nessuno parla

**Ollama standard non riesce a caricare questi file.** I kernel ternari si trovano nel fork llama.cpp di Prism ML. La verifica con Ollama 0.34.2 fallisce con `unsupported tensor "output.weight" size overflows`. Il runtime riconosce l'architettura `qwen35`, ma le sue librerie non contengono `pq2_0` né `ptq1_0` e non includono un runtime di attivazione Hadamard.

C'è un'altra trappola da conoscere prima di perderci una serata. **Il pacchetto F16 di questa famiglia sembra un ripiego sicuro, ma non lo è.** I tensori sono normali F16 e F32, quindi il file viene letto e caricato senza errori, ma poi genera testo incoerente. I pesi usano una base ruotata dichiarata nei metadati `prism.hadamard.*`. Un runtime deve applicare la rotazione corrispondente oppure produce risultati senza senso. Inoltre, con 50.1 GiB, il pacchetto F16 non può essere trasferito completamente su una scheda da 32 GB.

*Leggi la scheda del modello prima di scaricarlo. Una copia della community non è una build supportata, e questa pagina lo dice chiaramente.*

## L'ondata MoE dietro tutto questo

I modelli densi 27B raccontano solo metà della storia. I modelli mixture-of-experts attivano una piccola parte dei parametri per token e cambiano di nuovo i costi.

| Modello | Totale / attivi | Contesto | Nota |
|---|---|---|---|
| **Qwen3.8 2.4T A95B** | 2.4T / 95B | 1.0M | Modello a pesi aperti imparentato con Qwen3.8 Max |
| **Qwen3.6 35B A3B** | 35B / 3B | 262K | Apache 2.0, MoE sparso ibrido |
| **Qwen3 Coder Next** | 80B / 3B | 256K | Pesi aperti, progettato per agenti di programmazione sempre attivi |

**Qwen3 Coder Next è il modello da seguire per il lavoro locale.** Ha 80B parametri totali e ne attiva solo 3B per token. È pensato per agenti sempre attivi nei CLI e negli IDE. Un modello che attiva 3B parametri genera alla velocità di un modello 3B, sfruttando le capacità memorizzate in 80B. Le note del progetto indicano prestazioni paragonabili a modelli con una quantità di calcolo attiva da 10 a 20 volte superiore.

*Il modello denso 27B è la scelta sicura oggi. La curva di efficienza dei modelli sparsi continua a migliorare.*

{{< figure src="local-ai-moe-dense-tradeoff.webp" alt="Grafico che confronta un modello denso 27B che attiva tutti i parametri per token con un modello mixture-of-experts sparso che ne attiva solo 3 miliardi su 80 miliardi" >}}

## Si chiude la finestra per acquistare componenti

Questa parte della storia ha una scadenza.

L'inferenza locale è diventata economica proprio quando la memoria necessaria ha iniziato a costare di più. Le due tendenze stanno per scontrarsi e l'effetto si vede già nei prezzi al dettaglio.

### Cosa è successo ai prezzi della memoria

**Nel primo trimestre 2026 i prezzi contrattuali della DRAM convenzionale sono cresciuti del 90-95 percento rispetto al trimestre precedente**, il maggior incremento trimestrale mai registrato da TrendForce. La memoria flash NAND è salita del 55-60 percento nello stesso periodo.

La pressione non è diminuita. Secondo TrendForce, nel secondo trimestre la DRAM è aumentata di un altro **58-63 percento** e la NAND del 70-75 percento. Anche la moderazione del terzo trimestre, con la DRAM in rialzo del 13-18 percento e la NAND del 10-15 percento, si somma a due trimestri record anziché rappresentare un sollievo.

La causa è strutturale, non ciclica. I nuovi data center AI assorbono capacità di memoria che prima serviva telefoni, laptop e console. I produttori assegnano per primi i volumi agli ordini con margini più alti. Gli analisti che seguono l'offerta di moduli prevedono che nel 2027 la disponibilità di chip DRAM per i produttori di moduli scenda di oltre il 70 percento.

**Il CEO di Intel ha indicato una cifra precisa.** Al summit AI Infrastructure di Santa Clara del 15 settembre 2026, Lip-Bu Tan ha dichiarato che i prezzi della memoria sono già saliti di "cinque, sei e sette volte" rispetto ai livelli precedenti. Ha avvertito che la memoria ora rappresenta dal 70 all'80 percento del costo dei materiali di un laptop economico. In un'altra occasione ha detto che non ci sarà sollievo prima del 2028.

*Le notizie indipendenti sul confronto del costo per area tra wafer DRAM e wafer logici avanzati contengono una precisazione importante. I prezzi spot non sono prezzi contrattuali e il mercato spot DDR5 è troppo sottile per rendere definitivo il confronto. La tendenza generale non è in dubbio.*

{{< figure src="local-ai-memory-price-trend-2026.webp" alt="Grafico degli aumenti trimestrali dei prezzi contrattuali DRAM nel 2026: salto dal 90 al 95 percento nel primo trimestre, in rallentamento al 13-18 percento nel terzo" >}}

### L'effetto sulle schede grafiche

La memoria è una parte importante del costo di produzione di una scheda grafica, quindi i prezzi DRAM si riflettono direttamente su quelli delle GPU.

| Scheda | Inizio 2025 | Settembre 2026 |
|---|---|---|
| **Nvidia RTX 5090** | $1,999 | **oltre $5,000** |
| **Asus RTX 5080** | $1,199 | $1,595 |
| **AMD RX 9070 XT** | circa $830 | **oltre $1,037** |

Gli aumenti sono arrivati a ondate coordinate nel 2026, non come rincari isolati. Nvidia ha alzato i prezzi a gennaio, di nuovo a maggio in particolare per RTX 5090, e ancora più avanti nell'anno. AMD ha seguito ad agosto con aumenti di almeno il 10 percento su alcune schede Radeon e kit di memoria GDDR6, attribuendoli direttamente ai costi della memoria.

**La generazione successiva è slittata invece di arrivare sul mercato.** La serie RTX 60 di Nvidia è ora prevista per il 2028, saltando completamente il 2027. La causa indicata è la disponibilità di memoria.

*La scheda che compri oggi non compete con una scheda più economica l'anno prossimo. Compete con una versione più costosa di sé stessa.*

## Perché aspettare costa di più

Il consiglio hardware abituale è aspettare la generazione successiva. In un mercato della memoria con offerta limitata, questo consiglio lavora contro di te.

Tre punti spiegano perché.

**I prezzi sono già saliti e continuano a crescere.** Un rincaro trimestrale del 90-95 percento dei contratti DRAM non è un picco che si inverte nel trimestre successivo. TrendForce prevede un nuovo aumento nel terzo trimestre, non una diminuzione, e il CEO di Intel colloca il sollievo nel 2028.

**Nel 2027 non ci sarà un prodotto nuovo da aspettare.** Se le GPU consumer di prossima generazione arrivano solo nel 2028, la strategia di attesa si allunga a due anni. È gran parte di un ciclo di aggiornamento hardware trascorso ad aspettare invano.

**I modelli sono già abbastanza validi.** Questo è cambiato nel 2026. Due anni fa, l'hardware locale offriva un'esperienza visibilmente compromessa. Oggi la stessa spesa compra un modello 27B da 135 token al secondo, con contesto 262K, che supera un'API premium nell'indice complessivo di intelligenza.

*Se aspettavi che i modelli locali diventassero validi, l'attesa è finita. Se aspetti che l'hardware costi meno, i dati sull'offerta indicano il 2028.*

## Cosa assemblare

Abbinare l'hardware ai modelli descritti è semplice, perché i pesi ternari hanno ridotto i requisiti.

| Fascia | Memoria | Cosa esegue agevolmente |
|---|---|---|
| **Base** | 8-12 GB VRAM | Modello ternario 27B da 5.53 a 6.70 GiB, con spazio per il contesto |
| **Pratica** | 16-24 GB VRAM | Qwen3.8 27B completo da 18 GB oppure pacchetto ternario con contesto lungo |
| **Comoda** | 32 GB VRAM | Modello ternario 27B con contesto completo 262K o MoE 80B con 3B parametri attivi |
| **Memoria unificata** | 64-128 GB | Modelli MoE sparsi più grandi su Apple Silicon o un desktop con memoria condivisa |

Alcune indicazioni pratiche contano più della tabella:

- **Compra memoria, non la GPU di punta.** Il pacchetto ternario da 5.53 GiB rende davvero utilizzabile la fascia base. Spendi la differenza in RAM di sistema e archiviazione invece di inseguire una scheda halo ai prezzi del 2026.
- **I sistemi con memoria unificata offrono valore.** Una macchina con almeno 64 GB di memoria condivisa esegue modelli sparsi più grandi a una frazione del costo di una scheda discreta con la stessa capacità.
- **Potenza e raffreddamento contano.** Un sistema che esegue inferenza per ore si comporta diversamente da uno che esegue benchmark per pochi minuti.
- **Usa il pacchetto ternario insieme a un modello più piccolo.** Un modello 3B risponde alle domande semplici, mentre il 27B gestisce quelle difficili.

{{< centerbutton href="https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B" >}}
Scarica Ternary Bonsai 2 27B
{{< /centerbutton >}}

## Quando i modelli di fascia alta valgono ancora il prezzo

La ragione per scegliere il livello premium esiste, ed è più circoscritta di quanto suggerisca il marketing.

**La risposta onesta è l'affidabilità fattuale.** L'accuratezza AA-Omniscience è del 40.9 percento per Sonnet 4.6 e del 15.6 percento per il modello aperto 27B. Se una risposta sbagliata costa un cliente, una diagnosi o una posizione legale, un divario di 25 punti percentuali conta più di qualunque indice complessivo.

**La seconda ragione sono le lunghe sequenze agentiche.** Sonnet 4.6 ottiene il 53.0 percento in Terminal-Bench Hard e il 75.7 percento in τ²-Bench Telecom, che misurano l'uso prolungato degli strumenti e il comportamento di un agente su più turni. La scheda del modello aperto non riporta valori comparabili. L'assenza non è incoraggiante.

**La terza ragione è operativa.** Un'API ospitata non richiede aggiornamenti dei driver, gestione di stranezze di quantizzazione, controllo di un fork llama.cpp o configurazione corretta di una base dei pesi ruotata. Qualcun altro gestisce la disponibilità e riceve la chiamata alle tre del mattino.

### La domanda da porsi

Come si giustifica il livello premium fuori dalle aziende?

**Per il lavoro in cui la conoscenza è fondamentale, ha ancora senso.** Ricerca, analisi legale, domande mediche, modelli finanziari e qualsiasi attività in cui una risposta sbagliata ma sicura di sé costa cara. È una categoria reale e il divario di accuratezza è un motivo concreto per pagare.

**Per il lavoro generativo la giustificazione si indebolisce rapidamente.** Scrivere bozze, riassumere, rifattorizzare codice, riformattare dati, classificare documenti ed eseguire pipeline automatiche sono attività in cui l'output viene verificato prima di essere accettato. Il divario di accuratezza costa poco se una persona o una suite di test controlla prima il risultato. Per questi carichi di lavoro è difficile giustificare il pagamento a token per un indice 30.1 quando un indice 33.7 gira gratis su hardware che già possiedi.

**La decisione ora riguarda le conseguenze, non le capacità.** Due anni fa si chiedeva se un modello locale fosse abbastanza valido per svolgere il lavoro. Oggi ci si chiede quanto costa un errore e come rilevarlo.

*Il sovrapprezzo aziendale compra affidabilità, conformità e il turno di reperibilità di qualcun altro. Gli altri pagano per una differenza che smette di contare non appena una suite di test controlla il risultato.*

## Punti chiave

- **Un modello locale 27B supera Claude Sonnet 4.6 nell'indice complessivo di intelligenza**, 33.7 contro 30.1, e prevale in programmazione, attività agentiche, contesto lungo e ragionamento scientifico avanzato.
- **Sonnet 4.6 mantiene il vantaggio nell'accuratezza fattuale**, 40.9 contro 15.6 percento in AA-Omniscience, il motivo più forte rimasto per scegliere il livello premium.
- **La quantizzazione ternaria rende pratico questo risultato.** Bonsai 2 27B esegue lo stesso modello 26.90B in 5.53 GiB anziché 18 GB. Entrambi sono Apache 2.0.
- **Ollama standard non esegue i pacchetti ternari.** Serve il fork llama.cpp di Prism ML, mentre il ripiego F16 genera silenziosamente output incoerente invece di fallire.
- **La velocità di decodifica misurata è 135 token al secondo** su RTX 5090, molto oltre la velocità di lettura.
- **I prezzi della memoria sono il motivo per agire ora.** I prezzi contrattuali DRAM sono saliti del 90-95 percento in un trimestre del 2026 e le GPU consumer di nuova generazione sono slittate al 2028.
- **La RTX 5090 è passata da $1,999 a oltre $5,000 in meno di due anni**, e tutte le fasce si sono rincarate.

## Prossimi passi

1. **Scarica il modello e provalo sul tuo carico di lavoro**: **[Ternary Bonsai 2 27B su Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)**
2. **Scarica i pesi originali a piena precisione** se hai memoria sufficiente: **[Qwen3.8 su Ollama](https://ollama.com/library/qwen3.8)**
3. **Prova il modello prima di assemblare un sistema** con l'endpoint ospitato gratuito: **[Qwen3.8 27B gratuito su OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)**
4. **Confrontalo con il livello a pagamento usando gli stessi prompt**: **[Claude Sonnet 4.6 su OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)**
5. **Dimensiona il sistema per il livello che ti serve** usando la tabella della memoria e acquistando prima la memoria della scheda grafica.
6. **Se hai un Raspberry Pi inutilizzato**, controlla se può ospitare un modello più piccolo: **[Quali modelli AI funzionano su Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Articoli correlati

| Articolo | Contenuto |
|---|---|
| **[Quali modelli AI funzionano su Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)** | Il limite inferiore dell'inferenza locale e cosa possono gestire davvero le schede piccole |
| **[Creare un assistente AI che protegge la privacy per Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un assistente locale su hardware fuori rete, dove la privacy è essenziale |
| **[Il ruolo della memoria ECC nel ridurre la corruzione dei dati](/articles/the-role-of-ecc-memory-in-mitigating-data-corruption/)** | Perché la qualità della memoria conta di più quando contiene un modello grande |
| **[Cos'è un homelab e dovresti averne uno?](/articles/what-is-a-homelab-and-should-you-have-one/)** | Pianificare spazio, alimentazione e raffreddamento per hardware che genera calore |

## Riferimenti

1. [Ternary Bonsai 2 27B - mirror del modello su Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)
2. [Qwen3.8 - libreria modelli Ollama](https://ollama.com/library/qwen3.8)
3. [Qwen3.8 27B (gratuito) - benchmark e prezzi OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)
4. [Claude Sonnet 4.6 - benchmark e prezzi OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)
5. [Primo test di Bonsai 2 27B - è il MIGLIOR modello AI per una singola GPU? - Bijan Bowen](https://www.youtube.com/watch?v=OA5cICIzD-c)
6. [Artificial Analysis - valutazioni indipendenti dei modelli](https://artificialanalysis.ai/)
7. [TrendForce - previsioni dei prezzi contrattuali DRAM e NAND](https://www.trendforce.com/)
8. [I chip di memoria sono più costosi dei chip di calcolo per area - Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon)
9. [Il sollievo per le GPU slitta al 2028 mentre la DRAM sale del 95% - Tech Insider](https://tech-insider.org/gpu-relief-pushed-2028-dram-price-jump-2026/)
10. [Tan di Intel: memoria fino a 7 volte più cara, nessun sollievo prima del 2028 - shattered.io](https://shattered.io/intel-ceo-memory-shortage-no-relief-until-2028-2026/)
11. [Fork llama.cpp di Prism ML - kernel ternari](https://github.com/PrismML-Eng/llama.cpp)
12. [Ternary-Bonsai-2-27B-gguf - pesi originali](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
