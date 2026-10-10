---
title: "Comparativa de agentes de codificación CLI: Claude Code, Codex, Gemini, OpenCode, Copilot y Aider"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara seis agentes de codificación de terminal por flujo de trabajo, automatización, acceso a modelos, permisos y esfuerzo de revisión. Crea una lista corta con una prueba repetible en el repositorio."
genre: ["Herramientas para desarrolladores", "Inteligencia artificial", "Desarrollo de software"]
tags: ["agentes de codificación CLI", "Claude Code CLI", "Codex CLI", "Gemini CLI", "OpenCode CLI", "GitHub Copilot CLI", "Aider", "agentes de terminal", "automatización headless", "agent harness", "proveedores de modelos", "flujos de Git", "comparativa de agentes de codificación", "herramientas shell", "asistente de codificación", "permisos del agente", "contexto del repositorio", "automatización CI", "revisión de código", "herramientas para desarrolladores"]
cover: "/img/cover/cli-coding-agents-comparison.webp"
coverAlt: "Seis ventanas de terminal abstractas rodean un símbolo de repositorio en una cuadrícula equilibrada sobre un fondo oscuro"
coverCaption: ""
---

Los **agentes de codificación de terminal** comparten una interfaz conocida, pero difieren en cómo recopilan contexto, editan archivos, solicitan aprobación y encajan en scripts. Esta guía compara Claude Code CLI, Codex CLI, Gemini CLI, OpenCode CLI, GitHub Copilot CLI y Aider. Evalúa sus flujos de terminal de forma independiente de los productos de escritorio de cada proveedor.

**Empieza por tus restricciones.** El acceso al proveedor, la automatización repetible y los hábitos de revisión filtran mejor que una clasificación general. Las recomendaciones siguientes son juicios editoriales basados en documentación oficial revisada el 10 de octubre de 2026, no clasificaciones de rendimiento medido.

## Puntos clave

- **Claude Code, Codex y Gemini CLI** merecen una prueba si quieres sus respectivos flujos de modelos propios.
- **OpenCode y Aider** sirven para experimentar con varios proveedores de modelos, con enfoques distintos para la interacción y la edición.
- **Copilot CLI** merece atención cuando el acceso a GitHub y la política de la organización ya definen tu flujo.
- **Una interfaz de terminal no implica inferencia local**, elección libre de modelos ni ejecución desatendida.

**Requisitos previos:** Git, un checkout desechable, pruebas funcionales y credenciales de modelos aprobadas. La dificultad es intermedia. Reserva una tarde para comparar dos herramientas seleccionadas en tres tareas pequeñas.

## La lista corta

| Herramienta de terminal | Motivo para evaluarla | Decisión pendiente |
|---|---|---|
| **Claude Code CLI** | Trabajo de repositorio centrado en Claude | Ruta de cuenta y política de permisos |
| **Codex CLI** | Trabajo interactivo y ejecución mediante scripts | Ajustes de sandbox y gestión de salida |
| **Gemini CLI** | Flujo de Gemini y salida estructurada headless | Autenticación, cuotas y política de herramientas |
| **OpenCode CLI** | Selección de proveedor y agentes configurables | Compatibilidad del modelo y endpoint |
| **Copilot CLI** | Acceso a Copilot desde tu shell | Acceso de la organización y aprobación de herramientas |
| **Aider** | Programación en pareja centrada en Git | Selección de archivos y modelo de edición |

**Esta lista tiene un alcance definido.** Compara seis flujos de terminal establecidos, no todos los productos con CLI. Los editores y extensiones gráficas pertenecen a la [comparativa de agentes de codificación GUI](/articles/gui-coding-agents-comparison/).

## Claude Code y Codex

