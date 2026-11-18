---
title: "La carrera por detectar las cámaras Flock: qué cambió en 2026"
date: 2026-09-10
lastmod: 2026-11-13
toc: true
draft: false
description: "Repasa los cambios reportados en la detección de Flock Safety, las respuestas de la comunidad y los métodos infrarrojos para identificar cámaras."
genre: ["Tecnología de privacidad", "Contravigilancia", "Proyectos de código abierto", "Derechos digitales", "Seguridad de redes", "Investigación de seguridad", "Modificación de hardware", "Herramientas de privacidad"]
tags: ["Flock Safety", "ALPR", "Flock-You", "Detección de OUI", "Solicitud probe wildcard", "Modo WiFi promiscuo", "Supervisión 802.11", "DeFlockJoplin", "NitekryDPaul", "Detección BLE", "WiFi de 5 GHz", "MAC administrada localmente", "Coincidencia de patrones SSID", "Hardware de contravigilancia", "STS Collective", "colonelpanichacks", "Evasión de detección", "ESP32", "Detección WiFi", "Concienciación sobre vigilancia", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "Seguimiento de incidencias de GitHub", "Actualización de firmware", "Protección contra la huella digital del dispositivo", "Aleatorización de MAC", "Fingerprinting de elementos de información", "Salto de canales", "Defensa de la privacidad", "Seguridad de código abierto", "Vigilancia masiva", "Firmware de detección", "Detección WiFi durante la conducción", "Retirada de cámaras", "Hardware de privacidad", "Detección infrarroja", "Iluminador IR", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Detección óptica", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Escena urbana con una cámara Flock en una farola y un vehículo equipado con un dispositivo avanzado de detección. Unas señales luminosas muestran la comunicación inalámbrica sobre un fondo oscuro."
coverCaption: "Cómo los cambios de hardware de Flock Safety siguen interrumpiendo las herramientas de detección de código abierto y cómo la comunidad se pone al día"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Si tu detector Flock-You se ha quedado en silencio en una ruta donde antes detectaba cámaras cada vez, no te lo estás imaginando y probablemente el hardware no esté averiado.** El hardware y el firmware de las cámaras Flock Safety han cambiado al menos dos veces durante el último año, interrumpiendo los métodos de detección de la comunidad. Investigadores de código abierto han tenido que reconstruir una firma nueva cada vez.

*La situación cambia deprisa. El método de detección y la lista OUI que aparecen aquí reflejan la rama `main` de `colonelpanichacks/flock-you` en septiembre de 2026. Consulta el [repositorio de GitHub](https://github.com/colonelpanichacks/flock-you) antes de dar por defectuoso tu dispositivo.*

{{< youtube id="cVf-id71BuQ" >}}

*El video de Valleytech Custom Solutions muestra el síntoma descrito: un recorrido rutinario de wardriving que de pronto devuelve cero detecciones en varias versiones del firmware, aunque antes las cámaras se detectaban de forma fiable en esa ruta y algunas cámaras señaladas habían desaparecido físicamente del condado.*

______

## Un recorrido de wardriving que de pronto no detecta nada

Los informes suelen describir el mismo patrón. Una persona recorre una ruta que ya ha hecho docenas de veces. El detector lleva el firmware actual y antes encontró esas mismas cámaras. En un viaje no detecta nada: ni pitidos ni registros, con todas las compilaciones personalizadas que se probaron.

El video de Valleytech cuenta un caso parecido: el trayecto diario a la oficina de correos solía detectar al menos una cámara Flock, pero ahora ninguna. En una segunda ruta cerca de Micro Center antes aparecían cinco; ahora solo una sigue activa y las otras cuatro se arrancaron de sus postes.

**En ese mismo periodo ocurrían dos cosas que es fácil confundir:**

- **Algunas cámaras se retiran o se trasladan físicamente**, así que hay menos dispositivos que detectar.
- **La firma inalámbrica de las cámaras cambió**, por lo que una cámara aún instalada quizá no active hardware con firmware antiguo.

Dos incidencias de GitHub en el repositorio `colonelpanichacks/flock-you`, abiertas con varios meses de diferencia, documentan el segundo problema. Juntas muestran cómo la comunidad ya tuvo que evolucionar dos veces el método de detección.

______

## Incidencia #20: el punto de acceso de gestión dejó de emitir

**[La incidencia #20](https://github.com/colonelpanichacks/flock-you/issues/20)** se abrió en enero de 2026. Una persona probó el dispositivo junto a una cámara Flock conocida y registrada en DeFlock, pero no detectó nada. Durante las semanas siguientes llegaron informes similares desde Florida, Indiana, Atlanta y el Medio Oeste, con distintos equipos y antenas.

Un comentarista planteó la pregunta clave: **¿Flock había cambiado algo por su parte que interrumpió la detección para todo el mundo más o menos al mismo tiempo?**

El responsable del proyecto, colonelpanichacks, confirmó que sí. **Alrededor de diciembre de 2025, Flock desactivó el punto de acceso de gestión que emitían sus cámaras.** Ese AP era la base original de la detección inalámbrica. Cuando desapareció, la comunidad recurrió a señales Bluetooth Low Energy (BLE). Ese sustituto también dejó de funcionar de forma fiable en la primavera de 2026.

| Superficie de detección | Estado |
|---|---|
| **AP WiFi de gestión** | Desactivado por Flock, aproximadamente en diciembre de 2025 |
| **Balizas BLE** | Dejó de funcionar de forma fiable en la primavera de 2026 |
| **Enlace celular LTE** | Sigue en uso para subir datos a la nube, pero no se detecta de forma pasiva |
| **Solicitudes probe 802.11 wildcard** | Base actual de detección (véase más abajo) |

*Todo firmware personalizado basado en los antiguos métodos del AP o BLE busca una señal que las cámaras dejaron de emitir. Por eso un dispositivo que antes funcionaba se queda en silencio aunque su hardware siga bien.*

______

## El método sustituto: sondas comodín y huellas digitales de trama

El firmware actual de `flock-you` funciona en modo promiscuo 802.11 dedicado. La radio nunca transmite ni se conecta a una red. Solo escucha y cambia entre los canales WiFi 11, 6 y 1, con una permanencia de 250 milisegundos para seguir los cambios de canal de las cámaras.

**El firmware solo alerta cuando coinciden todas estas condiciones:**

1. La trama es una **solicitud probe de gestión 802.11** (tipo 0, subtipo 4).
2. El **elemento de información SSID está presente y tiene longitud 0**, lo que indica una probe wildcard en vez de una solicitud de una red concreta.
3. La dirección del transmisor (**addr2**) coincide con un prefijo OUI conocido de Flock.
4. Los demás elementos de información de la trama coinciden con el patrón de fingerprint documentado por la comunidad DeFlockJoplin, basado en la investigación de 2022 de Pintor y Atzori sobre **[fingerprinting de IE en solicitudes probe WiFi](https://ieeexplore.ieee.org/document/10001618)**.

El firmware denomina este método `wifi_wildcard_probe_ie_sig`. En las pruebas de campo, la comunidad DeFlockJoplin detectó **11 de 12 cámaras conocidas con solo 2 falsos positivos** en su ruta de prueba. Es la misma referencia verificada en campo que cita la **[guía de hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** del proyecto. El OUI de la cámara número doce se añadió después a la lista siguiente.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Cronología de la evolución de la detección de cámaras Flock: del punto de acceso WiFi de gestión a las balizas Bluetooth Low Energy y al método actual de solicitudes probe wildcard y fingerprinting de elementos de información, con una cuarta fase de nuevas SSID, 5 GHz y evasión mediante direcciones MAC" >}}

______

## La lista OUI actual

El fingerprint de wildcard probe solo se activa si la dirección MAC del transmisor coincide con un prefijo OUI que la comunidad haya confirmado en hardware Flock real. La lista la mantiene principalmente el investigador **@NitekryDPaul**. La comunidad **DeFlockJoplin** aportó el prefijo número 31 después de detectar una cámara que no aparecía en la lista original de 30.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**Esta lista no es estática.** Las notas de investigación mencionan prefijos que se probaron y luego se rebajaron: uno pertenecía a un reproductor multimedia Sony y otro era un marcador provisional que nunca coincidió con ningún dispositivo. Dos entradas tienen poca confianza. El prefijo `82:6b:f2` se conserva aunque sea una dirección administrada localmente, porque excluirlo habría eliminado en silencio una detección real confirmada por DeFlockJoplin.

**Un prefijo ya cuenta con confirmación independiente en hardware municipal.** La unidad Flock cuyas imágenes del sistema de archivos se publicaron en septiembre de 2026 llevaba la dirección MAC **`f4:6a:dd:57:46:fb`**; `f4:6a:dd` ocupa el puesto 13 de esta lista. No era un equipo de laboratorio ni una muestra comprada. Estaba montada en un poste en Wauwatosa, Wisconsin, fotografiando el tráfico. Es la confirmación más sólida obtenida hasta ahora para un prefijo de la lista.

*Si mantienes tu propio fork del firmware, obtén la lista OUI del directorio `datasets/` del proyecto original en vez de copiarla de forma fija. La lista cambia con la investigación y una copia antigua puede hacer que vuelvas a pasar por alto cámaras sin darte cuenta.*

______

## Clasificación de las señales de detección

El firmware actual se apoya sobre todo en la coincidencia OUI, que es la señal más débil de las cinco disponibles. La comunidad de **[WiFi Mothership](https://wifimothership.com/flock)** las clasifica por fiabilidad a partir de la investigación de firmware de GainSec.

| Confianza | Señal | Notas |
|---|---|---|
| **ALTA** | **ID de fabricante BLE `0x09C8`** (XUNTONG) | La huella digital más sólida. Aparece en unidades Raven y en cualquier Falcon o Sparrow con módulo de batería |
| **ALTA** | **UUID de servicios BLE Raven `0x3100` a `0x3500`** | Servicios GATT propios de Raven para GPS, energía, red, cargas y errores. Solo se activa en hardware Raven |
| **MEDIA** | **Patrón SSID WiFi `^Flock-[A-Z0-9]+$`** | Nombre predeterminado del hotspot de configuración. El firmware contiene otros SSID: `FS Ext Battery`, `Penguin` y `Pigvision` |
| **MEDIA** | **Subcadena del nombre del dispositivo BLE** | Nombres como `FS Ext Battery` aparecen en los paquetes de publicidad sin analizar datos del fabricante |
| **BAJA** | **Coincidencia de MAC y prefijo OUI** | **El método con más ruido.** Los prefijos de proveedores de componentes aparecen en miles de productos no relacionados |

*La última fila es la señal de la que más depende el firmware actual, y ese es el problema central de detectar primero por OUI.*

### Por qué la lista OUI genera tanto ruido

Los 31 prefijos anteriores no son 31 identificadores de Flock. WiFi Mothership sigue en paralelo **26 prefijos y clasifica cada uno según su propietario real**.

| Clase | Cantidad | Propietario |
|---|---:|---|
| **Flock Safety** | **1** | `B4:1E:52`, asignación IEEE a la propia empresa |
| **Módulos de batería** | 10 | Componentes de Silicon Labs en paquetes de batería extendida |
| **Módulos de cámara** | 11 | Módulos WiFi para cámaras de Liteon Technology |
| **Infraestructura de cómputo** | 4 | Raspberry Pi Foundation y Raspberry Pi Trading |

**Veinticinco de esos 26 prefijos pertenecen a proveedores de componentes**, cuyos productos aparecen en grandes cantidades de hardware ajeno. Un prefijo de Silicon Labs o Liteon aparece en productos sin relación con Flock Safety, y las placas Raspberry Pi están muy extendidas.

**Una coincidencia es un indicio, no una identificación.** Por eso importa tanto la firma wildcard probe: al combinarla con una OUI, una solicitud probe con SSID vacío eleva la confianza de una conjetura a 62 en la escala del proyecto.

*Solo `B4:1E:52` responde por sí solo a «¿es un dispositivo Flock?». Los otros 30 prefijos son indicios de apoyo.*

### Cuántas cámaras exponen un punto de acceso de configuración

Los datos de wardriving establecen un mínimo. WiFi Mothership contó **900 o más puntos de acceso Flock en WiGLE durante 2025**. Cada AP Flock corresponde a un dispositivo que emite el SSID predeterminado `Flock-XXXX`.

La cifra describe dispositivos que exponen un hotspot de configuración, no todas las instalaciones. Flock afirma tener decenas de miles de cámaras y la mayoría no emite nada que registre alguien que pase haciendo wardriving. **El mapa es una muestra, y pequeña.**

______

## Incidencia #43: nuevo patrón SSID, 5 GHz y antifingerprinting de MAC

Tres meses después de cerrar la incidencia #20 llegó un segundo informe que describe lo que parece una contramedida contra la detección, no un cambio casual de firmware. **[La incidencia #43](https://github.com/colonelpanichacks/flock-you/issues/43)**, presentada en mayo de 2026, se basa en datos de wardriving de WiGLE capturados junto a una cámara ya confirmada en DeFlock. Documenta tres hallazgos que las herramientas existentes no contemplaban.

### Hallazgo 1: otro formato SSID

El hotspot Flock documentado siempre había usado el patrón `Flock-XXXXXX`. La cámara de este informe emitía **`Flock Camera net.`**, una convención de nombres completamente distinta. Quien buscara en WiGLE con el comodín `Flock-*`, como hacían varios investigadores, no obtendría resultados para esa cámara aunque estuviera transmitiendo.

### Hallazgo 2: punto de acceso de configuración de 5 GHz confirmado

La misma cámara transmitía simultáneamente en el **canal 1 de 2,4 GHz** y en el **canal 157 de 5 GHz**, con direcciones MAC consecutivas en cada banda (`...9f:a2:de` y `...9f:a2:df`). Esto apunta a un único módulo WiFi de doble banda que asigna direcciones adyacentes a cada radio, no a dos dispositivos sin relación. El investigador nsm_barii ya había registrado por separado una solicitud probe Flock en el canal 149 de 5 GHz. Ahora hay dos datos que confirman que el uso de 5 GHz es real.

**Todos los métodos de detección descritos antes en este artículo, incluido el firmware actual de wildcard probe, solo escuchan en 2,4 GHz.** Una cámara que transmita únicamente o sobre todo en 5 GHz es invisible para ese hardware, sin importar la precisión de la lista OUI.

### Hallazgo 3: direcciones MAC administradas localmente en el punto de acceso

Ambas direcciones MAC capturadas tienen activado el **bit de administración local**, así que no pertenecen al bloque OUI de Flock registrado en IEEE. La lógica estándar de detección de `flock-you` omite expresamente esas direcciones porque así filtra teléfonos y portátiles que aleatorizan su MAC.

**Ese filtro reduce falsos positivos, pero también descarta una cámara Flock que use una MAC administrada localmente en su interfaz de hotspot.** Los últimos bytes consecutivos de las direcciones capturadas descartan la generación aleatoria y sugieren una asignación estructurada.

| Hallazgo | Qué sigue funcionando |
|---|---|
| **Nuevo formato SSID** (`Flock Camera net.`) | La coincidencia por patrón SSID funciona si se amplía el patrón |
| **Operación en 5 GHz** | Nada del firmware WiFi actual, que solo examina 2,4 GHz |
| **MAC administrada localmente** | La coincidencia por patrón SSID, que no depende de la dirección MAC |

*La coincidencia por SSID es el único método de la tabla que sigue funcionando con independencia de la banda o de cómo se asigne la dirección MAC. Es el argumento práctico para admitir patrones SSID más amplios en vez de depender solo de la coincidencia OUI.*

______

## ¿Flock está evadiendo la detección deliberadamente?

Ninguna de las dos incidencias de GitHub demuestra intención. El propio autor de la incidencia #43 la planteó como pregunta abierta: ¿ocurre esto en todas las instalaciones de Flock o solo en una versión de firmware de una cámara?

Pero observa el patrón conjunto de ambas incidencias. Una superficie de detección deja de funcionar, la comunidad encuentra un sustituto y sus puntos ciegos (solo escaneo de 2,4 GHz, coincidencias OUI y exclusión de MAC administradas localmente) coinciden con las propiedades que podrían aprovechar un SSID nuevo, una radio de 5 GHz y una MAC administrada localmente. **Podría ser una coincidencia producida por un ciclo de actualización de firmware sin relación. También podría tratarse de un proveedor que reduce su presencia inalámbrica, dificultando la detección de terceros como efecto secundario, intencional o no.**

*La postura más útil no es decidir cuál explicación es correcta. Construye sistemas de detección que no dependan de una sola suposición, porque en los dos años de historia de este proyecto ninguna se ha mantenido válida para siempre.*

### Confirmación visual: encendida, pero sin transmitir

**[Un tercer video corto de Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) comprueba la explicación de que quizá retiraron la cámara.**

{{< youtube id="sjI8FB0cLk0" >}}

El creador volvió de noche a la misma cámara del primer video y confirmó visualmente que los **LED infrarrojos seguían encendidos**. La unidad tenía alimentación e iluminaba la escena para la captura nocturna. Al mismo tiempo, **todos los firmwares personalizados que probaron registraron cero detecciones legítimas**. Saltó una alerta, pero era un falso positivo confirmado. La cámara no estaba transmitiendo nada por el lado inalámbrico.

**Esto permite distinguir claramente las dos explicaciones posibles.** Que hayan arrancado o trasladado la cámara no explica una unidad visiblemente encendida e iluminando de noche. Una cámara activa e iluminada que permanece en silencio ante todos los métodos de detección WiFi indica que desapareció su firma inalámbrica, no el hardware.

Después de hablar con otros desarrolladores que investigaban el mismo problema, el creador dijo que no era un caso aislado. **Varias personas observaron el mismo patrón aproximadamente al mismo tiempo**, lo que apunta a un cambio coordinado a escala nacional por parte de Flock, no a una anomalía local. *Es una afirmación anecdótica, basada en conversaciones informales y no en un conjunto de datos publicado. Aun así, encaja con los periodos de diciembre de 2025 y la primavera de 2026 descritos en la incidencia #20, y merece una nueva incidencia de GitHub.*

______

## Qué significa esto para tus dispositivos de detección

Si tu dispositivo se ha quedado en silencio, revisa esta lista antes de concluir que está averiado:

1. **Actualiza primero el firmware.** Si usas algo anterior a la rama `main` actual, quizá sigas buscando el AP de gestión desactivado o balizas BLE que ya no son fiables. Descarga el firmware más reciente y vuelve a instalarlo.
2. **Confirma que la cámara sigue ahí.** Algunos informes de cero detecciones resultaron ser cámaras realmente arrancadas o trasladadas, no fallos de detección. Compara con **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** o **[DeFlock](https://deflock.org/)** antes de diagnosticar tu dispositivo.
3. **Reduce la velocidad en las intersecciones.** Si la radio permanece 250 ms por canal, un paso rápido puede dejarte atrás antes de que llegue al canal correcto. Parar entre 30 y 60 segundos detecta más cámaras que pasar deprisa con una antena más grande.
4. **Informa de lo que observas.** Cero detecciones junto a una cámara confirmada visualmente es el tipo de dato que dio lugar a las incidencias #20 y #43. Abre una incidencia nueva en vez de suponer que alguien ya la reportó.
5. **Ten presentes los límites actuales.** El firmware que solo usa WiFi a 2,4 GHz no detectará una cámara que pase a 5 GHz o deje de emitir en las bandas que examina. Esa es una brecha real, no un fallo de tu compilación.

**Esto no vuelve inútil el hardware.** La lista OUI y la firma wildcard probe aún detectan la mayoría de las cámaras instaladas. Considera cualquier detector, propio o comprado, una instantánea de una carrera continua, no una solución permanente.

{{< stscollective-ad "flockyou" >}}

______

## Un enfoque paralelo: detectar el destello infrarrojo en vez de la señal WiFi

La detección inalámbrica no es el único frente de esta carrera. **[Otro video de seguimiento](https://www.youtube.com/shorts/mzpr6bslsYA) del mismo creador, Valleytech Custom Solutions, describe un enfoque totalmente distinto**: observar el iluminador infrarrojo de la cámara en vez de escuchar una firma de radio.

{{< youtube id="mzpr6bslsYA" >}}

La mayoría de las cámaras ALPR, incluidas las de Flock, usan **iluminación infrarroja para captar matrículas legibles por la noche**, por el mismo motivo que las cámaras de seguridad normales ven en la oscuridad. La luz IR es invisible al ojo humano, pero la capta un sensor de imagen sin filtro de corte infrarrojo. *Ese detalle, la ausencia del filtro IR, convierte un módulo de cámara corriente en un detector Flock.*

### Aspecto del prototipo

El método documentado en el video pasó por varias iteraciones antes de llegar a una combinación funcional:

- **Primer intento**: receptores con fotodiodos IR dedicados. Funcionaban, pero los componentes eran demasiado caros para un proyecto DIY práctico.
- **Segundo intento**: **Jetson Nano con un módulo de cámara Raspberry Pi**. Demostró que el concepto funcionaba, pero el coste y el consumo lo hacían poco práctico para un equipo portátil o instalado en un vehículo.
- **Versión actual**: **módulo de cámara ESP32 sin lente con filtro IR**. El creador probó **ESP32-CAM** y **M5Stack S3 Cam** antes de elegir **Seeed Studio XIAO ESP32S3 Sense**, junto con un **módulo GNSS Seeed XIAO basado en el chip Quectel L76K** para añadir etiquetas GPS a las detecciones. Usa el mismo patrón de wardriving GPS que el panel WiFi de `flock-you`.

| Requisito | Por qué importa |
|---|---|
| **Módulo de cámara sin filtro IR** | El filtro que da colores naturales a las fotos normales también bloquea la luz que este método necesita captar |
| **Una cámara en lugar de un fotodiodo** | Los receptores fotodiodo capaces de aislar la señal eran demasiado caros para una solución DIY práctica |
| **Registro GPS** | Asocia las detecciones a una ubicación, como el panel Flask del firmware WiFi |

### Patrón de parpadeo de la cámara

El método depende de que el iluminador emita destellos repetidos y detectables en vez de permanecer encendido. El creador indicó una **medición propia de unos 20 milisegundos encendido y 80 apagado, un periodo de 100 milisegundos, es decir, un ciclo de trabajo del 20 % a 10 Hz**. Aclaró que la cifra no está verificada y podría ser incorrecta. *Tómala como punto de partida para tus propias mediciones, no como especificación confirmada. Flock no la ha publicado y el creador tampoco afirmó tener certeza.*

### Estado del proyecto

**Es un prototipo inicial solo para DIY, no un producto terminado.** El creador describió el software como «vibe coded» y aún en desarrollo. Tiene previsto añadir un zumbador para avisos sonoros, pero todavía no lo ha hecho. Tampoco existe una placa lista para usar equivalente a OUI-SPY. La versión actual todavía requiere que **una persona confirme visualmente** si una detección señalada es una cámara real y no otra fuente de luz IR. Por eso sirve como herramienta de cribado, no como sistema totalmente automático.

*Esta superficie de detección es distinta de las demás del artículo. No depende de WiFi, de 2,4 o 5 GHz, de coincidencias OUI ni del comportamiento de las direcciones MAC, así que las técnicas de evasión de la incidencia #43 no la afectan. También tiene límites propios: línea de visión, interferencias de la luz diurna y un ciclo de trabajo que nadie ha confirmado de forma independiente.*

______

## Qué está haciendo la comunidad

La respuesta a ambas incidencias siguió el patrón que ha mantenido útil este proyecto durante dos años: alguien informa de una brecha, otra persona aporta una corrección y esta se publica en una actualización en vez de quedar en una lista de tareas pendientes.

- **La incidencia #20** terminó con una causa confirmada y una reescritura del firmware en torno a la firma wildcard probe, basada en la investigación de campo de la comunidad DeFlockJoplin.
- **La incidencia #43** sigue abierta al redactar este artículo; la sugerencia de añadir coincidencia por patrón SSID aún no se ha aplicado. *Añadir `Flock Camera` como patrón adicional es una contribución pequeña y bien delimitada para quien conozca la lógica de coincidencia del firmware.*
- El conjunto de datos OUI tiene versiones y fechas. Las entradas degradadas y las de baja confianza quedan documentadas en lugar de desaparecer sin explicación, para que cualquiera que bifurque el proyecto sepa qué cambió y por qué.

*Esta es la ventaja práctica de las herramientas de detección de código abierto frente a una alternativa cerrada. Quien detecta una brecha no puede corregir un detector propietario. Este proyecto ya se ha corregido dos veces.*

______

## La otra respuesta: retirar los dispositivos

La detección inalámbrica es una respuesta a estas cámaras. Otra iniciativa actuó sobre el propio hardware y, en septiembre de 2026, produjo las pruebas públicas más detalladas sobre el funcionamiento interno de una cámara Flock.

**El colectivo stegan0gram retiró una cámara de su poste, copió el almacenamiento interno y publicó las imágenes del sistema de archivos a través de Distributed Denial of Secrets.** Describió el trabajo así:

> «¿Por qué destruirlas sin más, si podemos aplicar ingeniería inversa y descubrir los secretos de quienes nos espían? Liberamos el hardware en el campo, lo desarmamos y luego aplicamos ingeniería inversa a las cámaras y a los equipos solares asociados».

*La diferencia importa. Destruir una cámara elimina una unidad. La ingeniería inversa aporta pruebas sobre todas ellas.*

### Qué reveló la retirada

El conjunto de datos publicado incluye una **partición multimedia de 18 GB**, una **imagen del sistema Android de 1,5 GB** y una **partición de credenciales de 32 MB**, además de la clave recuperada para el contenedor multimedia cifrado. Los investigadores establecieron las versiones del sistema operativo y del kernel, y encontraron credenciales de backend codificadas en el firmware y tokens de autenticación en texto sin cifrar que guarda la cámara.

Estas pruebas respaldan la investigación de seguridad de **[Vulnerabilidades en las cámaras Flock Safety: más de 50 fallos detectados](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**, que antes se basaba en dispositivos de laboratorio y unidades compradas.

### La respuesta a las retiradas

Las intervenciones físicas tienen consecuencias y el panorama es variado:

- **Han detenido a varias personas en todo el país** por presuntamente manipular o sabotear cámaras Flock.
- **Algunos municipios anunciaron que dejarían de usar cámaras Flock**, que es el resultado que buscan sus opositores.
- **Un departamento de policía construyó una carcasa falsa de una cámara Flock impresa en 3D** para atraer a posibles vándalos y detenerlos.

Noel Pichardo, expolicía de Pawtucket, Rhode Island, se convirtió en crítico de Flock tras cuestionar el uso de las cámaras por parte de su departamento. Dijo a WIRED que entiende la frustración, pero teme que el sabotaje convenza a la policía y al gobierno de que esa tecnología es necesaria. «Cuanto más tiempo ignore el gobierno las quejas de los residentes que se oponen a este tipo de vigilancia, más veces ocurrirá», dijo.

### Dónde encaja la detección

La retirada no cambia el problema de detección que trata este artículo. La cámara sigue transmitiendo, el firmware sigue necesitando su lista OUI y su firma probe, y los dos fallos documentados siguen vigentes.

La extracción confirma **la identidad del hardware**, incluido un prefijo OUI verificado en una unidad real, y recuerda qué tipo de presión cambia las instalaciones. **Las cámaras desaparecen de una ruta porque un ayuntamiento cancela un contrato, no porque un detector se quede en silencio.** Las herramientas inalámbricas responden a una pregunta personal sobre tu entorno. El debate político responde a la pregunta más amplia, y la extracción aportó las pruebas más sólidas hasta ahora.

______

## Conclusión: la detección es un objetivo cambiante

Que un detector se quede en silencio en una ruta donde antes encontraba cámaras no demuestra que el hardware haya fallado. Indica que la firma inalámbrica que debía reconocer volvió a cambiar, por segunda vez en un solo año. **El AP de gestión, las balizas BLE y quizá ahora las suposiciones de solo 2,4 GHz y solo OUI integradas en el firmware actual** han tenido una vida útil limitada.

**La solución nunca fue abandonar la detección inalámbrica.** Consistía en mantener visibles y documentadas sus suposiciones para poder corregirlas cuando aparezca un informe como las incidencias #20 o #43. Esa es la ventaja del firmware de código abierto: la comunidad puede cerrar la brecha en cuanto la encuentra, sin esperar al proveedor.

### Puntos clave

- **Ya han desaparecido dos superficies de detección documentadas**: el AP WiFi de gestión (desactivado alrededor de diciembre de 2025) y las balizas BLE (poco fiables desde la primavera de 2026).
- **El método actual, solicitudes probe wildcard junto con coincidencia OUI y fingerprinting de IE, detectó 11 de 12 cámaras en pruebas de campo**, pero solo funciona por WiFi a 2,4 GHz.
- **Un informe pendiente describe un formato SSID nuevo, un hotspot de 5 GHz confirmado y MAC administradas localmente** que el método actual, limitado a OUI y 2,4 GHz, no puede detectar.
- **Está surgiendo un enfoque diferente, sin conexión inalámbrica**: un módulo de cámara ESP32 sin filtro IR detecta el iluminador infrarrojo de Flock y evita las técnicas de evasión inalámbrica descritas.
- **La confirmación visual respalda el silencio inalámbrico**: una cámara estaba encendida e iluminaba de noche, pero registró cero detecciones WiFi válidas. En ese caso concreto, la retirada no explica el silencio.
- **Cero detecciones junto a una cámara conocida no significa automáticamente que tu hardware esté averiado.** Actualiza primero el firmware y luego confirma que la cámara sigue allí.
- **El proyecto de código abierto publica correcciones cuando la comunidad encuentra brechas.** Lee las incidencias de GitHub, además del README, para conocer el estado actual.

### Próximos pasos

1. **Actualiza el firmware** a la rama `main` actual antes de investigar otros problemas: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Lee la guía completa del hardware** si aún no la conoces: **[Proyecto de detección Flock-You: guía de hardware de contravigilancia](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Compara las posibles zonas sin detección** con **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** antes de concluir que tu dispositivo no vio algo.
4. **Entiende a qué te enfrentas**: **[Vigilancia con cámaras Flock Safety: alcance, problemas de privacidad y estrategias de protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Combina la detección WiFi con la detección celular** mediante **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)** para tener una visión más completa. Ninguno de los métodos de este artículo detecta simuladores de estaciones base celulares.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra dispositivos FlockYou listos para usar y ahorra un 20 %
{{< /centerbutton >}}

______

## Artículos relacionados

| Artículo | Contenido |
|---|---|
| **[Proyecto de detección Flock-You: guía de hardware de contravigilancia](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guía técnica de tres plataformas de hardware, configuración del firmware y método de detección de este artículo |
| **[Flock Finder: localiza en un mapa las cámaras Flock sospechosas cerca de ti](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Compara una posible zona sin detección con más de 40 000 ubicaciones de cámaras registradas antes de diagnosticar tu equipo |
| **[Cámaras Flock: herramienta de seguridad pública o máquina de vigilancia sin orden judicial?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Análisis de lo que permite la base de datos y por qué importa más la cuestión de las órdenes judiciales que la detección |
| **[Vigilancia con cámaras Flock Safety: alcance, problemas de privacidad y estrategias de protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Escala de despliegue, casos documentados de abuso y recursos para la organización comunitaria |
| **[Vulnerabilidades en las cámaras Flock Safety: más de 50 fallos detectados](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Investigación de seguridad del hardware y el software, distinta de la detección inalámbrica |
| **[Cómo instalar firmware en dispositivos Rayhunter: guía completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detecta IMSI catchers y stingrays, el equivalente celular de la brecha WiFi descrita aquí |

______

## Referencias

1. [Repositorio de GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Incidencia #20 de GitHub - No se detectan cámaras Flock, pero sí otros dispositivos](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [Incidencia #43 de GitHub - ¿Señal de 5 GHz? Nuevo OUI y filtrado de direcciones MAC](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [Conjunto de investigación OUI de NitekryDPaul](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - Investigación comunitaria de ALPR](https://deflockjoplin.today)
7. [Pintor, L. y Atzori, L. (2022) - Análisis de solicitudes probe WiFi para el fingerprinting de elementos de información, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED y 404 Media - Hackers entraron en una cámara Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - Las cámaras Flock están plagadas de vulnerabilidades y credenciales codificadas](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - Imágenes del sistema de archivos de una cámara ALPR Flock](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - Esta semana en seguridad: las cámaras Flock son antiguas, parches de Microsoft e investigadores atacan SSH](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - Referencia de dispositivos y detección ALPR de Flock Safety](https://wifimothership.com/flock)
13. [GainSec - Investigación de firmware y avisos de seguridad](https://gainsec.com/)
14. [The Hunt for the Hidden Probe - Comportamiento de wildcard probes con SSID ocultas](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
15. [DeFlock - Mapa comunitario de cámaras ALPR](https://deflock.org/)
16. [Colonel Panic Tech - OUI-SPY y hardware de detección](https://colonelpanic.tech)
17. [STS Collective - Dispositivos FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
18. [Está pasando algo extraño con las cámaras Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
19. [Wardriving infrarrojo para detectar cámaras Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
20. [Las cámaras Flock siguen encendidas, pero no transmiten - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
21. [Reconocimiento automático de matrículas - Wikipedia (iluminación infrarroja en sistemas ANPR/ALPR)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
22. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
23. [Módulo GNSS L76K para Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)
