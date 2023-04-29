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

 **Guía para la creación de un lago de datos en la nube seguro y conforme a las normas**.
 
 Un lago de datos basado en la nube es una herramienta muy útil para almacenar y analizar grandes volúmenes de datos. Sin embargo, plantea requisitos de seguridad muy exigentes que deben cumplirse para respetar las normas legales. En este artículo describimos las mejores prácticas para la creación de un lago de datos basado en la nube que sea seguro y flexible.
 
 ## Planificar un lago de datos
 
 Antes de comenzar con la creación de un Data Lake, **es importante elaborar un plan que tenga en cuenta los requisitos de seguridad y cumplimiento normativo** de su empresa. Comience con la elaboración de un plan que cumpla las normas del sector, como la Ley de Protección de Datos (DSGVO) o la Ley de Portabilidad y Responsabilidad del Seguro Médico (HIPAA).
 
 Es importante que el proveedor de servicios en la nube más adecuado cuente con una amplia experiencia en la creación de soluciones seguras que cumplan las normas de conformidad. Algunos de los principales proveedores de servicios en la nube son Amazon Web Services (AWS), Microsoft Azure y Google Cloud Platform.
 
 También puede definir **controles de acceso claros** para usuarios, roles y tareas. A esto se añaden los miembros internos de su equipo, así como los proveedores o socios externos que pueden tener acceso a los servicios.
 
 ## Erstellen des Data Lake
 
 Durante la creación de un lago de datos, deben implementarse **Controles de cambio y de acceso por diseño** en todas las fases de la captura de datos hacia, dentro y desde el lago de datos. Los procesos de captura deben permitir que los datos se desvíen durante la transferencia y se vuelvan a procesar. Utilice las mejores prácticas, como protocolos de seguridad de transporte en su cliente de mensajería instantánea o protocolos de red, como el protocolo de transferencia segura de archivos (SFTP) o un entorno Apache Kafka verificado.
 
 Los clientes o proveedores de servicios que copien datos de diferentes sistemas deben utilizar reglas de conexión basadas en el principio de la más alta calidad: Tenga en cuenta únicamente las condiciones que sean necesarias para obtener información relevante de una fuente externa.
 
 No utilice plataformas que permitan la transmisión de datos a través de Internet ni otras funciones criptográficas ampliadas, como la gestión de claves de acceso, por ejemplo, la transmisión de datos a través de un servidor con claves de acceso de cliente (CMK).
 
 **El control estricto del acceso a los datos es la clave**, y las soluciones como AWS Identity and Access Management o Azure Active Directory ofrecen un medio eficaz para controlar los derechos tanto de los usuarios como de los administradores.
 
 ## Gestión y administración de Data Lake
 
 Una buena gestión de la infraestructura de su Data Lake le ayudará a identificar problemas de seguridad** o actividades peligrosas que se encuentren en su Data Lake. **Mejore la recopilación de datos de todas las actividades relacionadas con el lago de datos** y guarde los protocolos de datos en una cuenta de auditoría independiente para evitar que los usuarios los pierdan o los manipulen. De este modo, se pueden gestionar rápidamente actividades como el escaneo de puertos, los ataques DDoS, los ataques de fuerza bruta o los ataques basados en red.
 
 Utilice una solución SIEM (gestión de eventos e información de seguridad), como AWS CloudTrail o Azure Monitor, para centralizar la recopilación de datos, automatizar los procesos y realizar análisis adicionales.
 
 Asimismo, asegúrese de que se han realizado **parches periódicos de los componentes críticos**. Las actualizaciones periódicas de los paquetes de software de los sistemas de terceros, como los sistemas empresariales, las bases de datos, los servidores web o las bibliotecas de los bibliotecarios, deben formar parte de su modelo de soporte para garantizar que los equipos de soporte informático cualificados se encargan de las actualizaciones.
 
 ## Mit der sich ändernden Bedrohungslandschaft Schritt halten
 
 **Gracias a un entorno de seguridad cada vez más seguro, los controles de seguridad en la nube deben adaptarse rápidamente a las nuevas infraestructuras.
 
 Si desea cumplir las normas de protección de datos más estrictas, obtendrá instrucciones para el cumplimiento de dichas normas mediante auditorías de cumplimiento e informes periódicos que se generarán a partir de los dispositivos correspondientes.
 
 ## Abschluss
 
 La implantación de un lago de datos basado en la nube ofrece ventajas únicas, pero también un mayor nivel de seguridad y cumplimiento normativo. Sin embargo, la aplicación de las mejores prácticas del sector, como el control de acceso en la fase inicial y durante la migración, la gestión de los controles de acceso en un nivel superior mediante la gestión de identidades y accesos (IAM), la mejora de su implementación mediante una protocolización más avanzada y el uso de parches continuos, le ayudarán a crear un Data Lake basado en la nube más seguro y flexible.
 
 Junto con el cumplimiento de los controles de migración y gobierno de la nube, su empresa podrá aprovechar al máximo las ventajas de los servicios basados en la nube y, al mismo tiempo, garantizar el cumplimiento y la seguridad.
 
 _______
 
 ## Verweise
 
 1. [Leitfaden zur Verwendung der AWS EBS-Verschlüsselung] (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
 2. [Microsoft - HIPAA-Übersicht](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
 3. 3. [¿Qué es SIEM?](https://www.varonis.com/blog/what-is-siem)
 4. 4. [AWS - Métodos de gestión de datos](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-ingestion-methods.html)
 5. 5. [HIPAA-Sicherheitsregelstandards und Implementierungsspezifikationen] (https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html)