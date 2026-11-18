---
title: "MeshCore frente a Meshtastic"
date: 2026-06-26
lastmod: 2026-11-12
toc: true
draft: false
description: "Compara MeshCore y Meshtastic según el enrutamiento, alcance, tiempo de transmisión, infraestructura, compatibilidad de dispositivos y tipo de despliegue."
genre: ["LoRa", "Redes malladas", "Comunicaciones sin conexión", "Comunicaciones de emergencia", "Comunicaciones tácticas", "Radioafición", "Código abierto", "Preparación ante desastres", "Redes inalámbricas", "Privacidad"]
tags: ["meshcore frente a meshtastic", "meshtastic", "meshcore", "red mallada lora", "comunicaciones sin conexión", "comparativa meshtastic", "comparativa meshcore", "radio lora", "redes malladas", "comunicaciones de emergencia", "malla táctica", "radio sin conexión", "protocolo meshtastic", "protocolo meshcore", "lora meshtastic", "comunicaciones ante desastres", "radio mallada", "almacenamiento y reenvío", "inundación lora", "malla LoRa", "t-beam meshtastic", "heltec lora", "rak wisblock", "mensajería sin conexión", "protocolo de red mallada", "meshtastic 2.6", "tiempo de transmisión lora", "radio para emergencias"]
cover: "/img/cover/meshcore-vs-meshtastic-comparison-guide.webp"
coverAlt: "Ilustración de dos redes LoRa malladas: Meshtastic a la izquierda con nodos que difunden paquetes, y MeshCore a la derecha con enrutamiento estructurado, sobre un fondo oscuro."
coverCaption: ""
ref: ["/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide"]
---

## Respuesta breve

Meshtastic y MeshCore funcionan con el mismo hardware LoRa económico. Ambos permiten enviar mensajes cifrados sin red móvil ni Internet. **Los protocolos no son compatibles entre sí.**

**Su filosofía de enrutamiento es distinta.** Meshtastic difunde paquetes a todos los nodos cercanos. MeshCore dirige el tráfico por una infraestructura planificada. Estos enfoques tienen distinto rendimiento al crecer la red.

*Meshtastic sirve a la mayoría.* Su aplicación móvil está pulida, su comunidad es grande, su documentación es sólida y la configuración tarda menos de 20 minutos. MeshCore se adapta mejor a despliegues planificados donde importa más la eficiencia del tiempo de transmisión que la autoorganización espontánea.

**Los fundamentos de radiofrecuencia importan más que el firmware.** Ningún protocolo compensa una antena mal ubicada.

______

## Qué hace cada sistema

### Meshtastic

**Meshtastic** es un proyecto de código abierto iniciado en 2020 por Kevin Hester. El firmware convierte hardware LoRa común en una red mallada de mensajería de texto sin depender de Internet ni de redes móviles. Las emisiones usan inundación controlada: cada nodo vuelve a transmitir los paquetes hasta un límite de saltos configurable. Desde la versión 2.6, **los mensajes directos usan enrutamiento al siguiente salto** tras descubrir la ruta, en vez de usar inundación. Así se reduce el tiempo de transmisión punto a punto.

El firmware funciona en hardware LoRa que muchos usuarios ya tienen o compran a bajo coste. **LILYGO T-Beam, Heltec WiFi LoRa 32, RAK WisBlock y Seeed SenseCAP Indicator** admiten Meshtastic sin herramientas especiales. Las aplicaciones para iOS y Android reciben buen mantenimiento. Una persona sin conocimientos técnicos se conecta en menos de diez minutos. El ecosistema incluye puentes MQTT, integración con Home Assistant y complementos ATAK.

### MeshCore

**MeshCore** ganó popularidad en 2023 y 2024. Su firmware funciona en gran parte del mismo hardware LoRa, pero usa una **arquitectura de enrutamiento híbrida**. Primero descubre rutas. Después, el tráfico pasa por repetidores hasta el destino en vez de difundirse a todos. Esto no es almacenamiento y reenvío en el sentido de redes tolerantes a demoras.

