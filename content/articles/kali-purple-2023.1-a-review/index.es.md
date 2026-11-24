---
title: "Kali Purple 2023.1: novedades y funciones principales"
date: 2023-04-08
lastmod: 2026-11-24
toc: true
draft: false
description: "Repaso de Kali Purple 2023.1, sus herramientas y mejoras de entonces, con referencias actuales para laboratorios de seguridad."
tags: ["Kali Linux", "Kali Purple", "2023.1", "hacking ético", "pruebas de penetración", "ciberseguridad", "herramientas", "marco de explotación", "actualizaciones de Kali ARM", "Kali NetHunter", "documentación de Kali", "compatibilidad con el kernel", "compatibilidad con Bluetooth", "LineageOS", "OneUI", "Radxa Zero", "computadora de placa única", "parches del kernel", "contribuciones de la comunidad", "Discord de Kali", "actualizaciones de Linux", "distribución de hacking ético", "nuevas funciones", "mejoras", "Xfce", "KDE", "GNOME", "Xfce 4.18", "KDE Plasma 5.27", "nuevas herramientas y paquetes", "compatibilidad con dispositivos ARM", "documentación de Kali", "normativa gubernamental"]
cover: "/img/cover/A_3D_animated_Kali_Linux_dragon_mascot_surrounded.webp"
coverAlt: "Un dragón de Kali Linux animado en 3D está sentado sobre un escudo y rodeado de herramientas de ciberseguridad."
coverCaption: ""
---

**Kali Purple 2023.1: una reseña**

Kali Purple 2023.1 fue la primera versión preliminar técnica de la orientación de seguridad defensiva de Kali. Ya no es la versión más reciente. Este artículo documenta el lanzamiento original e incluye referencias actuales para que no confundas las versiones de paquetes de 2023.1 con las actuales.

## Estado actual de Kali

