---
title: "Pacchetti di attività IA: prompt migliori e criteri di accettazione"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Trasforma richieste vaghe rivolte all’IA in pacchetti di attività con risultato, fonte, ambito dei file, verifiche e condizione di arresto definiti."
genre: ["Intelligenza artificiale", "Produttività", "Ingegneria del software"]
tags: ["scrittura di prompt IA", "pacchetto di attività", "prompt per agente di programmazione", "criteri di accettazione", "flusso di lavoro IA", "istruzioni per agenti IA"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "Una richiesta vaga riscritta come breve pacchetto di attività con fonte, ambito, verifica e condizione di arresto"
coverCaption: ""
---

[Torna al corso sui flussi di lavoro pratici con l’IA](/effective-ai-course-start/)

**Un buon prompt descrive il lavoro e come valuterai il risultato.** Aggiungere parole non risolve la mancanza di ambito. Questa lezione trasforma una richiesta vaga in un pacchetto di attività per il laboratorio del corso.

**Obiettivo di apprendimento:** scriverai un pacchetto di attività delimitato, con fonte, ambito dei file, verifiche e condizione di arresto.

## Punti chiave

- **Risultato** indica l’artefatto o il comportamento desiderato.
- **Ambito** indica i file consentiti e le azioni escluse.
- **Fonte** identifica il requisito approvato.
- **Criteri di accettazione** rendono osservabile il successo.
- **Condizioni di arresto** impediscono supposizioni e attività successive non autorizzate.

## Prima di iniziare

**Prerequisiti:** il laboratorio estratto, il suo file `docs/requirements.md` e la [lezione sul contesto del repository](/articles/effective-ai-agents-md-context/). Dedica 30 minuti. Il livello è principiante. L’esercizio termina con un pacchetto scritto. Per ora non serve modificare il codice.

## Confronta due richieste

**Richiesta vaga:** «Migliora lo script delle attività». Un agente potrebbe riscrivere l’output, aggiungere dipendenze, modificare i dati di esempio o saltare i test. La richiesta non definisce nessuna di queste scelte.

**Richiesta delimitata:** «Aggiungi un filtro di stato facoltativo a `task_report.py` usando la revisione 1 di `docs/requirements.md`. Mantieni l’output predefinito. Aggiungi test. Non modificare dati di esempio. Fermati prima del commit». L’agente sceglie ancora i dettagli dell’implementazione, mentre l’attività definisce il successo.

| Parte del pacchetto | Esempio del laboratorio | Verifica |
|---|---|---|
| **Risultato** | Aggiungere `--status` al rapporto | Entrambi i valori accettati funzionano |
| **Fonte** | `docs/requirements.md`, revisione 1 | Il codice corrisponde ai valori approvati |
| **Ambito** | Solo programma e test | Il diff non include altri file |
| **Vincoli** | Mantenere output predefinito e dati di esempio | L’output di base resta `Total tasks: 4` |
| **Evidenza** | Comando di test ed esecuzioni manuali | Gli output corrispondono ai conteggi attesi |
| **Arresto** | Non fare commit né push | Cronologia Git e remoto restano invariati |

## Usa un modello riutilizzabile

**Copia questo modello** per una piccola attività di programmazione o ricerca. Elimina i campi non pertinenti invece di riempirli con testo vago.

```text
Outcome:
Authoritative source and revision:
Relevant files or records:
Allowed changes:
Excluded changes and actions:
Examples of desired behavior:
Completion checks:
Stop or ask when:
Report back with:
```

**Per il laboratorio,** il pacchetto compilato è questo:

```text
Outcome: Add an optional --status filter to task_report.py.
Source: docs/requirements.md, revision 1.
Relevant files: task_report.py, tasks.json, tests/.
Allowed changes: task_report.py and focused tests.
Excluded: tasks.json, new dependencies, commits, pushes.
Examples: no filter prints Total tasks: 4. Open and done each print 2.
Checks: run unit tests and four manual commands: no filter, open, done, and invalid.
The invalid value must exit nonzero with a clear error.
Stop or ask: source conflict, missing file, unrelated failing baseline.
Report: changed files, commands, observed outputs, unresolved issues.
```

**Su Windows,** usa `py -3` nei comandi del pacchetto se il tuo ambiente usa il launcher Python.

**Il pacchetto non prescrive ogni riga di codice.** Lascia all’agente la scelta di una piccola implementazione e mantiene verificabile il risultato.

## Aggiungi esempi con attenzione

**Un esempio preciso riduce l’ambiguità.** Gli esempi `open` e `done` specificano l’output per il file fornito con quattro attività. Non stabiliscono una regola generale per ogni file. Per un file diverso, i conteggi dipendono dai suoi record.

**Separa i risultati attesi da quelli osservati.** Prima di eseguire il programma, `Total tasks: 2` è l’esito atteso per ciascuno stato. Dopo l’esecuzione, l’output del terminale è un’osservazione. Se i valori differiscono, esamina dati e implementazione prima di dichiarare il successo.

## Definisci una condizione di arresto

**Supponi che manchi il file dei requisiti.** Il pacchetto lo indica come fonte approvata. Fermati e chiedi il requisito invece di dedurre i valori accettati da una vecchia chat o da un problema di esempio.

**Supponi che i test di base falliscano prima delle modifiche.** Registra il fallimento e chiedi se correggere prima lo stato iniziale. Un’esecuzione successiva riuscita non chiarisce se la differenza dipenda dal filtro o dalla condizione iniziale.

**Supponi che l’agente voglia fare un commit.** Il pacchetto esclude i commit. Chiedigli di fermarsi dopo diff e test. Deciderai tu se un commit successivo rientra nel flusso del progetto.

## Controlla il pacchetto

**Assegna un punto per ogni risposta:** il risultato è concreto? La fonte che governa il lavoro è nominata? L’ambito dei file è chiaro? Sono indicate almeno due verifiche osservabili? È presente una condizione di arresto? Un punteggio sotto cinque indica che devi rivedere il pacchetto prima di delegare.

**Il tuo elaborato:** salva il pacchetto definitivo e una spiegazione di una riga di una condizione di arresto. Consegnalo a un agente di programmazione nella prossima lezione pratica oppure rispondi manualmente ai risultati attesi nel percorso di studio.

## Verifica la comprensione

1. **Domanda:** cosa rende verificabile un pacchetto di attività? **Risposta:** Una fonte, file consentiti, verifiche osservabili e una condizione di arresto.
2. **Domanda:** cosa deve fare un agente quando la fonte omette un dettaglio necessario? **Risposta:** Fermarsi e segnalare il dettaglio mancante invece di inventarlo.

## Risoluzione dei problemi

- **L’agente modifica troppo:** specifica file e azioni escluse nel pacchetto.
- **L’agente fa troppe domande:** fornisci la fonte mancante o un esempio concreto.
- **L’agente dichiara troppo presto il successo:** chiedi gli output osservati dei comandi e controlla i file.
- **Il pacchetto diventa troppo lungo:** sostituisci il materiale della fonte copiato con percorso e revisione.

## Passi successivi

**Continua con [La tua prima attività con un agente di programmazione](/articles/effective-ai-coding-agent-first-task/)**. Usa il pacchetto per guidare una piccola modifica del laboratorio.

**Navigazione del corso:** [Precedente: Contesto del repository](/articles/effective-ai-agents-md-context/), [Programma del corso](/effective-ai-course-start/).
