---
title: "Lista de seguridad personal 2026: por dónde empezar y qué omitir"
date: 2026-09-30
lastmod: 2026-11-15
toc: true
draft: false
description: "Prioriza las medidas de seguridad personal según su impacto en los ataques, desde la protección de cuentas y copias de seguridad hasta la privacidad y recuperación."
genre: ["Seguridad personal", "Privacidad", "Higiene digital", "Seguridad de cuentas", "Modelado de amenazas", "Seguridad del consumidor", "Gestión de contraseñas", "Protección de datos"]
tags: ["lista de seguridad personal", "lista de seguridad digital", "lista de privacidad 2026", "ciberseguridad personal", "seguridad de cuentas", "configuración de claves de acceso", "llave de seguridad física", "configuración del gestor de contraseñas", "buenas prácticas 2fa", "resistencia al phishing", "supervisión de filtraciones", "avisos de filtraciones", "congelación del crédito", "privacidad de alias de correo", "compartimentación", "modelo de amenazas", "cifrado de disco completo", "estrategia de copias 3-2-1", "protección del navegador", "bloqueo de rastreadores", "DNS sobre HTTPS", "eliminación de metadatos", "eliminación de EXIF", "protección contra el intercambio de SIM", "recuperación de cuentas", "códigos de respaldo", "robo de tokens de sesión", "malware infostealer", "prioridades de seguridad personal", "errores de higiene de seguridad", "herramientas de privacidad", "herramientas de seguridad del lado del cliente"]
cover: "/img/cover/personal-security-checklist-2026-tiered-structure.webp"
coverAlt: "Ilustración digital sobre un fondo oscuro con bloques de colores apilados que representan medidas de seguridad personal. Cada bloque simboliza una acción, como usar un gestor de contraseñas o autenticación de dos factores."
coverCaption: ""
ref: ["/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security", "/articles/bitwarden-and-keepassxc-vs-the-rest", "/checklists/password-security-checklist"]
---

**Todas las guías de seguridad personal te dan lo mismo: una lista larga y plana de cientos de consejos sin orden de prioridad.** Te dicen que desactives WebRTC, falsifiques la huella de canvas y cambies el user-agent, en la misma frase que recomienda configurar un gestor de contraseñas y activar las actualizaciones automáticas.

*Esas medidas no tienen el mismo valor. Tratarlas como iguales hace que muchas personas hagan lo fácil, se salten lo importante y sigan igual de expuestas.*

Este artículo mantiene el tema y descarta la falsa equivalencia. Encontrarás los mismos consejos, ordenados según cuánto riesgo reducen por el esfuerzo necesario, y una mirada honesta a los hábitos que conviene abandonar.

## La respuesta breve

| Pregunta | Respuesta breve |
|---|---|
| **¿Qué detiene más ataques?** | Un gestor de contraseñas, segundos factores resistentes al phishing y actualizaciones puntuales. Estos hábitos abordan vías comunes de vulneración de cuentas, pero no todas las amenazas. |
| **¿Cuál es la mejora más importante disponible hoy?** | **Claves de acceso o una llave de seguridad física.** Ambas resisten el phishing durante el inicio de sesión porque la credencial nunca sale de tu dispositivo. Protege también los métodos de recuperación y el dispositivo. |
| **¿Qué está sobrevalorado?** | Contraseñas complejas que memorizas, rotaciones programadas de contraseñas y la mayoría de los ajustes de huella del navegador. |
| **¿Qué está infravalorado?** | Copias de seguridad, configuración de recuperación de cuentas y seguridad física de los dispositivos. |
| **¿Importa el orden?** | Sí, más que la exhaustividad. **Hacer hoy el nivel 1 es mejor que completar algún día los 300 puntos.** |
| **¿Cuánto tarda el nivel 1?** | Aproximadamente dos horas, una sola vez. |

## Por qué el orden importa más que la exhaustividad

Una lista completa suele reunir cientos de elementos y etiquetarlos como **Esencial**, **Opcional** o **Avanzado**. La etiqueta sirve para filtrar, pero no sustituye una clasificación porque todos los elementos reciben la misma categoría sin importar cuánto riesgo reduzcan.

**Mi argumento: ni siquiera tres niveles dan suficiente precisión**, porque «Esencial» agrupa medidas con reducciones de riesgo muy distintas. Compara dos elementos considerados esenciales:

