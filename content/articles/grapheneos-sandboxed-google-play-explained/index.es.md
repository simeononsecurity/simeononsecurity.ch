---
title: "Sandboxed Google Play en GrapheneOS, explicado"
date: 2026-09-11
lastmod: 2026-11-20
toc: true
draft: false
description: "Descubra qué cambia Sandboxed Google Play en GrapheneOS, cuándo conviene usar un perfil separado y cómo se relacionan las cuentas, las notificaciones y la compatibilidad de las aplicaciones."
genre: ["Privacidad", "Seguridad móvil", "Código abierto"]
tags: ["GrapheneOS", "Sandboxed Google Play", "Google Play services", "Google Play Store", "privacidad de Android", "seguridad de Android", "aislamiento de aplicaciones", "cuenta de Google", "perfiles de GrapheneOS", "perfil del propietario", "perfiles de usuario", "perfil de trabajo", "compatibilidad de aplicaciones", "notificaciones push", "Firebase Cloud Messaging", "permisos de aplicaciones", "privacidad de Pixel", "instalación de Google Play", "privacidad móvil", "GrapheneOS App Store"]
cover: "/img/cover/grapheneos-sandboxed-google-play-explained.webp"
coverAlt: "La pantalla de un teléfono muestra aplicaciones en compartimentos transparentes separados, incluido un símbolo colorido de una tienda de aplicaciones."
coverCaption: ""
---

