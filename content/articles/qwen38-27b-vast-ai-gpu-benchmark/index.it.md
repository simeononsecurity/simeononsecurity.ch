---
title: "Benchmark GPU di Llama 3.1 8B e Qwen3.8 27B su Vast.ai"
date: 2026-10-02
lastmod: 2026-10-10
toc: true
draft: false
description: "Benchmark Ollama misurati di Llama 3.1 8B e Qwen3.8 27B sulle principali GPU Vast.ai. Confronta velocità di decodifica, contesto lungo, costo di noleggio, self-hosting, crediti API e abbonamenti."
genre: ["IA locale", "Benchmark GPU", "IA self-hosted", "Cloud computing", "Intelligenza artificiale", "Economia dell'IA"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "benchmark GPU", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "LLM locale", "contesto lungo", "noleggio GPU", "IA self-hosted", "modelli abliterated", "modelli senza censura", "crediti API", "abbonamento IA", "Q4_K_M", "token al secondo"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Spazio di lavoro high-tech con una scheda grafica e schermi che mostrano risultati di benchmark IA locali"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**H100 SXM è stata la scheda più veloce nei due test Ollama, ma non la più conveniente.** RTX PRO 5000 e RTX 6000 Ada hanno offerto il miglior rapporto tra velocità e costo. CMP 170HX ha avuto il prezzo orario più basso tra i test Qwen3.8 27B completati.

*Questi risultati misurano un modello, un wrapper Ollama, una quantizzazione predefinita e un solo schema di servizio. Usali per dimensionare questo carico, non per creare una classifica universale delle GPU.*

Questo articolo confronta **Llama 3.1:8b**, build Ollama Q4_K_M da 8,03 miliardi di parametri, con **Qwen3.8:27b**, build Ollama Q4_K_M da circa 27,3 miliardi di parametri. Entrambi sono stati testati su istanze GPU noleggiate da Vast.ai. I test hanno misurato il throughput di decodifica con lunghezze reali del prompt fino al limite di contesto supportato.

## Risposta breve

**Noleggia RTX PRO 5000 o RTX 6000 Ada per uso regolare da parte di un singolo utente.** RTX PRO 5000 ha guidato il confronto del valore nei contesti brevi e medi. RTX 6000 Ada costa meno e mantiene un vantaggio utile sulle A100. Noleggia H100 SXM quando la velocità conta più del prezzo orario o quando il carico include prompt lunghi.

| Obiettivo | Scelta | Motivo |
|---|---|---|
| **Costo minimo del test** | CMP 170HX | 0,420 $/ora e VRAM sufficiente per i modelli Q4_K_M testati |
| **Miglior valore sotto 1,25 $/ora** | RTX PRO 5000 o RTX 6000 Ada | Buona velocità senza il costo di H100 |
| **Risposte più rapide** | H100 SXM | Massima velocità nei due test |
| **Qwen con contesto lungo** | H100 SXM o RTX PRO 6000 Max-Q | Entrambe hanno completato il test Qwen di circa 131k token con molta VRAM libera |
| **Baseline 8B diffusa** | Llama 3.1:8b | Confronto pratico 8B con limite di contesto 128K |
| **Carico ricorrente piccolo** | Crediti API o abbonamento chat | Nessun costo GPU inattiva, manutenzione o deployment |
| **Carico privato frequente** | Workstation GPU di proprietà | L'acquisto è più facile da giustificare con uso continuo |
| **Esperimenti abliterated o senza censura** | Noleggia prima, compra solo dopo uso continuo | Comportamento, licenze e rischio operativo richiedono un test separato |

## Cosa è stato testato

**Il benchmark ha usato Ollama con la build Q4_K_M predefinita.** Non sono state aggiunte quantizzazioni speciali, speculative decoding, sampler personalizzati o stack di servizio. L'obiettivo era un confronto semplice e riproducibile delle istanze GPU.

Vast.ai descrive il servizio come un marketplace cloud che collega fornitori di calcolo e utenti. La documentazione elenca opzioni on-demand, riservate, interruptible e serverless, con filtri per GPU, memoria, prezzo e disponibilità. Le tariffe orarie provengono dalle istanze selezionate durante questa sessione, non da un listino permanente.

L'output misurato era il **throughput di decodifica**, espresso in token generati al secondo. Il throughput di prefill è separato perché misura l'elaborazione del prompt, non la velocità con cui appare la risposta. Un prompt lungo richiede spesso molto tempo anche quando la decodifica resta veloce.

Sono state usate due prove valide per contesto e registrata la mediana della decodifica. I livelli completati si basavano sui valori reali di `prompt_eval_count`:

- **Circa 16,4k token di prompt**
- **Circa 32,8k token di prompt**
- **Circa 65,5k token di prompt**
- **Circa 131k token di prompt**

Il test richiesto da 256k token non è stato completato. Le A100 da 40 GB e diverse schede più piccole stavano ancora elaborando o non hanno raggiunto il contesto obiettivo.

> **Limite del benchmark:** i valori descrivono due carichi Ollama Q4_K_M con un solo schema di servizio. Non predicono training, throughput multiutente, generazione immagini, prestazioni vLLM o il risultato di un altro modello.

## Nuovo test di Llama 3.1 8B

**Llama 3.1:8b offre una baseline pratica per lo stesso gruppo di GPU.** Ollama indica circa 120 milioni di download, quindi è una scelta ragionevole basata sulla popolarità. La [pagina ufficiale del modello Ollama](https://ollama.com/library/llama3.1:8b) indica build Q4_K_M da 4,9 GB, 8,03B parametri e contesto 128K.

Il test ha usato un runner specifico per il modello e un generatore di prompt calibrato sul tokenizer Ollama. Le etichette usano i conteggi reali:

- **Circa 32.676 token effettivi** per la destinazione 32k
- **Circa 65.342 token effettivi** per la destinazione 64k
- **Circa 130.671 token effettivi** per la destinazione 128k

Il livello 256k non è supportato perché il limite dichiarato è 128K. Il runner ha mantenuto tentativi e righe di stato, quindi un timeout resta visibile.

### Risultati di Llama 3.1 8B

| GPU | ~32k decodifica tok/s | ~64k decodifica tok/s | ~128k decodifica tok/s |
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
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Timeout |

I due record H100 provengono da istanze valide separate della stessa classe. Entrambe erano davanti alle altre schede. I risultati 32k erano più veloci del 44%–48% rispetto a RTX PRO 5000. I risultati 128k erano più veloci di circa 61%–65%.

I risultati 32k di A100 e RTX 5060 Ti sono troppo bassi per rappresentare un'esecuzione GPU comparabile. L'host RTX 5060 Ti è andato in timeout nella seconda prova 128k. Consideralo inadatto al confronto GPU valido, non come un vero risultato di classifica.

| Contesto | Stato |
|---|---|
| **32k** | Completato su tutti i 10 host |
| **64k** | Completato su tutti i 10 host |
| **128k** | Completato su 9 host. L'host 2x RTX 5060 Ti è andato in timeout nella seconda prova |
| **256k** | Non supportato da alcun host perché Llama 3.1 8B arriva a 128K |

## Confronto tra i due modelli

**Il modello Llama più piccolo era più veloce su ogni GPU comparabile, ma dimensione e qualità non sono intercambiabili.** Llama 3.1 8B è una baseline popolare con minore richiesta di memoria. Qwen3.8 27B richiede più memoria e offre capacità diverse. I numeri servono a scegliere l'hardware, non a dichiarare un modello migliore in assoluto.

| Uso | Riferimento migliore | Perché |
|---|---|---|
| **Assistente 8B rapido** | Llama 3.1:8b | Maggiore velocità e minore memoria richiesta |
| **Dimensionamento modello locale 27B** | Qwen3.8:27b | Rappresenta meglio un carico grande su una GPU |
| **Limite di contesto 128K** | Llama 3.1:8b | Il limite esplicito rende 256k non valido |
| **Test del margine VRAM** | Qwen3.8:27b | Il modello grande espone prima i limiti di memoria e contesto |
| **Baseline tra provider** | Llama 3.1:8b | Popolarità e dimensione facilitano la riproduzione |

Il precedente test Qwen ha corretto i conteggi reali a circa **32.770**, **65.538** e **131.074** token. Queste etichette sostituiscono i valori `num_ctx` richiesti nel confronto.

## Circa 16k token

**H100 SXM ha guidato il contesto breve con 134,4 token decodificati al secondo.** RTX PRO 5000 seguiva con 113,9 token al secondo e meno della metà del costo orario.

| Pos. | GPU | VRAM | Decodifica tok/s | Prefill tok/s | Tariffa |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

RTX PRO 5000 produceva circa l'84,7% della velocità H100 al 37,3% della tariffa. RTX 6000 Ada produceva il 66,3% della velocità al 30,2% del costo.

## Circa 32,8k token

**La classifica restava stabile nel contesto medio.** H100 SXM scendeva a 120,0 token al secondo, RTX PRO 5000 raggiungeva 105,0 e RTX 6000 Ada 75,7.

| Pos. | GPU | VRAM | Decodifica tok/s | Prefill tok/s | Tariffa |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

RTX PRO 5000 restava il noleggio più interessante. Era solo il 12,5% più lenta di H100 e costava il 62,7% in meno all'ora.

## Circa 65,5k token

**I prompt più lunghi hanno mostrato un divario maggiore tra schede con grande capacità e schede con meno margine.** H100 restava prima a 112,0 token al secondo. RTX PRO 6000 Max-Q superava RTX 6000 Ada.

| Pos. | GPU | VRAM | Decodifica tok/s | Prefill tok/s | Tariffa |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

RTX PRO 5000 restava il miglior equilibrio nella tabella completata. RTX 6000 Ada era più lenta, ma il prezzo inferiore favoriva i budget attenti alla disponibilità.

## Circa 131k token

**H100 era l'unica scheda oltre 100 token decodificati al secondo a questo contesto.** RTX PRO 6000 Max-Q completava a 73,4, seguita da RTX 6000 Ada a 61,7.

| Pos. | GPU | VRAM | Decodifica tok/s | Prefill tok/s | Tariffa |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | N/A | N/A | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | N/A | N/A | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | N/A | N/A | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

RTX PRO 6000 Max-Q diventava l'alternativa pratica a H100 per prompt lunghi. Offriva il 67,8% della velocità H100 al 56,0% del prezzo orario. RTX 6000 Ada costava meno, ma 48 GB di VRAM lasciavano meno spazio per prompt lunghi, batch più grandi o altre configurazioni.

## Confronto complessivo della decodifica

| GPU | ~16k | ~32,8k | ~65,5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | N/A |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | N/A |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | N/A |
| **A100 PCIe** | 38.4 | 36.1 | N/A | N/A |

**H100 guidava ogni livello completato.** Il vantaggio scendeva da 20,5 token al secondo su RTX PRO 5000 a circa 16k token a 12,0 a circa 32,8k. Il valore dipende dalla scelta tra prima risposta rapida e costo minimo per una sessione lunga.

## Costo per un milione di token decodificati

**Il prezzo orario da solo nasconde il confronto utile.** Dividere la tariffa per il throughput dà un costo approssimativo per un milione di token generati. Il calcolo ignora prefill, inattività, storage, trasferimento, tasse, sconti e test falliti.

| GPU | Tariffa contesto breve | Costo approssimativo per 1M token |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**CMP 170HX vince questo confronto aritmetico ristretto.** RTX PRO 5000 e RTX 6000 Ada seguono da vicino e offrono più throughput. Nell'uso interattivo, il tempo di attesa spesso conta più del costo minimo per token.

## Noleggiare, comprare crediti, abbonarsi o comprare hardware?

**La scelta dipende dall'utilizzo e dal controllo richiesto.** Il noleggio GPU è una spesa variabile. I crediti API sono una spesa variabile per modello. Un abbonamento chat è un costo fisso con limiti. L'hardware di proprietà richiede capitale, elettricità, raffreddamento, manutenzione e ammortamento.

| Budget mensile e carico | Percorso consigliato | Perché | Compromesso |
|---|---|---|---|
| **Meno di 10 $** | Compra crediti API o usa un modello locale gratuito | Verifica il flusso senza costo GPU inattiva | Meno controllo su hosting e limiti |
| **10–30 $** | Crediti API per uso occasionale, abbonamento chat per uso quotidiano | L'abbonamento serve al chat umano, i crediti agli script | Nessuno offre di default un endpoint privato 27B |
| **30–100 $** | Noleggia RTX 6000 Ada o PRO 5000 solo nelle sessioni attive | Copre brevi lavori e evita i costi di proprietà | Servono setup, storage, monitoraggio e arresto |
| **100–250 $** | Noleggia una scheda veloce o prova una workstation propria | L'uso mensile sostenuto diventa misurabile | Disponibilità e tariffe cambiano |
| **250–600 $** | Confronta un mese di PRO 5000 con una GPU locale | Punto decisionale per inferenza privata frequente | Più energia, calore, supporto e rischio di rivendita |
| **Oltre 600 $** | Compra solo con utilizzo alto o riserva H100 per i picchi | La strategia mista evita hardware di picco sempre fermo | Il capitale resta legato a una configurazione |

Queste fasce sono guide decisionali, non preventivi. H100 a 2,693 $/ora costa circa 64,63 $ al giorno e 1.941,00 $ per 30 giorni continui. RTX PRO 5000 a 1,005 $/ora costa circa 24,12 $ al giorno e 723,60 $ per 30 giorni. Una GPU usata solo nelle sessioni attive ha un totale diverso.

### Quando vincono i crediti API

**I crediti API vincono con uso irregolare, automazione e assenza di vincoli su un modello locale preciso.** Evitano provisioning GPU, download, problemi di driver e inattività. Permettono di confrontare modelli ospitati prima dell'acquisto.

I prezzi cambiano per modello e provider. Il catalogo OpenRouter confronta contesti, provider e prezzi per token. Usa il calcolatore live prima di confrontare una fattura API con questo benchmark. La GPU locale non applica un costo per token, ma l'ora di noleggio continua durante l'attesa.

### Quando vince un abbonamento

**Un abbonamento è adatto a chi usa ogni giorno un assistente ospitato.** I piani individuali Claude separano Free, Pro e Max con limiti e funzioni diverse. Un abbonamento non equivale all'accesso API. Offre interfaccia e strumenti integrati, mentre i crediti API offrono controllo programmatico.

Scegli un abbonamento per scrittura, ricerca, codice e revisione file interattivi. Scegli crediti API quando script, applicazione o agente richiede un endpoint misurato.

### Quando vince Vast.ai

**Vast.ai vince quando servono modello aperto, controllo privato del runtime o un picco breve di throughput.** Selezioni la GPU, avvii l'istanza, esegui Ollama, testi il modello e arresti l'istanza. È adatto a Qwen3.8 27B, varianti abliterated e file troppo grandi per un portatile.

Il costo è operativo. Verifica l'uso GPU, controlla la VRAM, proteggi il servizio esposto, conserva i file richiesti e arresta l'istanza dopo il test. Un prezzo basso non corregge un'istanza dimenticata.

### Quando vince comprare una GPU

**Comprare hardware conviene dopo uso continuo, requisiti stabili e necessità di controllo locale.** Elimina il rischio di disponibilità e offre un ambiente persistente. Permette anche di eseguire dati privati senza inviare prompt a un provider.

Il prezzo d'acquisto è solo una parte. Aggiungi sistema, alimentatore, storage, raffreddamento, elettricità, sostituzione e tempo di configurazione. Una scheda costosa resta ferma quando crediti API o abbonamento costano meno.

Le specifiche NVIDIA di riferimento RTX 4090 indicano 24 GB di memoria, 450 W di potenza grafica e 850 W di sistema minimo. È un riferimento utile, ma 24 GB sono sotto le configurazioni Q4_K_M 27B testate. Controlla l'uso reale della memoria invece di basarti solo sui parametri.

## Modelli abliterated e senza censura

**Le varianti abliterated e senza censura cambiano la decisione d'acquisto.** Possono offrire meno rifiuti o restrizioni. I costi includono sicurezza più debole, provenienza incerta, formattazione incoerente, maggiore necessità di revisione e possibili limiti di licenza o uso accettabile.

Per questi modelli, noleggia prima di comprare. Un giorno su RTX PRO 5000 al prezzo indicato costa circa 24,12 $ prima degli altri costi. Basta per verificare modello, uso GPU, qualità e rischio operativo.

**Non esporre direttamente un modello senza censura su Internet.** Metti autenticazione, limiti di velocità, controlli dei log e isolamento di rete davanti al modello. Non inviare dati personali, confidenziali o regolamentati a una fonte non verificata.

Se diventa uno strumento quotidiano, confronta il noleggio mensile con il costo completo di una workstation. Per uso occasionale il noleggio è più facile da fermare e sostituire.

## Avvertenze del benchmark

**I risultati mancanti fanno parte del risultato.** `N/A` significa che non è stata prodotta una misura valida. Non significa che la GPU sia lenta quanto suggerisce il punteggio di un'altra scheda.

- **La seconda istanza H100 non ha prodotto un set valido** perché il download del modello è finito troppo tardi.
- **L'istanza 2x RTX 5060 Ti è stata esclusa** perché Ollama ha caricato il modello sulla CPU.
- **Il prompt Qwen3.8 27B da 256k token non è stato completato.** Il livello valido massimo era circa 131k token reali. Llama 3.1 8B non supporta 256k, con limite 128K.
- **`num_ctx` richiesto non è stato usato come etichetta.** Le tabelle usano i valori reali `prompt_eval_count`.
- **Due prove valide per contesto sono state riassunte con la mediana.** Riduce l'effetto di una prova lenta, ma non sostituisce un campione maggiore.
- **Il wrapper era volutamente semplice.** Un deployment vLLM o llama.cpp ottimizzato produrrà una classifica diversa.

## Raccomandazione finale

**Inizia con RTX 6000 Ada o RTX PRO 5000 a noleggio.** RTX 6000 Ada è la scelta economica quando è disponibile a 0,813 $/ora. RTX PRO 5000 è la scelta più veloce sotto il prezzo H100. Usa H100 SXM per prompt lunghi, latenza interattiva alta o test brevi dove il tempo conta più del costo. Per un modello 8B, prova CMP 170HX se il prezzo conta più della velocità.

**Non comprare una GPU dopo un solo test riuscito.** Noleggia per un mese di carichi reali, registra ore attive, lunghezze, concorrenza e cambi modello, poi confronta il totale con il costo completo di proprietà. Compra quando il carico utilizza spesso la scheda e resta stabile.

Per uso occasionale, crediti API o abbonamento sono più semplici. Per inferenza privata, modelli aperti o test abliterated, Vast.ai richiede meno impegno iniziale. Usa Llama 3.1 8B come baseline a bassa memoria e Qwen3.8 27B quando il modello grande è l'obiettivo reale.

## Prossimi passi

Ripeti il confronto con le tue lunghezze di prompt e stima delle ore attive. Verifica l'uso GPU, registra revisione modello e versione runtime, arresta l'istanza dopo ogni prova e confronta il totale mensile con il costo completo prima di comprare.

## Riferimenti

1. [Marketplace cloud GPU Vast.ai](https://vast.ai/)
2. [Documentazione Vast.ai: marketplace, istanze, prezzi e tipi di noleggio](https://docs.vast.ai/)
3. [Libreria modelli Qwen3 di Ollama](https://ollama.com/library/qwen3)
4. [Pagina modello Llama 3.1 8B di Ollama](https://ollama.com/library/llama3.1:8b)
5. [Catalogo modelli e confronto prezzi OpenRouter](https://openrouter.ai/models)
6. [Prezzi Claude e piani individuali](https://www.anthropic.com/pricing)
7. [Specifiche NVIDIA GeForce RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [IA locale nel 2026: Qwen3.8 27B e hardware per modelli self-hosted](/articles/local-ai-2026-build-your-rig-now/)
9. [Test dei modelli Ollama su hardware Raspberry Pi](/articles/ai-models-raspberry-pi-4-5/)
