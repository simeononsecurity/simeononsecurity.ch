---
title: "Configurare un server MCP: autorizzazioni, test degli strumenti e rimozione sicura"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Collega un server MCP di documentazione in sola lettura, esamina gli strumenti, esegui una lettura reale e rimuovi la connessione."
genre: ["Intelligenza artificiale", "Strumenti per sviluppatori"]
tags: ["Configurazione server MCP", "Protocollo di contesto dei modelli (MCP)", "Autorizzazioni MCP", "MCP in Codex", "MCP in Claude Code", "MCP in OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Un client IA collegato a un server di documentazione in sola lettura, con uno strumento e un limite di accesso visibili"
coverCaption: ""
---

[Torna al corso Flusso di lavoro pratico con l’IA](/effective-ai-course-start/)

**Usa un server MCP quando un’attività richiede uno strumento riutilizzabile o informazioni aggiornate fuori dal progetto.** Model Context Protocol, o MCP, definisce come client e server scambiano informazioni su strumenti, risorse e prompt. Una voce del server non dimostra che lo strumento funzioni. Questa lezione verifica una connessione documentale in sola lettura.

**Obiettivo di apprendimento:** distinguere la configurazione da una lettura MCP reale e documentare la rimozione sicura.

## Concetti chiave

- **Host MCP:** applicazione IA che coordina utenti, modelli, autorizzazioni e client.
- **Client MCP:** componente del protocollo che comunica con un server.
- **Server MCP:** programma o servizio remoto che offre strumenti, risorse o prompt.
- **Rilevamento degli strumenti:** prova che nel client compare una capacità nominata.
- **Esecuzione dello strumento:** prova di una chiamata reale e dei contenuti restituiti.
- **Ambito delle autorizzazioni:** accesso concesso da host, server, account e utente.

## Prima di iniziare

**Prerequisiti:** [esercitazione su contesto e passaggio di consegne](/articles/effective-ai-context-window-management/) e un’installazione aggiornata di Codex CLI per il percorso guidato. Dedica 35 minuti. Difficoltà intermedia. Gli altri agenti di programmazione hanno guide di configurazione separate. Il [server ufficiale OpenAI Docs MCP](https://learn.chatgpt.com/learn/docs-mcp) fornisce documentazione per sviluppatori in sola lettura e non richiede il caricamento dei dati del corso.

**Usa il laboratorio sintetico del corso.** Non collegare calendari, email o sistemi di produzione per questa esercitazione. Una lettura documentale basta per imparare gli stati della connessione.

## Comprendere il limite

| Stato | Cosa dimostra | Cosa non dimostra |
|---|---|---|
| **Configurato** | Esiste una voce del server | Raggiungibilità |
| **Connesso** | Il client ha raggiunto il server | Che esistano strumenti utili |
| **Rilevato** | Compare uno strumento nominato | Che la chiamata abbia esito positivo |
| **Eseguito** | Una chiamata ha restituito contenuti | Che l’attività finale sia corretta |
| **Verificato** | Fonte e risultato rispondono alla domanda | Che le chiamate future funzionino sempre |

**MCP da solo non concede autorizzazioni all’account.** Contano anche host client, server, autenticazione, ambito dell’account e impostazioni locali di approvazione. La [specifica MCP](https://modelcontextprotocol.io/specification/2026-07-28) definisce il protocollo, mentre ogni prodotto controlla la propria esperienza utente.

**Tratta l’output del server come materiale di riferimento.** Una pagina recuperata non può sostituire il tuo compito né autorizzare la scrittura di file. Ogni definizione di strumento consuma anche spazio nel contesto: collega solo il server necessario a questa lettura e rimuovilo dopo l’esercizio.

## Collegare la documentazione in sola lettura

**In Codex CLI,** esegui questi comandi in un terminale. Il primo aggiunge il server pubblico di documentazione. Il secondo elenca i server configurati.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Prova di configurazione attesa:** l’elenco contiene `openaiDeveloperDocs`. Questo prova solo la registrazione. Avvia una nuova sessione Codex nella cartella del laboratorio estratto e controlla gli strumenti MCP con `/mcp`. Usa i nomi mostrati dalla versione installata.

**Richiedi una lettura reale:**

```text
Usa il server MCP della documentazione per sviluppatori OpenAI per trovare le indicazioni attuali di AGENTS.md.
Restituisci il titolo e l’URL della pagina sorgente e due punti rilevanti per questo laboratorio. Indica lo strumento MCP usato.
Non modificare file.
```
**Esamina il risultato.** La pagina dovrebbe descrivere `AGENTS.md` come indicazioni per il repository e includere l’URL esatto della fonte. Apri la pagina citata e confermane l’argomento. Una risposta senza chiamata MCP nella trascrizione è una risposta normale, non una prova dell’esecuzione dello strumento.

## Diagnosticare un errore

**Se `codex mcp list` mostra il server ma `/mcp` non mostra strumenti,** la registrazione è riuscita ma il rilevamento è fallito. Riavvia la sessione, controlla i server attivi con `/mcp` e la configurazione salvata con `codex mcp get openaiDeveloperDocs`, poi verifica l’URL del server e l’accesso alla rete. Non dichiarare riuscita la configurazione MCP basandoti solo sulla voce.

**Se compare uno strumento ma la lettura non riesce,** registra l’errore e riprova una volta dopo aver controllato la connettività. Se la chiamata fallisce di nuovo, usa nel browser la pagina ufficiale citata come fonte alternativa e segna l’esercitazione MCP come incompleta. Non inventare un risultato dello strumento.

## Rimuovere la connessione

**Dopo la lettura,** rimuovi il server di prova da Codex CLI e conferma che la voce sia scomparsa.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Prova di rimozione attesa:** `openaiDeveloperDocs` non compare nel nuovo elenco. Riavvia una sessione Codex attiva prima di verificare se gli strumenti disponibili sono cambiati. Rimuovere una definizione locale non revoca autorizzazioni separate dell’account usate da un altro servizio.

## Scegliere un’altra applicazione

**Anche Claude Code e OpenCode supportano MCP.** Segui la [guida MCP di Claude Code](https://code.claude.com/docs/en/mcp) o la [guida MCP di OpenCode](https://opencode.ai/docs/mcp-servers/) relativa alla versione installata. Registra gli stessi cinque stati: configurato, connesso, rilevato, eseguito e verificato. Schema di configurazione e autorizzazioni degli agenti OpenCode variano tra versioni. Copia gli esempi dalla guida adatta alla tua installazione.

**Per un percorso solo tramite browser,** leggi la [pagina ufficiale AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) e compila lo stesso registro di verifica. Segna rilevamento ed esecuzione degli strumenti come “non eseguiti”. Questo percorso insegna a controllare le fonti, ma non dimostra il funzionamento di MCP.

## Esercitarsi e verificare

**Il tuo risultato:** un registro di connessione di cinque righe con nome del server, nome dello strumento, URL della fonte, risultato osservato e prova della rimozione. Evita token e identificativi dell’account in schermate e log.

**Criterio di completamento:** il percorso connesso riesce solo dopo una vera lettura tramite strumento e la successiva rimozione della configurazione. Il percorso alternativo completa l’esercizio sulle fonti con MCP segnato come non eseguito.

## Verificare la comprensione

1. **Domanda:** una voce MCP salvata dimostra che uno strumento ha funzionato? **Risposta:** no. Verifica rilevamento, autorizzazioni e una lettura effettiva.
2. **Domanda:** quale costo di contesto aggiunge una connessione MCP ampia? **Risposta:** descrizioni e schemi degli strumenti consumano parte del contesto attivo.

## Risoluzione dei problemi

- **Comando `codex` sconosciuto:** installa o aggiorna Codex CLI dalla guida ufficiale collegata.
- **Server elencato, nessuno strumento:** controlla lo stato della sessione e la diagnostica del server.
- **La chiamata restituisce contenuti non pertinenti:** restringi la richiesta e verifica la pagina sorgente.
- **La rimozione sembra inefficace:** avvia una nuova sessione e controlla l’elenco dei server attivi.

## Passi successivi

**Continua con [Verifica dell’output dell’IA](/articles/effective-ai-output-verification/).** Per estensioni più ampie, leggi la [guida del sito su plugin e strumenti MCP di Claude Code](/articles/claude-code-plugins-skills-mcp-tools/).

**Navigazione del corso:** [Precedente: Gestione del contesto](/articles/effective-ai-context-window-management/), [Indice del corso](/effective-ai-course-start/).
