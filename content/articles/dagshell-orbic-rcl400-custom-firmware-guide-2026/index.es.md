---
title: "Firmware personalizado DagShell para Orbic RCL400: guía 2026"
date: 2026-05-28
lastmod: 2026-11-11
toc: true
draft: false
description: "Guía técnica del firmware DagShell para Orbic RCL400. Explica la instalación, las herramientas de privacidad, el wardriving y los límites de la investigación."
genre: ["Firmware personalizado", "Seguridad móvil", "Herramientas de privacidad", "Seguridad de redes", "Wardriving", "Pruebas de penetración", "Seguridad IoT", "Investigación de seguridad", "Seguridad de hardware", "Tecnología de privacidad"]
tags: ["DagShell", "Orbic RCL400", "Firmware personalizado", "Seguridad de hotspot", "Herramientas de privacidad", "Corrección TTL", "Suplantación MAC", "Detección de IMSI catchers", "Wardriving", "Seguimiento GPS", "Ataque Evil Twin", "Portal cautivo", "Sniffer DNS", "Escáner ARP", "Escáner de puertos", "Complemento Raspberry Pi", "Seguridad WiFi", "Hotspot móvil", "Supervisión de redes", "Pruebas de penetración", "Investigación de seguridad", "Escaneo Bluetooth", "Ataque de desautenticación", "Escaneo WiFi", "Búsqueda OUI", "Carga a Wigle", "Supervisión de torres celulares", "Comandos AT", "Gestor de firewall", "Bloqueo de anuncios", "Cifrado TLS", "Integración con RayHunter", "STS Collective", "Laboratorio de seguridad móvil", "Análisis de redes", "Firmware de privacidad", "Seguridad de código abierto", "Compilación cruzada ARM", "Linux integrado", "Kit de herramientas de seguridad", "Herramientas de hacking", "Equipo rojo", "Reconocimiento de redes"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Ilustración de un hotspot Orbic RCL400 con una interfaz verde brillante, rodeado de representaciones abstractas de herramientas de seguridad, como gráficos y mapas, sobre un fondo azul marino oscuro."
coverCaption: ""
---

**Convierte tu Orbic RCL400 en un laboratorio móvil de investigación de seguridad**

## Introducción: Un hotspot para hackers

**DagShell** es un firmware personalizado de código abierto para el **hotspot móvil Orbic RCL400**. Convierte un dispositivo celular común en un **kit portátil de investigación de seguridad y privacidad**. El firmware, creado por el investigador de seguridad «dag», ofrece **herramientas de hacking, funciones de privacidad y capacidades de supervisión de redes** en una interfaz de terminal con estética de hacker, verde sobre negro.

Esta guía explica:
- **Qué es DagShell** y qué funciones incluye
- **Cómo instalarlo paso a paso**, con webflasher y métodos manuales
- **Qué herramientas ofrece** y cómo funcionan
- Cómo configurar un **complemento Raspberry Pi** para ampliar sus funciones
- **Por qué combinar DagShell con RayHunter** para la seguridad móvil
- **Casos de uso reales** para investigadores de seguridad y defensores de la privacidad
- **Consideraciones legales y éticas**

**En resumen**: DagShell y RayHunter en un Orbic RCL400 forman un **laboratorio móvil de seguridad** para detectar IMSI catchers, hacer wardriving, analizar redes y proteger la privacidad.

**Dispositivos preconfigurados**: Este artículo cuenta con el patrocinio de **STS Collective**, que ofrece hotspots Orbic RCL400 preconfigurados con **RayHunter y DagShell** instalados: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Descuento exclusivo para lectores**: Ahorra hasta un 20 % en productos de STS Collective, incluidos los Orbic RCL400 preconfigurados. Usa el código **SIMEONONSECURITY** al pagar o [compra con el descuento aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

______

## ¿Qué es DagShell?

### Descripción general

**DagShell** es un firmware personalizado de código abierto que reemplaza la interfaz web original del Orbic RCL400 con un **kit completo de herramientas de seguridad**, que incluye:

- **Interfaz de estilo terminal** con arte ASCII y estética de hacker
- **Interfaz web cifrada con TLS 1.2 o superior** (certificado autofirmado)
- **Herramientas de protección de privacidad** (ocultación de TTL, suplantación de MAC y bloqueo de anuncios mediante DNS)
- **Supervisión de redes** (conexiones activas, tablas de enrutamiento y consultas DNS)
- **Herramientas de hacking** (detección de IMSI catchers, escaneo de puertos y descubrimiento ARP)
- **Capacidades de ataque** (punto de acceso Evil Twin, phishing con portal cautivo y ataques de desautenticación)
- **Seguimiento GPS y wardriving** con exportación CSV compatible con Wigle
- **Complemento Raspberry Pi** para GPS, escaneo Bluetooth y reconocimiento WiFi
- **Acceso al sistema de archivos** mediante un gestor de archivos en el navegador
- **Funciones SMS** mediante comandos AT
- **Persistencia**: se inicia automáticamente al arrancar

### Especificaciones técnicas

**Plataforma**: hotspot móvil Orbic RCL400\
**Arquitectura**: ARM Linux (kernel 3.18)\
**Lenguaje**: C/C++ (binario ARM estático)\
**Cifrado**: TLS 1.2 o superior con certificados autofirmados (PKI de dos niveles)\
**Servidor web**: servidor HTTPS integrado personalizado (puerto 8443)\
**Interfaz**: interfaz de terminal en el navegador\
**Licencia**: MIT (código abierto)\
**GitHub**: [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Diseño visual

DagShell tiene una **estética retro de hacker**:
- **Logotipo ASCII** en cada página
- **Colores verde sobre negro** (estilo Matrix)
- **Fuente monoespaciada** (Fira Code)
- **Efectos de líneas de escaneo** y texto brillante
- **Diseño inspirado en una terminal**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Firmware DagShell en un Orbic RCL400. La interfaz de terminal verde sobre negro muestra arte ASCII y un menú de herramientas de seguridad" >}}

______

## Desglose completo de funciones

### 🏠 Panel

**Resumen del sistema**:
- **Tiempo activo**: cuánto tiempo lleva funcionando el dispositivo
- **Interfaz de comandos AT**: control directo del módem para usuarios avanzados
- **Estado rápido**: dirección IP y estado de conexión

Los **comandos AT** permiten controlar el módem a bajo nivel:
```
Example AT Commands:
AT+CSQ       - Signal quality
AT+COPS?     - Current network operator  
AT+CREG?     - Network registration status
AT+CIMI      - Get IMSI (subscriber identity)
AT+CGSN      - Get IMEI (device identifier)
```

### 🌐 Herramientas de red

**Información de la red actual**:
- Detalles de la **dirección IP y la interfaz**
- **Máscara de subred, puerta de enlace** y dirección de difusión
- **Estadísticas de red** (paquetes enviados y recibidos)

**Visor de la tabla de enrutamiento**:
- Muestra todas las rutas de red
- Información de la puerta de enlace predeterminada
- Correspondencia de interfaces

**Monitor de conexiones activas**:
- Lista en tiempo real de **todas las conexiones TCP/UDP**
- Direcciones IP locales y remotas
- Números de puerto y estados de conexión
- Útil para **supervisar las comunicaciones del dispositivo**

### 🔒 Conjunto de protección de privacidad

#### Corrección TTL

**Propósito**: ocultar al operador el tráfico del hotspot para evitar su detección

**Cómo funciona**:
- Cambia a **65** el valor de **Time To Live (TTL)** de los paquetes IP
- Los operadores detectan el uso compartido de conexión mediante la reducción del TTL (teléfono = 64, dispositivo conectado = 63)
- Al establecer el TTL en 65, **todo el tráfico parece local**

**Caso de uso**: evitar restricciones o limitaciones del operador sobre el tethering

**Comandos**:
```bash
# Enable TTL fix
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Disable TTL fix  
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### Suplantación de la dirección MAC

**Propósito**: aleatorizar la dirección MAC del dispositivo para proteger la privacidad

**Cómo funciona**:
- Cambia la dirección MAC de **wlan0** (interfaz WiFi)
- Genera una **dirección MAC aleatoria** o permite introducir una personalizada
- Hace que el dispositivo sea **difícil de rastrear** entre sesiones

**Caso de uso**: evitar el seguimiento mediante MAC en las redes a las que te conectas

**Proceso**:
1. La interfaz se desactiva
2. Se aplica una nueva dirección MAC
3. La interfaz se vuelve a activar
4. Se restablece la conexión

#### Bloqueo de anuncios mediante DNS

**Propósito**: bloquear anuncios y rastreadores mediante DNS

**Cómo funciona**:
- Modifica el archivo `/etc/hosts` con una **lista de bloqueo**
- Los dominios de la lista se resuelven como **127.0.0.1** (localhost)
- Bloquea anuncios **para todos los dispositivos conectados**

**Caso de uso**: bloquear anuncios en toda la red sin configurar cada dispositivo

**Origen de la lista**: dominios comunes de anuncios y rastreo (personalizable)

### 📱 Administración de SMS

**Enviar SMS**:
- Envía mensajes de texto al módem mediante **comandos AT**
- Útil para **notificaciones remotas** o pruebas

**Ver mensajes**:
- Enlace a la bandeja de entrada nativa de Orbic
- Permite leer los SMS recibidos

**Comando AT utilizado**:
```
AT+CMGS="PHONE_NUMBER"
Message text here^Z
```

### 🔧 Herramientas de hacking

#### Detector de IMSI catchers

**Propósito**: supervisar información de torres celulares y buscar anomalías que indiquen dispositivos **IMSI catcher o Stingray**

**Cómo funciona**:
- Consulta al módem los **datos de la torre celular**:
  - **Cell ID** (identificador de torre)
  - **LAC** (código de área de ubicación)
  - **MCC/MNC** (código de país móvil y código de red móvil)
  - **Intensidad de señal** (RSSI)
  - **Generación de red** (2G/3G/4G)
- **Registra los cambios** para detectar cambios sospechosos de torre
- **Seguimiento de referencia**: establece cuáles son las torres habituales de la zona

**Indicadores de detección**:
- **Cambio repentino de torre celular** mientras el dispositivo permanece quieto
- **Descenso a 2G** *(los IMSI catchers suelen forzar 2G para eliminar el cifrado)*
- Aparición de un **Cell ID desconocido**
- **Señal débil** de una torre falsa
- **Reconexiones frecuentes**

**Complemento con RayHunter**: DagShell ofrece **supervisión de torres celulares**. RayHunter ofrece **detección dedicada de IMSI catchers** con un análisis más avanzado (consulta la sección siguiente).

#### Escáner de puertos

**Propósito**: analizar direcciones IP objetivo en busca de puertos abiertos

**Cómo funciona**:
- **Escaneo TCP SYN**: envía paquetes SYN a los puertos objetivo
- **Detección por tiempo de espera**: determina si el puerto está abierto, cerrado o filtrado
- **Compatibilidad con rangos**: analiza un puerto o un rango de puertos

**Casos de uso**:
- **Reconocimiento de redes**
- **Detección de dispositivos IoT**
- **Auditoría de seguridad** de redes locales
- **Identificación de servicios**

**Comando**:
```bash
# Scan ports 1-1000 on target
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Gestor de firewall

**Propósito**: bloquear o desbloquear direcciones IP mediante iptables

**Cómo funciona**:
- Usa **reglas iptables** para DESCARTAR paquetes desde o hacia las IP indicadas
- Las **reglas persistentes** sobreviven a los reinicios si se guardan
- Incluye funciones de **lista de permitidos y lista de bloqueo**

**Casos de uso**:
- **Bloquear IP maliciosas**
- **Impedir accesos no autorizados**
- **Gestionar o filtrar tráfico**
- **Control parental**

**Comandos**:
```bash
# Block IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Unblock IP
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Herramientas de ataque

**AVISO LEGAL IMPORTANTE**: Estas herramientas son solo para **pruebas de seguridad autorizadas**. Usarlas contra redes que no te pertenecen o para las que no tienes permiso explícito por escrito es **ilegal** en muchas jurisdicciones (por ejemplo, según la Computer Fraud and Abuse Act de EE. UU. y la Computer Misuse Act del Reino Unido). Úsalas solo en **tus propias redes** o en **entornos de laboratorio controlados**.

#### Sniffer DNS

**Propósito**: registrar las consultas DNS de los clientes conectados

**Cómo funciona**:
- **Registra con iptables** el tráfico del puerto 53 (DNS)
- **No requiere modo promiscuo**
- Registra todas las solicitudes DNS de los clientes del hotspot
- Revela **qué sitios web y servicios** consultan los clientes

**Casos de uso autorizados**:
- **Análisis del tráfico de red**
- **Supervisión parental** (de tu propia familia)
- **Investigación de seguridad** en tus dispositivos
- **Análisis del comportamiento de malware**

*Esto captura metadatos (los dominios visitados) de los clientes conectados. Despliégalo solo en redes que te pertenezcan o que administres.*

#### Escáner ARP

**Propósito**: detectar dispositivos en la red local

**Cómo funciona**:
- Envía **solicitudes ARP** a todas las IP de la subred
- Los dispositivos responden con sus **direcciones MAC**
- La **búsqueda OUI** identifica al fabricante (Apple, Samsung, etc.)
- Crea un **mapa de red** con los dispositivos activos

**Casos de uso**:
- **Inventario de red**
- **Detección de dispositivos desconocidos**
- **Análisis de redes BYOD**
- **Detección de dispositivos IoT**

**Ejemplo de salida**:
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Propósito**: mostrar la ruta de red hasta un destino

**Cómo funciona**:
- Envía paquetes con un **TTL creciente**
- Cada salto reduce el TTL y devuelve un mensaje **ICMP Time Exceeded**
- Muestra los **routers y la ruta** hasta el destino
- Mide el **tiempo de ida y vuelta (RTT)** de cada salto

**Casos de uso**:
- **Solución de problemas de red**
- **Análisis de rutas**
- **Diagnóstico de latencia**
- **Investigación del peering del proveedor de Internet**

#### Punto de acceso Evil Twin

**Propósito**: crear un punto de acceso WiFi falso que imita SSID existentes

**Cómo funciona**:
- Usa **wlan1** (segunda interfaz WiFi, si está disponible mediante el complemento Pi)
- Clona el **SSID y el tipo de cifrado** de la red objetivo
- **Captura a los clientes** que intenten conectarse
- Muestra un **portal cautivo** para robar credenciales

**Escenario de ataque** (entorno de laboratorio):
1. Busca redes WiFi legítimas
2. Crea un **punto de acceso falso** con el mismo SSID
3. Usa un **ataque de desautenticación** para desconectar a los clientes del punto real
4. Los clientes se reconectan automáticamente al **punto falso**
5. El portal cautivo captura sus credenciales

*Detección: si ambos puntos son visibles a la vez, los clientes ven **SSID duplicados**.*

#### Portal cautivo

**Propósito**: usar plantillas de páginas de phishing para robar credenciales

**Plantillas incluidas**:
- **Página de inicio de sesión WiFi** (estilo genérico de proveedor u hotel)
- **Inicios de sesión de redes sociales** (imitaciones de Facebook, Twitter e Instagram)
- Portales de **inicio de sesión corporativo**
- Páginas WiFi de **aeropuertos y cafeterías**

**Cómo funciona**:
1. El punto de acceso Evil Twin redirige **todo el tráfico** al portal
2. El cliente ve una **página de inicio de sesión**
3. El cliente introduce sus credenciales
4. Las credenciales se **guardan en un archivo**
5. Se permite el acceso a Internet o se muestra un error

**Uso educativo**: demuestra los **riesgos de la ingeniería social** y por qué debes verificar las URL

### 📍 Rastreador GPS y wardriving

#### Funciones GPS

**Fuente GPS**: solo el **complemento Raspberry Pi**
- *El Orbic RCL400 **no tiene GPS integrado**. Sin el complemento Pi no hay datos de ubicación.*
- El Pi conecta un **dongle GPS USB** (se recomienda el chipset U-Blox 7)
- El Pi envía coordenadas al Orbic mediante **archivos de datos compartidos**
- La conversión de **ECEF a latitud y longitud** se realiza automáticamente

**Datos del panel**:
- **Latitud y longitud** en grados decimales
- **Altitud** sobre el nivel del mar
- **Estado de la señal GPS** (precisión)
- **Actualización automática** cada 5 segundos
- **Sin solicitudes de geolocalización del navegador** (no usa la API del navegador)

**Estado GPS compartido**:
- Los datos GPS están disponibles para **todos los procesos de DagShell**
- El modo wardriving usa el GPS automáticamente
- Las funciones no entran en conflicto

#### Modo wardriving

**Propósito**: buscar redes WiFi y guardar sus coordenadas GPS para crear mapas

**Cómo funciona**:
1. Espera una **señal GPS válida** (no registra coordenadas 0,0)
2. Busca redes WiFi cada **5 segundos** en un bucle continuo
3. Registra los datos de red:
   - **SSID** (nombre de red)
   - **BSSID** (dirección MAC)
   - **Tipo de cifrado** (WPA2, WPA3 o abierto)
   - **Intensidad de señal** (RSSI en dBm)
   - **Número de canal**
   - **Coordenadas GPS** (latitud y longitud)
   - **Marca de tiempo**
4. Exporta los datos a un formato **CSV compatible con Wigle**

**Integración con Wigle**:
- **WiGLE** (wigle.net) es un proyecto mundial de mapas WiFi
- El CSV de DagShell se **puede cargar directamente** en WiGLE
- **Carga desde el navegador** en la página Files, sin herramientas externas
- Contribuye a una **base de datos pública** de ubicaciones WiFi

**Casos de uso**:
- **Mapeo de cobertura WiFi**
- **Medición de redes** para proveedores de Internet
- **Análisis de intensidad de señal**
- **Investigación de seguridad** (redes abiertas y cifrado débil)
- **Análisis basado en ubicación**

**Ejemplo de formato CSV**:
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="Modo wardriving de DagShell con coordenadas GPS y redes WiFi analizadas. El CSV compatible con Wigle registra SSID, BSSID, cifrado e intensidad de señal" >}}

### 🥧 Complemento Raspberry Pi

El **complemento Raspberry Pi** amplía las capacidades de DagShell mediante **hardware externo**.

#### Requisitos de hardware

**Mínimos**:
- **Raspberry Pi 3B+** o posterior *(la Pi Zero no suministra suficiente alimentación USB a los periféricos)*
- **Dongle GPS USB** (se recomienda el chipset U-Blox 7)
- **Fuente de alimentación** *(la Pi necesita alimentación propia. El puerto USB del Orbic no suministra suficiente energía)*

**Opcionales**:
- **Adaptador WiFi** (segunda interfaz para escanear sin perder la conexión)
- **Dongle Bluetooth** (si el Bluetooth interno de la Pi tiene poca cobertura)

#### Módulo GPS (U-Blox 7)

**Conexión**: dongle GPS USB conectado a la Pi\
**Protocolo**: sentencias NMEA por serie\
**Conversión**: la Pi convierte ECEF a latitud y longitud automáticamente\
**Compartición de datos**: escribe las coordenadas GPS en un **archivo compartido** del Orbic

**Análisis de sentencias**:
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Time    Latitude   Longitude   Fix Sats  Altitude
```

#### Escaneo Bluetooth (BLE)

**Propósito**: detectar dispositivos Bluetooth cercanos

**Cómo funciona**:
- Busca **anuncios BLE**
- Captura **direcciones MAC**
- Busca el **OUI** para identificar al fabricante
- Registra los resultados en **formato CSV**

**Control remoto**:
- Inicia o detiene el escaneo desde la interfaz web de DagShell
- No hace falta conectarse por SSH a la Pi
- Muestra actualizaciones de estado en tiempo real

**Casos de uso**:
- **Seguimiento y recuento de dispositivos**
- **Análisis del tránsito peatonal**
- **Detección de dispositivos Bluetooth**
- **Investigación de seguridad IoT**

**Salida CSV**:
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### Escaneo WiFi

**Propósito**: la Pi busca redes WiFi y envía los datos al Orbic

**Ventaja**: usa una interfaz dedicada para escanear mientras el **Orbic mantiene el hotspot**

**Cómo funciona**:
- La Pi usa un **segundo adaptador WiFi** o el WiFi integrado, si no lo necesita para conectarse
- Busca en **todos los canales** (1-14 en 2,4 GHz, 36-165 en 5 GHz, si son compatibles)
- Envía los resultados al Orbic mediante almacenamiento compartido
- DagShell registra los datos en el **CSV de wardriving**

**Coordinación**:
- La Pi y el Orbic **sincronizan** la hora del GPS
- Evita entradas duplicadas
- Combina **ambas fuentes de escaneo** en un solo registro

#### Ataques de desautenticación

**Propósito**: desconectar clientes de redes WiFi (para pruebas de laboratorio)

**Cómo funciona**:
- Envía **tramas de desautenticación 802.11**
- Falsifica la **dirección MAC del punto de acceso**
- El cliente recibe una orden de desconexión del punto de acceso
- El cliente **pierde la conexión** e intenta reconectarse

**Métodos de control**:
- **Desautenticación de un solo uso**: ráfaga única de tramas
- **Desautenticación continua**: impide la reconexión (DoS)
- **Control remoto**: se activa desde la página de escaneo de DagShell

**Casos de uso autorizados**:
- **Retirar dispositivos no autorizados** de tu propia red
- **Pruebas de penetración** con permiso
- **Ataques Evil Twin** en un laboratorio (forzar a los clientes a usar el punto falso)

**⚠️ Aviso legal**: Los ataques de desautenticación son **ilegales contra redes que no te pertenecen**. Pueden infringir las normas de la FCC y dar lugar a cargos según la CFAA.

#### Servicio de inicio automático

**Servicio systemd**: el complemento de la Pi se inicia automáticamente al arrancar

**Archivo de servicio** (`/etc/systemd/system/pi-companion.service`):
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**Comandos**:
```bash
# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

#### Base de datos OUI

**Propósito**: buscar el proveedor o fabricante asociado a una dirección MAC

**Base de datos**: API basada en prefijos de la [base de datos maestra OUI](https://standards.ieee.org/products-programs/regauth/)

**Cómo funciona**:
- Extrae los **primeros 3 bytes** de la dirección MAC (prefijo OUI)
- Consulta la API: `api.example.com/oui/A4:83:E7`
- Devuelve el **nombre del fabricante**

**Ejemplo**:
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Integración**: se usa en el escáner ARP, el escáner BLE y el wardriving WiFi

### 📁 Explorador de archivos

**Propósito**: explorar y administrar archivos del dispositivo

**Ubicación**: directorio `/data/` (partición con permisos de escritura)

**Funciones**:
- **Explorar archivos** y subdirectorios
- **Descargar** archivos al ordenador
- **Eliminar** archivos (con confirmación)
- **Ver el tamaño** y la fecha de los archivos

**Archivos comunes**:
- `wardrive_log.csv`: datos de escaneo WiFi
- `bluetooth_scan.csv`: datos de dispositivos BLE
- `gps_track.gpx`: rutas GPS
- `dns_queries.log`: consultas DNS capturadas
- `arp_scan.txt`: lista de dispositivos de red

**Carga a Wigle**:
- **Carga directa desde el navegador** en la página Files
- Se autentica con la cuenta de WiGLE
- Sube el CSV sin descargarlo primero

______

{{< stscollective-ad "rayhunter" >}}

## Guía de instalación

### Requisitos previos

**Hardware**:
- **Hotspot móvil Orbic RCL400**
- **Ordenador** (Windows, macOS o Linux)
- **Cable USB** (si instalas el firmware directamente)

**Software**:
- **Python 3** con los módulos `requests` y `cryptography`
- **Navegador web** (Chrome, Firefox, Edge o Safari)

**Opcionales**:
- **Raspberry Pi 3B+** o posterior (para GPS y funciones ampliadas)
- **Dongle GPS USB** (chipset U-Blox 7)

### Método 1: Webflasher (recomendado)

**Método más sencillo**: no requiere usar la línea de comandos

**Paso 1**: abre DagShell Webflasher
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Paso 2**: genera los certificados PKI
- Pulsa el botón **"Generate Certificates"**
- El navegador genera una **PKI de dos niveles** (certificado raíz CA y certificado del servidor)
- **Descarga los archivos**: `root.der` y `server.der`

**Paso 3**: activa el shell root en Orbic
- Conéctate a la red WiFi del Orbic
- Introduce la **contraseña de administrador** en el formulario web
- Pulsa **"Enable Shell"**
- La página web aprovecha la API del Orbic para abrir un **shell root en el puerto 24**

**Paso 4**: instala el firmware
- Pulsa el botón **"Deploy DagShell"**
- El script carga:
  - `orbic_app` (binario principal del firmware)
  - `root.der` (certificado raíz)
  - `server.der` (certificado TLS del servidor)
  - `dagshell_boot.sh` (script de persistencia)
- La instalación tarda **2 o 3 minutos**

**Paso 5**: reinicia el Orbic
- Apaga y vuelve a encender el dispositivo
- DagShell se inicia automáticamente al arrancar

**Paso 6**: accede a DagShell
- Abre el navegador en: `https://192.168.1.1:8443/`
- Acepta el **aviso de seguridad** (el certificado autofirmado es esperado)
- Inicia sesión con las credenciales predeterminadas, si se solicitan

### Método 2: Instalación manual

Para **usuarios avanzados** que prefieren compilar desde el código fuente.

#### Paso 1: instala las dependencias

**Windows**:
```powershell
# Install Python 3
# Download from python.org

# Install required modules
pip install requests cryptography

# ARM cross-compiler included in gcc_win/ folder
```

**macOS**:
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3

# Install required modules
pip3 install requests cryptography

# ARM toolchain included in gcc_mac/ folder
```

**Linux**:
```bash
# Install Python 3 and pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Install required modules
pip3 install requests cryptography

# Install ARM cross-compiler
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Paso 2: clona el repositorio

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Paso 3: compila el firmware

**Windows**:
```powershell
cd orbic_fw_c
python gen_pki.py          # Generate certificates
.\build.ps1                # Compile firmware
```

**macOS/Linux**:
```bash
cd orbic_fw_c
python3 gen_pki.py         # Generate certificates
./build.sh                 # Compile firmware (auto-builds BearSSL)
```

**Resultado**: `orbic_app` (binario ARM estático) y archivos de certificados DER

**⚠️ Nota para macOS**: la carpeta `gcc_mac/` contiene una cadena de herramientas ARM personalizada, compilada con **crosstool-ng** para usar encabezados de **Linux kernel 3.2**, compatibles con el kernel 3.18 del Orbic. *Los compiladores ARM estándar de Homebrew apuntan a kernels más recientes y **no funcionan**.*

#### Paso 4: activa el shell root en Orbic

```bash
# Connect to Orbic WiFi
# Replace YOUR_ADMIN_PASSWORD with actual password

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Este comando aprovecha la API web de Orbic para abrir un shell root en el **puerto 24**.

#### Paso 5: instala el firmware

```bash
python deploy_base64.py
```

El comando carga e instala:
- `orbic_app` en `/data/orbic_app`
- Los certificados en `/data/root.der` y `/data/server.der`
- El script de arranque en `/etc/rc.d/dagshell_boot.sh`

**Persistencia**: el firmware se inicia automáticamente al reiniciar mediante un script init.

#### Paso 6: reinicia y accede

```bash
# Reboot Orbic (power cycle or via SSH)
reboot

# After reboot, access DagShell
# Browser: https://192.168.1.1:8443/
```

### Aviso del certificado de seguridad

Al acceder a DagShell, verás un aviso **"Not Secure"** o **"Not Trusted"**:

**Navegadores de escritorio**:
- Pulsa **"Advanced"**
- Pulsa **"Proceed to 192.168.1.1 (unsafe)"**

**Navegadores móviles**:
- Pulsa **"Show Details"**
- Pulsa **"visit this website"**

**Por qué ocurre**:
- El certificado es **autofirmado** (no procede de una CA de confianza como Let's Encrypt)
- El dispositivo no tiene el certificado raíz en su almacén de confianza
- *Es un comportamiento **esperado** en firmware personalizado, no una señal de intrusión.*

**¿La conexión es segura?**:
- **Sí**. La conexión está cifrada con **TLS 1.2 o superior**
- Los datos no se pueden interceptar
- *El certificado no está vinculado a una CA pública de confianza, pero el cifrado es real.*

**Opcional**: instala `root.der` en el almacén de confianza del dispositivo para eliminar el aviso.

______

## Configuración del complemento Raspberry Pi

**Opcional, pero muy recomendable** para disponer de todas las funciones.

### Preparación del hardware

**Paso 1**: consigue los componentes
- **Raspberry Pi 3B+** o posterior (35-55 $)
- **Dongle GPS USB** con chipset U-Blox 7 (15-30 $)
- **Tarjeta microSD** de 16 GB o más para Raspberry Pi OS (10 $)
- **Fuente de alimentación** para la Pi (10 $)

**Paso 2**: instala Raspberry Pi OS
```bash
# Download Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# Flash "Raspberry Pi OS Lite" to SD card
# Boot Pi and complete setup
```

**Paso 3**: conecta el dongle GPS
- Conecta el GPS USB a la Pi
- Comprueba si se detecta: `lsusb` (debería aparecer el dispositivo GPS)
- Verifica el puerto serie: `ls /dev/ttyUSB*` o `ls /dev/ttyACM*`

### Instalación del software

**Paso 1**: clona el repositorio de DagShell en la Pi

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Paso 2**: instala las dependencias

```bash
# Update package list
sudo apt-get update

# Install required packages
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Install Python modules
pip3 install pyserial gps3 bluetooth pybluez
```

**Paso 3**: configura el servicio GPS

```bash
# Edit gpsd config
sudo nano /etc/default/gpsd

# Set DEVICES line to your GPS serial port
DEVICES="/dev/ttyUSB0"  # Adjust if different

# Restart gpsd
sudo systemctl restart gpsd

# Test GPS
cgps -s  # Should show satellite data after ~30 seconds
```

**Paso 4**: configura el complemento Pi

```bash
# Edit configuration file
nano pi_companion/config.py

# Set Orbic IP address
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# Set GPS serial port
GPS_DEVICE = "/dev/ttyUSB0"

# Save and exit
```

**Paso 5**: instala el servicio systemd

```bash
# Copy service file
sudo cp pi_companion.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

**Paso 6**: verifica la comunicación

```bash
# Check logs
journalctl -u pi-companion -f

# Should see GPS coordinates being sent to Orbic
```

### Configuración de red

**Opción A**: conexión WiFi

```bash
# Pi connects to Orbic hotspot
# Edit wpa_supplicant config
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Add network
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# Restart WiFi
sudo systemctl restart networking
```

**Opción B**: Ethernet por USB (recomendado)

- Conecta la Pi al Orbic mediante un **cable USB** (puerto USB de la Pi al del Orbic)
- Activa el **modo USB gadget** en la Pi
- La Pi funciona como un **dispositivo Ethernet USB**
- *Es más fiable que WiFi para transferir datos continuamente.*
- La Pi accede a Internet a través del Orbic

**Configuración USB gadget**:
```bash
# Edit config.txt
sudo nano /boot/config.txt

# Add at end
dtoverlay=dwc2

# Edit cmdline.txt
sudo nano /boot/cmdline.txt

# Add after rootwait
modules-load=dwc2,g_ether

# Reboot
sudo reboot
```

______

## Por qué combinar DagShell con RayHunter

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Diagrama comparativo de las herramientas de wardriving WiFi y ataques de red de DagShell frente a la detección de anomalías de protocolos celulares de RayHunter. Ambos funcionan en el mismo hotspot Orbic RCL400" >}}

### Funciones complementarias

**DagShell** y **RayHunter** son herramientas de seguridad **complementarias** que cubren distintos aspectos de la investigación móvil:

| Función | DagShell | RayHunter |
|---------|----------|-----------|
| **Detección de IMSI catchers** | Supervisión básica de torres celulares | Análisis avanzado de patrones |
| **Seguimiento GPS** | Sí (mediante Pi) | Sí (mediante módem) |
| **Wardriving WiFi** | Sí | No |
| **Escaneo Bluetooth** | Sí (mediante Pi) | No |
| **Herramientas de red** | Sí (sniffer DNS, escaneo ARP y de puertos) | No |
| **Herramientas de ataque** | Sí (Evil Twin, portal cautivo y desautenticación) | No |
| **Herramientas de privacidad** | Sí (corrección TTL, suplantación MAC y bloqueo de anuncios) | Mínimas |
| **Base de datos de torres celulares** | Básica | Completa |
| **Análisis de IA y aprendizaje automático** | No | Sí (detección de anomalías) |
| **Análisis de protocolos del operador** | Limitado | Profundo (SS7/Diameter) |

### Casos de uso complementarios

#### 1. **Defensa completa contra IMSI catchers**

**Escenario**: viajar por una zona con vigilancia intensiva

**Función de DagShell**:
- **Supervisa en tiempo real** los cambios de torre celular
- **Registra la ubicación GPS** durante cambios sospechosos
- **Guarda los datos de las torres** para analizarlos más tarde

**Función de RayHunter**:
- **Detecta anomalías mediante aprendizaje automático** en protocolos celulares
- **Inspecciona paquetes SS7/Diameter** para detectar ataques sofisticados
- Compara con una **base de datos de torres conocidas como fiables**

**Resultado conjunto**: DagShell ofrece **supervisión continua** y RayHunter ofrece **análisis detallado**.

#### 2. **Wardriving con seguridad celular**

**Escenario**: mapear redes WiFi en una zona urbana

**Función de DagShell**:
- **Busca redes WiFi** y guarda coordenadas GPS
- Ofrece herramientas de **análisis de red** (intensidad de señal y cifrado)
- Exporta archivos CSV de **Wigle** para crear mapas

**Función de RayHunter**:
- **Registra las torres celulares** durante el recorrido
- **Detecta IMSI catchers** durante el escaneo WiFi
- **Avisa si la seguridad celular está comprometida**

**Resultado conjunto**: wardriving con **conocimiento de la seguridad celular**.

#### 3. **Laboratorio de investigación de seguridad**

**Escenario**: equipo rojo o pruebas de penetración

**Función de DagShell**:
- Usa un **punto de acceso Evil Twin** para probar la seguridad WiFi
- Usa un **portal cautivo** en demostraciones de ingeniería social
- Ejecuta **ataques de desautenticación** para probar la resistencia
- Ofrece herramientas de **reconocimiento de redes**

**Función de RayHunter**:
- **Detecta si alguien te vigila** durante las pruebas
- Informa sobre la **seguridad de torres celulares**
- Ayuda a evitar la **contravigilancia** durante las pruebas

**Resultado conjunto**: herramientas ofensivas con **conocimiento de la defensa**.

#### 4. **Viajes con prioridad en la privacidad**

**Escenario**: periodista o activista en un entorno delicado

**Función de DagShell**:
- Usa **ocultación de TTL** para ocultar el tethering
- Usa **suplantación de MAC** para reducir el seguimiento
- Bloquea rastreadores con **AdBlock**
- Supervisa los **IMSI catchers**

**Función de RayHunter**:
- Ofrece **detección avanzada de IMSI catchers**
- Detecta **ataques a nivel de protocolo**
- Envía **alertas de seguridad celular**

**Resultado conjunto**: privacidad reforzada con **varias capas de protección**.

### Instalación conjunta

**Opción preconfigurada** (la más sencilla):
- Compra en **STS Collective**: [Orbic RCL400 preconfigurado con RayHunter y DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **Listo para usar** al sacarlo de la caja
- Ambas versiones del firmware están **probadas y verificadas**
- **Sin complicaciones de instalación**

**Instalación propia**:
1. **Instala primero RayHunter** (consulta la [guía para instalar RayHunter en dispositivos](/articles/how-to-flash-rayhunter-devices-complete-guide/))
2. **Instala DagShell después** (ambos pueden coexistir)
3. **RayHunter** usa los puertos predeterminados
4. **DagShell** usa el puerto 8443
5. Accede a cada uno en una pestaña distinta del navegador

**Sin conflictos**:
- RayHunter usa los puertos **80/443**
- DagShell usa el puerto **8443**
- No interfieren entre sí
- Funcionan **al mismo tiempo**

¿Prefieres no instalarlo por tu cuenta? El **[Orbic RCL400 con RayHunter y DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** preconfigurado está listo para usar. El código **SIMEONONSECURITY** ofrece hasta un 20 % de descuento en STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra el RCL400 preconfigurado y ahorra un 20 %
{{< /centerbutton >}}

______

## Casos de uso reales

### Caso de uso 1: investigador de seguridad

**Perfil**: especialista en pruebas de penetración que evalúa la seguridad WiFi

**Herramientas de DagShell**:
- **Wardriving WiFi** para mapear las redes de los clientes
- **Escáner ARP** para detectar dispositivos
- **Escáner de puertos** para identificar servicios
- **Evil Twin y portal cautivo** para probar la resistencia a la ingeniería social
- **Explorador de archivos** para extraer resultados

**Flujo de trabajo**:
1. Recorre en coche el perímetro de las instalaciones del cliente
2. Usa wardriving para mapear la cobertura WiFi
3. Crea una imitación Evil Twin de la red del cliente, con permiso
4. Supervisa los intentos de conexión de los clientes
5. Genera un informe con los datos recopilados

**Integración con RayHunter**: ayuda a que no vigilen al investigador durante la evaluación.

### Caso de uso 2: defensor de la privacidad

**Perfil**: periodista que viaja al extranjero

**Herramientas de DagShell**:
- **Corrección TTL** para evitar restricciones del operador
- **Suplantación de MAC** para reducir la identificación del dispositivo
- **Detector de IMSI catchers** para detectar posibles actividades de vigilancia
- **Sniffer DNS** para comprobar que ningún dispositivo filtre datos
- **AdBlock** para impedir el rastreo

**Flujo de trabajo**:
1. Activa la corrección TTL antes de usar el dispositivo
2. Aleatoriza la dirección MAC
3. Mantén activo el detector de IMSI catchers
4. Usa AdBlock en todos los dispositivos conectados
5. Registra la actividad celular sospechosa

**Integración con RayHunter**: detecta IMSI catchers con más precisión que la supervisión básica.

### Caso de uso 3: administrador de redes

**Perfil**: administrador de TI a cargo de varias instalaciones

**Herramientas de DagShell**:
- **Wardriving WiFi** para comprobar la cobertura
- **Escáner ARP** para inventariar dispositivos
- **Escáner de puertos** para auditorías de seguridad
- **Monitor de conexiones activas** para detectar tráfico no autorizado
- **Gestor de firewall** para bloquear IP

**Flujo de trabajo**:
1. Recorre las instalaciones para validar la cobertura WiFi
2. Escanea con ARP para detectar todos los dispositivos de red
3. Busca servicios expuestos en los servidores mediante un escaneo de puertos
4. Bloquea IP maliciosas con el firewall
5. Exporta informes para documentar el trabajo

**Integración con RayHunter**: supervisa la seguridad celular en instalaciones con dispositivos móviles.

### Caso de uso 4: investigador de seguridad IoT

**Perfil**: investigador que analiza la seguridad de dispositivos IoT

**Herramientas de DagShell**:
- **Escáner ARP** con búsqueda OUI para identificar dispositivos IoT
- **Escáner de puertos** para encontrar servicios abiertos
- **Sniffer DNS** para capturar patrones de tráfico IoT
- **Escáner Bluetooth** (Pi) para dispositivos IoT BLE
- **Traceroute** para analizar la conectividad

**Flujo de trabajo**:
1. Instala Orbic y Pi en un entorno de pruebas
2. Escanea con ARP para detectar dispositivos IoT
3. Busca servicios vulnerables mediante un escaneo de puertos
4. Escanea BLE para detectar dispositivos IoT Bluetooth
5. Analiza consultas DNS para observar el comportamiento de conexión con servidores externos
6. Documenta las vulnerabilidades

**Integración con RayHunter**: detecta si los dispositivos IoT tienen conectividad celular y supervisa anomalías.

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Diagrama de cuatro casos de uso de DagShell y RayHunter: investigación de seguridad, defensa de la privacidad, administración de redes e investigación IoT" >}}

______

## Consideraciones legales y éticas

### Marco legal

**Herramientas como DagShell operan en un terreno legal complejo**:

**Usos legales**:
✅ **Tus propias redes**: prueba tus dispositivos y redes\
✅ **Pruebas autorizadas**: realiza pruebas de penetración con permiso por escrito\
✅ **Fines educativos**: aprende en laboratorios aislados\
✅ **Protección de privacidad**: usa la corrección TTL y la suplantación de MAC en tu dispositivo\
✅ **Investigación de seguridad**: investiga vulnerabilidades y comunícalas de forma responsable

**Usos ilegales**:
❌ **Acceso no autorizado**: atacar redes ajenas (infracción de la CFAA)\
❌ **Ataques de desautenticación** contra otras redes (infracción de la FCC y posible delito grave)\
❌ Ataques **Evil Twin** contra el público (fraude electrónico y robo de identidad)\
❌ **Interceptar DNS** de otras personas sin consentimiento (interceptación ilegal de comunicaciones)\
❌ **Eludir controles de seguridad** para cometer fraude

### Leyes que debes conocer

**Estados Unidos**:
- **Computer Fraud and Abuse Act (CFAA)**: acceso no autorizado a ordenadores y redes
- **Wiretap Act**: interceptación de comunicaciones electrónicas
- **Normas de la FCC**: interferencia de radiofrecuencia (ataques de desautenticación)

**Reino Unido**:
- **Computer Misuse Act 1990**: ley similar a la CFAA
- **Regulation of Investigatory Powers Act (RIPA)**: restricciones sobre interceptación

**Unión Europea**:
- **RGPD**: protección de datos (escaneo WiFi o BLE que recopila datos identificables)
- *Las normas locales varían entre países y su aplicación también difiere.*

### Pautas éticas

**Haz lo siguiente**:
- ✅ Usa las herramientas en **tus propios dispositivos y redes**
- ✅ Obtén **permiso por escrito** antes de probar sistemas ajenos
- ✅ Practica la **divulgación responsable** si encuentras vulnerabilidades
- ✅ Limita el **uso educativo** a entornos controlados
- ✅ Protege **tu propia privacidad**

**Evita lo siguiente**:
- ❌ Atacar redes ajenas
- ❌ Robar credenciales de desconocidos
- ❌ Interferir con infraestructuras críticas
- ❌ Usar las herramientas con fines maliciosos
- ❌ Distribuir datos capturados

### Declaración de uso responsable

DagShell es una **herramienta de investigación de seguridad y privacidad**. Sus capacidades se parecen a las de herramientas profesionales de pruebas de penetración, como **Kali Linux**, **WiFi Pineapple** o **HackRF**.

**La intención importa**: tanto los **hackers maliciosos** como los **profesionales de seguridad** usan herramientas similares. La diferencia está en:
- **Autorización** (permiso para realizar pruebas)
- **Intención** (mejorar la seguridad o causar daño)
- **Divulgación** (informar de los hallazgos o explotarlos)

Usa DagShell de forma **responsable** y **ética**. *Si no sabes si una acción es legal, detente y consulta a un abogado antes de continuar.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Marco legal y ético para la investigación de seguridad con DagShell. Muestra usos autorizados y no autorizados y las leyes pertinentes" >}}

______

## Solución de problemas

### Problemas de instalación

**Problema**: `enable_shell.py` no logra conectarse

**Soluciones**:
- Comprueba que estés conectado al **WiFi del Orbic**
- Verifica que la dirección IP sea **192.168.1.1** (predeterminada)
- Vuelve a probar la contraseña de administrador (distingue mayúsculas y minúsculas)
- Comprueba si el puerto 80 está accesible: `telnet 192.168.1.1 80`

**Problema**: falla la carga del firmware

**Soluciones**:
- Asegúrate de haber activado primero el shell root (debe funcionar `enable_shell.py`)
- Comprueba la estabilidad de la red (usa una conexión por cable si es posible)
- Prueba `deploy_net.py` en lugar de `deploy_base64.py`
- Comprueba que haya espacio en la partición `/data`: `df -h /data`

**Problema**: el aviso del certificado no desaparece

**Soluciones**:
- *Es **normal** con certificados autofirmados. La conexión sigue cifrada.*
- Pulsa "Advanced" y luego "Proceed anyway" cada vez
- **Opcional**: instala `root.der` en el almacén de confianza del dispositivo (opción avanzada)

### Problemas durante el uso

**Problema**: DagShell no se inicia al arrancar

**Soluciones**:
- Comprueba el script de arranque: `ls -la /etc/rc.d/dagshell_boot.sh`
- Verifica que sea ejecutable: `chmod +x /etc/rc.d/dagshell_boot.sh`
- Revisa los registros: `logread | grep dagshell`
- Inícialo manualmente: `/data/orbic_app &`

**Problema**: el GPS no funciona

**Soluciones**:
- Verifica que el **complemento Pi** esté activo: `systemctl status pi-companion`
- Comprueba si el GPS tiene señal de satélite: `cgps -s` (en la Pi)
- Asegúrate de que el dongle GPS esté conectado: `lsusb`
- *Espera entre 5 y 10 minutos para obtener la señal GPS inicial. El primer arranque tarda más al aire libre.*

**Problema**: el wardriving no registra datos

**Soluciones**:
- Espera a que el GPS obtenga señal antes de empezar
- Comprueba que `/data` tenga permisos de escritura
- Verifica que se cree el archivo CSV: `ls -la /data/wardrive_log.csv`
- Comprueba que la interfaz WiFi esté activa: `ifconfig wlan0`

**Problema**: el complemento Pi no se comunica con el Orbic

**Soluciones**:
- Verifica la conexión de red: `ping 192.168.1.1`
- Comprueba que la dirección IP del archivo de configuración sea correcta
- Asegúrate de que el puerto 8443 esté abierto: `telnet 192.168.1.1 8443`
- Revisa los registros del complemento Pi: `journalctl -u pi-companion`

### Problemas de rendimiento

**Problema**: la interfaz web va lenta o se bloquea

**Soluciones**:
- Borra la caché del navegador
- Desactiva las extensiones del navegador (los bloqueadores de anuncios interfieren)
- Conecta el Orbic **por cable** en lugar de usar WiFi
- Reinicia DagShell: `killall orbic_app && /data/orbic_app &`

**Problema**: los escaneos de wardriving tardan demasiado

**Soluciones**:
- Aumenta el intervalo de escaneo en la configuración (reduce la frecuencia para mejorar el rendimiento)
- Reduce el número de canales analizados
- *Una señal GPS débil ralentiza los escaneos. El sistema espera coordenadas válidas antes de registrar datos.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="Flujo de solución de problemas de DagShell con fallos habituales de instalación, GPS y wardriving y sus soluciones paso a paso" >}}

______

## Configuración avanzada

### Personalizar DagShell

**Modificar el código fuente**:
- Edita los archivos del directorio `orbic_fw_c/`
- Vuelve a compilar con `build.sh` o `build.ps1`
- Instala de nuevo el firmware

**Añadir páginas personalizadas**:
- DagShell integra HTML en el código C++
- Edita `main.cpp` para añadir rutas
- Vuelve a compilar e instalar

**Certificado personalizado**:
- Genera tu propia PKI con `gen_pki.py`
- También puedes crear certificados con **OpenSSL**
- Sustituye `root.der` y `server.der`

### Integración con otras herramientas

**Exportar datos a Wireshark**:
```bash
# Capture pcap file
tcpdump -i wlan0 -w /data/capture.pcap

# Download via file browser
# Open in Wireshark on PC
```

**Importar rutas GPS a QGIS**:
```bash
# Export GPX format
python gps_to_gpx.py /data/gps_coords.txt

# Import to QGIS as vector layer
```

**Sincronizar con una base de datos externa**:
```python
# Custom script to upload wardrive data to MySQL
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### Ajuste del rendimiento

**Optimizar la velocidad de escaneo**:
```bash
# Edit wardrive scan interval
# In DagShell web UI, change from 5s to 3s for faster scanning
# Trade-off: Higher CPU usage, potential missed networks
```

**Optimizar la batería** (si usas una batería externa):
```bash
# Reduce screen brightness on Orbic
# Disable unused features (BT, GPS when not needed)
# Use sleep mode between wardrive sessions
```

______

## Comparación con alternativas

### DagShell frente a WiFi Pineapple

| Función | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **Precio** | 60-80 $ más el dispositivo | 99-299 $ |
| **Conexión celular** | ✅ 4G LTE integrado | ❌ No (solo WiFi) |
| **GPS** | ✅ Mediante el complemento Pi | ⚠️ Mediante dongle USB |
| **Evil Twin** | ✅ Sí | ✅ Sí |
| **Portal cautivo** | ✅ Sí | ✅ Sí |
| **Desautenticación** | ✅ Sí (mediante Pi) | ✅ Sí |
| **Wardriving** | ✅ Sí | ✅ Sí |
| **Detección IMSI** | ✅ Básica | ❌ No |
| **Portabilidad** | ✅ Muy portátil | ⚠️ Moderada |
| **Batería** | ✅ Integrada | ⚠️ Requiere una externa |
| **Curva de aprendizaje** | Moderada | Baja (interfaz pulida) |

**Ganador**: DagShell para **seguridad celular móvil**, mientras que Pineapple sirve para pruebas **centradas en WiFi** con una interfaz sencilla.

### DagShell frente a Kali Linux en Pi

| Función | DagShell | Kali en Pi |
|---------|----------|-----------|
| **Tiempo de configuración** | 15 minutos | 2-3 horas |
| **LTE celular** | ✅ Integrado | ❌ Requiere módem USB |
| **Interfaz web** | ✅ Sí | ⚠️ Limitada (requiere VNC o SSH) |
| **Número de herramientas** | ~15 | 600+ |
| **Especialización** | Seguridad móvil | Pruebas de penetración generales |
| **Portabilidad** | ✅ Cabe en el bolsillo | ⚠️ Requiere pantalla y alimentación |
| **Duración de batería** | 8-10 horas | 2-4 horas |

**Ganador**: DagShell para tareas **específicas de dispositivos móviles**, mientras que Kali ofrece un kit de herramientas **más amplio**.

### DagShell frente al firmware original de Orbic

| Función | DagShell | Firmware original |
|---------|----------|-------------------|
| **Herramientas de seguridad** | ✅ Amplias | ❌ Ninguna |
| **Funciones de privacidad** | ✅ Sí | ❌ Mínimas |
| **Personalización** | ✅ Total | ❌ Bloqueada |
| **Wardriving** | ✅ Sí | ❌ No |
| **GPS** | ✅ Sí (mediante Pi) | ❌ No |
| **Código abierto** | ✅ Sí | ❌ Propietario |
| **Asistencia** | ⚠️ Comunidad | ✅ Oficial |
| **Estabilidad** | ⚠️ Beta | ✅ Producción |

**Ganador**: DagShell para **investigadores**, mientras que el firmware original sirve para el **uso cotidiano**.

______

## Conclusión: el laboratorio móvil definitivo

**DagShell** convierte el **hotspot Orbic RCL400** en un **laboratorio móvil de seguridad**, con:

✅ **Protección de privacidad** (ocultación TTL, suplantación MAC y bloqueo de anuncios)\
✅ **Supervisión de redes** (conexiones, DNS y enrutamiento)\
✅ **Herramientas de hacking** (detección IMSI, escaneo de puertos y descubrimiento ARP)\
✅ **Capacidades de ataque** (Evil Twin, portal cautivo y desautenticación)\
✅ **Wardriving GPS** con integración de Wigle\
✅ **Ampliación con Raspberry Pi** (BLE, WiFi y GPS)\
✅ **Portátil y con alimentación por batería**\
✅ **Código abierto y personalizable**

### Al combinarlo con RayHunter

**RayHunter y DagShell** forman una **plataforma completa de seguridad móvil**:
- **RayHunter** detecta IMSI catchers mediante análisis avanzado
- **DagShell** aporta herramientas ofensivas y de privacidad
- Ambos funcionan **a la vez** en el mismo dispositivo
- Sus funciones **se complementan sin duplicarse**
- Un **solo equipo portátil** cubre varias tareas de seguridad móvil

### Empieza hoy

**Opción 1: preconfigurado** (la más sencilla)
- **STS Collective**: [Orbic RCL400 con RayHunter y DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- Llega **listo para usar**
- Sin complicaciones de instalación
- Configurado por profesionales

**Opción 2: instalación propia**
- Sigue esta guía
- Es **gratis** si ya tienes un Orbic RCL400
- Aprende el proceso de instalación
- Personalízalo a tu medida

### Lecturas relacionadas

- **[Cómo instalar RayHunter en dispositivos: guía completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)**: instala RayHunter primero
- **[Comparación de dispositivos RayHunter: análisis completo](/articles/rayhunter-device-comparison-2026-complete-review/)**: elige tu plataforma
- **[Proyecto Flock-You: guía de hardware contra la vigilancia](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**: más herramientas de detección

### Reflexiones finales

DagShell ofrece una plataforma **portátil, completa y asequible** para la seguridad móvil, tanto a **investigadores de seguridad** como a **especialistas en pruebas de penetración**, **defensores de la privacidad** y **administradores de redes**.

**Aviso**: úsalo con responsabilidad. Prueba solo redes y dispositivos que te pertenezcan o para los que tengas permiso explícito por escrito. Respeta la ley y la ética. ¡Feliz hacking! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Hotspot Orbic RCL400 con firmware DagShell como laboratorio portátil completo de investigación de seguridad móvil" >}}

______

## Referencias

1. [Repositorio de DagShell en GitHub](https://github.com/dagnazty/DagShell)
2. [Documentación de DagShell](https://dagnazty.github.io/DagShell/)
3. [STS Collective: dispositivos preconfigurados](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE: proyecto de mapas WiFi](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Documentación oficial de Raspberry Pi](https://www.raspberrypi.org/documentation/)
7. [Documentación del módulo GPS U-Blox](https://www.u-blox.com/)
8. [Base de datos OUI: estándares IEEE](https://standards.ieee.org/products-programs/regauth/)
9. [Tutorial de iptables](https://www.netfilter.org/documentation/)
10. [Documentación de OpenSSL](https://www.openssl.org/docs/)
