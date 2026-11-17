---
title: "Configuración del curso de flujos de trabajo con IA: terminal, Git y laboratorio práctico"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Prepara un espacio seguro para practicar con IA, aprende los términos de terminal y Git del curso y ejecuta el laboratorio inicial."
genre: ["Inteligencia artificial", "Ingeniería de software", "Educación"]
tags: ["configuración de curso de IA", "fundamentos de terminal", "fundamentos de Git", "requisitos previos para agentes de programación", "laboratorio práctico de IA", "curso de IA para principiantes"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Un espacio de práctica para principiantes con símbolos de terminal, Python y Git, una carpeta de laboratorio marcada y un archivo de reinicio"
coverCaption: ""
---

[Volver al curso práctico de flujos de trabajo con IA](/effective-ai-course-start/)

**Prepara un espacio seguro antes de usar un agente.** Las lecciones 1 y 2 funcionan en un navegador sin este laboratorio. Vuelve aquí antes de la lección 3 si quieres completar el curso. Las lecciones prácticas de programación usan Git, Python 3.10 o posterior y un agente de programación. La ruta de estudio sustituye las acciones no disponibles del agente por tareas manuales identificadas.

**Resultado de aprendizaje:** ejecutarás el laboratorio inicial, guardarás una línea base local y explicarás cómo restablecer una copia desechable.

## Puntos clave

- **Ruta de navegador:** completa los ejercicios de chat, planificación, comprobación de fuentes y revisión en ChatGPT o Claude.
- **Ruta local:** usa una terminal y el laboratorio de Python incluido para los ejercicios de programación.
- **Ruta de reinicio:** extrae una copia nueva del laboratorio cuando un ejercicio salga mal.
- **Regla de seguridad:** mantén los archivos privados, los registros de clientes y las credenciales fuera del laboratorio.

## Elige tu ruta

| Ruta | Requisitos | Práctica |
|---|---|---|
| **Introducción en navegador** | Navegador actualizado y una cuenta de ChatGPT o Claude | Lecciones 1 y 2, además del paquete de tareas de chat de la lección 1 |
| **Práctica local** | Git, Python 3.10 o posterior, terminal y un agente de programación | Archivos, diferencias, pruebas y cambios del agente |
| **Curso de estudio** | Navegador, Python 3.10 o posterior local y Git | Comprobaciones completas del laboratorio; los pasos de agente y MCP no disponibles se marcan como no ejecutados |

**Cada producto define sus propios planes y límites.** Consulta [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) y [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) antes de depender de una función. La ruta de estudio no demuestra habilidad práctica con un agente de programación no disponible. Anota esa diferencia en tus notas de finalización.

**Sigue una ruta predeterminada:** usa ChatGPT en el navegador para los ejercicios de chat y luego un agente de programación disponible con el laboratorio local. Claude es una alternativa equivalente para el chat. Codex CLI, Claude Code CLI y OpenCode son opciones para la etapa de programación. No necesitas tener cuentas con todos los proveedores.

**Anota cinco comprobaciones antes de abrir un agente de programación.** Así distingues una comprobación del laboratorio local de una afirmación sobre una cuenta o un espacio de trabajo alojado.

| Comprobación | Anota |
|---|---|
| **Espacio de trabajo** | La carpeta exacta del laboratorio extraído que leerá el agente |
| **Ejecución** | Computadora local o espacio remoto seleccionado |
| **Proveedor** | Cuenta o proveedor del modelo usado para esta tarea |
| **Permisos** | Si se permiten escrituras de archivos y comandos de shell, o si requieren aprobación |
| **Línea base** | Cantidad observada y dos pruebas aprobadas antes de editar |

**Mantén acotada la carpeta raíz de práctica.** Un espacio alojado necesita su propia copia del laboratorio sintético. Una ejecución local no demuestra que la copia remota o la cuenta tenga los mismos archivos y permisos.

## Aprende los términos locales

| Término | Significado sencillo |
|---|---|
| **Terminal** | Aplicación donde escribes comandos |
| **Shell** | Software que interpreta esos comandos |
| **CLI** | Interfaz de línea de comandos de un programa |
| **Directorio de trabajo** | Carpeta que usa un comando de forma predeterminada |
| **Repositorio** | Proyecto cuyo historial registra Git |
| **Commit** | Instantánea guardada de Git |
| **Rama** | Línea con nombre para los cambios de Git |
| **Diferencia** | Vista de las líneas añadidas o eliminadas |
| **Prueba** | Comprobación repetible del comportamiento esperado |
| **Código de salida** | Número que indica si un comando tuvo éxito o falló |

**No necesitas GitHub para el laboratorio inicial.** Git funciona en tu computadora. GitHub es un servicio de alojamiento independiente. Un commit local guarda una instantánea sin enviar tus archivos a ningún sitio.

## Prepara el laboratorio

**Descarga el [laboratorio inicial del curso](/downloads/effective-ai-course-lab.zip)** y extráelo en una carpeta nueva que controles. Abre una terminal dentro de ella. En macOS o Linux, abre Terminal y usa `cd` para entrar en la carpeta extraída. En Windows, usa PowerShell o Windows Terminal y `cd` para entrar. En Windows, suele usarse `py -3` en lugar de `python3`.

**Instala [Python 3.10 o posterior](https://www.python.org/downloads/) y [Git](https://git-scm.com/downloads) si hace falta.** Comprueba las herramientas instaladas antes de ejecutar el laboratorio. Los dos primeros comandos muestran los números de versión. `cd` cambia el directorio de trabajo. `ls` muestra los archivos. Sustituye la ruta de ejemplo por la ruta real de la carpeta extraída.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**En Windows PowerShell,** usa `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` y `Get-ChildItem`. Entre los archivos listados deben aparecer `task_report.py`, `tasks.json`, `tests` y `docs`. Si falla un comando de versión, termina la instalación antes de continuar.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**En Windows PowerShell,** sustituye `pwd` por `Get-Location` si lo prefieres, y `python3` por `py -3` si Python usa el iniciador. La primera orden muestra la ruta. Debe terminar en la carpeta del laboratorio extraído. Comprueba también los nombres de archivo. Un archivo llamado `AGENTS.md.txt` no sirve como `AGENTS.md`. En el Explorador de Windows, activa las extensiones de nombre para ver el nombre completo.

**Resultado esperado:** el informe dice `Total tasks: 4`. El comando de pruebas muestra dos pruebas y termina con `OK`. El shell devuelve el código de salida cero si todo sale bien. Si aparece otro total o un traceback, detente y revisa la carpeta y la configuración de Python.

**Interpreta cada comando por partes.** En `python3 task_report.py tasks.json`, `python3` inicia Python, `task_report.py` es el programa y `tasks.json` es un argumento que indica los datos de entrada. La cantidad impresa es el resultado, no otro comando. Tras un fallo, macOS y Linux muestran el estado con `echo $?`. PowerShell expone el último estado de un programa nativo mediante `$LASTEXITCODE`.

**Calcula unos diez minutos para la primera ejecución** una vez instalado Python: extrae el laboratorio, ejecuta el informe y compara el total con las cuatro entradas de `tasks.json`. Abre el archivo JSON en un editor de texto y cuenta las entradas.

## Practica Git con seguridad

**Inicia Git solo dentro de la carpeta del laboratorio extraído.** Estos comandos guardan una instantánea local. `git status` muestra si cambiaron archivos. `git diff` muestra las líneas modificadas después de editar un archivo con seguimiento.

```bash
git init
git add .
git commit -m "Línea base del laboratorio del curso"
git status --short
```

**Estado esperado:** después del commit no aparece ningún nombre de archivo. Si Git pide un nombre y un correo, configura una identidad solo para el laboratorio desde esta carpeta y vuelve a ejecutar el commit. Sustituye los valores de ejemplo por los tuyos y privados. No pegues la salida de identidad ni de credenciales en un chat público.

```bash
git config --local user.name "Estudiante del curso"
git config --local user.email "learner@example.invalid"
git commit -m "Línea base del laboratorio del curso"
git status --short
```

**Para restablecerlo no necesitas comandos de Git.** Guarda las notas fuera del laboratorio, elimina la copia de práctica extraída y vuelve a extraer el ZIP original. Usa este reinicio si la edición de una lección deja el programa en un estado desconocido.

## Protege tu espacio de práctica

**Usa ejemplos sintéticos.** No cargues documentos privados en un proyecto del curso. No pongas claves de API en prompts, archivos fuente, capturas de pantalla ni commits. El acceso del agente a archivos y comandos depende de sus permisos y de la carpeta que abras. Revisa ambos antes de permitir su ejecución.

**Comprueba el uso compartido antes de cargar archivos.** Los miembros del proyecto podrían tener acceso a los archivos. Sigue la política de tu organización para el trabajo real. El curso usa datos ficticios, así que el laboratorio no requiere una aprobación especial.

## Practica y comprueba

**Tu resultado:** anota la ruta elegida, los cinco campos de preflight, el total del informe, el resultado de las pruebas y el método de reinicio. Usa una copia nueva para confirmar que sabes restablecer el laboratorio.

**Razonamiento esperado:** sabes qué carpeta afectan los comandos, distingues Git local del alojamiento y tienes una forma de recuperarte antes de que un agente edite archivos.

## Comprueba lo aprendido

1. **Pregunta:** ¿La introducción solo con navegador completa la ruta del laboratorio local? **Respuesta:** No. La ruta completa requiere una línea base local de Python y Git.

2. **Pregunta:** ¿Qué debes guardar antes de cambiar el laboratorio desechable? **Respuesta:** El resultado aprobado de las pruebas iniciales y un punto limpio para reiniciar.

## Solución de problemas

- **Falta el comando de Python:** instala Python 3 desde su distribuidor oficial y vuelve a abrir la terminal.
- **No se encuentra el archivo:** comprueba el directorio de trabajo y muestra los archivos de la carpeta extraída.
- **Las pruebas no se ejecutan:** usa el comando exacto del README del laboratorio extraído.
- **Git pide una identidad para el commit:** configura Git localmente y no incluyas esos valores en las notas del curso.

## Próximos pasos

**Continúa con [el flujo de trabajo de IA fiable](/articles/effective-ai-workflow-foundations/)**. El primer ejercicio usa el mismo taller sintético antes de que cualquier herramienta reciba archivos reales.

**Navegación del curso:** [Índice del curso](/effective-ai-course-start/).
