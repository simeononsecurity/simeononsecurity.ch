---
title: "Un'unica fonte, molti strumenti: un framework di collaborazione AI per team misti"
date: 2026-10-01
lastmod: 2026-11-23
toc: true
draft: false
description: "Crea un sistema condiviso di collaborazione con l'AI, definendo la proprietà delle fonti, il versionamento del contesto, la revisione delle modifiche persistenti e la scelta tra mappa di progetto e RAG."
genre: ["Intelligenza artificiale", "Gestione della conoscenza", "Ingegneria del software", "Collaborazione di gruppo"]
tags: ["framework di collaborazione AI", "team misti", "fonte autorevole", "agenti AI", "AGENTS.md", "CLAUDE.md", "regole Cline", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "generazione aumentata dal recupero", "RAG", "Model Context Protocol", "mappa di progetto", "manifesto del contesto", "gestione della conoscenza", "deriva documentale", "approvazione umana", "registro delle decisioni", "passaggio tra agenti", "versionamento delle policy", "Git worktrees", "controlli per pull request"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustrazione di professionisti che collaborano su attività di sicurezza informatica"
coverCaption: ""
---

**Due persone pongono a due strumenti AI la stessa domanda:**** per quanto tempo il servizio deve conservare un'esportazione? In questo esempio, l'agente IDE dello sviluppatore risponde sette giorni basandosi su un README.** L'assistente chat del responsabile operativo risponde trenta giorni basandosi su una pagina wiki. Entrambe le risposte sembrano sicure. Ogni strumento ha letto una copia diversa della verità.

**Il problema è la titolarità****, non la qualità del prompt.** Il requisito nella wiki è cambiato la settimana scorsa, ma nessuno ha aggiornato il README. Lo sviluppatore chiede all'agente di correggere il job di conservazione. L'agente segue il documento più vecchio e prepara una patch ordinata che ripristina il comportamento sbagliato. I revisori esaminano il codice senza vedere la versione del requisito alla base della risposta.

**Assegna a ogni fatto una sola sede.**** Fai leggere quella fonte a ogni strumento e fai passare ogni modifica duratura da una persona.** Repository, wiki e tracker mantengono scopi diversi. Definisci la loro autorità, i responsabili e una procedura condivisa per trasferire informazioni tra i sistemi.

**Questa guida propone un modello da applicare questa settimana****, con o senza retrieval-augmented generation.** Inizia con una mappa di progetto, istruzioni versionate, registri delle prove e proposte revisionate. Aggiungi infrastrutture di ricerca soltanto quando il problema di recupero lo richiede.

**Il primo risultato è un registro delle fonti**, non un connettore. Per ogni tipo di fatto, elenca la sede autorevole, il responsabile, la revisione corrente e la persona che approva le modifiche.

## Punti chiave

- **Assegna l'autorità per tipo di informazione**, invece di costringere tutto in un'unica applicazione.
- **Tratta memoria e indici di recupero come cache**, mai come fonti indipendenti di policy.
- **Allega le versioni delle fonti alle proposte**, così i revisori vedono quali fatti hanno guidato una modifica.
- **Imponi l'approvazione fuori dai prompt**, tramite controlli di accesso e passaggi di revisione obbligatori.
- **Condividi la procedura tra strumenti**, adattandone l'esecuzione a ogni interfaccia.

## Prima di iniziare

**Prerequisiti:**** scegli un progetto pilota con repository, wiki o sistema documentale, tracker e responsabili disponibili a rivedere le modifiche.** Se il team non usa una wiki, sostituiscila con un archivio documentale versionato. Il modello di titolarità resta invariato.

**Tempo stimato:**** riserva da due a quattro ore per la mappa iniziale e i modelli, poi una settimana di prova.** **Difficoltà:** moderata. La parte difficile è concordare l'autorità, non installare un altro strumento AI.

**Ambito:**** questo è un modello operativo proposto per il team.** Le regole di approvazione e le convenzioni di denominazione sono raccomandazioni, non comportamenti predefiniti garantiti da Claude Code, Codex, Cline, Cowork, Copilot o ChatGPT. L'indice automatico sopra rimanda a ogni fase di implementazione.

## Strumenti misti, contesto separato

**Sviluppatori e non sviluppatori condividono un progetto****, ma usano interfacce diverse.** Uno sviluppatore usa un agente IDE o terminale. Un responsabile prodotto usa un progetto chat. Le operations usano wiki e tracker. Scegli le interfacce in base al compito, non all'accesso ai fatti autorevoli.

**Il contesto è il materiale disponibile per la risposta corrente.**** Per ogni sessione controlla file del repository, documenti caricati, cronologia chat, memoria salvata, risultati dei connettori ed estratti recuperati.** Due sessioni con prove diverse non devono per forza concordare, anche se la domanda è identica.

| Problema | Cosa osservi |
|---|---|
| **Deriva documentale** | Un README ripete un requisito obsoleto |
| **Promozione del riepilogo** | Un riepilogo di sessione diventa una prova senza la fonte originale |
| **Modifiche sovrapposte** | Due agenti sostituiscono la stessa pagina da versioni di base diverse |
| **Decisioni perse** | Un accordo di riunione non raggiunge il registro decisionale |
| **Provenienza mancante** | Una risposta plausibile non cita la versione della pagina o il commit |

**L'esempio della conservazione mostra la distinzione.**** La wiki descrive il comportamento approvato.** Il codice descrive quello implementato. Nessuno dei due dovrebbe riscrivere l'altro in silenzio. Registra la discrepanza e chiedi al responsabile se va modificata l'implementazione o il requisito.

> **Punto chiave:** definire l'autorità viene prima di scegliere uno strumento AI. Inizia con questi termini condivisi.

### Riquadro: cinque termini condivisi

| Termine | Significato nel framework |
|---|---|
| **Fonte** | Il record autorevole designato per un tipo di informazione |
| **Cache** | Una copia derivata usata per velocità o comodità |
| **Proposta** | Una modifica suggerita in attesa dell'approvazione del responsabile |
| **Mappa di progetto** | Un indice di sedi, identificatori e responsabili delle fonti |
| **Manifesto** | Il record delle prove esatte usate per una risposta o proposta |

## Assegna a ogni fatto una sede

**Un'unica fonte significa un'autorità per ogni fatto****, non un unico database per tutta l'organizzazione.** Definisci questa ripartizione nel pilota. Sostituisci i ruoli di esempio con i responsabili reali del team.

| Tipo di informazione | Sistema di riferimento | Responsabile | Chi scrive | Come leggono gli agenti |
|---|---|---|---|---|
| **Codice, test, configurazione, schemi** | Repository | Manutentore tecnico | Collaboratori tramite PR revisionate | File a un commit registrato |
| **Documentazione pubblicata e ADR** | Repository | Responsabile tecnico | Collaboratori tramite la stessa PR | File versionati |
| **Requisiti** | Wiki | Responsabile prodotto | Responsabile o editore autorizzato | ID pagina e revisione |
| **Runbook** | Wiki | Responsabile operations | Editore autorizzato | ID pagina e revisione |
| **Policy** | Wiki | Responsabile policy | Editore autorizzato dopo revisione | Pagina canonica più adapter locale |
| **Decisioni tra team** | Registro decisioni wiki | Responsabile decisionale nominato | Responsabile dopo l'approvazione | ID decisione e stato |
| **Task e rilievi** | Tracker | Responsabile del task | Persone o raccolta proposte autorizzata | Chiave issue e revisione |
| **Chat, riepiloghi, embedding** | Solo cache | Responsabile sessione o indice | Strumenti e partecipanti | Solo riferimento, poi verifica della fonte |

**Un record di decisione architetturale (ADR)** appartiene al codice quando governa l'architettura del repository. Una decisione tra team appartiene al registro condiviso. Collega i due record quando una decisione riguarda entrambi gli ambiti. Non mantenere lo stato di approvazione in due copie indipendenti.

**Le copie locali delle policy restano subordinate** alla pagina canonica. I test e gli schemi del repository sono invece fonti per il loro ambito. La posizione non determina l'autorità. La determina la mappa.

**Una cache non prevale mai su una fonte.** Se un riepilogo dice sette giorni e il requisito approvato dice trenta, usa il requisito per il comportamento atteso. Conserva il riepilogo in conflitto come prova di deriva, non come regola concorrente. Definisci ora il percorso di scrittura.

## Cache verso il basso, proposta verso l'alto

**Gli agenti acquisiscono prove nel contesto della sessione** e poi preparano proposte. Non approvano autonomamente fatti duraturi. Modificare un branch di lavoro o inviare una bozza è diverso dal pubblicare policy, unire codice o segnare una decisione come accettata.

```text
Fonte -> lettura con verifica delle autorizzazioni -> contesto della sessione
Contesto della sessione -> proposta + versione di base -> revisione del responsabile
Approvazione del responsabile -> pubblicazione controllata -> registro delle modifiche
Versione di base modificata -> riconciliare la proposta -> nuova revisione
```

**Registra la versione di base** prima di chiedere una revisione. Il revisore ha bisogno del valore precedente e di quello proposto, del motivo, delle prove e dei sistemi interessati. L'approvazione deve riferirsi a una revisione specifica della proposta, non a una chat in evoluzione.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Conserva le esportazioni per trenta giorni invece di sette."
evidence:
  - "decisione:DEC-12 approvata"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**Gli identificatori sopra sono esempi.** Per ogni modifica logica approvata, registra una riga nel log con ID proposta, record interessati, versioni precedente e risultante, approvatore, data e riferimento al merge o alla pubblicazione. Collega a quella riga gli eventi di audit dei sistemi senza sostituirne la cronologia nativa.

**La decisione spetta alle persone.** Un editore autorizzato o un'automazione vincolata applica la revisione approvata. Limita i permessi di scrittura. Le istruzioni da sole non separano la stesura dalla pubblicazione. La stessa distinzione vale per il recupero.

## Contesto condiviso senza RAG

**Una mappa di progetto è il primo indice di recupero.** Mantieni una pagina per progetto con ID delle fonti, percorsi del repository, chiavi del tracker, ambiti di autorità e responsabili. Leggi prima la mappa e poi recupera il record pertinente tramite ID. Cerca quando l'ID non è noto.

### Riquadro: esempio di mappa di progetto

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**I connettori diretti riducono la copia manuale.** Model Context Protocol (MCP) è un protocollo d'integrazione che espone strumenti e contesto alle applicazioni AI. Usa connettori approvati per wiki, tracker e repository quando disponibili. Un recupero mirato riduce risultati irrilevanti ma non sostituisce autorizzazione o verifica dell'attualità. Per scegliere i permessi del connettore, segui le indicazioni sulla sicurezza MCP nelle referenze.

**Il recupero esatto richiede poca configurazione.** Fornisce prove citabili senza database vettoriale. I limiti sono chiari: qualcuno deve mantenere la mappa, le domande ampie richiedono altre ricerche e le pagine grandi consumano spazio di sessione. Recupera la sezione pertinente insieme ai vincoli vicini, invece di incollare un intero manuale.

**Il lavoro offline usa snapshot espliciti.** Registra la revisione esportata e indica che le risposte si basano su uno snapshot. Non pubblicare modifiche finché una persona autorizzata o un connettore non controlla la fonte corrente. Poi rendi visibile la stessa policy in ogni interfaccia.

## Una policy, adapter diversi

**Mantieni una policy condivisa** e distribuisci brevi adapter specifici per gli strumenti. Metti la versione approvata della policy alla prima riga di ogni adapter o set di istruzioni copiato. Includi l'ID della fonte e uno snapshot locale revisionato per le sessioni senza connettore.

**Il caricamento varia da strumento a strumento.** Codex documenta la ricerca a livelli di `AGENTS.md`. Claude Code documenta `CLAUDE.md`, import e memoria di progetto. Cline documenta `.clinerules/` e i controlli delle regole. Consulta la documentazione ufficiale nelle referenze. Verifica quali istruzioni sono caricate nella versione installata invece di presumere che i nomi dei file si comportino allo stesso modo.

### Riquadro: esempio di intestazione AGENTS.md

```markdown
Versione della policy: v3 | Fonte: wiki:POL-01 | Stato: approvata

# Istruzioni del progetto

Leggi la mappa di progetto MAP-01 prima di iniziare un task.
Carica docs/policy-snapshot.md e registra la revisione della fonte.
Tratta memoria chat ed estratti di ricerca come cache.
Allega le revisioni delle fonti a ogni proposta fattuale.
Usa un branch di task e un worktree per ogni attività di sviluppo.
Non pubblicare policy, approvare decisioni o fare merge della tua PR.
Fermati in caso di conflitti tra fonti irrisolti o scritture sovrapposte.
Controlli richiesti: test, revisione documentazione, freschezza policy.
Responsabili: manutentore engineering, responsabile prodotto, responsabile policy.
```

**Le istruzioni di progetto nelle chat ricevono la stessa intestazione e procedura.** Un non sviluppatore riceve lo snapshot della policy e la mappa tramite upload o connettori approvati. Se l'interfaccia non ha accesso live, una persona fornisce l'esportazione versionata e registra il limite.

**Un'etichetta di versione è un'affermazione, non una prova di contenuto identico.** Genera adapter dallo snapshot approvato oppure confronta le parti di policy con un digest salvato. Revisiona separatamente le eccezioni specifiche degli adapter. Durante il pilota controlla regole disattivate, override annidati e istruzioni personali. Poi registra le prove usate da ogni task.

## Registra un manifesto del contesto

**Un manifesto del contesto spiega le prove di una risposta.** Registra ID e revisioni delle pagine, chiavi issue e relative revisioni o date di aggiornamento, oltre agli ID completi dei commit. Includi l'ora del recupero e le sezioni pertinenti. Segna i record non disponibili invece di sostituirli con riepiloghi ricordati.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook non recuperato. Nessuna modifica proposta al runbook."
```

**Il valore del commit è sintetico.** In un manifesto reale sostituiscilo con il commit verificato. Aggiungi l'ora durante la lettura effettiva. Un record creato prima dell'ispezione è una checklist, non una prova.

**Le citazioni supportano il controllo**, non la fiducia automatica. Collega ogni affermazione materiale al record e alla sezione di supporto. Se due fonti divergono, mantienile entrambe nel manifesto e segnala il conflitto irrisolto. Non scegliere il timestamp più recente senza controllare ambito e approvazione. Questa disciplina delle prove vale anche per il recupero semantico.

## Contesto condiviso con RAG

**La generazione aumentata dal recupero (RAG)** fornisce materiale recuperato al modello mentre produce una risposta. Un indice semantico trova passaggi pertinenti anche se la domanda usa parole diverse. La panoramica RAG di Microsoft descrive grounding, limiti del recupero e controlli di accesso. Consulta la fonte ufficiale nelle referenze.

**Usa RAG per esplorare raccolte ampie**, tra cui documentazione legacy, note di riunioni e trascrizioni. Etichetta classi di documenti e stati di approvazione. Una trascrizione indicizzata dalla registrazione originale documenta ciò che i partecipanti hanno detto, ma non è autorità sui requisiti approvati. Non trasformare conversazioni in policy tramite l'indicizzazione.

| Regola d'indice | Comportamento richiesto |
|---|---|
| **Ingerisci fonti, non cache** | Escludi riepiloghi generati e copie locali non tracciate |
| **Preserva la provenienza** | Memorizza ID fonte, revisione, sezione e stato del documento per ogni chunk |
| **Aggiorna dopo le modifiche** | Reindicizza le modifiche e invalida i chunk obsoleti |
| **Rispetta i cambi di accesso** | Aggiorna permessi e rimuovi contenuti revocati o cancellati |
| **Restituisci citazioni** | Mostra i riferimenti ai record accanto al testo recuperato |
| **Controlla il record live** | Recupera prove correnti prima di proporre un'azione rilevante |

**Un chunk recuperato funziona come puntatore in questo framework.** Il testo aiuta a trovare le prove. La fonte live conferma formulazione, approvazione, eccezioni e accesso correnti. Se il recupero live fallisce, etichetta lo snapshot e interrompi l'azione rilevante. È una regola di governance, non un'affermazione su ogni implementazione RAG.

**Embedding obsoleti e contesto mancante sono rischi distinti.** Un chunk vecchio perde una revisione. Anche un chunk attuale può fuorviare se un'eccezione si trova nella sezione successiva. Conserva i titoli e recupera i vincoli adiacenti prima di valutare un requisito.

**Le fughe di permessi richiedono un test dedicato.** Applica l'autorizzazione prima di restituire chunk al modello, non dopo aver generato la risposta. Esamina contenuti sensibili prima dell'indicizzazione o di chiamate esterne di embedding. Considera le copie nei log, nelle richieste al modello e nelle tracce di recupero. Un modello locale non rende locale un connettore remoto. Questi controlli indicano se RAG è adatto al pilota.

## Scegli mappa, RAG o entrambe

**Adatta il recupero alla domanda.** Un ID requisito noto favorisce l'accesso diretto. Una domanda aperta su materiale storico sparso favorisce la ricerca. Inizia dalla mappa, salvo che il problema di scoperta sia già misurato.

### Riquadro: RAG o no?

```text
I task indicano di solito un progetto, una pagina, un issue o un file?
  Sì -> Il recupero diretto è sufficiente per il pilota?
           Sì -> SOLO MAPPA
           No -> IBRIDO: mappa per ID noti, RAG per la scoperta
  No -> Le prove sono sparse in una raccolta ampia?
           No -> SOLO MAPPA, più ricerca nativa
           Sì -> Il lavoro è esplorativo e di sola lettura?
                    Sì -> SOLO RAG per la scoperta
                    No -> IBRIDO con controlli sulle fonti live

Ogni opzione mantiene responsabili, autorizzazione e provenienza.
La scoperta con RAG controlla comunque le fonti prima di un’azione duratura.
```

**RAG-only descrive l'interfaccia di recupero**, non il permesso di saltare la governance. Usala per una raccolta esplorativa limitata in cui resta disponibile il controllo diretto della fonte. È una scelta debole per modifiche su ID noti che richiedono verifiche precise delle versioni.

**Il modello ibrido separa scoperta e verifica.** La mappa gestisce ricerche note. RAG individua record sconosciuti. RAG risponde “dove”; la fonte risponde “cosa”. Per l'esempio della conservazione, recupera direttamente `REQ-17`. Per “quali decisioni precedenti sugli export spiegano questo limite?”, cerca nel registro e recupera ogni decisione pertinente. Ora applica il lato repository.

## Informazioni nel repository

**La conoscenza del repository cambia con l'implementazione.** Mantieni una struttura compatta, così agenti e revisori sanno dove cercare.

| File o directory | Responsabilità |
|---|---|
| **`CONTEXT.md`** | Termini di progetto e link a record autorevoli |
| **`docs/adr/`** | Decisioni architetturali accettate per il repository |
| **`docs/design/`** | Descrizioni approvate del comportamento del sistema |
| **`docs/plans/`** | Piani di implementazione proposti con stato esplicito |
| **`AGENTS.md`** | Gate di revisione, confini e ruoli dei responsabili |
| **`README.md`** | Configurazione e punti di ingresso, non requisiti duplicati |

**Applica la regola della stessa PR:** modifica insieme il codice e la documentazione del repository interessata. Se non serve un aggiornamento della knowledge base, richiedi un'eccezione scritta nella descrizione della PR o nel punto concordato per i trailer del commit.

```text
KB-Update: none (motivo: il refactoring interno conserva il comportamento documentato)
```

**La pipeline applica la dichiarazione.** Un controllo obbligatorio rifiuta modifiche di comportamento senza aggiornamenti documentali o eccezioni. Un responsabile umano della documentazione revisiona l'eccezione. Un controllo basato sui percorsi individua modifiche candidate, ma non dimostra completezza semantica. Applica controllo e revisione tramite branch protection o un equivalente controllo di merge.

**Un gate assente dalla pipeline non è un gate.** Citare “revisione documentazione” in un file di istruzioni fornisce solo una guida. Durante il pilota invia una PR intenzionalmente incompleta e verifica che il merge resti bloccato.

**Usa un task, un branch e un worktree.** La documentazione ufficiale Git descrive alberi di lavoro separati con stato di checkout proprio. Worktree distinti riducono le collisioni di modifica locali, ma non impediscono a due branch di modificare lo stesso file o a due agenti di aggiornare la stessa pagina wiki.

**Non fare mai commit direttamente sul branch predefinito**, sia esso `main`, `master` o altro. Segnala nel tracker i conflitti tra requisiti e codice. Allega i record in conflitto e lascia ai responsabili la decisione sul comportamento previsto prima di allineare uno dei lati. Applica controlli analoghi fuori da Git.

## Informazioni fuori dal repository

**La wiki ha bisogno di uno standard documentale.** Ogni pagina autorevole include scopo, stato, responsabile, revisione, data di revisione e ID delle fonti correlate. Inserisci le proposte nell'area bozze con un'etichetta chiara di non autorevolezza. Non mescolare testo proposto in una pagina di requisiti approvata.

**Gli aggiornamenti sicuri seguono una sequenza fissa:**

1. **Rileggi** la pagina attuale e i vincoli circostanti.
2. **Confronta** la sua versione con la base della proposta.
3. **Riconcilia** le modifiche intervenute e chiedi nuova approvazione per un testo cambiato.
4. **Scrivi** la revisione approvata con una condizione sulla versione attesa.
5. **Verifica** la pagina salvata e aggiungi il riferimento al log delle modifiche.

**Rileggere non elimina le gare.** Se disponibile, usa il meccanismo di aggiornamento condizionale del sistema. In sua assenza, un unico responsabile serializza la pubblicazione e ne verifica il risultato. Fermati se un altro autore cambia la base durante la revisione.

**Il divieto di eliminazione riguarda i flussi degli agenti.** Gli agenti propongono archiviazione o rimozione. Le persone autorizzate applicano le procedure di conservazione e cancellazione. Non interpretare la regola come autorizzazione a conservare per sempre informazioni sensibili.

**I rilievi nel tracker contengono prove**, non solo conclusioni. Registra osservazione, comando o metodo d'ispezione esatto, commit esaminato, comportamento atteso e reale e criteri di accettazione. Rimuovi segreti e output sensibili prima di allegare prove. Segna i comandi proposti come non eseguiti finché qualcuno non li avvia.

```text
Rilievo: l’implementazione della conservazione diverge dal requisito approvato
Prove: REQ-17 v8 e config/retention.yaml esaminato
Comando di ispezione: git show HEAD:config/retention.yaml
Commit: ID completo del commit esaminato registrato nel manifesto
Accettazione: la durata approvata coincide con codice, test e runbook
Stato: in attesa della revisione dei responsabili prodotto e ingegneria
```

**L'esempio è un modello di rilievo**, non un risultato misurato. Compilalo sulla base di un'ispezione reale. Collega l'aggiornamento wiki e le prove del tracker tramite l'ID proposta.

**Il registro decisionale separa regole e ragionamenti.** Registra domanda, opzioni, raccomandazione, compromessi, responsabile, stato di approvazione e riferimento alla regola risultante. Gli agenti propongono. Le persone decidono. Le regole approvate passano a policy e procedure; la motivazione resta nel registro.

**Raccogli fatti duraturi da riunioni e chat.** Invia una proposta con le prove di origine e ottieni approvazione. Fino alla pubblicazione, etichetta l'accordo come provvisorio. Poi collega il comportamento approvato tra repository e wiki.

## Collega i due sistemi

**La sincronizzazione post-merge trasferisce all'esterno le modifiche di implementazione.** Crea un task wiki collegato al commit integrato, al requisito approvato e al runbook interessato. Un agente prepara la bozza. Il responsabile wiki controlla la pagina attuale e approva la pubblicazione. Lascia aperto il task di sincronizzazione finché non verifichi la revisione salvata.

**La freschezza della policy è un audit separato.** Confronta ogni adapter del repository e copia di istruzioni nelle chat con la versione canonica approvata. La policy `v3` è in `POL-01`. Ogni `AGENTS.md` indica `v3` alla prima riga. L'audit segnala `v2`, etichette mancanti e differenze di contenuto anche quando le etichette coincidono.

| Controllo | Prova di completamento |
|---|---|
| **Freschezza della policy** | Versione canonica e confronto del digest dell'adapter |
| **Riconciliazione requisiti** | Revisione requisito confrontata con codice e test |
| **Sync post-merge** | Commit integrato collegato alla revisione wiki pubblicata |
| **Risoluzione conflitti** | Decisione approvata collegata a entrambi i record interessati |

**Riconcilia a calendario o al momento della PR.** Un audit settimanale è adatto al pilota. Una PR che cambia comportamento richiede un controllo del requisito prima del merge. Scegli la frequenza in base al costo della deriva e registra l'ultimo controllo riuscito.

**La modifica a trenta giorni ha più punti di controllo:** il prodotto approva il requisito, l'ingegneria aggiorna configurazione e test, i revisori integrano la PR e operations pubblica l'aggiornamento del runbook. Una riga del log collega i record risultanti. Una sincronizzazione wiki fallita resta visibile, invece di scomparire dietro un merge riuscito. Handoff condivisi mantengono la sequenza tra strumenti.

## Una procedura, ogni strumento

**Raggruppa i passaggi ripetuti in skill o prompt** con un ID procedura versionato. Condividi il contratto, non presumere un formato universale di file. Ogni adapter usa il meccanismo di caricamento o invocazione supportato.

| Procedura | Output richiesto |
|---|---|
| **Avvio task** | Responsabile, ambito, versione policy, manifesto fonti, prenotazione scrittura |
| **Lint documentazione** | Metadati mancanti, autorità duplicate, riferimenti a fonti non validi |
| **Verifica conoscenza** | Lacune tra requisito e codice con revisioni di supporto |
| **Handoff** | Prove correnti, proposte, controlli completati, domande irrisolte |

**I non sviluppatori lavorano senza Git.** Recuperano fonti consentite nei progetti chat, completano lo stesso modello di proposta e lo inviano al responsabile tramite pagina bozza o task tracker. Non serve un checkout per chiedere una correzione del requisito.

**Gli sviluppatori usano file del repository e gate PR.** Collegano la proposta approvata nella PR, registrano i commit esaminati ed eseguono i controlli richiesti. Entrambi i gruppi passano la stessa struttura di prove.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "Attached source IDs, revisions, and inspected commit"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["RUN-04 publication assigned to operations-owner"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**Un handoff resta una cache.** La persona successiva rilegge le fonti prima di agire e registra le revisioni nuove. Non considerare “completato” una prova senza controllare l'approvazione o il test collegato. Applica le protezioni seguenti prima di ogni scrittura.

## Protezioni prima di ogni scrittura

**Esamina i dati prima che lascino il sistema di origine.** Controlla classificazione, permessi dei connettori, destinazioni approvate, trattamento del provider del modello e logging. Invia solo il contenuto minimo pertinente. Non inserire record riservati in progetti chat o servizi di embedding non autorizzati.

**Il testo recuperato è una prova, non un canale di istruzioni.** Una pagina wiki o una risposta di uno strumento che chiede a un agente di ignorare la policy non ne cambia l'autorità. Esamina separatamente le istruzioni provenienti dai contenuti e la policy operativa approvata. Limita i connettori alla lettura durante il recupero e separa credenziali di pubblicazione e accesso della sessione.

**Assegna un solo responsabile attivo a ogni pagina o file.** Registra nel tracker prenotazione, ambito e scadenza. Rileggi prima di scrivere e usa controlli di versione. Worktree separati aiutano l'isolamento locale; prenotazioni e scritture condizionali proteggono i record condivisi.

| Motivo per fermarsi e chiedere | Risposta richiesta |
|---|---|
| **Fonti in conflitto senza responsabile** | Fermati e chiedi l'assegnazione dell'autorità |
| **Un altro task prenota la destinazione** | Concorda la proprietà prima di modificare |
| **La versione base è cambiata** | Riconcilia e chiedi una nuova approvazione |
| **Un'affermazione importante non ha prove** | Segnala che non è verificata e chiedi una fonte |
| **Gestione dati poco chiara** | Mantieni il contenuto nel sistema di origine |
| **Accesso live alla fonte non disponibile** | Registra i limiti dello snapshot e sospendi l'azione duratura |

**I prompt non sono controlli di sicurezza.** Testa diniego dei permessi, branch protetti, rifiuto di basi obsolete e proprietà di scrittura fuori dal modello. Una dimostrazione conforme non basta se l'account conserva diritti di pubblicazione illimitati. Usa questi test per decidere se il pilota è pronto.

## Pilota prima della promozione

**Avvia il framework come bozza.** Pilota un progetto con sviluppatore, non sviluppatore e responsabili delle fonti nominati. Poni la stessa domanda con ID noto a due strumenti, poi simula un conflitto tra fonti. Valuta manifesti e proposte, non la fluidità della prosa.

**Ragionamento atteso:** entrambi identificano il requisito approvato corrente e descrivono separatamente l'implementazione esaminata. Se non concordano, confrontano prima le voci del manifesto. È un esercizio proposto, non un benchmark osservato.

| Metrica | Definizione |
|---|---|
| **Tasso di citazione** | Affermazioni importanti supportate da fonti divise per le affermazioni fattuali importanti nel campione |
| **Rilievi settimanali di deriva** | Disallineamenti confermati di autorità o versione, raggruppati per tipo di fonte |
| **Tempo delle proposte** | Mediana dalla proposta pronta alla revisione alla decisione registrata |
| **Rielaborazione da contesto obsoleto** | Task riaperti per prove obsolete o non verificate |

**Misura una baseline prima di fissare obiettivi.** Più rilievi di deriva nella prima settimana possono indicare rilevamento migliore, non documentazione peggiore. Registra ricorrenza e tempi di risoluzione oltre al conteggio grezzo. Esamina prove sensibili senza copiarle negli export analytics.

**Prepara un repository di esempio durante il rollout.** Includi mappa sintetica, adapter policy, manifesti, modelli di proposta, eccezioni documentali e controlli eseguibili. Usa record fittizi di wiki e tracker, senza credenziali di produzione. Mostra pubblicazione negata, rifiuto di una base cambiata, deriva di versione della policy e handoff riuscito.

**Un repository di modelli è un risultato del rollout**, non un asset fornito con l'articolo. Promuovi il modello operativo dopo che direzione e responsabili delle fonti hanno revisionato i risultati pilota. Registra eccezioni e guasti irrisolti. Prima della promozione correggi i problemi prevedibili qui sotto.

## Risolvi i problemi del contesto condiviso

| Sintomo | Prima correzione |
|---|---|
| **Due strumenti danno risposte diverse** | Confronta ID fonti, revisioni, ambito e stato approvazione |
| **Istruzioni sembrano attuali ma il comportamento differisce** | Controlla adapter caricati, interruttori delle regole e override locali |
| **RAG restituisce requisiti vecchi** | Controlla il refresh dell'indice e recupera la pagina live |
| **Una modifica wiki cancella un'altra** | Richiedi scritture condizionali o pubblicazione serializzata |
| **I controlli documentali passano con testo obsoleto** | Aggiungi revisione del responsabile e riconciliazione requisiti |
| **Le decisioni restano nelle chat** | Assegna raccolta proposte e proprietà del registro |

**Correggi il percorso delle prove prima di riscrivere il prompt.** Poi ripeti il caso pilota fallito e registra il risultato. Usa la checklist per rendere ripetibile ogni settimana il processo corretto.

## Dieci passi questa settimana

1. **Scegli un progetto pilota** e le persone e gli strumenti partecipanti.
2. **Assegna una sede e un responsabile** a ogni tipo di informazione.
3. **Pubblica una mappa di progetto** con ID fonti e ambiti di autorità.
4. **Prepara una policy condivisa** e chiedi la revisione del responsabile.
5. **Versiona ogni adapter di istruzioni** alla prima riga e verifica che venga caricato.
6. **Richiedi un manifesto del contesto** per risposte fattuali e proposte importanti.
7. **Crea un canale per le proposte** con versioni base e approvatori nominati.
8. **Applica controlli di scrittura e la regola documentale della stessa PR.**
9. **Testa deriva, conflitto e handoff** con record sintetici.
10. **Esamina le metriche pilota** e approva la fase di rollout successiva.

**Assegna a ogni fatto una sola sede, fai leggere quella fonte a ogni strumento e instrada ogni modifica duratura attraverso una persona.**

## Riferimenti e passi successivi

**La documentazione ufficiale supporta i componenti tecnici**, non le regole organizzative di questo framework. Verifica il comportamento degli strumenti installati e i permessi dei connettori durante il pilota.

- **Istruzioni Codex:** [Istruzioni personalizzate con AGENTS.md](https://developers.openai.com/codex/guides/agents-md), sulla scoperta e verifica delle istruzioni.
- **Istruzioni Claude Code:** [Come Claude ricorda il tuo progetto](https://code.claude.com/docs/en/memory), su istruzioni di progetto e memoria.
- **Istruzioni Cline:** [Regole](https://docs.cline.bot/customization/cline-rules), su regole dell'area di lavoro e controlli di attivazione.
- **Progettazione del recupero:** [RAG in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), su grounding, limiti del recupero e sicurezza.
- **Sicurezza dei connettori:** [Buone pratiche di sicurezza MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), su autorizzazione e rischi dei connettori.
- **Isolamento dei worktree:** [Documentazione Git worktree](https://git-scm.com/docs/git-worktree), sugli alberi di lavoro separati e lo stato condiviso del repository.

**Per pianificare inferenza locale**, leggi la [Guida al contesto GPU per AI locale](/articles/local-ai-model-gpu-context-guide/). Capacità hardware e governance delle fonti condivise risolvono problemi diversi. Una finestra di contesto più ampia non risolve autorità in conflitto.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Leggi la guida al contesto AI locale
{{< /centerbutton >}}
