---
title: "Una fuente, muchas herramientas: marco de colaboración con IA para equipos mixtos"
date: 2026-10-01
lastmod: 2026-11-23
toc: true
draft: false
description: "Crea un sistema compartido de colaboración con IA con responsables de las fuentes, versiones de contexto, revisión de cambios duraderos y criterios claros para elegir entre un mapa de proyecto y RAG."
genre: ["Inteligencia artificial", "Gestión del conocimiento", "Ingeniería de software", "Colaboración en equipo"]
tags: ["marco de colaboración con IA", "equipos mixtos", "fuente de verdad", "agentes de IA", "AGENTS.md", "CLAUDE.md", "reglas de Cline", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "generación aumentada por recuperación", "RAG", "protocolo de contexto de modelos", "mapa del proyecto", "manifiesto de contexto", "gestión del conocimiento", "deriva documental", "aprobación humana", "registro de decisiones", "traspaso entre agentes", "versionado de políticas", "árboles de trabajo de Git", "controles de pull request"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustración de un grupo de profesionales que colabora en tareas de ciberseguridad"
coverCaption: ""
---

**Dos personas hacen la misma pregunta a dos herramientas de IA:** ¿cuánto tiempo debe conservar el servicio una exportación? En este ejemplo ilustrativo, el agente del IDE del desarrollador responde siete días basándose en un README. El asistente de chat de la responsable de operaciones responde treinta días desde una página wiki. Las dos respuestas suenan seguras. Cada herramienta leyó una copia distinta de la verdad.

**El fallo está en la propiedad de la información**, no en la calidad del prompt. El requisito del wiki cambió la semana pasada, pero nadie actualizó el README. El desarrollador pide al agente que corrija el proceso de retención. El agente sigue el documento antiguo y produce un parche limpio que restaura el comportamiento equivocado. Los revisores examinan el código sin ver la versión del requisito que guio la respuesta.

**Asigna un lugar a cada hecho.** Haz que cada herramienta lea desde ese lugar y encamina cada cambio duradero a través de una persona. El repositorio, el wiki y el tracker conservan funciones distintas. Necesitan autoridad explícita, responsables con nombre y un proceso compartido para mover la información.

**Esta guía ofrece un modelo que puedes aplicar esta semana**, con o sin generación aumentada por recuperación. Empieza con un mapa del proyecto, instrucciones versionadas, registros de pruebas y propuestas revisadas. Añade infraestructura de búsqueda solo cuando el problema de recuperación lo justifique.

**Tu primer resultado debe ser un registro de fuentes**, no un conector. Enumera cada tipo de hecho, su ubicación de autoridad, su responsable, su revisión actual y quién aprueba los cambios.

## Puntos clave

- **Asigna autoridad según el tipo de información**, en vez de forzar todo en una aplicación.
- **Trata la memoria y los índices de recuperación como cachés**, nunca como fuentes de política independientes.
- **Adjunta las versiones de las fuentes a las propuestas**, para que los revisores sepan qué hechos guiaron el cambio.
- **Exige aprobación fuera de los prompts**, con controles de acceso y revisiones obligatorias.
- **Comparte el proceso entre herramientas**, adaptando su presentación a cada interfaz.

## Antes de empezar

**Requisitos:** elige un proyecto piloto con un repositorio, un wiki o sistema documental, un tracker y responsables dispuestos a revisar cambios. Si el equipo no tiene wiki, usa un almacén documental versionado. Mantén igual el modelo de propiedad.

**Tiempo estimado:** reserva de dos a cuatro horas para el mapa y las plantillas iniciales, y luego una semana para el piloto. **Dificultad:** moderada. Lo difícil es acordar la autoridad, no instalar otra herramienta de IA.

**Alcance:** este es un modelo de trabajo propuesto. Sus reglas de aprobación y convenciones de nombres son recomendaciones. Claude Code, Codex, Cline, Cowork, Copilot y ChatGPT no garantizan ese comportamiento predeterminado. El índice automático enlaza con cada paso.

## Herramientas mixtas, contexto dividido

**Programadores y no programadores comparten un proyecto**, pero usan interfaces distintas. El desarrollador trabaja en un IDE o con un agente de terminal. El responsable de producto usa un proyecto de chat. La persona de operaciones trabaja desde un wiki y un tracker. Elige la interfaz según la tarea, no según el acceso a los hechos de autoridad.

**El contexto es el material disponible para la respuesta actual.** Revisa cada sesión en busca de archivos del repositorio, documentos cargados, historial de chat, memoria guardada, resultados de conectores y fragmentos recuperados. Dos sesiones con pruebas distintas pueden discrepar aunque reciban la misma pregunta.

| Fallo | Lo que observas |
|---|---|
| **Deriva documental** | Un README repite un requisito obsoleto |
| **Promoción de un resumen** | El resumen de una sesión se vuelve prueba sin su fuente original |
| **Escrituras simultáneas** | Dos agentes sustituyen la misma página desde versiones base distintas |
| **Decisiones perdidas** | Un acuerdo de reunión nunca llega al registro de decisiones |
| **Falta de procedencia** | Una respuesta plausible no indica versión de página ni commit |

**El ejemplo de retención muestra la diferencia.** El wiki describe el comportamiento objetivo aprobado. El código describe el comportamiento implementado. Ninguno debe reescribir al otro en silencio. Registra el desacuerdo y pregunta al responsable nombrado qué lado necesita cambiar.

> **Idea clave:** acuerda la autoridad antes de elegir una herramienta de IA. Empieza por definir el vocabulario.

### Recuadro: cinco términos compartidos

| Término | Significado en este marco |
|---|---|
| **Fuente** | Registro designado como autoridad para un tipo de información |
| **Caché** | Copia derivada que acelera o facilita el acceso |
| **Propuesta** | Cambio sugerido que espera aprobación del responsable |
| **Mapa del proyecto** | Índice de ubicaciones, identificadores y responsables de fuentes |
| **Manifiesto** | Registro de las pruebas exactas usadas en una respuesta o propuesta |

## Asigna un lugar a cada hecho

**Una fuente significa una autoridad por hecho**, no una sola base de datos para toda la organización. Define esta distribución durante el piloto y sustituye los cargos de ejemplo por los responsables reales del equipo.

| Tipo de información | Sistema de origen | Responsable | Quién escribe | Cómo leen los agentes |
|---|---|---|---|---|
| **Código, pruebas, configuración y esquemas** | Repositorio | Responsable de ingeniería | Colaboradores mediante PR revisado | Archivos de un commit registrado |
| **Documentación publicada y ADR** | Repositorio | Responsable técnico | Colaboradores mediante el mismo PR | Archivos versionados |
| **Requisitos** | Wiki | Responsable de producto | Responsable o editor aprobado | ID y revisión de página |
| **Procedimientos operativos** | Wiki | Responsable de operaciones | Editor aprobado | ID y revisión de página |
| **Política** | Wiki | Responsable de política | Editor aprobado tras revisión | Página canónica y adaptador local |
| **Decisiones entre equipos** | Registro de decisiones del wiki | Responsable de decisión nombrado | Responsable tras aprobar | ID y estado de decisión |
| **Tareas y hallazgos** | Tracker | Responsable de tarea | Personas o entrada de propuestas autorizada | Clave del issue y revisión |
| **Chats, resúmenes e incrustaciones** | Solo caché | Responsable de sesión o índice | Herramientas y participantes | Referencia, seguida de comprobaciones de fuente |

**Un registro de decisión de arquitectura (ADR)** pertenece junto al código cuando gobierna el diseño del repositorio. Una decisión entre equipos pertenece al registro compartido. Enlaza ambos registros cuando una decisión cubre los dos ámbitos, pero no mantengas copias independientes de su estado de aprobación.

**Las copias locales de política quedan subordinadas** a la página canónica. En cambio, las pruebas y esquemas del repositorio son fuentes dentro de su propio ámbito. La ubicación por sí sola no define la autoridad. El mapa sí.

**Una caché nunca sustituye una fuente.** Si un resumen dice siete días y el requisito aprobado dice treinta, usa el requisito para decidir el comportamiento objetivo. Conserva el resumen contradictorio como prueba de deriva y define después el proceso de escritura.

## Leer de la caché, proponer hacia arriba

**Los agentes incorporan pruebas al contexto de sesión** y luego redactan propuestas. No aprueban por sí solos hechos duraderos. Editar una rama de tarea o entregar un borrador no equivale a publicar política, fusionar código o aceptar una decisión.

```text
Fuente -> lectura con permisos comprobados -> contexto de sesión
Contexto de sesión -> propuesta + versión base -> revisión del responsable
Aprobación del responsable -> publicación controlada -> registro de cambios
Cambió la versión base -> concilia la propuesta -> solicita otra revisión
```

**Adjunta la versión base antes de pedir revisión.** El revisor necesita el valor anterior, el propuesto, la razón, las pruebas y los sistemas afectados. La aprobación debe referirse a una revisión concreta de la propuesta, no a un hilo de chat que sigue cambiando.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Conservar las exportaciones durante treinta días en vez de siete."
evidence:
  - "decision:DEC-12 aprobada"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**Los identificadores anteriores son ilustrativos.** Conserva una fila de registro por cada cambio lógico aprobado, con el ID de propuesta, registros afectados, versiones anterior y resultante, aprobador, fecha y referencia de fusión o publicación.

**Las personas son responsables de la decisión.** Un editor autorizado o una automatización restringida aplica la revisión aprobada. Limita las credenciales de escritura en consecuencia. Las instrucciones por sí solas no separan la redacción de la publicación.

## Contexto compartido sin RAG

**Un mapa del proyecto es el primer índice de recuperación.** Mantén una página por proyecto con ID de fuentes, ubicaciones del repositorio, claves del tracker, ámbitos de autoridad y responsables. Lee primero el mapa y luego recupera el registro pertinente por su ID.

### Recuadro: ejemplo de mapa de proyecto

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Los conectores directos reducen la copia manual.** El Model Context Protocol (MCP) es un protocolo de integración que expone herramientas y contexto a aplicaciones de IA. Usa conectores aprobados de wiki, tracker y repositorio cuando estén disponibles. Una consulta dirigida reduce el material irrelevante, pero no sustituye la autorización ni las comprobaciones de vigencia. Sigue la guía de seguridad MCP de las referencias para elegir permisos de conectores.

**La recuperación exacta requiere poca configuración.** Ofrece pruebas citables sin una base de datos vectorial. Sus límites también son claros: alguien mantiene el mapa, las preguntas abiertas requieren búsqueda adicional y las páginas grandes consumen espacio de sesión. Recupera la sección relevante con sus restricciones cercanas, no el manual entero.

**El trabajo sin conexión usa instantáneas explícitas.** Registra la revisión exportada y etiqueta las respuestas como basadas en una instantánea. No publiques cambios hasta que una persona o un conector autorizado compruebe la fuente actual. Después, muestra la misma política en cada interfaz.

## Una política, distintos adaptadores

**Mantén una política compartida**, y distribuye adaptadores breves para cada herramienta. Pon la versión aprobada en la primera línea de cada adaptador o conjunto de instrucciones copiado. Añade el ID de fuente y una instantánea local revisada para sesiones sin acceso a conectores.

**La carga de instrucciones depende de la herramienta.** Codex documenta la búsqueda por capas de **`AGENTS.md`**. Claude Code documenta **`CLAUDE.md`**, las importaciones y la memoria del proyecto. Cline documenta **`.clinerules/`** y los controles de reglas. Usa la documentación oficial enlazada en las referencias. Verifica las instrucciones cargadas en tu versión instalada en vez de suponer que todos los nombres de archivo se comportan igual.

### Recuadro: ejemplo de encabezado de AGENTS.md

```markdown
Versión de la política: v3 | Fuente: wiki:POL-01 | Estado: aprobada

# Instrucciones del proyecto

Lee el mapa del proyecto MAP-01 antes de iniciar una tarea.
Carga docs/policy-snapshot.md y registra su revisión de origen.
Trata la memoria de chat y los fragmentos de búsqueda como cachés.
Adjunta revisiones de fuentes a cada propuesta factual.
Usa una rama de tarea y un worktree por tarea de programación.
No publiques políticas, apruebes decisiones ni fusiones tu propio PR.
Detente si hay conflictos de fuentes sin resolver o escrituras solapadas.
Comprobaciones requeridas: pruebas, revisión documental y vigencia de políticas.
Responsables: mantenimiento de ingeniería, producto y política.
```

**Las instrucciones de un proyecto de chat reciben el mismo encabezado y proceso.** Una persona no programadora recibe la instantánea de política y el mapa mediante cargas o conectores aprobados. Si su interfaz no tiene acceso en directo, una persona facilita la exportación versionada y registra esa limitación.

**Una etiqueta de versión afirma algo, pero no prueba que el contenido sea idéntico.** Genera adaptadores desde la instantánea aprobada o compara sus partes de política con un digest guardado. Revisa aparte las excepciones específicas de cada adaptador. Durante el piloto, comprueba reglas desactivadas, anulaciones anidadas e instrucciones personales. Después registra las pruebas usadas en cada tarea.

## Registra un manifiesto de contexto

**Un manifiesto de contexto explica las pruebas de una respuesta.** Registra IDs y revisiones de páginas, claves de issues con su revisión u hora de actualización y el ID completo del commit del repositorio. Incluye la hora de recuperación y las secciones pertinentes. Marca los registros no disponibles en vez de sustituirlos por un resumen recordado.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "No se recuperó el procedimiento operativo. No se propone cambiarlo."
```

**El valor del commit es sintético.** Sustitúyelo por el commit inspeccionado en un manifiesto real. Añade la hora de recuperación durante la lectura. Un registro creado antes de inspeccionar la fuente es una lista de comprobación, no una prueba.

**Las citas ayudan a comprobar**, no generan confianza automáticamente. Enlaza cada afirmación importante con su registro y sección de respaldo. Si dos fuentes discrepan, conserva ambas en el manifiesto y explica la brecha pendiente. No elijas la hora más reciente sin comprobar el ámbito y el estado de aprobación. Esta disciplina también se aplica a la búsqueda semántica.

## Contexto compartido con RAG

**La generación aumentada por recuperación (RAG)** proporciona material recuperado al modelo mientras prepara una respuesta. Un índice semántico encuentra pasajes relevantes aunque la pregunta use otras palabras. La visión general de RAG de Microsoft describe la fundamentación, las restricciones de recuperación y los requisitos de control de acceso. Consulta la fuente oficial en las referencias.

**Usa RAG para buscar en colecciones grandes**, incluida documentación antigua, notas de reuniones y transcripciones. Etiqueta la clase y el estado de aprobación de cada documento. Una transcripción indexada desde su grabación original prueba lo que dijeron los participantes, no los requisitos aprobados. No conviertas una conversación en política mediante la indexación.

| Regla del índice | Comportamiento requerido |
|---|---|
| **Incorpora fuentes, no cachés** | Excluye resúmenes generados y copias locales sin seguimiento |
| **Conserva la procedencia** | Guarda ID de fuente, revisión, sección y estado del documento en cada fragmento |
| **Actualiza al cambiar la fuente** | Reindexa las ediciones e invalida fragmentos obsoletos |
| **Respeta los cambios de acceso** | Actualiza permisos y elimina contenido borrado o revocado |
| **Devuelve citas** | Muestra referencias junto al texto recuperado |
| **Comprueba el registro activo** | Recupera pruebas actuales antes de proponer una acción importante |

**Un fragmento recuperado funciona como un puntero.** Su texto ayuda a encontrar las pruebas. La fuente activa confirma la redacción actual, aprobación, excepciones cercanas y acceso. Si falla la recuperación activa, etiqueta la instantánea y detén la acción duradera. Esta es una regla de gobernanza, no una afirmación sobre todas las implementaciones de RAG.

**Las incrustaciones obsoletas y el contexto ausente son riesgos distintos.** Un fragmento antiguo pierde una revisión. Un fragmento actual también confunde si la excepción aparece en la siguiente sección. Conserva los encabezados y recupera las restricciones adyacentes antes de evaluar un requisito.

**Comprueba por separado la filtración de permisos.** Aplica la autorización antes de devolver fragmentos al modelo, no después de generar la respuesta. Examina el contenido sensible antes de indexarlo o enviarlo a un servicio de incrustaciones externo. Ten en cuenta el texto copiado en registros, solicitudes al modelo y trazas de recuperación. Usar un modelo local no convierte un conector remoto en local. Estas comprobaciones ayudan a decidir si RAG encaja en el piloto.

## Elige mapa, RAG o ambos

**Adapta la recuperación a la pregunta.** Un ID de requisito conocido favorece el acceso directo. Una pregunta abierta sobre material histórico disperso favorece la búsqueda. Empieza por el mapa salvo que la falta de descubrimiento ya sea un problema medido.

### Recuadro: ¿RAG o no?

```text
¿Las tareas suelen indicar un proyecto, página, issue o archivo?
  Sí -> ¿La recuperación directa basta para el piloto?
           Sí -> SOLO MAPA
           No -> HÍBRIDO: mapa para IDs conocidos, RAG para descubrir
  No -> ¿Las pruebas están dispersas en una colección grande?
           No -> SOLO MAPA, más búsqueda nativa
           Sí -> ¿El trabajo es exploratorio y de solo lectura?
                    Sí -> SOLO RAG para descubrir
                    No -> HÍBRIDO con comprobaciones de la fuente activa

Todas las opciones conservan responsables, autorización y procedencia.
La búsqueda con RAG también comprueba las fuentes antes de una acción duradera.
```

**RAG-only describe la interfaz de recuperación**, no un permiso para omitir la gobernanza. Úsalo para una colección exploratoria acotada donde aún se pueda comprobar directamente la fuente. No es adecuado para cambios por ID conocido que necesitan verificar versiones exactas.

**El modelo híbrido separa el descubrimiento de la verificación.** El mapa resuelve consultas conocidas. RAG localiza registros desconocidos. RAG responde «dónde» y la fuente responde «qué». Para el ejemplo de retención, recupera **`REQ-17`** directamente. Para averiguar qué decisiones antiguas sobre exportaciones explican el límite, busca en el registro y recupera cada decisión pertinente. Ahora aplica el proceso al repositorio.

## Información dentro del repositorio

**El conocimiento del repositorio cambia junto con la implementación.** Mantén una estructura compacta para que el agente y el revisor sepan dónde buscar.

| Archivo o directorio | Responsabilidad |
|---|---|
| **`CONTEXT.md`** | Términos del proyecto y enlaces a registros de autoridad |
| **`docs/adr/`** | Decisiones de arquitectura aceptadas para el repositorio |
| **`docs/design/`** | Descripciones aprobadas del comportamiento del sistema |
| **`docs/plans/`** | Planes de implementación propuestos con estado explícito |
| **`AGENTS.md`** | Controles de revisión, límites y funciones de responsables |
| **`README.md`** | Configuración y puntos de entrada, no requisitos duplicados |

**Aplica la regla del mismo PR:** cambia juntos el código y los documentos del repositorio afectados. Si no hace falta actualizar la base de conocimiento, exige una excepción escrita en la descripción del PR o en el lugar acordado para el trailer del commit.

```text
KB-Update: ninguna (motivo: la refactorización interna conserva el comportamiento documentado)
```

**La canalización aplica la declaración.** Una comprobación obligatoria rechaza cambios de comportamiento que no incluyan actualización documental o excepción. Un responsable humano de documentación revisa la excepción. Una comprobación por rutas detecta cambios candidatos, pero no prueba la integridad semántica. Exige la comprobación y revisión mediante protección de ramas o un control equivalente de fusión.

**Un control que no está en la canalización no es un control.** En el piloto, presenta un PR deliberadamente incompleto y confirma que la fusión sigue bloqueada. Llamar a algo «revisión documental» en un archivo de instrucciones solo da orientación.

**Usa una tarea, una rama y un worktree por trabajo.** La documentación oficial de Git describe worktrees separados, cada uno con su propio estado de checkout. Los worktrees reducen colisiones locales de edición. No impiden que dos ramas cambien el mismo archivo ni que dos agentes editen una misma página del wiki.

**Nunca hagas commit directamente en la rama predeterminada**, se llame **`main`**, **`master`** u otra cosa. Informa en el tracker las diferencias entre requisitos y código. Adjunta los registros en conflicto y pide a sus responsables que resuelvan el comportamiento esperado antes de alinear cualquiera de los dos. Aplica controles equivalentes fuera de Git.

## Información fuera del repositorio

**El wiki necesita un estándar documental.** Cada página de autoridad debe indicar propósito, estado, responsable, revisión, fecha de revisión e IDs de fuentes relacionadas. Guarda las propuestas en un área de borradores con una etiqueta clara de «no autoritativo». No mezcles texto propuesto en una página con requisitos aprobados.

**Las actualizaciones seguras siguen una secuencia fija:**

1. **Vuelve a leer** la página actual y sus restricciones cercanas.
2. **Compara** su versión con la versión base de la propuesta.
3. **Reconcilia** las ediciones intermedias y solicita nueva aprobación si cambió el texto.
4. **Escribe** la revisión aprobada con una condición de versión esperada.
5. **Verifica** la página guardada y añade la referencia al registro de cambios.

**Volver a leer no elimina las carreras.** Usa el mecanismo de actualización condicional del sistema cuando exista. Si no existe, serializa la publicación mediante un solo responsable y verifica el resultado. Detente si otra persona cambia la versión base durante la revisión.

**La regla de no borrar se aplica a los flujos de agentes.** Los agentes proponen archivar o eliminar. Las personas autorizadas aplican los procedimientos de retención y eliminación. Esta regla no permite conservar indefinidamente información sensible.

**Los hallazgos del tracker incluyen pruebas**, no solo conclusiones. Registra lo observado, el comando o método de inspección exacto, el commit inspeccionado, el comportamiento esperado, el observado y los criterios de aceptación. Elimina secretos y resultados sensibles antes de adjuntar pruebas. Marca los comandos sugeridos como no ejecutados hasta que alguien los ejecute.

```text
Hallazgo: la implementación de retención contradice el requisito aprobado
Pruebas: REQ-17 v8 y archivo config/retention.yaml inspeccionado
Comando de inspección: git show HEAD:config/retention.yaml
Commit: ID completo del commit inspeccionado registrado en el manifiesto
Criterio de aceptación: la duración aprobada coincide con código, pruebas y procedimiento
Estado: espera la revisión de responsables de producto e ingeniería
```

**El ejemplo es una plantilla de hallazgo**, no un resultado medido. Complétalo a partir de una inspección real. Vincula la actualización del wiki y las pruebas del tracker mediante el ID de propuesta.

**El registro de decisiones separa las reglas de su razonamiento.** Guarda la pregunta, opciones, recomendación, compensaciones, responsable, estado de aprobación y referencia a la regla resultante. Los agentes proponen. Las personas deciden. Las reglas aprobadas pasan a la política y a los procedimientos. Su fundamento queda en el registro.

**Extrae hechos duraderos de reuniones y chats.** Presenta una propuesta con sus fuentes y solicita aprobación. Hasta publicarla, etiqueta el acuerdo como provisional. Luego registra el comportamiento aprobado en el repositorio y el wiki.

## Conecta los dos sistemas

**La sincronización posterior a la fusión traslada los cambios de implementación.** Crea una tarea del wiki vinculada al commit fusionado, requisito aprobado y procedimiento operativo afectado. Un agente redacta la actualización. El responsable del wiki comprueba la página actual y aprueba la publicación. Mantén abierta la tarea hasta verificar la revisión guardada.

**La vigencia de la política es una auditoría aparte.** Compara cada adaptador del repositorio y cada copia de instrucciones de chat con la versión canónica aprobada. La política **`v3`** está en **`POL-01`**. Cada **`AGENTS.md`** indica **`v3`** en su primera línea. La auditoría detecta **`v2`**, etiquetas ausentes y diferencias de contenido aunque las etiquetas coincidan.

| Comprobación | Prueba de finalización |
|---|---|
| **Vigencia de la política** | Comparación de la versión canónica y el digest del adaptador |
| **Conciliación de requisitos** | Revisión del requisito comparada con código y pruebas |
| **Sincronización tras la fusión** | Commit fusionado vinculado a la revisión publicada del wiki |
| **Resolución de conflictos** | Decisión aprobada por el responsable y vinculada a ambos registros |

**Reconcilia con un calendario o durante el PR.** Una auditoría semanal sirve para el piloto. Un PR que cambie el comportamiento necesita comprobar requisitos antes de fusionarse. **El cambio a treinta días tiene varios controles:** producto aprueba el requisito, ingeniería actualiza la configuración y las pruebas, los revisores fusionan el PR y operaciones publica la actualización del procedimiento. Una fila del registro vincula los resultados. Una sincronización fallida del wiki debe seguir visible, aunque la fusión haya tenido éxito. Los traspasos compartidos mantienen este proceso entre herramientas.

## Un procedimiento para cada herramienta

**Empaqueta los pasos repetidos como skills o prompts**, con un ID de procedimiento versionado. Comparte el contrato, no un formato universal supuesto. Cada adaptador proporciona el método de carga o invocación que admite su herramienta.

| Procedimiento | Resultado requerido |
|---|---|
| **Iniciar tarea** | Responsable, alcance, versión de política, manifiesto de fuentes y reserva de escritura |
| **Revisión documental automática** | Metadatos ausentes, autoridad duplicada y referencias rotas |
| **Comprobación de conocimiento** | Diferencias entre requisitos y código con revisiones de respaldo |
| **Traspaso** | Pruebas actuales, propuestas, comprobaciones terminadas y preguntas abiertas |

**Las personas no programadoras trabajan sin Git.** Recuperan fuentes permitidas en proyectos de chat, completan la misma plantilla de propuesta y la envían al responsable en una página de borrador o una tarea del tracker. No necesitan un checkout del repositorio para solicitar la corrección de un requisito.

**Los programadores usan archivos del repositorio y controles de PR.** Enlazan la propuesta aprobada en el PR, registran los commits inspeccionados y ejecutan las comprobaciones requeridas. Ambos grupos entregan la misma estructura de pruebas.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "IDs de fuente, revisiones y commit inspeccionado adjuntos"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["Publicación de RUN-04 asignada al responsable de operaciones"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**Un traspaso también es una caché.** La siguiente persona vuelve a leer las fuentes antes de actuar y registra nuevas revisiones. No aceptes «completado» como prueba sin comprobar la aprobación o los resultados de prueba enlazados. Aplica las salvaguardas siguientes antes de escribir.

## Salvaguardas antes de cada escritura

**Examina los datos antes de sacarlos de su sistema de origen.** Comprueba la clasificación, permisos de conectores, destinos aprobados, tratamiento del proveedor del modelo y registros. Envía el mínimo de contenido pertinente. Mantén los registros restringidos fuera de proyectos de chat y servicios de incrustación no autorizados.

**El texto recuperado es prueba, no un canal de instrucciones.** Una página wiki o respuesta de herramienta que diga que ignores la política no cambia su autoridad. Evalúa por separado las instrucciones que vienen del contenido y la política operativa aprobada. Limita los conectores a lectura durante la recuperación y separa las credenciales de publicación del acceso de sesión.

**Asigna un único responsable activo a cada página o archivo.** Registra la reserva en el tracker con alcance y vencimiento. Vuelve a leer antes de escribir y usa comprobaciones de versión. Los worktrees aíslan el trabajo local; las reservas y escrituras condicionales se ocupan de los registros compartidos.

| Señal para detenerse y preguntar | Respuesta requerida |
|---|---|
| **Las fuentes discrepan y no hay responsable** | Pausa y solicita asignación de autoridad |
| **Otra tarea reservó el destino** | Negocia la propiedad antes de editar |
| **Cambió la versión base** | Reconcilia y solicita nueva aprobación |
| **Una afirmación importante no tiene pruebas** | Márcala como no verificada y solicita una fuente |
| **No está claro cómo tratar los datos** | Mantén el contenido en su sistema de origen |
| **Falla el acceso a la fuente activa** | Registra los límites de la instantánea y pausa la acción duradera |

**Los prompts no son controles de seguridad.** Prueba la denegación de permisos, ramas protegidas, rechazo de bases obsoletas y propiedad de escritura fuera del modelo. Una demostración correcta no basta si la cuenta aún puede publicar sin restricciones. Usa esas pruebas para decidir si el piloto está listo.

## Pilota antes de ampliar

**Empieza el marco como borrador.** Haz el piloto en un proyecto con una persona programadora, otra no programadora y responsables de fuentes nombrados. Formula la misma pregunta con ID conocido en dos herramientas y luego simula un conflicto de fuentes. Evalúa los manifiestos y las propuestas, no solo la fluidez del texto.

**Razonamiento esperado:** ambos participantes identifican el requisito aprobado actual y describen por separado la implementación inspeccionada. Si discrepan, comparan primero las entradas de sus manifiestos. Este es un ejercicio propuesto, no un resultado observado.

| Métrica | Definición |
|---|---|
| **Tasa de citas** | Afirmaciones importantes respaldadas por fuentes divididas por afirmaciones factuales importantes de las muestras |
| **Hallazgos semanales de deriva** | Diferencias confirmadas de autoridad o versión, agrupadas por tipo de fuente |
| **Tiempo de resolución de propuestas** | Tiempo mediano desde que una propuesta está lista para revisión hasta la decisión registrada |
| **Repetición por contexto obsoleto** | Tareas reabiertas por pruebas obsoletas o no verificadas |

**Mide una línea de base antes de fijar objetivos.** Más hallazgos de deriva la primera semana podrían indicar mejor detección, no peor documentación. Mide recurrencia y tiempo de resolución junto con el recuento bruto. No copies pruebas sensibles a exportaciones de analítica.

**Entrega un repositorio de ejemplo durante el despliegue.** Incluye un mapa sintético, adaptadores de política, manifiestos, plantillas de propuestas, excepciones documentales y comprobaciones ejecutables. Usa registros simulados del wiki y tracker, sin credenciales de producción. Demuestra publicación denegada, rechazo de una base cambiada, deriva de versión de política y un traspaso correcto.

**Un repositorio de plantillas es un entregable del despliegue**, no un recurso incluido con este artículo. Amplía el modelo operativo después de que liderazgo y responsables de fuentes revisen los resultados del piloto. Guarda excepciones y casos de fallo sin resolver en el registro de decisiones. Corrige antes los fallos previsibles siguientes.

## Soluciona problemas de contexto compartido

| Síntoma | Primera reparación |
|---|---|
| **Dos herramientas responden de forma distinta** | Compara IDs, revisiones, ámbito y estado de aprobación |
| **Las instrucciones parecen actuales, pero el comportamiento difiere** | Inspecciona adaptadores cargados, controles y anulaciones locales |
| **RAG devuelve requisitos antiguos** | Comprueba la actualización del índice y recupera la página activa |
| **Una edición del wiki borra otro cambio** | Exige escrituras condicionales o publicación serializada |
| **Las comprobaciones aceptan texto obsoleto** | Añade revisión del responsable y conciliación de requisitos |
| **Las decisiones siguen en el chat** | Asigna la entrada de propuestas y al responsable del registro |

**Corrige la ruta de las pruebas antes de reescribir el prompt.** Después repite el caso fallido del piloto y registra el resultado. Usa esta lista para convertir el proceso reparado en una práctica semanal repetible.

## Diez pasos para esta semana

1. **Elige un proyecto piloto** y a las personas y herramientas participantes.
2. **Asigna una ubicación y responsable** a cada tipo de información.
3. **Publica un mapa de proyecto** con IDs de fuentes y ámbitos de autoridad.
4. **Redacta una política compartida** y consigue la revisión del responsable.
5. **Versiona cada adaptador de instrucciones** en su primera línea y verifica que se carga.
6. **Exige un manifiesto de contexto** para respuestas factuales importantes y propuestas.
7. **Crea una vía de entrada de propuestas** con versiones base y aprobadores nombrados.
8. **Aplica controles de escritura** y la regla documental del mismo PR.
9. **Prueba deriva, conflictos y traspasos** con registros sintéticos.
10. **Revisa las métricas del piloto** y aprueba la siguiente fase del despliegue.

**Asigna un lugar a cada hecho, haz que cada herramienta lea desde allí y encamina cada cambio duradero a través de una persona.**

## Referencias y siguientes pasos

**La documentación oficial respalda los componentes técnicos**, no las reglas organizativas de este marco. Comprueba el comportamiento de las herramientas instaladas y los permisos de conectores durante el piloto.

- **Instrucciones de Codex:** [Instrucciones personalizadas con AGENTS.md](https://developers.openai.com/codex/guides/agents-md), sobre descubrimiento y verificación de instrucciones.
- **Instrucciones de Claude Code:** [Cómo Claude recuerda tu proyecto](https://code.claude.com/docs/en/memory), sobre instrucciones de proyecto y memoria.
- **Instrucciones de Cline:** [Reglas](https://docs.cline.bot/customization/cline-rules), sobre reglas de workspace y controles de activación.
- **Diseño de recuperación:** [Generación aumentada por recuperación en Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), sobre fundamentación, límites de recuperación y seguridad.
- **Seguridad de conectores:** [Buenas prácticas de seguridad MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), sobre autorización y riesgos de conectores.
- **Aislamiento de worktrees:** [Documentación de Git worktree](https://git-scm.com/docs/git-worktree), sobre árboles de trabajo separados y el estado compartido del repositorio.

**Para planificar inferencia local**, lee la [Guía de contexto de GPU para IA local](/articles/local-ai-model-gpu-context-guide/). La capacidad de hardware y la gobernanza de fuentes compartidas resuelven problemas distintos. Una ventana de contexto mayor no corrige una autoridad contradictoria.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Lee la Guía de contexto de GPU para IA local
{{< /centerbutton >}}
