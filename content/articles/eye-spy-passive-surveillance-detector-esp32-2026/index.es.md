---
title: "Eye Spy: Detector pasivo de vigilancia para el M5Stack Atom Lite (ESP32)"
date: 2026-06-07
toc: true
draft: false
description: "Una referencia técnica completa para Eye Spy v1.1 - un detector de vigilancia pasivo BLE y WiFi de código abierto que funciona en el M5Stack Atom Lite (ESP32-PICO-D4) y busca cámaras corporales, sistemas ALPR, AirTags, drones y cámaras ocultas usando un modelo de amenazas con puntuación de confianza y un único LED RGB."
genre: ["Herramientas de privacidad", "Contra-vigilancia", "Seguridad IoT", "Sistemas embebidos", "Investigación de seguridad", "Seguridad WiFi", "Seguridad Bluetooth", "Proyectos ESP32", "Seguridad de hardware", "Seguridad de código abierto"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Detección de vigilancia", "Contra-vigilancia", "Detección BLE", "Escaneo WiFi", "Detección AirTag", "Detección ALPR", "Flock Safety", "Detección cámara corporal", "Detección drones", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Código abierto", "Privacidad", "BLE pasivo", "Modo promiscuo", "Detección OUI", "Detección rastreador", "Axon Body Camera", "Ray-Ban Meta", "Samsung SmartTag", "Tile Tracker", "Cámara oculta", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Una ilustración de un pequeño dispositivo M5Stack Atom Lite con ondas coloridas de señales a su alrededor, sobre un fondo azul marino profundo, que representa la detección de vigilancia Bluetooth y WiFi."
coverCaption: ""
---

**Un sensor pasivo del tamaño de un pulgar que le dice cuando algo lo está observando**

## Introducción: El panorama de vigilancia que no puede ver

El mundo físico está cada vez más instrumentado con dispositivos que observan, graban y rastrean. Lectores de matrículas en las esquinas de las calles, cámaras corporales en las fuerzas del orden, cámaras en propiedades de alquiler, rastreadores comerciales tipo AirTag ocultos en bolsas o autos, y cámaras de vigilancia comerciales en cada entrada de comercio. La mayoría de estos dispositivos se comunican de forma inalámbrica mediante **Bluetooth LE** o **WiFi**, y *la mayoría de esas comunicaciones se transmiten al aire libre para que cualquiera con el receptor adecuado pueda detectarlas*.

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) es una herramienta de detección de vigilancia pasiva que aprovecha exactamente este hecho. Ejecutándose en el **M5Stack Atom Lite**, una placa de desarrollo ESP32-PICO-D4 aproximadamente del tamaño de un terrón de azúcar, Eye Spy monitorea continuamente los espectros BLE y WiFi en busca de las firmas electrónicas de dispositivos de grabación, cámaras de vigilancia, sistemas **ALPR** (lectores automáticos de matrículas), drones y rastreadores personales. Cuando encuentra algo, su LED RGB cambia de color.

*No se conecta a nada. No transmite.* Observa, puntúa y se ilumina.

Este artículo es una referencia técnica completa: qué detecta Eye Spy, cómo funciona el sistema de puntuación de confianza, la ingeniería detrás de cada motor de detección, cómo construirlo y flashearlo, y cuáles son sus limitaciones prácticas.

---

## Indicadores LED: La interfaz de usuario completa

Como el [ESP32 WiFi Canary](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), la salida completa de Eye Spy es un único SK6812 RGB NeoPixel en GPIO 27 del M5Stack Atom Lite. El LED comunica en todo momento un nivel de amenaza de cuatro estados:

| Color | Significado | Rango de puntuación |
|-------|-------------|---------------------|
| 🔵 Pulso azul | Inicio / primer escaneo | -- |
| 🟢 Verde sólido | Despejado - nada detectado | 0–2 |
| 🟡 Amarillo sólido | Precaución - posible dispositivo de grabación cercano | 3–5 |
| 🔴 Rojo parpadeante | Alerta - dispositivo de vigilancia/rastreo definitivo detectado | 6+ |

**Una sola detección de alta confianza (cámara corporal Axon, cámara Flock Safety, coincidencia OUI ALPR, AirTag) acumula suficientes puntos para empujar inmediatamente el LED al rojo en un solo ciclo de detección.**

