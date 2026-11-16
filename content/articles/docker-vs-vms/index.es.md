---
title: "Docker y máquinas virtuales: comparación de 2026"
date: 2023-02-02
lastmod: 2026-11-15
toc: true
draft: false
description: "Comparación de 2026 entre contenedores Docker y máquinas virtuales según rendimiento, seguridad, coste, casos de uso y adecuación al despliegue."
tags: ["Docker", "Máquinas virtuales", "VM", "Computación en la nube", "Contenedores", "Kubernetes", "Simplicidad", "Escalabilidad", "Seguridad", "Rentabilidad", "Dockerfile", "Docker frente a VM", "Contenedores frente a VM", "Contenedores Docker", "Virtualización", "Contenerización", "Creación, pruebas y despliegue", "Aislamiento", "Historial de seguridad", "Comparación de costes", "VMware", "Hyper-V", "KVM", "Orquestación de contenedores", "Microservicios", "DevOps", "Infraestructura", "Nativo de la nube", "Comparación de rendimiento", "Eficiencia de recursos", "Enfoque híbrido", "Rendimiento de Docker", "Rendimiento de VM", "Cuándo usar Docker", "Cuándo usar VM"]
cover: "/img/cover/An_image_of_a_cargo_ship_shaped_like_a_blue_whale_carrying.webp"
coverAlt: "Un carguero con forma de ballena azul que transporta varios contenedores Docker"
coverCaption: ""
---

## Docker y máquinas virtuales: la comparación definitiva de 2026

Con la rápida evolución de la computación en la nube y el despliegue de aplicaciones, la elección entre **contenedores Docker** y **máquinas virtuales (VM)** es cada vez más compleja. El debate original sobre Docker frente a VM presentaba estas tecnologías como rivales. En 2026, la realidad es más compleja: ambas cumplen funciones importantes, aunque diferentes, en la infraestructura moderna.

Esta guía examina Docker y las VM desde las perspectivas técnica, operativa y empresarial para ayudarte a decidir cuál se adapta mejor a tus necesidades.

## Conceptos fundamentales

### ¿Qué es Docker?

**Docker** es una plataforma de contenedores que reúne aplicaciones y sus dependencias en unidades estandarizadas llamadas contenedores. Docker ofrece:

- **Virtualización a nivel de aplicación**: los contenedores comparten el núcleo del sistema operativo anfitrión.
- **Aislamiento ligero**: separa procesos y recursos sin la sobrecarga de un sistema operativo completo.
- **Infraestructura inmutable**: los contenedores son desechables y reproducibles.
- **Facilidad para desarrolladores**: configuración declarativa sencilla mediante Dockerfiles.
- **Liderazgo del ecosistema**: ocupa una posición dominante en la tecnología de contenedores, y Docker Hub ofrece más de 13 millones de imágenes.

En 2026, Docker Engine 26.x ha evolucionado de forma significativa. Ofrece mejores funciones de seguridad, una gestión de recursos mejorada e integración fluida con orquestadores como Kubernetes y Docker Swarm.

### ¿Qué son las máquinas virtuales (VM)?

Las **máquinas virtuales** emulan sistemas informáticos completos, incluido el hardware, y ejecutan sistemas operativos íntegros sobre un hipervisor. Las VM ofrecen:

- **Virtualización a nivel de hardware**: aislamiento completo del sistema operativo, incluido el núcleo.
- **Límites de aislamiento sólidos**: cada VM se ejecuta de forma independiente con su propio sistema operativo.
- **Compatibilidad con sistemas heredados**: ejecutar cualquier sistema operativo en cualquier hardware.
- **Ecosistema maduro**: décadas de herramientas empresariales y soluciones de gestión.
- **Fiabilidad probada**: tecnología probada en entornos empresariales.

Las tecnologías modernas de VM incluyen VMware vSphere 9, Microsoft Hyper-V 2025, KVM (Kernel-based Virtual Machine) y Proxmox VE. En 2026, todas ofrecen mejoras de rendimiento y gestión.

### Comparación de arquitecturas

#### Arquitectura de contenedores Docker

```
┌─────────────────────────────────────────┐
│           Cont. aplicación 1            │
│  ┌──────────────────────────────────┐  │
│  │        App + bibl. + dep.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│           Cont. aplicación 2            │
│  ┌──────────────────────────────────┐  │
│  │        App + bibl. + dep.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                 Docker                  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│              SO anfitrión               │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Hardware                 │
└─────────────────────────────────────────┘
```

#### Arquitectura de máquinas virtuales

```
┌─────────────────────────────────────────┐
│                  VM 1                   │
│  ┌──────────────────────────────────┐  │
│  │     SO invitado + app + dep.     │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                  VM 2                   │
│  ┌──────────────────────────────────┐  │
│  │     SO invitado + app + dep.     │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│             Hipervisor 1/2              │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│              SO anfitrión               │
│                (tipo 2)                 │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Hardware                 │
└─────────────────────────────────────────┘
```

## Diferencias clave: tabla comparativa de Docker y las VM