Los repetidores se encargan de la mayor parte del reenvío. **Los servidores de sala son opcionales.** Guardan mensajes grupales para que los clientes los recuperen al reconectarse. Los clientes llevan una radio LoRa complementaria y se conectan mediante infraestructura cuando existe, o se comunican directamente con nodos cercanos si no hay repetidor.

______

## Diferencia técnica principal

### Cómo enruta Meshtastic

Las emisiones usan **inundación controlada**. Cada nodo retransmite paquetes hasta el límite de saltos. Ningún nodo necesita conocer la topología. Los nodos nuevos se incorporan sin configuración y los nodos caídos se evitan automáticamente. Desde la versión 2.6, **los mensajes directos usan enrutamiento al siguiente salto** tras descubrir la ruta, lo que reduce el tiempo de transmisión punto a punto.

**La restricción real es el tiempo de transmisión, no el número de nodos.** LoRa usa bandas ISM compartidas con límites regionales de ciclo de trabajo, normalmente del 1 % en Europa. Una red con balizas GPS frecuentes, telemetría y actividad de canal satura el tiempo de transmisión antes de llegar a un límite absoluto de nodos. Diez nodos activos que envían telemetría frecuente causan más contención que cincuenta sensores silenciosos. Las mallas densas con varias decenas de usuarios activos suelen tener más contención, pero no existe un límite fijo. El umbral depende del factor de dispersión, el ajuste de tiempo de transmisión, los intervalos de telemetría, el terreno y la ubicación de los repetidores.

Meshtastic genera tráfico adicional con anuncios de información de nodos, telemetría de batería, paquetes GPS y detección de vecinos. Las versiones recientes redujeron este tráfico. *Ajustar estos parámetros suele resolver problemas de rendimiento antes de que sea necesario cambiar de protocolo.*

### Cómo enruta MeshCore

MeshCore descubre y aprende rutas, luego dirige el tráfico hacia la infraestructura en vez de retransmitirlo a todos. **Los repetidores reenvían tráfico entre nodos.** Los servidores de sala pueden alojar conversaciones grupales y guardar mensajes para los clientes que vuelvan a conectarse.

La ocupación del canal depende de las conversaciones activas, no del total de nodos. Un despliegue grande con muchos nodos silenciosos no pierde rendimiento como una red densa de inundación con mucho tráfico adicional. MeshCore se diseñó para despliegues bastante mayores, aunque el rendimiento real depende de la calidad de la instalación.

Sin repetidor, los clientes se comunican directamente si están dentro del alcance. *La arquitectura rinde mejor con infraestructura, pero no la exige.*

______

## Hardware

Ambos protocolos funcionan en las mismas placas LoRa populares.

| Placa | Meshtastic | MeshCore |
|---|---|---|
| LILYGO T-Beam (ESP32 + SX1276/SX1262) | Sí | Sí |
| LILYGO T-Echo (nRF52840 + SX1262) | Sí | Sí |
| Heltec WiFi LoRa 32 V3 | Sí | Sí |
| RAK WisBlock 4631 | Sí | Sí |
| Seeed SenseCAP Indicator | Sí | Parcial |
| Station G2 | Sí | Sí |

**Puedes cargar cualquiera de los dos firmware en el mismo dispositivo físico.** Cambiar de protocolo no requiere comprar hardware nuevo. Probarlos solo cuesta tiempo.

______

## Facilidad de configuración

### Configurar Meshtastic

1. Descarga el firmware desde meshtastic.org
2. Cárgalo con el instalador web flasher.meshtastic.org, sin controladores
3. Instala la aplicación Meshtastic en el teléfono
4. Empareja por Bluetooth
5. Únete o crea un canal con un nombre y contraseña compartidos

