---
title: "Por qué se omite el filtrado DNS: comprueba la ruta del resolver"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Averigua por qué un dispositivo o navegador omite tu filtro DNS. Compara consultas directas y normales, revisa los registros y comprueba DNS cifrado, VPN, IPv6 y ajustes del router."
genre: ["Redes domésticas", "DNS", "Privacidad"]
tags: ["omisión del filtrado DNS", "omitir Pi-hole", "registro de consultas DNS", "DNS seguro del navegador", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "DNS de VPN", "DNS IPv6", "DHCP DNS del router", "Resolve-DnsName", "solución de problemas DNS", "prueba del filtro DNS", "solución de problemas NextDNS", "solución de problemas AdGuard DNS"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "La ruta DNS azul de un portátil atraviesa un filtro y termina en un símbolo de bloqueo, mientras que la ruta naranja del navegador llega a otro resolver."
coverCaption: "Sigue la ruta de la consulta antes de cambiar la regla del filtro."
---

Configuraste un resolver con filtrado, pero un dispositivo todavía llega a un dominio que tu política bloquea. La causa podría ser la regla, la asignación del Domain Name System (DNS) del dispositivo, un resolver cifrado del navegador o una VPN. **Comprueba la ruta antes de cambiar los ajustes.** Una consulta directa al filtro responde a una pregunta distinta de la consulta normal del dispositivo.

<!--more-->

## Puntos clave

- **Comprueba primero la regla:** Confirma que el filtro recibe y bloquea un dominio de prueba seguro.
- **Sigue cada capa:** El router, el sistema operativo, el navegador, la VPN y los ajustes móviles influyen en el enrutamiento DNS.
- **Usa consultas nuevas:** Relaciona un nombre de host nuevo y su hora con el registro de consultas del filtro.
- **Indica el límite:** Una consulta observada demuestra una ruta, no el comportamiento de todas las aplicaciones y dispositivos.

## Antes de empezar

Reserva unos 20 minutos. Necesitas acceso al registro de consultas del resolver filtrante, un dispositivo con el problema y una copia de los ajustes DNS del router. Los ejemplos usan un portátil Windows y **Pi-hole**, pero la misma comparación sirve para cualquier resolver que ofrezca registros por cliente. Identifica primero la dirección exacta del filtro. No publiques direcciones privadas de clientes, registros de consultas ni reglas de política.

Elige un **dominio de prueba inocuo** que tu política ya bloquee. Otra opción es añadir temporalmente una regla de denegación exacta para un dominio que controles en un perfil de prueba. Anota la regla y elimínala al terminar. No uses un dominio de malware activo como prueba. Una página bloqueada es un síntoma útil, pero el registro del resolver ofrece pruebas más sólidas sobre la ruta.

| Capa | Pregunta |
|---|---|
| **Filtro** | ¿Una consulta directa llega al resolver previsto y coincide con la regla? |
| **Dispositivo** | ¿Qué servidores DNS asigna la red? |
| **Navegador o aplicación** | ¿Este cliente usa el resolver del dispositivo o una ruta distinta? |
| **VPN o relay** | ¿Un túnel activo cambia el destino de las consultas? |

## Comprueba que el filtro funciona

Abre el registro de consultas del resolver. Consulta el dominio bloqueado elegido directamente en el filtro. En Windows, usa PowerShell e introduce la dirección del filtro y el dominio de prueba cuando se soliciten:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

La [referencia de Microsoft para **`Resolve-DnsName`**](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) define **`-Server`** como una consulta al resolver indicado. Busca la consulta en el registro del filtro y comprueba la respuesta y la regla coincidente. La [documentación de Pi-hole sobre consultas y registros](https://docs.pi-hole.net/main/pihole-command/) describe sus herramientas de consulta locales. Si la consulta directa se permite, corrige la regla o la asignación del grupo de clientes antes de investigar una omisión. Si no llega al filtro, comprueba la dirección, el servicio y la ruta de red.

**Esta prueba directa no demuestra que el portátil use normalmente el filtro.** La opción **`-Server`** reemplaza el resolver predeterminado para esta consulta. Esta distinción evita un falso positivo frecuente.

## Sigue la ruta del dispositivo

Usa un nombre de host nuevo para evitar una entrada anterior en la caché DNS. El siguiente ejemplo envía una consulta directamente al filtro y otra mediante la selección normal de resolver del portátil. Los nombres son distintos para identificar qué entrada del registro corresponde a cada ruta. Una respuesta **NXDOMAIN** significa que el servidor DNS informa que el nombre de host no existe. Es normal si el nombre aleatorio no se usa. Aquí importa si la consulta aparece en el registro del filtro.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Busca ambos nombres exactos en el registro del filtro y anota la hora y el cliente indicado. Si aparece **`direct-`** pero no **`default-`**, revisa los servidores DNS asignados al portátil. En Windows, **`Get-DnsClientServerAddress`** muestra las direcciones DNS de cada interfaz. Comprueba el adaptador Wi-Fi o Ethernet activo, no uno desconectado. La [referencia del cliente DNS de Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) describe este comando de solo lectura.

Deja los errores visibles durante la primera prueba. Un error o un tiempo de espera agotado necesita un diagnóstico separado y no equivale a una entrada ausente del registro.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Compara las filas IPv4 e IPv6. **DHCP** asigna ajustes de red, incluidos los servidores DNS. **IPv6** es la familia más reciente de direcciones del Internet Protocol y usa direcciones de 128 bits. Una concesión IPv4 podría señalar el filtro mientras los anuncios IPv6 del router proporcionan otro servidor DNS. Comprueba los anuncios **DHCP** y **DNS IPv6** del router y renueva la concesión de red del dispositivo después de corregirlos. La [guía posterior a la instalación de Pi-hole](https://docs.pi-hole.net/main/post-install/) explica cómo DHCP dirige los clientes a Pi-hole. Su [ejemplo de router](https://docs.pi-hole.net/routers/fritzbox/) aborda los anuncios DNS IPv6.

Si el registro muestra el **router** como cliente, quizá el router reenvía consultas en nombre de los dispositivos. El registro del filtro demuestra entonces que el router llegó al filtro, pero no cuál dispositivo originó la consulta. Confirma cómo reenvía consultas el router antes de considerar que falta la identidad del cliente.

## Comprueba el DNS del navegador

Una consulta desde la línea de comandos prueba la ruta del resolver del dispositivo. En cambio, el navegador podría usar **DNS over HTTPS (DoH)**. Abre el mismo dominio de prueba bloqueado en el navegador y observa si aparece una consulta correspondiente en el registro del filtro. Vacía la caché DNS del navegador o usa un nombre de host nuevo cubierto por una regla de prueba si los resultados guardados dificultan la comparación.

En **Chrome para ordenador**, abre **Configuración > Privacidad y seguridad > Seguridad > Usar DNS seguro**. La [ayuda de Google Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) indica que el modo automático usa el proveedor actual y vuelve a búsquedas sin cifrar si falla. Un proveedor personalizado seleccionado no vuelve del mismo modo. Anota el modo y el proveedor seleccionados antes de cambiar el ajuste.

En **Firefox**, abre **Configuración > Privacidad y seguridad > DNS sobre HTTPS**. La [guía de niveles de protección de Mozilla](https://support.mozilla.org/en-US/kb/dns-over-https) distingue los modos Predeterminado, Aumentado, Máximo, Personalizado y Desactivado. La [descripción general de DoH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) explica cuándo un resolver del navegador omite un filtro DNS local. Repite la prueba después de un solo cambio controlado y luego restaura el ajuste de privacidad deseado.

**No llames omisión a toda consulta ausente del navegador.** El navegador podría reutilizar datos en caché, acceder a una dirección ya conocida o usar un proxy. Compara un nombre nuevo, una ventana de tiempo coincidente y el ajuste del resolver del navegador antes de concluir adónde fue la consulta.

## Comprueba las rutas móviles y VPN

En **Android**, revisa **Configuración > Redes e Internet > DNS privado**. El nombre de host de un proveedor selecciona un servicio DNS privado distinto del DNS anunciado por el router. Los [ajustes de red de Android de Google](https://support.google.com/android/answer/9654714?hl=en) explican las opciones Desactivado, Automático y Nombre de host del proveedor. Para obtener un resultado local controlado, prueba por Wi-Fi con los datos móviles desactivados y luego restaura el ajuste habitual.

En **dispositivos Apple**, comprueba si **iCloud Private Relay** está activo para la red y si Safari sigue la ruta esperada. Apple afirma que [Private Relay protege la navegación de Safari y la información DNS](https://support.apple.com/en-gb/102602). Sus [controles de red](https://support.apple.com/en-ie/102022) describen el tratamiento por red cuando el filtrado entra en conflicto con Private Relay. No generalices un resultado de Safari a todas las aplicaciones del dispositivo.

Una **VPN** podría proporcionar su propio resolver DNS o enviar las consultas por el túnel. Anota si la VPN está conectada, sus ajustes DNS y su política de túnel dividido. Compara la misma prueba con la VPN activada y desactivada solo si tu política de seguridad lo permite. Un resultado distinto identifica una diferencia de ruta. Por sí solo, no demuestra una fuga ni un fallo del filtro.

## Interpreta los resultados

| Evidencia | Siguiente comprobación probable |
|---|---|
| **La consulta directa no aparece en el registro del filtro** | Dirección del filtro, servicio DNS, registro o accesibilidad de red |
| **La consulta directa se permite** | Regla de denegación exacta, política de grupo o prioridad de reglas |
| **Consulta directa registrada, consulta normal ausente** | DHCP, DNS estático del dispositivo, DNS IPv6 o resolver VPN |
| **Consulta normal registrada, consulta del navegador ausente** | DoH del navegador, caché del navegador, proxy o relay |
| **Ambas registradas y bloqueadas, pero el sitio carga** | Otro nombre de host, contenido en caché, dirección directa o ruta de la aplicación |

**La falta de registros es ambigua** si el registro está desactivado, el router reenvía en nombre del cliente o la prueba reutiliza datos guardados. Repite la prueba con un nombre nuevo y revisa la hora de la consulta antes de cambiar reglas del firewall. Bloquear DNS sin cifrar hacia resolvers externos no obliga a un navegador cifrado o una VPN a usar tu filtro. La [guía de Pi-hole para OPNsense](https://docs.pi-hole.net/routers/opnsense/) presenta el bloqueo de DNS externo como un control de red opcional. Las políticas del dispositivo y la configuración del navegador siguen siendo controles separados.

## Corrige y vuelve a probar

Cambia una capa a la vez. Corrige los anuncios DHCP o DNS IPv6, elimina un resolver estático no previsto, selecciona el proveedor DNS deseado en el navegador o ajusta la política DNS de la VPN. No debilites en silencio el DNS cifrado ni la protección relay en todos los dispositivos para resolver un solo fallo de prueba. Registra el dispositivo de origen, la interfaz, la dirección del filtro, el nombre consultado, la hora, la respuesta, el cliente del registro, el modo del navegador, el estado de la VPN y el cambio realizado.

Después de cada cambio, repite las pruebas **directa**, **normal** y **del navegador**. Usa un nombre de host nuevo en cada ejecución. Si un dispositivo tiene varios perfiles de red, prueba cada uno por separado. La [comparación de resolvers DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) ayuda a elegir un servicio. La [prueba de fugas del navegador](/articles/privacy-browser-leak-test-dns-webrtc/) responde a otra pregunta: qué información de red sale de tu configuración de navegador y VPN. **Un resultado fiable del filtro requiere una regla comprobada y una ruta del cliente comprobada.**

## Próximos pasos

Repite las pruebas directa, normal y del navegador después de cada cambio controlado. Consulta la [comparación de resolvers DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) al elegir un servicio de filtrado.
