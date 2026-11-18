---
title: "Paquetes de tareas de IA: mejores instrucciones y criterios de aceptación"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Convierte solicitudes vagas para una IA en paquetes de tareas con un resultado, una fuente, un alcance de archivos, verificaciones y una condición de parada definidos."
genre: ["Inteligencia artificial", "Productividad", "Ingeniería de software"]
tags: ["redacción de instrucciones para IA", "paquete de tareas", "instrucción para agente de programación", "criterios de aceptación", "flujo de trabajo de IA", "instrucciones para agentes de IA"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "Una solicitud vaga reformulada como un paquete breve de tareas con fuente, alcance, verificación y condición de parada"
coverCaption: ""
---

[Volver al curso práctico de flujos de trabajo con IA](/effective-ai-course-start/)

**Una buena instrucción describe el trabajo y cómo evaluarás el resultado.** Añadir palabras no corrige la falta de alcance. Esta lección convierte una solicitud vaga en un paquete de tareas para el laboratorio del curso.

**Objetivo de aprendizaje:** escribirás un paquete de tareas acotado con fuente, alcance de archivos, verificaciones y una condición de parada.

## Ideas clave

- **Resultado** nombra el artefacto o comportamiento que deseas.
- **Alcance** nombra los archivos permitidos y las acciones excluidas.
- **Fuente** identifica el requisito aprobado.
- **Criterios de aceptación** hacen observable el éxito.
- **Condiciones de parada** evitan suposiciones y trabajo posterior no autorizado.

## Antes de empezar

**Requisitos previos:** el laboratorio extraído, su archivo `docs/requirements.md` y la [lección sobre el contexto del repositorio](/articles/effective-ai-agents-md-context/). Reserva 30 minutos. El nivel es principiante. El ejercicio termina con un paquete escrito. Aún no hace falta editar código.

## Compara dos solicitudes

**Solicitud vaga:** «Mejora el script de tareas». Un agente podría reescribir la salida, añadir dependencias, editar datos de ejemplo u omitir pruebas. La solicitud no define ninguna de esas decisiones.

**Solicitud acotada:** «Añade un filtro de estado opcional a `task_report.py` según la revisión 1 de `docs/requirements.md`. Conserva la salida predeterminada. Añade pruebas. No cambies datos de ejemplo. Detente antes del commit». El agente sigue eligiendo detalles de implementación, mientras la tarea define qué significa tener éxito.

| Parte del paquete | Ejemplo del laboratorio | Verificación |
|---|---|---|
| **Resultado** | Añadir `--status` al informe | Funcionan ambos valores aceptados |
| **Fuente** | `docs/requirements.md`, revisión 1 | El código coincide con los valores aprobados |
| **Alcance** | Solo el programa y las pruebas | El diff no contiene otros archivos |
| **Restricciones** | Conservar la salida predeterminada y los datos de ejemplo | La salida base sigue siendo `Total tasks: 4` |
| **Evidencia** | Comando de prueba y ejecuciones manuales | Las salidas coinciden con los recuentos esperados |
| **Parada** | No hacer commit ni push | El historial de Git y el remoto no cambian |

## Usa una plantilla reutilizable

**Copia esta plantilla** para una tarea pequeña de programación o investigación. Elimina los campos irrelevantes en vez de rellenarlos con texto impreciso.

```text
Resultado:
Fuente autorizada y revisión:
Archivos o registros pertinentes:
Cambios permitidos:
Cambios y acciones excluidos:
Ejemplos del comportamiento deseado:
Comprobaciones de finalización:
Cuándo detenerse o preguntar:
Informe con:
```

**Para el laboratorio,** el paquete completo queda así:

```text
Objetivo: añade un filtro --status opcional a task_report.py.
Fuente: docs/requirements.md, revisión 1.
Archivos pertinentes: task_report.py, tasks.json, tests/.
Cambios permitidos: task_report.py y pruebas específicas.
Excluido: tasks.json, dependencias nuevas, commits y envíos.
Ejemplos: sin filtro muestra Total tasks: 4. open y done muestran 2 cada uno.
Comprobaciones: ejecuta las pruebas unitarias y cuatro comandos manuales: sin filtro, open, done y un valor no válido.
El valor no válido debe devolver un código distinto de cero con un mensaje claro.
Detente o pregunta si hay conflicto de fuentes, falta un archivo o falla una prueba inicial no relacionada.
Informe: archivos modificados, comandos, resultados observados y asuntos pendientes.
```

**En Windows,** usa `py -3` en los comandos del paquete si tu entorno utiliza el lanzador de Python.

**El paquete no prescribe cada línea de código.** Deja que el agente elija una implementación pequeña y mantiene el resultado comprobable.

## Añade ejemplos con cuidado

**Un ejemplo preciso reduce la ambigüedad.** Los ejemplos `open` y `done` especifican la salida para el archivo suministrado de cuatro tareas. No establecen una regla general para todos los archivos. En otro archivo, los recuentos dependen de sus registros.

**Separa lo esperado de lo observado.** Antes de ejecutar el programa, `Total tasks: 2` es el resultado esperado para cada estado. Después de ejecutarlo, la salida del terminal es una observación. Si los valores difieren, inspecciona los datos y la implementación antes de declarar el éxito.

## Practica una condición de parada

**Supón que falta el archivo de requisitos.** El paquete lo nombra como fuente aprobada. Detente y solicita el requisito en vez de deducir los valores aceptados de un chat antiguo o un problema de ejemplo.

**Supón que las pruebas iniciales fallan antes de editar.** Registra el fallo y pregunta si debes corregir primero el estado inicial. Una ejecución posterior satisfactoria no permite saber si la diferencia provino del filtro o del estado de partida.

**Supón que el agente quiere hacer un commit.** El paquete excluye los commits. Pídele que se detenga tras el diff y las pruebas. Tú decides si un commit posterior encaja en el flujo del proyecto.

## Revisa el paquete

**Asigna un punto por cada respuesta:** ¿el resultado es concreto? ¿Se nombra la fuente que rige? ¿Está claro el alcance de archivos? ¿Se indican al menos dos verificaciones observables? ¿Hay una condición de parada? Una puntuación inferior a cinco significa que debes revisar el paquete antes de delegar.

**Tu entregable:** guarda el paquete final y una explicación de una línea sobre una condición de parada. Dáselo a un agente de programación en la próxima lección práctica o responde manualmente a los resultados esperados en la ruta de estudio.

## Comprueba lo aprendido

1. **Pregunta:** ¿Qué hace que un paquete de tareas sea verificable? **Respuesta:** Una fuente, los archivos permitidos, verificaciones observables y una condición de parada.
2. **Pregunta:** ¿Qué debe hacer un agente si la fuente omite un detalle necesario? **Respuesta:** Detenerse e informar del detalle ausente en vez de inventarlo.

## Solución de problemas

- **El agente cambia demasiado:** indica los archivos y las acciones excluidas en el paquete.
- **El agente hace muchas preguntas:** proporciona la fuente que falta o un ejemplo concreto.
- **El agente afirma que terminó demasiado pronto:** solicita las salidas observadas de los comandos e inspecciona los archivos.
- **El paquete crece demasiado:** sustituye el material copiado de la fuente por su ruta y revisión.

## Próximos pasos

**Continúa con [Tu primera tarea con un agente de programación](/articles/effective-ai-coding-agent-first-task/)**. Usa el paquete para guiar una edición pequeña del laboratorio.

**Navegación del curso:** [Anterior: Contexto del repositorio](/articles/effective-ai-agents-md-context/), [Temario del curso](/effective-ai-course-start/).