**Tiempo total para un usuario nuevo: menos de 20 minutos.** El cifrado del canal usa claves precompartidas AES-256. El canal público predeterminado te conecta de inmediato con cualquier nodo Meshtastic cercano. La aplicación muestra posiciones GPS en un mapa si los nodos tienen GPS habilitado.

### Configurar MeshCore

1. Carga el nodo de infraestructura, repetidor o servidor de sala, con PlatformIO o un binario precompilado
2. Carga la radio complementaria del cliente
3. Instala la aplicación MeshCore
4. Configura la dirección y las credenciales de la infraestructura en la aplicación
5. Conecta la radio complementaria por Bluetooth

**La configuración exige más planificación.** Debes conocer las funciones de los nodos antes del despliegue. Los servidores de sala son opcionales, pero conservan mensajes para clientes desconectados. *Dos amigos que quieren comunicarse rápido deberían elegir Meshtastic. Un equipo que instala una estación base con un repetidor en el tejado debería elegir MeshCore.*

______

## El tiempo de transmisión es la restricción real

Ambos protocolos funcionan sobre LoRa. **La capacidad de LoRa depende del tiempo de transmisión y del presupuesto de ciclo de trabajo, no del número de nodos.**

Las variables que determinan el rendimiento de la red:

- **Factor de dispersión.** Los valores más altos aumentan el alcance, pero reducen la velocidad y la capacidad total.
- **Ajuste de tiempo de transmisión.** Los ajustes de largo alcance consumen más ciclo de trabajo por mensaje.
- **Intervalo de telemetría.** GPS, batería y paquetes ambientales de Meshtastic añaden tráfico continuo.
- **Frecuencia de mensajes.** Los usuarios activos que envían con frecuencia afectan más que los nodos pasivos.
- **Ubicación de repetidores.** Un repetidor bien ubicado distribuye la carga. Uno mal ubicado aumenta la congestión.
- **Terreno.** Los nodos que no se oyen añaden tráfico sin causar contención. Los que oyen simultáneamente a muchos otros sí la causan.

*Meshtastic reduce la planificación y acepta algo de tráfico adicional a cambio de la autoorganización. MeshCore exige planificación y la recompensa con un uso más predecible del tiempo de transmisión. Cambiar de Meshtastic a MeshCore sin mejorar la planificación no garantiza un mejor rendimiento.*

______

## Consideraciones normativas

Las comparaciones de rendimiento varían por región porque las reglas son distintas:

- **915 MHz (EE. UU.):** la FCC Parte 15 no fija un límite de ciclo de trabajo, aunque sí hay límites de potencia.
- **868 MHz (UE):** ciclo de trabajo del 1 % según ETSI, equivalente a 36 segundos de transmisión por hora y canal.
- **433 MHz (UE/Asia):** muchas regiones aplican límites más estrictos, a menudo del 10 % en ciertas subbandas.

**El ciclo de trabajo del 1 % en Europa es una restricción normativa estricta.** Las mallas densas de Meshtastic en la UE alcanzan los límites antes que despliegues equivalentes en EE. UU. El uso más eficiente del tiempo de transmisión de MeshCore ofrece un beneficio proporcionalmente mayor en regiones con límites de ciclo de trabajo.

______

## Privacidad y seguridad

### Meshtastic

Meshtastic cifra el tráfico de canales privados con **claves precompartidas AES-256**. Todos los mensajes de un canal usan la misma clave. Quien tenga la clave lee todos los mensajes, incluidas las posiciones GPS. **El canal público predeterminado usa una clave conocida que se distribuye con el firmware**, por lo que no ofrece confidencialidad frente a otras personas que usen Meshtastic cerca.

Las posiciones GPS de un canal privado cifrado solo las ven los nodos con la clave. En el canal público, cualquiera puede verlas. *Esto importa si el seguimiento tiene consecuencias operativas.*

Meshtastic 2.6 mejoró el enrutamiento de mensajes directos. El tráfico grupal sigue usando la clave compartida del canal. Los mensajes directos ofrecen más aislamiento, pero no tienen cifrado de extremo a extremo en el sentido del protocolo Signal.

