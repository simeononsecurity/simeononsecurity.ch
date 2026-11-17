---
title: "Ejecuta tu primera tarea de repositorio con un agente de programación"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Elige una interfaz de agente de programación, abre un repositorio de ejemplo, revisa un cambio propuesto y ejecuta comprobaciones antes de conservar la edición."
genre: ["Inteligencia artificial", "Ingeniería de software"]
tags: ["tutorial de Codex CLI", "aplicación Codex", "Claude Code CLI", "tutorial de OpenCode", "flujo de trabajo con agentes de programación", "herramientas de programación con IA"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Un repositorio de código con vistas separadas del agente en terminal y escritorio junto a un archivo revisado"
coverCaption: ""
---

[Volver al curso de Flujo de trabajo práctico con IA](/effective-ai-course-start/)

**Un agente de programación lee archivos, propone ediciones y ejecuta herramientas dentro de un espacio de trabajo.** En esta lección harás una pequeña tarea de repositorio. Elige Codex en la aplicación de escritorio ChatGPT o en CLI, Claude Code CLI u OpenCode TUI. Después revisa un cambio antes de aceptarlo.

**Objetivo de aprendizaje:** ejecutarás o aplicarás manualmente una edición acotada y verificarás su diferencia y comportamiento.

## Ideas clave

- **Codex en la aplicación de escritorio ChatGPT** ofrece un espacio visual para las tareas y su revisión.
- **Codex CLI** ejecuta una sesión de Codex desde la terminal.
- **Claude Code CLI** ejecuta el flujo de programación de Claude desde la terminal.
- **OpenCode TUI** ofrece un flujo de programación en terminal con proveedores y permisos configurables.
- **Una diferencia y el resultado de una prueba** importan más que el mensaje de finalización del asistente.

## Antes de empezar

**Requisitos previos:** termina la [configuración del curso](/articles/effective-ai-course-setup/), incluida la ejecución inicial y la instantánea local de Git. Completa [el contexto del repositorio](/articles/effective-ai-agents-md-context/) y [los paquetes de tareas](/articles/effective-ai-task-packets/) antes de esta lección. Usa un agente de programación al que tengas permiso de acceder. Reserva 45 minutos. La dificultad va de principiante a intermedia.

**Usa el [laboratorio inicial del curso](/downloads/effective-ai-course-lab.zip)** en una carpeta desechable. El archivo contiene un programa pequeño para informar tareas, datos de muestra y pruebas. No uses un repositorio de producción para tu primera edición. Tu tarea consiste en añadir un filtro `--status` y conservar el recuento total existente.

## Ruta de estudio sin agente de programación

**Usa un asistente de chat para proponer el mismo cambio** si no tienes un agente de programación. Pega solo `docs/requirements.md`, `task_report.py` y el archivo de prueba específico del laboratorio sintético. Pide una diferencia unificada y una explicación breve. Una diferencia unificada muestra las líneas antiguas con `-` y las nuevas con `+`. Abre el archivo indicado en un editor de texto, sustituye las líneas antiguas por el cambio propuesto y guarda el archivo. Después ejecuta todos los comandos de Revisar el resultado. Deja `tasks.json` sin cambios. Anota que el paso con el agente no se ejecutó. El proyecto final incluye una función JSON independiente, así que compara tu solución del filtro con el requisito y las comprobaciones de la lección 5.

## Elige una interfaz

**Elige primero una superficie de revisión.** Codex en la aplicación de escritorio ChatGPT se adapta a un proyecto visual y a la revisión de diferencias. Una interfaz de terminal sirve para trabajar desde la carpeta extraída del laboratorio. Compara las opciones de terminal entre sí:

| Herramienta de terminal | Comprobación de cuenta o proveedor | Comando de inicio |
|---|---|---|
| **Codex CLI** | Confirma el inicio de sesión de Codex y los permisos locales | `codex` |
| **Claude Code CLI** | Confirma el acceso a Claude Code y los permisos locales | `claude` |
| **OpenCode TUI** | Configura un proveedor de modelos compatible y los permisos | `opencode` |

**Instala e inicia sesión con la guía oficial actual** de la herramienta elegida. Lee [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [aplicación ChatGPT para escritorio](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) u [OpenCode](https://opencode.ai/docs/). Los comandos, las plataformas compatibles y los requisitos de cuenta cambian. Esta lección usa los nombres de inicio estables y un procedimiento de revisión común.

**Para una elección más detallada,** lee la [comparación de agentes de programación CLI](/articles/cli-coding-agents-comparison/) o la [comparación de agentes de programación con interfaz gráfica](/articles/gui-coding-agents-comparison/) del sitio. Las guías de [Codex CLI y escritorio](/articles/codex-cli-vs-desktop/), [Claude Code CLI y escritorio](/articles/claude-code-cli-vs-desktop/) y [OpenCode CLI y escritorio](/articles/opencode-cli-vs-desktop/) comparan las interfaces de cada producto.

**Empieza en la carpeta del laboratorio.** Cada interfaz requiere que elijas explícitamente un espacio de trabajo:

1. **Codex de escritorio:** abre la aplicación de escritorio ChatGPT, selecciona el laboratorio extraído como proyecto local e inicia una tarea local en ese proyecto. Revisa la ruta de la carpeta y las solicitudes de aprobación antes de una edición. Una tarea alojada usa una copia separada del espacio de trabajo.
2. **Codex CLI:** ejecuta `cd /path/to/effective-ai-course-lab` y luego `codex`. Confirma la carpeta de trabajo que aparece y el modo de aprobación.
3. **Claude Code CLI:** ejecuta el mismo comando `cd` y luego `claude`. Confirma la carpeta del proyecto y los permisos de las herramientas.
4. **OpenCode TUI:** ejecuta el mismo comando `cd` y luego `opencode`. Confirma el proveedor seleccionado, el proyecto y la configuración de permisos.

**ChatGPT chat y Claude Projects gestionan conversaciones y archivos de referencia compartidos.** Codex y Claude Code trabajan con un espacio de código que incluye herramientas para archivos y comandos. OpenCode también ofrece interfaces de escritorio e IDE, pero esta lección usa su interfaz de terminal. El proveedor, la cuenta y la ejecución local o alojada varían, así que registra la superficie elegida en vez de considerar todas las sesiones como una misma ejecución.

**Comprueba cinco detalles antes de abrir el laboratorio:** sistema operativo compatible, autenticación, coste del proveedor o la cuenta, permisos de archivos y comandos, y si la ejecución ocurre localmente o en un host remoto. Registra tu elección. No supongas que una aplicación de escritorio y una herramienta de terminal usan el mismo espacio de trabajo.

## Inspecciona el proyecto inicial

**Vuelve a abrir la carpeta limpia del laboratorio** de la lección sobre el contexto del repositorio. Esta copia tiene tu `AGENTS.md` confirmado y la guía opcional `CLAUDE.md`. Revisa los archivos antes de pedir una edición al agente. Ejecuta las pruebas iniciales desde esta carpeta.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Resultado inicial esperado:** el informe muestra `Total tasks: 4`. La ejecución de pruebas nombra dos pruebas y termina con `OK`. Si alguna falla, detente y revisa los archivos extraídos. No atribuyas al agente la reparación de un punto de partida defectuoso.

**Usa las instantáneas locales de Git** de la configuración del curso y la lección sobre el contexto del repositorio. `AGENTS.md` y `CLAUDE.md` opcional ya deberían estar confirmados. Ejecuta `git status --short` antes de editar la función y espera que no muestre archivos. El agente tampoco debe confirmar cambios. El archivo no incluye historial de Git. Su archivo `.gitignore` excluye el bytecode de Python generado al ejecutar las pruebas. Si extrajiste una copia nueva, repite la configuración del curso y la lección de contexto del repositorio en la carpeta nueva. Confirma los archivos de orientación antes de editar la función. Primero inicializa y confirma el proyecto inicial:

```bash
git init
git add .
git commit -m "Base del laboratorio del curso"
```

**Después añade `AGENTS.md` y el `CLAUDE.md` opcional** con el origen y el comando de prueba aprobados en la lección sobre el contexto del repositorio. Confirma esos archivos, verifica que `git status --short` esté limpio y empieza a editar la función. Ejecuta estos comandos en la carpeta extraída para practicar, no en la raíz de otro repositorio.

## Envía una solicitud acotada

**Abre la carpeta del laboratorio** en el agente de programación que elegiste. Envía este paquete de tareas:

```text
Añade un argumento opcional --status a task_report.py.
Valores permitidos: open y done.
Si falta, conserva sin cambios la salida actual del recuento total.
Si está presente, cuenta solo las tareas coincidentes e imprime Total tasks: N.
Añade pruebas para ambos valores, un valor inválido y la salida predeterminada sin cambios.
No cambies tasks.json ni archivos ajenos a la tarea.
Ejecuta las pruebas e informa del comando exacto y el resultado.
Detente después del código y las pruebas. No hagas commit ni push.
```

**En Windows,** sustituye `python3` por el comando `py -3` que verificaste durante la configuración, también en las instrucciones guardadas del repositorio y el paquete de tareas.

**Pide un plan breve antes de editar** si aún no conoces el código. Autoriza al agente a editar solo la carpeta desechable del laboratorio. Los controles de permisos varían entre herramientas, así que revisa la configuración actual antes de permitir comandos de shell o escrituras de archivos.

## Revisa el resultado

**Lee la diferencia.** Comprueba que la salida sin filtro siga igual, que el filtro acepte solo dos valores y que las pruebas cubran el error y la salida predeterminada sin cambios. Una ejecución verde de pruebas respalda el cambio solo si la prueba comprueba el comportamiento solicitado.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Resultados esperados:** los tres primeros comandos de informe muestran recuentos de 4, 2 y 2. El valor inválido muestra un error claro y termina con un estado distinto de cero. El texto exacto del error depende de la implementación. En macOS o Linux, ejecuta `echo $?` inmediatamente después del comando inválido para leer el código de salida. En PowerShell, revisa `$LASTEXITCODE`.

| Evidencia | Qué revisar |
|---|---|
| **Lista de archivos** | Solo cambian el programa y las pruebas |
| **Diferencia** | La lógica del filtro coincide con la solicitud |
| **Salida de pruebas** | Se ejecutaron y aprobaron los casos nuevos |
| **Ejecución manual** | Los recuentos predeterminado, `open` y `done` coinciden con `tasks.json` |

**Si el agente informa un resultado sin ejecutar pruebas,** ejecuta el comando tú mismo. Si la edición afecta archivos ajenos al paquete de tareas, pide una corrección acotada. Si el estado no está claro, elimina la copia de práctica extraída y vuelve a extraer el ZIP original.

## Respuestas de la ruta de estudio

**Usa estos archivos completos si falla tu parche manual.** Empieza con una extracción nueva del laboratorio, guarda el primer bloque como `task_report.py` y el segundo como `tests/test_task_report.py`, y ejecuta los comandos de Revisar el resultado. Deja `tasks.json` y `docs/requirements.md` sin cambios. Anota el fallo original antes de copiar los archivos.

`task_report.py`:

```python
"""Muestra el recuento de tareas de un archivo JSON."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Cuenta todas las tareas o las que tienen un estado permitido."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Cuenta las tareas del taller")
    parser.add_argument("path", type=Path, help="ruta a la lista JSON de tareas")
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
"""Pruebas del informe de tareas del taller."""

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

**Conserva una copia editada que haya pasado** las pruebas de filtro durante las lecciones de contexto y verificación de resultados. Si usaste esta clave de respuestas para recuperarte, guarda la copia nueva con sus pruebas aprobadas para esas lecciones. Conserva la diferencia y el registro de pruebas fuera del laboratorio. Restablece el proyecto inicial antes de la lección de delegación o descarta un intento fallido cuando necesites un nuevo intento limpio.

## Practica y comprueba

**Tu artefacto:** una diferencia del laboratorio y un registro de revisión de cuatro filas sobre el alcance de archivos, el comportamiento predeterminado, el comportamiento filtrado y la entrada inválida. Anota el nombre y la versión de la herramienta en tus notas privadas para reproducir un problema específico de versión.

**Razonamiento esperado:** elegiste una interfaz acorde con tu forma de trabajar, entregaste una tarea acotada, revisaste la edición real y ejecutaste una comprobación independiente del resumen del agente.

## Comprueba lo aprendido

1. **Pregunta:** ¿Qué demuestra que funcionó la edición del filtro de estado? **Respuesta:** Una diferencia acotada, pruebas aprobadas y resultados observados para la salida predeterminada, open, done y el caso inválido.
2. **Pregunta:** ¿El mensaje del agente de que ejecutó las pruebas cuenta como resultado tuyo? **Respuesta:** No. Ejecuta el comando o revisa su salida.

## Solución de problemas

- **Falta un comando:** termina la instalación con la guía del proveedor enlazada y abre de nuevo la terminal.
- **No hay acceso a archivos:** abre la carpeta extraída del laboratorio y revisa los permisos del espacio de trabajo.
- **Cambian archivos inesperados:** detente y revisa `git status --short` antes de otra solicitud.
- **Las pruebas pasan, pero el comportamiento es incorrecto:** añade un caso manual o una prueba para el requisito que falta.

## Próximos pasos

**Continúa con [Ventanas de contexto y traspasos](/articles/effective-ai-context-window-management/)**. Guardarás un registro útil para una sesión nueva.

**Navegación del curso:** [Anterior: Paquetes de tareas](/articles/effective-ai-task-packets/), [Índice del curso](/effective-ai-course-start/).
