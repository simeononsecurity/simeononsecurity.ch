---
title: "Tailscale Aperture: configura clientes de IA para inferencia y MCP en 2026"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Dirige solicitudes de modelos y herramientas MCP a través de Tailscale Aperture. Configura Codex, Claude Code, Claude Desktop, OpenCode y Hermes en otro dispositivo o puerta de enlace."
genre: ["Inteligencia artificial", "Herramientas para desarrolladores", "Redes"]
tags: ["Tailscale Aperture", "Configuración de Aperture", "Proxy de IA", "Puerta de enlace LLM", "Puerta de enlace MCP", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "Proxy de inferencia de IA", "API Responses", "API Anthropic Messages", "MCP remoto", "HTTP Streamable", "Tailscale", "IA autoalojada", "Agentes de programación", "Configuración de clientes de IA"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture conecta paneles de clientes con servicios de modelos y herramientas MCP mediante rutas separadas, azul para inferencia y verde para herramientas"
coverCaption: ""
---

## Introducción

Tailscale Aperture proporciona a los clientes de IA una puerta de enlace conectada a la red tailnet para la inferencia de modelos y las herramientas Model Context Protocol (MCP). Cada cliente debe usar una ruta que coincida con su protocolo de API. Las herramientas MCP usan un endpoint separado, y las concesiones de Aperture controlan qué modelos y conectores puede usar cada identidad de Tailscale.

Esta guía explica cómo configurar Codex, Claude Code, Claude Desktop, OpenCode y Hermes en macOS, Linux y Windows. Incluye ajustes de línea de comandos y de escritorio, muestra cómo consultar los ID de modelos disponibles para tu identidad e incluye una instrucción anonimizada que puedes reutilizar al configurar otro dispositivo o instancia de Aperture.

**Elección de ruta:** Las rutas de los endpoints dependen de tu puerta de enlace y de cada protocolo de API. Una ruta Responses como `/codex` no sirve tráfico de Anthropic Messages ni de MCP. Confirma el nombre de host de la puerta de enlace y la ruta de inferencia de cada cliente. Consulta los ID de modelos mediante tu propio acceso a Aperture antes de cambiar los ajustes del cliente.

## Puntos clave

- **El tráfico de modelos** necesita la ruta de API del protocolo del cliente.
- **El tráfico MCP** usa el endpoint separado `/v1/mcp`.
- **Los permisos de la puerta de enlace** deben permitir que tu identidad de Tailscale use cada modelo y conector.
- **La configuración del cliente** solo demuestra que se guardaron los ajustes. Comprueba una solicitud real y una llamada a una herramienta MCP.

## Cómo encajan las rutas

| Propósito | Solicitud del cliente | Ruta de Aperture | Servicio de la ruta |
|---|---|---|---|
| Codex y modelos compatibles con Responses | API OpenAI Responses | Normalmente `/v1`. Una ruta personalizada como `/codex` depende del despliegue. | Inferencia de modelos |
| Inferencia de modelos Claude | API Anthropic Messages | URL base de la puerta de enlace. Aperture gestiona `/v1/messages` | Inferencia compatible con Claude |
| Herramientas MCP | MCP HTTP Streamable | `/v1/mcp` | Herramientas y recursos de los conectores configurados |

{{< figure src="aperture-client-routes.webp" alt="Codex y Hermes usan una ruta Responses, Claude usa Anthropic Messages y los clientes MCP usan la ruta independiente /v1/mcp para acceder a los conectores de Aperture" caption="La inferencia de modelos y el tráfico MCP usan endpoints de Aperture separados" >}}

**Raíces de proveedores:** Aperture añade las rutas de las solicitudes del cliente a la URL base del proveedor. Configura `baseurl` del proveedor con la raíz de su API. No añadas `/v1` a una URL base ascendente cuando la ruta entrante ya incluye `/v1`. Consulta la [referencia de configuración de Aperture](https://tailscale.com/docs/aperture/configuration) para ver cómo se construyen las URL, el registro de modelos y las concesiones.

## Prepara la puerta de enlace

**Antes de editar**, pide a un administrador de Aperture estos valores:

- **Nombre de host de la puerta de enlace:** Usa `http://` con la mayoría de los clientes conectados a la red tailnet. La inferencia de Claude Desktop requiere `https://` con un certificado de confianza.
- **Rutas de inferencia:** OpenAI Responses y Anthropic Messages usan formatos de solicitud distintos.
- **ID de modelos:** Consulta los modelos disponibles para tu identidad de Tailscale con el endpoint que aparece a continuación. Usa los ID literales que devuelve para esa identidad.
- **Autenticación:** Comprueba si el cliente envía una clave API de marcador o una credencial de usuario.
- **Endpoint MCP:** Suele ser `http://<APERTURE_HOST>/v1/mcp` para clientes de la red tailnet. La inferencia de Claude Desktop requiere HTTPS con un certificado de confianza.
- **Concesiones de acceso:** Comprueba los permisos de modelos y conectores de tu identidad de Tailscale.

**Acceso de red:** El dispositivo cliente debe llegar a la puerta de enlace a través de la red tailnet. Un nombre de host no concede acceso a modelos ni herramientas. Aperture deniega el acceso salvo que una concesión coincidente permita el modelo o conector.

### Busca los modelos disponibles para tu usuario

**Consulta la lista de modelos** desde un dispositivo conectado a la misma red tailnet. Aperture usa la identidad de Tailscale del dispositivo y devuelve los modelos concedidos a ese usuario, como se describe en la [guía de concesiones de modelos](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS o Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, usa curl.exe para evitar el alias heredado curl
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**Interpreta el resultado:** Usa cada `id` devuelto como ID del modelo. Comprueba `metadata.provider.id` para identificar el proveedor de Aperture. Elige un modelo cuyo formato de API sea compatible con el cliente. Por ejemplo, Claude Desktop necesita un modelo Anthropic Messages. El [directorio de modelos](https://tailscale.com/docs/aperture/reference/chat) de Aperture también enumera los identificadores disponibles para el usuario autenticado.

**Faltan modelos:** Si no aparece un modelo esperado, pide a un administrador de Aperture que compruebe la configuración del proveedor y tu concesión de modelo. El endpoint no permite que los usuarios se concedan acceso a sí mismos.

**Esquema de URL:** Tailscale recomienda `http://` para la mayoría de los clientes conectados a la misma red tailnet. WireGuard cifra ese tráfico. Claude Desktop requiere `https://` y un certificado de confianza para el sistema operativo. Usa el esquema indicado en cada cliente más abajo.

### Añade un proveedor de inferencia

**OpenAI Responses:** Añade el proveedor ascendente a Aperture y activa el formato de API que usa el cliente. Para un proveedor OpenAI, añade un fragmento como este:

```json
{
  "providers": {
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "models": ["<MODEL_ID>"],
      "compatibility": {
        "openai_chat": true,
        "openai_responses": true
      }
    }
  }
}
```

**Anthropic Messages:** Usa la raíz de la API de Anthropic, el formato de autorización `x-api-key` y la compatibilidad `anthropic_messages`. El ID del modelo también debe aparecer en la lista `models` del proveedor. Añade un fragmento como este:

```json
{
  "providers": {
    "anthropic": {
      "baseurl": "https://api.anthropic.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "authorization": "x-api-key",
      "models": ["<CLAUDE_MODEL_ID>"],
      "compatibility": {
        "anthropic_messages": true
      }
    }
  }
}
```

**Cambios de configuración:** Sustituye cada marcador por los valores de tu proveedor ascendente. Añade los fragmentos a la configuración de Aperture existente. Conserva el resto del archivo actual. Activa las marcas de compatibilidad para las API que admita tu proveedor.

**Concesiones de acceso:** Aperture controla el acceso de cada usuario a cada modelo o conector. Concede a cada usuario de Tailscale previsto solo los permisos necesarios. Este ejemplo da a un usuario acceso a un modelo de un proveedor y a un conector:

```json
{
  "grants": [
    {
      "src": ["<TAILSCALE_USER>"],
      "app": {
        "tailscale.com/cap/aperture": [
          {"role": "user", "models": "openai/<MODEL_ID>"},
          {"connectors": ["teamtools/**"]}
        ]
      }
    }
  ]
}
```

**Concesión de modelo:** Usa el ID del proveedor y el ID del modelo en el patrón de concesión. La [guía de configuración de conectores](https://tailscale.com/docs/aperture/connectors/get-started) muestra la configuración actual de `connectors.servers`. La configuración antigua de nivel superior `mcp.servers` está obsoleta.

### Añade un conector MCP

**Conector MCP:** Aperture se conecta a servidores MCP ascendentes y expone sus herramientas en `/v1/mcp`:

```json
{
  "connectors": {
    "servers": {
      "teamtools": {
        "protocol": "mcp",
        "url": "<UPSTREAM_MCP_ENDPOINT>"
      }
    }
  }
}
```

**URL del conector:** Usa el endpoint MCP completo del servidor ascendente. Después concede a tu usuario de Tailscale acceso a `teamtools/**` o a un patrón más limitado de herramientas. La [referencia del proxy MCP](https://tailscale.com/docs/aperture/mcp-server) explica el endpoint único del cliente y el comportamiento de los conectores.

## Codex CLI y escritorio

**Ajustes compartidos:** Codex CLI y la aplicación de escritorio usan la misma configuración. En macOS y Linux, edita `~/.codex/config.toml`. En Windows, edita `%USERPROFILE%\.codex\config.toml` (los intérpretes que expanden el directorio personal también aceptan `~/.codex/config.toml`). La [presentación de la aplicación Codex](https://openai.com/index/introducing-the-codex-app/) indica que la aplicación de escritorio usa la configuración de Codex CLI. Los ajustes de usuario de Codex están en `~/.codex/config.toml`. La documentación de [configuración básica](https://learn.chatgpt.com/docs/config-file/config-basic) explica los campos de proveedor y MCP de usuario. Añade el proveedor a este archivo, reinicia la aplicación y confirma que el proveedor y el modelo aparecen en la interfaz.

```toml
model = "<MODEL_ID>"
model_provider = "aperture"

[model_providers.aperture]
name = "Aperture Proxy"
base_url = "http://<APERTURE_HOST>/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false
```

**Campos opcionales:** Estos dos valores coinciden con una configuración de proveedor de Codex. Consérvalos solo si tu puerta de enlace y tu configuración de Codex los requieren. La [guía actual de Tailscale para Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) no los incluye, usa `wire_api = "responses"` y señala que Aperture inyecta las credenciales ascendentes. Usa la URL exacta de Responses que indique el administrador de la puerta de enlace. `/codex` es una ruta específica del despliegue. La ruta predeterminada documentada por Tailscale es `/v1`.

**Configuración MCP:** Añade el servidor a la misma configuración de usuario:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Verifica Codex:** Ejecuta `codex mcp list`, inicia una sesión nueva e inspecciona `/mcp`. La lista de servidores confirma el registro. Un elemento de herramienta visible y una llamada correcta confirman su detección y ejecución. La [referencia de configuración de Codex](https://learn.chatgpt.com/docs/config-file/config-reference) documenta los ajustes de proveedor y MCP de usuario.

## Claude Code CLI

**Protocolo:** Claude Code usa Anthropic Messages. Configura el archivo global de Claude Code para que apunte a la puerta de enlace de Aperture compatible con Anthropic. Usa `~/.claude/settings.json` en macOS y Linux, o `%USERPROFILE%\.claude\settings.json` en Windows. En PowerShell, usa la ruta equivalente `$HOME\.claude\settings.json`. La ruta debe servir `/v1/messages`. Codex Responses usa otro protocolo y otra ruta. Tailscale recomienda HTTP para Claude Code en la red tailnet, porque WireGuard cifra la conexión.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Autenticación del cliente:** La guía del cliente de Aperture usa un marcador de posición en `apiKeyHelper`, porque Aperture inyecta la credencial ascendente. Para transferir una suscripción de Claude, el proveedor Anthropic de Aperture debe reenviar la credencial Claude del usuario. En ese caso, deja sin definir `ANTHROPIC_API_KEY` y `ANTHROPIC_AUTH_TOKEN`. Esas variables sustituyen la credencial de suscripción. Sigue las instrucciones actuales de [Claude Code con Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-code) para tu versión de Claude Code y la [guía de Anthropic para puertas de enlace](https://code.claude.com/docs/en/llm-gateway-connect) para consultar las opciones de autenticación.

**MCP por HTTP:** Añade el endpoint con estos comandos:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Verifica Claude Code:** Inicia una sesión y ejecuta `/mcp` para confirmar la conexión. Anthropic recomienda HTTP para servidores MCP remotos en su [documentación de MCP](https://code.claude.com/docs/en/mcp).

## Interfaz de Claude Desktop

**Ajustes separados:** Claude Desktop dispone de una pantalla de inferencia de terceros. Este ajuste dirige las solicitudes de modelos de Claude Desktop a través de Aperture. La configuración MCP requiere otro paso.

1. En Claude Desktop para macOS o Windows, selecciona **Ayuda > Solución de problemas > Activar modo de desarrollador**. En la beta de Linux, usa el mismo menú si aparece. Reinicia la aplicación si lo solicita. Si no aparece el menú, actualiza Claude Desktop y consulta las notas de versión de tu plataforma.
2. Selecciona **Desarrollador > Configurar inferencia de terceros**.
3. En **Tipo de conexión**, elige **Puerta de enlace**. En **Tipo de credencial**, elige **Clave API estática**.
4. Introduce `https://<APERTURE_HOST>` como **URL base de la puerta de enlace**. Usa el nombre de host completo cubierto por un certificado TLS de confianza.
5. Introduce una clave de marcador no vacía, como `aperture`. Aperture ignora el marcador y autentica a través de la red tailnet.
6. Deja vacíos los encabezados de inferencia personalizados.
7. Añade un modelo activado con un ID exacto devuelto por `GET /v1/models` para tu identidad de Tailscale. Filtra por un modelo Anthropic Messages. Introduce manualmente su ID, nombre visible y alias opcional de nivel. Esta pantalla de Claude Desktop no busca modelos automáticamente.
8. Selecciona **Guardar cambios** y luego **Aplicar cambios**. Cierra por completo y vuelve a abrir Claude Desktop.

**Comprobación del protocolo:** La [guía de Claude Desktop para Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) indica que Claude Desktop usa Anthropic Messages en `/v1/messages`. No introduzcas la ruta Codex `/codex` ni selecciones un tipo de conexión compatible con OpenAI.

### Conecta Claude Desktop a MCP

**Acceso MCP privado:** Ejecuta un puente local de tipo stdio en el mismo equipo que Claude Desktop. Añade esto a la configuración MCP local de Claude Desktop:

```json
{
  "mcpServers": {
    "aperture": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://<APERTURE_HOST>/v1/mcp"]
    }
  }
}
```

**Funcionamiento del puente:** El proceso local llega a Aperture mediante la conexión Tailscale del equipo. Usa la ruta de configuración de tu sistema operativo: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; beta de Linux, abre **Ajustes > Desarrollador > Editar configuración** y usa la ruta que abra Claude Desktop. La ruta de Linux varía según el paquete. Reinicia Claude Desktop, inspecciona la lista de conectores y ejecuta una llamada inofensiva a una herramienta. El [proyecto `mcp-remote`](https://github.com/punkpeye/mcp-remote) documenta este puente local a remoto.

**Conectores remotos:** El flujo Ajustes > Conectores de Anthropic necesita un servidor remoto al que pueda llegar el servicio de Anthropic. Un nombre de host exclusivo de la red tailnet es privado para tus dispositivos, así que usa el puente local para el endpoint privado. Si expones un servicio MCP público, configura antes su autenticación y permisos. Consulta la [guía de conectores MCP remotos](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) de Anthropic.

## OpenCode CLI y escritorio

**Ajustes compartidos:** OpenCode CLI y la aplicación de escritorio leen la misma configuración de OpenCode. La documentación actual de OpenCode V2 usa el mapa `providers` para proveedores personalizados y agrupa los servidores MCP en `mcp.servers`. Este ejemplo usa el endpoint de chat compatible con OpenAI en `/v1`. Comprueba que tu proveedor de Aperture admita OpenAI Chat Completions antes de usar esta ruta de modelo.

**Configuración global:** En macOS y Linux, edita `~/.config/opencode/opencode.json`. En Windows, usa `%USERPROFILE%\.config\opencode\opencode.json`. Añade un proveedor compatible con OpenAI y sustituye `<MODEL_ID>` por el ID exacto del modelo de Aperture. OpenCode también acepta `opencode.jsonc` en la misma carpeta para incluir comentarios. La [referencia de configuración](https://opencode.ai/docs/config/) explica la prioridad entre los ajustes globales y los del proyecto.

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aperture/<MODEL_ID>",
  "providers": {
    "aperture": {
      "env": ["APERTURE_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://<APERTURE_HOST>/v1"
      },
      "models": {
        "<MODEL_ID>": { "modelID": "<MODEL_ID>" }
      }
    }
  },
  "mcp": {
    "servers": {
      "aperture": {
        "type": "remote",
        "url": "http://<APERTURE_HOST>/v1/mcp",
        "oauth": false
      }
    }
  }
}
```

**Autenticación del cliente:** `oauth: false` omite el flujo OAuth predeterminado de OpenCode. Aperture identifica al usuario mediante Tailscale. OpenCode también requiere una entrada de autenticación del proveedor, así que define `APERTURE_API_KEY=-` en el entorno local. La aplicación de escritorio también debe recibir la variable. Si no hereda el entorno de tu intérprete, ejecuta `/connect` en la aplicación e introduce `-` para Aperture. No guardes la clave del proveedor ascendente en este archivo. La [guía de proveedores](https://opencode.ai/docs/providers/) y la [guía MCP](https://opencode.ai/docs/mcp-servers/) de OpenCode describen el formato actual. Ejecuta `opencode mcp list` para comprobar el servidor y usa `/mcps` en la aplicación para ver su estado.

## Hermes CLI y escritorio

**Ajustes compartidos:** Hermes Agent guarda los proveedores con nombre y los servidores MCP en `~/.hermes/config.yaml` en macOS y Linux. Las instalaciones nativas de Windows usan `%LOCALAPPDATA%\hermes\config.yaml`. Ejecuta `hermes config path` para confirmar el archivo activo en tu sistema. `HERMES_HOME` puede cambiar la ubicación predeterminada. Hermes Desktop local usa el mismo directorio Hermes y perfil que la CLI. Si Desktop se conecta a una puerta de enlace Hermes remota, configura Aperture en el equipo donde se ejecuta Hermes y confirma que el servidor llega a la red tailnet. Consulta la [guía de Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) para la configuración local y remota.

**Proveedor Responses:** Añade un proveedor con nombre. El valor `api` debe coincidir con el endpoint Responses de tu instancia de Aperture:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Añade key_env solo si tu configuración de Aperture requiere una clave de cliente.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Selección del protocolo:** Para OpenAI Chat Completions, define `transport: chat_completions`. Para Anthropic Messages, elige `transport: anthropic_messages` y usa la URL de la puerta de enlace Anthropic Messages. En la guía actual de [proveedores](https://hermes-agent.nousresearch.com/docs/integrations/providers), Hermes usa los campos `api`, `transport` y `default_model` de un proveedor con nombre.

**Configuración MCP:** Añade Aperture MCP al mismo archivo YAML:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Verifica Hermes:** Ejecuta `hermes mcp` e inspecciona cada conexión en el selector interactivo de servidores. Desktop local expone el mismo perfil de configuración. Hermes documenta los [servidores MCP HTTP remotos](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) y la [referencia completa de configuración MCP](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Verifica ambas rutas

**Haz comprobaciones independientes** para la inferencia de modelos y MCP:

1. Confirma que el dispositivo tiene conectividad Tailscale y llega a la puerta de enlace. Para Claude Desktop, confirma que la puerta de enlace presenta un certificado TLS de confianza.
2. Envía una instrucción breve desde cada cliente configurado. Confirma que aparece una solicitud coincidente en la lista de sesiones de Aperture.
3. Confirma que el ID del modelo seleccionado coincide con un modelo concedido a tu identidad de Tailscale.
4. Abre la pantalla de estado MCP de cada cliente o ejecuta su comando de lista. Confirma que el servidor Aperture se conecta y expone las herramientas esperadas.
5. Llama a una herramienta de solo lectura. Compara el contenido devuelto con el origen ascendente.
6. Revisa los registros de Aperture si falla la llamada al modelo o a la herramienta. Un archivo de configuración guardado no demuestra que la solicitud se haya completado.

| Síntoma | Comprobación |
|---|---|
| La solicitud de modelo devuelve 404 o 405 | Confirma que el endpoint del cliente usa la ruta y el protocolo correctos. No reutilices `/codex` para Anthropic Messages o MCP. |
| El modelo no está disponible | Consulta `/v1/models` como el usuario de Tailscale previsto. Comprueba que aparezca el ID exacto y que el formato de API coincida con el cliente. Pide a un administrador que revise las entradas de proveedor o concesiones que falten. |
| Solicitud no autorizada | Comprueba si el cliente necesita un marcador, un token bearer o transferencia de suscripción. Nunca copies una clave de proveedor ascendente en un archivo de proyecto público. |
| El servidor MCP aparece, pero no muestra herramientas | Comprueba `/v1/mcp`, el estado del conector, sus concesiones y la ruta de red del cliente a Aperture. |
| Claude Desktop no puede conectar con una URL MCP privada | Ejecuta un puente local como `mcp-remote` o usa un conector público aprobado con autenticación apropiada. |

## Repite la configuración en otro dispositivo

**Dispositivo nuevo:** Instala el mismo cliente y conecta primero el dispositivo a la red tailnet. Consulta `/v1/models` desde el nuevo dispositivo para descubrir los modelos concedidos a su identidad de Tailscale. Copia la estructura de la configuración y conserva las credenciales localmente. Sustituye `<APERTURE_HOST>`, `<MODEL_ID>` y `<UPSTREAM_MCP_ENDPOINT>` por valores de la instancia de Aperture de destino. Mantén un endpoint distinto para cada protocolo de API y configura después la ruta `/v1/mcp` para las herramientas. Por último, verifica una solicitud de modelo y una llamada a una herramienta MCP.

**Varias puertas de enlace:** Usa una configuración separada para cada instancia de Aperture. Un dispositivo necesita un endpoint Responses para Codex y Hermes, uno Anthropic Messages para Claude y el endpoint de agregación MCP para las herramientas. Guarda las credenciales de API en el almacén local de secretos de cada cliente o en una variable de entorno. No copies claves de API en `config.toml`, `opencode.json`, `config.yaml` compartidos ni en un repositorio público.

## Instrucción reutilizable para configurar Aperture

**Copia esta instrucción anonimizada** en tu asistente de programación. Sustituye los marcadores por los datos de tu puerta de enlace. El asistente debe consultar Aperture como tu identidad de Tailscale antes de elegir los ID de modelos.

```text
Configura mi puerta de enlace Tailscale Aperture existente y los clientes de IA instalados en este dispositivo.

Clientes incluidos: Codex CLI y escritorio, Claude Code, Claude Desktop, OpenCode CLI y escritorio, Hermes CLI y escritorio.

Primero detecta si este dispositivo usa macOS, Linux o Windows, identifica el intérprete de comandos activo (por ejemplo, zsh, bash o PowerShell) y usa en todo momento las rutas y la sintaxis de comandos de esa plataforma. Inspecciona primero la puerta de enlace actual, la conexión Tailscale, las versiones de los clientes y sus ajustes existentes. Lee la documentación oficial actual. Conserva la configuración no relacionada y crea una copia de seguridad de cada archivo antes de editarlo. No adivines nombres de host, ID de modelos, rutas de API ni credenciales. Guarda las claves de proveedores ascendentes en Aperture, nunca en los archivos del cliente ni en este repositorio.

Consulta los modelos disponibles desde este dispositivo conectado a Tailscale:
1. Consulta `http://<APERTURE_HOST>/v1/models` con la identidad de Tailscale que usan mis clientes. Usa la URL personalizada documentada para la lista de modelos de la puerta de enlace si es distinta.
2. Lee el `id` y `metadata.provider.id` de cada modelo. Esta lista refleja los modelos concedidos a mi identidad. No sustituyas la lista por la del administrador ni inventes ID.
3. Relaciona la compatibilidad de API de cada modelo con cada cliente. Codex usa OpenAI Responses. Los clientes Claude usan Anthropic Messages. OpenCode y Hermes necesitan un proveedor y un transporte compatibles configurados.
4. Cuando sea posible, conserva el modelo predeterminado de cada cliente. Si un cliente necesita uno predeterminado y no he indicado preferencia, muéstrame los modelos compatibles y pídeme que elija. Claude Desktop requiere que introduzcas manualmente el ID exacto del modelo.
5. Si el endpoint no devuelve ningún modelo apropiado, comprueba la configuración del proveedor y las concesiones solo si tengo acceso de administración. De lo contrario, indica qué acceso a modelos debe añadir un administrador. No te concedas acceso.

Localiza el despliegue de Aperture y la fuente de su configuración. No presupongas una ruta de archivo ni sustituyas toda la configuración. OpenAI Responses requiere `openai_responses`. Los clientes Anthropic requieren `anthropic_messages`. Los conectores MCP van en la configuración actual `connectors.servers` y los clientes se conectan mediante `/v1/mcp`.

Antes de cambiar una puerta de enlace compartida, prepara el cambio mínimo para proveedores, conectores y concesiones. Aplícalo solo si tengo autoridad administrativa y esta solicitud autoriza cambios en la puerta de enlace. Si no tengo esa autoridad, indica los cambios exactos propuestos para la persona propietaria de la instancia. No crees concesiones ni amplíes su alcance sin la autorización explícita de la persona propietaria. Conserva los ajustes existentes de la puerta de enlace.

Configura cada cliente instalado con su formato oficial actual y la ruta específica del sistema operativo:
- Codex CLI y escritorio comparten `~/.codex/config.toml` en macOS y Linux, y `%USERPROFILE%\.codex\config.toml` en Windows. Configura el proveedor Aperture, un modelo compatible, `wire_api = "responses"` y MCP en `mcp_servers`.
- Claude Code usa `ANTHROPIC_BASE_URL` y MCP remoto por HTTP. Usa `~/.claude/settings.json` en macOS y Linux, y `%USERPROFILE%\.claude\settings.json` en Windows.
- Claude Desktop usa Modo de desarrollador, Configurar inferencia de terceros, Puerta de enlace, Clave API estática, una URL HTTPS de puerta de enlace con certificado de confianza y un ID de modelo consultado para mi usuario. Usa un puente local `mcp-remote` para MCP privado de la red tailnet. Busca la configuración MCP en Ajustes > Desarrollador > Editar configuración cuando esté disponible. De lo contrario, usa la ruta documentada para el sistema operativo detectado.
- OpenCode usa el esquema V2 actual `providers` y `mcp.servers`. Su configuración global está en `~/.config/opencode/opencode.json` en macOS y Linux, y en `%USERPROFILE%\.config\opencode\opencode.json` en Windows. Define `oauth: false` para el MCP de Aperture. Usa una clave API local de marcador cuando sea necesario.
- Hermes usa un proveedor con nombre, un transporte que coincida con la API del modelo y `mcp_servers`. Usa `~/.hermes/config.yaml` en macOS y Linux. En Windows, comprueba `hermes config path`, normalmente `%LOCALAPPDATA%\hermes\config.yaml`. Comprueba si Hermes Desktop comparte el perfil local de Hermes.

Usa HTTP para el tráfico de la red tailnet cuando el cliente lo admita. La inferencia de Claude Desktop requiere HTTPS con un certificado de confianza. Usa `/v1` salvo que la puerta de enlace documente otra ruta.

Reinicia los clientes configurados. Verifica una solicitud de modelo por cliente en Aperture y una llamada inofensiva de solo lectura a una herramienta MCP. Informa de los modelos consultados para mi identidad, los clientes y archivos modificados, los resultados de verificación y las acciones administrativas pendientes. No instales software, no expongas la puerta de enlace al público, no hagas commits ni publiques.
```

## Conclusión

Una configuración funcional de Aperture depende de tres elementos: una puerta de enlace accesible, una ruta de modelo que coincida con el protocolo del cliente y concesiones para los modelos y conectores MCP necesarios. Los mismos patrones sirven en macOS, Linux y Windows, aunque cada cliente guarda sus ajustes en una ruta distinta según el sistema operativo.

Consulta los ID de modelos como la identidad de Tailscale que los usará. Configura por separado la inferencia de modelos y `/v1/mcp`, y después verifica una solicitud real y una llamada de solo lectura a una herramienta. Al pasar a otro dispositivo o instancia de Aperture, reutiliza la estructura de esta guía, confirma las rutas y concesiones de esa instancia y guarda las credenciales en el almacén local de secretos.

## Próximos pasos

**Práctica con MCP:** Para distinguir entre un servidor guardado y una llamada verificada a una herramienta, lee [Configuración de servidores MCP: permisos, pruebas de herramientas y eliminación segura](/articles/effective-ai-mcp-server-setup/). Para conocer la arquitectura autoalojada más amplia, consulta [Flota de agentes de IA híbrida: Tailscale, LiteLLM y Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).