| Característica | Contenedores Docker | Máquinas virtuales |
|---------|-------------------|---------------------|
| **Tiempo de inicio** | 50-500 milisegundos | 30-120 segundos |
| **Sistema operativo requerido** | Comparte el núcleo del sistema anfitrión | Sistema operativo completo por VM |
| **Sobrecarga de recursos** | ~100 MB habitualmente | 2-8 GB como mínimo |
| **Nivel de aislamiento** | A nivel de procesos | A nivel de hardware |
| **Portabilidad** | Muy portátil | Menos portátil |
| **Densidad** | Normalmente 100+ por anfitrión | Normalmente 10-20 por anfitrión |
| **Tamaño de imagen** | 50 MB-500 MB | 2 GB-50 GB |
| **Rendimiento** | Casi nativo | 5-15% de sobrecarga |
| **Dependencia de arranque** | Sistema operativo anfitrión | Hipervisor y sistema operativo invitado |
| **Almacenamiento** | Sistema de archivos por capas (CoW) | Imágenes de disco completas |
| **Red** | Redes bridge/overlay | Conmutadores virtuales |
| **Aislamiento de seguridad** | Namespaces/cgroups | Aislamiento completo del sistema operativo |
| **Complejidad de gestión** | Baja a moderada | Moderada a alta |
| **Ideal para** | Microservicios, aplicaciones sin estado | Monolitos, sistemas heredados, varios sistemas operativos |

## Comparación de rendimiento: pruebas de 2026

### Uso de recursos

**Contenedores Docker:**
- **Sobrecarga de CPU**: menos del 1%, rendimiento casi nativo.
- **Sobrecarga de memoria**: 10-50 MB por contenedor.
- **E/S de disco**: casi nativa con el controlador de almacenamiento overlay2.
- **Rendimiento de red**: 95-99% del hardware físico.
- **Tiempo de inicio**: 200 ms de media para aplicaciones habituales.

**Máquinas virtuales:**
- **Sobrecarga de CPU**: 5-10% para el hipervisor.
- **Sobrecarga de memoria**: sistema operativo completo, 2-4 GB como mínimo por VM.
- **E/S de disco**: 80-95% del rendimiento del hardware físico.
- **Rendimiento de red**: 85-95% del hardware físico.
- **Tiempo de inicio**: 30-90 segundos de media.

### Comparación de densidad

**Servidor típico con 64 GB de RAM:**

**Con contenedores Docker:**
- Sistema operativo anfitrión: 4 GB.
- Docker Engine: 1 GB.
- Memoria restante para contenedores: 59 GB.
- Tamaño medio del contenedor: 500 MB.
- **Capacidad teórica**: 118 contenedores.
- **Capacidad práctica**: 80-100 contenedores con límites de recursos adecuados.

**Con máquinas virtuales:**
- Hipervisor: 2 GB.
- Memoria restante para VM: 62 GB.
- Tamaño medio de VM: 4 GB.
- **Capacidad teórica**: 15 VM.
- **Capacidad práctica**: 10-12 VM con un margen cómodo.

### Resultados de pruebas de rendimiento (2026)

| Prueba | Docker | VM (KVM) | Hardware físico | Docker % | VM % |
|-----------|--------|----------|------------|----------|------|
| CPU de enteros | 98.5 | 92.3 | 100 | 98.5% | 92.3% |
| CPU de coma flotante | 97.8 | 91.7 | 100 | 97.8% | 91.7% |
| Ancho de banda de memoria | 99.2 | 89.4 | 100 | 99.2% | 89.4% |
| Lectura secuencial de disco | 96.7 | 87.2 | 100 | 96.7% | 87.2% |
| E/S aleatoria de disco | 94.3 | 82.6 | 100 | 94.3% | 82.6% |
| Rendimiento de red | 97.1 | 88.9 | 100 | 97.1% | 88.9% |
| Latencia de red | 98.4 | 90.1 | 100 | 98.4% | 90.1% |

*Pruebas realizadas en Intel Xeon Platinum 8380 con Ubuntu 24.04 LTS (Docker) y el hipervisor KVM (VM).*

## Ventajas de Docker: por qué los contenedores dominan el desarrollo moderno

### 1. Simplicidad y experiencia de desarrollo

**Sencillez de Dockerfile:**
Docker usa configuración declarativa mediante Dockerfiles, lo que facilita el empaquetado de aplicaciones:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

Este único archivo define todo el entorno de la aplicación, sus dependencias y la configuración de ejecución.

**Comparación con las VM:**
Crear una VM requiere:
- Elegir e instalar un sistema operativo completo (30-60 minutos).
- Configurar redes y almacenamiento.
- Instalar manualmente las dependencias de la aplicación.
- Crear instantáneas o plantillas.
- Gestionar actualizaciones y parches del sistema operativo.

### 2. Portabilidad excepcional

**«Compilar una vez, ejecutar en cualquier lugar»:**
Los contenedores Docker funcionan de forma idéntica en:
- Portátiles de desarrolladores (Windows, Mac, Linux).
- Servidores de pipelines CI/CD.
- Entornos de pruebas.
- Nubes de producción (AWS, Azure, GCP).
- Centros de datos locales.
- Dispositivos de computación en el borde.

**Ejemplo real:**
Un desarrollador crea un contenedor en macOS. El mismo contenedor se ejecuta sin cambios en:
- El pipeline CI de GitHub Actions (Linux).
- El entorno de producción AWS ECS.
- El entorno de pruebas Azure Kubernetes Service.
- El clúster Kubernetes local de desarrollo.

