---
title: "OpenClaw e Hermes Agent: una valutazione pratica"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Valuta gli agenti IA specializzati e persistenti con un inventario degli accessi, una revisione dei trigger, un registro del flusso dei dati e una decisione sul progetto pilota."
genre: ["Intelligenza artificiale", "Ingegneria del software", "Produttività"]
tags: ["agenti IA specializzati", "OpenClaw", "Hermes Agent", "agenti operativi", "valutazione degli agenti IA", "agenti IA persistenti"]
cover: "/img/cover/effective-ai-specialized-agent-evaluation.webp"
coverAlt: "Scheda che elenca gli strumenti, la memoria salvata, i trigger, i log e la decisione di revisione di un agente"
coverCaption: ""
---

[Torna al corso pratico sui flussi di lavoro con l’IA](/effective-ai-course-start/)

**Scegli un agente specializzato in base all’attività e agli accessi necessari.** Un agente operativo che esamina un file è diverso da un sistema persistente che riceve messaggi, conserva memoria ed esegue azioni pianificate. Questa lezione facoltativa usa OpenClaw e Hermes Agent come esempi e poi propone una scheda di valutazione da compilare prima dell’installazione.

**Obiettivo di apprendimento:** confronterai gli accessi e i trigger degli agenti, quindi registrerai una decisione per un progetto pilota limitato.

## Punti chiave

- **Agente operativo con ruolo circoscritto:** agente incaricato di una domanda o di un artefatto specifico.
- **Agente persistente:** servizio o sessione che conserva lo stato o risponde a trigger successivi.
- **Trigger:** evento, messaggio o pianificazione che avvia il lavoro.
- **Inventario degli accessi:** elenco degli strumenti, degli account, dei file e dei permessi di scrittura concessi all’agente.
- **Decisione sul progetto pilota:** rifiutare, eseguire un test limitato o approvare un uso definito.

## Prima di iniziare

**Prerequisiti:** [delega](/articles/effective-ai-agent-delegation/), [cicli con obiettivi delimitati](/articles/effective-ai-bounded-agent-loops/) e un caso d’uso fittizio. Dedica 35 minuti. La difficoltà è intermedia. Questa lezione non richiede l’installazione di un agente persistente.

**Caso d’uso:** una persona che coordina un laboratorio vuole che un assistente legga un programma e prepari una bozza di promemoria. La richiesta non autorizza l’invio del promemoria. La valutazione deve rispettare questo limite.

## Confronta i ruoli

| Approccio | Tipo di attività tipico | Prima domanda |
|---|---|---|
| **Una chat** | Scrivere un promemoria | Il programma è disponibile? |
| **Agente in sola lettura** | Verificare autonomamente i dati del programma | Quale fonte dovrebbe leggere? |
| **Agente di programmazione** | Aggiornare un programma locale per i rapporti | Quali file e test sono pertinenti? |
| **Piattaforma persistente** | Reagire a messaggi o programmi nel tempo | Quali trigger, strumenti e stati salvati esistono? |

