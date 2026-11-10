---
title: "Recupero dalla deriva degli agenti AI e flusso di passaggio delle consegne"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Individua fonti e adattatori delle policy obsoleti, recupera pubblicazioni interrotte e verifica i passaggi indipendenti tra agenti."
genre: ["Intelligenza artificiale", "Collaborazione di gruppo", "Ingegneria del software"]
tags: ["corso di collaborazione AI", "deriva delle fonti", "recupero della pubblicazione", "passaggio tra agenti", "verifica di fonti aggiornate", "compensazione"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustrazione di professionisti che esaminano insieme il lavoro di progetto in un ambiente di cybersecurity"
coverCaption: ""
---
[Torna al corso sulla collaborazione AI](/ai-collaboration-course-start/)

**Controlla le derive prima delle attività e dopo un'interruzione della pubblicazione.** Confronta le versioni delle fonti, degli adattatori e lo stato di consegna nel repository o nella sandbox di lavoro. Fallo dopo aver completato un percorso. In questo modo eviti che vecchi riepiloghi diventino l'autorità corrente e conservi uno storico di recupero verificabile.

## Punti chiave

- **La deriva delle fonti** è diversa da quella degli adattatori.
- **La pubblicazione parziale** richiede un registro per ciascun sistema.
- **Il recupero** conserva lo storico e le modifiche esaminate.
- **I passaggi di consegne** richiedono nuove letture indipendenti delle fonti correnti.

## Prima di iniziare

**Prerequisiti:** il [flusso di lavoro GitHub nel browser](/articles/ai-collaboration-github-browser-workflow/) oppure il [flusso di pubblicazione misto](/articles/ai-collaboration-confluence-jira-publication/). **Tempo stimato:** da 60 a 90 minuti. **Difficoltà:** revisione avanzata.

**Sicurezza:** usa solo record sintetici. Sospendi la pubblicazione automatica prima dei test di recupero. Non è incluso alcun servizio di eliminazione attivo.

**Risultato per il lettore:** completa un inventario dello stato, una decisione del proprietario, una correzione esaminata e un passaggio che un altro revisore possa ricostruire consultando le fonti correnti. Il completamento dell'esercizio non autorizza la pubblicazione.

## Classificare le derive

| Deriva | Segnale | Responsabile della correzione |
|---|---|---|
| **Requisito** | La fonte differisce dal manifest | Proprietario del prodotto |
| **Policy** | L'adattatore differisce da POL-01 | Proprietario della policy |
| **Implementazione** | La configurazione contraddice l'intento | Manutentore |
| **Runbook** | Le istruzioni contraddicono il comportamento approvato | Responsabile operativo |
| **Accesso** | Una fonte prima leggibile ora è negata | Amministratore, attività interrotta |
| **Consegna** | Completata senza registro completo | Responsabile della consegna |

**Il testo più recente non è necessariamente l'autorità approvata.** Una modifica recente e non autorizzata richiede un'indagine, non un'adozione automatica. Determina lo stato e il proprietario prima di copiare i valori.

## Eseguire il controllo preliminare

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**Il collaboratore esegue il controllo preliminare prima di preparare una bozza. L'editore lo ripete prima di scrivere.** Conserva il confronto tra versioni insieme alla proposta. I controlli settimanali integrano queste letture, ma non le sostituiscono.

**Esempio di deriva dell'adattatore:** POL-01 passa alla versione 2 mentre CLAUDE.md indica ancora la versione 1. Fermati, leggi la modifica di policy esaminata, aggiorna l'adattatore tramite una PR protetta e avvia una nuova sessione. Cambiare solo il numero di versione senza caricare la policy non aggiorna il contesto.

**Inserisci una deriva della fonte nel laboratorio offline:** estrai una copia aggiornata dello ZIP fornito in una directory temporanea vuota. Dalla radice copia `baseline/` in `candidate/`, esegui `python3 check.py capture --base baseline > candidate/context.json`, quindi esegui `python3 check.py validate --base baseline --candidate candidate`. Registra il primo risultato `PASS`. Apri `baseline/requirement.json` in un editor di testo e modifica soltanto `"retention_days": 7` in `"retention_days": 8`. Esegui di nuovo lo stesso comando validate. Lo stato di uscita atteso è diverso da zero con il messaggio `STALE_CONTEXT: capture the trusted base again`. Registra entrambi i risultati e il percorso della fonte modificata. Elimina l'estrazione temporanea dopo aver salvato le prove private, poi estrai una copia nuova per ripristinare lo stato iniziale. Non applicare la modifica a otto giorni al repository pubblicato e non considerare una nuova acquisizione come approvazione del proprietario.

**Inserisci una deriva dell'adattatore nel repository temporaneo:** su un nuovo branch di proposta, copia in CLAUDE.md il testo approvato dell'adattatore POL-01 versione 1 ed etichettalo come versione 1. In una proposta di policy separata e soggetta a revisione, scrivi una modifica alla versione 2 con una nuova condizione di arresto specifica. Lascia l'adattatore alla versione 1. Chiedi a un revisore di confrontare i due record e contrassegnare l'adattatore come obsoleto prima di qualsiasi merge o esecuzione dell'agente. Ripristina chiudendo le proposte di test oppure aggiornando l'adattatore tramite una PR esaminata; poi apri una nuova sessione e verifica entrambe le versioni e la nuova condizione di arresto. Conserva i diff precedente e corretto. È un test della documentazione, non una simulazione di diniego della piattaforma.

## Recuperare una pubblicazione interrotta

1. **Sospendi la pubblicazione di PROP-042** e assegna il responsabile del recupero.
2. **Leggi lo stato reale** in tutti i sistemi coinvolti. Distingui ciò che è completato, non riuscito e non tentato.
3. **Chiedi al prodotto di scegliere** tra completamento, ripristino esaminato o sospensione.
4. **Prepara una proposta di recupero** basata su versioni aggiornate, mantenendo invariati ambito ed eccezioni salvo revisione esplicita.
5. **Applica una sola fase esaminata per volta**, registrando e rileggendo ogni risultato.
6. **Verifica lo stato finale** e i limiti residui prima di riprendere il lavoro ordinario.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Sostituisci gli stati esemplificativi con revisioni e valori osservati.** Una precedente voce del registro o un'affermazione dell'assistente non costituisce prova di una rilettura.

| Scelta | Quando usarla | Limite |
|---|---|---|
| **Completamento** | L'approvazione è valida e le fonti sono coerenti | Richiede una verifica aggiornata |
| **Ripristino** | Il proprietario ritira la modifica o l'implementazione non riesce | Non recupera i dati eliminati |
| **Sospensione** | Mancano prove o accesso | La consegna resta incompleta |

**Scegli la sospensione se mancano prove.** Gli esercizi sintetici non giustificano sovrascritture alla cieca. Indica il ruolo successivo e le prove mancanti.

**Il recupero GitHub** usa un revert o una compensazione esaminati. **Il recupero Confluence** confronta lo storico e usa un ripristino o una compensazione esaminati. **Il recupero Jira** conserva lo storico della proposta e riapre o blocca la consegna. Leggi le revisioni risultanti invece di presumere che la numerazione dello storico riparta da zero.

## Verificare un passaggio indipendente

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Apri un altro strumento o una sessione pulita** con la mappa e il passaggio di consegne, non con la conversazione precedente. Richiedi nuove letture delle fonti, un nuovo manifest e l'identificazione dell'azione in sospeso. Le prove raccolte manualmente nel browser restano valide se sono etichettate come istantanea e ricontrollate prima di scrivere.

**Passaggio negativo:** nega l'accesso a REQ-17. Aspettati un blocco esplicito, non un valore indovinato o un estratto privilegiato. Ripristina solo l'accesso approvato tramite l'amministrazione e ripeti la verifica.

## Diagnosticare prima di riparare

**Inizia da un inventario dello stato.** «Gli assistenti non sono d'accordo» descrive un sintomo della risposta, non il problema della fonte sottostante. Leggi separatamente il requisito mappato, la configurazione, il runbook, la policy e il record di consegna prima di chiedere a uno dei due assistenti di correggerli.

| Osservazione | Diagnosi | Prima azione |
|---|---|---|
| **Le fonti concordano, la vecchia risposta differisce** | Contesto della risposta obsoleto | Ricostruisci dalle letture aggiornate |
| **Requisito trenta, configurazione sette** | Disallineamento di consegna o implementazione | Esamina il pacchetto approvato e il registro |
| **Adattatore uno, policy due** | Disallineamento della versione delle istruzioni | Leggi la modifica della policy e correggi l'adattatore |
| **Fonte prima accessibile, ora negata** | Modifica dell'accesso | Interrompi l'attività e chiedi una revisione autorizzata |
| **Registro completo, runbook sette** | Chiusura senza rilettura valida | Riapri o blocca la consegna e indaga |

**Non trattare ogni discrepanza come un problema del modello.** Aggiornare una sessione corregge il contesto obsoleto della conversazione. Non pubblica un runbook, non ripristina un'autorizzazione mancante e non risolve decisioni contrastanti dei proprietari. Indica il responsabile della correzione prima di scegliere un'azione nello strumento.

## Percorrere la compensazione

**Interruzione illustrativa:** REQ-17 contiene l'intento approvato di trenta giorni, ma la consegna è ancora in sospeso. Configurazione e runbook indicano ancora sette giorni. Il manutentore segnala un problema d'implementazione non risolto. Il prodotto sceglie il ripristino anziché il completamento.

1. **Registra le versioni correnti:** requisito trenta, configurazione sette, runbook sette, consegna bloccata.
2. **Sospendi la proposta in attesa:** conserva le revisioni e le prove della pubblicazione fallita.
3. **Prepara una modifica compensativa del requisito:** ripristina sette mantenendo le esclusioni e le note intermedie.
4. **Ottieni la revisione del proprietario:** indica la versione corrente della fonte e il testo esatto del ripristino.
5. **Pubblica tramite il percorso autorizzato:** rileggi la versione risultante del requisito.
6. **Riconcilia il registro:** tutti i valori pubblicati pertinenti sono sette, la modifica originale non è stata consegnata.

**La compensazione non cancella lo storico.** Conserva come record distinti il tentativo di modifica a trenta giorni, il suo fallimento e il ripristino successivo. La fonte finale indica sette, mentre lo storico della consegna spiega perché la proposta approvata non è stata completata.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**Se un altro autore ha aggiunto un'eccezione, conservala esplicitamente.** Incollare alla cieca il vecchio corpo della pagina rischia di rimuovere una modifica intermedia valida. Confronta il testo attuale con quello desiderato, quindi sottoponi a revisione una modifica compensativa minima basata sulla versione corrente.

## Testare un passaggio nuovo

**Usa una sessione pulita e un revisore diverso.** Fornisci la mappa, il pacchetto fissato, il registro e la decisione di recupero. Escludi la chat precedente. Chiedi al destinatario di dichiarare l'intento corrente, la configurazione, le istruzioni operative e la prossima azione autorizzata.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Ragionamento atteso:** il destinatario verifica il risultato della compensazione prima di descrivere la baseline come ripristinata. Se ripete solo «sette giorni» dal passaggio, il requisito di lettura indipendente non è stato verificato. Richiedi prove dalle fonti invece di un altro riepilogo.

**Inventario didattico completato, interruzione sintetica:**

| Record | Stato osservato | Prove da conservare | Prossimo proprietario |
|---|---|---|---|
| REQ-17 | v5 indica trenta giorni, backup esclusi | Storico della pagina e nuova lettura | Prodotto |
| Configurazione protetta | `main` su `base-001` indica sette giorni | Lettura del commit ed evento di merge negato | Manutentore del repository |
| RUN-04 | v2 indica ancora sette giorni | Nuova lettura della pagina | Operations |
| PROP-042 | r1 approvata, consegna bloccata | Revisioni fissate e registro | Responsabile della consegna |

Consegna questo inventario a un secondo lettore senza la vecchia chat. Il passaggio è superato solo se il lettore trova in autonomia tutti e quattro gli stati, indica l'esclusione dei backup, identifica `base-001` come revisione protetta corrente e raccomanda un passaggio di recupero esaminato dal proprietario. Segna come non superato una revisione errata, un'eccezione mancante o una ripresa non supportata. Registra i riferimenti alle fonti del lettore e qualsiasi correzione prima di un'altra scrittura.

## Decidere se riprendere

| Esito del controllo preliminare | Decisione sulla ripresa |
|---|---|
| **Le fonti corrispondono all'approvazione fissata** | Continua con il passaggio autorizzato in sospeso |
| **La fonte è cambiata fuori dall'ambito esaminato** | Interrompi per il confronto e una nuova revisione |
| **Manca l'accesso in lettura** | Sospendi con un revisore dell'accesso assegnato |
| **La policy è cambiata** | Correggi gli adattatori e rivaluta il permesso dell'attività |
| **Esito della scrittura sconosciuto** | Leggi la destinazione prima di riprovare |

**Definisci criteri concreti per l'accettazione del recupero.** Richiedi una rilettura coerente, un oggetto di revisione aggiornato, un registro riconciliato e un nuovo passaggio. Non chiudere il recupero perché l'assistente dichiara che il problema è risolto.

**Controllo di completamento:** consegna un inventario dello stato osservato, la decisione del proprietario, la correzione esaminata, la rilettura finale e una ricostruzione indipendente. Se l'accesso impedisce la lettura, documenta il blocco. Applica questo standard probatorio al progetto finale.

## Risoluzione dei problemi e ripristino

**Conflitti del revert:** prepara una modifica compensativa sullo stato corrente. **Il ripristino perde eccezioni:** confronta l'intera sezione pertinente prima di scrivere. **La vecchia memoria controlla la risposta:** riparti dalle fonti approvate e rimuovi il contesto obsoleto della bozza.

**Annullamento del recupero:** fermati all'ultimo stato verificato e aggiungi una voce al registro. Non cancellare gli eventi di audit nativi né forzare il reset dello storico protetto. Segnala al prodotto le questioni di autorità non risolte.

## Esercizio e autovalutazione

**Inserisci prove obsolete, un adattatore di policy non aggiornato e una pubblicazione parziale.** Fornisci i record a un altro revisore senza narrazione e chiedigli di indicare il responsabile della correzione.

**Ragionamento atteso:** il prodotto gestisce la riconciliazione dei requisiti, il proprietario della policy l'allineamento dell'adattatore e il coordinatore del recupero della consegna il coordinamento dei proprietari coinvolti. «Aggiorna il contesto» non è una correzione completa per tutti i casi.

## Riferimenti principali

- **Controlli di recupero del repository:** [Branch protetti](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Cronologia delle pagine:** [Documentazione Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Ispezione delle istruzioni:** [Memoria Claude Code](https://code.claude.com/docs/en/memory).

## Passaggi successivi

**Completa il [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** usando entrambi i percorsi e un secondo lettore. Mostra letture aggiornate delle fonti, discrepanze di versione, proprietario della decisione, recupero esaminato, rilettura e ricostruzione indipendente.
