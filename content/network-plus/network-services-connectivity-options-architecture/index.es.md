---
title: "Curso Network Plus: Exploración de servicios de red, opciones de conectividad y arquitectura"
date: 2023-07-04
toc: true
draft: false
description: "Descubra las funcionalidades de los servicios DHCP, DNS y NTP, comprenda la arquitectura de redes corporativas y de centros de datos, y explore los conceptos de nube y las opciones de conectividad para una comunicación y gestión de datos sin fisuras."
genre: ["Tecnología", "Red", "Conectividad", "Intercambio de datos", "Arquitectura de red", "Computación en nube", "Servicios de red", "DNS", "DHCP", "NTP"]
tags: ["servicios de red", "opciones de conectividad", "arquitectura", "DHCP", "DNS", "NTP", "red corporativa", "red de centros de datos", "conceptos de nube", "conectividad", "arquitectura de tres niveles", "redes definidas por software", "arquitectura de la columna vertebral y de las hojas", "flujos de tráfico", "sucursal", "centro de datos local", "colocación", "redes de área de almacenamiento", "Canal de fibra sobre Ethernet", "iSCSI", "explorando DHCP", "Comprender el DNS", "sincronización horaria en red", "arquitectura de redes corporativas", "opciones de conectividad en la nube", "arquitectura de red de tres niveles", "ventajas de las redes definidas por software", "arquitectura de la red troncal y de la red de hojas", "conectividad en la nube para sucursales", "tipos de redes de área de almacenamiento"]
cover: "/img/cover/A_cartoon_illustration_showcasing_various_networks.png"
coverAlt: "Una ilustración de dibujos animados que muestra varios componentes de red y opciones de conectividad en la nube"
coverCaption: "Libere el poder de los servicios de red y la conectividad en la nube"
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Introducción

En el mundo de las redes, varios servicios, opciones de conectividad y marcos arquitectónicos desempeñan un papel crucial en el establecimiento de una comunicación eficiente y fiable. Este artículo explorará tres servicios de red esenciales, a saber, el Protocolo de Configuración Dinámica de Host (DHCP), el Sistema de Nombres de Dominio (DNS) y el Protocolo de Tiempo de Red (NTP). Profundizaremos en sus funcionalidades, hablaremos de la arquitectura básica de redes corporativas y de centros de datos, y ofreceremos una visión general de los conceptos de nube y las opciones de conectividad.

## DHCP: Simplificando la configuración de red

{{< youtube id="e6-TaH5bkjo" >}}

**Dynamic Host Configuration Protocol (DHCP)** es un servicio de red que automatiza la asignación de direcciones IP y parámetros de configuración de red a los dispositivos conectados a una red. Al asignar dinámicamente direcciones IP, DHCP simplifica el proceso de configuración de la red, especialmente en entornos a gran escala.

### Ámbito y Rangos de Exclusión

Un ámbito DHCP define un rango de direcciones IP que pueden ser asignadas a dispositivos. Dentro de un ámbito, se pueden definir rangos de exclusión para reservar direcciones IP específicas para asignación estática o evitar que sean asignadas a dispositivos dinámicamente.

### Reserva y Asignación Dinámica

DHCP permite la reserva de direcciones IP específicas para dispositivos que requieren asignación estática. Esto garantiza que los dispositivos críticos, como servidores o impresoras de red, reciban siempre la misma dirección IP.

Por otro lado, la asignación dinámica consiste en asignar las direcciones IP disponibles del ámbito DHCP a los dispositivos que solicitan conectividad de red. La asignación dinámica es útil para dispositivos que no requieren una dirección IP fija.

### Tiempo de Arrendamiento y Opciones de Ámbito

Cuando un dispositivo obtiene una dirección IP de un servidor DHCP, lo hace por un periodo específico llamado tiempo de arrendamiento. Los tiempos de arrendamiento se pueden personalizar para satisfacer los requisitos del entorno de red. Además, las opciones de alcance de DHCP pueden configurarse para proporcionar parámetros adicionales, como direcciones de servidor DNS y pasarelas predeterminadas, a los dispositivos.

### Relevo DHCP y Ayudante IP/Remisión UPD

En redes más grandes, los agentes de retransmisión DHCP o las direcciones IP helper se utilizan para reenviar peticiones y respuestas DHCP entre clientes y servidores DHCP ubicados en diferentes subredes. Esto permite centralizar los servicios DHCP y proporciona una asignación eficiente de direcciones IP a través de múltiples segmentos de red.

{{< inarticle-dark >}}

## DNS: Traducción de nombres a direcciones IP

{{< youtube id="mpQZVYPuDGU" >}}

**El Sistema de Nombres de Dominio (DNS)** es un servicio de red crítico que traduce nombres de dominio legibles por humanos en sus correspondientes direcciones IP, permitiendo a los dispositivos localizarse y comunicarse entre sí a través de Internet y otras redes.

### Tipos de registro y jerarquía global

DNS utiliza varios tipos de registros para gestionar diferentes tipos de información. Estos incluyen:

