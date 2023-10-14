---
title: "Ejecución de pfSense en el Thin Client HP t740: consejos y guía de solución de problemas"
draft: false
toc: true
date: 2023-04-29
description: "Aprenda a configurar pfSense en el Thin Client HP t740 y a solucionar posibles problemas, como congelamiento y problemas de detección de SSD."
tags: ["pfSense", "OPNsense", "BSD endurecido", "hp t740", "cliente ligero", "servidor doméstico", "PPPoE", "FreeBSD", "indicador de arranque", "loader.conf.local", "editor nano", "Detección de SSD", "SSD M.2", "Occidente digital", "solución de problemas", "posterior a la instalación", "UART", "ESXi", "proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Una caricatura de un mago lanzando un hechizo para reparar una computadora congelada, con una burbuja de diálogo que dice Problema resuelto"
coverCaption: ""
canonical: "https://simeononsecurity.com/guides/installing-pfsense-on-hp-t740-thin-client/"
---
 pfSense, OPNsense o HardenedBSD en el Thin Client HP t740**

Si está buscando un dispositivo potente para ejecutar pfSense, OPNsense o HardenedBSD, el Thin Client HP t740 podría ser una opción adecuada para usted.

## Más potencia y servidor doméstico compacto

El Thin Client HP t740 es un dispositivo compacto que se puede utilizar como una potente caja pfSense o como un servidor doméstico compacto. Ofrece más potencia que el t730 o el t620 Plus, lo que lo convierte en una opción adecuada para ejecutar PPPoE, especialmente si tiene Internet de fibra. También puede ofrecer una ruta de actualización a redes de 10 Gigabit.

## PS/2 se congela

Sin embargo, si planea ejecutar FreeBSD o sus derivados como pfSense, OPNsense o HardenedBSD en la versión completa (a diferencia de dentro de ESXi o Proxmox), es posible que encuentre un problema en el que el sistema se congela al arrancar con el mensaje `atkbd0: [GIANT-LOCKED]` Afortunadamente, este problema se puede resolver ingresando los siguientes comandos en el indicador de inicio:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Tenga en cuenta que debe desactivar ambos, de lo contrario, aún se bloqueará en el arranque.*

Después de instalar el sistema operativo, abra un shell posterior a la instalación y ejecute el siguiente comando:

```bash
vi /boot/loader.conf.local
```
Luego, agrega estas dos líneas:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Cambios persistentes usando VI
Para aquellos que no están familiarizados con vi, pueden agregar la línea haciendo lo siguiente:

Agregando las lineas `hint.uart.0.disabled="1"` y `hint.uart.1.disabled="1"` hacia `/boot/loader.conf.local` El archivo usando el editor vi se puede hacer con los siguientes pasos:

1. Abra la terminal en su sistema FreeBSD.

2. Tipo `vi /boot/loader.conf.local` y presione Entrar para abrir el archivo en el editor vi.

3. Presione el botón `i` tecla para entrar en el modo de inserción.

4. Mueva el cursor al final del archivo usando las teclas de flecha.

5. Tipo `hint.uart.0.disabled="1"` sin las comillas.

6. Presione Entrar para comenzar una nueva línea.

7. Tipo `hint.uart.1.disabled="1"` sin las comillas.

8. Presione el botón `Esc` tecla para salir del modo de inserción.

9. Tipo `:wq` y presione Entrar para guardar y salir del archivo.

Esto agregará las dos líneas al `/boot/loader.conf.local` archivo, que deshabilitará los UART y solucionará el problema de bloqueo durante el arranque en ciertos dispositivos HP t740 "Thin Client" cuando se ejecuta FreeBSD o sus derivados como pfSense, OPNsense o HardenedBSD.

Esto solucionará el problema entre reinicios y actualizaciones de firmware en pfSense/OPNsense.

## SSD

Si está utilizando HP M.2 eMMC, no se detectará en una instalación de FreeBSD lista para usar. En ese caso, necesitará una SSD M.2 de terceros. Cualquier SSD M.2 puede funcionar, SATA o NVMe.

Si busca una SSD M.2 de otro fabricante para su thin client HP t740, le recomendamos que considere la [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Ambas opciones son confiables y deberían funcionar bien con su dispositivo. Si desea aprovechar ambas máquinas tragamonedas, necesitará ambas. Sacrificarás las velocidades de NVME, pero obtendrás algo de redundancia que es tan importante.

Tenga en cuenta que el autor de este artículo ha ejecutado con éxito pfSense CE 2.5.2 y OPNsense 22.1 en su t740 sin ningún problema después de seguir los pasos anteriores.

## Solución de problemas y postinstalación

Después de la instalación, si encuentra algún problema con la edición de archivos, puede instalar el editor nano usando `pkg update` y `pkg install nano` Esto le ayudará a editar archivos de texto con facilidad.

Para asegurarse de que los cambios realizados en el `/boot/loader.conf.local` el archivo persiste en las actualizaciones de la versión de pfSense, debe agregar las siguientes líneas a `/boot/loader.conf` y `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

Sin embargo, a veces la edición de `/boot/loader.conf.local` el archivo antes de reiniciar no soluciona el problema. En tales casos, puede ser necesario agregar las siguientes líneas al comienzo del primer arranque:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Estos pasos deberían resolver la mayoría de los problemas que puedan surgir durante y después del proceso de instalación.

### Referencias:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)