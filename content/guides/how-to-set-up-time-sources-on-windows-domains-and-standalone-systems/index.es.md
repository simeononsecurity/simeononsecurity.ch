---
title: "Mejores prácticas para la administración de fuentes de tiempo en dominios de Windows y máquinas independientes"
draft: false
toc: true
date: 2023-05-23
description: "Aprenda a configurar y manejar fuentes de tiempo de manera efectiva en dominios de Windows y máquinas independientes para garantizar una sincronización de tiempo precisa y evitar posibles problemas."
tags: ["fuentes de tiempo", "dominio de Windows", "máquinas independientes", "sincronización de tiempo", "cronometraje preciso", "servidores NTP", "controladores de dominio", "Servicio de hora de Windows", "fallas de autenticación", "inconsistencias del archivo de registro", "problemas de replicación", "configuración de la fuente de tiempo", "gestión de fuente de tiempo", "Sincronización de tiempo de Windows", "mejores prácticas de cronometraje", "configuración de la fuente de tiempo", "sincronizando la hora del sistema", "Sincronización de tiempo de dominio de Windows", "sincronización de tiempo de máquina independiente", "selección de fuente de tiempo", "solución de problemas de fuente de tiempo", "errores de fuente de tiempo", "problemas con la fuente de tiempo", "Comandos de configuración de la fuente de tiempo", "instrucciones de configuración de la fuente de tiempo", "desafíos de sincronización de tiempo", "consecuencias de la pérdida de tiempo", "prevención de deriva de tiempo", "resolución de fallas de sincronización de tiempo", "solución de problemas de sincronización de tiempo", "gestión de fuentes de tiempo en dominios de Windows", "manejo de fuentes de tiempo en máquinas Windows independientes", "prevención de pérdidas de tiempo en entornos Windows", "consecuencias de los fallos de sincronización horaria", "mejores prácticas para un cronometraje preciso"]
cover: "/img/cover/An_image_depicting_a_clock_being_synchronized_with_a_domain.png"
coverAlt: "Una imagen que muestra un reloj sincronizado con un controlador de dominio y una máquina independiente, que simboliza la gestión de la fuente de tiempo y la sincronización precisa del tiempo en entornos de Windows."
coverCaption: ""
---

**Cómo configurar y manejar fuentes de tiempo en un dominio de Windows y en máquinas independientes de Windows**

La sincronización de tiempo es crucial para mantener marcas de tiempo precisas y garantizar el funcionamiento adecuado de los sistemas en un dominio de Windows o en máquinas Windows independientes. En este artículo, analizaremos las prácticas recomendadas para configurar y gestionar fuentes de tiempo en ambos escenarios, destacando la importancia de que los miembros del dominio apunten a los controladores de dominio. También exploraremos diferentes opciones para fuentes de tiempo, enfatizando el uso de grupos NTP externos o servidores de tiempo basados en GPS para una precisión óptima.

______

## Configuración de fuentes de tiempo en un dominio de Windows

En un dominio de Windows, es fundamental contar con una sincronización horaria constante en todos los miembros del dominio. La mejor práctica es configurar los controladores de dominio como la fuente de tiempo principal para los miembros del dominio. Al hacerlo, se asegura de que todos los sistemas dentro del dominio tengan la hora sincronizada, lo cual es fundamental para la autenticación, el registro y varias operaciones del dominio.

### Opciones de fuente de tiempo para controladores de dominio

Los controladores de dominio pueden obtener su hora de diferentes fuentes, incluido el reloj del BIOS, VMware Tools (en entornos virtualizados) o servidores de hora externos. Si bien el uso del reloj del BIOS o VMware Tools puede ser conveniente, se recomienda utilizar una **fuente de estrato 0 o 1** como un grupo NTP externo o un servidor de tiempo basado en GPS para una mayor precisión.

#### Grupos NTP externos

