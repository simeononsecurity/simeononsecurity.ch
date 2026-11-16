---
title: "Capstone del flusso di lavoro IA: creare e verificare un rapporto JSON"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Crea un nuovo rapporto JSON con il contesto del progetto, una richiesta circoscritta per l’agente, test indipendenti, revisione delle fonti e passaggio a una nuova sessione."
genre: ["Intelligenza artificiale", "Ingegneria del software", "Istruzione"]
tags: ["capstone del flusso di lavoro IA", "progetto con agente di programmazione", "verifica delle attività IA", "AGENTS.md", "esercitazione MCP", "passaggio tra agenti"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Attività software del workshop completata con file sorgente, risultati dei test, revisione dell’agente e registro del passaggio"
coverCaption: ""
---

[Torna al corso sul flusso di lavoro pratico con IA](/effective-ai-course-start/)

**Crea un nuovo formato di output e dimostrane il comportamento.** In precedenza hai aggiunto un filtro di stato. Questo capstone parte da un laboratorio nuovo e aggiunge un rapporto JSON leggibile da un altro programma. Il nuovo requisito verifica se sai trasferire il tuo flusso di lavoro a una funzione diversa.

**Obiettivo didattico:** consegnerai un rapporto JSON verificato, un registro delle prove relative a fonti e strumenti e un passaggio che una nuova sessione possa comprendere.

## Punti chiave

- **Un requisito separato** definisce la funzione del capstone.
- **La modifica di un agente di programmazione** resta nei file indicati.
- **Verifiche indipendenti** determinano l’accettazione.
- **Un passaggio a una nuova sessione** permette di ricostruire il risultato.

## Prima di iniziare

**Prerequisiti:** completa le lezioni da 0 a 10, inclusi il contesto del repository, il primo compito di programmazione, MCP o l’alternativa nel browser, la delega e i cicli delimitati. La lezione 11 è facoltativa. Dedica da 90 a 120 minuti. Difficoltà intermedia.

**Usa una nuova estrazione** del [laboratorio iniziale](/downloads/effective-ai-course-lab.zip). Esegui `python3 task_report.py tasks.json` e i due test di base prima di ogni modifica. Su Windows, usa `py -3` se la configurazione usa il launcher Python. Crea una base Git locale come nella configurazione del corso. Il filtro di stato della lezione 5 è assente per scelta.

**Leggi `docs/capstone-requirements.md`, revisione 1.** Richiede `--format text|json`. L’output testuale predefinito resta `Total tasks: 4`. L’output JSON contiene un totale numerico e i conteggi per ogni stato presente nei dati. Verifica una lista vuota, uno stato mancante e un formato non supportato. Non usare `docs/requirements.md` come riferimento per questa nuova funzione.

**Scegli il percorso.** Il percorso connesso usa una modifica osservata di un agente di programmazione, una vera chiamata MCP in sola lettura e un worker nativo o una sessione worker separata. Il percorso di studio usa un assistente chat per proporre codice, una fonte browser al posto di MCP e chat separate come worker simulati. Indica come «non eseguiti» i passaggi degli strumenti non disponibili. Entrambi i percorsi richiedono test locali e revisione dei file. La soluzione qui sotto contiene file completi come percorso di ripristino. Salva il primo tentativo negli appunti prima di copiare la soluzione in una nuova estrazione.

## Verifica 1: Descrizione del progetto

**Apri il progetto sintetico del workshop ChatGPT o Claude.** Chiedi una bozza di promemoria di due frasi. Verifica le 19:00 in `approved-schedule.md`. Il programma del promemoria segue l’orario approvato. Il programma segue i requisiti del capstone.

**Prova:** registra il nome del progetto, la revisione della fonte, l’ora osservata nella bozza e ogni correzione. Non inviare il messaggio.

## Verifica 2: Contesto dell’archivio

**Apri il laboratorio nuovo.** Crea un breve `AGENTS.md` che rimandi a `docs/capstone-requirements.md`, `task_report.py`, ai test e al comando di test verificato durante la configurazione. Se usi Claude Code, importa il file condiviso da `CLAUDE.md`. Crea un commit umano di configurazione per questi file guida e poi conferma che `git status --short` non mostri modifiche. L’agente di programmazione non deve fare commit della modifica alla funzione.

**Prova:** salva la mappa e una copia pulita delle istruzioni. Indica le chiavi JSON e il comportamento per gli input non validi della revisione 1. Se una chat precedente descrive il filtro di stato, trattala come contesto di un’attività diversa.

## Verifica 3: Risorsa esterna

**Percorso connesso:** usa il [server OpenAI Docs MCP in sola lettura](https://learn.chatgpt.com/learn/docs-mcp) tramite un client supportato. Chiedi a uno strumento MCP le indicazioni correnti per `AGENTS.md`. Registra il nome dello strumento, l’URL della fonte e un punto utile per il laboratorio. Rimuovi poi la connessione di esercizio.

**Percorso di studio:** apri in un browser la [documentazione ufficiale di `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Registra titolo, URL e un punto utile. Indica «non eseguite» per la ricerca e l’esecuzione MCP.

**Prova:** una voce server configurata non dimostra che sia stata eseguita. Il percorso connesso richiede una chiamata allo strumento visibile e contenuto restituito dalla fonte.

## Verifica 4: Affida una revisione

**Chiedi a un worker in sola lettura** di esaminare `docs/capstone-requirements.md`, `task_report.py` e i test di base. Richiedi un rapporto di massimo cinque righe che indichi controlli mancanti e percorsi dei file. Nel percorso di studio, usa una chat separata e contrassegnala come worker simulato.

**Risultato atteso:** i test iniziali coprono il totale e un valore JSON che non è una lista. Non coprono l’output JSON, una lista vuota, uno stato mancante o un formato non valido. Apri il file dei test e verifica il rapporto. Una breve revisione indipendente è utile perché i criteri di accettazione differiscono da quelli della lezione 5.

**Prova:** salva il breve rapporto e la decisione di integrazione in una frase. Conserva la trascrizione del worker fuori dal registro principale dell’attività.

## Verifica 5: Richiedi il cambiamento

**Fornisci a un agente di programmazione** il pacchetto seguente. Nel percorso di studio, un assistente chat propone la patch e tu la applichi manualmente nel laboratorio.

```text
Obiettivo: aggiungere --format text|json dopo il percorso JSON.
Fonte: docs/capstone-requirements.md, revisione 1.
File modificabili: task_report.py e tests/test_task_report.py.
Mantenere: Total tasks: 4 come output predefinito e tasks.json invariato.
JSON: un oggetto con total e conteggi by_status, senza altro testo su stdout.
Controlli richiesti: testo predefinito ed esplicito, JSON 4/2/2, lista vuota,
stato mancante, formato non valido e test di base.
Fermarsi se: conflitto tra fonti, test di base non correlato fallisce o modifica fuori ambito.
Rapporto: file modificati, comandi, output osservati, problema irrisolto.
Non fare commit, push, pubblicare o inviare messaggi.
```

**Esamina il piano** prima delle modifiche. La scelta dello schema è importante: `total` è un numero, non la stringa `"4"`. `by_status` include ogni stato presente nell’input, così il rapporto comprende anche uno stato aggiunto in futuro. Mantieni la modifica nel laboratorio estratto.

## Verifica 6: Prova e revisione

**Esegui tu questi controlli.** Su Windows, sostituisci `python3` con `py -3`. L’ordine delle chiavi e gli spazi dell’output JSON non contano. Analizza l’output come JSON e confronta i valori tipizzati.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Comportamento atteso:** i test passano. Entrambi i comandi testuali stampano `Total tasks: 4`. Il comando JSON restituisce un solo oggetto con `total` 4, `by_status.open` 2 e `by_status.done` 2. Un formato non valido termina con un codice diverso da zero. I test coprono anche una lista vuota e un’attività priva di `status` testuale. Leggi l’output di errore osservato e il codice di uscita per questi casi.

| Checkpoint | Prova di esito positivo | Recupero in caso di errore |
|---|---|---|
| **Descrizione del progetto** | Il promemoria riporta le 19:00 | Aggiorna la fonte dell’orario |
| **Mappa del repository** | Requisito del capstone e percorsi dei test indicati | Correggi i file guida |
| **Risorsa esterna** | Fonte MCP letta o alternativa browser segnalata | Verifica connessione o URL |
| **Revisione del worker** | Controlli mancanti verificati nel file | Correggi il rapporto del worker |
| **Ambito dei file** | Solo programma e test | Esamina ogni modifica indesiderata |
| **Comportamento** | Testo, JSON, input vuoti ed errori verificati | Diagnostica una causa e riprova |
| **Passaggio** | Una nuova sessione ricostruisce lo stato | Aggiungi la fonte o il risultato mancante |

**Usa una nuova estrazione per un ripristino sicuro.** Salva gli appunti fuori dal laboratorio, elimina solo la copia estratta usa e getta ed estrai di nuovo lo ZIP originale. Non usare un ripristino Git generale in un repository con lavoro da conservare.

## Verifica 7: Consegna a una nuova sessione

**Scrivi un passaggio di meno di 180 parole** fuori dalla cartella del laboratorio. Includi revisione del requisito, file modificati, comando e risultato esatti del test, output testuale e JSON, controlli degli input non validi, registro d’uso e prossima azione. Apri una nuova sessione e chiedile di identificare le chiavi JSON e dire se la funzione ha superato i controlli.

**Risposta attesa:** la nuova sessione nomina `total` e `by_status`, indica la revisione 1, riporta solo verifiche osservate e segnala eventuali controlli mancanti.

## Soluzione e griglia di valutazione

**Una implementazione valida** è riportata sotto. Salva il primo blocco come `task_report.py` e il secondo come `tests/test_task_report.py` in una nuova estrazione del laboratorio. Lascia invariati `tasks.json` e i due file dei requisiti. Esegui i controlli del checkpoint 6. Confronta un’altra soluzione con il requisito e il comportamento osservato.

`task_report.py`:

```python
"""Stampa un conteggio testuale o un riepilogo JSON delle attività del workshop."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="Rapporto delle attività del workshop")
    parser.add_argument("path", type=Path, help="percorso all’elenco JSON delle attività")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Controlli per i rapporti testuali e JSON delle attività del workshop."""

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


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Ripristina dopo la soluzione:** salva gli appunti fuori dal laboratorio, elimina questa copia estratta ed estrai di nuovo il laboratorio iniziale originale. La nuova copia contiene i due test di base e nessuna implementazione della funzione.

**Assegna un punto per ogni checkpoint** della tabella sopra. Sette punti completano il percorso connesso se la voce della fonte esterna include una chiamata MCP reale e la riga del worker documenta una sessione reale. Sette punti completano il percorso di studio se la fonte è una pagina browser verificata e i passaggi degli strumenti sono indicati esplicitamente come non eseguiti. L’assenza di un controllo su comportamento, fonte o ambito dei file blocca entrambi i percorsi.

## Verifica la comprensione

1. **Quale requisito controlla questa funzione?** `docs/capstone-requirements.md`, revisione 1. Il requisito precedente sul filtro di stato appartiene alla lezione 5.
2. **Cosa prova il contratto JSON?** Analizza l’output del comando, confronta valori numerici e conteggi di ogni stato, e verifica input vuoti e non validi. Un riepilogo ben scritto dell’agente non basta.

## Risoluzione dei problemi

- **I test di base falliscono prima della modifica:** ripristina il laboratorio dallo ZIP e ripeti la configurazione.
- **L’agente modifica un altro file:** esamina il diff e ripristina solo la modifica indesiderata del laboratorio.
- **La connessione MCP non riesce:** usa la fonte browser e indica il checkpoint come percorso di studio.
- **Il worker ripete un valore errato:** rileggi il requisito del capstone e correggi il rapporto.
- **Il budget dei tentativi termina:** conserva il registro dell’errore e chiedi a un revisore umano il passo successivo.

## Passi successivi

**Salva il registro delle prove completato.** Per la pubblicazione avanzata in team e l’autorità tra sistemi, prosegui con il [Corso sull’implementazione della collaborazione IA](/ai-collaboration-course-start/).

**Navigazione del corso:** [Precedente obbligatoria: cicli delimitati](/articles/effective-ai-bounded-agent-loops/), [Facoltativa: valutazione degli agenti specializzati](/articles/effective-ai-specialized-agent-evaluation/), [Indice del corso](/effective-ai-course-start/).
