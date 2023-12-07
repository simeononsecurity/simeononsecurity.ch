---
title: "Curso Network Plus: Protocolos de enrutamiento, conceptos y optimización"
date: 2023-07-07
toc: true
draft: false
description: "Explore el mundo de las tecnologías y conceptos de enrutamiento, desde protocolos de enrutamiento dinámico como RIP, OSPF, EIGRP y BGP hasta protocolos de estado de enlace, vector distancia y enrutamiento híbrido, así como la configuración de enrutamiento estático y rutas por defecto."
genre: ["Tecnología", "Red", "Enrutamiento", "Protocolos de red", "Gestión de redes", "Enrutamiento dinámico", "Enrutamiento estático", "Gestión del ancho de banda", "Calidad del servicio", "Dispositivos de red"]
tags: ["tecnologías de enrutamiento", "protocolos de enrutamiento dinámico", "RIP", "OSPF", "EIGRP", "BGP", "estado del enlace", "vector distancia", "protocolos de encaminamiento híbridos", "enrutamiento estático", "rutas por defecto", "distancia administrativa", "ruta exterior", "enrutamiento interior", "tiempo de vivir", "gestión del ancho de banda", "moldeado del tráfico", "calidad del servicio", "dispositivos de red", "routers", "interruptores", "cortafuegos", "balanceadores de carga", "puntos de acceso", "optimización de la red", "rendimiento de la red", "seguridad de la red", "arquitectura de red", "tráfico de red"]
cover: "/img/cover/An_illustration_of_interconnected_network_devi.png"
coverAlt: "Ilustración de dispositivos de red interconectados con flujo de datos entre ellos."
coverCaption: "Navegando por la autopista digital: Optimizar el enrutamiento de red para obtener el máximo rendimiento"
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Introducción

En el mundo interconectado de hoy en día, el enrutamiento eficiente de la red es esencial para una transmisión y comunicación de datos sin problemas. Las tecnologías y conceptos de enrutamiento desempeñan un papel crucial a la hora de dirigir el tráfico de red y optimizar su rendimiento. Este artículo explora varios protocolos de enrutamiento, como RIP, OSPF, EIGRP y BGP, junto con protocolos de estado de enlace, vector distancia y enrutamiento híbrido. También profundizaremos en la configuración y el uso del enrutamiento estático y las rutas por defecto. Además, compararemos y contrastaremos diferentes dispositivos y su ubicación en la red.

{{< youtube id="YRzr56cwgCg" >}}

## Protocolos de enrutamiento dinámico

Los protocolos de enrutamiento dinámico están diseñados para automatizar el proceso de intercambio de información de enrutamiento entre routers. Se adaptan a los cambios en la red, como modificaciones en la topología o fallos en los enlaces, actualizando dinámicamente las tablas de enrutamiento. Veamos algunos de los protocolos de enrutamiento dinámico más utilizados:

### Protocolo de enrutamiento de Internet (RIP)

El Routing Internet Protocol (RIP) es un protocolo de enrutamiento vector distancia que funciona en base al número de saltos entre routers. Utiliza la métrica de recuento de saltos para determinar la mejor ruta hacia una red de destino. RIP es compatible con IPv4 e IPv6 y es adecuado para redes pequeñas y medianas.

### Abrir primero el camino más corto (OSPF)

Open Shortest Path First (OSPF) es un protocolo de enrutamiento de estado de enlace que calcula la ruta más corta a un destino utilizando el algoritmo de Dijkstra. Tiene en cuenta varias métricas, como el ancho de banda, el retardo y la fiabilidad, para determinar la ruta óptima. OSPF se utiliza ampliamente en redes de grandes empresas debido a su escalabilidad y rápida convergencia.

### Protocolo de Enrutamiento de Pasarela Interior Mejorado (EIGRP)

Enhanced Interior Gateway Routing Protocol (EIGRP) es un protocolo de enrutamiento híbrido desarrollado por Cisco. Combina las mejores características de los protocolos de vector distancia y de estado de enlace. EIGRP utiliza el algoritmo de actualización difusa (DUAL) para calcular las rutas y ofrece funciones avanzadas como el equilibrio de carga de coste desigual y el resumen de rutas.

