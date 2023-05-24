---
title: "Actualización de firmware sin conexión para Ubiquiti Unifi UDM Pro y UDM SE a través de la línea de comandos SSH"
draft: false
toc: true
date: 2023-05-28
description: "Aprenda a actualizar el firmware de Ubiquiti Unifi UDM Pro y UDM SE sin conexión a través de la línea de comandos SSH para obtener un rendimiento y una seguridad óptimos."
tags: ["Actualización de firmware de Ubiquiti", "UDM profesional", "UDM SE", "actualización de firmware fuera de línea", "línea de comandos SSH", "administración de redes", "Seguridad de la red", "actualización de firmware", "Conexión SSH", "archivo de firmware", "Controlador de red UniFi", "corrección de errores", "mejoras de rendimiento", "parches de seguridad", "redes", "dispositivos de red", "tecnología", "gestión de TI", "proceso de actualización de firmware", "optimización de red", "Actualización de firmware de Ubiquiti Networks", "Actualización de firmware de UDM Pro", "Actualización de firmware de UDM SE", "proceso de actualización de firmware fuera de línea", "Actualización de firmware SSH", "administración de dispositivos de red", "actualizaciones de seguridad de la red", "estrategias de actualización de firmware", "gestión de firmware fuera de línea", "optimización del rendimiento de la red", "gestión de parches de seguridad", "actualizaciones de tecnología de red"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "Una ilustración colorida que muestra una computadora que se conecta a un enrutador a través de SSH que simboliza el proceso de actualización de firmware fuera de línea para dispositivos Ubiquiti Unifi UDM Pro y UDM SE."
coverCaption: ""
---

**Actualice Ubiquiti Unifi UDM Pro y UDM SE sin conexión a través de SSH**

En el mundo de las redes, **Ubiquiti Networks** ha ganado reconocimiento por sus soluciones innovadoras. **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** y **Unifi Dream Machine SE (UDM SE)** son dos productos populares que ofrecen funciones integrales de administración de red. La actualización del firmware de estos dispositivos es crucial para garantizar un rendimiento y una seguridad óptimos. En este artículo, exploraremos cómo actualizar el firmware de UDM Pro y UDM SE **sin conexión** usando la línea de comandos SSH.

______

## ¿Por qué actualizar el firmware?

Las actualizaciones de firmware son esenciales para cualquier dispositivo de red, ya que a menudo contienen correcciones de errores, mejoras de rendimiento y parches de seguridad. La actualización periódica del firmware de su UDM Pro y UDM SE es crucial para garantizar que su red permanezca segura y funcione sin problemas.

______

## Actualización de firmware fuera de línea

La actualización del firmware de UDM Pro y UDM SE se puede realizar a través del **UniFi Dashboard**. Sin embargo, en algunos escenarios, una conexión a Internet puede no estar disponible o deseable. En tales casos, una actualización fuera de línea mediante SSH de línea de comandos proporciona una solución alternativa.

______

## Preparándose para la actualización sin conexión

Antes de continuar con la actualización sin conexión, asegúrese de tener los siguientes requisitos previos:

1. Una computadora o dispositivo con un cliente SSH instalado.
2. El archivo de firmware más reciente para su UDM Pro o UDM SE. Puede obtener el archivo de firmware del [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) cuenta

______

## Establecimiento de la conexión SSH

Para actualizar UDM Pro o UDM SE a través de SSH de línea de comandos, siga estos pasos:

1. Asegúrese de que su computadora o dispositivo esté conectado a la misma red que UDM Pro o UDM SE.
2. Abra su cliente SSH preferido y establezca una conexión SSH a la **dirección IP de UDM Pro o UDM SE**. Por ejemplo, si usa el **cliente OpenSSH** en Linux o macOS, puede usar el siguiente comando:

```bash
ssh root@<UDM_IP_ADDRESS>
```

Reemplazar `<UDM_IP_ADDRESS>` con la dirección IP real de tu UDM Pro o UDM SE.

3. Introduzca el **nombre de usuario** y la **contraseña** cuando se le solicite. Las credenciales predeterminadas para los dispositivos Ubiquiti suelen ser `ubnt` tanto para el nombre de usuario como para la contraseña.

______

## Actualización de firmware

Una vez que haya establecido la conexión SSH, puede continuar con la actualización del firmware:

1. Cargue el archivo de firmware en UDM Pro o UDM SE mediante **SCP (Copia segura)**. SCP permite la transferencia segura de archivos a través de SSH. Suponiendo que el archivo de firmware se encuentra en su máquina local, puede usar el siguiente comando:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Reemplazar `<FIRMWARE_FILE_PATH>` con la ruta al archivo de firmware en su máquina local, y `<UDM_IP_ADDRESS>` con la dirección IP de tu UDM Pro o UDM SE.

2. Una vez que se carga el archivo de firmware, puede iniciar el proceso de actualización de firmware. Ejecute el siguiente comando:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. El UDM Pro o UDM SE iniciará el proceso de actualización del firmware. Esto puede tomar varios minutos. **No interrumpa el proceso** hasta que se complete la actualización.

4. Una vez finalizada la actualización, puede verificar la versión del firmware iniciando sesión en el controlador de red UniFi o ejecutando el siguiente comando:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Tenga en cuenta que el proceso anterior asume que tiene el archivo de firmware necesario para su UDM Pro o UDM SE. Asegúrese de tener el archivo de firmware correcto para su modelo y versión de dispositivo específico.

## Conclusión

Actualizar el firmware de sus dispositivos Ubiquiti Unifi UDM Pro y UDM SE es un paso crucial para garantizar un rendimiento y una seguridad óptimos. Si bien UniFi Network Controller proporciona una forma conveniente de actualizar el firmware, realizar una actualización fuera de línea a través de la línea de comandos SSH ofrece una solución viable cuando una conexión a Internet no está disponible o no es deseable.

Si sigue los pasos descritos en este artículo, puede actualizar correctamente el firmware de sus dispositivos UDM Pro y UDM SE mediante SSH de línea de comandos. Recuerde usar siempre la última versión de firmware proporcionada por Ubiquiti Networks para aprovechar las correcciones de errores, las mejoras de rendimiento y los parches de seguridad.

## Referencias

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Página oficial de descargas de Ubiquiti para archivos de firmware.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)
