---
title: "La ciberseguridad de IA y las certificaciones de gobernanza no están al día con el problema"
draft: false
toc: true
date: 2026-06-26
description: "Una opinión profesional sobre la brecha entre las certificaciones de gobernanza de IA y la práctica real de seguridad de IA. Aprobamos varias de ellas y salimos decepcionados. Los marcos son incipientes y están orientados a la gobernanza. La superficie de ataque creció más rápido."
tags: ["seguridad IA", "gobernanza IA", "certificaciones IA", "NIST AI RMF", "NIST AI 600-1", "ISO 42001", "IAPP AIGP", "inyección de prompt", "ciberseguridad IA", "seguridad LLM", "OWASP LLM Top 10", "MITRE ATLAS", "gestión de riesgos IA", "cumplimiento IA", "seguridad machine learning", "cadena de suministro de modelos", "IA adversarial", "agentes IA", "seguridad MCP", "red teaming IA", "certificaciones gobernanza IA", "IA agéntica", "Google SAIF"]
cover: "/img/cover/ai-cybersecurity-governance-certifications-disappointing.webp"
coverAlt: "La imagen muestra una escena dividida: en un lado, profesionales en una oficina discutiendo documentos de gobernanza; en el otro, imágenes digitales caóticas que representan sistemas de IA bajo ciberataque, con colores vibrantes que resaltan el contraste."
coverCaption: ""
---

Rendimos los exámenes. Aprobamos. Salimos con certificados y un nivel de decepción que quiero describir con precisión.

Esto no es una queja sobre las personas que construyeron estos programas. Trabajan con material incompleto. La seguridad de IA como disciplina es joven. La investigación sobre ataques avanza más rápido que las herramientas defensivas. Los marcos de gobernanza llegaron antes que la orientación de ingeniería.

El problema es la brecha entre lo que enseñan las certificaciones y lo que usted necesita saber para realmente asegurar sistemas de IA en producción.

## Tres capas que frecuentemente se confunden

Antes de explicar qué falta, conviene separar lo que existe actualmente.

La primera capa es la gobernanza. Documentos como el NIST AI Risk Management Framework (AI RMF 1.0, 2023), ISO/IEC 42001:2023 y el EU AI Act operan a nivel organizacional y de procesos. Describen cómo gestionar el riesgo de IA, estructurar la supervisión y documentar la responsabilidad. Están deliberadamente orientados a la gobernanza en lugar de prescribir controles. Eso es por diseño.

La segunda capa es la taxonomía de amenazas. MITRE ATLAS documenta tácticas adversariales contra sistemas de IA en el mismo formato que ATT&CK. El OWASP Top 10 para aplicaciones de grandes modelos de lenguaje enumera las clases de ataque más relevantes para los LLMs desplegados. Estos documentos nombran los ataques y describen cómo funcionan. No prescriben defensas.

La tercera capa es la guía técnica. Incluye el Secure AI Framework (SAIF) de Google, el AI Security SDL de Microsoft, OWASP AI Exchange, NIST AI 600-1 (el perfil de IA generativa) y documentación de seguridad específica de proveedores como Anthropic, OpenAI, Meta y otros. Estos proporcionan orientación de nivel de ingeniería sobre despliegue seguro, prácticas de evaluación y controles en tiempo de ejecución.

La mayoría de las certificaciones de gobernanza de IA cubren la primera capa a fondo. Referencian la segunda capa a nivel de resumen. Raramente tocan la tercera.

## Qué cubren las certificaciones

Las certificaciones de gobernanza y seguridad de IA disponibles actualmente, incluidas IAPP AI Governance Professional (AIGP), el certificado AI Fundamentals de ISACA, las certificaciones ISO 42001 y CompTIA AI+, cubren un conjunto consistente de temas.

Usted aprende el NIST AI RMF y cómo mapear sus cuatro funciones, Govern, Map, Measure y Manage, al despliegue de IA de su organización. Aprende las clasificaciones de niveles de riesgo del EU AI Act y cómo luce la evaluación de conformidad para sistemas de alto riesgo. Aprende sobre sesgo, equidad, transparencia y responsabilidad como principios de gobernanza. Aprende a redactar políticas de gobernanza de IA y realizar evaluaciones de impacto.

