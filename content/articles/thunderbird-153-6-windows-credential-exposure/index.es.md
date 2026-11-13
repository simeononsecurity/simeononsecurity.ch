---
title: "Thunderbird 153.6: exposición de credenciales NTLM en Windows y cómo actualizar (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Dos fallos graves de Thunderbird pueden exponer datos de autenticación NTLM en Windows al mostrar un correo preparado. Conoce las dos vías, comprueba tu versión y limita el SMB saliente mientras actualizas."
genre: ["Ciberseguridad", "Seguridad del correo electrónico", "Seguridad de Windows"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "actualización de seguridad de Thunderbird", "vulnerabilidad de Thunderbird en Windows", "filtración NTLM de Thunderbird", "autenticación SMB de Thunderbird", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "adjunto de clave OpenPGP", "adjunto externo", "bloqueo de contenido remoto", "URL mailbox", "ruta UNC extendida", "nombre de cuenta de Windows", "datos de autenticación NTLM", "exposición de credenciales SMB", "SMB saliente", "puerto TCP 445", "seguridad del correo electrónico", "cliente de correo de Windows", "comprobar versión de Thunderbird", "actualizar Thunderbird", "retransmisión NTLM", "cracking de contraseñas sin conexión"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla corrigió dos **fallos graves que exponen credenciales de Windows** en Thunderbird 153.6. Bastaba con mostrar un correo malicioso para activar cualquiera de las solicitudes de red descritas en [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/). El aviso describe una posible divulgación de NTLM, no una vulneración confirmada de las credenciales de todos los destinatarios.

<!--more-->

## Puntos clave

- **CVE-2026-118174** afectaba a un adjunto de clave OpenPGP alojado externamente. Mostrar el mensaje provocaba una solicitud sin intervención del usuario, incluso con el contenido remoto bloqueado.
- **CVE-2026-118176** afectaba a una URL `mailbox:` especialmente preparada que usaba una ruta UNC extendida. Mostrar el mensaje provocaba una conexión SMB a un servidor elegido por el remitente.
- **Actualiza Thunderbird en Windows** y comprueba la versión instalada. El aviso identifica Thunderbird 153.6 como versión corregida. Las notas de Thunderbird señalan la compilación 153.6.0esr correspondiente.

## Qué activa el correo

**Los dos fallos tienen puntos de entrada diferentes.** Según las descripciones de Mozilla, ninguno requiere que el destinatario haga clic en un enlace del correo. El riesgo para las credenciales de Windows depende de que una solicitud de red llegue a un recurso compartido controlado por el atacante y de que se produzca el intercambio de autenticación. Mozilla no informa de explotación activa en el aviso.

| Problema | Qué se activa al mostrar el correo | Riesgo para las credenciales de Windows |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird carga el contenido de un adjunto de clave OpenPGP para ofrecer la importación. El remitente lo marca como adjunto externo con una URL elegida por el atacante. | Una URL a un recurso compartido de red expone las credenciales NTLM del usuario si la solicitud llega al recurso. |
| **CVE-2026-118176** | Una ruta UNC extendida elude la restricción de Thunderbird sobre recursos remotos en URL `mailbox:`. | Thunderbird se conecta a un servidor SMB elegido por el atacante y divulga el nombre de cuenta de Windows y datos de autenticación NTLM. |

Para la vía del **adjunto OpenPGP**, Mozilla afirma expresamente que la solicitud eludía el bloqueo del contenido remoto y no requería intervención del usuario. En sistemas distintos de Windows, el fallo también permitía una solicitud remota contraria a esa opción, pero Mozilla limita a Windows la filtración de credenciales NTLM. En la vía de la **URL `mailbox:`**, Mozilla indica que los demás sistemas operativos no están afectados. Consulta las entradas individuales de [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) y [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**Los datos de autenticación NTLM no son una contraseña en texto claro.** Mozilla indica que los datos divulgados por la vía SMB implican riesgo de cracking de contraseñas sin conexión o ataques de retransmisión. Recibir un mensaje preparado no demuestra que el ataque haya tenido éxito. El aviso también enumera otros fallos de Thunderbird, incluidas vías distintas para calendario y RSS. Este artículo trata las dos vías que se activan al mostrar el correo, no considera idénticos todos los problemas de la versión.

## Comprueba y actualiza Thunderbird

El flujo afectado es **leer correo en Thunderbird en Windows** antes de instalar la corrección correspondiente. El aviso de Mozilla identifica **Thunderbird 153.6** como versión corregida, pero no especifica todo el intervalo de versiones anteriores afectadas por estos dos problemas. Las [notas de la versión 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) indican que la compilación ESR se publicó el 27 de octubre de 2026. No deduzcas el estado del parche de otro canal, fork o paquete solo por su número de versión.

1. En Windows, abre **Help > About Thunderbird**. Lee la versión que muestra la ventana About, que también busca actualizaciones. Las [instrucciones de Mozilla para actualizar](https://support.mozilla.org/en-US/kb/updating-thunderbird) describen esta ruta.
2. Si hay una actualización, deja que Thunderbird la descargue y selecciona **Restart Thunderbird to Update**. Vuelve a abrir **Help > About Thunderbird** y confirma la versión instalada después del reinicio.
3. Para la **línea 153 ESR**, compara la versión resultante con **153.6.0esr** en las notas de Thunderbird. Si tu organización administra las actualizaciones, pide al administrador que verifique la corrección del proveedor en lugar de suponer que ya está instalada.

> **Nota sobre la versión:** Las notas de 153.6.0esr confirman que la versión existe, mientras que MFSA 2026-122 vincula las correcciones de seguridad a Thunderbird 153.6. Las notas no describen estas dos CVE por separado. Usa el aviso para consultar los detalles de las vulnerabilidades.

## Reduce la exposición mientras actualizas

**Instala primero la corrección del proveedor.** Desactivar el contenido remoto por sí solo no detiene CVE-2026-118174, ya que la solicitud descrita eludía esa opción. No consideres suficiente el consejo de «no hagas clic». Mozilla describe solicitudes que se activan al mostrar el mensaje.

Como **defensa en profundidad**, limita el SMB saliente desde los clientes Windows a Internet, incluido el **puerto TCP 445**, en el cortafuegos corporativo o en los equipos administrados. La [guía de Microsoft sobre tráfico SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) recomienda bloquear el TCP 445 saliente a Internet y limitar el acceso a los servidores de archivos necesarios. Haz un inventario de los recursos compartidos necesarios antes de aplicar una regla, sobre todo si tu entorno usa un servicio de archivos en la nube o trabajadores remotos fuera del perímetro. Este control de red limita la vía SMB descrita, pero no repara Thunderbird ni resuelve todos los problemas de solicitudes remotas del aviso.

Si un equipo Windows con una versión antigua de Thunderbird mostró un mensaje sospechoso, **trata la exposición como una cuestión que investigar, no como prueba de compromiso**. Revisa con el equipo de seguridad los registros disponibles de conexiones SMB salientes y de autenticación. El aviso del proveedor no incluye una prueba de exposición ni una instrucción general para cambiar todas las contraseñas.

## Fuentes

- [Mozilla Foundation Security Advisory 2026-122: vulnerabilidades corregidas en Thunderbird 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Notas de Thunderbird Desktop: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Soporte de Mozilla: actualiza Thunderbird a la versión más reciente](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: protege el tráfico SMB en Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