- **Activar 2FA** elimina toda una categoría de toma de control de cuentas.
- **Desactivar WebRTC** cierra una divulgación local de IP relevante para pocos usuarios.

Ambos pertenecen a una lista completa. Solo uno pertenece a tu primera hora.

**El principio correcto de ordenación es una proporción.** Clasifica cada acción según el riesgo que elimina dividido por el esfuerzo necesario, y luego avanza de arriba abajo. El orden es así:

| Nivel | Propósito | Esfuerzo | Bloquea |
|---|---|---|---|
| **1. Detener el ataque** | Cerrar las vías que usan los atacantes hoy | ~2 horas | Robo de credenciales, phishing, malware, robo de dispositivos |
| **2. Contener los daños** | Limitar el impacto cuando algo falla | ~1 hora | Punto único de fallo, bloqueo de cuenta, fraude de identidad |
| **3. Reducir la exposición** | Reducir tu huella de datos | Continuo | Perfilado, seguimiento, ingeniería social dirigida |
| **4. Seguridad física y humana** | Cubrir la capa que el software no alcanza | ~30 minutos | Incautación de dispositivos, miradas indiscretas, phishing de voz |

*Avanza hacia abajo. No saltes al nivel 3 solo porque te parezca más interesante.*
{{< figure src="personal-security-tiers-ranked-by-impact.webp" alt="Diagrama de cuatro niveles de medidas de seguridad personal, ordenadas por riesgo reducido y esfuerzo necesario, desde detener ataques hasta las medidas físicas y humanas" >}}

## Nivel 1: Detener el ataque

Cinco puntos, unas dos horas en total, para abordar las vías que usan los atacantes.

### 1. Un gestor de contraseñas y una contraseña única en cada sitio

**El relleno de credenciales automatizado es el principal método de toma de cuentas**, y funciona porque la gente reutiliza contraseñas. Cuando se filtra un sitio, los atacantes prueban esas credenciales automáticamente y a gran escala en los demás.

Un gestor de contraseñas corrige la causa raíz al hacer imposible la reutilización accidental. Genera una contraseña distinta de alta entropía para cada cuenta y la completa por ti.

Un detalle importante que muchos consejos omiten: **la contraseña del gestor es ahora el único punto de fallo**. Debe ser larga y memorizada. Es la única contraseña que nunca guardas en otro lugar. Una frase de cinco o seis palabras aleatorias es más segura que una cadena corta y compleja, y mucho más fácil de recordar.

Hay dos arquitecturas válidas:

| Enfoque | Ventaja | Compromiso |
|---|---|---|
| **Sincronizado en la nube** (Bitwarden y similares) | Cómodo, sincroniza entre dispositivos, recuperación sencilla | Confías en el cifrado y la disponibilidad del proveedor |
| **Archivo sin conexión** (KeePassXC y similares) | Control total, sin dependencia de proveedores | Tú gestionas las copias y la sincronización |

*Elige cualquiera. La diferencia entre ambos es mucho menor que la diferencia entre usar un gestor y no usar ninguno.*

Consulta la comparación completa **[Mejores gestores de contraseñas 2026: Bitwarden frente a KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)** y la guía **[Cómo crear contraseñas seguras en 2026](/articles/how-to-create-strong-passwords/)**.

### 2. Segundos factores resistentes al phishing

Los segundos factores no son intercambiables. Difieren mucho en los ataques que resisten.

| Método | Detiene el relleno de credenciales | Detiene el phishing | Detiene el robo de tokens de sesión |
|---|---|---|---|
| **Códigos SMS** | Sí | Parcialmente, mediante intercambio de SIM | No |
| **Códigos de aplicación autenticadora** | Sí | Parcialmente, mediante retransmisión en tiempo real | No |
| **Aprobación push** | Sí | Débilmente, mediante bombardeo de avisos | No |
| **Claves de acceso o llave física** | Sí | **Sí** | Sí |

**Las claves de acceso y las llaves físicas FIDO2 son las únicas opciones de la lista que vencen al phishing.** La razón es estructural, no gradual: la credencial está vinculada al origen, así que un dominio parecido no recibe nada útil. La víctima no tiene ningún código que leerle en voz alta al atacante.