Estas son habilidades reales. Las organizaciones necesitan personas que entiendan los marcos de gobernanza. Necesitan personas que lean el NIST AI RMF y sepan qué les pide construir.

Lo que las certificaciones no enseñan con la misma profundidad:

- Cómo los atacantes comprometen actualmente los sistemas de IA en producción
- Cómo luce operacionalmente la defensa en profundidad para la inyección de prompt y por qué ningún control único la elimina
- Cómo verificar la integridad de los modelos antes del despliegue
- Qué implica el red teaming específico de IA y cómo delimitarlo
- Cómo evaluar el comportamiento del modelo contra entradas adversariales antes del lanzamiento
- Cómo luce la observabilidad de IA en el momento de la inferencia
- Cómo difiere la respuesta a incidentes de IA de los playbooks estándar de IR
- Qué requiere asegurar agentes de IA con acceso a herramientas e integraciones externas

## El NIST AI RMF es gobernanza, no ingeniería

El NIST AI RMF es un documento bien construido. NIST lo diseñó para ser neutral tecnológicamente, agnóstico al sector y aplicable a diferentes enfoques de desarrollo de IA. Esto produce un marco de amplia aplicación.

También significa que el marco no prescribe controles técnicos para clases de ataque específicas. Si su organización adopta plenamente el AI RMF y mapea todas sus funciones al despliegue de IA, tendrá procesos de riesgo documentados. No necesariamente tendrá una defensa contra la inyección de prompt en su modelo de lenguaje desplegado.

NIST lo reconoce. NIST AI 600-1, el perfil de IA generativa publicado en 2024, extiende el AI RMF específicamente para IA generativa y grandes modelos de lenguaje. Cubre riesgos como inyección de prompt, envenenamiento de datos y riesgos informativos a un nivel de especificidad que el AI RMF base no alcanza. Si su certificación cubrió el AI RMF base sin AI 600-1, se perdió el documento más relevante para los sistemas actualmente desplegados.

## ISO 42001 y la comparación del sistema de gestión

ISO 42001:2023 es una norma de sistema de gestión de IA. Proporciona una estructura para gobernar el desarrollo y despliegue de IA a nivel organizacional. Los profesionales de seguridad reconocerán el paralelo con ISO 27001 para la seguridad de la información.

ISO 27001 está ampliamente adoptada. Las organizaciones certificadas aún sufren brechas. La certificación documenta que existe un sistema de gestión, sigue un proceso definido y se revisa. No certifica que los sistemas gobernados por ese proceso resistan los ataques que se usan contra ellos.

ISO 42001 proporciona disciplina organizacional. Obtener la certificación indica a los interesados que sus procesos de IA están documentados, revisados y sujetos a gobernanza. No les dice si sus modelos desplegados producen salidas consistentes bajo condiciones adversariales, si sus agentes operan dentro de límites de confianza definidos, o si sus modelos ajustados fueron construidos a partir de datos de entrenamiento verificados.

Esa es la misma brecha que tiene ISO 27001. En ciberseguridad tradicional aprendimos a vivir con ella. No debemos pretender que las certificaciones de gobernanza de IA la cierran cuando comparten la misma limitación estructural.

## El EU AI Act crea requisitos de resultados sin especificaciones de ingeniería

El EU AI Act clasifica los sistemas de IA por nivel de riesgo: inaceptable (prohibido), alto riesgo (evaluación de conformidad requerida), riesgo limitado (obligaciones de transparencia) y riesgo mínimo (sin requisitos específicos).

Los sistemas de alto riesgo, incluidos los utilizados en infraestructura crítica, identificación biométrica, selección de empleo, educación y aplicación de la ley, enfrentan requisitos de documentación técnica, obligaciones de supervisión humana y requisitos de robustez. El Acto requiere explícitamente que los sistemas de IA de alto riesgo sean robustos contra intentos de alterar el comportamiento mediante manipulación adversarial.