### Protocolo de Pasarela Fronteriza (BGP)

Border Gateway Protocol (BGP) es un protocolo de pasarela exterior utilizado para el enrutamiento entre sistemas autónomos (AS) en Internet. BGP es altamente escalable y permite a los sistemas autónomos intercambiar información de enrutamiento. Utiliza atributos y políticas de ruta para tomar decisiones de enrutamiento basadas en factores como políticas de red, longitud de ruta y ruta AS.

## Protocolos de estado de enlace, vector distancia y enrutamiento híbrido

Los protocolos de enrutamiento se pueden clasificar en estado de enlace, vector distancia e híbridos en función de su funcionamiento y de la información que utilizan para determinar las rutas.

### Protocolos de enrutamiento de estado de enlace

Los protocolos de enrutamiento de estado de enlace, como OSPF, mantienen un mapa detallado de toda la red mediante el intercambio de información de estado de enlace entre routers. Cada router construye una base de datos topológica que le permite calcular la mejor ruta hacia una red de destino en función de varias métricas.

### Protocolos de enrutamiento vector distancia

Los protocolos de enrutamiento vectorial de distancia, como RIP, utilizan una métrica simple (como el recuento de saltos) e intercambian información de enrutamiento con los routers vecinos. Los routers anuncian periódicamente sus tablas de enrutamiento a los routers vecinos, lo que les permite hacerse una idea de la red. Los protocolos de vector distancia tienen un conocimiento limitado de la red global y pueden ser propensos a los bucles de enrutamiento.

### Protocolos de enrutamiento híbridos

Los protocolos de enrutamiento híbridos, como EIGRP, combinan las características de los protocolos de estado de enlace y vector distancia. Mantienen una tabla de topología similar a la de los protocolos de estado de enlace, pero utilizan algoritmos de vector distancia para calcular las rutas. Los protocolos híbridos ofrecen las ventajas de una convergencia más rápida y una sobrecarga reducida.

## Enrutamiento estático y rutas por defecto

El enrutamiento estático implica la configuración manual de la tabla de enrutamiento en los routers, especificando las rutas para llegar a redes específicas. Se suele utilizar en escenarios en los que los cambios en la topología de la red son mínimos o predecibles. Las rutas estáticas son fáciles de configurar y pueden ser útiles para redes pequeñas o segmentos de red específicos.

Una ruta por defecto, también conocida como pasarela de último recurso, se utiliza cuando no existe una ruta explícita para una red de destino. Actúa como ruta comodín y se configura en los routers para dirigir el tráfico a una pasarela por defecto cuando el router no conoce la red de destino.

## Distancia Administrativa, Exterior vs. Interior, y Tiempo de Vida

{{< youtube id="HR59xk4umWY" >}}

### Distancia administrativa

La distancia administrativa (AD) es un valor asignado a los protocolos de enrutamiento para determinar la prioridad de las rutas cuando se ejecutan varios protocolos en un enrutador. Los valores más bajos de distancia administrativa indican una mayor prioridad para un protocolo de enrutamiento en particular. Por ejemplo, OSPF tiene una AD menor (110) que RIP (120), por lo que las rutas OSPF tendrán preferencia sobre las rutas RIP.

### Enrutamiento Exterior vs. Enrutamiento Interior

Los protocolos de enrutamiento exterior, como BGP, se utilizan para intercambiar información de enrutamiento entre sistemas autónomos (AS). Se encargan del encaminamiento entre distintas organizaciones y proveedores de servicios. Por otro lado, los protocolos de enrutamiento interior, como RIP, OSPF y EIGRP, se utilizan para el enrutamiento dentro de un sistema autónomo.

### Tiempo de vida (TTL)

Time to Live (TTL) es un campo en los paquetes IP que especifica el número máximo de saltos que un paquete puede recorrer antes de ser descartado. Evita que los paquetes circulen indefinidamente por la red si hay un bucle de enrutamiento u otros problemas. Cada router disminuye el valor TTL a medida que el paquete atraviesa la red.

## Gestión del ancho de banda

