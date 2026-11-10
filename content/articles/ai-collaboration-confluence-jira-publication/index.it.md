---
title: "Flusso di pubblicazione AI per GitHub, Confluence e Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Pubblica una proposta di conservazione fissa su Confluence, GitHub e Jira, con controlli di versione e procedure per recuperare una pubblicazione parziale."
genre: ["Intelligenza artificiale", "Collaborazione di squadra", "Ingegneria del software"]
tags: ["corso di collaborazione AI", "Confluence Cloud", "Jira Cloud", "pubblicazione tra sistemi", "controllo delle versioni", "registro di pubblicazione", "pubblicazione parziale"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustrazione di professionisti che esaminano insieme il lavoro di progetto in uno spazio di lavoro per la cybersicurezza"
coverCaption: ""
---

[Torna al corso sulla collaborazione AI](/ai-collaboration-course-start/)

**Il collaboratore blocca PROP-042 prima dell'approvazione dei responsabili.** Un responsabile della pubblicazione su Confluence aggiorna i requisiti, un manutentore di GitHub integra l'implementazione e il team operativo pubblica il runbook. Jira registra ogni passaggio. Esegui queste attività dopo aver verificato le autorizzazioni, perché i tre sistemi non formano un'unica transazione atomica. Il registro di pubblicazione rende visibili le consegne incomplete.

## Punti chiave

- **L'intento approvato** è diverso dal comportamento consegnato.
- **Le revisioni fisse della proposta** vincolano il riesame.
- **I registri di pubblicazione** rendono visibile il completamento parziale.
- **Nuove letture delle fonti** proteggono da basi modificate.

## Prima di iniziare

**Prerequisiti:** la [configurazione dell'ambiente di lavoro](/articles/ai-collaboration-confluence-jira-setup/), accesso alla pubblicazione, responsabili e un manutentore del repository. **Tempo stimato:** due ore. **Difficoltà:** coordinamento avanzato.

**Interfaccia di base:** letture dal browser, stesura facoltativa di bozze in una chat approvata e pubblicazione da parte di una persona. Non si presume un abbonamento al connettore. Prima di aggiungere un'integrazione, controlla la disponibilità nel tenant, gli ambiti, la gestione del provider e la mappatura delle identità. Non condividere mai le credenziali di un responsabile con un collaboratore.

**Risultato per il lettore:** al termine avrai una proposta fissa, un registro di pubblicazione per ciascun sistema, prove di lettura di ritorno e una decisione di recupero per il primo passaggio incompleto. L'esercizio dimostra una procedura e la gestione delle prove, non il comportamento della conservazione in produzione.

## Registra le fonti aggiornate

1. **Leggi MAP-01**, poi apri REQ-17 e RUN-04 tramite gli ID di pagina mappati.
2. **Apri il menu della pagina e la cronologia (Page History)**, quindi registra le versioni numeriche, lo stato, il testo, il responsabile e le eccezioni.
3. **Leggi l'elemento Jira** e allega un'esportazione fissa della proposta o un commit GitHub. La sola chiave non blocca le prove della revisione.
4. **Leggi POL-01 approvata** e la baseline di configurazione protetta.
5. **Fornisci alla chat solo gli estratti sintetici necessari**, contrassegnali come istantanee e mantieni disabilitate le azioni con permessi di scrittura.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**I pacchetti offline restano istantanee.** Prima di scrivere, il responsabile della pubblicazione ripete le letture in tempo reale. Un accesso negato blocca la pubblicazione. Un'esportazione precedente non sostituisce un'autorizzazione aggiornata.

## Blocca la proposta

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Sostituisci le versioni illustrative delle pagine con quelle effettivamente registrate.** Allega il JSON fisso e il testo proposto a Jira. Ogni responsabile registra il ruolo, la decisione, la revisione della proposta, le versioni delle fonti e l'ora della revisione. Ogni modifica sostanziale riporta il pacchetto allo stato `Review`.

**Il team di prodotto esamina intento e ambito. Il team operativo esamina la pulizia e il recupero.** Il manutentore esamina il diff. Le reazioni ai messaggi modificabili della chat non sono approvazioni legate a una revisione.

## Pubblica e rileggi

1. **Imposta Jira su `Publishing`** dopo che il responsabile della pubblicazione ha verificato entrambe le revisioni dei responsabili e l'assenza di modifiche alle basi delle fonti.
2. **Pubblica REQ-17** con trenta giorni e un campo per la consegna in sospeso. Registra la versione risultante, l'ambito e le eccezioni.
3. **Apri la PR di implementazione GitHub**, facendo riferimento alla versione approvata della pagina. Modifica la configurazione a trenta giorni e allega un'istantanea non autorevole del requisito.
4. **Integra dopo la revisione del repository** e rileggi **`main`**. Registra separatamente il comportamento del commit e quello in fase di esecuzione.
5. **Pubblica RUN-04**, rileggilo tramite ID e registra la versione risultante. Il responsabile aggiorna i riferimenti alla consegna nel requisito.
6. **Completa Jira** solo quando tutti i record corrispondono e sono allegate le prove dell'ultima rilettura.

**Usa il validatore locale solo per verificare la coerenza delle istantanee.** Copia il requisito Confluence precedente alla modifica nello schema JSON di baseline del laboratorio, acquisiscilo e modifica la versione candidata a trenta giorni. Incrementa la revisione locale dell'istantanea e conserva separatamente in Jira le versioni reali di Confluence. Il flusso con GitHub come fonte principale non convalida Confluence in tempo reale. Non presentare il suo stato verde come verifica dell'autorità esterna.

**In questo esercizio non distribuire la cancellazione.** Un servizio reale richiede prove di distribuzione, dati di test controllati, un meccanismo di sospensione e test dei limiti di runtime. Un'integrazione dimostra lo stato del repository, non il comportamento della conservazione in produzione.

## Tieni traccia della pubblicazione parziale

| Passaggio | Stato iniziale | Prova di completamento |
|---|---|---|
| **REQ-17** | Pending | Versione risultante della pagina |
| **Configurazione** | Pending | Commit integrato e revisione |
| **RUN-04** | Pending | Versione risultante della pagina |
| **Chiusura Jira** | Pending | Rilettura finale e transizione |

**Registra ogni risultato prima di tentare il passaggio successivo.** PROP-042 collega gli eventi dei singoli sistemi. Una riga completata non significa che l'intera modifica sia terminata.

**Errore descritto:** Confluence pubblica trenta giorni, ma GitHub rifiuta l'integrazione. Mantieni Jira in stato `Blocked` e indica nel requisito che la consegna è in sospeso. Il team di prodotto sceglie se completare la pubblicazione o ripristinare, dopo una revisione, il valore di sette giorni. Non promuovere una copia di emergenza del README ad autorità del requisito.

## Gestisci le modifiche concorrenti

**Baseline del browser:** assegna un solo responsabile della pubblicazione durante la finestra pilota. Riapri la cronologia della pagina subito prima della modifica e dopo la pubblicazione. Se un altro autore modifica la fonte, fermati, confronta e riconcilia le modifiche, quindi rinnova l'approvazione. Una pubblicazione serializzata è una procedura, non una garanzia di transazione atomica.

**Estensione API:** la documentazione Confluence v2 descrive **`GET /wiki/api/v2/pages/{id}?body-format=storage`** e **`PUT /wiki/api/v2/pages/{id}`** con un oggetto versione. Un'integrazione di pubblicazione revisionata confronta la versione corrente con la baseline approvata, invia la versione successiva e la rilegge. Non aggiornare automaticamente una versione non riuscita per riprovare con un corpo precedente.

**Il solo successo dell'API non basta.** Verifica il contenuto risultante, l'ID della fonte, l'ambito e la versione. Questo corso non fornisce un client API con permessi di scrittura. La pubblicazione tramite browser da parte di una persona è la procedura eseguibile per i non programmatori.

## Verifica i casi negativi

| Iniezione | Ragionamento atteso |
|---|---|
| **Modificare la fonte dopo l'approvazione** | Fermarsi e riapprovare sulla nuova versione |
| **Rimuovere l'accesso in modifica al responsabile** | Negare l'aggiornamento e mantenere il registro in sospeso |
| **Impostare Jira a sessanta giorni** | Fermarsi davanti al conflitto e mantenere Confluence come autorità |
| **Pubblicazione del runbook non riuscita** | Mantenere la consegna incompleta e assegnare il recupero |

**Registra i risultati effettivi della sandbox** con il ruolo dell'attore e le revisioni precedenti e successive. Non includere i contenuti protetti delle pagine nelle prove per un utente a cui è stato negato l'accesso. I risultati attesi non sono risultati misurati.

## Prepara il pacchetto di revisione

**Blocca il contenuto, non solo l'etichetta della proposta.** PROP-042 compare in ogni sistema, ma un'etichetta non identifica il contenuto esaminato dal responsabile. Includi in un unico pacchetto fisso il testo esatto del requisito, il diff dell'implementazione, il testo del runbook, le versioni delle fonti e la sequenza di pubblicazione.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Rendi il pacchetto leggibile per entrambi i responsabili.** Il team di prodotto deve conoscere intento ed esclusioni. Il team operativo deve conoscere la modifica operativa e i limiti del recupero. Entrambi devono capire per quanto tempo l'intento approvato differisce dalla configurazione consegnata. Un semplice diff del codice non basta a un responsabile che non conosce i file del repository.

**Contenuto compilato del pacchetto per questo esempio sintetico:**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Queste stringhe sono testi di proposta esemplificativi, non record di un tenant attivo. Prima della revisione allega il commit di base e le versioni effettive delle pagine. Il pacchetto fisso deve contenere i corpi proposti completi, non un riepilogo che costringa il responsabile a dedurre i dettagli.

**Separa l'istantanea offline dalla pubblicazione in tempo reale.** Un controllo di coerenza dimostra l'accordo tra i record acquisiti. Subito prima della prima scrittura, il responsabile ricontrolla le pagine mappate e il manutentore ricontrolla la base protetta. Se uno dei due è cambiato, il vecchio pacchetto si ferma allo stato `Review`.

## Esamina il registro

**Progressione di stato illustrativa:** la tabella usa revisioni didattiche, non osservazioni. Inserisci le versioni e i commit effettivamente risultanti dopo ogni scrittura nella sandbox.

| Passaggio | Stato dopo una rilettura riuscita | Lavoro restante |
|---|---|---|
| **Revisione dei responsabili completata** | Pacchetto approvato, tutti i valori pubblicati sono sette | Tutte le fasi di pubblicazione |
| **REQ-17 pubblicato** | Intento a trenta, consegna in sospeso | Configurazione e runbook |
| **Integrazione GitHub riletta** | Intento e configurazione a trenta, runbook a sette | Runbook e riconciliazione finale |
| **RUN-04 pubblicato** | Tutti i record pertinenti a trenta | Rilettura finale indipendente |
| **Consegna chiusa** | Registro completo con prove | Le lacune di runtime dichiarate restano |

**La consegna in sospeso è uno stato significativo.** Evita di descrivere la vecchia implementazione come conforme al nuovo intento mentre la pubblicazione è incompleta. In questo periodo i lettori hanno bisogno di entrambi i valori, non di un riepilogo che dichiari che la conservazione è di trenta giorni.

**Aggiungi i tentativi non riusciti come eventi separati.** Se una scrittura del runbook fallisce, conserva i risultati riusciti per il requisito e la configurazione. Registra il tentativo di scrittura del runbook, l'errore, la versione rimasta invariata, il ruolo assegnato e l'azione successiva. Non riportare le righe completate a Pending e non cancellare la sequenza osservata.

**Esempio di rifiuto per versione non aggiornata:** il responsabile legge REQ-17 v4, un altro editor autorizzato pubblica v5 e il responsabile tenta di applicare PROP-042 r1 su v4. La piattaforma segnala un conflitto di versione oppure la lettura prima della scrittura rileva v5. Registra l'attore `publisher`, la versione iniziale `v4`, il tentativo `PROP-042 r1`, il conflitto osservato o la versione corrente modificata, la versione finale `v5` rimasta invariata per questo tentativo e il responsabile assegnato `product owner`. Mantieni Jira in stato `Review`. Rileggi v5, riconcilia il testo e richiedi la revisione di un nuovo pacchetto fisso prima di un altro tentativo di scrittura. In un test reale, usa la risposta effettiva della piattaforma e la cronologia della pagina. Questa riga è un esempio didattico.

**Esempio didattico completato, solo valori sintetici:**

| Sistema | Fonte iniziale | Revisione fissa | Scrittura e rilettura | Stato finale |
|---|---|---|---|---|
| Confluence REQ-17 | v4, sette giorni | PROP-042 r1, Product ha approvato v4 verso v5 | Il responsabile ha scritto v5, il reviewer ha riaperto v5 | Trenta giorni, backup e blocchi legali esclusi |
| Configurazione GitHub | Commit `base-001` su `main`, sette giorni | PROP-042 r1, Operations ha approvato il diff candidato | PR integrata come `merge-002`, clone indipendente ha riletto trenta | Trenta giorni nella fonte protetta |
| Confluence RUN-04 | v2, sette giorni | PROP-042 r1, Operations ha approvato v2 verso v3 | Il responsabile ha scritto v3, il reviewer ha riaperto v3 | Procedura operativa di trenta giorni con ripristino |
| Jira PROP-042 | In Review | Entrambe le decisioni dei responsabili legate a r1 | Il responsabile della consegna ha allegato le prove e impostato `Done` | Chiusura dopo tutte e tre le riletture |

Le etichette sono illustrative e non costituiscono prove di un tenant. Il registro deve contenere i collegamenti alle versioni native delle pagine e gli ID dei commit. Prima di impostare Jira su `Done`, allega la proposta bloccata, le revisioni di entrambi i ruoli, il record della base di partenza, ogni lettura di ritorno della pubblicazione, il risultato del test negativo e i limiti di runtime irrisolti. Se manca un elemento, lascia la consegna aperta o impostala su `Blocked`.

**Controllo del pacchetto:** contrassegna ciascuna delle cinque verifiche come Supported o Blocked: le revisioni delle fonti sono aggiornate, entrambi i responsabili hanno approvato la stessa revisione fissa, tutte le pubblicazioni richieste corrispondono alla rilettura, i limiti di runtime restano espliciti e lo stato di recupero è riconciliato. `Done` richiede cinque verifiche Supported e nessuna scrittura non autorizzata.

## Gestisci una scrittura dall'esito incerto

**Un timeout lascia incerto l'esito.** Non dimostra né il successo né il fallimento. Nel flusso di base del browser, riapri la fonte mappata e controllane il contenuto attuale e la cronologia prima di decidere se riprovare.

1. **Metti in pausa il passaggio successivo:** mantieni incompleta la consegna.
2. **Leggi la destinazione:** confronta il testo, la versione e l'ambito correnti con il pacchetto fisso.
3. **Registra l'osservazione:** completato, invariato, in conflitto o inaccessibile.
4. **Scegli l'azione successiva:** continua da un completamento verificato, ripeti un passaggio autorizzato e invariato oppure segnala un conflitto.
5. **Mantieni traccia dell'incertezza:** conserva il tentativo fallito o sconosciuto insieme alla rilettura successiva.

**Non ripetere alla cieca l'intera sequenza.** Ripetere un passaggio già completato crea revisioni aggiuntive e rischia di sovrascrivere modifiche indipendenti. Riprendi dallo stato verificato. Se la fonte non è accessibile, scegli `Hold` invece di basarti sul vecchio registro.

## Confronta le decisioni di recupero

| Situazione | Decisione da esaminare | Motivo |
|---|---|---|
| **Requisito modificato, integrazione negata** | Completare o compensare il requisito | Intento e comportamento differiscono |
| **Configurazione modificata, pubblicazione del runbook negata** | Completare il runbook o ripristinare la configurazione | Le istruzioni operative non sono aggiornate |
| **Un altro responsabile modifica l'ambito** | Tornare a `Review` | L'approvazione fissa descrive un altro contenuto |
| **Esito della scrittura incerto** | Leggere prima la destinazione | Il tentativo successivo dipende dallo stato osservato |
| **Il responsabile perde l'accesso** | Sospendere e richiedere un amministratore autorizzato | La vecchia autorizzazione non consente nuove scritture |

**Scegli in base allo stato attuale e alla decisione del responsabile.** Il completamento richiede approvazioni aggiornate e controlli praticabili. Una compensazione richiede la revisione del ripristino rispetto alle modifiche intervenute. Un'operazione di recupero è un'altra pubblicazione, non un'eccezione privilegiata alla procedura.

## Controlla il completamento della pubblicazione

**Consegna un pacchetto che un reviewer indipendente possa riconciliare.** Deve trovare la proposta esatta esaminata, le basi delle fonti, entrambe le revisioni di ruolo, ogni esito della scrittura, i valori finali e i limiti di runtime ancora presenti. Chiedigli di identificare il primo passaggio incompleto dopo un'interruzione.

**Ragionamento atteso:** l'azione successiva deriva dalle fonti aggiornate e dal registro, non dalla sicurezza mostrata dall'assistente precedente. Porta i riferimenti mappati finali nei test di recupero, dove la ricerca deve mantenere la stessa distinzione tra autorità.

## Risoluzione dei problemi e recupero

**Versione modificata:** confronta la cronologia e rinnova la revisione. **Il controllo dell'istantanea passa ma il wiki differisce:** recupera di nuovo le fonti Confluence correnti. **Jira è stato completato troppo presto:** riaprilo tramite il flusso autorizzato e registra i passaggi mancanti.

**Recupero:** confronta le cronologie delle pagine e usa un ripristino o una modifica compensativa approvati dal responsabile. Registra la versione risultante e non presumere che il ripristino azzeri la numerazione. Se Product sceglie il rollback, ripristina la configurazione tramite una PR protetta. I file eliminati non rientrano nella garanzia di rollback.

## Esercizio e autoverifica

**Interrompi dopo la pubblicazione di REQ-17** e consegna a un altro responsabile solo la mappa e il registro.

**Ragionamento atteso:** recupera le fonti aggiornate, conferma l'approvazione fissa e riprende solo il passaggio pendente autorizzato. Le prove mancanti riportano il lavoro a `Review`.

## Riferimenti principali

- **Cronologia e ripristino:** [documentazione tecnica di Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Operazioni API versionate:** [pagine Confluence REST API v2](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Controlli del flusso di lavoro:** [flussi di lavoro Jira avanzati](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Sicurezza delle integrazioni:** [best practice di sicurezza MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Prossimi passi

**Dopo una pubblicazione revisionata, continua con [Recupero basato su mappa](/articles/ai-collaboration-map-first-retrieval/).**
