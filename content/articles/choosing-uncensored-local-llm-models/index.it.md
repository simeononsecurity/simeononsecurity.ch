---
title: "Come scegliere un modello AI locale senza censure"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Confronta le varianti locali in base a risposte complete, capacità mantenute, uso del contesto, quantizzazione e memoria VRAM necessaria."
genre: ["AI locale", "AI autogestita", "Sicurezza dell'AI", "Componenti GPU"]
tags: ["AI locale senza censure", "abliterazione", "LLM locale", "VRAM", "lunghezza del contesto", "quantizzazione", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Una workstation AI locale con una scheda grafica e monitor che mostrano visualizzazioni di modelli e inferenza"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Scelta del modello:** valuta ogni variante in base alle risposte utili che completa, alla qualità che mantiene e alla memoria richiesta dal tuo carico di lavoro. Un basso numero di rifiuti o una scheda modello popolare non dimostrano questi risultati.

L'etichetta **senza censure** non ha una scala standard di prestazioni. Chi pubblica i modelli la usa per modifiche diverse ai pesi, messa a punto e schema della conversazione. Confronta ogni candidato con il modello originale e provalo sulle attività che vuoi eseguire.

{{< youtube id="j-VqPVjztJE" enable="true" title="Ho provato tutti i modelli AI locali senza censure (da 8 GB a 32 GB di VRAM)" description="Confronto tra varianti di modelli locali, completamento delle risposte, impostazioni del contesto e livelli di memoria GPU." >}}

## Cosa indica l'etichetta

Un **modello abliterato** ha subito modifiche ai pesi per cambiare alcuni comportamenti di rifiuto. L'articolo del 2024 sulla direzione del rifiuto ha dimostrato un metodo su 13 modelli di conversazione aperti. Gli strumenti più recenti propongono altri approcci. Heretic 2, per esempio, documenta sia l'ablazione a rango arbitrario sia quella direzionale. L'etichetta di una scheda modello non indica quale comportamento è cambiato né che cosa abbia influenzato la modifica.

Quando confronti i modelli, tieni separate queste quattro proprietà:

| Proprietà | Cosa controllare |
|---|---|
| **Comportamento di rifiuto** | Quali richieste ricevono un rifiuto, una risposta parziale o una risposta completa? |
| **Capacità mantenute** | Come si confrontano con il modello originale le attività fattuali, di ragionamento, programmazione e formattazione? |
| **Completamento della risposta** | Con quale frequenza la generazione termina prima del limite di token o di tempo? |
| **Compatibilità con l'ambiente di esecuzione** | Il file quantizzato esatto funziona con memoria sufficiente per il contesto che ti serve? |

Un modello modificato resta probabilistico. **Tieni separate le verifiche di qualità:** accuratezza, affidabilità e uso sicuro. Mantieni disponibile un modello normalmente allineato per le attività in cui le sue protezioni sono importanti.

## Perché il numero di rifiuti è una classifica debole

**Un punteggio di rifiuto** misura un risultato su un insieme di richieste. Dice poco sull'accuratezza fattuale, sulla lunghezza della risposta o sulla capacità del modello di fornire una risposta finale prima di esaurire il budget di generazione.

**Il confronto di Sapwell su Qwen3.8-27B del settembre 2026** ha testato il modello base e otto varianti con la stessa configurazione di servizio. La suite di 13 attività misurava conoscenze, matematica, programmazione e veridicità. Un insieme separato di HarmBench conteneva 400 richieste dannose e un giudice LLM ha esaminato le risposte complete. Questi risultati riguardano una famiglia di modelli, una GPU e un disegno di valutazione.

| Variante Qwen3.8-27B nello studio | Rifiuti espliciti su 400 | Risposte con ragionamento incompleto |
|---|---:|---:|
| **Modello base** | 381 | 0% |
| **OrcaRouter** | 2 | 38% |
| **Trohrbaugh** | 122 | 15% |

L'alto numero di rifiuti del modello base coincideva con meno risposte incomplete. Il basso numero di rifiuti di OrcaRouter coincideva con una percentuale maggiore di risposte non completate. Trohrbaugh manteneva più rifiuti e produceva meno risposte incomplete. **Scegli in base al tuo compito e ai compromessi che accetti.**

**Uno studio su 23 varianti di Gemma 4 E4B** ha rilevato perdite sostanziali in alcune misure di capacità per la variante più scaricata, mentre una modifica minore è rimasta vicina al modello base nel test. Popolarità e numero di download descrivono l'adozione. Non misurano la qualità.

Non combinare queste misurazioni in un singolo punteggio. **Separa le misure:** rifiuto, completamento, correttezza e latenza. Registra anche l'insieme di richieste, la revisione del modello, lo schema della conversazione, l'ambiente di esecuzione, il contesto e il limite di uscita. Modificare una di queste impostazioni cambia il significato del confronto.

## Diagnostica le risposte vuote prima di sostituire un modello

**I token di ragionamento** consumano il limite di uscita prima che compaia il testo visibile. Se il limite si esaurisce durante il ragionamento interno, alcuni ambienti di esecuzione restituiscono una risposta vuota o troncata. Questo esito è diverso da un rifiuto o da una risposta completa ma errata.

**Il benchmark Qwen3.6-27B di Sapwell** ha mostrato come questo fenomeno influenzi i punteggi principali. I punteggi matematici grezzi variavano molto perché alcune esecuzioni non arrivavano mai alla risposta finale. Tra le risposte completate, i valori di accuratezza misurati erano molto più vicini. Il benchmark separava la capacità di risposta dall'esaurimento del budget di ragionamento.

**Quando una risposta è vuota, controlla il motivo di arresto dell'ambiente di esecuzione e i log.** Registra la lunghezza della richiesta, l'allocazione del contesto, il limite di token in uscita, il tempo trascorso e l'eventuale presenza di un marcatore di risposta finale. Poi ripeti la richiesta con un limite di uscita maggiore, se l'attrezzatura ha spazio sufficiente.

| Esito | Categoria probabile da verificare |
|---|---|
| **Testo di rifiuto** | Il modello ha rifiutato la richiesta. |
| **Risultato vuoto al limite di token** | La generazione ha esaurito il budget di uscita prima della risposta finale. |
| **Uscita troncato** | Il limite di generazione ha interrotto una risposta incompleta. |
| **Errore dell'ambiente di esecuzione** | Il server, il file del modello o l'allocazione della memoria non hanno funzionato. |
| **Risposta completa ma errata** | Il modello ha prodotto testo, ma non ha superato la verifica di correttezza. |

**Risultato vuoto:** verifica l'esito dell'ambiente di esecuzione prima di chiamare ogni caso un difetto del modello. Una finestra di contesto più ampia non corregge automaticamente un limite di uscita ridotto, uno schema malformato o un timeout dell'applicazione.

## Riserva VRAM per pesi e contesto

Il file del modello è solo uno dei componenti che consumano memoria. L'ambiente di esecuzione ha bisogno di spazio anche per la **cache KV**, che conserva lo stato di attenzione della richiesta e della risposta attive, oltre ai buffer di calcolo e agli altri processi caricati. Aumentare la lunghezza del contesto aumenta l'uso di memoria.

**La documentazione attuale di Ollama** indica finestre di contesto predefinite di 4K sotto i 24 GiB di VRAM, 32K tra 24 e 48 GiB e 256K con 48 GiB o più. Questi valori descrivono il comportamento predefinito dell'ambiente di esecuzione. Controlla il contesto allocato e il posizionamento del processore con `ollama ps`.

**Esempio Linux:** questo comando imposta un valore predefinito di 16K per le nuove sessioni del server Ollama:

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Verifica il contesto allocato** rispetto alle dimensioni normali di input e risposta con il modello caricato:

```bash
ollama ps
```

Le colonne `CONTEXT` e `PROCESSOR` mostrano l'allocazione e se il modello è sulla GPU o parzialmente spostato fuori dalla GPU. **Allocazione del contesto:** un limite elencato non garantisce che l'intera finestra entri nella VRAM.

### Punti di partenza in base alla memoria GPU

**Candidati iniziali:** queste famiglie di modelli sono apparse nei confronti di varianti del 2026. Le dimensioni dei file provengono da repository di quantizzazioni specifiche. Prima di considerare adatto un candidato, conferma il file preciso, il supporto dell'ambiente di esecuzione e la memoria misurata.

| Memoria GPU | Candidato iniziale | Vincolo principale |
|---|---|---|
| **8 GB** | Gemma 4 E4B, per esempio la variante `coder3101` | Mantiene piccolo il file dei pesi. Lascia memoria per il contesto e i buffer dell'ambiente di esecuzione. |
| **12 GB** | Gemma 4 12B, per esempio il file GGUF Q4 da 7,4 GB di `TrevorJS` | Offre maggiore capacità al modello, ma meno spazio per un contesto lungo rispetto a una variante più piccola. |
| **16 GB** | Un modello più piccolo o un file Q3 di Qwen3.8-27B | Il repository Qwen indica 13,72 GB per Q3_K_S. Chi pubblica il file lo definisce di bassa qualità. Lo spazio per il contesto sarà limitato. |
| **24 GB** | Qwen3.8-27B Q4_K_S o Q4_K_M | Il repository attuale indica file da 16,71 GB e 17,77 GB. Riserva spazio per cache e buffer. |
| **32 GB** | Qwen3.8-27B Q6_K | Il repository attuale indica un file da 23,46 GB. Un file più grande lascia meno memoria per il contesto rispetto a una quantizzazione più piccola. |

*Usa queste opzioni come punto di partenza. I repository e le versioni cambiano e la dimensione del file, da sola, non predice l'allocazione della memoria dell'ambiente di esecuzione o la qualità delle risposte.*

Le etichette di quantizzazione GGUF riassumono una scelta di codifica. **Differenze tra repository:** file con la stessa profondità nominale in bit non garantiscono la stessa qualità. Un repository Qwen definisce Q3_K_S di bassa qualità e Q4_K_M la scelta predefinita. Prima di scaricare, controlla la dimensione esatta del file, la scheda del modello, il formato della richiesta e i risultati dei test.

**Per dimensionare la cache e verificare l'uso di una GPU locale,** consulta la [guida locale a modelli, GPU e contesto](/articles/local-ai-model-gpu-context-guide/). Le sue raccomandazioni si concentrano sulle attività di programmazione. Questa pagina tratta il comportamento di rifiuto modificato e la valutazione.

## Controlla lo schema della conversazione e la provenienza del modello

Uno **schema della conversazione** avvolge i messaggi nei token e nelle istruzioni attese dal modello. Un pacchetto del modello a volte include uno schema personalizzato o un'istruzione di sistema. Queste modifiche influenzano il comportamento misurato anche se i pesi sottostanti restano invariati.

**Effetto dello schema:** Sapwell ha trovato una variante Qwen3.8 il cui pacchetto includeva una personalità che istruiva il modello a non rifiutare o avvertire mai. La sua dichiarazione sul basso numero di rifiuti dipendeva dallo schema. Il confronto standardizzava gli schemi per mettere in evidenza le differenze tra i pesi. Questo controllo non dimostra che lo schema fornito sia malevolo o inutilizzabile.

**Prima dell'installazione:** verifica chi pubblica il modello, il modello base, la licenza, il processo di conversione, il quantizzatore, lo schema e la cronologia delle revisioni. Confrontalo con il modello originale usando lo stesso schema e ambiente di esecuzione. Se la scheda del modello non descrive il metodo o la configurazione di test, registra la provenienza come sconosciuta.

## Esegui una valutazione ridotta per il tuo carico di lavoro

**Prepara un insieme di richieste ripetibile** partendo da attività ordinarie che ti appartengono o che hai il permesso di testare. Includi il lavoro che il modello svolgerà, domande fattuali con risposte note e richieste di formattazione con criteri di superamento chiari. Aggiungi alcuni casi di confine sicuri, così il comportamento di rifiuto resta parte della decisione.

**Mantieni fisse le impostazioni di test** tra il modello originale e la variante modificata. Non cambiare l'istruzione di sistema, lo schema, la quantizzazione, la versione dell'ambiente di esecuzione, il contesto, il limite di uscita o le impostazioni di campionamento. Salva la revisione del modello o l'hash del file insieme ai risultati.

Registra separatamente ogni esito:

- **Completamento:** risposta finale, rifiuto, uscita vuoto, troncamento o errore dell'ambiente di esecuzione.
- **Correttezza:** superamento o fallimento rispetto a una risposta attesa o a una rubrica.
- **Utilità:** se la risposta soddisfa i requisiti dell'attività.
- **Latenza:** tempo al primo token e tempo totale di generazione.
- **Memoria:** contesto allocato, posizionamento sulla GPU e VRAM di picco.
- **Comportamento di sicurezza:** rifiuto o prosecuzione appropriati per ogni caso di confine.

Ripeti l'insieme dopo aver cambiato una sola variabile. Se l'aumento del limite di uscita completa la risposta, il primo errore dipendeva dal budget. Se le risposte restano incomplete, controlla lo schema del modello, la modalità di ragionamento, l'ambiente di esecuzione e la revisione del modello. **Mantieni la variante solo se migliora l'attività obiettivo senza perdite inaccettabili di accuratezza o sicurezza.**

## Mantieni isolata la distribuzione

**Privacy:** l'inferenza locale dipende dall'intero sistema. Controlla l'interfaccia, i log, le estensioni, la telemetria e i percorsi di rete. Tratta i pesi non attendibili e gli schemi personalizzati come codice e configurazione di terze parti.

**Accesso pubblico:** non esporre mai direttamente l'endpoint del modello a Internet. Isola l'accesso agli strumenti e usa varianti modificate solo per attività autorizzate. Per l'accesso remoto, colloca l'endpoint dietro un gateway privato con autenticazione, limiti di frequenza e isolamento di rete. L'articolo originale sulla direzione del rifiuto descrive le implicazioni di sicurezza delle modifiche che eliminano i rifiuti.

## Conclusione

**Regola decisionale:** scegli il modello con i risultati verificati più solidi sul tuo insieme di attività. Usa il numero di rifiuti come una misura, poi controlla il completamento delle risposte, la correttezza, il comportamento dello schema e lo spazio VRAM disponibile. Inizia con un file adatto alla tua GPU, imposta il contesto per il tuo carico di lavoro e confrontalo con il modello originale a impostazioni identiche.

**Per dimensionare la GPU,** confronta questi risultati con il [benchmark di noleggio GPU per Qwen 27B](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Noleggia o prendi in prestito attrezzatura prima di acquistarlo se non conosci il file esatto del modello o il contesto necessario.

## Fonti

- [Benchmark di abliterazione Qwen3.8-27B](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6 settembre 2026.
- [Benchmark di abliterazione Qwen3.6-27B](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmark delle varianti Gemma 4 E4B](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1 agosto 2026.
- [Benchmark delle varianti Gemma 4 12B](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28 agosto 2026.
- [Il rifiuto nei modelli linguistici è mediato da una singola direzione](https://arxiv.org/abs/2406.11717), Arditi et al., 2024.
- [Documentazione del progetto Heretic](https://github.com/p-e-w/heretic/).
- [Scheda ufficiale del modello Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Documentazione Ollama sulla lunghezza del contesto](https://docs.ollama.com/context-length).
- [Scheda del modello Gemma 4 E4B `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [File GGUF Gemma 4 12B di TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [File GGUF OrcaRouter Qwen3.8-27B](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [Formato GGUF e tipi di quantizzazione](https://huggingface.co/docs/hub/en/gguf), documentazione Hugging Face.
- [Fonte video: Ho provato tutti i modelli AI locali senza censure (da 8 GB a 32 GB di VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).