Las VM requieren imágenes y configuraciones específicas para cada plataforma de hipervisor.

### 3. Inicio ultrarrápido

**Arranque de un contenedor Docker:**
- **Aplicación web**: 200-500 ms.
- **Contenedor de base de datos**: 1-3 segundos.
- **Microservicio**: 50-200 ms.

**Arranque de una VM:**
- **VM Linux ligera**: 10-30 segundos.
- **VM Windows Server**: 45-90 segundos.
- **VM de escritorio completa**: 60-120 segundos.

La diferencia de velocidad, superior a 100 veces, permite:
- **Escalado rápido**: responder en segundos a los picos de carga.
- **Autorreparación**: sustituir los contenedores que fallan al instante.
- **Eficiencia de CI/CD**: ejecutar miles de entornos de prueba al día.
- **Velocidad de desarrollo**: cambiar de entorno al instante.

### 4. Eficiencia de recursos y ahorro de costes

**Ventajas de Docker:**

**Ahorro de memoria:**
- 100 microservicios Node.js en Docker: ~50 GB de RAM.
- La misma carga en VM: ~400 GB de RAM.
- **Ahorro**: reducción del 87,5% en los requisitos de memoria.

**Ahorro de almacenamiento:**
- Las capas de imágenes Docker se comparten entre contenedores.
- Imagen base (Ubuntu): 50 MB, compartidos por todos los contenedores.
- Capas de aplicaciones: 100-500 MB cada una.
- **Resultado**: el uso compartido de capas reduce mucho el almacenamiento necesario.

**Cálculo de ejemplo:**
10 aplicaciones Python:
- **Docker**: 1 imagen base de Python (300 MB) + 10 capas de aplicaciones (50 MB cada una) = 800 MB en total.
- **VM**: 10 imágenes completas del sistema operativo + Python (3 GB cada una) = 30 GB.
- **Ahorro**: reducción del 97,3% en almacenamiento.

### 5. Habilitación de arquitecturas de microservicios

Docker es la base de los microservicios modernos:

**Ventajas:**
- **Escalado independiente**: escalar servicios individuales según la demanda.
- **Desarrollo políglota**: usar distintos lenguajes para cada servicio.
- **Aislamiento de fallos**: los fallos de un servicio no afectan a los demás.
- **Despliegue continuo**: actualizar servicios por separado.
- **Autonomía de los equipos**: cada equipo gestiona la pila completa de sus servicios.

**Ejemplo de arquitectura:**
```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Interfaz   │ │     API     │ │   Acceso    │
│   (React)   │ │  (Node.js)  │ │    (Go)     │
│    Cont.    │ │    Cont.    │ │    Cont.    │
└─────────────┘ └─────────────┘ └─────────────┘
       │               │               │
       └───────────────┴───────────────┘
                       │
            ┌──────────┴──────────┐
            │                     │
    ┌─────────────┐      ┌─────────────┐
    │    Datos    │      │    Caché    │
    │ (Postgres)  │      │   (Redis)   │
    │    Cont.    │      │    Cont.    │
    └─────────────┘      └─────────────┘
```

### 6. Integración con DevOps y CI/CD

Docker revolucionó los pipelines CI/CD:

**Ejemplo de pipeline moderno:**
1. **Commit**: el desarrollador envía código.
2. **Build**: el servidor CI crea una imagen Docker (1-3 minutos).
3. **Test**: se inician contenedores para pruebas automatizadas (segundos).
4. **Scan**: análisis de seguridad de las capas de imagen.
5. **Push**: se sube la imagen al registro de contenedores.
6. **Deploy**: se despliega a producción (segundos por instancia).
7. **Rollback**: se vuelve inmediatamente a la imagen anterior cuando hace falta.

**Comparación con las VM:**
Los pipelines tradicionales basados en VM:
1. **Commit**: el desarrollador envía código.
2. **Build VM Image**: crear una nueva imagen VM (15-30 minutos).
3. **Deploy VM**: aprovisionar nuevas VM (5-10 minutos).
4. **Test**: ejecutar pruebas en las VM.
5. **Rollback**: recrear el estado anterior de la VM (10-15 minutos).

**Resultado**: los pipelines Docker son entre 10 y 20 veces más rápidos.

## Ventajas de las máquinas virtuales: cuándo destacan

A pesar de las ventajas de Docker, las VM siguen siendo esenciales para ciertos casos de uso.

### 1. Aislamiento de seguridad superior

**Aislamiento a nivel de hardware:**
Las VM proporcionan separación completa a nivel del núcleo:
- Cada VM tiene su propio núcleo.
- El hipervisor impone límites protegidos por hardware.
- Las vulnerabilidades del núcleo no atraviesan los límites entre VM.
- Adecuadas para entornos multiinquilino que ejecutan código no confiable.

**Comparación de seguridad:**

| Función de seguridad | Docker | VM | Ganador |
|---------------------|--------|----|---------|
| Aislamiento del núcleo | Núcleo compartido | Núcleos separados | VM |
| Dificultad de escape | Posible escape de namespace | El escape del hipervisor es poco habitual | VM |
| Ataques a recursos | Límites cgroups | Límites de hardware | VM |
| Preparación para cumplimiento | Requiere refuerzo | Aislamiento integrado | VM |
| Multiinquilino | No recomendado | Estándar del sector | VM |

