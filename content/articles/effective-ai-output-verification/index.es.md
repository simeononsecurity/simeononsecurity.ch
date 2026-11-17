---
title: "Cómo verificar la salida, las fuentes, las pruebas y los costes de la IA"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Crea un registro de aceptación para un resultado de IA mediante la comprobación de fuentes, alcance de archivos, evidencias de pruebas, privacidad y uso."
genre: ["Inteligencia artificial", "Ingeniería de software"]
tags: ["verificar resultados de IA", "verificación de datos de IA", "revisión de agentes de programación", "evidencia de pruebas de IA", "seguimiento de costes de IA", "revisión humana"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "Una hoja de revisión que compara una afirmación de IA con un archivo fuente, un diff de código, la salida de pruebas y el total de uso"
coverCaption: ""
---

[Volver al curso Flujo de trabajo práctico con IA](/effective-ai-course-start/)

**Acepta un resultado de IA solo después de comprobar las pruebas adecuadas para la tarea.** Una explicación pulida, una herramienta configurada y un indicador de pruebas correctas responden a preguntas distintas. Esta lección crea un único registro de revisión para el laboratorio del taller.

**Objetivo de aprendizaje:** crearás un registro de aceptación de fuentes, alcance de archivos, pruebas, privacidad y uso.

## Ideas clave

- **Comprobación de fuentes:** compara una afirmación basada en hechos con un registro autorizado y vigente.
- **Comprobación del alcance:** inspecciona los archivos o sistemas que cambiaron.
- **Comprobación del comportamiento:** ejecuta pruebas y casos manuales pertinentes.
- **Comprobación de privacidad:** inspecciona qué información recibió la herramienta o el proveedor.
- **Comprobación del uso:** registra tokens, llamadas a herramientas y la tarifa usada para calcular el coste.

## Antes de empezar

**Requisitos previos:** el laboratorio del curso, `docs/requirements.md`, una instantánea local de Git y la [lección sobre MCP](/articles/effective-ai-mcp-server-setup/) o su alternativa en el navegador. Reserva 40 minutos. La dificultad es intermedia. Usa el laboratorio que editaste en la primera tarea con un agente de programación. Si omitiste la edición, usa una extracción nueva y marca las comprobaciones de funcionalidades como no implementadas. La línea base sin modificar aún supera sus dos pruebas originales.

## Comprobar una afirmación basada en hechos

**Afirmación:** «Los valores de estado aprobados son `open` y `pending`». Abre `docs/requirements.md`, revisión 1. Indica `open` y `done`. La afirmación es incorrecta. Un tono seguro no cambia el requisito.

**Para afirmaciones sobre productos,** usa documentación oficial vigente y registra el título de la página y la fecha de revisión. Una afirmación sobre un menú, plan, comando o límite de contexto queda obsoleta antes que un principio general de flujo de trabajo. La [documentación de Codex](https://learn.chatgpt.com/docs/codex/cli), la [documentación de Claude Code](https://code.claude.com/docs/en/overview) y la [documentación de OpenCode](https://opencode.ai/docs/) describen sus interfaces actuales.

| Afirmación | Fuente | Decisión |
|---|---|---|
| **`open` y `pending`** | Requisito del laboratorio, revisión 1 | Rechazar, sustituir `pending` por `done` |
| **El recuento sin filtros es 4** | Programa de línea base y cuatro entradas JSON | Comprobar al ejecutar el programa |
| **Se produjo una lectura MCP** | Transcripción de herramientas de la sesión | Aceptar solo si aparece una llamada a la herramienta |

## Inspeccionar el cambio

**Para una tarea de programación,** usa Git para enumerar los archivos modificados y leer el diff real. Un archivo nuevo sin seguimiento aparece en el estado aunque no figure en un diff normal, así que revisa ambos.

```bash
git status --short
git diff -- task_report.py tests
```

**Alcance previsto:** tras la tarea de filtros, solo cambian `task_report.py` y las pruebas específicas. Un cambio en `tasks.json`, `docs/requirements.md` o un archivo de configuración oculto necesita explicación y revisión aparte. Si no has ejecutado una edición, no debería haber cambios.

## Probar el comportamiento

**Ejecuta las mismas comprobaciones de línea base y funcionalidades** desde la carpeta extraída del laboratorio. Son las comprobaciones cuyos resultados observados debe indicar el informe de finalización del agente.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**En la copia editada,** las pruebas cubren los casos nuevos, los recuentos son 4, 2 y 2, y el valor no válido termina con un error claro. En una copia de inicio nueva, solo pasan las dos pruebas de línea base y el recuento total de 4. Registra ese estado inicial por separado.

**Un fallo en las pruebas de la funcionalidad requiere diagnóstico.** Si `open` muestra 4, comprueba si el argumento de filtro llega a la función de recuento y si el programa compara el campo `status` de la tarea. No describas una prueba fallida como aprobada porque el agente diga que terminó la implementación.

## Revisar privacidad y acceso

**Registra qué archivos recibió el agente.** El laboratorio contiene datos sintéticos y ningún secreto. Un proyecto real podría incluir credenciales, datos de clientes o documentos privados. Antes de compartir resultados, inspecciona las instrucciones, registros, capturas de pantalla y diffs para detectar esos valores.

**Una prueba local solo demuestra el comportamiento local.** No demuestra los permisos de una cuenta en la nube, el alcance de un servidor MCP ni un servicio desplegado. Prueba cada límite en el entorno donde importa.

## Registrar uso y costes

**Los tokens miden el volumen de entrada y salida del modelo.** Los paneles de los productos difieren, así que usa las cifras de uso de tu proveedor. Registra por separado las llamadas a herramientas y los cargos por imágenes o entornos alojados cuando corresponda. Consulta las tarifas vigentes antes de calcular una factura real.

**Abre la vista de uso de la cuenta que ejecutó la tarea.** Registra los tokens de entrada y salida mostrados, el modelo, el periodo de facturación y cualquier categoría de entrada almacenada en caché. En las suscripciones de ChatGPT o Claude, un límite o una asignación de uso no equivale al coste de API de una tarea. Para una ejecución de OpenCode con API o proveedor, consulta el uso o la facturación de ese proveedor y sus tarifas actuales. Si el producto no muestra tokens por tarea, escribe «no disponible» y no deduzcas un cargo a partir de la longitud del chat.

**Cálculo ilustrativo, no representa precios de un proveedor:** 30.000 tokens de entrada a 1 $ por millón cuestan 0,03 $. 5.000 tokens de salida a 5 $ por millón cuestan 0,025 $. El cargo combinado del modelo en este ejemplo es 0,055 $, antes de cargos por herramientas o alojamiento.

```text
coste de entrada = tokens de entrada / 1.000.000 × tarifa de entrada
coste de salida = tokens de salida / 1.000.000 × tarifa de salida
total = coste de entrada + coste de salida + cargos independientes de herramientas
```

**Una tarea de trabajo también consume tokens.** Delegar desplaza el resultado detallado fuera de la conversación principal, pero no hace que el trabajo sea gratis. Compara el coste con el valor de la comprobación independiente.

**Mantén separadas las categorías de cargos.** La entrada almacenada en caché, la entrada nueva, la salida, las llamadas a herramientas y la ejecución alojada pueden tener tarifas distintas. Este ejemplo usa solo tarifas de entrada nueva y salida. No dice nada sobre una factura de suscripción ni un cargo de herramienta.

## Mantener un registro de aceptación

| Campo | Ejemplo cumplimentado tras la edición |
|---|---|
| **Fuente** | `docs/requirements.md`, revisión 1, leído |
| **Archivos modificados** | `task_report.py` y `tests/test_task_report.py` en `git status --short` |
| **Pruebas** | Pasaron las pruebas de línea base y de filtros nuevos, registra el recuento observado |
| **Salida manual** | Se observaron `Total tasks: 4`, `2` y `2`, valor no válido rechazado |
| **Estado de la funcionalidad** | `--status open` y `--status done` implementados |
| **Privacidad** | Solo archivos sintéticos |
| **Uso** | Registra las cifras de tu proveedor, si las tienes |
| **Decisión** | Acepta solo cuando pasen las comprobaciones de fuentes, diff, pruebas y privacidad |

**Tu artefacto:** copia este registro y complétalo después de tu propia ejecución. Sustituye «observado» solo por una salida que hayas visto. Usa Aceptar cuando pasen todas las comprobaciones requeridas, Revisar cuando el arreglo tenga un alcance acotado y Detener cuando la fuente, el alcance o el acceso no estén claros.

## Comprueba lo aprendido

1. **Pregunta:** ¿Una línea base inicial aprobada demuestra que existe la funcionalidad solicitada? **Respuesta:** No. Prueba el comportamiento de aceptación nuevo después de la edición.

2. **Pregunta:** ¿Qué debe incluir un registro de aceptación? **Respuesta:** Evidencia de la fuente, archivos modificados, comprobaciones de comportamiento, alcance de acceso y uso observado.

## Solución de problemas

- **No hay fuente para una afirmación:** márcala como no verificada y busca un registro autorizado.
- **Las pruebas pasan pero la salida difiere:** añade un caso manual e inspecciona los datos.
- **Falta el uso:** registra «no disponible» en lugar de estimar un cargo real.
- **El diff incluye datos privados:** deja de compartir la salida y elimina esos datos del registro de práctica.

## Siguientes pasos

**Continúa con [Delegación de agentes](/articles/effective-ai-agent-delegation/)**. Para más detalles sobre costes y privacidad, lee [enrutamiento de proveedores](/articles/openrouter-provider-routing-quality-cost/) y [límites de privacidad de la IA local](/articles/local-ai-privacy-boundary/).

**Navegación del curso:** [Anterior: Configuración de MCP](/articles/effective-ai-mcp-server-setup/), [Índice del curso](/effective-ai-course-start/).
