---
title: "Una fonte, molti strumenti: costruire un framework di collaborazione IA per team misti"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Costruisci un framework condiviso di collaborazione IA per sviluppatori e non sviluppatori. Assegna le fonti autorevoli, traccia le versioni del contesto, rivedi i cambiamenti duraturi e scegli una mappa di progetto, RAG o entrambe."
genre: ["Intelligenza artificiale", "Gestione della conoscenza", "Ingegneria del software", "Collaborazione di squadra"]
tags: ["framework collaborazione IA", "team misti", "fonte autorevole", "agenti IA", "AGENTS.md", "CLAUDE.md", "regole Cline", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "retrieval augmented generation", "RAG", "Model Context Protocol", "mappa di progetto", "manifesto del contesto", "gestione della conoscenza", "deriva documentale", "approvazione umana", "registro decisioni", "passaggio tra agenti", "versionamento policy", "Git worktrees", "controlli pull request"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustrazione di professionisti che collaborano su un progetto di cybersicurezza"
coverCaption: ""
---

**Due persone pongono la stessa domanda a due strumenti IA:** per quanto tempo il servizio deve conservare un export? Nell'esempio, l'agente IDE dello sviluppatore risponde sette giorni leggendo un README. L'assistente chat delle operations risponde trenta giorni leggendo una pagina wiki. Entrambe le risposte sembrano sicure. Ogni strumento ha letto una copia diversa della verità.

**Il problema è la proprietà**, non la qualità del prompt. Il requisito wiki è cambiato, ma il README non è stato aggiornato. L'agente segue il documento vecchio e produce una patch ordinata che ripristina il comportamento sbagliato. I revisori guardano il codice senza vedere la versione del requisito usata.

**Dai a ogni fatto una sola sede.** Fai leggere ogni strumento da quella sede e fai passare ogni modifica duratura da una persona. Repository, wiki e tracker mantengono scopi diversi. Servono autorità esplicita, responsabili nominati e una procedura condivisa per spostare le informazioni.

**Questa guida offre un modello applicabile questa settimana**, con o senza retrieval-augmented generation. Inizia con una mappa di progetto, istruzioni versionate, registri delle prove e proposte revisionate. Aggiungi la ricerca solo quando il problema di recupero lo richiede.

**Il primo deliverable è un registro delle fonti**, non un connettore. Elenca ogni tipo di fatto, sede autorevole, responsabile, revisione corrente e persona che approva le modifiche.

## Punti chiave

- **Assegna l'autorità per tipo di informazione**, senza forzare tutto in un'applicazione.
- **Tratta memoria e indici di recupero come cache**, mai come fonti di policy indipendenti.
- **Collega le versioni delle fonti alle proposte**, così il revisore vede quali fatti hanno guidato il cambiamento.
- **Applica l'approvazione fuori dai prompt**, con controlli di accesso e gate di revisione.
- **Condividi la procedura tra gli strumenti**, adattandola a ogni interfaccia.

## Prima di iniziare

**Prerequisiti:** scegli un progetto pilota con repository, wiki o sistema documentale, tracker e responsabili disponibili alla revisione. Senza wiki, usa un archivio documentale versionato. Mantieni invariato il modello di ownership.

**Tempo stimato:** dedica da due a quattro ore alla mappa e ai modelli iniziali, poi una settimana al pilota. **Difficoltà:** media. La parte difficile è concordare l'autorità, non installare un altro strumento IA.

**Ambito:** questo è un modello operativo proposto. Regole di approvazione e convenzioni di nome non sono comportamenti predefiniti garantiti da Claude Code, Codex, Cline, Cowork, Copilot o ChatGPT.

## Strumenti misti, contesto separato

**Sviluppatori e non sviluppatori condividono un progetto**, ma usano interfacce diverse. Lo sviluppatore usa IDE o agente terminale. Il product owner usa un progetto chat. Il responsabile operations usa wiki e tracker. Scegli l'interfaccia in base al compito, non all'accesso ai fatti autorevoli.

**Il contesto è il materiale disponibile per la risposta corrente.** Controlla file del repository, documenti caricati, cronologia chat, memoria salvata, risultati dei connettori ed estratti recuperati. Due sessioni con prove diverse possono dare risposte diverse.

| Errore | Cosa osservi |
|---|---|
| **Deriva documentale** | Un README ripete un requisito obsoleto |
| **Promozione del riepilogo** | Un riepilogo diventa prova senza la fonte originale |
| **Scritture sovrapposte** | Due agenti sostituiscono la stessa pagina da versioni base diverse |
| **Decisioni perse** | Un accordo di riunione non arriva al registro |
| **Provenienza assente** | Una risposta plausibile non cita versione della pagina o commit |

**L'esempio della conservazione distingue i ruoli.** Il wiki descrive il comportamento approvato. Il codice descrive quello implementato. Nessuno dei due deve riscrivere l'altro senza registrare il conflitto. Chiedi al responsabile di decidere.

> **Punto chiave:** concordare l'autorità viene prima di scegliere lo strumento IA.

### Riquadro: cinque termini condivisi

| Termine | Significato nel framework |
|---|---|
| **Fonte** | Record autorevole per un tipo di informazione |
| **Cache** | Copia derivata usata per velocità o comodità |
| **Proposta** | Modifica suggerita in attesa dell'approvazione del responsabile |
| **Mappa di progetto** | Indice di posizioni, identificatori e responsabili delle fonti |
| **Manifesto** | Registro delle prove esatte usate per risposta o proposta |

## Una sede per ogni fatto

**Una fonte significa un'autorità per ogni fatto**, non un unico database per l'organizzazione. Definisci questa assegnazione durante il pilota.

| Tipo di informazione | Sistema principale | Responsabile | Chi scrive | Come leggono gli agenti |
|---|---|---|---|---|
| **Codice, test, configurazione, schemi** | Repository | Responsabile engineering | Contributor tramite PR revisionate | File a un commit registrato |
| **Documenti pubblicati e ADR** | Repository | Responsabile tecnico | Contributor nella stessa PR | File versionati |
| **Requisiti** | Wiki | Product owner | Owner o publisher approvato | ID e revisione pagina |
| **Runbook** | Wiki | Responsabile operations | Publisher approvato | ID e revisione pagina |
| **Policy** | Wiki | Responsabile policy | Publisher approvato dopo revisione | Pagina canonica e adapter locale |
| **Decisioni tra team** | Registro decisioni wiki | Responsabile nominato | Owner dopo approvazione | ID e stato decisione |
| **Task e risultati** | Tracker | Responsabile task | Persone o intake autorizzato | Chiave e revisione issue |
| **Chat, riepiloghi, embedding** | Solo cache | Steward sessione o indice | Strumenti e partecipanti | Riferimento seguito dal controllo fonte |

Un ADR resta vicino al codice quando governa il design del repository. Una decisione tra team resta nel registro comune. Le copie locali della policy sono subordinate alla pagina canonica. La cache non sostituisce la fonte.

## La cache scende, la proposta sale

**Gli agenti portano le prove nel contesto della sessione**, poi preparano proposte. Non approvano fatti duraturi da soli. Modificare un branch o inviare una bozza non equivale a pubblicare policy o fondere codice.

```text
Source -> permission-checked read -> session context
Session context -> proposal + base version -> owner review
Owner approval -> controlled publication -> change log
Changed base version -> reconcile proposal -> review again
```

**Collega la versione base** prima della revisione. Servono valore precedente, valore proposto, motivo, prove e sistemi coinvolti. L'approvazione deve indicare una revisione precisa.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Retain exports for thirty days instead of seven."
evidence:
  - "decision:DEC-12 accepted"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**Gli identificatori sono illustrativi.** Conserva una riga di change log per ogni modifica approvata con ID proposta, versioni precedente e risultante, approvatore, timestamp e riferimento di merge o pubblicazione.

## Contesto condiviso senza RAG

**La mappa di progetto è il primo indice di recupero.** Mantieni una pagina per progetto con ID delle fonti, posizioni del repository, chiavi del tracker, ambiti di autorità e responsabili. Leggi la mappa, poi recupera il record per ID.

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

**I connettori diretti riducono la copia manuale.** MCP è un protocollo d'integrazione per esporre strumenti e contesto alle applicazioni IA. I connettori approvati riducono la copia, ma non sostituiscono autorizzazione e controllo della freschezza. Nel lavoro offline registra la revisione esportata come snapshot.

## Una policy, adapter diversi

**Mantieni una policy condivisa**, poi distribuisci adapter brevi per ogni strumento. Metti la versione approvata sulla prima riga di ogni adapter, con ID fonte e snapshot locale revisionato. Verifica il caricamento installato di `AGENTS.md`, `CLAUDE.md` e `.clinerules/`.

### Riquadro: intestazione AGENTS.md

```markdown
Policy-Version: v3 | Source: wiki:POL-01 | Status: approved

# Project instructions

Read the project map MAP-01 before starting a task.
Load docs/policy-snapshot.md and record its source revision.
Treat chat memory and search excerpts as caches.
Attach source revisions to every factual proposal.
Use one task and one worktree per coding task.
Do not publish policy, approve decisions, or merge your own code.
Stop on unresolved source conflicts or overlapping writes.
Required checks: tests, documentation review, policy freshness.
Owners: engineering maintainer, product owner, policy owner.
```

Un'etichetta di versione non prova che il contenuto sia identico. Genera gli adapter dallo snapshot approvato oppure confronta la parte policy con un digest. Controlla eccezioni, regole disattivate e override locali.

## Registra un manifesto del contesto

**Il manifesto spiega le prove della risposta.** Registra ID e revisioni delle pagine, chiavi e revisioni delle issue, commit completo del repository, ora di recupero e sezioni usate.

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
  - "Runbook not retrieved. No runbook change proposed."
```

Il commit sintetico va sostituito con quello ispezionato. Collega ogni affermazione materiale alla fonte e alla sezione. Se le fonti divergono, conserva entrambe e verifica ambito e approvazione.

## Contesto condiviso con RAG

**La retrieval-augmented generation (RAG)** fornisce materiale recuperato al modello mentre crea la risposta. Un indice semantico trova passaggi con parole diverse. Usala per esplorare raccolte grandi, non per trasformare una trascrizione in policy approvata.

| Regola indice | Comportamento richiesto |
|---|---|
| **Ingest sources, not caches** | Escludere riepiloghi generati e copie non tracciate |
| **Preserve provenance** | Conservare ID, revisione, sezione e stato per ogni frammento |
| **Refresh on change** | Reindicizzare le modifiche e invalidare i frammenti obsoleti |
| **Honor access changes** | Aggiornare permessi e rimuovere contenuti revocati |
| **Return citations** | Esporre riferimenti accanto al testo recuperato |
| **Check the live record** | Recuperare prove attuali prima di una proposta importante |

Un frammento recuperato è un puntatore. La fonte attiva conferma formulazione, eccezioni e accesso. Se il recupero attivo fallisce, etichetta lo snapshot e ferma l'azione duratura. Embedding vecchi e contesto mancante creano rischi diversi. Applica l'autorizzazione prima di restituire frammenti al modello.

## Scegli mappa, RAG o entrambe

**Adatta il recupero alla domanda.** Un ID noto favorisce l'accesso diretto. Una domanda su materiale storico sparso favorisce la ricerca. Parti dalla mappa quando la scoperta non è un problema misurato.

### Riquadro: RAG o no?

```text
Do tasks usually name a project, page, issue, or file?
  Yes -> Is direct retrieval sufficient for the pilot?
           Yes -> MAP ONLY
           No  -> HYBRID: map for known IDs, RAG for discovery
  No  -> Is evidence scattered across a large collection?
           No  -> MAP ONLY, plus native search
           Yes -> Is work exploratory and read-only?
                    Yes -> RAG-LED ONLY for discovery
                    No  -> HYBRID with live-source checks

Every option retains owners, authorization, and provenance.
RAG-led discovery still checks sources before durable action.
```

RAG-only descrive l'interfaccia di recupero, non il permesso di ignorare la governance. Il modello ibrido separa scoperta e verifica. La mappa risponde “dove”, la fonte “cosa”.

## Informazioni dentro il repository

**La conoscenza del repository cambia con l'implementazione.** Mantieni una struttura compatta per agenti e revisori.

| File o directory | Responsabilità |
|---|---|
| **`CONTEXT.md`** | Termini del progetto e link alle fonti autorevoli |
| **`docs/adr/`** | Decisioni di architettura accettate |
| **`docs/design/`** | Descrizioni approvate del comportamento |
| **`docs/plans/`** | Piani proposti con stato esplicito |
| **`AGENTS.md`** | Gate di revisione, confini e ruoli |
| **`README.md`** | Setup e punti di ingresso, senza requisiti duplicati |

**Applica la regola della stessa PR:** modifica insieme codice e documentazione interessata. Se non serve un aggiornamento, scrivi l'eccezione nella PR. Usa un task, branch e worktree per lavoro. Non fare commit diretto sul branch predefinito.

```text
KB-Update: none (reason: internal refactor preserves documented behavior)
```

## Informazioni fuori dal repository

**Il wiki richiede uno standard documentale.** Ogni pagina autorevole ha scopo, stato, owner, revisione, data di revisione e ID correlati. Le proposte restano in bozze non autorevoli.

**Sequenza sicura:** rileggi pagina e vincoli, confronta la versione base, riconcilia le modifiche intermedie, scrivi con condizione sulla versione attesa, verifica la pagina e il change log. Usa scritture condizionali quando disponibili. Nei risultati del tracker conserva comando, commit, comportamento atteso e reale e criteri di accettazione.

```text
Finding: retention implementation disagrees with approved requirement
Evidence: REQ-17 v8 and inspected config/retention.yaml
Inspection command: git show HEAD:config/retention.yaml
Commit: full inspected commit ID recorded in the manifest
Acceptance: approved duration matches code, tests, and runbook
Status: awaiting product and engineering owner review
```

Il registro separa regole e ragionamento. Gli agenti propongono. Le persone decidono.

## Collega i due sistemi

**La sincronizzazione post-merge porta fuori le modifiche.** Crea un task wiki collegato a commit, requisito e runbook. Il proprietario verifica la pagina salvata. L'audit di freschezza della policy resta separato.

| Controllo | Prova di completamento |
|---|---|
| **Freschezza policy** | Confronto versione canonica e digest adapter |
| **Riconciliazione requisiti** | Revisione requisito confrontata con codice e test |
| **Sync post-merge** | Commit collegato alla revisione wiki pubblicata |
| **Risoluzione conflitti** | Decisione approvata collegata ai due record |

Un audit settimanale va bene per il pilota. Una PR che cambia comportamento richiede il controllo del requisito prima del merge. Il cambiamento da trenta giorni attraversa approvazione prodotto, codice e test, revisione PR e pubblicazione del runbook.

## Una procedura per ogni strumento

**Raccogli i passaggi ripetuti in skill o prompt**, con un ID di procedura versionato. Condividi il contratto, non un formato universale.

| Procedura | Output richiesto |
|---|---|
| **Avvia task** | Owner, ambito, versione policy, manifesto, prenotazione scrittura |
| **Lint documentazione** | Metadati mancanti, autorità duplicata, riferimenti rotti |
| **Controllo conoscenza** | Lacune requisito-codice con revisioni di supporto |
| **Handoff** | Prove correnti, proposte, controlli completati, domande aperte |

I non sviluppatori usano progetti chat e lo stesso modello di proposta. Gli sviluppatori collegano la proposta nella PR e registrano commit e controlli. Entrambi passano la stessa struttura di prove.

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

Un handoff è ancora una cache. Il destinatario rilegge le fonti e controlla le revisioni.

## Guardrail prima di ogni scrittura

**Controlla i dati prima che escano dalla sede.** Verifica classificazione, permessi, destinazioni, trattamento del provider e logging. Invia solo il minimo necessario. Il testo recuperato è prova, non canale di istruzioni. Assegna un owner attivo a ogni pagina o file e registra prenotazione e scadenza.

| Segnale di stop | Risposta richiesta |
|---|---|
| **Fonti in conflitto senza owner** | Fermati e chiedi assegnazione dell'autorità |
| **Un altro task riserva la destinazione** | Negozia la proprietà prima di modificare |
| **Versione base cambiata** | Riconcilia e chiedi nuova approvazione |
| **Affermazione materiale senza prova** | Marcala non verificata e chiedi una fonte |
| **Gestione dati incerta** | Mantieni il contenuto nel sistema di origine |
| **Fonte attiva non accessibile** | Registra i limiti dello snapshot e ferma l'azione |

I prompt non sono controlli di sicurezza. Testa rifiuto permessi, branch protetti, base obsoleta e ownership fuori dal modello.

## Pilota prima della promozione

**Inizia come bozza.** Pilota un progetto con sviluppatore, non sviluppatore e owner delle fonti. Ripeti una domanda con due strumenti e crea un conflitto deliberato. Valuta manifesti e proposte.

| Metrica | Definizione |
|---|---|
| **Tasso di citazione** | Affermazioni sostenute da fonte divise per affermazioni materiali campionate |
| **Rilievi di deriva settimanali** | Incongruenze confermate per tipo di fonte |
| **Tempo proposta** | Mediana da proposta pronta alla decisione registrata |
| **Rielaborazione da contesto obsoleto** | Task riaperti per prove obsolete o non verificate |

Misura una baseline prima degli obiettivi. Un aumento dei rilievi può indicare una migliore rilevazione. Prepara un repository sintetico con map, adapter, manifesti, modelli e controlli eseguibili.

## Risoluzione dei problemi del contesto

| Sintomo | Primo intervento |
|---|---|
| **Due strumenti rispondono diverso** | Confronta ID, revisioni, ambito e approvazione |
| **Istruzioni attuali, comportamento diverso** | Ispeziona adapter caricati, opzioni e override |
| **RAG restituisce requisiti vecchi** | Controlla refresh indice e pagina attiva |
| **Una modifica wiki cancella un'altra** | Richiedi scritture condizionali o pubblicazione seriale |
| **I controlli documentali accettano testo vecchio** | Aggiungi owner review e riconciliazione requisito |
| **Le decisioni restano in chat** | Assegna intake e owner del registro |

**Correggi il percorso delle prove prima del prompt.** Ripeti il caso del pilota e registra il risultato.

## Dieci passi questa settimana

1. **Scegli un progetto pilota** e partecipanti.
2. **Assegna sede e owner** a ogni tipo di informazione.
3. **Pubblica una mappa di progetto** con ID e ambiti.
4. **Prepara una policy condivisa** e ottieni la revisione.
5. **Versiona ogni adapter** e verifica il caricamento.
6. **Richiedi un manifesto del contesto** per risposte e proposte fattuali.
7. **Crea un intake di proposta** con versioni base e approvatori.
8. **Applica controlli di scrittura** e regola documentale della stessa PR.
9. **Testa deriva, conflitto e handoff** con record sintetici.
10. **Rivedi le metriche** e approva la fase successiva.

**Dai a ogni fatto una sede, fai leggere ogni strumento da quella sede e fai passare ogni modifica duratura da una persona.**

## Riferimenti e prossimi passi

**La documentazione ufficiale supporta i componenti tecnici**, non le regole organizzative del framework. Verifica il comportamento installato e i permessi dei connettori durante il pilota.

- **Istruzioni Codex:** [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- **Istruzioni Claude Code:** [How Claude remembers your project](https://code.claude.com/docs/en/memory)
- **Istruzioni Cline:** [Rules](https://docs.cline.bot/customization/cline-rules)
- **Design del recupero:** [Retrieval-augmented generation in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- **Sicurezza dei connettori:** [MCP Security Best Practices](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices)
- **Isolamento worktree:** [Git worktree documentation](https://git-scm.com/docs/git-worktree)

**Per pianificare l'inferenza locale**, leggi la [Guida al contesto GPU per l'IA locale](/articles/local-ai-model-gpu-context-guide/). Capacità hardware e governance delle fonti sono problemi diversi. Una finestra di contesto più grande non corregge autorità in conflitto.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Leggi la Guida al contesto GPU per l'IA locale
{{< /centerbutton >}}
