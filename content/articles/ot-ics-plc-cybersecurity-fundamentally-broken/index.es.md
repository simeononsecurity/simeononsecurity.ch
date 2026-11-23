---
title: "Por qué la ciberseguridad de OT, ICS y PLC sigue sin resolverse"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-22
description: "Analiza por qué los controles de seguridad OT se quedan atrás ante diseños heredados, límites operativos y rutas de ataque reales."
tags: ["seguridad OT", "seguridad ICS", "seguridad PLC", "seguridad IoT", "ciberseguridad industrial", "seguridad SCADA", "NIST 800-82", "IEC 62443", "NERC CIP", "tecnología operacional", "infraestructura crítica", "sensores analógicos", "aislamiento físico de red", "sistemas heredados", "opinión sobre ciberseguridad", "sistemas de control industrial", "SCADA", "Stuxnet", "seguridad de sistemas de control", "seguridad ciberfísica", "seguridad de la cadena de suministro", "cadena de suministro OT"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Ilustración que contrasta un PLC antiguo con funciones analógicas y un controlador moderno con capacidad de ciberseguridad, ambos sobre un fondo oscuro."
coverCaption: ""
---

He pasado suficiente tiempo en entornos industriales para decirlo con claridad: **la mayoría de los programas de ciberseguridad de OT, ICS y PLC son puro teatro**. Generan documentación de cumplimiento. No generan seguridad. La brecha entre ambas cosas es donde atacan a la infraestructura crítica.

Esto no es un ataque a quienes redactan estándares. **NIST SP 800-82 Rev 3**, **IEC 62443** y **NERC CIP** son documentos técnicamente sólidos. El problema no es la guía. *El problema es a qué sistemas se aplica.*

## Los sistemas se diseñaron para funcionar, no para protegerse

**Los PLC, los sistemas SCADA, los sistemas de control distribuido (DCS) y el hardware industrial IoT heredado** se diseñaron con un único objetivo: funcionar de manera fiable durante mucho tiempo. **La disponibilidad era el único objetivo de diseño que importaba.** La confidencialidad, la integridad, la autenticación y el registro de actividad no eran requisitos. En muchos casos, ni siquiera eran conceptos considerados cuando se diseñaron estos sistemas.

NIST SP 800-82 Rev 3 (2023) lo reconoce con franqueza. Describe los entornos OT como sistemas con *«requisitos particulares de rendimiento, fiabilidad y seguridad física»*, en los que *«la seguridad no puede interferir con el funcionamiento del sistema»*. Léelo otra vez. **El documento principal de orientación de seguridad para la tecnología operacional reconoce expresamente que la seguridad queda en segundo plano.** El documento no tiene un defecto. Describe el entorno con precisión.

No puedes aplicar control de acceso basado en roles a un PLC que no entiende el concepto de roles de usuario. No puedes actualizar el firmware de un equipo cuyo fabricante ya no existe. **Los protocolos serie heredados, entre ellos Modbus RTU y Profibus DP, no incluyen autenticación nativa.** Transmiten comandos y datos a cualquiera que los solicite. No verifican quién los solicita.

*La guía es sólida. A menudo, los sistemas no pueden cumplirla.* No son el mismo problema.

## Hay dos categorías de OT completamente distintas

**Los PLC heredados de los años ochenta hasta principios de los 2000** se diseñaron para funcionar de forma aislada y con acceso exclusivamente físico. Ejecutan sistemas operativos propietarios. A menudo se administran desde estaciones de ingeniería que también se conectan a las redes corporativas. Sus configuraciones se guardan en formatos sin verificación de integridad. Estos sistemas representan una parte importante de la infraestructura instalada en el tratamiento de agua, la generación de energía, la fabricación y el transporte.

**Los controladores modernos con funciones de seguridad son distintos.** Siemens, Schneider, Rockwell, Beckhoff y Phoenix Contact ya ofrecen plataformas con arranque seguro, firmware firmado, control de acceso basado en roles, identidad respaldada por TPM y comunicaciones cifradas. EtherNet/IP CIP Security, PROFINET Security Class y OPC UA con autenticación ya se ofrecen en el hardware actual.

No estoy restando valor a la ingeniería moderna de seguridad OT. El progreso es real. **El problema es que la mayoría de los sistemas instalados no son modernos.** Cuando alguien habla de «ciberseguridad OT», suele describir el intento de proteger un controlador programable de hace 20 años con un marco de ciberseguridad redactado en 2023. Esa es la brecha a la que me refiero.

## Qué funciona de verdad

**La seguridad física y el aislamiento de red son los controles más fiables disponibles para los entornos OT heredados.** Todos los principales marcos de seguridad ICS dicen lo mismo. IEC 62443 organiza los entornos OT en zonas de seguridad con conductos definidos. El objetivo es que el movimiento lateral tenga que cruzar límites controlados, en vez de propagarse por una red plana.

El aislamiento de red reduce de forma considerable la superficie de ataque basada en la red. No elimina todos los riesgos. Los medios extraíbles, el acceso interno, los portátiles de mantenimiento, las conexiones temporales de ingeniería y los ataques a la cadena de suministro son rutas de entrada documentadas a sistemas sin exposición de red. **Stuxnet**, que llegó a instalaciones iraníes de centrifugadoras aisladas de la red mediante memorias USB infectadas, es el ejemplo clásico. *El aislamiento de red es necesario. No es suficiente.*

**La supervisión humana de los parámetros del proceso físico** sigue siendo uno de los mecanismos de detección más fiables. Un operador capacitado que vigila la presión, la temperatura y el caudal en tiempo real detectará cosas que ningún sistema de detección de intrusiones verá, porque el IDS no puede comprobar si el valor digital coincide con la realidad física.

Controles que reducen el riesgo en los contextos adecuados:

- **Los diodos de datos** permiten sacar telemetría sin admitir conexiones entrantes
- **La lista de aplicaciones permitidas** en estaciones HMI limita lo que se ejecuta en equipos con acceso a los sistemas de control
- **Las plataformas pasivas de detección de anomalías** de Claroty, Dragos y Nozomi analizan el tráfico sin tocar las comunicaciones del plano de control
- **La segmentación de red** entre zonas OT ralentiza el movimiento lateral sin exigir un aislamiento físico total
- **Los principios de confianza cero**, mencionados en NIST SP 800-82 Rev 3, añaden requisitos de verificación por sesión a algunas arquitecturas OT modernas

*Ninguno resuelve las limitaciones de diseño de fondo. Reducen el riesgo en los bordes de sistemas que nunca se diseñaron para ello.*

## Las señales analógicas no se pueden autenticar

**Los lazos de corriente de 4-20 mA, las señales de 0-10 V, las salidas de termopares y las lecturas de RTD se transmiten como señales eléctricas variables.** La señal física no dispone de ningún mecanismo para verificar su autenticidad. Quien coloque la señal correcta en el cable será considerado legítimo.

Stuxnet lo demostró de forma concreta. El ataque manipuló la lógica del PLC que se ejecutaba en los controladores Siemens S7 y, al mismo tiempo, reprodujo datos normales del proceso que se habían grabado antes en las interfaces de operador. **Los operadores miraban pantallas con lecturas normales mientras las centrifugadoras superaban sus límites de funcionamiento.** El engaño duró lo suficiente para causar daños físicos que parecían una avería del equipo, no un ataque.

Las interferencias electromagnéticas de los cables de alimentación, los variadores de frecuencia, los rayos y una puesta a tierra incorrecta corrompen las mediciones analógicas durante el funcionamiento normal. IEC 61000 existe por este motivo. Las instalaciones industriales usan cables apantallados, una puesta a tierra correcta, filtros y separación física para controlarlas.

Los dispositivos de campo inteligentes modernos convierten internamente las mediciones analógicas a formato digital antes de transmitirlas mediante HART-IP, WirelessHART, EtherNet/IP CIP Security u OPC UA. El hardware moderno permite usar comunicaciones digitales autenticadas a nivel de dispositivo. **El cable analógico de 4-20 mA que conecta un transmisor heredado a una entrada de PLC heredada no ofrece autenticación y nunca la ofrecerá.** Una parte importante de la instrumentación instalada todavía usa ese cable.

## Validar sensores es un control de seguridad funcional, no de ciberseguridad

Los sistemas de seguridad de procesos realizan **votación redundante de sensores**. Una configuración 2 de 3 en la que dos sensores indican 230 PSI y otro marca 14 PSI identifica el valor atípico. Esto ofrece una resistencia limitada ante la manipulación de un único sensor. *Es un control de ingeniería de seguridad funcional, no un control de ciberseguridad.*

Los PLC estándar no validan criptográficamente sus entradas analógicas. Un generador de señales conectado al lazo resulta indistinguible de un transmisor legítimo. El PLC lee la corriente y actúa en consecuencia.

**Los sistemas instrumentados de seguridad debían ser la última línea de defensa independiente.** En 2017, **TRITON** (también conocido como **TRISIS**) atacó unidades SIS Triconex de Schneider Electric con el objetivo concreto de desactivar esa capa. Los atacantes llegaron al sistema de seguridad a través de la red de estaciones de ingeniería. *La independencia de esa capa dependía de una separación de red que no se había mantenido.*

IEC 62443-3-3, IEC 62443-4-2 y la coordinación con la seguridad funcional conforme a IEC 61511 reflejan ahora esta lección. Durante años, grupos distintos trataron la seguridad de procesos y la ciberseguridad como disciplinas separadas. **TRITON demostró en la práctica lo que análisis independientes ya habían defendido en teoría:** un atacante que neutraliza el sistema de seguridad antes de provocar la condición peligrosa elimina el último control que impide las consecuencias físicas.

## La cadena de suministro es una vía de entrada que quizá ignores

**La mayoría de los programas de seguridad OT se centran en la arquitectura de red. Muchos de los compromisos OT de los últimos años usaron puntos de entrada que la arquitectura de red no bloquea.**

Los riesgos de la cadena de suministro OT incluyen:

- **La integridad del firmware antes de la instalación**, en particular si el hardware llega de fábrica o del distribuidor con firmware sin verificar
- **Las sesiones de acceso remoto de proveedores**, que siguen siendo una exposición persistente en instalaciones que dependen del soporte del fabricante
- **Las estaciones de ingeniería** conectadas tanto a la red corporativa como a la red OT, a menudo por comodidad operativa
- La falta de **listas de materiales de software (SBOM)** en la mayoría de las implementaciones OT heredadas, lo que hace casi imposible rastrear sus componentes de software
- **Los contratistas de mantenimiento** que llevan portátiles y memorias USB a entornos operativos aislados
- **La compatibilidad con actualizaciones de firmware firmadas**, que falta en la mayoría de las plataformas antiguas

NIST SP 800-82 Rev 3 dedica apartados específicos a las dependencias de proveedores y al acceso de terceros. *Si tu separación de red está intacta por dentro, pero el proveedor de tus equipos mantiene un portal de acceso remoto persistente a tu red de ingeniería, no tienes una red aislada. Tienes una brecha con una puerta que controla otra persona.*

## Endurecer sistemas heredados cuesta más de lo que debería

Cada programa de PLC se escribe a medida para un proceso específico. La lógica que controla el sistema de compensación de oleaje de una refinería es completamente distinta de la que controla la secuencia de cloración de una planta de tratamiento de agua o el regulador de una turbina. No es una elección. Los procesos físicos son distintos.

**Endurecer sistemas OT heredados suele costar más de lo previsto** debido a los requisitos de validación de ingeniería, el tiempo de inactividad necesario, las limitaciones de soporte del proveedor, las lagunas en la documentación y los ciclos de prueba que superan las estimaciones iniciales. En algunos casos con equipos sin soporte del fabricante, el endurecimiento cuesta tanto como reemplazar el sistema o más.

**El cumplimiento de NERC CIP para activos cibernéticos del sistema eléctrico masivo cuesta millones de dólares al año a cada empresa eléctrica.** Una encuesta de 2019 de la American Public Power Association documentó costes de cumplimiento muy variados, con una carga desproporcionada para las empresas pequeñas. Muchos sistemas de agua y empresas eléctricas pequeñas quedan fuera de los requisitos de NERC CIP y no afrontan obligaciones comparables.

## Hay que sustituir los sistemas

**La respuesta correcta es sustituir los sistemas OT heredados.** En grandes instalaciones, esto implica decenas de millones de dólares, periodos de transición prolongados y el riesgo de trasladar de forma incorrecta conocimientos operativos complejos. Son costes y riesgos reales.

La orientación de CISA e ICS-CERT recomienda aplicar controles compensatorios mientras avanza la planificación de sustitución. Es una respuesta racional a las limitaciones. *Dicho claramente, reconoce que el equipo heredado no permite alcanzar una seguridad total. Por eso hay que aplicar los controles posibles y planificar su sustitución futura.*

**La realidad es que muchos de estos sistemas seguirán en servicio durante décadas.** Es un problema de financiación y políticas. La comunidad técnica ha explicado qué debe hacerse. Los presupuestos operativos y los calendarios de sustitución no han seguido el mismo ritmo.

## Añadir conectividad de red a los sistemas OT suele empeorar las cosas

Muchas organizaciones han añadido funciones de acceso remoto y supervisión a entornos OT que antes estaban aislados. El argumento operativo es sencillo: la visibilidad remota reduce el tiempo de respuesta y el soporte de proveedores es más rápido con una conexión remota. **La consecuencia para la seguridad es que los sistemas aislados, sin superficie de ataque remoto, ahora sí tienen una.**

El **incidente de la planta de tratamiento de agua de Oldsmar de 2021** ocurrió mediante una conexión de acceso remoto de TeamViewer. El atacante cambió la configuración de dosificación de hidróxido de sodio con una herramienta legítima de acceso remoto que se había añadido por comodidad. El **incidente de Colonial Pipeline de 2021** comenzó con un compromiso de la red de TI. El operador detuvo de forma preventiva las operaciones de la red OT de tuberías porque no podía confirmar que la red OT no se hubiera visto afectada. *El ataque no vulneró directamente la red OT. La incertidumbre sobre una posible vulneración provocó el cierre.*

Añadir conectividad de red a sistemas OT heredados por motivos operativos, sin diseñarla conforme a normas adecuadas, **genera en muchos casos más riesgo del que justifica el beneficio**. El modelo Purdue sigue siendo una arquitectura de referencia útil, pero NIST ya no lo considera suficiente por sí solo. El IIoT moderno, la conectividad con la nube, las operaciones remotas y las arquitecturas híbridas requieren un diseño más deliberado que la segmentación por zonas.

## Cumplir estándares escritos no equivale a tener seguridad

NIST SP 800-82 Rev 3, IEC 62443 y NERC CIP describen los controles adecuados para estos sistemas. No los estoy descartando. Señalo lo que dicen expresamente: **no todos los sistemas OT pueden aplicar todos los controles.** Los marcos usan niveles de seguridad escalonados y disposiciones para controles compensatorios precisamente porque los sistemas a los que se aplican a menudo no pueden cumplir todos los requisitos.

La brecha entre lo que describen los estándares y lo que puede lograr una instalación heredada concreta no es un error de documentación. Los sistemas no admiten esos controles. La guía lo reconoce. **Completar una auditoría de cumplimiento en OT heredada no significa que el entorno sea seguro.** Significa que documentaste los controles compensatorios y un auditor los aceptó.

El marco de gestión de riesgos de NIST deja claro que queda riesgo residual después de aplicar controles. Aceptar el riesgo es uno de los cuatro resultados del marco, junto con transferirlo, reducirlo y evitarlo. *La guía oficial incorpora el reconocimiento del riesgo residual.* **Si alguien te dice que cumplir los requisitos de conformidad hace seguro tu entorno OT, afirma algo que los propios marcos citados no respaldan.**

## Qué hacer con la OT heredada

Si operas entornos OT heredados:

- **Trata el aislamiento de red como tu control principal** y audita todo lo que cruza el límite OT
- **Elabora un plan de endurecimiento específico para las estaciones de ingeniería.** Conectan ambos entornos y suelen ser el punto de entrada
- **Controla y registra todos los medios extraíbles** en las zonas OT
- **Audita el acceso remoto de proveedores** y cierra todas las sesiones que no estén en uso
- Implementa supervisión redundante de sensores cuando el diseño del proceso lo permita
- **Crea un calendario de sustitución con estimaciones de coste reales**, aunque falten años para el reemplazo
- **Deja de tratar la finalización de auditorías de cumplimiento como un hito de seguridad**

Si vas a adquirir sistemas OT nuevos:

- **Incluye requisitos de seguridad en la especificación de compra** antes de que respondan los proveedores
- Elige plataformas que documenten soporte para comunicaciones autenticadas, actualizaciones de firmware firmadas y control de acceso basado en roles
- **Diseña los límites IT/OT como conductos explícitos conforme a IEC 62443**, no como una vaga política de «mantenerlos separados»
- **Exige SBOM de los componentes de software OT** como entrega contractual

La industria ha documentado bien el problema. Los estándares son técnicamente precisos. *Los sistemas instalados a menudo no pueden recibir lo que prescriben los estándares.* Reconocerlo abiertamente es el primer paso para decidir cómo gestionar el riesgo restante.

## Referencias

- NIST SP 800-82 Rev 3: Guía de seguridad de la tecnología operacional (OT) (2023)
- IEC 62443: serie de seguridad para sistemas de automatización y control industrial
- IEC 62443-3-3: requisitos de seguridad de sistemas y niveles de seguridad
- IEC 62443-4-2: requisitos técnicos de seguridad para componentes IACS
- IEC 61511: seguridad funcional de sistemas instrumentados de seguridad
- NERC CIP: estándares de protección de infraestructuras críticas para el sistema eléctrico masivo
- IEC 61000: estándares de compatibilidad electromagnética
- Avisos y buenas prácticas de CISA ICS-CERT
- Marco MITRE ATT&CK para ICS
- Análisis técnico de Stuxnet, Langner Communications, 2011
- Análisis técnico de TRITON/TRISIS, Dragos, 2017
- Revisión del incidente de Oldsmar Water Treatment, CISA, 2021
- Encuesta sobre costes de cumplimiento NERC CIP de la American Public Power Association, 2019
