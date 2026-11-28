---
title: "Proyecto Flock-You: Guía completa de hardware de contravigilancia y configuración 2026"
date: 2026-05-24
lastmod: 2026-11-19
toc: true
draft: false
description: "Guía técnica completa del proyecto de código abierto Flock-You para detectar cámaras ALPR de Flock Safety usando hardware basado en ESP32. Incluye instrucciones de configuración, detalles de firmware y opciones de compra."
genre: ["Hardware de seguridad", "Contravigilancia", "Tecnología de privacidad", "Proyectos de código abierto", "Desarrollo ESP32", "Monitoreo WiFi", "Herramientas de privacidad", "Derechos digitales", "Modificación de hardware", "Seguridad de red"]
tags: ["Proyecto Flock-You", "Detección ALPR", "ESP32-S3", "Detección OUI WiFi", "Hardware contra la vigilancia", "Detección Flock Safety", "Seguridad de código abierto", "Hardware de privacidad", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "Modo promiscuo WiFi", "Supervisión 802.11", "Colonel Panic Tech", "STS Collective", "Dispositivos de privacidad", "Detección de vigilancia", "Escaneo WiFi", "Proyecto GitHub", "colonelpanichacks", "Firmware ESP32", "Guía de configuración de hardware", "Herramientas de privacidad DIY", "Supervisión de red", "Base de datos OUI", "Detección de solicitudes de sondeo comodín", "Análisis de tramas", "Detección de cámaras ALPR", "Tecnología de privacidad", "Hardware de detección", "Arduino ESP32", "Platform.io", "Sistemas integrados", "Detección RF", "Procesamiento de señales", "Ingeniería de privacidad", "Tecnología contra la vigilancia", "Investigación de seguridad", "Activismo por la privacidad", "Hardware abierto", "Protección de la privacidad", "Firmware de detección", "Detección móvil", "Proyectos de privacidad", "Comparativa de hardware"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Una ilustración que muestra un dispositivo basado en ESP32 en primer plano, escaneando señales WiFi. Ondas coloridas representan diferentes intensidades de señal sobre un fondo oscuro."
coverCaption: "Soluciones de hardware de código abierto para detectar cámaras de vigilancia ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Guía técnica completa para construir y usar dispositivos de detección Flock-You**

## Introducción: Contravigilancia de código abierto

El **proyecto Flock-You** es una **iniciativa comunitaria de código abierto** para detectar y mapear la infraestructura de vigilancia ALPR de Flock Safety. Alojado en GitHub en **colonelpanichacks/flock-you**, este proyecto utiliza hardware ESP32 asequible para identificar cámaras Flock a través de sus **firmas de red WiFi**.

**Flock-You detecta únicamente cámaras Flock Safety por Wi-Fi.** No detecta simuladores de estaciones celulares como Stingray ni dispositivos de rastreo personales (AirTags, Tile u otros dispositivos Bluetooth desconocidos) que te acompañen. Para eso, consulta **[Cómo flashear dispositivos Rayhunter: guía completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** para detectar captadores IMSI y **[Eye Spy: detector pasivo de vigilancia y rastreadores con ESP32](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** para detectar AirTags y otros dispositivos de seguimiento. Los tres funcionan en la misma familia de hardware ESP32 económico.

Esta guía completa cubre todo, desde la **metodología técnica** detrás de la detección de Flock hasta las **instrucciones de configuración paso a paso** para tres plataformas de hardware, la **instalación de firmware** y la **información de compra de proveedores autorizados**. Ya sea un defensor de la privacidad, investigador de seguridad o ciudadano preocupado, esta guía le permitirá construir o comprar su propio dispositivo de detección.


*El hardware de Flock Safety está desplegado casi por completo en Estados Unidos, con una presencia menor en Canadá. Fuera de Norteamérica, la lista de OUI y las firmas de sondeo que aparecen a continuación no coincidirán con nada cercano. El hardware sigue siendo útil para la investigación, pero no encontrará una infraestructura que no exista allí.*

Para el contexto sobre por qué esta tecnología importa, lea nuestro artículo complementario: **[Vigilancia con cámaras Flock Safety: Prevalencia, preocupaciones de privacidad y estrategias de protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

¿Quiere ver dónde ya se han mapeado las cámaras Flock? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** es una herramienta de código abierto que traza 40.000+ cámaras Flock Safety sospechosas en todo el mundo usando datos WiFi WiGLE y huellas digitales OUI, actualizado diariamente. Fuente en **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

### De un vistazo: tres plataformas

*Las especificaciones completas, ventajas e inconvenientes de cada plataforma están más abajo. Ve a las [instrucciones de configuración](#instrucciones-de-configuración-paso-a-paso) si ya sabes cuál quieres.*


| Plataforma | Precio | Configuración | Ideal para |
|---|---|---|---|
| **DIY ESP32** | 5–12 $ | Placa de pruebas sin soldar, 10–15 min | Montajes económicos y aprender cómo funciona la detección |
| **M5 Atom Lite** (preinstalado) | 49,99 $ | Conectar y usar, sin configuración | Uso inmediato sin montaje DIY |
| **OUI-SPY** | 85 $ | Flashear una vez y elegir el modo en el menú Wi-Fi | Detección multimodo (ALPR, drones y BLE) |

______

## Comprender la metodología de detección Flock-You

### La base técnica

Las cámaras Flock Safety contienen **módulos WiFi integrados** para conectividad y gestión remota. Estos módulos transmiten firmas de red identificables detectables por dispositivos que operan en **modo de monitoreo promiscuo WiFi**. El proyecto Flock-You explota esta característica a través de:

#### 1. Detección WiFi OUI (Organizationally Unique Identifier)

Cada interfaz de red tiene una **dirección MAC** que consta de:
- **Primeros 3 bytes (24 bits)**: OUI, que identifica al fabricante
- **Últimos 3 bytes**: Identificador específico del dispositivo

Los investigadores **@NitekryDPaul** y la comunidad **DeFlockJoplin** descubrieron **31 OUI específicos** presentes de forma consistente en las implementaciones de cámaras Flock Safety:

```
OUI primarios de Espressif (módulos basados en ESP32):
D4:AD:FC - Espressif Inc. (ESP32-S3 común)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (variantes ESP32-S3)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (basado en ESP32)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (basado en ESP32)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

OUI adicionales identificados en implementaciones de Flock:
[... 21 OUI de fabricantes adicionales ...]
```

Al escanear el tráfico WiFi en modo promiscuo, **el dispositivo identifica cualquier equipo que transmita tramas con estos OUI**.

#### 2. Detección de solicitudes de sonda comodín

Las cámaras Flock envían periódicamente **solicitudes de sonda comodín** para buscar redes disponibles. Estas solicitudes tienen características distintivas:

- **Trama de gestión 802.11**: Tipo=0, Subtipo=4
- **Elemento de información SSID**: Longitud=0 (vacío/comodín)
- **Estructura de trama**: patrón predecible en el tiempo entre solicitudes
- **Elementos de información específicos del fabricante**: indicadores adicionales en la carga de la trama

El firmware analiza estos **patrones de solicitudes de sonda** para aumentar la confianza en la identificación de cámaras Flock, más allá de la coincidencia OUI.

#### 3. Monitorización Wi-Fi en modo promiscuo

El funcionamiento Wi-Fi estándar solo recibe tramas dirigidas a tu dispositivo. El **modo promiscuo** captura todas las tramas Wi-Fi dentro del alcance:

- **Estructura de trama 802.11**: analiza los campos addr1, addr2 y addr3
- **Tramas de gestión**: solicitudes de sonda, tramas beacon y solicitudes de asociación
- **Tramas de datos**: revelan patrones de actividad de la red
- **Tramas de control**: ACK, RTS y CTS aportan información temporal

Los microcontroladores ESP32 admiten el modo promiscuo mediante la **API esp_wifi**, lo que permite crear dispositivos de detección de bajo coste.

#### 4. Análisis de la intensidad de señal

Los dispositivos de detección miden el **RSSI (indicador de intensidad de señal recibida)** para:
- **Estimar la distancia** a las cámaras detectadas
- **Triangular ubicaciones** con varias mediciones
- **Filtrar falsos positivos** según las características de señal esperadas
- **Crear mapas de calor** de la densidad de cámaras

### Precisión de detección y falsos positivos

La precisión depende mucho del entorno. Una prueba de campo documentada ofrece una referencia concreta: la comunidad **DeFlockJoplin** detectó **11 de 12 cámaras Flock conocidas y registró solo 2 falsos positivos** durante una prueba en coche.

- **Referencia de campo**: 11 de 12 cámaras confirmadas detectadas y 2 falsos positivos (prueba de DeFlockJoplin)
- **Alcance de detección**: 50–300 pies, según los obstáculos y la antena
- **Puntuación de confianza**: combinar la coincidencia OUI, la firma de solicitudes wildcard y el umbral RSSI reduce las falsas alarmas
- **Los resultados varían**: el entorno de señal, la antena y la versión del firmware afectan a la precisión real

**Fuentes habituales de falsos positivos**:
- **Placas de desarrollo ESP32** usadas en otros dispositivos IoT
- **Productos comerciales basados en ESP32**, como equipos domésticos inteligentes y sensores
- **Otras cámaras de vigilancia** con componentes similares
- **Equipos de prueba Wi-Fi** utilizados por técnicos

**Estrategias de mitigación**:
- **Combinar varias señales**: coincidencia OUI, patrón de solicitudes de sonda y verificación física
- **Correlacionar la ubicación**: comparar detecciones con ubicaciones de cámaras conocidas
- **Confirmar visualmente**: comprobar el lugar desde una ubicación segura y pública después de una detección electrónica
- **Usar una base comunitaria**: validar las detecciones de forma colaborativa

{{< figure src="flockyou-oui-detection-methodology-overview.webp" alt="Diagrama de detección Flock-You: el ESP32 en modo Wi-Fi promiscuo compara MAC con OUI conocidos, comprueba sondas comodín y puntúa RSSI" >}}

{{< stscollective-ad "flockyou" >}}

## Comparación de plataformas de hardware

Hay tres plataformas principales para detectar Flock-You, cada una con ventajas distintas.
*Las tres plataformas usan el mismo método de detección: escaneo pasivo en modo promiscuo de WiFi para buscar OUI conocidos de cámaras Flock y firmas de solicitudes de sondeo comodín. Ninguna detecta Bluetooth. El firmware de Flock-You dejó de admitir la detección BLE en la primavera de 2026, cuando dejó de funcionar de forma fiable. Por eso, todas las plataformas de esta guía usan solo WiFi.*
### Tabla de descripción general de plataformas

| Función | DIY ESP32 | M5 Atom Lite (preflashado) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Fabricante** | DIY / Varios proveedores | STS Collective | Colonel Panic Tech |
| **Precio** | $5-12 | $49.99 | $85 |
| **Procesador** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Listo para usar** | No (DIY) | Sí (preflashado) | Sí (multi-modo) |
| **Pantalla** | Opcional | LED RGB (matriz 5×5) | Ninguna |
| **Batería** | Opcional | Externa recomendada | No incluida |
| **GPS** | Opcional | No | No |
| **Alertas** | Zumbador + LED | LED RGB (azul=detección) | Zumbador integrado |
| **Registro de datos** | Opcional | No | No |
| **Carcasa** | Impresión 3D o ninguna | Módulo plástico compacto | Ninguna (PCB desnuda) |
| **Firmware** | Flash manual | FlockYou precargado | Multi-modo (4 firmwares) |
| **Mejor para** | Aficionados DIY, aprendizaje | Presupuesto listo para usar | Detección multipropósito |
| **Dificultad de configuración** | Medio-Avanzado | Sin configuración | Sin configuración |
| **Peso** | 20–50 g (según el modelo) | 18 g (sin accesorios) | ~40 g |
| **Dimensiones** | Variables | 24 × 24 × 14 mm | Placa PCB |

### Análisis detallado de plataformas

#### 1. Construcción DIY ESP32 ($5-12)

**Descripción general**: Opción más asequible usando placas de desarrollo ESP32 estándar con firmware de código abierto.


**Especificaciones de hardware**:
- **Microcontrolador**: ESP32-WROOM-32 o similar (doble núcleo, 240 MHz)
- **Wi-Fi**: 802.11 b/g/n, compatible con el modo promiscuo
- **Memoria**: 520 KB de SRAM y 4 MB o más de memoria flash
- **Pantalla**: opcional, basta con el LED integrado
- **Alimentación**: por USB o batería externa
- **Zumbador**: módulo de zumbador pasivo opcional (KY-006)
- **Indicadores**: LED integrado y zumbador opcional
- **Ampliación**: compatible con placa de pruebas y fácil de modificar

**Firmware**: Fork de código abierto **simeononsecurity/flock-you-esp32**:
- Modificado para hardware ESP32 estándar (GPIO 25, 2, 17)
- Melodía de inicio de Super Mario Bros. (confirma el funcionamiento del zumbador)
- Dos pitidos ascendentes rápidos en nueva detección
- Pitidos de heartbeat cada 10 segundos durante el seguimiento activo
- Soporte de panel Flask para recorridos de reconocimiento de redes Wi-Fi con GPS
- Exportación a formatos JSON, CSV, KML

**Opciones de montaje**:
- **Solo LED ($5)**: ESP32 básico y cable USB, solo señal visual
- **Placa de pruebas ($9–11)**: añade zumbador pasivo, placa y cables puente para alertas sonoras
- **Con carcasa ($10–12)**: añade una carcasa impresa en 3D con tapa de cierre a presión

**Ventajas**:
- ✅ Opción más barata (85-95% de ahorro vs OUI-SPY)
- ✅ Completamente de código abierto y modificable
- ✅ Usa placas ESP32 ampliamente disponibles
- ✅ Educativo, enseña sistemas embebidos
- ✅ Documentación y guías completas
- ✅ Hay archivos para imprimir una carcasa en 3D
- ✅ **La misma precisión de detección que los dispositivos premium**

**Desventajas**:
- ❌ Requiere ensamblaje DIY
- ❌ Se necesita flasheo manual del firmware
- ❌ Sin batería integrada
- ❌ Solo ofrece alertas de audio básicas, sin pantalla
- ❌ Se necesita tiempo para conseguir los componentes

**Comprar componentes**:
- **Amazon**: busca “ESP32 DevKit” o “ESP32 Breadboard Kit”
- **AliExpress/eBay**: hay descuentos por volumen
- **Adafruit**: componentes seleccionados y tutoriales

**Recursos de configuración**:
- **Repositorio de GitHub**: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Guía de montaje**: ensamblaje sin soldadura en 10–15 minutos
- **Archivos de la carcasa**: diseño paramétrico OpenSCAD y archivos STL

**Mejor para**: Makers, estudiantes, defensores de la privacidad con presupuesto limitado.

---

{{< figure src="flockyou-diy-esp32-solderless-breadboard-build.webp" alt="Montaje Flock-You con ESP32 en placa sin soldar, DevKit, zumbador pasivo y cables en GPIO 25, 2 y 17" >}}

#### 2. M5 Atom Lite preflashado por STS Collective ($49.99)

**Descripción general**: Dispositivo de detección compacto preflashado, listo para usar.

**Especificaciones de hardware**:
- **Microcontrolador**: ESP32-PICO-D4 (doble núcleo, 240 MHz)
- **Wi-Fi**: 802.11 b/g/n, compatible con el modo promiscuo
- **Memoria**: 520 KB de SRAM y 4 MB de memoria flash
- **Pantalla**: matriz LED RGB 5×5 (WS2812C NeoPixel)
- **Alimentación**: 5 V por USB-C o conector Grove
- **Batería**: no incluida; se recomienda una batería USB externa
- **Indicador**: LED RGB programable (azul = detección)
- **Botones**: un botón programable
- **E/S**: conector Grove para ampliaciones
- **Tamaño**: ultracompacto, 24 × 24 × 14 mm
- **Carcasa**: módulo de plástico resistente


**Firmware**: versión personalizada de FlockYou por STS Collective (propietaria):
- Precargado y listo para usar
- Alerta LED azul cuando detecta una cámara Flock
- Basado en la investigación FlockYou de colonelpanichacks
- No requiere configuración ni flasheo
- Funcionamiento sencillo, conectar y usar
- Compatibilidad opcional con panel de control

**Ventajas**:
- ✅ Preflasheado, sin configuración técnica
- ✅ Solución lista para usar y asequible
- ✅ Muy compacto y portátil
- ✅ Plataforma de hardware probada
- ✅ LED azul sencillo para indicar una detección
- ✅ Alimentación USB-C (coche, batería externa u ordenador)
- ✅ Soporte de un proveedor con control de calidad
- ✅ Precio habitual $99.99, rebajado a $49.99

**Desventajas**:
- ❌ No tiene batería integrada (necesita alimentación USB)
- ❌ Pantalla limitada (solo LED RGB, sin pantalla)
- ❌ *El firmware es propietario y no es de código abierto por ahora*
- ❌ No registra datos sin conectarlo a un ordenador
- ❌ Un solo botón limita las funciones

**Ideal para**: quienes quieren detectar cámaras de inmediato, priorizan la portabilidad y prefieren una solución lista para usar con una señal LED sencilla.


**Compra**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Descuento exclusivo**: Ahorra hasta un 20 % en productos de STS Collective. Usa el código **SIMEONONSECURITY** al pagar o [compra con el descuento aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

{{< figure src="flockyou-m5-atom-lite-pocket-size-comparison.webp" alt="M5 Atom Lite preflasheado entre dos dedos, con tamaño compacto y LED RGB azul de detección" >}}

---

#### 3. OUI-SPY de Colonel Panic Tech ($85)

**Descripción general**: Placa de detección multimodo con cuatro modos de firmware seleccionables desde un menú Wi-Fi.


**Especificaciones de hardware**:
- **Microcontrolador**: ESP32-S3 con doble núcleo Xtensa LX7 y 8 MB de memoria flash
- **Wi-Fi**: 802.11 b/g/n, compatible con el modo promiscuo
- **Memoria**: 8 MB de memoria flash
- **Pantalla**: ninguna (PCB sin carcasa, con indicadores LED)
- **Batería**: no incluida
- **Carga**: alimentación y programación por USB-C
- **Almacenamiento**: ninguno (los modos solo detectan)
- **Indicadores**: zumbador PWM integrado con tonos propios de cada modo
- **Botones**: botón BOOT para cambiar de modo
- **Antena**: antena adhesiva integrada de 2,4 GHz; se puede cambiar por otra de mayor alcance
- **Carcasa**: ninguna (PCB desnuda con diseño impreso)
- **Función única**: aleatorización de la dirección MAC en cada arranque

**Firmware**: OUI-SPY Unified Blue con **4 modos seleccionables**:
1. **Modo Detector**: Escáner BLE multi-objetivo con filtrado OUI + portal de configuración web
2. **Modo Foxhunter**: Rastreador de proximidad RSSI de objetivo único para radiogonometría
3. **Modo Flock-You**: Detección de cámaras Flock Safety y Raven con recorridos de reconocimiento de redes Wi-Fi con GPS, exportación JSON/CSV/KML
4. **Modo Sky Spy**: Detector RemoteID de drones (OpenDroneID / ASTM F3411) con seguimiento multi-dron

**Selección de modo**:
- Menú de inicio Wi-Fi en `192.168.4.1`
- Mantén pulsado el botón BOOT durante dos segundos para volver al selector
- El último modo se conserva después de apagar y encender el dispositivo
- Cada modo tiene su propio tono de inicio y alertas de estilo retro
- Funcionamiento solo de detección, sin transmitir

**Ventajas**:
- ✅ Cuatro modos de firmware en un solo dispositivo
- ✅ Antena conmutable (integrada o externa MMCX)
- ✅ Zumbador integrado con melodías de inicio personalizadas
- ✅ Diseño de PCB de nivel profesional
- ✅ Multipropósito: ALPR, drones, BLE y radiogoniometría
- ✅ Desarrollo y actualizaciones activos
- ✅ Del creador original del proyecto Flock-You

**Desventajas**:
- ❌ Precio más alto para detección Flock únicamente
- ❌ Sin carcasa (PCB desnuda)
- ❌ Sin batería integrada
- ❌ Sin pantalla (solo hay respuesta de audio en la mayoría de los modos)
- ❌ Complejidad innecesaria para una detección básica
- ❌ Se necesita GPS externo para las funciones de recorridos de reconocimiento de redes Wi-Fi

**Ideal para**: detección de vigilancia polivalente, usuarios que buscan detección de drones, ALPR y BLE en un solo dispositivo, aplicaciones de radiogoniometría y quienes quieren una antena intercambiable y funciones avanzadas.

**Compra**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)

______

{{< figure src="flockyou-oui-spy-multimode-board-pcb.webp" alt="Placa OUI-SPY ESP32-S3 sin carcasa con antena, zumbador y botón de arranque; una pantalla muestra el menú Wi-Fi de cuatro modos" >}}

## Instrucciones de configuración paso a paso

### Guía de configuración 1: montaje DIY con ESP32

**Consulta la guía completa** en el [repositorio de GitHub](https://github.com/simeononsecurity/flock-you-esp32).

#### Inicio rápido

1. **Hardware necesario**:
   - Placa ESP32 DevKit ($5–6)
   - Cable USB (Micro-USB o USB-C, según la placa)
   - Opcional: zumbador pasivo (KY-006), placa de pruebas y cables puente
   - Opcional: carcasa impresa en 3D

2. **Preparar el software**:
   ```bash
   # Instalar PlatformIO
   pip install platformio

   # Clonar el repositorio
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32

   # Flashear el firmware
   pio run -t upload
   pio device monitor
   ```

3. **Montar el hardware** (si usas un zumbador):
   - Positivo del zumbador → GPIO 25
   - Negativo del zumbador → GND
   - Indicador LED → GPIO 2 (integrado)
   - Alimentación por USB

4. **Confirmar el arranque**:
   - Suena la melodía de Super Mario Bros. 1-2 si conectaste un zumbador
   - El LED parpadea mientras se realiza el escaneo
   - El monitor serie muestra la inicialización de “Flock-You ESP32”

5. **Alertas de detección**:
   - **Nueva detección**: dos pitidos ascendentes rápidos (2000 → 2800 Hz)
   - **Señal periódica**: dos pitidos cada 10 segundos mientras se realiza el seguimiento
   - **LED**: parpadea con cada detección

6. **Recorridos de reconocimiento Wi-Fi con GPS** (opcional):
   - Conecta el dispositivo a un ordenador por USB
   - Ejecuta el panel Flask con `cd api && python flockyou.py`
   - Abre `http://localhost:5000`
   - Conecta un GPS o usa la ubicación del navegador
   - Exporta las detecciones a JSON, CSV o KML

**Guía de montaje completa, archivos de la carcasa y solución de problemas**: consulta el README del repositorio en GitHub.

---

### Guía de configuración 2: M5 Atom Lite preflashado (STS Collective)

#### Inicio rápido

1. **Revisar el contenido de la caja**:
   - Dispositivo M5 Atom Lite con el firmware FlockYou preinstalado
   - Comprueba en la ficha del producto si incluye un cable USB-C

2. **Encender**:
   - Conecta una fuente USB-C, como una batería externa, un puerto USB del coche, un adaptador de pared o un ordenador
   - El dispositivo arranca automáticamente
   - Se inicializa la matriz LED RGB

3. **Uso**:
   - **Inactivo/escaneando**: el LED muestra un patrón de escaneo
   - **Detección**: el LED se ilumina en **AZUL** al detectar una cámara Flock
   - **Botón**: púlsalo para volver a escanear o reiniciar

4. **Uso portátil**:
   - Conecta una batería USB (5000 mAh ofrecen unas 20 horas)
   - Coloca el dispositivo en el portavasos, una bolsa o un bolsillo
   - El LED se ve a través de la carcasa translúcida

5. **Conectar el panel** (opcional):
   - Conecta el dispositivo a un ordenador por USB-C
   - Instala el panel FlockYou según las instrucciones de STS Collective
   - Consulta las detecciones en directo en el navegador

**Advertencia**: *Este firmware es propietario. Al instalar una versión de código abierto se borrará de forma permanente el firmware de STS.*

---

### Guía de configuración 3: placa multimodo OUI-SPY

#### Configuración inicial

1. **Contenido del paquete**:
   - Placa PCB OUI-SPY sin carcasa
   - Cable USB-C
   - Guía de inicio rápido

2. **Primer encendido**:
   - Conecta la alimentación USB-C a un ordenador, adaptador de pared o batería externa
   - El dispositivo anuncia la red Wi-Fi `OUISPY-[ID]`
   - El zumbador reproduce el tono de arranque del modo actual

3. **Seleccionar un modo Wi-Fi**:
   - Conecta el teléfono o el ordenador a la red Wi-Fi de OUI-SPY
   - Abre `http://192.168.4.1` en el navegador
   - La interfaz web ofrece cuatro modos de firmware:
     1. **Detector**: escáner BLE para varios objetivos
     2. **Foxhunter**: localización de señales de radio
     3. **Flock-You**: detección de cámaras ALPR
     4. **Sky Spy**: detección de drones mediante Remote ID
   - Elige el modo y pulsa «Activate»

4. **Usar el modo Flock-You**:
   - El dispositivo se reinicia en modo Flock-You
   - El zumbador reproduce el tono de inicio de Flock-You
   - Empieza a buscar 31 OUI conocidos
   - **Alerta de detección**: el zumbador emite un patrón distintivo
   - El último modo seleccionado se conserva al apagar y encender el dispositivo

5. **Cambiar de modo**:
   - Mantén pulsado el botón **BOOT** durante dos segundos
   - El dispositivo vuelve al selector de modos Wi-Fi
   - Vuelve a conectarte a la red Wi-Fi y selecciona otro modo

#### Opción avanzada: cambiar la antena

6. **Cambiar la antena** (para ampliar el alcance):
   - De forma predeterminada, se usa la antena adhesiva integrada
   - Puedes soldar una antena de mayor ganancia para ampliar el alcance
   - Es una modificación de hardware, no una opción de software. Comprueba en colonelpanic.tech el conector vigente antes de comprar otra antena

#### Montaje

7. **Instalación en vehículo o lugar fijo**:
   - *La placa no incluye carcasa. Protégela antes de instalarla.*
   - Opciones:
     - Imprime una carcasa personalizada en 3D
     - Fíjala al salpicadero con velcro
     - Usa cinta adhesiva de doble cara
     - Usa una caja para proyectos electrónicos
   - Deja accesible el puerto USB-C para la alimentación

#### Exportar datos (modo Flock-You)

8. **Recorridos de reconocimiento Wi-Fi con GPS**:
   - Conecta un módulo GPS externo, que no está incluido
   - El dispositivo registra las detecciones con coordenadas
   - Descarga los archivos de datos desde la interfaz web
   - Exporta a JSON, CSV o KML

**Nota**: consulta colonelpanic.tech para obtener actualizaciones de firmware e instrucciones de OUI-SPY Unified Blue.

______

## Guía de compra e información de proveedores

### Proveedores autorizados

#### Colonel Panic Tech (colonelpanic.tech)

**Productos disponibles**:
- **OUI-SPY** ($85): dispositivo de detección Flock listo para usar
- **Kits DIY** ($55): componentes, PCB y guía de montaje
- **Módulo GPS adicional** ($18): módulo GPS-6M compatible
- **Accesorios**: antenas, carcasas y mejoras de batería

**Por qué comprar a Colonel Panic**:
- ✅ Directamente del desarrollador del hardware OUI-SPY
- ✅ Firmware más reciente preinstalado
- ✅ Incluye soporte técnico
- ✅ Enfoque de código abierto, con esquemas disponibles
- ✅ Foro comunitario activo

**Envío**:
- Estados Unidos: 3–5 días hábiles
- Internacional: 7–14 días
- Envío gratuito en pedidos superiores a $100

**Garantía**: 90 días para el hardware y actualizaciones de firmware de por vida

**Sitio web**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Productos disponibles**:
- **M5 Atom Lite preflashado** ($49.99): dispositivo de detección Flock listo para usar
- **Accesorios**: compatibles con varias plataformas ESP32

**Por qué comprar a STS Collective**:
- ✅ Dispositivos preflasheados y listos para usar
- ✅ Control de calidad y pruebas
- ✅ Precios asequibles
- ✅ Atención al cliente

**Envío**:
- Estados Unidos: 2–4 días hábiles por Priority Mail
- Internacional: 7–21 días
- Hay opciones de envío urgente

**Garantía**: garantía estándar para el hardware

**Sitio web**: [https://stscollective.com](https://stscollective.com)

> 💰 **Descuento para lectores**: Usa el código **SIMEONONSECURITY** para obtener hasta un 20 % de descuento en productos de STS Collective. [Compra con el descuento aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Otras fuentes para comprar M5 Atom Lite

**Tienda oficial de M5Stack**:
- Sitio web: [shop.m5stack.com](https://shop.m5stack.com)
- Precio: $9.95 por un Atom Lite sin accesorios
- Accesorios: módulos de batería, sensores Grove y carcasas
- Envío: internacional, 7–14 días

**Amazon**: busca “M5Stack Atom Lite”
- Precio: aproximadamente $12–15, según el vendedor
- Envío Prime disponible
- Hay paquetes con accesorios

**Adafruit**: [adafruit.com](https://adafruit.com)
- Tienda de electrónica con selección curada
- Buenos recursos de aprendizaje
- Envío rápido dentro de Estados Unidos

**Nota**: *Si compras un M5 Atom Lite sin accesorios, debes instalar el firmware por separado siguiendo la guía DIY anterior. La versión preflasheada de STS Collective es otro producto.*

### Resumen comparativo de precios

| Dispositivo | Precio base | Complementos opcionales | Inversión total | Tiempo de configuración |
|--------|------------|-------------------------|-----------------|--------------------------|
| **DIY ESP32** | $5–12 | Carcasa 3D, batería | $5–20 | 15–30 min |
| **M5 Atom Lite** | $49.99 | Batería externa $10 | $50–60 | Listo para usar |
| **OUI-SPY** | $85 | Antena externa $20, carcasa | $85–115 | Listo para usar |

______

## Uso del detector: situaciones prácticas

{{< figure src="flockyou-detection-device-driving-scenario.webp" alt="Ilustración de un conductor que mira un detector FlockYou pequeño, colocado en el portavasos, mientras su LED avisa de una cámara Flock Safety cercana" >}}

### Situación 1: cartografiar el trayecto diario

**Objetivo**: Documentar las ubicaciones de las cámaras Flock en tus rutas habituales.

**Preparación**:
- Usa un dispositivo con GPS, como un ESP32 DIY con módulo GPS o un OUI-SPY con GPS.
- Activa el registro automático.
- Colócalo en el vehículo o llévalo en el bolsillo.
- Ajusta la sensibilidad a MEDIA para reducir los falsos positivos.

**Procedimiento**:
1. Enciende el detector antes de salir.
2. Conduce por tu ruta habitual.
3. El dispositivo avisa cuando detecta cámaras Flock.
4. Las coordenadas GPS se registran automáticamente.
5. Al volver a casa, exporta los datos.
6. Importa el GPX/CSV en un programa de cartografía.
7. Crea tu propio mapa de ubicaciones de cámaras.

**Ventajas**:
- Conocer la cobertura de vigilancia de tus rutas.
- Identificar rutas alternativas sin cámaras.
- Contribuir a proyectos de cartografía comunitaria.
- Registrar cambios en las instalaciones a lo largo del tiempo.

### Situación 2: evaluar la vigilancia del vecindario

**Objetivo**: Determinar la cobertura de cámaras Flock en tu zona residencial.

**Preparación**:
- Usa un dispositivo portátil (M5 Atom Lite, ESP32 DIY u OUI-SPY).
- Haz el recorrido a pie o en bicicleta.
- Realiza observaciones estacionarias en cruces importantes.

**Procedimiento**:
1. Recorre a pie o en bicicleta las calles del vecindario.
2. Detente en cada cruce durante 30 a 60 segundos.
3. Anota las detecciones en un mapa.
4. Usa la intensidad de señal para estimar la distancia y la dirección.
5. Confirma visualmente la ubicación de las cámaras cuando sea posible.
6. Documenta los resultados con fotos tomadas desde espacios públicos.

**Resultado**:
- Mapa completo de la infraestructura de vigilancia local.
- Evidencia para organizar a la comunidad.
- Datos para solicitudes de registros públicos.
- Información para tomar decisiones personales sobre privacidad.

*La velocidad al caminar importa más de lo que muchos creen. El firmware cambia de canal WiFi aproximadamente cada 250 ms para seguir el ritmo de los cambios de canal de la cámara. Si caminas o pedaleas rápido, puedes pasar por la ventana de detección antes de que coincida el salto de canal. Si las detecciones durante el recorrido son irregulares, camina más despacio en los cruces en vez de probar primero una antena de mayor ganancia. Una antena estándar y una pausa de 30 a 60 segundos en cada parada detectan muchas más cámaras que pasar a buen paso con una antena de alta ganancia.*

### Situación 3: evaluar la privacidad durante un viaje

**Objetivo**: Entender la exposición a la vigilancia durante un viaje.

**Preparación**:
- Lleva un dispositivo compacto (M5 Atom Lite en el bolsillo o ESP32 DIY).
- Activa el registro continuo.
- Revisa los datos después del viaje.

**Usos**:
- Citas médicas: evalúa la vigilancia cerca de clínicas.
- Consultas legales: comprueba la cobertura cerca de despachos de abogados.
- Servicios religiosos: entiende la vigilancia cerca de lugares de culto.
- Actividades políticas: evalúa la vigilancia en actos y protestas.
- Situaciones domésticas: identifica si una vivienda está vigilada.

### Situación 4: defensa comunitaria

**Objetivo**: Aportar datos a debates sobre políticas públicas y a iniciativas de sensibilización.

**Aplicaciones**:
- Presentar resultados en reuniones del ayuntamiento.
- Incluirlos en solicitudes de registros públicos.
- Compartirlos con organizaciones de defensa de la privacidad.
- Contribuir a proyectos de investigación.
- Informar a asociaciones vecinales.

**Presentación de datos**:
- Crear mapas de calor de la densidad de cámaras.
- Elaborar informes sobre diferencias de cobertura.
- Crear cronologías de expansión de las instalaciones.
- Comparar los datos con estadísticas delictivas, o con su ausencia.

______


## Cómo funciona realmente el código de detección

### Algoritmo de detección básico (simplificado)

Para quien tenga interés en la implementación técnica, esta es una versión simplificada de la lógica de detección:

```cpp
// Núcleo de detección Flock-You (conceptual, no es el código completo)

// Base de datos OUI (31 OUI asociados a Flock conocidos)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // Variante Espressif ESP32-S3
    // ... 28 OUI más ...
};

// Función de retorno del modo promiscuo
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;

    // Extraer la dirección MAC de la trama
    uint8_t *mac = pkt->payload + 10; // Posición del campo addr2

    // Comparar con la base de datos OUI
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // OUI coincidente encontrado
            int rssi = pkt->rx_ctrl.rssi;

            // Comprobar el umbral de intensidad de señal
            if (rssi > RSSI_THRESHOLD) {
                // Analizar la trama en busca de otras firmas
                if (is_wildcard_probe_request(pkt)) {
                    // Detección de alta confianza
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // Solo coincidencia OUI
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Detección de solicitudes de sondeo comodín
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Trama de gestión, subtipo solicitud de sondeo
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;

    // Comprobar si el elemento SSID está vacío (comodín)
    // La posición depende de la estructura de la trama
    uint8_t *ie = &pkt->payload[24]; // Inicio de los elementos de información
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Solicitud de sondeo comodín
    }
    return false;
}
```

### Conceptos técnicos clave

**Modo promiscuo**: En vez de recibir solo las tramas dirigidas al dispositivo, el ESP32 captura todas las tramas WiFi dentro del alcance. **Esto permite detectar dispositivos cercanos que no se comunican con el detector.**

**Estructura de la dirección MAC**: Cada trama WiFi contiene varias direcciones MAC:
- `addr1`: dirección del receptor
- `addr2`: dirección del transmisor (contiene la OUI)
- `addr3`: dirección del destino o la fuente final

**RSSI (indicador de intensidad de señal recibida)**: Intensidad de señal en dBm (decibelios negativos relativos a un milivatio). Valores habituales:
- -30 dBm: extremadamente intensa (muy cerca)
- -50 dBm: señal intensa
- -70 dBm: débil, pero utilizable
- -90 dBm: muy débil (límite del alcance)

**Solicitudes de sondeo**: Los dispositivos WiFi envían solicitudes de sondeo para encontrar redes disponibles. *Las solicitudes comodín (SSID vacío) buscan cualquier red. Son habituales en dispositivos IoT como las cámaras Flock, por lo que permiten detectarlas de forma fiable.*

______


## Solución de problemas frecuentes

{{< figure src="flockyou-troubleshooting-firmware-flash-flowchart.webp" alt="Diagrama de flujo para resolver problemas habituales al instalar el firmware FlockYou y detectar cámaras, desde fallos de alimentación hasta coincidencias OUI erróneas" >}}

### Problema: no hay detecciones pese a que se sabe que hay una cámara cerca

**Posibles causas**:
1. **Cámara desconectada o apagada**: las cámaras Flock pueden estar inactivas temporalmente.
2. **Señal bloqueada**: materiales de construcción como el metal y el hormigón absorben WiFi.
3. **Fuera de alcance**: el alcance efectivo es de unos 100 a 300 pies, según los obstáculos.
4. **Movimiento demasiado rápido**: el cambio de canal favorece caminar despacio o detenerse frente a caminar deprisa o ir en vehículo.
5. **Problema de firmware**: una versión antigua puede no reconocer variantes OUI nuevas.

**Soluciones**:
- Confirma que la cámara sea visible y parezca estar operativa (paneles solares, luces).
- Acércate a la ubicación sospechosa o detente entre 30 y 60 segundos en lugar de pasar caminando.
- Prueba distintas orientaciones de la antena.
- Actualiza al firmware Flock-You más reciente.
- **Comprueba que el dispositivo esté escaneando** y verifica la actividad del LED o la pantalla.

### Problema: demasiados falsos positivos

**Posibles causas**:
1. **Alta densidad de dispositivos ESP32**: los dispositivos inteligentes e IoT son habituales.
2. **Sensibilidad demasiado alta**: se detectan dispositivos lejanos o irrelevantes.
3. **Otras cámaras de vigilancia**: muchas usan módulos ESP32.

**Soluciones**:
- Reduce la sensibilidad.
- Activa la detección de solicitudes de sondeo comodín para obtener mayor confianza.
- Confirma físicamente las detecciones antes de registrarlas.
- Filtra por intensidad de señal y avisa solo de señales fuertes.
- Actualiza la base de datos OUI para centrarse en las OUI confirmadas de Flock.

### Problema: la batería se agota rápido

**Posibles causas**:
1. **Escaneo continuo**: no hay suspensión ni gestión de energía.
2. **Pantalla siempre encendida**: consume mucha energía.
3. **GPS activo**: los módulos GPS consumen bastante.
4. **Batería antigua**: las baterías Li-Po se degradan con el tiempo.

**Soluciones**:
- Activa el escaneo pasivo, con pausas, en vez del escaneo continuo.
- Configura el apagado automático de la pantalla.
- Desactiva el GPS cuando no necesites cartografiar.
- Cambia la batería (OUI-SPY y mesh-detect v2 tienen baterías reemplazables).
- Usa una batería externa para sesiones largas.

### Problema: el GPS no obtiene posición

**Posibles causas**:
1. **Uso en interiores**: el GPS necesita visibilidad del cielo.
2. **Antena desconectada**: mesh-detect v2 necesita una antena externa conectada.
3. **Inicio en frío**: la primera posición GPS tarda entre 5 y 15 minutos.
4. **Interferencias**: los dispositivos electrónicos cercanos afectan a la señal.

**Soluciones**:
- Ve a un lugar con vista despejada del cielo.
- Comprueba que la antena esté conectada al conector SMA.
- Espera a la primera posición; las siguientes llegan más rápido.
- Aléjate de las fuentes de interferencias de radiofrecuencia.
- Comprueba que el GPS esté activado en la configuración.

### Problema: no se guardan datos en la tarjeta SD

**Posibles causas**:
1. **Tarjeta SD sin formato**: para garantizar la compatibilidad, debe usar FAT32.
2. **Tarjeta SD llena**: no queda espacio disponible.
3. **Tarjeta no detectada**: no está insertada por completo.
4. **Sistema de archivos dañado**: la tarjeta está deteriorada.

**Soluciones**:
- **Formatea la tarjeta SD como FAT32** (máximo 32 GB por compatibilidad).
- Borra registros antiguos o usa una tarjeta de mayor capacidad.
- Vuelve a insertar la tarjeta hasta que encaje.
- Reformatea la tarjeta o sustitúyela si está dañada.
- Comprueba que el dispositivo la reconoce; el menú muestra el estado de la SD.

______

## Consideraciones legales y éticas

### Estado legal de los dispositivos de detección

**Legalidad del escaneo Wi-Fi**:
- ✅ **Legal en Estados Unidos**: la monitorización Wi-Fi pasiva, en modo de solo recepción, es legal
- ✅ **No intercepta comunicaciones**: los dispositivos solo observan tramas difundidas públicamente
- ✅ **No descifra datos**: no intentan descifrar datos ni conectarse a redes
- ✅ **Similar a un escáner de radio**: su situación legal se parece a la de los escáneres de radio policial

**Distinciones importantes**:
- ❌ **Ilegal**: interferir activamente con el funcionamiento de una cámara
- ❌ **Ilegal**: intentar piratear o acceder a sistemas de cámaras
- ❌ **Ilegal**: destruir o manipular cámaras físicas
- ⚠️ **Zona gris**: *Algunas jurisdicciones tienen leyes de privacidad más estrictas. Comprueba la normativa local antes de usar el dispositivo.*

**Recomendación**: **Los dispositivos de detección sirven para informar. No interfieras con el funcionamiento de las cámaras.**

### Pautas de uso ético

**Uso responsable**:
- ✅ Usa el dispositivo para conocer la vigilancia de tu entorno
- ✅ Documenta observaciones para actividades de defensa y debates sobre políticas
- ✅ Comparte datos agregados con organizaciones de privacidad
- ✅ Colabora en proyectos comunitarios de cartografía
- ✅ Informa a otras personas sobre la infraestructura de vigilancia

**Evita**:
- ❌ Usar los datos para facilitar actividades ilegales
- ❌ Acosar a propietarios por instalar cámaras
- ❌ Entrar en propiedades para confirmar ubicaciones de cámaras
- ❌ Tomar medidas por cuenta propia contra la infraestructura de vigilancia

### Consideraciones de privacidad

**Privacidad de tus datos**:
- **Los dispositivos registran TU ubicación** mediante GPS
- Guarda esos datos de forma segura
- **Ten en cuenta el riesgo de una citación judicial** si participas en un proceso legal
- Considera cifrar archivos de registro sensibles
- Consulta las políticas de privacidad de proveedores de dispositivos conectados a la nube

**Respeta a otras personas**:
- Ten cuidado al usar el dispositivo en espacios privados
- No lo uses para rastrear a otras personas
- Considera las consecuencias éticas de compartir datos

______

## Comunidad y desarrollo de código abierto

### Contribuir al proyecto Flock-You

El proyecto Flock-You se nutre de las contribuciones de la comunidad:

**Repositorio de GitHub**: [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**Formas de contribuir**:
1. **Nuevas OUI**: envía OUI de cámaras Flock identificadas recientemente.
2. **Mejoras del código**: envía solicitudes de incorporación de cambios para mejorar el firmware.
3. **Diseño de hardware**: comparte diseños propios de dispositivos de detección.
4. **Documentación**: mejora las guías de configuración y las traducciones.
5. **Pruebas**: informa de errores y comprueba las funciones en distintos dispositivos.
6. **Cartografía**: contribuye a bases de datos comunitarias de ubicaciones de cámaras.

### Recursos de la comunidad

**Foros y conversaciones**:
- **Reddit**: r/privacy, r/privacytoolsIO y debates activos.
- **Discord**: servidor de Colonel Panic Tech, con chat en tiempo real.
- **GitHub Issues**: asistencia técnica y solicitudes de funciones.

**Publicaciones de investigación**:
- Estudios académicos sobre vigilancia ALPR.
- Evaluaciones del impacto en la privacidad.
- Análisis jurídicos sobre la legalidad de los dispositivos de detección.

**Organizaciones de defensa**:
- **Electronic Frontier Foundation** (EFF): seguimiento mediante ALPR.
- **ACLU**: vigilancia y derechos de privacidad.
- **Grupos locales**: DeFlockJoplin y otras iniciativas comunitarias.

### Hoja de ruta de desarrollo

**Funciones previstas** (según el GitHub del proyecto):
- **Aprendizaje automático**: reconocimiento de patrones para mejorar la precisión.
- **Sincronización en la nube**: base de datos opcional de detecciones aportadas por la comunidad.
- **Aplicaciones móviles**: integración con teléfonos inteligentes para mejorar la interfaz.
- **Modos de detección adicionales**: otras tecnologías de vigilancia.
- **Alertas en tiempo real**: notificaciones push por red móvil o WiFi.

______

## Conclusión: proteger la privacidad con hardware de código abierto

El **proyecto de detección Flock-You** pone el hardware de contravigilancia al alcance de cualquier presupuesto. Puedes elegir el **montaje DIY con ESP32 ($5–12)**, el **M5 Atom Lite listo para usar ($49.99)** o el **OUI-SPY multimodo ($85)**. Cada opción convierte la detección de cámaras Flock en un dispositivo que puedes montar en una tarde.

*Ten presente qué detecta este hardware y qué queda fuera: detecta cámaras Flock por Wi-Fi. No detecta Stingrays ni rastreadores personales que te acompañen. Combínalo con Rayhunter y Eye Spy, enlazados abajo, si necesitas ampliar la cobertura.*

### Puntos clave

- **Código abierto y libre para modificar**: el desarrollo comunitario mantiene actualizados la lista OUI y el firmware
- **Hardware asequible**: un ESP32 básico cuesta $5–12. Cada nivel superior añade comodidad, no nuevas capacidades de detección
- **Solo monitorización pasiva**: el dispositivo recibe tramas Wi-Fi difundidas públicamente y no transmite nada
- **Actualizaciones periódicas**: las nuevas firmas OUI y la investigación sobre solicitudes wildcard se incorporan al firmware cuando cambia el hardware de Flock
- **Verificado sobre el terreno**: la comunidad DeFlockJoplin detectó 11 de 12 cámaras conocidas en una prueba real en coche

### Próximos pasos

1. **Lee los antecedentes**: [Cámaras de Flock Safety: alcance y problemas de privacidad](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Elige una plataforma**: ajusta el montaje DIY, M5 Atom Lite u OUI-SPY a tu presupuesto y experiencia
3. **Compra el hardware**: elige un proveedor autorizado de la lista anterior
4. **Instala y configura el firmware**: sigue la guía de la plataforma elegida
5. **Únete a la comunidad**: comparte tus observaciones y aporta detecciones al proyecto
6. **Cubre lo que este dispositivo no detecta**: usa [Rayhunter para detectar captadores IMSI](/articles/how-to-flash-rayhunter-devices-complete-guide/) para detectar captadores IMSI y [Eye Spy para detectar AirTags y otros rastreadores](/articles/eye-spy-passive-surveillance-detector-esp32-2026/) para AirTags y otros rastreadores

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra dispositivos FlockYou listos para usar y ahorra un 20 %
{{< /centerbutton >}}

La vigilancia ALPR sigue expandiéndose. Saber dónde están las cámaras te ayuda a planificar un trayecto, documentar un vecindario o oponerte a una instalación local.

______

## Artículos relacionados

| Artículo | Descripción |
|---------|-------------|
| **[Vigilancia con cámaras Flock Safety: alcance, problemas de privacidad y estrategias de protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Guía completa de la red ALPR de Flock Safety, los abusos documentados, los recursos para organizar a la comunidad y las medidas que puedes tomar para protegerte |
| **[Flock Finder: localiza las cámaras Flock Safety sospechosas cerca de ti](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Cómo usar la herramienta de código abierto Flock Finder para visualizar más de 40.000 cámaras Flock sospechosas en todo el mundo con datos WiGLE y huellas OUI |
| **[Eye Spy: detector pasivo de vigilancia y rastreadores con ESP32](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** | Detector BLE y WiFi que cubre lo que Flock-You no detecta: AirTags, rastreadores Tile, cámaras corporales y drones de la misma familia de hardware |
| **[Cómo flashear Rayhunter en dispositivos de detección de captadores IMSI](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Guía paso a paso para instalar el firmware Rayhunter y detectar captadores IMSI y stingrays en un punto de acceso móvil reutilizado, en vez de un ESP32 |
| **[Firmware personalizado DagShell para el Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Guía completa para instalar DagShell en el Orbic RCL400 y habilitar la supervisión avanzada de redes móviles y la detección de captadores IMSI |
| **[Comparativa de dispositivos Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparación de los dispositivos compatibles con Rayhunter para elegir el hardware adecuado para tu conjunto de herramientas contra la vigilancia |

*¿Buscas algo que combata activamente los rastreadores, en vez de limitarse a detectarlos? [Simulacra](https://github.com/Em3ritus/simulacra) es un proyecto de código abierto independiente y sin afiliación que llena la zona de dispositivos BLE y WiFi señuelo para ocultar la señal de tu dispositivo real. Resuelve un problema distinto al de los dispositivos de esta guía y puede interesarte si la detección pasiva no basta para tu modelo de amenazas.*

______

## Referencias

1. [Repositorio de GitHub de Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - mapa interactivo de cámaras ALPR](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - repositorio de GitHub](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - sitio oficial del proveedor](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite con firmware preinstalado](https://stscollective.com)
6. [Documentación oficial de M5Stack Atom Lite](https://docs.m5stack.com/en/core/ATOM%20Lite)
7. [Documentación de la API WiFi ESP32 de Espressif](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html)
8. [Referencia de solicitudes y respuestas Probe 802.11](https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/)
9. [DeFlock Joplin - investigación comunitaria sobre ALPR](https://deflockjoplin.today)
10. [DeFlock - mapa y datos ALPR colaborativos](https://deflock.me/)
11. [Electronic Frontier Foundation - ¿qué es ALPR?](https://www.eff.org/pages/what-alpr)
12. [Descarga oficial de Arduino IDE](https://www.arduino.cc/en/software)
13. [Documentación de Platform.io](https://docs.platformio.org/)
14. [IEEE Registration Authority - bloque grande de direcciones MAC (OUI)](https://standards.ieee.org/products-programs/regauth/oui/)
15. [Referencia de la estructura de tramas Beacon 802.11](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