### MeshCore

El enrutamiento híbrido de MeshCore implica que **un oyente pasivo no puede reconstruir toda la topología de la red** al escucharla. El tráfico se dirige a infraestructura concreta en vez de difundirse a todos. **Los mensajes directos usan cifrado por contacto**, no una clave compartida de canal. Otros nodos de la misma infraestructura no pueden descifrar tu conversación directa aunque usen el mismo repetidor.

Los nodos de infraestructura retransmiten tráfico cifrado. En mensajes directos con cifrado por contacto, el repetidor reenvía el texto cifrado sin descifrarlo. En las conversaciones de sala, sus servidores ven el contenido de las salas que alojan. *La pregunta clave es si controlas el servidor de sala.*

MeshCore no ofrece cifrado de extremo a extremo estricto como el protocolo Signal. **El cifrado por contacto de mensajes directos mejora de forma significativa la protección frente a una clave compartida de canal.** Los usos operativos de alto riesgo deben evaluar los detalles de implementación.

______

## Consumo de energía

Con los ajustes predeterminados, MeshCore genera menos transmisiones de radio adicionales que Meshtastic. **Transmitir menos mejora la autonomía de los nodos cliente.** Los paquetes de telemetría, las difusiones GPS y la inundación controlada de Meshtastic consumen tiempo de transmisión. Puedes reducir ese tráfico ajustando los intervalos de telemetría y desactivando la difusión GPS en nodos sin GPS. Con ajustes predeterminados comparables, **MeshCore transmite menos**.

Una instalación Meshtastic bien ajustada, con telemetría mínima, se acerca a la autonomía de MeshCore. Los valores predeterminados favorecen a MeshCore.

______

## Resiliencia de la red

**La inundación controlada de Meshtastic es resistente a fallos.** Perder un nodo de retransmisión suele tener poco efecto operativo porque los demás nodos redirigen el tráfico. No hace falta conocer de antemano los nodos disponibles. La malla se repara de forma pasiva.

**MeshCore depende más de la ubicación de los repetidores.** Una red MeshCore bien diseñada y con buena cobertura ofrece un rendimiento predecible. Si se pierde el único repetidor de una zona, los nodos que dependen de él pierden conectividad. *MeshCore recompensa la planificación previa. Meshtastic tolera mejor los fallos de nodos.*

Meshtastic acepta más tráfico de radio a cambio de resiliencia. MeshCore acepta dependencia de infraestructura a cambio de eficiencia.

______

## GPS y seguimiento de posiciones

**El ecosistema GPS de Meshtastic está más desarrollado.** La aplicación móvil incluye un mapa. Los nodos de la comunidad alimentan mapas públicos de seguimiento, como meshmap.net, mediante pasarelas MQTT. La telemetría de posición es una función central. El uso compartido de posiciones para senderismo, coordinación de búsqueda y rescate y seguimiento de eventos está bien desarrollado.

MeshCore no se centra en el seguimiento de posiciones. *Si necesitas principalmente conocer posiciones GPS, el ecosistema de Meshtastic es más desarrollado y maduro en 2026.*

______

## Ecosistema y comunidad

Meshtastic tiene una **comunidad más grande**:

- Discord activo con miles de miembros
- Subreddit activo en r/meshtastic
- Documentación amplia en meshtastic.org
- Integraciones de terceros con MQTT, Home Assistant, Node-RED, ATAK y bibliotecas Python
- Versiones frecuentes del firmware
- Muchos guías de hardware creadas por la comunidad

MeshCore crece, pero sigue siendo más pequeño. *Hay menos publicaciones en foros, tutoriales e integraciones de terceros. Si algo falla, buscarás respuestas en el código fuente del firmware o en el Discord del proyecto, en lugar de encontrar soluciones ya publicadas.*

