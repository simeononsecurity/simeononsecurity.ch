---
title: "Eye Spy: detector pasivo de vigilancia y rastreadores para ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Referencia técnica de Eye Spy v1.1, un detector pasivo de BLE y WiFi con ESP32 para cámaras, rastreadores, drones y señales relacionadas."
genre: ["Herramientas de privacidad", "Contra vigilancia", "Seguridad IoT", "Sistemas integrados", "Investigación de seguridad", "Seguridad WiFi", "Seguridad Bluetooth", "Proyectos ESP32", "Seguridad de hardware", "Seguridad de código abierto"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Detección de vigilancia", "Contra vigilancia", "Detección BLE", "Escaneo WiFi", "Detección de AirTag", "Detección ALPR", "Flock Safety", "Detección de cámaras corporales", "Detección de drones", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Código abierto", "Privacidad", "BLE pasivo", "Modo promiscuo", "Detección OUI", "Detección de rastreadores", "Cámara corporal Axon", "Ray-Ban Meta", "Samsung SmartTag", "Rastreador Tile", "Cámara oculta", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Ilustración de un pequeño M5Stack Atom Lite rodeado de ondas de señales coloridas sobre un fondo azul marino oscuro, como representación de la detección de vigilancia por Bluetooth y WiFi."
coverCaption: ""
---

**Un sensor pasivo del tamaño de un pulgar que le avisa cuando algo lo observa**

## Introducción: el panorama de vigilancia que no se ve

El mundo físico está cada vez más equipado con dispositivos que observan, graban y rastrean: lectores de matrículas en las esquinas, cámaras corporales de las fuerzas del orden, cámaras en viviendas de alquiler, rastreadores comerciales similares a AirTag ocultos en bolsos o automóviles y cámaras de vigilancia en las entradas de comercios. La mayoría de estos dispositivos se comunica de forma inalámbrica mediante **Bluetooth LE** o **WiFi**. *La mayoría de esas comunicaciones se emite al aire y cualquier persona con el receptor adecuado puede detectarla.*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) es una herramienta pasiva de detección de vigilancia que aprovecha precisamente este hecho. Eye Spy funciona en el **M5Stack Atom Lite**, una placa de desarrollo ESP32-PICO-D4 del tamaño aproximado de un terrón de azúcar, y vigila continuamente las bandas BLE y WiFi en busca de las firmas electrónicas de dispositivos de grabación, cámaras de vigilancia, sistemas **ALPR** (lectores automáticos de matrículas), drones y rastreadores personales. Cuando encuentra una señal, cambia el color de su LED RGB.

*No se conecta a ningún dispositivo ni transmite.* Observa, asigna puntuaciones y se ilumina.

Este artículo es una referencia técnica completa: explica qué detecta Eye Spy, cómo funciona el sistema de puntuación de confianza, cómo están diseñados los motores de detección, cómo construir y flashear el dispositivo y cuáles son sus límites prácticos.

