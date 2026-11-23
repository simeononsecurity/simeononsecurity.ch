---
title: "Tailscale frente a Headscale"
date: 2026-05-24
lastmod: 2026-11-23
toc: true
draft: false
description: "Compara Tailscale y Headscale por su modelo de alojamiento, gestión de identidades, funciones, costes, operación y soporte para elegir una VPN en malla con WireGuard que se ajuste a tus necesidades."
genre: ["VPN", "Seguridad de redes", "Alojamiento propio", "WireGuard", "Confianza cero", "Redes en malla", "Código abierto", "Infraestructura en la nube", "Acceso remoto", "Gestión de redes"]
tags: ["tailscale frente a headscale", "headscale frente a tailscale", "vpn con alojamiento propio", "vpn con wireguard", "vpn en malla", "redes de confianza cero", "alternativa a tailscale", "configuración de headscale", "comparativa de vpn", "vpn de código abierto", "precios de tailscale", "funciones de headscale", "malla con wireguard", "red privada", "rendimiento de vpn", "funciones de tailscale", "instalación de headscale", "redes en malla", "acceso remoto seguro", "seguridad de vpn", "coordinación de redes", "tailnet", "despliegue de vpn", "vpn empresarial", "vpn para laboratorio doméstico", "redes con alojamiento propio", "coste de tailscale", "headscale con docker", "gestión de vpn", "servidor de coordinación de wireguard"]
cover: "/img/cover/tailscale-vs-headscale-comparison-guide.webp"
coverAlt: "Ilustración de una red en malla con dispositivos interconectados por líneas luminosas sobre un fondo oscuro. Los dispositivos aparecen como iconos estilizados de colores vivos que representan conexiones seguras."
coverCaption: ""
---

## Introducción

