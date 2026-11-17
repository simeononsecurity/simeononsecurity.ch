---
title: "Projecte final del flux de treball amb IA: crea i verifica un informe JSON"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Crea un informe JSON amb context del projecte, una petició acotada per a l’agent, proves independents, revisió de les fonts i un traspàs a una sessió nova."
genre: ["Intel·ligència artificial", "Enginyeria del programari", "Educació"]
tags: ["projecte final de flux de treball amb IA", "projecte amb agent de programació", "verificació de tasques amb IA", "AGENTS.md", "pràctica de MCP", "traspàs entre agents"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Tasca de programari del taller completada amb fitxers de codi font, resultats de proves, revisió de l’agent i registre del traspàs"
coverCaption: ""
---

[Torna al curs de flux de treball pràctic amb IA](/effective-ai-course-start/)

**Crea un format de sortida nou i demostra com funciona.** Abans vas afegir un filtre d’estat. Aquest projecte final comença en un laboratori nou i afegeix un informe JSON perquè el llegeixi un altre programa. El requisit nou comprova si trasllades el teu flux de treball a una funció diferent.

**Objectiu d’aprenentatge:** lliuraràs un informe JSON verificat, un registre de proves sobre fonts i eines, i un traspàs que entengui una sessió nova.

## Idees clau

- **Un requisit separat** determina la funció del projecte final.
- **L’edició d’un agent de programació** queda limitada als fitxers indicats.
- **Les comprovacions independents** determinen l’acceptació.
- **Un traspàs a una sessió nova** permet reconstruir el resultat.

## Abans de començar

**Prerequisits:** completa les lliçons 0 a 10, inclosos el context del repositori, la primera tasca de programació, MCP o l’alternativa del navegador, la delegació i els cicles acotats. La lliçó 11 és opcional. Reserva entre 90 i 120 minuts. Dificultat intermèdia.

**Fes servir una extracció nova** del [laboratori inicial](/downloads/effective-ai-course-lab.zip). Executa `python3 task_report.py tasks.json` i les dues proves de referència abans de modificar res. A Windows, fes servir `py -3` si la configuració utilitza el llançador de Python. Crea una base local de Git com a la configuració del curs. El filtre d’estat de la lliçó 5 no hi és expressament.

**Llegeix `docs/capstone-requirements.md`, revisió 1.** Demana `--format text|json`. El text predeterminat continua sent `Total tasks: 4`. La sortida JSON inclou un total numèric i un recompte de cada estat present a les dades. Comprova una llista buida, un estat absent i un format no admès. No facis servir `docs/requirements.md` com a referència per a aquesta funció nova.

**Tria el recorregut.** El recorregut connectat fa servir una edició observada d’un agent de programació, una crida MCP real de només lectura i un worker natiu o una sessió de worker separada. El recorregut d’estudi fa servir un assistent de xat per proposar codi, una font del navegador en lloc de MCP i xats separats com a workers simulats. Marca com a «no executats» els passos amb eines no disponibles. Tots dos recorreguts exigeixen proves locals i revisió dels fitxers. La solució següent ofereix fitxers complets per recuperar-se. Desa el primer intent a les notes abans de copiar la solució en una extracció nova.

## Fase del recorregut 1: Resum del projecte

**Obre el projecte de taller sintètic de ChatGPT o Claude.** Demana un esborrany de recordatori de dues frases. Comprova l’hora de les 19.00 a `approved-schedule.md`. L’horari defineix el recordatori. El requisit del projecte final defineix el programa.

**Prova:** registra el nom del projecte, la revisió de la font, l’hora observada a l’esborrany i qualsevol correcció. No enviïs el missatge.

## Fase del recorregut 2: Entorn del repositori

**Obre el laboratori nou.** Crea un `AGENTS.md` breu amb enllaços a `docs/capstone-requirements.md`, `task_report.py`, les proves i l’ordre de prova verificat durant la configuració. Si fas servir Claude Code, importa el fitxer compartit des de `CLAUDE.md`. Fes un commit humà de configuració per als fitxers d’instruccions i confirma que `git status --short` no mostra canvis. L’agent de programació no ha de fer commit del canvi de la funció.

**Prova:** desa el mapa i una còpia neta de les instruccions. Anota les claus JSON i el comportament per a les entrades no vàlides de la revisió 1. Si un xat anterior descriu el filtre d’estat, tracta’l com a context d’una tasca diferent.

## Fase del recorregut 3: Font externa

**Recorregut connectat:** fes servir el [servidor OpenAI Docs MCP de només lectura](https://learn.chatgpt.com/learn/docs-mcp) amb un client admès. Demana a una eina MCP les instruccions actuals per a `AGENTS.md`. Registra el nom de l’eina, l’URL de la font i un punt útil per al laboratori. Després elimina la connexió de pràctica.

**Recorregut d’estudi:** obre en un navegador la [documentació oficial d’`AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Registra’n el títol, l’URL i un punt útil. Marca com a «no executades» la descoberta i l’execució de MCP.

**Prova:** una entrada de servidor configurada no demostra que s’hagi executat. El recorregut connectat exigeix una crida d’eina visible i contingut de la font retornat.

## Fase del recorregut 4: Delega una revisió

**Demana a un worker de només lectura** que revisi `docs/capstone-requirements.md`, `task_report.py` i les proves de referència. Demana un informe de cinc files com a màxim amb les comprovacions que falten i les rutes dels fitxers. Al recorregut d’estudi, fes servir un xat separat i marca’l com a worker simulat.

**Resultat esperat:** les proves inicials comproven el total i un valor JSON que no és una llista. No comproven la sortida JSON, una llista buida, un estat absent ni un format no vàlid. Obre tu mateix el fitxer de proves per verificar l’informe. Una revisió independent breu és útil perquè els criteris d’acceptació són diferents dels de la lliçó 5.

**Prova:** desa l’informe breu i la teva decisió d’integració en una frase. Conserva la transcripció del worker fora del registre principal de la tasca.

## Fase del recorregut 5: Demana el canvi

**Dona a un agent de programació** el paquet següent. Al recorregut d’estudi, un assistent de xat proposa un pedaç i tu l’apliques manualment al laboratori.

```text
Objectiu: afegir --format text|json després del camí JSON.
Font: docs/capstone-requirements.md, revisió 1.
Fitxers que es poden modificar: task_report.py i tests/test_task_report.py.
Conservar: Total tasks: 4 com a sortida predeterminada i tasks.json sense canvis.
JSON: un objecte amb total i recomptes by_status, sense text addicional a stdout.
Comprovacions obligatòries: text predeterminat i explícit, JSON 4/2/2, llista buida,
estat absent, format no vàlid i proves de referència.
Aturar-se si: hi ha conflicte entre fonts, falla una prova de referència no relacionada o s’edita fora de l’abast.
Informe: fitxers modificats, ordres, sortides observades, problema pendent.
No fer commit, push, publicació ni enviar cap missatge.
```

**Revisa el pla** abans de modificar res. L’elecció de l’esquema importa: `total` és un nombre, no la cadena `"4"`. `by_status` conté cada estat de l’entrada, inclosos els futurs. Limita el canvi al laboratori extret.

## Fase del recorregut 6: Prova i revisa

**Executa aquestes comprovacions tu mateix.** A Windows, substitueix `python3` per `py -3`. L’ordre de les claus JSON i els espais no són importants. Analitza la sortida com a JSON i compara valors tipats.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Comportament esperat:** les proves passen. Les dues ordres de text mostren `Total tasks: 4`. L’ordre JSON retorna un objecte amb `total` 4, `by_status.open` 2 i `by_status.done` 2. Un format no vàlid acaba amb un codi diferent de zero. Les proves també cobreixen una entrada buida i una tasca sense un `status` de text. Llegeix la sortida d’error observada i el codi de sortida per a aquests casos.

| Punt de control | Prova d’èxit | Recuperació si falla |
|---|---|---|
| **Resum del projecte** | El recordatori indica les 19.00 | Actualitza la font de l’horari |
| **Mapa del repositori** | S’han indicat el requisit i les rutes de les proves | Corregeix els fitxers d’instruccions |
| **Font externa** | S’ha llegit MCP o s’ha indicat l’alternativa del navegador | Revisa la connexió o l’URL |
| **Revisió del worker** | S’han confirmat al fitxer les proves que falten | Corregeix l’informe del worker |
| **Abast dels fitxers** | Només el programa i les proves | Revisa cada canvi no desitjat |
| **Comportament** | S’han comprovat text, JSON, buits i errors | Diagnostica una causa i torna-ho a provar |
| **Traspàs** | Una sessió nova reconstrueix l’estat | Afegeix la font o el resultat que falta |

**Fes servir una extracció nova per reiniciar amb seguretat.** Desa les notes fora del laboratori, descarta només la còpia extreta d’un sol ús i torna a extreure el ZIP original. No facis un reinici ampli de Git en un repositori amb feina que vulguis conservar.

## Fase del recorregut 7: Traspàs a una sessió nova

**Escriu un traspàs de menys de 180 paraules** fora de la carpeta del laboratori. Inclou la revisió del requisit, els fitxers modificats, l’ordre exacte de les proves i el resultat, les sortides de text i JSON, les comprovacions d’entrades no vàlides, el registre d’ús i l’acció pendent. Obre una sessió nova i demana-li que identifiqui les claus JSON i digui si la funció ha passat.

**Resposta esperada:** la sessió nova anomena `total` i `by_status`, apunta a la revisió 1, informa només de comprovacions observades i assenyala les que falten.

## Solució i rúbrica

**Una implementació vàlida** apareix a continuació. Desa el primer bloc com a `task_report.py` i el segon com a `tests/test_task_report.py` en una extracció nova del laboratori. No modifiquis `tasks.json` ni els dos fitxers de requisits. Executa les comprovacions del punt de control 6. Compara qualsevol altra solució amb el requisit i el comportament observat.

`task_report.py`:

```python
"""Imprimeix un recompte de text o un resum JSON de les tasques del taller."""

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
    parser = argparse.ArgumentParser(description="Informe de tasques del taller")
    parser.add_argument("path", type=Path, help="camí a la llista de tasques JSON")
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
"""Comprovacions dels informes de text i JSON de les tasques del taller."""

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

**Reinicia després d’utilitzar la solució:** desa les notes fora del laboratori, descarta aquesta còpia extreta i torna a extreure el laboratori inicial original. La còpia nova conté les dues proves de referència i no té implementada la funció.

**Dona un punt per cada punt de control** de la taula. Set punts completen el recorregut connectat si la fila de la font externa inclou una crida MCP real i la del worker documenta una sessió real. Set punts completen el recorregut d’estudi si la font és una pàgina de navegador verificada i els passos d’eines s’indiquen explícitament com a no executats. La manca d’una comprovació del comportament, de la font o de l’abast dels fitxers bloqueja tots dos recorreguts.

## Comprova què has après

1. **Quin requisit controla aquesta funció?** `docs/capstone-requirements.md`, revisió 1. El requisit anterior del filtre d’estat pertany a la lliçó 5.
2. **Què demostra el contracte JSON?** Analitza la sortida de l’ordre, compara els valors numèrics i el recompte de cada estat, i comprova entrades buides i no vàlides. Un resum polit de l’agent no és suficient.

## Resolució de problemes

- **La prova base falla abans d’editar:** restableix el laboratori des del ZIP i repeteix la configuració.
- **L’agent modifica un altre fitxer:** revisa el diff i restaura només el canvi no desitjat del laboratori.
- **La connexió MCP falla:** utilitza la font del navegador i marca el punt de control com a recorregut d’estudi.
- **El worker repeteix un valor erroni:** torna a llegir el requisit del projecte final i corregeix l’informe.
- **S’acaben els intents:** conserva el registre d’errors i demana el pas següent a una persona revisora.

## Passos següents

**Desa el registre de proves complet.** Per a la publicació avançada d’equip i l’autoritat entre sistemes, continua amb el [Curs d’implementació de la col·laboració amb IA](/ai-collaboration-course-start/).

**Navegació del curs:** [Anterior obligatòria: cicles acotats](/articles/effective-ai-bounded-agent-loops/), [Opcional: avaluació d’agents especialitzats](/articles/effective-ai-specialized-agent-evaluation/), [Esquema del curs](/effective-ai-course-start/).
