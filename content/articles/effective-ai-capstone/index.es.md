---
title: "Proyecto final de flujo de trabajo con IA: crear y verificar un informe JSON"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Crea un informe JSON nuevo con contexto del proyecto, una solicitud acotada para un agente, pruebas independientes, revisión de fuentes y una transferencia para una sesión nueva."
genre: ["Inteligencia artificial", "Ingeniería de software", "Educación"]
tags: ["proyecto final de flujo de trabajo con IA", "proyecto con agente de programación", "verificación de tareas con IA", "AGENTS.md", "práctica de MCP", "transferencia entre agentes"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Una tarea de software de taller terminada con archivos fuente, resultados de pruebas, revisión del agente y registro de transferencia"
coverCaption: ""
---

[Volver al curso de flujo de trabajo práctico con IA](/effective-ai-course-start/)

**Crea un formato de salida nuevo y demuestra su comportamiento.** Antes añadiste un filtro de estado. Este proyecto final empieza con un laboratorio nuevo y añade un informe JSON para que lo lea otro programa. El requisito nuevo comprueba si transfieres tu flujo de trabajo a otra función.

**Objetivo de aprendizaje:** entregarás un informe JSON comprobado, un registro de pruebas de fuentes y herramientas, y una transferencia que una sesión nueva pueda entender.

## Puntos clave

- **Un requisito separado** define la función del proyecto final.
- **La edición de un agente de programación** se limita a los archivos indicados.
- **Las comprobaciones independientes** determinan la aceptación.
- **Una transferencia a una sesión nueva** permite reconstruir el resultado.

## Antes de empezar

**Requisitos previos:** completa las lecciones 0 a 10, incluido el contexto del repositorio, la primera tarea de programación, MCP o su alternativa con navegador, la delegación y los ciclos acotados. La lección 11 es opcional. Reserva de 90 a 120 minutos. La dificultad es intermedia.

**Usa una extracción nueva** del [laboratorio inicial](/downloads/effective-ai-course-lab.zip). Ejecuta `python3 task_report.py tasks.json` y las dos pruebas de referencia antes de editar. En Windows, usa `py -3` si tu configuración usa el lanzador de Python. Crea una referencia local de Git como en la configuración del curso. El filtro de estado de la lección 5 no está presente a propósito.

**Lee `docs/capstone-requirements.md`, revisión 1.** Exige `--format text|json`. El texto predeterminado sigue siendo `Total tasks: 4`. La salida JSON incluye un total numérico y recuentos para cada estado presente en los datos. Probarás una lista vacía, un estado ausente y un formato no admitido. No uses `docs/requirements.md` como autoridad para esta función nueva.

**Elige tu modalidad.** La modalidad conectada usa una edición observada de un agente de programación, una llamada MCP real de solo lectura y un trabajador nativo o una sesión de trabajador separada. La modalidad de estudio usa un asistente de chat para proponer código, una fuente del navegador en lugar de MCP y chats separados como trabajadores simulados. Marca los pasos de herramientas que no estén disponibles como «no ejecutado». Ambas modalidades requieren pruebas locales y revisión de archivos. La clave de respuestas incluye archivos completos para recuperarte si tu intento lo necesita. Guarda tu primer intento en notas antes de copiar la clave a una extracción nueva.

## Punto de control 1: Resumen del proyecto

**Abre el proyecto de taller sintético de ChatGPT o Claude.** Pide un borrador de recordatorio de dos oraciones. Comprueba que indique las 19:00 según `approved-schedule.md`. El horario rige el recordatorio. El requisito del proyecto final rige el programa.

**Evidencia:** registra el nombre del proyecto, la revisión de la fuente, la hora observada en el borrador y cualquier corrección. No envíes el mensaje.

## Punto de control 2: Contexto del repositorio

**Abre el laboratorio nuevo.** Crea un `AGENTS.md` breve que apunte a `docs/capstone-requirements.md`, `task_report.py`, las pruebas y el comando de prueba comprobado durante la configuración. Si usas Claude Code, importa el archivo compartido desde `CLAUDE.md`. Haz un commit humano de configuración para esos archivos de orientación y confirma que `git status --short` no devuelve cambios. El agente de programación no debe hacer commit de la función.

**Evidencia:** guarda el mapa y una copia limpia de las instrucciones. Anota las claves JSON y el comportamiento ante entradas no válidas de la revisión 1. Si un chat anterior describe el filtro de estado, trátalo como contexto de otra tarea.

## Punto de control 3: Fuente externa

**Modalidad conectada:** usa el [servidor MCP de OpenAI Docs de solo lectura](https://learn.chatgpt.com/learn/docs-mcp) mediante un cliente compatible. Pide a una herramienta MCP las instrucciones actuales de `AGENTS.md`. Registra el nombre de la herramienta, la URL de la fuente y un punto pertinente para tu laboratorio. Después elimina la conexión de práctica.

**Modalidad de estudio:** abre en un navegador la [documentación oficial de `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Registra el título, la URL y un punto pertinente. Marca la búsqueda y ejecución de MCP como «no ejecutadas».

**Evidencia:** una entrada de servidor configurada no demuestra que se haya ejecutado. La modalidad conectada requiere una llamada de herramienta visible y contenido de fuente devuelto.

## Punto de control 4: Delegar una revisión

**Pide a un trabajador de solo lectura** que revise `docs/capstone-requirements.md`, `task_report.py` y las pruebas de referencia. Solicita un informe de cinco filas como máximo que indique las comprobaciones faltantes y las rutas de archivo. En la modalidad de estudio, usa un chat separado y márcalo como trabajador simulado.

**Hallazgo esperado:** las pruebas iniciales cubren el recuento total y un valor JSON que no es una lista. No cubren la salida JSON, una lista vacía, un estado ausente ni un formato no válido. Abre tú mismo el archivo de pruebas para confirmar el informe. Una revisión independiente breve es útil porque los criterios de aceptación difieren de los de la lección 5.

**Evidencia:** guarda el informe breve y tu decisión de integración en una oración. Mantén la transcripción del trabajador fuera del registro principal de la tarea.

## Punto de control 5: Solicitar la edición

**Entrega a un agente de programación** el paquete siguiente. En la modalidad de estudio, un asistente de chat propone el parche y tú lo aplicas manualmente en el laboratorio.

```text
Objetivo: añadir --format text|json después de la ruta JSON.
Fuente: docs/capstone-requirements.md, revisión 1.
Cambios permitidos: task_report.py y tests/test_task_report.py.
Conservar: Total tasks: 4 como salida predeterminada y tasks.json sin cambios.
JSON: un objeto con total y recuentos by_status, sin texto adicional en stdout.
Comprobaciones requeridas: texto predeterminado y explícito, JSON 4/2/2, lista vacía,
estado ausente, formato no válido y pruebas de referencia.
Detenerse si: hay conflicto entre fuentes, falla una prueba de referencia ajena al cambio o se edita fuera del alcance.
Informe: archivos modificados, comandos, salidas observadas, problema sin resolver.
No hagas commit, push, publicación ni envío de mensajes.
```

**Revisa el plan** antes de editar. La elección del esquema importa: `total` es un número, no la cadena `"4"`. `by_status` contiene cada estado presente en la entrada, para que el informe incluya también futuros valores de estado. Limita la edición al laboratorio extraído.

## Punto de control 6: Probar y revisar

**Ejecuta tú estas comprobaciones.** En Windows, sustituye `python3` por `py -3`. El orden exacto de las claves JSON y los espacios no importan. Analiza la salida como JSON y compara valores tipados.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Comportamiento esperado:** las pruebas pasan. Los dos comandos de texto muestran `Total tasks: 4`. El comando JSON devuelve un objeto con `total` 4, `by_status.open` 2 y `by_status.done` 2. El formato no válido termina con un código distinto de cero. Las pruebas también cubren una entrada vacía y una tarea sin un `status` de tipo cadena. Lee la salida de error observada y el código de salida para esos casos.

| Punto de control | Prueba de éxito | Recuperación ante fallos |
|---|---|---|
| **Resumen del proyecto** | El recordatorio indica las 19:00 | Actualiza la fuente del horario |
| **Mapa del repositorio** | Se nombran el requisito y las rutas de prueba | Corrige los archivos de orientación |
| **Fuente externa** | Se leyó MCP o se indicó la alternativa del navegador | Revisa la conexión o la URL |
| **Revisión del trabajador** | Se confirmaron los casos faltantes en el archivo | Corrige el informe del trabajador |
| **Alcance de archivos** | Solo el programa y las pruebas | Revisa cada cambio no deseado |
| **Comportamiento** | Se comprobaron texto, JSON, casos vacíos y errores | Diagnostica una causa y vuelve a intentarlo |
| **Transferencia** | Una sesión nueva reconstruye el estado | Añade la fuente o el resultado que falta |

**Usa una extracción nueva como reinicio seguro.** Guarda tus notas fuera del laboratorio, descarta solo la copia extraída desechable y extrae de nuevo el ZIP original. No uses un reinicio amplio de Git en un repositorio con trabajo que quieras conservar.

## Punto de control 7: Transferencia a una sesión nueva

**Escribe una transferencia de menos de 180 palabras** fuera de la carpeta del laboratorio. Incluye la revisión del requisito, los archivos modificados, el comando exacto de prueba y el resultado, las salidas de texto y JSON, las comprobaciones de entradas no válidas, el registro de uso y la acción pendiente. Abre una sesión nueva y pídele identificar las claves JSON e indicar si la función pasó.

**Respuesta esperada:** la sesión nueva nombra `total` y `by_status`, señala la revisión 1, informa solo las comprobaciones observadas e indica cualquier comprobación faltante.

## Clave de respuestas y rúbrica

**Una implementación válida** aparece abajo. Guarda el primer bloque como `task_report.py` y el segundo como `tests/test_task_report.py` en una extracción nueva del laboratorio. No cambies `tasks.json` ni los dos archivos de requisitos. Ejecuta las comprobaciones del punto de control 6. Compara otra solución con el requisito y el comportamiento observado.

`task_report.py`:

```python
"""Imprime un recuento de texto o un resumen JSON de las tareas del taller."""

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
    parser = argparse.ArgumentParser(description="Informe de tareas del taller")
    parser.add_argument("path", type=Path, help="ruta a la lista de tareas JSON")
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
"""Comprobaciones para informes de texto y JSON de las tareas del taller."""

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

**Reinicia después de usar la clave:** guarda tus notas fuera del laboratorio, descarta esta copia extraída y extrae de nuevo el laboratorio inicial. La copia nueva incluye las dos pruebas de referencia y no contiene una implementación de la función.

**Asigna un punto por cada control** de la tabla anterior. Siete puntos completan la modalidad conectada si la fila de fuente externa incluye una llamada MCP real y la fila de trabajador documenta una sesión real. Siete puntos completan la modalidad de estudio si la fila de fuente incluye una página de navegador verificada y los pasos de herramientas dicen explícitamente «no ejecutado». La falta de una comprobación de comportamiento, fuente o alcance de archivos impide completar cualquiera de las modalidades.

## Comprueba lo aprendido

1. **¿Qué requisito rige esta función?** `docs/capstone-requirements.md`, revisión 1. El requisito anterior del filtro de estado corresponde a la lección 5.
2. **¿Qué demuestra el contrato JSON?** Analiza la salida del comando, compara los valores numéricos y los recuentos de todos los estados, y comprueba entradas vacías y no válidas. Un resumen pulido del agente no basta.

## Solución de problemas

- **Falla la referencia antes de editar:** restablece el laboratorio desde el ZIP y repite la configuración.
- **El agente cambia otro archivo:** revisa el diff y restaura solo el cambio no deseado del laboratorio.
- **Falla la conexión MCP:** usa la fuente del navegador y marca el control como modalidad de estudio.
- **El trabajador repite un valor incorrecto:** vuelve a leer el requisito del proyecto final y corrige el informe.
- **Se agotan los intentos:** conserva el registro del fallo y pide a una persona que indique el siguiente paso.

## Siguientes pasos

**Guarda tu registro de pruebas completo.** Para publicación de equipo avanzada y autoridad entre sistemas, continúa con el [Curso de implementación de colaboración con IA](/ai-collaboration-course-start/).

**Navegación del curso:** [Anterior obligatoria: ciclos acotados](/articles/effective-ai-bounded-agent-loops/), [Opcional: evaluación de agentes especializados](/articles/effective-ai-specialized-agent-evaluation/), [Índice del curso](/effective-ai-course-start/).