El historial oficial de versiones de Kali identifica Kali 2026.2, publicada el 29 de junio de 2026, como la segunda versión rolling de ese año. Usa el kernel de Linux 6.19 y Xfce 4.20.7. Las [notas de Kali 2026.2](https://www.kali.org/blog/kali-linux-2026-2-release/) también describen GNOME 50, KDE Plasma 6.6, el cambio de `sources.list` a `sources.list.d/kali.source` y cambios en el arranque de máquinas virtuales.

Kali Purple representa una orientación defensiva y de equipos purple dentro de Kali. El anuncio de 2023.1 describió una versión preliminar con una arquitectura de referencia SOC-in-a-box, herramientas defensivas y categorías de menú del Marco de Ciberseguridad del NIST. Esos detalles corresponden al alcance histórico. Para elegir paquetes actuales, consulta la [documentación de metapaquetes](https://www.kali.org/docs/general-use/metapackages/) de Kali y selecciona solo los grupos de herramientas que necesite tu laboratorio.

*Realiza cada ejercicio ofensivo o defensivo en un laboratorio aislado y autorizado. Instalar Kali no te da permiso para probar sistemas que no posees ni administras.*

______

## Actualizaciones del fondo de pantalla y escritorio de Kali

Kali Purple 2023.1 introduce un **nuevo fondo de pantalla predeterminado** llamado Kali Sticker, con un fondo púrpura y varias pegatinas relacionadas con Kali. Este nuevo fondo de pantalla fue inspirado por el trabajo de /u/Albert-III- y TJ_Null.

Además del nuevo fondo de pantalla, Kali Purple 2023.1 también actualiza sus tres principales entornos de escritorio: **Xfce, KDE y GNOME**. Estas actualizaciones incluyen nuevas características, mejoras de rendimiento y correcciones de errores.

______

## Xfce 4.18

**Xfce 4.18** trae varias mejoras notables, incluyendo:

- Soporte mejorado para el escalado de la interfaz de usuario
- Actualizaciones del gestor de archivos Thunar
- Perfiles de panel para facilitar la personalización

______

## KDE Plasma 5.27

El **KDE Plasma 5.27** actualización introduce:

- Un nuevo sistema de mosaico de ventanas
- Un tema de aplicación más elegante
- Herramientas y widgets más limpios y fáciles de usar

______

## Actualizaciones de GNOME

Para GNOME, Kali Purple 2023.1 trae algunas mejoras de usabilidad, como la posibilidad de abrir rápidamente un terminal en la carpeta actual del gestor de archivos pulsando la tecla F4.

______

## Configuración por defecto del núcleo y problemas conocidos

Kali Purple 2023.1 actualiza algunos valores por defecto del kernel para una mejor usabilidad.

______

## Nuevas herramientas y paquetes

Kali Purple 2023.1 incorpora herramientas y paquetes para **pruebas de penetración** y **hacking ético**. Entre las novedades están:

- **Rizin 0.3.0**: un marco moderno de ingeniería inversa
- **Ghidra 10.1**: una suite de código abierto para ingeniería inversa de software
- **Python 3.10**: la versión más reciente del lenguaje de programación

Estas herramientas y las actualizaciones de paquetes existentes ampliaron la versión preliminar 2023.1 para profesionales de seguridad. Las versiones de este apartado describen el lanzamiento 2023.1 y no las versiones incluidas en Kali 2026.2.

______

## Soporte para dispositivos ARM

Kali Purple 2023.1 continúa ampliando su soporte para dispositivos ARM, añadiendo compatibilidad para nuevos dispositivos como el **Radxa Zero** y mejorando el soporte existente para dispositivos como el **LG V20**. Esta amplia gama de compatibilidad garantiza que Kali se pueda utilizar en una gran variedad de hardware, desde pequeños ordenadores de placa única hasta potentes smartphones.

______

## Documentación y comunidad

El equipo de Kali ha actualizado su **documentación** con nuevas guías, tutoriales y consejos para la resolución de problemas para ayudar a los usuarios a sacar el máximo provecho de Kali Purple 2023.1. También han reconocido a varios miembros de la comunidad por sus contribuciones a Kali, mostrando el poder de la colaboración de código abierto y la fuerza de la comunidad Kali.

______

## Normativa gubernamental

Aunque este artículo no cubre ninguna normativa gubernamental específica relacionada con el hacking ético o las pruebas de penetración, es importante tener en cuenta que estas actividades están reguladas en muchas jurisdicciones. Asegúrate siempre de que tienes los permisos adecuados y sigues las leyes aplicables cuando realices evaluaciones de seguridad. Para obtener más información sobre las normativas pertinentes, visite los siguientes recursos:

- [The Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
- [The General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## Conclusión

**Kali Purple 2023.1** fue la primera versión preliminar con funciones para la orientación defensiva de Kali. Amplió el conjunto de herramientas, mejoró la compatibilidad con ARM y reforzó la documentación. Para una instalación actual, consulta las notas de Kali y elige los paquetes adecuados para tu laboratorio. Cumple las normas aplicables y prueba sistemas solo con autorización expresa.

______

## Referencias

1. [Sitio web oficial de Kali Linux](https://www.kali.org/)
2. [Documentación de Kali Linux](https://www.kali.org/docs/)
3. [Descargas de Kali Linux](https://www.kali.org/get-kali/)
4. [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
5. [General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## Recursos adicionales

- [Foros oficiales de Kali Linux](https://forums.kali.org/)
- [Blog de Kali Linux](https://www.kali.org/blog/)
- [Formación y certificación de Kali Linux](https://www.offensive-security.com/)

______

## Lista de actualización

- **Consulta el historial de versiones.** Lee el [historial actual de versiones de Kali](https://www.kali.org/releases/) antes de descargar una imagen.
- **Usa imágenes oficiales.** Descarga desde [Get Kali](https://www.kali.org/get-kali/) y verifica las sumas de comprobación publicadas.
- **Actualiza las instalaciones rolling.** Sigue la [documentación actualizada de Kali](https://www.kali.org/docs/general-use/updating-kali/) en lugar de copiar sin revisar el ejemplo de repositorio de 2023.1.
- **Elige los metapaquetes con criterio.** Un laboratorio estándar o enfocado en Purple no requiere todos los paquetes de Kali.
- **Define el alcance del laboratorio.** Antes de ejecutar herramientas, especifica los sistemas autorizados, las ventanas de prueba, el registro y la limpieza.
