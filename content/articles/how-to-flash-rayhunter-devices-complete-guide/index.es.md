---
title: "Cómo flashear dispositivos Rayhunter: guía completa"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Flashea y configura Rayhunter para detectar captadores IMSI. Comprueba qué dispositivos son compatibles, instala el firmware, verifica que funcione y resuelve problemas habituales."
tags: ["Rayhunter", "captador de IMSI", "simulador de estación celular", "seguridad móvil", "detección de vigilancia", "protección de la privacidad", "Orbic RC400L", "TP-Link M7350", "punto de acceso móvil", "flasheo de dispositivos", "ciberseguridad", "seguridad inalámbrica", "contramedidas de vigilancia", "EFF", "herramientas de privacidad", "comprar Rayhunter", "guía de instalación", "configuración", "dispositivos compatibles", "seguridad de red"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Un dispositivo Rayhunter detecta señales inalámbricas y captadores IMSI, rodeado de escudos de seguridad"
coverCaption: "Sistema Rayhunter de detección de captadores IMSI para proteger las comunicaciones móviles de la vigilancia"
---

**Guía completa para flashear y configurar Rayhunter, el sistema definitivo para detectar captadores IMSI.**

## Resumen

**Rayhunter** es un sistema de código abierto que detecta captadores IMSI y funciona en puntos de acceso móviles modificados. Te avisa cuando equipos de vigilancia intentan interceptar comunicaciones celulares. Esta guía cubre la instalación completa en dispositivos Orbic RC400L y TP-Link M7350, las opciones de configuración, el análisis de actores de amenazas y su eficacia en redes 5G. Necesitas un dispositivo compatible con módem Qualcomm. El sistema detecta vigilancia en redes 2G, 3G y 4G mediante varias heurísticas. Sigue siendo útil pese a la adopción de 5G, porque continúan los ataques que fuerzan la conexión a generaciones de red anteriores. Ofrece protección esencial a periodistas, activistas y personas preocupadas por la privacidad frente a la vigilancia gubernamental, criminal y empresarial.

**Rayhunter** es una herramienta de código abierto diseñada para detectar captadores IMSI (simuladores de estaciones celulares) que pueden interceptar comunicaciones móviles. Si quieres **comprar Rayhunter** o aprender a flashear y configurar correctamente estos dispositivos, esta guía completa explica todo lo necesario sobre la instalación, la configuración y el uso de los sistemas **Rayhunter**.

**Declaración de patrocinio:** Este artículo está patrocinado por [STS Collective](https://stscollective.com), el principal proveedor de dispositivos compatibles con Rayhunter. A pesar del patrocinio, toda la información técnica, los análisis y las recomendaciones de esta guía son imparciales y se basan únicamente en la documentación oficial de Rayhunter, las opiniones de la comunidad y una evaluación técnica objetiva.

> 💰 **Descuento exclusivo para lectores:** Ahorra hasta un 20 % en dispositivos Rayhunter y todos los productos de STS Collective. Usa el código **SIMEONONSECURITY** al pagar o [compra directamente con el descuento aplicado](https://stscollective.com/discount/SIMEONONSECURITY).

## Introducción a Rayhunter

**Rayhunter** es un sistema avanzado de detección de captadores IMSI desarrollado por la **Electronic Frontier Foundation (EFF)**, una destacada organización sin ánimo de lucro dedicada a defender las libertades civiles en el mundo digital. Desde 1990, la EFF defiende la privacidad digital, la libertad de expresión y la innovación mediante litigios estratégicos, análisis de políticas, activismo de base y desarrollo tecnológico.

Esta potente herramienta funciona en puntos de acceso móviles compatibles y supervisa continuamente las redes celulares en busca de actividad sospechosa que pueda indicar la presencia de simuladores de estaciones celulares o «Stingrays» usados para vigilar. **Rayhunter** refleja el compromiso de la EFF de proporcionar herramientas prácticas de protección de la privacidad a personas y organizaciones que necesitan protegerse frente a la vigilancia.

El sistema **Rayhunter** ofrece alertas en tiempo real cuando detecta comportamientos potencialmente maliciosos en la red celular. Es una herramienta esencial de protección de la privacidad para periodistas, activistas, profesionales de seguridad y personas preocupadas por la privacidad. Puedes encontrar dispositivos compatibles **[con Rayhunter](https://stscollective.com/collections/rayhunter)** en STS Collective, el principal proveedor de estos dispositivos especializados.

### Apoyar el proyecto Rayhunter

**Rayhunter** es un proyecto de código abierto que se beneficia del apoyo de la comunidad. Puedes contribuir a su desarrollo continuo de varias maneras:

- **Comprar en STS Collective**: STS Collective dona a la EFF una parte de las ganancias de cada dispositivo Rayhunter vendido para apoyar el desarrollo continuo de **Rayhunter** y la investigación sobre privacidad.
- **Donaciones directas**: apoya directamente la labor de la EFF en favor de la privacidad y el desarrollo de **Rayhunter** mediante una **[donación a la EFF](https://supporters.eff.org/donate/donate)**.
- **Participar en la comunidad**: contribuye a los debates, la documentación y las pruebas en el repositorio oficial de GitHub.

Tu apoyo ayuda a mantener **Rayhunter** gratuito, de código abierto y en constante mejora para responder a las amenazas de vigilancia que evolucionan.

## Soporte, comentarios y comunidad

**Rayhunter** cuenta con el apoyo de una comunidad activa de investigadores de seguridad, defensores de la privacidad y ciudadanos preocupados. Puedes obtener ayuda y contribuir al proyecto por varios canales:

- **Documentación oficial**: [Documentación de Rayhunter](https://efforg.github.io/rayhunter/introduction.html), con guías completas de instalación, configuración y uso
- **Repositorio de GitHub**: [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Debates de la comunidad**: inicia debates en GitHub sobre compatibilidad de dispositivos y resolución de problemas
- **Investigación de seguridad**: colabora con investigadores para mejorar las capacidades de detección de **Rayhunter**

Si buscas dispositivos compatibles, STS Collective ofrece opciones **[de Rayhunter a la venta](https://stscollective.com/collections/rayhunter)**.

## Preguntas frecuentes

### ¿Necesito una tarjeta SIM activa para usar Rayhunter?

**Rayhunter** necesita que el dispositivo tenga una tarjeta SIM, pero no hace falta que tenga un plan de servicio activo. La SIM permite que el dispositivo se conecte a redes celulares y supervise actividades sospechosas. Si quieres usar el dispositivo como punto de acceso mientras ejecutas **Rayhunter**, necesitarás un plan activo.

### ¿Cómo puedo comprobar si mi dispositivo Rayhunter funciona?

Activa la heurística de prueba en los ajustes de configuración de **Rayhunter**. El dispositivo generará una alerta cada vez que detecte una torre celular, lo que te permitirá comprobar que el sistema funciona correctamente. Este modo de prueba genera muchas alertas, así que desactívalo después de la comprobación.

### ¿Me conviene un dispositivo bloqueado o desbloqueado?

Para la compatibilidad con **Rayhunter**, suelen preferirse los dispositivos desbloqueados, sobre todo si planeas usar tarjetas SIM que no sean de Verizon. La mayoría de los dispositivos Orbic de marca Verizon están desbloqueados, pero comprueba la compatibilidad antes de comprarlos. STS Collective ofrece dispositivos compatibles verificados **[con Rayhunter](https://stscollective.com/collections/rayhunter)**.

{{< stscollective-ad "rayhunter" >}}

## Guía de instalación

### Instalar la versión más reciente

La instalación de **Rayhunter** se ha probado en macOS y Ubuntu 24.04. Si tienes problemas con las versiones precompiladas, quizá debas instalarlo desde el código fuente.

#### Requisitos previos

Antes de instalar **Rayhunter**, asegúrate de tener un dispositivo compatible. En dispositivos TP-Link, inserta una tarjeta SD formateada en FAT para guardar las grabaciones.

#### Descarga y configuración

1. **Descarga la versión más reciente**: obtén el archivo `rayhunter-vX.X.X-PLATFORM.zip` adecuado desde la página oficial de versiones:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Extrae el archivo y abre la carpeta**:
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Conecta el dispositivo**: enciéndelo y conéctalo por WiFi o anclaje USB. Deberías poder acceder a:
   - Dispositivos Orbic: `http://192.168.1.1`
   - Dispositivos TP-Link: `http://192.168.0.1`

#### Instalación específica del dispositivo

**Para dispositivos Orbic RC400L** (disponibles **[con Rayhunter](https://stscollective.com)**):

**Rayhunter** ofrece dos métodos de instalación para dispositivos Orbic RC400L. Se recomienda el método WiFi para la mayoría de los usuarios, mientras que el método USB ofrece funciones adicionales de depuración.

**Método de instalación WiFi (recomendado)**:
```bash
# Los usuarios de macOS deben ejecutar primero este comando:
xattr -d com.apple.quarantine installer

# Para Verizon RC400L (la contraseña de administrador es la misma que la contraseña WiFi):
./installer orbic --admin-password 'YourWiFiPassword'

# Para Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Para dispositivos Moxee (formato de contraseña: 12$ + los 3 últimos dígitos de la contraseña WiFi):
./installer orbic --admin-password='12$XXX'
```

**Método de instalación USB (usuarios avanzados)**:
El método USB habilita el acceso a ADB (Android Debug Bridge) para depuración avanzada, pero no se recomienda en instalaciones habituales:

```bash
# AVISO: el instalador USB no se recomienda para la mayoría de los casos
./installer orbic-usb
```

Este método fuerza al dispositivo a entrar en modo de depuración para habilitar ADB, instala rootshell y **Rayhunter**, y después reinicia el dispositivo. Úsalo solo si necesitas ADB para otros fines.

**Para dispositivos TP-Link M7350** (disponibles **[con Rayhunter](https://stscollective.com)**):
```bash
./installer tplink
```

El instalador completará el flasheo de **Rayhunter** y reiniciará el dispositivo. Una línea verde en la pantalla indica que **Rayhunter** está funcionando correctamente.

### Instalar desde el código fuente

Para desarrolladores o usuarios que necesiten compilar **Rayhunter** desde el código fuente, el proyecto incluye:

- **Interfaz**: aplicación SvelteKit en JavaScript (`./daemon/web/`)
- **Servidor**: binario de Rust `rayhunter-daemon` (`./daemon/`)
- **Instalador**: binario de Rust que incluye todos los componentes (`./installer`)

#### Dependencias de compilación

Instala las siguientes dependencias:
- Lenguaje de programación Rust
- Node.js/npm
- Herramientas de compilación C (`build-essential` en Linux, `xcode-select --install` en macOS)

#### Proceso de compilación

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Sustituye 'orbic' por el tipo de tu dispositivo
```

Para desarrollar la interfaz con recarga automática:
```bash
cd daemon/web
npm run dev
# O con un objetivo personalizado:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Actualizar Rayhunter

La actualización de **Rayhunter** sigue el mismo proceso que la instalación. Repite los pasos con la versión más reciente para actualizar el dispositivo a la última versión de **Rayhunter**.

## Configuración

Puedes configurar **Rayhunter** desde la interfaz web o editando directamente `/data/rayhunter/config.toml` en el dispositivo.

### Configuración de la interfaz web

Para abrir la interfaz web de **Rayhunter**, conéctate a la red del dispositivo y visita:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Panel de la interfaz web de Rayhunter" caption="La interfaz web de Rayhunter ofrece opciones completas de supervisión y configuración" >}}

#### Opciones principales de configuración

**Nivel de interfaz del dispositivo**: controla lo que **Rayhunter** muestra en la pantalla:
- **Modo invisible**: no muestra nada
- **Modo discreto**: indicador de línea de color (verde=seguro, rojo=alerta, blanco=pausado)
- **Modo de demostración**: muestra gráficos de orcas y una línea de estado
- **Logotipo de EFF**: muestra el logotipo de EFF y una línea de estado
- **Alta visibilidad**: pantalla a color completa

**Modo de entrada del dispositivo**: configura el comportamiento del botón de encendido:
- **Desactivar control con botón**: desactiva el botón de encendido para **Rayhunter**
- **Doble toque para reiniciar la grabación**: restablece las alertas y reinicia la supervisión

**Ajustes de notificación**: configura la URL de ntfy para alertas remotas y activa o desactiva las notificaciones de advertencia y batería baja.

**Heurísticas del analizador**: activa o desactiva algoritmos de detección concretos de **Rayhunter** según tu entorno y modelo de amenazas.

## Desinstalar Rayhunter

### Dispositivos Orbic

Para eliminar **Rayhunter** de dispositivos Orbic:

```bash
./installer util orbic-shell --admin-password mypassword
```

Dentro del intérprete de comandos:

> **Aviso:** Los siguientes comandos eliminan permanentemente los archivos de Rayhunter y sus scripts de inicio. Confirma que estás en el intérprete del dispositivo previsto, copia las grabaciones o la configuración que necesites y ten a mano el instalador y el firmware compatible. Después, comprueba que los archivos ya no estén y que el dispositivo se reinicie sin el servicio Rayhunter. Para revertir el cambio, reinstala la misma versión desde el repositorio oficial.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### Dispositivos TP-Link

Para desinstalarlo de dispositivos TP-Link:

> **Aviso:** Estos comandos eliminan los archivos de Rayhunter y su script de inicio del dispositivo TP-Link. Exporta primero las grabaciones y la configuración. Ejecútalos solo dentro del intérprete del dispositivo, y luego comprueba que las rutas ya no existan y que el dispositivo arranque con normalidad. Reinstala la misma versión desde el repositorio oficial para revertirlo.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Elimina los activadores de puerto restantes en la interfaz de administración de TP-Link, en Settings > NAT Settings > Port Triggers.

## Usar Rayhunter

Una vez instalado, **Rayhunter** se inicia automáticamente y supervisa continuamente las redes celulares en busca de actividad sospechosa. Durante el funcionamiento normal, la pantalla muestra una línea verde, que cambia a puntos amarillos, guiones naranjas o una línea roja continua si detecta posibles captadores IMSI.

### Heurísticas de detección de Rayhunter

**Rayhunter** utiliza varios algoritmos avanzados para identificar posibles actividades de captadores IMSI:

#### Detección de solicitudes IMSI
Esta heurística identifica secuencias sospechosas en las que las torres celulares solicitan la identidad del dispositivo (IMSI, International Mobile Subscriber Identity) sin seguir los protocolos adecuados de autenticación. **Rayhunter** supervisa el momento y el contexto de estas solicitudes y marca patrones anormales que indican la posible presencia de equipos de vigilancia.

Las redes celulares legítimas siguen procedimientos de autenticación normalizados antes de solicitar identificadores confidenciales. Los captadores IMSI suelen saltarse estos protocolos para recopilar rápidamente las identidades de los dispositivos, lo que genera anomalías detectables en la secuencia de autenticación. Este método es especialmente eficaz frente a captadores IMSI «pasivos» básicos, que se limitan a recopilar información del dispositivo.

#### Detección de desconexiones y bajadas a 2G
**Rayhunter** supervisa continuamente los intentos sospechosos de obligar a los dispositivos móviles a desconectarse de redes 4G/5G seguras y volver a conectarse a redes 2G menos seguras. Los captadores IMSI usan con frecuencia este ataque de bajada, porque las redes 2G tienen un cifrado más débil y son más fáciles de interceptar.

El sistema analiza los patrones de desconexión en busca de frecuencias, momentos o contextos anormales que sugieran intención maliciosa en lugar de una optimización normal de la red. A veces, las redes legítimas pueden sugerir una bajada por motivos de cobertura o capacidad, pero **Rayhunter** distingue entre el comportamiento normal de la red y posibles actividades de vigilancia.

#### Detección de bajadas LTE SIB6/7
Los bloques de información del sistema (SIB) son mensajes que las redes celulares emiten para proporcionar datos de configuración a los dispositivos móviles. **Rayhunter** supervisa específicamente los mensajes SIB6 y SIB7, que contienen información sobre celdas vecinas y redirección de frecuencias.

Los actores maliciosos pueden emitir mensajes SIB6/7 falsos para obligar a los dispositivos a abandonar conexiones 4G seguras y conectarse a redes 2G controladas por el atacante. **Rayhunter** analiza estas emisiones para detectar incoherencias, patrones de redirección anormales y otros indicios de estaciones base fraudulentas que intentan rebajar la conexión del dispositivo para interceptarla.

#### Detección de cifrado nulo
Este método esencial identifica cuándo las redes celulares proponen comunicaciones sin cifrado (cifrado nulo). Las redes celulares comerciales legítimas nunca deberían proponer conexiones sin cifrar, ya que esto infringiría las normas de seguridad y los requisitos reglamentarios.

**Rayhunter** marca como muy sospechosa cualquier red que proponga cifrado nulo. *Una red legítima nunca propondrá cifrado nulo.* Es un indicador claro de que un equipo de vigilancia intenta interceptar comunicaciones en texto sin formato. Esta heurística es especialmente eficaz frente a captadores IMSI que priorizan recopilar datos por encima de mantener la apariencia de una red legítima.

#### Detección de SIB incompletos
Las estaciones base celulares legítimas emiten bloques de información del sistema completos con datos esenciales de configuración de red. **Rayhunter** supervisa las estaciones que proporcionan información incompleta o que no proporcionan información del sistema, lo que a menudo indica equipos de vigilancia desplegados con prisas o mal configurados.

Los captadores IMSI a menudo no implementan toda la funcionalidad de la red celular, y se centran solo en las funciones mínimas para conectar dispositivos e interceptar datos. Al detectar estas implementaciones incompletas, **Rayhunter** puede identificar estaciones base potencialmente maliciosas a las que les faltan las funciones esperadas de una infraestructura celular legítima.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Diagrama de las cinco heurísticas de detección de Rayhunter: solicitud IMSI sin autenticación, ataque de bajada a 2G, redirección LTE SIB6/7, propuesta de cifrado nulo y emisión de información del sistema incompleta" >}}

## Actores de amenazas y posibles objetivos

Entender quién despliega captadores IMSI y a quién se dirigen es esencial para evaluar tu modelo personal de amenazas y elegir una configuración adecuada de **Rayhunter**. Los actores de amenazas tienen distintos niveles de sofisticación, y sus estrategias para elegir objetivos ayudan a determinar los tipos de vigilancia que **Rayhunter** está diseñado para detectar.

### Organismos gubernamentales y fuerzas del orden

**Sofisticación de la amenaza**: de avanzada a profesional
**Objetivos principales**:
- Sospechosos de delitos bajo investigación
- Personas de interés en casos de seguridad nacional
- Manifestantes y activistas durante protestas
- Vigilancia general de la población en zonas de alta seguridad
- Ciudadanos extranjeros y personal diplomático

**Patrones de detección**: Los captadores IMSI operados por gobiernos suelen usar equipos sofisticados que pueden evitar las heurísticas básicas de detección. Aun así, recurren con frecuencia a **ataques de bajada a 2G** y **patrones de desconexión** para forzar a los dispositivos a usar redes menos seguras y facilitar la interceptación. La detección de bajadas LTE SIB6/7 y la supervisión de desconexiones de **Rayhunter** son especialmente eficaces contra las técnicas de vigilancia de las fuerzas del orden.

**Situaciones habituales**:
- Vigilancia de eventos en protestas, manifestaciones o reuniones públicas
- Seguimiento de ubicación cerca de instalaciones gubernamentales o infraestructuras sensibles
- Vigilancia dirigida de personas concretas bajo investigación
- Operaciones de vigilancia en fronteras y aeropuertos

### Agencias de inteligencia nacionales y extranjeras

**Sofisticación de la amenaza**: de profesional a militar
**Objetivos principales**:
- Agentes y recursos de inteligencia extranjeros
- Funcionarios gubernamentales y personal diplomático
- Contratistas e investigadores de defensa
- Directivos de empresas de sectores estratégicos
- Periodistas que informan sobre seguridad nacional
- Activistas que trabajan en asuntos políticos sensibles

**Patrones de detección**: Los equipos de inteligencia están diseñados para pasar desapercibidos, pero la detección de cifrado nulo y la supervisión de SIB incompletos de **Rayhunter** pueden identificar incluso operaciones sofisticadas. Durante operaciones dirigidas, las agencias de inteligencia suelen usar equipos que solicitan **información IMSI**, lo que activa los algoritmos de **Rayhunter** para detectar solicitudes IMSI.

**Situaciones habituales**:
- Vigilancia prolongada de objetivos de alto valor para la inteligencia
- Espionaje industrial cerca de sedes corporativas
- Supervisión diplomática y de embajadas
- Operaciones de contrainteligencia
- Servicios de inteligencia extranjeros que apuntan a recursos nacionales

### Organizaciones criminales

**Sofisticación de la amenaza**: de básica a intermedia
**Objetivos principales**:
- Personas adineradas para secuestro o extorsión
- Competidores empresariales para obtener inteligencia corporativa
- Personal policial que investiga el crimen organizado
- Testigos e informantes en causas penales
- Víctimas de acoso, hostigamiento o maltrato doméstico

**Patrones de detección**: Las organizaciones criminales suelen usar captadores IMSI comerciales de bajo coste que activan varias heurísticas de **Rayhunter** al mismo tiempo. Estos dispositivos suelen tener **implementaciones SIB incompletas**, usar **cifrado nulo** para recopilar más datos y realizar **ataques agresivos de bajada a 2G** debido a su menor sofisticación técnica.

**Situaciones habituales**:
- Seguimiento de posibles objetivos de secuestro o robo
- Supervisión de comunicaciones policiales durante operaciones criminales
- Espionaje empresarial y recopilación de inteligencia competitiva
- Campañas de acoso y hostigamiento
- Intimidación de testigos y seguimiento de ubicación

### Espionaje corporativo e inteligencia privada

**Sofisticación de la amenaza**: de intermedia a avanzada
**Objetivos principales**:
- Directivos de empresas competidoras
- Equipos de investigación y desarrollo
- Negociadores de fusiones y adquisiciones
- Titulares de propiedad intelectual
- Custodios de secretos comerciales
- Denunciantes corporativos y fuentes de amenazas internas

**Patrones de detección**: Las operaciones de vigilancia corporativa suelen usar equipos de gama media que equilibran coste y capacidad. Estos despliegues activan con frecuencia la **detección de desconexiones** y las **alertas de solicitudes IMSI** al dirigirse a personas concretas durante negociaciones comerciales o ciclos de desarrollo de productos.

**Situaciones habituales**:
- Vigilancia durante negociaciones de fusiones y adquisiciones
- Recopilación de inteligencia competitiva en ferias y conferencias
- Operaciones de robo de propiedad intelectual
- Supervisión de empleados y detección de amenazas internas
- Recopilación de datos de clientes para obtener ventaja competitiva

### Investigadores privados y empresas de vigilancia

**Sofisticación de la amenaza**: de básica a intermedia
**Objetivos principales**:
- Personas investigadas por fraude de seguros
- Cónyuges en procesos de divorcio
- Empleados sospechosos de conducta indebida
- Personas implicadas en disputas legales
- Celebridades y personas destacadas

**Patrones de detección**: Las operaciones de vigilancia privada suelen usar equipos comerciales con poca personalización. Por las limitaciones de costes y técnicas, estos sistemas suelen activar las heurísticas básicas de **Rayhunter**, sobre todo la **detección de cifrado nulo** y la **supervisión de SIB incompletos**.

**Situaciones habituales**:
- Investigaciones de divorcio y custodia
- Vigilancia por fraude de seguros
- Investigaciones de mala conducta de empleados
- Acoso a celebridades y operaciones de paparazzi
- Investigación de casos legales y recopilación de pruebas

### Personas malintencionadas y hacktivistas

**Sofisticación de la amenaza**: de básica a intermedia
**Objetivos principales**:
- Enemigos personales o parejas sentimentales
- Figuras públicas y celebridades
- Víctimas aleatorias en espacios públicos
- Participantes en eventos o ubicaciones concretas
- Miembros de comunidades o grupos seleccionados

**Patrones de detección**: Los atacantes individuales suelen usar configuraciones básicas, a menudo improvisadas, de captadores IMSI que activan varios algoritmos de **Rayhunter** al mismo tiempo. Es habitual que estos despliegues usen **cifrado nulo**, **emisiones SIB incompletas** y rudimentarios **intentos de bajada a 2G**.

**Situaciones habituales**:
- Campañas de persecución y hostigamiento
- Robo de identidad y fraude financiero
- Activismo político e interrupción de protestas
- Actividades generales de ciberdelincuencia
- Vigilancia oportunista en eventos públicos

### Evaluación de amenazas y configuración de Rayhunter

Las **personas de alto riesgo** (periodistas, activistas, funcionarios gubernamentales y directivos) deberían activar todas las heurísticas de **Rayhunter** y usar el modo de pantalla de **alta visibilidad** para maximizar la capacidad de detección.

Las **personas de riesgo moderado** (usuarios generalmente preocupados por la privacidad) pueden usar pantallas en **modo discreto** con las heurísticas principales activadas para protegerse a diario sin llamar la atención.

La **protección para eventos** (protestas, reuniones sensibles o viajes) justifica la activación temporal de todos los métodos de detección y los sistemas de notificación para tener una visión completa de la vigilancia.

Conocer tu modelo de amenazas te ayuda a optimizar la configuración de **Rayhunter** para tu perfil de riesgo y a conseguir una cobertura adecuada frente a los actores que con más probabilidad puedan dirigirse contra ti o tus actividades.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Diagrama de varios actores de amenazas que usan captadores IMSI, incluidas agencias gubernamentales, organizaciones criminales y operadores de espionaje corporativo que apuntan a dispositivos móviles" >}}

## Eficacia de Rayhunter en la era 5G

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Diagrama de un teléfono compatible con 5G forzado mediante un ataque de bajada a una red 4G o 3G supervisada, una técnica que Rayhunter sigue detectando en la era 5G" >}}

A medida que las redes celulares pasan a la tecnología 5G, surgen dudas sobre la eficacia continuada de **Rayhunter**, que detecta redes 2G, 3G y 4G/LTE, pero no los métodos nativos de vigilancia 5G. Para planificar estrategias de detección a largo plazo, es esencial comprender las limitaciones actuales y la relevancia de **Rayhunter** en un mundo 5G.

### Por qué Rayhunter sigue siendo eficaz en redes 5G

#### Persistencia de los ataques de bajada
El vector de ataque fundamental que detecta **Rayhunter**, obligar a los dispositivos a conectarse a redes menos seguras, sigue siendo muy relevante en los despliegues 5G. Los **captadores IMSI siguen recurriendo a ataques de bajada a 2G y 3G** porque:

- **Menor coste de implementación**: crear equipos de vigilancia para protocolos antiguos requiere mucha menos inversión que desarrollar sistemas compatibles con 5G
- **Compatibilidad con más dispositivos**: apuntar a 2G/3G permite vigilar también dispositivos antiguos que quizá no sean compatibles con 5G
- **Metodologías de ataque consolidadas**: las técnicas de vigilancia para redes 2G/3G están bien documentadas y probadas
- **Ventajas normativas**: algunas tecnologías de vigilancia antiguas pueden tener menos restricciones legales que los métodos avanzados de interceptación 5G

#### Compatibilidad con redes anteriores
Las redes 5G mantienen la **compatibilidad con 4G/LTE**, y la mayoría de los dispositivos móviles admiten varias generaciones simultáneamente. Esta compatibilidad sigue ofreciendo oportunidades para los ataques de bajada que **Rayhunter** se especializa en detectar:

- **Cambio automático a una red anterior**: los dispositivos vuelven naturalmente a 4G cuando la cobertura 5G es deficiente, lo que ofrece oportunidades para que los equipos de vigilancia intercepten estas transiciones
- **Vulnerabilidades en la negociación de protocolos**: captadores IMSI sofisticados pueden manipular el proceso de negociación entre generaciones de red
- **Explotación de brechas de cobertura**: equipos de vigilancia ubicados estratégicamente en zonas sin cobertura 5G completa pueden forzar a los dispositivos a usar redes 4G/LTE supervisadas

#### Despliegue gradual de 5G
El **despliegue lento de una cobertura 5G completa** garantiza que **Rayhunter** seguirá siendo pertinente durante años:

- **Diferencias entre zonas urbanas y rurales**: muchas regiones todavía dependen principalmente de redes 4G/LTE, donde las capacidades de detección de **Rayhunter** siguen siendo directamente útiles
- **Limitaciones de cobertura interior**: la señal 5G suele atravesar mal los edificios, por lo que los dispositivos vuelven a redes 4G que **Rayhunter** puede supervisar eficazmente
- **Consideraciones para viajes internacionales**: el despliegue global de 5G varía mucho entre países, de modo que la vigilancia 4G/LTE sigue siendo un riesgo para los viajeros

#### Retraso tecnológico de los actores de amenazas
Los **ciclos de adquisición y despliegue de equipos de vigilancia** suelen ir por detrás de la tecnología de redes comerciales:

- **Plazos de adquisición gubernamental**: las fuerzas del orden y las agencias de inteligencia pueden seguir usando durante años equipos de vigilancia 4G existentes después del despliegue de 5G
- **Análisis de coste y beneficio**: muchas operaciones de vigilancia logran sus objetivos con una interceptación 4G/LTE más barata, lo que reduce el incentivo para actualizar a sistemas 5G
- **Requisitos de formación y experiencia**: operar equipos de vigilancia 5G requiere conocimientos especializados que las organizaciones pueden tardar en desarrollar

### Limitaciones de Rayhunter en entornos 5G reales

#### Puntos ciegos de la vigilancia 5G nativa
*Esta es la limitación principal de Rayhunter.* **Rayhunter no puede detectar operaciones nativas de captadores IMSI 5G** que no dependan de ataques de bajada:

- **Redes 5G autónomas (SA)**: si los dispositivos se conectan a redes exclusivamente 5G sin volver a 4G, **Rayhunter** no puede supervisar esas comunicaciones
- **Equipos avanzados de vigilancia 5G**: actores sofisticados con tecnología avanzada podrían interceptar comunicaciones 5G sin activar las heurísticas de detección de **Rayhunter**
- **Explotación de la segmentación de red**: las capacidades de segmentación de red 5G podrían usarse para vigilar de formas que **Rayhunter** no detecta

#### Funciones de seguridad 5G mejoradas
Las redes 5G incorporan **medidas de seguridad mejoradas** que pueden reducir la eficacia de las técnicas de vigilancia tradicionales:

- **Protocolos de cifrado más sólidos**: 5G implementa normas de cifrado más robustas y difíciles de descifrar que las generaciones anteriores
- **Procedimientos de autenticación mejorados**: la autenticación más sólida de dispositivos en redes 5G puede dificultar la recopilación de IMSI
- **Supervisión de seguridad de red**: la infraestructura 5G incluye mejores capacidades de detección de intrusiones que pueden identificar y contrarrestar intentos de vigilancia

#### Cambios en el comportamiento de los dispositivos
A medida que se extienda el 5G, **el comportamiento de los dispositivos móviles puede evolucionar** de formas que afectan a la detección de **Rayhunter**:

- **Menor disposición a cambiar a una red anterior**: futuras actualizaciones de software podrían resistir mejor los ataques de bajada a medida que mejore la cobertura 5G
- **Preferencia por conectividad 5G**: los dispositivos pueden priorizar cada vez más las conexiones 5G y desconfiar de las solicitudes para usar protocolos de red antiguos
- **Mayor conciencia de seguridad**: los sistemas operativos móviles pueden implementar una detección mejor de comportamientos sospechosos de red

### Consideraciones estratégicas para desplegar Rayhunter

#### Recomendaciones de despliegue actuales
Para los despliegues inmediatos y a corto plazo, **Rayhunter** ofrece **capacidades completas de detección de vigilancia**:

- **Despliegues urbanos**: incluso en grandes ciudades con amplia cobertura 5G, **Rayhunter** detecta intentos de vigilancia dirigidos a redes 4G/LTE
- **Protección de eventos críticos**: en protestas, reuniones delicadas o actividades de alto riesgo, **Rayhunter** ofrece capacidades esenciales de detección, haya cobertura 5G o no
- **Seguridad durante los viajes**: **Rayhunter** sigue siendo muy eficaz para detectar vigilancia durante viajes nacionales e internacionales
#### Estrategias para prepararse para el futuro
Las organizaciones y las personas que planifiquen la detección de vigilancia a largo plazo deberían considerar:

- **Enfoques de detección híbridos**: combinar **Rayhunter** con otras herramientas de seguridad y técnicas de supervisión ofrece una cobertura completa de varios vectores de amenazas
- **Actualizaciones periódicas de la evaluación de amenazas**: vigilar la evolución de la tecnología de vigilancia ayuda a decidir cuándo complementar o sustituir las capacidades de **Rayhunter**
- **Apoyo al desarrollo de la comunidad**: apoyar el desarrollo de código abierto de **Rayhunter** aumenta las posibilidades de que se añadan capacidades de detección 5G en futuras versiones

#### Seguimiento de la evolución tecnológica
La comunidad de **Rayhunter** y la EFF siguen investigando **capacidades para detectar vigilancia 5G**:

- **Investigación sobre análisis de protocolos**: la investigación continua de los protocolos 5G puede identificar nuevas oportunidades de detección para futuras versiones de **Rayhunter**
- **Estudios de compatibilidad de hardware**: evaluar si se pueden mejorar los dispositivos actuales compatibles con **Rayhunter** para detectar intentos de vigilancia 5G
- **Seguimiento del panorama de amenazas**: seguir el desarrollo y despliegue de equipos de vigilancia compatibles con 5G ayuda a definir las prioridades futuras de desarrollo de **Rayhunter**

**Rayhunter** sigue siendo una **herramienta esencial para detectar vigilancia** en el panorama actual de las telecomunicaciones. Se espera que continúe siendo pertinente durante varios años mientras avanza gradualmente el despliegue de 5G y los actores de amenazas siguen recurriendo a métodos probados de ataque de bajada.

### Volver a analizar grabaciones

**Rayhunter** mejora continuamente sus capacidades de detección. Puedes volver a analizar grabaciones antiguas con las heurísticas actualizadas: haz clic en «N warnings» en la interfaz web y selecciona «re-analyze».

### Análisis en un ordenador

Para usuarios avanzados, **Rayhunter** incluye `rayhunter-check`, una herramienta CLI para analizar archivos PCAP y QMDL en ordenadores:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Modo de depuración
```

## Dispositivos compatibles

**Rayhunter** es compatible con varios puntos de acceso móviles con módems Qualcomm que exponen la interfaz `/dev/diag`.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Compatibilidad de dispositivos Rayhunter por región" caption="Compatibilidad de dispositivos y recomendaciones regionales para instalar Rayhunter" >}}

### Dispositivos recomendados

Estos dispositivos se han probado exhaustivamente y se usan ampliamente en la comunidad de **Rayhunter**:

#### Orbic RC400L (a veces comercializado como Kajeet RC400L)
- **Región recomendada**: América
- **Bandas compatibles**:
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Global y roaming: n257/n78
- **Disponibilidad**: **[Nuevo Orbic RC400L con Rayhunter](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** y **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**. Hay dispositivos compatibles.
- **Rango de precios**: STS Collective ofrece modelos profesionales

#### TP-Link M7350
- **Región recomendada**: África, Europa y Oriente Medio (también funciona en América, pero suele ser más caro)
- **Requisitos especiales**: se necesita una tarjeta SD formateada en FAT para grabaciones
- **Disponibilidad**: **[TP-Link M7350 con Rayhunter](https://stscollective.com/collections/rayhunter)**. Hay modelos compatibles verificados.

### Dispositivos funcionales

Se ha confirmado que **Rayhunter** también funciona en estos dispositivos:

- **Wingtech CT2MHS01** (América) - **[Rayhunter a la venta](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (América) - **[Rayhunter a la venta](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (África, Europa y Oriente Medio) - **[Rayhunter a la venta](https://stscollective.com)**
- **PinePhone y PinePhone Pro** (global) - **[Rayhunter a la venta](https://stscollective.com)**
- **FY UZ801** (Asia y Europa) - **[Rayhunter a la venta](https://stscollective.com)**
- **Punto de acceso Moxee** (América) - **[Moxee K779HSDL Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Notas de instalación por dispositivo

#### Orbic/Kajeet RC400L
El Orbic RC400L es el dispositivo original para el que se desarrolló **Rayhunter**. STS Collective lo ofrece **[con Rayhunter](https://stscollective.com)**.

**Métodos de instalación**:
- **Por red**: `./installer orbic` (recomendado, funciona por WiFi)
- **Por USB**: `./installer orbic-usb` (proporciona acceso a ADB y al intérprete de comandos root)

**Contraseñas predeterminadas**:
- **Verizon RC400L**: la contraseña de administrador siempre coincide con la contraseña WiFi (se encuentra en el menú del dispositivo)
- **Kajeet/Smartspot RC400L**: `$m@rt$p0tc0nf!g`
- **Dispositivos Moxee**: la contraseña tiene el formato `12$XXX`, donde XXX son los 3 últimos dígitos de la contraseña WiFi (consulta la contraseña WiFi bajo la batería)

**Acceso al intérprete**: después de la instalación, usa `./installer util orbic-shell`.

#### TP-Link M7350/M7310
Estos dispositivos funcionan de forma fiable con **Rayhunter** y están disponibles **[con Rayhunter](https://stscollective.com)**.

**Instalación**: `./installer tplink` (no requiere contraseña de administrador)
**Almacenamiento**: inserta una tarjeta SD formateada en FAT antes de la instalación
**Acceso al intérprete**: `./installer util tplink-shell`

#### Dispositivos especializados

**PinePhone y PinePhone Pro**: compatibilidad global, disponibles **[con Rayhunter](https://stscollective.com)**
**UZ801**: popular en regiones de Asia y Europa, disponible **[con Rayhunter](https://stscollective.com)**
**Wingtech CT2MHS01**: dispositivo orientado a América, disponible **[con Rayhunter](https://stscollective.com)**

### Añadir dispositivos nuevos

**Rayhunter** podría ser compatible con cualquier dispositivo que tenga un módem Qualcomm que exponga `/dev/diag`. Si quieres que **Rayhunter** sea compatible con tu dispositivo, inicia un debate en el repositorio oficial de GitHub.

## Documentación de la API REST

**Rayhunter** ofrece una API REST completa para acceder mediante programación al estado, las grabaciones y la configuración del dispositivo. La API permite integrarlo con otras herramientas de seguridad y sistemas de supervisión automatizada.

### Documentación oficial de la API

Para consultar la referencia completa de la API, incluidas las especificaciones detalladas de los puntos de acceso, ejemplos de solicitudes y respuestas y métodos de autenticación, visita la **[documentación oficial de la API REST de Rayhunter](https://efforg.github.io/rayhunter/api-docs/)**.

### Puntos de acceso de la API

La API de **Rayhunter** está disponible en `http://[device-ip]:8080/api/` y ofrece puntos de acceso para:

- **Estado del sistema**: supervisar el estado del dispositivo y el funcionamiento de **Rayhunter**
- **Gestión de grabaciones**: iniciar, detener y descargar grabaciones
- **Obtención de alertas**: acceder a alertas de detección y resultados del análisis
- **Configuración**: actualizar mediante programación los ajustes de **Rayhunter**
- **Control de heurísticas**: activar o desactivar algoritmos de detección concretos
- **Información del dispositivo**: obtener especificaciones y capacidades del dispositivo
- **Supervisión de red**: acceder a datos de la red celular en tiempo real
- **Registro de eventos**: consultar eventos de detección y alertas anteriores

### Autenticación

El acceso a la API usa la misma autenticación que la interfaz web. Asegúrate de que el dispositivo **Rayhunter** esté protegido correctamente y solo sea accesible para usuarios autorizados.

### Ejemplos de integración

La API REST de **Rayhunter** puede integrarse con varias plataformas de supervisión de seguridad, sistemas SIEM y herramientas de automatización personalizadas. Consulta la **[documentación oficial de la API](https://efforg.github.io/rayhunter/api-docs/)** para ver ejemplos completos de implementación y buenas prácticas.

## Solución de problemas

### Problemas habituales de instalación

**Problemas de conexión USB**: prueba otros cables o puertos USB. Las conexiones USB defectuosas suelen provocar fallos de instalación. *Es la causa más habitual de instalaciones fallidas.*

**Problemas de seguridad en macOS**: si aparece «No Orbic device found», cambia temporalmente a «Always» la opción «Allow accessories to connect» en los ajustes de seguridad.

**Detección del dispositivo**: después de la instalación, activa la heurística de prueba para verificar que **Rayhunter** funciona correctamente.

### Obtener ayuda

Para recibir ayuda con la instalación y la resolución de problemas:
- Consulta la documentación oficial de **Rayhunter**
- Usa `./installer --help` y `./installer util --help` para ver las opciones de los comandos
- Únete a los debates de GitHub para recibir apoyo de la comunidad
- Contacta con **[STS Collective](https://stscollective.com)** si tienes dudas sobre la compatibilidad del dispositivo

## Preguntas frecuentes (FAQ)

### Preguntas generales

#### ¿Qué es exactamente un captador de IMSI y cómo funciona?
Un captador de IMSI (también llamado StingRay, simulador de estación celular o torre celular falsa) es un equipo de vigilancia que imita torres celulares legítimas para interceptar comunicaciones de dispositivos móviles. Obliga a los dispositivos cercanos a conectarse al equipo malicioso en lugar de a torres legítimas, lo que permite a los operadores recopilar identificadores de dispositivos (números IMSI), datos de ubicación y metadatos de llamadas, y posiblemente interceptar comunicaciones. **Rayhunter** detecta estos dispositivos identificando patrones anormales en el comportamiento de la red celular.

#### ¿Puede Rayhunter detectar todos los tipos de equipos de vigilancia?
**Rayhunter** detecta específicamente captadores IMSI y simuladores de estaciones celulares que operan en redes 2G, 3G y 4G/LTE. No puede detectar otros tipos de vigilancia, como la supervisión WiFi, los dispositivos de seguimiento GPS, la vigilancia física o la vigilancia 5G nativa que no use ataques de bajada. **Rayhunter** es un componente de una estrategia integral de protección de la privacidad.

#### ¿Es legal usar Rayhunter?
En la mayoría de las jurisdicciones es completamente legal usar **Rayhunter**, ya que es una herramienta de supervisión pasiva que no interfiere con las redes celulares ni con otros dispositivos. Solo analiza las señales celulares que recibe el dispositivo de forma natural. Sin embargo, las leyes locales varían, por lo que los usuarios deberían comprobar la normativa de su zona. La EFF desarrolló **Rayhunter** como herramienta legítima de protección de la privacidad.

### Preguntas técnicas

#### ¿Por qué Rayhunter necesita una SIM si no requiere un plan activo?
La tarjeta SIM proporciona la identidad internacional de abonado móvil (IMSI) que el dispositivo necesita para autenticarse en las redes celulares y participar en los intercambios de protocolos que **Rayhunter** supervisa. Sin SIM, el dispositivo no puede conectarse a las redes celulares y **Rayhunter** no tendría actividad de red que analizar en busca de patrones sospechosos.

#### ¿Cuántos datos consume Rayhunter durante el funcionamiento normal?
**Rayhunter** usa pocos datos para la supervisión básica, ya que analiza principalmente información de protocolos celulares y no tráfico de Internet. Sin embargo, si activas notificaciones remotas mediante ntfy o usas el dispositivo como punto de acceso a la vez, el consumo de datos aumentará. La supervisión por sí sola consume un ancho de banda insignificante.

#### ¿Puedo usar Rayhunter mientras el dispositivo funciona como punto de acceso móvil?
Sí, **Rayhunter** puede funcionar simultáneamente mientras el dispositivo actúa como punto de acceso móvil. Se necesita un plan de servicio celular activo. La supervisión de **Rayhunter** funciona de forma independiente del punto de acceso, aunque usar ambas funciones a la vez consumirá más batería.

#### ¿Qué diferencia hay entre la instalación por WiFi y por USB?
El **método WiFi** (recomendado para la mayoría de los usuarios) instala **Rayhunter** mediante la interfaz inalámbrica del dispositivo y ofrece la funcionalidad estándar. El **método USB** habilita el acceso a Android Debug Bridge (ADB) para usuarios avanzados que necesiten depuración, pero es más complejo y no hace falta en instalaciones habituales.

### Preguntas sobre dispositivos y compatibilidad

#### ¿Por qué Rayhunter solo es compatible con algunos dispositivos?
**Rayhunter** requiere dispositivos con módems Qualcomm que expongan la interfaz `/dev/diag`, que proporciona acceso a información de protocolos celulares. La mayoría de los dispositivos de consumo no exponen esta interfaz por motivos de seguridad. Los dispositivos compatibles se han probado específicamente y se ha confirmado que cumplen los requisitos de **Rayhunter**.

#### ¿Puedo instalar Rayhunter en un teléfono inteligente normal?
No, **Rayhunter** no se puede instalar en teléfonos inteligentes normales. Necesita dispositivos especializados de punto de acceso móvil con determinados módems Qualcomm que expongan interfaces de diagnóstico. Entre los dispositivos compatibles están Orbic RC400L, TP-Link M7350 y varios otros modelos de puntos de acceso móviles.

#### ¿Qué ocurre si intento instalar Rayhunter en un dispositivo incompatible?
El instalador de **Rayhunter** detecta el dispositivo y normalmente se negará a instalarse en hardware incompatible. Intentar forzar la instalación en dispositivos no compatibles podría dañarlos o dejarlos inoperativos. Comprueba siempre la compatibilidad del dispositivo antes de intentar la instalación.

#### ¿Necesito dispositivos distintos para cada región?
Sí, las bandas de frecuencia celular varían según la región geográfica. El Orbic RC400L está optimizado para las redes de América, mientras que el TP-Link M7350 funciona bien en Europa, África y Oriente Medio. La información de compatibilidad de dispositivos **Rayhunter** incluye recomendaciones regionales para asegurar un rendimiento óptimo en tu ubicación.

### Preguntas sobre uso y configuración

#### ¿Cómo sé si mi dispositivo Rayhunter funciona correctamente?
Activa la heurística de prueba en los ajustes de configuración de **Rayhunter**. Esto generará alertas cada vez que el dispositivo detecte una torre celular y confirmará que el sistema funciona. La pantalla debería mostrar una línea verde durante el funcionamiento normal. Recuerda desactivar la heurística de prueba después de verificarlo, porque genera muchas alertas.

#### ¿Qué debo hacer si Rayhunter genera una alerta?
Cuando **Rayhunter** detecte actividad sospechosa, primero anota tu ubicación y las circunstancias. Pueden producirse falsos positivos debido a la optimización de la red o a problemas de los equipos. Si las alertas continúan en el mismo lugar o durante actividades delicadas, plantéate cambiar de ubicación y revisa los detalles en la interfaz web para comprender qué se detectó.

#### ¿Cada cuánto debería actualizar Rayhunter?
**Actualízalo mensualmente.** Consulta la página de versiones para ver nuevas heurísticas y mejoras de compatibilidad, que se añaden con frecuencia. La EFF mejora continuamente las capacidades de **Rayhunter** según evolucionan las técnicas de vigilancia. El proceso de actualización es igual al de la instalación inicial.

#### ¿Puede Rayhunter proteger a varias personas a la vez?
**Rayhunter** detecta captadores IMSI en la zona, por lo que puede proteger potencialmente a varias personas dentro del alcance (normalmente unos cientos de metros, según la intensidad de la señal). Sin embargo, cada persona que se tome en serio la detección de vigilancia debería considerar tener su propio dispositivo **Rayhunter** para obtener la máxima protección y control de configuración.

### Preguntas sobre seguridad y privacidad

#### ¿Usar Rayhunter me hace más visible para la vigilancia?
**Rayhunter** funciona de forma pasiva y no emite señales que permitan identificarlo a los equipos de vigilancia. Sin embargo, usar cualquier herramienta de seguridad indica preocupación por la privacidad. Las ventajas de la detección suelen superar los riesgos, especialmente para personas de alto riesgo como periodistas y activistas.

#### ¿Los equipos de vigilancia pueden detectar que uso Rayhunter?
**Rayhunter** es un sistema de supervisión pasiva que no transmite señales identificativas. Los operadores de vigilancia no pueden detectar el uso de **Rayhunter** a nivel de protocolo celular. La observación física del dispositivo o el análisis del tráfico de red podrían revelar su uso si están activadas las notificaciones remotas para **Rayhunter**.

#### ¿Qué información recopila Rayhunter sobre mí?
**Rayhunter** analiza información de protocolos celulares y almacena localmente las alertas de detección en el dispositivo. No recopila información personal, contenido de comunicaciones ni datos de ubicación más allá de lo que necesitan los algoritmos de detección. Todos los datos permanecen en el dispositivo salvo que actives las notificaciones remotas.

### Preguntas avanzadas

#### ¿Puedo analizar los datos de Rayhunter en mi ordenador?
Sí, **Rayhunter** incluye la herramienta de línea de comandos `rayhunter-check` para analizar archivos PCAP y QMDL grabados en ordenadores. Esto permite a los usuarios avanzados analizar en detalle los eventos detectados e investigar actividad sospechosa con todos los recursos del ordenador.

#### ¿Cómo funciona Rayhunter en zonas urbanas densas?
Las zonas urbanas densas tienen muchas torres celulares legítimas y pueden aumentar los falsos positivos porque hay más optimizaciones de red y cambios de torre. Los algoritmos de **Rayhunter** están diseñados para distinguir entre el comportamiento normal de la red y la vigilancia, pero los usuarios de zonas densas quizá tengan que ajustar la sensibilidad.

#### ¿Rayhunter funcionará durante un viaje internacional?
La eficacia de **Rayhunter** durante los viajes depende de la compatibilidad del dispositivo con las bandas celulares locales y los acuerdos de roaming. Los algoritmos de detección funcionan en todo el mundo, pero asegúrate de que el dispositivo admita las bandas de frecuencia que se usan en el país de destino. Quizá se necesite roaming internacional para disponer de toda la funcionalidad.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="Una persona revisa alertas de Rayhunter en un portátil mientras lleva un punto de acceso móvil en un entorno urbano con torres celulares cercanas" >}}

______

**Rayhunter** representa un avance crucial en la protección de la privacidad personal y la detección de vigilancia. Si flasheas y configuras correctamente **Rayhunter** en dispositivos compatibles, obtendrás capacidades eficaces para detectar captadores IMSI y proteger tus comunicaciones móviles de la vigilancia no autorizada.

Tanto si eres periodista, activista, profesional de seguridad o una persona preocupada por la privacidad, **Rayhunter** proporciona las herramientas necesarias para mantener la seguridad móvil en un mundo cada vez más vigilado. Para ver dispositivos compatibles verificados, consulta las opciones **[de Rayhunter a la venta](https://stscollective.com)** de proveedores de confianza de equipos de seguridad.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra dispositivos Rayhunter y ahorra un 20 %
{{< /centerbutton >}}

## Referencias

- [Repositorio oficial de Rayhunter en GitHub](https://github.com/EFForg/rayhunter)
- [Última versión de Rayhunter](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, proveedor de equipos Rayhunter](https://stscollective.com)