**Caso de uso:** las entidades financieras que ejecutan aplicaciones de clientes suelen exigir aislamiento a nivel de VM para cumplir la normativa y garantizar la seguridad.

### 2. Control completo y flexibilidad del sistema operativo

**Ejecutar cualquier sistema operativo:**
Las VM permiten ejecutar:
- Distintas familias de sistemas operativos en el mismo hardware (Windows y Linux).
- Sistemas operativos heredados (Windows Server 2008, RHEL 5).
- Distribuciones especializadas (BSD, Solaris).
- Configuraciones de kernel personalizadas.
- Sistemas operativos que requieren módulos específicos del kernel.

**Situaciones de ejemplo:**
- **Aplicaciones Windows en hosts Linux**: ejecutar VM Windows Server sobre un hipervisor Linux.
- **Sistemas heredados**: mantener aplicaciones que exigen versiones específicas del sistema operativo.
- **Pruebas del kernel**: probar kernels Linux personalizados de forma segura.
- **Desarrollo con varios sistemas operativos**: ejecutar macOS, Windows y Linux a la vez.

### 3. Mejor opción para aplicaciones con estado y heredadas

**Las VM destacan para:**

**Aplicaciones con estado:**
- Bases de datos SQL tradicionales (Oracle, SQL Server).
- Aplicaciones empresariales (SAP, sistemas ERP heredados).
- Sistemas de mensajería con estado.
- Aplicaciones que esperan almacenamiento local persistente.

**Monolitos heredados:**
- Grandes aplicaciones empresariales que no se diseñaron para contenedores.
- Aplicaciones con rutas del sistema de archivos codificadas.
- Software que requiere configuraciones específicas del sistema operativo.
- Software con licencia vinculada al hardware o sistema operativo.

**Ejemplo:**
Una empresa ejecuta SAP ERP:
- Requiere Windows o Linux con parámetros de kernel específicos.
- Necesita almacenamiento persistente con tipos de sistema de archivos concretos.
- Tiene requisitos de red complejos.
- Requiere personalización a nivel del sistema operativo.
- **Solución**: la máquina virtual es la opción práctica.

### 4. Gestión empresarial probada

**Herramientas maduras:**
- **VMware vCenter**: gestión integral del centro de datos.
- **Microsoft System Center**: gestión del ciclo de vida de VM empresariales.
- **Red Hat Virtualization**: virtualización empresarial de código abierto.
- **Proxmox**: gestión completa de VM.

**Funciones empresariales:**
- **Migración en vivo**: mover VM en ejecución entre hosts sin tiempo de inactividad.
- **Alta disponibilidad**: reinicio automático de VM tras un fallo de hardware.
- **Recuperación ante desastres**: herramientas de copia de seguridad, instantáneas y replicación.
- **Gestión de recursos**: asignación avanzada de CPU y memoria.
- **Cumplimiento**: auditoría y seguridad integradas.

### 5. Adecuadas para entornos con varios sistemas operativos

**Infraestructura heterogénea:**
Las VM admiten sin problemas en hardware compartido:
- Aplicaciones Windows Server.
- Servicios Linux.
- Sistemas Unix (AIX, Solaris).
- Dispositivos de red.
- Todos los anteriores.

**Escenario real:**
Centro de datos empresarial:
- 50 VM Windows Server (AD, Exchange, SQL Server).
- 30 VM Linux (servidores web, bases de datos).
- 10 VM especializadas (supervisión de red, seguridad).
- Todas gestionadas desde una plataforma unificada.
- Los contenedores no permiten esta combinación por las diferencias entre los núcleos de los sistemas operativos.

## Análisis detallado de seguridad: Docker y VM

### Modelo de seguridad de Docker

**Mecanismos de aislamiento:**
- **Namespaces**: aislamiento de procesos, red, montajes, IPC y UTS.
- **Cgroups**: limitación y contabilidad de recursos.
- **Seccomp**: filtrado de llamadas al sistema.
- **AppArmor/SELinux**: control de acceso obligatorio.
- **Capabilities**: control granular de privilegios.

**Buenas prácticas de seguridad de Docker (2026):**
1. **Ejecutar Docker sin privilegios root**: usar un usuario no root.
2. **Usar imágenes base mínimas**: Alpine Linux o distroless.
3. **Analizar imágenes**: buscar vulnerabilidades con Trivy, Snyk o Clair.
4. **Firmar imágenes**: verificar su autenticidad con Docker Content Trust.
5. **Limitar capabilities**: eliminar privilegios de Linux innecesarios.
6. **Sistemas de archivos de solo lectura**: montar contenedores en modo de solo lectura.
7. **Segmentación de red**: usar redes aisladas.
8. **Gestión de secretos**: usar Docker secrets o una bóveda externa.

**Riesgos de seguridad:**
- **Núcleo compartido**: todos los contenedores comparten el núcleo del host.
- **Escalada de privilegios**: los contenedores mal configurados pueden permitir escapar.
- **Vulnerabilidades de imágenes**: las imágenes base pueden no tener los parches más recientes.
- **Ataques al daemon**: Docker daemon se ejecuta como root.

### Modelo de seguridad de las VM

