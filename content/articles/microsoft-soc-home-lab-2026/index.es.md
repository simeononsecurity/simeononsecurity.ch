---
title: "Laboratorio SOC de Microsoft en casa: adquiere experiencia en ciberseguridad en 2026"
date: 2026-09-11
lastmod: 2026-11-27
toc: true
draft: false
description: "Crea un laboratorio SOC de Microsoft con Sentinel, Defender, Intune y Entra. Investiga incidentes, valida políticas de claves de acceso y documenta evidencias para tu portfolio."
genre: ["Ciberseguridad", "Seguridad en la nube", "Desarrollo profesional"]
tags: ["laboratorio SOC doméstico", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "laboratorio Azure doméstico", "experiencia en ciberseguridad", "analista SOC", "centro de operaciones de seguridad", "respuesta a incidentes", "KQL", "Log Analytics", "Conditional Access", "MFA resistente al phishing", "claves de acceso", "seguridad de identidad", "portfolio de ciberseguridad", "gestión de costos de nube", "seguridad de endpoints"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Un portátil muestra cronologías de incidentes de seguridad en un escritorio doméstico, bajo una nube con servidores y endpoints."
coverCaption: ""
---

Un **laboratorio SOC doméstico** ofrece un espacio para investigar alertas, explicar evidencias y probar cambios defensivos. Construye un entorno pequeño de Microsoft, recopila su telemetría y documenta cada investigación. El resultado útil es una investigación repetible respaldada por evidencias.

Esta guía desarrolla el enfoque de laboratorio descrito en el vídeo de carrera profesional de ciberseguridad de Mad Hat y en el runbook Cyber Range proporcionado. Usa documentación de Microsoft para los requisitos de producto y separa configuración, detección y validación en tareas medibles.

## Puntos clave

- **Empieza con poco:** un cliente Windows administrado y una identidad de prueba sirven para los primeros ejercicios.
- **Verifica la telemetría:** ver un dispositivo o un portal conectado no demuestra que lleguen los registros.
- **Completa la investigación:** registra el desencadenante, las evidencias, la respuesta y la repetición de la prueba.
- **Controla el gasto:** sigue por separado las licencias, la retención de datos, la red y el cómputo.
- **Describe la experiencia con precisión:** presenta el entorno como proyecto de laboratorio en tu currículum.

## Antes de empezar

**Requisitos previos:** conocimientos básicos de administración de Windows y redes, y familiaridad con máquinas virtuales. Usa un tenant dedicado de Microsoft Entra y una suscripción de Azure reservada para el laboratorio. Mantén fuera del ejercicio las identidades de producción, los archivos personales y los sistemas del empleador.

**Esfuerzo estimado:** reserva un fin de semana para la configuración inicial y después programa sesiones de investigación breves. Es una estimación de planificación. La aprobación de la prueba, las cuotas disponibles y el aprovisionamiento de servicios afectan al tiempo real. **Dificultad:** intermedia.

Prepara una cuenta administrativa separada y un usuario de prueba sin privilegios. Antes de probar políticas de acceso, establece y verifica el acceso de emergencia. Asigna privilegios para cada tarea de configuración y usa una cuenta con menos privilegios para la investigación diaria.

| Componente | Uso en el laboratorio |
|---|---|
| **Sentinel** | Gestión de información y eventos de seguridad (SIEM) para fuentes de registros conectadas |
| **Defender XDR** | Correlación e investigación en servicios de seguridad de Microsoft con licencia |
| **Defender for Endpoint** (protección de puntos de conexión) | Detección y respuesta en endpoints incorporados |
| **Intune** | Inscripción de dispositivos y administración de políticas de seguridad de endpoints |
| **Entra ID** | Identidades, registros de inicio de sesión y evaluación de políticas de acceso |
| **Defender for Servers** (protección de servidores) | Protección de servidores mediante Defender for Cloud |

## Comprueba primero las licencias

**Microsoft 365 E5** es una opción para un laboratorio amplio, pero el acceso depende de los planes de servicio y licencias asignados a cada usuario participante. Office 365 E5 y Microsoft 365 E5 son paquetes distintos. La licencia de un administrador no demuestra que todos los usuarios de prueba o cargas de trabajo estén cubiertos. Consulta los [requisitos previos de Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites) antes de elegir una suscripción.

**Sentinel en el portal de Defender** funciona sin E5 ni Defender XDR. Añadir XDR trae sus propios requisitos de licencias y configuración. Una vista de incidentes vacía no demuestra que falte una licencia E5. La [documentación de incorporación de Sentinel](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) explica ambas configuraciones.

**La protección de servidores** tiene una vía de licencias independiente. Defender for Servers se integra con Defender for Endpoint para las cargas de servidor compatibles. Los sistemas Windows cliente necesitan cobertura de cliente adecuada. No supongas que cada VM de Azure tiene una licencia de servidor automática. Consulta la documentación de Microsoft sobre la [integración de Defender for Endpoint](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Planifica la prueba:** comprueba en tu cuenta la elegibilidad, caducidad, renovación y los servicios incluidos. No calcules el presupuesto según una duración prometida de prueba o una cuota mensual fija mencionada en un vídeo.

## Define un presupuesto

**Los presupuestos de Azure** envían notificaciones. No detienen el consumo al alcanzar un umbral. Los informes de costos también se retrasan. Crea alertas cuanto antes y revisa el gasto después de cada sesión según la [guía de presupuestos de Microsoft](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Categoría de costo | Pregunta de planificación |
|---|---|
| **Licencias de usuario** | ¿Qué usuarios necesitan cada plan de servicio y cuándo caducan las pruebas? |
| **Cómputo** | ¿Cuántas horas de VM requiere cada ejercicio? |
| **Almacenamiento** | ¿Qué discos e instantáneas quedan después del apagado? |
| **Recopilación de registros** | ¿Qué tablas requieren ingesta y cuánto tiempo deben conservarse los datos? |
| **Red** | ¿El diseño incluye Bastion de pago, IP públicas o servicios salientes? |
| **Protección de servidores** | ¿Qué cargas tienen habilitado un plan Defender de pago? |

**Decisión de diseño:** empieza con un cliente. Añade un servidor cuando un ejercicio necesite telemetría del servidor. Cuatro clientes y varios servidores aumentan la administración y el costo antes de aportar práctica de investigación útil.

## Construye la red

**Diseño sugerido:** coloca los recursos de Azure en un grupo con un nombre claro, por ejemplo **`rg-soc-lab`**. Usa subredes separadas para clientes y servidores, reglas explícitas de grupos de seguridad de red y acceso de administración privado. Separar subredes por sí solo no bloquea el tráfico entre cargas.

Para un despliegue dedicado de **Azure Bastion**, cumple los requisitos de SKU, incluido el nombre reservado **`AzureBastionSubnet`** y una subred **`/26`** o mayor en los despliegues actuales. Developer SKU usa otro modelo. Revisa los [ajustes de configuración de Bastion](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) antes de elegir.

Mantén RDP y SSH cerrados a Internet público. Restringe el tráfico de administración a la ruta elegida. Permite las conexiones salientes que requieren la inscripción y la telemetría de seguridad.

**Validación:** establece acceso privado de administración y comprueba las reglas de red efectivas antes de instalar cargas. Si luego añades una aplicación vulnerable de forma intencional, mantenla dentro de la red de ejercicios y limita el acceso a las máquinas de prueba.

## Conecta Sentinel y los registros

**Configuración del portal:** crea un espacio de trabajo de Log Analytics y habilita Sentinel allí. Si no aparece en el portal de Defender, abre **System > Settings > Microsoft Sentinel > Connect a workspace** (Sistema > Configuración > Microsoft Sentinel > Conectar un espacio de trabajo). Verifica el tenant y los roles de Azure y Entra requeridos en los [requisitos previos de incorporación](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**La recopilación de registros es un paso separado.** En Entra, configura los ajustes de diagnóstico para enviar las categorías de actividad necesarias al mismo espacio de trabajo. Empieza con inicios de sesión interactivos y eventos de auditoría. La [guía de integración de registros de Entra](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) explica los permisos y el destino.

El flujo actual de Sentinel también admite la conexión mediante el portal de Microsoft Defender. Antes de investigar una tabla vacía, confirma que el espacio de trabajo principal sea el correcto, que el tenant coincida con las identidades de prueba y que la cuenta tenga los roles necesarios. Ver el portal no demuestra la ingesta. [Incorporación de Sentinel en el portal de Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Ejecuta este ejemplo de **Kusto Query Language (KQL)** en la vista Logs del espacio de trabajo después de generar un nuevo inicio de sesión de prueba. Sustituye el UPN de ejemplo por el usuario del laboratorio. Las columnas corresponden al [esquema de la tabla SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Resultado esperado:** una fila que coincida con la cuenta y la hora de inicio de sesión de prueba. Si no aparecen filas, comprueba el periodo, la identidad, los ajustes de recopilación, el destino y el retraso de ingesta. Si falta la tabla, revisa primero la recopilación o el espacio de trabajo y después la detección.

## Incorpora el primer endpoint

**La inscripción de Intune y la incorporación EDR** son puntos de control distintos. Conecta Intune y Defender for Endpoint, inscribe un cliente Windows compatible y asigna una política de incorporación EDR a su grupo de laboratorio. El registro de Entra por sí solo no confirma ninguno de esos pasos.

En Intune, revisa **Endpoint security > Defender for Endpoint** (Seguridad de puntos de conexión > Defender for Endpoint (protección de puntos de conexión)). Si la conexión no está disponible, habilita la conexión de Intune en las funciones avanzadas de endpoints de Defender. Sigue los pasos de la plataforma en la [guía de integración de Intune y Defender](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Punto de control | Evidencia que debes guardar |
|---|---|
| **Inscripción** | El cliente aparece en Intune con una sincronización reciente |
| **Asignación de política** | La política de incorporación se aplica al grupo de dispositivos previsto |
| **Informes del sensor** | Defender muestra el estado incorporado y telemetría reciente |
| **Prueba de detección** | Una prueba documentada genera la señal de seguridad esperada |

**Para los servidores**, habilita el plan elegido de Defender for Servers y su integración con endpoints, y verifica el despliegue e informes del sensor. Defender for Cloud también detecta máquinas antes de completar la incorporación. La presencia en el inventario no basta, como explica la guía de [detección e incorporación de recursos](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Investiga una alerta de prueba

**Empieza con la prueba de detección EDR documentada por Microsoft** en el endpoint del laboratorio. Sigue las [instrucciones actuales de la prueba](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), incluidos los requisitos de plataforma y la solución de problemas. Anota la hora de ejecución antes de abrir la cola de alertas.

Trata la alerta resultante como un ejercicio de investigación. El título del producto es un punto de partida. Tu tarea es establecer qué ocurrió y justificar la decisión con evidencias.

1. **Triage:** identifica el origen de la alerta, dispositivo, cuenta y hora del evento.
2. **Inspección:** revisa el árbol de procesos, la línea de comandos, detalles del archivo y la actividad de red disponible.
3. **Alcance:** busca actividad relacionada en la identidad de prueba y otros dispositivos del laboratorio.
4. **Evaluación:** explica si las evidencias corresponden al ejercicio previsto o a otro evento.
5. **Respuesta:** documenta la respuesta elegida, su impacto y los pasos de recuperación. Aplica la contención admitida solo si el ejercicio lo requiere.
6. **Repetición de la prueba:** después de cambiar un control, repite la prueba relevante y compara las evidencias.

**No inventes resultados ausentes.** Si la alerta no llega, conserva el registro de ejecución y revisa la recopilación. Si un control bloquea la prueba antes del evento esperado, documenta el resultado preventivo.

## Prueba los controles de identidad

**El phishing de tipo adversary-in-the-middle (AiTM)** coloca un intermediario controlado por un atacante en el flujo de inicio de sesión. El runbook suministrado usa este escenario para motivar una autenticación más fuerte. Para el primer ejercicio de identidad, prueba el comportamiento de las políticas directamente con tu propia cuenta sin privilegios.

Empieza registrando un inicio de sesión legítimo y sus detalles de autenticación. Revisa la [referencia de detección de riesgos de Entra](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) de Microsoft antes de interpretar señales de riesgo. Los requisitos y el procesamiento varían según la señal. Una IP nueva o un inicio de sesión fallido no garantizan una alerta AiTM.

**Las passkeys (FIDO2)** usan credenciales vinculadas al servicio legítimo en vez de códigos reutilizables introducidos en una página de inicio de sesión retransmitida. Habilita un perfil de passkey adecuado para el grupo piloto y registra el método antes de aplicar una política. Consulta la [guía de configuración de passkeys](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) para ver autenticadores admitidos y restricciones.

**Ejercicio de Conditional Access (acceso condicional):** crea una política dirigida solo al grupo piloto del laboratorio, excluye las cuentas de acceso de emergencia y selecciona **Require authentication strength > Phishing-resistant MFA strength** (nivel de autenticación y MFA resistente al phishing). Empieza en **Report-only (solo informe)**, revisa el impacto y luego habilita la política. Adapta el [ejemplo de política de administrador de Microsoft](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) a un grupo pequeño de prueba.

| Prueba | Evidencia que debes recopilar |
|---|---|
| **Política en modo Report-only (solo informe)** | Registro de inicio de sesión que muestra cómo se evalúa la política propuesta |
| **Política aplicada, método más débil** | Una autenticación nueva requiere un método más fuerte antes de conceder acceso |
| **Política aplicada, passkey registrada** | Inicio de sesión correcto que satisface el nivel requerido |

Usa una autenticación nueva para cada comparación y revisa los detalles de la política. Las sesiones existentes complican la comparación. **Alcance de la prueba:** este ejercicio valida el requisito de autenticación. No demuestra protección universal contra la intrusión del endpoint o el robo de una sesión existente.

## Documenta evidencias para tu portfolio

**Una entrada útil de portfolio** explica una decisión para que otro analista pueda evaluarla. Incluye una breve descripción de arquitectura, requisitos previos de recopilación, cronología del evento y razonamiento de la respuesta.

```text
Ejercicio:
Fecha y ventana horaria UTC:
Alcance del laboratorio y requisitos previos:
Desencadenante y señal esperada:
Alerta observada o prevención:
Evidencias y consultas:
Identidades y dispositivos afectados:
Conclusión y razonamiento:
Respuesta y recuperación:
Cambio de control y nueva prueba:
Limitaciones y seguimiento:
```

Sustituye cada campo por observaciones propias. **Sanitiza las exportaciones:** elimina credenciales, datos de sesión, información personal e identificadores innecesarios antes de publicar capturas de pantalla o resultados de consultas.

**Ejemplo para el currículum:** «Construí un laboratorio de seguridad de Microsoft, conecté registros de identidad a Sentinel, investigué alertas de pruebas de endpoints y documenté la validación de Conditional Access». Usa esta frase solo después de completar esas tareas. Inclúyela en proyectos o formación práctica con fechas y alcance reales.

Un laboratorio demuestra práctica independiente. **El trabajo en un SOC de producción** también implica impacto empresarial, escalación, compromisos de servicio y coordinación con otros equipos. Explica qué partes practicaste y cuáles aún no forman parte de tu experiencia.

## Solución de problemas

| Síntoma | Primera comprobación |
|---|---|
| **Espacio de trabajo ausente de Defender** | Mismo tenant, Sentinel habilitado y roles requeridos |
| **SigninLogs ausente o vacío** | Categorías de diagnóstico, destino, eventos nuevos y periodo |
| **Cliente ausente de Intune** | Requisitos previos y estado de inscripción |
| **Dispositivo visible sin telemetría** | Estado real de incorporación, estado del sensor y conectividad saliente |
| **Política de incorporación no aplicada** | Alcance de asignación, plataforma y sincronización reciente |
| **Sin alerta de riesgo de identidad** | Requisitos de la señal y actividad registrada, sin suponer detección determinista |
| **Acceso permitido de forma inesperada** | Estado Report-only (solo informe), exclusiones, alcance del recurso y sesión existente |
| **Cargos después del apagado** | Estado de asignación y recursos cobrados aparte del cómputo |

**Orden para solucionar problemas:** demuestra primero que ocurrió el evento, después que funcionó la recopilación y por último examina la lógica de detección. Anota cada fallo y corrección en las notas del proyecto.

## Pausa o elimina el laboratorio

**La desasignación** libera la asignación de cómputo de una VM. Apagar solo el sistema operativo invitado no garantiza la desasignación. Comprueba el estado de energía en Azure y consulta la documentación de Microsoft sobre [estados y facturación de VM](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Los recursos retenidos** también requieren revisión. Discos, instantáneas, servicios de red, retención de registros y suscripciones de usuario tienen ciclos de vida separados. Programa un recordatorio antes de que caduque cada prueba y revisa el siguiente informe de uso después de limpiar.

Antes de eliminar el grupo de recursos del laboratorio, exporta las evidencias que quieras conservar e inspecciónalas. **Eliminar un grupo de recursos es destructivo** para los recursos que contiene. Los usuarios del tenant, políticas de Intune y Conditional Access, suscripciones y ajustes de seguridad a nivel de suscripción pueden requerir una limpieza aparte.

## Próximos pasos

**Completa una investigación documentada** antes de añadir otra carga. Después añade un servidor, un ejercicio de identidad o una regla de detección con una condición de prueba clara. Anota qué enseña el nuevo componente y cuánto cuesta.

Usa la [guía de laboratorio de TI](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) para practicar infraestructura y la [guía de currículum de TI](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) para presentar el trabajo. Mantén el próximo proyecto lo bastante pequeño como para explicar la configuración, las evidencias y la limpieza.
