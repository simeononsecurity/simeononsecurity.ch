---
title: "Gestione della finestra di contesto IA: mantieni focalizzati gli agenti di coding"
description: "Controlla il contesto attivo di un’attività IA con file selezionati, passaggi concisi e risposte brevi dei collaboratori, preservando decisioni e prove."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Intelligenza artificiale", "Ingegneria del software"]
tags: ["gestione della finestra di contesto IA", "contesto agente di coding", "passaggio IA", "compattazione del contesto", "orchestrazione agenti", "budget di token"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "Una nota di passaggio concisa accanto a file di progetto selezionati e a una trascrizione di chat molto più lunga scartata"
coverCaption: ""
---

[Torna al Corso pratico sui flussi di lavoro con l’IA](/effective-ai-course-start/)

**La finestra di contesto è il testo e il materiale che un modello elabora nel turno corrente.** Prompt, istruzioni, definizioni degli strumenti, estratti di file, risultati degli strumenti e cronologia della conversazione occupano spazio. Questa lezione spiega come mantenere mirata l’attività successiva e lasciare un passaggio di consegne affidabile.

**Obiettivo di apprendimento:** creare un passaggio di consegne breve e provarlo in una nuova sessione.

## Concetti principali

- **Token:** unità usate da un modello per elaborare input e output.
- **Contesto attivo:** materiale disponibile durante un turno, entro i limiti del prodotto.
- **Fonti durature:** file o registri del progetto esterni alla chat.
- **Compattazione:** riassume o elimina il contesto precedente e potrebbe omettere un dettaglio necessario.
- **Passaggio di consegne:** indirizza una nuova sessione alle fonti aggiornate e al lavoro verificato.

## Prima di iniziare

**Prerequisiti:** il tuo laboratorio modificato dalla [prima attività con un agente di coding](/articles/effective-ai-coding-agent-first-task/), il requisito approvato e la [lezione sui pacchetti di attività](/articles/effective-ai-task-packets/). Se hai seguito il percorso di studio, usa il laboratorio che hai modificato manualmente. Dedica 35 minuti. La difficoltà è intermedia. Conserva le note del corso fuori dalla cartella estratta del laboratorio, così `git status` mostra solo le modifiche al codice.

## Seleziona il contesto in base all’attività

**Per modificare il filtro di stato,** l’agente ha bisogno di `task_report.py`, `docs/requirements.md`, dei test pertinenti e di un piccolo campione di `tasks.json`. Non servono tutte le vecchie chat, l’intera documentazione del sito o la cronologia Git completa. Consulta prima una mappa, poi carica solo i file necessari alla decisione successiva.

| Attività | Contesto utile | Contesto superfluo |
|---|---|---|
| **Definire il comportamento** | Requisito approvato e un campione di dati | Vecchie conversazioni esplorative |
| **Modificare il programma** | Programma e test mirati | Directory di progetti non pertinenti |
| **Esaminare il risultato** | Diff, output dei test, requisito | Trascrizione completa dell’agente |
| **Riprendere più tardi** | Nota di passaggio e percorsi delle fonti | Chat di ore incollata per intero |

**È una scelta di recupero delle informazioni, non una regola per nascondere prove.** Se un test fallisce, includi l’output esatto e il file coinvolto. Rimuovi i registri irrilevanti, non i dettagli necessari per diagnosticare il problema.

**Considera il costo fisso prima di aggiungere collaboratori.** Le istruzioni dell’agente e gli schemi degli strumenti disponibili possono occupare contesto prima della lettura di un file di attività. Un secondo collaboratore ripete parte di questo costo e aggiunge un rapporto che l’agente principale deve esaminare. Per una modifica a due file basta un agente. Per una ricerca indipendente su molte fonti, un breve rapporto può ridurre il contesto della sessione principale, anche se il consumo totale di token aumenta.

## Prepara un passaggio di consegne conciso

**Un passaggio di consegne è un breve resoconto per la sessione successiva.** Distingue il lavoro completato da quello proposto. Salva questo esempio come `course-notes/handoff.md`, fuori dal laboratorio, e sostituisci le osservazioni d’esempio con le tue.

```text
Obiettivo: aggiungere --status open|done al rapporto delle attività del corso.
Fonte: docs/requirements.md, revisione 1.
Area di lavoro: cartella effective-ai-course-lab estratta.
Stato attuale: il filtro di stato è presente in task_report.py e nei test.
Verificato: registra il risultato osservato dei test e i conteggi manuali 4, 2 e 2.
Decisione: tasks.json è rimasto invariato.
In sospeso: revisione indipendente delle differenze e della fonte.
Prossimo controllo: riesegui i test e il caso di stato non valido.
Fermati se: requisito o valore di base differiscono da questo registro.
```

**L’esempio non afferma che tu abbia svolto quel lavoro.** Annota i risultati effettivi dei test e i file modificati. Se cambia la revisione della fonte, aggiorna il passaggio dopo averla riletta.

## Prova una sessione nuova

**Avvia una nuova chat o sessione di agente di coding** nel laboratorio. In una chat, incolla il passaggio e il file `AGENTS.md` del laboratorio sintetico, quindi indica i file da esaminare. In un agente di coding, apri la cartella del laboratorio e incolla il passaggio consentendo l’accesso in lettura ai file nominati. Chiedi:

```text
Usando questo passaggio e i file correnti del repository, indica i valori di stato approvati, il conteggio di base e il prossimo controllo. Non modificare.
Se il passaggio è in conflitto con una fonte corrente, segnala il conflitto.
```

**Ragionamento previsto:** la nuova sessione trova `open` e `done` in `docs/requirements.md`, identifica il conteggio iniziale di 4 e indica test e verifiche manuali. Se ripete il vecchio valore `pending`, rileggi il requisito e correggi il passaggio.

## Mantieni snello l’orchestratore

**Un orchestratore è l’agente principale che coordina i collaboratori.** Assegna a ciascuno una domanda circoscritta e file di input precisi. Chiedi un risultato conciso: rilievo, percorso della prova, livello di fiducia e questione irrisolta. Conserva i registri dettagliati in un file o nella sessione del collaboratore. Riporta solo ciò che serve all’agente principale per decidere il passo successivo.

**Esempio:** chiedi a un collaboratore in sola lettura di esaminare i test e rispondere «caso mancante, file e riga, controllo suggerito». Non chiedergli di incollare tutti i test nella chat principale. L’agente principale verifica il rilievo nel repository prima di modificare il codice. La [lezione sulla delega](/articles/effective-ai-agent-delegation/) aggiunge un’attività indipendente quando l’ambito ne giustifica il costo.

**In molti prodotti le sessioni dei collaboratori hanno un contesto proprio,** ma ereditarietà e isolamento variano. Controlla le regole attuali del prodotto prima di supporre che un collaboratore veda le stesse istruzioni, gli stessi file o strumenti dell’agente principale. Le guide ai [subagenti di Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents) e ai [subagenti di Claude Code](https://code.claude.com/docs/en/sub-agents) descrivono il comportamento dei rispettivi prodotti.

## Usa la compattazione con attenzione

**La compattazione accorcia la cronologia attiva.** Codex, Claude Code e OpenCode differiscono per quando e come la eseguono. Considera un riepilogo compattato un aiuto per riprendere, non il registro completo del progetto. Conserva requisiti e decisioni nei file e ricontrollali dopo la compattazione. Consulta le indicazioni aggiornate sulle [buone pratiche di Codex](https://learn.chatgpt.com/docs/learn/best-practices), sui [comandi di Claude Code](https://code.claude.com/docs/en/commands) e sulla [compattazione in OpenCode 2](https://opencode.ai/v2/docs/compaction). OpenCode 1 e OpenCode 2 usano schemi diversi. Controlla `opencode --version` prima di copiare le impostazioni.

**Se l’assistente perde un vincolo,** interrompi la modifica, riapri la fonte e riformula il pacchetto di attività. Spesso una nuova sessione con un passaggio breve e verificato richiede meno attenzione delle correzioni ripetute in una chat lunga e confusa.

## Esercitati e verifica

**Il tuo artefatto:** un passaggio di meno di 180 parole, salvato fuori dal laboratorio. Contrassegna ogni riga come fonte, risultato osservato, decisione o azione in sospeso. Forniscilo a una nuova sessione e annota se nomina entrambi i valori di stato approvati e il controllo successivo.

**Verifica finale:** la nuova sessione indica `open`, `done`, il conteggio iniziale di 4 e un passaggio di test senza dipendere dalla vecchia chat. Correggi eventuali lacune e riprova con un’altra sessione nuova.

## Verifica la comprensione

1. **Domanda:** cosa deve contenere un passaggio per una nuova sessione? **Risposta:** obiettivo, fonte autorevole, stato attuale, risultato verificato e azione successiva.

2. **Domanda:** perché mantenere breve il rapporto di un collaboratore? **Risposta:** un rapporto conciso con prove fornisce all’orchestratore il risultato necessario senza ripetere la trascrizione del collaboratore.

## Risoluzione dei problemi

- **Il riepilogo omette una decisione:** aggiungi una breve riga con decisione e revisione della fonte.
- **La risposta del collaboratore è enorme:** chiedi una tabella delle prove limitata e riferimenti ai file.
- **Il passaggio è obsoleto:** rileggi le fonti attuali prima di modificare.
- **La pressione sul contesto continua:** dividi l’attività in sessioni più piccole con artefatti separati.

## Passi successivi

**Continua con la [configurazione del server MCP](/articles/effective-ai-mcp-server-setup/)**. Aggiungerai uno strumento esterno in sola lettura mantenendone circoscritto l’output.

**Navigazione del corso:** [Precedente: prima attività di coding](/articles/effective-ai-coding-agent-first-task/), [Indice del corso](/effective-ai-course-start/).