**Claude Code CLI** ofrece sesiones interactivas, conversaciones reanudables, entrada por pipe y un modo de impresión para scripts. Su [referencia de CLI](https://code.claude.com/docs/en/cli-reference) documenta esos puntos de entrada. Pruébalo si quieres que Claude trabaje en cambios del repositorio mientras diriges las tareas desde el shell.

**Codex CLI** expone inspección del repositorio, edición, ejecución de comandos y revisión en una interfaz de terminal. La [documentación de CLI de OpenAI](https://learn.chatgpt.com/docs/codex/cli) describe los controles interactivos. Su [modo no interactivo](https://learn.chatgpt.com/docs/non-interactive-mode) ofrece `codex exec` para scripts e integración continua.

**Elige entre ambos mediante trabajo completado.** Da a cada herramienta un error desconocido y una prueba existente que falle. Compara su explicación, el alcance del parche, la selección de pruebas y la recuperación después de un enfoque rechazado. Un mensaje final seguro no demuestra corrección.

## Gemini CLI y Copilot

**Gemini CLI** documenta el contexto del proyecto, las extensiones, la ejecución de herramientas y la automatización en su [guía oficial](https://geminicli.com/docs/). Su [referencia headless](https://geminicli.com/docs/cli/headless/) especifica la salida estructurada y los códigos de salida. Esto vuelve la gestión de salida una parte concreta de la prueba, no una suposición basada en la disponibilidad del terminal.

**GitHub Copilot CLI** admite trabajo interactivo y prompts programáticos mediante el comando independiente actual `copilot`. Su [documentación del producto](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli) cubre la planificación y los permisos de herramientas. Evalúalo con la cuenta y las políticas de tu equipo. La marca GitHub no concede acceso automático a todos los repositorios o servicios.

| Entrada de automatización | Familia de comandos documentada |
|---|---|
| **Claude Code** | `claude -p` |
| **Codex** | `codex exec` |
| **Gemini CLI** | `gemini -p` |
| **Copilot CLI** | `copilot -p` |

**El modo headless necesita una política de ejecución.** Define acciones permitidas, límites de tiempo, manejo de errores y recopilación de artefactos antes de poner un agente en un pipeline. Que un proceso termine con éxito no demuestra que el código generado cumpla tus criterios de aceptación.

## OpenCode y Aider

**OpenCode CLI** combina una interfaz de terminal interactiva con operaciones de línea de comandos. Su [referencia de CLI](https://opencode.ai/docs/cli/) documenta `opencode run`, mientras su [guía de proveedores](https://opencode.ai/docs/providers/) describe las conexiones de modelos. Pruébalo cuando la flexibilidad de proveedores justifique gestionar compatibilidad y facturación.

**Aider** se centra en la programación en pareja dentro de un repositorio Git. Su [documentación](https://aider.chat/docs/) cubre selección de archivos, mapas del repositorio, conexiones de modelos e integración de lint/test. Pruébalo cuando prefieras dirigir una conversación de edición acotada y mantener los cambios cerca de un flujo Git explícito.

**Los estilos de interacción distintos necesitan expectativas distintas.** Un asistente de edición limitado y un agente que explora un repositorio completo no consumen el contexto de la misma forma. Registra los archivos suministrados, la exploración permitida y la dirección humana necesaria. No atribuyas una mejora de productividad a una herramienta después de seleccionar tú mismo su contexto sin registrarlo.

{{< figure src="terminal-agent-evaluation-flow.webp" alt="Sesiones de terminal abstractas alimentan una revisión de parches compartida, una lista de pruebas y un registro del coste de la tarea" caption="Usa los mismos criterios de aceptación en cada flujo de terminal" >}}

## Modelos, acceso y coste

**El agente es el software que rodea al modelo.** Construye solicitudes, gestiona resultados de herramientas, mantiene el estado de la conversación y aplica la política de ejecución. El modelo y el endpoint de servicio influyen en el razonamiento, la fiabilidad de las llamadas de herramientas, la latencia y el contexto disponible.

**La flexibilidad del proveedor tiene costes operativos.** Un endpoint personalizado añade decisiones sobre identificadores de modelos, ajustes de contexto, autenticación y soporte de herramientas. Un servicio integrado reduce algunas opciones de configuración, pero vincula el acceso a su cuenta y sus políticas. Ninguna opción establece una clasificación universal de calidad.

| Categoría de coste | Incluir en la prueba |
|---|---|
| **Asignación de cuenta** | Acceso incluido, límites de frecuencia y comportamiento al agotarse |
| **Inferencia medida** | Uso de prompt, salida, cache y reintentos |
| **Servicio local** | Hardware, electricidad y mantenimiento del runtime |
| **Esfuerzo humano** | Configuración, correcciones y revisión final |
| **Trabajo fallido** | Ejecuciones abandonadas y parches revertidos |

**Compara el coste por cambio aceptado.** Separa las cuotas de suscripción de los cargos API incrementales y del tiempo del desarrollador. Un cliente gratuito con inferencia pagada difiere de una suscripción con asignación. Revisa las condiciones actuales de la cuenta antes de cambiar de proveedor.

**Fija las entradas de comparación.** Registra cada versión de CLI, identificador de modelo, proveedor, revisión inicial, modo de permisos y configuración de herramientas. Repite una tarea después de cambiar cualquiera de ellos. De lo contrario, un resultado mejor identifica un sistema cambiado, no una interfaz de terminal mejor.

## Permisos y contexto del repositorio

**La aprobación y el aislamiento son controles distintos.** Una solicitud de aprobación pregunta si una acción debe continuar. Un sandbox limita los recursos disponibles para una acción ejecutada. Comprueba ambos, incluido el acceso a archivos, red y comandos iniciados por las herramientas.

**La documentación de permisos de Codex** separa de forma explícita las reglas de sistema de archivos y red, incluidas las condiciones para aplicar restricciones de destino. Usa su [referencia de permisos](https://learn.chatgpt.com/docs/permissions) para inspeccionar la configuración instalada. Para cada herramienta candidata, prueba una acción permitida inocua y una acción prohibida inocua antes de confiar en la política.

**Las instrucciones del proyecto necesitan verificación.** Da a cada herramienta el mismo comando de compilación, criterios de aceptación y exclusiones mediante su mecanismo de instrucciones compatible. Pídele que repita las restricciones activas antes de editar. Un archivo de instrucciones ausente es un defecto de configuración, no un benchmark del modelo.

```text
Task: Fix the supplied reproduction without changing the public API.
Scope: Preserve unrelated work and avoid new dependencies.
Evidence: Run the existing regression test and relevant neighboring tests.
Report: Explain the cause, changed files, checks, and remaining uncertainty.
```

**Este prompt de prueba tiene límites intencionados.** Añade una reproducción conocida y comprobaciones escritas de forma independiente. Usa el mismo commit inicial en checkouts separados. Registra la versión de la herramienta, el modelo, el proveedor, la política de permisos, el tiempo transcurrido y las intervenciones.

## Elige tu primera pareja

| Tu prioridad | Empieza la prueba con |
|---|---|
| **Flujo Claude frente a OpenAI** | Claude Code CLI y Codex CLI |
| **Flujo Google frente a OpenAI** | Gemini CLI y Codex CLI |
| **Flexibilidad de proveedor** | OpenCode CLI y Aider |
| **Despliegue de GitHub existente** | Copilot CLI y una alternativa aprobada |
| **Claude frente a proveedores configurables** | Claude Code CLI y OpenCode CLI |

**Ejecuta tres tareas por herramienta:** un error reproducido, una función pequeña con pruebas independientes y una refactorización acotada. Conserva los intentos fallidos. Revisa los parches sin mirar qué agente los produjo si resulta práctico. El ganador es el flujo que produzca cambios aceptables con menos esfuerzo total en tu repositorio.

## Solución de problemas y siguientes pasos

**Los resultados inesperados suelen empezar en la configuración.** Herramientas ausentes, directorios de trabajo incorrectos, versiones de modelo distintas o asignaciones agotadas distorsionan las comparaciones. Verifica esos puntos antes de reescribir prompts repetidamente.

**Continúa con una guía enfocada:** [OpenCode frente a Claude Code](/articles/opencode-vs-claude-code/), [Codex CLI frente a escritorio](/articles/codex-cli-vs-desktop/), [Claude Code CLI frente a escritorio](/articles/claude-code-cli-vs-desktop/), [OpenCode CLI frente a escritorio](/articles/opencode-cli-vs-desktop/), o [Copilot CLI frente a VS Code](/articles/github-copilot-cli-vs-vscode/). Esas comparativas de interfaz se mantienen dentro de cada familia de productos.
