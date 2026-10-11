---
title: "Quale modello di IA locale dovresti eseguire? Guida a GPU, contesto e programmazione per ottobre 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Guida pratica di ottobre 2026 alla scelta di modelli di IA locali per gli agenti di programmazione. Confronta memoria GPU, crescita della cache KV, dimensione del contesto, qualità della quantizzazione, elaborazione dei prompt, livelli di ragionamento e costi del noleggio cloud."
genre: ["IA locale", "Hardware IA", "IA self-hosted", "Benchmark GPU", "Strumenti per sviluppatori", "Economia dell'IA"]
tags: ["modelli IA locali", "agenti di programmazione", "guida GPU", "VRAM", "cache KV", "finestra di contesto", "Qwen 27B", "mixture of experts", "quantizzazione", "llama.cpp", "Ollama", "decodifica speculativa", "predizione multi-token", "LLM locale", "noleggio GPU", "workstation IA", "programmazione con agenti", "elaborazione prompt", "velocità inferenza"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Una workstation che mostra modelli di IA locali, uso della memoria GPU e finestre di contesto degli agenti di programmazione"
coverCaption: ""
ref: ["/articles/32gb-vram-qwen-27b-hardware-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/local-ai-2026-build-your-rig-now"]
---

**Il miglior modello locale per programmare è quello che mantiene abbastanza progetto in memoria e lo legge abbastanza velocemente da restare utile.** La dimensione del modello conta ancora. Un modello che entra soltanto dopo lo spostamento nella RAM di sistema spesso offre un'esperienza peggiore rispetto a un modello più piccolo con una finestra di contesto stabile.

*Scegli il modello e il budget di memoria insieme. Non scegliere un modello da una classifica per poi forzarlo su hardware inadatto.*

Questa guida riguarda gli agenti di programmazione, non i prompt brevi di completamento automatico. Un agente legge file, output degli strumenti, errori del compilatore e risultati dei test prima di scrivere una correzione. Questi input consumano contesto e cambiano la scelta dell'hardware.

## Il video è un riferimento

Il video seguente confronta modelli locali su diverse fasce di memoria GPU. È utile per le osservazioni pratiche sulla scelta dei modelli e per i risultati hardware riportati. Questo articolo segue un percorso separato e organizza la decisione intorno al comportamento della memoria, al contesto dell'agente, all'elaborazione dei prompt e al costo totale di possesso.

{{< youtube id="C9M6iUFtVB4" enable="true" title="Ho testato ogni modello di IA locale così non devi farlo tu" description="Confronto pratico di modelli di IA locali su diverse fasce di memoria GPU, con attenzione ai carichi di programmazione e ai limiti hardware." >}}

## Perché le classifiche falliscono

Una classifica dei modelli associa di solito il numero di parametri a una quantità di memoria GPU. Questa scorciatoia è utile per una prima stima. Smette di essere utile quando un agente di programmazione inizia a leggere un repository reale.

I pesi del modello sono la prima allocazione. La **cache KV** è l'allocazione che cresce. Conserva chiavi e valori di attenzione del contesto attivo, così il runtime non deve ricalcolare l'intero prompt dopo ogni token generato.

| Consumatore di memoria | Cosa contiene | Perché conta |
|---|---|---|
| **Pesi del modello** | I parametri quantizzati | Requisito di caricamento iniziale |
| **Cache KV** | Note dal contesto attivo | Cresce con prompt e conversazione |
| **Buffer di runtime** | Spazio temporaneo per i calcoli | Varia in base a backend e dimensione del batch |
| **Istruzioni dell'agente** | Prompt di sistema e definizioni degli strumenti | Usa contesto prima che arrivino i file del progetto |

**Il fatto che un file del modello entri nella scheda non dimostra che l'agente sia utilizzabile.** Il runtime ha bisogno di spazio per cache, buffer temporanei, definizioni degli strumenti e risposta successiva.

## Il contesto è il vero budget

Gli agenti di programmazione consumano contesto per molto più dei file sorgente. Il budget comprende anche istruzioni di sistema, schemi degli strumenti, elenchi di directory, output della shell, messaggi del compilatore, risultati dei test e turni precedenti della conversazione.

Tre connessioni MCP con definizioni dettagliate degli strumenti consumano spesso diverse migliaia di token prima che l'agente apra un file del progetto. Un contesto predefinito piccolo lascia poco spazio al codice. L'agente risponde comunque, ma perde il set di lavoro necessario per riparazioni in più passaggi.

La [FAQ del runtime di Ollama](https://docs.ollama.com/faq) indica un contesto predefinito di 4.096 token. `OLLAMA_CONTEXT_LENGTH` modifica il valore predefinito, mentre `OLLAMA_NUM_PARALLEL` scala la memoria richiesta con il numero di richieste simultanee. Registra entrambi i valori prima di confrontare un benchmark locale con un risultato a richiesta singola.

```bash
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_NUM_PARALLEL=1 ollama serve
```

Questo esempio imposta un valore predefinito di 32K per una richiesta attiva. Non riserva 32K token ai file del progetto. Istruzioni, definizioni degli strumenti, input e output condividono ancora la finestra.

### Una semplice scheda del contesto

Prima di confrontare le GPU, registra questi valori:

- **Dimensione del progetto:** file e righe sorgente approssimative in un'attività normale.
- **Sovraccarico degli strumenti:** prompt di sistema, schemi MCP, strumenti shell e istruzioni dell'editor.
- **Carico degli errori:** lunghezza normale dell'output del compilatore e dei test.
- **Contesto obiettivo:** il prompt più grande che vuoi conservare senza troncamento.
- **Spazio per la risposta:** spazio riservato alla patch prevista e alla spiegazione.

Usa il risultato come specifica del carico di lavoro. Uno sviluppatore che modifica un file alla volta ha esigenze di memoria diverse da chi chiede a un agente di seguire un'API in un monorepo.

## La cache KV cambia la classifica

Due modelli con numeri di parametri simili spesso hanno costi di contesto diversi. Un modello denso in cui ogni livello contribuisce alla cache crescente richiede più memoria rispetto a un modello con architettura di attenzione ibrida.

Un modello di programmazione 27B discusso nel materiale di riferimento usa un numero limitato di livelli di attenzione completa, mentre gli altri livelli usano un riepilogo di dimensione fissa. Il costo riportato della cache per un contesto 128K resta sotto 9GB. Un modello di dimensioni simili con attenzione completamente crescente in ogni livello richiede secondo il rapporto più di 21GB alla stessa lunghezza di contesto.

Queste cifre descrivono architetture e impostazioni di runtime specifiche. Usale come motivo per esaminare l'architettura, non come formula universale della memoria.

| Comportamento del modello | Effetto sul contesto | Implicazione hardware |
|---|---|---|
| **Attenzione completa a ogni livello** | Grande crescita della cache | Più memoria per prompt lunghi |
| **Attenzione ibrida o scorrevole** | Minore crescita della cache in alcuni livelli | Più margine di contesto a parità di dimensione del modello |
| **Mixture of experts** | Meno parametri attivi per token | Meno calcolo per token, ma tutti i pesi richiedono spazio |
| **Estensione per contesti lunghi** | Finestra di lavoro più ampia | Più memoria per la cache e più lavoro di elaborazione del prompt |

**Leggi l'architettura del modello prima di comprare memoria.** Il numero di parametri da solo nasconde il costo di una lunga sessione di programmazione.

## Scegli in base alla fascia di memoria GPU

### Da quattro a otto GB

I piccoli modelli densi restano la scelta pratica. Entrano nella scheda, rispondono rapidamente e funzionano bene per completamento automatico, spiegazioni brevi e modifiche a file singoli.

Un modello più grande con offload sulla CPU potrebbe produrre testo, ma il tempo di risposta spesso diventa il limite. Un agente di programmazione richiede letture ripetute dei file e chiamate agli strumenti. Una configurazione da quattro token al secondo trasforma ogni riparazione in una lunga attesa, anche quando il modello funziona tecnicamente.

I modelli mixture of experts offrono un'altra strada. Una parte attiva ridotta diminuisce la pressione sul calcolo, mentre l'insieme completo dei pesi risiede in parte nella memoria di sistema. Servono molta RAM e percorsi di trasferimento rapidi.

| Carico di lavoro | Direzione suggerita |
|---|---|
| **Completamento automatico** | Piccolo modello denso con prompt breve |
| **Modifiche a un singolo file** | Piccolo modello instruct con supporto agli strumenti |
| **Agente sull'intero repository** | Noleggia una GPU più grande o aumenta prima la memoria di sistema |
| **Codice privato sotto NDA** | Usa un modello locale, accettando un ambito più ristretto o esecuzioni più lente |

**In questa fascia, compra RAM di sistema prima di inseguire un modello grande.** Un piccolo modello stabile è migliore di un modello grande che passa la maggior parte del tempo a spostare dati sul bus.

### Da dodici a sedici GB

Questa fascia apre la porta a un modello di programmazione 27B, ma la scelta della quantizzazione diventa centrale. Una build standard a 4 bit vicina a 17GB non entra in una scheda da 16GB una volta aggiunto l'overhead del runtime.

Una build a 3 bit vicina a 13GB lascia più spazio al contesto. Una scheda da 12GB spinge verso una build a 2 bit o verso un modello mixture of experts più piccolo. La qualità dipende dal quantizzatore specifico e dal processo di calibrazione. Due upload con la stessa profondità in bit producono spesso risultati diversi nella programmazione.

Controlla questi elementi prima di scaricare un modello quantizzato:

- **Autore del quantizzatore e note di rilascio**
- **Dati di calibrazione e risultati delle valutazioni**
- **Compatibilità del tokenizer**
- **Test delle chiamate agli strumenti**
- **Lunghezza del contesto con la quantizzazione scelta**
- **Supporto in Ollama, llama.cpp o nell'interfaccia scelta**

**Non trattare “2 bit” o “3 bit” come una descrizione completa della qualità.** Il metodo di impacchettamento e i dati di calibrazione contano.

### Da ventiquattro a trentadue GB

Questa è la fascia più flessibile per un modello di programmazione 27B. Una scheda da 24GB spesso ospita una build a 4 bit con un contesto utile, ma una finestra completa da 128K potrebbe superare la memoria restante. Una scheda da 32GB lascia più spazio al runtime per cache e allocazioni temporanee.

Questa fascia rende anche più facile giustificare l'acquisto. Una GPU gestisce il carico senza la complessità della divisione tra due schede. Il sistema usa meno energia di una configurazione multi-GPU e il supporto software è più semplice da testare.

| Capacità | Posizione pratica |
|---|---|
| **24GB** | Solido modello a 4 bit con limiti di contesto da misurare |
| **32GB** | Modello 27B a 4 o 6 bit con più margine per il contesto |
| **48GB** | Precisione maggiore o cache più ampia senza cambiare il modello principale |

**La fascia da 24GB a 32GB è la zona d'acquisto sensata per la programmazione privata frequente.** Evita l'offload più penalizzante senza portare hardware da data center in un case desktop.

### Quarantotto GB e oltre

Più memoria non significa automaticamente un modello nuovo. Lo stesso modello 27B potrebbe funzionare a precisione 8 bit su una scheda da 48GB, con cache più grande e meno compromessi. Il miglioramento riguarda coerenza, spazio per il contesto e qualità dell'output, non un nuovo livello di ragionamento.

A 128GB la decisione cambia. Diventa possibile un modello mixture of experts molto più grande, ma l'elaborazione del prompt diventa una preoccupazione seria. Un modello spesso genera rapidamente mentre impiega molto tempo a leggere un repository grande o un nuovo risultato di uno strumento.

**Per i modelli grandi, misura separatamente la velocità di prefill e quella di decode.** Una risposta rapida dopo una lettura lenta del prompt resta lenta in un flusso con agente.

## La velocità di decode è solo metà del test

**La velocità di decode** misura i token generati al secondo. Risponde a “Quanto velocemente scrive il modello?”. **La velocità di prefill** misura l'elaborazione del prompt. Risponde a “Quanto velocemente legge il modello?”.

Un agente passa molto tempo a leggere. Ogni chiamata a uno strumento aggiunge nuovo testo. Un file sorgente lungo, una traccia dello stack o un log di test entra nel prompt prima dell'inizio della risposta successiva.

| Metrica | Esperienza dell'utente |
|---|---|
| **Token di decode al secondo** | Velocità con cui compare la risposta dopo l'elaborazione |
| **Token di prompt al secondo** | Tempo di attesa prima dell'inizio della risposta |
| **Tempo al primo token** | Ritardo combinato di elaborazione del prompt e preparazione |
| **Conservazione del contesto** | Quanta parte dello stato del progetto resta disponibile durante l'attività |

**Misura le dimensioni dei prompt che usi davvero.** Un prompt sintetico breve nasconde il costo più importante durante il lavoro su un repository.

## Prima le impostazioni del runtime

Gli aggiornamenti hardware non sono il primo passo per le prestazioni. Prova le impostazioni del runtime prima di aprire una pagina di acquisto.

### Predizione multi-token

Alcune combinazioni di modello e backend supportano la predizione di diversi token futuri, che poi vengono verificati in un solo passaggio. La funzione spesso appare come flag del runtime o configurazione draft compatibile.

I test riportati nel materiale di riferimento mostrano grandi guadagni su alcune schede di fascia alta. I risultati variano in base a file del modello, backend, driver e scheda. I percorsi Apple Metal potrebbero non conservare la funzione richiesta durante la conversione.

### Livello di ragionamento

Un modello distribuito con ragionamento massimo dedica più tempo al lavoro interno prima di restituire un risultato. Un ragionamento medio offre spesso un equilibrio migliore per le riparazioni del codice, soprattutto quando l'attività include già un messaggio di errore chiaro e un file preciso.

Usa una matrice di test semplice:

1. Esegui la stessa correzione di bug con ragionamento basso, medio e alto.
2. Registra tempo al primo token, tempo totale, successo della patch e risultato dei test.
3. Ripeti con un prompt breve e con un prompt delle dimensioni di un repository.
4. Mantieni l'impostazione che completa meglio l'attività, non quella con il token rate più alto.

**Il ragionamento medio con un percorso multi-token compatibile è un buon punto di partenza.** Verifica la qualità sul tuo codice prima di renderlo predefinito.

## Hardware locale o GPU a noleggio?

Il calcolo a noleggio vince per l'uso occasionale. Paghi le sessioni attive invece di comprare, raffreddare, aggiornare e alimentare una scheda tutto l'anno.

L'hardware di proprietà vince quando il carico è frequente, privato o offline. Elimina anche i tempi di coda e offre un ambiente stabile per test ripetibili.

| Situazione | Prima scelta migliore |
|---|---|
| **Poche sessioni al mese** | Noleggia una GPU o usa un'API |
| **Programmazione privata quotidiana** | Compra un sistema supportato da 24GB a 32GB |
| **Repository grande con ricaricamenti frequenti** | Noleggia prima e misura la velocità di prefill |
| **Nessun codice esce dall'edificio** | Possiedi il sistema più piccolo che raggiunge il contesto obiettivo |
| **Sperimentazione con un nuovo modello** | Noleggia prima di acquistare hardware |

Calcola il punto di pareggio con le ore attive, non con le ore del calendario. Includi elettricità, spazio, raffreddamento, manutenzione e tempo necessario per tenere in funzione il runtime.

**Una GPU di fascia alta comprata per esperimenti occasionali è una spesa per hobby.** Un sistema da 24GB a 32GB usato ogni giorno per lavoro privato ha una motivazione economica più solida.

## Una checklist d'acquisto migliore

Segui questo ordine quando confronti un modello e una GPU:

1. **Definisci l'attività.** Completamento automatico, riparazione di un file, agente per repository o analisi con contesto lungo.
2. **Misura il prompt.** Conta istruzioni di sistema, schemi degli strumenti, file e output dei test normali.
3. **Esamina il comportamento della cache.** Cerca note sull'architettura e misure della memoria legate al contesto.
4. **Scegli una quantizzazione.** Controlla i risultati di qualità dell'upload specifico, non solo il numero di bit.
5. **Testa prefill e decode.** Usa prompt del tuo repository.
6. **Regola il ragionamento.** Confronta il tempo per completare l'attività con diversi livelli.
7. **Testa privacy e manutenzione.** Conferma dove viaggia il codice sorgente e chi mantiene il backend.
8. **Confronta il costo del noleggio.** Usa le ore attive previste e includi l'energia nella stima del sistema di proprietà.

## Raccomandazione finale

**Sotto 12GB, usa un modello più piccolo o un modello mixture of experts con RAM di sistema sufficiente.** Non forzare un modello denso 27B su una configurazione che passa la maggior parte del tempo a fare offload.

**Da 12GB a 16GB, concentrati sulla qualità della quantizzazione e su un contesto obiettivo controllato.** Una build a 2 o 3 bit ben testata con supporto agli strumenti è più utile di un file a 4 bit che non entra mai bene.

**Da 24GB a 32GB, un modello di programmazione 27B diventa il valore predefinito pratico per il lavoro privato quotidiano.** Misura l'uso del contesto e la velocità del prompt prima di dare per disponibile l'intera finestra dichiarata.

**A partire da 48GB, usa la memoria extra per precisione, spazio della cache e sessioni stabili prima di passare a un modello più grande.** Quando il sistema supera 128GB, la velocità di lettura del prompt e l'economia del noleggio meritano più attenzione della capacità grezza.

Il nome del modello è solo il punto di partenza. La domanda utile è quanto contesto del progetto resta dopo la quota del modello, del runtime, degli strumenti e della cache.

## Letture correlate

- [32GB di VRAM per Qwen 27B: guida all'hardware per l'IA locale](/articles/32gb-vram-qwen-27b-hardware-guide/), dedicata ai percorsi hardware per un carico 27B.
- [Benchmark GPU di Llama 3.1 8B e Qwen3.8 27B su Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), risultati misurati su GPU a noleggio e limiti del contesto lungo.
- [IA locale nel 2026: un modello 27B supera Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), qualità del modello, quantizzazione ed economia dell'hardware locale.