También hay que nombrar una amenaza relacionada porque invalida métodos que parecen seguros. **El malware infostealer ahora extrae directamente las cookies del navegador**, lo que permite a un atacante reutilizar una sesión autenticada sin tu contraseña ni el segundo factor. Por eso importa la última columna y **el punto 3 del nivel 1 no es opcional**.

*Orden de prioridad en este punto: claves de acceso cuando se ofrezcan, llave física para correo y finanzas, aplicación autenticadora para lo demás, SMS solo si no hay una opción mejor.*

{{< figure src="phishing-resistant-second-factor-comparison.webp" alt="Diagrama que compara códigos SMS, aplicaciones autenticadoras, aprobación push y claves de acceso frente al relleno de credenciales, phishing y robo de tokens de sesión. Las claves de acceso vencen a los tres." >}}

Genera y verifica códigos temporales localmente con nuestro **[Generador TOTP y HOTP](/totp-generator/)**. Lee un secreto Base32 o un URI `otpauth://` y funciona por completo en tu navegador.

### 3. Actualizaciones automáticas en todas partes

**La mayoría de las intrusiones exitosas explotan vulnerabilidades para las que ya existe un parche.** Los atacantes aprovechan el retraso de las actualizaciones.

La medida práctica no es estar más pendiente de las actualizaciones. Elimina la decisión activándolas de forma automática en todas las capas:

- **Sistema operativo**: Windows Update, Actualización de software en macOS o unattended-upgrades en Linux
- **Navegadores**: deja activa la actualización automática y reinicia cuando te lo pida. Un reinicio pendiente significa que el navegador sigue sin parchear.
- **Teléfono**: activa las actualizaciones automáticas de aplicaciones, no solo las del sistema operativo
- **Router**: esta es la capa que se olvida, aunque es accesible desde el exterior

**Un navegador pendiente de reinicio ejecuta código vulnerable.** Este solo hábito reduce más exposición que la mayoría de los puntos del nivel 3 juntos.

*Nuestro análisis de escape del kernel en **[Los contenedores ya no son una frontera de seguridad](/articles/containers-no-longer-security-boundary-2026/)** muestra lo importante que es el tiempo hasta aplicar un parche cuando interviene una escalada de privilegios.*

### 4. Cifra el dispositivo y usa una pantalla de bloqueo segura

**El cifrado de disco completo convierte el robo de un dispositivo en una pérdida de hardware, no en una filtración de datos.** Sin cifrado, quien tenga tu portátil o teléfono puede leerlo todo, incluido el almacén del gestor de contraseñas y los tokens de sesión activos.

Todas las plataformas principales ofrecen cifrado, aunque en algunas no está activado de forma predeterminada:

| Plataforma | Función | Comprobación |
|---|---|---|
| **Windows** | BitLocker o Device Encryption | Configuración, Privacidad y seguridad, Cifrado del dispositivo |
| **macOS** | FileVault | Ajustes del sistema, Privacidad y seguridad, FileVault |
| **Linux** | LUKS | Confirma al instalar que los volúmenes root y home estén cifrados |
| **iOS y Android** | Activado por defecto cuando configuras un código | Configura un código y confirma que el cifrado esté activo |

Junto al cifrado, importan dos reglas:

- **Usa una frase de contraseña o un PIN largo, no un código de cuatro dígitos.** Las cuentas de correo y finanzas merecen el bloqueo más fuerte del teléfono, porque el código protege todo lo demás en el dispositivo.
- **Prefiere un PIN a la biometría si te preocupa una posible coerción legal.** La biometría es cómoda y fácil de recordar, pero en algunas jurisdicciones las huellas o caras obtenidas por la fuerza reciben protecciones distintas de las que se aplican a los conocimientos forzados.

### 5. Copias de seguridad, probadas una vez

**El ransomware y los fallos de hardware tienen el mismo resultado, y una copia de seguridad es la única medida que resiste ambos.** Este es el elemento que más se omite y del que más se arrepiente la gente.

La estructura estándar es **3-2-1**: tres copias, en dos tipos de medios, con una fuera del sitio. Para una persona significa:

- **Una copia local** para recuperarte rápidamente
- **Una copia cifrada externa** frente al ransomware y los incendios
- **Una copia sin conexión o una copia con permiso de escritura** por si el ransomware llega a tu almacenamiento sincronizado

*Este último punto es el más importante y el que menos se implementa. El almacenamiento sincronizado no es una copia de seguridad. El ransomware y el borrado accidental también se replican.*

