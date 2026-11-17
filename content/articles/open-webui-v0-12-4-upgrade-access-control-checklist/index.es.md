---
title: "Open WebUI v0.12.4: lista de actualización y control de acceso 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Haz una copia de seguridad y actualiza Open WebUI a v0.12.4. Después, prueba el uso compartido de chats, los permisos de exportación, las concesiones de recursos, las cuentas y el acceso a la red."
genre: ["IA autoalojada", "Ciberseguridad", "Administración de sistemas"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "actualización de Open WebUI", "seguridad de Open WebUI", "control de acceso de Open WebUI", "IA autoalojada", "actualización de Docker", "actualización de pip", "copia de seguridad de Open WebUI", "permisos de Open WebUI", "roles de Open WebUI", "grupos de Open WebUI", "permiso de exportación de chats", "chats compartidos", "chats archivados", "acceso a la base de conocimientos", "acceso a modelos", "permisos de herramientas", "seguridad de claves API", "seguridad de la cuenta de administrador", "desactivar registros", "autenticación de proxy inverso", "acceso VPN", "fijación de imagen de contenedor"]
---

**Open WebUI v0.12.4 incluye correcciones de seguridad que sus responsables aún no han detallado.** Las notas de la versión recomiendan actualizar pronto las implementaciones e indican que publicarán avisos cuando se asignen CVE. Los cambios mencionados sobre compartir chats y permisos son los elementos visibles en las notas, no una lista completa de las correcciones de seguridad aún no divulgadas. [Notas de la versión de Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Conclusiones clave

- **Haz primero una copia de seguridad.** Conserva una copia recuperable del volumen de datos o de la base de datos y de las cargas antes de cambiar la aplicación.
- **Fija la versión oficial.** Usa `ghcr.io/open-webui/open-webui:v0.12.4` para la imagen Docker estándar o `open-webui==0.12.4` para pip.
- **Prueba los permisos con roles de usuario reales.** Que un botón esté oculto no demuestra que exista una comprobación de autorización en la API.
- **Mantén el acceso privado.** Exige autenticación en la aplicación y limita el acceso a la red mediante una VPN o un proxy inverso autenticado.

## Antes de actualizar

**Requisitos previos:** identifica el método de instalación actual, la variante de la imagen del contenedor, la ubicación de los datos persistentes, la base de datos externa, el proxy inverso y el proveedor de autenticación. Programa una ventana de interrupción y conserva la configuración del contenedor o la definición del servicio actual. Reserva tiempo para ensayar una restauración en una instancia separada. Los comandos siguientes son patrones documentados por el proveedor y adaptados a esta versión fijada. No son el resultado de una actualización real hecha para esta guía. [Actualizar Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **Inventaría el almacenamiento.** En la configuración Docker estándar, `open-webui` se monta en `/app/backend/data`. Registra los montajes enlazados, la base de datos externa, el almacenamiento de objetos y las variables de entorno personalizadas. Con pip, localiza el directorio de datos activo de la aplicación y la base de datos antes de cambiar el entorno. No supongas que una exportación de chats es una copia de seguridad completa.
2. **Haz una copia de seguridad con las escrituras detenidas.** Detén la aplicación o usa una instantánea coherente de la base de datos. Después, copia el volumen, la base externa y las cargas a otro almacenamiento. El proveedor documenta un archivo del volumen Docker. Adapta el nombre del volumen y la ruta de copia de seguridad a tu implementación. Comprueba que el archivo se abre y ensaya una restauración en otra instancia antes de confiar en él. [Copia de seguridad y restauración](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Lee las notas de la versión y las instrucciones de migración.** Las notas de v0.12.4 no enumeran las correcciones de seguridad pendientes ni indican sus versiones afectadas. No asignes un CVE a esas correcciones ni supongas que todas las versiones anteriores a v0.12.4 están afectadas por un fallo concreto. La guía de actualización advierte de migraciones de base de datos unidireccionales y de réplicas con versiones mixtas. Si varios trabajadores o réplicas comparten una base de datos, detenlos a la vez y sigue el [procedimiento de migración para varias réplicas](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Una reversión podría requerir la copia de seguridad de la base de datos anterior a la actualización.

## Actualiza el paquete instalado

**Docker, procedimiento del proveedor adaptado a una etiqueta fijada:** después de la copia, descarga la imagen estándar oficial y vuelve a crear el contenedor con el *mismo* volumen persistente, configuración y `WEBUI_SECRET_KEY`. El ejemplo supone el volumen con nombre predeterminado y un proxy enlazado localmente como destino. No pegues tu clave real en el historial del shell. Proporciónala mediante tu mecanismo existente de entorno protegido o gestión de secretos. Conserva las opciones de GPU, Ollama, red personalizada, base de datos y demás opciones de tu implementación. [Actualizar Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Etiquetas oficiales de imágenes](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Comprueba `./open-webui.env` antes de ejecutar:** el archivo ya debe existir, tener permisos restrictivos y contener tu `WEBUI_SECRET_KEY` actual y la configuración necesaria. La vinculación a loopback sirve para un proxy en el mismo host, no para uno en otra máquina. Con Compose, cambia solo la imagen del servicio por la etiqueta fijada. Después, ejecuta `docker compose pull open-webui` y `docker compose up -d open-webui` en el proyecto actual. Conserva el volumen y la configuración de entorno. Son comandos sugeridos, no una migración probada de tu implementación.

**pip, procedimiento del proveedor para actualizar a una versión fija:** en el entorno virtual actual, detén el servicio, instala la versión exacta del paquete y reinícialo con el mismo directorio de datos y entorno. Evita crear otro entorno de Python o una base de datos vacía. La instrucción genérica del proveedor usa `pip install -U open-webui`. La restricción de versión siguiente fija esta lista a v0.12.4. [Actualizar Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Inicio rápido](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Verifica el servicio en ejecución, no solo el artefacto instalado.** Comprueba la versión de inicio en `docker logs open-webui` o en los registros del servicio pip y compárala con la versión que muestra la aplicación tras iniciar sesión. La guía de actualización del proveedor recomienda revisar los registros del contenedor y cargar la página de inicio de sesión. Si la interfaz muestra recursos obsoletos, fuerza la recarga del navegador. Si el inicio informa de un error de migración, mantén el servicio fuera de línea hasta diagnosticarlo. No instales un binario antiguo sobre una base de datos migrada sin revisar los requisitos de restauración. [Comprobaciones posteriores a la actualización](https://docs.openwebui.com/getting-started/updating/)

## Comprueba el acceso después de reiniciar

**Comportamiento indicado por el proveedor:** v0.12.4 oculta Exportar de carpetas, Exportar de chats archivados y Copiar chats a usuarios sin **Allow Chat Export**. También oculta los controles de acceso en modelos, prompts, herramientas, conocimientos, habilidades, notas y carpetas a usuarios sin el permiso de uso compartido correspondiente. Quienes consultan una carpeta compartida dejan de recibir actualizaciones de chat en directo cuando el propietario archiva un chat. Quienes usan un enlace compartido dejan de recibirlas cuando el propietario deja de compartir todos los chats. Los controles ocultos son comportamiento de la interfaz, no prueba de una corrección del servidor para una vulnerabilidad no especificada. [Notas de la versión](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Verificación recomendada para el operador:** con una cuenta de prueba sin permisos de exportación ni uso compartido, comprueba que no aparezcan las acciones indicadas. Con una cuenta autorizada, confirma que las acciones previstas siguen funcionando. Crea un chat de prueba no sensible en una carpeta compartida, ábrelo desde otra cuenta, archívalo como propietario y confirma que dejan de llegar actualizaciones nuevas al usuario. Repite la prueba con un enlace compartido y **Unshare All Chats**. Vuelve a comprobar las concesiones guardadas y los enlaces antiguos. No supongas que se borraron el contenido archivado ni las copias históricas.

| Área de revisión | Qué verificar |
|---|---|
| **Roles y grupos** | Elimina miembros y asignaciones de administrador obsoletos. Comprueba los permisos efectivos de un usuario recién aprobado y de uno restringido. |
| **Modelos y herramientas** | Revisa las concesiones de acceso de cada modelo, las herramientas adjuntas, los derechos para crear herramientas y las credenciales del proveedor. Prueba con una cuenta no administradora. |
| **Conocimientos y archivos** | Inspecciona los colaboradores de la base de conocimientos, las concesiones de recursos, los adjuntos y la configuración de uso compartido. Comprueba una cuenta a la que se le retiró el acceso. |
| **Chats y exportaciones** | Revisa las carpetas compartidas, los enlaces, los chats archivados y las asignaciones de Allow Chat Export. Revoca los enlaces innecesarios. |

Estas comprobaciones de inventario son **recomendaciones para el operador**, no nuevas garantías de v0.12.4. La [guía de endurecimiento](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) del proveedor documenta roles por capas, grupos, concesiones por recurso, permisos del espacio de trabajo, claves API y ubicación de red.

## Cierra las brechas de cuentas y red

- **Registros, ajuste del proveedor:** desactiva el registro abierto cuando un administrador o proveedor de identidad aprovisione las cuentas. Comprueba `ENABLE_SIGNUP` y cualquier ajuste persistente de administración con la [guía de endurecimiento](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Mantén estrictas las reglas de aprobación de cuentas nuevas.
- **Claves API, revisión del operador:** inventaría las claves emitidas, elimina las que no se usan y limita su creación y el acceso a endpoints a los roles y rutas necesarios. Según la guía del proveedor, una clave actúa con los permisos de quien la creó. Mantén las claves fuera de los ejemplos y registros de la aplicación.
- **Administradores, revisión del operador:** elimina cuentas de administrador abandonadas, exige controles de inicio de sesión sólidos, revisa la disponibilidad de MFA e investiga cambios de cuenta inesperados. Prueba la recuperación de cuenta antes de desactivar un administrador redundante.
- **Límite de red, guía del proveedor:** coloca el servicio detrás de una VPN, proxy de acceso o proxy inverso con autenticación y lista de IP permitidas. No lo expongas públicamente sin autenticación. Evita `WEBUI_AUTH=False` en un servicio accesible. Un proxy inverso sin autenticación propia no sustituye por sí solo el inicio de sesión de la aplicación. [Endurecer Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Alcance:** esta lista se aplica a la versión oficial de Open WebUI y a sus rutas de instalación estándar documentadas. No verifica forks, imágenes derivadas ni paquetes de terceros. Las notas de v0.12.4 no afirman que exista explotación activa. Consulta los [avisos de seguridad del proyecto](https://github.com/open-webui/open-webui/security/advisories) para conocer divulgaciones posteriores y sus propias versiones afectadas y corregidas. No atribuyas a v0.12.4 la corrección de un aviso anterior sin leer su rango de versiones.

## Fuentes y referencias

- [Notas de la versión de Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Avisos de seguridad de Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Actualizar Open WebUI, incluidas copias, reversiones y migraciones](https://docs.openwebui.com/getting-started/updating/)
- [Inicio rápido de Open WebUI y etiquetas oficiales de imágenes](https://docs.openwebui.com/getting-started/quick-start/)
- [Endurecer Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Actualizaciones y migraciones de varias réplicas](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)
