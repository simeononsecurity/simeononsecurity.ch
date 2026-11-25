---
title: "Meshtastic vs. MeshCore vs. Reticulum"
date: 2026-09-01
lastmod: 2026-11-25
toc: true
draft: false
description: "Compara Meshtastic, MeshCore y Reticulum según el enrutamiento, el tiempo de transmisión, la infraestructura, el transporte y los usos sin conexión a internet."
genre: ["LoRa", "Redes malladas", "Comunicaciones sin conexión", "Comunicaciones de emergencia", "Radioafición", "Código abierto", "Preparación ante desastres", "Redes inalámbricas", "Privacidad", "Redes"]
tags: ["meshtastic vs meshcore vs reticulum", "red Reticulum", "meshtastic", "meshcore", "reticulum", "lxmf", "red mallada LoRa", "comunicaciones sin conexión", "rnode", "radio por paquetes", "redes independientes del transporte", "redes malladas", "comunicaciones de emergencia", "red comunitaria mallada", "tiempo de transmisión LoRa", "inundación gestionada", "límite de saltos", "nodo repetidor", "servidor de sala", "aplicación Sideband", "nomadnet", "meshchat", "comunicaciones en desastres", "radio sin conexión", "protocolo de red mallada", "red mallada regional", "ingeniería de RF"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Ilustración que compara tres sistemas de redes malladas con nodos, antenas y líneas de conexión sobre un fondo oscuro con colores vivos para representar sus funciones distintivas."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## La respuesta breve

**Estos tres proyectos no resuelven el mismo problema.** Meshtastic y MeshCore son sistemas de redes malladas LoRa con distintas filosofías de enrutamiento. Reticulum abarca más. Es una capa de red independiente del transporte que funciona a la vez sobre LoRa, radio por paquetes, Wi-Fi, Ethernet, enlaces serie e internet.

**La pregunta adecuada no es «cuál es mejor».** Es «qué arquitectura se adapta a la red que quiero construir».

*Meshtastic encaja con redes ad hoc y usuarios itinerantes.* **MeshCore encaja con una infraestructura fija construida de forma deliberada.** **Reticulum encaja con redes que necesitan unir distintos transportes o conectar redes que de otro modo estarían separadas.** La mayoría de quienes construyen una red LoRa regional solo necesitan una de las dos primeras opciones.

______

## Define la red que vas a construir

Antes de comparar protocolos, anota qué debe hacer la red. Un objetivo útil para la mayoría de las implementaciones comunitarias y de comunicaciones de emergencia sería:

- **Funcionamiento sin licencia**, para que cualquiera pueda participar sin una licencia de radioaficionado
- **Hardware de bajo costo** que una comunidad pueda desplegar a gran escala
- **Bajo consumo**, idealmente sostenible con energía solar o baterías
- **Comunicación de largo alcance** sin depender de la red celular ni de internet
- **Independencia de la infraestructura**, sin depender de la red eléctrica, los proveedores de internet ni las operadoras
- **Configuración y uso sencillos para quienes no son expertos en radio**
- **Apto para despliegues comunitarios**, no solo para el sótano de un operador
- **Capacidad para crecer más allá de unos pocos nodos** sin desmoronarse
- **Utilidad durante fallos de infraestructura**, cuando caen las torres celulares e internet
- **Entrega confiable por encima de un alcance récord**

Ten presente esta lista durante el resto del artículo. Evaluaremos cada decisión de arquitectura según estos criterios.

______

## Meshtastic

**Meshtastic** es la opción más madura y extendida de este grupo. Ofrece muchas ventajas para la mayoría de los usuarios.

- **Ecosistema maduro** con años de desarrollo activo
- **Gran comunidad**, un Discord activo y documentación amplia
- **Compatibilidad con muchos dispositivos** de LILYGO, Heltec, RAK y Seeed
- **Buenas aplicaciones móviles** para iOS y Android
- **Fácil para empezar**, la configuración inicial tarda menos de 20 minutos
- **Buen soporte para usuarios portátiles e itinerantes** que entran y salen de la malla de forma imprevisible
- **Funciones de GPS y telemetría** con un ecosistema desarrollado a su alrededor
- **Despliegues existentes** en la mayoría de las áreas metropolitanas, lo que facilita sumarse a una red en lugar de construir una desde cero

Para conocer en detalle el enrutamiento, la compatibilidad de hardware y la configuración de Meshtastic frente a MeshCore, consulta la **[guía comparativa de MeshCore y Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)**. Este artículo se centra en la cuestión de arquitectura más importante para despliegues grandes: **la inundación gestionada y los límites de saltos**.

### Inundación gestionada y por qué importan los saltos

En la **[inundación gestionada](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** de Meshtastic, un cliente normal cancela una retransmisión pendiente si antes oye el mismo paquete retransmitido. `ROUTER` y `ROUTER_LATE` pueden retransmitir de todos modos. `CLIENT_BASE` hace esa excepción para el tráfico hacia o desde un favorito.

El contador de saltos de Meshtastic vale **3** por defecto y admite hasta **7**. Desde el firmware 2.7.11, la infraestructura que cumple los requisitos puede [conservar el contador](https://meshtastic.org/blog/zero-cost-hops-favorite-routers/) después del primer salto si el retransmisor anterior es un `ROUTER` o `ROUTER_LATE` favorito. Cada retransmisión real consume tiempo de aire.

Un límite mayor puede alcanzar más repetidores, pero no obliga a transmitir a todos los receptores. **Más reenvíos** pueden causar:

- **Más tiempo de transmisión** consumido por mensaje
- **Más copias en el aire** si varios repetidores habilitados reenvían el mismo paquete
- **Más contención** por el canal compartido
- **Mayor riesgo de colisiones** cuando más radios transmiten en la misma ventana
- **Mayor consumo de batería** en cada nodo que recibe y retransmite
- **Menos capacidad disponible en el canal** para los mensajes reales

La capacidad de LoRa está limitada por el tiempo de transmisión y los límites regionales del ciclo de trabajo, no por la cantidad de nodos. Una red con diez nodos muy activos que difunden con frecuencia GPS y telemetría puede saturar un canal que cincuenta sensores silenciosos apenas usarían. Por eso una malla densa con un límite de saltos alto se degrada más rápido que otra con la misma cantidad de nodos, un límite menor y periodos de telemetría controlados.

Desde Meshtastic 2.6, los **mensajes directos** usan inundación para descubrir la ruta e intentan usar el siguiente salto aprendido. Si ese salto falla, pueden volver a la inundación.

En una malla pequeña o mediana, como la de un club de senderismo, esto rara vez importa. En una **red regional diseñada para cubrir una ciudad o varias localidades**, se convierte en la principal limitación de diseño.

______

## MeshCore

Los **repetidores dedicados** forman la capa fija de reenvío de MeshCore. Los dispositivos cliente son terminales.

### Funciones de los nodos

Los despliegues de MeshCore se organizan en torno a funciones diferenciadas, no como una red plana de nodos equivalentes:

- **Nodos complementarios o clientes** llevan una radio LoRa vinculada a un teléfono o portátil y, si hay infraestructura cercana, se comunican a través de ella
- **Repetidores** existen específicamente para reenviar tráfico entre clientes y otros elementos de infraestructura. Realizan gran parte del trabajo de enrutamiento
- **Servidores de sala** (opcionales) alojan conversaciones grupales y entregan mensajes almacenados a los clientes cuando vuelven a conectarse

En MeshCore, un **mensaje directo** inicial puede inundar la red para encontrar una ruta. Los siguientes pueden usarla y, según la configuración, volver a la inundación si falla. **[Los canales de grupo públicos y privados siguen usando inundación](https://docs.meshcore.io/faq/#5-general)** a través de repetidores habilitados. Los dispositivos cliente no retransmiten paquetes de otros nodos.

### Por qué encaja con una infraestructura fija

*Este es el argumento central a favor de MeshCore.* El modelo de inundación de Meshtastic ofrece ventajas reales para redes ad hoc e itinerantes: no requiere planificación ni infraestructura que mantener, y se adapta bien a la entrada y salida de nodos. El modelo de enrutamiento de MeshCore tiene ventaja cuando **los usuarios despliegan infraestructura de forma intencional**.

Una red basada en repetidores elevados y conocidos permite diseñar la cobertura a propósito. No depende de qué nodos estén al alcance entre sí en un día determinado. Esta diferencia importa para:

- **Nodos permanentes en azoteas** con energía confiable
- **Torres** e infraestructura de comunicaciones existente
- **Repetidores solares** en sitios sin personal
- **Sitios de retransmisión elevados o en montañas**
- **Infraestructura comunitaria** compartida por varios grupos
- **Redes regionales** que abarcan más de un barrio
- **Comunicaciones de emergencia** donde la cobertura predecible importa más que la flexibilidad

Vuelve a los fundamentos de RF: **los enlaces confiables entre puntos de infraestructura bien ubicados importan más que maximizar la ganancia de antena, la potencia de transmisión o el alcance teórico.** **Ambas mallas se benefician de repetidores bien ubicados.** Los nodos que retransmiten dependen de sus funciones y del tráfico.

______

## El argumento de los nodos itinerantes y su costo

Una sugerencia común es: *«Meshtastic es mejor para los nodos itinerantes y MeshCore para los fijos, así que usa Meshtastic para los usuarios y MeshCore como red troncal».*

La idea parece atractiva sobre el papel. En la práctica, mezclar ambos sistemas no combina automáticamente sus ventajas, porque **Meshtastic y MeshCore usan arquitecturas de red y enrutamiento distintas y no intercambian mensajes entre sí.** Un puente añade una capa de traducción entre dos sistemas incompatibles. No basta con elegir lo mejor de cada uno.

Al conectar ambas redes, tendrás:

- **Dos redes separadas**, cada una con su propia topología y comportamiento
- **Dos modelos de enrutamiento** que no comparten estado
- **Una capa de traducción** entre ambos que requiere desarrollo y mantenimiento continuos
- **Más infraestructura** para alojar el puente
- **Más configuración** entre dos ecosistemas de firmware en vez de uno
- **Más puntos de fallo**, porque el puente puede fallar por separado de cada malla
- **Diagnósticos más difíciles**, porque un fallo de entrega puede estar en cualquiera de las redes o en el puente que las conecta

Antes de adoptar este diseño, pregúntate directamente: **¿la complejidad añadida resuelve un problema que un único protocolo bien ajustado no puede resolver?** A menudo, una implementación de MeshCore bien configurada con algunos nodos complementarios aptos para usuarios itinerantes, o una implementación de Meshtastic con unos pocos repetidores bien ubicados y un límite de saltos mayor, ofrece la mayor parte del beneficio práctico sin mantener dos redes unidas por un puente.

______

## Reticulum

Reticulum merece una categoría propia, no un puesto como «tercera opción de malla LoRa», porque no es principalmente un protocolo de malla LoRa. **Su característica distintiva es la independencia del transporte.**

Reticulum es una pila de red basada en criptografía. No usa direcciones de origen, por lo que los paquetes no incluyen información sobre su procedencia. Cada dirección es soberana: una vez generada, puede alcanzarse globalmente en segundos o minutos y sigue siendo accesible aunque el dispositivo se traslade físicamente a otra parte de la red. Todas las comunicaciones se cifran de forma predeterminada con claves efímeras y secreto hacia adelante. Reticulum descarta los paquetes sin cifrar en vez de entregarlos. Nada de esto requiere controladores del kernel. Se ejecuta en el espacio de usuario de cualquier sistema con Python 3, incluida una Raspberry Pi Zero.

Reticulum admite estas interfaces:

- **LoRa**, con hardware compatible con RNode (un diseño abierto y definido de transceptor LoRa, que se puede construir, instalar en placas comunes o comprar ya preparado)
- **Radio por paquetes**, a través de cualquier TNC con modo KISS, adecuado para radioafición VHF y UHF
- **Wi-Fi y Ethernet cableada**, con descubrimiento automático de pares sin router ni servidor DHCP
- **Enlaces serie**, para conexiones directas entre dispositivos
- **TCP y UDP sobre redes IP existentes**, incluida internet
- **La red I2P** e interfaces personalizadas para cualquier otra opción que tenga un puente en Python

Sobre Reticulum funcionan aplicaciones como **LXMF** (un protocolo de mensajería tolerante a retrasos) y herramientas para usuarios finales como **Sideband**, **NomadNet** y clientes comunitarios de **MeshChat**, que añaden a las redes Reticulum funciones de mensajería y navegación comparables a las que Meshtastic y MeshCore incluyen de fábrica.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Diagrama que muestra cómo Reticulum conecta una malla LoRa, una red de radio por paquetes y un enlace a internet en una única red cifrada con direcciones" >}}

### Cuándo tiene sentido Reticulum

El valor de Reticulum se aprecia en una configuración heterogénea, por ejemplo:

**Malla LoRa → nodo Reticulum → enlace IP → nodo Reticulum → red de radio**

En este caso, Reticulum hace algo que ni Meshtastic ni MeshCore hacen: conecta dos sistemas de comunicación distintos en una misma red direccionable. Es un requisito concreto y real, no una mejora genérica. Algunos usos adecuados son:

- **Conectar redes geográficamente separadas** sin una ruta de radio directa entre ellas
- **Unir distintos medios físicos**, como una malla LoRa en un extremo y una red de radio por paquetes en el otro
- **Pasarelas de radio a IP** que transfieren tráfico entre una red de radio en campo e internet
- **Redes experimentales y de investigación**, donde importa más mezclar transportes que simplificar el despliegue
- **Redes sin un único medio que cubra todo el requisito**, en las que hay que unir varios componentes

### Cuándo Reticulum añade complejidad innecesaria

Si todas las personas de un despliegue usan hardware LoRa compatible y el objetivo real es **una sola malla LoRa regional**, añadir Reticulum aporta poco y tiene un costo concreto. Cada capa adicional de una pila de red implica más:

- **Configuración** que debe ser correcta y coherente en todos los nodos
- **Software** que instalar, actualizar y diagnosticar
- **Hardware** en algunas configuraciones, según cómo se conecten los puentes entre interfaces
- **Superficie de diagnóstico** cuando algo no se entrega
- **Conocimientos necesarios** para que los operadores entiendan un tercer modelo de red

*Usa Reticulum cuando la independencia del transporte resuelva una necesidad real, no solo porque admita más tipos de interfaz que las alternativas.* Un problema de límite de saltos en una sola malla LoRa se resuelve ajustando Meshtastic o MeshCore. No es un problema de independencia del transporte, y Reticulum no lo convierte en uno.

______

## Construye una malla sana antes de crear tres fragmentadas

Si un protocolo ya cumple tus requisitos, **construye una red sana** en vez de varias redes pequeñas unidas mediante puentes. Este principio de «primero una malla» debería orientar la mayoría de las decisiones anteriores.

En una red comunitaria, **la interoperabilidad entre quienes ya la usan suele importar más que la flexibilidad de arquitectura.** Una red grande y funcional basada en un único protocolo ofrece más valor práctico que tres redes interesantes en lo técnico, pero fragmentadas y con una comunicación parcial entre ellas.

### Las redes Meshtastic existentes importan

**No descartes Meshtastic solo porque MeshCore tenga ventajas de arquitectura para infraestructura fija.** Si una ciudad ya tiene decenas o cientos de nodos Meshtastic, esa base instalada es infraestructura real y una comunidad real. Migrar tiene un costo que una comparación de especificaciones no refleja:

- **Hardware instalado** que habría que reconfigurar o sustituir
- **Usuarios existentes** que ya saben usar la red
- **Conocimientos comunitarios** acumulados alrededor del despliegue actual
- **Repetidores instalados** y ubicados, a veces gracias a un acceso difícil de conseguir a azoteas o torres
- **Experiencia de configuración** acumulada por quienes mantienen la red
- **Canales establecidos** que la gente ya supervisa
- **Capacitación necesaria** para quienes aprendan un segundo sistema

La elección del protocolo es **en parte un problema de ingeniería y en parte un problema de adopción comunitaria.** La arquitectura que parece mejor sobre el papel no gana automáticamente si obliga a una comunidad activa a empezar de nuevo.

______

## El problema de las redes regionales

Considera un despliegue hipotético entre varias ciudades:

**Ciudad A, repetidor, repetidor, retransmisor rural, repetidor, Ciudad B, repetidor, Ciudad C**

En esta cadena, **prueba por separado los mensajes de grupo y los directos**. MeshCore puede reutilizar una ruta para los directos, pero sigue inundando para los grupales. Meshtastic puede conservar el contador de saltos en enlaces de infraestructura aptos. Cada retransmisión ocupa el canal. Ningún protocolo garantiza la entrega de extremo a extremo.

En este escenario, **los límites de saltos, el presupuesto de tiempo de transmisión, el comportamiento del enrutamiento y el diseño de la infraestructura dejan de ser teóricos** y determinan si la red funciona de extremo a extremo. A escala geográfica, las diferencias de arquitectura entre Meshtastic y MeshCore dejan de ser académicas.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Diagrama de una cadena de red mallada regional que conecta tres ciudades mediante repetidores y un retransmisor rural, y muestra cómo se acumulan el tiempo de transmisión y los saltos a lo largo de la distancia" >}}

______

## La RF importa más que el protocolo

**Ningún software de enrutamiento ingenioso crea una ruta de RF donde no existe una conexión física.** Antes de culpar al protocolo por un problema de cobertura, comprueba los fundamentos:

- **Altura de la antena** sobre los obstáculos
- **Línea de visión** entre los dos extremos del enlace
- **Despeje de la zona de Fresnel**, que no equivale a la línea de visión visual
- **Pérdidas en la línea de alimentación** por un cable coaxial barato o demasiado largo
- **Calidad de la antena** y si corresponde a la banda utilizada
- **Nivel de ruido** en el sitio de recepción
- **Terreno** entre los nodos
- **Ubicación de los nodos**, incluido el margen real para mejorarla
- **Margen del enlace**, la diferencia entre la señal recibida y el nivel mínimo necesario para decodificarla

*Una antena de 2 dBi bien ubicada en un mástil adecuado suele superar a una antena de alta ganancia mal colocada junto a una ventana del sótano.* El protocolo determina cómo gestiona la red los enlaces disponibles. No crea enlaces que la física no permite.

### Fiabilidad antes que alcance máximo

**No diseñes una red basándote en el límite máximo que un enlace alcanza de vez en cuando.** Diseña para que los enlaces funcionen de manera constante.

En una red comunitaria o de comunicaciones de emergencia, **una entrega predecible a 15 millas tiene más valor práctico que un enlace que llega a 40 millas de vez en cuando y falla el resto del tiempo.** Construye una cobertura solapada con infraestructura confiable en lugar de perseguir enlaces récord. Este principio se aplica sin importar qué protocolo transporte los mensajes.

______

## Cuál elegir

**Meshtastic tiene sentido** si valoras un ecosistema maduro, una adopción sencilla, usuarios portátiles e itinerantes y la compatibilidad con una comunidad Meshtastic existente. Es la opción predeterminada adecuada para la mayoría de quienes empiezan desde cero.

Los **repetidores fijos** ayudan a planificar la cobertura, no a eliminar la inundación. Para el chat grupal, prueba ambos protocolos con la frecuencia de mensajes, los ajustes de radio y la ubicación de repetidores previstos antes de elegir.

**Reticulum tiene sentido** cuando el problema va más allá de una sola malla LoRa y necesitas conectar distintos transportes o redes separadas en un único sistema direccionable.

Para una **red comunitaria de infraestructura sin licencia, de bajo consumo y largo alcance, basada principalmente en repetidores fijos**, inclínate por MeshCore. **Prueba el tráfico de grupo antes de cambiar.** Una red de repetidores fijos ayuda con la cobertura, pero no proporciona rutas dirigidas a los canales de grupo. *Si ya existe una red Meshtastic sana en tu zona, reemplazarla requiere beneficios suficientes para justificar la fragmentación de la comunidad existente.* Considera Reticulum cuando un protocolo de malla o un medio físico ya no cumpla los requisitos, no solo porque haga más cosas.

______

## Referencias

1. [Algoritmo de difusión en malla de Meshtastic](https://meshtastic.org/docs/overview/mesh-algo/)
2. [Configuración LoRa de Meshtastic (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Sitio oficial de MeshCore](https://meshcore.co.uk/)
4. [Pila de red Reticulum](https://reticulum.network/)
5. [¿Qué es Reticulum?](https://reticulum.network/manual/whatis.html)
6. [Configuración de interfaces de Reticulum](https://reticulum.network/manual/interfaces.html)
7. [Guía comparativa de MeshCore y Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)