**Prueba una restauración al menos una vez.** Una copia nunca restaurada es una hipótesis.

## Nivel 2: Contener los daños

El nivel 1 supone que nada falla. El nivel 2 supone que algo fallará y limita las consecuencias.

### 6. Deja de reutilizar tu dirección de correo

**Tu dirección de correo es la clave que une todas las bases de datos que alguna vez se filtraron.** Usar una sola dirección en todas partes permite relacionar una filtración con las demás y da a la ingeniería social un punto de partida verificado.

**Los alias resuelven ambos problemas.** Genera una dirección única por servicio, para que la propia dirección actúe como etiqueta:

| Ventaja | Por qué importa |
|---|---|
| **Atribución de filtraciones** | Si llega spam a un alias, sabes qué servicio filtró o vendió tu dirección |
| **Bloqueo instantáneo** | Desactiva un alias sin tocar tu bandeja real |
| **Resistencia a la correlación** | Las direcciones distintas impiden reunir tus cuentas en un solo perfil |
| **Detección de phishing** | Los mensajes a un alias que ya no usas son claramente fraudulentos |

**El subdireccionamiento** (`you+service@example.com`) es una versión más débil. Permite saber quién filtró tu dirección, pero también revela tu dirección real y no impide relacionar tus cuentas.

*Si tienes un dominio, los alias catch-all te dan esto gratis. Si no, los proveedores de alias especializados hacen lo mismo.*

### 7. La recuperación de cuentas es la verdadera superficie de ataque

**Los atacantes evitan cada vez más la puerta principal y apuntan a la recuperación.** Debe funcionar tras perder un dispositivo y no convertirse en el eslabón más débil.

Configura lo siguiente en este orden:

- **Guarda los códigos de respaldo sin conexión.** Imprímelos o guárdalos en un medio cifrado y mantenlos **separados del gestor de contraseñas**, para que la vulneración de uno no entregue el otro.
- **Prefiere las claves de recuperación a las preguntas de seguridad.** Las respuestas sobre el apellido de soltera de tu madre o tu primer coche suelen constar en registros públicos.
- **Usa respuestas falsas si un sitio obliga a responder preguntas.** Guárdalas junto a la cuenta en el gestor.
- **Registra un segundo dispositivo o llave** cuando el servicio lo permita, para que un fallo no te deje fuera.
- **Elimina los contactos y números de recuperación antiguos**, porque ese número ahora pertenece a otra persona.

> **Advertencia: perder el segundo factor sin códigos de respaldo suele significar perder la cuenta para siempre, y el soporte no restaurará el acceso a una cuenta protegida correctamente.** Configura la recuperación al mismo tiempo que activas el segundo factor.

{{< figure src="three-two-one-backup-strategy-diagram.webp" alt="Diagrama del modelo 3-2-1 de copias de seguridad: tres copias de datos en dos medios, con una copia sin conexión protegida frente al ransomware y el borrado accidental" >}}

### 8. Supervisa las filtraciones para enterarte pronto

**El valor de una notificación de filtración depende por completo del momento.** Te interesa saberlo mientras la contraseña siga siendo válida en algún sitio.

- **Have I Been Pwned** envía alertas cuando tu dirección aparece en un conjunto de datos nuevo. También ofrece avisos para todo el dominio si te pertenece y usas alias.
- **Tu gestor de contraseñas ofrece una señal mejor**, porque sabe qué entradas del almacén corresponden al servicio notificado y te las señala directamente.

*El flujo útil es breve: llega una alerta, cambias la contraseña de la cuenta afectada y la cambias donde hayas reutilizado la anterior. Esa es la ventaja del punto 1 del nivel 1: las contraseñas únicas eliminan el segundo paso.*

### 9. Congela el crédito antes de necesitarlo

**Congelar el crédito es la defensa más sólida disponible frente al fraude de identidad con cuentas nuevas**, y no cuesta nada. Impide que los prestamistas consulten tu expediente para abrir cuentas a tu nombre.

En Estados Unidos, puedes congelarlo en cada una de las tres principales agencias de crédito. Puedes descongelarlo temporalmente y volver a congelarlo después de una solicitud legítima. Sigue estos pasos:

1. **Congela el expediente en las tres agencias**, no solo en una. Cada una conserva un archivo distinto.
2. **Guarda los PIN para descongelarlo** en el gestor de contraseñas.
3. **Descongélalo temporalmente** al solicitar crédito y vuelve a congelarlo después.