---

## Hardware

### Objetivo principal: M5Stack Atom Lite

| Componente | Detalle |
|-----------|---------|
| Placa | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | SK6812 NeoPixel en GPIO 27 |
| Botón | GPIO 39 (solo entrada) |
| Flash | 4 MB |

El Atom Lite es una plataforma completa autónoma. **Sin soldadura, sin breadboard, sin componentes externos.** Conéctelo al USB y funciona.

---

## El sistema de puntuación

Eye Spy usa un **modelo de puntuación de confianza** que agrega señales de todos los motores de detección en un único entero. La puntuación controla el estado del LED (verde / amarillo / rojo) y está sujeta a dos mecanismos de gestión automática:

### Decaimiento de puntuación

La puntuación cae **−1 punto cada 60 segundos** sin nuevas detecciones. Si se aleja de un dispositivo detectado, el LED vuelve al verde en pocos minutos sin intervención del usuario.

### Tiempo de recarga

Cada *tipo* de detección tiene un **tiempo de espera de 120 segundos** antes de poder agregar puntos nuevamente desde la misma fuente. *Esto evita que un solo dispositivo persistente acumule la puntuación indefinidamente.*

---

## Motores de detección

Eye Spy opera tres fases de escaneo distintas en rotación continua:

**BLE pasivo (9 s) → Escaneo WiFi (~3 s) → Sniff promiscuo (5 s) → repetición**

---

### Motor 1: BLE - Escaneo pasivo

El escaneo BLE se implementa con **NimBLE sin solicitudes de escaneo transmitidas**. El dispositivo escucha paquetes de publicidad BLE sin enviar ninguna respuesta. *Esto hace que Eye Spy sea electrónicamente invisible para el equipo que está escaneando.*

#### Tabla de detección BLE

| # | Objetivo | Método de detección | Puntuación |
|---|----------|--------------------|----|
| 1 | **Cámara corporal Axon** | OUI MAC BLE `00:25:df` | +5 🔴 |
| 2 | **Ray-Ban Meta Smart Glasses** | UUID de servicio BLE `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE** | Nombre del dispositivo BLE que contiene `Flock`, `Penguin`, `Pigvision` o `FS Ext Battery` | +5 🔴 |
| 4 | **Skimmer de tarjetas (HC-03/05/06)** | Coincidencia exacta del nombre del dispositivo BLE | +5 🔴 |
| 5 | **Apple AirTag** | Datos del fabricante `0x004C` subtipo `0x12`/`0x1E` | +4 🔴 |
| 6 | **Drone (OpenDroneID BLE)** | UUID de servicio BLE `0xFFFA` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID de servicio BLE `0xFD5A` | +3 🟡 |
| 8 | **Tile tracker** | UUID de servicio BLE `0xFEED` o `0xFEEC` | +3 🟡 |
| 9 | **Nodo MeshCore** | Prefijo del nombre del dispositivo BLE `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (seguimiento en comercio/lugar)** | Datos del fabricante `0x004C 0x02 0x15` | +2 🟡 |
| 11 | **Dispositivo persistente desconocido** | Cualquier MAC BLE no clasificada vista ≥3× durante ≥5 minutos | +2 🟡 |

---

### Motor 2: Escaneo WiFi - Escaneo activo de canales

El motor de escaneo WiFi usa la interfaz estándar de escaneo AP del ESP32 para enumerar los puntos de acceso cercanos y comparar sus BSSID y SSID con las huellas de dispositivos de vigilancia conocidos.

#### Tabla de detección del escaneo WiFi

| # | Objetivo | Método de detección | Puntuación |
|---|----------|--------------------|----|
| 12 | **Cámara Flock Safety (OUI)** | BSSID coincide con la tabla OUI de Flock Safety de 22 entradas | +5 🔴 |
| 13 | **Cámara ALPR / LPR (OUI)** | BSSID coincide con Motorola Solutions / Vigilant Solutions OUI `00:0e:58` | +5 🔴 |
| 14 | **SSID palabra clave Flock** | SSID contiene: `flock`, `flocksafety`, `fs ext`, `penguin`, `pigvision` | +5 🔴 |
| 15 | **SSID palabra clave ALPR** | SSID contiene: `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola`, `automate` | +4 🔴 |
| 16 | **Proveedor de cámara de vigilancia (OUI)** | BSSID coincide con tabla OUI de cámaras de 31 entradas - Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix, Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID palabra clave cámara** | SSID contiene: `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect`, `genetec` y más | +2 🟡 |

