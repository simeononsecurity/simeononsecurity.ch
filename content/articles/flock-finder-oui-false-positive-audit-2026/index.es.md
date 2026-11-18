---
title: "Mapeamos 146.526 «cámaras Flock». 50.278 eran sistemas ClickShare"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Una auditoría de Flock Finder detecta ClickShare y otros falsos positivos, explica las pruebas y documenta los cambios."
genre: ["Investigación de seguridad", "Tecnología de privacidad", "Proyectos de código abierto", "Periodismo de datos", "Contravigilancia"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Huella OUI", "WiGLE", "Falsos positivos", "Calidad de datos", "Barco ClickShare", "Dirección MAC", "IEEE OUI", "Huella de elementos de información", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Rendición de cuentas de código abierto", "Mapeo de vigilancia", "WiFi", "Solicitud de sondeo", "Aleatorización MAC"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "Un mapa urbano oscuro lleno de marcadores rojos que resultan ser dispositivos WiFi de oficina, mientras unos pocos marcadores verdes representan detecciones más sólidas"
coverCaption: "La auditoría de 146.526 registros de Flock Finder reveló cómo una observación de campo útil se convirtió en una afirmación cartográfica demasiado segura."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**Colocamos 146.526 puntos en un mapa de cámaras de vigilancia. Al menos 50.278 eran sistemas de presentación Barco ClickShare. El hardware de salas de conferencias representaba más de un tercio de lo que nuestro titular llamó «cámaras mapeadas».**

Este era nuestro proyecto, nuestra canalización de datos y nuestro error. Flock Finder consultaba WiGLE a diario para encontrar prefijos MAC observados en cámaras Flock Safety, publicaba resultados con coordenadas de precisión completa y dibujaba todos los datos con el mismo marcador. Los metadatos incluían la palabra `suspected` y la documentación mencionaba falsos positivos. Aun así, el mapa y el titular transmitían certeza.

**Resultado para el lector:** reproduce la auditoría, separa observación y atribución y muestra el nivel de confianza junto al marcador y al titular. Una coincidencia de prefijo sirve para investigar, no demuestra que se trate de una cámara.

Cuando generamos un histograma de frecuencias de la columna SSID, el conjunto de datos explicó el fallo en minutos. ClickShare era solo la categoría más grande. Otros 6.099 registros se llamaban `SMARTGATE_*`, 3.801 empezaban por el prefijo genérico WiFi Direct `DIRECT-`, 314 tenían exactamente el nombre `AndroidAP`, 138 decían `Audi HUD`, 133, `MAX-PRINTER`, y 30 contenían la cadena de veredicto de otro detector. En total, **60.793 filas, o el 41,5%, cumplían las reglas de nombres conocidas para otros dispositivos del análisis original.**

Ahora Flock Finder publica una clase de evidencia por registro, excluye por defecto del mapa y del titular el hardware conocido como ajeno, ofrece filtros, marca registros fuera del mercado principal y separa los prefijos de alta confianza de los de fabricantes por contrato. Este artículo documenta el error, las pruebas y los límites que siguen.

______

## Cómo funciona la detección comunitaria de ALPR

Los detectores de Flock creados por la comunidad suelen combinar tres tipos de evidencia inalámbrica:

1. **Prefijos WiFi MAC/OUI.** Los primeros bytes de una dirección MAC administrada globalmente pueden identificar la organización que recibió el bloque de direcciones.
2. **Comportamiento WiFi.** Un SSID, una solicitud de sondeo comodín, la dirección del receptor, un patrón de canales o una secuencia de elementos de información 802.11 pueden precisar la clase del dispositivo.
3. **Evidencia Bluetooth.** Los identificadores de fabricante y los UUID de servicio pueden identificar radios expuestas por un producto o una generación de firmware.

La coincidencia OUI se hizo común porque es barata y pasiva. Un ESP32 económico puede examinar tramas 802.11 cercanas sin conectarse a una red. Una base histórica como [WiGLE](https://wigle.net/) también permite buscar observaciones anteriores sin desplegar escáneres propios.

El método siguió una línea comunitaria: el mapeo y la organización local de [DeFlock](https://deflock.org/), [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), bifurcaciones y proyectos complementarios como nuestro [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32), y, finalmente, [Flock Finder](https://github.com/simeononsecurity/flock-finder), que aplicó la lista de prefijos a datos de WiGLE en todo el mundo.

El trabajo de campo original merece un reconocimiento claro. [@NitekryDPaul](https://github.com/NitekryDPaul) observó 30 prefijos en equipos Flock reales mediante investigación en modo promiscuo. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) aportó otro durante pruebas de campo. Esas observaciones eran legítimas. Nuestro error posterior fue tratar **«observado en una cámara Flock» como si significara «exclusivo de las cámaras Flock».**

______

## El defecto estructural: un OUI describe la cadena de suministro

IEEE describe un OUI como un identificador de 24 bits asignado a un proveedor, fabricante u otra organización. Junto con otros 24 bits elegidos por el receptor, forma una dirección MAC. La [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/) publica el registro.

Eso indica quién recibió un bloque de direcciones, no necesariamente qué marca aparece en el producto terminado. Los fabricantes por contrato construyen módulos de radio para muchos clientes. Por eso, un proveedor de chips puede aparecer en cámaras, proyectores, impresoras, vehículos y placas para aficionados.

Las asignaciones del registro detrás de nuestra lista ya mostraban el riesgo:

| Registrante | Prefijos en la lista auditada |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` y otros |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

Las entradas de Espressif debieron alertarnos. Dos prefijos de una supuesta lista de cámaras pertenecían al fabricante de una de las plataformas WiFi integradas más comunes del mundo, incluido el silicio usado por muchos detectores comunitarios.

`B4:1E:52` es distinto porque está registrado directamente a Flock Safety. Se había añadido a la lista de 38 prefijos en el commit auditado, **pero aún no se había consultado**: `scan_stats.json` informaba de 31 prefijos consultados. Lo mismo ocurría con seis prefijos de baterías recién añadidos. La instantánea no demuestra si el prefijo propio de Flock es frecuente o raro. No convertiremos «no consultado» en «cero resultados».

El repositorio actual contiene 39 prefijos tras añadir `E0:0A:F6` para igualar el firmware del detector. El resumen de escaneo conservado todavía muestra datos de 31 prefijos. Por tanto, las entradas más recientes siguen pendientes de un recálculo completo, no son prefijos con cero resultados demostrado.

______

## El conjunto de datos se auditó a sí mismo

Cada cifra histórica que sigue se regeneró desde `data/flock_cameras.csv` en el commit de Flock Finder [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829), con `csv` y `collections.Counter` de la biblioteca estándar de Python. No hizo falta otra prueba de conducción. Los nombres, la geografía y la composición de prefijos ya contradecían el titular. Las cifras de la implementación corregida proceden del resumen `scan_stats.json` que conserva el repositorio actual.

### La geografía fue una alerta temprana

De 146.526 filas, 75.818 estaban en Estados Unidos, 70.674 fuera y 34 no tenían país. Alemania aportaba 13.491 registros, seguida de Canadá con 6.251, Francia con 5.839, Gran Bretaña con 4.836, Países Bajos con 4.636 y Suiza con 4.515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Barra apilada con 75.818 registros de Estados Unidos, 70.674 de fuera y 34 sin valor de país" caption="El histograma de países suma 146.492 porque 34 filas tienen el país nulo." >}}

La geografía sirve para filtrar, no como prueba. Flock describe su red como «nacional» y dice que conecta clientes en [49 estados de EE. UU.](https://www.flocksafety.com/flock-ecosystem). La expansión internacional también puede cambiar los límites del mercado. Marcamos las filas fuera del mercado para revisarlas, en lugar de borrarlas o declarar falsos todos los registros no estadounidenses.

La conclusión prudente basta: casi la mitad de los registros estaba fuera del mercado estadounidense principal del proyecto. Sin otra señal, una coincidencia OUI global no podía considerarse igual de plausible.

### Más de 60.000 dispositivos se identificaron por su nombre

| Familia SSID del análisis original | Registros | Porcentaje | Qué indica el nombre |
|---|---:|---:|---|
| Contiene `ClickShare` | 50.278 | 34,3% | Hardware de presentación inalámbrica Barco |
| `SMARTGATE_*` | 6.099 | 4,2% | Familia de puerta de enlace o dispositivo tipo OBD |
| `DIRECT-*` | 3.801 | 2,6% | Dispositivos WiFi Direct, como impresoras, televisores y adaptadores |
| Nombre exacto `AndroidAP` | 314 | 0,2% | Puntos de acceso Android |
| Nombre exacto `Audi HUD` | 138 | 0,1% | WiFi de infoentretenimiento o pantalla frontal Audi |
| Nombre exacto `MAX-PRINTER` | 133 | 0,1% | Impresoras de oficina |
| `Flock ALPR [...]` | 30 | <0,1% | Veredicto de otro detector almacenado como SSID |
| **Total del análisis original** | **60.793** | **41,5%** | Identificable como otro hardware o salida de detector |

La documentación de soporte de Barco indica que el nombre de red predeterminado de una unidad base ClickShare es [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). Esto confirma directamente la familia del producto, sin adivinar por geografía o registro del proveedor.

El clasificador de producción sustituyó esos controles de nombre exacto por expresiones regulares que ignoran mayúsculas y minúsculas. Incluye ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER y etiquetas de salida de detectores. En las mismas 146.526 filas, identifica 629 variantes AndroidAP, 139 Audi HUD y 134 MAX-PRINTER. El repositorio actual informa de **61.110 registros `identified_other`**, un poco más que los 60.793 del análisis original.

### La señal confirmatoria era solo del 2,4%

Solo **3.502 filas** tenían un SSID auténtico con patrón Flock. Otras 24.964 no tenían SSID. Las restantes indicaban otro hardware o combinaban un OUI con un nombre sin clasificar.

Las 3.502 filas confirmadas contenían 161 variantes reales de SSID: 3.342 instancias del nombre simple `Flock`, 157 nombres de aprovisionamiento únicos `Flock-XXXXXX` o `FLOCK-XXXXXX` y otros tres nombres con `flock`. Un recuento anterior de 166 variantes en el README incluía cinco cadenas de anotación distintas `Flock ALPR [...]`. Esas cinco prueban la presencia del detector, no de la cámara.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="Barra apilada al 100% que divide 146.526 registros en 3.502 confirmados por SSID, 57.267 con nombre sin clasificar, 24.964 solo OUI ocultos, 60.763 identificados como otros y 30 registros de retroalimentación del detector" caption="El titular anterior redujo cinco clases de evidencia materialmente distintas a una sola cifra." >}}

### La calidad de los prefijos variaba mucho

La tasa de falsos positivos no era uniforme. Algunos prefijos conservaban una señal Flock útil. Otros estaban dominados por dispositivos de oficina o de consumo con nombre.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Barras apiladas horizontales de 31 prefijos OUI: SSID Flock en verde, SSID conocidos de otros dispositivos en rojo, SSID ocultos en gris claro y registros sin clasificar en gris oscuro" caption="Los prefijos más grandes solían contener más dispositivos conocidos como ajenos. Cifras de la instantánea de auditoría de 146.526 filas." >}}

Compara dos prefijos que el mapa anterior etiquetaba igual:

- `70:C9:4E` tenía 495 filas: 133 nombres con patrón Flock y 29 nombres conocidos de otros dispositivos.
- `74:4C:A1` tenía 11.872 filas: 211 nombres con patrón Flock y 8.385 nombres conocidos de otros dispositivos.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Comparación del prefijo 70 C9 4E con 26,9% de SSID Flock y 5,9% conocidos como otros frente al prefijo 74 4C A1 con 1,8% de SSID Flock y 70,6% conocidos como otros" caption="Una etiqueta uniforme ocultaba proporciones de señal y ruido opuestas." >}}

El patrón se repite en los registros más grandes: `F4:6A:DD` tenía 8.422 nombres conocidos como otros frente a 327 nombres Flock, `D0:39:57` tenía 8.270 frente a 473, y `E0:4F:43` incluía 6.238 nombres conocidos como otros frente a 66 nombres Flock. El volumen de un prefijo no demostraba la calidad de la evidencia.

______

## El bucle de retroalimentación oculto en 30 filas

Treinta registros de Texas tenían SSID que eran claramente la salida de otro detector:

| Etiqueta de detector guardada como SSID | Confianza escrita por la herramienta | Registros |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | baja | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | media | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | baja | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | baja | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | baja | 1 |

La herramienta que creó 26 de los 30 los marcó con confianza baja. Una carga en WiGLE guardó después el veredicto de la herramienta en el campo SSID. Nuestra canalización encontró la palabra `Flock` y podría haber tratado esa etiqueta como confirmación independiente.

Treinta filas son pocas estadísticamente. El mecanismo sí importa: las herramientas que comparten una base de datos colaborativa pueden ingerir resultados de las demás y convertir una conjetura de baja confianza en una aparente corroboración. La corrección excluye todo el patrón `Flock ALPR [` antes de buscar la subcadena confirmatoria `flock`.

______

## En qué nos equivocamos

El titular del README decía **«Cámaras mapeadas | 146.526»**. El mapa publicaba coordenadas de precisión completa y dibujaba cada resultado con el mismo marcador. Se actualizaba con una programación de GitHub Actions, lo que daba a una heurística débil el aspecto de un inventario mantenido.

Sí incluimos reservas. Cada elemento tenía `match_confidence: "suspected"`. El README mencionaba ClickShare como posible dispositivo coexistente y el proyecto mantenía una vía separada para candidatos descubiertos por SSID. Esas reservas no regían la cifra, el marcador ni la vista predeterminada que veían los lectores.

Escribimos reservas en el texto y afirmamos cifras en el titular. El mapa hizo la afirmación.

Lo más evitable es que el firmware de [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) ya separaba identificadores de alta confianza de los de fabricantes por contrato y puntuaba la evidencia débil por debajo del umbral de alerta. El concepto ya existía en la misma organización, pero la canalización del mapa no lo heredó.

Encontramos la magnitud del error al ejecutar un histograma de nuestra propia columna SSID. Tardamos minutos. Cada día publicábamos 146.526 filas de evidencia contra nuestra presentación.

______

## Qué cambiamos

La corrección está implementada en el modelo de datos y la interfaz de Flock Finder:

- **Evidencia por registro:** `ssid_confirmed`, `oui_high`, `oui_mfr` o `identified_other`.
- **Niveles OUI:** los prefijos se separan en alta confianza observada en campo y niveles compartidos de fabricantes por contrato.
- **Exclusión de otros dispositivos conocidos:** ClickShare, SmartGate, WiFi Direct, puntos de acceso Android, Audi HUD, MAX-PRINTER y SSID de salida de detectores quedan excluidos por defecto del mapa y del titular.
- **Incertidumbre visible:** los colores de marcador, ventanas emergentes, recuentos y filtros muestran la clase de evidencia.
- **Marca de mercado:** los registros fuera del mercado estadounidense principal llevan `out_of_market: true` y siguen disponibles para revisión.
- **Titular desglosado:** 3.502 confirmados por SSID, 73.691 sospechosos por OUI de nivel alto, 8.223 sospechosos por OUI de fabricantes por contrato y 61.110 identificados como otros.

La cifra corregida útil para actuar es **85.416**, y todavía incluye 81.914 coincidencias OUI no confirmadas. Es un recuento defendible de lo que supera las reglas actuales, no un inventario verificado de cámaras.

`identified_other` también es un clasificador operativo, no un oráculo. ClickShare cuenta con documentación primaria sólida sobre su SSID predeterminado, mientras que un patrón amplio como `DIRECT-` describe una convención de nombres WiFi Direct usada por muchas clases de productos. Publicar la regla coincidente y el campo `blocked_reason` permite a investigadores auditar esas exclusiones y revisarlas si mejora la evidencia.

### La respuesta a largo plazo es la huella del firmware

La clasificación por niveles OUI reduce daños, pero no convierte un prefijo compartido del fabricante en uno específico del producto. La vía más sólida es la estructura ordenada de los elementos de información de las solicitudes de sondeo 802.11. El trabajo anterior documenta esta firma TLV:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

La secuencia describe el comportamiento de una pila de firmware concreta, no la propiedad de un bloque MAC. La huella de solicitudes de sondeo es una técnica establecida para identificar dispositivos. [La investigación publicada sobre huellas de la capa MAC 802.11](https://doi.org/10.1155/2017/6235484) muestra que los elementos de información de sondeo pueden seguir identificando un dispositivo cuando rotan las MAC. También aborda el fallo concreto del [issue #43 de flock-you](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` aparece en MAC administradas localmente y secuenciales en las bandas de 2,4 y 5 GHz.

La firma aún necesita validación de campo independiente en distintos equipos y versiones de firmware, y las capturas malformadas requieren análisis defensivo. Aun así, es el camino correcto. La aleatorización MAC convierte la coincidencia basada solo en OUI en un callejón sin salida anunciado.

______

## Por qué importa más allá de un repositorio

La gente utiliza mapas de vigilancia para decidir por dónde conducir, dónde aparcar, qué denunciar, investigar y organizar. Un marcador falso desvía la atención. Decenas de miles pueden desacreditar las observaciones precisas que tienen al lado.

También existe una asimetría de credibilidad. Un proveedor o crítico solo necesita un marcador ClickShare demostrablemente falso para cuestionar todo el conjunto de datos. Nosotros aportamos 50.278. Los periodistas y grupos de defensa pueden repetir un titular sencillo más rápido de lo que llega una corrección posterior.

La transparencia de código abierto gana confianza con métodos inspeccionables e incertidumbre visible. Publicar datos sin procesar ayudó a descubrir nuestro error, pero el acceso a los datos no justificaba una interfaz que exageraba la conclusión. La corrección debe aparecer donde el lector encuentra la afirmación: campo, filtro, marcador, leyenda y titular.

### Una petición a todos los mapas de Flock y ALPR

Otros proyectos de mapeo de Flock y ALPR también deberían auditar sus conjuntos de datos. Esta es una invitación a comparar métodos, no una acusación de que todos heredaron nuestro error.

[WiGLE](https://www.wigle.net/stats/) es el conjunto de datos de observaciones WiFi de acceso público y búsqueda global más amplio que conocemos. Ese alcance hizo atractivo Flock Finder: una API podía convertir una lista de firmas investigada en campo en un mapa mundial. También hizo que el error fuera lo bastante grande como para medirlo. Una base global devuelve todos los productos ajenos que comparten el espacio de direcciones de un proveedor de radio, no solo el producto que motivó la búsqueda.

Otros mapas utilizan pruebas distintas. Algunos se basan en fotos y observaciones voluntarias de campo. Otros importan etiquetas de vigilancia de OpenStreetMap, registros públicos, divulgaciones de proveedores o datos de otro proyecto comunitario. Sus totales no son comparables directamente con nuestros resultados de WiGLE, y la tasa de 2,4% confirmada por SSID no debe proyectarse sobre datos verificados en campo. El riesgo común es que la clasificación de un proyecto llegue a los datos fuente de otro y luego parezca una corroboración independiente.

Todo mapa público debería responder una auditoría breve:

1. **¿Qué significa un marcador?** ¿Un dispositivo fotografiado, un registro gubernamental, una coincidencia OUI, un informe de usuario o una importación de otro mapa?
2. **¿Cuántos registros tienen pruebas directas del producto?** Publica recuentos por clase de evidencia en vez de un único total de cámaras.
3. **¿Qué fuentes son independientes?** Sigue la procedencia de las importaciones para evitar contar una observación varias veces como confirmación.
4. **¿Qué contradice la clasificación?** Genera tablas de frecuencia de SSID, proveedores, países, etiquetas de colaboradores y otros campos categóricos.
5. **¿Cómo se muestran la incertidumbre y las disputas?** Incluye confianza y estado de corrección en marcadores, filtros, exportaciones y titulares.
6. **¿Puede otro investigador reproducir el recuento?** Publica la consulta, la instantánea de origen, las reglas de clasificación y la fecha.

Esta auditoría no reduce el problema de Flock. Una red de cámaras ALPR aún puede registrar desplazamientos, permitir búsquedas entre jurisdicciones y afectar a personas que nunca consintieron la recopilación. Los recuentos precisos hacen más difícil descartar esa crítica. Si cuestionamos los sistemas de vigilancia, nuestros mapas deben distinguir lo observado, lo inferido y lo confirmado.

Cometimos un error bien informado. Los prefijos procedían de investigación de campo legítima, la canalización era reproducible y las reservas eran reales. Aun así, la inferencia excedió las pruebas. Las buenas intenciones y las buenas entradas no eliminan la obligación de probar lo que produce un sistema a escala.

______

## Reproduce la auditoría

Obtén el commit `5551829` y ejecuta lo siguiente desde la raíz del repositorio. Usa solo la biblioteca estándar de Python e imprime el total, la geografía, los SSID frecuentes y algunas familias de dispositivos identificadas por nombre.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("filas", len(rows))
print("EE. UU.", countries["US"])
print("fuera de EE. UU.", sum(countries.values()) - countries["US"] - countries[""])
print("país ausente", countries[""])
print("SSID principales", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Para obtener la entrada histórica exacta, usa el CSV de ese commit, no un conjunto de datos generado actual. Tras la auditoría, el proyecto dejó de incluir en Git el CSV grande, el GeoJSON y los archivos por OUI, porque cada escaneo reescribía cientos de megabytes y había hecho crecer mucho el repositorio. Los datos generados actuales se restauran y publican en la versión continua [`data-latest`](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest). El pequeño resumen `scan_stats.json` sigue en Git. Por tanto, que falte un archivo generado en la rama actual no significa que se borraran las pruebas históricas ni que su recuento sea cero.

______

## La lección

**Una heurística marcada como «sospechada» en metadatos pero mostrada como marcador seguro en el mapa es una afirmación.** La etiqueta debe estar en el modelo de datos y la visualización, no solo en la documentación.

