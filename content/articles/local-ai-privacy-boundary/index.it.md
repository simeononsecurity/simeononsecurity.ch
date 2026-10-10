---
title: "Privacy dell'IA locale: cosa resta sul computer e cosa no"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Traccia prompt, file del modello, strumenti, log, esposizione di rete e costi energetici prima di scegliere l'inferenza locale o un servizio IA ospitato."
genre: ["IA locale", "Privacy", "IA self-hosted", "Cybersecurity", "Economia dell'IA"]
tags: ["privacy IA locale", "inferenza locale", "IA cloud", "privacy dati IA", "IA self-hosted", "privacy LLM", "costo possesso GPU", "costo elettricità IA", "RTX 5070", "Claude Haiku 5.5", "privacy Ollama", "llama.cpp", "sicurezza IA", "IA offline", "modelli linguistici locali", "privacy prompt", "modello minacce IA", "break-even GPU", "confine dati IA", "IA privata"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Una workstation IA locale collegata a un servizio cloud da percorsi dati visibili"
coverCaption: "Illustrazione dei percorsi dati dell'IA locale e ospitata"
---

**L'IA locale riduce il confine dei dati.** Un prompt elaborato da un runtime locale resta sul dispositivo quando modello, strumenti, log e percorso di rete restano locali. Una GPU locale non rende il computer un sistema isolato.

Runtime dei modelli, plugin degli strumenti, estensioni del browser, accesso remoto, API esposte e download dei modelli definiscono ancora il rischio. Conta anche il costo. L'elettricità può costare meno di un prezzo cloud per token, mentre il possesso dell'hardware sposta il punto di pareggio complessivo molto avanti nel tempo.

Questa guida mappa prima il confine della privacy. Poi verifica il costo con i prezzi attuali dei fornitori, un'ipotesi esplicita di consumo e i dati riportati dal video fornito.

<!--more-->

Questo confronto tra costi locali e ospitati fornisce il contesto per le formule sotto. Non copiare i dati di velocità senza testare lo stesso file del modello e lo stesso runtime sul tuo hardware.

{{< youtube id="DmkuFpoMYmc" enable="true" title="L'IA locale conviene? Abbiamo confrontato i costi con Claude Haiku 5.5" description="Confronto dei costi tra IA locale e ospitata." >}}

Il video riporta una durata di 2 minuti e 31 secondi. Ho verificato titolo e durata nella pagina di visione. Non ho ripetuto il test hardware, quindi le velocità restano misure riportate dalla fonte.

## La risposta breve

- **Scegli l'inferenza locale per un percorso dati controllato.** Mantieni il server del modello sul dispositivo, legalo al loopback e limita l'accesso agli strumenti.
- **Scegli l'inferenza ospitata per l'uso occasionale.** Evita la spesa hardware quando il carico è ridotto o il modello preferito non entra nel sistema.
- **Tratta il costo locale come due numeri.** Separa l'elettricità per ora attiva dal possesso dell'hardware.
- **Tratta la privacy come una proprietà del sistema.** Un modello privato perde il vantaggio quando un plugin carica file o un'API locale ascolta su ogni interfaccia di rete.

L'inferenza locale aiuta quando il testo sensibile deve restare in una workstation o rete isolata. Aiuta anche con il funzionamento offline, una versione fissa del modello o un accesso prevedibile senza quota del fornitore.

Questi vantaggi non provano risposte migliori. Un modello ospitato può adattarsi meglio a un'attività, finire più rapidamente o richiedere meno manutenzione. Misura il carico prima di comprare hardware.

## Traccia il percorso dei dati

Mappa ogni componente coinvolto in una richiesta. Il solo nome del modello non mostra dove viaggiano i dati.

| Componente | Domanda sulla privacy | Evidenze da raccogliere |
|---|---|---|
| **Server del modello locale** | Il prompt resta sull'host? | Configurazione del processo, indirizzo di ascolto e traffico in uscita |
| **Modello cloud** | Quali testi, file e risultati degli strumenti lasciano l'host? | Endpoint API, condizioni del fornitore, log delle richieste e impostazioni dell'account |
| **Modalità cloud in un'app locale** | Il modello selezionato gira sul dispositivo? | Identificatore del modello, etichetta del fornitore e connessione di rete |
| **Plugin dello strumento** | Il modello riceve file, output della shell o contenuti del browser? | Elenco strumenti, permessi e dati delle richieste catturate |
| **Download del modello** | Quale codice e quali pesi entrano nell'host? | Repository sorgente, licenza, checksum della release e percorso di download |
| **Log locali** | Dove restano prompt e risultati degli strumenti? | Log del runtime, cronologia shell, report di crash e ambito dei backup |

**Un modello locale rimuove un fornitore dal percorso del prompt.** Non elimina la necessità di controllare il resto del percorso.

## Locale non significa privato per impostazione predefinita

[La privacy policy di Ollama](https://ollama.com/privacy) afferma che Ollama non vede prompt o dati quando un modello gira localmente. La policy separa anche l'uso locale dai modelli ospitati nel cloud. Un modello cloud crea ancora un confine di servizio, anche quando la stessa applicazione avvia entrambe le modalità.

[La documentazione del server llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) mostra un server locale in ascolto su `127.0.0.1:8080` per impostazione predefinita. Gli esempi Docker mostrano anche `--host 0.0.0.0`, che espone il servizio su tutte le interfacce. Un indirizzo di bind più ampio cambia il confine di accesso.

Controlla l'indirizzo di ascolto prima di inviare testo sensibile:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

`127.0.0.1` o `localhost` limita normalmente l'accesso allo stesso host. Un indirizzo LAN o `0.0.0.0` richiede una regola firewall e un piano di autenticazione. Non esporre un endpoint del modello a una rete prima di aver testato entrambe le condizioni.

Controlla anche il nome del modello selezionato. La documentazione cloud di Ollama descrive i modelli cloud come un percorso di servizio distinto. Un'interfaccia locale non prova l'esecuzione locale.

Le [FAQ di Ollama](https://docs.ollama.com/faq) documentano una modalità solo locale. Imposta `disable_ollama_cloud` in `~/.ollama/server.json`, oppure imposta `OLLAMA_NO_CLOUD=1` prima di riavviare il servizio. Questo rimuove i modelli cloud e la ricerca web di Ollama dal runtime selezionato. Non limita altre applicazioni, strumenti del browser, plugin o accessi di rete sull'host.

```json
{
  "disable_ollama_cloud": true
}
```

Verifica l'impostazione dopo il riavvio. Un runtime solo locale restringe un percorso. Non stabilisce un host privato.

## Conta il costo ospitato

I prezzi dei token separano input e output. [Anthropic indica Claude Haiku 5.5 a 0,10 $ per milione di token di input e 0,50 $ per milione di token di output per prompt fino a 100.000 token](https://www.anthropic.com/claude/haiku). I prompt sopra 100.000 token usano le tariffe superiori indicate.

[La guida ai token di OpenAI](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) spiega perché il conteggio delle parole non equivale al conteggio dei token. Separa anche token di input, output, input memorizzati e ragionamento. Usa i campi di utilizzo del fornitore invece di una stima basata sulle parole.

Per un confronto semplice, usa un milione di token generati e un milione di token di input come carichi separati. Un agente di coding invia spesso contesto ripetuto e produce una risposta più piccola, quindi un unico totale nasconde la combinazione dei costi.

## Calcola la potenza locale

[L'annuncio di lancio della RTX 5070 di NVIDIA](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) indicava un prezzo iniziale di 549 $. [La pagina della famiglia RTX 5070 di NVIDIA](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) indica 12 GB di memoria e 250 W di potenza grafica totale per il design di riferimento Founders Edition. La pagina prodotto NVIDIA indica ancora 549 $ e mostrava la scheda esaurita durante questa verifica.

Il dato di potenza della GPU non è il consumo dell'intero sistema. Usa un wattmetro per il PC. L'esempio seguente assume un **consumo dell'intero sistema di 400 W**, includendo GPU, processore, memoria, archiviazione, ventole e perdite dell'alimentatore. È un'ipotesi per il calcolo, non una misura.

[La previsione della U.S. Energy Information Administration](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) usava 18,2 centesimi per kilowattora come prezzo medio residenziale dell'elettricità nel 2026. La tua tariffa cambia il risultato.

Usa questa formula per l'output generato:

```text
local cost per 1M output tokens =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

A 400 W e 0,182 $ per kilowattora, il sistema costa 0,0728 $ per ora attiva.

| Velocità output | Tempo per 1M token | Costo energia per 1M token |
|---:|---:|---:|
| **20 token al secondo** | 13 ore 53 minuti | **1,01 $** |
| **50 token al secondo** | 5 ore 33 minuti | **0,40 $** |
| **94 token al secondo** | 2 ore 57 minuti | **0,22 $** |

A 50 token output al secondo, la potenza locale costa meno del prezzo output di Haiku 5.5, pari a 0,50 $. A 20 token output al secondo costa di più. La soglia di velocità output con queste ipotesi è circa 40 token al secondo.

Il calcolo input usa la stessa formula. A 2.650 token input al secondo, un milione di token input richiede circa 6 minuti e 17 secondi e costa circa 0,008 $ di energia. A 1.000 token input al secondo, lo stesso lavoro costa circa 0,020 $.

La trascrizione fornita riporta 94 token output al secondo e 2.650 token input al secondo per l'esempio RTX 5070. I calcoli sopra concordano con questi dati nell'ipotesi di 400 W. La trascrizione non fornisce un record di laboratorio indipendente, l'hash del file del modello, la build del runtime, il prompt o una lettura del wattmetro. Considera queste velocità un risultato di riferimento, non una garanzia d'acquisto.

## L'hardware cambia il punto di pareggio

Il risparmio energetico da solo non ripaga l'hardware. Confronta l'acquisto completo con la differenza tra il costo output ospitato e il costo variabile locale.

A 50 token output al secondo:

```text
$0.50 hosted output price - $0.40 local power = $0.10 saved per 1M tokens
$549 GPU price / $0.10 = about 5.5 billion output tokens
```

A 94 token output al secondo, il risparmio arrotondato sale a circa 0,28 $ per milione di token. Recuperare una GPU da 549 $ richiede quindi circa 2 miliardi di token output. Entrambi i dati escludono memoria di sistema, archiviazione, scheda madre, alimentatore, raffreddamento, manutenzione e valore di rivendita.

Il prezzo di lancio non è un preventivo universale. La pagina corrente NVIDIA mostrava il prezzo ufficiale senza disponibilità. Un annuncio da 819 $ richiede una verifica separata prima di inserirlo in un modello di pareggio. Usa la fattura reale e la potenza misurata alla presa.

**L'hardware già presente cambia la decisione.** Se la workstation ha già memoria sufficiente e una GPU adatta, il costo hardware è già sostenuto per il prossimo lavoro. Confronta potenza, tempo, qualità, privacy e manutenzione. Se devi comprare un sistema completo, confronta il sistema completo con l'uso ospitato.

Per i dettagli sulla compatibilità dei modelli, leggi la [guida ai modelli IA locali e al contesto GPU](/articles/local-ai-model-gpu-context-guide/) e la [guida al dimensionamento di 16 GB di VRAM](/articles/is-16gb-vram-enough-local-llm/). Per una configurazione riportata di agente di coding locale, leggi la [guida Strata e OpenCode](/articles/strata-opencode-local-coding-agent-16gb/).

## Cosa offre la privacy locale

- **Un percorso dati più breve:** il prompt non deve raggiungere un fornitore del modello quando l'inferenza resta locale.
- **Funzionamento offline:** un modello scaricato e un runtime locale non richiedono una connessione attiva al fornitore per generare testo.
- **Controllo delle versioni:** scegli il file del modello e la versione del runtime invece di ricevere un cambio automatico dal fornitore.
- **Controllo dell'uso:** l'inferenza locale evita un contatore cloud per richiesta dopo aver considerato possesso dell'hardware ed energia.
- **Controllo della policy di rete:** firewall e controlli dell'host definiscono chi raggiunge l'endpoint del modello.

Questi vantaggi contano soprattutto per codice sorgente, dati dei clienti, progetti non pubblicati, note private e lavoro svolto in un ambiente disconnesso. L'inferenza locale richiede comunque cifratura del disco, aggiornamenti dell'host, separazione degli account e strumenti limitati.

## Cosa non offre la privacy locale

- **Una garanzia di qualità:** i modelli più piccoli o quantizzati richiedono test sui tuoi criteri reali di accettazione.
- **Una garanzia della supply chain:** file dei modelli, runtime, plugin e immagini container richiedono fonti affidabili e controlli di integrità.
- **Un host pulito:** malware, estensioni del browser, backup, reporter dei crash e amministrazione remota vedono ancora i dati dell'host.
- **Un endpoint di rete sicuro:** un server legato a ogni interfaccia crea un nuovo servizio da difendere.
- **Un sistema gratuito:** elettricità, archiviazione, raffreddamento, usura dell'hardware e manutenzione hanno ancora un costo.

La [guida all'agente di coding locale Strata](/articles/strata-opencode-local-coding-agent-16gb/) mostra perché memoria di sistema, contesto, accesso agli strumenti e impostazioni del runtime fanno parte della valutazione. La memoria GPU da sola non definisce il confine della privacy o delle prestazioni.

## Scegli il confine corretto

| Situazione | Prima scelta migliore | Motivo |
|---|---|---|
| **Documenti sensibili e PC compatibile esistente** | Inferenza locale | Mantieni i prompt in un host controllato ed evita nuova spesa hardware |
| **Scrittura generica occasionale** | API o servizio chat ospitato | Paga il carico ridotto ed evita la manutenzione |
| **Modello frontier o strumento cloud specializzato** | Servizio ospitato | Il modello o strumento richiesto non è disponibile sull'host locale |
| **Grande volume ricorrente con modello locale verificato** | Locale o ibrido | Confronta potenza, qualità, tempo di supporto e prezzi del fornitore |
| **Carichi misti** | Routing ibrido | Mantieni locali le attività sensibili e invia le attività generiche approvate a un modello ospitato |

**Il routing ibrido richiede una regola di classificazione esplicita.** Classifica i dati come solo locali, approvati per l'elaborazione ospitata o vietati fino alla revisione. Non affidarti al nome del modello o all'icona dell'applicazione per applicare la regola.

## Verifica prima di fidarti

1. **Nomina il percorso del modello.** Registra identificatore del modello, runtime, versione e fonte di download.
2. **Controlla l'indirizzo di bind.** Conferma che il server ascolti sul loopback, salvo una necessità documentata per un percorso più ampio.
3. **Elenca ogni strumento.** Esamina accesso a file, shell, browser, rete e plugin.
4. **Controlla la persistenza.** Trova log dei prompt, output degli strumenti, report di crash, backup e directory condivise dei modelli.
5. **Testa il comportamento di rete.** Osserva le connessioni durante un test sensibile con un prompt rappresentativo.
6. **Misura il sistema.** Registra potenza alla presa, velocità output, velocità input, lunghezza del contesto e retry.
7. **Testa il lavoro accettato.** Confronta attività completate e sforzo di revisione, non solo token al secondo.

La [guida IA locale contro ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/) tratta i compromessi delle capacità dei modelli. Usa questa checklist privacy insieme al test di qualità.

## Riferimenti

- [Video, L'IA locale conviene? Abbiamo confrontato i costi con Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [Annuncio di lancio NVIDIA Blackwell GeForce RTX 50 Series](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [Specifiche della famiglia NVIDIA GeForce RTX 5070](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [Pagina prodotto NVIDIA GeForce RTX 5070](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, Short-Term Energy Outlook di ottobre 2026](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Prezzi della piattaforma Anthropic Claude](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, comprendere e contare i token](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Privacy policy di Ollama](https://ollama.com/privacy)
- [Documentazione server llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
