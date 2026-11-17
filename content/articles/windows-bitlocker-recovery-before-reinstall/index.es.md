---
title: "Encuentra la clave de recuperación de BitLocker antes de reinstalar Windows"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Encuentra y verifica la clave de recuperación de BitLocker correcta, protege una copia aparte y elige la vía adecuada de recuperación o reinstalación de Windows antes de borrar una unidad."
genre: ["Seguridad de Windows", "Recuperación de datos", "Administración de sistemas"]
tags: ["clave de recuperación de BitLocker", "reinstalar Windows 11", "reinstalar Windows 10", "cifrado de dispositivo", "ID de clave de recuperación", "clave de recuperación de cuenta Microsoft", "clave de cuenta laboral o educativa", "copia de la clave de recuperación", "unidad cifrada", "instalación limpia", "recuperación de Windows", "copia de BitLocker", "clave de recuperación de 48 dígitos", "medio de instalación de Windows", "copia de seguridad de datos", "cifrado de disco", "lista de recuperación", "instalación de Windows", "solución de problemas de BitLocker", "preparación para reinstalar"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Un portátil con una unidad bloqueada, una tarjeta aparte con la clave de recuperación, una copia USB y una lista de recuperación marcada."
coverCaption: "Verifica la clave de recuperación antes de borrar la unidad."
---

Una instalación limpia de Windows borra la unidad seleccionada. Si la unidad anterior usa **BitLocker** o **Cifrado de dispositivo**, localiza la clave de recuperación y copia tus archivos antes de empezar. La clave permite acceder a los datos cifrados anteriores. Una nueva instalación de Windows no restaura los archivos borrados de la unidad.

<!--more-->

## Puntos clave

- **Encuentra la clave correcta:** compara el ID que muestra Windows con la clave de tu cuenta, una copia impresa o un respaldo USB.
- **Comprueba el acceso:** inspecciona la copia, compara el ID y desbloquea la unidad antes de borrar particiones.
- **Protege la copia:** guarda la clave de 48 dígitos separada del equipo y del USB de instalación.
- **Elige la vía adecuada:** usa las opciones de recuperación si necesitas la instalación anterior. Haz una instalación limpia solo después de verificar una copia independiente de tus archivos.

## Antes de empezar

Necesitas acceso al equipo afectado, otro dispositivo para revisar tu cuenta o copia, y una unidad externa o almacenamiento en la nube de confianza para los archivos importantes. **Tiempo:** localizar la clave depende del acceso a la cuenta. Copiar archivos depende de la cantidad de datos. **Dificultad:** básica para revisar la cuenta, intermedia para las herramientas de recuperación. Esta guía trata la preparación y las decisiones de recuperación para Windows 10 y Windows 11. La [guía de instalación limpia de Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) cubre los medios y la configuración.

*El soporte estándar de Windows 10 terminó el 14 de octubre de 2025. Planifica una instalación compatible de Windows 11 si tu equipo cumple los requisitos. Microsoft enumera el [ciclo de vida de Windows 10 y las opciones de soporte extendido](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Advertencia:** no elimines una partición para resolver una solicitud de recuperación de BitLocker si todavía necesitas archivos de la instalación anterior. Microsoft indica que un restablecimiento sin la clave elimina esos archivos. Consulta las [indicaciones de Microsoft sobre la clave de recuperación](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Comprueba si el cifrado está activo

**Cifrado de dispositivo** y **BitLocker** cifran una unidad para impedir que alguien sin las credenciales adecuadas lea su contenido. Si Windows todavía inicia, en Windows 11 abre **Configuración > Privacidad y seguridad > Cifrado de dispositivo**. En las ediciones con administración de BitLocker, busca **Administrar BitLocker** en Inicio. Anota la letra de la unidad cifrada y la cuenta usada para configurar el equipo. En un equipo laboral o educativo administrado, la organización suele guardar la clave.

También puedes revisar el estado desde la línea de comandos. Busca **Símbolo del sistema** en Inicio, selecciona **Ejecutar como administrador** e introduce estos comandos. Sustituye `C:` si Windows usa otra letra. Un **protector** es un método que Windows usa para desbloquear una unidad cifrada.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

El primer comando muestra el estado del cifrado, la protección y el bloqueo. El segundo enumera tipos e ID de protectores y podría mostrar la contraseña de recuperación. Microsoft documenta ambas comprobaciones en su [guía de operaciones de BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) y la [referencia del comando de estado](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **No pegues la salida en una solicitud de ayuda ni la compartas en una captura.** Si el equipo ya está bloqueado, usa el ID de la pantalla de recuperación. Los primeros ocho dígitos ayudan a elegir la clave correcta.

## Dónde encontrar la clave de recuperación de BitLocker

El **ID de la clave de recuperación** identifica una clave guardada. La **clave de recuperación** es el número independiente de 48 dígitos que se introduce para desbloquear la unidad. No pongas el ID en el campo de contraseña de recuperación.

| Equipo o copia de seguridad | Dónde buscar |
|---|---|
| **Cuenta personal de Microsoft** | En otro dispositivo, inicia sesión en la [página de claves de recuperación de Microsoft](https://aka.ms/myrecoverykey). Compara el ID antes de usar la clave de 48 dígitos. |
| **Equipo laboral o educativo** | Revisa la cuenta de la organización mediante la [página de Microsoft para cuentas laborales o educativas](https://aka.ms/aadrecoverykey), o consulta al equipo de TI. |
| **Copia impresa o USB** | Busca la impresión o el archivo de texto creado al activar el cifrado. Compara su ID con el que aparece en pantalla. |

Microsoft enumera estos lugares en [Encuentra la clave de recuperación de BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Empieza por la clave cuyo ID coincide con la solicitud. Una clave de otro dispositivo o de un protector eliminado quizá no desbloquee este volumen. Si otra persona configuró el equipo, su cuenta podría guardar la clave.

## Crea una copia independiente de la clave

Si Windows todavía inicia en una edición Pro, Enterprise o Education, busca **Administrar BitLocker**. Junto a la unidad cifrada, selecciona **Hacer una copia de seguridad de la clave de recuperación**. Microsoft ofrece guardarla en una cuenta, unidad USB, archivo de texto o impresión. Si eliges un archivo o USB, guárdalo solo en un medio cifrado con control de acceso y separado del equipo. No uses una ubicación sin cifrar. Consulta [Hacer una copia de seguridad de la clave de recuperación de BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key) para ver la interfaz y las opciones actuales.

En Windows Home no aparece **Administrar BitLocker**. En Windows 11 revisa **Configuración > Privacidad y seguridad > Cifrado de dispositivo** y confirma la clave en la cuenta Microsoft usada durante la configuración. Microsoft explica que [Cifrado de dispositivo](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) guarda la clave en la cuenta Microsoft o laboral vinculada al activarse. Guarda otra copia protegida si la configuración permite exportarla.

Abre una copia digital desde otro dispositivo. Si es impresa, compárala con la entrada de la cuenta o la pantalla de recuperación. Compara el **ID de la clave de recuperación** con el que aparece en pantalla o en la lista de protectores. Comprueba que incluya los 48 dígitos de la clave asociada. Guarda la copia impresa o extraíble lejos del equipo cifrado. Quien robe el equipo y la clave podría eludir la protección del disco, advierte Microsoft en sus [indicaciones de copia de seguridad](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). No adjuntes la clave a un ticket de soporte.

> **Resultado esperado:** tienes una clave de recuperación coincidente fuera del equipo.

## Desbloquea un equipo que no inicia

Si aparece la **pantalla de recuperación de BitLocker**, introduce la clave de 48 dígitos que coincide con su ID. Si Windows inicia, copia tus archivos antes de cambiar particiones. Si la clave desbloquea la unidad pero Windows sigue sin iniciar, abre el [Entorno de recuperación de Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) e intenta **Reparación de inicio** antes de restablecerlo. Algunas herramientas necesitan la clave mientras la unidad está cifrada.

Para copiar archivos desde las herramientas de recuperación, abre **Solucionar problemas > Opciones avanzadas > Símbolo del sistema** en el Entorno de recuperación de Windows. Usa `manage-bde -status` y `dir` para identificar el volumen de Windows cifrado y otra unidad externa para la copia. **Las letras pueden diferir de las de Windows normal.** No copies al USB de instalación ni a la unidad de origen cifrada.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

Las letras son ejemplos. Cuando identifiques los volúmenes correctos, desbloquea el de Windows con la clave coincidente. Sustituye la letra de ejemplo y el marcador por tus propios valores. Escribe localmente la clave real de 48 dígitos. No publiques ni compartas la salida.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

La opción documentada `-recoverypassword` recibe la clave de 48 dígitos como argumento. Esto la expone al historial de shell, las transcripciones y la inspección de procesos. Usa la pantalla de recuperación de Windows si quieres introducir la clave sin un argumento de línea de comandos. Si guardaste un archivo de clave `.bek` aparte, `-recoverykey <path-to-external-bek>` evita escribir los 48 dígitos. No muestres la clave en capturas ni tickets.

Microsoft documenta el [comando de desbloqueo](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). Sus [indicaciones de recuperación](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) también describen cómo copiar archivos de usuario a otra unidad después de desbloquearla. Para copiar como ejemplo Documentos, confirma primero el nombre de la cuenta de Windows y la letra de la unidad externa, y sustituye ambas rutas:

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

Las opciones **`/S /E`** incluyen subcarpetas, también las vacías. **`/I`** trata el destino como carpeta, **`/H`** incluye archivos ocultos y **`/V`** comprueba cada archivo escrito. Microsoft documenta estas opciones en la [referencia de xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Repite el proceso para otras carpetas necesarias. Abre los archivos copiados en otro dispositivo antes de borrar la unidad de Windows. Si no puedes identificar los volúmenes o falla la copia, detente y consulta a un especialista de recuperación de confianza.

## Elige si vas a reinstalar

**Una copia de la clave no es una copia de los archivos.** Sigue este orden antes de elegir una vía de reinstalación:

1. Identifica la unidad cifrada y su ID de clave de recuperación.
2. Recupera la clave de 48 dígitos coincidente desde tu cuenta, impresión o copia USB.
3. Si la unidad está bloqueada, desbloquéala desde la pantalla o las herramientas de recuperación.
4. Copia Escritorio, Documentos, Imágenes y otras carpetas locales a una unidad externa o nube de confianza. Incluye exportaciones del navegador, datos de aplicaciones y registros de licencias si hace falta.
5. Abre varios archivos copiados desde otro dispositivo.
6. Elige una reparación, un restablecimiento o una reinstalación solo después de comprobar la copia.

> **Resultado esperado:** la clave correcta y los archivos importantes están disponibles fuera de la instalación anterior.

Microsoft enumera [las opciones de recuperación de Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows) y sus distintos efectos en archivos y aplicaciones. Muchas opciones del Entorno de recuperación de Windows exigen la clave cuando BitLocker protege la unidad. Si el volumen está bloqueado allí, **Conservar mis archivos** no lo desbloquea sin la clave.

**Reparación de inicio** y **Restaurar sistema** intentan reparar la instalación existente. **Restablecer este PC** ofrece **Conservar mis archivos**, pero elimina aplicaciones y configuración. **Quitar todo** borra los archivos personales. Iniciar **`setup.exe` desde una sesión de Windows activa** ofrece una reinstalación en el sitio con opciones para conservar datos. Elegir **Instalar Windows** después de arrancar desde un USB inicia una instalación limpia que elimina archivos, aplicaciones y configuración de la instalación seleccionada. El mismo medio también ofrece una vía de reparación. Lee la opción mostrada y verifica el disco de destino antes de confirmar. Microsoft explica ambas vías en las [instrucciones de reinstalación](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Situación | Acción siguiente |
|---|---|
| **Windows inicia y necesitas los archivos** | Haz una copia de los archivos, verifica la clave y luego elige una reparación o reinstalación. |
| **Windows solicita la clave** | Compara el ID en pantalla con una clave guardada antes de cambiar el disco. |
| **No hay clave coincidente ni copia de archivos** | Detente antes de borrar la unidad. Revisa cada cuenta, impresión y copia USB, y consulta a TI. |
| **Los archivos están copiados y quieres empezar de cero** | Sigue las [instrucciones de reinstalación de Microsoft](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) y elige con cuidado el disco de destino. |

Microsoft dice que el personal de soporte no puede recrear una clave perdida. Si no la encuentras, deja de cambiar la configuración del firmware y revisa todas las ubicaciones de respaldo. Pide ayuda al administrador si el equipo está administrado. Un restablecimiento sin la clave necesaria elimina los archivos anteriores. Una instalación limpia también elimina archivos personales, aplicaciones, personalizaciones y configuración de la instalación elegida. Toma esa decisión después de revisar la copia.

## Solución de problemas

- **La clave no funciona:** vuelve a comprobar el ID y la cuenta. Un equipo puede tener varias claves guardadas.
- **No aparece Administrar BitLocker:** Windows Home usa Cifrado de dispositivo en equipos compatibles. Revisa Configuración y la cuenta Microsoft usada al configurar el equipo.
- **Aparecen varias claves en una cuenta:** compara los primeros ocho dígitos del ID de la pantalla con las entradas guardadas. No elijas una clave solo por el nombre del equipo.
- **La clave desbloquea la unidad, pero Windows no inicia:** prueba Reparación de inicio desde el Entorno de recuperación de Windows. Copia los archivos accesibles antes de restablecer o instalar de cero.
- **El trabajo o la escuela guardan la clave:** contacta al administrador antes de restablecer o reinstalar el equipo.
- **El archivo de la clave está en el equipo bloqueado:** busca una cuenta separada, impresión o copia extraíble. Una copia solo en la unidad cifrada no sirve mientras esté bloqueada.
- **La solicitud apareció tras un cambio de firmware:** anota el cambio y no hagas más. Busca la clave correcta o contacta al administrador.

## Pasos siguientes

Después de verificar la clave y los archivos, sigue la [guía de instalación limpia de Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) si se ajusta a tu objetivo. Cuando Windows inicie, revisa **Configuración > Privacidad y seguridad > Cifrado de dispositivo** o busca **Administrar BitLocker**. En Pro, Enterprise o Education, selecciona **Hacer una copia de seguridad de la clave de recuperación**. En Home, verifica que la cuenta vinculada tenga la clave actual y guarda otra copia si Windows permite exportarla. No supongas que la clave anterior sirve para una instalación nueva cifrada.
