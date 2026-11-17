---
title: "Por qué Tailscale usa un relé: conexiones directas, DERP y relés entre pares"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Descubre por qué Tailscale usa un relé, cómo leer la salida de status y netcheck y cuándo conviene investigar una conexión DERP o de relé entre pares."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "relé Tailscale", "DERP", "relé entre pares de Tailscale", "conexión directa", "WireGuard", "travesía NAT", "NAT difícil", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "rendimiento VPN", "acceso remoto", "tailnet", "red doméstica", "latencia del relé", "cifrado de extremo a extremo"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Dos portátiles en islas separadas intercambian paquetes cifrados mediante un relé central mientras una ruta directa está interrumpida."
coverCaption: ""
---

**Tailscale usa un relé** cuando los dispositivos no han establecido una conexión directa. Una conexión DERP breve durante el inicio es normal. El uso persistente de un relé suele deberse a condiciones de NAT o del cortafuegos que afectan la ruta entre los dispositivos. Las conexiones directas, DERP y de relé entre pares mantienen el cifrado de extremo a extremo de WireGuard. [Tipos de conexión de Tailscale](https://tailscale.com/docs/reference/connection-types).

## Puntos clave

- **Reconoce la ruta:** distingue entre conexiones directas, DERP y relés entre pares.
- **Recopila pruebas:** ejecuta sondeos dirigidos al par y revisiones de red en ambos extremos.
- **Analiza el patrón:** compara pares de dispositivos y condiciones de red.
- **Elige un cambio:** justifícalo con una carga de trabajo medida y una nueva prueba.

## Antes de empezar

**Requisitos:** dos dispositivos inscritos y conectados, y un terminal con la interfaz de línea de comandos de Tailscale, o **CLI**. Solo necesitas acceso administrativo si la investigación lleva a cambiar la configuración.

**Tiempo estimado:** cinco minutos para las comprobaciones básicas y luego 15–20 minutos para el ejercicio de comparación. **Dificultad:** principiante para observar y media para realizar cambios de red. Primero define el problema, por ejemplo una copia de seguridad lenta o una respuesta tardía del terminal.

## Conexión directa, DERP y relé entre pares

Un **tailnet** es tu red de Tailscale. Sus dispositivos intentan establecer conectividad UDP directa. Los relés están disponibles cuando falla la ruta directa. Tailscale vuelve a comprobar periódicamente sus opciones de conexión. [Establecimiento de conexiones](https://tailscale.com/docs/reference/connection-types).

| Ruta | Recorrido del tráfico | Implicación habitual |
|---|---|---|
| **Directa** | Entre los dos dispositivos | Suele ser la ruta preferida para obtener mejor rendimiento |
| **Relé DERP** | A través de la infraestructura de relés de Tailscale | Añade un intermediario cuando falla el acceso directo |
| **Relé entre pares** | A través de un dispositivo configurado en tu tailnet | Una alternativa de relé bajo tu administración |

El **rendimiento de DERP** depende en parte de la ruta adicional y de la capacidad compartida del servicio. Tailscale documenta límites de rendimiento para repartir los recursos DERP de forma justa. No existe una velocidad universal de relé que permita predecir el tiempo de transferencia de archivos. [Solución de problemas de rendimiento de Tailscale](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Cómo se negocia la conexión

La **travesía de NAT** es el proceso para establecer una ruta utilizable a través de dispositivos que traducen direcciones. Tailscale inicia la comunicación mediante DERP mientras negocia una ruta directa. Si falla la conectividad directa, un relé entre pares configurado y disponible ofrece otra opción. Tailscale vuelve a comprobar las opciones con el tiempo. [Establecimiento de conexiones](https://tailscale.com/docs/reference/connection-types).

**NAT difícil** describe un comportamiento de asignación que complica la travesía. Las condiciones en ambos extremos importan. Dos dispositivos detrás de routers diferentes no necesariamente se comportan igual, aunque ambas redes usen direcciones privadas. [Conectividad de los dispositivos](https://tailscale.com/docs/reference/device-connectivity).

Para **un portátil que cambia de red**, la ruta al servidor de casa podría cambiar al pasar de la wifi doméstica a la red de un hotel. Anota qué red usaste durante la observación. Una conexión directa de ayer no demuestra cuál es la ruta de hoy.

## Comprueba la conexión actual

Sustituye **`home-server`** por el nombre de Tailscale o la dirección de tu par:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** comprueba la conectividad con el par indicado. **`tailscale status`** muestra los pares y los detalles de conexión. **`tailscale netcheck`** informa sobre las condiciones de red del dispositivo donde ejecutas el comando. La [referencia de la CLI de Tailscale](https://tailscale.com/docs/reference/tailscale-cli) documenta estos comandos.

| Indicador de salida | Interpretación |
|---|---|
| **`direct`** | El tráfico hacia este par usa una ruta directa |
| **`relay`** | El tráfico hacia este par pasa por DERP |
| **`peer-relay`** | El tráfico usa un relé entre pares configurado |
| **Un pong DERP inicial** | Revisa los resultados posteriores antes de decidir que la ruta siguió usando el relé |

Estas etiquetas aparecen en la [documentación de tipos de conexión](https://tailscale.com/docs/reference/connection-types). **Genera tráfico primero** y después comprueba el par que te interesa. Los comandos anteriores son ejemplos, no resultados de un benchmark.

## Interpreta un cambio de ruta

Esta **secuencia ilustrativa** omite direcciones y tiempos para centrar la atención en el cambio de conexión:

```text
Primera respuesta:    mediante DERP
Respuesta posterior:  mediante un endpoint directo
Estado posterior:     direct
```

**Interpretación:** la negociación tuvo éxito durante esta observación. La primera respuesta por sí sola habría llevado a un diagnóstico equivocado. Si las respuestas posteriores y el estado siguen indicando un relé, anota el uso persistente de un relé para este par de dispositivos y este periodo de prueba.

**Alcance del sondeo:** un ping de Tailscale correcto confirma la conectividad con el par para ese sondeo. No demuestra que tu panel, servicio de archivos o demonio SSH acepte el tráfico de la aplicación. Prueba por separado la aplicación que falla antes de declarar resuelto el problema.

## Qué indica netcheck

Ejecuta **`tailscale netcheck` en ambos dispositivos**. Compara estos campos con la [referencia de conectividad de dispositivos](https://tailscale.com/docs/reference/device-connectivity):

| Campo | Interpretación útil |
|---|---|
| **`UDP`** | Si el sondeo observó conectividad UDP saliente |
| **`MappingVariesByDestIP`** | Las asignaciones externas variables pueden dificultar la travesía de NAT |
| **`IPv6`** | Si el dispositivo tiene conectividad IPv6 utilizable |
| **`PortMapping`** | Si hay disponible un mecanismo de asignación de puertos compatible |

**Un solo campo no da un veredicto.** Que haya un mecanismo de asignación disponible no demuestra que funcione la ruta hacia un par concreto. Una etiqueta de relé tampoco identifica qué router causó el problema. Compara ambos extremos y los resultados reales de ping.

**El NAT del operador** importa cuando la traducción ascendente está fuera de tu control, como explicamos en nuestra guía sobre el [reenvío de puertos de T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/). No des por hecho que todas las conexiones detrás del NAT del operador tienen el mismo comportamiento de travesía.

## Compara tres pares de dispositivos

Si tienes uno disponible, usa un **tercer dispositivo inscrito** para mejorar las pruebas. El siguiente patrón es hipotético, no es un resultado medido:

| Par de dispositivos | Ruta observada |
|---|---|
| **Portátil a servidor de casa** | DERP |
| **Portátil a otro servidor** | Directa |
| **Servidor de casa a otro servidor** | DERP |

**Hipótesis de trabajo:** investiga primero la red del servidor de casa, ya que las dos rutas observadas que lo incluyen siguieron usando un relé. Es una pista, no una prueba. Cada par negocia por separado y el servidor de comparación tiene sus propias condiciones de red.

**Siguiente observación:** recopila la salida de netcheck en los tres dispositivos y repite la prueba entre el portátil y el servidor de casa desde otra red que controles. Si la ruta cambia, anota exactamente qué red cambió. No atribuyas el resultado a una regla concreta del cortafuegos sin probarla.

**Ejercicio:** la conexión entre el portátil y el servidor de casa es directa, pero la transferencia de archivos sigue siendo lenta. Una explicación basada en un relé ya no encaja con esta observación. Antes de cambiar la configuración del relé, comprueba la conexión de subida subyacente, la carga del servidor, el almacenamiento y el comportamiento de la aplicación.

## Elige un cambio específico

Empieza con una **prueba comparativa** en otra red que controles. Si el mismo par pasa a conectarse directamente, obtienes pruebas útiles sobre la ruta de red original. Revisa las restricciones UDP y la configuración de NAT antes de cambiar ajustes de DNS o de aplicaciones que no guardan relación.

**Cambia una variable**, repite las comprobaciones y mide la misma carga de trabajo. Anota el sentido de la transferencia, el tamaño del archivo, el tiempo transcurrido y el tipo de conexión. Así separarás una ruta mejorada de un cambio no relacionado en la carga del servidor o del almacenamiento.

Los **cambios del cortafuegos** deben seguir las recomendaciones específicas de la plataforma y las pruebas recopiladas. Abrir un puerto de aplicación a Internet público no mejora por sí solo la ruta de transporte de Tailscale. Limita los cambios al tráfico necesario y a la red que administras. [Recomendaciones de Tailscale sobre cortafuegos](https://tailscale.com/docs/integrations/firewalls).

| Hallazgo | Cambio que conviene evaluar |
|---|---|
| **Falla el sondeo UDP** | Revisa las restricciones UDP salientes de esta red |
| **La asignación cambia según el destino** | Revisa el comportamiento de NAT en los equipos que administras |
| **Ruta directa, aplicación lenta** | Investiga el host, la conexión subyacente y la carga de trabajo |
| **El relé funciona y la experiencia es aceptable** | Conserva la configuración y documenta el valor de referencia |

*Prefiere una mejora medida antes que cambiar los ajustes solo para quitar la etiqueta del relé.*

## Evalúa un relé entre pares

Un **relé entre pares** requiere un host adecuado, un puerto UDP accesible y una política de acceso que permita su uso. Tanto el relé como los clientes participantes necesitan Tailscale 1.86 o posterior. Revisa las plataformas de host compatibles antes de asignar un dispositivo. [Requisitos para relés entre pares](https://tailscale.com/docs/features/peer-relay).

**La ubicación determina la utilidad.** Un dispositivo detrás del mismo límite de red inaccesible no ayudará a otros pares hasta que el puerto del relé sea accesible.

**Coste de mantenimiento:** alguien debe mantener el relé conectado, actualizado y con recursos suficientes. Si administras la red de vez en cuando y la latencia es aceptable, compara esta carga con el beneficio medido. Si realizas transferencias grandes con frecuencia, mide la carga de trabajo a través del relé propuesto antes de adoptarlo.

## Comprueba los efectos del tráfico compartido

El **tráfico agregado** merece atención cuando un router de subred o un nodo de salida lleva varias cargas de trabajo por DERP. Tailscale documenta situaciones en las que un gran volumen de tráfico retransmitido retrasa el tráfico sensible a la latencia que comparte la conexión. [Solución de problemas de NAT difícil](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Ejercicio de comparación:** observa tu sesión interactiva antes, durante y después de una copia de seguridad grande. Mantén fija la pareja de endpoints y anota la ruta cada vez. Los retrasos que aparecen durante la transferencia justifican investigar la carga compartida, pero no demuestran su causa exacta.

**Elige la siguiente prueba** según lo observado. Comprueba la saturación del enlace y la carga del host. Después, evalúa una ruta directa o la separación de los servicios sensibles a la latencia si la topología lo permite. No trates un síntoma de DNS como prueba automática de un error en la configuración de DNS.

## ¿Un relé es un nodo de salida?

Un **nodo de salida** enruta el tráfico general de Internet de un cliente a través de un dispositivo seleccionado del tailnet. Un relé transporta el tráfico entre pares de Tailscale. Elegir un nodo de salida no garantiza una ruta directa hasta él. [Documentación de nodos de salida](https://tailscale.com/docs/features/exit-nodes).

## Crea un registro de diagnóstico

Guarda un **registro breve del antes y el después** para el problema real:

```text
Fecha y versiones de Tailscale:
Dispositivos de origen y destino:
Redes usadas por cada dispositivo:
Rutas de conexión inicial y estable:
Observaciones de netcheck en ambos extremos:
Carga de trabajo, sentido y tiempo transcurrido:
Único cambio probado:
Resultado de la nueva prueba:
Decisión de conservar o revertir el cambio:
```

**Criterio de finalización:** el registro conecta un síntoma específico con observaciones, una hipótesis y una nueva prueba medida. «El relé desapareció» es un resultado incompleto si la aplicación sigue lenta. «La copia de seguridad cumple el tiempo requerido mediante DERP» es válido si el requisito está definido de forma explícita.

**Usa `tailscale netcheck` como evidencia, no como veredicto.** El comando describe la red que ve un dispositivo. La ruta establecida corresponde a un par de dispositivos y a una carga de trabajo. Antes de cambiar la configuración del cortafuegos o de NAT, guarda ambos endpoints, la última línea de `tailscale status` y la medición de la aplicación.

## Próximos pasos

Anota la ruta hacia el par importante y prueba la carga de trabajo antes de cambiar los ajustes de red. Para la pregunta independiente sobre quién opera tu infraestructura de coordinación, lee [Tailscale frente a Headscale](/articles/tailscale-vs-headscale-comparison-guide/).