*Hazlo antes de necesitarlo. Descubrir el proceso en medio de un fraude, mientras impugnas cuentas, es el peor momento para aprenderlo.*

## Nivel 3: Reducir la exposición

El nivel 3 reduce la huella de datos. Importa, pero va después porque no bloquea la toma de control de cuentas.

### 10. Refuerza el navegador que usas

**El navegador es donde se expone gran parte de tus datos personales**, y dos cambios cubren la mayor parte del problema:

- **Instala un bloqueador de contenido.** Los anuncios y rastreadores son el principal mecanismo de recopilación en la web. Bloquearlos reduce el seguimiento y una parte considerable de la superficie de ataque. Elige un bloqueador confiable, no varios.
- **Reduce las extensiones a las que usas.** **Las extensiones leen y modifican el contenido de las páginas**, por lo que una extensión abandonada o maliciosa puede acceder directamente a tus sesiones. Revisa la lista cada trimestre.

*Conviene entender la aleatorización de la huella del navegador, pero rara vez merece prioridad. No aporta cero valor. Su rendimiento es bajo frente a los puntos 1 a 5 y además rompe algunos sitios.*

Consulta el análisis completo en **[Mejores navegadores para la privacidad 2026: LibreWolf frente a Brave y Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**.

### 11. Cifra tus consultas DNS

**El DNS sin cifrar permite que tu operador de red y cualquiera en el trayecto vea todos los dominios que consultas.** DNS sobre HTTPS o DNS sobre TLS cifra esas consultas.

Dos salvedades importantes:

- **DoH traslada la confianza, no la elimina.** El resolver ve tus consultas en lugar de tu proveedor de internet. Por eso importa elegir un resolver con una política de privacidad publicada, no solo usar el protocolo.
- **DoH evita el filtrado a nivel de red**, incluidos los controles parentales y corporativos de los que dependen muchas personas.

*Un beneficio de seguridad concreto además de la privacidad: el DNS cifrado elimina la suplantación de DNS como vía práctica de ataque en redes hostiles.*

### 12. Elimina metadatos antes de compartir

**Las fotos contienen más que píxeles.** La mayoría de las cámaras de teléfonos incorpora datos EXIF, incluidas coordenadas GPS, marcas de tiempo e identificadores del dispositivo.

**Esto importa más en documentos que en fotos.** Un PDF o archivo de oficina compartido suele conservar nombres de autor, historial de edición y rutas internas, que pueden revelar detalles de una organización.

Nuestro **[Visor EXIF](/exif-viewer/)** lee localmente los metadatos de una imagen, para que veas qué revela una foto sin subirla. **[Analizador de URL](/url-parser/)** hace lo mismo con los enlaces: muestra parámetros de seguimiento y credenciales incluidas en la autoridad antes de pegar una URL en un chat.

## Nivel 4: Seguridad física y humana

Este nivel toma unos treinta minutos y cubre lo que ningún control de software alcanza.

### 13. Control físico de tus dispositivos

- **Bloquea todas las pantallas**, con un tiempo de espera breve. Un portátil desbloqueado equivale a la vulneración de todas tus cuentas.
- **No dejes dispositivos a la vista en un vehículo.** Es una medida contra el robo, y el robo también implica pérdida de datos.
- **Usa un filtro de privacidad** en espacios públicos para impedir la mayoría de las miradas indiscretas.
- **Revisa los puntos de carga públicos** antes de conectar un dispositivo. Prefiere un cable solo de alimentación o tu propio adaptador de pared en vez de un puerto USB desconocido.

### 14. Verifica a las personas, no los mensajes

**El phishing por voz y video ya ha debilitado la idea de que una voz conocida demuestra identidad.** Clonar voces a partir de unos segundos de audio público es habitual, y la petición suele incluir urgencia y una solicitud de pago o credenciales.

La respuesta debe usar otro canal:

1. **Cuelga y devuelve la llamada** a un número que ya tenías guardado, no al que te dio quien llamó.
2. **Trata la urgencia como una señal**, no como una razón para actuar. Presionar para que actúes de inmediato es parte del ataque.
3. **Acuerda una frase de verificación** con los familiares a quienes alguien podría suplantar.
4. **Nunca transfieras dinero basándote solo en una llamada o mensaje de voz.**

*Es la medida de mayor rendimiento del nivel 4 y no cuesta nada.*

### 15. Documentos y eliminación

- **Tritura o redacta** los documentos que contengan números de cuenta, números de identificación o datos médicos.
- **Añade marcas de agua a los documentos** que compartas para un fin concreto, con el destinatario y la fecha. No cuesta nada y permite rastrear una filtración.
- **Solicita la exclusión de los sitios de búsqueda de personas** y espera repetir el proceso, porque los listados vuelven a aparecer.
- **Revisa los registros públicos** y solicita la eliminación cuando sea posible.

*Nuestra **[Lista de seguridad física](/checklists/physical-security-checklist/)** cubre esta capa con más detalle.*

## Lo que la mayoría hace al revés

Ocho hábitos que conviene abandonar, por qué persisten y qué hacer en su lugar.

| Hábito | Por qué persiste | Haz esto en su lugar |
|---|---|---|
| **Memorizar contraseñas cortas y complejas** | Durante años, esa fue la recomendación | Usa un gestor y una frase larga para desbloquear la bóveda |
| **Cambiar contraseñas según un calendario** | Políticas de cumplimiento antiguas | Cámbialas tras una notificación de filtración o una sospecha de vulneración, no por calendario |
| **Depender de SMS para cuentas críticas** | Es la opción predeterminada | Cambia las cuentas de correo, finanzas e identidad a claves de acceso o una llave física |
| **Guardar códigos 2FA junto a las contraseñas en el mismo gestor** | Es más cómodo | Separa ambos factores para que una vulneración no exponga los dos |
| **Tratar el almacenamiento sincronizado en la nube como copia de seguridad** | Lo parece | Añade una copia sin conexión o una copia con permiso de escritura |
| **Buscar una huella de navegador perfecta** | Se puede medir y parece una acción concreta | Haz primero los puntos 1 a 5 |
| **Responder con sinceridad las preguntas de seguridad** | Parece obligatorio | Usa respuestas falsas guardadas en el gestor |
| **Suponer que HTTPS significa que un sitio es seguro** | El candado da confianza | Verifica el dominio, ya que muchos sitios de phishing tienen certificados válidos |

El patrón de los ocho: **cada hábito es visible y medible, por eso atrae la atención, aunque cada uno queda por debajo de una medida más eficaz.** Quien optimiza la entropía de su huella antes de instalar un gestor de contraseñas invierte el orden.

> **Error común: considerar peligrosos los gestores de contraseñas porque concentran secretos.** Sí, concentran el riesgo, pero la alternativa es reutilizar contraseñas en decenas de sitios. Es mejor una concentración que controlas que una dispersión que no controlas.

## Protege tus datos al usar herramientas

Un problema práctico atraviesa todo este tema. **Las herramientas que ayudan a proteger tus cuentas a menudo te piden los mismos secretos que intentas proteger.**

Un comprobador de contraseñas que envía tu contraseña a un servidor es un riesgo. Una calculadora de hashes que sube el archivo anula el propósito. Una herramienta de certificados que consulta tu nombre de host informa a un tercero de qué sitios administras.

**Todas las herramientas de abajo se ejecutan en tu navegador**, sin subir datos ni crear una cuenta. Este sitio declara esa política y menciona abiertamente las excepciones en vez de esconderlas.

**Comprueba el límite por tu cuenta:** desconéctate de la red, abre la herramienta y observa el panel de red del navegador mientras procesas un valor de prueba. La afirmación de procesamiento local describe el diseño previsto. También debes revisar las extensiones del navegador y la versión de la herramienta.

| Tarea | Herramienta | Qué hace |
|---|---|---|
| **Crear una contraseña segura** | **[Generador de contraseñas](/password-generator/)** | Usa `crypto.getRandomValues` con muestreo por rechazo para evitar sesgos de módulo, además de la entropía de la configuración elegida |
| **Comprobar la fortaleza de una contraseña** | **[Comprobador de contraseñas](/password-checker/)** | Evalúa una contraseña localmente, incluidos patrones y reutilización |
| **Configurar un segundo factor** | **[Generador TOTP y HOTP](/totp-generator/)** | Lee secretos Base32 o URI `otpauth://` y verifica códigos en distintas ventanas de tiempo |
| **Inspeccionar el certificado de un sitio** | **[Información de certificado SSL](/ssl-certificate-info/)** | Muestra sujeto, vigencia, fortaleza de la clave, SAN e indicadores de algoritmos débiles |
| **Comprobar una cadena de certificados** | **[Comprobador de cadenas SSL](/ssl-chain-tester/)** | Ordena la cadena y verifica cada firma para detectar certificados intermedios ausentes |
| **Verificar una descarga o archivo** | **[Calculadora de hashes](/hash-calculator/)** | Calcula desde MD5 hasta SHA-512 para confirmar la integridad frente a un resumen publicado |
| **Generar identificadores únicos** | **[Generador UUID](/uuid-generator/)** | Genera identificadores versión 4 con bits de versión y variante correctos |
| **Inspeccionar un enlace sospechoso** | **[Analizador de URL](/url-parser/)** | Decodifica la ruta, enumera parámetros y marca credenciales en la autoridad |
| **Comprobar metadatos de fotos** | **[Visor EXIF](/exif-viewer/)** | Muestra coordenadas GPS, marcas de tiempo y datos del dispositivo incluidos en una foto |
| **Medir codificación o cifrado** | **[Analizador de entropía](/entropy-analyzer/)** | Calcula la entropía de Shannon para distinguir datos repetitivos de contenido codificado o cifrado |
| **Neutralizar un indicador de forma segura** | **[Desactivar y reactivar IOC](/ioc-defang-refang/)** | Desactiva URL y direcciones para que no se puedan abrir al compartirlas |

*El principio de la tabla: si una herramienta necesita el secreto, debería ejecutarse donde vive el secreto. Consulta **[Todas las herramientas](/tools/)** para ver la lista completa, incluidas las pocas que hacen solicitudes de red y el motivo.*

## La pregunta del modelo de amenazas

**La lista adecuada depende de a quién intentas mantener fuera**, y saltarte esta pregunta lleva a dedicar esfuerzo a los riesgos equivocados.

| Tu situación | Adversario realista | Dónde enfocarte |
|---|---|---|
| **La mayoría de las personas** | Delincuentes oportunistas, relleno automatizado de credenciales y phishing indiscriminado | Niveles 1 y 2, además de los dispositivos que llevas contigo |
| **Persona conocida o con un cargo público** | Phishing dirigido, doxxing e intentos de toma de cuentas | Añade compartimentación, alias y considera vigilar tu presencia en redes |
| **Periodista, activista o persona con riesgo legal** | Estados o adversarios con muchos recursos, incautación de dispositivos | Añade Tor, dispositivos dedicados y disciplina al separar identidades |
| **Dueño de una pequeña empresa** | Vulneración del correo empresarial, fraude de facturas y desvío de pagos | Verifica por otro canal cada transferencia |
| **Profesional técnico** | Cadena de suministro, robo de credenciales y ataques mediante dependencias | Añade llaves físicas, prácticas de firma de código y separación de identidades laborales y personales |

**La lectura honesta de la tabla.** Para la mayoría, gran parte del riesgo realista se concentra en los niveles 1 y 2. Las medidas avanzadas son fundamentales para quienes las necesitan y a menudo las adopta gente que no las necesita.

*Nuestra guía **[Cómo crear tu propio modelo de amenazas](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)** explica cómo hacer esta evaluación.*

## Puntos clave

- **El orden importa más que la exhaustividad.** Cinco medidas del nivel 1 reducen más riesgos reales que los 300 puntos de una lista integral hechos al azar.
- **Las claves de acceso y las llaves físicas son los únicos segundos factores que resisten el phishing**, porque la credencial está vinculada al origen y nunca sale de tu dispositivo.
- **El malware infostealer roba directamente las cookies de sesión**, por eso el robo de tokens de sesión hace que un segundo factor débil no sea suficiente por sí solo.
- **El cifrado convierte el robo de un dispositivo en una pérdida de hardware** en lugar de una filtración de datos. Confirma que esté activado, porque no siempre viene activo de forma predeterminada.
- **El almacenamiento sincronizado no es una copia de seguridad.** Añade una copia sin conexión o una copia con permiso de escritura, y prueba una restauración.
- **La recuperación de cuentas es la nueva superficie de ataque.** Guarda los códigos de respaldo sin conexión y separados del gestor de contraseñas.
- **Los alias rompen la correlación** entre las bases de datos filtradas que contienen tu dirección.
- **La mayoría de los consejos optimizados ofrece poco rendimiento.** Los ajustes de huella y la suplantación del user-agent quedan muy por debajo de un gestor de contraseñas y las actualizaciones automáticas.
- **La lista correcta depende de tu adversario.** Las medidas avanzadas son fundamentales para quienes las necesitan y a menudo las adopta gente que no las necesita.

## Próximos pasos

1. **Haz hoy el nivel 1**, que toma unas dos horas: un gestor de contraseñas, un segundo factor resistente al phishing, actualizaciones automáticas, cifrado del dispositivo y una copia de seguridad probada.
2. **Consulta una lista comunitaria** con cientos de puntos en una docena de categorías: **[Lista de seguridad personal](https://github.com/Lissy93/personal-security-checklist)**
3. **Usa la versión interactiva** para filtrar según tu modelo de amenazas y registrar tu progreso: **[Digital Defense](https://digital-defense.io)**
4. **Aplica las listas organizativas del sitio** para las medidas equivalentes en el ámbito profesional: **[Seguridad de contraseñas](/checklists/password-security-checklist/)**, **[Concienciación sobre phishing](/checklists/phishing-awareness-checklist/)**, **[Copia de seguridad y recuperación de datos](/checklists/data-backup-recovery-checklist/)**, **[Seguridad de dispositivos móviles](/checklists/mobile-device-security-checklist/)** y **[Seguridad en redes sociales](/checklists/social-media-security-checklist/)**
5. **Elige un gestor de contraseñas** con la comparación de arquitecturas: **[Bitwarden frente a KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)**
6. **Cambia a un navegador mejor** en vez de optimizar uno más débil: **[LibreWolf frente a Brave y Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**
7. **Protege tus datos de pago** con números de tarjeta virtuales: **[Tarjetas virtuales de Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/)**
8. **Usa las herramientas localmente**, empezando por el **[Generador de contraseñas](/password-generator/)** y el **[Generador TOTP](/totp-generator/)**

## Artículos relacionados

| Artículo | Qué cubre |
|---|---|
| **[Cómo crear tu propio modelo de amenazas](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)** | La evaluación que determina el nivel adecuado para ti |
| **[Mejores gestores de contraseñas 2026: Bitwarden frente a KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)** | Elegir entre bóvedas sincronizadas en la nube y sin conexión |
| **[Cómo crear contraseñas seguras en 2026](/articles/how-to-create-strong-passwords/)** | Entropía, frases de contraseña y por qué la longitud supera al reemplazo de símbolos |
| **[Guía de autenticación multifactor](/articles/what-are-the-diferent-kinds-of-factors-in-mfa/)** | La clasificación de factores detrás de la comparación de segundos factores |
| **[Mejores navegadores para la privacidad 2026: LibreWolf frente a Brave y Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)** | Refuerzo del navegador para el nivel 3 |
| **[Opciones de relojes inteligentes para privacidad y seguridad](/articles/smartwatches-for-privacy-and-security-enthusiasts/)** | Aplicar la misma lógica de niveles a los dispositivos ponibles |
| **[Tarjetas virtuales de Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/)** | Reducir la exposición de pagos, junto con la congelación del crédito |

## Referencias

1. [Lista de seguridad personal, lista comunitaria de Alicia Sykes](https://github.com/Lissy93/personal-security-checklist)
2. [Lista de seguridad personal, documento completo](https://github.com/Lissy93/personal-security-checklist/blob/HEAD/CHECKLIST.md)
3. [Digital Defense, versión interactiva](https://digital-defense.io)
4. [Awesome Privacy, lista de software que respeta la privacidad](https://github.com/lissy93/awesome-privacy)
5. [Have I Been Pwned, notificaciones de filtraciones](https://haveibeenpwned.com)
6. [FIDO Alliance, especificaciones de claves de acceso y FIDO2](https://fidoalliance.org/passkeys/)
7. [Use Plaintext Email, configuración de correo en texto plano](https://useplaintext.email/)
8. [Consumer Financial Protection Bureau, informes y puntuaciones de crédito](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
9. [FTC, consejos para consumidores sobre robo de identidad](https://consumer.ftc.gov/identity-theft-and-online-security)
10. [Passkeys.dev, recurso comunitario sobre la implementación de claves de acceso](https://passkeys.dev/)
