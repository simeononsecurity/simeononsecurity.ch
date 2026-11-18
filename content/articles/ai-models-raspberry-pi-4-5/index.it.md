---
title: "Quali modelli AI funzionano su Raspberry Pi 4 o 5?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Usa i risultati misurati su Raspberry Pi 4 e 5 per scegliere modelli linguistici locali in base a memoria, velocità e carico, dai piccoli modelli LFM2.5 alle opzioni 3B e superiori."
genre: ["Raspberry Pi", "Intelligenza artificiale", "Self-hosting"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "AI locale", "piccoli modelli linguistici", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "quantizzazione dei modelli", "AI edge"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Due computer Raspberry Pi su una scrivania scura, con illustrazioni blu e ambra di reti neurali sopra di essi"
coverCaption: "Illustrazione di modelli AI locali in esecuzione su hardware Raspberry Pi."
---

Un Raspberry Pi può eseguire localmente un modello linguistico utile, ma il modello deve rientrare nella memoria della scheda e nei tempi di risposta che l'applicazione può tollerare. Un Raspberry Pi 4 da 2 GB è più adatto a modelli con meno di circa un miliardo di parametri. Un Raspberry Pi 5 da 8 GB esegue senza problemi modelli compatti da 1B–3B e può caricare alcuni modelli quantizzati più grandi, con compromessi notevoli.

Abbiamo testato questi modelli con Ollama su un **Pi 4B da 2 GB** e un **Pi 5 da 8 GB**, entrambi con scheda microSD. Le misurazioni nelle tabelle usano gli stessi cinque prompt brevi per l'assistente, lo stesso prompt di sistema, un seed fisso e un limite di output di 140 token. Prima di ogni prova scaricavamo gli altri modelli e misuravamo il caricamento a freddo, il tempo al primo token visibile, il tempo totale di risposta, la velocità di output e la memoria residente massima. Sono state prove singole di un carico con risposte brevi: i risultati servono a stimare le risorse, non sono classifiche universali di velocità o qualità. La [CPU Cortex-A76 e le configurazioni di memoria disponibili sul Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) differiscono in modo sostanziale anche dalla [piattaforma Cortex-A72 del Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Quali tipi di modello sono adatti

| Tipo di modello | Esempi misurati | Uso pratico |
|---|---|---|
| Modelli di testo piccoli, circa 230M–600M parametri | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Comandi locali brevi, riepiloghi e domande con vincoli; punto di partenza migliore per un Pi 4 da 2 GB |
| Modelli di testo compatti, circa 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Più spazio per istruzioni articolate su Pi 5 o Pi 4 con più memoria, ma risposte più lente dei modelli più piccoli |
| Modelli di testo quantizzati da 3B–4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Candidati più capaci per un Pi 5 da 8 GB se è accettabile attendere alcuni secondi per risposta |
| Modelli sparsi o ibridi più grandi | LFM2.5 8B | Eseguibile sul Pi 5 da 8 GB testato, ma con un ingombro di memoria elevato e un lungo caricamento a freddo |

Questi risultati riguardano la **generazione di testo**. Non descrivono le prestazioni di generazione di immagini, riconoscimento vocale, visione artificiale o addestramento. “Funziona” non significa solo che il file del modello entra nella scheda: servono RAM anche al runtime, alla cache del contesto, al sistema operativo e agli altri servizi. La quantizzazione riduce la dimensione dei pesi, ma può peggiorare la qualità delle risposte, soprattutto con impostazioni estreme come pesi a 1 bit.

### Cosa misurano i nostri dati

Il benchmark ha inviato all'API chat di Ollama prompt brevi su fatti, sicurezza procedurale, contesto recuperato, meteo e assistenza. Ogni modello ha ricevuto lo stesso insieme di prompt e lo stesso seed. Prima di misurarlo, scaricavamo il modello per includere nel tempo il caricamento a freddo. Il **tempo reale** riportato comprende l'intera richiesta; i **token al secondo** descrivono solo la generazione dell'output. Abbiamo registrato anche il primo token *visibile*, perché un modello può impiegare tempo a ragionare prima di rispondere.

Per la memoria abbiamo campionato RAM e swap disponibili sul Pi e la memoria residente di Ollama e del processo di inferenza durante ogni richiesta. I valori **RSS** indicano la memoria residente del processo, non il fabbisogno totale dell'host. Pagine dei file, sistema operativo, browser o altri servizi locali possono comunque causare swap anche se il modello sembra rientrare. Le tabelle usano le prime prove, una per ciascun modello, con cinque prompt. In seguito abbiamo ampliato il sistema di test con un prompt sulle notizie e verifiche delle regole di risposta. Queste verifiche chiariscono cosa controllare, ma non trasformano i tempi precedenti in risultati di conformità su sei prompt.

Né i token al secondo né il numero di parametri sono punteggi di qualità. Un modello può generare testo rapidamente ma omettere una fonte richiesta, superare il limite di parole o lasciare una frase incompleta. Confronteremmo i modelli sui prompt che vogliamo davvero usare e controlleremmo le risposte prima di sceglierne uno per un'applicazione.

## Raspberry Pi 4: scegli i modelli più piccoli

Il Pi 4 da 2 GB testato aveva poco margine di memoria. I modelli LFM2.5 più piccoli hanno completato tutti e cinque i prompt, così come `qwen2.5:0.5b`. Sono scelte sensate per brevi risposte offline o un piccolo assistente locale.

| Modello | File modello | Velocità di output misurata | Tempo medio di risposta | Memoria o risultato osservato |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF importato | 0.25 GB | 12.8 token/s | 7.2 s | Picco RSS 383 MB; 5/5 prompt |
| LFM2.5-350M, GGUF importato | 0.38 GB | 8.6 token/s | 8.6 s | Picco RSS 516 MB; 5/5 prompt |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 token/s | 9.7 s | 5/5 prompt; disponibile direttamente in Ollama |
| MiniCPM5-1B, GGUF importato, ragionamento disattivato | 0.69 GB | 5.9 token/s | 12.2 s | Picco RSS 883 MB; 5/5 prompt |
| MiniCPM5-1B, GGUF importato, ragionamento predefinito | 0.69 GB | 5.7 token/s | 33.3 s | Solo 1/5 prompt ha restituito una risposta visibile utile |
| `qwen3:0.6b`, ragionamento predefinito | 0.52 GB | 6.4 token/s | 40.4 s | Una risposta vuota; la scheda si è riavviata |
| `granite4:350m` | 0.71 GB | 4.6 token/s | 15.5 s | 913 MB RSS, nessuno swap o riavvio; lento ma stabile |
| `gemma3:1b` | 0.82 GB | 4.0 token/s | 30.7 s | Swap intenso; la scheda si è riavviata durante il test |
| `qwen3.5:0.8b` | 1.04 GB | — | — | Non ha completato; la scheda si è riavviata |

I risultati del Pi 4 dipendono in modo particolare dal resto del sistema. Durante i test con modelli più grandi abbiamo osservato riavvii della scheda, incluso un test `qwen3.5:0.8b` mai completato. È un'evidenza sulla nostra configurazione da 2 GB, non un'affermazione secondo cui tutti i Pi 4 o tutti i modelli 1B si riavvieranno. Un Pi 4 da 4 GB o 8 GB ha più memoria, ma la CPU continuerà a rendere l'inferenza più lenta rispetto al Pi 5 testato. Non abbiamo misurato direttamente queste varianti di memoria del Pi 4.

Una prima prova sul Pi 4 sembrava molto peggiore delle misurazioni finali: circa 625 MB di file GGUF temporanei erano in `/tmp`, basato su RAM, e lasciavano solo 500–600 MB liberi; centinaia di megabyte finivano nello swap. Dopo aver spostato quei file nell'archiviazione persistente, i risultati dei modelli piccoli hanno fornito un quadro più utile della memoria usata dall'inferenza. Su una scheda da 2 GB, persino la *posizione del download* può falsare un benchmark.

**Consiglio:** LFM2.5-350M importato è la nostra scelta predefinita per questa scheda da 2 GB. È rimasto stabile a **516 MB RSS**, ha lasciato circa **1 GB di RAM disponibile** e ha superato **5/6** controlli delle regole nella prova di conformità del Pi 4. Nei test ripetuti sul Pi 5 ha però omesso i nomi delle fonti; le applicazioni che richiedono attribuzione dovrebbero verificarli. Scegli LFM2.5-230M quando contano soprattutto latenza e margine di memoria: è stato più veloce e leggero, ma in una risposta con contesto medico ha trasformato “nausea o vomito” in “nausea/uso del ventilatore”. Questo errore di contenuto lo rende meno adatto come predefinito per risposte sanitarie o di sicurezza, nonostante il punteggio più alto nei controlli meccanici ripetuti. Scegli `qwen2.5:0.5b` se ti serve un modello dal [registro Ollama](https://ollama.com/library/qwen2.5/tags), tenendo conto della minore conformità alle istruzioni. `granite4:350m` è rimasto stabile ma è più lento e usa più memoria; MiniCPM5-1B è praticabile solo se il client disattiva il ragionamento. Evita Gemma 3 1B e Qwen3.5 0.8B su questa specifica configurazione da 2 GB perché le nostre esecuzioni hanno provocato riavvii.

## Raspberry Pi 5: più scelta, con un compromesso sulla velocità

Il Pi 5 da 8 GB ha gestito tutti i **25 modelli** nel nostro benchmark di velocità e memoria. La tabella include ogni prova, anche i modelli che non consigliamo per questo carico di risposte brevi. Il simbolo † indica un GGUF importato. “Think off” segnala l'impostazione usata per la prova di velocità; la prova separata di conformità non ha necessariamente usato la stessa impostazione.

| Modello | File GB | Uscita tok/s | Risposta s | Picco RSS MB | Valutazione per risposte brevi |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Latenza più bassa; 78% di conformità ripetuta |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Da evitare: pesi a 1 bit e conformità 3/6 in un singolo test |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Veloce, ma ha omesso la fonte in 5/18 ripetizioni |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Facile da installare dal registro; 61% di conformità ripetuta |
| `qwen3:0.6b`, ragionamento disattivato | 0.52 | 23.0 | 4.3 | 1,069 | Condizionale: 4/6 al test di conformità, l'impostazione conta |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Modello sperimentale a 1 bit; 6/6 in un singolo test non confermato |
| `minicpm5-1b` †, ragionamento disattivato | 0.69 | 18.4 | 5.1 | 869 | Condizionale: il ragionamento predefinito produceva risposte vuote |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Entra, ma è più lento e più grande dei piccoli LFM2.5 |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Migliore in generale per il nostro carico; 89% di conformità ripetuta |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Alternativa dal registro; 5/6 al test di conformità |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Migliore conformità ripetuta tra i modelli del registro: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6 al test; Gemma 3 1B ha seguito meglio le regole |
| `qwen3.5:0.8b`, ragionamento disattivato | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 con ragionamento predefinito; evita se non puoi controllarlo |
| `spark-x2.5-1.7b` †, ragionamento disattivato | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 con ragionamento predefinito; evita se non puoi controllarlo |
| `qwen3:1.7b`, ragionamento disattivato | 1.36 | 8.1 | 12.4 | 1,867 | Condizionale; più memoria e latenza delle opzioni piccole |
| `minicpm5-2b` †, ragionamento disattivato | 1.56 | 7.7 | 10.9 | 1,787 | Condizionale; 5/6 in un test singolo, elenchi più lunghi |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Modello 3B da provare; 5/6 in un test singolo |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Da evitare per l'uso interattivo: decodifica lenta |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Alternativa 3B; nessun test di conformità riportato |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Entra, ma risponde più lentamente delle alternative piccole |
| `qwen3.5:2b`, ragionamento disattivato | 2.74 | 5.0 | 16.1 | 3,627 | Molta memoria e latenza; nessun test di conformità riportato |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Da evitare per risposte rapide; 14.3 s al primo token |
| `ling-3.0-tiny` †, ragionamento disattivato | 4.82 | 9.9 | 19.4 | 5,071 | Ingombro elevato; 5/6 in un test singolo con errore di grounding |
| `lfm2.5:8b`, ragionamento disattivato | 5.16 | 8.7 | 54.6 | 5,317 | Entra a fatica; caricamento a freddo di 34.4 s e risposte troppo lunghe |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Da evitare: pressione sullo swap con altri servizi Pi |

† GGUF importato. Tempi di risposta e memoria provengono dalla prova di velocità Pi 5 con cinque prompt; i risultati di conformità vengono da test separati con sei prompt. Se manca un punteggio di conformità, non è stato dimostrato che il modello segua le regole di risposta.

I modelli LFM2.5 piccoli erano i più veloci per questo carico di risposte brevi. La versione 1.2B offre un compromesso pratico sul Pi 5 testato. Gemma 3 1B è un'alternativa disponibile nel registro che, nei test successivi, ha rispettato le regole di risposta più spesso di Qwen2.5 1.5B. Un modello 3B può valere l'attesa per prompt che richiedono più capacità, ma questi tempi da soli non dimostrano quale modello fornisca le risposte migliori.

Il caricamento a freddo e il ritardo al primo token cambiano l'esperienza. Sul Pi 5, LFM2.5-230M si caricava in circa **0.21 secondi** e mostrava un token dopo **0.37 secondi**. Qwen2.5 1.5B impiegava **2.59 secondi** per caricarsi e **3.66 secondi** al primo token visibile; Qwen2.5 3B richiedeva rispettivamente **5.60** e **7.97 secondi**. Per una domanda occasionale, questi ritardi possono contare più della velocità di output una volta avviata la generazione. Con un modello sempre caricato contano meno, ma la memoria resta occupata tra una richiesta e l'altra.

Altri candidati misurati mostrano perché non classifichiamo i modelli solo in base al numero di parametri. Con ragionamento disattivato, `qwen3:0.6b` ha raggiunto **23.0 token/s** sul Pi 5 a **1,069 MB RSS**, mentre MiniCPM5-1B importato ha raggiunto **18.4 token/s** a **869 MB RSS**. `granite4:350m` richiedeva un download di **0.71 GB** e generava **12.1 token/s**, nonostante il nome 350M. Il packaging e l'architettura cambiano il rapporto tra nome, dimensione del file, memoria e velocità.

Se il client può inviare in modo affidabile `think: false`, Qwen3 0.6B e MiniCPM5-1B sono esperimenti ragionevoli come alternative a LFM2.5. Anche MiniCPM5-2B, Qwen3 1.7B e Spark-X2.5 1.7B funzionavano sul Pi 5, ma nessuno offriva un chiaro vantaggio in velocità e memoria rispetto alle scelte principali. Il test di conformità ha usato il ragionamento predefinito per MiniCPM5-1B e Spark-X2.5; non presentare le risposte vuote come esito dei test di velocità think-off. Allo stesso modo, una prova rapida con ragionamento disattivato non dimostra che un bridge che omette quell'opzione riceverà una risposta utile.

Se la semplicità di installazione conta più della velocità pura, Gemma 3 1B e Llama 3.2 1B sono opzioni plausibili dal registro sul Pi 5 da 8 GB. Gemma 3 1B ha seguito le regole di risposta testate in **15/18** risposte ripetute. Llama 3.2 1B ha superato **5/6** in una prova singola, quindi la stima di conformità è meno certa. Nella prova di velocità, Qwen2.5 1.5B si caricava e rispondeva più in fretta di Gemma 3 1B, ma nella sua singola prova di conformità ha superato solo **4/6** controlli. Scegli in base al requisito importante per i tuoi prompt.

Per prompt occasionalmente più lunghi o difficili, Qwen2.5 3B e Llama 3.2 3B quantizzati sono i candidati 3B con uso della memoria gestibile sul nostro Pi 5 da 8 GB. Abbiamo misurato velocità e memoria; Qwen2.5 3B ha superato **5/6** in una singola prova di conformità, mentre non abbiamo pubblicato una prova comparabile per Llama 3.2 3B. Un numero maggiore di parametri è un motivo per *provare* questi modelli nelle attività in cui i più piccoli non bastano, non la prova che rispondano meglio. Granite 4 Micro e Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny e Gemma 3n E2B sono entrati o si sono caricati nei nostri test Pi 5, ma per questa applicazione a risposte brevi offrivano latenza, margine di memoria o affidabilità meno interessanti.

I due modelli Bonsai mostrano il costo della quantizzazione estrema. I file Q1_0 erano sorprendentemente piccoli per modelli chiamati 1.7B e 4B, ma il modello 1.7B ha superato solo **3/6** controlli di risposta. Il 4B li ha superati in una sola prova con sei prompt, ma ha richiesto **18.1 secondi** per risposta e non ha conferme ripetute di conformità. Li tratteremmo come esperimenti, non come raccomandazioni predefinite, soprattutto quando conta la qualità della risposta.

Il risultato LFM2.5 8B va contestualizzato: l'architettura ibrida usa meno parametri attivi per token, quindi la velocità di decodifica ha superato quella dei modelli densi 3B misurati. Il caricamento a freddo da microSD ha comunque richiesto **34.4 secondi** e il modello ha usato oltre **5.3 GB di memoria residente**. Dimostra cosa entra, ma non è una scelta predefinita comoda su un Pi che esegue anche altri servizi. Anche `gemma3n:e2b` misurato ha usato circa 5.3 GB di memoria residente e ha causato swap insieme agli altri servizi sull'host di test.

Il test LFM2.5 8B ha raggiunto il limite completo di **140 token** invece di mantenere breve la risposta. Gemma 3 4B ha impiegato **14.3 secondi** per il primo token e **30.3 secondi** per l'intera risposta. Entrambi possono caricarsi su questo Pi 5, ma nei nostri test nessuno si è comportato come un piccolo assistente reattivo. Un modello minuscolo con una risposta breve adeguata può servire una radio o un'interfaccia a comandi meglio di un modello più grande con velocità di decodifica superiore sulla carta.

## Memoria, ragionamento e formato del modello

Una prima stima utile, basata sulle nostre misurazioni, è **dimensione del download del modello × 1.4** per la memoria residente di inferenza. È solo una regola pratica: lunghezza del contesto, impostazioni del runtime, architettura del modello e altri processi possono cambiare il requisito. Controlla la memoria disponibile durante la generazione, mantieni caricato un solo modello su un host piccolo e lascia spazio per il sistema operativo. Una scheda da 4 GB può iniziare ragionevolmente con modelli piccoli o compatti, ma le nostre raccomandazioni per 4 GB sono estrapolazioni, non test diretti su Pi da 4 GB.

Per esempio, il file LFM2.5-1.2B da 0.73 GB ha corrisposto a circa **967 MB RSS** sul Pi 5, mentre il file Qwen2.5 1.5B da 0.99 GB ha raggiunto **1,361 MB RSS**. La regola è ragionevolmente valida per questi modelli, ma non è un limite rigido. Prevedi più memoria del solo processo misurato se il Pi esegue anche interfaccia, indice di ricerca, libreria locale o altri servizi in background. Controlla l'uso dello swap durante una richiesta reale; un modello che si carica ma usa continuamente lo swap non è adatto.

Alcuni modelli generano un blocco di ragionamento interno prima della risposta visibile. Nei nostri test, `qwen3:0.6b` sul Pi 4 da 2 GB impiegava molto più tempo prima di mostrare testo, e MiniCPM5-1B rispondeva in modo utile a uno solo dei cinque prompt con l'impostazione di ragionamento predefinita, contro cinque su cinque con il ragionamento disattivato. Per una risposta breve, imposta `think: false` in una richiesta compatibile all'API Ollama oppure scegli un modello che non ragiona per impostazione predefinita. L'impostazione vale per modelli e client supportati, non è un interruttore universale della velocità.

La distinzione conta perché il limite dei token può includere quelli consumati dal ragionamento, anche se l'utente non vede una risposta. Sul Pi 4, `qwen3:0.6b` con il ragionamento predefinito impiegava in media **40.4 secondi per richiesta** e un prompt ha prodotto una risposta visibile vuota. MiniCPM5-1B impiegava in media **33.3 secondi** con l'impostazione predefinita contro **12.2 secondi** con ragionamento disattivato. Nelle prove Pi 5 abbiamo disattivato il ragionamento anche per Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 e Spark-X2.5 dove indicato nei nostri dati. Confronta il modello usando esattamente l'impostazione che userà il client.

### Verifica che la risposta sia utilizzabile

Per il nostro carico di risposte brevi da mesh assistant, il contratto della risposta è importante quanto la velocità: massimo **90 parole**, non più di **tre punti elenco**, testo semplice, frase conclusa e uso del contesto recuperato con la fonte indicata. Il bridge divide il testo in parti da **180 caratteri**. Una risposta lunga occupa più tempo radio anche se il modello l'ha generata rapidamente.

La versione successiva del benchmark controlla le risposte vuote, il limite di parole specifico del prompt, troppi punti elenco, tabelle o blocchi di codice Markdown, una frase finale incompleta, termini mancanti dal contesto fornito e l'assenza del nome della fonte. Valutando le risposte con il prompt di sistema dell'assistente in distribuzione, i modelli piccoli violavano spesso queste regole. I problemi più gravi erano **risposte vuote** perché il ragionamento consumava il budget dei token, seguite da risposte che ignoravano il contesto recuperato o ne omettevano la fonte. Superare il limite di parole o usare troppi punti elenco produce comunque testo visibile, ma spreca tempo radio. Questi sono controlli meccanici, non sostituiscono la lettura della risposta: non dimostrano l'accuratezza dei fatti né la correttezza dei consigli di sicurezza.

#### Risultati di conformità ripetuti sul Pi 5

Per prima cosa abbiamo eseguito una volta sei prompt per modello con un limite di **220 token** e il prompt di sistema in distribuzione. Poi abbiamo provato altre due volte i modelli promettenti, con un seed diverso, ottenendo **18 risposte per modello**. Un risultato perfetto in una prova singola non garantiva lo stesso risultato nelle ripetizioni. I risultati ripetuti offrono un confronto più affidabile per le risposte brevi mesh testate:

| Modello | Risposte conformi a tutte le regole controllate | Principali errori osservati |
|---|---:|---|
| LFM2.5-1.2B importato | 16/18 (89%) | Due risposte incomplete |
| `gemma3:1b` | 15/18 (83%) | Tre risposte incomplete |
| LFM2.5-230M importato | 14/18 (78%) | Risposte incomplete e nomi di fonti mancanti |
| LFM2.5-350M importato | 13/18 (72%) | Nomi di fonti mancanti |
| `qwen2.5:0.5b` | 11/18 (61%) | Troppi punti elenco, troppe parole e nomi di fonti mancanti |

Sul **Pi 4 da 2 GB**, la prova separata con sei prompt ha dato **5/6** a LFM2.5-350M, **4/6** a LFM2.5-230M e **2/6** a Qwen2.5-0.5B. MiniCPM5-1B è passato da **1/6** con il ragionamento predefinito a **5/6** con il ragionamento disattivato. Questi punteggi del Pi 4 provengono da una sola prova, quindi per parlare in generale di conformità alle istruzioni diamo più peso ai risultati ripetuti del Pi 5 e usiamo i test Pi 4 per valutare stabilità e velocità su quella scheda.

Gli errori hanno conseguenze diverse. Una risposta **vuota** non offre nulla all'utente; una risposta che ignora il materiale fornito può essere fuorviante. Senza il nome della fonte, il lettore non può verificarne l'attribuzione. I punti elenco o le parole in eccesso consumano soprattutto altri pacchetti da 180 caratteri. Una frase incompleta può indicare che la risposta è stata troncata. L'errore di LFM2.5-230M su un termine medico ricorda che una risposta può superare i controlli meccanici e comunque essere sbagliata. Nessuno dei cinque candidati ripetuti ha rispettato ogni regola in tutti i 18 casi. Se un'app richiede lunghezza o formato rigidi, dovrebbe applicare i vincoli anche dopo la generazione e valutare separatamente i contenuti ad alto rischio.

Abbiamo controllato anche l'endpoint effettivo del bridge, `/v1/chat/completions` compatibile con OpenAI di Ollama, usando contesto WikiMed recuperato. Sul Pi 5 LFM2.5-1.2B ha restituito una risposta di 28 parole con sei termini forniti; Qwen2.5-0.5B una di 38 parole con sette termini. Entrambe rientravano in due pacchetti da 180 caratteri. Il controllo conferma che il modello LFM2.5 importato funziona nel percorso di richiesta del bridge, ma un'unica risposta riuscita non garantisce affidabilità.

Ollama pubblica molti modelli pronti da scaricare, incluse le varianti [Qwen2.5 da 0.5B, 1.5B e 3B](https://ollama.com/library/qwen2.5/tags). Abbiamo importato i piccoli modelli LFM2.5 in Ollama dalle [release GGUF di Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main). Prima di scaricare, controlla il tag esatto o il nome del file GGUF: i registri e i repository possono cambiare. Conserva i download GGUF nell'archiviazione persistente; nei nostri test, mettere i file in `/tmp` basato su RAM consumava la memoria limitata del Pi 4.

### Tag del registro e import GGUF

Un tag Ollama è il percorso più breve per una prima prova: scarica il tag esatto ed esegui il modello. I piccoli modelli LFM2.5 nelle tabelle erano **import GGUF**, non tag chiamati `lfm2.5-230m`, `lfm2.5-350m` o `lfm2.5-1.2b` nella libreria pubblica di Ollama. GGUF è un formato di file per modelli; nomi come `Q8_0` e `Q4_K_M` indicano scelte di quantizzazione. I file LFM2.5 da 230M e 350M usati erano Q8_0, mentre il file 1.2B era Q4_K_M. Perciò lo stesso numero di parametri scaricato con un'altra quantizzazione non avrà necessariamente la stessa dimensione, lo stesso uso di memoria o la stessa qualità.

Per importare la variante 350M testata, scarica il GGUF in una cartella di archiviazione persistente, crea un Modelfile che lo indichi e lascia che Ollama lo copi nel proprio archivio modelli:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

L'import richiede temporaneamente spazio sia per il file scaricato sia per la copia archiviata da Ollama. Abbiamo usato download riprendibili perché i trasferimenti GGUF lunghi a volte si interrompevano. Prima di importare, confronta SHA-256 del file scaricato con l'hash pubblicato dalla fonte: un trasferimento parziale può sembrare un problema del modello. Nella nostra configurazione Pi, `/tmp` era basato su RAM, quindi mettervi il GGUF riduceva la memoria disponibile per l'inferenza.

## Un punto di partenza pratico

| Hardware e obiettivo | Primo modello da provare | Perché |
|---|---|---|
| Pi 4 da 2 GB, uso predefinito | LFM2.5-350M importato | Stabile a 516 MB RSS con circa 1 GB disponibile; scelto dopo l'errore medico del 230M |
| Pi 4 da 2 GB, latenza minima | LFM2.5-230M importato | 383 MB RSS e risposta media di 7.2 s; verifica con attenzione il contenuto, soprattutto per domande di salute o sicurezza |
| Pi 4 da 2 GB, solo modelli da registro | `qwen2.5:0.5b` | Scaricabile direttamente da Ollama e stabile nella nostra prova Pi 4 con cinque prompt; 61% di conformità ripetuta sul Pi 5 |
| Pi 4 da 4 GB o Pi 5 | LFM2.5-1.2B importato, poi test locale | 967 MB RSS e 89% di conformità ripetuta sul nostro Pi 5 da 8 GB; non abbiamo testato direttamente i Pi 4 da 4 GB |
| Pi 5 da 8 GB, assistente reattivo | LFM2.5-1.2B importato | 15.5 token/s, 4.7 secondi di risposta totale e la conformità ripetuta più alta misurata |
| Pi 5 da 8 GB, solo modelli da registro | `gemma3:1b` | 11.2 token/s, 1,262 MB RSS e 83% di conformità ripetuta |
| Pi 5 da 8 GB, prova un modello testuale più grande | Qwen2.5 3B o Llama 3.2 3B quantizzati | Entrambi circa 5 token/s e 2.4–2.8 GB RSS; Qwen2.5 3B ha superato 5/6 in una prova di conformità singola |

Queste scelte danno priorità a risposte brevi e utili su un Pi che può eseguire anche altri servizi. Sono punti di partenza, non affermazioni che un modello sia migliore per ogni attività. Nel test di conformità singolo sul Pi 5, `qwen3.5:0.8b` e Spark-X2.5 con ragionamento predefinito non hanno prodotto risposte conformi; MiniCPM5-1B ha ottenuto 1/6. Se il client non può disattivare il ragionamento, evita questi modelli per carichi di risposta breve. Testa il modello finale con prompt, lunghezza del contesto, concorrenza e limite di risposta realmente previsti per la distribuzione.

Per il modello da registro, dopo aver [installato Ollama per Linux](https://ollama.com/download/linux), esegui:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Prova i tuoi prompt, la lunghezza desiderata delle risposte e gli altri servizi in esecuzione. Registra il tempo totale di risposta e l'uso della memoria. Questi dati diranno più del conteggio dei parametri per stabilire se un modello è adatto al tuo Pi.

Su un nodo con poca memoria, tieni sotto controllo lo swap durante i test. Se un modello più grande rende la scheda non responsiva, passa a un modello più piccolo e imposta un limite di memoria per il servizio Ollama adatto al modello, così un caricamento eccessivo fallisce prima di esaurire la memoria dell'host. Il limite del servizio è una protezione, non un modo per far entrare un modello troppo grande. I riavvii del Pi 4 nei nostri test mostrano perché reattività e margine di memoria contano insieme ai token al secondo.

## Trasforma il benchmark in una decisione di distribuzione

Prima di installare un modello per l'uso quotidiano, definisci quattro limiti: **tempo massimo di risposta, memoria residente massima, formato della risposta e comportamento in caso di errore**. Provali con i servizi che condivideranno la scheda. Un modello che supera il test da solo ma usa lo swap insieme al bridge radio o alla dashboard non soddisfa il requisito di distribuzione.

Mantieni installato un piccolo modello di riserva. Passa a questo modello quando quello principale supera il limite di memoria, restituisce una risposta vuota o non rispetta il contratto della risposta. Registra tag del modello, quantizzazione, versione di Ollama, prompt, lunghezza del contesto e seed per ogni confronto, così un aggiornamento del modello non sembrerà un miglioramento dell'hardware.
