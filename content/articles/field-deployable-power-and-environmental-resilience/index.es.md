---
title: "Alimentación y resiliencia ambiental para sistemas de campo"
date: 2026-08-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Planifica la alimentación y protección ambiental de nodos edge desplegados en campo. Dimensiona UPS, baterías y paneles solares, y gestiona sincronización horaria, clasificación de gabinetes, puesta a tierra y protección contra sobretensiones."
genre: ["Computación en el borde", "Informática de campo", "Sistemas de alimentación", "Hardware", "Recuperación ante desastres", "Computadoras reforzadas", "Redes"]
tags: ["dimensionamiento de UPS", "alimentación de campo", "alimentación de servidor CC", "servidor con energía solar", "clasificación IP de gabinetes", "clasificación NEMA", "protección contra sobretensiones", "puesta a tierra de electrónica", "alimentación de servidor sin conexión a red", "alimentación de centro de datos portátil", "cálculo de autonomía de batería", "alimentación de servidor de 12 V", "alimentación de 48 V CC", "alimentación de TI con generador", "sistema de alimentación reforzado", "alimentación de nodo edge", "alimentación para recuperación ante desastres", "servidor desplegable en campo", "resiliencia ambiental", "alimentación de expedición", "batería LiFePO4", "fosfato de hierro y litio", "alimentación USB PD", "comparación de químicas de baterías", "Network UPS Tools NUT", "monitoreo de UPS por SNMP", "sincronización horaria NTP", "reloj sincronizado por GPS"]
cover: "/img/cover/field-deployable-power-environmental-resilience-solar-ups.webp"
coverAlt: "Ilustración de un servidor reforzado al aire libre, con paneles solares que cargan un banco de baterías y gráficos digitales de gestión eléctrica sobre un fondo oscuro."
coverCaption: ""
ref: ["/articles/field-deployable-edge-compute-hardware-and-enclosure-selection", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes", "/articles/field-it-tidbits-beyond-the-mini-datacenter", "/articles/the-role-of-ecc-memory-in-mitigating-data-corruption"]
---

**La confiabilidad de un servidor desplegado en campo depende de su fuente de alimentación.** El mejor gabinete y la computadora más rápida no sirven si el sitio pierde energía y nada toma la carga. *La planificación eléctrica no es un accesorio de la instalación. Es la parte con más probabilidades de fallar primero.*

Esta es **la segunda parte de una serie de cuatro** sobre servidores compactos y equipos de red de despliegue rápido. [La primera parte](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) cubrió gabinetes y capacidad de cómputo. Esta parte explica cómo alimentar el equipo y protegerlo del calor, polvo, agua y problemas eléctricos. [La tercera parte](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/) aborda conectividad y seguridad de datos. [La cuarta parte](/articles/field-it-tidbits-beyond-the-mini-datacenter/) reúne otros detalles.

______

## Dimensiona un UPS para uso en campo

Un **UPS (sistema de alimentación ininterrumpida)** cubre el intervalo entre una falla eléctrica y el apagado o la transferencia a una fuente de respaldo. Dimensionarlo para campo empieza con un cálculo sencillo.

1. Suma la **potencia de cada dispositivo** dentro del estuche: computadora, switch, punto de acceso y almacenamiento.
2. Multiplica el total por **1,5 a 1,6** para dejar margen a la corriente de arranque.
3. Divide la **capacidad nominal en vatios-hora** del UPS entre la potencia total de la carga para estimar las horas de autonomía.

*La capacidad de la batería disminuye con la edad y la temperatura. Considera el tiempo publicado por el fabricante como el mejor caso, no como una garantía.* Planifica menos autonomía en condiciones reales, sobre todo en ambientes calurosos donde las baterías pierden capacidad más rápido.

**[Schneider Electric / APC](https://www.apc.com/) publica instrucciones detalladas sobre el dimensionamiento de UPS y el comportamiento de las baterías.** Su regla principal también aplica en campo: conecta el UPS directamente a una toma de pared o a la salida del generador, nunca a una regleta con protección contra sobretensiones. Conecta las tomas adicionales que necesites a una PDU separada después del UPS.

| Tipo de UPS | Ideal para | Compromiso |
|---|---|---|
| **UPS line-interactive** | La mayoría de los sistemas de campo con energía de red o generador | Tiempo breve de transferencia al perder energía, normalmente menos de 10 ms |
| **UPS en línea de doble conversión** | Equipos sensibles con energía inestable o ruidosa | Más peso y costo por vatio |
| **Paquete de baterías CC con inversor integrado** | Sistemas ultracompactos donde no cabe un UPS tradicional | Menor eficiencia al convertir CC a CA y de vuelta |

## Alimentación de CC: evita el inversor

Cada conversión de CA a CC desperdicia energía en forma de calor. **Si el equipo lo admite, alimentarlo directamente con corriente continua elimina una etapa de conversión y un punto de falla.**

- **Los sistemas de 12 V** sirven para montajes pequeños, como computadoras de placa única, thin clients y switches pequeños. Coinciden con el voltaje habitual de baterías de automóviles y embarcaciones.
- **Los sistemas de 48 V** sirven para montajes más grandes y coinciden con el estándar de voltaje de las centrales de telecomunicaciones. Por eso suele haber equipos de telecomunicaciones de CC usados a bajo costo.
- Muchos **switches de red y puntos de acceso** ya admiten PoE o entrada de CC. Revisa la ficha técnica antes de suponer que necesitas un inversor.

*Un montaje nativo de CC funciona más tiempo con la misma capacidad de batería que uno de CA con inversor intermedio, porque desaparecen las pérdidas propias del inversor.*

## Energía híbrida con panel solar y generador

Para despliegues que superan la autonomía de un solo paquete de baterías, combina un banco de baterías con una fuente de carga.

- **Los paneles solares portátiles con controlador de carga** funcionan bien para cargar durante el día y usar la batería por la noche en sitios con sol confiable.
- **Un generador inverter pequeño** recarga rápido y no depende del clima, pero añade logística de combustible y ruido. Esto es un problema serio en despliegues discretos o sensibles al ruido.
- **Un sistema híbrido**, con energía solar como fuente principal y un generador de respaldo, cubre los días en que el mal tiempo reduce la producción solar.

*Dimensiona el banco de baterías para al menos un día completo de autonomía sin ninguna fuente de carga.* Un plan que depende de sol continuo o reabastecimiento seguro de combustible no es resiliente.

{{< figure src="field-power-hybrid-solar-battery-generator.webp" alt="Diagrama donde un panel solar y un generador cargan un banco central de baterías, que alimenta un estuche de servidor compacto mediante distribución de CC y CA" >}}

## Química de baterías para uso en campo

No todos los paquetes de baterías son adecuados para un estuche expuesto a golpes, calor y frío de forma repetida. **La química de las celdas importa tanto como el valor en vatios-hora de la etiqueta.**

| Química | Ideal para | Compromiso |
|---|---|---|
| **LiFePO4 (fosfato de hierro y litio)** | La mayoría de los montajes de campo, larga vida de ciclos y modo de falla más seguro | Más peso por vatio-hora que otras químicas de litio |
| **Ion-litio (NMC/NCA)** | Montajes sensibles al peso, donde cada gramo importa | Menos tolerancia al calor y a la descarga profunda, vida de ciclos más corta |
| **Plomo-ácido sellada (AGM/gel)** | Montajes económicos o solución temporal si ya tienes baterías disponibles | Pesada, menor capacidad útil y vida de ciclos más corta de las tres |

**[La comparación de químicas secundarias de baterías de Battery University](https://www.batteryuniversity.com/article/bu-107-comparison-table-of-secondary-batteries) explica mejor los compromisos entre vida de ciclos y energía específica.** *LiFePO4 sobresale: tolera calor, maltrato y descarga completa mucho mejor que las otras dos químicas, justo las condiciones que enfrenta un estuche de campo.*

El calor daña cualquier química. **[La investigación de Battery University sobre pérdida de capacidad de baterías de ion-litio](https://www.batteryuniversity.com/article/bu-808b-what-causes-li-ion-to-die) documenta pérdidas reales muy superiores a los valores de laboratorio del fabricante cuando intervienen el calor y los ciclos de carga rápida.** Por la misma razón, esta serie recomienda planificar menos autonomía que la nominal en climas cálidos.

## Alimenta dispositivos por USB-C PD

Muchos thin clients, puntos de acceso y periféricos de un montaje compacto ahora aceptan energía **USB-C con la especificación [USB Power Delivery (USB PD)](https://www.usb.org/document-library/usb-power-delivery)**, lo que simplifica bastante un kit de campo.

- **Un solo banco USB PD reemplaza varios adaptadores específicos**, reduciendo la cantidad de cables y cargadores dentro del estuche.
- **Confirma la potencia que el dispositivo negocia en la práctica**, no solo la potencia máxima del cable. Una fuente PD insuficiente puede limitar el rendimiento o no cargar un dispositivo bajo carga sin señales evidentes.
- **Lleva un cable PD apto para la potencia más alta del kit.** Un cable barato, solo de carga y con capacidad de 60 W limita un dispositivo de 100 W sin una alerta clara.

*USB-C PD no reemplaza el UPS ni el dimensionamiento del banco de baterías. Es una capa práctica para periféricos pequeños, no la arquitectura eléctrica principal del estuche.*

## Supervisa el UPS en vez de adivinar

**Un UPS que pasó a batería hace una hora sin avisar no protege nada si nadie se entera antes de que se agote.** La mayoría de los UPS reportan su estado por USB o una tarjeta de red. Un montaje de campo debe leerlo en vez de asumir que todo funciona.

- **[Network UPS Tools (NUT)](https://networkupstools.org/) es un proyecto de código abierto compatible con más de mil modelos de UPS** y ofrece herramientas comunes de supervisión y control independientemente del protocolo del fabricante.
- **Activa el apagado automático y ordenado de las computadoras al alcanzar un umbral de batería definido**, en lugar de dejar que el UPS llegue a cero y corte un sistema de archivos activo.
- **Registra la salud y las tendencias de autonomía de la batería con el tiempo**, no solo el porcentaje de carga actual. Una batería que pierde capacidad gradualmente no presenta síntomas claros hasta el día de la falla.

*Un UPS sin supervisión es una batería con fecha de vencimiento desconocida.* Configurar NUT o la herramienta equivalente del fabricante toma una tarde y aporta información para cada despliegue posterior.

## Sincroniza la hora sin internet

**La hora precisa importa más en campo de lo que muchos montajes contemplan.** Afecta la correlación de registros, la validez de certificados, los intercambios de túneles cifrados y cualquier evidencia con marca de tiempo que produzca el despliegue.

- **Un servidor NTP local dentro del estuche**, sincronizado con un receptor GPS o una fuente stratum 1 cuando haya internet, mantiene todos los dispositivos en la misma hora durante las interrupciones de conectividad.
- **Los relojes sincronizados por GPS funcionan sin conexión a internet**, algo importante en los escenarios de red mesh y respaldo satelital que cubre más adelante esta serie.
- **Un reloj desfasado incluso unos minutos puede interrumpir la validación de certificados TLS y los intercambios VPN.** Lo que parece una falla de red puede ser un problema de hora que nadie pensó en revisar.

**La [especificación NTP versión 4, RFC 5905](https://www.ietf.org/rfc/rfc5905.txt), define el protocolo que implementa la mayoría de estas herramientas.** El descubrimiento dinámico de servidores permite que un pequeño servidor NTP en el estuche atienda a los demás dispositivos con poca configuración.

## Clasificaciones IP y NEMA

Dos sistemas de clasificación indican si un gabinete o dispositivo soportará el ambiente de destino. **Ninguno significa simplemente "reforzado". Ambos usan valores concretos y comprobables.**

El código **[IP (Ingress Protection)](https://en.wikipedia.org/wiki/IP_Code)**, definido por la norma IEC 60529, usa dos dígitos. El primero indica la protección contra partículas sólidas, como el polvo. El segundo indica la protección contra líquidos, como el agua.

| Clasificación IP | Significado |
|---|---|
| **IP54** | Protegido contra polvo y salpicaduras de agua desde cualquier dirección |
| **IP65** | Hermético al polvo y protegido contra chorros de agua a baja presión |
| **IP67** | Hermético al polvo y protegido contra inmersión temporal hasta 1 metro |
| **IP68** | Hermético al polvo y protegido contra inmersión continua a más de 1 metro, según la profundidad y el tiempo indicados por el fabricante |

El **[sistema NEMA de clasificación de gabinetes](https://en.wikipedia.org/wiki/NEMA_enclosure_types)**, común en equipos industriales de Norteamérica, usa números de tipo en lugar de pares de dígitos. **NEMA 3R** sirve para exposición general a la intemperie. **NEMA 4X** añade protección hermética al agua y resistencia a la corrosión para entornos costeros o de lavado. **NEMA 6P** cubre inmersión temporal.

*Elige la clasificación según la amenaza real del sitio, no el número más alto disponible.* Un gabinete IP68 para un despliegue en el desierto sin exposición al agua es un gasto innecesario. Es mejor invertir ese dinero en refrigeración o capacidad de batería.

## Temperatura, vibración y humedad

Además del polvo y el agua, tres factores ambientales dañan silenciosamente la electrónica de campo.

- **Las temperaturas extremas** acortan la vida de la batería y reducen el rendimiento o apagan los equipos. Revisa el rango de temperatura de funcionamiento de cada componente, no solo el del gabinete.
- **La vibración** afloja conectores y fatiga las uniones soldadas durante viajes repetidos. Los soportes aislantes de goma entre la bandeja del equipo y el estuche absorben las vibraciones antes de que lleguen al hardware.
- **La humedad y la condensación** aparecen cuando un estuche pasa de un vehículo frío a aire cálido y húmedo. Ante un gran cambio de temperatura, deja el estuche cerrado unos minutos antes de abrirlo. Considera un paquete desecante pequeño en gabinetes sellados.

## Puesta a tierra y protección contra sobretensiones

Las fuentes de campo, sobre todo los generadores, son más ruidosas y menos predecibles que la energía de red. **En el sitio no hay un electricista del edificio para detener una sobretensión o una falla de tierra antes de que llegue al equipo.**

- **Establece una puesta a tierra adecuada** para el estuche y los rieles metálicos del rack antes de conectar la energía. Usa una varilla de tierra o la conexión a tierra del chasis del vehículo según el caso.
- **Usa un dispositivo contra sobretensiones apto para la fuente real**, ya que los generadores pueden producir picos que no aparecen con energía de red estable.
- **Coloca el UPS entre la fuente sin acondicionar y los equipos**, nunca al revés, para que la protección del UPS reciba primero la energía más sucia.

*Omitir la puesta a tierra para ahorrar cinco minutos de instalación arriesga todo el estuche de equipo.*

## Lista de control de alimentación y ambiente

- [ ] UPS o banco de baterías dimensionado con un margen de 1,5 a 1,6 veces la potencia total de carga
- [ ] Al menos un día completo de autonomía disponible sin fuente de carga
- [ ] Clasificación IP o NEMA del gabinete ajustada a la amenaza real del sitio
- [ ] Rango de temperatura revisado para cada componente, no solo para el gabinete
- [ ] Aislamiento de vibración instalado para transporte largo o por caminos difíciles
- [ ] Puesta a tierra adecuada antes de conectar un generador u otra fuente de campo

## Próximos pasos

Con la alimentación y la protección ambiental cubiertas, la siguiente pregunta es cómo se comunica el despliegue con el exterior y protege sus datos. Continúa con la [tercera parte: conectividad y seguridad de datos para nodos edge](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/).

Si aún no la leíste, la [primera parte: selección de hardware y gabinete](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) cubre la computadora y el estuche que debe complementar este plan eléctrico. La [cuarta parte](/articles/field-it-tidbits-beyond-the-mini-datacenter/) cubre los demás detalles.
