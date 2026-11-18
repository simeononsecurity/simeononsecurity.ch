---
title: "Cicli delimitati per agenti IA: controlli, nuovi tentativi e regole di arresto"
date: 2026-10-10
lastmod: 2026-11-14
toc: true
draft: false
description: "Definisci un ciclo obiettivo per l'IA con stato osservabile, controlli, limiti ai nuovi tentativi, condizioni di arresto e un chiaro passaggio a una persona."
genre: ["Intelligenza artificiale", "Ingegneria del software", "Produttività"]
tags: ["cicli obiettivo IA", "ciclo di nuovo tentativo dell'agente", "regole di arresto per l'automazione IA", "monitoraggio degli agenti", "passaggio umano dell'IA", "flusso di lavoro IA delimitato"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "Un piccolo ciclo di agente passa da una modifica a un test, a una decisione di nuovo tentativo e al passaggio a una persona"
coverCaption: ""
---

[Torna al corso pratico sui flussi di lavoro IA](/effective-ai-course-start/)

**Un ciclo orientato a un obiettivo ripete il lavoro finché un risultato definito supera un controllo o scatta una regola di arresto.** Un ciclo utile legge lo stato corrente, esegue un'azione delimitata, controlla il risultato e registra ciò che è accaduto. Un'istruzione aperta come «continua a provare» non ha una regola di completamento affidabile.

**Obiettivo di apprendimento:** eseguirai un ciclo di laboratorio delimitato con un controllo che si sa essere fallito e registrerai la decisione di arresto.

## Punti chiave

- **Obiettivo:** un risultato descritto in termini osservabili.
- **Stato:** i file, gli output, gli errori e la revisione del codice sorgente correnti.
- **Controllo:** un test o una revisione legati all'obiettivo.
- **Budget di nuovi tentativi:** il numero massimo di tentativi consentiti per un errore.
- **Regola di arresto:** una condizione che richiede di concludere o chiedere una decisione umana.

## Prima di iniziare

**Prerequisiti:** il [pacchetto dell'attività](/articles/effective-ai-task-packets/), il [registro di verifica](/articles/effective-ai-output-verification/) e la [lezione sulla delega](/articles/effective-ai-agent-delegation/). Dedica 45 minuti. La difficoltà è intermedia. Usa una copia nuova del laboratorio sintetico, così il primo controllo fallito è noto in anticipo.

## Scrivi il contratto del ciclo

**Per la richiesta del filtro per stato**, definisci il contratto prima di qualsiasi nuovo tentativo:

```text
Obiettivo: supportare --status open|done senza modificare l’output predefinito.
Fonte: docs/requirements.md, revisione 1.
File consentiti: task_report.py e test mirati.
Controlli: test unitari, conteggi 4/2/2, valore non valido con codice di uscita diverso da zero.
Budget dei nuovi tentativi: al massimo due modifiche dopo il primo tentativo.
Interrompi subito: conflitto nella fonte, modifica imprevista di un file, esposizione di un segreto,
o errore di base non correlato a questa richiesta.
Consegna: riporta la differenza finale, i comandi, gli output, i tentativi e il problema irrisolto.
```

**Il budget è una regola dell'attività**, non un'impostazione predefinita del prodotto. Due nuovi tentativi bastano per diagnosticare una piccola attività di laboratorio senza nascondere gli errori ripetuti. Un'attività di produzione richiede una propria scelta su rischio e revisione.

## Usa una tabella dello stato

| Passaggio | Stato da registrare | Decisione |
|---|---|---|
| **Leggi** | Revisione del codice sorgente e risultato iniziale | Fermati se lo stato iniziale è diverso |
| **Agisci** | File modificati e azione eseguita | Rifiuta le modifiche fuori ambito |
| **Controlla** | Test esatto e output manuale | Accetta o diagnostica |
| **Riprova** | Causa dell'errore e nuova ipotesi | Continua solo entro il budget |
| **Passa il testimone** | Stato finale e responsabile successivo | Fermati dopo il superamento o il blocco |

**Registra i tentativi, non solo l'ultimo messaggio.** Un test che passa dopo tre modifiche non registrate non spiega che cosa sia cambiato. Mantieni un breve registro dell'errore, dell'ipotesi rivista e delle nuove prove.

## Analizza un errore

**Esempio di primo tentativo:** l'agente aggiunge il filtro e i test. `open` restituisce 2, ma `--status invalid` restituisce 0 e termina con successo. Il requisito richiede un codice di uscita diverso da zero per un valore non valido. Segna il controllo come fallito.

**Diagnosi:** esamina la convalida degli argomenti. L'agente ha trattato un valore sconosciuto come una corrispondenza vuota invece che come un errore. Chiedi una correzione delimitata che convalidi i valori accettati prima del conteggio. Ripeti il caso non valido e tutti i controlli precedenti.

```text
Tentativo 1: lo stato non valido ha restituito successo, quindi l’accettazione è fallita.
Causa individuata: manca la convalida dei valori accettati.
Richiesta per il tentativo 2: rifiuta i valori non supportati e mantieni i conteggi 4/2/2.
Prove richieste: esecuzione completa dei test e stato di uscita del comando non valido.
```

**Risultato atteso al secondo tentativo:** un errore chiaro e un codice di uscita diverso da zero per `invalid`, con i conteggi validi invariati. Se il secondo tentativo fallisce ancora, usa l'ultimo solo dopo aver indicato una nuova causa. Ripetere la stessa richiesta non è una diagnosi.

## Gestisci i risultati ambigui

**Un processo che si ferma senza un risultato non ha avuto successo.** Se uno strumento scade dopo una possibile scrittura, controlla i file e lo stato Git prima di eseguirlo di nuovo. Se un servizio collegato segnala un esito sconosciuto, leggi lo stato corrente prima di ripetere un'azione esterna. Fuori dal laboratorio, invii, pubblicazioni o scritture duplicate sono un rischio concreto.

**Fermati per una revisione umana** se il requisito è in conflitto con un'altra fonte approvata, un'autorizzazione blocca l'azione, il budget di nuovi tentativi è esaurito o l'azione richiesta supera un limite di pubblicazione. Il passaggio deve indicare lo stato esatto e la decisione ancora necessaria.

## Separa i cicli dai monitor

**Un ciclo di modifica** si svolge nell'ambito di un'attività delimitata e controlla il risultato dopo ogni azione. **Un monitor pianificato** si attiva più tardi per esaminare una condizione. Un monitor richiede una propria frequenza, soglia di cambiamento, regola di notifica e condizione di arresto. Non trasformare il ciclo di modifica del laboratorio in un'attività ricorrente. La lezione successiva valuta i sistemi persistenti prima di attivarli.

## Esegui un ciclo controllato

**Inizia con il laboratorio intatto.** I suoi due test iniziali passano. Nella nuova estrazione, crea `tests/test_loop_contract.py` con il controllo seguente. Questo file definisce una funzionalità desiderata che manca nel progetto iniziale. Non fa parte dello ZIP iniziale mantenuto.

```python
"""Un controllo fallito controllato per l’esercizio sul filtro di stato."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LoopContractTests(unittest.TestCase):
    def test_open_status_count(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"),
             str(ROOT / "tasks.json"), "--status", "open"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Total tasks: 2")


if __name__ == "__main__":
    unittest.main()
```

**Esegui `python3 -m unittest discover -s tests -v`.** I due test originali dovrebbero passare e il nuovo test contrattuale dovrebbe fallire perché il progetto iniziale non supporta `--status`. Registra l'errore effettivo. Se hai inizializzato Git come indicato nella lezione 0, registra anche `git status --short`. Altrimenti, confronta i file modificati con un'estrazione intatta. Su Windows, usa `py -3` se la configurazione usa il launcher.

**Imposta un budget di tre tentativi:** la prima modifica e al massimo due correzioni. Fornisci all'agente il contratto del ciclo qui sopra e chiedi una modifica delimitata. Dopo ogni tentativo, controlla i file modificati, riesegui tutti i test e prova i comandi predefinito, `open`, `done` e valore non valido. Registra la causa dell'errore prima di un altro tentativo. Fermati se un test passa, se fallisce una condizione iniziale non collegata alla richiesta, se c'è una modifica fuori ambito o dopo il terzo tentativo fallito.

**Percorso di studio:** dopo aver registrato il test rosso, applica la [soluzione completa della lezione 5](/articles/effective-ai-coding-agent-first-task/) in questa copia nuova. Riesegui gli stessi controlli e registra che la modifica dell'agente non è stata eseguita. Conserva il test contrattuale controllato. Non indebolirlo né eliminarlo per farlo passare.

| Tentativo | Stato e osservazione | Decisione |
|---|---|---|
| **Prima della modifica** | I due test iniziali passano, il nuovo controllo `open` fallisce | Procedi con una modifica delimitata |
| **Dopo ogni modifica** | Registra test esatti, conteggi, codice di uscita non nullo per il valore non valido e file modificati | Accetta, diagnostica o fermati |
| **Alla fine del budget** | Registra l'errore residuo e la differenza corrente | Passa il testimone senza un altro tentativo |

## Esercitati e verifica

**Il tuo artefatto:** il test controllato che fallisce, gli output osservati prima e dopo, un registro dei tentativi e una decisione finale di accettazione o arresto. Se la prima modifica passa, registra un solo tentativo. Non inventare un secondo errore per riempire il registro.

**Verifica di completamento:** il contratto indica una fonte, l'ambito dei file, controlli osservabili, il limite di nuovi tentativi, almeno una condizione di arresto immediato e un passaggio di consegne. Il registro include il vero test rosso, i risultati dei controlli successivi e un esito positivo o un arresto dovuto al budget. Un secondo tentativo indica una causa nuova ed è diverso dal primo.

## Verifica la comprensione

1. **Domanda:** che cosa dimostra il primo test contrattuale rosso? **Risposta:** il progetto iniziale non include il filtro di stato richiesto, come dimostra un test scritto prima della modifica.
2. **Domanda:** quando il ciclo deve fermarsi anche se restano tentativi? **Risposta:** in caso di modifica fuori ambito, autorizzazione poco chiara o requisito in conflitto.

## Risoluzione dei problemi

- **Il ciclo ripete lo stesso errore:** fermati e formula una nuova ipotesi sulla causa.
- **I controlli si indeboliscono:** ripristina i criteri di accettazione originali.
- **Esito esterno incerto:** controlla lo stato corrente prima di un nuovo tentativo.
- **Budget esaurito:** passa il registro degli errori invece di nasconderli.

## Prossimi passi

Continua con la lezione opzionale [Valutazione degli agenti specializzati](/articles/effective-ai-specialized-agent-evaluation/) oppure passa direttamente al [progetto finale del corso sui flussi di lavoro IA](/articles/effective-ai-capstone/). Per altre opzioni di runtime, leggi la [guida agli ambienti per agenti](/articles/best-ai-agent-harnesses/).

**Navigazione del corso:** [Precedente: delega degli agenti](/articles/effective-ai-agent-delegation/), [Programma del corso](/effective-ai-course-start/).