**¿Prefiere no construir uno?** STS Collective ofrece **[detectores Eye Spy](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** preconfigurados y listos para usar. El código para lectores **SIMEONONSECURITY** ofrece hasta un 20 % de descuento.

{{< stscollective-ad "eyespy" >}}

---

## Indicadores LED: toda la interfaz de usuario

Al igual que el [ESP32 WiFi Canary: detección pasiva de amenazas en 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), toda la salida de Eye Spy consiste en un único NeoPixel RGB SK6812 conectado al GPIO 27 del M5Stack Atom Lite. El LED comunica continuamente uno de cuatro niveles de amenaza:

| Color | Significado | Rango de puntuación |
|-------|-------------|---------------------|
| 🔵 Pulso azul | Inicio / primer escaneo | -- |
| 🟢 Verde fijo | Sin detecciones | 0–2 |
| 🟡 Amarillo fijo | Precaución: podría haber cerca un dispositivo de grabación | 3–5 |
| 🔴 Rojo intermitente | Alerta: se detectó un dispositivo de vigilancia o rastreo | 6+ |

**Una sola detección de alta confianza (cámara corporal Axon, cámara Flock Safety, coincidencia de OUI de ALPR o AirTag) suma suficientes puntos para poner el LED en rojo durante un ciclo de detección.** Varias detecciones de confianza media acumulan puntos hasta llegar al amarillo y pueden combinarse para alcanzar el rojo.

---

## Hardware

### Dispositivo principal: M5Stack Atom Lite

| Componente | Detalle |
|-----------|--------|
| Placa | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | NeoPixel SK6812 en GPIO 27 |
| Botón | GPIO 39 (solo entrada) |
| Flash | 4 MB |

El Atom Lite es una plataforma autónoma completa. **No requiere soldadura, placa de pruebas ni componentes externos.** Conéctelo al USB y estará listo.

### ESP32 DevKit genérico

Un segundo entorno de compilación de PlatformIO (`esp32dev`) funciona con cualquier ESP32 DevKit estándar que tenga un LED integrado en GPIO 2. Toda la lógica de detección funciona igual. Esta compilación resulta útil para desarrollar y probar la lógica, o para implementarla cuando no se necesita el formato del Atom Lite.

---

## El sistema de puntuación

Eye Spy usa un **modelo de puntuación de confianza** que reúne las señales de todos los motores de detección en un único entero. La puntuación determina el estado del LED (verde, amarillo o rojo) y se administra con dos mecanismos automáticos:

### Reducción de la puntuación

La puntuación baja **1 punto cada 60 segundos** si no hay nuevas detecciones. Si se aleja de un dispositivo detectado, el LED vuelve al verde en unos minutos sin que tenga que intervenir.

### Periodo de espera para volver a puntuar

Cada *tipo* de detección tiene un **periodo de espera de 120 segundos** antes de volver a sumar puntos desde la misma fuente. *Así, un dispositivo persistente no acumula puntos sin límite.* Una cámara Flock Safety que permanece dentro del alcance suma +5 una vez y espera 120 segundos antes de contribuir de nuevo.

En conjunto, estos mecanismos significan lo siguiente:

- **Detecciones pasajeras** (por ejemplo, un automóvil con un AirTag que pasa) desaparecen de forma automática.
- **Vigilancia persistente** (por ejemplo, cámaras corporales desplegadas en una ubicación fija) mantiene el LED en alerta mientras permanezca dentro del alcance.
- **No se acumulan puntos sin control** por detectar repetidamente un mismo dispositivo.

---

## Motores de detección

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Diagrama de los motores paralelos BLE y WiFi de Eye Spy, que buscan AirTags, cámaras corporales, sistemas ALPR y drones, y envían los resultados al modelo de puntuación de confianza" >}}

Eye Spy alterna continuamente entre tres fases de escaneo:

**BLE pasivo (9 s) → escaneo WiFi (~3 s) → captura promiscua (5 s) → repetir**

Eye Spy detiene BLE antes de cualquier operación WiFi para respetar el uso compartido de la radio ESP32. BLE se reinicia al principio de cada ciclo.

---

### Motor 1: BLE, escaneo pasivo

El escaneo BLE usa **NimBLE sin transmitir solicitudes de escaneo**. El dispositivo escucha paquetes de publicidad BLE sin responder. *Así Eye Spy resulta electrónicamente invisible para los equipos que busca: el objetivo no detecta un escáner pasivo.*

Para reducir los falsos positivos en entornos densos, se ignoran los dispositivos con una señal inferior a **−90 dBm**.

#### Tabla de detección BLE

| # | Objetivo | Método de detección | Puntuación |
|---|--------|-----------------|-------|
| 1 | **Cámara corporal Axon** | OUI de la MAC BLE `00:25:df` (Axon: cámaras corporales, dispositivos Taser y equipos policiales) | +5 🔴 |
| 2 | **Gafas inteligentes Ray-Ban Meta** | UUID de servicio BLE `0xFD5F` | +5 🔴 |
| 3 | **BLE de Flock Safety** | El nombre BLE contiene `Flock`, `Penguin`, `Pigvision` o `FS Ext Battery` | +5 🔴 |
| 4 | **Skimmer de tarjetas (HC-03/05/06)** | Coincidencia exacta del nombre BLE: módulos Bluetooth habituales en skimmers de terminales de pago | +5 🔴 |
| 5 | **Apple AirTag** | Datos del fabricante `0x004C`, subtipo `0x12`/`0x1E`, o carga útil `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Dron (OpenDroneID BLE)** | UUID de servicio BLE `0xFFFA` o carga útil de datos de servicio AD con código de aplicación `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID de servicio BLE `0xFD5A` | +3 🟡 |
| 8 | **Rastreador Tile** | UUID de servicio BLE `0xFEED` o `0xFEEC` | +3 🟡 |
| 9 | **Nodo MeshCore** | Prefijo del nombre BLE `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (seguimiento en comercios o recintos)** | Datos del fabricante `0x004C 0x02 0x15`; se usa en comercios, aeropuertos y estadios para seguir movimientos | +2 🟡 |
| 11 | **Dispositivo persistente desconocido** | MAC BLE sin clasificar que aparece al menos 3 veces en 5 minutos (detección de rastreo o seguimiento) | +2 🟡 |

#### Detecciones BLE destacadas en detalle

**Cámara corporal Axon (+5)**: Axon (antes TASER International) fabrica algunos de los sistemas de cámaras corporales más extendidos entre las fuerzas del orden de Estados Unidos. El OUI `00:25:df` está registrado a nombre de Axon y aparece en sus dispositivos portátiles. **Una detección basta para alcanzar el nivel de alerta.**

**Gafas inteligentes Ray-Ban Meta (+5)**: La colaboración Ray-Ban Meta produce gafas inteligentes de consumo que graban vídeo y toman fotografías. El UUID de servicio BLE `0xFD5F` es el anuncio característico de estos dispositivos. *Son productos de consumo y pueden aparecer en lugares públicos concurridos.* Conviene prestar atención a cualquier detección con esta puntuación, sin importar la intención de quien las lleva.

**Módulos Bluetooth de skimmers (+5)**: HC-03, HC-05 y HC-06 son módulos Bluetooth serie económicos que se encuentran con frecuencia en superposiciones de terminales de pago y en skimmers para cajeros automáticos. La detección compara el nombre exacto del dispositivo con los nombres predeterminados del firmware de esos módulos. **Una alerta roja justifica revisar físicamente los terminales de pago cercanos.**

**Apple AirTag (+4)**: Los AirTag transmiten anuncios mediante el protocolo propietario **Nearby Interaction** de Apple. La detección busca la cabecera de datos del fabricante (`0x004C` = Apple) junto con los subtipos específicos de AirTag (`0x12` para el anuncio estándar y `0x1E` para el anuncio de objeto perdido). Los patrones de la carga útil en bruto añaden una ruta de detección redundante.

**OpenDroneID BLE (+4)**: La norma **ASTM F3411 Remote ID**, adoptada también por la FAA para drones comerciales en Estados Unidos, define un protocolo de difusión para que los drones anuncien su identidad y posición. Eye Spy busca el UUID de servicio GATT `0xFFFA` (el servicio Remote ID designado) y el código de aplicación `0x0D` en la carga útil de datos de servicio AD. *Un dron comercial cercano que cumpla la norma activará esta detección.*

**Dispositivo persistente desconocido (+2)**: Este es el motor de **detección de seguimiento**. Registra toda MAC BLE que no clasifiquen las detecciones específicas anteriores. La MAC recibe puntos si aparece tres veces o más durante un periodo de al menos cinco minutos. El rastreador conserva hasta 50 MAC desconocidas a la vez y elimina las entradas tras 30 minutos sin actividad. **Así se pueden detectar rastreadores personalizados o modificados que no coinciden con ningún UUID de servicio o patrón de fabricante conocido.**

**iBeacon (+2)**: Los comercios, aeropuertos y estadios usan el formato iBeacon de Apple (`0x4C 0x00 0x02 0x15`) para seguir el movimiento de dispositivos en espacios físicos. La detección se activa con el formato estándar del anuncio, sin importar el UUID: identifica el tipo de despliegue y no un UUID concreto. *Una detección indica que probablemente se encuentra en un lugar que rastrea activamente la presencia de dispositivos Bluetooth.*

---

### Motor 2: escaneo WiFi, búsqueda activa de canales

El motor de escaneo WiFi usa la interfaz estándar de búsqueda de puntos de acceso del ESP32 para enumerar los puntos de acceso cercanos y comparar sus BSSID y SSID con las huellas conocidas de dispositivos de vigilancia.

#### Tabla de detección WiFi

| # | Objetivo | Método de detección | Puntuación |
|---|--------|-----------------|-------|
| 12 | **Cámara Flock Safety (OUI)** | BSSID coincide con la tabla Flock Safety de 22 OUI (`d4:bb:e6`, `3c:61:05` y prefijos de FS-Ext-Battery) | +5 🔴 |
| 13 | **Cámara ALPR / LPR (OUI)** | BSSID coincide con el OUI `00:0e:58` de Motorola Solutions / Vigilant Solutions | +5 🔴 |
| 14 | **SSID con palabras clave de Flock** | SSID contiene: `flock`, `flocksafety`, `fs ext`, `penguin` o `pigvision` | +5 🔴 |
| 15 | **SSID con palabras clave de ALPR** | SSID contiene: `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` o `automate` | +4 🔴 |
| 16 | **Proveedor de cámaras de vigilancia (OUI)** | BSSID coincide con una tabla de 31 OUI de cámaras: Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix o Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID con palabras clave de cámara** | SSID contiene, entre otras: `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` o `genetec` | +2 🟡 |

#### Tabla OUI de Flock Safety

La tabla `FLOCK_OUIS` de 22 entradas es la consulta más detallada del proyecto. Incluye:

- `d4:bb:e6`: OUI de Flock Safety registrado por IEEE.
- `3c:61:05`: OUI de Flock Safety registrado por IEEE.
- Otros 20 prefijos MAC observados sobre el terreno en dispositivos Flock FS-Ext-Battery y cámaras WiFi de Flock.

Estas 22 entradas representan rangos de direcciones MAC observados en sistemas ALPR Flock Safety desplegados. **La detección por OUI es independiente del SSID**: una cámara Flock con un SSID que no contenga palabras clave suma +5 si coincide su OUI BSSID.

Los OUI de Flock Safety y Vigilant Solutions están en tablas separadas para que puedan puntuar de forma independiente en un mismo ciclo de escaneo. *Un lugar con equipos de ambos proveedores podría acumular +10 durante una sola pasada WiFi.*

#### Tabla OUI de proveedores de cámaras de vigilancia

La tabla de 31 cámaras de vigilancia abarca los principales fabricantes de cámaras IP que podrían aparecer en despliegues comerciales, residenciales y de comercios:

- **Empresas y comercios**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix y Genetec.
- **Consumo y pequeñas oficinas**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex y Amcrest.
- **Infraestructura**: Ubiquiti UniFi (sus puntos de acceso y cámaras comparten rangos OUI) y FLIR.

Una coincidencia suma +3, en el rango de precaución, sin confirmar ninguna palabra clave. Si también coincide un SSID con una palabra clave, la misma red de cámaras suma primero +3 por el OUI y después +2 por el SSID, lo que alcanza el nivel de alerta en un ciclo de escaneo.

---

### Motor 3: WiFi promiscuo, captura pasiva de tramas

El motor promiscuo coloca la radio ESP32 en **modo monitor** y captura tramas de administración 802.11 en bruto. Así detecta dispositivos que no anuncian un SSID, en particular drones que usan el protocolo **Remote ID** sobre **WiFi Neighbor Awareness Networking (NaN)**.

Durante esta fase, la radio **salta entre los canales** `{1, 6, 11, 3, 8, 13}` cada 400 ms para ampliar la cobertura de los canales que emiten tramas NaN de drones.

#### Tabla de detección promiscua

| # | Objetivo | Método de detección | Puntuación |
|---|--------|-----------------|-------|
| 18 | **Dron (OpenDroneID WiFi NaN)** | Trama de administración 802.11 dirigida a `51:6f:9a:01:00:00`: difusión Remote ID según ASTM F3411 | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: La norma ASTM F3411 define la dirección multidifusión `51:6f:9a:01:00:00` para las tramas Remote ID de WiFi NaN. Los drones comerciales regulados que difunden su posición e identidad por WiFi envían tramas a esta dirección. Eye Spy busca tramas de administración dirigidas a esa MAC multidifusión: la detección es pasiva y fiable. *El operador del dron tendría que desactivar Remote ID para impedirla, lo que infringiría la normativa aplicable.*

Esta detección complementa el motor BLE de OpenDroneID (detección n.º 6). *Según el hardware y la configuración, un dron puede anunciarse mediante BLE, WiFi o ambos.* Eye Spy cubre las dos opciones.

---

## Calendario de fases y administración de la radio

```
BLE pasivo (9 s) → escaneo WiFi (~3 s) → captura promiscua (5 s) → repetir
```

El ESP32-PICO-D4 tiene **una sola radio compartida de 2,4 GHz** para BLE y WiFi. Eye Spy la administra de esta manera:

1. **Fase BLE** (9 segundos): NimBLE está activo y ejecuta el escaneo pasivo sin transmitir solicitudes.
2. **Detención de BLE**: se detiene explícitamente la pila BLE antes de usar WiFi.
3. **Escaneo WiFi** (~3 segundos): búsqueda activa de puntos de acceso en todos los canales y comparación de OUI y SSID.
4. **Captura promiscua** (5 segundos): captura pasiva de tramas 802.11 con saltos de canal.
5. **Detención de WiFi**: se detiene WiFi y se reinicia BLE para el siguiente ciclo.

Esta administración explícita de las fases evita conflictos de radio y permite que ambos motores BLE y WiFi accedan a la radio de forma ordenada en cada ciclo.

---

## Salida serie

Todas las líneas comienzan con `[eyespy]` para facilitar su filtrado. El monitor serie funciona a **115200 baudios**.

### Inicio

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Ciclo normal

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Eventos de detección

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

El campo `tracked=N` muestra cuántas MAC BLE únicas conserva el rastreador de persistencia. Ayuda a entender la densidad del entorno BLE.

### Campos de puntuación

Cada línea de estado incluye:

- **score**: puntuación de amenaza actual.
- **state**: `CLEAR` / `CAUTION` / `ALERT`.
- **phase**: motor activo (`BLE` / `WIFI` / `PROMISC`).
- **tracked**: cantidad de MAC BLE únicas en la tabla de persistencia.

---

## Compilar y flashear

### Requisitos

- **PlatformIO** (CLI o extensión de VS Code).
- **M5Stack Atom Lite** o cualquier ESP32 DevKit.
- Cable USB-C.

### Dependencias

PlatformIO las instala automáticamente:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** controla el LED RGB SK6812. **NimBLE-Arduino** proporciona la pila de escaneo BLE pasivo. Se prefiere a la biblioteca BLE ESP32 predeterminada porque admite el modo pasivo, evita enviar solicitudes de escaneo y consume menos memoria.

### Flashear el M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Compilar y flashear para Atom Lite
pio run -e atom-lite -t upload

# Abrir el monitor serie a 115200 baudios
pio device monitor -b 115200
```

### Flashear un ESP32 DevKit genérico

```bash
pio run -e esp32dev -t upload
```

### Estructura del proyecto

```
eye-spy/
├── src/
│   └── main.cpp          # Toda la lógica del firmware
├── platformio.ini         # Entornos de compilación (atom-lite, esp32dev)
├── partitions_4mb.csv     # Tabla de particiones para flash de 4 MB
└── README.md
```

### platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

*El entorno `atom-lite` usa la definición de placa `m5stick-c`, que tiene el mismo chip ESP32-PICO-D4 y un mapeo de pines compatible con el NeoPixel de GPIO 27.*

---

## Detección: notas y límites prácticos

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Ilustración con aspecto fotográfico del Eye Spy en un M5Stack Atom Lite, del tamaño aproximado de un terrón de azúcar, sostenido entre dos dedos para mostrar su pequeño tamaño" >}}

### Lo que Eye Spy no puede hacer

**WiFi de 5 GHz**: El ESP32 funciona **solo en 2,4 GHz**. Las cámaras de vigilancia, los sistemas ALPR y los puntos de acceso que funcionen únicamente en 5 GHz no aparecerán en los motores de escaneo WiFi ni de captura promiscua. *Muchas cámaras IP modernas también admiten 2,4 GHz, aunque sean compatibles con 5 GHz. Aun así, no se detectarán los despliegues que usen exclusivamente 5 GHz.*

**BLE cifrado**: Algunos productos de vigilancia de gama alta cifran u ocultan sus anuncios BLE. Eye Spy detecta dispositivos que difunden firmas identificables en texto claro, como OUI, UUID de servicio y datos del fabricante. *Los dispositivos que cambian de dirección MAC (una función de privacidad cada vez más habitual en rastreadores de consumo) evitan la detección basada en MAC.* El rastreador de persistencia quizá los detecte solo si el cambio ocurre con menos frecuencia que cada cinco minutos.

**Cámaras cableadas**: **Las cámaras IP conectadas por Ethernet sin radio WiFi no emiten señales inalámbricas que Eye Spy pueda detectar.** Las cámaras ocultas sin conexión de red que solo graban localmente tampoco generan una firma RF.

**Límites de alcance**: En interiores, la antena ESP32 recibe señales fuertes a una distancia práctica de **20 a 40 metros**; las señales débiles o bloqueadas llegan menos. *Los dispositivos en el límite del alcance o detrás de un blindaje RF importante podrían no sumar puntos o quedar por debajo del umbral RSSI de −90 dBm.*

### Falsos positivos previsibles

**Cámaras de consumo en casas vecinas**: Las cámaras Ring, Nest, Wyze, Arlo y Reolink son comunes en barrios residenciales y sus OUI aparecen en la tabla de 31 cámaras. *En una zona residencial, espere alguna detección amarilla de precaución (+3) de cámaras en timbres de vecinos.* No es un falso positivo en el sentido técnico, porque el dispositivo *sí* detecta una cámara. El contexto importa.

**Despliegues comerciales de iBeacon**: Los comercios grandes instalan infraestructura iBeacon en casi todas sus tiendas. *Una visita a un centro comercial o supermercado probablemente active la detección iBeacon (+2).* El dispositivo está cumpliendo su función: la infraestructura de seguimiento comercial está presente.

**Infraestructura Ubiquiti UniFi**: Los puntos de acceso UniFi aparecen en la tabla OUI de cámaras de vigilancia porque Ubiquiti fabrica equipos de red y cámaras de seguridad con rangos OUI que se solapan. *Una red que use UniFi sumará +3 por las coincidencias OUI del motor de escaneo WiFi.*

**Samsung SmartTag y dispositivos de consumo**: El UUID SmartTag (`0xFD5A`) es un servicio registrado por Samsung. *Los SmartTag son rastreadores de consumo que también tienen usos personales legítimos.* La presencia de un SmartTag cercano activará esta detección.

### Qué significa cada nivel de puntuación en la práctica

| Puntuación | Situación probable en el mundo real |
|-------|-----------------------------|
| 6–10 (🔴) | Detección creíble de alta confianza: cámara Axon a unos 30 m, cámara Flock Safety con OUI coincidente, patrón confirmado de seguimiento de AirTag o dron que anuncia Remote ID |
| 3–5 (🟡) | Varios rastreadores de consumo, cámaras de vecinos que acumulan puntos, posible cámara Flock o una detección OpenDroneID |
| 0–2 (🟢) | No se detectaron firmas importantes de vigilancia; hay actividad habitual de dispositivos de consumo, pero no supera el umbral |

---

## Comparación con proyectos relacionados

Eye Spy se ocupa de la vigilancia física en el entorno. [ESP32 WiFi Canary: detección pasiva de amenazas en 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) detecta ataques WiFi de capa de red contra sus propios dispositivos. *Son herramientas complementarias que abordan modelos de amenaza diferentes.*

| Capacidad | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| Detección de AirTag y rastreadores | ✅ | ❌ |
| Detección de cámaras ALPR / Flock | ✅ | ❌ |
| Detección de cámaras corporales | ✅ | ❌ |
| Detección de drones (Remote ID) | ✅ | ❌ |
| Detección de puntos de acceso gemelos maliciosos | ❌ | ✅ |
| Detección de ataques de desautenticación | ❌ | ✅ |
| Detección de degradación de seguridad | ❌ | ✅ |
| Aprendizaje de línea base | ❌ | ✅ |
| BLE pasivo | ✅ | ❌ |
| Misma plataforma de hardware | ✅ | ✅ |

Ambos proyectos funcionan en el mismo M5Stack Atom Lite y usan los mismos indicadores LED y el sistema de compilación PlatformIO. Para vigilar la red y el entorno físico, puede cargar cada proyecto en un Atom Lite distinto y llevar ambos.

Eye Spy también complementa el [proyecto de detección Flock You](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) para quienes se preocupan específicamente por la infraestructura de vigilancia ALPR.

---

## Casos de uso

### Conocimiento de la vigilancia cercana

El público principal de Eye Spy incluye a quienes quieren conocer la infraestructura de vigilancia en su entorno inmediato. Al caminar por un barrio, pasar en automóvil junto a una intersección o asistir a un evento público, Eye Spy convierte el análisis complejo de RF en **un solo estado de LED en tiempo real**.

### Detección de acoso con AirTag

El acoso con AirTag es un problema documentado. El **motor de detección de seguimiento** de Eye Spy (una MAC BLE desconocida y persistente vista al menos 3 veces durante 5 minutos o más) busca rastreadores personalizados o modificados que no coinciden con el formato de anuncios conocido de Apple. Junto con la detección directa de AirTag, ofrece **dos vías independientes para detectar un rastreador que lo sigue**.

### Inspección de viviendas de alquiler y habitaciones de hotel

Al entrar en una habitación de hotel o vivienda de alquiler con Eye Spy activo, obtiene una primera indicación de dispositivos BLE o WiFi inesperados. Una coincidencia de SSID con palabras clave de cámara o un OUI de vigilancia en el escaneo WiFi suma puntos de precaución. *Esto no sustituye un barrido RF adecuado*, pero añade una capa pasiva de observación a la inspección física.

### Despliegues ALPR e investigación de privacidad

Quienes investigan la infraestructura de vigilancia, trabajan como periodistas en entornos vigilados o promueven la privacidad pueden usar Eye Spy como equipo de detección portátil y económico. La salida serie registra cada detección con RSSI, por lo que sirve como dispositivo sencillo de recopilación de datos.

### Seguridad durante los viajes

Al igual que WiFi Canary, Eye Spy tiene un formato adecuado para viajar. El Atom Lite cabe en un bolsillo o se fija a un bolso. Durante un viaje por aeropuertos, estaciones de tren o eventos públicos con mucha vigilancia conocida, ofrece monitorización pasiva continua sin interacción.

---

## Notas sobre la arquitectura

### Por qué importa el BLE pasivo

La decisión de usar escaneo BLE pasivo, sin paquetes de solicitud de escaneo, tiene consecuencias de seguridad. En un escaneo BLE estándar, el escáner transmite un paquete **SCAN_REQ** para pedir datos publicitarios adicionales a cada anunciante. *Por ello, el escaneo BLE activo es observable por ambos dispositivos*: el dispositivo escaneado ve la dirección del escáner en la solicitud.

El modo pasivo de NimBLE solo escucha anuncios no dirigidos (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) y nunca transmite un SCAN_REQ. **Eye Spy no transmite nada por BLE durante la fase de escaneo.** Una cámara corporal Axon, un dispositivo Flock o un AirTag detectado no puede observar ni reaccionar a la presencia del escáner.

### Diseño del rastreador de persistencia

El rastreador de persistencia de dispositivos desconocidos mantiene una tabla con hasta **50 direcciones MAC BLE** y las marcas de tiempo de la primera y la última detección. Se activa cuando una MAC aparece tres veces o más en un periodo de cinco minutos como mínimo.

El límite de 50 entradas y la purga tras 30 minutos equilibran la sensibilidad de detección y la memoria RAM del ESP32. *En entornos BLE densos (transporte público, conferencias o centros comerciales), la tabla puede llenarse rápidamente con dispositivos de consumo.* El umbral RSSI de −90 dBm filtra los dispositivos lejanos y centra el rastreador en fuentes cercanas y persistentes.

### Interacción entre la reducción de puntuación y el periodo de espera

El **periodo de espera de 120 segundos** impide que un dispositivo que permanece siempre dentro del alcance acumule puntos en cada ciclo BLE de nueve segundos. Sin ese periodo, una cámara Flock sumaría +5 cada 15 segundos y llegaría a cientos de puntos en pocos minutos.

La **reducción de 1 punto cada 60 segundos** baja la puntuación cuando un dispositivo sale del alcance y el periodo de espera vence sin otra detección. *Una detección única de +5 que no vuelve a activarse se reduce a cero en cinco minutos.* El dispositivo vuelve así de forma natural a un estado de tranquilidad que corresponde a desplazamientos habituales.

---

## Contribuciones y estado del proyecto

Eye Spy está disponible bajo la licencia Apache-2.0 en [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy).

Entre las posibles ampliaciones se incluyen:

- **Añadir entradas OUI**: ampliar las tablas OUI de Flock Safety y cámaras cuando se documenten nuevas MAC de hardware sobre el terreno.
- **Añadir UUID de servicio BLE**: las nuevas gafas inteligentes, cámaras y rastreadores incorporan UUID nuevos.
- **Ajustar el rastreador de persistencia**: el límite de 50 entradas, el umbral de tres observaciones y la ventana de cinco minutos son constantes modificables.
- **Registrar datos serie**: el formato de salida serie permite el análisis mediante programas. Un registrador externo podría reunir eventos de varias unidades Eye Spy.

El firmware está en un único archivo `main.cpp` del directorio `src/`, lo que facilita su lectura, auditoría y modificación.

---

## Conclusión

Eye Spy aborda un problema específico pero importante: cada vez hay más dispositivos de vigilancia física en el entorno, y la mayoría emite firmas RF detectables. **Un M5Stack Atom Lite de 15 dólares con el firmware Eye Spy se convierte en un escáner ambiental continuo** que transforma el análisis de paquetes BLE y las consultas OUI de WiFi en un único LED RGB.

El modelo de puntuación de confianza refleja una ponderación práctica de las amenazas: una cámara corporal Axon cerca de un despliegue policial suma +5 y enciende inmediatamente la luz roja; un iBeacon comercial suma +2 y contribuye a la observación sin provocar por sí solo una alarma. La reducción de puntuación y los periodos de espera evitan que el dispositivo alerte en exceso por señales pasajeras o persistentes de bajo nivel.

Para tareas de contra vigilancia, seguridad durante viajes, detección de AirTag o simplemente para saber si algo cercano lo observa, Eye Spy es una herramienta práctica, de código abierto y pasiva que merece un lugar en el equipo de un profesional de seguridad.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Comprar detectores Eye Spy y ahorrar un 20 %
{{< /centerbutton >}}
