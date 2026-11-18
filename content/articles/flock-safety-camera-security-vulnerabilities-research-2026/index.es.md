---
title: "Vulnerabilidades en las cámaras de Flock Safety: más de 50 fallos descubiertos"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Esta investigación sobre vulnerabilidades de las cámaras Flock Safety analiza credenciales expuestas, protecciones débiles, acceso físico y límites de divulgación."
genre: ["Investigación de seguridad", "Análisis de vulnerabilidades", "Tecnología de vigilancia", "Ciberseguridad", "Privacidad y seguridad", "Seguridad de IoT", "Seguridad física", "Seguridad de redes", "Infraestructura crítica", "Tecnología gubernamental"]
tags: ["Vulnerabilidades de Flock Safety", "Seguridad ALPR", "Hackeo de cámaras", "Fallos de seguridad en IoT", "Contraseñas codificadas", "Vulnerabilidades de Android Things", "Explotación por acceso físico", "Seguridad de redes", "Fallos de cifrado", "Violaciones de privacidad de datos", "Divulgaciones de CVE", "Investigación de seguridad", "Investigación de GainSec", "Investigación de Ben Jordan", "Seguridad de cámaras de vigilancia", "Fallos de tecnología gubernamental", "Vulnerabilidades críticas", "Divulgación responsable", "Análisis de ciberseguridad", "Tecnología de las fuerzas del orden", "Seguridad pública", "Punto de acceso inalámbrico", "Elusión de autenticación", "Credenciales en texto claro", "Fuga de RF", "Ataque Tempest", "Divulgación de información", "Acceso a shell root", "Ejecución remota de código", "Auditoría de seguridad", "Evaluación de vulnerabilidades", "Riesgo para la seguridad nacional", "Investigación del Senado", "Programa de recompensas por errores", "Vulnerabilidad zero-day", "Desarrollo de exploits", "Pruebas de penetración", "Libro blanco de seguridad", "Cobertura de 404 Media", "Investigación independiente", "Seguridad de hardware", "Análisis de firmware", "Explotación de sistemas"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "Una cámara de vigilancia de alta tecnología aparece con reflejos azules y verdes sobre un fondo oscuro. Formas y líneas abstractas la rodean para representar vulnerabilidades de seguridad digital."
coverCaption: "Fallos críticos de seguridad exponen más de 80.000 cámaras de vigilancia al acceso no autorizado"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Más de 50 vulnerabilidades críticas exponen la red privada de vigilancia más grande del país**

## Introducción: una crisis de seguridad nacional

A finales de 2024 y durante todo 2025, investigadores independientes de seguridad descubrieron lo que podría ser **el fallo de seguridad más importante de la historia de la tecnología de vigilancia de las fuerzas del orden en Estados Unidos**. Se han descubierto más de **50 vulnerabilidades críticas** en los sistemas de cámaras de Flock Safety. Estas cámaras fotografían y rastrean más de **150 millones de vehículos al día** en más de **80.000 implementaciones** en todo el país.

Este artículo ofrece un análisis técnico completo de las vulnerabilidades, basado en:
- **El libro blanco formal de GainSec**, «Examining the Security Posture of an Anti-Crime Ecosystem» (51 hallazgos, 22 CVE asignados, 8 pendientes)
- **El periodismo de investigación de Ben Jordan** y sus pruebas prácticas de seguridad
- **Los reportajes de 404 Media** sobre transmisiones de cámaras expuestas al público
- **Las respuestas oficiales** de Flock Safety y senadores estadounidenses
- Las divulgaciones publicadas en la **National Vulnerability Database** (NVD)
- **La imagen del sistema de archivos de septiembre de 2026**, publicada por Distributed Denial of Secrets, con un análisis técnico detallado de Micah Lee y una investigación conjunta de WIRED y 404 Media

Para conocer **por qué existen estas cámaras** y sus **implicaciones para la privacidad**, consulta nuestro artículo: **[Vigilancia con cámaras Flock Safety: prevalencia, riesgos para la privacidad y estrategias de protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Para obtener información sobre **cómo detectar estas cámaras**, consulta: **[Proyecto de detección Flock-You: guía de hardware contra la vigilancia](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## El alcance del problema

### Escala de la infraestructura vulnerable

En mayo de 2026:
- **Más de 80.000 cámaras Flock Safety** desplegadas en Estados Unidos
- **Más de 5.000 ciudades y pueblos** usan los servicios de Flock
- **Más de 3.500 agencias de las fuerzas del orden** tienen acceso al sistema
- **Más de 22.000 usuarios de las fuerzas del orden** consultan bases de datos
- **Miles de millones de puntos de datos** almacenados en bases de datos consultables

### Cronología de vulnerabilidades

- **Finales de 2024**: el investigador de seguridad Jon «GainSec» Gaines descubre las primeras vulnerabilidades
- **Febrero de 2025**: comienza la divulgación responsable a Flock Safety
- **Abril de 2025**: se publican las primeras asignaciones de CVE
- **Noviembre de 2025**: se publica el libro blanco formal con 51 hallazgos
- **Diciembre de 2025**: Ben Jordan demuestra vulnerabilidades en un video
- **Enero de 2026**: 404 Media descubre más de 60 transmisiones de cámaras accesibles públicamente
- **Febrero de 2026**: senadores estadounidenses solicitan una investigación de la FTC
- **Mayo de 2026**: continúa el proceso de divulgación

### Categorías de vulnerabilidad

Las más de 50 vulnerabilidades abarcan varias categorías:
1. **Autenticación y autorización** (contraseñas codificadas, falta de autenticación multifactor)
2. **Criptografía y cifrado** (datos sin cifrar en reposo y en tránsito)
3. **Seguridad de redes** (puntos de acceso Wi-Fi expuestos, credenciales en texto claro)
4. **Seguridad física** (exploits mediante pulsación de botones, puertos USB expuestos)
5. **Privacidad de datos** (recopilación no autorizada, retención prolongada)
6. **Diseño del sistema** (software obsoleto, controles de acceso insuficientes)
7. **Divulgación de información** (claves API expuestas, transmisiones públicas de cámaras)

______

## La imagen del sistema de archivos de septiembre de 2026

**En septiembre de 2026, la organización sin ánimo de lucro Distributed Denial of Secrets, dedicada a la transparencia, publicó imágenes completas del sistema de archivos de una cámara Flock en servicio.** Un colectivo que se hace llamar **stegan0gram** desmontó el hardware del poste, copió el almacenamiento interno y publicó las imágenes. **404 Media** y **WIRED** realizaron una investigación conjunta, y el investigador de seguridad **Micah Lee** publicó un análisis técnico detallado del contenido.

Todos los hallazgos anteriores de este artículo procedían de un dispositivo de laboratorio de un investigador o de una unidad comprada. Estos datos provienen de una cámara en servicio municipal, por lo que constituyen la prueba más sólida publicada hasta la fecha.

*La cámara no fue vulnerada a través de la red. La retiraron físicamente.*

### Contenido de la imagen

La publicación incluye tres imágenes de particiones, y cada una revela una parte distinta del problema.

| Partición | Tamaño | Importancia |
|-----------|--------|------------|
| **system** | 1,5 GB | Imagen del sistema Android con **19 aplicaciones creadas por Flock**, entre ellas `flock-sambuca`, `flock-collins` y `flock-phone-home` |
| **persist** | 32 MB | Credenciales del dispositivo en `flock/auth0/auth0_cred`, en una **partición sin cifrar diseñada para sobrevivir a un restablecimiento de fábrica** |
| **media** | 18 GB | Registros e imágenes dentro de un contenedor cuya **clave de descifrado se almacena en la misma partición** |

### Confirmación del problema de las credenciales

La imagen permite determinar si las credenciales codificadas son teóricas o se han desplegado. Se han desplegado.

**Una clave API que permite acceder al backend de Flock está codificada en los binarios de las aplicaciones.** El valor se encuentra en una clase llamada `CameraSettings` dentro de `com.flocksafety.android.common.lib`. Flock incluye la biblioteca compartida en sus 19 aplicaciones, por lo que todas llevan la clave. La aplicación `flock-sambuca` la usa durante el aprovisionamiento.

**El flujo de autenticación funciona así:**

1. Cada cámara solicita credenciales a un servidor de Flock y se identifica mediante su **dirección MAC**
2. El servicio de inicio de sesión **Okta Auth0** de Flock devuelve un `FlockAuth0Token` de corta duración
3. La cámara almacena las credenciales recibidas **en texto claro**

El ID y el secreto del cliente Auth0 están en la **partición `/persist` sin cifrar**, en un archivo diseñado para sobrevivir a un restablecimiento de fábrica. Un atacante recupera primero la partición persist, porque nada la protege.

La [vulnerabilidad crítica n.º 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system) abarca el patrón general de secretos codificados en toda la plataforma.

### La clave de cifrado viene con el candado

Flock afirma que sus cámaras están protegidas mediante **cifrado en el dispositivo**. La imagen revela cómo se implementa en la práctica.

La partición media de 18 GB está dentro de un contenedor cifrado. La clave de descifrado está en la misma partición, en un archivo cuyo nombre termina en `.key`. El colectivo stegan0gram recuperó la clave, desbloqueó el contenedor y leyó su contenido. **Las imágenes están cifradas como lo está una caja cerrada cuya llave está pegada a la tapa.**

Los registros recuperados también revelaron la ubicación de la propia cámara. Las coordenadas GPS aparecen **155 veces** en los registros, agrupadas en un radio de unos 100 metros, la deriva habitual de un receptor fijado a un poste. Las coordenadas señalan **Wauwatosa, Wisconsin**, un suburbio de Milwaukee donde la cámara estaba instalada en N Mayfair Road. Micah Lee comparó los registros con Google Street View e identificó la unidad concreta por su número de serie y dirección MAC.

*El cifrado en reposo no sirve si la clave se guarda junto al texto cifrado.*

### La respuesta de Flock

La respuesta de Flock reiteró su postura frente a los hallazgos anteriores de GainSec. Un portavoz declaró:

> «Flock se toma la seguridad en serio y mantiene una política pública de divulgación de vulnerabilidades para que los investigadores nos comuniquen directamente los posibles fallos. No recibimos ninguna notificación mediante ese proceso y, dada la escasa información proporcionada, no tenemos suficientes detalles para evaluar las afirmaciones.»

Esta respuesta no encaja con la cronología. Las vulnerabilidades del sistema operativo de la cámara se corrigieron públicamente en **2018 y 2021**, y las normas para almacenar credenciales y gestionar claves no han cambiado desde mucho antes de que se enviara la cámara. **Revisar una década de historial público de vulnerabilidades no requiere un informe externo.**

Flock también calificó de ilegal la retirada y el análisis de la cámara, como lo son según la legislación vigente. Los hallazgos de seguridad siguen siendo válidos independientemente de cómo se obtuvo el hardware.

### Por qué esto importa más que las investigaciones anteriores

El libro blanco de GainSec documentó 51 hallazgos sobre dispositivos obtenidos legalmente. Flock cuestionó su gravedad y sostuvo que se requería proximidad física.

Esta imagen elimina esas reservas. El estado predeterminado de una cámara de producción, sin modificaciones de sus operadores, incluye credenciales de infraestructura en texto claro, claves almacenadas junto a los datos que protegen y un sistema operativo sin ocho años de actualizaciones de seguridad. **No hizo falta ningún exploit. Bastó una llave inglesa.**

______

## La flota de dispositivos

Flock vende una línea de productos, no una sola cámara, y las propiedades de seguridad varían según el dispositivo. Las especificaciones siguientes proceden de los desmontajes de GainSec y del análisis de firmware recopilado por la comunidad de detección en **[WiFi Mothership](https://wifimothership.com/flock)**.

| Dispositivo | Función | Plataforma | Sistema operativo |
|--------|------|----------|-----|
| **Falcon** | Cámara ALPR con energía solar | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Cámara ALPR con alimentación por cable | Igual que Falcon | Android 8.1 |
| **Raven** | Detección de disparos y llamadas de auxilio mediante audio | ESP32-WROOM-32D con DSP Syntiant NDP120-B0 | FreeRTOS / ESP-IDF |
| **Bravo** | Equipo informático de IA en el borde | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, kernel 5.4.180** |
| **Picard** | Equipo informático heredado | Retirado en favor de Bravo | |
| **Condor** | Cámara PTZ | Documentación incompleta | |
| **Alpha** | Dron autónomo | Diseñado por Flock, compatible con NDAA | Piloto automático propietario |
| **Aerodome M350** | Dron heredado | DJI Matrice M350 / M300 RTK | Firmware DJI |
| **Remolque LPR (ATS-5)** | Plataforma ALPR móvil | Chasis de All Traffic Solutions con cámara Flock | Igual que Falcon |
| **Wing** | Puente de software para cámaras de terceros | Ninguna, envuelve cámaras IP existentes | |

*La diferencia entre generaciones es lo primero que destaca. El equipo informático funciona con Android 13 mientras las cámaras que atiende usan Android 8.1, un sistema operativo publicado en 2017.*

**Falcon es el dispositivo que conviene vigilar.** Ejecuta la carga de trabajo ALPR, sigue con Android 8.1 y almacena datos en **una memoria eMMC de 32 GB sin cifrar**. El colectivo stegan0gram encontró en esa misma memoria los archivos multimedia y registros recuperados. Sparrow usa la misma plataforma con alimentación por cable.

**Bravo representa el caso opuesto.** El equipo informático moderno, con Android 13 e inferencia de IA para las transmisiones de las cámaras, demuestra que la empresa está dispuesta a distribuir software actualizado cuando así lo decide.

## Identificadores CVE verificados

Se han asignado quince CVE a las familias Falcon, Sparrow, Raven y Bravo. Cada identificador se verificó en su **registro de CVE.org** en septiembre de 2026, en lugar de copiarlo de una fuente secundaria.

### Dispositivos de detección de disparos y audio

| CVE | Hallazgo | CVSS |
|-----|---------|------|
| **CVE-2025-47818** | Contraseña de conexión codificada | 2.2 |
| **CVE-2025-47819** | Interfaz de depuración en chip con control de acceso inadecuado | 6.4 |
| **CVE-2025-47820** | Almacenamiento de código en texto claro | 2.0 |
| **CVE-2025-47821** | Contraseña del sistema codificada | 2.2 |

Los cuatro afectan a los dispositivos de detección de disparos **anteriores a la versión 1.3**.

### Lectores de matrículas

| CVE | Hallazgo | CVSS |
|-----|---------|------|
| **CVE-2025-47822** | Interfaz de depuración en chip con control de acceso inadecuado | 6.4 |
| **CVE-2025-47823** | Contraseña del sistema codificada | 2.2 |
| **CVE-2025-47824** | Almacenamiento de código en texto claro | 2.0 |

Estos tres afectan al firmware de lectores de matrículas **hasta la versión 2.2 incluida**.

### Fallos de aplicaciones en toda la flota

| CVE | Hallazgo | CVSS |
|-----|---------|------|
| **CVE-2025-59403** | La aplicación Collins expone endpoints administrativos en el **puerto 8080 sin autenticación**: `/reboot`, `/logs`, `/crashpack` y `/adb/enable`. El último inicia ADB por TCP sin confirmación de depuración, lo que concede un shell a un atacante en la misma red | **9.8 CRÍTICO** |
| **CVE-2025-59407** | La aplicación DetectionProcessing incluye un almacén de claves Java junto con su **contraseña codificada**, y el almacén contiene una clave privada | **9.8 CRÍTICO** |
| **CVE-2025-59405** | La aplicación Peripheral contiene una clave API de DataDog en texto claro | 7.5 |
| **CVE-2025-59409** | El firmware de producción de Falcon y Sparrow se distribuye con **credenciales de Wi-Fi de desarrollo en texto claro** | 7.5 |
| **CVE-2025-59406** | La aplicación Pisco contiene un **secreto de cliente Auth0** en texto claro | 6.2 |

### Equipo informático Bravo

| CVE | Hallazgo | CVSS |
|-----|---------|------|
| **CVE-2025-59402** | Acepta el cargador Firehose predeterminado de Thundercomm TurboX 6490, lo que permite flashear firmware y volcar particiones | 5.4 |
| **CVE-2025-59404** | Se distribuye con el cargador de arranque desbloqueado, lo que elude Android Verified Boot | 7.5 |
| **CVE-2025-59408** | Se distribuye con Secure Boot desactivado | 7.3 |

**Cuatro de estos fallos tienen un vector de ataque por red con una puntuación de 7,5 o superior, por lo que ninguno requiere acceso físico.** CVE-2025-59403 identifica la ruta de API sin autenticación e incluye la llamada `/adb/enable`, que utiliza la [vulnerabilidad crítica n.º 1](#critical-vulnerability-1-button-press-wireless-access-point) para obtener un shell root.

*Los registros de CVE importan por otra razón. Confirman el problema de los secretos en texto claro mediante registros independientes de los informes de investigadores, y la página de alertas de seguridad de Flock figura como referencia en las entradas de Raven y LPR.*

______

## Vulnerabilidad crítica n.º 1: punto de acceso inalámbrico activado con un botón {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Gravedad**: CRÍTICA (CVSS 9.8)

### El exploit

La vulnerabilidad más alarmante permite que **cualquier persona con acceso físico** a una cámara Flock Safety tome el control completo en menos de 60 segundos:

**Paso 1**: pulsar **tres veces** el botón situado en la parte posterior de la cámara Falcon/Sparrow
**Paso 2**: el dispositivo crea un punto de acceso Wi-Fi abierto
**Paso 3**: conectarse a la red Wi-Fi (contraseña codificada: documentada en el libro blanco de GainSec)
**Paso 4**: enviar el comando para activar ADB (Android Debug Bridge)
**Paso 5**: conectarse por ADB y obtener acceso a un shell root
### Detalles técnicos

```
Dispositivo: cámara ALPR Flock Safety Falcon/Sparrow
Hardware: Android Things 8.0/8.1 (fin del soporte en 2021)
Vector de ataque: secuencia de pulsaciones físicas del botón
Autenticación: contraseña WiFi codificada (la misma en todos los dispositivos)
Impacto: control total del dispositivo, extracción de datos e instalación de malware
```

### Qué permite

Una vez obtenido el acceso al shell, un atacante puede:
- **Extraer todas las imágenes almacenadas** (incluidas las de personas, no solo vehículos)
- **Modificar o eliminar pruebas** almacenadas en el dispositivo
- **Instalar malware persistente** (sobrevive a los reinicios)
- **Clonar la identidad del dispositivo** para suplantarlo
- **Interceptar y modificar** las transmisiones de video
- **Usar el dispositivo como cliente de una botnet** para ataques DDoS
- **Capturar credenciales Wi-Fi** de dispositivos cercanos (ataques de punto de acceso señuelo)
- **Desactivar la cámara** o causar una denegación de servicio

### Demostración

El investigador de seguridad Ben Jordan demostró este exploit en YouTube y mostró:
- Conexión al punto de acceso Wi-Fi en **menos de 30 segundos**
- Obtención de acceso a un shell root en **menos de 60 segundos en total**
- Acceso completo al sistema de archivos, las imágenes almacenadas y la memoria del sistema
- Capacidad para instalar cualquier aplicación Android

**Cita de la demostración**:
> «La contraseña de ese punto de acceso es [REDACTED], toda en minúsculas. Todas las cámaras que hemos probado tienen esa misma contraseña codificada. Después solo hay que enviarle un comando para activar ADB... en menos de 30 segundos se puede abrir un shell completo en el dispositivo y acceder a todo.»

### Respuesta del proveedor

Flock Safety afirmó inicialmente que la vulnerabilidad solo afectaba a **dispositivos no conectados a la nube**, comparándolos con **«un iPhone robado de un camión antes de conectarlo»**.

*La afirmación fue refutada.* Los investigadores reprodujeron la vulnerabilidad **en dispositivos conectados a la nube**, en varios modelos de cámara con una **vulnerabilidad idéntica** y en dispositivos adquiridos de **distintas fuentes**. Todos presentaban el fallo.

______

## Vulnerabilidad crítica n.º 2: sistema operativo Android obsoleto

### CVE-2025-47822 a CVE-2025-47824

**Gravedad**: MEDIA a BAJA (CVSS 6.4, 2.2 y 2.0)

### El problema

Las cámaras de Flock Safety ejecutan **Android Things 8.0 u 8.1**, que:
- Google **descontinuó en 2021**
- **NO recibe actualizaciones de seguridad desde 2021**
- Tiene **más de 900 vulnerabilidades publicadas** en 2026
- Lleva **más de cinco años sin soporte**

### Análisis técnico

**Sistema operativo**: Android Things 8.0/8.1  
**Fin de vida útil**: enero de 2021  
**Vulnerabilidades conocidas**: más de 900  
**Parches de seguridad**: ninguno desde el fin de vida útil  
**Dispositivos afectados**: Falcon, Sparrow, Condor y equipos informáticos Bravo

### Qué muestra la imagen de septiembre de 2026

Las imágenes del sistema de archivos publicadas en septiembre de 2026 indican las versiones exactas de una cámara en servicio, no de una unidad de laboratorio.

| Componente | Versión en la cámara | Estado |
|-----------|----------------------|--------|
| **Android** | 8.1, compilación fechada el 5 de junio de 2025 | Nivel del parche de seguridad **2018-06-05** |
| **Kernel de Linux** | 3.18.71 | Publicado en 2017. La serie 3.18 terminó con la versión 3.18.140 en mayo de 2019 |
| **Versión actual de Android** | Android 17, junio de 2026 | Nueve versiones principales más reciente |

La compilación de la cámara es reciente. **El sistema operativo subyacente no lo es**, y el nivel del parche indica que el dispositivo no ha recibido actualizaciones de seguridad de Android en **ocho años**. El kernel tiene **69 revisiones de parche de retraso** incluso respecto al fin de su propia rama de mantenimiento, más de nueve años de correcciones pendientes.

### Dos vulnerabilidades presentes en esta compilación

Micah Lee identificó dos fallos conocidos públicamente que afectan a componentes incluidos en la cámara. Las fechas de los parches prueban que el dispositivo es anterior a ambas correcciones.

| CVE | Componente | Efecto | Fecha del parche |
|-----|-----------|--------|---------|
| **CVE-2021-1905** | Controlador de GPU Qualcomm Adreno | Use-after-free que permite que **cualquier código del dispositivo, incluidas aplicaciones sin privilegios, corrompa la memoria del kernel y tome el control completo** | Mayo de 2021 |
| **CVE-2018-9568** «WrongZone» | Gestión de sockets del kernel de Linux | Confusión de tipos por IPv6 que permite que un programa **escalе a root**. Hay código de exploit público | Diciembre de 2018 |

Ambos fallos se corrigieron años antes de compilar el firmware de esta cámara. **Ninguno depende del acceso físico, porque se puede llegar a ambos desde software que ya se ejecuta en el dispositivo.** La salvedad de proximidad que Flock usó para restar importancia a los hallazgos de GainSec no se aplica a ninguno.

### Comparación con dispositivos de consumo

Como referencia:
- Tu **teléfono inteligente** deja de recibir actualizaciones tras unos cinco años y los fabricantes **dejan de venderlo**
- Una **cámara de seguridad doméstica** con software de hace cinco años se consideraría **críticamente insegura**
- Las agencias gubernamentales exigen **software actualizado y con soporte** para los sistemas sensibles

*Sin embargo, Flock Safety sigue desplegando y vendiendo cámaras con software sin soporte del proveedor, sin parches de seguridad, con cientos de exploits conocidos y que procesa datos sensibles de las fuerzas del orden.*

### Por qué importa

Ejecutar **software sin soporte** en dispositivos de vigilancia significa que:
- **Cualquier vulnerabilidad publicada de Android 8.x** funciona en estas cámaras
- Hay **código de exploit disponible públicamente** para muchos fallos
- **Ningún parche corregirá** los nuevos problemas que se descubran
- El **cumplimiento normativo** (FISMA, NIST, CMMC) es imposible

______

## Vulnerabilidad crítica n.º 3: falta de cifrado durante la ejecución

### CVE-2025-47824 y CVE-2025-59407

**Gravedad**: ALTA a CRÍTICA (CVSS 2.0 a 9.8)

### Afirmaciones de Flock Safety frente a la realidad

**El sitio web de Flock Safety afirma**:
> «Los datos y las grabaciones están cifrados durante todo su ciclo de vida».

**Hallazgos de la investigación independiente de GainSec y Ben Jordan**:
> «En toda nuestra investigación no hemos descifrado ni vulnerado nada. Todo estaba sin cifrar durante la ejecución».

*La diferencia entre la afirmación comercial y la realidad técnica es total.*

### Datos que no están cifrados

Al examinar los dispositivos, los investigadores encontraron **sin cifrar**:
1. **Videos e imágenes almacenados**
2. **Datos de matrículas y metadatos**
3. **Credenciales Wi-Fi y claves API**
4. **Archivos de bases de datos con registros de detección**
5. **Tráfico de red** (consulta la vulnerabilidad n.º 6)
6. **Registros del sistema con información sensible**

### Contradicción sobre la retención de datos

**Afirmación de Flock Safety**: los datos se eliminan automáticamente después de siete días.  
**Hallazgo de la investigación**: se encontraron imágenes que databan de la **fabricación del dispositivo** (meses o años antes).

Extracto del libro blanco de GainSec:
> «Encontramos imágenes de hace más de siete días. De hecho, algunas imágenes almacenadas se capturaron cuando la cámara se activó en la fábrica donde se fabricó el dispositivo».

*Esto significa que las políticas de privacidad declaradas no se aplican en el dispositivo.*

### Implicaciones para la privacidad

Este fallo del cifrado implica que:
- **El robo físico del dispositivo** causa una filtración de datos inmediata
- **La interceptación de la red** expone datos en texto claro
- Las **amenazas internas** pueden exfiltrar datos con facilidad
- Es posible que las **protecciones de las órdenes judiciales** no se apliquen a datos sin cifrar
- Se producen **incumplimientos de numerosas normativas** (HIPAA, CCPA, etc.)

______

## Vulnerabilidad crítica n.º 4: credenciales codificadas en todo el sistema {#critical-vulnerability-4-hardcoded-credentials-throughout-system}

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 y CVE-2025-59409

**Gravedad**: CRÍTICA (CVSS 9.8, el valor máximo)

### Categorías de secretos codificados

Los investigadores de seguridad descubrieron **numerosas credenciales codificadas**:

#### 1. Contraseñas de puntos de acceso Wi-Fi
- **Contraseña universal** en todas las cámaras Falcon/Sparrow
- Los usuarios y administradores **no pueden cambiarla**
- **Los investigadores la conocen** y se publicó en el libro blanco (secciones redactadas)
- **Confirmado por CVE-2025-59409**: el firmware de producción de Falcon y Sparrow (compilación `OPM1.171019.026`) se distribuye con **credenciales Wi-Fi de desarrollo en texto claro**

#### 2. Claves API y tokens
- **Codificados en el firmware** y el código de las aplicaciones
- **Permiten acceder al backend** de varios servicios
- **Encontrados mediante ingeniería inversa** de APK de Android
- **Confirmado por la imagen de septiembre de 2026**: una clave API del backend está codificada en `CameraSettings`, dentro de `com.flocksafety.android.common.lib`, una biblioteca compartida incluida en **las 19 aplicaciones Flock** del dispositivo
- El **ID y el secreto del cliente Auth0 se almacenan en la partición `/persist` sin cifrar**, en `flock/auth0/auth0_cred`, una ubicación diseñada para sobrevivir a un restablecimiento de fábrica
- Las **credenciales devueltas se almacenan en texto claro** después de que la cámara se autentica con el servicio Okta Auth0 de Flock mediante su propia dirección MAC

#### 3. Credenciales de bases de datos
- **Bases SQLite** sin protección por contraseña
- Credenciales de **MySQL/PostgreSQL** en archivos de configuración
- **Acceso directo a bases de datos** desde el shell local

#### 4. Almacenes criptográficos de claves
- **Confirmado por CVE-2025-59407**: la aplicación DetectionProcessing incluye un almacén de claves Java junto con su contraseña codificada, y el almacén contiene una **clave privada**
- **Gravedad**: CRÍTICA (CVSS 9.8), porque el material de la clave se distribuye junto al binario que debería protegerlo

#### 5. Nombres de redes Wi-Fi
- La lista de **redes preferidas** está codificada en el firmware
- Permite ataques mediante **puntos de acceso maliciosos** (consulta la vulnerabilidad n.º 6)

#### 6. Credenciales de servicios en la nube
- Tokens de **AWS/Azure** incluidos en el código
- **Claves API de terceros** (ArcGIS, servicios de mapas)
- Tokens **OAuth que nunca se rotan**

### Escenario de ataque: red maliciosa

Mediante los nombres de redes Wi-Fi codificados, los investigadores demostraron lo siguiente:

1. El atacante configura una **red Wi-Fi falsa** con un SSID igual al codificado
2. La cámara **se conecta automáticamente** (da prioridad a las redes codificadas)
3. El atacante captura **todo el tráfico de red** mediante un ataque de intermediario
4. Extrae las credenciales en texto claro del tráfico
5. Obtiene **acceso al sistema backend**

**No hace falta acceso físico a la cámara.** Basta con estar dentro del alcance de la red Wi-Fi.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Diagrama de cinco vectores de ataque con credenciales codificadas en cámaras Flock Safety, incluidas contraseñas Wi-Fi, claves API, credenciales de bases de datos y tokens de servicios en la nube" >}}

______

## Vulnerabilidad crítica n.º 5: falta de autenticación multifactor

### Fallo de las políticas organizativas

**Gravedad**: ALTA (organizativa)

### La revelación

**Flock Safety no exige 2FA/MFA** a algunas agencias de las fuerzas del orden, *las mismas que acceden a datos de seguimiento de 150 millones de vehículos al día*.

Cita de un investigador de seguridad:
> «Cuando me enteré, sencillamente no me lo podía creer. El proceso de seguridad para iniciar sesión en Disney Plus parece demasiado complicado para algunos departamentos de policía cuando acceden a información confidencial y a la ubicación, en algunos casos, de prácticamente todo el mundo».

### Por qué importa

Sin MFA/2FA:
- **Una sola contraseña comprometida** permite acceder a todo el sistema
- Los **ataques de phishing** son muy eficaces
- Funciona el **relleno de credenciales** con datos de otras filtraciones
- Las **amenazas internas** son más fáciles de ejecutar
- Los **dispositivos robados** conceden acceso inmediato

### Comparación

Requisitos de seguridad para sistemas **menos sensibles**:
- **Disney+**: ofrece 2FA
- **Gmail**: 2FA está activada de forma predeterminada en las cuentas nuevas
- **Servicios bancarios**: la ley exige 2FA
- **Redes sociales**: 2FA es habitual

Requisitos de seguridad para el **seguimiento diario de más de 150 millones de vehículos**:
- **Flock Safety**: 2FA es opcional (algunas agencias no la usan)

### Respuesta de un senador estadounidense

Este hallazgo se destacó específicamente en **la carta del senador Wyden** en la que solicitó una investigación de la FTC. Lo citó como prueba de que Flock Safety:
> «expuso innecesariamente los datos personales sensibles de los estadounidenses al robo por parte de hackers y espías extranjeros».

### Solución sencilla

Las **llaves de seguridad USB/NFC** cuestan **entre 10 y 25 dólares** y ofrecen:
- Autenticación **resistente al phishing**
- **No requieren aplicaciones ni códigos** adicionales
- Cumplimiento del estándar **FIDO2/WebAuthn**
- Una **experiencia de uso sencilla** (conectar la llave o acercar el dispositivo)

*Si esto representa «demasiadas molestias» para el personal de las fuerzas del orden, **no debería tener acceso** a sistemas nacionales de vigilancia.*

______

## Vulnerabilidad crítica n.º 6: tráfico de red en texto claro

### Identificador pendiente

**Gravedad**: ALTA (estimación de los investigadores: CVSS 7.8)

**Esta categoría no tiene un identificador CVE asignado.** El registro asignado más cercano, CVE-2025-59406, lleva la clasificación CWE-319 de transmisión en texto claro, pero se refiere a un secreto Auth0 integrado, no a la interceptación durante el tránsito. Los hallazgos de esta sección siguen basándose en los informes de investigación citados anteriormente.

### La vulnerabilidad

Al conectarse a redes (LTE o Wi-Fi), las cámaras transmiten datos **sin cifrado adecuado**:

**Tráfico afectado**:
- Imágenes y texto de matrículas
- Metadatos de detección
- Registros del sistema
- Datos de configuración
- Credenciales (en algunos casos)

### Vector de ataque n.º 1: red Wi-Fi maliciosa

Los investigadores demostraron lo siguiente:
1. Retirar la tarjeta SIM de la cámara **O** crear una red falsa con el SSID codificado
2. La cámara se conecta a la red Wi-Fi maliciosa
3. Capturar el tráfico con **Wireshark** o un analizador de paquetes similar
4. Analizarlo con herramientas como **NetworkMiner** o **Unblo**
5. Extraer **credenciales en texto claro** y datos sensibles

Cita de la investigación de GainSec:
> «Capturé durante un rato los paquetes que transmitía una de estas cámaras y los analicé con Wireshark y Unblo... y, efectivamente, los datos contenían credenciales en texto claro».

### Vector de ataque n.º 2: IMSI catcher / Stingray

Un ataque más sofisticado no requiere proximidad física:
1. Usar un **IMSI catcher** (dispositivo Stingray casero) o un SDR profesional
2. **Secuestrar la conexión LTE** suplantando una torre celular
3. La cámara se conecta a una **estación base maliciosa**
4. **Interceptar todo el tráfico** mediante un ataque de intermediario
5. Extraer credenciales, imágenes y metadatos

**No se requiere acceso físico.** Funciona a **cientos de pies de distancia**.

### Posibilidades de los ataques Tempest modernos

La transmisión en texto claro también permite **ataques de tipo Tempest**, en los que:
- Se pueden captar las emisiones RF de la cámara
- El flujo de video se puede **reconstruir a distancia**
- La técnica se parece a las de la **CIA durante la Guerra Fría**
- Los equipos SDR modernos la hacen **accesible a aficionados**

______

## Vulnerabilidad crítica n.º 7: transmisiones públicas de cámaras expuestas

### Descubrimiento de enero de 2026

**Gravedad**: CRÍTICA (CVSS 10.0, exposición total del sistema)

### El descubrimiento

En enero de 2026, Ben Jordan y **404 Media** descubrieron que con **simples búsquedas en Google** podían encontrar:
- **Más de 60 interfaces administrativas de Flock Safety completamente expuestas**
- **No se requería nombre de usuario ni contraseña**
- **Transmisiones de video en directo** y 30 días de grabaciones archivadas
- **Acceso completo al panel de control de las cámaras**

### Qué estaba accesible

Desde las interfaces expuestas cualquiera podía:
- **Ver transmisiones de video en directo**
- **Revisar 30 días** de grabaciones archivadas
- **Descargar directamente archivos de video**
- **Controlar cámaras PTZ** (giro, inclinación y zoom) de las unidades Condor
- **Ver rutas y hashes** de archivos de pruebas
- **Eliminar pruebas** con un solo clic
- **Modificar la configuración de las cámaras**
- **Consultar números de serie y ubicaciones de dispositivos**

### Violaciones de privacidad observadas

Ben Jordan documentó haber visto:
- **Una familia metiendo a un bebé en un coche** en el aparcamiento de Lowe's
- **Un hombre saliendo de su casa** en Nueva York por la mañana
- **Una mujer corriendo sola** por un sendero forestal de Georgia
- **Una pareja discutiendo** en un mercado callejero de Atlanta (la IA amplió automáticamente los rostros)
- **Un agente y una ambulancia** atendiendo una crisis de salud mental en Iowa
- **Niños jugando** en un parque infantil de la zona de la bahía de California
- **Un hombre en un columpio** en un parque vacío, disfrutando de un momento privado

Cita de Ben Jordan:
> «Decir estas cosas en voz alta me da náuseas. Pero intento mostrarte solo una mínima parte de la información que cualquier persona con acceso a un motor de búsqueda comercial ha tenido sobre quienes asistieron a ese mercado o caminaron por ese sendero durante los últimos 31 días».

### Capacidades de seguimiento

Las cámaras PTZ Condor expuestas cuentan con **seguimiento mediante IA**:
- **Amplían automáticamente** la imagen de las personas
- **Siguen a personas** mientras se desplazan
- **Detectan y enfocan** teléfonos inteligentes (para leer sus pantallas)
- **Siguen a varios objetivos** a la vez
- **Graban de forma continua** sin supervisión

### Posibilidad de doxxing

Ben Jordan demostró lo fácil que es averiguar la identidad de las personas a partir de grabaciones expuestas:
> «En menos de dos minutos de inteligencia de fuentes abiertas con un motor comercial de reconocimiento facial, descubrí que una de las personas acababa de terminar la carrera de Medicina y que la otra sufría síndrome del intestino irritable crónico. La pareja también había tenido un bebé el año pasado... También sé que condujeron más de 45 minutos desde su casa en los suburbios».

Al cruzar los datos con:
- Servicios de **reconocimiento facial**
- Perfiles de **redes sociales**
- Bases de datos de **registros públicos**
- Información de **filtraciones de datos** (Park Mobile, etc.)
- **Registros de llamadas de emergencia** (muchas ciudades los publican)

Resultado: **desanonimización completa en minutos**

______

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Diagrama general que muestra cómo cámaras Flock Safety PTZ expuestas con seguimiento automático por IA permitieron acceder públicamente a imágenes en directo de personas en parques, senderos y aparcamientos" >}}

______

## Vulnerabilidad crítica n.º 8: recopilación de datos no autorizada

### Contradicción con las declaraciones públicas

**Gravedad**: ALTA (implicaciones jurídicas y de privacidad)

### Afirmaciones de Flock Safety

**Declaración del sitio web oficial**:
> «Flock Safety no captura ni registra datos de personas, solo de vehículos».

### Hallazgos de la investigación independiente

**Lo que hacen realmente las cámaras**:
1. **La detección de movimiento** activa la cámara **ante cualquier movimiento**, no solo el de vehículos
2. La **IA busca matrículas** en la imagen
3. **Si no encuentra una matrícula**, la imagen **se almacena igualmente** (no se elimina)
4. Una **carpeta aparte** guarda las imágenes sin matrículas
5. Se capturan y conservan imágenes de **personas, peatones y ciclistas**

*La afirmación de que solo se capturan vehículos es falsa. La cámara guarda imágenes de cualquiera que pase delante de ella.*

### Observaciones verificadas

Los investigadores documentaron cámaras que capturaron:
- **Personas caminando** delante de una cámara (imagen almacenada)
- **Manos saludando** al objetivo (imagen almacenada)
- **Escritorios u objetos movidos** cerca de la cámara (imagen almacenada)
- **Trabajadores de fábrica** en las instalaciones de producción (imágenes conservadas durante meses)

Cita de GainSec:
> «Cuando pasé delante de la cámara, el módulo de radar activó el módulo de cámara para que me tomara una foto. Después, la IA integrada buscó una matrícula, no encontró ninguna, pero guardó la imagen de todos modos en otra carpeta».

### Implicaciones jurídicas

Esta recopilación de datos no autorizada podría:
- **Infringir las políticas de privacidad declaradas** (prácticas engañosas)
- **Incumplir contratos de adquisición** (si las ciudades especificaron «solo vehículos»)
- **Provocar infracciones del RGPD o la CCPA** (ciudadanos de la UE, residentes de California)
- **Invalidar acuerdos de consentimiento**
- **Exponer a la empresa a litigios** por publicidad engañosa

### Ampliación del alcance de la vigilancia

Las **cámaras PTZ Condor** (desplegadas en 2025-2026) están **diseñadas expresamente** para rastrear a las personas:
- **Detección de personas mediante IA**
- **Zoom automático** a los rostros
- **Seguimiento de personas** al moverse
- **Sin mecanismo de exclusión voluntaria**
- A menudo se despliegan en **parques, senderos y estaciones de transporte**

*Esto supone pasar a gran escala de «lectores de matrículas» a la vigilancia general de la población, sin cambiar las políticas, firmar nuevos contratos ni avisar al público.*

______

## Vulnerabilidad crítica n.º 9: puertos USB expuestos a ataques Rubber Ducky

### Explotación con acceso físico

**Gravedad**: ALTA (con acceso físico)

### La vulnerabilidad

Los **equipos informáticos Bravo** y algunos modelos de cámara tienen:
- **Puertos USB-C expuestos** en el exterior
- **Ninguna seguridad física** (sellos de la carcasa)
- **Ejecución automática** de dispositivos USB
- **Sin autenticación requerida**

### Ataque Rubber Ducky / BadUSB

Un **dispositivo BadUSB** (cuesta entre 5 y 15 dólares):
- Se presenta al sistema como un **teclado USB**
- **Ejecuta scripts preprogramados** (payloads)
- **Se ejecuta automáticamente** al conectarlo
- No requiere **interacción del usuario**

### Escenario de ataque

GainSec demostró lo siguiente:
1. Acercarse a un dispositivo Flock desplegado
2. Conectar un **dispositivo BadUSB** al puerto expuesto
3. El dispositivo ejecuta el payload (script)
4. El payload instala **malware persistente**
5. El atacante **se marcha**
6. El malware **se comunica con su servidor de mando y control** por LTE/Wi-Fi

**Tiempo total**: menos de 30 segundos

### Acciones posibles de los payloads

Los scripts automatizados pueden:
- **Activar el punto de acceso inalámbrico** (eludir las pulsaciones del botón)
- **Instalar una puerta trasera** para acceder de forma remota
- **Exfiltrar datos** a un servidor remoto
- **Modificar grabaciones o pruebas**
- **Desactivar la cámara** o causar una denegación de servicio
- **Unirse a una botnet** para lanzar ataques DDoS
- **Capturar credenciales** de otros sistemas

### Por qué importa

Con **más de 80.000 cámaras**, a menudo instaladas en **zonas semirrurales** con **visibilidad limitada**:
- El **acceso físico** es relativamente fácil
- **No hay guardias** ni vigilancia constante
- Están sujetas con **simples abrazaderas de manguera**
- Suelen instalarse a **siete pies del suelo** (se alcanzan con una escalera pequeña)

Cita de Ben Jordan:
> «Estas cámaras no son fortalezas impenetrables. Son cámaras Android de plástico y equipos informáticos montados a siete pies del suelo con abrazaderas de manguera».

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Diagrama de la cadena de ataque que muestra cómo un dispositivo BadUSB conectado al puerto USB expuesto de una cámara Flock Safety instala malware persistente en menos de 30 segundos" >}}

______

## Vulnerabilidad crítica n.º 10: claves API expuestas públicamente

### Descubrimiento de un investigador OSINT

**Gravedad**: CRÍTICA (CVSS 9.5)

### El descubrimiento

En 2025, el **investigador OSINT Joshua Michael** descubrió:
- Un **sitio web de demostración de Flock Safety expuesto** mediante búsquedas dirigidas en Google
- **5.000 líneas de código fuente** visibles
- Una **clave API activa** integrada en el código
- Acceso a **más de 50 capas privadas** de datos geoespaciales

### Acceso que otorgaba la clave API

La **clave API de ArcGIS** expuesta permitía acceder a:

**1. Datos de registro**
- Nombres de clientes
- Direcciones de correo electrónico
- Número de cámaras por ubicación
- Capacidad para adjuntar archivos

**2. Ubicaciones en directo de coches patrulla** (varios departamentos)
- Seguimiento GPS en tiempo real de vehículos policiales
- Despliegue en Aurora, Colorado
- Departamento de Policía de Carrollton
- **Riesgo para la seguridad nacional**

**3. Información personal de los agentes**
- Nombres y números de teléfono
- Direcciones de correo electrónico
- Zonas de patrulla previstas
- Jurisdicciones de origen

**4. Base de datos de alertas de listas de vigilancia** (Dallas, Texas)
- **6.000 registros** de vehículos señalados
- Matrículas y motivos de las alertas
- Ubicaciones y marcas de tiempo de detección
- ID de las cámaras que captaron los vehículos
- **Seguimiento de movimientos durante cinco meses**

Cita de Joshua Michael:
> «Cualquiera podía buscar en Google, encontrar este mapa y rastrear los patrones de movimiento de estas personas durante cinco meses. También cabe señalar que en la categoría del motivo aparece alguien marcado simplemente como “sospechoso” y muchas otras entradas no tienen motivo o están vacías».

### Superficie de ataque

Las claves API expuestas permiten:
- **Rastrear vehículos concretos**
- Comprometer la **seguridad de los agentes** (domicilios, patrones de patrulla)
- Vulnerar la **seguridad operativa** (dónde está o no está la policía)
- **Intimidar a testigos** (seguir a quienes denunciaron delitos)
- Recopilar **inteligencia criminal** para el crimen organizado

### Contexto de la filtración: Flax Typhoon

Pocas semanas antes de este hallazgo, el grupo de hackers **patrocinado por el Estado chino**, **Flax Typhoon**, comprometió ArcGIS, según los investigadores de seguridad Alexa Feminina y James Zhang.

Cita de InfoSecurity Magazine:
> «Los hackers supuestamente atacaron una aplicación ArcGIS legítima y accesible al público... utilizada para la recuperación ante desastres, la gestión de emergencias y otras funciones críticas».

**Esto significa que Estados hostiles podrían haber tenido acceso** a ubicaciones de vehículos policiales, identidades de agentes, ubicaciones de cámaras de vigilancia y patrones de respuesta ante emergencias.

______

## Vulnerabilidades adicionales (resumen de más de 50)

### Vulnerabilidades 11 a 51

El libro blanco de GainSec documenta **41 hallazgos adicionales**, incluidos:

**Fallos de diseño del sistema**:
- Modo de depuración activado en el firmware de producción
- Proceso de arranque inseguro que permite comprometer el cargador de arranque
- Ausencia de elemento seguro o TPM para almacenar claves
- Mecanismo predecible de actualización del firmware

**Problemas de autenticación**:
- Los tokens de sesión no caducan
- No hay restricciones de acceso por dirección IP
- Credenciales compartidas entre flotas de dispositivos
- No hay fijación de certificados

**Seguridad de redes**:
- Puertos abiertos con servicios de depuración
- Telnet activado en algunas unidades
- Servidores FTP con credenciales débiles
- Vulnerabilidades de DNS rebinding

**Privacidad y retención de datos**:
- Imágenes almacenadas más allá del plazo declarado
- Metadatos que nunca se eliminan
- Recopilación de datos de reconocimiento facial
- Seguimiento de ubicaciones que no se limita a vehículos

**Seguridad física**:
- Carcasas fáciles de desmontar
- Interfaces serie expuestas
- Puertos de depuración JTAG accesibles
- Ausencia de sellos que evidencien manipulación

**Fallos criptográficos**:
- Generación débil de números aleatorios
- Claves de cifrado codificadas
- MD5 todavía se usa en la cadena de hashes
- Validación de certificados desactivada

**Divulgación de información**:
- Mensajes de error detallados revelan información interna
- Listado de directorios activado en servidores web
- Comentarios del código fuente contienen credenciales
- Copias de seguridad de configuración legibles por todo el mundo

### Estado de CVE

En mayo de 2026:
- **22 CVE asignados** y publicados
- **8 CVE pendientes** de asignación por MITRE
- **21 hallazgos** no presentados para CVE, a discreción del investigador
- **Todos los hallazgos** documentados en el libro blanco de GainSec

Detalles técnicos completos: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## Respuesta de Flock Safety

### Declaraciones oficiales

**Publicación del blog de noviembre de 2025**:
> «Flock se compromete a mejorar continuamente la seguridad... Ninguna de las vulnerabilidades detalladas en el informe afecta a la capacidad de nuestros clientes para cumplir sus objetivos de seguridad pública».

**Afirmación**: las vulnerabilidades requieren acceso físico y un «conocimiento íntimo».

**Pruebas en contra**:
- Para ver transmisiones de cámaras expuestas solo hacía falta **buscar en Google**
- Los exploits inalámbricos solo requieren **estar cerca**
- La clave API expuesta se podía aprovechar **completamente a distancia**
- Las contraseñas codificadas se conocen **de forma generalizada** desde su divulgación

### Desestimación de los dispositivos de investigación

Flock afirmó inicialmente que los dispositivos de investigación estaban:
> «Sin conexión a la nube... como un iPhone robado de un camión antes de conectarlo».

*Se demostró que era falso.* Los investigadores probaron **dispositivos conectados a la nube** y obtuvieron los mismos resultados. Las cámaras de acceso público presentaban las **mismas vulnerabilidades**, y 404 Media encontró **más de 60 cámaras de producción expuestas**.

### Respuesta a los investigadores

GainSec informó que sus intentos de divulgación responsable recibieron:
- Una **recompensa por errores sujeta a un acuerdo de confidencialidad** (para silenciar la divulgación)
- **Ninguna confirmación** de que se hubieran aplicado correcciones
- Una **declaración de relaciones públicas** publicada antes del plazo de 90 días
- **Ningún reconocimiento al investigador** en la declaración
- La **pérdida de su empleo** dentro de las 48 horas posteriores a la publicación del video

Ben Jordan informó de:
- **Visitas de la policía** a su domicilio
- Presuntos **investigadores privados** fotografiando su casa
- **Acoso de vecinos**
- Amenazas de **cese y desistimiento** por parte de Flock Safety

Cita de Ben:
> «No considero estas situaciones consecuencias o castigos por investigar vulnerabilidades de seguridad. Las considero consecuencias y castigos por hacerlo de forma ética y transparente».

### Despliegue continuo

*A pesar de todo*, Flock Safety:
- **Sigue vendiendo** dispositivos vulnerables
- No publica **actualizaciones de firmware** que corrijan las causas raíz
- **Sigue usando Android Things 8.x** (fin de vida útil en 2021)
- No exige **MFA** a las fuerzas del orden

______

## Respuesta legislativa y política

### Solicitud de investigación del Senado de EE. UU.

**Febrero de 2026**: los senadores **Ron Wyden** (Oregón) y **Raja Krishnamoorthi** (Illinois) enviaron una carta formal a la FTC para solicitar una investigación.

**Extracto de la carta**:
> «Flock expuso innecesariamente los datos personales sensibles de los estadounidenses al robo por parte de hackers y espías extranjeros».

**Motivos citados**:
- Riesgos para la seguridad nacional
- Afirmaciones engañosas sobre privacidad
- Prácticas de seguridad inadecuadas
- Ausencia de requisitos de MFA

### Medidas de los ayuntamientos

**Denver, Colorado**:
- En diciembre de 2025, el ayuntamiento **votó en contra** de renovar el contrato de Flock
- Citó el **«desprecio de Flock por la honestidad y la rendición de cuentas»**
- En enero de 2026, el alcalde **revocó la decisión** mediante un «acuerdo entre bastidores»
- Continúa la reacción pública

**Evanston, Illinois**:
- Descubrió que **ICE usaba las cámaras** sin consentimiento
- Votó a favor de **retirar las cámaras**
- *Flock reinstaló las cámaras sin autorización*
- La ciudad usa dinero de los contribuyentes para **cubrirlas con lonas** y emprender acciones legales

**Oakland, California**:
- Aplazó la votación para una **ampliación de 2,25 millones de dólares**
- Encargó una auditoría de seguridad independiente
- La auditoría consideró **engañosas** las afirmaciones de eficacia de Flock

### Solicitudes de documentos públicos

Varias ciudades investigan a partir de:
- Investigaciones de seguridad disponibles públicamente
- Solicitudes FOIA de contratos de Flock
- Requisitos de auditoría independiente
- Presión de grupos comunitarios y defensores

______

## Análisis técnico: escenarios de ataque reales

### Escenario 1: vigilancia de un Estado-nación

**Actor de amenaza**: servicio de inteligencia extranjero

**Objetivo**: rastrear a funcionarios del gobierno

**Método**:
1. Usar un IMSI catcher para interceptar el tráfico LTE de las cámaras
2. Extraer credenciales en texto claro de la transmisión
3. Acceder al backend mediante claves API comprometidas (o una capa ArcGIS expuesta previamente)
4. Consultar la base de datos en busca de vehículos registrados en instalaciones gubernamentales
5. Seguir los movimientos de funcionarios y militares

**Tiempo de ejecución**: días (una vez instalada la infraestructura)  
**Probabilidad de detección**: baja (el canal C2 cifrado imita tráfico legítimo)

### Escenario 2: contravigilancia del crimen organizado

**Actor de amenaza**: organización de tráfico de drogas

**Objetivo**: identificar patrones de patrulla policial

**Método**:
1. Comprar un dispositivo BadUSB (15 dólares)
2. Conducir hasta las cámaras del territorio de operación
3. Conectar el BadUSB al puerto USB expuesto (30 segundos)
4. El payload desactiva la cámara o modifica las grabaciones
5. Alternativa: el payload exfiltra el seguimiento de vehículos policiales a un servidor remoto

**Tiempo de ejecución**: 30 segundos por cámara  
**Probabilidad de detección**: baja (parece actividad legítima de un dispositivo)

### Escenario 3: acosador o violencia doméstica

**Actor de amenaza**: expareja abusiva

**Objetivo**: seguir los movimientos de la víctima

**Método**:
1. Obtener la matrícula de la víctima (información pública)
2. Buscar en Google interfaces expuestas de cámaras Flock (vulnerabilidad de enero de 2026)
3. Consultar 30 días de grabaciones y buscar apariciones del vehículo
4. Cruzar la información con bases de datos públicas (trabajo, domicilio, etc.)
5. Establecer los hábitos y horarios de la víctima

**Tiempo de ejecución**: de minutos a horas  
**Probabilidad de detección**: cero (no existen registros de autenticación)

### Escenario 4: manipulación de pruebas

**Actor de amenaza**: acusado en una causa penal

**Objetivo**: destruir pruebas antes del juicio

**Método**:
1. Averiguar la ubicación de la cámara durante el descubrimiento probatorio de la orden judicial
2. Acceder físicamente a la cámara (secuencia de pulsaciones del botón)
3. Obtener un shell root
4. Navegar hasta la carpeta de pruebas
5. Eliminar imágenes o videos concretos, o modificar marcas de tiempo

**Tiempo de ejecución**: menos de cinco minutos  
**Probabilidad de detección**: baja (salvo que se analice forensemente la cámara antes del acceso de la defensa)

### Escenario 5: activista por la privacidad o periodista

**Actor de amenaza**: defensor de la transparencia

**Objetivo**: documentar excesos de vigilancia

**Método**:
1. Usar dispositivos de detección (consulta nuestra [guía de hardware Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Cartografiar las ubicaciones de cámaras de la comunidad
3. Presentar solicitudes FOIA sobre las políticas de grabación
4. Demostrar las vulnerabilidades ante el ayuntamiento
5. Promover la retirada o la supervisión

**Tiempo de ejecución**: continuo  
**Probabilidad de detección**: alta (actividad pública)

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matriz que compara cinco escenarios de ataque reales contra cámaras Flock Safety: vigilancia de un Estado-nación, contravigilancia del crimen organizado, acoso, manipulación de pruebas y activismo por la privacidad" >}}

______

## Cómo defenderse de estas vulnerabilidades

### Para agencias de las fuerzas del orden

**Medidas inmediatas**:
1. **Exigir MFA/2FA** a todos los usuarios (llaves de seguridad USB)
2. **Auditar mensualmente los registros de acceso** para detectar consultas no autorizadas
3. **Limitar el intercambio** a las jurisdicciones que realmente lo necesitan
4. **Aislar la red**: conectar las cámaras a VLAN dedicadas
5. **Seguridad física**: sellos que evidencien manipulaciones y vigilancia de las cámaras
6. Crear un **plan de respuesta a incidentes** en caso de intrusión

**Requisitos contractuales**:
1. **Auditorías de seguridad periódicas** a cargo de empresas independientes
2. **Actualizaciones de firmware obligatorias** dentro de los 30 días posteriores a cada parche
3. **Notificación de CVE** en un plazo de 24 horas
4. **Almacenamiento cifrado de pruebas** con claves gestionadas por el cliente
5. **Sanciones en los SLA** por fallos de seguridad
6. **Derecho a auditar** las instalaciones y el código del proveedor

**Estrategia a largo plazo**:
1. **Plan de transición** para abandonar sistemas operativos sin soporte
2. **Infraestructura autoalojada** (reducir la dependencia de la nube)
3. Evaluar **alternativas de código abierto**
4. Mantener la **transparencia con la comunidad** sobre ubicaciones y políticas de cámaras

### Para Flock Safety (recomendaciones)

**Prioridad crítica** (inmediata):
1. **Desactivar** la creación de puntos de acceso inalámbricos mediante pulsaciones del botón
2. **Obligar a usar MFA** en todas las cuentas (sin excepciones)
3. **Rotar todas las credenciales codificadas** en todo el sistema
4. Publicar un **parche urgente** para las interfaces públicas expuestas
5. Cifrar los datos **en reposo** y gestionar correctamente las claves

**Prioridad alta** (30 días):
1. **Migrar a un sistema operativo con soporte** (Android 12 o superior, o Linux)
2. Crear un **programa de recompensas por errores sin acuerdos de confidencialidad**
3. Publicar los resultados de una **auditoría de seguridad externa**
4. Cifrar el **tráfico de red de extremo a extremo**
5. **Mejorar la seguridad física** (retirar USB expuestos, reforzar carcasas)

**Prioridad media** (90 días):
1. **Rediseñar por completo** el sistema de autenticación
2. Implementar **arranque seguro** con firmware verificado
3. Integrar un **módulo de seguridad de hardware**
4. Obtener **certificaciones de cumplimiento** (FedRAMP, SOC 2, ISO 27001)
5. Crear un **panel de seguridad para clientes** con notificaciones de filtraciones

**A largo plazo** (un año):
1. Publicar **componentes de seguridad de código abierto** (para fomentar confianza)
2. Crear un programa de **pruebas adversariales** (equipo rojo)
3. Establecer requisitos para puestos de **ingeniería de seguridad**
4. Integrar prácticas de seguridad en el **ciclo de vida de desarrollo de software** (DevSecOps)
5. Participar en **estándares del sector** (OWASP, CIS)

### Para particulares

**Estrategias de protección**:
1. **Usar dispositivos de detección** (consulta nuestra [guía de hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Cartografiar las cámaras** de tu zona
3. **Variar rutas y horarios** para reducir el análisis de patrones
4. **Solicitar supervisión y transparencia** ante el ayuntamiento
5. Presentar solicitudes **FOIA** sobre tus datos (cuando la ley lo permita)
6. **Apoyar leyes de privacidad** estatales y federales

**Medidas de seguridad operativa**:
1. **Evitar vehículos distintivos** (elegir marca, modelo y color comunes)
2. **Usar vehículos distintos** para actividades sensibles (cuando sea legal)
3. Elegir **medios de transporte alternativos** (bicicleta, transporte público, caminar)
4. **Usar cubiertas de matrículas para proteger la privacidad** (solo si es legal en tu jurisdicción)
5. Usar **bolsas de Faraday** para teléfonos si preocupa la correlación

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Hoja de ruta priorizada de medidas correctivas inmediatas, a 30 días, 90 días y a largo plazo que Flock Safety debería aplicar para solucionar vulnerabilidades críticas" >}}

______

## El equipo de investigación

### GainSec (Jon «GainSec» Gaines)

**Trayectoria**: profesional de seguridad ofensiva, con más de diez años de experiencia

**Contribuciones**:
- Descubrió **47 de las 51** vulnerabilidades
- Publicó un **libro blanco formal** con detalles técnicos
- Coordinó la **divulgación responsable** con Flock Safety
- Registró **30 CVE** (22 publicadas, 8 pendientes)
- Creó una **lista de verificación para defensores** dirigida a profesionales de seguridad

**Contacto**: whitepaper@gainsecmail.com  
**Investigación**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)  
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Trayectoria**: periodista, músico e investigador de tecnología

**Contribuciones**:
- **Documentación en video** de vulnerabilidades
- **Demostraciones públicas** para periodistas (The Guardian, 404 Media)
- Descubrió **más de 60 transmisiones de cámaras expuestas** mediante Google
- **Activismo y educación pública**
- **Coordinación legislativa** con oficinas de senadores

**Contacto**: mediante su canal de YouTube  
**Trabajo**: YouTube - Benn Jordan

### Joshua Michael (Next AI)

**Trayectoria**: especialista OSINT e investigador de privacidad

**Contribuciones**:
- Descubrió **claves API expuestas** mediante búsquedas dirigidas en Google
- Documentó la **exposición de capas de ArcGIS**
- **Metodología OSINT** para seguir la investigación
- **Correlación de datos** con filtraciones públicas

**Organización**: Next AI, empresa de inteligencia de fuentes múltiples

### Colaboradores

- **404 Media**: periodismo de investigación y divulgación pública
- **The Guardian**: cobertura internacional
- **Lucy Parsons Labs**: años de activismo e investigación sobre ALPR
- **Sassy South**: organización comunitaria y transparencia
- **DeFlock / Will Freeman**: proyecto de cartografía de cámaras
- **Ed Vogel**: análisis jurídico y de políticas

______

## Consideraciones éticas

### Cronología de divulgación responsable

La comunidad de seguridad siguió las prácticas recomendadas de **divulgación responsable**:

**Protocolo habitual**:
1. Descubrir una vulnerabilidad
2. **Notificar al proveedor de forma privada durante 90 días**
3. El proveedor desarrolla y despliega un parche
4. Realizar la **divulgación pública** tras el parche o al cumplirse 90 días (lo que ocurra antes)
5. Publicar un análisis detallado para facilitar el aprendizaje defensivo

**Lo que ocurrió**:
1. GainSec descubrió vulnerabilidades (finales de 2024)
2. **Contactó repetidamente** con Flock Safety (desde febrero de 2025)
3. Flock ofreció una **recompensa por errores con acuerdo de confidencialidad** (para silenciar la divulgación)
4. Flock publicó una **declaración de prensa antes de tiempo** (sin reconocer al investigador)
5. **No confirmó** que se hubieran desplegado parches
6. GainSec procedió con la **divulgación pública** una vez vencidos los plazos de 90 días
7. Ben Jordan y 404 Media **verificaron de forma independiente** los fallos en sistemas de producción

### Represalias contra investigadores

Tanto GainSec como Ben Jordan informaron de:
- **Pérdida del empleo** o dificultades laborales
- **Visitas policiales** a sus domicilios
- **Vigilancia presunta** de sus casas y propiedades
- **Acoso de vecinos**
- Amenazas de **cese y desistimiento**
- **Ataques en redes sociales** (el director ejecutivo de Flock los llamó «terroristas»)

Este **efecto disuasorio** sobre la investigación de seguridad:
- Desalienta la divulgación de vulnerabilidades
- Retrasa correcciones de seguridad críticas
- Perjudica la seguridad pública
- Viola las normas éticas de la comunidad de seguridad

*La respuesta de Flock Safety a los investigadores que siguieron los protocolos de divulgación sienta un precedente peligroso para toda la comunidad de investigación de seguridad.*

Cita de Ben Jordan:
> «No tengo tiempo para dedicar aún más meses a otra vulnerabilidad de Flock Safety, pero, como se ve, esta es urgente y, francamente, me preocupa que ya se esté explotando».

### Interés público

Estos investigadores actuaron **en interés público** al:
- **Seguir los protocolos de divulgación responsable**
- **Avisar primero al proveedor** antes de la divulgación pública
- **Redactar detalles sensibles** que facilitarían la explotación
- **Proporcionar orientación defensiva** para profesionales
- **Abogar por cambios de política** mediante los canales adecuados
- **Aceptar riesgos personales** para informar al público

Sin su trabajo:
- **Más de 80.000 cámaras vulnerables** seguirían sin corregirse
- **Más de 150 millones de escaneos diarios de vehículos** seguirían desprotegidos
- **Millones de estadounidenses** quedarían expuestos sin saberlo
- La **seguridad nacional** se vería comprometida
- **No habría medidas legislativas** en marcha

______

## Conclusión: el camino a seguir

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Cronología del proceso de divulgación de vulnerabilidades de Flock Safety entre 2024 y 2026, desde el descubrimiento inicial y la divulgación responsable hasta la exposición que sigue sin corregirse" >}}

### Situación actual (mayo de 2026)

- **Más de 50 vulnerabilidades críticas** documentadas y divulgadas parcialmente
- **Más de 80.000 cámaras** continúan desplegadas con fallos sin corregir
- El proveedor no ha realizado una **corrección integral**
- **Medidas regulatorias limitadas** (se solicitó una investigación de la FTC, pero no se inició)
- **Riesgo de explotación continuo** para la seguridad nacional y la privacidad individual

### Qué debe hacerse

**En todo el sector**:
1. **Auditorías de seguridad obligatorias** antes de desplegar tecnología en organismos públicos
2. **Pruebas independientes** realizadas por terceros cualificados
3. **Divulgación pública** de los resultados de auditoría
4. **Responsabilidad del proveedor** por los fallos de seguridad
5. **Cumplimiento de estándares** (NIST, ISO, etc.)

**Para Flock Safety**:
1. **Parches de emergencia inmediatos** para vulnerabilidades críticas
2. **Migración del sistema operativo** a una plataforma con soporte
3. **Reconocimiento público** del alcance del problema
4. **Compensación** para investigadores afectados
5. **Informes transparentes** sobre la postura de seguridad

**Para las fuerzas del orden**:
1. Incluir **requisitos de seguridad** en los contratos de adquisición
2. Realizar **auditorías periódicas** de los sistemas desplegados
3. Hacer **obligatoria la MFA** para todos los usuarios
4. Preparar **planes de respuesta a incidentes**
5. Mantener la **transparencia con la comunidad** sobre programas de vigilancia

**Para legisladores**:
1. Aprobar **estándares federales** para tecnología de vigilancia
2. Exigir la **notificación de vulnerabilidades** a las partes afectadas
3. Establecer **protecciones para denunciantes** e investigadores de seguridad
4. Prever **recursos civiles** por violaciones de privacidad
5. Crear **mecanismos de supervisión** con experiencia técnica

### El panorama general

Este caso representa **mucho más que Flock Safety**. Es un ejemplo de:
- Un **sector de vigilancia** que prioriza el crecimiento sobre la seguridad
- **Adquisiciones gubernamentales** sin suficiente experiencia técnica
- **Afirmaciones de proveedores** sin cuestionar ni verificar
- **Incentivos financieros** incompatibles con la seguridad pública
- **Lagunas regulatorias** en la supervisión de tecnologías emergentes

*Cada ciudad que firma un contrato con Flock sin una verificación de seguridad independiente acepta estos riesgos en nombre de sus residentes.*

### Llamado a la acción

**Profesionales de seguridad**:
- **Apoyar la divulgación responsable**
- **Contribuir a herramientas de seguridad de código abierto**
- **Defender la protección de investigadores**

**Fuerzas del orden**:
- **Exigir responsabilidades a los proveedores**
- **Exigir auditorías de seguridad antes del despliegue**
- **Implementar MFA de inmediato**
- **Consultar a la comunidad de seguridad**

**Responsables de políticas públicas**:
- **Aprobar legislación que establezca estándares de seguridad**
- **Financiar auditorías independientes** de tecnología de vigilancia
- **Proteger a denunciantes e investigadores**
- **Crear organismos de supervisión** con experiencia técnica

**Público**:
- **Informarse** sobre la vigilancia en su comunidad
- **Asistir a reuniones del ayuntamiento** cuando se debatan contratos
- **Apoyar organizaciones** que defienden la transparencia
- **Contactar a representantes** para comunicar sus inquietudes
- Usar **herramientas de detección** para cartografiar la vigilancia (consulta nuestra [guía de hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### Lecturas relacionadas

- **[Vigilancia con cámaras Flock Safety: prevalencia, riesgos para la privacidad y estrategias de protección](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**: comprender el panorama de vigilancia
- **[Proyecto de detección Flock-You: guía de hardware contra la vigilancia](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**: crear tu propio dispositivo de detección

Esperar a que el sector corrija estos fallos no es una estrategia de protección. Los **[dispositivos de detección FlockYou](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** de STS Collective funcionan hoy, y el código para lectores **SIMEONONSECURITY** ofrece hasta un 20 % de descuento.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Comprar detectores FlockYou y ahorrar un 20 %
{{< /centerbutton >}}

______

## Referencias

1. [Investigación de GainSec sobre el ecosistema anti-crimen - GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [Libro blanco de GainSec - DOI de Zenodo: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [Blog de GainSec - análisis técnicos informales](https://gainsec.com/)
4. [Respuesta oficial de Flock Safety - noviembre de 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media - transmisiones expuestas de cámaras Flock](https://www.404media.co/)
6. [Ben Jordan en YouTube - demostraciones de vulnerabilidades](https://www.youtube.com/@BennJordan)
7. [National Vulnerability Database](https://nvd.nist.gov/)
8. [Base de datos CVE de MITRE](https://cve.mitre.org/)
9. [Electronic Frontier Foundation - vigilancia ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [Carta del senador Wyden a la FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs - investigación sobre ALPR](https://lucyparsonslabs.com/)
12. [Proyecto DeFlock - cartografía de cámaras](https://deflockproject.org/)
13. [Distributed Denial of Secrets - imágenes del sistema de archivos de cámaras ALPR de Flock](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee - las cámaras Flock están plagadas de vulnerabilidades de seguridad y credenciales codificadas](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED y 404 Media - hackers accedieron a una cámara Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday - esta semana en seguridad: las cámaras Flock son antiguas](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD - CVE-2021-1905: use-after-free de GPU Qualcomm Adreno](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD - CVE-2018-9568: confusión de tipos en sockets del kernel de Linux](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership - detección ALPR de Flock Safety y referencia de dispositivos](https://wifimothership.com/flock)
20. [CVE.org - búsqueda de registros del programa CVE](https://www.cve.org/)
21. [Alerta de seguridad de Flock Safety - detección de disparos y lectores de matrículas](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec - Fly By Device 2: RCE inalámbrica de Falcon y Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec - Root from the Coop Device 3: shell root en el equipo Bravo de Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)