- Dirección (A)**: Asigna un nombre de dominio a una dirección IPv4.
- **AAAA**: Asigna un nombre de dominio a una dirección IPv6.
- Nombre canónico (CNAME)**: Proporciona un alias o nombre alternativo para un nombre de dominio existente.
- Intercambio de correo (MX)**: Especifica el servidor de correo responsable de aceptar mensajes de correo electrónico para un dominio.
- Inicio de autoridad (SOA)**: Contiene información administrativa sobre una zona DNS.
- Puntero (PTR)**: Realiza una búsqueda DNS inversa, asignando una dirección IP a un nombre de dominio.
- Texto (TXT)**: Almacena datos de texto arbitrarios asociados a un dominio.
- Servicio (SRV)**: Define la ubicación de servicios específicos dentro de un dominio.
- Servidor de nombres (NS)**: Indica los servidores DNS autoritativos de un dominio.

Estos registros se organizan en una jerarquía global, empezando por los servidores DNS raíz, que almacenan información sobre los dominios de primer nivel (por ejemplo, .com, .org). Esta estructura jerárquica permite una resolución eficaz y descentralizada de los nombres de dominio.

### DNS Interno vs. Externo y Transferencias de Zona

El DNS puede clasificarse en DNS interno y DNS externo. El DNS interno gestiona la resolución de nombres dentro de la red privada de una organización, mientras que el DNS externo gestiona la resolución para dominios de acceso público.

Las transferencias de zona son mecanismos utilizados para replicar los datos de zona DNS entre servidores de nombres autorizados. Estas transferencias aseguran una información consistente y actualizada a través de múltiples servidores DNS.

### Almacenamiento en caché DNS y tiempo de vida (TTL)

El almacenamiento en caché de DNS mejora el rendimiento almacenando mapeos de nombres de dominio y direcciones IP resueltos recientemente. Las cachés pueden existir en servidores DNS, routers e incluso dispositivos individuales. El valor de tiempo de vida (TTL) asociado a los registros DNS determina cuánto tiempo permanece válida la información almacenada en caché antes de que sea necesario actualizarla desde los servidores DNS autorizados.

### DNS inverso y búsqueda recursiva

El DNS inverso, también conocido como búsqueda inversa, es el proceso de resolver una dirección IP a su correspondiente nombre de dominio. La búsqueda recursiva se refiere al proceso de consulta DNS en el que un resolutor DNS atraviesa la jerarquía DNS para obtener la dirección IP asociada a un nombre de dominio dado.

## NTP: Sincronización de la hora de red

**El Protocolo de Tiempo de Red (NTP)** es un protocolo de red que asegura la sincronización precisa del tiempo a través de dispositivos y redes. El mantenimiento preciso de la hora es vital para numerosas funciones de red, incluyendo autenticación, registro y coordinación entre sistemas.

### Estrato y Fuentes de Tiempo

NTP opera basado en un modelo jerárquico llamado estrato. El estrato 0 representa la fuente de tiempo más precisa, normalmente proporcionada por relojes atómicos o sistemas basados en satélites. Los servidores de estrato 1 sincronizan su hora con fuentes de estrato 0, y así sucesivamente.

### Clientes y servidores

En una infraestructura NTP, los clientes consultan a los servidores NTP para obtener información horaria precisa. Los servidores NTP mantienen referencias horarias precisas y proporcionan servicios de sincronización a los clientes.

{{< inarticle-dark >}}

## Arquitectura de redes corporativas y de centros de datos

{{< youtube id="23H0nA-_4YE" >}}

Para garantizar operaciones de red eficientes y escalables, las organizaciones suelen implantar marcos arquitectónicos específicos. Dos arquitecturas de red comúnmente utilizadas son la arquitectura de tres niveles y la arquitectura de columna vertebral y hoja.

### Arquitectura de tres niveles

La arquitectura de tres niveles comprende las siguientes capas:

1. **Núcleo**: La capa de núcleo proporciona conectividad de alta velocidad entre las diferentes partes de la red y sirve de columna vertebral para la transmisión de datos.
2. 2. **Capa de distribución/agregación**: La capa de distribución agrega conexiones desde los conmutadores de la capa de acceso y proporciona funciones de aplicación de políticas, filtrado y seguridad.
3. **Acceso/Extremo**: La capa de acceso conecta dispositivos de usuario final, como ordenadores y teléfonos IP, a la red.

Esta arquitectura proporciona escalabilidad, tolerancia a fallos y segmentación lógica de los servicios de red.

### Redes definidas por software

Las redes definidas por software (SDN) son un enfoque arquitectónico que separa el plano de control, responsable de la toma de decisiones en la red, del plano de datos, responsable del reenvío de datos. SDN consta de las siguientes capas:

1. **Capa de aplicación**: Esta capa incluye las aplicaciones y servicios de red que interactúan con el controlador SDN.
2. **Capa de control**: La capa de control está formada por el controlador SDN, que gestiona las políticas y la configuración de la red.
3. **Capa de infraestructura La capa de infraestructura está formada por los conmutadores y enrutadores de red que reenvían los paquetes de datos siguiendo las instrucciones del controlador SDN.
4. **Plano de gestión**: El plano de gestión se encarga de las tareas de gestión de la red, como la supervisión, el aprovisionamiento y la seguridad.

