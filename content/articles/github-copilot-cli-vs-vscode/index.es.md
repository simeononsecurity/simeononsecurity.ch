---
title: "GitHub Copilot CLI frente a VS Code: comparación de flujos de trabajo de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara el agente de terminal de Copilot con su experiencia en VS Code, incluido el contexto del editor, las diferencias visuales, el modo Agent, la integración CLI y las políticas de cuenta."
genre: ["Herramientas para desarrolladores", "Inteligencia artificial", "Desarrollo de software"]
tags: ["GitHub Copilot CLI frente a VS Code", "Copilot CLI", "GitHub Copilot", "VS Code", "modo Agent", "CLI frente a GUI", "contexto del editor", "sugerencias en línea", "diferencia visual", "sesiones de Copilot", "agente de terminal", "flujo de GitHub", "revisión de código", "integración IDE", "herramientas MCP", "permisos del agente", "AI Credits", "herramientas de desarrollo", "asistente de programación", "automatización"]
cover: "/img/cover/github-copilot-cli-vs-vscode.webp"
coverAlt: "Indicación de terminal conectada a una selección del editor y una diferencia visual en un espacio de programación azul y verde"
coverCaption: ""
---

**GitHub Copilot CLI y Copilot en VS Code ofrecen puntos de entrada distintos para el trabajo de programación.** CLI empieza con el shell y una tarea. VS Code combina contexto del editor, sugerencias, chat y flujos de agente. Evalúa ambos bajo la misma política de cuenta y repositorio.

**La elección no es exclusiva.** GitHub documenta una conexión entre Copilot CLI y VS Code. Una tarea desde terminal aprovecha la selección del editor y la revisión visual cuando conectas ambas interfaces de forma explícita.

## Puntos clave

- **Usa Copilot CLI para tareas desde terminal** y llamadas programáticas compatibles.
- **Usa Copilot en VS Code para trabajo centrado en el editor**, incluida la asistencia en línea y el modo Agent.
- **Conecta CLI con VS Code** cuando necesites indicaciones de terminal con contexto y diferencias del editor.
- **Verifica la cuenta, el modelo y las políticas**, incluso dentro de una misma familia de productos.

**Alcance y fecha:** Se revisó la documentación oficial el 10 de octubre de 2026. Esta comparación cubre el CLI independiente `copilot` y Copilot en VS Code, no la antigua extensión `gh copilot` ni un agente en la nube asignado a un issue de GitHub. Necesitas un repositorio comprobable y acceso permitido a Copilot. Reserva una hora para la prueba.

## Tres formas de trabajar

| Flujo | Interacción principal | Tarea de prueba adecuada |
|---|---|---|
| **CLI independiente** | Indicación de terminal y salida de comandos | Explicar y corregir un fallo de prueba reproducido |
| **Integración con VS Code** | Selección del editor, chat, sugerencias y diferencias | Modificar una función seleccionada y sus pruebas |
| **CLI conectado a VS Code** | Tarea de terminal con contexto y revisión del editor | Investigar desde shell y revisar el parche visualmente |

**El modo híbrido sigue siendo una sesión CLI.** Ejecutarlo en una terminal integrada no lo convierte automáticamente en una conversación nativa del modo Agent del editor. Comprueba la sesión y la conexión activas en lugar de confiar en la ventana que contiene la indicación.

## Qué ofrece CLI

```bash
copilot
```

**El comando independiente actual inicia el agente de terminal.** La [descripción general de Copilot CLI](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli) de GitHub explica el uso interactivo y programático, además de la planificación y los permisos de herramientas. Evalúalo donde la salida de terminal sea la evidencia principal.

**Una buena primera tarea tiene un fallo concreto.** Entrega el comando que falla, el comportamiento esperado y una restricción contra refactorizaciones ajenas. Pide reproducir el problema antes de modificar archivos. Comprueba que la explicación final coincide con la salida observada.

**La automatización exige límites explícitos.** Consulta las [guías de uso de CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli) para conocer la invocación y los controles actuales. Define herramientas permitidas, límites de tiempo y manejo de salida antes de ejecutar trabajos sin supervisión. No conviertas una política interactiva de permisos en autorización global para un flujo.

**El aislamiento cambia el límite de la prueba.** GitHub documenta aislamiento local para restricciones de archivos, red y sistema, además de sandboxes en la nube para ejecución aislada. Una solicitud de directorio confiable y una opción de aprobación no sustituyen esos límites. Prueba el sandbox, la red y el alcance de escritura con un recurso inocuo antes de cambiar un repositorio real.

## Qué añade VS Code

**La experiencia de Copilot en el IDE incluye sugerencias, chat y tareas de agente.** La [descripción del IDE](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides) separa esas funciones. La asistencia en línea sirve cuando tú sigues siendo el editor principal. El modo Agent sirve para un resultado limitado que requiere cambios en varios archivos.

