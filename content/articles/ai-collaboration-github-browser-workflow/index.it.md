---
title: "Workflow GitHub con IA per non programmatori: issue e pull request"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Usa modifiche dal browser, issue, pacchetti di contesto della chat e pull request revisionate senza un ambiente di sviluppo locale."
genre: ["Intelligenza artificiale", "Collaborazione di team", "Ingegneria del software"]
tags: ["corso di collaborazione con IA", "modifica GitHub dal browser", "GitHub Issues", "pull request", "collaboratori non programmatori", "pacchetto di contesto", "passaggio per la revisione"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustrazione di professionisti che revisionano un progetto condiviso in un ambiente di lavoro per la cybersicurezza"
coverCaption: ""
---

[Torna al corso sulla collaborazione con l'IA](/ai-collaboration-course-start/)

**I collaboratori non programmatori applicano le stesse regole di autorità attraverso il browser.** Leggi le fonti GitHub, prepara una bozza con uno strumento di chat approvato e invia un'issue o una modifica su un branch. Il maintainer esegue i controlli e pubblica dopo la revisione. Usa questo workflow dopo aver attivato la protezione del repository, così l'accesso dal browser non aggira i controlli dell'agente di codifica.

## Punti chiave

- **Il lavoro dal browser** non richiede un terminale locale.
- **I pacchetti di contesto** conservano ambito e prove delle revisioni.
- **Issue e branch** restano proposte.
- **I passaggi di consegne** identificano il lavoro in sospeso e il ruolo successivo.

## Prima di iniziare

**Prerequisiti:** la [lezione sui confini del repository](/articles/ai-collaboration-github-repository/), accesso in lettura al laboratorio e, se desiderato, uno strumento di chat approvato. **Tempo stimato:** da 45 a 60 minuti. **Difficoltà:** introduttiva. I collaboratori che usano solo le issue saltano Git locale e Actions. I collaboratori che inviano una PR si coordinano con un maintainer che ha completato la [lezione su agenti e Actions](/articles/ai-collaboration-github-agents-actions/).

**Base senza connettori:** apri GitHub tu stesso e fornisci solo estratti sintetici. Non si presume alcuna funzione di abbonamento alla chat. Se un provider non è approvato, prepara la bozza manualmente usando gli stessi record.

**Risultato:** consegni un'issue o una PR con revisioni delle fonti fissate, testo proposto, file interessati, esclusioni e domande irrisolte.

## Leggere il pacchetto delle fonti

1. **Apri MAP-01 su `main`**, poi individua POL-01, REQ-17 e RUN-04.
2. **Leggi ogni fonte** e annota la relativa revisione del commit dalla vista dei commit del browser.
3. **Copia le sezioni sintetiche pertinenti** con nomi dei file, revisioni, ambito ed eccezioni.
4. **Etichetta il pacchetto come basato su uno snapshot** finché il maintainer non lo confronta con le fonti correnti prima della pubblicazione.

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Allega privatamente le revisioni effettive della sandbox.** Il modello non contiene prove complete. Chiedi all'assistente di identificare i record mancanti prima di raccomandare la pubblicazione.

**Pacchetto sintetico compilato prima di leggere una fonte live:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs checks
```

**Il pacchetto è una richiesta completa in forma di bozza.** La riga sulle prove mancanti è intenzionale. Sostituisci la base del laboratorio fornita con le revisioni correnti della sandbox prima di chiedere la pubblicazione.

## Aprire un'issue

**Seleziona Issues, New issue** e usa il titolo **`PROP-042: propose thirty-day synthetic retention`**. Incolla questa descrizione e allega il pacchetto delle fonti.

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Chiedi alla chat di confrontare la proposta con il pacchetto**, elencare le ipotesi e preparare le domande per i responsabili. Salva la bozza nell'issue. Non chiederle di approvare la modifica e non trattare il thread della chat come registro delle decisioni.

## Inviare modifiche dal browser

1. **Apri la scheda Code del repository.** Seleziona il menu dei branch sopra l'elenco dei file, conferma **`main`**, digita **`proposal-042`** e scegli **Create branch: proposal-042 from main**. Se la creazione del branch non è disponibile, usa un fork approvato o il percorso dell'issue riportato sotto.
2. **Conferma `proposal-042` nel menu dei branch** prima di aprire un file. Seleziona il file e la sua icona a matita per modificarlo. L'editor web di GitHub non modifica un branch protetto.
3. **Modifica il requisito** a trenta giorni e alla revisione 2. Riapri il menu dei branch prima di ogni modifica restante. Modifica configurazione e runbook sullo stesso branch.
4. **Modifica `proposal.json`** con to_days 30, from_days 7 e base_revision 1.
5. **Visualizza l'anteprima Markdown** e controlla la punteggiatura JSON. Esegui il commit di ogni modifica dal browser su **`proposal-042`**.
6. **Apri Pull requests, poi New pull request.** Confronta **`proposal-042`** con **`main`**, controlla tutte e quattro le modifiche ai file e crea una PR che richiami l'issue. Chiedi al maintainer di allegare un manifest aggiornato della base protetta ed eseguire il controllo di coerenza.
7. **Richiedi le revisioni dei responsabili** sull'ultima revisione della proposta. Mantieni aperta la consegna finché revisione e rilettura non sono riuscite.

**Registro di navigazione:** annota nome del repository, numero dell'issue, branch della proposta, percorsi dei file modificati, numero della PR, nome del controllo, revisione esaminata e commit finale di `main`. Usa le viste Issues, Code, Pull requests, Actions e PR Checks/Reviews del repository per ritrovarli. Se GitHub sposta un controllo, ritrova lo stesso record usando il numero o l'ID del commit invece di indovinare da uno screenshot. Esporta una nota privata delle prove con gli URL dei record e lo stato osservato. Prima di condividere la nota fuori dal team autorizzato, rimuovi nomi degli account, indirizzi email, token, identificativi del tenant e dati di repository non pertinenti. Conserva la prova non redatta nella posizione privata approvata.

**GitHub documenta i percorsi di contribuzione tramite branch e fork.** Un collaboratore senza accesso in scrittura al repository usa un fork approvato o il percorso dell'issue. Un fork non concede accesso alla pubblicazione nel repository originale.

## Esaminare il diff lavorato

| File | Base | Candidato |
|---|---|---|
| **Requisito** | Revisione 1, sette giorni | Revisione 2, trenta giorni |
| **Configurazione** | Sette giorni | Trenta giorni |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Proposta** | Da 7, a 7 | Da 7, a 30, base 1 |
| **Manifest** | Non acquisito | Hash delle fonti protette prima della modifica |

**Il manifest descrive la base**, non il testo proposto per trenta giorni. Fare l'hash del requisito candidato e chiamarlo prova della base crea una mancata corrispondenza con la base attendibile.

## Verificare e consegnare

**Test positivo:** il maintainer fa il merge dopo la revisione dei responsabili e il superamento dei controlli. Apri i file risultanti su **`main`** e conferma che siano coerenti. Allega all'issue il commit risultante e la rilettura. Questo dimostra la configurazione sottoposta a commit, non il comportamento runtime della cancellazione.

**Test negativo:** chiedi alla chat di approvare o pubblicare la proposta. Il comportamento previsto dalla policy è una risposta limitata alla bozza. Tenta separatamente la pubblicazione diretta come collaboratore e registra il rifiuto della piattaforma con la revisione della fonte invariata. Mantieni distinti i test comportamentali e quelli di controllo degli accessi.

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Inizia una nuova sessione solo con mappa e passaggio di consegne.** Richiedi una nuova lettura delle fonti o una richiesta esplicita delle prove del browser. La sessione deve ricostruire il valore dai record delle fonti invece di ripetere il riepilogo dell'assistente precedente.

## Preparare una bozza senza perdere il contesto

**Un collaboratore dal browser ha comunque bisogno di una domanda completa.** «Modifica la conservazione a trenta giorni» omette autorità corrente, ambito, stato della revisione e record interessati. Fornisci alla chat il pacchetto delle fonti insieme a un'istruzione di redazione. Se il record non è disponibile, chiedi al maintainer una prova autorizzata invece di sostituire il testo ricordato.

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Esamina la risposta prima di copiarla.** Controlla se ha cambiato l'ambito, inventato un commit o descritto un'approvazione come completata. Rimuovi le affermazioni senza supporto e conserva le domande irrisolte nell'issue. La chat aiuta a scrivere la proposta. Non fornisce prove da sistemi che non ha letto.

## Scegliere il percorso di contribuzione

| Situazione | Percorso | Risultato |
|---|---|---|
| **Solo accesso in lettura** | Issue con testo proposto fissato | Richiesta di modifica pronta per il maintainer |
| **Accesso approvato a un branch** | Modifiche dal browser su un branch della proposta | PR con i file correlati |
| **Percorso tramite fork approvato** | Fork e PR verso l'upstream | Candidato in attesa della revisione upstream |
| **Nessun accesso alle fonti** | Fermarsi e chiedere prove autorizzate | Attività esplicitamente bloccata |

**Il percorso dell'issue è una contribuzione completa**, non un esercizio di programmazione fallito. Fornisci modifica desiderata, prove, ambito e domande di revisione. Il maintainer fornisce la patch e il manifest. Poi esamina la patch per verificare che corrisponda alla tua richiesta.

| Percorso | Controllo di completamento del collaboratore | Passaggio al maintainer |
|---|---|---|
| **Solo issue** | L'issue contiene un pacchetto di fonti verificato, testo proposto fissato, esclusioni e domande aperte | Il maintainer crea il branch, esegue i controlli e collega la PR |
| **PR** | Un branch contiene tutti i file interessati, il diff della PR corrisponde alla proposta e i revisori ricevono l'ultima revisione | Il maintainer esegue i controlli, ottiene la revisione dei responsabili, fa il merge e registra la rilettura |

**Quando usi modifiche dal browser, resta sul branch della proposta.** Dopo la prima modifica che crea il branch, riapri ogni file restante dallo stesso selettore del branch. Controlla il diff della PR alla fine. Creare quattro branch separati produce quattro modifiche incomplete invece di un pacchetto revisionabile.

## Esaminare il testo proposto

**Esempio di formulazione debole:** «Gli export sono ora disponibili per trenta giorni.» Descrive una consegna completata e omette l'ambito sintetico. Usa una dichiarazione di proposta mentre la revisione è in corso.

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**Confronta ogni file interessato con questa formulazione.** La revisione del requisito avanza nel candidato. La configurazione raggiunge trenta giorni. La prima riga del runbook raggiunge trenta giorni mantenendo il limite del laboratorio. La proposta indica ancora sette giorni come valore precedente e la revisione uno come base.

**Chiedi spiegazioni sulle differenze invece di riparare controlli che non conosci.** Se la patch del maintainer indebolisce anche la protezione o elimina una policy, chiedi una spiegazione e una revisione separata. Non devi comprendere ogni riga del workflow per riconoscere un cambiamento fuori ambito.

## Rispondere ai commenti di revisione

**Revisione illustrativa:** operations chiede una frase che spieghi che il rollback della configurazione non ripristina i file eliminati. Aggiorna la bozza sullo stesso branch e informa i revisori dell'ambito modificato. La revisione finale deve fare riferimento alla proposta modificata, non a una copia precedente della chat.

| Commento di revisione | Azione del collaboratore |
|---|---|
| **Esclusione mancante** | Ripristinare il testo e chiedere la revisione dell'intento |
| **Revisione della fonte obsoleta** | Ottenere un nuovo pacchetto autorizzato e riconciliarlo |
| **Manifest mancante** | Chiedere al maintainer di acquisire la base protetta |
| **Modifica di controllo non correlata** | Separarla o rimuoverla prima della revisione |
| **Affermazione runtime non testata** | Sostituirla con il limite preciso del laboratorio |

**Mantieni visibili le domande finché non ricevono risposta.** Risolvere un commento senza correggere il problema sottostante elimina un segnale utile. Collega la modifica o la prova nella risposta così un altro revisore segue la decisione senza leggere l'intera conversazione.

## Controllo di completamento dal browser

**Consegna un'issue o una PR che un altro maintainer può eseguire senza supposizioni.** Deve contenere pacchetto delle fonti, testo proposto, record interessati, esclusioni, ruoli dei responsabili e domande irrisolte. Dopo la pubblicazione, acquisisci la rilettura e separala dalla proposta originale.

**Auto-controllo:** consegna il pacchetto a qualcuno che non conosce la tua chat. Chiedigli di distinguere valori richiesti, approvati e pubblicati. Se riferisce trenta giorni come già consegnati prima del merge, correggi le etichette del pacchetto. Applica la stessa disciplina al percorso professionale.

| Gate di revisione | Condizione di superamento |
|---|---|
| **Revisioni delle fonti** | Ogni commit o versione di pagina dichiarato si apre nella sandbox. Le revisioni sconosciute restano indicate come mancanti. |
| **Esclusioni** | Dati di produzione, backup e conservazioni legali restano fuori dalla proposta. |
| **Domande** | Le domande irrisolte dei responsabili o delle fonti restano visibili nell'issue o nella PR. |
| **Freschezza dell'approvazione** | Le revisioni fanno riferimento all'ultima revisione della proposta. Un'approvazione precedente non copre le modifiche successive. |

**Ogni gate fallito mantiene la pubblicazione in sospeso.** I collaboratori del percorso issue consegnano il risultato al maintainer. I collaboratori del percorso PR chiedono una nuova revisione dopo le correzioni.

## Risoluzione dei problemi e rollback

**Nessun permesso di modifica:** usa un'issue o un fork approvato. **Riferimento a un commit inventato:** sostituiscilo con una prova verificata e sottoponi la bozza a nuova revisione. **Approvazione precedente alle modifiche:** chiedi una nuova approvazione.

**Rollback:** chiudi una PR non unita conservando le sue prove. Per contenuti uniti, chiedi al maintainer una proposta di ripristino protetta. Non modificare la base per simulare un recupero riuscito.

## Esercizio e autoverifica

**Nascondi il record del requisito** al nuovo assistente e chiedi una raccomandazione sulla pubblicazione.

**Ragionamento atteso:** chiede prove autorevoli o etichetta la risposta come basata su uno snapshot. La pubblicazione resta bloccata finché una nuova lettura non riesce.

## Riferimenti principali

- **Passaggi del browser:** [Modifica dei file](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Confine della revisione:** [Branch protetti](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Prossimi passi

**Continua con [Configurazione di Confluence e Jira](/articles/ai-collaboration-confluence-jira-setup/)** per ripetere il modello operativo nei sistemi di lavoro.