**Sandboxed Google Play** permite instalar los componentes oficiales de Google Play en GrapheneOS como aplicaciones normales. Se ejecutan sin los privilegios del sistema que Google Play suele recibir en el sistema operativo estándar. La instalación es opcional. [Descripción general de las funciones de GrapheneOS](https://grapheneos.org/features#sandboxed-google-play).

## Puntos clave

- **Entienda el aislamiento:** distinga los permisos de las aplicaciones de la actividad de las cuentas en línea.
- **Agrupe las dependencias:** mantenga en el mismo perfil la aplicación dependiente y Play.
- **Pruebe el funcionamiento:** compruebe las notificaciones en segundo plano y los flujos de trabajo esenciales.
- **Prepare un plan:** anote los perfiles, las cuentas y los requisitos de las aplicaciones que eligió.

## Antes de comenzar

**Público:** usuarios de GrapheneOS que deciden si instalar Google Play y dónde colocarlo. **Requisitos:** un dispositivo compatible con GrapheneOS actualizado y acceso a sus cuentas esenciales. La instalación del sistema operativo se describe en la [guía de instalación de GrapheneOS](/guides/how-to-install-graphine-os/).

**Tiempo estimado:** entre 20 y 30 minutos para hacer un inventario inicial de las aplicaciones y las comprobaciones, más el uso diario habitual para evaluar la fiabilidad de las notificaciones. **Dificultad:** principiante. Empiece con una aplicación representativa antes de reorganizar el teléfono.

## Qué cambia con el aislamiento

El **aislamiento de aplicaciones** de Android separa los recursos de las aplicaciones mediante protecciones del sistema operativo. Una aplicación no obtiene acceso ilimitado a los archivos privados de otra. La protección se aplica tanto al código nativo como al que se ejecuta en el entorno administrado de Android. [Documentación del aislamiento de aplicaciones de Android](https://source.android.com/docs/security/app-sandbox).

GrapheneOS añade una **capa de compatibilidad** para que los componentes oficiales de Play funcionen con esas restricciones habituales. Las aplicaciones del mismo perfil conservan formas compatibles de comunicarse con consentimiento mutuo. El aislamiento limita privilegios, pero no impide todos los intercambios intencionales entre aplicaciones. [Diseño de Sandboxed Google Play](https://grapheneos.org/features#sandboxed-google-play).

| Aspecto | Significado práctico |
|---|---|
| **Archivos privados de las aplicaciones** | Instalar Play no concede acceso ilimitado a los datos de otras aplicaciones |
| **Permisos** | Revise el acceso solicitado como lo haría con cualquier otra aplicación |
| **Funciones de Google** | Si una aplicación elige un servicio de Google, seguirá comunicándose con él |
| **Actividad de la cuenta** | Iniciar sesión en un servicio sigue siendo una decisión de privacidad independiente |

**El aislamiento y la privacidad de la cuenta** responden preguntas diferentes. El aislamiento restringe el acceso local. No borra la información que usted envía deliberadamente a un servicio en línea. Por ejemplo, iniciar sesión en una aplicación de compras sigue identificando su cuenta ante quien la opera.

## Separe tres decisiones de privacidad

**El acceso local, el uso de servicios y la identidad** son cuestiones distintas. Si una aplicación solicita acceso a los contactos e iniciar sesión en una cuenta, revise cada solicitud por separado:

| Decisión | Pregunta |
|---|---|
| **Permiso local** | ¿Esta función necesita mis contactos, micrófono o ubicación? |
| **Dependencia de un servicio** | ¿Qué función depende de servicios de Google Play? |
| **Identidad en línea** | ¿A qué cuenta estoy asociando esta actividad? |

**Ejemplo práctico:** una cuenta de compras ya contiene su dirección de entrega. Mover su aplicación a otro perfil no cambia la dirección que conserva el comercio. Rechazar el acceso a los contactos responde a otra pregunta, sobre los datos disponibles en el teléfono.

**Objetivo de privacidad:** anote la exposición concreta que quiere reducir. “Evitar que esta aplicación acceda a mis contactos personales” se puede comprobar. “Hacer anónima esta cuenta” requiere decisiones que van más allá de elegir un perfil.

## ¿Perfil del propietario o perfil separado?

**Instalar en el perfil del propietario** es una opción sencilla y compatible. Google Play sigue aislado allí. Un perfil de usuario o de trabajo separado permite elegir qué grupo de aplicaciones tendrá acceso a Play. [Instrucciones de instalación de GrapheneOS](https://grapheneos.org/usage#sandboxed-google-play-installation).

| Prioridad | Configuración inicial | Compromiso |
|---|---|---|
| **Uso diario sencillo** | Mantener las aplicaciones necesarias y Play en Propietario | Play está disponible para las aplicaciones que colaboran en ese perfil |
| **Separar aplicaciones dependientes de Google** | Instalarlas juntas en otro perfil | Más administración de perfiles |
| **Evitar los servicios de Google** | Empezar sin Play | Revisar las dependencias de cada aplicación |

**La ubicación en el perfil** importa más que instalar el mismo componente en todas partes. Las preguntas frecuentes de GrapheneOS explican cómo se limita Play a los perfiles seleccionados. Muchas aplicaciones funcionan sin él o lo necesitan solo para parte de sus funciones. [Preguntas frecuentes sobre los servicios de Google](https://grapheneos.org/faq#google-services).

*Use un perfil separado cuando el acceso selectivo a Play resuelva una necesidad concreta que ya haya identificado.*

## Comprenda la actividad de los perfiles

**Un perfil de usuario secundario** tiene sus propias instancias de las aplicaciones y sus propios datos. Cambiar a otro usuario y terminar la sesión del anterior son acciones distintas. **Terminar sesión** detiene las aplicaciones del perfil secundario y devuelve su almacenamiento cifrado al estado de reposo. [Preguntas frecuentes de GrapheneOS sobre el cifrado y los perfiles](https://grapheneos.org/faq#encryption).

**El reenvío de notificaciones** puede mostrar al usuario activo las notificaciones de un usuario que funciona en segundo plano. No mantiene activa una sesión que ya terminó. [Funciones de los perfiles de usuario de GrapheneOS](https://grapheneos.org/features).

| Estado del perfil | Condición de entrega |
|---|---|
| **Activo** | Pruebe la entrega dentro de este perfil |
| **En segundo plano** | Compruebe el reenvío al usuario activo |
| **Sesión terminada** | Las aplicaciones de este perfil están detenidas |

Para **una aplicación de mensajería de uso diario**, decida si es esencial recibir mensajes mientras usa Propietario. Una configuración que exige terminar sesiones con frecuencia entra en conflicto con la entrega continua en segundo plano. Valore esta diferencia antes de mover el historial de sus conversaciones principales.

## Instalación y cuentas

Abra la **GrapheneOS App Store** integrada, seleccione **Google Play services** e instálelo. También se instalará Play Store, que depende de ese componente. Deje que App Store mantenga estos componentes. Excluya servicios de Google Play de la optimización de batería para que funciones en segundo plano, como las notificaciones push, sean fiables. [Instrucciones oficiales de instalación](https://grapheneos.org/usage#sandboxed-google-play-installation).

**Iniciar sesión con una cuenta de Google** es opcional para funciones que no dependen de una cuenta. Para instalar aplicaciones desde Play Store sí se requiere iniciar sesión. Las instalaciones antiguas también incluyen Google Services Framework, que el proyecto recomienda conservar. Siga las instrucciones actuales en vez de una lista antigua de tres paquetes.

## Pruebe primero una aplicación

Use una **aplicación representativa de bajo riesgo** para comprobar la configuración prevista de los perfiles. Durante la prueba, mantenga disponibles sus métodos actuales de recuperación de cuentas.

1. **Elija un perfil:** decida dónde irá la aplicación antes de instalar sus dependencias.
2. **Instale Play:** siga en este perfil los pasos oficiales anteriores.
3. **Instale la aplicación:** use una fuente de distribución confiable y complete la configuración inicial.
4. **Revise las solicitudes:** apruebe permisos adecuados a la función que está probando.
5. **Pruebe una función:** envíe un mensaje, abra un mapa o realice otra acción reversible.
6. **Registre el resultado:** anote las versiones de la aplicación y del sistema, el perfil y la operación exacta.

**Prueba esperada:** una descripción repetible, como “llegó un mensaje de prueba con la pantalla bloqueada y el perfil activo”. No anote solo “funciona”, porque omite la función y las condiciones probadas.

## Diagnostique la falta de notificaciones

Las **notificaciones push** dependen de la implementación de la aplicación. Algunas mantienen su propia conexión en segundo plano. Otras dependen de Firebase Cloud Messaging de Google. Que una aplicación se abra no demuestra que sus notificaciones lleguen después de bloquear el teléfono. [Preguntas frecuentes de GrapheneOS sobre notificaciones](https://grapheneos.org/faq#notifications).

**Compruebe las condiciones de entrega** antes de cambiar los permisos de varias aplicaciones:

| Síntoma | Cómo acotar la investigación |
|---|---|
| **Los mensajes aparecen solo después de abrir la aplicación** | Revise el método de entrega en segundo plano y los ajustes de batería |
| **La entrega funciona solo en su perfil** | Revise la actividad del perfil y el reenvío de notificaciones |
| **No llegan después de Terminar sesión** | Inicie el perfil secundario antes de volver a probar |
| **La notificación llega sin sonido** | Revise el canal de notificaciones y los ajustes de sonido de la aplicación |

Los **canales de notificación** agrupan el comportamiento de las notificaciones de una aplicación, incluida su importancia y sonido. Android ofrece al usuario controles para esos canales. [Documentación de Android sobre canales de notificación](https://developer.android.com/develop/ui/compose/notifications/channels).

**Repita la prueba y cambie una condición a la vez:** mantenga fijos el dispositivo emisor y el tipo de mensaje mientras cambia el estado del perfil receptor. Registre “activo”, “en segundo plano” o “sesión terminada” con cada resultado. Así podrá distinguir un problema del ciclo de vida del perfil de uno de configuración de notificaciones.

## Evalúe los flujos de trabajo esenciales

Antes de depender de una nueva configuración, haga una breve **prueba personal de aceptación**:

| Flujo de trabajo | Comprobación en el dispositivo |
|---|---|
| **Mensajería** | Recibir un mensaje con la pantalla bloqueada |
| **Acceso a la cuenta** | Iniciar sesión y completar el segundo factor requerido |
| **Banca o pagos** | Probar la función exacta que necesita, incluidas las comprobaciones del dispositivo |
| **Navegación** | Obtener la ubicación con los permisos elegidos |

**Que una aplicación se inicie** es solo la primera comprobación. Al resolver problemas, registre las versiones de la aplicación y GrapheneOS, y la operación que falló. Este artículo ofrece un marco de decisión, no una lista de compatibilidad probada.

**Decisión de migración:** conserve el método de acceso anterior hasta que todas las operaciones esenciales hayan superado la prueba. Una aplicación de mensajería y una bancaria necesitan criterios de aceptación distintos. Recibir un mensaje no demuestra nada sobre las comprobaciones de cuenta o dispositivo de otra aplicación.

**Repita las comprobaciones después de actualizar GrapheneOS o las aplicaciones.** La ubicación del perfil, los permisos, los canales de notificación y el estado de la sesión siguen definiendo la prueba. Anote la versión junto a cada resultado para que un cambio en las notificaciones o el inicio de sesión no se convierta en una conclusión de privacidad sin fundamento.

Para **un inicio de sesión de trabajo**, pruebe toda la secuencia y el segundo factor requerido. En una aplicación de viajes, pruebe la función que espera usar fuera de casa. Elija acciones representativas sin compras innecesarias ni cambios en la seguridad de la cuenta.

## Organice su inventario de aplicaciones

Complete este **inventario** para sus cinco aplicaciones más importantes. Las filas son indicaciones, no afirmaciones de compatibilidad de productos concretos:

| Categoría de aplicación | Requisito que debe anotar | Prueba que debe reunir |
|---|---|---|
| **Mensajería** | Entrega en segundo plano y perfil elegido | Prueba con pantalla bloqueada y perfil en segundo plano |
| **Acceso al trabajo** | Inicio de sesión y segundo factor requeridos | Inicio de sesión completado |
| **Navegación** | Permiso de ubicación y necesidades sin conexión | Una ruta en las condiciones previstas |
| **Banca** | Operaciones esenciales compatibles | Resultados de cada función requerida |
| **Compras** | Acceso a la cuenta y a los datos locales | Revisión de permisos y uso habitual de la cuenta |

**Registre una decisión** para cada fila: perfil elegido, dependencia de Play, requisito de cuenta, permisos aprobados y alternativa. Marque como desconocidas las dependencias que aún no haya comprobado. Así evitará instalar componentes adicionales solo porque otra aplicación los necesitaba.

**Ejercicio:** una aplicación funciona mientras su perfil secundario está activo, pero deja de recibir mensajes al terminar la sesión. Primero reinicie el perfil y repita la prueba. Dar acceso a los contactos no resolvería una sesión detenida.

**Criterio de finalización:** su plan explica por qué cada aplicación está en el perfil elegido y qué prueba respalda la decisión de confiar en ella. Revise la fila correspondiente cuando una actualización cambie su comportamiento.

## Próximos pasos

Use la [guía de instalación de GrapheneOS](/guides/how-to-install-graphine-os/) del sitio si todavía no ha instalado el sistema operativo. Luego elija una configuración de perfiles y pruebe las aplicaciones esenciales antes de añadir más perfiles o cambiar permisos generales.
