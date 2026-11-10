---
title: "Claude Cowork e Claude Code con modelli locali: guida alla configurazione 2026"
date: 2026-09-22
lastmod: 2026-11-09
toc: true
draft: false
description: "Configura Ollama con Claude Desktop e Claude Code tramite un'API compatibile con Anthropic. Scopri i modelli e le funzioni cloud disponibili nel 2026."
genre: ["IA locale", "Strumenti di programmazione IA", "IA self-hosted", "Strumenti per sviluppatori", "Privacy", "Modelli open source", "Automazione", "Hardware IA"]
tags: ["claude cowork", "claude code", "modelli locali claude desktop", "ollama claude code", "anthropic base url", "anthropic_auth_token", "modello locale claude code", "usare claude offline", "agente di programmazione IA locale", "ollama launch claude", "claude desktop ollama", "programmazione llm locale", "programmazione IA privata", "programmazione IA offline", "agente IA locale", "qwen3.8", "modello cloud glm", "modelli con uso degli strumenti", "configurare claude code", "claude code gratis", "claude senza chiave API", "finestra di contesto modello locale", "llama.cpp", "ollama cloud", "privacy programmazione IA", "IA senza connessione", "strumenti IA devops"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "Postazione moderna con un computer che mostra un'interfaccia di programmazione, un tablet e altoparlanti intelligenti su uno sfondo blu scuro con accenti luminosi colorati."
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Gli strumenti agentici di Claude ora funzionano con modelli sul tuo hardware, senza chiave API, abbonamento o dati che lasciano il computer.** Ollama espone un'API compatibile con Anthropic, a cui Claude Code e Claude Desktop si collegano con pochi comandi.

*Molte guide tralasciano un dettaglio importante. Parlano di Claude Cowork e poi forniscono istruzioni per configurare lo strumento a riga di comando. Si tratta di due integrazioni diverse e solo una offre Cowork.*

Questa guida illustra separatamente i due percorsi, la variabile d'ambiente che molte guide popolari omettono, i modelli adatti a ciascuno nel settembre 2026 e le funzioni che restano disponibili solo nel cloud, qualunque configurazione tu scelga.

**Al termine della guida:** saprai quale integrazione ti serve, la collegherai tramite il percorso documentato di Ollama e verificherai l'endpoint con un test di chiamata a uno strumento. L'inferenza locale mantiene locali le richieste al modello solo se scegli un modello locale ed eviti le funzioni cloud.

## Risposta breve

**Ollama si collega a Claude in due modi distinti. Scegliere quello sbagliato è il motivo più comune per cui si completa una guida con un terminale funzionante ma senza Cowork.**

| Integrazione | Cosa offre | Percorso di configurazione | Piattaforma |
|---|---|---|---|
| **Claude Desktop** | Cowork, subagenti, ricerca sul web, modalità automatica | App Ollama, poi **Apps** e **Connect Claude** | **Solo macOS** |
| **Claude Code** | L'agente di programmazione CLI con chiamate agli strumenti e modifiche ai file | `ollama launch claude` oppure variabili d'ambiente | macOS, Linux, Windows |

**Se ti serve Cowork, usa l'integrazione con Claude Desktop.** Si configura tramite l'interfaccia grafica dell'app Ollama ed è disponibile solo su macOS. Il supporto per Windows è indicato come in arrivo.

**Se vuoi un agente nel terminale, usa Claude Code.** Basta un comando.

*Entrambi sono gratuiti. L'unico costo riguarda l'hardware e l'elettricità.*

## Due integrazioni diverse

La confusione parte dai nomi. **Claude Cowork è una funzione di Claude Desktop**, non un'applicazione separata e non un sinonimo di Claude Code.

La documentazione di Ollama elenca le due integrazioni su pagine e sezioni distinte. Claude Desktop si trova sotto **Assistants**, insieme a OpenClaw e Hermes. Claude Code è sotto **Coding**, insieme a OpenCode, Cline e Codex CLI.

La distinzione conta perché la configurazione cambia del tutto:

- **Claude Desktop** si configura dall'interfaccia di Ollama. Non devi modificare il profilo della shell.
- **Claude Code** si configura con variabili d'ambiente o un solo comando di avvio.

Una guida che ti fa esportare `ANTHROPIC_BASE_URL` e poi eseguire `claude` configura lo strumento a riga di comando. Se ti aspettavi l'esperienza desktop di Cowork, **la configurazione non si è guastata. Hai configurato un prodotto diverso.**

## Configurare Claude Desktop e Cowork

Questo percorso usa l'app Ollama invece del terminale.

### Prerequisiti

- **Ollama installato** su macOS. Il supporto per Windows è indicato come in arrivo.
- **Un modello già scaricato** se vuoi eseguire tutto in locale. Per un modello cloud, accedi a Ollama e abilita i modelli cloud. Alcuni richiedono un piano a pagamento.
- **Claude installato.** Se non è presente, Ollama offre di scaricarlo durante la configurazione.

### Passaggi

1. Apri Ollama e seleziona **Apps**.
2. Seleziona **Connect Claude**.
3. Segui le istruzioni. Se richiesto, installa Claude e riavvialo quando viene indicato.

La procedura termina qui. Per cambiare modello in seguito, apri **Ollama Settings**, vai ad **Apps**, scegli i modelli e seleziona **Restart Claude**.

### Funzioni disponibili

La documentazione di Ollama elenca quattro funzioni supportate da questa integrazione:

- **Cowork**, per completare attività difficili
- **Subagenti**, per suddividere attività più grandi tra agenti
- **Web search**, fornita per impostazione predefinita da Ollama
- **Auto mode**, che lascia all'agente la decisione su quando chiedere prima di apportare modifiche

*Cowork compare nell'elenco. È disponibile con questa integrazione, ma non con quella a riga di comando.*

### Disconnettere

La disconnessione ripristina la configurazione precedente di Claude, quindi la modifica non è distruttiva.

- Nell'interfaccia, apri **Apps**, disconnetti Claude e riavvialo quando richiesto.
- Da un terminale, esegui `ollama launch claude-desktop --restore`.
- **Chiudere Ollama mentre Claude è connesso ripristina anche la configurazione abituale di Claude.** Se vuoi mantenere la configurazione locale, lascia Ollama in esecuzione.

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Diagramma dell'app Ollama che si collega a Claude Desktop dal pannello Apps, con selezione dei modelli nelle impostazioni Ollama e percorso di ripristino della configurazione originale" >}}

## Configurare Claude Code dalla CLI

Quasi tutte le guide trattano questo percorso. È quello giusto per lavorare nel terminale.

### Metodo con un solo comando

```bash
ollama launch claude
```

Il comando imposta le variabili d'ambiente necessarie, indirizza Claude Code all'istanza locale di Ollama e avvia il programma. Scegli un modello dall'elenco e premi Invio. Per indicare prima il modello, aggiungi il flag:

```bash
ollama launch claude --model qwen3.5
```

*Il wrapper prepara l'ambiente. Leggi comunque la sezione seguente, perché sapere cosa imposta aiuta a risolvere eventuali problemi.*

### Impostare manualmente le variabili d'ambiente

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**La seconda riga è quella che molte guide popolari omettono.** Impostare `ANTHROPIC_API_KEY` a una stringa vuota evita che una chiave reale già presente nell'ambiente interferisca con la connessione locale. Se una guida pubblicata salta questa riga, chi ha già esportato una chiave incontra un errore difficile da capire.

Per evitare modifiche al profilo della shell, passa tutto direttamente nel comando:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

Due dettagli della documentazione ufficiale:

- **`ANTHROPIC_AUTH_TOKEN` contiene l'autenticazione bearer**, quindi in modalità locale il suo valore letterale è `ollama`.
- **I file delle impostazioni di Claude hanno la precedenza sulle variabili della shell.** Se la connessione si comporta in modo strano dopo aver esportato nuovi valori, controlla quei file e poi esegui `/status` in Claude Code per vedere quale endpoint viene usato.

### Collegarsi direttamente a Ollama Cloud

Per questa opzione non occorre installare Ollama. Imposta una chiave API e indirizza Claude Code all'endpoint ospitato da Ollama:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**C'è una limitazione.** La documentazione di Ollama segnala che la ricerca web ospitata e i controlli avanzati degli strumenti non sono supportati completamente con questo percorso. Chat di base, modifiche ai file e chiamate agli strumenti funzionano con modelli compatibili.

## Modelli per settembre 2026

La selezione dei modelli è cambiata molto nel 2026. Conviene ricontrollare i consigli scritti in primavera.

| Modello | Tipo | Contesto | Perché sceglierlo |
|---|---|---|---|
| **Qwen3.8 27B** | Locale, 18 GB | 256K | Miglior modello locale tuttofare attuale, con visione, chiamate agli strumenti e controllo del ragionamento |
| **Qwen3 Coder Next** | Locale, MoE 80B totali / 3B attivi | 256K | Creato per agenti di programmazione sempre attivi, con modalità rapida senza ragionamento |
| **Qwen3.6 35B A3B** | Locale, MoE 35B / 3B attivi | 262K | Apache 2.0 ed efficiente con poca memoria |
| **kimi-k2.7-code:cloud** | Cloud | Ampio | Modello cloud orientato alla programmazione senza requisiti hardware locali |
| **glm-5.3-flash** | Cloud | Ampio | Il modello indicato per primo dalla documentazione Ollama |

**Inizia con Qwen3.8 27B se hai memoria sufficiente.** Funziona localmente con una finestra di contesto 256K, visione nativa, chiamate agli strumenti e ragionamento attivabile per richiesta. Una scheda con almeno 24 GB lo rende adatto all'uso quotidiano.

**Scegli un modello cloud se non hai quella memoria.** Collegare Claude Code a un modello ospitato non costa nulla per una prova e elimina il problema dell'hardware, ma il tuo codice lascia il computer.

### Attenzione ai modelli ternari

Nella nostra **[guida all'IA locale](/articles/local-ai-2026-build-your-rig-now/)** spieghiamo che il modello ternario Bonsai 2 27B esegue un modello completo da 27B in **5,53 GiB**. Sembra una scelta allettante anche qui.

**Questo flusso di lavoro non lo supporta.** I kernel ternari fanno parte del fork di llama.cpp di Prism ML e Ollama standard non riesce a caricare quei file. Un comando come `ollama launch claude --model Ternary-Bonsai-2-27B` fallisce prima di avviare l'inferenza. Usa il pacchetto standard Qwen3.8 27B per Claude Code e tieni i pacchetti ternari per un runtime compatibile.

*In questo caso, praticità e massima efficienza portano a scelte diverse. Gli strumenti integrati richiedono un GGUF standard.*

## Imposta un contesto da 64K prima di incolpare il modello

La documentazione di Ollama dà un'indicazione diretta per lavorare sui repository: scegli un modello e **imposta una finestra di contesto di almeno 64K**, aumentandola per i repository più grandi.

Claude Code inserisce nella finestra di contesto i contenuti dei file, le differenze e l'output dei comandi. Con un valore predefinito ridotto, lo spazio finisce a metà attività. Il problema sembra di ragionamento, ma dipende dalle impostazioni.

| Contesto | Cosa gestisce |
|---|---|
| Meno di 32K | Modifiche a un file e domande rapide |
| **64K** | Lavoro su più file in un repository contenuto |
| 128K | Repository più grandi e output dei comandi esteso |
| 256K | L'intera finestra di Qwen3.8 27B |

*Se Claude Code perde il filo a metà di un'attività, controlla il contesto prima di cambiare modello.*

## Verificare le chiamate agli strumenti con un comando

Le chiamate agli strumenti distinguono un agente da un generatore di testo. Verifica che funzionino.

Dopo aver avviato Claude Code, chiedigli:

```text
Read the current directory and list all files
```

**Se elenca file reali, le chiamate agli strumenti funzionano.** Se dice che leggerebbe la directory e descrive cosa si aspetta di trovare, la funzione non è collegata. Stai usando un modello di chat con un prompt di programmazione, non un agente. Nessun prompt aggiuntivo risolve il problema.

Controlla le cause in quest'ordine:

1. **Passa a un modello con supporto verificato per gli strumenti.** Non tutti i modelli lo offrono e il numero di parametri non rivela questa differenza.
2. **Verifica che l'ambiente punti a Ollama.** Esegui `ollama --version` e controlla che `ANTHROPIC_BASE_URL` indichi l'endpoint locale.
3. **Esegui `/status` in Claude Code.** Un URL base o una credenziale nei file delle impostazioni di Claude prevale sulle variabili della shell appena esportate.

## Funzioni disponibili solo nel cloud

Conosci i limiti prima di ricostruire un flusso di lavoro attorno all'inferenza locale.

| Funzione | Modelli locali | Cloud |
|---|---|---|
| Chat e modifica dei file | Sì | Sì |
| Chiamate agli strumenti | Dipende dal modello | Sì |
| Subagenti | Sì | Sì |
| Ricerca web | Fornita tramite Ollama | Sì |
| **Cowork** | Tramite Claude Desktop | Sì |
| Modalità automatica | Tramite Claude Desktop | Sì |
| Prompt pianificati | Tramite `/loop` in Claude Code | Sì |

Tre limiti riguardano l'uso locale:

- **Il ragionamento su più file peggiora prima della velocità.** Un modello locale gestisce bene un file, in modo accettabile tre file e male un intero repository. Dimensiona il lavoro di conseguenza.
- **Alcuni modelli cloud richiedono un piano Ollama a pagamento.** Devi anche avere effettuato l'accesso e averli abilitati.
- **Il percorso diretto al cloud ha limiti funzionali.** Se salti l'installazione locale, la ricerca web ospitata e i controlli avanzati degli strumenti non sono completamente supportati.

*L'inferenza locale è adatta a lavori circoscritti e verificabili, meno a quelli ampi e ambigui. Organizza le attività tenendo presente questa distinzione.*

## Automatizzare

Due funzioni ampliano l'uso oltre le sessioni interattive.

### Esecuzioni headless per script e CI

Il flag `--yes` salta le selezioni interattive e scarica il modello se necessario. Richiede `--model`; tutto ciò che segue `--` passa direttamente a Claude Code:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Fai attenzione alle autorizzazioni.** Claude Code chiede conferma prima della maggior parte delle azioni. Un'esecuzione headless richiede quindi regole di autorizzazione configurate o un ambiente isolato. Non affidare una repository importante a un agente senza supervisione.

### Prompt pianificati con `/loop`

Durante una sessione di Claude Code, `/loop` esegue a intervalli un prompt o un comando slash:

```text
/loop 30m Check my open PRs and summarize their status
/loop 1h Research the latest AI news and summarize key developments
/loop 15m Check for new GitHub issues and triage by priority
```

*Funziona finché la sessione resta aperta. Non è un demone in background e termina con la sessione.*

## Risolvere i problemi

| Sintomo | Causa probabile | Soluzione |
|---|---|---|
| **Connessione rifiutata** | Ollama non è in esecuzione | Esegui `ollama serve` e verifica con `curl http://localhost:11434/api/tags` |
| **Descrive le azioni invece di eseguirle** | Il modello selezionato non supporta le chiamate agli strumenti | Passa a un modello con supporto verificato |
| **Viene usata una chiave API reale al posto dell'endpoint locale** | `ANTHROPIC_API_KEY` è ancora esportata | Impostala su una stringa vuota, come sopra |
| **Cowork non compare dopo la configurazione** | È stata configurata la CLI di Claude Code anziché Claude Desktop | Per Cowork, usa il percorso Ollama **Apps** |
| **La generazione è lenta** | Il contesto è troppo grande oppure il modello è denso mentre ne basta uno sparso | Riduci il contesto e poi prova un modello mixture-of-experts |
| **Le variabili esportate non hanno effetto** | I file delle impostazioni di Claude prevalgono sulle variabili della shell | Controlla i file delle impostazioni, poi esegui `/status` |
| **Le richieste in background falliscono** | Claude Code sceglie un modello piccolo per le attività interne | Imposta il modello piccolo sullo stesso modello locale |

*Due di questi sette problemi hanno la stessa causa. La maggior parte degli errori di configurazione deriva dall'endpoint sbagliato o da un modello senza supporto per gli strumenti.*

## Punti chiave

- **Claude Desktop e Claude Code sono integrazioni separate.** Cowork è disponibile in Claude Desktop e si configura su macOS dal pannello **Apps** di Ollama. Il percorso CLI non offre Cowork.
- **Un comando avvia il percorso CLI:** `ollama launch claude`. La configurazione manuale richiede tre variabili e **molte guide omettono `ANTHROPIC_API_KEY=""`**.
- **L'installazione locale non è indispensabile.** Indirizza Claude Code a `https://ollama.com` con una chiave API.
- **Imposta un contesto di almeno 64K prima di valutare un modello.** Una finestra ridotta può sembrare un problema di ragionamento.
- **Verifica le chiamate agli strumenti con una richiesta.** Se il modello descrive cosa farebbe, hai un generatore di testo, non un agente.
- **I pacchetti ternari Bonsai non funzionano in questo caso.** Richiedono il fork llama.cpp di Prism ML, che Ollama standard non può caricare.
- **Disconnettersi è sicuro.** Chiudere Ollama ripristina la configurazione precedente di Claude; dal terminale puoi anche usare `ollama launch claude-desktop --restore`.

## Passaggi successivi

1. **Installa Ollama e scarica un modello con supporto verificato per gli strumenti** prima di configurare Claude: **[Libreria dei modelli Ollama](https://ollama.com/library)**
2. **Consulta la pagina Ollama per Claude Code** per i flag e i modelli aggiornati: **[Integrazione Claude Code](https://docs.ollama.com/integrations/claude-code)**
3. **Se vuoi Cowork, consulta la pagina Claude Desktop:** **[Integrazione Claude Desktop](https://docs.ollama.com/integrations/claude-desktop)**
4. **Scegli l'hardware prima di acquistarlo**, usando le fasce di memoria della nostra guida all'inferenza locale: **[IA locale nel 2026: un modello 27B supera Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. **Controlla cosa gestisce l'hardware più piccolo** se vuoi un agente sempre attivo su un dispositivo a basso consumo: **[Quali modelli IA funzionano su Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Articoli correlati

| Articolo | Contenuto |
|---|---|
| **[IA locale nel 2026: un modello 27B supera Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Benchmark per l'inferenza locale, quantizzazione ternaria e scelta dell'hardware |
| **[Quali modelli IA funzionano su Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)** | Inferenza locale per un piccolo assistente sempre attivo |
| **[Creare un assistente IA per Meshtastic che tutela la privacy](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un modello locale per una radio off-grid, con la privacy come obiettivo principale |
| **[Le migliori estensioni VS Code per lo sviluppo IA](/articles/best-visual-studio-code-extensions-for-ai/)** | Strumenti per l'editor da affiancare a un agente di programmazione locale |

## Riferimenti

1. [Integrazione Claude Code - documentazione Ollama](https://docs.ollama.com/integrations/claude-code)
2. [Integrazione Claude Desktop - documentazione Ollama](https://docs.ollama.com/integrations/claude-desktop)
3. [Libreria dei modelli Ollama](https://ollama.com/library)
4. [Qwen3.8 - libreria dei modelli Ollama](https://ollama.com/library/qwen3.8)
5. [Claude Cowork con modelli locali - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Fork llama.cpp di Prism ML - kernel ternari](https://github.com/PrismML-Eng/llama.cpp)
