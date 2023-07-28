---
title: "Creación de un lago de datos basado en la nube seguro y conforme a las normas: Buenas prácticas para proteger los datos almacenados"
date: 2023-04-16
toc: true
draft: false
description: "Conozca las mejores prácticas de seguridad y cumplimiento de normativas a la hora de planificar, crear y gestionar lagos de datos basados en la nube en esta completa guía."
tags: ["lago de datos", "seguridad en la nube", "normas de cumplimiento", "controles de acceso", "codificación", "AWS", "Azure", "HIPAA", "GDPR", "control", "parcheando", "ciberseguridad", "Solución SIEM", "Equipos de apoyo informático", "panorama de amenazas", "migración a la nube", "gobierno de la nube"]
cover: "/img/cover/A_cartoon_image_of_a_castle_being_guarded_by_a_warrior.png"
coverAlt: "Una imagen de dibujos animados de un castillo custodiado por un caballero guerrero, que simboliza el concepto de protección sólida para un almacenamiento en la nube seguro y conforme a las normas"
coverCaption: ""
---

**Guía para la creación de un lago de datos en la nube seguro y conforme a las normas**.

Un lago de datos basado en la nube es una herramienta valiosa para almacenar y analizar grandes conjuntos de datos. Sin embargo, presenta retos de seguridad únicos que deben abordarse para garantizar el cumplimiento de la normativa gubernamental. En esta guía, analizaremos las mejores prácticas para crear un lago de datos basado en la nube seguro y que cumpla la normativa.

## Planificación del lago de datos

Antes de empezar a construir un lago de datos, **es fundamental crear un plan que tenga en cuenta los requisitos de seguridad y conformidad** de su organización. Comience con la creación de un marco que se adhiera a los estándares de la industria, como el Reglamento General de Protección de Datos (GDPR) o la Ley de Portabilidad y Responsabilidad del Seguro Médico (HIPAA).

Es importante elegir el proveedor de nube adecuado, uno con experiencia demostrada en la entrega de soluciones seguras que puedan cumplir con estas regulaciones de cumplimiento. Algunos de los proveedores de nube más populares son Amazon Web Services (AWS), Microsoft Azure y Google Cloud Platform.

Además, **defina controles de acceso claros** para usuarios, funciones y permisos. Esto incluye a los miembros de su equipo interno, así como a los proveedores o socios externos que puedan necesitar acceso en ocasiones.

## Construcción del lago de datos

Al construir un lago de datos, **el cifrado y los controles de acceso deben implementarse por diseño** en todas las etapas del movimiento de datos hacia, dentro y desde el lago de datos. Los procesos de ingestión deben cifrar los datos durante el tránsito y en reposo siempre que sea posible. Utilice las mejores prácticas, como protocolos de seguridad de la capa de transporte en su cliente de ingestión o protocolos de red, como el protocolo de transferencia segura de archivos (SFTP), o un servicio Apache Kafka gestionado.

Los clientes de ingestión o las aplicaciones que copian datos de distintos sistemas deben emplear políticas de acceso basadas en el principio del menor privilegio: conceder sólo los permisos necesarios para copiar información relevante de una fuente externa.

En los frentes de almacenamiento, seleccione plataformas que admitan el cifrado en reposo o proporcionen otras funciones avanzadas de criptografía como la gestión de claves, incluido el cifrado del lado del servidor con claves propiedad del cliente (CMK).

**El control estricto del acceso a los datos es clave**, y soluciones como AWS Identity and Access Management o Azure Active Directory proporcionan un medio eficaz para controlar los permisos tanto a nivel de objeto como en el plano de gestión.

## Supervisión y administración del lago de datos

Una **vigilancia precisa de la infraestructura de su lago de datos ayuda a identificar las brechas de seguridad** o las actividades sospechosas que se producen dentro de su lago de datos. **Implemente el registro de toda la actividad relacionada con el lago de datos** almacenando los registros de datos en una cuenta de auditoría independiente para evitar que los atacantes los borren o manipulen. Esto detectará rápidamente actividades sospechosas, como el escaneo de puertos, ataques DDos, ataques de fuerza bruta o ataques basados en la red.

Utilice una solución de gestión de eventos e información de seguridad (SIEM) como las incluidas en AWS CloudTrail o Azure Monitor para centralizar el registro, automatizar las alertas y realizar análisis avanzados.

Además, asegúrese de que **se apliquen parches periódicos a los componentes críticos**. Las actualizaciones periódicas de paquetes de software para sistemas subyacentes como sistemas operativos, bases de datos, servidores web o bibliotecas de terceros deben formar parte de su modelo de soporte para garantizar que las vulnerabilidades conocidas sean remediadas por equipos de soporte de TI cualificados.

## Mantenerse al día con el cambiante panorama de amenazas

**Debido a un panorama de seguridad en constante evolución, los controles de seguridad en la nube deben adaptarse rápidamente a las nuevas amenazas.

Si busca el cumplimiento de normativas específicas que regulan el almacenamiento de datos, tome medidas para mantener estos requisitos de cumplimiento mediante auditorías de cumplimiento e informes periódicos generados a partir de los servicios respectivos.

## Conclusión

La implantación de un lago de datos basado en la nube ofrece ventajas significativas, pero también conlleva una mayor carga en lo que respecta a la seguridad y el cumplimiento normativo. Sin embargo, seguir las mejores prácticas del sector, como el cifrado en reposo y en tránsito, la gestión de los controles de acceso a un alto nivel mediante la gestión de identidades y accesos (IAM), la supervisión de su implementación mediante el registro avanzado y el empleo de parches continuos, le ayudará a construir un lago de datos basado en la nube seguro y que cumpla las normativas.

Junto con el mantenimiento de controles adecuados de migración y gobernanza de la nube, su organización puede aprovechar todas las ventajas de los servicios basados en la nube, manteniendo al mismo tiempo la conformidad y la seguridad.

_______

## Referencias

1. [Guide to using AWS EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
2. [Microsoft - HIPAA overview](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
3. [What is SIEM?](https://www.varonis.com/blog/what-is-siem)
4. [AWS - Data ingestion methods](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-ingestion-methods.html)
5. [HIPAA Security Rule Standards and Implementation Specifications](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html)