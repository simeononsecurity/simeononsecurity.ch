---
title: "Construye un laboratorio doméstico en 10 niveles, de Pi-hole a la IA local"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Construye un laboratorio doméstico en diez etapas prácticas, desde el filtrado DNS de toda la red hasta la IA local, con hardware, costos, habilidades y compromisos para cada nivel."
genre: ["Laboratorio doméstico", "Autoalojamiento", "IA local", "Redes domésticas"]
tags: ["laboratorio doméstico", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "IA local", "consumo eléctrico"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Un laboratorio doméstico crece desde una Raspberry Pi y un router pequeños hasta almacenamiento, servidores, equipos de red y una estación de trabajo para IA local."
coverCaption: ""
---

Construye un laboratorio doméstico en 10 niveles, de Pi-hole a la IA local
=========================================================================

Un **laboratorio doméstico** es un conjunto de computadoras y servicios que ejecutas para resolver problemas cotidianos y aprender a operar sistemas reales. Puedes bloquear anuncios, automatizar luces, almacenar medios familiares o probar máquinas virtuales. **Empieza con una tarea útil.** Añade hardware cuando aparezca una limitación real.

Esta guía avanza desde una Raspberry Pi pequeña con Pi-hole hasta un servidor que ejecuta modelos de IA locales. **Cada nivel añade una capacidad y una nueva responsabilidad.** Las estimaciones de costos usan un consumo eléctrico ilustrativo y una tarifa de ejemplo de $0.15 por kilovatio-hora. Comprueba tu tarifa local y mide tus equipos antes de comprar más.

## Nivel 1: Bloquea anuncios en toda tu red doméstica

Instala [Pi-hole](https://docs.pi-hole.net/) en una Raspberry Pi o en otra computadora Linux pequeña. Pi-hole actúa como un **sumidero DNS**. Cuando un dispositivo solicita la dirección de un dominio en una lista de bloqueo, Pi-hole no devuelve un destino útil. El navegador, el teléfono y la televisión inteligente usan el mismo filtro cuando el router o el servidor DHCP dirige los clientes a Pi-hole.

El **filtrado DNS** también funciona fuera de los navegadores, incluso con algunos anuncios en aplicaciones y televisiones conectadas. El contenido de las páginas queda fuera del filtro, así que pasan los anuncios servidos desde el mismo dominio que un sitio o una aplicación. A veces una lista de bloqueo impide que carguen un inicio de sesión, un video o un pago. Revisa el registro de consultas de Pi-hole, permite el dominio concreto cuando sea necesario y prepara un DNS alternativo para las interrupciones.

El consumo eléctrico es bajo. Para un dispositivo de 8 vatios funcionando todo el mes, la estimación es 8 W × 24 horas × 30 días ÷ 1.000 × $0.15 = **unos $0.86 al mes**. Mide toda la fuente de alimentación en el enchufe. Una segunda computadora, un disco USB o un adaptador ineficiente cambian el total.

**Aprenderás:** DNS, DHCP, listas de bloqueo y mantenimiento básico de Linux.

## Nivel 2: Automatiza dispositivos inteligentes localmente

Añade [Home Assistant](https://www.home-assistant.io/), que reúne dispositivos inteligentes compatibles y automatizaciones en un solo sistema. Programa que las luces se apaguen a la hora de dormir. Enciende un ventilador cuando un sensor de temperatura supera un valor establecido. Recibe una alerta cuando un detector de fugas detecta agua. **Estas pequeñas automatizaciones aportan valor inmediato.**

El **control local** mantiene muchas automatizaciones dentro de casa cuando falla un servicio externo o la conexión a Internet. El comportamiento depende del dispositivo. Algunos productos todavía requieren una cuenta del proveedor, un servicio en la nube o conexión a Internet para la configuración y las funciones remotas. Revisa los requisitos de la integración antes de comprar hardware.

**Haz copias de seguridad de Home Assistant** y guarda una copia fuera de su host. Documenta las integraciones y los pasos de recuperación. Una tarjeta SD o una mini PC averiada no debería borrar tu configuración.

**Aprenderás:** integraciones de dispositivos, activadores, condiciones y recuperación de copias de seguridad.

## Nivel 3: Ejecuta varios servicios en una mini PC

Una **mini PC empresarial usada** suele ofrecer memoria ampliable, almacenamiento reemplazable y puertos útiles a bajo precio. Una mini PC Intel N100 suele consumir menos y ocupa poco espacio. Intel describe el N100 como un procesador de cuatro núcleos y cuatro subprocesos, con TDP de 6 vatios y compatibilidad con hasta 16 GB de memoria. La clasificación del procesador no equivale al consumo de todo el sistema en el enchufe. Compara la computadora exacta, la memoria, el almacenamiento, la garantía y los puertos de red.

Instala Linux y usa [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) para ejecutar servicios independientes como **contenedores**. Un contenedor empaqueta una aplicación y sus dependencias, pero comparte el kernel del sistema operativo anfitrión. Por ejemplo, ejecuta un gestor de contraseñas como Vaultwarden, un proyecto mantenido por la comunidad, y un monitor de disponibilidad como Uptime Kuma. **Trata el gestor de contraseñas como un servicio sensible:** limita el acceso, usa autenticación sólida, aplica actualizaciones y guarda una copia cifrada.

**Los contenedores no reemplazan las actualizaciones ni las copias de seguridad.** Asigna una ubicación de almacenamiento a cada servicio y registra los pasos de recuperación. Una mini PC pequeña también tiene límites. Varias bases de datos, conversiones de medios o aplicaciones grandes agotan la memoria, el almacenamiento o el tiempo de CPU.

**Aprenderás:** administración de Linux, contenedores, volúmenes, actualizaciones y recuperación de servicios.

## Nivel 4: Crea una biblioteca multimedia doméstica

[Jellyfin](https://jellyfin.org/docs/) es un servidor multimedia de código abierto. [Plex](https://support.plex.tv/) ofrece un ecosistema de clientes pulido y funciones opcionales vinculadas a una cuenta. Ambos organizan bibliotecas personales y transmiten medios a clientes compatibles. **Elige según tus clientes**, el modelo de acceso remoto, la compatibilidad del hardware y las funciones que necesitas.

**Tus necesidades de almacenamiento** dependen del tamaño y la calidad de tu colección. Empieza con un solo disco únicamente si ya tienes un plan de copia de seguridad independiente. Usa nombres de carpetas y metadatos coherentes para que el servidor identifique correctamente películas y episodios.

La **reproducción directa** envía un archivo compatible al cliente sin cambiar su flujo de video. La **transcodificación** convierte audio o video cuando el cliente, la conexión, los subtítulos o la calidad necesitan otro formato. La transcodificación aumenta la carga del servidor. Prueba tus dispositivos y la red antes de comprar una GPU o una CPU más potente. **Prescinde de un servidor multimedia dedicado** si todos los clientes reproducen tus archivos directamente y un host cubre tus necesidades.

**Aprenderás:** formatos multimedia, planificación del almacenamiento, rendimiento de red y pruebas de carga.

## Nivel 5: Añade redundancia de almacenamiento y una copia de seguridad separada

Un NAS de dos discos con **almacenamiento en espejo** escribe datos en ambas unidades. Si una unidad falla, la otra conserva una copia actual mientras reemplazas el disco averiado y reconstruyes el espejo. El espejo protege la disponibilidad ante el fallo de un disco. **Un espejo no restaura** un archivo eliminado, revierte el cifrado de ransomware ni protege contra robo, incendio o una falla eléctrica que dañe ambas unidades.

Guarda una **copia de seguridad separada** en otro dispositivo o ubicación. Incluye documentos importantes, fotos, exportaciones de configuración y datos de servicios. Programa las copias y conserva versiones para que los cambios accidentales no sobrescriban todas las copias correctas.

**Prueba una restauración.** Elige algunos archivos, restáuralos en otra carpeta y ábrelos. Para un servicio, restaura sus datos en una instancia de prueba o documenta los pasos y verifica cada archivo. Una copia de seguridad que nunca has restaurado es una suposición, no un plan de recuperación.

**Aprenderás:** sistemas de archivos, reemplazo de discos, rotación de copias de seguridad y pruebas de restauración.

## Nivel 6: Aprende virtualización con un clúster Proxmox pequeño

[Proxmox VE](https://pve.proxmox.com/pve-docs/) ejecuta máquinas virtuales y contenedores en hardware de servidor. Varios mini PC unidos en un **clúster** comparten una vista de administración y permiten aprender sobre nodos, almacenamiento y migración. Un clúster es un grupo de servidores configurados para coordinarse. Sus miembros no combinan la memoria en una sola reserva grande. **La alta disponibilidad requiere** planificación adicional y almacenamiento compartido o replicado adecuado.

Una **instantánea** registra el estado de una máquina virtual en un momento determinado y permite volver a un estado anterior tras un cambio en el laboratorio. Las instantáneas suelen depender del almacenamiento original. No son copias de seguridad independientes. **Copia los datos importantes en un destino de respaldo separado** y prueba la restauración.

Cada nodo añade consumo eléctrico, puertos de red, cables y actualizaciones. Tres computadoras pequeñas también implican tres sistemas que mantener y solucionar. Una sola mini PC con unas máquinas virtuales enseña muchos de los mismos conceptos básicos a menor costo. **Añade nodos cuando** los experimentos necesiten aislamiento o quieras practicar operaciones de clúster.

**Aprenderás:** máquinas virtuales, grupos de almacenamiento, instantáneas, pertenencia al clúster y mantenimiento de nodos.

## Nivel 7: Añade acceso remoto privado y separación de redes

[Tailscale](https://tailscale.com/kb/) conecta tus dispositivos aprobados mediante una red privada para acceder a algunos servicios domésticos cuando estás fuera. **Limita el acceso** a los dispositivos y servicios que necesita cada persona. Protege las cuentas con autenticación multifactor y revisa dispositivos y claves antiguos.

Un switch o router administrado con compatibilidad con **VLAN** separa grupos de dispositivos. Pon los enchufes inteligentes y otros dispositivos de baja confianza en una red distinta de las computadoras que guardan archivos personales. Coloca el almacenamiento en una red a la que solo lleguen los sistemas que lo necesiten. La segmentación limita la comunicación entre dispositivos. Mantén también las actualizaciones, las contraseñas seguras y las reglas de acceso.

**Evita exponer directamente los paneles de administración a Internet público** salvo que entiendas los requisitos de autenticación, parches y firewall del servicio. Una herramienta de acceso privado también requiere controlar bien las cuentas y los dispositivos.

**Aprenderás:** acceso privado, permisos basados en identidad, VLAN, reglas de firewall y límites de confianza de dispositivos.

## Nivel 8: Añade un servidor empresarial

Pasa a un servidor más grande cuando las mediciones confirmen que necesitas más núcleos de CPU, memoria, bahías de unidades, ranuras PCIe o capacidad de red. Los servidores empresariales antiguos suelen costar menos de segunda mano, pero sus ventiladores hacen ruido y el **consumo en reposo ronda los 100–160 vatios**, según el modelo y los componentes instalados. Trata este rango como una estimación, no como una especificación.

Calcula el gasto anual estimado de electricidad antes de comprar:

`vatios medidos ÷ 1.000 × 24 × 365 × tarifa eléctrica por kWh`

A 120 vatios y $0.15 por kWh, la estimación es de 1.051 kWh al año, o unos **$158 al año**. Mide el servidor exacto en reposo y con tu carga habitual. Añade el consumo de discos, refrigeración y UPS.

Comprueba la profundidad del chasis, la compatibilidad de discos, el ruido, el control de ventiladores, la fuente de alimentación y las tarjetas de expansión. Un servidor que supera tu presupuesto de espacio o electricidad no es una mejora práctica.

**Aprenderás:** hardware de servidor, administración remota, expansión, refrigeración y estimación de costos operativos.

## Nivel 9: Mide la energía y ajusta el tamaño del laboratorio

Usa un **medidor de energía enchufable** para medir cada computadora en reposo y durante el trabajo normal. Haz una lista de los mayores consumidores. Revisa los ajustes de energía del BIOS, quita tarjetas y discos que no uses y devuelve los servicios cotidianos a mini PC eficientes cuando no necesites hardware empresarial.

Ejecuta el servidor grande solo cuando una carga necesite su capacidad. Si usas un horario de Wake-on-LAN o control remoto de energía, documenta los pasos de recuperación ante fallas de red o electricidad. Mantén una **lista de dependencias de los servicios** para que los apagados no interrumpan el almacenamiento o la red que necesitan otros sistemas.

Un rack ayuda a organizar equipos y flujo de aire cuando el hardware para rack justifica el espacio. Un UPS cubre cortes breves y da tiempo para apagar los sistemas de forma ordenada. Ambos añaden costo de compra, espacio y consumo eléctrico. **Mide su consumo** e incluye el reemplazo de baterías en el presupuesto a largo plazo.

**Aprenderás:** medición de energía, administración eléctrica, mapeo de dependencias y planificación de capacidad.

## Nivel 10: Ejecuta modelos de IA localmente

[Ollama](https://docs.ollama.com/) descarga y ejecuta modelos de lenguaje compatibles en tu computadora. La **inferencia local** mantiene las solicitudes y respuestas en hardware bajo tu control cuando usas un modelo y una aplicación locales. Confirma que toda la ruta del software permanezca local. Una aplicación conectada, una función de telemetría o una opción de modelo en la nube envía datos fuera de tu red.

Los requisitos de hardware dependen del tamaño del modelo, la cuantización, la longitud del contexto y la velocidad deseada. **La memoria del sistema o de la GPU debe contener** los pesos del modelo y el contexto de trabajo. Las computadoras pequeñas ejecutan modelos pequeños, mientras que los modelos grandes y los contextos extensos necesitan más memoria y a menudo una GPU capaz. Mide la energía durante la inferencia. Un sistema con GPU suele consumir mucha más electricidad que una mini PC en reposo.

Los modelos locales sirven para redactar, resumir notas privadas y clasificar de forma sencilla cuando su calidad cumple tus necesidades. Producen respuestas incorrectas y los modelos pequeños suelen tener dificultades con el razonamiento complejo o los datos actuales. Los modelos en la nube a veces funcionan mejor en tareas específicas. **Compara calidad, privacidad, latencia, costo y consumo eléctrico** antes de decidir dónde ejecutar una carga de trabajo.

**Aprenderás:** memoria de modelos, cuantización, inferencia, límites de privacidad y evaluación de cargas de trabajo.

## Compara los diez niveles

**Los costos son estimaciones, no cotizaciones.** Los precios del hardware varían por región, estado y configuración del almacenamiento. Estima la electricidad con `vatios ÷ 1.000 × horas × días × tarifa por kWh`. Mide en el enchufe cuando sea posible e incluye las horas en reposo, porque muchos servidores domésticos funcionan todo el día.

### Capacidades y hardware

| Nivel | Nueva capacidad | Hardware habitual |
|---|---|---|
| **1** | Filtrado DNS de red | Raspberry Pi o host Linux pequeño |
| **2** | Automatización local de dispositivos | Pi o mini PC, dispositivos compatibles |
| **3** | Varias aplicaciones autoalojadas | Mini PC empresarial usado o sistema N100 |
| **4** | Transmisión de medios personales | Mini PC más almacenamiento multimedia |
| **5** | Tolerancia a fallos de disco y recuperación | NAS de dos discos más copia de seguridad separada |
| **6** | Laboratorio de servidores virtuales | Dos o más mini PC |
| **7** | Acceso privado y segmentación | Tailscale, router o switch administrado |
| **8** | Gran capacidad y expansión | Servidor empresarial |
| **9** | Menor consumo eléctrico del laboratorio | Medidor de energía, sistemas ajustados |
| **10** | Inferencia local de modelos | PC con mucha memoria, GPU opcional |

### Habilidades, costos y compromisos

| Nivel | Habilidades aprendidas | Estimación de costo recurrente | Principal compromiso |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Unos $1 al mes a 8 W y $0.15/kWh | Quedan algunos anuncios y hay que revisar falsos bloqueos |
| **2** | Integraciones, activadores, copias de seguridad | Electricidad del host y costo de dispositivos | Compatibilidad y trabajo de respaldo |
| **3** | Docker, actualizaciones, almacenamiento | Depende del consumo medido del sistema | Límites de CPU, memoria y disco |
| **4** | Formatos, organización, transcodificación | Almacenamiento y electricidad del servidor | La transcodificación a veces requiere más hardware |
| **5** | Espejo, retención, restauración | Electricidad del NAS, discos y destino de respaldo | Un espejo no es una copia de seguridad |
| **6** | Proxmox, VM, clústeres | Cada nodo aumenta consumo y mantenimiento | Más nodos implican más mantenimiento |
| **7** | Reglas de acceso, VLAN, firewall | Equipos de red y costo de servicios | Una regla mal configurada expone servicios |
| **8** | Hardware, refrigeración, administración remota | Varía por servidor, calcula con consumo medido | Ruido, calor y consumo en reposo |
| **9** | Medición, programación, ajuste de tamaño | Costo único del medidor, ahorro variable | Programar añade tareas operativas |
| **10** | Implementación y evaluación de modelos | Energía de cálculo y almacenamiento | Calidad y velocidad dependen del hardware |

## Elige la siguiente mejora útil

**Detente en el nivel que cubre tus necesidades actuales.** Pi-hole y una mini PC pueden cubrir tus servicios. Un NAS es útil cuando necesitas almacenamiento compartido y un plan de recuperación probado. Añade un clúster o un servidor empresarial cuando lo justifique una carga de trabajo o un objetivo de aprendizaje.

Anota **dónde están los datos de cada servicio, cómo se actualiza y cómo se restaura.** Prueba las copias de seguridad antes de añadir más equipos. Deja que la siguiente limitación real guíe tu próxima compra.

## Referencias

- [Documentación de Pi-hole](https://docs.pi-hole.net/)
- [Documentación de Home Assistant](https://www.home-assistant.io/docs/)
- [Especificaciones del procesador Intel N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker: ¿Qué es un contenedor?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Documentación de Jellyfin](https://jellyfin.org/docs/)
- [Soporte de Plex](https://support.plex.tv/)
- [Documentación de Proxmox VE](https://pve.proxmox.com/pve-docs/)
- [Documentación de Tailscale](https://tailscale.com/kb/)
- [Documentación de Ollama](https://docs.ollama.com/)
