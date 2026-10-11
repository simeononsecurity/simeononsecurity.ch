---
title: "Collaborazione IA con GitHub: confini del repository e delle revisioni"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Crea una mappa delle fonti centrata su GitHub, assegna la proprietà dei file e definisci un confine di pubblicazione protetto per i contributi IA revisionati."
genre: ["Intelligenza artificiale", "Collaborazione di squadra", "Ingegneria del software"]
tags: ["corso di collaborazione IA", "repository GitHub", "protezione del branch", "CODEOWNERS", "mappa delle fonti", "revisione pull request", "controlli di pubblicazione"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustrazione di professionisti che revisionano il lavoro condiviso di un progetto in un ambiente di cybersicurezza"
coverCaption: ""
---

[Torna al corso sulla collaborazione IA](/ai-collaboration-course-start/)

**Il maintainer costruisce il confine di pubblicazione centrato su GitHub** dopo l'approvazione della carta. Requisiti, configurazione, policy e runbook vivono in un repository usa e getta. I collaboratori propongono il lavoro tramite Issues e pull request. Stabilisci dove vivono i fatti approvati e blocca le modifiche non revisionate prima di collegare gli agenti.

## Punti chiave

- **`main` protetto** è il confine di pubblicazione.
- Le **Issues** raccolgono il lavoro proposto senza approvare la policy.
- **CODEOWNERS** assegna i revisori idonei dei file.
- **Utenti separati** dimostrano i controlli di revisione e rifiuto.

## Prima di iniziare

**Prerequisiti:** la [base del pilota](/articles/ai-collaboration-pilot-foundation/), il laboratorio estratto, un amministratore del repository e revisori separati per prodotto e operazioni. **Tempo stimato:** 60 minuti. **Difficoltà:** moderata.

**Limite del piano:** GitHub documenta i branch protetti per i repository pubblici su Free e per i repository privati su Pro, Team o Enterprise. Usa repository pubblici solo per contenuti sintetici. Verifica visibilità e piano nella guida dei branch protetti prima di affidarti all'applicazione.

**Risultato:** termini con un branch di pubblicazione protetto, proprietari dei file, una mappa delle fonti e un test di rifiuto registrato come evidenza.

## Crea il repository

1. **Crea `export-service-lab`** con un README e il branch predefinito **`main`**.
2. **Copia il laboratorio estratto** nella radice del repository, conservando **`check.py`**, **`test_check.py`** e **`baseline/`**. Copia i file di registrazione della baseline nella radice come registrazioni iniziali.
3. **Crea `docs/project-map.md`** usando il registro della fondazione. Aggiungi **`docs/policy.md`** con POL-01 approvata.
4. **Crea `docs/decisions/DEC-12.md`** con approvazione della carta, ruoli, decisione sulla baseline e stato.
5. **Esegui il commit dell'avvio** come amministratore. Registra questa eccezione iniziale. Abilita la protezione prima dei contributi successivi.

**Procedura di avvio locale per Git Bash, macOS Terminal o una shell Linux:** accedi a GitHub nel browser, apri il nuovo repository, seleziona **Code** e copia il suo URL di clonazione HTTPS. In una directory di lavoro usa e getta, esegui i comandi sotto. Sostituisci i due percorsi segnaposto con l'URL e il percorso del file ZIP del laboratorio scaricato. Non inserire un token nell'URL.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

Il comando clone deve assegnare al repository il nome della directory. Se `unzip` non è disponibile, estrai lo ZIP con il gestore file e copia il contenuto in questa copia di lavoro, lasciando intatto il README del repository. Salva `docs/project-map.md`, `docs/policy.md` e `docs/decisions/DEC-12.md` dal pacchetto della fondazione usando un editor di testo. Poi esegui:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git deve riportare un nuovo ID del commit e poi un push riuscito verso `main`. Lo stato breve finale deve essere vuoto. Apri il repository GitHub in una nuova vista del browser e conferma che file e ID del commit appaiano su `main`. Salva l'URL del commit come evidenza dell'avvio. Se Git richiede l'identità dell'autore, segui il setup bridge nel corso. Se l'autenticazione fallisce, usa il flusso di credenziali supportato da GitHub e riprova lo stesso push. Se branch o remote sono errati, fermati e controlla `git branch --show-current` e `git remote -v` prima di un'altra scrittura. Se il push viene rifiutato perché la protezione è già attiva, apri un branch di proposta e una PR invece di aggirare la regola. La procedura solo browser sotto resta disponibile per un maintainer.

| Record | Posizione | Proprietario |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Responsabile della policy |
| **REQ-17** | `requirement.json` | Responsabile prodotto |
| **RUN-04** | `runbook.md` | Responsabile operazioni |
| **Comportamento** | `config.json` | Maintainer |
| **Decisioni** | `docs/decisions/` | Responsabile del progetto |

**La mappa collega le posizioni invece di copiare i valori.** Mantieni il README concentrato sulla configurazione e sulla mappa. La ripetizione dei requisiti di conservazione crea deriva anche in un solo repository.

## Assegna i proprietari dei file

**Genera `.github/CODEOWNERS`** localmente con gli handle reali del sandbox. Inserisci gli handle senza il **`@`** iniziale. Mantieni le identità degli account nel laboratorio privato, non nelle evidenze pubbliche dell'esercizio.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

I proprietari devono avere accesso in scrittura perché GitHub li riconosca. Controlla nel browser il file CODEOWNERS per verificare gli errori. Proteggi i file di proprietà e le definizioni dei workflow insieme al contenuto ordinario.

**Più nomi sulla stessa riga non richiedono l'approvazione di tutti i proprietari elencati.** GitHub accetta l'approvazione di un proprietario idoneo per il percorso corrispondente. Usa proprietari designati distinti per i percorsi dei requisiti e del runbook. Il pilota richiede anche attestazioni del proprietario prodotto e del proprietario operazioni legate alla proposta finale.

## Proteggi la pubblicazione

1. **Apri Settings, Branches** e aggiungi una regola di protezione del branch per **`main`**. Usa sempre il percorso di protezione dei branch invece di mescolarlo con i ruleset in questo esercizio.
2. **Richiedi una pull request**, due revisioni approvate e la revisione dei code owner.
3. **Rimuovi le approvazioni obsolete** dopo i nuovi commit e richiedi la risoluzione delle conversazioni.
4. **Abilita Do not allow bypassing the above settings.** Mantieni disabilitati force push e cancellazione.
5. **Aggiungi il controllo di coerenza** dopo la sua prima esecuzione nel modulo successivo. Richiedi branch aggiornati prima del merge.

**Due approvazioni impongono un conteggio, non l'appartenenza a un ruolo aziendale.** CODEOWNERS aggiunge copertura basata sul percorso. Il maintainer controlla anche le due attestazioni di ruolo. Registra esplicitamente questo controllo procedurale invece di descriverlo come applicazione automatica di due ruoli.

**Gli amministratori gestiscono comunque la configurazione.** Acquisisci la regola prima e dopo i test. Non concedere a un agente l'accesso amministrativo e non usare un token privilegiato per dimostrare il rifiuto del collaboratore.

## Verifica il confine

| Tentativo | Risultato previsto |
|---|---|
| **Il collaboratore invia un branch** | Proposta consentita |
| **Il collaboratore pubblica direttamente** | Pubblicazione protetta rifiutata |
| **Un revisore approva** | Merge bloccato dalla soglia di revisione |
| **Un nuovo commit segue la revisione** | Nuova approvazione richiesta |
| **Un file sensibile non ha copertura del proprietario** | Correggere prima della pubblicazione |

**Usa la sessione browser del collaboratore per esaminare il percorso.** L'editor web di GitHub non modifica un branch **`main`** protetto. Un prompt per creare un branch mostra il percorso browser supportato. Non dimostra che il server abbia rifiutato un push diretto. Per l'evidenza del rifiuto della piattaforma, chiedi a un collaboratore con accesso Git locale approvato di tentare un push diretto innocuo verso **`main`** protetto e conserva la risposta del server. Segna il test di rifiuto come Bloccato quando l'accesso locale non è disponibile.

**Leggi `main` dopo il rifiuto** e conferma che la revisione non sia cambiata. Registra ruolo dell'attore, azione tentata, risultato e revisione sorgente. La promessa di un assistente di non pubblicare è evidenza comportamentale, non un test dei permessi della piattaforma.

**Usa il clone locale autenticato del collaboratore per il test del push diretto.** Un token del maintainer verificherebbe l'identità sbagliata. Questa risposta illustrativa mostra il tipo di evidenza del server da conservare. La formulazione esatta varia secondo le regole del repository.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Se l'autenticazione Git locale non è disponibile, segna il rifiuto lato server come Bloccato.** Conserva il prompt del branch del browser come evidenza del percorso, poi chiedi al maintainer di organizzare un test separato con un collaboratore. Non valutare il prompt del percorso come un push diretto rifiutato.

## Costruisci una mappa delle fonti utile

**Una mappa delle fonti è un documento di instradamento**, non un secondo documento dei requisiti. Chi arriva dalla chat deve trovare intento corrente, comportamento implementato e istruzioni operative senza scegliere tra riepiloghi concorrenti.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Non inserire il valore corrente di conservazione in ogni voce della mappa.** Una mappa con «sette giorni» diventa un altro valore da sincronizzare dopo PROP-042. Mantieni nella mappa identificatori stabili e posizioni, poi leggi il valore dal record autorevole.

**Proteggi le modifiche alla mappa come modifiche di instradamento.** Reindirizzare REQ-17 a un file di bozza modifica la selezione della fonte anche se il requisito approvato resta intatto. Revisiona destinazione, proprietario e ambito dell'autorità ogni volta che cambia la mappa.

## Separa baseline e candidato

**La radice del repository contiene i record attivi del laboratorio.** La directory **`baseline/`** scaricata è un dispositivo didattico. Non è automaticamente la baseline protetta per ogni PR successiva. Quando il lavoro revisionato raggiunge **`main`**, i record protetti nella radice definiscono la base della proposta successiva.

| Posizione | Scopo | Modificare durante PROP-042? |
|---|---|---|
| **Record radice di requisito/configurazione/runbook** | Record attivi proposti sul branch | Sì, tramite modifiche revisionate |
| **`baseline/`** | Fixture originale dell'esercizio offline | No |
| **Worktree trusted scollegato** | Record radice protetti acquisiti | No |
| **`context.json`** | Evidenza dei byte della base acquisita | Rigenerare dopo il riconcilio |

**Mantieni separati i cambiamenti ai controlli e quelli alla conservazione.** Avvia prima checker e regole di revisione. Poi proponi il cambio da sette a trenta giorni. Unire riscrittura della policy, del workflow e del valore rende più difficile distinguere controlli riparati da controlli aggirati.

## Revisiona la modifica completa

**Apri Files changed prima di accettare la descrizione di una PR.** La descrizione spiega l'intento dell'autore. Il diff mostra la modifica inviata. Per PROP-042, esamina revisione del requisito, esclusioni dell'ambito, configurazione, runbook, base della proposta ed evidenze del manifest.

1. **Revisione prodotto:** conferma l'intento di trenta giorni e le esclusioni invariate.
2. **Revisione operazioni:** conferma che il runbook corrisponda alla configurazione proposta e conservi la limitazione runtime.
3. **Revisione maintainer:** controlla JSON, acquisizione della fonte, risultati del checker e modifiche estranee.
4. **Revisione dei controlli:** esamina separatamente ogni modifica a mappa, policy, CODEOWNERS o workflow.

**Un controllo verde non spiega una cancellazione estranea.** Se il branch rimuove il documento di policy mentre modifica la conservazione, richiedi una proposta separata o una revisione da parte di un proprietario specifico. Limitare l'ambito mantiene comprensibile l'oggetto della revisione.

## Diagnostica un test di rifiuto

**Usa una sola azione tentata per ogni riga di evidenza.** «Il collaboratore ha fallito» è ambiguo. L'utente potrebbe non avere accesso ordinario in scrittura, incontrare una limitazione del browser o colpire la regola del branch prevista. Queste osservazioni stabiliscono confini diversi.

| Osservazione | Interpretazione | Seguito |
|---|---|---|
| **Non può creare alcun branch** | Manca l'accesso ai contributi | Usa una Issue approvata o un percorso fork |
| **Crea il branch, non può pubblicare su main** | Il percorso di pubblicazione testato è limitato | Acquisisci la revisione invariata di main |
| **Merge bloccato con una revisione** | Il conteggio delle revisioni vale per la PR testata | Aggiungi evidenza specifica del ruolo |
| **L'amministratore pubblica nonostante la regola** | L'identità testata aggira il confine | Esamina impostazioni di bypass e permessi |

**Registra ruolo e azione senza esporre dettagli dell'account** nelle evidenze condivise del corso. Conserva privatamente i record nativi dell'attore per il revisore. Acquisisci insieme configurazione della regola, operazione tentata, rifiuto e revisione protetta risultante.

## Controllo di completamento del repository

**Consegna un repository che un altro collaboratore possa consultare in autonomia.** Il README punta alla mappa, la mappa risolve i record autorevoli, la copertura dei proprietari include i percorsi sensibili e la protezione si applica a **`main`**. Conserva una proposta consentita e un tentativo di pubblicazione rifiutato.

**Non rivendicare l'applicazione basandoti solo sulle impostazioni.** Le impostazioni stabiliscono la configurazione prevista. Il tentativo nel sandbox stabilisce il comportamento osservato per un ruolo e un percorso specifici. Porta entrambi nella lezione su agenti e Actions.

## Risoluzione dei problemi e rollback

**Richiesta del proprietario mancante:** conferma accesso in scrittura e copertura del percorso del branch di base. **Protezione assente:** verifica piano e visibilità. **Merge ancora abilitato:** controlla obiettivo della regola, configurazione del bypass e numero di revisioni.

**Rollback:** chiudi le proposte non unite e disattiva l'automazione del laboratorio. Annulla il contenuto unito tramite un'altra PR revisionata. Conserva le evidenze prima di eliminare il repository usa e getta. Non indebolire la protezione per terminare un test fallito.

## Esercizio e autoverifica

**Proponi una modifica a `docs/policy.md`** come collaboratore. Decidi se la sola approvazione del maintainer stabilisca l'approvazione del proprietario della policy.

**Ragionamento atteso:** il conteggio delle revisioni da solo non stabilisce l'autorità. Il percorso richiede copertura del proprietario della policy e revisione corrente del ruolo. Elenca come controlli procedurali i requisiti specifici del ruolo non applicati.

## Riferimenti principali

- **Controlli del piano e delle revisioni:** [Branch protetti](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Idoneità dei proprietari:** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Contributo dal browser:** [Modifica dei file](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Prossimi passi

**Continua con [Adapter degli agenti e Actions](/articles/ai-collaboration-github-agents-actions/)** per collegare le evidenze delle fonti ai controlli eseguibili.
