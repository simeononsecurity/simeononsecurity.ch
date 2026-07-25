---
title: "Flock Finder: herramienta de código abierto para mapear cámaras de vigilancia ALPR de Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder es una herramienta de código abierto que mapea más de 40.000 cámaras ALPR de Flock Safety en todo el mundo usando datos WiFi de WiGLE y huella digital OUI. Aprenda cómo funciona, sus limitaciones y las herramientas de hardware para detección en tiempo real."
genre: ["Tecnología de privacidad", "Contra-vigilancia", "Proyectos de código abierto", "Derechos digitales", "Seguridad de redes", "Herramientas de privacidad", "Hacking de hardware", "Investigación de seguridad"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "lector de matrículas", "huella digital OUI", "WiGLE", "vigilancia WiFi", "contra-vigilancia", "STS Collective", "FlockYou", "ESP32", "herramientas de privacidad", "NitekryDPaul", "DeFlockJoplin", "detección ALPR", "seguridad de código abierto", "mapeo de vigilancia", "vigilancia masiva", "OUI WiFi", "protección de privacidad", "dirección MAC", "modo promiscuo", "802.11", "detección en tiempo real", "wardriving", "derechos digitales", "libertades civiles", "conciencia sobre vigilancia", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Un mapa interactivo que muestra marcadores coloridos que indican ubicaciones de cámaras ALPR de Flock Safety, con señales WiFi abstractas emanando de los marcadores sobre un fondo oscuro."
coverCaption: "Flock Finder mapea más de 40.000 cámaras ALPR de Flock Safety sospechosas usando datos WiFi de WiGLE y huella digital OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Una herramienta de conciencia de vigilancia de código abierto que mapea cámaras ALPR de Flock Safety usando datos WiFi de fuentes abiertas.**

## ¿Qué es Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** es un proyecto de código abierto que mapea **cámaras ALPR (lectores automáticos de matrículas) de Flock Safety** en los Estados Unidos y 108 otros países. Combina **31 prefijos OUI (Identificador Único Organizacional) WiFi conocidos de Flock Safety** con la **base de datos WiFi participativa WiGLE** para identificar y representar ubicaciones sospechadas de cámaras en un mapa interactivo.

El proyecto está en **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, se actualiza automáticamente a diario mediante GitHub Actions y, a julio de 2026, ha mapeado **más de 40.000 cámaras sospechadas** en 964 regiones de todo el mundo.

| Métrica | Valor |
|--------|-------|
| **Cámaras mapeadas** | 40.026+ |
| **Prefijos OUI conocidos** | 31 |
| **Países cubiertos** | 109 |
| **Regiones cubiertas** | 964 |
| **Retención de datos** | 730 días (2 años) |
| **Frecuencia de actualización automática** | Diaria |

*Esta es una herramienta de concienciación general, no un inventario definitivo. Lea la sección de limitaciones antes de sacar conclusiones de los datos.*

______

## Cómo funciona: huella digital OUI a través de WiGLE

### La idea central

Las cámaras Flock Safety contienen **transceptores WiFi** que se despiertan periódicamente para cargar datos de matrículas capturadas a la nube. Durante estas breves ventanas activas, la cámara transmite tramas WiFi que contienen su **dirección MAC**. Los primeros tres bytes de cada dirección MAC identifican al fabricante. Este es el **OUI (Identificador Único Organizacional)**.

El investigador de seguridad **@NitekryDPaul** descubrió **30 prefijos OUI** consistentemente asociados con el hardware de cámaras Flock Safety mediante **análisis en modo promiscuo de 2,4 GHz**. Un 31.º prefijo (`82:6B:F2`) fue aportado por **Michael / DeFlockJoplin** durante pruebas de campo en Joplin, MO.

Flock Finder toma esos 31 OUI, consulta WiGLE por cualquier red WiFi registrada que coincida con esos prefijos, y representa los resultados en un mapa.

### La técnica de detección addr1

El descubrimiento clave de @NitekryDPaul va más allá de simplemente coincidir con la dirección MAC del transmisor. Las cámaras Flock pasan la mayor parte de su ciclo de trabajo en **modo de reposo**. Cuando un punto de acceso cercano envía una trama dirigida *a* una cámara, la dirección MAC de la cámara aparece como **addr1 (la dirección del receptor)** en las tramas 802.11, incluso mientras la propia cámara no está transmitiendo activamente.

Combinada con la **detección de solicitudes de sonda genéricas** (tramas de gestión 802.11 tipo=0, subtipo=4, SSID vacío), esto produce una firma de detección muy precisa. Las pruebas de campo en Joplin, MO lograron detectar **11 de 12 cámaras con solo 2 falsos positivos**.

> ⚠️ **Importante**: el mapa Flock Finder basado en WiGLE **no** implementa la técnica addr1. WiGLE es un conjunto de datos histórico, recopilado pasivamente. Solo registra transmisores, no receptores. Para la detección en tiempo real que realmente usa el método de @NitekryDPaul, necesita hardware dedicado en el campo.

______

## Usar el mapa en vivo

El mapa interactivo está disponible en **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Muestra:

- **Marcadores de cámaras agrupados** codificados por color según el prefijo OUI
- **Búsqueda** por ciudad, estado o BSSID
- **Tabla de datos OUI** con recuentos de cámaras por prefijo
- **Panel de estadísticas** que muestra el total de cámaras, regiones y la marca de tiempo de la última actualización
- **Página sobre los ALPR** con daños documentados a la privacidad, contexto legal y recursos comunitarios

Las exportaciones de datos del mapa también están disponibles directamente:

- `data/flock_cameras.geojson` — GeoJSON para uso en QGIS, Leaflet u otras herramientas
- `data/flock_cameras.csv` — formato compatible con hojas de cálculo
- `data/scan_stats.json` — estadísticas y recuentos de escaneos

### Limitaciones importantes

**Tome el mapa con cautela.** WiGLE es un conjunto de datos participativo, actualizado esporádicamente, no un feed en vivo.

- **Las cámaras Flock no transmiten continuamente.** Se despiertan brevemente para cargar datos, por lo que los registros de WiGLE dependen completamente de que un wardriver esté cerca en el momento exacto.
- **Los datos pueden tener meses o años de antigüedad.** Las cámaras que han sido reubicadas o retiradas pueden seguir apareciendo.
- **La coincidencia OUI es una heurística.** Los OUI pueden ser compartidos, reasignados o falsificados. Cada resultado es un dispositivo Flock *sospechado*, no confirmado.
- **La cobertura es desigual.** Las zonas metropolitanas densas tienen más datos de WiGLE; las áreas rurales tienen mucho menos.

*Use el mapa para desarrollar una conciencia general de la densidad de vigilancia en su área. Para detección en tiempo real basada en datos del terreno, consulte las opciones de hardware a continuación.*

______

## Ejecutar Flock Finder usted mismo

### Requisitos previos

- Python 3.8+
- Una cuenta gratuita de [WiGLE](https://wigle.net/account) con credenciales de API

### Configuración

```bash
# Clonar el repositorio
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Instalar dependencias
pip install -r requirements.txt

# Configurar sus credenciales de API de WiGLE
cp .env.example .env
# Edite .env con su nombre de API de WiGLE y su token
```

### Ejecutar el escáner

```bash
# Escaneo completo — los 31 prefijos OUI, en todo el mundo
python3 scripts/wigle_query.py

# Prueba de un único OUI
python3 scripts/wigle_query.py --oui 70:C9:4E

# Solo EE.UU.
python3 scripts/wigle_query.py --country US

# Cuadro delimitador específico (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Simulación — verificar autenticación, sin consultas API
python3 scripts/wigle_query.py --dry-run
```

### Ver el mapa localmente

```bash
python3 -m http.server 8080 --directory docs/
# Abra http://localhost:8080 en su navegador
```

### Actualizaciones automáticas diarias mediante GitHub Actions

Bifurque el repositorio y agregue sus credenciales de WiGLE como **secretos del repositorio** (`WIGLE_API_NAME` y `WIGLE_API_TOKEN`). El flujo de trabajo incluido se ejecuta a las 6 AM UTC diariamente y confirma automáticamente los archivos de datos actualizados cuando se encuentran nuevas cámaras.

______

## Detección en tiempo real: hardware FlockYou de STS Collective

El mapa WiGLE le indica dónde *han sido observadas* las cámaras. Para la detección en tiempo real mientras conduce, usando el método de coincidencia OUI de @NitekryDPaul en tráfico WiFi en vivo, necesita hardware dedicado.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** fabrica detectores portátiles basados en ESP32 que escanean las firmas OUI de Flock y le alertan en el momento en que se detecta una firma coincidente.

### Línea de productos FlockYou

| Dispositivo | Descripción |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Detector Flock compacto, de bolsillo. Preinstalado, plug-and-play. Alertas LED al detectar. |
| **FlockYou Pro — LED + Audio** | Añade alertas de audio junto con indicadores LED. No pierda ninguna cámara mientras conduce. |
| **FlockYou Atom VoiceS3R** | Detector con voz y alertas de audio habladas para operación manos libres, con los ojos en la carretera. |

Todos los dispositivos:
- **Preinstalados**, listos para usar directamente
- Escanean el tráfico WiFi en vivo para los 31 OUI Flock conocidos
- Compactos y portátiles, caben en un portavasos o en un bolsillo
- Alimentados por USB-C (adaptador de coche, batería portátil o portátil)

> 💰 **Descuentos exclusivos**: use el código **FLOCKFINDER** para un **20% de descuento** en todos los dispositivos FlockYou de STS Collective, o use el código **SIMEONONSECURITY** para hasta un 20% de descuento en todo su pedido. [Compre en stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Estructura del proyecto

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # Consulta de API WiGLE y pipeline de datos
├── data/
│   ├── flock_ouis.csv         # 31 prefijos OUI Flock Safety conocidos
│   ├── flock_cameras.geojson  # Ubicaciones de cámaras (GeoJSON)
│   ├── flock_cameras.csv      # Ubicaciones de cámaras (CSV)
│   └── scan_stats.json        # Estadísticas de escaneo
├── docs/
│   └── index.html             # Mapa interactivo Leaflet
└── .github/workflows/
    └── update-data.yml        # Flujo de trabajo de actualización automática diaria
```

______

## Preguntas frecuentes

### ¿Es legal?

Sí. **Flock Finder utiliza únicamente datos disponibles públicamente** de la base de datos WiGLE, que agrega datos de encuestas WiFi contribuidos voluntariamente. No hay piratería, acceso no autorizado ni sistemas propietarios involucrados. La monitorización pasiva de WiFi para firmas OUI es legal en los Estados Unidos.

### ¿Cada cámara mapeada es definitivamente una cámara Flock?

No. La coincidencia OUI es una **heurística**. Los prefijos OUI pueden ser compartidos entre fabricantes, reasignados o falsificados. Cada registro en la base de datos es un dispositivo Flock *sospechado*, no confirmado.

### ¿Por qué algunos prefijos OUI no muestran cámaras?

La cobertura de WiGLE es desigual. Si ningún wardriver ha escaneado una zona determinada con ese OUI específico activo, no habrá registros. *La ausencia de datos no significa ausencia de cámaras.*

### ¿Qué tan actualizados están los datos?

El flujo de trabajo de GitHub Actions se ejecuta diariamente y extrae los últimos resultados de WiGLE. Sin embargo, WiGLE en sí puede tener registros que van desde días hasta años de antigüedad para cualquier ubicación. Consulte el archivo `scan_stats.json` para ver la marca de tiempo del escaneo más reciente.

### ¿Puedo contribuir mis propios datos de wardrive?

Sí. Suba sus datos de wardrive a [WiGLE](https://wigle.net). Se alimentan automáticamente en el próximo escaneo diario de Flock Finder. También puede contribuir con prefijos OUI o mejoras de código a través de la [Guía de contribución](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Comunidad y proyectos relacionados

Flock Finder no está solo. Un ecosistema creciente de herramientas y organizaciones trabaja para documentar y contrarrestar la vigilancia ALPR:

- **[DeFlock.org](https://deflockjoplin.org/)** — Seguimiento de ALPR impulsado por la comunidad, documentación y defensa
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Verifique si su matrícula ha sido buscada en el sistema de Flock
- **[FlockHopper](https://flockhopper.com/)** — Planificación de rutas que evita las cámaras ALPR conocidas
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — La base de datos de la EFF de tecnología de vigilancia utilizada por las fuerzas del orden
- **[NoALPRs.com](https://noalprs.com/)** — Recursos para comunidades que luchan contra los despliegues ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Firmware de código abierto e investigación de campo; contribuyó el 31.º prefijo OUI

______

## Créditos

- **Investigación OUI**: @NitekryDPaul — los 30 prefijos OUI originales y la estrategia de detección addr1/modo promiscuo
- **Pruebas de campo**: Michael / DeFlockJoplin — 31.º prefijo OUI (`82:6B:F2`) y ajuste de la sonda genérica
- **Fuente de datos**: [WiGLE](https://wigle.net) — base de datos de redes WiFi/celular participativa
- **Inspirado por**: [DeFlock](https://deflockjoplin.org/) y track-openroaming-passpoint
- **Socio de hardware**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — detectores FlockYou ESP32

______

## Conclusión

**Flock Finder** da a cualquiera una idea rápida y visual de cuán ampliamente se han desplegado las cámaras ALPR de Flock Safety: más de 40.000 ubicaciones estimadas en 109 países, actualizadas automáticamente cada día a partir de datos WiFi participativos.

Es una **herramienta de transparencia**, no un rastreador en vivo. Sus datos son históricos, incompletos y probabilísticos. Pero hace visible la escala de la vigilancia ALPR de una manera que los informes y resúmenes no pueden.

Para una protección genuina en tiempo real mientras atraviesa zonas vigiladas, combine el mapa con hardware dedicado. **[Los dispositivos FlockYou de STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implementan el método de detección de @NitekryDPaul directamente en un ESP32 y le alertan en el momento en que se detecta una firma de cámara en vivo. Disponibles en **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** con el código **FLOCKFINDER** o **SIMEONONSECURITY** para hasta un 20% de descuento.

______

## Referencias

1. [Repositorio GitHub de Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Mapa interactivo de Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — dispositivos FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — mapeo de redes inalámbricas](https://wigle.net)
5. [DeFlock — concienciación comunitaria sobre ALPR](https://deflockjoplin.org/)
6. [DeFlockJoplin — firmware de detección de código abierto](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Usted está siendo rastreado](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
