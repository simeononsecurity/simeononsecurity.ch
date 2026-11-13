---
title: "Bucles acotados de agentes de IA: comprobaciones, reintentos y reglas de parada"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Define un bucle de objetivos de IA con estado observable, comprobaciones, límites de reintentos, condiciones de parada y una transferencia clara a una persona."
genre: ["Inteligencia artificial", "Ingeniería de software", "Productividad"]
tags: ["bucles de objetivos de IA", "bucle de reintento de agente", "reglas de parada de automatización de IA", "monitorización de agentes", "transferencia humana de IA", "flujo de trabajo de IA acotado"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "Un pequeño bucle de agente que pasa de una edición a una prueba, una decisión de reintento y una transferencia a una persona"
coverCaption: ""
---

[Volver al curso práctico de flujos de trabajo con IA](/effective-ai-course-start/)

**Un bucle de objetivos repite el trabajo hasta que un resultado definido supera la comprobación o se activa una regla de parada.** El bucle útil lee el estado actual, realiza una acción acotada, comprueba el resultado y registra lo ocurrido. Una instrucción abierta como «sigue intentándolo» no tiene una regla de finalización fiable.

**Objetivo de aprendizaje:** ejecutarás un bucle de laboratorio acotado con una comprobación que se sabe que falla y registrarás la decisión de parada.

## Ideas clave

- **Objetivo:** un resultado expresado en términos observables.
- **Estado:** los archivos, resultados, errores y revisión del código fuente actuales.
- **Comprobación:** una prueba o revisión vinculada al objetivo.
- **Presupuesto de reintentos:** el máximo de intentos permitidos para un fallo.
- **Regla de parada:** una condición que exige terminar o pedir una decisión humana.

## Antes de empezar

**Requisitos previos:** el [paquete de tareas](/articles/effective-ai-task-packets/), el [registro de verificación](/articles/effective-ai-output-verification/) y la [lección sobre delegación](/articles/effective-ai-agent-delegation/). Reserva 45 minutos. La dificultad es intermedia. Usa una copia nueva del laboratorio sintético para conocer de antemano la primera comprobación fallida.

## Escribe el contrato del bucle

**Para la solicitud de filtro por estado**, define el contrato antes de cualquier reintento:

```text
Objetivo: admitir --status open|done sin cambiar la salida predeterminada.
Fuente: docs/requirements.md, revisión 1.
Archivos permitidos: task_report.py y pruebas específicas.
Comprobaciones: pruebas unitarias, recuentos 4/2/2 y código de salida distinto de cero para un valor no válido.
Presupuesto de reintentos: como máximo dos ediciones después del primer intento.
Detente de inmediato: conflicto en la fuente, cambio de archivo inesperado, exposición de un secreto,
o fallo de referencia ajeno a esta solicitud.
Entrega: informa del diff final, los comandos, las salidas, los intentos y el problema pendiente.
```

**El presupuesto es una política de la tarea**, no un valor predeterminado del producto. Dos reintentos bastan para diagnosticar una tarea pequeña de laboratorio sin ocultar fallos repetidos. Una tarea de producción necesita su propia decisión sobre riesgos y revisión.

## Usa una tabla de estado

| Paso | Estado que debes registrar | Decisión |
|---|---|---|
| **Leer** | Revisión del código fuente y resultado inicial | Para si el estado inicial es distinto |
| **Actuar** | Archivos modificados y acción realizada | Rechaza los cambios fuera del alcance |
| **Comprobar** | Prueba exacta y resultado manual | Acepta o diagnostica |
| **Reintentar** | Causa del fallo e hipótesis nueva | Continúa solo dentro del presupuesto |
| **Transferir** | Estado final y siguiente responsable | Para tras aprobar o quedar bloqueado |

**Registra los intentos, no solo el último mensaje.** Una prueba que pasa después de tres ediciones ocultas no explica qué cambió. Mantén un registro breve del fallo, la hipótesis revisada y las nuevas pruebas.

## Analiza un fallo

**Primer intento ilustrativo:** el agente añade el filtro y las pruebas. `open` muestra 2, pero `--status invalid` muestra 0 y termina correctamente. El requisito exige que un valor no válido devuelva un código de salida distinto de cero. Marca la comprobación como fallida.

**Diagnóstico:** inspecciona la validación de argumentos. El agente trató un valor desconocido como una coincidencia vacía en lugar de un error. Pide una corrección acotada para validar los valores admitidos antes de contar. Repite el caso no válido y todas las comprobaciones anteriores.

```text
Intento 1: el estado no válido terminó correctamente, así que la aceptación falló.
Causa encontrada: no se validaron los valores aceptados.
Petición del intento 2: rechaza los valores no admitidos y conserva los recuentos 4/2/2.
Pruebas necesarias: ejecución completa de las pruebas y código de salida del comando no válido.
```

**Resultado esperado del segundo intento:** un error claro y un código de salida distinto de cero para `invalid`, con los recuentos válidos sin cambios. Si el segundo intento sigue fallando, usa el último reintento solo después de identificar una causa nueva. Repetir la misma solicitud no es diagnosticar.

## Gestiona resultados ambiguos

**Que un proceso termine sin resultado no significa que haya tenido éxito.** Si una herramienta agota el tiempo después de una posible escritura, inspecciona los archivos y el estado de Git antes de repetirla. Si un servicio conectado informa de un resultado desconocido, consulta su estado actual antes de repetir una acción externa. Fuera del laboratorio, duplicar envíos, publicaciones o escrituras es un riesgo real.

**Detente para una revisión humana** cuando el requisito entre en conflicto con otra fuente aprobada, un permiso impida la acción, se agote el presupuesto de reintentos o la acción solicitada cruce un límite de publicación. La transferencia debe indicar el estado exacto y la decisión pendiente.

## Separa los bucles de los monitores

**Un bucle de edición** se ejecuta dentro de una tarea acotada y comprueba el resultado después de cada acción. **Un monitor programado** se activa más tarde para inspeccionar una condición. Un monitor necesita su propia frecuencia, umbral de cambio, regla de notificación y condición de parada. No conviertas el bucle de edición del laboratorio en una tarea recurrente. La siguiente lección evalúa sistemas persistentes antes de activarlos.

## Ejecuta un bucle controlado

**Empieza con el laboratorio intacto.** Sus dos pruebas iniciales pasan. Crea `tests/test_loop_contract.py` en la extracción nueva con la comprobación siguiente. Este archivo expresa una función deseada que falta en el proyecto inicial. No forma parte del ZIP inicial mantenido.

```python
"""One controlled failing check for the status-filter exercise."""

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

**Ejecuta `python3 -m unittest discover -s tests -v`.** Las dos pruebas originales deberían pasar y la nueva prueba contractual debería fallar porque el proyecto inicial no admite `--status`. Registra el fallo real. Si inicializaste Git como se indica en la lección 0, registra también `git status --short`. Si no, compara los archivos modificados con una extracción intacta. En Windows, usa `py -3` si tu configuración utiliza el lanzador.

**Fija un presupuesto de tres intentos:** la primera edición y como máximo dos correcciones. Entrega al agente el contrato del bucle anterior y pide una edición acotada. Después de cada intento, inspecciona los archivos modificados, vuelve a ejecutar todas las pruebas y ejecuta los comandos predeterminado, `open`, `done` y no válido. Registra la causa del fallo antes de otro intento. Para si una prueba pasa, falla una línea base no relacionada, aparece un cambio fuera del alcance o falla el tercer intento.

**Ruta de estudio:** aplica la [solución completa de la lección 5](/articles/effective-ai-coding-agent-first-task/) en esta copia nueva después de registrar la prueba roja. Vuelve a ejecutar las mismas comprobaciones y anota que no se ejecutó la edición del agente. Conserva la prueba contractual controlada. No la debilites ni la elimines para hacerla pasar.

| Intento | Estado y observación | Decisión |
|---|---|---|
| **Antes de editar** | Pasan las dos pruebas iniciales y falla la nueva comprobación de `open` | Continúa con una edición acotada |
| **Después de cada edición** | Registra pruebas exactas, recuentos, salida no nula para un valor inválido y archivos modificados | Acepta, diagnostica o para |
| **Al agotarse el presupuesto** | Registra el fallo pendiente y la diferencia actual | Transfiere sin otro intento |

## Practica y comprueba

**Tu artefacto:** la prueba controlada que falla, los resultados observados antes y después, un registro de intentos y una decisión final de aceptar o parar. Si la primera edición pasa, registra un intento. No inventes un segundo fallo para rellenar el registro.

**Comprobación de finalización:** el contrato especifica una fuente, el alcance de los archivos, comprobaciones observables, un límite de reintentos, al menos una condición de parada inmediata y una transferencia. El registro incluye la prueba roja real, los resultados posteriores y una aprobación o una parada por presupuesto. Un segundo intento identifica una causa nueva y difiere del primero.

## Comprueba lo que aprendiste

1. **Pregunta:** ¿qué demuestra la primera prueba contractual roja? **Respuesta:** que el proyecto inicial no tiene el filtro de estado solicitado, según una prueba escrita antes de editarlo.
2. **Pregunta:** ¿cuándo debe parar el bucle aunque queden reintentos? **Respuesta:** ante un cambio fuera del alcance, un permiso poco claro o un requisito en conflicto.

## Solución de problemas

- **El bucle repite el mismo fallo:** para y formula una hipótesis nueva sobre la causa.
- **Las comprobaciones se debilitan:** restaura los criterios originales de aceptación.
- **Resultado externo incierto:** inspecciona el estado actual antes de otro intento.
- **Presupuesto agotado:** transfiere el registro de fallos en lugar de ocultarlos.

## Próximos pasos

Continúa con la optativa [Evaluación de agentes especializados](/articles/effective-ai-specialized-agent-evaluation/) o ve directamente al [proyecto final del curso de flujos de trabajo con IA](/articles/effective-ai-capstone/). Para conocer opciones de entornos de ejecución, consulta la [guía de entornos de agentes](/articles/best-ai-agent-harnesses/).

**Navegación del curso:** [Anterior: Delegación de agentes](/articles/effective-ai-agent-delegation/), [Índice del curso](/effective-ai-course-start/).