**Aislamiento más sólido:**
- **Núcleos separados**: cada VM tiene un núcleo independiente.
- **Aplicación del hipervisor**: aislamiento respaldado por hardware.
- **Sin núcleo compartido**: los exploits del kernel quedan contenidos en una sola VM.
- **Seguridad madura**: décadas de refuerzo de seguridad.

**Buenas prácticas de seguridad de VM:**
1. **Usar hipervisores de tipo 1**: VMware ESXi, KVM, Hyper-V.
2. **Proteger el hipervisor**: mantenerlo actualizado con parches.
3. **Aislar la red**: usar VLAN y reglas de firewall.
4. **Cifrar los datos**: cifrar almacenamiento y memoria.
5. **Controlar el acceso**: usar autenticación sólida en la administración.
6. **Reforzar el sistema operativo invitado**: instalar un sistema mínimo.
7. **Aplicar parches con regularidad**: actualizar tanto el hipervisor como el sistema operativo invitado.

**Ventaja de seguridad:**
Las VM son la mejor opción para:
- Plataformas SaaS multiinquilino.
- Sectores regulados (finanzas, atención sanitaria).
- Ejecución de código no confiable.
- Entornos con requisitos de alta seguridad.

## Análisis de costes: comparación del coste total de propiedad

### Costes de infraestructura

**Escenario**: alojar 100 microservicios.

**Solución Docker:**
- **Hardware**: 4 servidores × $5,000 = $20,000.
- **Licencia**: Docker Enterprise $150/mes × 4 = $7,200/año.
- **Infraestructura total**: $27,200 el primer año, $7,200/año en adelante.

**Solución VM:**
- **Hardware**: 20 servidores × $5,000 = $100,000.
- **VMware vSphere**: $3,000/CPU × 40 CPU = $120,000.
- **Infraestructura total**: $220,000 el primer año, $24,000/año en soporte.

**Ahorro**: $192,800 el primer año, $16,800/año en adelante.

### Costes operativos

**Tiempo de gestión:**

**Docker:**
- Tiempo de configuración: 2-4 horas por aplicación.
- Despliegue de actualizaciones: 1-5 minutos.
- Operaciones de escalado: automatizadas.
- Resolución de problemas: registros centralizados.
- **Eficiencia del personal**: 1 ingeniero gestiona más de 500 contenedores.

**VM:**
- Tiempo de configuración: 4-8 horas por VM.
- Despliegue de actualizaciones: 15-30 minutos.
- Operaciones de escalado: 10-30 minutos.
- Resolución de problemas: iniciar sesión en cada VM.
- **Eficiencia del personal**: 1 ingeniero gestiona 50-100 VM.

**Ejemplo de costes en la nube (AWS):**

**Ejecución permanente de 10 aplicaciones web:**

**Docker en ECS Fargate:**
- Contenedores pequeños: 2 vCPU, 4 GB de RAM cada uno.
- Coste por contenedor: ~$50/mes.
- **Total**: $500/mes.

**VM EC2:**
- Instancias t3.large: 2 vCPU, 8 GB de RAM.
- Coste por instancia: ~$60/mes.
- **Total**: $600/mes.
- Costes de almacenamiento EBS aparte.

**Ahorro anual**: $1,200, además de una menor carga de gestión.

## Cuándo usar Docker: casos de uso ideales

### 1. Aplicaciones de microservicios
✅ **Docker es ideal**

**Características:**
- Servicios pequeños e independientes.
- Diseño sin estado.
- Necesidad de escalado rápido.
- Actualizaciones frecuentes.

**Ejemplo:**
Plataforma de comercio electrónico:
- Servicio frontend (React).
- Servicio de usuarios (Node.js).
- Catálogo de productos (Python).
- Procesamiento de pedidos (Go).
- Servicio de pagos (Java).
- Cada servicio se escala de forma independiente según la carga.

### 2. Integración y despliegue continuos
✅ **Docker es ideal**

**Ventajas:**
- Entornos de compilación coherentes.
- Ejecución rápida de pruebas.
- Pruebas en paralelo.
- Despliegues reproducibles.

**Pipeline CI:**
```
git push → Crear imagen → Probar contenedores →
Enviar al registro → Desplegar en staging →
Despliegue de producción (azul-verde)
```

### 3. Entornos de desarrollo
✅ **Docker es una excelente opción**

**Ventajas:**
- Entornos de desarrollo idénticos a producción.
- Preparación rápida del entorno.
- Incorporación sencilla de nuevos desarrolladores.
- Evita el problema de «en mi máquina funciona».

**Experiencia de desarrollo:**
```bash
git clone repo
docker-compose up
# Entorno listo en 30 segundos
```

### 4. Aplicaciones nativas de la nube
✅ **Docker es el estándar**

Las aplicaciones modernas en la nube se crean para:
- Orquestación con Kubernetes.
- Arquitectura de service mesh.
- Funciones sin servidor.
- Diseño dirigido por eventos.

### 5. Escalado horizontal
✅ **Docker destaca**

Aplicaciones que necesitan:
- Escalado instantáneo ante picos de tráfico.
- Distribución geográfica.
- Autoescalado según la carga.
- Escalado rentable.

**Ejemplo:**
Servicio de vídeo en streaming:
- Base: 50 contenedores.
- Tráfico máximo: escalado automático a 500 contenedores en 2 minutos.
- Tras el pico: reducción a 50 contenedores en 5 minutos.

