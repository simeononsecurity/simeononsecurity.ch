---
title: "Planificar y probar la segmentación VLAN de un homelab"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Crea un plan VLAN para dispositivos de confianza, servidores, IoT e invitados. Registra el tráfico permitido, configura la red por etapas y comprueba el aislamiento."
genre: ["Homelab", "Seguridad de redes", "Redes"]
tags: ["VLAN homelab", "segmentación VLAN", "red IoT", "red de invitados", "firewall homelab", "enrutamiento entre VLAN", "802.1Q", "aislamiento de red", "prueba VLAN", "VLAN pfSense", "puerto de acceso", "puerto troncal", "reglas de firewall", "seguridad homelab", "plan de red", "subred", "DHCP", "DNS", "switch administrable", "SSID inalámbrico"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Un router y un switch de homelab separan portátiles, servidores, dispositivos IoT e invitados en zonas de red protegidas."
coverCaption: "Planifica los límites de las VLAN y prueba cada ruta permitida y bloqueada."
---

Un homelab suele conectar portátiles, servidores, cámaras y dispositivos de invitados a una sola red. La **segmentación VLAN** coloca estos grupos en redes separadas. Un router, firewall o switch de capa 3 enruta el tráfico entre ellas. Las reglas de firewall o las listas de control de acceso del switch controlan esos flujos enrutados. Esta guía te ayuda a preparar el plan, aplicar un cambio por vez y probar el resultado.

## Puntos clave

- **Agrupa por confianza:** coloca los dispositivos de administración, servidores, dispositivos IoT e invitados en redes distintas cuando sus necesidades de acceso difieran.
- **Registra las rutas permitidas:** anota el origen, destino, servicio y motivo de cada conexión entre redes.
- **Configura ambas capas:** los ajustes del switch y del punto de acceso asignan los dispositivos a las VLAN. Las reglas de firewall o las listas de control de acceso del switch controlan el tráfico enrutado.
- **Prueba ambos resultados:** verifica una conexión permitida y otra bloqueada desde cada red pertinente.

## Antes de empezar

Necesitas un router o firewall con interfaces VLAN, o un switch de capa 3 que admita enrutamiento VLAN y listas de control de acceso. Un switch administrable transporta las VLAN cableadas. Si separas los clientes inalámbricos, necesitas también un punto de acceso con redes Wi-Fi asociadas a VLAN. Mantén un dispositivo en la red de administración actual mientras cambias la configuración. Guarda primero la configuración del router, switch y punto de acceso. Los pasos siguientes usan un **plan ilustrativo**. Adapta las direcciones y los puertos a tus equipos.

Una **interfaz VLAN** conecta la puerta de enlace con una VLAN. La puerta de enlace puede ser un router, firewall o switch de capa 3. Un **ámbito DHCP** es el rango de direcciones que un servicio DHCP ofrece a los dispositivos de esa red. Un **relay DHCP** reenvía las solicitudes de direcciones de una VLAN a un servidor DHCP en otra red. Usa un relay cuando la puerta de enlace no asigne direcciones para esa VLAN y el servidor DHCP esté en otro lugar. La [guía de Juniper sobre relay DHCP](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) describe esta ruta. Un **SSID** inalámbrico es el nombre de red al que se conectan los clientes. Si tus equipos no incluyen un switch administrable o punto de acceso compatible con VLAN, empieza con la red de invitados integrada y comprueba su aislamiento antes de comprar o cambiar hardware.

Si primero necesitas los conceptos básicos, lee [subredes y VLAN](/articles/networking-basics-what-are-subnets-and-vlans/). La [guía de segmentación de redes](/articles/how-to-perform-network-segmentation-for-improved-security/) del sitio cubre el concepto de seguridad más amplio. CISA describe redes domésticas separadas para invitados y dispositivos del Internet de las cosas en su [guía Federal Mobile Workplace Security](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Advertencia:** Cambiar la VLAN del puerto que transporta tu conexión de administración puede dejarte sin acceso. Mantén acceso físico y una ruta de recuperación conocida hasta que todas las redes superen las pruebas.

Antes de mover un cable, exporta la configuración de cada dispositivo. Anota también la IP de administración actual, el puerto del switch, el ajuste VLAN y el inicio de sesión de administrador. Deja un puerto de administración conocido y un portátil en la red original. Si un cambio corta el acceso, vuelve a conectar el portátil a ese puerto, restaura el ajuste o la configuración guardada y confirma que responde la puerta de enlace anterior antes de intentarlo de nuevo. Si no hay una ruta de administración disponible para el switch, usa la consola documentada o el procedimiento de recuperación local. No restablezcas el equipo hasta saber qué borra el restablecimiento.

## Inventariar dispositivos y flujos

Anota cada dispositivo, su dirección actual, quién lo administra y los servicios que necesita. Define por qué cada dispositivo debe acceder a otra red. Por ejemplo, un portátil podría administrar un servidor, mientras que una cámara solo requiere acceso a una grabadora y a un servidor DNS. Un teléfono de invitado necesita Internet, pero no acceso a los servidores.

| Grupo de dispositivos | Ejemplos | Acceso necesario |
|---|---|---|
| **Administración** | Portátil de administración, interfaces de gestión del switch y punto de acceso | Administrar el router, switch, punto de acceso y servidores |
| **Servidores** | Hipervisor, NAS, destino de copias de seguridad | Actualizaciones, DNS, tráfico de aplicaciones aprobado |
| **IoT** | Cámaras, enchufes inteligentes, dispositivos multimedia | DNS, servicio horario, controlador o grabadora específicos |
| **Invitados** | Teléfonos y portátiles de visitantes | Internet, DNS, sin acceso a subredes privadas |

Registra las excepciones antes de añadir reglas. Las funciones de descubrimiento local, como la transmisión a una pantalla, suelen depender del tráfico multicast, que por defecto no atraviesa un límite enrutado. No abras todo el tráfico entre VLAN para solucionar un problema de descubrimiento. Identifica el protocolo y añade la excepción compatible más limitada.

## Asignar VLAN y direcciones

Asigna un identificador VLAN y una subred IP diferente a cada grupo. Este **plan ilustrativo** usa direcciones reservadas para documentación y supone que el router proporciona DHCP y DNS. No copies la tabla a una red activa sin comprobar si hay conflictos de direcciones.

| Red | ID de VLAN | Subred | Puerta de enlace de ejemplo |
|---|---:|---|---|
| **Administración** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Servidores** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Invitados** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Estos rangos reservados para documentación ilustran el diseño, tal como define [RFC 5737](https://www.rfc-editor.org/info/rfc5737). Para tu laboratorio real, usa direcciones privadas de [RFC 1918](https://www.rfc-editor.org/info/rfc1918), con una subred sin solapamientos por VLAN. Registra en tu plan cada puerta de enlace real, grupo DHCP, dirección DNS y reserva de dispositivo.

Los **puertos de acceso** transportan la red de un solo dispositivo sin etiqueta VLAN. Los **puertos troncales** transportan VLAN seleccionadas con etiqueta entre el router, switch y punto de acceso. Configura el mismo ID de VLAN y el mismo ajuste nativo o sin etiqueta en ambos extremos. La [guía de Netgate sobre switches VLAN](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) explica los puertos troncales etiquetados, los puertos de acceso sin etiqueta y los ID de VLAN por puerto. Evita usar la VLAN 1 predeterminada para administración si tu equipo permite una VLAN separada, como explica la [guía de seguridad VLAN](https://docs.netgate.com/pfsense/en/latest/vlan/security.html) de Netgate.

El tráfico **nativo** o **sin etiqueta** de un troncal no lleva etiqueta VLAN. Ambos extremos deben asignarlo a la misma VLAN, o un dispositivo podría acabar en la red equivocada. Permite solo las VLAN que necesite el enlace. Deshabilita los puertos sin uso del switch o asígnalos a una red restringida. Netgate también recomienda no considerar una VLAN como una frontera de seguridad completa si un atacante controla un puerto del switch. Protege los puertos físicos y las credenciales de los dispositivos, además del tráfico enrutado.

## Crear una matriz de tráfico

Una VLAN por sí sola separa dominios de difusión. El **enrutamiento entre VLAN** en el router o switch de capa 3 sigue requiriendo reglas de acceso. Decide qué dispositivo enruta el tráfico entre VLAN. Si un switch de capa 3 enruta localmente, el tráfico entre sus VLAN quizá nunca llegue al firewall del router. Aplica listas de control de acceso equivalentes en el switch o enruta el tráfico por el firewall. Después prueba en el punto donde se aplican las reglas. Comprueba la dirección de la ACL del switch y si mantiene el estado de las conexiones. Muchas ACL de switch comparan los paquetes por separado en cada dirección, así que una conexión permitida podría requerir una regla limitada para el tráfico de respuesta. La [guía de Cisco sobre ACL](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) describe la dirección de interfaz y las coincidencias ordenadas de paquetes. Usa el inventario de dispositivos para registrar las conexiones que quieres permitir. Las siguientes entradas son ejemplos, no un conjunto universal de reglas.

| Origen | Destino | Servicio | Decisión |
|---|---|---|---|
| **Administración** | Interfaz de administración del servidor | TCP 443 | Permitir a dispositivos de administración aprobados |
| **Administración** | Interfaces de administración del router, switch y punto de acceso | Puertos de administración documentados | Permitir a dispositivos de administración aprobados |
| **IoT** | Grabadora de cámaras | Puerto documentado de la grabadora | Permitir solo si hace falta |
| **IoT** | Servicio DNS y horario aprobado | DNS y NTP | Permitir solo hacia los servicios elegidos |
| **IoT** | Subred de administración | Cualquiera | Denegar |
| **Invitados** | Subredes privadas | Cualquiera | Denegar |
| **Invitados** | DNS e Internet | DNS, tráfico web | Permitir mediante el resolver y la puerta de enlace aprobados |

Incluye los servicios del router en el plan. Una regla que bloquee el acceso de IoT a otras VLAN quizá deje accesible la interfaz de administración del router. Limita los servicios de administración a la red de administración. Empieza con las reglas de permiso necesarias y una denegación predeterminada para el resto del tráfico enrutado. Comprueba si ya existen reglas amplias de permiso antes de asumir que la política predeterminada lo deniega todo. Las [prácticas recomendadas de firewall](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) de Netgate indican que la LAN predeterminada de pfSense incluye una regla de permiso. Si usas pfSense, su [metodología de reglas](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) explica que las reglas de interfaz filtran el tráfico que entra en esa interfaz y que las conexiones permitidas crean un estado para el tráfico de respuesta.

La tabla de ejemplo cubre IPv4. Si tu red usa IPv6, asigna un prefijo IPv6 y una política a cada VLAN, revisa los anuncios del router y prueba también las rutas IPv6 permitidas y denegadas. Bloquear IPv4 no demuestra aislamiento de IPv6. Si no quieres enrutar IPv6, revisa la configuración IPv6 del router y las direcciones de los clientes en vez de suponer que IPv6 no existe. Netgate documenta el [comportamiento del firewall IPv6](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) y los [anuncios del router](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Configurar una red a la vez

1. Elige la puerta de enlace de la VLAN. Si enruta el router o firewall, crea allí una interfaz VLAN y asígnale la dirección de puerta de enlace. Si enruta un switch de capa 3, crea la interfaz VLAN en el switch. Configura un ámbito DHCP en la puerta de enlace o un relay DHCP hacia el servidor DHCP actual. Confirma que se puede alcanzar el resolver DNS aprobado. La [guía de configuración VLAN de Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) enumera los pasos de interfaz y servicios para una puerta de enlace pfSense.
2. Si el router es la puerta de enlace VLAN, añade esa VLAN al troncal entre el router y el switch. Si lo es el switch de capa 3, deja que el switch mantenga la dirección de puerta de enlace de la VLAN y enruta hacia el router o firewall mediante una red de tránsito separada o un enlace ascendente enrutado. Configura en el switch una ruta predeterminada hacia el router ascendente. Añade en el router una ruta de retorno para cada VLAN cuya puerta de enlace esté en el switch. Comprueba la política del firewall del router y el NAT saliente de esas subredes si necesitan Internet. No configures la misma dirección de puerta de enlace o ámbito DHCP en ambos dispositivos. Añade la VLAN al troncal pertinente entre switch y punto de acceso si los clientes inalámbricos necesitan la red. La [guía de Cisco sobre enrutamiento entre VLAN](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) muestra puertas de enlace VLAN en un switch. Netgate documenta las [rutas de retorno](https://docs.netgate.com/pfsense/en/latest/routing/static.html) y el [NAT saliente](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) para redes detrás de un router interno.
3. Asigna a la VLAN un puerto de acceso o SSID inalámbrico de prueba. Conecta a ese puerto o SSID un dispositivo de prueba que no sea crítico.
4. Añade las reglas de firewall o ACL del switch previstas en el dispositivo que enruta la VLAN. Verifica que se deniegue el resto del tráfico enrutado. Comprueba la dirección de la ACL y el tráfico de respuesta si el switch no mantiene el estado. Prueba el acceso a cada puerta de enlace, interfaz de administración, subred local y a IPv6 cuando corresponda. Permite solo las rutas de tu matriz de tráfico. Limita la administración a la red de administración. Revisa el orden de las reglas y elimina o restringe reglas amplias de permiso existentes solo después de que funcione la ruta de administración de prueba.
5. Confirma que el dispositivo de prueba recibe una dirección, puerta de enlace y servidor DNS de la subred prevista. Después ejecuta las comprobaciones de conexión siguientes antes de mover otros dispositivos.

No muevas el último dispositivo de administración hasta que funcione la ruta de sustitución. Guarda la configuración que funciona después de que cada red supere las pruebas. Si falla DHCP, DNS o el acceso de administración, devuelve el dispositivo de prueba al puerto o SSID original. Restaura desde la configuración guardada el último cambio del switch o router y vuelve a probar la red original antes de continuar.

## Probar aislamiento y acceso

Usa un servicio bajo tu control que sepas que está escuchando en el destino. En un dispositivo de prueba Windows, sustituye la dirección y el puerto de ejemplo por un servidor real y ejecuta:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

El campo **`TcpTestSucceeded`** indica si se completó una conexión TCP. La [referencia de Microsoft para Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) documenta los parámetros `-ComputerName` y `-Port`. Una conexión fallida por sí sola no demuestra que la regla de firewall funcionara. El servicio podría estar detenido o el firewall del host podría rechazar el tráfico. Comprueba el servicio de destino y el registro del firewall de red antes de sacar conclusiones.

Prueba desde un dispositivo conectado realmente a cada VLAN de origen. Antes de cada prueba, registra la dirección de origen, la puerta de enlace y el servidor DNS. Comprueba una conexión permitida al servicio previsto, una conexión denegada a un servicio interno fuera de la matriz, una consulta DNS mediante el resolver previsto y el acceso a Internet si está planeado. En una VLAN cuya puerta de enlace está en un switch, comprueba la ruta predeterminada del switch, la ruta de retorno del router y el camino de vuelta desde el destino si falla una conexión permitida. Repite las pruebas permitidas y denegadas con direcciones IPv6 si IPv6 está activo. En pfSense, **Status > System Logs > Firewall** muestra acciones permitidas o bloqueadas registradas. La [guía de Netgate sobre registros del firewall](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) describe esa vista. Compara en el registro el origen, destino, puerto y regla con tu prueba. Si la prueba funciona cuando no debería, revisa reglas amplias de permiso y entradas de estado existentes. Inicia una conexión nueva después de cambiar reglas, ya que una conexión activa podría seguir funcionando por su estado existente.

Para comprobar DNS en Windows, ejecuta `nslookup example.com` y compara el servidor mostrado con el resolver previsto. Luego intenta una consulta desde un cliente invitado o IoT con DNS restringido. Una consulta correcta no demuestra por sí sola que el cliente haya usado el resolver elegido, así que comprueba el servidor indicado y un registro del firewall o del resolver. Prueba por separado el acceso directo desde un dispositivo IoT o de invitados a la dirección de administración del router como caso denegado.

Los dispositivos de **la misma VLAN** podrían intercambiar tráfico sin pasar por el firewall del router. Prueba por separado el aislamiento local de clientes si el punto de acceso lo ofrece y utiliza firewalls de host en los servidores. Las pruebas de firewall entre VLAN no demuestran aislamiento dentro de la misma VLAN.

> **Resultado esperado:** cada dispositivo recibe una dirección de su subred prevista. Los servicios permitidos funcionan. Los intentos denegados coinciden con un bloqueo del firewall o un control equivalente documentado.

## Solución de problemas

- **No hay dirección:** comprueba la VLAN del puerto de acceso o SSID, las etiquetas del troncal, el ámbito DHCP y la interfaz de puerta de enlace.
- **La dirección funciona, pero DNS no:** comprueba la dirección del resolver, la vinculación del servicio en el router y la regla de firewall para DNS.
- **Un dispositivo llega inesperadamente a otra VLAN:** comprueba las reglas del router, las reglas amplias de permiso y si ambos dispositivos aún comparten una red sin etiqueta.
- **No hay registro del firewall para el tráfico enrutado:** comprueba si un switch de capa 3 u otra puerta de enlace enrutó la conexión antes de que llegara al firewall.
- **Una VLAN cuya puerta de enlace está en el switch llega a redes locales, pero no a Internet:** comprueba la ruta predeterminada del switch, las rutas de retorno del router, la política del firewall y el NAT saliente de la subred VLAN.
- **IPv4 está bloqueado, pero la conexión funciona:** comprueba las direcciones IPv6, los anuncios del router, las reglas IPv6 y las entradas de estado existentes.
- **Una prueba denegada agota el tiempo sin un registro del firewall:** confirma que el servicio de destino esté escuchando. Después revisa el enrutamiento y la configuración de registros. La [guía de solución de problemas de firewall de Netgate](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) describe las comprobaciones de registros y estados.
- **El envío a pantalla o el descubrimiento deja de funcionar:** identifica el protocolo de descubrimiento y la ruta del controlador antes de añadir una excepción limitada.

## Pasos siguientes

Guarda el inventario de dispositivos y la matriz de tráfico con el diagrama de red. Revisa las reglas cuando añadas un servidor o dispositivo IoT. Repite una prueba permitida y otra denegada después de cada cambio de red relevante. Consulta [segmentación de redes](/articles/how-to-perform-network-segmentation-for-improved-security/) para ver los principios de diseño más amplios.