Los grupos de NTP externos son fuentes confiables y distribuidas globalmente para la sincronización de tiempo. Consisten en una gran cantidad de servidores NTP mantenidos por organizaciones e instituciones en todo el mundo. Al configurar los controladores de dominio para sincronizarlos con grupos NTP externos, puede garantizar un cronometraje preciso dentro del dominio de Windows.

Para configurar controladores de dominio para usar un grupo NTP externo, siga estos pasos:

1. Abra un símbolo del sistema elevado en el controlador de dominio.
2. Ejecute el siguiente comando:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"pool.ntp.org" /reliable:yes /update
```

Este comando configura el controlador de dominio para sincronizar con el grupo NTP pool.ntp.org. Ajuste el comando para usar un grupo NTP diferente o múltiples fuentes si lo desea.

3. Reinicie el servicio de hora de Windows para aplicar los cambios:

```shell
net stop w32time && net start w32time
```


#### Servidores de hora basados en GPS

Otra opción para los controladores de dominio es utilizar servidores de tiempo basados en GPS. Estos servidores se basan en señales de GPS para proporcionar información de tiempo muy precisa. Al configurar un servidor de tiempo basado en GPS alojado localmente y configurar controladores de dominio para sincronizar con él, puede lograr una sincronización de tiempo precisa dentro del dominio de Windows.

### Configuración de miembros del dominio

Los miembros del dominio, como las máquinas cliente y otros servidores, deben configurarse para sincronizar su tiempo con los controladores de dominio. Esto garantiza que todos los sistemas del dominio permanezcan sincronizados y evite cualquier problema relacionado con el tiempo.

Para configurar los miembros del dominio para sincronizar la hora con los controladores de dominio, normalmente no se requieren pasos adicionales. De forma predeterminada, los miembros del dominio sincronizan automáticamente su tiempo con los controladores de dominio.

______

## Configuración de fuentes de tiempo en máquinas Windows independientes

En máquinas Windows independientes que no forman parte de un dominio, el proceso de configuración de fuentes de tiempo puede variar según la versión de Windows y la configuración regional. De forma predeterminada, las máquinas Windows independientes suelen utilizar **time.windows.com** como fuente de tiempo principal. Sin embargo, vale la pena señalar que el comportamiento predeterminado se puede modificar.

### Cambio de la fuente de tiempo en máquinas independientes

Si desea cambiar la fuente de tiempo en una máquina Windows independiente, puede seguir estos pasos:

1. Abra un símbolo del sistema elevado en la máquina.
2. Ejecute el siguiente comando para configurar el servidor NTP:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"time.windows.com" /update
```

Este comando establece time.windows.com como la fuente de tiempo para la máquina independiente. Ajuste el comando para usar una fuente de tiempo diferente si lo desea.

3. Reinicie el servicio de hora de Windows para que los cambios surtan efecto:

```shell
net stop w32time && net start w32time
```


Al ejecutar estos comandos, puede configurar una máquina Windows independiente para sincronizar su hora con la fuente de hora deseada.

______

## Conclusión

La sincronización de tiempo adecuada es vital para los dominios de Windows y las máquinas independientes por igual. En un dominio de Windows, es fundamental configurar los miembros del dominio para que apunten a los controladores de dominio para la sincronización de tiempo. Los controladores de dominio pueden obtener su tiempo de varias fuentes, siendo el uso de grupos NTP externos o servidores de tiempo basados en GPS la práctica recomendada para una mayor precisión.

En máquinas Windows independientes, la fuente de hora predeterminada suele ser time.windows.com. Sin embargo, puede cambiar la fuente de tiempo usando los comandos proporcionados.

Al seguir estas prácticas recomendadas y configurar las fuentes de tiempo adecuadas, se asegura un cronometraje preciso, una autenticación confiable y un registro coherente dentro de su entorno de Windows.

______

## Referencias

- [Microsoft Docs: How the Windows Time Service Works](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/how-the-windows-time-service-works)
- [Microsoft Docs: Windows Time Service Tools and Settings](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [NTP Pool Project](https://www.ntppool.org/)
- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)