Una gestión eficiente del ancho de banda es crucial para optimizar el rendimiento de la red y asegurar un flujo fluido del tráfico. Dos aspectos importantes de la gestión del ancho de banda son la conformación del tráfico y la calidad del servicio (QoS).

### Conformación del tráfico

La conformación del tráfico es una técnica utilizada para controlar la velocidad de transmisión de datos en una red. Permite a los administradores de red dar forma al flujo de tráfico definiendo límites de ancho de banda y priorizando ciertos tipos de tráfico. Esto ayuda a evitar la congestión de la red y garantiza que las aplicaciones críticas reciban suficiente ancho de banda.

### Calidad de servicio (QoS)

La calidad de servicio (QoS) se refiere a la capacidad de una red para priorizar y asignar recursos a diferentes tipos de tráfico en función de su importancia y requisitos. Los mecanismos de QoS, como la priorización del tráfico, la asignación de ancho de banda y la gestión de la congestión, ayudan a garantizar un rendimiento óptimo para aplicaciones en tiempo real como voz y vídeo.

## Comparación y colocación de dispositivos

Los distintos dispositivos desempeñan funciones específicas en una red y tienen características diversas que los hacen adecuados para tareas concretas. Comparemos y contrastemos algunos dispositivos de red comunes y analicemos su ubicación adecuada:

- Enrutadores**: Los routers se encargan de dirigir el tráfico entre diferentes redes. Funcionan en la capa de red (Capa 3) y utilizan protocolos de encaminamiento para determinar la mejor ruta para la transmisión de datos.

- Conmutadores**: Los conmutadores operan en la capa de enlace de datos (Capa 2) y facilitan la comunicación entre dispositivos dentro de una red de área local (LAN). Utilizan las direcciones MAC para reenviar los paquetes de datos a su destinatario.

- Cortafuegos**: Los cortafuegos protegen las redes de accesos no autorizados y tráfico malicioso. Aplican políticas de seguridad inspeccionando el tráfico de red y permitiendo o bloqueando conexiones específicas basándose en reglas predefinidas.

- Equilibradores de carga**: Los equilibradores de carga distribuyen el tráfico de red entrante entre varios servidores para optimizar la utilización de los recursos, mejorar el rendimiento y garantizar una alta disponibilidad.

- Puntos de acceso**: Los puntos de acceso (AP) proporcionan conectividad inalámbrica a los dispositivos de una red. Permiten la comunicación inalámbrica mediante la transmisión y recepción de datos entre los dispositivos inalámbricos y la red cableada.

La ubicación de estos dispositivos depende de la arquitectura y los requisitos de la red. **Los enrutadores** suelen situarse en el perímetro de la red para gestionar el tráfico entre redes. **Los conmutadores** se instalan dentro de las LAN para conectar dispositivos y facilitar la comunicación local. **Los cortafuegos** se colocan entre las redes para protegerlas de amenazas externas. **Los equilibradores de carga** se colocan delante de los servidores web para distribuir el tráfico de forma eficiente. **Los puntos de acceso** se colocan estratégicamente para proporcionar cobertura inalámbrica en las zonas deseadas.

______

## Conclusión

Comprender las **tecnologías y conceptos de enrutamiento** es crucial para los administradores de red y profesionales de TI. **Los protocolos de enrutamiento dinámico** como **RIP, OSPF, EIGRP y BGP** automatizan el proceso de intercambio de información de enrutamiento y se adaptan a los cambios de la red. **Los protocolos de enrutamiento de estado de enlace, vector distancia e híbridos** ofrecen distintos enfoques para determinar las rutas óptimas. **El enrutamiento estático y las rutas por defecto** proporcionan un control manual sobre las decisiones de enrutamiento. Las técnicas de **gestión del ancho de banda**, como la **formación del tráfico y la QoS**, garantizan una utilización eficaz de la red. Comparar y colocar adecuadamente los dispositivos de red mejora el rendimiento y la seguridad de la red.

Al dominar las **tecnologías y conceptos de enrutamiento**, los administradores de red pueden construir **redes robustas y eficientes** que satisfagan las exigencias de la conectividad moderna.

______