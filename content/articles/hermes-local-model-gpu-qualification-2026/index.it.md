---
title: "Benchmark locali dei modelli Hermes: quali combinazioni di GPU e modelli sceglierei"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Le mie raccomandazioni per Hermes derivano da test di contesto lungo, strumenti, streaming e visione su sistemi RTX 5060 Ti, RTX 2000E Ada, RTX 3060 Ti e RTX 3070."
genre: ["Intelligenza artificiale", "IA locale", "Componenti hardware"]
tags: ["Hermes Agent", "modelli linguistici locali", "benchmark LLM", "inferenza GPU", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "qualificazione dei modelli", "chiamate agli strumenti", "contesto lungo", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Illustrazione di schede grafiche a doppia ventola e a basso profilo accanto al titolo Hermes Model Benchmarks su sfondo blu scuro"
coverCaption: ""
---

Per le attività Hermes con contesto lungo, partirei da Qwen3.5 35B su due RTX 5060 Ti da 16 GB. La route testata ha conservato 239.153 token di input tramite LiteLLM e superato verifiche separate di strumenti, streaming, visione, coda e annullamento. Qwen3.6 è la mia alternativa con una scheda. Sui sistemi RTX 3060 Ti e RTX 3070 partirei da Qwen3.5 2B o 4B.

Queste scelte derivano dall'esecuzione dei modelli attraverso i percorsi di inferenza usati dall'agente. Ho verificato la conservazione degli input lunghi, i cicli degli strumenti, le risposte in streaming, le domande sulle immagini e il rilascio del modello. Ho provato anche modalità e impostazioni di memoria, perché il caricamento corretto dice poco sull'utilità durante una lunga richiesta dell'agente.

Hermes richiede almeno 64.000 token di contesto per usare strumenti da agente. Ho usato 65.536 token di input effettivi come soglia per il contesto lungo. Il conteggio dell'input conta più del contesto dichiarato dal server. ([Documentazione dei provider Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## GPU in ciascun sistema

Le lettere dei sistemi indicano queste combinazioni hardware nei risultati.

| Sistema | GPU usate nel benchmark | Modello iniziale che sceglierei |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, 16 GB ciascuna | Qwen3.5 35B su entrambe le schede oppure Qwen3.6 su una sola scheda |
| B | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B quando alcuni minuti di elaborazione dell’input lungo sono adatti all’attività |
| C | 1 × RTX 2000E Ada, 16GB | Gemma 3 4B per il percorso testato con input lunghi; Qwen3.5 0.8B senza ragionamento per recupero mirato |
| D | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B, Gemma 4 12B-IT o GPT-OSS 20B per i carichi di lavoro testati con modelli più grandi |
| E | 9 × GeForce RTX 3060 Ti, 8 GB ciascuna | Qwen3.5 2B o 4B |
| F | 8 × GeForce RTX 3060 Ti, 8 GB ciascuna | Qwen3.5 2B o 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B o 4B |

Il numero di schede installate non implica che ogni richiesta abbia usato tutte le GPU. I test Qwen3.5 35B e Flash Next hanno usato entrambe le schede del sistema A. Qwen3.6 ne ha usata una. La ripetizione riuscita del test visivo Qwen3.5 4B sul sistema E ha usato una scheda selezionata da un gruppo di otto, mentre una nona è rimasta esclusa dalle attività AI.

Considera le durate come risultati combinati del modello, runtime e sistema testati. Queste esecuzioni confrontano configurazioni utilizzabili, senza isolare l'architettura GPU come causa della differenza di velocità.

## Due RTX 5060 Ti rendono Qwen3.5 35B la mia scelta per il contesto lungo

Qwen3.5 35B ha conservato la quantità maggiore di input nei test. La progressione diretta Ollama ha mantenuto 248.279 token in un contesto runtime di 262.144. Una richiesta gateway separata in streaming ha conservato 239.153 token, restituito il marcatore iniziale e terminato normalmente dopo 31 token di output in 148,12 secondi.

Il risultato gateway interessa Hermes perché la richiesta è passata dal broker e LiteLLM. Richieste separate hanno completato un ciclo dello strumento, riconosciuto un'immagine rossa e restituito due risposte corrette quando inviate insieme. Il broker le ha messe in coda. Chiudere la richiesta in streaming ha liberato il broker e scaricato il modello entro 60,31 secondi.

| Richiesta Qwen3.5 35B | Token di input | Token di output | Durata | Esito |
|---|---:|---:|---:|---|
| Ollama diretto, prima fase progressiva | 69,429 | 31 | 38.783 s | Marcatore iniziale esatto |
| Ollama diretto, continuazione con prefisso condiviso | 124,179 | 31 | 28.472 s | Marcatore iniziale esatto |
| Ollama diretto, continuazione con prefisso condiviso | 182,579 | 31 | 38.974 s | Marcatore iniziale esatto |
| Ollama diretto, continuazione con prefisso condiviso | 248,279 | 31 | 54.215 s | Marcatore iniziale esatto |
| richiesta in streaming del broker | 69,427 | 29 | 38.872 s | Marcatore iniziale esatto |
| richiesta in streaming LiteLLM | 239,153 | 31 | 148.12 s | Marcatore iniziale esatto, clean unload |

Le richieste dirette progressive riutilizzavano un prefisso sempre più lungo. Le durate descrivono una continuazione con prefisso caldo. Il risultato di 54,215 secondi non è una misura indipendente a freddo per un nuovo prompt da 248K.

Nella fase diretta più ampia il modello ha riportato circa 27,3 miliardi di byte residenti sulle due GPU. I picchi per scheda hanno raggiunto 14.964 e 12.386 MiB.

Le temperature massime hanno raggiunto 62 e 63 °C, senza errori OOM o Xid. Restavano 13.865 token nel contesto configurato per continuare. La risposta breve del marcatore ne ha usati 31.

Userei questa route quando conservare un ampio insieme di lavoro conta più della risposta iniziale più rapida. I controlli di strumenti e visione verificano comportamenti utili dell'agente; il test di input lungo verifica la conservazione. Sono carichi di lavoro distinti.

## Qwen3.6 è l'opzione con una scheda

Qwen3.6-35B-A3B UD-Q4_K_XL ha conservato 131.000 token di input su una RTX 5060 Ti. L'altra scheda è rimasta inattiva. È un'alternativa utile quando non conviene dedicare entrambe le schede a un solo modello.

| Richiesta gateway Qwen3.6 | Token di input | Token di output | Durata | Esito |
|---|---:|---:|---:|---|
| richiesta lunga iniziale | 66,007 |  | 167.82 s | Marcatore iniziale conservato |
| richiesta più lunga | 90,000 | 11 | 159.92 s | Marcatore iniziale conservato, zero cached input |
| richiesta più lunga | 119,999 | 11 | 250.61 s | Marcatore iniziale conservato, zero cached input |
| vicino al limite di esecuzione | 131,000 | 11 | 287.09 s | Marcatore iniziale conservato, zero cached input |

La richiesta da 131.000 token si è avvicinata al limite runtime di 131.072. Per un agente lascerei più spazio alla risposta e ai successivi messaggi degli strumenti. La conservazione vicino al limite prova la gestione dell'input, ma non definisce un budget predefinito sensato.

L'uso degli strumenti è riuscito con il pensiero disattivato. Il pensiero predefinito ha consumato i 512 token della prova prima di chiamare lo strumento. Anche le richieste rapide, in streaming e visive del pilot sono riuscite. Il primo controllo di contesto da 65.845 token è durato 139,57 secondi.

## Qwen3.8 27B vince il confronto con risposta abbinata a 66K

Per lo stesso carico con marcatore da 66.007 token sul sistema A, Qwen3.8 27B ha risposto più rapidamente. Terrei disponibile questa route per richieste vicine alla dimensione testata e Qwen3.5 35B per l'insieme di lavoro più ampio.

| Route sistema A | Token di input | Durata | Esito |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Marcatore iniziale conservato |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Marcatore iniziale conservato |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Marcatore iniziale conservato |
| Flash Next IQ4 compatibility alias | 66,007 | 213.25 s | Marcatore conservato |

Qwen3.8 27B ha impiegato circa un terzo delle durate delle richieste abbinate Qwen3.6 e Flash Next. Sono osservazioni di richieste complete con i runtime testati, non un confronto limitato all'hardware.

Anche risposte rapide, streaming e uso degli strumenti sono riusciti. La modalità senza pensiero ha completato la sequenza di colori e il ciclo dello strumento; la prova con pensiero ha restituito solo parte della sequenza entro 512 token.

Flash Next è una scelta predefinita meno interessante su questo sistema per la pressione di memoria. Il pilot da 65.847 token è riuscito in 201,41 secondi con contesto runtime 98.304. Due profili precedenti con contesto 131.072 hanno raggiunto il limite di memoria prima di diventare pronti.

La route successiva ha raggiunto il limite cgroup di 54 GiB. Per il lavoro non sorvegliato sceglierei più margine di memoria.

La route chiamata `flash-iq2` serviva il backend compatibile Flash Next IQ4. Il nome non indica un risultato IQ2.

## La RTX 2000E Ada gestisce input lunghi, ma la scelta del modello cambia l'attesa

Gemma 3 4B è la mia route testata preferita per input lunghi sul sistema C. Due percorsi hanno conservato oltre 84K token in circa 88 secondi. Anche i modelli più grandi hanno superato controlli utili di conservazione, ma le richieste sono durate minuti.

| Sistema | Modello e percorso | Token di input | Durata | Esito |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, gateway | 72,265 | 263 s | Entrambi i marcatori conservati; controllo successivo di ripresa mining superato |
| C | Gemma 3 4B, gateway | 84,044 | 88.05 s | Marcatore iniziale conservato |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Marcatore iniziale conservato |
| C | Gemma 4 12B-IT, gateway | 67,254 | 263.07 s | Marcatore iniziale conservato |
| C | Gemma 4 12B-IT, Aperture senza streaming | 67,255 | 274.24 s | Marcatore iniziale conservato |
| C | Gemma 4 12B-IT, streaming Aperture | 67,255 | 282.16 s | Marcatore iniziale conservato |
| C | Qwen3.5 9B, gateway | 75,648 | 319.36 s | Marcatore iniziale conservato, modello scaricato dalla memoria |
| C | GPT-OSS 20B, gateway | 84,099 | 315.83 s | Marcatore iniziale conservato, modello scaricato dalla memoria |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Conservazione superata sull'artefatto installato |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Conservazione superata sull'artefatto installato |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Conservazione superata sull'artefatto installato |

Lo streaming non ha eliminato l'attesa di prefill di Gemma 4 sul sistema C. Il primo contenuto è arrivato dopo 277,49 secondi, più tardi della risposta non in streaming completa da 274,24. Un tentativo precedente è andato in timeout prima della ripetizione riuscita. Terrei questa route per attività compatibili con alcuni minuti di elaborazione iniziale.

Gemma 3 4B mostra perché la qualificazione deve restare specifica per il sistema testato. Il sistema D ha mancato il marcatore iniziale in due prove di richiamo 65K, inclusa una ripetizione a temperatura zero con 67.252 token. La richiesta deterministica è terminata normalmente in 62,07 secondi con piena residenza GPU.

Una risposta rapida e una risposta API normale non dimostravano la correttezza. Userei la route riuscita del sistema C ed escluderei quella fallita del sistema D dalla selezione Hermes.

## La modalità di pensiero decide se Qwen3.5 0.8B è utile

Qwen3.5 0.8B è diventato un candidato utile per richiami circoscritti sul sistema C dopo aver disattivato il pensiero. Il piccolo modello Q8_0 ha conservato 75.649 token via gateway in 65,92 secondi. Il risultato appartiene all'artefatto Q8_0 e alla route senza pensiero testati, non alle vecchie configurazioni con contesto 16K nelle altre righe.

| Richiesta Qwen3.5 0.8B sul sistema C | Token di input | Token di output | Durata | Esito |
|---|---:|---:|---:|---|
| diagnostica breve con ragionamento predefinito | 9,050 | 3,391 | 66.56 s | Marcatore iniziale esatto |
| ragionamento disattivato, diagnostica abbinata | 9,055 | 21 | 7.65 s | Marcatore iniziale esatto, no reasoning text |
| tentativo lungo con ragionamento predefinito |  |  | Timeout 600 s | Nessuna risposta completata |
| ragionamento disattivato, Ollama nativo | 75,656 | 22 | 69.80 s | Marcatore iniziale esatto |
| endpoint compatibile OpenAI senza ragionamento | 75,646 | 12 | 69.09 s | Marcatore iniziale esatto |
| Broker con modalità senza ragionamento imposta | 75,647 | 13 | 66.83 s | Marcatore iniziale esatto |
| LiteLLM dal sistema A al sistema C | 75,649 | 15 | 65.92 s | Marcatore iniziale esatto |

La diagnostica abbinata è scesa da 66,56 a 7,65 secondi, circa 8,7 volte più rapida, mentre l'output è passato da 3.391 a 21 token. Per questo imposterei esplicitamente il ragionamento per semplici attività di estrazione e instradamento. Il ragionamento predefinito ha speso la maggior parte del lavoro in output non necessario.

Una breve prova compatibile OpenAI non ha trovato il marcatore, ma la ripetizione a temperatura zero sì. Le route riuscite usavano la modalità senza pensiero e il completamento naturale senza limite di output. Altri tre gateway hanno superato brevi richieste con marcatore in 4,22, 4,37 e 3,85 secondi. Questi controlli provano l'instradamento; i 75.649 token provano la conservazione dell'input lungo tramite gateway.

Proverei questa route per richiami limitati ed estrazione. Per il ragionamento aperto di un agente sceglierei un modello più grande. Recuperare un marcatore sintetico è più ristretto che pianificare, programmare o coordinare più strumenti.

## I sistemi RTX 3060 Ti e RTX 3070 favoriscono Qwen3.5 2B e 4B

Qwen3.5 2B e 4B sono le mie scelte pratiche iniziali per schede da 8 GB. Le prove di contesto testuale sui sistemi E, F e G sono riuscite con 65.579 token e durate da 30,343 a 93,753 secondi. Anche le route 4B testate hanno superato controlli di strumenti, streaming e immagine.

La ripetizione visiva 4B del sistema E ha conservato entrambi i marcatori e l'ordine dei colori a 65.637 token in 44,88 secondi. Sono riuscite anche richieste con ordine diretto e inverso. La ripetizione ha usato una scheda funzionante dopo che un'altra ha subito un errore di collegamento Xid 79 e il sistema è stato riavviato.

| Sistema | Contesto testuale Qwen3.5 2B | Contesto testuale Qwen3.5 4B | Contesto visivo Qwen3.5 4B |
|---|---|---|---|
| E, RTX 3060 Ti pool | 65,579 tokens, 30.343 s | 65,579 tokens, 53.787 s | 65,637 tokens, 44.88 s |
| F, RTX 3060 Ti pool | 65,579 tokens, 61.282 s | 65,579 tokens, 93.753 s | 65,635 tokens, 84.749 s |
| G, RTX 3070 pool | 65,579 tokens, 76.731 s | 65,579 tokens, 90.807 s | 65,635 tokens, 87.496 s |

Ogni sistema ha registrato 29 controlli riusciti. La differenza di tempi tra i due sistemi RTX 3060 Ti mostra perché sceglierei un profilo testato anziché classificare le schede in base a queste durate.

Tutti e sette i sistemi sono tornati al mining dopo la finestra di inferenza. Il controllo separato di recupero dopo l'arresto del sistema B è riuscito con nuove share accettate. La scheda guasta del sistema E è tornata al mining dopo un riavvio e il rafforzamento del collegamento PCIe, ma è rimasta esclusa dal pool AI. Il ripristino a fine finestra è diverso dal passaggio automatico dopo una singola richiesta.

## Caricare un modello non lo qualifica

Escluderei DeepSeek Coder V2 16B dalle scelte Hermes 65K testate. L'esecuzione con cache f16 ha conservato 50.477 token di input, ma il test 65K ha raggiunto il limite VRAM. Le cache Q4 e Q8 hanno caricato i pesi sulle GPU, poi hanno incontrato limiti di memoria host o scarso throughput dei prompt lunghi.

| Profilo cache DeepSeek Coder V2 | Contesto runtime | Risultato osservato | Valutazione |
|---|---:|---|---|
| f16 | 81,920 | recupero di 50.477 token riuscito, richiesta sovradimensionata rifiutata | Risultato utile con contesto più breve |
| f16 | 73,728 | prefill mirato a 65K interrotto a 15.802 MiB di uso GPU | Non qualificato per 65K |
| Q4_0 | 98,304 | Il prefill lungo è sceso a 96.72 token/s prima dell’arresto controllato | Poco adatto a questo carico |
| Q8_0 | 77,824 | Il prefill lungo è sceso a 120.12 token/s prima dell’arresto controllato | Poco adatto a questo carico |
| Q4_0 / Q8_0, profili più grandi | 163,840 / 98,304 | Le protezioni della memoria host hanno arrestato le prove | La capacità di memoria dipende dall’intero sistema |

La lezione pratica è testare la richiesta che si intende inviare. Residenza GPU, risposta breve e contesto configurato ampio non dimostrano la conservazione di input lungo a latenza utile.

Granite 4.2 8B e GPT-OSS 20B sono migliorati dopo lavori di follow-up specifici per route sul sistema A. La route Granite Q6_K ha conservato 66.082 token in 88,636 secondi senza input in cache. GPT-OSS ha completato il ciclo dello strumento dopo la correzione del broker: 9,854 secondi per la chiamata e 9,849 per il seguito. Terrei questi controlli riusciti separati dai tentativi incompleti precedenti.

## Risultati completi del benchmark

La tabella contiene 295 controlli su 59 combinazioni di modelli e sistemi. Registra 273 prove riuscite, una prova di richiamo fallita e sette risultati incompleti, incoerenti o incompatibili. Quattordici controlli sono fuori dall'ambito 65K. Ogni riga mostra l'esito misurato.

Le raccomandazioni riguardano le route e i carichi riusciti. Una riga fallita o incompleta non qualifica il comportamento corrispondente.

I risultati con contesto breve ed embedding valgono per i rispettivi carichi. Superare un contesto 16K o 32K non qualifica una route per il carico Hermes da 65.536 token. I nomi dei modelli qui sono etichette di route. `flash-iq2` serviva il backend compatibile IQ4.

La riga di contesto Qwen3.5 35B del sistema A è l'ultima fase con prefisso condiviso descritta sopra. Le durate degli strumenti con un segno più mostrano chiamata e seguito separatamente.

La riga di concorrenza riporta i tempi delle due richieste in coda. Quella di annullamento indica il tempo di rilascio dopo la chiusura dello stream da parte del client. Progressioni di contesto supplementari e confronti Qwen3.5 0.8B sono nelle rispettive tabelle.

### Sistema A

| Etichetta route modello | Controllo | Esito | Token di input | Durata richiesta |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Superato | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Superato | 57 | 6.429 s |
| bonsai-2-27b | stream | Superato |  | 9.371 s |
| bonsai-2-27b | tools | Superato |  | 10.478 s |
| deepseek-coder-v2:16b | context | Incompatibile | 50,477 |  |
| deepseek-coder-v2:16b | quick | Superato | 77 | 43.239 s |
| flash-iq2 | context | Superato | 66,007 | 213.25 s |
| flash-iq2 | quick | Superato |  | 56.03 s |
| flash-iq2 | stream | Superato |  | 1.35 s |
| flash-iq2 | tools | Superato |  | 16.55 s |
| gemma-4-12b-it | context | Superato | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Superato | 21 | 5.166 s |
| gemma-4-12b-it | stream | Superato |  | 4.653 s |
| gemma-4-12b-it | tools | Superato |  | 18.72 s |
| gemma-4-12b-it | vision | Superato | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Superato | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Superato | 115 | 7.467 s |
| gemma-4-e4b-it | context | Superato | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Superato | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Superato |  | 4.25 s |
| gemma-4-e4b-it | tools | Superato |  | 8.734 s |
| gpt-oss-20b | context | Superato | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Superato | 73 | 10.548 s |
| gpt-oss-20b | stream | Superato |  | 20.594 s |
| gpt-oss-20b | tools | Superato |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Superato | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Superato | 20 | 4.009 s |
| granite-4.2-3b | stream | Superato |  | 5.365 s |
| granite-4.2-3b | tools | Superato |  | 6.086 s |
| granite-4.2-8b | context | Superato | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Superato | 20 | 5.857 s |
| granite-4.2-8b | stream | Superato |  | 11.826 s |
| granite-4.2-8b | tools | Superato |  | 11.852 s |
| qwen27b | context | Superato | 66,007 | 54.64 s |
| qwen27b | quick | Superato | 57 | 31.5 s |
| qwen27b | stream | Superato |  | 0.92 s |
| qwen27b | tools | Superato |  | 4.25 s |
| qwen3-embedding-0.6b | context | Superato | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Superato | 14 | 2.125 s |
| qwen3.5-0.8b | context | Superato | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Superato | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Superato |  | 2.125 s |
| qwen3.5-0.8b | tools | Superato |  | 4.416 s |
| qwen3.5-2b | context | Superato | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Superato | 17 | 4.519 s |
| qwen3.5-2b | stream | Superato |  | 3.736 s |
| qwen3.5-2b | tools | Superato |  | 5.046 s |
| qwen3.5-4b | context | Superato | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Superato | 15 | 19.935 s |
| qwen3.5-4b | stream | Superato |  | 17.496 s |
| qwen3.5-4b | tools | Superato |  | 7.308 s |
| qwen3.5-4b | vision | Superato | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Superato | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Superato | 70 | 4.386 s |
| qwen3.5-9b | context | Superato | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Superato | 17 | 3.88 s |
| qwen3.5-9b | stream | Superato |  | 3.378 s |
| qwen3.5-9b | tools | Superato |  | 10.204 s |
| qwen3.5-9b | vision | Superato | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Superato | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Superato | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Superato |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Superato |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Superato | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Superato | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Superato | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Superato | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Superato |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Superato |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Superato | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Superato | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Superato |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Superato | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Superato | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Superato | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Superato | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Superato |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Superato |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Superato |  | 3.86 s |

### Sistema B

| Etichetta route modello | Controllo | Esito | Token di input | Durata richiesta |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Superato | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Superato | 21 | 15.261 s |
| gemma-4-12b-it | stream | Superato |  | 148.792 s |
| gemma-4-12b-it | tools | Superato |  | 34.124 s |
| gemma-4-12b-it | vision | Superato | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Superato | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Superato | 120 | 32.511 s |
| gemma3-4b | context | Superato | 65,584 | 67.382 s |
| gemma3-4b | quick | Superato | 15 | 6.329 s |
| gemma3-4b | stream | Superato |  | 24.138 s |
| gemma3-4b | vision | Superato | 306 | 7.018 s |
| gemma3-4b | vision_context | Superato | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Superato | 306 | 5.762 s |
| gpt-oss-20b | context | Superato | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Superato | 72 | 16.583 s |
| gpt-oss-20b | stream | Superato |  | 32.075 s |
| gpt-oss-20b | tools | Superato |  | 28.102 s |
| nomic-embed-text | context | Incompleto | 2,048 |  |
| nomic-embed-text | quick | Superato |  | 7.117 s |
| qwen3-14b | context | Incompleto |  | 1800.09 s |
| qwen3-14b | quick | Superato | 15 | 37.199 s |
| qwen3-14b | stream | Superato |  | 35.471 s |
| qwen3-14b | tools | Superato |  | 87.554 s |
| qwen3-8b | context | Escluso dall'ambito 65K |  |  |
| qwen3-8b | quick | Superato, fuori ambito 65K | 15 | 21.059 s |
| qwen3-8b | stream | Escluso dall'ambito 65K |  |  |
| qwen3-8b | tools | Escluso dall'ambito 65K |  |  |
| qwen3.5-9b | context | Superato | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Superato | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Superato |  |  |
| qwen3.5-9b | quick | Superato | 15 | 25.881 s |
| qwen3.5-9b | stream | Superato |  | 143.44 s |
| qwen3.5-9b | tools | Superato |  | 31.812 s |
| qwen3.5-9b | vision | Superato | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Superato | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Superato | 75 | 28.626 s |

### Sistema C

| Etichetta route modello | Controllo | Esito | Token di input | Durata richiesta |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Superato | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Superato | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Superato | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Superato | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Superato | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Superato | 27 | 20.98 s |
| gemma-4-12b-it | quick | Superato | 21 | 16.447 s |
| gemma-4-12b-it | stream | Superato |  | 15.175 s |
| gemma-4-12b-it | tools | Superato |  | 37.821 s |
| gemma-4-12b-it | vision | Superato | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Superato | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Superato | 120 | 31.25 s |
| gemma3-4b | aperture_context | Superato | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Superato | 24 | 5.42 s |
| gemma3-4b | aperture_short | Superato | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Superato |  | 3.72 s |
| gemma3-4b | context | Superato | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Superato | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Superato |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Superato |  |  |
| gemma3-4b | gateway_short_via_system_f | Superato |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Superato |  | 6.06 s |
| gemma3-4b | quick | Superato | 15 | 5.163 s |
| gemma3-4b | stream | Superato |  | 24.691 s |
| gemma3-4b | vision | Superato | 306 | 7.318 s |
| gemma3-4b | vision_context | Superato | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Superato | 306 | 5.831 s |
| gpt-oss-20b | context | Superato | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Superato | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Incoerente |  |  |
| gpt-oss-20b | quick | Superato | 72 | 21.603 s |
| gpt-oss-20b | stream | Superato |  | 31.957 s |
| gpt-oss-20b | tools | Superato |  | 26.096 s |
| nomic-embed-text | context | Incompleto, fuori ambito 65K | 2,048 |  |
| nomic-embed-text | quick | Superato, fuori ambito 65K |  | 4.178 s |
| qwen3-14b | context | Incompleto, fuori ambito 65K |  | 1800.06 s |
| qwen3-14b | quick | Superato, fuori ambito 65K | 15 | 35.809 s |
| qwen3-14b | stream | Superato, fuori ambito 65K |  | 35.43 s |
| qwen3-14b | tools | Superato, fuori ambito 65K |  | 87.723 s |
| qwen3-8b | context | Escluso dall'ambito 65K |  |  |
| qwen3-8b | quick | Superato, fuori ambito 65K | 15 | 21.293 s |
| qwen3-8b | stream | Incompleto, fuori ambito 65K |  | 900.01 s |
| qwen3-8b | tools | Escluso dall'ambito 65K |  |  |
| qwen3.5-9b | context | Superato | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Superato | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Superato | 21 | 72.14 s |
| qwen3.5-9b | quick | Superato | 15 | 24.635 s |
| qwen3.5-9b | stream | Superato |  | 143.157 s |
| qwen3.5-9b | tools | Superato |  | 30.395 s |
| qwen3.5-9b | vision | Superato | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Superato | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Superato | 75 | 28.645 s |

### Sistema D

| Etichetta route modello | Controllo | Esito | Token di input | Durata richiesta |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Superato | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Superato | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Superato | 34 | 30.74 s |
| gemma-4-12b-it | quick | Superato | 21 | 15.05 s |
| gemma-4-12b-it | stream | Superato |  | 14.722 s |
| gemma-4-12b-it | tools | Superato |  | 33.869 s |
| gemma-4-12b-it | vision | Superato | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Superato | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Superato | 120 | 29.978 s |
| gemma3-4b | context | Superato | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Fallito | 67,252 | 62.07 s |
| gemma3-4b | quick | Superato | 15 | 5.151 s |
| gemma3-4b | stream | Superato |  | 22.552 s |
| gemma3-4b | vision | Superato | 306 | 8.276 s |
| gemma3-4b | vision_context | Superato | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Superato | 306 | 5.651 s |
| gpt-oss-20b | context | Superato | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Superato | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Superato | 84 | 15.96 s |
| gpt-oss-20b | quick | Superato | 72 | 15.431 s |
| gpt-oss-20b | stream | Superato |  | 31.052 s |
| gpt-oss-20b | tools | Superato |  | 23.65 s |
| nomic-embed-text | context | Incompleto | 2,048 |  |
| nomic-embed-text | quick | Superato |  | 2.798 s |
| qwen3-14b | context | Incompleto | 40,939 | 872.209 s |
| qwen3-14b | quick | Superato | 15 | 36.021 s |
| qwen3-14b | stream | Superato |  | 33.491 s |
| qwen3-14b | tools | Superato |  | 82.471 s |
| qwen3-8b | context | Incompleto |  | 1800.07 s |
| qwen3-8b | quick | Superato | 15 | 19.283 s |
| qwen3-8b | stream | Superato |  | 19.401 s |
| qwen3-8b | tools | Superato |  | 65.054 s |
| qwen3.5-9b | context | Superato | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Superato | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Superato | 29 | 94.48 s |
| qwen3.5-9b | quick | Superato | 15 | 27.16 s |
| qwen3.5-9b | stream | Superato |  | 28.62 s |
| qwen3.5-9b | tools | Superato |  | 28.129 s |
| qwen3.5-9b | vision | Superato | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Superato | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Superato | 75 | 27.602 s |

### Sistema E

| Etichetta route modello | Controllo | Esito | Token di input | Durata richiesta |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Superato | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Superato | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Superato |  | 28.136 s |
| gemma-4-e4b-it | tools | Superato |  | 56.756 s |
| granite-4.0-h-tiny | context | Superato | 65,566 |  |
| granite-4.0-h-tiny | quick | Superato | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Superato |  | 27.798 s |
| granite-4.0-h-tiny | tools | Superato |  | 43.304 s |
| granite-4.2-3b | context | Superato | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Superato | 20 | 14.569 s |
| granite-4.2-3b | stream | Superato |  | 6.948 s |
| granite-4.2-3b | tools | Superato |  | 56.376 s |
| qwen3-embedding-0.6b | context | Superato | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Superato | 14 | 9.592 s |
| qwen3.5-0.8b | context | Superato | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Superato | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Superato |  | 11.163 s |
| qwen3.5-0.8b | tools | Superato |  | 39.214 s |
| qwen3.5-2b | context | Superato | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Superato | 15 | 12.509 s |
| qwen3.5-2b | stream | Superato |  | 26.165 s |
| qwen3.5-2b | tools | Superato |  | 42.056 s |
| qwen3.5-4b | context | Superato | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Superato | 15 | 26.736 s |
| qwen3.5-4b | stream | Superato |  | 26.02 s |
| qwen3.5-4b | tools | Superato |  | 57.293 s |
| qwen3.5-4b | vision | Superato | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Superato | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Superato | 72 | 9.96 s |

### Sistema F

| Etichetta route modello | Controllo | Esito | Token di input | Durata richiesta |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Superato | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Superato | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Superato |  | 28.042 s |
| gemma-4-e4b-it | tools | Superato |  | 73.891 s |
| granite-4.0-h-tiny | context | Superato | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Superato | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Superato |  | 27.296 s |
| granite-4.0-h-tiny | tools | Superato |  | 75.377 s |
| granite-4.2-3b | context | Superato | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Superato | 20 | 15.703 s |
| granite-4.2-3b | stream | Superato |  | 35.482 s |
| granite-4.2-3b | tools | Superato |  | 52.539 s |
| qwen3-embedding-0.6b | context | Superato | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Superato | 14 | 8.122 s |
| qwen3.5-0.8b | context | Superato | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Superato | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Superato |  | 13.266 s |
| qwen3.5-0.8b | tools | Superato |  | 40.825 s |
| qwen3.5-2b | context | Superato | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Superato | 15 | 16.738 s |
| qwen3.5-2b | stream | Superato |  | 25.29 s |
| qwen3.5-2b | tools | Superato |  | 47.444 s |
| qwen3.5-4b | context | Superato | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Superato | 15 | 33.039 s |
| qwen3.5-4b | stream | Superato |  | 25.658 s |
| qwen3.5-4b | tools | Superato |  | 71.731 s |
| qwen3.5-4b | vision | Superato | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Superato | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Superato | 70 | 27.518 s |

### Sistema G

| Etichetta route modello | Controllo | Esito | Token di input | Durata richiesta |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Superato | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Superato | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Superato |  | 43.549 s |
| gemma-4-e4b-it | tools | Superato |  | 66.616 s |
| granite-4.0-h-tiny | context | Superato | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Superato | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Superato |  | 31.751 s |
| granite-4.0-h-tiny | tools | Superato |  | 63.338 s |
| granite-4.2-3b | context | Superato | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Superato | 20 | 23.355 s |
| granite-4.2-3b | stream | Superato |  | 28.75 s |
| granite-4.2-3b | tools | Superato |  | 44.226 s |
| qwen3-embedding-0.6b | context | Superato | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Superato | 14 | 8.924 s |
| qwen3.5-0.8b | context | Superato | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Superato | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Superato |  | 15.095 s |
| qwen3.5-0.8b | tools | Superato |  | 36.672 s |
| qwen3.5-2b | context | Superato | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Superato | 15 | 20.949 s |
| qwen3.5-2b | stream | Superato |  | 25.194 s |
| qwen3.5-2b | tools | Superato |  | 37.552 s |
| qwen3.5-4b | context | Superato | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Superato | 15 | 41.84 s |
| qwen3.5-4b | stream | Superato |  | 40.812 s |
| qwen3.5-4b | tools | Superato |  | 54.999 s |
| qwen3.5-4b | vision | Superato | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Superato | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Superato | 70 | 26.283 s |

## Come ho verificato la praticabilità di Hermes

Ho usato un marcatore sintetico vicino all'inizio di un prompt lungo e ho chiesto di restituirlo dopo il testo riempitivo. La risposta doveva contenere il valore atteso. La dimensione dipendeva dai token di input riportati dal server. Un modello che rispondeva normalmente dopo un input ampio falliva comunque se sbagliava il marcatore iniziale.

La progressione Qwen3.5 35B usava record riempitivi numerati, temperatura 0 e lunghezze crescenti di 3.800, 6.800, 10.000 e 13.600 record. Le fasi hanno restituito 69.429, 124.179, 182.579 e 248.279 token. Il modello è rimasto caricato tra le fasi, consentendo il riuso del prefisso. I controlli Qwen3.6 vicini al limite hanno riportato zero token in cache.

Il prompt lungo 0.8B ripeteva `river stone lantern orchard circuit velvet compass marble` 8.400 volte tra una chiave iniziale e la domanda finale. La prova nativa usava `think:false`, `num_ctx:131072`, `stream:false` e `keep_alive:0`. La route compatibile OpenAI usava `reasoning_effort:"none"`. Il broker imponeva la modalità senza pensiero.

### Controlli di strumenti, visione e rilascio

I test degli strumenti controllavano richiesta e risposta dopo il risultato. Un test semplice usava `add_numbers(7, 11)` e si aspettava 18. Il test Qwen3.5 35B usava `lookup_square` e si aspettava 49. GPT-OSS interrogava l'inventario e doveva usare il risultato restituito.

I controlli visivi usavano domande su immagini rosse e blu, ordine invertito e prompt lunghi con colori e marcatori iniziali e finali. Il test Qwen3.5 35B usava un PNG rosso 256 × 256. Il broker ha richiesto una correzione della conversione immagini. Il test visivo lungo 4B sul sistema E richiedeva entrambi i marcatori e l'ordine dei colori.

Durante le prove ho controllato memoria GPU, residenza del modello, temperature, pressione della memoria host, eventi OOM e guasti GPU. Il controllo Qwen3.5 35B verificava anche il rilascio dopo un'interruzione controllata. I controlli successivi di annullamento client e richieste in coda hanno esercitato il broker. Due richieste in coda provano la gestione del carico testato, non due backend GPU indipendenti simultanei.

### Interpretare i risultati di prestazione

Le durate includono prefill dell'input lungo e risposta. Non sono token generati al secondo. Per lo streaming conta il ritardo al primo contenuto; le progressioni con prefisso in cache vanno interpretate separatamente.

I test di follow-up riusciti sui sistemi A e C hanno usato finestre di inferenza dedicate con mining inattivo. I modelli sono stati scaricati dopo le richieste. Il mining è stato ripristinato su tutti e sette i sistemi a fine finestra. I risultati descrivono il servizio durante l'inferenza, non mining e inferenza simultanei.

## Profili backend usati nei test

Scegli il profilo del carico che vuoi riprodurre. Quantizzazione, contesto runtime, tipo di cache, modalità di ragionamento e collocazione GPU influenzano il risultato.

| Sistema e modello | Profilo backend testato |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, cache KV f16, entrambe le RTX 5060 Ti da 16GB, 64 GiB di RAM host e contesto runtime 262.144 per la progressione lunga. Le richieste native usavano `think:false`, temperatura 0, streaming e cinque minuti di keep-alive tra le fasi. Le richieste gateway passavano tramite broker e LiteLLM. Nessun limite di output. |
| A, Qwen3.8 27B | llama.cpp su richiesta tramite broker e LiteLLM, contesto runtime 262.144, uno slot di inferenza, cache K/V Q4 ed entrambe le RTX 5060 Ti. La richiesta da 66.007 token non aveva un limite di output. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, contesto 131.072, cache KV INT8, una GPU selezionata, limite di memoria del gruppo di processi 55 GiB, limite runtime di 30 minuti, caricamento differito e scaricamento dopo 60 secondi di inattività. Risposta lunga pilota: 217 token di output. Risposta gateway vicina al limite: 11 token, nessun limite di output. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, contesto 98.304, cache KV Q4, cache esperti residente 8 GiB ed entrambe le RTX 5060 Ti. Limite memoria pilota 52 GiB, percorso successivo 54 GiB. Risposta lunga pilota: 10 token. Le precedenti combinazioni con contesto/cache maggiori si sono fermate ai limiti di memoria. |
| A, Granite 4.2 8B | Pesi GGUF Q6_K, processo di lavoro condiviso di llama.cpp, contesto 131.072, cache K/V Q4_0 e `--n-predict -1`. La richiesta lunga usava temperatura 0 e misurazione dell’uso in streaming, senza limite di output. |
| A, DeepSeek Coder V2 16B | Pesi GGUF Q4_0, Ollama 0.34.2, due RTX 5060 Ti e 64 GiB di RAM host. Le prove separate delle cache f16, Q4_0 e Q8_0 usavano i contesti runtime mostrati nella tabella di confronto. Nessun limite di output. |
| B, C, D, servizio Ollama verificato | Ollama 0.34.2, contesto 131.072, parallelismo 1, un modello caricato, coda di dimensione 128, keep-alive 0, Flash Attention e cache KV Q4_0. |
| B, prova gateway pilota Qwen3.5 9B | Timeout di percorso LiteLLM di 1.800 secondi, zero tentativi aggiuntivi e nessun limite di contesto o token di output. Entrambi i marcatori sono rimasti con 72.265 token di input. La verifica separata del ripristino del mining è passata. |
| C, Qwen3.5 0.8B | Pesi Q8_0 su una RTX 2000E Ada con profilo di potenza da 30 W. Contesto runtime 131.072. `think:false` nativo, `reasoning_effort:"none"` compatibile con OpenAI, nessun limite di output. L’alias del broker fissava il contesto e imponeva la modalità senza ragionamento. |
| C, Gemma 4 12B-IT | Profilo Ollama a GPU singola, contesto runtime 131.072 e richieste Aperture in streaming e non, senza limite di output. L’esecuzione Aperture diretta ha raggiunto 75 C e 30,64 W con il profilo configurato a 30 W, quindi ha scaricato il modello. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Artefatti esatti installati e testati tramite Aperture, contesto runtime 131.072, piena residenza su una GPU e completamento naturale senza limite di output. |
| E, F, G, processi di chat llama.cpp | Build 11669, 99 livelli GPU, parallelismo 1, Flash Attention, cache K/V Q4_0 e `--n-predict -1`. Il contesto runtime variava in base alla famiglia del modello. |

I profili registrati descrivono le proprie configurazioni runtime. Il profilo Qwen3.5 35B con cache f16 del sistema A non eredita le impostazioni Q4_0 dei sistemi Ollama più piccoli.

### Impronte dei modelli nei nuovi test di input conservato

Questi identificatori distinguono gli artefatti testati da altri download o alias con nomi simili.

| Artefatto | Quantizzazione | Digest registrato o SHA-256 file |
|---|---|---|
| Qwen3.5 35B-A3B Ollama tag | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Qwen3.5 0.8B base Ollama tag | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Granite 4.2 8B GGUF file | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

I digest dei manifest Ollama e i valori SHA-256 dei file di pesi identificano oggetti diversi. Abbina l'identificatore al tipo di artefatto nella tabella.

## Cosa userei con Hermes

Userei Qwen3.5 35B come route principale ad alto contesto sul sistema con due RTX 5060 Ti. La conservazione di 239.153 token via gateway, i controlli separati di strumenti e visione e il rilascio verificato rendono la scelta più solida di un modello che pubblicizza solo un contesto grande. Terrei Qwen3.8 27B per la risposta più rapida a 66K e Qwen3.6 quando conta una sola scheda.

Sui sistemi RTX 2000E Ada sceglierei la route Gemma 3 4B verificata del sistema C per il carico testato di risposta con input lungo. Proverei Qwen3.5 0.8B senza pensiero per richiami ed estrazione limitati. Le route più grandi Gemma, Qwen e GPT-OSS vanno bene se una risposta iniziale di quattro o cinque minuti è accettabile. Escluderei la route Gemma 3 fallita sul sistema D.

Per le RTX 3060 Ti e RTX 3070 da 8 GB partirei da Qwen3.5 2B o 4B. I risultati testuali 65K e i controlli immagini 4B sostengono una configurazione iniziale utile senza dedicare sempre le due schede da 16 GB. La pressione di memoria di Flash Next e il comportamento incompleto di DeepSeek Coder V2 a 65K li rendono impostazioni predefinite più deboli nei profili provati.

I test supportano queste scelte per flussi specifici. Conservazione dell'input, ciclo corretto di uno strumento, riconoscimento immagini e rilascio pulito coprono aspetti distinti della praticabilità di Hermes. Una configurazione affidabile deve fornire i comportamenti usati dall'agente e lasciare contesto per risposta e traffico degli strumenti.

## Fonti e letture correlate

- [Configurazione provider e requisiti di contesto Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Specifiche NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Specifiche NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Panoramica Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Scegliere un backend locale](/hermes-local-ai-broker-course/02-choose-a-backend/)
