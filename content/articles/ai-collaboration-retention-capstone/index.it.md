---
title: "Capstone sulla collaborazione con l'IA: GitHub, Confluence e Jira"
date: 2026-10-01
lastmod: 2026-11-13
toc: true
draft: false
description: "Consegna una modifica sintetica della conservazione tramite workflow GitHub-first e Confluence/Jira, con prove di errore e revisione indipendente."
genre: ["Intelligenza artificiale", "Collaborazione di gruppo", "Ingegneria del software"]
tags: ["corso di collaborazione IA", "proposta di conservazione", "revisione GitHub", "workflow Confluence Jira", "matrice degli errori", "accettazione indipendente"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustrazione di professionisti che revisionano un progetto condiviso in un ambiente di lavoro per la cybersicurezza"
coverCaption: ""
---

[Torna al corso sulla collaborazione con l'IA](/ai-collaboration-course-start/)

**Consegna PROP-042 due volte**, prima con GitHub-first e poi con GitHub, Confluence e Jira. Tu contribuisci, proprietari separati revisionano e i pubblicatori autorizzati applicano la modifica. Usa sandbox sintetiche isolate dopo le lezioni precedenti. Il capstone verifica l'intera procedura, inclusi rifiuto, recupero e passaggio indipendente, non la qualità della prosa dell'assistente.

## Punti chiave

- **Una modifica condivisa** confronta entrambi i modelli di autorità.
- **I test negativi** contano quanto una consegna riuscita.
- **I pacchetti di prove** sostengono la revisione indipendente.
- **La conclusione del laboratorio** non autorizza il rilascio in produzione.

## Prima di iniziare

**Prerequisiti:** [moduli precedenti del corso](/ai-collaboration-course-start/), accesso approvato alla sandbox e revisori separati. **Tempo di pianificazione:** da otto a dodici ore in più sessioni, oltre alla revisione indipendente. Il tempo reale dipende dalla configurazione degli account e dalle riparazioni. **Difficoltà:** avanzata.

**Artefatti richiesti:** statuto, mappa, policy, adattatori, baseline, manifest, proposta corretta, revisioni dei proprietari, registro, record di recupero e passaggio. Le autorizzazioni dipendenti dal piano mancanti bloccano il completamento e non diventano approvazioni presunte.

**Prepara una directory di prove per ogni percorso prima dei test.** Un revisore deve riconoscere attore, revisioni sorgente, azione tentata, risultato osservato e stato finale senza affidarsi al riepilogo di una chat.

## Stabilire due baseline

1. **Crea esecuzioni isolate** chiamate GitHub-first e Mixed. Mantieni separate revisioni e revisioni dei proprietari.
2. **Ripristina la baseline di sette giorni** con la procedura approvata di ogni percorso e registra le revisioni risultanti.
3. **Verifica i controlli di diniego** con account di contributore e di utente escluso.
4. **Cattura il contesto corrente** e conferma l'accordo tra adattatore e policy.
5. **Dichiara l'ambito:** conservazione sintetica dell'export per trenta giorni, esclusi dati reali, backup e conservazioni legali.

**PROP-042 è un'etichetta di correlazione, non un'approvazione riutilizzabile.** Ogni esecuzione richiede una propria revisione congelata e prove sorgente. Inserisci gli ID di esecuzione nei report.

## Consegnare con GitHub-first

**Apri l'Issue e la PR candidata** usando le lezioni GitHub. Modifica insieme requisito, configurazione, proposta e runbook. Cattura la base protetta, esegui controlli affidabili e ottieni le revisioni prodotto e operations sul commit finale.

```text
Esecuzione: GitHub-first
Modifica: conservazione sintetica 7 -> 30 giorni
Requisito: REQ-17 revisione 2
Configurazione: retention_days 30
Runbook: periodo di conservazione: 30 giorni
Proposta: revisione base 1, da 7, a 30
Manifesto: hash delle fonti protette prima della modifica
Revisione: revisione di prodotto e operations sulla versione finale della proposta
Pubblicazione: commit unito e nuova lettura di verifica
Limite: nessun servizio di eliminazione in esecuzione è stato testato
```

**Inserisci i riferimenti reali dalla sandbox.** Lo schema descrive la mappatura attesa, non prove completate. Il maintainer fa il merge solo dopo la revisione, poi legge indipendentemente **`main`**. Chiudi l'Issue dopo aver collegato i record finali.

## Consegnare il percorso Mixed

**Leggi le versioni Confluence e congela la proposta Jira.** Ottieni entrambe le revisioni dei proprietari. Pubblica il requisito con la consegna in sospeso, fai il merge della configurazione, pubblica il runbook e rileggi tutti i sistemi prima di Done.

**Registra ogni pubblicazione** con versione della pagina, commit o prova della transizione. Le copie dei requisiti nel repository restano snapshot. Il checker locale non stabilisce l'autorità corrente di Confluence.

| Confronto | GitHub-first | Ambiente di lavoro misto |
|---|---|---|
| **Requisito** | Revisione del repository protetto | Pubblicazione revisionata dal proprietario Confluence |
| **Coordinamento** | Issue/PR | Proposta Jira congelata |
| **Unità di pubblicazione** | Merge del repository | Scritture di pagina separate e merge |
| **Aggiornamento** | Commit protetto | Versioni di pagina più commit |
| **Recupero** | Revert o compensazione revisionati | Compensazione guidata dal registro |

**Scegli il workflow in base alle esigenze di proprietà.** GitHub-first riduce il coordinamento tra sistemi. Il percorso Mixed conserva le sedi di lavoro e aggiunge controlli di pubblicazione e accesso.

## Eseguire la matrice degli errori

| Caso | Iniezione | Prova osservata richiesta |
|---|---|---|
| **Modifica approvata** | Invia una proposta revisionata di trenta giorni | Read-back coerente e revisione |
| **Contesto obsoleto** | Cambia la sorgente dopo la cattura | Rifiuto, riconciliazione, nuova approvazione |
| **Scrittura non autorizzata** | Il contributore pubblica | Diniego e revisione invariata |
| **Conflitto** | Jira dice sessanta, Confluence sette | Blocco e riconciliazione del proprietario |
| **Pubblicazione parziale** | Interrompi dopo una scrittura | Registro in sospeso e recupero |
| **Diniego di accesso** | Rimuovi l'accesso in lettura al task | Nessun testo protetto o pubblicazione |
| **Recupero** | Completamento o backout approvato | Nuove revisioni esaminate |
| **Passaggio** | Una nuova sessione riceve solo mappa e registro | Nuova lettura e prossima azione corretta |

**Il conflitto tra sistemi appartiene a Mixed.** In GitHub-first, prova una descrizione dell'Issue in conflitto con il file approvato. Esegui gli altri casi applicabili in entrambi i percorsi. Un errore del validatore locale non sostituisce una prova live delle autorizzazioni.

| Caso e file di prova | Esecuzione GitHub-first | Esecuzione Mixed |
|---|---|---|
| **Modifica approvata** `01-approved-change.md` | PR revisionata e read-back | Pagine revisionate, merge e registro |
| **Contesto obsoleto** `02-stale-context.md` | Cambia la base protetta dopo la cattura | Cambia una pagina autoritativa dopo la cattura |
| **Scrittura non autorizzata** `03-unauthorized-write.md` | Diniego del direct push del contributore | Diniego di modifica pagina e transizione |
| **Conflitto** `04-conflict.md` | L'Issue non concorda con il file approvato | Il testo Jira non concorda con Confluence |
| **Pubblicazione parziale** `05-partial-publication.md` | Fermati prima del merge o read-back | Fermati dopo una scrittura di pagina |
| **Diniego di accesso** `06-access-denial.md` | Nega una sorgente protetta del repository | Escludi un utente da una pagina riservata |
| **Recupero** `07-recovery.md` | Revert o completamento revisionato | Compensazione guidata dal registro |
| **Passaggio** `08-handoff.md` | Una nuova sessione legge i file protetti | Una nuova sessione legge pagine e registro mappati |

**Crea ogni file prima del test.** Registra risultato atteso, risultato osservato, ruolo dell'attore, revisioni iniziale e finale, riferimento della prova nativa e decisione del revisore. Un prompt di percorso del browser non dimostra il diniego del direct push. Mantieni separate le due directory dei percorsi.

**Tieni separati risultati attesi e osservati.** Per ogni caso registra ID di esecuzione, ruolo, revisioni iniziali, azione tentata, aspettativa, osservazione, revisioni risultanti e decisione del revisore. Redigi credenziali e identificatori degli account nei report condivisi.

## Valutare il completamento

**Il superamento richiede prove osservate per ogni riga applicabile** e accettazione indipendente. I revisori controllano permessi, freschezza delle sorgenti, revisione dei ruoli, pubblicazione parziale, ricostruzione del passaggio e log di coerenza.

**Fallisci immediatamente** per pubblicazione non autorizzata, testo negato arrivato al modello o sovrascrittura silenziosa di una base cambiata. Mantieni il lavoro bloccato finché i controlli corretti non superano un nuovo test. Non trasformare questi errori in una media favorevole.

**Misura casi completati e bloccati, proposte obsolete rifiutate, scritture negate, recuperi e tempo dei revisori.** I risultati proposti restano attesi finché non vengono osservati. I dieci unit test forniti coprono la coerenza, non la sicurezza live del tenant.

## Pianificare le due esecuzioni

**Non riutilizzare un'approvazione tra i percorsi.** Il valore richiesto è uguale, ma sedi sorgente, revisioni catturate, permessi e sequenza di pubblicazione differiscono. Ogni esecuzione deve avere directory di prove e pacchetto di revisione propri.

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    stesse categorie di prove, raccolte in modo indipendente
```

**Questi nomi sono un esempio organizzativo**, non file di archivio forniti. Conserva le prove reali in privato nella sandbox approvata. Le consegne condivise devono usare ruoli e riferimenti redatti, mentre i revisori mantengono l'accesso ai record nativi.

**Assegna un osservatore dei test prima degli errori.** Il contributore esegue l'azione tentata. L'osservatore registra stato iniziale, esito e stato risultante. Un revisore decide poi se le prove sostengono l'affermazione. Dichiara sovrapposizioni di ruolo invece di suggerire accettazione indipendente.

## Eseguire gli errori in isolamento

**Ripristina uno stato verificato e revisionato tra i casi.** Iniettare insieme deriva della sorgente, revoca dell'accesso e incompatibilità del runbook nasconde quale controllo ha respinto la proposta. Un errore per esecuzione offre al revisore una ragione tracciabile.

1. **Cattura lo stato iniziale:** revisioni sorgente, configurazione, stato della consegna e ruolo dell'attore.
2. **Applica un'iniezione sintetica:** cambia una condizione rilevante tramite un percorso di test autorizzato.
3. **Tenta l'azione delimitata:** validazione, lettura, pubblicazione o passaggio.
4. **Registra l'osservazione:** output reale e stato sorgente risultante.
5. **Ripara tramite revisione:** conserva le prove dell'errore prima di ripristinare i controlli.
6. **Ripeti il caso positivo:** conferma che il workflow corretto consegni ancora il lavoro consentito.

**Scheda di iniezione e ripristino per ogni caso:** prima del caso successivo, usa una nuova proposta sintetica o ripristina una base revisionata. La persona osservatrice registra la precondizione e conferma il ripristino. Non eliminare mai il tentativo fallito dal ledger.

| Caso | Iniezione e verifica: GitHub-first | Iniezione e verifica: Mixed | Ripristino prima del caso successivo |
|---|---|---|---|
| Modifica approvata | Invia la PR fissata, ottieni entrambe le revisioni, uniscila e riapri `main` | Pubblica REQ-17, unisci il diff revisionato, pubblica RUN-04 e rileggi i record | Registra le revisioni finali come nuova base |
| Contesto obsoleto | Acquisisci un manifest, poi modifica la base di test con una PR separata e revisionata prima di convalidare la vecchia proposta | Acquisisci le versioni delle pagine e fai modificare una pagina di test da un editor autorizzato prima della lettura pre-scrittura | Fermati, confronta le versioni, acquisisci nuove fonti e fai revisionare un nuovo pacchetto |
| Scrittura non autorizzata | Contributor tenta un push diretto innocuo su `main` protetto e registra il rifiuto del server | Contributor tenta di modificare REQ-17 e di attivare Approved | Rileggi commit, versione della pagina e stato Jira per confermare che non siano cambiati |
| Conflitto | La bozza dell’Issue indica sessanta giorni, il file approvato sette | La bozza Jira indica sessanta giorni, REQ-17 sette | Il responsabile prodotto concilia la bozza e registra la decisione |
| Pubblicazione parziale | Fermati dopo l’approvazione e prima del merge o della rilettura, lasciando aperto l’Issue | Fermati dopo la rilettura di REQ-17 mentre configurazione e RUN-04 indicano ancora sette | Lascia la consegna in sospeso e ottieni una decisione revisionata per completare o compensare |
| Accesso negato | Un’identità di test esclusa tenta di leggere una fonte sintetica in un repository di test privato | L’identità esclusa tenta di accedere a una pagina sintetica riservata | Ripristina solo l’accesso di test approvato e verifica che il lettore normale riesca ancora |
| Ripristino | Interrompi una modifica di test approvata e proponi il completamento o il revert dopo una revisione | Usa il ledger della pubblicazione parziale per proporre il completamento o una compensazione revisionata | Rileggi ogni fonte e confrontala con il ledger |
| Passaggio di consegne | Invia MAP-01 e il ledger a un nuovo revisore senza la vecchia chat | Invia gli ID delle pagine mappate e il ledger a un nuovo revisore senza la vecchia chat | Il revisore apre le fonti attuali e registra la prossima azione autorizzata |

Per ogni caso negato, registra la risposta della piattaforma e rileggi il record protetto. Per il caso dell’utente escluso, consulta le tracce degli strumenti, i log di recupero o gli audit del provider per verificare se il testo protetto è arrivato al task. Senza queste prove, indica come Bloccato il controllo di sicurezza degli accessi: un rifiuto visibile non dimostra che non sia stato restituito un estratto in cache. Se il piano non include il controllo o manca un’identità di test approvata, registra Bloccato invece di simulare un esito positivo.



**Un errore pianificato resta un'osservazione di errore.** Non chiamare riuscito un test di pubblicazione non autorizzata solo perché volevi sondare il controllo. Il test ha esposto un difetto, ma il confine di pubblicazione ha fallito e richiede una riparazione.

## Interpretare un risultato misto

**Pacchetto di prove illustrativo:** i controlli locali di coerenza superano il test, prodotto e operations revisionano il pacchetto corretto, la pubblicazione del requisito riesce e l'accesso di modifica del runbook viene negato. La configurazione non è ancora stata unita. Jira resta Bloccato.

| Affermazione | Verdetto | Motivo |
|---|---|---|
| **I record candidati concordano** | Supportato dal controllo locale | I record forniti hanno superato i confronti |
| **I proprietari hanno accettato intento e operations** | Richiede revisioni native congelate | Le sole etichette dei ruoli non bastano |
| **La consegna di trenta giorni è completata** | Non supportato | Le pubblicazioni richieste restano in sospeso |
| **Il confine dei permessi funziona per ogni ruolo** | Non supportato | Un'azione negata ha portata limitata |
| **Il responsabile del recupero deve agire** | Supportato come prossimo passo | Una consegna parziale richiede una decisione revisionata |

**Ragionamento atteso:** mantieni l'esecuzione incompleta, verifica le sorgenti correnti e chiedi la decisione del proprietario appropriato. Non concludere indebolendo i permessi o descrivendo il controllo dello snapshot come prova di pubblicazione live.

**Pacchetto didattico Mixed, sintetico e non riferito a un tenant:**

```text
Esecuzione: MIXED-042-example
Base acquisita: REQ-17 v4 = 7 giorni; RUN-04 v2 = 7 giorni.
GitHub main base-001 config.json = {"retention_days": 7}; Jira PROP-042 r1 = In Review.
Proposta fissata: REQ-17 v5 stabilisce 30 giorni per le esportazioni sintetiche. Esclude dati di produzione, backup e obblighi di conservazione legale.
GitHub config.json porta retention_days da 7 a 30. RUN-04 v3 indica 30 giorni; nel laboratorio non opera alcun servizio di eliminazione. La pubblicazione incompleta resta in sospeso.
Revisione: il responsabile di prodotto approva il testo esatto di REQ-17. Operations approva il diff di configurazione e il runbook a r1.
Pubblicazione: il publisher rilegge REQ-17 v5 e RUN-04 v3, entrambi a 30 giorni; il maintainer rilegge main a merge-002 con retention_days 30.
Azione negata: il contributor non può modificare REQ-17 v5. Il publisher conferma che è invariato e l’osservatore salva la prova nativa.
Ripristino: un tentativo RUN-04 fallisce e Jira resta Blocked. Operations autorizza un nuovo tentativo; dopo aver riletto v3, Jira passa a Done.
Passaggio: un nuovo revisore riceve MAP-01 e il registro, rilegge le tre fonti e Jira e segnala i 30 giorni e la lacuna di esecuzione.
Limite: è dimostrata solo la pubblicazione delle fonti. Tempo di eliminazione: non eseguito.
```

## Revisione con un lettore indipendente

**Chiedi al revisore di ricostruire gli eventi**, non di leggere soltanto la conclusione. Deve trovare baseline approvata, proposta corretta, decisioni dei proprietari, revisioni risultanti, tentativi falliti, riparazione e lacune senza la tua narrazione.

```text
Domande per la revisione indipendente:
Quale fonte governa l’intento di conservazione in questo flusso?
Quale pacchetto esatto ha esaminato ciascun responsabile?
Una fonte è cambiata dopo la revisione?
Che cosa è stato pubblicato e che cosa resta in sospeso?
Quale azione negata è stata osservata e con quale ruolo?
Il testo protetto è arrivato al contesto di un utente escluso?
Quale correzione è stata revisionata e riletta?
Il nuovo passaggio ricostruisce in autonomia lo stato corrente?
```

**Valuta ogni requisito separatamente.** Usa Supported, Failed, Blocked o Not run con un riferimento alla prova. Coerenza, approvazione, permessi, recupero e passaggio sono requisiti distinti. Molti test locali verdi non compensano un confine di pubblicazione live fallito.

```text
ID e flusso:
Ruolo e data della revisione:
Caso 01 modifica approvata: stato ___ prova ___ lacuna ___
Caso 02 contesto obsoleto: stato ___ prova ___ lacuna ___
Caso 03 scrittura non autorizzata: stato ___ prova ___ lacuna ___
Caso 04 conflitto: stato ___ prova ___ lacuna ___
Caso 05 pubblicazione parziale: stato ___ prova ___ lacuna ___
Caso 06 accesso negato: stato ___ prova ___ lacuna ___
Caso 07 ripristino: stato ___ prova ___ lacuna ___
Caso 08 passaggio: stato ___ prova ___ lacuna ___
Decisione complessiva: Supportata / Fallita / Bloccata / Non eseguita
Prossimo ruolo responsabile e azione:
```

**Supported significa che il revisore ha trovato prove osservate per ogni caso applicabile.** Registra Failed per un controllo fallito osservato, Blocked per accesso o controllo mancante e Not run per un caso non tentato. Conserva ogni riferimento nativo nel file di prova nominato.

**Criterio di superamento del corso:** completa entrambi i percorsi GitHub-first e Mixed. In ciascun percorso, tutti gli otto casi applicabili devono essere Supported. Un confine Failed o un read-back nativo mancante blocca il percorso. Un piano a pagamento o un'identità di test mancante produce Blocked, non un superamento ipotizzato. Un percorso completato produce un risultato parziale documentato, non il completamento del corso.

**Pacchetto modello redatto, solo illustrativo:**

```text
Flusso: github-first | Esecuzione: G-01 | Revisore: ruolo pilota indipendente
Base: commit protetto base-001 | Proposta fissata: PROP-042 r1
Approvazioni: revisione prodotto P-01, revisione operations O-01
Coerenza: controllo locale superato, output C-01 salvato
Permesso: push diretto del contributor negato, evento nativo D-01
Pubblicazione: commit merge-002; un clone pulito conferma 30 giorni
Eccezione: backup e obblighi legali restano esclusi
Ripristino: interruzione R-01 riletta e risolta tramite revisione
Passaggio: il secondo lettore trova la base corrente, l’eccezione e il passo successivo
Limite operativo: nessuna affermazione su eliminazione o distribuzione in produzione
Decisione: supportata solo per il flusso sintetico GitHub-first
```

Sostituisci ogni riferimento illustrativo con un artefatto osservato della sandbox. Ripeti il pacchetto completo per Mixed con versioni sorgente e revisioni proprie. Il revisore deve rifiutare un'approvazione GitHub copiata nel pacchetto Mixed.

## Scrivere una decisione delimitata

**Una buona decisione nomina il prossimo pilot**, non un rollout senza limiti. Per esempio, scegli un'altra impostazione di export sintetico con gli stessi ruoli e lo stesso percorso di lookup diretto, lasciando fuori dati reali e pubblicazione automatica.

| Elemento della decisione | Dettaglio richiesto |
|---|---|
| **Ambito** | Una modifica successiva e le sue esclusioni esplicite |
| **Prove** | Casi supportati e errori irrisolti |
| **Controlli** | Requisiti imposti dalla piattaforma e requisiti procedurali separati |
| **Proprietari** | Ruolo responsabile di ogni lacuna restante |
| **Lacuna runtime** | Comportamento di eliminazione o deployment non testato |
| **Condizioni di stop** | Accesso mancante, autorità cambiata, pubblicazione non autorizzata |

**Controllo finale:** entrambi i pacchetti superano la ricostruzione indipendente, i casi di errore applicabili hanno prove osservate e i controlli irrisolti restano visibili. Se solo GitHub è completo, segnala il completamento parziale del corso invece di supporre che Mixed si comporti allo stesso modo.

## Risoluzione dei problemi e backout

**Solo prove del percorso felice:** ripeti i test di diniego e interruzione. **Ruoli sovrapposti:** dichiarali e ripeti con utenti separati. **Controlli del piano mancanti:** fermati e ottieni una sandbox approvata.

**Backout:** ripristina la baseline tramite PR revisionate e modifiche Confluence, revoca le integrazioni temporanee, archivia le prove Jira ed esegui la pulizia sintetica approvata dai proprietari dopo la conservazione delle prove. Mantieni lo storico del recupero.

## Creare la decisione di rollout

```text
Decisione: altro pilota sintetico, bloccato o respinto
Prove: entrambi i pacchetti di esecuzione e la matrice dei guasti
Requisiti non applicati: elencare esplicitamente i controlli procedurali
Revisione del provider: ambito degli input e conservazione
Copertura dei responsabili: prodotto, operations, policy, repository, distribuzione
Lacune di produzione: test runtime, segreti, distribuzione, revisione degli accessi
Prossimo passo: seguito circoscritto con un ruolo responsabile
Data di revisione: assegnata dai responsabili del pilota
```

**Ragionamento atteso:** un successo sintetico sostiene un altro pilot delimitato. La produzione richiede approvazione separata per dati reali, deployment, gestione del provider e comportamento runtime. Una risposta riuscita dell'assistente non è autorizzazione al deployment.

## Riferimenti principali

- **Controlli del repository:** [Branch protetti](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Accesso al workplace:** [Permessi Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controlli di consegna:** [Schemi dei permessi Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Prossimi passi

**Torna all'[hub del corso](/ai-collaboration-course-start/)** per rivedere i controlli mancanti. Confronta la tua implementazione con [l'articolo sul framework](/articles/one-source-many-tools-ai-collaboration-framework/) prima di scegliere un altro pilot.