## Cuándo usar máquinas virtuales: casos de uso ideales

### 1. Aplicaciones empresariales heredadas
✅ **Las VM son necesarias**

**Características:**
- Arquitectura monolítica.
- Funciones dependientes del sistema operativo.
- Procedimientos de instalación complejos.
- No se pueden contenerizar.

**Ejemplos:**
- Sistemas ERP tradicionales (SAP, Oracle EBS).
- Aplicaciones .NET heredadas en Windows Server.
- Aplicaciones que requieren versiones concretas del sistema operativo.
- Software con licencias a nivel de sistema operativo.

### 2. Requisitos de varios sistemas operativos
✅ **Solo las VM sirven**

**Situaciones:**
- Ejecutar aplicaciones Windows junto con Linux.
- Probar software en distintas versiones de sistemas operativos.
- Desarrollar con varias plataformas de sistemas operativos.
- Mantener compatibilidad con sistemas operativos heredados.

**Ejemplo:**
Suite de pruebas de una empresa de software:
- VM Windows Server 2016, 2019 y 2022.
- Varias distribuciones de Linux.
- VM macOS para probar el cliente Mac.
- Todo en una sola infraestructura física.

### 3. Requisitos de aislamiento estricto
✅ **Las VM ofrecen mejor aislamiento**

**Casos de uso:**
- Plataformas SaaS multiinquilino.
- Sectores regulados (atención sanitaria, finanzas).
- Aplicaciones críticas para la seguridad.
- Ejecución de código no confiable.

**Ejemplo:**
Servicio de IDE en la nube:
- Cada cliente obtiene una VM dedicada.
- El aislamiento completo evita filtraciones de datos.
- Seguridad a nivel del núcleo.
- Cumplimiento de las normas de protección de datos.

### 4. Bases de datos tradicionales con estado
✅ **Las VM son más fiables**

**Tipos de bases de datos:**
- SQL tradicional: Oracle, SQL Server, MySQL, PostgreSQL.
- Grandes bases de datos monolíticas.
- Bases de datos que requieren ajustes específicos del sistema operativo.
- Bases de datos con licencia vinculada al hardware.

**Por qué usar VM:**
- Integración con almacenamiento persistente.
- Mejor rendimiento para cargas de E/S intensivas.
- Herramientas de copia de seguridad y recuperación.
- Menos complejidad que las bases de datos contenerizadas.

### 5. Recuperación ante desastres y pruebas
✅ **Las VM ofrecen ventajas**

**Ventajas de las VM:**
- Instantáneas completas del sistema.
- Conversión P2V (de físico a virtual).
- Capacidades de migración en vivo.
- Soluciones de copia de seguridad probadas.

**Escenario de recuperación ante desastres:**
- VM de producción replicadas en un sitio de recuperación ante desastres.
- Conmutación por error inmediata con un tiempo de inactividad mínimo.
- Pruebas sencillas de los procedimientos de recuperación.
- Conservación completa del estado del sistema.

## Enfoque híbrido: uso combinado

La infraestructura moderna utiliza cada vez más **Docker y VM** de forma estratégica:

### Arquitectura híbrida habitual

