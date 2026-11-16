---
title: "Come verificare risultati, fonti, test e costi dell’IA"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Crea un verbale di accettazione per un risultato dell’IA verificando fonti, ambito dei file, prove dei test, privacy e utilizzo."
genre: ["Intelligenza artificiale", "Ingegneria del software"]
tags: ["verificare i risultati dell’IA", "verifica dei fatti con l’IA", "revisione di agenti di programmazione", "prove dei test IA", "monitoraggio dei costi IA", "revisione umana"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "Una scheda di revisione confronta un’affermazione dell’IA con un file sorgente, un diff del codice, l’output dei test e il totale di utilizzo"
coverCaption: ""
---

[Torna al corso Flusso di lavoro pratico con l’IA](/effective-ai-course-start/)

**Accetta un risultato dell’IA solo dopo aver verificato le prove adatte all’attività.** Una spiegazione curata, uno strumento configurato e un indicatore verde dei test rispondono a domande diverse. Questa lezione crea un unico verbale di revisione per il laboratorio del corso.

**Obiettivo di apprendimento:** produrrai un verbale di accettazione per fonti, ambito dei file, test, privacy e utilizzo.

## Punti chiave

- **Verifica delle fonti:** confronta un’affermazione fattuale con una fonte autorevole e aggiornata.
- **Verifica dell’ambito:** controlla quali file o sistemi sono cambiati.
- **Verifica del comportamento:** esegui test e casi manuali pertinenti.
- **Verifica della privacy:** controlla quali dati sono arrivati allo strumento o al fornitore.
- **Verifica dell’utilizzo:** registra token, chiamate agli strumenti e tariffa usata per il calcolo dei costi.

## Prima di iniziare

**Prerequisiti:** il laboratorio del corso, `docs/requirements.md`, uno snapshot Git locale e la [lezione MCP](/articles/effective-ai-mcp-server-setup/) o l’alternativa nel browser. Dedica 40 minuti. La difficoltà è intermedia. Usa il laboratorio modificato nella prima attività con un agente di programmazione. Se hai saltato la modifica, usa una nuova estrazione e indica che i controlli delle funzionalità non sono implementati. La base intatta supera ancora i due test originali.

## Verificare un’affermazione fattuale

**Affermazione:** «I valori di stato approvati sono `open` e `pending`». Apri `docs/requirements.md`, revisione 1. Il file indica `open` e `done`. L’affermazione è errata. Un tono sicuro non cambia il requisito.

**Per le affermazioni sui prodotti,** usa la documentazione ufficiale aggiornata e registra il titolo della pagina e la data di revisione. Un’affermazione su un menu, un piano, un comando o un limite di contesto diventa obsoleta prima di un principio generale del flusso di lavoro. La [documentazione Codex](https://learn.chatgpt.com/docs/codex/cli), la [documentazione Claude Code](https://code.claude.com/docs/en/overview) e la [documentazione OpenCode](https://opencode.ai/docs/) descrivono le interfacce correnti.

| Affermazione | Fonte | Decisione |
|---|---|---|
| **`open` e `pending`** | Requisito del laboratorio, revisione 1 | Rifiuta, sostituisci `pending` con `done` |
| **Il conteggio senza filtri è 4** | Programma di base e quattro voci JSON | Verifica eseguendo il programma |
| **È avvenuta una lettura MCP** | Trascrizione degli strumenti della sessione | Accetta solo se è visibile una chiamata allo strumento |

## Ispezionare la modifica

**Per un’attività di programmazione,** usa Git per elencare i file modificati e leggere il diff effettivo. Un nuovo file non tracciato compare nello stato anche se non compare in un diff normale, quindi controlla entrambi.

```bash
git status --short
git diff -- task_report.py tests
```

**Ambito previsto:** dopo l’attività di filtraggio cambiano solo `task_report.py` e i test mirati. Una modifica a `tasks.json`, `docs/requirements.md` o a un file di configurazione nascosto richiede una spiegazione e una revisione separata. Se non hai eseguito modifiche, non dovresti vedere cambiamenti.

## Verificare il comportamento

**Esegui gli stessi controlli di base e delle funzionalità** dalla cartella estratta del laboratorio. Il resoconto di completamento dell’agente deve riportare i risultati osservati.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Nella copia modificata,** i test coprono i nuovi casi, i conteggi sono 4, 2 e 2, e il valore non valido termina con un errore chiaro e un codice di uscita diverso da zero. In una nuova copia iniziale, passano solo i due test di base e il totale è 4. Registra separatamente lo stato iniziale.

**Un test della funzionalità non riuscito va diagnosticato.** Se `open` restituisce 4, controlla se l’argomento del filtro raggiunge la funzione di conteggio e se il programma confronta il campo `status` dell’attività. Non indicare come superato un test fallito solo perché l’agente dichiara completata l’implementazione.

## Controllare la riservatezza e l’accesso

**Registra quali file ha ricevuto l’agente.** Il laboratorio contiene dati sintetici e nessun segreto. Un progetto reale potrebbe contenere credenziali, dati dei clienti o documenti privati. Prima di condividere l’output, controlla prompt, log, schermate e diff per individuare questi valori.

**Un test locale dimostra solo il comportamento locale.** Non prova i permessi di un account cloud, l’ambito di un server MCP o il comportamento di un servizio distribuito. Verifica ogni confine nell’ambiente in cui è rilevante.

## Registrare utilizzo e costi

**I token misurano il volume di input e output del modello.** I dashboard dei prodotti variano, quindi usa i dati d’utilizzo mostrati dal tuo fornitore. Registra a parte le chiamate agli strumenti e i costi per immagini o ambienti ospitati, quando pertinenti. Controlla le tariffe correnti prima di calcolare una fattura reale.

**Apri la vista di utilizzo dell’account che ha eseguito l’attività.** Registra i token di input e output mostrati, il modello, il periodo di fatturazione e l’eventuale categoria di input memorizzato nella cache. Per gli abbonamenti ChatGPT o Claude, un limite o una quota d’uso non equivale al costo API di una singola attività. Per un’esecuzione di OpenCode tramite API o fornitore, consulta l’utilizzo o la fatturazione di quel fornitore e la tariffa corrente. Se il prodotto non mostra i token per attività, scrivi «non disponibile» e non dedurre un costo dalla lunghezza della chat.

**Calcolo illustrativo, non tariffa di un fornitore:** 30.000 token di input a 1 $ per milione costano 0,03 $. 5.000 token di output a 5 $ per milione costano 0,025 $. Il costo complessivo del modello in questo esempio è 0,055 $, prima dei costi degli strumenti o dell’hosting.

```text
costo input = token input / 1.000.000 × tariffa input
costo output = token output / 1.000.000 × tariffa output
totale = costo input + costo output + costi separati degli strumenti
```

**Anche un’attività delegata consuma token.** La delega sposta l’output dettagliato fuori dalla conversazione principale, ma non rende gratuito il lavoro. Confronta il costo con il valore del controllo indipendente.

**Tieni separate le categorie di costo.** Input memorizzato nella cache, nuovo input, output, chiamate agli strumenti ed esecuzione ospitata possono avere tariffe diverse. Questo esempio usa solo le tariffe per nuovo input e output. Non descrive un addebito di abbonamento o di uno strumento.

## Tenere un verbale di accettazione

| Campo | Esempio compilato dopo la modifica |
|---|---|
| **Fonte** | `docs/requirements.md`, revisione 1, letto |
| **File modificati** | `task_report.py` e `tests/test_task_report.py` in `git status --short` |
| **Test** | Superati i test di base e i nuovi test del filtro, registra il conteggio osservato |
| **Output manuale** | Osservati `Total tasks: 4`, `2` e `2`, valore non valido rifiutato |
| **Stato della funzionalità** | `--status open` e `--status done` implementati |
| **Riservatezza** | Solo file sintetici |
| **Utilizzo** | Registra i dati del tuo fornitore, se disponibili |
| **Decisione** | Accetta solo dopo il superamento dei controlli di fonte, diff, test e privacy |

**Il tuo risultato:** copia questo verbale e compilalo dopo la tua esecuzione. Sostituisci «osservato» solo con un output che hai visto. Scegli Accetta quando tutti i controlli richiesti passano, Rivedi quando la correzione è limitata, e Interrompi quando fonte, ambito o accesso non sono chiari.

## Verificare la comprensione

1. **Domanda:** il superamento della base iniziale dimostra che la funzionalità richiesta esiste? **Risposta:** No. Dopo la modifica, verifica il nuovo comportamento di accettazione.

2. **Domanda:** cosa deve contenere un verbale di accettazione? **Risposta:** prove delle fonti, file modificati, controlli del comportamento, ambito di accesso e utilizzo osservato.

## Risoluzione dei problemi

- **Nessuna fonte per un’affermazione:** contrassegnala come non verificata e trova una fonte autorevole.
- **I test passano ma l’output è diverso:** aggiungi un caso manuale e ispeziona i dati.
- **Mancano i dati d’uso:** registra «non disponibile» invece di stimare un costo reale.
- **Il diff include dati privati:** interrompi la condivisione dell’output e rimuovi quei dati dal verbale di esercitazione.

## Prossimi passi

**Continua con la [delega degli agenti](/articles/effective-ai-agent-delegation/)**. Per dettagli su costi e privacy, leggi il [routing dei fornitori](/articles/openrouter-provider-routing-quality-cost/) e il [confine di privacy dell’IA locale](/articles/local-ai-privacy-boundary/).

**Navigazione del corso:** [Precedente: configurazione MCP](/articles/effective-ai-mcp-server-setup/), [Indice del corso](/effective-ai-course-start/).
