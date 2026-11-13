---
title: "Conceptos básicos de redes: subredes, subdivisión en subredes y diseño de VLAN"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Aprende los fundamentos de subredes, subdivisión en subredes y VLAN para administrar redes con eficiencia y mejorar su seguridad."
genre: ["Fundamentos de redes", "Subdivisión en subredes", "VLAN", "Administración de redes", "Seguridad de redes", "Direccionamiento IP", "Segmentación de redes", "Uso eficiente de recursos", "Rendimiento de red", "IPv4"]
tags: ["fundamentos de redes", "subredes", "subdivisión en subredes", "VLAN", "administración de redes", "seguridad de redes", "direccionamiento IP", "segmentación de redes", "uso eficiente de recursos", "rendimiento de red", "IPv4", "configuración de subred", "máscaras de subred", "asignación de direcciones IP", "comunicación entre VLAN", "puertos de switch", "configuración de VLAN", "interfaces VLAN", "conectividad de red", "redes subdivididas", "dominios de difusión", "medidas de seguridad", "rango de direcciones IP", "ejemplos de subred", "despliegue de VLAN", "administración de red", "configuración de switch", "configuración de router", "escalabilidad de red", "comunicación y transferencia de datos", "redes eficientes"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Ilustración simbólica de redes informáticas interconectadas con subredes y VLAN"
coverCaption: "Redes eficientes: subredes y VLAN explicadas de forma sencilla."
---

## Conceptos básicos de redes: subredes, subdivisión en subredes y diseño de VLAN

### Introducción

En el mundo conectado actual, las redes informáticas son esenciales para la comunicación y la transferencia de datos. Conocer los fundamentos de redes sirve tanto a profesionales de TI como a usuarios. Este artículo explica las subredes, la subdivisión en subredes y las VLAN, además de su propósito y funcionamiento.

## Subredes: una explicación más detallada

### ¿Qué es una subred?

{{< youtube id="nR5xCmXJE5E" >}}

Una **subred** es una subdivisión lógica de una red IP. Permite al administrador dividir una red grande en segmentos más pequeños y manejables. Cada subred tiene un rango propio de direcciones IP, lo que ayuda a aprovecharlas mejor.

### ¿Por qué usar subredes?

Las redes informáticas usan subredes por varios motivos:

1. **Segmentación de red:** Las subredes dividen una red grande en otras más pequeñas. Esto mejora el rendimiento y reduce la congestión.

2. **Mayor seguridad:** Separar dispositivos en distintas subredes permite aplicar cortafuegos y listas de control de acceso para gestionar el tráfico y mejorar la seguridad.

3. **Uso eficiente de recursos:** La subdivisión en subredes permite asignar mejor las direcciones IP, un recurso limitado en IPv4.

### ¿Cómo crear subredes?

{{< youtube id="LdSAaSHfK3M" >}}

La subdivisión en subredes consiste en dividir una red en subredes más pequeñas. Sigue estos pasos:

1. **Determina los requisitos de red:** Calcula cuántas subredes y hosts necesitas en cada una.

2. **Elige un esquema de direccionamiento IP:** Selecciona un esquema adecuado al número de subredes y hosts requeridos.

3. **Calcula las máscaras de subred:** Determina las máscaras según la cantidad de subredes y hosts necesarios.

4. **Asigna direcciones IP:** Asigna direcciones a cada subred y comprueba que estén dentro del rango correcto.

5. **Prueba y verifica:** Comprueba la conectividad y las asignaciones de direcciones IP.

### Ejemplos de subdivisión en subredes

Veamos un ejemplo sencillo de subdivisión en subredes:

Supongamos que tenemos el rango IP 192.168.0.0/24 y queremos crear cuatro subredes con la misma cantidad de hosts. Podemos dividir la red así:

1. **Paso 1: Determina los requisitos de red:** Necesitamos cuatro subredes con la misma cantidad de hosts.

2. **Paso 2: Elige un esquema de direccionamiento IP:** Elegimos una máscara /26, que permite 64 direcciones por subred.

3. **Paso 3: Calcula las máscaras de subred:** La máscara /26 es 255.255.255.192.

4. **Paso 4: Asigna direcciones IP:** Asignamos estas direcciones a las subredes:

   - subred 1: 192.168.0.0/26
   - subred 2: 192.168.0.64/26
   - subred 3: 192.168.0.128/26
   - subred 4: 192.168.0.192/26

5. **Paso 5: Prueba y verifica:** Comprobamos la conectividad entre los dispositivos de cada subred.

### Tablas útiles de subdivisión en subredes

#### Tabla de referencia para calcular subredes

| Máscara de subred | Notación CIDR | Direcciones IP totales | Direcciones IP utilizables |
|-------------|---------------|--------------------|---------------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /19 | 255.255.224.0 | 8,192 | 8,190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32,768 | 32,766 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /15 | 255.254.0.0 | 131,072 | 131,070 |
| /14 | 255.252.0.0 | 262,144 | 262,142 |
| /13 | 255.248.0.0 | 524,288 | 524,286 |
| /12 | 255.240.0.0 | 1,048,576 | 1,048,574 |
| /11 | 255.224.0.0 | 2,097,152 | 2,097,150 |
| /10 | 255.192.0.0 | 4,194,304 | 4,194,302 |
| /9 | 255.128.0.0 | 8,388,608 | 8,388,606 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /7 | 254.0.0.0 | 33,554,432 | 33,554,430 |
| /6 | 252.0.0.0 | 67,108,864 | 67,108,862 |
| /5 | 248.0.0.0 | 134,217,728 | 134,217,726 |
| /4 | 240.0.0.0 | 268,435,456 | 268,435,454 |
| /3 | 224.0.0.0 | 536,870,912 | 536,870,910 |
| /2 | 192.0.0.0 | 1,073,741,824 | 1,073,741,822 |
| /1 | 128.0.0.0 | 2,147,483,648 | 2,147,483,646 |
| /0 | 0.0.0.0 | 4,294,967,296 | 4,294,967,294 |

#### Tabla de subredes utilizables

| Notación CIDR | Número de subredes utilizables |
|---------------|-------------------------|
| /0 | 1 |
| /1 | 2 |
| /2 | 4 |
| /3 | 8 |
| /4 | 16 |
| /5 | 32 |
| /6 | 64 |
| /7 | 128 |
| /8 | 256 |
| /9 | 512 |
| /10 | 1024 |
| /11 | 2048 |
| /12 | 4096 |
| /13 | 8192 |
| /14 | 16384 |
| /15 | 32768 |
| /16 | 65536 |
| /17 | 131072 |
| /18 | 262144 |
| /19 | 524288 |
| /20 | 1048576 |
| /21 | 2097152 |
| /22 | 4194304 |
| /23 | 8388608 |
| /24 | 16777216 |
| /25 | 33554432 |
| /26 | 67108864 |
| /27 | 134217728 |
| /28 | 268435456 |
| /29 | 536870912 |
| /30 | 1073741824 |
| /31 | 2147483648 |
| /32 | 4294967296 |

#### Tabla de potencias de dos

| Potencia de dos | Valor |
|--------------|-------|
| 2^32 | 4294967296 |
| 2^31 | 2147483648 |
| 2^30 | 1073741824 |
| 2^29 | 536870912 |
| 2^28 | 268435456 |
| 2^27 | 134217728 |
| 2^26 | 67108864 |
| 2^25 | 33554432 |
| 2^24 | 16777216 |
| 2^23 | 8388608 |
| 2^22 | 4194304 |
| 2^21 | 2097152 |
| 2^20 | 1048576 |
| 2^19 | 524288 |
| 2^18 | 262144 |
| 2^17 | 131072 |
| 2^16 | 65536 |
| 2^15 | 32768 |
| 2^14 | 16384 |
| 2^13 | 8192 |
| 2^12 | 4096 |
| 2^11 | 2048 |
| 2^10 | 1024 |
| 2^9 | 512 |
| 2^8 | 256 |
| 2^7 | 128 |
| 2^6 | 64 |
| 2^5 | 32 |
| 2^4 | 16 |
| 2^3 | 8 |
| 2^2 | 4 |
| 2^1 | 2 |
| 2^0 | 1 |

## VLAN: redes de área local virtuales

### ¿Qué es una VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

Una **VLAN (Virtual Local Area Network)** es una agrupación lógica de dispositivos de una red, sin importar su ubicación física. Las VLAN crean dominios de difusión separados y mejoran la flexibilidad, seguridad y escalabilidad de la red.

### ¿Por qué usar VLAN?

Las VLAN ofrecen varias ventajas para administrar redes:

1. **Mayor seguridad:** Las VLAN aíslan datos sensibles y limitan el acceso no autorizado. El tráfico permanece en segmentos concretos, lo que protege recursos importantes.

2. **Mejor rendimiento:** Las VLAN separan lógicamente el tráfico, reducen la congestión y mejoran el rendimiento. El tráfico de difusión queda limitado a la VLAN.

3. **Administración más sencilla:** Las VLAN agrupan dispositivos por función, departamento u otro criterio lógico, lo que simplifica su administración y configuración.

### Configuración de VLAN

Para configurar una VLAN, normalmente se siguen estos pasos:

1. **Identifica los requisitos de VLAN:** Determina el propósito y alcance del despliegue. Identifica los dispositivos y su ubicación en las VLAN.

2. **Asigna identificadores de VLAN:** Asigna un identificador único a cada VLAN. Suelen ser números del 1 al 4094, aunque algunos están reservados.

3. **Configura los puertos del switch:** Asigna los puertos a las VLAN adecuadas como puertos de acceso o troncales.

4. **Configura las interfaces VLAN:** Si necesitas comunicación entre VLAN, [configura las interfaces VLAN](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/) en un switch de capa 3 o en un router.

5. **Prueba y verifica:** Comprueba la conectividad entre los dispositivos de cada VLAN.

### Tabla de VLAN reservadas

| Etiquetas VLAN | Descripción |
|-------------------|----------------------------------------------------|
| VLAN 0 | ID de VLAN reservada, no debe usarse |
| VLAN 1 | VLAN predeterminada de muchos dispositivos de red |
| VLAN 2 | VLAN predeterminada para tráfico de gestión |
| VLAN 3-4 | ID de VLAN reservadas |
| VLAN 5 | Reservada para la ID de VLAN de Token Ring |
| VLAN 6-1001 | ID de VLAN reservadas |
| VLAN 1002-1005 | VLAN predeterminadas de Cisco para fines específicos |
| VLAN 1006-1024 | ID de VLAN reservadas |
| VLAN 1025-4094 | Reservadas para el rango VLAN extendido |
| VLAN 4095 | ID de VLAN reservada, no debe usarse |

## Conclusión

[Entender las subredes](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) y las VLAN es esencial para diseñar y administrar redes informáticas eficientes. Las subredes segmentan la red para mejorar el rendimiento y la seguridad. Las VLAN agrupan dispositivos de forma lógica y facilitan la gestión. Con estos pasos, los administradores pueden dividir redes y configurar VLAN según sus necesidades.

Los fundamentos de redes son la base de redes robustas y escalables que responden a las necesidades actuales de comunicación y transferencia de datos.

## Referencias

- [Fundamentos de subnetting](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Comprender y configurar VLAN](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [Estándar IEEE 802.1Q](https://standards.ieee.org/standard/802_1Q-2018.html)
