---
title: "Configuración de IA en Confluence y Jira: permisos y autoridad"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Configura páginas de referencia oficiales en Confluence y permisos de Jira administrados por la empresa para colaborar entre equipos con revisión."
genre: ["Inteligencia artificial", "Colaboración en equipo", "Ingeniería de software"]
tags: ["curso de colaboración con IA", "Confluence Cloud", "Jira Cloud", "páginas de referencia oficiales", "esquema de permisos de Jira", "transición del flujo de trabajo", "pruebas de acceso"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustración de profesionales que revisan el trabajo compartido de un proyecto en un entorno de ciberseguridad"
coverCaption: ""
---

[Volver al curso de colaboración con IA](/ai-collaboration-course-start/)

**El administrador configura la autoridad del lugar de trabajo antes de conectar las herramientas de chat.** Los responsables de producto y operaciones publican requisitos y manuales en Confluence Cloud. Jira Cloud coordina la entrega. GitHub controla la implementación. Crea entornos de pruebas dedicados después de establecer la base, porque un permiso incorrecto expone información con independencia del comportamiento del modelo.

## Ideas clave

- **Confluence** conserva la redacción aprobada de los requisitos.
- **Jira** controla el estado de entrega, no la política de retención.
- **GitHub** controla la configuración y las políticas compartidas.
- **Las pruebas de permisos** requieren planes adecuados y usuarios separados.

## Antes de empezar

**Requisitos previos:** los [fundamentos](/articles/ai-collaboration-pilot-foundation/), el repositorio del laboratorio, la administración de espacios de Confluence y de Jira, y usuarios separados con roles de colaborador, responsable y publicador. **Tiempo estimado:** de 90 a 120 minutos. **Dificultad:** administración avanzada.

**Requisito del plan:** Confluence Free no admite restricciones de contenido. Jira Free no incluye esquemas de permisos configurables, roles de espacio ni esquemas de seguridad de elementos de trabajo. Para esta ruta, usa entornos de pruebas adecuados con Standard o un plan superior. Antes de probar, verifica el plan y los privilegios reales en las referencias.

**Nota de navegación:** la documentación actual de Jira usa “space” y “work item”. Algunos tenants conservan “project” y “issue”. Elige una configuración administrada por la empresa. Este procedimiento no cubre el comportamiento de permisos en una configuración administrada por el equipo. No se necesitan Rovo, aplicaciones de Marketplace, aprobaciones de Jira Service Management ni un conector de chat de pago.

**Resultado:** prepara una matriz de permisos, páginas de referencia oficiales con nombre, un flujo de trabajo de Jira exclusivo del laboratorio y pruebas de denegación con usuarios separados. Anota el plan del tenant y las suposiciones sobre roles junto a los resultados.

**Comprobaciones antes de crear registros:**

| Comprobación | Si está disponible | Si falta |
|---|---|---|
| Restricciones de páginas y administración de espacios de Confluence | Crea páginas aprobadas y excluidas por separado | Marca como Bloqueadas las pruebas de edición y de denegación de lectura |
| Esquema de permisos y editor de flujos de trabajo de Jira administrado por la empresa | Copia un esquema y flujo exclusivos del laboratorio | Marca como Bloqueadas las pruebas de transición |
| Usuarios separados para colaborador, responsable, publicador y usuario excluido | Ejecuta pruebas positivas y negativas para cada rol | Marca como Bloqueados los roles no probados |
| Responsable del repositorio y rama protegida | Enlaza la ruta de implementación revisada | Completa primero la ruta GitHub-first antes de una publicación mixta |

Desde octubre de 2026, usa el botón **Share** o el control de restricciones para administrar el acceso a una página, el área de permisos de **Space settings** en Confluence para concesiones más amplias y **Settings > Work items > Permission schemes** en Jira para el esquema del laboratorio. El editor de flujos de trabajo de Jira administrado por la empresa controla las transiciones. Las etiquetas de la interfaz y las funciones del plan varían según el tenant. Antes de seguir estos pasos, registra la ruta y el plan reales en tus pruebas. Consulta los [permisos de página de Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) y los [esquemas de permisos de Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Crear páginas de referencia oficiales

1. **Crea un espacio de Confluence** llamado **`Export Service Lab`**. Desactiva el acceso anónimo y el uso compartido público mediante los controles disponibles del sitio o del espacio.
2. **Crea páginas publicadas**, no documentos activos, llamadas **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** y **`Decision Register`**.
3. Como responsable de producto, **publica el requisito inicial** que aparece abajo. Registra el ID y la versión reales de la página en el mapa del repositorio.
4. Como responsable de operaciones, **publica RUN-04** con siete días de retención y la declaración de que en este laboratorio no se ejecuta ninguna tarea de eliminación.
5. En cada página de referencia oficial, **abre Share**. Configura el acceso general como solo lectura para los miembros aptos del espacio y concede permisos de edición específicos a los responsables y publicadores designados. Guarda y verifica con el usuario colaborador.

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**Aplica restricciones a cada página de referencia oficial.** No des por hecho que una restricción de edición en una página principal protege sus páginas secundarias. La herencia de lectura y edición funciona de forma distinta, y los permisos del espacio siguen aplicándose. Un enlace no concede acceso por sí solo. Revisa todas las pertenencias si un usuario que supuestamente solo puede leer todavía puede editar.

**Usa estos textos iniciales para las otras dos páginas.** Sustituye los campos de revisión provisionales por pruebas reales del entorno de pruebas antes de aprobar un registro.

```text
Source ID: RUN-04
Owner role: operations-owner
Status: Approved baseline
Scope: synthetic export files only
Configured retention: 7 days
Procedure: compare REQ-17 with config.json before a reviewed change
Runtime limit: this lab has no deletion job and produces no deletion evidence
Recovery: restore the prior approved configuration through review
Recovery limit: restoring configuration does not restore deleted files
Review evidence: add actual reviewer, page version, and decision reference
```

```text
Page: Decision Register
Entry ID: DEC-12
Decision: use seven days as the synthetic baseline
Scope: export-service-lab only
Requirement: REQ-17 page version, record after publication
Runbook: RUN-04 page version, record after publication
Policy: POL-01 protected GitHub revision, record after review
Product review: pending until the named owner records a decision
Operations review: pending until the named owner records a decision
Status: draft example, replace with observed review evidence
```

## Actualizar el mapa

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Añade al mapa las ubicaciones privadas reales del entorno de pruebas y los ID de las páginas.** La plantilla indica cuáles son las fuentes oficiales sin fingir que contiene direcciones activas. Elimina del README las frases que asignan autoridad sobre los requisitos de la ruta mixta al archivo JSON copiado.

**Mantén POL-01 en GitHub** para ambas rutas. Confluence enlaza a su revisión aprobada. Cambiar la autoridad de una política durante una tarea requiere otra transición de autoridad revisada.

## Configurar permisos de Jira

1. **Crea un espacio de laboratorio administrado por la empresa** y copia un esquema de permisos a un esquema dedicado al laboratorio. No edites un esquema de producción compartido.
2. **Abre Settings, Work items, Permission Schemes**, selecciona el esquema del laboratorio y actualiza las concesiones.
3. **Concede a los colaboradores permisos para consultar, crear y comentar.** Restringe los privilegios administrativos. Revisa expresamente los permisos de edición y **Transition work items**.
4. **Asocia el esquema** al espacio del laboratorio y verifica que ningún espacio de producción lo comparta.
5. **Crea PROP-042** como elemento de trabajo. Registra su clave generada en el mapa y conserva PROP-042 como ID lógico de propuesta en su descripción.

**Pega este borrador en PROP-042.** El elemento de Jira registra la entrega. Su texto no reemplaza la redacción aprobada en Confluence.

```text
Proposal ID: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 page version to record
Proposed value: 30 days for synthetic export files
Exclusions: production data, backups, legal holds
Affected records: REQ-17, RUN-04, config.json, proposal.json
Fixed proposal attachment: pending
Product-owner review: pending
Operations-owner review: pending
Publication ledger: pending
Stop on changed source version, missing review, or denied access
```

| Rol | Confluence | Jira | GitHub |
|---|---|---|---|
| **Colaborador** | Lee páginas aprobadas | Crea borradores y comenta | Rama de propuesta o Issue |
| **Responsable de producto** | Revisa el requisito | Registra la revisión del requisito | Revisa las pruebas de la PR |
| **Responsable de operaciones** | Revisa el manual | Registra la revisión operativa | Revisa el impacto operativo |
| **Publicador** | Edita páginas aprobadas | Registra el estado de publicación | Sin autoridad automática para fusionar |
| **Mantenedor** | Lee el requisito | Registra la implementación | Revisa y fusiona la PR protegida |

**Los permisos de varios grupos se acumulan.** Elimina en el laboratorio las concesiones amplias no previstas en vez de suponer que una concesión limitada las reemplaza. No añadas identidades de conectores a grupos administrativos.

## Configurar estados de entrega

**Copia un flujo de trabajo administrado por la empresa** en otro exclusivo del laboratorio. Añade los estados Borrador, Revisión, Aprobado, Publicación, Hecho y Bloqueado. Añade transiciones de envío, aprobación, publicación, finalización, bloqueo y regreso a revisión. Asígnalo solo al tipo de trabajo del laboratorio.

1. En el editor del flujo de trabajo, **selecciona la transición a Aprobado**.
2. **Añade una condición o restricción** que limite la acción al rol o grupo designado de responsables/publicadores. Usa los controles de condiciones documentados y publica el borrador del flujo como administrador.
3. **Comprueba manualmente las revisiones de ambos responsables** antes de la transición. Cada revisión identifica la propuesta congelada y las versiones de las fuentes.
4. **Restringe Hecho** al rol responsable de la entrega. Elimina transiciones alternativas o globales que eviten este límite.

**Una transición restringida no equivale a una aprobación de dos personas.** Controla quién ejecuta la transición. En este piloto, la comprobación de pruebas de los dos roles sigue siendo un procedimiento. Registra explícitamente este límite.

**Ejemplo de registro de transición:** para **Revisión a Aprobado**, permite que solo el grupo designado de responsables/publicadores active la transición. Antes de activarla, quien la ejecuta abre el adjunto fijo de PROP-042 y comprueba una decisión del responsable de producto y otra del responsable de operaciones para la misma revisión de la propuesta. Si falta una decisión o corresponde a una revisión anterior, deja el elemento en Revisión y registra la brecha. La restricción del flujo controla quién ejecuta la transición. La comprobación de pruebas es un paso humano independiente.

## Verificar la denegación

**Como colaborador**, lee REQ-17, intenta editarlo, crea el borrador de Jira e intenta la transición a Aprobado. Los resultados esperados son requisito legible, edición denegada, propuesta creada correctamente y aprobación denegada. Compara las versiones de la fuente antes y después de la denegación.

**Como usuario excluido**, abre una página sintética con restricciones separadas. No debe haber acceso al contenido. Prueba las páginas secundarias de forma independiente. No pegues texto protegido en el chat del usuario excluido como alternativa.

## Adaptar el mapa del repositorio

**Mantén estables los ID de origen cuando cambie su ubicación.** REQ-17 sigue representando la intención aprobada de retención, pero en la ruta mixta su ubicación es una página de Confluence. Una copia en el repositorio ayuda con las comprobaciones y las revisiones. No reemplaza la fuente oficial de la página.

| Registro | Ubicación autorizada | Tratamiento en el repositorio |
|---|---|---|
| **REQ-17** | Página de requisitos de Confluence indicada en el mapa | Copia capturada con pruebas de revisión de la página |
| **RUN-04** | Página del manual de Confluence indicada en el mapa | Extracto operativo capturado para mantener la coherencia |
| **POL-01** | Política protegida en GitHub | Las instrucciones compartidas de los agentes hacen referencia a ella |
| **Configuración** | Registro protegido en GitHub | Diferencia de implementación propuesta |
| **Entrega** | Elemento de trabajo de Jira | Enlace de correlación, no copia de la política |

**Añade la procedencia a las copias.** Registra el ID de origen, referencia y versión de la página, hora de captura y rol que la capturó en el paquete privado de la propuesta. No incluyas ID nativos de páginas en entregas públicas del curso. Si el publicador encuentra otra versión vigente, resuelve la diferencia antes de usar la copia.

**No cambies el nombre de la autoridad para adaptarlo a la herramienta.** La descripción editable de Jira facilita la conversación, pero sigue siendo un registro de entrega. Una frase de treinta días en Jira no invalida un requisito de siete días en Confluence.

## Diseñar pruebas de acceso

**Separa la lectura, la preparación de borradores y la publicación.** Un colaborador necesita acceso suficiente para entender el requisito sintético y presentar una propuesta. No necesita permisos de edición en la página de referencia oficial ni permiso para aprobar su propia propuesta.

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**Usa un registro separado para la lectura denegada.** Que el colaborador pueda leer el requisito prueba la separación entre publicación y edición. Que el usuario excluido no pueda abrir una página prueba la confidencialidad. Combinar ambos casos en una fila oculta qué límite se probó.

**Comprueba también el acceso permitido.** Los responsables y publicadores deben poder utilizar la ruta asignada. Si todos reciben una denegación, el entorno de pruebas es restrictivo pero inutilizable. Conserva una edición autorizada correcta en una página de prueba desechable, sin cambiar el requisito aprobado durante el diagnóstico de permisos.

## Ensayar la revisión en Jira

**Trata los nombres de estado como el diseño de este piloto.** Borrador contiene una solicitud. Revisión contiene un paquete congelado. Aprobado indica que los responsables completaron la revisión. Publicación indica una entrega incompleta. Hecho requiere una lectura de comprobación. Bloqueado indica que falta evidencia o acceso, o que hay un conflicto sin resolver.

| Transición | Paquete requerido | Comprobación responsable |
|---|---|---|
| **Borrador a Revisión** | Propuesta fija y versiones de las fuentes | El colaborador confirma que está completa |
| **Revisión a Aprobado** | Decisiones de producto y operaciones | La persona autorizada comprueba ambos roles |
| **Aprobado a Publicación** | Comparación con las fuentes actuales | El publicador confirma que las bases no cambiaron |
| **Publicación a Hecho** | Registro completado por sistema | El responsable de entrega comprueba la lectura |
| **Cualquier paso admitido a Bloqueado** | Fallo y acción pendiente | Responsable de recuperación asignado |

**Ensaya con un paquete sintético incompleto.** Envía solo una revisión de producto y pide a la persona autorizada que evalúe la transición. Lo esperado es dejar el trabajo en Revisión y solicitar la revisión de operaciones. Así se prueba el paso de revisión del procedimiento por separado de la denegación de la plataforma al colaborador.

**Prueba deliberadamente las rutas alternativas.** En la vista del flujo de trabajo del entorno de pruebas, inspecciona todas las rutas a Aprobado y Hecho. Una transición restringida y nombrada no basta si otra ruta disponible evita el mismo límite de revisión. Registra las rutas inspeccionadas y el actor usado, en vez de afirmar una cobertura completa tras un solo clic.

## Diagnosticar accesos inesperados

**Empieza por la identidad efectiva.** Confirma que la sesión del navegador pertenece al rol de prueba previsto. Después, revisa pertenencias a grupos, permisos del espacio, acceso a páginas y asociación del flujo con las herramientas de administración del producto. No cambies varios controles a la vez, porque la denegación perdería valor diagnóstico.

1. **Confirma la identidad:** usa sesiones separadas para colaborador, publicador y usuario excluido.
2. **Localiza la concesión:** identifica la pertenencia o ajuste que permite la acción intentada.
3. **Ajusta el control del laboratorio:** conserva el acceso legítimo de los responsables.
4. **Repite el mismo intento:** registra la versión de origen sin cambios después de la denegación.
5. **Repite el caso positivo:** confirma que la publicación autorizada sigue funcionando.

**Lista final de evidencias:** registra el árbol de páginas de Confluence y sus ID en el mapa, la asociación del esquema Jira del laboratorio, la asociación del flujo de trabajo, la pertenencia a grupos de cada rol de prueba, una lectura permitida del requisito, una edición denegada con la versión sin cambios, la creación permitida de un borrador, una transición a Aprobado denegada con el estado sin cambios, la lectura denegada al usuario excluido y la persona responsable de la limpieza. En cada fila, conserva el rol del actor, la versión o el estado inicial y final, el resultado nativo y el revisor independiente. Registra la ruta de navegación observada en el tenant, ya que las etiquetas y controles disponibles varían según el plan.

**Comprobación final:** entrega las páginas de referencia oficiales del mapa, el flujo exclusivo del laboratorio, la matriz prevista de roles y los registros de permisos observados. Si el plan no ofrece un control necesario, deja la fila correspondiente como Bloqueada. La lección sobre publicación supone que estas pruebas se aprobaron, no solo que existen capturas de los ajustes.

## Solución de problemas y reversión

**El colaborador aún puede editar:** revisa el acceso a la página, los permisos del espacio y las pertenencias. **La transición aún se completa:** revisa la asociación del flujo y las rutas de omisión. **Faltan ajustes:** verifica el tipo administrado por la empresa, la edición y los permisos de administrador.

**Reversión:** elimina los permisos de conectores y archiva borradores. Desvincula esquemas y flujos exclusivos del laboratorio después de guardar las pruebas. Restaura la redacción aprobada de la página mediante el historial revisado o una corrección compensatoria. No elimines las pruebas de auditoría.

## Ejercicio y autoevaluación

**Jira indica treinta días, mientras que REQ-17 indica siete.** Identifica la entrada de implementación y quién debe resolver la discrepancia.

**Razonamiento esperado:** Confluence define la intención. Jira contiene un error de propuesta o de entrega. Detén la publicación y pide al responsable de producto que concilie los valores, en lugar de elegir la marca de tiempo más reciente.

## Referencias principales

- **Restricciones y plan:** [permisos de Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controles para compartir:** [acceso a contenido específico](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Administración de esquemas:** [esquemas de permisos de Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Condiciones de transición:** [flujos de trabajo avanzados](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Próximos pasos

**Continúa con [Publicación entre sistemas](/articles/ai-collaboration-confluence-jira-publication/)** cuando las pruebas de acceso terminen correctamente.
