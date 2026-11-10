---
title: "SenseCAP M1 Raspberry Pi Shield: pinout y reutilización para LoRaWAN"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "Conoce el shield SenseCAP M1, compara mapas GPIO contradictorios, examina su ATECC608 y planifica una puerta de enlace LoRaWAN con una versión moderna de Raspberry Pi OS."
genre: ["Raspberry Pi", "IoT", "Seguridad de hardware"]
tags: ["SenseCAP M1", "Shield SenseCAP M1", "Pinout SenseCAP M1", "Shield Raspberry Pi", "Raspberry Pi HAT", "Puerta de enlace LoRaWAN", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Reutilización de hotspot Helium", "Concentrador LoRa", "SPI GPIO", "GPIO17", "LED GPIO22", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "Diagnóstico I2C", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "Ingeniería inversa de hardware"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Shield SenseCAP M1 con módulo Seeed WM1302, conector Raspberry Pi, cable de antena, toma USB-C y conector de ventilador"
coverCaption: "Foto de la placa: Clockwork Bird, 2023. La fuente y la atribución aparecen al final."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**El shield SenseCAP M1 es útil como hardware de puerta de enlace LoRaWAN, pero su cableado requiere más comprobaciones que las que ofrece un tutorial genérico de HAT para Raspberry Pi.** Esta guía amplía [la investigación de Clockwork Bird de 2023](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) con documentación del fabricante, una revisión del controlador upstream y recomendaciones GPIO actuales. Identificarás el hardware, separarás los hechos confirmados de los datos incompletos del pinout y crearás un registro de puesta en marcha reproducible.

> **Alcance:** Esta es una guía de hardware basada en documentación. No se probaron sus comandos ni los mapas de la placa en un M1 físico.

## Puntos clave

- **Identifica ambas placas:** El carrier M1 y el concentrador extraíble tienen datos de modelo y revisión independientes.
- **Audita los scripts de reinicio:** Los valores predeterminados de CoreCell entran en conflicto con señales del pinout M1 publicado.
- **Comprueba las interfaces del sistema operativo:** Los archivos de dispositivo SPI, la numeración GPIO y las versiones de las herramientas GPIO responden preguntas distintas.
- **Protege el aprovisionamiento del elemento seguro:** Leer datos del dispositivo no equivale a configurarlo ni a generar claves.
- **Comprueba toda la ruta:** Detectar un concentrador no demuestra que se entreguen los datos del sensor.

## Antes de empezar

**Dificultad: intermedia.** Calcula entre una y dos horas para inventariar el equipo, preparar el sistema operativo y revisar la documentación. La verificación eléctrica, la adaptación del controlador y el despliegue del servidor de red requieren trabajo adicional, sobre todo si no conoces la revisión de la placa.

| Elemento | Propósito |
|---|---|
| **Shield M1 y concentrador** | Leer la revisión del carrier y la etiqueta completa del módulo |
| **Raspberry Pi 4** | Empezar con el anfitrión usado en el diseño M1 original |
| **Tarjeta microSD de repuesto** | Preparar otro sistema operativo y conservar la instalación original |
| **Fuente y antena adecuadas** | Ajustarse al conjunto y a la banda RF del módulo |
| **SSH o consola local** | Registrar diagnósticos y editar la configuración |
| **Sensor y servidor LoRaWAN** | Verificar la entrega real a la aplicación tras la puesta en marcha |
| **Multímetro y experiencia con hardware** | Resolver conexiones no documentadas antes de accionarlas |

Fotografía ambos lados del conjunto apagado antes de desmontar nada. Anota la orientación de los conectores, tornillos, separadores y recorrido de la antena. Conserva la tarjeta y la configuración originales hasta que la instalación nueva supere las comprobaciones de aceptación.

## Identifica las tres capas

**El M1 completo, el shield carrier y el concentrador son componentes distintos.** Seeed describe el hotspot montado como un Raspberry Pi 4 con un concentrador WM1302/SX1302 o WM1303/SX1303. Un anuncio titulado «SenseCAP M1 shield» no confirma cuál de esas piezas incluye el carrier. [Descripción general del M1 de Seeed Studio](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

El **carrier** conecta la alimentación y las señales periféricas entre el Pi y el módulo. El **concentrador** gestiona la recepción y transmisión de radio. Un **reenviador de paquetes** se ejecuta en el anfitrión e intercambia paquetes de radio recibidos y enlaces descendentes programados con un servidor. [Descripción general del HAL SX1302 de Semtech](https://github.com/Lora-net/sx1302_hal)

Por ejemplo, un sensor de temperatura de estantería envía un enlace ascendente por radio. El concentrador lo recibe, el anfitrión lo reenvía y los servicios de red y aplicación lo procesan. Que Linux arranque solo demuestra la parte del anfitrión de esta cadena.

La foto de Clockwork Bird muestra un carrier M1 v1.1 con un módulo etiquetado explícitamente como `WM1302-SPI-EU868`. Usa la imagen para localizar las etiquetas en tu equipo. Los números de serie identifican el equipo fotografiado, no la configuración de otra puerta de enlace.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Carrier M1 verde con módulo WM1302 SPI EU868 etiquetado, junto a USB-C, botón, conector de ventilador y cable de antena" caption="Hardware M1 v1.1 fotografiado por Clockwork Bird, también usado en la portada" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Conexiones de alimentación y radio

**Trata el conector USB-C del M1 como una entrada de alimentación.** El fabricante especifica 5 V CC y 3 A para toda la puerta de enlace, e identifica USB-C como interfaz de alimentación. Llamarlo puerto de carga sugiere una batería que esas especificaciones no describen. [Especificaciones del SenseCAP M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

El diagrama de bloques del fabricante separa la fuente de 5 V del riel regulado de 3,3 V del módulo. Esta diferencia importa al diagnosticar problemas: un Pi en marcha puede coexistir con un concentrador sin alimentación. No inyectes 5 V en un pin de señal ni supongas que las dos entradas de alimentación están aisladas.

**Las variantes SPI y USB requieren conexiones distintas al anfitrión.** La documentación WM1302 de Seeed describe acceso SPI directo para el modelo SPI y un puente USB STM32L4 para el modelo USB. La forma mini-PCIe describe el formato del módulo, mientras que sus interfaces eléctricas documentadas son SPI o USB. Que encaje en una toma de portátil no demuestra compatibilidad. [Documentación WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc)

Antes de alimentar el conjunto, instala el módulo con la alimentación desconectada y conecta una antena adecuada. Haz coincidir el hardware RF, la antena y el plan regional previsto. Cambiar el nombre de un archivo de configuración no cambia los componentes RF, y la toma de alimentación M1 no demuestra compatibilidad con una variante USB.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Diagrama que conecta Raspberry Pi 4 al shield M1 mediante alimentación, SPI, GPIO e I2C" caption="Diagrama del fabricante SenseCAP reproducido en el artículo original de Clockwork Bird, con el diseño WM1302" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Lee el pinout con atención

**Registra los números GPIO BCM y los pines físicos del conector en columnas separadas.** Por ejemplo, BCM GPIO17 corresponde al pin físico 11 del conector Pi. El conector de borde del módulo introduce un tercer sistema de numeración, por lo que su número de pin de reinicio no es un GPIO de Raspberry Pi.

La tabla siguiente transcribe las conexiones de la imagen anotada de Clockwork Bird. Es una **referencia comunitaria**, no un esquema completo del fabricante ni una medición de todas las revisiones M1. El dibujo también usa etiquetas `SX1262`, mientras que el script genérico de reinicio de Semtech usa nombres `SX1261`.

| Señal del dibujo | BCM / pin físico | Interpretación |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Bus de gestión compartido |
| **Reinicio SX1302** | GPIO17 / 11 | Candidato a reinicio del concentrador |
| **LED de usuario** | GPIO22 / 15 | Anotación M1 |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | Señales de datos SPI |
| **Reloj SPI** | GPIO11 / 23 | Señal de reloj SPI |
| **Selección SX1302** | GPIO8 / 24 | SPI0 CE0 |
| **Reinicio SX1262** | GPIO5 / 29 | Candidato a reinicio de radio auxiliar |
| **Selección SX1262** | GPIO6 / 31 | GPIO6, distinto de SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Salida de estado de radio auxiliar |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Señales auxiliares que se deben verificar antes de usar |

Las anotaciones GPS/UART tachadas no demuestran que el M1 incluya GPS. No añadas configuración GPS salvo que tu hardware lo tenga. El diagrama publicado tampoco resuelve el botón de usuario ni el control del ventilador. [Investigación del pinout de Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Dibujo anotado del conector Raspberry Pi con LED M1, reinicio del concentrador, señales SPI y conexiones GPS tachadas" caption="Referencia anotada por la comunidad, con cobertura de revisiones sin resolver, no es un esquema M1 completo" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Resuelve los conflictos de los scripts de reinicio

**Un script de reinicio selecciona salidas eléctricas, no simples preferencias de software.** El `reset_lgw.sh` upstream de Semtech se dirige al diseño de referencia CoreCell. Sus valores predeterminados incluyen GPIO23 para reiniciar el concentrador, GPIO18 para activar la alimentación, GPIO22 para reinicio auxiliar y GPIO13 para reiniciar un AD5338R. [Código del script de reinicio de Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Las instrucciones antiguas de Seeed cambian las dos asignaciones de reinicio a GPIO17 y GPIO5, pero mantienen las otras entradas del diseño de referencia. Compara esos valores con la imagen anotada M1 antes de seguir el ejemplo. [Instrucciones de instalación WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc)

| Asignación | Evidencia en conflicto | Decisión necesaria |
|---|---|---|
| **GPIO22 como reinicio auxiliar** | La imagen M1 lo identifica como LED de usuario | Elimina esta suposición antes de activar el LED |
| **GPIO18 como activación de alimentación** | La imagen M1 lo identifica como BUSY auxiliar | Verifica el net y su dirección antes de accionarlo |
| **GPIO13 como reinicio de DAC** | El script genérico nombra otro diseño de referencia | Determina si existe el circuito |
| **Dispositivo SPI auxiliar** | La imagen M1 selecciona GPIO6 en vez de CE1 | Confirma el enrutamiento de selección y el soporte del controlador |

**Inferencia:** Si GPIO18 se conecta a una salida de radio auxiliar como indica el dibujo, configurar el extremo Pi como salida crea riesgo de contención eléctrica. La discrepancia establece la necesidad de verificar, no demuestra daños ni un mapa de cableado universal para todos los M1.

Desconecta toda la alimentación y traza las conexiones accesibles entre el conector y el módulo. Anota la revisión de la placa y ambos extremos. Una prueba de continuidad demuestra conectividad; la documentación de componentes establece la dirección de señal y los límites eléctricos.

Usa el diagrama del módulo siguiente para no confundir los pines del conector de borde con los del Pi. Las etiquetas de radio auxiliar describen la referencia publicada del módulo, no demuestran que todas las revisiones usen el mismo silicio o admitan las mismas funciones. [Pinout del módulo WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Diagrama Seeed que etiqueta ambos lados del conector de borde del WM1302 con alimentación, SPI, I2C y señales de radio auxiliar" caption="La numeración del conector de borde del módulo difiere de la numeración del conector Raspberry Pi" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Prepara Raspberry Pi OS

Registra el entorno del anfitrión en la instalación de repuesto:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

La versión del sistema, el kernel y el modelo Pi forman el punto de partida reproducible. Regístralos antes de comparar resultados con un tutorial antiguo.

Instala herramientas de inspección y compilación:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

En **Interface Options**, activa SPI e I2C y reinicia. SPI sirve para la ruta del concentrador e I2C para los dispositivos de gestión descritos más adelante. No importes cambios de puerto serie GPS sin relación con este equipo desde un tutorial de otro HAT.

Inspecciona las interfaces expuestas:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

Estos comandos enumeran nodos de dispositivo, adaptadores, controladores GPIO, líneas y la versión de la herramienta GPIO instalada. **`i2cdetect -l` enumera adaptadores sin escanear direcciones.** El archivo `/dev/spidev0.0` demuestra que hay una interfaz SPI expuesta, no que se comunique con un concentrador operativo. [Manual de i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Guía GPIO de Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### Ten en cuenta las versiones GPIO

**No copies números GPIO globales de otra máquina.** Los scripts antiguos escriben mediante `/sys/class/gpio`, una interfaz obsoleta según la documentación del kernel. Las integraciones nuevas en espacio de usuario deben usar la interfaz de dispositivo de caracteres GPIO con el controlador y el desplazamiento de línea correctos. [Documentación GPIO de Linux](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

También inspecciona `gpioset --help` antes de adaptar un script. La sintaxis y el comportamiento de procesos difieren entre las versiones 1 y 2. La herramienta actual mantiene las líneas solicitadas de forma predeterminada, pero el contrato portable no garantiza su estado después de que termina el proceso. [Documentación gpioset de libgpiod](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi documenta un comportamiento de persistencia de salida en su kernel y opciones para cambiarlo. Registra la configuración real del kernel en vez de suponer que todos los Linux se comportan igual. La numeración actualizada y una herramienta más nueva no corrigen un mapa eléctrico incorrecto. [Guía de uso GPIO de Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## Prueba el LED de usuario

Después de comprobar que GPIO22 pertenece al LED y eliminar consumidores GPIO en conflicto, edita la configuración de arranque:

```bash
sudoedit /boot/firmware/config.txt
```

Las versiones modernas de Raspberry Pi OS montan la configuración de arranque en **`/boot/firmware/config.txt`**. Las imágenes antiguas usan `/boot/config.txt`, la ruta del artículo de 2023. Haz una copia del archivo activo antes de editarlo. [Documentación config.txt de Raspberry Pi](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Añade el overlay LED bajo una sección aplicable a tu Pi, como `[all]`:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

El parámetro **`gpio`** usa la numeración BCM. **`label`** nombra el dispositivo LED Linux y **`trigger=heartbeat`** asigna el disparador de latido del kernel. Clockwork Bird informa de esta asignación para el M1, y la referencia de overlays de Raspberry Pi documenta estos parámetros. [Observación original del LED](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [Referencia del overlay gpio-led](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Después de reiniciar, inspecciona el LED registrado:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

El resultado esperado es una entrada LED `lorawan` con `heartbeat` seleccionado entre corchetes. Un LED parpadeante demuestra esta ruta GPIO/controlador. No informa de registro LoRaWAN, recepción de radio ni estado Helium.

## Investiga los dispositivos I2C

**Una dirección I2C es una pista, no la identidad del dispositivo.** Clockwork Bird observó respuestas en `0x60` y `0x39`, y luego leyó información ATECC608 con la biblioteca criptográfica. La identificación del sensor de temperatura seguía siendo tentativa en el artículo original.

Empieza por la lista de adaptadores de la sección anterior. Los escaneos amplios de `i2cdetect` envían transacciones de sondeo, no observan pasivamente el tráfico, y el manual upstream advierte de posibles interrupciones. Evita escanear de forma rutinaria una puerta de enlace activa o dispositivos conectados desconocidos. [Comportamiento de sondeo de i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Observación | Conclusión respaldada | Pregunta pendiente |
|---|---|---|
| **Respuesta en `0x60`** | Algo reconoció el sondeo | ¿Es el elemento seguro esperado? |
| **Respuesta en `0x39`** | Algo reconoció el sondeo | ¿Qué componente y revisión respondieron? |
| **`UU` en un escaneo** | Un controlador posee la dirección y se omitió el sondeo | ¿Qué controlador la usa? |
| **Sin respuesta** | El sondeo no recibió confirmación | ¿Alimentación, bus, propietario o protocolo? |

### Afina la pista del sensor de temperatura

**STTS751 es una opción para `0x39` respaldada por fuentes.** El encabezado del controlador de temperatura de Semtech asocia explícitamente `0x39` con `STTS751-0DP3F`. Esto refuerza la hipótesis original, pero no identifica todos los componentes montados en esta dirección. [Encabezado del controlador STTS751 de Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

Después de identificar un componente compatible y confirmar que ningún otro proceso lo usa, estos comandos leen sus registros de identificación:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

Aquí **`1`** selecciona el bus verificado, **`0x39`** el dispositivo y **`b`** solicita una lectura SMBus de datos de byte. Para STTS751-0, el ID de producto documentado en `0xFD` es `0x00`, y el ID del fabricante en `0xFE` es `0x53`. Estas transacciones seleccionan direcciones de registro, pero no escriben valores de configuración. [Ficha técnica STTS751, mapa y registros de identificación](https://www.st.com/resource/en/datasheet/stts751.pdf)

Compara las lecturas con la marca del chip y su documentación. Un par coincidente aporta pruebas para identificarlo; si hay un error, comprueba el bus y su propietario antes de cambiar la configuración del hardware. El sensor mide su temperatura local, distinta de la temperatura de la CPU del Pi.

## Inspecciona el elemento seguro

**El ATECC608 es un componente de autenticación independiente.** Trata su configuración, número de serie, clave pública y material de clave protegido como conceptos distintos. Leer una clave pública no revela la clave privada correspondiente.

**CryptoAuthLib** de Microchip proporciona la interfaz del dispositivo. El repositorio **cryptoauthtools** contiene ejemplos basados en la biblioteca. Prepara la biblioteca nativa y los enlaces Python para tu sistema siguiendo las instrucciones de esos proyectos antes de ejecutar un ejemplo. Instalar un paquete Python ajeno o copiar un solo script no demuestra que funcione el backend I2C. [CryptoAuthLib de Microchip](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools de Microchip](https://github.com/MicrochipTech/cryptoauthtools)

Desde un directorio preparado `cryptoauthtools/python/examples`, ejecuta el comando de inspección del artículo original:

```bash
sudo python3 info.py -i i2c
```

El argumento **`-i i2c`** selecciona la interfaz. Con un entorno virtual, usa su intérprete Python explícito y asegúrate de que encuentra la biblioteca nativa correspondiente. En muchas instalaciones, `sudo python3` selecciona el intérprete del sistema, lo que explica algunos errores de importación de módulos.

El `info.py` revisado lee datos de revisión, número de serie, configuración y estado de bloqueo. Si la zona de datos está bloqueada, intenta obtener la clave pública del slot 0. No ejecuta la secuencia de aprovisionamiento del ejemplo. Un fallo aislado al leer la clave pública del slot 0 no demuestra que el dispositivo esté averiado. [Código fuente info.py de Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Salida u operación | Significado |
|---|---|
| **Configuración bloqueada** | Se aplican restricciones a la configuración |
| **Zona de datos bloqueada** | Interpreta el acceso según las políticas configuradas de los slots |
| **Se muestra la clave pública** | Se obtuvo información pública, no se exportó una clave privada |
| **Ejecución de `config.py`** | Ejemplo de aprovisionamiento con configuración, bloqueo y generación de claves |

**No ejecutes `config.py` para reparar un error de inspección.** Su código incluye escrituras de configuración, llamadas para bloquear zonas y generación de claves. La ruta predeterminada de generación también importa en un dispositivo configurado previamente. [Código fuente config.py de Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Los perfiles de aprovisionamiento documentados por Microchip muestran por qué bloquear la zona de datos no significa que todos los slots tengan permisos idénticos. Esos perfiles no demuestran la configuración exacta del M1. Conserva la configuración existente y consulta la documentación de la pieza correspondiente antes de planificar una reutilización de claves. [Políticas de acceso a memoria y slots de Microchip](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## Resuelve las dudas del ventilador y el botón

**Una toma de ventilador de tres pines no determina su voltaje, polaridad ni método de control.** Fotografía la numeración y lee la etiqueta del ventilador. Resuelve las conexiones de alimentación y control antes de conectar un repuesto o elegir un overlay GPIO.

La investigación original tampoco determina el GPIO del botón. Busca un controlador o una configuración para la revisión de tu placa y verifica la conectividad con la alimentación desconectada. No configures como salidas todos los GPIO aparentemente libres para encontrar el botón.

| Periférico | Evidencia que debes reunir | Condición de aceptación |
|---|---|---|
| **Alimentación del ventilador** | Especificación del ventilador, tierra y alimentación del conector | La fuente medida coincide con las especificaciones del ventilador |
| **Control del ventilador** | Controlador/configuración o circuito de control trazado | Comportamiento definido al arrancar y a temperatura elevada |
| **Botón de usuario** | Cableado de contactos, mapa GPIO, polaridad de entrada | Una pulsación intencionada produce el evento esperado |

Una instalación nueva del sistema operativo no reproduce automáticamente la política de refrigeración del equipo original. En la primera prueba prolongada, observa a la vez el ventilador y las temperaturas. Mantén el flujo de aire de la carcasa y detén la prueba si el conjunto pierde la refrigeración necesaria.

## Elige una pila para la puerta de enlace

**Separa el soporte de la placa del protocolo del servidor.** Un servidor LoRaWAN compatible no corrige una rutina de reinicio equivocada ni una calibración RF incorrecta. Primero elige software compatible con el concentrador, el cableado del carrier, el sistema operativo y la configuración regional.

| Opción de software | Función útil | Comprobar antes del despliegue |
|---|---|---|
| **Semtech SX1302 HAL** | Puesta en marcha a nivel de código y herramientas de diagnóstico | Rutina de reinicio de placa y configuración del módulo |
| **LoRa Basics Station** | Conexión autenticada de la puerta de enlace al servidor | Integración funcional de la placa y credenciales del servidor |
| **ChirpStack Concentratord** | Servicio dedicado al concentrador | Modelo compatible, calibración y mapa GPIO |

ChirpStack incluye el modelo SPI **`seeed_wm1302`**. Esto demuestra el soporte del módulo, no que exista una imagen M1 completa ni soporte para todas las revisiones M1. No trates las instrucciones independientes de instalación de SenseCAP M2 como instrucciones de firmware M1. [Soporte de hardware de ChirpStack](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [Destino de instalación Seeed de ChirpStack](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Para The Things Stack, la documentación recomienda **LoRa Basics Station** frente al reenviador UDP Semtech heredado. Station ofrece TLS y autenticación mediante tokens, junto con funciones de configuración centralizada. Los ejemplos UDP sirven para entender el reenvío de paquetes, pero la dirección del servidor no proporciona esas protecciones. [Guía UDP de The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [Documentación LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Prepara las herramientas upstream

Compila en el Pi objetivo en un directorio de trabajo nuevo:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Guarda el identificador del commit con los resultados de compilación. Una compilación completada demuestra compatibilidad con el compilador, pero la radio también requiere el procedimiento de reinicio verificado y la configuración correcta. La documentación de Semtech explica el papel de su HAL y herramientas auxiliares. [Documentación de compilación y herramientas SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Revisa el archivo de reinicio antes de ejecutar herramientas de acceso al hardware:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

No copies este archivo sin cambios al directorio de ejecución. Semtech documenta el uso automático del script por sus programas de acceso al hardware, incluidas herramientas de identificación. Revisa todos los pines asignados, dirección de señal, API GPIO y estado al iniciar y terminar.

Después de verificar la placa, sigue las instrucciones de la pila elegida para leer el EUI del concentrador y registrar la puerta de enlace. Conserva la calibración del módulo y los ajustes RF al añadir la configuración del servidor. En la configuración UDP de Semtech, `gateway_ID` representa el EUI; el Gateway ID de la consola de The Things Stack es el identificador legible que se registra. [Configuración de puerta de enlace de The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## Demuestra la entrega del sensor

**Usa pruebas por etapas para localizar la primera capa que falla.** Que una puerta de enlace aparezca en línea demuestra una conexión al servidor. La prueba de aceptación también necesita un sensor conocido, un plan de frecuencias coincidente y una carga útil de aplicación decodificada.

La secuencia siguiente es un plan de prueba propuesto, no un resultado medido en un M1:

| Punto de control | Evidencia que debes guardar | Significado |
|---|---|---|
| **Anfitrión listo** | Sistema operativo, kernel, alimentación e inventario de interfaces | Preparación Linux terminada |
| **Responde el concentrador** | EUI y registro de inicialización correcta | Funciona la comunicación entre anfitrión y concentrador |
| **Recepción de radio** | Paquete esperado del sensor y metadatos de recepción | Funciona la ruta de recepción configurada |
| **El servidor acepta** | Evento de puerta de enlace asociado al sensor | Funcionan el reenvío y el enrutamiento del servidor |
| **Decodificación de aplicación** | Medición y marca de tiempo esperadas | Funciona la ruta de aplicación |
| **Recuperación tras reiniciar** | Las mismas comprobaciones después del reinicio | La configuración de inicio es reproducible |

Para un sensor **OTAA**, confirma también el intercambio de activación y el enlace ascendente posterior. OTAA significa activación por el aire y es el procedimiento de unión que establece una sesión. Recibir una solicitud de unión no demuestra que la unión se haya completado ni que funcione la ruta de enlace descendente. [Documentación de activación de The Things Stack](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Diagnóstico práctico:** la puerta de enlace se conecta al servidor e informa su EUI, pero no aparece el sensor. Da prioridad a la configuración de transmisión del sensor, los canales de recepción seleccionados, la ruta de antena y los registros de radio. Reprogramar el ATECC608 no resolvería las pruebas que faltan en este caso.

**Segundo diagnóstico:** un paquete del sensor aparece localmente, pero no llega a la aplicación. Correlaciona la hora del paquete con los eventos de la puerta de enlace y el servidor, y revisa el enrutamiento, el registro del dispositivo y la decodificación. Un paquete RF en un registro no basta para culpar al decodificador antes de que el servidor acepte el evento.

## Diagnóstico por síntoma

| Síntoma | Comprueba primero | Siguiente acción |
|---|---|---|
| **No hay archivo de dispositivo SPI** | Configuración de arranque activa y opciones de interfaz | Activa la interfaz prevista y reinicia |
| **Existe SPI, falla la radio** | Alimentación, inserción, secuencia de reinicio y selección de chip | Verifica la ruta eléctrica antes de cambiar el servidor |
| **Error de exportación GPIO** | Suposiciones de sysfs heredadas y kernel instalado | Usa una implementación revisada para la API GPIO |
| **GPIO en uso** | Consumidor que muestra `gpioinfo` | Resuelve la propiedad antes de volver a probar |
| **El LED falla tras configurarlo** | Aplicación del overlay y conflictos GPIO22 | Inspecciona dispositivos LED registrados y el script de reinicio |
| **Falta un dispositivo I2C** | Número de bus, alimentación y uso existente | Investiga sin repetir escaneos amplios |
| **Falla la importación de la biblioteca criptográfica** | Intérprete, enlaces y ruta de biblioteca nativa | Corrige el entorno de software |
| **Falla la lectura de clave pública** | Política del slot y lecturas previas correctas | Revisa la configuración sin aprovisionar |
| **No funciona el ventilador** | Fuente verificada e implementación de refrigeración | Restaura la refrigeración antes de pruebas prolongadas |
| **Llegan enlaces ascendentes, falla la unión** | Ruta descendente y ajustes regionales/del dispositivo | Rastrea la respuesta de unión y ventanas de recepción |

Trata cada corrección como un experimento. Guarda la configuración anterior, cambia una variable, repite la misma comprobación y registra si apareció la evidencia esperada.

## Crea tu registro de hardware

Usa esta plantilla para convertir la investigación en un traspaso reproducible:

```text
Revisión del carrier y fotografías:
Modelo, interfaz y banda RF del concentrador:
Modelo del anfitrión / sistema operativo / kernel / versión de la herramienta GPIO:
Fuente / antena / configuración de refrigeración:
Mapa de pines verificado y pruebas:
Conexiones sin resolver y funciones excluidas:
Repositorio de software y commit:
Implementación de reinicio y propietario GPIO:
EUI de la puerta de enlace / servidor / plan de frecuencias:
Activación del sensor y pruebas del enlace ascendente decodificado:
Resultado de recuperación tras reiniciar:
Ubicación de la tarjeta original y procedimiento de reversión:
```

**Ejercicio de decisión:** tienes un carrier desnudo y económico sin etiqueta de módulo, y un conjunto más caro con etiquetas legibles y funcionamiento documentado. Decide cuál encaja con tu proyecto tras añadir el Pi, el concentrador, la antena, la fuente y el tiempo de verificación que faltan. La mejor opción depende del coste total y de las pruebas que requiere el servicio previsto, no del precio anunciado del carrier.

**Razonamiento esperado:** un proyecto de aprendizaje tolera conexiones sin resolver si dispones de instrumentos de medición y tiempo. Una puerta de enlace para sensores operativos requiere inicio reproducible, refrigeración, soporte de software y entrega demostrada. Anota qué condición sin resolver detendría el despliegue.

## Próximos pasos

Empieza completando el registro de hardware y resolviendo las discrepancias del script de reinicio. Después, pon en marcha un sensor conocido y guarda pruebas hasta la decodificación de la aplicación antes de añadir más dispositivos.

**Registro de aceptación:** guarda la revisión de la placa, etiqueta del módulo, banda de radio, medición de alimentación, dispositivo SPI activo, nombres de líneas GPIO, secuencia de reinicio, registro del concentrador, conexión al servidor y un enlace ascendente decodificado. Marca cada dato como observado, documentado o aún supuesto. No consideres que un proceso iniciado demuestra rendimiento RF o entrega a la aplicación.

Si tu objetivo es la mensajería mesh, compara primero las funciones de los protocolos en nuestra [guía de Meshtastic, MeshCore y Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Compartir tecnología de radio LoRa no demuestra compatibilidad de firmware. Para un despliegue de mensajería, consulta la [documentación de hardware compatible con MeshtasticD](https://meshtastic.org/docs/meshtasticd/) en vez de tratar este procedimiento LoRaWAN como una conversión a Meshtastic.

## Fuentes y créditos de imágenes

Investigación revisada el 12 de septiembre de 2026. Los enlaces a documentación y repositorios sin fecha remiten a las versiones revisadas para este artículo. Las figuras locales conservan sus rótulos y atribución originales.

| Editor | Fuente y fecha |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03. Foto de la placa, conector anotado y diagrama de bloques del fabricante reproducido |
| **Seeed Studio / SenseCAP** | [Descripción y especificaciones M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/), sin fecha. Atribución del diagrama de bloques original |
| **Seeed Studio** | [Documentación WM1302 y pinout del módulo](https://github.com/seeed-lora/WM1302-doc), repositorio |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), incluidas las fuentes enlazadas del script de reinicio y el controlador de temperatura |
| **Raspberry Pi** | [Configuración de arranque](https://www.raspberrypi.com/documentation/computers/config_txt.html), [guía GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) y [referencia de overlays](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Interfaz GPIO sysfs obsoleta](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) y [manual gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html), este último fechado en agosto de 2026 |
| **i2c-tools** | [Manual i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), código fuente v4.3 |
| **STMicroelectronics** | [Ficha técnica STTS751](https://www.st.com/resource/en/datasheet/stts751.pdf), revisión 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) y [documentación de políticas de acceso a slots](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Soporte de hardware Concentratord](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) y [destino de instalación Seeed](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [Reenviador UDP](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) y [activación de dispositivos](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [Documentación MeshtasticD](https://meshtastic.org/docs/meshtasticd/), sin fecha |
