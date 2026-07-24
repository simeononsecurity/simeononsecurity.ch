---
title: "Guía Definitiva: Instalar GrapheneOS en tu Google Pixel"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Aprende a instalar GrapheneOS en tu Google Pixel para mayor privacidad y seguridad usando el instalador web o el método de línea de comandos."
tags: ["GrapheneOS", "Google Pixel", "privacidad", "seguridad", "Android", "dispositivos móviles", "sistema operativo", "guía de instalación", "ROM personalizada", "centrado en privacidad", "protección de datos", "SO seguro", "código abierto", "seguridad del dispositivo", "funciones de privacidad", "datos personales", "privacidad móvil", "privacidad digital", "personalización de dispositivo", "tecnología", "fastboot", "bootloader", "arranged boot", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "Una ilustración digital abstracta de un smartphone Google Pixel conectado a un ordenador mediante un cable USB-C, rodeado de elementos gráficos que representan la transferencia de datos y la seguridad."
coverCaption: ""
---

**Cómo instalar GrapheneOS en tu Google Pixel**

GrapheneOS es un sistema operativo de código abierto centrado en la privacidad basado en Android. Ofrece un endurecimiento de seguridad y protecciones de privacidad significativamente mejorados, lo que lo convierte en una excelente opción para cualquier persona preocupada por la privacidad y seguridad de datos. Si tienes un dispositivo Google Pixel compatible y quieres cambiar a GrapheneOS, esta guía cubre tanto el método de **instalador web** recomendado como el método tradicional de **línea de comandos (CLI)**.

> **Consejo:** Si tienes problemas con el proceso de instalación, pide ayuda en el [canal de chat oficial de GrapheneOS](https://grapheneos.org/contact#community). Antes de pedir ayuda, intenta seguir la guía por tu cuenta y luego pregunta específicamente donde te quedes atascado.

## Requisitos previos

### Requisitos de hardware y sistema

- Un ordenador con al menos **2 GB de memoria libre** y **32 GB de espacio de almacenamiento libre**.
- Un **cable USB-C de alta calidad** incluido con el dispositivo (o un cable USB-C a USB-A si es necesario). Evita los hubs USB — conecta directamente a un puerto trasero de escritorio o puerto de laptop.
- Instalar desde una máquina virtual **no se recomienda** debido a la transmisión USB poco fiable.

> Es una buena práctica actualizar tu dispositivo Pixel antes de instalar GrapheneOS para tener el firmware más reciente. De todas formas, GrapheneOS flashea el firmware más reciente al inicio del proceso de instalación.

### Sistemas operativos oficialmente soportados

#### Instalador web

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (seguir instrucciones de Ubuntu 22.04 LTS), Linux Mint 22 (seguir instrucciones de Ubuntu 24.04 LTS)
- Linux Mint Debian Edition 6 (seguir instrucciones de Debian 12)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15 y 16 con certificación Play Protect

#### Método CLI

Todos los anteriores excepto ChromeOS, GrapheneOS y Android (que solo pueden usar el instalador web).

Las versiones más antiguas en fin de vida de estas plataformas también pueden usarse pero no están oficialmente soportadas. **Asegúrate de que tu sistema operativo esté actualizado antes de continuar.**

### Navegadores oficialmente soportados (solo instalador web)

- **Chromium** (fuera de Ubuntu — su paquete Snap carece de WebUSB funcional)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (con Brave Shields desactivado — limita el uso del almacenamiento para evitar el fingerprinting)

> - En Android, **desactiva el modo escritorio** en tu navegador. El modo escritorio impide que el instalador web detecte Android y solicite permiso de reconexión tras los reinicios. Está activado por defecto en tablets grandes con 8 GB+ de RAM (p. ej., Pixel Tablet).
> - Evita las versiones Flatpak y Snap del navegador — causan problemas durante la instalación.
> - **No** uses el modo incógnito/navegación privada — estos modos restringen el espacio de almacenamiento necesario para extraer la versión descargada.

### Dispositivos soportados

Necesitas uno de los [dispositivos Pixel oficialmente soportados](https://grapheneos.org/faq#supported-devices). **Evita las variantes de operador** — los Pixel de operador tienen un carrier ID no nulo flasheado en fábrica que deshabilita el desbloqueo del bootloader. Consigue un dispositivo independiente de operador (desbloqueado).

---

## Activar el desbloqueo OEM

El desbloqueo OEM debe activarse desde el sistema operativo antes de poder continuar.

1. Ve a **Ajustes → Acerca del teléfono/tablet** y toca repetidamente **Número de compilación** hasta que el modo desarrollador esté activado.
2. Ve a **Ajustes → Sistema → Opciones de desarrollador** y activa **Desbloqueo OEM**. En algunas SKU compatibles con operadores, esto requiere una conexión a internet activa para que el OS predeterminado pueda verificar que el dispositivo no fue vendido bloqueado a un operador.

> **Nota Pixel 6a:** El desbloqueo OEM no funcionará con la versión OS de fábrica. Actualiza via OTA a la versión de **junio de 2022** o posterior, luego realiza un restablecimiento de fábrica para reparar el desbloqueo OEM.

---

## Método de instalación 1: Instalador web (Recomendado)

El [instalador web de GrapheneOS](https://grapheneos.org/install/web) es el enfoque recomendado para la mayoría de usuarios. Usa WebUSB directamente en tu navegador — no se requiere instalación de software.

### Paso 1: Evitar errores de fwupd (solo Linux)

En Linux, `fwupd` se conecta incorrectamente a los dispositivos usando el protocolo fastboot, bloqueando el instalador. Detenlo antes de conectar tu dispositivo:

```bash
sudo systemctl stop fwupd.service
```

Esto no persistirá tras los reinicios.

### Paso 2: Configurar reglas udev (solo Linux)

En Arch Linux:

```bash
sudo pacman -S android-udev
```

En Debian y Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Paso 3: Arrancar en la interfaz del bootloader

Mantén pulsado el botón de **bajar volumen** mientras el dispositivo arranca (enciéndelo desde apagado manteniendo bajar volumen, o reinicia y mantén bajar volumen). El dispositivo debe mostrar un **triángulo de advertencia rojo** y las palabras **"Fastboot Mode"** — no pulses el botón de encendido para activar "Iniciar".

### Paso 4: Conectar el dispositivo

Conecta el dispositivo a tu ordenador mediante USB. En Linux, reconecta el cable si las reglas udev no estaban configuradas antes de la primera conexión.

> **Pixel Tablet:** Desconecta del soporte antes de conectar via USB — la tablet no puede usar ambos simultáneamente.

> **Windows:** Windows 10/11 actual incluye un controlador fastboot genérico para Pixel 4a (5G) y posteriores. Para Pixels más antiguos o Windows desactualizado, instala el controlador desde Windows Update (busca en "Ver actualizaciones opcionales" → "LeMobile Android Device").

### Paso 5: Desbloquear el bootloader

Ve a [https://grapheneos.org/install/web](https://grapheneos.org/install/web) y haz clic en el botón **Desbloquear el bootloader**. Confirma en el dispositivo usando los botones de volumen para cambiar la selección y el botón de encendido para confirmar. **Esto borra todos los datos.**

### Paso 6: Descargar y flashear las imágenes de fábrica

1. Haz clic en **Descargar versión** para descargar las imágenes de fábrica para tu dispositivo.
2. Haz clic en **Flashear imágenes de fábrica** y espera a que el proceso se complete. Flasheará automáticamente el firmware, reiniciará en la interfaz del bootloader y flasheará el OS. **No interactúes con el dispositivo hasta que termine.**

### Paso 7: Bloquear el bootloader

Tras el flasheo, haz clic en **Bloquear el bootloader** en el instalador web. Confirma en el dispositivo. **Esto borra todos los datos de nuevo** — bloquear el bootloader activa el verified boot completo.

---

## Método de instalación 2: Línea de comandos (CLI)

### Paso 1: Abrir un terminal

En Windows, abre una ventana de **PowerShell normal (no administrador)**. Elimina el alias heredado de `curl`:

```powershell
Remove-Item Alias:Curl
```

### Paso 2: Instalar fastboot

Necesitas fastboot versión **≥ 35.0.1**.

**Arch Linux:**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** — sus paquetes están desactualizados. Usa la versión independiente:

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS:**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows:**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

Verifica tu versión:

```bash
fastboot --version
# Esperado: fastboot version 35.0.2-12147458
```

### Paso 3: Configurar reglas udev (solo Linux)

Arch Linux:

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Paso 4: Evitar errores de fwupd (solo Linux)

```bash
sudo systemctl stop fwupd.service
```

### Paso 5: Arrancar en la interfaz del bootloader

Mantén **bajar volumen** durante el arranque hasta que el dispositivo muestre **"Fastboot Mode"** con el triángulo de advertencia rojo.

### Paso 6: Conectar y desbloquear el bootloader

Conecta via USB, luego ejecuta:

```bash
fastboot flashing unlock
```

Confirma en el dispositivo (botones de volumen para la selección, botón de encendido para confirmar). **Esto borra todos los datos.**

### Paso 7: Instalar OpenSSH (para verificación de imágenes)

macOS y Windows incluyen OpenSSH por defecto.

Arch Linux:

```bash
sudo pacman -S openssh
```

Debian / Ubuntu:

```bash
sudo apt install openssh-client
```

### Paso 8: Descargar y verificar las imágenes de fábrica

Descarga la clave de firma:

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Contenido esperado:

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Descarga las imágenes de fábrica (reemplaza `DEVICE_NAME` y `VERSION` con los valores reales):

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Verifica la firma (Linux / macOS):

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows:

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Salida esperada:

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Paso 9: Flashear las imágenes de fábrica

Extrae las imágenes:

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

Entra en el directorio y ejecuta el script de flasheo:

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Espera a que el proceso termine. Maneja automáticamente el flasheo del firmware, reinicios del bootloader y flasheo del OS. **No interactúes con el dispositivo hasta que termine.**

> **Solución de problemas tmpfs en Linux:** Si `/tmp` no tiene suficiente espacio, usa:
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Paso 10: Bloquear el bootloader

```bash
fastboot flashing lock
```

Confirma en el dispositivo. **Esto borra todos los datos de nuevo.** Bloquear activa el verified boot completo y evita que fastboot modifique las particiones.

---

## Post-instalación

### Arranque

Pulsa el botón de encendido con la opción predeterminada **Iniciar** seleccionada en la interfaz del bootloader para arrancar GrapheneOS.

### Desactivar el desbloqueo OEM

Durante la primera configuración, la última pantalla contiene un interruptor para el desbloqueo OEM (marcado por defecto — dejarlo marcado **desactiva** el desbloqueo OEM). Esto es recomendable. Puedes cambiarlo más tarde en **Opciones de desarrollador**.

### Verificar la instalación

GrapheneOS aprovecha el verified boot y la atestación de hardware. El verified boot verifica todo el firmware e imágenes del OS en cada arranque contra claves grabadas en los fusibles del SoC. GrapheneOS flashea su propia clave pública de verified boot en el elemento seguro — en cada arranque, esta clave verifica el OS.

#### Hashes de clave Verified Boot

Cuando se carga un OS alternativo, el dispositivo muestra un **aviso amarillo** con el identificador del OS (sha256 de la clave de verified boot). Los Pixels de 4ª y 5ª generación solo muestran los primeros 32 bits; **los Pixels de 6ª generación en adelante muestran el hash completo**. Compara con los hashes oficiales:

| Dispositivo | Hash de clave Verified Boot |
|------------|---------------------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### Atestación basada en hardware con Auditor

GrapheneOS proporciona la [app Auditor](https://attestation.app/) para verificar la integridad del hardware, firmware y OS usando verified boot y atestación remota. Los resultados se muestran en un segundo dispositivo Android ejecutando Auditor (no en el dispositivo que se está verificando), o mediante el [servicio de monitoreo de integridad de dispositivos](https://attestation.app/) opcional para verificaciones automáticas programadas con alertas por correo.

---

## Reemplazar GrapheneOS con el OS predeterminado

La instalación del OS predeterminado via la [herramienta de flasheo web de Google](https://flash.android.com/) es similar al proceso anterior. Sin embargo, antes de flashear y bloquear, debes borrar la clave de verified boot de GrapheneOS para revertir completamente al stock:

**Instalador web:** Usa el botón "Borrar clave no-stock" en el instalador web de GrapheneOS.

**CLI:**

```bash
fastboot erase avb_custom_key
```

Luego flashea las imágenes de fábrica stock y bloquea el bootloader.

---

## Conclusión

Instalar GrapheneOS en tu Google Pixel proporciona funciones de privacidad y seguridad líderes en la industria. Usa el **instalador web** en [grapheneos.org/install/web](https://grapheneos.org/install/web) para la experiencia más sencilla, o sigue los pasos CLI anteriores para un enfoque tradicional. Siempre bloquea el bootloader después del flasheo para activar el verified boot completo, y opcionalmente usa la app Auditor para confirmar la integridad de tu instalación.

## Referencias

1. [Sitio web de GrapheneOS](https://grapheneos.org/)
2. [Instalador web de GrapheneOS](https://grapheneos.org/install/web)
3. [Guía de instalación CLI de GrapheneOS](https://grapheneos.org/install/cli)
4. [Versiones de GrapheneOS](https://grapheneos.org/releases)
5. [Guía de uso de GrapheneOS](https://grapheneos.org/usage)
6. [FAQ de GrapheneOS](https://grapheneos.org/faq)
7. [App Auditor](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
