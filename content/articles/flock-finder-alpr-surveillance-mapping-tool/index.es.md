---
title: "Flock Finder: Mapa de cámaras ALPR de Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder es una herramienta de código abierto que mapea más de 40.000 cámaras Flock Safety ALPR en todo el mundo utilizando datos WiFi de WiGLE y huellas digitales OUI. Aprende cómo funciona, sus limitaciones y las herramientas de hardware para la detección en tiempo real."
genre: ["Tecnología de privacidad", "Contravigilancia", "Proyectos de código abierto", "Derechos digitales", "Seguridad de redes", "Herramientas de privacidad", "Hacking de hardware", "Investigación de seguridad"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Lector de matrículas", "Huella digital OUI", "WiGLE", "Vigilancia WiFi", "Contravigilancia", "STS Collective", "FlockYou", "ESP32", "Herramientas de privacidad", "NitekryDPaul", "DeFlockJoplin", "Detección ALPR", "Seguridad de código abierto", "Mapeo de vigilancia", "Vigilancia masiva", "WiFi OUI", "Protección de privacidad", "Dirección MAC", "Modo promiscuo", "802.11", "Detección en tiempo real", "Wardriving", "Derechos digitales", "Libertades civiles", "Conciencia de vigilancia", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Un mapa interactivo que muestra marcadores de colores que indican las ubicaciones de las cámaras Flock Safety ALPR, con señales WiFi abstractas emanando de los marcadores sobre un fondo oscuro."
coverCaption: "Flock Finder mapea más de 40.000 presuntas cámaras Flock Safety ALPR utilizando datos WiFi de WiGLE y huellas digitales OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Una herramienta de código abierto para la concienciación sobre la vigilancia que mapea las cámaras Flock Safety ALPR utilizando datos WiFi de colaboración ciudadana.**

## ¿Qué es Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** es un proyecto de código abierto que mapea las **cámaras Flock Safety ALPR (Lector Automático de Matrículas)** en los Estados Unidos y en otros 108 países. Combina **31 prefijos OUI (Identificador Único Organizacional) WiFi de Flock Safety conocidos** con la **base de datos WiFi colaborativa WiGLE** para identificar y representar las ubicaciones de cámaras sospechosas en un mapa interactivo.

El proyecto se encuentra en **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, se actualiza automáticamente cada día a través de GitHub Actions y, a partir de julio de 2026, ha mapeado **más de 40.000 cámaras sospechosas** en 964 regiones de todo el mundo.

| Métrica | Valor |
|--------|-------|
| **Cámaras mapeadas** | 40.026+ |
| **Prefijos OUI conocidos** | 31 |
| **Países cubiertos** | 109 |
| **Regiones cubiertas** | 964 |
| **Retención de datos** | 730 días (2 años) |
| **Frecuencia de actualización automática** | Diariamente |

*Esta es una herramienta de concienciación general, no un inventario definitivo. Lee la sección de limitaciones antes de sacar conclusiones de los datos.*

Para obtener contexto sobre por qué la vigilancia ALPR de Flock Safety es importante para la privacidad, lee **[Vigilancia de cámaras Flock Safety: Prevalencia, preocupaciones de privacidad y estrategias de protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## Cómo funciona: Huella digital OUI a través de WiGLE

### La idea central

Las cámaras Flock Safety contienen **transceptores WiFi** que se despiertan periódicamente del sueño para subir los datos de matrícula capturados a la nube. Durante estas breves ventanas activas, la cámara emite tramas WiFi que contienen su **dirección MAC** — y los primeros tres bytes de cada dirección MAC identifican al fabricante. Esto es el **OUI (Identificador Único Organizacional)**.

El investigador de seguridad **@NitekryDPaul** descubrió **30 prefijos OUI** consistentemente asociados con el hardware de las cámaras Flock Safety mediante **análisis 2,4 GHz en modo promiscuo**. Un 31.º prefijo (`82:6B:F2`) fue aportado por **Michael / DeFlockJoplin** durante las pruebas de campo en Joplin, MO.

Flock Finder toma esos 31 OUIs, consulta WiGLE en busca de redes WiFi registradas que coincidan con esos prefijos y representa los resultados en un mapa.

### Los 31 prefijos OUI conocidos de Flock Safety

| # | Prefijo OUI | Fuente | # | Prefijo OUI | Fuente |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### La técnica de detección addr1

El descubrimiento clave de @NitekryDPaul va más allá de simplemente hacer coincidir la dirección MAC del transmisor. Las cámaras Flock pasan la mayor parte de su ciclo de trabajo **durmiendo**. Cuando un punto de acceso cercano envía un marco dirigido *a* una cámara, la MAC de la cámara aparece como **addr1 (la dirección del receptor)** en las tramas 802.11 — incluso mientras la propia cámara no transmite activamente.

Combinado con la **detección de solicitudes de sonda wildcard** (tramas de gestión 802.11 tipo=0, subtipo=4, SSID vacío), esto produce una firma de detección muy precisa. Las pruebas de campo en Joplin, MO lograron **11 de 12 cámaras detectadas con solo 2 falsos positivos**.

> ⚠️ **Importante**: El mapa Flock Finder basado en WiGLE **no** implementa la técnica addr1. WiGLE es un conjunto de datos históricos, recopilados pasivamente — solo registra transmisores, no receptores. Para la detección en tiempo real que realmente usa el método de @NitekryDPaul, necesitas hardware dedicado funcionando en el campo.

______

## Uso del mapa en vivo

El mapa interactivo está disponible en **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Muestra:

- **Marcadores de cámara agrupados** codificados por color según el prefijo OUI
- **Búsqueda** por ciudad, estado o BSSID
- **Tabla de datos OUI** con recuentos de cámaras por prefijo
- **Panel de estadísticas** que muestra el total de cámaras, regiones y la última marca de tiempo de actualización
- **Página sobre ALPRs** con daños de privacidad documentados, contexto legal y recursos comunitarios

Las exportaciones de datos del mapa también están disponibles directamente:

- `data/flock_cameras.geojson` — GeoJSON para uso en QGIS, Leaflet u otras herramientas
- `data/flock_cameras.csv` — formato compatible con hojas de cálculo
- `data/scan_stats.json` — estadísticas y recuentos de escaneo

### Limitaciones clave

**Toma el mapa con cautela.** WiGLE es un conjunto de datos de colaboración ciudadana, actualizado esporádicamente, no una transmisión en directo.

- **Las cámaras Flock no transmiten continuamente.** Se despiertan brevemente para subir datos, por lo que los registros de WiGLE dependen completamente de que un wardriver esté cerca exactamente en el momento adecuado.
- **Los datos pueden tener meses o años de antigüedad.** Las cámaras que han sido trasladadas o eliminadas pueden seguir apareciendo.
- **La coincidencia OUI es una heurística.** Los OUIs pueden compartirse, reasignarse o falsificarse. Cada resultado es un dispositivo Flock *sospechoso*, no confirmado.
- **La cobertura es desigual.** Las zonas metropolitanas densas tienen más datos de WiGLE; las áreas rurales tienen mucho menos.

*Usa el mapa para desarrollar una conciencia general de la densidad de vigilancia en tu área. Para la detección en tiempo real con datos reales sobre el terreno, consulta las opciones de hardware a continuación.*

______

## Ejecutar Flock Finder tú mismo

### Requisitos previos

- Python 3.8+
- Una cuenta gratuita de [WiGLE](https://wigle.net/account) con credenciales de API

### Configuración

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### Ejecutar el escáner

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### Ver el mapa localmente

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### Actualizaciones diarias automatizadas a través de GitHub Actions

Haz un fork del repositorio y agrega tus credenciales de WiGLE como **secretos del repositorio** (`WIGLE_API_NAME` y `WIGLE_API_TOKEN`). El flujo de trabajo incluido se ejecuta a las 6 AM UTC diariamente y confirma automáticamente los archivos de datos actualizados cada vez que se encuentran nuevas cámaras.

______

## Detección en tiempo real: Hardware STS Collective FlockYou

El mapa de WiGLE te dice dónde se han *observado* las cámaras. Para la detección en tiempo real mientras conduces — usando el método real de coincidencia OUI de @NitekryDPaul en tráfico WiFi en vivo — necesitas hardware dedicado.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** fabrica detectores portátiles basados en ESP32 que buscan firmas OUI de Flock y te alertan en el momento en que se detecta una firma coincidente.

### Línea de dispositivos FlockYou

| Dispositivo | Descripción |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Detector Flock compacto, de tamaño de bolsillo. Preflasheado, plug-and-play. Alertas LED al detectar. |
| **FlockYou Pro — LED + Audio** | Agrega alertas de audio junto con indicadores LED. Nunca te pierdas una cámara mientras conduces. |
| **FlockYou Atom VoiceS3R** | Detector con voz con alertas de audio habladas para una operación con manos libres y ojos en la carretera. |

Todos los dispositivos:
- **Preflasheados**, listos para usar directamente de la caja
- Escanean el tráfico WiFi en vivo en busca de los 31 OUIs de Flock conocidos
- Compactos y portátiles — caben en un portavasos o bolsillo
- Alimentados por USB-C (adaptador de coche, batería externa o portátil)

> 💰 **Descuentos exclusivos**: Usa el código **FLOCKFINDER** para un **20% de descuento** en todos los dispositivos STS Collective FlockYou — o usa el código **SIMEONONSECURITY** para hasta un 20% de descuento en tu pedido completo. [Compra en stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Para un análisis técnico completo de estos dispositivos y alternativas DIY, lee la **[Guía completa de hardware y configuración del Proyecto de Detección Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Estructura del proyecto

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## Preguntas frecuentes

### ¿Es legal?

Sí. **Flock Finder utiliza únicamente datos disponibles públicamente** de la base de datos de WiGLE, que agrega datos de encuestas WiFi contribuidos voluntariamente. No hay piratería, acceso no autorizado ni sistemas propietarios involucrados. El monitoreo pasivo de WiFi para firmas OUI es legal en los Estados Unidos.

### ¿Cada cámara mapeada es definitivamente una cámara Flock?

No. La coincidencia OUI es una **heurística**. Los prefijos OUI pueden compartirse entre fabricantes, reasignarse o falsificarse. Cada registro en la base de datos es un dispositivo Flock *sospechoso* — no confirmado. Lee la [Política de datos](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) para obtener detalles sobre cómo solicitar una corrección.

### ¿Por qué algunos prefijos OUI no muestran cámaras?

La cobertura de WiGLE es desigual. Si ningún wardriver ha escaneado un área determinada con ese OUI específico activo, no habrá registros. *La ausencia de datos no significa la ausencia de cámaras.*

### ¿Qué tan actualizados están los datos?

El flujo de trabajo de GitHub Actions se ejecuta diariamente y obtiene los últimos resultados de WiGLE. Sin embargo, WiGLE en sí puede tener registros que van desde días hasta años de antigüedad para cualquier ubicación determinada. Revisa el archivo `scan_stats.json` para obtener la marca de tiempo del escaneo más reciente.

### ¿Puedo contribuir con mis propios datos de wardrive?

Sí. Sube tus datos de wardrive a [WiGLE](https://wigle.net) — se incorporan automáticamente al próximo escaneo diario de Flock Finder. También puedes contribuir con prefijos OUI o mejoras de código a través de la [Guía de contribución](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Comunidad y proyectos relacionados

Flock Finder no actúa solo. Un ecosistema creciente de herramientas y organizaciones trabaja para documentar y combatir la vigilancia ALPR:

- **[DeFlock.org](https://deflockjoplin.org/)** — Seguimiento, documentación y defensa de ALPR impulsados por la comunidad
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Comprueba si tu matrícula ha sido buscada en el sistema de Flock
- **[FlockHopper](https://flockhopper.com/)** — Planificación de rutas que evita cámaras ALPR conocidas
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Base de datos de la EFF sobre tecnología de vigilancia utilizada por las fuerzas del orden
- **[NoALPRs.com](https://noalprs.com/)** — Recursos para comunidades que luchan contra los despliegues de ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Firmware de código abierto e investigación de campo; contribuyó el 31.º prefijo OUI

______

## Créditos

- **Investigación OUI**: @NitekryDPaul — todos los 30 prefijos OUI originales y la estrategia de detección addr1/modo promiscuo
- **Pruebas de campo**: Michael / DeFlockJoplin — 31.º prefijo OUI (`82:6B:F2`) y ajuste de sonda wildcard
- **Fuente de datos**: [WiGLE](https://wigle.net) — base de datos WiFi/red celular de colaboración ciudadana
- **Inspirado por**: [DeFlock](https://deflockjoplin.org/) y track-openroaming-passpoint
- **Socio de hardware**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — detectores FlockYou ESP32

______

## Conclusión

**Flock Finder** da a cualquier persona una idea rápida y visual de cuán ampliamente se han desplegado las cámaras Flock Safety ALPR — más de 40.000 ubicaciones estimadas en 109 países, actualizadas automáticamente cada día a partir de datos WiFi de colaboración ciudadana.

Es una **herramienta de transparencia**, no un rastreador en vivo. Sus datos son históricos, incompletos y probabilísticos. Pero hace visible la escala de la vigilancia ALPR de una manera que los resúmenes e informes no pueden.

Para una protección genuina en tiempo real mientras te mueves por áreas vigiladas, combina el mapa con hardware dedicado. **[Los dispositivos FlockYou de STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implementan el método de detección de @NitekryDPaul directamente en un ESP32 y te alertan en el momento en que se detecta una firma de cámara en vivo — disponibles en **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** con el código **FLOCKFINDER** o **SIMEONONSECURITY** para hasta un 20% de descuento.

### Artículos relacionados

| Artículo | Qué cubre |
|---------|---------------|
| **[Vigilancia de cámaras Flock Safety: Privacidad y protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | El cuadro completo: estadísticas de prevalencia, cuestiones de libertades civiles, kit de herramientas ACLU, estadísticas DeFlock, guía FOIA y estrategias de protección |
| **[Proyecto de Detección Flock-You: Guía de hardware de contravigilancia](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guía técnica completa de detectores Flock basados en ESP32 — OUI-SPY, M5 Atom Lite, construcción DIY, configuración de firmware paso a paso |
| **[Cómo flashear dispositivos Rayhunter: Guía completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detectar captadores IMSI (simuladores de estaciones base) junto a cámaras ALPR para una concienciación completa sobre contravigilancia |
| **[Firmware personalizado DagShell para Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Convertir un punto de acceso móvil en una plataforma de investigación de seguridad — se integra bien con el hardware de detección Flock |
| **[Comparación de dispositivos Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparar opciones de hardware de detección entre categorías de amenazas ALPR y de vigilancia celular |

______

## Referencias

1. [Repositorio GitHub de Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Mapa interactivo de Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — Dispositivos FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Mapeo de redes inalámbricas](https://wigle.net)
5. [DeFlock — Concienciación comunitaria sobre ALPR](https://deflockjoplin.org/)
6. [DeFlockJoplin — Firmware de detección de código abierto](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Estás siendo rastreado](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
