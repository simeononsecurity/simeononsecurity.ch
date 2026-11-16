---
title: "Executa la teva primera tasca de repositori amb un agent de programació"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Tria una interfície d’agent de programació, obre un repositori de mostra, revisa un canvi proposat i executa comprovacions abans de conservar-lo."
genre: ["Intel·ligència artificial", "Enginyeria del programari"]
tags: ["guia de Codex CLI", "aplicació Codex", "Claude Code CLI", "guia d’OpenCode", "flux de treball amb agents de programació", "eines de programació amb IA"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Un repositori de codi amb vistes separades de l’agent al terminal i a l’escriptori, al costat d’un diff revisat"
coverCaption: ""
---

[Torna al curs de Flux de treball pràctic amb IA](/effective-ai-course-start/)

**Un agent de programació llegeix fitxers, proposa canvis i executa eines dins d’un espai de treball.** En aquesta lliçó faràs una tasca petita en un repositori. Tria Codex a l’aplicació d’escriptori o a la CLI de ChatGPT, Claude Code CLI o OpenCode TUI. Després revisa un canvi abans d’acceptar-lo.

**Objectiu d’aprenentatge:** executaràs o aplicaràs manualment un canvi acotat i en verificaràs el diff i el comportament.

## Idees clau

- **Codex a l’aplicació d’escriptori de ChatGPT** ofereix un espai visual per a tasques i revisions.
- **Codex CLI** inicia una sessió de Codex des del terminal.
- **Claude Code CLI** executa el flux de programació de Claude des del terminal.
- **OpenCode TUI** ofereix un flux de terminal amb proveïdors i permisos configurables.
- **Un diff i el resultat d’una prova** són més importants que el missatge de finalització de l’assistent.

## Abans de començar

**Requisits previs:** completa la [configuració del curs](/articles/effective-ai-course-setup/), incloses l’execució de referència i la instantània local de Git. Completa [el context del repositori](/articles/effective-ai-agents-md-context/) i els [paquets de tasques](/articles/effective-ai-task-packets/) abans d’aquesta lliçó. Fes servir un agent de programació al qual tinguis accés autoritzat. Reserva 45 minuts. La dificultat va de principiant a intermèdia.

**Fes servir el [laboratori inicial del curs](/downloads/effective-ai-course-lab.zip)** en una carpeta prescindible. L’arxiu conté un programa petit d’informes de tasques, dades de mostra i proves. No facis servir un repositori de producció per al primer canvi. Afegeix un filtre `--status` i conserva el recompte total actual.

## Ruta d’estudi sense agent

**Demana a un assistent de xat que proposi el mateix canvi** si no tens un agent de programació. Enganxa només `docs/requirements.md`, `task_report.py` i el fitxer de prova específic del laboratori sintètic. Demana un diff unificat i una explicació breu. Un diff unificat marca les línies antigues amb `-` i les noves amb `+`. Obre el fitxer indicat en un editor de text, substitueix les línies antigues per la proposta i desa’l. Després executa totes les ordres de Revisar el resultat. Deixa `tasks.json` sense canvis. Anota que no has executat el pas amb l’agent. El projecte final té una funció JSON independent, així que compara la solució del filtre amb el requisit i les comprovacions de la lliçó 5.

## Tria una interfície

**Tria primer una superfície de revisió.** Codex a l’aplicació d’escriptori de ChatGPT és adequat per a un projecte visual i per revisar diffs. Una interfície de terminal és adequada per treballar des de la carpeta extreta del laboratori. Compara les opcions de terminal entre elles:

| Eina de terminal | Comprovació del compte o proveïdor | Ordre d’inici |
|---|---|---|
| **Codex CLI** | Confirma l’inici de sessió de Codex i els permisos locals | `codex` |
| **Claude Code CLI** | Confirma l’accés a Claude Code i els permisos locals | `claude` |
| **OpenCode TUI** | Configura un proveïdor de models compatible i els permisos | `opencode` |

**Instal·la l’eina i inicia sessió amb la guia oficial actualitzada.** Llegeix [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [l’aplicació d’escriptori de ChatGPT](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) o [OpenCode](https://opencode.ai/docs/). Les ordres, plataformes compatibles i requisits del compte canvien. Aquesta lliçó fa servir només els noms d’inici estables i un procediment de revisió comú.

**Per triar millor el producte,** llegeix la comparació d’[agents de programació CLI](/articles/cli-coding-agents-comparison/) o d’[agents amb interfície gràfica](/articles/gui-coding-agents-comparison/). Les guies de [Codex CLI i escriptori](/articles/codex-cli-vs-desktop/), [Claude Code CLI i escriptori](/articles/claude-code-cli-vs-desktop/) i [OpenCode CLI i escriptori](/articles/opencode-cli-vs-desktop/) comparen les interfícies de cada producte.

**Comença a la carpeta del laboratori.** Cada interfície exigeix triar explícitament un espai de treball:

1. **Codex d’escriptori:** obre l’aplicació d’escriptori de ChatGPT, selecciona el laboratori extret com a projecte local i inicia-hi una tasca local. Comprova el camí de la carpeta i les sol·licituds d’aprovació abans de fer canvis. Una tasca allotjada fa servir una còpia separada de l’espai de treball.
2. **Codex CLI:** executa `cd /path/to/effective-ai-course-lab` i després `codex`. Confirma la carpeta de treball mostrada i el mode d’aprovació.
3. **Claude Code CLI:** executa la mateixa ordre `cd` i després `claude`. Confirma la carpeta del projecte i els permisos de les eines.
4. **OpenCode TUI:** executa la mateixa ordre `cd` i després `opencode`. Confirma el proveïdor triat, el projecte i els permisos.

**ChatGPT chat i Claude Projects gestionen converses i fitxers de referència compartits.** Codex i Claude Code treballen en un espai de codi amb eines per a fitxers i ordres. OpenCode també ofereix superfícies d’escriptori i IDE, però aquesta lliçó fa servir el terminal. El proveïdor, el compte i l’execució local o allotjada varien. Anota la superfície escollida en lloc de tractar totes les sessions com una mateixa execució.

**Comprova cinc detalls abans d’obrir el laboratori:** sistema operatiu compatible, autenticació, cost del proveïdor o del compte, permisos de fitxers i ordres, i si l’execució és local o en un host remot. Anota la tria. No pressuposis que una aplicació d’escriptori i una eina de terminal fan servir el mateix espai de treball.

## Inspecciona el projecte inicial

**Torna a obrir la carpeta neta del laboratori** de la lliçó sobre context del repositori. Aquesta còpia conté el teu `AGENTS.md` confirmat i les instruccions opcionals de `CLAUDE.md`. Revisa els fitxers abans de demanar un canvi a l’agent. Executa les proves de referència des d’aquesta carpeta.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Resultat inicial esperat:** l’informe mostra `Total tasks: 4`. La prova anomena dues proves i acaba amb `OK`. Si alguna falla, atura’t i inspecciona els fitxers extrets. No atribueixis a l’agent la reparació d’un punt de partida defectuós.

**Fes servir les instantànies locals de Git** de la configuració del curs i de la lliçó sobre el context del repositori. `AGENTS.md` i el `CLAUDE.md` opcional ja haurien d’estar confirmats. Executa `git status --short` abans del canvi i espera que no mostri cap fitxer. L’agent tampoc no ha de fer cap commit. L’arxiu no conté historial de Git. El seu fitxer `.gitignore` exclou el bytecode de Python que generen les proves. Si has extret una còpia nova, repeteix-hi la configuració del curs i la lliçó de context. Confirma els fitxers d’instruccions abans del canvi. Inicialitza i confirma primer el projecte inicial:

```bash
git init
git add .
git commit -m "Base del laboratori del curs"
```

**Després afegeix `AGENTS.md` i el `CLAUDE.md` opcional** amb la font i l’ordre de prova aprovades a la lliçó de context. Confirma aquests fitxers, comprova que `git status --short` sigui net i comença el canvi. Executa aquestes ordres a la carpeta de pràctica extreta, no a l’arrel d’un altre repositori.

## Dona una petició acotada

**Obre la carpeta del laboratori** a l’agent de programació escollit. Envia aquest paquet de tasques:

```text
Afegeix un argument opcional --status a task_report.py.
Valors permesos: open i done.
Si falta, conserva la sortida actual del recompte total.
Si hi és, compta només les tasques coincidents i mostra Total tasks: N.
Afegeix proves per als dos valors, un valor no vàlid i la sortida predeterminada inalterada.
No canviïs tasks.json ni fitxers no relacionats.
Executa les proves i informa de l’ordre i el resultat exactes.
Atura’t després del codi i les proves. No facis commit ni push.
```

**A Windows,** substitueix `python3` per l’ordre `py -3` verificada durant la configuració, també a les instruccions desades del repositori i al paquet de tasques.

**Demana un pla breu abans d’editar** si encara no coneixes el codi. Autoritza l’agent a editar només la carpeta prescindible del laboratori. Els controls de permisos varien segons l’eina. Revisa’n la configuració actual abans de permetre ordres de shell o escriptura de fitxers.

## Revisa el resultat

**Llegeix el diff.** Comprova que la sortida sense filtre continuï igual, que el filtre accepti només dos valors i que les proves cobreixin l’error i la sortida predeterminada inalterada. Les proves aprovades confirmen el canvi només si comproven el comportament sol·licitat.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Resultats esperats:** les tres primeres ordres d’informe mostren 4, 2 i 2. El valor no vàlid mostra un error clar i acaba amb un codi diferent de zero. El text concret depèn de la implementació. A macOS o Linux, executa `echo $?` immediatament després de l’ordre no vàlida per llegir-ne el codi de sortida. A PowerShell, comprova `$LASTEXITCODE`.

| Evidència | Què cal inspeccionar |
|---|---|
| **Llista de fitxers** | Només han canviat el programa i les proves |
| **Diff** | La lògica del filtre coincideix amb la petició |
| **Resultats de les proves** | Els casos nous s’han executat i han passat |
| **Execució manual** | Els recomptes predeterminat, `open` i `done` coincideixen amb `tasks.json` |

**Si l’agent comunica un resultat sense executar les proves,** executa tu l’ordre. Si el canvi surt del paquet de tasques, demana una correcció acotada. Si l’estat no és clar, elimina la còpia de pràctica extreta i torna a extreure el ZIP original.

## Solucions de la ruta d’estudi

**Fes servir aquests fitxers complets si falla el teu pedaç manual.** Comença amb un laboratori acabat d’extreure, desa el primer bloc com a `task_report.py` i el segon com a `tests/test_task_report.py`, i executa les ordres de Revisar el resultat. Deixa `tasks.json` i `docs/requirements.md` intactes. Anota l’error inicial abans de copiar els fitxers.

`task_report.py`:

```python
"""Mostra el recompte de tasques d’un fitxer JSON."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Compta totes les tasques o les d’un estat permès."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compta les tasques del taller")
    parser.add_argument("path", type=Path, help="camí a la llista de tasques JSON")
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
"""Proves de l’informe de tasques del taller."""

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

**Conserva una còpia modificada amb les proves del filtre aprovades** per a les lliçons de context i verificació de resultats. Si has recuperat la feina amb aquesta solució, conserva la còpia nova amb les proves aprovades per a aquestes lliçons. Desa el diff i el registre de proves fora del laboratori. Restaura el projecte inicial abans de la lliçó de delegació o elimina un intent fallit per començar de nou.

## Practica i comprova

**El teu resultat:** un diff del laboratori i un registre de revisió de quatre files sobre l’abast dels fitxers, el comportament predeterminat, el comportament filtrat i l’entrada no vàlida. Anota el nom i la versió de l’eina en apunts privats per reproduir problemes específics d’una versió.

**Raonament esperat:** has triat una interfície adequada a la teva manera de treballar, has delimitat la tasca, has revisat el canvi real i has executat una comprovació independent del resum de l’agent.

## Comprova què has après

1. **Pregunta:** Què demostra que funciona el canvi al filtre d’estat? **Resposta:** Un diff acotat, proves aprovades i resultats observats per al cas predeterminat, open, done i l’entrada no vàlida.
2. **Pregunta:** El missatge de l’agent dient que ha executat les proves compta com el teu resultat? **Resposta:** No. Executa l’ordre o revisa la sortida de les proves.

## Resolució de problemes

- **Falta una ordre:** acaba la instal·lació amb la guia de l’empresa proveïdora i torna a obrir el terminal.
- **No tens accés als fitxers:** obre la carpeta extreta del laboratori i comprova els permisos de l’espai de treball.
- **S’han canviat fitxers inesperats:** atura’t i revisa `git status --short` abans d’una altra petició.
- **Les proves passen, però el comportament és incorrecte:** afegeix un cas manual o una prova per al requisit que falta.

## Passos següents

**Continua amb [Finestres de context i traspassos](/articles/effective-ai-context-window-management/)**. Conservaràs un registre útil per a una sessió nova.

**Navegació del curs:** [Anterior: Paquets de tasques](/articles/effective-ai-task-packets/), [Programa del curs](/effective-ai-course-start/).
