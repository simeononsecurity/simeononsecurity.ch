---
title: "Proiect final pentru fluxul de lucru AI: construiește și verifică un raport JSON"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Creează un raport JSON pentru sarcini, cu contextul proiectului, o solicitare clar delimitată pentru agent, teste independente, verificarea surselor și predarea către o sesiune nouă."
genre: ["Inteligență artificială", "Inginerie software", "Educație"]
tags: ["proiect final flux de lucru AI", "proiect cu agent de programare", "verificarea sarcinilor AI", "AGENTS.md", "exercițiu MCP", "predare către agent"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Sarcină software de atelier încheiată, cu fișiere sursă, rezultate de testare, revizuirea agentului și înregistrarea predării"
coverCaption: ""
---

[Înapoi la cursul Flux de lucru practic cu AI](/effective-ai-course-start/)

**Creează un format nou de ieșire și dovedește cum funcționează.** Mai devreme ai adăugat un filtru de stare. Acest proiect final pornește de la un laborator nou și adaugă un raport JSON pe care îl citește un alt program. Cerința nouă verifică dacă transferi fluxul de lucru la o altă funcție.

**Obiectiv de învățare:** vei livra un raport JSON verificat, o evidență a surselor și instrumentelor și o predare pe care o înțelege o sesiune nouă.

## Idei principale

- **O cerință separată** controlează funcția proiectului final.
- **Modificarea unui agent de programare** rămâne în fișierele indicate.
- **Verificările independente** determină acceptarea.
- **Predarea către o sesiune nouă** permite reconstruirea rezultatului.

## Înainte să începi

**Cerințe preliminare:** finalizează lecțiile 0–10, inclusiv contextul depozitului, prima sarcină de programare, MCP sau alternativa din browser, delegarea și ciclurile delimitate. Lecția 11 este opțională. Rezervă 90–120 de minute. Dificultate: medie.

**Folosește o extragere nouă** a [laboratorului inițial](/downloads/effective-ai-course-lab.zip). Rulează `python3 task_report.py tasks.json` și cele două teste de bază înainte de editare. În Windows, folosește `py -3` dacă ai configurat lansatorul Python. Creează o bază Git locală ca în configurarea cursului. Filtrul de stare din lecția 5 lipsește intenționat.

**Citește `docs/capstone-requirements.md`, revizia 1.** Cere `--format text|json`. Textul implicit rămâne `Total tasks: 4`. Ieșirea JSON conține un total numeric și numărul fiecărei stări din date. Testează o listă goală, o stare lipsă și un format nesuportat. Nu folosi `docs/requirements.md` ca autoritate pentru această funcție nouă.

**Alege traseul.** Traseul conectat folosește o modificare observată a unui agent de programare, un apel MCP real, doar pentru citire, și un worker nativ sau o sesiune separată. Traseul de studiu folosește un asistent de chat pentru a propune cod, o sursă din browser în loc de MCP și chat-uri separate drept workeri simulați. Marchează pașii indisponibili cu instrumente drept „neexecutați”. Ambele trasee cer teste locale și revizuirea fișierelor. Cheia de răspuns de mai jos oferă fișiere complete pentru recuperare. Salvează prima încercare în notițe înainte de a copia cheia într-o extragere nouă.

## Punctul de control 1: Brieful proiectului

**Deschide proiectul sintetic de atelier ChatGPT sau Claude.** Cere un proiect de memento în două propoziții. Verifică ora 19:00 în `approved-schedule.md`. Programul aprobat controlează mementoul. Cerința proiectului final controlează programul.

**Dovadă:** notează numele proiectului, revizia sursei, ora observată în proiect și orice corecție. Nu trimite mesajul.

## Punctul de control 2: Contextul depozitului

**Deschide laboratorul nou.** Creează un `AGENTS.md` scurt care indică `docs/capstone-requirements.md`, `task_report.py`, testele și comanda de test verificată la configurare. Dacă folosești Claude Code, importă fișierul comun din `CLAUDE.md`. Creează un commit uman de configurare pentru aceste fișiere de instrucțiuni, apoi confirmă că `git status --short` nu arată modificări. Agentul de programare nu trebuie să facă commit la modificarea funcției.

**Dovadă:** salvează harta și copia curată a instrucțiunilor. Notează cheile JSON și comportamentul la intrări nevalide din revizia 1. Dacă un chat anterior descrie filtrul de stare, tratează-l ca context pentru altă sarcină.

## Punctul de control 3: Sursa externă

**Traseu conectat:** folosește [serverul MCP OpenAI Docs cu acces doar pentru citire](https://learn.chatgpt.com/learn/docs-mcp) printr-un client acceptat. Cere unui instrument MCP instrucțiunile actuale pentru `AGENTS.md`. Notează numele instrumentului, URL-ul sursei și un punct relevant pentru laborator. Apoi elimină conexiunea de exercițiu.

**Traseu de studiu:** deschide în browser [documentația oficială `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Notează titlul, URL-ul și un punct relevant. Marchează căutarea și execuția MCP drept „neexecutate”.

**Dovadă:** o intrare de server configurată nu dovedește că a fost folosită. Traseul conectat cere un apel vizibil al instrumentului și conținut returnat din sursă.

## Punctul de control 4: Deleagă o verificare

**Cere unui worker cu acces doar la citire** să verifice `docs/capstone-requirements.md`, `task_report.py` și testele de bază. Cere un raport de cel mult cinci rânduri, cu verificările lipsă și căile fișierelor. În traseul de studiu, folosește un chat separat și marchează-l ca worker simulat.

**Rezultatul așteptat:** testele inițiale verifică totalul și o valoare JSON care nu este listă. Nu verifică ieșirea JSON, o listă goală, o stare lipsă sau un format invalid. Deschide singur fișierul de teste și verifică raportul. O verificare independentă scurtă este utilă deoarece criteriile diferă de cele din lecția 5.

**Dovadă:** păstrează raportul scurt și decizia de integrare într-o singură propoziție. Ține transcrierea workerului în afara jurnalului principal al sarcinii.

## Punctul de control 5: Cere modificarea

**Dă-i unui agent de programare** pachetul următor. În traseul de studiu, un asistent de chat propune un patch pe care îl aplici manual în laborator.

```text
Obiectiv: adaugă --format text|json după calea JSON.
Sursă: docs/capstone-requirements.md, revizia 1.
Fișiere permise: task_report.py și tests/test_task_report.py.
Păstrează: Total tasks: 4 ca ieșire implicită și tasks.json nemodificat.
JSON: un obiect cu total și numere by_status, fără text suplimentar pe stdout.
Verificări obligatorii: text implicit și explicit, JSON 4/2/2, listă goală,
stare lipsă, format invalid și testele de bază.
Oprește-te dacă: sursele se contrazic, eșuează un test de bază fără legătură sau modifici în afara domeniului.
Raport: fișiere schimbate, comenzi, ieșiri observate, problemă nerezolvată.
Nu face commit, push, publicare și nu trimite mesaje.
```

**Verifică planul** înainte de editare. Schema contează: `total` este un număr, nu șirul `"4"`. `by_status` include fiecare stare din intrare, inclusiv valori viitoare. Limitează modificările la laboratorul extras.

## Punctul de control 6: Testează și verifică

**Rulează singur aceste verificări.** În Windows, înlocuiește `python3` cu `py -3`. Ordinea exactă a cheilor JSON și spațiile nu contează. Analizează ieșirea ca JSON și compară tipurile valorilor.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Comportament așteptat:** testele trec. Ambele comenzi text afișează `Total tasks: 4`. Comanda JSON returnează un singur obiect cu `total` 4, `by_status.open` 2 și `by_status.done` 2. Formatul invalid se încheie cu un cod diferit de zero. Testele acoperă și o intrare goală și o sarcină fără `status` text. Citește ieșirea de eroare și codul de ieșire pentru aceste cazuri.

| Punct de control | Dovadă de reușită | Recuperare după eșec |
|---|---|---|
| **Brieful proiectului** | Mementoul indică ora 19:00 | Reîmprospătează sursa programului |
| **Harta depozitului** | Sunt menționate cerința și căile testelor | Corectează fișierele de instrucțiuni |
| **Sursa externă** | S-a citit MCP sau s-a notat alternativa din browser | Verifică legătura sau URL-ul |
| **Verificarea workerului** | Testele lipsă au fost confirmate în fișier | Corectează raportul workerului |
| **Domeniul fișierelor** | Doar programul și testele | Verifică fiecare schimbare nedorită |
| **Comportament** | Text, JSON, intrări goale și erori verificate | Diagnostichează o cauză și reîncearcă |
| **Predare** | O sesiune nouă reconstruiește starea | Adaugă sursa sau rezultatul lipsă |

**Folosește o extragere nouă pentru resetarea sigură.** Salvează notițele în afara laboratorului, șterge numai copia extrasă de unică folosință și extrage din nou arhiva ZIP originală. Nu folosi o resetare Git amplă într-un depozit cu lucru de păstrat.

## Punctul de control 7: Predarea către o sesiune nouă

**Scrie o predare de sub 180 de cuvinte** în afara directorului laboratorului. Include revizia cerinței, fișierele schimbate, comanda exactă de test și rezultatul, ieșirile text și JSON, verificările intrărilor invalide, jurnalul de utilizare și acțiunea rămasă. Deschide o sesiune nouă și cere-i să identifice cheile JSON și să spună dacă funcția a trecut.

**Răspuns așteptat:** sesiunea nouă numește `total` și `by_status`, indică revizia 1, raportează doar verificări observate și menționează orice control lipsă.

## Cheia de răspuns și grila de evaluare

**O implementare validă** este mai jos. Salvează primul bloc ca `task_report.py` și al doilea ca `tests/test_task_report.py` într-o extragere nouă a laboratorului. Lasă `tasks.json` și ambele fișiere cu cerințe neschimbate. Rulează verificările de la punctul 6. Compară altă soluție cu cerința și comportamentul observat.

`task_report.py`:

```python
"""Afișează un total text sau un rezumat JSON al sarcinilor atelierului."""

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
    parser = argparse.ArgumentParser(description="Raport pentru sarcinile atelierului")
    parser.add_argument("path", type=Path, help="calea către lista JSON de sarcini")
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
"""Verificări pentru rapoartele text și JSON ale sarcinilor atelierului."""

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

**Resetează după folosirea soluției:** salvează notițele în afara laboratorului, elimină copia extrasă și extrage din nou laboratorul inițial original. Noua copie conține cele două teste de bază și nu conține implementarea funcției.

**Acordă un punct pentru fiecare control** din tabel. Șapte puncte încheie traseul conectat dacă rândul sursei externe include un apel MCP real și rândul workerului documentează o sesiune reală. Șapte puncte încheie traseul de studiu dacă sursa este o pagină de browser verificată și pașii cu instrumente sunt marcați explicit drept neexecutați. Lipsa unei verificări a comportamentului, sursei sau domeniului fișierelor blochează ambele trasee.

## Verifică înțelegerea

1. **Care cerință controlează această funcție?** `docs/capstone-requirements.md`, revizia 1. Cerința anterioară privind filtrul de stare aparține lecției 5.
2. **Ce dovedește contractul JSON?** Analizează ieșirea comenzii, compară valorile numerice și numărul fiecărei stări și verifică intrările goale și invalide. Un rezumat elegant al agentului nu este suficient.

## Depanare

- **Testul de bază eșuează înainte de editare:** resetează laboratorul din ZIP și repetă configurarea.
- **Agentul schimbă alt fișier:** verifică diff-ul și restaurează numai schimbarea nedorită din laborator.
- **Conexiunea MCP eșuează:** folosește sursa din browser și marchează punctul drept traseu de studiu.
- **Workerul repetă o valoare greșită:** recitește cerința proiectului și corectează raportul.
- **Se termină limita de reîncercări:** păstrează jurnalul erorilor și cere unui evaluator uman pasul următor.

## Pașii următori

**Salvează evidența completă.** Pentru publicarea avansată în echipă și autoritatea între sisteme, continuă cu [Cursul de implementare a colaborării AI](/ai-collaboration-course-start/).

**Navigarea cursului:** [Precedenta obligatorie: cicluri delimitate](/articles/effective-ai-bounded-agent-loops/), [Opțională: evaluarea agenților specializați](/articles/effective-ai-specialized-agent-evaluation/), [Structura cursului](/effective-ai-course-start/).