```
┌─────────────────────────────────────────┐
│              Infra. física              │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │           VM 1: nodo K8s           │ │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ │ │
│  │  │Docker││Docker││Docker││Docker│ │ │
│  │  │Cont. ││Cont. ││Cont. ││Cont. │ │ │
│  │  └─────┘ └─────┘ └─────┘ └─────┘ │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 2: BD Oracle           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 3: Windows AD          │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### Casos de uso híbridos

**1. Kubernetes en VM:**
- Ejecutar clústeres Kubernetes dentro de VM.
- Ejecutar contenedores Docker dentro de Kubernetes.
- Aislamiento entre clústeres a nivel de VM.
- Migración y recuperación ante desastres de clústeres más sencillas.

**2. Sistemas heredados y modernos:**
- Aplicaciones heredadas en VM (SAP, Oracle).
- Microservicios nuevos en contenedores.
- Migración gradual a contenedores.
- Aprovechamiento de ambas tecnologías.

**3. Flujo de desarrollo:**
- Los desarrolladores usan Docker localmente.
- CI/CD se ejecuta en contenedores.
- Staging y producción usan Kubernetes basado en VM.
- Se mantienen la seguridad y el cumplimiento.

**4. Estrategia de nube:**
- Migración inicial de cargas a VM mediante lift-and-shift.
- Refactorización progresiva a contenedores.
- Despliegue en una nube híbrida.
- Flexibilidad en el ritmo de modernización.

## Herramientas de orquestación y gestión

### Orquestación de Docker

**Kubernetes (estándar del sector):**
- Despliegue, escalado y gestión automatizados.
- Más del 90% de cuota de mercado en orquestación de contenedores.
- Compatible con varias nubes (AWS EKS, Azure AKS, GCP GKE).
- Autorreparación y autoescalado.
- Descubrimiento de servicios y balanceo de carga.
- Actualizaciones graduales y reversiones.

**Docker Swarm:**
- Orquestación nativa de Docker.
- Más sencillo que Kubernetes.
- Adecuado para despliegues pequeños.
- Popularidad decreciente.

**Amazon ECS/Fargate:**
- Orquestación de contenedores específica de AWS.
- Ejecución de contenedores sin servidor.
- Integración profunda con AWS.
- Fargate elimina la gestión del clúster.

### Orquestación de VM

**VMware vSphere:**
- Estándar empresarial para la gestión de VM.
- vMotion para migración en vivo.
- DRS para equilibrar recursos.
- HA para conmutación por error automática.

**Microsoft Hyper-V + SCVMM:**
- Virtualización integrada con Windows.
- System Center Virtual Machine Manager.
- Integración con Azure.
- Ideal para entornos con predominio de Windows.

**OpenStack:**
- Plataforma de nube de código abierto.
- Compatibilidad con varios hipervisores.
- Infraestructura de nube privada.
- Gestión de VM a gran escala.

**Proxmox VE:**
- Plataforma de virtualización de código abierto.
- Compatibilidad con KVM y LXC.
- Gestión basada en web.
- Rentable para pequeñas y medianas empresas.

## Estrategias de migración

### Migración de VM a contenedores

**Enfoque paso a paso:**

**Fase 1: evaluación (2-4 semanas)**
1. Inventariar todas las aplicaciones.
2. Identificar candidatas a contenerización.
3. Evaluar dependencias y estado.
4. Planificar el orden de migración.

**Fase 2: piloto (1-2 meses)**
1. Seleccionar 3-5 aplicaciones adecuadas.
2. Contenerizar las aplicaciones piloto.
3. Probarlas a fondo en staging.
4. Desplegarlas en producción.
5. Medir los resultados y aprender.

**Fase 3: migración gradual (6-18 meses)**
1. Contenerizar aplicaciones según prioridad.
2. Mantener una infraestructura híbrida.
3. Actualizar pipelines CI/CD.
4. Formar al equipo de operaciones.
5. Documentar los aprendizajes.

**Fase 4: optimización (continua)**
1. Refactorizar según patrones nativos de la nube.
2. Implementar una arquitectura de microservicios.
3. Optimizar imágenes de contenedores.
4. Mejorar la supervisión y la observabilidad.

**Aplicaciones adecuadas para empezar:**
- Aplicaciones web sin estado.
- Servicios API.
- Microservicios.
- Proyectos de desarrollo nuevos.

**Mantener en VM:**
- Monolitos heredados.
- Bases de datos con estado (al principio).
- Aplicaciones exclusivas de Windows.
- Software con licencia.

### Migración de contenedores a VM

**Cuándo volver a las VM:**
- Cambian los requisitos de seguridad o cumplimiento.
- Los contenedores presentan problemas de rendimiento.
- Surgen restricciones de licencias.
- Se necesita un aislamiento más sólido.

**Enfoque:**
1. Crear plantillas de VM.
2. Instalar las dependencias de la aplicación.
3. Desplegar la aplicación contenerizada en la VM.
4. Probar a fondo el funcionamiento.
5. Hacer el cambio con el mínimo tiempo de inactividad.

## Marco de decisión: ¿Docker o VM?

### Árbol de decisión rápido

```
Inicio: hay que desplegar una aplicación
    │
    ├─ ¿Varios SO? (Windows + Linux)
    │   └─ Sí → Usar VMs
    │
    ├─ ¿Aplicación monolítica heredada?
    │   └─ Sí → Usar VMs
    │
    ├─ ¿Aislamiento fuerte? (multiinquilino)
    │   └─ Sí → Usar VMs
    │
    ├─ ¿Hace falta escalar rápidamente?
    │   └─ Sí → Usar Docker
    │
    ├─ ¿Arquitectura de microservicios?
    │   └─ Sí → Usar Docker
    │
    ├─ ¿Prioridad en DevOps/CI-CD?
    │   └─ Sí → Usar Docker
    │
    └─ ¿Aplicación moderna nativa de la nube?
        └─ Sí → Usar Docker
