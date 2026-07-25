---
title: "Firmware personalizado DagShell para Orbic RCL400: Guía completa de instalación y uso 2026"
date: 2026-05-28
toc: true
draft: false
description: "Guía completa del firmware personalizado DagShell para el hotspot Orbic RCL400, incluyendo instalación, herramientas de privacidad, funciones de hacking, capacidades de wardriving y por qué se combina perfectamente con RayHunter para investigación de seguridad móvil."
genre: ["Firmware personalizado", "Seguridad móvil", "Herramientas de privacidad", "Seguridad de red", "Wardriving", "Pruebas de penetración", "Hacking IoT", "Investigación de seguridad", "Hacking de hardware", "Tecnología de privacidad"]
tags: ["DagShell", "Orbic RCL400", "Firmware personalizado", "Hacking hotspot", "Herramientas de privacidad", "Corrección TTL", "Suplantación MAC", "Detección IMSI Catcher", "Wardriving", "Seguimiento GPS", "Ataque Evil Twin", "Portal cautivo", "Sniffer DNS", "Escáner ARP", "Escáner de puertos", "Raspberry Pi Companion", "Seguridad WiFi", "Hotspot móvil", "Monitoreo de red", "Pruebas de penetración", "Investigación de seguridad", "Escaneo Bluetooth", "Ataque Deauth", "Escaneo WiFi", "Búsqueda OUI", "Subida Wigle", "Monitoreo de torre celular", "Comandos AT", "Gestor de firewall", "AdBlock", "Cifrado TLS", "Integración RayHunter", "STS Collective", "Laboratorio de seguridad móvil", "Análisis de red", "Firmware de privacidad", "Seguridad de código abierto", "Compilación cruzada ARM", "Linux embebido", "Kit de herramientas de seguridad", "Herramientas hacker", "Red Team", "Reconocimiento de red"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Una ilustración de un hotspot móvil Orbic RCL400 con una interfaz verde brillante, rodeada de representaciones abstractas de herramientas de seguridad como gráficos y mapas, sobre un fondo azul marino oscuro."
coverCaption: ""
---

**Transforme su Orbic RCL400 en un laboratorio de investigación de seguridad móvil**

## Introducción: Un hotspot para hackers

**DagShell** es un firmware personalizado de código abierto para el **hotspot móvil Orbic RCL400** que transforma un dispositivo celular ordinario en un **kit de herramientas portátil de investigación de seguridad y privacidad**. Creado por el investigador de seguridad "dag", este firmware de estilo terminal proporciona **herramientas de hacking, funciones de privacidad y capacidades de monitoreo de red** en una elegante interfaz hacker de verde sobre negro.

Esta guía completa cubre:
- **Qué es DagShell** y su conjunto completo de características
- Instrucciones de **instalación paso a paso** (métodos de webflasher y manual)
- **Todas las herramientas y capacidades** explicadas en detalle
- Configuración del **Raspberry Pi companion** para funcionalidad extendida
- **Por qué combinar DagShell con RayHunter** para seguridad móvil completa
- **Casos de uso del mundo real** para investigadores de seguridad y defensores de la privacidad
- **Consideraciones legales y éticas**

**En resumen**: DagShell + RayHunter en Orbic RCL400 = **Laboratorio de seguridad móvil completo** para detección de IMSI catchers, wardriving, análisis de red y protección de privacidad.

**Dispositivos pre-flasheados disponibles**: Este artículo es patrocinado por **STS Collective**, que ofrece hotspots Orbic RCL400 pre-flasheados con **RayHunter y DagShell** preinstalados y listos para usar: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Descuento exclusivo para lectores**: Ahorre hasta un 20% en productos de STS Collective, incluidos dispositivos Orbic RCL400 pre-flasheados. Use el código **SIMEONONSECURITY** al pagar o [compre con el descuento aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

______

## ¿Qué es DagShell?

### Descripción general

**DagShell** es un firmware personalizado de código abierto que reemplaza la interfaz web estándar de Orbic RCL400 con un **kit de herramientas de seguridad completo** que incluye:

- **Interfaz de estilo terminal** con arte ASCII y estética hacker
- Interfaz web **cifrada con TLS 1.2+** (certificado autofirmado)
- **Herramientas de protección de privacidad** (enmascaramiento TTL, suplantación MAC, bloqueo de anuncios DNS)
- **Monitoreo de red** (conexiones activas, tablas de enrutamiento, consultas DNS)
- **Herramientas de hacking** (detección de IMSI catchers, escaneo de puertos, descubrimiento ARP)
- **Capacidades de ataque** (Evil Twin AP, phishing de portal cautivo, ataques deauth)
- **Seguimiento GPS y wardriving** con exportación CSV compatible con Wigle
- **Raspberry Pi companion** para GPS, escaneo Bluetooth y reconocimiento WiFi
- **Acceso al sistema de archivos** con gestor de archivos basado en navegador
- **Funcionalidad SMS** via comandos AT
- **Persistencia** - Inicio automático en el arranque

### Especificaciones técnicas

**Plataforma**: Hotspot móvil Orbic RCL400
**Arquitectura**: ARM Linux (kernel 3.18)
**Lenguaje**: C/C++ (binario ARM estático)
**Cifrado**: TLS 1.2+ con certificados autofirmados (PKI de 2 niveles)
**Servidor web**: Servidor HTTPS embebido personalizado (puerto 8443)
**Interfaz**: IU de terminal basada en navegador
**Licencia**: MIT (código abierto)
**GitHub**: [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

______

## Desglose completo de características

### Suite de protección de privacidad

#### Corrección TTL

**Propósito**: Enmascarar el tráfico del hotspot de la detección del operador

**Cómo funciona**:
- Modifica el valor **Time To Live (TTL)** en los paquetes IP a **65**
- Los operadores detectan el tethering por decrementos de TTL (teléfono=64, dispositivo conectado=63)
- Configurar TTL a 65 hace que **todo el tráfico parezca local**

**Caso de uso**: Evitar restricciones/throttling de tethering del operador

#### Suplantación de dirección MAC

**Propósito**: Aleatorizar la dirección MAC del dispositivo por privacidad

**Cómo funciona**:
- Cambia la dirección MAC de **wlan0** (interfaz WiFi)
- Genera una **MAC aleatoria** o permite entrada personalizada
- Hace el dispositivo **no rastreable** entre sesiones

#### Bloqueo de anuncios basado en DNS

**Propósito**: Bloquear anuncios y rastreo a nivel DNS

**Cómo funciona**:
- Modifica el archivo `/etc/hosts` con una **lista de bloqueo**
- Los dominios en la lista se resuelven a **127.0.0.1** (localhost)
- Bloquea anuncios **para todos los dispositivos conectados**

### Herramientas de hacking

#### Detector de IMSI Catcher

**Propósito**: Monitorear información de torres celulares para detectar anomalías que indiquen dispositivos **IMSI catcher/Stingray**

**Indicadores de detección**:
- **Cambio repentino de torre celular** mientras está estacionario
- **Degradación a 2G** *(los IMSI catchers a menudo fuerzan 2G para eliminar el cifrado)*
- **ID de celda desconocida** que aparece
- **Señal débil** de la torre falsa
- **Reconexiones frecuentes**

#### Escáner de puertos

**Propósito**: Escanear direcciones IP objetivo en busca de puertos abiertos

**Casos de uso**:
- **Reconocimiento de red**
- **Descubrimiento de dispositivos IoT**
- **Auditoría de seguridad** de redes locales

### Herramientas de ataque

**AVISO LEGAL IMPORTANTE**: Estas herramientas son solo para **pruebas de seguridad autorizadas**. Usarlas contra redes que no son de su propiedad o para las que no tiene permiso escrito explícito es **ILEGAL** en la mayoría de las jurisdicciones.

#### Sniffer DNS

**Propósito**: Registrar consultas DNS de clientes conectados

*Esto captura metadatos (dominios visitados) de clientes conectados. Despliéguelo solo en redes que posea o administre.*

#### Escáner ARP

**Propósito**: Descubrir dispositivos en la red local

#### Evil Twin AP

**Propósito**: Crear un punto de acceso WiFi falso que clone SSIDs existentes

Use estos escenarios de ataque solo en **entornos de laboratorio**.

#### Portal cautivo

**Propósito**: Plantillas de páginas de phishing para captura de credenciales

**Propósito educativo**: Demuestra **riesgos de ingeniería social** y por qué los usuarios deben verificar las URL

### Rastreador GPS y wardriving

#### Funcionalidad GPS

**Fuente GPS**: **Solo Raspberry Pi companion**
- El Orbic RCL400 **no tiene GPS integrado**
- El Pi conecta un **dongle USB GPS** (chipset U-Blox 7)

#### Modo wardriving

**Propósito**: Escanear redes WiFi con coordenadas GPS para mapear

**Integración Wigle**:
- El CSV de DagShell es **directamente subible a WiGLE**
- Contribuye a la **base de datos pública** de ubicaciones WiFi

**Ejemplo de formato CSV**:
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

### Raspberry Pi Companion

El **Raspberry Pi companion** extiende las capacidades de DagShell con **hardware externo**:

#### Requisitos de hardware

**Mínimo**:
- **Raspberry Pi 3B+** o más nuevo
- **Dongle USB GPS** (chipset U-Blox 7 recomendado)
- **Fuente de alimentación** *(el Pi requiere alimentación separada)*

______

## Guía de instalación

### Método 1: Webflasher (recomendado)

**Método más sencillo** - No se requiere línea de comandos

**Paso 1**: Visitar el Webflasher de DagShell
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Paso 2**: Generar certificados PKI
- Haga clic en el botón **"Generate Certificates"**
- El navegador genera una **PKI de 2 niveles** (CA raíz + certificado de servidor)
- **Descargue los archivos**: `root.der` y `server.der`

**Paso 3**: Habilitar shell root en Orbic
- Conéctese a la red WiFi de Orbic
- Ingrese la **contraseña de administrador** en el formulario web
- Haga clic en **"Enable Shell"**

**Paso 4**: Desplegar el firmware
- Haga clic en el botón **"Deploy DagShell"**

**Paso 5**: Reiniciar Orbic
- Apague y encienda el dispositivo
- DagShell se inicia automáticamente al arrancar

**Paso 6**: Acceder a DagShell
- Abra el navegador en: `https://192.168.1.1:8443/`
- Acepte la **advertencia de seguridad** (certificado autofirmado, esto es esperado)

### Método 2: Instalación manual

**Para usuarios avanzados** que quieren construir desde el código fuente

#### Paso 1: Instalar dependencias

**macOS**:
```bash
brew install python3
pip3 install requests cryptography
```

**Linux**:
```bash
sudo apt-get install python3 python3-pip
pip3 install requests cryptography
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Paso 2: Clonar el repositorio

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Paso 3: Construir el firmware

```bash
cd orbic_fw_c
python3 gen_pki.py
./build.sh
```

#### Paso 4: Habilitar shell root en Orbic

```bash
python enable_shell.py SU_CONTRASEÑA_ADMIN
```

#### Paso 5: Desplegar el firmware

```bash
python deploy_base64.py
```

#### Paso 6: Reiniciar y acceder

```bash
reboot
# Navegador: https://192.168.1.1:8443/
```

______

## ¿Por qué combinar DagShell con RayHunter?

### Capacidades complementarias

| Característica | DagShell | RayHunter |
|----------------|----------|-----------|
| **Detección IMSI Catcher** | Monitoreo básico de torres | Análisis avanzado de patrones |
| **Seguimiento GPS** | Sí (via Pi) | Sí (via módem) |
| **WiFi Wardriving** | Sí | No |
| **Escaneo Bluetooth** | Sí (via Pi) | No |
| **Herramientas de red** | Sí | No |
| **Herramientas de ataque** | Sí | No |
| **Herramientas de privacidad** | Sí | Mínimo |

______

## Casos de uso del mundo real

### Caso 1: Investigador de seguridad

**Perfil**: Probador de penetración realizando evaluación de seguridad WiFi

**Flujo de trabajo con DagShell**:
1. Conducir alrededor del perímetro de las instalaciones del cliente
2. Wardriving para mapear la cobertura WiFi
3. Crear Evil Twin de la red del cliente (con permiso)
4. Monitorear intentos de conexión de clientes
5. Generar informe con datos recopilados

### Caso 2: Defensor de la privacidad

**Perfil**: Periodista viajando internacionalmente

**Flujo de trabajo con DagShell**:
1. Activar la corrección TTL antes de usar el dispositivo
2. Aleatorizar la dirección MAC
3. Monitorear continuamente el detector de IMSI catchers
4. Usar AdBlock para todos los dispositivos conectados
5. Registrar actividad celular sospechosa

______

## Consideraciones legales y éticas

### Marco legal

**Usos legales**:
- Sus propias redes
- Pruebas autorizadas con permiso escrito
- Fines educativos en entornos de laboratorio aislados
- Protección de privacidad en su dispositivo

**Usos ilegales**:
- Acceso no autorizado a redes (violación CFAA en EE.UU.)
- Ataques deauth en redes ajenas (violación FCC)
- Ataques Evil Twin contra el público

### Uso responsable

DagShell es una **herramienta de investigación de seguridad y privacidad**. Úsela de manera **responsable** y **ética**. *Si no está seguro de si algo es legal, deténgase y consulte a un abogado antes de continuar.*

______

## Conclusión: El laboratorio móvil definitivo

**DagShell** transforma el modesto **hotspot Orbic RCL400** en un **poderoso laboratorio de seguridad móvil** que combina:

- Protección de privacidad (enmascaramiento TTL, suplantación MAC, AdBlock)
- Monitoreo de red (conexiones, DNS, enrutamiento)
- Herramientas de hacking (detección IMSI, escaneo de puertos, descubrimiento ARP)
- Capacidades de ataque (Evil Twin, portal cautivo, deauth)
- Wardriving GPS con integración Wigle
- Expansión Raspberry Pi (BLE, WiFi, GPS)
- Portátil y con batería integrada
- Código abierto y personalizable

Ya sea un **investigador de seguridad**, **probador de penetración**, **defensor de la privacidad** o **administrador de red**, DagShell proporciona una plataforma **portable, potente y asequible** para el trabajo de seguridad móvil.

**Aviso legal**: Use de manera responsable. Solo pruebe redes y dispositivos que posea o para los que tenga permiso escrito explícito.

______

## Referencias

1. [DagShell GitHub Repository](https://github.com/dagnazty/DagShell)
2. [DagShell Documentation](https://dagnazty.github.io/DagShell/)
3. [STS Collective - Pre-Flashed Devices](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE - WiFi Mapping Project](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Raspberry Pi Official Documentation](https://www.raspberrypi.org/documentation/)
7. [U-Blox GPS Module Documentation](https://www.u-blox.com/)
8. [OUI Database - IEEE Standards](https://standards.ieee.org/products-programs/regauth/)
9. [iptables Tutorial](https://www.netfilter.org/documentation/)
10. [OpenSSL Documentation](https://www.openssl.org/docs/)
