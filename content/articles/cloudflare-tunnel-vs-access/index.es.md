---
title: "Cloudflare Tunnel y Access: ¿necesitas ambos?"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Entiende la diferencia entre Cloudflare Tunnel y Access, elige protección para un panel doméstico y evita publicar una aplicación privada sin autenticación."
genre: ["Seguridad de redes", "Alojamiento propio", "Seguridad en la nube"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel y Access", "Cloudflare Zero Trust", "cloudflared", "aplicaciones autoalojadas", "seguridad de homelab", "acceso remoto", "proveedor de identidad", "políticas de acceso", "autenticación de aplicaciones", "nombre de host público", "protección del origen", "túnel saliente", "tokens de servicio", "Service Auth", "MFA", "panel privado", "proxy inverso", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Un servidor doméstico se conecta mediante un paso transparente a una puerta de enlace en la nube con un punto de verificación de identidad independiente."
coverCaption: ""
---

**Cloudflare Tunnel** conecta tu aplicación con Cloudflare. **Cloudflare Access** controla quién puede llegar a ella. Para un panel doméstico privado expuesto mediante un nombre de host público, usa ambos. Un túnel operativo no añade por sí solo una comprobación de identidad. La [guía de Cloudflare para publicar aplicaciones](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) explica esta diferencia.

## Puntos clave

- **Explica la ruta:** distingue el conector, el origen y la comprobación de identidad.
- **Configura una política:** permite que personas específicas accedan a un panel privado.
- **Evalúa la protección:** prueba rutas de acceso permitidas, denegadas y alternativas.
- **Diseña el acceso:** documenta requisitos distintos para visitantes y automatización.

## Antes de empezar

**Audiencia:** propietarios de servidores domésticos que quieren proteger un panel web. El ejemplo presupone un dominio activo en Cloudflare, una aplicación web local operativa y permiso para administrar ambos. **Esfuerzo estimado:** 20–30 minutos para el ejercicio de políticas después de configurar el conector. **Dificultad:** de principiante a intermedia.

**Orden de lectura:** empieza por las funciones de cada producto, sigue una solicitud y configura y revisa una política sencilla. Termina escribiendo una especificación de acceso para tu servicio.

## Qué hace cada producto

El **origen** es el servidor que ejecuta tu aplicación. El conector **`cloudflared`** inicia conexiones desde tu infraestructura hacia Cloudflare, por lo que el origen no necesita una dirección IP enrutable públicamente. Después, las solicitudes y las respuestas viajan por la conexión establecida. [Descripción general de Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Pregunta | Tunnel | Access |
|---|---|---|
| **¿Cómo llega Cloudflare a mi servidor?** | Establece la conexión | No sustituye la conectividad con el origen |
| **¿Quién obtiene acceso?** | Por sí solo no ofrece inicio de sesión de usuario | Evalúa las políticas de acceso configuradas |
| **¿Qué configuro?** | Conector y ruta de la aplicación | Aplicación, proveedor de identidad y políticas |
| **¿Qué demuestra el éxito?** | El origen se alcanza mediante la ruta | Una solicitud cumplió la política configurada |

Un **proveedor de identidad (IdP)** autentica al visitante. Una **política de Access** define una acción y los criterios de coincidencia. Allow admite a los usuarios que coinciden. Bypass desactiva la aplicación de Access para el tráfico coincidente. [Referencia de políticas de Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Sigue una solicitud del navegador

Para **`dashboard.example.com`**, la ruta lógica es:

```text
Navegador -> Cloudflare Access -> conexión del túnel -> cloudflared -> panel
                     |
                     +-> proveedor de identidad cuando se requiere autenticación
```

El **conector inicia la conexión del túnel hacia fuera** desde tu red. Después, las solicitudes del navegador llegan al origen por esa conexión establecida. Una conexión saliente que transporta solicitudes entrantes de la aplicación es la razón principal por la que Tunnel funciona sin reenviar un puerto convencional al origen. [Modelo de conexión de Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Los permisos de la aplicación** son otra decisión. El acceso a un panel no determina automáticamente quién puede cambiar su configuración o borrar sus datos. Si la aplicación incluye roles de consulta y administración, configúralos y pruébalos por separado.

Por ejemplo, **un familiar con acceso de consulta** necesita ver el estado de las copias de seguridad, mientras que tú necesitas permiso para cambiar sus destinos. Anota esos requisitos antes de seleccionar identidades. Dos personas que superan la misma comprobación de Access no deberían recibir automáticamente los mismos privilegios en la aplicación.

## Cuándo necesitas ambos

**La audiencia determina la protección.** Compara estas opciones antes de publicar una ruta:

| Audiencia prevista | Configuración sugerida | Revisar antes de usar |
|---|---|---|
| **Cualquier persona que lea un sitio público** | Tunnel si hace falta para conectarse al origen | La exposición pública es intencionada |
| **Tú y algunos familiares** | Tunnel más Access | Permite solo las identidades previstas |
| **Un origen público existente** | Access con protección independiente del origen | El acceso directo al origen no debe omitir la comprobación |
| **Un script programado** | Tunnel más una política Service Auth | El cliente admite el método de autenticación |

**Access sin Tunnel** funciona con un origen que ya sea accesible. Protege también las rutas alternativas al servidor. Cloudflare recomienda crear primero la aplicación Access al publicar una nueva ruta de túnel. [Requisitos de aplicaciones autoalojadas](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*Para un panel doméstico privado al que se accede mediante un nombre de host público, empieza con Tunnel y Access.*

## Configura una política para el panel

Usa esta **configuración guiada** para dos visitantes previstos. Sustituye las dos direcciones de ejemplo por identidades que controles. Crea la aplicación de Access antes de añadir la ruta pública del túnel.

1. **Aplicación:** abre Zero Trust → Access controls → Applications y crea una aplicación autoalojada con un nombre de host público.
2. **Nombre de host:** introduce el nombre dedicado al panel. Deja la ruta sin restricciones para este ejemplo que abarca todo el nombre de host.
3. **Política:** crea una política Allow llamada `Dashboard viewers`.
4. **Selector de identidad:** añade una regla Include con Emails. Sustituye `alice@example.com` y `bob@example.com` por las dos direcciones previstas.
5. **Inicio de sesión:** selecciona el proveedor de identidad que usan los visitantes y elige de forma deliberada la duración de la sesión.
6. **Ruta:** guarda la aplicación y conecta después el nombre de host con el panel mediante tu túnel.

El [flujo oficial de configuración de aplicaciones](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) documenta estos ajustes. **Resultado esperado:** un visitante nuevo debe autenticarse antes de llegar a la aplicación. Antes de confiar en la política, realiza la prueba con una identidad denegada que se indica abajo.

## Interpreta la lógica de las reglas

**Include** combina alternativas con OR. **Require** añade condiciones obligatorias con AND. **Exclude** elimina a los usuarios coincidentes. Añadir otra condición Include amplía el grupo que puede acceder. [Semántica de las reglas de Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Fragmento de política | Efecto lógico |
|---|---|
| **Include Alice or Bob** | Cualquiera de las identidades nombradas cumple los requisitos |
| **Include Alice, Include a country** | También pueden acceder las personas que coinciden con el país |
| **Include Alice, Require a country** | Alice también debe cumplir la condición del país |

**Ejercicio de revisión de políticas:** el requisito solo incluye a Alice y Bob, pero un compañero añade un país como otra condición Include. Rechaza el cambio porque admite a un grupo adicional. La ubicación geográfica no demuestra que alguien pertenezca a tu hogar.

## Autentica scripts programados

Un **token de servicio** contiene un Client ID y un Client Secret para solicitudes automatizadas. Configura la política de la aplicación para aceptar el token mediante **Service Auth**. Crear un token sin la política correspondiente no concede acceso a la aplicación. [Tokens de servicio de Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Para un script de copias de seguridad o una comprobación de monitorización, guarda el **secreto** en el almacén protegido de credenciales de la herramienta. Usa un nombre de token distinto y una fecha de caducidad deliberada para cada integración. Rota o revoca su token al retirar la integración. La documentación de tokens de servicio explica estas operaciones del ciclo de vida.

**Comprueba explícitamente la compatibilidad del cliente.** Una herramienta que espera una respuesta de API no necesariamente admite el inicio de sesión interactivo en el navegador. Antes de elegir la política, confirma que admita encabezados de solicitud u otro método de autenticación compatible.

## Prueba las decisiones de acceso

Usa estas **comprobaciones de aceptación** para tu implementación:

| Comprobación | Evidencia que debes registrar |
|---|---|
| **Visitante sin sesión** | Access intercepta una solicitud desde una sesión de navegador nueva |
| **Identidad permitida** | La aplicación prevista se carga después del inicio de sesión |
| **Identidad denegada** | Una cuenta no incluida no obtiene acceso a la aplicación |
| **Ruta alternativa** | Los nombres DNS y puertos del origen antiguos no dan acceso imprevisto |
| **Automatización** | El cliente aprobado funciona y una solicitud sin credenciales falla |

**Una pantalla de inicio de sesión visible** solo demuestra que una ruta encontró autenticación. Prueba también el caso denegado y las rutas alternativas. Son comprobaciones recomendadas, no resultados de un ejemplo desplegado.

## Comprueba el límite del origen

Un **origen que confía en la identidad de Access** debe validar el token firmado de la aplicación. Cloudflare lo reenvía en el encabezado **`Cf-Access-Jwt-Assertion`**. La mera presencia del encabezado no demuestra que sea auténtico. [Validación de JWT de Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

Un **JSON Web Token (JWT)** transporta afirmaciones firmadas. Al integrar la identidad de Access con un origen, usa el método de validación documentado, incluidos el emisor esperado y la audiencia de la aplicación. Decodificar un token y leer un campo de correo electrónico no basta para validarlo.

**Issuer** identifica a la autoridad que emite el token. **Audience** identifica a la aplicación prevista. Comprueba la validez y caducidad del token con una biblioteca de validación compatible, en lugar de implementar comprobaciones de firma desde cero.

**Define el límite con claridad:** indica dónde se valida y qué rutas llegan a la aplicación. Una antigua redirección de puerto o un nombre de host alternativo requieren una revisión propia, aunque el nombre principal supere todas las pruebas en el navegador.

## Soluciona discrepancias en las políticas

| Observación | Siguiente comprobación |
|---|---|
| **Un visitante inesperado accede** | Revisa las condiciones Include, las políticas Bypass y la cobertura del nombre de host |
| **Se deniega a un visitante previsto** | Compara la identidad autenticada con los valores exactos del selector |
| **Un script recibe una página de inicio de sesión** | Revisa sus credenciales y la política Service Auth |
| **Un usuario admitido modifica la configuración** | Revisa los roles asignados por la propia aplicación |

**El comportamiento de las sesiones** también afecta a las nuevas pruebas. Access ofrece varias duraciones de sesión, incluidas las de aplicación y globales. Anota el ajuste y usa una sesión nueva al comprobar otra identidad. [Administración de sesiones de Access](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Escribe tu especificación de acceso

Prepara una **especificación breve** antes de añadir otro servicio:

```text
Servicio y nombre de host:
Identidades humanas permitidas:
Roles necesarios en la aplicación:
Credencial de automatización y caducidad:
Otras rutas al origen:
Dónde se validan los tokens de Access:
Resultado de la prueba con identidad permitida:
Resultado de la prueba con identidad denegada:
```

**Criterio de finalización:** otro administrador debe entender quién obtiene acceso, cómo se autentica cada cliente y qué evidencia demuestra la denegación. Si más adelante añades una integración de monitorización, actualiza su credencial y repite la comprobación con una solicitud no autenticada.

## Próximos pasos

Sigue la [guía de configuración de Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) para configurar el conector y aplica después el [flujo oficial de la aplicación Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). Si usas una conexión móvil, consulta los [límites de reenvío de puertos de T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/) antes de elegir la ruta de acceso remoto.
