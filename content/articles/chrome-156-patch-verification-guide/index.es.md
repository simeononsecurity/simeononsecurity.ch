---
title: "Actualización de seguridad de Chrome 156: verifica el parche de octubre"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Comprueba la versión de seguridad de Chrome 156 del 27 de octubre en Windows, macOS, Linux y Android. Compara la compilación instalada, completa un reinicio pendiente y revisa por separado los dispositivos administrados."
genre: ["Navegadores", "Seguridad", "Gestión de parches"]
tags: ["Chrome 156", "actualización de seguridad de Chrome", "verificación de parches de Chrome", "comprobación de versión de Chrome", "Chrome 156 para Windows", "Chrome 156 para macOS", "Chrome 156 para Linux", "Chrome 156 para Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "parches de navegador", "Chrome Enterprise Core", "navegadores administrados", "seguridad de Chromium", "actualizaciones de navegador", "reinicio de Chrome", "chrome://version", "chrome://settings/help", "actualización de Chrome para Android", "actualizaciones de seguridad de Brave", "actualizaciones de seguridad de Edge"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Ilustración de un candado y un escudo que representan una actualización de seguridad, no una pantalla de versión de Chrome"
coverCaption: ""
---

**La versión de seguridad de Chrome del 27 de octubre de 2026** incluye 52 correcciones. Para comprobar tu instalación, compara la versión completa con la publicación correspondiente a tu sistema operativo y reinicia Chrome para completar cualquier actualización pendiente. El anuncio de una versión no demuestra que tu dispositivo haya recibido la actualización. ([Lanzamiento de Chrome para escritorio](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## ¿Qué versión deberías ver?

Google publicó estas versiones del canal Stable el 27 de octubre de 2026. El anuncio para escritorio enumera compilaciones distintas para Windows y macOS y para Linux. El [lanzamiento para Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) indica su propia compilación y señala que las versiones para Android incluyen las mismas correcciones de seguridad que las versiones de escritorio correspondientes, «salvo que se indique lo contrario».

| Plataforma | Compilación del anuncio de Google del 27 de octubre |
|---|---|
| **Windows** | 156.0.8078.73 o 156.0.8078.74 |
| **macOS** | 156.0.8078.73 o 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Usa esta tabla para el lanzamiento del 27 de octubre, no como un objetivo permanente. Consulta el [feed actual de versiones de Chrome](https://chromereleases.googleblog.com/) para ver futuras actualizaciones de seguridad.* Google dijo que el despliegue para escritorio tomaría «los próximos días o semanas» y que la compilación de Android llegaría a Google Play durante los próximos días. Si un dispositivo muestra una versión inferior a la indicada, debes revisarlo aunque el despliegue sea gradual. ([Aviso para escritorio](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [aviso para Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

La [lista de correcciones de seguridad para escritorio](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) clasifica cuatro fallos comunicados como **Critical**: corrupción de memoria en FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), validación de entrada incorrecta en FileAPI CVE-2026-118331, validación de entrada incorrecta en Skia CVE-2026-118348 y use-after-free en Layout CVE-2026-118344. El mismo aviso enumera otros CVE de nivel **High** y **Medium**. La cifra 52 describe las correcciones de seguridad incluidas en la versión, no 52 informes de explotación verificados de forma independiente. ([Registro de NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**El aviso de la versión no afirma que se estén explotando activamente estas vulnerabilidades.** La advertencia se refiere al momento de la divulgación: «El acceso a los detalles de los errores y a los enlaces podría permanecer restringido hasta que la mayoría de los usuarios haya recibido una corrección». No trates la restricción de esos detalles como prueba de explotación. ([Aviso para escritorio](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Comprueba y completa la actualización de escritorio

1. Abre **`chrome://version`** en la instalación de Chrome que utilizas. Anota la versión completa y el sistema operativo, no solo el número principal 156. Comprueba por separado las ventanas de Chrome de otro canal o instaladas en otra ubicación.
2. Abre **`chrome://settings/help`** o selecciona **Más > Ayuda > Información de Google Chrome**. Google indica que Chrome busca actualizaciones en esta página. Espera a que termine la comprobación. ([Instrucciones de actualización de Google para escritorio](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Selecciona **Reiniciar** si aparece esa opción. Guarda antes el trabajo pendiente. Cierra las demás ventanas de Chrome, vuelve a abrir el navegador y comprueba **`chrome://version`** otra vez. Compara con la tabla la versión que aparece después del reinicio.
4. Si la versión sigue por debajo de la compilación anunciada, vuelve a buscar actualizaciones. Si una organización administra el navegador o el actualizador informa de un error, ponte en contacto con el administrador. Una descarga correcta no demuestra que haya cambiado la versión del navegador en ejecución.

> **Resultado esperado:** Después de reiniciar, la compilación Stable de Chrome en ejecución cumple la versión de la plataforma indicada en el anuncio del 27 de octubre o una versión posterior anunciada por el proveedor. Un botón Reiniciar pendiente no demuestra que la actualización haya terminado.

En **Android**, abre Play Store > icono del perfil > Gestionar apps y dispositivo, y actualiza Chrome en Actualizaciones disponibles si aparece. En Chrome, abre Más > Configuración > Información de Chrome para ver la versión instalada. Compárala con la fila de Android después de que termine la actualización de la aplicación. Estas rutas de menú siguen las [instrucciones de Google para Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Verifica las flotas administradas

Para los navegadores inscritos, usa el **informe de versiones de Chrome** de la consola de administración de Google para localizar compilaciones antiguas según el sistema operativo. Abre la vista Browser Versions, selecciona la unidad organizativa correspondiente, revisa la versión menor completa y exporta el CSV si necesitas una lista de dispositivos para trabajar. Google indica que el informe incluye navegadores que enviaron informes durante los 28 días anteriores. También advierte que puede haber demoras, sobre todo en flotas grandes. ([Consulta los detalles de las versiones de Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Separa el inventario informado de la verificación en vivo.** Revisa la hora del último informe y el canal de cada dispositivo, y confirma las excepciones directamente en el navegador o mediante el inventario de dispositivos administrados. Google cuenta por separado las instalaciones distintas de Chrome, como Stable y Beta. Los informes de navegador requieren inscripción y [generación de informes de navegadores administrados](https://support.google.com/chrome/a/answer/9301421?hl=en). Que un equipo no aparezca en un informe no demuestra que tenga el parche.

## Comprueba por separado los derivados de Chromium

**La tabla de versiones de Chrome se aplica a Google Chrome.** Microsoft Edge, Brave y otros navegadores basados en Chromium tienen sus propios paquetes, números de versión y calendarios de actualización. El anuncio de Chrome no confirma su estado de parche. Comprueba la versión instalada de cada navegador y su propio aviso de seguridad o notas de versión para las correcciones pertinentes de Chromium. No compares directamente una versión de Edge o Brave con Chrome 156.0.8078.73 para declararla corregida.

Para cada derivado, anota el nombre del producto, el canal, la compilación instalada, la URL del aviso del proveedor y la compilación que el proveedor identifica como corregida. Si el proveedor no ha confirmado una corrección, marca el estado como **sin verificar** y sigue sus instrucciones de actualización. Mantén Chrome y los derivados en filas separadas del inventario.

## Fuentes y referencias

- [Chrome Releases: actualización del canal Stable para escritorio, 27 de octubre de 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Compilaciones de escritorio, 52 correcciones, CVE y texto del proveedor sobre la divulgación.
- [Chrome Releases: actualización de Chrome para Android, 27 de octubre de 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Compilación de Android y salvedad sobre las correcciones de escritorio correspondientes.
- [Rastreador de problemas de Chromium: consulta de correcciones de seguridad M156](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Enlace del anuncio para escritorio. El acceso a los detalles de cada problema depende de las restricciones de divulgación.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) y [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Descripciones de vulnerabilidades y versiones de Chrome afectadas. Los niveles de gravedad anteriores siguen el aviso de Google, no una evaluación CVSS de NVD.
- [Ayuda de Google Chrome: actualiza Chrome en ordenadores](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) y [en Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Comprobación de actualizaciones y rutas para consultar la versión.
- [Ayuda de Chrome Enterprise: consulta los detalles de la versión de Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en) y [activa los informes de navegadores administrados](https://support.google.com/chrome/a/answer/9301421?hl=en). Requisitos y límites de los informes de flota.
