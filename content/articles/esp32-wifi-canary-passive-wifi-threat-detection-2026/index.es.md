---
title: "ESP32 WiFi Canary: Detección pasiva de amenazas en 2,4 GHz con alertas LED RGB"
date: 2026-06-06
toc: true
draft: false
description: "Un análisis detallado del proyecto ESP32 WiFi Canary - un sensor de concienciación 2,4 GHz compacto y pasivo para el M5Stack Atom Lite que vigila silenciosamente los AP Evil Twin, los ataques de desautenticación, las degradaciones de seguridad y las inundaciones de beacon con un modelo de amenazas de puntuación de confianza y un único LED RGB."
genre: ["Seguridad de red", "Seguridad WiFi", "Seguridad IoT", "Investigación de seguridad", "Sistemas embebidos", "Herramientas de privacidad", "Proyectos ESP32", "Seguridad de hardware", "Seguridad inalámbrica", "Seguridad de código abierto"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Detección Deauth", "Detección Evil Twin", "Seguridad WiFi", "Monitoreo WiFi pasivo", "Tramas de gestión 802.11", "Seguridad de red", "Seguridad IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Código abierto", "Sensor de seguridad", "Detección de amenazas inalámbricas", "Monitoreo BSSID", "Monitoreo SSID", "Detección degradación seguridad", "Detección inundación beacon", "Monitoreo WiFi", "LED RGB", "Modo promiscuo", "Seguridad embebida", "Seguridad en viajes", "Seguridad WiFi hotel", "WiFi cafetería", "Concienciación sobre seguridad", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Una ilustración de un pequeño dispositivo similar al ESP32 WiFi Canary, conectado a un puerto USB, con un LED RGB que brilla en varios colores sobre un fondo oscuro, simbolizando sus capacidades de detección de amenazas."
coverCaption: ""
---

**Un sensor WiFi pasivo del tamaño de un pulgar que nunca responde**

## Introducción: El problema con el WiFi público

Cada vez que se conecta al WiFi de un hotel, un café o una red de aeropuerto, confía en que el punto de acceso frente a usted es el real. El problema es que las **tramas de gestión 802.11**, las mismas tramas que anuncian redes, gestionan conexiones y coordinan clientes, están *completamente sin autenticar en la mayoría de los despliegues*. Cualquiera con hardware modesto puede clonar un SSID, enviar tramas de desautenticación a los clientes o configurar un señuelo abierto junto a una red WPA2 legítima.

El [**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) es un sensor de concienciación pasivo que aborda esta realidad con la huella más pequeña posible. Cabe en el M5Stack Atom Lite, un dispositivo aproximadamente del tamaño de un terrón de azúcar, se conecta a cualquier puerto USB, aprende el entorno circundante y enciende un LED RGB cuando detecta patrones consistentes con amenazas inalámbricas.

No se conecta a nada. No captura credenciales. No transmite ni una sola trama. Observa, puntúa y le dice de qué color es la situación.

Este artículo es una referencia técnica completa para el proyecto: qué detecta, cómo funciona el modelo de confianza, cómo construirlo y flashearlo, y cuáles son sus limitaciones en el mundo real.

---

## Qué hace el ESP32 WiFi Canary (y qué no hace)

### Solo pasivo, siempre

El WiFi Canary opera en dos modos de radio, nunca simultáneamente:

1. **Modo promiscuo** - recibe e inspecciona tramas de gestión 802.11 (desauth, disassoc) sin asociarse con ninguna red
2. **Modo escaneo** - realiza escaneos WiFi activos para enumerar los puntos de acceso cercanos y compararlos con una línea base aprendida

El dispositivo nunca:
- Se asocia o conecta a ninguna red
- Captura tramas de datos o credenciales
- Transmite tramas 802.11 de ningún tipo
- Almacena nada en flash persistente
- Comunica por internet

**Todo lo que aprende se mantiene en RAM y se reinicia al reiniciar.** Este diseño es intencional: el canary es un **sensor**, no un dispositivo de captura.

### El LED es la interfaz

No hay pantalla, no hay aplicación, no hay interfaz web. La única salida del dispositivo es un único **SK6812 RGB NeoPixel** en GPIO 27 del M5Stack Atom Lite. El LED habla un lenguaje de cuatro estados:

| Estado del LED | Significado |
|---------------|-------------|
| 🔵 Azul (pulso lento) | Inicio - construyendo referencia de línea base |
| 🟢 Verde (sólido) | Normal - sin problemas de alta confianza |
| 🟡 Amarillo (sólido) | Precaución - patrón sospechoso detectado |
| 🔴 Rojo (pulso rápido) | Alerta - amenaza de mayor confianza detectada |

El inicio tarda aproximadamente **24 segundos** (3 escaneos × 8 segundos cada uno).

---

## El proceso de aprendizaje de la línea base

### Por qué importa una línea base

Un canary que se active en cada red abierta de una ciudad sería inútil. El ESP32 WiFi Canary resuelve este problema aprendiendo su entorno antes de comenzar a puntuar amenazas.

### Tres escaneos, 24 segundos

Al inicio, el dispositivo realiza tres escaneos WiFi secuenciales. Después de completarlos todos, el conjunto aprendido de APs, SSID, BSSID, tipo de cifrado, intensidad de señal, se almacena como línea base.

---

## Qué detecta: Categorías de amenazas

El WiFi Canary monitorea cinco patrones de amenazas distintos.

### 1. Ráfagas de desautenticación / desasociación

| Condición | Puntos añadidos |
|-----------|----------------|
| ≥ 8 tramas de una fuente en 5 s | +2 |
| ≥ 20 tramas de una fuente en 5 s | +4 |
| ≥ 5 tramas de desauth en broadcast | +1 |

### 2. Clon abierto de una red cifrada conocida (Evil Twin)

| Condición | Puntos añadidos |
|-----------|----------------|
| Mismo SSID, estaba cifrado, ahora abierto | +3 |
| BSSID no visto en la línea base | +1 |
| Señal del clon ≥ 10 dB más fuerte que el AP conocido | +1 |

### 3. AP cifrado original desaparecido + Clon abierto presente

| Condición | Puntos añadidos |
|-----------|----------------|
| AP cifrado de línea base desaparecido + red abierta coincidente apareció | +3 |

### 4. Degradación de seguridad

| Condición | Puntos añadidos |
|-----------|----------------|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Caída de 2+ rangos de cifrado | +3 |

### 5. SSID duplicado de proveedor inesperado

| Condición | Puntos añadidos |
|-----------|----------------|
| OUI diferente del AP de línea base con el mismo SSID | +1 |
| El clon también es ≥ 10 dB más fuerte | +2 |

### 6. Inundación de beacon / SSID

| Condición | Puntos añadidos |
|-----------|----------------|
| ≥ 15 nuevos SSID en 30 s | +2 |
| ≥ 30 nuevos SSID en 30 s | +3 |

---

## El modelo de puntuación de confianza

Todas las señales detectadas alimentan una única **puntuación de amenaza** entera.

| Rango de puntuación | Estado del LED |
|---------------------|----------------|
| 0–2 | Normal (verde) |
| 3–5 | Precaución (amarillo) |
| 6+ | Alerta (rojo, pulso rápido) |

### Decaimiento de puntuación

La puntuación **cae 1 punto cada 60 segundos** sin nuevos eventos de activación.

---

## Construcción y flasheo

### Requisitos

- **PlatformIO** (CLI o extensión de VS Code)
- **M5Stack Atom Lite** (o cualquier ESP32 DevKit para pruebas)
- Cable USB-C

### Flashear en M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Construir y flashear
pio run -e atom-lite --target upload

# Abrir monitor serie a 115200 baudios
pio device monitor -b 115200
```

### Flashear en ESP32 DevKit genérico

```bash
pio run -e esp32dev --target upload
```

---

## Notas de detección y limitaciones prácticas

### Qué puede causar falsos positivos

**Las redes empresariales y de malla** son la mayor fuente de falsos positivos. Un gran despliegue empresarial, un hotel con muchos APs o un sistema de malla puede mostrar legítimamente múltiples BSSID para el mismo SSID con diferentes OUI de proveedores.

### Qué puede causar falsos negativos

**Un ataque Evil Twin bien elaborado** que suplanta el BSSID exacto del AP legítimo *puede no acumular suficiente puntuación para cruzar el umbral de Precaución*.

---

## Casos de uso

### Viajar con trabajo sensible

El canary está diseñado principalmente para viajes. Conéctelo al puerto USB de un portátil, a una toma USB de una habitación de hotel o a un banco de energía portátil, y déjelo aprender el entorno.

### Cafeterías y WiFi público

Los entornos de WiFi abierto son la superficie de ataque más común para las configuraciones Evil Twin.

### Concienciación sobre seguridad y formación

La salida serie del dispositivo proporciona un registro detallado y legible por humanos.

### Monitoreo pasivo de laboratorio

En un laboratorio casero o pequeña oficina, el canary puede servir como monitor ambiental persistente.

---

## Conclusión

El ESP32 WiFi Canary es una herramienta de alcance estrecho que hace una cosa: observar el entorno de 2,4 GHz a su alrededor y cambiar de color cuando algo parece incorrecto. No intenta ser un sistema completo de detección de intrusos inalámbricos. Es un canario, un sensor pasivo cuyo trabajo es notar cuando la mina se vuelve peligrosa.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