Ese requisito está en el texto. El Acto especifica intencionalmente resultados en lugar de prescribir controles técnicos. Los métodos técnicos para demostrar robustez adversarial en todos los contextos de despliegue aún no tienen respuestas de consenso para cada tipo de sistema y caso de uso.

Las certificaciones construidas alrededor del EU AI Act lo preparan para clasificar sistemas de IA, redactar documentación técnica y estructurar protocolos de supervisión. Lo preparan para la auditoría. El trabajo de ingeniería que produce un sistema conforme con los requisitos de robustez del Acto pertenece a una disciplina diferente a la que actualmente cubren las certificaciones.

## Qué está atacando realmente los sistemas de IA

MITRE ATLAS y OWASP LLM Top 10 documentan el panorama de amenazas operacional. Estos son los recursos que enumeran los ataques a un nivel de detalle útil. Los marcos de gobernanza referencian amenazas a mayor nivel de abstracción. Lo siguiente proviene de esas fuentes específicas de seguridad.

La inyección de prompt funciona proporcionando entradas a un modelo de lenguaje que anulan o manipulan las instrucciones del sistema. La inyección directa apunta directamente a la entrada del modelo. La inyección indirecta incrusta instrucciones maliciosas en el contenido que el modelo recupera, procesa o resume. Su pipeline RAG lee un documento controlado por el atacante y actúa según instrucciones ocultas en él. Su agente de navegación visita una página controlada por el atacante y sigue sus directivas incrustadas. Su bot de soporte al cliente resume un artículo de soporte que contiene instrucciones para ignorar sus pautas de seguridad.

No existe una mitigación universalmente efectiva para la inyección de prompt en 2026. La defensa en profundidad reduce el riesgo: filtrado de entradas, validación de salidas, alcances de herramientas con privilegios limitados, entornos de ejecución en sandbox y puertas de aprobación humana para acciones consecuentes. Ninguno de estos elimina la clase de ataque. NIST, OWASP, Anthropic, OpenAI, Google y Microsoft recomiendan controles en capas en lugar de soluciones únicas.

El envenenamiento de datos de entrenamiento introduce ejemplos maliciosos en los datos de entrenamiento para degradar el comportamiento del modelo, introducir puertas traseras o implantar comportamientos basados en desencadenantes. La señal de un envenenamiento exitoso suele estar ausente hasta que el modelo encuentra entradas desencadenantes específicas. Si su organización ajusta modelos con contenido generado por usuarios, documentos recuperados o conjuntos de datos de terceros sin verificar su procedencia, enfrenta este riesgo.

La compromiso de la cadena de suministro de modelos es la amenaza que la mayoría de las organizaciones tratan como secundaria. Los repositorios de modelos frecuentemente distribuyen código ejecutable junto con los pesos del modelo, y formatos de serialización no seguros como pickle han creado repetidamente riesgos en la cadena de suministro. Los paquetes que acompañan las descargas de modelos pueden instalar dependencias con sus propias vulnerabilidades. Muchas organizaciones descargan modelos aplicando mucho menos escrutinio de cadena de suministro del que aplican a las dependencias de software. La superficie de ataque es comparable a npm pero la cultura de seguridad a su alrededor es mucho más temprana.

La extracción de modelos permite a los atacantes reconstruir modelos funcionalmente similares mediante consultas de inferencia repetidas contra su API. Esto representa tanto pérdida de propiedad intelectual como un medio de estudiar su modelo fuera de línea para desarrollar ataques más dirigidos.

La inferencia de membresía permite a los atacantes determinar con diversa confianza si registros de datos específicos estuvieron en su conjunto de entrenamiento, dependiendo de la arquitectura del modelo y el régimen de entrenamiento. Esto crea riesgo de privacidad para organizaciones que entrenaron sobre información personal.

