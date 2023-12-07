---
title: "Curso Network Plus: Comprensión del modelo OSI, topologías y tipos de red"
date: 2023-07-01
toc: true
draft: false
description: "Explore la importancia de los fundamentos de las redes, incluido el modelo OSI, las topologías de red y los distintos tipos de redes, para crear infraestructuras eficientes y fiables."
genre: ["Tecnología", "Red", "Infraestructura informática", "Arquitectura de red", "Informática", "Comunicación de datos", "Tecnologías de la información", "Seguridad de las redes", "Gestión de redes", "Internet"]
tags: ["fundamentos de redes", "Modelo OSI", "topologías de red", "tipos de red", "data encapsulation", "capas de red", "topología de malla", "topología en estrella", "topología de bus", "topología de anillo", "topología híbrida", "red de pares", "red cliente-servidor", "LAN", "MAN", "WAN", "WLAN", "PAN", "CAN", "SAN", "SDWAN", "MPLS", "mGRE", "vSwitch", "vNIC", "NFV", "hipervisor", "enlaces por satélite", "DSL", "internet por cable", "línea arrendada", "metro-óptico"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_nodes.png"
coverAlt: "Ilustración simbólica de nodos interconectados que forman una red."
coverCaption: "Liberar el poder de los fundamentos de las redes."
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

Los fundamentos de las redes desempeñan un papel crucial en el mundo interconectado de hoy. Ya se trate de navegar por Internet, enviar correos electrónicos o transmitir vídeos, todas estas actividades dependen de una sólida infraestructura de red. En este artículo, ofreceremos una visión general de los **fundamentos de las redes**, empezando por el **modelo OSI** y los conceptos de **encapsulación**. También exploraremos diferentes **topologías de red** y sus características.

## Visión General del Modelo OSI y Conceptos de Encapsulación

El **modelo OSI (Interconexión de Sistemas Abiertos)** es un marco conceptual que define las funciones de una red en siete capas diferentes. Cada capa tiene responsabilidades específicas e interactúa con las capas por encima y por debajo de ella. Entender el modelo OSI es esencial para comprender cómo se transmiten y procesan los datos a través de una red.

### Capas del Modelo OSI

{{< youtube id="G7aVKgGUe9c" >}}

1. **Capa 1 - Física**: La capa física se ocupa de la transmisión y recepción de flujos de bits en bruto a través de medios físicos como cables de cobre, cables de fibra óptica o conexiones inalámbricas.

2. **Capa 2 - Enlace de datos**: La capa de enlace de datos se encarga de establecer y terminar las conexiones entre los dispositivos de red. También se encarga de la detección y corrección de errores para garantizar una transmisión de datos fiable.

3. **Capa 3 - Red**: La capa de red facilita el encaminamiento de paquetes de datos desde el origen hasta el destino a través de múltiples nodos de red. Se ocupa de los problemas relacionados con la **congestión de la red**, el **enrutamiento de paquetes** y el **direccionamiento IP**.

4. **Capa 4 - Transporte**: La capa de transporte garantiza la **entrega de datos de extremo a extremo** y establece una comunicación fiable entre el origen y el destino. Gestiona la **segmentación de datos**, el **control de flujo** y la **recuperación de errores**.

5. **Capa 5 - Sesión**: La capa de sesión establece, mantiene y finaliza las sesiones de comunicación entre aplicaciones. Gestiona el **control de diálogo** y la **sincronización** entre dispositivos.

6. **Capa 6 - Presentación**: La capa de presentación se centra en la **sintaxis** y la **semántica** de la información intercambiada entre aplicaciones. Se encarga de la **encriptación**, **compresión** y **formateo** de los datos para su correcta interpretación.

7. **Capa 7 - Aplicación**: La capa de aplicación representa las aplicaciones y servicios de red reales utilizados por los usuarios finales. Proporciona servicios como **correo electrónico**, **transferencia de archivos**, **navegación web** y **acceso remoto**.

### Encapsulación y desencapsulación de datos en el contexto del modelo OSI

{{< youtube id="_fPzeQ9PHhA" >}}

La encapsulación de datos es el proceso de añadir cabeceras y remolques específicos del protocolo a la carga útil en cada capa del modelo OSI. Esta encapsulación permite que los datos atraviesen la red y lleguen al destino previsto. Por el contrario, la desencapsulación consiste en eliminar las cabeceras y remolques añadidos en cada capa del modelo OSI para extraer la carga útil original.

En el contexto del modelo OSI, los siguientes elementos contribuyen a la encapsulación y desencapsulación de datos:

- **Cabecera Ethernet**: La cabecera Ethernet contiene información como las direcciones MAC de los dispositivos de origen y destino, el tipo de protocolo Ethernet y mecanismos de comprobación de errores.

- Cabecera del Protocolo de Internet (IP): La cabecera IP incluye las direcciones IP de origen y destino, la identificación del paquete, el tiempo de vida y otros parámetros esenciales para la comunicación basada en IP.

- Cabeceras del Protocolo de Control de Transmisión (TCP)/Protocolo de Datagramas de Usuario (UDP)**: Las cabeceras TCP y UDP contienen números de puerto, números de secuencia, sumas de comprobación y otra información relevante necesaria para la comunicación en la capa de transporte.

- Indicadores TCP**: Las banderas TCP indican funciones de control y opciones específicas durante una sesión TCP. Incluyen indicadores para establecer conexiones, confirmar datos, finalizar conexiones, etc.

- Carga útil**: La carga útil son los datos reales que se transmiten, como una página web, un mensaje de correo electrónico o un archivo multimedia.

- Unidad Máxima de Transmisión (MTU)**: La MTU representa el tamaño máximo de un paquete de datos que puede transmitirse a través de una red sin fragmentación.

## Explorar las topologías de red y sus características

{{< youtube id="zbqrNg4C98U" >}}

Las topologías de red definen la disposición física o lógica de los dispositivos de red y las interconexiones entre ellos. Cada topología tiene sus puntos fuertes y débiles, y elegir la adecuada depende de varios factores, como la escalabilidad, la tolerancia a fallos y el coste.

### Topología de malla

En una topología **mesh**, cada dispositivo está conectado a todos los demás, formando una red totalmente interconectada. Esta redundancia proporciona una alta tolerancia a fallos, pero puede ser costosa y compleja de implementar. Las topologías de malla se utilizan habitualmente en infraestructuras críticas y entornos informáticos de alto rendimiento.

### Topología de estrella/cubo y radios

En una topología en estrella, todos los dispositivos están conectados a un concentrador o conmutador central. El concentrador actúa como punto central de conexión, facilitando la comunicación entre dispositivos. Esta topología es fácil de gestionar y proporciona un control centralizado, pero puede crear un único punto de fallo si falla el concentrador.

### Topología de bus

En una topología de **bus**, todos los dispositivos están conectados a una única línea de comunicación, llamada bus. Los datos se transmiten secuencialmente a lo largo del bus, y los dispositivos reciben los datos destinados a ellos. Las topologías de bus son sencillas y rentables, pero pueden sufrir congestiones en la red y tienen una escalabilidad limitada.

### Topología en anillo

En una topología de **anillo**, los dispositivos están conectados en una cadena circular, en la que cada dispositivo se conecta al siguiente y el último dispositivo se conecta al primero. Los datos circulan en una dirección alrededor del anillo. Las topologías en anillo ofrecen un acceso equitativo y pueden soportar grandes cargas de tráfico, pero pueden sufrir interrupciones en la red si falla un dispositivo.

### Topología híbrida

Una **topología híbrida** combina varias topologías para formar una red más flexible y escalable. Por ejemplo, una combinación de topologías en estrella y en anillo puede proporcionar redundancia y tolerancia a fallos manteniendo la escalabilidad.

## Tipos de red y características

{{< youtube id="6a-roIeJ_a4" >}}

Las redes abarcan varios tipos de redes, cada uno de los cuales responde a necesidades y casos de uso específicos. Estos son algunos de los tipos de red más comunes:

### Red entre iguales (P2P)

En una red **de igual a igual (P2P)**, los dispositivos se conectan directamente entre sí sin depender de un servidor centralizado. Las redes P2P suelen utilizarse para compartir archivos, aplicaciones colaborativas y sistemas descentralizados.

### Red Cliente-Servidor

Una **red cliente-servidor** implica clientes, que solicitan servicios o recursos, y servidores, que proporcionan esos servicios o recursos. Las redes cliente-servidor se utilizan mucho en entornos empresariales, donde el control centralizado y la gestión de recursos son esenciales.

### Red de área local (LAN)

Una **red de área local (LAN)** abarca un área geográfica pequeña, como un edificio de oficinas o un hogar. Permite a los dispositivos de la red comunicarse y compartir recursos. Las LAN se utilizan habitualmente para la comunicación interna, compartir archivos e impresoras.

### Red de área metropolitana (MAN)

Una **red de área metropolitana (MAN)** cubre un área geográfica mayor que una LAN pero menor que una WAN. Conecta múltiples LANs dentro de una ciudad o región metropolitana. Las MAN suelen ser utilizadas por organizaciones que necesitan conectividad de alta velocidad entre sus sucursales o campus.

### Red de área extensa (WAN)

Una **red de área extensa (WAN)** abarca una gran área geográfica, conectando múltiples LANs o MANs a través de diferentes ciudades, países o continentes. Las WAN se basan en diversas tecnologías de comunicación, como líneas alquiladas, satélites y redes ópticas, para transmitir datos a larga distancia.

### Red de área local inalámbrica (WLAN)

Una **red de área local inalámbrica (WLAN)** proporciona conectividad inalámbrica dentro de un área limitada, normalmente utilizando tecnología Wi-Fi. Las WLAN suelen encontrarse en hogares, oficinas, cafeterías y espacios públicos, y permiten a los usuarios conectar sus dispositivos sin cables físicos.

### Red de área personal (PAN)

Una **red de área personal (PAN)** cubre un área pequeña, normalmente dentro del espacio de trabajo de una persona o en su entorno inmediato. Permite la comunicación entre dispositivos personales, como teléfonos inteligentes, tabletas y dispositivos portátiles.

### Red de área de campus (CAN)

Una **red de área de campus (CAN)** es una red que abarca un campus universitario o un gran campus corporativo. Proporciona conectividad a varios edificios e instalaciones dentro del área del campus, facilitando la comunicación y el uso compartido de recursos.

### Red de área de almacenamiento (SAN)

Una **red de área de almacenamiento (SAN)** es una red especializada diseñada con fines de almacenamiento. Permite a varios servidores acceder a recursos de almacenamiento compartidos, como matrices de discos o bibliotecas de cintas, a través de una conexión de alta velocidad.

### Red de área extensa definida por software (SDWAN)

**La red de área extensa definida por software (SDWAN)** es una tecnología que simplifica la gestión y configuración de las WAN al separar el plano de control de la red del hardware subyacente. Proporciona un control centralizado y permite a las organizaciones gestionar dinámicamente su infraestructura WAN.

### Conmutación multiprotocolo de etiquetas (MPLS)

**La conmutación de etiquetas multiprotocolo (MPLS)** es una técnica de enrutamiento que utiliza etiquetas para reenviar eficazmente paquetes de datos a través de una red. Proporciona una comunicación de alto rendimiento, fiable y segura, lo que la hace adecuada para proveedores de servicios y empresas.

### Encapsulación de enrutamiento genérico multipunto (mGRE)

**La encapsulación de enrutamiento genérico multipunto (mGRE)** es una técnica utilizada para crear redes privadas virtuales (VPN) encapsulando paquetes de datos y enviándolos a través de una red multipunto. Permite una comunicación eficaz entre varios sitios o puntos finales.

## Conceptos de red virtual

{{< youtube id="A29g5-Os-u8" >}}

Las tecnologías de virtualización han revolucionado la forma de diseñar y gestionar las redes. He aquí algunos conceptos de red virtual:

### vSwitch

Un **vSwitch**, o conmutador virtual, es un conmutador de red basado en software que opera dentro de un entorno virtualizado, como un hipervisor. Permite la comunicación entre máquinas virtuales (VMs) y las conecta a la red física.

### Tarjeta de Interfaz de Red Virtual (vNIC)

Una **tarjeta de interfaz de red virtual (vNIC)** es una tarjeta de interfaz de red virtualizada que emula un adaptador de red físico dentro de una máquina virtual. Permite a las máquinas virtuales comunicarse con el conmutador virtual y la red física.

### Virtualización de funciones de red (NFV)

**La virtualización de funciones de red (NFV)** es un enfoque que virtualiza funciones de red, como cortafuegos, enrutadores y equilibradores de carga, ejecutándolos en servidores estándar en lugar de dispositivos de hardware dedicados. Ofrece flexibilidad, escalabilidad y ahorro de costes en la infraestructura de red.

### Hipervisor

Un **hipervisor** es una capa de software que permite la creación y gestión de máquinas virtuales. Proporciona abstracción de hardware, permitiendo la ejecución de múltiples máquinas virtuales en un único servidor físico.

## Enlaces de proveedores

{{< youtube id="M2cJtZXJrpE" >}}

Los enlaces de proveedores hacen referencia a los distintos tipos de opciones de conectividad que ofrecen los proveedores de servicios. Estos son algunos de los enlaces de proveedores más comunes:

### Satélite

**Los enlaces por satélite** utilizan satélites de comunicaciones para transmitir datos a larga distancia. Suelen utilizarse en zonas remotas donde otras opciones de conectividad son limitadas.

### Línea de abonado digital (DSL)

**La línea de abonado digital (DSL)** es una tecnología que proporciona acceso a Internet de alta velocidad a través de las líneas telefónicas existentes. Ofrece velocidades más rápidas que las conexiones telefónicas tradicionales y está ampliamente disponible en entornos residenciales y empresariales.

### Cable

**Internet por cable** utiliza los mismos cables coaxiales que la televisión por cable para proporcionar acceso a Internet de alta velocidad. Es popular en zonas residenciales y ofrece velocidades más rápidas que DSL.

### Línea dedicada

Una **línea alquilada** es una conexión dedicada, punto a punto, entre dos ubicaciones. Proporciona una conectividad fiable y segura, por lo que es adecuada para empresas con grandes necesidades de ancho de banda.

### Metroóptica

**Las redes metro-ópticas** utilizan tecnología de fibra óptica para proporcionar conectividad de alta velocidad dentro de un área metropolitana. Ofrecen un gran ancho de banda y baja latencia, ideales para aplicaciones con gran volumen de datos.

______

En conclusión, comprender los fundamentos de las redes es crucial para construir y mantener infraestructuras de red fiables y eficientes. El **modelo OSI** proporciona un marco para comprender cómo se transmiten y procesan los datos a través de las diferentes capas de la red. Además, el conocimiento de las **topologías de red** ayuda a diseñar redes que cumplan requisitos específicos de escalabilidad, tolerancia a fallos y rentabilidad. Si nos familiarizamos con los distintos **tipos de red**, los **conceptos de red virtual** y los **enlaces de proveedor**, podremos tomar decisiones fundamentadas a la hora de configurar y gestionar redes.

Referencias:
- [OSI Model - Cisco](https://learningnetwork.cisco.com/s/article/osi-model-reference-chart)
- [How Does the Internet Work? - Stanford University](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
