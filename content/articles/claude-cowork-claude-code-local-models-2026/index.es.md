---
title: "Claude Cowork y Claude Code con modelos locales: guía de configuración 2026"
date: 2026-09-22
lastmod: 2026-11-12
toc: true
draft: false
description: "Configura Ollama con Claude Desktop y Claude Code mediante una API compatible con Anthropic. Revisa los modelos y las funciones exclusivas de la nube en 2026."
genre: ["IA local", "Herramientas de programación con IA", "IA autohospedada", "Herramientas para desarrolladores", "Privacidad", "Modelos de código abierto", "Automatización", "Hardware para IA"]
tags: ["claude cowork", "claude code", "modelos locales claude desktop", "ollama claude code", "anthropic base url", "anthropic_auth_token", "modelo local claude code", "usar claude sin conexión", "agente local de programación con IA", "ollama launch claude", "claude desktop ollama", "programación local con llm", "programación privada con IA", "programación con IA sin conexión", "agente local de IA", "qwen3.8", "modelo glm en la nube", "modelos con llamadas a herramientas", "configurar claude code", "claude code gratis", "claude sin clave de API", "ventana de contexto de modelo local", "llama.cpp", "ollama cloud", "privacidad en la programación con IA", "IA aislada de la red", "herramientas de IA para devops"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "Espacio de trabajo moderno con una computadora que muestra una interfaz de programación, una tableta y altavoces inteligentes sobre un fondo azul oscuro con acentos luminosos de colores."
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Las herramientas de agente de Claude ya funcionan con modelos en tu propio hardware, sin clave de API, suscripción ni datos que salgan de tu equipo.** Ollama ofrece una API compatible con Anthropic a la que Claude Code y Claude Desktop se conectan con unos pocos comandos.

*Muchas guías pasan por alto un detalle importante. Describen Claude Cowork y luego dan pasos que configuran la herramienta de línea de comandos. Son dos integraciones distintas y solo una ofrece Cowork.*

Esta guía explica ambas rutas por separado, la variable de entorno que omiten los tutoriales populares, los modelos adecuados para cada una en septiembre de 2026 y las funciones que siguen siendo exclusivas de la nube sin importar la configuración.

**Al terminar esta guía:** identificarás la integración que necesitas, la conectarás mediante la ruta documentada de Ollama y comprobarás el endpoint con una prueba de llamada a herramienta. La inferencia local mantiene las solicitudes al modelo en tu equipo solo si eliges un modelo local y evitas las funciones basadas en la nube.

## Respuesta breve

**Ollama se conecta con Claude de dos maneras distintas. Elegir la incorrecta es la razón más común por la que alguien termina una guía con una terminal funcional, pero sin Cowork.**

| Integración | Qué ofrece | Ruta de configuración | Plataforma |
|---|---|---|---|
| **Claude Desktop** | Cowork, subagentes, búsqueda web, modo automático | Aplicación Ollama, luego **Apps** y **Connect Claude** | **Solo macOS** |
| **Claude Code** | El agente de programación CLI con llamadas a herramientas y edición de archivos | `ollama launch claude` o variables de entorno | macOS, Linux, Windows |

**Si quieres Cowork, usa la integración de Claude Desktop.** Es un proceso gráfico en la aplicación Ollama y solo está disponible en macOS. La compatibilidad con Windows sigue figurando como próxima.

**Si quieres un agente en la terminal, usa Claude Code.** Basta un comando.

*Ambos son gratuitos. El único costo es el hardware y la electricidad.*

## Dos integraciones, no una

La confusión empieza con los nombres. **Claude Cowork es una función de Claude Desktop**, no una aplicación independiente ni un sinónimo de Claude Code.

La documentación de Ollama los incluye en páginas y secciones separadas. Claude Desktop aparece en **Assistants**, junto a OpenClaw y Hermes. Claude Code está en **Coding**, junto a OpenCode, Cline y Codex CLI.

La diferencia importa porque la configuración cambia por completo:

- **Claude Desktop** se configura desde la interfaz de la aplicación Ollama. No modificas un perfil de shell.
- **Claude Code** se configura con variables de entorno o un único comando de inicio.

Una guía que te pide exportar `ANTHROPIC_BASE_URL` y ejecutar `claude` ha configurado la herramienta de línea de comandos. Si esperabas la experiencia de escritorio de Cowork, **no hay nada roto en tu configuración. Configuraste otro producto.**

## Configurar Claude Desktop y Cowork

Esta ruta se realiza en la aplicación Ollama, no en la terminal.

### Requisitos previos

- **Ollama instalado** en macOS. La compatibilidad con Windows figura como próxima.
- **Un modelo descargado de antemano** si quieres ejecutarlo localmente. Para usar un modelo en la nube, inicia sesión en Ollama y habilita los modelos cloud. Algunos requieren un plan de pago.
- **Claude instalado.** Si falta, Ollama ofrece descargarlo durante la configuración.

### Pasos

1. Abre Ollama y selecciona **Apps**.
2. Selecciona **Connect Claude**.
3. Sigue las instrucciones. Instala Claude si aparece la solicitud y reinícialo cuando se indique.

Ese es todo el proceso. Para cambiar de modelo después, abre **Ollama Settings**, ve a **Apps**, elige los modelos y selecciona **Restart Claude**.

### Funciones disponibles

La documentación de Ollama indica que esta integración admite cuatro funciones:

- **Cowork**, para completar tareas difíciles
- **Subagentes**, para dividir tareas grandes entre agentes
- **Web search**, proporcionada de forma predeterminada por Ollama
- **Auto mode**, que permite al agente decidir cuándo pedir permiso antes de hacer cambios

*Cowork figura en la lista. Está disponible con esta integración, pero no con la de línea de comandos.*

### Desconectar

Al desconectar se restaura la configuración anterior de Claude, por lo que el cambio no es destructivo.

- Desde la interfaz, abre **Apps**, desconecta Claude y reinícialo cuando se indique.
- Desde una terminal, ejecuta `ollama launch claude-desktop --restore`.
- **Si cierras Ollama mientras Claude está conectado, también se restaura la configuración habitual de Claude.** Deja Ollama en ejecución si quieres conservar la configuración local.

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Diagrama de la aplicación Ollama conectándose a Claude Desktop desde el panel Apps, la selección del modelo en los ajustes de Ollama y la ruta para restaurar la configuración original" >}}

## Configurar Claude Code desde la CLI

Esta es la ruta que cubren casi todas las guías y la adecuada para trabajar en la terminal.

### Método de un solo comando

```bash
ollama launch claude
```

El comando define las variables de entorno necesarias, dirige Claude Code a tu instancia local de Ollama e inicia el programa. Elige un modelo de la lista y pulsa Enter. Para indicar el modelo de antemano, añade la opción:

```bash
ollama launch claude --model qwen3.5
```

*El wrapper se encarga del entorno. Lee la siguiente sección de todos modos, porque saber lo que configura te ayudará a solucionar problemas.*

### Definir las variables de entorno manualmente

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**La segunda línea es la que omiten las guías populares.** Asignar una cadena vacía a `ANTHROPIC_API_KEY` evita que una clave real ya presente en tu entorno interfiera con la conexión local. Si una guía publicada omite esa línea, los lectores que ya tengan una clave exportada recibirán un error confuso.

Para no modificar el perfil del shell, pasa todo directamente en la línea de comandos:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

Dos detalles de la documentación oficial:

- **`ANTHROPIC_AUTH_TOKEN` contiene la autenticación bearer**, por eso en el modo local lleva el texto literal `ollama`.
- **Los archivos de ajustes de Claude tienen prioridad sobre las variables del shell.** Si la conexión se comporta de forma extraña después de exportar valores nuevos, revisa esos ajustes y ejecuta `/status` en Claude Code para ver qué endpoint se usa.

### Conectarse directamente a Ollama Cloud

No necesitas instalar Ollama para esta ruta. Define una clave de API y apunta Claude Code al endpoint alojado de Ollama:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**Esta ruta tiene una limitación.** La documentación de Ollama indica que la búsqueda web alojada y los controles avanzados de herramientas no son totalmente compatibles. El chat básico, la edición de archivos y las llamadas a herramientas funcionan con modelos compatibles.

## Modelos para septiembre de 2026

La oferta de modelos cambió mucho durante 2026, así que conviene revisar los consejos publicados en primavera.

| Modelo | Tipo | Contexto | Motivo para elegirlo |
|---|---|---|---|
| **Qwen3.8 27B** | Local, 18 GB | 256K | El mejor modelo local de propósito general actual, con visión, llamadas a herramientas y control del razonamiento |
| **Qwen3 Coder Next** | Local, MoE 80B total / 3B activos | 256K | Diseñado para agentes de programación permanentes, con un modo rápido sin razonamiento |
| **Qwen3.6 35B A3B** | Local, MoE 35B / 3B activos | 262K | Apache 2.0 y eficiente con memoria limitada |
| **kimi-k2.7-code:cloud** | Nube | Amplio | Modelo cloud centrado en programación que no requiere hardware local |
| **glm-5.3-flash** | Nube | Amplio | El primer modelo que recomienda la propia documentación de Ollama |

**Empieza con Qwen3.8 27B si tienes suficiente memoria.** Funciona localmente con una ventana de contexto de 256K, visión nativa, llamadas a herramientas y razonamiento que se activa por solicitud. Una tarjeta con al menos 24 GB es adecuada para el uso diario.

**Empieza con un modelo cloud si no tienes esa memoria.** Probar Claude Code con un modelo alojado no cuesta nada y elimina la cuestión del hardware, aunque tu código sale del equipo.

### Advertencia sobre los modelos ternarios

En nuestra **[guía de IA local](/articles/local-ai-2026-build-your-rig-now/)** explicamos que el modelo ternario Bonsai 2 27B ejecuta un modelo completo de 27B en **5,53 GiB**. Es tentador usarlo aquí.

**No funciona con este flujo de trabajo.** Los kernels ternarios están en la bifurcación de llama.cpp de Prism ML, y Ollama estándar no carga esos archivos. Un comando como `ollama launch claude --model Ternary-Bonsai-2-27B` falla antes de empezar la inferencia. Usa el paquete estándar Qwen3.8 27B con Claude Code y reserva los paquetes ternarios para un runtime compatible.

*La comodidad y la eficiencia máxima requieren opciones distintas. Las herramientas integradas esperan un GGUF estándar.*

## Configura un contexto de 64K antes de culpar al modelo

La documentación de Ollama da una instrucción directa para trabajar con repositorios: elige un modelo y **establece una ventana de contexto de al menos 64K**. Auméntala para repositorios más grandes.

Claude Code carga el contenido de archivos, las diferencias y la salida de comandos en la ventana de contexto. Si el valor predeterminado es pequeño, se queda sin espacio a mitad de una tarea. El fallo parece un problema de razonamiento, pero se debe a la configuración.

| Contexto | Qué permite hacer |
|---|---|
| Menos de 32K | Editar un archivo y responder preguntas rápidas |
| **64K** | Trabajar con varios archivos en un repositorio modesto |
| 128K | Repositorios más grandes y salidas de comandos extensas |
| 256K | La ventana completa de Qwen3.8 27B |

*Si Claude Code pierde el hilo a mitad de una tarea, revisa el contexto antes de cambiar de modelo.*

## Verificar las llamadas a herramientas con un comando

Las llamadas a herramientas distinguen a un agente de un generador de texto. Comprueba que funcionen en lugar de darlo por hecho.

Cuando Claude Code esté en ejecución, pídele:

```text
Lee el directorio actual y enumera todos los archivos
```

**Si muestra archivos reales, las llamadas a herramientas funcionan.** Si responde que leería el directorio y describe lo que espera encontrar, la función no está conectada. Estás hablando con un modelo de chat al que se añadió una instrucción de programación, no con un agente. Ninguna indicación adicional lo arreglará.

Comprueba los problemas en este orden:

1. **Cambia a un modelo con compatibilidad confirmada con herramientas.** No todos los modelos la ofrecen y la cantidad de parámetros no permite distinguirlos.
2. **Confirma que el entorno apunte a Ollama.** Ejecuta `ollama --version` y comprueba que `ANTHROPIC_BASE_URL` señale tu endpoint local.
3. **Ejecuta `/status` en Claude Code.** Una URL base o credencial en los ajustes de Claude tiene prioridad sobre las variables del shell que acabas de exportar.

## Qué funciones siguen siendo exclusivas de la nube

Conoce este límite antes de reconstruir un flujo de trabajo en torno a la inferencia local.

| Función | Modelos locales | Nube |
|---|---|---|
| Chat y edición de archivos | Sí | Sí |
| Llamadas a herramientas | Depende del modelo | Sí |
| Subagentes | Sí | Sí |
| Búsqueda web | Proporcionada mediante Ollama | Sí |
| **Cowork** | Mediante Claude Desktop | Sí |
| Modo automático | Mediante Claude Desktop | Sí |
| Indicaciones programadas | Mediante `/loop` en Claude Code | Sí |

En el entorno local hay tres advertencias:

- **El razonamiento con varios archivos se deteriora antes que la velocidad.** Un modelo local maneja bien un archivo, de forma aceptable tres y mal un repositorio entero. Ajusta el tamaño de la tarea.
- **Algunos modelos cloud requieren un plan de pago de Ollama.** También necesitas iniciar sesión y habilitarlos.
- **La ruta directa a la nube tiene límites funcionales.** Si omites la instalación local, la búsqueda web alojada y los controles avanzados de herramientas no son totalmente compatibles.

*La inferencia local destaca en tareas acotadas y verificables y funciona peor en trabajos amplios y ambiguos. Organiza el trabajo teniendo en cuenta esa diferencia.*

## Automatizar

Dos funciones permiten ir más allá de las sesiones interactivas.

### Ejecuciones sin interfaz para scripts y CI

La opción `--yes` omite los selectores interactivos y descarga el modelo si hace falta. Requiere `--model`, y todo lo que venga después de `--` se envía directamente a Claude Code:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Ten en cuenta el modelo de permisos.** Claude Code pide confirmación antes de la mayoría de las acciones, así que una ejecución sin interfaz requiere reglas de permisos configuradas o un entorno aislado. No dirijas un agente desatendido a un repositorio que te importe.

### Indicaciones programadas con `/loop`

Dentro de una sesión de Claude Code, `/loop` ejecuta una indicación o comando slash a intervalos:

```text
/loop 30m Revisa mis PR abiertas y resume su estado
/loop 1h Investiga las últimas noticias de IA y resume los avances clave
/loop 15m Revisa las nuevas incidencias de GitHub y ordénalas por prioridad
```

*Esto se ejecuta mientras la sesión está abierta. No es un servicio en segundo plano, por lo que termina al cerrar la sesión.*

## Solución de problemas

| Síntoma | Causa probable | Solución |
|---|---|---|
| **Conexión rechazada** | Ollama no está en ejecución | Ejecuta `ollama serve` y confirma con `curl http://localhost:11434/api/tags` |
| **Describe las acciones en lugar de ejecutarlas** | El modelo elegido no admite llamadas a herramientas | Cambia a un modelo con compatibilidad confirmada |
| **Se usa una clave de API real en lugar del endpoint local** | `ANTHROPIC_API_KEY` sigue exportada | Asígnale una cadena vacía, como se muestra arriba |
| **Cowork no aparece después de la configuración** | Se configuró la CLI de Claude Code en lugar de Claude Desktop | Para Cowork, usa el flujo **Apps** de Ollama |
| **La generación es lenta** | El contexto es demasiado grande o se eligió un modelo denso cuando basta uno disperso | Reduce el contexto y luego prueba un modelo mixture-of-experts |
| **Las variables exportadas no tienen efecto** | Los ajustes de Claude prevalecen sobre las variables del shell | Revisa los archivos de ajustes y ejecuta `/status` |
| **Fallan las solicitudes en segundo plano** | Claude Code usa un modelo pequeño para tareas internas | Configura la sustitución del modelo pequeño para que use el mismo modelo local |

*Dos de estos siete problemas tienen la misma causa. La mayoría de los fallos de configuración se deben a un endpoint incorrecto o a un modelo sin llamadas a herramientas.*

## Puntos clave

- **Claude Desktop y Claude Code son integraciones distintas.** Cowork forma parte de Claude Desktop y se configura en macOS desde el panel **Apps** de Ollama. La ruta CLI no ofrece Cowork.
- **Un comando inicia la ruta CLI:** `ollama launch claude`. La configuración manual requiere tres variables y **muchas guías omiten `ANTHROPIC_API_KEY=""`**.
- **No necesitas una instalación local.** Apunta Claude Code a `https://ollama.com` con una clave de API.
- **Establece un contexto de al menos 64K antes de evaluar un modelo.** Una ventana pequeña parece un fallo de razonamiento.
- **Verifica las llamadas a herramientas con una solicitud.** Si el modelo describe lo que haría, tienes un generador de texto, no un agente.
- **Los paquetes Bonsai ternarios no funcionan aquí.** Requieren la bifurcación de llama.cpp de Prism ML, que Ollama estándar no puede cargar.
- **Desconectar es seguro.** Cerrar Ollama restaura la configuración anterior de Claude. También puedes ejecutar `ollama launch claude-desktop --restore` desde la terminal.

## Próximos pasos

1. **Instala Ollama y descarga un modelo con compatibilidad confirmada con herramientas** antes de configurar Claude: **[Biblioteca de modelos de Ollama](https://ollama.com/library)**
2. **Lee la página de Claude Code de Ollama** para ver las opciones y modelos actuales: **[Integración de Claude Code](https://docs.ollama.com/integrations/claude-code)**
3. **Consulta la página de Claude Desktop** si quieres usar Cowork: **[Integración de Claude Desktop](https://docs.ollama.com/integrations/claude-desktop)**
4. **Elige el hardware antes de comprarlo**, con los niveles de memoria de nuestra guía de inferencia local: **[IA local en 2026: un modelo 27B supera a Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. **Comprueba qué puede manejar un equipo pequeño** si quieres un agente permanente en un dispositivo de bajo consumo: **[¿Qué modelos de IA funcionan en una Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Artículos relacionados

| Artículo | Qué incluye |
|---|---|
| **[IA local en 2026: un modelo 27B supera a Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Referencia de rendimiento para inferencia local, cuantización ternaria y selección de hardware |
| **[¿Qué modelos de IA funcionan en una Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)** | Inferencia local para un asistente pequeño que siempre está activo |
| **[Crear un asistente de IA para Meshtastic que protege la privacidad](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un modelo local conectado a una radio sin red, con la privacidad como prioridad |
| **[Mejores extensiones de VS Code para el desarrollo de IA](/articles/best-visual-studio-code-extensions-for-ai/)** | Herramientas de edición para combinar con un agente local de programación |

## Referencias

1. [Integración de Claude Code - documentación de Ollama](https://docs.ollama.com/integrations/claude-code)
2. [Integración de Claude Desktop - documentación de Ollama](https://docs.ollama.com/integrations/claude-desktop)
3. [Biblioteca de modelos de Ollama](https://ollama.com/library)
4. [Qwen3.8 - biblioteca de modelos de Ollama](https://ollama.com/library/qwen3.8)
5. [Claude Cowork con modelos locales - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Bifurcación de llama.cpp de Prism ML - kernels ternarios](https://github.com/PrismML-Eng/llama.cpp)