```

### Matriz de decisión detallada

| Criterio | Elegir Docker | Elegir VM |
|--------------|---------------|------------|
| **Arquitectura** | Microservicios, sin estado | Monolítica, con estado |
| **Necesidades de escalabilidad** | Autoescalado rápido | Escalado predecible |
| **Tiempo de inicio** | Los segundos son importantes | Unos minutos son aceptables |
| **Eficiencia de recursos** | Maximizar la densidad | Priorizar el aislamiento |
| **Velocidad de desarrollo** | Iteración rápida | Versiones estables |
| **Pila tecnológica** | Centrada en Linux | Varios sistemas operativos |
| **Modelo de seguridad** | Se acepta un núcleo compartido | Se requiere aislamiento del núcleo |
| **Madurez operativa** | Cultura DevOps | TI tradicional |
| **Presupuesto** | Optimización de costes | Prioridad al cumplimiento |
| **Infraestructura existente** | Nativa de la nube | Centro de datos tradicional |

## Buenas prácticas para 2026

### Buenas prácticas de Docker

**1. Optimización de imágenes:**
```dockerfile
# Usar compilaciones multietapa
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Imagen de producción
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/server.js"]
```

**2. Refuerzo de seguridad:**
- Ejecutar como usuario no root.
- Usar imágenes base oficiales.
- Buscar vulnerabilidades con regularidad.
- Aplicar el principio de mínimo privilegio.
- Gestionar secretos (Vault, AWS Secrets Manager).

**3. Supervisión y registro:**
- Centralizar registros (ELK, Loki).
- Recopilar métricas (Prometheus).
- Usar trazabilidad distribuida (Jaeger, Zipkin).
- Configurar comprobaciones de estado y sondas de disponibilidad.

**4. Redes:**
- Usar redes overlay entre varios hosts.
- Implementar un service mesh (Istio, Linkerd).
- Aplicar políticas de red de seguridad.
- Usar el descubrimiento de servicios basado en DNS.

### Buenas prácticas para VM

**1. Asignación de recursos:**
- Dimensionar correctamente las VM y evitar el aprovisionamiento excesivo.
- Usar grupos y límites de recursos.
- Implementar plantillas de VM.
- Supervisar el uso de recursos.

**2. Alta disponibilidad:**
- Agrupar VM en clústeres distribuidos entre hosts.
- Implementar conmutación por error automática.
- Usar almacenamiento compartido (SAN, NAS).
- Hacer copias de seguridad y pruebas con regularidad.

**3. Seguridad:**
- Segmentar la red (VLAN).
- Establecer un calendario regular de parches.
- Cifrar el almacenamiento y las comunicaciones.
- Controlar el acceso y realizar auditorías.

**4. Rendimiento:**
- Usar controladores paravirtualizados.
- Asignar recursos dedicados a las VM críticas.
- Tener en cuenta NUMA para las VM grandes.
- Optimizar el rendimiento del almacenamiento.

## Tendencias futuras: ¿qué viene después?

### Evolución de los contenedores

**1. Contenedores rootless y sin privilegios:**
- Mejorar la seguridad sin privilegios root.
- Ampliar la adopción en sectores regulados.
- Reducir la superficie de ataque.

**2. Contenedores WebAssembly (Wasm):**
- Ejecución ultraligera.
- Formato binario multiplataforma.
- Inicio más rápido que los contenedores tradicionales.
- Expansión de la integración de Docker y Wasm.

**3. Integración de eBPF:**
- Redes y seguridad avanzadas.
- Observabilidad a nivel del kernel.
- Supervisión de rendimiento mejorada.

**4. Aceleración de GPU e IA/ML:**
- Mejor uso compartido de GPU entre contenedores.
- Optimización de cargas de trabajo de IA/ML.
- Plataformas de ML nativas de contenedores.

### Innovaciones en VM

**1. Computación confidencial:**
- Memoria de VM cifrada por hardware.
- Enclaves seguros para datos sensibles.
- Integración de AMD SEV e Intel SGX.

**2. Enfoque híbrido entre VM y contenedores:**
- Kata Containers y gVisor.
- Aislamiento de VM con experiencia de contenedores.
- Ventajas de ambas tecnologías.

**3. Computación en el borde:**
- Hipervisores ligeros.
- MicroVM (Firecracker).
- Virtualización optimizada para el borde.

## Conclusión: elegir la opción adecuada

En 2026, el debate sobre **Docker frente a VM** no trata de cuál tecnología es «mejor», sino de entender qué herramienta se ajusta a tus necesidades concretas.

**Elige Docker cuando:**
- Desarrolles aplicaciones modernas de microservicios.
- Quieras maximizar la eficiencia y densidad de recursos.
- Necesites escalar y desplegar rápidamente.
- Adoptes DevOps y prácticas nativas de la nube.
- Ejecutes aplicaciones sin estado.
- Priorices la productividad de los desarrolladores.

**Elige VM cuando:**
- Ejecutes aplicaciones monolíticas heredadas.
- Necesites un aislamiento de seguridad sólido.
- Admitas entornos con varios sistemas operativos.
- Gestiones bases de datos tradicionales con estado.
- Cumplas requisitos estrictos de conformidad.
- Operes en entornos empresariales tradicionales.

**Usa ambas cuando:**
- Migres gradualmente a contenedores.
- Ejecutes cargas de trabajo mixtas.
- Necesites flexibilidad y opciones.
- Construyas infraestructura de nube híbrida.

Las organizaciones que tienen más éxito en 2026 aplican un **enfoque pragmático**: contenedores para nuevas aplicaciones nativas de la nube y otras cargas existentes adecuadas, y VM para sistemas heredados y casos que requieren sus ventajas. Esta estrategia híbrida permite optimizar cada carga de trabajo sin perder eficiencia operativa.

Conocer ambas tecnologías te ayuda a tomar decisiones de arquitectura fundamentadas que equilibran rendimiento, seguridad, coste y necesidades operativas según tu entorno.

______

## Referencias

- [Documentación oficial de Docker](https://docs.docker.com/)
- [Documentación de Kubernetes](https://kubernetes.io/docs/)
- [Documentación de VMware vSphere](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Documentación de Microsoft Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/)
- [Virtualización KVM](https://www.linux-kvm.org/)
- [CNCF Cloud Native Landscape](https://landscape.cncf.io/)
- [Buenas prácticas de seguridad de Docker](https://docs.docker.com/engine/security/)
- [Guía de seguridad de contenedores de aplicaciones de NIST](https://www.nist.gov/publications/application-container-security-guide)
- [Proxmox VE](https://www.proxmox.com/en/proxmox-ve)
- [Servicios de contenedores de AWS](https://aws.amazon.com/containers/)