**OpenClaw** è una piattaforma open source per agenti con gateway, canali di messaggistica, strumenti, memoria, connessioni MCP e sottoagenti. La [panoramica](https://docs.openclaw.ai/start/why-openclaw), la [guida alle connessioni MCP](https://docs.openclaw.ai/tools/mcp) e la [guida ai sottoagenti](https://docs.openclaw.ai/tools/subagents) descrivono questi componenti. Prima del progetto pilota, controlla le impostazioni attive dei canali, degli strumenti e della sandbox.

**Hermes Agent** è l’applicazione per agenti di Nous Research. La famiglia di modelli Hermes è separata. La [documentazione](https://hermes-agent.nousresearch.com/docs/), la [guida alla delega](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) e la [guida alla configurazione](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) trattano CLI, messaggistica, strumenti, memoria e attività delegate. La [guida alla memoria](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/) descrive gli archivi locali e l’approvazione delle scritture. Il valore predefinito documentato di `memory.write_approval` e `skills.write_approval` è `false`. Per un progetto pilota che richiede la revisione delle scritture, attiva l’approvazione o disabilita l’archivio pertinente. Verifica la configurazione in esecuzione prima di fare affidamento su uno dei due controlli.

| Punto di valutazione | OpenClaw | Hermes Agent |
|---|---|---|
| **Punto di ingresso** | Gateway e canali connessi | CLI o interfaccia di messaggistica configurata |
| **Lavoro delegato** | Sottoagenti con regole specifiche della piattaforma per sessioni e strumenti | Attività delegate con regole specifiche della piattaforma per gli strumenti |
| **Stato persistente** | Controlla la memoria abilitata e l’archiviazione delle sessioni | Controlla memoria e profili, oltre alle scritture delle competenze |
| **Lavoro ricorrente** | Controlla i trigger e le pianificazioni configurati | Controlla [processi cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/) e stato del gateway |
| **Primo progetto pilota** | Una richiesta manuale tramite un canale selezionato | Una richiesta manuale tramite CLI o messaggistica |

La tabella indica cosa controllare, non impostazioni di sicurezza equivalenti. Registra la versione installata e la configurazione attiva prima di concedere accesso a dati o account reali.

**I nomi non definiscono un modello di autorizzazione comune.** Un “sottoagente” di un prodotto potrebbe ricevere file, strumenti e cronologia diversi da un agente operativo di un altro prodotto. Controlla la documentazione della versione installata e le impostazioni attive, senza trasferire le tue supposizioni da uno strumento all’altro.

## Compila una scheda degli accessi

**Aggiungi una riga per ogni funzionalità** prima di installare o connettere un sistema. Se il prodotto è disponibile, usa le impostazioni effettive. Scrivi “sconosciuto” invece di indovinare.

| Domanda | Risposta per il progetto pilota del laboratorio |
|---|---|
| **Attività** | Preparare una bozza di promemoria usando un programma sintetico |
| **Ingresso** | Un file del programma approvato |
| **File** | Leggere il file del programma, senza accesso in scrittura |
| **Strumenti esterni** | Nessuno per il primo progetto pilota |
| **Accesso agli account** | Nessun account e-mail o calendario |
| **Trigger** | Solo richiesta manuale |
| **Scritture di memoria e competenze** | Registrare le impostazioni attive, disabilitare gli archivi o richiedere l’approvazione delle scritture durante il progetto pilota |
| **Log** | Registrare percorso di archiviazione, regola di conservazione, prompt, revisione della fonte e bozza |
| **Revisione** | Una persona controlla data, ora, luogo e lista dei destinatari |
| **Ripristino** | Eliminare la bozza e disabilitare il progetto pilota |

**Il flusso dei dati fa parte della scheda.** Indica dove gli input lasciano il computer, quale provider li elabora e dove persistono le trascrizioni o la memoria. Se uno strumento si collega all’e-mail, documenta se legge, crea bozze o invia. Sono ambiti di autorizzazione distinti.

## Decidi sul progetto pilota

**Rifiuta:** l’agente richiede ampi permessi di scrittura nella casella di posta per un’attività che deve solo creare una bozza, oppure trigger e log sono sconosciuti. Non occorre installare nulla per rifiutare una soluzione inadeguata.

**Progetto pilota:** limita l’input al programma sintetico, usa un trigger manuale, disabilita l’invio e controlla una bozza. Il risultato atteso è l’orario corretto delle 19:00 e nessun messaggio inviato. Se esegui il progetto pilota, registra la tua osservazione.

**Approva un uso definito:** solo dopo che il progetto pilota supera i controlli e il responsabile accetta gli accessi, i trigger, la conservazione e i passaggi di revisione esatti. L’approvazione per la redazione non autorizza l’invio o l’automazione successiva.

## Diagnostica un errore

**Supponi che una bozza di promemoria indichi le 18:00.** Controlla se l’agente ha letto il programma corrente o se la memoria salvata o un vecchio messaggio ha fornito l’orario non aggiornato. Sostituisci l’input obsoleto, ripeti un progetto pilota manuale e lascia l’invio disabilitato. Una seconda bozza corretta non cancella il primo errore dal registro.

**Supponi che nelle impostazioni appaia una connessione MCP, ma nessuno strumento sia raggiungibile.** Consulta gli [stati della connessione MCP](/articles/effective-ai-mcp-server-setup/). La presenza di una voce del server salvata non dimostra che la lettura sia riuscita.

## Esercitati e verifica

**Il tuo artefatto:** una scheda degli accessi compilata e una decisione: Rifiuta, Progetto pilota o Approva un uso definito. Indica un trigger, un limite delle autorizzazioni, una domanda sul flusso dei dati e un modo per fermare l’agente.

**Verifica di completamento:** un’altra persona dovrebbe capire quale azione esegue l’agente, cosa legge e memorizza, quando viene eseguito, chi controlla il risultato e come disabilitarlo. Se una risposta è sconosciuta, scegli Rifiuta o un Progetto pilota più ristretto.

## Verifica la comprensione

1. **Domanda:** un’attività di promemoria limitata alla bozza richiede il permesso di inviare e-mail? **Risposta:** No. Mantieni l’invio fuori dall’ambito del progetto pilota.
2. **Domanda:** quali impostazioni Hermes vanno controllate prima di un progetto pilota con scritture controllate? **Risposta:** Controlla le impostazioni attive di scrittura di memoria e competenze, inclusi i relativi controlli di approvazione.

## Prossimi passi

**Continua con il [progetto conclusivo del flusso di lavoro IA](/articles/effective-ai-capstone/)**. Per un confronto più ampio degli ambienti di esecuzione, consulta la [guida agli ambienti degli agenti](/articles/best-ai-agent-harnesses/).

**Navigazione del corso:** [Precedente: Cicli delimitati](/articles/effective-ai-bounded-agent-loops/), [Indice del corso](/effective-ai-course-start/).
