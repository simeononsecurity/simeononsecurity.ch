---
title: "Hindsight self-hosted: memoria locale per agenti e instradamento privato dei modelli"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Caso di studio su Hindsight self-hosted, percorsi Qwen locali osservati e lavoro GPU per richiesta senza abbonamento a modelli ospitati nei percorsi ispezionati."
genre: ["IA locale", "IA self-hosted", "Agenti IA", "Infrastruttura IA", "Privacy"]
tags: ["Hindsight", "Hindsight self-hosted", "memoria degli agenti", "IA locale", "LLM locale", "Qwen3.5", "LiteLLM", "VPN privata", "gateway dei modelli", "embedding", "reranking", "pianificazione GPU", "inferenza privata", "Docker", "banchi di memoria", "pagine di conoscenza", "instradamento di modelli locali"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Un servizio di memoria privata instrada le attività verso server di modelli locali su CPU e GPU"
coverCaption: "Memoria, recupero e percorsi dei modelli ispezionati funzionano su hardware di proprietà"
---

**Il nostro servizio di memoria Hindsight funziona su hardware che controlliamo.** Il motore di memoria, il database, il modello di embedding e il reranker funzionano in un unico deployment self-hosted. Hindsight invia le richieste di generazione a un gateway privato. Il backend Qwen condiviso ispezionato e il percorso di aggiornamento delle pagine testato usano server di modelli locali, senza un abbonamento a inferenza ospitata.

Questa è la descrizione di un deployment operativo. **Self-hosted non significa offline.** La VPN usa un servizio esterno di coordinamento, e le immagini software e i pesi dei modelli devono essere scaricati. L’affermazione riguarda l’elaborazione della memoria e l’inferenza del modello, non ogni connessione di rete dei nostri dispositivi o degli altri strumenti degli agenti.

<!--more-->

## Punti chiave

- **Hindsight gestisce il flusso della memoria.** Un container Docker serve API, worker e piano di controllo. Un volume persistente conserva i dati dei banchi.
- **I piccoli modelli di recupero restano locali.** Embedding e reranking funzionano nel processo Hindsight sulla CPU.
- **Qwen genera il testo.** Retain, Reflect e Consolidation richiedono l’alias privato Qwen3.5-4B con ragionamento disattivato e output limitato. Il backend ispezionato lo serve localmente.
- **L’aggiornamento lento delle pagine riceve una GPU.** Un alias separato prende in prestito una scheda per una richiesta in background e la rilascia al termine.
- **Il gateway nasconde la posizione fisica.** Hindsight sceglie un alias del modello. I servizi di instradamento privati scelgono l’endpoint di servizio.

## Definisci i confini prima di scegliere i modelli

**Hindsight è il motore di memoria, non il server dei modelli.** L’immagine Docker completa include modelli locali per embedding e reranking, ma la generazione linguistica richiede un endpoint. La [guida all’installazione di Hindsight](https://hindsight.vectorize.io/developer/installation) spiega questa distinzione e mostra server locali llama.cpp, Ollama e vLLM come alternative ai provider ospitati.

**L’API della memoria resta sulla rete privata.** Il piano di controllo web funziona su un’interfaccia locale. Un volume persistente conserva il database incorporato, così ricreare il container non elimina i banchi. L’autenticazione protegge l’API e i banchi separati organizzano il contesto dei progetti.

**Il gateway di generazione fornisce nomi di modello stabili.** Hindsight invia richieste compatibili con OpenAI attraverso il gateway privato e la VPN. Il gateway le inoltra agli endpoint locali. Il percorso Qwen ispezionato raggiunge un deployment LiteLLM associato a un server CPU locale. La [documentazione del router LiteLLM](https://docs.litellm.ai/docs/routing) descrive questo schema di alias. Un altro router compatibile con OpenAI può svolgere lo stesso ruolo.

{{< figure src="hindsight-private-request-path.webp" alt="Diagramma con agenti, un servizio Hindsight privato, modelli locali di recupero, un gateway privato e server Qwen locali" caption="Il diagramma omette nomi host, indirizzi, chiavi di accesso e nomi degli host fisici" >}}

[Apri il diagramma completo del percorso della richiesta](hindsight-private-request-path.webp).

**Esiste comunque un’API interna.** Hindsight chiama un gateway privato usando il formato compatibile con OpenAI. I percorsi ispezionati servono l’inferenza localmente. Non abbiamo verificato tutte le regole di fallback del gateway. Controllane la policy prima di considerare locale l’elaborazione di ogni richiesta.

## Assegna ogni attività di memoria al calcolo giusto

Le operazioni di Hindsight svolgono lavori diversi. **Retain** estrae fatti dal nuovo materiale. **Recall** trova ricordi pertinenti. **Reflect** cerca e scrive una risposta sintetizzata. **Consolidation** unisce fatti correlati. L’**aggiornamento delle pagine di conoscenza** ricostruisce un riepilogo aggiornato dal banco.

| Operazione | Posizione del modello | Motivo |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B tramite il gateway privato | Estrazione strutturata locale con budget di output limitato |
| **Recall** | Embedding e reranking locali su CPU | La ricerca non richiede una chiamata all’API di generazione |
| **Reflect** | Qwen3.5-4B tramite il gateway privato | La sintesi richiede generazione dopo il recupero della memoria |
| **Consolidation** | Qwen3.5-4B tramite il gateway privato | I batch piccoli limitano le risposte strutturate lunghe |
| **Aggiornamento di una pagina di conoscenza** | Percorso Qwen locale dedicato su GPU | La grande sintesi in background superava il limite di tempo del percorso CPU |

*Tieni i piccoli lavori di recupero sulla CPU e riserva l’inferenza GPU al lavoro lungo che hai misurato.*

Il container Hindsight carica **BAAI/bge-small-en-v1.5** per gli embedding e **hindsight-ai/hs-rerank-1** per il reranking. I log di avvio confermano che entrambi funzionano localmente su CPU. La [referenza dei modelli Hindsight](https://hindsight.vectorize.io/developer/models) documenta le opzioni locali e il percorso facoltativo del modello decisionale.

Abbiamo mantenuto il modello di embedding esistente perché cambiare lo spazio di embedding richiede di ricostruire i vettori salvati. Il reranker è già locale, quindi un servizio di reranking ospitato aggiungerebbe un nuovo confine dei dati senza risolvere il timeout di generazione osservato. Un test locale di **hs-decide-1-flash** ha prodotto una risposta Reflect corretta, ma il risultato è terminato vicino al limite di tempo del test. I dati sintetici di Consolidation non hanno esercitato il percorso decisionale. Perciò il modello decisionale non è incluso nell’instradamento di produzione.

## Assegna una GPU al lavoro lento in background

**Il nome del modello normale e quello per l’aggiornamento sono diversi.** Retain, Reflect e Consolidation usano l’alias Qwen condiviso. L’aggiornamento delle pagine in background usa un alias GPU specifico del nodo con una sola chiamata simultanea al modello linguistico. Questo limita un lungo lavoro di manutenzione a una GPU per volta.

**Una prenotazione associata alla richiesta limita l’uso della GPU.** Il pool GPU avvia un worker di modello quando arriva una richiesta. Il controller prenota una scheda, serve la richiesta, arresta il worker e libera la prenotazione. Il diagramma omette l’inventario degli host fisici.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagramma di una GPU prenotata per aggiornare una pagina in background e liberata al termine della richiesta" caption="Un lease associato alla richiesta prenota una GPU per aggiornare una pagina" >}}

[Apri il diagramma completo del ciclo di prenotazione GPU](hindsight-gpu-lease-cycle.webp).

Questa distinzione deriva da un errore che abbiamo misurato. **Un aggiornamento di pagina prima su CPU ha raggiunto il limite di un’ora.** Dopo aver instradato gli aggiornamenti in background al pool GPU locale, cinque pagine fallite in precedenza sono state completate in circa due-sei minuti in una procedura di recupero. Questi valori descrivono quelle pagine e impostazioni. Non sono un benchmark generale del throughput Qwen.

## Correggi i valori predefiniti e i timeout

**I precedenti limiti di output di Hindsight non erano adatti al nostro router locale.** Il router accetta fino a 8.192 token di output e applica 256 token quando la richiesta non specifica un limite. Un precedente limite Retain di 64.000 token ha causato HTTP 400. I batch Consolidation da otto fatti si fermavano per la lunghezza dell’output e Reflect richiedeva un limite esplicito per evitare il fallback del router a 256 token.

**Abbiamo reso espliciti i limiti di ogni attività.** Il ragionamento Qwen è disattivato per queste operazioni di memoria. Hindsight ora consente quattro chiamate LLM simultanee in totale, incluse al massimo una chiamata di aggiornamento pagine in background. Il timeout LLM globale è di 1.800 secondi con un nuovo tentativo del modello.

| Carico di lavoro | Limite di output o batch | Limiti della chiamata e dell’operazione |
| --- | --- | --- |
| **Retain** | 8.192 token di output | Timeout generale della chiamata: 1.800 secondi |
| **Reflect** | 4.096 token di output | 900 secondi per chiamata, 3.600 secondi per operazione |
| **Consolidation** | 4.096 token di output, quattro fatti per chiamata | 900 secondi per chiamata, 14.400 secondi per operazione |
| **Aggiornamento pagina** | Una chiamata simultanea al modello | 900 secondi per chiamata, percorso GPU dedicato |

*Questi valori descrivono il nostro deployment di novembre 2026 e il relativo router locale.*

**Il timeout di una chiamata e il limite di un’operazione controllano fasi diverse.** Alcune chiamate Qwen valide superavano il precedente timeout di 300 secondi per chiamata. I limiti di operazione più lunghi consentono lavori con più chiamate, mentre i 900 secondi per chiamata continuano a limitare ogni tentativo.

Nel recupero, varie attività Retain hanno completato con **1.042-2.076 token di output**. Due esecuzioni di Consolidation hanno completato **41 su 41** e **30 su 30** elementi. In seguito, la scadenza del limite di un aggiornamento pagina ha portato al percorso GPU separato descritto sopra. Questi risultati non dimostrano affidabilità a lungo termine.

## Cosa comporta questo progetto

**Nessuna fattura per un modello ospitato non significa costo zero.** Il deployment usa hardware di proprietà, elettricità, archiviazione, tempo di manutenzione e tempo GPU durante gli aggiornamenti. Ogni scelta di posizione scambia capacità per latenza o semplicità operativa.

| Scelta | Vantaggio | Compromesso |
| --- | --- | --- |
| **Generazione prima su CPU** | Mantiene disponibile la GPU | Un aggiornamento testato ha raggiunto il limite di un’ora |
| **Aggiornamento delle pagine su GPU** | Cinque pagine sono terminate in circa due-sei minuti in un’esecuzione | Usa capacità GPU e dipende dal percorso dedicato |
| **Database incorporato** | Mantiene compatto il deployment | Restringe il dominio di errore e richiede test di backup |

*Usa un percorso di aggiornamento GPU quando la latenza CPU misurata supera la tua finestra di manutenzione.*

La [guida all’installazione di Hindsight](https://hindsight.vectorize.io/developer/installation) raccomanda PostgreSQL separato per deployment di produzione più grandi. **Il nostro database incorporato ha bisogno di un percorso di backup e ripristino testato** man mano che il banco cresce.

**L’inferenza privata dipende dal percorso.** Controlla il provider Hindsight selezionato, la mappatura dei modelli del gateway, le regole di fallback, il processo locale del modello, la conservazione dei log e il traffico in uscita. Gli ID di traccia di Hindsight aiutano a correlare le richieste e Docker ruota i log del container. Nessuna delle due misure prova che una richiesta successiva sia rimasta locale. Un audit del gateway fornisce la prova end-to-end mancante.

## Raccomandazione

**Inizia con modelli di recupero locali e limiti di generazione espliciti.** Esegui Hindsight e i modelli di embedding e reranking su hardware di proprietà. Instrada la generazione tramite un gateway privato compatibile con OpenAI usando una VPN. Misura ogni operazione prima di assegnare capacità CPU o GPU, e riserva il percorso GPU ai lavori in background la cui latenza CPU supera la finestra di manutenzione.

*Esamina ogni fallback del gateway e prova il ripristino dei banchi prima di considerare il deployment privato e resiliente.* La [guida ai confini della privacy dell’IA locale](/articles/local-ai-privacy-boundary/) offre una lista di controllo iniziale.

## Conclusione

**Questo deployment mantiene la memoria Hindsight e i percorsi di inferenza ispezionati su hardware di proprietà, senza un abbonamento a modelli ospitati.** Il recupero CPU, le chiamate Qwen limitate e il percorso GPU di aggiornamento con una chiamata gestiscono carichi diversi. Le procedure di recupero hanno completato Retain, Consolidation e gli aggiornamenti delle pagine con queste impostazioni. I prossimi controlli sono l’audit di tutti i fallback del gateway, la prova dei backup e un’osservazione più lunga dell’affidabilità.