Las entradas adversariales manipulan las salidas del modelo mediante perturbaciones diseñadas. La técnica está más estudiada en clasificación de imágenes pero se aplica a texto, audio y sistemas multimodales. Si su IA toma decisiones sobre detección de fraude, solvencia crediticia, imágenes médicas o acceso físico, la robustez adversarial es una propiedad de seguridad que debe probar, no solo documentar.

La filtración de datos a través de sistemas de IA es una categoría que merece atención directa. Los pipelines RAG exponen documentos de su base de conocimientos, a veces a usuarios que no deberían tener acceso a ellos. La filtración de prompt desde instrucciones del sistema revela detalles operativos que pretendía mantener confidenciales. Los despliegues de IA multi-tenant crean requisitos de aislamiento que los ingenieros de seguridad de aplicaciones tradicionales a veces subestiman. Estos son riesgos operativos que aparecen regularmente en sistemas desplegados.

## Los agentes de IA cambian completamente la superficie de ataque

La mayoría de las certificaciones de seguridad de IA fueron escritas cuando los sistemas de IA significaban principalmente chatbots y clasificadores. La IA empresarial en 2026 significa cada vez más agentes.

Los agentes difieren de los chatbots en una forma operativamente importante: toman acciones. Un agente con acceso a herramientas de su sistema de correo electrónico, bases de datos internas, sistemas de archivos, navegador y entornos de ejecución de código no es un chatbot con más funciones. Es un proceso autónomo con acceso significativo a sistemas reales, operando basado en las salidas del modelo de lenguaje.

OWASP mantiene ahora un Agentic AI Top 10 separado porque el modelo de amenazas para los agentes difiere suficientemente de las aplicaciones de chat LLM como para requerir documentación separada.

La inyección de prompt en un contexto de agente no produce una respuesta textual no deseada. Produce una acción no deseada. Una inyección indirecta en un documento recuperado instruye al agente a eliminar archivos, exfiltrar datos o enviar correos electrónicos. La consecuencia no es una respuesta inapropiada. Es una acción no autorizada tomada contra sistemas a los que el agente tiene acceso.

La superficie de ataque para los agentes incluye:

- Límites de invocación de herramientas: si el agente está restringido a un conjunto mínimo de herramientas apropiadas para cada tarea
- Alcance de credenciales: si las credenciales que tiene el agente se limitan a lo que cada tarea requiere
- Reversibilidad de acciones: si las acciones consecuentes requieren aprobación humana antes de ejecutarse
- Filtrado de salidas: si las salidas del agente se validan antes de desencadenar acciones posteriores
- Sandboxing: si el entorno de ejecución del agente previene el acceso no intencional a sistemas conectados

La mayoría de las certificaciones de gobernanza de IA no cubren el diseño de seguridad de agentes a este nivel de especificidad.

## El Model Context Protocol crea una nueva superficie de ataque empresarial

El Model Context Protocol (MCP) se ha convertido en un estándar ampliamente adoptado para conectar agentes de IA con herramientas externas, fuentes de datos y servicios. Los servidores MCP exponen capacidades que los agentes descubren y utilizan. La integración es rápida y flexible. Las implicaciones de seguridad no siempre reciben atención equivalente.

Los riesgos específicos de MCP incluyen:

- Servidores MCP maliciosos que representan incorrectamente sus capacidades ante un agente y ejecutan acciones no previstas
- Envenenamiento de herramientas donde un servidor MCP legítimo devuelve datos controlados por el atacante e incrusta instrucciones en lo que deberían ser salidas de datos
- Herramientas con exceso de privilegios donde las integraciones MCP tienen permisos más allá de lo que la tarea requiere
- Confusión de límites de confianza donde los agentes reciben instrucciones de herramientas MCP adjuntas que parecen equivalentes a las instrucciones del usuario

Las organizaciones que despliegan agentes con integraciones MCP necesitan un marco para evaluar la confianza del servidor MCP, auditar los permisos de herramientas y validar que las respuestas de las herramientas se traten como datos en lugar de instrucciones.

## La evaluación es la práctica operativa que las certificaciones omiten

El red teaming de IA y las suites de evaluación están reemplazando las evaluaciones de seguridad estáticas como métodos principales para entender el riesgo de los modelos de IA antes y después del despliegue.

