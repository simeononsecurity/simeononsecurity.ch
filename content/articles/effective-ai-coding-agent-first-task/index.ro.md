---
title: "Execută prima ta sarcină de repository cu un agent de programare"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Alege o interfață pentru agentul de programare, deschide un repository demonstrativ, examinează o modificare propusă și rulează verificările înainte de a o păstra."
genre: ["Inteligență artificială", "Inginerie software"]
tags: ["tutorial Codex CLI", "aplicația Codex", "Claude Code CLI", "tutorial OpenCode", "flux de lucru cu agenți de programare", "instrumente de programare AI"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Un repository de cod cu vizualizări separate ale agentului în terminal și pe desktop, lângă un diff revizuit"
coverCaption: ""
---

[Înapoi la cursul Flux de lucru practic cu AI](/effective-ai-course-start/)

**Un agent de programare citește fișiere, propune modificări și rulează instrumente într-un spațiu de lucru.** În această lecție vei rezolva o sarcină mică într-un repository. Alege Codex din aplicația desktop ChatGPT sau din CLI, Claude Code CLI ori OpenCode TUI. Apoi examinează modificarea înainte să o accepți.

**Obiectiv de învățare:** vei rula sau vei aplica manual o modificare bine delimitată și îi vei verifica diff-ul și comportamentul.

## Idei principale

- **Codex în aplicația desktop ChatGPT** oferă un spațiu vizual pentru sarcini și revizuirea lor.
- **Codex CLI** pornește o sesiune Codex din terminal.
- **Claude Code CLI** rulează fluxul de programare Claude din terminal.
- **OpenCode TUI** oferă un flux de programare în terminal cu furnizori și permisiuni configurabile.
- **Un diff și rezultatul unui test** contează mai mult decât mesajul asistentului că a terminat.

## Înainte să începi

**Condiții prealabile:** finalizează [configurarea cursului](/articles/effective-ai-course-setup/), inclusiv rularea de bază și instantaneul Git local. Înaintea acestei lecții, parcurge [contextul repository-ului](/articles/effective-ai-agents-md-context/) și [pachetele de sarcini](/articles/effective-ai-task-packets/). Folosește un agent de programare la care ai acces autorizat. Rezervă 45 de minute. Dificultatea este de la începător la intermediar.

**Folosește [laboratorul de pornire al cursului](/downloads/effective-ai-course-lab.zip)** într-un folder temporar. Arhiva conține un program mic pentru raportarea sarcinilor, date de probă și teste. Nu folosi un repository de producție pentru prima modificare. Adaugă filtrul `--status` și păstrează numărul total existent.

## Parcurs de studiu fără agent de programare

**Cere unui asistent de chat să propună aceeași modificare** dacă nu ai un agent de programare. Lipește doar `docs/requirements.md`, `task_report.py` și fișierul de test specific din laboratorul sintetic. Cere un diff unificat și o explicație scurtă. Un diff unificat marchează liniile vechi cu `-` și liniile noi cu `+`. Deschide fișierul indicat într-un editor de text, înlocuiește liniile vechi cu propunerea și salvează. Apoi rulează toate comenzile din secțiunea Examinează rezultatul. Lasă `tasks.json` neschimbat. Notează că nu ai rulat pasul cu agentul. Proiectul final conține o funcție JSON separată, deci compară soluția filtrului cu cerința și verificările din lecția 5.

## Alege o interfață

**Alege mai întâi suprafața de revizuire.** Codex în aplicația desktop ChatGPT se potrivește proiectelor vizuale și revizuirii diff-urilor. O interfață de terminal se potrivește lucrului din folderul laboratorului extras. Compară opțiunile de terminal între ele:

| Instrument de terminal | Verificarea contului sau furnizorului | Comandă de pornire |
|---|---|---|
| **Codex CLI** | Confirmă conectarea la Codex și permisiunile locale | `codex` |
| **Claude Code CLI** | Confirmă accesul la Claude Code și permisiunile locale | `claude` |
| **OpenCode TUI** | Configurează un furnizor de modele acceptat și permisiunile | `opencode` |

**Instalează și autentifică-te folosind ghidul oficial actual** al instrumentului ales. Citește [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [aplicația desktop ChatGPT](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) sau [OpenCode](https://opencode.ai/docs/). Comenzile, platformele acceptate și condițiile conturilor se schimbă. Lecția folosește doar numele stabile de lansare și o procedură comună de revizuire.

**Pentru o alegere mai detaliată a produsului,** citește comparația site-ului pentru [agenții de programare CLI](/articles/cli-coding-agents-comparison/) sau [agenții cu interfață grafică](/articles/gui-coding-agents-comparison/). Ghidurile pentru [Codex CLI și desktop](/articles/codex-cli-vs-desktop/), [Claude Code CLI și desktop](/articles/claude-code-cli-vs-desktop/) și [OpenCode CLI și desktop](/articles/opencode-cli-vs-desktop/) compară interfețele fiecărui produs.

**Începe din folderul laboratorului.** Fiecare interfață cere să alegi explicit spațiul de lucru:

1. **Codex desktop:** deschide aplicația desktop ChatGPT, selectează laboratorul extras ca proiect local și pornește o sarcină locală în acel proiect. Verifică ruta folderului și solicitările de aprobare înainte de modificări. O sarcină găzduită folosește o copie separată a spațiului de lucru.
2. **Codex CLI:** rulează `cd /path/to/effective-ai-course-lab`, apoi `codex`. Confirmă folderul de lucru afișat și modul de aprobare.
3. **Claude Code CLI:** rulează aceeași comandă `cd`, apoi `claude`. Confirmă folderul proiectului și permisiunile instrumentelor.
4. **OpenCode TUI:** rulează aceeași comandă `cd`, apoi `opencode`. Confirmă furnizorul selectat, proiectul și setările permisiunilor.

**ChatGPT chat și Claude Projects gestionează conversații și fișiere de referință partajate.** Codex și Claude Code lucrează într-un spațiu de cod cu instrumente pentru fișiere și comenzi. OpenCode oferă și interfețe desktop și IDE, dar lecția folosește terminalul. Furnizorul, contul și execuția locală sau găzduită diferă. Notează interfața aleasă în loc să tratezi toate sesiunile ca aceeași rulare.

**Verifică cinci detalii înainte să deschizi laboratorul:** sistemul de operare acceptat, autentificarea, costul furnizorului sau contului, permisiunile pentru fișiere și comenzi și dacă execuția are loc local sau pe un gazdă la distanță. Notează alegerea. Nu presupune că aplicația desktop și instrumentul de terminal folosesc același spațiu de lucru.

## Examinează proiectul inițial

**Redeschide folderul curat al laboratorului** din lecția despre contextul repository-ului. Această copie include `AGENTS.md` confirmat și instrucțiunile opționale din `CLAUDE.md`. Examinează fișierele înainte să ceri agentului o modificare. Rulează testele de bază din acest folder.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Rezultat de bază așteptat:** raportul afișează `Total tasks: 4`. Rularea testelor numește două teste și se încheie cu `OK`. Dacă vreun test eșuează, oprește-te și inspectează fișierele extrase. Nu atribui agentului repararea unui punct de pornire defect.

**Folosește instantaneele Git locale** din configurarea cursului și lecția despre contextul repository-ului. `AGENTS.md` și `CLAUDE.md` opțional ar trebui să fie deja confirmate. Rulează `git status --short` înaintea modificării și așteaptă-te să nu apară fișiere. Nici agentul nu trebuie să facă un commit. Arhiva nu include istoric Git. Fișierul `.gitignore` exclude bytecode-ul Python generat la rularea testelor. Dacă ai extras o copie nouă, repetă configurarea și lecția de context în acel folder. Confirmă fișierele de instrucțiuni înainte să modifici funcția. Inițializează și confirmă mai întâi proiectul inițial:

```bash
git init
git add .
git commit -m "Baza laboratorului cursului"
```

**Apoi adaugă `AGENTS.md` și `CLAUDE.md` opțional** cu sursa aprobată și comanda de test din lecția de context. Confirmă aceste fișiere, verifică un `git status --short` curat și începe modificarea funcției. Rulează comenzile în folderul de practică extras, nu în rădăcina altui repository.

## Formulează o solicitare limitată

**Deschide folderul laboratorului** în agentul ales. Trimite acest pachet de sarcină:

```text
Adaugă argumentul opțional --status la task_report.py.
Valori permise: open și done.
Dacă lipsește, păstrează neschimbată ieșirea actuală pentru numărul total.
Dacă este prezent, numără doar sarcinile potrivite și afișează Total tasks: N.
Adaugă teste pentru ambele valori, o valoare invalidă și ieșirea implicită neschimbată.
Nu modifica tasks.json sau fișiere fără legătură.
Rulează testele și raportează comanda exactă și rezultatul.
Oprește-te după cod și teste. Nu crea commit și nu face push.
```

**În Windows,** înlocuiește `python3` cu comanda `py -3` verificată la configurare, inclusiv în instrucțiunile salvate și pachetul de sarcină.

**Cere un plan scurt înainte de editare** dacă nu cunoști codul. Permite agentului să editeze doar folderul temporar al laboratorului. Controalele de permisiuni diferă între instrumente, așa că verifică setările actuale înainte de a permite comenzi shell sau scrierea fișierelor.

## Examinează rezultatul

**Citește diff-ul.** Verifică dacă ieșirea fără filtru rămâne neschimbată, filtrul acceptă doar două valori și testele acoperă eroarea și ieșirea implicită neschimbată. Testele reușite confirmă modificarea doar dacă verifică comportamentul cerut.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Rezultate așteptate:** primele trei comenzi de raport afișează 4, 2 și 2. Valoarea invalidă afișează o eroare clară și procesul se încheie cu un cod diferit de zero. Textul exact depinde de implementare. Pe macOS sau Linux, rulează `echo $?` imediat după comanda invalidă pentru codul de ieșire. În PowerShell, verifică `$LASTEXITCODE`.

| Dovadă | Ce verifici |
|---|---|
| **Lista fișierelor** | S-au schimbat doar programul și testele |
| **Diff** | Logica filtrului corespunde solicitării |
| **Rezultatul testelor** | Noile cazuri au fost rulate și au trecut |
| **Rulare manuală** | Numerele implicite, `open` și `done` corespund cu `tasks.json` |

**Dacă agentul raportează rezultatul fără să ruleze testele,** execută tu comanda. Dacă modificarea depășește pachetul, cere o corecție limitată. Dacă starea nu este clară, șterge copia de practică extrasă și extrage din nou arhiva ZIP originală.

## Răspunsuri pentru traseul de studiu

**Folosește aceste fișiere complete dacă patch-ul manual eșuează.** Începe cu un laborator extras din nou, salvează primul bloc ca `task_report.py` și al doilea ca `tests/test_task_report.py`, apoi rulează comenzile din Examinează rezultatul. Lasă `tasks.json` și `docs/requirements.md` neschimbate. Notează eșecul inițial înainte de copiere.

`task_report.py`:

```python
"""Afișează numărul sarcinilor dintr-un fișier JSON."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Numără toate sarcinile sau pe cele cu un statut permis."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Numără sarcinile atelierului")
    parser.add_argument("path", type=Path, help="cale către lista de sarcini JSON")
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
"""Teste pentru raportul de sarcini al atelierului."""

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

**Păstrează o copie editată cu testele filtrului reușite** pe durata lecțiilor despre context și verificarea rezultatelor. Dacă ai folosit soluția de mai sus pentru recuperare, păstrează copia nouă cu testele reușite pentru acele lecții. Ține diff-ul și raportul testelor în afara laboratorului. Revino la proiectul inițial înainte de lecția despre delegare sau șterge o încercare eșuată pentru a relua curat.

## Exersează și verifică

**Rezultatul tău:** un diff al laboratorului și o notă de revizuire în patru rânduri despre fișierele atinse, comportamentul implicit, filtrare și intrarea invalidă. Notează privat numele și versiunea instrumentului pentru a reproduce o problemă specifică versiunii.

**Raționament așteptat:** ai ales o interfață potrivită stilului tău de lucru, ai delimitat sarcina, ai examinat modificarea reală și ai executat o verificare independentă de raportul agentului.

## Verifică ce ai înțeles

1. **Întrebare:** Ce dovedește că filtrul de stare funcționează? **Răspuns:** Un diff limitat, teste reușite și rezultate observate pentru ieșirea implicită, open, done și cazul invalid.
2. **Întrebare:** Mesajul agentului că a rulat testele constituie rezultatul tău? **Răspuns:** Nu. Rulează comanda sau examinează ieșirea testelor.

## Depanare

- **Comandă lipsă:** finalizează instalarea urmând ghidul furnizorului și redeschide terminalul.
- **Nu poți accesa fișiere:** deschide folderul laboratorului extras și verifică permisiunile spațiului de lucru.
- **S-au schimbat fișiere neașteptate:** oprește-te și examinează `git status --short` înaintea unei alte solicitări.
- **Testele trec, dar comportamentul este greșit:** adaugă un caz manual sau un test pentru cerința lipsă.

## Pașii următori

**Continuă cu [Ferestre de context și predări](/articles/effective-ai-context-window-management/)**. Vei păstra o înregistrare utilă pentru o sesiune nouă.

**Navigarea cursului:** [Anterior: Pachete de sarcini](/articles/effective-ai-task-packets/), [Programa cursului](/effective-ai-course-start/).
