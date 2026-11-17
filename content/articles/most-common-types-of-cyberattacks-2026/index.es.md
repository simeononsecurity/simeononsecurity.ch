---
title: "Los tipos de ciberataque más comunes y cómo detectarlos"
date: 2026-09-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Aprende cuáles son los ciberataques más comunes, qué rastros dejan en los registros y la telemetría, y practica su detección en un laboratorio de seguridad doméstico."
genre: ["Ciberseguridad", "Detección de amenazas", "Blue Team", "Operaciones de seguridad", "Desarrollo profesional"]
tags: ["tipos de ciberataques", "malware", "ransomware", "phishing", "spear phishing", "ingeniería social", "suplantación", "ataques basados en identidad", "credential stuffing", "password spraying", "inyección SQL", "secuencias de comandos en sitios cruzados", "ataque a la cadena de suministro", "amenaza interna", "tunelización DNS", "ataques IoT", "ataques basados en IA", "denegación de servicio", "ingeniería de detección", "analista SOC", "Blue Team", "laboratorio doméstico", "análisis de registros", "respuesta a incidentes", "MITRE ATT&CK", "carrera de ciberseguridad", "búsqueda de amenazas", "centro de operaciones de seguridad", "telemetría", "clasificación de alertas"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "Ilustración digital con iconos abstractos y coloridos que representan varios tipos de ciberataque, como ransomware, phishing y denegación de servicio, sobre un fondo oscuro."
coverCaption: ""
---

Un **tipo de ataque** es una categoría de técnicas, no una herramienta concreta. Ransomware, phishing y credential stuffing describen métodos que un adversario repite contra muchos objetivos con pequeñas variaciones. Aprender estas categorías te ofrece un índice mental de las alertas que encontrarás en un equipo de seguridad.

*Las familias de malware individuales aparecen y desaparecen en cuestión de meses. Las categorías de ataque que se presentan aquí llevan años estables y cada una deja un rastro reconocible en la telemetría de los endpoints, las identidades, la red o el correo electrónico.*

<!--more-->

## Puntos clave

- **Aprende el patrón, no la carga útil.** Las categorías de ataque cambian mucho más despacio que las herramientas concretas.
- **Cada categoría deja pruebas.** El trabajo de detección comienza por saber qué telemetría registra la actividad.
- **Reproduce un ataque para entenderlo.** Un laboratorio doméstico convierte una categoría abstracta en una observación registrada.
- **Documenta lo que encuentres.** Una breve nota de investigación demuestra el trabajo y enseña las pruebas reunidas.

## Tipos de ataque de un vistazo

La tabla enumera las categorías que los equipos de seguridad encuentran con mayor frecuencia. Las secciones siguientes describen cada categoría, sus variantes habituales y los datos que un defensor examina para detectarla.

| Tipo de ataque | Qué hace |
|---|---|
| **Malware** | Ejecuta software malicioso, como ransomware, spyware y troyanos |
| **Denegación de servicio** | Inunda un servicio de tráfico hasta que los usuarios legítimos pierden el acceso |
| **Phishing** | Engaña a una persona para que revele sus credenciales o ejecute un archivo malicioso |
| **Suplantación** | Se hace pasar por un sistema, remitente o dirección de confianza |
| **Ataques basados en identidad** | Abusan de credenciales robadas o falsificadas para actuar como un usuario válido |
| **Inyección de código** | Inserta código malicioso en una aplicación para cambiar su comportamiento |
| **Ataques a la cadena de suministro** | Comprometen a un proveedor, una biblioteca o un canal de actualización de confianza |
| **Ingeniería social** | Manipula a una persona para que realice una acción insegura |
| **Amenazas internas** | Abusan del acceso de un empleado actual o anterior |
| **Tunelización DNS** | Codifica datos en consultas DNS para eludir controles |
| **Ataques IoT** | Atacan dispositivos conectados para desplazarse por la red, espiar o unirse a una botnet |
| **Ataques basados en IA** | Usan aprendizaje automático para generar contenido, suplantar personas o evadir filtros |

**Nota sobre el alcance:** estas categorías se solapan. Un correo de phishing suele distribuir malware, y el robo de credenciales suele preceder a un ataque basado en identidad. Trata la lista como un conjunto de perspectivas, no como categorías rígidas.

______

## Malware

**Malware** incluye cualquier programa diseñado para dañar, controlar o sacar provecho de un sistema. El término abarca ransomware, malware sin archivos, spyware, adware, troyanos, gusanos, rootkits, keyloggers y botnets.

| Subtipo | Comportamiento |
|---|---|
| **Ransomware** | Cifra archivos y exige un pago a cambio de la clave de descifrado |
| **Malware sin archivos** | Funciona mediante herramientas integradas del sistema y apenas escribe en el disco |
| **Spyware** | Recopila datos de actividad sin que el usuario lo sepa |
| **Troyano** | Se hace pasar por software legítimo para conseguir que lo ejecuten |
| **Gusano** | Se copia entre hosts sin intervención del usuario |
| **Rootkit** | Se oculta en el sistema operativo para mantener el control de forma persistente |

**Dónde encontrar las pruebas:** las herramientas de detección y respuesta de endpoints, o **EDR**, registran árboles de procesos, líneas de comandos, escrituras de archivos y cambios en el registro. Un ataque sin archivos también genera telemetría de procesos y scripts, porque el sistema operativo sigue iniciando las herramientas que el atacante aprovecha.

______

## Denegación de servicio

**Un ataque de denegación de servicio (DoS)** inunda un objetivo con solicitudes hasta que los usuarios legítimos pierden el acceso. **Un ataque distribuido de denegación de servicio (DDoS)** repite la misma idea desde muchos sistemas a la vez, lo que dificulta mucho más filtrar el tráfico por dirección de origen.

| Rasgo | DoS | DDoS |
|---|---|---|
| **Origen** | Un sistema | Muchos sistemas |
| **Dificultad para bloquearlo** | Moderada | Alta, porque las fuentes se extienden por muchas redes |
| **Impacto habitual** | Pérdida de disponibilidad | Pérdida de disponibilidad a mayor escala |

**Dónde encontrar las pruebas:** volumen de tráfico frente a una referencia, conexiones por origen, picos en la tasa de solicitudes y cambios en la tasa de errores. La supervisión de disponibilidad suele generar una alerta antes de que el equipo de seguridad vea el incidente.

______

## Phishing

**El phishing** usa correo electrónico, mensajes de texto, llamadas telefónicas o redes sociales para convencer a una persona de que revele sus credenciales o ejecute un archivo adjunto malicioso. Sus variantes se distinguen por el objetivo y el canal.

| Variante | Objetivo y canal |
|---|---|
| **Spear phishing** | Una persona o equipo concreto, normalmente por correo electrónico |
| **Whaling** | Personal directivo o ejecutivo, a menudo para mover dinero o datos |
| **Smishing** | Mensajes de texto fraudulentos |
| **Vishing** | Llamadas o mensajes de voz fraudulentos |

**Dónde encontrar las pruebas:** registros de la pasarela de correo, resultados del análisis de URL, análisis de archivos adjuntos e informes de los usuarios. El aviso de un empleado prudente es una de las señales más valiosas de esta lista.

______

## Suplantación

**La suplantación** oculta a un atacante tras una identidad de confianza para que el objetivo acepte la conexión, el mensaje o la dirección. El disfraz gana tiempo y supera las comprobaciones basadas en la confianza.

| Tipo | Qué se falsifica |
|---|---|
| **Suplantación de dominio** | Un sitio web o dominio de correo similar que imita una marca real |
| **Suplantación de correo electrónico** | La dirección del remitente de un mensaje |
| **Suplantación ARP** | Una dirección de red local para interceptar tráfico entre dos hosts |

**Dónde encontrar las pruebas:** resultados SPF, DKIM y DMARC en los encabezados de correo, antigüedad del registro del dominio, discrepancias de certificados y avisos de direcciones duplicadas en la red local.

______

## Ataques basados en identidad

**Los ataques basados en identidad** usan una cuenta válida en lugar de un defecto de software. El atacante dispone de credenciales funcionales, por lo que la actividad se parece al uso normal y pasa desapercibida. Esta categoría genera una parte importante de las alertas que un **centro de operaciones de seguridad (SOC)** gestiona cada día.

*Si practicas una sola categoría en un laboratorio doméstico, elige esta. Sus señales son variadas, los ejercicios se repiten y la configuración sigue siendo pequeña.*

| Técnica | Qué ocurre |
|---|---|
| **Kerberoasting** | Solicita un ticket de servicio y después descifra sin conexión la contraseña cifrada |
| **Ataque de intermediario (MITM)** | Se sitúa entre dos partes para leer o modificar una sesión |
| **Ataque de reutilización del hash (Pass-the-Hash)** | Reutiliza un hash de contraseña robado para abrir una sesión nueva |
| **Golden ticket** | Falsifica un ticket de Kerberos para obtener un amplio acceso al dominio |
| **Silver ticket** | Falsifica un ticket de servicio para un servicio concreto |
| **Recolección de credenciales** | Recopila nombres de usuario y contraseñas en bloque |
| **Credential stuffing** | Repite las mismas credenciales en muchos sitios web sin relación entre sí |
| **Password spraying** | Prueba una contraseña habitual en muchas cuentas |
| **Fuerza bruta** | Prueba muchas contraseñas contra una cuenta |
| **Degradación** | Fuerza una conexión a usar una versión de protocolo más débil |

**Dónde encontrar las pruebas:** registros de inicio de sesión, recuentos de autenticaciones fallidas, anomalías en tokens, alertas de desplazamientos imposibles y detecciones de riesgo de identidad. **El phishing adversary-in-the-middle (AiTM)** también pertenece a esta categoría, porque el atacante roba un token de sesión activo en lugar de una contraseña y su reutilización desde una infraestructura desconocida activa el motor de riesgo de identidad.

______

## Inyección de código

**La inyección de código** introduce código controlado por el atacante en una aplicación vulnerable para que se ejecute como parte de su actividad normal. La acción dañina la realiza la aplicación, no el atacante.

| Tipo | Objetivo |
|---|---|
| **Inyección SQL** | Una consulta a la base de datos construida con entradas no validadas |
| **Cross-site scripting (XSS)** | Una página web que ejecuta el script del atacante en el navegador de un visitante |
| **Malvertising** | Un espacio publicitario legítimo ocupado por código malicioso |
| **Envenenamiento de datos** | Un conjunto de entrenamiento de un modelo de IA o aprendizaje automático |

**Dónde encontrar las pruebas:** registros de aplicaciones web, registros de consultas a bases de datos, informes de la política de seguridad de contenido y patrones de solicitudes diferentes del uso normal de la aplicación.

______

## Ataques a la cadena de suministro

**Un ataque a la cadena de suministro** se dirige a un tercero de confianza cuyo producto o servicio llega a muchos clientes. **Un ataque a la cadena de suministro de software** inserta código malicioso en una aplicación, biblioteca o actualización, y lo distribuye a todos los usuarios del producto. **Un ataque a la cadena de suministro de hardware** compromete un componente físico antes de que se envíe.

*El software moderno depende de bibliotecas de terceros, así que una dependencia comprometida llega mucho más lejos que el proveedor original.*

**Dónde encontrar las pruebas:** análisis de composición de software, registros de la canalización de compilación, conexiones salientes inesperadas de una actualización de confianza y comprobaciones de integridad de los artefactos distribuidos.

______

## Ingeniería social

**La ingeniería social** emplea presión psicológica para que una persona realice una acción insegura. El atacante apela a la autoridad, la urgencia, el miedo, el dinero o la confianza.

| Técnica | Enfoque |
|---|---|
| **Pretexting** | Inventa una situación creíble para ganarse la confianza |
| **Compromiso de correo empresarial (BEC)** | Se hace pasar por un compañero de confianza para desviar un pago o compartir datos |
| **Desinformación** | Difunde relatos falsos mediante redes sociales y bots |
| **Quid pro quo** | Ofrece una recompensa a cambio de información o acceso |
| **Trampa romántica** | Construye una relación falsa para obtener dinero, datos o acceso |
| **Tailgating** | Sigue a un empleado a través de una puerta segura |

**Dónde encontrar las pruebas:** resultados de autenticación de correo, solicitudes inusuales de cambios de pago, registros del servicio de asistencia y registros de acceso físico.

______

## Amenazas internas

**Una amenaza interna** consiste en el uso indebido del acceso por parte de un empleado actual o anterior, contratista o socio. Algunas personas actúan con intención por dinero o resentimiento. Otras actúan por negligencia, como al dejar credenciales en un documento compartido.

*Los informes de incidentes mencionan a personas internas negligentes más a menudo que a las maliciosas. En ambos casos se necesita el mismo control de detección: comparar el acceso con una referencia para el puesto.*

**Dónde encontrar las pruebas:** volumen de transferencia de datos, actividad fuera del horario habitual, cambios de privilegios y descargas masivas de repositorios confidenciales.

______

## Tunelización DNS

**La tunelización DNS** codifica datos dentro de consultas y respuestas DNS. Casi todas las redes permiten DNS, por lo que esta técnica envía datos más allá de los controles diseñados para inspeccionar el tráfico web.

*La detección depende del volumen y la forma. Un host que envía miles de consultas a un dominio destaca frente a la referencia normal, y los subdominios inusualmente largos apuntan a una carga útil codificada.*

**Dónde encontrar las pruebas:** registros de consultas DNS, longitud y volumen de las consultas por host, tipos de registro poco comunes como TXT y consultas a dominios registrados pocos días antes.

______

## Ataques basados en IoT

**Un ataque basado en IoT** se dirige a un dispositivo conectado, como una cámara, una impresora, un termostato o un sensor. Las credenciales predeterminadas débiles y las actualizaciones de firmware poco frecuentes convierten estos dispositivos en puntos de entrada habituales. Una vez comprometido, un dispositivo se une a una botnet, filtra datos o abre una ruta hacia la red más amplia.

*El despliegue de 5G añade dispositivos conectados a gran escala, y cada dispositivo nuevo es otro objetivo con un ciclo de actualización largo.*

**Dónde encontrar las pruebas:** inventario de dispositivos, patrones de conexión saliente, transferencias anómalas de un dispositivo con una función fija y diferencias de versión de firmware entre los equipos.

______

## Ataques basados en IA

**Los ataques basados en IA** aplican aprendizaje automático al trabajo del atacante.

| Técnica | Uso |
|---|---|
| **IA/ML adversarial** | Manipula los datos de entrenamiento o las entradas para engañar a un modelo |
| **Dark AI** | Aplica IA y aprendizaje automático específicamente para explotar vulnerabilidades |
| **Deepfake** | Genera audio, vídeo o imágenes falsas realistas |
| **Ingeniería social generada por IA** | Mantiene conversaciones convincentes por chat o voz a gran escala |

*Una llamada con voz deepfake o una conversación de phishing fluida eleva la credibilidad de un viejo truco. La técnica subyacente sigue siendo conocida, por lo que las capacidades de detección basadas en el comportamiento duran más que las ligadas a una sola herramienta.*

**Dónde encontrar las pruebas:** señales de procedencia del contenido, verificación por un canal alternativo para solicitudes de dinero o acceso y anomalías de comportamiento asociadas a cambios de identidad y pagos.

______

## Relacionar los ataques con la telemetría

Cada categoría alimenta una fuente de datos distinta. La tabla las relaciona y ofrece un punto de partida para el trabajo de detección.

| Tipo de ataque | Telemetría principal |
|---|---|
| **Malware** | Registros EDR de procesos, archivos y registro del sistema |
| **Denegación de servicio** | Flujos de red y monitores de disponibilidad |
| **Phishing** | Registros de la pasarela de correo y el análisis de URL |
| **Suplantación** | Registros de autenticación de correo y direcciones de red |
| **Basado en identidad** | Registros de inicio de sesión y protección de identidad |
| **Inyección de código** | Registros de aplicaciones web y consultas a bases de datos |
| **Cadena de suministro** | Canalización de compilación e inventario de dependencias |
| **Ingeniería social** | Registros de correo, asistencia y acceso físico |
| **Amenaza interna** | Registros de acceso y transferencia de datos |
| **Tunelización DNS** | Registros de consultas DNS |
| **IoT** | Inventario de dispositivos y registros de flujos salientes |
| **Basado en IA** | Registros de identidad, pagos y procedencia del contenido |

*Empieza el trabajo de detección por la columna de telemetría. Una regla útil surge de una fuente de datos y un comportamiento conocidos, no del nombre de una herramienta.*

**Las categorías se solapan durante un incidente.** Un mensaje de phishing puede provocar el robo de credenciales, la ejecución de malware y una intrusión basada en identidad. Etiqueta la técnica de acceso inicial y registra por separado los comportamientos posteriores. Así evitas convertir un solo suceso en cuatro alertas inconexas y obtienes una cronología más clara para la investigación.

______

## Practica su detección en un laboratorio

Una categoría sigue siendo abstracta hasta que observas cómo se manifiesta. Un laboratorio doméstico permite generar actividad, capturar la telemetría y comparar la alerta con el registro sin procesar. El [vídeo profesional sobre la creación de un centro de operaciones de seguridad](https://www.youtube.com/watch?v=s3g8o7Np1_g) muestra el montaje completo para adquirir experiencia laboral antes de conseguir un empleo.

{{< youtube id="s3g8o7Np1_g" >}}

Empieza por la categoría de identidad. Crea un usuario de prueba, activa el registro de inicios de sesión y ejecuta una secuencia de accesos fallidos y correctos. Después, lee el registro y apunta los campos que distinguen el uso normal del ejercicio.

**Un ejercicio repetible:**

1. **Elige una categoría** de la tabla de telemetría anterior.
2. **Reproduce una versión inocua** de la actividad en tu propio sistema o cuenta de prueba.
3. **Recopila la telemetría** que produce la categoría.
4. **Redacta la idea de detección** como una regla, búsqueda guardada o consulta.
5. **Prueba la regla** con el ejercicio y confirma que se activa ante el comportamiento esperado.
6. **Anota los límites** de la regla, incluidas las actividades que no detecta.

La guía [Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/) explica en detalle cómo montar el entorno: licencias, segmentación de red, recopilación de registros y pruebas de controles de identidad. La guía [Mad Hat Cyber Range](https://madhat.io/pages/cyber-range-guide) amplía la misma idea con una configuración de taller que incluye ejercicios de ataque, detección y defensa.

Para usar un vocabulario coherente, relaciona el comportamiento observado con la técnica correspondiente de [MITRE ATT&CK](https://attack.mitre.org/). Considera esa relación una ayuda para el analista, no una prueba de atribución. Conserva con el registro del ejercicio el evento sin procesar, la consulta, la versión de la regla y los puntos ciegos conocidos.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Lee la guía Microsoft SOC Home Lab
{{< /centerbutton >}}

______

## Próximos pasos

Empieza con una categoría y un ejercicio. Añade una segunda categoría cuando hayas completado y documentado la primera. El objetivo es profundizar en una investigación, no crear una lista de herramientas.

- **[Guía Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/)** prepara el entorno para estos ejercicios.
- **[Crear un laboratorio de TI doméstico](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** cubre la infraestructura de base para un laboratorio de seguridad.
- **[Consejos para redactar un currículum de TI](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** muestra cómo presentar un laboratorio documentado como experiencia práctica.
- **[Los cinco principales vectores de ciberataque y sus mitigaciones](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** reduce la lista a los vectores más frecuentes.

**Material de referencia:** las categorías de ataque y sus subtipos siguen la [guía de CrowdStrike sobre ciberataques comunes](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/) de Kurt Baker. Los enlaces de productos y referencias apuntan a documentación de Microsoft.