---

### Motor 3: WiFi Promiscuo - Captura pasiva de tramas

El motor promiscuo pone el radio ESP32 en **modo monitor** y captura tramas de gestión 802.11 sin procesar. Esto permite la detección de dispositivos que no publicitan un SSID, específicamente drones que usan el protocolo **Remote ID** sobre **WiFi Neighbor Awareness Networking (NaN)**.

#### Tabla de detección en modo promiscuo

| # | Objetivo | Método de detección | Puntuación |
|---|----------|--------------------|----|
| 18 | **Drone (OpenDroneID WiFi NaN)** | Trama de gestión 802.11 hacia el destino `51:6f:9a:01:00:00` | +4 🔴 |

---

## Construcción y flasheo

### Requisitos

- **PlatformIO** (CLI o extensión de VS Code)
- **M5Stack Atom Lite** o cualquier ESP32 DevKit
- Cable USB-C

### Flashear en M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Construir y flashear para Atom Lite
pio run -e atom-lite -t upload

# Monitor serie a 115200 baudios
pio device monitor -b 115200
```

### Flashear en ESP32 DevKit genérico

```bash
pio run -e esp32dev -t upload
```

---

## Notas de detección y limitaciones prácticas

### Lo que Eye Spy no puede hacer

**WiFi de 5 GHz**: El ESP32 es un dispositivo **solo de 2,4 GHz**. Cualquier cámara de vigilancia, sistema ALPR o punto de acceso que opere exclusivamente en bandas de 5 GHz no será visible.

**BLE cifrado**: Varios productos de vigilancia de alta gama cifran u ocultan sus publicidades BLE.

**Cámaras cableadas**: **Las cámaras IP conectadas mediante Ethernet sin radio WiFi no producen emisiones inalámbricas que Eye Spy pueda detectar.**

**Limitaciones de alcance**: La antena ESP32 tiene un alcance de recepción interior práctico de **20 a 40 metros** para señales fuertes.

### Falsos positivos a esperar

**Cámaras de consumidores en casas de vecinos**: Las cámaras Ring, Nest, Wyze, Arlo y Reolink son omnipresentes en los barrios residenciales. Espere algunos resultados amarillos (+3) de las cámaras de timbre de los vecinos.

**Despliegues de iBeacon en comercios**: Los grandes minoristas despliegan infraestructura iBeacon en prácticamente cada tienda. Cualquier visita a un centro comercial probablemente activará la detección iBeacon (+2).

---

## Casos de uso

### Conciencia de contra-vigilancia

El público principal de Eye Spy es cualquier persona que quiera conciencia ambiental de la infraestructura de vigilancia en su entorno inmediato.

### Detección de acoso con AirTag

El acoso mediante AirTag es un problema documentado. El **motor de detección de seguidor** de Eye Spy (MAC BLE persistente desconocida vista ≥3× durante ≥5 minutos) apunta específicamente a rastreadores modificados o personalizados.

### Inspección de alquiler / habitación de hotel

Entrar en una nueva habitación de hotel o propiedad de alquiler con Eye Spy funcionando proporciona una primera indicación de dispositivos BLE y WiFi inesperados.

### Seguridad en viajes

Como el WiFi Canary, Eye Spy está diseñado para el factor de forma de viaje. El Atom Lite cabe en cualquier bolsillo.

---

## Conclusión

Eye Spy aborda un problema estrecho pero significativo: el entorno de vigilancia física a su alrededor está cada vez más instrumentado, y la mayor parte de esa instrumentación transmite firmas RF detectables. **Un M5Stack Atom Lite de 15 dólares ejecutando el firmware Eye Spy se convierte en un escáner ambiental continuo** que transforma la complejidad del análisis de paquetes BLE y las búsquedas OUI WiFi en un único LED RGB.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)