SDN ofrece flexibilidad, gestión centralizada y programabilidad, lo que permite a las organizaciones adaptar su infraestructura de red a las necesidades cambiantes.

### Arquitectura de columna y hoja

La arquitectura de columna vertebral y hoja es una solución escalable y de gran ancho de banda para redes de centros de datos. Consta de los siguientes componentes:

- Red definida por software**: La arquitectura de columna vertebral y hoja suele aprovechar los principios de SDN para el control centralizado y la programabilidad.
- Conmutación en la parte superior del rack**: Cada bastidor del centro de datos está conectado a un conmutador en la parte superior del bastidor, que proporciona conectividad a los servidores y otros dispositivos.
- Cableado troncal**: La capa troncal está formada por conmutadores de alta velocidad que interconectan todos los conmutadores de hoja.
- Flujos de tráfico En la arquitectura spine y leaf, los flujos de tráfico se producen tanto de norte a sur (entre el centro de datos y las redes externas) como de este a oeste (entre servidores dentro del centro de datos).

Esta arquitectura ofrece mayor rendimiento, escalabilidad y tolerancia a fallos para entornos de centros de datos.

## Conceptos de nube y opciones de conectividad

La computación en nube ha revolucionado la forma en que las organizaciones almacenan, procesan y acceden a datos y aplicaciones. Comprender los conceptos de nube y las opciones de conectividad es crucial para aprovechar las ventajas de los servicios en la nube.

### Sucursal vs. Centro de datos local vs. Colocación

{{< youtube id="-V2NJCS6qSE" >}}

Al considerar la conectividad en la nube, las organizaciones deben elegir entre varias opciones de despliegue, como:

- Sucursales**: Las sucursales suelen conectarse a la nube a través de conexiones de red dedicadas, como MPLS o túneles VPN.
- Centro de datos local**: Los centros de datos locales pueden establecer conexiones directas con los proveedores de servicios en la nube, lo que permite una conectividad segura y de baja latencia.
- Ubicación**: Las organizaciones que colocan su infraestructura en centros de datos de terceros pueden aprovechar las opciones de conectividad del centro de datos, como las conexiones cruzadas directas con los proveedores de nube.

Cada opción de despliegue tiene sus propias consideraciones en cuanto a diseño de red, seguridad y rendimiento.

### Redes de área de almacenamiento

{{< youtube id="prkPpAPm4lA" >}}

Las redes de área de almacenamiento (SAN) proporcionan conectividad de almacenamiento de alto rendimiento a través de redes dedicadas. Las SAN admiten varios tipos de conexión, entre ellos:

- Canal de fibra sobre Ethernet (FCoE)**: FCoE permite el transporte de tráfico de almacenamiento Fibre Channel a través de redes Ethernet, reduciendo la necesidad de redes específicas de almacenamiento separadas.
- Canal de fibra**: Fibre Channel es un protocolo de almacenamiento de alta velocidad que facilita transferencias de datos rápidas y fiables entre servidores y dispositivos de almacenamiento.
- **Internet Small Computer Systems Interface (iSCSI)**: iSCSI permite el acceso al almacenamiento en bloque a través de redes IP, lo que lo convierte en una alternativa asequible y flexible al Canal de Fibra.

Las SAN son fundamentales para las aplicaciones que requieren un acceso de alta velocidad y baja latencia a los recursos de almacenamiento.

## Conclusión

Los servicios de red, las opciones de conectividad y los marcos arquitectónicos constituyen la base de la comunicación y el intercambio de datos modernos. DHCP simplifica la configuración de la red, DNS traduce los nombres de dominio en direcciones IP y NTP garantiza una sincronización horaria precisa. La comprensión de la arquitectura de redes corporativas y de centros de datos, como la arquitectura de tres niveles y la arquitectura de columna vertebral y hoja, ayuda a diseñar redes escalables y eficientes. Además, familiarizarse con los conceptos de la nube y las opciones de conectividad permite a las organizaciones tomar decisiones informadas sobre el aprovechamiento de los servicios en la nube. Al comprender estos conceptos fundamentales, los administradores de red pueden crear infraestructuras de red sólidas y fiables que satisfagan las necesidades cambiantes de las empresas.

## Referencias

- DHCP: [https://www.ietf.org/rfc/rfc2131.txt](https://www.ietf.org/rfc/rfc2131.txt)
- DNS: [https://www.ietf.org/rfc/rfc1035.txt](https://www.ietf.org/rfc/rfc1035.txt)
- NTP: [https://www.ietf.org/rfc/rfc958.txt](https://www.ietf.org/rfc/rfc958.txt)
- Conceptos de nube: [https://aws.amazon.com/what-is-cloud-computing/](https://aws.amazon.com/what-is-cloud-computing/)
