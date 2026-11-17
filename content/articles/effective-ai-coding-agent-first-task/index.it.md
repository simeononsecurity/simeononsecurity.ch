---
title: "Esegui la tua prima attività di repository con un agente di programmazione"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Scegli un'interfaccia per agenti di programmazione, apri un repository di esempio, controlla una modifica proposta ed esegui le verifiche prima di conservarla."
genre: ["Intelligenza artificiale", "Ingegneria del software"]
tags: ["guida a Codex CLI", "app Codex", "Claude Code CLI", "guida a OpenCode", "flusso di lavoro con agenti di programmazione", "strumenti di programmazione IA"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Un repository di codice con viste distinte dell'agente nel terminale e sul desktop accanto a un diff revisionato"
coverCaption: ""
---

[Torna al corso Flusso di lavoro pratico con l'IA](/effective-ai-course-start/)

**Un agente di programmazione legge file, propone modifiche ed esegue strumenti in un'area di lavoro.** In questa lezione completerai una piccola attività su un repository. Scegli Codex nell'app desktop di ChatGPT o nella CLI, Claude Code CLI oppure OpenCode TUI. Poi controlla una modifica prima di accettarla.

**Obiettivo didattico:** eseguirai o applicherai manualmente una modifica circoscritta e ne verificherai il diff e il comportamento.

## Punti chiave

- **Codex nell'app desktop di ChatGPT** offre un'area visuale per le attività e la loro revisione.
- **Codex CLI** avvia una sessione Codex dal terminale.
- **Claude Code CLI** esegue il flusso di programmazione di Claude dal terminale.
- **OpenCode TUI** offre un flusso di programmazione da terminale con provider e autorizzazioni configurabili.
- **Un diff e il risultato di un test** contano più del messaggio di completamento dell'assistente.

## Prima di iniziare

**Prerequisiti:** completa la [configurazione del corso](/articles/effective-ai-course-setup/), inclusi il test iniziale e lo snapshot Git locale. Completa [il contesto del repository](/articles/effective-ai-agents-md-context/) e i [pacchetti di attività](/articles/effective-ai-task-packets/) prima di questa lezione. Usa un agente di programmazione a cui sei autorizzato ad accedere. Dedica 45 minuti. La difficoltà va da principiante a intermedia.

**Usa il [laboratorio iniziale del corso](/downloads/effective-ai-course-lab.zip)** in una cartella temporanea. L'archivio contiene un piccolo programma per il resoconto delle attività, dati di esempio e test. Non usare un repository di produzione per la prima modifica. L'attività consiste nell'aggiungere un filtro `--status` mantenendo il conteggio totale esistente.

## Percorso senza agente di programmazione

**Chiedi a un assistente di chat di proporre la stessa modifica** se non hai un agente di programmazione. Incolla solo `docs/requirements.md`, `task_report.py` e il file di test mirato del laboratorio sintetico. Chiedi un diff unificato e una breve spiegazione. Un diff unificato mostra le righe precedenti con `-` e quelle nuove con `+`. Apri il file indicato in un editor di testo, sostituisci le righe vecchie con quelle proposte e salva. Poi esegui tutti i comandi della sezione Esamina il risultato. Lascia invariato `tasks.json`. Registra che il passaggio con l'agente non è stato eseguito. Il progetto finale ha una funzione JSON separata, quindi confronta la soluzione del filtro con il requisito e i controlli della lezione 5.

## Scegli un'interfaccia

**Scegli prima una superficie di revisione.** Codex nell'app desktop di ChatGPT è adatto a un progetto visuale e alla revisione dei diff. Un'interfaccia terminale è adatta al lavoro dalla cartella estratta del laboratorio. Confronta le opzioni per terminale tra loro:

| Strumento terminale | Verifica di account o provider | Comando iniziale |
|---|---|---|
| **Codex CLI** | Conferma l'accesso a Codex e le autorizzazioni locali | `codex` |
| **Claude Code CLI** | Conferma l'accesso a Claude Code e le autorizzazioni locali | `claude` |
| **OpenCode TUI** | Configura un provider di modelli supportato e le autorizzazioni | `opencode` |

**Installa e accedi seguendo la guida ufficiale aggiornata** dello strumento scelto. Leggi [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [app desktop ChatGPT](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) oppure [OpenCode](https://opencode.ai/docs/). Comandi, piattaforme supportate e requisiti degli account cambiano. Questa lezione usa solo i nomi di avvio stabili e una procedura comune di revisione.

**Per scegliere meglio il prodotto,** leggi il confronto del sito tra [agenti di programmazione CLI](/articles/cli-coding-agents-comparison/) o tra [agenti di programmazione con interfaccia grafica](/articles/gui-coding-agents-comparison/). Le guide di [Codex CLI e desktop](/articles/codex-cli-vs-desktop/), [Claude Code CLI e desktop](/articles/claude-code-cli-vs-desktop/) e [OpenCode CLI e desktop](/articles/opencode-cli-vs-desktop/) confrontano le interfacce di ciascun prodotto.

**Inizia dalla cartella del laboratorio.** Ogni interfaccia richiede la scelta esplicita di un'area di lavoro:

1. **Codex desktop:** apri l'app desktop ChatGPT, seleziona il laboratorio estratto come progetto locale e avvia un'attività locale al suo interno. Prima di una modifica, controlla il percorso della cartella e le richieste di approvazione. Un'attività ospitata usa una copia separata dell'area di lavoro.
2. **Codex CLI:** esegui `cd /path/to/effective-ai-course-lab`, poi `codex`. Conferma la cartella di lavoro mostrata e la modalità di approvazione.
3. **Claude Code CLI:** esegui lo stesso comando `cd`, poi `claude`. Conferma la cartella del progetto e le autorizzazioni degli strumenti.
4. **OpenCode TUI:** esegui lo stesso comando `cd`, poi `opencode`. Conferma il provider selezionato, il progetto e le impostazioni delle autorizzazioni.

**ChatGPT chat e Claude Projects gestiscono conversazioni e file di riferimento condivisi.** Codex e Claude Code lavorano in un'area di codice con strumenti per file e comandi. OpenCode offre anche superfici desktop e IDE, ma questa lezione usa l'interfaccia terminale. Provider, account ed esecuzione locale o ospitata variano, quindi registra la superficie scelta invece di trattare ogni sessione come la stessa esecuzione.

**Controlla cinque dettagli prima di aprire il laboratorio:** sistema operativo supportato, autenticazione, costo di provider o account, autorizzazioni per file e comandi e modalità di esecuzione locale o su host remoto. Registra la scelta. Non presumere che un'app desktop e uno strumento terminale usino la stessa area di lavoro.

## Esamina il progetto iniziale

**Riapri la cartella pulita del laboratorio** dalla lezione sul contesto del repository. Questa copia contiene il tuo `AGENTS.md` confermato e le indicazioni facoltative in `CLAUDE.md`. Esamina i file prima di chiedere all'agente di modificarli. Esegui i test iniziali da questa cartella.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Risultato iniziale atteso:** il resoconto stampa `Total tasks: 4`. L'esecuzione dei test nomina due test e termina con `OK`. Se uno dei due fallisce, fermati ed esamina i file estratti. Non attribuire all'agente la riparazione di una base iniziale difettosa.

**Usa gli snapshot Git locali** della configurazione del corso e della lezione sul contesto del repository. `AGENTS.md` e il `CLAUDE.md` facoltativo dovrebbero essere già confermati. Esegui `git status --short` prima della modifica e aspetta di vedere zero file. Anche l'agente non deve creare commit. L'archivio non contiene cronologia Git. Il file `.gitignore` esclude il bytecode Python generato durante l’esecuzione dei test. Se estrai una nuova copia, ripeti la configurazione del corso e la lezione sul contesto del repository in quella cartella. Conferma i file di istruzioni prima della modifica. Inizializza e conferma prima il progetto iniziale:

```bash
git init
git add .
git commit -m "Base del laboratorio del corso"
```

**Poi aggiungi `AGENTS.md` e il `CLAUDE.md` facoltativo** con la fonte approvata e il comando di test della lezione sul contesto del repository. Conferma i file, verifica che `git status --short` sia pulito e inizia la modifica. Esegui questi comandi nella cartella di pratica estratta, non nella radice di un altro repository.

## Invia una richiesta circoscritta

**Apri la cartella del laboratorio** nell'agente di programmazione scelto. Invia questo pacchetto di attività:

```text
Aggiungi un argomento facoltativo --status a task_report.py.
Valori consentiti: open e done.
Se assente, mantieni invariato l’attuale output del conteggio totale.
Se presente, conta solo le attività corrispondenti e stampa Total tasks: N.
Aggiungi test per entrambi i valori, un valore non valido e l’output predefinito invariato.
Non modificare tasks.json né file non correlati.
Esegui i test e comunica il comando esatto e il risultato.
Fermati dopo il codice e i test. Non creare commit né eseguire push.
```

**Su Windows,** sostituisci `python3` con il comando `py -3` verificato durante la configurazione, anche nelle istruzioni salvate del repository e nel pacchetto di attività.

**Chiedi un piano breve prima della modifica** se non conosci il codice. Autorizza l'agente a modificare solo la cartella temporanea del laboratorio. I controlli delle autorizzazioni cambiano tra strumenti, quindi verifica le impostazioni correnti prima di permettere comandi shell o scrittura di file.

## Esamina il risultato

**Leggi il diff.** Controlla che l'output senza filtro resti invariato, che il filtro accetti solo due valori e che i test coprano l'errore e l'output predefinito invariato. I test superati confermano la modifica solo se verificano il comportamento richiesto.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Risultati attesi:** i primi tre comandi del resoconto mostrano conteggi di 4, 2 e 2. Il valore non valido mostra un errore chiaro e termina con un codice diverso da zero. Il testo preciso dell'errore dipende dall'implementazione. Su macOS o Linux, esegui `echo $?` subito dopo il comando non valido per leggere il codice di uscita. In PowerShell, controlla `$LASTEXITCODE`.

| Evidenza | Cosa controllare |
|---|---|
| **Elenco file** | Cambiano solo programma e test |
| **Diff** | La logica del filtro corrisponde alla richiesta |
| **Output dei test** | I nuovi casi sono stati eseguiti e superati |
| **Esecuzione manuale** | I conteggi predefinito, `open` e `done` corrispondono a `tasks.json` |

**Se l'agente riferisce un risultato senza eseguire i test,** esegui il comando tu stesso. Se la modifica supera l'ambito del pacchetto, chiedi una correzione circoscritta. Se lo stato non è chiaro, elimina la copia di pratica estratta e decomprimi di nuovo lo ZIP originale.

## Soluzioni per il percorso di studio

**Usa questi file completi se la patch manuale non funziona.** Parti da un laboratorio appena estratto, salva il primo blocco come `task_report.py` e il secondo come `tests/test_task_report.py`, poi esegui i comandi della sezione Esamina il risultato. Lascia invariati `tasks.json` e `docs/requirements.md`. Registra il problema iniziale prima di copiare i file.

`task_report.py`:

```python
"""Mostra il numero di attività in un file JSON."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Conta tutte le attività o quelle con uno stato consentito."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Conta le attività del laboratorio")
    parser.add_argument("path", type=Path, help="percorso all’elenco attività JSON")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Test del resoconto attività del laboratorio."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Conserva una copia modificata che superi i test del filtro** durante le lezioni sul contesto e sulla verifica dei risultati. Se hai usato questo esempio completo per ripristinare il lavoro, conserva la nuova copia con i test del filtro superati per quelle lezioni. Mantieni il diff e il resoconto dei test fuori dal laboratorio. Ripristina il progetto iniziale prima della lezione sulla delega oppure elimina un tentativo non riuscito per ripartire da zero.

## Esercitati e verifica

**Il tuo risultato:** un diff del laboratorio e una registrazione di revisione in quattro righe che copra ambito dei file, comportamento predefinito, comportamento filtrato e input non valido. Annota nome e versione dello strumento in appunti privati per riprodurre un problema specifico della versione.

**Ragionamento atteso:** hai scelto un'interfaccia adatta al tuo modo di lavorare, hai definito un'attività circoscritta, hai esaminato la modifica reale e hai eseguito una verifica indipendente dal resoconto dell'agente.

## Verifica la comprensione

1. **Domanda:** Quali elementi dimostrano che la modifica al filtro di stato funziona? **Risposta:** Un diff circoscritto, test superati e risultati osservati per output predefinito, open, done e caso non valido.
2. **Domanda:** Il messaggio dell'agente che afferma di aver eseguito i test conta come risultato dei tuoi test? **Risposta:** No. Esegui il comando o esamina l'output dei test.

## Risoluzione dei problemi

- **Comando mancante:** completa l'installazione seguendo la guida del fornitore collegata, poi riapri il terminale.
- **Nessun accesso ai file:** apri la cartella estratta del laboratorio e controlla le autorizzazioni dell'area di lavoro.
- **File inattesi modificati:** fermati e controlla `git status --short` prima di inviare un'altra richiesta.
- **Test superati ma comportamento errato:** aggiungi un caso manuale o un test per il requisito mancante.

## Passaggi successivi

**Continua con [Finestre di contesto e passaggi di consegne](/articles/effective-ai-context-window-management/)**. Conserverai una nota utile per una nuova sessione.

**Navigazione del corso:** [Precedente: Pacchetti di attività](/articles/effective-ai-task-packets/), [Programma del corso](/effective-ai-course-start/).