**Tailscale** y **Headscale** son servidores de coordinación para crear VPN seguras en malla basadas en [WireGuard](https://www.wireguard.com/). Tailscale es un servicio comercial alojado en la nube con un plan gratuito generoso. Headscale es una alternativa de código abierto y alojamiento propio que implementa el protocolo de control de Tailscale. Entender sus diferencias es fundamental para elegir la opción adecuada para las necesidades de red de tu organización.

La decisión principal es **quién controla el plano de control**. Elige Tailscale si das prioridad a la gestión de identidades, la administración y el soporte como servicios gestionados. Evalúa Headscale si el alojamiento propio y el control sobre los datos de coordinación justifican el trabajo operativo adicional. Las siguientes secciones comparan las funciones, el rendimiento, los costes, la seguridad y el mantenimiento.

______

## Conceptos básicos de las VPN en malla y WireGuard

Antes de comparar las dos opciones, conviene entender la tecnología que comparten.

### ¿Qué es WireGuard?

**WireGuard** es un protocolo VPN moderno de alto rendimiento con estas características:
- **Rendimiento excepcional:** Hasta 10 veces más rápido que OpenVPN
- **Superficie de ataque mínima:** Solo ~4,000 líneas de código (frente a más de 100,000 en OpenVPN)
- **Criptografía moderna:** Curve25519, ChaCha20, Poly1305
- **Integrado en el kernel de Linux:** Desde Linux 5.6 (2020)

### ¿Qué es una VPN en malla?

Una **VPN en malla** establece conexiones directas entre dispositivos y evita que todo el tráfico tenga que pasar por un servidor central:
- **Conexiones directas:** Los dispositivos se conectan directamente entre sí cuando es posible
- **Travesía de NAT:** Atraviesa automáticamente firewalls y NAT
- **Menor latencia:** Evita saltos innecesarios por servidores centrales
- **Mejor rendimiento:** Aprovecha todo el ancho de banda entre pares

### La función de los servidores de coordinación

WireGuard por sí solo es un protocolo. Para crear una VPN en malla, necesitas un **servidor de coordinación** (o plano de control) que cumpla estas funciones:
- Gestionar la autenticación y autorización de dispositivos
- Distribuir las claves de cifrado
- Facilitar la travesía de NAT y el descubrimiento de pares
- Gestionar las políticas de control de acceso
- Proporcionar resolución DNS dentro de la red

**Tailscale** y **Headscale** son servidores de coordinación que se encargan de estas tareas.

______

## Comparación general entre Tailscale y Headscale

| Aspecto | Tailscale | Headscale |
|--------|-----------|-----------|
| **Tipo** | SaaS comercial | Código abierto y alojamiento propio |
| **Licencia** | Propietaria (con plan gratuito) | Licencia BSD de 3 cláusulas |
| **Alojamiento** | En la nube (gestionado por Tailscale) | Propio (lo gestionas tú) |
| **Lanzamiento inicial** | 2019 | 2020 |
| **Responsable principal del mantenimiento** | Tailscale Inc. | Juan Font y la comunidad |
| **Estrellas en GitHub** | No aplica (código cerrado) | Más de 38.9 mil (en 2026) |
| **Complejidad de la configuración** | Muy baja (5 minutos) | Moderada (30-60 minutos) |
| **Coste mensual (100 usuarios)** | De $0 (gratuito) a $18 por usuario (empresarial) | Solo el alojamiento del servidor ($5-50 al mes) |
| **Compatibilidad de protocolo** | Protocolo de Tailscale | Protocolo de Tailscale (compatible) |

______

## Comparación detallada de funciones

### Funciones básicas de red

| Función | Tailscale | Headscale | Notas |
|---------|-----------|-----------|-------|
| **Malla basada en WireGuard** | ✅ Sí | ✅ Sí | Ambos usan WireGuard para todas las conexiones entre pares |
| **Travesía automática de NAT** | ✅ Sí | ✅ Sí | STUN/DERP para una conectividad fiable |
| **Enrutamiento de subredes** | ✅ Sí | ✅ Sí | Acceso a redes detrás de una puerta de enlace |
| **Nodos de salida** | ✅ Sí | ✅ Sí | Enruta todo el tráfico de Internet a través de un nodo |
| **MagicDNS** | ✅ Sí | ✅ Sí | Resolución de nombres dentro de la red en malla |
| **DNS dividido** | ✅ Sí | ✅ Sí | Configuración de DNS distinta para dominios específicos |
| **Enrutamiento de alta disponibilidad** | ✅ Sí | ✅ Sí | Conmutación automática entre rutas en caso de fallo |
| **Compatibilidad con IPv6** | ✅ Completa | ✅ Completa | Direccionamiento IPv6 completo en la malla |
| **Compatibilidad con multidifusión** | ❌ No | ❌ No | Actualmente, ninguno admite multidifusión |

### Control de acceso y seguridad

| Función | Tailscale | Headscale | Notas |
|---------|-----------|-----------|-------|
| **Motor de ACL** | ✅ Avanzado | ✅ Compatible | Headscale implementa la sintaxis de ACL de Tailscale |
| **Control de acceso por etiquetas** | ✅ Sí | ✅ Sí | Agrupa dispositivos mediante etiquetas |
| **Gestión de usuarios y grupos** | ✅ Sí | ✅ Sí | Headscale usa el concepto de «usuarios» |
| **OpenID Connect (OIDC)** | ✅ Sí | ✅ Sí | Autenticación con Google, Okta, Keycloak, etc. |
| **Autenticación SAML** | ✅ Sí (Enterprise) | ❌ No | Solo en Tailscale |
| **Tailnet Lock** | ✅ Sí | ❌ No | Impide el uso de servidores de coordinación no autorizados |
| **Comprobaciones de seguridad del dispositivo** | ✅ Sí (beta) | ❌ No | Comprueba que el dispositivo cumple los requisitos antes de darle acceso |
| **Acceso justo a tiempo** | ✅ Sí | ❌ No | Permisos elevados temporales |
| **Registro de auditoría** | ✅ Exhaustivo | ⚠️ Básico | Tailscale proporciona registros detallados |

### Gestión y administración

| Función | Tailscale | Headscale | Limitaciones |
|---------|-----------|-----------|-------------|
| **Interfaz web** | ✅ Oficial | ⚠️ Comunitaria | Headscale cuenta con varias interfaces creadas por la comunidad |
| **Gestión mediante CLI** | ✅ Sí | ✅ Sí | Ambos ofrecen herramientas de línea de comandos completas |
| **API REST** | ✅ Sí | ✅ Sí | Automatiza las tareas de gestión |
| **API gRPC** | ❌ No | ✅ Sí | Headscale ofrece gRPC para el control remoto |
| **Proveedor de Terraform** | ✅ Oficial | ❌ No | Integración con infraestructura como código |
| **Operador de Kubernetes** | ✅ Oficial | ⚠️ Comunitario | Operador comunitario para Headscale |
| **Aplicaciones móviles** | ✅ iOS, Android | ✅ Compatibles | Usa las aplicaciones de Tailscale con el servidor Headscale |
| **Consola de administración** | ✅ Completa | ❌ No | Headscale se gestiona mediante la CLI o la API |
| **Acceso para varios administradores** | ✅ Sí | ⚠️ Manual | Headscale requiere una implementación personalizada |

### Funciones avanzadas

| Función | Tailscale | Headscale | Notas |
|---------|-----------|-----------|-------|
| **Tailscale SSH** | ✅ Sí | ⚠️ Solo servidor | Los nodos de Headscale solo admiten el rol de servidor SSH |
| **Taildrop (intercambio de archivos)** | ✅ Sí | ⚠️ Incompleto | Compatibilidad limitada con Taildrop en Headscale |
| **Funnel (acceso público entrante)** | ✅ Sí | ❌ No | Expone servicios a la Internet pública |
| **Serve (uso compartido privado)** | ✅ Sí | ❌ No | Comparte servicios dentro de la tailnet |
| **Recopilación de servicios** | ✅ Sí | ❌ Limitada | Descubre servicios en la red |
| **Tailscale DERP** | ✅ Red global | ⚠️ Integrado | Headscale incluye DERP integrado y admite uno personalizado |
| **Servidores DERP personalizados** | ✅ Sí | ✅ Sí | Ambos admiten servidores de retransmisión personalizados |
| **Extensión de Docker** | ✅ Sí | ❌ No | Extensión de Tailscale para redes de contenedores en Docker |

______

## Comparación de precios (2026)

### Precios de Tailscale

| Plan | Coste mensual | Coste anual | Dispositivos | Funciones |
|------|-------------|-------------|---------|----------|
| **Personal** | $0 | $0 | Hasta 100 | 1 usuario, funciones básicas, soporte de la comunidad |
| **Personal Pro** | $6 por usuario al mes | $48 por usuario al año | Ilimitados | Varios usuarios, enrutamiento de subredes, ACL |
| **Team** | $10 por usuario al mes | $100 por usuario al año | Ilimitados | Consola de administración, registros de auditoría, SSO |
| **Business** | $15 por usuario al mes | $150 por usuario al año | Ilimitados | ACL avanzadas, grupos de usuarios, soporte prioritario |
| **Enterprise** | $18 o más por usuario al mes | Personalizado | Ilimitados | Tailnet Lock, SAML, soporte dedicado, SLA |

**Nota.** El plan Personal gratuito de Tailscale admite hasta 100 dispositivos para uso personal, un límite muy generoso para laboratorios domésticos y despliegues pequeños.

### Costes de Headscale

Headscale es **gratuito y de código abierto**, aunque debes cubrir los costes de infraestructura:

| Recurso | Intervalo de coste mensual | Notas |
|----------|-------------------|-------|
| **VPS pequeño** (1 CPU, 1GB de RAM) | $5-10 | Adecuado para <50 dispositivos |
| **VPS mediano** (2 CPU, 4GB de RAM) | $15-25 | Adecuado para 50-200 dispositivos |
| **VPS grande** (4 CPU, 8GB de RAM) | $40-80 | Adecuado para 200-1000 o más dispositivos |
| **Nombre de dominio** | $10-15 al año | Para certificados TLS |
| **Ancho de banda** | Suele estar incluido | Consulta los límites del proveedor de VPS |
| **Tiempo necesario** | Variable | Configuración, mantenimiento y actualizaciones |

**Coste total de propiedad (100 usuarios):**
- **Tailscale:** $0 (plan gratuito) o $1,000-1,800 al mes (planes de pago)
- **Headscale:** $15-30 al mes + 5-10 horas de configuración + 2-5 horas de mantenimiento al mes

**Punto de equilibrio.** Para organizaciones con más de 3-5 usuarios de pago, Headscale resulta rentable si valoras tu tiempo en menos de $50 por hora.

______

## Comparación de rendimiento

### Latencia y velocidad de transferencia

Tailscale y Headscale usan WireGuard en el plano de datos, por lo que **el rendimiento entre pares es idéntico**:

| Métrica | Tailscale | Headscale |
|--------|-----------|-----------|
| **Latencia adicional P2P** | <1ms | <1ms |
| **Velocidad de transferencia P2P** | Casi nativa (~900 Mbps en una conexión de 1 Gbps) | Casi nativa |
| **Velocidad de transferencia del tráfico retransmitido (DERP)** | 50-300 Mbps | 10-200 Mbps (depende de tu servidor) |
| **Latencia del tráfico retransmitido** | +10-50ms | +5-100ms (depende de la ubicación) |
| **Establecimiento de la conexión** | 100-500ms | 200-800ms |
| **Propagación de actualizaciones de políticas de ACL** | <5 segundos | <30 segundos |

**Diferencia principal.** Tailscale opera una red global de retransmisión DERP con servidores en todo el mundo, lo que mejora el rendimiento cuando fallan las conexiones directas. El DERP integrado de Headscale se ejecuta en tu servidor y puede añadir latencia si el servicio carece de distribución geográfica.

### Escalabilidad

| Aspecto | Tailscale | Headscale |
|--------|-----------|-----------|
| **Número máximo de nodos** | Más de 100,000 (probado) | ~5,000 (según la comunidad) |
| **Número recomendado de nodos** | Ilimitado | <1,000 para un solo servidor |
| **Solicitudes por minuto (RPM) del plano de control** | Muy optimizado | Depende de las especificaciones del servidor |
| **Memoria por nodo** | No aplica (servicio gestionado) | ~1-5 MB (en el servidor) |
| **Base de datos** | PostgreSQL (gestionada) | SQLite o PostgreSQL |

______

## Comparación de seguridad

### Seguridad de la infraestructura

| Aspecto | Tailscale | Headscale | Evaluación |
|--------|-----------|-----------|------------|
| **Confianza en el servidor de coordinación** | Debes confiar en Tailscale Inc. | Tú controlas el servidor | Headscale ofrece mayor privacidad |
| **Claves de cifrado** | Los dispositivos las generan y nunca se envían a Tailscale | Los dispositivos las generan y nunca se envían al servidor | ✅ Excelente en ambos casos |
| **Seguridad del plano de datos** | WireGuard (excelente) | WireGuard (excelente) | ✅ Excelente en ambos casos |
| **Seguridad del plano de control** | HTTPS + atestación | HTTPS + equivalente opcional de Tailnet Lock | ⚠️ Tailscale es ligeramente más robusto |
| **Trazabilidad de auditoría** | Registros exhaustivos | Registros básicos | ⚠️ Tailscale es superior |
| **Programa de recompensas por vulnerabilidades** | ✅ Sí | ❌ No | Tailscale ha remunerado a investigadores de seguridad |
| **Certificaciones de seguridad** | SOC 2 Type II | No aplica | Tailscale está preparado para empresas |

### Consideraciones de privacidad

| Aspecto de privacidad | Tailscale | Headscale |
|----------------|-----------|-----------|
| **Visibilidad de los metadatos** | Tailscale puede ver los nombres de dispositivos, las direcciones IP y los metadatos de conexión | Tú controlas todos los metadatos |
| **Visibilidad del tráfico** | ❌ No tiene visibilidad del tráfico (cifrado) | ❌ No tiene visibilidad del tráfico (cifrado) |
| **Requisitos de cumplimiento** | Sujeto a la jurisdicción de EE. UU. | Sujeto a la jurisdicción de tu servidor |
| **Residencia de los datos** | Infraestructura en la nube de Tailscale | El centro de datos que elijas |

**Veredicto.** Ambas soluciones ofrecen **un cifrado excelente y una arquitectura de conocimiento cero** para el tráfico en sí. Headscale ofrece mayor **privacidad** porque tú controlas todos los metadatos. Tailscale ofrece mayores **garantías de seguridad** mediante certificaciones, auditorías y recompensas por vulnerabilidades.

______

## Comparación de configuración y despliegue

### Configuración de Tailscale

**Tiempo necesario:** 5-10 minutos

1. **Crea una cuenta** en [tailscale.com](https://tailscale.com/)
2. **Instala el cliente** en cada dispositivo (con un comando o descargando la aplicación)
3. **Autentícate** mediante OAuth (Google, Microsoft, GitHub, etc.)
4. **Configura las ACL** (opcional, puedes hacerlo más adelante)
5. **¡Listo!** La red queda operativa de inmediato

**Ejemplo de instalación en Linux:**

> **Revisa el instalador antes de ejecutarlo.** Descárgalo en un archivo temporal, inspecciónalo y confirma la distribución del equipo y el origen del paquete. Tras la instalación, ejecuta `tailscale version` y `tailscale status` para verificar el resultado. Si la instalación falla, elimina el paquete con el gestor de paquetes de tu distribución y restaura el estado anterior de los paquetes desde una copia de seguridad del sistema.

```bash
curl -fsSL https://tailscale.com/install.sh -o /tmp/tailscale-install.sh
less /tmp/tailscale-install.sh
sh /tmp/tailscale-install.sh
sudo tailscale up
```

### Configuración de Headscale

**Tiempo necesario:** 30-90 minutos (la primera vez)

1. **Aprovisiona un servidor** (VPS con IP pública, se recomienda 1GB de RAM o más)
2. **Configura el DNS** (un registro A que apunte al servidor)
3. **Instala Headscale** (mediante un gestor de paquetes o Docker)
4. **Configura Headscale** (config.yaml con la URL del servidor, la base de datos, etc.)
5. **Configura los certificados TLS** (se recomienda Let's Encrypt)
6. **Inicia el servicio de Headscale**
7. **Crea usuarios** mediante la CLI con `headscale users create alice`
8. **Instala el cliente de Tailscale** en cada dispositivo
9. **Configura los clientes** para usar el servidor de coordinación personalizado
10. **Registra los nodos** mediante autenticación web o claves de preautenticación
11. **Configura las ACL** (archivo policy.json)

**Ejemplo de instalación de Headscale en Ubuntu:**
```bash
# Instalar Headscale
curl -fsSL https://pkgs.headscale.net/headscale_<VERSION>_linux_amd64.deb -o headscale.deb
sudo apt install ./headscale.deb

# Configurar Headscale
sudo nano /etc/headscale/config.yaml
# Establecer server_url en https://headscale.example.com

# Iniciar el servicio
sudo systemctl enable --now headscale

# Crear usuario
headscale users create myuser

# En el equipo cliente
sudo tailscale up --login-server=https://headscale.example.com
```

**Opción más fácil de configurar.** **Tailscale** es mucho más sencillo de configurar por primera vez.

______

## Complejidad operativa

### Gestión diaria

| Tarea | Tailscale | Headscale | Opción ganadora |
|------|-----------|-----------|--------|
| **Añadir un dispositivo** | Abrir el enlace y autenticarse | Generar una clave de autenticación o autenticarse por web | Tailscale (más fácil) |
| **Actualizar las ACL** | Editar en la interfaz web, con efecto inmediato | Editar el archivo y recargar la configuración | Tailscale (más fácil) |
| **Consultar el estado de la conectividad** | Panel web | CLI o interfaz de la comunidad | Tailscale (más fácil) |
| **Resolver problemas** | Registros detallados en el panel | Registros del servidor y del cliente | Tailscale (más fácil) |
| **Actualizar el software** | Automático | Actualizaciones manuales del servidor | Tailscale (más fácil) |
| **Hacer copias de seguridad de la configuración** | Automático | Manual (base de datos y configuración) | Tailscale (más fácil) |
| **Recuperarse de un desastre** | Automático | Restauración manual desde una copia de seguridad | Tailscale (más fácil) |

### Carga de mantenimiento

**Tailscale (servicio gestionado):**
- ✅ Sin mantenimiento de servidores
- ✅ Actualizaciones y parches de seguridad automáticos
- ✅ Redundancia y conmutación por error integradas
- ✅ Soporte profesional disponible
- ❌ Depende de la disponibilidad del servicio de Tailscale

**Headscale (alojamiento propio):**
- ⚠️ Actualizaciones y parches de seguridad del sistema operativo del servidor (cada mes)
- ⚠️ Actualizaciones de Headscale (cada 1-3 meses)
- ⚠️ Copias de seguridad de la base de datos (se recomienda hacerlas a diario)
- ⚠️ Renovación de certificados TLS (automatizada con Let's Encrypt)
- ⚠️ Configuración de la monitorización y las alertas
- ⚠️ Resolución de problemas cuando surjan
- ✅ Control total sobre la infraestructura
- ✅ Sin dependencia de servicios de terceros

**Tiempo mensual estimado:**
- **Tailscale:** 30 minutos (revisar políticas y añadir usuarios)
- **Headscale:** 2-5 horas (actualizaciones, monitorización y resolución de problemas)

______

## Recomendaciones según el caso de uso

### Elige Tailscale si:

✅ **Quieres configurar la red lo antes posible** - 5 minutos desde la creación de la cuenta hasta tener la red operativa\
✅ **Tienes <100 dispositivos** - El plan gratuito cubre el uso personal y el de pequeñas empresas\
✅ **Das prioridad a la facilidad de uso** - Interfaz web y experiencia de usuario entre las mejores de su categoría\
✅ **Necesitas funciones empresariales** - SSO, registros de auditoría, Tailnet Lock y comprobaciones de seguridad del dispositivo\
✅ **Valoras tu tiempo** - Sin carga de mantenimiento y con actualizaciones automáticas\
✅ **Necesitas disponibilidad garantizada** - El plan Enterprise de Tailscale ofrece un SLA del 99.99% de disponibilidad\
✅ **Quieres aplicaciones móviles oficiales** - Aplicaciones nativas para iOS y Android con todas las funciones\
✅ **Necesitas soporte profesional** - Los planes de pago incluyen soporte prioritario\
✅ **Te importa el cumplimiento normativo** - Certificación SOC 2 Type II\
✅ **Tu organización es una entidad comercial** - Precios sencillos por usuario, sin costes ocultos\

### Elige Headscale si:

✅ **Necesitas plena soberanía sobre los datos** - Todos los metadatos permanecen en tu infraestructura\
✅ **Tienes requisitos de privacidad o cumplimiento** - Los datos deben permanecer en determinadas jurisdicciones\
✅ **Tienes experiencia técnica** - Te manejas con la administración de sistemas Linux, Docker y la resolución de problemas\
✅ **Tienes >10 usuarios de pago** - El ahorro se vuelve considerable a medida que aumenta el número de usuarios\
✅ **Quieres aprender** - Es un buen proyecto para entender las VPN en malla\
✅ **Prefieres el código abierto** - Puedes auditar el código, aportar correcciones y personalizarlo\
✅ **Cuidas el presupuesto** - Costes recurrentes mínimos ($5-30 al mes por el servidor)\
✅ **Ya tienes infraestructura** - Puedes desplegarlo en tu infraestructura de Kubernetes o de máquinas virtuales\
✅ **Necesitas una API gRPC** - Headscale ofrece gRPC para automatización avanzada\
✅ **Ya alojas tus propios servicios** - Se integra en tu entorno de alojamiento propio\

### Enfoque híbrido con ambas soluciones

Algunas organizaciones usan **ambas soluciones**:

1. **Tailscale para producción** - Infraestructura crítica con SLA y soporte
2. **Headscale para desarrollo y pruebas** - Entornos de desarrollo rentables
3. **Tailscale para usuarios sin perfil técnico** - Incorporación sencilla del personal
4. **Headscale para equipos técnicos** - Personal de ingeniería con experiencia en alojamiento propio

______

## Escenarios de migración

### Migración de Tailscale a Headscale

**Motivación:** Reducir costes, lograr soberanía sobre los datos y tener más control

**Proceso:**
1. Despliega el servidor de Headscale y comprueba su funcionamiento
2. Prueba Headscale con un subconjunto de dispositivos no críticos
3. Exporta las ACL de Tailscale y adáptalas para Headscale
4. Migra gradualmente los dispositivos al servidor de coordinación de Headscale
5. Actualiza la configuración de DNS y las rutas de subred
6. Cancela la suscripción a Tailscale

**Dificultades:**
- No hay una herramienta de migración automatizada
- Debes volver a autenticar todos los dispositivos
- El funcionamiento de algunas funciones cambia (Funnel, Serve, Taildrop)
- La sintaxis de las ACL es compatible y requiere pruebas

**Tiempo necesario:** 5-20 horas, según la complejidad

### Migración de Headscale a Tailscale

**Motivación:** Reducir la carga operativa y obtener funciones empresariales y mejor soporte

**Proceso:**
1. Crea una cuenta de Tailscale y configura las ACL
2. Instala los clientes de Tailscale (puedes sustituir los existentes en el mismo dispositivo)
3. Migra los dispositivos ejecutando `tailscale up` sin especificar un servidor personalizado
4. Verifica la conectividad y los controles de acceso
5. Retira el servidor de Headscale

**Dificultades:**
- Debes volver a autenticar todos los dispositivos
- Algunos usuarios pueden necesitar cuentas de Tailscale (correo electrónico o SSO)
- Debes gestionar el cambio y comunicarlo a los usuarios

**Tiempo necesario:** 2-8 horas, según el tamaño del despliegue

______

## Comunidad y ecosistema

### Ecosistema de Tailscale

| Recurso | Disponibilidad |
|----------|--------------|
| **Documentación oficial** | ✅ Completa y bien mantenida |
| **Foro de la comunidad** | ✅ Foro activo con participación del personal de Tailscale |
| **Servidor de Discord** | ✅ Muy activo, con personal que responde a las consultas |
| **Incidencias en GitHub** | ❌ Código cerrado (comentarios a través del foro) |
| **Stack Overflow** | ✅ Etiqueta activa con más de 2,000 preguntas |
| **Tutoriales en YouTube** | ✅ Contenido oficial y de la comunidad |
| **Integraciones** | ✅ Docker, Kubernetes, Terraform, Synology, QNAP, etc. |

### Ecosistema de Headscale

| Recurso | Disponibilidad |
|----------|--------------|
| **Documentación oficial** | ✅ Buena, mantenida por la comunidad |
| **Foro de la comunidad** | ⚠️ GitHub Discussions cumple la función de foro |
| **Servidor de Discord** | ✅ Servidor activo de la comunidad |
| **Incidencias en GitHub** | ✅ Código abierto, seguimiento activo de incidencias (más de 38.9 mil estrellas) |
| **Stack Overflow** | ⚠️ Comunidad más pequeña (~100 preguntas) |
| **Tutoriales en YouTube** | ⚠️ Contenido creado por la comunidad |
| **Interfaces web** | ⚠️ Varias opciones de la comunidad (Headscale-UI, Headplane, ouroboros) |
| **Operador de Kubernetes** | ⚠️ Operador mantenido por la comunidad |

**Tamaño de la comunidad (2026):**
- **Tailscale:** Más de 100,000 miembros activos en la comunidad, con el respaldo de una empresa bien financiada
- **Headscale:** Más de 10,000 miembros activos en la comunidad, proyecto de código abierto

______

## Pruebas de rendimiento en condiciones reales (2026)

Resultados basados en pruebas de la comunidad y mediciones publicadas:

### Pruebas de velocidad de transferencia entre pares

| Escenario | Tailscale | Headscale | Referencia (sin VPN) |
|----------|-----------|-----------|-------------------|
| **LAN gigabit** | 940 Mbps | 940 Mbps | 945 Mbps |
| **WAN (100 Mbps)** | 98 Mbps | 98 Mbps | 100 Mbps |
| **WAN (fibra de 1 Gbps)** | 920 Mbps | 920 Mbps | 950 Mbps |
| **Entre continentes (DERP)** | 180 Mbps | 95 Mbps | No aplica |

**Análisis.** Las conexiones directas entre pares tienen el mismo rendimiento. Tailscale ofrece mayor velocidad en las conexiones retransmitidas gracias a su red global de servidores DERP.

### Pruebas de latencia

| Escenario | Tailscale | Headscale | Referencia |
|----------|-----------|-----------|----------|
| **Ping en la LAN** | 1.2ms | 1.2ms | 0.8ms |
| **WAN regional (100 millas)** | 15ms | 15ms | 12ms |
| **De un extremo a otro del país** | 48ms | 48ms | 45ms |
| **Entre continentes (conexión directa)** | 155ms | 155ms | 152ms |
| **Entre continentes (DERP)** | 185ms | 220ms | No aplica |

**Análisis.** Ambos añaden una latencia mínima (~1-2ms) a las conexiones directas. La latencia de DERP en Headscale varía según la ubicación del servidor.

### Uso de recursos

| Métrica | Cliente de Tailscale | Cliente de Headscale | Servidor de Headscale |
|--------|------------------|------------------|------------------|
| **Uso de RAM (en reposo)** | 80-120 MB | 80-120 MB | 50-200 MB (varía según el número de nodos) |
| **Uso de RAM (en actividad)** | 120-200 MB | 120-200 MB | 100-500 MB |
| **Uso de CPU (en reposo)** | <1% | <1% | <1% |
| **Uso de CPU (en actividad)** | 5-15% | 5-15% | 3-20% (depende del número de nodos) |
| **Uso de disco** | 100-500 MB | 100-500 MB | 100MB-2GB (base de datos) |

______

## Ejemplos de configuración avanzada

### Headscale con Docker Compose

```yaml
version: '3'
services:
  headscale:
    image: headscale/headscale:0.28.0
    container_name: headscale
    restart: unless-stopped
    ports:
      - "127.0.0.1:8080:8080"  # API/web
      - "443:443"              # HTTPS
      - "3478:3478/udp"        # STUN
    volumes:
      - ./config:/etc/headscale
      - ./data:/var/lib/headscale
    command: serve
    environment:
      - TZ=UTC
```

### Ejemplo de ACL de Headscale

```json
{
  "groups": {
    "group:admin": ["alice@", "bob@"],
    "group:developers": ["charlie@", "diana@"]
  },
  "hosts": {
    "production-db": "100.64.0.10/32",
    "staging-db": "100.64.0.20/32"
  },
  "acls": [
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["*:*"]
    },
    {
      "action": "accept",
      "src": ["group:developers"],
      "dst": ["staging-db:5432", "autogroup:self:*"]
    }
  ]
}
```

### Configuración del cliente de Tailscale con Headscale

```bash
# Linux
sudo tailscale up \
  --login-server=https://headscale.example.com \
  --accept-routes \
  --advertise-tags=tag:server

# Con una clave de preautenticación
headscale preauthkeys create --user engineering --expiration 1h

sudo tailscale up \
  --login-server=https://headscale.example.com \
  --authkey=<YOUR_AUTH_KEY>
```

______

## Solución de problemas habituales

### Problemas de Tailscale

| Problema | Solución |
|---------|----------|
| **No hay conexión con el servidor de coordinación** | Revisa el firewall y verifica la conexión a Internet |
| **Falla la conexión directa** | El cliente suele recurrir a DERP automáticamente. Revisa la configuración de NAT |
| **Latencia alta** | Comprueba que la conexión se haya establecido directamente, sin retransmisión |
| **Clave caducada** | Vuelve a autenticarte o desactiva la caducidad de claves en la consola de administración |
| **Una ACL bloquea el tráfico** | Revisa las reglas de ACL y prueba la configuración |

### Problemas de Headscale

| Problema | Solución |
|---------|----------|
| **Los nodos no se registran** | Comprueba que la URL de Headscale sea accesible y revisa el certificado TLS |
| **Falla la resolución DNS** | Comprueba que MagicDNS esté bien configurado en config.yaml |
| **La retransmisión DERP falla** | Comprueba que el puerto STUN (3478/udp) esté abierto y verifica la configuración de DERP |
| **Los nodos quedan desconectados después de reiniciar** | Comprueba que los clientes estén configurados para iniciarse al arrancar el sistema |
| **Los cambios en las ACL no se aplican** | Recarga Headscale con `systemctl reload headscale` |
| **Base de datos dañada** | Restaura desde una copia de seguridad y considera usar PostgreSQL en producción |

### Comandos de diagnóstico

```bash
# Diagnóstico de Tailscale
tailscale status
tailscale netcheck
tailscale ping <hostname>
tailscale debug derp

# Diagnóstico de Headscale
headscale nodes list
headscale nodes list-routes
headscale debug routes
journalctl -u headscale -f  # Ver registros
```

______

## Buenas prácticas de seguridad

### Para ambas soluciones

1. **Activa la caducidad de las claves** - Exige volver a autenticarse periódicamente
2. **Aplica el principio de mínimo privilegio** - Concede solo el acceso imprescindible en las ACL
3. **Etiqueta los nodos de infraestructura** - Separa los dispositivos de los usuarios de los servidores
4. **Activa la MFA** - Exige autenticación multifactor al iniciar sesión
5. **Supervisa los registros de acceso** - Revisa periódicamente los patrones de conexión
6. **Mantén los clientes actualizados** - Aplica los parches de seguridad cuanto antes

### Seguridad específica de Headscale

1. **Refuerza la seguridad del sistema operativo del servidor** - Sigue las guías de CIS y desactiva los servicios innecesarios
2. **Usa Let's Encrypt** - Automatiza la gestión de los certificados TLS
3. **Implementa fail2ban** - Bloquea los intentos de fuerza bruta
4. **Haz copias de seguridad periódicas** - Automatiza las copias de seguridad de la base de datos en una ubicación independiente
5. **Actualiza cuanto antes** - Sigue las nuevas versiones de Headscale para identificar los parches de seguridad
6. **Segmenta la red** - Aísla el servidor de Headscale en la VLAN de administración
7. **Activa el firewall** - Expón solo los puertos necesarios (443, 3478/udp)

______

## Planes de desarrollo

### Planes de Tailscale (2026)

Según las declaraciones públicas de Tailscale:
- ✅ **Disponible:** Aperture (puerta de enlace para la gobernanza de la IA), comprobaciones de seguridad del dispositivo mejoradas
- 🚧 **En desarrollo:** Detección avanzada de amenazas, compatibilidad con más plataformas
- 📋 **Previsto:** Modo exclusivo de IPv6, observabilidad mejorada, más integraciones

### Estado de Headscale (2026)

Según los hitos de GitHub y las conversaciones de la comunidad:
- ✅ **Añadido recientemente:** Autenticación OIDC, mejoras en DERP, mejor compatibilidad con ACL
- 🚧 **En desarrollo:** Mejoras en Taildrop, mejor integración con interfaces web
- 📋 **Solicitudes de la comunidad:** Equivalente de Funnel/Serve, registro avanzado, modo de alta disponibilidad

**Evaluación de madurez:**
- **Tailscale:** Apto para producción y para empresas, más de 5 años de desarrollo
- **Headscale:** Apto para producción en casos de uso básicos, en desarrollo activo e impulsado por la comunidad

______

## Conclusión

Tanto **Tailscale** como **Headscale** ofrecen funciones excelentes de VPN en malla con WireGuard. Cada solución se adapta a distintos públicos y casos de uso.

**Elige Tailscale si:**
- Valoras la sencillez y quieres empezar a trabajar en cuestión de minutos
- Formas parte de un equipo pequeño (<100 dispositivos) que se beneficia del generoso plan gratuito
- Necesitas funciones empresariales como SSO, registros de auditoría y soporte profesional
- Prefieres los servicios gestionados al alojamiento propio
- Las certificaciones de cumplimiento (SOC 2) son importantes para ti

**Elige Headscale si:**
- Necesitas un control total sobre tu infraestructura y tus metadatos
- Tienes experiencia técnica y te gusta alojar tus propios servicios
- Optimizar los costes es fundamental (>10 usuarios de pago = ahorro considerable)
- La soberanía de los datos y la privacidad son prioritarias
- Prefieres soluciones de código abierto que puedas auditar y personalizar

**Recomendaciones principales para 2026:**

1. **Startups y pymes.** Empieza con **el plan gratuito de Tailscale**. Es difícil de superar para 0-100 dispositivos.
2. **TI empresarial.** **Tailscale Enterprise** con SSO y soporte ofrece el mejor coste total de propiedad si tienes en cuenta el tiempo del personal.
3. **Usuarios que priorizan la privacidad.** **Headscale** ofrece el máximo control y privacidad.
4. **Usuarios con experiencia técnica y un laboratorio doméstico.** **Headscale** es una excelente oportunidad para aprender.
5. **Organizaciones con un enfoque híbrido.** Usa **Tailscale para producción** y **Headscale para desarrollo y pruebas**.

Elijas la opción que elijas, usarás WireGuard, una tecnología de primer nivel para redes seguras y modernas. La decisión depende de tus prioridades al sopesar **comodidad y control**, **servicio gestionado y alojamiento propio**, y **coste y funciones**.

Para la mayoría de las organizaciones en 2026, **el servicio gestionado de Tailscale** ofrece el mejor equilibrio entre funciones, facilidad de uso y relación calidad-precio. Para las organizaciones con requisitos específicos de soberanía, privacidad o coste, **Headscale ofrece una alternativa atractiva de alojamiento propio**.

______

## Referencias y recursos

1. [Sitio web oficial de Tailscale](https://tailscale.com/)
2. [Documentación de Tailscale](https://tailscale.com/kb/)
3. [Documentación oficial de Headscale](https://headscale.net/)
4. [Repositorio de Headscale en GitHub](https://github.com/juanfont/headscale)
5. [Sitio oficial de WireGuard](https://www.wireguard.com/)
6. [Blog de Tailscale - Cómo funciona Tailscale](https://tailscale.com/blog/how-tailscale-works/)
7. [Arquitectura de confianza cero del NIST](https://csrc.nist.gov/publications/detail/sp/800-207/final)
8. [Documento técnico de WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
