---
title: "Evitando el BGW-320: Uso de una ONT Azores COTS - Guía paso a paso"
draft: false
toc: true
date: 2023-04-30
description: "Aprenda cómo evitar el BGW-320 y utilizar una ONT COTS fabricada por Azores para conectarse a la red de su ISP con esta guía fácil de seguir."
tags: ["COTS ONT", "BGW-320", "Azores", "fibra", "red", "XGS-PON", "Ethernet", "Paso de IP", "personalización", "ISP", "tener ID", "Dirección MAC", "identificación del equipo", "versión de la imagen", "versión de hardware", "telnet", "Aplicación CLI", "GUI web", "modo de configuración de fábrica", "problemas de compatibilidad"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Un técnico de dibujos animados sostiene una ONT COTS con un cable de fibra al fondo."
coverCaption: ""
---

## Cómo puentear el BGW-320 y usar un Azores WAG-D20

La mayoría de la gente con fibra tiene dos formas de conectarse a Internet - fibra a una ONT, Ethernet a una pasarela o fibra directamente a la pasarela. En este artículo, nos centraremos en cómo evitar el BGW-320 y utilizar una ONT COTS fabricada por Azores.

### Aspectos técnicos

El[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Acceso al dispositivo

La dirección IP por defecto del dispositivo es 192.168.1.1 y su dirección Gateway tiene un error tipográfico de fábrica utilizando una dirección IP pública, es decir, muestra 192.162.1.1 en lugar de 192.168.1.1.

Una vez que arranca, tienes que pulsar enter para obtener un mensaje de inicio de sesión en la interfaz serie TTL (115200 8N1). Este dispositivo tiene un sistema de imagen A/B con una partición superpuesta que contiene los archivos que personalices.
 
### Credenciales

-`admin``ADMIN123!@#` - Inicio de sesión de administrador para GUI web
-`Guest``welcome` - Invitado
-`test``default` - Inicio de sesión en fábrica

### Interfaz Ethernet

Conecte su cliente al puerto ethernet 10G y configúrelo con una dirección en la red 192.168.1.x/24 como - 192.168.1.2/255.255.255.0.

Al ejecutar un escaneo de puertos desde 1-65535, notará algunos puertos abiertos:

- Puertos`23` &`8009` - Telnet, requiere inicio de sesión, ejecuta la aplicación CLI.
- Puertos`10002` - Desconocido
- Puerto`80` - WebUI, sólo dos funciones

### Personalización de la ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Ahora viene la parte importante, es decir, cambiar algunos datos del dispositivo para hacerlo compatible con la red de tu ISP.

En primer lugar, obtenga la siguiente información de su ISP Gateway u ONT:

1. **ID DE LA ONT
2. **Dirección MAC
3. **Identificación del equipo**
4. **Versión de la imagen
5. **Versión de hardware

Nota: Estos son los valores OMCI y no los de la interfaz web.

Conéctese a su ONT personal (telnet 192.168.1.1), inicie sesión como **.`test` utilizando el **`default` contraseña y ejecute el comando 'test' para pasar al modo de configuración de fábrica.

Visualiza los valores actualmente configurados con el comando 'show':

-`show gpon mac`
-`show sn`
-`show equipment id`

Una vez hecho esto, personaliza la configuración con los siguientes comandos sustituyendo x por los valores de tu dispositivo:

-`set gpon mac xx:xx:xx:xx:xx:xx`
-`set sn <insert ONT ID here>`

Para HUMAX:

-`set equipment id “iONT320500G”`
-`config ONU-G_Version "BGW320-500_2.1”`

Para Nokia:

-`set equipment id “iONT320505G”`
-`config ONU-G_Version "BGW320-505_2.2”`

Nota: Los dos últimos comandos deben aplicarse desde telnet conectado como el **.`test` usuario.

### Reinicie y disfrute del True IP Passthrough

Después de la personalización, reinicie el ONT y disfrute del verdadero paso de IP.

### Resolución de problemas y pasos adicionales
Para obtener más información sobre este tema, consulte la página[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusión

Siguiendo estos pasos se puede evitar con éxito el BGW-320 y utilizar la ONT COTS hecha por Azores para conectarse a la red de su ISP. Sin embargo, tenga cuidado al introducir los comandos y asegúrese de reemplazar 'x' con los valores de su dispositivo correctamente, de lo contrario, puede enfrentarse a problemas de compatibilidad que pueden dar lugar a fallos de conexión.


