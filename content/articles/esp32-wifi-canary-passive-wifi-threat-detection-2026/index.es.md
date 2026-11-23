---
title: "ESP32 WiFi Canary: detección pasiva de amenazas en 2,4 GHz"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "Análisis técnico de ESP32 WiFi Canary, un sensor pasivo de 2,4 GHz que detecta evil twins, desautenticación, degradaciones de seguridad e inundaciones de beacons."
genre: ["Seguridad de redes", "Seguridad WiFi", "Seguridad IoT", "Investigación de seguridad", "Sistemas embebidos", "Herramientas de privacidad", "Proyectos ESP32", "Seguridad de hardware", "Seguridad inalámbrica", "Seguridad de código abierto"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Detección de desautenticación", "Detección de evil twins", "Seguridad WiFi", "Supervisión pasiva de WiFi", "Tramas de gestión 802.11", "Seguridad de redes", "Seguridad IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Código abierto", "Sensor de seguridad", "Detección de amenazas inalámbricas", "Supervisión de BSSID", "Supervisión de SSID", "Detección de degradación de seguridad", "Detección de inundación de beacons", "Supervisión WiFi", "LED RGB", "Modo promiscuo", "Seguridad embebida", "Seguridad en viajes", "Seguridad WiFi en hoteles", "WiFi en cafeterías", "Concienciación sobre seguridad", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Ilustración de un dispositivo pequeño parecido a ESP32 WiFi Canary conectado a un puerto USB. Su LED RGB brilla con varios colores para representar sus funciones de detección de amenazas."
coverCaption: ""
---

**Un sensor pasivo de amenazas WiFi del tamaño de un pulgar que nunca transmite**

## El problema del WiFi público

Cada vez que te conectas al WiFi de un hotel, una cafetería o un aeropuerto, confías en que el punto de acceso sea legítimo. El problema es que las **tramas de gestión 802.11**, que anuncian redes, administran conexiones y coordinan clientes, *no están autenticadas en la mayoría de las implementaciones*. Con equipo sencillo, cualquiera puede clonar un SSID, enviar tramas de desautenticación o crear una red señuelo abierta junto a una WPA2 legítima.

[**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) es un sensor pasivo que ayuda a reconocer ese riesgo con un dispositivo diminuto. Cabe en el M5Stack Atom Lite, aproximadamente del tamaño de un terrón de azúcar. Se conecta por USB, aprende el entorno y enciende un LED RGB al detectar patrones asociados con amenazas inalámbricas.

No se conecta a redes, no captura credenciales y no transmite tramas. Observa, calcula una puntuación y comunica el estado mediante un color.

Este artículo es una referencia técnica completa del proyecto: qué detecta, cómo funciona el modelo de confianza, cómo compilarlo y grabarlo, y cuáles son sus limitaciones prácticas.

---

## Qué hace ESP32 WiFi Canary y qué no hace

### Siempre funciona de forma pasiva

WiFi Canary utiliza dos modos de radio, nunca simultáneamente:

1. **Modo promiscuo**: recibe e inspecciona tramas de gestión 802.11, como desautenticación y desasociación, sin asociarse a una red.
2. **Modo de escaneo**: busca activamente puntos de acceso WiFi cercanos y los compara con una línea base aprendida.

El dispositivo nunca:
- se asocia ni se conecta a una red;
- captura tramas de datos ni credenciales;
- transmite tramas 802.11;
- guarda datos en memoria flash persistente;
- se comunica por Internet.

**Todo lo que aprende permanece en RAM y se borra al reiniciar.** Es intencional: el canario es un **sensor**, no un dispositivo de captura.

### El LED es la interfaz

No hay pantalla, aplicación ni interfaz web. Toda la salida del dispositivo es un solo **NeoPixel RGB SK6812** conectado al GPIO 27 del M5Stack Atom Lite. El LED comunica cuatro estados:

| Estado del LED | Significado |
|---|---|
| 🔵 Azul (pulso lento) | Inicio, creación de la línea base |
| 🟢 Verde (fijo) | Normal, sin problemas de alta confianza |
| 🟡 Amarillo (fijo) | Precaución, patrón sospechoso detectado |
| 🔴 Rojo (pulso rápido) | Alerta, amenaza de mayor confianza detectada |

El inicio tarda aproximadamente **24 segundos** (3 escaneos de 8 segundos). Cuando el LED deja el azul, ya existe una línea base y empieza la supervisión.

---

## Hardware

### Objetivo principal: M5Stack Atom Lite

El proyecto se diseñó para M5Stack Atom Lite, una plataforma de desarrollo ESP32 completa en una carcasa de 24 × 24 mm.

| Componente | Detalle |
|---|---|
| MCU | ESP32-PICO-D4 |
| LED | Un NeoPixel RGB SK6812 (GPIO 27) |
| Botón | GPIO 39, activo en nivel bajo |
| USB | Puente UART CP2104 |
| Alimentación | USB-C, ~80–120 mA durante el escaneo |

**No se necesita protoboard, componentes externos ni soldadura.** Conéctalo a una fuente USB y funcionará.

### ESP32 DevKit genérico para desarrollo y pruebas

El proyecto incluye un segundo entorno de compilación PlatformIO (`esp32dev`) para placas ESP32 estándar. En esta configuración:

- se usa el LED integrado en GPIO 2 en lugar del NeoPixel;
- se habilita toda la salida de depuración serie;
- la lógica de detección funciona igual que en Atom Lite.

Así, cualquier persona con un ESP32 DevKit de $5 puede usar el proyecto y probar la lógica de detección sin el hardware objetivo.

---

## Proceso de aprendizaje de la línea base

### Por qué importa una línea base

Un canario que se activa ante todas las redes abiertas de una ciudad sería inútil. ESP32 WiFi Canary aprende primero el entorno y luego puntúa las amenazas. La primera fase crea una **tabla de referencia** de puntos de acceso que existen legítimamente en la zona.

### Tres escaneos en 24 segundos

Al iniciarse, el dispositivo ejecuta tres escaneos WiFi consecutivos, separados por una pausa. Al terminar, guarda como línea base el conjunto aprendido de puntos de acceso: SSID, BSSID, tipo de cifrado y potencia de señal.

La salida serie durante esta fase se ve así:

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 18 APs
[canary] baseline scan 2/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 19 APs
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
  ...
[canary] STARTUP → NORMAL  (score=0  "")
```

Cuando el LED cambia de azul a verde, el dispositivo ya funciona por completo.

---

## Qué detecta: categorías de amenazas

WiFi Canary supervisa seis patrones de amenaza. Cada uno suma puntos a una **puntuación de confianza** que determina el estado del LED. *Ningún indicador aislado se considera concluyente*: el modelo acumula señales que se corroboran antes de elevar la alerta.

### 1. Ráfagas de desautenticación y desasociación

Las **tramas de gestión 802.11 con subtipos 10 (desasociación) y 12 (desautenticación)** son herramientas habituales de ataques WiFi. Cualquier dispositivo puede enviarlas, y los clientes que las reciben se desconectan de su punto de acceso.

El canario cuenta estas tramas por MAC de origen durante una ventana móvil de **5 segundos** en **modo promiscuo**.

| Condición | Puntos añadidos |
|---|---|
| ≥ 8 tramas de un origen en 5 s | +2 |
| ≥ 20 tramas de un origen en 5 s | +4 |
| ≥ 5 tramas de desautenticación broadcast | +1 |

**Los umbrales importan**: un cliente que cambia de punto de acceso genera unas pocas tramas legítimas. Las herramientas de ataque producen algo muy distinto: cientos de tramas por segundo sostenidas contra un objetivo. La ventana de 5 segundos y el mínimo de 8 tramas filtran el ruido normal de itinerancia y detectan ráfagas como las de `aireplay-ng`.

### 2. Clon abierto de una red cifrada conocida (evil twin)

**Es la detección de mayor confianza.** Un ataque evil twin suele:

1. Crear una copia abierta, sin contraseña, de un SSID WPA2 conocido.
2. Emitir una señal más fuerte que el punto de acceso real para que los clientes se conecten automáticamente.

Tras aprender la línea base, si un nuevo escaneo encuentra un SSID que antes solo usaba WPA/WPA2/WPA3 y ahora aparece como **OPEN**:

| Condición | Puntos añadidos |
|---|---|
| Mismo SSID, antes cifrado y ahora abierto | +3 |
| BSSID no visto en la línea base | +1 |
| Señal del clon ≥ 10 dB más fuerte que el punto de acceso conocido | +1 |

Un clon abierto del WiFi del hotel que además sea 10 dB más fuerte que el punto de acceso real es un caso de libro. *Esta combinación alcanza 5 puntos (Precaución) en un solo ciclo de escaneo.*

**Ejemplo serie**:

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Falta el punto de acceso cifrado original y hay un clon abierto

Una variante más avanzada: el clon más potente hace que los clientes lo prefieran y, a la vez, expulsa de la red al punto de acceso legítimo mediante desautenticación.

| Condición | Puntos añadidos |
|---|---|
| Desaparece el punto de acceso cifrado de la línea base y aparece una red abierta coincidente | +3 |

Esto cubre casos en que el punto de acceso real sigue transmitiendo, pero pierde la competencia de señal, o sufre una interrupción activa.

### 4. Degradación de seguridad

Se observa el mismo SSID que en la línea base, pero con un cifrado más débil que el registrado.

| Condición | Puntos añadidos |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Descenso de 2 o más niveles de cifrado | +3 |

*Las degradaciones a una red abierta se gestionan en la detección de evil twins, con puntuaciones mayores.* Esta categoría cubre degradaciones parciales que podrían pasar inadvertidas al comparar solo redes abiertas y cifradas.

### 5. SSID duplicado de un proveedor inesperado

El mismo SSID y el mismo tipo de seguridad de un punto de acceso de la línea base, pero con un BSSID de un **OUI de proveedor distinto** (los primeros 3 bytes de la dirección MAC).

| Condición | Puntos añadidos |
|---|---|
| OUI distinto al del punto de acceso de la línea base con el mismo SSID | +1 |
| El clon también es ≥ 10 dB más fuerte | +2 |

*La puntuación es intencionalmente baja.* Las redes empresariales, los sistemas mesh y los puntos de acceso de proveedores de Internet suelen tener legítimamente varios BSSID del mismo SSID con distintos proveedores. Esta señal debe sumarse a otras evidencias, no activar una alerta por sí sola.

### 6. Inundación de beacons o SSID

Cuenta SSID nuevos, ausentes de la línea base, que aparecen durante una **ventana móvil de 30 segundos**.

| Condición | Puntos añadidos |
|---|---|
| ≥ 15 SSID nuevos en 30 s | +2 |
| ≥ 30 SSID nuevos en 30 s | +3 |

Los ataques de **inundación de beacons** difunden miles de SSID falsos para confundir las tablas de escaneo o impedir los beacons legítimos. Quince SSID desconocidos nuevos en 30 segundos es inusual en la mayoría de los entornos.

---

## Modelo de puntuación de confianza

Todas las señales detectadas se suman en una **puntuación de amenaza** entera, que controla el LED:

| Rango de puntuación | Estado del LED |
|---|---|
| 0–2 | Normal (verde) |
| 3–5 | Precaución (amarillo) |
| 6+ | Alerta (rojo, pulso rápido) |

### Degradación de la puntuación

La puntuación **baja un punto cada 60 segundos** si no aparecen nuevos eventos. Es una decisión de diseño importante:

- Una ráfaga de desautenticación eleva la puntuación a Precaución. Si el ataque termina, vuelve a Normal por sí sola en unos minutos.
- Un ataque sostenido mantiene el estado de Alerta mientras continúen los eventos.
- El dispositivo se restablece sin intervención ni reinicio.

Esto significa que:
- **Las anomalías breves** (itinerancia o redes vecinas transitorias) se resuelven solas.
- **Los ataques sostenidos** siguen señalados.
- **No hay fatiga por alertas** ante eventos únicos que no se repiten.

### Restablecimiento con el botón

Al pulsar el botón GPIO 39 de Atom Lite se realizan dos acciones:

1. Se vuelca la tabla completa de puntos de acceso al puerto serie, lo que permite auditar lo que ve el dispositivo.
2. La puntuación vuelve a 0 y el LED regresa de inmediato al verde para observar limpio el siguiente escaneo.

---

## Compilar y flashear

### Requisitos

- **PlatformIO** (CLI o extensión de VS Code)
- **M5Stack Atom Lite** (o ESP32 DevKit para pruebas)
- Cable USB-C

### Flashear en M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Compilar y flashear
pio run -e atom-lite --target upload

# Abrir el monitor serie a 115200 baudios
pio device monitor -b 115200
```

### Flashear en un ESP32 DevKit genérico

```bash
pio run -e esp32dev --target upload
```

La compilación DevKit usa GPIO 2 (LED integrado) y muestra el registro serie completo. No controla ningún NeoPixel. La lógica de detección es idéntica a la de Atom Lite.

### Estructura del proyecto

```
esp32-wifi-canary/
├── main.cpp              # Toda la lógica del firmware
├── platformio.ini        # Entornos de compilación (atom-lite, esp32dev)
├── partitions_4mb.csv    # Tabla de particiones de flash de 4 MB
└── README.md
```

Todo el firmware está en **un único archivo fuente C++**. La lógica de detección no usa bibliotecas externas, solo el framework ESP32 Arduino para escaneos WiFi, callbacks en modo promiscuo y control del NeoPixel.

### Entornos de platformio.ini

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

El entorno `atom-lite` usa la definición de placa `m5stick-c` (mismo chip ESP32-PICO-D4 y asignación de pines compatible con el NeoPixel en GPIO 27).

---

## Referencia de salida serie

El dispositivo registra información detallada a **115200 baudios**. Todas las líneas empiezan por `[canary]` para filtrarlas fácilmente.

### Secuencia de inicio

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
...
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
[canary] STARTUP → NORMAL  (score=0  "")
```

### Eventos de detección

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Cambios de puntuación

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

El registro serie permite saber qué vio el dispositivo, cuándo y por qué cambió la puntuación. También sirve como **registro de auditoría pasivo** aunque no estés mirando el LED.

---

## Notas de detección y limitaciones prácticas

El README explica con honestidad lo que este dispositivo no puede hacer. Conviene detallar esas limitaciones.

### Causas de falsos positivos

**Las redes empresariales y mesh** son la mayor fuente de falsos positivos. Una empresa grande, un hotel o una red mesh como Eero o Google WiFi puede mostrar legítimamente:

- Varios BSSID para el mismo SSID con distintos OUI de proveedor (detección de proveedor).
- Diferencias de configuración de seguridad entre bandas (detección de degradación).
- Puntos de acceso que aparecen y desaparecen cuando la red mesh se ajusta.

**Los routers Airbnb y SOHO** con varios SSID para distintas bandas también pueden activar discrepancias de OUI si las radios de 2,4 y 5 GHz usan bloques MAC consecutivos de proveedores distintos.

*Cambios transitorios de redes vecinas*: una red cifrada que desaparece temporalmente del escaneo y vuelve con otros parámetros (actualización de firmware, reinicio o reconfiguración) puede activar una detección momentánea.

La puntuación y su degradación están diseñadas para *reducir, no eliminar*, los falsos positivos.

### Causas de falsos negativos

Un **ataque evil twin bien diseñado** que:

- Suplanta el BSSID exacto del punto de acceso legítimo para que coincida el OUI.
- Usa el mismo tipo de seguridad, con una configuración IE WPA2 correcta.
- Mantiene una señal a menos de 10 dB de la del punto de acceso real.

*Puede no sumar suficientes puntos para llegar a Precaución.* La parte de desautenticación necesaria para apartar clientes del punto real sumaría puntos, pero un atacante sofisticado que reduzca las tramas podría quedar bajo el umbral.

### Brecha al cambiar de radio

**La radio ESP32 no puede estar en modo promiscuo y escanear activamente puntos de acceso al mismo tiempo.** El firmware alterna entre ambos modos. Por eso, **las tramas de desautenticación que lleguen durante los ~3 segundos del escaneo no se capturan**. Un atacante podría ajustar sus ráfagas a esos intervalos, aunque necesitaría conocer el calendario de escaneo.

### Solo 2,4 GHz

La radio ESP32 funciona en 2,4 GHz. **No escanea ni supervisa redes de 5 y 6 GHz.** No detectará evil twins que operen solo en 5 GHz.

### Alcance pasivo

La detección de desautenticación requiere que el dispositivo reciba las tramas. Un atacante lejano, con antena muy direccional o que ataque a un cliente lejos del canario, podría emitir señales demasiado débiles para activar los contadores.

---

## Casos de uso

### Viajes con trabajo sensible

El canario está pensado principalmente para viajar. Conéctalo al USB de un portátil, a una toma USB de hotel o a una batería portátil para aprender el entorno del hotel o centro de conferencias. Una aparición posterior de un clon abierto del SSID del hotel, el escenario más común, activará como mínimo Precaución.

### Cafeterías y WiFi público

Los entornos WiFi abiertos son un objetivo frecuente para evil twins. La línea base permite aprender el punto de acceso legítimo al llegar y vigilar SSID rivales que aparezcan junto a él.

### Concienciación y formación de seguridad

La salida serie ofrece un registro detallado y legible de lo que observa. En una formación, mostrar en tiempo real una ráfaga de desautenticación y el cambio de color del LED es mucho más efectivo que una presentación.

### Supervisión pasiva de laboratorio

En un laboratorio doméstico u oficina pequeña, el canario sirve como monitor ambiental permanente. El LED muestra el estado de un vistazo y el botón permite consultar la tabla de redes actual.

---

## Notas de arquitectura

### Por qué usar una puntuación única en vez de alertas separadas

El modelo suma señales distintas en un solo número, en lugar de presentar categorías separadas. Es una decisión deliberada de interfaz: el dispositivo usa un LED con tres estados. Las alertas independientes exigirían una pantalla o aplicación. *La puntuación convierte señales ruidosas y parcialmente correlacionadas en un indicador práctico.*

### Por qué degradar la puntuación

Sin degradación, un falso positivo aislado requeriría pulsar el botón. Con una reducción cada 60 segundos, las anomalías breves desaparecen en minutos. **Así, el canario funciona sin supervisión** en una mochila, habitación de hotel o coche y vuelve a su estado normal tras eventos transitorios.

### Por qué hacer tres escaneos de línea base

Un escaneo podría pasar por alto un punto de acceso que no transmitía en ese momento, por una pausa de escaneo o un corte temporal. *Tres escaneos en unos 24 segundos ofrecen una imagen más completa del entorno estable antes de iniciar la supervisión.*

---

## Contribuciones y estado del proyecto

El proyecto está disponible en [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary) con una licencia de uso pasivo. El código consta de un único `main.cpp`, fácil de leer, auditar y ampliar.

Quienes usan PlatformIO y ESP32 pueden compilar el proyecto sin modificaciones para Atom Lite o DevKit estándar.

---

## Comparación con otros métodos de supervisión WiFi

| Método | ¿Pasivo? | Sin credenciales | Una salida LED | Formato para viajar |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (portátil) | ✅ | ✅ | ❌ (requiere pantalla) | ❌ (pesado) |
| WiFi Pineapple | ❌ (activo) | ❌ | ❌ | Parcial |
| IDS inalámbrico (empresa) | ✅ | ✅ | ❌ (requiere infraestructura) | ❌ |
| Escaneo manual (aplicación móvil) | Parcial | ✅ | ❌ | ✅ |

El canario ocupa un nicho específico: **supervisión ambiental permanente, sin interacción ni conexión de red**, en un formato que cabe en un llavero o bolso de portátil.

---

## Conclusión

ESP32 WiFi Canary hace una sola cosa: observa el entorno de 2,4 GHz y cambia de color cuando algo parece sospechoso. No es un sistema completo de detección de intrusiones inalámbricas, una herramienta de captura de paquetes ni un analizador forense. Es un canario: un sensor pasivo que avisa cuando el entorno se vuelve peligroso.

El **modelo de puntuación de confianza**, la **degradación de la puntuación** y la **línea base de tres fases** afrontan el problema de falsos positivos de los sensores ambientales. El dispositivo puede funcionar sin supervisión en un hotel o centro de conferencias y señalar anomalías importantes sin reaccionar al ruido normal de la red.

Para quien prepara un kit de seguridad portátil, trabaja con infraestructura WiFi no confiable o busca un proyecto ESP32 útil, WiFi Canary merece una tarde y un M5Stack Atom Lite de $15.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