Ambos proyectos son de código abierto, aunque sus licencias difieren. **Meshtastic usa una licencia de tipo BSD. MeshCore usa GPL.** Algunas organizaciones lo tienen en cuenta al desplegar y distribuir el software.

______

## Cuándo conviene Meshtastic

**Grupos informales pequeños.** Un club de senderismo que quiera enviar mensajes sin conexión y compartir posiciones debería usar Meshtastic. Se configura fácilmente, el mapa funciona bien y la red se organiza sola.

**Despliegues móviles.** Meshtastic funciona bien con usuarios que se mueven por el terreno y entran o salen de forma impredecible. Su inundación se autoorganiza y no exige planificar la infraestructura para los nodos móviles.

**Despliegues para consumidores.** Las personas sin conocimientos técnicos pueden configurar sus dispositivos sin ayuda. Meshtastic facilita la incorporación.

**Despliegue rápido para un evento.** Comunicaciones de festivales, coordinación de carreras o búsqueda y rescate que empieza hoy y termina la semana siguiente. La configuración rápida y la ausencia de infraestructura obligatoria hacen práctico Meshtastic.

**Seguimiento GPS.** En 2026, Meshtastic es la opción adecuada si el seguimiento de posiciones es el uso principal.

______

## Cuándo conviene MeshCore

**Despliegues con infraestructura planificada.** Tienes un repetidor en una azotea o un servidor de sala con alimentación fiable. El enrutamiento híbrido de MeshCore aprovecha la infraestructura fija.

**Redes grandes con infraestructura dedicada.** Elige MeshCore si importan más la eficiencia de transmisión y el rendimiento predecible a escala que la autoorganización espontánea.

**Persistencia de mensajes con conectividad intermitente.** Los servidores de sala guardan mensajes y los entregan cuando se reconectan los clientes. **Es una de las ventajas prácticas más concretas de MeshCore frente a Meshtastic.**

**Separación entre nodos fijos y móviles.** Necesitas algunos nodos como infraestructura y otros como clientes. El modelo de roles de MeshCore se diseñó para ello.

**Regiones con límites de ciclo de trabajo.** Los despliegues europeos sujetos al límite ETSI del 1 % aprovechan más la eficiencia de transmisión de MeshCore.

**Cifrado por contacto.** Para cifrar mensajes directos, el modelo de MeshCore mejora de forma significativa el enfoque de Meshtastic con claves compartidas de canal.

______

## Cuándo falla cada sistema

### Debilidades de Meshtastic

- **Contención de transmisión a escala.** Las mallas densas con ajustes predeterminados de mucho tráfico, difusiones GPS frecuentes y canales activos se degradan. Corrige la configuración antes de cambiar de protocolo.
- **Sin persistencia de mensajes si no hay infraestructura.** Sin pasarela MQTT, los mensajes perdidos no se recuperan.
- **Privacidad de posición en el canal público.** Cualquiera que escuche ve todas las difusiones GPS. Puede servir para uso informal, pero no para requisitos de seguridad operativa.
- Las versiones principales del firmware a veces introducen problemas de compatibilidad hasta que la red se actualiza a versiones compatibles.

### Debilidades de MeshCore

- **Configuración compleja.** Debes comprender las funciones de infraestructura antes de desplegarlo de forma útil.
- **Comunidad más pequeña.** La documentación, los tutoriales y las integraciones de terceros de Meshtastic están más desarrollados.
- **Menos variedad de hardware.** MeshCore admite una lista menor de dispositivos.
- **Aplicaciones móviles menos maduras.** Son funcionales, pero menos pulidas que las aplicaciones Meshtastic para iOS y Android.
- **Dependencia de infraestructura para el mejor rendimiento.** Sin repetidores, los clientes se comunican directamente, pero desaparece la eficiencia del enrutamiento. Si el grupo no se compromete con una infraestructura fija, la ventaja arquitectónica no se materializa.
- **Recuperación de la red.** Perder un repetidor en una zona corta la conexión de los nodos dependientes. La inundación de Meshtastic tolera mejor los fallos.
- **Sin interoperabilidad entre protocolos.** MeshCore y Meshtastic no intercambian mensajes. El mismo hardware admite cualquiera de los dos firmware, pero usar ambos implica administrar dos redes separadas.