El red teaming para IA implica:

- Pruebas adversariales estructuradas del comportamiento del modelo contra técnicas de ataque conocidas
- Benchmarking de jailbreak contra conjuntos de datos de ataques de prompt establecidos
- Pruebas de robustez adversarial que miden la deriva de salidas bajo entradas perturbadas
- Pruebas de regresión de comportamiento entre versiones del modelo
- Evaluación de benchmarks de seguridad contra suites de evaluación publicadas

NIST, Anthropic, OpenAI, Microsoft, Google y CISA recomiendan el red teaming específico de IA antes del despliegue para sistemas de alto riesgo. Esto se está convirtiendo en expectativa estándar, no práctica opcional.

Ninguna de las certificaciones actuales de gobernanza de IA prepara adecuadamente a los profesionales para delimitar, ejecutar o interpretar un ejercicio de red teaming contra un modelo o sistema de agente desplegado. Describen qué es el red teaming. No le enseñan a hacerlo.

## La observabilidad de IA es una disciplina separada

La auditoría de seguridad tradicional no se transfiere directamente a los sistemas de IA. Monitorear un LLM o agente en producción requiere recopilación de datos diferente y análisis diferente.

La infraestructura de observabilidad de IA cubre:

- Telemetría de prompts y salidas para detección de anomalías e identificación de violaciones de políticas
- Registros de invocación de herramientas para agentes, incluyendo qué herramientas fueron llamadas con qué argumentos
- Monitoreo de calidad de recuperación para pipelines RAG
- Detección y clasificación de intentos de jailbreak
- Monitoreo de consistencia de salidas para detectar deriva del modelo entre versiones
- Seguimiento de tasa de alucinaciones para aplicaciones donde la precisión factual importa
- Patrones de latencia que pueden indicar intentos de inyección de prompt que inflan el tamaño del contexto

Esta es una disciplina emergente. La mayoría de las organizaciones que despliegan IA en 2026 tienen significativamente menos visibilidad sobre sus componentes de IA que sobre su infraestructura tradicional. La mayoría de las certificaciones de gobernanza no describen cómo luce la observabilidad adecuada para sistemas de IA.

## La respuesta a incidentes de IA no es como la IR habitual

Cuando un sistema tradicional es comprometido, su playbook de IR cubre contención, forense y recuperación. Los incidentes de IA introducen preguntas que el playbook estándar no aborda.

Preguntas para las que necesita playbooks antes de necesitarlos:

- Cómo determinar si un modelo fue envenenado durante el ajuste fino
- Cómo evaluar si una recuperación RAG fue abusada para devolver contenido controlado por el atacante
- Cómo identificar si un agente ejecutó acciones no autorizadas y cuál fue su alcance
- Cómo verificar si una actualización de modelo de un proveedor tercero cambió el comportamiento de maneras relevantes para la seguridad
- Cómo establecer cuál era el comportamiento de un modelo antes de un incidente para compararlo con el comportamiento posterior

Esto requiere preparación antes del incidente. Requiere registros y telemetría que debe configurar con anticipación. Requiere runbooks específicos de IA que dediquen espacio a la forense del comportamiento del modelo, no solo al tráfico de red y los registros de endpoints.

## El problema de actualización de las certificaciones

Una razón estructural por la que las certificaciones se quedan atrás de la práctica actual: la seguridad de IA cambia más rápido de lo que los ciclos de actualización de certificaciones permiten.

Security+, CISSP e ISO 27001 cubren dominios que evolucionan a lo largo de años. Las superficies de ataque centrales de redes, endpoints y aplicaciones son relativamente estables. Las técnicas de ataque de IA evolucionan en meses. Las técnicas de inyección de prompt, los métodos de ataque adversarial y las superficies de ataque agénticas en 2026 son diferentes de lo que existía cuando se lanzaron las primeras certificaciones de IA en 2023 y 2024.

