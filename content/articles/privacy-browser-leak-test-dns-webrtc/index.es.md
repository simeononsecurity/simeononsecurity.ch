---
title: "Cómo comprobar fugas de DNS y WebRTC en el navegador con una VPN"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Comprueba la IP pública, el resolvedor DNS y las direcciones WebRTC del navegador antes y después de conectar una VPN. Interpreta los resultados e investiga problemas de enrutamiento."
genre: ["Privacidad", "Navegadores", "Redes"]
tags: ["prueba de fuga DNS", "prueba de fuga WebRTC", "prueba de fuga VPN", "prueba de privacidad del navegador", "fuga de dirección IP", "DNS sobre HTTPS", "DNS seguro", "DNS de Firefox", "DNS seguro de Chrome", "candidatos WebRTC", "túnel dividido de VPN", "fuga IPv6", "prueba de resolvedor", "privacidad del navegador", "privacidad de red", "solución de problemas de VPN", "resolvedor DNS", "candidatos ICE", "dirección IP privada", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Ventana de navegador con tres paneles para IP pública, DNS y conexiones entre pares, además de un túnel sólido y una ruta alternativa punteada hacia servidores remotos."
coverCaption: "Compara cada ruta de red antes y después de conectar tu VPN."
---

El icono de conexión de una red privada virtual (VPN) no demuestra que todas las solicitudes del navegador sigan la misma ruta. Comprueba por separado tu **IP pública**, el **resolvedor del Sistema de nombres de dominio (DNS)** y las **direcciones WebRTC**. Cada resultado responde a una pregunta distinta. Esta guía ofrece una comprobación repetible y una forma de investigar resultados inesperados.

<!--more-->

## Puntos clave

- **Compara dos estados:** Registra las mismas pruebas antes y después de conectar la VPN.
- **Interpreta cada resultado por separado:** Un cambio de IP pública no demuestra adónde fueron las consultas DNS.
- **Revisa los candidatos WebRTC:** Busca una dirección pública ajena a la ruta prevista. Una dirección privada significa algo distinto.
- **Cambia un ajuste cada vez:** Vuelve a probar después de cada cambio de VPN, navegador o DNS.

## Antes de empezar

Usa el navegador y la conexión de red que quieres proteger. Decide si la VPN debe cubrir todo el dispositivo o solo algunas aplicaciones. Si la VPN usa túnel dividido, anota si el navegador de prueba pasa por el túnel. Ten a mano la política DNS del cliente VPN para compararla.

El **túnel dividido** envía algunas aplicaciones por la VPN y otras por la red habitual.

Este procedimiento usa las páginas [IP de BrowserLeaks](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) y [WebRTC](https://browserleaks.com/webrtc). El servicio ve tu dirección de conexión cuando lo visitas. Según la descripción de la prueba, su análisis DNS pide al navegador resolver 50 nombres aleatorios. No ejecutes una prueba externa en una red administrada o restringida sin autorización. No introduzcas credenciales, nombres de host internos ni registros privados de navegación en un sitio de pruebas.

> **Aviso:** No publiques tus direcciones IP exactas en capturas ni mensajes de soporte. Anota si las direcciones coinciden con la ruta prevista de tu proveedor de Internet o de la VPN. Comparte los valores reales solo por un canal de soporte aprobado.

## Qué muestra cada prueba

| Comprobación | Qué comparar | Qué no demuestra el resultado |
|---|---|---|
| **IP pública** | Dirección que ve un sitio web normal | Qué resolvedor procesó DNS |
| **Resolvedor DNS** | Servidores observados durante nuevas búsquedas de nombres | Adónde envía DNS cada aplicación |
| **WebRTC** | Candidatos de conexión locales y públicos | Qué candidato usará una llamada posterior |

La página de IP pública informa de la dirección usada para su solicitud web. La página DNS inicia nuevas consultas e informa de los resolvedores que las atienden. WebRTC, sigla de Web Real-Time Communication, permite que las aplicaciones del navegador establezcan conexiones entre pares. La página WebRTC comprueba las direcciones que se exponen durante esas conexiones. Un **candidato ICE** es una posible dirección de red para una conexión entre pares. Una **salida VPN** es la dirección pública que se usa cuando el tráfico sale de la VPN. [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) explica por qué los candidatos de conexión WebRTC a veces incluyen direcciones distintas de la que ve una solicitud web normal, en especial con túneles divididos o proxies.

Un servidor DNS de tu proveedor VPN, un resolvedor distinto elegido dentro de la VPN o un resolvedor cifrado seleccionado por el navegador muestran nombres diferentes en la prueba. El nombre del resolvedor por sí solo no identifica una fuga. Compáralo con la política que querías usar.

## Registra una referencia inicial

Desconecta la VPN solo si tu situación permite una referencia sin túnel. Abre las tres páginas de prueba en un perfil normal del navegador. Ejecuta la prueba DNS y espera el resultado. Registra lo siguiente sin publicar direcciones exactas:

| Campo | Nota de referencia |
|---|---|
| **Navegador y versión** | Nombre, versión y extensiones de privacidad pertinentes |
| **Red** | Wi-Fi doméstico, punto de acceso móvil u otra red aprobada |
| **IPv4 e IPv6 públicas** | Si cada una pertenece a tu conexión habitual |
| **Resultado DNS** | Nombres u operadores de los resolvedores mostrados |
| **Resultado WebRTC** | Candidatos públicos, privados o `.local` mostrados |

Si no puedes desconectar la VPN, empieza con la ruta VPN prevista y marca la referencia sin túnel como no disponible. No deduzcas la dirección habitual de tu proveedor por una etiqueta de ubicación o un mapa. Las bases de datos de ubicación a veces difieren del operador real de la red.

## Repite la prueba con la VPN conectada

Conecta la VPN y confirma que el cliente informa de un túnel activo. Recarga cada página de prueba en el **mismo perfil del navegador**. Ejecuta de nuevo la prueba DNS para crear consultas nuevas. Registra también los resultados IPv4 e IPv6 cuando el servicio los muestre.

Compara los resultados en este orden:

1. **IP pública:** La solicitud web debe mostrar una dirección coherente con la salida VPN o la ruta que configuraste intencionalmente. Si el navegador debería estar dentro del túnel, que siga apareciendo la IP habitual del proveedor indica un problema de enrutamiento.
2. **DNS:** Compara cada resolvedor mostrado con los ajustes DNS del navegador y de la VPN. Investiga un resolvedor del proveedor de Internet fuera del túnel previsto. Un resolvedor externo con nombre es normal si lo seleccionaste intencionalmente en el navegador.
3. **WebRTC:** Compara el candidato WebRTC público con la salida VPN y la IP pública de referencia. Si el navegador debe enviar todo el tráfico por la VPN, que la IP pública habitual aparezca solo en WebRTC merece atención.
4. **Direcciones privadas:** Una dirección de los [rangos privados RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) o un candidato `.local` difiere de una IP pública del proveedor. Registra la entrada local y decide si el sitio debe conocerla.

El [estándar de tratamiento de IP de WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) describe cómo una aplicación obtiene otras direcciones públicas o privadas mediante la detección de candidatos ICE. El diseño de [candidatos de host mDNS de Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) sustituye algunas direcciones privadas por nombres `.local`. Un resultado WebRTC vacío es **inconcluso** si JavaScript, la API o el servidor de pruebas no funcionó. Un resultado vacío no demuestra una protección completa.

> **Resultado esperado:** La solicitud web normal del navegador y los candidatos WebRTC públicos siguen la ruta elegida. Los resultados DNS coinciden con la política del resolvedor de VPN o del navegador que registraste.

## Investiga una discrepancia de DNS

Primero comprueba si el navegador elige su propio resolvedor. Los ajustes de [DNS sobre HTTPS de Firefox](https://support.mozilla.org/en-US/kb/dns-over-https) muestran el estado activo y el nivel de protección. La protección predeterminada recurre al resolvedor del sistema en ciertas condiciones y respeta señales de red. Los niveles Aumentada y Personalizada usan un proveedor seleccionado con mecanismos de respaldo. El nivel Máxima avisa cuando falla la resolución segura. El estado y la lista de excepciones importan más que un interruptor aislado.

La [guía de DNS seguro de Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) describe el modo automático y un proveedor personalizado. El modo automático recurre a consultas sin cifrar si falla la resolución segura. Un proveedor personalizado no vuelve por defecto al modo sin cifrar. Los dispositivos administrados y los controles parentales limitan este ajuste. Consulta la interfaz actual del navegador antes de cambiar una política administrada.

Si el resolvedor del navegador no es la causa, compara el ajuste DNS del cliente VPN, la lista de aplicaciones del túnel dividido, el resolvedor del sistema operativo y la ruta IPv6. Cambia un elemento y repite la prueba DNS. Una prueba DNS del navegador mide la ruta de consulta de ese navegador. El resultado no indica cómo resuelven nombres otras aplicaciones. Si tu red usa [filtrado DNS](/articles/nextdns-vs-adguard-ad-blocker-comparison/), prueba un dominio que bloquees intencionalmente y otro que permitas. No tomes la ausencia de un anuncio como prueba de la ruta del resolvedor.

## Investiga una discrepancia de WebRTC

Comprueba si el navegador está excluido del túnel VPN o usa un proxy fuera de la ruta prevista. Corrige la ruta y vuelve a probar. No desactives IPv6 ni WebRTC como primera respuesta a un único resultado ambiguo. El [estándar WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) describe el equilibrio entre exponer direcciones y mantener el rendimiento de llamadas directas. Restringir candidatos o forzar un proxy afecta a las videollamadas y otras conexiones entre pares.

Si el navegador o la VPN ofrecen un control documentado de tratamiento de IP WebRTC, lee su descripción actual y elige una política acorde con el uso que haces de las llamadas. Vuelve a probar el candidato público. Una dirección local por sí sola no demuestra que la IP pública del proveedor haya salido de la VPN. Una IP pública expuesta del proveedor, frente a una dirección HTTP distinta de la VPN, es una señal más sólida.

## Conserva un registro de pruebas

| Campo | Resultado que debes anotar |
|---|---|
| **Fecha y navegador** | Versión, perfil, extensiones y red |
| **Ruta prevista** | VPN para todo el dispositivo, túnel dividido o proxy del navegador |
| **Antes y después** | Operador de IP pública, operador DNS y candidato WebRTC público |
| **Discrepancia** | Resultado que no coincidió con la política prevista |
| **Cambio único** | Ajuste cambiado y motivo |
| **Nueva prueba** | Nuevo resultado e incertidumbre pendiente |

Repite la comprobación después de cambiar la configuración del navegador, la VPN o la red. Un resultado limpio cubre el navegador, perfil, red y momento probados. No demuestra anonimato ni cubre todas las aplicaciones. Si aún eliges navegador, consulta la [comparación de navegadores privados](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) para ver funciones y luego ejecuta esta prueba en tu propia configuración.

## Próximos pasos

Repite la prueba después de cambiar el navegador, la VPN o la red. Consulta la [comparación de navegadores privados](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) para elegir uno.