______

## La radiofrecuencia importa más que el firmware

**La calidad y altura de la antena, las pérdidas del cable, el terreno y los ajustes de radio afectan más al rendimiento que la elección del firmware.**

Un nodo Meshtastic bien ubicado en una cima y con buena antena supera a un repetidor MeshCore mal ubicado en una caja metálica en un sótano. Esta comparación supone una calidad física de despliegue similar.

Antes de cambiar de protocolo para solucionar un problema de rendimiento, comprueba lo siguiente:

- Las conexiones de antena están limpias y tienen pocas pérdidas.
- Los nodos están lo más altos posible.
- El ajuste de tiempo de transmisión corresponde al alcance necesario.
- **Los intervalos de telemetría no saturan el canal.**
- El factor de dispersión corresponde a la densidad de nodos.

______

## Resumen comparativo

| Factor | Meshtastic | MeshCore |
|---|---|---|
| Modelo de red | Inundación controlada y mensajes directos al siguiente salto | Descubrimiento híbrido de rutas y reenvío dirigido |
| Dificultad de configuración | Fácil | Media a alta |
| Diseño para escalar | Flexible, pierde rendimiento con contención | Diseñado para redes planificadas mayores |
| Calidad de la aplicación móvil | Excelente | Funcional |
| Tamaño de la comunidad | Muy grande | En crecimiento |
| Seguimiento GPS y de posiciones | Ecosistema desarrollado | Enfoque mínimo |
| Persistencia de mensajes | No. Requiere pasarela MQTT | Sí, mediante servidores de sala opcionales |
| Cifrado de mensajes directos | Clave compartida de canal | Cifrado por contacto |
| Necesidad de infraestructura | No es necesaria | Optimizado para nodos de infraestructura |
| Recuperación de red | Resiliente y autorreparable | Depende de la ubicación de repetidores |
| Compatibilidad de hardware | Amplia | Subconjunto concreto |
| Ideal para | Grupos móviles, improvisados y pequeños | Despliegues planificados con infraestructura fija |

______

## Cuál elegir

**Empieza con Meshtastic.** Estarás transmitiendo en una tarde. Encontrarás gente con quien probarlo. La aplicación funciona y la documentación es excelente. El enrutamiento al siguiente salto de Meshtastic 2.6 reduce la diferencia de eficiencia para mensajes directos punto a punto.

**Pasa a MeshCore cuando los valores predeterminados de Meshtastic no se ajusten al despliegue.** Si tienes repetidores dedicados, necesitas conservar mensajes para usuarios intermitentes o construyes una red grande y planificada donde la eficiencia de transmisión importe más que la autoorganización, la arquitectura de MeshCore encaja y compensa el esfuerzo de configuración.

Antes de cambiar de protocolo, **ajusta tu instalación de Meshtastic**. Reduce los intervalos de telemetría. Desactiva la difusión GPS en nodos sin GPS. Ajusta el tiempo de transmisión a la densidad de nodos. *Muchos problemas de rendimiento se deben a la configuración, no al protocolo.*

Los protocolos cubren necesidades distintas en el equilibrio entre planificación y espontaneidad. Meshtastic reduce la planificación y acepta el tráfico adicional de la autoorganización. MeshCore exige planificación y la recompensa con un rendimiento más predecible. **Ninguno sustituirá al otro porque sus usos son distintos.**

*¿Construyes una red que debe conectar LoRa con radio por paquetes, Wi-Fi o Internet, en vez de limitarse a una malla LoRa?* Consulta la **[guía comparativa de Meshtastic, MeshCore y Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)** para ver dónde encaja una red independiente del transporte y dónde añade complejidad innecesaria.
