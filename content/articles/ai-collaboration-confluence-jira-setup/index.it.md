---
title: "Configurazione AI di Confluence e Jira: autorizzazioni e autorità"
date: 2026-10-01
lastmod: 2026-11-12
toc: true
draft: false
description: "Configura le pagine di riferimento ufficiali in Confluence e le autorizzazioni di Jira gestite dall’azienda per una collaborazione tra team soggetta a revisione."
genre: ["Intelligenza artificiale", "Collaborazione di gruppo", "Ingegneria del software"]
tags: ["corso di collaborazione AI", "Confluence Cloud", "Jira Cloud", "pagine autorevoli", "schema autorizzazioni Jira", "transizione del workflow", "test di accesso"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustrazione di professionisti che revisionano il lavoro condiviso di un progetto in un ambiente di sicurezza informatica"
coverCaption: ""
---

[Torna al corso di collaborazione AI](/ai-collaboration-course-start/)

**L’amministratore definisce l’autorità sul posto di lavoro prima di collegare gli strumenti di chat.** I responsabili di prodotto e operazioni pubblicano requisiti e runbook in Confluence Cloud. Jira Cloud coordina la consegna. GitHub gestisce l’implementazione. Crea ambienti di test dedicati solo dopo aver preparato le basi, perché un’autorizzazione errata espone informazioni indipendentemente dal comportamento del modello.

## Punti chiave

- **Confluence** conserva la formulazione approvata dei requisiti.
- **Jira** gestisce lo stato di consegna, non la politica di conservazione.
- **GitHub** gestisce la configurazione e le politiche condivise.
- **I test di autorizzazione** richiedono piani adeguati e utenti separati.

## Prima di iniziare

**Prerequisiti:** le [fondamenta](/articles/ai-collaboration-pilot-foundation/), il repository del laboratorio, l’amministrazione degli spazi Confluence e di Jira, oltre a utenti separati con ruoli di collaboratore, responsabile e pubblicatore. **Tempo stimato:** da 90 a 120 minuti. **Difficoltà:** amministrazione avanzata.

**Requisiti del piano:** Confluence Free non supporta le restrizioni sui contenuti. Jira Free non offre schemi di autorizzazione configurabili, ruoli degli spazi o schemi di sicurezza per gli elementi di lavoro. Per questo percorso usa ambienti di test adeguati con piano Standard o superiore. Prima di eseguire i test, verifica piano e privilegi nelle fonti.

**Nota sulla navigazione:** la documentazione Jira attuale usa “space” e “work item”. Alcuni tenant mantengono “project” e “issue”. Scegli una configurazione gestita dall’azienda. Questa procedura non tratta i comportamenti delle autorizzazioni gestite dal team. Non servono Rovo, app del marketplace, approvazioni di Jira Service Management o connettori di chat a pagamento.

**Risultato:** prepara una matrice delle autorizzazioni, pagine di riferimento ufficiali nominate, un workflow Jira riservato al laboratorio e prove di accesso negato da utenti separati. Registra il piano del tenant e le ipotesi sui ruoli accanto ai risultati dei test.

**Controlli preliminari prima di creare record:**

| Controllo | Se disponibile | Se non disponibile |
|---|---|---|
| Restrizioni delle pagine e amministrazione dello spazio Confluence | Crea pagine separate approvate ed escluse | Segna come Bloccati i test di modifica della pagina e di lettura negata |
| Schema autorizzazioni e editor del workflow di Jira gestito dall’azienda | Copia uno schema e un workflow riservati al laboratorio | Segna come Bloccati i test delle transizioni |
| Utenti separati per collaboratore, responsabile, pubblicatore e utente escluso | Esegui test positivi e negativi specifici per ruolo | Segna come Bloccati i ruoli non testati |
| Manutentore del repository e branch protetto | Collega il percorso di implementazione revisionato | Completa prima il percorso GitHub-first, poi passa alla pubblicazione mista |

A ottobre 2026, usa il controllo **Share** o delle restrizioni per gestire l’accesso alla pagina, l’area delle autorizzazioni **Space settings** in Confluence per concessioni più ampie e **Settings > Work items > Permission schemes** in Jira per lo schema del laboratorio. L’editor del workflow di Jira gestito dall’azienda controlla le transizioni. Le etichette dell’interfaccia e le funzioni del piano variano tra tenant. Prima di seguire questi passaggi, registra nei tuoi dati di prova il percorso effettivo e il piano. Consulta le [autorizzazioni a livello di pagina in Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) e gli [schemi di autorizzazione Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Crea le pagine autorevoli

1. **Crea uno spazio Confluence** chiamato **`Export Service Lab`**. Disattiva l’accesso anonimo e la condivisione pubblica tramite i controlli disponibili per sito e spazio.
2. **Crea pagine pubblicate**, non documenti live, chiamate **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** e **`Decision Register`**.
3. Come responsabile di prodotto, **pubblica il requisito iniziale** riportato sotto. Registra l’ID e la versione effettivi della pagina nella mappa del repository.
4. Come responsabile delle operazioni, **pubblica RUN-04** con conservazione di sette giorni e con l’indicazione che in questo laboratorio non viene eseguito alcun processo di eliminazione.
5. Su ogni pagina autorevole, **apri Share**. Imposta l’accesso generale in sola lettura per i membri dello spazio idonei e assegna autorizzazioni di modifica specifiche ai responsabili e ai pubblicatori designati. Salva e verifica con l’utente collaboratore.

```text
ID sorgente: REQ-17
Ruolo responsabile: product-owner
Stato: riferimento approvato
Ambito: solo file di esportazione sintetici
Conservazione: 7 giorni
Stato di consegna: configurazione di base del laboratorio
Eccezioni: esclusi i dati di produzione, i backup e gli obblighi di conservazione legale
Prova di approvazione: revisione della baseline DEC-12
Riferimento di implementazione: allegare il commit di base protetto su GitHub
```

**Applica restrizioni a ogni pagina autorevole.** Non presumere che la restrizione di modifica di una pagina padre protegga anche le figlie. L’ereditarietà di lettura e modifica funziona in modo diverso e restano valide anche le autorizzazioni dello spazio. Un collegamento da solo non concede accesso. Controlla tutte le appartenenze se un utente che dovrebbe avere solo lettura riesce ancora a modificare.

**Usa questi testi iniziali per le altre due pagine.** Prima di approvare un record, sostituisci i campi di revisione segnaposto con prove reali dell’ambiente di test.

```text
ID sorgente: RUN-04
Ruolo responsabile: operations-owner
Stato: riferimento approvato
Ambito: solo file di esportazione sintetici
Conservazione configurata: 7 giorni
Procedura: confrontare REQ-17 con config.json prima di una modifica soggetta a revisione
Limite di esecuzione: questo laboratorio non ha un processo di eliminazione e non produce prove di eliminazione
Ripristino: ripristinare la configurazione approvata precedente dopo la revisione
Limite del ripristino: ripristinare la configurazione non recupera i file eliminati
Prova della revisione: aggiungere il revisore effettivo, la versione della pagina e il riferimento alla decisione
```

```text
Pagina: Registro delle decisioni
ID voce: DEC-12
Decisione: usare sette giorni come baseline sintetica
Ambito: solo export-service-lab
Requisito: registrare la versione della pagina REQ-17 dopo la pubblicazione
Runbook: registrare la versione della pagina RUN-04 dopo la pubblicazione
Policy: registrare la revisione protetta GitHub di POL-01 dopo la revisione
Revisione prodotto: in attesa finché il responsabile indicato non registra una decisione
Revisione operativa: in attesa finché il responsabile indicato non registra una decisione
Stato: esempio di bozza, sostituire con prove di revisione osservate
```

## Aggiorna la mappa

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Aggiungi alla mappa le posizioni private effettive dell’ambiente di test e gli ID delle pagine.** Il modello indica le fonti autorevoli senza fingere di contenere indirizzi reali. Rimuovi dal README il testo che assegna al file JSON copiato l’autorità sui requisiti del percorso misto.

**Mantieni POL-01 in GitHub** per entrambi i percorsi. Confluence rimanda alla revisione verificata. Spostare l’autorità della politica durante un’attività richiede un altro passaggio di autorità soggetto a revisione.

## Imposta le autorizzazioni Jira

1. **Crea uno spazio di laboratorio gestito dall’azienda** e copia uno schema di autorizzazione in uno schema dedicato al laboratorio. Non modificare uno schema di produzione condiviso.
2. **Apri Settings, Work items, Permission Schemes**, seleziona lo schema del laboratorio e aggiorna le concessioni.
3. **Concedi ai collaboratori i permessi di consultazione, creazione e commento.** Limita i privilegi amministrativi. Verifica esplicitamente i permessi di modifica e **Transition work items**.
4. **Associa lo schema** allo spazio del laboratorio e verifica che nessuno spazio di produzione lo condivida.
5. **Crea PROP-042** come elemento di lavoro. Registra nella mappa la chiave generata e mantieni PROP-042 come ID logico della proposta nella descrizione.

**Incolla questa bozza in PROP-042.** L’elemento Jira tiene traccia della consegna. Il testo non sostituisce la formulazione approvata in Confluence.

```text
ID proposta: PROP-042
Stato: Bozza
Valore attualmente approvato: 7 giorni, da registrare la versione della pagina REQ-17
Valore proposto: 30 giorni per i file di esportazione sintetici
Esclusioni: dati di produzione, backup e obblighi di conservazione legale
Record interessati: REQ-17, RUN-04, config.json, proposal.json
Allegato fisso della proposta: in attesa
Revisione del responsabile prodotto: in attesa
Revisione del responsabile operativo: in attesa
Registro di pubblicazione: in attesa
Interrompere se cambia la versione della fonte, manca la revisione o l’accesso viene negato
```

| Ruolo | Confluence | Jira | GitHub |
|---|---|---|---|
| **Collaboratore** | Legge le pagine approvate | Crea e commenta le bozze | Branch della proposta o Issue |
| **Responsabile di prodotto** | Revisiona il requisito | Registra la revisione del requisito | Revisiona le prove della PR |
| **Responsabile delle operazioni** | Revisiona il runbook | Registra la revisione operativa | Revisiona l’impatto operativo |
| **Pubblicatore** | Modifica le pagine approvate | Registra lo stato di pubblicazione | Nessuna autorità automatica di merge |
| **Manutentore** | Legge il requisito | Registra l’implementazione | Revisiona e integra la PR protetta |

**Le autorizzazioni assegnate tramite gruppi diversi si sommano.** Rimuovi dal laboratorio le concessioni ampie non volute, invece di presumere che una concessione più limitata le sovrascriva. Non inserire le identità dei connettori nei gruppi amministrativi.

## Imposta gli stati di consegna

**Copia un workflow gestito dall’azienda** in un workflow riservato al laboratorio. Aggiungi gli stati Bozza, Revisione, Approvato, Pubblicazione, Completato e Bloccato. Aggiungi le transizioni di invio, approvazione, pubblicazione, completamento, blocco e ritorno alla revisione. Associalo solo al tipo di lavoro del laboratorio.

1. Nell’editor del workflow, **seleziona la transizione verso Approvato**.
2. **Aggiungi una condizione o restrizione** che consenta l’attivazione solo al ruolo o al gruppo designato di responsabili/pubblicatori. Usa i controlli documentati e pubblica la bozza del workflow come amministratore.
3. **Verifica manualmente entrambe le revisioni dei responsabili** prima della transizione. Ciascuna revisione identifica la proposta congelata e le versioni delle fonti.
4. **Limita Completato** al ruolo responsabile della consegna. Rimuovi le transizioni alternative o globali che aggirano il limite.

**Una transizione limitata non equivale all’approvazione di due persone.** Controlla chi esegue la transizione. In questo progetto pilota, la verifica delle prove dei due ruoli resta procedurale. Registra esplicitamente questo limite.

**Esempio di record di transizione:** per **Revisione ad Approvato**, consenti l’attivazione solo al gruppo designato di responsabili/pubblicatori. Prima di attivarla, chi esegue la transizione apre l’allegato fisso PROP-042 e verifica le decisioni del responsabile di prodotto e di quello operativo sulla stessa revisione della proposta. Se manca una decisione o si riferisce a una revisione precedente, lascia l’elemento in Revisione e registra la lacuna. La restrizione del workflow controlla chi esegue la transizione. La verifica delle prove è un passaggio umano separato.

## Verifica la negazione dell’accesso

**Come collaboratore**, leggi REQ-17, prova a modificarlo, crea la bozza Jira e tenta la transizione ad Approvato. I risultati attesi sono requisito leggibile, modifica negata, creazione della proposta riuscita e approvazione negata. Confronta le versioni della fonte prima e dopo il diniego.

**Come utente escluso**, apri una pagina sintetica con restrizioni separate. L’accesso ai contenuti deve essere negato. Verifica indipendentemente le pagine figlie. Non copiare il testo protetto nella chat dell’utente escluso per aggirare il controllo.

## Adatta la mappa del repository

**Mantieni stabili gli ID delle fonti quando cambia la loro posizione.** REQ-17 indica ancora l’intento approvato di conservazione, ma nel percorso misto la sua sede è una pagina Confluence. Una copia nel repository supporta i controlli e la revisione. Non sostituisce la pagina autorevole.

| Record | Sede autorevole | Trattamento nel repository |
|---|---|---|
| **REQ-17** | Pagina dei requisiti Confluence indicata nella mappa | Copia acquisita con prova della revisione della pagina |
| **RUN-04** | Pagina del runbook Confluence indicata nella mappa | Estratto operativo acquisito per coerenza |
| **POL-01** | Politica protetta in GitHub | Le istruzioni condivise degli agenti vi fanno riferimento |
| **Configurazione** | Record protetto in GitHub | Differenza di implementazione proposta |
| **Consegna** | Elemento di lavoro Jira | Collegamento di correlazione, non copia della politica |

**Aggiungi la provenienza alle copie.** Nel pacchetto privato della proposta registra l’ID della fonte, il riferimento alla pagina, la versione, l’ora di acquisizione e il ruolo di chi ha acquisito i dati. Non includere gli identificatori nativi delle pagine negli elaborati pubblici del corso. Se il pubblicatore trova una versione attuale diversa, risolvi la differenza prima di usare la copia.

**Non rinominare l’autorità per adattarla allo strumento.** La descrizione modificabile di Jira è utile per discutere, ma resta un record di consegna. Una frase di trenta giorni in Jira non sostituisce un requisito di sette giorni in Confluence.

## Progetta i test di accesso

**Separa lettura, bozza e pubblicazione.** Un collaboratore deve poter comprendere il requisito sintetico e inviare una proposta. Non gli servono i permessi di modifica sulla pagina autorevole né il permesso di approvare la propria proposta.

```text
Record di test: PERM-REQ-EDIT
Ruolo: collaboratore
Fonte: REQ-17
Prerequisito: la fonte è leggibile e la revisione pubblicata è stata acquisita
Tentativo: modificare il requisito autorevole
Risultato previsto: modifica negata, revisione pubblicata invariata
Risultato osservato: compilare dalla sandbox
Prova: risultato nativo e rilettura indipendente della revisione
Revisore: amministratore o revisore indipendente delle autorizzazioni
```

**Usa un record separato per testare la lettura negata.** Il requisito leggibile dal collaboratore verifica la separazione tra pubblicazione e modifica. La pagina inaccessibile per l’utente escluso verifica la riservatezza. Riunire i due casi in un’unica riga nasconde quale limite è stato testato.

**Verifica anche gli accessi consentiti.** I responsabili e i pubblicatori devono poter usare il percorso assegnato. Se tutti gli utenti ricevono un diniego, l’ambiente di test è restrittivo ma inutilizzabile. Conserva una modifica autorizzata riuscita su una pagina di prova usa e getta senza alterare il requisito approvato durante la diagnosi delle autorizzazioni.

## Prova la revisione Jira

**Considera i nomi degli stati il progetto di questo pilota.** Bozza contiene una richiesta. Revisione contiene un pacchetto congelato. Approvato indica che i responsabili hanno completato la revisione. Pubblicazione indica una consegna ancora in corso. Completato richiede una rilettura. Bloccato indica prove o accesso mancanti, oppure un conflitto irrisolto.

| Transizione | Pacchetto richiesto | Controllo responsabile |
|---|---|---|
| **Bozza a Revisione** | Proposta fissa e versioni delle fonti | Il collaboratore conferma la completezza |
| **Revisione ad Approvato** | Decisioni del responsabile di prodotto e di quello operativo | L’attore autorizzato verifica entrambi i ruoli |
| **Approvato a Pubblicazione** | Confronto con le fonti attuali | Il pubblicatore conferma che le basi non sono cambiate |
| **Pubblicazione a Completato** | Registro completato per ogni sistema | Il responsabile della consegna verifica la rilettura |
| **Qualsiasi passaggio supportato a Bloccato** | Errore e azione in sospeso | Responsabile del ripristino assegnato |

**Prova con un pacchetto sintetico incompleto.** Invia solo la revisione del prodotto e chiedi all’attore autorizzato di valutare la transizione. Il comportamento atteso è lasciare il lavoro in Revisione e richiedere la revisione operativa. Questo verifica il passaggio procedurale separatamente dal diniego sulla piattaforma per il collaboratore.

**Verifica deliberatamente i percorsi alternativi.** Nella vista workflow dell’ambiente di test controlla ogni percorso verso Approvato e Completato. Una transizione nominata e limitata non basta se un’altra via disponibile salta lo stesso controllo. Registra i percorsi ispezionati e l’utente usato, invece di dichiarare una copertura completa dopo un solo clic.

## Diagnostica gli accessi imprevisti

**Parti dall’identità effettiva.** Verifica che la sessione del browser appartenga al ruolo di test previsto. Poi controlla appartenenza ai gruppi, autorizzazioni dello spazio, accesso alle pagine e associazione del workflow con gli strumenti amministrativi del prodotto. Non modificare più controlli insieme, perché così il diniego perde valore diagnostico.

1. **Conferma l’identità:** usa sessioni separate per collaboratore, pubblicatore e utente escluso.
2. **Individua la concessione:** trova l’appartenenza o l’impostazione che consente l’azione tentata.
3. **Modifica il controllo del laboratorio:** conserva il legittimo accesso dei responsabili.
4. **Ripeti lo stesso tentativo:** dopo il diniego acquisisci la versione invariata della fonte.
5. **Ripeti il caso positivo:** conferma che la pubblicazione autorizzata funzioni ancora.

**Elenco finale delle prove:** registra l’albero delle pagine Confluence e i relativi ID, l’associazione dello schema Jira del laboratorio, l’associazione del workflow, l’appartenenza ai gruppi di ogni ruolo di test, una lettura consentita del requisito, una modifica negata con versione invariata, la creazione consentita di una bozza, una transizione ad Approvato negata con stato invariato, la lettura negata all’utente escluso e il responsabile della pulizia. Per ogni riga conserva il ruolo dell’attore, la versione o lo stato iniziale e finale, il risultato nativo e il revisore indipendente. Registra il percorso di navigazione osservato nel tenant, perché etichette e controlli disponibili variano in base al piano.

**Verifica del completamento:** consegna le pagine autorevoli mappate, il workflow riservato al laboratorio, la matrice dei ruoli prevista e i record delle autorizzazioni osservati. Se il piano non include un controllo richiesto, lascia la relativa riga in stato Bloccato. La lezione sulla pubblicazione presuppone che i test siano riusciti, non la sola esistenza di schermate delle impostazioni.

## Risoluzione dei problemi e rollback

**Il collaboratore riesce ancora a modificare:** controlla accesso alla pagina, autorizzazioni dello spazio e appartenenze. **La transizione riesce ancora:** controlla l’associazione del workflow e i percorsi di bypass. **Mancano impostazioni:** verifica la configurazione gestita dall’azienda, l’edizione e i privilegi amministrativi.

**Rollback:** rimuovi le autorizzazioni dei connettori e archivia le bozze. Scollega schemi e workflow riservati al laboratorio dopo aver conservato le prove. Ripristina la formulazione approvata della pagina tramite la cronologia revisionata o una modifica correttiva. Non eliminare le prove di audit.

## Esercizio e autoverifica

**Jira indica trenta giorni, mentre REQ-17 ne indica sette.** Identifica l’input dell’implementazione e il responsabile della riconciliazione.

**Ragionamento atteso:** Confluence definisce l’intento. Jira contiene un errore di proposta o di consegna. Interrompi la pubblicazione e chiedi al responsabile di prodotto di riconciliare i dati, invece di scegliere il timestamp più recente.

## Riferimenti principali

- **Restrizioni e piano:** [autorizzazioni Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controlli di condivisione:** [accesso a contenuti specifici](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Amministrazione degli schemi:** [schemi di autorizzazione Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Condizioni delle transizioni:** [workflow avanzati](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Passaggi successivi

**Dopo aver superato i test di accesso, continua con [Pubblicazione tra sistemi](/articles/ai-collaboration-confluence-jira-publication/)**.
