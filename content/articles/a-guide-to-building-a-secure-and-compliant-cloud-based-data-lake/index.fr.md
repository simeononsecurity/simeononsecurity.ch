---
title: "Construcción de un lago de datos basado en la nube seguro y conforme a la normativa: Buenas prácticas para proteger los datos almacenados"
date: 2023-04-16
toc: true
draft: false
descripción: "Conoce las mejores prácticas de seguridad y cumplimiento normativo a la hora de planificar, construir y gestionar lagos de datos basados en la nube en esta completa guía."
tags: ["lago de datos", "seguridad en la nube", "normativas de cumplimiento", "controles de acceso", "cifrado", "AWS", "Azure", "HIPAA", "GDPR", "monitorización", "parches", "ciberseguridad", "solución SIEM", "equipos de soporte de TI", "panorama de amenazas", "migración a la nube", "gobierno de la nube"].
cover: "/img/cover/A_cartoon_image_of_a_castle_being_guarded_by_a_warrior.png"
coverAlt: "Imagen de dibujos animados de un castillo custodiado por un caballero guerrero, que simboliza el concepto de protección sólida para un almacenamiento seguro y conforme a las normas basado en la nube"
coverCaption: ""
---

 **Una guía para crear un almacén de datos seguro y conforme basado en la nube**.
 
 Una base de datos en la nube es una herramienta muy útil para almacenar y analizar grandes conjuntos de datos. Sin embargo, presenta problemas de seguridad únicos que deben resolverse para garantizar el cumplimiento de la normativa gubernamental. En esta guía se describen las mejores prácticas para crear una red de datos segura y fiable basada en la nube.
 
 ## Planification du lac de données
 
 Antes de empezar a crear una base de datos, **es esencial crear un plan que tenga en cuenta los requisitos de seguridad y conformidad** de tu organización. Empieza por crear un marco que respete las normas del sector, como el Reglamento General de Protección de Datos (RGPD) o la ley HIPAA (Health Insurance Portability and Accountability Act).
 
 Es importante elegir un buen proveedor de cloud computing que tenga experiencia en el suministro de soluciones seguras que puedan cumplir estas normativas. Algunos de los proveedores de nube más conocidos son Amazon Web Services (AWS), Microsoft Azure y Google Cloud Platform.
 
 Además, **defina controles de acceso claros** para los usuarios, los roles y las autorizaciones. Esto incluye a los miembros de tu equipo interno, así como a los proveedores o socios externos que a veces necesiten acceso.
 
 ## Construir la base de datos
 
 Durante la creación de un lago de datos, **deberán aplicarse desde la concepción** el control y los controles de acceso a todas las etapas del desplazamiento de datos hacia, dentro y fuera del lago de datos. Los procesos de ingestión deben registrar los datos durante el tránsito y, si es posible, volver a guardarlos. Utiliza las mejores prácticas, como los protocolos de seguridad de la capa de transporte de tu cliente de ingestión o los protocolos de red, como el protocolo de transferencia segura de archivos (SFTP) o un servicio Apache Kafka.
 
 Los clientes o aplicaciones de ingesta que copien datos de diferentes sistemas deben utilizar políticas de acceso basadas en el principio de la privacidad absoluta: sólo se necesitan las autorizaciones necesarias para copiar la información pertinente de una fuente externa.
 
 En el plan de almacenamiento, seleccione las placas-formato que cargan el recuento en reposo o que proporcionan otras funciones de recuento avanzadas como la gestión de claves, incluido el recuento en la parte del servidor con las claves pertenecientes al cliente (CMK).
 
 **Un control estricto del acceso a los datos es esencial**, y las soluciones como AWS Identity and Access Management o Azure Active Directory proporcionan una forma eficaz de controlar las autorizaciones a nivel del objeto y del plan de gestión.
 
 ## Surveillance and management du lac de données
 
 Una **vigilancia precisa de la infraestructura de su lago de datos permite identificar los fallos de seguridad** o las actividades sospechosas que se producen en su lago de datos. **Lleve un registro diario de todas las actividades relacionadas con la laguna de datos** almacenando los diarios de datos en una cuenta de auditoría separada para evitar que los atacantes los supriman o falsifiquen. Esto detecta rápidamente las actividades sospechosas, como el análisis de puertos, los ataques DDoS, los ataques de fuerza bruta o los ataques basados en la red.
 
 Utilice una solución de gestión de información y eventos de seguridad (SIEM) como las incluidas en AWS CloudTrail o Azure Monitor para centralizar el registro, automatizar las alertas y realizar análisis avanzados.
 
 Asegúrese también de que ** se realicen correcciones periódicas de los componentes críticos **. Las revisiones periódicas de los paquetes logísticos para los sistemas subyacentes, como los sistemas de explotación, las bases de datos, los servidores Web o las bibliotecas de nivel superior, deben formar parte de su modelo de soporte para garantizar que las vulnerabilidades detectadas sean corregidas por equipos de soporte informático cualificados.
 
 ## Siga la evolución del panorama de amenazas
 
 **El mantenimiento de una vigilancia reforzada es un requisito indispensable para mantener las bases de datos en la nube seguras y conformes.** Debido a un entorno de seguridad en constante evolución, los controles de seguridad de la nube deben adaptarse rápidamente a las nuevas amenazas.
 
 Si desea cumplir las normas específicas que regulan el almacenamiento de datos, tome medidas para mantener estos requisitos de conformidad mediante auditorías de conformidad e informes regulares generados por los servicios correspondientes.
 
 ## Conclusión
 
 La puesta en marcha de un almacenamiento de datos basado en la nube ofrece ventajas significativas, pero también conlleva un coste adicional en términos de seguridad y conformidad. Siguiendo las mejores prácticas del sector, como el registro de datos en reposo y en tránsito, la gestión de los controles de acceso a un nivel superior mediante la gestión de identidades y accesos (IAM), la supervisión de su puesta en marcha mediante un registro avanzado y la utilización de correctivos continuos, le ayudarán a crear una nube segura y conforme. lac de données basé sur .
 
 Paralelamente al mantenimiento de controles de gobierno y de migración a la nube apropiados, su organización puede utilizar en su totalidad servicios basados en la nube manteniendo la conformidad y la seguridad.
 
 _______
 
 ## Referencias
 
 1. 1. [Guía de uso de AWS EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
 2. [Microsoft - Presentación HIPAA](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
 3. 3. [¿Qué es SIEM?](https://www.varonis.com/blog/what-is-siem)
 4. 4. [AWS - Méthodes d'ingestion de données](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-ingestion-methods.html)
 5. 5. [Normas de seguridad HIPAA y especificaciones de aplicación] (https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html)