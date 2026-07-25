---
title: "Proyecto Flock-You: Guía completa de hardware de contravigilancia y configuración 2026"
date: 2026-05-24
lastmod: 2026-05-24
toc: true
draft: false
description: "Guía técnica completa del proyecto de código abierto Flock-You para detectar cámaras ALPR de Flock Safety usando hardware basado en ESP32. Incluye instrucciones de configuración, detalles de firmware y opciones de compra."
genre: ["Hardware de seguridad", "Contravigilancia", "Tecnología de privacidad", "Proyectos de código abierto", "Desarrollo ESP32", "Monitoreo WiFi", "Herramientas de privacidad", "Derechos digitales", "Modificación de hardware", "Seguridad de red"]
tags: ["Proyecto Flock-You", "Detección ALPR", "ESP32-S3", "Detección WiFi OUI", "Hardware de contravigilancia", "Detección Flock Safety", "Seguridad open source", "Hardware de privacidad", "M5 Atom Lite", "OUI-SPY", "Modo promiscuo WiFi", "Monitoreo 802.11", "Colonel Panic Tech", "STS Collective", "Dispositivos de privacidad", "Detección de vigilancia", "Escaneo WiFi", "Proyecto GitHub"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Una ilustración que muestra un dispositivo basado en ESP32 en primer plano, escaneando señales WiFi. Ondas coloridas representan diferentes intensidades de señal sobre un fondo oscuro."
coverCaption: "Soluciones de hardware de código abierto para detectar cámaras de vigilancia ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Guía técnica completa para construir y usar dispositivos de detección Flock-You**

## Introducción: Contravigilancia de código abierto

El **proyecto Flock-You** es una **iniciativa comunitaria de código abierto** para detectar y mapear la infraestructura de vigilancia ALPR de Flock Safety. Alojado en GitHub en **colonelpanichacks/flock-you**, este proyecto utiliza hardware ESP32 asequible para identificar cámaras Flock a través de sus **firmas de red WiFi**.

Esta guía completa cubre todo, desde la **metodología técnica** detrás de la detección de Flock hasta las **instrucciones de configuración paso a paso** para tres plataformas de hardware, la **instalación de firmware** y la **información de compra de proveedores autorizados**. Ya sea un defensor de la privacidad, investigador de seguridad o ciudadano preocupado, esta guía le permitirá construir o comprar su propio dispositivo de detección.

Para el contexto sobre por qué esta tecnología importa, lea nuestro artículo complementario: **[Vigilancia con cámaras Flock Safety: Prevalencia, preocupaciones de privacidad y estrategias de protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

¿Quiere ver dónde ya se han mapeado las cámaras Flock? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** es una herramienta de código abierto que traza 40.000+ cámaras Flock Safety sospechosas en todo el mundo usando datos WiFi WiGLE y huellas digitales OUI, actualizado diariamente. Fuente en **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

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

#### 2. Detección de solicitudes de sonda comodín

Las cámaras Flock envían periódicamente **solicitudes de sonda comodín** buscando redes disponibles. Estas tienen características distintivas:

- **Frame de gestión 802.11**: Tipo=0, Subtipo=4
- **Elemento de información SSID**: Longitud=0 (vacío/comodín)

#### 3. Monitoreo WiFi en modo promiscuo

El modo promiscuo captura todos los frames WiFi en el rango, y los microcontroladores ESP32 lo soportan a través de la **esp_wifi API**.

#### 4. Análisis de intensidad de señal

Los dispositivos de detección miden el **RSSI** para estimar la distancia a las cámaras detectadas, filtrar falsos positivos y crear mapas de calor de densidad.

______

## Comparación de plataformas de hardware

### Tabla de descripción general de plataformas

| Función | DIY ESP32 | M5 Atom Lite (preflashado) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Fabricante** | DIY / Varios proveedores | STS Collective | Colonel Panic Tech |
| **Precio** | $5-12 | $39,99 | $85 |
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
| **Dificultad de configuración** | Medio-Avanzado | Plug-and-play | Plug-and-play |

### Análisis detallado de plataformas

#### 1. Construcción DIY ESP32 ($5-12)

**Descripción general**: Opción más asequible usando placas de desarrollo ESP32 estándar con firmware de código abierto.

**Firmware**: Fork de código abierto en **simeononsecurity/flock-you-esp32**:
- Modificado para hardware ESP32 estándar (GPIO 25, 2, 17)
- Melodía de inicio de Super Mario Bros. (confirma el funcionamiento del zumbador)
- Dos pitidos ascendentes rápidos en nueva detección
- Pitidos de heartbeat cada 10 segundos durante el seguimiento activo
- Soporte de panel Flask para wardriving GPS
- Exportación a formatos JSON, CSV, KML

**Ventajas**:
- ✅ Opción más barata (85-95% de ahorro vs OUI-SPY)
- ✅ Completamente de código abierto y modificable
- ✅ Usa placas ESP32 ampliamente disponibles
- ✅ Educativo, enseña sistemas embebidos
- ✅ **Misma precisión de detección que dispositivos premium**

**Desventajas**:
- ❌ Requiere ensamblaje DIY
- ❌ Se necesita flasheo manual del firmware
- ❌ Sin batería integrada

**Mejor para**: Makers, estudiantes, defensores de la privacidad con presupuesto limitado.

---

#### 2. M5 Atom Lite preflashado por STS Collective ($39,99)

**Descripción general**: Dispositivo de detección compacto preflashado, listo para usar.

**Firmware**: Port FlockYou personalizado por STS Collective (propietario):
- Precargado y listo para usar
- Alerta LED azul en detección de cámara Flock
- Sin configuración ni flasheo requerido

**Ventajas**:
- ✅ Preflashado, sin configuración técnica requerida
- ✅ Solución lista para usar asequible
- ✅ Extremadamente compacto y portátil
- ✅ LED azul simple = detección

**Desventajas**:
- ❌ Sin batería integrada (necesita alimentación USB)
- ❌ Pantalla limitada (solo LED RGB)
- ❌ *El firmware es propietario*

**Compra**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Descuento exclusivo**: Ahorre hasta 20% en productos STS Collective - use el código **SIMEONONSECURITY** al pagar o [haga clic aquí para comprar con el descuento aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### 3. OUI-SPY de Colonel Panic Tech ($85)

**Descripción general**: Placa de detección de vigilancia multi-modo con cuatro modos de firmware diferentes seleccionables a través del menú WiFi.

**Especificaciones de hardware**:
- **Microcontrolador**: ESP32-S3 dual-core Xtensa LX7, 8 MB de flash
- **Antena**: **Conmutable**, cerámica 2,4 GHz integrada O externa mediante conector MMCX
- **Función única**: Aleatorización de MAC en cada inicio

**Firmware**: OUI-SPY Unified Blue con **4 modos seleccionables**:
1. **Modo Detector**: Escáner BLE multi-objetivo con filtrado OUI + portal de configuración web
2. **Modo Foxhunter**: Rastreador de proximidad RSSI de objetivo único para radiogonometría
3. **Modo Flock-You**: Detección de cámaras Flock Safety y Raven con wardriving GPS, exportación JSON/CSV/KML
4. **Modo Sky Spy**: Detector RemoteID de drones (OpenDroneID / ASTM F3411) con seguimiento multi-dron

**Ventajas**:
- ✅ Cuatro modos de firmware en un solo dispositivo
- ✅ Antena conmutable (integrada o externa MMCX)
- ✅ Zumbador integrado con melodías de inicio personalizadas
- ✅ Multipropósito: ALPR, drones, BLE, radiogonometría
- ✅ Del creador original del proyecto Flock-You

**Desventajas**:
- ❌ Precio más alto para detección Flock únicamente
- ❌ Sin carcasa (PCB desnuda)
- ❌ Sin batería integrada

**Compra**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)

______

## Instrucciones de configuración paso a paso

### Guía de configuración 1: Construcción DIY ESP32

```bash
# Instalar PlatformIO
pip install platformio

# Clonar repositorio
git clone https://github.com/simeononsecurity/flock-you-esp32.git
cd flock-you-esp32

# Flashear firmware
pio run -t upload
pio device monitor
```

**Ensamblaje de hardware** (si usa zumbador):
- Zumbador positivo → GPIO 25
- Zumbador negativo → GND
- Indicador LED → GPIO 2 (integrado)

### Guía de configuración 2: M5 Atom Lite Preflashado

**Inicio rápido**:
1. Conectar a fuente de alimentación USB-C
2. El dispositivo arranca automáticamente
3. La matriz LED RGB se inicializa
4. **Detección**: LED se vuelve **AZUL** cuando se detecta una cámara Flock

### Guía de configuración 3: Placa multi-modo OUI-SPY

**Configuración inicial**:
1. Conectar alimentación USB-C
2. El dispositivo transmite red WiFi: `OUISPY-[ID]`
3. Conectarse a esa red y abrir `http://192.168.4.1`
4. Seleccionar el modo Flock-You en la interfaz web
5. El dispositivo reinicia y comienza a escanear

______

## Guía de compra e información de proveedores

### Proveedores autorizados

**Colonel Panic Tech** (colonelpanic.tech):
- OUI-SPY ($85), kits DIY ($55), módulo GPS ($18)
- Envío USA: 3-5 días hábiles
- Garantía de hardware de 90 días, actualizaciones de firmware de por vida

**STS Collective** (stscollective.com):
- M5 Atom Lite preflashado ($39,99)
- Envío USA: 2-4 días hábiles

> 💰 **Descuento para lectores**: Use el código **SIMEONONSECURITY** para hasta 20% de descuento - [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Consideraciones legales y éticas

### Estado legal de los dispositivos de detección

- ✅ **Legal en EE. UU.**: El monitoreo WiFi pasivo (solo recepción) es legal
- ✅ **Sin interceptación**: Los dispositivos solo monitorean frames transmitidos públicamente
- ✅ **Sin descifrado**: No intenta descifrar datos ni conectarse a redes
- ❌ **Ilegal**: Interferencia activa con el funcionamiento de la cámara
- ⚠️ **Área gris**: *Algunas jurisdicciones tienen leyes de privacidad más estrictas. Verificar regulaciones locales antes de usar.*

______

## Conclusión: Proteger la privacidad a través de la tecnología

El **proyecto de detección Flock-You** representa una democratización poderosa de la tecnología de contravigilancia. Por menos del costo de una suscripción mensual de streaming, los individuos obtienen conciencia de la infraestructura de vigilancia que los rodea. Ya elija la **construcción DIY ESP32 ($5-12)**, el **M5 Atom Lite listo para usar ($40)** o el **OUI-SPY multi-modo ($85)**, está invirtiendo en conciencia de privacidad y autonomía digital.

______

## Referencias

1. [Repositorio GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - Mapa interactivo de cámaras ALPR](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - Repositorio GitHub](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - Proveedor oficial](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite Preflashado](https://stscollective.com)
6. [Documentación oficial M5Stack](https://docs.m5stack.com/en/core/atom_lite)
7. [Documentación técnica Espressif ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
8. [DeFlockJoplin Community Research](https://deflockjoplin.org/)
9. [Electronic Frontier Foundation - ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [Documentación Platform.io](https://docs.platformio.org/)