Los organismos de certificación actualizan materiales según calendarios. El OWASP LLM Top 10 publicó una revisión significativa dentro de su primer año. MCP no existía como preocupación empresarial cuando se diseñaron muchas certificaciones de IA actuales. Los marcos de seguridad de IA agéntica son posteriores a la mayoría de los programas de certificación actuales.

Este es un problema estructural, no un fallo de intención. Debe leer fuentes primarias de forma continua en lugar de tratar una certificación como un corpus fijo de conocimiento.

## Qué debe estar en el contenido de las certificaciones de seguridad de IA

Para que los programas de certificación reflejen la práctica actual de seguridad de IA, necesitan cubrir:

- Defensa en profundidad contra inyección de prompt: filtrado de entradas, validación de salidas, delimitación de herramientas, sandboxing y puertas de aprobación humana, junto con las limitaciones documentadas de cada uno
- Verificación de cadena de suministro de modelos: riesgos de serialización no segura, requisitos SBOM, documentación de proveniencia y verificación de artefactos firmados
- Arquitectura de seguridad de agentes IA: límites de confianza, acceso a herramientas con mínimo privilegio, reversibilidad de acciones y requisitos de monitoreo
- Seguridad de MCP e integraciones externas: evaluación de confianza para servidores de herramientas, auditoría de permisos de herramientas y separación de datos vs. instrucciones
- Evaluación y red teaming: cómo delimitar una evaluación adversarial, qué benchmarks y conjuntos de datos de evaluación existen y cómo interpretar los resultados
- Observabilidad de IA: qué registros y telemetría requieren los sistemas de IA y cómo usarlos para la detección de incidentes y la respuesta
- Respuesta a incidentes específica de IA: planificación previa para escenarios de incidentes de IA, recopilación de evidencia para preguntas sobre comportamiento del modelo y consideraciones de recuperación exclusivas de los sistemas de IA
- Prevención de filtración de datos: aislamiento RAG, confidencialidad de prompts, controles de acceso multi-tenant y filtrado de salidas

## Qué debe hacer ahora mismo

Si usted es responsable de sistemas de IA en su organización:

Lea el OWASP Top 10 para aplicaciones de grandes modelos de lenguaje y el OWASP Agentic AI Top 10. Son gratuitos. Son más específicos operacionalmente que cualquier programa de certificación pagado actual.

Revise MITRE ATLAS antes de su próxima sesión de modelado de amenazas en cualquier componente de IA. Conozca qué tácticas adversariales se aplican a su arquitectura antes de finalizar su diseño de despliegue.

Lea NIST AI 600-1. Extiende el AI RMF base específicamente para IA generativa y es significativamente más relevante para despliegues de LLM y agentes que el marco base solo.

Revise Google SAIF, el AI SDL de Microsoft y OWASP AI Exchange para orientación de nivel de ingeniería que los marcos de gobernanza no proporcionan.

Verifique la proveniencia de cada modelo que despliegue su organización. Revise las fichas del modelo. Escanee los formatos de serialización en busca de clases de exploits conocidas antes de cargar los pesos.

Mapee cada agente de IA en su entorno contra el acceso que tiene. Un agente con acceso de lectura y escritura a su base de conocimientos interna, correo electrónico y sistema de archivos es un amplificador de inyección de prompt. Minimice sus credenciales a lo que cada tarea requiere.

Exija red teaming específico de IA antes de desplegar cualquier modelo o agente en un contexto de alta consecuencia. Trátelo como obligatorio, no opcional.

Construya runbooks de respuesta a incidentes específicos de IA ahora, antes de necesitarlos.

Trate su certificación de gobernanza como documentación de su capa de procesos. No es documentación de su postura de seguridad.

## Referencias

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- NIST SP 1270: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL documentation
- CISA Guidance on AI Cybersecurity, 2024
- Barreno et al., Can Machine Learning Be Secure?, 2006
- Biggio et al., Poisoning Attacks Against Support Vector Machines, 2012
- Goodfellow et al., Explaining and Harnessing Adversarial Examples, ICLR 2015
- IAPP AI Governance Professional (AIGP) program documentation
- ISACA AI Fundamentals Certificate program documentation
