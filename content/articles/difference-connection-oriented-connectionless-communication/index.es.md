---
title: "Comunicación orientada a conexión y sin conexión"
date: 2023-07-02
lastmod: 2026-11-11
toc: true
draft: false
description: "Conoce las diferencias entre la comunicación orientada a conexión y la comunicación sin conexión, sus protocolos, servicios y métodos de enrutamiento."
genre: ["Tecnología", "Redes", "Comunicación", "Protocolos", "Informática", "Transmisión de datos", "Infraestructura de red", "Internet", "Tecnologías de la información", "Telecomunicaciones"]
tags: ["orientada a conexión", "sin conexión", "comunicación", "protocolos", "servicios", "redes", "transmisión de datos", "TCP", "UDP", "métodos de enrutamiento", "fiabilidad", "eficiencia", "control de flujo", "recuperación de errores", "latencia", "TCP/IP", "infraestructura de red", "protocolos de Internet", "protocolos de red", "aplicaciones en tiempo real", "fiabilidad de red", "eficiencia de red", "entrega de datos", "latencia de red", "simplicidad de red", "sobrecarga de red", "gestión de errores de red", "control de congestión de red", "enrutamiento de red"]
cover: "/img/cover/An_illustration_showing_two_devices_connected.webp"
coverAlt: "Ilustración de dos dispositivos conectados mediante una conexión fiable y ordenada."
coverCaption: "Comunicación fiable y ordenada: entiende la diferencia"
---

## Introducción

En las redes se usan dos enfoques habituales: la comunicación orientada a conexión y la comunicación sin conexión. Se diferencian en cómo establecen y mantienen la comunicación entre dispositivos. Este artículo explica sus diferencias principales, protocolos, servicios y métodos de enrutamiento.

## Comunicación orientada a conexión

La comunicación orientada a conexión establece un enlace dedicado entre el emisor y el receptor antes de transmitir datos. El enlace permanece activo durante toda la sesión. Un ejemplo conocido de protocolo orientado a conexión es el **Protocolo de control de transmisión (TCP)**.

### Cómo funciona la comunicación orientada a conexión

Antes de transferir datos, el emisor y el receptor intercambian información de control para establecer la conexión. Esta información incluye las direcciones de origen y destino, los mecanismos de comprobación de errores y los datos de secuenciación.

Una vez establecida la conexión, los datos se transmiten de forma fiable y ordenada. TCP garantiza que los paquetes lleguen a su destino sin pérdidas ni daños y en el orden correcto. Este enfoque ofrece funciones como control de flujo, control de congestión y recuperación de errores, que ayudan a entregar los datos de forma fiable.

### Ventajas de la comunicación orientada a conexión

La comunicación orientada a conexión ofrece varias ventajas:

1. **Fiabilidad**: garantiza la entrega fiable de datos mediante una transmisión sin errores y ordenada.

2. **Recuperación de errores**: TCP detecta y recupera errores de red para mantener la integridad de los datos.

3. **Control de flujo**: los protocolos orientados a conexión evitan saturar al receptor con datos.

4. **Secuenciación**: se conserva el orden de transmisión para que el receptor obtenga los datos en la secuencia correcta.

5. **Control de congestión**: TCP ajusta la velocidad de transmisión para evitar la congestión y mantener estable la red.

## Comunicación sin conexión

A diferencia de la comunicación orientada a conexión, la comunicación sin conexión no establece un enlace dedicado antes de transmitir datos. Cada paquete se trata como una unidad independiente y se enruta por separado. Un protocolo conocido de este tipo es el **Protocolo de datagramas de usuario (UDP)**.

### Cómo funciona la comunicación sin conexión

Los paquetes se envían a la red sin configuración previa ni acuse de recibo. Cada paquete contiene la información necesaria, incluidas las direcciones de origen y destino, para enrutarlo y entregarlo de forma independiente. Al no tener el coste de establecer ni mantener una conexión, este enfoque suele ser más rápido, pero menos fiable que el orientado a conexión.

### Ventajas de la comunicación sin conexión

La comunicación sin conexión ofrece algunas ventajas:

1. **Eficiencia**: al evitar el coste de establecer y mantener conexiones, se usan con más eficiencia los recursos de red y el procesamiento.

2. **Menor latencia**: al no requerir el establecimiento de una conexión, reduce la latencia. Es adecuada para aplicaciones en tiempo real, como el vídeo en streaming y los juegos en línea.

3. **Simplicidad**: la ausencia de configuración y mantenimiento de conexiones simplifica la comunicación y reduce su complejidad.

## Comparación de las dos formas de comunicación

Estas son las diferencias principales entre la comunicación orientada a conexión y la comunicación sin conexión:

| | Comunicación orientada a conexión | Comunicación sin conexión |
|--------------------|----------------------------------------|---------------------------------------|
| Establecimiento | Requiere una fase de establecimiento | No requiere establecer una conexión |
| Fiabilidad | Transmisión fiable de datos | No se garantiza la transmisión |
| Orden | Los paquetes llegan en orden | Los paquetes pueden llegar desordenados |
| Coste | Mayor coste por la configuración | Menor coste al no haber conexión |
| Gestión de errores | Incluye mecanismos de recuperación | No incluye mecanismos de recuperación |
| Aplicaciones | Adecuada para aplicaciones que requieren | Adecuada para aplicaciones en tiempo real |
| | entrega fiable y ordenada de datos | con menor latencia |

## Enrutamiento con y sin conexión

El tipo de comunicación también afecta al enrutamiento de la red. El enrutamiento selecciona una ruta adecuada para transmitir datos desde el origen hasta el destino.

En el enrutamiento orientado a conexión, la infraestructura de red establece una ruta predeterminada al crear la conexión. La ruta no cambia durante la sesión. El enrutamiento sin conexión no necesita una ruta predeterminada. Cada paquete se enruta por separado según las condiciones actuales de la red y las rutas disponibles.

## Conclusión

La diferencia principal es si se establece un enlace dedicado antes de transmitir datos. La comunicación orientada a conexión, como TCP, ofrece fiabilidad, recuperación de errores, control de flujo, secuenciación y control de congestión. La comunicación sin conexión, como UDP, ofrece eficiencia, menor latencia y simplicidad. Elige según las necesidades de la aplicación. Usa el enfoque orientado a conexión cuando necesites una entrega fiable y ordenada. Elige el enfoque sin conexión para aplicaciones en tiempo real que necesiten menos latencia.

______

## Referencias

1. [Protocolo de control de transmisión (TCP) - Grupo de Trabajo de Ingeniería de Internet (IETF)](https://tools.ietf.org/html/rfc793)
2. [Protocolo de datagramas de usuario (UDP) - Grupo de Trabajo de Ingeniería de Internet (IETF)](https://tools.ietf.org/html/rfc768)
3. [Arquitectura de la información - Interaction Design Foundation](https://www.interaction-design.org/literature/topics/information-architecture)
4. [Instituto Nacional de Estándares y Tecnología (NIST) - Centro de Recursos de Seguridad Informática](https://csrc.nist.gov/)
5. [Grupo de Trabajo de Ingeniería de Internet (IETF) - Normas y protocolos](https://www.ietf.org/standards/)
______
