---
title: "Evitar el BGW-320: usar un COTS ONT de Azores: una guía paso a paso"
draft: false
toc: true
date: 2023-04-30
description: "Aprenda cómo omitir el BGW-320 y usar una COTS ONT fabricada por Azores para conectarse a la red de su ISP con esta guía fácil de seguir".
tags: ["CUNAS ONT","BGW-320","Azores","fibra","red","XGS-PON","Ethernet","paso de IP","personalización","ISP","identificación de ont","Dirección MAC","identificación del equipo","versión de la imagen","versión del hardware","telnet","Aplicación CLI","GUI web","modo de configuración de fábrica","problemas de compatibilidad"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Un técnico de dibujos animados sosteniendo un COTS ONT con un cable de fibra en el fondo".
coverCaption: ""
---

## Cómo omitir el BGW-320 y usar un Azores WAG-D20

La mayoría de las personas con fibra tienen dos formas de conectarse a Internet: fibra a una ONT, Ethernet a una puerta de enlace o fibra directamente a la puerta de enlace. En este artículo, nos centraremos en cómo eludir el BGW-320 y usar un COTS ONT fabricado por Azores.

### Aspectos técnicos

El[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Acceso al dispositivo

La dirección IP predeterminada del dispositivo es 192.168.1.1 y su dirección de puerta de enlace tiene un error tipográfico de fábrica al usar una dirección IP pública, es decir, muestra 192.162.1.1 en lugar de 192.168.1.1.

Una vez que se inicia, debe presionar Intro para obtener un aviso de inicio de sesión en la interfaz serial TTL (115200 8N1). Este dispositivo tiene un sistema de imágenes A/B con una partición superpuesta que contiene los archivos que personalizas.
 
### Cartas credenciales

- `admin`/`ADMIN123!@#` - Inicio de sesión del administrador para la GUI web
- `Invitado`/`bienvenido` - Inicio de sesión de invitado
- `test`/`default` - Inicio de sesión de fábrica

### Interfaz Ethernet

Conecte su cliente al puerto ethernet 10G y configúrelo con una dirección en la red 192.168.1.x/24 como - 192.168.1.2/255.255.255.0.

Al ejecutar un escaneo de puertos desde 1-65535, notará algunos puertos abiertos:

- Puertos `23` y `8009` - Telnet, requiere inicio de sesión, ejecuta la aplicación CLI.
- Puerto `10002` - Desconocido
- Puerto `80` - WebUI, solo dos funciones

### Personalizando la ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Ahora viene la parte importante, es decir, cambiar la información del dispositivo para que sea compatible con la red de su ISP.

Primero, tome la siguiente información de su ISP Gateway u ONT:

1. **Identificación de ONT**
2. **Dirección MAC**
3. **Identificación del equipo**
4. **Versión de la imagen**
5. **Versión de hardware**

Nota: Estos son los valores de OMCI y no los de la interfaz de usuario web.

Telnet a su ONT personal (telnet 192.168.1.1), inicie sesión como **`test`** usando la contraseña **`default`** y ejecute el comando 'test' para pasar al modo de configuración de fábrica.

Muestre los valores establecidos actualmente con el comando 'mostrar':

- `mostrar gpon mac`
- `mostrar sn`
- `mostrar identificación del equipo`

Una vez hecho esto, personalice la configuración con los siguientes comandos reemplazando x con los valores de su dispositivo:

- `establecer gpon mac xx:xx:xx:xx:xx:xx`
- `establecer sn <insertar ID de ONT aquí>`

Para HUMAX:

- `Establecer id de equipo “iONT320500G”`
- `config ONU-G_Version "BGW320-500_2.1”`

Para Nokia:

- `Establecer id de equipo "iONT320505G"`
- `config ONU-G_Version "BGW320-505_2.2”`

Nota: Los dos últimos comandos se deben aplicar desde telnet con sesión iniciada como usuario **`test`**.

### Reinicie y disfrute de True IP Passthrough

Después de personalizar, reinicie la ONT y disfrute de un verdadero paso de IP.

### Solución de problemas y pasos adicionales
Para obtener más información sobre este tema, consulte el[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusión

Siguiendo estos pasos, uno puede omitir con éxito el BGW-320 y usar COTS ONT fabricado por Azores para conectarse a la red de su ISP. Sin embargo, tenga cuidado al ingresar comandos y asegúrese de reemplazar 'x' con los valores de su dispositivo correctamente; de lo contrario, puede enfrentar problemas de compatibilidad que pueden provocar fallas en la conexión.


