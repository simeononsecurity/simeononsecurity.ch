---
title: "Delegare agli agenti IA: assegnare il lavoro e rivedere i risultati"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Decidi quando è utile un secondo agente IA, assegna a ogni agente un compito delimitato, previeni conflitti di modifica e integra le prove nella sessione principale."
genre: ["Intelligenza artificiale", "Ingegneria del software"]
tags: ["delegazione agenti IA", "sottoagenti", "agenti lavoratori", "contesto orchestratore", "worktree IA", "attività IA parallele"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Un agente principale assegna attività separate di ricerca e revisione dei test, poi combina brevi rapporti con le prove"
coverCaption: ""
---

[Torna al corso pratico sui flussi di lavoro IA](/effective-ai-course-start/)

**Delega quando una domanda indipendente richiede una sessione separata.** Un agente lavoratore esamina le fonti, rivede i test o prepara una modifica circoscritta nel proprio contesto. L’agente principale controlla e integra il risultato. Questa lezione confronta documentazione mentre la sessione principale conserva la piccola attività di laboratorio.

**Obiettivo di apprendimento:** assegnerai una revisione indipendente a un lavoratore e verificherai il suo breve rapporto con le prove.

## Punti chiave

- **Orchestratore:** agente principale che coordina l’attività e la revisione finale.
- **Lavoratore:** agente separato incaricato di un unico risultato circoscritto.
- **Lavoro indipendente:** sottoattività la cui risposta non dipende dal risultato incompleto di un altro lavoratore.
- **Proprietà:** file o domanda assegnati a un solo lavoratore.
- **Integrazione:** confronto dell’output del lavoratore con le fonti attuali svolto dall’agente principale.

## Prima di iniziare

**Prerequisiti:** i tuoi resoconti di [passaggio del contesto](/articles/effective-ai-context-window-management/) e [verifica dell’output](/articles/effective-ai-output-verification/). Dedica 40 minuti. Difficoltà intermedia. Il percorso connesso richiede un prodotto con supporto per i lavoratori. Il percorso di studio usa una chat separata e l’integrazione manuale.

**Parti da una copia iniziale pulita per questa lezione.** Salva fuori dal laboratorio il diff del filtro modificato e il registro dei test. Estrai lo ZIP originale in una nuova cartella temporanea. Esegui il comando iniziale e i suoi due test di riferimento. Ripeti la base Git della lezione di configurazione del corso e ricrea le brevi istruzioni `AGENTS.md` e l’`CLAUDE.md` facoltativo della lezione sul contesto del repository. Esegui tu il commit di questi file e verifica che `git status --short` sia pulito. Conserva la copia modificata del filtro come riferimento, ma svolgi l’esercizio del lavoratore sulla copia iniziale pulita.

## Decidi se delegare

**Usa un agente** per una piccola modifica sequenziale. La delega ha costi di configurazione, token e revisione. Usa un lavoratore quando una domanda indipendente di sola lettura altrimenti riempirebbe la chat principale con molti file o pagine fonte.

| Attività di laboratorio | Delegare? | Motivo |
|---|---|---|
| **Aggiungere un filtro a due valori** | Di solito no | Un file piccolo e test mirati |
| **Trovare casi mancanti in due test di base** | Di solito no | La sessione principale legge prima un file breve |
| **Confrontare la documentazione attuale di tre prodotti** | Sì, in sola lettura | La lettura delle fonti resta nel contesto del lavoratore |
| **Modificare due volte la stessa funzione** | No | Le modifiche simultanee creano conflitti |

**Il lavoratore dovrebbe ricevere meno contesto dell’orchestratore,** non una copia dell’intera conversazione. Fornisci obiettivo, percorso della fonte, limiti dell’attività e formato di risposta. Mantieni un breve rapporto di prove nella sessione principale. Controlla di persona i file citati prima di agire.

## Avvia un lavoratore in sola lettura

**Mantieni piccolo il compito principale.** Nella sessione principale, leggi l’`AGENTS.md` locale e annota quale file contiene il comando di test. Assegna la domanda di ricerca separata qui sotto a un lavoratore. Non gli serve l’intero laboratorio o la chat precedente.

**Percorso connesso:** in Codex, Claude Code o un altro client con supporto ai lavoratori, apri il laboratorio come progetto e chiedi all’agente principale di delegare la richiesta in sola lettura seguente a un lavoratore. Controlla la trascrizione degli strumenti per verificare un avvio reale e il rapporto ricevuto. Se il prodotto non mostra un lavoratore, usa una sessione separata e identificala come sessione separata. Le guide correnti di [subagent Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagent Claude Code](https://code.claude.com/docs/en/sub-agents) e [agent OpenCode](https://opencode.ai/docs/agents/) descrivono i controlli disponibili.

**Percorso di studio:** apri una nuova chat per la stessa richiesta. Forniscile i tre link ufficiali o estratti delle fonti. Etichettala come lavoratore simulato. Una seconda chat è un contesto separato, non la prova di un subagent nativo.

```text
Usa la documentazione ufficiale corrente Codex AGENTS.md, Claude Code memory e OpenCode rules.
Confronta come ciascun prodotto carica i file di istruzioni del repository.
Non modificare i file.
Restituisci al massimo tre righe: prodotto, file di istruzioni, URL della fonte e un comportamento di caricamento.
Indica l’incertezza. Non incollare pagine intere.
```

**Fonti:** [istruzioni di progetto Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [memoria Claude Code](https://code.claude.com/docs/en/memory) e [regole OpenCode](https://opencode.ai/docs/rules/). Il rapporto atteso indica `AGENTS.md` per Codex e OpenCode. Le versioni correnti di Claude Code caricano direttamente anche `AGENTS.md` quando non prevalgono `CLAUDE.md` o `CLAUDE.local.md`. Questo laboratorio usa un file `CLAUDE.md` con un’importazione `@AGENTS.md`, compatibile anche con sessioni meno recenti o configurate diversamente. Verifica le pagine attuali e la versione attiva prima di presentare l’esempio come output osservato di un lavoratore.

## Integra i risultati

**Apri di persona le pagine fonte citate.** Se il lavoratore afferma che Claude Code richiede sempre un’importazione `CLAUDE.md`, controlla la sua guida memory e correggi il rapporto. Confrontalo con i file di istruzioni locali. Scrivi una breve nota d’integrazione:

```text
Accettato: Codex e OpenCode usano AGENTS.md per le istruzioni di progetto.
Le versioni correnti di Claude Code possono caricare AGENTS.md direttamente. Questo laboratorio
usa CLAUDE.md con un’importazione @AGENTS.md per una mappa condivisa stabile.
Prove: registra gli URL delle tre pagine ufficiali correnti e la data di revisione.
Decisione: mantieni una mappa condivisa breve e un’importazione per Claude.
```

**Questa nota è il risultato utile del lavoratore.** L’orchestratore ha bisogno di risultati verificati e percorsi delle fonti, non della trascrizione di ricerca. La delega consuma più token complessivi, quindi riduci la conversazione principale solo quando la sessione separata risparmia attenzione.

## Assegna la proprietà delle modifiche

**Se i lavoratori modificano file,** assegna la proprietà per file oppure usa worktree separati per attività sovrapposte sul repository. Un worktree è un’altra copia dello stesso repository Git con file di lavoro propri. Separa le modifiche simultanee. L’agente principale rivede e trasferisce i cambiamenti con un merge, cherry-pick o patch esplicito, poi ripete i test nell’albero integrato.

| Lavoratore | Lavoro assegnato | Restituisci |
|---|---|---|
| **Implementazione** | `task_report.py` | Diff e comando di test |
| **Autore dei test** | `tests/test_task_report.py` | Casi di test e risultato osservato |
| **Orchestratore** | Requisiti e integrazione finale | Diff combinato e criteri di accettazione |

**Il piccolo laboratorio non richiede modifiche parallele.** La tabella mostra un modello di assegnazione per lavori più grandi. I test in un worktree non validano un’implementazione ancora isolata in un altro. Se due lavoratori hanno bisogno della stessa funzione, procedi in sequenza o chiedi a uno di revisionare senza modificare. I worktree separati evitano collisioni tra file, ma non risolvono requisiti contraddittori.

## Verifica il comportamento del prodotto

**I subagent differiscono in base all’host.** Codex, Claude Code e OpenCode gestiscono in modo diverso ereditarietà del contesto, permessi degli strumenti e restituzione dei risultati. Leggi le guide di [subagent Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagent Claude Code](https://code.claude.com/docs/en/sub-agents) e [agent OpenCode](https://opencode.ai/docs/agents/) per il prodotto installato. Non presumere che un lavoratore condivida tutto il contesto principale o abbia un worktree isolato.

## Fai pratica e verifica

**Il tuo risultato:** un breve rapporto di un lavoratore sulla documentazione e una nota d’integrazione. Nel percorso di studio usa una nuova chat e contrassegnala come lavoratore simulato. Non dichiarare l’esecuzione di un subagent nativo in questo percorso.

**Controllo di completamento:** il rapporto cita tre fonti ufficiali, resta entro la domanda e rispetta il limite di lunghezza. La nota d’integrazione verifica le fonti e indica i file di istruzioni usati dal laboratorio.

## Verifica la comprensione

1. **Domanda:** Quando un lavoratore aiuta più di un singolo agente? **Risposta:** Quando possiede una domanda o un risultato indipendente e fornisce un rapporto di prove utile.

2. **Domanda:** Cosa fare dopo che due lavoratori modificano file sovrapposti? **Risposta:** Integra le modifiche, controlla il diff combinato e ripeti i controlli.

## Risoluzione dei problemi

- **Il lavoratore restituisce una lunga trascrizione:** chiedi una tabella di prove più breve con riferimenti ai file.
- **I lavoratori non concordano:** rileggi il file autorevole prima di scegliere una risposta.
- **Due modifiche si sovrappongono:** interrompine una e assegna la proprietà dei file o separa i worktree.
- **L’accesso agli strumenti del lavoratore è diverso:** controlla i suoi permessi invece di presumere che corrispondano a quelli del principale.

## Prossimi passi

**Continua con i [cicli di obiettivi delimitati](/articles/effective-ai-bounded-agent-loops/).** Per la governance del team oltre questo piccolo laboratorio, usa il [corso di implementazione della collaborazione IA](/ai-collaboration-course-start/).

**Navigazione del corso:** [Precedente: verifica dell’output](/articles/effective-ai-output-verification/), [Schema del corso](/effective-ai-course-start/).
