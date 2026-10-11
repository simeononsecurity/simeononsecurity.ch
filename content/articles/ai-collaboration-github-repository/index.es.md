---
title: "Colaboración de IA en GitHub: límites del repositorio y de la revisión"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Crea un mapa de fuentes basado en GitHub, asigna propietarios de archivos y establece un límite de publicación protegido para contribuciones de IA revisadas."
genre: ["Inteligencia artificial", "Colaboración de equipos", "Ingeniería de software"]
tags: ["curso de colaboración de IA", "repositorio de GitHub", "protección de ramas", "CODEOWNERS", "mapa de fuentes", "revisión de pull requests", "controles de publicación"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustración de profesionales que revisan trabajo compartido en un espacio de ciberseguridad"
coverCaption: ""
---

[Volver al curso de colaboración de IA](/ai-collaboration-course-start/)

**El mantenedor crea el límite de publicación basado en GitHub** después de aprobar el acta. Los requisitos, la configuración, la política y los procedimientos operativos viven en un repositorio desechable. Los colaboradores proponen cambios mediante Issues y pull requests. Tú defines dónde viven los hechos aprobados y bloqueas los cambios sin revisión antes de conectar agentes.

## Puntos clave

- **`main` protegido** es el límite de publicación.
- **Las Issues** reúnen trabajo propuesto sin aprobar políticas.
- **CODEOWNERS** asigna revisores elegibles para cada archivo.
- **Usuarios separados** demuestran los controles de revisión y denegación.

## Antes de comenzar

**Requisitos previos:** la [base del piloto](/articles/ai-collaboration-pilot-foundation/), el laboratorio extraído, un administrador del repositorio y revisores separados de producto y operaciones. **Tiempo estimado:** 60 minutos. **Dificultad:** moderada.

**Límite del plan:** GitHub documenta ramas protegidas para repositorios públicos en Free y repositorios privados en Pro, Team o Enterprise. Usa repositorios públicos solo para contenido sintético. Comprueba la visibilidad y el plan en la referencia de ramas protegidas antes de confiar en la aplicación de estas reglas.

**Resultado:** terminas con una rama de publicación protegida, propietarios de archivos, un mapa de fuentes y una prueba de denegación registrada como evidencia.

## Crear el repositorio

1. **Crea `export-service-lab`** con un README y la rama predeterminada **`main`**.
2. **Copia el laboratorio extraído** en la raíz del repositorio y conserva **`check.py`**, **`test_check.py`** y **`baseline/`**. Copia los archivos de registro de referencia a la raíz como registros iniciales.
3. **Crea `docs/project-map.md`** usando el registro de la base. Añade **`docs/policy.md`** con el POL-01 aprobado.
4. **Crea `docs/decisions/DEC-12.md`** con la aprobación del acta, los roles, la decisión de referencia y el estado.
5. **Confirma el arranque** como administrador. Registra esta excepción inicial. Activa la protección antes de las contribuciones posteriores.

**Ruta de arranque local para Git Bash, Terminal de macOS o un shell de Linux:** inicia sesión en GitHub desde un navegador, abre el repositorio nuevo, selecciona **Code** y copia su URL HTTPS de clonación. En un directorio de trabajo desechable, ejecuta los comandos siguientes. Sustituye las dos rutas de marcador por la URL y la ruta del ZIP del laboratorio descargado. No pegues un token en la URL.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

El comando clone debe dar nombre al directorio del repositorio. Si `unzip` no está disponible, extrae el ZIP con el administrador de archivos y copia su contenido en este checkout, dejando intacto el README del repositorio. `git status --short` debe mostrar los registros copiados, el comprobador, las pruebas y `baseline/` como archivos nuevos. Guarda `docs/project-map.md`, `docs/policy.md` y `docs/decisions/DEC-12.md` del paquete de la base con un editor de texto. Después ejecuta:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git debe mostrar un ID de commit nuevo y después un push correcto a `main`. El estado corto final debe estar vacío. Abre el repositorio de GitHub en una vista nueva del navegador y confirma que los archivos y el ID del commit aparecen en `main`. Guarda la URL del commit como evidencia de arranque. Si Git solicita la identidad del autor, sigue el puente de configuración del centro del curso. Si falla la autenticación, usa el flujo de credenciales compatible con GitHub y repite el mismo push. Si la rama o el remoto son incorrectos, detente e inspecciona `git branch --show-current` y `git remote -v` antes de escribir de nuevo. Si el push se rechaza porque la protección ya estaba activa, abre una rama de propuesta y una PR en lugar de evadir la regla. La ruta exclusiva del navegador sigue disponible mediante un mantenedor.

| Registro | Ubicación | Propietario |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Propietario de política |
| **REQ-17** | `requirement.json` | Propietario de producto |
| **RUN-04** | `runbook.md` | Propietario de operaciones |
| **Comportamiento** | `config.json` | Mantenedor |
| **Decisiones** | `docs/decisions/` | Líder del proyecto |

**El mapa enlaza ubicaciones en lugar de copiar valores.** Mantén el README centrado en la configuración y el mapa. Repetir requisitos de retención crea divergencias incluso dentro de un solo repositorio.

## Asignar propietarios de archivos

**Genera `.github/CODEOWNERS`** localmente con identificadores reales del entorno aislado. Introduce los identificadores sin el **`@`** inicial. Conserva las identidades de las cuentas en tu laboratorio privado, no en la evidencia pública del ejercicio.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

**Los propietarios necesitan acceso de escritura** para que GitHub los reconozca. Inspecciona el archivo CODEOWNERS en el navegador para detectar errores. Protege los archivos de propietarios y las definiciones de flujo de trabajo junto con el contenido normal.

**Varios nombres en una línea no requieren la aprobación de todos.** GitHub acepta la aprobación de un propietario elegible para la ruta correspondiente. Usa propietarios designados distintos para las rutas de requisitos y procedimientos. El piloto también requiere declaraciones de producto y operaciones vinculadas a la propuesta final.

## Proteger la publicación

1. **Abre Settings, Branches** y añade una regla de protección de ramas para **`main`**. Usa la ruta de protección de ramas de forma coherente en lugar de mezclarla con rulesets durante este ejercicio.
2. **Exige una pull request**, dos revisiones aprobatorias y una revisión de los propietarios del código.
3. **Descarta las aprobaciones obsoletas** después de nuevos commits y exige resolver las conversaciones.
4. **Activa No permitir omitir las configuraciones anteriores.** Mantén desactivadas las subidas forzadas y la eliminación.
5. **Añade la comprobación de consistencia** después de su primera ejecución en el módulo siguiente. Exige que las ramas estén actualizadas antes de fusionarlas.

**Dos aprobaciones imponen una cantidad, no pertenencia a roles empresariales.** CODEOWNERS añade cobertura de propietarios por ruta. El mantenedor también comprueba las dos declaraciones de roles. Registra este control procedimental de forma explícita en lugar de describirlo como aplicación automatizada de dos roles.

**Los administradores siguen gestionando la configuración.** Captura la regla antes y después de las pruebas. No concedas acceso de administrador a un agente ni uses un token privilegiado para demostrar la denegación del colaborador.

## Verificar el límite

| Intento | Resultado esperado |
|---|---|
| **El colaborador envía una rama** | Propuesta permitida |
| **El colaborador publica directamente** | Publicación protegida denegada |
| **Un revisor aprueba** | La fusión queda bloqueada por el umbral de revisión |
| **Un commit nuevo sigue a la revisión** | Se requiere una aprobación nueva |
| **Un archivo sensible carece de cobertura de propietario** | Reparar antes de publicar |

**Usa la sesión de navegador del colaborador para inspeccionar la ruta.** El editor web de GitHub no edita una rama **`main`** protegida. Un aviso para crear una rama muestra la ruta compatible con el navegador. No demuestra que el servidor haya rechazado un push directo. Para obtener evidencia de denegación de plataforma, pide a un colaborador con acceso Git local aprobado que intente un push directo e inofensivo a **`main`** protegida y conserva la respuesta del servidor. Marca esta prueba de denegación como Bloqueada cuando no haya acceso local.

**Lee `main` después de la denegación** y confirma que la revisión no cambió. Registra el rol del actor, la acción intentada, el resultado y la revisión de origen. Un asistente que promete no publicar aporta evidencia de comportamiento, no una prueba de permisos de plataforma.

**Usa el clon local autenticado del propio colaborador para la prueba de push directo.** Un token del mantenedor probaría la identidad equivocada. Esta respuesta ilustrativa muestra el tipo de evidencia del servidor que debes conservar. El texto exacto varía según las reglas del repositorio.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Si la autenticación Git local no está disponible, marca la denegación del servidor como Bloqueada.** Conserva el aviso de rama del navegador como evidencia de ruta y pide al mantenedor que organice una prueba separada con un colaborador. No clasifiques el aviso de ruta como un push directo rechazado.

## Crear un mapa de fuentes útil

**Un mapa de fuentes es un documento de enrutamiento**, no un segundo documento de requisitos. Alguien que llega desde el chat debe encontrar la intención actual, el comportamiento implementado y las instrucciones operativas sin elegir entre resúmenes que compiten.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**No pongas el valor actual de retención en cada entrada del mapa.** Un mapa que contiene “siete días” se convierte en otro valor que sincronizar después de PROP-042. Conserva identificadores y ubicaciones estables en el mapa, y lee el valor del registro autorizado.

**Protege los cambios del mapa como cambios de enrutamiento.** Redirigir REQ-17 a un archivo de borrador cambia la selección de fuentes aunque el requisito aprobado permanezca intacto. Revisa el destino, el propietario y el alcance de autoridad cada vez que cambie el mapa.

## Separar la base y la propuesta

**La raíz del repositorio contiene los registros activos del laboratorio.** El directorio **`baseline/`** descargado es un recurso didáctico. No es automáticamente la base protegida para cada PR posterior. Cuando el trabajo revisado llega a **`main`**, los registros protegidos de la raíz definen la base de la propuesta siguiente.

| Ubicación | Propósito | ¿Editar durante PROP-042? |
|---|---|---|
| **Requisito/configuración/procedimiento de la raíz** | Registros activos propuestos en la rama | Sí, mediante cambios revisados |
| **`baseline/`** | Recurso original del ejercicio sin conexión | No |
| **Worktree confiable separado** | Registros protegidos capturados de la raíz | No |
| **`context.json`** | Evidencia de los bytes de la base capturada | Regenerar después de reconciliar |

**Mantén separados los cambios de control y los de retención.** Primero inicia el comprobador y las reglas de revisión. Después propone el cambio de siete a treinta días. Combinar una reescritura de política, una reescritura de flujo y un cambio de valor dificulta distinguir controles reparados de controles eludidos.

## Revisar el cambio completo

**Abre los archivos modificados antes de aceptar una descripción de PR.** La descripción explica la intención del autor. El diff revela el cambio enviado. Para PROP-042, inspecciona la revisión del requisito, las exclusiones de alcance, la configuración, el procedimiento, la base de la propuesta y la evidencia del manifiesto.

1. **Revisión de producto:** confirma la intención de treinta días y las exclusiones sin cambios.
2. **Revisión de operaciones:** confirma que el procedimiento coincide con la configuración propuesta y conserva la limitación de ejecución.
3. **Revisión del mantenedor:** inspecciona JSON, captura de origen, resultados de comprobación y cambios no relacionados.
4. **Revisión de control:** inspecciona por separado cualquier cambio de mapa, política, CODEOWNERS o flujo de trabajo.

**Una comprobación correcta no explica una eliminación no relacionada.** Si la rama elimina el documento de política mientras cambia la retención, solicita una propuesta separada o una revisión específica del propietario. Limitar el alcance mantiene comprensible el objeto de revisión.

## Diagnosticar una prueba de denegación

**Usa una acción intentada por cada fila de evidencia.** “El colaborador falló” es ambiguo. El usuario podría carecer de acceso normal de escritura, encontrar una limitación del navegador o chocar con la regla de rama prevista. Cada observación establece un límite distinto.

| Observación | Interpretación | Seguimiento |
|---|---|---|
| **No puede crear ninguna rama** | Falta acceso de contribución | Usa una ruta aprobada de Issue o fork |
| **Crea una rama, no puede publicar en main** | La ruta de publicación probada está restringida | Captura la revisión intacta de main |
| **La fusión se bloquea con una revisión** | El recuento de revisiones se aplica a la PR probada | Añade evidencia específica del rol |
| **El administrador publica pese a la regla** | La identidad probada omite el límite | Inspecciona la configuración de omisión y los permisos |

**Registra el rol y la acción sin exponer datos de cuenta** en la evidencia compartida del curso. Conserva los registros nativos del actor disponibles en privado para el revisor. Captura juntos la configuración de la regla, la operación intentada, la denegación y la revisión protegida resultante.

## Comprobación de finalización del repositorio

**Entrega un repositorio que otro colaborador pueda recorrer de forma independiente.** El README apunta al mapa, el mapa resuelve los registros autorizados, la cobertura de propietarios incluye rutas sensibles y la protección se aplica a **`main`**. Conserva una propuesta permitida y un intento de publicación denegado.

**No afirmes que existe aplicación basándote solo en la configuración.** La configuración establece el comportamiento previsto. El intento del entorno aislado establece el comportamiento observado para un rol y una ruta concretos. Lleva ambas pruebas a la lección de agentes y Actions.

## Solución de problemas y reversión

**Falta una solicitud de propietario:** confirma el acceso de escritura y la cobertura de rutas de la rama base. **Falta protección:** verifica el plan y la visibilidad. **La fusión sigue habilitada:** inspecciona el objetivo de la regla, la configuración de omisión y el recuento de revisiones.

**Reversión:** cierra las propuestas sin fusionar y desactiva la automatización del laboratorio. Revierte el contenido fusionado mediante otra PR revisada. Conserva la evidencia antes de eliminar el repositorio desechable. No debilites la protección para terminar una prueba fallida.

## Ejercicio y autoevaluación

**Propón una edición de `docs/policy.md`** como colaborador. Decide si la aprobación del mantenedor por sí sola establece la aprobación del propietario de la política.

**Razonamiento esperado:** el recuento de revisiones por sí solo no establece autoridad. La ruta necesita cobertura del propietario de política y revisión del rol actual. Enumera los requisitos específicos del rol que no estén aplicados como controles procedimentales.

## Referencias principales

- **Controles de plan y revisión:** [Ramas protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Elegibilidad de propietarios:** [Propietarios del código](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Contribución desde el navegador:** [Editar archivos](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Siguientes pasos

**Continúa con [Adaptadores de agentes y Actions](/articles/ai-collaboration-github-agents-actions/)** para conectar la evidencia de origen con comprobaciones ejecutables.