**El modo Agent edita y ejecuta comandos de forma iterativa.** La [guía del modo Agent](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode) describe seleccionar Agent en el chat, revisar cambios y ampliar herramientas mediante MCP. La disponibilidad y la aprobación de comandos dependen también de la configuración y la administración.

**Evalúa la transferencia de contexto de forma deliberada.** Selecciona una función y pide una explicación de su manejo de errores. Después solicita un cambio pequeño con una prueba independiente. Registra si necesitas aportar archivos vecinos o corregir una suposición del agente sobre el código seleccionado.

{{< figure src="copilot-terminal-editor-bridge.webp" alt="Indicación de terminal vinculada a una selección del editor y una diferencia de código lado a lado en un espacio de repositorio" caption="Una sesión CLI conectada combina la entrada de terminal con la revisión del editor" >}}

## Conecta las dos interfaces

```text
/ide
```

**Usa `/ide` en una sesión interactiva de Copilot CLI** para inspeccionar o cambiar la conexión de VS Code. La [guía de conexión](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code) documenta la coincidencia del espacio confiable, el uso compartido de la selección y la muestra de cambios propuestos como diferencias.

**La conexión automática depende de que coincida el espacio de trabajo.** Un CLI local no se conecta a un Codespace remoto solo porque coincida el nombre del repositorio. Ejecuta CLI en el entorno correspondiente. La autorización amplia de edición también omite el flujo de aprobación del diff propuesto. Revisa los permisos si desaparecen las indicaciones esperadas.

**Las transcripciones de CLI aparecen en la vista Sessions de VS Code**, con continuación mediante Resume in Terminal. Esto conserva el flujo de terminal. No supongas que convierte la conversación en una sesión nativa del agente del editor.

| Antes de conectar | Verifica |
|---|---|
| **Espacio de trabajo** | La carpeta deseada está abierta y es confiable |
| **Lugar de ejecución** | CLI y la integración del editor usan el mismo entorno |
| **Selección** | El código resaltado coincide con la solicitud actual |
| **Permisos** | La revisión de cambios propuestos sigue activa si se requiere |
| **Sesión** | Continúa la conversación deseada |

## Modelos, facturación y política

**Usa el mismo modelo seleccionado para probar ambas interfaces cuando esté disponible.** Si las opciones difieren, registra la diferencia. Otro modelo, contexto o conjunto de herramientas cambia el experimento más allá de la diferencia gráfica y terminal.

**Verifica la contabilidad de uso actual de tu cuenta.** La documentación del modo Agent de GitHub menciona AI Credits. No apliques estimaciones antiguas de solicitudes premium sin revisar el acuerdo de facturación. Una indicación de CLI y una tarea del editor no equivalen automáticamente a una unidad de trabajo.

**El acceso de la organización es un requisito.** Si falta una función, revisa la política antes de reinstalar la extensión. Registra las herramientas e integraciones aprobadas para ambas superficies. Iniciar sesión con un proveedor no concede autoridad para modificar todos los repositorios ni contactar todos los servicios externos.

## Ejecuta una prueba pareada

**Prepara dos copias de la misma revisión inicial.** Usa instrucciones y pruebas de aceptación iguales. Realiza el primer intento en el CLI independiente y el segundo en el modo Agent de VS Code. Haz un tercer intento con CLI conectado solo si la interacción mixta encaja con tu trabajo habitual.

| Medida | Motivo para registrarla |
|---|---|
| **Contexto suministrado** | Revela el esfuerzo manual oculto de preparación |
| **Corrección** | Distingue código plausible de una solución verificada |
| **Pasos de aprobación** | Muestra la carga de supervisión bajo la misma política |
| **Tiempo de revisión** | Mide el esfuerzo para entender todo el parche |
| **Reparaciones manuales** | Captura el trabajo pendiente después del agente |
| **Uso** | Relaciona el coste con los resultados aceptados |

**Mantén la recuperación dentro de la prueba.** Rechaza un enfoque propuesto y explica el motivo. Observa si el siguiente intento conserva el trabajo útil y respeta la corrección. Esto revela más sobre el uso diario que una demostración única sin interrupciones.

## Solución de problemas y siguientes pasos

**Si CLI se conecta a la ventana equivocada**, revisa `/ide` y selecciona el espacio correcto. Si deja de aparecer la aprobación visual, revisa los permisos amplios de edición. Si Agent no está disponible, revisa el estado de la extensión y la política de la organización.

**Elige el CLI independiente** cuando dominen el contexto del shell y la invocación repetible. **Elige VS Code** cuando dominen el contexto por selección, el trabajo en línea y la revisión gráfica. **Usa el CLI conectado** cuando la entrada de terminal y la inspección del editor funcionen bien juntas.

**Para comparar proveedores**, lee la [comparación principal de CLI](/articles/cli-coding-agents-comparison/) o la [comparación principal de GUI](/articles/gui-coding-agents-comparison/). Mantén esas evaluaciones separadas de esta prueba de interfaces de una misma familia.
